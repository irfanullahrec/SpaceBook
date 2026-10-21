"""Move stacked @sec lines (several at the top of a page) down to the heading/box they name,
so each section owns its content instead of leaving empty cards.

    python tools/fix_secs.py <class> <subj> [--write]
The first @sec of a page stays on top; each later one moves directly above the first
'#'/'##' heading or 'box' line whose English title equals the @sec's English title.
"""
import sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
cl, subj = sys.argv[1], sys.argv[2]
write = '--write' in sys.argv
LANG_EN = {'urdu': 1, 'isl': 1, 'quran': 1, 'arabic': 1, 'hpe': 1, 'pashto': 1}
def norm(s): return re.sub(r'\W+', ' ', s).strip().lower()
changed = 0
for f in sorted((HERE / f'class-{cl}' / subj / 'pages').glob('p*.txt')):
    L = f.read_text(encoding='utf-8').split('\n')
    sec_idx = [i for i, l in enumerate(L) if l.startswith('@sec ')]
    if len(sec_idx) < 2: continue
    # only stacked at top: consecutive run
    top = [i for i in sec_idx if all(L[j].startswith('@') for j in range(sec_idx[0], i))]
    if len(top) < 2: continue
    moves = []
    for i in top[1:]:
        body = L[i][5:].split('|', 1)[1] if '|' in L[i] else ''
        parts = [p.strip() for p in body.split('||')]
        titles = {norm(p) for p in parts[:3]}
        tgt = None
        for j, l in enumerate(L):
            if j <= top[-1]: continue
            m = re.match(r'(#{1,3})\s+(.*)$', l) or re.match(r'box\s+\w+\s*\|\s*(.*)$', l)
            if not m: continue
            txt = m.group(m.lastindex)
            ps = {norm(p) for p in txt.split('||')}
            if titles & ps - {''}:
                tgt = j; break
        if tgt is not None: moves.append((i, tgt))
    if not moves: continue
    lines = L[:]
    for i, tgt in sorted(moves, key=lambda m: -m[1]):
        lines.insert(tgt, L[i])
    for i, _ in sorted(moves, key=lambda m: -m[0]):
        # remove original (indices before tgt are unchanged by inserts after them)
        lines.pop(i)
    changed += 1
    if write: f.write_text('\n'.join(lines), encoding='utf-8')
    print(f.name, len(moves), 'moved')
print(changed, 'pages', 'written' if write else 'dry run')
