#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/setup.sh
export X509_USER_PROXY=/afs/cern.ch/user/y/yeo/tmp/x509up
voms-proxy-info -all
voms-proxy-info -all --file $1
cd /afs/cern.ch/user/y/yeo/rdf/24.10.11/CMSSW_14_0_14/src/JMETriggerAnalysis/NanoAnalysis/test
mkdir -p /eos/home-y/yeo/rdf/output/2024D_JETMET1_250415_v1
python3 Rdataframe.py -f ./input/2024D_JETMET1_250415_v1 -i $1 -o /eos/home-y/yeo/rdf/output/2024D_JETMET1_250415_v1