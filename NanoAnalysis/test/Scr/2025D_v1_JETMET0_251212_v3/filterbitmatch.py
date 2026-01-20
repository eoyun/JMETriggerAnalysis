#!/usr/bin/env python

import datetime
import numpy as np
import ROOT
import argparse
import os
import LumiMask

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", dest="filename", action="store") 
parser.add_argument("-i", "--index", dest="index", action="store") 
parser.add_argument("-o", "--outputdir", dest="outputdir", action="store") 
parser.add_argument("-e","--era",dest="era",action="store")
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

def dphi(phi):
    """Calculates delta phi between objects"""
    x = np.abs(phi[1] - phi[0])
    sign = x<=np.pi
    dphi = sign* x + ~sign * (2*np.pi - x)
    return dphi



def analysis(filename_idx,idx,outputdir,era):
    declare_struc()
    inputfile = "root://xrootd-cms.infn.it/"+filename_idx
    #df = ROOT.RDataFrame("Events", "DYJetsToLL_M_50_2022.root")
    #df = ROOT.RDataFrame("Events","root://xrootd-cms.infn.it//store/data/Run2023B/JetMET0/NANOAOD/22Sep2023-v1/2540000/060eed3c-d114-4135-b3f6-2cc6c8cf4c19.root")
    #df = ROOT.RDataFrame("Events","root://xrootd-cms.infn.it//store/data/Run2023D/JetMET0/NANOAOD/22Sep2023_v1-v1/2530000/90b4ce31-2fb1-4822-8ca4-aef2c302761d.root")
    print(inputfile)
    df = ROOT.RDataFrame("Events",inputfile)
    #df = ROOT.RDataFrame("Events","root://xrootd-cms.infn.it//store/mc/Run3Winter23NanoAOD/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/NANOAODSIM/126X_mcRun3_2023_forPU65_v1-v1/2540000/a1c3034d-ce5a-4d4c-9ee6-939b6c04edb5.root")
    df = df.Filter("nJet >= 2", "Events with exactly two muons")
    #df = df.Filter("Muon_charge[0] + Muon_charge[1] == 0", "Muons with opposite charge")

    #df_dimuon = df.Define("Dimuon_mass", "InvariantMass(Muon_pt, Muon_eta, Muon_phi, Muon_mass)")
    df = df.Define("Lead_jet", "Jet_pt[0]")
    df = df.Define("Sub_jet", "Jet_pt[1]")
    df = df.Define("Lead_jet_phi", "Jet_phi[0]")
    df = df.Define("Sub_jet_phi", "Jet_phi[1]")
    df = df.Define("Lead_jet_eta", "Jet_eta[0]")
    df = df.Define("Sub_jet_eta", "Jet_eta[1]")
    #print(np.array(df.Take['float']("Lead_jet").GetValue()))
    #print(np.array(df_lead_jet.Take['float']("Lead_jet").GetValue()))
    #print(type(ROOT.vector['float'](np.zeros(10))))
    ROOT.gInterpreter.Declare(
            """
            vector<int> random_idx(){
                //std::cout<<std::rand()%2<<std::endl;

                vector<int> tnp;
                int tmp = std::rand()%2;

                tnp.push_back(tmp);
                tnp.push_back((tmp+1)%2);
                //std::cout<<tmp<< " | "<<(tmp+1)%2<<std::endl;
                return tnp;
            }
            """
            )
    ROOT.gInterpreter.Declare(
            """
            double dphi(double phi1, double phi2){
                float x  = abs(phi1-phi2);
                if (x>M_PI)return 2*M_PI - x;
                else return x;
            }
            """
            )
    ROOT.gInterpreter.Declare(
            """
            vector<int> match_hlt_offline ( ROOT::VecOps::RVec<float> hlt_eta,ROOT::VecOps::RVec<float> hlt_phi,ROOT::VecOps::RVec<float> off_eta,ROOT::VecOps::RVec<float> off_phi){
                vector<int> hlt_matched;
                int off_index;
                float dr=0.2;
                if  (off_eta.size()==0 || hlt_eta.size()==0) {
                    hlt_matched.push_back(-1);
                    return hlt_matched;
                }
                //for (int i=0; i< hlt_eta.size();i++){
                for (int i=0; i< off_eta.size();i++){
                    off_index = -1;
                    //std::cout<<off_phi.size()<<" | "<<off_eta.size()<<" | "<<i<<" | "<<hlt_phi.size()<<" | "<<hlt_eta.size()<<std::endl;
                    for (int j=0;j<hlt_eta.size();j++){
                        if (sqrt(pow(hlt_eta[j]-off_eta[i],2)+pow(hlt_phi[j]-off_phi[i],2))<dr){
                            off_index = j;
                            break;
                        }
                    }
                    //std::cout<<off_index<<std::endl;
                    hlt_matched.push_back(off_index);
                }
                //std::cout<<hlt_matched.size()<<" | "<<off_eta.size()<<" | "<<hlt_eta.size()<<std::endl;
                return hlt_matched;
            }
            """

            )
    #df_delta_phi = df.Define("Delta_phi","double x = Jet_phi[0]- Jet_phi[1]; return x > TMath::pi ? 2 * TMath::pi - x : x")
    df = df.Define("Delta_phi","dphi(Jet_phi[0],Jet_phi[1])")
    df = df.Define("alpha","nJet==2 ? 0 : 2 * Jet_pt[2]/(Jet_pt[0]+Jet_pt[1])")
    #df = df.Define("Trig_obj_pt","TrigObj_pt[TrigObj_id == 1 && (TrigObj_filterBits % 64) /32  != 0 && (TrigObj_filterBits % 4096) / 2048 == 0]")
    #df = df.Define("hlt_Jet_eta","TrigObj_eta[TrigObj_id == 1 && (TrigObj_filterBits % 64) /32  != 0 && (TrigObj_filterBits % 4096) / 2048 == 0]")
    #df = df.Define("hlt_Jet_phi","TrigObj_phi[TrigObj_id == 1 && (TrigObj_filterBits % 64) /32  != 0 && (TrigObj_filterBits % 4096) / 2048 == 0]")
    #df = df.Define("hlt_Jet_id","TrigObj_filterBits[TrigObj_id==1&& (TrigObj_filterBits % 64) /32  != 0&& (TrigObj_filterBits % 4096) / 2048 == 0]")
    bitmask_42 = 1 << 42
    print(bitmask_42)

    df = df.Define("Trig_obj_pt",f"TrigObj_pt[TrigObj_id == 1 && (TrigObj_filterBits & {bitmask_42}) != 0 && TrigObj_pt >550]")
    df = df.Define("hlt_Jet_eta",f"TrigObj_eta[TrigObj_id == 1 && (TrigObj_filterBits & {bitmask_42}) != 0 && TrigObj_pt >550]")
    df = df.Define("hlt_Jet_phi",f"TrigObj_phi[TrigObj_id == 1 && (TrigObj_filterBits & {bitmask_42}) != 0 && TrigObj_pt >550]")
    df = df.Define("hlt_Jet_id",f"TrigObj_filterBits[TrigObj_id==1&& (TrigObj_filterBits & {bitmask_42})  != 0 && TrigObj_pt >550]")
    #df = df.Define("Trig_obj_pt","TrigObj_pt[TrigObj_id == 1 ]")
    #df = df.Define("hlt_Jet_eta","TrigObj_eta[TrigObj_id == 1]")
    #df = df.Define("hlt_Jet_phi","TrigObj_phi[TrigObj_id == 1]")
    #df = df.Define("hlt_Jet_id","TrigObj_filterBits[TrigObj_id==1]")
    #df = df.Define("Trig_obj_pt","TrigObj_pt[TrigObj_id == 1 ]")
    #df = df.Define("hlt_Jet_eta","TrigObj_eta[TrigObj_id == 1 ]")
    #df = df.Define("hlt_Jet_phi","TrigObj_phi[TrigObj_id == 1 ]")
    #df = df.Define("hlt_Jet_id","TrigObj_filterBits[TrigObj_id==1]")
    #df.Display("hlt_Jet_id").Print()
    #print(df.Take['ROOT::VecOps::RVec<int>']("hlt_Jet_id").GetValue())
    df = df.Define("Jet_hlt_matched_index","match_hlt_offline(hlt_Jet_eta,hlt_Jet_phi,Jet_eta,Jet_phi)")
    df = df.Define("hlt_Jet_off_matched_pt","Trig_obj_pt[Jet_hlt_matched_index[0]]")
    df = df.Define("hlt_Jet_matched_id","hlt_Jet_id[Jet_hlt_matched_index[0]]")
    df = df.Define("hlt_Jet_matched_eta","hlt_Jet_eta[Jet_hlt_matched_index[0]]")
    df = df.Define("hlt_Jet_matched_phi","hlt_Jet_phi[Jet_hlt_matched_index[0]]")
    #print(df.Take['vector<int>']("Jet_hlt_matched_index").GetValue())
    #df_delta_phi = df.Define("Delta_phi","dphi(Jet_phi)")
    LumiMask_ = LumiMask.lumimask(era=era)(df.Take[ROOT.UInt_t]("run").GetValue(),df.Take[ROOT.UInt_t]("luminosityBlock").GetValue())
    #print(LumiMask_)
    df = df.Define("counter","counter++")
    Lumi_arr = ROOT.VecOps.AsRVec(LumiMask_)
    #print(Lumi_arr)
    df = ROOT.RDFAddArray(ROOT.RDF.AsRNode(df),Lumi_arr,"LumiMask")
    #print(df.AsNumpy(columns=["LumiMask"]))
    df = df.Filter("LumiMask > 0.5","")
    df = df.Define("tnp","random_idx()")
    #print(df.Take['vector<int>']("tnp").GetValue())
    #for i in range(len(tag_array)) :
    #    print(str(tag_array[i][0])+" | "+str(probe_array[i][1]))
    df = df.Define("pT_ave","(Lead_jet + Sub_jet)/2")
    df = df.Define("tag_jet_eta","Jet_eta[tnp[0]]")
    df = df.Define("tag_jet_phi","Jet_phi[tnp[0]]")
    df = df.Define("pT_tag","Jet_pt[tnp[0]]")
    #df = df.Define("tag_jet_id","Jet_jetId[tnp[0]]")
    #df = df.Define("probe_jet_id","Jet_jetId[tnp[1]]")
    df = df.Define("probe_jet_eta","Jet_eta[tnp[1]]")
    df = df.Define("probe_jet_phi","Jet_phi[tnp[1]]")
    df = df.Define("pT_probe","Jet_pt[tnp[1]]")
    #df = df.Filter("Jet_hlt_matched_index[tnp[0]]!=-1","") 
    #df = df.Filter("Delta_phi>2.7","") 
    #df = df.Filter("alpha < 0.1","") 
    #df = df.Filter("abs(Lead_jet_eta) < 1.3","")
    #df = df.Filter("abs(Sub_jet_eta) < 1.3","")
    #df = df.Filter("Trig_obj_pt[Jet_hlt_matched_index[tnp[0]]]>500")
    #df = df.Filter("tag_jet_id > 1","")
    #df_after = df.Filter("Jet_hlt_matched_index[tnp[1]]!=-1","")
    #df_after = df_after.Filter("Trig_obj_pt[Jet_hlt_matched_index[tnp[1]]]>500")
    df_after = df.Filter("Jet_hlt_matched_index[tnp[0]]!=-1","") 
    df_dphi_alpha_after = df_after.Filter("Delta_phi>2.7","") 
    df_dphi_alpha_after = df_dphi_alpha_after.Filter("alpha < 0.1","") 

    
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
    #_histo_tag_id      = df.Histo1D(("h_id_tag",";x-axis;y-axis",100,0,100), "tag_jet_id")
    #_histo_probe_id    = df.Histo1D(("h_id_probe",";x-axis;y-axis",100,0,100), "probe_jet_id")
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
    #_after_histo_tag_id      = df_after.Histo1D(("h_after_id_tag",";x-axis;y-axis",100,0,100), "tag_jet_id")
    #_after_histo_probe_id    = df_after.Histo1D(("h_after_id_probe",";x-axis;y-axis",100,0,100), "probe_jet_id")
    _after_histo_dphi        = df_after.Histo1D(("h_after_dphi", ";x-axis;y-axis", 100, 0, 3.14), "Delta_phi")
    _after_histo_alpha       = df_after.Histo1D(("h_after_alpha", ";x-axis;y-axis", 100, 0, 1), "alpha")
    _after_histo_trig        = df_after.Histo1D(("h_after_trig_pt",";pT;a.u.",100,0,1000),"Trig_obj_pt")
    _after_histo_matched     = df_after.Histo1D(("h_after_hlt_matched_pt",";pT;a.u.",1000,0,10000),"hlt_Jet_off_matched_pt")
    _after_histo_matched_id  = df_after.Histo1D(("h_after_hlt_matched_id",";pT;a.u.",10000,0,10000),"hlt_Jet_matched_id")
    _after_histo_matched_eta = df_after.Histo1D(("h_after_hlt_matched_eta",";pT;a.u.",100,-5,5),"hlt_Jet_matched_eta")
    _after_histo_matched_phi = df_after.Histo1D(("h_after_hlt_matched_phi",";pT;a.u.",100,-3.2,3.2),"hlt_Jet_matched_phi")
    
    _dphi_alpha_after_histo             = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_pt_lead", ";x-axis;y-axis", 100, 0, 1000), "Lead_jet")
    _dphi_alpha_after_histo_tag         = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_pt_tag", ";x-axis;y-axis", 100, 0, 1000), "pT_tag")
    _dphi_alpha_after_histo_probe       = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_pt_probe", ";x-axis;y-axis", 100, 0, 1000), "pT_probe")
    _dphi_alpha_after_histo_ave         = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_pt_ave", ";x-axis;y-axis", 100, 0, 1000), "pT_ave")
    _dphi_alpha_after_histo_sub         = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_pt_sub", ";x-axis;y-axis", 100, 0, 1000), "Sub_jet")
    _dphi_alpha_after_histo_tag_phi     = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_phi_tag", ";x-axis;y-axis", 100, -3.2, 3.2), "tag_jet_phi")
    _dphi_alpha_after_histo_probe_phi   = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_phi_probe", ";x-axis;y-axis", 100, -3.2, 3.2), "probe_jet_phi")
    _dphi_alpha_after_histo_tag_eta     = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_eta_tag", ";x-axis;y-axis", 100, -5, 5), "tag_jet_eta")
    _dphi_alpha_after_histo_probe_eta   = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_eta_probe", ";x-axis;y-axis", 100, -5, 5), "probe_jet_eta")
    _dphi_alpha_after_histo_phi         = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_phi_lead", ";x-axis;y-axis", 100, -3.2, 3.2), "Lead_jet_phi")
    _dphi_alpha_after_histo_sub_phi     = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_phi_sub", ";x-axis;y-axis", 100, -3.2, 3.2), "Sub_jet_phi")
    _dphi_alpha_after_histo_eta         = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_eta_lead", ";x-axis;y-axis", 100, -5, 5), "Lead_jet_eta")
    _dphi_alpha_after_histo_sub_eta     = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_eta_sub", ";x-axis;y-axis", 100, -5, 5), "Sub_jet_eta")
    _dphi_alpha_after_histo_dphi        = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_dphi", ";x-axis;y-axis", 100, 0, 3.14), "Delta_phi")
    _dphi_alpha_after_histo_alpha       = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_alpha", ";x-axis;y-axis", 100, 0, 1), "alpha")
    _dphi_alpha_after_histo_trig        = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_trig_pt",";pT;a.u.",100,0,1000),"Trig_obj_pt")
    _dphi_alpha_after_histo_matched     = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_hlt_matched_pt",";pT;a.u.",1000,0,10000),"hlt_Jet_off_matched_pt")
    _dphi_alpha_after_histo_matched_id  = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_hlt_matched_id",";pT;a.u.",10000,0,10000),"hlt_Jet_matched_id")
    _dphi_alpha_after_histo_matched_eta = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_hlt_matched_eta",";pT;a.u.",100,-5,5),"hlt_Jet_matched_eta")
    _dphi_alpha_after_histo_matched_phi = df_dphi_alpha_after.Histo1D(("h_dphi_alpha_after_hlt_matched_phi",";pT;a.u.",100,-3.2,3.2),"hlt_Jet_matched_phi")
    
    fOUT = ROOT.TFile.Open(outputdir+"/output_hist"+str(idx)+".root","RECREATE")
    #df_den_40.Snapshot("newtree","./"+outputdir+"/output_40_den_"+str(idx)+".root")
    #df_num_40.Snapshot("newtree","./"+outputdir+"/output_40_num_"+str(idx)+".root")
    #df_den_60.Snapshot("newtree","./"+outputdir+"/output_60_den_"+str(idx)+".root")
    #df_num_60.Snapshot("newtree","./"+outputdir+"/output_60_num_"+str(idx)+".root")
    #df_den_80.Snapshot("newtree","./"+outputdir+"/output_80_den_"+str(idx)+".root")
    #df_num_80.Snapshot("newtree","./"+outputdir+"/output_80_num_"+str(idx)+".root")
    #df_den_140.Snapshot("newtree","./"+outputdir+"/output_140_den_"+str(idx)+".root")
    #df_num_140.Snapshot("newtree","./"+outputdir+"/output_140_num_"+str(idx)+".root")
    #df_den_200.Snapshot("newtree","./"+outputdir+"/output_200_den_"+str(idx)+".root")
    #df_num_200.Snapshot("newtree","./"+outputdir+"/output_200_num_"+str(idx)+".root")
    #df_den_260.Snapshot("newtree","./"+outputdir+"/output_260_den_"+str(idx)+".root")
    #df_num_260.Snapshot("newtree","./"+outputdir+"/output_260_num_"+str(idx)+".root")
    #df_den_320.Snapshot("newtree","./"+outputdir+"/output_320_den_"+str(idx)+".root")
    #df_num_320.Snapshot("newtree","./"+outputdir+"/output_320_num_"+str(idx)+".root")
    #df_den_400.Snapshot("newtree","./"+outputdir+"/output_400_den_"+str(idx)+".root")
    #df_num_400.Snapshot("newtree","./"+outputdir+"/output_400_num_"+str(idx)+".root")
    #df_den_450.Snapshot("newtree","./"+outputdir+"/output_450_den_"+str(idx)+".root")
    #df_num_450.Snapshot("newtree","./"+outputdir+"/output_450_num_"+str(idx)+".root")
    #df_den_500.Snapshot("newtree","./"+outputdir+"/output_500_den_"+str(idx)+".root")
    #df_num_500.Snapshot("newtree","./"+outputdir+"/output_500_num_"+str(idx)+".root")
    #days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    #now = datetime.datetime.now()
    #m = "produced: %s %s"%(days[now.weekday()],now)
    #timestamp = ROOT.TNamed(m,"")
    #timestamp.Write()

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
    #_histo_tag_id.Write()
    #_histo_probe_id.Write()
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
    
    _dphi_alpha_after_histo.Write()
    _dphi_alpha_after_histo_tag.Write()
    _dphi_alpha_after_histo_probe.Write()
    _dphi_alpha_after_histo_ave.Write()
    _dphi_alpha_after_histo_sub.Write()
    _dphi_alpha_after_histo_tag_phi.Write()
    _dphi_alpha_after_histo_probe_phi.Write()
    _dphi_alpha_after_histo_tag_eta.Write()
    _dphi_alpha_after_histo_probe_eta.Write()
    _dphi_alpha_after_histo_phi.Write()
    _dphi_alpha_after_histo_sub_phi.Write()
    _dphi_alpha_after_histo_eta.Write()
    _dphi_alpha_after_histo_sub_eta.Write()
    _dphi_alpha_after_histo_dphi.Write()
    _dphi_alpha_after_histo_alpha.Write()
    _dphi_alpha_after_histo_trig.Write()
    _dphi_alpha_after_histo_matched.Write()
    _dphi_alpha_after_histo_matched_id.Write()
    _dphi_alpha_after_histo_matched_eta.Write()
    _dphi_alpha_after_histo_matched_phi.Write()
    
    
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
    #print(filelist[index])
    analysis(filelist[index],index,outputdir,era)



