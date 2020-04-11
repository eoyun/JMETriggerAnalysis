import FWCore.ParameterSet.Config as cms

def customize_hltPhase2_TRKv06(process):

    ###
    ### Modules (taken from configuration developed by TRK POG)
    ###

    process.TrackProducer = cms.EDProducer('TrackProducer',
        AlgorithmName = cms.string('undefAlgorithm'),
        Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
        GeometricInnerState = cms.bool(False),
        MeasurementTracker = cms.string(''),
        MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        Propagator = cms.string('RungeKuttaTrackerPropagator'),
        SimpleMagneticField = cms.string(''),
        TTRHBuilder = cms.string('WithTrackAngle'),
        TrajectoryInEvent = cms.bool(False),
        alias = cms.untracked.string('ctfWithMaterialTracks'),
        beamSpot = cms.InputTag('offlineBeamSpot'),
        clusterRemovalInfo = cms.InputTag(''),
        src = cms.InputTag('ckfTrackCandidates'),
        useHitsSplitting = cms.bool(False),
        useSimpleMF = cms.bool(False)
    )

    process.MeasurementTracker = cms.ESProducer('MeasurementTrackerESProducer',
        ComponentName = cms.string(''),
        DebugPixelModuleQualityDB = cms.untracked.bool(False),
        DebugPixelROCQualityDB = cms.untracked.bool(False),
        DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
        DebugStripModuleQualityDB = cms.untracked.bool(False),
        DebugStripStripQualityDB = cms.untracked.bool(False),
        HitMatcher = cms.string('StandardMatcher'),
        MaskBadAPVFibers = cms.bool(True),
        Phase2StripCPE = cms.string('Phase2StripCPE'),
        PixelCPE = cms.string('PixelCPEGeneric'),
        SiStripQualityLabel = cms.string(''),
        StripCPE = cms.string('StripCPEfromTrackAngle'),
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

    process.PixelCPEGenericESProducer = cms.ESProducer('PixelCPEGenericESProducer',
        Alpha2Order = cms.bool(True),
        ClusterProbComputationFlag = cms.int32(0),
        ComponentName = cms.string('PixelCPEGeneric'),
        DoCosmics = cms.bool(False),
        DoLorentz = cms.bool(False),
        EdgeClusterErrorX = cms.double(50),
        EdgeClusterErrorY = cms.double(85),
        IrradiationBiasCorrection = cms.bool(False),
        LoadTemplatesFromDB = cms.bool(False),
        MagneticFieldRecord = cms.ESInputTag('',''),
        SmallPitch = cms.bool(False),
        TruncatePixelCharge = cms.bool(False),
        Upgrade = cms.bool(True),
        UseErrorsFromTemplates = cms.bool(False),
        appendToDataLabel = cms.string(''),
        eff_charge_cut_highX = cms.double(1),
        eff_charge_cut_highY = cms.double(1),
        eff_charge_cut_lowX = cms.double(0),
        eff_charge_cut_lowY = cms.double(0),
        inflate_all_errors_no_trk_angle = cms.bool(False),
        inflate_errors = cms.bool(False),
        lAOffset = cms.double(0),
        lAWidthBPix = cms.double(0),
        lAWidthFPix = cms.double(0),
        size_cutX = cms.double(3),
        size_cutY = cms.double(3),
        useLAAlignmentOffsets = cms.bool(False),
        useLAWidthFromDB = cms.bool(True)
    )

    process.hltPhase2PixelTracksTrackingRegions = cms.EDProducer('GlobalTrackingRegionFromBeamSpotEDProducer',
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag('offlineBeamSpot'),
            nSigmaZ = cms.double(4.0),
            originRadius = cms.double(0.02),
            precise = cms.bool(True),
            ptMin = cms.double(0.9)
        )
    )

    process.hltPhase2PixelTracksSeedLayers = cms.EDProducer('SeedingLayersEDProducer',
        BPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        FPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        MTEC = cms.PSet(
    
        ),
        MTIB = cms.PSet(
    
        ),
        MTID = cms.PSet(
    
        ),
        MTOB = cms.PSet(
    
        ),
        TEC = cms.PSet(
    
        ),
        TIB = cms.PSet(
    
        ),
        TID = cms.PSet(
    
        ),
        TOB = cms.PSet(
    
        ),
        layerList = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
        )
    )
    
    process.hltPhase2PixelTracksHitDoublets = cms.EDProducer('HitPairEDProducer',
        clusterCheck = cms.InputTag(''),
        layerPairs = cms.vuint32(0, 1, 2),
        maxElement = cms.uint32(50000000),
        maxElementTotal = cms.uint32(50000000),
        produceIntermediateHitDoublets = cms.bool(True),
        produceSeedingHitSets = cms.bool(False),
        seedingLayers = cms.InputTag('hltPhase2PixelTracksSeedLayers'),
        trackingRegions = cms.InputTag('hltPhase2PixelTracksTrackingRegions'),
        trackingRegionsSeedingLayers = cms.InputTag('')
    )
    
    process.hltPhase2PixelTracksHitQuadruplets = cms.EDProducer('CAHitQuadrupletEDProducer',
        CAHardPtCut = cms.double(0.0),
        CAPhiCut = cms.double(0.2),
        CAThetaCut = cms.double(0.0012),
        SeedComparitorPSet = cms.PSet(
            ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
            clusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
            clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
        ),
        doublets = cms.InputTag('hltPhase2PixelTracksHitDoublets'),
        extraHitRPhitolerance = cms.double(0.032),
        fitFastCircle = cms.bool(True),
        fitFastCircleChi2Cut = cms.bool(True),
        maxChi2 = cms.PSet(
            enabled = cms.bool(True),
            pt1 = cms.double(0.7),
            pt2 = cms.double(2.0),
            value1 = cms.double(200.0),
            value2 = cms.double(50.0)
        ),
        mightGet = cms.untracked.vstring('IntermediateHitDoublets_hltPhase2PixelTracksHitDoublets__RECO'),
        useBendingCorrection = cms.bool(True)
    )
    
    process.hltPhase2PixelTrackFilterByKinematics = cms.EDProducer('PixelTrackFilterByKinematicsProducer',
        chi2 = cms.double(1000.0),
        nSigmaInvPtTolerance = cms.double(0.0),
        nSigmaTipMaxTolerance = cms.double(0.0),
        ptMin = cms.double(0.9),
        tipMax = cms.double(1.0)
    )
    
    process.hltPhase2PixelTrackCleanerBySharedHits = cms.ESProducer('PixelTrackCleanerBySharedHitsESProducer',
        ComponentName = cms.string('hltPhase2PixelTrackCleanerBySharedHits'),
        appendToDataLabel = cms.string(''),
        useQuadrupletAlgo = cms.bool(False)
    )
    
    process.hltPhase2PixelFitterByHelixProjections = cms.EDProducer('PixelFitterByHelixProjectionsProducer',
        scaleErrorsForBPix1 = cms.bool(False),
        scaleFactor = cms.double(0.65)
    )
    
    process.hltPhase2PixelTracks = cms.EDProducer('PixelTrackProducer',
        Cleaner = cms.string('hltPhase2PixelTrackCleanerBySharedHits'),
        Filter = cms.InputTag('hltPhase2PixelTrackFilterByKinematics'),
        Fitter = cms.InputTag('hltPhase2PixelFitterByHelixProjections'),
        SeedingHitSets = cms.InputTag('hltPhase2PixelTracksHitQuadruplets'),
        mightGet = cms.untracked.vstring(
            '', 
            'RegionsSeedingHitSets_hltPhase2PixelTracksHitQuadruplets__RECO'
        ),
        passLabel = cms.string('hltPhase2PixelTracks')
    )
    
    process.hltPhase2PSetPvClusterComparerForIT = cms.PSet(
        track_chi2_max = cms.double(20.0),
        track_prob_min = cms.double(-1.0),
        track_pt_max = cms.double(20.0),
        track_pt_min = cms.double(1.0)
    )
    process.hltPhase2PixelVertices = cms.EDProducer('PixelVertexProducer',
        Finder = cms.string('DivisiveVertexFinder'),
        Method2 = cms.bool(True),
        NTrkMin = cms.int32(2),
        PVcomparer = cms.PSet(
            refToPSet_ = cms.string('hltPhase2PSetPvClusterComparerForIT')
        ),
        PtMin = cms.double(1.0),
        TrackCollection = cms.InputTag('hltPhase2PixelTracks'),
        UseError = cms.bool(True),
        Verbosity = cms.int32(0),
        WtAverage = cms.bool(True),
        ZOffset = cms.double(5.0),
        ZSeparation = cms.double(0.05),
        beamSpot = cms.InputTag('offlineBeamSpot')
    )
    
    process.hltPhase2TrimmedPixelVertices = cms.EDProducer('PixelVertexCollectionTrimmer',
        PVcomparer = cms.PSet(
            refToPSet_ = cms.string('hltPhase2PSetPvClusterComparerForIT')
        ),
        fractionSumPt2 = cms.double(0.3),
        maxVtx = cms.uint32(100),
        minSumPt2 = cms.double(0.0),
        src = cms.InputTag('hltPhase2PixelVertices')
    )
    
    process.hltPhase2InitialStepSeeds = cms.EDProducer('SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer',
        MinOneOverPtError = cms.double(1),
        OriginTransverseErrorMultiplier = cms.double(1),
        SeedComparitorPSet = cms.PSet(
            ClusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
            ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
            ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
            FilterAtHelixStage = cms.bool(False),
            FilterPixelHits = cms.bool(True),
            FilterStripHits = cms.bool(False)
        ),
        SeedMomentumForBOFF = cms.double(5),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string(''),
        mightGet = cms.untracked.vstring(
            '', 
            'RegionsSeedingHitSets_hltPhase2PixelTracksHitQuadruplets__RECO'
        ),
        propagator = cms.string('PropagatorWithMaterial'),
        seedingHitSets = cms.InputTag('hltPhase2PixelTracksHitQuadruplets')
    )
    
    process.hltPhase2HighPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer('TrajectoryCleanerESProducer',
        ComponentName = cms.string('hltPhase2HighPtTripletStepTrajectoryCleanerBySharedHits'),
        ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
        MissingHitPenalty = cms.double(20.0),
        ValidHitBonus = cms.double(5.0),
        allowSharedFirstHit = cms.bool(True),
        fractionShared = cms.double(0.16)
    )
    
    process.hltPhase2HighPtTripletStepTrackingRegions = cms.EDProducer('GlobalTrackingRegionFromBeamSpotEDProducer',
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag('offlineBeamSpot'),
            nSigmaZ = cms.double(4),
            originHalfLength = cms.double(0),
            originRadius = cms.double(0.02),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        ),
        mightGet = cms.optional.untracked.vstring
    )

    process.hltPhase2InitialStepTrajectoryFilter = cms.PSet(
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        chargeSignificance = cms.double(-1.0),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        maxCCCLostHits = cms.int32(0),
        maxConsecLostHits = cms.int32(1),
        maxLostHits = cms.int32(1),
        maxLostHitsFraction = cms.double(999),
        maxNumberOfHits = cms.int32(100),
        minGoodStripCharge = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        minHitsMinPt = cms.int32(4),
        minNumberOfHitsForLoopers = cms.int32(13),
        minNumberOfHitsPerLoop = cms.int32(4),
        minPt = cms.double(0.9),
        minimumNumberOfHits = cms.int32(4),
        nSigmaMinPt = cms.double(5.0),
        pixelSeedExtension = cms.bool(False),
        seedExtension = cms.int32(0),
        seedPairPenalty = cms.int32(0),
        strictSeedExtension = cms.bool(False)
    )
    process.hltPhase2HighPtTripletStepTrajectoryFilterInOut = cms.PSet(
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        chargeSignificance = cms.double(-1.0),
        constantValueForLostHitsFractionFilter = cms.double(2.0),
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        maxCCCLostHits = cms.int32(9999),
        maxConsecLostHits = cms.int32(1),
        maxLostHits = cms.int32(999),
        maxLostHitsFraction = cms.double(0.1),
        maxNumberOfHits = cms.int32(100),
        minGoodStripCharge = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        minHitsMinPt = cms.int32(3),
        minNumberOfHitsForLoopers = cms.int32(13),
        minNumberOfHitsPerLoop = cms.int32(4),
        minPt = cms.double(0.9),
        minimumNumberOfHits = cms.int32(4),
        nSigmaMinPt = cms.double(5.0),
        pixelSeedExtension = cms.bool(False),
        seedExtension = cms.int32(1),
        seedPairPenalty = cms.int32(0),
        strictSeedExtension = cms.bool(False)
    )
    process.hltPhase2HighPtTripletStepTrajectoryFilterBase = cms.PSet(
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        chargeSignificance = cms.double(-1.0),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        maxCCCLostHits = cms.int32(0),
        maxConsecLostHits = cms.int32(1),
        maxLostHits = cms.int32(1),
        maxLostHitsFraction = cms.double(999.0),
        maxNumberOfHits = cms.int32(100),
        minGoodStripCharge = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        minHitsMinPt = cms.int32(3),
        minNumberOfHitsForLoopers = cms.int32(13),
        minNumberOfHitsPerLoop = cms.int32(4),
        minPt = cms.double(0.9),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        pixelSeedExtension = cms.bool(False),
        seedExtension = cms.int32(1),
        seedPairPenalty = cms.int32(0),
        strictSeedExtension = cms.bool(False)
    )
    process.hltPhase2InitialStepChi2Est = cms.ESProducer('Chi2ChargeMeasurementEstimatorESProducer',
        ComponentName = cms.string('hltPhase2InitialStepChi2Est'),
        MaxChi2 = cms.double(9.0),
        MaxDisplacement = cms.double(0.5),
        MaxSagitta = cms.double(2),
        MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
        MinimalTolerance = cms.double(0.5),
        appendToDataLabel = cms.string(''),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
        ),
        nSigma = cms.double(3.0),
        pTChargeCutThreshold = cms.double(15.0)
    )
    
    process.hltPhase2HighPtTripletStepChi2Est = cms.ESProducer('Chi2ChargeMeasurementEstimatorESProducer',
        ComponentName = cms.string('hltPhase2HighPtTripletStepChi2Est'),
        MaxChi2 = cms.double(16.0),
        MaxDisplacement = cms.double(0.5),
        MaxSagitta = cms.double(2),
        MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
        MinimalTolerance = cms.double(0.5),
        appendToDataLabel = cms.string(''),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
        ),
        nSigma = cms.double(3),
        pTChargeCutThreshold = cms.double(-1)
    )
    
    process.hltPhase2HighPtTripletStepTrajectoryFilter = cms.PSet(
        ComponentType = cms.string('CompositeTrajectoryFilter'),
        filters = cms.VPSet(
            cms.PSet(
                refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryFilterBase')
            ), 
            cms.PSet(
                refToPSet_ = cms.string('ClusterShapeTrajectoryFilter')
            )
        )
    )
    process.hltPhase2InitialStepTrajectoryBuilder = cms.PSet(
        ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
        MeasurementTrackerName = cms.string(''),
        TTRHBuilder = cms.string('WithTrackAngle'),
        alwaysUseInvalidHits = cms.bool(False),
        bestHitOnly = cms.bool(True),
        estimator = cms.string('hltPhase2InitialStepChi2Est'),
        foundHitBonus = cms.double(10.0),
        inOutTrajectoryFilter = cms.PSet(
            refToPSet_ = cms.string('hltPhase2InitialStepTrajectoryFilter')
        ),
        intermediateCleaning = cms.bool(True),
        keepOriginalIfRebuildFails = cms.bool(True),
        lockHits = cms.bool(True),
        lostHitPenalty = cms.double(30.0),
        maxCand = cms.int32(2),
        maxDPhiForLooperReconstruction = cms.double(2.0),
        maxPtForLooperReconstruction = cms.double(0.7),
        minNrOfHitsForRebuild = cms.int32(1),
        propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
        requireSeedHitsInRebuild = cms.bool(True),
        seedAs5DHit = cms.bool(False),
        trajectoryFilter = cms.PSet(
            refToPSet_ = cms.string('hltPhase2InitialStepTrajectoryFilter')
        ),
        updator = cms.string('KFUpdator'),
        useSameTrajFilter = cms.bool(True)
    )
    process.hltPhase2InitialStepTrackCandidates = cms.EDProducer('CkfTrackCandidateMaker',
        MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
        SimpleMagneticField = cms.string('ParabolicMf'),
        TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
        TrajectoryBuilderPSet = cms.PSet(
            refToPSet_ = cms.string('hltPhase2InitialStepTrajectoryBuilder')
        ),
        TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
        TransientInitialStateEstimatorParameters = cms.PSet(
            numberMeasurementsForFit = cms.int32(4),
            propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
            propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
        ),
        cleanTrajectoryAfterInOut = cms.bool(True),
        doSeedingRegionRebuilding = cms.bool(True),
        maxNSeeds = cms.uint32(100000),
        maxSeedsBeforeCleaning = cms.uint32(1000),
        numHitsForSeedCleaner = cms.int32(50),
        onlyPixelHitsForSeedCleaner = cms.bool(True),
        reverseTrajectories = cms.bool(False),
        src = cms.InputTag('hltPhase2InitialStepSeeds'),
        useHitsSplitting = cms.bool(False)
    )
    
    process.hltPhase2HighPtTripletStepTrajectoryBuilder = cms.PSet(
        ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
        MeasurementTrackerName = cms.string(''),
        TTRHBuilder = cms.string('WithTrackAngle'),
        alwaysUseInvalidHits = cms.bool(False),
        bestHitOnly = cms.bool(True),
        estimator = cms.string('hltPhase2HighPtTripletStepChi2Est'),
        foundHitBonus = cms.double(10.0),
        inOutTrajectoryFilter = cms.PSet(
            refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryFilterInOut')
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
            refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryFilter')
        ),
        updator = cms.string('KFUpdator'),
        useSameTrajFilter = cms.bool(False)
    )

    process.hltPhase2InitialStepTracks = cms.EDProducer('TrackProducer',
        AlgorithmName = cms.string('initialStep'),
        Fitter = cms.string('FlexibleKFFittingSmoother'),
        GeometricInnerState = cms.bool(False),
        MeasurementTracker = cms.string(''),
        MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        Propagator = cms.string('RungeKuttaTrackerPropagator'),
        SimpleMagneticField = cms.string(''),
        TTRHBuilder = cms.string('WithTrackAngle'),
        TrajectoryInEvent = cms.bool(False),
        alias = cms.untracked.string('ctfWithMaterialTracks'),
        beamSpot = cms.InputTag('offlineBeamSpot'),
        clusterRemovalInfo = cms.InputTag(''),
        src = cms.InputTag('hltPhase2InitialStepTrackCandidates'),
        useHitsSplitting = cms.bool(False),
        useSimpleMF = cms.bool(False)
    )
    
    process.hltPhase2InitialStepTrackRefsForJets = cms.EDProducer('ChargedRefCandidateProducer',
        particleType = cms.string('pi+'),
        src = cms.InputTag('hltPhase2InitialStepTracks')
    )
    
    process.hltPhase2InitialStepTrackCutClassifier = cms.EDProducer('TrackCutClassifier',
        beamspot = cms.InputTag('offlineBeamSpot'),
        ignoreVertices = cms.bool(False),
        mva = cms.PSet(
            dr_par = cms.PSet(
                d0err = cms.vdouble(0.003, 0.003, 0.003),
                d0err_par = cms.vdouble(0.001, 0.001, 0.001),
                dr_exp = cms.vint32(4, 4, 4),
                dr_par1 = cms.vdouble(0.8, 0.7, 0.6),
                dr_par2 = cms.vdouble(0.6, 0.5, 0.45)
            ),
            dz_par = cms.PSet(
                dz_exp = cms.vint32(4, 4, 4),
                dz_par1 = cms.vdouble(0.9, 0.8, 0.7),
                dz_par2 = cms.vdouble(0.8, 0.7, 0.55)
            ),
            maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
            maxChi2n = cms.vdouble(2.0, 1.4, 1.2),
            maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
            maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
            maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
            maxLostLayers = cms.vint32(3, 2, 2),
            min3DLayers = cms.vint32(3, 3, 4),
            minLayers = cms.vint32(3, 3, 3),
            minNVtxTrk = cms.int32(3),
            minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
            minPixelHits = cms.vint32(0, 0, 3)
        ),
        qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
        src = cms.InputTag('hltPhase2InitialStepTracks'),
        vertices = cms.InputTag('hltPhase2PixelVertices')
    )
    
    process.hltPhase2InitialStepTrackSelectionHighPurity = cms.EDProducer('TrackCollectionFilterCloner',
        copyExtras = cms.untracked.bool(True),
        copyTrajectories = cms.untracked.bool(False),
        minQuality = cms.string('highPurity'),
        originalMVAVals = cms.InputTag('hltPhase2InitialStepTrackCutClassifier','MVAValues'),
        originalQualVals = cms.InputTag('hltPhase2InitialStepTrackCutClassifier','QualityMasks'),
        originalSource = cms.InputTag('hltPhase2InitialStepTracks')
    )
    
    process.hltPhase2HighPtTripletStepClusters = cms.EDProducer('TrackClusterRemoverPhase2',
        TrackQuality = cms.string('highPurity'),
        maxChi2 = cms.double(9.0),
        mightGet = cms.optional.untracked.vstring,
        minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
        oldClusterRemovalInfo = cms.InputTag(''),
        overrideTrkQuals = cms.InputTag(''),
        phase2OTClusters = cms.InputTag('siPhase2Clusters'),
        phase2pixelClusters = cms.InputTag('siPixelClusters'),
        trackClassifier = cms.InputTag('','QualityMasks'),
        trajectories = cms.InputTag('hltPhase2InitialStepTracks')
    )
    
    process.hltPhase2HighPtTripletStepSeedLayers = cms.EDProducer('SeedingLayersEDProducer',
        BPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'),
            TTRHBuilder = cms.string('WithTrackAngle'),
            skipClusters = cms.InputTag('hltPhase2HighPtTripletStepClusters')
        ),
        FPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'),
            TTRHBuilder = cms.string('WithTrackAngle'),
            skipClusters = cms.InputTag('hltPhase2HighPtTripletStepClusters')
        ),
        MTEC = cms.PSet(
    
        ),
        MTIB = cms.PSet(
    
        ),
        MTID = cms.PSet(
    
        ),
        MTOB = cms.PSet(
    
        ),
        TEC = cms.PSet(
    
        ),
        TIB = cms.PSet(
    
        ),
        TID = cms.PSet(
    
        ),
        TOB = cms.PSet(
    
        ),
        layerList = cms.vstring(
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg'
        ),
        mightGet = cms.optional.untracked.vstring
    )
    
    process.hltPhase2HighPtTripletStepHitDoublets = cms.EDProducer('HitPairEDProducer',
        clusterCheck = cms.InputTag('trackerClusterCheck'),
        layerPairs = cms.vuint32(0, 1),
        maxElement = cms.uint32(50000000),
        maxElementTotal = cms.uint32(50000000),
        mightGet = cms.optional.untracked.vstring,
        produceIntermediateHitDoublets = cms.bool(True),
        produceSeedingHitSets = cms.bool(False),
        seedingLayers = cms.InputTag('hltPhase2HighPtTripletStepSeedLayers'),
        trackingRegions = cms.InputTag('hltPhase2HighPtTripletStepTrackingRegions'),
        trackingRegionsSeedingLayers = cms.InputTag('')
    )
    
    process.hltPhase2HighPtTripletStepHitTriplets = cms.EDProducer('CAHitTripletEDProducer',
        CAHardPtCut = cms.double(0.5),
        CAPhiCut = cms.double(0.06),
        CAThetaCut = cms.double(0.003),
        SeedComparitorPSet = cms.PSet(
            ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
            clusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
            clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
        ),
        doublets = cms.InputTag('hltPhase2HighPtTripletStepHitDoublets'),
        extraHitRPhitolerance = cms.double(0.032),
        maxChi2 = cms.PSet(
            enabled = cms.bool(True),
            pt1 = cms.double(0.8),
            pt2 = cms.double(8),
            value1 = cms.double(100),
            value2 = cms.double(6)
        ),
        mightGet = cms.untracked.vstring(
            'IntermediateHitDoublets_highPtTripletStepHitDoublets__RECO', 
            'IntermediateHitDoublets_hltPhase2HighPtTripletStepHitDoublets__RECO'
        ),
        useBendingCorrection = cms.bool(True)
    )
    
    process.hltPhase2HighPtTripletStepSeeds = cms.EDProducer('SeedCreatorFromRegionConsecutiveHitsEDProducer',
        MinOneOverPtError = cms.double(1),
        OriginTransverseErrorMultiplier = cms.double(1),
        SeedComparitorPSet = cms.PSet(
            ComponentName = cms.string('none')
        ),
        SeedMomentumForBOFF = cms.double(5),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string(''),
        mightGet = cms.untracked.vstring(
            'RegionsSeedingHitSets_highPtTripletStepHitTriplets__RECO', 
            'RegionsSeedingHitSets_hltPhase2HighPtTripletStepHitTriplets__RECO'
        ),
        propagator = cms.string('PropagatorWithMaterial'),
        seedingHitSets = cms.InputTag('hltPhase2HighPtTripletStepHitTriplets')
    )
    
    process.hltPhase2HighPtTripletStepTrackCandidates = cms.EDProducer('CkfTrackCandidateMaker',
        MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
        SimpleMagneticField = cms.string('ParabolicMf'),
        TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
        TrajectoryBuilderPSet = cms.PSet(
            refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryBuilder')
        ),
        TrajectoryCleaner = cms.string('hltPhase2HighPtTripletStepTrajectoryCleanerBySharedHits'),
        TransientInitialStateEstimatorParameters = cms.PSet(
            numberMeasurementsForFit = cms.int32(4),
            propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
            propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
        ),
        cleanTrajectoryAfterInOut = cms.bool(True),
        doSeedingRegionRebuilding = cms.bool(True),
        maxNSeeds = cms.uint32(100000),
        maxSeedsBeforeCleaning = cms.uint32(1000),
        numHitsForSeedCleaner = cms.int32(50),
        onlyPixelHitsForSeedCleaner = cms.bool(True),
        phase2clustersToSkip = cms.InputTag('hltPhase2HighPtTripletStepClusters'),
        reverseTrajectories = cms.bool(False),
        src = cms.InputTag('hltPhase2HighPtTripletStepSeeds'),
        useHitsSplitting = cms.bool(False)
    )
    
    process.hltPhase2FirstStepPrimaryVerticesUnsorted = cms.EDProducer('PrimaryVertexProducer',
        TkClusParameters = cms.PSet(
            TkDAClusParameters = cms.PSet(
                Tmin = cms.double(2.0),
                Tpurge = cms.double(2.0),
                Tstop = cms.double(0.5),
                coolingFactor = cms.double(0.6),
                d0CutOff = cms.double(3.0),
                dzCutOff = cms.double(3.0),
                uniquetrkweight = cms.double(0.8),
                vertexSize = cms.double(0.006),
                zmerge = cms.double(0.01)
            ),
            algorithm = cms.string('DA_vect')
        ),
        TkFilterParameters = cms.PSet(
            algorithm = cms.string('filter'),
            maxD0Significance = cms.double(4.0),
            maxEta = cms.double(4.0),
            maxNormalizedChi2 = cms.double(10.0),
            minPixelLayersWithHits = cms.int32(2),
            minPt = cms.double(0.9),
            minSiliconLayersWithHits = cms.int32(5),
            trackQuality = cms.string('any')
        ),
        TrackLabel = cms.InputTag('hltPhase2InitialStepTracks'),
        beamSpotLabel = cms.InputTag('offlineBeamSpot'),
        verbose = cms.untracked.bool(False),
        vertexCollections = cms.VPSet(cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string(''),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(0.0),
            useBeamConstraint = cms.bool(False)
        ))
    )
    
    process.hltPhase2Ak4CaloJetsForTrk = cms.EDProducer('FastjetJetProducer',
        Active_Area_Repeats = cms.int32(1),
        GhostArea = cms.double(0.01),
        Ghost_EtaMax = cms.double(5.0),
        Rho_EtaMax = cms.double(4.4),
        doAreaDiskApprox = cms.bool(False),
        doAreaFastjet = cms.bool(False),
        doPUOffsetCorr = cms.bool(False),
        doPVCorrection = cms.bool(True),
        doRhoFastjet = cms.bool(False),
        inputEMin = cms.double(0.0),
        inputEtMin = cms.double(0.3),
        jetAlgorithm = cms.string('AntiKt'),
        jetPtMin = cms.double(10.0),
        jetType = cms.string('CaloJet'),
        maxBadEcalCells = cms.uint32(9999999),
        maxBadHcalCells = cms.uint32(9999999),
        maxProblematicEcalCells = cms.uint32(9999999),
        maxProblematicHcalCells = cms.uint32(9999999),
        maxRecoveredEcalCells = cms.uint32(9999999),
        maxRecoveredHcalCells = cms.uint32(9999999),
        minSeed = cms.uint32(14327),
        nSigmaPU = cms.double(1.0),
        puPtMin = cms.double(10),
        rParam = cms.double(0.4),
        radiusPU = cms.double(0.5),
        src = cms.InputTag('caloTowerForTrk'),
        srcPVs = cms.InputTag('hltPhase2FirstStepPrimaryVerticesUnsorted'),
        useDeterministicSeed = cms.bool(True),
        voronoiRfact = cms.double(-0.9)
    )
    
    process.hltPhase2FirstStepPrimaryVertices = cms.EDProducer('RecoChargedRefCandidatePrimaryVertexSorter',
        assignment = cms.PSet(
            maxDistanceToJetAxis = cms.double(0.07),
            maxDtSigForPrimaryAssignment = cms.double(4.0),
            maxDxyForJetAxisAssigment = cms.double(0.1),
            maxDxyForNotReconstructedPrimary = cms.double(0.01),
            maxDxySigForNotReconstructedPrimary = cms.double(2),
            maxDzErrorForPrimaryAssignment = cms.double(0.05),
            maxDzForJetAxisAssigment = cms.double(0.1),
            maxDzForPrimaryAssignment = cms.double(0.1),
            maxDzSigForPrimaryAssignment = cms.double(5.0),
            maxJetDeltaR = cms.double(0.5),
            minJetPt = cms.double(25),
            preferHighRanked = cms.bool(False),
            useTiming = cms.bool(False)
        ),
        jets = cms.InputTag('hltPhase2Ak4CaloJetsForTrk'),
        particles = cms.InputTag('hltPhase2InitialStepTrackRefsForJets'),
        produceAssociationToOriginalVertices = cms.bool(False),
        produceNoPileUpCollection = cms.bool(False),
        producePileUpCollection = cms.bool(False),
        produceSortedVertices = cms.bool(True),
        qualityForPrimary = cms.int32(3),
        sorting = cms.PSet(
    
        ),
        trackTimeResoTag = cms.InputTag(''),
        trackTimeTag = cms.InputTag(''),
        usePVMET = cms.bool(True),
        vertices = cms.InputTag('hltPhase2FirstStepPrimaryVerticesUnsorted')
    )
    
    process.hltPhase2HighPtTripletStepTracks = cms.EDProducer('TrackProducer',
        AlgorithmName = cms.string('highPtTripletStep'),
        Fitter = cms.string('FlexibleKFFittingSmoother'),
        GeometricInnerState = cms.bool(False),
        MeasurementTracker = cms.string(''),
        MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        Propagator = cms.string('RungeKuttaTrackerPropagator'),
        SimpleMagneticField = cms.string(''),
        TTRHBuilder = cms.string('WithTrackAngle'),
        TrajectoryInEvent = cms.bool(False),
        alias = cms.untracked.string('ctfWithMaterialTracks'),
        beamSpot = cms.InputTag('offlineBeamSpot'),
        clusterRemovalInfo = cms.InputTag(''),
        src = cms.InputTag('hltPhase2HighPtTripletStepTrackCandidates'),
        useHitsSplitting = cms.bool(False),
        useSimpleMF = cms.bool(False)
    )
    
    process.hltPhase2HighPtTripletStepTrackCutClassifier = cms.EDProducer('TrackCutClassifier',
        beamspot = cms.InputTag('offlineBeamSpot'),
        ignoreVertices = cms.bool(False),
        mva = cms.PSet(
            dr_par = cms.PSet(
                d0err = cms.vdouble(0.003, 0.003, 0.003),
                d0err_par = cms.vdouble(0.002, 0.002, 0.001),
                dr_exp = cms.vint32(4, 4, 4),
                dr_par1 = cms.vdouble(0.7, 0.6, 0.6),
                dr_par2 = cms.vdouble(0.6, 0.5, 0.45)
            ),
            dz_par = cms.PSet(
                dz_exp = cms.vint32(4, 4, 4),
                dz_par1 = cms.vdouble(0.8, 0.7, 0.7),
                dz_par2 = cms.vdouble(0.6, 0.6, 0.55)
            ),
            maxChi2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            maxChi2n = cms.vdouble(2.0, 1.0, 0.8),
            maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
            maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
            maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
            maxLostLayers = cms.vint32(3, 2, 2),
            min3DLayers = cms.vint32(3, 3, 4),
            minLayers = cms.vint32(3, 3, 4),
            minNVtxTrk = cms.int32(3),
            minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
            minPixelHits = cms.vint32(0, 0, 3)
        ),
        qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
        src = cms.InputTag('hltPhase2HighPtTripletStepTracks'),
        vertices = cms.InputTag('hltPhase2PixelVertices')
    )
    
    process.hltPhase2HighPtTripletStepTrackSelectionHighPurity = cms.EDProducer('TrackCollectionFilterCloner',
        copyExtras = cms.untracked.bool(True),
        copyTrajectories = cms.untracked.bool(False),
        minQuality = cms.string('highPurity'),
        originalMVAVals = cms.InputTag('hltPhase2HighPtTripletStepTrackCutClassifier','MVAValues'),
        originalQualVals = cms.InputTag('hltPhase2HighPtTripletStepTrackCutClassifier','QualityMasks'),
        originalSource = cms.InputTag('hltPhase2HighPtTripletStepTracks')
    )
    
    process.trackAlgoPriorityOrder = cms.ESProducer('TrackAlgoPriorityOrderESProducer',
        ComponentName = cms.string('trackAlgoPriorityOrder'),
        algoOrder = cms.vstring(
            'initialStep', 
            'highPtTripletStep'
        ),
        appendToDataLabel = cms.string('')
    )
    
    process.hltPhase2GeneralTracks = cms.EDProducer('TrackListMerger',
        Epsilon = cms.double(-0.001),
        FoundHitBonus = cms.double(5.0),
        LostHitPenalty = cms.double(5.0),
        MaxNormalizedChisq = cms.double(1000.0),
        MinFound = cms.int32(3),
        MinPT = cms.double(0.9),
        ShareFrac = cms.double(0.19),
        TrackProducers = cms.VInputTag('hltPhase2InitialStepTrackSelectionHighPurity', 'hltPhase2HighPtTripletStepTrackSelectionHighPurity'),
        allowFirstHitShare = cms.bool(True),
        copyExtras = cms.untracked.bool(True),
        copyMVA = cms.bool(False),
        hasSelector = cms.vint32(0, 0),
        indivShareFrac = cms.vdouble(1.0, 1.0),
        makeReKeyedSeeds = cms.untracked.bool(False),
        newQuality = cms.string('confirmed'),
        selectedTrackQuals = cms.VInputTag(cms.InputTag('hltPhase2InitialStepTrackSelectionHighPurity'), cms.InputTag('hltPhase2HighPtTripletStepTrackSelectionHighPurity')),
        setsToMerge = cms.VPSet(cms.PSet(
            pQual = cms.bool(True),
            tLists = cms.vint32(0, 1)
        )),
        trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
        writeOnlyTrkQuals = cms.bool(False)
    )
    
    process.hltPhase2UnsortedOfflinePrimaryVertices = cms.EDProducer('PrimaryVertexProducer',
        TkClusParameters = cms.PSet(
            TkDAClusParameters = cms.PSet(
                Tmin = cms.double(2.0),
                Tpurge = cms.double(2.0),
                Tstop = cms.double(0.5),
                coolingFactor = cms.double(0.6),
                d0CutOff = cms.double(3.0),
                dzCutOff = cms.double(3.0),
                uniquetrkweight = cms.double(0.8),
                vertexSize = cms.double(0.006),
                zmerge = cms.double(0.01)
            ),
            algorithm = cms.string('DA_vect')
        ),
        TkFilterParameters = cms.PSet(
            algorithm = cms.string('filter'),
            maxD0Significance = cms.double(4.0),
            maxEta = cms.double(4.0),
            maxNormalizedChi2 = cms.double(10.0),
            minPixelLayersWithHits = cms.int32(2),
            minPt = cms.double(0.9),
            minSiliconLayersWithHits = cms.int32(5),
            trackQuality = cms.string('any')
        ),
        TrackLabel = cms.InputTag('hltPhase2GeneralTracks'),
        beamSpotLabel = cms.InputTag('offlineBeamSpot'),
        verbose = cms.untracked.bool(False),
        vertexCollections = cms.VPSet(
            cms.PSet(
                algorithm = cms.string('AdaptiveVertexFitter'),
                chi2cutoff = cms.double(2.5),
                label = cms.string(''),
                maxDistanceToBeam = cms.double(1.0),
                minNdof = cms.double(0.0),
                useBeamConstraint = cms.bool(False)
            ), 
            cms.PSet(
                algorithm = cms.string('AdaptiveVertexFitter'),
                chi2cutoff = cms.double(2.5),
                label = cms.string('WithBS'),
                maxDistanceToBeam = cms.double(1.0),
                minNdof = cms.double(2.0),
                useBeamConstraint = cms.bool(True)
            )
        )
    )
    
    process.hltPhase2TrackWithVertexRefSelectorBeforeSorting = cms.EDProducer('TrackWithVertexRefSelector',
        copyExtras = cms.untracked.bool(False),
        copyTrajectories = cms.untracked.bool(False),
        d0Max = cms.double(999.0),
        dzMax = cms.double(999.0),
        etaMax = cms.double(5.0),
        etaMin = cms.double(0.0),
        nSigmaDtVertex = cms.double(0),
        nVertices = cms.uint32(0),
        normalizedChi2 = cms.double(999999.0),
        numberOfLostHits = cms.uint32(999),
        numberOfValidHits = cms.uint32(0),
        numberOfValidPixelHits = cms.uint32(0),
        ptErrorCut = cms.double(9e+99),
        ptMax = cms.double(9e+99),
        ptMin = cms.double(0.9),
        quality = cms.string('highPurity'),
        rhoVtx = cms.double(0.2),
        src = cms.InputTag('hltPhase2GeneralTracks'),
        timeResosTag = cms.InputTag(''),
        timesTag = cms.InputTag(''),
        useVtx = cms.bool(True),
        vertexTag = cms.InputTag('hltPhase2UnsortedOfflinePrimaryVertices'),
        vtxFallback = cms.bool(True),
        zetaVtx = cms.double(1.0)
    )
    
    process.hltPhase2TrackRefsForJetsBeforeSorting = cms.EDProducer('ChargedRefCandidateProducer',
        particleType = cms.string('pi+'),
        src = cms.InputTag('hltPhase2TrackWithVertexRefSelectorBeforeSorting')
    )
    
    process.hltPhase2OfflinePrimaryVerticesWithBS = cms.EDProducer('RecoChargedRefCandidatePrimaryVertexSorter',
        assignment = cms.PSet(
            maxDistanceToJetAxis = cms.double(0.07),
            maxDtSigForPrimaryAssignment = cms.double(4.0),
            maxDxyForJetAxisAssigment = cms.double(0.1),
            maxDxyForNotReconstructedPrimary = cms.double(0.01),
            maxDxySigForNotReconstructedPrimary = cms.double(2),
            maxDzErrorForPrimaryAssignment = cms.double(0.05),
            maxDzForJetAxisAssigment = cms.double(0.1),
            maxDzForPrimaryAssignment = cms.double(0.1),
            maxDzSigForPrimaryAssignment = cms.double(5.0),
            maxJetDeltaR = cms.double(0.5),
            minJetPt = cms.double(25),
            preferHighRanked = cms.bool(False),
            useTiming = cms.bool(False)
        ),
        jets = cms.InputTag('hltPhase2Ak4CaloJetsForTrk'),
        particles = cms.InputTag('hltPhase2TrackRefsForJetsBeforeSorting'),
        produceAssociationToOriginalVertices = cms.bool(False),
        produceNoPileUpCollection = cms.bool(False),
        producePileUpCollection = cms.bool(False),
        produceSortedVertices = cms.bool(True),
        qualityForPrimary = cms.int32(3),
        sorting = cms.PSet(
    
        ),
        trackTimeResoTag = cms.InputTag(''),
        trackTimeTag = cms.InputTag(''),
        usePVMET = cms.bool(True),
        vertices = cms.InputTag('hltPhase2UnsortedOfflinePrimaryVertices','WithBS')
    )
    
    process.hltPhase2OfflinePrimaryVertices = cms.EDProducer('RecoChargedRefCandidatePrimaryVertexSorter',
        assignment = cms.PSet(
            maxDistanceToJetAxis = cms.double(0.07),
            maxDtSigForPrimaryAssignment = cms.double(4.0),
            maxDxyForJetAxisAssigment = cms.double(0.1),
            maxDxyForNotReconstructedPrimary = cms.double(0.01),
            maxDxySigForNotReconstructedPrimary = cms.double(2),
            maxDzErrorForPrimaryAssignment = cms.double(0.05),
            maxDzForJetAxisAssigment = cms.double(0.1),
            maxDzForPrimaryAssignment = cms.double(0.1),
            maxDzSigForPrimaryAssignment = cms.double(5.0),
            maxJetDeltaR = cms.double(0.5),
            minJetPt = cms.double(25),
            preferHighRanked = cms.bool(False),
            useTiming = cms.bool(False)
        ),
        jets = cms.InputTag('hltPhase2Ak4CaloJetsForTrk'),
        particles = cms.InputTag('hltPhase2TrackRefsForJetsBeforeSorting'),
        produceAssociationToOriginalVertices = cms.bool(False),
        produceNoPileUpCollection = cms.bool(False),
        producePileUpCollection = cms.bool(False),
        produceSortedVertices = cms.bool(True),
        qualityForPrimary = cms.int32(3),
        sorting = cms.PSet(
    
        ),
        trackTimeResoTag = cms.InputTag(''),
        trackTimeTag = cms.InputTag(''),
        usePVMET = cms.bool(True),
        vertices = cms.InputTag('hltPhase2UnsortedOfflinePrimaryVertices')
    )
    
    process.hltPhase2InclusiveVertexFinder = cms.EDProducer('InclusiveVertexFinder',
        beamSpot = cms.InputTag('offlineBeamSpot'),
        clusterizer = cms.PSet(
            clusterMaxDistance = cms.double(0.05),
            clusterMaxSignificance = cms.double(4.5),
            clusterMinAngleCosine = cms.double(0.5),
            distanceRatio = cms.double(20),
            maxTimeSignificance = cms.double(3.5),
            seedMax3DIPSignificance = cms.double(9999),
            seedMax3DIPValue = cms.double(9999),
            seedMin3DIPSignificance = cms.double(1.2),
            seedMin3DIPValue = cms.double(0.005)
        ),
        fitterRatio = cms.double(0.25),
        fitterSigmacut = cms.double(3),
        fitterTini = cms.double(256),
        maxNTracks = cms.uint32(30),
        maximumLongitudinalImpactParameter = cms.double(0.3),
        maximumTimeSignificance = cms.double(3),
        minHits = cms.uint32(8),
        minPt = cms.double(0.9),
        primaryVertices = cms.InputTag('hltPhase2OfflinePrimaryVertices'),
        tracks = cms.InputTag('hltPhase2GeneralTracks'),
        useDirectVertexFitter = cms.bool(True),
        useVertexReco = cms.bool(True),
        vertexMinAngleCosine = cms.double(0.95),
        vertexMinDLen2DSig = cms.double(2.5),
        vertexMinDLenSig = cms.double(0.5),
        vertexReco = cms.PSet(
            finder = cms.string('avr'),
            primcut = cms.double(1),
            seccut = cms.double(3),
            smoothing = cms.bool(True)
        )
    )
    
    process.hltPhase2VertexMerger = cms.EDProducer('VertexMerger',
        maxFraction = cms.double(0.7),
        minSignificance = cms.double(2),
        secondaryVertices = cms.InputTag('hltPhase2InclusiveVertexFinder')
    )
    
    process.hltPhase2TrackVertexArbitrator = cms.EDProducer('TrackVertexArbitrator',
        beamSpot = cms.InputTag('offlineBeamSpot'),
        dLenFraction = cms.double(0.333),
        dRCut = cms.double(0.4),
        distCut = cms.double(0.04),
        fitterRatio = cms.double(0.25),
        fitterSigmacut = cms.double(3),
        fitterTini = cms.double(256),
        maxTimeSignificance = cms.double(3.5),
        primaryVertices = cms.InputTag('hltPhase2OfflinePrimaryVertices'),
        secondaryVertices = cms.InputTag('hltPhase2VertexMerger'),
        sigCut = cms.double(5),
        trackMinLayers = cms.int32(4),
        trackMinPixels = cms.int32(1),
        trackMinPt = cms.double(0.9),
        tracks = cms.InputTag('hltPhase2GeneralTracks')
    )

    process.hltPhase2InclusiveSecondaryVertices = cms.EDProducer('VertexMerger',
        maxFraction = cms.double(0.2),
        minSignificance = cms.double(10.0),
        secondaryVertices = cms.InputTag('hltPhase2TrackVertexArbitrator')
    )

    ###
    ### Sequences
    ###

    process.itLocalReco = cms.Sequence(
        process.siPhase2Clusters
      + process.siPixelClusters
      + process.siPixelClusterShapeCache
      + process.siPixelRecHits
    )

    process.otLocalReco = cms.Sequence(
        process.MeasurementTrackerEvent
    )

    process.hltPhase2PixelTracksSequence = cms.Sequence(
        process.hltPhase2PixelTrackFilterByKinematics
      + process.hltPhase2PixelFitterByHelixProjections
      + process.hltPhase2PixelTracksTrackingRegions
      + process.hltPhase2PixelTracksSeedLayers
      + process.hltPhase2PixelTracksHitDoublets
      + process.hltPhase2PixelTracksHitQuadruplets
      + process.hltPhase2PixelTracks
    )

    process.hltPhase2PixelVerticesSequence = cms.Sequence(
        process.hltPhase2PixelVertices
      + process.hltPhase2TrimmedPixelVertices
    )

    process.hltPhase2InitialStepPVSequence = cms.Sequence(
        process.hltPhase2FirstStepPrimaryVerticesUnsorted
      + process.hltPhase2InitialStepTrackRefsForJets
      + process.hcalGlobalRecoSequence
      + process.caloTowerForTrk
      + process.hltPhase2Ak4CaloJetsForTrk
      + process.hltPhase2FirstStepPrimaryVertices
    )

    process.hltPhase2InitialStepSequence = cms.Sequence(
#       process.hltPhase2InitialStepSeedLayers
#     + process.hltPhase2InitialStepTrackingRegions
#     + process.hltPhase2InitialStepHitDoublets
#     + process.hltPhase2InitialStepHitQuadruplets
        process.hltPhase2InitialStepSeeds
      + process.hltPhase2InitialStepTrackCandidates
      + process.hltPhase2InitialStepTracks
#     + process.hltPhase2InitialStepPVSequence # use pixelVertices
      + process.hltPhase2InitialStepTrackCutClassifier
      + process.hltPhase2InitialStepTrackSelectionHighPurity
    )

    process.hltPhase2HighPtTripletStepSequence = cms.Sequence(
        process.hltPhase2HighPtTripletStepClusters
      + process.hltPhase2HighPtTripletStepSeedLayers
      + process.hltPhase2HighPtTripletStepTrackingRegions
      + process.hltPhase2HighPtTripletStepHitDoublets
      + process.hltPhase2HighPtTripletStepHitTriplets
      + process.hltPhase2HighPtTripletStepSeeds
      + process.hltPhase2HighPtTripletStepTrackCandidates
      + process.hltPhase2HighPtTripletStepTracks
      + process.hltPhase2HighPtTripletStepTrackCutClassifier
      + process.hltPhase2HighPtTripletStepTrackSelectionHighPurity
    )

    process.hltPhase2VertexReco = cms.Sequence(
        process.hltPhase2InitialStepPVSequence # pixelVertices moved to here, for now still keeping it
      + process.hltPhase2UnsortedOfflinePrimaryVertices
      + process.hltPhase2TrackWithVertexRefSelectorBeforeSorting
      + process.hltPhase2TrackRefsForJetsBeforeSorting
      + process.hltPhase2OfflinePrimaryVertices
      + process.hltPhase2OfflinePrimaryVerticesWithBS
      + process.hltPhase2InclusiveVertexFinder
      + process.hltPhase2VertexMerger
      + process.hltPhase2TrackVertexArbitrator
      + process.hltPhase2InclusiveSecondaryVertices
    )

    process.globalreco_tracking = cms.Sequence(
        process.itLocalReco
      + process.offlineBeamSpot
      + process.otLocalReco
      + process.trackerClusterCheck
      + process.hltPhase2PixelTracksSequence # pixeltracks
      + process.hltPhase2PixelVerticesSequence # pixelvertices
      + process.hltPhase2InitialStepSequence
      + process.hltPhase2HighPtTripletStepSequence
      + process.hltPhase2GeneralTracks
      + process.hltPhase2VertexReco
    )

    # clones of hltPhase2GeneralTracks and process.hltPhase2OfflinePrimaryVertices
    # to reduce the need for modications in downstream modules
    process.generalTracks = process.hltPhase2GeneralTracks.clone()
    process.offlinePrimaryVertices = process.hltPhase2OfflinePrimaryVertices.clone()

    process.globalreco_tracking += cms.Sequence(
        process.generalTracks
      + process.offlinePrimaryVertices
    )

    # remove globalreco_trackingTask to avoid any ambiguities
    # with the updated sequence process.globalreco_tracking
    if hasattr(process, 'globalreco_trackingTask'):
       del process.globalreco_trackingTask

    return process
