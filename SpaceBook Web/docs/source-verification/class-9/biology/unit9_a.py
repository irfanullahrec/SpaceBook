# -*- coding: utf-8 -*-
"""Unit 9 part A — PDF 181-188 (printed 178-185): SLOs, intro, 9.1 transport in plants, 9.2 transpiration, start of 9.3."""
from bio9_tools import Section, svg_wrap, txt
from unit4_figs2 import pointer

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
PR = ('Point to remember', 'یاد رکھنے کا نکتہ', 'د یادولو ټکی')
AI = ('Analysing and Interpreting', 'تجزیہ اور توضیح', 'شننه او تفسیر')


def lab(L, k):
    return L[k] if isinstance(L[k], list) else [L[k]]


# ---- Figure 9.1 root structure -------------------------------------------------
def root_fig(L):
    b = ['<circle cx="300" cy="140" r="120" fill="#fff8e1" stroke="#a1887f" stroke-width="3"/>',
         '<circle cx="300" cy="140" r="112" fill="none" stroke="#d7ccc8" stroke-width="10" stroke-dasharray="12 3"/>']
    for r in (95, 80, 65):
        b.append(f'<circle cx="300" cy="140" r="{r}" fill="none" stroke="#e0c9a6" stroke-width="12" stroke-dasharray="14 3"/>')
    b.append('<circle cx="300" cy="140" r="52" fill="none" stroke="#6d4c41" stroke-width="4"/>')
    b.append('<circle cx="300" cy="140" r="46" fill="#ffcc80" stroke="#ef6c00" stroke-width="3"/>')
    b.append('<path d="M300,100 L300,180 M260,140 L340,140 M272,112 L328,168 M328,112 L272,168" stroke="#c62828" stroke-width="9" stroke-linecap="round"/>')
    for x, y in ((318, 118), (282, 118), (282, 162), (318, 162)):
        b.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#43a047"/>')
    b.append('<path d="M190,190 C150,220 120,250 70,262" stroke="#8d6e63" stroke-width="7" fill="none" stroke-linecap="round"/>')
    b.append('<path d="M75,240 C130,225 180,200 230,165 C260,150 280,145 300,140" stroke="#1e88e5" stroke-width="2.5" stroke-dasharray="6 4" fill="none"/>')
    b.append('<path d="M70,282 C130,270 190,235 245,190" stroke="#039be5" stroke-width="2.5" fill="none"/>')
    b.append(pointer(95, 234, 10, 180, lab(L, 'cells'), 'start') + pointer(75, 280, 20, 300, lab(L, 'walls'), 'start'))
    b.append(pointer(130, 248, 160, 300, lab(L, 'hair')) + pointer(195, 140, 120, 90, lab(L, 'epidermis'), 'end'))
    b.append(pointer(215, 120, 120, 50, lab(L, 'cortex'), 'end') + pointer(250, 140, 470, 290, lab(L, 'endo')))
    b.append(pointer(344, 120, 470, 60, lab(L, 'pericycle')) + pointer(330, 140, 470, 140, lab(L, 'xylem')) + pointer(318, 162, 470, 210, lab(L, 'phloem')))
    return svg_wrap('<g transform="translate(60,0)">' + ''.join(b) + '</g>', 640, 320, L['title'])


ROOT = {'en': dict(title='Figure 9.1: The internal structure of root', cells=['Water & salts', 'moving through cells'], walls=['Water & salts moving', 'through cell walls'], hair='Root hair', epidermis='Epidermis', cortex='Cortex', endo='Endodermis', pericycle='Pericycle', xylem='Xylem', phloem='Phloem'),
        'ur': dict(title='شکل 9.1', cells=['پانی اور نمکیات', 'خلیوں کے اندر سے'], walls=['پانی اور نمکیات', 'خلوی دیواروں سے'], hair='جڑ کا بال', epidermis='اپی ڈرمس', cortex='کارٹیکس', endo='اینڈوڈرمس', pericycle='پیری سائیکل', xylem='زائلم', phloem='فلوئم'),
        'ps': dict(title='شکل 9.1', cells=['اوبه او مالګې', 'له حجرو دننه'], walls=['اوبه او مالګې', 'له حجروي دېوالونو'], hair='د ریښې وېښته', epidermis='اپیډرمس', cortex='کورټکس', endo='انډوډرمس', pericycle='پیري سایکل', xylem='زایلم', phloem='فلویم')}


# ---- Figure 9.2 events of transpiration -------------------------------------------
def leaf_fig(L):
    b = ['<rect x="150" y="20" width="300" height="24" fill="#c8e6c9" stroke="#2e7d32"/>']
    for i in range(10):
        b.append(f'<rect x="{154 + i*29.5}" y="48" width="25" height="70" rx="10" fill="#81c784" stroke="#2e7d32"/>')
    for i in range(9):
        for j in range(2):
            b.append(f'<ellipse cx="{170 + i*33 + j*12}" cy="{140 + j*30}" rx="13" ry="10" fill="#a5d6a7" stroke="#2e7d32"/>')
    b.append('<rect x="340" y="125" width="110" height="18" fill="#795548"/>')
    b.append('<rect x="150" y="200" width="300" height="20" fill="#c8e6c9" stroke="#2e7d32"/>')
    b.append('<rect x="235" y="198" width="30" height="24" fill="#fff"/><ellipse cx="240" cy="210" rx="7" ry="11" fill="#43a047"/><ellipse cx="260" cy="210" rx="7" ry="11" fill="#43a047"/>')
    b.append('<path d="M250,190 C245,170 260,160 255,150" stroke="#1e88e5" stroke-width="2" stroke-dasharray="3 3" fill="none"/><path d="M250,225 l0,30" stroke="#1e88e5" stroke-width="2" stroke-dasharray="3 3"/>')
    b.append(pointer(150, 32, 90, 32, lab(L, 'upper'), 'end') + pointer(152, 100, 90, 100, lab(L, 'meso'), 'end'))
    b.append(pointer(240, 170, 90, 165, lab(L, 'vapour'), 'end') + pointer(150, 210, 90, 210, lab(L, 'lower'), 'end'))
    b.append(pointer(250, 222, 200, 250, lab(L, 'stoma'), 'end') + pointer(262, 220, 300, 255, lab(L, 'guard')) + pointer(400, 143, 430, 255, lab(L, 'xylem')))
    return svg_wrap(''.join(b), 520, 285, L['title'])


LEAF = {'en': dict(title='Figure 9.2: Events of Transpiration', upper=['Upper', 'epidermis'], meso=['Mesophyll', 'cells'], vapour=['Water', 'vapours'], lower=['Lower', 'epidermis'], stoma='Stoma', guard=['Guard', 'cells'], xylem='Xylem'),
        'ur': dict(title='شکل 9.2', upper=['بالائی', 'اپی ڈرمس'], meso=['میزوفل', 'خلیے'], vapour=['پانی کے', 'بخارات'], lower=['زیریں', 'اپی ڈرمس'], stoma='اسٹوما', guard=['محافظ', 'خلیے'], xylem='زائلم'),
        'ps': dict(title='شکل 9.2', upper=['پورتنی', 'اپیډرمس'], meso=['میزوفیل', 'حجرې'], vapour=['د اوبو', 'بخارات'], lower=['ښکتنی', 'اپیډرمس'], stoma='سټوما', guard=['ساتونکې', 'حجرې'], xylem='زایلم')}


# ---- Figure 9.3 opening and closing of stoma ----------------------------------------
def stoma_fig(L):
    def pair(cx, open_):
        g = 22 if open_ else 4
        b = f'<rect x="{cx-110}" y="40" width="220" height="150" fill="#fff59d" stroke="#bdb76b"/>'
        for side in (-1, 1):
            x = cx + side * (g + 22)
            b += f'<ellipse cx="{x}" cy="115" rx="24" ry="58" fill="#90caf9" stroke="#1565c0" stroke-width="2"/>'
            b += ''.join(f'<circle cx="{x + side*6}" cy="{y}" r="4" fill="#e53935"/>' for y in (85, 105, 125, 145))
        if open_:
            b += f'<ellipse cx="{cx}" cy="115" rx="{g-2}" ry="45" fill="#fffde7"/>'
        for dx, dy in ((-75, 70), (75, 70), (-75, 165), (75, 165)):
            b += txt(cx + dx, 40 + dy, 'H₂O', 11, 'middle', 'bold')
            arrow_x = cx + dx * 0.6
            d = 1 if open_ else -1
            b += f'<path d="M{cx+dx*0.85},{40+dy-4} L{arrow_x},{40+dy-4}" stroke="#212121" stroke-width="1.5"/>' if open_ else f'<path d="M{arrow_x},{40+dy-4} L{cx+dx*0.85},{40+dy-4}" stroke="#212121" stroke-width="1.5"/>'
        return b
    b = pair(130, True) + pair(380, False)
    b += pointer(108, 95, 40, 70, lab(L, 'chloro'), 'end')
    b += pointer(150, 60, 190, 20, lab(L, 'guard'), 'middle') + pointer(290, 45, 270, 20, lab(L, 'epidermis'), 'middle')
    b += txt(130, 228, L['open'], 13, 'middle', 'bold') + txt(380, 228, L['closed'], 13, 'middle', 'bold')
    return svg_wrap('<g transform="translate(40,0)">' + b + '</g>', 560, 240, L['title'])


STOMA = {'en': dict(title='Figure 9.3: Opening and closing of stoma', chloro='Chloroplast', guard='Guard cells', epidermis='Epidermis', open='Open stoma', closed='Closed stoma'),
         'ur': dict(title='شکل 9.3', chloro='کلوروپلاسٹ', guard='محافظ خلیے', epidermis='اپی ڈرمس', open='کھلا اسٹوما', closed='بند اسٹوما'),
         'ps': dict(title='شکل 9.3', chloro='کلوروپلاسټ', guard='ساتونکې حجرې', epidermis='اپیډرمس', open='خلاص سټوما', closed='تړلی سټوما')}


# ---- Figure 9.4 transport of water in plants ----------------------------------------
def water_fig(L):
    b = ['<path d="M420,60 L380,170 L460,170 Z M420,100 L370,230 L470,230 Z" fill="#2e7d32"/><rect x="412" y="230" width="16" height="60" fill="#6d4c41"/>',
         '<path d="M412,290 l-30,25 M428,290 l30,25 M420,290 v30" stroke="#6d4c41" stroke-width="3"/>']
    for y, k in ((20, 'leaf'), (130, 'stem'), (230, 'root')):
        b.append(f'<rect x="170" y="{y}" width="120" height="80" fill="#e8f5e9" stroke="#33691e" transform="rotate(-8 230 {y+40})"/>')
        b.append(''.join(f'<path d="M{185 + i*22},{y+5} v70" stroke="#558b2f" stroke-width="5" transform="rotate(-8 230 {y+40})"/>' for i in range(5)))
        b.append(pointer(172, y + 45, 110, y + 45, lab(L, k), 'end'))
    b.append('<path d="M240,300 C235,260 235,200 232,130 C230,90 228,60 226,30" stroke="#1e88e5" stroke-width="3" stroke-dasharray="2 6" stroke-linecap="round" fill="none"/>')
    b.append('<path d="M295,50 C330,40 360,60 380,110" stroke="#43a047" stroke-width="3" fill="none"/><path d="M295,170 C330,170 360,200 375,200 M295,270 C330,280 370,285 400,295" stroke="#43a047" stroke-width="3" fill="none"/>')
    b.append(pointer(290, 30, 330, 20, lab(L, 'transp')))
    b.append(pointer(180, 305, 110, 320, lab(L, 'hair'), 'end') + pointer(248, 300, 300, 330, lab(L, 'molecule')))
    return svg_wrap(''.join(b), 520, 360, L['title'])


WATER = {'en': dict(title='Figure 9.4: Transport of water in plants', leaf=['Xylem', 'of leaf'], stem=['Xylem', 'of stem'], root=['Xylem', 'of root'], transp='Transpiration', hair=['Root', 'hair'], molecule=['Water', 'molecule']),
         'ur': dict(title='شکل 9.4', leaf=['پتے کا', 'زائلم'], stem=['تنے کا', 'زائلم'], root=['جڑ کا', 'زائلم'], transp='عملِ تبخیر', hair=['جڑ کا', 'بال'], molecule=['پانی کا', 'مالیکیول']),
         'ps': dict(title='شکل 9.4', leaf=['د پاڼې', 'زایلم'], stem=['د ډډ', 'زایلم'], root=['د ریښې', 'زایلم'], transp='ټرانسپایرېشن', hair=['د ریښې', 'وېښته'], molecule=['د اوبو', 'مالیکول'])}


def tri(fn, D):
    return [fn(D[k]) for k in ('en', 'ur', 'ps')]


def sections():
    out = []
    s = Section('bio9_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [181, 182])
    s.h('After studying this unit, the students will be able to', 'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې')
    s.ul([
        ('Conceptualize transport and its needs', 'نقل و حمل اور اس کی ضروریات کا تصور کر سکیں', 'لېږد او د هغه اړتیاوې درک کړي'),
        ('Explain the internal structure of root and root hair.', 'جڑ اور جڑ کے بال کی اندرونی ساخت کی وضاحت کر سکیں۔', 'د ریښې او د ریښې د وېښته داخلي جوړښت تشریح کړي.'),
        ('Describe how roots take up water and mineral salts by active and passive absorption.', 'بیان کر سکیں کہ جڑیں فعال اور غیر فعال جذب سے پانی اور معدنی نمکیات کیسے لیتی ہیں۔', 'بیان کړي چې ریښې څنګه په فعال او غیر فعال جذب اوبه او معدني مالګې اخلي.'),
        ('Define transpiration and relate this process with cell surface.', 'عملِ تبخیر کی تعریف کر کے اسے خلوی سطح سے منسلک کر سکیں۔', 'ټرانسپایرېشن تعریف کړي او له حجروي سطحې سره یې وتړي.'),
        ('Relate transpiration with stomatal opening and closing', 'عملِ تبخیر کو اسٹوما کے کھلنے اور بند ہونے سے منسلک کر سکیں', 'ټرانسپایرېشن د سټوما له خلاصېدو او تړل کېدو سره وتړي'),
        ('Describe temperature, wind and humidity as the factors affecting the rate of transpiration.', 'درجۂ حرارت، ہوا اور نمی کو عملِ تبخیر کی شرح پر اثر انداز عوامل کے طور پر بیان کر سکیں۔', 'تودوخه، باد او رطوبت د ټرانسپایرېشن پر کچه د اغېزمنو عواملو په توګه بیان کړي.'),
        ('Describe the significance of transpiration', 'عملِ تبخیر کی اہمیت بیان کر سکیں', 'د ټرانسپایرېشن اهمیت بیان کړي'),
        ('Describe transpiration as a necessary evil', 'عملِ تبخیر کو ایک ضروری برائی کے طور پر بیان کر سکیں', 'ټرانسپایرېشن د یوې اړینې بدۍ په توګه بیان کړي'),
        ('Relate wilting with excessive transpiration', 'مرجھانے کو زیادہ عملِ تبخیر سے منسلک کر سکیں', 'مړاوي کېدل له ډېر ټرانسپایرېشن سره وتړي'),
        ('Describe the pathway of water and food in stem.', 'تنے میں پانی اور خوراک کا راستہ بیان کر سکیں۔', 'په ډډ کې د اوبو او خوړو لاره بیان کړي.'),
        ('Explain the movement of water in terms of transpirational pull.', 'ٹرانسپائریشنل پُل کے لحاظ سے پانی کی حرکت کی وضاحت کر سکیں۔', 'د اوبو حرکت د ټرانسپایرېشنل کشش له مخې تشریح کړي.'),
        ('Explain the mechanism of food translocation by the theory of Pressure Flow Mechanism.', 'پریشر فلو میکانزم کے نظریے سے خوراک کی ترسیل کا طریقہ کار واضح کر سکیں۔', 'د فشار جریان میکانیزم د تیورۍ له مخې د خوړو د لېږد میکانیزم تشریح کړي.'),
        ('List the functions of the components of blood.', 'خون کے اجزا کے افعال کی فہرست بنا سکیں۔', 'د وینې د برخو دندې لېست کړي.'),
        ('Describe the blood groups in A-B-O and Rh blood group systems, with reference to the presence/absence of antigens and antibodies.', 'اینٹی جنز اور اینٹی باڈیز کی موجودگی/غیر موجودگی کے حوالے سے A-B-O اور Rh بلڈ گروپ نظاموں میں خون کے گروپ بیان کر سکیں۔', 'د انټي جنونو او انټي باډيو د شتون/نشتون په اړه د A-B-O او Rh سیسټمونو د وینې ګروپونه بیان کړي.'),
        ('State the risk of incompatibility in blood transfusion due to antigen-antibody reactions.', 'اینٹی جن اینٹی باڈی تعاملات کی وجہ سے انتقالِ خون میں عدم مطابقت کا خطرہ بیان کر سکیں۔', 'د انټي جن انټي باډي تعاملونو له امله د وینې په لېږد کې د نامطابقت خطر بیان کړي.'),
        ('List the appropriate donors and recipients for each of the four blood groups', 'چاروں بلڈ گروپس میں سے ہر ایک کے لیے مناسب عطیہ دہندگان اور وصول کنندگان کی فہرست بنا سکیں', 'د څلورو وینې ګروپونو هر یوه لپاره مناسب ورکوونکي او اخیستونکي لېست کړي'),
        ('State the sign and symptoms, causes and treatments of the diseases of blood (leukemia and thalassaemia).', 'خون کی بیماریوں (لیوکیمیا اور تھیلیسیمیا) کی علامات، وجوہات اور علاج بیان کر سکیں۔', 'د وینې د ناروغیو (لوکیمیا او تالاسیمیا) نښې، لاملونه او درملنه بیان کړي.'),
        ('Describe the major pathway of blood through circulatory system.', 'دورانِ خون کے نظام میں خون کا بڑا راستہ بیان کر سکیں۔', 'د دوران سیسټم له لارې د وینې لویه لاره بیان کړي.'),
        ('Describe the external and internal structure of human heart.', 'انسانی دل کی بیرونی اور اندرونی ساخت بیان کر سکیں۔', 'د انسان د زړه بهرنی او داخلي جوړښت بیان کړي.'),
        ('Describe the circulation of blood through atria and ventricles of the heart, explaining the role of the bicuspid, tricuspid and semilunar valves.', 'دل کے ایٹریا اور وینٹریکلز سے خون کے دوران کو بائی کسپڈ، ٹرائی کسپڈ اور سیمی لیونر والوز کے کردار کے ساتھ بیان کر سکیں۔', 'د زړه له اذینونو او بطینونو د وینې دوران د بای کسپډ، ټرای کسپډ او نیم سپوږمۍ والونو د رول سره بیان کړي.'),
        ('Describe the low-pressure circulation to the lungs and a high-pressure circulation to the body tissues.', 'پھیپھڑوں تک کم دباؤ والے اور جسم کی بافتوں تک زیادہ دباؤ والے دوران کو بیان کر سکیں۔', 'سږو ته د ټیټ فشار دوران او د بدن نسجونو ته د لوړ فشار دوران بیان کړي.'),
        ('Explain how the heart is structurally adapted to its functions.', 'وضاحت کر سکیں کہ دل ساخت کے لحاظ سے اپنے افعال کے لیے کیسے موزوں ہے۔', 'تشریح کړي چې زړه څنګه د خپلو دندو لپاره جوړښتي برابر دی.'),
        ('Define the terms heartbeat, heart rate and pulse rate.', 'دل کی دھڑکن، دل کی شرح اور نبض کی شرح کی اصطلاحات کی تعریف کر سکیں۔', 'د زړه ټکان، د زړه کچه او د نبض کچه اصطلاحات تعریف کړي.'),
        ('Compare the structure and function of an artery, a vein and a capillary', 'شریان، ورید اور شعری نالی کی ساخت اور کام کا موازنہ کر سکیں', 'د شریان، ورید او شعریه رګ جوړښت او دنده پرتله کړي'),
        ('Describe the transfer of materials between capillaries and tissue fluid.', 'شعری نالیوں اور بافتی سیال کے درمیان مادوں کی منتقلی بیان کر سکیں۔', 'د شعریه رګونو او نسجي مایع ترمنځ د موادو لېږد بیان کړي.'),
        ('Describe the origins, locations and targets areas of main arteries.', 'اہم شریانوں کے آغاز، مقامات اور ہدف کے علاقے بیان کر سکیں۔', 'د اصلي شریانونو پیل، ځایونه او موخې سیمې بیان کړي.'),
        ('Describe the originating areas, locations and target heart chambers of main veins.', 'اہم وریدوں کے آغاز کے علاقے، مقامات اور ہدف کے دل کے خانے بیان کر سکیں۔', 'د اصلي وریدونو د پیل سیمې، ځایونه او د زړه موخې خونې بیان کړي.'),
        ('Identify the main arteries and veins in charts, diagrams, models etc.', 'چارٹس، خاکوں، ماڈلز وغیرہ میں اہم شریانوں اور وریدوں کی شناخت کر سکیں۔', 'په چارټونو، ډیاګرامونو، ماډلونو او نورو کې اصلي شریانونه او وریدونه وپېژني.'),
        ('Describe the contributions of Ibn-al-Nafees and William Harvey in revealing the knowledge about the circulation of blood in human body.', 'انسانی جسم میں دورانِ خون کے علم کو سامنے لانے میں ابن النفیس اور ولیم ہاروے کی خدمات بیان کر سکیں۔', 'په انساني بدن کې د وینې د دوران د پوهې په څرګندولو کې د ابن النفیس او ویلیم هاروي ونډې بیان کړي.'),
        ('Define cardiovascular disorders and differentiate between Atherosclerosis and Arteriosclerosis.', 'دل اور خون کی نالیوں کی خرابیوں کی تعریف اور ایتھروسکلیروسس اور آرٹیریوسکلیروسس میں فرق کر سکیں۔', 'د زړه او رګونو اختلالات تعریف کړي او د اتروسکلیروزس او ارټیریوسکلیروزس ترمنځ توپیر وکړي.'),
        ('State the causes, treatments and prevention of myocardial infarction.', 'مایوکارڈیل انفارکشن کی وجوہات، علاج اور روک تھام بیان کر سکیں۔', 'د مایوکارډیل انفارکشن لاملونه، درملنه او مخنیوی بیان کړي.'),
    ])
    out.append(s)

    s = Section('bio9_1', '9.1', 'Transport in Plants', 'پودوں میں نقل و حمل', 'په بوټو کې لېږد', [183, 184])
    s.p('Living organisms always require certain materials for their metabolic processes. In a particular environment different types of materials either move in or out of the body of an organism. This movement of molecules into and out of the body or cells of an organism is called transport.',
        'جانداروں کو اپنے میٹابولک عوامل کے لیے ہمیشہ کچھ مادے درکار ہوتے ہیں۔ کسی خاص ماحول میں مختلف قسم کے مادے جاندار کے جسم میں داخل ہوتے یا اس سے باہر نکلتے ہیں۔ جاندار کے جسم یا خلیوں میں مالیکیولز کے اندر آنے اور باہر جانے کی اس حرکت کو نقل و حمل (ٹرانسپورٹ) کہتے ہیں۔',
        'ژوندي موجودات تل د خپلو میټابولیکي پروسو لپاره ځینو موادو ته اړتیا لري. په یوه ځانګړي چاپېریال کې بېلابېل مواد د ژوندي موجود بدن ته ننوځي یا ترې وځي. د ژوندي موجود بدن یا حجرو ته د مالیکولونو د ننوتلو او وتلو دې حرکت ته لېږد (ټرانسپورټ) ویل کېږي.')
    s.callout(PR, [('In multi-cellular organisms, an organ system is responsible for the transport of materials. In unicellular organisms there is no such system, however processes, such as, diffusion, osmosis etc. sufficient for the transport of materials.', 'کثیر خلوی جانداروں میں مادوں کی نقل و حمل کا ذمہ دار ایک اعضائی نظام ہوتا ہے۔ یک خلوی جانداروں میں ایسا کوئی نظام نہیں ہوتا، تاہم نفوذ، اوسموسس وغیرہ جیسے عوامل مادوں کی نقل و حمل کے لیے کافی ہیں۔', 'په څو حجروي ژوندیو موجوداتو کې د موادو د لېږد مسؤل یو غړیز سیسټم وي. په یو حجروي ژوندیو موجوداتو کې داسې سیسټم نشته، خو پروسې لکه خپرېدل، اوسموزس او نور د موادو د لېږد لپاره بس دي.')])
    s.p('Unicellular and less complex multicellular organisms do not have any specific organs for transport. They perform this process by simple diffusion or active transport. In more complex animals and plants, there are special organ systems for exchange of material with the environment and for transport of material within the body.',
        'یک خلوی اور کم پیچیدہ کثیر خلوی جانداروں میں نقل و حمل کے لیے کوئی مخصوص اعضا نہیں ہوتے۔ وہ یہ عمل سادہ نفوذ یا فعال نقل و حمل سے انجام دیتے ہیں۔ زیادہ پیچیدہ جانوروں اور پودوں میں ماحول سے مادوں کے تبادلے اور جسم کے اندر مادوں کی نقل و حمل کے لیے خاص اعضائی نظام ہوتے ہیں۔',
        'یو حجروي او لږ پېچلي څو حجروي ژوندي موجودات د لېږد لپاره کوم ځانګړي غړي نه لري. دا پروسه په ساده خپرېدو یا فعال لېږد ترسره کوي. په ډېرو پېچلو ژویو او بوټو کې له چاپېریال سره د موادو د تبادلې او په بدن کې د موادو د لېږد لپاره ځانګړي غړیز سیسټمونه وي.')
    s.p('Each and every cell of the body needs food and oxygen and also needs to remove the waste products, it produces during its metabolic activities. However, every cell is not in direct contact with the external sources to get nutrients and remove wastes. Also, the cells are not in direct contact with the organs/ tissues/ cells of the body where these nutrients are formed and wastes are stored. Hence a system is needed to transport all the needs like O₂, CO₂, nutrients, water etc. and to remove the wastes from the cells. All organisms whether unicellular or multicellular, plants or animals, simple or complex, have a transport system in their bodies. In this unit, we will discuss the process of transport in plants and humans.',
        'جسم کے ہر خلیے کو خوراک اور آکسیجن درکار ہے اور اسے اپنی میٹابولک سرگرمیوں کے دوران بننے والے فضلات کو بھی خارج کرنا ہوتا ہے۔ تاہم ہر خلیہ غذائی اجزا لینے اور فضلات خارج کرنے کے لیے بیرونی ذرائع سے براہِ راست رابطے میں نہیں ہوتا۔ نیز خلیے جسم کے ان اعضا/بافتوں/خلیوں سے بھی براہِ راست رابطے میں نہیں ہوتے جہاں یہ غذائی اجزا بنتے اور فضلات ذخیرہ ہوتے ہیں۔ اس لیے O₂، CO₂، غذائی اجزا، پانی وغیرہ جیسی تمام ضروریات کی نقل و حمل اور خلیوں سے فضلات کے اخراج کے لیے ایک نظام درکار ہے۔ تمام جاندار، یک خلوی ہوں یا کثیر خلوی، پودے ہوں یا جانور، سادہ ہوں یا پیچیدہ، اپنے جسم میں نقل و حمل کا نظام رکھتے ہیں۔ اس یونٹ میں ہم پودوں اور انسانوں میں نقل و حمل کے عمل پر بحث کریں گے۔',
        'د بدن هره حجره خوړو او اکسیجن ته اړتیا لري او باید هغه فاضله مواد هم وباسي چې د میټابولیکي فعالیتونو پر مهال یې تولیدوي. خو هره حجره د غذايي موادو د اخیستو او د فاضله موادو د ایستلو لپاره له بهرنیو سرچینو سره مستقیمه اړیکه نه لري. همدارنګه حجرې د بدن له هغو غړو/نسجونو/حجرو سره هم مستقیمه اړیکه نه لري چې دا غذايي مواد پکې جوړېږي او فاضله مواد پکې زېرمه کېږي. نو د ټولو اړتیاوو لکه O₂، CO₂، غذايي موادو، اوبو او نورو د لېږد او له حجرو د فاضله موادو د ایستلو لپاره یو سیسټم اړین دی. ټول ژوندي موجودات، که یو حجروي وي که څو حجروي، بوټي وي که ژوي، ساده وي که پېچلي، په خپلو بدنونو کې د لېږد سیسټم لري. په دې یونټ کې به په بوټو او انسانانو کې د لېږد پروسه وڅېړو.')
    s.h('9.1 Transport in Plants', '9.1 پودوں میں نقل و حمل', '9.1 په بوټو کې لېږد')
    s.p('Plants transport many substances within the body. Water and dissolved salts are transported from the roots to the shoot through the xylem tissue. The food is transported from the leaves, where it is manufactured, to all other parts of the body through phloem tissue. Similarly, the stored food is transported from storage organs to all other parts.',
        'پودے اپنے جسم میں بہت سے مادوں کی نقل و حمل کرتے ہیں۔ پانی اور حل شدہ نمکیات زائلم بافت کے ذریعے جڑوں سے شاخ تک پہنچتے ہیں۔ خوراک پتوں سے، جہاں یہ بنتی ہے، فلوئم بافت کے ذریعے جسم کے دوسرے تمام حصوں تک پہنچتی ہے۔ اسی طرح ذخیرہ شدہ خوراک ذخیرہ کرنے والے اعضا سے دوسرے تمام حصوں تک پہنچتی ہے۔',
        'بوټي په خپل بدن کې ډېر مواد لېږدوي. اوبه او حل شوې مالګې د زایلم نسج له لارې له ریښو شاخ ته لېږدول کېږي. خواړه له پاڼو، چېرې چې جوړېږي، د فلویم نسج له لارې د بدن ټولو نورو برخو ته لېږدول کېږي. همدارنګه زېرمه شوي خواړه له زېرمه کوونکو غړو ټولو نورو برخو ته لېږدول کېږي.')
    s.h('Absorption of Water and Salts', 'پانی اور نمکیات کا جذب', 'د اوبو او مالګو جذب')
    s.p('Water is absorbed by the plants through their roots. Roots are in contact with the soil from where water enters into roots tissues through osmosis. In order to understand the absorption of water and salts by roots, we have to study the internal structure of a root.',
        'پودے پانی اپنی جڑوں سے جذب کرتے ہیں۔ جڑیں مٹی سے رابطے میں ہوتی ہیں جہاں سے پانی اوسموسس کے ذریعے جڑ کی بافتوں میں داخل ہوتا ہے۔ جڑوں کے ذریعے پانی اور نمکیات کے جذب کو سمجھنے کے لیے ہمیں جڑ کی اندرونی ساخت کا مطالعہ کرنا ہوگا۔',
        'بوټي اوبه د خپلو ریښو له لارې جذبوي. ریښې له خاورې سره په تماس کې دي چې اوبه ترې د اوسموزس له لارې د ریښې نسجونو ته ننوځي. د ریښو له لارې د اوبو او مالګو د جذب د پوهېدو لپاره باید د ریښې داخلي جوړښت ولولو.')
    s.p('The outermost covering of the root i.e. epidermis is a single layer of cells. Many cells of epidermis have tiny hair-like extensions called root hair into the spaces in soil. The root hair are in direct contact with soil water. They provide large surface area to the root for the maximum absorption of water and salts.',
        'جڑ کا سب سے بیرونی غلاف یعنی اپی ڈرمس خلیوں کی ایک تہہ ہے۔ اپی ڈرمس کے بہت سے خلیوں میں مٹی کے خالی مقامات میں ننھے بال نما ابھار ہوتے ہیں جنہیں جڑ کے بال کہتے ہیں۔ جڑ کے بال مٹی کے پانی سے براہِ راست رابطے میں ہوتے ہیں۔ یہ پانی اور نمکیات کے زیادہ سے زیادہ جذب کے لیے جڑ کو بڑا سطحی رقبہ فراہم کرتے ہیں۔',
        'د ریښې بهرنی پوښ یعنې اپیډرمس د حجرو یو پوړ دی. د اپیډرمس ډېرې حجرې د خاورې تشو ځایونو ته کوچني وېښته ډوله غځېدنې لري چې د ریښې وېښتان بلل کېږي. د ریښې وېښتان د خاورې له اوبو سره مستقیم تماس لري. د اوبو او مالګو د اعظمي جذب لپاره ریښې ته لویه سطحه برابروي.')
    s.p('The root hair cells have high concentration of salts as compared to their surrounding soil water. They also take in more salts by active transport. Due to this higher concentration of salts in root hair cells, water moves by passive transport i.e. osmosis from soil into the root hair cells. From root hair cells, water goes by osmosis to the other cells of epidermis.',
        'جڑ کے بالوں کے خلیوں میں اپنے اردگرد کے مٹی کے پانی کی نسبت نمکیات کا زیادہ ارتکاز ہوتا ہے۔ یہ فعال نقل و حمل سے مزید نمکیات بھی لیتے ہیں۔ جڑ کے بالوں کے خلیوں میں نمکیات کے اس زیادہ ارتکاز کی وجہ سے پانی غیر فعال نقل و حمل یعنی اوسموسس سے مٹی سے جڑ کے بالوں کے خلیوں میں جاتا ہے۔ جڑ کے بالوں کے خلیوں سے پانی اوسموسس سے اپی ڈرمس کے دوسرے خلیوں میں جاتا ہے۔',
        'د ریښې د وېښتانو حجرې د شاوخوا خاورې د اوبو په پرتله د مالګو لوړ غلظت لري. دوی د فعال لېږد له لارې نورې مالګې هم اخلي. د ریښې د وېښتانو په حجرو کې د مالګو د دې لوړ غلظت له امله اوبه د غیر فعال لېږد یعنې اوسموزس له لارې له خاورې د ریښې د وېښتانو حجرو ته ځي. له دې حجرو اوبه په اوسموزس د اپیډرمس نورو حجرو ته ځي.')
    s.callout(AI, [('Identify root hairs on a growing root of onion, carrot etc.', 'پیاز، گاجر وغیرہ کی بڑھتی جڑ پر جڑ کے بالوں کی شناخت کریں۔', 'د پیاز، ګازرې او نورو په وده کوونکې ریښه د ریښې وېښتان وپېژنئ.')])
    s.p('From epidermis, salts and water move to the cortex of root. It is present just below the epidermis. The innermost boundary of the cortex is the endodermis. The water and salts move to a narrow layer of cells called pericycle. After crossing pericycle, water and salts reach in the innermost region where vascular tissue i.e. xylem and phloem are present. Water and salts enter the xylem of root. The xylem and phloem of root are connected to the xylem and phloem of the stem.',
        'اپی ڈرمس سے نمکیات اور پانی جڑ کے کارٹیکس میں جاتے ہیں۔ یہ اپی ڈرمس کے بالکل نیچے ہوتا ہے۔ کارٹیکس کی سب سے اندرونی حد اینڈوڈرمس ہے۔ پانی اور نمکیات خلیوں کی ایک تنگ تہہ میں جاتے ہیں جسے پیری سائیکل کہتے ہیں۔ پیری سائیکل پار کرنے کے بعد پانی اور نمکیات سب سے اندرونی حصے میں پہنچتے ہیں جہاں ویسکولر بافت یعنی زائلم اور فلوئم ہوتے ہیں۔ پانی اور نمکیات جڑ کے زائلم میں داخل ہوتے ہیں۔ جڑ کے زائلم اور فلوئم تنے کے زائلم اور فلوئم سے جڑے ہوتے ہیں۔',
        'له اپیډرمس څخه مالګې او اوبه د ریښې کورټکس ته ځي. دا د اپیډرمس لاندې پروت دی. د کورټکس داخلي پوله انډوډرمس ده. اوبه او مالګې د حجرو یوه نري پوړ ته ځي چې پیري سایکل بلل کېږي. له پیري سایکل وروسته اوبه او مالګې داخلي سیمې ته رسېږي چې وعايي نسج یعنې زایلم او فلویم پکې دي. اوبه او مالګې د ریښې زایلم ته ننوځي. د ریښې زایلم او فلویم د ډډ له زایلم او فلویم سره تړلي دي.')
    en, ur, ps = tri(root_fig, ROOT)
    s.fig('bio9-fig9-1', en, ur, ps, .65, caption=('Figure 9.1: The internal structure of root and the passage of water and minerals through the root', 'شکل 9.1: جڑ کی اندرونی ساخت اور جڑ سے پانی اور معدنیات کا گزر', 'شکل 9.1: د ریښې داخلي جوړښت او له ریښې د اوبو او معدنونو تېرېدل'))
    out.append(s)

    s = Section('bio9_2', '9.2', 'Transpiration', 'عملِ تبخیر (ٹرانسپائریشن)', 'ټرانسپایرېشن', [185, 186, 187, 188])
    s.h('9.2 Transpiration', '9.2 عملِ تبخیر', '9.2 ټرانسپایرېشن')
    s.p('Loss of water in the form of vapours from the aerial parts of the plant, is called transpiration. Transpiration occurs mainly through the special openings present in leaf epidermis. These openings are called stomata (Singular: stoma). In leaves, water is present in the xylem tissues. This water moves to the cell walls of mesophyll cells. From the moist walls of mesophyll cells, water evaporates into the air spaces of the leaf. These water vapours then move towards the stomata and pass into the outside air.',
        'پودے کے ہوائی حصوں سے بخارات کی شکل میں پانی کے ضیاع کو عملِ تبخیر (ٹرانسپائریشن) کہتے ہیں۔ عملِ تبخیر زیادہ تر پتے کی اپی ڈرمس میں موجود خاص سوراخوں سے ہوتا ہے۔ ان سوراخوں کو اسٹومیٹا (واحد: اسٹوما) کہتے ہیں۔ پتوں میں پانی زائلم بافتوں میں ہوتا ہے۔ یہ پانی میزوفل خلیوں کی دیواروں تک جاتا ہے۔ میزوفل خلیوں کی نم دیواروں سے پانی بخارات بن کر پتے کی ہوائی جگہوں میں جاتا ہے۔ پھر یہ آبی بخارات اسٹومیٹا کی طرف جا کر باہر کی ہوا میں نکل جاتے ہیں۔',
        'د بوټي له هوايي برخو د بخار په بڼه د اوبو ضایع کېدو ته ټرانسپایرېشن ویل کېږي. ټرانسپایرېشن ډېری د پاڼې په اپیډرمس کې د ځانګړو سوریو له لارې کېږي. دې سوریو ته سټوماټا (مفرد: سټوما) ویل کېږي. په پاڼو کې اوبه په زایلم نسجونو کې وي. دا اوبه د میزوفیل حجرو دېوالونو ته ځي. د میزوفیل حجرو له لندو دېوالونو اوبه تبخیرېږي او د پاڼې هوايي ځایونو ته ځي. بیا دا بخارات سټوماټا ته ځي او بهرنۍ هوا ته وځي.')
    s.callout(PR, [('Some transpiration also occurs through the cuticle present on leaf epidermis and through special openings called lenticels present in the stems of some plants.', 'کچھ عملِ تبخیر پتے کی اپی ڈرمس پر موجود کیوٹیکل اور بعض پودوں کے تنوں میں موجود لینٹی سیلز نامی خاص سوراخوں سے بھی ہوتا ہے۔', 'ځینې ټرانسپایرېشن د پاڼې پر اپیډرمس د کیوټیکل له لارې او د ځینو بوټو په ډډونو کې د لېنټي سېل په نوم ځانګړو سوریو له لارې هم کېږي.')])
    s.callout(SI, [('More than 90% water absorbed by the roots is ultimately lost to the atmosphere through transpiration.', 'جڑوں سے جذب ہونے والا 90% سے زیادہ پانی آخرکار عملِ تبخیر سے فضا میں ضائع ہو جاتا ہے۔', 'د ریښو له خوا جذب شوې له 90% ډېرې اوبه په پای کې د ټرانسپایرېشن له لارې اتموسفیر ته ضایع کېږي.')])
    en, ur, ps = tri(leaf_fig, LEAF)
    s.fig('bio9-fig9-2', en, ur, ps, .55, caption=('Figure 9.2: Events of Transpiration', 'شکل 9.2: عملِ تبخیر کے مراحل', 'شکل 9.2: د ټرانسپایرېشن پېښې'))
    s.h('9.2.1 Stomatal Control of Transpiration', '9.2.1 اسٹوما کے ذریعے عملِ تبخیر کا کنٹرول', '9.2.1 د سټوما له لارې د ټرانسپایرېشن کنټرول')
    s.p('Transpiration occurs through stomata which allows the water vapours to transpire into the environment. When there is sufficient water, stomata remain open allowing transpiration to take place. Each stoma is lined by two bean shaped cells called guard cells. Guard cells are the only epidermal cells which contain chloroplasts. Stomata open and close when the turgor pressure of guard cells changes. Stoma opens when guard cells are turgid, while it closes when guard cells become flaccid.',
        'عملِ تبخیر اسٹومیٹا سے ہوتا ہے جو آبی بخارات کو ماحول میں جانے دیتے ہیں۔ جب کافی پانی ہو تو اسٹومیٹا کھلے رہتے ہیں اور عملِ تبخیر ہوتا رہتا ہے۔ ہر اسٹوما دو لوبیا نما خلیوں سے گھرا ہوتا ہے جنہیں محافظ خلیے (گارڈ سیلز) کہتے ہیں۔ محافظ خلیے اپی ڈرمس کے وہ واحد خلیے ہیں جن میں کلوروپلاسٹ ہوتے ہیں۔ محافظ خلیوں کا ٹرگر دباؤ بدلنے سے اسٹومیٹا کھلتے اور بند ہوتے ہیں۔ جب محافظ خلیے تنے ہوئے (ٹرجڈ) ہوں تو اسٹوما کھلتا ہے اور جب ڈھیلے (فلیسڈ) ہو جائیں تو بند ہو جاتا ہے۔',
        'ټرانسپایرېشن د سټوماټا له لارې کېږي چې بخارات چاپېریال ته پرېږدي. کله چې کافي اوبه وي، سټوماټا خلاص پاتې کېږي او ټرانسپایرېشن کېږي. هر سټوما د لوبیا په شکل دوو حجرو پوښلی چې ساتونکې حجرې بلل کېږي. ساتونکې حجرې د اپیډرمس یوازینۍ حجرې دي چې کلوروپلاسټ لري. د ساتونکو حجرو د ټرګر فشار په بدلون سټوماټا خلاصېږي او تړل کېږي. کله چې ساتونکې حجرې ټرګیډ (کلکې) وي سټوما خلاصېږي او کله چې فلاسیډ (سستې) شي تړل کېږي.')
    s.callout(SI, [('Desert plants have very few or no stomata. Their leaves are modified into thorns to minimize transpiration.', 'صحرائی پودوں میں بہت کم یا کوئی اسٹومیٹا نہیں ہوتے۔ عملِ تبخیر کم کرنے کے لیے ان کے پتے کانٹوں میں بدل جاتے ہیں۔', 'د دښتې بوټي ډېر لږ یا هېڅ سټوماټا نه لري. د ټرانسپایرېشن د کمولو لپاره یې پاڼې په ازغیو بدلې شوې.')])
    s.callout(PR, [('During daytime, movement of potassium ions in guard cells also increases their solute concentration.', 'دن کے وقت محافظ خلیوں میں پوٹاشیم آئنز کی حرکت بھی ان کے محلول کے ارتکاز کو بڑھاتی ہے۔', 'د ورځې پر مهال په ساتونکو حجرو کې د پوټاشیم ایونونو حرکت هم د هغوی د منحل موادو غلظت زیاتوي.')])
    s.p('During day time, guard cells do photosynthesis and prepare glucose. So the solute concentration remains high in guard cells. Therefore water moves in them and they become turgid. In turgid state, the inner walls of guard cells move outward and stoma opens. At evening, the glucose concentration in guard cells falls. Due to this, water also moves from guard cells and they lose turgor (state of turgidity). Their inner sides touch each other and the stoma closes.',
        'دن کے وقت محافظ خلیے ضیائی تالیف کر کے گلوکوز بناتے ہیں۔ اس لیے محافظ خلیوں میں محلول کا ارتکاز زیادہ رہتا ہے۔ چنانچہ پانی ان میں داخل ہوتا ہے اور وہ تن جاتے ہیں۔ تنی ہوئی حالت میں محافظ خلیوں کی اندرونی دیواریں باہر کی طرف ہٹتی ہیں اور اسٹوما کھل جاتا ہے۔ شام کو محافظ خلیوں میں گلوکوز کا ارتکاز کم ہو جاتا ہے۔ اس کی وجہ سے پانی بھی محافظ خلیوں سے نکل جاتا ہے اور وہ ٹرگر (تناؤ کی حالت) کھو دیتے ہیں۔ ان کے اندرونی حصے ایک دوسرے کو چھوتے ہیں اور اسٹوما بند ہو جاتا ہے۔',
        'د ورځې پر مهال ساتونکې حجرې فوتوسنتز کوي او ګلوکوز جوړوي. نو په ساتونکو حجرو کې د منحل موادو غلظت لوړ پاتې کېږي. له همدې امله اوبه پکې ننوځي او ټرګیډ کېږي. په ټرګیډ حالت کې د ساتونکو حجرو داخلي دېوالونه بهر ته ځي او سټوما خلاصېږي. ماښام د ساتونکو حجرو د ګلوکوز غلظت ټیټېږي. د دې له امله اوبه هم له ساتونکو حجرو وځي او ټرګر (د کلکوالي حالت) له لاسه ورکوي. داخلي خواوې یې یو بل سره لګېږي او سټوما تړل کېږي.')
    en, ur, ps = tri(stoma_fig, STOMA)
    s.fig('bio9-fig9-3', en, ur, ps, .6, caption=('Figure 9.3: Opening and closing of stoma', 'شکل 9.3: اسٹوما کا کھلنا اور بند ہونا', 'شکل 9.3: د سټوما خلاصېدل او تړل کېدل'))
    s.h('9.2.2 Factors Affecting Rate of Transpiration', '9.2.2 عملِ تبخیر کی شرح پر اثر انداز عوامل', '9.2.2 د ټرانسپایرېشن پر کچه اغېزمن عوامل')
    s.p('The rate of transpiration depends on many factors. Some of the important factors and their effects are as follows:', 'عملِ تبخیر کی شرح کئی عوامل پر منحصر ہے۔ چند اہم عوامل اور ان کے اثرات درج ذیل ہیں:', 'د ټرانسپایرېشن کچه په ډېرو عواملو پورې اړه لري. ځینې مهم عوامل او اغېزې یې دا دي:')
    s.lines([
        ('i. Light: Light directly controls the opening and closing of stomata. In strong light, stomata are open and the rate of transpiration become high. In low light and darkness, stomata get closed and transpiration stops.', 'i. روشنی: روشنی براہِ راست اسٹومیٹا کے کھلنے اور بند ہونے کو کنٹرول کرتی ہے۔ تیز روشنی میں اسٹومیٹا کھلے ہوتے ہیں اور عملِ تبخیر کی شرح زیادہ ہو جاتی ہے۔ کم روشنی اور اندھیرے میں اسٹومیٹا بند ہو جاتے ہیں اور عملِ تبخیر رک جاتا ہے۔', 'i. رڼا: رڼا مستقیم د سټوماټا خلاصېدل او تړل کېدل کنټرولوي. په تېزه رڼا کې سټوماټا خلاص وي او د ټرانسپایرېشن کچه لوړېږي. په کمه رڼا او تیاره کې سټوماټا تړل کېږي او ټرانسپایرېشن درېږي.'),
        ('ii. Temperature: With a rise in temperature, water evaporates more rapidly. So transpiration rate increases. At lower temperature, the rate of transpiration is low.', 'ii. درجۂ حرارت: درجۂ حرارت بڑھنے سے پانی زیادہ تیزی سے بخارات بنتا ہے۔ اس لیے عملِ تبخیر کی شرح بڑھ جاتی ہے۔ کم درجۂ حرارت پر عملِ تبخیر کی شرح کم ہوتی ہے۔', 'ii. تودوخه: د تودوخې په لوړېدو اوبه ژر تبخیرېږي. نو د ټرانسپایرېشن کچه زیاتېږي. په ټیټه تودوخه کې د ټرانسپایرېشن کچه ټیټه وي.'),
        ('iii. Humidity: Presence of water vapours in air is called humidity. In low humidity, there are less water vapours in the atmosphere. So the rate of the loss of water vapours from leaf is high. When there is higher humidity in atmosphere, the rate of transpiration becomes low.', 'iii. نمی: ہوا میں آبی بخارات کی موجودگی کو نمی کہتے ہیں۔ کم نمی میں فضا میں آبی بخارات کم ہوتے ہیں۔ اس لیے پتے سے آبی بخارات کے ضیاع کی شرح زیادہ ہوتی ہے۔ جب فضا میں نمی زیادہ ہو تو عملِ تبخیر کی شرح کم ہو جاتی ہے۔', 'iii. رطوبت: په هوا کې د بخاراتو شتون ته رطوبت ویل کېږي. په ټیټ رطوبت کې په اتموسفیر کې لږ بخارات وي. نو له پاڼې د بخاراتو د ضایع کېدو کچه لوړه وي. کله چې په اتموسفیر کې رطوبت لوړ وي، د ټرانسپایرېشن کچه ټیټېږي.'),
        ('iv. Soil Moisture: If more water is present in the soil, more absorption will take place through the roots and rate of transpiration will increase.', 'iv. مٹی کی نمی: اگر مٹی میں زیادہ پانی ہو تو جڑوں سے زیادہ جذب ہوگا اور عملِ تبخیر کی شرح بڑھ جائے گی۔', 'iv. د خاورې لندبل: که په خاوره کې ډېرې اوبه وي، د ریښو له لارې ډېر جذب کېږي او د ټرانسپایرېشن کچه زیاتېږي.'),
        ('v. Wind: Air in motion is called wind. If the air is not moving, the water molecules transpiring out of stomata remain in the surrounding air which becomes humid. It stops further water molecule to come out and the rate of transpiration is reduced. If air is moving, the transpired water is rapidly removed from the leaf surroundings and there is space for more water vapours to come out of stomata. This increases the rate of transpiration.', 'v. ہوا: حرکت کرتی ہوا کو ہوا (ونڈ) کہتے ہیں۔ اگر ہوا حرکت نہ کر رہی ہو تو اسٹومیٹا سے نکلنے والے پانی کے مالیکیولز اردگرد کی ہوا میں رہتے ہیں جو نم ہو جاتی ہے۔ یہ مزید پانی کے مالیکیولز کو نکلنے سے روکتی ہے اور عملِ تبخیر کی شرح کم ہو جاتی ہے۔ اگر ہوا چل رہی ہو تو خارج شدہ پانی پتے کے اردگرد سے تیزی سے ہٹ جاتا ہے اور اسٹومیٹا سے مزید آبی بخارات نکلنے کی گنجائش بنتی ہے۔ اس سے عملِ تبخیر کی شرح بڑھتی ہے۔', 'v. باد: په حرکت کې هوا ته باد ویل کېږي. که هوا حرکت نه کوي، له سټوماټا وتلي د اوبو مالیکولونه په شاوخوا هوا کې پاتې کېږي چې لنده کېږي. دا د نورو مالیکولونو د وتلو مخه نیسي او د ټرانسپایرېشن کچه کمېږي. که هوا په حرکت کې وي، وتلې اوبه د پاڼې له شاوخوا ژر لرې کېږي او له سټوماټا د نورو بخاراتو د وتلو ځای جوړېږي. دا د ټرانسپایرېشن کچه زیاتوي.'),
        ('vi. Number and Distribution of Stomata: Leaves with more surface area have more stomata than the leaves with narrow blades. The greater the number of stomata on a leaf, the higher would be the transpiration rate. In most land plants, the number of stomata is greater on the lower leaf surface than on the upper surface. Therefore, more transpiration occurs from the lower surface', 'vi. اسٹومیٹا کی تعداد اور تقسیم: زیادہ سطحی رقبے والے پتوں میں تنگ پتوں کی نسبت زیادہ اسٹومیٹا ہوتے ہیں۔ پتے پر جتنے زیادہ اسٹومیٹا ہوں گے، عملِ تبخیر کی شرح اتنی زیادہ ہوگی۔ زیادہ تر زمینی پودوں میں پتے کی نچلی سطح پر اوپری سطح کی نسبت زیادہ اسٹومیٹا ہوتے ہیں۔ اس لیے نچلی سطح سے زیادہ عملِ تبخیر ہوتا ہے', 'vi. د سټوماټا شمېر او وېش: ډېرې سطحې لرونکې پاڼې د نریو پاڼو په پرتله ډېر سټوماټا لري. په پاڼه چې څومره ډېر سټوماټا وي، د ټرانسپایرېشن کچه به هومره لوړه وي. په ډېرو ځمکنیو بوټو کې د پاڼې په ښکتنۍ سطحه د پورتنۍ په پرتله ډېر سټوماټا وي. نو له ښکتنۍ سطحې ډېر ټرانسپایرېشن کېږي'),
    ])
    s.h('9.2.3 Significance of Transpiration', '9.2.3 عملِ تبخیر کی اہمیت', '9.2.3 د ټرانسپایرېشن اهمیت')
    s.p('Transpiration is a vital process in the life of plants. It prevents the leaves from overheating and keeps them cool. Roots constantly absorb water. Transpiration helps the plant to get rid of excess water and salts. Transpiration from leaves creates a pulling force on the water in xylem tissues of stem and root. This pulling force causes the water to rise up in the xylem tissues.',
        'عملِ تبخیر پودوں کی زندگی میں ایک اہم عمل ہے۔ یہ پتوں کو زیادہ گرم ہونے سے بچاتا اور ٹھنڈا رکھتا ہے۔ جڑیں مسلسل پانی جذب کرتی ہیں۔ عملِ تبخیر پودے کو اضافی پانی اور نمکیات سے چھٹکارا پانے میں مدد دیتا ہے۔ پتوں سے عملِ تبخیر تنے اور جڑ کی زائلم بافتوں میں پانی پر کھنچاؤ کی قوت پیدا کرتا ہے۔ یہ کھنچاؤ کی قوت پانی کو زائلم بافتوں میں اوپر چڑھاتی ہے۔',
        'ټرانسپایرېشن د بوټو په ژوند کې حیاتي پروسه ده. پاڼې له ډېرې تودېدو ساتي او یخې یې ساتي. ریښې په دوامداره توګه اوبه جذبوي. ټرانسپایرېشن له بوټي سره د اضافي اوبو او مالګو په ایستلو کې مرسته کوي. له پاڼو ټرانسپایرېشن د ډډ او ریښې د زایلم نسجونو په اوبو کشوونکی ځواک جوړوي. دا کشوونکی ځواک اوبه په زایلم نسجونو کې پورته کوي.')
    s.callout(('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه'), [('The plant living in areas with adequate water content in the soil (due to irrigation or rainfall) have better nutrients uptake from the soil. They also have efficient transport of nutrients within the plant body. Write a short summary to explain the role of water in soil with respect to the distribution of nutrients in the plant.', 'جو پودے ایسے علاقوں میں رہتے ہیں جہاں مٹی میں (آبپاشی یا بارش کی وجہ سے) مناسب پانی ہو، وہ مٹی سے بہتر غذائی اجزا لیتے ہیں۔ ان کے جسم میں غذائی اجزا کی نقل و حمل بھی مؤثر ہوتی ہے۔ پودے میں غذائی اجزا کی تقسیم کے حوالے سے مٹی میں پانی کے کردار کی وضاحت کے لیے ایک مختصر خلاصہ لکھیں۔', 'هغه بوټي چې په داسې سیمو کې اوسېږي چې په خاوره کې (د اوبو لګولو یا باران له امله) کافي اوبه وي، له خاورې غذايي مواد ښه اخلي. د بوټي په بدن کې یې د غذايي موادو لېږد هم اغېزمن وي. په بوټي کې د غذايي موادو د وېش په اړه د خاورې د اوبو د رول د تشریح لپاره یو لنډ لنډیز ولیکئ.')])
    s.p('Due to transpiration, the mesophyll cells always remain moist. This helps in gaseous exchange especially the absorption of CO₂ which is essential for photosynthesis.', 'عملِ تبخیر کی وجہ سے میزوفل خلیے ہمیشہ نم رہتے ہیں۔ یہ گیسوں کے تبادلے، خاص طور پر CO₂ کے جذب میں مدد دیتا ہے جو ضیائی تالیف کے لیے ضروری ہے۔', 'د ټرانسپایرېشن له امله د میزوفیل حجرې تل لندې پاتې کېږي. دا د ګازونو په تبادله کې، په ځانګړي ډول د CO₂ په جذب کې چې د فوتوسنتز لپاره اړین دی، مرسته کوي.')
    s.p('Although transpiration plays an important role in the normal functioning of the plants, it may prove harmful when there is deficiency of water in the soil. In such conditions, transpiration may result in wilting. Transpiration is important for plants but excessive loss of water is harmful. Therefore, transpiration is considered as a necessary evil.',
        'اگرچہ عملِ تبخیر پودوں کے معمول کے کام میں اہم کردار ادا کرتا ہے، لیکن مٹی میں پانی کی کمی ہو تو یہ نقصان دہ ثابت ہو سکتا ہے۔ ایسے حالات میں عملِ تبخیر سے پودا مرجھا سکتا ہے۔ عملِ تبخیر پودوں کے لیے اہم ہے لیکن پانی کا حد سے زیادہ ضیاع نقصان دہ ہے۔ اس لیے عملِ تبخیر کو ایک ضروری برائی سمجھا جاتا ہے۔',
        'که څه هم ټرانسپایرېشن د بوټو په عادي دنده کې مهم رول لري، خو کله چې په خاوره کې د اوبو کمښت وي ښايي زیانمن ثابت شي. په داسې حالاتو کې ټرانسپایرېشن ښايي د مړاوي کېدو لامل شي. ټرانسپایرېشن د بوټو لپاره مهم دی خو د اوبو ډېر ضایع کېدل زیانمن دي. له همدې امله ټرانسپایرېشن یوه اړینه بدي ګڼل کېږي.')
    s.callout(SI, [('One of the terminology related to transpiration is "Evapotranspiration". It is defined as loss of water from the soil both by evaporation from the soil surface and by transpiration from the leaves of the plants growing on it. Factors that affect the rate of evapotranspiration include the amount of solar radiation, atmospheric vapor pressure, temperature, wind and soil moisture.', 'عملِ تبخیر سے متعلق ایک اصطلاح ”ایوا پو ٹرانسپائریشن“ ہے۔ اس کی تعریف مٹی سے پانی کا ضیاع ہے جو مٹی کی سطح سے تبخیر اور اس پر اگنے والے پودوں کے پتوں سے عملِ تبخیر دونوں سے ہوتا ہے۔ ایوا پو ٹرانسپائریشن کی شرح پر اثر انداز عوامل میں سورج کی شعاعوں کی مقدار، فضائی بخاراتی دباؤ، درجۂ حرارت، ہوا اور مٹی کی نمی شامل ہیں۔', 'له ټرانسپایرېشن سره تړلې یوه اصطلاح ”اېواپوټرانسپایرېشن“ ده. داسې تعریف کېږي: له خاورې د اوبو ضایع کېدل چې د خاورې له سطحې د تبخیر او پرې د راشنو بوټو له پاڼو د ټرانسپایرېشن دواړو له لارې کېږي. د اېواپوټرانسپایرېشن پر کچه اغېزمن عوامل د لمر د وړانګو اندازه، د اتموسفیر د بخار فشار، تودوخه، باد او د خاورې لندبل دي.')])
    out.append(s)

    s = Section('bio9_3', '9.3', 'Transportation of Water', 'پانی کی نقل و حمل', 'د اوبو لېږد', [188])
    s.h('9.3 Transportation of Water', '9.3 پانی کی نقل و حمل', '9.3 د اوبو لېږد')
    s.p('Transpiration of water from the leaves creates a pulling force in the leaves. This pulling force is called transpirational pull. The transpirational pull occurs when mesophyll cells of leaves lose water vapours, more water enters in them from the xylem vessels of the leaf. The xylem vessels and leaf are linked with the xylem vessels of stem and root. There is an unbroken column of water in xylem vessels. This unbroken water column is mainly due to three reasons; (i) the attractive forces among water molecules, (ii) narrow diameter of xylem vessels and (iii) the force by which water molecules are adhered to the walls of xylem vessels.',
        'پتوں سے پانی کا عملِ تبخیر پتوں میں کھنچاؤ کی قوت پیدا کرتا ہے۔ اس کھنچاؤ کی قوت کو ٹرانسپائریشنل پُل کہتے ہیں۔ ٹرانسپائریشنل پُل اس وقت پیدا ہوتا ہے جب پتوں کے میزوفل خلیے آبی بخارات کھوتے ہیں تو پتے کی زائلم نالیوں سے مزید پانی ان میں داخل ہوتا ہے۔ پتے کی زائلم نالیاں تنے اور جڑ کی زائلم نالیوں سے جڑی ہیں۔ زائلم نالیوں میں پانی کا ایک ناقابلِ انقطاع ستون ہوتا ہے۔ یہ مسلسل ستون بنیادی طور پر تین وجوہات سے ہے؛ (i) پانی کے مالیکیولز کے درمیان کشش کی قوتیں، (ii) زائلم نالیوں کا تنگ قطر اور (iii) وہ قوت جس سے پانی کے مالیکیولز زائلم نالیوں کی دیواروں سے چپکے رہتے ہیں۔',
        'له پاڼو د اوبو ټرانسپایرېشن په پاڼو کې کشوونکی ځواک جوړوي. دې ځواک ته ټرانسپایرېشنل کشش ویل کېږي. ټرانسپایرېشنل کشش هغه وخت رامنځته کېږي چې د پاڼو د میزوفیل حجرې بخارات له لاسه ورکړي، نو د پاڼې له زایلم رګونو نورې اوبه ورته ننوځي. د پاڼې زایلم رګونه د ډډ او ریښې له زایلم رګونو سره تړلي دي. په زایلم رګونو کې د اوبو یوه نه شلېدونکې ستنه وي. دا پرله پسې ستنه په اصل کې د درېیو لاملونو له امله ده؛ (i) د اوبو د مالیکولونو ترمنځ جذب ځواکونه، (ii) د زایلم رګونو نری قطر او (iii) هغه ځواک چې د اوبو مالیکولونه پرې د زایلم رګونو په دېوالونو نښتي وي.')
    en, ur, ps = tri(water_fig, WATER)
    s.fig('bio9-fig9-4', en, ur, ps, .5, caption=('Figure 9.4: Transport of water in plants', 'شکل 9.4: پودوں میں پانی کی نقل و حمل', 'شکل 9.4: په بوټو کې د اوبو لېږد'))
    out.append(s)
    return out
