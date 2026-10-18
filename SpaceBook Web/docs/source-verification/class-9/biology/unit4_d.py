# -*- coding: utf-8 -*-
"""Unit 4 part D — PDF 82-88 (printed 79-85): 4.4 specificity, 4.5 SA/V, 4.6 transport (diffusion, facilitated, osmosis)."""
from bio9_tools import Section, svg_wrap, txt
from unit4_figs import multiline

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')
IP = ('Initiating and Planning', 'آغاز اور منصوبہ بندی', 'پیل او پلان جوړونه')


def cube(x, y, s, d, fill='#fff3c4'):
    return (f'<polygon points="{x},{y} {x+s},{y} {x+s+d},{y-d} {x+d},{y-d}" fill="#ffe082" stroke="#795548"/>'
            f'<polygon points="{x+s},{y} {x+s+d},{y-d} {x+s+d},{y+s-d} {x+s},{y+s}" fill="#ffca28" stroke="#795548"/>'
            f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{fill}" stroke="#795548"/>')


def sa_cubes(L):
    b = [cube(30, 60, 150, 25), '<circle cx="105" cy="135" r="9" fill="#1e88e5" stroke="#0d47a1" stroke-width="3"/>']
    b.append('<path d="M215,40 v150 M209,40 h12 M209,190 h12" stroke="#555"/>' + txt(222, 120, L['big'], 12, 'start', 'bold'))
    for r in range(3):
        for c in range(3):
            b.append(cube(300 + c * 50, 60 + r * 50, 46, 12))
            b.append(f'<circle cx="{323 + c*50}" cy="{83 + r*50}" r="6" fill="#1e88e5" stroke="#0d47a1" stroke-width="2"/>')
    b.append('<path d="M285,110 v46 M280,110 h10 M280,156 h10" stroke="#555"/>' + txt(278, 138, L['small'], 12, 'end', 'bold'))
    b.append(multiline(30, 235, L['cap1']) + multiline(320, 235, L['cap2']))
    return svg_wrap(''.join(b), 480, 280, L['title'])


SA_EN = dict(title='Figure 4.19: Cell size and surface area', big='30 um²', small='10 μm²', cap1=['Surface area of', 'one large cube', '= 5400 μm²'], cap2=['Total Surface area of', '27 small cubes', '= 16,200 μm²'])
SA_UR = dict(SA_EN, title='شکل 4.19', cap1=['ایک بڑے مکعب کا', 'سطحی رقبہ', '= 5400 μm²'], cap2=['27 چھوٹے مکعبوں کا', 'کل سطحی رقبہ', '= 16,200 μm²'])
SA_PS = dict(SA_EN, title='شکل 4.19', cap1=['د یوه لوی مکعب', 'سطحې مساحت', '= 5400 μm²'], cap2=['د 27 کوچنیو مکعبونو', 'ټول سطحې مساحت', '= 16,200 μm²'])


def activity_cubes(L):
    b = ['<g fill="none" stroke="#424242">']
    for x, y, s in ((60, 80, 70), (250, 40, 140)):
        d = s * .3
        b.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}"/><path d="M{x},{y} l{d},{-d} h{s} l{-d},{d} M{x+s},{y+s} l{d},{-d} v{-s}"/>')
    b.append('</g>')
    b.append(txt(160, 125, '1cm', 11) + txt(90, 165, '1cm', 11) + txt(140, 165, '1cm', 11))
    b.append(txt(400, 110, '2cm', 11) + txt(300, 200, '2cm', 11) + txt(400, 200, '2cm', 11))
    return svg_wrap(''.join(b), 470, 215, L)


def diffusion_fig(L):
    b = ['<rect x="20" y="70" width="440" height="120" fill="#fff8e1"/>']
    for y in (75, 185):
        b.append(''.join(f'<circle cx="{25 + i*14}" cy="{y}" r="7" fill="#f48fb1"/>' for i in range(32) if not 110 < 25 + i*14 < 190))
    b.append('<path d="M120,55 q-20,80 0,150 h30 q20,-75 0,-150 z M150,55 q20,80 0,150 h30 q-20,-75 0,-150 z" fill="#fff59d" stroke="#f9a825"/>')
    b.append('<path d="M150,225 L150,25" stroke="#212121" stroke-width="2"/><polygon points="144,30 156,30 150,18" fill="#212121"/>')
    b.append('<path d="M280,225 L280,25" stroke="#212121" stroke-width="2"/><polygon points="274,30 286,30 280,18" fill="#212121"/>')
    b.append(''.join(f'<text x="{x}" y="{y}" font-size="14" fill="#2e7d32">★</text>' for x, y in [(125, 225), (160, 232), (140, 240), (130, 30), (165, 22)]))
    b.append(''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#29b6f6"/>' for x, y in [(260, 220), (290, 225), (305, 215), (270, 235), (300, 240), (265, 30), (295, 35)]))
    b.append('<path d="M140,80 L100,40" stroke="#333"/>' + multiline(60, 22, L['protein'], 'start'))
    b.append(txt(150, 262, L['fac'], 12, 'middle', 'bold') + txt(280, 262, L['dif'], 12, 'middle', 'bold'))
    return svg_wrap(''.join(b), 480, 275, L['title'])


DF_EN = dict(title='Figure 4.20: Diffusion and facilitated diffusion', protein=['Transport', 'protein'], fac='Facilitated diffusion', dif='Diffusion')
DF_UR = dict(title='شکل 4.20', protein=['ٹرانسپورٹ', 'پروٹین'], fac='فیسلیٹیٹڈ ڈفیوژن', dif='ڈفیوژن')
DF_PS = dict(title='شکل 4.20', protein=['لېږدوونکی', 'پروټین'], fac='اسانه شوی ډیفیوژن', dif='ډیفیوژن')


def osmosis_fig(L):
    b = ['<rect x="300" y="20" width="150" height="250" fill="#64b5f6"/>']
    for i, key in enumerate(('hypo', 'iso', 'hyper')):
        b.append(txt(80 + i * 150, 15, L[key], 12, 'middle', 'bold'))
    b.append('<circle cx="80" cy="80" r="35" fill="#fff176" stroke="#f9a825"/><path d="M60,55 l-8,-12 M95,50 l6,-12" stroke="#1565c0"/>')
    b.append('<circle cx="230" cy="80" r="30" fill="#fff176" stroke="#f9a825"/>')
    b.append('<path d="M360,65 l10,-8 l10,8 l12,0 l-4,12 l8,10 l-12,4 l-4,12 l-10,-6 l-10,6 l-4,-12 l-12,-4 l8,-10 l-4,-12 z" fill="#fff176" stroke="#f9a825"/>')
    for i, key in enumerate(('lysed', 'normal', 'shrinked')):
        b.append(txt(80 + i * 150, 135, L[key], 11, 'middle'))
    b.append('<rect x="45" y="160" width="70" height="70" rx="6" fill="#c8e6c9" stroke="#2e7d32" stroke-width="3"/><rect x="52" y="167" width="56" height="56" rx="6" fill="#e3f2fd" stroke="#1565c0"/>')
    b.append('<rect x="195" y="160" width="70" height="70" rx="6" fill="#c8e6c9" stroke="#2e7d32" stroke-width="3"/><rect x="205" y="170" width="50" height="50" rx="10" fill="#e3f2fd" stroke="#1565c0"/>')
    b.append('<rect x="345" y="160" width="70" height="70" rx="6" fill="#c8e6c9" stroke="#2e7d32" stroke-width="3"/><path d="M362,178 q18,-8 36,4 q6,20 -6,30 q-18,8 -28,-4 q-10,-14 -2,-30 z" fill="#e3f2fd" stroke="#1565c0"/>')
    for i, key in enumerate(('turgid', 'flaccid', 'plasmo')):
        b.append(txt(80 + i * 150, 250, L[key], 11, 'middle'))
    b.append(multiline(455, 70, L['animal']) + multiline(455, 190, L['plant']))
    b.append(''.join(txt(x, y, 'H₂O', 9, 'middle', 'normal', '#0d47a1') for x, y in [(60, 40), (215, 45), (245, 45), (390, 40), (60, 155), (215, 155), (245, 155), (395, 155)]))
    return svg_wrap(''.join(b), 520, 275, L['title'])


OS_EN = dict(title='Figure 4.21: Effect of different solutions on animal and plant cells', hypo='Hypotonic solution', iso='Isotonic solution', hyper='Hypertonic solution',
             lysed='Lysed', normal='Normal', shrinked='Shrinked', turgid='Turgid (normal)', flaccid='Flaccid', plasmo='Plasmolysed', animal=['Animal', 'Cell'], plant=['Plant', 'Cell'])
OS_UR = dict(title='شکل 4.21', hypo='ہائپوٹونک محلول', iso='آئسوٹونک محلول', hyper='ہائپرٹونک محلول', lysed='پھٹا ہوا', normal='نارمل', shrinked='سکڑا ہوا',
             turgid='ٹرجڈ (نارمل)', flaccid='ڈھیلا (فلیسڈ)', plasmo='پلازمولائزڈ', animal=['جانور کا', 'خلیہ'], plant=['پودے کا', 'خلیہ'])
OS_PS = dict(title='شکل 4.21', hypo='هایپوټونیک محلول', iso='ایزوټونیک محلول', hyper='هایپرټونیک محلول', lysed='شلېدلې', normal='عادي', shrinked='راټوله شوې',
             turgid='ټینګه (عادي)', flaccid='سسته (فلاسډ)', plasmo='پلازمولایز شوې', animal=['د ژوي', 'حجره'], plant=['د بوټي', 'حجره'])


def sections():
    out = []
    s = Section('bio4_4', '4.4', 'Cells and their specificity', 'خلیات اور ان کی خصوصیت', 'حجرې او د هغوی ځانګړتیا', [82, 83])
    s.p('We know that cell is the basic unit of structure and function of living organisms. In unicellular organisms, a single cell performs all the functions. But in multicellular organisms, different cells are specialized to perform different functions. For example;',
        'ہم جانتے ہیں کہ خلیہ جانداروں کی ساخت اور فعل کی بنیادی اکائی ہے۔ یک خلوی جانداروں میں ایک ہی خلیہ تمام کام انجام دیتا ہے۔ لیکن کثیر خلوی جانداروں میں مختلف خلیات مختلف کام انجام دینے کے لیے مخصوص ہوتے ہیں۔ مثال کے طور پر؛',
        'موږ پوهېږو چې حجره د ژوندیو موجوداتو د جوړښت او دندې بنسټیز واحد دی. په یو حجروي موجوداتو کې یوه حجره ټولې دندې ترسره کوي. خو په څو حجروي موجوداتو کې بېلابېلې حجرې د بېلابېلو دندو لپاره ځانګړې شوې دي. د بېلګې په توګه؛')
    s.ul([('In plants, xylem cells conduct water from roots to upper parts. Phloem cells conduct food to various parts of the body. Similarly, there are cells specialized for photosynthesis.',
           'پودوں میں زائلم کے خلیات جڑوں سے اوپری حصوں تک پانی پہنچاتے ہیں۔ فلوئم کے خلیات خوراک کو جسم کے مختلف حصوں تک پہنچاتے ہیں۔ اسی طرح ضیائی تالیف کے لیے مخصوص خلیات بھی ہیں۔',
           'په بوټو کې د زایلم حجرې له ریښو پورتنیو برخو ته اوبه رسوي. د فلویم حجرې د بدن بېلابېلو برخو ته خواړه رسوي. همدارنګه د فوتوسنتز لپاره ځانګړې حجرې هم شته.'),
          ('Similarly in animals also different cells perform different functions. For example, nerve cells conduct nerve impulse and thus contribute in coordination in the body. Muscle cells undergo contraction and play role in movements of body. Red blood cells carry oxygen and white blood cells kill foreign agents and so contribute in the roles of blood in the transportation and defense of the body. The cells of bone deposit calcium in their extracellular spaces to make the bone tough and thus contribute to the supporting role of bones.',
           'اسی طرح جانوروں میں بھی مختلف خلیات مختلف کام انجام دیتے ہیں۔ مثال کے طور پر اعصابی خلیات عصبی پیغام منتقل کرتے ہیں اور اس طرح جسم میں ہم آہنگی میں حصہ لیتے ہیں۔ عضلاتی خلیات سکڑتے ہیں اور جسم کی حرکات میں کردار ادا کرتے ہیں۔ سرخ خونی خلیات آکسیجن لے جاتے ہیں اور سفید خونی خلیات بیرونی عوامل کو مارتے ہیں اور یوں جسم میں ترسیل اور دفاع میں خون کے کردار میں حصہ لیتے ہیں۔ ہڈی کے خلیات اپنی بیرونی خلوی جگہوں میں کیلشیم جمع کر کے ہڈی کو سخت بناتے ہیں اور یوں ہڈیوں کے سہارا دینے کے کردار میں حصہ لیتے ہیں۔',
           'همدارنګه په ژویو کې هم بېلابېلې حجرې بېلابېلې دندې ترسره کوي. د بېلګې په توګه عصبي حجرې عصبي پیغام لېږدوي او په دې توګه په بدن کې په همغږۍ کې ونډه لري. عضلي حجرې تړل کېږي او د بدن په حرکتونو کې رول لري. سرې وینې حجرې اکسیجن وړي او سپینې وینې حجرې بهرني عوامل وژني او په دې توګه د بدن په لېږد او دفاع کې د وینې په رول کې ونډه اخلي. د هډوکي حجرې په خپلو بهرني حجروي ځایونو کې کلسیم زېرمه کوي ترڅو هډوکی کلک کړي او په دې توګه د هډوکو د ملاتړ په رول کې ونډه لري.')])
    s.p('The cells perform these specialized functions due to their size and shapes and presence of organelles. For example;',
        'خلیات یہ مخصوص کام اپنی جسامت، شکل اور عضیات کی موجودگی کی وجہ سے انجام دیتے ہیں۔ مثال کے طور پر؛',
        'حجرې دا ځانګړې دندې د خپل جسامت، بڼې او د اورګانیلونو د شتون له امله ترسره کوي. د بېلګې په توګه؛')
    s.ul([('Nerve cells are long for the transmission of nerve impulse.', 'عصبی پیغام کی ترسیل کے لیے اعصابی خلیات لمبے ہوتے ہیں۔', 'عصبي حجرې د عصبي پیغام د لېږد لپاره اوږدې وي.'),
          ('Xylem cells are tube-like and have thick walls for conduction of water and support.', 'زائلم کے خلیات نلکی نما ہوتے ہیں اور پانی کی ترسیل اور سہارے کے لیے ان کی دیواریں موٹی ہوتی ہیں۔', 'د زایلم حجرې نل ډوله وي او د اوبو د لېږد او ملاتړ لپاره پنډ دېوالونه لري.'),
          ('Red blood cells are disc like and biconcave in shape to increase their surface area to volume ratio, so more oxygen can be carried.', 'سرخ خونی خلیات طشتری نما اور دونوں طرف سے مقعر ہوتے ہیں تاکہ ان کے سطحی رقبے اور حجم کا تناسب بڑھے اور زیادہ آکسیجن لے جائی جا سکے۔', 'سرې وینې حجرې ټیکلي ډوله او دواړو خواوو ته ژورې وي ترڅو د سطحې او حجم نسبت یې زیات شي او ډېر اکسیجن یوسي.'),
          ('Root hair cells have large surface area for the maximum absorption of water and salts.', 'جڑ کے بالوں کے خلیوں کا سطحی رقبہ زیادہ ہوتا ہے تاکہ پانی اور نمکیات زیادہ سے زیادہ جذب ہوں۔', 'د ریښې د وېښتانو حجرې د اوبو او مالګو د زیات جذب لپاره لویه سطحه لري.'),
          ('Cells involved in making secretions have more complex endoplasmic reticulum and golgi apparatus.', 'رطوبتیں بنانے والے خلیوں میں اینڈوپلازمک ریٹیکولم اور گولجی اپریٹس زیادہ پیچیدہ ہوتے ہیں۔', 'هغه حجرې چې افرازات جوړوي، ډېر پېچلی انډوپلازمیک ریټیکولم او ګولجي اپراټس لري.'),
          ('Cells involved in photosynthesis have chloroplasts.', 'ضیائی تالیف کرنے والے خلیوں میں کلوروپلاسٹ ہوتے ہیں۔', 'هغه حجرې چې فوتوسنتز کوي کلوروپلاسټ لري.')])
    s.p('Cell as an open system: A cell works as an open system i.e. it takes in substances needed for its activities through its cell membrane. Then it performs the metabolic processes assigned to it. Products and by-products are formed in metabolism. Cell either utilizes the products or transports them to other cells. The byproducts are either stored or are excreted out of the cell.',
        'خلیہ ایک کھلے نظام کے طور پر: خلیہ ایک کھلے نظام کے طور پر کام کرتا ہے یعنی اپنی سرگرمیوں کے لیے درکار مادے اپنی خلوی جھلی کے ذریعے اندر لیتا ہے۔ پھر اپنے ذمے میٹابولک عمل انجام دیتا ہے۔ میٹابولزم میں پیداوار اور ضمنی پیداوار بنتی ہے۔ خلیہ یا تو پیداوار استعمال کرتا ہے یا انہیں دوسرے خلیوں تک پہنچاتا ہے۔ ضمنی پیداوار یا تو ذخیرہ ہوتی ہے یا خلیے سے خارج کر دی جاتی ہے۔',
        'حجره د خلاص سیسټم په توګه: حجره د یو خلاص سیسټم په توګه کار کوي یعنې د خپلو فعالیتونو لپاره اړین مواد د خپلې غشا له لارې اخلي. بیا ورته سپارل شوې میټابولیکي پروسې ترسره کوي. په میټابولیزم کې محصولات او فرعي محصولات جوړېږي. حجره یا محصولات کاروي یا یې نورو حجرو ته لېږدوي. فرعي محصولات یا زېرمه کېږي یا له حجرې بهر اطراح کېږي.')
    s.callout(SI, [('Cells vary greatly in size. The smallest cells are some bacteria, with diameter between 0.1 μm to 1.0 μm. The largest cells are bird eggs and the longest cells are some muscle cells and nerve cells. Most cells lie between these extremes.',
                    'خلیوں کی جسامت میں بہت فرق ہوتا ہے۔ سب سے چھوٹے خلیے بعض بیکٹیریا ہیں جن کا قطر 0.1 μm سے 1.0 μm تک ہوتا ہے۔ سب سے بڑے خلیے پرندوں کے انڈے اور سب سے لمبے خلیے بعض عضلاتی اور اعصابی خلیات ہیں۔ زیادہ تر خلیے ان انتہاؤں کے درمیان ہوتے ہیں۔',
                    'حجرې په اندازه کې ډېر توپیر لري. تر ټولو کوچنۍ حجرې ځینې باکتریا دي چې قطر یې له 0.1 μm تر 1.0 μm دی. تر ټولو لویې حجرې د مرغانو هګۍ او تر ټولو اوږدې حجرې ځینې عضلي او عصبي حجرې دي. ډېری حجرې د دې دوو حدونو ترمنځ دي.')])
    out.append(s)

    s = Section('bio4_5', '4.5', 'Surface area to Volume Ratio', 'سطحی رقبے اور حجم کا تناسب', 'د سطحې مساحت او حجم نسبت', [83, 84, 85, 86])
    s.p('Large cells have less surface area in relation to their volume while small cells have more surface area. Figure 4.19 shows 1 large cell and 27 small cells. In both cases, the total volume is the same:',
        'بڑے خلیوں کا سطحی رقبہ ان کے حجم کے لحاظ سے کم ہوتا ہے جبکہ چھوٹے خلیوں کا سطحی رقبہ زیادہ ہوتا ہے۔ شکل 4.19 میں 1 بڑا خلیہ اور 27 چھوٹے خلیات دکھائے گئے ہیں۔ دونوں صورتوں میں کل حجم ایک ہی ہے:',
        'لویې حجرې د خپل حجم په پرتله لږه سطحه لري په داسې حال کې چې کوچنۍ حجرې ډېره سطحه لري. شکل 4.19 یوه لویه حجره او 27 کوچنۍ حجرې ښيي. په دواړو حالتونو کې ټول حجم یو شان دی:')
    s.lines([('Volume = 30 μm × 30 μm × 30 μm = 27,000 μm³', 'حجم = 30 μm × 30 μm × 30 μm = 27,000 μm³', 'حجم = 30 μm × 30 μm × 30 μm = 27,000 μm³')])
    s.p('In contrast to the total volume, the total surface areas are very different. Because the cell has 6 sides, its surface area is 6 times the area of 1 side. The surface areas of the cells are as follows:',
        'کل حجم کے برعکس کل سطحی رقبے بہت مختلف ہیں۔ چونکہ خلیے کے 6 رخ ہیں، اس لیے اس کا سطحی رقبہ ایک رخ کے رقبے کا 6 گنا ہے۔ خلیوں کے سطحی رقبے یہ ہیں:',
        'د ټول حجم برعکس، ټولې سطحې ډېر توپیر لري. ځکه چې حجره 6 مخونه لري، سطحه یې د یوه مخ د مساحت 6 چنده ده. د حجرو سطحې دا دي:')
    s.lines([('Surface area of 1 large cell = 6 × (30 μm × 30 μm) = 5400 μm²', 'ایک بڑے خلیے کا سطحی رقبہ = 6 × (30 μm × 30 μm) = 5400 μm²', 'د یوې لویې حجرې سطحه = 6 × (30 μm × 30 μm) = 5400 μm²'),
             ('Surface area of 1 small cell = 6 × (10 μm × 10 μm) = 600 μm²', 'ایک چھوٹے خلیے کا سطحی رقبہ = 6 × (10 μm × 10 μm) = 600 μm²', 'د یوې کوچنۍ حجرې سطحه = 6 × (10 μm × 10 μm) = 600 μm²'),
             ('and', 'اور', 'او'),
             ('Surface area of 27 small cells = 27 × 600 μm² = 16, 200 μm²', '27 چھوٹے خلیوں کا سطحی رقبہ = 27 × 600 μm² = 16,200 μm²', 'د 27 کوچنیو حجرو سطحه = 27 × 600 μm² = 16,200 μm²')])
    s.p('The need of nutrients and rate of waste production are directly proportional to cell volume. The cell takes up nutrients and excretes wastes through its surface cell membrane. So a large volume cell demands large surface area. But, a large cell has a much smaller surface area relative to its volume than smaller cells. So, the cell membranes of small cells can serve their small volumes more easily than the membrane of the large cell.',
        'غذائی اجزا کی ضرورت اور فضلات بننے کی شرح خلیے کے حجم کے راست متناسب ہیں۔ خلیہ اپنی سطحی خلوی جھلی کے ذریعے غذائی اجزا لیتا اور فضلات خارج کرتا ہے۔ اس لیے بڑے حجم والے خلیے کو زیادہ سطحی رقبہ درکار ہے۔ لیکن بڑے خلیے کا سطحی رقبہ اپنے حجم کے لحاظ سے چھوٹے خلیوں سے بہت کم ہوتا ہے۔ اس لیے چھوٹے خلیوں کی جھلیاں اپنے چھوٹے حجم کی ضرورت بڑے خلیے کی جھلی سے زیادہ آسانی سے پوری کر سکتی ہیں۔',
        'د غذايي موادو اړتیا او د فاضله موادو د تولید کچه د حجرې له حجم سره مستقیم تناسب لري. حجره غذايي مواد اخلي او فاضله مواد د خپلې سطحي غشا له لارې باسي. نو لوی حجم لرونکې حجره لویې سطحې ته اړتیا لري. خو لویه حجره د خپل حجم په پرتله تر کوچنیو حجرو ډېره لږه سطحه لري. نو د کوچنیو حجرو غشاوې خپل کوچني حجم ته د لویې حجرې له غشا اسانه خدمت کولای شي.')
    s.p('Each unit of volume requires a specific amount of surface area to supply its metabolism with raw materials. The amount of surface area available to each unit of volume varies with the size of a cell. As a cell grows its SA/V (surface area to volume ratio) decreases. At some point in its growth, its SA/V becomes so small that its surface area is too small to supply its raw materials to its volume. At this point, the cell cannot get larger.',
        'حجم کی ہر اکائی کو اپنے میٹابولزم کو خام مال فراہم کرنے کے لیے ایک مخصوص سطحی رقبہ درکار ہے۔ حجم کی ہر اکائی کو دستیاب سطحی رقبہ خلیے کی جسامت کے ساتھ بدلتا ہے۔ جیسے جیسے خلیہ بڑھتا ہے اس کا SA/V (سطحی رقبے اور حجم کا تناسب) کم ہوتا جاتا ہے۔ نشوونما کے کسی مرحلے پر اس کا SA/V اتنا کم ہو جاتا ہے کہ اس کا سطحی رقبہ اپنے حجم کو خام مال فراہم کرنے کے لیے ناکافی ہو جاتا ہے۔ اس مرحلے پر خلیہ مزید بڑا نہیں ہو سکتا۔',
        'د حجم هر واحد د خپل میټابولیزم ته د خامو موادو د رسولو لپاره ټاکلې سطحې ته اړتیا لري. د حجم هر واحد ته د موجودې سطحې اندازه د حجرې له جسامت سره بدلېږي. لکه څنګه چې حجره لویېږي د هغې SA/V (د سطحې او حجم نسبت) کمېږي. د ودې په یو پړاو کې یې SA/V دومره کوچنی کېږي چې سطحه یې خپل حجم ته د خامو موادو د رسولو لپاره بسنه نه کوي. په دې پړاو کې حجره نوره نه لویېږي.')
    s.fig('bio4-fig4-19', sa_cubes(SA_EN), sa_cubes(SA_UR), sa_cubes(SA_PS), .7,
          caption=('Figure 4.19: Cell size and surface area', 'شکل 4.19: خلیے کی جسامت اور سطحی رقبہ', 'شکل 4.19: د حجرې جسامت او سطحه'))
    s.p('SpaceBook note: the figure labels the cube sides as "30 um²" and "10 μm²"; these are lengths (30 μm and 10 μm). Printed labels are kept.',
        'اسپیس بک نوٹ: شکل میں مکعب کے اضلاع کو ”30 um²“ اور ”10 μm²“ لکھا گیا ہے؛ یہ لمبائیاں (30 μm اور 10 μm) ہیں۔ چھپے ہوئے لیبل رکھے گئے ہیں۔',
        'د سپېس بوک یادونه: شکل د مکعب اړخونه ”30 um²“ او ”10 μm²“ لیکلي؛ دا اوږدوالي (30 μm او 10 μm) دي. چاپ شوي لیبلونه ساتل شوي.', editorial=True)
    s.h('Example', 'مثال', 'بېلګه')
    s.p('Compare the surface area to volume ratio SA / V (surface area:volume) of the following:', 'درج ذیل کے سطحی رقبے اور حجم کے تناسب SA / V (سطحی رقبہ:حجم) کا موازنہ کریں:', 'د لاندې د سطحې او حجم نسبت SA / V (سطحه:حجم) پرتله کړئ:')
    s.ul([('Cube a: 1 cm × 1 cm × 1 cm', 'مکعب a: 1 cm × 1 cm × 1 cm', 'مکعب a: 1 cm × 1 cm × 1 cm'), ('Cube b: 10 cm × 10 cm × 10 cm', 'مکعب b: 10 cm × 10 cm × 10 cm', 'مکعب b: 10 cm × 10 cm × 10 cm')])
    s.h('Solution:', 'حل:', 'حل:')
    s.lines([('Smaller cube (1 cm × 1 cm × 1 cm)', 'چھوٹا مکعب (1 cm × 1 cm × 1 cm)', 'کوچنی مکعب (1 cm × 1 cm × 1 cm)'),
             ('The surface area of one side = 1 cm × 1 cm = 1 square cm (or 1 cm²).', 'ایک رخ کا سطحی رقبہ = 1 cm × 1 cm = 1 مربع سینٹی میٹر (یا 1 cm²)۔', 'د یوه مخ سطحه = 1 cm × 1 cm = 1 مربع سانتي متر (یا 1 cm²).'),
             ('There are 6 sides, so the total surface area = 6 × cm² = 6 cm².', '6 رخ ہیں، اس لیے کل سطحی رقبہ = 6 × cm² = 6 cm²۔', '6 مخونه دي، نو ټوله سطحه = 6 × cm² = 6 cm².'),
             ('Volume = 1 cm × 1 cm × 1 cm = 1 cubic cm (or 1 cm³)', 'حجم = 1 cm × 1 cm × 1 cm = 1 مکعب سینٹی میٹر (یا 1 cm³)', 'حجم = 1 cm × 1 cm × 1 cm = 1 مکعب سانتي متر (یا 1 cm³)'),
             ('Surface Area: Volume = 6 cm²/1 cm³ = 6 cm²/cm³ (or 6 square cm of surface area for each cubic cm of volume)', 'سطحی رقبہ: حجم = 6 cm²/1 cm³ = 6 cm²/cm³ (یعنی حجم کے ہر مکعب سینٹی میٹر کے لیے 6 مربع سینٹی میٹر سطحی رقبہ)', 'سطحه: حجم = 6 cm²/1 cm³ = 6 cm²/cm³ (یعنې د حجم د هر مکعب سانتي متر لپاره 6 مربع سانتي متره سطحه)'),
             ('Larger cube (10 cm × 10 cm × 10 cm)', 'بڑا مکعب (10 cm × 10 cm × 10 cm)', 'لوی مکعب (10 cm × 10 cm × 10 cm)'),
             ('The surface area of one side = 10 cm × 10 cm = 100 square cm (or 100 cm²).', 'ایک رخ کا سطحی رقبہ = 10 cm × 10 cm = 100 مربع سینٹی میٹر (یا 100 cm²)۔', 'د یوه مخ سطحه = 10 cm × 10 cm = 100 مربع سانتي متره (یا 100 cm²).'),
             ('There are 6 sides, so the total surface area = 6 × 100cm² = 600 cm².', '6 رخ ہیں، اس لیے کل سطحی رقبہ = 6 × 100 cm² = 600 cm²۔', '6 مخونه دي، نو ټوله سطحه = 6 × 100 cm² = 600 cm².'),
             ('Volume = 10 cm × 10 cm × 10 cm = 1000 cubic cm (or 1000 cm³)', 'حجم = 10 cm × 10 cm × 10 cm = 1000 مکعب سینٹی میٹر (یا 1000 cm³)', 'حجم = 10 cm × 10 cm × 10 cm = 1000 مکعب سانتي متره (یا 1000 cm³)'),
             ('Surface Area: Volume = 600 cm²/1000 cm³ = 0.6 cm²/cm³ (or 0.6 square cm of surface area for each cubic cm of volume)', 'سطحی رقبہ: حجم = 600 cm²/1000 cm³ = 0.6 cm²/cm³ (یعنی حجم کے ہر مکعب سینٹی میٹر کے لیے 0.6 مربع سینٹی میٹر سطحی رقبہ)', 'سطحه: حجم = 600 cm²/1000 cm³ = 0.6 cm²/cm³ (یعنې د حجم د هر مکعب سانتي متر لپاره 0.6 مربع سانتي متره سطحه)')])
    s.callout(('Activity 4.2', 'سرگرمی 4.2', 'فعالیت 4.2'), [('Compare the surface area and volume of large and small cubes with given dimensions in the diagrams below.',
                                                         'نیچے دی گئی اشکال میں دیے گئے ابعاد کے ساتھ بڑے اور چھوٹے مکعبوں کے سطحی رقبے اور حجم کا موازنہ کریں۔',
                                                         'په لاندې انځورونو کې د ورکړل شوو اندازو سره د لویو او کوچنیو مکعبونو سطحه او حجم پرتله کړئ.')])
    a = activity_cubes('Activity 4.2 cubes: 1 cm and 2 cm')
    s.fig('bio4-act4-2', a, a.replace('Activity 4.2 cubes: 1 cm and 2 cm', 'سرگرمی 4.2'), a.replace('Activity 4.2 cubes: 1 cm and 2 cm', 'فعالیت 4.2'), .55)
    s.callout(('Activities 4.3', 'سرگرمیاں 4.3', 'فعالیتونه 4.3'), [
        ('• Examine an animal and a plant cell under the microscope. Draw the diagrams to represent your observations of the cells.', '• خوردبین کے نیچے جانور اور پودے کے خلیے کا معائنہ کریں۔ خلیوں کے اپنے مشاہدات ظاہر کرنے کے لیے اشکال بنائیں۔', '• د مایکروسکوپ لاندې د ژوي او بوټي حجره وګورئ. د حجرو د خپلو کتنو د ښودلو لپاره انځورونه رسم کړئ.'),
        ('• Draw diagrams to represent differences between plant and animal cells.', '• پودے اور جانور کے خلیوں کا فرق ظاہر کرنے کے لیے اشکال بنائیں۔', '• د بوټي او ژوي د حجرو توپیرونه د ښودلو لپاره انځورونه رسم کړئ.'),
        ('• Draw diagrams to represent differences between prokaryote and eukaryote.', '• پروکیریوٹ اور یوکیریوٹ کا فرق ظاہر کرنے کے لیے اشکال بنائیں۔', '• د پروکاریوټ او یوکاریوټ توپیرونه د ښودلو لپاره انځورونه رسم کړئ.')])
    s.callout(IP, [('Compare the parts of the cells to the human body parts. For example, the nucleus is the brain of the cell while the endoplasmic reticulum is the cell\'s circulatory system.',
                    'خلیے کے حصوں کا انسانی جسم کے حصوں سے موازنہ کریں۔ مثال کے طور پر مرکزہ خلیے کا دماغ ہے جبکہ اینڈوپلازمک ریٹیکولم خلیے کا دورانِ خون کا نظام ہے۔',
                    'د حجرې برخې د انساني بدن له برخو سره پرتله کړئ. د بېلګې په توګه هسته د حجرې دماغ دی په داسې حال کې چې انډوپلازمیک ریټیکولم د حجرې د دوران سیسټم دی.')])
    s.callout(('Communication and Teamwork', 'ابلاغ اور ٹیم ورک', 'اړیکې او ډله ییز کار'), [('Make the models of plant and animal cell with all their cell organelles and explain their functions in class presentation.',
                                                                                         'پودے اور جانور کے خلیے کے تمام عضیات کے ساتھ ماڈل بنائیں اور کلاس پریزنٹیشن میں ان کے افعال کی وضاحت کریں۔',
                                                                                         'د بوټي او ژوي د حجرې ماډلونه د ټولو اورګانیلونو سره جوړ کړئ او په ټولګي کې یې دندې تشریح کړئ.')])
    out.append(s)

    s = Section('bio4_6', '4.6', 'Passage of Molecules into and out of Cells (Active and Passive Transport)', 'خلیوں کے اندر اور باہر مالیکیولز کی آمد و رفت (ایکٹیو اور پیسو ٹرانسپورٹ)', 'حجرو ته د ننه او بهر د مالیکولونو تګ راتګ (فعال او غیر فعال لېږد)', [86, 87, 88])
    s.p('You know that cell membrane is semi-permeable. It controls the movement of molecules into and out of the cell. In this way, it maintains equilibrium inside the cell as well as outside. The movement of materials in and out of cell is through diffusion, facilitated diffusion, osmosis, filtration, active transport, endocytosis and exocytosis.',
        'آپ جانتے ہیں کہ خلوی جھلی نیم نفوذ پذیر ہے۔ یہ خلیے کے اندر اور باہر مالیکیولز کی حرکت کو کنٹرول کرتی ہے۔ اس طرح یہ خلیے کے اندر اور باہر توازن برقرار رکھتی ہے۔ خلیے کے اندر اور باہر مادوں کی حرکت ڈفیوژن، فیسلیٹیٹڈ ڈفیوژن، اوسموسس، فلٹریشن، ایکٹیو ٹرانسپورٹ، اینڈوسائٹوسس اور ایگزوسائٹوسس کے ذریعے ہوتی ہے۔',
        'تاسو پوهېږئ چې د حجرې غشا نیم نفوذ منونکې ده. دا حجرې ته د ننه او بهر د مالیکولونو حرکت کنټرولوي. په دې ډول د حجرې دننه او بهر توازن ساتي. حجرې ته د ننه او بهر د موادو حرکت د ډیفیوژن، اسانه شوي ډیفیوژن، اوسموزس، فلټریشن، فعال لېږد، انډوسایټوزس او اګزوسایټوزس له لارې کېږي.')
    s.h('i. Diffusion', 'i. ڈفیوژن (نفوذ)', 'i. ډیفیوژن')
    s.p('It is the random movement of a substance from the region of higher concentration to the region of lower concentration. Cell membrane does not spend energy when molecules diffuse through it. That is why diffusion is a type of passive transport.',
        'یہ کسی مادے کی زیادہ ارتکاز والے علاقے سے کم ارتکاز والے علاقے کی طرف بے ترتیب حرکت ہے۔ جب مالیکیولز خلوی جھلی سے نفوذ کرتے ہیں تو جھلی توانائی خرچ نہیں کرتی۔ اسی لیے ڈفیوژن غیر فعال (پیسو) ٹرانسپورٹ کی ایک قسم ہے۔',
        'دا د یوې مادې له لوړ غلظت لرونکې سیمې څخه ټیټ غلظت لرونکې سیمې ته ناڅاپي حرکت دی. کله چې مالیکولونه له غشا څخه تېرېږي، غشا انرژي نه لګوي. له همدې امله ډیفیوژن د غیر فعال لېږد یو ډول دی.')
    s.callout(STS, [('"All diseases are disturbances at the cellular level" (Rudolph Virchow, 1858). We always try to treat a disease and for this we try to find out the causes for the disease. We must understand the changes occurring at the cellular level to understand the cause of disease. The changes in the gene function may be the reasons for various disease. However, not all diseases are because of the gene functions such as infectious disease. In all diseases, cell biology is important from causes to treatments.',
                     '”تمام بیماریاں خلوی سطح پر خرابیاں ہیں“ (روڈولف ورشو، 1858)۔ ہم ہمیشہ بیماری کا علاج کرنے کی کوشش کرتے ہیں اور اس کے لیے بیماری کی وجوہات معلوم کرنے کی کوشش کرتے ہیں۔ بیماری کی وجہ سمجھنے کے لیے ہمیں خلوی سطح پر ہونے والی تبدیلیوں کو سمجھنا چاہیے۔ جین کے افعال میں تبدیلیاں مختلف بیماریوں کی وجہ ہو سکتی ہیں۔ تاہم تمام بیماریاں جین کے افعال کی وجہ سے نہیں ہوتیں جیسے متعدی بیماریاں۔ تمام بیماریوں میں وجوہات سے علاج تک خلوی حیاتیات اہم ہے۔',
                     '”ټولې ناروغۍ په حجروي کچه ګډوډۍ دي“ (روډولف ویرشو، 1858). موږ تل د ناروغۍ د درملنې هڅه کوو او د دې لپاره د ناروغۍ د لاملونو د موندلو هڅه کوو. د ناروغۍ د لامل د پوهېدو لپاره باید په حجروي کچه بدلونونه وپېژنو. د جین په دندو کې بدلونونه ښايي د بېلابېلو ناروغیو لاملونه وي. خو ټولې ناروغۍ د جین د دندو له امله نه دي لکه ساري ناروغۍ. په ټولو ناروغیو کې له لاملونو تر درملنې د حجرې بیولوژي مهمه ده.'),
                    ('Cell biology is important field of biological sciences. Studying cell biology may lead to a successful career. Cell biologist examines how the cell develops and how it works. Molecular biologist studies the molecules and processes inside the cells. Research specialist conducts and report research in the research laboratory. Laboratory technician assists the scientist in their research. A graduate of cell biology could be a Biology teacher who teaches cell biology at graduate and secondary school level.',
                     'خلوی حیاتیات حیاتیاتی علوم کا اہم شعبہ ہے۔ خلوی حیاتیات کا مطالعہ کامیاب کیریئر کا باعث بن سکتا ہے۔ سیل بائیولوجسٹ جانچتا ہے کہ خلیہ کیسے بنتا اور کیسے کام کرتا ہے۔ مالیکیولر بائیولوجسٹ خلیوں کے اندر مالیکیولز اور عوامل کا مطالعہ کرتا ہے۔ ریسرچ اسپیشلسٹ تحقیقی لیبارٹری میں تحقیق کرتا اور رپورٹ کرتا ہے۔ لیبارٹری ٹیکنیشن سائنس دانوں کی تحقیق میں مدد کرتا ہے۔ خلوی حیاتیات کا فارغ التحصیل حیاتیات کا استاد بن سکتا ہے جو گریجویٹ اور ثانوی اسکول کی سطح پر خلوی حیاتیات پڑھائے۔',
                     'د حجرې بیولوژي د بیولوژیکي علومو مهمه برخه ده. د حجرې د بیولوژي مطالعه ښايي بریالي مسلک ته لار پرانیزي. د حجرې بیولوژیست ګوري چې حجره څنګه جوړېږي او څنګه کار کوي. مالیکولي بیولوژیست د حجرو دننه مالیکولونه او پروسې څېړي. څېړنیز متخصص په څېړنیز لابراتوار کې څېړنه کوي او راپور ورکوي. لابراتوار تخنیکر له ساینس پوهانو سره په څېړنه کې مرسته کوي. د حجرې بیولوژي فارغ کېدای شي د بیولوژي ښوونکی شي چې په لیسانس او ثانوي ښوونځي کچه د حجرې بیولوژي تدریسوي.')])
    s.p('Only small molecules can diffuse through cell membrane e.g. water, carbon dioxide, oxygen and some other simple molecules. Diffusion is a slow process, yet it is efficient and rapid enough to fulfill the requirements of the cells. Substance such as glucose, O₂ and CO₂ can easily diffuse through the membrane. Glucose is present in higher concentration after the food is digested in small intestine. Therefore, glucose is transported to villi from the inner space of small intestine through diffusion to be stored in the form of glycogen in liver.',
        'صرف چھوٹے مالیکیول خلوی جھلی سے نفوذ کر سکتے ہیں مثلاً پانی، کاربن ڈائی آکسائیڈ، آکسیجن اور کچھ دوسرے سادہ مالیکیول۔ ڈفیوژن ایک سست عمل ہے، پھر بھی یہ خلیوں کی ضروریات پوری کرنے کے لیے کافی مؤثر اور تیز ہے۔ گلوکوز، O₂ اور CO₂ جیسے مادے آسانی سے جھلی سے نفوذ کر سکتے ہیں۔ چھوٹی آنت میں خوراک ہضم ہونے کے بعد گلوکوز زیادہ ارتکاز میں ہوتا ہے۔ اس لیے گلوکوز چھوٹی آنت کی اندرونی جگہ سے ڈفیوژن کے ذریعے ولائی تک پہنچایا جاتا ہے تاکہ جگر میں گلائکوجن کی شکل میں ذخیرہ ہو۔',
        'یوازې کوچني مالیکولونه له غشا ډیفیوژ کېدای شي لکه اوبه، کاربن ډای اکساید، اکسیجن او ځینې نور ساده مالیکولونه. ډیفیوژن ورو پروسه ده، خو د حجرو د اړتیاوو د پوره کولو لپاره کافي اغېزمنه او چټکه ده. ګلوکوز، O₂ او CO₂ په څېر مواد په اسانۍ له غشا ډیفیوژ کېدای شي. په کوچنۍ کولمه کې د خوړو له هضم وروسته ګلوکوز په لوړ غلظت کې وي. نو ګلوکوز د کوچنۍ کولمې له داخلي فضا څخه د ډیفیوژن له لارې ویلایو ته لېږدول کېږي ترڅو په ځيګر کې د ګلایکوجن په بڼه زېرمه شي.')
    s.h('ii. Facilitated Diffusion', 'ii. فیسلیٹیٹڈ ڈفیوژن', 'ii. اسانه شوی ډیفیوژن')
    s.p('Many molecules cannot diffuse through cell membranes due to their size or charge. Such molecules are taken into or out of the cells with the help of transport proteins present in cell membranes. When transport proteins help to move a molecule from high to low concentration without the expenditure of energy, the process is called facilitated diffusion. It is also a type of passive transport.',
        'بہت سے مالیکیول اپنی جسامت یا چارج کی وجہ سے خلوی جھلیوں سے نفوذ نہیں کر سکتے۔ ایسے مالیکیولز کو خلوی جھلیوں میں موجود ٹرانسپورٹ پروٹینز کی مدد سے خلیوں کے اندر یا باہر لے جایا جاتا ہے۔ جب ٹرانسپورٹ پروٹینز توانائی خرچ کیے بغیر کسی مالیکیول کو زیادہ سے کم ارتکاز کی طرف لے جانے میں مدد دیں تو اس عمل کو فیسلیٹیٹڈ ڈفیوژن کہتے ہیں۔ یہ بھی غیر فعال ٹرانسپورٹ کی ایک قسم ہے۔',
        'ډېر مالیکولونه د خپلې اندازې یا چارج له امله له غشاوو ډیفیوژ کېدای نه شي. داسې مالیکولونه په غشاوو کې د موجودو لېږدوونکو پروټینونو په مرسته حجرو ته ننه یا بهر وړل کېږي. کله چې لېږدوونکي پروټینونه پرته له انرژي لګولو د یو مالیکول له لوړ څخه ټیټ غلظت ته په حرکت کې مرسته وکړي، دې پروسې ته اسانه شوی ډیفیوژن ویل کېږي. دا هم د غیر فعال لېږد یو ډول دی.')
    s.callout(SI, [('Diffusion can be clearly demonstrated by a simple example i.e. when a coloured crystal like KMnO₄ is dropped in a beaker of water. Gradually its molecules will diffuse evenly in all directions throughout the water, resulting in uniform distribution of colour.',
                    'ڈفیوژن کو ایک سادہ مثال سے واضح طور پر دکھایا جا سکتا ہے یعنی جب KMnO₄ جیسا رنگین قلم پانی کے بیکر میں ڈالا جائے۔ آہستہ آہستہ اس کے مالیکیول پورے پانی میں ہر سمت یکساں پھیل جائیں گے اور رنگ یکساں تقسیم ہو جائے گا۔',
                    'ډیفیوژن په یوه ساده بېلګه ښه ښودل کېدای شي یعنې کله چې د KMnO₄ په څېر رنګین کرسټال د اوبو په بیکر کې واچول شي. ورو ورو یې مالیکولونه په ټولو اوبو کې ټولو لورو ته یو شان خپرېږي او رنګ یو شان وېشل کېږي.')])
    s.callout(IP, [('Construct an experiment to show the diffusion speed in solids, liquids and gases.', 'ٹھوس، مائع اور گیس میں ڈفیوژن کی رفتار دکھانے کے لیے ایک تجربہ ترتیب دیں۔', 'په جامدو، مایعاتو او ګازونو کې د ډیفیوژن د سرعت د ښودلو لپاره یوه تجربه جوړه کړئ.')])
    s.fig('bio4-fig4-20', diffusion_fig(DF_EN), diffusion_fig(DF_UR), diffusion_fig(DF_PS), .65,
          caption=('Figure 4.20: Diffusion and facilitated diffusion', 'شکل 4.20: ڈفیوژن اور فیسلیٹیٹڈ ڈفیوژن', 'شکل 4.20: ډیفیوژن او اسانه شوی ډیفیوژن'))
    s.h('iii. Osmosis', 'iii. اوسموسس', 'iii. اوسموزس')
    s.p('It is the diffusion of solvent (water) through a semi-permeable membrane. It is controlled by the relative concentration of solutes in the water on both sides of membrane. Water always moves from a hypotonic solution (with lower concentration of solutes) to a hypertonic solution (with higher concentration of solutes). Few examples of how osmosis occurs in cells are following:',
        'یہ نیم نفوذ پذیر جھلی کے ذریعے محلل (پانی) کا نفوذ ہے۔ یہ جھلی کے دونوں طرف پانی میں منحل اشیا کے اضافی ارتکاز سے کنٹرول ہوتا ہے۔ پانی ہمیشہ ہائپوٹونک محلول (کم منحل ارتکاز والے) سے ہائپرٹونک محلول (زیادہ منحل ارتکاز والے) کی طرف حرکت کرتا ہے۔ خلیوں میں اوسموسس کی چند مثالیں یہ ہیں:',
        'دا د نیم نفوذ منونکې غشا له لارې د محلل (اوبو) ډیفیوژن دی. دا د غشا په دواړو خواوو کې په اوبو کې د حل شویو موادو په نسبي غلظت کنټرولېږي. اوبه تل له هایپوټونیک محلول (د حل شویو موادو ټیټ غلظت) څخه هایپرټونیک محلول (د حل شویو موادو لوړ غلظت) ته ځي. په حجرو کې د اوسموزس ځینې بېلګې دا دي:')
    s.lines([('(i) When a cell is placed in a hypotonic solution (which has lower solute concentration than the cell) the rate of movement of water inside the cell is more. In such conditions, animal cells swells and may rupture while the plant cells becomes turgid (due to their hard cell wall).',
              '(i) جب خلیے کو ہائپوٹونک محلول (جس میں منحل کا ارتکاز خلیے سے کم ہو) میں رکھا جائے تو خلیے کے اندر پانی کی حرکت کی شرح زیادہ ہوتی ہے۔ ایسے حالات میں جانوروں کے خلیے پھول جاتے ہیں اور پھٹ سکتے ہیں جبکہ پودوں کے خلیے (سخت خلوی دیوار کی وجہ سے) تن جاتے (ٹرجڈ) ہیں۔',
              '(i) کله چې حجره په هایپوټونیک محلول (چې د حل شوي مادې غلظت یې له حجرې کم وي) کې کېښودل شي، حجرې ته د اوبو د ننوتلو کچه زیاته وي. په داسې حالاتو کې د ژویو حجرې پړسېږي او ښايي وشلېږي په داسې حال کې چې د بوټو حجرې (د کلک دېوال له امله) ټینګې کېږي.'),
             ('(ii) When a cell is placed in an isotonic solution (solution in which the concentration of solutes is equal to that of the cell), the rate of osmosis outward is equal to the rate of osmosis to inward. In such a condition, animal cells retain their volume constant while plant cells become flaccid (loose), because the net uptake of water is not enough.',
              '(ii) جب خلیے کو آئسوٹونک محلول (جس میں منحل کا ارتکاز خلیے کے برابر ہو) میں رکھا جائے تو باہر کی طرف اوسموسس کی شرح اندر کی طرف اوسموسس کی شرح کے برابر ہوتی ہے۔ ایسی حالت میں جانوروں کے خلیے اپنا حجم مستقل رکھتے ہیں جبکہ پودوں کے خلیے ڈھیلے (فلیسڈ) ہو جاتے ہیں کیونکہ پانی کی خالص مقدار کافی نہیں ہوتی۔',
              '(ii) کله چې حجره په ایزوټونیک محلول (چې د حل شوي مادې غلظت یې د حجرې سره برابر وي) کې کېښودل شي، بهر ته د اوسموزس کچه دننه ته د اوسموزس له کچې سره برابره وي. په داسې حالت کې د ژویو حجرې خپل حجم ثابت ساتي په داسې حال کې چې د بوټو حجرې سستې (فلاسډ) کېږي ځکه چې د اوبو خالص جذب کافي نه وي.'),
             ('(iii) When a cell is placed in a hypertonic solution (which has higher salt concentration than the cell), water moves out. In such conditions, animal cells shrink in size. In plant cells, the cytoplasm shrinks within the cell wall.',
              '(iii) جب خلیے کو ہائپرٹونک محلول (جس میں نمک کا ارتکاز خلیے سے زیادہ ہو) میں رکھا جائے تو پانی باہر نکلتا ہے۔ ایسے حالات میں جانوروں کے خلیے سکڑ جاتے ہیں۔ پودوں کے خلیوں میں سائٹوپلازم خلوی دیوار کے اندر سکڑ جاتا ہے۔',
              '(iii) کله چې حجره په هایپرټونیک محلول (چې د مالګې غلظت یې له حجرې زیات وي) کې کېښودل شي، اوبه بهر وځي. په داسې حالاتو کې د ژویو حجرې کوچنۍ کېږي. د بوټو په حجرو کې سایټوپلازم د حجرې د دېوال دننه راټولېږي.')])
    s.fig('bio4-fig4-21', osmosis_fig(OS_EN), osmosis_fig(OS_UR), osmosis_fig(OS_PS), .7,
          caption=('Figure 4.21: Effect of different solutions on animal and plant cells', 'شکل 4.21: جانوروں اور پودوں کے خلیوں پر مختلف محلولوں کا اثر', 'شکل 4.21: د ژویو او بوټو پر حجرو د بېلابېلو محلولونو اغېز'))
    out.append(s)
    return out
