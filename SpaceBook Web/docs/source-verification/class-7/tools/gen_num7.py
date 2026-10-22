"""Class 7 Maths phase 2: Unit 1 (place value, rounding, estimation, signed meanings,
number-line positions), 6.1 Q1 descriptive sets, 6.2 Q1-2 sets.
Writes class-7/math/dsl/num_sets2.txt (then: python msol_run.py 7; python build_math7.py)."""
from fractions import Fraction
from math import floor
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'num_sets2.txt'
lines = []


def R(en, ur, ps):
    return '|'.join([en, ur, ps])


def same(t):
    return R(t, t, t)


def emit(key, rows, ans):
    lines.append(f'{key} ~ @text ' + ' ;; '.join(rows) + f' => {ans} %%')


def fmt(n):
    return f'{n:,}'


# ---- 1.1 Q1e
emit('1.1|1|e', [R('A rational number is p/q with q ≠ 0. Here p = 7 and q = −2 ≠ 0, so 7/(−2) = −3.5 is rational.',
                   'ناطق عدد p/q ہوتا ہے جس میں q ≠ 0 ہو۔ یہاں p = 7 اور q = −2 ≠ 0 ہے، اس لیے 7/(−2) = −3.5 ناطق ہے۔',
                   'ناطق عدد p/q وي چې q ≠ 0 وي. دلته p = 7 او q = −2 ≠ 0 دی، نو 7/(−2) = −3.5 ناطق دی.')], 'Rational')

# ---- 1.1 Q2 place values
names = ['Ones', 'Tens', 'Hundreds', 'Thousands', 'Ten-thousands', 'Hundred-thousands', 'Millions']
ur_n = ['اکائی', 'دہائی', 'سیکڑہ', 'ہزار', 'دس ہزار', 'لاکھ', 'دس لاکھ']
ps_n = ['یکې', 'لسیزه', 'سلیزه', 'زرګونه', 'لس زره', 'سل زره', 'ملیونه']
dec_n = ['Tenths', 'Hundredths', 'Thousandths', 'Ten-thousandths']
dec_u = ['دسویں', 'سویں', 'ہزارویں', 'دس ہزارویں']
dec_p = ['لسمه', 'سلمه', 'زرمه', 'لس زرمه']
for p, s in zip('abcdef', ['5487234', '782398', '1572009', '4.186', '8.200', '0.7694']):
    ip, _, fp = s.partition('.')
    en, ur, ps, ans = [], [], [], []
    for i, ch in enumerate(ip):
        k = len(ip) - 1 - i
        en.append(f'{ch} → {names[k]}'); ur.append(f'{ch} ← {ur_n[k]}'); ps.append(f'{ch} ← {ps_n[k]}')
        ans.append(f'{names[k]} {ch}')
    for i, ch in enumerate(fp):
        en.append(f'{ch} → {dec_n[i]}'); ur.append(f'{ch} ← {dec_u[i]}'); ps.append(f'{ch} ← {dec_p[i]}')
        ans.append(f'{dec_n[i]} {ch}')
    emit(f'1.1|2|{p}', [R('Read the digits from the right: ones, tens, hundreds, … and after the point: tenths, hundredths, …',
                         'اکائی سے بائیں طرف: اکائی، دہائی، سیکڑہ، … اور اعشاریہ کے بعد: دسویں، سویں، …',
                         'له یکو څخه چپ لور ته: یکې، لسیزې، سلیزې، … او له اعشاریې وروسته: لسمه، سلمه، …'),
                     R(', '.join(en), ', '.join(ur), ', '.join(ps))], '; '.join(ans))

# ---- 1.2 Q1 rounding
def rnd(n, b):
    return (n + b // 2) // b * b


for p, n in zip('abcd', [53152, 898430, 7431897, 1399267]):
    out = [rnd(n, b) for b in (10, 100, 1000)]
    e = (f'To round, look at the digit just to the right of the place: 5 or more rounds up, 4 or less keeps the digit. '
         f'{fmt(n)} → nearest 10: {fmt(out[0])}; nearest 100: {fmt(out[1])}; nearest 1000: {fmt(out[2])}.')
    u = (f'گول کرنے کے لیے مطلوبہ مقام کے دائیں ہندسے کو دیکھیں: 5 یا زیادہ ہو تو اوپر، 4 یا کم ہو تو وہی رہتا ہے۔ '
         f'{fmt(n)} ← قریب ترین 10: {fmt(out[0])}؛ 100: {fmt(out[1])}؛ 1000: {fmt(out[2])}۔')
    s = (f'د ګردولو لپاره د مطلوب ځای ښي لور ته رقم وګورئ: 5 یا ډېر وي پورته، 4 یا لږ وي همدا پاتې کیږي. '
         f'{fmt(n)} ← نږدې 10: {fmt(out[0])}؛ 100: {fmt(out[1])}؛ 1000: {fmt(out[2])}.')
    extra = ' (the printed key shows 74318900 for the first two; 7,431,900 is correct)' if p == 'c' else ''
    emit(f'1.2|1|{p}', [R(e, u, s)], f'{fmt(out[0])}, {fmt(out[1])}, {fmt(out[2])}{extra}')

# ---- 1.2 Q2 calculate and estimate
def sig1(n):
    d = len(str(n)) - 1
    return rnd(n, 10 ** d)


items = {'a': (6258, '+', 3422), 'b': (11852, '+', 48412), 'c': (15203, '-', 10545), 'd': (49396, '-', 22415),
         'e': (624, '×', 23), 'f': (988, '×', 18), 'g': (13216, '÷', 56), 'h': (32436, '÷', 34)}
for p, (x, op, y) in items.items():
    if op in '+-':
        ex, ey = rnd(x, 1000), rnd(y, 1000)
    else:
        ex, ey = sig1(x), sig1(y)
    f = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '×': lambda a, b: a * b, '÷': lambda a, b: Fraction(a, b)}[op]
    exact, est = f(x, y), f(ex, ey)
    exs = fmt(exact) if exact == int(exact) else f'{float(exact):.2f}'
    ests = fmt(est) if est == int(est) else f'{float(est):.0f}'
    ok = abs(float(est) - float(exact)) / float(exact) <= 0.1
    v_en, v_ur, v_ps = (('reasonable', 'معقول', 'معقول') if ok else ('not close enough', 'قریب نہیں', 'نږدې نه دی'))
    emit(f'1.2|2|{p}', [R(f'Exact: {fmt(x)} {op} {fmt(y)} = {exs}', f'درست: {fmt(x)} {op} {fmt(y)} = {exs}', f'سم: {fmt(x)} {op} {fmt(y)} = {exs}'),
                       R(f'Estimate (round each number first): {fmt(ex)} {op} {fmt(ey)} ≈ {ests}',
                         f'اندازہ (پہلے ہر عدد گول کریں): {fmt(ex)} {op} {fmt(ey)} ≈ {ests}',
                         f'اټکل (لومړی هر عدد ګرد کړئ): {fmt(ex)} {op} {fmt(ey)} ≈ {ests}'),
                       R(f'The estimate {ests} is {v_en} when compared with {exs} (within 10 % counts as reasonable). The printed key rounds differently, so its estimates differ.',
                         f'اندازہ {ests}، {exs} کے مقابلے میں {v_ur} ہے (10 فیصد کے اندر ہو تو معقول)۔ چھپی کلید مختلف طریقے سے گول کرتی ہے، اس لیے اندازے مختلف ہیں۔',
                         f'اټکل {ests} د {exs} په پرتله {v_ps} دی (په 10 سلنې کې وي نو معقول). چاپ شوې کلیل بل ډول ګردوي، نو اټکلونه توپیر لري.')],
         f'{exs} (estimate {ests}, {v_en})')

# ---- 1.3 Q1 number line, Q2 opposite sign
nl = {'i': ('−2 to +5', 'Draw a line, mark 0, then −2, −1, 0, 1, 2, 3, 4, 5 with filled dots.', 'ایک لکیر کھینچیں، 0 لگائیں، پھر −2 سے +5 تک تمام صحیح اعداد ٹھوس نقطوں سے ظاہر کریں۔', 'یوه کرښه رسم کړئ، 0 وټاکئ، بیا له −2 تر +5 ټول بشپړ عددونه ډک ټکو سره وښایاست.'),
      'ii': ('−8 to 0', 'Mark −8, −7, …, −1, 0 with filled dots to the left of and at zero.', '−8, −7, …, −1, 0 کو صفر کے بائیں طرف اور صفر پر ٹھوس نقطوں سے ظاہر کریں۔', '−8, −7, …, −1, 0 د صفر په کیڼ لور او په صفر کې ډک ټکو سره وښایاست.'),
      'iii': ('−5 to +5', 'Mark −5, −4, …, 0, …, +4, +5 with filled dots; zero is in the middle.', '−5 سے +5 تک ہر صحیح عدد ٹھوس نقطے سے ظاہر کریں؛ صفر درمیان میں ہے۔', 'له −5 تر +5 هر بشپړ عدد په ډک ټکي وښایاست؛ صفر په منځ کې دی.')}
for p, (rng, e, u, s) in nl.items():
    emit(f'1.3|1|{p}', [R(e, u, s)], f'Integers {rng} marked on the number line')

for p, (given, ans) in {'i': ('−2', '+2'), 'ii': ('+5', '−5'), 'iii': ('+10', '−10'), 'iv': ('−7', '+7'), 'v': ('−23', '+23')}.items():
    emit(f'1.3|2|{p}', [R(f'The corresponding number has the opposite sign: {given} → {ans}.',
                         f'متعلقہ عدد کی علامت الٹ ہوتی ہے: {given} ← {ans}۔',
                         f'اړوند عدد مخالفه نښه لري: {given} ← {ans}.')], ans)

def mean(key, e, u, s, a):
    emit(key, [R(e, u, s)], a)


mean('1.3|5|', 'Paying money out is a loss for Junaid, so it is negative: −30.', 'رقم ادا کرنا جنید کے لیے نقصان ہے، اس لیے منفی: −30۔', 'پیسې ورکول د جنید لپاره تاوان دی، نو منفي: −30.', '−30 (negative)')
mean('1.3|6|', 'Receiving money is a gain, so it is positive: +200.', 'رقم ملنا فائدہ ہے، اس لیے مثبت: +200۔', 'پیسې ترلاسه کول ګټه ده، نو مثبت: +200.', '+200')
mean('1.3|7|', '+6 is 6 m above sea level, so −6 is the opposite: 6 m below sea level.', '+6 کا مطلب سطح سمندر سے 6 میٹر اوپر ہے، اس لیے −6 کا مطلب 6 میٹر نیچے۔', '+6 یعنې د سمندر له سطحې 6 متره پورته، نو −6 یعنې 6 متره لاندې.', '6 m below sea level')
mean('1.3|8|', '−10 is 10 units to the left of zero, so +5 is 5 units to the right of zero.', '−10 کا مطلب صفر سے 10 اکائی بائیں، اس لیے +5 کا مطلب صفر سے 5 اکائی دائیں۔', '−10 یعنې له صفر 10 واحده کیڼ لور ته، نو +5 یعنې له صفر 5 واحده ښي لور ته.', '5 units to the right of zero')
mean('1.3|9|', '−20 is a loss of Rs. 20, so +50 is a profit of Rs. 50. (The printed key shows Rs 5, which does not match.)', '−20 یعنی 20 روپے کا نقصان، اس لیے +50 یعنی 50 روپے کا منافع۔ (چھپی کلید میں 5 روپے ہیں جو درست نہیں۔)', '−20 یعنې 20 روپۍ تاوان، نو +50 یعنې 50 روپۍ ګټه. (چاپ شوې کلیل 5 روپۍ لري چې سمه نه ده.)', 'Profit of Rs. 50')
mean('1.3|10|', '+40 is a clockwise turn, so −30 is the opposite: an anticlockwise turn of 30.', '+40 گھڑی کی سمت گھماؤ ہے، اس لیے −30 الٹی سمت (اینٹی کلاک وائز) 30 کا گھماؤ ہے۔', '+40 د ساعت په لوري ګرځېدل دي، نو −30 د ساعت په مخالف لوري 30 ګرځېدل دي.', 'Anticlockwise turn of 30')

# ---- 1.4 Q1 fractions on number line
fr = {'a': ['3/4'], 'b': ['-2/5'], 'c': ['6/4', '-35/14'], 'd': ['10/15', '-8/24'], 'e': ['7/4', '9/2', '-11/4'],
      'f': ['1/2', '-4/7', '-13/4'], 'g': ['9/2', '-11/2'], 'h': ['11/4', '-39/26', '-14/12']}
for p, lst in fr.items():
    es, us, ps_ = [], [], []
    for t in lst:
        v = Fraction(t)
        lo = floor(v)
        d = v.denominator
        sgn = '−' if v < 0 else ''
        txt = f'{sgn}{abs(v.numerator)}/{d}' if d != 1 else str(v)
        es.append(f'{txt} = {float(v):.3g} lies between {lo} and {lo + 1}: divide each unit into {d} equal parts and count {abs(v - lo) * d if v >= 0 else (v - lo) * d} part(s) right of {lo}')
        us.append(f'{txt} = {float(v):.3g}، {lo} اور {lo + 1} کے درمیان ہے: ہر اکائی کو {d} برابر حصوں میں بانٹیں اور {lo} سے دائیں {(v - lo) * d} حصے گنیں')
        ps_.append(f'{txt} = {float(v):.3g}، د {lo} او {lo + 1} تر منځ دی: هره واحده په {d} مساوي برخو وویشئ او له {lo} څخه ښي لور ته {(v - lo) * d} برخې وشمیرئ')
    emit(f'1.4|1|{p}', [R('; '.join(es), '؛ '.join(us), '؛ '.join(ps_))], ', '.join(lst) + ' marked')

# ---- 1.4 Q5 integer ranges
for p, (a, b) in zip('abcdefgh', [(-7, 6), (-9, 7), (-10, 0), (-5, 13), (-5, 10), (-2, 7), (-4, 5), (-2, 0)]):
    emit(f'1.4|5|{p}', [R(f'Draw a number line that includes {a} to {b}; put a filled dot on every integer from {a} to {b}. It has {b - a + 1} points.',
                         f'ایک عددی لکیر کھینچیں جس میں {a} سے {b} تک شامل ہو؛ {a} سے {b} تک ہر صحیح عدد پر ٹھوس نقطہ لگائیں۔ کل {b - a + 1} نقطے ہیں۔',
                         f'یوه عددي کرښه رسم کړئ چې له {a} تر {b} پکې وي؛ له {a} تر {b} پر هر بشپړ عدد ډک ټکی کېږدئ. ټول {b - a + 1} ټکي دي.')],
         f'{b - a + 1} points marked')

# ---- 6.1 Q1 descriptive
D6 = {'a': 'Set of solar months starting with the letter J', 'b': 'The set of the first five letters of the English alphabet',
      'c': 'Set of integers between −5 and 0', 'd': 'Set of the weekdays just before and just after Friday',
      'e': 'Set of even numbers between 0 and 10', 'f': 'Set of even numbers greater than 12',
      'g': 'Set of positive odd numbers', 'h': 'Set of even numbers between 8 and 22 except 18',
      'i': 'The set of positive even numbers', 'j': 'Set of odd numbers between 99 and 111',
      'k': 'Set of whole numbers', 'l': 'Set of squares of the first five natural numbers',
      'm': 'Set of the first five odd numbers', 'n': 'Set of the first four multiples of 11'}
for p, d in D6.items():
    note = ''
    if p == 'h': note = ' (the set as printed lists 10, 12, 14, 16, 20)'
    emit(f'6.1|1|{p}', [R('Descriptive form states the common property of the elements in words. Find what every element has in common.',
                         'بیانیہ صورت میں عناصر کی مشترک خصوصیت الفاظ میں لکھی جاتی ہے۔ دیکھیں کہ تمام عناصر میں کیا بات مشترک ہے۔',
                         'تشریحي بڼه کې د عناصرو ګډه ځانګړتیا په ټکو لیکل کیږي. وګورئ چې ټول عناصر کوم ګډ شی لري.'),
                     R(d + note, d + note, d + note)], d + note)

# ---- 6.2 Q1 tabular infinite sets
T6 = {'a': ('N', '{1, 2, 3, …}'), 'b': ('W', '{0, 1, 2, 3, …}'), 'c': ('Z', '{0, ±1, ±2, ±3, …}'), 'd': ('E⁺', '{2, 4, 6, …}'),
      'e': ('O', '{±1, ±3, ±5, ±7, …}'), 'f': ('P', '{2, 3, 5, 7, 11, …}'), 'g': ('K', '{4, 6, 8, 9, 10, 12, …}')}
for p, (s, v) in T6.items():
    emit(f'6.2|1|{p}', [R('Tabular form lists the elements; for an infinite set write the first few and then three dots (…).',
                         'جدولی صورت میں عناصر لکھے جاتے ہیں؛ لامحدود سیٹ میں پہلے چند عناصر لکھ کر تین نقطے (…) لگائیں۔',
                         'جدولي بڼه کې عناصر لیکل کیږي؛ بې پایه سیټ کې لومړي څو عناصر ولیکئ او بیا درې ټکي (…) کېږدئ.'),
                     R(f'{s} = {v}', f'{s} = {v}', f'{s} = {v}')], f'{s} = {v}')

# ---- 6.2 Q2 Venn
V6 = {'a': ('N', 'Z', 'every natural number is an integer'), 'b': ('E⁺', 'W', 'every positive even number is a whole number'),
      'c': ('P', 'W', 'every prime is a whole number'), 'd': ('N', 'Q', 'every natural number is rational'),
      'e': ('N', 'W', 'every natural number is a whole number')}
for p, (a, b, why) in V6.items():
    emit(f'6.2|2|{p}', [R(f'{a} ⊂ {b} because {why}. Draw a large circle for {b} and a smaller circle for {a} entirely inside it.',
                         f'{a} ⊂ {b} کیونکہ {a} کا ہر عنصر {b} میں موجود ہے۔ {b} کے لیے بڑا دائرہ اور اس کے اندر {a} کے لیے چھوٹا دائرہ بنائیں۔',
                         f'{a} ⊂ {b} ځکه چې د {a} هر عنصر په {b} کې دی. د {b} لپاره لوی دایره او د {a} لپاره یې په منځ کې کوچنۍ دایره رسم کړئ.')],
         f'{a} inside {b}')

OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(len(lines), 'rows ->', OUT)
