# -*- coding: utf-8 -*-
"""Unit 4 part E — PDF 88-97 (printed 85-94): turgor, plasmolysis, active transport, endo/exocytosis, filtration, 4.7-4.8 tissues."""
import math
from bio9_tools import Section, svg_wrap, txt
from unit4_figs import multiline
from unit4_figs2 import pointer

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')


def three(fn, en, ur, ps):
    return fn(en), fn(ur), fn(ps)


def membrane_band(y, x0=20, x1=460, gap=None):
    out = []
    for row, flip in ((y, 1), (y + 90, -1)):
        for i in range(int((x1 - x0) / 14)):
            x = x0 + 7 + i * 14
            if gap and gap[0] < x < gap[1]:
                continue
            out.append(f'<circle cx="{x}" cy="{row}" r="7" fill="#e53935"/>')
    return ''.join(out)


def active_fig(L):
    b = ['<rect x="20" y="100" width="420" height="90" fill="#fff8e1"/>', membrane_band(100, gap=(190, 260))]
    b.append('<path d="M195,85 q-15,70 5,125 h25 q8,-70 -5,-125 z M230,85 q15,70 -5,125 h25 q15,-60 0,-125 z" fill="#fff176" stroke="#f9a825"/>')
    b.append(''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="#b3e5fc" stroke="#0288d1"/>' + txt(x, y + 4, 'Na⁺', 8, 'middle') for x, y in [(160, 30), (190, 50), (230, 25), (270, 45), (300, 30), (330, 60), (215, 70)]))
    b.append(''.join(txt(x, y, 'K⁺', 10, 'middle', 'bold') for x, y in [(250, 75), (280, 80), (110, 225), (140, 245), (170, 230)]))
    b.append(''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="#b3e5fc" stroke="#0288d1"/>' + txt(x, y + 4, 'Na⁺', 8, 'middle') for x, y in [(300, 230), (330, 250)]))
    b.append('<rect x="190" y="180" width="30" height="16" fill="#ffca28"/>' + txt(205, 192, 'ATP', 10, 'middle', 'bold') + '<rect x="235" y="180" width="30" height="16" fill="#ffca28"/>' + txt(250, 192, 'ATP', 10, 'middle', 'bold'))
    b.append(multiline(60, 60, L['outside']) + multiline(60, 215, L['inside']) + pointer(260, 110, 450, 110, L['carrier']))
    return svg_wrap(''.join(b), 540, 265, L['title'])


AT_EN = dict(title='Figure 4.22 Active transport of Na⁺ and K⁺ across cell membrane of Nerve cells', outside=['Outside', 'of Cell'], inside=['Inside', 'of Cell'], carrier=['Carrier', 'protein'])
AT_UR = dict(title='شکل 4.22', outside=['خلیے کا', 'بیرونی حصہ'], inside=['خلیے کا', 'اندرونی حصہ'], carrier=['کیریئر', 'پروٹین'])
AT_PS = dict(title='شکل 4.22', outside=['د حجرې', 'بهر'], inside=['د حجرې', 'دننه'], carrier=['لېږدوونکی', 'پروټین'])


def endo_exo(L):
    b = []
    for row, (y, label, rev) in enumerate([(20, L['endo'], False), (170, L['exo'], True)]):
        b.append(f'<rect x="40" y="{y}" width="380" height="110" fill="#fffde7" stroke="#bdbdbd"/>')
        b.append(f'<path d="M40,{y+35} h380" stroke="#ffcc80" stroke-width="6"/>')
        steps = [0, 1, 2, 3]
        for i, k in enumerate(steps):
            stage = (3 - k) if rev else k
            x = 85 + i * 95
            cy = y + 35 + stage * 14
            if stage == 0:
                b.append(f'<path d="M{x-22},{y+35} a22,22 0 0,0 44,0" fill="#ffe0b2" stroke="#ff9800" stroke-width="3"/>')
            else:
                b.append(f'<circle cx="{x}" cy="{cy}" r="20" fill="#ffe0b2" stroke="#ff9800" stroke-width="3"/><circle cx="{x}" cy="{cy}" r="11" fill="#5c6bc0"/>')
            if i < 3:
                b.append(f'<path d="M{x+28},{y+70} h35" stroke="#c62828" stroke-width="2"/><polygon points="{x+63},{y+66} {x+70},{y+70} {x+63},{y+74}" fill="#c62828"/>')
        b.append(txt(230, y + 128, label, 12, 'middle', 'bold'))
    b.append(pointer(420, 30, 440, 30, L['extra']) + pointer(420, 55, 440, 70, L['cyto']) + pointer(420, 100, 440, 110, L['intra']))
    return svg_wrap(''.join(b), 560, 320, L['title'])


EE_EN = dict(title='Figure 4.23 Endocytosis and Exocytosis', endo='(a) Endocytosis', exo='(b) Exocytosis', extra=['Extracellular', 'environment'], cyto='Cytoplasm', intra=['intracellular', 'environment'])
EE_UR = dict(title='شکل 4.23', endo='(a) اینڈوسائٹوسس', exo='(b) ایگزوسائٹوسس', extra=['بیرونی خلوی', 'ماحول'], cyto='سائٹوپلازم', intra=['اندرونی خلوی', 'ماحول'])
EE_PS = dict(title='شکل 4.23', endo='(a) انډوسایټوزس', exo='(b) اګزوسایټوزس', extra=['د حجرې بهرنی', 'چاپېریال'], cyto='سایټوپلازم', intra=['د حجرې دننه', 'چاپېریال'])


def filtration(L):
    b = ['<path d="M40,110 Q240,95 460,105 L460,175 Q240,185 40,170 Z" fill="#ffccbc" stroke="#d84315"/>']
    b.append(''.join(f'<circle cx="{60 + (i*37)%400}" cy="{120 + (i*13)%50}" r="5" fill="#fff59d"/>' for i in range(22)))
    b.append(''.join(f'<circle cx="{120 + (i*29)%330}" cy="{40 + (i*17)%50}" r="2" fill="#43a047"/>' for i in range(60)))
    b.append(''.join(f'<circle cx="{120 + (i*31)%330}" cy="{205 + (i*11)%45}" r="2" fill="#43a047"/>' for i in range(60)))
    for x in (150, 220, 290, 360):
        b.append(f'<path d="M{x},110 q20,-25 50,-30" stroke="#29b6f6" stroke-width="5" fill="none"/><path d="M{x},175 q20,25 50,30" stroke="#29b6f6" stroke-width="5" fill="none"/>')
    b.append(txt(90, 140, L['bp1'], 15) + txt(90, 160, L['bp2'], 15))
    b.append(pointer(130, 45, 100, 30, L['small'], 'end') + pointer(440, 125, 455, 70, L['large']) + pointer(80, 172, 70, 225, L['membrane']))
    return svg_wrap(''.join(b), 560, 265, L['title'])


FI_EN = dict(title='Figure 4.24: Filtration through the cell membrane of capillary wall', bp1='Blood', bp2='pressure', small='Small molecules', large=['Large', 'molecules'], membrane=['Membrane of', 'Capillary wall cells'])
FI_UR = dict(title='شکل 4.24', bp1='بلڈ', bp2='پریشر', small='چھوٹے مالیکیول', large=['بڑے', 'مالیکیول'], membrane=['شعری دیوار کے', 'خلیوں کی جھلی'])
FI_PS = dict(title='شکل 4.24', bp1='د وینې', bp2='فشار', small='کوچني مالیکولونه', large=['لوی', 'مالیکولونه'], membrane=['د شعریه دېوال', 'د حجرو غشا'])


def meristem(L):
    b = ['<path d="M150,30 L150,300" stroke="#00897b" stroke-width="14"/>',
         '<path d="M150,90 q60,-40 110,0 q-50,40 -110,0 z M150,140 q-70,-35 -110,10 q60,25 110,-10 z M150,230 q-70,-30 -110,10 q60,25 110,-10 z" fill="#26a69a"/>',
         '<path d="M150,300 q-30,20 -50,50 M150,300 q30,20 50,45 M150,300 v55 M130,320 l-25,15 M170,320 l25,12" stroke="#00897b" stroke-width="6" fill="none"/>',
         '<circle cx="150" cy="32" r="6" fill="#004d40"/>', '<rect x="285" y="175" width="18" height="26" rx="6" fill="#26a69a"/><path d="M245,188 h30" stroke="#039be5" stroke-width="4"/><polygon points="275,182 285,188 275,194" fill="#039be5"/>']
    b.append(pointer(156, 32, 200, 30, L['shoot']) + multiline(205, 160, L['lateral']) + pointer(195, 345, 260, 300, L['root']))
    return svg_wrap(''.join(b), 360, 370, L['title'])


ME_EN = dict(title='Figure 4.25: Apical and lateral meristem', shoot=['Shoot', 'apical meristem'], lateral=['Lateral', 'meristem'], root=['Root', 'apical meristem'])
ME_UR = dict(title='شکل 4.25', shoot=['تنے کا', 'ایپیکل میرسٹیم'], lateral=['لیٹرل', 'میرسٹیم'], root=['جڑ کا', 'ایپیکل میرسٹیم'])
ME_PS = dict(title='شکل 4.25', shoot=['د ډډ', 'سرنی میرسټیم'], lateral=['اړخیز', 'میرسټیم'], root=['د ریښې', 'سرنی میرسټیم'])


def simple_tissues(L):
    b = []
    # epidermal: flattened tight cells
    b.append(''.join(f'<rect x="{20 + (i%5)*36}" y="{20 + (i//5)*20}" width="34" height="18" fill="#c8e6c9" stroke="#1b5e20"/>' for i in range(10)))
    # parenchyma: round thin cells with spaces
    b.append(''.join(f'<circle cx="{260 + (i%4)*34}" cy="{30 + (i//4)*32}" r="15" fill="#f1f8e9" stroke="#33691e"/>' for i in range(8)))
    # collenchyma: polygons with thick corners
    b.append(''.join(f'<rect x="{30 + (i%4)*42}" y="{120 + (i//4)*38}" width="38" height="34" rx="8" fill="#fffde7" stroke="#827717" stroke-width="5"/>' for i in range(8)))
    # sclerenchyma: very thick walls small lumen
    b.append(''.join(f'<circle cx="{270 + (i%4)*34}" cy="{140 + (i//4)*34}" r="16" fill="#8d6e63" stroke="#4e342e"/><circle cx="{270 + (i%4)*34}" cy="{140 + (i//4)*34}" r="4" fill="#fff"/>' for i in range(8)))
    b.append(txt(110, 75, L['epi'], 12, 'middle', 'bold') + txt(310, 110, L['par'], 12, 'middle', 'bold') + txt(110, 210, L['col'], 12, 'middle', 'bold') + txt(320, 210, L['scl'], 12, 'middle', 'bold'))
    return svg_wrap(''.join(b), 420, 220, L['title'])


ST_EN = dict(title='Figure 4.26: Plant Simple Tissues', epi='Epidermal cells', par='Parenchyma', col='Collenchyma', scl='Sclerenchyma')
ST_UR = dict(title='شکل 4.26', epi='اپی ڈرمل خلیات', par='پیرنکائما', col='کولنکائما', scl='اسکلیرنکائما')
ST_PS = dict(title='شکل 4.26', epi='اپیډرمي حجرې', par='پارینکایما', col='کولینکایما', scl='سکلیرینکایما')


def compound_tissues(L):
    b = ['<rect x="10" y="10" width="220" height="330" fill="none" stroke="#90a4ae"/><rect x="230" y="10" width="200" height="330" fill="none" stroke="#90a4ae"/>']
    b.append(txt(120, 28, L['xylem'], 13, 'middle', 'bold') + txt(330, 28, L['phloem'], 13, 'middle', 'bold'))
    b.append('<rect x="35" y="90" width="45" height="170" rx="6" fill="#e0f2f1" stroke="#00796b" stroke-width="2"/><path d="M35,175 h45" stroke="#00796b"/>')
    b.append(''.join(f'<circle cx="{42 + (i%4)*10}" cy="{100 + (i//4)*12}" r="1.6" fill="#004d40"/>' for i in range(52)))
    b.append('<path d="M37,95 l40,-6 M37,103 l40,-6 M37,111 l40,-6" stroke="#004d40" stroke-width="2"/>')
    b.append('<path d="M130,60 L145,310 L160,60 Z" fill="#b2dfdb" stroke="#00796b"/><path d="M180,50 L188,320 L196,50 Z" fill="#4db6ac" stroke="#004d40"/>')
    b.append('<rect x="270" y="70" width="45" height="230" rx="8" fill="#80cbc4" stroke="#00695c" stroke-width="2"/><path d="M270,185 h45" stroke="#00695c" stroke-width="3"/>')
    b.append('<rect x="262" y="80" width="10" height="210" rx="4" fill="#fff59d"/>' + ''.join(f'<circle cx="{280 + (i%3)*12}" cy="{90 + (i//3)*16}" r="2.5" fill="#004d40"/>' for i in range(39)))
    b.append('<path d="M390,40 L398,330 L406,40 Z" fill="#4db6ac" stroke="#004d40"/>')
    b.append(pointer(45, 98, 30, 45, L['perf'], 'start') + pointer(140, 110, 120, 88, L['trach'], 'end') + pointer(188, 70, 200, 45, L['fibre']) + pointer(80, 230, 95, 245, L['vessel']))
    b.append(pointer(267, 270, 240, 318, L['comp'], 'start') + pointer(292, 72, 300, 45, L['plate'], 'start') + pointer(305, 150, 330, 160, L['area']) + pointer(315, 280, 340, 300, L['element'], 'start') + pointer(398, 50, 410, 45, L['fibre']))
    return svg_wrap(''.join(b), 470, 350, L['title'])


CT_EN = dict(title='Figure 4.27: Plant Compound Tissues (xylem and phloem)', xylem='XYLEM', phloem='PHLOEM', perf=['Perforation', 'plates'], trach='Tracheids', fibre='Fibre',
             vessel=['Vessel', 'member'], comp=['Companion', 'cell'], plate=['Sieve', 'plate'], area=['Sieve', 'area'], element='Sieve element')
CT_UR = dict(title='شکل 4.27', xylem='زائلم', phloem='فلوئم', perf=['سوراخ دار', 'پلیٹیں'], trach='ٹریکیڈز', fibre='فائبر', vessel=['ویسل', 'ممبر'], comp=['کمپینین', 'سیل'],
             plate=['سیو', 'پلیٹ'], area=['سیو', 'ایریا'], element='سیو ایلیمنٹ')
CT_PS = dict(title='شکل 4.27', xylem='زایلم', phloem='فلویم', perf=['سوري لرونکې', 'پلېټې'], trach='ټراکیډونه', fibre='فایبر', vessel=['د رګ', 'غړی'], comp=['ملګرې', 'حجره'],
             plate=['چاڼ', 'پلېټ'], area=['چاڼ', 'ساحه'], element='چاڼ عنصر')


def animal_tissues(L):
    b = ['<path d="M240,40 a28,28 0 1,1 0.1,0 M205,95 h70 l40,140 h-20 l-30,-90 v190 h-25 v-110 h-10 v110 h-25 v-190 l-30,90 h-20 z" fill="#f8bbd0"/>']
    spots = [('cart', 170, 60, 210, 120), ('conn', 320, 60, 270, 130), ('adip', 70, 120, 220, 180), ('musc', 420, 130, 270, 190),
             ('nerv', 70, 230, 210, 230), ('epit', 420, 240, 265, 245), ('bone', 150, 330, 225, 320), ('blood', 340, 330, 255, 330)]
    fills = dict(cart='#bbdefb', conn='#fce4ec', adip='#f8bbd0', musc='#f48fb1', nerv='#ce93d8', epit='#f8bbd0', bone='#efebe9', blood='#ef9a9a')
    for key, cx, cy, tx, ty in spots:
        b.append(f'<path d="M{cx},{cy} L{tx},{ty}" stroke="#333"/><circle cx="{cx}" cy="{cy}" r="38" fill="{fills[key]}" stroke="#222" stroke-width="2"/>')
        b.append(txt(cx, cy + 54, L[key], 11, 'middle', 'bold'))
    return svg_wrap(''.join(b), 490, 395, L['title'])


AN_EN = dict(title='Figure 4.28: Animal Tissues', cart='Cartilage tissue', conn='Connective tissue', adip='Adipose tissue', musc='Muscle tissue', nerv='Nervous tissue', epit='Epithelial tissue', bone='Bone tissue', blood='Blood')
AN_UR = dict(title='شکل 4.28', cart='کارٹلیج بافت', conn='کنیکٹیو بافت', adip='ایڈیپوز بافت', musc='عضلاتی بافت', nerv='اعصابی بافت', epit='اپی تھیلیل بافت', bone='ہڈی کی بافت', blood='خون')
AN_PS = dict(title='شکل 4.28', cart='د کرکړې نسج', conn='نښلوونکی نسج', adip='د غوړ نسج', musc='عضلي نسج', nerv='عصبي نسج', epit='اپیتیلیل نسج', bone='د هډوکي نسج', blood='وینه')


def extend_4_6(s):
    s.pdf_pages += [89, 90, 91]
    s.callout(SI, [('When a plant cell loses water, its turgidity is lost and it becomes flaccid (soft and limp). The leaves with flaccid cells become limp and the stem droops. Thus plant cells with reduced turgor are said to be wilting.',
                    'جب پودے کا خلیہ پانی کھو دیتا ہے تو اس کا تناؤ ختم ہو جاتا ہے اور وہ ڈھیلا (نرم اور ڈھیلا ڈھالا) ہو جاتا ہے۔ ڈھیلے خلیوں والے پتے ڈھلک جاتے ہیں اور تنا جھک جاتا ہے۔ چنانچہ کم ٹرگر والے پودوں کے خلیوں کو مرجھاتے ہوئے کہا جاتا ہے۔',
                    'کله چې د بوټي حجره اوبه له لاسه ورکړي، ټینګوالی یې له منځه ځي او سسته (نرمه او ځوړنده) کېږي. د سستو حجرو پاڼې ځوړندې کېږي او ډډ ټیټېږي. نو د کم ټورګر بوټو حجرو ته وړمېدونکې ویل کېږي.')])
    s.h('Turgor', 'ٹرگر', 'ټورګر')
    s.p('We know that when a plant cell is surrounded by water or hypotonic solution, the water moves into the cell vacuole by osmosis. The vacuole increases in size and pushes the cell contents against the cell wall. This pressure which is exerted by the cytoplasm against the cell wall is known as turgor pressure and the phenomenon is called turgor. In turgid condition, the plant cell does not burst because the cell wall is strong and relatively inelastic. The importance of turgor in plants are as follows:',
        'ہم جانتے ہیں کہ جب پودے کا خلیہ پانی یا ہائپوٹونک محلول سے گھرا ہو تو پانی اوسموسس کے ذریعے خلیے کے ویکیول میں داخل ہوتا ہے۔ ویکیول کی جسامت بڑھتی ہے اور یہ خلیے کے اجزا کو خلوی دیوار کی طرف دباتا ہے۔ سائٹوپلازم کا خلوی دیوار پر ڈالا جانے والا یہ دباؤ ٹرگر پریشر اور یہ مظہر ٹرگر کہلاتا ہے۔ تنی ہوئی حالت میں پودے کا خلیہ نہیں پھٹتا کیونکہ خلوی دیوار مضبوط اور نسبتاً غیر لچکدار ہوتی ہے۔ پودوں میں ٹرگر کی اہمیت درج ذیل ہے:',
        'موږ پوهېږو چې کله د بوټي حجره په اوبو یا هایپوټونیک محلول را ګرځېدلې وي، اوبه د اوسموزس له لارې د حجرې واکیول ته ننوځي. واکیول لویېږي او د حجرې محتویات د حجرې دېوال ته ټېلوي. دې فشار ته چې سایټوپلازم یې پر دېوال اچوي د ټورګر فشار او دې پدیدې ته ټورګر ویل کېږي. په ټینګ حالت کې د بوټي حجره نه چاودېږي ځکه چې دېوال یې قوي او نسبتاً نه کشېدونکی دی. په بوټو کې د ټورګر اهمیت دا دی:')
    s.ol([('i) It plays an important role in maintaining the shape of the plant.', 'i) یہ پودے کی شکل برقرار رکھنے میں اہم کردار ادا کرتا ہے۔', 'i) دا د بوټي د بڼې په ساتلو کې مهم رول لري.'),
          ('ii) It provides supports to plants especially in young tissues.', 'ii) یہ پودوں کو خاص طور پر نوجوان بافتوں میں سہارا دیتا ہے۔', 'ii) دا بوټو ته په ځانګړي ډول په ځوانو نسجونو کې ملاتړ ورکوي.'),
          ('iii) It also helps in closing and opening of the stomata.', 'iii) یہ اسٹومیٹا کے کھلنے اور بند ہونے میں بھی مدد دیتا ہے۔', 'iii) دا د سټوماټا په خلاصېدو او تړل کېدو کې هم مرسته کوي.'),
          ('iv) Some flowers open during the day time and close at night. This is also due to change in turgor in the cells of sepals of flowers.', 'iv) بعض پھول دن کے وقت کھلتے اور رات کو بند ہو جاتے ہیں۔ یہ بھی پھولوں کے سیپلز کے خلیوں میں ٹرگر کی تبدیلی کی وجہ سے ہے۔', 'iv) ځینې ګلان د ورځې خلاصېږي او د شپې تړل کېږي. دا هم د ګلانو د سیپلونو په حجرو کې د ټورګر د بدلون له امله دی.')])
    s.h('Plasmolysis', 'پلازمولائسس', 'پلازمولیزس')
    s.p('We know that when a plant cell is surrounded by hypertonic solution, the water leaves the cell by osmosis. Water is lost first from the cytoplasm and then from the vacuole. Due to this outward movement of water, the cytoplasm shrinks and pulls away from the cell wall. This process is known as plasmolysis and the cell is said to be plasmolysed. When a plasmolysed cell is placed in a hypotonic solution, the cell restores its turgidity. The process is called deplasmolysis.',
        'ہم جانتے ہیں کہ جب پودے کا خلیہ ہائپرٹونک محلول سے گھرا ہو تو پانی اوسموسس کے ذریعے خلیے سے باہر نکلتا ہے۔ پانی پہلے سائٹوپلازم سے اور پھر ویکیول سے ضائع ہوتا ہے۔ پانی کی اس باہر کی طرف حرکت سے سائٹوپلازم سکڑ کر خلوی دیوار سے الگ ہو جاتا ہے۔ اس عمل کو پلازمولائسس کہتے ہیں اور خلیے کو پلازمولائزڈ کہا جاتا ہے۔ جب پلازمولائزڈ خلیے کو ہائپوٹونک محلول میں رکھا جائے تو خلیہ اپنا تناؤ بحال کر لیتا ہے۔ اس عمل کو ڈی پلازمولائسس کہتے ہیں۔',
        'موږ پوهېږو چې کله د بوټي حجره په هایپرټونیک محلول را ګرځېدلې وي، اوبه د اوسموزس له لارې حجره پرېږدي. اوبه لومړی له سایټوپلازم او بیا له واکیول ځي. د اوبو د دې بهر ته حرکت له امله سایټوپلازم راټولېږي او له دېوال جلا کېږي. دې پروسې ته پلازمولیزس ویل کېږي او حجره پلازمولایز شوې بلل کېږي. کله چې پلازمولایز شوې حجره په هایپوټونیک محلول کې کېښودل شي، حجره خپل ټینګوالی بېرته ترلاسه کوي. دې پروسې ته ډي پلازمولیزس ویل کېږي.')
    s.h('iv. Active Transport', 'iv. ایکٹیو ٹرانسپورٹ', 'iv. فعال لېږد')
    s.p('Sometimes, cell membrane helps to move the substances against concentration gradient i.e. from an area of lower concentration to the area of higher concentration. This uphill movement requires the expenditure of energy (ATP) and is called active transport. For the active transport of substances, carrier proteins present in cell membrane use energy and move them against the concentration gradient. Na⁺/K⁺ are actively transported across the membrane according to the requirement of the cell/body. For example, nerve impulse is carried when Na⁺ is actively transported across the membrane from nerve cell to outside.',
        'بعض اوقات خلوی جھلی مادوں کو ارتکاز کے فرق کے خلاف یعنی کم ارتکاز والے علاقے سے زیادہ ارتکاز والے علاقے کی طرف حرکت دینے میں مدد کرتی ہے۔ اس چڑھائی والی حرکت کے لیے توانائی (ATP) خرچ ہوتی ہے اور اسے ایکٹیو ٹرانسپورٹ کہتے ہیں۔ مادوں کی ایکٹیو ٹرانسپورٹ کے لیے خلوی جھلی میں موجود کیریئر پروٹینز توانائی استعمال کرتے ہیں اور انہیں ارتکاز کے فرق کے خلاف حرکت دیتے ہیں۔ Na⁺/K⁺ کو خلیے/جسم کی ضرورت کے مطابق جھلی کے آر پار فعال طور پر منتقل کیا جاتا ہے۔ مثال کے طور پر عصبی پیغام اس وقت منتقل ہوتا ہے جب Na⁺ کو اعصابی خلیے سے باہر کی طرف جھلی کے آر پار فعال طور پر منتقل کیا جاتا ہے۔',
        'کله کله د حجرې غشا د موادو په حرکت کې د غلظت د توپیر پر خلاف مرسته کوي یعنې له ټیټ غلظت سیمې څخه لوړ غلظت سیمې ته. دا لوړ ته حرکت انرژي (ATP) غواړي او فعال لېږد بلل کېږي. د موادو د فعال لېږد لپاره په غشا کې موجود لېږدوونکي پروټینونه انرژي کاروي او هغوی د غلظت د توپیر پر خلاف خوځوي. Na⁺/K⁺ د حجرې/بدن د اړتیا سره سم له غشا څخه په فعال ډول لېږدول کېږي. د بېلګې په توګه عصبي پیغام هغه وخت لېږدول کېږي کله چې Na⁺ له عصبي حجرې بهر ته د غشا له لارې په فعال ډول لېږدول شي.')
    s.fig('bio4-fig4-22', *three(active_fig, AT_EN, AT_UR, AT_PS), .6,
          caption=('Figure 4.22 Active transport of Na⁺ and K⁺ across cell membrane of Nerve cells', 'شکل 4.22 اعصابی خلیوں کی خلوی جھلی کے آر پار Na⁺ اور K⁺ کی ایکٹیو ٹرانسپورٹ', 'شکل 4.22 د عصبي حجرو د غشا له لارې د Na⁺ او K⁺ فعال لېږد'))
    s.h('v. Endocytosis and Exocytosis', 'v. اینڈوسائٹوسس اور ایگزوسائٹوسس', 'v. انډوسایټوزس او اګزوسایټوزس')
    s.p('Endocytosis is a general term for the process that brings macromolecules, large particles and even small cells into the cell. In endocytosis, the cell membrane invaginates (folds inward) and takes in the materials from the environment, forming a small pocket. The pocket deepens, forming a vesicle. This vesicle separates from the plasma membrane and migrates with its contents to the cell\'s interior.',
        'اینڈوسائٹوسس اس عمل کی عمومی اصطلاح ہے جو بڑے مالیکیولز، بڑے ذرات اور حتیٰ کہ چھوٹے خلیوں کو خلیے کے اندر لاتا ہے۔ اینڈوسائٹوسس میں خلوی جھلی اندر کی طرف مڑتی ہے اور ماحول سے مادے اندر لے کر ایک چھوٹی جیب بناتی ہے۔ جیب گہری ہو کر ایک ویسیکل بن جاتی ہے۔ یہ ویسیکل پلازما جھلی سے الگ ہو کر اپنے مواد سمیت خلیے کے اندر چلا جاتا ہے۔',
        'انډوسایټوزس د هغې پروسې عمومي اصطلاح ده چې لوی مالیکولونه، لویې ذرې او حتی کوچنۍ حجرې حجرې ته ننباسي. په انډوسایټوزس کې د حجرې غشا دننه خوا ته قاتېږي او له چاپېریال مواد اخلي او کوچنی جېب جوړوي. جېب ژورېږي او ویسیکل جوړوي. دا ویسیکل له پلازما غشا جلا کېږي او له خپلو محتویاتو سره د حجرې دننه ته ځي.')
    s.callout(SI, [('There are two forms of endocytosis i.e. phagocytosis (cellular eating) and pinocytosis (cellular drinking). In phagocytosis cell takes in solid material while in pinocytosis cell takes in liquid.',
                    'اینڈوسائٹوسس کی دو اقسام ہیں یعنی فیگوسائٹوسس (خلوی کھانا) اور پنوسائٹوسس (خلوی پینا)۔ فیگوسائٹوسس میں خلیہ ٹھوس مادہ اندر لیتا ہے جبکہ پنوسائٹوسس میں خلیہ مائع اندر لیتا ہے۔',
                    'انډوسایټوزس دوه ډوله دی یعنې فاګوسایټوزس (حجروي خوړل) او پینوسایټوزس (حجروي څښل). په فاګوسایټوزس کې حجره جامد مواد اخلي او په پینوسایټوزس کې مایع اخلي.')])
    s.p('Exocytosis is the process by which materials packaged in vesicles are excreted from a cell. The initial event in this process is the binding of vesicle membrane with the cell membrane. Then, the contents of the vesicle are released to the environment and the vesicle membrane is incorporated into cell membrane.',
        'ایگزوسائٹوسس وہ عمل ہے جس کے ذریعے ویسیکلز میں بند مادے خلیے سے خارج کیے جاتے ہیں۔ اس عمل کا پہلا واقعہ ویسیکل کی جھلی کا خلوی جھلی سے جڑنا ہے۔ پھر ویسیکل کا مواد ماحول میں خارج ہو جاتا ہے اور ویسیکل کی جھلی خلوی جھلی میں شامل ہو جاتی ہے۔',
        'اګزوسایټوزس هغه پروسه ده چې په ویسیکلونو کې بسته شوي مواد له حجرې بهر کېږي. د دې پروسې لومړۍ پېښه د ویسیکل د غشا له حجروي غشا سره نښلېدل دي. بیا د ویسیکل محتویات چاپېریال ته خوشې کېږي او د ویسیکل غشا په حجروي غشا کې شاملېږي.')
    s.fig('bio4-fig4-23', *three(endo_exo, EE_EN, EE_UR, EE_PS), .75,
          caption=('Figure 4.23 Endocytosis and Exocytosis', 'شکل 4.23 اینڈوسائٹوسس اور ایگزوسائٹوسس', 'شکل 4.23 انډوسایټوزس او اګزوسایټوزس'))
    s.callout(('Activities 4.4', 'سرگرمیاں 4.4', 'فعالیتونه 4.4'), [('• Perform an experiment to prove plasmolysis and deplasmolysis.', '• پلازمولائسس اور ڈی پلازمولائسس ثابت کرنے کے لیے ایک تجربہ کریں۔', '• د پلازمولیزس او ډي پلازمولیزس د ثابتولو لپاره یوه تجربه وکړئ.'),
                                                                   ('• Use models to explain diffusion and osmosis.', '• ڈفیوژن اور اوسموسس کی وضاحت کے لیے ماڈل استعمال کریں۔', '• د ډیفیوژن او اوسموزس د تشریح لپاره ماډلونه وکاروئ.')])
    s.h('vi. Filtration', 'vi. فلٹریشن', 'vi. فلټریشن')
    s.p('It is the process in which small molecules are pushed or forced across a selectively permeable membrane with the help of hydrostatic pressure or blood pressure. In our body filtration occurs in the kidneys and helps us filter out harmful waste materials.',
        'یہ وہ عمل ہے جس میں چھوٹے مالیکیولز کو ہائیڈروسٹیٹک پریشر یا بلڈ پریشر کی مدد سے منتخب نفوذ پذیر جھلی کے آر پار دھکیلا جاتا ہے۔ ہمارے جسم میں فلٹریشن گردوں میں ہوتی ہے اور نقصان دہ فضلات کو چھان کر نکالنے میں مدد دیتی ہے۔',
        'دا هغه پروسه ده چې کوچني مالیکولونه د هایډروسټاټیک فشار یا د وینې د فشار په مرسته له انتخابي نفوذ منونکې غشا څخه ټېل وهل کېږي. زموږ په بدن کې فلټریشن په پښتورګو کې کېږي او له موږ سره د زیانمنو فاضله موادو په چاڼولو کې مرسته کوي.')
    s.fig('bio4-fig4-24', *three(filtration, FI_EN, FI_UR, FI_PS), .7,
          caption=('Figure 4.24: Filtration through the cell membrane of capillary wall', 'شکل 4.24: شعری دیوار کی خلوی جھلی سے فلٹریشن', 'شکل 4.24: د شعریه دېوال د حجرې له غشا فلټریشن'))


def sections():
    out = []
    s = Section('bio4_7', '4.7', 'Tissues', 'بافتیں', 'نسجونه', [91, 92, 93, 94, 95])
    s.p('All plants and animals have tissues. Tissue is a group of cells which perform a common function. All cells of the tissues are dependent on each other. However, there are organisms where cells group together but they do not form tissues. This is because the cells are not dependent but function independently. Volvox is a common example of such organization (recall from Unit-1). In Volvox, many cells combine together forming a colony but they do not form tissues. Other examples of such organizations are bacteria, slime molds etc.',
        'تمام پودوں اور جانوروں میں بافتیں ہوتی ہیں۔ بافت خلیوں کا ایک گروہ ہے جو ایک مشترک کام انجام دیتا ہے۔ بافتوں کے تمام خلیے ایک دوسرے پر منحصر ہوتے ہیں۔ تاہم ایسے جاندار بھی ہیں جن میں خلیے اکٹھے ہوتے ہیں لیکن بافتیں نہیں بناتے۔ اس کی وجہ یہ ہے کہ خلیے منحصر نہیں بلکہ آزادانہ کام کرتے ہیں۔ والوکس اس قسم کی تنظیم کی ایک عام مثال ہے (یونٹ 1 یاد کریں)۔ والوکس میں بہت سے خلیے مل کر کالونی بناتے ہیں لیکن بافتیں نہیں بناتے۔ ایسی تنظیم کی دوسری مثالیں بیکٹیریا، سلائم مولڈز وغیرہ ہیں۔',
        'ټول بوټي او ژوي نسجونه لري. نسج د حجرو هغه ډله ده چې یوه ګډه دنده ترسره کوي. د نسجونو ټولې حجرې یو پر بل متکي دي. خو داسې موجودات هم شته چې حجرې یې سره یوځای کېږي خو نسجونه نه جوړوي. دا ځکه چې حجرې متکي نه دي بلکې په خپلواکه توګه کار کوي. والواکس د داسې تنظیم عامه بېلګه ده (یونټ 1 رایاد کړئ). په والواکس کې ډېرې حجرې یوځای کېږي او کلوني جوړوي خو نسجونه نه جوړوي. د داسې تنظیم نورې بېلګې باکتریا، سلایم مولډونه او نور دي.')
    s.p('There are various types of tissues in plants and animals depending upon their functions or morphology.', 'پودوں اور جانوروں میں ان کے افعال یا بیرونی ساخت کے لحاظ سے بافتوں کی مختلف اقسام ہیں۔', 'په بوټو او ژویو کې د دندو یا مورفولوژي له مخې بېلابېل ډوله نسجونه شته.')
    s.h('4.7.1 Plant Tissues', '4.7.1 پودوں کی بافتیں', '4.7.1 د بوټو نسجونه')
    s.p('Plant tissues may be classified into two major groups i.e. simple tissues and compound tissues.', 'پودوں کی بافتوں کو دو بڑے گروہوں یعنی سادہ بافتوں اور مرکب بافتوں میں درجہ بند کیا جا سکتا ہے۔', 'د بوټو نسجونه په دوو لویو ډلو یعنې ساده نسجونو او مرکبو نسجونو ډلبندي کېدای شي.')
    s.h('A. Simple Tissues', 'A. سادہ بافتیں', 'A. ساده نسجونه')
    s.p('They are composed of only one type of cells. They are further classified into:', 'یہ صرف ایک قسم کے خلیوں سے بنی ہوتی ہیں۔ انہیں مزید درج ذیل میں تقسیم کیا جاتا ہے:', 'دا یوازې له یو ډول حجرو جوړ دي. بیا په لاندې ډلو وېشل کېږي:')
    s.lines([('a. Meristematic Tissues or Embryonic Tissues', 'a. میرسٹیمیٹک بافتیں یا جنینی بافتیں', 'a. میرسټیمي نسجونه یا جنیني نسجونه'), ('b. Permanent Tissues', 'b. مستقل بافتیں', 'b. دایمي نسجونه')])
    s.h('a. Meristematic Tissues or Embryonic Tissues', 'a. میرسٹیمیٹک بافتیں یا جنینی بافتیں', 'a. میرسټیمي نسجونه یا جنیني نسجونه')
    s.p('These are made up of those cells which have the ability to divide and produce new cells at the growing points of a plant. The cells of meristematic tissue have dense cytoplasm, a large central nucleus with small or no vacuoles. Cells are alike, with no intercellular spaces and have thin walls. These tissues are of two types:',
        'یہ ان خلیوں سے بنی ہوتی ہیں جو پودے کے بڑھنے کے مقامات پر تقسیم ہو کر نئے خلیے بنانے کی صلاحیت رکھتے ہیں۔ میرسٹیمیٹک بافت کے خلیوں میں گاڑھا سائٹوپلازم، ایک بڑا مرکزی مرکزہ اور چھوٹے یا کوئی ویکیول نہیں ہوتے۔ خلیے یکساں ہوتے ہیں، ان کے درمیان کوئی خلا نہیں ہوتا اور ان کی دیواریں پتلی ہوتی ہیں۔ یہ بافتیں دو اقسام کی ہیں:',
        'دا له هغو حجرو جوړ دي چې د بوټي د ودې په ځایونو کې د وېش او د نویو حجرو د جوړولو وړتیا لري. د میرسټیمي نسج حجرې ټینګ سایټوپلازم، لویه مرکزي هسته او کوچني یا هېڅ واکیولونه نه لري. حجرې یو شان وي، ترمنځ یې تشې نه وي او نري دېوالونه لري. دا نسجونه دوه ډوله دي:')
    s.ul([('Apical meristem is present at the apex of root and shoot. Here the cells of meristem divide and redivide and result in the elongation of stem and root. Such a growth is called primary growth.',
           'ایپیکل میرسٹیم جڑ اور تنے کی چوٹی پر ہوتا ہے۔ یہاں میرسٹیم کے خلیے بار بار تقسیم ہوتے ہیں جس سے تنا اور جڑ لمبے ہوتے ہیں۔ ایسی نشوونما کو پرائمری گروتھ کہتے ہیں۔',
           'سرنی میرسټیم د ریښې او ډډ په سر کې وي. دلته د میرسټیم حجرې بیا بیا وېشل کېږي او د ډډ او ریښې د اوږدېدو لامل کېږي. داسې ودې ته لومړنۍ وده ویل کېږي.'),
          ('Lateral meristem is present on the lateral sides of roots and shoot. Here, the cells divide and results in the increase of thickness of root and shoot. Such a growth is called secondary growth.',
           'لیٹرل میرسٹیم جڑوں اور تنے کے پہلوؤں پر ہوتا ہے۔ یہاں خلیے تقسیم ہو کر جڑ اور تنے کی موٹائی میں اضافہ کرتے ہیں۔ ایسی نشوونما کو سیکنڈری گروتھ کہتے ہیں۔',
           'اړخیز میرسټیم د ریښو او ډډ په اړخونو کې وي. دلته حجرې وېشل کېږي او د ریښې او ډډ د پنډوالي د زیاتېدو لامل کېږي. داسې ودې ته ثانوي وده ویل کېږي.')])
    s.fig('bio4-fig4-25', *three(meristem, ME_EN, ME_UR, ME_PS), .45, caption=('Figure 4.25: Apical and lateral meristem', 'شکل 4.25: ایپیکل اور لیٹرل میرسٹیم', 'شکل 4.25: سرنی او اړخیز میرسټیم'))
    s.h('b. Permanent Tissues', 'b. مستقل بافتیں', 'b. دایمي نسجونه')
    s.p('The cells of these tissues lack the ability to divide. They originate from the primary meristem. The permanent tissues consist of epidermal, ground, supporting or mechanical tissues.',
        'ان بافتوں کے خلیوں میں تقسیم ہونے کی صلاحیت نہیں ہوتی۔ یہ پرائمری میرسٹیم سے پیدا ہوتی ہیں۔ مستقل بافتیں اپی ڈرمل، گراؤنڈ، سہارا دینے والی یا میکینیکل بافتوں پر مشتمل ہیں۔',
        'د دې نسجونو حجرې د وېش وړتیا نه لري. له لومړني میرسټیم څخه پیدا کېږي. دایمي نسجونه اپیډرمي، ځمکني، ملاتړي یا میخانیکي نسجونه لري.')
    s.callout(SI, [('Plants have certain areas where meristematic tissues are present such as tips of root and shoot. These tips can be used for the proliferation of high quality plants through tissue culture especially where other vegetative methods fail to work.',
                    'پودوں میں بعض جگہیں ہیں جہاں میرسٹیمیٹک بافتیں ہوتی ہیں جیسے جڑ اور تنے کے سرے۔ ان سروں کو ٹشو کلچر کے ذریعے اعلیٰ معیار کے پودوں کی افزائش کے لیے استعمال کیا جا سکتا ہے خاص طور پر جہاں دوسرے نباتی طریقے کام نہ کریں۔',
                    'بوټي ځینې ځایونه لري چې میرسټیمي نسجونه پکې وي لکه د ریښې او ډډ سرونه. دا سرونه د نسج کلچر له لارې د لوړ کیفیت بوټو د تکثیر لپاره کارول کېدای شي په ځانګړي ډول چېرته چې نور نباتي میتودونه کار نه کوي.')])
    s.h('Epidermal Tissues', 'اپی ڈرمل بافتیں', 'اپیډرمي نسجونه')
    s.p('These tissues are present as outermost protective covering of leaf, stem and root. Cells of the epidermal tissues are flattened and irregular in shape. They are thick walled and are closely packed with no intercellular spaces. In stem, the walls of these cells are covered with waxy material which prevents loss of water. In leaves, the epidermal tissue has small guarded openings called stomata, for gaseous exchange.',
        'یہ بافتیں پتے، تنے اور جڑ کے بیرونی حفاظتی غلاف کے طور پر ہوتی ہیں۔ اپی ڈرمل بافتوں کے خلیے چپٹے اور بے قاعدہ شکل کے ہوتے ہیں۔ یہ موٹی دیوار والے اور قریب قریب جڑے ہوتے ہیں اور ان کے درمیان خلا نہیں ہوتا۔ تنے میں ان خلیوں کی دیواروں پر موم جیسا مادہ ہوتا ہے جو پانی کے ضیاع کو روکتا ہے۔ پتوں میں اپی ڈرمل بافت میں گیسوں کے تبادلے کے لیے چھوٹے محفوظ سوراخ ہوتے ہیں جنہیں اسٹومیٹا کہتے ہیں۔',
        'دا نسجونه د پاڼې، ډډ او ریښې د تر ټولو بهرني ساتونکي پوښ په توګه وي. د اپیډرمي نسجونو حجرې پلنې او بې قاعدې بڼه لري. پنډ دېوالونه لري او سره نږدې پرتې دي او ترمنځ یې تشې نشته. په ډډ کې د دې حجرو دېوالونه په مومي ماده پوښل شوي چې د اوبو د ضایع کېدو مخه نیسي. په پاڼو کې اپیډرمي نسج د ګازونو د تبادلې لپاره کوچني ساتل شوي سوري لري چې سټوماټا بلل کېږي.')
    s.callout(SI, [('The cells of root epidermal tissue also have extensions in the form of root hairs.', 'جڑ کی اپی ڈرمل بافت کے خلیوں میں جڑ کے بالوں کی شکل میں ابھار بھی ہوتے ہیں۔', 'د ریښې د اپیډرمي نسج حجرې د ریښې د وېښتانو په بڼه غځونې هم لري.')])
    s.h('Ground Tissues', 'گراؤنڈ بافتیں', 'ځمکني نسجونه')
    s.p('This tissue is present in all parts of the plant except the epidermal tissue and vascular tissue. It is composed of thin walled cells called parenchyma cells. These cells are oval, spherical or polygonal in shape. Their walls are thin. They store food. In leaves, the ground tissue contains chlorophyll and is called mesophyll tissue. It prepares food.',
        'یہ بافت اپی ڈرمل بافت اور ویسکولر بافت کے سوا پودے کے تمام حصوں میں ہوتی ہے۔ یہ پتلی دیوار والے خلیوں سے بنی ہوتی ہے جنہیں پیرنکائما خلیات کہتے ہیں۔ یہ خلیات بیضوی، کروی یا کثیر الاضلاع شکل کے ہوتے ہیں۔ ان کی دیواریں پتلی ہوتی ہیں۔ یہ خوراک ذخیرہ کرتے ہیں۔ پتوں میں گراؤنڈ بافت میں کلوروفل ہوتا ہے اور اسے میزوفل بافت کہتے ہیں۔ یہ خوراک تیار کرتی ہے۔',
        'دا نسج له اپیډرمي او رګي نسج پرته د بوټي په ټولو برخو کې وي. له نري دېوال لرونکو حجرو جوړ دی چې پارینکایما حجرې بلل کېږي. دا حجرې هګۍ ډوله، کروي یا څو ضلعي بڼه لري. دېوالونه یې نري دي. خواړه زېرمه کوي. په پاڼو کې ځمکنی نسج کلوروفیل لري او میزوفیل نسج بلل کېږي. خواړه جوړوي.')
    s.fig('bio4-fig4-26', *three(simple_tissues, ST_EN, ST_UR, ST_PS), .6, caption=('Figure 4.26: Plant Simple Tissues', 'شکل 4.26: پودوں کی سادہ بافتیں', 'شکل 4.26: د بوټو ساده نسجونه'))
    s.h('Supporting or Mechanical Tissues', 'سہارا دینے والی یا میکینیکل بافتیں', 'ملاتړي یا میخانیکي نسجونه')
    s.p('Plants need support to maintain their shape and remain stable. Supporting tissues provide strength and flexibility to the plant. These are of two types:',
        'پودوں کو اپنی شکل برقرار رکھنے اور مستحکم رہنے کے لیے سہارے کی ضرورت ہے۔ سہارا دینے والی بافتیں پودے کو مضبوطی اور لچک دیتی ہیں۔ یہ دو اقسام کی ہیں:',
        'بوټي د خپلې بڼې د ساتلو او ثابت پاتې کېدو لپاره ملاتړ ته اړتیا لري. ملاتړي نسجونه بوټي ته ټینګښت او انعطاف ورکوي. دا دوه ډوله دي:')
    s.lines([('a. Collenchyma tissues', 'a. کولنکائما بافتیں', 'a. کولینکایما نسجونه'), ('b. Sclerenchyma tissues', 'b. اسکلیرنکائما بافتیں', 'b. سکلیرینکایما نسجونه')])
    s.p('a. Collenchyma Tissue: It is found in young stems where it provides strength to different parts of the plant. The cells of this tissue are living, elongated and polygonal with tapering ends.',
        'a. کولنکائما بافت: یہ نوجوان تنوں میں پائی جاتی ہے جہاں یہ پودے کے مختلف حصوں کو مضبوطی دیتی ہے۔ اس بافت کے خلیے زندہ، لمبے اور کثیر الاضلاع ہوتے ہیں جن کے سرے نوکیلے ہوتے ہیں۔',
        'a. کولینکایما نسج: په ځوانو ډډونو کې موندل کېږي چې د بوټي بېلابېلو برخو ته ټینګښت ورکوي. د دې نسج حجرې ژوندۍ، اوږدې او څو ضلعي دي چې سرونه یې نري کېږي.')
    s.p('b. Sclerenchyma Tissue: These are thick walled dead cells. Walls of these cells are heavily filled with lignin which provides hardness and strength to the cell.',
        'b. اسکلیرنکائما بافت: یہ موٹی دیوار والے مردہ خلیے ہیں۔ ان خلیوں کی دیواریں لگنن سے بھری ہوتی ہیں جو خلیے کو سختی اور مضبوطی دیتا ہے۔',
        'b. سکلیرینکایما نسج: دا پنډ دېوال لرونکې مړې حجرې دي. د دې حجرو دېوالونه په لیګنین ډک وي چې حجرې ته کلکوالی او ټینګښت ورکوي.')
    s.h('B. Compound Tissues', 'B. مرکب بافتیں', 'B. مرکب نسجونه')
    s.p('These are the tissues which are composed of more than one type of cells performing a common function. Xylem and phloem tissues found in the vascular bundles are examples of compound tissues.',
        'یہ وہ بافتیں ہیں جو ایک سے زیادہ قسم کے خلیوں سے بنی ہوتی ہیں جو ایک مشترک کام انجام دیتے ہیں۔ ویسکولر بنڈلز میں پائی جانے والی زائلم اور فلوئم بافتیں مرکب بافتوں کی مثالیں ہیں۔',
        'دا هغه نسجونه دي چې له یو ډول ډېرو حجرو جوړ وي او ګډه دنده ترسره کوي. په رګي بنډلونو کې موندل کېدونکي زایلم او فلویم نسجونه د مرکبو نسجونو بېلګې دي.')
    s.p('a. Xylem Tissue: Xylem tissue consists of two types of cells i.e. vessels and tracheids. Vessel cells are short and wide and have thick secondary cell walls. These cells are dead and hollow and join together to form long tubes. Tracheids are long, slender cells with overlapping ends. Water moves upward from tracheid to tracheid.',
        'a. زائلم بافت: زائلم بافت دو قسم کے خلیوں یعنی ویسلز اور ٹریکیڈز پر مشتمل ہے۔ ویسل خلیے چھوٹے اور چوڑے ہوتے ہیں اور ان کی موٹی سیکنڈری خلوی دیواریں ہوتی ہیں۔ یہ خلیے مردہ اور کھوکھلے ہوتے ہیں اور آپس میں جڑ کر لمبی نلکیاں بناتے ہیں۔ ٹریکیڈز لمبے، پتلے خلیے ہیں جن کے سرے ایک دوسرے پر چڑھے ہوتے ہیں۔ پانی ایک ٹریکیڈ سے دوسرے میں اوپر کی طرف جاتا ہے۔',
        'a. زایلم نسج: زایلم نسج دوه ډوله حجرې لري یعنې رګونه او ټراکیډونه. د رګ حجرې لنډې او پلنې دي او پنډ ثانوي دېوالونه لري. دا حجرې مړې او تشې دي او سره یوځای کېږي اوږده نلونه جوړوي. ټراکیډونه اوږدې، نرۍ حجرې دي چې سرونه یې پر یو بل پراته وي. اوبه له یوه ټراکیډ بل ته پورته ځي.')
    s.p('Xylem tissue is responsible for the transport of water and dissolved substances from roots to the upper parts. Due to the presence of lignin in the secondary walls of its cells, xylem tissue also provides support to the plant body.',
        'زائلم بافت جڑوں سے اوپری حصوں تک پانی اور حل شدہ مادوں کی ترسیل کی ذمہ دار ہے۔ اس کے خلیوں کی سیکنڈری دیواروں میں لگنن کی موجودگی کی وجہ سے زائلم بافت پودے کے جسم کو سہارا بھی دیتی ہے۔',
        'زایلم نسج له ریښو پورتنیو برخو ته د اوبو او حل شویو موادو د لېږد مسؤل دی. د حجرو په ثانوي دېوالونو کې د لیګنین د شتون له امله زایلم نسج د بوټي بدن ته ملاتړ هم ورکوي.')
    s.p('b. Phloem Tissue: Phloem tissue consists of sieve tube cells and companion cells. In Sieve tube cells, protoplasm has no nucleus and the end walls have small pores called sieve plates. The transport of food occurs through the cytoplasm of the sieve tube cells. Companion cells accompany the sieve tube cells. They regulate the movement of food through sieve tubes.',
        'b. فلوئم بافت: فلوئم بافت سیو ٹیوب خلیوں اور کمپینین خلیوں پر مشتمل ہے۔ سیو ٹیوب خلیوں میں پروٹوپلازم میں مرکزہ نہیں ہوتا اور سرے کی دیواروں میں چھوٹے سوراخ ہوتے ہیں جنہیں سیو پلیٹس کہتے ہیں۔ خوراک کی ترسیل سیو ٹیوب خلیوں کے سائٹوپلازم کے ذریعے ہوتی ہے۔ کمپینین خلیے سیو ٹیوب خلیوں کے ساتھ ہوتے ہیں۔ یہ سیو ٹیوبز کے ذریعے خوراک کی حرکت کو منظم کرتے ہیں۔',
        'b. فلویم نسج: فلویم نسج د چاڼ نل حجرې او ملګرې حجرې لري. د چاڼ نل په حجرو کې پروټوپلازم هسته نه لري او د پای دېوالونه کوچني سوري لري چې د چاڼ پلېټونه بلل کېږي. د خوړو لېږد د چاڼ نل حجرو د سایټوپلازم له لارې کېږي. ملګرې حجرې د چاڼ نل حجرو سره وي. دوی د چاڼ نلونو له لارې د خوړو حرکت تنظیموي.')
    s.fig('bio4-fig4-27', *three(compound_tissues, CT_EN, CT_UR, CT_PS), .65, caption=('Figure 4.27: Plant Compound Tissues (xylem and phloem)', 'شکل 4.27: پودوں کی مرکب بافتیں (زائلم اور فلوئم)', 'شکل 4.27: د بوټو مرکب نسجونه (زایلم او فلویم)'))
    out.append(s)

    s = Section('bio4_8', '4.8', 'Animal Tissues', 'جانوروں کی بافتیں', 'د ژویو نسجونه', [95, 96, 97])
    s.p('Animal tissues are classified according to their structure and functions into four major types.', 'جانوروں کی بافتوں کو ان کی ساخت اور افعال کے لحاظ سے چار بڑی اقسام میں تقسیم کیا جاتا ہے۔', 'د ژویو نسجونه د جوړښت او دندو له مخې په څلورو لویو ډولونو ډلبندي کېږي.')
    s.ol([('i. Epithelial tissues', 'i. اپی تھیلیل بافتیں', 'i. اپیتیلیل نسجونه'), ('ii. Connective tissues', 'ii. کنیکٹیو بافتیں', 'ii. نښلوونکي نسجونه'),
          ('iii. Muscular tissues', 'iii. عضلاتی بافتیں', 'iii. عضلي نسجونه'), ('iv. Nervous tissues', 'iv. اعصابی بافتیں', 'iv. عصبي نسجونه')])
    s.h('i. Epithelial Tissues', 'i. اپی تھیلیل بافتیں', 'i. اپیتیلیل نسجونه')
    s.p('The interior of the body is physically separated from the outside world by the skin. The skin is made of epithelial tissue, which is in the form of continuous sheets of cells. Epithelial tissue also lines the gut, lungs and urinary tract. Structurally these cells are flattened and elongated.',
        'جسم کا اندرونی حصہ جلد کے ذریعے بیرونی دنیا سے جسمانی طور پر الگ ہوتا ہے۔ جلد اپی تھیلیل بافت سے بنی ہوتی ہے جو خلیوں کی مسلسل تہوں کی شکل میں ہوتی ہے۔ اپی تھیلیل بافت معدے و آنتوں، پھیپھڑوں اور پیشاب کی نالی کو بھی اندر سے ڈھانپتی ہے۔ ساخت کے لحاظ سے یہ خلیے چپٹے اور لمبے ہوتے ہیں۔',
        'د بدن دننه برخه د پوستکي په واسطه له بهرنۍ نړۍ جلا ده. پوستکی له اپیتیلیل نسج جوړ دی چې د حجرو د پرله پسې پاڼو په بڼه وي. اپیتیلیل نسج د هاضمې نل، سږي او د تشو متیازو لارې هم دننه پوښي. له جوړښته دا حجرې پلنې او اوږدې دي.')
    s.h('ii. Connective Tissue', 'ii. کنیکٹیو بافت', 'ii. نښلوونکی نسج')
    s.p('Connective tissue is the major supporting tissue of the animal body. Its cells are scattered through an extracellular material. There are many types of connective tissues.',
        'کنیکٹیو بافت جانور کے جسم کی بڑی سہارا دینے والی بافت ہے۔ اس کے خلیے بیرونی خلوی مادے میں بکھرے ہوتے ہیں۔ کنیکٹیو بافتوں کی بہت سی اقسام ہیں۔',
        'نښلوونکی نسج د ژوي د بدن لوی ملاتړی نسج دی. حجرې یې په بهرني حجروي مادې کې خورې وي. د نښلوونکو نسجونو ډېر ډولونه شته.')
    s.lines([
        ('a. Loose Connective Tissue: Its extracellular material contains loosely packed collagen (a protein) fibers. It is widely distributed under the epithelial tissues. It holds organs at their specific place.',
         'a. ڈھیلی کنیکٹیو بافت: اس کے بیرونی خلوی مادے میں ڈھیلے بھرے ہوئے کولاجن (ایک پروٹین) کے ریشے ہوتے ہیں۔ یہ اپی تھیلیل بافتوں کے نیچے وسیع پیمانے پر پھیلی ہوتی ہے۔ یہ اعضا کو ان کی مخصوص جگہ پر تھامے رکھتی ہے۔',
         'a. سست نښلوونکی نسج: بهرنۍ حجروي ماده یې سست پراته د کولاجن (یو پروټین) تارونه لري. د اپیتیلیل نسجونو لاندې پراخه خپره ده. غړي په خپل ځانګړي ځای کې ساتي.'),
        ('b. Fibrous Connective Tissue: Its extracellular material contains tightly packed collagen fibers. It is in the form of tendons which attach muscles to bones and ligaments join two bones.',
         'b. ریشے دار کنیکٹیو بافت: اس کے بیرونی خلوی مادے میں گنجان کولاجن ریشے ہوتے ہیں۔ یہ ٹینڈنز کی شکل میں ہوتی ہے جو عضلات کو ہڈیوں سے جوڑتے ہیں اور لگامنٹس دو ہڈیوں کو جوڑتے ہیں۔',
         'b. تارلرونکی نښلوونکی نسج: بهرنۍ حجروي ماده یې ټینګ پراته کولاجن تارونه لري. د وترونو په بڼه دی چې عضلې له هډوکو سره نښلوي او اربطې دوه هډوکي سره نښلوي.'),
        ('c. Adipose Tissue: It contains swollen cells due to the presence of large number of fat droplets. It is found around kidneys, under skin, in abdomen etc. It provides energy, insulates against heat loss and protects and supports organs.',
         'c. ایڈیپوز بافت: اس میں چربی کے بہت سے قطروں کی موجودگی کی وجہ سے پھولے ہوئے خلیے ہوتے ہیں۔ یہ گردوں کے گرد، جلد کے نیچے، پیٹ میں وغیرہ پائی جاتی ہے۔ یہ توانائی فراہم کرتی، حرارت کے ضیاع سے بچاتی اور اعضا کی حفاظت اور سہارا دیتی ہے۔',
         'c. د غوړ نسج: د غوړ د ډېرو څاڅکو د شتون له امله پړسېدلې حجرې لري. د پښتورګو شاوخوا، د پوستکي لاندې، په ګېډه کې او نورو ځایونو کې موندل کېږي. انرژي برابروي، د تودوخې له ضایع کېدو ساتي او غړي ساتي او ملاتړ یې کوي.'),
        ('d. Cartilage: Its extracellular material contains bundles of collagen fibers and rubbery substance. It is found around the ends of bones, in external ear, in nose, trachea and larynx etc. It provides support and maintains shape while allowing flexibility.',
         'd. کارٹلیج (کرکری ہڈی): اس کے بیرونی خلوی مادے میں کولاجن ریشوں کے گچھے اور ربڑ جیسا مادہ ہوتا ہے۔ یہ ہڈیوں کے سروں کے گرد، بیرونی کان، ناک، سانس کی نالی اور حنجرے وغیرہ میں پائی جاتی ہے۔ یہ لچک کے ساتھ سہارا دیتی اور شکل برقرار رکھتی ہے۔',
         'd. کرکړه: بهرنۍ حجروي ماده یې د کولاجن تارونو غونچې او ربړ ډوله ماده لري. د هډوکو د سرونو شاوخوا، په بهرني غوږ، پوزه، د ساه نل او حنجره کې موندل کېږي. د انعطاف سره ملاتړ ورکوي او بڼه ساتي.'),
        ('e. Bone: Its extracellular material contains collagen fibers and calcium salts. It supports, protects, provide lever system for movements, stores calcium and forms blood cells.',
         'e. ہڈی: اس کے بیرونی خلوی مادے میں کولاجن ریشے اور کیلشیم کے نمکیات ہوتے ہیں۔ یہ سہارا دیتی، حفاظت کرتی، حرکات کے لیے لیور نظام فراہم کرتی، کیلشیم ذخیرہ کرتی اور خون کے خلیے بناتی ہے۔',
         'e. هډوکی: بهرنۍ حجروي ماده یې د کولاجن تارونه او د کلسیم مالګې لري. ملاتړ کوي، ساتنه کوي، د حرکتونو لپاره د اهرم سیسټم برابروي، کلسیم زېرمه کوي او د وینې حجرې جوړوي.'),
        ('f. Blood: It is a special type of connective tissue. Its extracellular material (plasma) is fluid. It transports substances from one part of the body to the other and is also responsible for immunity.',
         'f. خون: یہ کنیکٹیو بافت کی ایک خاص قسم ہے۔ اس کا بیرونی خلوی مادہ (پلازما) سیال ہے۔ یہ مادوں کو جسم کے ایک حصے سے دوسرے حصے تک پہنچاتا ہے اور قوتِ مدافعت کا بھی ذمہ دار ہے۔',
         'f. وینه: دا د نښلوونکي نسج ځانګړی ډول دی. بهرنۍ حجروي ماده یې (پلازما) مایع ده. مواد د بدن له یوې برخې بلې ته وړي او د معافیت مسؤله هم ده.')])
    s.h('iii. Muscular Tissue', 'iii. عضلاتی بافت', 'iii. عضلي نسج')
    s.p('It consist of highly specialized contractile cells or fibers held together by connective tissue. Each muscle fiber is an elongated cell which has the ability to contract and relax. Skeletal, smooth and cardiac muscles are the examples of these tissues.',
        'یہ انتہائی مخصوص سکڑنے والے خلیوں یا ریشوں پر مشتمل ہے جو کنیکٹیو بافت کے ذریعے جڑے ہوتے ہیں۔ ہر عضلاتی ریشہ ایک لمبا خلیہ ہے جو سکڑنے اور پھیلنے کی صلاحیت رکھتا ہے۔ اسکیلیٹل، اسموتھ اور کارڈیک عضلات ان بافتوں کی مثالیں ہیں۔',
        'دا له ډېرو ځانګړو انقباضي حجرو یا تارونو جوړ دی چې د نښلوونکي نسج په واسطه سره تړل شوي. هر عضلي تار یوه اوږده حجره ده چې د تړل کېدو او خلاصېدو وړتیا لري. اسکلېټي، هوارې او د زړه عضلې د دې نسجونو بېلګې دي.')
    s.lines([
        ('a. Skeletal muscles: These are attached to cartilages and bones with the help of connective tissues called tendons. They are composed of striated (striped) cells that are long and cylindrical. The cells of skeletal muscles contain many nuclei. Skeletal muscles are voluntary and produce powerful, rapid contractions. It helps arms and legs to move.',
         'a. اسکیلیٹل عضلات: یہ کنیکٹیو بافتوں جنہیں ٹینڈنز کہتے ہیں کی مدد سے کارٹلیج اور ہڈیوں سے جڑے ہوتے ہیں۔ یہ دھاری دار خلیوں سے بنے ہوتے ہیں جو لمبے اور نلکی نما ہوتے ہیں۔ اسکیلیٹل عضلات کے خلیوں میں بہت سے مرکزے ہوتے ہیں۔ اسکیلیٹل عضلات ارادی ہیں اور طاقتور، تیز سکڑاؤ پیدا کرتے ہیں۔ یہ بازوؤں اور ٹانگوں کو حرکت دینے میں مدد دیتے ہیں۔',
         'a. اسکلېټي عضلې: د نښلوونکو نسجونو چې وترونه بلل کېږي په مرسته له کرکړو او هډوکو سره نښتي دي. له لیکه لرونکو حجرو جوړې دي چې اوږدې او استوانه یي دي. د اسکلېټي عضلو حجرې ډېرې هستې لري. اسکلېټي عضلې ارادي دي او قوي، چټک انقباضونه تولیدوي. د لاسونو او پښو په حرکت کې مرسته کوي.'),
        ('b. Smooth muscles: These are found in the walls of hollow structures such as blood vessels, gut etc. They produce slow contractions. Their contraction moves substances (foodstuff, urine) in the hollow organs. They are composed of Spindle shaped, un-striated muscles and are involuntary in action.',
         'b. اسموتھ عضلات: یہ کھوکھلی ساختوں جیسے خون کی نالیوں، آنتوں وغیرہ کی دیواروں میں پائے جاتے ہیں۔ یہ سست سکڑاؤ پیدا کرتے ہیں۔ ان کا سکڑاؤ کھوکھلے اعضا میں مادوں (خوراک، پیشاب) کو حرکت دیتا ہے۔ یہ تکلے نما، غیر دھاری دار عضلات سے بنے ہوتے ہیں اور غیر ارادی عمل کرتے ہیں۔',
         'b. هوارې عضلې: د تشو جوړښتونو لکه د وینې رګونو، کولمو او نورو په دېوالونو کې موندل کېږي. ورو انقباضونه تولیدوي. انقباض یې په تشو غړو کې مواد (خواړه، تشې متیازې) خوځوي. له دوک ډوله، بې لیکو عضلو جوړې دي او په عمل کې غیر ارادي دي.'),
        ('c. Cardiac muscle: These are found in heart. These are composed of branched fibers and are capable of sustained contraction. Their contraction produces heartbeat that propels blood into vessels. They are also involuntary in action.',
         'c. کارڈیک عضلہ: یہ دل میں پائے جاتے ہیں۔ یہ شاخ دار ریشوں سے بنے ہوتے ہیں اور مسلسل سکڑنے کی صلاحیت رکھتے ہیں۔ ان کا سکڑاؤ دل کی دھڑکن پیدا کرتا ہے جو خون کو نالیوں میں دھکیلتی ہے۔ یہ بھی غیر ارادی عمل کرتے ہیں۔',
         'c. د زړه عضله: په زړه کې موندل کېږي. له څانګه لرونکو تارونو جوړه ده او د دوامداره انقباض وړتیا لري. انقباض یې د زړه ټکان تولیدوي چې وینه رګونو ته ټېلوي. دا هم په عمل کې غیر ارادي دي.')])
    s.h('iv. Nervous Tissue', 'iv. اعصابی بافت', 'iv. عصبي نسج')
    s.p('It is composed of nerve cells which are called neurons. Neurons are capable of transmitting nerve impulses to conduct messages in the whole body. Nervous tissue is found in brain, spinal cord and nerves.',
        'یہ اعصابی خلیوں سے بنی ہوتی ہے جنہیں نیورونز کہتے ہیں۔ نیورونز پورے جسم میں پیغامات پہنچانے کے لیے عصبی پیغامات منتقل کرنے کی صلاحیت رکھتے ہیں۔ اعصابی بافت دماغ، حرام مغز اور اعصاب میں پائی جاتی ہے۔',
        'دا له عصبي حجرو جوړ دی چې نیورونونه بلل کېږي. نیورونونه په ټول بدن کې د پیغامونو د رسولو لپاره د عصبي پیغامونو د لېږد وړتیا لري. عصبي نسج په دماغ، نخاع او عصبونو کې موندل کېږي.')
    s.fig('bio4-fig4-28', *three(animal_tissues, AN_EN, AN_UR, AN_PS), .75, caption=('Figure 4.28: Animal Tissues', 'شکل 4.28: جانوروں کی بافتیں', 'شکل 4.28: د ژویو نسجونه'))
    s.callout(('Activities 4.5', 'سرگرمیاں 4.5', 'فعالیتونه 4.5'), [
        ('• Identify different animal and plant tissues from charts or from observation of prepared slides under microscope. Draw these tissues.', '• چارٹس سے یا خوردبین کے نیچے تیار شدہ سلائیڈز کے مشاہدے سے جانوروں اور پودوں کی مختلف بافتوں کی شناخت کریں۔ ان بافتوں کی اشکال بنائیں۔', '• له چارټونو یا د مایکروسکوپ لاندې د چمتو شویو سلایډونو له کتنې د ژویو او بوټو بېلابېل نسجونه وپېژنئ. دا نسجونه رسم کړئ.'),
        ('• Prepare a slide of tissue from flowering plants and observe the cells.', '• پھول دار پودوں کی بافت کی سلائیڈ تیار کریں اور خلیوں کا مشاہدہ کریں۔', '• له ګل لرونکو بوټو د نسج سلایډ چمتو کړئ او حجرې وګورئ.')])
    out.append(s)
    return out
