import re,glob,sys
want=[tuple(x.split('|')) for x in sys.argv[1].split(',')]
lines=[]
for f in sorted(glob.glob('docs/source-verification/class-7/math/pages/p*.txt')):
    for ln in open(f,encoding='utf8').read().split('\n'): lines.append((f[-8:-4],ln))
cur=None;i=0
while i<len(lines):
    pg,l=lines[i]
    if l.startswith('exercise '): cur=l[9:].strip()
    elif l.startswith('endexercise'): cur=None
    m=re.match(r'q\s+(\S+)\s*\|',l)
    if m and (cur,m.group(1)) in want:
        print(f'#### {cur}|{m.group(1)} {pg}')
        j=i
        while True:
            b=lines[j][1].split(' || ')[0]
            if j>i and re.match(r'(q\s+\S+\s*\||exercise |endexercise)',lines[j][1]): break
            if not b.startswith(('@','<','endsvg')) and b.strip(): print('  ',b[:200])
            j+=1
            if j>=len(lines): break
    i+=1
