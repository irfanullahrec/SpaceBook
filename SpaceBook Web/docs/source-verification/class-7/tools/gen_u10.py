"""Class 7 Maths phase 4: 10.1 Q1g, 11.1 Q3-6 (quadrilateral angles), 11.3 Q3,5-10 (polygon angles),
12.5 Q1c, 13.6 Q1c. Writes math/dsl/u10_13.txt."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'u10_13.txt'
L = []
def N(en, ur, ps): return f'{en}|{ur}|{ps}'
def add(key, rows, ans, note=None):
    s = f'{key} ~ ' + ' ;; '.join(rows)
    if note: s += ' @@ ' + note
    L.append(s + f' => {ans} %%')
def keynote(k): return N(f'The printed key shows {k}, which does not match the data given in the question.',
                         f'چھپی کلید {k} دیتی ہے جو سوال کے اعداد سے نہیں ملتا۔',
                         f'چاپ شوې کلیل {k} ښیي چې د پوښتنې له شمېرو سره نه جوړیږي.')
T = lambda s: rf'\text{{{s}}}'

add('10.1|1|g', [r'1 \text{ cm} = 10 \text{ mm} ;; 50 \times 10 = 500'], '500 mm')

# 11.1 Q3 parallelograms: opposite angles equal, adjacent angles add to 180
add('11.1|3|a', [T('Opposite angles are equal: ') + r'a = 78'], '78°')
add('11.1|3|b', [T('Opposite angles are equal: ') + r'b = 110'], '110°', keynote('70°'))
add('11.1|3|c', [T('Opposite angles are equal: ') + r'c = 85', T('Adjacent angles add up to 180: ') + r'd = 180 - 85 = 95'], 'c = 85°, d = 95°')
add('11.1|3|d', [T('Opposite angle = 125; adjacent angles: ') + r'180 - 125 = 55'], 'The other angles are 55°, 125° and 55°')
# Q4 rhombus
add('11.1|4|a', [T('Opposite angles of a rhombus are equal: ') + r'a = 65'], '65°')
add('11.1|4|b', [T('Adjacent angles add up to 180: ') + r'b = 180 - 118 = 62'], '62°')
add('11.1|4|c', [T('Adjacent angles add up to 180: ') + r'c = 180 - 60 = 120', T('Opposite angles are equal: ') + r'd = 60'], 'c = 120°, d = 60°')
add('11.1|4|d', [T('Adjacent angles add up to 180: ') + r'e = 180 - 15 = 165', T('Opposite angles are equal: ') + r'f = 15,\; g = 165'], 'e = 165°, f = 15°, g = 165°')
# Q5 trapeziums
add('11.1|5|a', [T('Angles between the parallel sides on one leg add up to 180: ') + r'a = 180 - 90 = 90'], '90°')
add('11.1|5|b', [T('Co-interior angles between parallel lines add up to 180: ') + r'b = 180 - 22 = 158'], '158°')
add('11.1|5|c', [r'c = 180 - 105 = 75', r'd = 180 - 18 = 162'], 'c = 75°, d = 162°')
# Q6 kites
add('11.1|6|a', [T('In kite UXWV, ') + r'\angle X = \angle V = 135', r'\angle U = 360 - 135 - 135 - 53 = 37'], '∠X = 135°, ∠U = 37°')
add('11.1|6|b', [T('In kite BEDC, ') + r'\angle E = \angle C', r'\angle E = \frac{360 - 104 - 40}{2} = \frac{216}{2} = 108'], '∠E = ∠C = 108°')
add('11.1|6|c', [T('In kite PQRS, ') + r'\angle S = \angle Q = 122', r'\angle R = 360 - 50 - 122 - 122 = 66'], '∠S = 122°, ∠R = 66°')

# 11.3
for p, n in zip('abcdef', [5, 6, 8, 10, 13, 20]):
    v = 180 * (n - 2) / n
    vs = f'{v:g}' if abs(v - round(v)) < 1e-9 else f'{v:.2f}'
    add(f'11.3|3|{p}', [rf'\text{{Interior angle}} = \frac{{(n - 2) \times 180}}{{n}}', rf'\frac{{({n} - 2) \times 180}}{{{n}}} = \frac{{{(n - 2) * 180}}}{{{n}}} = {vs}'], f'{vs}°')
for q, n, kind in [(5, 8, 'e'), (6, 6, 'i'), (7, 9, 'e'), (8, 11, 'i')]:
    if kind == 'e':
        add(f'11.3|{q}|', [r'\text{Exterior angle} = \frac{360}{n}', rf'\frac{{360}}{{{n}}} = {360 // n}'], f'{360 // n}°')
    else:
        v = 180 * (n - 2) / n
        vs = f'{v:g}' if abs(v - round(v)) < 1e-9 else f'{v:.2f}'
        add(f'11.3|{q}|', [r'\text{Interior angle} = \frac{(n - 2) \times 180}{n}', rf'\frac{{({n} - 2) \times 180}}{{{n}}} = \frac{{{(n - 2) * 180}}}{{{n}}} = {vs}'], f'{vs}°')
add('11.3|9|', [r'\text{Sum of the angles of a pentagon} = (5 - 2) \times 180 = 540', r'115 + 92 + 107 + 83 = 397', r'540 - 397 = 143'], '143°')
add('11.3|10|a', [r'\text{Heptagon: } (7 - 2) \times 180 = 900', r'129 + 116 + 120 + 125 + 135 + 130 = 755', r'y = 900 - 755 = 145'], '145°')
add('11.3|10|b', [r'\text{Pentagon: } 540', r'117 + 100 + 115 + 105 = 437', r'x = 540 - 437 = 103'], '103°')
add('11.3|10|c', [r'\text{Hexagon: } (6 - 2) \times 180 = 720', r'135 + 62 + 151 + 140 + n + (n + 6) = 720', r'488 + 2n + 6 = 720 \Rightarrow 2n = 226 \Rightarrow n = 113'], 'n = 113° (so F = 119°)', keynote('134°'))
add('11.3|10|d', [r'\text{Pentagon: } 540', r'115 + 115 + 90 + 90 = 410', r'\angle A = 540 - 410 = 130'], '130°', keynote('90°, 90°'))
add('11.3|10|e', [r'\text{Hexagon: } 720', r'120 + 90 + 110 + 130 + 160 = 610', r'x = 720 - 610 = 110'], '110°')
# 12.5
add('12.5|1|c', [T('Exterior angle = sum of the two opposite interior angles: ') + r'120 = 60 + y', r'y = 120 - 60 = 60', r'x = 180 - 120 = 60'], 'x = 60°, y = 60°')
# 13.6
add('13.6|1|c', [r'\text{Mean} = \frac{114 + 154 + 240 + 112}{4}', r'\frac{620}{4} = 155'], '155', keynote('536'))
OUT.write_text('\n'.join(L) + '\n', encoding='utf-8'); print(len(L))
