# JME Trigger Analysis - NTuple Analysis Tools

## Overview

This toolkit provides a complete workflow for analyzing Jet/MET (JME) trigger performance using "flat" ROOT NTuples produced from CRAB3 jobs. The analysis pipeline consists of:

1. **Preparation**: Merging NTuples from distributed storage
2. **Analysis**: Running analysis on batch systems (HTCondor/SGE)
3. **Harvesting**: Post-processing histograms to create efficiency curves, profiles, etc.
4. **Plotting**: Creating publication-quality performance plots

---

## Requirements

- CMSSW environment (Phase2 or Run3)
- Python 3 for batch management scripts
- Python 2 for legacy plotting scripts (some scripts still use Python 2 syntax)
- Access to batch system (HTCondor or SGE)
- ROOT with Python bindings

---

## Initial Setup

### 1. Environment Configuration

Before running any analysis, set up the environment variables:

```bash
source env.sh
```

**What this does:**
- Sets `JMEANA_BASE` to the current directory
- Adds scripts to `PATH` so they can be run from anywhere
- Configures Python paths for the common utilities
- Disables Python bytecode generation

**Verification:**
```bash
echo $JMEANA_BASE  # Should show current directory path
```

---

## Complete Analysis Workflow

### Step 1: Prepare Analysis NTuples

**Script:** `hadd_ntuples.py`

**Purpose:** Merge ROOT files from multiple CRAB3 task output directories into consolidated NTuples.

**Basic Usage:**
```bash
hadd_ntuples.py -i [INPUT_DIRS] -o [OUTPUT_DIR] -l 0 -s DQM
```

**Detailed Example:**
```bash
hadd_ntuples.py \
  -i /eos/cms/store/user/username/task1/ /eos/cms/store/user/username/task2/ \
  -o ${HOME}/analysis/ntuples \
  -s DQM failed \
  -l 0 \
  -v 1
```

**Key Parameters:**
- `-i, --inputs`: List of CRAB3 output directories (can specify multiple)
- `-o, --output`: Output directory where merged files will be stored
- `-s, --skip`: Keywords to skip files (e.g., "DQM" skips DQM files, "failed" skips failed jobs)
- `-l, --level`: Directory depth level for organizing outputs (0 = flat structure)
- `-p, --postfix`: Optional postfix for output file names
- `-v, --verbosity`: Verbosity level (0=quiet, 1=normal, 2=debug)
- `-d, --dry-run`: Test run without actually merging files

**Output:**
- Merged ROOT files in `OUTPUT_DIR`, one file per CRAB3 task

**Tips:**
- Use `-s DQM` to skip DQM monitor files if you only need analysis NTuples
- Use `-d` first to preview what will be merged before running the actual merge
- For large datasets, this step may take significant time

---

### Step 2: Submit Analysis Jobs to Batch System

**Script:** `batch_driver.py`

**Purpose:** Create and optionally submit batch jobs that run your analysis on the merged NTuples.

**Basic Usage:**
```bash
batch_driver.py \
  -i ${NTUDIR}/*.root \
  -o ${OUTDIR}/jobs \
  -od /eos/user/x/username/outputs \
  -n 50000 \
  -l 0
```

**Detailed Example with Submission:**
```bash
batch_driver.py \
  -i /afs/cern.ch/work/u/user/ntuples/*.root \
  -o ${HOME}/analysis/batch_jobs \
  -od /eos/user/u/user/analysis/outputs \
  -n 50000 \
  -t Events \
  -p jetmet_analysis \
  --batch htc \
  --JobFlavour longlunch \
  --submit \
  -l 0 \
  -v
```

**Key Parameters:**

**Required:**
- `-i, --inputs`: Input ROOT files containing TTrees (use wildcards)
- `-o, --output`: Local directory for batch job scripts and logs
- `-od, --outputdir`: EOS directory where job outputs will be stored
- `-n, --nperjob`: Number of events processed per batch job (smaller = more parallel jobs)

**Optional:**
- `-s, --script`: Custom Python script to run (default: auto-detected)
- `-t, --tree-name`: Name of TTree in input files (default: "Events")
- `-p, --plugin`: Analysis plugin name to use
- `--batch`: Batch system type: `htc` (HTCondor, default) or `sge` (Sun Grid Engine)
- `--JobFlavour`: HTCondor job duration category
  - `espresso`: 20 minutes
  - `microcentury`: 1 hour
  - `longlunch`: 2 hours
  - `workday`: 8 hours
  - `tomorrow`: 1 day
  - `testmatch`: 3 days
  - `nextweek`: 1 week
- `--AccountingGroup`: HTCondor accounting group for resource allocation
- `--time`: Maximum runtime in seconds (alternative to JobFlavour)
- `--submit`: Actually submit jobs to batch system (without this, only creates scripts)
- `-l, --level`: Output directory depth level
- `-v, --verbose`: Enable detailed output
- `-d, --dry-run`: Create scripts without submitting

**Output:**
- Batch submission scripts (`.htc` for HTCondor, `.sh` for SGE)
- Log files directory structure
- Configuration files for each job

**Workflow Tips:**
1. First run **without** `--submit` to create scripts and verify setup
2. Check a few `.htc` files to ensure paths and commands are correct
3. Add `--submit` to actually submit to the batch system

**Choosing Event Splitting (`-n`):**
- Smaller values (10000-50000): More parallel jobs, faster completion, higher overhead
- Larger values (100000+): Fewer jobs, less overhead, but individual jobs take longer
- Recommended: 50000 events for balanced performance

---

### Step 3: Monitor and Manage Batch Jobs

**Script:** `batch_monitor.py`

**Purpose:** Monitor job status, identify failures, and automatically resubmit failed/stuck jobs.

**Basic Monitoring (No Resubmission):**
```bash
batch_monitor.py -i ${OUTDIR}/jobs
```

**Active Monitoring with Resubmission:**
```bash
batch_monitor.py \
  -i ${OUTDIR}/jobs \
  -r \
  --repeat -1 \
  -f 300 \
  --check-root \
  -v
```

**Detailed Example:**
```bash
batch_monitor.py \
  -i ${HOME}/analysis/batch_jobs \
  --batch htc \
  -r \
  --repeat -1 \
  -f 600 \
  --check-err \
  --check-log \
  --check-root \
  --jobflavour longlunch \
  -j 5000 \
  -v
```

**Key Parameters:**

**Required:**
- `-i, --inputs`: Directory containing batch job scripts (same as `-o` from batch_driver.py)

**Monitoring Options:**
- `--batch`: Batch system type (`htc` or `sge`)
- `-r, --resubmit`: Enable automatic resubmission of failed jobs
- `--repeat`: Number of monitoring cycles (-1 = infinite, run until all complete)
- `-f, --frequency`: Time between monitoring cycles in seconds (default: 60)

**Job Validation:**
- `--check-err`: Resubmit if error file is not empty
- `--check-log`: Resubmit if log contains "abort" or error keywords
- `--check-root`: Validate ROOT file integrity before marking job complete

**Resubmission Control:**
- `--jobflavour`: Job duration category for resubmitted jobs
- `-t, --job-maxtime`: Maximum runtime for resubmitted jobs (seconds)
- `-j, --jobs-max`: Maximum number of jobs in queue simultaneously
- `--skip`: List of job IDs to ignore (e.g., `--skip 42 137`)

**Other Options:**
- `-l, --local`: Run jobs locally instead of batch system (for debugging)
- `-v, --verbose`: Detailed status output
- `-d, --dry-run`: Show what would be done without actually resubmitting

**How Job Completion is Tracked:**
- The monitor looks for `.completed` files for each job
- A job is considered complete when `jobname.completed` exists
- Jobs without `.completed` and not running are candidates for resubmission

**Typical Monitoring Workflow:**

1. **Initial check** (no resubmission):
   ```bash
   batch_monitor.py -i ${OUTDIR}/jobs -v
   ```
   Review the status summary

2. **Active monitoring** with automatic resubmission:
   ```bash
   batch_monitor.py -i ${OUTDIR}/jobs -r --repeat -1 -f 600 --check-root
   ```
   Runs every 10 minutes, validates outputs, resubmits failures

3. **Final check** after completion:
   ```bash
   batch_monitor.py -i ${OUTDIR}/jobs --check-root -v
   ```
   Verify all jobs completed successfully

**Status Output Interpretation:**
- **Completed**: Job finished, `.completed` file exists
- **Running**: Job currently in batch queue
- **Failed**: Job error detected or no output
- **Pending**: Job script exists but not submitted

---

### Step 4: Merge Batch Job Outputs

**Script:** `merge_batchOutputs.py`

**Purpose:** Merge all individual ROOT files from batch jobs into consolidated files for further processing.

**Basic Usage:**
```bash
merge_batchOutputs.py \
  -i ${OUTDIR}/jobs/*.root \
  -o ${OUTDIR}/merged \
  -l 0
```

**Detailed Example:**
```bash
merge_batchOutputs.py \
  -i /eos/user/u/user/analysis/outputs/*.root \
  -o ${HOME}/analysis/merged_outputs \
  -l 1 \
  -v
```

**Key Parameters:**
- `-i, --inputs`: Input ROOT files from batch jobs (supports wildcards)
- `-o, --output`: Output directory for merged files
- `-l, --level`: Directory depth level for output organization
  - `0`: All files in single directory
  - `1`: Create subdirectories by sample/category
  - `2+`: Additional hierarchical levels
- `-v, --verbose`: Enable detailed logging
- `-d, --dry-run`: Preview merge operations without executing

**Output:**
- Merged ROOT files organized by directory level
- Maintains histogram structure from individual jobs

**Memory Considerations:**
- For very large datasets, merging may require substantial memory
- Consider merging in stages if you encounter memory issues

---

### Step 5: Harvest Analysis Products

**Script:** `jmeAnalysisHarvester.py`

**Purpose:** Post-process merged histograms to create derived products like efficiency curves, profile histograms, resolution plots, and trigger turn-on curves.

**Basic Usage:**
```bash
jmeAnalysisHarvester.py \
  -i ${OUTDIR}/merged/*.root \
  -o ${OUTDIR}/harvested \
  -l 0
```

**Detailed Example:**
```bash
jmeAnalysisHarvester.py \
  -i ${HOME}/analysis/merged_outputs/*.root \
  -o ${HOME}/analysis/harvested \
  -s "_vs_" \
  -l 0 \
  -v
```

**Key Parameters:**
- `-i, --inputs`: Merged ROOT files from previous step
- `-o, --output`: Output directory (multiple inputs) or file (single input)
- `-s, --separator-2d`: String separator in 2D histogram names (default: "_vs_")
  - Used to identify and create profile histograms from 2D plots
  - Example: Histogram named `pt_vs_eta` with separator `_vs_` creates profile
- `-l, --level`: Output directory organization level
- `--copy-only`: Only copy existing objects without creating new derived products
- `-v, --verbose`: Enable detailed logging
- `-d, --dry-run`: Preview operations without creating files

**What Harvesting Does:**
1. **Profile Creation**: Converts 2D histograms to profile plots
   - Identifies 2D histograms using separator string
   - Creates mean and RMS profiles along each axis
2. **Efficiency Calculation**: Creates efficiency curves from pass/fail histograms
3. **Resolution Plots**: Computes resolution from response distributions
4. **Trigger Turn-ons**: Generates trigger efficiency vs. threshold plots

**Output:**
- ROOT files with original histograms plus derived products
- Profile histograms (mean, RMS)
- Efficiency curves (TEfficiency objects)
- Resolution plots

**Example Use Cases:**
- **Trigger efficiency**: Pass histograms → efficiency vs. pT
- **Jet response**: 2D (true pT, measured pT) → profile plots → resolution
- **Turn-on curves**: Pass/total histograms → sigmoid efficiency curves

---

## Plotting and Visualization

### Available Plotting Scripts

After harvesting, various specialized plotting scripts create publication-quality figures:

#### 1. **Phase 2 Trigger Plots**
```bash
./plot_hltPhase2TDR.py -i ${OUTDIR}/harvested/*.root -o ${OUTDIR}/plots
```
- Creates comprehensive plots for Phase 2 Trigger TDR
- Includes jet/MET performance, trigger efficiency, rates

#### 2. **General JME Plots**
```bash
./jmePlots_phase2.py -i ${OUTDIR}/harvested/*.root
```
- Standard JME performance plots for Phase 2
- Can be customized for different objects and selections

#### 3. **Rate and Efficiency Plots**
```bash
./plotJMERatesAndEffs.py --input ${OUTDIR}/harvested/file.root --output plots/
```
- Specialized for trigger rate and efficiency studies
- Includes rate vs. pT threshold, efficiency turn-ons

#### 4. **Comparison Plots**
- `jmePlots_compare.py`: Compare different configurations
- `jmePlots_compareFiles.py`: Compare different input files
- `jmePlots_compareObjs.py`: Compare specific objects

**Note:** Many plotting scripts use Python 2 syntax. If you encounter syntax errors with Python 3, try using a Python 2 environment or CMSSW's Python 2.

---

## Complete Example Workflow

### Scenario: Analyze Phase 2 VBF Invisible trigger performance

```bash
# 1. Setup environment
cd /path/to/JMETriggerAnalysis/NTupleAnalysis/test
source env.sh

# 2. Prepare NTuples from CRAB outputs
hadd_ntuples.py \
  -i /eos/cms/store/user/myuser/VBFInv_Phase2_v1/ \
  -o ${HOME}/vbfinv_analysis/ntuples \
  -s DQM \
  -l 0 \
  -v 1

# 3. Submit batch jobs (50k events each)
batch_driver.py \
  -i ${HOME}/vbfinv_analysis/ntuples/*.root \
  -o ${HOME}/vbfinv_analysis/jobs \
  -od /eos/user/m/myuser/vbfinv_outputs \
  -n 50000 \
  --batch htc \
  --JobFlavour workday \
  --submit \
  -l 0

# 4. Monitor jobs (continuous, check every 10 min)
batch_monitor.py \
  -i ${HOME}/vbfinv_analysis/jobs \
  -r \
  --repeat -1 \
  -f 600 \
  --check-root \
  -v

# 5. After jobs complete, merge outputs
merge_batchOutputs.py \
  -i /eos/user/m/myuser/vbfinv_outputs/*.root \
  -o ${HOME}/vbfinv_analysis/merged \
  -l 0 \
  -v

# 6. Harvest to create efficiencies and profiles
jmeAnalysisHarvester.py \
  -i ${HOME}/vbfinv_analysis/merged/*.root \
  -o ${HOME}/vbfinv_analysis/harvested \
  -s "_vs_" \
  -l 0 \
  -v

# 7. Create plots
./plot_hltPhase2TDR.py \
  -i ${HOME}/vbfinv_analysis/harvested/*.root \
  -o ${HOME}/vbfinv_analysis/plots
```

---

## Common Issues and Troubleshooting

### Issue: "Python not found"
**Solution:** Use `python3` explicitly or ensure Python is in your PATH via CMSSW environment.

### Issue: Syntax errors in plotting scripts
**Cause:** Some plotting scripts use Python 2 syntax
**Solution:**
```bash
cmsenv  # Use CMSSW's Python 2
python plot_script.py
```

### Issue: Jobs failing silently
**Solution:** Use `--check-err --check-log --check-root` with batch_monitor.py to detect failures

### Issue: Out of memory during merge
**Solution:**
- Reduce number of files merged at once
- Use higher-memory batch jobs
- Merge in multiple stages

### Issue: Missing .completed files
**Cause:** Jobs crashed before completion marker created
**Solution:** Use `batch_monitor.py -r --check-root` to validate outputs and resubmit

### Issue: Harvester creates unexpected objects
**Solution:** Check `-s` separator string matches your 2D histogram naming convention

---

## Expected Output File Structure

The following is based on actually running each step against a real input file (`260114.root`, 2460 events). File names follow the pattern `<inputfile>__<jobindex>` for per-job outputs.

---

### Step 1 output — `hadd_ntuples.py` → input NTuple

```
ntuples/
└── 260114.root
```

**Internal ROOT structure:**
```
260114.root
└── JMETriggerNTuple/          [TDirectoryFile]
    └── Events                 [TTree, 184 branches]
```

**Branch groups in `Events`:**

| Group | Example branches | Type |
|-------|-----------------|------|
| Event ID | `run`, `luminosityBlock`, `event` | `/i`, `/i`, `/l` |
| Generator info | `HepMCGenEvent_scale`, `GenEventInfo_qScale` | `/F` |
| Pileup (BX=0) | `pileupInfo_BX0_numPUInteractions`, `pileupInfo_BX0_numTrueInteractions`, `pileupInfo_BX0_n_pThat*` (10 bins) | `/I`, `/F`, `/i` |
| HLT trigger flags | `MC_JME`, `HLT_AK4PFPuppiJet520`, `HLT_PFPuppiHT1070`, `HLT_PFPuppiMETTypeOne140_PFPuppiMHT140` | `/O` (bool) |
| Rho + vertices | `fixedGridRhoFastjetAllTmp`, `hltPrimaryVerticesMultiplicity`, `hltPrimaryVertices_{x,y,z,chi2,ndof,...}` | `/D`, vector |
| Gen jets AK4 | `ak4GenJetsNoNu_{pt,eta,phi,mass,energy fractions,multiplicities,...}` | vector |
| Gen jets AK8 | `ak8GenJetsNoNu_{pt,eta,phi,mass,energy fractions,multiplicities,...}` | vector |
| HLT jets (4 collections) | `hltAK4PFCHSJets_*`, `hltAK4PFJets_*`, `hltAK4PFPuppiJets_*`, `hltAK4PFPuppiJetsCorrected_*` — each with `{energy,pt,eta,phi,mass,jesc,jetArea,energy fractions,multiplicities}` | vector |
| Gen MET | `genMETTrue_{pt,phi,sumEt,energy fractions}` | `/F` |
| HLT MET (4 collections) | `hltCaloMET_*`, `hltPFMET_*`, `hltPFPuppiMET_*`, `hltPFPuppiMETTypeOne_*` — each with `{pt,phi,sumEt,energy fractions}` | `/F` |

---

### Step 2 output — `batch_driver.py` → job scripts

One `.sh` + `.htc` pair is created per event-chunk per input file. With `-n 50000` and 2460 events, one chunk is created (`__0`):

```
jobs/
├── htc/                                    [directory, created automatically]
│   ├── 260114__0.out.<Cluster>.<Process>   [stdout from HTCondor]
│   ├── 260114__0.err.<Cluster>.<Process>   [stderr from HTCondor]
│   └── 260114__0.log.<Cluster>.<Process>   [HTCondor system log]
├── 260114__0.sh                            [bash script run by HTCondor]
└── 260114__0.htc                           [HTCondor submission config]
```

**`260114__0.sh` content:**
```bash
#!/bin/bash
cd /path/to/CMSSW_16_0_0_pre3/src
eval `scramv1 runtime -sh`
cd - &> /dev/null

set -e
if [ -f /eos/.../260114__0.root ]; then rm -f /eos/.../260114__0.root; fi;
run.py -i ntuples/260114.root -o /eos/.../260114__0.root \
  -p JMETriggerAnalysisDriverPhase2 --skipEvents 0 --maxEvents 2460
touch jobs/260114__0.completed
```

**`260114__0.htc` content:**
```
batch_name = 260114__0
executable = /abs/path/jobs/260114__0.sh
output = jobs/htc/260114__0.out.$(Cluster).$(Process)
error  = jobs/htc/260114__0.err.$(Cluster).$(Process)
log    = jobs/htc/260114__0.log.$(Cluster).$(Process)
transfer_executable = True
universe = vanilla
getenv = True
should_transfer_files   = IF_NEEDED
when_to_transfer_output = ON_EXIT
MY.WantOS = "el8"
RequestMemory = 2000
+MaxRuntime = 10800
queue
```

---

### Step 3 — `batch_monitor.py` + job execution → per-job ROOT output + `.completed`

After the job runs successfully:

```
jobs/
├── htc/
│   ├── 260114__0.out.12345.0   [stdout]
│   ├── 260114__0.err.12345.0   [stderr — empty if no errors]
│   └── 260114__0.log.12345.0   [HTCondor log]
├── 260114__0.sh
├── 260114__0.htc
└── 260114__0.completed         [empty file, created by touch on job success]
```

The actual analysis ROOT output goes to the EOS directory (`-od`):

```
eos_outputs/
└── 260114__0.root
```

**Internal ROOT structure of `260114__0.root` (produced by `run.py`):**
```
260114__0.root
├── eventsProcessed    [TH1D — single bin, stores number of processed events]
├── weight             [TH1D — event weight distribution]
└── NoSelection/       [TDirectoryFile — 10,861 histogram objects total]
    ├── ak4GenJetsNoNu_*           (6,669 objects: TH1D + TH2D)
    ├── genMETTrue_*               (   13 objects: TH1D + TH2D + TH3D)
    ├── hltAK4PFJets_*             (1,349 objects: TH1D + TH2D)
    ├── hltAK4PFJetsCorrected_*    (    1 object:  TH2D)
    ├── hltAK4PFPuppiJets_*        (1,349 objects: TH1D + TH2D)
    ├── hltAK4PFPuppiJetsCorrected_* (1,350 objects: TH1D + TH2D)
    ├── hltPFMET_*                 (   39 objects: TH1D + TH2D)
    ├── hltPFPuppiHT_*             (    6 objects: TH1D + TH2D)
    ├── hltPFPuppiMET_*            (   39 objects: TH1D + TH2D)
    ├── hltPFPuppiMETTypeOne_*     (   43 objects: TH1D + TH2D)
    └── l1tPFPuppiHT_*             (    3 objects: TH1D)
```

**Histogram naming convention inside `NoSelection/`:**

| Pattern | Example | Description |
|---------|---------|-------------|
| `<obj>_<etabin>_<var>` | `ak4GenJetsNoNu_EtaIncl_pt` | 1D distribution |
| `<obj>_<etabin>_<var>__vs__<var2>` | `ak4GenJetsNoNu_EtaIncl_pt__vs__hltPF_pt` | 2D response/correlation |
| `<obj>_<etabin>_MatchedTo<reco>_<var>` | `ak4GenJetsNoNu_EtaIncl_MatchedTohltPFPuppi_pt` | matched-object histogram |
| `<obj>_<etabin>_njets` | `hltAK4PFPuppiJets_EtaIncl_njets` | jet multiplicity |
| `<obj>_<etabin>_HT` | `hltAK4PFPuppiJets_EtaIncl_HT` | scalar HT sum |
| `<met>_pt__vs__<other>_pt` | `genMETTrue_pt__vs__hltPFPuppiMETTypeOne_pt` | MET vs MET 2D |

Eta bins used: `EtaIncl` (inclusive), `HBPt0`, `HEPt0`, `HFPt0`, etc.

---

### Step 4 output — `merge_batchOutputs.py` → merged ROOT file

With a single input chunk, the file is renamed (not truly merged):

```
merged/
└── 260114.root     [identical internal structure to step 3 output, 10,861 objects in NoSelection/]
```

With multiple chunks (`260114__0.root`, `260114__1.root`, ...), `hadd` merges them:
```
merged/
└── 260114.root     [histogram counts summed across all chunks]
```

---

### Step 5 output — `jmeAnalysisHarvester.py` → harvested ROOT file

```
harvested/
└── 260114.root
```

**What changes vs. step 4:**

The harvester transforms the histogram file:
- **Adds 2,535 new derived objects** from the 10,861 input objects
- **Removes intermediate source histograms** no longer needed after deriving
- **Net result: 9,146 objects** in `NoSelection/`

| New object type | Count | Naming pattern | Description |
|----------------|-------|---------------|-------------|
| `TGraphAsymmErrors` | 700 | `*_eff` | Efficiency curves (pass/total ratio with Clopper-Pearson errors) |
| `TH1D` | 1,660 | `*_cumul`, `*_Mean_wrt_*` | Cumulative distributions and mean-vs-variable profiles |
| `TH2D` | 175 | `*_eff` (2D) | 2D efficiency maps (eta vs pT) |

**Examples of newly added objects:**
```
NoSelection/
├── ak4GenJetsNoNu_EtaIncl_MatchedTohltPFPuppiCorr_pt_eff   [TGraphAsymmErrors — jet matching eff vs pT]
├── ak4GenJetsNoNu_EtaIncl_MatchedTohltPFPuppi_eta_eff       [TGraphAsymmErrors — jet matching eff vs eta]
├── ak4GenJetsNoNu_EtaIncl_pt0_cumul                         [TH1D — cumulative leading jet pT]
├── ak4GenJetsNoNu_EtaIncl_HT_cumul                          [TH1D — cumulative HT]
├── ak4GenJetsNoNu_EtaIncl_MatchedTohltPF_eta__vs__pt_eff    [TH2D — 2D matching eff]
└── hltPFPuppiMET_pt_Mean_wrt_GEN_pt                         [TH1D — mean MET response vs gen MET]
```

---

### Full Directory Layout (All Steps Together)

```
analysis/
│
├── ntuples/                            [Step 1: hadd_ntuples.py]
│   └── 260114.root                     TTree: JMETriggerNTuple/Events, 184 branches
│
├── jobs/                               [Step 2: batch_driver.py]
│   ├── htc/
│   │   ├── 260114__0.out.<C>.<P>       HTCondor stdout
│   │   ├── 260114__0.err.<C>.<P>       HTCondor stderr
│   │   └── 260114__0.log.<C>.<P>       HTCondor system log
│   ├── 260114__0.sh                    bash script (sets CMSSW env, runs run.py)
│   ├── 260114__0.htc                   HTCondor job config
│   └── 260114__0.completed             [Step 3] empty marker, created on job success
│
├── eos_outputs/                        [Step 3: run.py via HTCondor]
│   └── 260114__0.root                  TH1D/TH2D histograms in NoSelection/ (10,861 objects)
│
├── merged/                             [Step 4: merge_batchOutputs.py]
│   └── 260114.root                     same internal structure, chunks summed (10,861 objects)
│
├── harvested/                          [Step 5: jmeAnalysisHarvester.py]
│   └── 260114.root                     9,146 objects: original histos + 2,535 new
│                                       (TGraphAsymmErrors efficiencies, cumulative TH1D, 2D eff maps)
│
└── plots/                              [Step 6: plotting scripts]
    ├── jetPt_response.pdf
    ├── met_efficiency.pdf
    └── trigger_turnon.pdf
```

---

## Tips for Efficient Analysis

1. **Use dry-run mode** (`-d`) to test commands before executing
2. **Monitor batch jobs actively** with `--repeat -1` to catch failures early
3. **Validate ROOT files** using `--check-root` to avoid corrupted outputs
4. **Organize outputs** using `-l` parameter for complex multi-sample analyses
5. **Start small**: Test workflow on subset of data before full production
6. **Check logs**: Always review `.log` and `.err` files if jobs fail
7. **Backup critical outputs**: Harvested files are valuable, keep backups

---

## Additional Resources

- **Common utilities**: See `common/` directory for shared Python modules
  - `efficiency.py`: Efficiency calculation helpers
  - `plot.py`: Plotting utilities
  - `th1.py`: TH1 histogram wrappers
  - `utils.py`: General utilities

- **Test scripts**: See `test/` directory for examples and validation scripts

- **Legacy scripts**: See `old/` directory for deprecated versions

---

## Script Reference Summary

| Script | Purpose | Key Options |
|--------|---------|-------------|
| `hadd_ntuples.py` | Merge CRAB outputs | `-i` input dirs, `-o` output, `-s` skip keywords |
| `batch_driver.py` | Create/submit batch jobs | `-i` inputs, `-o` job dir, `-n` events/job, `--submit` |
| `batch_monitor.py` | Monitor/resubmit jobs | `-i` job dir, `-r` resubmit, `--repeat`, `--check-root` |
| `merge_batchOutputs.py` | Merge batch outputs | `-i` input files, `-o` output dir |
| `jmeAnalysisHarvester.py` | Create efficiencies/profiles | `-i` inputs, `-o` output, `-s` separator |
| `plot_hltPhase2TDR.py` | Phase 2 TDR plots | `-i` harvested files, `-o` plot dir |
| `jmePlots_phase2.py` | General Phase 2 plots | `-i` harvested files |

---

## Getting Help

For script-specific help, run:
```bash
python3 script_name.py --help
```

For issues or questions:
- Check log files in job directories
- Review error messages in `.err` files
- Consult CMSSW documentation for ROOT/Python integration
- Contact package maintainers

---

**Last Updated:** 2026-04-10
**CMSSW Version:** 16_0_0_pre3
**Branch:** master_phase2_16_0_0_pre3
