from PhysicsTools.NanoAODTools.postprocessing.framework.preskimming import preSkim
import ROOT 
import numpy as np

with ROOT.TFile("root://xrootd-cms.infn.it//store/data/Run2023D/JetMET0/NANOAOD/22Sep2023_v1-v1/2530000/90b4ce31-2fb1-4822-8ca4-aef2c302761d.root","read") as infile :
    t = infile['Events']
    elist, JsonFilter = preSkim(t,jsonInput="/eos/user/c/cmsdqm/www/CAF/certification/Collisions23/Cert_Collisions2023_eraD_369803_370790_Golden.json")

    print(elist)
    print(JsonFilter)


