# -*- coding: utf-8 -*-
"""Unit 6 Enzymes — PDF 119-131 (printed 116-128)."""
import math
from bio9_tools import Section, svg_wrap, txt
from unit4_figs import multiline
from unit4_figs2 import pointer

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
PR = ('Point to remember', 'یاد رکھنے کا نکتہ', 'د یادولو ټکی')
STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')


def axes(x0, y0, w, h, xl, yl, xticks=(), vertical_ylabel=True):
    b = [f'<path d="M{x0},{y0} V{y0-h} M{x0},{y0} H{x0+w}" stroke="#333" stroke-width="2"/>',
         f'<polygon points="{x0-4},{y0-h} {x0+4},{y0-h} {x0},{y0-h-8}" fill="#333"/><polygon points="{x0+w},{y0-4} {x0+w},{y0+4} {x0+w+8},{y0}" fill="#333"/>']
    for x, lab in xticks:
        b.append(f'<path d="M{x},{y0} v5" stroke="#333"/>' + txt(x, y0 + 18, lab, 11, 'middle'))
    b.append(txt(x0 + w / 2, y0 + 36, xl, 12, 'middle', 'bold'))
    b.append(f'<text x="{x0-20}" y="{y0 - h/2}" font-size="12" font-weight="bold" text-anchor="middle" transform="rotate(-90 {x0-20} {y0 - h/2})" font-family="Segoe UI, Noto Sans, sans-serif">{yl}</text>')
    return ''.join(b)


def activation_fig(L):
    b = [txt(240, 20, L['head'], 16, 'middle', 'bold', '#0277bd')]
    b.append('<path d="M60,230 L60,40 M60,230 L60,330" stroke="#1e88e5" stroke-width="4"/><polygon points="54,45 66,45 60,30" fill="#1e88e5"/><polygon points="54,325 66,325 60,340" fill="#1e88e5"/>')
    b.append(f'<text x="40" y="140" font-size="11" transform="rotate(-90 40 140)" text-anchor="middle" font-weight="bold">{L["supplied"]}</text><text x="40" y="285" font-size="11" transform="rotate(-90 40 285)" text-anchor="middle" font-weight="bold">{L["released"]}</text>')
    b.append('<path d="M70,180 L110,180 C150,180 150,50 190,50 C240,50 230,300 300,300 L340,300" stroke="#8e244d" stroke-width="3" fill="none"/>')
    b.append('<path d="M70,180 L110,180 C150,180 160,120 190,120 C240,120 230,300 300,300" stroke="#64b5f6" stroke-width="5" fill="none"/>')
    b.append('<path d="M70,50 H420 M70,120 H300 M70,180 H420" stroke="#333" stroke-dasharray="6 4"/>')
    b.append('<path d="M330,180 V58 M300,175 V125 M320,185 V292" stroke="#222" stroke-width="1.5"/>')
    b.append(txt(200, 45, L['without'], 11, 'start', 'bold') + txt(205, 116, L['with'], 10, 'start', 'bold', '#1565c0'))
    b.append(multiline(340, 80, L['ae_without']) + multiline(305, 140, L['ae_with']) + multiline(330, 210, L['overall']))
    b.append('<rect x="75" y="185" width="85" height="32" fill="#fff8e1" stroke="#333"/>' + multiline(80, 198, L['react']))
    b.append('<rect x="290" y="305" width="80" height="32" fill="#fff8e1" stroke="#333"/>' + multiline(295, 318, L['prod']))
    return svg_wrap(''.join(b), 470, 350, L['title'])


AE_EN = dict(title='Figure 6.1: Activation energy', head='Enzyme Action', supplied='Energy supplied', released='Energy released', without='Without enzyme', with_='',
             **{'with': 'With enzyme'}, ae_without=['Activation', 'energy', 'without', 'enzyme'], ae_with=['Activation', 'energy', 'with enzyme'], overall=['Overall energy', 'released during', 'reaction'],
             react=['Reactions:', 'Glucose + O₂'], prod=['Products:', 'CO₂ + H₂O'])
AE_UR = dict(AE_EN, title='شکل 6.1', head='انزائم کا عمل', supplied='فراہم کردہ توانائی', released='خارج شدہ توانائی', without='انزائم کے بغیر', **{'with': 'انزائم کے ساتھ'},
             ae_without=['ایکٹیویشن', 'انرجی', 'انزائم کے', 'بغیر'], ae_with=['ایکٹیویشن', 'انرجی', 'انزائم کے ساتھ'], overall=['تعامل میں خارج', 'ہونے والی کل', 'توانائی'], react=['متعاملات:', 'Glucose + O₂'], prod=['حاصلات:', 'CO₂ + H₂O'])
AE_PS = dict(AE_EN, title='شکل 6.1', head='د انزایم عمل', supplied='ورکړل شوې انرژي', released='خوشې شوې انرژي', without='بې انزایمه', **{'with': 'له انزایم سره'},
             ae_without=['د فعالولو', 'انرژي', 'بې', 'انزایمه'], ae_with=['د فعالولو', 'انرژي', 'له انزایم سره'], overall=['د تعامل پر مهال', 'ټوله خوشې', 'شوې انرژي'], react=['تعاملونه:', 'Glucose + O₂'], prod=['محصولات:', 'CO₂ + H₂O'])


def enzyme_shape(x, y, col='#fff9c4', site='cup'):
    if site == 'cup':
        return f'<path d="M{x-55},{y} q0,55 55,55 q55,0 55,-55 h-25 q-10,-25 -30,0 q-20,-25 -30,0 z" fill="{col}" stroke="#555" stroke-width="2"/>'
    return f'<path d="M{x-55},{y} q0,55 55,55 q55,0 55,-55 q-20,-30 -55,-30 q-35,0 -55,30 z" fill="{col}" stroke="#555" stroke-width="2"/>'


def cofactor_fig(L):
    b = [enzyme_shape(110, 110), '<path d="M70,70 q40,-40 80,0 l-10,10 q-30,-20 -60,0 z" fill="#4fc3f7" stroke="#0277bd"/>', '<rect x="115" y="100" width="14" height="14" rx="3" fill="#ec407a"/>']
    b.append(txt(110, 62, L['substrate'], 11, 'middle', 'bold') + txt(90, 145, L['ezyme'], 11, 'middle', 'bold') + pointer(126, 110, 170, 140, L['prosthetic']))
    b.append(enzyme_shape(330, 110, '#f06292') + '<path d="M290,70 q40,-40 80,0 l-10,10 q-30,-20 -60,0 z" fill="#4fc3f7" stroke="#0277bd"/>')
    b.append('<path d="M360,160 l20,20" stroke="#5e35b1" stroke-width="3"/><rect x="378" y="175" width="18" height="18" fill="#7e57c2"/>')
    b.append(txt(330, 62, L['substrate'], 11, 'middle', 'bold') + txt(330, 140, L['enzyme'], 11, 'middle', 'bold', '#fff') + txt(400, 210, L['coenzyme'], 11, 'start', 'bold'))
    return svg_wrap(''.join(b), 470, 225, L['title'])


CF_EN = dict(title='Figure 6.2: Cofactors of enzymes', substrate='Substrate', ezyme='Ezyme', enzyme='Enzyme', prosthetic=['Prosthetic', 'group'], coenzyme='Coenzyme')
CF_UR = dict(title='شکل 6.2', substrate='سبسٹریٹ', ezyme='انزائم', enzyme='انزائم', prosthetic=['پروستھیٹک', 'گروپ'], coenzyme='کو انزائم')
CF_PS = dict(title='شکل 6.2', substrate='سبسټریټ', ezyme='انزایم', enzyme='انزایم', prosthetic=['پروسټیټیک', 'ګروپ'], coenzyme='کو انزایم')


def specificity_fig(L):
    b = [enzyme_shape(220, 170), '<path d="M120,60 q50,-45 100,0 l-12,12 q-10,-15 -25,0 q-15,-12 -25,0 q-15,-15 -26,0 z" fill="#5c6bc0" stroke="#283593"/>',
         '<path d="M260,60 q50,-45 100,0 l-12,12 q-20,-20 -40,4 q-20,-20 -36,-4 z" fill="#5c6bc0" stroke="#283593"/>']
    b.append(txt(170, 12, L['s1'], 12, 'middle', 'bold') + txt(310, 12, L['s2'], 12, 'middle', 'bold'))
    b.append('<path d="M175,95 L205,135" stroke="#333" stroke-width="2"/><polygon points="200,138 210,140 207,130" fill="#333"/><path d="M300,95 L245,135" stroke="#333" stroke-width="2" stroke-dasharray="4 3"/><polygon points="248,128 240,140 252,138" fill="#333"/>')
    b.append(txt(140, 115, L['fits'], 12, 'start', 'bold') + txt(300, 115, L['nofit'], 12, 'start', 'bold') + txt(250, 205, L['enzyme'], 12, 'middle', 'bold'))
    b.append(pointer(205, 180, 160, 215, L['site'], 'end'))
    return svg_wrap(''.join(b), 430, 240, L['title'])


SP_EN = dict(title='Figure 5.3: shape of active site of enzyme and its specificity', s1='Substrate 1', s2='Substrate 2', fits='Fits in', nofit='Does not fit in', enzyme='Enzyme', site=['Active', 'site'])
SP_UR = dict(title='شکل 5.3 (جیسا چھپا ہے)', s1='سبسٹریٹ 1', s2='سبسٹریٹ 2', fits='فٹ ہوتا ہے', nofit='فٹ نہیں ہوتا', enzyme='انزائم', site=['ایکٹیو', 'سائٹ'])
SP_PS = dict(title='شکل 5.3 (لکه چې چاپ شوې)', s1='سبسټریټ 1', s2='سبسټریټ 2', fits='سمون خوري', nofit='سمون نه خوري', enzyme='انزایم', site=['فعال', 'ځای'])


def model_fig(L, induced=False):
    b = []
    xs = [80, 240, 400]
    b.append(enzyme_shape(xs[0], 120, '#fffde7', 'cup' if not induced else 'round'))
    b.append('<path d="M45,60 q35,-35 70,0 l-10,10 q-10,-12 -25,0 q-12,-12 -25,0 z" fill="#4fc3f7" stroke="#0277bd"/>' + txt(80, 50, L['substrate'], 11, 'middle', 'bold'))
    b.append(f'<circle cx="{xs[1]}" cy="140" r="52" fill="#fffde7" stroke="#555" stroke-width="2"/><path d="M{xs[1]-50},125 q50,-55 100,0 z" fill="#4fc3f7"/>')
    b.append(enzyme_shape(xs[2], 120, '#fffde7') + f'<path d="M{xs[2]-40},60 l25,-20 l20,25 z M{xs[2]+15},55 l25,-25 l25,20 l-20,20 z" fill="#f06292" stroke="#ad1457"/>')
    b.append(txt(xs[2] - 25, 50, L['p1'], 10, 'middle', 'bold') + txt(xs[2] + 45, 40, L['p2'], 10, 'middle', 'bold'))
    b.append(txt(xs[0], 160, L['enzyme'], 11, 'middle', 'bold') + txt(xs[2], 160, L['enzyme'], 11, 'middle', 'bold') + txt(xs[1], 215, L['complex'], 11, 'middle', 'bold'))
    for x in (150, 310):
        b.append(f'<path d="M{x},180 h25" stroke="#333" stroke-width="2"/><polygon points="{x+25},175 {x+33},180 {x+25},185" fill="#333"/>')
    if L.get('site'):
        b.append(pointer(80, 125, 40, 200, L['site'], 'middle'))
    return svg_wrap(''.join(b), 480, 230, L['title'])


LK_EN = dict(title='Figure 6.4: Lock and Key Model of enzyme action', substrate='Substrate', p1='Product 1', p2='Product 2', enzyme='Enzyme', complex='Enzyme-Substrate Complex', site=['Active', 'site'])
LK_UR = dict(title='شکل 6.4', substrate='سبسٹریٹ', p1='حاصل 1', p2='حاصل 2', enzyme='انزائم', complex='انزائم سبسٹریٹ کمپلیکس', site=['ایکٹیو', 'سائٹ'])
LK_PS = dict(title='شکل 6.4', substrate='سبسټریټ', p1='محصول 1', p2='محصول 2', enzyme='انزایم', complex='انزایم-سبسټریټ کمپلېکس', site=['فعال', 'ځای'])
IF_EN = dict(LK_EN, title='Figure 6.5: Induced Fit Model of enzyme action', site=None)
IF_UR = dict(LK_UR, title='شکل 6.5', site=None)
IF_PS = dict(LK_PS, title='شکل 6.5', site=None)


def temp_graph(L):
    x0, y0 = 70, 300
    sx = lambda t: x0 + t * 6
    b = [axes(x0, y0, 380, 210, L['xl'], L['yl'], [(sx(t), str(t)) for t in (0, 10, 20, 30, 40, 50, 60)])]
    pts = []
    for t in range(0, 61):
        r = (t / 37) ** 2 * 180 if t <= 37 else 180 * max(0, 1 - ((t - 37) / 23) ** 1.6)
        pts.append(f'{sx(t):.1f},{y0 - r:.1f}')
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#4fc3f7" stroke-width="4"/>')
    for i, (lines, x) in enumerate(zip(L['boxes'], (95, 215, 335))):
        b.append(f'<rect x="{x-55}" y="10" width="110" height="62" fill="#37474f"/>' + multiline(x, 26, lines, 'middle', 10).replace('#212121', '#fff'))
    return svg_wrap(''.join(b), 480, 345, L['title'])


TG_EN = dict(title='Figure 6.6: Effect of temperature on enzyme activity', xl='Temperature (°C)', yl='Rate of reaction',
             boxes=[['Heat energy causes', 'more collisions', 'between enzymes', 'and substrate'], ['Optimum', 'temperature', 'for humans is', 'close to 37°C'], ['Enzymes', 'denature at high', 'temperatures', 'so rate falls rapidally']])
TG_UR = dict(title='شکل 6.6', xl='درجۂ حرارت (°C)', yl='تعامل کی شرح', boxes=[['حرارتی توانائی سے', 'انزائمز اور سبسٹریٹ', 'میں زیادہ ٹکراؤ'], ['انسانوں کے لیے', 'موزوں ترین درجۂ', 'حرارت تقریباً 37°C'], ['زیادہ درجۂ حرارت پر', 'انزائمز ڈی نیچر', 'ہو کر شرح تیزی', 'سے گرتی ہے']])
TG_PS = dict(title='شکل 6.6', xl='تودوخه (°C)', yl='د تعامل کچه', boxes=[['د تودوخې انرژي', 'د انزایمونو او سبسټریټ', 'ترمنځ ډېر ټکرونه'], ['د انسانانو لپاره', 'غوره تودوخه', 'شاوخوا 37°C'], ['په لوړه تودوخه', 'انزایمونه ډي نیچر', 'کېږي او کچه ژر', 'راټیټېږي']])


def ph_graph(L):
    x0, y0 = 60, 260
    sx = lambda p: x0 + (p - 4) * 28
    b = [axes(x0, y0, 220, 200, 'pH', L['yl'], [(sx(p), str(p)) for p in range(4, 12)])]
    pts = [f'{sx(p):.1f},{y0 - 180 * math.exp(-((p - 7.8) ** 2) / 2.2):.1f}' for p in [4 + i * 0.1 for i in range(71)]]
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#4fc3f7" stroke-width="4"/>')
    b.append('<rect x="120" y="20" width="110" height="24" fill="#37474f"/>' + txt(175, 37, L['opt'], 12, 'middle', 'bold', '#fff'))
    return svg_wrap(''.join(b), 320, 310, L['title'])


PG_EN = dict(title='Figure 6.7: The effect of pH on enzyme activity', yl='Increasing enzyme activity', opt='Optimum pH')
PG_UR = dict(title='شکل 6.7', yl='انزائم کی بڑھتی سرگرمی', opt='موزوں ترین pH')
PG_PS = dict(title='شکل 6.7', yl='د انزایم زیاتېدونکی فعالیت', opt='غوره pH')


def substrate_graph(L):
    x0, y0 = 70, 240
    b = [axes(x0, y0, 300, 200, L['xl'] + ' →', L['yl'] + ' →')]
    b.append(f'<path d="M{x0},{y0-60} L{x0+90},{y0-170} H{x0+300}" stroke="#e91e63" stroke-width="3" fill="none"/>')
    b.append(f'<path d="M{x0+150},{y0-110} L{x0+110},{y0-160}" stroke="#333"/><polygon points="{x0+107},{y0-163} {x0+117},{y0-160} {x0+111},{y0-152}" fill="#333"/>' + txt(x0 + 160, y0 - 95, L['sat'], 12, 'middle', 'bold'))
    return svg_wrap(''.join(b), 420, 290, L['title'])


SG_EN = dict(title='Figure 6.8: The effect of substrate concentration on enzyme activity', xl='Substrate concentration', yl='Enzyme activity', sat='Saturation point')
SG_UR = dict(title='شکل 6.8', xl='سبسٹریٹ کا ارتکاز', yl='انزائم کی سرگرمی', sat='سیچوریشن پوائنٹ')
SG_PS = dict(title='شکل 6.8', xl='د سبسټریټ غلظت', yl='د انزایم فعالیت', sat='د مړښت ټکی')


def three(fn, a, b, c):
    return fn(a), fn(b), fn(c)


def exercise_figures(title):
    b = []
    # MCQ iii graph
    x0, y0 = 70, 150
    b.append(axes(x0, y0, 200, 120, 'Temperature', 'Rate', [(x0, '0'), (x0 + 50, '20'), (x0 + 100, '40'), (x0 + 150, '60')]))
    b.append(f'<path d="M{x0},{y0} Q{x0+70},{y0-160} {x0+100},{y0-100} Q{x0+130},{y0-20} {x0+160},{y0-10}" stroke="#333" fill="none" stroke-width="2"/>')
    b.append(txt(170, 15, 'MCQ iii: Rate of Enzyme catalyzed reaction', 11, 'middle', 'bold'))
    # LQ iv diagram
    b.append(txt(470, 15, 'C iv: enzyme, substrate and products', 11, 'middle', 'bold'))
    for i, x in enumerate((360, 470, 580)):
        b.append(f'<path d="M{x-35},120 q0,35 35,35 q35,0 35,-35 h-15 l-6,-12 l-6,12 h-16 l-6,-12 l-6,12 z" fill="#5c8fd6"/>')
    b.append(''.join(f'<circle cx="{330 + k*14}" cy="60" r="6" fill="none" stroke="#333"/>' for k in range(4)) + '<path d="M325,60 h60" stroke="#333"/>')
    b.append(txt(318, 52, 'A', 12, 'end', 'bold') + txt(318, 125, 'B →', 12, 'end', 'bold') + txt(560, 50, 'C', 12, 'end', 'bold'))
    b.append(''.join(f'<circle cx="{570 + k*14 + (k > 1)*12}" cy="60" r="6" fill="none" stroke="#333"/>' for k in range(4)))
    b.append(''.join(f'<circle cx="{450 + k*12}" cy="{100 - (k % 2)*12}" r="6" fill="none" stroke="#333"/>' for k in range(4)))
    b.append('<path d="M410,130 h20 M520,130 h20" stroke="#333" stroke-width="2"/>')
    # LQ vi graphs
    x0, y0 = 70, 330
    b.append(axes(x0, y0, 160, 110, 'Temperature (°C)', 'Rate', [(x0, '0'), (x0 + 40, '20'), (x0 + 80, '40'), (x0 + 120, '60')]))
    b.append(f'<path d="M{x0},{y0} L{x0+80},{y0-95} L{x0+110},{y0}" stroke="#333" fill="none" stroke-width="2"/>' + txt(150, 395, 'Graph A', 11, 'middle', 'bold'))
    x0 = 360
    b.append(axes(x0, y0, 220, 110, 'pH', 'Rate', [(x0, '0'), (x0 + 60, '4'), (x0 + 120, '8'), (x0 + 180, '12')]))
    b.append(f'<path d="M{x0+5},{y0} L{x0+25},{y0-100} L{x0+65},{y0}" stroke="#333" fill="none" stroke-width="2"/><path d="M{x0+50},{y0} Q{x0+130},{y0-200} {x0+200},{y0}" stroke="#333" fill="none" stroke-width="2"/>')
    b.append(txt(x0 + 40, y0 - 105, 'pepsin', 11) + txt(x0 + 175, y0 - 100, 'Pancreatic lipase', 11) + txt(470, 395, 'Graph B', 11, 'middle', 'bold'))
    b.append(txt(320, 212, 'C vi: Graph A and Graph B', 11, 'middle', 'bold'))
    return svg_wrap(''.join(b), 640, 410, title)


def sections():
    out = []
    s = Section('bio6_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [119])
    s.h('After studying this unit, the students will be able to:', 'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې:')
    s.ul([
        ('Define metabolism and differentiate between catabolism and anabolism.', 'میٹابولزم کی تعریف کر سکیں اور کیٹابولزم اور اینابولزم میں فرق کر سکیں۔', 'میټابولیزم تعریف کړي او د کټابولیزم او انابولیزم ترمنځ توپیر وکړي.'),
        ('Describe enzymes as the proteins that speed up biochemical reactions.', 'انزائمز کو ایسی پروٹینز کے طور پر بیان کر سکیں جو حیاتیاتی کیمیائی تعاملات کو تیز کرتی ہیں۔', 'انزایمونه د هغو پروټینونو په توګه بیان کړي چې بیوکیمیاوي تعاملونه چټکوي.'),
        ('Categorize enzymes as intra and extracellular.', 'انزائمز کو اندرونی اور بیرونی خلوی میں درجہ بند کر سکیں۔', 'انزایمونه په داخل او بهر حجروي ډلبندي کړي.'),
        ('Comprehend that enzymes increase rate of reaction.', 'سمجھ سکیں کہ انزائمز تعامل کی شرح بڑھاتے ہیں۔', 'پوه شي چې انزایمونه د تعامل کچه زیاتوي.'),
        ('State that small quantity of enzyme is effective for large amount of substrate.', 'بیان کر سکیں کہ انزائم کی تھوڑی مقدار سبسٹریٹ کی بڑی مقدار کے لیے مؤثر ہے۔', 'بیان کړي چې د انزایم لږ مقدار د سبسټریټ د ډېر مقدار لپاره اغېزمن دی.'),
        ('Infer that enzymes are specific for specific substrates.', 'نتیجہ اخذ کر سکیں کہ انزائمز مخصوص سبسٹریٹس کے لیے مخصوص ہیں۔', 'پایله واخلي چې انزایمونه د ځانګړو سبسټریټونو لپاره ځانګړي دي.'),
        ('State that some enzymes require co-factor for their functioning.', 'بیان کر سکیں کہ بعض انزائمز کو کام کے لیے کو فیکٹر درکار ہوتا ہے۔', 'بیان کړي چې ځینې انزایمونه د خپلې دندې لپاره کوفکټور ته اړتیا لري.'),
        ('Describe the concept of energy of activation and how it is lowered by enzyme.', 'ایکٹیویشن انرجی کا تصور اور انزائم کے ذریعے اس کی کمی بیان کر سکیں۔', 'د فعالولو د انرژۍ مفهوم او د انزایم په واسطه د هغې کمېدل بیان کړي.'),
        ('Explain the effect of pH, temperature and concentration of substrate on the activity of an enzyme.', 'انزائم کی سرگرمی پر pH، درجۂ حرارت اور سبسٹریٹ کے ارتکاز کے اثر کی وضاحت کر سکیں۔', 'د انزایم پر فعالیت د pH، تودوخې او د سبسټریټ د غلظت اغېز تشریح کړي.'),
        ('Describe, through equation, that enzyme substrate complex is formed and release of enzyme takes place after completing the reaction.', 'مساوات کے ذریعے بیان کر سکیں کہ انزائم سبسٹریٹ کمپلیکس بنتا ہے اور تعامل مکمل ہونے کے بعد انزائم آزاد ہو جاتا ہے۔', 'د معادلې له لارې بیان کړي چې انزایم-سبسټریټ کمپلېکس جوړېږي او د تعامل له بشپړېدو وروسته انزایم خوشې کېږي.'),
        ('Describe the action of enzyme through "Lock and Key Model"', '”لاک اینڈ کی ماڈل“ کے ذریعے انزائم کا عمل بیان کر سکیں', 'د ”قلف او کیلي ماډل“ له لارې د انزایم عمل بیان کړي'),
        ('Describe the specificity of different enzymes for different substrates.', 'مختلف سبسٹریٹس کے لیے مختلف انزائمز کی خصوصیت بیان کر سکیں۔', 'د بېلابېلو سبسټریټونو لپاره د بېلابېلو انزایمونو ځانګړتیا بیان کړي.'),
        ('Relate that specificity of enzyme is due to its shape.', 'تعلق جوڑ سکیں کہ انزائم کی خصوصیت اس کی شکل کی وجہ سے ہے۔', 'وتړي چې د انزایم ځانګړتیا د هغې د بڼې له امله ده.'),
        ('Categorise that proteases will act on proteins only and lipases will act on lipids or fats only.', 'درجہ بند کر سکیں کہ پروٹیزز صرف پروٹینز پر اور لائپیزز صرف لپڈز یا چکنائی پر عمل کرتے ہیں۔', 'ډلبندي کړي چې پروټیازونه یوازې پر پروټینونو او لایپازونه یوازې پر لیپیډونو یا غوړو عمل کوي.'),
    ])
    out.append(s)

    s = Section('bio6_1', '6.1', 'Metabolism', 'میٹابولزم', 'میټابولیزم', [120])
    s.p('The characteristics of living things, such as breathing, growth, reproduction and responsiveness to stimuli are the outcome of chemical reactions taking place inside the body of a living organism. The chemical processes that occur within a living organism in order to maintain life are collectively called metabolism. All these reactions are controlled by specific proteins called enzymes. In this unit, we will study enzymes and how they control metabolism.',
        'جانداروں کی خصوصیات جیسے سانس لینا، نشوونما، تولید اور محرکات پر ردِعمل جاندار کے جسم کے اندر ہونے والے کیمیائی تعاملات کا نتیجہ ہیں۔ زندگی برقرار رکھنے کے لیے جاندار کے اندر ہونے والے کیمیائی عوامل کو مجموعی طور پر میٹابولزم کہتے ہیں۔ یہ تمام تعاملات انزائمز نامی مخصوص پروٹینز کنٹرول کرتی ہیں۔ اس یونٹ میں ہم انزائمز اور میٹابولزم پر ان کے کنٹرول کا مطالعہ کریں گے۔',
        'د ژوندیو شیانو ځانګړتیاوې لکه ساه اخیستل، وده، تکثر او محرکاتو ته ځواب د ژوندي موجود په بدن کې د کیمیاوي تعاملونو پایله دي. هغو کیمیاوي پروسو ته چې د ژوند د ساتلو لپاره په ژوندي موجود کې کېږي په ګډه میټابولیزم ویل کېږي. دا ټول تعاملونه د ځانګړو پروټینونو په واسطه چې انزایمونه بلل کېږي کنټرولېږي. په دې یونټ کې به انزایمونه او دا چې څنګه میټابولیزم کنټرولوي ولولو.')
    s.h('6.1 Metabolism', '6.1 میٹابولزم', '6.1 میټابولیزم')
    s.p('The sum of all chemical reactions going on within a living organism is called metabolism. Metabolism consists of anabolism and catabolism. Anabolism is building up of larger molecules from smaller ones. These type of reactions are known as anabolic reactions. Photosynthesis, is a process by which smaller and simpler molecules (water and carbon dioxide) react to form a larger and complex molecule (glucose). Therefore, it is an example of anabolism. Whereas, catabolism is the breakdown of larger molecules into smaller ones. These type of reactions are known as catabolic reactions. In respiration, a larger and complex molecule (glucose) is broken down into smaller and simpler molecules (carbon dioxide and water). Therefore, it is an example of catabolism.',
        'جاندار کے اندر ہونے والے تمام کیمیائی تعاملات کے مجموعے کو میٹابولزم کہتے ہیں۔ میٹابولزم اینابولزم اور کیٹابولزم پر مشتمل ہے۔ اینابولزم چھوٹے مالیکیولز سے بڑے مالیکیول بنانا ہے۔ ایسے تعاملات کو اینابولک تعاملات کہتے ہیں۔ ضیائی تالیف ایک ایسا عمل ہے جس میں چھوٹے اور سادہ مالیکیول (پانی اور کاربن ڈائی آکسائیڈ) تعامل کر کے بڑا اور پیچیدہ مالیکیول (گلوکوز) بناتے ہیں۔ اس لیے یہ اینابولزم کی مثال ہے۔ جبکہ کیٹابولزم بڑے مالیکیولز کا چھوٹے مالیکیولز میں ٹوٹنا ہے۔ ایسے تعاملات کو کیٹابولک تعاملات کہتے ہیں۔ تنفس میں ایک بڑا اور پیچیدہ مالیکیول (گلوکوز) چھوٹے اور سادہ مالیکیولز (کاربن ڈائی آکسائیڈ اور پانی) میں ٹوٹتا ہے۔ اس لیے یہ کیٹابولزم کی مثال ہے۔',
        'په ژوندي موجود کې د روانو ټولو کیمیاوي تعاملونو مجموعې ته میټابولیزم ویل کېږي. میټابولیزم انابولیزم او کټابولیزم لري. انابولیزم له کوچنیو مالیکولونو د لویو مالیکولونو جوړول دي. دې ډول تعاملونو ته انابولیک تعاملونه ویل کېږي. فوتوسنتز هغه پروسه ده چې کوچني او ساده مالیکولونه (اوبه او کاربن ډای اکساید) تعامل کوي او لوی او پېچلی مالیکول (ګلوکوز) جوړوي. نو دا د انابولیزم بېلګه ده. په داسې حال کې چې کټابولیزم د لویو مالیکولونو په کوچنیو ماتېدل دي. دې ډول تعاملونو ته کټابولیک تعاملونه ویل کېږي. په تنفس کې یو لوی او پېچلی مالیکول (ګلوکوز) په کوچنیو او ساده مالیکولونو (کاربن ډای اکساید او اوبو) ماتېږي. نو دا د کټابولیزم بېلګه ده.')
    s.lines([('Photosynthesis: 6CO₂ + 12H₂O —(sunlight, chlorophyl)→ C₆H₁₂O₆ + 6O₂ + 6H₂O', 'ضیائی تالیف: 6CO₂ + 12H₂O —(سورج کی روشنی، کلوروفل)→ C₆H₁₂O₆ + 6O₂ + 6H₂O', 'فوتوسنتز: 6CO₂ + 12H₂O —(د لمر رڼا، کلوروفیل)→ C₆H₁₂O₆ + 6O₂ + 6H₂O'),
             ('Respiration: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP', 'تنفس: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP', 'تنفس: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP'),
             ('Comparison of anabolic reaction and catabolic reaction', 'اینابولک اور کیٹابولک تعامل کا موازنہ', 'د انابولیک او کټابولیک تعامل پرتله')])
    s.p('Enzymes are biological catalysts which speed up the chemical reactions within the body, without getting consumed. The molecules that react in the enzyme-catalysed reactions are called substrates and the molecules produced in the reactions are called products.',
        'انزائمز حیاتیاتی عمل انگیز ہیں جو خود خرچ ہوئے بغیر جسم کے اندر کیمیائی تعاملات کو تیز کرتے ہیں۔ انزائم کے ذریعے عمل انگیز تعاملات میں تعامل کرنے والے مالیکیولز کو سبسٹریٹس اور تعاملات میں بننے والے مالیکیولز کو حاصلات (پروڈکٹس) کہتے ہیں۔',
        'انزایمونه بیولوژیکي کتلستونه دي چې پرته له دې چې پخپله مصرف شي د بدن دننه کیمیاوي تعاملونه چټکوي. هغو مالیکولونو ته چې په انزایمي تعاملونو کې تعامل کوي سبسټریټونه او په تعاملونو کې جوړ شوو مالیکولونو ته محصولات ویل کېږي.')
    s.callout(PR, [('The term "enzyme" was first of all used by a German physiologist Winhelm Kuhne in 1878. Enzymes kick start biochemical reactions', 'لفظ ”انزائم“ سب سے پہلے 1878ء میں جرمن ماہرِ فعلیات وِلہیلم کوہنے نے استعمال کیا۔ انزائمز حیاتیاتی کیمیائی تعاملات کا آغاز کرتے ہیں', 'د ”انزایم“ اصطلاح لومړی ځل په 1878 کې آلماني فزیولوژیست ویلهلم کوهنه وکاروله. انزایمونه بیوکیمیاوي تعاملونه پیلوي')])
    out.append(s)

    s = Section('bio6_2', '6.2', 'Enzymes lower the Activation Energy', 'انزائمز ایکٹیویشن انرجی کم کرتے ہیں', 'انزایمونه د فعالولو انرژي کموي', [121])
    s.p('Whenever a chemical reaction takes place some amount of energy is spent to break the chemical bonds in reactants (substrates). This energy is called activation energy. Enzymes lower off the amount of activation energy. Thus, in the presence of enzymes, reactions proceed at a faster rate. Enzymes act in many ways to lower the activation energy. For example; they change the shape of substrate molecules or bring them in correct orientation. They may also disrupt the charge distribution on substrate molecules.',
        'جب بھی کوئی کیمیائی تعامل ہوتا ہے تو متعاملات (سبسٹریٹس) کے کیمیائی بندھن توڑنے کے لیے کچھ توانائی خرچ ہوتی ہے۔ اس توانائی کو ایکٹیویشن انرجی کہتے ہیں۔ انزائمز ایکٹیویشن انرجی کی مقدار کم کر دیتے ہیں۔ اس طرح انزائمز کی موجودگی میں تعاملات تیز رفتار سے ہوتے ہیں۔ انزائمز ایکٹیویشن انرجی کم کرنے کے لیے کئی طریقوں سے کام کرتے ہیں۔ مثال کے طور پر یہ سبسٹریٹ مالیکیولز کی شکل بدلتے ہیں یا انہیں درست سمت میں لاتے ہیں۔ یہ سبسٹریٹ مالیکیولز پر چارج کی تقسیم کو بھی متاثر کر سکتے ہیں۔',
        'هرکله چې کیمیاوي تعامل کېږي، د متعاملو (سبسټریټونو) د کیمیاوي اړیکو د ماتولو لپاره یو څه انرژي لګېږي. دې انرژۍ ته د فعالولو انرژي ویل کېږي. انزایمونه د فعالولو د انرژۍ اندازه کموي. په دې ډول د انزایمونو په شتون کې تعاملونه په چټکۍ کېږي. انزایمونه د فعالولو د انرژۍ د کمولو لپاره په ډېرو لارو عمل کوي. د بېلګې په توګه د سبسټریټ مالیکولونو بڼه بدلوي یا یې سم لوري ته راولي. دوی ښايي پر سبسټریټ مالیکولونو د چارج وېش هم ګډوډ کړي.')
    s.callout(PR, [('Complex apparatus and high temperatures are required to break down carbohydrates, fats or proteins in the laboratory. However, with the help of enzymes, cells can carry out these reactions quite rapidly within normal body temperature.', 'لیبارٹری میں کاربوہائیڈریٹس، چکنائی یا پروٹینز کو توڑنے کے لیے پیچیدہ آلات اور زیادہ درجۂ حرارت درکار ہوتا ہے۔ تاہم انزائمز کی مدد سے خلیے یہ تعاملات جسم کے عام درجۂ حرارت پر کافی تیزی سے کر سکتے ہیں۔', 'په لابراتوار کې د کاربوهایډریټونو، غوړو یا پروټینونو د ماتولو لپاره پېچلي وسایل او لوړې تودوخې ته اړتیا ده. خو د انزایمونو په مرسته حجرې دا تعاملونه د بدن په عادي تودوخه کې ډېر ژر ترسره کولای شي.')])
    s.fig('bio6-fig6-1', *three(activation_fig, AE_EN, AE_UR, AE_PS), .7, caption=('Figure 6.1: Activation energy', 'شکل 6.1: ایکٹیویشن انرجی', 'شکل 6.1: د فعالولو انرژي'))
    out.append(s)

    s = Section('bio6_3', '6.3', 'Characteristics of Enzymes', 'انزائمز کی خصوصیات', 'د انزایمونو ځانګړتیاوې', [121, 122, 123])
    s.lines([('i) Enzymes are proteins in nature and are secreted by cells.', 'i) انزائمز فطرتاً پروٹین ہیں اور خلیے انہیں خارج کرتے ہیں۔', 'i) انزایمونه په طبیعت کې پروټینونه دي او حجرې یې افرازوي.'),
             ('ii) Enzymes function as catalysts and increase the rate of chemical reactions. They do so by lowering the activation energy.', 'ii) انزائمز عمل انگیز کے طور پر کام کرتے ہیں اور کیمیائی تعاملات کی شرح بڑھاتے ہیں۔ یہ ایسا ایکٹیویشن انرجی کم کر کے کرتے ہیں۔', 'ii) انزایمونه د کتلست په توګه کار کوي او د کیمیاوي تعاملونو کچه زیاتوي. دا کار د فعالولو انرژۍ په کمولو کوي.'),
             ('iii) Enzymes are specific in action. They are specific not only for substrate but also for the kind of reaction.', 'iii) انزائمز عمل میں مخصوص ہیں۔ یہ نہ صرف سبسٹریٹ بلکہ تعامل کی قسم کے لیے بھی مخصوص ہیں۔', 'iii) انزایمونه په عمل کې ځانګړي دي. نه یوازې د سبسټریټ بلکې د تعامل د ډول لپاره هم ځانګړي دي.'),
             ('iv) A small amount of an enzyme is needed to catalyze relatively large quantities of substrate. They are not used during the chemical reactions.', 'iv) نسبتاً زیادہ سبسٹریٹ کے عمل انگیز کے لیے انزائم کی تھوڑی مقدار درکار ہوتی ہے۔ یہ کیمیائی تعاملات کے دوران استعمال نہیں ہوتے۔', 'iv) د نسبتاً ډېر سبسټریټ لپاره د انزایم لږ مقدار ته اړتیا ده. دوی د کیمیاوي تعاملونو پر مهال نه مصرفېږي.')])
    s.callout(PR, [('Enzymes are also classified according to the chemical reactions they catalyse. For example; the enzymes which catalyse hydrolysis (reactions in which water molecules are needed to break down complex molecule) are known as hydrolases.', 'انزائمز کو ان کیمیائی تعاملات کے لحاظ سے بھی درجہ بند کیا جاتا ہے جنہیں یہ عمل انگیز کرتے ہیں۔ مثال کے طور پر ہائیڈرولائسس (وہ تعاملات جن میں پیچیدہ مالیکیول توڑنے کے لیے پانی کے مالیکیول درکار ہوں) کو عمل انگیز کرنے والے انزائمز ہائیڈرولیزز کہلاتے ہیں۔', 'انزایمونه د هغو کیمیاوي تعاملونو له مخې هم ډلبندي کېږي چې دوی یې کتلست کوي. د بېلګې په توګه هغه انزایمونه چې هایډرولیزس (هغه تعاملونه چې د پېچلي مالیکول د ماتولو لپاره د اوبو مالیکولونو ته اړتیا وي) کتلست کوي هایډرولېزونه بلل کېږي.')])
    s.p("v) All enzymes are synthesized inside the cells. Some enzymes work inside the cells and are called 'Intracellular enzymes' e.g. mitochondrial enzymes. Some enzymes are released from the cell and they work outside. Such enzymes are called extracellular enzymes e.g. pepsin enzyme working in the stomach cavity.",
        'v) تمام انزائمز خلیوں کے اندر بنتے ہیں۔ بعض انزائمز خلیوں کے اندر کام کرتے ہیں اور ’اندرونی خلوی انزائمز‘ کہلاتے ہیں مثلاً مائٹوکونڈریا کے انزائمز۔ بعض انزائمز خلیے سے خارج ہو کر باہر کام کرتے ہیں۔ ایسے انزائمز بیرونی خلوی انزائمز کہلاتے ہیں مثلاً معدے کی گہا میں کام کرنے والا پیپسن انزائم۔',
        'v) ټول انزایمونه د حجرو دننه جوړېږي. ځینې انزایمونه د حجرو دننه کار کوي او ’داخل حجروي انزایمونه‘ بلل کېږي لکه د مایټوکونډریا انزایمونه. ځینې انزایمونه له حجرې خوشې کېږي او بهر کار کوي. داسې انزایمونو ته بهر حجروي انزایمونه ویل کېږي لکه پیپسین انزایم چې د معدې په تشه کې کار کوي.')
    s.callout(SI, [('Enzymes inhibitors are molecules that interact with enzyme to prevent it from working. Poisons and drugs are the examples of enzyme inhibitors.', 'انزائم انہیبیٹرز وہ مالیکیول ہیں جو انزائم سے تعامل کر کے اسے کام کرنے سے روکتے ہیں۔ زہر اور ادویات انزائم انہیبیٹرز کی مثالیں ہیں۔', 'د انزایم مخنیوونکي هغه مالیکولونه دي چې له انزایم سره تعامل کوي او د کار مخه یې نیسي. زهرونه او درمل د انزایم مخنیوونکو بېلګې دي.')])
    s.lines([('vi) In complex metabolic reactions, many enzymes work together in a sequence. One enzyme takes the product of another enzyme as a substrate. After speeding up the reaction, the new product is passed on to another enzyme.', 'vi) پیچیدہ میٹابولک تعاملات میں بہت سے انزائمز ترتیب سے مل کر کام کرتے ہیں۔ ایک انزائم دوسرے انزائم کی پیداوار کو سبسٹریٹ کے طور پر لیتا ہے۔ تعامل تیز کرنے کے بعد نئی پیداوار دوسرے انزائم کو منتقل کر دی جاتی ہے۔', 'vi) په پېچلو میټابولیکي تعاملونو کې ډېر انزایمونه په ترتیب سره یوځای کار کوي. یو انزایم د بل انزایم محصول د سبسټریټ په توګه اخلي. د تعامل له چټکولو وروسته نوی محصول بل انزایم ته سپارل کېږي.'),
             ('vii) Some enzymes require non-protein molecules called cofactors for their action. The main types of cofactors are prosthetic groups, coenzymes and activators:', 'vii) بعض انزائمز کو اپنے عمل کے لیے غیر پروٹینی مالیکیول درکار ہوتے ہیں جنہیں کو فیکٹرز کہتے ہیں۔ کو فیکٹرز کی اہم اقسام پروستھیٹک گروپس، کو انزائمز اور ایکٹیویٹرز ہیں:', 'vii) ځینې انزایمونه د خپل عمل لپاره غیر پروټیني مالیکولونو ته اړتیا لري چې کوفکټورونه بلل کېږي. د کوفکټورونو اصلي ډولونه پروسټیټیک ګروپونه، کو انزایمونه او فعالوونکي دي:')])
    s.fig('bio6-fig6-2', *three(cofactor_fig, CF_EN, CF_UR, CF_PS), .65, caption=('Figure 6.2: Cofactors of enzymes', 'شکل 6.2: انزائمز کے کو فیکٹرز', 'شکل 6.2: د انزایمونو کوفکټورونه'))
    s.lines([('a) Prosthetic groups can be organic the organic molecules which make permanent attachment with the enzyme.', 'a) پروستھیٹک گروپس نامیاتی مالیکیول ہو سکتے ہیں جو انزائم سے مستقل طور پر جڑتے ہیں۔', 'a) پروسټیټیک ګروپونه عضوي مالیکولونه کېدای شي چې له انزایم سره دایمي نښلي.'),
             ('b) Coenzymes are the organic molecules, which are not permanently attached to the enzyme. Most coenzymes are derived from vitamins.', 'b) کو انزائمز وہ نامیاتی مالیکیول ہیں جو انزائم سے مستقل طور پر نہیں جڑے ہوتے۔ زیادہ تر کو انزائمز وٹامنز سے حاصل ہوتے ہیں۔', 'b) کو انزایمونه هغه عضوي مالیکولونه دي چې له انزایم سره دایمي نه دي نښتي. ډېری کو انزایمونه له ویټامینونو اخیستل کېږي.'),
             ('(c) Activators: It is another type of cofactors. These are metal ions (e.g. zinc, copper, or iron) which form temporary attachment with the enzyme.', '(c) ایکٹیویٹرز: یہ کو فیکٹرز کی ایک اور قسم ہے۔ یہ دھاتی آئنز (مثلاً زنک، تانبا یا لوہا) ہیں جو انزائم سے عارضی طور پر جڑتے ہیں۔', '(c) فعالوونکي: دا د کوفکټورونو بل ډول دی. دا فلزي ایونونه (لکه جست، مس یا اوسپنه) دي چې له انزایم سره لنډمهاله نښلي.')])
    s.p('SpaceBook note: item (a) is printed "can be organic the organic molecules" and the figure label is printed "Ezyme"; both kept as printed.', 'اسپیس بک نوٹ: (a) میں ”can be organic the organic molecules“ اور شکل میں ”Ezyme“ چھپا ہے؛ دونوں اسی طرح رکھے گئے ہیں۔', 'د سپېس بوک یادونه: په (a) کې ”can be organic the organic molecules“ او په شکل کې ”Ezyme“ چاپ شوي؛ دواړه لکه چې دي ساتل شوي.', editorial=True)
    s.callout(SI, [('Strawberries, blueberries and blackberries are a good source of manganese. This mineral is an enzyme activator in the body that aids in the synthesis of biotin, thiamine, vitamin C and choline. It also helps in the metabolism of carbohydrates and protein.', 'اسٹرابیری، بلیو بیری اور بلیک بیری مینگنیز کا اچھا ذریعہ ہیں۔ یہ معدن جسم میں انزائم ایکٹیویٹر ہے جو بایوٹن، تھایامین، وٹامن سی اور کولین کی تالیف میں مدد دیتا ہے۔ یہ کاربوہائیڈریٹس اور پروٹین کے میٹابولزم میں بھی مدد کرتا ہے۔', 'سټرابري، بلو بیري او بلیک بیري د منګنیز ښه سرچینه ده. دا معدن په بدن کې د انزایم فعالوونکی دی چې د بایوټین، تیامین، ویټامین C او کولین په جوړولو کې مرسته کوي. د کاربوهایډریټونو او پروټین په میټابولیزم کې هم مرسته کوي.')])
    s.h('Specificity of Enzyme', 'انزائم کی خصوصیت', 'د انزایم ځانګړتیا')
    s.p('We have studied that enzymes are specific for their substrate and the type of reaction. For example, the enzyme protease speed up the digestion of protein only. It does not catalyse the digestion of starch. Enzyme amylase works for the digestion of starch only. Similarly, enzyme cellulase speed up the digestion of cellulose only. Similarly, lipase digests lipids only. The specificity of different enzymes is due to the shape of their active sites. The active sites of each enzyme possess specific shape that fits with specific substrate.',
        'ہم پڑھ چکے ہیں کہ انزائمز اپنے سبسٹریٹ اور تعامل کی قسم کے لیے مخصوص ہیں۔ مثال کے طور پر انزائم پروٹیز صرف پروٹین کے ہضم کو تیز کرتا ہے۔ یہ نشاستے کے ہضم کو عمل انگیز نہیں کرتا۔ انزائم ایمائلیز صرف نشاستے کے ہضم کے لیے کام کرتا ہے۔ اسی طرح انزائم سیلولیز صرف سیلولوز کے ہضم کو تیز کرتا ہے۔ اسی طرح لائپیز صرف لپڈز کو ہضم کرتا ہے۔ مختلف انزائمز کی خصوصیت ان کی ایکٹیو سائٹس کی شکل کی وجہ سے ہے۔ ہر انزائم کی ایکٹیو سائٹ کی ایک مخصوص شکل ہوتی ہے جو مخصوص سبسٹریٹ سے مطابقت رکھتی ہے۔',
        'موږ لوستي دي چې انزایمونه د خپل سبسټریټ او د تعامل د ډول لپاره ځانګړي دي. د بېلګې په توګه پروټیاز انزایم یوازې د پروټین هضم چټکوي. د نشایستې هضم نه کتلست کوي. امیلاز انزایم یوازې د نشایستې د هضم لپاره کار کوي. همدارنګه سیلولاز انزایم یوازې د سلولوز هضم چټکوي. همدارنګه لایپاز یوازې لیپیډونه هضموي. د بېلابېلو انزایمونو ځانګړتیا د هغوی د فعالو ځایونو د بڼې له امله ده. د هر انزایم فعال ځای ځانګړې بڼه لري چې له ځانګړي سبسټریټ سره سمون خوري.')
    s.fig('bio6-fig6-3', *three(specificity_fig, SP_EN, SP_UR, SP_PS), .55, caption=('Figure 5.3: shape of active site of enzyme and its specificity', 'شکل 5.3 (جیسا چھپا ہے): انزائم کی ایکٹیو سائٹ کی شکل اور اس کی خصوصیت', 'شکل 5.3 (لکه چې چاپ شوې): د انزایم د فعال ځای بڼه او ځانګړتیا یې'))
    s.p('SpaceBook note: this caption is printed as "Figure 5.3" inside Unit 6 (between Figures 6.2 and 6.4); the printed number is kept.', 'اسپیس بک نوٹ: یہ عنوان یونٹ 6 میں (شکل 6.2 اور 6.4 کے درمیان) ”شکل 5.3“ چھپا ہے؛ چھپا ہوا نمبر رکھا گیا ہے۔', 'د سپېس بوک یادونه: دا سرلیک په یونټ 6 کې (د شکل 6.2 او 6.4 ترمنځ) ”شکل 5.3“ چاپ شوی؛ چاپ شوې شمېره ساتل شوې.', editorial=True)
    out.append(s)

    s = Section('bio6_4', '6.4', 'Mechanism of Enzyme Action', 'انزائم کے عمل کا طریقۂ کار', 'د انزایم د عمل میکانیزم', [124, 125])
    s.p('There is a small portion in the enzyme molecule that is actually involved in catalysis. It is in the form of a depression or "pocket" on the surface of enzyme molecule. This catalytic region is called active site.',
        'انزائم مالیکیول کا ایک چھوٹا حصہ دراصل عمل انگیزی میں شامل ہوتا ہے۔ یہ انزائم مالیکیول کی سطح پر ایک گڑھے یا ”جیب“ کی شکل میں ہوتا ہے۔ اس عمل انگیز حصے کو ایکٹیو سائٹ کہتے ہیں۔',
        'د انزایم په مالیکول کې یوه کوچنۍ برخه په اصل کې په کتلیز کې ونډه لري. دا د انزایم مالیکول پر سطحه د ژوروالي یا ”جېب“ په بڼه ده. دې کتلیزي برخې ته فعال ځای ویل کېږي.')
    s.p('When an enzyme attaches with the substrate, a temporary enzyme-substrate (ES) complex is formed. The active site catalyzes the reaction and substrate is converted to product. The ES complex breaks and the enzyme and the product are released.',
        'جب انزائم سبسٹریٹ سے جڑتا ہے تو ایک عارضی انزائم سبسٹریٹ (ES) کمپلیکس بنتا ہے۔ ایکٹیو سائٹ تعامل کو عمل انگیز کرتی ہے اور سبسٹریٹ حاصل میں بدل جاتا ہے۔ ES کمپلیکس ٹوٹ جاتا ہے اور انزائم اور حاصل آزاد ہو جاتے ہیں۔',
        'کله چې انزایم له سبسټریټ سره نښلي، لنډمهاله انزایم-سبسټریټ (ES) کمپلېکس جوړېږي. فعال ځای تعامل کتلست کوي او سبسټریټ په محصول بدلېږي. ES کمپلېکس ماتېږي او انزایم او محصول خوشې کېږي.')
    s.lines([('Enzyme (active site) + Substrate → Enzyme-Substrate (Complex) → Enzyme + Products', 'انزائم (ایکٹیو سائٹ) + سبسٹریٹ ← انزائم سبسٹریٹ (کمپلیکس) ← انزائم + حاصلات', 'انزایم (فعال ځای) + سبسټریټ ← انزایم-سبسټریټ (کمپلېکس) ← انزایم + محصولات')])
    s.p('Two models have been proposed to explain the mechanism of enzyme action. These are the "lock and key model" and the "Induced fit model"', 'انزائم کے عمل کے طریقۂ کار کی وضاحت کے لیے دو ماڈل پیش کیے گئے ہیں۔ یہ ”لاک اینڈ کی ماڈل“ اور ”انڈیوسڈ فٹ ماڈل“ ہیں', 'د انزایم د عمل د میکانیزم د تشریح لپاره دوه ماډلونه وړاندې شوي. دا ”قلف او کیلي ماډل“ او ”هڅول شوی سمون ماډل“ دي')
    s.h('Lock and Key Model', 'لاک اینڈ کی ماڈل (تالا اور چابی ماڈل)', 'قلف او کیلي ماډل')
    s.p('This model was proposed by a German chemist Emil Fischer in 1894. According to this model, the active site of enzyme and the substrate have specific geometric shapes. The substrate molecule exactly fits in the active site of enzyme just like a lock and a key (enzyme is the lock and substrate is the key). This model suggests that the active site is a rigid and non-flexible structure.',
        'یہ ماڈل 1894ء میں جرمن کیمیا دان ایمل فشر نے پیش کیا۔ اس ماڈل کے مطابق انزائم کی ایکٹیو سائٹ اور سبسٹریٹ کی مخصوص جیومیٹریکل شکلیں ہوتی ہیں۔ سبسٹریٹ مالیکیول انزائم کی ایکٹیو سائٹ میں بالکل تالے اور چابی کی طرح فٹ ہوتا ہے (انزائم تالا اور سبسٹریٹ چابی ہے)۔ یہ ماڈل ظاہر کرتا ہے کہ ایکٹیو سائٹ ایک سخت اور غیر لچکدار ساخت ہے۔',
        'دا ماډل په 1894 کې آلماني کیمیاپوه ایمیل فیشر وړاندې کړ. د دې ماډل له مخې د انزایم فعال ځای او سبسټریټ ځانګړې هندسي بڼې لري. د سبسټریټ مالیکول د انزایم په فعال ځای کې لکه قلف او کیلي سم ځای پر ځای کېږي (انزایم قلف او سبسټریټ کیلي ده). دا ماډل وايي چې فعال ځای کلک او نه انعطاف منونکی جوړښت دی.')
    s.fig('bio6-fig6-4', model_fig(LK_EN), model_fig(LK_UR), model_fig(LK_PS), .7, caption=('Figure 6.4: Lock and Key Model of enzyme action', 'شکل 6.4: انزائم کے عمل کا لاک اینڈ کی ماڈل', 'شکل 6.4: د انزایم د عمل د قلف او کیلي ماډل'))
    s.callout(STS, [('There is a famous expression, "without which there is none" and this expression is very much true for the role of enzymes inside our body. Digestion could not be done without enzymes. We have foods that contain enzymes for their own digestion and we should prefer such foods. These food containing enzymes lower the burden of digestion on our digestive system.', 'ایک مشہور قول ہے ”جس کے بغیر کچھ نہیں“ اور یہ قول ہمارے جسم میں انزائمز کے کردار کے لیے بالکل درست ہے۔ انزائمز کے بغیر ہضم نہیں ہو سکتا۔ ہمارے پاس ایسی غذائیں ہیں جن میں ان کے اپنے ہضم کے لیے انزائمز ہوتے ہیں اور ہمیں ایسی غذاؤں کو ترجیح دینی چاہیے۔ انزائمز والی یہ غذائیں ہمارے نظامِ انہضام پر ہضم کا بوجھ کم کرتی ہیں۔', 'یوه مشهوره وینا ده ”چې بې له هغه هېڅ نشته“ او دا وینا زموږ په بدن کې د انزایمونو د رول لپاره ډېره سمه ده. بې له انزایمونو هضم نه شي کېدای. موږ داسې خواړه لرو چې د خپل هضم لپاره انزایمونه لري او باید داسې خواړه غوره کړو. دا انزایم لرونکي خواړه زموږ د هضم پر سیسټم د هضم بار کموي.')])
    s.h('Induced Fit Model:', 'انڈیوسڈ فٹ ماڈل:', 'هڅول شوی سمون ماډل:')
    s.p('Recent studies do not support lock and key model. On the basis of new evidences, in 1958 an American biologist Daniel Koshland proposed "Induced Fit Model". According to this model, when a substrate molecule fits in the active site of enzyme, the enzyme molecule alters the shape of active site slightly so that it fits more tightly around the substrate molecule (induced fit)',
        'حالیہ مطالعات لاک اینڈ کی ماڈل کی تائید نہیں کرتے۔ نئے شواہد کی بنیاد پر 1958ء میں امریکی ماہرِ حیاتیات ڈینیئل کوشلینڈ نے ”انڈیوسڈ فٹ ماڈل“ پیش کیا۔ اس ماڈل کے مطابق جب سبسٹریٹ مالیکیول انزائم کی ایکٹیو سائٹ میں فٹ ہوتا ہے تو انزائم مالیکیول ایکٹیو سائٹ کی شکل کو تھوڑا سا بدل دیتا ہے تاکہ یہ سبسٹریٹ مالیکیول کے گرد زیادہ مضبوطی سے فٹ ہو (انڈیوسڈ فٹ)',
        'وروستۍ څېړنې د قلف او کیلي ماډل ملاتړ نه کوي. د نویو شواهدو پر بنسټ په 1958 کې امریکایي بیولوژیست ډینیل کوشلنډ ”هڅول شوی سمون ماډل“ وړاندې کړ. د دې ماډل له مخې کله چې د سبسټریټ مالیکول د انزایم په فعال ځای کې ځای پر ځای شي، د انزایم مالیکول د فعال ځای بڼه لږ بدلوي ترڅو د سبسټریټ مالیکول شاوخوا ټینګ سمون وخوري (هڅول شوی سمون)')
    s.fig('bio6-fig6-5', model_fig(IF_EN, True), model_fig(IF_UR, True), model_fig(IF_PS, True), .7, caption=('Figure 6.5: Induced Fit Model of enzyme action', 'شکل 6.5: انزائم کے عمل کا انڈیوسڈ فٹ ماڈل', 'شکل 6.5: د انزایم د عمل هڅول شوی سمون ماډل'))
    s.callout(('Activity 6.1', 'سرگرمی 6.1', 'فعالیت 6.1'), [('Build or design model of an enzyme to demonstrate the working of an enzyme.', 'انزائم کے کام کو دکھانے کے لیے انزائم کا ماڈل بنائیں یا ڈیزائن کریں۔', 'د انزایم د کار د ښودلو لپاره د انزایم ماډل جوړ یا ډیزاین کړئ.')])
    out.append(s)

    s = Section('bio6_5', '6.5', 'Factors that affect the rate of enzyme action', 'انزائم کے عمل کی شرح پر اثر انداز ہونے والے عوامل', 'د انزایم د عمل پر کچه اغېزمن عوامل', [125, 126, 127])
    s.p('There are different factors which affect the enzyme activity. Some of them are discussed as follow.', 'انزائم کی سرگرمی پر مختلف عوامل اثر انداز ہوتے ہیں۔ ان میں سے کچھ پر ذیل میں بحث کی گئی ہے۔', 'بېلابېل عوامل د انزایم پر فعالیت اغېز کوي. ځینې یې لاندې بیانېږي.')
    s.h('a. Effect of Temperature on Enzyme Activity', 'a. انزائم کی سرگرمی پر درجۂ حرارت کا اثر', 'a. د انزایم پر فعالیت د تودوخې اغېز')
    s.p('Increase in temperature, speeds up the rate of enzyme catalyzed reactions but only to a point. Each enzyme works at the maximum rate at a specific temperature, which is called its optimum temperature. The optimum temperature of enzymes varies in different organisms. For most enzymes, the optimum temperature is about 40 - 45°C. Certain enzymes in plants have a high optimum temperature. Decrease in temperature lowers the rate of reaction.',
        'درجۂ حرارت میں اضافہ انزائم کے عمل انگیز تعاملات کی شرح تیز کرتا ہے لیکن صرف ایک حد تک۔ ہر انزائم ایک مخصوص درجۂ حرارت پر زیادہ سے زیادہ شرح سے کام کرتا ہے جسے اس کا موزوں ترین (آپٹیمم) درجۂ حرارت کہتے ہیں۔ انزائمز کا موزوں ترین درجۂ حرارت مختلف جانداروں میں مختلف ہوتا ہے۔ زیادہ تر انزائمز کے لیے موزوں ترین درجۂ حرارت تقریباً 40 - 45°C ہے۔ پودوں کے بعض انزائمز کا موزوں ترین درجۂ حرارت زیادہ ہوتا ہے۔ درجۂ حرارت میں کمی تعامل کی شرح کم کر دیتی ہے۔',
        'د تودوخې زیاتوالی د انزایمي تعاملونو کچه چټکوي خو یوازې تر یوه حده. هر انزایم په یوه ځانګړې تودوخه کې په اعظمي کچه کار کوي چې غوره (اپټیمم) تودوخه یې بلل کېږي. د انزایمونو غوره تودوخه په بېلابېلو موجوداتو کې توپیر لري. د ډېری انزایمونو لپاره غوره تودوخه شاوخوا 40 - 45°C ده. د بوټو ځینې انزایمونه لوړه غوره تودوخه لري. د تودوخې کمښت د تعامل کچه کموي.')
    s.p('When temperature rises above the optimum temperature, the rate of reaction decreases rapidly. This is due to the denaturation (alteration in the structure) of the protein of enzyme. The average temperature of human body is 37°C. It is the optimum temperature for human enzymes. Human enzymes start to denature quickly at temperatures above 40°C.',
        'جب درجۂ حرارت موزوں ترین درجۂ حرارت سے بڑھ جائے تو تعامل کی شرح تیزی سے کم ہو جاتی ہے۔ یہ انزائم کی پروٹین کے ڈی نیچریشن (ساخت میں تبدیلی) کی وجہ سے ہے۔ انسانی جسم کا اوسط درجۂ حرارت 37°C ہے۔ یہ انسانی انزائمز کا موزوں ترین درجۂ حرارت ہے۔ انسانی انزائمز 40°C سے زیادہ درجۂ حرارت پر تیزی سے ڈی نیچر ہونے لگتے ہیں۔',
        'کله چې تودوخه له غوره تودوخې لوړه شي، د تعامل کچه ژر کمېږي. دا د انزایم د پروټین د ډي نیچر کېدو (په جوړښت کې بدلون) له امله ده. د انسان د بدن منځنۍ تودوخه 37°C ده. دا د انساني انزایمونو غوره تودوخه ده. انساني انزایمونه له 40°C لوړې تودوخې کې ژر ډي نیچر کېږي.')
    s.fig('bio6-fig6-6', *three(temp_graph, TG_EN, TG_UR, TG_PS), .7, caption=('Figure 6.6: Effect of temperature on enzyme activity', 'شکل 6.6: انزائم کی سرگرمی پر درجۂ حرارت کا اثر', 'شکل 6.6: د انزایم پر فعالیت د تودوخې اغېز'))
    s.callout(('Points to Ponder:', 'غور طلب نکات:', 'د فکر وړ ټکي:'), [('• Why does enzyme activity increase as temperature rises?', '• درجۂ حرارت بڑھنے کے ساتھ انزائم کی سرگرمی کیوں بڑھتی ہے؟', '• ولې د تودوخې په لوړېدو د انزایم فعالیت زیاتېږي؟'),
                                                                   ('• Why does enzyme activity decrease at high temperature?', '• زیادہ درجۂ حرارت پر انزائم کی سرگرمی کیوں کم ہو جاتی ہے؟', '• ولې په لوړه تودوخه د انزایم فعالیت کمېږي؟')])
    s.h('b. Effect of pH on Enzyme Activity', 'b. انزائم کی سرگرمی پر pH کا اثر', 'b. د انزایم پر فعالیت د pH اغېز')
    s.p('Enzymes are affected by the acidity or alkalinity of the solutions in which they act. Each enzymes works best at a specific pH, which is called its optimum pH. Some work best in slightly acidic pH while others require slightly alkaline pH. Most enzymes function between a pH of 6 – 8, however pepsin in the stomach works best at a pH of 2 and trypsin at a pH of 8.',
        'انزائمز ان محلولوں کی تیزابیت یا القلیت سے متاثر ہوتے ہیں جن میں وہ کام کرتے ہیں۔ ہر انزائم ایک مخصوص pH پر بہترین کام کرتا ہے جسے اس کا موزوں ترین pH کہتے ہیں۔ بعض ہلکے تیزابی pH میں بہتر کام کرتے ہیں جبکہ دوسروں کو ہلکا القلی pH درکار ہوتا ہے۔ زیادہ تر انزائمز 6 – 8 کے pH پر کام کرتے ہیں، تاہم معدے میں پیپسن pH 2 پر اور ٹرپسن pH 8 پر بہترین کام کرتا ہے۔',
        'انزایمونه د هغو محلولونو له تیزابیت یا القلیت اغېزمنېږي چې پکې کار کوي. هر انزایم په یوه ځانګړي pH کې غوره کار کوي چې غوره pH یې بلل کېږي. ځینې په لږ تیزابي pH کې ښه کار کوي او نور لږ القلي pH ته اړتیا لري. ډېری انزایمونه د 6 – 8 pH ترمنځ کار کوي، خو په معده کې پیپسین په pH 2 او ټرپسین په pH 8 کې غوره کار کوي.')
    s.p('Any change in pH can lower the enzymatic activity. Extreme changes in the pH of solutions denature the enzymes.', 'pH میں کوئی بھی تبدیلی انزائم کی سرگرمی کم کر سکتی ہے۔ محلولوں کے pH میں شدید تبدیلیاں انزائمز کو ڈی نیچر کر دیتی ہیں۔', 'په pH کې هر بدلون ښايي انزایمي فعالیت کم کړي. د محلولونو په pH کې سخت بدلونونه انزایمونه ډي نیچر کوي.')
    s.fig('bio6-fig6-7', *three(ph_graph, PG_EN, PG_UR, PG_PS), .45, caption=('Figure 6.7: The effect of pH on enzyme activity', 'شکل 6.7: انزائم کی سرگرمی پر pH کا اثر', 'شکل 6.7: د انزایم پر فعالیت د pH اغېز'))
    s.h('c. Effect of Concentration of Substrate on Enzyme Activity', 'c. انزائم کی سرگرمی پر سبسٹریٹ کے ارتکاز کا اثر', 'c. د انزایم پر فعالیت د سبسټریټ د غلظت اغېز')
    s.p('As the concentration of substrate increases, the rate of reaction increases. This is due to successful collisions with enzyme molecules. However, if the substrate concentration is increased beyond a saturation point, the active sites of enzyme are not available and rate of reaction does not increase more.',
        'جیسے جیسے سبسٹریٹ کا ارتکاز بڑھتا ہے، تعامل کی شرح بڑھتی ہے۔ یہ انزائم مالیکیولز کے ساتھ کامیاب ٹکراؤ کی وجہ سے ہے۔ تاہم اگر سبسٹریٹ کا ارتکاز سیچوریشن پوائنٹ سے بڑھا دیا جائے تو انزائم کی ایکٹیو سائٹس دستیاب نہیں رہتیں اور تعامل کی شرح مزید نہیں بڑھتی۔',
        'لکه څنګه چې د سبسټریټ غلظت زیاتېږي، د تعامل کچه زیاتېږي. دا له انزایم مالیکولونو سره د بریالیو ټکرونو له امله ده. خو که د سبسټریټ غلظت له مړښت ټکي زیات شي، د انزایم فعال ځایونه نه وي موجود او د تعامل کچه نوره نه زیاتېږي.')
    s.fig('bio6-fig6-8', *three(substrate_graph, SG_EN, SG_UR, SG_PS), .55, caption=('Figure 6.8: The effect of substrate concentration on enzyme activity', 'شکل 6.8: انزائم کی سرگرمی پر سبسٹریٹ کے ارتکاز کا اثر', 'شکل 6.8: د انزایم پر فعالیت د سبسټریټ د غلظت اغېز'))
    s.callout(('Analyzing and Interpreting', 'تجزیہ اور توضیح', 'شننه او تفسیر'), [('• Draw graphs showing the effects of temperature, pH and concentration of substrate on the rate of enzyme catalyzed reactions.', '• انزائم کے عمل انگیز تعاملات کی شرح پر درجۂ حرارت، pH اور سبسٹریٹ کے ارتکاز کے اثرات دکھانے والے گراف بنائیں۔', '• د انزایمي تعاملونو پر کچه د تودوخې، pH او د سبسټریټ د غلظت اغېزې ښودونکي ګرافونه رسم کړئ.'),
                                                                                     ('• Illustrate through a diagram, the lowering of activation energy by enzyme.', '• ایک شکل کے ذریعے انزائم سے ایکٹیویشن انرجی کی کمی کو واضح کریں۔', '• د یوه انځور له لارې د انزایم په واسطه د فعالولو انرژۍ کمېدل وښیئ.')])
    s.callout(('Activities 6.2', 'سرگرمیاں 6.2', 'فعالیتونه 6.2'), [('• Perform an experiment to show the working of enzyme in vitro (out of body or in a test tube) e.g., pepsin working on meat in a test tube.', '• ان وٹرو (جسم سے باہر یا ٹیسٹ ٹیوب میں) انزائم کا کام دکھانے کے لیے تجربہ کریں مثلاً ٹیسٹ ٹیوب میں گوشت پر پیپسن کا عمل۔', '• د بدن بهر (په ټیسټ ټیوب کې) د انزایم د کار د ښودلو لپاره تجربه وکړئ لکه په ټیسټ ټیوب کې پر غوښه د پیپسین عمل.'),
                                                                   ('• Put diastase in a starch solution in test tube at 37°C and after fifteen minutes perform iodine test for presence of starch.', '• ٹیسٹ ٹیوب میں نشاستے کے محلول میں 37°C پر ڈائیاسٹیز ڈالیں اور پندرہ منٹ بعد نشاستے کی موجودگی کے لیے آیوڈین ٹیسٹ کریں۔', '• په ټیسټ ټیوب کې د نشایستې په محلول کې په 37°C ډیاسټاز واچوئ او له پنځلسو دقیقو وروسته د نشایستې د شتون لپاره د ایوډین ازموینه وکړئ.')])
    out.append(s)

    s = Section('bio6_exfig', 'Exercise figures', 'Exercise diagrams and graphs', 'مشق کی اشکال اور گراف', 'د تمرین انځورونه او ګرافونه', [129, 131])
    s.p('Diagrams and graphs printed with Exercise A (iii) and Exercise C (iv) and (vi).', 'مشق A (iii) اور مشق C (iv) اور (vi) کے ساتھ چھپی ہوئی اشکال اور گراف۔', 'د تمرین A (iii) او تمرین C (iv) او (vi) سره چاپ شوي انځورونه او ګرافونه.')
    e = exercise_figures('Unit 6 exercise diagrams')
    s.fig('bio6-exercise-figs', e, e, e, 1)
    out.append(s)
    return out


KEY_POINTS = [
    ('Enzymes are biological or organic catalysts. They are made of proteins and can speed up the rate of chemical reactions without themselves being chemically changed at the end of the reactions.', 'انزائمز حیاتیاتی یا نامیاتی عمل انگیز ہیں۔ یہ پروٹینز سے بنے ہیں اور تعاملات کے اختتام پر خود کیمیائی طور پر تبدیل ہوئے بغیر کیمیائی تعاملات کی شرح تیز کر سکتے ہیں۔', 'انزایمونه بیولوژیکي یا عضوي کتلستونه دي. له پروټینونو جوړ دي او د کیمیاوي تعاملونو کچه چټکولای شي پرته له دې چې د تعامل په پای کې پخپله کیمیاوي بدلون ومومي.'),
    ('Enzymes are specific in their actions because of the shape of their active sites. Only substances with shapes complementary to that of active site can fit into the enzyme molecules and be acted upon by the enzymes.', 'انزائمز اپنی ایکٹیو سائٹس کی شکل کی وجہ سے اپنے عمل میں مخصوص ہیں۔ صرف وہی مادے جن کی شکل ایکٹیو سائٹ کے مطابق ہو انزائم مالیکیولز میں فٹ ہو سکتے ہیں اور انزائمز ان پر عمل کر سکتے ہیں۔', 'انزایمونه د خپلو فعالو ځایونو د بڼې له امله په عمل کې ځانګړي دي. یوازې هغه مواد چې بڼه یې د فعال ځای سره بشپړوونکې وي د انزایم په مالیکول کې ځای نیسي او انزایم پرې عمل کوي.'),
    ('Factors affecting the rate of enzyme catalyzed reactions are temperature, pH, enzyme concentration and substrate concentration.', 'انزائم کے عمل انگیز تعاملات کی شرح پر اثر انداز ہونے والے عوامل درجۂ حرارت، pH، انزائم کا ارتکاز اور سبسٹریٹ کا ارتکاز ہیں۔', 'د انزایمي تعاملونو پر کچه اغېزمن عوامل تودوخه، pH، د انزایم غلظت او د سبسټریټ غلظت دي.'),
    ('Every enzyme has its optimum temperature and pH. At optimum temperature and pH, an enzyme works at the greatest speed.', 'ہر انزائم کا اپنا موزوں ترین درجۂ حرارت اور pH ہوتا ہے۔ موزوں ترین درجۂ حرارت اور pH پر انزائم سب سے زیادہ رفتار سے کام کرتا ہے۔', 'هر انزایم خپله غوره تودوخه او pH لري. په غوره تودوخه او pH کې انزایم په تر ټولو لوړ سرعت کار کوي.'),
    ('When temperature rises well above the optimum temperature, the protein structure of enzyme is denatured and so the rate of reaction decreases rapidly.', 'جب درجۂ حرارت موزوں ترین سے کافی بڑھ جائے تو انزائم کی پروٹینی ساخت ڈی نیچر ہو جاتی ہے اور اس لیے تعامل کی شرح تیزی سے کم ہو جاتی ہے۔', 'کله چې تودوخه له غوره تودوخې ډېره لوړه شي، د انزایم پروټیني جوړښت ډي نیچر کېږي او نو د تعامل کچه ژر کمېږي.'),
    ('Enzymes are specific in action. They are specific not only for substrate but also for the kind of reaction.', 'انزائمز عمل میں مخصوص ہیں۔ یہ نہ صرف سبسٹریٹ بلکہ تعامل کی قسم کے لیے بھی مخصوص ہیں۔', 'انزایمونه په عمل کې ځانګړي دي. نه یوازې د سبسټریټ بلکې د تعامل د ډول لپاره هم ځانګړي دي.'),
    ('Intracellular enzymes e.g. mitochondrial enzymes work inside the cells while extracellular enzymes e.g. pepsin are released from the cell and they work outside the cell.', 'اندرونی خلوی انزائمز مثلاً مائٹوکونڈریا کے انزائمز خلیوں کے اندر کام کرتے ہیں جبکہ بیرونی خلوی انزائمز مثلاً پیپسن خلیے سے خارج ہو کر خلیے کے باہر کام کرتے ہیں۔', 'داخل حجروي انزایمونه لکه د مایټوکونډریا انزایمونه د حجرو دننه کار کوي په داسې حال کې چې بهر حجروي انزایمونه لکه پیپسین له حجرې خوشې کېږي او بهر کار کوي.'),
    ('Cofactors are the non-protein molecules required by enzymes for their action.', 'کو فیکٹرز وہ غیر پروٹینی مالیکیول ہیں جو انزائمز کو اپنے عمل کے لیے درکار ہوتے ہیں۔', 'کوفکټورونه هغه غیر پروټیني مالیکولونه دي چې انزایمونه یې د خپل عمل لپاره اړتیا لري.'),
    ('The cofactors called prosthetic groups make permanent attachment with the enzyme while the cofactors called coenzymes are not permanently attached to the enzyme.', 'پروستھیٹک گروپس کہلانے والے کو فیکٹرز انزائم سے مستقل طور پر جڑتے ہیں جبکہ کو انزائمز کہلانے والے کو فیکٹرز انزائم سے مستقل طور پر نہیں جڑے ہوتے۔', 'هغه کوفکټورونه چې پروسټیټیک ګروپونه بلل کېږي له انزایم سره دایمي نښلي په داسې حال کې چې کو انزایمونه له انزایم سره دایمي نه نښلي.'),
    ('An enzyme attaches with the substrate to form enzyme-substrate (ES) complex. The active site of enzyme catalyzes the reaction and substrate is converted to product.', 'انزائم سبسٹریٹ سے جڑ کر انزائم سبسٹریٹ (ES) کمپلیکس بناتا ہے۔ انزائم کی ایکٹیو سائٹ تعامل کو عمل انگیز کرتی ہے اور سبسٹریٹ حاصل میں بدل جاتا ہے۔', 'انزایم له سبسټریټ سره نښلي او انزایم-سبسټریټ (ES) کمپلېکس جوړوي. د انزایم فعال ځای تعامل کتلست کوي او سبسټریټ په محصول بدلېږي.'),
    ('The lock and key model of enzyme action states that the substrate molecule exactly fits in the active site of enzyme which is a rigid and non-flexible structure.', 'انزائم کے عمل کا لاک اینڈ کی ماڈل بیان کرتا ہے کہ سبسٹریٹ مالیکیول انزائم کی ایکٹیو سائٹ میں بالکل فٹ ہوتا ہے جو ایک سخت اور غیر لچکدار ساخت ہے۔', 'د انزایم د عمل د قلف او کیلي ماډل وايي چې د سبسټریټ مالیکول د انزایم په فعال ځای کې سم ځای نیسي چې کلک او نه انعطاف منونکی جوړښت دی.'),
    ('The induced fit model suggests that the enzyme molecule alters the shape of active site slightly so that it fits more tightly around the substrate molecule.', 'انڈیوسڈ فٹ ماڈل ظاہر کرتا ہے کہ انزائم مالیکیول ایکٹیو سائٹ کی شکل تھوڑی سی بدلتا ہے تاکہ یہ سبسٹریٹ مالیکیول کے گرد زیادہ مضبوطی سے فٹ ہو۔', 'هڅول شوی سمون ماډل وايي چې د انزایم مالیکول د فعال ځای بڼه لږ بدلوي ترڅو د سبسټریټ مالیکول شاوخوا ټینګ سمون وخوري.'),
]

NOTE = 'SpaceBook answer — the textbook prints no answer key for this exercise.'
MCQS = [
    ('i. The chemicals which are involved as catalysts inside the living bodies are:', ['Carbohydrates', 'Fats', 'Proteins', 'Starch'], 2, NOTE),
    ('ii. Enzymes are biological catalysts which:', ['Allow new chemical reactions to occur.', 'Are used up during chemical reactions.', 'Alter the direction of chemical reactions.', 'Alter the rate of chemical reactions.'], 3, NOTE),
    ('iii. The graph below shows that the rate of an enzyme-catalysed reaction, its rate: (graph in "Exercise diagrams and graphs")', ['Increases when the temperature is increased', 'Decreases when the temperature is increased.', 'Increases with temperature upto a maximum of 40°C.', 'remain unchanged.'], 2, NOTE),
    ('iv. What is TRUE about enzymes?', ['All parts of enzyme molecule take part in reaction', 'Enzymes lower the activation energy of reaction', 'An enzyme can act upon any kind of substrates', 'They are needed in large quantities'], 1, NOTE),
    ('v. What is TRUE about cofactors?', ['Take part in reactions', 'Help enzymes in their activity', 'Increase activation energy', 'Are composed of proteins'], 1, NOTE),
    ('vi. One of the following may function as coenzymes for the enzymes', ['Proteins', 'Carbohydrates', 'Vitamins', 'DNA'], 2, NOTE + ' Most coenzymes are derived from vitamins.'),
    ('vii. Increase or decrease in temperature beyond the optimum temperature will:', ['Increase the rate of reaction', 'Decrease the rate of reaction', 'Not affect the rate of reaction', 'Denature the enzyme'], 1, NOTE + ' Only a rise above the optimum denatures the enzyme; both changes decrease the rate.'),
    ('viii. Trypsin, an enzymes, works at:', ['alkaline pH', 'acidic pH', 'neutral pH', 'pH does not affect its activity'], 0, NOTE + ' Trypsin works best at pH 8.'),
    ('ix. Change in environmental factors will affect enzymes activity and therefore, may affect:', ['Metabolism', 'Respiration', 'Digestion', 'All of them'], 3, NOTE),
    ('x. The body temperature at 104°F is known as critical because it causes:', ['Nerves breakdown', 'Boiling of body water', 'Enzymes stop to work', 'None of them'], 2, NOTE + ' 104°F = 40°C, above which human enzymes start to denature.'),
]
SQ = ['i. Differentiate between lock and key model and the induced-fit model.', 'ii. In what way does an enzyme affect the chemical reaction it catalyses?',
      'iii. What will be the effect on digestion if we take some digestive enzymes from outsides?', 'iv. What is meant by denaturation of enzyme?', 'v. How are enzymes specific for the substrate?',
      'vi. What are the terms used to describe the temperature and the pH at which an enzyme can work most effectively in a reaction?']
LQ = ['i. Describe the factors which affect the enzymes activities.', 'ii. Explain the mode of action of an enzyme in a reaction.', 'iii. Write the various properties of enzymes.',
      'iv. The diagram below shows the relationship between an enzyme, a substrate and the products of an enzyme-catalyzed reaction. a. What is represented by the parts labeled A, B and C in the diagram? b. Name two properties of enzymes that are represented in this diagram. What will happen to the chemical reaction if the enzyme is removed? c. What will happen to the rate of reaction if the reaction temperature is raised steadily: (i). from 25°C to 35°C, and (ii). from 40°C to 60°C? d. What term is used to describe the condition of the enzyme when it is heated to a temperature of 60°C and above?',
      'vi. The graph below shows the rate of an enzymatic reaction. A. According to graph A, at which temperature the enzyme activity is highest. When temperature increases above this point, what will happen to the enzyme? B. According to graph B, what is the optimum pH for (i) pepsin, and (ii) lipase? As pH moves away from the optimum value, what will happen to the enzyme activity?']
LAB = 'SpaceBook-authored answer based on this unit (the textbook prints no answers):\n'
SQ_ANS = ['Lock and key (Fischer, 1894): the active site is rigid and the substrate fits exactly, like a key in a lock. Induced fit (Koshland, 1958): the active site changes its shape slightly when the substrate enters so it fits more tightly.',
          'It speeds up the reaction by lowering the activation energy (changing substrate shape, bringing molecules into correct orientation or disrupting charge distribution), without being used up.',
          'Enzymes taken in foods lower the burden of digestion on our digestive system (Science, Technology and Society box, section 6.4).',
          'Denaturation is an alteration in the structure of the enzyme protein, for example at temperatures above the optimum or extreme pH; the rate of reaction then falls rapidly.',
          'Each enzyme has an active site with a specific shape that fits only a specific substrate, e.g. protease acts on protein only, amylase on starch, lipase on lipids.',
          'Optimum temperature and optimum pH.']
LQ_ANS = ['Temperature: rate rises to the optimum (about 40-45°C for most enzymes; 37°C for human enzymes), then falls rapidly as the enzyme denatures. pH: each enzyme has an optimum pH (most 6-8; pepsin 2; trypsin 8); extreme pH denatures enzymes. Substrate concentration: rate rises until the saturation point, then stays constant because no active sites are free.',
          'The substrate binds at the active site to form a temporary enzyme-substrate (ES) complex; the active site catalyses the reaction; the complex breaks and the enzyme and products are released: Enzyme + Substrate → ES complex → Enzyme + Products. Explained by the lock and key model and the induced fit model.',
          'Enzymes are proteins secreted by cells; act as catalysts by lowering activation energy; are specific for substrate and reaction; small amounts act on large quantities of substrate and are not used up; may be intracellular or extracellular; may work in sequences; some need cofactors (prosthetic groups, coenzymes, activators).',
          'a. A: substrate; B: enzyme (active site); C: products. b. Enzymes are specific (shape of active site) and are not used up/reused; without the enzyme the reaction would proceed very slowly because activation energy is high. c. (i) rate increases; (ii) rate decreases rapidly. d. Denatured.',
          'A. Highest at about 40°C; above this the enzyme is denatured and activity falls. B. (i) pepsin about pH 2 (graph peak near 2); (ii) lipase about pH 8; away from the optimum, activity decreases.']


def keypoints_section():
    s = Section('bio6_keypoints', 'Key Points', 'Key Points', 'اہم نکات', 'مهم ټکي', [128])
    s.ul(KEY_POINTS)
    return s


def exercise():
    return dict(sourcePdfPages=[129, 130, 131], sourcePrintedPages=[126, 127, 128], heading='A. Encircle the best suitable answers.',
                mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
                shortQuestions=[dict(q=q, answer=LAB + a, sourceSection='B. Give short answers to the following questions.') for q, a in zip(SQ, SQ_ANS)],
                detailedQuestions=[dict(q=q, answer=LAB + a, sourceSection='C. Give detailed answers to the following questions. (The book numbers these i, ii, iii, iv, vi; there is no v.)') for q, a in zip(LQ, LQ_ANS)],
                activities=[dict(title='Activity 6.1', desc='Build or design model of an enzyme to demonstrate the working of an enzyme.', sourcePrintedPage=122),
                            dict(title='Activities 6.2', desc='Perform an experiment to show the working of enzyme in vitro (out of body or in a test tube) e.g., pepsin working on meat in a test tube. Put diastase in a starch solution in test tube at 37°C and after fifteen minutes perform iodine test for presence of starch.', sourcePrintedPage=124)])
