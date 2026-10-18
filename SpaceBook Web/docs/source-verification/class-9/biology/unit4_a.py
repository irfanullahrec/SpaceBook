# -*- coding: utf-8 -*-
"""Unit 4 part A — PDF 66-70 (printed 63-67): SLOs, introduction, 4.1 Microscopy."""
from bio9_tools import Section, photo_figure, svg_wrap, txt

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')


def leeuwenhoek_microscope(L):
    """Figure 4.1: flat plate microscope with labelled focus knob, lens and sample holder."""
    b = ['<path d="M40,150 Q20,90 70,60 L230,30 Q290,25 300,70 L310,140 Q300,180 250,180 L80,200 Q50,200 40,150 Z" fill="#c9a66b" stroke="#6d4c41" stroke-width="2"/>']
    b.append('<circle cx="120" cy="120" r="7" fill="#fff" stroke="#3e2723" stroke-width="2"/>')
    b.append('<path d="M128,118 L420,190" stroke="#5d4037" stroke-width="9" stroke-linecap="round"/>')
    b.append('<path d="M140,112 L140,70 M135,70 h12" stroke="#5d4037" stroke-width="5"/>')
    b.append('<path d="M180,125 L195,60 L215,55 L205,128" fill="#8d6e63" stroke="#3e2723"/>')
    b.append('<rect x="410" y="180" width="30" height="18" rx="4" fill="#8d6e63" stroke="#3e2723" transform="rotate(14 425 189)"/>')
    b.append('<path d="M205,55 L240,25" stroke="#333"/>' + txt(244, 22, L['knob'], 13, 'start', 'bold'))
    b.append('<path d="M118,128 L80,230" stroke="#333"/>' + txt(50, 246, L['lens'], 13, 'start', 'bold'))
    b.append('<path d="M140,112 L150,235" stroke="#333"/>' + txt(130, 252, L['holder1'], 13, 'start', 'bold') + txt(130, 268, L['holder2'], 13, 'start', 'bold'))
    return svg_wrap(''.join(b), 470, 280, L['title'])


LM_EN = dict(title='Figure 4.1: Microscope used by Leeuwenhoek', knob='Focus Knob', lens='Lens', holder1='Sample', holder2='Holder')
LM_UR = dict(title='شکل 4.1', knob='فوکس ناب', lens='عدسہ', holder1='نمونہ', holder2='ہولڈر')
LM_PS = dict(title='شکل 4.1', knob='د فوکس تڼۍ', lens='عدسیه', holder1='د نمونې', holder2='ساتونکی')


def onion_and_compound(L):
    """Figure 4.2: onion epidermal cells (left) and compound microscope with labels (right)."""
    b = ['<rect x="5" y="10" width="270" height="200" fill="#f3e5f5" stroke="#8e24aa"/>']
    import random
    random.seed(4)
    for row in range(5):
        y = 20 + row * 38
        x = 5 - (row % 2) * 40
        while x < 275:
            w = 70 + random.randint(-10, 15)
            b.append(f'<rect x="{max(x, 7)}" y="{y}" width="{min(w, 273 - max(x, 7))}" height="34" rx="6" fill="#fafafa" stroke="#7b1fa2" stroke-width="1.5"/>')
            if random.random() < .5:
                b.append(f'<ellipse cx="{max(x, 7) + 15}" cy="{y + 17}" rx="5" ry="4" fill="#ab47bc"/>')
            x += w + 2
    b.append('<path d="M100,230 L80,195 M100,230 L140,190" stroke="#222" stroke-width="1.5"/>' + txt(100, 248, L['onion'], 13, 'middle', 'bold'))
    # compound microscope
    b.append('<path d="M400,215 h120 l-10,-15 h-100 z" fill="#37474f"/>')
    b.append('<path d="M470,200 L470,110 Q470,90 455,85 L430,80" stroke="#37474f" stroke-width="14" fill="none"/>')
    b.append('<rect x="395" y="130" width="70" height="10" fill="#263238"/>')
    b.append('<rect x="420" y="40" width="16" height="48" fill="#455a64" transform="rotate(-25 428 64)"/>')
    b.append('<path d="M405,100 l-6,22 M418,100 l0,24 M430,100 l6,22" stroke="#607d8b" stroke-width="6"/>')
    b.append('<circle cx="485" cy="155" r="12" fill="#263238"/><circle cx="485" cy="155" r="6" fill="#546e7a"/>')
    b.append('<ellipse cx="425" cy="180" rx="12" ry="6" fill="#90a4ae"/>')
    b.append('<path d="M425,50 L350,30" stroke="#222"/>' + txt(300, 28, L['eyepiece'], 12, 'start', 'bold'))
    b.append('<path d="M405,112 L350,95" stroke="#222"/>' + txt(290, 92, L['obj1'], 12, 'start', 'bold') + txt(290, 106, L['obj2'], 12, 'start', 'bold'))
    b.append('<path d="M395,135 L350,140" stroke="#222"/>' + txt(310, 145, L['stage'], 12, 'start', 'bold'))
    b.append('<path d="M413,180 L355,185" stroke="#222"/>' + txt(290, 182, L['light1'], 12, 'start', 'bold') + txt(290, 196, L['light2'], 12, 'start', 'bold'))
    b.append('<path d="M497,155 L530,150" stroke="#222"/>' + txt(533, 148, L['focus1'], 12, 'start', 'bold') + txt(533, 162, L['focus2'], 12, 'start', 'bold'))
    return svg_wrap(''.join(b), 600, 260, L['title'])


OC_EN = dict(title='Figure 4.2: Cells of a layer of onion under microscope (left); A compound microscope (right)', onion='Onion cells', eyepiece='Eyepiece',
             obj1='Objective', obj2='lenses', stage='Stage', light1='Source of light', light2='(illuminator)', focus1='Focus', focus2='knobs')
OC_UR = dict(title='شکل 4.2', onion='پیاز کے خلیات', eyepiece='آئی پیس', obj1='آبجیکٹو', obj2='عدسے', stage='اسٹیج', light1='روشنی کا ذریعہ', light2='(السٹریٹر)', focus1='فوکس', focus2='ناب')
OC_PS = dict(title='شکل 4.2', onion='د پیاز حجرې', eyepiece='آی پیس', obj1='آبجیکټیو', obj2='عدسې', stage='سټېج', light1='د رڼا سرچینه', light2='(روښانوونکی)', focus1='د فوکس', focus2='تڼۍ')


def sections():
    out = []
    s = Section('bio4_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [66, 67])
    s.h('After studying this unit the students will be able to:', 'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې:')
    s.ul([
        ('Explain the concepts of light microscopy and electron microscopy.', 'روشنی اور الیکٹران خوردبینی کے تصورات کی وضاحت کر سکیں۔', 'د رڼا او الکترون مایکروسکوپۍ مفاهیم تشریح کړي.'),
        ('Explain the relationship between developments in imaging technology and the current understanding of the cell.', 'تصویر کشی کی ٹیکنالوجی میں ترقی اور خلیے کی موجودہ سمجھ کے درمیان تعلق کی وضاحت کر سکیں۔', 'د انځور اخیستنې ټکنالوژۍ د پرمختګ او د حجرې د اوسني پوهې ترمنځ اړیکه تشریح کړي.'),
        ('Trace the development of the cell theory: from Aristotle to Hooke, Pasteur, Brown, and Schwann and Schleiden.', 'خلوی نظریے کی ارتقا کا سراغ لگا سکیں: ارسطو سے ہُک، پاسچر، براؤن اور شوان اور شلائیڈن تک۔', 'د حجروي تیورۍ پرمختګ تعقیب کړي: له ارسطو تر هوک، پاسچر، براون او شوان او شلایډن پورې.'),
        ('Rationalize that there are sub-cellular particles, such as viruses and prions, which have some characteristics of living things.', 'دلیل دے سکیں کہ وائرس اور پرائیونز جیسے ذیلی خلوی ذرات موجود ہیں جن میں جانداروں کی کچھ خصوصیات ہیں۔', 'دلیل ورکړي چې فرعي حجروي ذرې لکه ویروسونه او پریونونه شته چې د ژوندیو شیانو ځینې ځانګړتیاوې لري.'),
        ('Construct a time line that traces the development of the cell theory from the first observations by Robert Hooke to our current understanding of cell structure.', 'ایک ٹائم لائن بنا سکیں جو رابرٹ ہُک کے پہلے مشاہدات سے خلیے کی ساخت کی موجودہ سمجھ تک خلوی نظریے کی ترقی کو ظاہر کرے۔', 'یوه مهال وېشه جوړه کړي چې د رابرټ هوک له لومړیو کتنو تر د حجرې د جوړښت اوسني پوهې پورې د حجروي تیورۍ پرمختګ وښيي.'),
        ('Identify the structure and describe in general terms, the functions of the components of plant and animal cell.', 'پودے اور جانور کے خلیے کے اجزا کی ساخت کی شناخت اور ان کے افعال کو عمومی طور پر بیان کر سکیں۔', 'د بوټي او ژوي د حجرې د برخو جوړښت وپېژني او دندې یې په عمومي ډول بیان کړي.'),
        ('Justify how the cells of the leaf system have a variety of specialized structures and functions.', 'ثابت کر سکیں کہ پتے کے نظام کے خلیوں میں مختلف مخصوص ساختیں اور افعال کیسے ہوتے ہیں۔', 'ثابت کړي چې د پاڼې د سیسټم حجرې څنګه بېلابېل ځانګړي جوړښتونه او دندې لري.'),
        ('State the relationship between cell function and cell structure (for absorption- root hair cells; conduction and support xylem vessels and transport of oxygen- red blood cells).', 'خلیے کے فعل اور ساخت کے درمیان تعلق بیان کر سکیں (جذب کے لیے جڑ کے بالوں کے خلیات؛ ترسیل اور سہارے کے لیے زائلم ویسلز اور آکسیجن کی ترسیل کے لیے سرخ خونی خلیات)۔', 'د حجرې د دندې او جوړښت ترمنځ اړیکه بیان کړي (جذب لپاره د ریښې د وېښتانو حجرې؛ لېږد او ملاتړ لپاره د زایلم رګونه او د اکسیجن د لېږد لپاره سرې وینې حجرې).'),
        ('Describe the cell as a functioning open system.', 'خلیے کو ایک فعال کھلے نظام کے طور پر بیان کر سکیں۔', 'حجره د یو فعال خلاص سیسټم په توګه بیان کړي.'),
        ('Determine ways in which various types of cells contribute to the healthy functioning of the human body.', 'وہ طریقے معلوم کر سکیں جن سے مختلف اقسام کے خلیات انسانی جسم کے صحت مند کام میں حصہ ڈالتے ہیں۔', 'هغه لارې معلومې کړي چې بېلابېل ډوله حجرې د انساني بدن په روغ فعالیت کې ونډه اخلي.'),
        ('Assess the capabilities of animal and plant cell types, owing to the presence or absence of chloroplasts and cell wall.', 'کلوروپلاسٹ اور خلوی دیوار کی موجودگی یا عدم موجودگی کی بنا پر جانوروں اور پودوں کے خلیوں کی صلاحیتوں کا جائزہ لے سکیں۔', 'د کلوروپلاسټ او د حجرې دېوال د شتون یا نه شتون له امله د ژوي او بوټي د حجرو وړتیاوې وارزوي.'),
        ('Describe the differences in the structure and function of prokaryotic and eukaryotic cells.', 'پروکیریوٹک اور یوکیریوٹک خلیوں کی ساخت اور افعال کے فرق بیان کر سکیں۔', 'د پروکاریوټیکو او یوکاریوټیکو حجرو د جوړښت او دندې توپیرونه بیان کړي.'),
        ('Assess the capabilities of prokaryotic and eukaryotic cells, owing to the presence or absence of nucleus and mitochondria.', 'مرکزے اور مائٹوکونڈریا کی موجودگی یا عدم موجودگی کی بنا پر پروکیریوٹک اور یوکیریوٹک خلیوں کی صلاحیتوں کا جائزہ لے سکیں۔', 'د هستې او مایټوکونډریا د شتون یا نه شتون له امله د پروکاریوټیکو او یوکاریوټیکو حجرو وړتیاوې وارزوي.'),
        ('Describe cell size and shape as they relate to surface area to volume ratio.', 'خلیے کی جسامت اور شکل کو سطحی رقبے اور حجم کے تناسب کے حوالے سے بیان کر سکیں۔', 'د حجرې اندازه او بڼه د سطحې مساحت او حجم د نسبت په اړه بیان کړي.'),
        ('Explain how surface area to volume ratio limits cell size.', 'وضاحت کر سکیں کہ سطحی رقبے اور حجم کا تناسب خلیے کی جسامت کو کیسے محدود کرتا ہے۔', 'تشریح کړي چې د سطحې مساحت او حجم نسبت څنګه د حجرې اندازه محدودوي.'),
        ('Describe the phenomena of diffusion, facilitated diffusion, osmosis, filtration, active transport, endocytosis and exocytosis.', 'ڈفیوژن، فیسلیٹیٹڈ ڈفیوژن، اوسموسس، فلٹریشن، ایکٹیو ٹرانسپورٹ، اینڈوسائٹوسس اور ایگزوسائٹوسس کے مظاہر بیان کر سکیں۔', 'د ډیفیوژن، اسانه شوي ډیفیوژن، اوسموزس، فلټریشن، فعال لېږد، انډوسایټوزس او اګزوسایټوزس پدیدې بیان کړي.'),
        ('Compare passive transport of matter by diffusion and osmosis with active transport (e.g. diffusion of glucose from intestine to villus epithelium and active transport of Sodium ions from nerve cell to outside)', 'ڈفیوژن اور اوسموسس کے ذریعے مادے کی غیر فعال ترسیل کا ایکٹیو ٹرانسپورٹ سے موازنہ کر سکیں (مثلاً آنت سے ولس اپی تھیلیم میں گلوکوز کا ڈفیوژن اور اعصابی خلیے سے باہر سوڈیم آئنز کی ایکٹیو ٹرانسپورٹ)', 'د ډیفیوژن او اوسموزس له لارې د مادې غیر فعال لېږد له فعال لېږد سره پرتله کړي (لکه له کولمو د ویلس اپیتیلیم ته د ګلوکوز ډیفیوژن او له عصبي حجرې بهر ته د سوډیم ایونونو فعال لېږد)'),
        ('Define turgor and describe its importance.', 'ٹرگر کی تعریف اور اس کی اہمیت بیان کر سکیں۔', 'ټورګر تعریف او اهمیت یې بیان کړي.'),
        ('Describe the phenomena of plasmolysis and explain its relationship with osmosis.', 'پلازمولائسس کا مظہر بیان کر سکیں اور اوسموسس سے اس کے تعلق کی وضاحت کر سکیں۔', 'د پلازمولیزس پدیده بیان کړي او له اوسموزس سره یې اړیکه تشریح کړي.'),
        ('Describe the role of the cell membrane in maintaining equilibrium while exchanging matter.', 'مادے کے تبادلے کے دوران توازن برقرار رکھنے میں خلوی جھلی کا کردار بیان کر سکیں۔', 'د مادې د تبادلې پر مهال د توازن په ساتلو کې د حجرې د غشا رول بیان کړي.'),
        ('Define tissue as the group of similar cells, performing the same function.', 'بافت کی تعریف ایک جیسے خلیوں کے گروہ کے طور پر کر سکیں جو ایک ہی کام انجام دیتے ہیں۔', 'نسج د ورته حجرو د هغې ډلې په توګه تعریف کړي چې یوه دنده ترسره کوي.'),
        ('Describe the major animal tissues (epithelial, connective, muscular and nervous) in terms of their cell specificities, locations and functions', 'جانوروں کی بڑی بافتوں (اپی تھیلیل، کنیکٹیو، عضلاتی اور اعصابی) کو ان کے خلوی خواص، مقامات اور افعال کے لحاظ سے بیان کر سکیں', 'د ژویو لوی نسجونه (اپیتیلیل، نښلوونکي، عضلي او عصبي) د حجروي ځانګړتیاوو، ځایونو او دندو له مخې بیان کړي'),
        ('Describe the major plant tissues i.e. simple tissues (meristematic tissues, permanent tissues) and compound tissues (xylem tissues and phloem tissues) in terms of their cell specificities, locations and functions.', 'پودوں کی بڑی بافتوں یعنی سادہ بافتوں (میرسٹیمیٹک بافتیں، مستقل بافتیں) اور مرکب بافتوں (زائلم اور فلوئم بافتیں) کو ان کے خلوی خواص، مقامات اور افعال کے لحاظ سے بیان کر سکیں۔', 'د بوټو لوی نسجونه یعنې ساده نسجونه (میرسټیمي نسجونه، دایمي نسجونه) او مرکب نسجونه (زایلم او فلویم نسجونه) د حجروي ځانګړتیاوو، ځایونو او دندو له مخې بیان کړي.'),
        ('Relate the function of a particular tissue to its structure and ultimately to the structure and function of the cells constituting it.', 'کسی خاص بافت کے فعل کو اس کی ساخت اور بالآخر اسے بنانے والے خلیوں کی ساخت اور فعل سے جوڑ سکیں۔', 'د یو ځانګړي نسج دنده له جوړښت او په پای کې د جوړوونکو حجرو له جوړښت او دندې سره وتړي.'),
        ('Justify why a colony of cells does not get tissue level of organization, in spite of having many cells', 'ثابت کر سکیں کہ بہت سے خلیات ہونے کے باوجود خلیوں کی کالونی بافت کی سطح کی تنظیم کیوں حاصل نہیں کرتی', 'ثابت کړي چې د حجرو کلوني سره له ډېرو حجرو د نسج کچې تنظیم ولې نه لري'),
    ])
    out.append(s)

    s = Section('bio4_1', '4.1', 'Microscopy', 'خوردبینی (مائیکروسکوپی)', 'مایکروسکوپي', [68, 69, 70])
    s.p('All organisms are made up of cells. The cell is the structural and functional unit of living organisms. The body of unicellular organism is made up of a single cell while the body of multicellular organism is composed of many cells. In this unit, we will study what a cell is actually made of and how they organize to make the bodies of organisms. Before going into the details of cell, we will study the instrument which helps scientists to discover these details i.e. a microscope.',
        'تمام جاندار خلیوں سے بنے ہیں۔ خلیہ جانداروں کی ساختی اور فعلی اکائی ہے۔ یک خلوی جاندار کا جسم ایک خلیے سے جبکہ کثیر خلوی جاندار کا جسم بہت سے خلیوں سے بنا ہوتا ہے۔ اس یونٹ میں ہم مطالعہ کریں گے کہ خلیہ دراصل کس چیز سے بنا ہے اور خلیات کس طرح منظم ہو کر جانداروں کے جسم بناتے ہیں۔ خلیے کی تفصیلات سے پہلے ہم اس آلے کا مطالعہ کریں گے جو سائنس دانوں کو یہ تفصیلات دریافت کرنے میں مدد دیتا ہے یعنی خوردبین۔',
        'ټول ژوندي موجودات له حجرو جوړ دي. حجره د ژوندیو موجوداتو جوړښتي او دندیز واحد دی. د یو حجروي موجود بدن له یوې حجرې او د څو حجروي موجود بدن له ډېرو حجرو جوړ دی. په دې یونټ کې به موږ ولولو چې حجره په اصل کې له څه جوړه ده او حجرې څنګه تنظیمېږي ترڅو د موجوداتو بدنونه جوړ کړي. د حجرې له جزیاتو مخکې به هغه وسیله ولولو چې ساینس پوهانو سره د دې جزیاتو په موندلو کې مرسته کوي یعنې مایکروسکوپ.')
    s.h('4.1 Microscopy', '4.1 خوردبینی', '4.1 مایکروسکوپي')
    s.p('The use of microscope is known as microscopy. The first microscope was developed by Zacharias Janssen, in Holland, in 1595. It was simply a tube with lenses at each end. Its magnification ranged from 3x (3 times) to 9x (9 times).',
        'خوردبین کے استعمال کو مائیکروسکوپی کہتے ہیں۔ پہلی خوردبین زکریاس جانسن نے 1595ء میں ہالینڈ میں بنائی۔ یہ محض ایک نلکی تھی جس کے دونوں سروں پر عدسے لگے تھے۔ اس کی میگنیفکیشن 3x (3 گنا) سے 9x (9 گنا) تک تھی۔',
        'د مایکروسکوپ کارونې ته مایکروسکوپي ویل کېږي. لومړی مایکروسکوپ زکریاس جانسن په 1595 کې په هالنډ کې جوړ کړ. دا یوازې یو نل و چې په دواړو سرونو کې یې عدسې وې. لویوالی یې له 3x (3 چنده) تر 9x (9 چنده) پورې و.')
    s.p('Anton van Leeuwenhoek (1632-1723), a Dutch scientist made a much better microscope and observed small organisms under it. The magnification power of Leeuwenhoek\'s microscope was more than 250x. He is considered to be the first microscopist.',
        'ولندیزی سائنس دان اینٹون وان لیون ہک (1632-1723) نے کہیں بہتر خوردبین بنائی اور اس سے چھوٹے جانداروں کا مشاہدہ کیا۔ لیون ہک کی خوردبین کی میگنیفکیشن 250x سے زیادہ تھی۔ انہیں پہلا مائیکروسکوپسٹ سمجھا جاتا ہے۔',
        'هالنډي ساینس پوه انټون وان لیوونهوک (1632-1723) ډېر ښه مایکروسکوپ جوړ کړ او واړه موجودات یې پرې ولیدل. د لیوونهوک د مایکروسکوپ لویوالی له 250x ډېر و. هغه لومړنی مایکروسکوپ پوه ګڼل کېږي.')
    s.fig('bio4-leeuwenhoek', photo_figure('Anton van Leeuwenhoek', [('', 'Portrait (painting)')], 'Anton van Leeuwenhoek', cols=1),
          photo_figure('Anton van Leeuwenhoek', [('', 'تصویر (پینٹنگ)')], 'اینٹون وان لیون ہک', cols=1),
          photo_figure('Anton van Leeuwenhoek', [('', 'انځور (نقاشي)')], 'انټون وان لیوونهوک', cols=1), .3,
          caption=('Anton van Leeuwenhoek', 'اینٹون وان لیون ہک', 'انټون وان لیوونهوک'))
    s.fig('bio4-fig4-1', leeuwenhoek_microscope(LM_EN), leeuwenhoek_microscope(LM_UR), leeuwenhoek_microscope(LM_PS), .6,
          caption=('Figure 4.1: Microscope used by Leeuwenhoek', 'شکل 4.1: لیون ہک کی استعمال کردہ خوردبین', 'شکل 4.1: هغه مایکروسکوپ چې لیوونهوک کاراوه'))
    s.callout(SI, [('Leeuwenhoek made many discoveries using his microscope. He was the first to see and describe bacteria and other microorganisms in a drop of water.',
                    'لیون ہک نے اپنی خوردبین سے بہت سی دریافتیں کیں۔ وہ پانی کے ایک قطرے میں بیکٹیریا اور دوسرے خرد جانداروں کو دیکھنے اور بیان کرنے والے پہلے شخص تھے۔',
                    'لیوونهوک په خپل مایکروسکوپ ډېر کشفونه وکړل. هغه لومړنی کس و چې د اوبو په یوه څاڅکي کې یې باکتریا او نور مایکرو ژوندي موجودات ولیدل او بیان یې کړل.')])
    s.h('Magnification and Resolution', 'میگنیفکیشن اور ریزولوشن', 'لویوالی او جلا ښودنه (ریزولوشن)')
    s.p('When we see things under a microscope, its image sizes increases many times. The increase in the image size of an object is called magnification. Resolution means the ability of a microscope or any optical instrument to show two objects separately. For example; our eye can differentiate between two points at least 0.1 mm apart. It means that the resolution of human eye is 0.1 mm. Due to lenses, the resolution of microscope is many times greater than the human eye. That is why, we can see minute things clearly through microscope.',
        'جب ہم چیزوں کو خوردبین سے دیکھتے ہیں تو ان کی شبیہ کئی گنا بڑی ہو جاتی ہے۔ کسی شے کی شبیہ کے سائز میں اضافے کو میگنیفکیشن کہتے ہیں۔ ریزولوشن سے مراد خوردبین یا کسی بصری آلے کی دو اشیا کو الگ الگ دکھانے کی صلاحیت ہے۔ مثال کے طور پر، ہماری آنکھ کم از کم 0.1 ملی میٹر کے فاصلے پر دو نقطوں میں فرق کر سکتی ہے۔ اس کا مطلب ہے کہ انسانی آنکھ کا ریزولوشن 0.1 ملی میٹر ہے۔ عدسوں کی وجہ سے خوردبین کا ریزولوشن انسانی آنکھ سے کئی گنا زیادہ ہے۔ اسی لیے ہم خوردبین سے باریک چیزیں صاف دیکھ سکتے ہیں۔',
        'کله چې موږ شیان د مایکروسکوپ لاندې ګورو، د هغو انځور څو چنده لوی کېږي. د یو شي د انځور د اندازې زیاتوالي ته لویوالی (مګنیفیکېشن) ویل کېږي. ریزولوشن یعنې د مایکروسکوپ یا بلې نوري وسیلې وړتیا چې دوه شیان جلا جلا وښيي. د بېلګې په توګه، زموږ سترګه د لږ تر لږه 0.1 ملي متره واټن لرونکو دوو ټکو ترمنځ توپیر کولای شي. د دې معنا دا ده چې د انسان د سترګې ریزولوشن 0.1 ملي متره دی. د عدسو له امله د مایکروسکوپ ریزولوشن د انسان له سترګې څو چنده زیات دی. له همدې امله موږ د مایکروسکوپ له لارې کوچني شیان په روښانه ډول لیدلای شو.')
    s.h('4.1.1 Light Microscope', '4.1.1 روشنی کی خوردبین', '4.1.1 د رڼا مایکروسکوپ')
    s.p('Light microscope uses light to make the image of an object. Light passes through the sample and then through two glass lenses. One lens produces an enlarged image of the sample and the second lens magnifies the image more. After passing through the object and the lenses, the light is projected into the viewer\'s eye where an enlarged and clear image is formed.',
        'روشنی کی خوردبین کسی شے کی شبیہ بنانے کے لیے روشنی استعمال کرتی ہے۔ روشنی نمونے سے اور پھر شیشے کے دو عدسوں سے گزرتی ہے۔ ایک عدسہ نمونے کی بڑی شبیہ بناتا ہے اور دوسرا عدسہ شبیہ کو مزید بڑا کرتا ہے۔ شے اور عدسوں سے گزرنے کے بعد روشنی دیکھنے والے کی آنکھ میں پڑتی ہے جہاں ایک بڑی اور صاف شبیہ بنتی ہے۔',
        'د رڼا مایکروسکوپ د یو شي د انځور جوړولو لپاره رڼا کاروي. رڼا له نمونې او بیا د ښیښې له دوو عدسو تېرېږي. یوه عدسه د نمونې لوی انځور جوړوي او دوهمه عدسه انځور نور لوی کوي. له شي او عدسو تېرېدو وروسته رڼا د کتونکي سترګې ته رسېږي چېرته چې لوی او روښانه انځور جوړېږي.')
    s.callout(SI, [('There are two basic types of light microscopes: Simple microscope uses a single lens for magnification. Compound microscope uses several lenses (at least two) to enhance the magnification of a sample.',
                    'روشنی کی خوردبین کی دو بنیادی اقسام ہیں: سادہ خوردبین بڑا کرنے کے لیے ایک عدسہ استعمال کرتی ہے۔ مرکب خوردبین نمونے کو مزید بڑا کرنے کے لیے کئی عدسے (کم از کم دو) استعمال کرتی ہے۔',
                    'د رڼا مایکروسکوپ دوه بنسټیز ډولونه لري: ساده مایکروسکوپ د لویولو لپاره یوه عدسه کاروي. مرکب مایکروسکوپ د نمونې د لا لویولو لپاره څو عدسې (لږ تر لږه دوه) کاروي.')])
    s.p('The magnification of a light microscope is 1500X. Its resolving power is 0.2 micrometer (μm) and 1μm = 1/1000 mm. In other words, the light microscope cannot distinguish objects smaller than 0.2 μm.',
        'روشنی کی خوردبین کی میگنیفکیشن 1500X ہے۔ اس کی ریزولونگ پاور 0.2 مائیکرو میٹر (μm) ہے اور 1μm = 1/1000 ملی میٹر۔ دوسرے الفاظ میں روشنی کی خوردبین 0.2 μm سے چھوٹی اشیا میں فرق نہیں کر سکتی۔',
        'د رڼا مایکروسکوپ لویوالی 1500X دی. د جلا ښودنې ځواک یې 0.2 مایکرومتره (μm) دی او 1μm = 1/1000 ملي متره. په بل عبارت، د رڼا مایکروسکوپ له 0.2 μm کوچني شیان نه شي جلا کولای.')
    s.fig('bio4-fig4-2', onion_and_compound(OC_EN), onion_and_compound(OC_UR), onion_and_compound(OC_PS), .9,
          caption=('Figure 4.2: Cells of a layer of onion under microscope (left); A compound microscope (right)', 'شکل 4.2: خوردبین کے نیچے پیاز کی تہ کے خلیات (بائیں)؛ مرکب خوردبین (دائیں)', 'شکل 4.2: د مایکروسکوپ لاندې د پیاز د یوه پوړ حجرې (کیڼ)؛ مرکب مایکروسکوپ (ښي)'))
    s.h('4.1.2 Electron Microscope', '4.1.2 الیکٹران خوردبین', '4.1.2 الکترون مایکروسکوپ')
    s.p('In an electron microscope, a beam of electrons is used. Magnetic lenses focus the electron beam on a screen or photographic film and make much enlarged image. Its resolving power is much greater than the light microscope. It can distinguish objects as small as 0.2 nanometer (nm) and 1 nm = 1/1000,000 mm. There are two types of electron microscopes.',
        'الیکٹران خوردبین میں الیکٹرانز کی شعاع استعمال ہوتی ہے۔ مقناطیسی عدسے الیکٹران کی شعاع کو اسکرین یا فوٹوگرافک فلم پر مرکوز کرتے ہیں اور بہت بڑی شبیہ بناتے ہیں۔ اس کی ریزولونگ پاور روشنی کی خوردبین سے بہت زیادہ ہے۔ یہ 0.2 نینو میٹر (nm) جتنی چھوٹی اشیا میں فرق کر سکتی ہے اور 1 nm = 1/1000,000 ملی میٹر۔ الیکٹران خوردبین کی دو اقسام ہیں۔',
        'په الکترون مایکروسکوپ کې د الکترونونو وړانګه کارول کېږي. مقناطیسي عدسې د الکترون وړانګه پر پرده یا عکاسي فلم متمرکزوي او ډېر لوی انځور جوړوي. د جلا ښودنې ځواک یې له رڼا مایکروسکوپ ډېر زیات دی. دا تر 0.2 نانومتره (nm) پورې کوچني شیان جلا کولای شي او 1 nm = 1/1000,000 ملي متره. الکترون مایکروسکوپونه دوه ډوله دي.')
    s.p('(i) Transmission Electron Microscope (TEM) is used to view the internal cell structure. It can magnify objects about 250,000 times.',
        '(i) ٹرانسمیشن الیکٹران مائیکروسکوپ (TEM) خلیے کی اندرونی ساخت دیکھنے کے لیے استعمال ہوتی ہے۔ یہ اشیا کو تقریباً 2,50,000 گنا بڑا کر سکتی ہے۔',
        '(i) لېږدونکی الکترون مایکروسکوپ (TEM) د حجرې د داخلي جوړښت د لیدو لپاره کارول کېږي. دا شیان شاوخوا 250,000 چنده لویولای شي.')
    s.p('(ii) Scanning Electron Microscope (SEM) is used to study the details of surfaces of cells or any other objects. The surfaces are coated with metal. When electrons beam hits the metal, it is reflected and makes the enlarged image.',
        '(ii) اسکیننگ الیکٹران مائیکروسکوپ (SEM) خلیوں یا کسی دوسری شے کی سطحوں کی تفصیلات کے مطالعے کے لیے استعمال ہوتی ہے۔ سطحوں پر دھات کی تہ چڑھائی جاتی ہے۔ جب الیکٹران کی شعاع دھات سے ٹکراتی ہے تو منعکس ہو کر بڑی شبیہ بناتی ہے۔',
        '(ii) سکېنینګ الکترون مایکروسکوپ (SEM) د حجرو یا نورو شیانو د سطحو د جزیاتو د مطالعې لپاره کارول کېږي. سطحې په فلز پوښل کېږي. کله چې د الکترون وړانګه فلز ته ورسېږي، منعکسېږي او لوی انځور جوړوي.')
    s.fig('bio4-fig4-3', photo_figure('Figure 4.3', [('left', 'TEM view of an animal cell'), ('right', 'SEM view of red blood cells')], 'Electron micrographs in the book'),
          photo_figure('Figure 4.3', [('بائیں', 'جانور کے خلیے کا TEM منظر'), ('دائیں', 'سرخ خونی خلیوں کا SEM منظر')], 'کتاب میں الیکٹران مائیکروگراف'),
          photo_figure('Figure 4.3', [('کیڼ', 'د ژوي د حجرې TEM منظره'), ('ښي', 'د سرو وینې حجرو SEM منظره')], 'په کتاب کې الکترون مایکروګرافونه'), .6,
          caption=('Figure 4.3: TEM view of an animal cell (left); SEM view of red blood cells (right)', 'شکل 4.3: جانور کے خلیے کا TEM منظر (بائیں)؛ سرخ خونی خلیوں کا SEM منظر (دائیں)', 'شکل 4.3: د ژوي د حجرې TEM منظره (کیڼ)؛ د سرو وینې حجرو SEM منظره (ښي)'))
    s.table('bio4-tab4-1', ['', 'Light Microscope', 'Electron Microscope'],
            [['Radiation Type', 'Light', 'Beams of electrons'], ['Lenses', 'Optical', 'Magnetic'],
             ['Magnification', '10,000 times greater than the naked eye', '100 times greater than light microscope'],
             ['Resolution', '500 times of the naked eye', '400 times of the light microscope'], ['Images', '2D images', 'TEM shows 2D while SEM shows 3D images']],
            ['', 'روشنی کی خوردبین', 'الیکٹران خوردبین'],
            [['شعاع کی قسم', 'روشنی', 'الیکٹرانز کی شعاعیں'], ['عدسے', 'بصری', 'مقناطیسی'],
             ['میگنیفکیشن', 'کھلی آنکھ سے 10,000 گنا زیادہ', 'روشنی کی خوردبین سے 100 گنا زیادہ'],
             ['ریزولوشن', 'کھلی آنکھ کا 500 گنا', 'روشنی کی خوردبین کا 400 گنا'], ['شبیہیں', '2D شبیہیں', 'TEM دو جہتی جبکہ SEM سہ جہتی شبیہیں دکھاتی ہے']],
            ['', 'د رڼا مایکروسکوپ', 'الکترون مایکروسکوپ'],
            [['د وړانګې ډول', 'رڼا', 'د الکترونونو وړانګې'], ['عدسې', 'نوري', 'مقناطیسي'],
             ['لویوالی', 'له سترګې 10,000 چنده زیات', 'له رڼا مایکروسکوپ 100 چنده زیات'],
             ['ریزولوشن', 'د سترګې 500 چنده', 'د رڼا مایکروسکوپ 400 چنده'], ['انځورونه', '2D انځورونه', 'TEM دوه بعدي او SEM درې بعدي انځورونه ښيي']],
            ratio=.95, caption=('Table 4.1: Comparison between light and electron microscope', 'جدول 4.1: روشنی اور الیکٹران خوردبین کا موازنہ', 'جدول 4.1: د رڼا او الکترون مایکروسکوپ پرتله'))
    s.p('SpaceBook note: Table 4.1 gives light-microscope magnification as 10,000 times the naked eye, while the text on page 66 gives 1500X. Both are kept as printed.',
        'اسپیس بک نوٹ: جدول 4.1 میں روشنی کی خوردبین کی میگنیفکیشن کھلی آنکھ سے 10,000 گنا دی گئی ہے جبکہ صفحہ 66 کے متن میں 1500X ہے۔ دونوں قدریں جیسی چھپی ہیں رکھی گئی ہیں۔',
        'د سپېس بوک یادونه: جدول 4.1 د رڼا مایکروسکوپ لویوالی له سترګې 10,000 چنده ښيي، په داسې حال کې چې د 66 پاڼې متن 1500X وايي. دواړه لکه چې چاپ شوي ساتل شوي.', editorial=True)
    out.append(s)
    return out
