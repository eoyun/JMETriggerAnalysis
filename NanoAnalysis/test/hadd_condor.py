#!/usr/bin/env python3
"""Step 1 of 2: merge the per-job output of one production tag with HTCondor,
one job per (year, era) group.

Input  : <indir>/<YYYY><E>_v<N>_JETMET<x>_<tag>/output_hist*.root
Output : <outdir>/<YYYY>_<tag>_<E>.root          (one per era, JETMET0+1 and
                                                  the v1/v2/... sub-versions merged)

The file list of each group is built here, at submit time, and shipped to the
job, so the worker never has to walk EOS.

  python3 hadd_condor.py -t 260916_v1 --dry-run   # 생성만, 제출 안 함
  python3 hadd_condor.py -t 260916_v1             # 생성 + condor_submit
"""

import argparse
import os
import re
import subprocess
import sys

EOS_BASE = "/eos/home-y/yeo/rdf/output"
MIN_INPUT_BYTES = 1024   # a real output is ~250 kB; stubs are 63 B
LCG_VIEW = "/cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/setup.sh"

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--tag", required=True,
                    help="production tag, e.g. 260916_v1")
parser.add_argument("-i", "--indir", default=EOS_BASE,
                    help="directory holding the per-dataset output dirs")
parser.add_argument("-o", "--outdir", default=os.path.join(EOS_BASE, "hadd_files"),
                    help="where the merged per-era files go")
parser.add_argument("-s", "--scrdir", default="Scr_hadd",
                    help="local directory for the generated job files")
parser.add_argument("-e", "--eras", default="",
                    help="comma-separated merge keys or era letters to restrict to")
parser.add_argument("--memory", type=int, default=4000, help="request_memory [MB]")
parser.add_argument("--runtime", type=int, default=21600, help="+MaxRuntime [s]")
parser.add_argument("--dry-run", action="store_true",
                    help="write the job files but do not call condor_submit")
args = parser.parse_args()


DEDUP_SRC = '''import ROOT, sys
src, dst = sys.argv[1], sys.argv[2]
f = ROOT.TFile.Open(src)
o = ROOT.TFile.Open(dst, "RECREATE")
seen = set()
for k in f.GetListOfKeys():
    n = k.GetName()
    if n in seen:
        continue
    seen.add(n)
    obj = f.Get(n)              # newest cycle = the fully merged one
    if hasattr(obj, "SetDirectory"):
        obj.SetDirectory(0)
    o.cd()
    obj.Write(n)
o.Close()
f.Close()
print("kept %d unique keys" % len(seen))
'''


def group_inputs(indir, tag):
    """key -> [root files], grouping every dataset dir by (year, era letter)."""
    pat = re.compile(r"^(\d{4})([A-Z])_v\d+_(JETMET\d?)_" + re.escape(tag) + r"$")
    groups = {}
    for name in sorted(os.listdir(indir)):
        m = pat.match(name)
        if not m:
            continue
        key = "%s_%s_%s" % (m.group(1), tag, m.group(2))
        path = os.path.join(indir, name)
        # A job that died mid-write (XRootD I/O failures) leaves a 63-byte stub.
        # "hadd -k" does not skip those on its multi-pass path: it fails inside
        # OpenExcessFiles and returns 1, which then aborts the whole group.
        # Drop them here so hadd only ever sees readable inputs.
        files, stubs = [], 0
        for f in sorted(os.listdir(path)):
            if not f.endswith(".root"):
                continue
            fp = os.path.join(path, f)
            if os.path.getsize(fp) < MIN_INPUT_BYTES:
                stubs += 1
                continue
            files.append(fp)
        if stubs:
            print("  %s: 깨진 스텁 %d개 제외" % (name, stubs))
        groups.setdefault(key, []).extend(files)
    return groups


def write_executable(scrdir, outdir):
    path = os.path.join(scrdir, "hadd.sh")
    with open(path, "w") as f:
        f.write("""#!/bin/bash
# one era group per job: hadd in the scratch dir, drop the duplicated
# bookkeeping keys, then copy to EOS
KEY=$1
source /cvmfs/cms.cern.ch/cmsset_default.sh
source %s
cd $_CONDOR_SCRATCH_DIR
NFILES=$(wc -l < ${KEY}.txt)
echo "merging ${NFILES} files into ${KEY}.root"
# -k : skip corrupt/missing inputs (some jobs die on XRootD and leave stubs)
# -n : cap simultaneously open files -> hadd runs in several passes
hadd -f -k -n 200 ${KEY}_raw.root $(cat ${KEY}.txt)
STATUS=$?
echo "hadd exit status ${STATUS}"
if [ ${STATUS} -ne 0 ]; then
    echo "FATAL: hadd failed, not copying"
    exit 1
fi
# Histograms merge, but TNamed does not: every pass re-copies the bookkeeping
# keys of every input, so they pile up quadratically (2025D: 1874 files in 10
# passes -> a 179 MB file whose key list alone took minutes to read). Keep one
# copy of each key -- the newest cycle is the fully merged one.
python3 dedup_keys.py ${KEY}_raw.root ${KEY}.root
if [ $? -ne 0 ] || [ ! -s ${KEY}.root ]; then
    echo "FATAL: dedup step failed, not copying"
    exit 1
fi
ls -l ${KEY}_raw.root ${KEY}.root
mkdir -p %s
cp ${KEY}.root %s/${KEY}.root
echo "copied to %s/${KEY}.root"
""" % (LCG_VIEW, outdir, outdir, outdir))
    os.chmod(path, 0o755)
    return path


def write_submit(scrdir, executable, keylist, memory, runtime):
    path = os.path.join(scrdir, "condor.submit")
    with open(path, "w") as f:
        f.write("# one hadd job per (year, era)\n")
        f.write("Universe = vanilla\n")
        f.write("Executable = %s\n" % executable)
        f.write("arguments = $(key)\n")
        f.write("transfer_input_files = %s/filelists/$(key).txt, %s/dedup_keys.py\n" % (scrdir, scrdir))
        f.write("request_disk = 8000000\n")
        f.write("should_transfer_files = Yes\n")
        f.write("request_memory = %d\n" % memory)
        f.write("output = %s/log/$(key).out\n" % scrdir)
        f.write("error  = %s/log/$(key).err\n" % scrdir)
        f.write("log    = %s/log/$(key).log\n" % scrdir)
        f.write("+MaxRuntime = %d\n" % runtime)
        f.write("queue key from %s\n" % keylist)
    return path


def main():
    scrdir = os.path.join(args.scrdir, args.tag)
    os.makedirs(os.path.join(scrdir, "filelists"), exist_ok=True)
    os.makedirs(os.path.join(scrdir, "log"), exist_ok=True)
    os.makedirs(args.outdir, exist_ok=True)

    groups = group_inputs(args.indir, args.tag)
    if not groups:
        sys.exit("no dataset directories matched tag '%s' under %s" % (args.tag, args.indir))

    wanted = [w for w in args.eras.split(",") if w]
    if wanted:
        groups = dict((k, v) for k, v in groups.items()
                      if k in wanted or k.rsplit("_", 1)[1] in wanted)
        if not groups:
            sys.exit("no group left after --eras %s" % args.eras)

    empty = sorted(k for k, v in groups.items() if not v)
    if empty:
        print("입력이 하나도 없는 그룹은 제외합니다: %s" % ", ".join(empty))
        groups = dict((k, v) for k, v in groups.items() if v)

    keylist = os.path.join(scrdir, "key_list.txt")
    with open(keylist, "w") as kl:
        for key in sorted(groups):
            with open(os.path.join(scrdir, "filelists", key + ".txt"), "w") as fl:
                fl.write("\n".join(groups[key]) + "\n")
            kl.write(key + "\n")
            print("%-24s %6d files" % (key, len(groups[key])))
    print("%d groups, %d files total" % (len(groups), sum(len(v) for v in groups.values())))

    with open(os.path.join(scrdir, "dedup_keys.py"), "w") as f:
        f.write(DEDUP_SRC)
    executable = write_executable(scrdir, args.outdir)
    submit = write_submit(scrdir, executable, keylist, args.memory, args.runtime)
    print("\nwrote %s\n      %s\n      %s/filelists/<key>.txt" % (executable, submit, scrdir))

    if args.dry_run:
        print("\n--dry-run: not submitting. To submit:\n  condor_submit %s" % submit)
        return
    subprocess.call(["condor_submit", submit])


if __name__ == "__main__":
    main()
