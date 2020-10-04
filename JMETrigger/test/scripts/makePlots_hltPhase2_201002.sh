#!/bin/bash

set -e

if [ ! -d ${JMEANA_BASE} ]; then
  printf "%s\n" "environment variable JMEANA_BASE does not contain a valid directory: JMEANA_BASE=${JMEANA_BASE}"
  exit 1
fi

tar_output=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tar) tar_output=1; shift;;
  esac
done

inpdir=${JMEANA_BASE}/output_hltPhase2_201002
outdir=plots_hltPhase2_201002

samples=(
# Phase2HLTTDR_QCD_Pt_15to3000_Flat_14TeV_NoPU
  Phase2HLTTDR_QCD_Pt_15to3000_Flat_14TeV_PU200
# Phase2HLTTDR_VBF_HToInvisible_14TeV_NoPU
  Phase2HLTTDR_VBF_HToInvisible_14TeV_PU200
)

exts=(
  pdf
  png
# root
)

outdirbase=${outdir%%/*}

if [ ${tar_output} -gt 0 ] && [ -f ${outdirbase}.tar.gz ]; then
  printf "%s\n" ">> target output file already exists: ${outdirbase}.tar.gz"
  exit 1
fi

if [ -d ${outdirbase} ]; then
  printf "%s\n" ">> target output directory already exists: ${outdirbase}"
  exit 1
fi

for sample in "${samples[@]}"; do

  outd_i=${outdir}/${sample}

  if [[ ${sample} == "Phase2HLTTDR_QCD_Pt_15to3000_Flat_14TeV_"* ]]; then

    jmePlots.py -k phase2_dqm_compareTRK \
      -o ${outd_i}/dqm_compareTRK_withoutTICL -l ${sample} -e ${exts[*]} -i \
      ${inpdir}/ntuples/HLT_TRKv06/${sample}.root:'TRK-v6':880:1:25 \
      ${inpdir}/ntuples/HLT_TRKv07p2/${sample}.root:'TRK-v7.2':801:1:26

#    jmePlots.py -k phase2_dqm_compareTRK -m 'PFCandidateHistograms_*' \
#      -o ${outd_i}/dqm_compareTRK_withTICL -l ${sample} -e ${exts[*]} -i \
#      ${inpdir}/ntuples/HLT_TRKv06_TICL/${sample}.root:'TRK-v6 + TICL':880:1:25 \
#      ${inpdir}/ntuples/HLT_TRKv07p2_TICL/${sample}.root:'TRK-v7.2 + TICL':801:1:26
#
#    jmePlots.py -k phase2_dqm_compareTRK2 \
#      -o ${outd_i}/dqm_compareTICL_withTRKv06 -l ${sample} -e ${exts[*]} -i \
#      ${inpdir}/ntuples/HLT_TRKv06/${sample}.root:'TRK-v6':1:1:20 \
#      ${inpdir}/ntuples/HLT_TRKv06_TICL/${sample}.root:'TRK-v6 + TICL':1:2:20
#
#    jmePlots.py -k phase2_dqm_compareTRK2 \
#      -o ${outd_i}/dqm_compareTICL_withTRKv07p2 -l ${sample} -e ${exts[*]} -i \
#      ${inpdir}/ntuples/HLT_TRKv07p2/${sample}.root:'TRK-v7.2':1:1:20 \
#      ${inpdir}/ntuples/HLT_TRKv07p2_TICL/${sample}.root:'TRK-v7.2 + TICL':1:2:20
  fi

  continue

  opts_i=""
  if   [[ ${sample} == *"QCD_"* ]]; then opts_i="-m 'NoSel*/*JetsCorr*' 'NoSel*/*MET_*' 'NoSel*/*/offline*MET*_pt' -s '*MET*GEN*'"
  elif [[ ${sample} == *"HToInv"* ]]; then opts_i="-m 'NoSel*/*MET_*' 'NoSel*/*/offline*METs*_pt'"
  fi

  jmePlots.py -k jme_compare ${opts_i} \
    -o ${outd_i}/compareTRK_withoutTICL -l ${sample} -e ${exts[*]} -i \
    ${inpdir}/harvesting/HLT_TRKv06/${sample}.root:'TRK-v6':1:1:20 \
    ${inpdir}/harvesting/HLT_TRKv07p2/${sample}.root:'TRK-v7.2':2:1:33 \

  jmePlots.py -k jme_compare ${opts_i} \
    -o ${outd_i}/compareTRK_withTICL -l ${sample} -e ${exts[*]} -i \
    ${inpdir}/harvesting/HLT_TRKv06_TICL/${sample}.root:'TRK-v6 + TICL':4:1:24 \
    ${inpdir}/harvesting/HLT_TRKv07p2_TICL/${sample}.root:'TRK-v7.2 + TICL':801:1:27

  jmePlots.py -k jme_compare ${opts_i} \
    -o ${outd_i}/compareTRKandTICL -l ${sample} -e ${exts[*]} -i \
    ${inpdir}/harvesting/HLT_TRKv06/${sample}.root:'TRK-v6':1:1:20 \
    ${inpdir}/harvesting/HLT_TRKv06_TICL/${sample}.root:'TRK-v6 + TICL':4:1:24 \
    ${inpdir}/harvesting/HLT_TRKv07p2/${sample}.root:'TRK-v7.2':2:1:33 \
    ${inpdir}/harvesting/HLT_TRKv07p2_TICL/${sample}.root:'TRK-v7.2 + TICL':801:1:27

  unset outd_i opts_i
done
unset sample

if [ ${tar_output} -gt 0 ] && [ -d ${outdirbase} ]; then
  tar cfz ${outdirbase}.tar.gz ${outdirbase}
  rm -rf ${outdirbase}
fi

unset inpdir outdir samples exts outdirbase tar_output
