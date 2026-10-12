#!/usr/bin/env python

# Dijet tag-and-probe jet-trigger turn-on, JME POG binning conventions.
#
# Based on filterbitmatch.py. Physics selection is unchanged; what differs:
#   [A] eta-phi maps use the JME jet-veto-map grid: 82 variable eta bins
#       (calorimeter-tower aligned) x 72 uniform phi bins over [-pi, pi].
#   [B] TH2 axis order is X = eta, Y = phi, so the name matches the fill.
#       (filterbitmatch.py named them eta_phi but filled Fill(phi, eta).)
#   [C] every phi axis runs over [-pi, pi] instead of [-3.2, 3.2].
#   [D] the "40/320/500" histogram families are renamed hltpt200/320/500,
#       because the cut is on the matched HLT jet pT, not on an HLT path.
#   [E] all booked histograms are written, including the TH2s.
#   [F] every AK4 single-jet PFJet path is added as a leg, with the denominator
#       taken from the next lower path (JME prescription, arXiv:2111.10431).
#       Names: h_pfjet<thr>_{den,num,objden,objnum}_*  -- see section [10].
# 1D pT and eta binning is deliberately left as-is: fine binning is correct for
# resolving a turn-on shape (the "<50% migration" rule governs measured spectra).

import ROOT
import argparse
import LumiMask
from array import array

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", dest="filename", action="store")
parser.add_argument("-i", "--index", dest="index", action="store")
parser.add_argument("-o", "--outputdir", dest="outputdir", action="store")
parser.add_argument("-e", "--era", dest="era", action="store")
parser.add_argument("-t", "--tagcut", dest="tagcut", action="store", default="online",
                    choices=["off", "online", "full"],
                    help="tag requirement for the PFJet leg denominators: "
                         "off = none (biased, matches the old behaviour), "
                         "online = tag HLT object above the reference threshold "
                         "(default: this is what removes the bias -- the tag itself "
                         "satisfied the reference path's HLT filter), "
                         "full = additionally tag offline pT above the reference "
                         "plateau. Only covers the L1-seed loophole, which is "
                         "negligible for these thresholds; keep it as a systematic "
                         "cross-check, not as the nominal.")
parser.add_argument("-j", "--plateau", dest="plateau", action="store", default="plateau.json",
                    help="JSON with the offline plateau of each PFJet path; "
                         "falls back to built-in defaults when the file is absent")
args = parser.parse_args()

ROOT.ROOT.EnableImplicitMT()

PI = ROOT.TMath.Pi()

# JME jet veto map eta grid: 82 bins / 83 edges, HCAL trigger-tower aligned.
# Source: POG/JME/*/jetvetomaps.json.gz (Summer19UL16_V1 grid; the grid itself
# is detector geometry and stable across eras, the map contents are not).
ETA_BINS = array('d', [
    -5.191, -4.889, -4.716, -4.538, -4.363, -4.191, -4.013, -3.839, -3.664, -3.489,
    -3.314, -3.139, -2.964, -2.853, -2.650, -2.500, -2.322, -2.172, -2.043, -1.930,
    -1.830, -1.740, -1.653, -1.566, -1.479, -1.392, -1.305, -1.218, -1.131, -1.044,
    -0.957, -0.870, -0.783, -0.696, -0.609, -0.522, -0.435, -0.348, -0.261, -0.174,
    -0.087,  0.000,  0.087,  0.174,  0.261,  0.348,  0.435,  0.522,  0.609,  0.696,
     0.783,  0.870,  0.957,  1.044,  1.131,  1.218,  1.305,  1.392,  1.479,  1.566,
     1.653,  1.740,  1.830,  1.930,  2.043,  2.172,  2.322,  2.500,  2.650,  2.853,
     2.964,  3.139,  3.314,  3.489,  3.664,  3.839,  4.013,  4.191,  4.363,  4.538,
     4.716,  4.889,  5.191])
N_ETA_VETO = len(ETA_BINS) - 1   # 82
N_PHI_VETO = 72                  # uniform 2*pi/72 = 0.0872665

# 1D models: (nbins, low, high)
M_PT       = (100, 0., 1000.)
M_ETA      = (100, -5., 5.)
M_PHI      = (100, -PI, PI)
M_DPHI     = (100, 0., PI)
M_ALPHA    = (100, 0., 1.)
M_HLT_PT   = (1000, 0., 10000.)
M_HLT_ID   = (10000, 0., 10000.)

# AK4 single-jet HLT paths, ascending. Legs absent from a given NanoAOD are
# skipped at runtime, so the same script works across 2022-2025.
# TrigObj_filterBits bit 42 ("SinglePFJetX") tags the HLT jet objects of these
# paths but does NOT say which threshold fired -- hence the per-path handling below.
PFJET_LEGS = [40, 60, 80, 110, 140, 200, 260, 320, 400, 450, 500, 550]

# Per-leg histograms are probe-centric: a turn-on needs the probe spectrum, not
# a copy of every dijet observable. Each leg node also gets its eta-phi map.
LEG_VAR_NAMES = ["pt_probe", "pt_ave", "pt_tag", "eta_probe", "phi_probe"]

# Offline pT above which each path is fully efficient. Built-in fallback is the
# nominal threshold, which is provisional -- see plateau.json. Overridden by
# whatever -j points at, so re-deriving these needs no code change.
REF_PLATEAU = dict((thr, thr) for thr in PFJET_LEGS)


def load_plateau(path):
    """Merge the plateau table from a JSON file, if it was shipped with the job."""
    import json, os
    if not path or not os.path.isfile(path):
        print("plateau file '%s' not found, using built-in defaults" % path)
        return dict(REF_PLATEAU)
    with open(path) as fin:
        table = json.load(fin).get("plateau", {})
    merged = dict(REF_PLATEAU)
    merged.update(dict((int(k), v) for k, v in table.items()))
    print("plateau table from %s: %s" % (path, sorted(merged.items())))
    return merged

# (name suffix, RDF column, 1D model) -- booked for every stage
BASE_VARS = [
    ("pt_lead",   "Lead_jet",      M_PT),
    ("pt_tag",    "pT_tag",        M_PT),
    ("pt_probe",  "pT_probe",      M_PT),
    ("pt_ave",    "pT_ave",        M_PT),
    ("pt_sub",    "Sub_jet",       M_PT),
    ("phi_tag",   "tag_jet_phi",   M_PHI),
    ("phi_probe", "probe_jet_phi", M_PHI),
    ("eta_tag",   "tag_jet_eta",   M_ETA),
    ("eta_probe", "probe_jet_eta", M_ETA),
    ("phi_lead",  "Lead_jet_phi",  M_PHI),
    ("phi_sub",   "Sub_jet_phi",   M_PHI),
    ("eta_lead",  "Lead_jet_eta",  M_ETA),
    ("eta_sub",   "Sub_jet_eta",   M_ETA),
    ("dphi",      "Delta_phi",     M_DPHI),
    ("alpha",     "alpha",         M_ALPHA),
]

LEG_VARS = [v for name in LEG_VAR_NAMES for v in BASE_VARS if v[0] == name]

# additionally booked once the tag jet is HLT-matched
TAG_MATCH_VARS = [
    ("trig_pt",         "Trig_obj_pt",            M_PT),
    ("hlt_matched_pt",  "hlt_Jet_off_matched_pt", M_HLT_PT),
    ("hlt_matched_id",  "hlt_Jet_matched_id",     M_HLT_ID),
    ("hlt_matched_eta", "hlt_Jet_matched_eta",    M_ETA),
    ("hlt_matched_phi", "hlt_Jet_matched_phi",    M_PHI),
]

# additionally booked once the probe jet is HLT-matched
PROBE_MATCH_VARS = [
    ("hlt_matched_pt_probe",  "hlt_Jet_off_matched_pt_probe", M_HLT_PT),
    ("hlt_matched_id_probe",  "hlt_Jet_matched_id_probe",     M_HLT_ID),
    ("hlt_matched_eta_probe", "hlt_Jet_matched_eta_probe",    M_ETA),
    ("hlt_matched_phi_probe", "hlt_Jet_matched_phi_probe",    M_PHI),
]


def veto_map_model(name):
    """TH2 on the JME veto-map grid. X = eta (82 variable), Y = phi (72 uniform)."""
    h = ROOT.TH2D(name, ";#eta;#phi", N_ETA_VETO, ETA_BINS, N_PHI_VETO, -PI, PI)
    h.SetDirectory(0)
    return ROOT.RDF.TH2DModel(h)


def leg_denominator(node, ref, plateau, mode):
    """Sample recorded by the reference path, with the TAG responsible for it.

    Without a tag requirement the reference path may have been fired by the
    probe, which correlates the denominator with the quantity the numerator
    cuts on and biases the turn-on upwards. Cheapest and most-rejecting term
    first, so C++ && short-circuits before the vector indexing.
    """
    if ref is None:
        # Lowest leg: no lower path exists, so it references itself. The event
        # must have been taken by this path AND the tag must be the jet that
        # fired it -- the probe still carries no requirement, so it stays
        # unbiased. Dropping the path requirement (as this branch used to) lets
        # the event be recorded by any trigger; TrigObj then only holds the
        # objects of whichever single-jet paths did fire, the probe has nothing
        # to match below that event-dependent threshold, and the result is not
        # a turn-on at all: measured on 2025D it went 0.72 at 300-400 GeV, down
        # to 0.46 at 400-500, back up to 0.81 at 500-600.
        lo = PFJET_LEGS[0]
        return node.Filter("HLT_PFJet%d && hlt_Jet_off_matched_pt > %d" % (lo, lo),
                           "ref HLT_PFJet%d (tag-fired, lowest leg)" % lo)
    cuts = ["HLT_PFJet%d" % ref]
    if mode in ("online", "full"):
        cuts.append("hlt_Jet_off_matched_pt > %d" % ref)
    if mode == "full" and plateau.get(ref):
        cuts.append("pT_tag > %g" % plateau[ref])
    return node.Filter(" && ".join(cuts), "ref PFJet%d (tagcut=%s)" % (ref, mode))


def book_stage(node, prefix, varlist):
    """Book one histogram per entry in varlist plus the eta-phi map. Returns [RResultPtr]."""
    booked = []
    for suffix, column, (nbin, lo, hi) in varlist:
        name = prefix + suffix
        booked.append(node.Histo1D((name, ";" + column + ";entries", nbin, lo, hi), column))
    booked.append(node.Histo2D(veto_map_model(prefix + "eta_phi_probe"),
                               "probe_jet_eta", "probe_jet_phi"))
    return booked


def declare_struc():
    if not hasattr(ROOT, 'RDFAddArray'):
        ROOT.gInterpreter.Declare('''
        ROOT::RDF::RNode RDFAddArray(ROOT::RDF::RNode df, ROOT::RVec<double> &v, const std::string &name) 
        {
            return df.Define(name, [&](unsigned c) { return v[c]; }, {"counter"});
        }
        unsigned counter = 0;

        ''')

def analysis(filename_idx,idx,outputdir,era,tagcut="online",plateau_file="plateau.json"):
    declare_struc()
    # [1] Remote input path (XRootD)
    inputfile = "root://xrootd-cms.infn.it/"+filename_idx
    print(inputfile)
    df = ROOT.RDataFrame("Events",inputfile)
    # [2] Basic jet selections and kinematics
    df = df.Filter("nJet >= 2", "Events with at least two jets")
    df = df.Define("Lead_jet", "Jet_pt[0]")
    df = df.Define("Sub_jet", "Jet_pt[1]")
    df = df.Define("Lead_jet_phi", "Jet_phi[0]")
    df = df.Define("Sub_jet_phi", "Jet_phi[1]")
    df = df.Define("Lead_jet_eta", "Jet_eta[0]")
    df = df.Define("Sub_jet_eta", "Jet_eta[1]")
    ROOT.gInterpreter.Declare(
            """
            vector<int> random_idx(double jet_eta1, double jet_eta2){
                vector<int> tnp;
                if (abs(jet_eta1) < 1.3 && abs(jet_eta2) < 1.3){
                    int tmp = std::rand()%2;

                    tnp.push_back(tmp);
                    tnp.push_back((tmp+1)%2);
                }
                else if (abs(jet_eta1) < 1.3 && abs(jet_eta2) > 1.3) {
                    tnp.push_back(0);
                    tnp.push_back(1);
                }
                else if (abs(jet_eta1) > 1.3 && abs(jet_eta2) < 1.3) {
                    tnp.push_back(1);
                    tnp.push_back(0);
                }
                else{
                    int tmp = std::rand()%2;

                    tnp.push_back(tmp);
                    tnp.push_back((tmp+1)%2);
                }


                return tnp;
            }
            """
            )
    ROOT.gInterpreter.Declare(
            """
            // [3] Delta-phi helper for dijet selections
            double dphi(double phi1, double phi2){
                float x  = abs(phi1-phi2);
                if (x>M_PI)return 2*M_PI - x;
                else return x;
            }
            """
            )
    ROOT.gInterpreter.Declare(
            """
            static inline float deltaPhi(float a, float b) {
                // wrap into [-pi, pi]
                float d = a - b;
                constexpr float pi = 3.14159265358979323846f;
                while (d >  pi) d -= 2.0f * pi;
                while (d < -pi) d += 2.0f * pi;
                return d;
            }
            
            // [4] Returns: for each offline object i, the matched HLT index j (or -1 if none)
            std::vector<int> match_hlt_offline(
                const ROOT::VecOps::RVec<float>& hlt_eta,
                const ROOT::VecOps::RVec<float>& hlt_phi,
                const ROOT::VecOps::RVec<float>& off_eta,
                const ROOT::VecOps::RVec<float>& off_phi,
                float dr = 0.2f
            ){
                std::vector<int> matched;
                matched.reserve(off_eta.size());
            
                // basic size guards (avoid out-of-range)
                if (hlt_eta.size() != hlt_phi.size() || off_eta.size() != off_phi.size()) {
                    // return consistent shape: offline-sized vector filled with -1
                    matched.assign(off_eta.size(), -1);
                    return matched;
                }
            
                if (off_eta.empty() || hlt_eta.empty()) {
                    matched.assign(off_eta.size(), -1);
                    return matched;
                }
            
                const float dr2 = dr * dr;
            
                for (size_t i = 0; i < off_eta.size(); ++i) {
                    int best_j = -1;
                    float best_dr2 = dr2; // only accept matches strictly within dr
            
                    for (size_t j = 0; j < hlt_eta.size(); ++j) {
                        const float deta = hlt_eta[j] - off_eta[i];
                        const float dphi = deltaPhi(hlt_phi[j], off_phi[i]);
                        const float d2   = deta * deta + dphi * dphi;
            
                        if (d2 < best_dr2) {
                            best_dr2 = d2;
                            best_j = static_cast<int>(j);
                        }
                    }
            
                    matched.push_back(best_j);
                }
            
                return matched;
            }
            """

            )
    df = df.Define("Delta_phi","dphi(Jet_phi[0],Jet_phi[1])")
    df = df.Define("alpha","nJet==2 ? 0 : 2 * Jet_pt[2]/(Jet_pt[0]+Jet_pt[1])")
    bitmask_42 = 1 << 42
    print(bitmask_42)
    # [5] Filter HLT jets by filter bit and a pT threshold
    df = df.Define("Trig_obj_pt",f"TrigObj_pt[TrigObj_id == 1 && (TrigObj_filterBits & {bitmask_42}) != 0]")
    df = df.Define("hlt_Jet_eta",f"TrigObj_eta[TrigObj_id == 1 && (TrigObj_filterBits & {bitmask_42}) != 0]")
    df = df.Define("hlt_Jet_phi",f"TrigObj_phi[TrigObj_id == 1 && (TrigObj_filterBits & {bitmask_42}) != 0]")
    df = df.Define("hlt_Jet_id",f"TrigObj_filterBits[TrigObj_id==1&& (TrigObj_filterBits & {bitmask_42})  != 0]")
    df = df.Define("Jet_hlt_matched_index","match_hlt_offline(hlt_Jet_eta,hlt_Jet_phi,Jet_eta,Jet_phi)")
    # [6] Apply certified lumisections using a vector mask
    LumiMask_ = LumiMask.lumimask(era=era)(
        df.Take[ROOT.UInt_t]("run").GetValue(),
        df.Take[ROOT.UInt_t]("luminosityBlock").GetValue()
    )
    df = df.Define("counter","counter++")
    Lumi_arr = ROOT.VecOps.AsRVec(LumiMask_)
    df = ROOT.RDFAddArray(ROOT.RDF.AsRNode(df),Lumi_arr,"LumiMask")
    df = df.Filter("LumiMask > 0.5","")
    df = df.Define("tnp","random_idx(Lead_jet_eta,Sub_jet_eta)")
    # [7] Tag-and-probe dijet definitions
    df = df.Define("pT_ave","(Lead_jet + Sub_jet)/2")
    df = df.Define("tag_jet_eta","Jet_eta[tnp[0]]")
    df = df.Define("tag_jet_phi","Jet_phi[tnp[0]]")
    df = df.Define("pT_tag","Jet_pt[tnp[0]]")
    df = df.Define("probe_jet_eta","Jet_eta[tnp[1]]")
    df = df.Define("probe_jet_phi","Jet_phi[tnp[1]]")
    df = df.Define("pT_probe","Jet_pt[tnp[1]]")
    # [8] Common dijet base: tag jet matched to a SinglePFJet HLT object,
    #     back-to-back, third-jet activity vetoed, one jet in the barrel.
    #     No HLT path requirement here -- the legs below add their own.
    df_dijet = df.Filter("Jet_hlt_matched_index[tnp[0]]!=-1","")
    df_dijet = df_dijet.Define("hlt_Jet_off_matched_pt","Trig_obj_pt[Jet_hlt_matched_index[tnp[0]]]")
    df_dijet = df_dijet.Define("hlt_Jet_matched_id","hlt_Jet_id[Jet_hlt_matched_index[tnp[0]]]")
    df_dijet = df_dijet.Define("hlt_Jet_matched_eta","hlt_Jet_eta[Jet_hlt_matched_index[tnp[0]]]")
    df_dijet = df_dijet.Define("hlt_Jet_matched_phi","hlt_Jet_phi[Jet_hlt_matched_index[tnp[0]]]")
    df_dijet = df_dijet.Filter("Delta_phi>2.7","")
    df_dijet = df_dijet.Filter("alpha < 0.1","")
    df_dijet = df_dijet.Filter("abs(Sub_jet_eta) < 1.3 || abs(Lead_jet_eta) < 1.3","")

    # [9] Legacy stages, identical selection to filterbitmatch.py:
    #     reference trigger HLT_PFJet110, then cuts on the HLT jet pT matched
    #     to the PROBE. Those are online-pT thresholds, NOT path names.
    df_after = df_dijet.Filter("HLT_PFJet110","")
    df_after_match = df_after.Filter("Jet_hlt_matched_index[tnp[1]]!=-1","")
    df_after_match = df_after_match.Define("hlt_Jet_off_matched_pt_probe","Trig_obj_pt[Jet_hlt_matched_index[tnp[1]]]")
    df_after_match = df_after_match.Define("hlt_Jet_matched_id_probe","hlt_Jet_id[Jet_hlt_matched_index[tnp[1]]]")
    df_after_match = df_after_match.Define("hlt_Jet_matched_eta_probe","hlt_Jet_eta[Jet_hlt_matched_index[tnp[1]]]")
    df_after_match = df_after_match.Define("hlt_Jet_matched_phi_probe","hlt_Jet_phi[Jet_hlt_matched_index[tnp[1]]]")
    df_hltpt200 = df_after_match.Filter("hlt_Jet_off_matched_pt_probe > 200","")
    df_hltpt320 = df_after_match.Filter("hlt_Jet_off_matched_pt_probe > 320","")
    df_hltpt500 = df_after_match.Filter("hlt_Jet_off_matched_pt_probe > 500","")

    stages = [
        ("h_",                 df,             BASE_VARS),
        ("h_after_",           df_after,       BASE_VARS + TAG_MATCH_VARS),
        ("h_after_hltpt200_",  df_hltpt200,    BASE_VARS + TAG_MATCH_VARS + PROBE_MATCH_VARS),
        ("h_after_hltpt320_",  df_hltpt320,    BASE_VARS + TAG_MATCH_VARS + PROBE_MATCH_VARS),
        ("h_after_hltpt500_",  df_hltpt500,    BASE_VARS + TAG_MATCH_VARS + PROBE_MATCH_VARS),
    ]

    # [10] Single-jet PFJet legs, JME prescription (arXiv:2111.10431):
    #      "The efficiency of each trigger is determined from the data set
    #       recorded by the next single-jet trigger (with lower but closest
    #       threshold), except for the most inclusive trigger."
    #      The lowest available leg has no lower path; its denominator is the
    #      tag-and-probe sample itself (tag matched to a SinglePFJet object).
    #
    #      Two numerators per leg, because CMS HLT prescales are deterministic
    #      counters, not random draws: adjacent prescaled paths accept almost
    #      disjoint event sets (measured on one 2022C file: PFJet40 && PFJet60
    #      fires 0 times in 1.14M events), so the event-level path AND is empty
    #      wherever both legs are prescaled. It stays valid for the unprescaled
    #      high legs (450/500/550).
    #
    #        _den_    / _num_     event-level: reference path fired / + this path fired
    #        _objden_ / _objnum_  object-level: probe matched to a SinglePFJet HLT
    #                             object / + that object above this threshold.
    #                             Prescale-immune, since the HLT jet was stored by
    #                             the lower path that did fire. Use this for turn-ons.
    plateau = load_plateau(plateau_file)
    available = set(str(c) for c in df.GetColumnNames())
    legs = [thr for thr in PFJET_LEGS if ("HLT_PFJet%d" % thr) in available]
    missing = [thr for thr in PFJET_LEGS if thr not in legs]
    if missing:
        print("PFJet legs absent from this file, skipped: %s" % missing)

    leg_reference = []
    for i, thr in enumerate(legs):
        ref = legs[i-1] if i > 0 else None
        den = leg_denominator(df_dijet, ref, plateau, tagcut)
        num = den.Filter("HLT_PFJet%d" % thr, "HLT_PFJet%d" % thr)

        probe_pt = "probe_hlt_pt_%d" % thr
        objden = den.Filter("Jet_hlt_matched_index[tnp[1]]!=-1", "probe matched (leg %d)" % thr)
        objden = objden.Define(probe_pt, "Trig_obj_pt[Jet_hlt_matched_index[tnp[1]]]")
        objnum = objden.Filter("%s > %d" % (probe_pt, thr), "probe HLT pT > %d" % thr)

        stages.append(("h_pfjet%d_den_"    % thr, den,    LEG_VARS))
        if ref is not None:
            # lowest leg: its denominator already requires this path, so the
            # event-level numerator would be identical to it (efficiency == 1)
            stages.append(("h_pfjet%d_num_" % thr, num,    LEG_VARS))
        stages.append(("h_pfjet%d_objden_" % thr, objden, LEG_VARS))
        stages.append(("h_pfjet%d_objnum_" % thr, objnum, LEG_VARS))
        leg_reference.append("%d:%s" % (thr, "tagprobe" if ref is None else str(ref)))
    print("PFJet legs booked (leg:reference): %s" % ",".join(leg_reference))

    booked = []
    for prefix, node, varlist in stages:
        booked += book_stage(node, prefix, varlist)

    # [11] One event loop happens here, then everything booked is written.
    fOUT = ROOT.TFile.Open(outputdir+"/output_hist"+str(idx)+".root","RECREATE")
    for h in booked:
        h.Write()
    # leg -> reference-path map, so downstream code does not have to guess
    ROOT.TNamed("pfjet_leg_reference", ",".join(leg_reference)).Write()
    ROOT.TNamed("pfjet_tagcut", "mode=%s;plateau=%s" % (
        tagcut, ",".join("%d:%s" % (k, plateau[k]) for k in sorted(plateau)))).Write()
    print("wrote %d histograms to %s" % (len(booked), fOUT.GetName()))
    fOUT.Close()


if __name__ == "__main__":

    filename = args.filename+".out"
    outputdir = args.outputdir
    index = int(args.index)
    era = int(args.era)
    f = open(filename,'r')
    filelist = []
    for line in f:
        line = line.strip()
        filelist.append(line)
    analysis(filelist[index],index,outputdir,era,args.tagcut,args.plateau)
