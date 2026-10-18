# -*- coding: utf-8 -*-
"""Coded figures for Unit 9: 9.11 blood vessels, 9.12 major arteries and veins, 9.15 atherosclerosis."""
from bio9_tools import svg_wrap, txt
from unit4_figs2 import pointer


def lab(L, k):
    return L[k] if isinstance(L[k], list) else [L[k]]


def vessels(L):
    b = []
    # capillary bed inset
    b.append('<rect x="170" y="10" width="200" height="120" fill="#fff" stroke="#9e9e9e"/>')
    b.append('<path d="M175,40 C220,40 230,60 250,70 C270,80 300,60 365,50" stroke="#c62828" stroke-width="8" fill="none"/>')
    b.append('<path d="M175,110 C220,110 240,90 260,85 C290,80 320,100 365,110" stroke="#1565c0" stroke-width="8" fill="none"/>')
    for x in (230, 260, 290, 320):
        b.append(f'<path d="M{x},62 C{x+5},75 {x-5},85 {x},95" stroke="#7b1fa2" stroke-width="2" fill="none"/>')
    # artery (left), vein (right), capillary (bottom)
    b.append('<rect x="60" y="170" width="90" height="170" fill="#c62828"/><ellipse cx="105" cy="340" rx="45" ry="16" fill="#8e0000"/>')
    b.append('<ellipse cx="105" cy="340" rx="36" ry="12" fill="#ef9a9a"/><ellipse cx="105" cy="340" rx="24" ry="8" fill="#fce4ec"/><ellipse cx="105" cy="340" rx="18" ry="5" fill="#5d4037"/>')
    b.append('<rect x="390" y="170" width="90" height="170" fill="#1565c0"/><ellipse cx="435" cy="340" rx="45" ry="16" fill="#0d47a1"/>')
    b.append('<ellipse cx="435" cy="340" rx="40" ry="13" fill="#90caf9"/><ellipse cx="435" cy="340" rx="34" ry="10" fill="#e3f2fd"/>')
    b.append('<path d="M410,300 q25,30 50,0" stroke="#fff" stroke-width="4" fill="none"/>')
    b.append('<rect x="240" y="330" width="60" height="22" rx="11" fill="#9575cd"/><ellipse cx="270" cy="352" rx="30" ry="6" fill="#4527a0"/>')
    b.append(pointer(175, 40, 120, 30, lab(L, 'artery'), 'end') + pointer(365, 110, 420, 30, lab(L, 'vein')))
    b.append(pointer(230, 62, 215, 22, lab(L, 'arteriole'), 'middle') + pointer(290, 85, 300, 145, lab(L, 'capillaries'), 'middle') + pointer(330, 95, 345, 22, lab(L, 'venule'), 'middle'))
    b.append(pointer(148, 200, 200, 200, lab(L, 'conn')) + pointer(141, 340, 200, 225, lab(L, 'muscle')))
    b.append(pointer(122, 340, 200, 250, lab(L, 'lumen')) + pointer(129, 337, 200, 275, lab(L, 'endo')))
    b.append(pointer(445, 305, 500, 290, lab(L, 'valve')) + pointer(470, 338, 500, 360, lab(L, 'endo')))
    b.append(pointer(245, 340, 200, 390, lab(L, 'capillary'), 'end'))
    return svg_wrap('<g transform="translate(70,10)">' + ''.join(b) + '</g>', 680, 420, L['title'])


def body_map(L):
    b = ['<circle cx="200" cy="50" r="32" fill="#ffe0b2" stroke="#8d6e63"/>',
         '<path d="M150,95 L250,95 L280,140 L300,300 L270,300 L255,160 L250,330 L235,560 L210,560 L200,350 L190,560 L165,560 L150,330 L145,160 L130,300 L100,300 L120,140 Z" fill="#ffe0b2" stroke="#8d6e63"/>']
    R, B = '#c62828', '#1565c0'
    b.append(f'<path d="M206,150 C206,120 215,110 225,120 L212,345" stroke="{R}" stroke-width="7" fill="none"/>')  # aorta + dorsal aorta
    b.append(f'<path d="M210,125 L200,70 M215,118 L265,140 L285,290 M205,120 L135,140 L115,290" stroke="{R}" stroke-width="3" fill="none"/>')
    b.append(f'<path d="M212,345 L180,380 L178,555 M212,345 L225,380 L222,555" stroke="{R}" stroke-width="4" fill="none"/>')
    b.append(f'<path d="M193,345 L170,385 L168,555 M193,345 L215,385 L212,555" stroke="{B}" stroke-width="4" fill="none"/>')
    b.append(f'<path d="M193,345 L194,175 L192,120 L185,70" stroke="{B}" stroke-width="7" fill="none"/>')  # vena cava
    b.append('<path d="M175,160 Q200,140 225,165 Q215,195 200,200 Q180,190 175,160 Z" fill="#e57373" stroke="#b71c1c"/>')  # heart
    b.append(f'<path d="M205,160 L160,150 M200,165 L245,150" stroke="{B}" stroke-width="3"/><path d="M205,172 L160,172 M210,172 L248,170" stroke="{R}" stroke-width="3"/>')
    b.append('<ellipse cx="180" cy="260" rx="8" ry="14" fill="#8d6e63"/><ellipse cx="225" cy="260" rx="8" ry="14" fill="#8d6e63"/>')
    b.append(f'<path d="M212,255 L225,258" stroke="{R}" stroke-width="3"/><path d="M194,265 L180,262" stroke="{B}" stroke-width="3"/>')
    b.append(pointer(192, 110, 90, 90, lab(L, 'svc'), 'end') + pointer(225, 120, 320, 80, lab(L, 'aorta')))
    b.append(pointer(245, 150, 320, 140, lab(L, 'partery')) + pointer(248, 170, 320, 165, lab(L, 'pvein')))
    b.append(pointer(212, 210, 320, 195, lab(L, 'dorsal')) + pointer(225, 258, 320, 225, lab(L, 'rartery')) + pointer(220, 266, 320, 260, lab(L, 'rvein')))
    b.append(pointer(185, 180, 90, 210, lab(L, 'coronary'), 'end') + pointer(193, 300, 90, 280, lab(L, 'ivc'), 'end'))
    b.append(pointer(168, 480, 90, 480, lab(L, 'fvein'), 'end') + pointer(222, 480, 320, 480, lab(L, 'fartery')))
    return svg_wrap('<g transform="translate(90,0)">' + ''.join(b) + '</g>', 540, 575, L['title'])


def athero(L):
    b = ['<path d="M80,60 C40,100 40,200 100,270 C140,310 180,330 200,340 C240,320 290,280 300,220 C310,150 290,90 240,70 Z" fill="#e57373" stroke="#b71c1c" stroke-width="3"/>',
         '<path d="M120,10 L120,90 M120,280 L120,330" stroke="#1565c0" stroke-width="20"/><path d="M170,80 C170,40 200,20 240,25" stroke="#c62828" stroke-width="18" fill="none"/>',
         '<path d="M140,120 C190,140 230,180 240,240 C245,270 235,300 225,320" stroke="#b71c1c" stroke-width="5" fill="none"/>',
         '<ellipse cx="225" cy="290" rx="22" ry="34" fill="#424242" opacity=".75"/>']
    b.append('<circle cx="420" cy="120" r="95" fill="#fff" stroke="#555" stroke-width="2"/>')
    b.append('<clipPath id="athc"><circle cx="420" cy="120" r="93"/></clipPath><path d="M320,45 L520,195" stroke="#c62828" stroke-width="60" clip-path="url(#athc)"/>')
    b.append('<path d="M380,85 q30,10 40,40 L430,100 Z M440,150 q-25,-5 -30,-30 L420,160 Z" fill="#fdd835" stroke="#795548"/>')
    b.append('<path d="M232,232 L345,180" stroke="#555" stroke-dasharray="4 4"/>')
    b.append(pointer(425, 135, 470, 240, lab(L, 'plaque')) + pointer(225, 300, 300, 330, lab(L, 'dead')))
    return svg_wrap(''.join(b), 560, 360, L['title'])


FIG = {
    'vessels': {
        'en': dict(title='Figure 9.11: Blood vessels', artery='Artery', vein='Vein', arteriole='Arteriole', capillaries='Capillaries', venule='Venule', conn='Connective tissue', muscle='Smooth muscles', lumen='Lumen', endo='Endothelium', valve='Valve', capillary='Capillary'),
        'ur': dict(title='شکل 9.11', artery='شریان', vein='ورید', arteriole='آرٹیریول', capillaries='شعری نالیاں', venule='وینیول', conn='جوڑنے والی بافت', muscle='ہموار عضلات', lumen='لیومن (خلا)', endo='اینڈوتھیلیم', valve='والو', capillary='شعری نالی'),
        'ps': dict(title='شکل 9.11', artery='شریان', vein='ورید', arteriole='ارټیریول', capillaries='شعریه رګونه', venule='وینیول', conn='نښلوونکی نسج', muscle='اواره عضلې', lumen='لومن (تشه)', endo='اندوتیلیم', valve='والو', capillary='شعریه رګ'),
    },
    'body': {
        'en': dict(title='Figure 9.12: Major arteries and veins in human body', svc=['Superior', 'vena cava'], aorta='Aorta', partery='Pulmonary artery', pvein='Pulmonary vein', dorsal='Dorsal aorta', rartery='Renal artery', rvein='Renal vein', coronary=['Coronary', 'artery and', 'vein'], ivc=['Inferior', 'vena cava'], fvein='Femoral vein', fartery='Femoral artery'),
        'ur': dict(title='شکل 9.12', svc=['سپیریئر', 'وینا کیوا'], aorta='ایورٹا', partery='پلمونری شریان', pvein='پلمونری ورید', dorsal='ڈورسل ایورٹا', rartery='رینل شریان', rvein='رینل ورید', coronary=['کورونری', 'شریان اور', 'ورید'], ivc=['انفیریئر', 'وینا کیوا'], fvein='فیمورل ورید', fartery='فیمورل شریان'),
        'ps': dict(title='شکل 9.12', svc=['پورتنی', 'اجوف ورید'], aorta='اورټا', partery='سږی شریان', pvein='سږی ورید', dorsal='شاتنۍ اورټا', rartery='د پښتورګي شریان', rvein='د پښتورګي ورید', coronary=['اکلیلي', 'شریان او', 'ورید'], ivc=['ښکتنی', 'اجوف ورید'], fvein='فیمورل ورید', fartery='فیمورل شریان'),
    },
    'athero': {
        'en': dict(title='Figure 9.15: Atherosclerosis and resulting Myocardial infarction', plaque=['Plaque in', 'coronary artery'], dead='Dead tissue'),
        'ur': dict(title='شکل 9.15', plaque=['کورونری شریان', 'میں پلاک'], dead='مردہ بافت'),
        'ps': dict(title='شکل 9.15', plaque=['په اکلیلي شریان', 'کې پلاک'], dead='مړ نسج'),
    },
}
FN = dict(vessels=vessels, body=body_map, athero=athero)


def three(key):
    return [FN[key](FIG[key][lang]) for lang in ('en', 'ur', 'ps')]
