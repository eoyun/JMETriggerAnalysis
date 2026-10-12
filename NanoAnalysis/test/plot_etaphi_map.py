#!/usr/bin/env python3
"""eta-phi efficiency maps from the tag-and-probe output, on the JME veto-map grid.

The booked maps sit on exactly the grid the official JME jet veto maps use
(82 variable eta bins x 72 uniform phi bins over [-pi, pi]), so ours can be
compared with theirs bin for bin.

Pairings -- the denominator is always h_pfjet<L>_den_eta_phi_probe, which puts
NO requirement on the probe. Using objden as the denominator would drop a dead
region from numerator and denominator alike and hide exactly what we look for.

  match      objden/den   probe matched to a SinglePFJet HLT object at all.
  threshold  objnum/den   + that object above the leg threshold.

"match" is NOT threshold-free: TrigObj only stores the objects of the paths
that fired, so for leg L the effective online threshold is that of the
reference path (leg 550 -> HLT_PFJet500). Measured on 2023D leg 550, objden/den
is 0.054 at an offline probe pT of 300-400 GeV and 0.776 at 500-600, i.e. it
turns on at ~500 GeV, not at 40. Read both maps as "the trigger response around
the reference threshold", not as a pT-independent detector map.

Every leg is plottable: with no pT cut on the booked maps, 2024G gives 98
probes/bin at leg 40 (92% of the 5904 bins measured) and 1991/bin at leg 550
(69%). Low legs cover forward eta better, high legs have the density.

Known limitation: the booked maps carry no offline probe pT cut, so the raw
efficiency map is weighted by the local pT spectrum. The ring-normalised map
(each eta row divided by its own mean over phi) removes most of that and is
what should be read for phi-localised structure such as BPix.

  python3 plot_etaphi_map.py -t 260923_v1
  python3 plot_etaphi_map.py -t 260923_v1 -e 2024G -L 550 -p match
"""

import argparse
from array import array
import glob
import gzip
import json
import os
import re

import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPalette(ROOT.kBird)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

POG = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME"

# era -> veto-map campaign. 2022 splits at the ECAL endcap water-leak (E onward),
# 2023 splits at the BPix failure (D onward). 2025 has no map published yet.
CAMPAIGN = {
    "2022C": "2022_Summer22", "2022D": "2022_Summer22",
    "2022E": "2022_Summer22EE", "2022F": "2022_Summer22EE", "2022G": "2022_Summer22EE",
    "2023B": "2023_Summer23", "2023C": "2023_Summer23", "2023D": "2023_Summer23BPix",
    "2024C": "2024_Summer24", "2024D": "2024_Summer24", "2024E": "2024_Summer24",
    "2024F": "2024_Summer24", "2024G": "2024_Summer24", "2024H": "2024_Summer24",
    "2024I": "2024_Summer24",
}

PFJET_LEGS = [40, 60, 80, 110, 140, 200, 260, 320, 400, 450, 500, 550]

PAIRING = {"match": "objden", "threshold": "objnum"}

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--tag", required=True)
parser.add_argument("-i", "--indir", default="/eos/home-y/yeo/rdf/output/hadd_files")
parser.add_argument("-o", "--outdir", default="/eos/home-y/yeo/rdf/plots")
parser.add_argument("-e", "--eras", default="")
parser.add_argument("-L", "--leg", default="all",
                    help="PFJet leg(s): 'all', or a comma-separated list e.g. 320,550")
parser.add_argument("-p", "--pairing", default="match", choices=sorted(PAIRING) + ["all"])
parser.add_argument("--min-den", type=float, default=20, help="bins below this stay blank")
parser.add_argument("--format", default="png,pdf")
args = parser.parse_args()


def veto_map(campaign, kind="jetvetomap"):
    """Official map as a TH2D on its own grid, or None when not published."""
    path = os.path.join(POG, campaign, "jetvetomaps.json.gz")
    if not os.path.isfile(path):
        return None, None
    doc = json.load(gzip.open(path))
    corr = doc["corrections"][0]
    for item in corr["data"]["content"]:
        if str(item["key"]) != kind:
            continue
        mb = item["value"]
        ex, ey = mb["edges"]
        # array() keeps the buffer alive; a temporary std::vector would be freed
        # right away and TH2D would be left with dangling edges.
        ax, ay = array("d", ex), array("d", ey)
        h = ROOT.TH2D("veto_" + campaign + "_" + kind, ";#eta;#phi",
                      len(ex) - 1, ax, len(ey) - 1, ay)
        h.SetDirectory(0)
        for i in range(len(ex) - 1):
            for j in range(len(ey) - 1):
                h.SetBinContent(i + 1, j + 1, mb["content"][i * (len(ey) - 1) + j])
        return h, corr["name"]
    return None, None


def ratio_map(num, den, min_den):
    """Bin-by-bin efficiency; bins with too little denominator are left empty."""
    r = den.Clone(num.GetName() + "_eff")
    r.SetDirectory(0)
    r.Reset()
    for i in range(1, den.GetNbinsX() + 1):
        for j in range(1, den.GetNbinsY() + 1):
            d = den.GetBinContent(i, j)
            if d < min_den:
                continue
            n = num.GetBinContent(i, j)
            p = n / d
            r.SetBinContent(i, j, p)
            r.SetBinError(i, j, ((p * (1 - p) / d) ** 0.5) or 1e-6)
    return r


def ring_normalise(h):
    """Divide every eta row by its own mean over phi -- kills the pT-spectrum
    trend in eta and leaves phi-localised structure visible."""
    out = h.Clone(h.GetName() + "_ring")
    out.SetDirectory(0)
    for i in range(1, h.GetNbinsX() + 1):
        vals = [h.GetBinContent(i, j) for j in range(1, h.GetNbinsY() + 1)
                if h.GetBinContent(i, j) > 0]
        if len(vals) < 5:
            for j in range(1, h.GetNbinsY() + 1):
                out.SetBinContent(i, j, 0)
            continue
        m = sum(vals) / len(vals)
        for j in range(1, h.GetNbinsY() + 1):
            v = h.GetBinContent(i, j)
            out.SetBinContent(i, j, (v / m) if v > 0 and m > 0 else 0)
    return out


def draw(h, title, era, path, zmin, zmax, extra=None):
    c = ROOT.TCanvas("c", "", 1000, 620)
    c.SetRightMargin(0.13)
    c.SetLeftMargin(0.09)
    h.SetTitle(";jet #eta;jet #phi")
    h.GetZaxis().SetRangeUser(zmin, zmax)
    h.Draw("COLZ")
    marks = None
    if extra is not None:                       # 공식 veto bin 을 점으로 덧그림
        marks = ROOT.TGraph()
        for i in range(1, extra.GetNbinsX() + 1):
            for j in range(1, extra.GetNbinsY() + 1):
                if extra.GetBinContent(i, j) == 0:
                    continue
                marks.SetPoint(marks.GetN(),
                               extra.GetXaxis().GetBinCenter(i),
                               extra.GetYaxis().GetBinCenter(j))
        if marks.GetN():
            marks.SetMarkerStyle(20)
            marks.SetMarkerSize(0.35)
            marks.SetMarkerColor(ROOT.kRed + 1)
            marks.Draw("P SAME")
    t = ROOT.TLatex(); t.SetNDC(); t.SetTextFont(42); t.SetTextSize(0.037)
    t.DrawLatex(0.09, 0.94, "#bf{CMS} #it{Preliminary}")
    t.SetTextSize(0.031)
    t.DrawLatex(0.45, 0.94, "%s   %s" % (era, title))
    for ext in args.format.split(","):
        c.SaveAs("%s.%s" % (path, ext))
    c.Close()


def overlap_stats(eff, veto, min_den, thresh):
    """How well do our low-efficiency bins line up with the official veto bins?"""
    ours = set(); theirs = set()
    for i in range(1, eff.GetNbinsX() + 1):
        for j in range(1, eff.GetNbinsY() + 1):
            if eff.GetBinContent(i, j) > 0 and eff.GetBinContent(i, j) < thresh:
                ours.add((i, j))
            if veto is not None and veto.GetBinContent(i, j) != 0:
                theirs.add((i, j))
    both = ours & theirs
    return len(ours), len(theirs), len(both)


def main():
    pairings = sorted(PAIRING) if args.pairing == "all" else [args.pairing]
    legs = PFJET_LEGS if args.leg == "all" else [int(x) for x in args.leg.split(",") if x]
    wanted = [w for w in args.eras.split(",") if w]
    outroot = os.path.join(args.outdir, args.tag, "etaphi")
    os.makedirs(outroot, exist_ok=True)

    files = []
    for p in sorted(glob.glob(os.path.join(args.indir, "*_%s_*.root" % args.tag))):
        m = re.match(r"^(\d{4})_%s_([A-Z])$" % re.escape(args.tag), os.path.basename(p)[:-5])
        if not m or os.path.getsize(p) < 1000:
            continue
        era = m.group(1) + m.group(2)
        if not wanted or era in wanted:
            files.append((era, p))
    if not files:
        raise SystemExit("no merged file for tag %s" % args.tag)

    print("%-7s %-5s %-10s %8s %7s %8s %7s %10s   %s" % (
        "era", "leg", "pairing", "측정bin", "bin당", "평균eff", "저효율", "겹침/공식",
        "campaign"))
    for era, path in files:
        f = ROOT.TFile.Open(path)
        camp = CAMPAIGN.get(era)
        veto, vname = veto_map(camp) if camp else (None, None)
        for leg in legs:
          for pname in pairings:
            den = f.Get("h_pfjet%d_den_eta_phi_probe" % leg)
            num = f.Get("h_pfjet%d_%s_eta_phi_probe" % (leg, PAIRING[pname]))
            if not den or not num or den.GetEntries() == 0:
                print("  [%s leg%d %s] 건너뜀: 히스토그램 없음/빈 분모" % (era, leg, pname))
                continue
            eff = ratio_map(num, den, args.min_den)
            ring = ring_normalise(eff)
            base = os.path.join(outroot, "%s_leg%d_%s" % (era, leg, pname))
            draw(eff, "%s  leg%d  %s" % (pname, leg, PAIRING[pname] + "/den"),
                 era, base, 0.0, 1.0, veto)
            draw(ring, "%s  leg%d  ring-normalised" % (pname, leg),
                 era, base + "_ring", 0.8, 1.05, veto)
            nz = [eff.GetBinContent(i, j)
                  for i in range(1, eff.GetNbinsX() + 1)
                  for j in range(1, eff.GetNbinsY() + 1) if eff.GetBinContent(i, j) > 0]
            o, t_, b = overlap_stats(ring, veto, args.min_den, 0.90)
            print("%-7s %-5d %-10s %8d %7.0f %8.3f %7d %10s   %s" % (
                era, leg, pname, len(nz),
                (den.Integral() / len(nz)) if nz else 0,
                (sum(nz) / len(nz)) if nz else 0, o,
                ("%d/%d" % (b, t_)) if veto else "-", vname or "없음"))
        if veto is not None:
            draw(veto, "official jetvetomap", era,
                 os.path.join(outroot, "%s_official_vetomap" % era), 0, 1)
        f.Close()
    print("\nmaps -> %s" % outroot)


if __name__ == "__main__":
    main()
