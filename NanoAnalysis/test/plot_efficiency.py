#!/usr/bin/env python3
"""Step 2 of 2: tag-and-probe trigger efficiency curves from the merged files.

Efficiency vs the OFFLINE probe jet pT, with Clopper-Pearson intervals
(TEfficiency, 68.3% CL) -- numerator and denominator are nested by
construction, so a binomial treatment is the correct one.

Pairings (-p), all built from the tag-and-probe dijet sample where the
reference path was fired by the TAG:

  obj      num h_pfjet<L>_objnum_pt_probe / den h_pfjet<L>_den_pt_probe
           probe matched to a SinglePFJet HLT object above <L>, over the whole
           reference sample. Nothing about the probe enters the denominator,
           so this is the turn-on.                                  [default]

  objcond  num h_pfjet<L>_objnum_pt_probe / den h_pfjet<L>_objden_pt_probe
           same numerator, but conditional on the probe being matched at all.
           The denominator is then already filtered on the probe's online pT,
           which biases the rise upwards. Diagnostic only.

  event    num h_pfjet<L>_num_pt_probe / den h_pfjet<L>_den_pt_probe
           event-level path AND. CMS HLT prescales are deterministic counters,
           so adjacent prescaled paths accept nearly disjoint events and this
           collapses to ~0 for those legs. Valid for the unprescaled high legs.

  legacy   the h_after_hltpt* triplet (reference HLT_PFJet110, no tag cut).

Usage
  python3 plot_efficiency.py -t 260916_v1                    # obj, 모든 era
  python3 plot_efficiency.py -t 260916_v1 -p all -e 2024G
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

PAIRINGS = {
    "obj":     ("h_pfjet{L}_objnum_pt_probe", "h_pfjet{L}_den_pt_probe"),
    "objcond": ("h_pfjet{L}_objnum_pt_probe", "h_pfjet{L}_objden_pt_probe"),
    "event":   ("h_pfjet{L}_num_pt_probe",    "h_pfjet{L}_den_pt_probe"),
}
LEGACY = [
    ("eff200_sel",     "h_after_hltpt200_pt_probe", "h_after_pt_probe"),
    ("eff320_hltpt200", "h_after_hltpt320_pt_probe", "h_after_hltpt200_pt_probe"),
    ("eff500_hltpt320", "h_after_hltpt500_pt_probe", "h_after_hltpt320_pt_probe"),
]
COLORS = [ROOT.kBlack, ROOT.kRed + 1, ROOT.kAzure + 2, ROOT.kGreen + 2,
          ROOT.kMagenta + 1, ROOT.kOrange + 7, ROOT.kCyan + 2, ROOT.kGray + 2,
          ROOT.kViolet + 1, ROOT.kSpring - 6, ROOT.kPink + 7, ROOT.kTeal + 3]

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--tag", required=True, help="production tag, e.g. 260916_v1")
parser.add_argument("-i", "--indir", default="/eos/home-y/yeo/rdf/output/hadd_files")
parser.add_argument("-o", "--outdir", default="/eos/home-y/yeo/rdf/plots",
                    help="그림 출력 디렉토리 (기본: EOS)")
parser.add_argument("-p", "--pairing", default="obj",
                    choices=sorted(PAIRINGS) + ["legacy", "all"])
parser.add_argument("-e", "--eras", default="", help="comma-separated, e.g. 2024G,2025D")
parser.add_argument("-r", "--rebin", type=int, default=2, help="rebin factor (10 GeV bins)")
parser.add_argument("-l", "--level", type=float, default=0.995, help="working point")
parser.add_argument("--min-den", type=float, default=20, help="min denominator per bin")
parser.add_argument("--format", default="png,pdf")
args = parser.parse_args()


# ---------------------------------------------------------------- helpers
def as_counts(h, name):
    """Unweighted clone: TEfficiency refuses histograms carrying Sumw2."""
    ax = h.GetXaxis()
    out = ROOT.TH1D(name, h.GetTitle(), h.GetNbinsX(), ax.GetXmin(), ax.GetXmax())
    out.SetDirectory(0)
    out.Sumw2(ROOT.kFALSE)
    for b in range(0, h.GetNbinsX() + 2):
        out.SetBinContent(b, round(h.GetBinContent(b)))
    out.SetEntries(h.GetEntries())   # SetBinContent bumps fEntries, restore it
    return out


def load_pair(f, num_name, den_name, rebin):
    num, den = f.Get(num_name), f.Get(den_name)
    if not num or not den:
        return None, None, "히스토그램 없음 (%s / %s)" % (num_name, den_name)
    num = as_counts(num, num_name + "_c")
    den = as_counts(den, den_name + "_c")
    if rebin > 1:
        num.Rebin(rebin)
        den.Rebin(rebin)
    bad = [b for b in range(0, den.GetNbinsX() + 2)
           if num.GetBinContent(b) > den.GetBinContent(b)]
    if bad:
        return None, None, "num > den in bins %s" % bad[:5]
    return num, den, None


def make_eff(num, den, name, level):
    eff = ROOT.TEfficiency(num, den)
    eff.SetStatisticOption(ROOT.TEfficiency.kFCP)   # Clopper-Pearson
    eff.SetConfidenceLevel(0.683)
    eff.SetName(name)
    eff.SetTitle(";offline probe jet p_{T} [GeV];efficiency")
    return eff


def asymptote(eff, den, min_den, from_pt):
    """Efficiency the curve actually settles at, averaged over pT > from_pt.

    It is not 1: the probe may sit outside the SinglePFJet acceptance (bit 42
    is central-only, forward jets are bit 43) or fail the dR<0.2 match, so the
    curve levels off a percent or two below one. Measured on 2024G leg 320 the
    matched fraction falls from 0.78 in the barrel to 0.17 at |eta| ~ 3.75.
    """
    axmax = den.GetXaxis().GetXmax()
    from_pt = min(from_pt, 0.6 * axmax)      # 축 밖으로 나가면 점근값이 안 잡힌다
    num_s = den_s = 0.0
    for b in range(1, den.GetNbinsX() + 1):
        if den.GetBinContent(b) < min_den:
            continue
        if den.GetXaxis().GetBinLowEdge(b) < from_pt:
            continue
        den_s += den.GetBinContent(b)
        num_s += den.GetBinContent(b) * eff.GetEfficiency(b)
    return (num_s / den_s) if den_s else None


def plateau_point(eff, den, level, min_den, window=5):
    """Lowest bin edge from which the efficiency stays at or above `level`.

    The requirement is checked over the next `window` sufficiently populated
    bins rather than all the way to the end of the axis: with 20 GeV bins the
    last populated bins carry very few events and a single downward
    fluctuation there would otherwise push the answer hundreds of GeV up.
    """
    good = [b for b in range(1, den.GetNbinsX() + 1)
            if den.GetBinContent(b) >= min_den]
    for i, b in enumerate(good):
        block = good[i:i + window]
        if len(block) < min(window, len(good) - i):
            break
        if all(eff.GetEfficiency(bb) >= level for bb in block):
            return den.GetXaxis().GetBinLowEdge(b)
    return None


def style(obj, i):
    c = COLORS[i % len(COLORS)]
    obj.SetLineColor(c)
    obj.SetMarkerColor(c)
    obj.SetMarkerStyle(20 + (i % 8))
    obj.SetMarkerSize(0.8)


def header(era, extra=""):
    t = ROOT.TLatex()
    t.SetNDC()
    t.SetTextFont(42)
    t.SetTextSize(0.040)
    t.DrawLatex(0.12, 0.92, "#bf{CMS} #it{Preliminary}")
    t.SetTextSize(0.035)
    t.DrawLatex(0.62, 0.92, "%s  %s" % (era, extra))


def save(canvas, path):
    for ext in args.format.split(","):
        canvas.SaveAs("%s.%s" % (path, ext))


# ---------------------------------------------------------------- drawing
def eff_graph(eff, den, min_den):
    """TEfficiency is the Clopper-Pearson calculator; drawing goes through a
    graph so that bins too empty to mean anything are simply left out."""
    g = ROOT.TGraphAsymmErrors()
    ax = den.GetXaxis()
    for b in range(1, den.GetNbinsX() + 1):
        if den.GetBinContent(b) < min_den:
            continue
        i = g.GetN()
        g.SetPoint(i, ax.GetBinCenter(b), eff.GetEfficiency(b))
        g.SetPointError(i, ax.GetBinWidth(b) / 2.0, ax.GetBinWidth(b) / 2.0,
                        eff.GetEfficiencyErrorLow(b), eff.GetEfficiencyErrorUp(b))
    return g


def make_frame(xmax):
    fr = ROOT.TH1F("frame", ";offline probe jet p_{T} [GeV];efficiency", 1, 0.0, xmax)
    fr.SetDirectory(0)
    fr.SetMinimum(0.0)
    fr.SetMaximum(1.4)
    fr.GetYaxis().SetTitleOffset(1.2)
    return fr


def draw_one(eff, den, label, era, outpath, level, xmax, from_pt):
    c = ROOT.TCanvas("c", "", 800, 650)
    c.SetGridx(); c.SetGridy(); c.SetTicks(1, 1)
    fr = make_frame(xmax); fr.Draw()
    g = eff_graph(eff, den, args.min_den)
    style(g, 0)
    g.Draw("P SAME")

    asym = asymptote(eff, den, args.min_den, from_pt)
    plat_abs = plateau_point(eff, den, level, args.min_den)
    plat_rel = plateau_point(eff, den, level * asym, args.min_den) if asym else None

    keep_local = []
    line = ROOT.TLine(0.0, level, xmax, level)
    line.SetLineStyle(2); line.SetLineColor(ROOT.kRed + 1); line.Draw(); keep_local.append(line)
    if asym:
        la = ROOT.TLine(0.0, asym, xmax, asym)
        la.SetLineColor(ROOT.kGray + 2); la.Draw(); keep_local.append(la)
        lr = ROOT.TLine(0.0, level * asym, xmax, level * asym)
        lr.SetLineStyle(2); lr.SetLineColor(ROOT.kBlue + 1); lr.Draw(); keep_local.append(lr)
    if plat_rel is not None:
        m = ROOT.TLine(plat_rel, 0.0, plat_rel, 1.4)
        m.SetLineStyle(3); m.SetLineColor(ROOT.kBlue + 1); m.Draw(); keep_local.append(m)

    txt = ROOT.TLatex(); txt.SetNDC(); txt.SetTextFont(42); txt.SetTextSize(0.031)
    txt.DrawLatex(0.46, 0.34, label)
    txt.DrawLatex(0.46, 0.29, "plateau #varepsilon_{#infty} = %s  (p_{T} > %.0f GeV)" % (
        ("%.4f" % asym) if asym else "--", from_pt))
    txt.DrawLatex(0.46, 0.24, "#varepsilon/#varepsilon_{#infty} > %.3f above %s" % (
        level, ("%.0f GeV" % plat_rel) if plat_rel is not None else "--"))
    txt.DrawLatex(0.46, 0.19, "#varepsilon > %.3f (absolute) above %s" % (
        level, ("%.0f GeV" % plat_abs) if plat_abs is not None else "--"))
    txt.DrawLatex(0.46, 0.14, "denominator %.0f entries" % den.GetEntries())
    header(era, "tag & probe")
    save(c, outpath)
    c.Close()
    return plat_rel, plat_abs, asym


def draw_overlay(items, title, era, outpath, level, xmax):
    """items = [(label, TEfficiency, denominator)]"""
    c = ROOT.TCanvas("c", "", 850, 650)
    c.SetGridx(); c.SetGridy(); c.SetTicks(1, 1)
    fr = make_frame(xmax); fr.Draw()
    leg = ROOT.TLegend(0.13, 0.74, 0.90, 0.89)
    leg.SetNColumns(4)
    leg.SetBorderSize(0); leg.SetFillStyle(0); leg.SetTextSize(0.026)
    graphs = []
    for i, (label, eff, den) in enumerate(items):
        g = eff_graph(eff, den, args.min_den)
        style(g, i)
        g.Draw("P SAME")
        graphs.append(g)
        leg.AddEntry(g, label, "lp")
    line = ROOT.TLine(0.0, level, xmax, level)
    line.SetLineStyle(2); line.SetLineColor(ROOT.kRed + 1); line.Draw()
    leg.Draw()
    header(era, title)
    save(c, outpath)
    c.Close()


# ---------------------------------------------------------------- main
def era_files(indir, tag, wanted):
    out = []
    for path in sorted(glob.glob(os.path.join(indir, "*_%s_*.root" % tag))):
        m = re.match(r"^(\d{4})_%s_([A-Z])$" % re.escape(tag),
                     os.path.basename(path)[:-5])
        if not m:
            continue
        era = m.group(1) + m.group(2)
        if wanted and era not in wanted:
            continue
        if os.path.getsize(path) < 1000:          # 빈 era 자리표시 파일
            print("  skip %s (비어 있음)" % era)
            continue
        out.append((era, path))
    return out


def main():
    pairings = sorted(PAIRINGS) + ["legacy"] if args.pairing == "all" else [args.pairing]
    wanted = [w for w in args.eras.split(",") if w]
    outroot = os.path.join(args.outdir, args.tag)
    os.makedirs(outroot, exist_ok=True)

    files = era_files(args.indir, args.tag, wanted)
    if not files:
        raise SystemExit("no merged file found for tag %s in %s" % (args.tag, args.indir))
    print("eras: %s" % ", ".join(e for e, _ in files))

    rows = []                         # (era, pairing, leg, plateau, den, num)
    per_leg = {}                      # (pairing, leg) -> [(era, eff)]
    keep = []                         # keep python refs alive for ROOT

    for era, path in files:
        f = ROOT.TFile.Open(path)
        edir = os.path.join(outroot, era)
        os.makedirs(edir, exist_ok=True)
        for pname in pairings:
            entries = (LEGACY if pname == "legacy" else
                       [("eff%d" % L, PAIRINGS[pname][0].format(L=L),
                         PAIRINGS[pname][1].format(L=L)) for L in LEGS])
            overlay = []
            for tagname, nname, dname in entries:
                num, den, err = load_pair(f, nname, dname, args.rebin)
                if err:
                    print("  [%s %s %s] 건너뜀: %s" % (era, pname, tagname, err))
                    continue
                if den.GetEntries() == 0:
                    print("  [%s %s %s] 건너뜀: 분모 0" % (era, pname, tagname))
                    continue
                L = int(tagname[3:]) if tagname.startswith("eff") and tagname[3:].isdigit() else None
                xmax = min(1000.0, max(200.0, 3.0 * L)) if L else 1000.0
                eff = make_eff(num, den, "%s_%s_%s" % (era, pname, tagname), args.level)
                keep += [num, den, eff]
                label = "#splitline{%s}{num %s}" % (tagname, nname)
                from_pt = 2.0 * L if L else 600.0
                plat, plat_abs, asym = draw_one(
                    eff, den, label, era,
                    os.path.join(edir, "%s_%s" % (tagname, pname)),
                    args.level, xmax, from_pt)
                rows.append((era, pname, tagname, plat, plat_abs, asym,
                             den.GetEntries(), num.GetEntries()))
                overlay.append(("%s" % tagname, eff, den))
                per_leg.setdefault((pname, tagname), []).append((era, eff, den))
            if overlay:
                draw_overlay(overlay, pname, era,
                             os.path.join(edir, "all_%s" % pname), args.level, 1000.0)
        f.Close()

    # era 비교: leg 하나당 모든 era 겹쳐 그리기
    cmpdir = os.path.join(outroot, "era_comparison")
    os.makedirs(cmpdir, exist_ok=True)
    for (pname, tagname), items in sorted(per_leg.items()):
        if len(items) < 2:
            continue
        L = int(tagname[3:]) if tagname.startswith("eff") and tagname[3:].isdigit() else None
        xmax = min(1000.0, max(200.0, 3.0 * L)) if L else 1000.0
        draw_overlay(items, "%s  %s" % (tagname, pname), "all eras",
                     os.path.join(cmpdir, "%s_%s" % (tagname, pname)), args.level, xmax)

    # 요약 + 측정된 plateau (plateau.json 과 같은 스키마)
    csv = os.path.join(outroot, "summary.csv")
    with open(csv, "w") as out:
        out.write("era,pairing,leg,plateau_rel_GeV,plateau_abs_GeV,eff_asymptote,"
                  "den_entries,num_entries\n")
        for r in rows:
            out.write("%s,%s,%s,%s,%s,%s,%.0f,%.0f\n" % (
                r[0], r[1], r[2],
                "" if r[3] is None else "%.0f" % r[3],
                "" if r[4] is None else "%.0f" % r[4],
                "" if r[5] is None else "%.4f" % r[5], r[6], r[7]))

    measured = {}
    for era, pname, tagname, plat, _, _, _, _ in rows:
        if pname != "obj" or plat is None or not tagname.startswith("eff"):
            continue
        if not tagname[3:].isdigit():
            continue
        L = int(tagname[3:])
        measured[L] = max(measured.get(L, 0), plat)     # era 중 가장 보수적인 값
    pj = os.path.join(outroot, "plateau_measured.json")
    with open(pj, "w") as out:
        json.dump({"_comment": [
            "Measured with plot_efficiency.py from tag %s, pairing 'obj'." % args.tag,
            "plateau = lowest bin edge above which eff/eff_asymptote stays >= %.3f," % args.level,
            "relative to the plateau the curve actually reaches (it is below 1:",
            "forward probes are outside the bit-42 SinglePFJet acceptance).",
            "Most conservative value over all eras.",
            "Copy into plateau.json to feed it back into the analysis."],
            "plateau": dict((str(k), v) for k, v in sorted(measured.items()))},
            out, indent=2)

    print("\n%-8s %-8s %-8s %12s %12s %10s %12s" %
          ("era", "pairing", "leg", "plateau(rel)", "plateau(abs)", "eff_inf", "den"))
    for r in rows:
        print("%-8s %-8s %-8s %12s %12s %10s %12.0f" % (
            r[0], r[1], r[2],
            "-" if r[3] is None else "%.0f GeV" % r[3],
            "-" if r[4] is None else "%.0f GeV" % r[4],
            "-" if r[5] is None else "%.4f" % r[5], r[6]))
    print("\nplots   -> %s/<era>/" % outroot)
    print("summary -> %s" % csv)
    print("plateau -> %s : %s" % (pj, measured))


if __name__ == "__main__":
    main()
