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

# Review 8 Q14-Q15 (points transcribed in the page files: p154 and p163)
def quad(x, y):
    return 'on an axis' if x == 0 or y == 0 else ('I' if x > 0 and y > 0 else 'II' if x < 0 < y else 'III' if x < 0 and y < 0 else 'IV')


pts14 = [(2, 11), (14, 10), (-9, 5), (8, -1), (-8, -2), (-11, -7), (14, -9)]
rws = [r'\text{Read each point as (x, y): x from the horizontal axis, y from the vertical axis}'] + [rf'({x}, {y}):\; \text{{Quadrant {quad(x, y)}}}' for x, y in pts14]
with OUT.open('a', encoding='utf-8') as fh:
    fh.write('R8|14| ~ ' + ' ;; '.join(rws) + ' => ' + '; '.join(f'({x}, {y}) Q{quad(x, y)}' for x, y in pts14) + ' %% \n'.replace(' %% \n', ' %%\n'))
pts15 = [('Q', -2, 4), ('S', 1, 4), ('R', 4, 4), ('T', -4, 2), ('U', -3, 1), ('J', 3, 1), ('B', 1, -2), ('L', -4, -3), ('A', 3, -3)]
rws = [r'\text{Ordered pairs of the lettered points: } ' + ',\; '.join(f'{n}({x}, {y})' for n, x, y in pts15),
       r'\text{No lettered point has x-ordinate } 5 \text{ (the largest x is 4); so the ordered pairs are listed by quadrant:}'] + \
      [rf'\text{{Quadrant {q}: }} ' + ',\; '.join(f'{n}({x}, {y})' for n, x, y in pts15 if quad(x, y) == q) for q in ('I', 'II', 'III', 'IV')]
with OUT.open('a', encoding='utf-8') as fh:
    fh.write('R8|15| ~ ' + ' ;; '.join(rws) + ' => QI: S(1, 4), R(4, 4), J(3, 1); QII: Q(−2, 4), T(−4, 2), U(−3, 1); QIII: L(−4, −3); QIV: B(1, −2), A(3, −3) %%\n')

# 9.1 Q1-Q2 (figures read from the scan, p163)
rows = [r'\text{(a) T-shape: top bar } 6 \times 2,\; \text{stem } 3 \text{ wide, } 5 \text{ high}', r'\text{Area} = 6 \times 2 + 3 \times 5 = 12 + 15 = 27',
        r'\text{Perimeter} = 6 + 2 + 1.5 + 5 + 3 + 5 + 1.5 + 2 = 26',
        r'\text{(b) L-shape: bottom } 5,\; \text{inner horizontal } 3 \Rightarrow \text{vertical bar is } 5 - 3 = 2 \text{ wide; height } 4 + 2 = 6',
        r'\text{Area} = 2 \times 6 + 3 \times 2 = 12 + 6 = 18', r'\text{Perimeter} = 2(5 + 6) = 22']
with OUT.open('a', encoding='utf-8') as fh:
    fh.write('9.1|1| ~ ' + ' ;; '.join(rows) + ' => (a) perimeter 26 m, area 27 m²; (b) perimeter 22 m, area 18 m² %%\n')
rows = [r'\text{(a) The shaded region is the 1 m by 1 m square hole}', r'\text{Perimeter} = 4 \times 1 = 4', r'\text{Area} = 1 \times 1 = 1',
        r'\text{(b) The shaded region is the 4 m by 2 m rectangular hole}', r'\text{Perimeter} = 2(4 + 2) = 12', r'\text{Area} = 4 \times 2 = 8']
with OUT.open('a', encoding='utf-8') as fh:
    fh.write('9.1|2| ~ ' + ' ;; '.join(rows) + ' => (a) perimeter 4 m, area 1 m²; (b) perimeter 12 m, area 8 m² %%\n')

# 12.5 Q1 f (figure small; a, b, d follow from the stated angles, c is taken from the key)
note = ('The figure is too small in the scan to read the position of c; a, b and d follow from the marked 105 degrees, 102 degrees and 30 degrees, and c is taken from the printed key.'
        '|شکل سکین میں اتنی چھوٹی ہے کہ c کی جگہ پڑھی نہیں جا سکتی؛ a، b اور d نشان زد 105 ڈگری، 102 ڈگری اور 30 ڈگری سے نکلتے ہیں اور c چھپی کلید سے لیا گیا ہے۔'
        '|انځور په سکین کې دومره کوچنی دی چې د c ځای نه لوستل کیږي؛ a، b او d له نښه شوو 105 درجو، 102 درجو او 30 درجو څخه راځي او c له چاپ شوې کلیل څخه اخیستل شوی.')
with OUT.open('a', encoding='utf-8') as fh:
    fh.write(r'12.5|1|f ~ a = 180 - 105 = 75 ;; b = 180 - 102 - 30 = 48 ;; d = 180 - 75 - 48 = 57 @@ ' + note + ' => a = 75°, b = 48°, c = 32° (from the key), d = 57° %%\n')
