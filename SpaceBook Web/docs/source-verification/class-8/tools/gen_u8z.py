"""Class 8 Maths phase 6c: items whose data sits in the page files (tables, data lists, figure parameters):
statistics (11.2, R11), frequency tables / polygons (11.3, R11), probability (11.4, 11.5, R11), proportion tables,
currency (with the exchange rates implied by the printed key), lines (8.8, R8), Pythagoras and sector items (9.1, 9.2),
cones (R9), polynomials, set-law verification, number-line positions, trapezium constructions.
Writes class-8/math/dsl/u8z.txt.   Run: python gen_u8z.py ; python msol_run.py 8 ; python apply_gen8.py"""
import math
import statistics
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
from itertools import combinations
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'u8z.txt'
L = []


def N(en, ur, ps):
    return f'{en}|{ur}|{ps}'


def kn(k):
    return N(f'The printed key shows {k}, which does not match the data given in the question.',
             f'چھپی کلید {k} دیتی ہے جو سوال کے اعداد سے نہیں ملتا۔',
             f'چاپ شوې کلیل {k} ښیي چې د پوښتنې له شمېرو سره نه جوړیږي.')


def add(key, rows, ans, note=None):
    s = f'{key} ~ ' + ' ;; '.join(rows)
    if note:
        s += ' @@ ' + note
    L.append(s + f' => {ans} %%')


def text(key, en, ur, ps, ans):
    L.append(f'{key} ~ @text {en}|{ur}|{ps} => {ans} %%')


def T(s):
    return rf'\text{{{s}}}'


def frac(f):
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else rf'\frac{{{f.numerator}}}{{{f.denominator}}}'


def fs(f):
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'


# ---------------------------------------------------------------- 11.2 statistics
def stats_rows(data, key_var=None):
    n = len(data)
    mean = Fraction(sum(Fraction(str(x)) for x in data), n)
    dev2 = [(Fraction(str(x)) - mean) ** 2 for x in data]
    pop = sum(dev2) / n
    smp = sum(dev2) / (n - 1)
    return n, mean, pop, smp


def stats_item(key_prefix, data, parts, key_var):
    n, mean, pop, smp = stats_rows(data)
    rng = max(data) - min(data)
    var = pop if abs(float(pop) - key_var) < abs(float(smp) - key_var) else smp
    kind = 'population (÷ n)' if var == pop else 'sample (÷ n − 1)'
    div = n if var == pop else n - 1
    sd = math.sqrt(float(var))
    sdata = ', '.join(str(x) for x in data)
    r_range = rf'\text{{Range}} = {max(data)} - {min(data)} = {rng}'
    r_mean = rf'\bar{{x}} = \frac{{{sdata.replace(", ", " + ")}}}{{{n}}} = {float(mean):.4g}'
    r_var = rf'S^2 = \frac{{\sum (x - \bar{{x}})^2}}{{{div}}} = \frac{{{float(sum((Fraction(str(x)) - mean) ** 2 for x in data)):.2f}}}{{{div}}} = {float(var):.2f}'
    r_sd = rf'S = \sqrt{{{float(var):.2f}}} = {sd:.2f}'
    return rng, var, sd, [r_range, r_mean, r_var, r_sd], kind


marks = [82, 83, 59, 94, 70, 76, 32, 80, 87, 94, 62]
ages = [28, 31, 45, 35, 30, 50, 54, 38, 40, 36]
pages_ = [120, 225, 100, 154, 188, 204, 212, 170]
income = [6000, 65230, 78600, 8000, 9350, 9680, 1030, 1236, 14340, 15000]
for key, data, kv, parts in [('11.2|2', marks, 300.066, 'abc'), ('11.2|3', ages, 67.41, 'abc'), ('11.2|5', pages_, 1737.98, ''), ('11.2|6', income, 680145468.04, '')]:
    rng, var, sd, rows_, kind = stats_item(key, data, parts, kv)
    if parts:
        add(f'{key}|a', [rows_[0]], f'Range = {rng}')
        add(f'{key}|b', [rows_[1], rows_[2]], f'Variance = {float(var):.2f}',
            N(f'Variance is the mean of the squared deviations ({kind}), as in the printed key.', f'تغیر (ویریئنس) انحرافات کے مربعات کی اوسط ہے ({kind})، چھپی کلید کی طرح۔', f'تغیر د انحرافونو د مربعاتو اوسط دی ({kind})، لکه د چاپ شوې کلیل په څېر.'))
        add(f'{key}|c', [rows_[1], rows_[2], rows_[3]], f'Standard deviation = {sd:.2f}')
    else:
        add(f'{key}|', [rows_[0], rows_[1], rows_[2]] + ([rows_[3]] if key.endswith('6') else []),
            f'Range = {rng}, variance = {float(var):.2f}' + (f', standard deviation = {sd:.2f}' if key.endswith('6') else ''))

# Review 11 Q5 range
add('Review Exercise 11|5|', [r'\text{Largest} = 101.5,\; \text{smallest} = 11.6', r'\text{Range} = 101.5 - 11.6 = 89.9'], 'Range = 89.9')


# ---------------------------------------------------------------- frequency tables
def freq_table(data, lo, width, nint):
    out = []
    for i in range(nint):
        a = lo + i * width
        b = a + width - 1 if isinstance(width, int) and all(isinstance(x, int) for x in data) else a + width
        cnt = sum(1 for x in data if a <= x <= b) if (isinstance(width, int) and all(isinstance(x, int) for x in data)) else sum(1 for x in data if a <= x < b)
        out.append((a, b, cnt))
    return out


def poly_marks(rows):
    return [((a + b) / 2, c) for a, b, c in rows]


w = [30, 39, 36.2, 42, 38, 42, 45, 39, 38.2, 41.5, 34, 44.8, 36.2, 38, 41.5, 44.8, 35, 41.5, 39, 42]
ft = [(30, 35, sum(1 for x in w if 30 <= x < 35)), (35, 40, sum(1 for x in w if 35 <= x < 40)),
      (40, 45, sum(1 for x in w if 40 <= x < 45)), (45, 50, sum(1 for x in w if 45 <= x < 50))]
assert sum(c for _, _, c in ft) == 20
add('11.3|1|', [T('Smallest = 30, largest = 45, so use equal classes of width 5 (the upper limit is not included).'),
                T('; '.join(f'{a}-{b}: {c}' for a, b, c in ft)), rf'{" + ".join(str(c) for _, _, c in ft)} = 20'],
    '; '.join(f'{a}–{b}: {c}' for a, b, c in ft) + ' (total 20)')

m2 = [25, 19, 26, 15, 25, 28, 25, 27, 19, 28, 28, 19, 19, 15, 28, 19, 19, 25, 27, 25, 28]
ft2 = [(15, 19, sum(1 for x in m2 if 15 <= x <= 19)), (20, 24, sum(1 for x in m2 if 20 <= x <= 24)), (25, 29, sum(1 for x in m2 if 25 <= x <= 29))]
add('11.3|2|a', [T('Equal classes of width 5: ') + T('; '.join(f'{a}-{b}: {c}' for a, b, c in ft2)),
                 T(f'Only {len(m2)} marks are printed in the question although it says 25 students, so the total is {len(m2)}.')],
    '; '.join(f'{a}–{b}: {c}' for a, b, c in ft2))
top = max(m2)
add('11.3|2|b', [rf'\text{{Highest mark}} = {top}', rf'\text{{Number of students with {top}}} = {m2.count(top)}'], f'{m2.count(top)} students scored {top}')

park = [42, 64, 36, 62, 41, 47, 87, 69, 65, 55, 83, 79, 34, 68, 25, 28, 46, 51, 74, 27, 29, 44, 59, 96, 40, 20, 50, 88, 86, 93]
ftp = [(a, a + 19, sum(1 for x in park if a <= x <= a + 19)) for a in (20, 40, 60, 80)]
assert sum(c for *_, c in ftp) == 30
add('11.3|4|', [T('Smallest = 20, largest = 96; use classes of width 20: ') + T('; '.join(f'{a}-{b}: {c}' for a, b, c in ftp)),
                T('Draw the classes on the x-axis and the frequencies on the y-axis; the bars touch each other (no gaps), with heights ') + ', '.join(str(c) for *_, c in ftp)],
    'Histogram with bar heights ' + ', '.join(str(c) for *_, c in ftp))

books = [195, 206, 100, 98, 150, 210, 195, 106, 195, 168, 180, 212, 104, 195, 100, 216, 195, 209, 112, 99, 206, 116, 195, 100, 142, 100, 135, 98, 160, 155]
ftb = [(a, a + 24, sum(1 for x in books if a <= x <= a + 24)) for a in (95, 120, 145, 170, 195)]
assert sum(c for *_, c in ftb) == 30, sum(c for *_, c in ftb)
pm = [((a + b) / 2, c) for a, b, c in ftb]
add('11.3|5|', [T('Classes of width 25: ') + T('; '.join(f'{a}-{b}: {c}' for a, b, c in ftb)),
                T('Class marks (mid-points): ') + ', '.join(f'{m:g}' for m, _ in pm),
                T('Plot the points ') + ', '.join(f'({m:g}, {c})' for m, c in pm) + T(' and join them with straight lines; close the polygon on the x-axis one class mark before the first and after the last class.')],
    'Frequency polygon through ' + ', '.join(f'({m:g}, {c})' for m, c in pm))


def poly_item(key, rows_, hist=False, lab=''):
    cm = [((a + b) / 2, c) for a, b, c in rows_]
    r = [T('Class marks: ') + ', '.join(f'{m:g}' for m, _ in cm),
         T('Plot the points ') + ', '.join(f'({m:g}, {c})' for m, c in cm) + T(' and join them with straight lines; add a point of frequency 0 before the first and after the last class mark.')]
    if hist:
        r.insert(0, T('Histogram: one bar for each class (no gaps), heights ') + ', '.join(str(c) for *_, c in rows_))
    add(key, r, ('Histogram and ' if hist else '') + 'frequency polygon through ' + ', '.join(f'({m:g}, {c})' for m, c in cm))


poly_item('11.3|6|', [(91, 100, 6), (101, 110, 3), (111, 120, 3), (121, 130, 5), (131, 140, 8)])
poly_item('11.3|7|', [(4, 6, 4), (7, 9, 8), (10, 12, 6), (13, 15, 12)], hist=True)
poly_item('11.3|8|', [(150, 153, 7), (154, 157, 7), (158, 161, 15), (162, 165, 10), (166, 169, 5), (170, 173, 6)])
add('Review Exercise 11|7|', [T('One bar per class, no gaps, heights 5, 9, 12, 10, 7 on the classes 10-15, 15-20, 20-25, 25-30, 30-35.')], 'Histogram with heights 5, 9, 12, 10, 7')
add('Review Exercise 11|8|', [T('One bar per class, no gaps, heights 8, 30, 20, 25, 22 on the classes 20-30, 30-40, 40-50, 50-60, 60-70.')], 'Histogram with heights 8, 30, 20, 25, 22')
poly_item('Review Exercise 11|10|', [(25, 29, 2), (30, 34, 4), (35, 39, 7), (40, 44, 10), (45, 49, 8), (50, 54, 6), (55, 59, 3)], hist=True)
temp = [31, 33, 35, 37, 32, 31, 31, 34, 38, 40, 30, 32, 32, 33, 34, 34, 33, 30, 30, 35, 34, 29, 42, 39, 42, 40, 39, 42, 40, 41]
ftt = [(29, 31, sum(1 for x in temp if 29 <= x <= 31)), (32, 34, sum(1 for x in temp if 32 <= x <= 34)), (35, 37, sum(1 for x in temp if 35 <= x <= 37)),
       (38, 40, sum(1 for x in temp if 38 <= x <= 40)), (41, 43, sum(1 for x in temp if 41 <= x <= 43))]
assert sum(c for *_, c in ftt) == 30
add('Review Exercise 11|9|', [T('Smallest = 29, largest = 42; classes of width 3: ') + T('; '.join(f'{a}-{b}: {c}' for a, b, c in ftt)), rf'{" + ".join(str(c) for *_, c in ftt)} = 30'],
    '; '.join(f'{a}–{b}: {c}' for a, b, c in ftt))

# ---------------------------------------------------------------- probability
def pr(a, b):
    return Fraction(a, b)


add('11.5|2|a', [rf'P_{{exp}}(\text{{head}}) = \frac{{28}}{{50}} = \frac{{14}}{{25}}', r'P_{th}(\text{head}) = \frac{1}{2}', r'\frac{14}{25} = 0.56 > 0.5'], 'Experimental 14/25, theoretical 1/2 (experimental is a little higher)')
add('11.5|2|b', [rf'P_{{exp}}(\text{{tail}}) = \frac{{22}}{{50}} = \frac{{11}}{{25}}', r'P_{th}(\text{tail}) = \frac{1}{2}', r'\frac{11}{25} = 0.44 < 0.5'], 'Experimental 11/25, theoretical 1/2 (experimental is a little lower)')
die = {1: 8, 2: 6, 3: 7, 4: 9, 5: 4, 6: 6}
for p, nm, ev in [('a', 'a 5', {5}), ('b', 'an odd number', {1, 3, 5}), ('c', 'a number less than 2', {1}), ('d', 'a factor of 12', {1, 2, 3, 4, 6}), ('e', 'a multiple of 3', {3, 6})]:
    c = sum(die[k] for k in ev)
    e, t = pr(c, 40), pr(len(ev), 6)
    add(f'11.5|3|{p}', [rf'\text{{Favourable throws}} = {" + ".join(str(die[k]) for k in sorted(ev))} = {c}',
                        rf'P_{{exp}} = \frac{{{c}}}{{40}} = {frac(e)}', rf'P_{{th}} = \frac{{{len(ev)}}}{{6}} = {frac(t)}'],
        f'Experimental {fs(e)}, theoretical {fs(t)}')
btn = {'red': 10, 'yellow': 8, 'blue': 10, 'green': 12}
bag = {'red': 3, 'yellow': 4, 'blue': 6, 'green': 5}
for p, nm, cols in [('a', 'red', ['red']), ('b', 'blue', ['blue']), ('c', 'not green', ['red', 'yellow', 'blue']), ('d', 'yellow', ['yellow'])]:
    c = sum(btn[k] for k in cols)
    t = sum(bag[k] for k in cols)
    e, th = pr(c, 40), pr(t, 18)
    add(f'11.5|4|{p}', [rf'P_{{exp}} = \frac{{{c}}}{{40}} = {frac(e)}', rf'\text{{Bag: }} 3 + 4 + 6 + 5 = 18;\; P_{{th}} = \frac{{{t}}}{{18}} = {frac(th)}'],
        f'Experimental {fs(e)}, theoretical {fs(th)}')
add('11.5|5|', [r'P_{exp}(\text{red}) = \frac{18}{45} = \frac{2}{5}', r'P_{exp}(\text{yellow}) = \frac{12}{45} = \frac{4}{15}', r'P_{exp}(\text{blue}) = \frac{15}{45} = \frac{1}{3}',
                T('The theoretical probabilities depend on how the spinner is divided in the figure (equal parts: 1/3 each); the experimental ones are computed from the table.')],
    'Experimental: red 2/5, yellow 4/15, blue 1/3')
rd = {1: 5, 2: 4, 3: 3, 4: 6, 5: 5, 6: 7}
for p, nm, ev in [('a', 'a 6', {6}), ('b', 'an odd number', {1, 3, 5}), ('c', 'a number less than 4', {1, 2, 3}), ('d', 'a factor of 6', {1, 2, 3, 6})]:
    c = sum(rd[k] for k in ev)
    e, t = pr(c, 30), pr(len(ev), 6)
    add(f'Review Exercise 11|15|{p}', [rf'\text{{Favourable rolls}} = {" + ".join(str(rd[k]) for k in sorted(ev))} = {c}',
                                       rf'P_{{exp}} = \frac{{{c}}}{{30}} = {frac(e)}', rf'P_{{th}} = \frac{{{len(ev)}}}{{6}} = {frac(t)}'],
        f'Experimental {fs(e)}, theoretical {fs(t)}',
        N('The question text mentions a head or a tail; the experiment is a die, so the die probabilities are compared.', 'سوال میں سر یا دم کا ذکر ہے مگر تجربہ پانسے کا ہے، اس لیے پانسے کے احتمالات کا موازنہ کیا گیا ہے۔', 'په پوښتنه کې سر یا لکۍ یاده شوې خو تجربه د پاسې ده، نو د پاسې احتمالات پرتله شوي.'))
add('11.4|4|', [T('The marble is put back, so the first pick does not change the second pick: the events are independent.'),
                r'P(\text{green}) = \frac{3}{17},\quad P(\text{red}) = \frac{7}{17}', r'P(\text{green then red}) = \frac{3}{17} \times \frac{7}{17} = \frac{21}{289}'],
    'Independent; 21/289', kn('21/17 (a probability cannot exceed 1)'))

# ---------------------------------------------------------------- proportion tables
def prop_rows(xs, ys):
    ratios = [Fraction(y, x) for x, y in zip(xs, ys)]
    prods = [x * y for x, y in zip(xs, ys)]
    if len(set(ratios)) == 1:
        return [T('y ÷ x: ') + ',\\; '.join(rf'\frac{{{y}}}{{{x}}} = {frac(r)}' for x, y, r in zip(xs, ys, ratios)), T('The ratio y ÷ x is constant, so y is directly proportional to x (y = kx, k = ') + frac(ratios[0]) + T(').')], 'direct'
    if len(set(prods)) == 1:
        return [T('x × y: ') + ',\\; '.join(rf'{x} \times {y} = {p}' for x, y, p in zip(xs, ys, prods)), T('The product x × y is constant, so y is inversely proportional to x (xy = k, k = ') + str(prods[0]) + T(').')], 'inverse'
    return [T('Neither y ÷ x nor x × y is constant, so the values are not proportional.')], 'none'


r1, k1 = prop_rows([1, 3, 9, 5], [2, 6, 18, 10])
r2, k2 = prop_rows([-35, 20, 55, -15], [7, -4, -11, 3])
add('3.1|13|', [T('Table 1.')] + r1 + [T('Table 2.')] + r2 + [T('Plot each table as points (x, y): the direct one gives a straight line through the origin; the inverse one gives a curve (hyperbola).')],
    f'Table 1: {k1}; Table 2: {k2}')
r1, k1 = prop_rows([3, 4, 5, 6], [9, 12, 15, 18])
r2, k2 = prop_rows([-6, 12, -8, -1], [-4, 2, -3, -24])
add('Review Exercise 3|11|', [T('Table 1.')] + r1 + [T('Table 2.')] + r2 + [T('Plot each table as points (x, y): the direct one gives a straight line through the origin; the inverse one gives a curve (hyperbola).')],
    f'Table 1: {k1}; Table 2: {k2}')

# ---------------------------------------------------------------- currency (rates implied by the printed key of 3.6)
USD, CAD, EUR, GBP = 179.181648, 144.45, 199.64, 239.6635   # the book's own rates (section 3.6, scan pages 54-56)
PUSD, PCAD, PEUR, PGBP = 0.0055809287, 0.0069, 0.0050, 0.0042
RATES = {'USD': USD, 'CAD': CAD, 'EUR': EUR, 'GBP': GBP}
BACK = {'USD': PUSD, 'CAD': PCAD, 'EUR': PEUR, 'GBP': PGBP}
rate_note = N('The exchange rates are the ones printed in section 3.6 of the book: 1 USD = Rs 179.181648, 1 CAD = Rs 144.45, 1 EUR = Rs 199.64, 1 GBP = Rs 239.6635; and 1 PKR = 0.0055809287 USD = 0.0069 CAD = 0.0050 EUR = 0.0042 GBP. Current market rates differ.',
              'شرحیں وہی ہیں جو کتاب کے حصہ 3.6 میں چھپی ہیں: 1 USD = 179.181648 روپے، 1 CAD = 144.45، 1 EUR = 199.64، 1 GBP = 239.6635؛ اور 1 PKR = 0.0055809287 USD = 0.0069 CAD = 0.0050 EUR = 0.0042 GBP۔ آج کی مارکیٹ شرحیں مختلف ہیں۔',
              'نرخونه هغه دي چې د کتاب په 3.6 برخه کې چاپ شوي: 1 USD = 179.181648 روپۍ، 1 CAD = 144.45، 1 EUR = 199.64، 1 GBP = 239.6635؛ او 1 PKR = 0.0055809287 USD = 0.0069 CAD = 0.0050 EUR = 0.0042 GBP. د نن ورځې بازار نرخونه توپیر لري.')
cur1 = [('a', 340, 'USD'), ('b', 120, 'CAD'), ('c', 98, 'EUR'), ('d', 250, 'GBP'), ('e', 29, 'USD'), ('f', 45, 'CAD'), ('g', 444, 'EUR'), ('h', 654, 'GBP')]
for p, amt, c in cur1:
    add(f'3.6|1|{p}', [rf'{amt} \times {RATES[c]} = {amt * RATES[c]:.2f}'], f'Rs {amt * RATES[c]:,.2f}', rate_note)
cur2 = [('a', 600, 'USD'), ('b', 35, 'CAD'), ('c', 897, 'EUR'), ('d', 600, 'GBP'), ('e', 425, 'USD'), ('f', 98, 'CAD'), ('g', 326, 'EUR'), ('h', 562, 'GBP')]
for p, amt, c in cur2:
    add(f'3.6|2|{p}', [rf'{amt} \times {BACK[c]} = {amt * BACK[c]:.4f}'], f'{amt * BACK[c]:.4f} {c}', rate_note)
for p, amt, c in [('a', 23, 'USD'), ('b', 556, 'CAD'), ('c', 67, 'EUR'), ('d', 85, 'GBP'), ('e', 455, 'USD'), ('f', 890, 'CAD'), ('g', 23, 'EUR'), ('h', 456, 'GBP')]:
    add(f'Review Exercise 3|9|{p}', [rf'{amt} \times {RATES[c]} = {amt * RATES[c]:.2f}'], f'Rs {amt * RATES[c]:,.2f}', rate_note)
for p, amt, c in [('a', 456, 'USD'), ('b', 777, 'CAD'), ('c', 89, 'EUR'), ('d', 128, 'GBP'), ('e', 778, 'USD'), ('f', 765, 'CAD'), ('g', 200, 'EUR'), ('h', 989, 'GBP')]:
    add(f'Review Exercise 3|10|{p}', [rf'{amt} \times {BACK[c]} = {amt * BACK[c]:.4f}'], f'{amt * BACK[c]:.4f} {c}', rate_note)

# ---------------------------------------------------------------- lines (8.8, R8 Q12)
def line_rows(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    m = Fraction(y2 - y1, x2 - x1)
    c = y1 - m * x1
    return m, c, [rf'm = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = {frac(m)}', rf'c = y - mx = {y1} - ({frac(m)})({x1}) = {frac(c)}',
                  rf'y = {frac(m)}x + {frac(c)}']


segs = [((-1, -5), (3, 4)), ((-6, 5), (6, 0)), ((-3, -3), (2, 6)), ((2, -6), (5, 5))]
rws, ans = [], []
for i, (a, b) in enumerate(segs, 1):
    m, c, r = line_rows(a, b)
    rws.append(T(f'Line {i}, points {a} and {b}:'))
    rws += r
    ans.append(f'({i}) m = {fs(m)}, y-intercept {fs(c)}')
add('8.8|1|', rws + [T('A positive gradient means the line rises as x increases; a negative gradient means it falls. The y-intercept is where the line cuts the y-axis.')], '; '.join(ans))
add('8.8|2|', [T('A vertical line has the equation x = (the x-value of every point on it).'), r'x = -5,\; x = -3,\; x = 3,\; x = 5'], 'x = −5, x = −3, x = 3, x = 5')
add('8.8|3|', [T('A horizontal line has the equation y = (the y-value of every point on it).'), r'y = 4,\; y = 2,\; y = -3,\; y = -7'], 'y = 4, y = 2, y = −3, y = −7')
rws, ans = [], []
for i, (a, b) in enumerate([((-12, -4), (8, 6)), ((-7, -6), (-2, 4)), ((-1, -6), (2, 6))], 1):
    m, c, r = line_rows(a, b)
    rws.append(T(f'Line {i}, points {a} and {b}:'))
    rws += r
    ans.append(f'({i}) m = {fs(m)}, y-intercept {fs(c)}')
add('Review Exercise 8|12|', rws, '; '.join(ans))
add('8.9|1|', [T('Table 1, y = 2x - 2: '), r'x = 0 \Rightarrow y = -2;\; y = 0 \Rightarrow x = 1;\; x = -1 \Rightarrow y = -4;\; y = 2 \Rightarrow x = 2',
               T('Table 2, y = 1/(2x + 3): '), r'x = 0 \Rightarrow y = \frac{1}{3};\; x = 2 \Rightarrow y = \frac{1}{7};\; x = 1 \Rightarrow y = \frac{1}{5};\; y = 0 \text{ is never reached (a fraction with numerator 1 is never 0)}',
               T('Table 3, y = -3x - 5: '), r'x = 0 \Rightarrow y = -5;\; y = 0 \Rightarrow x = -\frac{5}{3};\; y = -2 \Rightarrow x = -1;\; x = -1 \Rightarrow y = -2'],
    'Tables completed')

# ---------------------------------------------------------------- Pythagoras and sectors
add('9.1|1|', [r'x^2 + 8^2 = 10^2', r'x^2 = 100 - 64 = 36', r'x = \sqrt{36} = 6', r'\text{(iii) } x^2 = 5^2 + 12^2 = 25 + 144 = 169', r'x = \sqrt{169} = 13'],
    '(i) 6, (ii) 15 (the figure for (ii) is not transcribed; value from the printed key), (iii) 13')
add('9.1|2|', [r'\text{(i) } x^2 = 16^2 + 12^2 = 256 + 144 = 400', r'x = \sqrt{400} = 20', r'\text{(iii) } x^2 = 40^2 - 30^2 = 1600 - 900 = 700', r'x = \sqrt{700} = 10\sqrt{7}'],
    '(i) 20, (ii) 10√3 (the figure for (ii) is not transcribed; value from the printed key), (iii) 10√7')
add('9.1|7|', [r'\text{base}^2 = 35^2 - 21^2 = 1225 - 441 = 784', r'\text{base} = \sqrt{784} = 28'], '28 m')
add('9.1|12|', [r'd^2 = 10^2 + 15^2 = 100 + 225 = 325', r'd = \sqrt{325} = 5\sqrt{13} \approx 18.03'], '5√13 km')

sec = [(315, 11, 'm'), (60, 10, 'cm'), (150, 3, 'm'), (210, 12, 'm'), (160, 8, 'cm'), (150, 5, 'cm'), (120, 11, 'cm'), (80, 3, 'm'), (125, 4, 'm')]
rws, ans = [], []
for i, (ang, r, u) in enumerate(sec, 1):
    arc = round(ang / 360 * 2 * 22 / 7 * r, 2)
    area = round(ang / 360 * 22 / 7 * r * r, 2)
    rws.append(rf'\frac{{{ang}}}{{360}} \times 2 \times \frac{{22}}{{7}} \times {r} = {arc:.2f}')
    rws.append(rf'\frac{{{ang}}}{{360}} \times \frac{{22}}{{7}} \times {r}^2 = {area:.2f}')
    ans.append(f'({i}) l = {arc:.2f} {u}, A = {area:.2f} {u}²')
add('9.2|1|', rws, '; '.join(ans))

# cones, spheres (pi = 3.14)
cones = [(4, 5, 3), (4, 5, 3), (14, 50, 48)]
rws, ans = [], []
for i, (r, l, h) in enumerate(cones, 1):
    tsa = round(3.14 * r * (l + r), 2)
    v = round(3.14 * r * r * h / 3, 2)
    rws.append(rf'3.14 \times {r} \times {l + r} = {tsa:.2f}')
    rws.append(rf'\frac{{1}}{{3}} \times 3.14 \times {r}^2 \times {h} = {v:.2f}')
    ans.append(f'({i}) A = {tsa:.2f}, V = {v:.2f}')
add('Review Exercise 9|10|', [r'A = \pi r (l + r), \quad V = \frac{1}{3}\pi r^2 h'] + rws, '; '.join(ans),
    N('Part (ii): r^2 = 5^2 - 3^2 = 16, so r = 4. Part (iii): the diameter 28 gives r = 14 (check 50^2 - 48^2 = 14^2). Rows below give, for each part, the total surface area and then the volume.',
      'حصہ (ii): r^2 = 5^2 - 3^2 = 16، اس لیے r = 4۔ حصہ (iii): قطر 28 سے r = 14 (جانچ 50^2 - 48^2 = 14^2)۔ نیچے ہر حصے کے لیے پہلے کل سطحی رقبہ اور پھر حجم ہے۔',
      'برخه (ii): r^2 = 5^2 - 3^2 = 16، نو r = 4. برخه (iii): قطر 28 r = 14 ورکوي (ازموینه 50^2 - 48^2 = 14^2). لاندې هره برخه لومړی ټوله سطحي ساحه او بیا حجم لري.'))
# ---------------------------------------------------------------- polynomials
add('6.5|1|v', [r'(37x^5 - 33x^4y^3 + 20x^3y^2 + 31y^5) - (10x^5 - 13x^4y^3 + 33x^3y^2)',
                r'= (37 - 10)x^5 + (-33 + 13)x^4y^3 + (20 - 33)x^3y^2 + 31y^5',
                r'= 27x^5 - 20x^4y^3 - 13x^3y^2 + 31y^5'], '27x⁵ − 20x⁴y³ − 13x³y² + 31y⁵',
    N('The printed term "20xy^3y^2" is read as 20x^3y^2, which gives the printed key.', 'چھپا ہوا جزو "20xy^3y^2" کو 20x^3y^2 پڑھا گیا ہے جو چھپی کلید دیتا ہے۔', 'چاپ شوی ټرم "20xy^3y^2" د 20x^3y^2 په توګه لوستل شوی چې چاپ شوې کلیل ورکوي.'))
add('6.7|2|iv', [r'20x^3 \div 5x = 4x^2;\quad 4x^2(5x - 3) = 20x^3 - 12x^2;\quad (20x^3 - 17x^2) - (20x^3 - 12x^2) = -5x^2',
                 r'-5x^2 + 34x \text{ gives } -x(5x - 3) = -5x^2 + 3x;\quad 31x + 15 \text{ remains}',
                 r'\text{Quotient } 4x^2 - x,\; \text{remainder } 31x + 15'], 'Quotient 4x² − x, remainder 31x + 15 (does not divide exactly)',
    N('As printed, 20x³ − 17x² + 34x + 15 is not exactly divisible by 5x − 3; the printed key 4x² − x belongs to 20x³ − 17x² + 3x.', 'جیسا چھپا ہے، 20x³ − 17x² + 34x + 15 کو 5x − 3 پوری طرح تقسیم نہیں کرتا؛ چھپی کلید 4x² − x دراصل 20x³ − 17x² + 3x کی ہے۔', 'لکه څنګه چې چاپ شوی، 20x³ − 17x² + 34x + 15 په 5x − 3 پوره نه وېشل کیږي؛ چاپ شوې کلیل 4x² − x د 20x³ − 17x² + 3x ده.'))
add('6.10|1|o', [r'2tx + 6ty - 3qx - 9qy = 2t(x + 3y) - 3q(x + 3y)', r'= (x + 3y)(2t - 3q)'], '(x + 3y)(2t − 3q)',
    N('The stray "16" after 9qy is a printing mark and is ignored; the printed key (x + y)(2t − 3q) does not match the terms.', 'جزو 9qy کے بعد "16" چھپائی کا نشان ہے اور نظر انداز کیا گیا؛ چھپی کلید (x + y)(2t − 3q) ان جزوں سے نہیں ملتی۔', 'د 9qy وروسته "16" د چاپ نښه ده او پرېښودل شوه؛ چاپ شوې کلیل (x + y)(2t − 3q) له ټرمونو سره نه جوړیږي.'))
text('6.3|2|vii', 'The variables are a, b, c and d (four variables), so it belongs to the group with more than three variables.', 'اس میں متغیرات a, b, c اور d (چار) ہیں، اس لیے یہ تین سے زیادہ متغیرات والے گروہ میں ہے۔', 'په دې کې متغیرونه a, b, c او d (څلور) دي، نو دا له درېیو ډېرو متغیرونو ګروپ کې دی.', '(d) more than three variables')
text('6.3|2|viii', 'The variables are r, b, t and u (four variables), so it belongs to the group with more than three variables.', 'اس میں متغیرات r, b, t اور u (چار) ہیں، اس لیے یہ تین سے زیادہ متغیرات والے گروہ میں ہے۔', 'په دې کې متغیرونه r, b, t او u (څلور) دي، نو دا له درېیو ډېرو متغیرونو ګروپ کې دی.', '(d) more than three variables')

# ---------------------------------------------------------------- sequences, definitions, rational/irrational
seqs = [('i', 2, '+', 3), ('ii', 5, '*', 2), ('iii', 3, '*', 3), ('iv', 1, '+', 4), ('v', 80, '-', 8)]
for p, a, op, d in seqs:
    terms = [a]
    for _ in range(5):
        terms.append(terms[-1] + d if op == '+' else terms[-1] - d if op == '-' else terms[-1] * d)
    kind = 'arithmetic (common difference ' + (f'{d}' if op == '+' else f'-{d}') + ')' if op in '+-' else f'geometric (common ratio {d})'
    pass
rws, ans = [], []
for p, a, op, d in seqs:
    terms = [a]
    for _ in range(5):
        terms.append(terms[-1] + d if op == '+' else terms[-1] - d if op == '-' else terms[-1] * d)
    kind = ('arithmetic, common difference ' + (str(d) if op == '+' else str(-d))) if op in '+-' else f'geometric, common ratio {d}'
    rws.append(T(f'({p}) start {a}, rule: ') + T({'+': f'add {d}', '-': f'subtract {d}', '*': f'multiply by {d}'}[op]) + rf':\; {", ".join(str(t) for t in terms)}, \dots \; \text{{({kind})}}')
    ans.append(f'({p}) {", ".join(str(t) for t in terms[:5])}, … ({kind.split(",")[0]})')
add('6.1|2|', rws, '; '.join(ans))

text('Review Exercise 7|2|', 'An exponent (power) says how many times a base is multiplied by itself; the base is the number being multiplied; the value is the result. Example: in 2^3 = 2 × 2 × 2 = 8 the base is 2, the exponent is 3 and the value is 8.',
     'قوت نما (طاقت) بتاتا ہے کہ اساس کو خود سے کتنی بار ضرب دیا جائے؛ اساس وہ عدد ہے جسے ضرب دیا جاتا ہے؛ قیمت نتیجہ ہے۔ مثال: 2^3 = 2 × 2 × 2 = 8 میں اساس 2، قوت نما 3 اور قیمت 8 ہے۔',
     'توان ښیي چې اساس څو ځله په خپل ځان کې ضرب شي؛ اساس هغه عدد دی چې ضرب کیږي؛ قیمت پایله ده. بېلګه: په 2^3 = 2 × 2 × 2 = 8 کې اساس 2، توان 3 او قیمت 8 دی.',
     'Exponent = number of repeated factors, base = repeated number, value = result')
rat = [('−3½', 'rational (a mixed fraction −7/2)'), ('√12', 'irrational (12 is not a perfect square)'), ('5.7', 'rational (terminating decimal)'),
       ('0', 'rational (0/1)'), ('−8π', 'irrational (π is irrational)'), ('9', 'rational'), ('√25', 'rational (= 5)'), ('π/2', 'irrational'),
       ('12/5', 'rational'), ('4/7', 'rational'), ('√9', 'rational (= 3)'), ('15/38', 'rational'), ('5.2', 'rational (terminating decimal)'),
       ('√17', 'irrational (17 is not a perfect square)'), ('−√16', 'rational (= −4)')]
add('Review Exercise 2|5|', [T('; '.join(f'{a}: {b}' for a, b in rat))],
    'Rational: −3½, 5.7, 0, 9, √25, 12/5, 4/7, √9, 15/38, 5.2, −√16. Irrational: √12, −8π, π/2, √17',
    N('√25, √9 and −√16 are perfect squares (5, 3, −4), so they are rational; the printed key lists them as irrational.', '√25، √9 اور −√16 مکمل مربع ہیں (5، 3، −4)، اس لیے ناطق ہیں؛ چھپی کلید میں انہیں غیر ناطق لکھا ہے۔', '√25، √9 او −√16 بشپړ مربعات دي (5، 3، −4)، نو ناطق دي؛ چاپ شوې کلیل یې غیر ناطق لیکلي.'))


# ---------------------------------------------------------------- number-line positions
def positions(vals):
    rows_ = []
    for label, v in vals:
        lo = math.floor(v)
        rows_.append(rf'\text{{{label}}} \approx {v:.3f}\text{{: between }} {lo} \text{{ and }} {lo + 1}')
    return rows_


add('2.4|1|a', positions([('-1.7', -1.7), ('0.2', 0.2), ('2', 2), ('-3.2', -3.2), ('4', 4)]) + [T('Mark each value at its distance from 0 (to the right if positive, to the left if negative).')], 'Positions marked on the number line')
add('2.4|1|b', positions([('√2', math.sqrt(2)), ('-√5', -math.sqrt(5)), ('2/7', 2 / 7), ('-1/2', -0.5)]), 'Positions marked on the number line')
add('2.4|1|c', positions([('-2', -2), ('-1 2/3', -5 / 3), ('-1 1/3', -4 / 3), ('-1', -1), ('-1/3', -1 / 3)]), 'Positions marked on the number line')
add('2.4|1|d', positions([('3/2', 1.5), ('2', 2), ('2.2', 2.2), ('-2', -2)]), 'Positions marked on the number line')
add('2.4|1|e', positions([('2', 2), ('4', 4), ('0', 0), ('1.5', 1.5), ('1/2', 0.5), ('-3/2', -1.5)]), 'Positions marked on the number line')
add('2.4|1|f', positions([('1 3/7', 10 / 7), ('2.5', 2.5), ('3.5', 3.5), ('-2.2', -2.2), ('-4 3/7', -31 / 7), ('-30/6', -5)]), 'Positions marked on the number line')
add('Review Exercise 2|6|a', positions([('2.4', 2.4), ('-1.9', -1.9), ('3', 3), ('2/3', 2 / 3)]), 'Positions marked on the number line')
add('Review Exercise 2|6|b', positions([('√11', math.sqrt(11)), ('-√3', -math.sqrt(3)), ('3.3', 3.3), ('22/7', 22 / 7), ('-1/5', -0.2)]), 'Positions marked on the number line')
add('Review Exercise 2|6|c', positions([('6', 6), ('0', 0), ('0.5', 0.5), ('3/4', 0.75), ('1/2', 0.5)]), 'Positions marked on the number line')

# ---------------------------------------------------------------- Review 1 Q2 significant figures
def sig(x, n):
    d = Decimal(str(x))
    if d == 0:
        return d
    e = d.adjusted()
    q = Decimal(1).scaleb(e - n + 1)
    return d.quantize(q, rounding=ROUND_HALF_UP)


rws, ans = [], []
for p, x in zip('abcde', ['6729001', '7609168', '23.8712', '0.672451', '45.76217']):
    vals = [sig(x, n) for n in (2, 3, 4, 5)]
    shown = [format(v, 'f') if abs(float(v)) < 1e15 else str(v) for v in vals]
    rws.append(rf'\text{{({p}) }} {x}:\; 2\text{{ s.f.}} = {shown[0]},\; 3\text{{ s.f.}} = {shown[1]},\; 4\text{{ s.f.}} = {shown[2]},\; 5\text{{ s.f.}} = {shown[3]}')
    ans.append(f'({p}) ' + ', '.join(shown))
add('Review Exercise 1|2|', [T('Count significant figures from the first non-zero digit; if the next digit is 5 or more, round up.')] + rws, '; '.join(ans))

# ---------------------------------------------------------------- set laws and Venn counts
def sset(s):
    return '{' + ', '.join(str(x) for x in sorted(s)) + '}'


def verify_laws(X, Y, T_, nx='X', ny='Y', nt='T'):
    rows_ = []
    rows_.append(T(f'{nx} = {sset(X)}, {ny} = {sset(Y)}, {nt} = {sset(T_)}'))
    comm_u = X | Y == Y | X
    comm_i = X & Y == Y & X
    assoc_u = (X | Y) | T_ == X | (Y | T_)
    assoc_i = (X & Y) & T_ == X & (Y & T_)
    d1 = X | (Y & T_) == (X | Y) & (X | T_)
    d2 = X & (Y | T_) == (X & Y) | (X & T_)
    rows_.append(T(f'Commutative: {nx} ∪ {ny} = {sset(X | Y)} = {ny} ∪ {nx}; {nx} ∩ {ny} = {sset(X & Y)} = {ny} ∩ {nx}'))
    rows_.append(T(f'Associative: ({nx} ∪ {ny}) ∪ {nt} = {sset((X | Y) | T_)} = {nx} ∪ ({ny} ∪ {nt}); ({nx} ∩ {ny}) ∩ {nt} = {sset((X & Y) & T_)} = {nx} ∩ ({ny} ∩ {nt})'))
    rows_.append(T(f'Distributive: {nx} ∪ ({ny} ∩ {nt}) = {sset(X | (Y & T_))} = ({nx} ∪ {ny}) ∩ ({nx} ∪ {nt}); {nx} ∩ ({ny} ∪ {nt}) = {sset(X & (Y | T_))} = ({nx} ∩ {ny}) ∪ ({nx} ∩ {nt})'))
    assert comm_u and comm_i and assoc_u and assoc_i and d1 and d2
    return rows_


add('5.3|3|', verify_laws({0, 2, 4, 6, 8, 10}, {4, 8, 12, 16, 20}, {6, 12, 18, 24, 30}) + [T('Show each side in a Venn diagram with three overlapping circles; the shaded regions are equal.')], 'The properties hold for the given sets')
X9, Y9, T9 = {-9, -7, -5, -3, -1, 0, 1, 3}, {-5, -3, -1, 0, 1, 3, 5}, {-10, -5, 0, 5, 10}
add('5.3|9|i', [T(f'X ∪ (Y ∩ T): Y ∩ T = {sset(Y9 & T9)}, so X ∪ (Y ∩ T) = {sset(X9 | (Y9 & T9))}'), T(f'(X ∪ Y) ∩ (X ∪ T): X ∪ Y = {sset(X9 | Y9)}, X ∪ T = {sset(X9 | T9)}, intersection = {sset((X9 | Y9) & (X9 | T9))}'), T('Both sides are equal, so the law is verified.')], 'Verified')
add('5.3|9|ii', [T(f'X ∩ (Y ∪ T): Y ∪ T = {sset(Y9 | T9)}, so X ∩ (Y ∪ T) = {sset(X9 & (Y9 | T9))}'), T(f'(X ∩ Y) ∪ (X ∩ T): X ∩ Y = {sset(X9 & Y9)}, X ∩ T = {sset(X9 & T9)}, union = {sset((X9 & Y9) | (X9 & T9))}'), T('Both sides are equal, so the law is verified.')], 'Verified')
text('5.3|13|', 'Total 160 = only Maths 70 + only Science 50 + both 20 + neither 20. Draw two overlapping circles inside a rectangle: put 70 in the Maths-only part, 50 in the Science-only part, 20 in the overlap and 20 outside the circles.',
     'کل 160 = صرف ریاضی 70 + صرف سائنس 50 + دونوں 20 + کوئی نہیں 20۔ مستطیل کے اندر دو آپس میں ملتے دائرے بنائیں: ریاضی والے حصے میں 70، سائنس والے حصے میں 50، مشترک حصے میں 20 اور دائروں کے باہر 20 لکھیں۔',
     'ټول 160 = یوازې ریاضي 70 + یوازې ساینس 50 + دواړه 20 + هیڅ نه 20. په مستطیل کې دوه یو بل پرې کوونکې دایرې رسم کړئ: په ریاضي برخه کې 70، په ساینس برخه کې 50، په ګډه برخه کې 20 او له دایرو بهر 20 ولیکئ.',
     'Venn diagram with 70, 50, 20 and 20 outside')
VEN = {'only burger': 8, 'only pizza': 10, 'only sandwich': 7, 'burger and pizza only': 4, 'burger and sandwich only': 5, 'pizza and sandwich only': 2, 'all three': 6}
for p, q, v, how in [('a', 'only pizza', 10, 'the pizza-only region'), ('b', 'only sandwich', 7, 'the sandwich-only region'),
                     ('c', 'both pizza and burger', 10, '4 (burger and pizza only) + 6 (all three)'),
                     ('d', 'both sandwich and pizza', 8, '2 (pizza and sandwich only) + 6 (all three)'),
                     ('e', 'only pizza and sandwich', 2, 'the region shared by pizza and sandwich only'), ('f', 'all three', 6, 'the centre region')]:
    add(f'5.3|14|{p}', [T(f'Read the Venn diagram: {how} = {v}')], f'{v} students',
        N('The numbers in the Venn diagram are read as separate regions (for example 4 = burger and pizza only).', 'وین خاکے کی تعداد کو الگ الگ حصے سمجھا گیا ہے (مثلاً 4 = صرف برگر اور پیزا)۔', 'د وین انځور شمېرې جلا جلا برخې ګڼل شوې دي (لکه 4 = یوازې برګر او پیزا).'))

# ---------------------------------------------------------------- trapezium constructions (coordinates checked)
# 10.6 Q1: WX ∥ YZ, ZY = 4.8, WX = 7, WZ = 2.6, angle XYZ = 112
th = math.radians(112)
t = None
a_, b_, c_ = 1.0, 2 * (-(7 - 4.8)) * 0 + 0, 0
# solve |Y + t d - Z'|^2 = 2.6^2 with Z=(0,0), Y=(4.8,0), Z'=(7,0), d=(cos(th)*-1, sin(th))
d = (-math.cos(th), math.sin(th))
A = d[0] ** 2 + d[1] ** 2
B = 2 * ((4.8 - 7) * d[0])
C = (4.8 - 7) ** 2 - 2.6 ** 2
disc = B * B - 4 * A * C
t = (-B + math.sqrt(disc)) / (2 * A)
X = (4.8 + t * d[0], t * d[1])
W = (X[0] - 7, X[1])
assert abs(math.hypot(W[0], W[1]) - 2.6) < 1e-9
add('10.6|1|', [T('Take Z at the origin and Y 4.8 cm to the right (YZ = 4.8 cm).'),
                T('At Y draw the ray YX making 112 degrees with YZ. Mark Z\' on line ZY, 7 cm from Z (beyond Y).'),
                T(f'With centre Z\' and radius 2.6 cm draw an arc to cut the ray at X (YX comes out about {t:.2f} cm).'),
                T('Through X draw XW parallel to YZ, 7 cm long, towards the Z side; join WZ.'),
                T(f'Check: WZ = {math.hypot(W[0], W[1]):.2f} cm, WX = 7 cm, WX parallel to YZ. The trapezium WXYZ is drawn. (Not verified against a drawing in the book.)')],
    'Trapezium WXYZ constructed (YX ≈ %.2f cm)' % t)
# 10.6 Q2: AB ∥ DC, AB = 8.2, BC = 6, AD = 7.5, angle B = 75
hgt = 6 * math.sin(math.radians(75))
dx = math.sqrt(7.5 ** 2 - hgt ** 2)
add('10.6|2|', [T('Draw AB = 8.2 cm. At B draw ∠ABC = 75 degrees and mark C with BC = 6 cm.'),
                T(f'Through C draw a line parallel to AB (height of C above AB = 6 sin 75 = {hgt:.2f} cm).'),
                T(f'With centre A and radius 7.5 cm cut that line at D (horizontal distance of D from A = {dx:.2f} cm).'),
                T('Join AD. ABCD is the trapezium with AB parallel to DC. (Not verified against a drawing in the book.)')],
    f'Trapezium ABCD constructed (height {hgt:.2f} cm)')
add('10.10|4|', [r'\text{Height} = \sqrt{6^2 - 3^2} = \sqrt{27} = 5.196',
                 T('Draw the base 3 cm; at one end draw a perpendicular; with the other end as centre and radius 6 cm cut the perpendicular. Join to complete the right triangle with hypotenuse 6 cm and base 3 cm.')],
    'Right triangle with sides 3 cm, 5.196 cm and hypotenuse 6 cm')

OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'rows ->', OUT)


# ---- merge part-keyed entries into whole-question entries (the stubs for these questions are not split into parts)
def merge(prefix):
    parts, rest = [], []
    for ln in L:
        head = ln.split(' ~', 1)[0]
        if head.startswith(prefix + '|') and len(head) == len(prefix) + 2:
            parts.append(ln)
        else:
            rest.append(ln)
    if not parts:
        return
    rows, answers, note = [], [], None
    for ln in parts:
        head, body = ln.split(' ~', 1)
        label = head[-1]
        body = body.rsplit('%%', 1)[0]
        body, ans = body.rsplit('=>', 1)
        if '@@' in body:
            body, nt = body.split('@@', 1)
            note = note or nt.strip()
        rows.append(rf'\text{{({label})}}')
        rows += [r.strip() for r in body.split(';;') if r.strip()]
        answers.append(f'({label}) {ans.strip()}')
    line = f'{prefix}| ~ ' + ' ;; '.join(rows) + (f' @@ {note}' if note else '') + ' => ' + '; '.join(answers) + ' %%'
    L[:] = rest + [line]


for pre in ['11.2|2', '11.2|3', '11.3|2', '11.5|2', '11.5|3', '11.5|4', 'Review Exercise 11|15', '5.3|14']:
    merge(pre)
OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'rows after merge')
