#!/usr/bin/env python3
"""Turn-on curves per calorimeter region, from the eta-vs-pT maps.

arXiv:2111.10431 fixes the offline pT interval of each single-jet trigger by
requiring "an efficiency above 99.5% in all pT and |y| bins" -- in |y| BINS,
not integrated over eta. plot_efficiency.py answers the eta-inclusive question;
this one splits the probe into the five regions booked in eta_pt_probe:

    -HF [-5.2,-3.0]  -HE [-3.0,-1.3]  HB [-1.3,1.3]  HE [1.3,3.0]  HF [3.0,5.2]

Numerator and denominator are the same pairing used for the 1D curves, so a
region here is simply the ProjectionY of one eta row of the 2D map.

  python3 plot_turnon_eta.py -t 261005_v1
  python3 plot_turnon_eta.py -t 261005_v1 -e 2024G -L 320
"""

import argparse
import glob
import json
import os
import re

import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

LEGS = [40, 60, 80, 110, 140, 200, 260, 320, 400, 450, 500, 550]
ALL_REGIONS = [(1, "-HF"), (2, "-HE"), (3, "HB"), (4, "HE"), (5, "HF")]
REGION_SETS = {
    "all":  ALL_REGIONS,
    "nohf": [r for r in ALL_REGIONS if "HF" not in r[1]],   # -HE, HB, HE 만
}
PAIRING = {"obj": "objnum", "event": "num"}
COLORS = [ROOT.kAzure + 2, ROOT.kGreen + 2, ROOT.kBlack, ROOT.kOrange + 7, ROOT.kRed + 1]

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--tag", required=True)
parser.add_argument("-i", "--indir", default="/eos/home-y/yeo/rdf/output/hadd_files")
parser.add_argument("-o", "--outdir", default="/eos/home-y/yeo/rdf/plots")
parser.add_argument("-e", "--eras", default="")
parser.add_argument("-L", "--leg", default="all")
parser.add_argument("-p", "--pairing", default="obj", choices=sorted(PAIRING))
parser.add_argument("-r", "--rebin", type=int, default=2)
parser.add_argument("-l", "--level", type=float, default=0.995)
parser.add_argument("--regions", default="all", choices=sorted(REGION_SETS),
                    help="all = 5구간, nohf = HF 제외 (-HE, HB, HE)")
parser.add_argument("--subdir", default="turnon_eta",
                    help="출력 하위 폴더 이름 (기존 그림을 덮지 않으려면 다르게 지정)")
parser.add_argument("--min-den", type=float, default=20)
parser.add_argument("--format", default="png,pdf")
args = parser.parse_args()


def as_counts(h, name):
    """Unweighted clone: TEfficiency refuses histograms carrying Sumw2."""
    ax = h.GetXaxis()
    out = ROOT.TH1D(name, "", h.GetNbinsX(), ax.GetXmin(), ax.GetXmax())
    out.SetDirectory(0)
    out.Sumw2(ROOT.kFALSE)
    for b in range(0, h.GetNbinsX() + 2):
        out.SetBinContent(b, round(h.GetBinContent(b)))
    out.SetEntries(h.GetEntries())
    return out


def row(h2, ibin, name):
    """One eta row of the 2D map, projected on pT."""
    p = h2.ProjectionY(name + "_py", ibin, ibin)
    p.SetDirectory(0)
    return as_counts(p, name)


def asymptote(eff, den, min_den, from_pt):
    num_s = den_s = 0.0
    from_pt = min(from_pt, 0.6 * den.GetXaxis().GetXmax())
    for b in range(1, den.GetNbinsX() + 1):
        if den.GetBinContent(b) < min_den or den.GetXaxis().GetBinLowEdge(b) < from_pt:
            continue
        den_s += den.GetBinContent(b)
        num_s += den.GetBinContent(b) * eff.GetEfficiency(b)
    return (num_s / den_s) if den_s else None


def plateau_point(eff, den, level, min_den, window=5):
    good = [b for b in range(1, den.GetNbinsX() + 1) if den.GetBinContent(b) >= min_den]
    for i, b in enumerate(good):
        block = good[i:i + window]
        if len(block) < min(window, len(good) - i):
            break
        if all(eff.GetEfficiency(bb) >= level for bb in block):
            return den.GetXaxis().GetBinLowEdge(b)
    return None


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


def main():
    regions = REGION_SETS[args.regions]
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

    rows_out = []
    keep = []
    print("%-7s %-5s %-5s %10s %10s %10s %10s" % (
        "era", "leg", "구간", "den", "eff_inf", "plateau", "99.5% 도달"))
    for era, path in files:
        f = ROOT.TFile.Open(path)
        edir = os.path.join(outroot, era)
        os.makedirs(edir, exist_ok=True)
        for leg in legs:
            d2 = f.Get("h_pfjet%d_den_eta_pt_probe" % leg)
            n2 = f.Get("h_pfjet%d_%s_eta_pt_probe" % (leg, PAIRING[args.pairing]))
            if not d2 or not n2 or d2.GetEntries() == 0:
                continue
            c = ROOT.TCanvas("c", "", 850, 650)
            c.SetGridx(); c.SetGridy(); c.SetTicks(1, 1)
            xmax = min(1000., max(200., 3. * leg))
            fr = ROOT.TH1F("fr", ";offline probe jet p_{T} [GeV];efficiency", 1, 0., xmax)
            fr.SetDirectory(0); fr.SetMinimum(0.); fr.SetMaximum(1.4); fr.Draw()
            # turn-on 은 1.0 에서 포화하므로 그 위 여백에 레전드를 둔다
            leg_box = ROOT.TLegend(0.13, 0.75, 0.90, 0.89)
            leg_box.SetNColumns(3)
            leg_box.SetBorderSize(0); leg_box.SetFillStyle(0); leg_box.SetTextSize(0.028)
            for k, (ib, rname) in enumerate(regions):
                den = row(d2, ib, "den_%s_%d_%s" % (era, leg, rname))
                num = row(n2, ib, "num_%s_%d_%s" % (era, leg, rname))
                if args.rebin > 1:
                    den.Rebin(args.rebin); num.Rebin(args.rebin)
                if den.Integral() < args.min_den:
                    continue
                bad = [b for b in range(0, den.GetNbinsX() + 2)
                       if num.GetBinContent(b) > den.GetBinContent(b)]
                if bad:
                    print("  [%s leg%d %s] 건너뜀: num>den" % (era, leg, rname))
                    continue
                eff = ROOT.TEfficiency(num, den)
                eff.SetStatisticOption(ROOT.TEfficiency.kFCP)
                eff.SetConfidenceLevel(0.683)
                asym = asymptote(eff, den, args.min_den, 2. * leg)
                plat = plateau_point(eff, den, args.level, args.min_den)
                g = eff_graph(eff, den, args.min_den)
                ci = [r[1] for r in ALL_REGIONS].index(rname)
                g.SetLineColor(COLORS[ci]); g.SetMarkerColor(COLORS[ci])
                g.SetMarkerStyle(20 + ci); g.SetMarkerSize(0.8)
                g.Draw("P SAME")
                leg_box.AddEntry(g, "%s  (%.0f)" % (rname, den.Integral()), "lp")
                keep += [den, num, eff, g]
                ok = (asym is not None and asym >= args.level)
                rows_out.append((era, leg, rname, den.Integral(), asym, plat, ok))
                print("%-7s %-5d %-5s %10.0f %10s %10s %10s" % (
                    era, leg, rname, den.Integral(),
                    ("%.4f" % asym) if asym else "-",
                    ("%.0f GeV" % plat) if plat else "-",
                    "예" if ok else "아니오"))
            line = ROOT.TLine(0., args.level, xmax, args.level)
            line.SetLineStyle(2); line.SetLineColor(ROOT.kRed + 1); line.Draw()
            leg_box.Draw()
            t = ROOT.TLatex(); t.SetNDC(); t.SetTextFont(42); t.SetTextSize(0.040)
            t.DrawLatex(0.12, 0.92, "#bf{CMS} #it{Preliminary}")
            t.SetTextSize(0.033)
            t.DrawLatex(0.56, 0.92, "%s   PFJet%d   %s" % (era, leg, args.pairing))
            for ext in args.format.split(","):
                c.SaveAs(os.path.join(edir, "eff%d_%s_byeta.%s" % (leg, args.pairing, ext)))
            c.Close()
        f.Close()

    csv = os.path.join(outroot, "summary_byeta.csv")
    with open(csv, "w") as out:
        out.write("era,leg,region,den,eff_asymptote,plateau_GeV,reaches_%.3f\n" % args.level)
        for r in rows_out:
            out.write("%s,%d,%s,%.0f,%s,%s,%s\n" % (
                r[0], r[1], r[2], r[3],
                ("%.4f" % r[4]) if r[4] else "", ("%.0f" % r[5]) if r[5] else "", int(r[6])))
    print("\nplots   -> %s/<era>/" % outroot)
    print("summary -> %s" % csv)


if __name__ == "__main__":
    main()
