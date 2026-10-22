"""gen_order7.py - Class 7 Unit 1 ordering / comparing items (1.3 Q4, 1.6 Q1-8, Review 1 Q5-6), computed with exact Fractions.
Writes class-7/math/dsl/order.txt (key-checked lines). Lines whose printed key is wrong are re-marked !! by mark_key_errors() after a run."""
import re, json, sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import msol_run

HERE = Path(__file__).resolve().parents[2]
APP = HERE.parent.parent
B = chr(92)
TEXT = B + 'text'
SEMI = B + ';'
FRAC = B + 'frac'


def num(t):
    t = t.strip().replace(' ', '').replace('+', '').replace('$', '')
    m = re.fullmatch(r'(-?)' + re.escape(FRAC) + r'\{(-?\d+)\}\{(-?\d+)\}', t)
    if m:
        s = -1 if m.group(1) else 1
        return s * Fraction(int(m.group(2)), int(m.group(3)))
    return Fraction(t.replace(',', ''))


def split_items(p):
    p = p.strip().strip('$')
    if ';' in p:
        parts = p.split(';')
    elif FRAC in p:
        parts = re.split(r',\s*(?=[-+]?\s*(?:' + re.escape(FRAC) + r'|\d))', p)
    else:
        parts = re.split(r',(?!\d{3}\b)', p)
    return [x.strip() for x in parts if x.strip()]


def tx(v, src=None):
    if src is not None:
        return src.replace('+', '').replace('$', '').strip()
    v = Fraction(v)
    return str(v.numerator) if v.denominator == 1 else f'{FRAC}{{{v.numerator}}}{{{v.denominator}}}'


def main():
    leaves = json.load(open(APP / 'tmp' / 'm7_leaves.json', encoding='utf8'))
    out = []
    for q in leaves:
        key = f"{msol_run.exk(q)}|{q['q']}"
        ex, n, u = q['ex'], q['q'], q['u']
        if (ex, n) in {('1.6', '1'), ('Review Exercise', '5')} and (ex == '1.6' or u == 1):
            for no, pt in q['parts']:
                try:
                    items = split_items(pt)
                    a, b = num(items[0]), num(items[1])
                except Exception:
                    continue
                sym = '>' if a > b else '<' if a < b else '='
                ans = f'{tx(a, items[0])} {sym} {tx(b, items[1])}' if ex == '1.6' else sym
                out.append(f"{key}|{no} ~ {tx(a, items[0])} {sym} {tx(b, items[1])} => {ans}")
        elif (ex, n) in {('1.6', '2'), ('1.6', '4'), ('1.6', '6'), ('1.6', '8'), ('Review Exercise', '6')} and (ex != 'Review Exercise' or u == 1):
            for no, pt in q['parts']:
                try:
                    items = split_items(pt)
                    vals = [(num(i), tx(None, i) if False else tx(num(i), i)) for i in items]
                except Exception:
                    continue
                asc = sorted(vals, key=lambda t: t[0])
                dsc = asc[::-1]
                lt = ' < '.join(s for v, s in asc)
                gt = ' > '.join(s for v, s in dsc)
                out.append(f"{key}|{no} ~ {TEXT}{{Ascending (smallest first):}} {SEMI} {lt} ;; {TEXT}{{Descending (largest first):}} {SEMI} {gt} => Ascending: {', '.join(s for v, s in asc)}; Descending: {', '.join(s for v, s in dsc)}")
        elif (ex, n) == ('1.6', '3'):
            for no, pt in q['parts']:
                try:
                    items = re.split(r'\s+or\s+', pt.strip().replace('$', ''))
                    a, b = num(items[0]), num(items[1])
                except Exception:
                    continue
                big = a if a > b else b
                out.append(f"{key}|{no} ~ {TEXT}{{The number nearer to zero is greater:}} {SEMI} {tx(a)} {'>' if a > b else '<'} {tx(b)} => {tx(big)}")
        elif (ex, n) == ('1.6', '7'):
            for no, pt in q['parts']:
                try:
                    items = [x.strip() for x in pt.split(',')]
                    vals = [Fraction(i) for i in items]
                except Exception:
                    continue
                small = items[vals.index(min(vals))]
                out.append(f"{key}|{no} ~ {TEXT}{{Compare place by place from the left. The smallest of }} {', '.join(items)} {TEXT}{{ is }} {small} ;; {small} => {small}")
        elif (ex, n) == ('1.3', '4'):
            for no, pt in q['parts']:
                try:
                    items = split_items(pt)
                    vals = [(abs(num(i)), str(abs(num(i)))) for i in items]
                except Exception:
                    continue
                asc = sorted(vals, key=lambda t: t[0])
                dsc = asc[::-1]
                out.append(f"{key}|{no} ~ {TEXT}{{Absolute values:}} {SEMI} {', '.join(s for v, s in vals)} ;; {TEXT}{{Ascending:}} {SEMI} {(' ' + B + 'le ').join(s for v, s in asc)} ;; {TEXT}{{Descending:}} {SEMI} {(' ' + B + 'ge ').join(s for v, s in dsc)} => Ascending: {', '.join(s for v, s in asc)}; Descending: {', '.join(s for v, s in dsc)}")
    (HERE / 'class-7' / 'math' / 'dsl' / 'order.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(len(out))


def mark_key_errors():
    import subprocess
    d = json.load(open(APP / 'tmp' / 'disc7.json', encoding='utf8'))
    bad = {x['dsl'] for x in d if x.get('why', '').startswith('key ')}
    p = HERE / 'class-7' / 'math' / 'dsl' / 'order.txt'
    L = p.read_text(encoding='utf-8').split('\n')
    n = 0
    for i, ln in enumerate(L):
        if '~' in ln and ln.split('~')[0].strip() in bad and not ln.rstrip().endswith('!!'):
            L[i] = ln.rstrip() + ' !!'
            n += 1
    p.write_text('\n'.join(L), encoding='utf-8')
    print('marked', n)


if __name__ == '__main__':
    main()
    if len(sys.argv) > 1 and sys.argv[1] == 'mark':
        mark_key_errors()
