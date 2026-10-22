import json,re,sys,glob
miss=json.load(open('tmp/miss8.json',encoding='utf8'))
want={}
for ex,v in miss.items():
    for q,ps,en,k in v: want.setdefault(ex,{})[q]=ps
pages=sorted(glob.glob('docs/source-verification/class-8/math/pages/p*.txt'))
cur=None;out={}
lines=[]
for f in pages:
    for ln in open(f,encoding='utf8').read().split('\n'):
        lines.append((f[-8:-4],ln))
res=[];i=0
while i<len(lines):
    pg,l=lines[i]
    if l.startswith('exercise '): cur=l[9:].strip()
    elif l.startswith('endexercise'): cur=None
    m=re.match(r'q\s+(\S+)\s*\|',l)
    if m and cur in want and m.group(1) in want[cur]:
        blk=[l];j=i+1
        while j<len(lines) and not re.match(r'(q\s+\S+\s*\||exercise |endexercise)',lines[j][1]) :
            blk.append(lines[j][1]); j+=1
        res.append((cur,m.group(1),pg,blk))
    i+=1
for cur,q,pg,blk in res:
    print(f'#### {cur} | {q} | {pg}')
    for b in blk:
        b=b.split(' || ')[0]
        if b.startswith(('@','svg','<','endsvg')) or not b.strip(): continue
        print('  ',b[:230])
