import sys, re
from pathlib import Path
HERE=Path(__file__).resolve().parent
cur=None; buf=[]
def flush():
    if cur: (HERE/'src'/f'{cur}.src').write_text('\n'.join(buf).strip('\n')+'\n',encoding='utf-8')
for line in Path(sys.argv[1]).read_text(encoding='utf-8').splitlines():
    m=re.match(r'^=== (p\d{3})\s*$',line)
    if m: flush(); cur,buf=m.group(1),[]
    else: buf.append(line)
flush()
