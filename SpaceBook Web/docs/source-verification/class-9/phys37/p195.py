# -*- coding: utf-8 -*-
TITLE = 'Hooke\'s law Eq 7.6 / 7.10 Stress, strain and Young\'s modulus / Eq 7.7, 7.8 / Lab work'
SECTIONS = [
    ('7.9.1-law', ('7.9.1 Hooke’s law (continued)', '7.9.1 ہُک کا قانون (جاری)', '7.9.1 د هوک قانون (دوام)'), [
        ('q', 'within elastic limits the extension (or compression) x is directly proportional to the restoring force F_res, i.e.', 'لچک کی حدود میں لمبائی میں اضافہ (یا کمی) x بحالی قوت F_res کے راست متناسب ہوتا ہے، یعنی', 'د ارتجاع په حدودو کې غځېدنه (یا لنډېدنه) x د بېرته راګرځوونکي قوت F_res سره مستقیم متناسب ده، یعنې'),
        ('eq', None, 'F_{res} ∝ −x'),
        ('eq', 'phys9-u7-eq76', 'or   F_{res} = −kx', '7.6'),
        ('p', 'where k is known as the force constant having units N m^{-1}. The negative sign shows that force is directed against displacement. This relationship is also true for a wire under tension.', 'جہاں k قوت کا مستقل کہلاتا ہے جس کی اکائی N m^{-1} ہے۔ منفی علامت ظاہر کرتی ہے کہ قوت ہٹاؤ کے مخالف سمت میں ہے۔ یہ تعلق کھنچاؤ میں تار کے لیے بھی درست ہے۔', 'چې k د قوت ثابت بلل کېږي او واحد یې N m^{-1} دی. منفي نښه ښيي چې قوت د بې ځایه کېدو پر ضد لوري ته دی. دا اړیکه د کشش لاندې سیم لپاره هم سمه ده.'),
    ]),
    ('7.10', ('7.10 STRESS, STRAIN AND YOUNG’S MODULUS', '7.10 تناؤ، تغیرِ شکل اور ینگ کا معیار', '7.10 فشار، کشش او د ینګ ماډولس'), [
        ('p', 'A wire under tension will extend. Its extension depends on a number of factors such as the tension, its diameter and length and the material of the wire.', 'کھنچاؤ میں تار لمبا ہوگا۔ اس کی لمبائی میں اضافہ کئی عوامل پر منحصر ہے جیسے کھنچاؤ، اس کا قطر اور لمبائی اور تار کا مادہ۔', 'د کشش لاندې سیم غځېږي. غځېدنه یې په څو عواملو پورې اړه لري لکه کشش، قطر او اوږدوالی یې او د سیم ماده.'),
        ('p', 'Suppose that a wire of length l and cross-sectional area ‘A’ is stretched by a force F and the extension produced is x as shown in figure 7.10.', 'فرض کریں کہ لمبائی l اور تراشی رقبہ \'A\' کا ایک تار قوت F سے کھینچا جاتا ہے اور پیدا ہونے والا اضافہ x ہے جیسا کہ شکل 7.10 میں دکھایا گیا ہے۔', 'فرض کړئ چې د l اوږدوالي او \'A\' مقطعي ساحې یو سیم د F قوت په واسطه غځول کېږي او رامنځته شوې غځېدنه x ده لکه په 7.10 شکل کې.'),
        ('fig', 'Figure 7.10 — a cylindrical wire of length l and cross-sectional area A stretched by force F, producing extension x.', 'شکل 7.10 — لمبائی l اور تراشی رقبہ A کا بیلنی تار جو قوت F سے کھینچا گیا اور اضافہ x پیدا ہوا۔', '7.10 شکل — د l اوږدوالي او A مقطعي ساحې استوانه یي سیم چې د F قوت په واسطه غځول شوی او x غځېدنه یې جوړه کړې.'),
        ('h', 'Stress:', 'تناؤ (اسٹریس):', 'فشار (سټرېس):'),
        ('p', 'The stress applied to the wire is defined as the force applied per unit area of cross-section to produce deformation. Mathematically', 'تار پر لگایا گیا تناؤ بگاڑ پیدا کرنے کے لیے فی اکائی تراشی رقبہ لگائی گئی قوت کے طور پر تعریف کیا جاتا ہے۔ ریاضیاتی طور پر', 'پر سیم اچول شوی سټرېس د بدلون د رامنځته کولو لپاره په واحدې مقطعي ساحې اچول شوی قوت تعریف کېږي. په ریاضي ډول'),
        ('eq', None, 'Stress = [[Force|Area of crossection]]'),
        ('eq', 'phys9-u7-eq77', 'or   stress = [[F|A]]', '7.7'),
        ('p', 'The unit for stress is N m^{-2} or pascal.', 'تناؤ کی اکائی N m^{-2} یا پاسکل ہے۔', 'د سټرېس واحد N m^{-2} یا پاسکال دی.'),
        ('h', 'Strain:', 'تغیرِ شکل (اسٹرین):', 'کشش (سټرېن):'),
        ('p', 'As a result of the wire being stretched, it is under strain. The strain is defined as the extension per unit length. Mathematically', 'تار کے کھینچے جانے کے نتیجے میں وہ اسٹرین میں ہوتا ہے۔ اسٹرین کی تعریف فی اکائی لمبائی اضافہ ہے۔ ریاضیاتی طور پر', 'د سیم د غځېدو په پایله کې هغه د سټرېن لاندې وي. سټرېن په واحد اوږدوالي غځېدنه تعریف کېږي. په ریاضي ډول'),
        ('eq', None, 'Strain = [[Extension|Original Length]]'),
        ('eq', 'phys9-u7-eq78', 'or   strain = [[x|l]]', '7.8'),
        ('p', 'Since strain is the ratio of two lengths, it does not have a unit.', 'چونکہ اسٹرین دو لمبائیوں کا نسبت ہے، اس کی کوئی اکائی نہیں۔', 'څرنګه چې سټرېن د دوو اوږدوالیو نسبت دی، واحد نه لري.'),
        ('h', 'LAB WORK', 'لیب ورک', 'لابراتواري کار'),
        ('p', 'To find the density of a liquid using 5 ml syringe (instead of dimity bottle).', '5 ml سرنج کے ذریعے (ڈمٹی بوتل کی بجائے) مائع کی کثافت معلوم کرنا۔', 'د 5 ml سرنج په مرسته (د ډیمیټي بوتل پر ځای) د مایع کثافت معلومول.'),
        ('h', 'Young’s Modulus:', 'ینگ کا معیار:', 'د ینګ ماډولس:'),
        ('p', 'The strain produced in a stretched wire is proportional to the stress within', 'کھنچے ہوئے تار میں پیدا ہونے والا اسٹرین تناؤ کے متناسب ہوتا ہے', 'په غځول شوي سیم کې رامنځته شوی سټرېن د سټرېس سره متناسب دی'),
    ]),
]
