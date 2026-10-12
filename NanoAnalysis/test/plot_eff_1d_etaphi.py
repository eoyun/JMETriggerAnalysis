#!/usr/bin/env python3
"""Efficiency vs eta and vs phi, per leg, straight from the 1D histograms.

Same numerator/denominator as the turn-on curves -- only the variable on the
x axis changes:

    den     h_pfjet<L>_den_<var>_probe       dijet base + reference path fired
                                             + tag above the reference threshold
    objnum  h_pfjet<L>_objnum_<var>_probe    + probe matched, HLT pT > L
    objden  h_pfjet<L>_objden_<var>_probe    + probe matched (any threshold)

No pT cut is applied, so a point is the turn-on integrated over the probe pT
spectrum at that eta (or phi), not the plateau efficiency. Structure in phi at
fixed eta, or an asymmetry between +eta and -eta, is still meaningful: the
spectrum does not know about phi, and is symmetric in eta.

  python3 plot_eff_1d_etaphi.py -t 261005_v1
  python3 plot_eff_1d_etaphi.py -t 261005_v1 -e 2024G -L 320,550
"""

import argparse
import glob
import os
import re

import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

LEGS = [40, 60, 80, 110, 140, 200, 260, 320, 400, 450, 500, 550]
PAIRING = {"obj": "objnum", "match": "objden"}
Y_MAX = 1.4          # 1.0 위 여백을 레전드 자리로 쓴다
def build_vars(eta_max):
    return [("eta", "probe jet #eta", -eta_max, eta_max),
            ("phi", "probe jet #phi", -3.1416, 3.1416)]
COLORS = [ROOT.kBlack, ROOT.kRed + 1, ROOT.kAzure + 2, ROOT.kGreen + 2, ROOT.kMagenta + 1,
          ROOT.kOrange + 7, ROOT.kCyan + 2, ROOT.kGray + 2, ROOT.kViolet + 1,
          ROOT.kSpring - 6, ROOT.kPink + 7, ROOT.kTeal + 3]

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--tag", required=True)
parser.add_argument("-i", "--indir", default="/eos/home-y/yeo/rdf/output/hadd_files")
parser.add_argument("-o", "--outdir", default="/eos/home-y/yeo/rdf/plots")
parser.add_argument("-e", "--eras", default="")
parser.add_argument("-L", "--leg", default="all")
parser.add_argument("-p", "--pairing", default="obj", choices=sorted(PAIRING))
parser.add_argument("-r", "--rebin", type=int, default=2)
parser.add_argument("--eta-max", type=float, default=5.2, help="eta 축 표시 범위 (+/-)")
parser.add_argument("--subdir", default="eff1d_etaphi",
                    help="출력 하위 폴더 이름 (기존 그림을 덮지 않으려면 다르게 지정)")
parser.add_argument("--min-den", type=float, default=20)
parser.add_argument("--format", default="png,pdf")
args = parser.parse_args()
VARS = build_vars(args.eta_max)


def as_counts(h, name):
    ax = h.GetXaxis()
    out = ROOT.TH1D(name, "", h.GetNbinsX(), ax.GetXmin(), ax.GetXmax())
    out.SetDirectory(0)
    out.Sumw2(ROOT.kFALSE)
    for b in range(0, h.GetNbinsX() + 2):
        out.SetBinContent(b, round(h.GetBinContent(b)))
    out.SetEntries(h.GetEntries())
    return out


def eff_graph(eff, den, min_den):
    g = ROOT.TGraphAsymmErrors()
    ax = den.GetXaxis()
    for b in range(1, den.GetNbinsX() + 1):
        if den.GetBinContent(b) < min_den:
            continue
        i = g.GetN()
        g.SetPoint(i, ax.GetBinCenter(b), eff.GetEfficiency(b))
        g.SetPointError(i, ax.GetBinWidth(b) / 2., ax.GetBinWidth(b) / 2.,
                        eff.GetEfficiencyErrorLow(b), eff.GetEfficiencyErrorUp(b))
    return g


def pair(f, leg, var, rebin):
    d = f.Get("h_pfjet%d_den_%s_probe" % (leg, var))
    n = f.Get("h_pfjet%d_%s_%s_probe" % (leg, PAIRING[args.pairing], var))
    if not d or not n or d.GetEntries() == 0:
        return None, None
    d = as_counts(d, "d_%d_%s" % (leg, var))
    n = as_counts(n, "n_%d_%s" % (leg, var))
    if rebin > 1:
        d.Rebin(rebin); n.Rebin(rebin)
    if any(n.GetBinContent(b) > d.GetBinContent(b) for b in range(0, d.GetNbinsX() + 2)):
        return None, None
    return n, d


def header(era, txt):
    t = ROOT.TLatex(); t.SetNDC(); t.SetTextFont(42); t.SetTextSize(0.040)
    t.DrawLatex(0.11, 0.93, "#bf{CMS} #it{Preliminary}")
    t.SetTextSize(0.033)
    t.DrawLatex(0.55, 0.93, "%s   %s" % (era, txt))


def main():
    legs = LEGS if args.leg == "all" else [int(x) for x in args.leg.split(",") if x]
    wanted = [w for w in args.eras.split(",") if w]
    outroot = os.path.join(args.outdir, args.tag, args.subdir)
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

    keep = []
    for era, path in files:
        f = ROOT.TFile.Open(path)
        edir = os.path.join(outroot, era)
        os.makedirs(edir, exist_ok=True)
        overlay = {v: [] for v, _, _, _ in VARS}
        for k, leg in enumerate(legs):
            c = ROOT.TCanvas("c", "", 1200, 520)
            c.Divide(2, 1)
            for ip, (var, xtitle, xlo, xhi) in enumerate(VARS):
                num, den = pair(f, leg, var, args.rebin)
                if num is None:
                    continue
                eff = ROOT.TEfficiency(num, den)
                eff.SetStatisticOption(ROOT.TEfficiency.kFCP)
                eff.SetConfidenceLevel(0.683)
                g = eff_graph(eff, den, args.min_den)
                keep += [num, den, eff, g]
                overlay[var].append((leg, eff, den))
                p = c.cd(ip + 1)
                p.SetGridx(); p.SetGridy(); p.SetTicks(1, 1); p.SetLeftMargin(0.12)
                fr = ROOT.TH1F("fr%d" % ip, ";%s;efficiency" % xtitle, 1, xlo, xhi)
                fr.SetDirectory(0); fr.SetMinimum(0.); fr.SetMaximum(Y_MAX); fr.Draw()
                keep.append(fr)
                g.SetMarkerStyle(20); g.SetMarkerSize(0.7)
                g.SetLineColor(ROOT.kAzure + 2); g.SetMarkerColor(ROOT.kAzure + 2)
                g.Draw("P SAME")
                t = ROOT.TLatex(); t.SetNDC(); t.SetTextFont(42); t.SetTextSize(0.042)
                t.DrawLatex(0.15, 0.86, "PFJet%d  %s" % (leg, args.pairing))
                t.SetTextSize(0.034)
                t.DrawLatex(0.15, 0.80, "den %.0f" % den.Integral())
            c.cd(0)
            header(era, "eff vs #eta / #phi")
            for ext in args.format.split(","):
                c.SaveAs(os.path.join(edir, "eff%d_%s_vs_etaphi.%s" % (leg, args.pairing, ext)))
            c.Close()

        # 모든 leg 겹쳐 그리기
        for var, xtitle, xlo, xhi in VARS:
            if not overlay[var]:
                continue
            c = ROOT.TCanvas("c", "", 900, 620)
            c.SetGridx(); c.SetGridy(); c.SetTicks(1, 1)
            fr = ROOT.TH1F("fro", ";%s;efficiency" % xtitle, 1, xlo, xhi)
            fr.SetDirectory(0); fr.SetMinimum(0.); fr.SetMaximum(Y_MAX); fr.Draw()
            # headroom above 1.0 is empty, so the legend goes there in columns
            # instead of sitting on top of the points
            lg = ROOT.TLegend(0.13, 0.74, 0.90, 0.89)
            lg.SetNColumns(4)
            lg.SetBorderSize(0); lg.SetFillStyle(0); lg.SetTextSize(0.028)
            for k, (leg, eff, den) in enumerate(overlay[var]):
                g = eff_graph(eff, den, args.min_den)
                g.SetMarkerStyle(20 + (k % 8)); g.SetMarkerSize(0.6)
                g.SetLineColor(COLORS[k % len(COLORS)]); g.SetMarkerColor(COLORS[k % len(COLORS)])
                g.Draw("P SAME"); keep.append(g)
                lg.AddEntry(g, "PFJet%d" % leg, "lp")
            lg.Draw()
            header(era, "eff vs %s, all legs" % var)
            for ext in args.format.split(","):
                c.SaveAs(os.path.join(edir, "all_%s_%s.%s" % (var, args.pairing, ext)))
            c.Close()
        f.Close()
    print("plots -> %s/<era>/" % outroot)


if __name__ == "__main__":
    main()
