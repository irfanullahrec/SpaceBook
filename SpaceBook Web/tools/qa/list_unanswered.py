"""List the question lines (q without parts, qp parts) of a page-book source that have no answer line yet.

    python -X utf8 tools/qa/list_unanswered.py <class-dir> <subject> [--from pNNN] [--to pNNN] [--width N]

Output: pNNN:LINE<TAB>kind<TAB>no<TAB>text.  LINE is the 1-based line of the q/qp in pages/pNNN.txt; tools/qa/apply_answers.py
inserts a `sol` line after the anchors listed in an answers batch file.  A group heading (`q` followed by `qp` lines) is not listed.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'docs' / 'source-verification'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
opts = {sys.argv[i]: sys.argv[i + 1] for i in range(len(sys.argv) - 1) if sys.argv[i].startswith('--')}
cls, subj = args[0], args[1]
lo, hi = opts.get('--from', 'p000'), opts.get('--to', 'p999')
width = int(opts.get('--width', '170'))
pdir = ROOT / cls / subj / 'pages'
ANS = ('sol ', 'solution', 'qsolution', 'qsol ', 'qsolve ')
n_total = n_open = 0
for f in sorted(pdir.glob('p[0-9][0-9][0-9].txt')):
    if not (lo <= f.stem <= hi):
        continue
    L = f.read_text(encoding='utf-8').split('\n')
    items = []
    for i, ln in enumerate(L):
        s = ln.strip()
        m = re.match(r'(qp|q)\s+([^|]*)\|\s*(.*)$', s)
        if m:
            items.append([i, m.group(1), m.group(2).strip(), m.group(3)])
    for k, (i, kind, no, text) in enumerate(items):
        end = items[k + 1][0] if k + 1 < len(items) else len(L)
        nxt = items[k + 1] if k + 1 < len(items) else None
        if kind == 'q' and nxt and nxt[1] == 'qp' and nxt[0] <= i + 3:
            continue            # heading of a part group
        if kind == 'q' and (k + 1 < len(items)) is False and any(L[j].strip().startswith('qp ') for j in range(i + 1, min(len(L), i + 3))):
            continue
        n_total += 1
        body = [L[j].strip() for j in range(i + 1, end)]
        if any(b.startswith(ANS) for b in body):
            continue
        n_open += 1
        print(f'{f.stem}:{i + 1}\t{kind}\t{no}\t{re.sub(chr(32) + "+", chr(32), text)[:width]}')
print(f'# {cls}/{subj}: {n_open} of {n_total} question lines without an answer', file=sys.stderr)
