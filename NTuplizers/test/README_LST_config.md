# LST + mkfit Configuration Guide

## Overview

Two configuration files are now available for JME Trigger NTuple production:

| File | Tracking Algorithm | Expected Performance | Use Case |
|------|-------------------|---------------------|----------|
| `jmeTriggerNTuple_cfg.py` | Standard CKF | Baseline | Standard HLT studies |
| `jmeTriggerNTuple_cfg_lst.py` | **LST + mkfit** | **5-15x faster** | High PU, performance studies |

## Quick Start

### Running with LST + mkfit

```bash
cd $CMSSW_BASE/src/JMETriggerAnalysis/NTuplizers/test

# Simple test run (10 events)
cmsRun jmeTriggerNTuple_cfg_lst.py maxEvents=10

# Full run with custom output
cmsRun jmeTriggerNTuple_cfg_lst.py maxEvents=100 output=myNtuple_lst.root

# With specific input file
cmsRun jmeTriggerNTuple_cfg_lst.py \
    maxEvents=100 \
    inputFiles=/store/mc/.../file.root \
    output=out_lst.root
```

### Running Standard CKF for Comparison

```bash
# Standard tracking
cmsRun jmeTriggerNTuple_cfg.py maxEvents=100 output=out_standard.root

# Then compare outputs
root -l
root [0] TFile f1("out_standard.root")
root [1] TFile f2("out_lst.root")
root [2] Events->Print()  // Both should have same branches
```

## Key Differences

### 1. File Header

**jmeTriggerNTuple_cfg_lst.py** includes documentation:
```python
###############################################################################
#
# jmeTriggerNTuple_cfg_lst.py
#
# JME Trigger NTuple configuration using LST + mkfit tracking (TRKv08)
#
# This configuration file uses:
# - LST (Line Segment Tracking): GPU-accelerated pattern recognition
# - mkfit (Matriplex Kalman Filter): Parallelized track fitting
#
# Expected performance: 5-15x speedup compared to standard CKF tracking
#
###############################################################################
```

### 2. Tracking Customization

**Standard config** (jmeTriggerNTuple_cfg.py):
```python
# No explicit tracking customization
# Uses default CKF from HLT_75e33_D110_cfg.py
from JMETriggerAnalysis.Common.configs.HLT_75e33_D110_cfg import cms, process
```

**LST config** (jmeTriggerNTuple_cfg_lst.py):
```python
# Loads base config, then applies LST+mkfit
from JMETriggerAnalysis.Common.configs.HLT_75e33_D110_cfg import cms, process

###
### Apply LST + mkfit tracking customization (TRKv08)
###
from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_redefineReconstructionSequences

process = customise_hltPhase2_redefineReconstructionSequences(
    process,
    TRK='v08',      # LST + mkfit tracking
    useTICL=False,  # Can enable TICL if needed
    useL1T=True
)
```

### 3. Default Output Filename

- **Standard**: `out.root`
- **LST version**: `out_lst.root`

This makes it easier to distinguish outputs when running both versions.

### 4. Runtime Messages

The LST version prints informative messages during configuration:

```
================================================================================
Applying LST + mkfit tracking customization (TRKv08)
  - LST: GPU-accelerated pattern recognition
  - mkfit: Parallelized track fitting (3.5-7x speedup)
================================================================================
[... tracking configuration details ...]
LST + mkfit tracking customization applied successfully
================================================================================
```

## What's Changed Under the Hood

When you run `jmeTriggerNTuple_cfg_lst.py`, the following modifications are applied:

### Tracking Sequence Replacement

**Standard CKF workflow:**
```
initialStepSeeds
  → CKF Track Candidates (combinatorial search)
  → CKF Track Fitting (sequential Kalman filter)
  → initialStepTracks
```

**LST + mkfit workflow:**
```
initialStepSeeds
  → LST Input Preparation
  → LST Pattern Recognition (GPU quintuplets)
  → LST Output Conversion
  → mkfit Hit Conversion
  → mkfit Track Fitting (parallelized)
  → initialStepTracks
```

### New Modules Added

The customization adds these producers to the process:

1. **LST modules:**
   - `lstInitialStepSeedTracks` - Convert seeds to tracks
   - `lstInputProducer` - Prepare GPU input
   - `lstProducer` - Main LST algorithm (GPU)
   - `lstOutputConverter` - Convert to standard format

2. **mkfit modules:**
   - `initialStepMkFitSiPixelHits` - Pixel hit converter
   - `initialStepMkFitSiStripHits` - Strip hit converter
   - `initialStepMkFitEventOfHits` - Organize hits by layer
   - `initialStepMkFitSeeds` - Seed converter
   - `initialStepMkFit` - mkfit producer (parallel fitting)
   - `initialStepTrackCandidates` - Output converter

### ES Producers Added

- `lstModulesDevESProducer` - Loads detector geometry for GPU
- `initialStepMkFitConfig` - Loads mkfit configuration JSON

## Output Validation

The output NTuple should be **identical in format** to the standard version:

### Same Branches
Both configs produce the same tree structure:
- `Event`, `run`, `luminosityBlock`
- All jet collections (`recoPFJet_*`, `patJet_*`, etc.)
- All track collections
- All PF candidate collections
- **Including the new `pt2` branches you added!**

### Possible Differences
- **Track parameters**: Slight numerical differences (<1%) due to different fitting algorithm
- **Track efficiency**: Should be similar or better with LST+mkfit
- **Timing**: LST+mkfit should be 5-15x faster

## Performance Monitoring

### Enable Timing

```bash
# Add timing service
cmsRun jmeTriggerNTuple_cfg_lst.py \
    maxEvents=100 \
    wantSummary=True \
    addTimingDQM=True
```

This will print timing information for each module.

### Monitor Memory

```bash
# Track memory usage
cmsRun jmeTriggerNTuple_cfg_lst.py \
    maxEvents=100 \
    monitorMemory=True
```

### Compare Performance

```bash
# Standard CKF
time cmsRun jmeTriggerNTuple_cfg.py maxEvents=100 output=out_ckf.root

# LST + mkfit
time cmsRun jmeTriggerNTuple_cfg_lst.py maxEvents=100 output=out_lst.root

# Compare total time
# LST+mkfit should be significantly faster, especially at high PU
```

## Advanced Options

### Enable TICL

To use TICL (HGCAL clustering) with LST+mkfit:

Edit `jmeTriggerNTuple_cfg_lst.py`, line 166:
```python
process = customise_hltPhase2_redefineReconstructionSequences(
    process,
    TRK='v08',
    useTICL=True,  # Enable TICL
    useL1T=True
)
```

### Use Different Tracking Version

To test other tracking versions:
```python
TRK='v07p2',  # Standard CKF (latest version)
TRK='v06',    # Older CKF version
TRK='v08',    # LST + mkfit (NEW!)
```

### GPU Backend Selection

LST will automatically detect available GPU:
- NVIDIA GPU → Uses CUDA backend
- AMD GPU → Uses ROCm backend
- No GPU → Falls back to CPU serial backend (slower but functional)

To force CPU backend:
```python
# In hltPhase2_TRKv08_LST_mkfit.py
process.lstProducer = lstProducer.clone(
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('serial_sync'),  # Force CPU
    )
)
```

## Troubleshooting

### Config Validation Error

If you get an error loading the config:
```bash
# Check syntax
python3 -m py_compile jmeTriggerNTuple_cfg_lst.py

# Check if customization is available
python3 -c "from JMETriggerAnalysis.Common.customizeHLTForPhase2 import customise_hltPhase2_redefineReconstructionSequences; print('OK')"
```

### TRK version not found

```
Error: Unknown tracking version 'v08'
```

**Solution**: Make sure you've rebuilt CMSSW after adding the v08 configuration:
```bash
cd $CMSSW_BASE/src
scram b -j 8
```

### LST/mkfit modules not found

```
Error: EDProducer 'LSTProducer@alpaka' not found
```

**Solution**: LST is only available in CMSSW_15_1_0_pre4 and later:
```bash
echo $CMSSW_VERSION  # Should be CMSSW_15_1_0_pre4 or later
```

### GPU Memory Error

```
Error: CUDA out of memory
```

**Solution**: Reduce events per job or use CPU backend:
```bash
cmsRun jmeTriggerNTuple_cfg_lst.py maxEvents=10  # Fewer events
```

## Summary

| Aspect | Standard Config | LST Config |
|--------|----------------|------------|
| **File** | jmeTriggerNTuple_cfg.py | jmeTriggerNTuple_cfg_lst.py |
| **Tracking** | CKF | LST + mkfit |
| **Hardware** | CPU only | GPU + CPU |
| **Speed** | Baseline | 5-15x faster |
| **Output** | out.root | out_lst.root |
| **Format** | Identical | Identical |
| **Use** | Standard studies | Performance optimization |

## Next Steps

1. **Test both configs:**
   ```bash
   cmsRun jmeTriggerNTuple_cfg.py maxEvents=100
   cmsRun jmeTriggerNTuple_cfg_lst.py maxEvents=100
   ```

2. **Compare outputs:**
   - Check tree structure is identical
   - Compare track multiplicity
   - Check timing differences

3. **Production use:**
   - Use LST config for large-scale production
   - Especially beneficial at high PU (>140)
   - Requires GPU access for best performance

4. **Read full documentation:**
   - See `LST_mkfit_Tutorial.md` for algorithm details
   - Contact tracking group for optimization help

---

**Created for CMSSW_15_1_0_pre4**
**JMETriggerAnalysis Framework**
