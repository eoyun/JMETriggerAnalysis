#!/bin/bash -e

# Run first the L1 step (note : very very big file output... ~100MB/Evt )
cmsRun jmeTriggerNTuple_L1Only_cfg.py maxEvents=100 skipEvents=5 output=L1_output.root

# HLT step with analyser that producer JMETrigger NTuple tree structure.
cmsRun jmeTriggerNTuple_cfg.py track=LST inputFiles=file:L1_output.root output=./260114/out_LST.root
cmsRun jmeTriggerNTuple_cfg.py track=MkFit inputFiles=file:L1_output.root output=./260114/out_MkFit.root
cmsRun jmeTriggerNTuple_cfg.py track=both inputFiles=file:L1_output.root output=./260114/out_both.root
cmsRun jmeTriggerNTuple_cfg.py track=menu inputFiles=file:L1_output.root output=./260114/out_menu.root
cmsRun jmeTriggerNTuple_cfg.py inputFiles=file:L1_output.root output=./260114/out_default.root

# Remove the large FEVTDEBUGHLT outputs
 rm Phase2*HLT.root
 rm L1_output.root

