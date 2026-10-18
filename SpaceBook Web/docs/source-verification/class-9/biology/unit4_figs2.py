# -*- coding: utf-8 -*-
"""Coded organelle figures for Unit 4 (Figures 4.10-4.18). Each takes a label dict L."""
import math
from bio9_tools import svg_wrap, txt
from unit4_figs import multiline, mito, golgi


def pointer(x1, y1, x2, y2, lines, anchor='start', size=11):
    lines = lines if isinstance(lines, list) else [lines]
    dx = 4 if anchor == 'start' else -4
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#212121" stroke-width="1.2"/>' + multiline(x2 + dx, y2 + 4, lines, anchor, size)


def er(L):
    b = ['<rect x="60" y="40" width="300" height="200" rx="20" fill="#fce4ec"/>']
    for k in range(5):
        y = 70 + k * 30
        b.append(f'<path d="M180,{y} q60,-25 160,10" stroke="#ad1457" stroke-width="10" fill="none" stroke-linecap="round"/>')
        b.append(''.join(f'<circle cx="{190 + j*18}" cy="{y - 8 + j*1.5}" r="2.5" fill="#311b92"/>' for j in range(8)))
    b.append('<path d="M80,90 q20,40 60,30 q30,-10 40,30 M90,160 q30,10 50,-10" stroke="#ec407a" stroke-width="6" fill="none"/>')
    b.append('<path d="M70,230 q120,-40 280,-10" stroke="#880e4f" stroke-width="5" fill="none"/>')
    b.append(pointer(110, 115, 110, 20, L['ser'], 'middle') + pointer(260, 80, 300, 20, L['rer'], 'start'))
    b.append(pointer(330, 85, 370, 90, L['ribo']) + pointer(250, 220, 280, 260, L['nucmem']))
    return svg_wrap(''.join(b), 470, 275, L['title'])


ER_EN = dict(title='Figure 4.10: Endoplasmic Reticulum', ser=['Smooth endoplasmic', 'Reticulum'], rer=['Rough endoplasmic', 'Reticulum'], ribo='Ribosomes', nucmem='Nuclear membrane')
ER_UR = dict(title='شکل 4.10', ser=['ہموار اینڈوپلازمک', 'ریٹیکولم'], rer=['کھردرا اینڈوپلازمک', 'ریٹیکولم'], ribo='رائبوسومز', nucmem='مرکزی جھلی')
ER_PS = dict(title='شکل 4.10', ser=['هوار انډوپلازمیک', 'ریټیکولم'], rer=['زیږ انډوپلازمیک', 'ریټیکولم'], ribo='رایبوزومونه', nucmem='هستوي غشا')


def golgi_fig(L):
    b = [golgi(200, 120, 3.2)]
    b.append(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ec407a"/>' for x, y, r in [(110, 90, 9), (300, 95, 8), (140, 220, 7), (260, 225, 8), (200, 245, 9), (330, 150, 7)]))
    b.append(pointer(110, 82, 90, 30, L['vesicle'], 'middle') + pointer(270, 120, 320, 35, L['cisternae']) + pointer(200, 254, 200, 285, L['transport'], 'middle'))
    return svg_wrap(''.join(b), 420, 300, L['title'])


GO_EN = dict(title='Figure 4.11: Golgi Apparatus', vesicle='Vesicle', cisternae='Cisternae', transport='Transport vesicle')
GO_UR = dict(title='شکل 4.11', vesicle='ویسیکل', cisternae='سسٹرنی', transport='ٹرانسپورٹ ویسیکل')
GO_PS = dict(title='شکل 4.11', vesicle='ویسیکل', cisternae='سیسټرني', transport='د لېږد ویسیکل')


def mito_fig(L):
    b = ['<ellipse cx="190" cy="120" rx="150" ry="70" fill="#ef9a9a" stroke="#b71c1c" stroke-width="3"/>',
         '<ellipse cx="190" cy="120" rx="138" ry="60" fill="#ffebee" stroke="#c62828" stroke-width="2"/>']
    for k in range(7):
        x = 85 + k * 35
        up = k % 2 == 0
        b.append(f'<path d="M{x},{70 if up else 170} q10,{45 if up else -45} 20,0" fill="#ef9a9a" stroke="#c62828" stroke-width="2"/>')
    b.append(pointer(300, 80, 350, 30, L['inner']) + pointer(320, 90, 360, 60, L['outer']) + pointer(230, 160, 330, 220, L['cristae']) + pointer(160, 120, 140, 230, L['matrix']))
    return svg_wrap(''.join(b), 460, 250, L['title'])


MI_EN = dict(title='Figure 4.12 Mitochondrion', inner='Inner Membrane', outer='Outer Membrane', cristae='Cristae', matrix='Matrix')
MI_UR = dict(title='شکل 4.12', inner='اندرونی جھلی', outer='بیرونی جھلی', cristae='کرسٹی', matrix='میٹرکس')
MI_PS = dict(title='شکل 4.12', inner='داخلي غشا', outer='بهرنۍ غشا', cristae='کریسټي', matrix='میټرکس')


def ribosome_fig(L):
    b = ['<ellipse cx="120" cy="80" rx="70" ry="45" fill="#9575cd" stroke="#4527a0"/>', '<ellipse cx="120" cy="140" rx="55" ry="25" fill="#ce93d8" stroke="#6a1b9a"/>']
    b.append(pointer(185, 70, 230, 50, L['large']) + pointer(170, 145, 230, 160, L['small']))
    return svg_wrap(''.join(b), 340, 190, L['title'])


RB_EN = dict(title='Fig. 4.13: Subunits of Ribsome', large='Large subunit', small='Small subunit')
RB_UR = dict(title='شکل 4.13', large='بڑی ذیلی اکائی', small='چھوٹی ذیلی اکائی')
RB_PS = dict(title='شکل 4.13', large='لوی فرعي واحد', small='کوچنی فرعي واحد')


def chloroplast_fig(L):
    b = ['<ellipse cx="200" cy="120" rx="170" ry="80" fill="#c5e1a5" stroke="#33691e" stroke-width="3"/>',
         '<ellipse cx="200" cy="120" rx="158" ry="70" fill="#dcedc8" stroke="#558b2f" stroke-width="2"/>']
    for gx in (100, 160, 230, 290):
        for k in range(6):
            b.append(f'<ellipse cx="{gx}" cy="{90 + k*10}" rx="18" ry="5" fill="#2e7d32"/>')
        b.append(f'<path d="M{gx+18},{110} h40" stroke="#2e7d32" stroke-width="3"/>' if gx < 290 else '')
    b.append(pointer(290, 92, 360, 20, L['granum']) + pointer(160, 140, 120, 230, L['thylakoid'], 'middle') + pointer(340, 120, 390, 110, L['inner']))
    b.append(pointer(60, 150, 20, 220, L['outer'], 'start') + pointer(200, 165, 230, 230, L['stroma']))
    return svg_wrap(''.join(b), 480, 250, L['title'])


CH_EN = dict(title='Figure 4.14: Chloroplast', granum='Granum', thylakoid='Thylakoid', inner=['Inner', 'membrane'], outer=['Outer', 'membrane'], stroma='Stroma')
CH_UR = dict(title='شکل 4.14', granum='گرینم', thylakoid='تھائیلاکوئیڈ', inner=['اندرونی', 'جھلی'], outer=['بیرونی', 'جھلی'], stroma='اسٹروما')
CH_PS = dict(title='شکل 4.14', granum='ګرانوم', thylakoid='تایلاکویډ', inner=['داخلي', 'غشا'], outer=['بهرنۍ', 'غشا'], stroma='سټروما')


def cytoskeleton_fig(L):
    b = ['<polygon points="140,30 440,30 400,70 100,70" fill="#90a4ae" stroke="#37474f"/>', '<polygon points="140,190 440,190 400,230 100,230" fill="#b3e5fc" stroke="#0277bd"/>']
    b.append('<path d="M160,70 L170,190 M240,70 L230,190 M330,70 L340,190 M380,70 L370,190" stroke="#fbc02d" stroke-width="2" stroke-dasharray="4 3"/>')
    b.append('<path d="M120,120 L430,105 M130,150 L440,140" stroke="#29b6f6" stroke-width="7"/>' + mito(330, 125, 0, 1.4))
    b.append(''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#f48fb1"/>' for x, y in [(200, 130), (260, 160), (180, 170)]))
    b.append(pointer(150, 50, 70, 40, L['plasma'], 'end') + pointer(130, 120, 70, 95, L['er'], 'end') + pointer(190, 165, 70, 140, L['ribo'], 'end'))
    b.append(pointer(130, 225, 70, 220, L['microfil'], 'end') + pointer(400, 106, 450, 70, L['microtub']) + pointer(355, 130, 450, 150, L['mito']))
    return svg_wrap('<g transform="translate(80,0)">' + ''.join(b) + '</g>', 640, 250, L['title'])


CY_EN = dict(title='Figure 4.15: Cytoskeleton', plasma=['Plasma', 'membrane'], er=['Endoplasmic', 'reticulum'], ribo='Ribosomes', microfil='Microfilaments', microtub='Microtubule', mito='Mitochondrion')
CY_UR = dict(title='شکل 4.15', plasma=['پلازما', 'جھلی'], er=['اینڈوپلازمک', 'ریٹیکولم'], ribo='رائبوسومز', microfil='مائیکرو فلامنٹس', microtub='مائیکرو ٹیوبول', mito='مائٹوکونڈریون')
CY_PS = dict(title='شکل 4.15', plasma=['پلازما', 'غشا'], er=['انډوپلازمیک', 'ریټیکولم'], ribo='رایبوزومونه', microfil='مایکروفلامنټونه', microtub='مایکروټیوبول', mito='مایټوکونډریون')


def centriole_fig(L):
    b = ['<circle cx="120" cy="140" r="65" fill="#fff59d" stroke="#33691e" stroke-width="2"/><circle cx="120" cy="140" r="6" fill="#fff" stroke="#333"/>']
    for k in range(9):
        a = 2 * math.pi * k / 9
        b.append(f'<path d="M120,140 L{120 + 65*math.cos(a):.1f},{140 + 65*math.sin(a):.1f}" stroke="#33691e"/>')
        for j, col in enumerate(('#f8bbd0', '#64b5f6', '#2e7d32')):
            r = 72 + j * 9
            aa = a + 0.12 * j
            b.append(f'<circle cx="{120 + r*math.cos(aa):.1f}" cy="{140 + r*math.sin(aa):.1f}" r="5" fill="{col}"/>')
    for k in range(9):
        y = 70 + k * 16
        for j, col in enumerate(('#2e7d32', '#64b5f6', '#f8bbd0')):
            b.append(f'<rect x="{290 + j*6}" y="{y + j*4}" width="180" height="9" rx="4" fill="{col}" stroke="#333" stroke-width=".5"/>')
    b.append(txt(120, 40, L['overhead'], 12, 'middle', 'bold') + txt(380, 50, L['side'], 12, 'middle', 'bold'))
    b.append(pointer(300, 205, 260, 250, L['triplet'], 'end'))
    return svg_wrap(''.join(b), 500, 280, L['title'])


CE_EN = dict(title='Figure 4.16: Centriole', overhead='Overhead view', side='Side view', triplet=['Triplet', 'Microtubules'])
CE_UR = dict(title='شکل 4.16', overhead='اوپر سے منظر', side='پہلو سے منظر', triplet=['ٹرپلٹ', 'مائیکرو ٹیوبولز'])
CE_PS = dict(title='شکل 4.16', overhead='له پاسه منظره', side='له اړخه منظره', triplet=['درې ګونی', 'مایکروټیوبولونه'])


def vacuole_lysosome(L):
    b = ['<rect x="20" y="20" width="180" height="200" rx="10" fill="#c8e6c9" stroke="#2e7d32" stroke-width="4"/>',
         '<path d="M50,50 h120 q15,0 15,15 v120 q0,15 -15,15 h-120 q-15,0 -15,-15 v-120 q0,-15 15,-15 z" fill="#e3f2fd" stroke="#1565c0" stroke-width="2"/>']
    b.append(pointer(185, 90, 230, 60, L['tonoplast']) + pointer(110, 130, 230, 140, L['vacuole']) + txt(110, 240, 'a.', 12, 'middle', 'bold'))
    b.append('<circle cx="380" cy="120" r="70" fill="#fff9c4" stroke="#f57f17" stroke-width="4"/>')
    b.append(''.join(f'<circle cx="{350 + (k%4)*20}" cy="{95 + (k//4)*22}" r="5" fill="#8d6e63"/>' for k in range(12)))
    b.append(txt(380, 35, L['lysosome'], 12, 'middle', 'bold') + pointer(440, 85, 480, 70, L['membrane']) + pointer(400, 140, 480, 170, L['enzymes']) + txt(380, 240, 'b.', 12, 'middle', 'bold'))
    return svg_wrap(''.join(b), 580, 255, L['title'])


VL_EN = dict(title='Figure 4.17: a) Central Vacuole in plant cell, b) Lysosome', tonoplast='Tonoplast', vacuole='Vacuole', lysosome='Lysosome', membrane='Membrane', enzymes=['Proteins/', 'Enzymes'])
VL_UR = dict(title='شکل 4.17', tonoplast='ٹونوپلاسٹ', vacuole='ویکیول', lysosome='لائسوسوم', membrane='جھلی', enzymes=['پروٹینز/', 'انزائمز'])
VL_PS = dict(title='شکل 4.17', tonoplast='ټونوپلاسټ', vacuole='واکیول', lysosome='لایزوزوم', membrane='غشا', enzymes=['پروټینونه/', 'انزایمونه'])


def nucleus_fig(L):
    b = ['<circle cx="200" cy="140" r="110" fill="#b3e5fc" stroke="#0277bd" stroke-width="6" stroke-dasharray="40 8"/>', '<circle cx="200" cy="140" r="98" fill="#e1f5fe"/>']
    b.append('<path d="M120,100 q30,-20 60,10 t60,0 M110,170 q40,20 80,-10 t70,20 M150,80 q20,60 -10,120 M260,90 q-30,40 0,100" stroke="#90a4ae" fill="none" stroke-dasharray="3 3"/>')
    b.append('<ellipse cx="195" cy="145" rx="45" ry="38" fill="#ef5350"/>')
    b.append(pointer(150, 95, 100, 20, L['chromatin'], 'middle') + pointer(285, 85, 330, 20, L['envelope']) + pointer(175, 165, 110, 265, L['nucleolus'], 'middle') + pointer(300, 180, 340, 255, L['pore']))
    return svg_wrap(''.join(b), 440, 285, L['title'])


NU_EN = dict(title='Figure 4.18: The Nucleus', chromatin='Chromatin Network', envelope=['Nuclear', 'Envelope'], nucleolus='Nucleolus', pore=['Nuclear', 'Pore'])
NU_UR = dict(title='شکل 4.18', chromatin='کرومیٹن نیٹ ورک', envelope=['مرکزی', 'لفافہ'], nucleolus='نیوکلیولس', pore=['مرکزی', 'مسام'])
NU_PS = dict(title='شکل 4.18', chromatin='د کروماټین جال', envelope=['هستوي', 'پوښ'], nucleolus='نیوکلیولس', pore=['هستوي', 'سوری'])
