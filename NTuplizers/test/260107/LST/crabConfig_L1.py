# crabConfig_L1.py
from CRABClient.UserUtilities import config
config = config()

# --- General
config.General.requestName = 'Phase2_T33_TTbar_PU200_L1_L1TrackTrigger'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

# --- JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'rerunL1_cfg.py'
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 1
# 필요시 runtime 올리기
# config.JobType.maxJobRuntimeMin = 2400

# --- Data (입력은 공식 dataset을 DAS에서)
config.Data.inputDataset = '/TT_TuneCP5_14TeV-powheg-pythia8/Phase2Spring24DIGIRECOMiniAOD-PU200_AllTP_140X_mcRun4_realistic_v4-v1/GEN-SIM-DIGI-RAW-MINIAOD'
config.Data.inputDBS = 'global'

# 이벤트가 적은 테스트면 FileBased가 편함 (파일 단위)
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

# output 저장
config.Data.outLFNDirBase = '/store/user/yeo/Phase2/L1T_T33/'
config.Data.publication = True
config.Data.outputDatasetTag = 'L1_L1TrackTrigger_T33_trackingLST'

# --- Site
config.Site.storageSite = 'T3_CH_CERNBOX'  # 예: 'T2_KR_KNU'

