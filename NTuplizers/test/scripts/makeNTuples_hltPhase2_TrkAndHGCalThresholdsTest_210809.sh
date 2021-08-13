#!/bin/bash -e

if [ $# -ne 1 ]; then
  printf "\n%s\n\n" ">> argument missing - specify path to output directory"
  exit 1
fi

NEVT=-1
ODIR=${1}

if [ -d ${ODIR} ]; then
  printf "%s\n" "output directory already exists: ${ODIR}"
  exit 1
fi

declare -A samplesMap

# VBF H(125)->Invisible
samplesMap["Phase2HLTTDR_VBF_HToInvisible_14TeV_NoPU"]="/VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-NoPU_111X_mcRun4_realistic_T15_v1-v1/FEVT"
samplesMap["Phase2HLTTDR_VBF_HToInvisible_14TeV_PU140"]="/VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU140_111X_mcRun4_realistic_T15_v1_ext1-v2/FEVT"
samplesMap["Phase2HLTTDR_VBF_HToInvisible_14TeV_PU200"]="/VBF_HToInvisible_M125_14TeV_powheg_pythia8_TuneCP5/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT"

recoKeys=(
  HLT_TRKv06p1_TICL
  HLT_75e33_TrkPtX1p00_HGCEnX1p00
  HLT_75e33_TrkPtX1p25_HGCEnX1p25
  HLT_75e33_TrkPtX1p50_HGCEnX1p50
  HLT_75e33_TrkPtX1p75_HGCEnX1p75
  HLT_75e33_TrkPtX2p00_HGCEnX2p00
  HLT_75e33_TrkPtX1p50_HGCEnX1p00
  HLT_75e33_TrkPtX2p00_HGCEnX1p00
  HLT_75e33_TrkPtX1p00_HGCEnX1p50
  HLT_75e33_TrkPtX1p00_HGCEnX2p00
  HLT_75e33_TrkPtX9p99_HGCEnX9p99
  HLT_75e33_TrkPtX9p99_HGCEnX1p00
  HLT_75e33_TrkPtX1p00_HGCEnX9p99
)

# additional options for bdriver
opts=""

for recoKey in "${recoKeys[@]}"; do
  python jmeTriggerNTuple_cfg.py dumpPython=.tmp_${recoKey}_cfg.py numThreads=1 reco=${recoKey} trkdqm=1 pvdqm=1 pfdqm=1

  for sampleKey in ${!samplesMap[@]}; do
    sampleName=${samplesMap[${sampleKey}]}

    # number of events per sample
    numEvents=${NEVT}
    if [[ ${sampleKey} == *MinBias* ]]; then
      numEvents=2000000
    fi

    bdriver -c .tmp_${recoKey}_cfg.py --customize-cfg -m ${numEvents} -n 250 --cpus 1 --mem 4000 --time 10800 ${opts} \
      -d ${sampleName} -p 0 -o ${ODIR}/${recoKey}/${sampleKey} \
      --customise-commands \
       '# output [TFileService]' \
       "if hasattr(process, 'TFileService'):" \
       '  process.TFileService.fileName = opts.output'

    unset numEvents sampleName
  done
  unset sampleKey

  rm -f .tmp_${recoKey}_cfg.py
done
unset recoKey opts recoKeys samplesMap NEVT ODIR
