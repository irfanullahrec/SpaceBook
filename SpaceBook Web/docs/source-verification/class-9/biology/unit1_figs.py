# -*- coding: utf-8 -*-
"""Coded SVG figures for Unit 1 (Figures 1.2-1.5). Each builder takes a label
dict so English, Urdu and Pashto variants share one geometry."""
import math
from bio9_tools import svg_wrap, txt

FONT = 'Segoe UI, Noto Sans, Noto Naskh Arabic, sans-serif'


def pie_bioelements(L):
    """Figure 1.2 percentage composition (by mass) of bio-elements: values from source."""
    # clockwise from the top, matching the book: small slices sit at the top
    data = [('others', 1, '#90a4ae'), ('oxygen', 65, '#f9d5e5'), ('carbon', 18, '#fbe3ee'), ('hydrogen', 10, '#e8f5e9'),
            ('nitrogen', 3, '#fde7f3'), ('calcium', 2, '#f3e5f5'), ('phosphorous', 1, '#ec407a')]
    cx, cy, r = 210, 175, 120
    a = math.radians(-80)
    body = []
    inner = {'oxygen': (275, 215), 'carbon': (135, 185), 'hydrogen': (172, 118)}
    outer = {'nitrogen': (20, 72, 'start'), 'calcium': (20, 24, 'start'), 'phosphorous': (432, 24, 'end'), 'others': (432, 72, 'end')}
    for key, v, col in data:
        sweep = 2 * math.pi * v / 100
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        a2 = a + sweep
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        large = 1 if sweep > math.pi else 0
        body.append(f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f} Z" fill="{col}" stroke="#4a4a4a" stroke-width="1.2"/>')
        mid = a + sweep / 2
        if key in outer:
            lx, ly, anchor = outer[key]
            ex, ey = cx + (r - 6) * math.cos(mid), cy + (r - 6) * math.sin(mid)
            tx = lx + 75 if anchor == 'start' else lx - 75
            body.append(f'<path d="M{ex:.1f},{ey:.1f} L{tx},{ly - 4}" stroke="#333" fill="none"/>')
            body.append(txt(lx, ly, L[key], 13, anchor, 'normal', '#222') + txt(lx, ly + 15, f'{v}%', 12, anchor, 'normal', '#222'))
        else:
            lx, ly = inner[key]
            body.append(txt(lx, ly, L[key], 13, 'middle', 'normal', '#222') + txt(lx, ly + 15, f'{v}%', 12, 'middle', 'normal', '#222'))
        a = a2
    return svg_wrap(''.join(body), 440, 300, L['title'])


PIE_EN = dict(title='Figure 1.2: Percentage composition (by mass) of bio-elements in organisms',
              oxygen='Oxygen', carbon='Carbon', hydrogen='Hydrogen', nitrogen='Nitrogen', calcium='Calcium',
              phosphorous='Phosphorous', others='Others')
PIE_UR = dict(title='شکل 1.2', oxygen='آکسیجن', carbon='کاربن', hydrogen='ہائیڈروجن', nitrogen='نائٹروجن',
              calcium='کیلشیم', phosphorous='فاسفورس', others='دیگر')
PIE_PS = dict(title='شکل 1.2', oxygen='اکسیجن', carbon='کاربن', hydrogen='هایدروجن', nitrogen='نایټروجن',
              calcium='کلسیم', phosphorous='فاسفورس', others='نور')


def levels_diagram(L):
    """Figure 1.3: U-shaped sequence Atoms -> ... -> Organism -> Population -> ... -> Biosphere."""
    left = ['atoms', 'molecule', 'organelle', 'cell', 'tissue', 'organ', 'organ_system']
    right = ['population', 'community', 'ecosystem', 'biosphere']
    body = ['<defs><marker id="b13a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#c2185b"/></marker></defs>']
    # pink U arrow
    body.append('<path d="M150,60 C150,420 220,470 290,470 C345,470 340,400 340,345" fill="none" stroke="#f8bbd0" stroke-width="26" stroke-linecap="round"/>')
    body.append('<polygon points="318,350 362,350 340,312" fill="#f48fb1" stroke="#c2185b" stroke-width="2"/>')
    # icons on the left path
    icons = [
        '<g fill="#ef9a9a">' + ''.join(f'<circle cx="{170+i*7}" cy="{30+(i%2)*6}" r="2"/>' for i in range(6)) + '</g>',
        '<circle cx="168" cy="85" r="7" fill="#e57373"/><circle cx="182" cy="85" r="7" fill="#e57373"/><circle cx="175" cy="74" r="5" fill="#fff" stroke="#e57373"/>',
        '<ellipse cx="175" cy="132" rx="11" ry="7" fill="#81c784" stroke="#2e7d32"/>',
        '<ellipse cx="175" cy="180" rx="24" ry="14" fill="#ffe0b2" stroke="#8d6e63"/><circle cx="170" cy="180" r="5" fill="#8d6e63"/>',
        '<ellipse cx="185" cy="232" rx="20" ry="11" fill="#fff3e0" stroke="#8d6e63"/><path d="M168,232 h34 M175,224 v16 M190,224 v16" stroke="#bcaaa4"/>',
        '<path d="M200,270 q12,-14 22,4 q-6,18 -18,10 z" fill="#e57373" stroke="#b71c1c"/>',
        '<path d="M205,330 q20,-25 50,-5 q10,25 -10,40 q-30,10 -40,-35 z" fill="#d7ccc8" stroke="#5d4037"/>',
    ]
    ys = [30, 85, 132, 180, 232, 282, 340]
    for i, key in enumerate(left):
        body.append(icons[i])
        body.append(f'<rect x="10" y="{ys[i]-15}" width="120" height="26" fill="#fff" stroke="#111" stroke-width="1.5"/>')
        body.append(txt(70, ys[i] + 3, L[key], 13, 'middle', 'bold', '#111'))
    # organism (elephant silhouette) at the bottom
    body.append('<path d="M265,440 q-5,-40 35,-45 q40,-3 45,30 l0,25 h-10 v-18 h-12 v18 h-10 v-18 h-25 v18 h-10 z M300,400 q-25,0 -28,30 l-6,22" fill="#9e9e9e" stroke="#424242"/>')
    body.append(f'<rect x="200" y="470" width="120" height="26" fill="#fff" stroke="#111" stroke-width="1.5"/>')
    body.append(txt(260, 488, L['organism'], 13, 'middle', 'bold', '#111'))
    # right column with scene tiles
    rys = [300, 225, 150, 70]
    fills = ['#c8e6c9', '#a5d6a7', '#fff59d', '#90caf9']
    for i, key in enumerate(right):
        y = rys[i]
        if key == 'biosphere':
            body.append(f'<circle cx="420" cy="{y-5}" r="38" fill="#64b5f6" stroke="#1565c0"/><path d="M398,{y-20} q15,-8 25,5 q-5,15 -20,10 z M425,{y+5} q12,-5 18,8 q-10,12 -18,2 z" fill="#81c784"/>')
        else:
            body.append(f'<rect x="360" y="{y-32}" width="180" height="60" rx="4" fill="{fills[i]}" stroke="#8d6e63"/>')
            body.append(f'<path d="M370,{y+20} q40,-30 80,0 t80,0" fill="none" stroke="#6d4c41"/>')
        body.append(f'<rect x="440" y="{y-14}" width="130" height="26" fill="#fff" stroke="#111" stroke-width="1.5"/>')
        body.append(txt(505, y + 4, L[key], 13, 'middle', 'bold', '#111'))
    return svg_wrap(''.join(body), 580, 505, L['title'])


LEV_EN = dict(title='Figure 1.3: Diagram showing different Levels of Biological Organization', atoms='Atoms', molecule='Molecule',
              organelle='Organelle', cell='Cell', tissue='Tissue', organ='Organ', organ_system='Organ system', organism='Organism',
              population='Population', community='Community', ecosystem='Ecosystem', biosphere='Biosphere')
LEV_UR = dict(title='شکل 1.3', atoms='ایٹم', molecule='مالیکیول', organelle='عضیہ', cell='خلیہ', tissue='بافت', organ='عضو',
              organ_system='نظامِ اعضا', organism='جاندار', population='آبادی', community='کمیونٹی', ecosystem='ماحولیاتی نظام', biosphere='بائیوسفیئر')
LEV_PS = dict(title='شکل 1.3', atoms='اتومونه', molecule='مالیکول', organelle='اورګانیل', cell='حجره', tissue='نسج', organ='غړی',
              organ_system='د غړو سیسټم', organism='ژوندی موجود', population='نفوس', community='ټولنه', ecosystem='ایکوسیسټم', biosphere='بایوسفیر')


def chlamy_volvox(L):
    """Figure 1.4: (a) Chlamydomonas with labelled flagella, eye spot, nucleus, chloroplast; (b) Volvox colonies."""
    b = ['<rect x="0" y="0" width="560" height="250" fill="#ffffff"/>']
    # (a) Chlamydomonas
    b.append('<path d="M95,70 q-25,-45 -55,-10 q-10,15 -25,5" fill="none" stroke="#37474f" stroke-width="2"/>')
    b.append('<path d="M105,70 q25,-45 55,-10 q10,15 25,5" fill="none" stroke="#37474f" stroke-width="2"/>')
    b.append('<ellipse cx="100" cy="135" rx="52" ry="68" fill="#c5e1a5" stroke="#558b2f" stroke-width="2"/>')
    b.append('<path d="M55,100 q-10,90 45,100 q55,-10 45,-100 q-10,-30 -20,-20 q10,40 -25,95 q-35,-55 -25,-95 q-10,-10 -20,20 z" fill="#43a047" opacity=".85"/>')
    b.append('<circle cx="92" cy="92" r="6" fill="#e8f5e9" stroke="#2e7d32"/><circle cx="108" cy="92" r="6" fill="#e8f5e9" stroke="#2e7d32"/>')
    b.append('<circle cx="100" cy="135" r="13" fill="#5d4037"/>')
    b.append('<ellipse cx="100" cy="182" rx="16" ry="9" fill="#a5d6a7" stroke="#1b5e20"/>')
    b.append('<ellipse cx="146" cy="120" rx="4" ry="7" fill="#d32f2f"/>')
    b.append(txt(100, 22, L['flagella'], 12, 'middle', 'bold'))
    b.append('<path d="M150,120 h22" stroke="#333"/>' + txt(175, 124, L['eyespot'], 12, 'start', 'bold'))
    b.append('<path d="M113,135 h70" stroke="#333"/>' + txt(186, 139, L['nucleus'], 12, 'start', 'bold'))
    b.append('<path d="M140,165 h43" stroke="#333"/>' + txt(186, 169, L['chloroplast'], 12, 'start', 'bold'))
    b.append(txt(100, 235, 'a', 14, 'middle', 'bold'))
    # (b) Volvox colonies
    for cx, cy, rr, kids in [(330, 120, 75, [(-25, -20), (20, -30), (-10, 25), (30, 15)]), (470, 125, 70, [(-15, -30), (15, 0), (-5, 30)])]:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="#f1f8e9" stroke="#7cb342" stroke-width="2"/>')
        for i in range(36):
            ang = 2 * math.pi * i / 36
            b.append(f'<circle cx="{cx + (rr-4)*math.cos(ang):.1f}" cy="{cy + (rr-4)*math.sin(ang):.1f}" r="2.2" fill="#558b2f"/>')
        for dx, dy in kids:
            b.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="15" fill="#9ccc65" stroke="#33691e"/>')
    b.append(txt(400, 235, 'b', 14, 'middle', 'bold'))
    b.append(txt(400, 22, L['daughter'], 11, 'middle', 'normal', '#475569', italic=True))
    return svg_wrap(''.join(b), 560, 250, L['title'])


CV_EN = dict(title='Figure 1.4: Unicellular Organization (a) Chlamydomonas and Colonial Organization (b) Volvox colonies',
             flagella='Flagella', eyespot='Eye spot', nucleus='Nucleus', chloroplast='Chloroplast', daughter='Volvox colonies with daughter colonies')
CV_UR = dict(title='شکل 1.4', flagella='فلیجیلا', eyespot='آئی اسپاٹ', nucleus='مرکزہ', chloroplast='کلوروپلاسٹ', daughter='والوکس کالونیاں')
CV_PS = dict(title='شکل 1.4', flagella='فلاجیلا', eyespot='د سترګې ټکی', nucleus='هسته', chloroplast='کلوروپلاسټ', daughter='د والواکس کلونۍ')


def mustard_frog(L):
    """Figure 1.5: Multicellular organization — mustard plant and frog."""
    b = []
    # mustard: stem, branches, leaves, yellow flowers
    b.append('<path d="M110,250 L110,60 M110,170 L70,120 M110,140 L150,95 M110,110 L90,70" stroke="#558b2f" stroke-width="4" fill="none"/>')
    b.append('<path d="M110,215 q-45,-5 -50,-35 q40,0 50,35 z M110,195 q45,-10 48,-38 q-40,5 -48,38 z" fill="#7cb342"/>')
    for x, y in [(110, 55), (102, 48), (118, 48), (90, 65), (82, 72), (150, 90), (158, 82), (68, 115), (60, 108), (110, 40)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#fdd835" stroke="#f9a825"/>')
    b.append(txt(70, 270, L['mustard'], 14, 'middle', 'bold', '#b71c1c'))
    # frog
    b.append('<ellipse cx="330" cy="170" rx="85" ry="50" fill="#6d4c41" stroke="#3e2723" stroke-width="2"/>')
    b.append('<ellipse cx="400" cy="140" rx="38" ry="30" fill="#795548" stroke="#3e2723" stroke-width="2"/>')
    b.append('<circle cx="410" cy="122" r="9" fill="#212121"/><circle cx="412" cy="120" r="3" fill="#fff"/>')
    b.append('<path d="M260,190 q-30,25 -10,45 h40 M300,212 q-5,25 15,30 h30 M370,205 q10,25 30,30" stroke="#3e2723" stroke-width="10" fill="none" stroke-linecap="round"/>')
    for x, y in [(300, 150), (330, 140), (350, 175), (310, 185), (280, 165)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#4e342e"/>')
    b.append(txt(390, 270, L['frog'], 14, 'middle', 'bold', '#b71c1c'))
    return svg_wrap(''.join(b), 480, 285, L['title'])


MF_EN = dict(title='Figure 1.5: Multicellular Organization', mustard='Mustard', frog='Frog')
MF_UR = dict(title='شکل 1.5', mustard='سرسوں', frog='مینڈک')
MF_PS = dict(title='شکل 1.5', mustard='شړشم', frog='چنګښه')
