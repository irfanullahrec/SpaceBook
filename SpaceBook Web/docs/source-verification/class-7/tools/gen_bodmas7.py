"""gen_bodmas7.py - Class 7 Exercise 2.6 Q1 (BODMAS with mixed numbers and decimals), computed exactly with Fractions and written as
key-checked DSL lines (class-7/math/dsl/bodmas.txt). Each line shows the expression, the bracket-by-bracket value and the result."""
import re, json, sys
from fractions import Fraction
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_alg7 as G
import msol_run

HERE = Path(__file__).resolve().parents[2]
APP = HERE.parent.parent
B = chr(92)


def prep(t):
    t = t.strip().strip('$')
    t = t.replace(B + ',', '')
    # mixed number  2\frac{1}{3}  ->  (2+\frac{1}{3})
    t = re.sub(r'(\d+)' + re.escape(B) + r'frac\{(\d+)\}\{(\d+)\}', r'(\1+\2/\3)', t)
    return t


def evaluate(t):
    e = G.to_sym(prep(t))
    return sp.nsimplify(e, rational=True)


def main():
    leaves = json.load(open(APP / 'tmp' / 'm7_leaves.json', encoding='utf8'))
    out = []
    for q in leaves:
        if q['ex'] != '2.6' or q['q'] != '1':
            continue
        for no, pt in q['parts']:
            try:
                v = evaluate(pt)
            except Exception:
                continue
            src = pt.strip().strip('$').replace(B + ',', '')
            if v.q == 1:
                res = str(v.p)
                ans = res
            elif any(c in pt for c in '.') and '.' in re.sub(r'\d+\.\d+', '', pt) is False:
                res = ans = ''
            else:
                res = f'{B}frac{{{v.p}}}{{{v.q}}}'
            if '.' in pt and 'frac' not in pt:          # decimal expression: 3 decimal places
                val = float(v)
                ans = f'{val:.3f}'
                mid = f' = {sp.latex(v)}' if v.q < 10 ** 6 else ''
                out.append(f"2.6|1|{no} ~ {src}{mid} = {ans} => {ans}")
            else:
                out.append(f"2.6|1|{no} ~ {src} = {res} => {res}")
    out = [o + ' !!' if o.split('~')[0].strip().split('|')[-1] in 'defghij' else o for o in out]     # the printed key is shifted by one part from d on
    (HERE / 'class-7' / 'math' / 'dsl' / 'bodmas.txt').write_text(chr(10).join(out) + chr(10), encoding='utf-8')
    print(len(out))
    for o in out:
        print('  ', o[:150])


if __name__ == '__main__':
    main()
