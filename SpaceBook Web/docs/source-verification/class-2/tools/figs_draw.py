"""Class 2 Drawing book: hand-coded SVG pictures for the 'join the dots and colour' and 'look and draw' pages.

Each picture is a list of parts in a 200 x 160 box. A part is (element, fill):
  element  an SVG element without fill/stroke, e.g. '<circle cx="100" cy="80" r="20"/>'
  fill     a colour; 'line:#hex' draws a stroke-only part (legs, rays, water lines, fold lines).
render(parts, mode) draws the coloured model ('model'), the dotted outline to trace ('dots') or a plain
pencil outline ('outline').
"""
import math

INK = '#1f2937'


def C(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'


def E(cx, cy, rx, ry, rot=0):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ''
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"{t}/>'


def R(x, y, w, h, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'


def P(d):
    return f'<path d="{d}"/>'


def G(pts):
    return '<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'


def L(*pts):
    return '<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'


def T(x, y, s, size=12):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" font-family="Arial, sans-serif">{s}</text>'


def ln(c='#1f2937'):
    return 'line:' + c


def _rhombus(cx, cy, a, L_=40):
    u = lambda ang, k: (cx + k * math.cos(math.radians(ang)), cy + k * math.sin(math.radians(ang)))
    return G([(cx, cy), u(a - 30, L_), u(a, L_ * math.sqrt(3)), u(a + 30, L_)])


def _petals(cx, cy, n, dist, rx, ry, fill):
    return [(E(cx + dist * math.cos(2 * math.pi * i / n), cy + dist * math.sin(2 * math.pi * i / n), rx, ry,
               math.degrees(2 * math.pi * i / n)), fill) for i in range(n)]


def _rays(cx, cy, r1, r2, n=10):
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n
        out.append((L((cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + r2 * math.cos(a), cy + r2 * math.sin(a))), ln('#f59e0b')))
    return out


def _star5(cx, cy, R1, R2, rot=-90):
    pts = []
    for i in range(10):
        a = math.radians(rot + 36 * i)
        r = R1 if i % 2 == 0 else R2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


# ---------------------------------------------------------------- pictures
def star6():
    cols = ['#dc2626', '#16a34a', '#7c3aed', '#f97316', '#9d174d', '#92400e']
    return [(_rhombus(100, 80, -90 + 60 * i, 38), cols[i]) for i in range(6)]


def tomato_chilli():
    return [(P('M40 40 Q30 30 38 22 Q44 30 46 40 Q62 90 92 130 Q96 138 86 134 Q48 104 40 40 Z'), '#16a34a'),
            (E(135, 90, 50, 40), '#dc2626'),
            (G([(135, 52), (122, 40), (131, 54), (110, 52), (128, 60), (135, 74), (142, 60), (160, 52), (139, 54), (148, 40)]), '#15803d')]


def sunflower():
    return ([(R(97, 80, 6, 75), '#16a34a'),
             (E(78, 118, 20, 9, -30), '#22c55e'), (E(122, 128, 20, 9, 30), '#22c55e')]
            + _petals(100, 52, 14, 24, 13, 6, '#facc15') + [(C(100, 52, 15), '#78350f')])


def spider():
    legs = []
    for side in (-1, 1):
        for k, (dx, dy, ex, ey) in enumerate([(30, -30, 55, -10), (38, -10, 70, 20), (36, 10, 66, 55), (28, 24, 48, 75)]):
            legs.append((L((100, 82), (100 + side * dx, 82 + dy), (100 + side * ex, 82 + ey)), ln('#78350f')))
    return legs + [(E(100, 98, 20, 26), '#92400e'), (C(100, 66, 13), '#7c2d12'), (C(95, 63, 2.5), '#fff'), (C(105, 63, 2.5), '#fff')]


def bucket():
    return [(P('M50 50 Q90 0 130 50'), ln('#475569')),
            (G([(45, 50), (135, 50), (122, 140), (58, 140)]), '#22c55e'),
            (E(90, 50, 45, 9), '#86efac'),
            (L((70, 95), (110, 95)), ln('#15803d')),
            (R(138, 70, 6, 50), '#a16207'), (G([(130, 118), (152, 118), (148, 150), (134, 150)]), '#94a3b8')]


def lamp():
    return [(G([(70, 20), (130, 20), (160, 75), (40, 75)]), '#f472b6'),
            (E(100, 20, 30, 5), '#fbcfe8'),
            (E(100, 105, 30, 28), '#fb923c'),
            (C(100, 105, 6), '#dc2626')] + _petals(100, 105, 6, 9, 5, 3, '#ef4444') + [
            (R(88, 131, 24, 8, 2), '#a855f7'), (E(100, 145, 36, 8), '#7c3aed')]


def tree():
    return [(P('M90 155 L94 105 L80 88 L92 92 L96 80 L104 80 L108 92 L120 86 L106 105 L110 155 Z'), '#b45309'),
            (P('M70 88 Q48 88 50 68 Q40 50 60 42 Q62 18 86 22 Q100 6 116 22 Q140 18 140 42 Q160 50 150 68 Q152 88 130 88 Z'), '#16a34a')]


def scenery_sea():
    out = [(C(30, 25, 12), '#facc15')] + _rays(30, 25, 15, 22)
    out += [(R(0, 100, 200, 60), '#7dd3fc')]
    for y in (110, 125, 140):
        out.append((P(f'M5 {y} q15 -8 30 0 t30 0 t30 0 t30 0'), ln('#0369a1')))
    out += [(E(160, 145, 40, 14), '#a16207'),
            (P('M158 140 Q156 100 164 70 L168 70 Q162 100 164 140 Z'), '#92400e'),
            (P('M166 70 Q140 55 125 72 Q146 62 166 72 Z'), '#16a34a'), (P('M166 70 Q190 52 198 74 Q182 62 166 72 Z'), '#16a34a'),
            (P('M166 70 Q160 45 140 42 Q158 52 164 70 Z'), '#22c55e'), (P('M166 70 Q176 44 194 46 Q178 54 168 70 Z'), '#22c55e')]
    return out


def bed():
    return [(R(25, 30, 6, 100), '#7c2d12'), (R(169, 30, 6, 100), '#7c2d12'), (P('M25 40 Q100 15 175 40'), ln('#7c2d12')),
            (R(25, 70, 150, 50, 4), '#38bdf8'), (R(55, 58, 34, 14, 4), '#f472b6'), (R(111, 58, 34, 14, 4), '#f472b6')] + [
            (L((x, 82), (x, 115)), ln('#0369a1')) for x in range(40, 170, 15)] + [
            (R(32, 120, 8, 14), '#7c2d12'), (R(160, 120, 8, 14), '#7c2d12')]


def bear():
    return [(P('M40 70 Q60 40 110 45 Q160 45 172 80 Q178 110 160 118 L160 145 L145 145 L142 120 L80 122 L78 145 L62 145 L60 118 Q42 108 40 70 Z'), '#a16207'),
            (C(42, 62, 20), '#a16207'), (C(30, 44, 7), '#92400e'), (C(52, 42, 7), '#92400e'),
            (C(36, 60, 2.5), INK), (C(48, 60, 2.5), INK), (E(30, 70, 5, 4), INK)]


def cake():
    out = [(R(40, 95, 120, 45, 8), '#facc15'), (R(55, 60, 90, 38, 8), '#fde047'),
           (P('M55 66 q11 10 22 0 q11 10 22 0 q11 10 23 0 q11 10 23 0'), ln('#dc2626')),
           (P('M40 102 q15 12 30 0 q15 12 30 0 q15 12 30 0 q15 12 30 0'), ln('#dc2626'))]
    for i, (x, col) in enumerate([(75, '#22c55e'), (100, '#f97316'), (125, '#3b82f6')]):
        out += [(R(x - 4, 30, 8, 30, 2), col), (P(f'M{x} 14 Q{x + 7} 24 {x} 30 Q{x - 7} 24 {x} 14 Z'), '#f59e0b')]
    return out


def shower():
    out = [(P('M40 60 Q100 0 160 60 Z'), '#7c3aed'), (L((45, 45), (30, 25)), ln('#ca8a04')), (L((155, 45), (170, 25)), ln('#ca8a04')),
           (R(30, 60, 140, 8, 3), '#facc15'), (R(40, 68, 8, 70), '#64748b'), (R(40, 132, 60, 8), '#64748b'),
           (P('M95 128 L135 128 Q135 152 115 152 Q95 152 95 128 Z'), '#0ea5e9')]
    for x in range(80, 125, 9):
        out.append((L((x, 74), (x, 118)), ln('#38bdf8')))
    return out


def fridge():
    return [(R(60, 10, 80, 140, 6), '#22c55e'), (L((60, 70), (140, 70)), ln('#14532d')),
            (R(66, 25, 5, 30, 2), '#7f1d1d'), (R(66, 82, 5, 40, 2), '#7f1d1d'),
            (C(90, 32, 8), '#fff'), (C(112, 32, 8), '#fff'), (C(91, 33, 3), INK), (C(113, 33, 3), INK),
            (P('M88 48 Q101 60 114 48'), ln(INK))]


def bird():
    return [(P('M60 78 Q20 50 18 90 Q40 80 62 96 Z'), '#92400e'), (P('M140 78 Q180 50 182 90 Q160 80 138 96 Z'), '#92400e'),
            (E(100, 98, 36, 34), '#fb923c'), (C(100, 52, 26), '#16a34a'), (E(100, 66, 18, 10), '#93c5fd'),
            (C(91, 48, 6), '#fff'), (C(109, 48, 6), '#fff'), (C(92, 49, 2.5), INK), (C(110, 49, 2.5), INK),
            (G([(94, 60), (106, 60), (100, 70)]), '#f59e0b'),
            (L((88, 130), (84, 145)), ln('#78350f')), (L((112, 130), (116, 145)), ln('#78350f'))]


def slide():
    out = [(R(40, 30, 6, 120), '#dc2626'), (R(70, 30, 6, 120), '#dc2626')]
    for y in range(45, 150, 18):
        out.append((R(46, y, 24, 5), '#b91c1c'))
    out += [(G([(76, 40), (90, 40), (175, 140), (160, 150)]), '#facc15'), (G([(76, 40), (82, 40), (165, 145), (160, 150)]), '#f97316')]
    return out


def trophy():
    return [(P('M60 20 L140 20 Q140 85 100 95 Q60 85 60 20 Z'), '#f59e0b'),
            (P('M60 30 Q35 30 40 50 Q45 65 66 66'), ln('#b45309')), (P('M140 30 Q165 30 160 50 Q155 65 134 66'), ln('#b45309')),
            (C(100, 50, 15), '#fff'), (T(100, 55, '1st', 13), INK),
            (R(94, 95, 12, 18), '#d97706'), (R(70, 112, 60, 12, 2), '#d97706'), (R(55, 124, 90, 28, 3), '#57534e'),
            (R(70, 130, 60, 14, 2), '#fff'), (T(100, 141, 'Name', 9), INK)]


def horse():
    return [(P('M20 130 Q100 165 180 130'), ln('#7c3aed')),
            (L((55, 100), (45, 136)), ln('#ec4899')), (L((75, 102), (70, 140)), ln('#ec4899')),
            (L((125, 102), (130, 140)), ln('#ec4899')), (L((145, 100), (155, 136)), ln('#ec4899')),
            (E(100, 88, 55, 20), '#f472b6'), (G([(80, 72), (120, 72), (112, 100), (88, 100)]), '#22c55e'),
            (P('M140 80 L150 30 L170 22 L188 42 L178 50 L162 46 L156 84 Z'), '#f472b6'),
            (P('M150 30 Q138 50 142 70'), ln('#3b82f6')), (C(170, 34, 3), INK),
            (P('M45 80 Q20 85 25 115'), ln('#0ea5e9'))]


def burger():
    return [(P('M30 75 Q30 20 100 20 Q170 20 170 75 Z'), '#f97316'),
            (P('M25 75 q12 12 25 0 q12 12 25 0 q12 12 25 0 q12 12 25 0 q12 12 25 0 q12 12 25 0 L175 90 L25 90 Z'), '#22c55e'),
            (R(28, 88, 144, 12, 4), '#f472b6'), (R(32, 100, 136, 16, 6), '#7c2d12'),
            (G([(30, 116), (170, 116), (160, 126), (40, 126)]), '#facc15'),
            (P('M30 126 L170 126 Q170 150 100 150 Q30 150 30 126 Z'), '#fb923c')]


def potato_onion():
    return [(P('M20 80 Q20 40 70 45 Q120 40 118 90 Q120 135 65 130 Q18 128 20 80 Z'), '#a16207'),
            (E(45, 70, 5, 3), '#fde68a'), (E(85, 62, 5, 3), '#fde68a'), (E(70, 105, 5, 3), '#fde68a'), (E(100, 95, 5, 3), '#fde68a'),
            (P('M150 60 Q185 90 168 130 Q155 145 142 130 Q125 90 150 60 Z'), '#7e22ce'),
            (P('M150 60 L140 10 L152 55 L158 8 L155 60 Z'), '#22c55e'),
            (L((150, 140), (146, 152)), ln('#a16207')), (L((154, 140), (158, 152)), ln('#a16207'))]


def maize():
    rot = ' transform="rotate(25 100 70)"'
    out = [(E(100, 70, 26, 60, 25), '#facc15')]
    for k in (-14, -5, 5, 14):
        out.append((f'<line x1="{100 + k}" y1="{18 + abs(k)}" x2="{100 + k}" y2="{122 - abs(k)}"{rot}/>', ln('#ca8a04')))
    for y in range(28, 120, 12):
        hw = 26 * (1 - ((y - 70) / 60) ** 2) ** 0.5
        out.append((f'<line x1="{100 - hw:.1f}" y1="{y}" x2="{100 + hw:.1f}" y2="{y}"{rot}/>', ln('#ca8a04')))
    out += [(P('M60 150 Q60 90 92 60 Q78 110 96 140 Z'), '#16a34a'), (P('M140 150 Q150 95 122 70 Q130 112 108 140 Z'), '#22c55e')]
    return out


def scenery_house():
    out = [(C(25, 25, 11), '#facc15')] + _rays(25, 25, 14, 21)
    out += [(P('M70 25 q6 -12 18 -6 q10 -8 18 2 q10 2 4 12 h-40 q-8 -4 0 -8 Z'), '#93c5fd'),
            (P('M140 25 q6 -12 18 -6 q10 -8 18 2 q10 2 4 12 h-40 q-8 -4 0 -8 Z'), '#93c5fd'),
            (R(0, 135, 200, 25), '#86efac'),
            (G([(50, 80), (100, 45), (150, 80)]), '#7c3aed'), (R(58, 80, 84, 60), '#fde68a'),
            (R(92, 108, 16, 32), '#f9a8d4'), (R(66, 90, 16, 14), '#7dd3fc'), (R(118, 90, 16, 14), '#7dd3fc')]
    return out


def ship():
    out = [(P('M15 95 L185 95 L165 140 L40 140 Z'), '#dc2626'), (R(15, 110, 170, 8), '#7c3aed'),
           (R(55, 60, 95, 35, 4), '#f8fafc'), (R(75, 40, 40, 20, 3), '#fde68a'), (R(120, 25, 16, 35), '#dc2626'),
           (P('M128 25 q-6 -12 6 -14 q4 -10 16 -6 q14 0 10 10 q-10 6 -22 2 Z'), '#cbd5e1')]
    for x in (70, 88, 106, 124, 142):
        out.append((C(x, 78, 6), '#38bdf8'))
    return out


def chick_parts():
    return [(C(100, 70, 40), '#f9a8d4'),
            (P('M132 70 Q165 60 160 95 Q148 85 134 95 Z'), '#fb923c'),
            (L((90, 110), (88, 140), (80, 145)), ln('#475569')), (L((110, 110), (112, 140), (120, 145)), ln('#475569')),
            (C(86, 62, 4), '#38bdf8'), (C(114, 62, 4), '#38bdf8'), (G([(94, 72), (106, 72), (100, 84)]), '#7c3aed')]


def turtle_parts():
    out = [(P('M40 110 Q40 40 100 40 Q160 40 160 110 Z'), '#16a34a'),
           (P('M158 98 Q170 70 190 80 Q198 100 178 108 Q166 110 158 106 Z'), '#4ade80'),
           (R(52, 108, 18, 30, 4), '#4ade80'), (R(82, 108, 18, 30, 4), '#4ade80'), (R(112, 108, 18, 30, 4), '#4ade80'),
           (R(136, 108, 18, 26, 4), '#4ade80')]
    pat = [(L((70, 50), (70, 110)), ln('#14532d')), (L((100, 40), (100, 110)), ln('#14532d')), (L((130, 50), (130, 110)), ln('#14532d')),
           (L((46, 80), (154, 80)), ln('#14532d')), (C(182, 88, 4), '#38bdf8')]
    return out + pat


def car():
    return [(P('M15 110 L15 85 Q20 70 45 68 L65 40 L140 40 L160 68 Q185 70 188 90 L188 110 Z'), '#facc15'),
            (G([(72, 46), (100, 46), (100, 66), (60, 66)]), '#7dd3fc'), (G([(106, 46), (134, 46), (150, 66), (106, 66)]), '#7dd3fc'),
            (C(55, 112, 16), INK), (C(55, 112, 7), '#dc2626'), (C(150, 112, 16), INK), (C(150, 112, 7), '#dc2626'),
            (E(22, 90, 5, 4), '#f97316')]


def fan_parts():
    return [(C(100, 60, 45), '#fef9c3'),
            (R(92, 105, 16, 38), '#38bdf8'), (R(60, 143, 80, 10, 2), '#f472b6'),
            (C(100, 60, 9), '#16a34a'),
            (P('M100 60 Q80 20 110 22 Q125 40 100 60 Z'), '#ef4444'),
            (P('M100 60 Q140 60 135 85 Q110 92 100 60 Z'), '#ef4444'),
            (P('M100 60 Q75 95 62 72 Q68 52 100 60 Z'), '#ef4444')]


def ball_parts():
    return [(C(100, 80, 60), '#fde047'),
            (P('M42 92 Q100 72 158 96'), ln(INK)),
            (P('M80 23 Q60 70 82 138'), ln(INK)),
            (P('M128 28 Q150 60 152 112'), ln(INK))]


def starfish():
    pts = _star5(100, 82, 75, 30, -100)
    d = 'M' + ' '.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
    out = [(P(d), '#ef4444')]
    for x, y in [(100, 30), (100, 45), (150, 62), (138, 68), (130, 120), (122, 108), (68, 122), (78, 110), (45, 64), (60, 68)]:
        out.append((C(x, y, 3.5), '#fde047'))
    out += [(C(90, 78, 7), '#fff'), (C(110, 78, 7), '#fff'), (C(91, 79, 3), INK), (C(111, 79, 3), INK), (P('M90 94 Q100 102 110 94'), ln(INK))]
    return out


def tri_tree_parts():
    cols = ['#9d174d', '#93c5fd', '#a16207', '#22c55e', '#dc2626']
    out = []
    for i, c in enumerate(cols[:4]):
        y = 20 + i * 26
        half = 22 + i * 14
        out.append((G([(100, y), (100 - half, y + 40), (100 + half, y + 40)]), c))
    out.append((R(92, 140, 16, 18), '#7c2d12'))
    return out


# origami: each step is its own small picture (non-cumulative)
def _sq(fill='#fff'):
    return (G([(100, 15), (165, 80), (100, 145), (35, 80)]), fill)


def bird_fold_steps():
    blue = '#7dd3fc'
    s1 = [_sq(), (L((35, 80), (165, 80)), ln('#475569')), (P('M60 70 Q100 50 140 70'), ln('#2563eb'))]
    s2 = [_sq(), (L((100, 15), (100, 145)), ln('#94a3b8')), (L((100, 15), (65, 80)), ln('#94a3b8')), (L((100, 15), (135, 80)), ln('#94a3b8'))]
    kite = (G([(100, 15), (130, 95), (100, 145), (70, 95)]), blue)
    s3 = [kite, (L((70, 95), (130, 95)), ln('#475569'))]
    s4 = [(G([(100, 15), (130, 95), (70, 95)]), blue), (G([(70, 95), (130, 95), (100, 145)]), '#fff')]
    s5 = [(G([(100, 15), (115, 140), (85, 140)]), blue), (L((100, 15), (100, 140)), ln('#475569'))]
    s6 = [(G([(80, 30), (150, 140), (100, 130)]), blue), (P('M80 30 Q70 60 90 80'), ln('#475569'))]
    s7 = [(G([(40, 80), (160, 95), (60, 110)]), blue), (G([(40, 80), (55, 60), (60, 82)]), '#fff'), (C(62, 85, 4), INK)]
    s8 = [(G([(30, 80), (170, 100), (60, 112)]), blue), (G([(30, 80), (40, 70), (55, 82)]), '#38bdf8'), (C(52, 88, 4), INK),
          (G([(90, 100), (150, 105), (100, 125)]), '#38bdf8')]
    return [s1, s2, s3, s4, s5, s6, s7, s8]


def owl_fold_steps():
    br = '#c2410c'
    s1 = [_sq(), (L((35, 80), (165, 80)), ln('#475569')), (P('M70 65 Q100 50 130 65'), ln('#2563eb'))]
    s2 = [_sq(), (L((35, 80), (165, 80)), ln('#475569')), (L((100, 15), (100, 145)), ln('#94a3b8')), (P('M100 30 q10 10 0 20 q10 10 0 20'), ln('#dc2626'))]
    s3 = [_sq(), (G([(80, 35), (120, 35), (100, 55)]), br)]
    s4 = [(G([(35, 60), (165, 60), (165, 100), (35, 100)]), '#fff'), (G([(70, 60), (130, 60), (100, 85)]), br),
          (G([(35, 100), (100, 75), (165, 100)]), br)]
    s5 = [(R(45, 30, 110, 110), br), (G([(45, 30), (155, 30), (100, 80)]), '#fff'), (G([(70, 30), (130, 30), (100, 55)]), br)]
    s6 = s5[:] + [(C(78, 55, 11), '#fff'), (C(122, 55, 11), '#fff'), (C(78, 55, 5), INK), (C(122, 55, 5), INK),
                  (P('M60 100 q10 8 20 0 M85 110 q10 8 20 0 M110 100 q10 8 20 0'), ln('#7c2d12'))]
    return [s1, s2, s3, s4, s5, s6]


PICTURES = {
    'star6': star6, 'tomato': tomato_chilli, 'sunflower': sunflower, 'spider': spider, 'bucket': bucket, 'lamp': lamp,
    'tree': tree, 'seascene': scenery_sea, 'bed': bed, 'bear': bear, 'cake': cake, 'shower': shower, 'fridge': fridge,
    'bird': bird, 'slide': slide, 'trophy': trophy, 'horse': horse, 'burger': burger, 'potato': potato_onion,
    'maize': maize, 'housescene': scenery_house, 'ship': ship, 'chick': chick_parts, 'turtle': turtle_parts, 'car': car,
    'fan': fan_parts, 'ball': ball_parts, 'starfish': starfish, 'tritree': tri_tree_parts,
}
# cumulative 'look and draw' steps: number of parts shown in each step
STEPS = {'chick': [1, 2, 4, 7], 'turtle': [1, 2, 6, 11], 'fan': [1, 3, 4, 7], 'ball': [1, 2, 3, 4], 'tritree': [1, 2, 3, 5]}
FOLDS = {'birdfold': bird_fold_steps, 'owlfold': owl_fold_steps}


def render(parts, mode, x=0, y=0, scale=1.0):
    out = []
    for el, fill in parts:
        line = fill.startswith('line:')
        col = fill[5:] if line else fill
        if mode == 'model':
            st = (f'fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"' if line
                  else f'fill="{col}" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"')
        elif mode == 'dots':
            st = 'fill="none" stroke="#475569" stroke-width="1.8" stroke-dasharray="1 5" stroke-linecap="round"'
        else:
            st = f'fill="{"none" if line else "#fff"}" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"'
        if el.startswith('<text'):
            out.append(el.replace('<text', f'<text fill="{INK if mode != "dots" else "#94a3b8"}"', 1))
        else:
            out.append(el.replace('/>', f' {st}/>', 1) if el.endswith('/>') else el)
    return f'<g transform="translate({x} {y}) scale({scale})">' + ''.join(out) + '</g>'
