# -*- coding: utf-8 -*-
"""Coded SVG figures for Unit 5 (cell cycle, mitosis, meiosis)."""
import math
from bio9_tools import svg_wrap, txt
from unit4_figs import multiline
from unit4_figs2 import pointer

RED, BLUE = '#e53935', '#1e88e5'


def chrom(x, y, h=22, col=RED, rot=0, w=5, double=True):
    """X-shaped (two chromatid) or single chromosome centred at x,y."""
    if double:
        body = (f'<path d="M{-w},{-h/2} L{w},{h/2} M{w},{-h/2} L{-w},{h/2}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>'
                '<circle r="2.5" fill="#fdd835"/>')
    else:
        body = f'<path d="M0,{-h/2} L0,{h/2}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>'
    return f'<g transform="translate({x},{y}) rotate({rot})">{body}</g>'


def cell(cx, cy, r, stage, plant=False, label=None):
    """Schematic cell at a mitotic stage: interphase, early_pro, late_pro, meta, early_ana, late_ana, telo."""
    b = []
    pinch = stage in ('late_ana', 'telo') and not plant
    if plant:
        b.append(f'<rect x="{cx-r}" y="{cy-r*1.25}" width="{2*r}" height="{2.5*r}" rx="8" fill="#f1f8e9" stroke="#5d4037" stroke-width="3"/>')
    elif pinch:
        b.append(f'<path d="M{cx-r},{cy} a{r},{r*0.65} 0 1,1 {2*r},0 M{cx-r},{cy}" fill="none"/>')
        b.append(f'<ellipse cx="{cx}" cy="{cy - r*0.5}" rx="{r}" ry="{r*0.62}" fill="#f8bbd0" stroke="#c2185b" stroke-width="2"/>'
                 f'<ellipse cx="{cx}" cy="{cy + r*0.5}" rx="{r}" ry="{r*0.62}" fill="#f8bbd0" stroke="#c2185b" stroke-width="2"/>')
    else:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f8bbd0" stroke="#c2185b" stroke-width="2"/>')
    if stage == 'interphase':
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.45}" fill="#fce4ec" stroke="#880e4f" stroke-width="2"/><circle cx="{cx+r*0.12}" cy="{cy-r*0.1}" r="{r*0.12}" fill="#ad1457"/>')
        b.append(f'<path d="M{cx-r*0.3},{cy} q{r*0.15},{-r*0.2} {r*0.3},0 t{r*0.3},0 M{cx-r*0.25},{cy+r*0.2} q{r*0.2},{-r*0.15} {r*0.4},0" stroke="#7b1fa2" fill="none"/>')
    elif stage == 'early_pro':
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.5}" fill="none" stroke="#880e4f" stroke-dasharray="5 3" stroke-width="2"/>')
        b.append(chrom(cx - r*0.15, cy - r*0.1, r*0.35, RED, 20) + chrom(cx + r*0.15, cy + r*0.1, r*0.35, BLUE, -30))
        b.append(f'<circle cx="{cx - r*0.6}" cy="{cy - r*0.55}" r="4" fill="#2e7d32"/>' + ''.join(f'<path d="M{cx - r*0.6},{cy - r*0.55} l{8*math.cos(a):.1f},{8*math.sin(a):.1f}" stroke="#2e7d32"/>' for a in [0, 1, 2, 3, 4, 5]))
    elif stage == 'late_pro':
        b.append(f'<path d="M{cx},{cy - r*0.9} Q{cx - r*0.6},{cy} {cx},{cy + r*0.9} M{cx},{cy - r*0.9} Q{cx + r*0.6},{cy} {cx},{cy + r*0.9}" stroke="#9e9e9e" fill="none"/>')
        b.append(chrom(cx - r*0.2, cy, r*0.35, RED, 40) + chrom(cx + r*0.2, cy - r*0.15, r*0.35, BLUE, -20))
        b.append(f'<circle cx="{cx}" cy="{cy - r*0.9}" r="4" fill="#2e7d32"/><circle cx="{cx}" cy="{cy + r*0.9}" r="4" fill="#2e7d32"/>')
    elif stage == 'meta':
        for dx in (-0.5, -0.2, 0.2, 0.5):
            b.append(f'<path d="M{cx},{cy - r*0.92} L{cx + r*dx},{cy} L{cx},{cy + r*0.92}" stroke="#9e9e9e" fill="none"/>')
        b.append(chrom(cx - r*0.3, cy, r*0.3, RED, 90) + chrom(cx + r*0.3, cy, r*0.3, BLUE, 90))
    elif stage in ('early_ana', 'late_ana'):
        d = 0.35 if stage == 'early_ana' else 0.65
        for sgn in (-1, 1):
            for dx, col in ((-0.25, RED), (0.25, BLUE)):
                b.append(f'<path d="M{cx},{cy + sgn*r*0.92} L{cx + r*dx},{cy + sgn*r*d}" stroke="#9e9e9e"/>')
                b.append(f'<path d="M{cx + r*dx - 6},{cy + sgn*(r*d - 8)} L{cx + r*dx},{cy + sgn*r*d} L{cx + r*dx + 6},{cy + sgn*(r*d - 8)}" stroke="{col}" stroke-width="4" fill="none"/>')
    elif stage == 'telo':
        for sgn in (-1, 1):
            b.append(f'<circle cx="{cx}" cy="{cy + sgn*r*0.55}" r="{r*0.3}" fill="#fce4ec" stroke="#880e4f" stroke-width="2"/>')
            b.append(f'<path d="M{cx - r*0.15},{cy + sgn*r*0.55} q{r*0.1},-6 {r*0.3},0" stroke="#7b1fa2" fill="none" stroke-width="2"/>')
    if label:
        b.append(txt(cx, cy + r * (1.4 if plant else 1.15) + 12, label, 11, 'middle', 'bold'))
    return ''.join(b)


def interphase_fig(L):
    b = ['<circle cx="130" cy="120" r="100" fill="#f8bbd0" stroke="#c2185b" stroke-width="2"/>',
         '<circle cx="130" cy="120" r="55" fill="#fce4ec" stroke="#880e4f" stroke-width="3"/>', '<circle cx="145" cy="105" r="14" fill="#ad1457"/>',
         '<path d="M95,125 q15,-15 30,0 t30,0 M100,145 q20,-10 40,0" stroke="#7b1fa2" fill="none" stroke-width="2"/>']
    b.append(pointer(150, 100, 250, 50, L['nucleolus']) + pointer(182, 130, 250, 130, L['envelope']) + pointer(130, 145, 250, 190, L['chromatin']))
    return svg_wrap(''.join(b), 360, 240, L['title'])


IN_EN = dict(title='Figure 5.1: A cell during interphase', nucleolus='Nucleolus', envelope=['Nuclear', 'envlope'], chromatin='Chromatin')
IN_UR = dict(title='شکل 5.1', nucleolus='نیوکلیولس', envelope=['مرکزی', 'لفافہ'], chromatin='کرومیٹن')
IN_PS = dict(title='شکل 5.1', nucleolus='نیوکلیولس', envelope=['هستوي', 'پوښ'], chromatin='کروماټین')


def cycle_fig(L):
    cx, cy, R = 200, 190, 130
    b = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#ec407a" stroke-width="10" stroke-dasharray="680 140"/>']
    for ang in (-90, 10, 130, 210):
        x = cx + R * math.cos(math.radians(ang)); y = cy + R * math.sin(math.radians(ang))
        b.append(cell(x, y, 22, 'meta' if ang == -90 else 'interphase'))
    for ang in (-90, 10, 130, 210):
        x = cx + 0.9 * R * math.cos(math.radians(ang)); y = cy + 0.9 * R * math.sin(math.radians(ang))
        b.append(f'<path d="M{cx},{cy} L{x:.0f},{y:.0f}" stroke="#333"/>')
    b.append('<path d="M330,200 Q380,220 420,260" stroke="#ec407a" stroke-width="6" fill="none"/><polygon points="412,262 428,268 420,250" fill="#ec407a"/>')
    b.append('<path d="M215,62 Q300,70 360,150" stroke="#7e57c2" stroke-width="6" fill="none"/>' + cell(440, 160, 22, 'interphase') + cell(440, 285, 22, 'interphase'))
    b.append(multiline(150, 110, L['g2']) + multiline(240, 140, L['mitosis']) + multiline(-60, 200, L['s']) + multiline(200, 230, L['g1']) + multiline(400, 215, L['g0']))
    return svg_wrap('<g transform="translate(70,0)">' + ''.join(b) + '</g>', 580, 340, L['title'])


CY_EN = dict(title='Figure 5.2: Cell Cycle', g2=['G2', '• Preparation of', 'proteins for', 'division'], mitosis=['Mitosis', '• Cell Division'],
             s=['S', '• Duplication of', 'chromosomes', '(replication of DNA)', '• Growth', 'in size'], g1=['G1', '• Growth in size', '• Chemical changes', '• Synthesis of RNA,', 'ribosome and', 'enzymes'], g0=['G0', '• Division stopped'])
CY_UR = dict(title='شکل 5.2', g2=['G2', '• تقسیم کے لیے', 'پروٹینز کی تیاری'], mitosis=['مائٹوسس', '• خلوی تقسیم'], s=['S', '• کروموسومز کی', 'دوہرائی (DNA', 'کی نقل)', '• جسامت میں اضافہ'],
             g1=['G1', '• جسامت میں اضافہ', '• کیمیائی تبدیلیاں', '• RNA، رائبوسوم', 'اور انزائمز کی تیاری'], g0=['G0', '• تقسیم رک گئی'])
CY_PS = dict(title='شکل 5.2', g2=['G2', '• د وېش لپاره', 'د پروټینونو چمتو کول'], mitosis=['مایټوزس', '• حجروي وېش'], s=['S', '• د کروموزومونو', 'دوه چنده کېدل', '(د DNA نقل)', '• په اندازه کې وده'],
             g1=['G1', '• په اندازه کې وده', '• کیمیاوي بدلونونه', '• د RNA، رایبوزوم', 'او انزایمونو جوړول'], g0=['G0', '• وېش ودرېد'])


def stage_fig(stages, L, w=180):
    b = []
    for i, (stage, key) in enumerate(stages):
        b.append(cell(90 + i * w, 90, 60, stage, label=L.get(key, '')))
    if L.get('extra'):
        b.append(L['extra'](pointer))
    return svg_wrap(''.join(b), w * len(stages) + L.get('pad', 0), 190, L['title'])


def cytokinesis_plant(L):
    b = ['<rect x="80" y="20" width="160" height="200" rx="8" fill="#f1f8e9" stroke="#5d4037" stroke-width="4"/>',
         '<circle cx="160" cy="65" r="25" fill="#fce4ec" stroke="#880e4f"/><circle cx="160" cy="175" r="25" fill="#fce4ec" stroke="#880e4f"/>']
    b.append(''.join(f'<circle cx="{100 + i*15}" cy="120" r="4" fill="#ffca28" stroke="#f57f17"/>' for i in range(9)))
    b.append(pointer(105, 120, 30, 120, L['vesicles'], 'end') + pointer(200, 120, 270, 110, L['plate']) + pointer(238, 40, 270, 40, L['wall']))
    return svg_wrap('<g transform="translate(60,0)">' + ''.join(b) + '</g>', 420, 235, L['title'])


CK_EN = dict(title='Cytokinesis in plant cell', vesicles='Vesicles', plate='Cell plate', wall='Cell wall')
CK_UR = dict(title='پودے کے خلیے میں سائٹوکائنیسس', vesicles='ویسیکلز', plate='سیل پلیٹ', wall='خلوی دیوار')
CK_PS = dict(title='د بوټي په حجره کې سایټوکاینیزس', vesicles='ویسیکلونه', plate='د حجرې پلېټ', wall='د حجرې دېوال')


def test_mitosis_plant(title):
    b = []
    for i, st in enumerate(['interphase', 'late_pro', 'meta', 'late_ana', 'telo']):
        x = 60 + (i % 3) * 140; y = 80 + (i // 3) * 170
        b.append(cell(x, y, 45, st if st != 'late_ana' else 'early_ana', plant=True))
    return svg_wrap(''.join(b), 420, 340, title)


def chiasma_fig(L):
    b = []
    for i in range(5):
        x = 30 + i * 100
        cross = i >= 3
        b.append(f'<rect x="{x}" y="20" width="12" height="150" rx="6" fill="{RED}"/>')
        if i == 3:
            b.append(f'<path d="M{x+30},20 L{x+16},95 L{x+30},170" stroke="{BLUE}" stroke-width="12" fill="none" stroke-linecap="round"/>')
        else:
            b.append(f'<rect x="{x+(20 if i != 1 else 26)}" y="20" width="12" height="150" rx="6" fill="#90caf9"/>')
        if i == 4:
            b.append(f'<rect x="{x}" y="20" width="12" height="40" rx="6" fill="#90caf9"/><rect x="{x+20}" y="20" width="12" height="40" rx="6" fill="{RED}"/>')
        b.append(f'<rect x="{x-2}" y="92" width="36" height="6" fill="#ffb74d"/>')
        if i < 4:
            b.append(f'<path d="M{x+45},95 h35" stroke="#888" stroke-width="2"/><polygon points="{x+80},90 {x+88},95 {x+80},100" fill="#888"/>')
    return svg_wrap(''.join(b), 520, 190, L)


def meiosis1_fig(L):
    b = []
    heads = L['heads']
    for i in range(4):
        x = 75 + i * 150
        b.append(f'<rect x="{x-55}" y="5" width="110" height="28" fill="#4db6ac"/>' + multiline(x, 18, heads[i].split('|'), 'middle', 10))
        b.append(f'<circle cx="{x}" cy="120" r="55" fill="#a5d6a7" stroke="#2e7d32" stroke-width="2"/>' if i < 3 else
                 f'<ellipse cx="{x}" cy="95" rx="50" ry="32" fill="#a5d6a7" stroke="#2e7d32"/><ellipse cx="{x}" cy="150" rx="50" ry="32" fill="#a5d6a7" stroke="#2e7d32"/>')
    b.append(chrom(60, 110, 30, RED, 20) + chrom(75, 125, 30, BLUE, 30) + '<circle cx="50" cy="80" r="10" fill="none" stroke="#333"/>')
    b.append(chrom(205, 120, 26, RED, 90) + chrom(245, 120, 26, BLUE, 90) + '<path d="M225,68 V172" stroke="#9e9e9e"/>')
    b.append(chrom(375, 95, 22, RED, 0) + chrom(395, 95, 22, BLUE, 0) + chrom(375, 145, 22, BLUE, 0) + chrom(395, 145, 22, RED, 0))
    b.append(chrom(525, 95, 22, RED, 90) + chrom(525, 150, 22, BLUE, 90))
    b.append(pointer(50, 80, 30, 50, L['centrosome'], 'end') + pointer(60, 80, 90, 50, L['centrioles']) + pointer(70, 135, 20, 175, L['chiasmata'], 'end'))
    b.append(pointer(230, 100, 268, 60, L['plate']) + pointer(205, 110, 200, 68, L['centromere'], 'end') + pointer(397, 150, 440, 182, L['sister']) + pointer(570, 122, 590, 60, L['furrow']))
    caps = L['caps']
    for i in range(4):
        b.append(multiline(75 + i * 150, 215, caps[i].split('|'), 'middle', 9))
    return svg_wrap('<g transform="translate(70,0)">' + ''.join(b) + '</g>', 780, 265, L['title'])


M1_EN = dict(title='Figure 5.4: Events of Meiosis I', heads=['Prophase I', 'Metaphase I', 'Anaphase I', 'Telophase I|and Cytokinesis'],
             centrosome='Centrosome', centrioles='Centrioles', chiasmata='Chiasmata', plate=['Metaphase', 'plate'], centromere=['Centromere', '(with kinetachore)'], sister=['Sister', 'chromatids'], furrow='Cleavage furrow',
             caps=['The chromosomes condense, and the|nuclear envelope breaks down.|Crossing-over occurs.', 'Pairs of homologous|chromosomes move|to the equator of the cell.',
                   'Homologous chromosomes move|to the oppisite poles of the cell', 'Chromosomes gather|at the poles of the cells.|The cytoplasm divides.'])
M1_UR = dict(title='شکل 5.4', heads=['پروفیز I', 'میٹافیز I', 'اینافیز I', 'ٹیلوفیز I|اور سائٹوکائنیسس'], centrosome='سینٹروسوم', centrioles='سینٹریولز', chiasmata='کائزمیٹا',
             plate=['میٹافیز', 'پلیٹ'], centromere=['سینٹرومیئر', '(کائنیٹوکور کے ساتھ)'], sister=['سسٹر', 'کرومیٹڈز'], furrow='کلیویج فرو',
             caps=['کروموسومز گاڑھے ہوتے ہیں، مرکزی|لفافہ ٹوٹ جاتا ہے۔ کراسنگ اوور ہوتا ہے۔', 'ہومولوگس کروموسومز کے جوڑے|خلیے کے خطِ استوا پر آتے ہیں۔',
                   'ہومولوگس کروموسومز خلیے کے|مخالف قطبین کی طرف جاتے ہیں', 'کروموسومز قطبین پر جمع ہوتے|ہیں۔ سائٹوپلازم تقسیم ہوتا ہے۔'])
M1_PS = dict(title='شکل 5.4', heads=['پروفېز I', 'میټافېز I', 'اینافېز I', 'ټیلوفېز I|او سایټوکاینیزس'], centrosome='سنټروزوم', centrioles='سنټریولونه', chiasmata='کیازماټا',
             plate=['میټافېز', 'پلېټ'], centromere=['سنټرومیر', '(له کاینیټوکور سره)'], sister=['خور', 'کروماټیډونه'], furrow='د وېش کنده',
             caps=['کروموزومونه ټینګېږي، هستوي پوښ|ماتېږي. کراسنګ اوور کېږي.', 'د همولوګو کروموزومونو جوړې|د حجرې استوا ته ځي.',
                   'همولوګ کروموزومونه د حجرې|مخالفو قطبونو ته ځي', 'کروموزومونه په قطبونو کې|راټولېږي. سایټوپلازم وېشل کېږي.'])


def meiosis2_fig(L):
    b = []
    heads = L['heads']
    b.append(txt(70, 14, L['m1'], 11, 'middle', 'bold', '#1565c0') + txt(200, 14, L['m2'], 11, 'middle', 'bold', '#1565c0'))
    for i, h in enumerate(heads):
        b.append(multiline(70 + i * 120, 30, h.split('|'), 'middle', 10))
    for row in (0, 1):
        y = 100 + row * 175
        b.append(f'<ellipse cx="70" cy="{y}" rx="45" ry="40" fill="#f8bbd0" stroke="#4fc3f7" stroke-width="3"/>' + chrom(60, y, 20, RED, 30) + chrom(80, y, 20, BLUE, -30))
        for i, st in enumerate(['late_pro', 'meta', 'early_ana', 'telo']):
            b.append(cell(190 + i * 120, y, 40, st))
            b.append(f'<path d="M{120 + i*120},{y} h18" stroke="#29b6f6" stroke-width="4"/><polygon points="{138 + i*120},{y-5} {146 + i*120},{y} {138 + i*120},{y+5}" fill="#29b6f6"/>')
    b.append(pointer(70, 140, 30, 175, L['furrow'], 'end'))
    caps = L['caps']
    for i in range(4):
        b.append(multiline(190 + i * 120, 158, caps[i].split('|'), 'middle', 9))
    b.append(multiline(70, 330, L['two'].split('|'), 'middle', 9))
    return svg_wrap('<g transform="translate(100,0)">' + ''.join(b) + '</g>', 780, 370, L['title'])


M2_EN = dict(title='Figure 5.5: Events of Meiosis II', m1='Meiosis-I', m2='Meiosis-II', heads=['Telophase &|Cytokinesis', 'Prophase-II', 'Metaphase-II', 'Anaphase-II', 'Telophase-II'],
             furrow='Cleavage furrow', caps=['A new spindle|forms around|the chromosomes.', 'Chromosomes line|up at the equator.', 'Sister chromatids|separate', 'A nuclear envelope forms|around each set of chromosomes.|The cytoplasm divides|and four Haploid daughter|cells form.'],
             two='Two haploid cells|form: chromosomes|are still double')
M2_UR = dict(title='شکل 5.5', m1='مییوسس I', m2='مییوسس II', heads=['ٹیلوفیز اور|سائٹوکائنیسس', 'پروفیز II', 'میٹافیز II', 'اینافیز II', 'ٹیلوفیز II'], furrow='کلیویج فرو',
             caps=['کروموسومز کے گرد|نیا اسپنڈل بنتا ہے۔', 'کروموسومز خطِ استوا|پر قطار بناتے ہیں۔', 'سسٹر کرومیٹڈز|الگ ہوتے ہیں', 'ہر سیٹ کے گرد مرکزی|لفافہ بنتا ہے۔ سائٹوپلازم|تقسیم ہو کر چار ہیپلائیڈ|خلیے بنتے ہیں۔'],
             two='دو ہیپلائیڈ خلیے|بنتے ہیں: کروموسومز|ابھی دوہرے ہیں')
M2_PS = dict(title='شکل 5.5', m1='مییوزس I', m2='مییوزس II', heads=['ټیلوفېز او|سایټوکاینیزس', 'پروفېز II', 'میټافېز II', 'اینافېز II', 'ټیلوفېز II'], furrow='د وېش کنده',
             caps=['د کروموزومونو شاوخوا|نوی سپنډل جوړېږي.', 'کروموزومونه په استوا|کې قطار کېږي.', 'خور کروماټیډونه|جلا کېږي', 'د هرې ټولګې شاوخوا هستوي|پوښ جوړېږي. سایټوپلازم|وېشل کېږي او څلور هاپلویډ|حجرې جوړېږي.'],
             two='دوه هاپلویډ حجرې|جوړېږي: کروموزومونه|لا دوه ګوني دي')


def test_meiosis(title):
    b = []
    row1 = ['early_pro', 'late_pro', 'meta', 'early_ana', 'telo']
    for i, st in enumerate(row1):
        b.append(cell(50 + i * 100, 55, 40, st))
    for r in (1, 2):
        for i, st in enumerate(['telo', 'late_pro', 'meta', 'early_ana', 'interphase']):
            b.append(cell(50 + i * 100, 55 + r * 95, 32, st))
    return svg_wrap(''.join(b), 500, 300, title)
