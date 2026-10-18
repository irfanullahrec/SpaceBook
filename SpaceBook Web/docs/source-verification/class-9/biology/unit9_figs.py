# -*- coding: utf-8 -*-
"""Coded figures for Unit 9 (Figures 9.5-9.10 and Table 9.1 cell row). Each takes a label dict L."""
import math
from bio9_tools import svg_wrap, txt
from unit4_figs2 import pointer

BLUE = '#1e63b5'
RED = '#d32f2f'


def lab(L, k):
    return L[k] if isinstance(L[k], list) else [L[k]]


# ---- Figure 9.5 translocation of food ----------------------------------------
def translocation(L):
    b = ['<rect x="60" y="30" width="60" height="280" fill="#bbdefb" stroke="#1565c0"/>',
         '<rect x="150" y="30" width="60" height="280" fill="#ffe0b2" stroke="#e65100"/>',
         '<rect x="172" y="40" width="16" height="260" fill="#ef5350"/>']
    for y in (90, 150, 210, 270):
        b.append(f'<path d="M150,{y} h60" stroke="#e65100" stroke-width="2"/>')
    b.append('<ellipse cx="245" cy="70" rx="28" ry="18" fill="#a5d6a7" stroke="#2e7d32"/>')
    b.append('<ellipse cx="230" cy="110" rx="18" ry="14" fill="#c5e1a5" stroke="#558b2f"/>')
    b.append('<ellipse cx="245" cy="280" rx="28" ry="18" fill="#d7ccc8" stroke="#6d4c41"/>')
    for y in (60, 110, 160, 210, 260):
        b.append(f'<circle cx="180" cy="{y}" r="5" fill="#fff59d" stroke="#f57f17"/>')
    b.append(f'<path d="M180,70 v200" stroke="#b71c1c" stroke-width="3"/><path d="M174,262 l6,12 l6,-12 z" fill="#b71c1c"/>')
    b.append(f'<path d="M120,70 h28" stroke="{BLUE}" stroke-width="3"/><path d="M146,64 l8,6 l-8,6 z" fill="{BLUE}"/>' + txt(132, 62, 'H₂O', 10, 'middle', 'bold'))
    b.append(f'<path d="M150,270 h-28" stroke="{BLUE}" stroke-width="3"/><path d="M124,264 l-8,6 l8,6 z" fill="{BLUE}"/>' + txt(132, 262, 'H₂O', 10, 'middle', 'bold'))
    b.append(txt(90, 22, L['xylem'], 12, 'middle', 'bold') + txt(180, 22, L['phloem'], 12, 'middle', 'bold'))
    b.append(pointer(270, 70, 300, 55, lab(L, 'companion')) + pointer(248, 110, 300, 105, lab(L, 'meso')))
    b.append(pointer(185, 160, 300, 155, lab(L, 'food')) + pointer(210, 210, 300, 210, lab(L, 'sieve')))
    b.append(pointer(272, 280, 300, 275, lab(L, 'root')))
    return svg_wrap(''.join(b), 440, 320, L['title'])


# ---- Figure 9.6 composition of blood -----------------------------------------
def composition(L):
    b = ['<rect x="30" y="20" width="44" height="180" rx="20" fill="#fff" stroke="#555"/><rect x="33" y="50" width="38" height="146" rx="18" fill="#c62828"/>',
         '<rect x="110" y="20" width="44" height="180" rx="20" fill="#fff" stroke="#555"/><rect x="113" y="50" width="38" height="70" fill="#fff59d"/><rect x="113" y="120" width="38" height="76" rx="18" fill="#c62828"/>']
    b.append(txt(18, 120, L['whole'], 11, 'middle', 'bold', extra=' transform="rotate(-90 18 120)"'))
    b.append('<path d="M82,110 h20" stroke="#c62828" stroke-width="3"/>')
    b.append('<rect x="170" y="45" width="330" height="80" fill="#fff9c4"/><rect x="170" y="125" width="330" height="75" fill="#f8bbd0"/>')
    b.append('<path d="M160,55 h6 v60 h-6 M160,125 h6 v70 h-6" stroke="#333" fill="none"/>')
    b.append(txt(178, 82, L['plasma'], 12, 'start', 'bold') + txt(178, 98, '55%', 12, 'start', 'bold'))
    b.append('<path d="M250,88 L320,60 M250,88 L320,88 M250,88 L320,116" stroke="#333"/>')
    b.append(txt(325, 64, L['water'], 12, 'start', 'bold') + txt(325, 92, L['proteins'], 12, 'start', 'bold') + txt(325, 120, L['others'], 12, 'start', 'bold'))
    b.append(''.join(txt(178, 148 + i * 14, t, 11, 'start', 'bold') for i, t in enumerate(lab(L, 'cells'))) + txt(178, 190, '45%', 11, 'start', 'bold'))
    b.append('<path d="M270,165 L320,145 M270,165 L320,190" stroke="#333"/>')
    b.append(''.join(txt(325, 145 + i * 14, t, 11, 'start', 'bold') for i, t in enumerate(lab(L, 'wbc'))) + txt(325, 194, L['rbc'], 11, 'start', 'bold'))
    return svg_wrap(''.join(b), 520, 215, L['title'])


# ---- Figure 9.7 blood cells in a vessel ---------------------------------------
def rbc(cx, cy, r=16):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e53935"/><circle cx="{cx}" cy="{cy}" r="{r*0.45}" fill="#ef9a9a"/>')


def blood_cells(L):
    b = ['<path d="M20,60 C150,20 300,40 420,90 L420,230 C300,190 150,200 20,240 Z" fill="#fce4ec" stroke="#ad1457" stroke-width="3"/>']
    for cx, cy in ((80, 110), (140, 170), (220, 120), (300, 170), (360, 130), (110, 200), (250, 190)):
        b.append(rbc(cx, cy))
    b.append('<circle cx="180" cy="150" r="20" fill="#e1bee7" stroke="#6a1b9a"/><path d="M172,142 q8,-6 14,2 q-4,10 -12,8 z" fill="#4a148c"/>')
    b.append('<circle cx="330" cy="200" r="20" fill="#e1bee7" stroke="#6a1b9a"/><circle cx="330" cy="200" r="9" fill="#4a148c"/>')
    for cx, cy in ((60, 160), (270, 95), (390, 180)):
        b.append(f'<path d="M{cx},{cy} l6,-4 l6,4 l-3,6 l-6,0 z" fill="#ffb74d"/>')
    b.append(pointer(200, 50, 230, 18, lab(L, 'vessel')) + pointer(400, 120, 450, 60, lab(L, 'plasma')))
    b.append(pointer(60, 160, 0, 290, lab(L, 'platelet')) + pointer(180, 160, 150, 290, lab(L, 'wbc')) + pointer(250, 200, 300, 290, lab(L, 'rbc')))
    return svg_wrap('<g transform="translate(20,0)">' + ''.join(b) + '</g>', 540, 325, L['title'])


# ---- Figure 9.8 formation of clot ---------------------------------------------
def clot(L):
    def vessel(x, damaged):
        v = f'<rect x="{x}" y="60" width="220" height="110" fill="#f8bbd0"/><rect x="{x}" y="40" width="220" height="20" fill="#e57373"/><rect x="{x}" y="170" width="220" height="20" fill="#e57373"/>'
        if damaged:
            v += f'<rect x="{x+90}" y="38" width="40" height="24" fill="#fff"/>'
        return v
    b = [vessel(20, True), vessel(300, True)]
    for i, (cx, cy) in enumerate(((60, 110), (100, 140), (150, 90), (190, 130), (130, 160), (80, 80))):
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="14" ry="6" fill="#6d4c41" transform="rotate({i*30} {cx} {cy})"/>')
    for i in range(14):
        cx = 360 + (i % 7) * 15
        cy = 40 + (i // 7) * 16
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="10" ry="5" fill="#6d4c41" transform="rotate({i*25} {cx} {cy})"/>')
    b.append('<path d="M350,35 L480,60 M355,60 L470,30 M370,25 L460,70" stroke="#fff3e0" stroke-width="1.5"/>')
    b.append('<path d="M250,115 h30" stroke="#333" stroke-width="3"/>')
    b.append(pointer(80, 80, 40, 20, lab(L, 'platelet'), 'end') + pointer(130, 40, 150, 10, lab(L, 'damaged')) + pointer(410, 35, 440, 10, lab(L, 'clot')))
    return svg_wrap('<g transform="translate(40,10)">' + ''.join(b) + '</g>', 600, 210, L['title'])


# ---- Table 9.1 red-cell row -----------------------------------------------------
def abo_cells(L):
    b = []
    for i, (key, a, bb) in enumerate((('A', True, False), ('B', False, True), ('AB', True, True), ('O', False, False))):
        cx = 70 + i * 130
        b.append(f'<circle cx="{cx}" cy="70" r="34" fill="#c62828"/><circle cx="{cx}" cy="70" r="15" fill="#4e342e"/>')
        for k in range(10):
            ang = math.radians(k * 36)
            x, y = cx + 40 * math.cos(ang), 70 + 40 * math.sin(ang)
            if a and (not bb or k % 2 == 0):
                b.append(f'<path d="M{x-4},{y+4} L{x},{y-4} L{x+4},{y+4} Z" fill="#c2185b"/>')
            elif bb:
                b.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#00897b"/>')
        b.append(txt(cx, 135, L['g' + key], 13, 'middle', 'bold'))
    b.append('<path d="M20,160 l8,-12 l8,12 z" fill="#c2185b"/>' + txt(44, 160, L['antA'], 11, 'start', 'bold'))
    b.append('<circle cx="250" cy="155" r="5" fill="#00897b"/>' + txt(262, 160, L['antB'], 11, 'start', 'bold'))
    return svg_wrap(''.join(b), 540, 175, L['title'])


# ---- Figure 9.9 heart -----------------------------------------------------------
def heart_shape():
    b = ['<path d="M150,120 C110,150 110,250 170,320 C210,370 250,390 270,400 C300,380 360,340 380,280 C400,210 380,140 330,120 Z" fill="#ef9a9a" stroke="#b71c1c" stroke-width="3"/>']
    b.append('<path d="M150,120 C110,150 110,250 170,320 C200,350 230,370 255,385 L265,170 Z" fill="#90caf9" stroke="#0d47a1" stroke-width="2"/>')
    b.append('<path d="M265,170 L262,380" stroke="#6d4c41" stroke-width="6"/>')  # septum
    b.append('<path d="M140,200 h120 M268,205 h110" stroke="#fff" stroke-width="4"/>')  # AV valve planes
    b.append('<path d="M175,10 L175,130 M175,330 L175,420" stroke="#1565c0" stroke-width="22"/>')  # venae cavae
    b.append('<path d="M250,150 C250,90 260,40 310,30 C350,25 360,60 350,90" stroke="#c62828" stroke-width="24" fill="none"/>')  # aorta
    b.append('<path d="M225,160 C220,110 240,80 270,70 L330,60" stroke="#1565c0" stroke-width="16" fill="none"/>')  # pulmonary artery
    b.append('<path d="M330,150 L410,130 M330,175 L410,175" stroke="#c62828" stroke-width="12"/>')  # pulmonary veins
    b.append('<path d="M200,198 l12,10 l12,-10 M300,203 l12,10 l12,-10" stroke="#fff" stroke-width="3" fill="none"/>')
    b.append('<path d="M240,160 q8,-10 16,0 M268,160 q8,-10 16,0" stroke="#fff" stroke-width="3" fill="none"/>')
    return ''.join(b)


def heart(L):
    b = [heart_shape()]
    b.append(pointer(300, 18, 300, -30, lab(L, 'aorta'), 'middle'))
    b.append(pointer(330, 62, 430, 45, lab(L, 'partery')) + pointer(405, 132, 430, 110, lab(L, 'pvein')))
    b.append(pointer(350, 180, 430, 190, lab(L, 'latrium')) + pointer(320, 210, 430, 245, lab(L, 'bicuspid')))
    b.append(pointer(340, 290, 430, 290, lab(L, 'lventricle')))
    b.append(pointer(175, 60, 100, 50, lab(L, 'svc'), 'end') + pointer(150, 160, 100, 140, lab(L, 'ratrium'), 'end'))
    b.append(pointer(200, 205, 100, 215, lab(L, 'tricuspid'), 'end') + pointer(170, 270, 100, 265, lab(L, 'rventricle'), 'end'))
    b.append(pointer(175, 400, 100, 360, lab(L, 'ivc'), 'end'))
    b.append(pointer(248, 158, 240, 430, lab(L, 'semilunar'), 'middle') + pointer(263, 350, 330, 430, lab(L, 'septum'), 'middle'))
    return svg_wrap('<g transform="translate(130,60)">' + ''.join(b) + '</g>', 760, 520, L['title'])


# ---- Figure 9.10 cardiac cycle ---------------------------------------------------
def cycle_heart(dx, systole):
    g = [f'<g transform="translate({dx},0) scale(.6)">', heart_shape()]
    if systole:  # AV valves closed (solid), semilunar open
        g.append('<path d="M195,200 h40 M295,205 h40" stroke="#212121" stroke-width="6"/>')
    else:  # semilunar closed
        g.append('<path d="M238,158 h22 M266,158 h22" stroke="#212121" stroke-width="6"/>')
    g.append('</g>')
    return ''.join(g)


def cardiac(L):
    b = [cycle_heart(0, True), cycle_heart(270, False)]
    b.append(pointer(125, 122, 60, 290, lab(L, 'avclosed'), 'end'))
    b.append(pointer(430, 95, 520, 120, lab(L, 'slclosed')))
    b.append(txt(160, 275, L['systole'], 14, 'middle', 'bold') + txt(430, 275, L['diastole'], 14, 'middle', 'bold'))
    return svg_wrap('<g transform="translate(60,10)">' + ''.join(b) + '</g>', 680, 340, L['title'])


FIG = {
    'translocation': {
        'en': dict(title='Figure 9.5: The translocation of Food in Plants', xylem='Xylem', phloem='Phloem', companion=['Companion', 'cell'], meso=['Mesophyll', 'cell (source)'], food=['Food', 'molecules'], sieve='Sieve tubes', root=['Root cell', '(sink)']),
        'ur': dict(title='شکل 9.5', xylem='زائلم', phloem='فلوئم', companion=['کمپینین', 'خلیہ'], meso=['میزوفل خلیہ', '(منبع)'], food=['خوراک کے', 'مالیکیولز'], sieve='سیو ٹیوبز', root=['جڑ کا خلیہ', '(سنک)']),
        'ps': dict(title='شکل 9.5', xylem='زایلم', phloem='فلویم', companion=['ملګرې', 'حجره'], meso=['میزوفیل حجره', '(سرچینه)'], food=['د خوړو', 'مالیکولونه'], sieve='غلبیلي نلونه', root=['د ریښې حجره', '(مصرف ځای)']),
    },
    'composition': {
        'en': dict(title='Figure 9.6: Composition of Blood', whole='Whole blood', plasma='Plasma', water='Water: 90%', proteins='Proteins: 7%', others='Others: 3%', cells=['Cells &', 'Cell-like bodies'], wbc=['White blood cells', '& Platelets: 0.9%'], rbc='Red blood cells: 99.1%'),
        'ur': dict(title='شکل 9.6', whole='پورا خون', plasma='پلازما', water='پانی: 90%', proteins='پروٹینز: 7%', others='دیگر: 3%', cells=['خلیے اور', 'خلیہ نما اجسام'], wbc=['سفید خونی خلیے', 'اور پلیٹ لیٹس: 0.9%'], rbc='سرخ خونی خلیے: 99.1%'),
        'ps': dict(title='شکل 9.6', whole='ټوله وینه', plasma='پلازما', water='اوبه: 90%', proteins='پروټینونه: 7%', others='نور: 3%', cells=['حجرې او', 'حجرې ته ورته اجسام'], wbc=['سپینې وینې حجرې', 'او پلېټلېټونه: 0.9%'], rbc='سرې وینې حجرې: 99.1%'),
    },
    'cells': {
        'en': dict(title='Figure 9.7: Composition of Blood', vessel='Blood vessel', plasma='Plasma', platelet='Platelet', wbc=['White', 'blood cell'], rbc=['Red', 'blood cell']),
        'ur': dict(title='شکل 9.7', vessel='خون کی نالی', plasma='پلازما', platelet='پلیٹ لیٹ', wbc=['سفید', 'خونی خلیہ'], rbc=['سرخ', 'خونی خلیہ']),
        'ps': dict(title='شکل 9.7', vessel='د وینې رګ', plasma='پلازما', platelet='پلېټلېټ', wbc=['سپینه', 'وینې حجره'], rbc=['سره', 'وینې حجره']),
    },
    'clot': {
        'en': dict(title='Figure 9.8: Formation of clot by platelets', platelet='Platelet', damaged=['Damaged', 'blood vessel'], clot='Clot'),
        'ur': dict(title='شکل 9.8', platelet='پلیٹ لیٹ', damaged=['متاثرہ', 'خون کی نالی'], clot='لوتھڑا'),
        'ps': dict(title='شکل 9.8', platelet='پلېټلېټ', damaged=['زیانمن', 'د وینې رګ'], clot='پرنډ'),
    },
    'abo': {
        'en': dict(title='Table 9.1: Red blood cell type', gA='Group A', gB='Group B', gAB='Group AB', gO='Group O', antA='A antigen', antB='B antigen'),
        'ur': dict(title='جدول 9.1', gA='گروپ A', gB='گروپ B', gAB='گروپ AB', gO='گروپ O', antA='A اینٹی جن', antB='B اینٹی جن'),
        'ps': dict(title='جدول 9.1', gA='ګروپ A', gB='ګروپ B', gAB='ګروپ AB', gO='ګروپ O', antA='A انټي جن', antB='B انټي جن'),
    },
    'heart': {
        'en': dict(title='Figure 9.9: Human heart structure and blood circulation', aorta=['Aorta', 'takes oxygentaed blood to body parts.'], partery=['Pulmonary arteries', 'take blood to lungs.'], pvein=['Pulmonary veins', 'carry blood from', 'lungs to left atrium.'], latrium=['Left atrium', 'sends blood to left', 'ventricle.'], bicuspid='Bicuspid valve', lventricle=['Left ventricle', 'sends blood to', 'aorta.'], svc=['Superior vena cava', 'brings deoxygenated', 'blood from upper body', 'to right atrium.'], ratrium=['Right atrium', 'sends blood to', 'right ventricle.'], tricuspid='Tricuspid valve', rventricle=['Right ventricle', 'sends blood to', 'pulmonary arteries.'], ivc=['Inferior vena cava', 'brings deoxygenated', 'blood from lower body', 'to right atrium.'], semilunar=['Semilunar', 'valves'], septum='Septum'),
        'ur': dict(title='شکل 9.9', aorta=['ایورٹا', 'آکسیجن والا خون جسم کو لے جاتی ہے۔'], partery=['پلمونری شریانیں', 'خون پھیپھڑوں کو لے جاتی ہیں۔'], pvein=['پلمونری وریدیں', 'پھیپھڑوں سے خون', 'بائیں ایٹریم کو لاتی ہیں۔'], latrium=['بایاں ایٹریم', 'خون بائیں وینٹریکل', 'کو بھیجتا ہے۔'], bicuspid='بائی کسپڈ والو', lventricle=['بایاں وینٹریکل', 'خون ایورٹا', 'کو بھیجتا ہے۔'], svc=['سپیریئر وینا کیوا', 'جسم کے اوپری حصے سے', 'بغیر آکسیجن والا خون', 'دائیں ایٹریم کو لاتی ہے۔'], ratrium=['دایاں ایٹریم', 'خون دائیں وینٹریکل', 'کو بھیجتا ہے۔'], tricuspid='ٹرائی کسپڈ والو', rventricle=['دایاں وینٹریکل', 'خون پلمونری', 'شریانوں کو بھیجتا ہے۔'], ivc=['انفیریئر وینا کیوا', 'جسم کے نچلے حصے سے', 'بغیر آکسیجن والا خون', 'دائیں ایٹریم کو لاتی ہے۔'], semilunar=['سیمی لیونر', 'والوز'], septum='سیپٹم'),
        'ps': dict(title='شکل 9.9', aorta=['ابهر (اورټا)', 'اکسیجن لرونکې وینه بدن ته وړي.'], partery=['سږي شریانونه', 'وینه سږو ته وړي.'], pvein=['سږي وریدونه', 'له سږو وینه', 'کیڼ اذین ته راوړي.'], latrium=['کیڼ اذین', 'وینه کیڼ بطین ته', 'لېږي.'], bicuspid='بای کسپډ والو', lventricle=['کیڼ بطین', 'وینه اورټا ته', 'لېږي.'], svc=['پورتنی اجوف ورید', 'د بدن له پورتنۍ برخې', 'بې اکسیجنه وینه', 'ښي اذین ته راوړي.'], ratrium=['ښی اذین', 'وینه ښي بطین ته', 'لېږي.'], tricuspid='ټرای کسپډ والو', rventricle=['ښی بطین', 'وینه سږي', 'شریانونو ته لېږي.'], ivc=['ښکتنی اجوف ورید', 'د بدن له ښکتنۍ برخې', 'بې اکسیجنه وینه', 'ښي اذین ته راوړي.'], semilunar=['نیم سپوږمۍ', 'والونه'], septum='سپټم'),
    },
    'cardiac': {
        'en': dict(title='Figure 9.10: One Cardiac Cycle / Heartbeat', avclosed=['Tricuspid and', 'bicuspid closed'], slclosed=['Semilunar', 'closed'], systole='Systole', diastole='Diastole'),
        'ur': dict(title='شکل 9.10', avclosed=['ٹرائی کسپڈ اور', 'بائی کسپڈ بند'], slclosed=['سیمی لیونر', 'بند'], systole='سسٹولی', diastole='ڈایاسٹولی'),
        'ps': dict(title='شکل 9.10', avclosed=['ټرای کسپډ او', 'بای کسپډ تړلي'], slclosed=['نیم سپوږمۍ', 'تړلي'], systole='سیسټول', diastole='ډیاسټول'),
    },
}
FN = dict(translocation=translocation, composition=composition, cells=blood_cells, clot=clot, abo=abo_cells, heart=heart, cardiac=cardiac)


def three(key):
    return [FN[key](FIG[key][lang]) for lang in ('en', 'ur', 'ps')]
