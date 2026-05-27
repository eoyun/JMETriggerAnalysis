#!/usr/bin/env python3
"""Draw representative plots from harvest/menu_run.root"""

import ROOT, os
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetFrameLineWidth(1)

INFILE = 'harvest/menu_run.root'
OUTDIR = 'harvest/plots'
os.makedirs(OUTDIR, exist_ok=True)

f = ROOT.TFile.Open(INFILE)
d = f.Get('NoSelection')

COLORS = [ROOT.kBlack, ROOT.kRed+1, ROOT.kBlue+1, ROOT.kGreen+2, ROOT.kMagenta+1]
MARKERS = [20, 21, 22, 23, 33]

def style_th1(h, color, marker=20, lw=2):
    h.SetLineColor(color); h.SetMarkerColor(color)
    h.SetMarkerStyle(marker); h.SetMarkerSize(0.9)
    h.SetLineWidth(lw)

def style_graph(g, color, marker=20):
    g.SetLineColor(color); g.SetMarkerColor(color)
    g.SetMarkerStyle(marker); g.SetMarkerSize(0.9)
    g.SetLineWidth(2)

def save(c, name):
    for ext in ['pdf', 'png']:
        c.SaveAs(f'{OUTDIR}/{name}.{ext}')
    print(f'  saved: {OUTDIR}/{name}.pdf')

def legend(x1, y1, x2, y2):
    lg = ROOT.TLegend(x1, y1, x2, y2)
    lg.SetBorderSize(0); lg.SetFillStyle(0)
    lg.SetTextSize(0.038)
    return lg

def cms_label(pad, extra='Phase-2 Simulation'):
    pad.cd()
    t = ROOT.TLatex()
    t.SetNDC(); t.SetTextFont(62); t.SetTextSize(0.048)
    t.DrawLatex(0.13, 0.92, 'CMS')
    t.SetTextFont(52); t.SetTextSize(0.038)
    t.DrawLatex(0.26, 0.92, extra)

# ──────────────────────────────────────────────────────────────
# 1. Jet matching efficiency vs gen pT  (3 reco collections)
# ──────────────────────────────────────────────────────────────
print('Plot 1: jet matching efficiency vs pT')
c = ROOT.TCanvas('c1','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)

names = [
    ('hltPF',         'AK4 PF'),
    ('hltPFPuppi',    'AK4 PF PUPPI'),
    ('hltPFPuppiCorr','AK4 PF PUPPI (corr)'),
]
frame = ROOT.TH1F('fr1','',1,0,500)
frame.GetXaxis().SetTitle('Gen jet p_{T} (GeV)')
frame.GetYaxis().SetTitle('Matching efficiency')
frame.GetYaxis().SetRangeUser(0, 1.12)
frame.Draw()

lg = legend(0.55, 0.18, 0.90, 0.42)
for i,(key,label) in enumerate(names):
    gname = f'ak4GenJetsNoNu_EtaIncl_MatchedTo{key}_pt_eff'
    g = d.Get(gname)
    if not g: continue
    style_graph(g, COLORS[i], MARKERS[i])
    g.Draw('P SAME')
    lg.AddEntry(g, label, 'lp')
lg.Draw()
cms_label(c)
save(c, 'jet_matching_eff_vs_pt')
del c, frame

# ──────────────────────────────────────────────────────────────
# 2. Jet matching efficiency vs eta
# ──────────────────────────────────────────────────────────────
print('Plot 2: jet matching efficiency vs eta')
c = ROOT.TCanvas('c2','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)

frame = ROOT.TH1F('fr2','',1,-5,5)
frame.GetXaxis().SetTitle('Gen jet #eta')
frame.GetYaxis().SetTitle('Matching efficiency')
frame.GetYaxis().SetRangeUser(0, 1.12)
frame.Draw()

lg = legend(0.16, 0.18, 0.52, 0.42)
for i,(key,label) in enumerate(names):
    gname = f'ak4GenJetsNoNu_EtaIncl_MatchedTo{key}_eta_eff'
    g = d.Get(gname)
    if not g: continue
    style_graph(g, COLORS[i], MARKERS[i])
    g.Draw('P SAME')
    lg.AddEntry(g, label, 'lp')
lg.Draw()
cms_label(c)
save(c, 'jet_matching_eff_vs_eta')
del c, frame

# ──────────────────────────────────────────────────────────────
# 3. MET response (reco/gen) vs gen MET pT
# ──────────────────────────────────────────────────────────────
print('Plot 3: MET response vs gen MET pT')
c = ROOT.TCanvas('c3','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)

met_names = [
    ('hltPFMET',           'PF MET'),
    ('hltPFPuppiMET',      'PF PUPPI MET'),
    ('hltPFPuppiMETTypeOne','PF PUPPI TypeI MET'),
]
frame = ROOT.TH1F('fr3','',1,0,600)
frame.GetXaxis().SetTitle('Gen MET p_{T} (GeV)')
frame.GetYaxis().SetTitle('MET response (reco/gen)')
frame.GetYaxis().SetRangeUser(0, 2.0)
frame.Draw()

line = ROOT.TLine(0, 1, 600, 1)
line.SetLineStyle(2); line.SetLineColor(ROOT.kGray+1)
line.Draw()

lg = legend(0.16, 0.65, 0.60, 0.88)
for i,(key,label) in enumerate(met_names):
    hname = f'{key}_pt_overGEN_Mean_wrt_GEN_pt'
    h = d.Get(hname)
    if not h: continue
    style_th1(h, COLORS[i], MARKERS[i])
    h.Draw('E SAME')
    lg.AddEntry(h, label, 'lp')
lg.Draw()
cms_label(c)
save(c, 'met_response_vs_genMET')
del c, frame

# ──────────────────────────────────────────────────────────────
# 4. MET resolution vs gen MET pT
# ──────────────────────────────────────────────────────────────
print('Plot 4: MET resolution vs gen MET pT')
c = ROOT.TCanvas('c4','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)

frame = ROOT.TH1F('fr4','',1,0,600)
frame.GetXaxis().SetTitle('Gen MET p_{T} (GeV)')
frame.GetYaxis().SetTitle('MET resolution (#sigma/mean)')
frame.GetYaxis().SetRangeUser(0, 1.0)
frame.Draw()

lg = legend(0.40, 0.55, 0.88, 0.78)
for i,(key,label) in enumerate(met_names):
    hname = f'{key}_pt_overGEN_RMSOverMean_wrt_GEN_pt'
    h = d.Get(hname)
    if not h: continue
    style_th1(h, COLORS[i], MARKERS[i])
    h.Draw('E SAME')
    lg.AddEntry(h, label, 'lp')
lg.Draw()
cms_label(c)
save(c, 'met_resolution_vs_genMET')
del c, frame

# ──────────────────────────────────────────────────────────────
# 5. Gen jet pT spectrum + HLT jet pT spectra
# ──────────────────────────────────────────────────────────────
print('Plot 5: jet pT spectra')
c = ROOT.TCanvas('c5','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)
c.SetLogy()

jet_spec = [
    ('ak4GenJetsNoNu_EtaIncl_pt',              'Gen AK4 jets'),
    ('hltAK4PFJets_EtaIncl_pt',               'AK4 PF jets'),
    ('hltAK4PFPuppiJets_EtaIncl_pt',          'AK4 PF PUPPI jets'),
    ('hltAK4PFPuppiJetsCorrected_EtaIncl_pt', 'AK4 PF PUPPI (corr)'),
]
frame = ROOT.TH1F('fr5','',1,0,500)
frame.GetXaxis().SetTitle('Jet p_{T} (GeV)')
frame.GetYaxis().SetTitle('Entries / bin')
frame.GetYaxis().SetRangeUser(0.5, 1e6)
frame.Draw()

lg = legend(0.45, 0.55, 0.88, 0.88)
for i,(hname,label) in enumerate(jet_spec):
    h = d.Get(hname)
    if not h: continue
    style_th1(h, COLORS[i], MARKERS[i])
    h.Draw('HIST SAME')
    lg.AddEntry(h, label, 'l')
lg.Draw()
cms_label(c)
save(c, 'jet_pt_spectra')
del c, frame

# ──────────────────────────────────────────────────────────────
# 6. MET pT distributions (gen + reco)
# ──────────────────────────────────────────────────────────────
print('Plot 6: MET pT distributions')
c = ROOT.TCanvas('c6','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)
c.SetLogy()

met_dist = [
    ('genMETTrue_pt',          'Gen MET'),
    ('hltPFMET_pt',            'PF MET'),
    ('hltPFPuppiMET_pt',       'PF PUPPI MET'),
    ('hltPFPuppiMETTypeOne_pt','PF PUPPI TypeI MET'),
]
frame = ROOT.TH1F('fr6','',1,0,600)
frame.GetXaxis().SetTitle('MET p_{T} (GeV)')
frame.GetYaxis().SetTitle('Entries / bin')
frame.GetYaxis().SetRangeUser(0.5, 1e5)
frame.Draw()

lg = legend(0.40, 0.55, 0.88, 0.88)
for i,(hname,label) in enumerate(met_dist):
    h = d.Get(hname)
    if not h: continue
    style_th1(h, COLORS[i], MARKERS[i])
    h.Draw('HIST SAME')
    lg.AddEntry(h, label, 'l')
lg.Draw()
cms_label(c)
save(c, 'met_pt_distributions')
del c, frame

# ──────────────────────────────────────────────────────────────
# 7. HT: gen vs reco comparison
# ──────────────────────────────────────────────────────────────
print('Plot 7: HT distributions')
c = ROOT.TCanvas('c7','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)
c.SetLogy()

ht_dist = [
    ('ak4GenJetsNoNu_EtaIncl_HT',              'Gen HT'),
    ('hltAK4PFPuppiJetsCorrected_EtaIncl_HT',  'HLT HT (PF PUPPI corr)'),
    ('hltAK4PFPuppiJets_EtaIncl_HT',           'HLT HT (PF PUPPI)'),
    ('hltAK4PFJets_EtaIncl_HT',                'HLT HT (PF)'),
]
frame = ROOT.TH1F('fr7','',1,0,2000)
frame.GetXaxis().SetTitle('H_{T} (GeV)')
frame.GetYaxis().SetTitle('Entries / bin')
frame.GetYaxis().SetRangeUser(0.5, 1e5)
frame.Draw()

lg = legend(0.40, 0.55, 0.88, 0.88)
for i,(hname,label) in enumerate(ht_dist):
    h = d.Get(hname)
    if not h: continue
    style_th1(h, COLORS[i], MARKERS[i])
    h.Draw('HIST SAME')
    lg.AddEntry(h, label, 'l')
lg.Draw()
cms_label(c)
save(c, 'ht_distributions')
del c, frame

# ──────────────────────────────────────────────────────────────
# 8. Jet pT response (reco/gen) Mean vs gen pT — eta bins
# ──────────────────────────────────────────────────────────────
print('Plot 8: jet pT response vs gen pT by eta bin')
c = ROOT.TCanvas('c8','',800,600)
c.SetLeftMargin(0.14); c.SetBottomMargin(0.13)

eta_bins = [
    ('EtaIncl', '|#eta| < 5 (incl.)'),
    ('HBPt0',   'HB (|#eta| < 1.3)'),
    ('HEPt0',   'HE (1.3 < |#eta| < 3.0)'),
    ('HFPt0',   'HF (3.0 < |#eta| < 5.0)'),
]
frame = ROOT.TH1F('fr8','',1,0,500)
frame.GetXaxis().SetTitle('Gen jet p_{T} (GeV)')
frame.GetYaxis().SetTitle('Jet response (reco/gen), mean')
frame.GetYaxis().SetRangeUser(0, 1.4)
frame.Draw()

line2 = ROOT.TLine(0, 1, 500, 1)
line2.SetLineStyle(2); line2.SetLineColor(ROOT.kGray+1)
line2.Draw()

lg = legend(0.40, 0.18, 0.88, 0.45)
drawn = 0
for i,(ebin,elabel) in enumerate(eta_bins):
    hname = f'ak4GenJetsNoNu_{ebin}_MatchedTohltPFPuppiCorr_pt_overhltPFPuppiCorr_Mean_wrt_hltPFPuppiCorr_pt'
    h = d.Get(hname)
    if not h: continue
    style_th1(h, COLORS[i], MARKERS[i])
    h.Draw('E SAME')
    lg.AddEntry(h, f'PF PUPPI corr, {elabel}', 'lp')
    drawn += 1
if drawn: lg.Draw()
cms_label(c)
save(c, 'jet_response_vs_pt_etabins')
del c, frame

f.Close()
print(f'\nAll plots saved to {OUTDIR}/')
