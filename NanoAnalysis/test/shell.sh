#!/bin/bash

voms
cmsenv
cd /afs/cern.ch/user/y/yeo/rdf/24.10.11/CMSSW_14_0_14/src/JMETriggerAnalysis/NanoAnalysis/test
for i in {B,C,D,F,G,H}
do
	for j in {0,1}
	do
		python3 submit.py -d /JetMET$j/Run2024$i-PromptReco-v1/NANOAOD -o 2024${i}_JETMET${j}_251120_v3 -p Efficiency.py
		sleep 1
	done
done
for i in {E,I}
do
	for j in {0,1}
	do
		python3 submit.py -d /JetMET$j/Run2024$i-PromptReco-v2/NANOAOD -o 2024${i}_JETMET${j}_251120_v3 -p Efficiency.py
		sleep 1
	done
done
