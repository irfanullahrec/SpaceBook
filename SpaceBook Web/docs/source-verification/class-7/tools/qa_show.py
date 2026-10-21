"""Print page files compactly for authoring answers.
    python qa_show.py CLASS SUBJ FIRST LAST [slot]   (slot = index of the || slot to show, default: English slot for the book)
"""
import sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
cl, subj, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
RTL = {'urdu':1,'isl':1,'quran':1,'arabic':1,'hpe':1,'pashto':1}
slot = int(sys.argv[5]) if len(sys.argv) > 5 else (1 if subj in RTL else 0)
for n in range(a, b + 1):
    f = HERE / f'class-{cl}' / subj / 'pages' / f'p{n:03}.txt'
    if not f.exists(): continue
    print(f'=== p{n:03}')
    for l in f.read_text(encoding='utf-8').split('\n'):
        if l.startswith(('@deco','@issue','@printed','@status')): continue
        op, _, rest = l.partition(' ')
        if '||' in rest:
            parts = [x.strip() for x in rest.split('||')]
            # first slot may carry "no | text"
            if len(parts) > 1 and slot < len(parts):
                head = parts[0].split('|', 1)
                if slot == 0: txt = parts[0].split('|',1)[-1].strip() if op in ('q','qp') else parts[0]
                else: txt = parts[slot]
                if op in ('q','qp'): txt = (head[0].strip() + ' | ' if len(head) > 1 else '') + txt
                print(op, txt[:400])
                continue
        print(l[:400])
