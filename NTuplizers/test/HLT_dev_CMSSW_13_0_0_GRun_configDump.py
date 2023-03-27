import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.CUDACore.ProcessAcceleratorCUDA import ProcessAcceleratorCUDA
from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA

process = cms.Process("HLTX")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/Run3Winter23Digi/SinglePionGun_E200to500/GEN-SIM-RAW/EpsilonPU_126X_mcRun3_2023_forPU65_v1-v1/40000/53422f51-f90b-4ec6-ba57-35faab88d66a.root'),
    inputCommands = cms.untracked.vstring('keep *')
)
process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/dev/CMSSW_13_0_0/GRun/V16')
)

process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.5),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.HLTPSetJetCoreStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet(
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    DeltaR = cms.double(0.2),
    DeltaZ = cms.double(15.9),
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    Eta_fixed = cms.bool(False),
    Eta_min = cms.double(0.1),
    MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
    OnDemand = cms.int32(-1),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.1),
    Pt_fixed = cms.bool(False),
    Pt_min = cms.double(1.5),
    Rescale_Dz = cms.double(3.0),
    Rescale_eta = cms.double(3.0),
    Rescale_phi = cms.double(3.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    maxRegions = cms.int32(2),
    precise = cms.bool(True),
    vertexCollection = cms.InputTag("pixelVertices")
)

process.HLTPSetPixelLessStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(-1),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutForHI = cms.PSet(
    value = cms.double(2069.0)
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.datasets = cms.PSet(
    AlCaLowPtJet = cms.vstring(
        'AlCa_AK8PFJet40_v17',
        'AlCa_PFJet40_v22'
    ),
    AlCaLumiPixelsCountsExpress = cms.vstring('AlCa_LumiPixelsCounts_Random_v4'),
    AlCaLumiPixelsCountsPrompt = cms.vstring(
        'AlCa_LumiPixelsCounts_Random_v4',
        'AlCa_LumiPixelsCounts_ZeroBias_v4'
    ),
    AlCaP0 = cms.vstring(
        'AlCa_EcalEtaEBonly_v15',
        'AlCa_EcalEtaEEonly_v15',
        'AlCa_EcalPi0EBonly_v15',
        'AlCa_EcalPi0EEonly_v15'
    ),
    AlCaPPSExpress = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v2',
        'HLT_PPSMaxTracksPerRP4_v2'
    ),
    AlCaPPSPrompt = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v2',
        'HLT_PPSMaxTracksPerRP4_v2'
    ),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v11'),
    BTagMu = cms.vstring(
        'HLT_BTagMu_AK4DiJet110_Mu5_v15',
        'HLT_BTagMu_AK4DiJet170_Mu5_v14',
        'HLT_BTagMu_AK4DiJet20_Mu5_v15',
        'HLT_BTagMu_AK4DiJet40_Mu5_v15',
        'HLT_BTagMu_AK4DiJet70_Mu5_v15',
        'HLT_BTagMu_AK4Jet300_Mu5_v14',
        'HLT_BTagMu_AK8DiJet170_Mu5_v11',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v4',
        'HLT_BTagMu_AK8Jet300_Mu5_v14'
    ),
    Commissioning = cms.vstring(
        'HLT_IsoTrackHB_v6',
        'HLT_IsoTrackHE_v6',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v3',
        'HLT_PFJet40_GPUvsCPU_v1'
    ),
    Cosmics = cms.vstring('HLT_L1SingleMuCosmics_v2'),
    DQMGPUvsCPU = cms.vstring(
        'DQM_EcalReconstruction_v4',
        'DQM_HcalReconstruction_v3',
        'DQM_PixelReconstruction_v4'
    ),
    DQMOnlineBeamspot = cms.vstring(
        'HLT_HT300_Beamspot_v13',
        'HLT_ZeroBias_Beamspot_v6'
    ),
    DisplacedJet = cms.vstring(
        'HLT_CaloMET60_DTCluster50_v3',
        'HLT_CaloMET60_DTClusterNoMB1S50_v3',
        'HLT_CscCluster_Loose_v2',
        'HLT_CscCluster_Medium_v2',
        'HLT_CscCluster_Tight_v2',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v3',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v3',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v3',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v3',
        'HLT_HT425_v11',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v2',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v3',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v3',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v15',
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT550_DisplacedDijet60_Inclusive_v15',
        'HLT_HT650_DisplacedDijet60_Inclusive_v15',
        'HLT_L1CSCShower_DTCluster50_v2',
        'HLT_L1CSCShower_DTCluster75_v2',
        'HLT_L1MET_DTCluster50_v3',
        'HLT_L1MET_DTClusterNoMB1S50_v3',
        'HLT_L1Mu6HT240_v2',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v1',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v3',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v3',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v3'
    ),
    EGamma0 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v6',
        'HLT_DiPhoton10Time1p2ns_v2',
        'HLT_DiPhoton10Time1p4ns_v2',
        'HLT_DiPhoton10Time1p6ns_v2',
        'HLT_DiPhoton10Time1p8ns_v2',
        'HLT_DiPhoton10Time2ns_v2',
        'HLT_DiPhoton10_CaloIdL_v2',
        'HLT_DiPhoton10sminlt0p12_v2',
        'HLT_DiPhoton10sminlt0p1_v2',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v16',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v3',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v3',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v15',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v15',
        'HLT_DoubleEle25_CaloIdL_MW_v7',
        'HLT_DoubleEle27_CaloIdL_MW_v7',
        'HLT_DoubleEle33_CaloIdL_MW_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v22',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v22',
        'HLT_DoublePhoton33_CaloIdL_v9',
        'HLT_DoublePhoton70_v9',
        'HLT_DoublePhoton85_v17',
        'HLT_ECALHT800_v12',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v17',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v10',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v18',
        'HLT_Ele15_IsoVVVL_PFHT450_v18',
        'HLT_Ele15_IsoVVVL_PFHT600_v22',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v11',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v21',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
        'HLT_Ele28_HighEta_SC20_Mass55_v15',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v15',
        'HLT_Ele30_WPTight_Gsf_v3',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v15',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v11',
        'HLT_Ele32_WPTight_Gsf_v17',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v7',
        'HLT_Ele35_WPTight_Gsf_v11',
        'HLT_Ele38_WPTight_Gsf_v11',
        'HLT_Ele40_WPTight_Gsf_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v20',
        'HLT_Ele50_IsoVVVL_PFHT450_v18',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Photon100EBHE10_v4',
        'HLT_Photon110EB_TightID_TightIso_v4',
        'HLT_Photon120_R9Id90_HE10_IsoM_v16',
        'HLT_Photon120_v15',
        'HLT_Photon150_v9',
        'HLT_Photon165_R9Id90_HE10_IsoM_v17',
        'HLT_Photon175_v17',
        'HLT_Photon200_v16',
        'HLT_Photon20_HoverELoose_v12',
        'HLT_Photon300_NoHE_v15',
        'HLT_Photon30EB_TightID_TightIso_v3',
        'HLT_Photon30_HoverELoose_v12',
        'HLT_Photon33_v7',
        'HLT_Photon50_R9Id90_HE10_IsoM_v16',
        'HLT_Photon50_v15',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v1',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v1',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v1',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
        'HLT_Photon75_R9Id90_HE10_IsoM_v16',
        'HLT_Photon75_v15',
        'HLT_Photon90_R9Id90_HE10_IsoM_v16',
        'HLT_Photon90_v15'
    ),
    EGamma1 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v6',
        'HLT_DiPhoton10Time1p2ns_v2',
        'HLT_DiPhoton10Time1p4ns_v2',
        'HLT_DiPhoton10Time1p6ns_v2',
        'HLT_DiPhoton10Time1p8ns_v2',
        'HLT_DiPhoton10Time2ns_v2',
        'HLT_DiPhoton10_CaloIdL_v2',
        'HLT_DiPhoton10sminlt0p12_v2',
        'HLT_DiPhoton10sminlt0p1_v2',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v16',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v3',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v3',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v15',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v15',
        'HLT_DoubleEle25_CaloIdL_MW_v7',
        'HLT_DoubleEle27_CaloIdL_MW_v7',
        'HLT_DoubleEle33_CaloIdL_MW_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v22',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v22',
        'HLT_DoublePhoton33_CaloIdL_v9',
        'HLT_DoublePhoton70_v9',
        'HLT_DoublePhoton85_v17',
        'HLT_ECALHT800_v12',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v17',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v10',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v18',
        'HLT_Ele15_IsoVVVL_PFHT450_v18',
        'HLT_Ele15_IsoVVVL_PFHT600_v22',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v11',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v21',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
        'HLT_Ele28_HighEta_SC20_Mass55_v15',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v15',
        'HLT_Ele30_WPTight_Gsf_v3',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v15',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v11',
        'HLT_Ele32_WPTight_Gsf_v17',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v7',
        'HLT_Ele35_WPTight_Gsf_v11',
        'HLT_Ele38_WPTight_Gsf_v11',
        'HLT_Ele40_WPTight_Gsf_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v20',
        'HLT_Ele50_IsoVVVL_PFHT450_v18',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Photon100EBHE10_v4',
        'HLT_Photon110EB_TightID_TightIso_v4',
        'HLT_Photon120_R9Id90_HE10_IsoM_v16',
        'HLT_Photon120_v15',
        'HLT_Photon150_v9',
        'HLT_Photon165_R9Id90_HE10_IsoM_v17',
        'HLT_Photon175_v17',
        'HLT_Photon200_v16',
        'HLT_Photon20_HoverELoose_v12',
        'HLT_Photon300_NoHE_v15',
        'HLT_Photon30EB_TightID_TightIso_v3',
        'HLT_Photon30_HoverELoose_v12',
        'HLT_Photon33_v7',
        'HLT_Photon50_R9Id90_HE10_IsoM_v16',
        'HLT_Photon50_v15',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v1',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v1',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v1',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
        'HLT_Photon75_R9Id90_HE10_IsoM_v16',
        'HLT_Photon75_v15',
        'HLT_Photon90_R9Id90_HE10_IsoM_v16',
        'HLT_Photon90_v15'
    ),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v4'),
    EphemeralHLTPhysics = cms.vstring('HLT_EphemeralPhysics_v3'),
    EphemeralZeroBias = cms.vstring('HLT_EphemeralZeroBias_v3'),
    EventDisplay = cms.vstring(
        'HLT_DoublePhoton85_v17',
        'HLT_PFJet500_v23'
    ),
    ExpressAlignment = cms.vstring(
        'HLT_HT300_Beamspot_v13',
        'HLT_ZeroBias_Beamspot_v6'
    ),
    ExpressPhysics = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v21',
        'HLT_ExpressMuons_v3',
        'HLT_IsoMu20_v17',
        'HLT_IsoMu24_v15',
        'HLT_IsoMu27_v18',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v17',
        'HLT_Physics_v8',
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v2',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v6',
        'HLT_ZeroBias_IsolatedBunches_v6',
        'HLT_ZeroBias_v7'
    ),
    HLTMonitor = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v21',
        'HLT_Ele32_WPTight_Gsf_v17',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v2',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT550_DisplacedDijet60_Inclusive_v15',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v2',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBTagParticleNet_2BTagSum0p65_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v3',
        'HLT_PFHT510_v19',
        'HLT_PFJet260_v22',
        'HLT_PFJet320_v22',
        'HLT_PFMET130_PFMHT130_IDTight_v22',
        'HLT_PFMET140_PFMHT140_IDTight_v22'
    ),
    HLTPhysics = cms.vstring('HLT_Physics_v8'),
    HcalNZS = cms.vstring(
        'HLT_HcalNZS_v14',
        'HLT_HcalPhiSym_v16'
    ),
    IsolatedBunch = cms.vstring('HLT_HcalIsolatedbunch_v6'),
    JetMET0 = cms.vstring(
        'HLT_AK8DiPFJet250_250_MassSD30_v2',
        'HLT_AK8DiPFJet250_250_MassSD50_v2',
        'HLT_AK8DiPFJet260_260_MassSD30_v2',
        'HLT_AK8DiPFJet270_270_MassSD30_v2',
        'HLT_AK8PFJet140_v17',
        'HLT_AK8PFJet200_v17',
        'HLT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet230_SoftDropMass40_v3',
        'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
        'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet260_v18',
        'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
        'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet320_v18',
        'HLT_AK8PFJet400_MassSD30_v2',
        'HLT_AK8PFJet400_v18',
        'HLT_AK8PFJet40_v18',
        'HLT_AK8PFJet420_MassSD30_v2',
        'HLT_AK8PFJet425_SoftDropMass40_v3',
        'HLT_AK8PFJet450_MassSD30_v2',
        'HLT_AK8PFJet450_SoftDropMass40_v3',
        'HLT_AK8PFJet450_v18',
        'HLT_AK8PFJet500_v18',
        'HLT_AK8PFJet550_v13',
        'HLT_AK8PFJet60_v17',
        'HLT_AK8PFJet80_v17',
        'HLT_AK8PFJetFwd140_v16',
        'HLT_AK8PFJetFwd15_v5',
        'HLT_AK8PFJetFwd200_v16',
        'HLT_AK8PFJetFwd25_v5',
        'HLT_AK8PFJetFwd260_v17',
        'HLT_AK8PFJetFwd320_v17',
        'HLT_AK8PFJetFwd400_v17',
        'HLT_AK8PFJetFwd40_v17',
        'HLT_AK8PFJetFwd450_v17',
        'HLT_AK8PFJetFwd500_v17',
        'HLT_AK8PFJetFwd60_v16',
        'HLT_AK8PFJetFwd80_v16',
        'HLT_CaloJet500_NoJetID_v14',
        'HLT_CaloJet550_NoJetID_v9',
        'HLT_CaloMET350_NotCleaned_v6',
        'HLT_CaloMET90_NotCleaned_v6',
        'HLT_CaloMHT90_v6',
        'HLT_DiJet110_35_Mjj650_PFMET110_v11',
        'HLT_DiJet110_35_Mjj650_PFMET120_v11',
        'HLT_DiJet110_35_Mjj650_PFMET130_v11',
        'HLT_DiPFJetAve100_HFJEC_v18',
        'HLT_DiPFJetAve140_v15',
        'HLT_DiPFJetAve160_HFJEC_v18',
        'HLT_DiPFJetAve200_v15',
        'HLT_DiPFJetAve220_HFJEC_v18',
        'HLT_DiPFJetAve260_HFJEC_v1',
        'HLT_DiPFJetAve260_v16',
        'HLT_DiPFJetAve300_HFJEC_v18',
        'HLT_DiPFJetAve320_v16',
        'HLT_DiPFJetAve400_v16',
        'HLT_DiPFJetAve40_v16',
        'HLT_DiPFJetAve500_v16',
        'HLT_DiPFJetAve60_HFJEC_v17',
        'HLT_DiPFJetAve60_v16',
        'HLT_DiPFJetAve80_HFJEC_v18',
        'HLT_DiPFJetAve80_v15',
        'HLT_DoublePFJets100_PFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets200_PFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets350_PFBTagDeepJet_p71_v4',
        'HLT_DoublePFJets40_PFBTagDeepJet_p71_v3',
        'HLT_L1ETMHadSeeds_v4',
        'HLT_MET105_IsoTrk50_v11',
        'HLT_MET120_IsoTrk50_v11',
        'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_Mu12eta2p3_PFJet40_v3',
        'HLT_Mu12eta2p3_v3',
        'HLT_PFHT1050_v20',
        'HLT_PFHT180_v19',
        'HLT_PFHT250_v19',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v11',
        'HLT_PFHT350_v21',
        'HLT_PFHT370_v19',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v3',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v10',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v3',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v3',
        'HLT_PFHT400_SixPFJet32_v10',
        'HLT_PFHT430_v19',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v3',
        'HLT_PFHT450_SixPFJet36_v9',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v14',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v14',
        'HLT_PFHT510_v19',
        'HLT_PFHT590_v19',
        'HLT_PFHT680_v19',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v14',
        'HLT_PFHT780_v19',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v14',
        'HLT_PFHT890_v19',
        'HLT_PFJet110_v2',
        'HLT_PFJet140_v21',
        'HLT_PFJet200_v21',
        'HLT_PFJet260_v22',
        'HLT_PFJet320_v22',
        'HLT_PFJet400_v22',
        'HLT_PFJet40_v23',
        'HLT_PFJet450_v23',
        'HLT_PFJet500_v23',
        'HLT_PFJet550_v13',
        'HLT_PFJet60_v23',
        'HLT_PFJet80_v22',
        'HLT_PFJetFwd140_v20',
        'HLT_PFJetFwd200_v20',
        'HLT_PFJetFwd260_v21',
        'HLT_PFJetFwd320_v21',
        'HLT_PFJetFwd400_v21',
        'HLT_PFJetFwd40_v21',
        'HLT_PFJetFwd450_v21',
        'HLT_PFJetFwd500_v21',
        'HLT_PFJetFwd60_v21',
        'HLT_PFJetFwd80_v20',
        'HLT_PFMET105_IsoTrk50_v3',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v11',
        'HLT_PFMET120_PFMHT120_IDTight_v22',
        'HLT_PFMET130_PFMHT130_IDTight_v22',
        'HLT_PFMET140_PFMHT140_IDTight_v22',
        'HLT_PFMET200_BeamHaloCleaned_v11',
        'HLT_PFMET200_NotCleaned_v11',
        'HLT_PFMET250_NotCleaned_v11',
        'HLT_PFMET300_NotCleaned_v11',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v11',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v22',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v21',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v21',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v13',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v11',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet103_88_75_15_v7',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet105_88_76_15_v7',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet111_90_80_15_v7',
        'HLT_QuadPFJet70_50_40_30_v3',
        'HLT_QuadPFJet70_50_40_35_PFBTagParticleNet_2BTagSum0p65_v3',
        'HLT_QuadPFJet70_50_45_35_PFBTagParticleNet_2BTagSum0p65_v3',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v11',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v11',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v11'
    ),
    JetMET1 = cms.vstring(
        'HLT_AK8DiPFJet250_250_MassSD30_v2',
        'HLT_AK8DiPFJet250_250_MassSD50_v2',
        'HLT_AK8DiPFJet260_260_MassSD30_v2',
        'HLT_AK8DiPFJet270_270_MassSD30_v2',
        'HLT_AK8PFJet140_v17',
        'HLT_AK8PFJet200_v17',
        'HLT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet230_SoftDropMass40_v3',
        'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
        'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet260_v18',
        'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
        'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet320_v18',
        'HLT_AK8PFJet400_MassSD30_v2',
        'HLT_AK8PFJet400_v18',
        'HLT_AK8PFJet40_v18',
        'HLT_AK8PFJet420_MassSD30_v2',
        'HLT_AK8PFJet425_SoftDropMass40_v3',
        'HLT_AK8PFJet450_MassSD30_v2',
        'HLT_AK8PFJet450_SoftDropMass40_v3',
        'HLT_AK8PFJet450_v18',
        'HLT_AK8PFJet500_v18',
        'HLT_AK8PFJet550_v13',
        'HLT_AK8PFJet60_v17',
        'HLT_AK8PFJet80_v17',
        'HLT_AK8PFJetFwd140_v16',
        'HLT_AK8PFJetFwd15_v5',
        'HLT_AK8PFJetFwd200_v16',
        'HLT_AK8PFJetFwd25_v5',
        'HLT_AK8PFJetFwd260_v17',
        'HLT_AK8PFJetFwd320_v17',
        'HLT_AK8PFJetFwd400_v17',
        'HLT_AK8PFJetFwd40_v17',
        'HLT_AK8PFJetFwd450_v17',
        'HLT_AK8PFJetFwd500_v17',
        'HLT_AK8PFJetFwd60_v16',
        'HLT_AK8PFJetFwd80_v16',
        'HLT_CaloJet500_NoJetID_v14',
        'HLT_CaloJet550_NoJetID_v9',
        'HLT_CaloMET350_NotCleaned_v6',
        'HLT_CaloMET90_NotCleaned_v6',
        'HLT_CaloMHT90_v6',
        'HLT_DiJet110_35_Mjj650_PFMET110_v11',
        'HLT_DiJet110_35_Mjj650_PFMET120_v11',
        'HLT_DiJet110_35_Mjj650_PFMET130_v11',
        'HLT_DiPFJetAve100_HFJEC_v18',
        'HLT_DiPFJetAve140_v15',
        'HLT_DiPFJetAve160_HFJEC_v18',
        'HLT_DiPFJetAve200_v15',
        'HLT_DiPFJetAve220_HFJEC_v18',
        'HLT_DiPFJetAve260_HFJEC_v1',
        'HLT_DiPFJetAve260_v16',
        'HLT_DiPFJetAve300_HFJEC_v18',
        'HLT_DiPFJetAve320_v16',
        'HLT_DiPFJetAve400_v16',
        'HLT_DiPFJetAve40_v16',
        'HLT_DiPFJetAve500_v16',
        'HLT_DiPFJetAve60_HFJEC_v17',
        'HLT_DiPFJetAve60_v16',
        'HLT_DiPFJetAve80_HFJEC_v18',
        'HLT_DiPFJetAve80_v15',
        'HLT_DoublePFJets100_PFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets200_PFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets350_PFBTagDeepJet_p71_v4',
        'HLT_DoublePFJets40_PFBTagDeepJet_p71_v3',
        'HLT_L1ETMHadSeeds_v4',
        'HLT_MET105_IsoTrk50_v11',
        'HLT_MET120_IsoTrk50_v11',
        'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_Mu12eta2p3_PFJet40_v3',
        'HLT_Mu12eta2p3_v3',
        'HLT_PFHT1050_v20',
        'HLT_PFHT180_v19',
        'HLT_PFHT250_v19',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v11',
        'HLT_PFHT350_v21',
        'HLT_PFHT370_v19',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v3',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v10',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v3',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v3',
        'HLT_PFHT400_SixPFJet32_v10',
        'HLT_PFHT430_v19',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v3',
        'HLT_PFHT450_SixPFJet36_v9',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v14',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v14',
        'HLT_PFHT510_v19',
        'HLT_PFHT590_v19',
        'HLT_PFHT680_v19',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v14',
        'HLT_PFHT780_v19',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v14',
        'HLT_PFHT890_v19',
        'HLT_PFJet110_v2',
        'HLT_PFJet140_v21',
        'HLT_PFJet200_v21',
        'HLT_PFJet260_v22',
        'HLT_PFJet320_v22',
        'HLT_PFJet400_v22',
        'HLT_PFJet40_v23',
        'HLT_PFJet450_v23',
        'HLT_PFJet500_v23',
        'HLT_PFJet550_v13',
        'HLT_PFJet60_v23',
        'HLT_PFJet80_v22',
        'HLT_PFJetFwd140_v20',
        'HLT_PFJetFwd200_v20',
        'HLT_PFJetFwd260_v21',
        'HLT_PFJetFwd320_v21',
        'HLT_PFJetFwd400_v21',
        'HLT_PFJetFwd40_v21',
        'HLT_PFJetFwd450_v21',
        'HLT_PFJetFwd500_v21',
        'HLT_PFJetFwd60_v21',
        'HLT_PFJetFwd80_v20',
        'HLT_PFMET105_IsoTrk50_v3',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v11',
        'HLT_PFMET120_PFMHT120_IDTight_v22',
        'HLT_PFMET130_PFMHT130_IDTight_v22',
        'HLT_PFMET140_PFMHT140_IDTight_v22',
        'HLT_PFMET200_BeamHaloCleaned_v11',
        'HLT_PFMET200_NotCleaned_v11',
        'HLT_PFMET250_NotCleaned_v11',
        'HLT_PFMET300_NotCleaned_v11',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v11',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v22',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v21',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v21',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v13',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v11',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet103_88_75_15_v7',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet105_88_76_15_v7',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet111_90_80_15_v7',
        'HLT_QuadPFJet70_50_40_30_v3',
        'HLT_QuadPFJet70_50_40_35_PFBTagParticleNet_2BTagSum0p65_v3',
        'HLT_QuadPFJet70_50_45_35_PFBTagParticleNet_2BTagSum0p65_v3',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v11',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v11',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v11'
    ),
    L1Accept = cms.vstring(
        'DST_Physics_v8',
        'DST_ZeroBias_v3'
    ),
    MonteCarlo = cms.vstring(
        'MC_AK4CaloJetsFromPV_v10',
        'MC_AK4CaloJets_v11',
        'MC_AK4PFJets_v19',
        'MC_AK8CaloHT_v10',
        'MC_AK8PFHT_v18',
        'MC_AK8PFJets_v19',
        'MC_AK8TrimPFJets_v19',
        'MC_CaloBTagDeepCSV_v10',
        'MC_CaloHT_v10',
        'MC_CaloMET_JetIdCleaned_v11',
        'MC_CaloMET_v10',
        'MC_CaloMHT_v10',
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v15',
        'MC_DoubleEle5_CaloIdL_MW_v18',
        'MC_DoubleMuNoFiltersNoVtx_v9',
        'MC_DoubleMu_TrkIsoVVL_DZ_v13',
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'MC_Ele5_WPTight_Gsf_v10',
        'MC_IsoMu_v17',
        'MC_PFBTagDeepCSV_v12',
        'MC_PFBTagDeepJet_v3',
        'MC_PFHT_v18',
        'MC_PFMET_v19',
        'MC_PFMHT_v18',
        'MC_ReducedIterativeTracking_v14',
        'MC_Run3_PFScoutingPixelTracking_v18'
    ),
    Muon0 = cms.vstring(
        'HLT_CascadeMu100_v5',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v3',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v3',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v3',
        'HLT_DoubleL2Mu50_v3',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v3',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v12',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v12',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v12',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v12',
        'HLT_DoubleMu43NoFiltersNoVtx_v6',
        'HLT_DoubleMu48NoFiltersNoVtx_v6',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v10',
        'HLT_HighPtTkMu100_v4',
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v3',
        'HLT_IsoMu20_v17',
        'HLT_IsoMu24_TwoProngs35_v3',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v3',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v3',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_v17',
        'HLT_IsoMu24_v15',
        'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
        'HLT_IsoMu27_v18',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v2',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v2',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v17',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v17',
        'HLT_Mu15_IsoVVVL_PFHT450_v17',
        'HLT_Mu15_IsoVVVL_PFHT600_v21',
        'HLT_Mu15_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v17',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v16',
        'HLT_Mu17_TrkIsoVVL_v15',
        'HLT_Mu17_v15',
        'HLT_Mu18_Mu9_SameSign_v6',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v5',
        'HLT_Mu19_TrkIsoVVL_v6',
        'HLT_Mu19_v6',
        'HLT_Mu20_v14',
        'HLT_Mu27_v15',
        'HLT_Mu37_TkMu27_v7',
        'HLT_Mu3_PFJet40_v18',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v4',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v17',
        'HLT_Mu50_IsoVVVL_PFHT450_v17',
        'HLT_Mu50_L1SingleMuShower_v1',
        'HLT_Mu50_v15',
        'HLT_Mu55_v5',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v18',
        'HLT_Mu8_TrkIsoVVL_v14',
        'HLT_Mu8_v14',
        'HLT_TripleMu_10_5_5_DZ_v12',
        'HLT_TripleMu_12_10_5_v12',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v5',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v10',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v8'
    ),
    Muon1 = cms.vstring(
        'HLT_CascadeMu100_v5',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v3',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v3',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v3',
        'HLT_DoubleL2Mu50_v3',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v3',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v12',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v12',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v12',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v12',
        'HLT_DoubleMu43NoFiltersNoVtx_v6',
        'HLT_DoubleMu48NoFiltersNoVtx_v6',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v10',
        'HLT_HighPtTkMu100_v4',
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v3',
        'HLT_IsoMu20_v17',
        'HLT_IsoMu24_TwoProngs35_v3',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v3',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v3',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_v17',
        'HLT_IsoMu24_v15',
        'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
        'HLT_IsoMu27_v18',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v2',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v2',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v17',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v17',
        'HLT_Mu15_IsoVVVL_PFHT450_v17',
        'HLT_Mu15_IsoVVVL_PFHT600_v21',
        'HLT_Mu15_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v17',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v16',
        'HLT_Mu17_TrkIsoVVL_v15',
        'HLT_Mu17_v15',
        'HLT_Mu18_Mu9_SameSign_v6',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v5',
        'HLT_Mu19_TrkIsoVVL_v6',
        'HLT_Mu19_v6',
        'HLT_Mu20_v14',
        'HLT_Mu27_v15',
        'HLT_Mu37_TkMu27_v7',
        'HLT_Mu3_PFJet40_v18',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v4',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v17',
        'HLT_Mu50_IsoVVVL_PFHT450_v17',
        'HLT_Mu50_L1SingleMuShower_v1',
        'HLT_Mu50_v15',
        'HLT_Mu55_v5',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v18',
        'HLT_Mu8_TrkIsoVVL_v14',
        'HLT_Mu8_v14',
        'HLT_TripleMu_10_5_5_DZ_v12',
        'HLT_TripleMu_12_10_5_v12',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v5',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v10',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v8'
    ),
    MuonEG = cms.vstring(
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v19',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v19',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v19',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v9',
        'HLT_Mu17_Photon30_IsoCaloId_v8',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v3',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9',
        'HLT_Mu27_Ele37_CaloIdL_MW_v7',
        'HLT_Mu37_Ele27_CaloIdL_MW_v7',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v3',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v3',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v7',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v7',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v20',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v20',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v21',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v21',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v3',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBTagParticleNet_2BTagSum0p65_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v3',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v3',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_QuadPFJet70_50_40_30_PFBTagParticleNet_2BTagSum0p65_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_QuadPFJet70_50_40_30_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v13'
    ),
    NoBPTX = cms.vstring(
        'HLT_CDC_L2cosmic_10_er1p0_v2',
        'HLT_CDC_L2cosmic_5p5_er1p0_v2',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v6',
        'HLT_L2Mu10_NoVertex_NoBPTX_v7',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v6',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v5',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v7',
        'HLT_UncorrectedJetE30_NoBPTX_v7',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v7',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v7'
    ),
    OnlineMonitor = cms.vstring( (
        'HLT_AK8DiPFJet250_250_MassSD30_v2',
        'HLT_AK8DiPFJet250_250_MassSD50_v2',
        'HLT_AK8DiPFJet260_260_MassSD30_v2',
        'HLT_AK8DiPFJet270_270_MassSD30_v2',
        'HLT_AK8PFJet140_v17',
        'HLT_AK8PFJet200_v17',
        'HLT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet230_SoftDropMass40_v3',
        'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
        'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet260_v18',
        'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
        'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
        'HLT_AK8PFJet320_v18',
        'HLT_AK8PFJet400_MassSD30_v2',
        'HLT_AK8PFJet400_v18',
        'HLT_AK8PFJet40_v18',
        'HLT_AK8PFJet420_MassSD30_v2',
        'HLT_AK8PFJet425_SoftDropMass40_v3',
        'HLT_AK8PFJet450_MassSD30_v2',
        'HLT_AK8PFJet450_SoftDropMass40_v3',
        'HLT_AK8PFJet450_v18',
        'HLT_AK8PFJet500_v18',
        'HLT_AK8PFJet550_v13',
        'HLT_AK8PFJet60_v17',
        'HLT_AK8PFJet80_v17',
        'HLT_AK8PFJetFwd140_v16',
        'HLT_AK8PFJetFwd15_v5',
        'HLT_AK8PFJetFwd200_v16',
        'HLT_AK8PFJetFwd25_v5',
        'HLT_AK8PFJetFwd260_v17',
        'HLT_AK8PFJetFwd320_v17',
        'HLT_AK8PFJetFwd400_v17',
        'HLT_AK8PFJetFwd40_v17',
        'HLT_AK8PFJetFwd450_v17',
        'HLT_AK8PFJetFwd500_v17',
        'HLT_AK8PFJetFwd60_v16',
        'HLT_AK8PFJetFwd80_v16',
        'HLT_BTagMu_AK4DiJet110_Mu5_v15',
        'HLT_BTagMu_AK4DiJet170_Mu5_v14',
        'HLT_BTagMu_AK4DiJet20_Mu5_v15',
        'HLT_BTagMu_AK4DiJet40_Mu5_v15',
        'HLT_BTagMu_AK4DiJet70_Mu5_v15',
        'HLT_BTagMu_AK4Jet300_Mu5_v14',
        'HLT_BTagMu_AK8DiJet170_Mu5_v11',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v4',
        'HLT_BTagMu_AK8Jet300_Mu5_v14',
        'HLT_CDC_L2cosmic_10_er1p0_v2',
        'HLT_CDC_L2cosmic_5p5_er1p0_v2',
        'HLT_CaloJet500_NoJetID_v14',
        'HLT_CaloJet550_NoJetID_v9',
        'HLT_CaloMET350_NotCleaned_v6',
        'HLT_CaloMET60_DTCluster50_v3',
        'HLT_CaloMET60_DTClusterNoMB1S50_v3',
        'HLT_CaloMET90_NotCleaned_v6',
        'HLT_CaloMHT90_v6',
        'HLT_CascadeMu100_v5',
        'HLT_CscCluster_Loose_v2',
        'HLT_CscCluster_Medium_v2',
        'HLT_CscCluster_Tight_v2',
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v6',
        'HLT_DiJet110_35_Mjj650_PFMET110_v11',
        'HLT_DiJet110_35_Mjj650_PFMET120_v11',
        'HLT_DiJet110_35_Mjj650_PFMET130_v11',
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v19',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v19',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v19',
        'HLT_DiPFJetAve100_HFJEC_v18',
        'HLT_DiPFJetAve140_v15',
        'HLT_DiPFJetAve160_HFJEC_v18',
        'HLT_DiPFJetAve200_v15',
        'HLT_DiPFJetAve220_HFJEC_v18',
        'HLT_DiPFJetAve260_HFJEC_v1',
        'HLT_DiPFJetAve260_v16',
        'HLT_DiPFJetAve300_HFJEC_v18',
        'HLT_DiPFJetAve320_v16',
        'HLT_DiPFJetAve400_v16',
        'HLT_DiPFJetAve40_v16',
        'HLT_DiPFJetAve500_v16',
        'HLT_DiPFJetAve60_HFJEC_v17',
        'HLT_DiPFJetAve60_v16',
        'HLT_DiPFJetAve80_HFJEC_v18',
        'HLT_DiPFJetAve80_v15',
        'HLT_DiPhoton10Time1p2ns_v2',
        'HLT_DiPhoton10Time1p4ns_v2',
        'HLT_DiPhoton10Time1p6ns_v2',
        'HLT_DiPhoton10Time1p8ns_v2',
        'HLT_DiPhoton10Time2ns_v2',
        'HLT_DiPhoton10_CaloIdL_v2',
        'HLT_DiPhoton10sminlt0p12_v2',
        'HLT_DiPhoton10sminlt0p1_v2',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v16',
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v3',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v3',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v15',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v15',
        'HLT_DoubleEle25_CaloIdL_MW_v7',
        'HLT_DoubleEle27_CaloIdL_MW_v7',
        'HLT_DoubleEle33_CaloIdL_MW_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v22',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v22',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v3',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v3',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v3',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v3',
        'HLT_DoubleL2Mu50_v3',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v3',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v2',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v3',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v2',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v2',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v12',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v12',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v12',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v12',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu43NoFiltersNoVtx_v6',
        'HLT_DoubleMu48NoFiltersNoVtx_v6',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v10',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_DoublePFJets100_PFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets200_PFBTagDeepJet_p71_v3',
        'HLT_DoublePFJets350_PFBTagDeepJet_p71_v4',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v2',
        'HLT_DoublePFJets40_PFBTagDeepJet_p71_v3',
        'HLT_DoublePhoton33_CaloIdL_v9',
        'HLT_DoublePhoton70_v9',
        'HLT_DoublePhoton85_v17',
        'HLT_ECALHT800_v12',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v17',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v10',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v18',
        'HLT_Ele15_IsoVVVL_PFHT450_v18',
        'HLT_Ele15_IsoVVVL_PFHT600_v22',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v11',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v21',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Ele28_HighEta_SC20_Mass55_v15',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v15',
        'HLT_Ele30_WPTight_Gsf_v3',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v15',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v11',
        'HLT_Ele32_WPTight_Gsf_v17',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v7',
        'HLT_Ele35_WPTight_Gsf_v11',
        'HLT_Ele38_WPTight_Gsf_v11',
        'HLT_Ele40_WPTight_Gsf_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v2',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v20',
        'HLT_Ele50_IsoVVVL_PFHT450_v18',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v3',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v3',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v3',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v3',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v3',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v3',
        'HLT_HT425_v11',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v2',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v3',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v3',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v15',
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v15',
        'HLT_HT550_DisplacedDijet60_Inclusive_v15',
        'HLT_HT650_DisplacedDijet60_Inclusive_v15',
        'HLT_HcalIsolatedbunch_v6',
        'HLT_HcalNZS_v14',
        'HLT_HcalPhiSym_v16',
        'HLT_HighPtTkMu100_v4',
        'HLT_IsoMu20_v17',
        'HLT_IsoMu24_TwoProngs35_v3',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v3',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v3',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v2',
        'HLT_IsoMu24_eta2p1_v17',
        'HLT_IsoMu24_v15',
        'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
        'HLT_IsoMu27_v18',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v2',
        'HLT_IsoTrackHB_v6',
        'HLT_IsoTrackHE_v6',
        'HLT_L1CSCShower_DTCluster50_v2',
        'HLT_L1CSCShower_DTCluster75_v2',
        'HLT_L1ETMHadSeeds_v4',
        'HLT_L1MET_DTCluster50_v3',
        'HLT_L1MET_DTClusterNoMB1S50_v3',
        'HLT_L1Mu6HT240_v2',
        'HLT_L1SingleMuCosmics_v2',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v1',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v3',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v6',
        'HLT_L2Mu10_NoVertex_NoBPTX_v7',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v6',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v5',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v2',
        'HLT_MET105_IsoTrk50_v11',
        'HLT_MET120_IsoTrk50_v11',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v14',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v17',
        'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v3',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v9',
        'HLT_Mu12eta2p3_PFJet40_v3',
        'HLT_Mu12eta2p3_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v17',
        'HLT_Mu15_IsoVVVL_PFHT450_v17',
        'HLT_Mu15_IsoVVVL_PFHT600_v21',
        'HLT_Mu15_v5',
        'HLT_Mu17_Photon30_IsoCaloId_v8',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v17',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v16',
        'HLT_Mu17_TrkIsoVVL_v15',
        'HLT_Mu17_v15',
        'HLT_Mu18_Mu9_SameSign_v6',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v5',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v5',
        'HLT_Mu19_TrkIsoVVL_v6',
        'HLT_Mu19_v6',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v3',
        'HLT_Mu20_v14',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu27_Ele37_CaloIdL_MW_v7',
        'HLT_Mu27_v15',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu37_Ele27_CaloIdL_MW_v7',
        'HLT_Mu37_TkMu27_v7',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v3',
        'HLT_Mu3_PFJet40_v18',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v4',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v4',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v3',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v7',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v7',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v17',
        'HLT_Mu50_IsoVVVL_PFHT450_v17',
        'HLT_Mu50_L1SingleMuShower_v1',
        'HLT_Mu50_v15',
        'HLT_Mu55_v5',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v3',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v3',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v20',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v20',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v21',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v21',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v18',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v3',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBTagParticleNet_2BTagSum0p65_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v3',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v3',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_QuadPFJet70_50_40_30_PFBTagParticleNet_2BTagSum0p65_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_QuadPFJet70_50_40_30_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v13',
        'HLT_Mu8_TrkIsoVVL_v14',
        'HLT_Mu8_v14',
        'HLT_OnlineMonitorGroup_v3',
        'HLT_PFHT1050_v20',
        'HLT_PFHT180_v19',
        'HLT_PFHT250_v19',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v11',
        'HLT_PFHT350_v21',
        'HLT_PFHT370_v19',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v3',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v10',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v3',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v3',
        'HLT_PFHT400_SixPFJet32_v10',
        'HLT_PFHT430_v19',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v3',
        'HLT_PFHT450_SixPFJet36_v9',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v14',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v14',
        'HLT_PFHT510_v19',
        'HLT_PFHT590_v19',
        'HLT_PFHT680_v19',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v14',
        'HLT_PFHT780_v19',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v14',
        'HLT_PFHT890_v19',
        'HLT_PFJet110_v2',
        'HLT_PFJet140_v21',
        'HLT_PFJet200_v21',
        'HLT_PFJet260_v22',
        'HLT_PFJet320_v22',
        'HLT_PFJet400_v22',
        'HLT_PFJet40_v23',
        'HLT_PFJet450_v23',
        'HLT_PFJet500_v23',
        'HLT_PFJet550_v13',
        'HLT_PFJet60_v23',
        'HLT_PFJet80_v22',
        'HLT_PFJetFwd140_v20',
        'HLT_PFJetFwd200_v20',
        'HLT_PFJetFwd260_v21',
        'HLT_PFJetFwd320_v21',
        'HLT_PFJetFwd400_v21',
        'HLT_PFJetFwd40_v21',
        'HLT_PFJetFwd450_v21',
        'HLT_PFJetFwd500_v21',
        'HLT_PFJetFwd60_v21',
        'HLT_PFJetFwd80_v20',
        'HLT_PFMET105_IsoTrk50_v3',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v11',
        'HLT_PFMET120_PFMHT120_IDTight_v22',
        'HLT_PFMET130_PFMHT130_IDTight_v22',
        'HLT_PFMET140_PFMHT140_IDTight_v22',
        'HLT_PFMET200_BeamHaloCleaned_v11',
        'HLT_PFMET200_NotCleaned_v11',
        'HLT_PFMET250_NotCleaned_v11',
        'HLT_PFMET300_NotCleaned_v11',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v11',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v22',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v21',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v2',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v21',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v13',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v11',
        'HLT_Photon100EBHE10_v4',
        'HLT_Photon110EB_TightID_TightIso_v4',
        'HLT_Photon120_R9Id90_HE10_IsoM_v16',
        'HLT_Photon120_v15',
        'HLT_Photon150_v9',
        'HLT_Photon165_R9Id90_HE10_IsoM_v17',
        'HLT_Photon175_v17',
        'HLT_Photon200_v16',
        'HLT_Photon20_HoverELoose_v12',
        'HLT_Photon300_NoHE_v15',
        'HLT_Photon30EB_TightID_TightIso_v3',
        'HLT_Photon30_HoverELoose_v12',
        'HLT_Photon33_v7',
        'HLT_Photon35_TwoProngs35_v3',
        'HLT_Photon50_R9Id90_HE10_IsoM_v16',
        'HLT_Photon50_v15',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v1',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v1',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v1',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
        'HLT_Photon75_R9Id90_HE10_IsoM_v16',
        'HLT_Photon75_v15',
        'HLT_Photon90_R9Id90_HE10_IsoM_v16',
        'HLT_Photon90_v15',
        'HLT_Physics_v8',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet103_88_75_15_v7',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet105_88_76_15_v7',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v3',
        'HLT_QuadPFJet111_90_80_15_v7',
        'HLT_QuadPFJet70_50_40_30_v3',
        'HLT_QuadPFJet70_50_40_35_PFBTagParticleNet_2BTagSum0p65_v3',
        'HLT_QuadPFJet70_50_45_35_PFBTagParticleNet_2BTagSum0p65_v3',
        'HLT_Random_v3',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v13',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v11',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v11',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v11',
        'HLT_TripleMu_10_5_5_DZ_v12',
        'HLT_TripleMu_12_10_5_v12',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v5',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v10',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v8',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v7',
        'HLT_UncorrectedJetE30_NoBPTX_v7',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v7',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v7',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v2',
        'HLT_ZeroBias_Alignment_v2',
        'HLT_ZeroBias_FirstBXAfterTrain_v4',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v6',
        'HLT_ZeroBias_FirstCollisionInTrain_v5',
        'HLT_ZeroBias_IsolatedBunches_v6',
        'HLT_ZeroBias_LastCollisionInTrain_v4',
        'HLT_ZeroBias_v7'
     ) ),
    ParkingDoubleElectronLowMass0 = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v2',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_v2',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_v2',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_v2',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_v2',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_v2',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
        'HLT_SingleEle8_SingleEGL1_v1',
        'HLT_SingleEle8_v1'
    ),
    ParkingDoubleElectronLowMass1 = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v2',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_v2',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_v2',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_v2',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_v2',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_v2',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
        'HLT_SingleEle8_SingleEGL1_v1',
        'HLT_SingleEle8_v1'
    ),
    ParkingDoubleElectronLowMass2 = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v2',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_v2',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_v2',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_v2',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_v2',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_v2',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
        'HLT_SingleEle8_SingleEGL1_v1',
        'HLT_SingleEle8_v1'
    ),
    ParkingDoubleElectronLowMass3 = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v2',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_v2',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_v2',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_v2',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_v2',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_v2',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
        'HLT_SingleEle8_SingleEGL1_v1',
        'HLT_SingleEle8_v1'
    ),
    ParkingDoubleElectronLowMass4 = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v2',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_v2',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_v2',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_v2',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_v2',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_v2',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
        'HLT_SingleEle8_SingleEGL1_v1',
        'HLT_SingleEle8_v1'
    ),
    ParkingDoubleElectronLowMass5 = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v2',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4_eta1p22_mMax6_v2',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5_eta1p22_mMax6_v2',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6_eta1p22_mMax6_v2',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7_eta1p22_mMax6_v2',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8_eta1p22_mMax6_v2',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9_eta1p22_mMax6_v2',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v1',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
        'HLT_SingleEle8_SingleEGL1_v1',
        'HLT_SingleEle8_v1'
    ),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass4 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass5 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass6 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingDoubleMuonLowMass7 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon10_Upsilon_y1p4_v3',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
        'HLT_Dimuon14_PsiPrime_v15',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_3_LowMass_v3',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_JpsiTrk_Bc_v2',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_LowMass_Displaced_v3',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ParkingSingleMuon0 = cms.vstring('HLT_Mu12_IP6_v2'),
    ParkingSingleMuon1 = cms.vstring('HLT_Mu12_IP6_v2'),
    ParkingSingleMuon2 = cms.vstring('HLT_Mu12_IP6_v2'),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNormalisation_v14'),
    ReservedDoubleMuonLowMass = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
        'HLT_Dimuon0_Jpsi_NoVertexing_v10',
        'HLT_Dimuon0_Jpsi_v10',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
        'HLT_Dimuon0_LowMass_L1_4R_v9',
        'HLT_Dimuon0_LowMass_L1_4_v10',
        'HLT_Dimuon0_LowMass_L1_TM530_v8',
        'HLT_Dimuon0_LowMass_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
        'HLT_Dimuon0_Upsilon_L1_4p5_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
        'HLT_Dimuon0_Upsilon_L1_5M_v10',
        'HLT_Dimuon0_Upsilon_L1_5_v11',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
        'HLT_Dimuon0_Upsilon_NoVertexing_v9',
        'HLT_Dimuon12_Upsilon_y1p4_v4',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
        'HLT_Dimuon18_PsiPrime_v16',
        'HLT_Dimuon24_Phi_noCorrL1_v8',
        'HLT_Dimuon24_Upsilon_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_noCorrL1_v8',
        'HLT_Dimuon25_Jpsi_v16',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_v14',
        'HLT_DoubleMu4_3_Bs_v17',
        'HLT_DoubleMu4_3_Jpsi_v17',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_Displaced_v9',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
        'HLT_Mu25_TkMu0_Phi_v10',
        'HLT_Mu30_TkMu0_Psi_v3',
        'HLT_Mu30_TkMu0_Upsilon_v3',
        'HLT_Mu4_L1DoubleMu_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v12',
        'HLT_Mu7p5_L2Mu2_Upsilon_v12',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
    ),
    ScoutingPFMonitor = cms.vstring(
        'DST_Run3_PFScoutingPixelTracking_v18',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v17',
        'HLT_Ele35_WPTight_Gsf_v11',
        'HLT_IsoMu27_v18',
        'HLT_Mu50_v15',
        'HLT_PFHT1050_v20',
        'HLT_Photon200_v16'
    ),
    ScoutingPFRun3 = cms.vstring(
        'DST_HLTMuon_Run3_PFScoutingPixelTracking_v18',
        'DST_Run3_PFScoutingPixelTracking_v18'
    ),
    Tau = cms.vstring(
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v3',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v2',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v2',
        'HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1_v2',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v2',
        'HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1_v3',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v14',
        'HLT_Photon35_TwoProngs35_v3',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v2'
    ),
    TestEnablesEcalHcal = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v5'
    ),
    TestEnablesEcalHcalDQM = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v5'
    ),
    ZeroBias = cms.vstring(
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v2',
        'HLT_ZeroBias_FirstBXAfterTrain_v4',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v6',
        'HLT_ZeroBias_FirstCollisionInTrain_v5',
        'HLT_ZeroBias_IsolatedBunches_v6',
        'HLT_ZeroBias_LastCollisionInTrain_v4',
        'HLT_ZeroBias_v7'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring(
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'Tracking/TrackParameters/GeneralProperties/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/GeneralProperties/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/GeneralProperties/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertice/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    ALCALowPtJet = cms.vstring('AlCaLowPtJet'),
    ALCALumiPixelsCountsExpress = cms.vstring('AlCaLumiPixelsCountsExpress'),
    ALCALumiPixelsCountsPrompt = cms.vstring('AlCaLumiPixelsCountsPrompt'),
    ALCAP0 = cms.vstring('AlCaP0'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    ALCAPPSExpress = cms.vstring('AlCaPPSExpress'),
    ALCAPPSPrompt = cms.vstring('AlCaPPSPrompt'),
    Calibration = cms.vstring('TestEnablesEcalHcal'),
    DQM = cms.vstring('OnlineMonitor'),
    DQMCalibration = cms.vstring('TestEnablesEcalHcalDQM'),
    DQMEventDisplay = cms.vstring('EventDisplay'),
    DQMGPUvsCPU = cms.vstring('DQMGPUvsCPU'),
    DQMOnlineBeamspot = cms.vstring('DQMOnlineBeamspot'),
    EcalCalibration = cms.vstring('EcalLaser'),
    Express = cms.vstring('ExpressPhysics'),
    ExpressAlignment = cms.vstring('ExpressAlignment'),
    ExpressCosmics = cms.vstring(),
    HLTMonitor = cms.vstring('HLTMonitor'),
    NanoDST = cms.vstring('L1Accept'),
    ParkingDoubleElectronLowMass0 = cms.vstring(
        'ParkingDoubleElectronLowMass0',
        'ParkingDoubleElectronLowMass1'
    ),
    ParkingDoubleElectronLowMass1 = cms.vstring(
        'ParkingDoubleElectronLowMass2',
        'ParkingDoubleElectronLowMass3'
    ),
    ParkingDoubleElectronLowMass2 = cms.vstring(
        'ParkingDoubleElectronLowMass4',
        'ParkingDoubleElectronLowMass5'
    ),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'ParkingDoubleMuonLowMass0',
        'ParkingDoubleMuonLowMass1'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'ParkingDoubleMuonLowMass2',
        'ParkingDoubleMuonLowMass3'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'ParkingDoubleMuonLowMass4',
        'ParkingDoubleMuonLowMass5'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'ParkingDoubleMuonLowMass6',
        'ParkingDoubleMuonLowMass7'
    ),
    ParkingSingleMuon0 = cms.vstring('ParkingSingleMuon0'),
    ParkingSingleMuon1 = cms.vstring('ParkingSingleMuon1'),
    ParkingSingleMuon2 = cms.vstring('ParkingSingleMuon2'),
    PhysicsCommissioning = cms.vstring(
        'Commissioning',
        'Cosmics',
        'HLTPhysics',
        'HcalNZS',
        'IsolatedBunch',
        'MonteCarlo',
        'NoBPTX',
        'ZeroBias'
    ),
    PhysicsDispJetBTagMuEGTau = cms.vstring(
        'BTagMu',
        'DisplacedJet',
        'MuonEG',
        'Tau'
    ),
    PhysicsEGamma0 = cms.vstring('EGamma0'),
    PhysicsEGamma1 = cms.vstring('EGamma1'),
    PhysicsHLTPhysics = cms.vstring('EphemeralHLTPhysics'),
    PhysicsJetMET0 = cms.vstring('JetMET0'),
    PhysicsJetMET1 = cms.vstring('JetMET1'),
    PhysicsMuon0 = cms.vstring('Muon0'),
    PhysicsMuon1 = cms.vstring('Muon1'),
    PhysicsReservedDoubleMuonLowMass = cms.vstring('ReservedDoubleMuonLowMass'),
    PhysicsScoutingPFMonitor = cms.vstring('ScoutingPFMonitor'),
    PhysicsZeroBias = cms.vstring('EphemeralZeroBias'),
    RPCMON = cms.vstring('RPCMonitor'),
    ScoutingPF = cms.vstring('ScoutingPFRun3')
)

process.transferSystem = cms.PSet(
    default = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        streamLookArea = cms.PSet(

        ),
        test = cms.vstring('Lustre')
    ),
    destinations = cms.vstring(
        'Tier0',
        'DQM',
        'ECAL',
        'EventDisplay',
        'Lustre',
        'None'
    ),
    streamA = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamDQM = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamDQMCalibration = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamEcalCalibration = cms.PSet(
        default = cms.vstring('ECAL'),
        emulator = cms.vstring('None'),
        test = cms.vstring('ECAL')
    ),
    streamEventDisplay = cms.PSet(
        default = cms.vstring(
            'EventDisplay',
            'Tier0'
        ),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'EventDisplay',
            'Lustre'
        )
    ),
    streamExpressCosmics = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamLookArea = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamNanoDST = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamRPCMON = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamTrackerCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    transferModes = cms.vstring(
        'default',
        'test',
        'emulator'
    )
)

process.hltAK4CaloAbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L3Absolute')
)


process.hltAK4CaloCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("hltAK4CaloFastJetCorrector", "hltAK4CaloRelativeCorrector", "hltAK4CaloAbsoluteCorrector", "hltAK4CaloResidualCorrector")
)


process.hltAK4CaloFastJetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAllCalo")
)


process.hltAK4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(0.9),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4CaloJetsCorrected = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("hltAK4CaloCorrector"),
    src = cms.InputTag("hltAK4CaloJets")
)


process.hltAK4CaloJetsCorrectedIDPassed = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("hltAK4CaloCorrector"),
    src = cms.InputTag("hltAK4CaloJetsIDPassed")
)


process.hltAK4CaloJetsIDPassed = cms.EDProducer("HLTCaloJetIDProducer",
    JetIDParams = cms.PSet(
        ebRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        eeRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag("hltHbhereco"),
        hfRecHitsColl = cms.InputTag("hltHfreco"),
        hoRecHitsColl = cms.InputTag("hltHoreco"),
        useRecHits = cms.bool(True)
    ),
    jetsInput = cms.InputTag("hltAK4CaloJets"),
    max_EMF = cms.double(999.0),
    min_EMF = cms.double(1e-06),
    min_N90 = cms.int32(-2),
    min_N90hits = cms.int32(2)
)


process.hltAK4CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(-9.0),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4CaloRelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L2Relative')
)


process.hltAK4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L2L3Residual')
)


process.hltAK4PFAbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L3Absolute')
)


process.hltAK4PFCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("hltAK4PFFastJetCorrector", "hltAK4PFRelativeCorrector", "hltAK4PFAbsoluteCorrector", "hltAK4PFResidualCorrector")
)


process.hltAK4PFFastJetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAll")
)


process.hltAK4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(0),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltParticleFlow"),
    srcPVs = cms.InputTag("hltPixelVertices"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(-9.0),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4PFJetsCorrected = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("hltAK4PFCorrector"),
    src = cms.InputTag("hltAK4PFJets")
)


process.hltAK4PFJetsLooseID = cms.EDProducer("HLTPFJetIDProducer",
    CEF = cms.double(0.99),
    CHF = cms.double(0.0),
    NCH = cms.int32(0),
    NEF = cms.double(0.99),
    NHF = cms.double(0.99),
    NTOT = cms.int32(1),
    jetsInput = cms.InputTag("hltAK4PFJets"),
    maxCF = cms.double(99.0),
    maxEta = cms.double(1e+99),
    minPt = cms.double(20.0)
)


process.hltAK4PFJetsLooseIDCorrected = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("hltAK4PFCorrector"),
    src = cms.InputTag("hltAK4PFJetsLooseID")
)


process.hltAK4PFJetsTightID = cms.EDProducer("HLTPFJetIDProducer",
    CEF = cms.double(0.99),
    CHF = cms.double(0.0),
    NCH = cms.int32(0),
    NEF = cms.double(0.99),
    NHF = cms.double(0.9),
    NTOT = cms.int32(1),
    jetsInput = cms.InputTag("hltAK4PFJets"),
    maxCF = cms.double(99.0),
    maxEta = cms.double(1e+99),
    minPt = cms.double(20.0)
)


process.hltAK4PFJetsTightIDCorrected = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("hltAK4PFCorrector"),
    src = cms.InputTag("hltAK4PFJetsTightID")
)


process.hltAK4PFRelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L2Relative')
)


process.hltAK4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L2L3Residual')
)


process.hltAK8CaloAbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8CaloHLT'),
    level = cms.string('L3Absolute')
)


process.hltAK8CaloCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("hltAK8CaloFastJetCorrector", "hltAK8CaloRelativeCorrector", "hltAK8CaloAbsoluteCorrector", "hltAK8CaloResidualCorrector")
)


process.hltAK8CaloFastJetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK8CaloHLT'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAllCalo")
)


process.hltAK8CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(0.9),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK8CaloJetsCorrected = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("hltAK8CaloCorrector"),
    src = cms.InputTag("hltAK8CaloJets")
)


process.hltAK8CaloJetsCorrectedIDPassed = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("hltAK8CaloCorrector"),
    src = cms.InputTag("hltAK8CaloJetsIDPassed")
)


process.hltAK8CaloJetsIDPassed = cms.EDProducer("HLTCaloJetIDProducer",
    JetIDParams = cms.PSet(
        ebRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        eeRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag("hltHbhereco"),
        hfRecHitsColl = cms.InputTag("hltHfreco"),
        hoRecHitsColl = cms.InputTag("hltHoreco"),
        useRecHits = cms.bool(True)
    ),
    jetsInput = cms.InputTag("hltAK8CaloJets"),
    max_EMF = cms.double(999.0),
    min_EMF = cms.double(1e-06),
    min_N90 = cms.int32(-2),
    min_N90hits = cms.int32(2)
)


process.hltAK8CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(-9.0),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK8CaloRelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8CaloHLT'),
    level = cms.string('L2Relative')
)


process.hltAK8CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8CaloHLT'),
    level = cms.string('L2L3Residual')
)


process.hltAK8HtMhtForMC = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK8CaloJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(30.0),
    minPtJetMht = cms.double(20.0),
    pfCandidatesLabel = cms.InputTag(""),
    usePt = cms.bool(False)
)


process.hltAK8PFAbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFHLT'),
    level = cms.string('L3Absolute')
)


process.hltAK8PFCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("hltAK8PFFastJetCorrector", "hltAK8PFRelativeCorrector", "hltAK8PFAbsoluteCorrector", "hltAK8PFResidualCorrector")
)


process.hltAK8PFFastJetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK8PFHLT'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAll")
)


process.hltAK8PFHTForMC = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK8PFJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40.0),
    minPtJetMht = cms.double(20.0),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    usePt = cms.bool(True)
)


process.hltAK8PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(0),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltParticleFlow"),
    srcPVs = cms.InputTag("hltPixelVertices"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(-9.0),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK8PFJetsCorrected = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("hltAK8PFCorrector"),
    src = cms.InputTag("hltAK8PFJets")
)


process.hltAK8PFJetsLooseID = cms.EDProducer("HLTPFJetIDProducer",
    CEF = cms.double(0.99),
    CHF = cms.double(0.0),
    NCH = cms.int32(0),
    NEF = cms.double(0.99),
    NHF = cms.double(0.99),
    NTOT = cms.int32(1),
    jetsInput = cms.InputTag("hltAK8PFJets"),
    maxCF = cms.double(99.0),
    maxEta = cms.double(1e+99),
    minPt = cms.double(20.0)
)


process.hltAK8PFJetsLooseIDCorrected = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("hltAK8PFCorrector"),
    src = cms.InputTag("hltAK8PFJetsLooseID")
)


process.hltAK8PFJetsTightID = cms.EDProducer("HLTPFJetIDProducer",
    CEF = cms.double(0.99),
    CHF = cms.double(0.0),
    NCH = cms.int32(0),
    NEF = cms.double(0.99),
    NHF = cms.double(0.9),
    NTOT = cms.int32(1),
    jetsInput = cms.InputTag("hltAK8PFJets"),
    maxCF = cms.double(99.0),
    maxEta = cms.double(1e+99),
    minPt = cms.double(20.0)
)


process.hltAK8PFJetsTightIDCorrected = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("hltAK8PFCorrector"),
    src = cms.InputTag("hltAK8PFJetsTightID")
)


process.hltAK8PFRelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFHLT'),
    level = cms.string('L2Relative')
)


process.hltAK8PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFHLT'),
    level = cms.string('L2L3Residual')
)


process.hltAK8TrimModJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(20.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(0.1),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltParticleFlow"),
    srcPVs = cms.InputTag("hltPixelVertices"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(0.03),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(True),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltCaloJetFromPV = cms.EDProducer("PixelJetPuId",
    MaxTrackChi2 = cms.double(20.0),
    MaxTrackDistanceToJet = cms.double(0.04),
    MinEtForwardJets = cms.double(40.0),
    MinEtaForwardJets = cms.double(2.4),
    MinGoodJetTrackPt = cms.double(1.8),
    MinGoodJetTrackPtRatio = cms.double(0.045),
    MinTrackPt = cms.double(0.6),
    UseForwardJetsAsNoPU = cms.bool(True),
    jets = cms.InputTag("hltSelectorJets20L1FastJetForNoPU"),
    primaryVertex = cms.InputTag("hltTrimmedPixelVertices"),
    tracks = cms.InputTag("hltPixelTracks")
)


process.hltCsc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    CSCDebug = cms.untracked.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(False),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCUseStaticPedestals = cms.bool(False),
    CSCUseTimingCorrections = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCstripWireDeltaTime = cms.int32(8),
    ConstSyst_ME12 = cms.double(0.0),
    ConstSyst_ME13 = cms.double(0.0),
    ConstSyst_ME1a = cms.double(0.022),
    ConstSyst_ME1b = cms.double(0.007),
    ConstSyst_ME21 = cms.double(0.0),
    ConstSyst_ME22 = cms.double(0.0),
    ConstSyst_ME31 = cms.double(0.0),
    ConstSyst_ME32 = cms.double(0.0),
    ConstSyst_ME41 = cms.double(0.0),
    NoiseLevel_ME12 = cms.double(9.0),
    NoiseLevel_ME13 = cms.double(8.0),
    NoiseLevel_ME1a = cms.double(7.0),
    NoiseLevel_ME1b = cms.double(8.0),
    NoiseLevel_ME21 = cms.double(9.0),
    NoiseLevel_ME22 = cms.double(9.0),
    NoiseLevel_ME31 = cms.double(9.0),
    NoiseLevel_ME32 = cms.double(9.0),
    NoiseLevel_ME41 = cms.double(9.0),
    UseAverageTime = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME12 = cms.double(0.0),
    XTasymmetry_ME13 = cms.double(0.0),
    XTasymmetry_ME1a = cms.double(0.0),
    XTasymmetry_ME1b = cms.double(0.0),
    XTasymmetry_ME21 = cms.double(0.0),
    XTasymmetry_ME22 = cms.double(0.0),
    XTasymmetry_ME31 = cms.double(0.0),
    XTasymmetry_ME32 = cms.double(0.0),
    XTasymmetry_ME41 = cms.double(0.0),
    readBadChambers = cms.bool(True),
    readBadChannels = cms.bool(False),
    stripDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCWireDigi")
)


process.hltCscSegments = cms.EDProducer("CSCSegmentProducer",
    algo_psets = cms.VPSet(cms.PSet(
        algo_name = cms.string('CSCSegAlgoRU'),
        algo_psets = cms.VPSet(
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.005),
                dPhiMax = cms.double(0.006),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.004),
                dPhiMax = cms.double(0.005),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.003),
                dPhiMax = cms.double(0.004),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(60.0),
                chi2Norm_2D_ = cms.double(20.0),
                chi2_str = cms.double(30.0),
                dPhiIntMax = cms.double(0.002),
                dPhiMax = cms.double(0.003),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(180.0),
                chi2Norm_2D_ = cms.double(60.0),
                chi2_str = cms.double(80.0),
                dPhiIntMax = cms.double(0.005),
                dPhiMax = cms.double(0.007),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            ),
            cms.PSet(
                chi2Max = cms.double(100.0),
                chi2Norm_2D_ = cms.double(35.0),
                chi2_str = cms.double(50.0),
                dPhiIntMax = cms.double(0.004),
                dPhiMax = cms.double(0.006),
                dRIntMax = cms.double(2.0),
                dRMax = cms.double(1.5),
                doCollisions = cms.bool(True),
                enlarge = cms.bool(False),
                minLayersApart = cms.int32(1),
                wideSeg = cms.double(3.0)
            )
        ),
        chamber_types = cms.vstring(
            'ME1/a',
            'ME1/b',
            'ME1/2',
            'ME1/3',
            'ME2/1',
            'ME2/2',
            'ME3/1',
            'ME3/2',
            'ME4/1',
            'ME4/2'
        ),
        parameters_per_chamber_type = cms.vint32(
            1, 2, 3, 4, 5,
            6, 5, 6, 5, 6
        )
    )),
    algo_type = cms.int32(1),
    inputObjects = cms.InputTag("hltCsc2DRecHits")
)


process.hltDt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    dtDigiLabel = cms.InputTag("hltMuonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
    recAlgoConfig = cms.PSet(
        debug = cms.untracked.bool(False),
        doVdriftCorr = cms.bool(True),
        maxTime = cms.double(420.0),
        minTime = cms.double(-3.0),
        readLegacyTTrigDB = cms.bool(True),
        readLegacyVDriftDB = cms.bool(True),
        stepTwoFromDigi = cms.bool(False),
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        tTrigModeConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doT0Correction = cms.bool(True),
            doTOFCorrection = cms.bool(True),
            doWirePropCorrection = cms.bool(True),
            t0Label = cms.string(''),
            tTrigLabel = cms.string(''),
            tofCorrType = cms.int32(0),
            vPropWire = cms.double(24.4),
            wirePropCorrType = cms.int32(0)
        ),
        useUncertDB = cms.bool(True)
    )
)


process.hltDt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    Reco4DAlgoConfig = cms.PSet(
        AllDTRecHits = cms.bool(True),
        Reco2DAlgoConfig = cms.PSet(
            AlphaMaxPhi = cms.double(1.0),
            AlphaMaxTheta = cms.double(0.9),
            MaxAllowedHits = cms.uint32(50),
            debug = cms.untracked.bool(False),
            hit_afterT0_resolution = cms.double(0.03),
            nSharedHitsMax = cms.int32(2),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            performT0_vdriftSegCorrection = cms.bool(False),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(True),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                readLegacyTTrigDB = cms.bool(True),
                readLegacyVDriftDB = cms.bool(True),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(True),
                    doWirePropCorrection = cms.bool(True),
                    t0Label = cms.string(''),
                    tTrigLabel = cms.string(''),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(True)
            ),
            segmCleanerMode = cms.int32(2)
        ),
        Reco2DAlgoName = cms.string('DTCombinatorialPatternReco'),
        debug = cms.untracked.bool(False),
        hit_afterT0_resolution = cms.double(0.03),
        nSharedHitsMax = cms.int32(2),
        nUnSharedHitsMin = cms.int32(2),
        performT0SegCorrection = cms.bool(False),
        performT0_vdriftSegCorrection = cms.bool(False),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doVdriftCorr = cms.bool(True),
            maxTime = cms.double(420.0),
            minTime = cms.double(-3.0),
            readLegacyTTrigDB = cms.bool(True),
            readLegacyVDriftDB = cms.bool(True),
            stepTwoFromDigi = cms.bool(False),
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            tTrigModeConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doT0Correction = cms.bool(True),
                doTOFCorrection = cms.bool(True),
                doWirePropCorrection = cms.bool(True),
                t0Label = cms.string(''),
                tTrigLabel = cms.string(''),
                tofCorrType = cms.int32(0),
                vPropWire = cms.double(24.4),
                wirePropCorrType = cms.int32(0)
            ),
            useUncertDB = cms.bool(True)
        ),
        segmCleanerMode = cms.int32(2)
    ),
    Reco4DAlgoName = cms.string('DTCombinatorialPatternReco4D'),
    debug = cms.untracked.bool(False),
    recHits1DLabel = cms.InputTag("hltDt1DRecHits"),
    recHits2DLabel = cms.InputTag("dt2DSegments")
)


process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigis"),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityTTIdErrors")
)


process.hltEcalDigisFromGPU = cms.EDProducer("EcalCPUDigisProducer",
    digisInLabelEB = cms.InputTag("hltEcalDigisGPU","ebDigis"),
    digisInLabelEE = cms.InputTag("hltEcalDigisGPU","eeDigis"),
    digisOutLabelEB = cms.string('ebDigis'),
    digisOutLabelEE = cms.string('eeDigis'),
    produceDummyIntegrityCollections = cms.bool(False)
)


process.hltEcalDigisGPU = cms.EDProducer("EcalRawToDigiGPU",
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    InputLabel = cms.InputTag("rawDataCollector"),
    digisLabelEB = cms.string('ebDigis'),
    digisLabelEE = cms.string('eeDigis'),
    maxChannelsEB = cms.uint32(61200),
    maxChannelsEE = cms.uint32(14648)
)


process.hltEcalDigisLegacy = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
    bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4.0),
        cThreshold_double = cms.double(10.0),
        cThreshold_endcap = cms.double(15.0),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.04),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(-0.024),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2.0),
        tightenCrack_e1_single = cms.double(2.0),
        tightenCrack_e4e1_single = cms.double(3.0),
        tightenCrack_e6e2_double = cms.double(3.0)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50.0),
    logWarningEtThreshold_EE_FE = cms.double(50.0),
    recoverEBFE = cms.bool(False),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(False),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8.0),
    skipTimeCalib = cms.bool(False),
    sum8ChannelRecoveryThreshold = cms.double(0.0),
    triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigis","EcalTriggerPrimitives")
)


process.hltEcalUncalibRecHitFromSoA = cms.EDProducer("EcalUncalibRecHitConvertGPU2CPUFormat",
    isPhase2 = cms.bool(False),
    recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
    recHitsLabelGPUEB = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEB"),
    recHitsLabelGPUEE = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEE")
)


process.hltEcalUncalibRecHitGPU = cms.EDProducer("EcalUncalibRecHitProducerGPU",
    EBtimeConstantTerm = cms.double(0.6),
    EBtimeFitLimits_Lower = cms.double(0.2),
    EBtimeFitLimits_Upper = cms.double(1.4),
    EBtimeNconst = cms.double(28.5),
    EEtimeConstantTerm = cms.double(1.0),
    EEtimeFitLimits_Lower = cms.double(0.2),
    EEtimeFitLimits_Upper = cms.double(1.4),
    EEtimeNconst = cms.double(31.8),
    amplitudeThresholdEB = cms.double(10.0),
    amplitudeThresholdEE = cms.double(10.0),
    digisLabelEB = cms.InputTag("hltEcalDigisGPU","ebDigis"),
    digisLabelEE = cms.InputTag("hltEcalDigisGPU","eeDigis"),
    kernelMinimizeThreads = cms.untracked.vuint32(32, 1, 1),
    outOfTimeThresholdGain12mEB = cms.double(1000.0),
    outOfTimeThresholdGain12mEE = cms.double(1000.0),
    outOfTimeThresholdGain12pEB = cms.double(1000.0),
    outOfTimeThresholdGain12pEE = cms.double(1000.0),
    outOfTimeThresholdGain61mEB = cms.double(1000.0),
    outOfTimeThresholdGain61mEE = cms.double(1000.0),
    outOfTimeThresholdGain61pEB = cms.double(1000.0),
    outOfTimeThresholdGain61pEE = cms.double(1000.0),
    recHitsLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelEE = cms.string('EcalUncalibRecHitsEE'),
    shouldRunTimingComputation = cms.bool(True)
)


process.hltEcalUncalibRecHitLegacy = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("hltEcalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("hltEcalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(
            -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
            91.01147, -50.35761, 11.05621
        ),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(
            -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
            140.7432, -75.41106, 16.20277
        ),
        EEtimeNconst = cms.double(31.8),
        activeBXs = cms.vint32(
            -5, -4, -3, -2, -1,
            0, 1, 2, 3, 4
        ),
        addPedestalUncertaintyEB = cms.double(0.0),
        addPedestalUncertaintyEE = cms.double(0.0),
        ampErrorCalculation = cms.bool(False),
        amplitudeThresholdEB = cms.double(10.0),
        amplitudeThresholdEE = cms.double(10.0),
        doPrefitEB = cms.bool(False),
        doPrefitEE = cms.bool(False),
        dynamicPedestalsEB = cms.bool(False),
        dynamicPedestalsEE = cms.bool(False),
        gainSwitchUseMaxSampleEB = cms.bool(True),
        gainSwitchUseMaxSampleEE = cms.bool(False),
        mitigateBadSamplesEB = cms.bool(False),
        mitigateBadSamplesEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(1000.0),
        outOfTimeThresholdGain12mEE = cms.double(1000.0),
        outOfTimeThresholdGain12pEB = cms.double(1000.0),
        outOfTimeThresholdGain12pEE = cms.double(1000.0),
        outOfTimeThresholdGain61mEB = cms.double(1000.0),
        outOfTimeThresholdGain61mEE = cms.double(1000.0),
        outOfTimeThresholdGain61pEB = cms.double(1000.0),
        outOfTimeThresholdGain61pEE = cms.double(1000.0),
        prefitMaxChiSqEB = cms.double(25.0),
        prefitMaxChiSqEE = cms.double(10.0),
        selectiveBadSampleCriteriaEB = cms.bool(False),
        selectiveBadSampleCriteriaEE = cms.bool(False),
        simplifiedNoiseModelForGainSwitch = cms.bool(True),
        timealgo = cms.string('RatioMethod'),
        useLumiInfoRunHeader = cms.bool(False)
    )
)


process.hltEcalUncalibRecHitSoA = cms.EDProducer("EcalCPUUncalibRecHitProducer",
    containsTimingInformation = cms.bool(True),
    isPhase2 = cms.bool(False),
    recHitsInLabelEB = cms.InputTag("hltEcalUncalibRecHitGPU","EcalUncalibRecHitsEB"),
    recHitsInLabelEE = cms.InputTag("hltEcalUncalibRecHitGPU","EcalUncalibRecHitsEE"),
    recHitsOutLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsOutLabelEE = cms.string('EcalUncalibRecHitsEE')
)


process.hltFEDSelectorTCDS = cms.EDProducer("EvFFEDSelector",
    fedList = cms.vuint32(1024, 1025),
    inputTag = cms.InputTag("rawDataCollector")
)


process.hltFixedGridRhoFastjetAll = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(5.0),
    pfCandidatesTag = cms.InputTag("hltParticleFlow")
)


process.hltFixedGridRhoFastjetAllCalo = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(5.0),
    pfCandidatesTag = cms.InputTag("hltTowerMakerForAll")
)


process.hltGemRecHits = cms.EDProducer("GEMRecHitProducer",
    applyMasking = cms.bool(False),
    ge21Off = cms.bool(False),
    gemDigiLabel = cms.InputTag("hltMuonGEMDigis"),
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    )
)


process.hltGemSegments = cms.EDProducer("GEMSegmentProducer",
    algo_name = cms.string('GEMSegmentAlgorithm'),
    algo_pset = cms.PSet(
        clusterOnlySameBXRecHits = cms.bool(True),
        dEtaChainBoxMax = cms.double(0.05),
        dPhiChainBoxMax = cms.double(0.02),
        dXclusBoxMax = cms.double(1.0),
        dYclusBoxMax = cms.double(5.0),
        maxRecHitsInCluster = cms.int32(4),
        minHitsPerSegment = cms.uint32(2),
        preClustering = cms.bool(True),
        preClusteringUseChaining = cms.bool(True)
    ),
    ge0_name = cms.string('GE0SegAlgoRU'),
    ge0_pset = cms.PSet(
        allowWideSegments = cms.bool(True),
        doCollisions = cms.bool(True),
        maxChi2Additional = cms.double(100.0),
        maxChi2GoodSeg = cms.double(50.0),
        maxChi2Prune = cms.double(50.0),
        maxETASeeds = cms.double(0.1),
        maxNumberOfHits = cms.uint32(300),
        maxNumberOfHitsPerLayer = cms.uint32(100),
        maxPhiAdditional = cms.double(0.001096605744),
        maxPhiSeeds = cms.double(0.001096605744),
        maxTOFDiff = cms.double(25.0),
        minNumberOfHits = cms.uint32(4),
        requireCentralBX = cms.bool(True)
    ),
    gemRecHitLabel = cms.InputTag("hltGemRecHits")
)


process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    DmxFWId = cms.uint32(0),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    TMTCheck = cms.bool(True),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltGtStage2ObjectMap = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("hltGtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    EmulateBxInEvent = cms.int32(1),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1DataBxInEvent = cms.int32(5),
    MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    PrescaleSet = cms.uint32(1),
    PrintL1Menu = cms.untracked.bool(False),
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    RequireMenuToMatchAlgoBlkInput = cms.bool(True),
    TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.untracked.int32(0),
    resetPSCountersEachLumiSec = cms.bool(True),
    semiRandomInitialPSCounters = cms.bool(False),
    useMuonShowers = cms.bool(True)
)


process.hltHbherecoFromGPU = cms.EDProducer("HcalCPURecHitsProducer",
    produceLegacy = cms.bool(True),
    produceSoA = cms.bool(True),
    recHitsLegacyLabelOut = cms.string(''),
    recHitsM0LabelIn = cms.InputTag("hltHbherecoGPU"),
    recHitsM0LabelOut = cms.string('')
)


process.hltHbherecoGPU = cms.EDProducer("HBHERecHitProducerGPU",
    applyTimeSlew = cms.bool(True),
    digisLabelF01HE = cms.InputTag("hltHcalDigisGPU"),
    digisLabelF3HB = cms.InputTag("hltHcalDigisGPU"),
    digisLabelF5HB = cms.InputTag("hltHcalDigisGPU"),
    firstSampleShift = cms.int32(0),
    kernelMinimizeThreads = cms.vuint32(16, 1, 1),
    kprep1dChannelsPerBlock = cms.uint32(32),
    maxTimeSamples = cms.uint32(10),
    meanTime = cms.double(0.0),
    recHitsLabelM0HBHE = cms.string(''),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    slopeTimeSlewParameters = cms.vdouble(-3.178648, -1.5610227, -1.075824),
    timeSigmaHPD = cms.double(5.0),
    timeSigmaSiPM = cms.double(2.5),
    tmaxTimeSlewParameters = cms.vdouble(16.0, 10.0, 6.25),
    ts4Thresh = cms.double(0.0),
    tzeroTimeSlewParameters = cms.vdouble(23.960177, 11.977461, 9.109694),
    useEffectivePedestals = cms.bool(True)
)


process.hltHbherecoLegacy = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        activeBXs = cms.vint32(
            -3, -2, -1, 0, 1,
            2, 3, 4
        ),
        applyLegacyHBMCorrection = cms.bool(False),
        applyPedConstraint = cms.bool(False),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(False),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        calculateArrivalTime = cms.bool(False),
        chiSqSwitch = cms.double(-1.0),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        deltaChiSqThresh = cms.double(0.001),
        dynamicPed = cms.bool(False),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        nMaxItersMin = cms.int32(50),
        nMaxItersNNLS = cms.int32(500),
        nnlsThresh = cms.double(1e-11),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 20000.0, 30000.0),
        ts4Min = cms.double(0.0),
        ts4Thresh = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(False),
        useMahi = cms.bool(True)
    ),
    digiLabelQIE11 = cms.InputTag("hltHcalDigis"),
    digiLabelQIE8 = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    0.0, 100.0, -50.0, 0.0, -15.0,
                    0.15
                )
            ),
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    100.0, 2000.0, -50.0, 0.0, -5.0,
                    0.05
                )
            ),
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    2000.0, 1000000.0, -50.0, 0.0, 95.0,
                    0.0
                )
            ),
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0,
                    0.0
                )
            )
        )
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(False),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5.0, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250.0, 500.0, 100000.0),
        LinearCut = cms.vdouble(-3.0, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20.0, 100.0, 100000.0),
        MinimumChargeThreshold = cms.double(20.0),
        MinimumTS4TS5Threshold = cms.double(100.0),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20.0, 100.0, 100000.0),
        RightSlopeCut = cms.vdouble(5.0, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150.0, 200.0, 100000.0),
        RightSlopeThreshold = cms.vdouble(250.0, 400.0, 100000.0),
        TS3TS4ChargeThreshold = cms.double(70.0),
        TS3TS4UpperChargeThreshold = cms.double(20.0),
        TS4TS5ChargeThreshold = cms.double(70.0),
        TS4TS5LowerCut = cms.vdouble(
            -1.0, -0.7, -0.5, -0.4, -0.3,
            0.1
        ),
        TS4TS5LowerThreshold = cms.vdouble(
            100.0, 120.0, 160.0, 200.0, 300.0,
            500.0
        ),
        TS4TS5UpperCut = cms.vdouble(1.0, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70.0, 90.0, 100.0, 400.0),
        TS5TS6ChargeThreshold = cms.double(70.0),
        TS5TS6UpperChargeThreshold = cms.double(20.0),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(True),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(False),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(False),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(False),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(False),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    tsFromDB = cms.bool(False),
    use8ts = cms.bool(True)
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.hltHcalDigisGPU = cms.EDProducer("HcalDigisProducerGPU",
    digisLabelF01HE = cms.string(''),
    digisLabelF3HB = cms.string(''),
    digisLabelF5HB = cms.string(''),
    hbheDigisLabel = cms.InputTag("hltHcalDigis"),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    qie11DigiLabel = cms.InputTag("hltHcalDigis")
)


process.hltHfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hltHfreco = cms.EDProducer("HFPhase1Reconstructor",
    HFStripFilter = cms.PSet(
        gap = cms.int32(2),
        lstrips = cms.int32(2),
        maxStripTime = cms.double(10.0),
        maxThreshold = cms.double(100.0),
        seedHitIetaMax = cms.int32(35),
        stripThreshold = cms.double(40.0),
        timeMax = cms.double(6.0),
        verboseLevel = cms.untracked.int32(10),
        wedgeCut = cms.double(0.05)
    ),
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            2.0, 0.0, 1.0, 0.0, 0.0,
            1.0, 0.0, 1.0, 0.0, 2.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            1.0
        ),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(False),
    inputLabel = cms.InputTag("hltHfprereco"),
    runHFStripFilter = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    useChannelQualityFromDB = cms.bool(False)
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    hfTimingTrustParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltHtMhtFromPVForMC = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltCaloJetFromPV"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(30.0),
    minPtJetMht = cms.double(20.0),
    pfCandidatesLabel = cms.InputTag(""),
    usePt = cms.bool(False)
)


process.hltIter0IterL3FromL1MuonCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('none'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksFiltered"),
    useHitsSplitting = cms.bool(True)
)


process.hltIter0IterL3FromL1MuonCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0IterL3FromL1MuonCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracksInRegionL1"),
    InputVertexCollection = cms.InputTag(""),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    includeFourthHit = cms.bool(True),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksFiltered = cms.EDProducer("MuonHLTSeedMVAClassifier",
    L1Muon = cms.InputTag("hltGtStage2Digis","Muon"),
    L2Muon = cms.InputTag("hltL2MuonCandidates"),
    baseScore = cms.double(0.5),
    doSort = cms.bool(False),
    etaEdge = cms.double(1.2),
    isFromL1 = cms.bool(True),
    minL1Qual = cms.int32(7),
    mvaCutB = cms.double(0.01),
    mvaCutE = cms.double(0.01),
    mvaFileBL1 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0FromL1_PatatrackSeeds_barrel_v2.xml'),
    mvaFileBL2 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0_PatatrackSeeds_barrel_v2.xml'),
    mvaFileEL1 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0FromL1_PatatrackSeeds_endcap_v2.xml'),
    mvaFileEL2 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0_PatatrackSeeds_endcap_v2.xml'),
    mvaScaleMeanBL1 = cms.vdouble(
        0.0005000589710660383, 3.90864688207247e-06, 5.566857527819724e-06, 2.919765272506742e-05, 0.0020554125627069656,
        0.00037638302502636416, 0.17319245569742575, -0.001928435311705264
    ),
    mvaScaleMeanBL2 = cms.vdouble(
        0.0005535405438531338, 5.803137756667417e-06, 9.844857031022169e-06, 8.572205780682784e-06, 0.0015762679722632618,
        0.0004395397563024067, 0.1374567309015325, -0.005115438205054733, 0.11749212456078427, 6.10630569023574e-05
    ),
    mvaScaleMeanEL1 = cms.vdouble(
        0.0004633287331326438, 4.336517990150388e-06, 1.1353478376025763e-05, -0.0009703999978722195, -0.016733916560431213,
        0.0010338859165970008, 0.1664362346287898, -0.002093062022327288
    ),
    mvaScaleMeanEL2 = cms.vdouble(
        0.00047677144995220935, 3.6745265753688003e-06, 8.865597384997202e-06, 0.0003035250572254308, -0.017277139191991336,
        0.0007614700645923214, 0.13098441610679598, -0.004062335797232639, 0.10313449419117496, 8.091070691633311e-05
    ),
    mvaScaleStdBL1 = cms.vdouble(
        0.0024104956748896007, 0.000265014770862918, 0.0007474433025576554, 0.07076843921543456, 0.8267930143339328,
        0.5908013434667966, 0.16945213299167364, 0.19343332776069666
    ),
    mvaScaleStdBL2 = cms.vdouble(
        0.002626537945220411, 0.004217812355595011, 0.01003037371073428, 0.08030848788317736, 0.8112437912866772,
        0.682723351939253, 0.14357759358396366, 0.1714659927555431, 0.12492124275832932, 0.14997195939803123
    ),
    mvaScaleStdEL1 = cms.vdouble(
        0.0017591716932616446, 0.00043554653252872314, 0.0018509069108135767, 0.3154887917554714, 1.0554267175028256,
        0.46607446165391897, 0.1599804481244901, 0.1802872646042384
    ),
    mvaScaleStdEL2 = cms.vdouble(
        0.0017644245219973625, 0.00014737438911735824, 0.0005815417377127688, 0.32486307205392545, 0.9554477166210787,
        0.6368300706332602, 0.18228633778650377, 0.17472670187127687, 0.1069305400952516, 0.12396350430658183
    ),
    nSeedsMaxB = cms.int32(99999),
    nSeedsMaxE = cms.int32(99999),
    rejectAll = cms.bool(False),
    src = cms.InputTag("hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks")
)


process.hltIter0IterL3FromL1MuonTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 3.40282346639e+38),
            d0err_par = cms.vdouble(0.001, 0.001, 3.40282346639e+38),
            dr_exp = cms.vint32(4, 4, 2147483647),
            dr_par1 = cms.vdouble(0.4, 0.4, 3.40282346639e+38),
            dr_par2 = cms.vdouble(0.3, 0.3, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 2147483647),
            dz_par1 = cms.vdouble(0.4, 0.4, 3.40282346639e+38),
            dz_par2 = cms.vdouble(0.35, 0.35, 3.40282346639e+38)
        ),
        maxChi2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 100.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 4),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0IterL3FromL1MuonCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter0IterL3FromL1MuonTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0IterL3FromL1MuonTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0IterL3FromL1MuonTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0IterL3FromL1MuonCtfWithMaterialTracks")
)


process.hltIter0IterL3MuonCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('none'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltIter0IterL3MuonPixelSeedsFromPixelTracksFiltered"),
    useHitsSplitting = cms.bool(True)
)


process.hltIter0IterL3MuonCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0IterL3MuonCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0IterL3MuonPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracksInRegionL2"),
    InputVertexCollection = cms.InputTag(""),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    includeFourthHit = cms.bool(True),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0IterL3MuonPixelSeedsFromPixelTracksFiltered = cms.EDProducer("MuonHLTSeedMVAClassifier",
    L1Muon = cms.InputTag("hltGtStage2Digis","Muon"),
    L2Muon = cms.InputTag("hltL2MuonCandidates"),
    baseScore = cms.double(0.5),
    doSort = cms.bool(False),
    etaEdge = cms.double(1.2),
    isFromL1 = cms.bool(False),
    minL1Qual = cms.int32(7),
    mvaCutB = cms.double(0.01),
    mvaCutE = cms.double(0.01),
    mvaFileBL1 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0FromL1_PatatrackSeeds_barrel_v2.xml'),
    mvaFileBL2 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0_PatatrackSeeds_barrel_v2.xml'),
    mvaFileEL1 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0FromL1_PatatrackSeeds_endcap_v2.xml'),
    mvaFileEL2 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0_PatatrackSeeds_endcap_v2.xml'),
    mvaScaleMeanBL1 = cms.vdouble(
        0.0005000589710660383, 3.90864688207247e-06, 5.566857527819724e-06, 2.919765272506742e-05, 0.0020554125627069656,
        0.00037638302502636416, 0.17319245569742575, -0.001928435311705264
    ),
    mvaScaleMeanBL2 = cms.vdouble(
        0.0005535405438531338, 5.803137756667417e-06, 9.844857031022169e-06, 8.572205780682784e-06, 0.0015762679722632618,
        0.0004395397563024067, 0.1374567309015325, -0.005115438205054733, 0.11749212456078427, 6.10630569023574e-05
    ),
    mvaScaleMeanEL1 = cms.vdouble(
        0.0004633287331326438, 4.336517990150388e-06, 1.1353478376025763e-05, -0.0009703999978722195, -0.016733916560431213,
        0.0010338859165970008, 0.1664362346287898, -0.002093062022327288
    ),
    mvaScaleMeanEL2 = cms.vdouble(
        0.00047677144995220935, 3.6745265753688003e-06, 8.865597384997202e-06, 0.0003035250572254308, -0.017277139191991336,
        0.0007614700645923214, 0.13098441610679598, -0.004062335797232639, 0.10313449419117496, 8.091070691633311e-05
    ),
    mvaScaleStdBL1 = cms.vdouble(
        0.0024104956748896007, 0.000265014770862918, 0.0007474433025576554, 0.07076843921543456, 0.8267930143339328,
        0.5908013434667966, 0.16945213299167364, 0.19343332776069666
    ),
    mvaScaleStdBL2 = cms.vdouble(
        0.002626537945220411, 0.004217812355595011, 0.01003037371073428, 0.08030848788317736, 0.8112437912866772,
        0.682723351939253, 0.14357759358396366, 0.1714659927555431, 0.12492124275832932, 0.14997195939803123
    ),
    mvaScaleStdEL1 = cms.vdouble(
        0.0017591716932616446, 0.00043554653252872314, 0.0018509069108135767, 0.3154887917554714, 1.0554267175028256,
        0.46607446165391897, 0.1599804481244901, 0.1802872646042384
    ),
    mvaScaleStdEL2 = cms.vdouble(
        0.0017644245219973625, 0.00014737438911735824, 0.0005815417377127688, 0.32486307205392545, 0.9554477166210787,
        0.6368300706332602, 0.18228633778650377, 0.17472670187127687, 0.1069305400952516, 0.12396350430658183
    ),
    nSeedsMaxB = cms.int32(99999),
    nSeedsMaxE = cms.int32(99999),
    rejectAll = cms.bool(False),
    src = cms.InputTag("hltIter0IterL3MuonPixelSeedsFromPixelTracks")
)


process.hltIter0IterL3MuonTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 3.40282346639e+38),
            d0err_par = cms.vdouble(0.001, 0.001, 3.40282346639e+38),
            dr_exp = cms.vint32(4, 4, 2147483647),
            dr_par1 = cms.vdouble(0.4, 0.4, 3.40282346639e+38),
            dr_par2 = cms.vdouble(0.3, 0.3, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 2147483647),
            dz_par1 = cms.vdouble(0.4, 0.4, 3.40282346639e+38),
            dz_par2 = cms.vdouble(0.35, 0.35, 3.40282346639e+38)
        ),
        maxChi2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 100.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 4),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0IterL3MuonCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter0IterL3MuonTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0IterL3MuonTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0IterL3MuonTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0IterL3MuonCtfWithMaterialTracks")
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracks"),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    includeFourthHit = cms.bool(True),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0PFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(3.40282346639e+38, 0.8, 0.8),
            dr_par2 = cms.vdouble(3.40282346639e+38, 0.6, 0.6)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(3.40282346639e+38, 0.75, 0.75),
            dz_par2 = cms.vdouble(3.40282346639e+38, 0.5, 0.5)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIterL3FromL1MuonPixelTracksTrackingRegions = cms.EDProducer("L1MuonSeededTrackingRegionsEDProducer",
    CentralBxOnly = cms.bool(True),
    L1MaxEta = cms.double(2.5),
    L1MinPt = cms.double(0.0),
    L1MinQuality = cms.uint32(7),
    Propagator = cms.string('SteppingHelixPropagatorAny'),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        deltaEtas = cms.vdouble(0.35, 0.35, 0.35, 0.35),
        deltaPhis = cms.vdouble(1.0, 0.8, 0.6, 0.3),
        input = cms.InputTag("hltL1MuonsPt0"),
        maxNRegions = cms.int32(5),
        maxNVertices = cms.int32(1),
        measurementTrackerName = cms.InputTag(""),
        mode = cms.string('BeamSpotSigma'),
        nSigmaZBeamSpot = cms.double(4.0),
        nSigmaZVertex = cms.double(3.0),
        originRadius = cms.double(0.2),
        precise = cms.bool(True),
        ptMin = cms.double(0.0),
        ptRanges = cms.vdouble(0.0, 10.0, 15.0, 20.0, 1e+64),
        searchOpt = cms.bool(False),
        vertexCollection = cms.InputTag("notUsed"),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVetex = cms.double(0.2)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    SetMinPtBarrelTo = cms.double(3.5),
    SetMinPtEndcapTo = cms.double(1.0)
)


process.hltIterL3GlbMuon = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutGEM = cms.double(1.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            GEMRecHitLabel = cms.InputTag("hltGemRecHits"),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = cms.bool(True),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaEta = cms.double(0.2),
            DeltaPhi = cms.double(0.15),
            DeltaR = cms.double(0.025),
            DeltaZ = cms.double(24.2),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.bool(True),
            Eta_min = cms.double(0.1),
            MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
            OnDemand = cms.int32(-1),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.bool(True),
            Phi_min = cms.double(0.1),
            Pt_fixed = cms.bool(False),
            Pt_min = cms.double(3.0),
            Rescale_Dz = cms.double(4.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseVertex = cms.bool(False),
            Z_fixed = cms.bool(False),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
            maxRegions = cms.int32(2),
            precise = cms.bool(True),
            vertexCollection = cms.InputTag("pixelVertices")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltIterL3MuonAndMuonFromL1Merged"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(9999.0),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("Notused")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring(
            'hltESPSmartPropagatorAny',
            'SteppingHelixPropagatorAny',
            'hltESPSmartPropagator',
            'hltESPSteppingHelixPropagatorOpposite'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltIterL3MuonAndMuonFromL1Merged = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIterL3MuonMerged", "hltIter0IterL3FromL1MuonTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIterL3MuonMerged", "hltIter0IterL3FromL1MuonTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIterL3MuonCandidates = cms.EDProducer("L3MuonCandidateProducerFromMuons",
    DisplacedReconstruction = cms.bool(False),
    InputObjects = cms.InputTag("hltIterL3Muons")
)


process.hltIterL3MuonMerged = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIterL3OIMuonTrackSelectionHighPurity", "hltIter0IterL3MuonTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIterL3OIMuonTrackSelectionHighPurity", "hltIter0IterL3MuonTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIterL3MuonPixelTracksTrackingRegions = cms.EDProducer("MuonTrackingRegionByPtEDProducer",
    DeltaR = cms.double(0.025),
    DeltaZ = cms.double(24.2),
    MeasurementTrackerName = cms.InputTag(""),
    OnDemand = cms.int32(-1),
    Pt_fixed = cms.bool(True),
    Pt_min = cms.double(0.0),
    Rescale_Dz = cms.double(4.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    deltaEtas = cms.vdouble(0.2, 0.2, 0.2),
    deltaPhis = cms.vdouble(0.75, 0.45, 0.225),
    input = cms.InputTag("hltL2SelectorForL3IO"),
    maxRegions = cms.int32(5),
    precise = cms.bool(True),
    ptRanges = cms.vdouble(0.0, 15.0, 20.0, 1e+64),
    vertexCollection = cms.InputTag("notUsed")
)


process.hltIterL3MuonTracks = cms.EDProducer("HLTMuonTrackSelector",
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    muon = cms.InputTag("hltIterL3Muons"),
    originalMVAVals = cms.InputTag("none"),
    track = cms.InputTag("hltIterL3MuonAndMuonFromL1Merged")
)


process.hltIterL3Muons = cms.EDProducer("MuonIDFilterProducerForHLT",
    allowedTypeMask = cms.uint32(0),
    applyTriggerIdLoose = cms.bool(True),
    inputMuonCollection = cms.InputTag("hltIterL3MuonsNoID"),
    maxNormalizedChi2 = cms.double(9999.0),
    minNMuonHits = cms.int32(0),
    minNMuonStations = cms.int32(0),
    minNTrkLayers = cms.int32(0),
    minPixHits = cms.int32(0),
    minPixLayer = cms.int32(0),
    minPt = cms.double(0.0),
    minTrkHits = cms.int32(0),
    requiredTypeMask = cms.uint32(0),
    typeMuon = cms.uint32(0)
)


process.hltIterL3MuonsFromL2LinksCombination = cms.EDProducer("L3TrackLinksCombiner",
    labels = cms.VInputTag("hltL3MuonsIterL3OI", "hltL3MuonsIterL3IO")
)


process.hltIterL3MuonsNoID = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("Notused"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("Notused"),
            EERecHitCollectionLabel = cms.InputTag("Notused"),
            HBHERecHitCollectionLabel = cms.InputTag("Notused"),
            HORecHitCollectionLabel = cms.InputTag("Notused"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("Notused"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("Notused"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("Notused"),
            EERecHitCollectionLabel = cms.InputTag("Notused"),
            HBHERecHitCollectionLabel = cms.InputTag("Notused"),
            HORecHitCollectionLabel = cms.InputTag("Notused"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            CSCsegments = cms.InputTag("hltCscSegments"),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(100.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(2.7),
            DTsegments = cms.InputTag("hltDt4DSegments"),
            DoWireCorr = cms.bool(False),
            DropTheta = cms.bool(True),
            HitError = cms.double(6.0),
            HitsMin = cms.int32(5),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(10000.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorCSC = cms.double(7.4),
        ErrorDT = cms.double(6.0),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("Notused"),
        DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("Notused"),
        EERecHitCollectionLabel = cms.InputTag("Notused"),
        GEMSegmentCollectionLabel = cms.InputTag("hltGemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("Notused"),
        HORecHitCollectionLabel = cms.InputTag("Notused"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(False),
        useGEM = cms.bool(True),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("hltOnlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.01),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("hltIter0IterL3FromL1MuonTrackSelectionHighPurity")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(False)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(False),
    fillEnergy = cms.bool(False),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(False),
    fillIsolation = cms.bool(False),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(False),
    fillTrackerKink = cms.bool(False),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("hltIterL3MuonAndMuonFromL1Merged", "hltIterL3GlbMuon", "hltL2Muons:UpdatedAtVtx"),
    inputCollectionTypes = cms.vstring(
        'inner tracks',
        'links',
        'outer tracks'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(0.0),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(2.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    pvInputTag = cms.InputTag("offlinePrimaryVertices"),
    runArbitrationCleaner = cms.bool(False),
    selectHighPurity = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(False),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(False)
)


process.hltIterL3OIL3MuonCandidates = cms.EDProducer("L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag("hltIterL3OIL3MuonsLinksCombination"),
    InputObjects = cms.InputTag("hltIterL3OIL3Muons"),
    MuonPtOption = cms.string('Tracker')
)


process.hltIterL3OIL3Muons = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsIterL3OI")
)


process.hltIterL3OIL3MuonsLinksCombination = cms.EDProducer("L3TrackLinksCombiner",
    labels = cms.VInputTag("hltL3MuonsIterL3OI")
)


process.hltIterL3OIMuCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('iter10'),
    Fitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string('hltESPMeasurementTracker'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIterL3OITrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltIterL3OIMuonTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(True),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 3.40282346639e+38),
            d0err_par = cms.vdouble(0.001, 0.001, 3.40282346639e+38),
            dr_exp = cms.vint32(4, 4, 2147483647),
            dr_par1 = cms.vdouble(0.4, 0.4, 3.40282346639e+38),
            dr_par2 = cms.vdouble(0.3, 0.3, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 2147483647),
            dz_par1 = cms.vdouble(0.4, 0.4, 3.40282346639e+38),
            dz_par2 = cms.vdouble(0.35, 0.35, 3.40282346639e+38)
        ),
        maxChi2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 100.0),
        maxLostLayers = cms.vint32(4, 3, 2),
        min3DLayers = cms.vint32(1, 2, 1),
        minLayers = cms.vint32(3, 5, 5),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 1)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIterL3OIMuCtfWithMaterialTracks"),
    vertices = cms.InputTag("Notused")
)


process.hltIterL3OIMuonTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIterL3OIMuonTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIterL3OIMuonTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIterL3OIMuCtfWithMaterialTracks")
)


process.hltIterL3OISeedsFromL2Muons = cms.EDProducer("TSGForOIDNN",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    debug = cms.untracked.bool(False),
    dnnMetadataPath = cms.string('RecoMuon/TrackerSeedGenerator/data/OIseeding/DNNclassifier_Run3_metadata.json'),
    estimator = cms.string('hltESPChi2MeasurementEstimator100'),
    fixedErrorRescaleFactorForHitless = cms.double(2.0),
    getStrategyFromDNN = cms.bool(True),
    hitsToTry = cms.int32(1),
    layersToTry = cms.int32(2),
    maxEtaForTOB = cms.double(1.8),
    maxHitDoubletSeeds = cms.uint32(0),
    maxHitSeeds = cms.uint32(1),
    maxHitlessSeeds = cms.uint32(5),
    maxHitlessSeedsIP = cms.uint32(5),
    maxHitlessSeedsMuS = cms.uint32(0),
    maxSeeds = cms.uint32(20),
    minEtaForTEC = cms.double(0.7),
    propagatorName = cms.string('PropagatorWithMaterialParabolicMf'),
    src = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    useRegressor = cms.bool(False)
)


process.hltIterL3OITrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(True),
    src = cms.InputTag("hltIterL3OISeedsFromL2Muons"),
    useHitsSplitting = cms.bool(False)
)


process.hltL1MuonsPt0 = cms.EDProducer("HLTL1TMuonSelector",
    CentralBxOnly = cms.bool(True),
    InputObjects = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MaxEta = cms.double(5.0),
    L1MinPt = cms.double(-1.0),
    L1MinQuality = cms.uint32(7)
)


process.hltL2MuonCandidates = cms.EDProducer("L2MuonCandidateProducer",
    InputObjects = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL2MuonSeeds = cms.EDProducer("L2MuonSeedGeneratorFromL1T",
    CentralBxOnly = cms.bool(True),
    EtaMatchingBins = cms.vdouble(0.0, 2.5),
    GMTReadoutCollection = cms.InputTag(""),
    InputObjects = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MaxEta = cms.double(2.5),
    L1MinPt = cms.double(0.0),
    L1MinQuality = cms.uint32(7),
    MatchDR = cms.vdouble(0.3),
    MatchType = cms.uint32(0),
    OfflineSeedLabel = cms.untracked.InputTag("hltL2OfflineMuonSeeds"),
    Propagator = cms.string('SteppingHelixPropagatorAny'),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    SetMinPtBarrelTo = cms.double(3.5),
    SetMinPtEndcapTo = cms.double(1.0),
    SortType = cms.uint32(0),
    UseOfflineSeed = cms.untracked.bool(True),
    UseUnassociatedL1 = cms.bool(False)
)


process.hltL2Muons = cms.EDProducer("L2MuonProducer",
    DoSeedRefit = cms.bool(False),
    InputObjects = cms.InputTag("hltL2MuonSeeds"),
    L2TrajBuilderParameters = cms.PSet(
        BWFilterParameters = cms.PSet(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('outsideIn'),
            GEMRecSegmentLabel = cms.InputTag("hltGemRecHits"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
        ),
        DoBackwardFilter = cms.bool(True),
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableGEMMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('insideOut'),
            GEMRecSegmentLabel = cms.InputTag("hltGemRecHits"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RescaleError = cms.double(100.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    SeedTransformerParameters = cms.PSet(
        Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        NMinRecHits = cms.uint32(2),
        Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        RescaleError = cms.double(100.0),
        UseSubRecHits = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring(
            'hltESPFastSteppingHelixPropagatorAny',
            'hltESPFastSteppingHelixPropagatorOpposite'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPosition = cms.vdouble(0.0, 0.0, 0.0),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL2OfflineMuonSeeds = cms.EDProducer("MuonSeedGenerator",
    CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
    CSC_01 = cms.vdouble(
        0.166, 0.0, 0.0, 0.031, 0.0,
        0.0
    ),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    CSC_02 = cms.vdouble(
        0.612, -0.207, 0.0, 0.067, -0.001,
        0.0
    ),
    CSC_03 = cms.vdouble(
        0.787, -0.338, 0.029, 0.101, -0.008,
        0.0
    ),
    CSC_12 = cms.vdouble(
        -0.161, 0.254, -0.047, 0.042, -0.007,
        0.0
    ),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    CSC_13 = cms.vdouble(
        0.901, -1.302, 0.533, 0.045, 0.005,
        0.0
    ),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_14 = cms.vdouble(
        0.606, -0.181, -0.002, 0.111, -0.003,
        0.0
    ),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    CSC_23 = cms.vdouble(
        -0.081, 0.113, -0.029, 0.015, 0.008,
        0.0
    ),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    CSC_24 = cms.vdouble(
        0.004, 0.021, -0.002, 0.053, 0.0,
        0.0
    ),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_34 = cms.vdouble(
        0.062, -0.067, 0.019, 0.021, 0.003,
        0.0
    ),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
    DT_12 = cms.vdouble(
        0.183, 0.054, -0.087, 0.028, 0.002,
        0.0
    ),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13 = cms.vdouble(
        0.315, 0.068, -0.127, 0.051, -0.002,
        0.0
    ),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    DT_14 = cms.vdouble(
        0.359, 0.052, -0.107, 0.072, -0.004,
        0.0
    ),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    DT_23 = cms.vdouble(
        0.13, 0.023, -0.057, 0.028, 0.004,
        0.0
    ),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    DT_24 = cms.vdouble(
        0.176, 0.014, -0.051, 0.051, 0.003,
        0.0
    ),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(
        0.044, 0.004, -0.013, 0.029, 0.003,
        0.0
    ),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    EnableME0Measurement = cms.bool(False),
    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
    OL_1213 = cms.vdouble(
        0.96, -0.737, 0.0, 0.052, 0.0,
        0.0
    ),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222 = cms.vdouble(
        0.848, -0.591, 0.0, 0.062, 0.0,
        0.0
    ),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    OL_1232 = cms.vdouble(
        0.184, 0.0, 0.0, 0.066, 0.0,
        0.0
    ),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    OL_2213 = cms.vdouble(
        0.117, 0.0, 0.0, 0.044, 0.0,
        0.0
    ),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_2222 = cms.vdouble(
        0.107, 0.0, 0.0, 0.04, 0.0,
        0.0
    ),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    SMB_10 = cms.vdouble(
        1.387, -0.038, 0.0, 0.19, 0.0,
        0.0
    ),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    SMB_11 = cms.vdouble(
        1.247, 0.72, -0.802, 0.229, -0.075,
        0.0
    ),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SMB_12 = cms.vdouble(
        2.128, -0.956, 0.0, 0.199, 0.0,
        0.0
    ),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_20 = cms.vdouble(
        1.011, -0.052, 0.0, 0.188, 0.0,
        0.0
    ),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    SMB_21 = cms.vdouble(
        1.043, -0.124, 0.0, 0.183, 0.0,
        0.0
    ),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    SMB_22 = cms.vdouble(
        1.474, -0.758, 0.0, 0.185, 0.0,
        0.0
    ),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    SMB_30 = cms.vdouble(
        0.505, -0.022, 0.0, 0.215, 0.0,
        0.0
    ),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SMB_31 = cms.vdouble(
        0.549, -0.145, 0.0, 0.207, 0.0,
        0.0
    ),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    SMB_32 = cms.vdouble(
        0.67, -0.327, 0.0, 0.22, 0.0,
        0.0
    ),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    SME_11 = cms.vdouble(
        3.295, -1.527, 0.112, 0.378, 0.02,
        0.0
    ),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SME_12 = cms.vdouble(
        0.102, 0.599, 0.0, 0.38, 0.0,
        0.0
    ),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    SME_13 = cms.vdouble(
        -1.286, 1.711, 0.0, 0.356, 0.0,
        0.0
    ),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SME_21 = cms.vdouble(
        -0.529, 1.194, -0.358, 0.472, 0.086,
        0.0
    ),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SME_22 = cms.vdouble(
        -1.207, 1.491, -0.251, 0.189, 0.243,
        0.0
    ),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SME_31 = cms.vdouble(
        -1.594, 1.482, -0.317, 0.487, 0.097,
        0.0
    ),
    SME_32 = cms.vdouble(
        -0.901, 1.333, -0.47, 0.41, 0.073,
        0.0
    ),
    SME_41 = cms.vdouble(
        -0.003, 0.005, 0.005, 0.608, 0.076,
        0.0
    ),
    SME_42 = cms.vdouble(
        -0.003, 0.005, 0.005, 0.608, 0.076,
        0.0
    ),
    beamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    crackWindow = cms.double(0.04),
    deltaEtaCrackSearchWindow = cms.double(0.25),
    deltaEtaSearchWindow = cms.double(0.2),
    deltaPhiSearchWindow = cms.double(0.25),
    scaleDT = cms.bool(True)
)


process.hltL2SelectorForL3IO = cms.EDProducer("HLTMuonL2SelectorForL3IO",
    InputLinks = cms.InputTag("hltIterL3OIL3MuonsLinksCombination"),
    MaxNormalizedChi2 = cms.double(20.0),
    MaxPtDifference = cms.double(0.3),
    MinNhits = cms.int32(1),
    MinNmuonHits = cms.int32(1),
    applyL3Filters = cms.bool(False),
    l2Src = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    l3OISrc = cms.InputTag("hltIterL3OIL3MuonCandidates")
)


process.hltL3MuonsIterL3IO = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutGEM = cms.double(1.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            GEMRecHitLabel = cms.InputTag("hltGemRecHits"),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = cms.bool(True),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaEta = cms.double(0.04),
            DeltaPhi = cms.double(0.15),
            DeltaR = cms.double(0.025),
            DeltaZ = cms.double(24.2),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.bool(True),
            Eta_min = cms.double(0.1),
            MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
            OnDemand = cms.int32(-1),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.bool(True),
            Phi_min = cms.double(0.1),
            Pt_fixed = cms.bool(True),
            Pt_min = cms.double(3.0),
            Rescale_Dz = cms.double(4.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseVertex = cms.bool(False),
            Z_fixed = cms.bool(True),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            input = cms.InputTag("hltL2SelectorForL3IO"),
            maxRegions = cms.int32(2),
            precise = cms.bool(True),
            vertexCollection = cms.InputTag("pixelVertices")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        matchToSeeds = cms.bool(True),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltIter0IterL3MuonTrackSelectionHighPurity"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(9999.0),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("hltTrimmedPixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring(
            'hltESPSmartPropagatorAny',
            'SteppingHelixPropagatorAny',
            'hltESPSmartPropagator',
            'hltESPSteppingHelixPropagatorOpposite'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3MuonsIterL3Links = cms.EDProducer("MuonLinksProducer",
    inputCollection = cms.InputTag("hltIterL3Muons")
)


process.hltL3MuonsIterL3OI = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutGEM = cms.double(1.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            GEMRecHitLabel = cms.InputTag("hltGemRecHits"),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = cms.bool(True),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaEta = cms.double(0.2),
            DeltaPhi = cms.double(0.15),
            DeltaR = cms.double(0.025),
            DeltaZ = cms.double(24.2),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.bool(True),
            Eta_min = cms.double(0.1),
            MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
            OnDemand = cms.int32(-1),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.bool(True),
            Phi_min = cms.double(0.1),
            Pt_fixed = cms.bool(False),
            Pt_min = cms.double(3.0),
            Rescale_Dz = cms.double(4.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseVertex = cms.bool(False),
            Z_fixed = cms.bool(False),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
            maxRegions = cms.int32(2),
            precise = cms.bool(True),
            vertexCollection = cms.InputTag("pixelVertices")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltIterL3OIMuonTrackSelectionHighPurity"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(9999.0),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("Notused")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring(
            'hltESPSmartPropagatorAny',
            'SteppingHelixPropagatorAny',
            'hltESPSmartPropagator',
            'hltESPSteppingHelixPropagatorOpposite'
        ),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltLightPFTracks = cms.EDProducer("LightPFTrackProducer",
    TkColList = cms.VInputTag("hltPFMuonMerging"),
    TrackQuality = cms.string('none'),
    UseQuality = cms.bool(False)
)


process.hltMergedTracks = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks")
)


process.hltMuonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    B904Setup = cms.untracked.bool(False),
    B904dmb = cms.untracked.int32(3),
    B904vmecrate = cms.untracked.int32(1),
    Debug = cms.untracked.bool(False),
    DisableMappingCheck = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535558134),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False),
    useCSCShowers = cms.bool(False),
    useGEMs = cms.bool(False),
    useRPCs = cms.bool(False)
)


process.hltMuonDTDigis = cms.EDProducer("DTuROSRawToDigi",
    debug = cms.untracked.bool(False),
    inputLabel = cms.InputTag("rawDataCollector")
)


process.hltMuonGEMDigis = cms.EDProducer("GEMRawToDigiModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    fedIdEnd = cms.uint32(1478),
    fedIdStart = cms.uint32(1467),
    ge21Off = cms.bool(True),
    keepDAQStatus = cms.bool(True),
    readMultiBX = cms.bool(False),
    useDBEMap = cms.bool(True)
)


process.hltMuonLinks = cms.EDProducer("MuonLinksProducerForHLT",
    InclusiveTrackerTrackCollection = cms.InputTag("hltPFMuonMerging"),
    LinkCollection = cms.InputTag("hltL3MuonsIterL3Links"),
    pMin = cms.double(2.5),
    ptMin = cms.double(2.5),
    shareHitFraction = cms.double(0.8)
)


process.hltMuonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(False)
)


process.hltMuons = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal',
            'hcal',
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForAll"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("hltAK4CaloJetsPFEt5"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForAll"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            CSCsegments = cms.InputTag("hltCscSegments"),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(100.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(2.7),
            DTsegments = cms.InputTag("hltDt4DSegments"),
            DoWireCorr = cms.bool(False),
            DropTheta = cms.bool(True),
            HitError = cms.double(6.0),
            HitsMin = cms.int32(5),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(10000.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorCSC = cms.double(7.4),
        ErrorDT = cms.double(6.0),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForAll"),
        DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
        HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("hltOnlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("hltPFMuonMerging")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(False)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(False),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(True),
    fillEnergy = cms.bool(True),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(False),
    fillIsolation = cms.bool(True),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(False),
    fillTrackerKink = cms.bool(False),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("hltPFMuonMerging", "hltMuonLinks", "hltL2Muons"),
    inputCollectionTypes = cms.vstring(
        'inner tracks',
        'links',
        'outer tracks'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(10.0),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(10.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    pvInputTag = cms.InputTag("offlinePrimaryVertices"),
    runArbitrationCleaner = cms.bool(False),
    selectHighPurity = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(False),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(False)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    beamMode = cms.untracked.uint32(11),
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    src = cms.InputTag("hltScalersRawToDigi"),
    useTransientRecord = cms.bool(True)
)


process.hltOnlineBeamSpotToGPU = cms.EDProducer("BeamSpotToCUDA",
    src = cms.InputTag("hltOnlineBeamSpot")
)


process.hltOnlineMetaDataDigis = cms.EDProducer("OnlineMetaDataRawToDigi",
    onlineMetaDataInputLabel = cms.InputTag("rawDataCollector")
)


process.hltPFHTForMC = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK4PFJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40.0),
    minPtJetMht = cms.double(20.0),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    usePt = cms.bool(True)
)


process.hltPFMETProducer = cms.EDProducer("PFMETProducer",
    alias = cms.string('hltPFMet'),
    applyWeight = cms.bool(False),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.0),
    parameters = cms.PSet(

    ),
    src = cms.InputTag("hltParticleFlow"),
    srcWeights = cms.InputTag("")
)


process.hltPFMuonMerging = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIterL3MuonTracks", "hltMergedTracks"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIterL3MuonTracks", "hltMergedTracks"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltPSetMap = cms.EDProducer("ParameterSetBlobProducer")


process.hltParticleFlow = cms.EDProducer("PFProducer",
    GedElectronValueMap = cms.InputTag("gedGsfElectronsTmp"),
    GedPhotonValueMap = cms.InputTag("tmpGedPhotons","valMapPFEgammaCandToPhoton"),
    PFEGammaCandidates = cms.InputTag("particleFlowEGamma"),
    PFEGammaFiltersParameters = cms.PSet(
        electron_ecalDrivenHademPreselCut = cms.double(0.15),
        electron_iso_combIso_barrel = cms.double(10.0),
        electron_iso_combIso_endcap = cms.double(10.0),
        electron_iso_mva_barrel = cms.double(-0.1875),
        electron_iso_mva_endcap = cms.double(-0.1075),
        electron_iso_pt = cms.double(10.0),
        electron_maxElePtForOnlyMVAPresel = cms.double(50.0),
        electron_missinghits = cms.uint32(1),
        electron_noniso_mvaCut = cms.double(-0.1),
        electron_protectionsForBadHcal = cms.PSet(
            dEta = cms.vdouble(0.0064, 0.01264),
            dPhi = cms.vdouble(0.0547, 0.0394),
            eInvPInv = cms.vdouble(0.184, 0.0721),
            enableProtections = cms.bool(False),
            full5x5_sigmaIetaIeta = cms.vdouble(0.0106, 0.0387)
        ),
        electron_protectionsForJetMET = cms.PSet(
            maxDPhiIN = cms.double(0.1),
            maxE = cms.double(50.0),
            maxEcalEOverPRes = cms.double(0.2),
            maxEcalEOverP_1 = cms.double(0.5),
            maxEcalEOverP_2 = cms.double(0.2),
            maxEeleOverPout = cms.double(0.2),
            maxEeleOverPoutRes = cms.double(0.5),
            maxEleHcalEOverEcalE = cms.double(0.1),
            maxHcalE = cms.double(10.0),
            maxHcalEOverEcalE = cms.double(0.1),
            maxHcalEOverP = cms.double(1.0),
            maxNtracks = cms.double(3.0),
            maxTrackPOverEele = cms.double(1.0)
        ),
        photon_HoE = cms.double(0.05),
        photon_MinEt = cms.double(10.0),
        photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
        photon_SigmaiEtaiEta_endcap = cms.double(0.034),
        photon_combIso = cms.double(10.0),
        photon_protectionsForBadHcal = cms.PSet(
            enableProtections = cms.bool(False),
            solidConeTrkIsoOffset = cms.double(10.0),
            solidConeTrkIsoSlope = cms.double(0.3)
        ),
        photon_protectionsForJetMET = cms.PSet(
            sumPtTrackIso = cms.double(4.0),
            sumPtTrackIsoSlope = cms.double(0.001)
        )
    ),
    PFHFCleaningParameters = cms.PSet(
        maxDeltaPhiPt = cms.double(7.0),
        maxSignificance = cms.double(2.5),
        minDeltaMet = cms.double(0.4),
        minHFCleaningPt = cms.double(5.0),
        minSignificance = cms.double(2.5),
        minSignificanceReduction = cms.double(1.4)
    ),
    PFMuonAlgoParameters = cms.PSet(

    ),
    blocks = cms.InputTag("hltParticleFlowBlock"),
    calibHF_a_EMHAD = cms.vdouble(
        1.42215, 1.00496, 0.68961, 0.81656, 0.98504,
        0.98504, 1.00802, 1.0593, 1.4576, 1.4576
    ),
    calibHF_a_EMonly = cms.vdouble(
        0.96945, 0.96701, 0.76309, 0.82268, 0.87583,
        0.89718, 0.98674, 1.4681, 1.458, 1.458
    ),
    calibHF_b_EMHAD = cms.vdouble(
        1.27541, 0.85361, 0.86333, 0.89091, 0.94348,
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444
    ),
    calibHF_b_HADonly = cms.vdouble(
        1.27541, 0.85361, 0.86333, 0.89091, 0.94348,
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444
    ),
    calibHF_eta_step = cms.vdouble(
        0.0, 2.9, 3.0, 3.2, 4.2,
        4.4, 4.6, 4.8, 5.2, 5.4
    ),
    calibHF_use = cms.bool(False),
    calibrationsLabel = cms.string('HLT'),
    cleanedHF = cms.VInputTag("hltParticleFlowRecHitHF:Cleaned", "hltParticleFlowClusterHF:Cleaned"),
    debug = cms.untracked.bool(False),
    dptRel_DispVtx = cms.double(10.0),
    egammaElectrons = cms.InputTag(""),
    factors_45 = cms.vdouble(10.0, 100.0),
    goodPixelTrackDeadHcal_chi2n = cms.double(2.0),
    goodPixelTrackDeadHcal_dxy = cms.double(0.02),
    goodPixelTrackDeadHcal_dz = cms.double(0.05),
    goodPixelTrackDeadHcal_maxLost3Hit = cms.int32(0),
    goodPixelTrackDeadHcal_maxLost4Hit = cms.int32(1),
    goodPixelTrackDeadHcal_maxPt = cms.double(50.0),
    goodPixelTrackDeadHcal_minEta = cms.double(2.3),
    goodPixelTrackDeadHcal_ptErrRel = cms.double(1.0),
    goodTrackDeadHcal_chi2n = cms.double(5.0),
    goodTrackDeadHcal_dxy = cms.double(0.5),
    goodTrackDeadHcal_layers = cms.uint32(4),
    goodTrackDeadHcal_ptErrRel = cms.double(0.2),
    goodTrackDeadHcal_validFr = cms.double(0.5),
    iCfgCandConnector = cms.PSet(
        bCalibPrimary = cms.bool(False),
        bCorrect = cms.bool(False),
        nuclCalibFactors = cms.vdouble(0.8, 0.15, 0.5, 0.5, 0.05)
    ),
    muon_ECAL = cms.vdouble(0.5, 0.5),
    muon_HCAL = cms.vdouble(3.0, 3.0),
    muon_HO = cms.vdouble(0.9, 0.9),
    muons = cms.InputTag("hltMuons"),
    nsigma_TRACK = cms.double(1.0),
    pf_nsigma_ECAL = cms.double(0.0),
    pf_nsigma_HCAL = cms.double(1.0),
    pf_nsigma_HFEM = cms.double(1.0),
    pf_nsigma_HFHAD = cms.double(1.0),
    postHFCleaning = cms.bool(False),
    postMuonCleaning = cms.bool(True),
    pt_Error = cms.double(1.0),
    rejectTracks_Bad = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    resolHF_square = cms.vdouble(7.834401, 0.012996, 0.0),
    useCalibrationsFromDB = cms.bool(True),
    useEGammaElectrons = cms.bool(False),
    useEGammaFilters = cms.bool(False),
    useHO = cms.bool(False),
    usePFConversions = cms.bool(False),
    usePFDecays = cms.bool(False),
    usePFNuclearInteractions = cms.bool(False),
    useProtectionsForJetMET = cms.bool(True),
    useVerticesForNeutral = cms.bool(True),
    verbose = cms.untracked.bool(False),
    vertexCollection = cms.InputTag("hltPixelVertices"),
    vetoEndcap = cms.bool(False)
)


process.hltParticleFlowBlock = cms.EDProducer("PFBlockProducer",
    debug = cms.untracked.bool(False),
    elementImporters = cms.VPSet(
        cms.PSet(
            DPtOverPtCuts_byTrackAlgo = cms.vdouble(
                0.5, 0.5, 0.5, 0.5, 0.5,
                0.5
            ),
            NHitCuts_byTrackAlgo = cms.vuint32(
                3, 3, 3, 3, 3,
                3
            ),
            cleanBadConvertedBrems = cms.bool(False),
            importerName = cms.string('GeneralTracksImporter'),
            muonMaxDPtOPt = cms.double(1.0),
            muonSrc = cms.InputTag("hltMuons"),
            source = cms.InputTag("hltLightPFTracks"),
            trackQuality = cms.string('highPurity'),
            useIterativeTracking = cms.bool(False),
            vetoEndcap = cms.bool(False)
        ),
        cms.PSet(
            BCtoPFCMap = cms.InputTag(""),
            importerName = cms.string('ECALClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterECALUnseeded")
        ),
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHCAL")
        ),
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHF")
        )
    ),
    linkDefinitions = cms.VPSet(
        cms.PSet(
            linkType = cms.string('TRACK:ECAL'),
            linkerName = cms.string('TrackAndECALLinker'),
            useKDTree = cms.bool(True)
        ),
        cms.PSet(
            linkType = cms.string('TRACK:HCAL'),
            linkerName = cms.string('TrackAndHCALLinker'),
            nMaxHcalLinksPerTrack = cms.int32(1),
            trajectoryLayerEntrance = cms.string('HCALEntrance'),
            trajectoryLayerExit = cms.string('HCALExit'),
            useKDTree = cms.bool(True)
        ),
        cms.PSet(
            linkType = cms.string('ECAL:HCAL'),
            linkerName = cms.string('ECALAndHCALLinker'),
            minAbsEtaEcal = cms.double(2.5),
            useKDTree = cms.bool(False)
        ),
        cms.PSet(
            linkType = cms.string('HFEM:HFHAD'),
            linkerName = cms.string('HFEMAndHFHADLinker'),
            useKDTree = cms.bool(False)
        )
    ),
    verbose = cms.untracked.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALUnseeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowClusterECALUnseeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        ebSrFlagLabel = cms.InputTag("hltEcalDigis"),
        eeSrFlagLabel = cms.InputTag("hltEcalDigis"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedUnseeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
    minimumPSEnergy = cms.double(0.0),
    skipPS = cms.bool(False)
)


process.hltParticleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                gatheringThreshold = cms.vdouble(0.4, 0.3, 0.3, 0.3),
                gatheringThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                ),
                gatheringThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(5),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.4, 0.3, 0.3, 0.3)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHBHE"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                seedingThreshold = cms.vdouble(0.6, 0.5, 0.5, 0.5),
                seedingThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275,
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        )
    )
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("hltParticleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    )
)


process.hltParticleFlowClusterHF = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DClusterForEachSeed'),
        thresholdsByDetector = cms.VPSet()
    ),
    pfClusterBuilder = cms.PSet(

    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHF"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(0),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HF_EM'),
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('HF_HAD'),
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowClusterPSUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSUnseeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        )
    )
)


process.hltParticleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        hcalEnums = cms.vint32(1, 2),
        name = cms.string('PFRecHitHCALDenseIdNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                cuts = cms.VPSet(
                    cms.PSet(
                        depth = cms.vint32(1, 2, 3, 4),
                        detectorEnum = cms.int32(1),
                        threshold = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                    ),
                    cms.PSet(
                        depth = cms.vint32(
                            1, 2, 3, 4, 5,
                            6, 7
                        ),
                        detectorEnum = cms.int32(2),
                        threshold = cms.vdouble(
                            0.1, 0.2, 0.2, 0.2, 0.2,
                            0.2, 0.2
                        )
                    )
                ),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            ),
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )
        ),
        src = cms.InputTag("hltHbhereco")
    ))
)


process.hltParticleFlowRecHitHF = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        hcalEnums = cms.vint32(4),
        name = cms.string('PFRecHitHCALDenseIdNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        EMDepthCorrection = cms.double(22.0),
        HADDepthCorrection = cms.double(25.0),
        HFCalib29 = cms.double(1.07),
        LongFibre_Cut = cms.double(120.0),
        LongFibre_Fraction = cms.double(0.1),
        ShortFibre_Cut = cms.double(60.0),
        ShortFibre_Fraction = cms.double(0.01),
        name = cms.string('PFHFRecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0, 120.0, 60.0),
                flags = cms.vstring(
                    'Standard',
                    'HFLong',
                    'HFShort'
                ),
                maxSeverities = cms.vint32(11, 9, 9),
                name = cms.string('PFRecHitQTestHCALChannel')
            ),
            cms.PSet(
                cuts = cms.VPSet(cms.PSet(
                    depth = cms.vint32(1, 2),
                    detectorEnum = cms.int32(4),
                    threshold = cms.vdouble(1.2, 1.8)
                )),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            )
        ),
        src = cms.InputTag("hltHfreco"),
        thresh_HF = cms.double(0.4)
    ))
)


process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltEcalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducerFromSoAPhase1",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('loose'),
    pixelRecHitLegacySrc = cms.InputTag("hltSiPixelRecHits"),
    trackSrc = cms.InputTag("hltPixelTracksSoA")
)


process.hltPixelTracksCPU = cms.EDProducer("CAHitNtupletCUDAPhase1",
    CAThetaCutBarrel = cms.double(0.00200000009499),
    CAThetaCutForward = cms.double(0.00300000002608),
    dcaCutInnerTriplet = cms.double(0.15000000596),
    dcaCutOuterTriplet = cms.double(0.25),
    doClusterCut = cms.bool(True),
    doPtCut = cms.bool(True),
    doSharedHitCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    earlyFishbone = cms.bool(True),
    fillStatistics = cms.bool(False),
    fitNas4 = cms.bool(False),
    hardCurvCut = cms.double(0.0328407224959),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(True),
    lateFishbone = cms.bool(False),
    maxNumberOfDoublets = cms.uint32(524288),
    minHitsForSharingCut = cms.uint32(10),
    minHitsPerNtuplet = cms.uint32(3),
    onGPU = cms.bool(False),
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsFromLegacy"),
    ptmin = cms.double(0.899999976158),
    trackQualityCuts = cms.PSet(
        chi2Coeff = cms.vdouble(0.9, 1.8),
        chi2MaxPt = cms.double(10.0),
        chi2Scale = cms.double(8.0),
        quadrupletMaxTip = cms.double(0.5),
        quadrupletMaxZip = cms.double(12.0),
        quadrupletMinPt = cms.double(0.3),
        tripletMaxTip = cms.double(0.3),
        tripletMaxZip = cms.double(12.0),
        tripletMinPt = cms.double(0.5)
    ),
    useRiemannFit = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True)
)


process.hltPixelTracksFilter = cms.EDProducer("PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double(1000.0),
    nSigmaInvPtTolerance = cms.double(0.0),
    nSigmaTipMaxTolerance = cms.double(0.0),
    ptMin = cms.double(0.1),
    tipMax = cms.double(1.0)
)


process.hltPixelTracksFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)


process.hltPixelTracksFromGPU = cms.EDProducer("PixelTrackSoAFromCUDAPhase1",
    src = cms.InputTag("hltPixelTracksGPU")
)


process.hltPixelTracksGPU = cms.EDProducer("CAHitNtupletCUDAPhase1",
    CAThetaCutBarrel = cms.double(0.00200000009499),
    CAThetaCutForward = cms.double(0.00300000002608),
    dcaCutInnerTriplet = cms.double(0.15000000596),
    dcaCutOuterTriplet = cms.double(0.25),
    doClusterCut = cms.bool(True),
    doPtCut = cms.bool(True),
    doSharedHitCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    earlyFishbone = cms.bool(True),
    fillStatistics = cms.bool(False),
    fitNas4 = cms.bool(False),
    hardCurvCut = cms.double(0.0328407224959),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(True),
    lateFishbone = cms.bool(False),
    maxNumberOfDoublets = cms.uint32(524288),
    minHitsForSharingCut = cms.uint32(10),
    minHitsPerNtuplet = cms.uint32(3),
    onGPU = cms.bool(True),
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsGPU"),
    ptmin = cms.double(0.899999976158),
    trackQualityCuts = cms.PSet(
        chi2Coeff = cms.vdouble(0.9, 1.8),
        chi2MaxPt = cms.double(10.0),
        chi2Scale = cms.double(8.0),
        quadrupletMaxTip = cms.double(0.5),
        quadrupletMaxZip = cms.double(12.0),
        quadrupletMinPt = cms.double(0.3),
        tripletMaxTip = cms.double(0.3),
        tripletMaxZip = cms.double(12.0),
        tripletMinPt = cms.double(0.5)
    ),
    useRiemannFit = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True)
)


process.hltPixelTracksInRegionL1 = cms.EDProducer("TrackSelectorByRegion",
    produceMask = cms.bool(False),
    produceTrackCollection = cms.bool(True),
    regions = cms.InputTag("hltIterL3FromL1MuonPixelTracksTrackingRegions"),
    tracks = cms.InputTag("hltPixelTracks")
)


process.hltPixelTracksInRegionL2 = cms.EDProducer("TrackSelectorByRegion",
    produceMask = cms.bool(False),
    produceTrackCollection = cms.bool(True),
    regions = cms.InputTag("hltIterL3MuonPixelTracksTrackingRegions"),
    tracks = cms.InputTag("hltPixelTracks")
)


process.hltPixelTracksTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        nSigmaZ = cms.double(4.0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.8)
    )
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducerFromSoA",
    TrackCollection = cms.InputTag("hltPixelTracks"),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    src = cms.InputTag("hltPixelVerticesSoA")
)


process.hltPixelVerticesCPU = cms.EDProducer("PixelVertexProducerCUDAPhase1",
    PtMax = cms.double(75.0),
    PtMin = cms.double(0.5),
    chi2max = cms.double(9.0),
    eps = cms.double(0.07),
    errmax = cms.double(0.01),
    minT = cms.int32(2),
    onGPU = cms.bool(False),
    oneKernel = cms.bool(True),
    pixelTrackSrc = cms.InputTag("hltPixelTracksSoA"),
    useDBSCAN = cms.bool(False),
    useDensity = cms.bool(True),
    useIterative = cms.bool(False)
)


process.hltPixelVerticesFromGPU = cms.EDProducer("PixelVertexSoAFromCUDA",
    src = cms.InputTag("hltPixelVerticesGPU")
)


process.hltPixelVerticesGPU = cms.EDProducer("PixelVertexProducerCUDAPhase1",
    PtMax = cms.double(75.0),
    PtMin = cms.double(0.5),
    chi2max = cms.double(9.0),
    eps = cms.double(0.07),
    errmax = cms.double(0.01),
    minT = cms.int32(2),
    onGPU = cms.bool(True),
    oneKernel = cms.bool(True),
    pixelTrackSrc = cms.InputTag("hltPixelTracksGPU"),
    useDBSCAN = cms.bool(False),
    useDensity = cms.bool(True),
    useIterative = cms.bool(False)
)


process.hltRpcRecHits = cms.EDProducer("RPCRecHitProducer",
    deadSource = cms.string('File'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    maskSource = cms.string('File'),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    ),
    rpcDigiLabel = cms.InputTag("hltMuonRPCDigis")
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltSiPixelClustersCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelClustersFromSoA = cms.EDProducer("SiPixelDigisClustersFromSoAPhase1",
    clusterThreshold_layer1 = cms.int32(4000),
    clusterThreshold_otherLayers = cms.int32(4000),
    produceDigis = cms.bool(False),
    src = cms.InputTag("hltSiPixelDigisSoA"),
    storeDigis = cms.bool(False)
)


process.hltSiPixelClustersGPU = cms.EDProducer("SiPixelRawToClusterCUDA",
    CablingMapLabel = cms.string(''),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    UseQualityInfo = cms.bool(False),
    clusterThreshold_layer1 = cms.int32(4000),
    clusterThreshold_otherLayers = cms.int32(4000),
    isRun2 = cms.bool(False)
)


process.hltSiPixelClustersLegacy = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(10),
    ClusterMode = cms.string('PixelThresholdClusterizer'),
    ClusterThreshold = cms.int32(4000),
    ClusterThreshold_L1 = cms.int32(4000),
    DropDuplicates = cms.bool(True),
    ElectronPerADCGain = cms.double(135.0),
    MissCalibrate = cms.bool(True),
    Phase2Calibration = cms.bool(False),
    Phase2DigiBaseline = cms.double(1200.0),
    Phase2KinkADC = cms.int32(8),
    Phase2ReadoutMode = cms.int32(-1),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(1),
    VCaltoElectronGain_L1 = cms.int32(1),
    VCaltoElectronOffset = cms.int32(0),
    VCaltoElectronOffset_L1 = cms.int32(0),
    maxNumberOfClusters = cms.int32(40000),
    payloadType = cms.string('HLT'),
    src = cms.InputTag("hltSiPixelDigisLegacy")
)


process.hltSiPixelDigiErrorsSoA = cms.EDProducer("SiPixelDigiErrorsSoAFromCUDA",
    src = cms.InputTag("hltSiPixelClustersGPU")
)


process.hltSiPixelDigisFromSoA = cms.EDProducer("SiPixelDigiErrorsFromSoA",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    UsePhase1 = cms.bool(True),
    UserErrorList = cms.vint32(40),
    digiErrorSoASrc = cms.InputTag("hltSiPixelDigiErrorsSoA")
)


process.hltSiPixelDigisLegacy = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    SiPixelQualityLabel = cms.string(''),
    UsePhase1 = cms.bool(True),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelDigisSoA = cms.EDProducer("SiPixelDigisSoAFromCUDA",
    src = cms.InputTag("hltSiPixelClustersGPU")
)


process.hltSiPixelRecHitsFromGPU = cms.EDProducer("SiPixelRecHitFromCUDAPhase1",
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsGPU"),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelRecHitsFromLegacy = cms.EDProducer("SiPixelRecHitSoAFromLegacyPhase1",
    CPE = cms.string('hltESPPixelCPEFast'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    convertToLegacy = cms.bool(True),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelRecHitsGPU = cms.EDProducer("SiPixelRecHitCUDAPhase1",
    CPE = cms.string('hltESPPixelCPEFast'),
    beamSpot = cms.InputTag("hltOnlineBeamSpotToGPU"),
    src = cms.InputTag("hltSiPixelClustersGPU")
)


process.hltSiPixelRecHitsSoAFromGPU = cms.EDProducer("SiPixelRecHitSoAFromCUDAPhase1",
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsGPU")
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("hltSiPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag("hltSiPixelDigis"),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility'),
    switchOffPixelsIfEmpty = cms.bool(True),
    vectorHits = cms.InputTag(""),
    vectorHitsRej = cms.InputTag("")
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        Use10bitsTruncation = cms.bool(False),
        doAPVRestore = cms.bool(False),
        useCMMeanMap = cms.bool(False)
    ),
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        ConditionsLabel = cms.string(''),
        MaxAdjacentBad = cms.uint32(0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        setDetId = cms.bool(True)
    ),
    DoAPVEmulatorCheck = cms.bool(False),
    HybridZeroSuppressed = cms.bool(False),
    ProductLabel = cms.InputTag("rawDataCollector"),
    onDemand = cms.bool(True)
)


process.hltTowerMakerForAll = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime',
        'kWeird',
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(),
    HBThreshold = cms.double(0.3),
    HBThreshold1 = cms.double(0.1),
    HBThreshold2 = cms.double(0.2),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HEDThreshold = cms.double(0.2),
    HEDThreshold1 = cms.double(0.1),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(),
    HESGrid = cms.vdouble(),
    HESThreshold = cms.double(0.2),
    HESThreshold1 = cms.double(0.1),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(),
    HF1Grid = cms.vdouble(),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(),
    HF2Grid = cms.vdouble(),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(),
    HOGrid = cms.vdouble(),
    HOThreshold0 = cms.double(3.5),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1e-99),
    HOWeights = cms.vdouble(),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(1),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(False),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    UseSymEETreshold = cms.bool(False),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    hbheInput = cms.InputTag("hltHbhereco"),
    hfInput = cms.InputTag("hltHfreco"),
    hoInput = cms.InputTag("hltHoreco"),
    missingHcalRescaleFactorForEcal = cms.double(0.0)
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@'),
    throw = cms.bool(False)
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices")
)


process.hltEcalDigis = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltEcalDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EEDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EBDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EEDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EBSrFlagsSorted')
            ),
            cms.PSet(
                type = cms.string('EESrFlagsSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityBlockSizeErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityTTIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityZSXtalIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EcalPnDiodeDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalPseudoStripInputs'),
                type = cms.string('EcalPseudoStripInputDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalTriggerPrimitives'),
                type = cms.string('EcalTriggerPrimitiveDigisSorted')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltEcalDigisFromGPU = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EEDigiCollection')
            )
        ),
        hltEcalDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EEDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EBSrFlagsSorted')
            ),
            cms.PSet(
                type = cms.string('EESrFlagsSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityBlockSizeErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityTTIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityZSXtalIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EcalPnDiodeDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalPseudoStripInputs'),
                type = cms.string('EcalPseudoStripInputDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalTriggerPrimitives'),
                type = cms.string('EcalTriggerPrimitiveDigisSorted')
            )
        )
    )
)


process.hltEcalUncalibRecHit = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltEcalUncalibRecHitLegacy = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltEcalUncalibRecHitFromSoA = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltHbhereco = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltHbherecoLegacy = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltHbherecoFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('HBHERecHitsSorted')
        ))
    )
)


process.hltPixelTracksSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltPixelTracksCPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltPixelTracksFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltPixelVerticesSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltPixelVerticesCPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltPixelVerticesFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelClusters = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelClustersLegacy = cms.VPSet(cms.PSet(
            type = cms.string('SiPixelClusteredmNewDetSetVector')
        ))
    ),
    cuda = cms.EDAlias(
        hltSiPixelClustersFromSoA = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelDigis = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('DetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('SiPixelRawDataErroredmDetSetVector')
            ),
            cms.PSet(
                type = cms.string('PixelFEDChanneledmNewDetSetVector')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelDigisFromSoA = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelRecHits = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelRecHitsFromLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('SiPixelRecHitedmNewDetSetVector')
            ),
            cms.PSet(
                type = cms.string('uintAsHostProduct')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelRecHitsFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelRecHitsSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelRecHitsFromLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('pixelTopologyPhase1TrackingRecHitSoAHost')
            ),
            cms.PSet(
                type = cms.string('uintAsHostProduct')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelRecHitsSoAFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.statusOnGPU = SwitchProducerCUDA(
    cpu = cms.EDProducer("BooleanProducer",
        value = cms.bool(False)
    ),
    cuda = cms.EDProducer("BooleanProducer",
        value = cms.bool(True)
    )
)


process.hltAK4CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(5.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsPF")
)


process.hltAK4PFJetCollection20Filter = cms.EDFilter("HLT1PFJet",
    MaxEta = cms.double(3.0),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltAK4PFJetsCorrected"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(85)
)


process.hltAK8CaloHTOpenFilter = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltAK8HtMhtForMC"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltAK8HtMhtForMC"),
    minHt = cms.vdouble(-1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltAK8CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(5.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK8CaloJetsPF")
)


process.hltAK8PFHTOpenFilter = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltAK8PFHTForMC"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltAK8PFHTForMC"),
    minHt = cms.vdouble(-1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltAK8PFJetCollection20Filter = cms.EDFilter("HLT1PFJet",
    MaxEta = cms.double(3.0),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltAK8PFJetsCorrected"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(85)
)


process.hltAK8TrimPFJetCollection20Filter = cms.EDFilter("HLT1PFJet",
    MaxEta = cms.double(3.0),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltAK8TrimModJets"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(85)
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltCaloHtMhtFromPVOpenFilter = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltHtMhtFromPVForMC"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltHtMhtFromPVForMC"),
    minHt = cms.vdouble(-1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltCaloJetCollection20Filter = cms.EDFilter("HLT1CaloJet",
    MaxEta = cms.double(-1.0),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltAK4CaloJetsCorrectedIDPassed"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(0)
)


process.hltCaloJetFromPVCollection20Filter = cms.EDFilter("HLT1CaloJet",
    MaxEta = cms.double(-1.0),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltCaloJetFromPV"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(0)
)


process.hltPFMETOpenFilter = cms.EDFilter("HLT1PFMET",
    MaxEta = cms.double(-1.0),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(-1.0),
    inputTag = cms.InputTag("hltPFMETProducer"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(87)
)


process.hltPFMHTOpenFilter = cms.EDFilter("HLTMhtFilter",
    mhtLabels = cms.VInputTag("hltPFHTForMC"),
    minMht = cms.vdouble(-1.0),
    saveTags = cms.bool(True)
)


process.hltPreMCAK4CaloJets = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCAK4CaloJetsFromPV = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCAK4PFJets = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCAK8CaloHT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCAK8PFHT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCAK8PFJets = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCAK8TrimPFJets = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCPFMET = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCPFMHT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltSelectorJets20L1FastJetForNoPU = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(20.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsCorrectedIDPassed")
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.statusOnGPUFilter = cms.EDFilter("BooleanFilter",
    src = cms.InputTag("statusOnGPU")
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string('DQMIO.root')
)


process.hltOutputFull = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('output.root'),
    outputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_hltSiPixelDigisLegacy_*_*',
        'drop *_hltSiPixelClustersLegacy_*_*',
        'drop *_hltSiPixelRecHitsFromLegacy_*_*',
        'drop *_hltEcalDigisLegacy_*_*',
        'drop *_hltEcalUncalibRecHitLegacy_*_*',
        'drop *_hltHbherecoLegacy_*_*'
    )
)


process.CUDAService = cms.Service("CUDAService",
    allocator = cms.untracked.PSet(
        devicePreallocate = cms.untracked.vuint32(),
        hostPreallocate = cms.untracked.vuint32()
    ),
    enabled = cms.untracked.bool(True),
    limits = cms.untracked.PSet(
        cudaLimitDevRuntimePendingLaunchCount = cms.untracked.int32(-1),
        cudaLimitDevRuntimeSyncDepth = cms.untracked.int32(-1),
        cudaLimitMallocHeapSize = cms.untracked.int32(-1),
        cudaLimitPrintfFifoSize = cms.untracked.int32(-1),
        cudaLimitStackSize = cms.untracked.int32(-1)
    ),
    verbose = cms.untracked.bool(False)
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring(
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'Tracking/TrackParameters/GeneralProperties/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/GeneralProperties/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/GeneralProperties/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertice/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices'
    ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmMemoryRange = cms.untracked.double(1000000.0),
    dqmMemoryResolution = cms.untracked.double(5000.0),
    dqmModuleMemoryRange = cms.untracked.double(100000.0),
    dqmModuleMemoryResolution = cms.untracked.double(500.0),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmPathMemoryRange = cms.untracked.double(1000000.0),
    dqmPathMemoryResolution = cms.untracked.double(5000.0),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmTimeRange = cms.untracked.double(2000.0),
    dqmTimeResolution = cms.untracked.double(5.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMTransitions = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyPath = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(True),
    jsonFileName = cms.untracked.string('resources.json'),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(True),
    writeJSONSummary = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    FastReport = cms.untracked.PSet(

    ),
    HLTrigReport = cms.untracked.PSet(

    ),
    L1GtTrigReport = cms.untracked.PSet(

    ),
    L1TGlobalSummary = cms.untracked.PSet(

    ),
    ThroughputService = cms.untracked.PSet(

    ),
    TriggerSummaryProducerAOD = cms.untracked.PSet(

    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enableStatistics = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        threshold = cms.untracked.string('INFO')
    ),
    debugModules = cms.untracked.vstring(),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring(
        'hltL3TkTracksFromL2IOHit',
        'hltL3TkTracksFromL2OIHit',
        'hltL3TkTracksFromL2OIState',
        'hltOnlineBeamSpot'
    ),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(
        'hltL3MuonsIOHit',
        'hltL3MuonsOIHit',
        'hltL3MuonsOIState',
        'hltLightPFTracks',
        'hltOnlineBeamSpot',
        'hltPixelTracks',
        'hltPixelTracksForHighMult',
        'hltSiPixelClusters',
        'hltSiPixelDigis'
    )
)


process.ThroughputService = cms.Service("ThroughputService",
    dqmPath = cms.untracked.string('HLT/Throughput'),
    dqmPathByProcesses = cms.untracked.bool(True),
    enableDQM = cms.untracked.bool(True),
    eventRange = cms.untracked.uint32(10000),
    eventResolution = cms.untracked.uint32(1),
    printEventSummary = cms.untracked.bool(False),
    timeRange = cms.untracked.double(60000.0),
    timeResolution = cms.untracked.double(5.828)
)


process.ProcessAcceleratorCUDA = ProcessAcceleratorCUDA()


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CSCObjectMapESProducer = cms.ESProducer("CSCObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.DTObjectMapESProducer = cms.ESProducer("DTObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    appendToDataLabel = cms.string(''),
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlobalParameters = cms.ESProducer("StableParametersTrivialProducer",
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberChips = cms.uint32(1),
    NumberConditionChips = cms.uint32(1),
    NumberL1CenJet = cms.uint32(4),
    NumberL1EGamma = cms.uint32(12),
    NumberL1ForJet = cms.uint32(4),
    NumberL1IsoEG = cms.uint32(4),
    NumberL1Jet = cms.uint32(12),
    NumberL1JetCounts = cms.uint32(12),
    NumberL1Mu = cms.uint32(4),
    NumberL1Muon = cms.uint32(8),
    NumberL1NoIsoEG = cms.uint32(4),
    NumberL1Tau = cms.uint32(12),
    NumberL1TauJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(512),
    NumberPhysTriggersExtended = cms.uint32(64),
    NumberPsbBoards = cms.int32(7),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(1),
    OrderOfChip = cms.vint32(1),
    PinsOnChip = cms.uint32(512),
    PinsOnConditionChip = cms.uint32(512),
    TotalBxInEvent = cms.int32(5),
    UnitLength = cms.int32(8),
    WordLength = cms.int32(64),
    appendToDataLabel = cms.string('')
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStep'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripClusterizerConditionsESProducer = cms.ESProducer("SiStripClusterizerConditionsESProducer",
    Label = cms.string(''),
    QualityLabel = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32(20),
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20)
)


process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    minVertices = cms.uint32(1),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
    appendToDataLabel = cms.string(''),
    buildMisalignedGeometry = cms.bool(False),
    compactViewTag = cms.string(''),
    dbTag = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromPreprocessedDB = cms.untracked.bool(True),
    isRun2 = cms.bool(False),
    verbosity = cms.untracked.uint32(1)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalElectronicsMappingGPUESProducer = cms.ESProducer("EcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalGainRatiosGPUESProducer = cms.ESProducer("EcalGainRatiosGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalIntercalibConstantsGPUESProducer = cms.ESProducer("EcalIntercalibConstantsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAPDPNRatiosGPUESProducer = cms.ESProducer("EcalLaserAPDPNRatiosGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAPDPNRatiosRefGPUESProducer = cms.ESProducer("EcalLaserAPDPNRatiosRefGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAlphasGPUESProducer = cms.ESProducer("EcalLaserAlphasGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLinearCorrectionsGPUESProducer = cms.ESProducer("EcalLinearCorrectionsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPedestalsGPUESProducer = cms.ESProducer("EcalPedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPulseCovariancesGPUESProducer = cms.ESProducer("EcalPulseCovariancesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPulseShapesGPUESProducer = cms.ESProducer("EcalPulseShapesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalRechitADCToGeVConstantGPUESProducer = cms.ESProducer("EcalRechitADCToGeVConstantGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalRechitChannelStatusGPUESProducer = cms.ESProducer("EcalRechitChannelStatusGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalSamplesCorrelationGPUESProducer = cms.ESProducer("EcalSamplesCorrelationGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated',
            'kDeadVFE',
            'kDeadFE',
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC',
            'kNoLaser',
            'kNoisy',
            'kNNoisy',
            'kNNNoisy',
            'kNNNNoisy',
            'kNNNNNoisy',
            'kFixedG6',
            'kFixedG1',
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware',
            'kDead',
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco',
            'kPoorCalib',
            'kNoisy',
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered',
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird',
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.ecalTimeBiasCorrectionsGPUESProducer = cms.ESProducer("EcalTimeBiasCorrectionsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalTimeCalibConstantsGPUESProducer = cms.ESProducer("EcalTimeCalibConstantsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalChannelPropertiesESProd = cms.ESProducer("HcalChannelPropertiesEP")


process.hcalChannelQualityGPUESProducer = cms.ESProducer("HcalChannelQualityGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalConvertedEffectivePedestalWidthsGPUESProducer = cms.ESProducer("HcalConvertedEffectivePedestalWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string('withTopoEff'),
    label1 = cms.string('withTopoEff'),
    label2 = cms.string(''),
    label3 = cms.string('')
)


process.hcalConvertedEffectivePedestalsGPUESProducer = cms.ESProducer("HcalConvertedEffectivePedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string('withTopoEff'),
    label1 = cms.string(''),
    label2 = cms.string('')
)


process.hcalConvertedPedestalWidthsGPUESProducer = cms.ESProducer("HcalConvertedPedestalWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string(''),
    label3 = cms.string('')
)


process.hcalConvertedPedestalsGPUESProducer = cms.ESProducer("HcalConvertedPedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string('')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalElectronicsMappingGPUESProducer = cms.ESProducer("HcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalGainWidthsGPUESProducer = cms.ESProducer("HcalGainWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalGainsGPUESProducer = cms.ESProducer("HcalGainsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalLUTCorrsGPUESProducer = cms.ESProducer("HcalLUTCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalQIECodersGPUESProducer = cms.ESProducer("HcalQIECodersGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalQIETypesGPUESProducer = cms.ESProducer("HcalQIETypesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask',
        'HcalCellOff',
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('TimingFromTDC')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity',
                'HBHEIsolatedNoise',
                'HBHEFlatNoise',
                'HBHESpikeNoise',
                'HBHETS4TS5Noise',
                'HBHENegativeNoise',
                'HBHEPulseFitBit',
                'HBHEOOTPU'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort',
                'HFS8S1Ratio',
                'HFPET',
                'HFSignalAsymmetry'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff',
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring()
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcalRecoParamsWithPulseShapesGPUESProducer = cms.ESProducer("HcalRecoParamsWithPulseShapesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalRespCorrsGPUESProducer = cms.ESProducer("HcalRespCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalSiPMCharacteristicsGPUESProducer = cms.ESProducer("HcalSiPMCharacteristicsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalSiPMParametersGPUESProducer = cms.ESProducer("HcalSiPMParametersGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalTimeCorrsGPUESProducer = cms.ESProducer("HcalTimeCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertex',
        'CombinedSVPseudoVertex',
        'CombinedSVNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeLooseMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = cms.double(2000.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutForHI')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2MeasurementEstimator100 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = cms.double(40.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12)
)


process.hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerShortSig5 = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.05),
    maxImpactParameterSig = cms.double(5.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D1stLoose = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.03),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPKFFittingSmootherForLoopers'),
    standardFitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2MeasurementEstimator36'),
    MaxChi2 = cms.double(36.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherForLoopers'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPMixedStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMixedTripletStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPMixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEFast = cms.ESProducer("PixelCPEFastESProducerPhase1",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEFast'),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
    SmallPitch = cms.bool(False),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    isPhase2 = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(False),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    appendToDataLabel = cms.string(''),
    barrelTemplateID = cms.int32(0),
    directoryWithTemplates = cms.int32(0),
    doLorentzFromAlignment = cms.bool(False),
    forwardTemplateID = cms.int32(0),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    speed = cms.int32(-2),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True)
)


process.hltESPPixelLessStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPPixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPPixelPairStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2MeasurementEstimator25'),
    MaxChi2 = cms.double(25.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelPairTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPRKTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPTobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPTobTecStepFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmoother'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('hltESPTobTecStepFitterSmoother')
)


process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.hltESPTrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string(''),
    usePhase2Stacks = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltOnlineBeamSpotESProducer = cms.ESProducer("OnlineBeamSpotESProducer",
    appendToDataLabel = cms.string(''),
    sigmaZThreshold = cms.double(2.0),
    timeThreshold = cms.int32(1000000)
)


process.hltPixelTracksCleanerBySharedHits = cms.ESProducer("PixelTrackCleanerBySharedHitsESProducer",
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)


process.hltTrackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('hltTrackCleaner'),
    appendToDataLabel = cms.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(1.0),
    ValidHitBonus = cms.double(1000.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.1)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelGainCalibrationForHLTGPU = cms.ESProducer("SiPixelGainCalibrationForHLTGPUESProducer",
    appendToDataLabel = cms.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityLabel = cms.string(''),
    siPixelQualityLabel_RawToDigi = cms.string('')
)


process.siPixelROCsStatusAndMappingWrapperESProducer = cms.ESProducer("SiPixelROCsStatusAndMappingWrapperESProducer",
    CablingMapLabel = cms.string(''),
    ComponentName = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalParametersRcd')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(True),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(True),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('126X_mcRun3_2023_forPU65_v1'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('BeamSpotOnlineLegacyObjectsRcd'),
            refreshTime = cms.uint64(2)
        ),
        cms.PSet(
            record = cms.string('BeamSpotOnlineHLTObjectsRcd'),
            refreshTime = cms.uint64(2)
        )
    )
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.ecalMultifitParametersGPUESProducer = cms.ESSource("EcalMultifitParametersGPUESProducer",
    EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
    EBtimeFitParameters = cms.vdouble(
        -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
        91.01147, -50.35761, 11.05621
    ),
    EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
    EEtimeFitParameters = cms.vdouble(
        -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
        140.7432, -75.41106, 16.20277
    ),
    appendToDataLabel = cms.string(''),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    )
)


process.ecalRecHitParametersGPUESProducer = cms.ESSource("EcalRecHitParametersGPUESProducer",
    ChannelStatusToBeExcluded = cms.vstring(
        'kDAC',
        'kNoisy',
        'kNNoisy',
        'kFixedG6',
        'kFixedG1',
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE',
        'kDeadFE',
        'kNoDataNoTP'
    ),
    appendToDataLabel = cms.string(''),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hcalMahiPulseOffsetsGPUESProducer = cms.ESSource("HcalMahiPulseOffsetsGPUESProducer",
    appendToDataLabel = cms.string(''),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    )
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.ppsPixelTopologyESSource = cms.ESSource("PPSPixelTopologyESSource",
    PitchSimX = cms.double(0.1),
    PitchSimY = cms.double(0.15),
    RunType = cms.string('Run3'),
    activeEdgeSigma = cms.double(0.02),
    appendToDataLabel = cms.string(''),
    deadEdgeWidth = cms.double(0.2),
    noOfPixelSimX = cms.int32(160),
    noOfPixelSimY = cms.int32(104),
    noOfPixels = cms.int32(16640),
    physActiveEdgeDist = cms.double(0.15),
    simXWidth = cms.double(16.6),
    simYWidth = cms.double(16.2),
    thickness = cms.double(0.23)
)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask = cms.ConditionalTask(process.hltEcalDetIdToBeRecovered, process.hltEcalDigis, process.hltEcalDigisFromGPU, process.hltEcalDigisGPU, process.hltEcalDigisLegacy, process.hltEcalRecHit, process.hltEcalUncalibRecHit, process.hltEcalUncalibRecHitFromSoA, process.hltEcalUncalibRecHitGPU, process.hltEcalUncalibRecHitLegacy, process.hltEcalUncalibRecHitSoA)


process.HLTDoLocalHcalTask = cms.ConditionalTask(process.hltHbhereco, process.hltHbherecoFromGPU, process.hltHbherecoGPU, process.hltHbherecoLegacy, process.hltHcalDigis, process.hltHcalDigisGPU, process.hltHfprereco, process.hltHfreco, process.hltHoreco)


process.HLTDoLocalPixelTask = cms.ConditionalTask(process.hltOnlineBeamSpotToGPU, process.hltSiPixelClusters, process.hltSiPixelClustersCache, process.hltSiPixelClustersFromSoA, process.hltSiPixelClustersGPU, process.hltSiPixelClustersLegacy, process.hltSiPixelDigiErrorsSoA, process.hltSiPixelDigis, process.hltSiPixelDigisFromSoA, process.hltSiPixelDigisLegacy, process.hltSiPixelDigisSoA, process.hltSiPixelRecHits, process.hltSiPixelRecHitsFromGPU, process.hltSiPixelRecHitsFromLegacy, process.hltSiPixelRecHitsGPU, process.hltSiPixelRecHitsSoA, process.hltSiPixelRecHitsSoAFromGPU)


process.HLTRecoPixelTracksTask = cms.ConditionalTask(process.hltPixelTracks, process.hltPixelTracksCPU, process.hltPixelTracksFromGPU, process.hltPixelTracksGPU, process.hltPixelTracksSoA, process.hltPixelTracksTrackingRegions)


process.HLTRecopixelvertexingTask = cms.ConditionalTask(process.HLTRecoPixelTracksTask, process.hltPixelVertices, process.hltPixelVerticesCPU, process.hltPixelVerticesFromGPU, process.hltPixelVerticesGPU, process.hltPixelVerticesSoA, process.hltTrimmedPixelVertices)


process.HLTPreshowerTask = cms.ConditionalTask(process.hltEcalPreshowerDigis, process.hltEcalPreshowerRecHit)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineMetaDataDigis+process.hltOnlineBeamSpot)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask)


process.HLTDoLocalHcalSequence = cms.Sequence(process.HLTDoLocalHcalTask)


process.HLTDoCaloSequencePF = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForAll)


process.HLTAK4CaloJetsPrePFRecoSequence = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK4CaloJetsPF)


process.HLTPreAK4PFJetsRecoSequence = cms.Sequence(process.HLTAK4CaloJetsPrePFRecoSequence+process.hltAK4CaloJetsPFEt5)


process.HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits+process.hltMuonGEMDigis+process.hltGemRecHits+process.hltGemSegments)


process.HLTL2muonrecoNocandSequence = cms.Sequence(process.HLTMuonLocalRecoSequence+process.hltL2OfflineMuonSeeds+process.hltL2MuonSeeds+process.hltL2Muons)


process.HLTL2muonrecoSequence = cms.Sequence(process.HLTL2muonrecoNocandSequence+process.hltL2MuonCandidates)


process.HLTDoLocalPixelSequence = cms.Sequence(process.HLTDoLocalPixelTask)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTIterL3OImuonTkCandidateSequence = cms.Sequence(process.hltIterL3OISeedsFromL2Muons+process.hltIterL3OITrackCandidates+process.hltIterL3OIMuCtfWithMaterialTracks+process.hltIterL3OIMuonTrackCutClassifier+process.hltIterL3OIMuonTrackSelectionHighPurity+process.hltL3MuonsIterL3OI)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.hltPixelTracksFitter+process.hltPixelTracksFilter, process.HLTRecopixelvertexingTask)


process.HLTIterL3MuonRecopixelvertexingSequence = cms.Sequence(process.HLTRecopixelvertexingSequence+process.hltIterL3MuonPixelTracksTrackingRegions+process.hltPixelTracksInRegionL2)


process.HLTIterativeTrackingIteration0ForIterL3Muon = cms.Sequence(process.hltIter0IterL3MuonPixelSeedsFromPixelTracks+process.hltIter0IterL3MuonPixelSeedsFromPixelTracksFiltered+process.hltIter0IterL3MuonCkfTrackCandidates+process.hltIter0IterL3MuonCtfWithMaterialTracks+process.hltIter0IterL3MuonTrackCutClassifier+process.hltIter0IterL3MuonTrackSelectionHighPurity)


process.HLTIterL3IOmuonTkCandidateSequence = cms.Sequence(process.HLTIterL3MuonRecopixelvertexingSequence+process.HLTIterativeTrackingIteration0ForIterL3Muon+process.hltL3MuonsIterL3IO)


process.HLTIterL3OIAndIOFromL2muonTkCandidateSequence = cms.Sequence(process.HLTIterL3OImuonTkCandidateSequence+process.hltIterL3OIL3MuonsLinksCombination+process.hltIterL3OIL3Muons+process.hltIterL3OIL3MuonCandidates+process.hltL2SelectorForL3IO+process.HLTIterL3IOmuonTkCandidateSequence+process.hltIterL3MuonsFromL2LinksCombination)


process.HLTRecopixelvertexingSequenceForIterL3FromL1Muon = cms.Sequence(process.HLTRecopixelvertexingSequence+process.hltIterL3FromL1MuonPixelTracksTrackingRegions+process.hltPixelTracksInRegionL1)


process.HLTIterativeTrackingIteration0ForIterL3FromL1Muon = cms.Sequence(process.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks+process.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksFiltered+process.hltIter0IterL3FromL1MuonCkfTrackCandidates+process.hltIter0IterL3FromL1MuonCtfWithMaterialTracks+process.hltIter0IterL3FromL1MuonTrackCutClassifier+process.hltIter0IterL3FromL1MuonTrackSelectionHighPurity)


process.HLTIterL3IOmuonFromL1TkCandidateSequence = cms.Sequence(process.HLTRecopixelvertexingSequenceForIterL3FromL1Muon+process.HLTIterativeTrackingIteration0ForIterL3FromL1Muon)


process.HLTIterL3muonTkCandidateSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.HLTIterL3OIAndIOFromL2muonTkCandidateSequence+process.hltL1MuonsPt0+process.HLTIterL3IOmuonFromL1TkCandidateSequence)


process.HLTL3muonrecoNocandSequence = cms.Sequence(process.HLTIterL3muonTkCandidateSequence+process.hltIterL3MuonMerged+process.hltIterL3MuonAndMuonFromL1Merged+process.hltIterL3GlbMuon+process.hltIterL3MuonsNoID+process.hltIterL3Muons+process.hltL3MuonsIterL3Links+process.hltIterL3MuonTracks)


process.HLTL3muonrecoSequence = cms.Sequence(process.HLTL3muonrecoNocandSequence+process.hltIterL3MuonCandidates)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackCutClassifier+process.hltMergedTracks)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0)


process.HLTTrackReconstructionForPF = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02+process.hltPFMuonMerging+process.hltMuonLinks+process.hltMuons)


process.HLTPreshowerSequence = cms.Sequence(process.HLTPreshowerTask)


process.HLTParticleFlowSequence = cms.Sequence(process.HLTPreshowerSequence+process.hltParticleFlowRecHitECALUnseeded+process.hltParticleFlowRecHitHBHE+process.hltParticleFlowRecHitHF+process.hltParticleFlowRecHitPSUnseeded+process.hltParticleFlowClusterECALUncorrectedUnseeded+process.hltParticleFlowClusterPSUnseeded+process.hltParticleFlowClusterECALUnseeded+process.hltParticleFlowClusterHBHE+process.hltParticleFlowClusterHCAL+process.hltParticleFlowClusterHF+process.hltLightPFTracks+process.hltParticleFlowBlock+process.hltParticleFlow)


process.HLTAK4PFJetsReconstructionSequence = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK4PFJets+process.hltAK4PFJetsLooseID+process.hltAK4PFJetsTightID)


process.HLTAK4PFCorrectorProducersSequence = cms.Sequence(process.hltAK4PFFastJetCorrector+process.hltAK4PFRelativeCorrector+process.hltAK4PFAbsoluteCorrector+process.hltAK4PFResidualCorrector+process.hltAK4PFCorrector)


process.HLTAK4PFJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAll+process.HLTAK4PFCorrectorProducersSequence+process.hltAK4PFJetsCorrected+process.hltAK4PFJetsLooseIDCorrected+process.hltAK4PFJetsTightIDCorrected)


process.HLTAK4PFJetsSequence = cms.Sequence(process.HLTPreAK4PFJetsRecoSequence+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTDoCaloSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForAll)


process.HLTAK4CaloJetsReconstructionSequence = cms.Sequence(process.HLTDoCaloSequence+process.hltAK4CaloJets+process.hltAK4CaloJetsIDPassed)


process.HLTAK4CaloCorrectorProducersSequence = cms.Sequence(process.hltAK4CaloFastJetCorrector+process.hltAK4CaloRelativeCorrector+process.hltAK4CaloAbsoluteCorrector+process.hltAK4CaloResidualCorrector+process.hltAK4CaloCorrector)


process.HLTAK4CaloJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAllCalo+process.HLTAK4CaloCorrectorProducersSequence+process.hltAK4CaloJetsCorrected+process.hltAK4CaloJetsCorrectedIDPassed)


process.HLTAK4CaloJetsSequence = cms.Sequence(process.HLTAK4CaloJetsReconstructionSequence+process.HLTAK4CaloJetsCorrectionSequence)


process.HLTNoPUSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.hltSelectorJets20L1FastJetForNoPU+process.hltCaloJetFromPV)


process.HLTAK8CaloJetsPrePFRecoSequence = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK8CaloJetsPF+process.hltAK4CaloJetsPF)


process.HLTPreAK8PFJetsRecoSequence = cms.Sequence(process.HLTAK8CaloJetsPrePFRecoSequence+process.hltAK8CaloJetsPFEt5+process.hltAK4CaloJetsPFEt5)


process.HLTAK8PFJetsReconstructionSequence = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK8PFJets+process.hltAK8PFJetsLooseID+process.hltAK8PFJetsTightID)


process.HLTAK8PFCorrectorProducersSequence = cms.Sequence(process.hltAK8PFFastJetCorrector+process.hltAK8PFRelativeCorrector+process.hltAK8PFAbsoluteCorrector+process.hltAK8PFResidualCorrector+process.hltAK8PFCorrector)


process.HLTAK8PFJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAll+process.HLTAK8PFCorrectorProducersSequence+process.hltAK8PFJetsCorrected+process.hltAK8PFJetsLooseIDCorrected+process.hltAK8PFJetsTightIDCorrected)


process.HLTAK8PFJetsSequence = cms.Sequence(process.HLTPreAK8PFJetsRecoSequence+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence)


process.HLTAK8CaloJetsReconstructionSequence = cms.Sequence(process.HLTDoCaloSequence+process.hltAK8CaloJets+process.hltAK8CaloJetsIDPassed)


process.HLTAK8CaloCorrectorProducersSequence = cms.Sequence(process.hltAK8CaloFastJetCorrector+process.hltAK8CaloRelativeCorrector+process.hltAK8CaloAbsoluteCorrector+process.hltAK8CaloResidualCorrector+process.hltAK8CaloCorrector)


process.HLTAK8CaloJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAllCalo+process.HLTAK8CaloCorrectorProducersSequence+process.hltAK8CaloJetsCorrected+process.hltAK8CaloJetsCorrectedIDPassed)


process.HLTAK8CaloJetsSequence = cms.Sequence(process.HLTAK8CaloJetsReconstructionSequence+process.HLTAK8CaloJetsCorrectionSequence)


process.HLTriggerFirstPath = cms.Path(process.hltGetRaw+process.hltPSetMap+process.hltBoolFalse)


process.Status_OnCPU = cms.Path(process.statusOnGPU+~process.statusOnGPUFilter)


process.Status_OnGPU = cms.Path(process.statusOnGPU+process.statusOnGPUFilter)


process.MC_PFMET_v19 = cms.Path(process.HLTBeginSequence+process.hltPreMCPFMET+process.HLTAK4PFJetsSequence+process.hltPFMETProducer+process.hltPFMETOpenFilter+process.HLTEndSequence)


process.MC_AK4PFJets_v19 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK4PFJets+process.HLTAK4PFJetsSequence+process.hltAK4PFJetCollection20Filter+process.HLTEndSequence)


process.MC_PFMHT_v18 = cms.Path(process.HLTBeginSequence+process.hltPreMCPFMHT+process.HLTAK4PFJetsSequence+process.hltPFHTForMC+process.hltPFMHTOpenFilter+process.HLTEndSequence)


process.MC_AK4CaloJets_v11 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK4CaloJets+process.HLTAK4CaloJetsSequence+process.hltCaloJetCollection20Filter+process.HLTEndSequence)


process.MC_AK4CaloJetsFromPV_v10 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK4CaloJetsFromPV+process.HLTAK4CaloJetsSequence+process.HLTNoPUSequence+process.hltCaloJetFromPVCollection20Filter+process.hltHtMhtFromPVForMC+process.hltCaloHtMhtFromPVOpenFilter+process.HLTEndSequence)


process.MC_AK8PFJets_v19 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK8PFJets+process.HLTAK8PFJetsSequence+process.hltAK8PFJetCollection20Filter+process.HLTEndSequence)


process.MC_AK8TrimPFJets_v19 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK8TrimPFJets+process.HLTAK8PFJetsSequence+process.hltAK8TrimModJets+process.hltAK8TrimPFJetCollection20Filter+process.HLTEndSequence)


process.MC_AK8PFHT_v18 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK8PFHT+process.HLTAK8PFJetsSequence+process.hltAK8PFHTForMC+process.hltAK8PFHTOpenFilter+process.HLTEndSequence)


process.MC_AK8CaloHT_v10 = cms.Path(process.HLTBeginSequence+process.hltPreMCAK8CaloHT+process.HLTAK8CaloJetsSequence+process.hltAK8HtMhtForMC+process.hltAK8CaloHTOpenFilter+process.HLTEndSequence)


process.HLTriggerFinalPath = cms.Path(process.hltGtStage2Digis+process.hltScalersRawToDigi+process.hltFEDSelectorTCDS+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.FullOutput = cms.FinalPath(process.hltOutputFull)


process.DQMOutput = cms.FinalPath(process.dqmOutput)


process.schedule = cms.Schedule(*[ process.HLTriggerFirstPath, process.Status_OnCPU, process.Status_OnGPU, process.MC_PFMET_v19, process.MC_AK4PFJets_v19, process.MC_PFMHT_v18, process.MC_AK4CaloJets_v11, process.MC_AK4CaloJetsFromPV_v10, process.MC_AK8PFJets_v19, process.MC_AK8TrimPFJets_v19, process.MC_AK8PFHT_v18, process.MC_AK8CaloHT_v10, process.HLTriggerFinalPath, process.FullOutput, process.DQMOutput ])

