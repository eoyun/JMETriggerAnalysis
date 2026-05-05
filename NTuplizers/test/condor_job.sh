#!/bin/bash
set -euo pipefail

# ----------------------------------------------------------------------
# Run the *whole* job inside the CMS EL8 container when executed on EL9.
# This avoids:
#  - SCRAM el8-on-el9 runtime warnings/errors
#  - xrdfs/xrdcp picking host libs (e.g. libreadline.so.7 missing)
# ----------------------------------------------------------------------
if [[ -f /etc/redhat-release ]] && grep -qE 'AlmaLinux.*release 9|Red Hat.*release 9|CentOS Stream.*9' /etc/redhat-release; then
  if command -v cmssw-el8 >/dev/null 2>&1; then
    echo "[INFO] Host is EL9; re-exec inside cmssw-el8 container..."
    exec cmssw-el8 -- "$0" "$@"
  fi
fi

PROCESS="${1:?PROCESS missing}"
START_SKIP="${2:?START_SKIP missing}"
STEP="${3:?STEP missing}"
DATE_TAG="${4:?DATE_TAG missing}"

FILE_EVT=1000

mapfile -t filelist < vbfinv.dat

[[ "${PROCESS}" =~ ^[0-9]+$ ]] || { echo "PROCESS not numeric: ${PROCESS}"; exit 2; }
[[ "${START_SKIP}" =~ ^[0-9]+$ ]] || { echo "START_SKIP not numeric: ${START_SKIP}"; exit 2; }
[[ "${STEP}" =~ ^[0-9]+$ ]] || { echo "STEP not numeric: ${STEP}"; exit 2; }

SKIP=$(( START_SKIP + STEP * PROCESS ))
IDX=$(printf "%05d" "${SKIP}")

DATA_FILE=$((SKIP/FILE_EVT))
START_SKIP_IN_FILE=$((SKIP%FILE_EVT))

if (( DATA_FILE < 0 || DATA_FILE >= ${#filelist[@]} )); then
    echo "DATA_FILE out of range: ${DATA_FILE}"
    exit 3
fi

INPUT_FILE="${filelist[$DATA_FILE]}"

echo "input is $INPUT_FILE"

echo "=== Processing events ${SKIP} -> $((SKIP+STEP-1)) (Process=${PROCESS}) ==="

WORKDIR="${_CONDOR_SCRATCH_DIR:-$(pwd)}"
cd "${WORKDIR}"
echo "WORKDIR=${WORKDIR}"
echo "OS: $(cat /etc/redhat-release || true)"
echo "uname: $(uname -a || true)"

# X509 proxy sanity (needed for EOS write access via xrootd)
echo "X509_USER_PROXY=${X509_USER_PROXY:-<unset>}"
if [[ -z "${X509_USER_PROXY:-}" || ! -r "${X509_USER_PROXY}" ]]; then
  echo "[ERROR] X509 proxy is missing or not readable inside the job."
  exit 88
fi
if command -v voms-proxy-info >/dev/null 2>&1; then
  echo "=== voms-proxy-info (summary) ==="
  voms-proxy-info -timeleft || true
  voms-proxy-info -identity || true
fi

# ----------------------------------------------------------------------
# IMPORTANT: Use EOS CMS user area (X509-friendly) instead of eosuser/cernbox home.
# /eos/home-y/... often requires different auth (and triggers 'public access level restriction').
# ----------------------------------------------------------------------
EOS_XROOTD="root://eosuser.cern.ch"
EOS_DIR="/eos/cms/store/user/yeo/Phase2/${DATE_TAG}"
EOS_DIR_XRD="${EOS_XROOTD}//${EOS_DIR}"
AFS_DIR="/afs/cern.ch/user/y/yeo/phase2/CMSSW_16_0_0_pre3/src/JMETriggerAnalysis/NTuplizers/test/260206_vbf"

echo "EOS_DIR=${EOS_DIR}"
echo "EOS_DIR_XRD=${EOS_DIR_XRD}"

# CMSSW setup
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=el8_amd64_gcc13

cd /afs/cern.ch/user/y/yeo/phase2/CMSSW_16_0_0_pre3/src
eval "$(scramv1 runtime -sh)"

# Ensure we use CMSSW-provided xrootd clients
XROOTD_BASE="$(scram tool info xrootd 2>/dev/null | awk -F= '/^XROOTD_BASE=/{print $2}' | tail -n 1)"
if [[ -n "${XROOTD_BASE}" && -d "${XROOTD_BASE}/bin" ]]; then
  export PATH="${XROOTD_BASE}/bin:${PATH}"
  [[ -d "${XROOTD_BASE}/lib64" ]] && export LD_LIBRARY_PATH="${XROOTD_BASE}/lib64:${LD_LIBRARY_PATH:-}"
  [[ -d "${XROOTD_BASE}/lib"   ]] && export LD_LIBRARY_PATH="${XROOTD_BASE}/lib:${LD_LIBRARY_PATH:-}"
fi
echo "which xrdfs: $(command -v xrdfs || echo '<not found>')"
echo "which xrdcp: $(command -v xrdcp || echo '<not found>')"

cd "${WORKDIR}"

echo "=== Running cmsRun in scratch ==="
cmsRun jmeTriggerNTuple_L1Only_cfg.py \
  maxEvents="${STEP}" \
  skipEvents="${START_SKIP_IN_FILE}" \
  inputFiles="${INPUT_FILE}"\
  output="L1_output_${IDX}.root"

cmsRun jmeTriggerNTuple_cfg.py track=LST    inputFiles="file:L1_output_${IDX}.root" output="out_LST_${IDX}.root"
cmsRun jmeTriggerNTuple_cfg.py track=MkFit  inputFiles="file:L1_output_${IDX}.root" output="out_MkFit_${IDX}.root"
cmsRun jmeTriggerNTuple_cfg.py track=both   inputFiles="file:L1_output_${IDX}.root" output="out_both_${IDX}.root"
cmsRun jmeTriggerNTuple_cfg.py track=menu   inputFiles="file:L1_output_${IDX}.root" output="out_menu_${IDX}.root"
cmsRun jmeTriggerNTuple_cfg.py              inputFiles="file:L1_output_${IDX}.root" output="out_default_${IDX}.root"

rm -f Phase2*HLT.root "L1_output_${IDX}.root" || true

# Make remote EOS directory (best-effort)
#if command -v xrdfs >/dev/null 2>&1; then
#  echo "xrdfs eosuser.cern.ch mkdir -p ${EOS_DIR}"
#  xrdfs eosuser.cern.ch mkdir -p "${EOS_DIR}" || echo "[WARN] xrdfs mkdir failed (will try xrdcp anyway)."
#fi

stageout_ok=1
for f in out_*_"${IDX}".root; do
  echo "cp ${f} -> ${AFS_DIR}/${f}"
  if cp "${f}" "${AFS_DIR}/${f}"; then
    rm -f "${f}"
  else
    echo "[ERROR] xrdcp failed for ${f}"
    stageout_ok=0
  fi
done

if [[ "${stageout_ok}" -ne 1 ]]; then
  echo "[ERROR] One or more outputs failed to transfer. Keeping local files in ${WORKDIR} for debugging."
  exit 90
fi

echo "=== Done. Outputs staged to EOS (/eos/cms/store/user/...) and local copies removed. ==="
