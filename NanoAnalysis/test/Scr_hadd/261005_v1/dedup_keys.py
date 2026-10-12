import ROOT, sys
src, dst = sys.argv[1], sys.argv[2]
f = ROOT.TFile.Open(src)
o = ROOT.TFile.Open(dst, "RECREATE")
seen = set()
for k in f.GetListOfKeys():
    n = k.GetName()
    if n in seen:
        continue
    seen.add(n)
    obj = f.Get(n)              # newest cycle = the fully merged one
    if hasattr(obj, "SetDirectory"):
        obj.SetDirectory(0)
    o.cd()
    obj.Write(n)
o.Close()
f.Close()
print("kept %d unique keys" % len(seen))
