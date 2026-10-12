#!/bin/bash
# one era group per job: hadd in the scratch dir, then copy to EOS
KEY=$1
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/setup.sh
cd $_CONDOR_SCRATCH_DIR
NFILES=$(wc -l < ${KEY}.txt)
echo "merging ${NFILES} files into ${KEY}.root"
# -k : skip corrupt/missing inputs (some jobs die on XRootD and leave stubs)
# -n : cap simultaneously open files
hadd -f -k -n 200 ${KEY}.root $(cat ${KEY}.txt)
STATUS=$?
echo "hadd exit status ${STATUS}"
if [ ! -s ${KEY}.root ]; then
    echo "FATAL: ${KEY}.root missing or empty, not copying"
    exit 1
fi
mkdir -p /eos/home-y/yeo/rdf/output/hadd_files
cp ${KEY}.root /eos/home-y/yeo/rdf/output/hadd_files/${KEY}.root
echo "copied to /eos/home-y/yeo/rdf/output/hadd_files/${KEY}.root"
