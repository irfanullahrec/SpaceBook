"""Class 7 Maths 13.7 Q2-Q3, read from the scan (spinner sectors 1,2,2,3,3,4,5,6; jar of 3 squares, 3 circles, 3 triangles).
Writes math/dsl/prob7.txt."""
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'prob7.txt'
L = []


def fr(f):
    return str(f.numerator) if f.denominator == 1 else rf'\frac{{{f.numerator}}}{{{f.denominator}}}'


sp = [1, 2, 2, 3, 3, 4, 5, 6]
ev = [('a', 'P(<3)', lambda x: x < 3), ('b', 'P(not 5)', lambda x: x != 5), ('c', 'P(smaller than 6)', lambda x: x < 6),
      ('d', 'P(odd)', lambda x: x % 2 == 1), ('e', 'P(prime)', lambda x: x in (2, 3, 5)), ('f', 'P(even)', lambda x: x % 2 == 0),
      ('g', 'P(10)', lambda x: x == 10)]
rows, ans = [r'\text{Spinner sectors read from the figure: } 1, 2, 2, 3, 3, 4, 5, 6 \; (8 \text{ equal sectors})'], []
for k, nm, f in ev:
    c = sum(1 for x in sp if f(x))
    p = F(c, 8)
    rows.append(rf'\text{{({k}) {nm}: }} \frac{{{c}}}{{8}} = {fr(p)}')
    rows.append(rf'1 - {fr(p)} = {fr(1 - p)}')
    ans.append(f'({k}) {p}, complement {1 - p}')
L.append('13.7|2| ~ ' + ' ;; '.join(rows) + ' => ' + '; '.join(ans) + ' %%')
rows3 = [r'\text{Jar: 3 square + 3 circular + 3 triangular buttons} = 9']
items = [('i', 'square', 3), ('ii', 'a button', 9), ('iii', 'NOT a button', 0), ('iv', 'circular', 3), ('v', 'triangular', 3),
         ('vi', 'NOT a rectangular', 9)]
a3 = []
for k, nm, c in items:
    p = F(c, 9)
    rows3.append(rf'\text{{({k}) P({nm}): }} \frac{{{c}}}{{9}} = {fr(p)}')
    rows3.append(rf'1 - {fr(p)} = {fr(1 - p)}')
    a3.append(f'({k}) {p}, complement {1 - p}')
rows3.append(r'\text{Certain: (ii) and (vi) (probability 1); impossible: (iii) (probability 0)}')
L.append('13.7|3| ~ ' + ' ;; '.join(rows3) + ' => ' + '; '.join(a3) + '; certain: ii, vi; impossible: iii %%')
OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L))

# 13.6 Q4 grouped mean (table read from the scan)
cls = [(1, 10, 2), (11, 20, 7), (21, 30, 10), (31, 40, 3), (41, 50, 1)]
mids = [(a + b) / 2 for a, b, _ in cls]
sfx = sum(m * f for m, (_, _, f) in zip(mids, cls))
n = sum(f for *_, f in cls)
r13 = [r'\text{Mid-points: } 5.5,\; 15.5,\; 25.5,\; 35.5,\; 45.5', rf'\sum f = {" + ".join(str(f) for *_, f in cls)} = {n}',
       rf'\sum fx = {" + ".join(f"{f} \times {m:g}" for m, (_, _, f) in zip(mids, cls))} = {sfx:g}',
       rf'\text{{Mean}} = \frac{{{sfx:g}}}{{{n}}} = {sfx / n:.2f}']
with OUT.open('a', encoding='utf-8') as fh:
    fh.write('13.6|4| ~ ' + ' ;; '.join(r13) + f' => {sfx / n:.2f} m %%\n')

# Review 13 Q12 marbles (bag read from the scan: 3 red, 6 green, 3 blue = 12)
items = [('i', 'red', 3), ('ii', 'green', 6), ('iii', 'blue', 3), ('iv', 'not blue', 9), ('v', 'marble', 12), ('vi', 'yellow', 0), ('vii', 'not a marble', 0)]
rws, ans = [r'\text{Bag read from the figure: } 3 \text{ red} + 6 \text{ green} + 3 \text{ blue} = 12 \text{ marbles}'], []
for k, nm, c in items:
    p = F(c, 12)
    rws.append(rf'\text{{({k}) P({nm}): }} \frac{{{c}}}{{12}} = {fr(p)}')
    rws.append(rf'1 - {fr(p)} = {fr(1 - p)}')
    ans.append(f'({k}) {p}, complement {1 - p}')
rws.append(r'\text{Certain: (v) (probability 1); impossible: (vi) and (vii) (probability 0); no two colours are equally likely except red and blue (} \frac{1}{4} \text{ each)}')
with OUT.open('a', encoding='utf-8') as fh:
    fh.write('R13|12| ~ ' + ' ;; '.join(rws) + ' => ' + '; '.join(ans) + '; certain: v; impossible: vi, vii; equally likely: red and blue %%\n')

# Review 5 Q9 income tax (the book's worked example uses 5 %; the question gives no rebate)
note = ('The question gives no rate and no rebate; the book\'s example in this unit uses 5 %, and 5 % of the whole income gives the printed key. If a rebate such as Rs 400,000 applied, there would be no tax.'
        '|سوال میں نہ شرح دی گئی ہے نہ رعایتی حد؛ اس باب کی مثال میں 5 فیصد استعمال ہوا ہے اور پوری آمدنی کے 5 فیصد سے چھپی کلید ملتی ہے۔ اگر 4,00,000 روپے جیسی رعایتی حد لاگو ہوتی تو ٹیکس صفر ہوتا۔'
        '|په پوښتنه کې نه نرخ ورکړل شوی نه معافي حد؛ د دې څپرکي بېلګه 5 سلنه کاروي او د ټول عاید 5 سلنه چاپ شوې کلیل ورکوي. که د 4,00,000 روپیو غوندې معافي حد پلی کېده نو مالیه به صفر وای.')
with OUT.open('a', encoding='utf-8') as fh:
    fh.write(r'R5|9| ~ \text{Income tax at 5 \%} = 236000 \times \frac{5}{100} = 11800 @@ ' + note + ' => Rs 11,800 %%\n')
