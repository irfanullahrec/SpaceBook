"""Coded labelled figure panels for Class 5 General Science pages.

    python sci5_figs.py NAME            -> prints one SVG (see FIGS)
Panels are simple schematic drawings (not copies of the printed art) keeping the printed labels and grouping.
"""
import sys

W = 220  # panel width


def panel_row(items, title=None, h=200):
    """items: list of (label, inner_svg_drawn_in_0..W x 0..h-40). Returns a row of panels with green labels."""
    n = len(items)
    total_h = h + (34 if title else 0)
    out = [f'<svg viewBox="0 0 {n * W + 10} {total_h + 10}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14">']
    for i, (label, inner) in enumerate(items):
        x = 5 + i * W
        out.append(f'<rect x="{x}" y="5" width="{W - 4}" height="{h - 4}" fill="#fff" stroke="#334155"/>')
        out.append(f'<g transform="translate({x},5)">{inner}</g>')
        out.append(f'<rect x="{x}" y="{h - 33}" width="{W - 4}" height="28" fill="#86efac" stroke="#334155"/>')
        fit = f' textLength="{W - 14}" lengthAdjust="spacingAndGlyphs"' if len(label) > 27 else ''
        out.append(f'<text x="{x + (W - 4) / 2}" y="{h - 14}" text-anchor="middle" font-weight="bold"{fit}>{label}</text>')
    if title:
        out.append(f'<rect x="5" y="{h + 1}" width="{n * W - 4}" height="30" fill="#fdba74" stroke="#334155"/>')
        out.append(f'<text x="{5 + (n * W - 4) / 2}" y="{h + 21}" text-anchor="middle" font-weight="bold">{title}</text>')
    out.append('</svg>')
    return '\n'.join(out)


BACTERIUM = '<rect x="35" y="45" width="140" height="70" rx="35" fill="#c084fc" stroke="#6b21a8" stroke-width="4"/><rect x="45" y="55" width="120" height="50" rx="25" fill="#e9d5ff"/><path d="M70 80 q10 -15 20 0 t20 0 t20 0 t20 0" stroke="#4c1d95" stroke-width="5" fill="none"/><path d="M175 80 q25 10 15 40 t10 30" stroke="#111827" stroke-width="2" fill="none"/>'
AMOEBA = '<path d="M40 70 q20 -40 50 -20 q30 -30 50 0 q30 10 20 40 q20 30 -10 40 q-10 40 -40 20 q-30 20 -40 -10 q-40 0 -30 -30 q-20 -20 0 -40z" fill="#f9a8d4" stroke="#9d174d" stroke-width="2"/><circle cx="110" cy="100" r="12" fill="#fbcfe8" stroke="#9d174d"/><circle cx="80" cy="80" r="5" fill="#be185d"/><circle cx="140" cy="125" r="4" fill="#be185d"/>'
PARAMECIUM = '<ellipse cx="110" cy="90" rx="80" ry="38" transform="rotate(-25 110 90)" fill="#ecfccb" stroke="#365314" stroke-width="2"/><g stroke="#365314">' + ''.join(f'<line x1="{45 + i * 10}" y1="{125 - i * 4.5}" x2="{42 + i * 10}" y2="{133 - i * 4.5}"/>' for i in range(15)) + '</g><circle cx="90" cy="95" r="10" fill="#a3a3a3"/><circle cx="130" cy="75" r="6" fill="#65a30d"/><path d="M100 110 q20 5 25 -10" stroke="#57534e" stroke-width="5" fill="none"/>'
SPIROGYRA = ''.join(f'<path d="M{20 + i * 22} 160 C{40 + i * 22} 110 {10 + i * 22} 70 {40 + i * 22} 10" stroke="#4d7c0f" stroke-width="5" fill="none"/>' for i in range(8)) + '<rect x="170" y="10" width="34" height="150" rx="10" fill="#bbf7d0" stroke="#166534"/>' + ''.join(f'<path d="M172 {20 + k * 28} q15 14 30 0" stroke="#15803d" stroke-width="3" fill="none"/>' for k in range(5))

MUSHROOM = ''.join(f'<rect x="{x - 5}" y="{y}" width="10" height="{150 - y}" fill="#f5f5f4" stroke="#78716c"/><ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * 0.45}" fill="#a8a29e" stroke="#57534e"/>' for x, y, r in [(60, 70, 40), (120, 50, 45), (170, 85, 32), (95, 100, 28)])
RHIZOPUS = '<path d="M10 150 H210" stroke="#78716c" stroke-width="2"/>' + ''.join(f'<path d="M{x} 150 C{x - 5} 110 {x + 8} 80 {x} {y}" stroke="#57534e" stroke-width="2" fill="none"/><circle cx="{x}" cy="{y}" r="11" fill="#57534e"/><path d="M{x} 150 l-10 12 M{x} 150 l8 12 M{x} 150 l-2 14" stroke="#57534e"/>' for x, y in [(50, 45), (100, 30), (150, 50), (185, 40)])
BRACKET = ''.join(f'<path d="M{40 + i * 8} {40 + i * 25} q70 -35 150 0 q-75 22 -150 0z" fill="#fdba74" stroke="#c2410c"/>' for i in range(5)) + '<rect x="25" y="20" width="18" height="140" fill="#78350f"/>'
YEAST = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#bef264" stroke="#3f6212"/>' for x, y, r in [(60, 60, 18), (90, 50, 14), (80, 85, 16), (115, 75, 18), (140, 55, 13), (150, 95, 17), (110, 110, 15), (70, 120, 14), (130, 130, 12), (170, 70, 11)])
FLOWERING = '<path d="M110 160 V70" stroke="#15803d" stroke-width="5"/>' + ''.join(f'<ellipse cx="{110 + 30 * __import__("math").cos(a)}" cy="{60 + 30 * __import__("math").sin(a)}" rx="24" ry="14" transform="rotate({a * 57.3} {110 + 30 * __import__("math").cos(a)} {60 + 30 * __import__("math").sin(a)})" fill="#f87171" stroke="#b91c1c"/>' for a in [0, 1.26, 2.51, 3.77, 5.03]) + '<circle cx="110" cy="60" r="10" fill="#fde047"/><path d="M110 120 q-35 -10 -45 10 q30 5 45 -10z M110 135 q35 -10 45 10 q-30 5 -45 -10z" fill="#22c55e"/>'
PINE = '<rect x="102" y="120" width="16" height="45" fill="#78350f"/>' + ''.join(f'<polygon points="110,{20 + i * 25} {60 - i * 6},{75 + i * 25} {160 + i * 6},{75 + i * 25}" fill="#166534"/>' for i in range(4))
FERN = ''.join(f'<g transform="rotate({ang} 110 165)"><path d="M110 165 V30" stroke="#4d7c0f" stroke-width="3"/>' + ''.join(f'<path d="M110 {40 + k * 12} l{-30 + k} -6 M110 {40 + k * 12} l{30 - k} -6" stroke="#65a30d" stroke-width="4"/>' for k in range(10)) + '</g>' for ang in (-25, 0, 25))

RABBIT = '<ellipse cx="120" cy="110" rx="60" ry="38" fill="#a8a29e" stroke="#57534e"/><circle cx="70" cy="80" r="26" fill="#a8a29e" stroke="#57534e"/><ellipse cx="62" cy="35" rx="9" ry="30" fill="#d6d3d1" stroke="#57534e" transform="rotate(-15 62 35)"/><ellipse cx="82" cy="35" rx="9" ry="30" fill="#d6d3d1" stroke="#57534e" transform="rotate(10 82 35)"/><circle cx="62" cy="78" r="4" fill="#111827"/><circle cx="178" cy="105" r="10" fill="#f5f5f4"/>'
DUCK = '<ellipse cx="105" cy="110" rx="65" ry="35" fill="#cbd5e1" stroke="#334155"/><path d="M140 100 q20 -70 0 -80 q-25 -5 -25 25 q0 30 10 55z" fill="#1e293b"/><circle cx="135" cy="35" r="20" fill="#065f46"/><path d="M152 38 l25 6 l-25 6z" fill="#facc15"/><circle cx="138" cy="30" r="3" fill="#fff"/><path d="M95 145 v15 m20 -15 v15" stroke="#f97316" stroke-width="4"/>'
CRAB = '<ellipse cx="110" cy="100" rx="50" ry="32" fill="#dc2626"/>' + ''.join(f'<path d="M{110 + s * 40} {105 + k * 8} l{s * 40} {10 + k * 6}" stroke="#dc2626" stroke-width="5"/>' for s in (-1, 1) for k in range(3)) + '<path d="M80 75 l-25 -30 M140 75 l25 -30" stroke="#dc2626" stroke-width="6"/><path d="M45 50 a14 14 0 1 1 22 -12 l-10 6z M175 50 a14 14 0 1 0 -22 -12 l10 6z" fill="#dc2626"/>'
BAMBOO = ''.join(f'<rect x="{x}" y="10" width="14" height="155" fill="#65a30d" stroke="#365314"/>' + ''.join(f'<line x1="{x}" y1="{y}" x2="{x + 14}" y2="{y}" stroke="#365314" stroke-width="3"/>' for y in (40, 80, 120)) for x in (50, 100, 150)) + ''.join(f'<path d="M{x + 14} {y} q25 -10 40 5" stroke="#16a34a" stroke-width="5" fill="none"/>' for x, y in ((50, 40), (100, 80), (150, 30)))
SUGARCANE = ''.join(f'<rect x="{x}" y="15" width="12" height="150" fill="#d9f99d" stroke="#4d7c0f"/>' + ''.join(f'<line x1="{x}" y1="{y}" x2="{x + 12}" y2="{y}" stroke="#4d7c0f" stroke-width="2"/>' for y in (45, 75, 105, 135)) for x in (60, 95, 130, 165)) + ''.join(f'<path d="M{x} 20 q-30 -5 -45 20" stroke="#16a34a" stroke-width="5" fill="none"/>' for x in (66, 136))
MAIZE = '<rect x="104" y="20" width="12" height="145" fill="#4d7c0f"/>' + ''.join(f'<path d="M110 {y} q{s * 60} -20 {s * 85} 10" stroke="#16a34a" stroke-width="7" fill="none"/>' for y, s in ((60, -1), (80, 1), (105, -1), (125, 1))) + '<ellipse cx="130" cy="95" rx="10" ry="25" fill="#facc15" stroke="#a16207"/>'

PEA = ''.join(f'<path d="M{x} 20 q-10 70 5 140" stroke="#15803d" stroke-width="3" fill="none"/><path d="M{x - 5} {y} q14 -25 26 0 q-12 38 -26 0z" fill="#86efac" stroke="#166534"/>' for x, y in ((50, 80), (110, 60), (165, 95)))
ROSE = '<path d="M110 160 V80" stroke="#166534" stroke-width="4"/><ellipse cx="80" cy="120" rx="20" ry="11" fill="#166534"/><ellipse cx="140" cy="105" rx="20" ry="11" fill="#166534"/><circle cx="110" cy="60" r="32" fill="#dc2626"/><path d="M90 55 q20 -25 40 0 q-20 20 -40 0" stroke="#7f1d1d" fill="none" stroke-width="2"/>'
MANGO = '<path d="M20 20 Q110 0 200 30" stroke="#166534" stroke-width="5" fill="none"/>' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="30" fill="#f97316" stroke="#9a3412"/>' for x, y in ((70, 80), (120, 95), (165, 75), (100, 135)))
MONO_SEED = '<ellipse cx="0" cy="0" rx="22" ry="30" fill="#fde68a" stroke="#a16207"/><path d="M-8 -20 q-6 25 6 45" stroke="#a16207" fill="none"/>'
DI_SEED = '<ellipse cx="-14" cy="0" rx="18" ry="26" fill="#bef264" stroke="#3f6212"/><ellipse cx="14" cy="0" rx="18" ry="26" fill="#bef264" stroke="#3f6212"/>'
MONO_LEAF = '<path d="M-15 35 Q-25 -20 0 -40 Q25 -20 15 35z" fill="#4ade80" stroke="#166534"/>' + ''.join(f'<path d="M{x} 33 Q{x * 1.2} -10 0 -38" stroke="#166534" fill="none"/>' for x in (-10, -4, 4, 10))
DI_LEAF = '<path d="M0 40 Q-38 0 0 -40 Q38 0 0 40z" fill="#4ade80" stroke="#166534"/><path d="M0 40 V-38" stroke="#166534"/>' + ''.join(f'<path d="M0 {y} l{s * 18} -10 m{-s * 8} 4 l{s * 3} 8" stroke="#166534" fill="none"/>' for y in (-20, 0, 20) for s in (-1, 1))
MONO_FLOWER = ''.join(f'<ellipse cx="{22 * __import__("math").cos(a)}" cy="{22 * __import__("math").sin(a)}" rx="20" ry="9" transform="rotate({a * 57.3} {22 * __import__("math").cos(a)} {22 * __import__("math").sin(a)})" fill="#facc15" stroke="#a16207"/>' for a in [0.5, 2.6, 4.7]) + '<circle r="6" fill="#92400e"/>'
DI_FLOWER = ''.join(f'<ellipse cx="{22 * __import__("math").cos(a)}" cy="{22 * __import__("math").sin(a)}" rx="20" ry="11" transform="rotate({a * 57.3} {22 * __import__("math").cos(a)} {22 * __import__("math").sin(a)})" fill="#f87171" stroke="#b91c1c"/>' for a in [0, 1.26, 2.51, 3.77, 5.03]) + '<circle r="6" fill="#7f1d1d"/>'


def mono_di_table():
    rows = [('Seed', MONO_SEED, DI_SEED), ('Leaf', MONO_LEAF, DI_LEAF), ('Flower', MONO_FLOWER, DI_FLOWER)]
    out = ['<svg viewBox="0 0 520 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15">',
           '<rect x="5" y="5" width="510" height="320" fill="#fff" stroke="#334155"/>',
           '<line x1="5" y1="35" x2="515" y2="35" stroke="#334155"/><line x1="120" y1="5" x2="120" y2="325" stroke="#334155"/><line x1="320" y1="5" x2="320" y2="325" stroke="#334155"/>',
           '<text x="62" y="26" text-anchor="middle" font-weight="bold">Part of Plant</text><text x="220" y="26" text-anchor="middle" font-weight="bold">Monocot Plant</text><text x="417" y="26" text-anchor="middle" font-weight="bold">Dicot Plant</text>']
    for i, (name, m, d) in enumerate(rows):
        y = 35 + i * 97
        if i:
            out.append(f'<line x1="5" y1="{y}" x2="515" y2="{y}" stroke="#334155"/>')
        out.append(f'<text x="62" y="{y + 53}" text-anchor="middle" font-weight="bold">{name}</text>')
        out.append(f'<g transform="translate(220,{y + 48})">{m}</g><g transform="translate(417,{y + 48})">{d}</g>')
    out.append('</svg>')
    return '\n'.join(out)


def fish(body, fin, shark=False, stripe=None):
    tail = '<path d="M30 90 l-25 -25 v50z" fill="%s" stroke="#334155"/>' % fin
    shape = ('<path d="M30 90 Q100 40 190 85 Q100 130 30 90z" fill="%s" stroke="#334155"/>' % body) if not shark else ('<path d="M25 90 Q110 55 195 92 L165 100 Q100 120 25 90z" fill="%s" stroke="#334155"/><path d="M100 70 l15 -30 l10 32z" fill="%s"/>' % (body, fin))
    s = '' if not stripe else '<path d="M110 60 v60 M140 65 v50" stroke="%s" stroke-width="10"/>' % stripe
    return tail + shape + s + '<circle cx="165" cy="82" r="4" fill="#111827"/><path d="M95 60 q15 -18 35 0" fill="%s"/>' % fin


BUTTERFLY = '<ellipse cx="110" cy="90" rx="6" ry="40" fill="#1e293b"/><path d="M110 70 Q40 10 30 70 Q40 110 110 90z M110 70 Q180 10 190 70 Q180 110 110 90z" fill="#60a5fa" stroke="#1e3a8a"/><path d="M110 95 Q55 100 60 140 Q90 150 110 105z M110 95 Q165 100 160 140 Q130 150 110 105z" fill="#93c5fd" stroke="#1e3a8a"/><path d="M106 52 l-12 -20 M114 52 l12 -20" stroke="#1e293b" stroke-width="2"/>'
PIGEON = '<ellipse cx="100" cy="100" rx="55" ry="35" fill="#9ca3af" stroke="#374151"/><circle cx="150" cy="65" r="20" fill="#6b7280" stroke="#374151"/><path d="M168 65 l14 4 l-14 4z" fill="#f59e0b"/><circle cx="154" cy="61" r="3" fill="#dc2626"/><path d="M50 95 l-35 25 l40 -5z" fill="#4b5563"/><path d="M95 133 v20 m20 -20 v20" stroke="#dc2626" stroke-width="3"/>'

def frog(c):
    return f'<ellipse cx="110" cy="100" rx="55" ry="35" fill="{c}" stroke="#334155"/><circle cx="85" cy="68" r="12" fill="{c}" stroke="#334155"/><circle cx="135" cy="68" r="12" fill="{c}" stroke="#334155"/><circle cx="85" cy="68" r="5" fill="#111827"/><circle cx="135" cy="68" r="5" fill="#111827"/><path d="M60 120 q-30 20 -15 35 M160 120 q30 20 15 35" stroke="{c}" stroke-width="10" fill="none"/>'


def lizard(c, spots='#111827'):
    return f'<path d="M20 100 Q60 85 100 95 Q140 80 175 92 Q200 95 210 85 Q200 105 175 102 Q140 112 100 110 Q60 115 20 100z" fill="{c}" stroke="#334155"/>' + ''.join(f'<circle cx="{x}" cy="{98 + (x % 3)}" r="3" fill="{spots}"/>' for x in range(60, 170, 18)) + '<path d="M80 108 l-8 22 M130 108 l8 22 M80 92 l-8 -20 M130 92 l8 -20" stroke="#334155" stroke-width="4"/>'


TORTOISE = '<path d="M40 120 Q110 20 180 120z" fill="#92400e" stroke="#451a03"/><path d="M70 100 l20 -25 h40 l20 25" stroke="#451a03" fill="none"/><ellipse cx="190" cy="115" rx="16" ry="11" fill="#a16207"/><path d="M60 120 v15 M160 120 v15" stroke="#a16207" stroke-width="10"/>'
SNAKE = '<path d="M30 150 Q60 120 100 140 T170 120 Q180 90 140 90 Q110 85 120 60 Q130 40 150 50" stroke="#a16207" stroke-width="12" fill="none" stroke-linecap="round"/><ellipse cx="152" cy="46" rx="12" ry="8" fill="#a16207"/><path d="M162 46 l10 -2 m-10 2 l10 3" stroke="#dc2626"/>'
CROCODILE = '<path d="M10 100 Q60 80 120 90 L210 85 L215 95 L120 108 Q60 118 10 100z" fill="#4d7c0f" stroke="#1a2e05"/>' + ''.join(f'<path d="M{x} 89 l5 -8 l5 8" fill="#365314"/>' for x in range(40, 120, 12)) + '<path d="M60 105 l-8 20 M110 105 l8 20" stroke="#365314" stroke-width="6"/>'

def bird(body, head, beak='#f59e0b', long_legs=False, long_neck=False, tail=None, wings_up=False):
    legs = 60 if long_legs else 20
    neck = f'<path d="M140 95 Q150 60 145 35" stroke="{head}" stroke-width="10" fill="none"/>' if long_neck else ''
    hy = 35 if long_neck else 70
    s = f'<ellipse cx="105" cy="{105 - legs // 3}" rx="50" ry="30" fill="{body}" stroke="#334155"/>' + neck
    s += f'<circle cx="{145 if long_neck else 150}" cy="{hy}" r="16" fill="{head}" stroke="#334155"/><path d="M{160 if long_neck else 165} {hy} l16 4 l-16 4z" fill="{beak}"/>'
    s += f'<path d="M95 {130 - legs // 3} v{legs} M115 {130 - legs // 3} v{legs}" stroke="#a16207" stroke-width="3"/>'
    if tail:
        s += f'<path d="M58 {95 - legs // 3} q-40 -40 -30 20 q10 -10 30 -5z" fill="{tail}"/>'
    if wings_up:
        s += f'<path d="M100 {85 - legs // 3} q-20 -60 -70 -50 q30 30 60 55z" fill="{body}" stroke="#334155"/>'
    return s


def dinos():
    return ('<svg viewBox="0 0 470 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15">'
            '<rect x="5" y="5" width="460" height="250" fill="#fff" stroke="#334155"/>'
            '<path d="M40 210 Q60 140 90 140 Q110 60 70 40 Q60 30 80 30 Q120 50 110 140 Q150 150 180 200 Q230 220 260 200 Q220 230 170 225 L60 215z" fill="#60a5fa" stroke="#1e3a8a"/>'
            '<path d="M250 90 Q300 60 360 80 L420 75 L400 92 Q360 110 300 105 L260 115z" fill="#4d7c0f" stroke="#1a2e05"/><path d="M400 75 l15 -15 M410 80 l20 -8" stroke="#1a2e05" stroke-width="3"/>'
            '<path d="M260 190 Q320 150 380 170 L440 180 Q380 200 320 200z" fill="#22c55e" stroke="#14532d"/>' + ''.join(f'<path d="M{x} 168 l8 -18 l8 18" fill="#15803d"/>' for x in range(290, 380, 18)) +
            '<path d="M70 180 Q100 150 130 165 Q160 170 175 200 L140 195 Q110 200 80 190z" fill="#a3e635" stroke="#3f6212"/>'
            '<path d="M150 240 Q230 225 300 230 L360 220 L350 235 Q280 245 150 245z" fill="#a3a36b" stroke="#57534e"/>'
            '<rect x="5" y="255" width="460" height="40" fill="#fdba74" stroke="#334155"/><text x="235" y="281" text-anchor="middle" font-weight="bold">Dinosaurs</text></svg>')


PENGUIN = '<ellipse cx="110" cy="95" rx="38" ry="60" fill="#111827"/><ellipse cx="115" cy="105" rx="24" ry="45" fill="#f8fafc"/><circle cx="120" cy="45" r="5" fill="#fff"/><path d="M140 50 l18 6 l-18 4z" fill="#f59e0b"/><path d="M100 155 l-10 8 h20z M125 155 l-5 8 h20z" fill="#f59e0b"/>'
WOODPECKER = '<rect x="140" y="5" width="50" height="160" fill="#78716c"/><ellipse cx="110" cy="95" rx="22" ry="48" fill="#111827"/><circle cx="110" cy="45" r="16" fill="#111827"/><path d="M100 32 q10 -15 22 0z" fill="#dc2626"/><path d="M124 45 l18 2 l-18 5z" fill="#57534e"/>'
HUMMINGBIRD = '<ellipse cx="100" cy="100" rx="35" ry="16" transform="rotate(-25 100 100)" fill="#16a34a"/><circle cx="130" cy="78" r="12" fill="#15803d"/><path d="M140 75 l40 -10" stroke="#111827" stroke-width="2"/><path d="M95 90 q-30 -60 -60 -40 q30 20 60 40z" fill="#4ade80" stroke="#166534"/><path d="M70 115 l-30 25" stroke="#166534" stroke-width="6"/>'
EAGLE = bird('#3f2a14', '#f8fafc', '#facc15')

def quad(c, mane=None, trunk=False, horns=False, small=False, udder=False):
    k = 0.7 if small else 1.0
    s = f'<g transform="translate({30 if small else 0},{40 if small else 0}) scale({k})">'
    s += f'<ellipse cx="105" cy="90" rx="60" ry="30" fill="{c}" stroke="#334155"/>'
    s += ''.join(f'<rect x="{x}" y="105" width="11" height="50" fill="{c}" stroke="#334155"/>' for x in (60, 80, 125, 145))
    s += f'<ellipse cx="172" cy="62" rx="22" ry="18" fill="{c}" stroke="#334155"/><circle cx="180" cy="58" r="3" fill="#111827"/>'
    if mane:
        s += f'<circle cx="168" cy="62" r="28" fill="{mane}" opacity="0.85"/><ellipse cx="176" cy="64" rx="15" ry="13" fill="{c}"/>'
    if trunk:
        s += f'<path d="M190 70 q15 30 0 60" stroke="{c}" stroke-width="12" fill="none"/><ellipse cx="160" cy="62" rx="16" ry="22" fill="{c}" stroke="#334155"/>'
    if horns:
        s += '<path d="M165 46 q-5 -15 5 -18 M182 46 q5 -15 -5 -18" stroke="#e7e5e4" stroke-width="4" fill="none"/>'
    if udder:
        s += '<ellipse cx="120" cy="118" rx="12" ry="7" fill="#fbcfe8"/>'
    s += f'<path d="M45 85 q-20 15 -15 45" stroke="{c}" stroke-width="5" fill="none"/></g>'
    return s


CAT = '<ellipse cx="110" cy="110" rx="55" ry="35" fill="#d6a46b" stroke="#78350f"/><circle cx="110" cy="65" r="30" fill="#d6a46b" stroke="#78350f"/><path d="M85 45 l-5 -25 l20 15z M135 45 l5 -25 l-20 15z" fill="#d6a46b" stroke="#78350f"/><circle cx="100" cy="62" r="4"/><circle cx="120" cy="62" r="4"/><path d="M95 75 h-25 M125 75 h25" stroke="#78350f"/>'
BAT = '<ellipse cx="110" cy="85" rx="12" ry="25" fill="#78350f"/><path d="M98 80 Q60 40 20 70 Q40 80 45 95 Q70 85 98 95z M122 80 Q160 40 200 70 Q180 80 175 95 Q150 85 122 95z" fill="#a16207" stroke="#78350f"/><path d="M104 62 l-3 -10 l8 6 M116 62 l3 -10 l-8 6" fill="#78350f"/>'
PLATYPUS = '<ellipse cx="100" cy="100" rx="70" ry="35" fill="#a8a29e" stroke="#57534e"/><path d="M165 95 q35 -10 40 10 q-20 15 -40 5z" fill="#57534e"/><path d="M35 100 q-25 0 -25 20 q20 5 30 -10z" fill="#78716c"/><path d="M70 130 l-10 15 h20z M130 130 l-5 15 h20z" fill="#57534e"/>'
KANGAROO = '<ellipse cx="110" cy="100" rx="28" ry="45" fill="#b45309" stroke="#78350f"/><circle cx="120" cy="45" r="16" fill="#b45309" stroke="#78350f"/><path d="M115 30 l-3 -18 l8 14 M125 30 l5 -16 l-1 18" fill="#b45309"/><ellipse cx="115" cy="110" rx="14" ry="12" fill="#d97706"/><circle cx="117" cy="104" r="5" fill="#b45309"/><path d="M90 140 l-30 20 h50 M85 120 q-40 20 -60 35" stroke="#b45309" stroke-width="10" fill="none"/>'

SPONGES = ''.join(f'<path d="M{x} 160 q-15 -60 0 -{h} q20 -10 30 0 q10 {h - 20} -5 {h}z" fill="{c}" stroke="#831843"/>' + ''.join(f'<circle cx="{x + 15}" cy="{160 - k * 20}" r="4" fill="#831843" opacity="0.6"/>' for k in range(1, h // 20)) for x, h, c in ((30, 120, '#f472b6'), (90, 90, '#c084fc'), (150, 110, '#fb7185')))
EARTHWORM = '<path d="M30 110 Q70 60 110 100 T190 90" stroke="#b45309" stroke-width="14" fill="none" stroke-linecap="round"/>' + ''.join(f'<line x1="{x}" y1="80" x2="{x}" y2="120" stroke="#78350f" stroke-width="1" opacity="0.5"/>' for x in range(50, 180, 12))
ASCARIS = '<path d="M60 150 Q20 80 70 60 Q120 40 100 110 Q80 160 140 140 Q190 110 150 50 Q130 20 170 30" stroke="#e7d5b3" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M60 150 Q20 80 70 60 Q120 40 100 110 Q80 160 140 140 Q190 110 150 50 Q130 20 170 30" stroke="#a16207" stroke-width="1" fill="none"/>'
LIVERFLUKE = '<path d="M30 100 Q60 40 150 50 Q205 70 200 100 Q190 140 120 150 Q50 150 30 100z" fill="#d97706" stroke="#78350f"/>' + ''.join(f'<path d="M{x} 70 q8 30 0 60" stroke="#92400e" fill="none"/>' for x in range(60, 180, 14))

def insect(c, stripes=None, long_legs=False, labels=False, wings='#e0f2fe'):
    L = 40 if long_legs else 22
    s = f'<path d="M80 75 q30 -45 70 -20 q-30 20 -70 20z" fill="{wings}" stroke="#64748b" opacity="0.8"/>'
    s += f'<ellipse cx="160" cy="90" rx="14" ry="12" fill="{c}" stroke="#1f2937"/><ellipse cx="128" cy="92" rx="18" ry="14" fill="{c}" stroke="#1f2937"/><ellipse cx="80" cy="96" rx="34" ry="18" fill="{c}" stroke="#1f2937"/>'
    if stripes:
        s += ''.join(f'<path d="M{x} 80 v32" stroke="{stripes}" stroke-width="6"/>' for x in (66, 82, 98))
    s += ''.join(f'<path d="M{x} 102 l{d} {L}" stroke="#1f2937" stroke-width="2"/>' for x, d in ((118, -10), (128, 0), (138, 10)))
    s += '<path d="M168 84 l18 -18 M170 88 l22 -8" stroke="#1f2937" stroke-width="2"/>'
    if labels:
        s += '<g font-size="11"><text x="150" y="35">Thorax</text><text x="170" y="60">Head</text><text x="40" y="65">Abdomen</text></g><path d="M155 38 L130 78 M178 63 L163 82 M60 68 L75 82" stroke="#334155"/>'
    return s


MOSQUITO = '<ellipse cx="90" cy="95" rx="40" ry="8" transform="rotate(-20 90 95)" fill="#57534e"/><circle cx="135" cy="78" r="8" fill="#44403c"/><path d="M142 76 l30 -10" stroke="#111827"/><path d="M100 85 q20 -40 50 -40 q-20 30 -50 40z" fill="#e5e7eb" stroke="#9ca3af"/>' + ''.join(f'<path d="M{x} 95 q{d} 20 {d * 2} 60" stroke="#111827" fill="none"/>' for x, d in ((95, -15), (105, -5), (115, 10)))
STICK = '<path d="M30 100 H190" stroke="#57534e" stroke-width="6"/>' + ''.join(f'<path d="M{x} 100 l{dx} {dy}" stroke="#57534e" stroke-width="3"/>' for x, dx, dy in ((70, -30, -50), (70, -25, 45), (110, 10, -55), (110, 15, 50), (150, 35, -40), (150, 30, 45)))
LEAFINSECT = '<path d="M50 100 Q90 40 170 80 Q120 140 50 100z" fill="#86efac" stroke="#15803d"/><path d="M60 98 Q110 85 165 82" stroke="#15803d" fill="none"/><circle cx="175" cy="80" r="8" fill="#4ade80"/>' + ''.join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#15803d" stroke-width="3"/>' for x, y, dx, dy in ((110, 90, -10, -40), (110, 100, -5, 45), (140, 85, 15, -35), (140, 95, 20, 40)))
SNAIL = '<path d="M20 145 Q100 130 200 145 Q150 155 20 150z" fill="#d6d3d1" stroke="#78716c"/><circle cx="110" cy="100" r="42" fill="#b45309" stroke="#78350f"/><path d="M110 100 m-30 0 a30 30 0 1 1 30 30 a20 20 0 1 1 0 -40 a10 10 0 1 1 -10 10" stroke="#78350f" fill="none" stroke-width="3"/><path d="M50 140 q-10 -40 -5 -60 M45 80 l-5 -15 M45 80 l8 -14" stroke="#a8a29e" stroke-width="5" fill="none"/>'
OYSTER = '<path d="M30 110 Q60 40 110 70 Q120 120 30 110z" fill="#e7e5e4" stroke="#57534e"/><path d="M110 70 Q170 40 200 100 Q150 140 110 70z" fill="#d6d3d1" stroke="#57534e"/><circle cx="75" cy="90" r="9" fill="#fb923c"/><circle cx="88" cy="96" r="8" fill="#fb923c"/><circle cx="150" cy="90" r="9" fill="#fb923c"/>'
OCTOPUS = '<ellipse cx="110" cy="65" rx="40" ry="35" fill="#c2410c"/>' + ''.join(f'<path d="M{90 + i * 6} 95 Q{40 + i * 20} {130 + (i % 2) * 20} {20 + i * 26} {110 + (i % 3) * 15}" stroke="#c2410c" stroke-width="7" fill="none" stroke-linecap="round"/>' for i in range(7))

import math as _m


def star(cx, cy, r1, r2, n=5, c='#f97316'):
    pts = []
    for i in range(2 * n):
        r = r1 if i % 2 == 0 else r2
        a = -_m.pi / 2 + i * _m.pi / n
        pts.append(f'{cx + r * _m.cos(a):.1f},{cy + r * _m.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{c}" stroke="#9a3412"/>'


ANEMONE = '<path d="M70 160 Q75 100 110 100 Q145 100 150 160z" fill="#f472b6" stroke="#9d174d"/>' + ''.join(f'<path d="M110 100 Q{110 + 70 * _m.cos(a)} {80 + 40 * _m.sin(a)} {110 + 80 * _m.cos(a)} {60 + 50 * _m.sin(a)}" stroke="#ec4899" stroke-width="4" fill="none"/>' for a in [-_m.pi + k * 0.25 for k in range(13)])
BRITTLE = '<circle cx="110" cy="90" r="12" fill="#ea580c"/>' + ''.join(f'<path d="M110 90 Q{110 + 40 * _m.cos(a) + 15} {90 + 40 * _m.sin(a)} {110 + 75 * _m.cos(a)} {90 + 75 * _m.sin(a)}" stroke="#ea580c" stroke-width="5" fill="none" stroke-linecap="round"/>' for a in [-_m.pi / 2 + k * 2 * _m.pi / 5 for k in range(5)])

DOLPHIN = '<path d="M30 130 Q20 60 90 50 Q150 45 190 60 L205 58 L190 70 Q150 80 120 85 Q80 100 60 140 L40 160 L55 135z" fill="#a8a29e" stroke="#57534e"/><path d="M190 64 l18 -4" stroke="#57534e" stroke-width="3"/><path d="M110 50 l10 -15 l8 16" fill="#78716c"/>'
MANGROVE = '<rect x="0" y="130" width="216" height="40" fill="#bae6fd"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4d7c0f"/>' for x, y, r in ((40, 60, 35), (90, 45, 40), (140, 55, 38), (180, 70, 30))) + ''.join(f'<path d="M{x} 95 q{d} 30 {d * 1.5} 55" stroke="#9a3412" stroke-width="3" fill="none"/>' for x in range(40, 190, 14) for d in (-12, 12))

def bird_feet():
    leg = '<rect x="-6" y="-80" width="12" height="70" fill="{c}"/>'
    A = leg.format(c='#ea580c') + '<path d="M0 -10 L-40 50 Q0 35 40 50z" fill="#f97316" stroke="#9a3412"/><path d="M0 -10 L-30 45 M0 -10 L0 40 M0 -10 L30 45" stroke="#9a3412"/>'
    B = leg.format(c='#292524') + ''.join(f'<path d="M0 -10 q{d} 20 {d * 1.5} 40 l{d / 3:.0f} 8" stroke="#eab308" stroke-width="7" fill="none"/>' for d in (-18, 0, 18)) + '<path d="M0 -5 l-5 25" stroke="#eab308" stroke-width="6"/>'
    C = leg.format(c='#57534e') + ''.join(f'<path d="M0 -10 l{d} 45" stroke="#d6a46b" stroke-width="7"/>' for d in (-28, 0, 28)) + '<path d="M0 -10 l15 -18" stroke="#d6a46b" stroke-width="6"/>'
    D = leg.format(c='#57534e') + ''.join(f'<path d="M0 -10 q{d} 15 {d * 1.3} 35 l3 8" stroke="#a8a29e" stroke-width="4" fill="none"/>' for d in (-20, 0, 20)) + '<path d="M0 -10 l-14 -14" stroke="#a8a29e" stroke-width="4"/>'
    out = ['<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="18" font-weight="bold">']
    for i, (lab, f) in enumerate((('A', A), ('B', B), ('C', C), ('D', D))):
        out.append(f'<g transform="translate({80 + i * 160},100)">{f}</g><text x="{80 + i * 160}" y="190" text-anchor="middle">{lab}</text>')
    out.append('</svg>')
    return '\n'.join(out)


def cup_microscope():
    s = ['<svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">']
    steps = [('1. Plastic cup with a hole in its base', '<path d="M-45 -60 L-30 60 H30 L45 -60z" fill="#e0f2fe" stroke="#0369a1"/><circle cx="0" cy="60" r="10" fill="#fff" stroke="#0369a1"/>'),
             ('2. Plastic sheet tied with a rubber band', '<path d="M-45 -40 L-30 60 H30 L45 -40z" fill="#e0f2fe" stroke="#0369a1"/><path d="M-55 -45 Q0 -60 55 -45 L50 -35 Q0 -48 -50 -35z" fill="#f1f5f9" stroke="#64748b"/><path d="M-48 -38 H48" stroke="#ef4444" stroke-width="4"/>'),
             ('3. A drop of water on the sheet — tiny object seen larger', '<path d="M-45 -40 L-30 60 H30 L45 -40z" fill="#e0f2fe" stroke="#0369a1"/><path d="M-55 -45 Q0 -60 55 -45" stroke="#64748b" fill="none"/><ellipse cx="0" cy="-52" rx="16" ry="8" fill="#7dd3fc" stroke="#0284c7"/><circle cx="0" cy="45" r="5" fill="#92400e"/>')]
    for i, (lab, d) in enumerate(steps):
        s.append(f'<rect x="{10 + i * 210}" y="5" width="200" height="210" fill="#f8fafc" stroke="#94a3b8"/><g transform="translate({110 + i * 210},95)">{d}</g><text x="{110 + i * 210}" y="200" text-anchor="middle">{lab}</text>')
    s.append('</svg>')
    return '\n'.join(s)


BACILLI = ''.join(f'<rect x="{x}" y="{y}" width="46" height="16" rx="8" transform="rotate({r} {x + 23} {y + 8})" fill="#93c5fd" stroke="#1e40af"/>' for x, y, r in ((20, 40, 20), (70, 30, -15), (120, 50, 35), (40, 90, -30), (100, 100, 10), (150, 90, -40), (60, 135, 15), (130, 140, -10)))
FLAGELLATE = '<rect x="40" y="70" width="110" height="44" rx="22" fill="#a5f3fc" stroke="#0e7490"/>' + ''.join(f'<path d="M150 {82 + k * 8} q20 -10 40 {-20 + k * 6} t30 -5" stroke="#0e7490" fill="none"/>' for k in range(3))
FILAMENT = '<path d="M30 150 Q80 120 110 90 T190 30" stroke="#a3e635" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M30 150 Q80 120 110 90 T190 30" stroke="#3f6212" stroke-width="2" stroke-dasharray="4 6" fill="none"/>'

def spiky(c, spike, n=16, r=45, knob=8):
    s = f'<circle cx="110" cy="85" r="{r}" fill="{c}" stroke="#1f2937"/>'
    for i in range(n):
        a = 2 * _m.pi * i / n
        x1, y1 = 110 + r * _m.cos(a), 85 + r * _m.sin(a)
        x2, y2 = 110 + (r + 18) * _m.cos(a), 85 + (r + 18) * _m.sin(a)
        s += f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{spike}" stroke-width="4"/><circle cx="{x2:.0f}" cy="{y2:.0f}" r="{knob}" fill="{spike}"/>'
    return s


PHAGE = '<polygon points="110,15 130,27 130,52 110,64 90,52 90,27" fill="#db2777" stroke="#831843"/><rect x="105" y="64" width="10" height="55" fill="#be185d"/><rect x="95" y="119" width="30" height="6" fill="#831843"/>' + ''.join(f'<path d="M110 125 L{110 + d} 150 L{110 + d * 1.3:.0f} 165" stroke="#831843" stroke-width="2" fill="none"/>' for d in (-40, -22, 22, 40))

ROUND = ''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="#818cf8" stroke="#3730a3"/>' for x, y in ((40, 50), (60, 62), (82, 70), (104, 75), (126, 72), (148, 64), (170, 52), (70, 110), (95, 120), (120, 125), (145, 118)))
SPIRAL = ''.join(f'<path d="M{x} {y} q12 -18 24 0 t24 0 t24 0 t24 0 t24 0" stroke="#7f1d1d" stroke-width="5" fill="none"/>' for x, y in ((25, 60), (45, 120)))
MOLD = '<circle cx="110" cy="85" r="65" fill="#fb923c" stroke="#c2410c"/><circle cx="110" cy="85" r="35" fill="#a7f3d0" stroke="#047857" opacity="0.9"/><circle cx="110" cy="85" r="15" fill="#10b981"/>'
TOADSTOOL = ''.join(f'<rect x="{x - 8}" y="{y}" width="16" height="{150 - y}" fill="#f5f5f4" stroke="#a8a29e"/><path d="M{x - 40} {y + 5} Q{x} {y - 45} {x + 40} {y + 5}z" fill="#dc2626" stroke="#7f1d1d"/>' + ''.join(f'<circle cx="{x + dx}" cy="{y - 12 + dy}" r="3" fill="#fff"/>' for dx, dy in ((-20, 8), (-5, -10), (12, 0), (25, 10))) for x, y in ((80, 70), (150, 85)))

ROTWOOD = '<path d="M20 120 Q60 60 140 70 Q200 80 200 120 Q150 160 60 150z" fill="#a16207" stroke="#451a03"/>' + ''.join(f'<path d="M{30 + k * 15} {130 - k * 4} q50 -30 120 -20" stroke="#fef3c7" stroke-width="2" fill="none"/>' for k in range(5))
MOLDBREAD = '<path d="M30 140 V70 Q30 30 110 30 Q190 30 190 70 V140z" fill="#fde68a" stroke="#a16207"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f1f5f9" stroke="#94a3b8"/>' for x, y, r in ((70, 70, 15), (130, 95, 20), (160, 60, 10), (90, 115, 12)))
ROTAPPLE = '<circle cx="110" cy="90" r="60" fill="#fbbf24" stroke="#78350f"/><circle cx="105" cy="95" r="45" fill="#451a03"/><path d="M110 30 q5 -15 15 -20" stroke="#57534e" stroke-width="4"/>'

DOUGH = '<path d="M30 140 Q20 100 50 95 H170 Q200 100 190 140z" fill="#d6d3d1" stroke="#78716c"/><path d="M45 100 Q60 20 110 25 Q165 20 175 100z" fill="#fcd34d" stroke="#a16207"/>'
YOGHURT = '<path d="M35 70 H185 Q180 150 110 155 Q40 150 35 70z" fill="#f5f5f4" stroke="#a8a29e"/><ellipse cx="110" cy="70" rx="75" ry="15" fill="#fafaf9" stroke="#a8a29e"/><path d="M150 60 L195 15" stroke="#334155" stroke-width="5"/>'
SEWAGE = '<rect x="15" y="40" width="190" height="110" fill="#a8a29e" stroke="#57534e"/>' + ''.join(f'<rect x="{20 + i * 47}" y="45" width="42" height="100" fill="#78716c" stroke="#44403c"/>' for i in range(4)) + ''.join(f'<path d="M{25 + i * 47} {60 + k * 25} q10 -6 20 0 t20 0" stroke="#d6d3d1" fill="none"/>' for i in range(4) for k in range(3))

FIGS = {
    'foodmicro': lambda: panel_row([('Use of yeast to rise the dough', DOUGH), ('Use of bacteria in making yoghurt', YOGHURT)], None, 190),
    'sewage': lambda: panel_row([('Sewage treatment tanks', SEWAGE)], 'Cleaning of Environment', 190),
    'decomp': lambda: panel_row([('Rotting wood', ROTWOOD), ('Moldy bread', MOLDBREAD), ('Rotten fruit', ROTAPPLE)], 'Harmful Effects of Decomposition', 190),
    'bactshapes': lambda: panel_row([('Round', ROUND), ('Rod-shaped', BACILLI), ('Spiral', SPIRAL)], 'Shapes of Bacteria', 190),
    'fungi3': lambda: panel_row([('Mold on orange', MOLD), ('Mushroom', TOADSTOOL), ('Yeast', YEAST)], 'Fungi', 190),
    'viruses': lambda: panel_row([('Polio virus', spiky('#7f1d1d', '#4338ca', 18, 38, 5)), ('Corona virus', spiky('#44403c', '#dc2626', 14, 45, 9)), ('Bacteriophage virus', PHAGE)], 'Viruses', 190),
    'cupmicro': cup_microscope,
    'micro3': lambda: panel_row([('', FILAMENT), ('', FLAGELLATE), ('', BACILLI)], 'Microorganisms', 190),
    'birdfeet': bird_feet,
    'dolphin': lambda: panel_row([('Indus dolphin', DOLPHIN)], None, 190),
    'mangroves': lambda: panel_row([('Mangroves', MANGROVE)], None, 200),
    'echino': lambda: panel_row([('Starfish', star(110, 85, 70, 28)), ('Sea anemone', ANEMONE), ('Brittle star', BRITTLE)], 'Echinoderms', 190),
    'insects': lambda: panel_row([('Wasp', insect('#facc15', stripes='#111827')), ('Cockroach', insect('#7c2d12', long_legs=True, wings='#9a3412')), ('Mosquito', MOSQUITO), ('Honey bee', insect('#d97706', stripes='#78350f', labels=True))], 'Insects', 190),
    'stickleaf': lambda: panel_row([('Stick insect', STICK), ('Leaf insect', LEAFINSECT)], None, 190),
    'molluscs': lambda: panel_row([('Snail', SNAIL), ('Oyster', OYSTER), ('Octopus', OCTOPUS)], 'Molluscs', 190),
    'sponges': lambda: panel_row([('Sponges', SPONGES)], None, 200),
    'worms': lambda: panel_row([('Earthworm', EARTHWORM), ('Ascaris (Roundworm)', ASCARIS), ('Liverfluke (Flatworm)', LIVERFLUKE)], 'Worms', 200),
    'mammals4': lambda: panel_row([('Horse', quad('#9a3412')), ('Lion', quad('#ca8a04', mane='#78350f')), ('Cow', quad('#d6d3d1', horns=True, udder=True)), ('Cat', CAT)], 'Mammals', 190),
    'mammals5': lambda: panel_row([('Polar bear', quad('#f1f5f9')), ('Elephant', quad('#9ca3af', trunk=True)), ('Bat', BAT), ('Platypus', PLATYPUS), ('Kangaroo', KANGAROO)], None, 190),
    'bigbirds': lambda: panel_row([('Hawk', bird('#57534e', '#44403c', '#facc15', wings_up=True)), ('Hummingbird', HUMMINGBIRD), ('Eagle', EAGLE), ('Penguin', PENGUIN), ('Woodpecker', WOODPECKER)], None, 190),
    'dinos': dinos,
    'birds5': lambda: panel_row([('Dove', bird('#f1f5f9', '#e2e8f0', '#94a3b8', wings_up=True)), ('Sparrow', bird('#a16207', '#c2410c', '#78350f', tail='#92400e')), ('Kiwi', bird('#78350f', '#78350f', '#d6d3d1', long_legs=False)), ('Ostrich', bird('#292524', '#e7e5e4', '#d6d3d1', long_legs=True, long_neck=True)), ('Rooster', bird('#7c2d12', '#ea580c', '#facc15', tail='#1e293b'))], 'Birds', 190),
    'amphibians': lambda: panel_row([('Frog', frog('#a3e635')), ('Salamander', lizard('#1e293b', '#fde047')), ('Toad', frog('#a8765a')), ('Newt', lizard('#9a3412', '#fdba74'))], 'Amphibians', 190),
    'reptiles': lambda: panel_row([('Tortoise', TORTOISE), ('Snake', SNAKE), ('Crocodile', CROCODILE), ('Lizard', lizard('#78716c'))], 'Reptiles', 190),
    'fish5': lambda: panel_row([('Rohu', fish('#a3a3a3', '#78716c')), ('Shark', fish('#94a3b8', '#64748b', shark=True)), ('Catfish', fish('#a8a29e', '#57534e')), ('Goldfish', fish('#fb923c', '#f97316')), ('Butterfly fish', fish('#fde047', '#1e293b', stripe='#1e293b'))], 'Fish', 190),
    'butterflypigeon': lambda: panel_row([('Butterfly', BUTTERFLY), ('Pigeon', PIGEON)], None, 190),
    'dicots': lambda: panel_row([('Pea', PEA), ('Rose', ROSE), ('Mango', MANGO)], 'Dicot plants', 200),
    'monodi': mono_di_table,
    'animalia': lambda: panel_row([('Rabbit', RABBIT), ('Duck', DUCK), ('Crab', CRAB)], 'Kingdom Animalia', 200),
    'monocots': lambda: panel_row([('Bamboo', BAMBOO), ('Sugarcane', SUGARCANE), ('Maize', MAIZE)], 'Monocot Plants', 200),
    'fungi': lambda: panel_row([('Mushroom', MUSHROOM), ('Rhizopus', RHIZOPUS), ('Bracket Fungi', BRACKET), ('Yeast', YEAST)], 'Kingdom Fungi', 200),
    'plantae': lambda: panel_row([('Flowering plant', FLOWERING), ('Pine', PINE), ('Fern', FERN)], 'Kingdom Plantae', 210),
    'monera': lambda: panel_row([('Bacterium', BACTERIUM)], 'Kingdom Monera', 180),
    'protista': lambda: panel_row([('Amoeba', AMOEBA), ('Paramecium', PARAMECIUM), ('Spirogyra', SPIROGYRA)], 'Kingdom Protista', 210),
}

# --- Chapter 4: Environmental Pollution ---
SMOKE = lambda x, y, c='#57534e': f'<g fill="{c}" opacity=".75"><circle cx="{x}" cy="{y}" r="12"/><circle cx="{x + 12}" cy="{y - 16}" r="15"/><circle cx="{x + 28}" cy="{y - 34}" r="18"/></g>'
FORESTFIRE = '<rect x="10" y="20" width="200" height="130" fill="#7c2d12" opacity=".35"/>' + ''.join(f'<path d="M{30 + i * 40} 150 l0 -70 m0 25 l-12 -14 m12 4 l12 -16" stroke="#292524" stroke-width="4" fill="none"/><path d="M{18 + i * 40} 150 q12 -45 12 -60 q10 25 14 10 q8 25 0 50z" fill="#f97316"/>' for i in range(5)) + SMOKE(60, 60) + SMOKE(140, 55)
FACTORY = '<rect x="10" y="20" width="200" height="130" fill="#fdba74" opacity=".4"/>' + ''.join(f'<rect x="{30 + i * 45}" y="70" width="16" height="80" fill="#44403c"/>' + SMOKE(38 + i * 45, 60, '#78716c') for i in range(4)) + '<rect x="10" y="135" width="200" height="15" fill="#292524"/>'
TRAFFIC = '<rect x="10" y="20" width="200" height="130" fill="#cbd5e1"/>' + ''.join(f'<rect x="{20 + i * 62}" y="{95 + (i % 2) * 15}" width="54" height="26" rx="6" fill="#94a3b8" stroke="#334155"/><circle cx="{32 + i * 62}" cy="{122 + (i % 2) * 15}" r="6" fill="#111827"/><circle cx="{62 + i * 62}" cy="{122 + (i % 2) * 15}" r="6" fill="#111827"/>' + SMOKE(14 + i * 62, 110 + (i % 2) * 15, '#475569') for i in range(3))
PIPE = '<rect x="10" y="20" width="200" height="130" fill="#64748b"/><rect x="90" y="40" width="120" height="30" fill="#44403c"/><path d="M95 70 q-20 30 -30 70" stroke="#a3a35a" stroke-width="10" fill="none"/><path d="M10 120 q50 -10 100 0 t100 0 l0 30 l-200 0z" fill="#475569"/>'
GARBAGE = '<rect x="10" y="20" width="200" height="130" fill="#d6d3d1"/>' + ''.join(f'<rect x="{15 + (k * 37) % 185}" y="{70 + (k * 23) % 70}" width="{14 + k % 3 * 6}" height="{10 + k % 4 * 4}" fill="{["#ef4444", "#3b82f6", "#f8fafc", "#22c55e", "#eab308", "#a855f7"][k % 6]}" stroke="#57534e" transform="rotate({k * 17 % 40 - 20} {20 + (k * 37) % 185} {75 + (k * 23) % 70})"/>' for k in range(26))
DUMP = '<rect x="10" y="20" width="200" height="130" fill="#bae6fd"/><path d="M10 150 l0 -40 q60 -40 110 -20 q50 15 90 0 l0 60z" fill="#a8a29e"/><rect x="20" y="40" width="70" height="45" fill="#78716c"/><rect x="85" y="55" width="20" height="30" fill="#57534e"/><circle cx="35" cy="88" r="8" fill="#111827"/><circle cx="80" cy="88" r="8" fill="#111827"/>' + ''.join(f'<circle cx="{110 + k * 11}" cy="{115 + (k % 3) * 8}" r="4" fill="{["#fef3c7", "#e7e5e4", "#fca5a5"][k % 3]}"/>' for k in range(9))
DEADFISH = '<rect x="10" y="20" width="200" height="130" fill="#44403c"/>' + ''.join(f'<g transform="translate({50 + k * 55},{70 + (k % 2) * 40}) rotate({k * 30 - 20})"><ellipse rx="22" ry="9" fill="#e7e5e4"/><path d="M20 0 l12 -8 l0 16z" fill="#e7e5e4"/><circle cx="-14" cy="-2" r="2" fill="#111827"/></g>' for k in range(3))
ACIDTREES = '<rect x="10" y="20" width="200" height="130" fill="#1e3a8a"/>' + ''.join(f'<path d="M{25 + k * 30} 150 l{(k % 3) - 1} -{60 + (k * 13) % 50} m0 20 l-10 -10 m10 20 l9 -12" stroke="#d6d3d1" stroke-width="3" fill="none"/>' for k in range(7))
RAINWATER = '<rect x="10" y="20" width="200" height="130" fill="#14532d"/><path d="M10 150 q50 -40 100 -20 q60 25 100 -10 l0 30z" fill="#4d7c0f"/>' + ''.join(f'<circle cx="{25 + (k * 41) % 180}" cy="{50 + (k * 29) % 80}" r="{5 + k % 3 * 3}" fill="#a3e635" opacity=".7"/>' for k in range(14))
GREENHOUSE = '<rect x="10" y="20" width="200" height="130" fill="#1e293b"/><path d="M25 140 l0 -60 l85 -40 l85 40 l0 60z" fill="#93c5fd" opacity=".55" stroke="#e2e8f0" stroke-width="2"/>' + ''.join(f'<path d="M{45 + k * 20} 140 l0 -{58 + (k if k < 4 else 7 - k) * 10}" stroke="#e2e8f0" stroke-width="1.5"/>' for k in range(8)) + ''.join(f'<circle cx="{35 + k * 17}" cy="132" r="7" fill="#16a34a"/>' for k in range(10))

FIGS.update({
    'airpoll': lambda: panel_row([('Forest fire smoke', FORESTFIRE), ('Industrial smoke', FACTORY), ('Vehicles smoke', TRAFFIC)], 'Air pollution', 190),
    'waterpoll': lambda: panel_row([('Polluted sewerage water', PIPE)], 'Water pollution', 190),
    'landpoll': lambda: panel_row([('Garbage', GARBAGE)], 'Land pollution', 190),
    'dumping': lambda: panel_row([('Disposing of garbage', DUMP)], None, 190),
    'polleffects': lambda: panel_row([('Effects of pollution on aquatic life', DEADFISH), ('Effects of acid rain', ACIDTREES), ('Polluted rain water', RAINWATER)], None, 190),
    'greenhouse': lambda: panel_row([('Greenhouse', GREENHOUSE)], None, 190),
})

FLOOD = '<rect x="10" y="20" width="200" height="130" fill="#a8a29e"/><rect x="10" y="20" width="200" height="40" fill="#cbd5e1"/>' + ''.join(f'<path d="M{20 + k * 45} 75 l0 -30" stroke="#3f6212" stroke-width="4"/><circle cx="{20 + k * 45}" cy="42" r="12" fill="#4d7c0f"/>' for k in range(5)) + '<path d="M10 75 l200 0 l0 75 l-200 0z" fill="#78716c" opacity=".85"/>' + ''.join(f'<g transform="translate({55 + k * 30},{105 + (k % 2) * 6})"><circle r="6" fill="#fde68a"/><rect x="-6" y="5" width="12" height="16" fill="{["#f8fafc", "#16a34a", "#dc2626", "#1d4ed8"][k % 4]}"/></g>' for k in range(4))
ICEMELT = '<rect x="10" y="20" width="200" height="130" fill="#0f766e"/><path d="M10 20 l200 0 l0 70 q-20 10 -30 -5 q-15 15 -30 0 q-20 15 -35 -2 q-20 12 -40 0 q-25 15 -40 -2 q-15 10 -25 0z" fill="#7dd3fc"/>' + ''.join(f'<path d="M{20 + k * 22} 25 l0 55" stroke="#e0f2fe" stroke-width="2"/>' for k in range(9)) + '<path d="M95 85 l25 -15 l10 40 l-30 10z" fill="#bae6fd"/><path d="M100 120 q20 -12 40 0" stroke="#f0f9ff" stroke-width="4" fill="none"/>'
def _icon(kind):
    d = {
        'Wood': ''.join(f'<circle cx="{40 + (k % 4) * 45}" cy="{60 + (k // 4) * 45}" r="20" fill="#dc6b4a" stroke="#7c2d12" stroke-width="3"/><circle cx="{40 + (k % 4) * 45}" cy="{60 + (k // 4) * 45}" r="8" fill="none" stroke="#7c2d12"/>' for k in range(8)),
        'Bread': '<ellipse cx="110" cy="85" rx="80" ry="55" fill="#d97706"/><ellipse cx="110" cy="85" rx="64" ry="42" fill="#fde68a"/><g fill="#a16207"><circle cx="90" cy="75" r="4"/><circle cx="125" cy="95" r="4"/><circle cx="110" cy="70" r="3"/></g>',
        'Water': '<path d="M80 40 l60 0 l-8 105 l-44 0z" fill="#e0f2fe" stroke="#64748b" stroke-width="2"/><path d="M85 80 l50 0 l-5 65 l-40 0z" fill="#60a5fa"/>',
        'Leather': '<path d="M40 40 q70 -15 140 0 l-10 110 q-60 10 -120 0z" fill="#7c2d12"/><path d="M60 50 l0 90 M110 45 l0 100 M160 50 l0 90" stroke="#9a3412" stroke-dasharray="4 4"/>',
        'Stone': ''.join(f'<ellipse cx="{30 + (k * 37) % 170}" cy="{45 + (k * 23) % 100}" rx="{12 + k % 3 * 4}" ry="{9 + k % 2 * 4}" fill="{["#94a3b8", "#64748b", "#cbd5e1"][k % 3]}" stroke="#334155"/>' for k in range(16)),
        'Fruit': ''.join(f'<circle cx="{40 + (k % 4) * 45}" cy="{60 + (k // 4) * 45}" r="20" fill="{["#dc2626", "#f59e0b", "#ea580c", "#facc15"][k % 4]}"/>' for k in range(8)),
        'Vegetables and fruits': ''.join(f'<circle cx="{30 + (k % 6) * 32}" cy="{50 + (k // 6) * 32}" r="14" fill="{["#dc2626", "#16a34a", "#f97316", "#facc15", "#65a30d", "#a855f7"][k % 6]}"/>' for k in range(18)),
        'Meat': '<path d="M60 120 q-30 -40 10 -80 q60 -30 100 20 q20 40 -30 60 q-40 10 -60 0z" fill="#b45309"/><path d="M60 120 l-25 25 m-5 -10 l10 15" stroke="#f5f5f4" stroke-width="8"/>',
        'Paper': ''.join(f'<path d="M{40 + k * 6} {110 - k * 8} l120 -30 l10 15 l-120 30z" fill="#f8fafc" stroke="#64748b"/>' for k in range(5)),
        'Polythene bags': ''.join(f'<path d="M{40 + k * 40} 60 l40 0 l10 85 l-60 0z" fill="{["#38bdf8", "#f97316", "#ef4444", "#22c55e"][k]}" opacity=".85"/><path d="M{45 + k * 40} 60 q5 -30 12 0 M{70 + k * 40} 60 q5 -30 12 0" stroke="{["#38bdf8", "#f97316", "#ef4444", "#22c55e"][k]}" stroke-width="5" fill="none"/>' for k in range(3)),
        'Plastic bottle': '<rect x="102" y="22" width="16" height="14" fill="#1d4ed8"/><path d="M102 36 q-20 15 -20 35 l0 70 q0 8 8 8 l40 0 q8 0 8 -8 l0 -70 q0 -20 -20 -35z" fill="#bfdbfe" stroke="#64748b"/>',
        'Computer components': '<rect x="40" y="40" width="70" height="50" fill="#1f2937"/><rect x="47" y="47" width="56" height="36" fill="#60a5fa"/><rect x="120" y="35" width="45" height="105" fill="#111827"/><rect x="30" y="105" width="85" height="30" fill="#374151"/><path d="M35 115 l75 0 M35 125 l75 0" stroke="#9ca3af"/>',
    }
    return d[kind]
FIGS.update({
    'ghgeffects': lambda: panel_row([('Flood', FLOOD), ('Melting of Ice', ICEMELT)], 'Effects of greenhouse gases', 190),
    'act45': lambda: panel_row([(k, _icon(k)) for k in ('Wood', 'Bread', 'Water', 'Leather', 'Stone', 'Fruit')], None, 190),
    'biodeg': lambda: panel_row([(k, _icon(k)) for k in ('Vegetables and fruits', 'Meat', 'Paper')], 'Biodegradable Materials', 190),
    'nonbiodeg': lambda: panel_row([(k, _icon(k)) for k in ('Polythene bags', 'Plastic bottle', 'Computer components')], 'Non-biodegradable Materials', 190),
})

# --- Chapter 5: Physical and Chemical Changes of Matter ---
def _beaker(x, state):
    """Beaker 100x110 at x (y 30..140) filled with particles in a solid, liquid or gas arrangement."""
    out = [f'<path d="M{x} 30 l0 105 q0 6 6 6 l88 0 q6 0 6 -6 l0 -105" fill="#fff" stroke="#111827" stroke-width="3"/>']
    import random
    rnd = random.Random(7)
    if state == 'solid':
        pts = [(x + 12 + c * 13, 40 + r * 13) for r in range(8) for c in range(7)]
    elif state == 'liquid':
        pts = [(x + 12 + c * 14 + rnd.uniform(-3, 3), 62 + r * 14 + rnd.uniform(-3, 3)) for r in range(6) for c in range(6) if rnd.random() > .12]
    else:
        pts = [(x + 14 + rnd.uniform(0, 72), 38 + rnd.uniform(0, 92)) for _ in range(11)]
    out += [f'<circle cx="{a:.0f}" cy="{b:.0f}" r="6" fill="#2563eb" stroke="#1e3a8a"/>' for a, b in pts]
    return ''.join(out)


def state_change(left, right, arrow, title):
    """Two beakers (left -> right state) with an arrow and the printed text above it, plus an orange caption bar."""
    lines = arrow.split('|')
    txt = ''.join(f'<text x="210" y="{48 + i * 17}" text-anchor="middle" font-weight="bold">{s}</text>' for i, s in enumerate(lines))
    return (f'<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14">'
            f'<rect x="2" y="2" width="416" height="172" fill="#fff" stroke="#334155"/>{_beaker(20, left)}{_beaker(300, right)}{txt}'
            f'<path d="M170 110 l70 0" stroke="#111827" stroke-width="2.5"/><path d="M240 110 l-10 -6 l0 12z" fill="#111827"/>'
            f'<text x="70" y="163" text-anchor="middle" font-weight="bold">{left.capitalize()}</text><text x="350" y="163" text-anchor="middle" font-weight="bold">{right.capitalize()}</text>'
            f'<rect x="2" y="176" width="416" height="32" fill="#f87171" stroke="#334155"/><text x="210" y="197" text-anchor="middle" font-weight="bold">{title}</text></svg>')

DISH = lambda cx, cy, water=True: f'<ellipse cx="{cx}" cy="{cy + 10}" rx="62" ry="16" fill="#d1d5db" stroke="#111827" stroke-width="3"/><ellipse cx="{cx}" cy="{cy}" rx="62" ry="16" fill="{"#7dd3fc" if water else "#f1f5f9"}" stroke="#111827" stroke-width="3"/>'
STIR = DISH(110, 120) + '<path d="M130 40 l-20 85" stroke="#6b7280" stroke-width="5"/><path d="M118 40 q20 -10 30 5 l-5 18 q-15 5 -25 -5z" fill="#ef4444"/>'
BOIL = DISH(110, 50) + '<path d="M60 65 l-35 85 M160 65 l35 85 M110 65 l0 0" stroke="#111827" stroke-width="2"/><rect x="104" y="80" width="12" height="60" fill="#9ca3af"/><path d="M110 62 q-8 10 0 18 q8 -8 0 -18z" fill="#f97316"/><path d="M90 150 l40 0 M95 140 q-30 0 -25 10" stroke="#111827" stroke-width="3" fill="none"/>'
LEFT = DISH(110, 95, False) + ''.join(f'<circle cx="{75 + k * 9}" cy="{95 + (k % 3) - 1}" r="2" fill="#fff" stroke="#94a3b8"/>' for k in range(8))
CAN = '<path d="M50 70 q60 -30 120 0 l10 50 q-70 30 -140 0z" fill="#dc2626" stroke="#7f1d1d"/><ellipse cx="110" cy="68" rx="62" ry="18" fill="#cbd5e1" stroke="#475569"/><path d="M60 95 l30 10 l20 -15 l25 15 l30 -10" stroke="#7f1d1d" stroke-width="3" fill="none"/>'
FIGS.update({
    'saltdissolve': lambda: panel_row([('Dissolving salt in water', STIR), ('Boil water', BOIL), ('Leftover salt', LEFT)], None, 190),
    'crushedcan': lambda: panel_row([('Crushed aluminium can', CAN)], None, 190),
    'melting': lambda: state_change('solid', 'liquid', 'Absorption|of|heat', 'Change of solid into liquid'),
    'freezing': lambda: state_change('liquid', 'solid', 'Release|of|heat', 'Change of liquid into solid'),
    'boiling': lambda: state_change('liquid', 'gas', 'Absorption|of|heat', 'Change of liquid into gas'),
    'condensation': lambda: state_change('gas', 'liquid', 'Release|of|heat', 'Change of Gas into Liquid'),
})

LAKEMIST = '<rect x="10" y="20" width="200" height="130" fill="#9f1239" opacity=".45"/><path d="M10 70 q30 -30 50 -10 q20 -35 50 -5 q25 -30 50 0 q20 -20 50 5 l0 20 l-200 0z" fill="#3f1d2b"/><rect x="10" y="90" width="200" height="60" fill="#be7fa0"/>' + ''.join(f'<path d="M{20 + k * 25} 120 q8 -15 0 -30 q-8 -15 0 -30" stroke="#fdf2f8" stroke-width="3" fill="none" opacity=".8"/>' for k in range(8))
COLDGLASS = '<path d="M70 35 l80 0 l-10 115 l-60 0z" fill="#e0f2fe" stroke="#64748b" stroke-width="2"/><path d="M76 70 l68 0 l-7 80 l-54 0z" fill="#bae6fd"/>' + ''.join(f'<circle cx="{75 + (k * 13) % 70}" cy="{45 + (k * 17) % 100}" r="2.5" fill="#fff" stroke="#38bdf8"/>' for k in range(22))
PANBOIL = '<rect x="10" y="20" width="200" height="130" fill="#bae6fd"/><path d="M30 80 l130 0 l-10 35 l-110 0z" fill="#6d28d9"/><path d="M160 85 l45 -10" stroke="#111827" stroke-width="8"/><rect x="20" y="120" width="160" height="12" fill="#57534e"/>' + ''.join(f'<path d="M{45 + k * 22} 115 q-4 8 0 14 q4 -6 0 -14z" fill="#f97316"/>' for k in range(6)) + ''.join(f'<path d="M{50 + k * 25} 75 q8 -12 0 -24 q-8 -12 0 -24" stroke="#fff" stroke-width="3" fill="none"/>' for k in range(5))
def _glass(cx, label, stir=False, warm=False):
    s = f'<path d="M{cx - 30} 60 l0 70 q0 6 6 6 l48 0 q6 0 6 -6 l0 -70" fill="{"#fecaca" if warm else "#e0f2fe"}" stroke="#111827" stroke-width="2.5"/><path d="M{cx - 30} 90 l60 0" stroke="#38bdf8"/><text x="{cx - 42}" y="130" font-weight="bold" font-size="14">{label}</text>'
    if stir:
        s += f'<path d="M{cx + 5} 35 l-8 95" stroke="#6b7280" stroke-width="3"/><path d="M{cx} 25 q14 -8 22 4 l-4 14 q-12 4 -18 -4z" fill="#ef4444"/>'
    return s
FIGS.update({
    'pannboil': lambda: panel_row([('(a) Boiling of water', PANBOIL)], None, 190),
    'evaporation': lambda: panel_row([('Evaporation', LAKEMIST)], None, 190),
    'coldglass': lambda: panel_row([('Water drops on a cold glass', COLDGLASS)], None, 190),
    'stirring': lambda: panel_row([('Dissolving sugar in water', '<rect x="10" y="135" width="200" height="15" fill="#b91c1c"/>' + _glass(70, 'A', stir=True) + _glass(160, 'B'))], None, 190),
    'hotcold': lambda: panel_row([('(a) Hot water', _glass(110, '', warm=True) + '<rect x="100" y="35" width="18" height="14" fill="#fff" stroke="#94a3b8"/>'), ('(b) Cold water', _glass(110, '') + '<rect x="100" y="35" width="18" height="14" fill="#fff" stroke="#94a3b8"/>')], 'Effect of temperature on dissolving salt', 190),
})

ROTAPPLE2 = '<circle cx="110" cy="90" r="58" fill="#7f1d1d"/><path d="M110 35 l5 -18" stroke="#57534e" stroke-width="5"/>' + ''.join(f'<circle cx="{80 + (k * 23) % 60}" cy="{70 + (k * 17) % 50}" r="{6 + k % 3 * 3}" fill="#451a03" opacity=".7"/>' for k in range(7))
SKELEAF = '<rect x="10" y="20" width="200" height="130" fill="#1c1917"/><path d="M30 130 q40 -110 160 -95 q-20 110 -160 95z" fill="#78350f" opacity=".6" stroke="#d6d3d1"/><path d="M30 130 q80 -50 160 -95" stroke="#e7e5e4" stroke-width="2" fill="none"/>' + ''.join(f'<path d="M{55 + k * 18} {118 - k * 11} l{-8 + k} -{22 - k}" stroke="#d6d3d1" fill="none"/><path d="M{55 + k * 18} {118 - k * 11} l20 4" stroke="#d6d3d1" fill="none"/>' for k in range(7))
MATCH = '<rect x="10" y="20" width="200" height="130" fill="#111827"/><rect x="106" y="70" width="6" height="80" fill="#fef3c7"/><path d="M109 70 q-12 -18 0 -45 q12 27 0 45z" fill="#f59e0b"/><path d="M109 66 q-5 -10 0 -24 q5 14 0 24z" fill="#fff7ed"/>'
LOCK = '<rect x="10" y="20" width="200" height="130" fill="#a8a29e"/><path d="M75 75 l0 -25 a35 35 0 0 1 70 0 l0 25" stroke="#7c2d12" stroke-width="12" fill="none"/><rect x="55" y="75" width="110" height="70" rx="8" fill="#9a3412"/>' + ''.join(f'<circle cx="{65 + (k * 29) % 95}" cy="{85 + (k * 13) % 55}" r="{3 + k % 3}" fill="#451a03"/>' for k in range(12)) + '<circle cx="110" cy="105" r="7" fill="#1c1917"/><rect x="107" y="105" width="6" height="18" fill="#1c1917"/>'
def _cup(cx, glass, solid):
    s = f'<path d="M{cx - 38} 45 l76 0 l-8 95 l-60 0z" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/><path d="M{cx - 34} 75 l68 0 l-6 65 l-56 0z" fill="#e0f2fe"/><text x="{cx - 34}" y="138" font-size="12">{glass}</text>'
    return s + (f'<rect x="{cx - 9}" y="122" width="18" height="16" fill="#fff" stroke="#94a3b8"/>' if solid == 'cube' else ''.join(f'<circle cx="{cx - 20 + k * 5}" cy="{136 - (k % 2) * 3}" r="2" fill="#fff" stroke="#94a3b8"/>' for k in range(8)) + f'<path d="M{cx + 12} 20 q-10 10 -4 30 l10 0 q6 -20 -6 -30z" fill="#e2e8f0"/>')
DRINKS = '<svg viewBox="0 0 420 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15" font-weight="bold">' + ''.join(f'<path d="M{20 + k * 80} 20 l64 0 l-6 105 q-26 8 -52 0z" fill="{c}" stroke="#111827" stroke-width="3"/><ellipse cx="{52 + k * 80}" cy="20" rx="32" ry="6" fill="#fff" stroke="#111827" stroke-width="3"/><text x="{52 + k * 80}" y="155" text-anchor="middle">{k + 1}</text>' for k, c in enumerate(['#bfe3c0', '#d9c37a', '#e1873f', '#e2493b', '#f0202a'])) + '<rect x="10" y="137" width="400" height="26" fill="none" stroke="#2563eb" stroke-width="2"/></svg>'
def rust_tubes():
    out = ['<svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14" font-weight="bold">']
    for i, (x, fill, oil, lab) in enumerate([(70, 210, False, 'A'), (270, 160, True, 'B'), (470, 0, False, 'C')]):
        out.append(f'<path d="M{x - 30} 10 l60 0 l-6 28 l-48 0z" fill="#a16207"/><path d="M{x - 20} 38 l0 210 a20 20 0 0 0 40 0 l0 -210" fill="#fff" stroke="#111827" stroke-width="2"/>')
        if fill:
            out.append(f'<path d="M{x - 20} {fill} l40 0 l0 {248 - fill} a20 20 0 0 1 -40 0z" fill="#93c5fd" opacity=".7"/>')
        if oil:
            out.append(f'<rect x="{x - 20}" y="{fill - 10}" width="40" height="10" fill="#fde047"/>')
        out.append(f'<path d="M{x - 6} 150 l8 110" stroke="{"#9a3412" if lab == "A" else "#334155"}" stroke-width="6"/><path d="M{x - 12} 150 l14 -2" stroke="#334155" stroke-width="4"/><text x="{x}" y="292" text-anchor="middle" font-size="18">{lab}</text>')
    lab = [(90, 90, 'Air', 70), (90, 220, 'Water', 70), (90, 255, 'Rusted Nail', 70), (290, 150, 'Oil', 270), (290, 225, 'Boiled Water', 270), (490, 120, 'Dry Air', 470)]
    for (x, y, s, tx) in lab:
        out.append(f'<path d="M{x + 30} {y} l-{x + 30 - tx - 8} 0" stroke="#111827"/><path d="M{tx + 8} {y} l8 -4 l0 8z" fill="#111827"/>')
        for j, w in enumerate(s.split(' ') if len(s) > 8 else [s]):
            out.append(f'<text x="{x + 34}" y="{y + 5 + j * 16}">{w}</text>')
    out.append('</svg>')
    return ''.join(out)
FIGS.update({
    'sugarcube': lambda: panel_row([('B: sugar cube', _cup(110, 'B', 'cube')), ('A: sugar grains', _cup(110, 'A', 'grains'))], 'Dissolvent of sugar grains and sugar cube', 190),
    'drinks5': lambda: DRINKS,
    'decaying': lambda: panel_row([('Rotten apple', ROTAPPLE2), ('Decayed leaf', SKELEAF)], 'Decaying', 190),
    'burning': lambda: panel_row([('Burning', MATCH)], None, 190),
    'rusttubes': rust_tubes,
    'rustlock': lambda: panel_row([('Rusted iron lock', LOCK)], None, 190),
})

def _bk(level, foam=False, powder=False):
    s = '<rect x="10" y="20" width="200" height="130" fill="#57534e"/><path d="M75 40 l0 100 q0 6 6 6 l58 0 q6 0 6 -6 l0 -100" fill="#e7e5e4" fill-opacity=".25" stroke="#f5f5f4" stroke-width="2"/>'
    if level:
        s += f'<rect x="77" y="{146 - level}" width="66" height="{level - 2}" fill="#f8fafc"/>'
    if powder:
        s += '<ellipse cx="110" cy="140" rx="25" ry="5" fill="#fff"/>'
    if foam:
        s += ''.join(f'<circle cx="{82 + k * 9}" cy="{38 - (k % 3) * 5}" r="8" fill="#f8fafc"/>' for k in range(7))
    return s
POT = '<rect x="10" y="20" width="200" height="130" fill="#44403c"/><path d="M40 70 l140 0 l-12 50 l-116 0z" fill="#a8a29e"/>' + ''.join(f'<circle cx="{60 + (k * 23) % 100}" cy="{85 + (k * 11) % 30}" r="4" fill="#e7e5e4"/>' for k in range(10)) + ''.join(f'<path d="M{70 + k * 18} 140 q-4 -8 0 -14 q4 6 0 14z" fill="#3b82f6"/>' for k in range(5))
FOAMCUP = '<rect x="10" y="20" width="200" height="130" fill="#0c4a6e"/><path d="M70 70 l80 0 l-10 75 l-60 0z" fill="#e0f2fe"/>' + ''.join(f'<circle cx="{65 + k * 11}" cy="{62 - (k % 3) * 8}" r="14" fill="#f8fafc"/>' for k in range(9))
ICECUBE = '<rect x="10" y="20" width="200" height="130" fill="#0ea5e9"/><ellipse cx="110" cy="125" rx="85" ry="20" fill="#7dd3fc"/><path d="M70 60 l50 -15 l40 20 l0 55 l-45 15 l-45 -20z" fill="#e0f2fe" fill-opacity=".85" stroke="#f0f9ff" stroke-width="2"/><path d="M70 60 l45 20 l45 -15 M115 80 l0 55" stroke="#bae6fd" stroke-width="2" fill="none"/>'
EGG = '<rect x="10" y="20" width="200" height="130" fill="#e7e5e4"/><ellipse cx="110" cy="85" rx="60" ry="48" fill="#fdba74" fill-opacity=".85" stroke="#fb923c"/><ellipse cx="110" cy="85" rx="28" ry="24" fill="#f97316" fill-opacity=".6"/>'
FIGS.update({
    'sodavinegar': lambda: panel_row([('Baking soda', _bk(0, powder=True)), ('Adding vinegar', _bk(35)), ('Bubbles form', _bk(85)), ('Foam overflows', _bk(100, foam=True))], None, 190),
    'boilfoam': lambda: panel_row([('Boiling water', POT), ('Vinegar and baking soda', FOAMCUP)], None, 190),
    'icemelt': lambda: panel_row([('Melting ice', ICECUBE)], None, 190),
    'shellless': lambda: panel_row([('Egg after 12 hours in vinegar', EGG)], None, 190),
})

# --- Chapter 6: Light and Sound ---
def _li(kind):
    bg = {'dark': '<rect x="10" y="20" width="200" height="130" fill="#111827"/>', 'none': ''}
    d = {
        'Candle': bg['dark'] + '<rect x="95" y="85" width="30" height="60" fill="#b91c1c"/><path d="M110 85 q-14 -20 0 -45 q14 25 0 45z" fill="#facc15"/><path d="M110 80 q-6 -10 0 -24 q6 14 0 24z" fill="#fff7ed"/>',
        'Sun': '<rect x="10" y="20" width="200" height="130" fill="#dc2626" opacity=".55"/><circle cx="110" cy="85" r="38" fill="#fde047"/><circle cx="110" cy="85" r="52" fill="#facc15" opacity=".35"/>',
        'Stars': bg['dark'] + ''.join(f'<g transform="translate({30 + (k * 47) % 170},{35 + (k * 31) % 105})"><path d="M0 -9 L2 -2 L9 0 L2 2 L0 9 L-2 2 L-9 0 L-2 -2z" fill="#e0e7ff"/></g>' for k in range(9)),
        'Electric bulb': bg['dark'] + '<circle cx="110" cy="75" r="40" fill="#bfdbfe" opacity=".5"/><path d="M85 75 a25 25 0 1 1 50 0 q0 15 -12 25 l0 15 l-26 0 l0 -15 q-12 -10 -12 -25z" fill="#e0f2fe" stroke="#94a3b8"/><rect x="97" y="115" width="26" height="18" fill="#6b7280"/><path d="M103 95 l4 -18 l6 18 l4 -18" stroke="#f59e0b" stroke-width="2" fill="none"/>',
        'Lightning': '<rect x="10" y="20" width="200" height="130" fill="#7f1d1d"/><path d="M10 120 q50 -20 100 0 t100 0 l0 30 l-200 0z" fill="#1c1917"/><path d="M120 25 l-25 50 l18 0 l-20 55 l40 -65 l-18 0 l20 -40z" fill="#fde68a"/>',
        'Firefly': '<rect x="10" y="20" width="200" height="130" fill="#14532d"/><ellipse cx="115" cy="85" rx="40" ry="16" fill="#44403c" transform="rotate(-25 115 85)"/><circle cx="80" cy="102" r="16" fill="#d9f99d"/><circle cx="80" cy="102" r="28" fill="#bef264" opacity=".35"/><path d="M140 70 l25 -25 M145 75 l30 -15" stroke="#a8a29e" stroke-width="2"/>',
        'Chair': '<path d="M70 40 l0 110 M70 95 l80 0 l0 55 M70 120 l80 0 M70 40 l10 0 l0 55" stroke="#7c2d12" stroke-width="8" fill="none"/><path d="M70 92 l85 0 l0 10 l-85 0z" fill="#451a03"/>',
        'Moon': '<path d="M130 40 a50 50 0 1 0 25 85 a40 40 0 1 1 -25 -85z" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>',
        'Human Body': '<rect x="70" y="25" width="80" height="125" fill="#fff"/><circle cx="110" cy="50" r="16" fill="#fed7aa"/><path d="M98 40 q12 -14 24 0" fill="#ea580c"/><rect x="95" y="66" width="30" height="40" rx="8" fill="#fed7aa"/><rect x="95" y="100" width="30" height="14" fill="#2563eb"/><path d="M100 114 l0 32 M120 114 l0 32 M95 70 l-12 30 M125 70 l12 30" stroke="#fed7aa" stroke-width="8"/>',
        'Book page': '<rect x="65" y="25" width="90" height="125" fill="#f8fafc" stroke="#94a3b8"/>' + ''.join(f'<path d="M75 {40 + k * 10} l70 0" stroke="#cbd5e1"/><circle cx="68" cy="{38 + k * 10}" r="2" fill="#475569"/>' for k in range(11)),
        'Lighted energy saver': '<rect x="10" y="20" width="200" height="130" fill="#16a34a" opacity=".5"/><rect x="102" y="25" width="16" height="30" fill="#111827"/><path d="M90 55 l40 0 l8 30 q-28 40 -56 0z" fill="#f8fafc"/><circle cx="110" cy="95" r="35" fill="#fff" opacity=".4"/>',
        'Oil lamp': '<path d="M60 100 q50 50 100 0z" fill="#b91c1c"/><ellipse cx="110" cy="100" rx="50" ry="10" fill="#7f1d1d"/><path d="M110 98 q-10 -15 0 -38 q10 23 0 38z" fill="#facc15"/>',
        'Torch': '',
    }
    return d[kind]
def _torchscene(target):
    s = '<rect x="10" y="20" width="200" height="130" fill="#f0abfc" opacity=".35"/><path d="M40 105 l150 0 l0 10 l-150 0z" fill="#b91c1c"/><path d="M50 115 l0 35 M180 115 l0 35 M65 115 l0 28 M165 115 l0 28" stroke="#b91c1c" stroke-width="7"/>'
    s += '<rect x="25" y="60" width="35" height="14" fill="#44403c"/><path d="M60 58 l20 -5 l0 28 l-20 -5z" fill="#fde68a"/>'
    if target == 'water':
        s += '<path d="M80 53 l100 -10 l0 45 l-100 -7z" fill="#fde68a" opacity=".7"/><rect x="115" y="55" width="22" height="48" fill="#e0f2fe" fill-opacity=".6" stroke="#64748b"/>'
    elif target == 'milk':
        s += '<path d="M80 53 l45 -3 l0 33 l-45 -2z" fill="#fde68a" opacity=".7"/><path d="M137 55 l30 -2 l0 30 l-30 -2z" fill="#fde68a" opacity=".3"/><rect x="115" y="55" width="22" height="48" fill="#f8fafc" stroke="#94a3b8"/>'
    else:
        s += '<path d="M80 53 l45 -3 l0 33 l-45 -2z" fill="#fde68a" opacity=".7"/><rect x="125" y="40" width="8" height="63" fill="#1d4ed8"/>'
    return s
FIGS.update({
    'lightsrcA': lambda: panel_row([(k, _li(k)) for k in ('Candle', 'Sun', 'Stars')], None, 190),
    'lightsrcB': lambda: panel_row([(k, _li(k)) for k in ('Electric bulb', 'Lightning', 'Firefly')], None, 190),
    'luminous10a': lambda: panel_row([(k, _li(k)) for k in ('Chair', 'Moon', 'Human Body', 'Book page', 'Lighted energy saver')], None, 190),
    'luminous10b': lambda: panel_row([(k, _li(k)) for k in ('Oil lamp', 'Candle', 'Firefly', 'Stars', 'Sun')], None, 190),
    'torch3': lambda: panel_row([('1. Glass of water', _torchscene('water')), ('2. Glass of milk', _torchscene('milk')), ('3. Cardboard', _torchscene('card'))], None, 190),
})

_OBJ = {
    'Glasses': '<g fill="none" stroke="#111827" stroke-width="8"><rect x="35" y="60" width="62" height="45" rx="12"/><rect x="123" y="60" width="62" height="45" rx="12"/><path d="M97 72 q13 -10 26 0 M35 70 l-15 -8 M185 70 l15 -8"/></g>',
    'Door': '<rect x="80" y="25" width="60" height="125" fill="#7f1d1d"/><circle cx="130" cy="90" r="4" fill="#fde68a"/>',
    'Window pane': '<rect x="60" y="25" width="100" height="120" fill="#7f1d1d"/><rect x="68" y="33" width="84" height="104" fill="#f8fafc"/><path d="M110 33 l0 104 M68 70 l84 0 M68 105 l84 0" stroke="#a8a29e" stroke-width="3"/><circle cx="110" cy="85" r="12" fill="#4d7c0f" opacity=".6"/>',
    'Net curtain': ''.join(f'<rect x="{25 + k * 17}" y="25" width="12" height="125" fill="#818cf8" opacity=".55"/>' for k in range(10)),
    'Magnifying glass': '<circle cx="100" cy="80" r="45" fill="#f8fafc" stroke="#111827" stroke-width="7"/><path d="M132 112 l35 35" stroke="#7f1d1d" stroke-width="12"/>',
    'Brick wall': '<rect x="15" y="25" width="190" height="125" fill="#b91c1c"/>' + ''.join(f'<path d="M15 {40 + r * 16} l190 0" stroke="#fecaca" stroke-width="2"/>' for r in range(7)) + ''.join(f'<path d="M{15 + c * 38 + (r % 2) * 19} {25 + r * 16} l0 16" stroke="#fecaca" stroke-width="2"/>' for r in range(8) for c in range(5)),
    'Tissue paper': '<rect x="10" y="20" width="200" height="130" fill="#7f1d1d"/>' + ''.join(f'<path d="M{30 + k * 8} {110 - k * 10} l120 -25 l25 35 l-120 25z" fill="#f8fafc" opacity=".85" stroke="#d6d3d1"/>' for k in range(3)),
    'Soft drink': '<rect x="10" y="20" width="200" height="130" fill="#b91c1c"/><path d="M55 50 l110 0 l-15 95 l-80 0z" fill="#3b82f6"/><ellipse cx="110" cy="50" rx="55" ry="15" fill="#818cf8"/>',
    'Packing tape': '<circle cx="110" cy="85" r="50" fill="#c4a484" opacity=".8"/><circle cx="110" cy="85" r="28" fill="#fff"/>',
    'Plastic sheet': '<path d="M25 110 l150 -60 l25 40 l-150 60z" fill="#bfdbfe" opacity=".6" stroke="#94a3b8"/><ellipse cx="45" cy="95" rx="18" ry="30" fill="#93c5fd" opacity=".5"/>',
    'Ironsheet': ''.join(f'<path d="M{30 + k * 16} 130 l60 -90" stroke="#94a3b8" stroke-width="9"/>' for k in range(8)),
    'Plastic bottle': '<rect x="102" y="22" width="16" height="14" fill="#94a3b8"/><path d="M102 36 q-20 15 -20 35 l0 70 q0 8 8 8 l40 0 q8 0 8 -8 l0 -70 q0 -20 -20 -35z" fill="#e2e8f0" stroke="#64748b"/>' + ''.join(f'<path d="M84 {90 + k * 12} l52 0" stroke="#94a3b8"/>' for k in range(4)),
}
CARDHOLES = ('<svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg"><path d="M60 200 l540 0 l20 30 l-540 0z" fill="#c2725a" stroke="#7f1d1d"/>'
    + ''.join(f'<path d="M{170 + k * 150} 50 l70 -10 l0 160 l-70 10z" fill="#c2725a" stroke="#7f1d1d" stroke-width="2"/><circle cx="{190 + k * 150}" cy="100" r="8" fill="#fff" stroke="#111827" stroke-width="2"/>' for k in range(3))
    + '<path d="M50 100 l500 0" stroke="#111827" stroke-width="2" stroke-dasharray="10 8"/>'
    + '<path d="M30 85 q20 15 0 30 q-8 -15 0 -30z" fill="#ef4444"/><ellipse cx="38" cy="100" rx="8" ry="5" fill="#fff" stroke="#111827"/><circle cx="40" cy="100" r="3" fill="#111827"/>'
    + '<circle cx="570" cy="105" r="50" fill="#fde047" opacity=".35"/><rect x="558" y="110" width="24" height="90" rx="4" fill="#f472b6"/><path d="M570 108 q-12 -18 0 -38 q12 20 0 38z" fill="#f59e0b"/></svg>')
def _shadow(dist, size):
    return (f'<rect x="10" y="20" width="200" height="130" fill="#ecfccb"/><rect x="180" y="20" width="30" height="130" fill="#d6d3d1"/>'
            f'<path d="M180 {85 - size} q-15 {size} 0 {size * 2} l0 -{size * 2}z" fill="#111827" opacity=".7"/>'
            f'<path d="M30 110 l90 0 l0 8 l-90 0z M35 118 l0 30 M115 118 l0 30" fill="#dc2626" stroke="#dc2626" stroke-width="6"/><rect x="66" y="88" width="8" height="22" fill="#fda4af"/><path d="M70 88 q-6 -10 0 -18 q6 8 0 18z" fill="#f59e0b"/>'
            f'<path d="M{80 + dist} 72 l22 0 l4 -6 l4 6 l3 -6 l3 6 l0 12 l-36 0z" fill="#57534e"/>')
FIGS.update({
    'tto12a': lambda: panel_row([(k, _OBJ[k]) for k in ('Glasses', 'Door', 'Window pane')], None, 190),
    'tto12b': lambda: panel_row([(k, _OBJ[k]) for k in ('Net curtain', 'Magnifying glass', 'Brick wall')], None, 190),
    'tto12c': lambda: panel_row([(k, _OBJ[k]) for k in ('Tissue paper', 'Soft drink', 'Packing tape')], None, 190),
    'tto12d': lambda: panel_row([(k, _OBJ[k]) for k in ('Plastic sheet', 'Ironsheet', 'Plastic bottle')], None, 190),
    'cardholes': lambda: CARDHOLES,
    'shadows3': lambda: panel_row([('Hand midway', _shadow(40, 18)), ('Hand near the candle', _shadow(10, 34)), ('Hand far from the candle', _shadow(70, 10))], None, 190),
})

def _reflect(shiny):
    s = '<rect x="10" y="20" width="200" height="130" fill="#292524"/><path d="M25 125 l12 -6 l70 -35 l4 8 l-70 35z" fill="#fca5a5"/><path d="M40 120 l130 -55 l6 18z" fill="#fde047" opacity=".75"/>'
    s += '<rect x="170" y="55" width="10" height="40" fill="#e2e8f0"/>' if shiny else '<rect x="170" y="55" width="10" height="40" fill="#78716c"/>'
    s += '<path d="M172 65 l-110 -35 l-6 18z" fill="#fef9c3" opacity=".75"/>' if shiny else '<path d="M172 65 l-70 -20 l-4 12z" fill="#fef9c3" opacity=".15"/>'
    return s
SPEAKER = lambda moving: ('<rect x="10" y="20" width="200" height="130" fill="#1c1917"/>' + ''.join(f'<circle cx="110" cy="85" r="{r}" fill="none" stroke="#57534e" stroke-width="2"/>' for r in (60, 45, 30))
    + (''.join(f'<circle cx="{110 + (k * 37) % 70 - 35}" cy="{85 + (k * 23) % 60 - 30}" r="3" fill="#f87171"/>' for k in range(30)) if moving else '<circle cx="110" cy="85" r="22" fill="none" stroke="#f87171" stroke-width="9"/>'))
GUITAR = '<ellipse cx="80" cy="115" rx="40" ry="28" fill="#c2410c" transform="rotate(-35 80 115)"/><circle cx="85" cy="110" r="8" fill="#111827"/><path d="M95 100 l90 -75" stroke="#111827" stroke-width="9"/><path d="M80 120 l95 -85" stroke="#f5f5f4"/>'
DRUM = '<rect x="60" y="55" width="100" height="75" fill="#16a34a"/><ellipse cx="110" cy="55" rx="50" ry="14" fill="#dc2626"/><ellipse cx="110" cy="130" rx="50" ry="12" fill="#dc2626"/>' + ''.join(f'<path d="M{62 + k * 25} 63 l12 60 l12 -60z" fill="{["#facc15", "#1d4ed8"][k % 2]}"/>' for k in range(4))
FLUTE = '<path d="M30 120 l160 -70" stroke="#c2410c" stroke-width="11"/><path d="M150 68 l40 -18" stroke="#111827" stroke-width="11"/>' + ''.join(f'<circle cx="{60 + k * 20}" cy="{107 - k * 8.7:.0f}" r="3" fill="#111827"/>' for k in range(5))
EARTABLE = '<rect x="10" y="20" width="200" height="130" fill="#57534e"/><rect x="20" y="85" width="180" height="60" fill="#1c1917"/><path d="M20 85 l180 0" stroke="#a8a29e" stroke-width="3"/><circle cx="45" cy="72" r="14" fill="#fed7aa"/><path d="M33 70 q12 -18 26 -4" fill="#111827"/><path d="M180 80 l-10 6 m6 -10 l-10 6" stroke="#fed7aa" stroke-width="4"/>' + ''.join(f'<path d="M{150 - k * 25} 92 q-6 6 0 12" stroke="#fde047" fill="none" stroke-width="2"/>' for k in range(4))
TUB = '<rect x="10" y="20" width="200" height="130" fill="#78716c"/><path d="M45 95 l130 0 l-12 50 l-106 0z" fill="#e7e5e4"/><ellipse cx="110" cy="95" rx="65" ry="12" fill="#86efac"/><circle cx="70" cy="60" r="16" fill="#fed7aa"/><circle cx="160" cy="75" r="14" fill="#fed7aa"/><path d="M150 85 l-20 10 l-5 -5" stroke="#16a34a" stroke-width="6" fill="none"/><path d="M80 85 l20 15 M95 88 l15 14" stroke="#94a3b8" stroke-width="3"/>'
FIGS.update({
    'reflect2': lambda: panel_row([('Shining steel plate (mirror)', _reflect(True)), ('Dull cardboard', _reflect(False))], None, 190),
    'speaker': lambda: panel_row([('Grains on a speaker cone', SPEAKER(False)), ('Grains vibrating when sound plays', SPEAKER(True))], None, 190),
    'instruments': lambda: panel_row([('Guitar', GUITAR), ('Drum', DRUM), ('Flute', FLUTE)], None, 190),
    'eartable': lambda: panel_row([('Ear on the table', EARTABLE)], None, 190),
    'tub': lambda: panel_row([('Listening to spoons struck in water', TUB)], None, 190),
})

FENCE = ('<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg"><rect width="520" height="200" fill="#fff"/><path d="M60 40 l440 0 M60 150 l440 0" stroke="#111827" stroke-width="5"/>'
    + ''.join(f'<path d="M{70 + k * 14} 30 l0 125" stroke="#111827" stroke-width="5"/>' for k in range(31))
    + '<g fill="none" stroke="#57534e" stroke-width="4"><circle cx="35" cy="55" r="12"/><path d="M35 67 l0 70 M35 137 l-12 45 M35 137 l12 45 M35 85 l40 25"/></g><path d="M75 110 l12 8" stroke="#94a3b8" stroke-width="4"/>'
    + '<g fill="none" stroke="#57534e" stroke-width="4"><circle cx="490" cy="58" r="12"/><path d="M490 70 l0 70 M490 140 l-12 45 M490 140 l12 45"/></g><circle cx="482" cy="58" r="4" fill="#fed7aa"/></svg>')
def _snd(kind):
    d = {
        'Bird chirping': '<rect x="10" y="20" width="200" height="130" fill="#fb7185" opacity=".55"/><path d="M60 140 l120 -60" stroke="#57534e" stroke-width="5"/><ellipse cx="110" cy="85" rx="35" ry="20" fill="#a8a29e"/><circle cx="140" cy="68" r="13" fill="#78716c"/><path d="M152 66 l12 2 l-12 4z" fill="#f59e0b"/>',
        'Lion roaring': '<rect x="10" y="20" width="200" height="130" fill="#7c2d12" opacity=".6"/><circle cx="110" cy="85" r="55" fill="#b45309"/><circle cx="110" cy="85" r="36" fill="#f59e0b"/><path d="M95 95 q15 25 30 0z" fill="#7f1d1d"/><circle cx="96" cy="75" r="4" fill="#111827"/><circle cx="124" cy="75" r="4" fill="#111827"/>',
        'Jet plane': '<rect x="10" y="20" width="200" height="130" fill="#818cf8" opacity=".5"/><path d="M30 95 l140 -20 l25 8 l-25 8z" fill="#374151"/><path d="M90 88 l-30 -45 l20 0 l40 40z M90 92 l-30 45 l20 0 l40 -40z" fill="#374151"/>',
        'Playing flute': '<rect x="10" y="20" width="200" height="130" fill="#fecaca"/><circle cx="130" cy="55" r="20" fill="#fed7aa"/><path d="M110 50 q20 -25 40 -5" fill="#57534e"/><rect x="110" y="75" width="50" height="70" fill="#64748b"/><path d="M118 70 l-60 40" stroke="#a16207" stroke-width="7"/>',
        'Cat hissing': '<rect x="10" y="20" width="200" height="130" fill="#991b1b" opacity=".6"/><ellipse cx="110" cy="115" rx="55" ry="30" fill="#d6d3d1"/><circle cx="110" cy="70" r="30" fill="#e7e5e4"/><path d="M85 48 l-5 -20 l18 12z M135 48 l5 -20 l-18 12z" fill="#e7e5e4"/><path d="M98 82 q12 14 24 0z" fill="#7f1d1d"/>',
        'Thunder': '<rect x="10" y="20" width="200" height="130" fill="#581c87"/><path d="M120 22 l-25 55 l18 0 l-22 70 l42 -80 l-18 0 l22 -45z" fill="#f5f3ff"/>',
        'Tractor': '<rect x="10" y="20" width="200" height="130" fill="#fdba74"/><circle cx="150" cy="70" r="40" fill="#ef4444"/><rect x="40" y="75" width="80" height="35" fill="#4f46e5"/><rect x="75" y="55" width="35" height="25" fill="#6366f1"/><circle cx="60" cy="118" r="18" fill="#111827"/><circle cx="110" cy="122" r="12" fill="#111827"/>',
        'Donkey braying': '<rect x="10" y="20" width="200" height="130" fill="#1c1917"/><path d="M70 140 q10 -60 40 -70 l30 50 q-30 20 -70 20z" fill="#57534e"/><path d="M110 70 l-8 -40 l12 30 l10 -32 l-4 42z" fill="#78716c"/>',
        'Dog barking': '<rect x="10" y="20" width="200" height="130" fill="#fef3c7"/><path d="M60 140 q-10 -60 30 -80 l40 -10 l30 25 l-25 15 l-30 -5 q-5 40 -15 55z" fill="#78350f"/><path d="M125 70 l-10 -25 l18 18z" fill="#78350f"/><path d="M160 75 l-25 10 l25 5" fill="#7f1d1d"/>',
        'Bird singing': '<rect x="10" y="20" width="200" height="130" fill="#57534e"/><path d="M40 130 l140 -10" stroke="#1c1917" stroke-width="6"/><ellipse cx="100" cy="100" rx="35" ry="20" fill="#78350f"/><circle cx="130" cy="78" r="13" fill="#9a3412"/><path d="M140 72 l14 -8 l-10 14z" fill="#facc15"/>',
        'Traffic jam': '<rect x="10" y="20" width="200" height="130" fill="#292524"/>' + ''.join(f'<rect x="{20 + c * 47}" y="{30 + r * 28}" width="38" height="20" rx="5" fill="#d6d3d1"/>' for c in range(4) for r in range(4)),
        'Harmonium': '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M30 70 l140 -20 l20 40 l-140 25z" fill="#9a3412"/><path d="M50 95 l140 -25 l0 30 l-140 25z" fill="#7c2d12"/>' + ''.join(f'<rect x="{60 + k * 10}" y="{88 - k * 1.8:.0f}" width="7" height="14" fill="#f8fafc" stroke="#111827" stroke-width=".5"/>' for k in range(11)),
    }
    return d[kind]
FIGS.update({
    'fence': lambda: FENCE,
    'intensityA': lambda: panel_row([(k, _snd(k)) for k in ('Bird chirping', 'Lion roaring', 'Jet plane')], None, 190),
    'intensityB': lambda: panel_row([(k, _snd(k)) for k in ('Playing flute', 'Cat hissing', 'Thunder')], None, 190),
    'pleasantA': lambda: panel_row([(k, _snd(k)) for k in ('Tractor', 'Donkey braying', 'Dog barking')], None, 190),
    'pleasantB': lambda: panel_row([(k, _snd(k)) for k in ('Bird singing', 'Traffic jam', 'Harmonium')], None, 190),
})

NOHORN = lambda x, y: f'<circle cx="{x}" cy="{y}" r="12" fill="#fff" stroke="#dc2626" stroke-width="4"/><path d="M{x - 6} {y + 2} l8 -6 l0 10z" fill="#111827"/><path d="M{x - 9} {y + 9} l18 -18" stroke="#dc2626" stroke-width="3"/>'
SCHOOLZONE = ('<rect x="10" y="20" width="200" height="130" fill="#e0f2fe"/><rect x="50" y="40" width="120" height="70" fill="#dc2626"/><rect x="85" y="28" width="50" height="14" fill="#b91c1c"/><text x="110" y="39" text-anchor="middle" font-size="10" fill="#fff">SCHOOL</text>'
    + ''.join(f'<rect x="{58 + (k % 6) * 18}" y="{50 + (k // 6) * 18}" width="10" height="10" fill="#fde68a"/>' for k in range(18))
    + '<rect x="10" y="115" width="200" height="35" fill="#334155"/><rect x="25" y="100" width="70" height="30" rx="6" fill="#f59e0b"/><circle cx="40" cy="132" r="7" fill="#111827"/><circle cx="80" cy="132" r="7" fill="#111827"/>' + NOHORN(30, 85))
HOSPZONE = ('<rect x="10" y="20" width="200" height="130" fill="#bae6fd"/><path d="M110 150 l-30 -80 l60 0 l30 80z" fill="#a78bfa"/><rect x="95" y="55" width="70" height="18" fill="#fff" stroke="#b91c1c"/><text x="130" y="68" text-anchor="middle" font-size="11" fill="#b91c1c">HOSPITAL</text>'
    + '<path d="M50 150 l0 -95" stroke="#111827" stroke-width="3"/>' + NOHORN(50, 55) + '<circle cx="50" cy="85" r="11" fill="#2563eb" stroke="#dc2626" stroke-width="3"/><path d="M42 77 l16 16 M58 77 l-16 16" stroke="#dc2626" stroke-width="3"/>')
FIGS.update({
    'traffic': lambda: panel_row([('Traffic noise in a city', _snd('Traffic jam'))], None, 190),
    'quietzones': lambda: panel_row([('No horn near a school', SCHOOLZONE), ('No horn near a hospital', HOSPZONE)], None, 190),
})

HARE = '<rect x="10" y="20" width="200" height="130" fill="#4d7c0f"/><ellipse cx="110" cy="115" rx="50" ry="28" fill="#78716c"/><circle cx="125" cy="85" r="22" fill="#a8a29e"/><path d="M115 68 l-10 -45 l12 0 l6 45z M132 68 l8 -45 l12 2 l-10 45z" fill="#a8a29e"/><circle cx="132" cy="82" r="3" fill="#111827"/>'
PARROTS = '<rect x="10" y="20" width="200" height="130" fill="#14532d"/><path d="M30 120 l160 -5" stroke="#78350f" stroke-width="6"/>' + ''.join(f'<ellipse cx="{75 + k * 70}" cy="85" rx="20" ry="32" fill="{["#dc2626", "#2563eb"][k]}"/><circle cx="{75 + k * 70}" cy="55" r="12" fill="#facc15"/><path d="M{82 + k * 70} 55 l8 4 l-8 4z" fill="#111827"/>' for k in range(2))
GUITARIST = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><circle cx="90" cy="50" r="16" fill="#92400e"/><rect x="70" y="66" width="45" height="65" fill="#1e40af"/><ellipse cx="115" cy="110" rx="30" ry="20" fill="#c2410c" transform="rotate(-20 115 110)"/><path d="M130 100 l60 -30" stroke="#78350f" stroke-width="7"/>'
SINGER = '<rect x="10" y="20" width="200" height="130" fill="#1e3a8a"/><path d="M80 150 q-10 -60 30 -90 q40 30 30 90z" fill="#15803d"/><circle cx="110" cy="65" r="18" fill="#fed7aa"/><path d="M90 60 q20 -35 40 0" fill="#15803d"/><rect x="105" y="80" width="8" height="20" fill="#111827"/>'
PHORN = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M40 70 l30 0 l40 20 l0 20 l-40 -20 l-30 0z M60 100 l30 0 l60 25 l0 25 l-60 -25 l-30 0z" fill="#dc2626"/><path d="M40 70 l20 30" stroke="#111827" stroke-width="5"/>'
FIGS.update({
    'hare': lambda: panel_row([('Hare with raised ears', HARE)], None, 190),
    'lightningq': lambda: panel_row([('Lightning', _snd('Thunder'))], None, 190),
    'pleasant2A': lambda: panel_row([('Parrots', PARROTS), ('Thunder and lightning', _snd('Thunder')), ('Playing guitar', GUITARIST)], None, 190),
    'pleasant2B': lambda: panel_row([('Singing', SINGER), ('Pressure horn', PHORN)], None, 190),
})

# --- Chapter 7: Electricity and Magnetism ---
HAIRUP = '<rect x="10" y="20" width="200" height="130" fill="#86efac" opacity=".6"/><circle cx="110" cy="95" r="28" fill="#fed7aa"/><path d="M80 90 q0 -40 30 -42 q30 2 30 42" fill="#292524"/>' + ''.join(f'<path d="M{85 + k * 7} 55 q{(k - 4) * 3} -18 {(k - 4) * 5} -32" stroke="#292524" stroke-width="2" fill="none"/>' for k in range(9)) + '<rect x="82" y="123" width="56" height="27" fill="#3b82f6"/>'
COMBHAIR = '<rect x="10" y="20" width="200" height="130" fill="#bbf7d0"/><path d="M60 140 q0 -60 60 -65 q50 5 55 65z" fill="#fca5a5"/><path d="M60 100 q20 -45 75 -40 q30 5 40 40" fill="#b91c1c"/><rect x="110" y="40" width="70" height="16" rx="3" fill="#dc2626" transform="rotate(25 145 48)"/>' + ''.join(f'<path d="M{118 + k * 7} {52 + k * 3} l-4 12" stroke="#7f1d1d" stroke-width="2"/>' for k in range(8))
COMBPAPER = '<rect x="10" y="20" width="200" height="130" fill="#bbf7d0"/><rect x="70" y="50" width="90" height="18" rx="3" fill="#dc2626" transform="rotate(-25 115 59)"/><path d="M30 140 l120 -12 l25 10 l-120 12z" fill="#f8fafc" stroke="#94a3b8"/>' + ''.join(f'<rect x="{100 + k * 9}" y="{80 + (k % 3) * 12}" width="6" height="5" fill="#f8fafc" stroke="#64748b" transform="rotate({k * 25} {103 + k * 9} {82 + (k % 3) * 12})"/>' for k in range(6))
def _balloon(touch):
    return ('<rect x="10" y="20" width="200" height="130" fill="#fef9c3"/><path d="M160 145 l0 -110 l-40 0" stroke="#57534e" stroke-width="4" fill="none"/><rect x="130" y="140" width="60" height="6" fill="#57534e"/>'
            + (f'<path d="M120 35 l-25 60" stroke="#57534e"/><circle cx="95" cy="105" r="16" fill="#ef4444"/>' if touch else '<path d="M120 35 l0 60" stroke="#57534e"/><circle cx="120" cy="105" r="16" fill="#ef4444"/>')
            + '<circle cx="45" cy="60" r="16" fill="#fed7aa"/><path d="M30 55 q15 -22 30 0" fill="#57534e"/><rect x="30" y="76" width="34" height="50" fill="#78350f"/><rect x="' + ('62' if touch else '45') + '" y="90" width="26" height="30" rx="4" fill="#4338ca"/>')
FIGS.update({
    'hairup': lambda: panel_row([('Static electricity in hair', HAIRUP)], None, 190),
    'comb2': lambda: panel_row([('Combing dry hair', COMBHAIR), ('Comb attracting paper bits', COMBPAPER)], None, 190),
    'balloon2': lambda: panel_row([('Before rubbing', _balloon(False)), ('After rubbing: cloth attracts balloon', _balloon(True))], None, 190),
    'lightningcloud': lambda: panel_row([('Lightning between clouds', _snd('Thunder'))], None, 190),
})

def _twoballoons(gap, lean):
    s = '<rect x="10" y="20" width="200" height="130" fill="#fecaca" opacity=".5"/>'
    for i, x in enumerate((55, 165)):
        d = -1 if i == 0 else 1
        s += f'<path d="M{x} 145 l0 -110 l{-d * 15} 0" stroke="#9f1239" stroke-width="5" fill="none"/><rect x="{x - 25}" y="140" width="50" height="8" fill="#9f1239"/>'
        bx = x - d * 15 + (-d * lean)
        s += f'<path d="M{x - d * 15} 35 L{bx} 95" stroke="#57534e"/><ellipse cx="{bx}" cy="105" rx="16" ry="19" fill="#be123c"/>'
    return s
TOYCAR = '<rect x="10" y="20" width="200" height="130" fill="#d6d3d1"/><path d="M50 60 l110 10 l-10 60 l-110 -10z" fill="#facc15"/>' + ''.join(f'<rect x="{x}" y="{y}" width="20" height="26" rx="4" fill="#111827"/>' for x, y in ((35, 50), (150, 58), (30, 108), (145, 118))) + '<rect x="100" y="70" width="18" height="40" fill="#e5e7eb" stroke="#b91c1c"/><rect x="122" y="72" width="18" height="40" fill="#e5e7eb" stroke="#b91c1c"/><path d="M70 85 q20 -15 30 0" stroke="#111827" fill="none"/>'
CELL = ('<svg viewBox="0 0 420 150" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15" font-weight="bold">'
    '<rect x="120" y="35" width="230" height="70" rx="30" fill="#111827"/><path d="M150 35 l100 0 l0 70 l-100 0 q-30 0 -30 -35 q0 -35 30 -35z" fill="#f59e0b"/>'
    '<ellipse cx="128" cy="70" rx="12" ry="30" fill="#fde68a" stroke="#a16207"/><circle cx="128" cy="70" r="6" fill="#d4d4d8"/>'
    '<text x="200" y="78" font-size="26" fill="#111827" text-anchor="middle">+</text><text x="320" y="78" font-size="26" fill="#f8fafc" text-anchor="middle">&#8722;</text>'
    '<text x="40" y="75" fill="#1d4ed8">Positive</text><text x="200" y="135" fill="#1d4ed8" text-anchor="middle">Cell</text><text x="330" y="135" fill="#1d4ed8" text-anchor="middle">Negative</text></svg>')
def circuit(closed=True, labels=False, title=None):
    s = [f'<svg viewBox="0 0 360 {250 if title else 230}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15" font-weight="bold">']
    s.append('<path d="M180 70 q140 0 140 70 q0 50 -60 55" stroke="#111827" stroke-width="3" fill="none"/><path d="M180 70 q-140 0 -120 90 l25 15" stroke="#dc2626" stroke-width="3" fill="none"/>')
    if closed:
        s.append('<g stroke="#f59e0b" stroke-width="3">' + ''.join(f'<path d="M{180 + 34 * __import__("math").cos(a / 10)} {38 + 34 * __import__("math").sin(a / 10)} l{8 * __import__("math").cos(a / 10)} {8 * __import__("math").sin(a / 10)}"/>' for a in range(-30, 2, 5)) + '</g><circle cx="180" cy="40" r="24" fill="#fef08a" stroke="#a16207"/>')
    else:
        s.append('<circle cx="180" cy="40" r="24" fill="#fff" stroke="#57534e"/>')
    s.append('<path d="M160 60 l40 0 l-6 18 l-28 0z" fill="#fb7185" stroke="#9f1239"/>')
    s.append('<rect x="70" y="170" width="60" height="22" fill="#dc2626"/><rect x="75" y="158" width="10" height="14" fill="#fde68a"/><rect x="115" y="158" width="10" height="14" fill="#fde68a"/>')
    s.append('<path d="M80 160 l42 0" stroke="#a16207" stroke-width="7"/>' if closed else '<path d="M80 160 l35 -30" stroke="#a16207" stroke-width="7"/>')
    s.append('<rect x="200" y="180" width="110" height="26" rx="4" fill="#9a3412"/><rect x="205" y="183" width="48" height="20" rx="8" fill="#292524"/><rect x="256" y="183" width="48" height="20" rx="8" fill="#292524"/><path d="M130 180 l70 10" stroke="#111827" stroke-width="3"/>')
    if labels:
        s.append('<text x="220" y="35" fill="#1d4ed8">Bulb</text><text x="70" y="220" fill="#1d4ed8">Swith</text><text x="240" y="225" fill="#1d4ed8">Battery</text>')
    if title:
        s.append(f'<text x="180" y="240" text-anchor="middle" fill="#1d4ed8">{title}</text>')
    s.append('</svg>')
    return ''.join(s)
BATTERY = '<rect x="10" y="20" width="200" height="130" fill="#fef3c7"/><rect x="30" y="70" width="160" height="40" rx="6" fill="#9a3412"/><rect x="38" y="74" width="68" height="32" rx="12" fill="#292524"/><rect x="114" y="74" width="68" height="32" rx="12" fill="#292524"/>'
FIGS.update({
    'balloons3': lambda: panel_row([('1. Balloons not rubbed', _twoballoons(0, 0)), ('2. Both rubbed with wool: repel', _twoballoons(0, 12)), ('3. Rubbed with wool and plastic: attract', _twoballoons(0, -14))], None, 190),
    'toycar': lambda: panel_row([('Battery-powered toy car', TOYCAR)], None, 190),
    'cell': lambda: CELL,
    'circuitlab': lambda: circuit(True, True),
    'battery2': lambda: panel_row([('Battery of two cells', BATTERY)], None, 190),
    'closedcircuit': lambda: circuit(True, False, 'Closed Circuit'),
    'opencircuit': lambda: circuit(False, False, 'Open Circuit'),
})

def circuit_gap(label):
    s = circuit(True, False)
    gap = (f'<rect x="58" y="88" width="34" height="12" fill="#e7e5e4" stroke="#57534e" transform="rotate(-35 75 94)"/>' if label == 'Material'
           else '<path d="M60 100 q8 -12 16 -4 q8 8 16 -4" stroke="#94a3b8" stroke-width="2" fill="none"/>')
    return s.replace('</svg>', gap + f'<circle cx="62" cy="104" r="4" fill="#111827"/><circle cx="92" cy="84" r="4" fill="#111827"/><text x="20" y="75" fill="#1d4ed8" font-size="15" font-weight="bold">{label}</text></svg>')
WASHER = '<rect x="60" y="30" width="100" height="115" rx="8" fill="#cbd5e1"/><rect x="60" y="30" width="100" height="22" fill="#7f1d1d"/><rect x="60" y="110" width="100" height="35" fill="#7f1d1d"/>' + ''.join(f'<circle cx="{75 + k * 15}" cy="41" r="4" fill="#f8fafc"/>' for k in range(5))
KETTLE = '<path d="M75 60 l70 0 l10 75 l-90 0z" fill="#d6d3d1" stroke="#57534e" stroke-width="2"/><path d="M145 70 q30 5 25 45 l-15 0" stroke="#292524" stroke-width="9" fill="none"/><path d="M75 75 l-25 -20" stroke="#57534e" stroke-width="8"/><rect x="65" y="135" width="100" height="10" fill="#292524"/>'
IRONB = '<path d="M40 120 q20 -50 130 -40 l10 40z" fill="#e2e8f0" stroke="#64748b"/><path d="M90 80 q30 -30 70 -10 l-10 15 q-30 -12 -50 5z" fill="#34d399"/>'
FAN = '<circle cx="110" cy="65" r="40" fill="#e5e7eb" stroke="#111827" stroke-width="4"/>' + ''.join(f'<path d="M110 65 l{30 * __import__("math").cos(k)} {30 * __import__("math").sin(k)}" stroke="#374151" stroke-width="10"/>' for k in (0, 2.1, 4.2)) + '<path d="M110 105 l0 35 M80 145 l60 0" stroke="#e5e7eb" stroke-width="8"/>'
FUSEPAIR = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M40 40 l40 0 l10 30 l-10 30 l-40 0 q-15 -30 0 -60z" fill="#d6d3d1" stroke="#78716c"/><rect x="40" y="45" width="15" height="10" fill="#a16207"/><rect x="40" y="85" width="15" height="10" fill="#a16207"/><rect x="120" y="35" width="70" height="105" rx="6" fill="#e7e5e4" stroke="#78716c"/><rect x="140" y="45" width="30" height="16" fill="#a16207"/><rect x="140" y="115" width="30" height="16" fill="#a16207"/><path d="M155 61 l0 54" stroke="#b91c1c" stroke-width="2"/>'
BREAKERS = '<rect x="10" y="20" width="200" height="130" fill="#fef9c3"/>' + ''.join(f'<rect x="{25 + k * 32}" y="40" width="28" height="100" rx="3" fill="#e5e7eb" stroke="#64748b"/><rect x="{32 + k * 32}" y="85" width="14" height="22" fill="#111827"/>' for k in range(3)) + '<rect x="130" y="50" width="60" height="16" rx="4" fill="#d6d3d1" stroke="#a16207" stroke-width="3"/><path d="M150 100 l35 0 l-8 18 l-20 0z" fill="#dc2626"/><path d="M130 130 l40 -20" stroke="#111827" stroke-width="7"/>'
FIGS.update({
    'materialcircuit': lambda: circuit_gap('Material'),
    'fusecircuit': lambda: circuit_gap('Fuse'),
    'appliances': lambda: panel_row([('Washing machine', WASHER), ('Electric kettle', KETTLE), ('Electric iron', IRONB), ('Electric fan', FAN)], None, 190),
    'fuses': lambda: panel_row([('Fuse', FUSEPAIR)], None, 190),
    'breakers': lambda: panel_row([('Circuit breakers and fuses', BREAKERS)], None, 190),
})

BARMAG = lambda x, y, w=80, rot=0: (f'<g transform="rotate({rot} {x + w / 2} {y + 10})"><rect x="{x}" y="{y}" width="{w / 2}" height="20" fill="#dc2626"/><rect x="{x + w / 2}" y="{y}" width="{w / 2}" height="20" fill="#2563eb"/>'
    f'<text x="{x + 8}" y="{y + 15}" font-size="13" font-weight="bold" fill="#fff">N</text><text x="{x + w - 16}" y="{y + 15}" font-size="13" font-weight="bold" fill="#fff">S</text></g>')
MAGOBJ = ('<rect x="10" y="20" width="200" height="130" fill="#4d7c0f" opacity=".6"/>' + BARMAG(25, 35, 70, 30)
    + '<path d="M120 40 l0 30 M128 42 l2 30 M136 40 l-2 28" stroke="#374151" stroke-width="2"/><path d="M40 90 q20 -20 40 0 q10 15 -20 20" stroke="#292524" stroke-width="4" fill="none"/>'
    + '<rect x="40" y="125" width="60" height="9" rx="4" fill="#ea580c"/><ellipse cx="135" cy="125" rx="16" ry="12" fill="#a8a29e"/><path d="M165 110 l30 20 M170 125 l25 -10" stroke="#111827" stroke-width="2"/>')
LODESTONE = '<rect x="10" y="20" width="200" height="130" fill="#7dd3fc"/><path d="M60 110 q-10 -50 40 -60 q50 -5 60 40 q-20 40 -100 20z" fill="#44403c"/>' + ''.join(f'<path d="M{150 + k * 3} {70 + k * 6} l{12} -{3}" stroke="#292524" stroke-width="2"/>' for k in range(5))
UMAG = '<path d="M80 50 l0 50 a30 30 0 0 0 60 0 l0 -50" stroke="#dc2626" stroke-width="20" fill="none"/><rect x="70" y="40" width="20" height="14" fill="#d4d4d8"/><rect x="130" y="40" width="20" height="14" fill="#d4d4d8"/>'
RINGMAG = '<ellipse cx="110" cy="90" rx="60" ry="28" fill="#57534e"/><ellipse cx="110" cy="85" rx="22" ry="10" fill="#bae6fd"/>'
DISCMAG = '<ellipse cx="110" cy="100" rx="50" ry="18" fill="#57534e"/><rect x="60" y="80" width="100" height="20" fill="#78716c"/><ellipse cx="110" cy="80" rx="50" ry="18" fill="#a8a29e"/>'
def _hang(obj):
    s = '<rect x="10" y="20" width="200" height="130" fill="#fef3c7"/><path d="M50 145 l0 -110 l90 0" stroke="#57534e" stroke-width="6" fill="none"/><rect x="25" y="140" width="60" height="8" fill="#57534e"/><path d="M130 35 l0 60" stroke="#111827"/>'
    return s + ('<rect x="95" y="94" width="70" height="7" rx="3" fill="#facc15" stroke="#a16207"/>' if obj == 'pencil' else BARMAG(95, 92, 70, 0))
SUSPOLES = ('<svg viewBox="0 0 440 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif"><rect width="440" height="240" fill="#fff"/><path d="M60 225 l0 -200 M60 50 l130 0" stroke="#57534e" stroke-width="8"/><rect x="20" y="220" width="110" height="12" fill="#57534e"/>'
    '<path d="M180 50 l-20 110" stroke="#dc2626" stroke-width="2"/>' + BARMAG(110, 160, 110, 8) + '<path d="M150 160 l12 -15 l12 15z" fill="#fde68a"/>' + BARMAG(290, 175, 90, 15)
    + '<path d="M380 180 q30 0 50 10 l-10 20 q-25 -5 -40 -10z" fill="#d6a46b"/></svg>')
FIGS.update({
    'magobjects': lambda: panel_row([('Magnet and objects', MAGOBJ)], None, 190),
    'lodestone': lambda: panel_row([('Lodestone', LODESTONE)], None, 190),
    'magshapes': lambda: panel_row([('U Magnet', UMAG), ('Bar Magnet', BARMAG(50, 75, 120)), ('Ring Magnet', RINGMAG), ('Disc Magnet', DISCMAG)], 'Magnets of Different Shapes', 190),
    'hangpm': lambda: panel_row([('Suspended pencil', _hang('pencil')), ('Suspended bar magnet', _hang('magnet'))], None, 190),
    'suspoles': lambda: SUSPOLES,
})

def _over(table_mag):
    s = _hang('none') if False else '<rect x="10" y="20" width="200" height="130" fill="#fdba74" opacity=".5"/><path d="M50 145 l0 -110 l90 0" stroke="#57534e" stroke-width="6" fill="none"/><rect x="25" y="140" width="60" height="8" fill="#57534e"/><path d="M130 35 l0 50" stroke="#111827"/>'
    if table_mag:
        return s + BARMAG(95, 85, 70) .replace('#dc2626', '#TMP').replace('#2563eb', '#dc2626').replace('#TMP', '#2563eb').replace('>N<', '>X<').replace('>S<', '>N<').replace('>X<', '>S<') + BARMAG(100, 120, 80)
    return s + BARMAG(95, 85, 70, 40)
NEEDLEGLASS = ('<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14" font-weight="bold"><rect width="360" height="230" fill="#fff"/>'
    + BARMAG(30, 40, 40, 90) + '<path d="M70 70 l30 0 l0 -8 l14 12 l-14 12 l0 -8 l-30 0z" fill="#fff" stroke="#111827" stroke-width="2"/><path d="M20 82 l300 0" stroke="#111827" stroke-width="3"/><ellipse cx="22" cy="82" rx="6" ry="3" fill="none" stroke="#111827" stroke-width="2"/>'
    + '<text x="80" y="35" fill="#1d4ed8">Magnet</text><text x="40" y="115" fill="#1d4ed8">Needle</text><path d="M60 100 l10 -15" stroke="#111827"/>'
    + '<path d="M180 130 l120 0 l-15 95 l-90 0z" fill="#f8fafc" stroke="#111827" stroke-width="2"/><path d="M170 140 l150 -30" stroke="#57534e" stroke-width="6"/><path d="M245 125 l0 50" stroke="#111827"/><path d="M230 175 l30 0" stroke="#111827" stroke-width="2"/></svg>')
COMPASS = '<circle cx="110" cy="85" r="55" fill="#fde68a" stroke="#a16207" stroke-width="6"/><circle cx="110" cy="85" r="45" fill="#f8fafc"/><path d="M110 45 l10 40 l-20 0z" fill="#dc2626"/><path d="M110 125 l10 -40 l-20 0z" fill="#e5e7eb" stroke="#94a3b8"/><text x="106" y="55" font-size="10" fill="#111827">N</text>'
ATM = '<rect x="10" y="20" width="200" height="130" fill="#fef3c7"/><rect x="25" y="30" width="70" height="115" fill="#1d4ed8"/><rect x="35" y="45" width="40" height="30" fill="#22c55e"/><rect x="40" y="85" width="30" height="20" fill="#93c5fd"/><rect x="110" y="55" width="90" height="55" rx="6" fill="#1e3a8a"/><rect x="122" y="72" width="14" height="12" fill="#facc15"/>'
NAILSTAND = ('<svg viewBox="0 0 360 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14" font-weight="bold"><rect width="360" height="260" fill="#fff"/>'
    '<path d="M70 210 l220 0 l40 30 l-220 0z" fill="#e7a29b"/><rect x="175" y="20" width="12" height="200" fill="#be7d7d"/><rect x="60" y="40" width="120" height="30" fill="#8b5cf6"/><rect x="180" y="40" width="120" height="30" fill="#f87171"/>'
    + ''.join(f'<path d="M{68} {70 + k * 22} l-8 4 l8 18 l8 -18z" fill="#f8fafc" stroke="#94a3b8"/>' for k in range(4))
    + ''.join(f'<path d="M{292} {70 + k * 22} l-8 4 l8 18 l8 -18z" fill="#111827"/>' for k in range(4))
    + '<text x="250" y="30" fill="#1d4ed8">Bar Magnet</text><text x="85" y="120" fill="#1d4ed8">Steel Nails</text><text x="205" y="120" fill="#1d4ed8">Iron Nails</text><text x="200" y="185" fill="#1d4ed8">Stand</text></svg>')
FIGS.update({
    'earthmag1': lambda: panel_row([('Suspended magnet over a magnet', _over(True))], None, 190),
    'earthmag2': lambda: panel_row([('Suspended magnet alone', _over(False))], None, 190),
    'needleglass': lambda: NEEDLEGLASS,
    'compass': lambda: panel_row([('Magnetic compass', COMPASS)], None, 190),
    'atm': lambda: panel_row([('ATM Machine and Card', ATM)], None, 190),
    'nailstand': lambda: NAILSTAND,
})

ELECTRO = ('<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg"><rect width="400" height="300" fill="#fff"/><rect x="170" y="20" width="110" height="18" fill="#4f46e5"/><path d="M225 38 l0 150" stroke="#111827"/>'
    '<path d="M110 260 l160 -100" stroke="#78716c" stroke-width="6"/><path d="M262 148 l20 -10 l-6 22z" fill="#e7e5e4" stroke="#57534e"/>'
    + ''.join(f'<ellipse cx="{150 + k * 12}" cy="{236 - k * 7.5:.0f}" rx="5" ry="9" fill="none" stroke="#f472b6" stroke-width="3" transform="rotate(30 {150 + k * 12} {236 - k * 7.5:.0f})"/>' for k in range(9))
    + '<path d="M150 236 l0 50 l100 0 M260 175 l100 0 l0 110 l-60 0" stroke="#111827" stroke-width="2" fill="none"/>'
    '<rect x="250" y="270" width="90" height="26" rx="4" fill="#9a3412"/><rect x="255" y="273" width="38" height="20" rx="8" fill="#292524"/><rect x="297" y="273" width="38" height="20" rx="8" fill="#292524"/><path d="M230 286 l14 -10" stroke="#57534e" stroke-width="4"/>'
    + ''.join(f'<rect x="{100 + (k % 2) * 10}" y="{262 + k * 9}" width="8" height="22" rx="4" fill="none" stroke="#57534e" stroke-width="2" transform="rotate(20 104 {270 + k * 9})"/>' for k in range(3)) + '</svg>')
WALLBALLOON = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><rect x="40" y="20" width="40" height="130" fill="#c2725a"/><circle cx="125" cy="70" r="38" fill="#7f1d1d"/>' + ''.join(f'<text x="{92 + (k % 2) * 3}" y="{55 + k * 12}" fill="#fff" font-size="12">−</text><text x="{150}" y="{50 + k * 12}" fill="#fff" font-size="12">+</text>'.replace('−', '&#8722;') for k in range(3)) + '<path d="M125 108 q10 20 -5 35" stroke="#111827" fill="none"/>'
FIGS.update({
    'electromagnet': lambda: ELECTRO,
    'wallballoon': lambda: panel_row([('Charged balloon on a wall', WALLBALLOON)], None, 190),
})

RINGSTAND = ('<svg viewBox="0 0 340 270" xmlns="http://www.w3.org/2000/svg" font-family="serif" font-size="18"><rect width="340" height="270" fill="#fff"/>'
    '<path d="M60 220 l200 0 l20 25 l-200 0z" fill="#b45309"/><rect x="155" y="20" width="16" height="200" fill="#1d4ed8"/>'
    '<ellipse cx="163" cy="200" rx="90" ry="18" fill="#f87171"/><ellipse cx="163" cy="194" rx="90" ry="18" fill="#57534e"/><ellipse cx="163" cy="194" rx="12" ry="4" fill="#1d4ed8"/>'
    '<ellipse cx="163" cy="85" rx="90" ry="18" fill="#57534e"/><ellipse cx="163" cy="79" rx="90" ry="18" fill="#f87171"/><ellipse cx="163" cy="79" rx="12" ry="4" fill="#1d4ed8"/>'
    '<g stroke="#111827"><path d="M200 75 l50 -45"/><path d="M200 190 l40 -35 l60 0"/><path d="M130 205 l-25 50 l60 0" stroke-dasharray="3 2"/></g>'
    '<text x="252" y="30">N</text><path d="M240 155 l60 0" stroke="#111827" stroke-dasharray="3 2"/></svg>')
COMBKEY = '<rect x="10" y="20" width="200" height="130" fill="#f5f5f4"/><rect x="60" y="40" width="110" height="20" rx="3" fill="#57534e" transform="rotate(-40 115 50)"/>' + ''.join(f'<path d="M{75 + k * 8} {95 - k * 6.7:.0f} l14 10" stroke="#57534e" stroke-width="3"/>' for k in range(12)) + '<circle cx="150" cy="125" r="12" fill="none" stroke="#57534e" stroke-width="4"/><path d="M138 125 l-50 0 m10 0 l0 8 m10 -8 l0 6" stroke="#57534e" stroke-width="4"/>'
EGGHALF = '<rect x="10" y="20" width="200" height="130" fill="#d9f99d"/><ellipse cx="110" cy="85" rx="60" ry="50" fill="#f87171"/><ellipse cx="105" cy="82" rx="50" ry="42" fill="#fff"/><ellipse cx="100" cy="80" rx="24" ry="22" fill="#fb923c"/>'
EARTHHALF = '<rect x="10" y="20" width="200" height="130" fill="#d9f99d"/><circle cx="110" cy="85" r="60" fill="#60a5fa"/><path d="M130 40 q40 10 35 50 q-20 30 -40 20z" fill="#16a34a"/><path d="M110 25 a60 60 0 0 0 0 120z" fill="#be123c"/><path d="M110 32 a53 53 0 0 0 0 106z" fill="#f87171"/>'
FIGS.update({
    'ringstand': lambda: RINGSTAND,
    'combkey': lambda: panel_row([('Charged comb and iron key', COMBKEY)], None, 190),
    'eggearth': lambda: panel_row([('Boiled egg cut in half', EGGHALF), ('Inside of the Earth', EARTHHALF)], None, 190),
})

# --- Chapter 8: Structure of the Earth ---
EARTHWEDGE = ('<svg viewBox="0 0 480 400" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15"><rect width="480" height="400" fill="#fff"/>'
    '<path d="M60 20 l300 0 l30 90 l-330 0z" fill="#38bdf8"/><path d="M60 20 l50 0 l20 90 l-100 0z" fill="#16a34a"/>'
    '<path d="M30 110 L390 110 L210 395z" fill="#ef4444"/><path d="M30 110 l360 0" stroke="#111827" stroke-width="6"/>'
    '<path d="M131 270 L289 270 L210 395z" fill="#fdba74"/><path d="M175 340 L245 340 L210 395z" fill="#fde047"/>'
    '<g stroke="#111827" stroke-width="1.5" fill="none"><path d="M330 105 l60 -10"/><path d="M230 160 l170 40 M220 240 l180 -40"/><path d="M230 300 l160 0"/><path d="M215 365 l175 0"/></g>'
    '<g fill="#111827"><text x="395" y="98">Crust</text><text x="405" y="205">Mantle</text><text x="395" y="305">External Core</text><text x="395" y="370">Internal Core</text></g></svg>')
PEACH = ('<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14"><rect width="420" height="220" fill="#fff"/>'
    '<ellipse cx="230" cy="115" rx="95" ry="80" fill="#b91c1c"/><ellipse cx="230" cy="115" rx="88" ry="73" fill="#ef4444"/><ellipse cx="225" cy="105" rx="30" ry="36" fill="#1c1917"/>'
    '<g stroke="#111827" stroke-width="1.5"><path d="M150 50 l-30 -25"/><path d="M230 100 l90 -70"/><path d="M180 160 l-40 40"/></g>'
    '<g fill="#fff" stroke="#111827"><rect x="20" y="10" width="110" height="26"/><rect x="300" y="10" width="110" height="26"/><rect x="40" y="186" width="110" height="26"/></g>'
    '<g fill="#94a3b8"><text x="30" y="28">1</text><text x="310" y="28">2</text><text x="50" y="204">3</text></g></svg>')
LAKE = '<rect x="10" y="20" width="200" height="130" fill="#93c5fd"/><path d="M10 80 l40 -30 l30 15 l40 -35 l50 30 l40 -10 l0 40 l-200 0z" fill="#475569"/><path d="M40 50 l10 -8 l8 6z M110 30 l10 -8 l12 10z" fill="#f8fafc"/><path d="M10 85 q100 -10 200 0 l0 65 l-200 0z" fill="#166534"/><path d="M40 105 q80 -15 160 5 q-40 20 -160 15z" fill="#22d3ee"/>'
WATERCYCLE = ('<svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15" font-weight="bold"><rect width="520" height="300" fill="#bae6fd"/>'
    '<circle cx="450" cy="55" r="38" fill="#f97316"/><path d="M0 220 q150 -40 260 -20 l260 20 l0 80 l-520 0z" fill="#86efac"/><path d="M0 250 q200 -20 520 0 l0 50 l-520 0z" fill="#0ea5e9"/>'
    '<path d="M40 60 q20 -25 50 -10 q20 -25 50 0 q20 10 0 25 l-90 0 q-20 -5 -10 -15z" fill="#e5e7eb"/><path d="M60 90 l-8 30 M80 90 l-8 30 M100 90 l-8 30" stroke="#3b82f6" stroke-width="3"/>'
    '<path d="M420 100 q-60 -60 -160 -40" stroke="#c2410c" stroke-width="10" fill="none"/><path d="M260 60 l14 -12 l0 24z" fill="#c2410c"/>'
    '<path d="M140 80 q-50 60 -20 130" stroke="#c2410c" stroke-width="10" fill="none"/><path d="M120 210 l-10 -16 l22 0z" fill="#c2410c"/>'
    '<path d="M300 250 q80 0 120 -60" stroke="#c2410c" stroke-width="10" fill="none"/><path d="M420 190 l2 18 l-18 -6z" fill="#c2410c"/>'
    '<path d="M150 240 q60 20 120 10" stroke="#c2410c" stroke-width="10" fill="none"/><path d="M270 250 l-14 -10 l0 22z" fill="#c2410c"/>'
    '<g fill="#fff" stroke="#475569"><rect x="210" y="40" width="120" height="24"/><rect x="40" y="140" width="110" height="24"/><rect x="380" y="150" width="105" height="24"/><rect x="250" y="220" width="95" height="24"/></g>'
    '<g fill="#1e3a8a"><text x="218" y="58">Condensation</text><text x="46" y="158">Precipitation</text><text x="386" y="168">Evaporation</text><text x="258" y="238">Collection</text></g>'
    '<text x="250" y="150" fill="#b91c1c" font-size="30">WATER</text><text x="255" y="185" fill="#b91c1c" font-size="30">CYCLE</text></svg>')
FIGS.update({
    'earthwedge': lambda: EARTHWEDGE,
    'peach': lambda: PEACH,
    'lake': lambda: panel_row([('Sources of Water', LAKE)], None, 190),
    'watercycle': lambda: WATERCYCLE,
})

SOILKIDS = '<rect x="10" y="20" width="200" height="130" fill="#f5f5f4"/><rect x="25" y="105" width="75" height="40" fill="#fff" stroke="#d6d3d1"/><rect x="120" y="105" width="75" height="40" fill="#fff" stroke="#d6d3d1"/><ellipse cx="62" cy="128" rx="25" ry="8" fill="#44403c"/><ellipse cx="157" cy="128" rx="25" ry="8" fill="#44403c"/><circle cx="62" cy="55" r="15" fill="#fed7aa"/><rect x="45" y="70" width="34" height="32" fill="#9f1239"/><circle cx="157" cy="55" r="15" fill="#fed7aa"/><rect x="140" y="70" width="34" height="32" fill="#1e293b"/><circle cx="140" cy="95" r="10" fill="none" stroke="#16a34a" stroke-width="4"/>'
SOILJAR = '<rect x="10" y="20" width="200" height="130" fill="#ecfccb"/><rect x="75" y="30" width="70" height="14" rx="3" fill="#e5e7eb" stroke="#94a3b8"/><path d="M78 44 l64 0 l6 15 l0 85 q-38 8 -76 0 l0 -85z" fill="#f8fafc" fill-opacity=".6" stroke="#94a3b8"/><rect x="72" y="85" width="76" height="6" fill="#3f6212"/><rect x="72" y="91" width="76" height="20" fill="#292524"/><rect x="72" y="111" width="76" height="18" fill="#a16207"/><path d="M72 129 l76 0 l0 14 q-38 6 -76 0z" fill="#d6c4a8"/><rect x="72" y="60" width="76" height="25" fill="#bae6fd" opacity=".6"/>'
def _soil(c1, c2, n, big):
    return f'<rect x="10" y="20" width="200" height="130" fill="{c1}"/>' + ''.join(f'<circle cx="{14 + (k * 37) % 192}" cy="{24 + (k * 53) % 122}" r="{big + (k % 3)}" fill="{c2}" opacity=".8"/>' for k in range(n))
FIGS.update({
    'soilkids': lambda: panel_row([('Looking at soil through a magnifying glass', SOILKIDS)], None, 190),
    'soiljar': lambda: panel_row([('Soil settled in a jar of water', SOILJAR)], None, 190),
    'soiltypes': lambda: panel_row([('Clay', _soil('#3f3f1d', '#65a30d', 120, 2)), ('Sand', _soil('#1f2a1f', '#94a3b8', 160, 1)), ('Silt', _soil('#14532d', '#4d7c0f', 90, 4))], 'Types of Soil', 190),
})

BURROW = '<rect x="10" y="20" width="200" height="130" fill="#57534e"/><path d="M30 60 q40 30 20 80 M90 40 q-10 50 30 100 M150 50 q20 40 -10 90" stroke="#f9a8d4" stroke-width="5" fill="none"/><ellipse cx="160" cy="125" rx="20" ry="10" fill="#9a3412"/>'
def cups3():
    out = ['<svg viewBox="0 0 540 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="16" font-weight="bold"><rect width="540" height="220" fill="#ecfccb"/>']
    for i, (c, lab) in enumerate((('#c4b5fd', 'A'), ('#78716c', 'B'), ('#be123c', 'C'))):
        x = 30 + i * 175
        out.append(f'<path d="M{x} 70 l0 130 l130 0 l0 -130" fill="none" stroke="#111827" stroke-width="3"/><path d="M{x + 18} 90 l94 0 l-10 100 l-74 0z" fill="{c}" stroke="#111827" stroke-width="2"/>')
        out.append(f'<path d="M{x + 40} 192 l50 0" stroke="#111827" stroke-dasharray="2 3" stroke-width="3"/><text x="{x + 135}" y="200">{lab}</text>')
        out.append(f'<rect x="{x + 90}" y="20" width="40" height="22" rx="4" fill="#475569" transform="rotate(-30 {x + 110} 31)"/><path d="M{x + 92} 45 q-10 20 -20 45" stroke="#e0f2fe" stroke-width="4" fill="none"/>')
    out.append('</svg>')
    return ''.join(out)
FIGS.update({
    'burrow': lambda: panel_row([('Earthworms in the soil', BURROW)], None, 190),
    'cups3': cups3,
})

WCBLANK = ('<svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="15" font-weight="bold"><rect width="520" height="300" fill="#fff"/>'
    '<circle cx="420" cy="40" r="28" fill="#fde047"/><path d="M200 50 q30 -25 60 -5 q30 -25 70 0 q20 15 -10 25 l-110 0z M380 120 q20 -20 50 -5 q30 -15 50 10 l-100 5z" fill="#e0f2fe"/>'
    '<path d="M60 230 l100 -140 l50 50 l40 -40 l90 80 l170 -10 l0 110 l-450 0z" fill="#4d7c0f"/><path d="M130 130 l30 -40 l25 35z" fill="#94a3b8"/><path d="M60 230 l450 -10 l0 80 l-450 0z" fill="#7c2d12"/><path d="M250 240 q100 -20 260 -10 l0 40 l-260 0z" fill="#0ea5e9"/>'
    '<path d="M400 40 l-60 10" stroke="#0284c7" stroke-width="3"/><path d="M340 50 l10 -6 l0 12z" fill="#0284c7"/>'
    + ''.join(f'<path d="M{400 + k * 15} 200 q-6 -10 0 -20 q6 -10 0 -20" stroke="#0284c7" stroke-width="2" fill="none"/>' for k in range(6))
    + ''.join(f'<path d="M{215 + k * 12} 80 l-3 12" stroke="#0284c7" stroke-width="2"/>' for k in range(4))
    + '<g fill="#fff" stroke="#111827"><rect x="340" y="62" width="90" height="22"/><rect x="200" y="56" width="90" height="22"/><rect x="400" y="140" width="90" height="22"/><rect x="330" y="215" width="90" height="22"/></g>'
    '<g fill="#94a3b8"><text x="346" y="79">1</text><text x="206" y="73">2</text><text x="406" y="157">3</text><text x="336" y="232">4</text></g></svg>')
import math
def soilpie():
    parts = [('Air', 25, '#a8a29e'), ('Water', 25, '#7dd3fc'), ('Humus', 5, '#ec4899'), ('Sand and other minerals', 45, '#0ea5e9')]
    cx, cy, r = 140, 130, 100
    out = ['<svg viewBox="0 0 330 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13"><rect width="330" height="260" fill="#fff"/>']
    a0 = -90
    for name, pc, col in parts:
        a1 = a0 + pc * 3.6
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        out.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if pc > 50 else 0} 1 {x1:.1f} {y1:.1f}z" fill="{col}" stroke="#fff"/>')
        am = math.radians((a0 + a1) / 2)
        if name == 'Humus':
            out.append(f'<path d="M{cx + 80 * math.cos(am):.0f} {cy + 80 * math.sin(am):.0f} L210 250" stroke="#111827"/><text x="214" y="254">Humus</text>')
        else:
            words = name.split(' and ')
            for j, w in enumerate(words if len(words) > 1 else [name]):
                out.append(f'<text x="{cx + 55 * math.cos(am):.0f}" y="{cy + 55 * math.sin(am) + j * 15:.0f}" text-anchor="middle">{w if j == 0 or len(words) == 1 else "and " + w}</text>')
        a0 = a1
    out.append('</svg>')
    return ''.join(out)
FIGS.update({'wcblank': lambda: WCBLANK, 'soilpie': soilpie})

# --- Chapter 9: Space and Satellites ---
STARS = lambda n=30, seed=3: ''.join(f'<circle cx="{(k * 97 + seed * 13) % 200 + 10}" cy="{(k * 61 + seed * 7) % 130 + 20}" r="{1 + k % 2}" fill="#f8fafc"/>' for k in range(n))
SPACESCENE = ('<svg viewBox="0 0 520 280" xmlns="http://www.w3.org/2000/svg"><rect width="520" height="280" fill="#0b1020"/>'
    + ''.join(f'<circle cx="{(k * 131) % 520}" cy="{(k * 73) % 280}" r="{1 + k % 2}" fill="#f8fafc"/>' for k in range(60))
    + '<ellipse cx="270" cy="130" rx="150" ry="55" fill="#7c3aed" opacity=".35" transform="rotate(15 270 130)"/><ellipse cx="290" cy="140" rx="80" ry="30" fill="#f43f5e" opacity=".3"/>'
    '<circle cx="60" cy="55" r="38" fill="#d6d3d1"/><circle cx="48" cy="45" r="8" fill="#a8a29e"/><circle cx="72" cy="66" r="6" fill="#a8a29e"/>'
    '<path d="M50 230 l70 -35 l10 10 l-70 35z" fill="#f8fafc"/><path d="M120 195 l20 -8 l-5 18z" fill="#f97316"/><path d="M60 225 l-15 15 M70 238 l-10 18" stroke="#f8fafc" stroke-width="5"/>'
    '<rect x="400" y="200" width="20" height="30" fill="#e5e7eb"/><rect x="360" y="208" width="38" height="14" fill="#1e3a8a"/><rect x="422" y="208" width="38" height="14" fill="#1e3a8a"/>'
    '<rect x="410" y="40" width="70" height="10" fill="#9ca3af"/><rect x="430" y="30" width="30" height="30" fill="#78716c"/></svg>')
SPUTNIK = '<rect x="10" y="20" width="200" height="130" fill="#111827"/>' + STARS(15) + '<circle cx="140" cy="85" r="28" fill="#cbd5e1"/><circle cx="132" cy="78" r="8" fill="#f8fafc" opacity=".7"/><path d="M115 92 l-100 30 M118 100 l-95 45 M120 75 l-100 -15 M118 70 l-90 -40" stroke="#e5e7eb" stroke-width="1.5"/>'
MOONSTEP = '<rect x="10" y="20" width="200" height="130" fill="#1f2937"/><path d="M10 110 q100 -30 200 -10 l0 50 l-200 0z" fill="#9ca3af"/><circle cx="90" cy="88" r="8" fill="#e5e7eb"/><rect x="82" y="96" width="16" height="22" fill="#f8fafc"/><path d="M85 118 l-3 15 M95 118 l3 15" stroke="#f8fafc" stroke-width="5"/><path d="M150 80 l40 0 l10 30 l-60 0z" fill="#d97706"/><path d="M150 110 l-8 18 M200 110 l8 18" stroke="#a16207" stroke-width="3"/>'
STATION = lambda big=False: ('<rect x="10" y="20" width="200" height="130" fill="#0f172a"/>' + ('<path d="M10 120 q100 -30 200 0 l0 30 l-200 0z" fill="#1d4ed8"/>' if big else STARS(12))
    + '<rect x="80" y="78" width="60" height="14" fill="#e5e7eb"/><rect x="104" y="60" width="12" height="50" fill="#cbd5e1"/>'
    + ''.join(f'<rect x="{x}" y="45" width="10" height="70" fill="{c}"/>' for x, c in ((30, '#a16207'), (45, '#a16207'), (165, '#64748b'), (180, '#64748b'))) + '<path d="M55 85 l25 0 M140 85 l25 0" stroke="#e5e7eb" stroke-width="3"/>')
ORBIT = ('<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14"><rect width="420" height="260" fill="#111827"/>'
    '<circle cx="190" cy="215" r="200" fill="none" stroke="#e5e7eb" stroke-width="2"/><circle cx="190" cy="215" r="35" fill="#f87171"/><text x="175" y="252" fill="#e5e7eb">Sun</text>'
    '<circle cx="330" cy="80" r="55" fill="none" stroke="#e5e7eb" stroke-width="2"/><circle cx="330" cy="80" r="18" fill="#3b82f6"/><circle cx="380" cy="100" r="6" fill="#f8fafc"/>'
    '<text x="300" y="120" fill="#e5e7eb">Earth</text><text x="368" y="125" fill="#e5e7eb">Moon</text><path d="M372 70 q8 15 3 25" stroke="#e5e7eb" fill="none"/><path d="M371 95 l4 -1 l-1 -5" stroke="#e5e7eb" fill="none"/></svg>')
FIGS.update({
    'spacescene': lambda: SPACESCENE,
    'sputnik': lambda: panel_row([('Sputnik-1', SPUTNIK)], None, 190),
    'moonstep': lambda: panel_row([('Human first step on moon', MOONSTEP)], None, 190),
    'mir': lambda: panel_row([('MIR space station', STATION())], None, 190),
    'iss': lambda: panel_row([('International space station', STATION(True))], None, 190),
    'orbit': lambda: ORBIT,
})

EARTHSPIN = ('<svg viewBox="0 0 340 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14" font-weight="bold"><rect width="340" height="260" fill="#fff"/>'
    '<circle cx="170" cy="130" r="80" fill="#bae6fd"/><path d="M130 80 q30 -20 60 10 q-10 30 -30 40 q-20 -10 -30 -50z M160 150 q30 0 25 50 q-20 10 -30 -20z" fill="#c2410c"/>'
    '<path d="M170 40 l0 -20 M170 220 l0 20" stroke="#111827" stroke-width="2"/><path d="M158 26 q12 -10 24 0 M158 236 q12 10 24 0" stroke="#111827" fill="none"/>'
    '<path d="M95 100 q60 70 170 50" stroke="#111827" stroke-width="3" fill="none"/><path d="M265 150 l-12 -8 l2 14z" fill="#111827"/>'
    '<text x="190" y="18">North Pole</text><text x="135" y="255">South Pole</text><text x="70" y="95">West</text><text x="270" y="155">East</text></svg>')
SAT = lambda: '<rect x="85" y="75" width="40" height="30" fill="#d6d3d1"/><rect x="25" y="80" width="55" height="20" fill="#1e3a8a"/><rect x="130" y="80" width="55" height="20" fill="#1e3a8a"/><path d="M80 90 l5 0 M125 90 l5 0" stroke="#e5e7eb" stroke-width="3"/>'
HUBBLE = '<rect x="10" y="20" width="200" height="130" fill="#111827"/><path d="M10 120 q100 -30 200 0 l0 30 l-200 0z" fill="#93c5fd"/><rect x="70" y="45" width="90" height="28" rx="6" fill="#d6d3d1" transform="rotate(25 115 59)"/><rect x="95" y="75" width="12" height="40" fill="#78716c" transform="rotate(25 101 95)"/>'
GEOSAT = '<rect x="10" y="20" width="200" height="130" fill="#111827"/><path d="M10 115 q100 -25 200 0 l0 35 l-200 0z" fill="#3b82f6"/>' + SAT()
THREESATS = ('<svg viewBox="0 0 300 160" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" font-weight="bold"><rect width="300" height="160" fill="#fff"/>'
    '<ellipse cx="150" cy="85" rx="130" ry="60" fill="none" stroke="#111827"/><path d="M150 85 L30 60 L270 50z" fill="#fef08a" opacity=".6"/><path d="M150 85 L270 50 L230 140z" fill="#f9a8d4" opacity=".6"/><path d="M150 85 L230 140 L30 60z" fill="#86efac" opacity=".6"/>'
    '<circle cx="150" cy="85" r="20" fill="#16a34a"/><g fill="#475569"><rect x="22" y="54" width="16" height="10"/><rect x="262" y="44" width="16" height="10"/><rect x="222" y="134" width="16" height="10"/></g>'
    '<text x="10" y="20">Satellite 1</text><text x="230" y="20">Satellite 2</text><text x="240" y="155">Satellite 3</text></svg>')
POLAR = '<rect x="10" y="20" width="200" height="130" fill="#312e81"/><circle cx="100" cy="90" r="55" fill="#bae6fd"/><path d="M100 20 l0 140" stroke="#111827" stroke-width="5"/><ellipse cx="100" cy="90" rx="30" ry="68" fill="none" stroke="#c7d2fe" stroke-dasharray="4 3"/><circle cx="130" cy="45" r="7" fill="#fde047"/>'
COMMSAT = '<rect x="10" y="20" width="200" height="130" fill="#1f2937"/><path d="M10 125 q100 -20 200 0 l0 25 l-200 0z" fill="#93c5fd"/>' + SAT() + '<circle cx="105" cy="70" r="8" fill="#e5e7eb"/><circle cx="95" cy="108" r="6" fill="#e5e7eb"/>'
FIGS.update({
    'earthspin': lambda: EARTHSPIN,
    'hubble': lambda: panel_row([('Hubble space telescope', HUBBLE)], None, 190),
    'geosat': lambda: panel_row([('Geostationary Satellite', GEOSAT)], None, 190),
    'threesats': lambda: THREESATS,
    'polarsat': lambda: panel_row([('Poler Satellite', POLAR)], None, 190),
    'commsat': lambda: panel_row([('Communication Satellite', COMMSAT)], None, 190),
})

SATFORCE = ('<svg viewBox="0 0 360 260" xmlns="http://www.w3.org/2000/svg"><rect width="360" height="260" fill="#fff"/>'
    '<ellipse cx="180" cy="130" rx="150" ry="105" fill="none" stroke="#111827" stroke-width="3" stroke-dasharray="3 8"/>'
    '<circle cx="180" cy="130" r="55" fill="#1d4ed8"/><path d="M150 100 q30 -20 50 10 q-10 30 -30 30z M190 150 q25 0 20 30 q-20 5 -25 -15z" fill="#16a34a"/>'
    '<g fill="#475569"><rect x="310" y="40" width="22" height="12"/><rect x="18" y="110" width="22" height="12"/></g>'
    '<path d="M150 25 l-12 4 l12 4" stroke="#111827" stroke-width="2" fill="none"/><path d="M250 236 l12 -4 l-12 -4" stroke="#111827" stroke-width="2" fill="none"/>'
    '<g stroke="#dc2626" stroke-width="3"><path d="M312 52 L245 95"/><path d="M42 118 L120 125"/></g><path d="M245 95 l4 -10 l6 8z M120 125 l-9 -5 l0 10z" fill="#dc2626"/></svg>')
FIGS.update({'satforce': lambda: SATFORCE})

# --- Chapter 10: Technology in everyday Life ---
TRUSS = '<svg viewBox="0 0 320 110" xmlns="http://www.w3.org/2000/svg"><rect width="320" height="110" fill="#fff"/><path d="M10 80 l300 0 M40 80 l0 20 M280 80 l0 20 M50 80 l30 -55 l40 55 l40 -55 l40 55 l40 -55 l30 55 M80 25 l160 0" stroke="#111827" stroke-width="7" fill="none" stroke-linejoin="round"/></svg>'
def _bridge_step(k):
    s = '<rect x="10" y="20" width="200" height="130" fill="#fdf4ff"/>'
    if k >= 1:
        s += '<path d="M25 110 l170 0 M25 60 l170 0" stroke="#c2a27c" stroke-width="4"/>'
    if k >= 2:
        s += ''.join(f'<path d="M{25 + i * 34} 110 l17 -50 l17 50" stroke="#c2a27c" stroke-width="3" fill="none"/>' for i in range(5))
    if k >= 3:
        s += '<path d="M25 128 l170 0" stroke="#d6b88f" stroke-width="12"/>'
    return s
SHELF = '<rect x="10" y="20" width="200" height="130" fill="#ecfccb"/><rect x="40" y="30" width="140" height="115" fill="#7c2d12"/>' + ''.join(f'<rect x="46" y="{36 + k * 36}" width="128" height="28" fill="#451a03"/><rect x="40" y="{64 + k * 36}" width="140" height="8" fill="#c2410c"/>' for k in range(3))
SPIRIT = lambda three=False: ('<svg viewBox="0 0 480 90" xmlns="http://www.w3.org/2000/svg"><rect width="480" height="90" fill="#fff"/><rect x="10" y="25" width="460" height="50" fill="#facc15"/><rect x="5" y="20" width="10" height="60" fill="#111827"/><rect x="465" y="20" width="10" height="60" fill="#111827"/>'
    '<rect x="210" y="15" width="60" height="25" rx="4" fill="#111827"/><rect x="218" y="20" width="44" height="12" rx="6" fill="#bbf7d0"/><ellipse cx="240" cy="26" rx="8" ry="4" fill="#f8fafc"/>'
    + ('<circle cx="70" cy="50" r="7" fill="#111827"/><circle cx="125" cy="50" r="22" fill="#111827"/><rect x="117" y="34" width="16" height="32" rx="6" fill="#bbf7d0"/><circle cx="400" cy="50" r="22" fill="#111827"/><rect x="392" y="34" width="16" height="32" rx="6" fill="#bbf7d0" transform="rotate(45 400 50)"/>' if three else '') + '</svg>')
LEVELTABLE = '<rect x="10" y="20" width="200" height="130" fill="#fef3c7"/><path d="M10 130 l200 -40 l0 60 l-200 0z" fill="#5eead4"/><rect x="40" y="95" width="150" height="16" fill="#facc15" transform="rotate(-11 115 103)"/><circle cx="165" cy="55" r="30" fill="#fef9c3" stroke="#111827" stroke-width="2"/><rect x="150" y="48" width="30" height="12" rx="6" fill="#4ade80"/><ellipse cx="165" cy="54" rx="5" ry="3" fill="#f8fafc"/>'
PLUMB = ('<svg viewBox="0 0 440 280" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="14" font-weight="bold"><rect width="440" height="280" fill="#fff"/>'
    '<path d="M40 30 l40 0" stroke="#111827" stroke-width="3"/><path d="M60 30 q20 -25 40 -20" stroke="#111827" fill="none"/><path d="M60 30 l0 190" stroke="#111827"/><path d="M45 220 l30 0 l-15 40z" fill="#9ca3af" stroke="#111827"/>'
    '<text x="85" y="45" fill="#111827">Square</text><text x="85" y="60" fill="#111827">plate</text><text x="80" y="140" fill="#111827">String</text><text x="85" y="250" fill="#111827">Plumb bub</text>'
    '<rect x="330" y="20" width="14" height="250" fill="#d1d5db" stroke="#6b7280"/><rect x="344" y="30" width="30" height="70" fill="#f8fafc"/><rect x="374" y="30" width="60" height="70" fill="#14532d"/><circle cx="404" cy="65" r="17" fill="#f8fafc"/><circle cx="410" cy="62" r="15" fill="#14532d"/>'
    '<path d="M300 110 l29 0 M315 110 l0 120" stroke="#111827"/><path d="M308 230 l14 0 l-7 18z" fill="#9ca3af" stroke="#111827"/><rect x="262" y="95" width="40" height="20" fill="#f5c9a8"/></svg>')
FIGS.update({
    'truss': lambda: TRUSS,
    'bridgesteps': lambda: panel_row([('Cut skewers to size', _bridge_step(1)), ('Make the side walls', _bridge_step(2)), ('Fix the deck', _bridge_step(3))], None, 190),
    'shelf': lambda: panel_row([('Model of a bookshelf', SHELF)], None, 190),
    'spirit': lambda: SPIRIT(False),
    'spirit3': lambda: SPIRIT(True),
    'leveltable': lambda: panel_row([('Checking a table top with a spirit level', LEVELTABLE)], None, 190),
    'plumb': lambda: PLUMB,
})

LEDROWS = '<svg viewBox="0 0 480 130" xmlns="http://www.w3.org/2000/svg"><rect width="480" height="130" fill="#fff"/>' + ''.join(f'<rect x="10" y="{12 + r * 40}" width="460" height="22" fill="{bg}"/>' + ''.join(f'<circle cx="{30 + k * 38}" cy="{23 + r * 40}" r="8" fill="{c}" stroke="#111827"/>' for k in range(12)) for r, (bg, c) in enumerate((('#bfdbfe', '#2563eb'), ('#fecaca', '#dc2626'), ('#bbf7d0', '#16a34a')))) + '</svg>'
LEDLEGS = ('<svg viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="16" font-weight="bold"><rect width="260" height="130" fill="#fff"/>'
    + ''.join(f'<path d="M{20 + k * 70} 45 a20 20 0 0 1 40 0 l0 15 l-40 0z" fill="{c}"/><path d="M{28 + k * 70} 60 l0 40 M{52 + k * 70} 60 l0 55" stroke="#111827" stroke-width="2"/><text x="{20 + k * 70}" y="112">&#8722;</text><text x="{56 + k * 70}" y="126">+</text>' for k, c in enumerate(('#f87171', '#4ade80', '#facc15'))) + '</svg>')
STRIPHOLES = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M15 60 l190 0 l-10 50 l-180 0z" fill="#f87171"/>' + ''.join(f'<circle cx="{35 + k * 40}" cy="{75 + j * 18}" r="3" fill="#fff"/>' for k in range(5) for j in range(2))
STRIPLEDS = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M15 85 l190 0 l-10 30 l-180 0z" fill="#f87171"/>' + ''.join(f'<path d="M{45 + k * 55} 85 l0 -30 a14 14 0 0 1 28 0 l0 30z" fill="#a855f7"/><path d="M{50 + k * 55} 115 l0 30 M{66 + k * 55} 115 l0 25" stroke="#111827" stroke-width="2"/>' for k in range(3))
SHOEBOX = lambda tube: ('<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M30 80 l90 -30 l80 30 l-90 30z" fill="#fca5a5"/><path d="M30 80 l0 40 l90 30 l0 -40z" fill="#dc2626"/><path d="M120 110 l0 40 l80 -30 l0 -40z" fill="#b91c1c"/><ellipse cx="115" cy="80" rx="22" ry="10" fill="#7f1d1d"/>'
    + ('<rect x="140" y="95" width="70" height="20" rx="10" fill="#a16207" transform="rotate(-15 175 105)"/>' + ''.join(f'<path d="M{60 + k * 12} {70 - k * 4} l70 25" stroke="#f8fafc" stroke-width="2"/>' for k in range(2)) if tube else ''))
FIGS.update({
    'ledrows': lambda: LEDROWS,
    'ledlegs': lambda: LEDLEGS,
    'ledstrip': lambda: panel_row([('Figure 3', STRIPHOLES), ('Figure 4', STRIPLEDS)], None, 190),
    'shoebox': lambda: panel_row([('Shoe box with a round hole', SHOEBOX(False)), ('Box with tube and rubber bands', SHOEBOX(True))], None, 190),
})

WAGONNET = ('<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg"><rect width="420" height="220" fill="#fff"/>'
    '<path d="M60 10 l200 0 l0 35 l40 0 l0 95 l-40 0 l0 35 l-200 0 l0 -35 l-40 0 l0 -95 l40 0z" fill="none" stroke="#1d4ed8" stroke-width="2"/>'
    '<rect x="60" y="45" width="200" height="95" fill="none" stroke="#dc2626" stroke-width="2"/>'
    + ''.join(f'<circle cx="{325 + (k % 2) * 60}" cy="{120 + (k // 2) * 60}" r="28" fill="none" stroke="#111827" stroke-width="2"/><circle cx="{325 + (k % 2) * 60}" cy="{120 + (k // 2) * 60}" r="5" fill="none" stroke="#111827" stroke-width="2"/>' for k in range(4)) + '</svg>')
WAGON = '<rect x="10" y="20" width="200" height="130" fill="#292524"/><path d="M45 110 q0 -70 65 -75 q65 5 65 75z" fill="#f5f5f4"/><rect x="40" y="105" width="140" height="14" fill="#a8a29e"/><circle cx="65" cy="125" r="12" fill="#e7e5e4" stroke="#57534e" stroke-width="2"/><circle cx="155" cy="125" r="12" fill="#e7e5e4" stroke="#57534e" stroke-width="2"/>'
FAKIT = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M25 60 l170 0 l0 70 l-170 0z" fill="#ea580c"/><path d="M30 64 l160 0 l0 62 l-160 0z" fill="#1f2937"/><rect x="40" y="70" width="40" height="18" fill="#e5e7eb"/><rect x="40" y="95" width="25" height="12" fill="#5eead4"/><path d="M95 75 l80 0 M95 88 l70 0 M95 101 l75 0" stroke="#e5e7eb" stroke-width="4"/><rect x="85" y="40" width="50" height="12" rx="4" fill="#9a3412"/>'
def _hand(bandage):
    s = '<rect x="10" y="20" width="200" height="130" fill="#fff"/><path d="M20 120 q60 -40 150 -30 l20 30 q-90 20 -170 20z" fill="#f5c9a8"/>'
    return s + ('<path d="M100 95 q30 -8 50 -2 l5 30 q-30 6 -55 4z" fill="#f8fafc" stroke="#d6d3d1"/><circle cx="125" cy="108" r="6" fill="#dc2626" opacity=".5"/>' if bandage else '<path d="M95 60 q20 -30 40 0 l-10 40 l-25 0z" fill="#fef3c7" stroke="#d6d3d1"/>')
SCENE = lambda k: ('<rect x="10" y="20" width="200" height="130" fill="#7dd3fc"/>' + ''.join(f'<circle cx="{25 + i * 30}" cy="80" r="14" fill="#16a34a"/>' for i in range(7)) + '<rect x="10" y="100" width="200" height="50" fill="#57534e"/><path d="M10 125 l200 0" stroke="#facc15" stroke-dasharray="10 8" stroke-width="2"/>'
    + ('<rect x="30" y="100" width="70" height="25" rx="8" fill="#dc2626"/><circle cx="45" cy="127" r="6" fill="#111827"/><circle cx="85" cy="127" r="6" fill="#111827"/><ellipse cx="140" cy="125" rx="16" ry="5" fill="#9f1239"/><circle cx="170" cy="95" r="6" fill="#fed7aa"/><rect x="165" y="101" width="10" height="20" fill="#1f2937"/>' if k == 1 else
       '<circle cx="90" cy="85" r="6" fill="#fed7aa"/><rect x="85" y="91" width="10" height="22" fill="#e5e7eb"/><circle cx="120" cy="85" r="6" fill="#fed7aa"/><rect x="115" y="91" width="10" height="22" fill="#1f2937"/><ellipse cx="105" cy="105" rx="14" ry="5" fill="#9f1239"/>'))
CALL1122 = '<rect x="10" y="20" width="200" height="130" fill="#6366f1" opacity=".6"/><rect x="20" y="75" width="110" height="45" rx="6" fill="#f8fafc" stroke="#dc2626"/><circle cx="40" cy="122" r="8" fill="#111827"/><circle cx="110" cy="122" r="8" fill="#111827"/><rect x="145" y="35" width="50" height="95" rx="6" fill="#111827"/><rect x="150" y="45" width="40" height="70" fill="#f8fafc"/><text x="152" y="70" font-size="14" font-weight="bold" fill="#dc2626">1122</text><rect x="152" y="95" width="36" height="12" rx="6" fill="#dc2626"/>'
FIGS.update({
    'wagonnet': lambda: WAGONNET,
    'wagon': lambda: panel_row([('Wagon with a paper roof', WAGON)], None, 190),
    'firstaid': lambda: panel_row([('First Aid Box', FAKIT)], None, 190),
    'dressing': lambda: panel_row([('Placing the bandage', _hand(False)), ('Dressing the wound', _hand(True))], None, 190),
    'step1': lambda: panel_row([('An accident on the road', SCENE(1)), ('Moving the injured person to safety', SCENE(2))], None, 190),
    'bleed': lambda: panel_row([('Bandage to stop bleeding', _hand(True))], None, 190),
    'call1122': lambda: panel_row([('Calling the ambulance (1122)', CALL1122)], None, 190),
})

def _drill(kind):
    s = '<rect x="10" y="20" width="200" height="130" fill="#1d4ed8"/>'
    table = '<path d="M50 60 l120 0 l0 8 l-120 0z M58 68 l0 75 M162 68 l0 75" fill="#111827" stroke="#111827" stroke-width="6"/>'
    fig = {
        'Drop': '<circle cx="85" cy="70" r="14" fill="#f8fafc"/><path d="M95 85 q40 0 50 30 l-20 25 M95 85 l-25 50 M140 110 l20 30" stroke="#f8fafc" stroke-width="10" fill="none" stroke-linecap="round"/>',
        'Cover': table + '<circle cx="95" cy="105" r="12" fill="#f8fafc"/><path d="M105 115 q30 0 40 20 M105 115 l-20 25" stroke="#f8fafc" stroke-width="9" fill="none" stroke-linecap="round"/>',
        'Hold on': table + '<path d="M75 135 q20 -25 60 -20 q20 5 25 20z" fill="#f8fafc"/><circle cx="80" cy="120" r="10" fill="#f8fafc"/><path d="M150 115 l10 -45" stroke="#f8fafc" stroke-width="7"/>',
        'Stand up': table + '<circle cx="110" cy="80" r="11" fill="#f8fafc"/><path d="M110 92 l0 30 l-12 22 M110 122 l12 22 M110 100 l-15 15 M110 100 l15 15" stroke="#f8fafc" stroke-width="8" fill="none" stroke-linecap="round"/>',
        'Exit': '<rect x="20" y="40" width="40" height="105" fill="#111827"/><circle cx="140" cy="55" r="11" fill="#f8fafc"/><path d="M140 67 l-10 35 l-25 30 M130 102 l25 30 M135 80 l30 -10 M135 80 l-30 10" stroke="#f8fafc" stroke-width="8" fill="none" stroke-linecap="round"/>',
    }[kind]
    return s + fig
CLASSDRILL = '<rect x="10" y="20" width="200" height="130" fill="#7c2d12"/>' + ''.join(f'<rect x="{20 + c * 65}" y="{45 + r * 50}" width="55" height="10" fill="#a16207"/><path d="M{24 + c * 65} 55 l0 {20 + r * 50} M{70 + c * 65} 55 l0 {20 + r * 50}" stroke="#78350f" stroke-width="4"/><circle cx="{47 + c * 65}" cy="{68 + r * 50}" r="8" fill="#fed7aa"/>' for c in range(3) for r in range(2))
LAWNDRILL = '<rect x="10" y="20" width="200" height="130" fill="#65a30d"/>' + ''.join(f'<circle cx="{25 + (k % 9) * 22}" cy="{40 + (k // 9) * 30}" r="9" fill="#fed7aa"/><path d="M{17 + (k % 9) * 22} {34 + (k // 9) * 30} q8 -10 16 0" stroke="#facc15" stroke-width="4" fill="none"/>' for k in range(36))
EXTING = '<rect x="10" y="20" width="200" height="130" fill="#bae6fd"/><rect x="85" y="50" width="45" height="95" rx="16" fill="#dc2626"/><rect x="95" y="80" width="25" height="28" fill="#f8fafc"/><path d="M95 50 l0 -15 l30 0 l20 -8 M110 35 l-25 -8" stroke="#111827" stroke-width="5" fill="none"/>'
FIGS.update({
    'drillA': lambda: panel_row([(k, _drill(k)) for k in ('Drop', 'Cover', 'Hold on')], None, 190),
    'drillB': lambda: panel_row([(k, _drill(k)) for k in ('Hold on', 'Stand up', 'Exit')], None, 190),
    'drillpics': lambda: panel_row([('If you are in classroom', CLASSDRILL), ('If you are in the lawn', LAWNDRILL)], None, 190),
    'extinguisher': lambda: panel_row([('Fire Extinguisher', EXTING)], None, 190),
})

if __name__ == '__main__':
    print(FIGS[sys.argv[1]]())
