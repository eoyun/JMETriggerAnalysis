import os
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", dest="dataset", action="store") 
parser.add_argument("-o", "--outputdir", dest="outputdir", action="store") 
parser.add_argument("-p", "--pythonscript", dest="pythonscr", action="store") 
parser.add_argument("-e","--era",dest="era",action="store")
args = parser.parse_args()

def Make_CondorScr(outname, script_name) :
    os.system("mkdir -p Scr/"+outname+"/log")
    condor_filename = "Scr/"+outname+"/condor.submit"
    lines =0
    with open("./input/"+outname+".out","r") as fp :
        lines = len(fp.readlines())
    f = open(condor_filename,"w")
    f.write('# Unix submit description file\n')
    f.write('Universe = vanilla\n')
    f.write('transfer_input_files = /afs/cern.ch/user/y/yeo/tmp/x509up, ./input/'+outname+'.out, ./Scr/'+outname+'/'+script_name+', ./Scr/'+outname+'/LumiMask.py, ./Scr/'+outname+'/callable_array.py\n')
    f.write('Executable = ./Scr/'+outname+'/test.sh\n')
    f.write('request_memory = 1000\n') 
    f.write('should_transfer_files   = Yes\n')
    f.write('arguments = $(ProcId)\n')
    f.write('output = ./Scr/'+outname+'/log/$(ProcId).out\n')
    f.write('error = ./Scr/'+outname+'/log/$(ProcId).err\n')
    f.write('log = ./Scr/'+outname+'/log/$(ProcId).log\n')
    f.write('+MaxRuntime = 36000\n')
    f.write('Queue '+str(lines)+'\n')
    f.close()
    subchMod = "condor_submit ./Scr/"+outname+"/condor.submit"
    os.system("pwd")
    os.system(subchMod)
    return 0

def Make_Scr(outname, script,era) :
    os.system("mkdir -p Scr/"+outname)
    scr_filename = "Scr/"+outname+"/test.sh"
    f = open(scr_filename,"w")
    f.write('#!/bin/bash\n')
    f.write('source /cvmfs/cms.cern.ch/cmsset_default.sh\n') 
    f.write('source /cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/setup.sh\n')
    f.write('export X509_USER_PROXY=/afs/cern.ch/user/y/yeo/tmp/x509up\n')
    f.write('voms-proxy-info -all\n')
    f.write('voms-proxy-info -all --file $X509_USER_PROXY\n')
    #f.write('cd /afs/cern.ch/user/y/yeo/rdf/24.09.25\n') 
    f.write('cd $_CONDOR_SCRATCH_DIR\n')
    f.write('mkdir -p /eos/home-y/yeo/rdf/output/'+outname+'\n') 
    script_name = os.path.basename(script)
    f.write('python3 ./'+script_name+' -f '+outname+' -i $1 -o /eos/home-y/yeo/rdf/output/'+outname +" -e "+era)
    f.close()
    os.system("cp "+script+" Scr/"+outname+"/")
    os.system("cp LumiMask.py Scr/"+outname+"/")
    os.system("cp callable_array.py Scr/"+outname+"/")


    return 0

def Make_input(dataset,outname) :
    os.system("mkdir -p input")
    os.system("dasgoclient -query=\"file dataset=" + dataset +" system=rucio\" > ./input/"+outname+".out")
    os.system("echo "+dataset+" > ./input/"+outname+"_dataset.txt");
    return 0

if __name__ == '__main__':
    outname = args.outputdir
    dataset = args.dataset
    script = args.pythonscr
    era = args.era
    if (os.path.isfile('./input/'+outname+'.out')) :
    
        print('plz check output name')
    else :
        Make_input(dataset,outname)
        Make_Scr(outname,script,era)
        Make_CondorScr(outname, os.path.basename(script))

    #Make_input("/JetMET0/Run2024C-PromptReco-v1/NANOAOD",outname)
    #Make_Scr(outname)
    #Make_CondorScr(outname)
