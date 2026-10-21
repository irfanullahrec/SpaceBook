"""List question lines (leaf q, or qp) of a class/subject that carry no answer in the page transcriptions.

    python unanswered.py CLASS SUBJ [--show N]

A leaf is a `q` with no `qp` before the next `q`, or a `qp`. It is answered when a sol / solution / qsol / qsolve
line follows it (or follows its parent `q` for qsolve / qsol). Used to find what is still open in a book.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def scan(cls, subj):
    pages = sorted((ROOT / f'class-{cls}' / subj / 'pages').glob('p*.txt'))
    srcs = [(p, p.read_text(encoding='utf8').split('\n')) for p in pages]
    res, total = [], 0
    parent_solved = False        # a question's parts and its qsolve may sit on the next page
    ex = None
    for k, (p, src) in enumerate(srcs):
        if any(l.startswith('@status answers') for l in src):
            continue
        more = [x for _, s2 in srcs[k + 1:k + 3] for x in s2]
        for i, line in enumerate(src):
            if line.startswith('exercise '):
                ex = line[9:]
            m = re.match(r'^(q|qp)\s+(\S+)\s*\|\s*(.*)$', line)
            if not m:
                continue
            tail = src[i + 1:] + more
            if m.group(1) == 'q':
                parent_solved = False
                has_parts = False
                for x in tail:
                    if re.match(r'^(q|exercise|endexercise|page|unit)\b', x):
                        break
                    if x.startswith('qp '):
                        has_parts = True
                    if re.match(r'^(qsolve|qsol)\b', x):
                        parent_solved = True
                if has_parts:
                    continue
            elif parent_solved:
                continue
            ahead = []
            for x in src[i + 1:]:
                if re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', x):
                    break
                ahead.append(x)
            total += 1
            if parent_solved or any(re.match(r'^(sol|solution|qsol|qsolve)\b', x) for x in ahead):
                continue
            res.append((p.name, ex or '', m.group(1), m.group(2), m.group(3).split(' || ')[0][:100]))
    return total, res


if __name__ == '__main__':
    cls, subj = sys.argv[1], sys.argv[2]
    n = int(sys.argv[sys.argv.index('--show') + 1]) if '--show' in sys.argv else 0
    total, res = scan(cls, subj)
    print(f'class {cls} {subj}: {len(res)} unanswered of {total} leaf questions')
    for r in res[:n]:
        print('  ', *r)
