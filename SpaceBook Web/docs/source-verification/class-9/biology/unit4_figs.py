# -*- coding: utf-8 -*-
"""Coded SVG figures for Unit 4 (Figures 4.4, 4.5, 4.7, 4.8, 4.9). Label dicts per language."""
import math, random
from bio9_tools import svg_wrap, txt


def lab(x1, y1, x2, y2, text, anchor='start', size=11):
    tx = x2 + (4 if anchor == 'start' else -4)
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#b71c1c" stroke-width="1"/>' + txt(tx, y2 + 4, text, size, anchor, 'bold', '#212121')


def multiline(x, y, lines, anchor='start', size=11):
    return ''.join(txt(x, y + i * 13, ln, size, anchor, 'bold', '#212121') for i, ln in enumerate(lines))


def microscope_mechanisms(L):
    b = []
    # light microscope column
    b.append('<rect x="95" y="20" width="16" height="30" fill="#37474f"/><path d="M103,5 l-8,15 h16 z" fill="#37474f"/>')
    b.append('<path d="M103,60 L103,300" stroke="#f9a825" stroke-width="10" opacity=".5"/>')
    for y in (110, 160, 250):
        b.append(f'<ellipse cx="103" cy="{y}" rx="30" ry="7" fill="#e3f2fd" stroke="#1565c0"/>')
    b.append('<rect x="80" y="196" width="46" height="6" fill="#5d4037"/><circle cx="103" cy="305" r="9" fill="#e53935"/>')
    b.append('<path d="M68,110 L35,140 M68,160 L35,140 M68,250 L35,140" stroke="#222"/>' + multiline(5, 135, L['optical'], size=11))
    b.append(lab(126, 199, 150, 215, L['sample']))
    b.append('<path d="M94,305 L60,320" stroke="#222"/>' + multiline(10, 320, L['source'], size=11))
    b.append(multiline(103, 360, L['lm'], 'middle'))
    # TEM column
    b.append('<rect x="210" y="10" width="110" height="320" fill="#fff8e1" stroke="#333"/>')
    b.append('<path d="M265,20 L245,60 L285,60 Z" fill="#ec407a" opacity=".6"/><path d="M265,60 L265,310" stroke="#ec407a" stroke-width="6" opacity=".5"/>')
    for y in (80, 140, 190, 240):
        b.append(f'<rect x="245" y="{y}" width="8" height="18" fill="#263238"/><rect x="277" y="{y}" width="8" height="18" fill="#263238"/>')
    b.append('<rect x="248" y="170" width="34" height="4" fill="#5d4037"/><rect x="225" y="312" width="80" height="6" fill="#81c784"/>')
    b.append('<path d="M300,295 L330,265" stroke="#555" stroke-width="5"/>')
    b.append('<path d="M285,90 L340,60 M285,148 L340,60 M285,198 L340,60 M285,248 L340,60" stroke="#222"/>' + multiline(342, 55, L['magnetic']))
    b.append(lab(282, 172, 340, 190, L['sample']) + lab(330, 265, 340, 250, L['eye']) + lab(305, 315, 330, 330, L['screen']))
    b.append(multiline(265, 360, L['tem'], 'middle'))
    # SEM column
    b.append('<rect x="420" y="10" width="90" height="220" fill="#fff8e1" stroke="#333"/>')
    b.append('<path d="M465,20 L450,50 L480,50 Z" fill="#ec407a" opacity=".6"/><path d="M465,50 L470,200" stroke="#ec407a" stroke-width="6" opacity=".5"/>')
    for y in (70, 130):
        b.append(f'<rect x="448" y="{y}" width="8" height="18" fill="#263238"/><rect x="476" y="{y}" width="8" height="18" fill="#263238"/>')
    b.append('<rect x="445" y="200" width="45" height="6" fill="#5d4037"/><path d="M495,185 l10,-20" stroke="#333" stroke-width="5"/>')
    b.append('<rect x="440" y="250" width="70" height="50" rx="4" fill="#263238"/><rect x="447" y="256" width="56" height="36" fill="#4dd0e1"/>')
    b.append(multiline(465, 360, L['sem'], 'middle'))
    return svg_wrap(''.join(b), 560, 390, L['title'])


MM_EN = dict(title='Figure 4.4: Mechanism of the light and electron microscopes', optical=['Optical', 'lenses'], sample='Sample', source=['Source of', 'light'],
             lm=['Light', 'Microscope'], magnetic=['Magnetic', 'lenses'], eye='Eye', screen='Screen', tem=['Transmission Electron', 'Microscope'], sem=['Scanning Electron', 'Microscope'])
MM_UR = dict(title='شکل 4.4', optical=['بصری', 'عدسے'], sample='نمونہ', source=['روشنی کا', 'ذریعہ'], lm=['روشنی کی', 'خوردبین'], magnetic=['مقناطیسی', 'عدسے'],
             eye='آنکھ', screen='اسکرین', tem=['ٹرانسمیشن الیکٹران', 'خوردبین'], sem=['اسکیننگ الیکٹران', 'خوردبین'])
MM_PS = dict(title='شکل 4.4', optical=['نوري', 'عدسې'], sample='نمونه', source=['د رڼا', 'سرچینه'], lm=['د رڼا', 'مایکروسکوپ'], magnetic=['مقناطیسي', 'عدسې'],
             eye='سترګه', screen='پرده', tem=['لېږدونکی الکترون', 'مایکروسکوپ'], sem=['سکېنینګ الکترون', 'مایکروسکوپ'])


def cork(L):
    random.seed(7)
    b = []
    for cx, fill, stroke, key in [(140, '#6d4c41', '#efebe9', 'drawing'), (390, '#4e342e', '#f5f5f5', 'cork')]:
        b.append(f'<clipPath id="ck{cx}"><circle cx="{cx}" cy="130" r="110"/></clipPath><circle cx="{cx}" cy="130" r="110" fill="{fill}"/>')
        g = [f'<g clip-path="url(#ck{cx})" fill="none" stroke="{stroke}" stroke-width="2">']
        for row in range(14):
            for col in range(14):
                x = cx - 120 + col * 18 + (row % 2) * 9 + random.uniform(-2, 2)
                y = 20 + row * 16 + random.uniform(-2, 2)
                g.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="15" height="13" rx="3"/>')
        g.append('</g>')
        b.append(''.join(g))
        b.append(f'<rect x="{cx-110}" y="0" width="{len(L[key])*7+10}" height="20" fill="#bbdefb"/>' + txt(cx - 105, 15, L[key], 12, 'start', 'bold'))
    return svg_wrap(''.join(b), 520, 250, L['title'])


CK_EN = dict(title="Figure 4.5: Robert Hooke's observation of cork under microscope", drawing='Drawing by Hooke', cork='Cork tissue')
CK_UR = dict(title='شکل 4.5', drawing='ہُک کی بنائی ہوئی شکل', cork='کارک کی بافت')
CK_PS = dict(title='شکل 4.5', drawing='د هوک رسم', cork='د کارک نسج')


def mito(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><ellipse rx="22" ry="11" fill="#e57373" stroke="#b71c1c"/>'
            '<path d="M-14,-6 q4,10 8,0 q4,-10 8,0 q4,10 8,0" fill="none" stroke="#ffcdd2" stroke-width="2"/></g>')


def chloro(x, y, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><ellipse rx="22" ry="12" fill="#66bb6a" stroke="#1b5e20"/>'
            + ''.join(f'<rect x="{-15 + k*8}" y="-7" width="5" height="14" fill="#1b5e20"/>' for k in range(4)) + '</g>')


def golgi(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})">' + ''.join(f'<path d="M-24,{k*7} q24,-10 48,0" stroke="#ad1457" stroke-width="4" fill="none"/>' for k in range(4)) + '</g>'


def rough_er(x, y, h=50):
    pts = ''.join(f'<circle cx="{x + (6 if k % 2 else -6)}" cy="{y + k*5}" r="1.6" fill="#212121"/>' for k in range(h // 5))
    return f'<path d="M{x-6},{y} q12,{h/4} 0,{h/2} q-12,{h/4} 0,{h/2} M{x+6},{y} q12,{h/4} 0,{h/2} q-12,{h/4} 0,{h/2}" stroke="#5d4037" fill="none" stroke-width="2"/>' + pts


def plant_cell(L):
    b = ['<rect x="140" y="20" width="250" height="360" rx="30" fill="#a5d6a7" stroke="#2e7d32" stroke-width="6"/>',
         '<rect x="148" y="28" width="234" height="344" rx="26" fill="#dcedc8" stroke="#558b2f" stroke-width="1.5"/>',
         '<path d="M220,90 Q330,60 345,150 Q360,300 260,320 Q200,300 205,220 Q190,120 220,90 Z" fill="#fafafa" stroke="#7cb342" stroke-width="2"/>']
    b.append('<circle cx="190" cy="160" r="26" fill="#f8bbd0" stroke="#880e4f"/><circle cx="188" cy="158" r="10" fill="#6a1b9a"/>')
    b.append(rough_er(215, 175, 45) + '<path d="M180,110 q10,8 0,16 q-10,8 0,16" stroke="#795548" fill="none" stroke-width="2"/>')
    b.append(golgi(305, 75, .8) + chloro(360, 110, 90) + chloro(360, 190, 90) + chloro(180, 250, 90) + chloro(200, 50, 0))
    b.append(mito(355, 300, -40) + mito(260, 350, 0) + mito(345, 230, -60, .7))
    b.append('<circle cx="275" cy="240" r="16" fill="none" stroke="#455a64" stroke-dasharray="2 2" stroke-width="3"/>')
    b.append('<path d="M285,160 L300,215 M290,150 L305,205" stroke="#424242" stroke-width="2"/><rect x="240" y="120" width="40" height="12" fill="#616161" transform="rotate(30 260 126)"/>')
    b.append('<ellipse cx="180" cy="330" rx="12" ry="7" fill="#eeeeee" stroke="#9e9e9e"/>')
    b.append(''.join(f'<circle cx="{172 + (k%5)*7}" cy="{90 + (k//5)*7}" r="1.8" fill="#212121"/>' for k in range(10)))
    b.append(''.join(f'<circle cx="{255 + k*8}" cy="{70 + (k%2)*6}" r="3" fill="#a1887f"/>' for k in range(3)))
    left = [('golgiv', 255, 72, 85), ('ribosome', 180, 95, 105), ('ser', 180, 120, 128), ('nucleolus', 188, 158, 160), ('nucleus', 175, 178, 182),
            ('rer', 210, 190, 205), ('vacuole', 230, 260, 262), ('amylo', 180, 330, 318)]
    for key, x, y, ty in left:
        b.append(f'<path d="M{x},{y} L130,{ty}" stroke="#b71c1c" stroke-width="1"/>' + multiline(126, ty + 4 - 6 * (len(L[key]) - 1), L[key], 'end', 10))
    right = [('wall', 385, 25, 22), ('membrane', 380, 40, 40), ('golgi', 320, 78, 62), ('chloro', 375, 110, 100), ('vacmem', 345, 150, 130),
             ('raphide', 300, 210, 180), ('druse', 285, 240, 225), ('mito', 365, 295, 270), ('cyto', 300, 365, 360)]
    for key, x, y, ty in right:
        b.append(f'<path d="M{x},{y} L400,{ty}" stroke="#b71c1c" stroke-width="1"/>' + multiline(404, ty + 4 - 6 * (len(L[key]) - 1), L[key], 'start', 10))
    return svg_wrap(''.join(b), 540, 395, L['title'])


PC_EN = dict(title='Figure 4.7 Structure of a plant cell', golgiv=['Golgi vesicles'], ribosome=['Ribosome'], ser=['Smooth ER', '(no ribosomes)'], nucleolus=['Nucleolus'],
             nucleus=['Nucleus'], rer=['Rough ER', '(endoplasmic', 'reticulum)'], vacuole=['Large central', 'vacuole'], amylo=['Amyloplast', '(starch grain)'],
             wall=['Cell wall'], membrane=['Cell membrane'], golgi=['Golgi', 'apparatus'], chloro=['Chloroplast'], vacmem=['Vacuole', 'membrane'],
             raphide=['Raphide', 'crystal'], druse=['Druse', 'crystal'], mito=['Mitochondrion'], cyto=['Cytoplasm'])
PC_UR = dict(title='شکل 4.7', golgiv=['گولجی ویسیکلز'], ribosome=['رائبوسوم'], ser=['ہموار ER', '(رائبوسوم کے بغیر)'], nucleolus=['نیوکلیولس'], nucleus=['مرکزہ'],
             rer=['کھردرا ER', '(اینڈوپلازمک', 'ریٹیکولم)'], vacuole=['بڑا مرکزی', 'ویکیول'], amylo=['ایمائلوپلاسٹ', '(نشاستے کا دانہ)'], wall=['خلوی دیوار'],
             membrane=['خلوی جھلی'], golgi=['گولجی', 'اپریٹس'], chloro=['کلوروپلاسٹ'], vacmem=['ویکیول کی', 'جھلی'], raphide=['ریفائیڈ', 'قلم'], druse=['ڈروز', 'قلم'],
             mito=['مائٹوکونڈریون'], cyto=['سائٹوپلازم'])
PC_PS = dict(title='شکل 4.7', golgiv=['ګولجي ویسیکلونه'], ribosome=['رایبوزوم'], ser=['هوار ER', '(بې رایبوزومه)'], nucleolus=['نیوکلیولس'], nucleus=['هسته'],
             rer=['زیږ ER', '(انډوپلازمیک', 'ریټیکولم)'], vacuole=['لوی مرکزي', 'واکیول'], amylo=['امایلوپلاسټ', '(د نشایستې دانه)'], wall=['د حجرې دېوال'],
             membrane=['د حجرې غشا'], golgi=['ګولجي', 'اپراټس'], chloro=['کلوروپلاسټ'], vacmem=['د واکیول', 'غشا'], raphide=['رافایډ', 'کرسټال'], druse=['ډروز', 'کرسټال'],
             mito=['مایټوکونډریون'], cyto=['سایټوپلازم'])


def animal_cell(L):
    b = ['<ellipse cx="270" cy="200" rx="150" ry="165" fill="#fff3e0" stroke="#bcaaa4" stroke-width="2"/>']
    b.append('<path d="M225,170 Q240,130 295,140 Q340,160 330,220 Q315,265 260,255 Q215,240 225,170 Z" fill="#d81b60" opacity=".85"/><circle cx="268" cy="175" r="16" fill="#6a1b9a"/>')
    b.append(golgi(275, 85, 1) + '<ellipse cx="200" cy="70" rx="20" ry="9" fill="#ffe082" stroke="#f57f17"/>')
    b.append(''.join(f'<circle cx="{220 + k*9}" cy="{95 + (k%2)*4}" r="3.5" fill="#f48fb1"/>' for k in range(4)))
    b.append(mito(320, 75, -30) + mito(330, 265, -20) + mito(250, 300, 0))
    b.append(rough_er(160, 150, 60) + rough_er(380, 150, 60))
    b.append('<path d="M165,240 l40,-30 M150,280 l60,10 M370,240 l-20,40 M330,330 l40,-30" stroke="#9ccc65" stroke-width="2"/>')
    b.append('<g fill="#ffcc80" stroke="#e65100"><circle cx="238" cy="270" r="7"/><circle cx="250" cy="280" r="7"/></g>')
    b.append(''.join(f'<circle cx="{300 + (k%4)*10}" cy="{300 + (k//4)*8}" r="2" fill="#212121"/>' for k in range(8)))
    left = [('lysosome', 200, 70, 70), ('golgiv', 220, 97, 100), ('rer', 160, 160, 160), ('ser', 175, 230, 230), ('membrane', 125, 270, 275), ('centrioles', 240, 275, 315)]
    for key, x, y, ty in left:
        b.append(f'<path d="M{x},{y} L110,{ty}" stroke="#212121" stroke-width="1"/>' + multiline(106, ty + 4 - 6 * (len(L[key]) - 1), L[key], 'end', 10))
    right = [('golgi', 285, 82, 20), ('mito', 335, 70, 60), ('nucleolus', 270, 175, 110), ('nucleus', 310, 205, 205), ('microtubules', 372, 245, 255),
             ('cyto', 340, 290, 290), ('ribosome', 320, 305, 320)]
    for key, x, y, ty in right:
        b.append(f'<path d="M{x},{y} L430,{ty}" stroke="#212121" stroke-width="1"/>' + multiline(434, ty + 4 - 6 * (len(L[key]) - 1), L[key], 'start', 10))
    return svg_wrap(''.join(b), 560, 390, L['title'])


AC_EN = dict(title='Figure 4.8: The structure of an animal cell', lysosome=['Lysosome'], golgiv=['Golgi', 'vesicles'], rer=['Rough ER', '(endoplasmic', 'reticulum)'],
             ser=['Smooth ER', '(no ribosomes)'], membrane=['Cell (plasma)', 'membrane'], centrioles=['Centrioles (2)', 'Each composed', 'of 9 microtubule', 'triplets.'],
             golgi=['Golgi', 'apparatus'], mito=['Mitochondrion'], nucleolus=['Nucleolus'], nucleus=['Nucleus'], microtubules=['Microtubules'], cyto=['Cytoplasm'], ribosome=['Ribosome'])
AC_UR = dict(title='شکل 4.8', lysosome=['لائسوسوم'], golgiv=['گولجی', 'ویسیکلز'], rer=['کھردرا ER', '(اینڈوپلازمک', 'ریٹیکولم)'], ser=['ہموار ER', '(رائبوسوم کے بغیر)'],
             membrane=['خلوی (پلازما)', 'جھلی'], centrioles=['سینٹریولز (2)', 'ہر ایک 9 مائیکرو', 'ٹیوبول ٹرپلٹس', 'سے بنا'], golgi=['گولجی', 'اپریٹس'], mito=['مائٹوکونڈریون'],
             nucleolus=['نیوکلیولس'], nucleus=['مرکزہ'], microtubules=['مائیکرو ٹیوبولز'], cyto=['سائٹوپلازم'], ribosome=['رائبوسوم'])
AC_PS = dict(title='شکل 4.8', lysosome=['لایزوزوم'], golgiv=['ګولجي', 'ویسیکلونه'], rer=['زیږ ER', '(انډوپلازمیک', 'ریټیکولم)'], ser=['هوار ER', '(بې رایبوزومه)'],
             membrane=['د حجرې (پلازما)', 'غشا'], centrioles=['سنټریولونه (2)', 'هر یو له 9 مایکرو', 'ټیوبول درېګونو', 'جوړ'], golgi=['ګولجي', 'اپراټس'], mito=['مایټوکونډریون'],
             nucleolus=['نیوکلیولس'], nucleus=['هسته'], microtubules=['مایکروټیوبولونه'], cyto=['سایټوپلازم'], ribosome=['رایبوزوم'])


def fluid_mosaic(L):
    b = ['<rect x="60" y="135" width="460" height="100" fill="#fff9c4"/>']
    for row_y, flip in ((140, 1), (230, -1)):
        for i in range(30):
            x = 70 + i * 15
            if 200 <= x <= 290 and True:
                continue
            b.append(f'<circle cx="{x}" cy="{row_y}" r="7" fill="#e53935"/>')
            b.append(f'<path d="M{x-2},{row_y + 7*flip} q-3,{18*flip} 0,{38*flip} M{x+2},{row_y + 7*flip} q3,{18*flip} 0,{38*flip}" stroke="#9e9e9e" fill="none"/>')
    b.append('<path d="M205,120 q-10,60 5,125 h30 q10,-60 -2,-125 z M250,120 q10,60 -2,125 h30 q12,-60 -2,-125 z" fill="#fff59d" stroke="#f9a825"/>')
    b.append('<ellipse cx="410" cy="132" rx="20" ry="16" fill="#4db6ac"/><ellipse cx="120" cy="240" rx="20" ry="12" fill="#4db6ac"/>')
    b.append('<path d="M410,116 q-6,-14 4,-24 q-8,-10 2,-20" stroke="#4fc3f7" stroke-width="4" fill="none"/><path d="M180,133 q-6,-14 4,-24 q-8,-10 2,-20" stroke="#4fc3f7" stroke-width="4" fill="none"/>')
    b.append('<path d="M395,190 l8,10 l-10,4 z" fill="#ad1457"/>')
    b.append('<path d="M172,85 h20 M182,85 v6" stroke="#333"/>' + txt(182, 78, L['glycolipid'], 12, 'middle', 'bold'))
    b.append('<path d="M405,62 h20 M415,62 v6" stroke="#333"/>' + txt(415, 55, L['glycoprotein'], 12, 'middle', 'bold'))
    b.append('<path d="M330,100 L240,150 M330,100 L400,130" stroke="#333"/>' + txt(330, 95, L['proteins'], 12, 'middle', 'bold'))
    b.append('<path d="M50,140 h-8 v95 h8" stroke="#333" fill="none"/>' + multiline(5, 180, L['bilayer'], 'start', 12))
    b.append('<path d="M403,205 L450,260" stroke="#333"/>' + txt(455, 268, L['cholesterol'], 12, 'start', 'bold'))
    b.append(multiline(120, 95, L['outside'], 'start', 12) + multiline(120, 270, L['inside'], 'start', 12))
    return svg_wrap(''.join(b), 560, 300, L['title'])


FM_EN = dict(title='Figure 4.9: Fluid Mosaic Model of Cell Membrane', glycolipid='Glycolipid', glycoprotein='Glycoprotein', proteins='Proteins', bilayer=['Lipid', 'bilayer'],
             cholesterol='Cholesterol', outside=['Outside', 'of Cell'], inside=['Inside', 'of Cell'])
FM_UR = dict(title='شکل 4.9', glycolipid='گلائکو لپڈ', glycoprotein='گلائکو پروٹین', proteins='پروٹینز', bilayer=['لپڈ', 'دوہری تہ'], cholesterol='کولیسٹرول',
             outside=['خلیے کا', 'بیرونی حصہ'], inside=['خلیے کا', 'اندرونی حصہ'])
FM_PS = dict(title='شکل 4.9', glycolipid='ګلایکولیپیډ', glycoprotein='ګلایکوپروټین', proteins='پروټینونه', bilayer=['لیپیډي', 'دوه پوړی'], cholesterol='کولسټرول',
             outside=['د حجرې', 'بهر'], inside=['د حجرې', 'دننه'])
