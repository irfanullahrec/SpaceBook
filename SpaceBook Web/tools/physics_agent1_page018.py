from physics_agent1_sequential import save, render
def tr(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto,translationOrigin='SpaceBook')
paras=[
 tr('ACTIVITY 1.2 ABOUT US','سرگرمی 1.2: ہمارے بارے میں','فعالیت 1.2: زموږ په اړه'),
 tr('Calculate your height in centimeters and meters and your mass (notice that we do not say weight) in kilograms.',
 'اپنا قد سینٹی میٹر اور میٹر میں، اور اپنی کمیت کلوگرام میں معلوم کریں (غور کریں کہ ہم وزن نہیں کہہ رہے)۔',
 'خپل قد په سانتي مترو او مترو، او خپله کتله په کیلوګرامو معلومه کړئ (پام وکړئ چې موږ وزن نه وایو).'),
 tr('CAN YOU TELL? Choose the base physical quantities and derived physical quantities from the following. Temperature, Volume, Time, Area, Density, Length',
 'کیا آپ بتا سکتے ہیں؟ درج ذیل میں سے بنیادی اور ماخوذ طبعی مقداریں منتخب کریں: درجہ حرارت، حجم، وقت، رقبہ، کثافت، لمبائی۔',
 'آیا ویلای شئ؟ له لاندې څخه بنسټیز او مشتق فزیکي کمیتونه وټاکئ: د تودوخې درجه، حجم، وخت، مساحت، کثافت، اوږدوالی.'),
 tr('INFORMATION: The mass of this mosquito can be expressed in different ways: 1 × 10⁻⁵ kg, 0.01 g, or 10 mg.',
 'معلومات: اس مچھر کی کمیت مختلف صورتوں میں ظاہر کی جا سکتی ہے: 1 × 10⁻⁵ کلوگرام، 0.01 گرام یا 10 ملی گرام۔',
 'معلومات: د دې غوماشې کتله په بېلابېلو بڼو څرګندېدای شي: 1 × 10⁻⁵ کیلوګرامه، 0.01 ګرامه یا 10 ملي ګرامه.'),
 tr('Example 1.4 SIZE OF BACTERIUM','مثال 1.4: بیکٹیریا کا سائز','بېلګه 1.4: د باکتریا اندازه'),
 tr('A typical bacterium has a mass of 2.0 fg. Express this measurement in terms of kg.',
 'ایک عام بیکٹیریا کی کمیت 2.0 فیمٹوگرام ہے۔ اس پیمائش کو کلوگرام میں ظاہر کریں۔',
 'د یوې عادي باکتریا کتله 2.0 فېمټوګرامه ده. دا اندازه په کیلوګرامو څرګنده کړئ.'),
 tr('Given mass m = 2.0 fg','دی گئی کمیت m = 2.0 فیمٹوگرام۔','ورکړل شوې کتله m = 2.0 فېمټوګرامه.'),
 tr('We know that femtogram 1 fg = 1 × 10⁻¹⁵ g; kilogram 1 kg = 1 × 10³ g.',
 'ہم جانتے ہیں کہ 1 فیمٹوگرام = 1 × 10⁻¹⁵ گرام؛ اور 1 کلوگرام = 1 × 10³ گرام۔',
 'موږ پوهېږو چې 1 فېمټوګرام = 1 × 10⁻¹⁵ ګرامه؛ او 1 کیلوګرام = 1 × 10³ ګرامه.'),
 tr('m = 2 fg; m = 2 fg = 2 × 10⁻¹⁵ g × (1 kg / (1 × 10³ g)); therefore m = 2 fg = 2 × 10⁻¹⁸ kg — Answer',
 'm = 2 فیمٹوگرام؛ m = 2 × 10⁻¹⁵ گرام × (1 کلوگرام / (1 × 10³ گرام))؛ لہٰذا m = 2 × 10⁻¹⁸ کلوگرام — جواب۔',
 'm = 2 فېمټوګرامه؛ m = 2 × 10⁻¹⁵ ګرامه × (1 کیلوګرام / (1 × 10³ ګرامه))؛ نو m = 2 × 10⁻¹⁸ کیلوګرامه — ځواب.'),
 tr('Tuberculosis is a respiratory disease (infectious) caused by a bacteria known as Mycobacterium tuberculosis.',
 'تپِ دق سانس کی ایک متعدی بیماری ہے، جس کا سبب مائیکوبیکٹیریم ٹیوبرکلوسس نامی بیکٹیریا ہے۔',
 'توبرکلوز د تنفسي سیستم یوه ساري ناروغي ده چې د مایکوباکټریوم توبرکلوسس په نوم باکتریا یې رامنځته کوي.'),
 tr('Assignment 1.4 SMALLEST BIRD','مشق 1.4: سب سے چھوٹا پرندہ','دنده 1.4: تر ټولو کوچنی مرغه'),
 tr('The smallest bird is the bee hummingbird. Males measure only 0.057 m. Convert this number to standard form and write this number in millimetre.',
 'سب سے چھوٹا پرندہ بی ہمنگ برڈ ہے۔ نر کی لمبائی صرف 0.057 میٹر ہوتی ہے۔ اس عدد کو معیاری صورت میں تبدیل کریں اور ملی میٹر میں لکھیں۔',
 'تر ټولو کوچنی مرغه بي همنګبرډ دی. د نر اوږدوالی یوازې 0.057 متره دی. دا عدد معیاري بڼې ته واړوئ او په ملي مترو یې ولیکئ.'),
 tr('Example 1.5 PESHAWAR TO LAHORE VIA MOTORWAY','مثال 1.5: موٹروے کے ذریعے پشاور سے لاہور','بېلګه 1.5: د موټروې له لارې له پېښور څخه لاهور ته'),
 tr('The distance from Peshawar to Lahore through motorway is 489 km, convert this number to megametre (Mm).',
 'موٹروے کے ذریعے پشاور سے لاہور کا فاصلہ 489 کلومیٹر ہے؛ اسے میگامیٹر (Mm) میں تبدیل کریں۔',
 'د موټروې له لارې له پېښور څخه لاهور ته واټن 489 کیلومتره دی؛ دا اندازه مېګامتر (Mm) ته واړوئ.')
]
example=dict(num='1.4',title='SIZE OF BACTERIUM',statement=paras[5]['text'],given='m = 2.0 fg',required='Mass in kg',formula='1 fg = 10⁻¹⁵ g; 1 kg = 10³ g',solution='\n\n'.join(p['text'] for p in paras[6:9]),answer='2 × 10⁻¹⁸ kg',sourcePdfPage=18,sourcePrintedPage=13,solutionOrigin='textbook')
next_example=dict(num='1.5',title='PESHAWAR TO LAHORE VIA MOTORWAY',statement=paras[13]['text'],given='Distance = 489 km',required='Distance in megametre (Mm)',formula='',solution='',answer='',sourcePdfPage=18,sourcePrintedPage=13,solutionStatus='Continues on the immediately following PDF page')
save(dict(pdfPage=18,printedPage=13,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',title='Activity 1.2 / Example 1.4 / Assignment 1.4 / Example 1.5 question',
 activities=[dict(num='Activity 1.2',name='ABOUT US',procedure=paras[1]['text'],urdu=paras[1]['urdu'],pashto=paras[1]['pashto'],sourcePdfPage=18,sourcePrintedPage=13)],numericals=[example,next_example],sections=[dict(code='1.5',heading='1.5 Prefixes to Power of Ten',paras=paras,blocks=[dict(type='formula',latex=r'm=2\times10^{-15}\,\mathrm{g}\times\frac{1\,\mathrm{kg}}{10^3\,\mathrm{g}}=2\times10^{-18}\,\mathrm{kg}'),dict(type='assignment',number='1.4',question=paras[11]['text'])])],comparison='Corrected swapped existing example numbers 1.4/1.5; full printed bacterium solution preserved; all questions and information captions retained as translated text'))
render(19)
