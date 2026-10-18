# -*- coding: utf-8 -*-
TITLE = 'Ice box cork / H. soldering / 9.2 Thermal conductivity: factors, equation 9.1, Figure 9.5, Table 9.1 (first part)'
H = ['Substance', 'Thermal conductivity J m⁻¹ K⁻¹ s⁻¹']
R1 = [['Silver', '420'], ['Copper', '390'], ['Gold', '318'], ['Aluminum', '220'], ['brass', '105'], ['Steel iron', '80'], ['lead', '35']]
U1 = ['چاندی', 'تانبا', 'سونا', 'ایلومینیم', 'پیتل', 'فولادی لوہا', 'سیسہ']
P1 = ['سپین زر', 'مس', 'سره زر', 'المونیم', 'پیتل', 'فولادي اوسپنه', 'سرپ']
R2 = [['Steel (stainless)', '14'], ['Ice', '2.2'], ['Concrete brick', '0.84'], ['Glass (average)', '0.8'], ['Water', '0.6'], ['Wood', '0.08-0.16'], ['Cotton', '0.08'], ['Cork', '0.042'], ['Wool', '0.04'], ['Plastic foam', '0.033'], ['Air', '0.023'], ['Styrofoam', '0.010']]
U2 = ['فولاد (زنگ سے پاک)', 'برف', 'کنکریٹ اینٹ', 'شیشہ (اوسط)', 'پانی', 'لکڑی', 'کپاس', 'کارک', 'اون', 'پلاسٹک فوم', 'ہوا', 'اسٹائروفوم']
P2 = ['فولاد (زنګ نه نیوونکی)', 'یخ', 'کانکرېټي خښته', 'ښیښه (منځنۍ)', 'اوبه', 'لرګی', 'پنبه', 'کارک', 'وړۍ', 'پلاستیکي فوم', 'هوا', 'سټایروفوم']
HU, HP = ['مادہ', 'حرارتی ایصالیت J m⁻¹ K⁻¹ s⁻¹'], ['ماده', 'تودوخیز هدایت J m⁻¹ K⁻¹ s⁻¹']
SECTIONS = [
    ('9.1.3', ('9.1.3 PRACTICAL APPLICATIONS OF CONDUCTION OF HEAT', '9.1.3 حرارت کے ایصال کے عملی استعمالات', '9.1.3 د تودوخې د هدایت عملي کارونې'), [
        ('p', 'The cork prevents the flow of out side heat into the box, thus keeping the ice from melting.', 'کارک باہر کی حرارت کو ڈبے میں آنے سے روکتا ہے اور یوں برف پگھلنے سے بچتی ہے۔', 'کارک د بهر تودوخه صندوق ته له ننوتو منع کوي او یخ له ویلې کېدو ساتي.'),
        ('h', 'H. Soldering:', 'H. ٹانکا لگانا:', 'H. لحیم کول:'),
        ('p', 'During soldering objects are in direct contact, such as the soldering iron and the circuit board, heat is transferred by conduction as shown in the figure 9.4 f.', 'ٹانکا لگاتے وقت اشیا جیسے سولڈرنگ آئرن اور سرکٹ بورڈ براہِ راست رابطے میں ہوتی ہیں اور حرارت ایصال سے منتقل ہوتی ہے جیسا کہ شکل 9.4 f میں ہے۔', 'د لحیم کولو پر مهال شیان لکه د لحیم اوسپنه او سرکټ بورډ مستقیم تماس کې وي او تودوخه د هدایت له لارې لېږدول کېږي لکه په 9.4 f شکل کې.'),
        ('fig', 'Figure 9.4 f Soldering.', 'شکل 9.4 f ٹانکا لگانا۔', '9.4 f شکل لحیم کول.'),
    ]),
    ('9.2', ('9.2 THERMAL CONDUCTIVITY', '9.2 حرارتی ایصالیت', '9.2 تودوخیز هدایت'), [
        ('p', 'The thermal conductivity of a substance is a measure of the ability of the substance to conduct heat energy. The rate of flow of heat through a medium depends on a number of factors.', 'کسی مادے کی حرارتی ایصالیت اس کی حرارتی توانائی منتقل کرنے کی صلاحیت کی پیمائش ہے۔ کسی واسطے سے حرارت کے بہاؤ کی شرح کئی عوامل پر منحصر ہے۔', 'د یوې مادې تودوخیز هدایت د تودوخیزې انرژۍ د لېږد د وړتیا اندازه ده. له یوې واسطې د تودوخې د بهیر کچه په څو عواملو پورې اړه لري.'),
        ('p', "For example consider a rod of length 'L', area of cross-section 'A'. Let the hot face of the slab be at temperature T_h and the colder face be at temperature T_c, which means T_h > T_c. The rate of heat flow (Q/t) across the slab depends on the following factors.", "مثلاً لمبائی 'L' اور عمودی تراش کا رقبہ 'A' والی سلاخ لیں۔ سلیب کا گرم رخ T_h اور ٹھنڈا رخ T_c پر ہو یعنی T_h > T_c۔ سلیب کے آر پار حرارت کے بہاؤ کی شرح (Q/t) ان عوامل پر منحصر ہے۔", "د بېلګې په توګه د 'L' اوږدوالي او 'A' مقطع مساحت لرونکې میله په پام کې ونیسئ. د سلیب ګرم مخ په T_h او سړ مخ په T_c کې دی یعنې T_h > T_c. د سلیب له لارې د تودوخې د بهیر کچه (Q/t) په لاندې عواملو پورې اړه لري."),
        ('ul', [('The difference of temperatures T_h − T_c between the two faces of the slab. The greater the temperature difference, the greater is the heat transferred per unit time across the slab.', 'سلیب کے دونوں رخوں کے درجۂ حرارت کا فرق T_h − T_c؛ فرق جتنا زیادہ ہو فی اکائی وقت اتنی زیادہ حرارت منتقل ہوتی ہے۔', 'د سلیب د دواړو مخونو د تودوخې توپیر T_h − T_c؛ توپیر څومره ډېر وي هومره په واحد وخت کې ډېره تودوخه لېږدول کېږي.'),
                ("Length of rod 'L' more the length, the less is the rate of flow of heat through it.", "سلاخ کی لمبائی 'L'؛ لمبائی جتنی زیادہ ہو حرارت کے بہاؤ کی شرح اتنی کم ہوتی ہے۔", "د میلې اوږدوالی 'L'؛ څومره اوږده وي د تودوخې بهیر هومره کم وي."),
                ('The cross-section area (A). Larger cross-sectional area will allow a greater rate of heat flow.', 'عمودی تراش کا رقبہ (A)؛ زیادہ رقبہ حرارت کے بہاؤ کی زیادہ شرح دیتا ہے۔', 'د مقطع مساحت (A)؛ لویه مساحت د تودوخې ډېر بهیر اجازه ورکوي.'),
                ('The nature or material of the slab.', 'سلیب کی نوعیت یا مادہ۔', 'د سلیب طبیعت یا ماده.')]),
        ('p', 'Mathematically,', 'ریاضیاتی طور پر،', 'په ریاضي ډول،'),
        ('eq', 'phys9-u9-eq91', '[[Q|t]] = k × A × [[T_h − T_c|L]]', '9.1'),
        ('fig', 'Figure 9.5 CONDUCTIVITY: a. A bar with cross-sectional area A and length L. b. The bar is placed between two thermal reservoirs with temperatures T_h and T_c (heat Q flows from T_h to T_c).', 'شکل 9.5 ایصالیت: a. عمودی تراش رقبہ A اور لمبائی L والی سلاخ۔ b. سلاخ T_h اور T_c درجۂ حرارت کے دو حرارتی ذخیروں کے درمیان (حرارت Q کا بہاؤ T_h سے T_c کی طرف)۔', '9.5 شکل هدایت: a. د A مقطع مساحت او L اوږدوالي میله. b. میله د T_h او T_c تودوخو دوو تودوخیزو زېرمو ترمنځ (تودوخه Q له T_h څخه T_c ته بهېږي).'),
        ('tab', 'phys9-u9-table91a', 'TABLE 9.1: THERMAL CONDUCTIVITIES OF COMMON SUBSTANCES', H, R1, (HU, [[U1[i], r[1]] for i, r in enumerate(R1)]), (HP, [[P1[i], r[1]] for i, r in enumerate(R1)])),
    ]),
]
EXTRA = dict(tables=[dict(id='phys9-u9-table91', sourceNumber='Table 9.1', title='TABLE 9.1: THERMAL CONDUCTIVITIES OF COMMON SUBSTANCES', headers=H, rows=R1 + R2)],
             definitions=[dict(term='Thermal conductivity', definition='A measure of the ability of a substance to conduct heat energy.', urdu='کسی مادے کی حرارتی توانائی منتقل کرنے کی صلاحیت کی پیمائش۔', pashto='د یوې مادې د تودوخیزې انرژۍ د لېږد د وړتیا اندازه.')])
