#!/usr/bin/env python3
"""Year-level plots, restricted to |eta| < 3.

Takes one merged file per year (hadd of that year's era files) and produces,
for every leg:

  1. turnon_eta3     integrated turn-on over |eta| < 3, i.e. the ProjectionY of
                     eta_pt_probe over the -HE, HB and HE rows. The plain
                     pt_probe histogram cannot be used here: it has no eta axis
                     and would include HF.
  2. turnon_region   the same three rows drawn separately.
  3. eff_vs_eta      efficiency vs eta from eta_probe, axis clipped to +/-3.
  4. eff_vs_phi      efficiency vs phi from eta_phi_probe, projected over the
                     |eta| < 3 rows only, so it matches the other three.

  python3 plot_year.py -t 261005_v1 -y 2024,2025
"""

import argparse
import os

import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

LEGS = [40, 60, 80, 110, 140, 200, 260, 320, 400, 450, 500, 550]
# eta_pt_probe rows: 1=-HF 2=-HE 3=HB 4=HE 5=HF
REGIONS = [(2, "-HE"), (3, "HB"), (4, "HE")]
ETA_MAX = 3.0
RCOL = {"-HE": ROOT.kGreen + 2, "HB": ROOT.kBlack, "HE": ROOT.kOrange + 7}
RMRK = {"-HE": 21, "HB": 20, "HE": 23}
COLORS = [ROOT.kBlack, ROOT.kRed + 1, ROOT.kAzure + 2, ROOT.kGreen + 2, ROOT.kMagenta + 1,
          ROOT.kOrange + 7, ROOT.kCyan + 2, ROOT.kGray + 2, ROOT.kViolet + 1,
          ROOT.kSpring - 6, ROOT.kPink + 7, ROOT.kTeal + 3]

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--tag", required=True)
parser.add_argument("-y", "--years", default="2024,2025")
parser.add_argument("-i", "--indir", default="/eos/home-y/yeo/rdf/output/hadd_files/year")
parser.add_argument("-o", "--outdir", default="/eos/home-y/yeo/rdf/plots")
parser.add_argument("-p", "--pairing", default="obj", choices=["obj", "match"])
parser.add_argument("-r", "--rebin", type=int, default=2)
parser.add_argument("-l", "--level", type=float, default=0.995)
parser.add_argument("--min-den", type=float, default=20)
parser.add_argument("--subdir", default="year")
parser.add_argument("--format", default="png,pdf")
args = parser.parse_args()

NUM = {"obj": "objnum", "match": "objden"}[args.pairing]
KEEP = []


def as_counts(h, name):
    ax = h.GetXaxis()
    out = ROOT.TH1D(name, "", h.GetNbinsX(), ax.GetXmin(), ax.GetXmax())
    out.SetDirectory(0)
    out.Sumw2(ROOT.kFALSE)
    for b in range(0, h.GetNbinsX() + 2):
        out.SetBinContent(b, round(h.GetBinContent(b)))
    out.SetEntries(h.GetEntries())
    return out


def projy(h2, b1, b2, name):
    p = h2.ProjectionY(name + "_py", b1, b2)
    p.SetDirectory(0)
    return as_counts(p, name)


def make(num, den, rebin):
    if rebin > 1:
        num.Rebin(rebin); den.Rebin(rebin)
    if any(num.GetBinContent(b) > den.GetBinContent(b) for b in range(0, den.GetNbinsX() + 2)):
        return None
    e = ROOT.TEfficiency(num, den)
    e.SetStatisticOption(ROOT.TEfficiency.kFCP)
    e.SetConfidenceLevel(0.683)
    KEEP.extend([num, den, e])
    return e


def graph(eff, den):
    g = ROOT.TGraphAsymmErrors()
    ax = den.GetXaxis()
    for b in range(1, den.GetNbinsX() + 1):
        if den.GetBinContent(b) < args.min_den:
            continue
        i = g.GetN()
        g.SetPoint(i, ax.GetBinCenter(b), eff.GetEfficiency(b))
        g.SetPointError(i, ax.GetBinWidth(b) / 2., ax.GetBinWidth(b) / 2.,
                        eff.GetEfficiencyErrorLow(b), eff.GetEfficiencyErrorUp(b))
    KEEP.append(g)
    return g


def asymptote(eff, den, from_pt):
    n = d = 0.
    from_pt = min(from_pt, 0.6 * den.GetXaxis().GetXmax())
    for b in range(1, den.GetNbinsX() + 1):
        if den.GetBinContent(b) < args.min_den or den.GetXaxis().GetBinLowEdge(b) < from_pt:
            continue
        d += den.GetBinContent(b); n += den.GetBinContent(b) * eff.GetEfficiency(b)
    return (n / d) if d else None


def plateau(eff, den, level, window=5):
    good = [b for b in range(1, den.GetNbinsX() + 1) if den.GetBinContent(b) >= args.min_den]
    for i, b in enumerate(good):
        block = good[i:i + window]
        if len(block) < min(window, len(good) - i):
            break
        if all(eff.GetEfficiency(bb) >= level for bb in block):
            return den.GetXaxis().GetBinLowEdge(b)
    return None


_CN = [0]


def canvas(xtitle, xlo, xhi, ncol, w=900, h=640):
    # 두 캔버스를 동시에 열어두므로 이름이 겹치면 ROOT 가 앞엣것을 지운다
    _CN[0] += 1
    c = ROOT.TCanvas("c%d" % _CN[0], "", w, h)
    c.SetGridx(); c.SetGridy(); c.SetTicks(1, 1); c.SetLeftMargin(0.12)
    fr = ROOT.TH1F("fr%d" % _CN[0], ";%s;efficiency" % xtitle, 1, xlo, xhi)
    fr.SetDirectory(0); fr.SetMinimum(0.); fr.SetMaximum(1.4); fr.Draw()
    lg = ROOT.TLegend(0.13, 0.74, 0.90, 0.89)
    lg.SetNColumns(ncol); lg.SetBorderSize(0); lg.SetFillStyle(0); lg.SetTextSize(0.027)
    KEEP.extend([fr, lg])
    return c, lg


def finish(c, lg, year, txt, path, level_line=None, xlo=None, xhi=None):
    c.cd()      # 두 캔버스를 동시에 열어두므로 반드시 대상 캔버스를 활성화한다
    if level_line is not None:
        ln = ROOT.TLine(xlo, level_line, xhi, level_line)
        ln.SetLineStyle(2); ln.SetLineColor(ROOT.kRed + 1); ln.Draw(); KEEP.append(ln)
    lg.Draw()
    t = ROOT.TLatex(); t.SetNDC(); t.SetTextFont(42); t.SetTextSize(0.040)
    t.DrawLatex(0.12, 0.93, "#bf{CMS} #it{Preliminary}")
    t.SetTextSize(0.033)
    t.DrawLatex(0.55, 0.93, "%s   %s" % (year, txt))
    for ext in args.format.split(","):
        c.SaveAs("%s.%s" % (path, ext))
    c.Close()


def main():
    rows = []
    for year in [y for y in args.years.split(",") if y]:
        path = os.path.join(args.indir, "%s_%s.root" % (year, args.tag))
        if not os.path.isfile(path):
            print("없음: %s" % path); continue
        f = ROOT.TFile.Open(path)
        out = os.path.join(args.outdir, args.tag, args.subdir, year)
        os.makedirs(out, exist_ok=True)
        print("=== %s" % year)

        # --- 1) |eta|<3 통합 turn-on : 모든 leg 한 장에 ---
        c, lg = canvas("offline probe jet p_{T} [GeV]", 0., 1000., 4)
        for k, L in enumerate(LEGS):
            d2 = f.Get("h_pfjet%d_den_eta_pt_probe" % L)
            n2 = f.Get("h_pfjet%d_%s_eta_pt_probe" % (L, NUM))
            if not d2 or not n2:
                continue
            den = projy(d2, 2, 4, "d%s%d" % (year, L))
            num = projy(n2, 2, 4, "n%s%d" % (year, L))
            eff = make(num, den, args.rebin)
            if eff is None:
                continue
            g = graph(eff, den)
            g.SetMarkerStyle(20 + (k % 8)); g.SetMarkerSize(0.7)
            g.SetLineColor(COLORS[k % 12]); g.SetMarkerColor(COLORS[k % 12])
            g.Draw("P SAME"); lg.AddEntry(g, "PFJet%d" % L, "lp")
            a = asymptote(eff, den, 2. * L); p = plateau(eff, den, args.level)
            rows.append((year, L, "|eta|<3", den.Integral(), a, p))
            print("  leg %-4d |eta|<3  den %10.0f  eff_inf %s  plateau %s" % (
                L, den.Integral(), ("%.4f" % a) if a else "-", ("%.0f GeV" % p) if p else "-"))
        finish(c, lg, year, "turn-on, |#eta|<3", os.path.join(out, "turnon_eta3_all"),
               args.level, 0., 1000.)

        # --- 2) leg 마다 구간별 turn-on ---
        for L in LEGS:
            d2 = f.Get("h_pfjet%d_den_eta_pt_probe" % L)
            n2 = f.Get("h_pfjet%d_%s_eta_pt_probe" % (L, NUM))
            if not d2 or not n2:
                continue
            xmax = min(1000., max(200., 3. * L))
            c, lg = canvas("offline probe jet p_{T} [GeV]", 0., xmax, 3)
            for ib, rname in REGIONS:
                den = projy(d2, ib, ib, "d%s%d%s" % (year, L, rname))
                num = projy(n2, ib, ib, "n%s%d%s" % (year, L, rname))
                if den.Integral() < args.min_den:
                    continue
                eff = make(num, den, args.rebin)
                if eff is None:
                    continue
                g = graph(eff, den)
                g.SetMarkerStyle(RMRK[rname]); g.SetMarkerSize(0.8)
                g.SetLineColor(RCOL[rname]); g.SetMarkerColor(RCOL[rname])
                g.Draw("P SAME")
                a = asymptote(eff, den, 2. * L); p = plateau(eff, den, args.level)
                lg.AddEntry(g, "%s  #varepsilon_{#infty}=%s" % (
                    rname, ("%.4f" % a) if a else "-"), "lp")
                rows.append((year, L, rname, den.Integral(), a, p))
            finish(c, lg, year, "PFJet%d  turn-on by region" % L,
                   os.path.join(out, "turnon_region_eff%d" % L), args.level, 0., xmax)

        # --- 3) eff vs eta, 4) eff vs phi (|eta|<3 행만) ---
        ce, lge = canvas("probe jet #eta", -ETA_MAX, ETA_MAX, 4)
        cp, lgp = canvas("probe jet #phi", -3.1416, 3.1416, 4)
        for k, L in enumerate(LEGS):
            de = f.Get("h_pfjet%d_den_eta_probe" % L)
            ne = f.Get("h_pfjet%d_%s_eta_probe" % (L, NUM))
            if de and ne:
                nn = as_counts(ne, "ne%s%d" % (year, L))
                dd = as_counts(de, "de%s%d" % (year, L))
                eff = make(nn, dd, args.rebin)
                if eff is not None:
                    ce.cd()
                    g = graph(eff, dd)
                    g.SetMarkerStyle(20 + (k % 8)); g.SetMarkerSize(0.6)
                    g.SetLineColor(COLORS[k % 12]); g.SetMarkerColor(COLORS[k % 12])
                    g.Draw("P SAME"); lge.AddEntry(g, "PFJet%d" % L, "lp")
            d2 = f.Get("h_pfjet%d_den_eta_phi_probe" % L)
            n2 = f.Get("h_pfjet%d_%s_eta_phi_probe" % (L, NUM))
            if d2 and n2:
                ax = d2.GetXaxis()
                b1, b2 = ax.FindBin(-ETA_MAX + 1e-3), ax.FindBin(ETA_MAX - 1e-3)
                den = projy(d2, b1, b2, "dp%s%d" % (year, L))
                num = projy(n2, b1, b2, "np%s%d" % (year, L))
                eff = make(num, den, args.rebin)
                if eff is not None:
                    cp.cd()
                    g = graph(eff, den)
                    g.SetMarkerStyle(20 + (k % 8)); g.SetMarkerSize(0.6)
                    g.SetLineColor(COLORS[k % 12]); g.SetMarkerColor(COLORS[k % 12])
                    g.Draw("P SAME"); lgp.AddEntry(g, "PFJet%d" % L, "lp")
        finish(ce, lge, year, "eff vs #eta (|#eta|<3)", os.path.join(out, "eff_vs_eta"))
        finish(cp, lgp, year, "eff vs #phi (|#eta|<3)", os.path.join(out, "eff_vs_phi"))
        f.Close()

    csv = os.path.join(args.outdir, args.tag, args.subdir, "summary_year.csv")
    with open(csv, "w") as o:
        o.write("year,leg,region,den,eff_asymptote,plateau_GeV\n")
        for r in rows:
            o.write("%s,%d,%s,%.0f,%s,%s\n" % (
                r[0], r[1], r[2], r[3],
                ("%.4f" % r[4]) if r[4] else "", ("%.0f" % r[5]) if r[5] else ""))
    print("\nplots   -> %s/<year>/" % os.path.join(args.outdir, args.tag, args.subdir))
    print("summary -> %s" % csv)


if __name__ == "__main__":
    main()
