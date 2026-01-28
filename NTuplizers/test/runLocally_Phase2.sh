#!/bin/bash -e

# Run first the L1 step (note : very very big file output... ~100MB/Evt )
#cmsRun rerunL1_cfg.py maxEvents=50 output=output_Phase2_L1T.root
cmsDriver.py Phase2 -s L1,L1TrackTrigger --conditions auto:phase2_realistic_T33 --geometry ExtendedRun4D110 --era Phase2C17I13M9 --eventcontent RAW --datatier GEN-SIM-DIGI-RAW-MINIAOD --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT,L1Trigger/Configuration/customisePhase2TTOn110.customisePhase2TTOn110 --filein /store/mc/Phase2Spring24DIGIRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_AllTP_140X_mcRun4_realistic_v4-v1/2560000/11d1f6f0-5f03-421e-90c7-b5815197fc85.root --fileout file:output_Phase2_L1T.root --python_filename rerunL1_cfg.py --inputCommands="keep *, drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT" --outputCommands="keep *, drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT" --mc -n 1 --nThreads 1 --procModifiers trackingLST

#cmsRun  Phase2_L1P2GT_HLT.py
cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX --conditions auto:phase2_realistic_T33 --geometry ExtendedRun4D110 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 --filein file:output_Phase2_L1T.root --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' --mc -n 1 --nThreads 1 --procModifiers trackingLST



# HLT step with analyser that producer JMETrigger NTuple tree structure.
cmsRun jmeTriggerNTuple_cfg.py inputFiles=file:Phase2_L1P2GT_HLT.root output=out_LST.root

# Remove the large FEVTDEBUGHLT outputs
rm Phase2*HLT.root
rm output_Phase2_L1T.root

