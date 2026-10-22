"""Class 7 Maths phase 5b: data that sits in the page files (tables, graphs, data lists), BODMAS 2.6 d-j, and key-driven
option judgements for the conceptual Review multiple-choice items (each says whether the option is the printed-key answer).
Needs tmp/m7_leaves.json (node tmp/mdump.cjs 7). Writes class-7/math/dsl/data_mcq.txt; then
    python msol_run.py 7 ; python build_math7.py"""
import json
import math
import re
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parent / 'math' / 'dsl' / 'data_mcq.txt'
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


F = Fraction

# ---- 1.3 Q3
add('1.3|3|', [T('The numerical value (absolute value) of a number is its distance from 0, so the sign is dropped.'),
               r'|+2| = 2,\; |+7| = 7,\; |0| = 0,\; |-1| = 1,\; |-7| = 7,\; |+5| = 5,\; |-5| = 5,\; |-15| = 15,\; |+13| = 13,\; |+12| = 12,\; |-14| = 14'],
    '2, 7, 0, 1, 7, 5, 5, 15, 13, 12, 14')

# ---- 2.6 d-j BODMAS
d_ = F(15, 8) / (F(5, 6) * (F(12, 5) * (F(4, 5) - F(1, 2))))
e_ = F(5, 4) ** 2 * (F(6, 25) / F(3, 5) + (F(1, 3) + F(9, 2) - F(7, 3)))
f_ = 3.3 + 2.02 * (50.85 - 32.15)
g_ = 3.9 ** 2 + (15.89 * 22.8 - 70.1)
h_ = 0.088 * (3.1 + 2.02 * (2 - 0.75))
i_ = 9 - (2.4285 + (1.0714 / 0.7142))
j_ = 5.5 - (1.55 * ((3.25 - 0.25) * 0.572))
add('2.6|1|d', [r'\frac{4}{5} - \frac{1}{2} = \frac{3}{10}', r'2\frac{2}{5} \times \frac{3}{10} = \frac{12}{5} \times \frac{3}{10} = \frac{18}{25}', r'\frac{5}{6} \times \frac{18}{25} = \frac{3}{5}',
                r'1\frac{7}{8} \div \frac{3}{5} = \frac{15}{8} \times \frac{5}{3} = \frac{25}{8}'], r'3\frac{1}{8}')
add('2.6|1|e', [r'\left(1\frac{1}{4}\right)^2 = \left(\frac{5}{4}\right)^2 = \frac{25}{16}', r'\frac{6}{25} \div \frac{3}{5} = \frac{6}{25} \times \frac{5}{3} = \frac{2}{5}',
                r'\frac{1}{3} + 4\frac{1}{2} - 2\frac{1}{3} = \frac{1}{3} + \frac{9}{2} - \frac{7}{3} = \frac{5}{2}', r'\frac{2}{5} + \frac{5}{2} = \frac{29}{10}',
                r'\frac{25}{16} \times \frac{29}{10} = \frac{145}{32}'], r'4\frac{17}{32}')
add('2.6|1|f', [r'50.85 - 32.15 = 18.7', r'2.02 \times 18.7 = 37.774', r'3.3 + 37.774 = 41.074'], '41.074')
add('2.6|1|g', [r'3.9^2 = 15.21', r'15.89 \times 22.8 = 362.292', r'362.292 - 70.1 = 292.192', r'15.21 + 292.192 = 307.402'], '307.402')
add('2.6|1|h', [r'2 - 0.75 = 1.25', r'2.02 \times 1.25 = 2.525', r'3.1 + 2.525 = 5.625', r'0.088 \times 5.625 = 0.495'], '0.495')
add('2.6|1|i', [r'1.0714 \div 0.7142 = 1.5001', r'2.4285 + 1.5001 = 3.9286', r'9 - 3.9286 = 5.0714'], '5.071')
add('2.6|1|j', [r'3.25 - 0.25 = 3', r'3 \times 0.572 = 1.716', r'1.55 \times 1.716 = 2.6598', r'5.5 - 2.6598 = 2.8402'], '2.840')

# ---- 5.1 Q1 profit / loss table
tab = [('a', 1800, 1500, None), ('b', 2450, 2200, None), ('c', 4000, None, ('profit', 1260)), ('d', 6425, None, ('loss', 200)), ('e', 9000, None, ('loss', 2000))]
rws, ans = [], []
for p, cp, sp, other in tab:
    rws.append(T(f'({p})'))
    if sp is not None:
        loss = cp - sp
        pct = loss / cp * 100
        rws += [rf'{cp} - {sp} = {loss}', rf'rac{{{loss}}}{{{cp}}} 	imes 100 = {pct:.2f}']
        ans.append(f'({p}) loss Rs {loss}, loss % {pct:.2f}')
    elif other[0] == 'profit':
        sp = cp + other[1]
        pct = other[1] / cp * 100
        rws += [rf'{cp} + {other[1]} = {sp}', rf'rac{{{other[1]}}}{{{cp}}} 	imes 100 = {pct:.2f}']
        ans.append(f'({p}) S.P. Rs {sp}, profit % {pct:.2f}')
    else:
        sp = cp - other[1]
        pct = other[1] / cp * 100
        rws += [rf'{cp} - {other[1]} = {sp}', rf'rac{{{other[1]}}}{{{cp}}} 	imes 100 = {pct:.2f}']
        ans.append(f'({p}) S.P. Rs {sp}, loss % {pct:.2f}')
add('5.1|1|', rws, '; '.join(ans))

# ---- 7.2 Q2 table
expr = [('u² + v − 5', 'u, v', '1, 1', '2 and 1', '−5'), ('3a² + b + 8', 'a, b', '3, 1', '2 and 1', '8'), ('4x + 6y² − 4', 'x, y', '4, 6', '1 and 2', '−4'),
        ('−⅓y⁴ + y + 1', 'y', '−1/3, 1', '4 and 1', '1'), ('8a² − 7a³ + a²', 'a', '8, −7, 1', '2, 3, 2', 'none')]
add('7.2|2|', [T('; '.join(f'{e}: variables {v}; coefficients {c}; exponents {x}; constant {k}' for e, v, c, x, k in expr))],
    '; '.join(f'{e}: variables {v}, coefficients {c}, exponents {x}, constant {k}' for e, v, c, x, k in expr))

# ---- 8.5 Q2
add('8.5|2|', [T('The point (x, y) is in Quadrant I when x > 0 and y > 0; II when x < 0, y > 0; III when x < 0, y < 0; IV when x > 0, y < 0.'),
               T('(3, 3): x = 3, y = 3, Quadrant I. (-3, -2): x = -3, y = -2, Quadrant III. (-5, -4): x = -5, y = -4, Quadrant III. (7, -6): x = 7, y = -6, Quadrant IV. No point lies in Quadrant II.')],
    'QI: (3, 3); QII: none; QIII: (−3, −2), (−5, −4); QIV: (7, −6)')

# ---- 10.3 Q3 times
add('10.3|3|', [T('(a) 1:01 a.m. + 5 h 15 min = 6:16 a.m.'), T('(b) arrival 7:20 p.m. (19:20) - 11 h 2 min = 8:18 a.m.'),
                T('(c) 8:55 p.m. to 6:20 a.m.: 8:55 p.m. to midnight = 3 h 5 min, plus 6 h 20 min = 9 h 25 min'), T('(d) 10:40 a.m. + 5 h 50 min = 4:30 p.m.')],
    '(a) 6:16 a.m.; (b) 8:18 a.m.; (c) 9 h 25 min; (d) 4:30 p.m.')

# ---- 12.5 Q2, Q3
add('12.5|2|', [r'\angle A = 90,\; \angle C = 68', r'\angle B = 180 - 90 - 68 = 22'], '22°')
add('12.5|3|', [T('Isosceles triangle: the angles opposite the equal sides are equal, so a = b.'), r'a + b = 180 - 52 = 128', r'a = b = \frac{128}{2} = 64'], '∠a = 64°, ∠b = 64°')

# ---- 13 graphs and tables
add('13.1|2|', [T('Read the bars: textbooks Mon 15, Tue 19, Wed 23, Thu 33; notebooks Mon 8, Tue 39, Wed 18, Thu 33.'),
                T('(a) 15  (b) 23  (c) least notebooks: Monday (8)  (d) greatest notebooks: Tuesday (39)  (e) 39 + 18 = 57'),
                T('(f) total books per day: Mon 23, Tue 58, Wed 41, Thu 66, so Thursday')],
    '(a) 15; (b) 23; (c) Monday; (d) Tuesday; (e) 57; (f) Thursday',
    kn('(b) 25 and (e) 60 (the graph values read 23 and 57)'))
add('13.2|1|', [T('Toys by month: Jan 2000, Feb 3000, Mar 1500, Apr 5800, May 3500, Jun 4900.'),
                T('(a) highest: April (5800)  (b) decrease: February to March and April to May, i.e. in March and May  (c) 3500 - 1500 = 2000  (d) 5800 - 2000 = 3800')],
    '(a) April; (b) March and May (the months after a fall); (c) 2000; (d) 3800',
    kn('(b) February and April and (d) 4000'))
pie = {'above 50': 72, 'above 70': 100, 'above 80': 108, 'above 90': 80}
st = {k: v / 360 * 90 for k, v in pie.items()}
add('13.3|5|', [T('Each sector angle shows part of 360 degrees, which stands for 90 students: students = angle / 360 x 90.'),
                T('Above 50: 72/360 x 90 = 18; above 70: 100/360 x 90 = 25; above 80: 108/360 x 90 = 27; above 90: 80/360 x 90 = 20.'),
                T('(e) between 50 and 80: 18 + 25 = 43  (f) between 70 and 90: 25 + 27 = 52  (g) ratio above 50 : above 90 = 18 : 20 = 9 : 10  (h) 27 - 18 = 9')],
    '(a) 18; (b) 25; (c) 27; (d) 20; (e) 43; (f) 52; (g) 9 : 10; (h) 9')
h = [130, 125, 125, 126, 127, 127, 128, 128, 128, 129, 125, 140, 142, 143, 144, 144, 146, 146, 147, 149,
     134, 135, 135, 136, 136, 137, 137, 138, 138, 139, 139, 130, 131, 131, 131, 132, 132, 133, 133, 133]
cls = [(125, 129), (130, 134), (135, 139), (140, 144), (145, 149)]
fr = [(a, b, sum(1 for x in h if a <= x <= b)) for a, b in cls]
add('13.4|3|', [T('Count the tally for each class: ' + '; '.join(f'{a}-{b}: {c}' for a, b, c in fr) + f' (total {sum(c for *_, c in fr)})'),
                T('(a) class size 5  (b) the classes with equal frequency: 125-129 and 135-139 (10 each)  (c) highest frequency: 130-134  (d) lowest frequency: 145-149  (e) upper limit of 135-139 is 139  (f) lower limit of 130-134 is 130')],
    '; '.join(f'{a}–{b}: {c}' for a, b, c in fr))
add('13.4|7|', [T('(a) 3 classes  (b) 24 + 10 + 15 = 49 students  (c) lowest data value (lower limit of the first class) = 55  (d) 70-84: 10 students  (e) 70 or more: 10 + 15 = 25')],
    '(a) 3; (b) 49; (c) 55; (d) 10; (e) 25', kn('(c) 10'))
add('13.6|2|', [r'60 + 72 + 58 + 66 + 54 + 63 + 77 + 60 + 59 + 71 = 640', r'\text{Mean} = \frac{640}{10} = 64'], '64 kg')
add('13.6|5|', [T('Mid-points: 2, 4, 6, 8.'), r'\sum f = 12 + 22 + 27 + 19 = 80', r'\sum fx = 12(2) + 22(4) + 27(6) + 19(8) = 24 + 88 + 162 + 152 = 426', r'\text{Mean} = \frac{426}{80} = 5.325'], '5.325 years')
data = sorted([36, 25, 32, 40, 28, 35, 26, 32, 30, 27, 32, 28, 39, 20, 35])
add('13.6|6|', [T('Arranged in order: ' + ', '.join(map(str, data))), T('15 values, so the median is the 8th value = ' + str(data[7])), T('32 occurs 3 times (more than any other value), so the mode is 32')], 'median = 32, mode = 32')

# ---- 1.4 number lines
add('1.4|4|a', [T('x > 7 means every number greater than 7 but not 7 itself: 8, 9, 10, 11, 12, ... Draw a number line from 0 to 12, put an open circle at 7 and an arrow to the right (or dots on 8 to 12 with an arrow).')], 'Open circle at 7 with an arrow to the right')
add('1.4|6|a', [T('Between 0 and 0.2 the line is divided into 4 big parts of 0.05, and each big part into 5 small parts of 0.01.'),
                T('The boxes: 0.02 = 2 small parts after 0; 0.11 = 0.10 + 1 small part; 0.18 = 0.15 + 3 small parts.')], '0.02, 0.11, 0.18')
add('1.4|7|a', [T('Divide 6.2 to 6.9 into tenths and mark 6.2, 6.6 and 6.9.')], '6.2, 6.6 and 6.9 marked on the number line')
add('1.4|7|b', [T('Order the values 0.1, 0.3, 0.5, 0.8 and mark each on a number line from 0 to 1 divided into tenths.')], '0.1, 0.3, 0.5, 0.8 marked on the number line')


def pos(items):
    out = []
    for lab, v in items:
        out.append(T(f'{lab} = {float(v):.3f} lies between {math.floor(v)} and {math.floor(v) + 1}'))
    return out


R12 = [('a', [('-5/4', F(-5, 4))]), ('b', [('8/5', F(8, 5))]), ('c', [('15/2', F(15, 2)), ('-7/4', F(-7, 4))]), ('d', [('1/15', F(1, 15)), ('-3/2', F(-3, 2))]),
       ('e', [('17/3', F(17, 3)), ('-18/2', F(-9))]), ('f', [('23', F(23)), ('24', F(24)), ('27', F(27))]), ('g', [('-1', F(-1)), ('-4', F(-4)), ('-11', F(-11))]),
       ('h', [('-2', F(-2)), ('-8', F(-8)), ('-15', F(-15))])]
for p, items in R12:
    add(f'R1|2|{p}', pos(items) + [T('Mark each value at that position on the number line.')], 'Marked on the number line')

# ---- 9.6 prisms (triangle with given sides / height)
# e: triangle sides 8.4, 13, 14.9, height 9 on base 13?  Not consistent, so only the sound parts are reported.
text('9.6|1|e', 'The triangle sides 8.4, 13 and 14.9 cm do not agree with a height of 9 cm on any of those bases (the area from Heron\'s formula is 54.4 cm², but the base 13 with height 9 gives 58.5 cm²), so the surface area cannot be computed reliably from the printed data. The printed key shows 683.2.',
     'مثلث کے اطراف 8.4، 13 اور 14.9 سینٹی میٹر 9 سینٹی میٹر اونچائی سے کسی بھی قاعدے پر مطابقت نہیں رکھتے (ہیرون فارمولا سے رقبہ 54.4 مربع سینٹی میٹر، جبکہ قاعدہ 13 اور اونچائی 9 سے 58.5)، اس لیے چھپے اعداد سے سطحی رقبہ قابلِ اعتماد طور پر نہیں نکالا جا سکتا۔ چھپی کلید 683.2 دیتی ہے۔',
     'د درې ګوني اړخونه 8.4، 13 او 14.9 سانتي متره د 9 سانتي متره لوړوالي سره په هیڅ یوه قاعده سمون نه لري (د هیرون فورمول مساحت 54.4 مربع سانتي متره، خو قاعده 13 او لوړوالی 9 له 58.5 ورکوي)، نو له چاپ شوو شمېرو سطحي ساحه په باوري ډول نه ایستل کیږي. چاپ شوې کلیل 683.2 ښيي.',
     'Not computable from the printed data')
text('9.6|1|f', 'The triangle sides 11.4, 12 and 14.2 m with height 11 m are not consistent either (Heron gives area 67.4 m²; base 12 with height 11 would give 66), so the surface area cannot be computed reliably from the printed data. The printed key shows 395.2.',
     'مثلث کے اطراف 11.4، 12 اور 14.2 میٹر اور اونچائی 11 میٹر بھی مطابقت نہیں رکھتے (ہیرون سے رقبہ 67.4 مربع میٹر، قاعدہ 12 اور اونچائی 11 سے 66)، اس لیے چھپے اعداد سے سطحی رقبہ قابلِ اعتماد طور پر نہیں نکالا جا سکتا۔ چھپی کلید 395.2 دیتی ہے۔',
     'د درې ګوني اړخونه 11.4، 12 او 14.2 متره او لوړوالی 11 متره هم سمون نه لري (هیرون مساحت 67.4 مربع متره، قاعده 12 او لوړوالی 11 له 66 ورکوي)، نو له چاپ شوو شمېرو سطحي ساحه په باوري ډول نه ایستل کیږي. چاپ شوې کلیل 395.2 ښيي.',
     'Not computable from the printed data')

# ---- 10.2 Q5e
add('10.2|5|e', [r'465 \text{ minutes} = 7 \text{ h } 45 \text{ min} = 27900 \text{ seconds}', T('As printed ("minutes and seconds") the question is read as: 465 minutes = 465 minutes 0 seconds.')],
    '465 min 0 s (= 7 h 45 min)', kn('420 min 35 s'))

# ---- key-driven option judgements for the conceptual multiple-choice items
g = json.load(open(HERE.parent / 'math' / 'gen_solutions.json', encoding='utf8'))
leaves = json.load(open(ROOT / 'tmp' / 'm7_leaves.json', encoding='utf8'))
keyof, txt = {}, {}
for l in leaves:
    ex = l['ex'] if not l['ex'].startswith('Review') else 'R%d' % l['u']
    if l['q'] == '1' and l.get('key'):
        keyof[ex] = {a: re.findall(r'[ivx]+', b) for a, b in re.findall(r'\b([a-z])\)\s*([ivx]+(?:\s*,\s*[ivx]+)*)', l['key'])}
    for p, t in l['parts']:
        txt[f'{ex}|{l["q"]}|{p}'] = t
own = {ln.split(' ~')[0] for ln in OUT.read_text(encoding='utf-8').splitlines() if ' ~' in ln} if OUT.exists() else set()
done = {ln.split(' ~')[0] for ln in L}
opt_re = re.compile(r'\b(iv|iii|ii|i)[\.\)]\s')
n_mcq = 0
for k, v in g.items():
    if not (v.get('derived') or k in own) or k in done:
        continue
    ex, q, p = (k.split('|') + ['', ''])[:3]
    if q != '1' or ex not in keyof or p not in keyof[ex] or k not in txt:
        continue
    t = txt[k]
    i = t.rfind('(i')
    if i < 0:
        continue
    tail = t[i + 1:].rstrip(') ').rstrip()
    ms = list(opt_re.finditer(tail))
    if len(ms) < 3:
        continue
    opts = {m.group(1): tail[m.end(): (ms[j + 1].start() if j + 1 < len(ms) else len(tail))].strip() for j, m in enumerate(ms)}
    right = keyof[ex][p]
    if not all(r in opts for r in right) or any(c in x for x in opts.values() for c in ('|', '~', ';;', '=>', '@@', '%%')):
        continue
    names = ', '.join(f'{r}) {opts[r]}' for r in right)
    stem = t[:i].strip()
    if any(c in stem for c in ('|', '~', ';;', '=>', '@@', '%%')):
        stem = ''
    text(k, f'The correct option is {names} (answer from the printed key).', f'درست آپشن {names} ہے (چھپی کلید کے مطابق)۔', f'سم انتخاب {names} دی (د چاپ شوې کلیل له مخې).', f'Option {names}')
    n_mcq += 1

OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'rows;', n_mcq, 'option judgements')
