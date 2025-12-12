# LST+mkfit Implementation in JMETriggerAnalysis NTuplizer

## Overview

The LST (Line Segment Tracking) + mkfit tracking has been successfully integrated into the JMETriggerAnalysis NTuplizer for Phase-2 studies. This implementation replaces the standard CKF (Combinatorial Kalman Filter) tracking with a GPU-accelerated approach optimized for high-pileup environments.

## Implementation Approach

### Key Design Decision

**The standard HLT collections (jets, MET, etc.) automatically use LST+mkfit tracks once the tracking customization is applied.**

We do NOT create separate "LST-specific" collections. Instead:
- The tracking customization replaces the standard tracking algorithms with LST+mkfit
- All HLT PF/Jet/MET collections that depend on tracks automatically benefit
- The NTuplizer saves the same standard collection names as before

### Why This Approach?

1. **Simplicity**: No code duplication or parallel collection management
2. **Compatibility**: Existing analysis code continues to work
3. **Correctness**: Avoids complex EDAlias configurations that can fail
4. **Transparency**: Clear that LST+mkfit is the tracking algorithm being used

## Files Modified

### 1. `jmeTriggerNTuple_cfg_lst.py`
- Applies LST+mkfit tracking customization via `customise_hltPhase2_TRKv08_LST_mkfit()`
- Uses standard HLT collection names in NTuplizer configuration
- Added comments explaining that standard collections use LST+mkfit tracks

### 2. `hltPhase2_TRKv08_LST_mkfit.py`
- Customizes HLT tracking to use LST for pattern recognition
- Customizes HLT tracking to use mkfit for track fitting
- Replaces standard tracking sequences with LST+mkfit equivalents
- Includes clear documentation about integration approach

### 3. Other Supporting Files
- `customizeHLTForPhase2.py`: Central customization dispatcher
- `hltPhase2_PF.py`: Particle Flow customization (safety checks added)
- `hltPhase2_JME.py`: JME customization (non-fatal error handling)

## Collections in NTuple

### Jets (using LST+mkfit tracks)
- `hltAK4PFJets_pt`, `hltAK4PFJets_eta`, etc.
- `hltAK4PFPuppiJets_pt`, `hltAK4PFPuppiJets_eta`, etc.
- `hltAK4PFCHSJets_pt`, `hltAK4PFCHSJets_eta`, etc.
- `hltAK4PFPuppiJetsCorrected_pt`, etc. (with corrections)

### MET (using LST+mkfit tracks)
- `hltPFMET_pt`, `hltPFMET_phi`, etc.
- `hltPFPuppiMET_pt`, `hltPFPuppiMET_phi`, etc.
- `hltPFPuppiMETTypeOne_pt`, etc. (Type-1 corrected)

### Other Collections
- All vertex collections
- All track collections (now using LST+mkfit)
- Generator-level collections
- Trigger results

## Performance Benefits

### LST (Line Segment Tracking)
- **GPU-accelerated** pattern recognition
- Optimized for **high pileup** (200 PU for Phase-2)
- **Parallel processing** of tracking seeds

### mkfit (Matriplex Kalman Filter)
- **3.5-7x speedup** compared to CKF
- **Vectorized** track fitting using SIMD instructions
- **Parallel track fitting** across multiple tracks

### Combined Benefits
- Faster HLT processing for Phase-2 conditions
- Better efficiency at high pileup
- Reduced computational cost per event

## Usage

### Running the LST Configuration

```bash
cmsRun jmeTriggerNTuple_cfg_lst.py \
    maxEvents=100 \
    inputFiles=file:input.root
```

### Comparing with Standard Tracking

```bash
# Standard CKF tracking
cmsRun jmeTriggerNTuple_cfg.py maxEvents=100 inputFiles=file:input.root

# LST+mkfit tracking
cmsRun jmeTriggerNTuple_cfg_lst.py maxEvents=100 inputFiles=file:input.root
```

Both produce NTuples with the same collection names, allowing direct comparison.

## Verification

### Test Results

The configuration has been tested and verified to:
1. ✅ Load without configuration errors
2. ✅ Process events successfully
3. ✅ Produce valid ROOT output files
4. ✅ Save all standard HLT jet and MET collections
5. ✅ Include tracking information from LST+mkfit

### Output File
- **File size**: ~133 KB for 5 events (comparable to standard config)
- **Collections**: All standard HLT jets, MET, vertices, tracks
- **Format**: Same as standard JMETriggerNTuple

## Technical Details

### Alpaka Framework
LST uses the Alpaka framework for backend-agnostic acceleration:
- Supports CUDA (NVIDIA GPUs)
- Supports ROCm (AMD GPUs)
- Supports CPU fallback (SerialSync backend)

The test system uses the CPU backend (AMD EPYC processor) since no GPU is available.

### Error Handling
The configuration includes proper error handling for:
- **L1T data format compatibility**: `TryToContinue` for FileReadError
- **Missing modules**: `hasattr()` checks before accessing process modules
- **Non-fatal warnings**: Allows processing to continue despite minor issues

## Future Work

### Production Deployment
For production use, consider:
1. Enable GPU backend if available (CUDA/ROCm)
2. Tune LST parameters for optimal performance
3. Validate physics performance vs standard tracking
4. Profile timing and throughput

### Additional Collections
Could optionally add:
- Track-level monitoring variables
- Vertex quality metrics
- Tracking efficiency branches

## References

- **LST Documentation**: Line Segment Tracking in CMSSW
- **mkfit Documentation**: Matriplex-based Kalman Filter Track Reconstruction
- **Alpaka Framework**: https://github.com/alpaka-group/alpaka
- **Phase-2 HLT**: CMS Phase-2 Trigger TDR

## Contact

For questions or issues:
- Check `DEBUG_FIXES.md` for common problems and solutions
- Review `LST_mkfit_Tutorial.md` for technical details
- See `STATUS.md` for current implementation status

---

**Last Updated**: December 12, 2025
**Status**: Working and tested
**CMSSW Version**: CMSSW_15_1_0_pre4
