"""List q / qp lines with no sol line under them.   python list_unanswered.py CLASS SUBJ [--full]"""
import sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
cl, subj = sys.argv[1], sys.argv[2]
RTL = {'urdu':1,'isl':1,'quran':1,'arabic':1,'hpe':1,'pashto':1}
slot = 1 if subj in RTL else 0
for f in sorted((HERE / f'class-{cl}' / subj / 'pages').glob('p*.txt')):
    L = f.read_text(encoding='utf-8').split('\n')
    ex = None
    for i, l in enumerate(L):
        if l.startswith('exercise '): ex = l.split(None, 1)[1]
        if l.startswith('endexercise'): ex = None
        m = re.match(r'(q|qp)\s+(\S+)\s*\|?\s*(.*)', l)
        if not m: continue
        j = i + 1
        while j < len(L) and L[j].startswith('@'): j += 1
        nxt = L[j] if j < len(L) else ''
        # a q with qp children is answered through its parts
        if m.group(1) == 'q' and nxt.startswith('qp '): continue
        if nxt.startswith(('sol ', 'solution', 'qsol')): continue
        parts = m.group(3).split('||')
        t = (parts[slot] if len(parts) > slot else parts[0]).strip()
        print(f'{f.stem} [{ex}] {m.group(1)} {m.group(2)}: {t[:(400 if "--full" in sys.argv else 130)]}')
