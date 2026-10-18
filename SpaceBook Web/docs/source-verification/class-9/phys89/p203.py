# -*- coding: utf-8 -*-
TITLE = 'Thermodynamics introduction / 8.1 Temperature / internal energy begins'
SECTIONS = [
    ('source-u8-introduction', ('Introduction', 'تعارف', 'سریزه'), [
        ('p', 'The study of heat transformations into other forms of energy, called thermodynamics, began with the eighteenth-century engineers who built the first steam engines. These steam engines were used to power trains, factories, and water pumps for coal mines, and thus they contributed greatly to the Industrial Revolution. Although the study of thermodynamics began in the eighteenth century, it was not until around 1900 that the concepts of thermodynamics were linked to the motions of atoms and molecules in solids, liquids, and gases.',
         'حرارت کی توانائی کی دوسری شکلوں میں تبدیلی کا مطالعہ، جسے حرحرکیات (تھرموڈائنامکس) کہتے ہیں، اٹھارویں صدی کے ان انجینئروں سے شروع ہوا جنہوں نے پہلے بھاپ کے انجن بنائے۔ یہ بھاپ کے انجن ریل گاڑیاں، کارخانے اور کوئلے کی کانوں کے پانی کے پمپ چلانے میں استعمال ہوئے اور یوں صنعتی انقلاب میں بہت بڑا حصہ ڈالا۔ اگرچہ حرحرکیات کا مطالعہ اٹھارویں صدی میں شروع ہوا، لیکن تقریباً 1900ء تک اس کے تصورات کو ٹھوس، مائع اور گیس میں ایٹموں اور سالمات کی حرکت سے نہیں جوڑا گیا۔',
         'د تودوخې پر نورو انرژیو د بدلېدو مطالعه، چې ترمودینامیک بلل کېږي، د اتلسمې پېړۍ له هغو انجنیرانو پیل شوه چې لومړني بخاري انجنونه یې جوړ کړل. دا بخاري انجنونه د اورګاډو، فابریکو او د ډبرو سکرو د کانونو د اوبو پمپونو چلولو ته کارېدل او په دې توګه یې صنعتي انقلاب ته لویه ونډه ورکړه. که څه هم د ترمودینامیک مطالعه په اتلسمه پېړۍ کې پیل شوه، خو شاوخوا تر ۱۹۰۰ کال پورې یې مفاهیم په جامدو، مایعاتو او ګازونو کې د اتومونو او مالیکولونو له حرکت سره ونه تړل شول.'),
        ('p', 'Today, the concepts of thermodynamics are widely used in various applications that involve heat and temperature. Engineers use the laws of thermodynamics to continually develop higher performance refrigerators, automobile engines, aircraft engines, and numerous other machines.',
         'آج حرحرکیات کے تصورات حرارت اور درجۂ حرارت سے متعلق مختلف استعمالات میں وسیع پیمانے پر استعمال ہوتے ہیں۔ انجینئر حرحرکیات کے قوانین سے مسلسل بہتر کارکردگی والے ریفریجریٹر، گاڑیوں کے انجن، ہوائی جہازوں کے انجن اور بہت سی دوسری مشینیں تیار کرتے ہیں۔',
         'نن ورځ د ترمودینامیک مفاهیم په هغو بېلابېلو کارونو کې پراخه کارول کېږي چې تودوخه او د تودوخې درجه پکې شامله ده. انجنیران د ترمودینامیک قوانین کاروي ترڅو په دوامداره توګه ښه کارکړدګي لرونکي یخچالونه، د موټرو انجنونه، د الوتکو انجنونه او نور ډېر ماشینونه جوړ کړي.'),
    ]),
    ('8.1', ('8.1 TEMPERATURE', '8.1 درجۂ حرارت', '8.1 د تودوخې درجه'), [
        ('p', 'Temperature is a concept we all understand from experience. Even as small children we learn to perceive hotness and coldness of objects. We hear weather forecasters tell us that the temperature will be 32 °C today. We hear doctors tell us that our body temperature is 98.6 °F. We know from General Science for class 8, unit 9: SOURCES AND EFFECTS OF HEAT ENERGY, that temperature is defined as',
         'درجۂ حرارت ایسا تصور ہے جسے ہم سب تجربے سے سمجھتے ہیں۔ چھوٹے بچے بھی اشیا کی گرمی اور ٹھنڈک محسوس کرنا سیکھ لیتے ہیں۔ ہم موسم کی پیش گوئی کرنے والوں سے سنتے ہیں کہ آج درجۂ حرارت 32 °C ہوگا۔ ڈاکٹر بتاتے ہیں کہ ہمارے جسم کا درجۂ حرارت 98.6 °F ہے۔ جماعت ہشتم کی جنرل سائنس، یونٹ 9: حرارتی توانائی کے ذرائع اور اثرات سے ہم جانتے ہیں کہ درجۂ حرارت کی تعریف یوں ہے:',
         'د تودوخې درجه هغه مفهوم دی چې موږ ټول یې له تجربې پوهېږو. حتی کوچني ماشومان هم د شیانو ګرمي او سړښت احساسول زده کوي. موږ له هوا وړاندوینه کوونکو اورو چې نن به د تودوخې درجه 32 °C وي. ډاکټران راته وايي چې زموږ د بدن تودوخه 98.6 °F ده. د اتم ټولګي له عمومي ساینس، 9 څپرکي: د تودوخیزې انرژۍ سرچینې او اغېزې څخه پوهېږو چې د تودوخې درجه داسې تعریفېږي:'),
        ('q', "'the measure of the degree of hotness or coldness of a body with respect to some standard'.",
         "'کسی معیار کے لحاظ سے کسی جسم کی گرمی یا ٹھنڈک کے درجے کی پیمائش'۔",
         "'د یوه معیار په پرتله د یوه جسم د ګرمۍ یا سړښت د درجې اندازه'."),
        ('p', 'Temperature is measured in °C, °F, and K. Here we would extend our understanding of temperature on the basis of kinetic molecular theory. According to this theory atoms and molecules are in continuous random motion. According to this theory, the temperature can also be defined as:',
         'درجۂ حرارت °C، °F اور K میں ناپا جاتا ہے۔ یہاں ہم سالماتی حرکی نظریے کی بنیاد پر درجۂ حرارت کی سمجھ کو وسعت دیں گے۔ اس نظریے کے مطابق ایٹم اور سالمات مسلسل بے ترتیب حرکت میں رہتے ہیں۔ اسی نظریے کے مطابق درجۂ حرارت کی تعریف یوں بھی کی جا سکتی ہے:',
         'د تودوخې درجه په °C، °F او K اندازه کېږي. دلته به د مالیکولي حرکي تیورۍ پر بنسټ د تودوخې د درجې پوهه پراخه کړو. د دې تیورۍ له مخې اتومونه او مالیکولونه په دوامداره ګډوډ حرکت کې دي. د همدې تیورۍ له مخې د تودوخې درجه داسې هم تعریفېدای شي:'),
        ('q', "'The average kinetic energy of molecules of a body'.", "'کسی جسم کے سالمات کی اوسط حرکی توانائی'۔", "'د یوه جسم د مالیکولونو منځنۍ حرکي انرژي'."),
        ('h', 'INFORMATION', 'معلومات', 'معلومات'),
        ('fig', 'Death Valley, California: The hottest place on Earth, in summer temperature reach to 56 °C.', 'ڈیتھ ویلی، کیلیفورنیا: زمین کا گرم ترین مقام، گرمیوں میں درجۂ حرارت 56 °C تک پہنچ جاتا ہے۔', 'ډېت ویلي، کالیفورنیا: د ځمکې تر ټولو ګرم ځای، په اوړي کې تودوخه 56 °C ته رسېږي.'),
        ('fig', 'The Antarctic: During the continuous darkness of mid-winter, the temperature here can be as low as -87 °C.', 'انٹارکٹکا: وسط سرما کی مسلسل تاریکی میں یہاں درجۂ حرارت -87 °C تک گر سکتا ہے۔', 'انټارکټیکا: د ژمي د منځ په دوامداره تیاره کې دلته تودوخه تر -87 °C پورې ټیټېدای شي.'),
        ('h', 'Internal Energy and Temperature:', 'اندرونی توانائی اور درجۂ حرارت:', 'داخلي انرژي او د تودوخې درجه:'),
        ('p', 'Internal energy is the sum of the kinetic and potential energies associated with the motion of the atoms of the substance. For example, in a gas made up of',
         'اندرونی توانائی کسی مادے کے ایٹموں کی حرکت سے وابستہ حرکی اور مخفی توانائیوں کا مجموعہ ہے۔ مثال کے طور پر، ایسی گیس میں جو',
         'داخلي انرژي د یوې مادې د اتومونو له حرکت سره تړلې د حرکي او پټې انرژیو مجموعه ده. د بېلګې په توګه، په داسې ګاز کې چې له'),
    ]),
]
EXTRA = dict(definitions=[
    dict(term='Temperature', definition="The measure of the degree of hotness or coldness of a body with respect to some standard. (Kinetic molecular theory: the average kinetic energy of molecules of a body.)",
         urdu='کسی معیار کے لحاظ سے جسم کی گرمی یا ٹھنڈک کے درجے کی پیمائش (سالماتی نظریہ: جسم کے سالمات کی اوسط حرکی توانائی)۔',
         pashto='د یوه معیار په پرتله د جسم د ګرمۍ یا سړښت د درجې اندازه (مالیکولي تیوري: د جسم د مالیکولونو منځنۍ حرکي انرژي).'),
    dict(term='Internal energy', definition='The sum of the kinetic and potential energies associated with the motion of the atoms of the substance.',
         urdu='کسی مادے کے ایٹموں کی حرکت سے وابستہ حرکی اور مخفی توانائیوں کا مجموعہ۔', pashto='د مادې د اتومونو له حرکت سره تړلې د حرکي او پټې انرژیو مجموعه.'),
])
