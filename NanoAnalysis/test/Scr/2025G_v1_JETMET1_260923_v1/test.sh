#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/setup.sh
export X509_USER_PROXY=/afs/cern.ch/user/y/yeo/tmp/x509up
voms-proxy-info -all
voms-proxy-info -all --file $X509_USER_PROXY
cd $_CONDOR_SCRATCH_DIR
mkdir -p /eos/home-y/yeo/rdf/output/2025G_v1_JETMET1_260923_v1
python3 ./filterbitmatch_jme.py -f 2025G_v1_JETMET1_260923_v1 -i $1 -o /eos/home-y/yeo/rdf/output/2025G_v1_JETMET1_260923_v1 -e 2025