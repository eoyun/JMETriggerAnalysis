#!/bin/bash
set -e

# configuration
TOTAL_EVENTS=10000
STEP=5
OUTDIR=260114

mkdir -p ${OUTDIR}

for (( SKIP=885; SKIP<${TOTAL_EVENTS}; SKIP+=${STEP} )); do
    IDX=$(printf "%05d" ${SKIP})

    echo "=== Processing events ${SKIP} -> $((SKIP+STEP-1)) ==="

    # L1 step
    cmsRun jmeTriggerNTuple_L1Only_cfg.py \
        maxEvents=${STEP} \
        skipEvents=${SKIP} \
        output=L1_output_${IDX}.root

    # HLT steps
    cmsRun jmeTriggerNTuple_cfg.py track=LST    inputFiles=file:L1_output_${IDX}.root output=${OUTDIR}/out_LST_${IDX}.root
    cmsRun jmeTriggerNTuple_cfg.py track=MkFit  inputFiles=file:L1_output_${IDX}.root output=${OUTDIR}/out_MkFit_${IDX}.root
    cmsRun jmeTriggerNTuple_cfg.py track=both   inputFiles=file:L1_output_${IDX}.root output=${OUTDIR}/out_both_${IDX}.root
    cmsRun jmeTriggerNTuple_cfg.py track=menu   inputFiles=file:L1_output_${IDX}.root output=${OUTDIR}/out_menu_${IDX}.root
    cmsRun jmeTriggerNTuple_cfg.py              inputFiles=file:L1_output_${IDX}.root output=${OUTDIR}/out_default_${IDX}.root

    # cleanup large intermediate files
    rm -f Phase2*HLT.root
    rm -f L1_output_${IDX}.root
done
