# -*- coding: utf-8 -*-
TITLE = 'Greenhouse analogy / Unit 9 key points / projects groups A-B'
KP = [
    ('Heat transfer: The process, in which heat travels from one place to another place because of difference of temperature, is called transfer of heat.', 'حرارت کی منتقلی: وہ عمل جس میں درجۂ حرارت کے فرق کی وجہ سے حرارت ایک جگہ سے دوسری جگہ جاتی ہے۔', 'د تودوخې لېږد: هغه بهیر چې د تودوخې د توپیر له امله تودوخه له یوه ځای بل ته ځي.'),
    ('Conduction of heat: The particle to particle mode of heat transfer by collisions or indirect interaction is called conduction of heat.', 'حرارت کا ایصال: ٹکراؤ یا بالواسطہ تعامل سے ذرے سے ذرے تک حرارت کی منتقلی۔', 'د تودوخې هدایت: د ټکرونو یا غیرمستقیم تعامل له لارې له ذرې ذرې ته د تودوخې لېږد.'),
    ('Thermal conductivity: The thermal conductivity of a substance is a measure of the ability to conduct heat energy.', 'حرارتی ایصالیت: کسی مادے کی حرارتی توانائی منتقل کرنے کی صلاحیت کی پیمائش۔', 'تودوخیز هدایت: د یوې مادې د تودوخیزې انرژۍ د لېږد د وړتیا اندازه.'),
    ('Convection of heat: The transfer of heat from one place to another by the actual motion of the heated substance is called convection of heat.', 'حرارت کا کنویکشن: گرم مادے کی اصل حرکت سے حرارت کی ایک جگہ سے دوسری جگہ منتقلی۔', 'د تودوخې حمل: د تودې مادې د اصلي حرکت له لارې له یوه ځای بل ته د تودوخې لېږد.'),
    ('Convection currents: The currents set up in the process are known as convection currents.', 'کنویکشن رو: اس عمل میں بننے والی رو۔', 'د حمل جریانونه: په دې بهیر کې جوړ شوي جریانونه.'),
    ('Radiation of heat: The heat and energy transfer from a hotter place to a colder place with or without having a material medium in between is called radiation of heat.', 'حرارت کی اشعاع: مادی واسطے کے ساتھ یا بغیر گرم سے ٹھنڈی جگہ تک حرارت کی منتقلی۔', 'د تودوخې وړانګې: له مادي واسطې سره یا پرته له ګرم څخه سړ ځای ته د تودوخې لېږد.'),
    ('Radiant energy: The energy emitted from a hotter place and carried through radiation is called radiant energy.', 'اشعاعی توانائی: گرم جگہ سے خارج ہو کر اشعاع کے ذریعے جانے والی توانائی۔', 'وړانګیزه انرژي: له ګرم ځای خپره شوې او د وړانګو له لارې وړل شوې انرژي.'),
]
PROJ = [
    ('GROUP - A', 'HEAT CONDUCTOR SURFACES', 'Choose a variety of surfaces for your ice to melt on. Compare metal, plastic, glass, and paper to see which makes a better conductor of heat. Explain your finding in form of research and present your findings in classroom.',
     'حرارت کی موصل سطحیں', 'برف پگھلانے کے لیے مختلف سطحیں منتخب کریں۔ دھات، پلاسٹک، شیشہ اور کاغذ کا موازنہ کریں کہ کون سا بہتر موصل ہے۔ اپنے نتائج تحقیق کی صورت میں بیان کر کے جماعت میں پیش کریں۔',
     'د تودوخې هادي سطحې', 'د یخ د ویلې کولو لپاره بېلابېلې سطحې وټاکئ. فلز، پلاستیک، ښیښه او کاغذ پرتله کړئ چې کوم یې ښه هادي دی. موندنې مو د څېړنې په بڼه ولیکئ او په ټولګي کې یې وړاندې کړئ.'),
    ('GROUP - B', 'OIL AND GHEE HEAT CONDUCTION', 'Investigate heat transfer in any cooking process. Does cooking oil or ghee added during cooking increase the heat transfer? Do we require materials that are good conductors of heat transfer for cooking? Demonstrate your results in class in form of a presentation.',
     'تیل اور گھی سے حرارت کا ایصال', 'کسی بھی کھانا پکانے کے عمل میں حرارت کی منتقلی کی تحقیق کریں۔ کیا پکاتے وقت ڈالا گیا تیل یا گھی حرارت کی منتقلی بڑھاتا ہے؟ کیا پکانے کے لیے حرارت کے اچھے موصل مادے چاہییں؟ اپنے نتائج جماعت میں پریزنٹیشن کی صورت میں دکھائیں۔',
     'د تېلو او غوړو له لارې د تودوخې هدایت', 'په هر پخلي کې د تودوخې لېږد وڅېړئ. ایا د پخلي پر مهال اچول شوي تېل یا غوړي د تودوخې لېږد زیاتوي؟ ایا د پخلي لپاره د تودوخې ښو هادیو موادو ته اړتیا ده؟ پایلې مو په ټولګي کې د پرېزنټېشن په بڼه وښایاست.'),
]
ITEMS = []
for g, t, en, tu, ur, tp, ps in PROJ:
    ITEMS += [('h', f'{g}: {t}', f'{g.replace("GROUP", "گروپ")}: {tu}', f'{g.replace("GROUP", "ډله")}: {tp}'), ('p', en, ur, ps)]
SECTIONS = [
    ('9.5.2', ('9.5.2 IMPORTANCE OF GREENHOUSE EFFECT', '9.5.2 گرین ہاؤس اثر کی اہمیت', '9.5.2 د شنې خونې د اغېز اهمیت'), [
        ('p', "The 'greenhouse effect' of the atmosphere is named by analogy to greenhouses (a structure with walls and roof made chiefly of transparent material, such as glass) which become warmer in sunlight. However, a greenhouse is not primarily warmed by the 'greenhouse effect', because 'greenhouse effect' works by preventing absorbed heat from leaving the structure through radiative transfer, while in 'green house' warming is produced mainly by reducing convection of air. Similar effect is also observed in car parked in the hot sun with its windows closed, there is some greenhouse effect but the warming is chiefly achieved through reduction in convection.",
         'فضا کے "گرین ہاؤس اثر" کا نام گرین ہاؤس (ایسی عمارت جس کی دیواریں اور چھت زیادہ تر شیشے جیسے شفاف مادے کی ہوں) کی مناسبت سے رکھا گیا ہے جو دھوپ میں گرم ہو جاتا ہے۔ تاہم گرین ہاؤس بنیادی طور پر "گرین ہاؤس اثر" سے گرم نہیں ہوتا، کیونکہ "گرین ہاؤس اثر" جذب شدہ حرارت کو اشعاعی منتقلی سے باہر جانے سے روک کر کام کرتا ہے جبکہ گرین ہاؤس میں گرمی زیادہ تر ہوا کے کنویکشن کو کم کرنے سے پیدا ہوتی ہے۔ ایسا ہی اثر دھوپ میں بند کھڑکیوں والی کھڑی گاڑی میں دیکھا جاتا ہے؛ وہاں کچھ گرین ہاؤس اثر ہوتا ہے مگر گرمی بنیادی طور پر کنویکشن کم ہونے سے ہوتی ہے۔',
         'د اتموسفیر "د شنې خونې اغېز" د شنو خونو (هغه جوړښت چې دېوالونه او چت یې ډېری له شفافو موادو لکه ښیښې جوړ وي) په ورته والي نومول شوی چې په لمر کې تودېږي. خو شنه خونه اساساً د "شنې خونې اغېز" په واسطه نه تودېږي، ځکه "د شنې خونې اغېز" د جذب شوې تودوخې د وړانګیز لېږد له لارې د وتلو په مخنیوي کار کوي، په داسې حال کې چې په شنه خونه کې تودوخه اساساً د هوا د حمل په کمولو رامنځته کېږي. ورته اغېز په لمر کې د تړلو کړکیو سره ولاړ موټر کې هم لیدل کېږي؛ هلته یو څه د شنې خونې اغېز شته خو تودوخه اساساً د حمل په کمولو ترلاسه کېږي.'),
    ]),
    ('source-u9-key-points', ('KEY POINTS', 'اہم نکات', 'مهم ټکي'), [('ul', KP)]),
    ('source-u9-projects', ('PROJECTS', 'منصوبے', 'پروژې'), ITEMS),
]
EXTRA = dict(activities=[dict(num=f'Project 9 {g[-1]}', name=t, procedure=en, urdu=ur, pashto=ps) for g, t, en, tu, ur, tp, ps in PROJ])
