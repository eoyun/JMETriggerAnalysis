#!/bin/bash
# one era group per job: hadd in the scratch dir, drop the duplicated
# bookkeeping keys, then copy to EOS
KEY=$1
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/setup.sh
cd $_CONDOR_SCRATCH_DIR
NFILES=$(wc -l < ${KEY}.txt)
echo "merging ${NFILES} files into ${KEY}.root"
# -k : skip corrupt/missing inputs (some jobs die on XRootD and leave stubs)
# -n : cap simultaneously open files -> hadd runs in several passes
hadd -f -k -n 200 ${KEY}_raw.root $(cat ${KEY}.txt)
STATUS=$?
echo "hadd exit status ${STATUS}"
if [ ${STATUS} -ne 0 ]; then
    echo "FATAL: hadd failed, not copying"
    exit 1
fi
# Histograms merge, but TNamed does not: every pass re-copies the bookkeeping
# keys of every input, so they pile up quadratically (2025D: 1874 files in 10
# passes -> a 179 MB file whose key list alone took minutes to read). Keep one
# copy of each key -- the newest cycle is the fully merged one.
python3 dedup_keys.py ${KEY}_raw.root ${KEY}.root
if [ $? -ne 0 ] || [ ! -s ${KEY}.root ]; then
    echo "FATAL: dedup step failed, not copying"
    exit 1
fi
ls -l ${KEY}_raw.root ${KEY}.root
mkdir -p /eos/home-y/yeo/rdf/output/hadd_files
cp ${KEY}.root /eos/home-y/yeo/rdf/output/hadd_files/${KEY}.root
echo "copied to /eos/home-y/yeo/rdf/output/hadd_files/${KEY}.root"
