# LST + mkfit Tracking Tutorial for Phase-2 HLT

## Table of Contents
1. [Introduction](#introduction)
2. [What is LST (Line Segment Tracking)?](#what-is-lst)
3. [What is mkfit (Matriplex Kalman Filter)?](#what-is-mkfit)
4. [How LST and mkfit Work Together](#how-they-work-together)
5. [Performance Benefits](#performance-benefits)
6. [How to Enable LST + mkfit in Your Configuration](#how-to-enable)
7. [Technical Deep Dive](#technical-deep-dive)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

This tutorial explains how to use **LST (Line Segment Tracking)** and **mkfit** tracking algorithms in Phase-2 HLT reconstruction for CMSSW_15_1_0_pre4.

Traditional HLT tracking uses the **CKF (Combinatorial Kalman Filter)** algorithm, which works well but becomes challenging at high pileup (PU) due to:
- Combinatorial explosion of hit patterns
- Sequential processing
- CPU-intensive computations

LST + mkfit provides an alternative approach optimized for Phase-2 HL-LHC conditions (200 PU):
- **LST**: GPU-accelerated pattern recognition
- **mkfit**: Parallelized track fitting (3.5-7x speedup)

---

## What is LST?

### LST Overview

**LST (Line Segment Tracking)** is a GPU-friendly track pattern recognition algorithm designed for the Phase-2 CMS detector.

### Key Concepts

1. **Line Segments**: Instead of looking at individual hits, LST builds small track segments (doublets, triplets) from hits in adjacent detector layers.

2. **Segment Linking**: These segments are progressively linked together to form longer track candidates:
   - Mini Doublets (MD): Pairs of hits in adjacent layers
   - Segments (SG): Connected mini doublets
   - Triplets (T3): Three connected segments
   - Tracklets (T5/Quintuplets): Five connected segments forming a complete track

3. **GPU Acceleration**: The algorithm is implemented using the **Alpaka** framework, which allows it to run on:
   - NVIDIA GPUs (CUDA backend)
   - AMD GPUs (ROCm backend)
   - CPUs (serial backend for development/testing)

### Why LST?

- **Parallel by Design**: Each hit combination can be evaluated independently
- **High PU Tolerance**: Segment-based approach reduces combinatorics
- **Phase-2 Optimized**: Designed for the extended Phase-2 tracker geometry
- **Fast**: Pattern recognition is 10-30x faster on GPU compared to CPU CKF

### LST Configuration in CMSSW

LST consists of three main components:

```python
# 1. Input Producer: Prepares hits and seed tracks for LST
lstInputProducer = cms.EDProducer('LSTInputProducer@alpaka',
    ptCut = cms.double(0.8),  # Minimum track pT
    phase2OTRecHits = cms.InputTag('siPhase2RecHits'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    seedTracks = cms.VInputTag(
        'lstInitialStepSeedTracks',
        'lstHighPtTripletStepSeedTracks'
    )
)

# 2. LST Producer: Main pattern recognition algorithm
lstProducer = cms.EDProducer('LSTProducer@alpaka',
    lstInput = cms.InputTag('lstInputProducer'),
    ptCut = cms.double(0.8),
    nopLSDupClean = cms.bool(False),  # Duplicate cleaning
    tcpLSTriplets = cms.bool(False),  # Use quintuplets (T5)
)

# 3. Output Converter: Converts LST tracks to standard format
lstOutputConverter = cms.EDProducer('LSTOutputConverter',
    lstOutput = cms.InputTag('lstProducer'),
    includeT5s = cms.bool(True),  # Include quintuplet tracks
)
```

---

## What is mkfit?

### mkfit Overview

**mkfit (Matriplex Kalman Filter)** is a parallelized track fitting algorithm that uses:
- **Matriplex operations**: Process multiple tracks simultaneously using SIMD vectorization
- **Kalman Filter**: Standard track fitting technique, but executed in parallel

### Key Concepts

1. **Vectorization**: Instead of fitting one track at a time:
   ```
   Traditional: Fit Track1 → Fit Track2 → Fit Track3 → ...
   mkfit:      Fit [Track1, Track2, Track3, ..., TrackN] in parallel
   ```

2. **Matriplex Library**: Custom matrix library that operates on "matrices of matrices":
   - Process N tracks simultaneously
   - Use CPU vector instructions (AVX2, AVX-512)
   - Significant speedup from parallel execution

3. **Kalman Filter Steps** (executed in parallel):
   - Propagation: Extrapolate track from one layer to the next
   - Update: Incorporate new hit information
   - Chi2 calculation: Evaluate track quality

### Why mkfit?

- **3.5-7x Speedup**: Compared to standard CKF track fitting
- **CPU-based**: No GPU required (but can use CPU vector units)
- **Drop-in Replacement**: Uses same hit inputs and produces same output format
- **Mature**: Already used in CMS offline reconstruction

### mkfit Configuration in CMSSW

mkfit requires several components:

```python
# 1. Hit converters: Transform hits to mkfit format
mkFitSiPixelHits = cms.EDProducer("mkFitSiPixelHitConverter",
    pixelRecHits = cms.InputTag("siPixelRecHits")
)

mkFitSiStripHits = cms.EDProducer("mkFitSiStripHitConverter",
    stripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
)

# 2. Event of hits: Organize hits by layer
mkFitEventOfHits = cms.EDProducer("mkFitEventOfHitsProducer",
    pixelHits = cms.InputTag("mkFitSiPixelHits"),
    stripHits = cms.InputTag("mkFitSiStripHits")
)

# 3. Seed converter: Prepare seeds for mkfit
mkFitSeeds = cms.EDProducer("mkFitSeedConverter",
    seeds = cms.InputTag("initialStepSeeds")
)

# 4. mkfit configuration: Load algorithm parameters
mkFitConfig = cms.ESProducer("mkFitIterationConfigESProducer",
    config = 'RecoTracker/MkFit/data/mkfit-phase2-initialStep.json'
)

# 5. mkfit producer: Main track fitting
mkFitProducer = cms.EDProducer("mkFitProducer",
    pixelHits = cms.InputTag("mkFitSiPixelHits"),
    stripHits = cms.InputTag("mkFitSiStripHits"),
    eventOfHits = cms.InputTag("mkFitEventOfHits"),
    seeds = cms.InputTag("mkFitSeeds"),
    config = cms.ESInputTag('', 'mkFitConfig')
)

# 6. Output converter: Back to standard format
mkFitOutput = cms.EDProducer("mkFitOutputConverter",
    mkFitSeeds = cms.InputTag("mkFitSeeds"),
    mkFitOutput = cms.InputTag("mkFitProducer")
)
```

---

## How They Work Together

### Integration Workflow

The LST + mkfit integration replaces the standard CKF tracking workflow:

#### Traditional CKF Workflow:
```
Pixel Hits
   ↓
Seeding (e.g., quadruplets)
   ↓
CKF Pattern Recognition (track candidates)
   ↓
CKF Track Fitting (Kalman filter)
   ↓
Track Collection
```

#### LST + mkfit Workflow:
```
Pixel/Strip Hits
   ↓
Initial Seeds (same as before)
   ↓
LST Pattern Recognition (GPU)
   │
   ├─→ Build line segments
   ├─→ Link segments → quintuplets
   └─→ Output track candidates
   ↓
Convert to standard format
   ↓
mkfit Track Fitting (CPU parallel)
   │
   ├─→ Vectorized propagation
   ├─→ Parallel hit updates
   └─→ Chi2 evaluation
   ↓
Track Collection
```

### Division of Labor

1. **LST handles**:
   - Pattern recognition (find which hits belong together)
   - Operates on GPU
   - Produces high-quality track candidates

2. **mkfit handles**:
   - Track fitting (refine track parameters)
   - Operates on CPU with vectorization
   - Produces final fitted tracks

3. **Why separate?**:
   - Pattern recognition is highly parallel → Good for GPU
   - Track fitting needs precise floating point → Good for CPU with vector units
   - Best of both worlds: GPU pattern recognition + CPU fitting

---

## Performance Benefits

### Expected Speedups (compared to CKF)

| Component | Speedup | Notes |
|-----------|---------|-------|
| LST Pattern Recognition | 10-30x | On GPU vs CPU CKF |
| mkfit Track Fitting | 3.5-7x | Vectorized CPU vs standard CKF |
| Overall Tracking | 5-15x | Depends on GPU availability |

### Scaling with Pileup

At Phase-2 conditions (PU=200):
- CKF: Scales poorly, combinatorics become overwhelming
- LST: Scales better due to segment-based approach
- mkfit: Constant speedup regardless of PU

### Resource Usage

- **GPU Memory**: ~2-4 GB for LST (Phase-2 detector)
- **CPU Cores**: mkfit benefits from more cores (linear scaling)
- **Power**: GPU increases power consumption but reduces time

---

## How to Enable

### Method 1: Direct Tracking Version Selection

Modify your `jmeTriggerNTuple_cfg.py` to use TRK version 'v08':

```python
# In jmeTriggerNTuple_cfg.py
from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_redefineReconstructionSequences

# Use LST + mkfit tracking
process = customise_hltPhase2_redefineReconstructionSequences(
    process,
    TRK='v08',      # LST + mkfit tracking
    useTICL=False   # Use HGCAL TICL or not
)
```

### Method 2: Convenience Functions

Use pre-defined convenience functions:

```python
# Option A: JME reconstruction without filters
from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_scheduleHLTJMERecoWithoutFilters_TRKv08

process = customise_hltPhase2_scheduleHLTJMERecoWithoutFilters_TRKv08(process)

# Option B: Full JME triggers with LST + mkfit
from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_scheduleJMETriggers_TRKv08

process = customise_hltPhase2_scheduleJMETriggers_TRKv08(process)

# Option C: With TICL enabled
from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_scheduleJMETriggers_TRKv08_TICL

process = customise_hltPhase2_scheduleJMETriggers_TRKv08_TICL(process)
```

### Method 3: Comparison Configuration

To compare different tracking algorithms, create multiple config files:

```bash
# Create configs for comparison
cp jmeTriggerNTuple_cfg.py jmeTriggerNTuple_CKF_cfg.py      # Keep default (CKF)
cp jmeTriggerNTuple_cfg.py jmeTriggerNTuple_LSTmkfit_cfg.py # Use TRK='v08'
```

Edit `jmeTriggerNTuple_LSTmkfit_cfg.py`:
```python
# Change TRK version to v08
process = customise_hltPhase2_redefineReconstructionSequences(
    process,
    TRK='v08',  # Changed from 'v07p2' to 'v08'
    useTICL=False
)
```

### Available Tracking Versions

| Version | Description | Algorithm |
|---------|-------------|-----------|
| v00 | Original Phase-2 tracking | CKF |
| v02 | Updated Phase-2 tracking | CKF |
| v06 | Iterative tracking v6 | CKF |
| v06p1 | Iterative tracking v6.1 | CKF |
| v06p3 | Iterative tracking v6.3 | CKF |
| v07p2 | Latest CKF tracking | CKF |
| **v08** | **LST + mkfit tracking** | **LST + mkfit** |

---

## Technical Deep Dive

### LST Algorithm Details

#### 1. Module Maps (lstModulesDevESProducer)

LST needs detector geometry information on the GPU. The ES Producer loads:
- Module positions (x, y, z)
- Module orientations
- Layer structure
- Connectivity information

This data is prepared on the CPU and transferred to GPU memory at job start.

#### 2. Seed Track Preparation

```python
# Convert TrackingSeeds to Tracks (without refitting)
lstInitialStepSeedTracks = cms.EDProducer("TrackFromSeedProducer",
    src = cms.InputTag("initialStepSeeds"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    TTRHBuilder = cms.string("WithoutRefit")  # Fast conversion
)
```

Why? LST needs approximate track directions to:
- Constrain segment building
- Reduce combinatorics
- Improve pattern recognition efficiency

#### 3. LST Input Preparation (lstInputProducer)

Creates GPU-friendly data structures:
- **Hit List**: All hits organized by layer
- **Seed Track List**: Seed tracks in GPU format
- **Module Map**: Detector geometry (from ES)

#### 4. LST Pattern Recognition (lstProducer)

Main algorithm steps executed on GPU:

```
For each seed track:
  1. Build Mini Doublets (MD)
     - Find hit pairs in adjacent layers
     - Apply compatibility cuts

  2. Build Segments (SG)
     - Connect compatible MDs
     - Check geometric consistency

  3. Build Triplets (T3)
     - Link segments forming 3-point tracks
     - Apply circle fit quality cuts

  4. Build Tracklets (T5)
     - Extend triplets to 5-point tracks
     - Full helix fit
     - Chi2 evaluation

  5. Duplicate Removal
     - Remove tracks sharing too many hits
     - Keep highest quality tracks
```

Key parameters:
- `ptCut`: Minimum track pT (0.8 GeV default)
- `nopLSDupClean`: Enable pLS duplicate cleaning
- `tcpLSTriplets`: Use triplets instead of quintuplets

#### 5. LST Output Conversion (lstOutputConverter)

Converts LST internal format to standard CMSSW format:

```python
lstOutputConverter = cms.EDProducer('LSTOutputConverter',
    lstOutput = cms.InputTag('lstProducer'),
    includeT5s = cms.bool(True),         # Include quintuplets
    includeNonpLSTSs = cms.bool(False),  # Only pLS triplets
    # Creates TrackCandidates compatible with standard track fitting
)
```

Output: `TrackCandidate` collection compatible with any CMSSW track fitter

### mkfit Algorithm Details

#### 1. Hit Conversion

```python
# Pixel hits
mkFitSiPixelHits = mkFitSiPixelHitConverter.clone(
    pixelRecHits = cms.InputTag("siPixelRecHits")
)

# Strip hits
mkFitSiStripHits = mkFitSiStripHitConverter.clone(
    stripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
)
```

Converts CMSSW hit format to mkfit internal format:
- Strips global position, error matrix
- Organizes by detector module
- Prepares for fast lookup

#### 2. Event of Hits

```python
mkFitEventOfHits = mkFitEventOfHitsProducer.clone(
    pixelHits = cms.InputTag("mkFitSiPixelHits"),
    stripHits = cms.InputTag("mkFitSiStripHits")
)
```

Creates layer-organized hit structure:
- Hits grouped by layer
- Fast spatial lookup structures
- Optimized for vectorized access

#### 3. Seed Conversion

```python
mkFitSeeds = mkFitSeedConverter.clone(
    seeds = cms.InputTag("lstOutputConverter")
)
```

Converts TrackCandidate (from LST) to mkfit seed format:
- Extract starting track parameters
- Prepare for parallel processing
- Group into vectorization blocks

#### 4. mkfit Configuration

```python
mkFitConfig = mkFitIterationConfigESProducer.clone(
    config = 'RecoTracker/MkFit/data/mkfit-phase2-initialStep.json'
)
```

JSON configuration file contains:
- Chi2 cuts per layer
- Number of hit candidates to consider
- Backward fit options
- Duplicate removal criteria

Example JSON structure:
```json
{
  "m_iteration_index": 0,
  "m_track_algorithm": 4,
  "m_requires_seed_hit_sorting": true,
  "m_backward_fit_to_pca": true,
  "m_max_chi2_per_hit": 20.0,
  ...
}
```

#### 5. mkfit Producer

```python
mkFitProducer = mkFitProducer.clone(
    pixelHits = cms.InputTag("mkFitSiPixelHits"),
    stripHits = cms.InputTag("mkFitSiStripHits"),
    eventOfHits = cms.InputTag("mkFitEventOfHits"),
    seeds = cms.InputTag("mkFitSeeds"),
    config = cms.ESInputTag('', 'mkFitConfig')
)
```

Main fitting algorithm:
```
Group seeds into blocks of N (e.g., N=64)
For each block in parallel:
  For each layer:
    1. Propagate all tracks to layer (vectorized)
    2. Find hit candidates (vectorized search)
    3. Update track parameters (vectorized KF)
    4. Evaluate chi2 (vectorized)

  Backward fit (smooth tracks)
  Quality evaluation
```

Vectorization example:
```cpp
// Traditional: Process one track at a time
for (int i = 0; i < nTracks; i++) {
    track[i] = propagate(track[i], layer);
}

// mkfit: Process N tracks simultaneously
MPlexF track_matrix(N, 5);  // N tracks, 5 parameters each
propagate_vectorized(track_matrix, layer);  // Single call for all N
```

#### 6. Output Conversion

```python
mkFitOutput = mkFitOutputConverter.clone(
    mkFitSeeds = cms.InputTag("mkFitSeeds"),
    mkFitOutput = cms.InputTag("mkFitProducer")
)
```

Converts back to standard CMSSW `TrackCandidate` format for downstream processing.

### Complete Sequence

The full `initialStepSequence` with LST + mkfit:

```python
process.initialStepSequence = cms.Sequence(
    # LST Pattern Recognition
    process.lstInitialStepSeedTracks
  + process.lstHighPtTripletStepSeedTracks
  + process.lstInputProducer
  + process.lstProducer
  + process.lstOutputConverter

    # mkfit Track Fitting
  + process.initialStepMkFitSiPixelHits
  + process.initialStepMkFitSiStripHits
  + process.initialStepMkFitEventOfHits
  + process.initialStepMkFitSeeds
  + process.initialStepMkFit
  + process.initialStepTrackCandidates

    # Final Track Fitting & Quality
  + process.initialStepTracks
  + process.initialStepTrackCutClassifier
  + process.initialStepTracksSelectionHighPurity
)
```

---

## Troubleshooting

### GPU Not Available

If GPU is not available, LST will automatically fall back to CPU serial backend:

```python
# Alpaka will use CPU serial backend automatically
# Performance will be slower but should still work
```

Check backend being used:
```bash
# Check what backends are available
edmPluginDump | grep alpaka
```

### Memory Issues

LST on GPU requires ~2-4 GB GPU memory. If you encounter OOM errors:

1. Reduce number of events per job:
   ```python
   process.maxEvents = cms.untracked.PSet(
       input = cms.untracked.int32(10)  # Process fewer events
   )
   ```

2. Check GPU memory:
   ```bash
   nvidia-smi  # For NVIDIA GPUs
   rocm-smi    # For AMD GPUs
   ```

### Compilation Errors

If you get compilation errors after adding v08:

1. Rebuild CMSSW:
   ```bash
   cd $CMSSW_BASE/src
   scram b clean
   scram b -j 8
   ```

2. Check that LST and mkfit packages are available:
   ```bash
   # Check LST
   ls $CMSSW_RELEASE_BASE/src/RecoTracker/LST/

   # Check mkfit
   ls $CMSSW_RELEASE_BASE/src/RecoTracker/MkFit/
   ```

### Runtime Errors

**Error: "Unknown tracking version v08"**

Solution: Make sure you've imported and added v08 to the dictionary in `customizeHLTForPhase2.py`

**Error: "LSTProducer not found"**

Solution: LST is only available in CMSSW_15_1_0_pre4 and later. Check your CMSSW version:
```bash
echo $CMSSW_VERSION
```

**Error: "mkFitProducer configuration file not found"**

Solution: The Phase-2 mkfit config might not exist. Use Phase-1 config temporarily:
```python
process.initialStepMkFitConfig = mkFitIterationConfigESProducer.clone(
    config = 'RecoTracker/MkFit/data/mkfit-phase1-initialStep.json'  # Use phase1
)
```

### Performance Monitoring

Compare tracking performance:

```python
# Add timing service to config
process.Timing = cms.Service("Timing",
    summaryOnly = cms.untracked.bool(True)
)

# Run and compare timing
cmsRun jmeTriggerNTuple_cfg.py  # CKF
cmsRun jmeTriggerNTuple_LSTmkfit_cfg.py  # LST + mkfit
```

Check track efficiency in NTuple:
- Track multiplicity
- pT distribution
- Hit counts per track
- Track quality variables

---

## Summary

### Key Takeaways

1. **LST**: GPU-accelerated pattern recognition
   - 10-30x faster than CKF pattern recognition
   - Optimized for high PU
   - Requires GPU (but has CPU fallback)

2. **mkfit**: Parallelized track fitting
   - 3.5-7x faster than standard Kalman filter
   - CPU-based with vectorization
   - Drop-in replacement for CKF fitting

3. **Integration**: Both work together seamlessly
   - LST finds track candidates
   - mkfit fits the tracks
   - Standard CMSSW output format

4. **How to Use**: Simply change TRK='v08' in your config
   - No other changes needed
   - Compatible with existing NTuplizer
   - Output format identical to CKF tracks

### Next Steps

1. **Test**: Run with your MC samples and compare to CKF
2. **Validate**: Check track efficiency, fake rate, timing
3. **Optimize**: Tune LST parameters for your use case
4. **Report**: Share results with tracking group

### References

- LST Paper: [arXiv:2203.XXXXX]
- mkfit Paper: [JINST 15 (2020) P06028]
- CMSSW Documentation: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideTracker
- Alpaka Framework: https://alpaka.readthedocs.io/

### Contact

For questions about:
- **LST**: CMS LST developers (tracking group)
- **mkfit**: CMS mkfit developers (tracking group)
- **This integration**: JMETriggerAnalysis maintainers

---

**Generated with LST + mkfit for Phase-2 HLT - Version 1.0**
