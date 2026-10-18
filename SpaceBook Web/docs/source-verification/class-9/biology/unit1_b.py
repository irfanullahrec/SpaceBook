# -*- coding: utf-8 -*-
"""Unit 1 part B — PDF 11-13 (printed 5-7): 1.3.3-1.3.5, 1.4, 1.5."""
from bio9_tools import Section

STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')
AI = ('Analysing and Interpreting:', 'تجزیہ اور توضیح:', 'شننه او تفسیر:')


def extend_1_3(s):
    s.p('1.3.3 Biogeography is the study of distribution of organisms in space and time. For example, in biogeography we study why polar bears are found only in certain parts of the arctic regions or why malaria-causing mosquitoes flourish in damp and warm areas.',
        '1.3.3 بائیو جغرافیہ مکان اور زمان میں جانداروں کی تقسیم کا مطالعہ ہے۔ مثال کے طور پر، بائیو جغرافیہ میں ہم یہ مطالعہ کرتے ہیں کہ قطبی ریچھ صرف آرکٹک علاقوں کے بعض حصوں میں کیوں پائے جاتے ہیں یا ملیریا پھیلانے والے مچھر نم اور گرم علاقوں میں کیوں پھلتے پھولتے ہیں۔',
        '1.3.3 بایوجغرافیه په ځای او وخت کې د ژوندیو موجوداتو د وېش مطالعه ده. د بېلګې په توګه، په بایوجغرافیه کې موږ څېړو چې قطبي ییږان ولې یوازې د ارکټیک سیمو په ځینو برخو کې موندل کېږي یا د ملاریا خپروونکي ماشومان ولې په لوندو او ګرمو سیمو کې ډېرېږي.')
    s.p('1.3.4 Biostatistics or Biometry is the application of statistical and mathematical formulas in the study of biology. It involves the design, analysis and interpretation of research data.',
        '1.3.4 بائیو اسٹیٹسٹکس یا بائیو میٹری حیاتیات کے مطالعے میں شماریاتی اور ریاضیاتی فارمولوں کا اطلاق ہے۔ اس میں تحقیقی ڈیٹا کی منصوبہ بندی، تجزیہ اور توضیح شامل ہے۔',
        '1.3.4 بایوستاټیسټیک یا بایومټري د بیولوژي په مطالعه کې د احصایوي او ریاضیاتي فورمولونو کارونه ده. په دې کې د څېړنیزو معلوماتو ډیزاین، تحلیل او تفسیر شامل دي.')
    s.p('1.3.5 Bio-economics is the co-relation between biology and economics. It deals with the study of organisms from economical point of view. In bio-economics, scientists calculate and compare the cost and profit of the biological projects e.g. production of a new variety of a crop.',
        '1.3.5 بائیو اکنامکس حیاتیات اور معاشیات کے درمیان باہمی تعلق ہے۔ یہ معاشی نقطۂ نظر سے جانداروں کے مطالعے سے متعلق ہے۔ بائیو اکنامکس میں سائنس دان حیاتیاتی منصوبوں مثلاً کسی فصل کی نئی قسم کی پیداوار کی لاگت اور منافع کا حساب لگاتے اور موازنہ کرتے ہیں۔',
        '1.3.5 بایو اقتصاد د بیولوژي او اقتصاد ترمنځ متقابله اړیکه ده. دا له اقتصادي نظره د ژوندیو موجوداتو له مطالعې سره سروکار لري. په بایو اقتصاد کې ساینس پوهان د بیولوژیکي پروژو لکه د یوې فصل د نوي ډول د تولید لګښت او ګټه محاسبه او پرتله کوي.')


def sections():
    out = []
    s = Section('bio1_4', '1.4', 'Careers in Biology', 'حیاتیات میں پیشے', 'په بیولوژي کې مسلکونه', [11, 12])
    s.p('Careers in Biology: Studying biology can be immensely rewarding and exciting. There are several career/paths one can follow as a biologist, such as:',
        'حیاتیات میں پیشے: حیاتیات کا مطالعہ بے حد فائدہ مند اور دلچسپ ہو سکتا ہے۔ ماہرِ حیاتیات کے طور پر کئی پیشے/راستے اختیار کیے جا سکتے ہیں، مثلاً:',
        'په بیولوژي کې مسلکونه: د بیولوژي مطالعه ډېره ګټوره او په زړه پورې کېدای شي. د بیولوژیست په توګه څو مسلکونه/لارې غوره کېدای شي، لکه:')
    s.callout(('Scientific Tips', 'سائنسی مشورے', 'ساینسي لارښوونې'),
              [('You should not only excel in biology but also in related areas such as communication skills, analysis of the situation, critical thinking and self-motivation.',
                'آپ کو نہ صرف حیاتیات میں بلکہ متعلقہ شعبوں مثلاً ابلاغی مہارتوں، صورتِ حال کے تجزیے، تنقیدی سوچ اور خود ترغیبی میں بھی ممتاز ہونا چاہیے۔',
                'تاسو باید نه یوازې په بیولوژي کې بلکې په اړوندو برخو لکه د اړیکو مهارتونو، د حالت شننې، انتقادي فکر او ځان هڅونې کې هم غوره اوسئ.')])
    s.p('1.4.1 Medicine and Surgery: The field of medicine is related with the diagnosis and treatment of human diseases. In surgery, the defective parts of the body are repaired, replaced or removed. One can choose these professions in the same course (MBBS) after studying biology at higher secondary level.',
        '1.4.1 طب اور جراحی: طب کا شعبہ انسانی بیماریوں کی تشخیص اور علاج سے متعلق ہے۔ جراحی میں جسم کے خراب حصوں کی مرمت کی جاتی ہے، انہیں تبدیل کیا جاتا ہے یا نکال دیا جاتا ہے۔ ہائیر سیکنڈری سطح پر حیاتیات پڑھنے کے بعد ایک ہی کورس (ایم بی بی ایس) میں یہ پیشے اختیار کیے جا سکتے ہیں۔',
        '1.4.1 طب او جراحي: د طب برخه د انساني ناروغیو له تشخیص او درملنې سره تړاو لري. په جراحۍ کې د بدن خرابې برخې ترمیمېږي، بدلېږي یا لرې کېږي. په لوړه ثانوي کچه د بیولوژي له لوستلو وروسته دا مسلکونه په یوه کورس (ایم بي بي ایس) کې غوره کېدای شي.')
    s.p('1.4.2 Fisheries is the profession related to the production of fish. Fisheries managers work in fish hatcheries and study fish habitats, nutrition requirements, genetics and diseases etc. to raise fish production. One can adopt this career after completing a bachelor or master degree in zoology.',
        '1.4.2 ماہی پروری مچھلی کی پیداوار سے متعلق پیشہ ہے۔ ماہی پروری کے منتظمین مچھلی کی ہیچریوں میں کام کرتے ہیں اور مچھلی کی پیداوار بڑھانے کے لیے مچھلیوں کے مساکن، غذائی ضروریات، جینیات اور بیماریوں وغیرہ کا مطالعہ کرتے ہیں۔ حیوانیات میں بیچلر یا ماسٹر ڈگری مکمل کرنے کے بعد یہ پیشہ اختیار کیا جا سکتا ہے۔',
        '1.4.2 کب روزنه د کبانو له تولید سره تړلی مسلک دی. د کب روزنې مدیران د کبانو په هچریو کې کار کوي او د کبانو د تولید د زیاتولو لپاره د کبانو استوګنځایونه، غذايي اړتیاوې، جنیټیک او ناروغۍ څېړي. په ژوپوهنه کې د لیسانس یا ماسټرۍ له بشپړولو وروسته دا مسلک غوره کېدای شي.')
    s.p('1.4.3 Agriculture: A biologist can also opt his/her career as an agriculturalist who deals with crops and livestock. In Pakistan, there are Agricultural universities where one can do professional courses in agriculture after the higher secondary education in biology. Agriculturists may work in the agriculture department, veterinary and pharmaceutical industries, food industries, farming, agricultural banks etc.',
        '1.4.3 زراعت: ماہرِ حیاتیات ماہرِ زراعت کے طور پر بھی اپنا پیشہ اختیار کر سکتا/سکتی ہے جو فصلوں اور مویشیوں سے متعلق ہوتا ہے۔ پاکستان میں زرعی جامعات ہیں جہاں حیاتیات میں ہائیر سیکنڈری تعلیم کے بعد زراعت کے پیشہ ورانہ کورس کیے جا سکتے ہیں۔ ماہرینِ زراعت محکمۂ زراعت، ویٹرنری اور دوا ساز صنعتوں، خوراک کی صنعتوں، کاشتکاری، زرعی بینکوں وغیرہ میں کام کر سکتے ہیں۔',
        '1.4.3 کرنه: بیولوژیست کولای شي د کرنپوه په توګه هم خپل مسلک غوره کړي چې له فصلونو او څارویو سره سروکار لري. په پاکستان کې کرنیز پوهنتونونه شته چې هلته په بیولوژي کې د لوړې ثانوي زده کړې وروسته د کرنې مسلکي کورسونه کېدای شي. کرنپوهان کولای شي د کرنې په ریاست، وترنري او درمل جوړونې صنعتونو، د خوړو صنعتونو، کرهڼې، کرنیزو بانکونو او نورو کې کار وکړي.')
    s.callout(STS, [('Penicillin: An accidental breakthrough in the world of medicine.',
                     'پنسلین: طب کی دنیا میں ایک اتفاقی پیش رفت۔',
                     'پنسلین: د طب په نړۍ کې یوه ناڅاپي لاسته راوړنه.'),
                    ('Penicillin is the first naturally occurring and most extensively used antibiotic. It was discovered in 1928. It has enabled the physicians to treat severe infections such as meningitis, pneumonia and gonorrhoea. The first patient was successfully treated in the United States in 1942. Penicillin helped in reducing the number of deaths.',
                     'پنسلین پہلی قدرتی طور پر پائی جانے والی اور سب سے زیادہ استعمال ہونے والی اینٹی بائیوٹک ہے۔ یہ 1928ء میں دریافت ہوئی۔ اس نے معالجین کو گردن توڑ بخار، نمونیا اور سوزاک جیسے شدید انفیکشنز کا علاج کرنے کے قابل بنایا۔ پہلے مریض کا کامیاب علاج 1942ء میں امریکہ میں کیا گیا۔ پنسلین نے اموات کی تعداد کم کرنے میں مدد کی۔',
                     'پنسلین لومړنۍ طبیعي او تر ټولو پراخه کارېدونکې انټي بیوټیک ده. دا په 1928 کال کې کشف شوه. دې ډاکټرانو ته وړتیا ورکړه چې سختې انتاني ناروغۍ لکه مننژیت، سینه بغل او سوزاک درملنه کړي. لومړی ناروغ په 1942 کال کې په متحده ایالاتو کې په بریالیتوب درملنه شو. پنسلین د مړینو په کمولو کې مرسته وکړه.')])
    s.h('1.4.4 Animal Science', '1.4.4 حیوانی سائنس', '1.4.4 د حیواناتو ساینس')
    s.p('Animal science or animal husbandry deals with the breeding and raising of livestock (domestic animals). The professional course is taught in many universities and colleges after higher secondary education in biology. Graduates of these courses work in veterinary hospitals, pharmaceutical industry, livestock department and pet food industry etc.',
        'حیوانی سائنس یا گلہ بانی مویشیوں (پالتو جانوروں) کی افزائشِ نسل اور پرورش سے متعلق ہے۔ یہ پیشہ ورانہ کورس حیاتیات میں ہائیر سیکنڈری تعلیم کے بعد کئی جامعات اور کالجوں میں پڑھایا جاتا ہے۔ ان کورسز کے فارغ التحصیل ویٹرنری ہسپتالوں، دوا ساز صنعت، محکمۂ لائیو سٹاک اور پالتو جانوروں کی خوراک کی صنعت وغیرہ میں کام کرتے ہیں۔',
        'د حیواناتو ساینس یا مالداري د څارویو (کورني ژویو) له نسل اخیستنې او روزنې سره سروکار لري. دا مسلکي کورس په بیولوژي کې د لوړې ثانوي زده کړې وروسته په ډېرو پوهنتونونو او کالجونو کې تدریسېږي. د دې کورسونو فارغان په وترنري روغتونونو، درمل جوړونې صنعت، د مالدارۍ ریاست او د کورني ژویو د خوړو صنعت کې کار کوي.')
    s.callout(('Forensic science:', 'فرانزک سائنس:', 'عدلي ساینس:'),
              [('Forensic biologists work with police departments and other law enforcement agencies using scientific methods to discover and process evidence that can be used to detect criminals.',
                'فرانزک ماہرینِ حیاتیات پولیس کے محکموں اور قانون نافذ کرنے والے دیگر اداروں کے ساتھ سائنسی طریقے استعمال کرتے ہوئے ایسے شواہد دریافت کرتے اور ان پر کارروائی کرتے ہیں جو مجرموں کا پتہ لگانے میں استعمال ہو سکتے ہیں۔',
                'عدلي بیولوژیستان له پولیسو او نورو قانون پلي کوونکو ادارو سره د ساینسي میتودونو په کارولو داسې شواهد کشفوي او پرې کار کوي چې د جنایتکارانو د موندلو لپاره کارېدای شي.')])
    s.h('1.4.5 Horticulture', '1.4.5 باغبانی', '1.4.5 باغواني')
    s.p('After higher secondary education, you can opt for a professional course in horticulture. Horticulturist can open business and find jobs in fruits and vegetable production, landscape design, nurseries, gardens, pest management etc.',
        'ہائیر سیکنڈری تعلیم کے بعد آپ باغبانی کا پیشہ ورانہ کورس اختیار کر سکتے ہیں۔ ماہرِ باغبانی پھلوں اور سبزیوں کی پیداوار، لینڈ اسکیپ ڈیزائن، نرسریوں، باغات، کیڑوں کے انتظام وغیرہ میں کاروبار شروع کر سکتا ہے اور ملازمتیں حاصل کر سکتا ہے۔',
        'له لوړې ثانوي زده کړې وروسته تاسو کولای شئ د باغوانۍ مسلکي کورس غوره کړئ. باغوان کولای شي د مېوو او سبزیو په تولید، د منظرې ډیزاین، نرسریو، باغونو، د آفتونو په مدیریت او نورو کې سوداګري پیل کړي او دندې ومومي.')
    s.callout(('Health care:', 'صحت کی دیکھ بھال:', 'روغتیايي پاملرنه:'),
              [('Biologists may develop public health campaigns to defeat illnesses such as tuberculosis, cancer and heart diseases. Others work to prevent the spread of rare and deadly diseases, such as dengue fever.',
                'ماہرینِ حیاتیات تپ دق، کینسر اور دل کی بیماریوں جیسی بیماریوں کو شکست دینے کے لیے صحتِ عامہ کی مہمات تیار کر سکتے ہیں۔ دوسرے نایاب اور مہلک بیماریوں مثلاً ڈینگی بخار کے پھیلاؤ کو روکنے کے لیے کام کرتے ہیں۔',
                'بیولوژیستان کولای شي د نري رنځ، سرطان او زړه د ناروغیو په څېر ناروغیو د ماتولو لپاره د عامې روغتیا کمپاینونه جوړ کړي. نور د نادرو او وژونکو ناروغیو لکه ډینګي تبې د خپرېدو د مخنیوي لپاره کار کوي.')])
    s.h('1.4.6 Forestry', '1.4.6 جنگلات', '1.4.6 ځنګلداري')
    s.p('Forestry is concerned with managing forests and growing forests to provide timber and for wildlife habitat, recreation and biodiversity management.',
        'جنگلات (فاریسٹری) جنگلات کے انتظام اور لکڑی کی فراہمی اور جنگلی حیات کے مسکن، تفریح اور حیاتیاتی تنوع کے انتظام کے لیے جنگلات اگانے سے متعلق ہے۔',
        'ځنګلداري د ځنګلونو له مدیریت او د لرګیو د برابرولو او د ځنګلي ژوند د استوګنځای، تفریح او د ژوندیو تنوع د مدیریت لپاره د ځنګلونو له کرلو سره سروکار لري.')
    s.h('1.4.7 Farming', '1.4.7 فارمنگ', '1.4.7 فارم داري')
    s.p('In farming farms are developed and maintained for animal breeding, poultry, fruit and vegetables. A student of biology after doing professional course in agriculture or animal husbandry etc. can adopt this field.',
        'فارمنگ میں جانوروں کی افزائشِ نسل، مرغبانی، پھلوں اور سبزیوں کے لیے فارم بنائے اور چلائے جاتے ہیں۔ حیاتیات کا طالب علم زراعت یا گلہ بانی وغیرہ میں پیشہ ورانہ کورس کرنے کے بعد یہ شعبہ اختیار کر سکتا ہے۔',
        'په فارم دارۍ کې د ژویو د نسل اخیستنې، چرګانو روزنې، مېوو او سبزیو لپاره فارمونه جوړېږي او ساتل کېږي. د بیولوژي زده کوونکی په کرنه یا مالدارۍ کې د مسلکي کورس له کولو وروسته دا برخه غوره کولای شي.')
    s.callout(AI, [('A group of class fellows is interested in various fields of biology. On the basis of your knowledge, analyse where they can make their careers.',
                    'ہم جماعتوں کا ایک گروپ حیاتیات کے مختلف شعبوں میں دلچسپی رکھتا ہے۔ اپنے علم کی بنیاد پر تجزیہ کریں کہ وہ اپنا کیریئر کہاں بنا سکتے ہیں۔',
                    'د ټولګیوالو یوه ډله د بیولوژي په بېلابېلو برخو کې لېوالتیا لري. د خپلې پوهې پر بنسټ وشنئ چې دوی چېرته خپل مسلک جوړولای شي.')])
    s.table('bio1-tab-careers',
            ['Students', 'Field', 'Career (may be 1 or more)'],
            [['1', 'Immunology', ''], ['2', 'Entomology', ''], ['3', 'Histology', ''], ['4', 'Parasitology', '']],
            ['طلبہ', 'شعبہ', 'کیریئر (ایک یا زیادہ)'],
            [['1', 'امیونولوجی', ''], ['2', 'اینٹومولوجی', ''], ['3', 'ہسٹالوجی', ''], ['4', 'پیراسائٹالوجی', '']],
            ['زده کوونکي', 'برخه', 'مسلک (یو یا ډېر)'],
            [['1', 'امیونولوژي', ''], ['2', 'انټومولوژي', ''], ['3', 'هسټولوژي', ''], ['4', 'پاراسایټولوژي', '']],
            ratio=.9)
    out.append(s)

    # PDF 13 (printed 7) — 1.5
    s = Section('bio1_5', '1.5', 'The Five Kingdoms', 'پانچ کنگڈمز (مملکتیں)', 'پنځه سلطنتونه (کنګډمونه)', [13])
    s.p('Robert Whittaker in 1969 classified all living organisms into five kingdoms. This is known as “Five-Kingdom System of Classification”. These five kingdoms are:',
        'رابرٹ وٹیکر نے 1969ء میں تمام جانداروں کو پانچ کنگڈمز میں درجہ بند کیا۔ اسے ”درجہ بندی کا پانچ کنگڈم نظام“ کہا جاتا ہے۔ یہ پانچ کنگڈمز یہ ہیں:',
        'رابرټ وټیکر په 1969 کال کې ټول ژوندي موجودات په پنځو کنګډمونو وېشل. دې ته ”د ډلبندۍ پنځه کنګډمي سیسټم“ ویل کېږي. دا پنځه کنګډمونه دا دي:')
    s.lines([('1. Prokaryotae  2. Protoctista  3. Fungi', '1. پروکیریوٹی  2. پروٹوکٹسٹا  3. فنجائی', '1. پروکاریوټي  2. پروټوکټیسټا  3. فنجای'),
             ('4. Plantae  5. Animalia', '4. پلانٹی  5. اینیمیلیا', '4. پلانټي  5. انیمالیا')])
    s.h('1.5.1 Kingdom Prokaryotae (Monera)', '1.5.1 کنگڈم پروکیریوٹی (مونیرا)', '1.5.1 کنګډم پروکاریوټي (مونېرا)')
    s.p('This kingdom includes all unicellular and microscopic organisms. These organisms lack membrane bounded nucleus and other organelles inside their cells. Their cell wall is made of murein. Examples are Bacteria and Cyanobacteria.',
        'اس کنگڈم میں تمام یک خلوی اور خوردبینی جاندار شامل ہیں۔ ان جانداروں کے خلیوں کے اندر جھلی دار مرکزہ اور دیگر عضیات نہیں ہوتے۔ ان کی خلوی دیوار میورین سے بنی ہوتی ہے۔ مثالیں بیکٹیریا اور سائنو بیکٹیریا ہیں۔',
        'په دې کنګډم کې ټول یو حجروي او مایکروسکوپي ژوندي موجودات شامل دي. د دې موجوداتو په حجرو کې غشا لرونکې هسته او نور اورګانیلونه نشته. د دوی د حجرې دېوال له میورین څخه جوړ دی. بېلګې یې باکتریا او سیانوباکتریا دي.')
    s.h('1.5.2 Kingdom Protista or Protoctista', '1.5.2 کنگڈم پروٹسٹا یا پروٹوکٹسٹا', '1.5.2 کنګډم پروټیسټا یا پروټوکټیسټا')
    s.p('This kingdom included eukaryotic organisms which are usually small and having differences with the organisms of other eukaryotic kingdoms. They usually live in aquatic habitats. Algae, slime molds, protozoans (Plasmodium, Amoeba and Paramecium) are some of the examples of this kingdom.',
        'اس کنگڈم میں یوکیریوٹک جاندار شامل ہیں جو عموماً چھوٹے ہوتے ہیں اور دوسری یوکیریوٹک کنگڈمز کے جانداروں سے مختلف ہوتے ہیں۔ یہ عموماً آبی مساکن میں رہتے ہیں۔ الجی، سلائم مولڈز، پروٹوزوآ (پلازموڈیم، امیبا اور پیرامیشیم) اس کنگڈم کی چند مثالیں ہیں۔',
        'په دې کنګډم کې یوکاریوټیک ژوندي موجودات شامل دي چې معمولاً واړه وي او د نورو یوکاریوټیکو کنګډمونو له موجوداتو سره توپیرونه لري. دوی معمولاً په اوبو کې اوسېږي. الجي، سلایم مولډونه، پروټوزوا (پلازموډیم، امیبا او پارامیشیم) د دې کنګډم ځینې بېلګې دي.')
    s.h('1.5.3 Kingdom Fungi', '1.5.3 کنگڈم فنجائی', '1.5.3 کنګډم فنجای')
    s.p('Fungi includes organisms which are all eukaryotic and multicellular. Their cell wall is made of chitin (a polysaccharide). They do not have chloroplast, so they cannot synthesize their own food and are therefore heterotrophic. The food is stored inside the body in the form of glycogen. Some of the examples are Mushrooms, Molds, Puffballs, yeast etc.',
        'فنجائی میں ایسے جاندار شامل ہیں جو سب یوکیریوٹک اور کثیر خلوی ہیں۔ ان کی خلوی دیوار کائٹن (ایک پولی سیکرائیڈ) سے بنی ہوتی ہے۔ ان میں کلوروپلاسٹ نہیں ہوتا، اس لیے یہ اپنی خوراک خود تیار نہیں کر سکتے اور اسی وجہ سے ہیٹروٹرافک ہیں۔ خوراک جسم کے اندر گلائکوجن کی صورت میں ذخیرہ ہوتی ہے۔ چند مثالیں کھمبیاں، مولڈز، پف بالز، خمیر وغیرہ ہیں۔',
        'فنجای هغه موجودات لري چې ټول یوکاریوټیک او څو حجروي دي. د دوی د حجرې دېوال له کایټین (یو پولي سکرایډ) جوړ دی. کلوروپلاسټ نه لري، نو خپل خواړه نه شي جوړولای او له همدې امله هټروټروفیک دي. خواړه د بدن دننه د ګلایکوجن په بڼه زېرمه کېږي. ځینې بېلګې یې مرخېړي، مولډونه، پف بالونه، خمیره او نور دي.')
    s.h('1.5.4 Kingdom Plantae', '1.5.4 کنگڈم پلانٹی', '1.5.4 کنګډم پلانټي')
    s.p('This kingdom includes multicellular and eukaryotic organisms which are autotrophic in nature. Their cell wall is made of cellulose and mostly lack centrioles inside their cells. The reserve food is in the form of starch. Examples are Brassica, Mulberry, Pinus, Ferns etc.',
        'اس کنگڈم میں کثیر خلوی اور یوکیریوٹک جاندار شامل ہیں جو فطرتاً آٹوٹرافک ہیں۔ ان کی خلوی دیوار سیلولوز سے بنی ہوتی ہے اور ان کے خلیوں میں عموماً سینٹریولز نہیں ہوتے۔ ذخیرہ شدہ خوراک نشاستے کی صورت میں ہوتی ہے۔ مثالیں براسیکا، شہتوت، پائنس، فرن وغیرہ ہیں۔',
        'په دې کنګډم کې څو حجروي او یوکاریوټیک موجودات شامل دي چې په طبیعت کې اوټوټروفیک دي. د دوی د حجرې دېوال له سلولوز جوړ دی او په حجرو کې یې ډېری وخت سنټریولونه نه وي. زېرمه شوي خواړه د نشایستې په بڼه وي. بېلګې یې براسیکا، توت، پاینس، فرن او نور دي.')
    s.h('1.5.5 Kingdom Animalia', '1.5.5 کنگڈم اینیمیلیا', '1.5.5 کنګډم انیمالیا')
    s.p('This kingdom includes multicellular and eukaryotic organisms which are heterotrophic in nature. These organisms lack the cell wall and centrioles are present in the cells. The reserve food is glycogen. The members of this kingdom can be split into two groups that is vertebrates and invertebrates. Animals include jellyfish, worms, insects, fish, reptiles, birds, mammals etc.',
        'اس کنگڈم میں کثیر خلوی اور یوکیریوٹک جاندار شامل ہیں جو فطرتاً ہیٹروٹرافک ہیں۔ ان جانداروں میں خلوی دیوار نہیں ہوتی اور خلیوں میں سینٹریولز موجود ہوتے ہیں۔ ذخیرہ شدہ خوراک گلائکوجن ہے۔ اس کنگڈم کے ارکان کو دو گروہوں یعنی فقاریوں اور غیر فقاریوں میں تقسیم کیا جا سکتا ہے۔ جانوروں میں جیلی فش، کیڑے (ورمز)، حشرات، مچھلیاں، رینگنے والے جانور، پرندے، ممالیہ وغیرہ شامل ہیں۔',
        'په دې کنګډم کې څو حجروي او یوکاریوټیک موجودات شامل دي چې په طبیعت کې هټروټروفیک دي. دا موجودات د حجرې دېوال نه لري او په حجرو کې یې سنټریولونه شته. زېرمه شوي خواړه ګلایکوجن دي. د دې کنګډم غړي په دوو ډلو یعنې فقاریه وو او غیر فقاریه وو وېشل کېدای شي. ژوي جیلي فش، چینجي، حشرات، کبان، خزنده، مرغان، تي لرونکي او نور شاملوي.')
    out.append(s)
    return out
