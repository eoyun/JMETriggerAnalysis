import json
import fsspec
import ROOT
import numpy
import callable_array

class lumimask:
    def __init__(self, era = 2024):
        if era == 2024 :
            jsonfile = "/eos/user/c/cmsdqm/www/CAF/certification/Collisions24/Cert_Collisions2024_378981_386951_Golden.json"
        if era == 2025 :
            jsonfile = "/eos/user/c/cmsdqm/www/CAF/certification/Collisions25/Cert_Collisions2025_391658_398860_Golden.json"
        #jsonfile = "/eos/user/c/cmsdqm/www/CAF/certification/Collisions24/2024C_Golden.json"

        with fsspec.open(jsonfile) as fin:
            goldenjson = json.load(fin)

        self.masks_ = {}
        for run, lumilist in goldenjson.items():
            #print(str(run)+" | "+str(lumilist))
            mask = numpy.array(lumilist,dtype=numpy.uint32).flatten()
            mask[::2] -= 1
            self.masks_[numpy.uint32(run)] = mask

    def __call__(self,runs, lumis) :
        runs_ = numpy.fromiter(runs,dtype='uint32')
        mask_out = numpy.zeros(shape=runs_.shape)
        mask = self.masks_
        for iev in range(len(runs_)):
            run = numpy.uint32(runs[iev])
            lumi = numpy.uint32(lumis[iev])
            if run in mask :
                lumi_ = mask[run]
                ind = numpy.searchsorted(lumi_,lumi)
                if numpy.mod(ind,2) == 1:
                    mask_out[iev] = 1
            #print(str(run)+" | "+str(lumi)+" | "+str(mask_out[iev]))
        carray  = dict(enumerate(mask_out, 1))

        #return mask_out
        return mask_out
