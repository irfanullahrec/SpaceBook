"""Class 7 Maths phase 3: 7.4 Q9, 8.4 Q1 (solutions of linear equations in two variables),
9.5 Q1e, 9.6 Q1/Q2 (prisms), 9.7 Q4. Writes math/dsl/u789.txt."""
from fractions import Fraction
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'u789.txt'
L = []
def N(en, ur, ps): return f'{en}|{ur}|{ps}'
def key_note(k):
    return N(f'The printed key shows {k}, which does not match the given data.',
             f'چھپی کلید {k} دیتی ہے جو دیے گئے اعداد سے نہیں ملتا۔',
             f'چاپ شوې کلیل {k} ښيي چې له ورکړل شوو شمېرو سره نه جوړیږي.')

# 7.4 Q9
L.append(r'7.4|9| ~ (3x^2 - 5x^2y + 2y^2) - (2x^2y - 3y^2) = 3x^2 - 7x^2y + 5y^2 ;; (3xy^2 + 5y^2 - 2x^2y) + (x^2y + 5x^2 - 3xy^2) = 5x^2 - x^2y + 5y^2 ;; (5x^2 - x^2y + 5y^2) - (3x^2 - 7x^2y + 5y^2) = 2x^2 + 6x^2y => $2x^2 + 6x^2y$ !!')

# 8.4 Q1
eqs = {'a': (2, -1, 1, '2x - y = 1'), 'b': (1, 1, 3, 'x + y = 3'), 'c': (3, 2, -2, '3x + 2y = -2'), 'd': (2, -1, -1, '2x - y = -1'),
       'e': (2, 3, 10, '2x + 3y = 10'), 'f': (3, 4, 18, '3x + 4y = 18'), 'g': (2, 1, 6, '2x + y = 6'), 'h': (3, 1, 4, '3x + y = 4'),
       'i': (4, 1, 3, 'y = -4x + 3'), 'j': (1, -1, -2, 'y - 2 = x'), 'k': (2, -1, 8, '2x - y = 8'), 'l': (2, 1, 1, '-2x - y = 1 \text{ (as printed: } -2x - y = -1)')}
eqs['l'] = (2, 1, 1, '-2x - y = -1')
def fm(v): return str(v)
for p, (a, b, c, txt) in eqs.items():
    sols = []
    for x in sorted(range(-12, 25), key=lambda t: (abs(t), t)):
        y = Fraction(c - a * x, b)
        if y.denominator == 1:
            sols.append((x, int(y)))
        if len(sols) == 5: break
    sols.sort()
    sol_t = r',\; '.join(f'({x}, {y})' for x, y in sols)
    if abs(b) == 1:
        m, k = Fraction(-a, b), Fraction(c, b)
        mt = '' if m == 1 else ('-' if m == -1 else str(m))
        row1 = 'y = ' + (f'{mt}x' if m else '') + (f' + {k}' if k > 0 else (f' - {-k}' if k < 0 else ''))
    else:
        row1 = rf'y = \frac{{{c} - {a}x}}{{{b}}}'
    sub = r' \;\; '.join(rf'x = {x} \Rightarrow y = {y}' for x, y in sols)
    L.append(rf'8.4|1|{p} ~ {txt} ;; {row1} ;; {sub} => {sol_t} %%')

# 9.5 Q1e
L.append(r'9.5|1|e ~ V = \pi r^2 h ;; V = 3.14 \times 5^2 \times 14 = 3.14 \times 25 \times 14 = 1099 @@ ' + key_note('274.75 cm³') + ' => 1099 cm³ %%')
# 9.6 Q1 c,d
L.append(r'9.6|1|c ~ A = 6a^2 ;; A = 6 \times 4^2 = 6 \times 16 = 96 @@ ' + key_note('748 cm²') + ' => 96 cm² %%')
L.append(r'9.6|1|d ~ \text{Area of one triangle} = \frac{1}{2} \times 2 \times 1.5 = 1.5 ;; \text{Perimeter of triangle} = 2 + 1.5 + 2.5 = 6 ;; A = 2 \times 1.5 + 6 \times 10 = 3 + 60 = 63 @@ ' + key_note('68 m²') + ' => 63 m² %%')
# 9.6 Q2
L.append(r'9.6|2|b ~ V = l \times w \times h = 6 \times 4 \times 11 = 264 @@ ' + key_note('312 in³') + ' => 264 m³ %%')
L.append(r'9.6|2|c ~ V = \frac{1}{2} \times b \times h \times l ;; V = \frac{1}{2} \times 13 \times 10 \times 12 = 65 \times 12 = 780 @@ ' + key_note('858 in³') + ' => 780 cm³ %%')
L.append(r'9.6|2|d ~ V = \frac{1}{2} \times b \times h \times l ;; V = \frac{1}{2} \times 10 \times 13 \times 17 = 65 \times 17 = 1105 @@ ' + key_note('1248 in³') + ' => 1105 m³ %%')
L.append(r'9.6|2|e ~ V = \frac{1}{2} \times b \times h \times l ;; V = \frac{1}{2} \times 7 \times 6 \times 15 = 21 \times 15 = 315 @@ ' + key_note('364 in³') + ' => 315 cm³ %%')
# 9.7 Q4
L.append(r'9.7|4| ~ V = \text{area of triangular face} \times \text{length} ;; V = 20 \times 4.5 = 90 @@ ' + N('Volume only: the surface area and the cost need the side lengths of the face, which the question does not give. The printed key writes m² for the volume; it is m³.', 'صرف حجم: سطحی رقبہ اور لاگت کے لیے رخ کے اطراف درکار ہیں جو سوال میں نہیں دیے۔ چھپی کلید میں حجم m² لکھا ہے، صحیح m³ ہے۔', 'یوازې حجم: سطحي ساحه او لګښت د مخ اړخونه غواړي چې پوښتنه نه ورکوي. چاپ شوې کلیل حجم m² لیکلی، سم m³ دی.') + ' => 90 m³ %%')
OUT.write_text('\n'.join(L) + '\n', encoding='utf-8'); print(len(L))
