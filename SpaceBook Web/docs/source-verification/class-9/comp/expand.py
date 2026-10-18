# -*- coding: utf-8 -*-
"""Expand Class 9 Computer Science page sources (src/pNNN.src) into page DSL (pages/pNNN.txt).

    python -X utf8 comp/expand.py NNN [NNN ...] | all

Extra source line understood (all other lines are copied unchanged):
    fig10 KEY || EN caption || UR caption || PS caption
copies the <svg> drawn for the Class 10 (Urdu-medium edition of the same Grade X book) figure whose
English caption starts with "Figure KEY" (or "Flowchart KEY" when KEY starts with "fc"), and emits
    svg EN || UR || PS / <svg ...> / endsvg
"""
import re, sys, io
from pathlib import Path

HERE = Path(__file__).resolve().parent
C10 = HERE.parents[1] / 'class-10' / 'comp' / 'pages'


def index10():
    figs = {}
    for f in sorted(C10.glob('p*.txt')):
        lines = f.read_text(encoding='utf-8').splitlines()
        i = 0
        while i < len(lines):
            l = lines[i]
            if l.startswith('svg ') or l == 'svg':
                parts = [x.strip() for x in l[4:].split('||')]
                en = parts[1] if len(parts) == 3 else parts[0]
                j = i + 1
                body = []
                while lines[j].strip() != 'endsvg':
                    body.append(lines[j]); j += 1
                m = re.match(r'(Figure|Flowchart|Table)\s+([\w.\-]+)', en)
                key = ({'Figure': 'f', 'Flowchart': 'fc', 'Table': 't'}[m.group(1)] + m.group(2)) if m else f'{f.stem}:{i}'
                figs.setdefault(key, '\n'.join(body))
                figs[f'{f.stem}:{i}'] = '\n'.join(body)
                i = j
            i += 1
    return figs


import json
JMAP = {int(k): v for k, v in json.load(open(HERE / 'jpgmap.json')).items()}
INV = {}
for k_, v_ in sorted(JMAP.items()):
    INV.setdefault(v_, k_)


def expand(n, figs):
    src = (HERE / 'src' / f'p{n:03}.src').read_text(encoding='utf-8')
    out = []
    m_ = re.search(r'^@printed (\d+)', src, re.M)
    if m_ and '@pdf' not in src:
        idx = INV.get(int(m_.group(1)), n)
        if int(m_.group(1)) + 8 != n:
            raise SystemExit(f'p{n:03}: printed {m_.group(1)} should be in p{int(m_.group(1)) + 8:03}')
        if idx != n:
            out.append(f'@pdf {idx + 1}')
    for line in src.splitlines():
        if line.startswith('flow '):
            spec, _, cap = line[5:].partition('||')
            import contextlib, sys as _s
            _s.path.insert(0, str(HERE.parents[1] / 'class-10' / 'tools'))
            import flowsvg
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                flowsvg.main([x.strip() for x in spec.split(';')])
            out += ['svg ' + cap.strip(), buf.getvalue().rstrip(), 'endsvg']
            continue
        if line.startswith('tt '):
            # truth table: tt KIND || caption; KIND = and2/and3/or2/or3/nand2/nor2/xor2/xnor2/not1 or expr:VARS:OUT:pyexpr
            import itertools
            kind, _, cap = line[3:].partition('||')
            kind = kind.strip()
            ops = {'and': ('.', lambda b: int(all(b))), 'or': ('+', lambda b: int(any(b))),
                   'nand': (None, lambda b: 1 - int(all(b))), 'nor': (None, lambda b: 1 - int(any(b))),
                   'xor': (None, lambda b: sum(b) % 2), 'xnor': (None, lambda b: 1 - sum(b) % 2), 'not': (None, lambda b: 1 - b[0])}
            if kind.startswith('expr:'):
                _, vs, outn, ex = kind.split(':', 3)
                names = vs.split(',')
                fn = lambda b: int(eval(ex, {}, dict(zip(names, b))))
            else:
                op, nv = kind.rstrip('0123456789'), int(kind[-1])
                names = ['X', 'Y', 'Z'][:nv] if op != 'not' else ['A']
                sym, fn = ops[op]
                outn = {'and': 'F=X.Y.Z', 'or': 'F=X+Y+Z'}.get(op, op.upper())
                if op in ('and', 'or'):
                    outn = 'F=' + sym.join(names)
            out += ['table ' + cap.strip(), 'th | ' + ' | '.join(names) + ' | ' + outn]
            for bits in itertools.product([0, 1], repeat=len(names)):
                out.append('tr | ' + ' | '.join(map(str, bits)) + f' | {fn(bits)}')
            out.append('endtable')
            continue
        if line.startswith('fig10 '):
            key, _, cap = line[6:].partition('||')
            key = key.strip()
            if key not in figs:
                raise SystemExit(f'p{n:03}: no Class 10 svg for {key}')
            out += ['svg ' + cap.strip(), figs[key], 'endsvg']
        else:
            out.append(line)
    (HERE / 'pages' / f'p{n:03}.txt').write_text('\n'.join(out).rstrip('\n') + '\n', encoding='utf-8')


if __name__ == '__main__':
    figs = index10()
    if sys.argv[1:] == ['keys']:
        print(' '.join(k for k in figs if ':' not in k)); raise SystemExit
    ns = sorted(int(p.stem[1:]) for p in (HERE / 'src').glob('p*.src')) if sys.argv[1:] == ['all'] else [int(a) for a in sys.argv[1:]]
    for n in ns:
        expand(n, figs)
    print('expanded', ns)
