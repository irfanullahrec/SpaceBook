# -*- coding: utf-8 -*-
"""Coded figures for Unit 8 digestive system (Figures 8.8-8.15). Each takes a label dict L."""
from bio9_tools import svg_wrap, txt
from unit4_figs2 import pointer

PINK = '#ef9a9a'
RED = '#e57373'
DARK = '#c62828'
GREEN = '#66bb6a'


def lab(L, k):
    return L[k] if isinstance(L[k], list) else [L[k]]


# ---- Figure 8.8 General outline of human digestive system -------------------
def digestive(L):
    b = ['<path d="M150,20 C120,30 115,70 130,100 L140,140 C100,160 90,200 100,230 L100,470 L300,470 L300,230 C310,200 300,160 260,140 L250,100 C265,70 260,30 230,20" fill="#fff8e1" stroke="#bcaaa4"/>']
    # mouth, salivary glands, pharynx, oesophagus
    b.append('<path d="M150,80 q20,-10 40,0" stroke="' + DARK + '" stroke-width="8" fill="none"/>')
    b.append(f'<ellipse cx="200" cy="60" rx="10" ry="7" fill="{RED}"/><ellipse cx="215" cy="85" rx="9" ry="6" fill="{RED}"/><ellipse cx="190" cy="95" rx="8" ry="5" fill="{RED}"/>')
    b.append(f'<path d="M205,85 L205,240" stroke="{RED}" stroke-width="9"/>')
    b.append('<path d="M200,112 l10,0 l-3,10 z" fill="#64b5f6"/>')
    # liver, gall bladder
    b.append('<path d="M120,235 C140,215 220,215 235,235 L215,280 C180,285 140,280 120,265 Z" fill="#8d6e63"/>')
    b.append('<ellipse cx="185" cy="285" rx="8" ry="11" fill="#43a047"/>')
    # stomach
    b.append(f'<path d="M205,240 C260,230 285,260 270,295 C255,320 220,315 215,300" fill="{PINK}" stroke="{DARK}" stroke-width="2"/>')
    # pancreas & ducts
    b.append('<path d="M200,305 C220,300 245,305 262,312" stroke="#ffb74d" stroke-width="9" stroke-linecap="round"/>')
    b.append('<path d="M190,292 L200,318 M215,307 L200,318" stroke="#2e7d32" stroke-width="2"/>')
    # duodenum C
    b.append(f'<path d="M215,300 C190,305 180,320 185,335 C190,350 215,350 230,345" stroke="{RED}" stroke-width="9" fill="none"/>')
    # large intestine frame
    b.append(f'<path d="M150,440 L150,345 L260,345 L260,420 C255,440 235,445 225,450" stroke="{GREEN}" stroke-width="16" fill="none" stroke-linejoin="round"/>')
    b.append(f'<path d="M222,450 L222,470" stroke="{GREEN}" stroke-width="12"/><path d="M222,470 L222,485" stroke="#1565c0" stroke-width="6"/>')
    b.append(f'<path d="M150,440 q-6,14 4,22" stroke="{GREEN}" stroke-width="7" fill="none"/>')
    # small intestine coils
    b.append(f'<path d="M230,345 C245,360 170,365 175,380 C180,395 245,385 240,400 C235,415 170,410 175,425 C180,440 200,440 158,438" stroke="#f06292" stroke-width="8" fill="none"/>')
    # labels right
    b.append(pointer(203, 60, 260, 40, lab(L, 'salivary')))
    b.append(pointer(206, 105, 320, 105, lab(L, 'pharynx')) + pointer(207, 118, 320, 125, lab(L, 'epiglottis')))
    b.append(pointer(205, 190, 320, 190, lab(L, 'oesophagus')) + pointer(265, 270, 320, 245, lab(L, 'stomach')))
    b.append(pointer(250, 310, 320, 275, lab(L, 'pancreas')) + pointer(212, 309, 320, 300, lab(L, 'pduct')))
    b.append(pointer(198, 314, 320, 325, lab(L, 'bileduct')))
    b.append(pointer(262, 360, 320, 360, lab(L, 'colon')) + pointer(158, 455, 320, 400, lab(L, 'caecum')))
    b.append(pointer(222, 455, 320, 430, lab(L, 'rectum')) + pointer(222, 482, 320, 470, lab(L, 'anus')))
    b.append('<path d="M410,355 v80" stroke="#212121"/>' + txt(415, 395, L['large'][0], 11, 'start', 'bold') + txt(415, 408, L['large'][1], 11, 'start', 'bold'))
    # labels left
    b.append(pointer(165, 80, 80, 70, lab(L, 'oral'), 'end'))
    b.append(pointer(150, 245, 80, 240, lab(L, 'liver'), 'end') + pointer(180, 287, 80, 280, lab(L, 'gall'), 'end'))
    b.append(pointer(185, 330, 80, 320, lab(L, 'duodenum'), 'end') + pointer(180, 380, 80, 350, lab(L, 'jejunum'), 'end'))
    b.append(pointer(175, 422, 80, 380, lab(L, 'ileum'), 'end') + pointer(152, 460, 80, 455, lab(L, 'appendix'), 'end'))
    b.append('<path d="M20,320 v60" stroke="#212121"/>' + txt(15, 400, L['small'][0], 11, 'start', 'bold') + txt(15, 413, L['small'][1], 11, 'start', 'bold'))
    return svg_wrap(''.join(b), 470, 500, L['title'])


# ---- Figure 8.9 Parts of buccal cavity ---------------------------------------
def buccal(L):
    b = ['<rect x="80" y="20" width="270" height="230" rx="16" fill="#fce4ec"/>']
    b.append('<path d="M100,60 C150,40 230,40 280,70 L300,110" stroke="#ad1457" stroke-width="10" fill="none"/>')  # hard/soft palate
    b.append('<path d="M100,80 h70" stroke="#fff" stroke-width="9" stroke-dasharray="10 3"/>')  # teeth
    b.append('<path d="M110,160 C130,100 230,90 270,140 C285,170 270,210 230,220 L120,215 Z" fill="#ec407a"/>')  # tongue
    b.append('<path d="M300,110 l8,22 l-12,0 z" fill="#ad1457"/>')  # uvula
    b.append('<circle cx="292" cy="150" r="9" fill="#f48fb1" stroke="#ad1457"/><circle cx="268" cy="205" r="8" fill="#f48fb1" stroke="#ad1457"/>')
    b.append('<path d="M315,40 l8,90 M330,50 v190" stroke="#8d6e63" stroke-width="6"/>')
    b.append('<path d="M85,70 q-12,15 0,30 M85,180 q-12,15 0,30" stroke="#ad1457" stroke-width="7" fill="none"/>')
    b.append(pointer(150, 52, 150, 10, lab(L, 'hard'), 'middle') + pointer(250, 58, 250, 10, lab(L, 'soft'), 'middle'))
    b.append(pointer(320, 60, 360, 30, lab(L, 'ptonsil')) + pointer(304, 125, 360, 120, lab(L, 'uvula')))
    b.append(pointer(300, 150, 360, 150, lab(L, 'paltonsil')) + pointer(280, 180, 360, 180, lab(L, 'root')))
    b.append(pointer(275, 205, 360, 210, lab(L, 'lingual')))
    b.append(pointer(85, 85, 60, 85, lab(L, 'lip'), 'end') + pointer(100, 80, 60, 110, lab(L, 'cheek'), 'end'))
    b.append(pointer(150, 160, 60, 160, lab(L, 'body'), 'end'))
    return svg_wrap('<g transform="translate(55,0)">' + ''.join(b) + '</g>', 535, 260, L['title'])


# ---- Figure 8.10 Peristalsis in oesophagus -----------------------------------
def peristalsis(L):
    b = ['<path d="M190,10 C190,60 205,80 205,110 C205,140 175,160 175,190 C175,220 205,240 205,270 L205,300 L235,300 L235,270 C235,240 265,220 265,190 C265,160 235,140 235,110 C235,80 250,60 250,10 Z" fill="#ef9a9a" stroke="#c62828" stroke-width="2"/>']
    b.append('<ellipse cx="220" cy="270" rx="16" ry="20" fill="#8d6e63"/>')
    for y in (130, 220):
        b.append(f'<path d="M220,{y-25} v35" stroke="#1565c0" stroke-width="3"/><path d="M213,{y+8} l7,12 l7,-12 z" fill="#1565c0"/>')
    for y in (55, 200):
        b.append(f'<path d="M140,{y} h40" stroke="#1565c0" stroke-width="4"/><path d="M180,{y-6} l10,6 l-10,6 z" fill="#1565c0"/>')
        b.append(f'<path d="M300,{y} h-40" stroke="#1565c0" stroke-width="4"/><path d="M260,{y-6} l-10,6 l10,6 z" fill="#1565c0"/>')
    b.append(''.join(txt(20, 50 + i * 13, t, 11, 'start', 'bold') for i, t in enumerate(lab(L, 'mixing'))))
    b.append(''.join(txt(20, 105 + i * 13, t, 11, 'start', 'bold') for i, t in enumerate(lab(L, 'contractmix'))))
    b.append(''.join(txt(20, 185 + i * 13, t, 11, 'start', 'bold') for i, t in enumerate(lab(L, 'pushes'))))
    b.append(pointer(245, 30, 320, 20, lab(L, 'contracted')) + pointer(225, 140, 320, 130, lab(L, 'direction')))
    b.append(pointer(258, 240, 320, 240, lab(L, 'relaxed')) + pointer(232, 275, 320, 280, lab(L, 'ball')))
    return svg_wrap(''.join(b), 460, 310, L['title'])


# ---- Figure 8.11 Structure of the stomach ------------------------------------
def stomach(L):
    b = [f'<path d="M110,20 C120,60 60,70 60,140 C60,220 150,250 210,230 C240,220 250,200 260,190" stroke="{DARK}" stroke-width="30" fill="none" stroke-linecap="round"/>']
    b.append('<path d="M110,20 C120,60 60,70 60,140 C60,220 150,250 210,230 C240,220 250,200 260,190" stroke="#ffcdd2" stroke-width="18" fill="none"/>')
    b.append('<circle cx="125" cy="140" r="30" fill="#795548" stroke="#4e342e"/>')
    b.append('<rect x="98" y="45" width="24" height="8" fill="#212121"/><rect x="238" y="186" width="8" height="24" fill="#212121"/>')
    # gastric gland magnified
    b.append('<path d="M150,135 C220,120 250,140 280,150" stroke="#e65100" stroke-width="2" fill="none"/><path d="M276,144 l8,7 l-10,3 z" fill="#e65100"/>')
    b.append('<circle cx="370" cy="150" r="90" fill="#fbe9e7" stroke="#795548" stroke-width="2"/>')
    for x in (320, 370, 420):
        b.append(f'<path d="M{x-12},75 L{x-12},215 Q{x},230 {x+12},215 L{x+12},75" fill="#ffccbc" stroke="#6d4c41"/>')
        b.append(f'<path d="M{x},75 L{x},210" stroke="#3e2723" stroke-width="2"/>')
        b.append(''.join(f'<circle cx="{x-7}" cy="{y}" r="4" fill="#fff59d"/><circle cx="{x+7}" cy="{y}" r="4" fill="#fff59d"/>' for y in (95, 115)))
        b.append(''.join(f'<circle cx="{x-7}" cy="{y}" r="4" fill="#4fc3f7"/><circle cx="{x+7}" cy="{y}" r="4" fill="#4fc3f7"/>' for y in (150, 170)))
        b.append(''.join(f'<circle cx="{x-7}" cy="{y}" r="4" fill="#424242"/><circle cx="{x+7}" cy="{y}" r="4" fill="#424242"/>' for y in (195,)))
    b.append(pointer(130, 30, 170, 15, lab(L, 'cardiacp')))
    b.append(pointer(100, 50, 40, 50, lab(L, 'cardiacs'), 'end') + pointer(240, 200, 40, 100, lab(L, 'pylorics'), 'end'))
    b.append(pointer(120, 245, 150, 265, lab(L, 'pyloricp')) + txt(370, 260, L['glands'], 11, 'middle', 'bold'))
    b.append(pointer(420, 80, 470, 70, lab(L, 'pore')) + pointer(427, 105, 470, 105, lab(L, 'mucous')))
    b.append(pointer(427, 160, 470, 150, lab(L, 'hcl')) + pointer(427, 195, 470, 195, lab(L, 'pepsinogen')))
    return svg_wrap('<g transform="translate(60,0)">' + ''.join(b) + '</g>', 660, 280, L['title'])


# ---- Figure 8.12 Digestive glands --------------------------------------------
def glands(L):
    b = ['<rect x="200" y="15" width="16" height="60" fill="#e57373"/>']
    b.append(f'<path d="M216,70 C300,60 330,120 310,190 C295,240 230,235 215,200 L210,150" fill="{PINK}" stroke="{DARK}" stroke-width="2"/>')
    b.append('<path d="M70,90 C120,60 260,60 300,80 C280,110 230,130 120,150 C80,150 60,120 70,90 Z" fill="#6d4c41"/>')
    b.append('<ellipse cx="120" cy="150" rx="10" ry="16" fill="#43a047"/>')
    b.append('<path d="M175,120 L175,200 M120,160 L175,175" stroke="#2e7d32" stroke-width="3"/>')
    b.append('<path d="M180,200 C210,195 250,200 280,212" stroke="#ffb74d" stroke-width="12" stroke-linecap="round"/>')
    b.append(f'<path d="M210,160 C160,170 150,200 160,225 C170,250 200,250 215,245" stroke="{RED}" stroke-width="14" fill="none"/>')
    b.append(pointer(120, 145, 80, 30, lab(L, 'gall'), 'end') + pointer(208, 30, 260, 20, lab(L, 'oesophagus')))
    b.append(pointer(290, 80, 340, 80, lab(L, 'liver')) + pointer(305, 160, 340, 160, lab(L, 'stomach')))
    b.append(pointer(260, 208, 340, 230, lab(L, 'pancreas')) + pointer(175, 190, 80, 220, lab(L, 'bileduct'), 'end'))
    return svg_wrap(''.join(b), 440, 260, L['title'])


# ---- Figure 8.13 Structure of villus -----------------------------------------
def villus(L):
    b = ['<rect x="30" y="40" width="150" height="190" rx="20" fill="#ce93d8" stroke="#6a1b9a"/>',
         '<rect x="55" y="40" width="100" height="190" fill="#7e57c2"/>']
    for y in (80, 120, 160, 200):
        b.append(f'<path d="M30,{y} h150" stroke="#4a148c" stroke-width="5"/>')
    b.append('<path d="M180,140 C220,140 230,150 260,150" stroke="#1565c0" stroke-width="4" fill="none"/><path d="M258,142 l12,8 l-12,8 z" fill="#1565c0"/>')
    for i, x in enumerate((300, 360, 420)):
        b.append(f'<path d="M{x-22},240 L{x-22},90 Q{x},50 {x+22},90 L{x+22},240" fill="#ce93d8" stroke="#6a1b9a" stroke-width="2"/>')
        b.append(f'<path d="M{x-12},240 L{x-12},100 Q{x},80 {x+12},100 L{x+12},240" fill="none" stroke="#e53935" stroke-width="2"/>')
        b.append(f'<path d="M{x-12},150 L{x+12},140 M{x-12},190 L{x+12},180" stroke="#1e88e5" stroke-width="1.5"/>')
        b.append(f'<path d="M{x},240 L{x},110" stroke="#fff9c4" stroke-width="5"/>')
    b.append('<rect x="275" y="240" width="170" height="20" fill="#9fa8da"/>')
    b.append(pointer(110, 50, 150, 20, lab(L, 'small')) + pointer(100, 120, 60, 280, lab(L, 'folds'), 'end'))
    b.append(pointer(440, 80, 470, 70, lab(L, 'single')) + pointer(432, 160, 470, 160, lab(L, 'capillaries')))
    b.append(pointer(420, 200, 470, 215, lab(L, 'lacteal')))
    return svg_wrap('<g transform="translate(30,0)">' + ''.join(b) + '</g>', 610, 300, L['title'])


# ---- Figure 8.14 Large intestine ---------------------------------------------
def large_intestine(L):
    c = '#e57373'
    b = [f'<path d="M110,250 L110,70 C110,50 120,45 140,45 L340,45 C360,45 370,55 370,75 L370,220 C370,250 330,240 300,260 C280,275 250,270 240,285 L240,320" stroke="{c}" stroke-width="40" fill="none" stroke-linejoin="round"/>']
    b.append('<path d="M110,250 L110,70 C110,50 120,45 140,45 L340,45 C360,45 370,55 370,75 L370,220 C370,250 330,240 300,260 C280,275 250,270 240,285 L240,320" stroke="#fff3e0" stroke-width="3" stroke-dasharray="6 10" fill="none"/>')
    b.append(f'<path d="M110,270 q20,5 30,20" stroke="{c}" stroke-width="10" fill="none" stroke-linecap="round"/>')
    b.append(pointer(240, 50, 240, 20, lab(L, 'transverse'), 'middle') + pointer(372, 140, 420, 140, lab(L, 'descending')))
    b.append(pointer(92, 170, 60, 170, lab(L, 'ascending'), 'end') + pointer(140, 288, 160, 315, lab(L, 'appendix')))
    b.append(pointer(310, 255, 400, 270, lab(L, 'sigmoid')) + pointer(258, 310, 300, 320, lab(L, 'rectum')))
    return svg_wrap('<g transform="translate(60,0)">' + ''.join(b) + '</g>', 580, 340, L['title'])


# ---- Figure 8.15 Gastric ulcer -----------------------------------------------
def ulcer(L):
    b = [f'<path d="M280,20 C280,60 240,70 230,110 C215,170 260,220 330,215 C390,210 420,160 400,90 C390,60 360,50 340,20" fill="{PINK}" stroke="{DARK}" stroke-width="3"/>']
    b.append('<circle cx="300" cy="170" r="18" fill="none" stroke="#fff" stroke-width="2"/><circle cx="300" cy="170" r="6" fill="#4e342e"/>')
    b.append('<rect x="40" y="70" width="150" height="120" fill="#ef9a9a" stroke="#b71c1c"/>')
    b.append('<path d="M60,70 C70,140 160,140 170,70" fill="#3e2723"/>')
    b.append('<path d="M40,150 h150 M40,170 h150" stroke="#ffcdd2" stroke-width="5"/>')
    b.append('<path d="M100,150 l-10,25 l25,0 z" fill="#212121"/>')
    b.append('<path d="M100,170 L170,240 L300,175" stroke="#212121" stroke-width="1.5" fill="none"/>' + ''.join(txt(170, 258 + i * 13, t, 12, 'middle', 'bold') for i, t in enumerate(lab(L, 'sore'))))
    b.append(pointer(400, 160, 440, 200, lab(L, 'stomach')))
    return svg_wrap(''.join(b), 540, 290, L['title'])


# ---- label dictionaries ------------------------------------------------------
FIG = {
    'digestive': {
        'en': dict(title='Figure 8.8: General outline of human digestive system', salivary=['Salivary', 'glands'], pharynx='Pharynx', epiglottis='Epiglottis', oesophagus='Oesophagus', stomach='Stomach', pancreas='Pancreas', pduct='Pancreatic duct', bileduct=['Common bile', 'duct'], colon='Colon', caecum='Caecum', rectum='Rectum', anus='Anus', large=['Large', 'intestine'], oral=['Oral', 'cavity'], liver='Liver', gall='Gall bladder', duodenum='Duodenum', jejunum='Jejunum', ileum='Ileum', appendix='Appendix', small=['Small', 'intestine']),
        'ur': dict(title='شکل 8.8', salivary=['لعابی', 'غدود'], pharynx='حلق (فیرنکس)', epiglottis='اپی گلوٹس', oesophagus='غذائی نالی', stomach='معدہ', pancreas='لبلبہ', pduct='لبلبے کی نالی', bileduct=['مشترکہ صفراوی', 'نالی'], colon='کولون', caecum='سیکم', rectum='ریکٹم', anus='مقعد', large=['بڑی', 'آنت'], oral=['منہ کا', 'خلا'], liver='جگر', gall='پتہ', duodenum='ڈیوڈینم', jejunum='جیجونم', ileum='آئیلیم', appendix='اپینڈکس', small=['چھوٹی', 'آنت']),
        'ps': dict(title='شکل 8.8', salivary=['د لاړو', 'غدې'], pharynx='حلق (فارنکس)', epiglottis='اپي ګلوټس', oesophagus='مرۍ', stomach='معده', pancreas='پانقراس', pduct='د پانقراس نل', bileduct=['ګډ صفراوي', 'نل'], colon='کولون', caecum='سیکم', rectum='رکتم', anus='مقعد', large=['لویه', 'کولمه'], oral=['د خولې', 'تشه'], liver='ځيګر', gall='د صفرا کڅوړه', duodenum='دیوډینم', jejunum='جیجونم', ileum='ایلیم', appendix='اپنډکس', small=['کوچنۍ', 'کولمه']),
    },
    'buccal': {
        'en': dict(title='Figure 8.9: Parts of Buccal Cavity', hard='Hard palate', soft='Soft palate', ptonsil='Pharyngeal tonsil', uvula='Uvula', paltonsil='Palatine tonsil', root='Root of the tongue', lingual='Lingual tonsil', lip='Labium, or lip', cheek='Cheek', body=['Body of the', 'tongue']),
        'ur': dict(title='شکل 8.9', hard='سخت تالو', soft='نرم تالو', ptonsil='حلقی ٹانسل', uvula='کوا (یوولا)', paltonsil='تالو کا ٹانسل', root='زبان کی جڑ', lingual='لسانی ٹانسل', lip='ہونٹ', cheek='گال', body=['زبان کا', 'جسم']),
        'ps': dict(title='شکل 8.9', hard='سخت تالو', soft='نرم تالو', ptonsil='حلقي ټانسل', uvula='کوچنۍ ژبه (یوولا)', paltonsil='د تالو ټانسل', root='د ژبې ریښه', lingual='ژبني ټانسل', lip='شونډه', cheek='اننګی', body=['د ژبې', 'بدن']),
    },
    'peristalsis': {
        'en': dict(title='Figure 8.10: Peristalsis in oesophagus', mixing=['Mixing Movements'], contractmix=['Contractions mix food', 'with digestive juices'], pushes=['Peristalsis - pushes food', 'down the tube'], contracted='Contracted muscle', direction=['Direction of food', 'movement'], relaxed='Relaxed muscle', ball='Ball of food'),
        'ur': dict(title='شکل 8.10', mixing=['ملانے کی حرکات'], contractmix=['سکڑاؤ خوراک کو', 'ہاضم رسوں سے', 'ملاتا ہے'], pushes=['پیریسٹالسس خوراک کو', 'نالی میں نیچے', 'دھکیلتا ہے'], contracted='سکڑا ہوا عضلہ', direction=['خوراک کی حرکت', 'کی سمت'], relaxed='ڈھیلا عضلہ', ball='خوراک کا گولا'),
        'ps': dict(title='شکل 8.10', mixing=['د ګډولو حرکتونه'], contractmix=['انقباض خواړه له', 'هاضمه شیرو سره ګډوي'], pushes=['پیرسټالسس خواړه', 'نل ته ښکته', 'ټېلوي'], contracted='منقبضه عضله', direction=['د خوړو د حرکت', 'لوری'], relaxed='سسته عضله', ball='د خوړو ګوله'),
    },
    'stomach': {
        'en': dict(title='Figure 8.11: Structure of the Stomach', cardiacp='Cardiac portion', cardiacs=['Cardiac', 'sphincter'], pylorics=['Pyloric', 'sphincter'], pyloricp='Pyloric portion', glands='Gastric glands', pore='Pore of gland', mucous=['Mucous secreting', 'cells'], hcl=['HCl secreting', 'cells'], pepsinogen=['Pepsinogen secreting', 'cells']),
        'ur': dict(title='شکل 8.11', cardiacp='کارڈیک حصہ', cardiacs=['کارڈیک', 'اسفنکٹر'], pylorics=['پائیلورک', 'اسفنکٹر'], pyloricp='پائیلورک حصہ', glands='معدے کے غدود', pore='غدود کا سوراخ', mucous=['بلغم خارج کرنے', 'والے خلیے'], hcl=['HCl خارج کرنے', 'والے خلیے'], pepsinogen=['پیپسینوجن خارج', 'کرنے والے خلیے']),
        'ps': dict(title='شکل 8.11', cardiacp='کارډیک برخه', cardiacs=['کارډیک', 'سفنکټر'], pylorics=['پایلوریک', 'سفنکټر'], pyloricp='پایلوریک برخه', glands='معدي غدې', pore='د غدې سوری', mucous=['بلغم افرازوونکې', 'حجرې'], hcl=['HCl افرازوونکې', 'حجرې'], pepsinogen=['پیپسینوجن', 'افرازوونکې حجرې']),
    },
    'glands': {
        'en': dict(title='Figure 8.12: Digestive Glands', gall='Gall bladder', oesophagus='Oesophagus', liver='Liver', stomach='Stomach', pancreas='Pancreas', bileduct=['Common', 'bile duct']),
        'ur': dict(title='شکل 8.12', gall='پتہ', oesophagus='غذائی نالی', liver='جگر', stomach='معدہ', pancreas='لبلبہ', bileduct=['مشترکہ', 'صفراوی نالی']),
        'ps': dict(title='شکل 8.12', gall='د صفرا کڅوړه', oesophagus='مرۍ', liver='ځيګر', stomach='معده', pancreas='پانقراس', bileduct=['ګډ', 'صفراوي نل']),
    },
    'villus': {
        'en': dict(title='Figure 8.13: Structure of villus', small=['Small', 'intestine'], folds=['Folds in', 'Inner wall'], single=['Single', 'villus'], capillaries=['Blood', 'capillaries'], lacteal='Lacteal'),
        'ur': dict(title='شکل 8.13', small=['چھوٹی', 'آنت'], folds=['اندرونی دیوار', 'کی تہیں'], single=['ایک', 'ولس'], capillaries=['خون کی شعری', 'نالیاں'], lacteal='لیکٹیل'),
        'ps': dict(title='شکل 8.13', small=['کوچنۍ', 'کولمه'], folds=['د داخلي دېوال', 'ګونځې'], single=['یو', 'ویلس'], capillaries=['د وینې شعریه', 'رګونه'], lacteal='لاکټیل'),
    },
    'large': {
        'en': dict(title='Figure 8.14: Large Intestine', transverse='Transverse colon', descending='Descending colon', ascending='Ascending colon', appendix='Appendix', sigmoid='sigmoid colon', rectum='Rectum'),
        'ur': dict(title='شکل 8.14', transverse='عرضی کولون', descending='نزولی کولون', ascending='صعودی کولون', appendix='اپینڈکس', sigmoid='سگمائیڈ کولون', rectum='ریکٹم'),
        'ps': dict(title='شکل 8.14', transverse='عرضي کولون', descending='ښکته کېدونکی کولون', ascending='پورته کېدونکی کولون', appendix='اپنډکس', sigmoid='سیګمایډ کولون', rectum='رکتم'),
    },
    'ulcer': {
        'en': dict(title='Figure 8.15: Gastric ulcer', sore=['Sore (gastric ulcer)'], stomach='Stomach'),
        'ur': dict(title='شکل 8.15', sore=['زخم (معدے کا السر)'], stomach='معدہ'),
        'ps': dict(title='شکل 8.15', sore=['زخم (معدي زخم)'], stomach='معده'),
    },
}
FN = dict(digestive=digestive, buccal=buccal, peristalsis=peristalsis, stomach=stomach, glands=glands, villus=villus, large=large_intestine, ulcer=ulcer)


def three(key):
    return [FN[key](FIG[key][lang]) for lang in ('en', 'ur', 'ps')]
