#!/usr/bin/env python

import ROOT
import argparse
import LumiMask

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", dest="filename", action="store") 
parser.add_argument("-i", "--index", dest="index", action="store") 
parser.add_argument("-o", "--outputdir", dest="outputdir", action="store") 
parser.add_argument("-e", "--era", dest="era", action="store", default="2024")
args = parser.parse_args()

ROOT.ROOT.EnableImplicitMT()

def declare_struc():
    if not hasattr(ROOT, 'RDFAddArray'):
        ROOT.gInterpreter.Declare('''
        ROOT::RDF::RNode RDFAddArray(ROOT::RDF::RNode df, ROOT::RVec<double> &v, const std::string &name) 
        {
            return df.Define(name, [&](unsigned c) { return v[c]; }, {"counter"});
        }
        unsigned counter = 0;

        ''')

def analysis(filename_idx,idx,outputdir):
    declare_struc()
def analysis(filename_idx,idx,outputdir):
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
            vector<int> random_idx(){
                vector<int> tnp;
                tnp.push_back(0);
                tnp.push_back(1);
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
            // [4] Match each offline jet to the nearest HLT jet within deltaR
            vector<int> match_hlt_offline ( ROOT::VecOps::RVec<float> hlt_eta,ROOT::VecOps::RVec<float> hlt_phi,ROOT::VecOps::RVec<float> off_eta,ROOT::VecOps::RVec<float> off_phi){
                vector<int> hlt_matched;
                int off_index;
                float dr=0.2;
                if  (off_eta.size()==0 || hlt_eta.size()==0) {
                    hlt_matched.push_back(-1);
                    return hlt_matched;
                }
                for (int i=0; i< off_eta.size();i++){
                    off_index = -1;
                    float best_dr2 = dr * dr;
                    for (int j=0;j<hlt_eta.size();j++){
                        float dphi = abs(hlt_phi[j]-off_phi[i]);
                        if (dphi > M_PI) {
                            dphi = 2 * M_PI - dphi;
                        }
                        float dr2 = pow(hlt_eta[j]-off_eta[i],2) + pow(dphi,2);
                        if (dr2 < best_dr2){
                            best_dr2 = dr2;
                            off_index = j;
                        }
                    }
                    hlt_matched.push_back(off_index);
                }
                return hlt_matched;
            }
            """

            )
    ROOT.gInterpreter.Declare(
            """
            // [5] Safe indexing for matched HLT arrays
            float get_or_default(ROOT::VecOps::RVec<float> values, int index, float fallback) {
                if (index < 0 || index >= static_cast<int>(values.size())) {
                    return fallback;
                }
                return values[index];
            }
            int get_or_default_int(ROOT::VecOps::RVec<int> values, int index, int fallback) {
                if (index < 0 || index >= static_cast<int>(values.size())) {
                    return fallback;
                }
                return values[index];
            }
            """
            )
    df = df.Define("Delta_phi","dphi(Jet_phi[0],Jet_phi[1])")
    df = df.Define("alpha","nJet==2 ? 0 : 2 * Jet_pt[2]/(Jet_pt[0]+Jet_pt[1])")
    # [6] HLT jet collections (all jet-type trigger objects)
    df = df.Define("Trig_obj_pt","TrigObj_pt[TrigObj_id == 1 ]")
    df = df.Define("hlt_Jet_eta","TrigObj_eta[TrigObj_id == 1]")
    df = df.Define("hlt_Jet_phi","TrigObj_phi[TrigObj_id == 1]")
    df = df.Define("hlt_Jet_id","TrigObj_filterBits[TrigObj_id==1]")
    df = df.Define("Jet_hlt_matched_index","match_hlt_offline(hlt_Jet_eta,hlt_Jet_phi,Jet_eta,Jet_phi)")
    df = df.Define("hlt_Jet_off_matched_pt","get_or_default(Trig_obj_pt, Jet_hlt_matched_index[0], -1.0)")
    df = df.Define("hlt_Jet_matched_id","get_or_default_int(hlt_Jet_id, Jet_hlt_matched_index[0], -1)")
    df = df.Define("hlt_Jet_matched_eta","get_or_default(hlt_Jet_eta, Jet_hlt_matched_index[0], -99.0)")
    df = df.Define("hlt_Jet_matched_phi","get_or_default(hlt_Jet_phi, Jet_hlt_matched_index[0], -99.0)")
    # [7] Apply certified lumisections
    lumi_mask = LumiMask.lumimask(int(args.era))
    lumi_values = lumi_mask(
        df.Take[ROOT.UInt_t]("run").GetValue(),
        df.Take[ROOT.UInt_t]("luminosityBlock").GetValue()
    )
    df = df.Define("counter","counter++")
    lumi_arr = ROOT.VecOps.AsRVec(lumi_values)
    df = ROOT.RDFAddArray(ROOT.RDF.AsRNode(df), lumi_arr, "LumiMask")
    df = df.Filter("LumiMask > 0.5","")
    df = df.Define("tnp","random_idx()")
    # [8] Tag-and-probe dijet definitions
    df = df.Define("pT_ave","(Lead_jet + Sub_jet)/2")
    df = df.Define("tag_jet_eta","Jet_eta[tnp[0]]")
    df = df.Define("tag_jet_phi","Jet_phi[tnp[0]]")
    df = df.Define("pT_tag","Jet_pt[tnp[0]]")
    df = df.Define("probe_jet_eta","Jet_eta[tnp[1]]")
    df = df.Define("probe_jet_phi","Jet_phi[tnp[1]]")
    df = df.Define("pT_probe","Jet_pt[tnp[1]]")
    df = df.Filter("Jet_hlt_matched_index[tnp[0]]!=-1","") 
    df = df.Filter("Delta_phi>2.7","") 
    df = df.Filter("alpha < 0.1","") 
    df = df.Filter("abs(Lead_jet_eta) < 1.3","")
    df = df.Filter("abs(Sub_jet_eta) < 1.3","")
    df = df.Filter("Trig_obj_pt[Jet_hlt_matched_index[tnp[0]]]>500")
    df_after = df.Filter("Jet_hlt_matched_index[tnp[1]]!=-1","")
    df_after = df_after.Filter("Trig_obj_pt[Jet_hlt_matched_index[tnp[1]]]>500")

    
    _histo             = df.Histo1D(("h_pt_lead", ";x-axis;y-axis", 100, 0, 1000), "Lead_jet")
    _histo_tag         = df.Histo1D(("h_pt_tag", ";x-axis;y-axis", 100, 0, 1000), "pT_tag")
    _histo_probe       = df.Histo1D(("h_pt_probe", ";x-axis;y-axis", 100, 0, 1000), "pT_probe")
    _histo_ave         = df.Histo1D(("h_pt_ave", ";x-axis;y-axis", 100, 0, 1000), "pT_ave")
    _histo_sub         = df.Histo1D(("h_pt_sub", ";x-axis;y-axis", 100, 0, 1000), "Sub_jet")
    _histo_tag_phi     = df.Histo1D(("h_phi_tag", ";x-axis;y-axis", 100, -3.2, 3.2), "tag_jet_phi")
    _histo_probe_phi   = df.Histo1D(("h_phi_probe", ";x-axis;y-axis", 100, -3.2, 3.2), "probe_jet_phi")
    _histo_tag_eta     = df.Histo1D(("h_eta_tag", ";x-axis;y-axis", 100, -5, 5), "tag_jet_eta")
    _histo_probe_eta   = df.Histo1D(("h_eta_probe", ";x-axis;y-axis", 100, -5, 5), "probe_jet_eta")
    _histo_phi         = df.Histo1D(("h_phi_lead", ";x-axis;y-axis", 100, -3.2, 3.2), "Lead_jet_phi")
    _histo_sub_phi     = df.Histo1D(("h_phi_sub", ";x-axis;y-axis", 100, -3.2, 3.2), "Sub_jet_phi")
    _histo_eta         = df.Histo1D(("h_eta_lead", ";x-axis;y-axis", 100, -5, 5), "Lead_jet_eta")
    _histo_sub_eta     = df.Histo1D(("h_eta_sub", ";x-axis;y-axis", 100, -5, 5), "Sub_jet_eta")
    _histo_dphi        = df.Histo1D(("h_dphi", ";x-axis;y-axis", 100, 0, 3.14), "Delta_phi")
    _histo_alpha       = df.Histo1D(("h_alpha", ";x-axis;y-axis", 100, 0, 1), "alpha")
    _histo_trig        = df.Histo1D(("h_trig_pt",";pT;a.u.",100,0,1000),"Trig_obj_pt")
    _histo_matched     = df.Histo1D(("h_hlt_matched_pt",";pT;a.u.",1000,0,10000),"hlt_Jet_off_matched_pt")
    _histo_matched_id  = df.Histo1D(("h_hlt_matched_id",";pT;a.u.",10000,0,10000),"hlt_Jet_matched_id")
    _histo_matched_eta = df.Histo1D(("h_hlt_matched_eta",";pT;a.u.",100,-5,5),"hlt_Jet_matched_eta")
    _histo_matched_phi = df.Histo1D(("h_hlt_matched_phi",";pT;a.u.",100,-3.2,3.2),"hlt_Jet_matched_phi")
    
    _after_histo             = df_after.Histo1D(("h_after_pt_lead", ";x-axis;y-axis", 100, 0, 1000), "Lead_jet")
    _after_histo_tag         = df_after.Histo1D(("h_after_pt_tag", ";x-axis;y-axis", 100, 0, 1000), "pT_tag")
    _after_histo_probe       = df_after.Histo1D(("h_after_pt_probe", ";x-axis;y-axis", 100, 0, 1000), "pT_probe")
    _after_histo_ave         = df_after.Histo1D(("h_after_pt_ave", ";x-axis;y-axis", 100, 0, 1000), "pT_ave")
    _after_histo_sub         = df_after.Histo1D(("h_after_pt_sub", ";x-axis;y-axis", 100, 0, 1000), "Sub_jet")
    _after_histo_tag_phi     = df_after.Histo1D(("h_after_phi_tag", ";x-axis;y-axis", 100, -3.2, 3.2), "tag_jet_phi")
    _after_histo_probe_phi   = df_after.Histo1D(("h_after_phi_probe", ";x-axis;y-axis", 100, -3.2, 3.2), "probe_jet_phi")
    _after_histo_tag_eta     = df_after.Histo1D(("h_after_eta_tag", ";x-axis;y-axis", 100, -5, 5), "tag_jet_eta")
    _after_histo_probe_eta   = df_after.Histo1D(("h_after_eta_probe", ";x-axis;y-axis", 100, -5, 5), "probe_jet_eta")
    _after_histo_phi         = df_after.Histo1D(("h_after_phi_lead", ";x-axis;y-axis", 100, -3.2, 3.2), "Lead_jet_phi")
    _after_histo_sub_phi     = df_after.Histo1D(("h_after_phi_sub", ";x-axis;y-axis", 100, -3.2, 3.2), "Sub_jet_phi")
    _after_histo_eta         = df_after.Histo1D(("h_after_eta_lead", ";x-axis;y-axis", 100, -5, 5), "Lead_jet_eta")
    _after_histo_sub_eta     = df_after.Histo1D(("h_after_eta_sub", ";x-axis;y-axis", 100, -5, 5), "Sub_jet_eta")
    _after_histo_dphi        = df_after.Histo1D(("h_after_dphi", ";x-axis;y-axis", 100, 0, 3.14), "Delta_phi")
    _after_histo_alpha       = df_after.Histo1D(("h_after_alpha", ";x-axis;y-axis", 100, 0, 1), "alpha")
    _after_histo_trig        = df_after.Histo1D(("h_after_trig_pt",";pT;a.u.",100,0,1000),"Trig_obj_pt")
    _after_histo_matched     = df_after.Histo1D(("h_after_hlt_matched_pt",";pT;a.u.",1000,0,10000),"hlt_Jet_off_matched_pt")
    _after_histo_matched_id  = df_after.Histo1D(("h_after_hlt_matched_id",";pT;a.u.",10000,0,10000),"hlt_Jet_matched_id")
    _after_histo_matched_eta = df_after.Histo1D(("h_after_hlt_matched_eta",";pT;a.u.",100,-5,5),"hlt_Jet_matched_eta")
    _after_histo_matched_phi = df_after.Histo1D(("h_after_hlt_matched_phi",";pT;a.u.",100,-3.2,3.2),"hlt_Jet_matched_phi")
    
    fOUT = ROOT.TFile.Open(outputdir+"/output_hist"+str(idx)+".root","RECREATE")

    _histo.Write()
    _histo_tag.Write()
    _histo_probe.Write()
    _histo_ave.Write()
    _histo_sub.Write()
    _histo_tag_phi.Write()
    _histo_probe_phi.Write()
    _histo_tag_eta.Write()
    _histo_probe_eta.Write()
    _histo_phi.Write()
    _histo_sub_phi.Write()
    _histo_eta.Write()
    _histo_sub_eta.Write()
    _histo_dphi.Write()
    _histo_alpha.Write()
    _histo_trig.Write()
    _histo_matched.Write()
    _histo_matched_id.Write()
    _histo_matched_eta.Write()
    _histo_matched_phi.Write()
    
    _after_histo.Write()
    _after_histo_tag.Write()
    _after_histo_probe.Write()
    _after_histo_ave.Write()
    _after_histo_sub.Write()
    _after_histo_tag_phi.Write()
    _after_histo_probe_phi.Write()
    _after_histo_tag_eta.Write()
    _after_histo_probe_eta.Write()
    _after_histo_phi.Write()
    _after_histo_sub_phi.Write()
    _after_histo_eta.Write()
    _after_histo_sub_eta.Write()
    _after_histo_dphi.Write()
    _after_histo_alpha.Write()
    _after_histo_trig.Write()
    _after_histo_matched.Write()
    _after_histo_matched_id.Write()
    _after_histo_matched_eta.Write()
    _after_histo_matched_phi.Write()
    
    
    fOUT.Close()
    

if __name__ == "__main__":

    filename = args.filename+".out"
    outputdir = args.outputdir
    index = int(args.index)
    f = open(filename,'r')
    filelist = []
    for line in f:
        line = line.strip()
        filelist.append(line)
    analysis(filelist[index],index,outputdir)
