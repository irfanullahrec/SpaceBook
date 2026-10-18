import json,os,sys
m={int(k):v for k,v in json.load(open(os.path.join(os.path.dirname(__file__),'jpgmap.json'))).items()}
inv={}
for k,v in sorted(m.items()): inv.setdefault(v,k)
files=sorted(os.listdir('D:/SpaceBook/Books/9th/9th Computer Science/jpg'))
a,b=int(sys.argv[1]),int(sys.argv[2])
print(' '.join(f'{p}:{files[inv[p]]}' for p in range(a,b+1) if p in inv))
