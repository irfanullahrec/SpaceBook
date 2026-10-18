# -*- coding: utf-8 -*-
"""Unit 2 part A — PDF 29-34 (printed 23-25, 27-29). Printed page 26 is missing from every local PDF copy."""
from bio9_tools import Section, pair

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')
GAP = ('[Source gap] Printed page 26 is missing from the scanned textbook (PDF page 31 is printed page 25 and PDF page 32 is printed page 27). Its text is not reproduced here. The lesson resumes with observation iii of the malaria problem.',
       '[ماخذ میں خلا] چھپا ہوا صفحہ 26 اسکین شدہ نصابی کتاب میں موجود نہیں (PDF صفحہ 31 چھپا ہوا صفحہ 25 اور PDF صفحہ 32 چھپا ہوا صفحہ 27 ہے)۔ اس کا متن یہاں شامل نہیں کیا گیا۔ سبق ملیریا کے مسئلے کے مشاہدہ iii سے دوبارہ شروع ہوتا ہے۔',
       '[په سرچینه کې تشه] چاپ شوې پاڼه 26 په سکن شوي درسي کتاب کې نشته (PDF پاڼه 31 چاپ شوې پاڼه 25 او PDF پاڼه 32 چاپ شوې پاڼه 27 ده). د هغې متن دلته نه دی راوړل شوی. لوست د ملاریا د ستونزې له iii کتنې بیا پیلېږي.')


def sections():
    out = []
    s = Section('bio2_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [29])
    s.h('After studying this unit, the students will be able to:', 'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې:')
    s.ul([
        ('Describe the steps involved in biological method i.e. recognition of a biological problems, observation and identification, building up hypothesis, drawing deductions, devising experiments and inferring results (malaria as an example).',
         'حیاتیاتی طریقے کے مراحل بیان کر سکیں یعنی حیاتیاتی مسئلے کی شناخت، مشاہدہ اور شناخت، مفروضہ قائم کرنا، استنباط اخذ کرنا، تجربات وضع کرنا اور نتائج اخذ کرنا (ملیریا بطور مثال)۔',
         'د بیولوژیکي میتود پړاوونه بیان کړي یعنې د بیولوژیکي ستونزې پېژندنه، کتنه او پېژندنه، فرضیه جوړول، استنتاج اخیستل، تجربې طرح کول او پایلې اخیستل (ملاریا د بېلګې په توګه).'),
        ('Describe the use of ratio and proportion in solving biological problems.',
         'حیاتیاتی مسائل کے حل میں نسبت اور تناسب کا استعمال بیان کر سکیں۔',
         'د بیولوژیکي ستونزو په حل کې د نسبت او تناسب کارونه بیان کړي.'),
        ('Explain the importance of data analysis for confirming, modifying or rejecting a hypothesis.',
         'مفروضے کی تصدیق، ترمیم یا رد کرنے کے لیے ڈیٹا کے تجزیے کی اہمیت کی وضاحت کر سکیں۔',
         'د فرضیې د تایید، تعدیل یا ردولو لپاره د معلوماتو د شننې اهمیت تشریح کړي.'),
        ('Justify mathematics as an integral part of the scientific process.',
         'ریاضی کو سائنسی عمل کا لازمی جز ثابت کر سکیں۔',
         'ریاضي د ساینسي پروسې د اړین جز په توګه ثابته کړي.'),
    ])
    out.append(s)

    s = Section('bio2_1', '2.1', 'Biological Method', 'حیاتیاتی طریقہ', 'بیولوژیکي میتود', [30, 31])
    s.p('In the previous unit, you have come to know that science is the study of the world through observation and experiment. You also know that in biology, we study the living organisms in detail. The most important feature of biology and other sciences is the problem-solving approach called the scientific method. The scientific method, in which biological problems are solved, is termed as biological method. In this unit, you will study the different steps involved in scientific or biological method.',
        'پچھلے یونٹ میں آپ نے جانا کہ سائنس مشاہدے اور تجربے کے ذریعے دنیا کا مطالعہ ہے۔ آپ یہ بھی جانتے ہیں کہ حیاتیات میں ہم جانداروں کا تفصیل سے مطالعہ کرتے ہیں۔ حیاتیات اور دوسری سائنسوں کی سب سے اہم خصوصیت مسئلہ حل کرنے کا طریقہ ہے جسے سائنسی طریقہ کہتے ہیں۔ وہ سائنسی طریقہ جس سے حیاتیاتی مسائل حل کیے جاتے ہیں، حیاتیاتی طریقہ کہلاتا ہے۔ اس یونٹ میں آپ سائنسی یا حیاتیاتی طریقے کے مختلف مراحل کا مطالعہ کریں گے۔',
        'په تېر یونټ کې تاسو پوه شوئ چې ساینس د کتنې او تجربې له لارې د نړۍ مطالعه ده. تاسو دا هم پوهېږئ چې په بیولوژي کې موږ ژوندي موجودات په تفصیل سره مطالعه کوو. د بیولوژي او نورو ساینسونو تر ټولو مهمه ځانګړتیا د ستونزې د حل لاره ده چې ساینسي میتود بلل کېږي. هغه ساینسي میتود چې بیولوژیکي ستونزې پرې حلېږي، بیولوژیکي میتود بلل کېږي. په دې یونټ کې به تاسو د ساینسي یا بیولوژیکي میتود بېلابېل پړاوونه مطالعه کړئ.')
    s.h('2.1 Biological Method', '2.1 حیاتیاتی طریقہ', '2.1 بیولوژیکي میتود')
    s.p('In biological studies or researches, biologists recognize some biological problem and attempt to find its solution. For solving a biological problem, biologists take the following steps.',
        'حیاتیاتی مطالعات یا تحقیقات میں ماہرینِ حیاتیات کسی حیاتیاتی مسئلے کو پہچانتے ہیں اور اس کا حل تلاش کرنے کی کوشش کرتے ہیں۔ حیاتیاتی مسئلہ حل کرنے کے لیے ماہرینِ حیاتیات درج ذیل مراحل اختیار کرتے ہیں۔',
        'په بیولوژیکي مطالعو یا څېړنو کې بیولوژیستان یوه بیولوژیکي ستونزه پېژني او د هغې د حل هڅه کوي. د بیولوژیکي ستونزې د حل لپاره بیولوژیستان لاندې پړاوونه اخلي.')
    s.ol([('i. Recognition of biological problem', 'i. حیاتیاتی مسئلے کی شناخت', 'i. د بیولوژیکي ستونزې پېژندنه'),
          ('ii. Observations and previous research', 'ii. مشاہدات اور سابقہ تحقیق', 'ii. کتنې او پخوانۍ څېړنه'),
          ('iii. Hypothesis', 'iii. مفروضہ', 'iii. فرضیه'),
          ('iv. Deductions', 'iv. استنباط', 'iv. استنتاجونه'),
          ('v. Experiments', 'v. تجربات', 'v. تجربې'),
          ('vi. Conclusions and reporting', 'vi. نتائج اور رپورٹنگ', 'vi. پایلې او راپور ورکول')])
    s.h('i) Recognition of biological problem', 'i) حیاتیاتی مسئلے کی شناخت', 'i) د بیولوژیکي ستونزې پېژندنه')
    s.p('Recognition of a biological problem begins with the formulation of a question relating to the problem. For example, what are the risk factors for lung cancer?',
        'حیاتیاتی مسئلے کی شناخت مسئلے سے متعلق ایک سوال وضع کرنے سے شروع ہوتی ہے۔ مثال کے طور پر، پھیپھڑوں کے کینسر کے خطرے کے عوامل کیا ہیں؟',
        'د بیولوژیکي ستونزې پېژندنه له ستونزې سره د اړوندې پوښتنې په جوړولو پیلېږي. د بېلګې په توګه، د سږو د سرطان د خطر عوامل کوم دي؟')
    s.h('ii) Observations and previous research', 'ii) مشاہدات اور سابقہ تحقیق', 'ii) کتنې او پخوانۍ څېړنه')
    s.p('After recognizing the biological problem, the biologist makes observations which can help him in finding a solutions. He also recalls his old observations and also studies previous researches on the same problem.',
        'حیاتیاتی مسئلہ پہچاننے کے بعد ماہرِ حیاتیات ایسے مشاہدات کرتا ہے جو حل تلاش کرنے میں اس کی مدد کر سکیں۔ وہ اپنے پرانے مشاہدات بھی یاد کرتا ہے اور اسی مسئلے پر سابقہ تحقیقات کا مطالعہ بھی کرتا ہے۔',
        'د بیولوژیکي ستونزې له پېژندلو وروسته بیولوژیست داسې کتنې کوي چې د حل په موندلو کې ورسره مرسته وکړي. هغه خپلې پخوانۍ کتنې هم رایادوي او په همدې ستونزه پخوانۍ څېړنې هم لولي.')
    s.p('Observations are made with five senses i.e. vision, hearing, smell, taste and touch. There are two types of observations i.e. qualitative and quantitative. Quantitative observations are considered more accurate because these are measurable and can be recorded in numbers.',
        'مشاہدات پانچ حواس یعنی بصارت، سماعت، سونگھنے، چکھنے اور چھونے سے کیے جاتے ہیں۔ مشاہدات کی دو اقسام ہیں یعنی کیفیتی اور مقداری۔ مقداری مشاہدات زیادہ درست سمجھے جاتے ہیں کیونکہ یہ قابلِ پیمائش ہوتے ہیں اور اعداد میں درج کیے جا سکتے ہیں۔',
        'کتنې په پنځو حواسو یعنې لید، اورېدو، بوی، خوند او لمس کېږي. کتنې دوه ډوله دي یعنې کیفي او کمي. کمي کتنې ډېرې دقیقې ګڼل کېږي ځکه چې اندازه کېدای شي او په عددونو کې ثبتېدای شي.')
    s.table('bio2-tab-observations',
            ['Quantitative Observations', 'Qualitative Observations'],
            [['• Deal with numbers', '• Deal with description'], ['• Can be measured', '• Can be observed but not measured'],
             ['• Length, height, area, temperature, volume, weight, cost etc.', '• Colour, texture, smell, taste etc.']],
            ['مقداری مشاہدات', 'کیفیتی مشاہدات'],
            [['• اعداد سے متعلق', '• بیان سے متعلق'], ['• ناپے جا سکتے ہیں', '• دیکھے جا سکتے ہیں لیکن ناپے نہیں جا سکتے'],
             ['• لمبائی، اونچائی، رقبہ، درجۂ حرارت، حجم، وزن، لاگت وغیرہ', '• رنگ، بناوٹ، بو، ذائقہ وغیرہ']],
            ['کمي کتنې', 'کیفي کتنې'],
            [['• له عددونو سره سروکار', '• له تشریح سره سروکار'], ['• اندازه کېدای شي', '• لیدل کېدای شي خو اندازه کېدای نه شي'],
             ['• اوږدوالی، لوړوالی، مساحت، تودوخه، حجم، وزن، لګښت او نور', '• رنګ، جوړښت، بوی، خوند او نور']],
            ratio=.95)
    s.h('iii) Hypothesis', 'iii) مفروضہ', 'iii) فرضیه')
    s.p('Biologist uses observations to develop a possible answer to a biological problem. Such tentative answer is called a hypothesis. A good hypothesis has the following characteristics:',
        'ماہرِ حیاتیات مشاہدات کو حیاتیاتی مسئلے کا ممکنہ جواب تیار کرنے کے لیے استعمال کرتا ہے۔ ایسے عارضی جواب کو مفروضہ کہتے ہیں۔ اچھے مفروضے کی درج ذیل خصوصیات ہوتی ہیں:',
        'بیولوژیست کتنې د بیولوژیکي ستونزې د یو ممکن ځواب د جوړولو لپاره کاروي. داسې لنډمهاله ځواب ته فرضیه ویل کېږي. ښه فرضیه لاندې ځانګړتیاوې لري:')
    s.ul([('It is based upon the observations made by the biologist.', 'یہ ماہرِ حیاتیات کے کیے گئے مشاہدات پر مبنی ہوتا ہے۔', 'دا د بیولوژیست پر کړو کتنو ولاړه وي.'),
          ('It is a proposed statement to answer the problem.', 'یہ مسئلے کا جواب دینے کے لیے ایک تجویز کردہ بیان ہوتا ہے۔', 'دا د ستونزې د ځواب لپاره وړاندیز شوې څرګندونه ده.'),
          ('It is testable through experiments.', 'یہ تجربات کے ذریعے قابلِ جانچ ہوتا ہے۔', 'دا د تجربو له لارې ازمویل کېدای شي.'),
          ('There is always a way to disprove the hypothesis after experimentation.', 'تجربے کے بعد مفروضے کو غلط ثابت کرنے کا ہمیشہ ایک طریقہ ہوتا ہے۔', 'له تجربې وروسته د فرضیې د ناسم ثابتولو تل یوه لاره شته.')])
    s.p('A hypothesis is assumed as the possible answer. Biologist may make more than one hypothesis for a single problem. There is a need to test all hypothesis so that the true one can be selected. This testing is done by experimentation. But before going to experimentation, biologist makes deductions from each hypothesis.',
        'مفروضے کو ممکنہ جواب فرض کیا جاتا ہے۔ ماہرِ حیاتیات ایک ہی مسئلے کے لیے ایک سے زیادہ مفروضے بنا سکتا ہے۔ تمام مفروضوں کو جانچنے کی ضرورت ہوتی ہے تاکہ درست کا انتخاب کیا جا سکے۔ یہ جانچ تجربے سے کی جاتی ہے۔ لیکن تجربے سے پہلے ماہرِ حیاتیات ہر مفروضے سے استنباط اخذ کرتا ہے۔',
        'فرضیه د ممکن ځواب په توګه ګڼل کېږي. بیولوژیست کولای شي د یوې ستونزې لپاره له یوې ډېرې فرضیې جوړې کړي. ټولې فرضیې باید وازمویل شي ترڅو سمه وټاکل شي. دا ازموینه په تجربې کېږي. خو له تجربې مخکې بیولوژیست له هرې فرضیې استنتاجونه اخلي.')
    s.h('iv) Deductions', 'iv) استنباط', 'iv) استنتاجونه')
    s.p('Deductions are the logical consequences of hypothesis. For making deductions, the biologist takes hypothesis as true and draws out the expected results called deductions. It involves the use of “if” and “then”. For example, if all birds have wings then pigeon is a bird. Deductions help the biologist to do experiments.',
        'استنباط مفروضے کے منطقی نتائج ہیں۔ استنباط اخذ کرنے کے لیے ماہرِ حیاتیات مفروضے کو درست مان کر متوقع نتائج نکالتا ہے جنہیں استنباط کہتے ہیں۔ اس میں ”اگر“ اور ”تو“ کا استعمال ہوتا ہے۔ مثال کے طور پر، اگر تمام پرندوں کے پر ہوتے ہیں تو کبوتر ایک پرندہ ہے۔ استنباط ماہرِ حیاتیات کو تجربات کرنے میں مدد دیتے ہیں۔',
        'استنتاجونه د فرضیې منطقي پایلې دي. د استنتاج لپاره بیولوژیست فرضیه سمه ګڼي او تمه شوې پایلې راباسي چې استنتاجونه بلل کېږي. په دې کې د ”که“ او ”نو“ کارونه کېږي. د بېلګې په توګه، که ټول مرغان وزرونه لري نو کوتره مرغه ده. استنتاجونه بیولوژیست سره د تجربو په کولو کې مرسته کوي.')
    s.callout(SI, [('Hypothesis: “All plant cells have a nucleus”.', 'مفروضہ: ”پودوں کے تمام خلیوں میں مرکزہ ہوتا ہے“۔', 'فرضیه: ”د بوټو ټولې حجرې هسته لري“.'),
                   ('Deduction: “If all plant cells have a nucleus, then a nucleus will be observed in each cell of a blade of grass under the microscope”.',
                    'استنباط: ”اگر پودوں کے تمام خلیوں میں مرکزہ ہوتا ہے تو خوردبین کے نیچے گھاس کے پتے کے ہر خلیے میں مرکزہ نظر آئے گا“۔',
                    'استنتاج: ”که د بوټو ټولې حجرې هسته ولري، نو د مایکروسکوپ لاندې به د واښه د پاڼې په هره حجره کې هسته ولیدل شي“.')])
    s.h('v) Experiments', 'v) تجربات', 'v) تجربې')
    s.p('It is the most important step of biological method. Biologist performs experiments on his hypothesis and checks the deductions. Through experiments he can find that deductions of some hypothesis have come true while others have not. In this way, the hypothesis are proved as true or false',
        'یہ حیاتیاتی طریقے کا سب سے اہم مرحلہ ہے۔ ماہرِ حیاتیات اپنے مفروضے پر تجربات کرتا ہے اور استنباط کی جانچ کرتا ہے۔ تجربات کے ذریعے وہ معلوم کر سکتا ہے کہ بعض مفروضوں کے استنباط درست ثابت ہوئے جبکہ دوسروں کے نہیں۔ اس طرح مفروضے درست یا غلط ثابت ہوتے ہیں',
        'دا د بیولوژیکي میتود تر ټولو مهم پړاو دی. بیولوژیست پر خپله فرضیه تجربې کوي او استنتاجونه ګوري. د تجربو له لارې هغه موندلای شي چې د ځینو فرضیو استنتاجونه سم وختل او د نورو نه. په دې ډول فرضیې سمې یا ناسمې ثابتېږي',
        sourceNote='Sentence continues on the missing printed page 26; the PDF 31 text ends at the right margin with partly cut words ("deductio", "have co"), completed here as "deductions" and "have come".')
    s.p(*GAP, editorial=True, sourceGap=dict(printedPage=26, betweenPdfPages=[31, 32]))
    out.append(s)

    s = Section('bio2_2', '2.2', 'Malaria as an example of the biological method', 'حیاتیاتی طریقے کی مثال: ملیریا', 'د بیولوژیکي میتود بېلګه: ملاریا', [32, 33, 34])
    s.p('iii. When some volunteers drank the water from marshes, they did not develop malaria. Thus a new observation was made i.e. the disease did not result from drinking the water of marshes.',
        'iii. جب کچھ رضاکاروں نے دلدلوں کا پانی پیا تو انہیں ملیریا نہیں ہوا۔ اس طرح ایک نیا مشاہدہ ہوا یعنی یہ بیماری دلدلوں کا پانی پینے سے نہیں ہوتی۔',
        'iii. کله چې ځینو رضاکارانو د جبو اوبه وڅښلې، ملاریا یې ونه نیوله. په دې ډول یوه نوې کتنه وشوه یعنې دا ناروغي د جبو د اوبو له څښلو نه پیدا کېږي.')
    s.p('Then they began thinking that stagnant water of marshes poisoned the air. When people breathed in this “bad air”, they got malaria. That is why they gave the name malaria to this disease. The Italian words mala means “bad” and aria means “air”.',
        'پھر وہ سوچنے لگے کہ دلدلوں کا ٹھہرا ہوا پانی ہوا کو زہریلا کر دیتا ہے۔ جب لوگ اس ”خراب ہوا“ میں سانس لیتے ہیں تو انہیں ملیریا ہو جاتا ہے۔ اسی لیے انہوں نے اس بیماری کا نام ملیریا رکھا۔ اطالوی الفاظ مالا کا مطلب ”خراب“ اور آریا کا مطلب ”ہوا“ ہے۔',
        'بیا یې فکر پیل کړ چې د جبو ولاړې اوبه هوا مسمومه کوي. کله چې خلک په دې ”خرابه هوا“ کې ساه اخلي، ملاریا یې نیسي. له همدې امله یې دې ناروغۍ ته د ملاریا نوم ورکړ. په ایټالوي ژبه مالا یعنې ”خراب“ او آریا یعنې ”هوا“.')
    s.p('These observations did not help much for solving the problem i.e. “what is the cause of malaria?”',
        'ان مشاہدات نے مسئلے یعنی ”ملیریا کی وجہ کیا ہے؟“ کو حل کرنے میں زیادہ مدد نہیں کی۔',
        'دې کتنو د ستونزې یعنې ”د ملاریا لامل څه دی؟“ په حل کې ډېره مرسته ونه کړه.')
    s.callout(('Discovery of Quinine', 'کونین کی دریافت', 'د کونین کشف'), [
        ('In 17th century, malaria was a major disease in Europe. When America was discovered, many medicinal plants were sent from America to Europe. The bark of a tree quina-quina was very suitable for curing fevers. Its demands increased day by day in Europe. Some dishonest exporters began to export the bark of a similar tree, cinchona in place of quina-quina.',
         'سترہویں صدی میں ملیریا یورپ کی ایک بڑی بیماری تھی۔ جب امریکہ دریافت ہوا تو بہت سے طبی پودے امریکہ سے یورپ بھیجے گئے۔ کوینا کوینا نامی درخت کی چھال بخار کے علاج کے لیے بہت موزوں تھی۔ یورپ میں اس کی مانگ دن بدن بڑھتی گئی۔ کچھ بے ایمان برآمد کنندگان نے کوینا کوینا کی جگہ ایک ملتے جلتے درخت سنکونا کی چھال برآمد کرنا شروع کر دی۔',
         'په اوولسمه پېړۍ کې ملاریا په اروپا کې لویه ناروغي وه. کله چې امریکا کشف شوه، ډېر طبي بوټي له امریکا اروپا ته ولېږل شول. د کوینا کوینا ونې پوټکی د تبې د درملنې لپاره ډېر مناسب و. په اروپا کې یې غوښتنه ورځ تر بلې زیاتېده. ځینو بې ایمانه صادرونکو د کوینا کوینا پر ځای د ورته ونې سنکونا پوټکی صادرول پیل کړل.'),
        ('This dishonesty proved much beneficial. It was found that cinchona bark was excellent for treating malaria. It was then discovered that cinchona bark contained a chemical quinine that is effective in treating malaria. Quinine was the only remedy for malaria from the 17th to the 20th century.',
         'یہ بے ایمانی بہت فائدہ مند ثابت ہوئی۔ معلوم ہوا کہ سنکونا کی چھال ملیریا کے علاج کے لیے بہترین ہے۔ پھر دریافت ہوا کہ سنکونا کی چھال میں ایک کیمیکل کونین ہوتا ہے جو ملیریا کے علاج میں مؤثر ہے۔ سترہویں سے بیسویں صدی تک کونین ملیریا کا واحد علاج تھا۔',
         'دا بې ایماني ډېره ګټوره ثابته شوه. معلومه شوه چې د سنکونا پوټکی د ملاریا د درملنې لپاره ډېر ښه دی. بیا کشف شوه چې د سنکونا پوټکی کونین نومی کیمیاوي ماده لري چې د ملاریا په درملنه کې اغېزمنه ده. له اوولسمې تر شلمې پېړۍ پورې کونین د ملاریا یوازینۍ درملنه وه.')])
    s.p('Two hundred years later, it was proved that many diseases are caused by micro-organisms like bacteria. In 1878 a French Physician Laveran studied the ancient observations and work. He observed the blood of a malarial patient under microscope. He noticed some microorganisms in the blood. He won the Nobel Prize for his discoveries. Five years after Laveran, the same microorganism was observed in the blood of malarial patients and this microorganism was given a name of Plasmodium.',
        'دو سو سال بعد یہ ثابت ہوا کہ بہت سی بیماریاں بیکٹیریا جیسے خرد جانداروں سے ہوتی ہیں۔ 1878ء میں ایک فرانسیسی معالج لاویران نے قدیم مشاہدات اور کام کا مطالعہ کیا۔ اس نے ملیریا کے مریض کے خون کا خوردبین کے نیچے مشاہدہ کیا۔ اس نے خون میں کچھ خرد جاندار دیکھے۔ اس نے اپنی دریافتوں پر نوبل انعام حاصل کیا۔ لاویران کے پانچ سال بعد ملیریا کے مریضوں کے خون میں وہی خرد جاندار دیکھا گیا اور اس خرد جاندار کو پلازموڈیم کا نام دیا گیا۔',
        'دوه سوه کاله وروسته ثابته شوه چې ډېرې ناروغۍ د باکتریاوو په څېر مایکرو ژوندیو موجوداتو له امله پیدا کېږي. په 1878 کال کې فرانسوي ډاکټر لاوران پخوانۍ کتنې او کار مطالعه کړل. هغه د ملاریا د ناروغ وینه د مایکروسکوپ لاندې وکتله. هغه په وینه کې ځینې مایکرو ژوندي موجودات ولیدل. هغه د خپلو کشفونو له امله د نوبل جایزه وګټله. له لاوران پنځه کاله وروسته د ملاریا د ناروغانو په وینه کې همدا مایکرو ژوندی موجود ولیدل شو او دې ته د پلازموډیم نوم ورکړل شو.')
    s.h('Step 2: Hypothesis and Deduction', 'مرحلہ 2: مفروضہ اور استنباط', 'پړاو 2: فرضیه او استنتاج')
    s.p('Biologists further built upon the ancient observations and the discovery of Laveran. They developed a hypothesis i.e. “Plasmodium is the cause of malaria.” For testing the hypothesis through experiment, biologists made a deduction; “If Plasmodium is the cause of malaria, then all malarial patients should have Plasmodium in their blood.”',
        'ماہرینِ حیاتیات نے قدیم مشاہدات اور لاویران کی دریافت پر مزید کام کیا۔ انہوں نے ایک مفروضہ قائم کیا یعنی ”پلازموڈیم ملیریا کی وجہ ہے۔“ تجربے کے ذریعے مفروضے کی جانچ کے لیے ماہرینِ حیاتیات نے یہ استنباط کیا: ”اگر پلازموڈیم ملیریا کی وجہ ہے تو ملیریا کے تمام مریضوں کے خون میں پلازموڈیم ہونا چاہیے۔“',
        'بیولوژیستانو پر پخوانیو کتنو او د لاوران پر کشف نور کار وکړ. هغوی یوه فرضیه جوړه کړه یعنې ”پلازموډیم د ملاریا لامل دی.“ د تجربې له لارې د فرضیې د ازموینې لپاره بیولوژیستانو دا استنتاج وکړ: ”که پلازموډیم د ملاریا لامل وي، نو د ملاریا د ټولو ناروغانو په وینه کې باید پلازموډیم وي.“')
    s.h('Step 3: Experiment and Results', 'مرحلہ 3: تجربہ اور نتائج', 'پړاو 3: تجربه او پایلې')
    s.p('In order to test the hypothesis “Plasmodium is the cause of malaria”, biologists carried out the following experiment.',
        'مفروضے ”پلازموڈیم ملیریا کی وجہ ہے“ کی جانچ کے لیے ماہرینِ حیاتیات نے درج ذیل تجربہ کیا۔',
        'د ”پلازموډیم د ملاریا لامل دی“ فرضیې د ازموینې لپاره بیولوژیستانو لاندې تجربه وکړه.')
    s.ol([('i. They examined the blood of 100 malarial patients under microscope. It was labelled as the experimental group.',
           'i. انہوں نے ملیریا کے 100 مریضوں کے خون کا خوردبین کے نیچے معائنہ کیا۔ اسے تجرباتی گروپ کا نام دیا گیا۔',
           'i. هغوی د ملاریا د 100 ناروغانو وینه د مایکروسکوپ لاندې وکتله. دې ته تجربوي ډله ونومول شوه.'),
          ('ii. They also examined the blood of 100 healthy persons under microscope. It was labelled as the control group.',
           'ii. انہوں نے 100 صحت مند افراد کے خون کا بھی خوردبین کے نیچے معائنہ کیا۔ اسے کنٹرول گروپ کا نام دیا گیا۔',
           'ii. هغوی د 100 روغو کسانو وینه هم د مایکروسکوپ لاندې وکتله. دې ته کنټرول ډله ونومول شوه.')])
    s.p('Results: It was observed that all the malarial patients had Plasmodium in their blood; whereas the blood of healthy persons was free from Plasmodium. These results supported the hypothesis that Plasmodium is the cause of malaria. So it was taken as the solution of a biological problem.',
        'نتائج: دیکھا گیا کہ ملیریا کے تمام مریضوں کے خون میں پلازموڈیم تھا؛ جبکہ صحت مند افراد کا خون پلازموڈیم سے پاک تھا۔ ان نتائج نے اس مفروضے کی تائید کی کہ پلازموڈیم ملیریا کی وجہ ہے۔ چنانچہ اسے حیاتیاتی مسئلے کا حل مان لیا گیا۔',
        'پایلې: ولیدل شول چې د ملاریا ټولو ناروغانو په وینه کې پلازموډیم و؛ په داسې حال کې چې د روغو کسانو وینه له پلازموډیم پاکه وه. دې پایلو د دې فرضیې ملاتړ وکړ چې پلازموډیم د ملاریا لامل دی. نو دا د بیولوژیکي ستونزې د حل په توګه ومنل شوه.')
    s.h('Biological Problem 2: How is Plasmodium transmitted to human beings?', 'حیاتیاتی مسئلہ 2: پلازموڈیم انسانوں میں کیسے منتقل ہوتا ہے؟', 'بیولوژیکي ستونزه 2: پلازموډیم انسانانو ته څنګه لېږدول کېږي؟')
    s.h('Step 1: Observations:', 'مرحلہ 1: مشاہدات:', 'پړاو 1: کتنې:')
    s.p('Biologists were having the following observations:', 'ماہرینِ حیاتیات کے پاس درج ذیل مشاہدات تھے:', 'بیولوژیستانو سره لاندې کتنې وې:')
    s.ul([('Malaria is associated with marshes.', 'ملیریا کا تعلق دلدلوں سے ہے۔', 'ملاریا له جبو سره تړاو لري.'),
          ('Drinking water of marshes did not cause malaria.', 'دلدلوں کا پانی پینے سے ملیریا نہیں ہوا۔', 'د جبو د اوبو څښلو ملاریا نه پیدا کوله.')])
    s.p('In 1883 an American physician, Albert Freeman Africanus King (A. F. A. King), listed 20 more observations about malaria. Some important observations of King were:',
        '1883ء میں ایک امریکی معالج البرٹ فریمین افریکانس کنگ (اے ایف اے کنگ) نے ملیریا کے بارے میں مزید 20 مشاہدات کی فہرست بنائی۔ کنگ کے چند اہم مشاہدات یہ تھے:',
        'په 1883 کال کې یو امریکایي ډاکټر البرټ فریمن افریکانس کینګ (اې اېف اې کینګ) د ملاریا په اړه 20 نورې کتنې لېست کړې. د کینګ ځینې مهمې کتنې دا وې:')
    s.ol([('i. People who slept in open places suffered from malaria more than the people who slept indoors.',
           'i. جو لوگ کھلی جگہوں پر سوتے تھے وہ گھر کے اندر سونے والوں سے زیادہ ملیریا میں مبتلا ہوتے تھے۔',
           'i. هغه خلک چې په خلاصو ځایونو کې ویده کېدل، د کور دننه ویده کېدونکو په پرتله ډېر په ملاریا اخته کېدل.'),
          ('ii. Individuals who slept near a smoky fire usually did not get malaria.',
           'ii. جو افراد دھوئیں والی آگ کے قریب سوتے تھے انہیں عموماً ملیریا نہیں ہوتا تھا۔',
           'ii. هغه کسان چې د لوګي لرونکي اور سره نږدې ویده کېدل، معمولاً ملاریا نه نیول.'),
          ('iii. People who used mosquito nets suffered from malaria less than the ones who did not use mosquito nets.',
           'iii. جو لوگ مچھر دانی استعمال کرتے تھے وہ مچھر دانی استعمال نہ کرنے والوں سے کم ملیریا میں مبتلا ہوتے تھے۔',
           'iii. هغه خلک چې د ماشو جال یې کاراوه، د نه کاروونکو په پرتله لږ په ملاریا اخته کېدل.')])
    s.callout(STS, [('The life expectancy of people has been improved by controlling many of the infectious diseases. Tuberculosis (T.B), once known as a great killer disease, is one common examples that have been effectively controlled due to research in vaccination.',
                     'بہت سی متعدی بیماریوں پر قابو پا کر لوگوں کی متوقع عمر میں اضافہ ہوا ہے۔ تپ دق (ٹی بی)، جو کبھی ایک بڑی جان لیوا بیماری سمجھی جاتی تھی، ان عام مثالوں میں سے ایک ہے جن پر ویکسین کی تحقیق کی بدولت مؤثر طریقے سے قابو پایا گیا ہے۔',
                     'د ډېرو ساري ناروغیو په کنټرول سره د خلکو د ژوند تمه ښه شوې ده. نری رنځ (ټي بي) چې یو وخت لویه وژونکې ناروغي ګڼل کېده، یوه عامه بېلګه ده چې د واکسین په څېړنه یې په اغېزمنه توګه مخنیوی شوی دی.')])
    s.h('Step 2: Hypothesis and Deduction:', 'مرحلہ 2: مفروضہ اور استنباط:', 'پړاو 2: فرضیه او استنتاج:')
    s.p('On the basis of these observations A. F. A. King suggested a hypothesis: “Mosquitoes transmit Plasmodium.” In order to test the hypothesis, following deduction was made:',
        'ان مشاہدات کی بنیاد پر اے ایف اے کنگ نے ایک مفروضہ پیش کیا: ”مچھر پلازموڈیم منتقل کرتے ہیں۔“ مفروضے کی جانچ کے لیے درج ذیل استنباط کیا گیا:',
        'د دې کتنو پر بنسټ اې اېف اې کینګ یوه فرضیه وړاندې کړه: ”ماشي پلازموډیم لېږدوي.“ د فرضیې د ازموینې لپاره لاندې استنتاج وشو:')
    s.p('“If mosquitoes transmit Plasmodium, then Plasmodium should be present in mosquitoes.”',
        '”اگر مچھر پلازموڈیم منتقل کرتے ہیں تو مچھروں میں پلازموڈیم موجود ہونا چاہیے۔“',
        '”که ماشي پلازموډیم لېږدوي، نو په ماشو کې باید پلازموډیم موجود وي.“')
    s.h('Step 3: Experiment and Results', 'مرحلہ 3: تجربہ اور نتائج', 'پړاو 3: تجربه او پایلې')
    s.p('Ronald Ross was a British army physician who worked in India in 1880\'s. He performed important experiments to test the above deduction. He also received Nobel Prize for his work on the transmission of Plasmodium. He allowed a female Anopheles mosquito to bite a malarial patient. He killed the mosquito and found Plasmodium multiplying in mosquito\'s stomach. In the next experiment, he thought to allow an infected mosquito (having Plasmodium) to bite a healthy person. If the hypothesis was true, the healthy person would have gotten malaria. But he did not use human beings for such risky experiment. Ross performed his experiment again but used sparrows instead of human beings. He allowed a female Culex mosquito to bite a sparrow suffering from malaria. He killed some of the mosquitoes and studied them. He found that Plasmodium multiplied in the walls of the mosquito\'s stomach and then moved into the mosquito\'s salivary glands. He allowed infected mosquitoes to bite healthy sparrows. Ross found that these healthy sparrows got malaria. When he examined the blood of these previously healthy sparrows, he found many Plasmodium in it. In this way, biologists had got the solution of the 2nd biological problem (How Plasmodium is transmitted to human beings?). The hypothesis (Mosquitoes transmit Plasmodium) was proved true and taken as the solution of biological problem.',
        'رونالڈ راس ایک برطانوی فوجی معالج تھا جس نے 1880 کی دہائی میں ہندوستان میں کام کیا۔ اس نے اوپر والے استنباط کی جانچ کے لیے اہم تجربات کیے۔ پلازموڈیم کی منتقلی پر کام کے لیے اسے نوبل انعام بھی ملا۔ اس نے ایک مادہ اینوفیلیز مچھر کو ملیریا کے مریض کو کاٹنے دیا۔ اس نے مچھر کو مار کر اس کے معدے میں پلازموڈیم کو بڑھتے ہوئے پایا۔ اگلے تجربے میں اس نے سوچا کہ ایک متاثرہ مچھر (جس میں پلازموڈیم ہو) کو صحت مند شخص کو کاٹنے دے۔ اگر مفروضہ درست ہوتا تو صحت مند شخص کو ملیریا ہو جاتا۔ لیکن اس نے ایسے خطرناک تجربے کے لیے انسانوں کو استعمال نہیں کیا۔ راس نے اپنا تجربہ دوبارہ کیا لیکن انسانوں کی بجائے چڑیاں استعمال کیں۔ اس نے ایک مادہ کیولیکس مچھر کو ملیریا میں مبتلا چڑیا کو کاٹنے دیا۔ اس نے کچھ مچھر مار کر ان کا مطالعہ کیا۔ اس نے پایا کہ پلازموڈیم مچھر کے معدے کی دیواروں میں بڑھتا ہے اور پھر مچھر کے لعابی غدود میں چلا جاتا ہے۔ اس نے متاثرہ مچھروں کو صحت مند چڑیوں کو کاٹنے دیا۔ راس نے پایا کہ ان صحت مند چڑیوں کو ملیریا ہو گیا۔ جب اس نے ان پہلے صحت مند چڑیوں کے خون کا معائنہ کیا تو اس میں بہت سے پلازموڈیم پائے۔ اس طرح ماہرینِ حیاتیات کو دوسرے حیاتیاتی مسئلے (پلازموڈیم انسانوں میں کیسے منتقل ہوتا ہے؟) کا حل مل گیا۔ مفروضہ (مچھر پلازموڈیم منتقل کرتے ہیں) درست ثابت ہوا اور اسے حیاتیاتی مسئلے کا حل مان لیا گیا۔',
        'رونالډ راس یو برتانوي پوځي ډاکټر و چې د 1880 لسیزه کې یې په هند کې کار کاوه. هغه د پورتني استنتاج د ازموینې لپاره مهمې تجربې وکړې. د پلازموډیم د لېږد په اړه د کار لپاره یې د نوبل جایزه هم ترلاسه کړه. هغه یوې ښځینه انوفلیس ماشې ته اجازه ورکړه چې د ملاریا ناروغ وچیچي. هغه ماشۍ ووژله او د ماشۍ په معده کې یې پلازموډیم د زیاتېدو په حال کې ومونده. په بله تجربه کې یې فکر وکړ چې یوې اخته ماشۍ (چې پلازموډیم لري) ته اجازه ورکړي چې روغ کس وچیچي. که فرضیه سمه وای، روغ کس به ملاریا نیولی وای. خو هغه د داسې خطرناکې تجربې لپاره انسانان ونه کارول. راس خپله تجربه بیا وکړه خو د انسانانو پر ځای یې چڼچڼې وکارولې. هغه یوې ښځینه کیولیکس ماشې ته اجازه ورکړه چې په ملاریا اخته چڼچڼه وچیچي. هغه ځینې ماشي ووژلې او مطالعه یې کړې. هغه وموندل چې پلازموډیم د ماشۍ د معدې په دېوالونو کې زیاتېږي او بیا د ماشۍ لعابي غدو ته ځي. هغه اخته ماشو ته اجازه ورکړه چې روغې چڼچڼې وچیچي. راس وموندل چې دې روغو چڼچڼو ملاریا ونیوله. کله یې چې د دې پخوا روغو چڼچڼو وینه وکتله، ډېر پلازموډیم یې پکې وموندل. په دې ډول بیولوژیستانو د دوهمې بیولوژیکي ستونزې (پلازموډیم انسانانو ته څنګه لېږدول کېږي؟) حل ترلاسه کړ. فرضیه (ماشي پلازموډیم لېږدوي) سمه ثابته شوه او د بیولوژیکي ستونزې د حل په توګه ومنل شوه.')
    s.callout(SI, [('Patient suffering from malaria have Plasmodium in their blood. When a female Anopheles mosquito bites a malarial patient, it sucks blood from him/her. Thus the plasmodium enters the body of the mosquito. When the infected mosquito bites a healthy person, it injects Plasmodium in his blood.',
                    'ملیریا کے مریض کے خون میں پلازموڈیم ہوتا ہے۔ جب مادہ اینوفیلیز مچھر ملیریا کے مریض کو کاٹتا ہے تو اس کا خون چوستا ہے۔ اس طرح پلازموڈیم مچھر کے جسم میں داخل ہو جاتا ہے۔ جب متاثرہ مچھر کسی صحت مند شخص کو کاٹتا ہے تو اس کے خون میں پلازموڈیم داخل کر دیتا ہے۔',
                    'د ملاریا ناروغ په وینه کې پلازموډیم وي. کله چې ښځینه انوفلیس ماشۍ د ملاریا ناروغ چیچي، د هغه/هغې وینه رودي. په دې ډول پلازموډیم د ماشۍ بدن ته ننوځي. کله چې اخته ماشۍ روغ کس وچیچي، د هغه په وینه کې پلازموډیم ننباسي.')])
    out.append(s)
    return out
