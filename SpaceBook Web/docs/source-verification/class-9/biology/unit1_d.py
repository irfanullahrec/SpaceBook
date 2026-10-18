# -*- coding: utf-8 -*-
"""Unit 1 part D — PDF 18-24 (printed 12-18): 1.7, 1.8, 1.9."""
from bio9_tools import Section
import unit1_figs as F

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')


def sections():
    out = []
    s = Section('bio1_7', '1.7', 'Muslim scientists and their contributions', 'مسلمان سائنس دان اور ان کی خدمات', 'مسلمان ساینس پوهان او د هغوی خدمتونه', [18, 19])
    s.p('Muslim scientists contributed a lot of knowledge to the science of biology and medicines from 8th to 15th century. Their views were highly respected and taken as authority. Some of the famous Muslim scientists are:',
        'مسلمان سائنس دانوں نے آٹھویں سے پندرہویں صدی تک حیاتیات اور طب کی سائنس میں بہت زیادہ علم کا اضافہ کیا۔ ان کی آرا کا بے حد احترام کیا جاتا تھا اور انہیں سند مانا جاتا تھا۔ چند مشہور مسلمان سائنس دان یہ ہیں:',
        'مسلمانو ساینس پوهانو له اتمې تر پنځلسمې پېړۍ پورې د بیولوژي او طب ساینس ته ډېره پوهه ورزیاته کړه. د هغوی نظریات ډېر درناوی کېدل او د سند په توګه منل کېدل. ځینې مشهور مسلمان ساینس پوهان دا دي:')
    people = [
        ('1.7.1 Jabir Bin Hayyan (721 - 815 AD)', '1.7.1 جابر بن حیان (721 - 815ء)', '1.7.1 جابر بن حیان (721 - 815 ز)',
         'He was born in Iran and practiced medicine in Iraq. He introduced experimental chemistry and also wrote a number of books on plants and animals. Among these, “Al-Nabatat” and “Al-Hayawan” are noteworthy. He was also an astronomer, pharmacist, physician, philosopher and engineer.',
         'وہ ایران میں پیدا ہوئے اور عراق میں طب کی پریکٹس کی۔ انہوں نے تجرباتی کیمیا متعارف کرائی اور پودوں اور جانوروں پر کئی کتابیں بھی لکھیں۔ ان میں ”النباتات“ اور ”الحیوان“ قابلِ ذکر ہیں۔ وہ ماہرِ فلکیات، دوا ساز، طبیب، فلسفی اور انجینئر بھی تھے۔',
         'هغه په ایران کې زېږېدلی و او په عراق کې یې طبابت کاوه. هغه تجربوي کیمیا معرفي کړه او د بوټو او ژویو په اړه یې ګڼ کتابونه هم ولیکل. په دې کې ”النباتات“ او ”الحیوان“ د یادونې وړ دي. هغه ستورپوه، درملپوه، ډاکټر، فیلسوف او انجنیر هم و.'),
        ('1.7.2 Abdul Malik Aasmai (740 - 828 AD)', '1.7.2 عبدالملک اصمعی (740 - 828ء)', '1.7.2 عبدالملک اصمعي (740 - 828 ز)',
         'He was born in Busra. He was regarded as a specialist in animal sciences. He wrote many books on animals and plants. One of his books "Al-Kheil" is about horses, another, "Al-Ibil" about camels, a third "A-sha" about sheep and fourth "Al-Wahoosh" is about wild animals. In the book "Khalaq-ul-Insan", he had described different parts and functions of human body.',
         'وہ بصرہ میں پیدا ہوئے۔ انہیں حیوانی علوم کا ماہر سمجھا جاتا تھا۔ انہوں نے جانوروں اور پودوں پر بہت سی کتابیں لکھیں۔ ان کی ایک کتاب ”الخیل“ گھوڑوں کے بارے میں، دوسری ”الابل“ اونٹوں کے بارے میں، تیسری ”الشاء“ بھیڑوں کے بارے میں اور چوتھی ”الوحوش“ جنگلی جانوروں کے بارے میں ہے۔ کتاب ”خلق الانسان“ میں انہوں نے انسانی جسم کے مختلف حصوں اور افعال کو بیان کیا تھا۔',
         'هغه په بصره کې زېږېدلی و. هغه د حیواني علومو کارپوه ګڼل کېده. هغه د ژویو او بوټو په اړه ډېر کتابونه ولیکل. د هغه یو کتاب ”الخیل“ د اسونو په اړه، بل ”الابل“ د اوښانو په اړه، درېیم ”الشاء“ د پسونو په اړه او څلورم ”الوحوش“ د ځنګلي ژویو په اړه دی. په ”خلق الانسان“ کتاب کې یې د انساني بدن بېلابېلې برخې او دندې بیان کړې وې.'),
        ('1.7.3 Bu Ali Sina (980 - 1037 AD)', '1.7.3 بو علی سینا (980 - 1037ء)', '1.7.3 بو علي سینا (980 - 1037 ز)',
         'He was born near Bukhara. He was among the greatest Muslims scientists and his most valuable contribution was in the field of medicines. He was an expert in Mathematics, Astronomy, Physics and Palaeontology. He worked on the structure, function and diseases of the eye. His book “Al-Qanun-fit-Tibb” was translated into many European languages.',
         'وہ بخارا کے قریب پیدا ہوئے۔ وہ عظیم ترین مسلمان سائنس دانوں میں سے تھے اور ان کی سب سے قیمتی خدمت طب کے شعبے میں تھی۔ وہ ریاضی، فلکیات، طبیعیات اور پیلیئنٹالوجی کے ماہر تھے۔ انہوں نے آنکھ کی ساخت، افعال اور بیماریوں پر کام کیا۔ ان کی کتاب ”القانون فی الطب“ کا کئی یورپی زبانوں میں ترجمہ کیا گیا۔',
         'هغه د بخارا سره نږدې زېږېدلی و. هغه د سترو مسلمانو ساینس پوهانو له ډلې و او تر ټولو ارزښتناک خدمت یې د طب په برخه کې و. هغه د ریاضي، ستورپوهنې، فزیک او پالیونټولوژي کارپوه و. هغه د سترګې په جوړښت، دندې او ناروغیو کار وکړ. د هغه کتاب ”القانون في الطب“ په ډېرو اروپایي ژبو وژباړل شو.'),
        ('1.7.4 Abu - Usman Umar Aljahiz', '1.7.4 ابو عثمان عمر الجاحظ', '1.7.4 ابو عثمان عمر الجاحظ',
         'He wrote the famous book "Al- Haywan" which described his own observations on animals, such as the seasonal migration of fish in river Tigris. Similarly, he described the life system of an ant.',
         'انہوں نے مشہور کتاب ”الحیوان“ لکھی جس میں جانوروں کے بارے میں ان کے اپنے مشاہدات بیان کیے گئے، مثلاً دریائے دجلہ میں مچھلیوں کی موسمی ہجرت۔ اسی طرح انہوں نے چیونٹی کے نظامِ زندگی کو بیان کیا۔',
         'هغه مشهور کتاب ”الحیوان“ ولیکه چې په هغه کې یې د ژویو په اړه خپلې کتنې بیان کړې، لکه د دجلې په سیند کې د کبانو موسمي کډوالي. په همدې ډول یې د مېږي د ژوند سیسټم بیان کړ.'),
        ('1.7.5 Al-Farabi', '1.7.5 الفارابی', '1.7.5 الفارابي',
         'This renowned Hakim and biologist lived in 870 - 950 AD. He wrote two books " Kitab-ul-Nabatat" which is about plants and " Kitab-ul- Haywanat" which is about animals.',
         'یہ مشہور حکیم اور ماہرِ حیاتیات 870 - 950ء میں رہے۔ انہوں نے دو کتابیں لکھیں: ”کتاب النباتات“ جو پودوں کے بارے میں ہے اور ”کتاب الحیوانات“ جو جانوروں کے بارے میں ہے۔',
         'دا نامتو حکیم او بیولوژیست په 870 - 950 ز کې ژوند کاوه. هغه دوه کتابونه ولیکل: ”کتاب النباتات“ چې د بوټو په اړه دی او ”کتاب الحیوانات“ چې د ژویو په اړه دی.'),
        ('1.7.6 Abdul Qasim Ali-Zahravi', '1.7.6 ابو القاسم الزہراوی', '1.7.6 ابو القاسم الزهراوي',
         'This great Muslim surgeon was born in 936 AD and died in 1004 AD. He was famous for the removal of stone from urinary bladder.',
         'یہ عظیم مسلمان جراح 936ء میں پیدا ہوئے اور 1004ء میں وفات پائی۔ وہ مثانے سے پتھری نکالنے کے لیے مشہور تھے۔',
         'دا ستر مسلمان جراح په 936 ز کې زېږېدلی او په 1004 ز کې مړ شو. هغه د مثانې څخه د تیږې د ایستلو لپاره مشهور و.'),
        ('1.7.7 Ibn-ul-Haitham', '1.7.7 ابن الہیثم', '1.7.7 ابن الهیثم',
         'He lived in 965 - 1039 AD and was one of the most outstanding biologists of Muslim word. Basically he was an ophthalmologist. He corrected the Greek concept of vision locating retina as the seat of vision. His famous books" Kitabul Manazir" and " Mizanul Hikma" were translated into Latin, Hebrew, Greek and other western languages.',
         'وہ 965 - 1039ء میں رہے اور مسلم دنیا کے نمایاں ترین ماہرینِ حیاتیات میں سے ایک تھے۔ بنیادی طور پر وہ ماہرِ امراضِ چشم تھے۔ انہوں نے بصارت کے یونانی تصور کی اصلاح کی اور ریٹینا کو بصارت کا مقام قرار دیا۔ ان کی مشہور کتابوں ”کتاب المناظر“ اور ”میزان الحکمۃ“ کا لاطینی، عبرانی، یونانی اور دیگر مغربی زبانوں میں ترجمہ کیا گیا۔',
         'هغه په 965 - 1039 ز کې ژوند کاوه او د اسلامي نړۍ له تر ټولو برجسته بیولوژیستانو څخه و. په اصل کې هغه د سترګو ډاکټر و. هغه د لید یوناني مفکوره سمه کړه او ریټینا یې د لید ځای وټاکه. د هغه مشهور کتابونه ”کتاب المناظر“ او ”میزان الحکمة“ په لاتیني، عبراني، یوناني او نورو لوېدیځو ژبو وژباړل شول.'),
        ('1.7.8 Ali Bin Isa', '1.7.8 علی بن عیسیٰ', '1.7.8 علي بن عیسی',
         'He was a well-known eye specialist. He worked on the structure, function and diseases of the eye. He described 130 diseases of the eye in his book. The book was translated into many European languages.',
         'وہ آنکھوں کے مشہور ماہر تھے۔ انہوں نے آنکھ کی ساخت، افعال اور بیماریوں پر کام کیا۔ انہوں نے اپنی کتاب میں آنکھ کی 130 بیماریاں بیان کیں۔ اس کتاب کا کئی یورپی زبانوں میں ترجمہ کیا گیا۔',
         'هغه د سترګو مشهور متخصص و. هغه د سترګې په جوړښت، دندې او ناروغیو کار وکړ. هغه په خپل کتاب کې د سترګې 130 ناروغۍ بیان کړې. دا کتاب په ډېرو اروپایي ژبو وژباړل شو.'),
        ('1.7.9 Ibn-ul-Nafees', '1.7.9 ابن النفیس', '1.7.9 ابن النفیس',
         'He was a renowned biologist of 13th century A.D. He described the circulation of blood in human body.',
         'وہ تیرہویں صدی عیسوی کے مشہور ماہرِ حیاتیات تھے۔ انہوں نے انسانی جسم میں خون کی گردش بیان کی۔',
         'هغه د دیارلسمې زېږدیزې پېړۍ نامتو بیولوژیست و. هغه په انساني بدن کې د وینې دوران بیان کړ.'),
    ]
    for h_en, h_ur, h_ps, en, ur, ps in people:
        s.h(h_en, h_ur, h_ps)
        s.p(en, ur, ps)
    out.append(s)

    s = Section('bio1_8', '1.8', 'Levels of Biological Organization', 'حیاتیاتی تنظیم کی سطحیں', 'د بیولوژیکي تنظیم کچې', [19, 20, 21, 22])
    s.p('Millions of organisms are present on the Earth. They are different from each other and range from the simplest organisms i.e. bacteria to the most complex ones i.e. human beings. The bodies of all living things are made of different parts organized in a certain manner that supports life functions. This organisation includes atoms → molecules → organelles → cells → tissues → organs → organ systems → organisms.',
        'زمین پر لاکھوں جاندار موجود ہیں۔ یہ ایک دوسرے سے مختلف ہیں اور سادہ ترین جانداروں یعنی بیکٹیریا سے لے کر پیچیدہ ترین یعنی انسانوں تک پھیلے ہوئے ہیں۔ تمام جانداروں کے جسم مختلف حصوں سے بنے ہیں جو ایک خاص انداز میں منظم ہیں جو زندگی کے افعال میں مدد دیتا ہے۔ اس تنظیم میں ایٹم ← مالیکیول ← عضیات ← خلیات ← بافتیں ← اعضا ← نظامہائے اعضا ← جاندار شامل ہیں۔',
        'پر ځمکه میلیونونه ژوندي موجودات شته. دوی یو له بل سره توپیر لري او له ساده ترینو موجوداتو یعنې باکتریاوو نیولې تر پېچلو یعنې انسانانو پورې دي. د ټولو ژوندیو شیانو بدنونه له بېلابېلو برخو جوړ دي چې په یو ځانګړي ډول تنظیم شوي او د ژوند دندو ته ملاتړ کوي. په دې تنظیم کې اتومونه ← مالیکولونه ← اورګانیلونه ← حجرې ← نسجونه ← غړي ← د غړو سیسټمونه ← ژوندي موجودات شامل دي.')
    s.p('Level 1: Sub-atomic Particles and Atoms: You know that living and non-living matter is composed of simple units called atoms. Each atom is further composed of sub-atomic particles (electrons, protons and neutrons). The bodies of organisms are made of 16 kinds of elements. These elements are called bio-elements. Out of these bio-elements:',
        'سطح 1: ذیلی ایٹمی ذرات اور ایٹم: آپ جانتے ہیں کہ جاندار اور بے جان مادہ سادہ اکائیوں سے بنا ہے جنہیں ایٹم کہتے ہیں۔ ہر ایٹم مزید ذیلی ایٹمی ذرات (الیکٹران، پروٹان اور نیوٹران) سے بنا ہوتا ہے۔ جانداروں کے جسم 16 قسم کے عناصر سے بنے ہیں۔ ان عناصر کو بائیو ایلیمنٹس کہتے ہیں۔ ان بائیو ایلیمنٹس میں سے:',
        'کچه 1: فرعي اتومي ذرې او اتومونه: تاسو پوهېږئ چې ژوندی او بې ژوندی مواد له ساده واحدونو جوړ دي چې اتومونه بلل کېږي. هر اتوم بیا له فرعي اتومي ذرو (الکترونونو، پروټونونو او نیوټرونونو) جوړ دی. د ژوندیو موجوداتو بدنونه له 16 ډوله عناصرو جوړ دي. دې عناصرو ته بایو عناصر ویل کېږي. له دې بایو عناصرو څخه:')
    s.callout(SI, [('The most complex of all the matter are the living organisms. However, they are made of only 16 elements (bio-elements).',
                    'تمام مادے میں سب سے پیچیدہ جاندار ہیں۔ تاہم وہ صرف 16 عناصر (بائیو ایلیمنٹس) سے بنے ہیں۔',
                    'په ټولو موادو کې تر ټولو پېچلي ژوندي موجودات دي. خو دوی یوازې له 16 عناصرو (بایو عناصرو) جوړ دي.')])
    s.ul([('Only six (O, C, H, N, Ca and P) make 99% of the protoplasm.',
           'صرف چھ (O، C، H، N، Ca اور P) پروٹوپلازم کا 99% بناتے ہیں۔',
           'یوازې شپږ (O، C، H، N، Ca او P) د پروټوپلازم 99% جوړوي.'),
          ('Other ten (K, S, Cl, Na, Mg, Fe, Cu, Mn, Zn and I) collectively make 1% of the protoplasm.',
           'باقی دس (K، S، Cl، Na، Mg، Fe، Cu، Mn، Zn اور I) مل کر پروٹوپلازم کا 1% بناتے ہیں۔',
           'نور لس (K، S، Cl، Na، Mg، Fe، Cu، Mn، Zn او I) په ګډه د پروټوپلازم 1% جوړوي.')])
    s.fig('bio1-fig1-2', F.pie_bioelements(F.PIE_EN), F.pie_bioelements(F.PIE_UR), F.pie_bioelements(F.PIE_PS), .45,
          caption=('Figure 1.2: Percentage composition (by mass) of bio-elements in organisms',
                   'شکل 1.2: جانداروں میں بائیو ایلیمنٹس کی فیصد ترکیب (کمیت کے لحاظ سے)',
                   'شکل 1.2: په ژوندیو موجوداتو کې د بایو عناصرو سلنه ترکیب (د کتلې له مخې)'))
    s.p('Level 2: Molecules and Compounds: You know that atoms combine through bonds and form molecules and compounds. Similarly, the atoms of bio-elements combine to form bio-molecules. There are two types of bio-molecules. The bio-molecules with low molecular weight are called micro-molecules e.g. water, amino acids, glucose etc. The bio-molecules with higher molecular weights are called macro-molecules e.g. starch, protein, lipids etc.',
        'سطح 2: مالیکیول اور مرکبات: آپ جانتے ہیں کہ ایٹم بانڈز کے ذریعے مل کر مالیکیول اور مرکبات بناتے ہیں۔ اسی طرح بائیو ایلیمنٹس کے ایٹم مل کر بائیو مالیکیولز بناتے ہیں۔ بائیو مالیکیولز کی دو اقسام ہیں۔ کم مالیکیولی وزن والے بائیو مالیکیولز کو مائیکرو مالیکیولز کہتے ہیں مثلاً پانی، امائنو ایسڈز، گلوکوز وغیرہ۔ زیادہ مالیکیولی وزن والے بائیو مالیکیولز کو میکرو مالیکیولز کہتے ہیں مثلاً نشاستہ، پروٹین، لپڈز وغیرہ۔',
        'کچه 2: مالیکولونه او مرکبونه: تاسو پوهېږئ چې اتومونه د بانډونو له لارې یوځای کېږي او مالیکولونه او مرکبونه جوړوي. په همدې ډول د بایو عناصرو اتومونه یوځای کېږي او بایو مالیکولونه جوړوي. بایو مالیکولونه دوه ډوله دي. هغو بایو مالیکولونو ته چې ټیټ مالیکولي وزن لري مایکرو مالیکولونه ویل کېږي لکه اوبه، امینو اسیدونه، ګلوکوز او نور. هغو بایو مالیکولونو ته چې لوړ مالیکولي وزن لري مکرو مالیکولونه ویل کېږي لکه نشایسته، پروټین، لیپیډونه او نور.')
    s.p('Level 3: Organelles: Different bio-molecules combine together in a specific manner and form sub-cellular structures called organelles e.g. mitochondria, chloroplast, ribosome etc. Each organelle performs a particular function. For example, mitochondria provide energy to the cell and ribosomes prepare proteins.',
        'سطح 3: عضیات: مختلف بائیو مالیکیولز ایک خاص انداز میں مل کر ذیلی خلوی ساختیں بناتے ہیں جنہیں عضیات کہتے ہیں مثلاً مائٹوکونڈریا، کلوروپلاسٹ، رائبوسوم وغیرہ۔ ہر عضیہ ایک خاص کام انجام دیتا ہے۔ مثال کے طور پر، مائٹوکونڈریا خلیے کو توانائی فراہم کرتے ہیں اور رائبوسومز پروٹین تیار کرتے ہیں۔',
        'کچه 3: اورګانیلونه: بېلابېل بایو مالیکولونه په یو ځانګړي ډول یوځای کېږي او فرعي حجروي جوړښتونه جوړوي چې اورګانیلونه بلل کېږي لکه مایټوکونډریا، کلوروپلاسټ، رایبوزوم او نور. هر اورګانیل یوه ځانګړې دنده ترسره کوي. د بېلګې په توګه، مایټوکونډریا حجرې ته انرژي ورکوي او رایبوزومونه پروټین جوړوي.')
    s.p('Level 4: Cells: Cell is the basic structural and functional unit of an organism. It consists of many organelles such as, golgi bodies, mitochondria, lysosomes etc. which perform different specific functions inside the cell.',
        'سطح 4: خلیات: خلیہ کسی جاندار کی بنیادی ساختی اور فعلی اکائی ہے۔ یہ کئی عضیات مثلاً گولجی باڈیز، مائٹوکونڈریا، لائسوسومز وغیرہ پر مشتمل ہوتا ہے جو خلیے کے اندر مختلف مخصوص کام انجام دیتے ہیں۔',
        'کچه 4: حجرې: حجره د ژوندي موجود بنسټیز جوړښتي او دندیز واحد دی. دا له ګڼو اورګانیلونو لکه ګولجي باډیو، مایټوکونډریا، لایزوزومونو او نورو جوړه ده چې د حجرې دننه بېلابېلې ځانګړې دندې ترسره کوي.')
    s.p('In unicellular organisms, a single cell makes the whole body. While in multicellular organisms, there are more levels of biological organization.',
        'یک خلوی جانداروں میں ایک ہی خلیہ پورا جسم بناتا ہے۔ جبکہ کثیر خلوی جانداروں میں حیاتیاتی تنظیم کی مزید سطحیں ہوتی ہیں۔',
        'په یو حجروي موجوداتو کې یوه حجره ټول بدن جوړوي. په داسې حال کې چې په څو حجروي موجوداتو کې د بیولوژیکي تنظیم نورې کچې هم شته.')
    s.callout(STS, [('The heart, brain, kidneys, eyes and arterial blood vessels are main targets of hypertension and hypotension. Due to advancement in technologies, it is now possible to transplant some of these organs, such as; heart, kidneys, liver and lungs. Kidneys are the most commonly transplanted organs; followed by the liver and then the heart. Some tissues can also be transplanted.',
                     'دل، دماغ، گردے، آنکھیں اور شریانیں ہائی بلڈ پریشر اور لو بلڈ پریشر کا بڑا نشانہ ہیں۔ ٹیکنالوجی میں ترقی کی وجہ سے اب ان میں سے بعض اعضا مثلاً دل، گردوں، جگر اور پھیپھڑوں کی پیوند کاری ممکن ہے۔ گردے سب سے زیادہ پیوند کیے جانے والے اعضا ہیں؛ اس کے بعد جگر اور پھر دل۔ بعض بافتوں کی بھی پیوند کاری کی جا سکتی ہے۔',
                     'زړه، دماغ، پښتورګي، سترګې او شریاني رګونه د لوړ او ټیټ فشار اصلي هدفونه دي. د ټکنالوژۍ د پرمختګ له امله اوس د دې ځینو غړو لکه زړه، پښتورګو، ځيګر او سږو پیوند ممکن دی. پښتورګي تر ټولو ډېر پیوند کېدونکي غړي دي؛ ورپسې ځيګر او بیا زړه. ځینې نسجونه هم پیوند کېدای شي.')])
    s.p('Level 5: Tissues: In multicellular organisms, the cells which are similar in structure and perform similar functions make groups. Such groups of cells are called tissues. For example, in plants mesophyll tissue is made of cells which perform photosynthesis. In animals, glandular tissue is made of cells which produce secretions.',
        'سطح 5: بافتیں: کثیر خلوی جانداروں میں وہ خلیات جو ساخت میں ایک جیسے ہوں اور ایک جیسے کام انجام دیں، گروہ بناتے ہیں۔ خلیات کے ایسے گروہوں کو بافتیں کہتے ہیں۔ مثال کے طور پر، پودوں میں میزوفل بافت ان خلیات سے بنی ہوتی ہے جو ضیائی تالیف کرتے ہیں۔ جانوروں میں غدودی بافت ان خلیات سے بنی ہوتی ہے جو رطوبتیں پیدا کرتے ہیں۔',
        'کچه 5: نسجونه: په څو حجروي موجوداتو کې هغه حجرې چې په جوړښت کې ورته وي او ورته دندې ترسره کوي ډلې جوړوي. د حجرو داسې ډلو ته نسجونه ویل کېږي. د بېلګې په توګه، په بوټو کې میزوفیل نسج له هغو حجرو جوړ دی چې فوتوسنتز کوي. په ژویو کې غدوي نسج له هغو حجرو جوړ دی چې افرازات تولیدوي.')
    s.p('Level 6: Organs: Different tissues work together to perform a specific activity. Such a group of related tissues is called an organ. For example, the organ stomach is made of two major tissues. Its epithelial (glandular) tissue secretes gastric juice for the digestion of proteins while its muscular tissue contracts and grinds food.',
        'سطح 6: اعضا: مختلف بافتیں مل کر ایک مخصوص سرگرمی انجام دیتی ہیں۔ متعلقہ بافتوں کے ایسے گروہ کو عضو کہتے ہیں۔ مثال کے طور پر، معدہ نامی عضو دو بڑی بافتوں سے بنا ہے۔ اس کی اپی تھیلیل (غدودی) بافت پروٹین کے ہضم کے لیے معدی رس خارج کرتی ہے جبکہ اس کی عضلاتی بافت سکڑتی ہے اور خوراک کو پیستی ہے۔',
        'کچه 6: غړي: بېلابېل نسجونه یوځای کار کوي ترڅو یو ځانګړی فعالیت ترسره کړي. د اړوندو نسجونو داسې ډلې ته غړی ویل کېږي. د بېلګې په توګه، معده نومی غړی له دوو لویو نسجونو جوړ دی. د هغې اپیتیلیل (غدوي) نسج د پروټینونو د هضم لپاره معدي شیره افرازوي په داسې حال کې چې عضلي نسج یې تړل کېږي او خواړه میده کوي.')
    s.p('Level 7: Organ Systems: The organs in turn coordinate and constitute an organ system which performs a particular function e.g. blood circulatory system in animals. The blood circulatory system is composed of organs like heart, arteries, veins and capillaries.',
        'سطح 7: نظامہائے اعضا: اعضا آگے چل کر باہم ہم آہنگی سے ایک نظامِ اعضا بناتے ہیں جو ایک خاص کام انجام دیتا ہے مثلاً جانوروں میں دورانِ خون کا نظام۔ دورانِ خون کا نظام دل، شریانوں، وریدوں اور شعریوں جیسے اعضا پر مشتمل ہے۔',
        'کچه 7: د غړو سیسټمونه: غړي په خپل وار همغږي کېږي او د غړو یو سیسټم جوړوي چې یوه ځانګړې دنده ترسره کوي لکه په ژویو کې د وینې د دوران سیسټم. د وینې د دوران سیسټم له زړه، شریانونو، وریدونو او شعریه رګونو په څېر غړو جوړ دی.')
    s.p('Level 8: Organism: Different organ systems then collectively form a whole organism. In case of man, different organ systems such as blood circulatory system, respiratory system, digestive system etc. work in coordination. Similarly in plants, root and shoot systems constitute plant body.',
        'سطح 8: جاندار: پھر مختلف نظامہائے اعضا مل کر ایک مکمل جاندار بناتے ہیں۔ انسان کے معاملے میں مختلف نظامہائے اعضا مثلاً دورانِ خون کا نظام، نظامِ تنفس، نظامِ انہضام وغیرہ ہم آہنگی سے کام کرتے ہیں۔ اسی طرح پودوں میں جڑ اور تنے کے نظام پودے کا جسم بناتے ہیں۔',
        'کچه 8: ژوندی موجود: بیا د غړو بېلابېل سیسټمونه په ګډه یو بشپړ ژوندی موجود جوړوي. د انسان په صورت کې د غړو بېلابېل سیسټمونه لکه د وینې د دوران سیسټم، د تنفس سیسټم، د هضم سیسټم او نور په همغږۍ کار کوي. په همدې ډول په بوټو کې د ریښې او ټوکي سیسټمونه د بوټي بدن جوړوي.')
    s.callout(('Levels higher than the organism level:', 'جاندار کی سطح سے بلند سطحیں:', 'د ژوندي موجود له کچې لوړې کچې:'), [
        ('• The group of similar individuals in an area is called a population.', '• کسی علاقے میں ایک جیسے افراد کے گروہ کو آبادی کہتے ہیں۔', '• په یوه سیمه کې د ورته افرادو ډلې ته نفوس ویل کېږي.'),
        ('• Two or more populations of different organisms living together make a community.', '• مختلف جانداروں کی دو یا زیادہ آبادیاں جو اکٹھی رہتی ہیں، کمیونٹی بناتی ہیں۔', '• د بېلابېلو موجوداتو دوه یا ډېر نفوس چې یوځای اوسېږي ټولنه جوړوي.'),
        ('• The community and the non-living components of an area make an ecosystem.', '• کسی علاقے کی کمیونٹی اور بے جان اجزا مل کر ماحولیاتی نظام بناتے ہیں۔', '• د یوې سیمې ټولنه او بې ژوندي اجزا ایکوسیسټم جوړوي.'),
        ('• All the ecosystems of the planet Earth are collectively called the biosphere.', '• کرۂ ارض کے تمام ماحولیاتی نظام مجموعی طور پر بائیوسفیئر کہلاتے ہیں۔', '• د ځمکې سیارې ټولو ایکوسیسټمونو ته په ګډه بایوسفیر ویل کېږي.'),
    ])
    s.callout(('Analysing and Interpreting:', 'تجزیہ اور توضیح:', 'شننه او تفسیر:'),
              [('Enlist five tissues, organs and systems of human body.', 'انسانی جسم کی پانچ بافتوں، اعضا اور نظاموں کی فہرست بنائیں۔', 'د انساني بدن پنځه نسجونه، غړي او سیسټمونه ولیکئ.')])
    s.fig('bio1-fig1-3', F.levels_diagram(F.LEV_EN), F.levels_diagram(F.LEV_UR), F.levels_diagram(F.LEV_PS), .75,
          caption=('Figure 1.3: Diagram showing different Levels of Biological Organization',
                   'شکل 1.3: حیاتیاتی تنظیم کی مختلف سطحیں دکھانے والی شکل',
                   'شکل 1.3: د بیولوژیکي تنظیم بېلابېلې کچې ښودونکی انځور'))
    s.callout(('Activity: Write the levels against each example.', 'سرگرمی: ہر مثال کے سامنے سطح لکھیں۔', 'فعالیت: د هرې بېلګې په وړاندې کچه ولیکئ.'), [])
    s.table('bio1-tab-levels-activity',
            ['Organization', 'Level', 'Organization', 'Level'],
            [['Heart', '', 'Blood', ''], ['C₆H₁₂O₅ (as printed)', '', 'Mitochondria', ''], ['Parenchyma', '', 'Neuron', '']],
            ['تنظیم', 'سطح', 'تنظیم', 'سطح'],
            [['دل', '', 'خون', ''], ['C₆H₁₂O₅ (جیسا چھپا ہے)', '', 'مائٹوکونڈریا', ''], ['پیرنکائما', '', 'نیورون', '']],
            ['تنظیم', 'کچه', 'تنظیم', 'کچه'],
            [['زړه', '', 'وینه', ''], ['C₆H₁₂O₅ (لکه چې چاپ شوی)', '', 'مایټوکونډریا', ''], ['پارینکایما', '', 'نیورون', '']],
            ratio=.9)
    s.p('SpaceBook note: the activity table prints the formula as C₆H₁₂O₅; glucose is C₆H₁₂O₆. The printed value is kept above.',
        'اسپیس بک نوٹ: سرگرمی کے جدول میں فارمولا C₆H₁₂O₅ چھپا ہے؛ گلوکوز کا فارمولا C₆H₁₂O₆ ہے۔ اوپر چھپی ہوئی قدر برقرار رکھی گئی ہے۔',
        'د سپېس بوک یادونه: د فعالیت په جدول کې فورمول C₆H₁₂O₅ چاپ شوی؛ د ګلوکوز فورمول C₆H₁₂O₆ دی. پورته چاپ شوی ارزښت ساتل شوی.',
        editorial=True)
    out.append(s)

    s = Section('bio1_9', '1.9', 'Cellular Organization', 'خلوی تنظیم', 'حجروي تنظیم', [23, 24])
    s.p('All organisms are made of either one (unicellular) or many cells (multi-cellular). Moreover, there are certain organisms which are unicellular but they live in groups and make colonies. This is called colonial form of organism.',
        'تمام جاندار یا تو ایک خلیے (یک خلوی) یا بہت سے خلیات (کثیر خلوی) سے بنے ہیں۔ مزید یہ کہ بعض جاندار یک خلوی ہوتے ہیں لیکن گروہوں میں رہتے ہیں اور کالونیاں بناتے ہیں۔ اسے جاندار کی کالونیل شکل کہتے ہیں۔',
        'ټول ژوندي موجودات یا له یوې حجرې (یو حجروي) یا له ډېرو حجرو (څو حجروي) جوړ دي. سربېره پر دې، ځینې موجودات یو حجروي دي خو په ډلو کې اوسېږي او کلونۍ جوړوي. دې ته د ژوندي موجود کلونیایي بڼه ویل کېږي.')
    s.p('(i) Unicellular Organization: Unicellular organisms such as Amoeba, Chlamydomonas, Euglena etc. have bodies made of single cells and the work is distributed among different organelles of the cells. So there is division of labour among different organelles. Although these are single celled organisms yet they are capable of carrying out all the vital activities of life. Their single cells are capable of respiration, digestion, excretion, reproduction etc. These types of organisms can live independently.',
        '(i) یک خلوی تنظیم: یک خلوی جانداروں مثلاً امیبا، کلیمائیڈوموناس، یوگلینا وغیرہ کے جسم ایک خلیے سے بنے ہوتے ہیں اور کام خلیے کے مختلف عضیات میں تقسیم ہوتا ہے۔ چنانچہ مختلف عضیات کے درمیان تقسیمِ کار ہوتی ہے۔ اگرچہ یہ یک خلوی جاندار ہیں پھر بھی زندگی کی تمام اہم سرگرمیاں انجام دینے کے قابل ہیں۔ ان کے واحد خلیے تنفس، ہضم، اخراج، تولید وغیرہ کے قابل ہیں۔ اس قسم کے جاندار آزادانہ زندگی گزار سکتے ہیں۔',
        '(i) یو حجروي تنظیم: د یو حجروي موجوداتو لکه امیبا، کلامیډوموناس، یوګلینا او نورو بدنونه له یوې حجرې جوړ دي او کار د حجرې په بېلابېلو اورګانیلونو وېشل شوی دی. نو د بېلابېلو اورګانیلونو ترمنځ د کار وېش شته. که څه هم دا یو حجروي موجودات دي خو د ژوند ټول حیاتي فعالیتونه ترسره کولای شي. د دوی یوه حجره د تنفس، هضم، اطراح، تکثر او نورو وړتیا لري. دا ډول موجودات په خپلواکه توګه ژوند کولای شي.')
    s.p('(ii) Colonial Organization: Volvox is a green alga. It is a common example of unicellular colonial organisms. It lives in water. Hundreds of volvox cells make a small volvox colony. Many small colonies make a big colony. Most of the functions are performed by every cell. However, an individual volvox cell cannot live independently as the cells of colony are dependent on each other. For example, there are cells which are specialized for mobility while other cells are for reproduction. Therefore, the division is above the cellular level and this is a trend towards more complex division of labour in multi-cellular organisms.',
        '(ii) کالونیل تنظیم: والوکس ایک سبز الجی ہے۔ یہ یک خلوی کالونیل جانداروں کی ایک عام مثال ہے۔ یہ پانی میں رہتا ہے۔ والوکس کے سینکڑوں خلیات ایک چھوٹی والوکس کالونی بناتے ہیں۔ بہت سی چھوٹی کالونیاں ایک بڑی کالونی بناتی ہیں۔ زیادہ تر کام ہر خلیہ انجام دیتا ہے۔ تاہم والوکس کا انفرادی خلیہ آزادانہ زندہ نہیں رہ سکتا کیونکہ کالونی کے خلیات ایک دوسرے پر منحصر ہوتے ہیں۔ مثال کے طور پر، کچھ خلیات حرکت کے لیے مخصوص ہوتے ہیں جبکہ دوسرے خلیات تولید کے لیے۔ لہٰذا یہ تقسیم خلوی سطح سے بلند ہے اور یہ کثیر خلوی جانداروں میں زیادہ پیچیدہ تقسیمِ کار کی طرف ایک رجحان ہے۔',
        '(ii) کلونیایي تنظیم: والواکس یو شین الجی دی. دا د یو حجروي کلونیایي موجوداتو عامه بېلګه ده. دا په اوبو کې اوسېږي. د والواکس سلګونه حجرې یوه کوچنۍ والواکس کلوني جوړوي. ډېرې کوچنۍ کلونۍ یوه لویه کلوني جوړوي. ډېری دندې هره حجره ترسره کوي. خو د والواکس یوه ځانګړې حجره په خپلواکه توګه ژوندی نه شي پاتې کېدای ځکه چې د کلونۍ حجرې یو پر بل متکي دي. د بېلګې په توګه، ځینې حجرې د حرکت لپاره ځانګړې شوې دي په داسې حال کې چې نورې د تکثر لپاره دي. نو دا وېش له حجروي کچې پورته دی او دا په څو حجروي موجوداتو کې د لا پېچلي کار وېش په لور یو تمایل دی.')
    s.fig('bio1-fig1-4', F.chlamy_volvox(F.CV_EN), F.chlamy_volvox(F.CV_UR), F.chlamy_volvox(F.CV_PS), .9,
          caption=('Figure 1.4: Unicellular Organization (a) Chlamydomonas and Colonial Organization (b) Volvox colonies',
                   'شکل 1.4: یک خلوی تنظیم (a) کلیمائیڈوموناس اور کالونیل تنظیم (b) والوکس کالونیاں',
                   'شکل 1.4: یو حجروي تنظیم (a) کلامیډوموناس او کلونیایي تنظیم (b) د والواکس کلونۍ'))
    s.p('(iii) Multicellular Organization: In multicellular organization, cells are organized into tissues which inturn form organs and organs make organ systems. All plants and animals have multicellular organization.',
        '(iii) کثیر خلوی تنظیم: کثیر خلوی تنظیم میں خلیات بافتوں میں منظم ہوتے ہیں جو آگے اعضا بناتی ہیں اور اعضا نظامہائے اعضا بناتے ہیں۔ تمام پودوں اور جانوروں میں کثیر خلوی تنظیم ہوتی ہے۔',
        '(iii) څو حجروي تنظیم: په څو حجروي تنظیم کې حجرې په نسجونو کې تنظیمېږي چې بیا غړي جوړوي او غړي د غړو سیسټمونه جوړوي. ټول بوټي او ژوي څو حجروي تنظیم لري.')
    s.p('The body of a plant is made of vegetative and reproductive organs. Roots, stem, branches and leaves are the vegetative organs while flowers are the reproductive organs of plants. For example, Mustard plant has multicellular organization.',
        'پودے کا جسم نباتی اور تولیدی اعضا سے بنا ہوتا ہے۔ جڑیں، تنا، شاخیں اور پتے نباتی اعضا ہیں جبکہ پھول پودوں کے تولیدی اعضا ہیں۔ مثال کے طور پر، سرسوں کے پودے میں کثیر خلوی تنظیم ہوتی ہے۔',
        'د بوټي بدن له نباتي او تکثري غړو جوړ دی. ریښې، ډډ، څانګې او پاڼې نباتي غړي دي په داسې حال کې چې ګلان د بوټو تکثري غړي دي. د بېلګې په توګه، د شړشمو بوټی څو حجروي تنظیم لري.')
    s.p('Similarly, the body of an animal is made of different organ systems e.g. digestive system, respiratory system, blood circulatory system, nervous system, reproductive system etc. For example, frog shows multicellular organization.',
        'اسی طرح جانور کا جسم مختلف نظامہائے اعضا مثلاً نظامِ انہضام، نظامِ تنفس، دورانِ خون کا نظام، اعصابی نظام، تولیدی نظام وغیرہ سے بنا ہوتا ہے۔ مثال کے طور پر، مینڈک کثیر خلوی تنظیم ظاہر کرتا ہے۔',
        'په همدې ډول د ژوي بدن د غړو له بېلابېلو سیسټمونو لکه د هضم سیسټم، د تنفس سیسټم، د وینې د دوران سیسټم، عصبي سیسټم، تکثري سیسټم او نورو جوړ دی. د بېلګې په توګه، چنګښه څو حجروي تنظیم ښيي.')
    s.fig('bio1-fig1-5', F.mustard_frog(F.MF_EN), F.mustard_frog(F.MF_UR), F.mustard_frog(F.MF_PS), .6,
          caption=('Figure 1.5: Multicellular Organization', 'شکل 1.5: کثیر خلوی تنظیم', 'شکل 1.5: څو حجروي تنظیم'))
    s.callout(('Activity', 'سرگرمی', 'فعالیت'),
              [('Draw the diagrams of digestive and respiratory systems of man and label their main organs.',
                'انسان کے نظامِ انہضام اور نظامِ تنفس کی اشکال بنائیں اور ان کے اہم اعضا کے نام لکھیں۔',
                'د انسان د هضم او تنفس د سیسټمونو انځورونه رسم کړئ او د هغوی اصلي غړي نښه کړئ.')])
    out.append(s)
    return out
