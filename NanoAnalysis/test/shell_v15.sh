#!/bin/bash

voms
cmsenv
cd /afs/cern.ch/user/y/yeo/rdf/24.10.11/CMSSW_14_0_14/src/JMETriggerAnalysis/NanoAnalysis/test
python3 submit.py -d /JetMET0/Run2024C-MINIv6NANOv15-v1/NANOAOD    -o 2024C_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024D-MINIv6NANOv15-v1/NANOAOD    -o 2024D_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024E-MINIv6NANOv15-v1/NANOAOD    -o 2024E_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024F-MINIv6NANOv15-v2/NANOAOD    -o 2024F_v2_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024G-MINIv6NANOv15-v2/NANOAOD    -o 2024G_v2_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024H-MINIv6NANOv15-v2/NANOAOD    -o 2024G_v2_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD -o 2024I_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET0/Run2024I-MINIv6NANOv15-v2/NANOAOD    -o 2024I_v2_JETMET0_251216_v3 -p filterbitmatch.py -e 2024

python3 submit.py -d /JetMET1/Run2024C-MINIv6NANOv15-v1/NANOAOD    -o 2024C_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024D-MINIv6NANOv15-v1/NANOAOD    -o 2024D_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024E-MINIv6NANOv15-v1/NANOAOD    -o 2024E_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024F-MINIv6NANOv15-v2/NANOAOD    -o 2024F_v2_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024G-MINIv6NANOv15-v2/NANOAOD    -o 2024G_v2_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024H-MINIv6NANOv15-v2/NANOAOD    -o 2024H_v2_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD -o 2024I_v2_JETMET1_251216_v3 -p filterbitmatch.py -e 2024
python3 submit.py -d /JetMET1/Run2024I-MINIv6NANOv15-v1/NANOAOD    -o 2024I_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2024

python3 submit.py -d /JetMET0/Run2025B-PromptReco-v1/NANOAOD 	   -o 2025B_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025C-PromptReco-v1/NANOAOD 	   -o 2025C_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025C-PromptReco-v2/NANOAOD 	   -o 2025C_v2_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025D-PromptReco-v1/NANOAOD 	   -o 2025D_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025E-PromptReco-v1/NANOAOD 	   -o 2025E_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025F-PromptReco-v1/NANOAOD 	   -o 2025F_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025F-PromptReco-v2/NANOAOD 	   -o 2025F_v2_JETMET0_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET0/Run2025G-PromptReco-v1/NANOAOD 	   -o 2025G_v1_JETMET0_251216_v3 -p filterbitmatch.py -e 2025

python3 submit.py -d /JetMET1/Run2025B-PromptReco-v1/NANOAOD 	   -o 2025B_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025C-PromptReco-v1/NANOAOD 	   -o 2025C_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025C-PromptReco-v2/NANOAOD 	   -o 2025C_v2_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025D-PromptReco-v1/NANOAOD 	   -o 2025D_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025E-PromptReco-v1/NANOAOD 	   -o 2025E_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025F-PromptReco-v1/NANOAOD 	   -o 2025F_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025F-PromptReco-v2/NANOAOD 	   -o 2025F_v2_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
python3 submit.py -d /JetMET1/Run2025G-PromptReco-v1/NANOAOD 	   -o 2025G_v1_JETMET1_251216_v3 -p filterbitmatch.py -e 2025
