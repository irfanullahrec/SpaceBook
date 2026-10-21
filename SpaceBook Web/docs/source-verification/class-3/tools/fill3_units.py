"""Answers for the Class 3 Maths compound-unit sums (km/m, kg/g, l/ml add and subtract) that had no `sol` line.

    python fill3_units.py [--write]

The sum is read from the part itself and computed in the small unit, so the answer is always exact.
"""
import re, sys
from pathlib import Path

PAGES = Path(__file__).resolve().parents[1] / 'math' / 'pages'
UNITS = {'km': ('m', 1000, ('kilometres', 'کلومیٹر', 'کیلومتر'), ('metres', 'میٹر', 'متره')),
         'kg': ('g', 1000, ('kilograms', 'کلوگرام', 'کیلوګرام'), ('grams', 'گرام', 'ګرام')),
         'l': ('ml', 1000, ('litres', 'لیٹر', 'لیتر'), ('millilitres', 'ملی لیٹر', 'ملي لیتر'))}
PAT = re.compile(r'^(\d+) (km|kg|l) (\d+) (m|g|ml) ([+−-]) (\d+) (km|kg|l) (\d+) (m|g|ml)$')


def solve(text):
    m = PAT.match(text.strip())
    if not m:
        return None
    a1, u1, a2, u2, op, b1, _, b2, _ = m.groups()
    big, small = u1, UNITS[u1][0]
    f = UNITS[big][1]
    A, B = int(a1) * f + int(a2), int(b1) * f + int(b2)
    v = A + B if op == '+' else A - B
    if v < 0:
        return None
    sign = '+' if op == '+' else '−'
    name_b, name_s = UNITS[big][2], UNITS[big][3]
    ans = f'{v // f} {big} {v % f} {small}'
    verb = ('Add', 'جمع کریں', 'جمع کړئ') if op == '+' else ('Subtract', 'تفریق کریں', 'تفریق کړئ')
    en = (f'{verb[0]} the {name_s[0]} first and then the {name_b[0]}, regrouping 1,000 {name_s[0]} as 1 {big} when needed: '
          f'{A:,} {small} {sign} {B:,} {small} = {v:,} {small} = {ans}.')
    ur = (f'پہلے {name_s[1]} کو {verb[1]}، پھر {name_b[1]} کو، اور ضرورت پر 1,000 {name_s[1]} کو 1 {big} بنائیں: '
          f'{A:,} {small} {sign} {B:,} {small} = {v:,} {small} = {ans}۔')
    ps = (f'لومړی {name_s[2]} {verb[2]}، بیا {name_b[2]}، او اړتیا پر 1,000 {name_s[2]} د 1 {big} په توګه ولیکئ: '
          f'{A:,} {small} {sign} {B:,} {small} = {v:,} {small} = {ans}.')
    return ans, en, ur, ps


def main():
    write = '--write' in sys.argv
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'class-4' / 'tools'))
    import unanswered
    OPEN = {(r[0], r[3], r[4]) for r in unanswered.scan(3, 'math')[1]}
    n = 0
    for p in sorted(PAGES.glob('p*.txt')):
        lines = p.read_text(encoding='utf8').split('\n')
        out, changed = [], False
        for k, line in enumerate(lines):
            out.append(line)
            m = re.match(r'^qp\s+(\S+)\s*\|\s*(.*)$', line)
            if not m:
                continue
            if (p.name, m.group(1), m.group(2).split(' || ')[0][:100]) not in OPEN:
                continue
            r = solve(m.group(2).split(' || ')[0])
            if r:
                out.append(f'sol {r[0]} ## {r[1]} || {r[2]} || {r[3]}')
                n += 1
                changed = True
        if write and changed:
            with open(p, 'w', encoding='utf8', newline='\n') as fh:
                fh.write('\n'.join(out))
    print(f'{"written" if write else "found"}: {n}')


if __name__ == '__main__':
    main()
