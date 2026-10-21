"""Turn one-line answers whose explanation already states a single checked arithmetic fact ("... 670 ÷ 100 = 6.7 m ...")
into a short chain the animated solution can show.

    CLS=5 python upgrade_why.py [--write]

Only `sol ANSWER ## why` lines whose `why` (English part) contains `A op B = R` with plain numbers are touched, the fact is
re-computed here and must be true, and the line must be the only answer line of its item. The original explanation stays
as step 1. Facts that are false are printed and not changed.
"""
import re, sys
from decimal import Decimal
from pathlib import Path
import arith4

HERE = arith4.HERE
FACT = re.compile(r'(\d[\d,]*(?:\.\d+)?)\s*(×|÷|\+|−|-|x)\s*(\d[\d,]*(?:\.\d+)?)\s*=\s*(\d[\d,]*(?:\.\d+)?)')
OPS = {'×': 'x', 'x': 'x', '÷': '/', '+': '+', '−': '-', '-': '-'}
SYM = {'x': r'\times', '/': r'\div', '+': '+', '-': '-'}


def D(s):
    return Decimal(s.replace(',', ''))


def process(path, write):
    src = path.read_text(encoding='utf8').split('\n')
    out, n, bad, i = [], 0, [], 0
    while i < len(src):
        line = src[i]
        out.append(line)
        m = re.match(r'^(q|qp)\s+(\S+)\s*\|', line)
        if m:
            j, ans = i + 1, []
            while j < len(src) and not re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', src[j]):
                if re.match(r'^(sol|solution|qsol|qsolve|ss|sm)\b', src[j]):
                    ans.append(j)
                j += 1
            if len(ans) == 1 and src[ans[0]].startswith('sol ') and '##' in src[ans[0]]:
                head, _, why = src[ans[0]][4:].partition('##')
                en = why.split(' || ')[0]
                facts = FACT.findall(en)
                if len(facts) == 1:
                    a, o, b, r = facts[0]
                    op = OPS[o]
                    A, B, R = D(a), D(b), D(r)
                    val = A * B if op == 'x' else A + B if op == '+' else A - B if op == '-' else (A / B if B else None)
                    if val is not None and val.normalize() == R.normalize():
                        row = f'{arith4.t(A) if A == A.to_integral() else a} {SYM[op]} {arith4.t(B) if B == B.to_integral() else b} = {arith4.t(R) if R == R.to_integral() else r}'
                        row = row.replace(',', '{,}') if ',' in row and '{,}' not in row else row
                        out.extend(src[i + 1:ans[0]])
                        out.append('solution ' + head.strip())
                        out.append('ss ' + why.strip())
                        out.append('sm ' + row)
                        i = ans[0] + 1
                        n += 1
                        continue
                    elif val is not None:
                        bad.append(f'{path.name} {m.group(2)}: {a} {o} {b} is {val.normalize()} not {r}')
        i += 1
    if write and n:
        with open(path, 'w', encoding='utf8', newline='\n') as f:
            f.write('\n'.join(out))
    return n, bad


if __name__ == '__main__':
    tot, allbad = 0, []
    for p in sorted((HERE / 'math' / 'pages').glob('p*.txt')):
        n, bad = process(p, '--write' in sys.argv)
        tot += n
        allbad += bad
    print(f'{"upgraded" if "--write" in sys.argv else "can upgrade"}: {tot}; false facts: {len(allbad)}')
    for b in allbad[:20]:
        print('  ', b)
