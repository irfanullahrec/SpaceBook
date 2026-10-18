# -*- coding: utf-8 -*-
TITLE = 'Unit 9 projects groups C-E / exercise MCQs 1-5'
PROJ = [
    ('GROUP - C', 'INSULATING MATERIALS', 'Visit the market and find out the materials available for home roof and wall insulation. State the advantages of different materials over the other. Make your own suggestive material that is both good insulator and cost effective. Defend your material in front of class.',
     'حاجز مادے', 'بازار جا کر گھر کی چھت اور دیواروں کی حرارتی حاجزیت کے لیے دستیاب مادے معلوم کریں۔ مختلف مادوں کے ایک دوسرے پر فوائد بیان کریں۔ اپنا ایسا تجویز کردہ مادہ بنائیں جو اچھا حاجز اور سستا ہو اور جماعت کے سامنے اس کا دفاع کریں۔',
     'عایق مواد', 'بازار ته لاړ شئ او د کور د چت او دېوالونو د عایق کولو لپاره شته مواد ومومئ. د بېلابېلو موادو ګټې یو پر بل ووایاست. خپل داسې وړاندیز شوی مواد جوړ کړئ چې ښه عایق او ارزانه وي او د ټولګي مخې ته یې دفاع وکړئ.'),
    ('GROUP - D', 'GLOBAL WARMING', 'Write an essay on how important for us to keep the temperature of earth. What are the consequences of global warming and how we can safely overcome it.',
     'عالمی حدت', 'اس پر مضمون لکھیں کہ زمین کا درجۂ حرارت برقرار رکھنا ہمارے لیے کتنا اہم ہے، عالمی حدت کے نتائج کیا ہیں اور ہم محفوظ طریقے سے اس پر کیسے قابو پا سکتے ہیں۔',
     'نړیواله تودوخه', 'مقاله ولیکئ چې د ځمکې د تودوخې ساتل موږ ته څومره مهم دي، د نړیوالې تودوخې پایلې څه دي او څنګه یې په خوندي ډول مخه نیولای شو.'),
    ('GROUP - E', 'COLOR TEMPERATURE', 'Research books and internet to find how are the temperature measured using the color of hot objects? Write a column for school magazine.',
     'رنگ سے درجۂ حرارت', 'کتابوں اور انٹرنیٹ سے تحقیق کریں کہ گرم اشیا کے رنگ سے درجۂ حرارت کیسے ناپا جاتا ہے۔ اسکول میگزین کے لیے کالم لکھیں۔',
     'د رنګ له مخې تودوخه', 'په کتابونو او انټرنېټ کې وڅېړئ چې د ګرمو شیانو د رنګ په مرسته تودوخه څنګه اندازه کېږي. د ښوونځي مجلې لپاره کالم ولیکئ.'),
]
ORIGIN = 'SpaceBook answer key (the textbook answer key covers assignments and numerical problems only)'
M = [
    ('Which of the following is the best heat conductor?', 'ان میں سے حرارت کا بہترین موصل کون سا ہے؟', 'له دې څخه د تودوخې تر ټولو ښه هادي کوم دی؟', ['aluminum', 'tin', 'iron', 'copper'], 3, 'Copper (390 J m⁻¹ K⁻¹ s⁻¹) conducts better than the other three (Table 9.1).'),
    ('Identical cubes of the following materials are kept in a room at the same temperature. Which will feel coldest by touching them?', 'ان مادوں کے ایک جیسے مکعب ایک کمرے میں ایک ہی درجۂ حرارت پر رکھے ہیں۔ چھونے پر کون سا سب سے ٹھنڈا لگے گا؟', 'د دې موادو ورته مکعبونه په یوه خونه کې په یوه تودوخه ایښودل شوي. په لمس کې کوم تر ټولو سوړ احساسېږي؟', ['Wood', 'Glass', 'Iron', 'Styrofoam'], 2, 'Iron, the best conductor, draws heat from the hand fastest.'),
    ('The transfer of heat by convection is smallest in', 'کنویکشن سے حرارت کی منتقلی سب سے کم کس میں ہوتی ہے', 'د حمل له لارې د تودوخې لېږد په کوم کې تر ټولو لږ دی', ['solids', 'liquids', 'gases', 'none'], 0, 'Convection cannot occur in solids (p.240).'),
    ('One way that heat is transferred from place to place inside the human body is by the flow of blood. Which one of the following heat transfer processes best describes this action of the blood?', 'انسانی جسم میں حرارت کی منتقلی کا ایک طریقہ خون کا بہاؤ ہے۔ خون کے اس عمل کو حرارت کی منتقلی کا کون سا طریقہ بہترین بیان کرتا ہے؟', 'د انسان په بدن کې د تودوخې د لېږد یوه لار د وینې بهیر دی. کوم بهیر د وینې دا عمل ښه بیانوي؟', ['convection', 'conduction', 'radiation', 'none'], 0, 'Heat is carried by the bulk motion of a fluid (blood): convection.'),
    ('The best absorber of radiation is a body whose surface is', 'اشعاع کا بہترین جاذب وہ جسم ہے جس کی سطح ہو', 'د وړانګو تر ټولو ښه جذبوونکی هغه جسم دی چې سطحه یې وي', ['White', 'Grey', 'Dull black', 'Highly polished'], 2, 'Dull black surfaces absorb (and emit) radiation best (p.244-245).'),
]
L = 'ABCD'
ITEMS = []
for g, t, en, tu, ur, tp, ps in PROJ:
    ITEMS += [('h', f'{g}: {t}', f'{g.replace("GROUP", "گروپ")}: {tu}', f'{g.replace("GROUP", "ډله")}: {tp}'), ('p', en, ur, ps)]
MITEMS = [('h', 'EXERCISE', 'مشق', 'تمرین'), ('h', 'MULTIPLE CHOICE QUESTIONS — Choose the best possible answer:', 'کثیر الانتخابی سوالات — بہترین جواب منتخب کریں:', 'څو ځوابیزې پوښتنې — غوره ځواب وټاکئ:')]
for i, (q, u, p, o, a, e) in enumerate(M, 1):
    opts = '   '.join(f'{L[k]}. {x}' for k, x in enumerate(o))
    MITEMS.append(('p', f'{i}. {q}  {opts}', f'{i}. {u}  {opts}', f'{i}. {p}  {opts}'))
SECTIONS = [('source-u9-projects', ('PROJECTS', 'منصوبے', 'پروژې'), ITEMS),
            ('source-u9-exercise-mcqs', ('EXERCISE — MULTIPLE CHOICE QUESTIONS', 'مشق — کثیر الانتخابی سوالات', 'تمرین — څو ځوابیزې پوښتنې'), MITEMS)]
EXTRA = dict(activities=[dict(num=f'Project 9 {g[-1]}', name=t, procedure=en, urdu=ur, pashto=ps) for g, t, en, tu, ur, tp, ps in PROJ])
