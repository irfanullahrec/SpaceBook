"""Class 7 Maths phase 5: computable Review Exercise items R1-R13. Writes math/dsl/review2.txt."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'review2.txt'
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


add('R1|1|e', [r'54.231 \approx 54'], '54')
add('R2|1|a', [r'\frac{7}{9} + \frac{1}{2} = \frac{14 + 9}{18} = \frac{23}{18} = 1\frac{5}{18}'], r'$1\frac{5}{18}$')
add('R2|1|b', [r'\frac{5}{13} + \frac{-7}{26} = \frac{10}{26} - \frac{7}{26} = \frac{3}{26}'], r'$\frac{3}{26}$')
add('R2|1|c', [r'\frac{-11}{15} + \frac{-2}{15} = \frac{-13}{15}'], r'$\frac{-13}{15}$')
add('R2|1|e', [r'\frac{14}{21} = \frac{14 \div 7}{21 \div 7} = \frac{2}{3}'], r'$\frac{2}{3}$')
add('R2|1|f', [r'\frac{1}{6} + \frac{-2}{5} = \frac{5}{30} - \frac{12}{30} = \frac{-7}{30}'], r'$\frac{-7}{30}$')
add('R2|1|g', [T('The additive inverse of a number is the number with the opposite sign: ') + r'-\frac{5}{6}'], r'$\frac{-5}{6}$')
add('R4|1|c', [r'20 : 15 = \frac{20}{15} = \frac{4}{3} = 4 : 3'], '4 : 3')
add('R4|1|e', [r'12 : 4 = 3 : 1 = 6 : 2'], '6 : 2', kn('option ii (2 : 1)'))
add('R4|1|h', [r'76 \times \frac{5}{2} = 38 \times 5 = 190'], '190', kn('option i (32)'))
add('R5|1|a', [r'\text{Loss} = 72 - 60 = 12', r'\text{Loss \%} = \frac{12}{72} \times 100 = 16.67'], '16.67%')
add('R5|1|b', [r'\text{Marked price} = 30 + 5 = 35'], 'Rs 35')
add('R5|1|h', [r'\text{Commission} = 5000 \times \frac{5}{100} = 250'], 'Rs 250')

sets2 = {'a': '{square, rectangle, trapezium, kite, rhombus}', 'b': '{2, 3, 5, 7, 11, 13, …}', 'c': '{3, 6, 9, 12, 15}',
         'd': 'ϕ', 'e': '{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39}',
         'f': '{1, 3, 5, 7, 9, 11, 13, 15, 17}'}
why2 = {'a': N('Five different shapes with four sides.', 'چار اطراف والی پانچ مختلف شکلیں۔', 'څلور اړخونو لرونکې پنځه بېلابېلې بڼې.'),
        'b': N('Prime numbers have exactly two factors (1 and itself); the list never ends.', 'مفرد اعداد کے صرف دو جزو ہوتے ہیں (1 اور خود)؛ فہرست ختم نہیں ہوتی۔', 'لومړني عددونه یوازې دوه فکتورونه لري (1 او خپله)؛ لیست نه ختمیږي.'),
        'c': N('3 × 1, 3 × 2, 3 × 3, 3 × 4, 3 × 5.', '3 × 1، 3 × 2، 3 × 3، 3 × 4، 3 × 5۔', '3 × 1، 3 × 2، 3 × 3، 3 × 4، 3 × 5.'),
        'd': N('The factors of 45 are 1, 3, 5, 9, 15, 45: all are odd, so there is no even factor.', '45 کے جزو 1, 3, 5, 9, 15, 45 ہیں: سب طاق ہیں، اس لیے کوئی جفت جزو نہیں۔', 'د 45 فکتورونه 1, 3, 5, 9, 15, 45 دي: ټول تاق دي، نو جفت فکتور نشته.'),
        'e': N('Composite numbers have more than two factors; those below 40 are listed in order (1 is neither prime nor composite).', 'مرکب اعداد کے دو سے زیادہ جزو ہوتے ہیں؛ 40 سے کم ایسے اعداد ترتیب سے لکھے ہیں (1 نہ مفرد ہے نہ مرکب)۔', 'مرکب عددونه له دوو ډېر فکتورونه لري؛ له 40 څخه کم عددونه په ترتیب لیکل شوي (1 نه لومړنی دی نه مرکب).'),
        'f': N('Odd numbers less than 18: 1, 3, …, 17.', '18 سے چھوٹے طاق اعداد: 1, 3, …, 17۔', 'له 18 څخه کوچني تاق عددونه: 1, 3, …, 17.')}
for p, v in sets2.items():
    L.append(f'R6|2|{p} ~ @text {why2[p]} ;; {v}|{v}|{v} => {v} %%')
desc = {'a': 'Set of natural numbers', 'b': 'Set of natural numbers less than 7', 'c': 'Set of the first six multiples of 5',
        'd': 'Set of the first four prime numbers', 'e': 'Set of the first four multiples of 5'}
for p, d in desc.items():
    L.append(f'R6|3|{p} ~ @text Descriptive form states the common property in words: {d}.|بیانیہ صورت میں مشترک خصوصیت الفاظ میں لکھی جاتی ہے: {d}۔|تشریحي بڼه کې ګډه ځانګړتیا په ټکو لیکل کیږي: {d}. => {d} %%')
rel = {'a': 'X ∪ Y = X', 'b': 'Y ∪ X = X', 'c': 'X ∩ Y = Y', 'd': 'Y ∩ X = Y'}
for p, v in rel.items():
    e = 'Every element of Y (10, 20, 30, …) is also in X (multiples of 5), so Y ⊂ X.'
    L.append(f'R6|4|{p} ~ @text {e}|Y کا ہر عنصر (10, 20, 30, …) X (5 کے مضاعف) میں بھی ہے، اس لیے Y ⊂ X۔|د Y هر عنصر (10, 20, 30, …) په X (د 5 مضربونه) کې هم دی، نو Y ⊂ X. ;; {v}|{v}|{v} => {v} %%')

text('R8|1|b', 'A linear equation has variables with power 1 only. In 3x + 5y² = 12 the power of y is 2, so it is not linear.', 'خطی مساوات میں متغیر کی طاقت صرف 1 ہوتی ہے۔ 3x + 5y² = 12 میں y کی طاقت 2 ہے، اس لیے یہ خطی نہیں۔', 'خطي معادله کې د متغیر توان یوازې 1 وي. په 3x + 5y² = 12 کې د y توان 2 دی، نو دا خطي نه ده.', '3x + 5y² = 12 (option ii)')
text('R8|1|f', 'A linear equation in two variables has x and y, both to the power 1: 3x − y = 6.', 'دو متغیرات والی خطی مساوات میں x اور y دونوں کی طاقت 1 ہوتی ہے: 3x − y = 6۔', 'په دوو متغیرونو کې خطي معادله کې x او y دواړه توان 1 لري: 3x − y = 6.', '3x − y = 6 (option ii)')
add('R8|1|h', [r'x = -2, y = -3: \quad 2(-2) - (-3) = -4 + 3 = -1'], 'x = −2 and y = −3 (option iv)')
text('R8|1|j', 'The 3rd quadrant has x < 0 and y < 0. The point (−1, 2) has y = 2 > 0, so it is not in the 3rd quadrant.', 'تیسرے کواڈرنٹ میں x < 0 اور y < 0 ہوتے ہیں۔ نقطہ (−1, 2) میں y = 2 > 0 ہے، اس لیے وہ تیسرے کواڈرنٹ میں نہیں۔', 'په دریمه څلورمه کې x < 0 او y < 0 وي. نقطه (−1, 2) کې y = 2 > 0 دی، نو دا په دریمه څلورمه کې نه ده.', '(−1, 2) (option iii)')
text('R8|2|', 'An equation with one variable and power 1 is linear: for example 2x + 3 = 0, x + 5 = 0, 3x − 4 = 0.', 'ایک متغیر اور طاقت 1 والی مساوات خطی ہوتی ہے، مثلاً 2x + 3 = 0، x + 5 = 0، 3x − 4 = 0۔', 'یو متغیر او توان 1 لرونکې معادله خطي وي، لکه 2x + 3 = 0، x + 5 = 0، 3x − 4 = 0.', '2x + 3 = 0; x + 5 = 0; 3x − 4 = 0')
text('R8|3|a', 'On a horizontal line every point has the same y-value, so its equation is y = c.', 'افقی لکیر کے ہر نقطے کی y قیمت یکساں ہوتی ہے، اس لیے مساوات y = c ہے۔', 'په افقي کرښه کې د هر ټکي y قیمت یو شان وي، نو معادله y = c ده.', 'y = c')
text('R8|3|b', 'On a vertical line every point has the same x-value, so its equation is x = c.', 'عمودی لکیر کے ہر نقطے کی x قیمت یکساں ہوتی ہے، اس لیے مساوات x = c ہے۔', 'په عمودي کرښه کې د هر ټکي x قیمت یو شان وي، نو معادله x = c ده.', 'x = c')

add('R10|1|a', [r'5 \times 60 = 300'], '300 minutes')
add('R10|1|b', [r'500 \div 100 = 5'], '5 metres')
add('R10|1|c', [T('1 km = 1000 m, so multiply by ') + r'1000'], '1000')
for p, r, a in [('a', r'8 \times 100 = 800', '800 cm'), ('b', r'5 \times 1000 + 70 = 5070', '5070 m'), ('c', r'110 \times 10 = 1100', '1100 mm'),
                ('d', r'50 \times 100 + 6 = 5006', '5006 cm'), ('e', r'44 \times 1000 = 44000', '44000 m'), ('f', r'3 \times 100 + 15 = 315', '315 cm'),
                ('g', r'56000 \div 1000 = 56', '56 km'), ('h', r'96314 = 96 \times 1000 + 314', '96 km 314 m'), ('i', r'99 = 90 + 9', '9 cm 9 mm')]:
    add(f'R10|2|{p}', [r], a)
for p, r, a in [('a', r'2 \times 60 + 25 = 145', '145 minutes'), ('b', r'255 \div 60 = 4 \text{ remainder } 15', '4 h 15 min'),
                ('c', r'880 \div 60 = 14 \text{ remainder } 40', '14 min 40 s'), ('d', r'360 \div 60 = 6 \text{ remainder } 0', '6 h 0 min')]:
    add(f'R10|3|{p}', [r], a)
add('R10|4|a', [r'849 \div 1000 = 0.849'], '0.849 km/h')
add('R10|4|b', [r'450 \times 100 \div 3600 = \frac{45000}{3600} = 12.5'], '12.5 cm/s')
add('R10|4|d', [r'124 \text{ cm/s} = 1.24 \text{ m/s}', r'1.24 \times 3600 = 4464'], '4464 m/h')
add('R10|5|', [r'1{:}22 \text{ p.m.} = 13{:}22', r'13{:}22 - 11{:}57 = 1 \text{ h } 25 \text{ min}'], '1 hour 25 minutes', kn('1 hour 19 minutes'))
add('R10|6|', [r'\text{Speed} = \frac{\text{Distance}}{\text{Time}} = \frac{560}{10} = 56'], '56 km/h', kn('560 km/h'))

for p, n in zip('abc', [5, 10, 7]):
    v = 180 * (n - 2) / n
    vs = f'{v:g}' if abs(v - round(v)) < 1e-9 else f'{v:.2f}'
    add(f'R11|11|{p}', [rf'\frac{{({n} - 2) \times 180}}{{{n}}} = \frac{{{(n - 2) * 180}}}{{{n}}} = {vs}'], f'{vs}°')
for p, n in zip('abcde', [5, 3, 7, 4, 8]):
    s = (n - 2) * 180
    add(f'R11|13|{p}', [rf'({n} - 2) \times 180 = {s}'], f'{s}°', kn('899.5°') if n == 7 else None)
add('R11|14|', [r'\frac{360}{4} = 90'], '90°')
add('R11|15|', [r'\frac{(5 - 2) \times 180}{5} = \frac{540}{5} = 108'], '108°', kn('72°'))
add('R11|16|', [r'\frac{360}{6} = 60'], '60°')
add('R11|17|', [r'\frac{(8 - 2) \times 180}{8} = \frac{1080}{8} = 135'], '135°', kn('45°'))

add('R12|18|a', [r'x = 180 - (20 + 110) = 50'], '50°')
add('R12|18|b', [r'b = 180 - 128 = 52', r'a = 180 - (60 + 52) = 68'], 'a = 68°, b = 52°')
add('R12|18|c', [T('Base angles of an isosceles triangle are equal: ') + r'a = \frac{180 - 86}{2} = 47'], '47°', kn('∠B = 80°, ∠C = 40°'))
add('R12|18|d', [T('Exterior angle = sum of the two opposite interior angles: ') + r'150 = 55 + \angle B', r'\angle B = 150 - 55 = 95', r'\angle ACB = 180 - 150 = 30'], '∠B = 95°, ∠ACB = 30°', kn('a = 47°, b = 47°'))
add('R12|18|e', [T('Base angles are equal, so ') + r'c = 60', r'b = 180 - (60 + 60) = 60'], 'b = 60°, c = 60°')

add('R13|11|b', [r'12 + 18 + 15 + 16 + 12 + 15 + 18 + 18 + 18 + 18 + 16 + 19 = 195', r'\text{Mean} = \frac{195}{12} = 16.25', r'\text{Sorted: } 12, 12, 15, 15, 16, 16, 18, 18, 18, 18, 18, 19 \;\Rightarrow\; \text{Median} = \frac{16 + 18}{2} = 17', r'18 \text{ occurs 5 times: Mode} = 18'], 'mean = 16.25, median = 17, mode = 18', kn('mean 177.58'))
OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L))
