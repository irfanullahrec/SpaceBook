# -*- coding: utf-8 -*-
"""Unit 1 part A — PDF 7-10 (printed 1-4): SLOs, opening, 1.1, 1.2, 1.3.1-1.3.2."""
from bio9_tools import Section, photo_figure

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')


def sections():
    out = []

    # PDF 7 (printed 1) — unit opener and learning outcomes
    s = Section('bio1_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [7])
    s.h('After studying this unit, the students will be able to:',
        'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ:',
        'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې:')
    s.ul([
        ('Define biology, its major divisions i.e. Botany, Zoology and Microbiology.',
         'حیاتیات اور اس کے بڑے شعبوں یعنی نباتیات، حیوانیات اور خرد حیاتیات کی تعریف کر سکیں۔',
         'بیولوژي او د هغې لویې څانګې یعنې بوټپوهنه، ژوپوهنه او مایکروبیولوژي تعریف کړي.'),
        ('Define the branches of Biology.',
         'حیاتیات کی شاخوں کی تعریف کر سکیں۔',
         'د بیولوژي څانګې تعریف کړي.'),
        ('Link the study of biology with that of Physics, Chemistry, Mathematics, Geography and Economics.',
         'حیاتیات کے مطالعے کا طبیعیات، کیمیا، ریاضی، جغرافیہ اور معاشیات کے مطالعے سے ربط قائم کر سکیں۔',
         'د بیولوژي مطالعه له فزیک، کیمیا، ریاضي، جغرافیې او اقتصاد سره وتړي.'),
        ('Explain how the study of biology can lead to different careers.',
         'وضاحت کر سکیں کہ حیاتیات کا مطالعہ کس طرح مختلف پیشوں کی طرف لے جا سکتا ہے۔',
         'تشریح کړي چې د بیولوژي مطالعه څنګه بېلابېلو مسلکونو ته لار پرانیزي.'),
        ('Identify that living organisms are divided into five groups i.e. prokaryotes, protists, fungi, plants and animals.',
         'شناخت کر سکیں کہ جاندار پانچ گروہوں یعنی پروکیریوٹس، پروٹسٹس، فنجائی، پودوں اور جانوروں میں تقسیم ہیں۔',
         'وپېژني چې ژوندي موجودات په پنځو ډلو ویشل شوي دي یعنې پروکاریوټونه، پروټیسټونه، فنجای، بوټي او ژوي.'),
        ('Relate at least three verses from the Holy Quran, instructing for the study of the origin and the characteristics of life, with the modern scientific achievements.',
         'قرآن مجید کی کم از کم تین آیات، جو زندگی کی ابتدا اور خصوصیات کے مطالعے کی ہدایت کرتی ہیں، کا جدید سائنسی کامیابیوں سے تعلق بیان کر سکیں۔',
         'د قرآن کریم لږ تر لږه درې آیتونه چې د ژوند د پیل او ځانګړتیاوو د مطالعې لارښوونه کوي، له عصري ساینسي لاسته راوړنو سره وتړي.'),
        ('Relate the contributions of Jaber Bin Hayan, Abdul Malik Asmai and Bu Ali Sina with the current knowledge about plants and animals.',
         'جابر بن حیان، عبدالملک اصمعی اور بو علی سینا کی خدمات کا پودوں اور جانوروں کے بارے میں موجودہ علم سے تعلق بیان کر سکیں۔',
         'د جابر بن حیان، عبدالملک اصمعي او بو علي سینا خدمتونه د بوټو او ژویو په اړه له اوسني پوهې سره وتړي.'),
        ('Describe bioelements as the most basic level of biological organization.',
         'بائیو ایلیمنٹس کو حیاتیاتی تنظیم کی سب سے بنیادی سطح کے طور پر بیان کر سکیں۔',
         'بایو عناصر د بیولوژیکي تنظیم د تر ټولو بنسټیزې کچې په توګه بیان کړي.'),
        ('Define biomolecules and distinguish them as micromolecules and macromolecules.',
         'بائیو مالیکیولز کی تعریف کر سکیں اور ان میں مائیکرو مالیکیولز اور میکرو مالیکیولز کے طور پر فرق کر سکیں۔',
         'بایو مالیکولونه تعریف کړي او د مایکرو مالیکولونو او مکرو مالیکولونو په توګه یې توپیر وکړي.'),
        ('Describe the level of organization of life (organelles, cells, tissues, organs, organ systems and individuals).',
         'زندگی کی تنظیم کی سطحیں (عضیات، خلیات، بافتیں، اعضا، نظامہائے اعضا اور افراد) بیان کر سکیں۔',
         'د ژوند د تنظیم کچې (اورګانیلونه، حجرې، نسجونه، غړي، د غړو سیسټمونه او افراد) بیان کړي.'),
        ('Explain division of labor among cells and tissues in a multicellular organism.',
         'کثیر خلوی جاندار میں خلیات اور بافتوں کے درمیان تقسیمِ کار کی وضاحت کر سکیں۔',
         'په څو حجروي ژوندي موجود کې د حجرو او نسجونو ترمنځ د کار وېش تشریح کړي.'),
        ('Compare cellular organization in organisms i.e. unicellular organization (Amoeba), colonial organization (Volvox) and multicellular organization (mustard and frog). (Only brief comparison referring to cellular organization is required. Details of organs and organ-systems of frog and mustard should be avoided).',
         'جانداروں میں خلوی تنظیم یعنی یک خلوی تنظیم (امیبا)، کالونیل تنظیم (والوکس) اور کثیر خلوی تنظیم (سرسوں اور مینڈک) کا موازنہ کر سکیں۔ (صرف خلوی تنظیم کے حوالے سے مختصر موازنہ درکار ہے۔ مینڈک اور سرسوں کے اعضا اور نظامہائے اعضا کی تفصیل سے گریز کیا جائے۔)',
         'په ژوندیو موجوداتو کې حجروي تنظیم یعنې یو حجروي تنظیم (امیبا)، کلونیایي تنظیم (والواکس) او څو حجروي تنظیم (شړشم او چنګښه) پرتله کړي. (یوازې د حجروي تنظیم په اړه لنډه پرتله پکار ده. د چنګښې او شړشمو د غړو او د غړو د سیسټمونو له جزیاتو دې ډډه وشي.)'),
    ])
    out.append(s)

    # PDF 8 (printed 2) — opening paragraphs and Figure 1.1
    s = Section('bio1_intro', 'Intro', 'Introduction to Biology', 'حیاتیات کا تعارف', 'بیولوژي ته پېژندنه', [8])
    s.p('Have you ever wondered about the beauty of things in the world! They are not only beautiful but fascinating too. They are fascinating especially because of the variation in their size, shape, colour, eating habits, habitats etc. Human beings have always been interested in observing and studying living organisms. The history of such study is perhaps as old as the history of mankind.',
        'کیا آپ نے کبھی دنیا کی چیزوں کی خوبصورتی پر غور کیا ہے! یہ نہ صرف خوبصورت بلکہ دلکش بھی ہیں۔ یہ خاص طور پر اپنی جسامت، شکل، رنگ، کھانے کی عادات، مساکن وغیرہ میں تنوع کی وجہ سے دلکش ہیں۔ انسان ہمیشہ سے جانداروں کے مشاہدے اور مطالعے میں دلچسپی رکھتا آیا ہے۔ اس طرح کے مطالعے کی تاریخ شاید اتنی ہی پرانی ہے جتنی انسان کی تاریخ۔',
        'ایا تاسو کله د نړۍ د شیانو په ښکلا فکر کړی دی! دا نه یوازې ښکلي بلکې زړه راښکونکي هم دي. دا په ځانګړي ډول د خپل جسامت، بڼې، رنګ، د خوړو عادتونو، استوګنځایونو او نورو د توپیر له امله زړه راښکونکي دي. انسانان تل د ژوندیو موجوداتو په کتنه او مطالعه کې لېوال پاتې شوي دي. د داسې مطالعې تاریخ ښايي هومره زوړ وي لکه د انسان تاریخ.')
    s.p('In this unit, we will study about the branch of science that explores living things i.e. biology and its relationship with other branches of science and also the levels of organization in living organisms.',
        'اس یونٹ میں ہم سائنس کی اس شاخ کا مطالعہ کریں گے جو جانداروں کی کھوج کرتی ہے یعنی حیاتیات، اور سائنس کی دوسری شاخوں سے اس کے تعلق اور جانداروں میں تنظیم کی سطحوں کا بھی مطالعہ کریں گے۔',
        'په دې یونټ کې به موږ د ساینس هغه څانګه مطالعه کړو چې ژوندي شیان څېړي یعنې بیولوژي، او د ساینس له نورو څانګو سره د هغې اړیکه او په ژوندیو موجوداتو کې د تنظیم کچې به هم ولولو.')
    items = [('a)', 'Bacteria'), ('b)', 'Monkey'), ('c)', 'Insect'), ('d)', 'Fern'), ('e)', 'Frog'), ('f)', 'Mushroom')]
    items_ur = [('a)', 'بیکٹیریا'), ('b)', 'بندر'), ('c)', 'کیڑا'), ('d)', 'فرن'), ('e)', 'مینڈک'), ('f)', 'کھمبی')]
    items_ps = [('a)', 'باکتریا'), ('b)', 'بیزو'), ('c)', 'حشره'), ('d)', 'فرن'), ('e)', 'چنګښه'), ('f)', 'مرخېړی')]
    s.fig('bio1-fig1-1',
          photo_figure('Figure 1.1: A collection of living organisms around us', items, 'Six living organisms (photographs in the book)'),
          photo_figure('شکل 1.1', items_ur, 'چھ جاندار (کتاب میں تصاویر)'),
          photo_figure('شکل 1.1', items_ps, 'شپږ ژوندي موجودات (په کتاب کې انځورونه)'),
          .6,
          caption=('Figure 1.1: A collection of living organisms around us: a) Bacteria b) Monkey c) Insect d) Fern e) frog f) Mushroom',
                   'شکل 1.1: ہمارے اردگرد جانداروں کا ایک مجموعہ: a) بیکٹیریا b) بندر c) کیڑا d) فرن e) مینڈک f) کھمبی',
                   'شکل 1.1: زموږ شاوخوا د ژوندیو موجوداتو یوه ټولګه: a) باکتریا b) بیزو c) حشره d) فرن e) چنګښه f) مرخېړی'))
    out.append(s)

    # PDF 9 (printed 3) — 1.1
    s = Section('bio1_1', '1.1', 'Introduction to Biology', 'حیاتیات کا تعارف', 'بیولوژي ته پېژندنه', [9])
    s.p('Biology is the science of life. The word “Biology” is derived from two Greek words “Bio” means \'life\' and “Logos” means \'to study\'. In 1736, a Swedish Scientist Carl Linneaus for the first time used the word biology. Biology has three major divisions:',
        'حیاتیات زندگی کی سائنس ہے۔ لفظ ”بائیولوجی“ دو یونانی الفاظ سے ماخوذ ہے: ”بائیو“ یعنی ’زندگی‘ اور ”لوگوس“ یعنی ’مطالعہ کرنا‘۔ 1736ء میں سویڈن کے سائنس دان کارل لینیئس نے پہلی بار لفظ بائیولوجی استعمال کیا۔ حیاتیات کے تین بڑے شعبے ہیں:',
        'بیولوژي د ژوند ساینس دی. د ”بیولوژي“ کلمه له دوو یوناني کلمو اخیستل شوې: ”بایو“ یعنې ’ژوند‘ او ”لوګوس“ یعنې ’مطالعه کول‘. په 1736 کال کې سویډني ساینس پوه کارل لینیوس د لومړي ځل لپاره د بیولوژي کلمه وکاروله. بیولوژي درې لویې څانګې لري:')
    s.ol([
        ('(i) Botany: It is the study of plants.', '(i) نباتیات (باٹنی): یہ پودوں کا مطالعہ ہے۔', '(i) بوټپوهنه (باټني): دا د بوټو مطالعه ده.'),
        ('(ii) Zoology: It is the study of animals.', '(ii) حیوانیات (زوآلوجی): یہ جانوروں کا مطالعہ ہے۔', '(ii) ژوپوهنه (زوولوجي): دا د ژویو مطالعه ده.'),
        ('(iii) Microbiology: It is the study of microorganisms e.g. viruses, bacteria and microscopic fungi.',
         '(iii) خرد حیاتیات (مائیکرو بائیولوجی): یہ خرد جانداروں مثلاً وائرس، بیکٹیریا اور خوردبینی فنجائی کا مطالعہ ہے۔',
         '(iii) مایکروبیولوژي: دا د مایکرو ژوندیو موجوداتو لکه ویروسونو، باکتریاوو او مایکروسکوپي فنجای مطالعه ده.'),
    ])
    out.append(s)

    # PDF 9-10 (printed 3-4) — 1.2
    s = Section('bio1_2', '1.2', 'Branches of Biology', 'حیاتیات کی شاخیں', 'د بیولوژي څانګې', [9, 10])
    s.p('Biology is a fast growing field of science. Therefore, it is divided into many specialised branches for better understanding and convenience. The following are the main branches of biology.',
        'حیاتیات سائنس کا تیزی سے بڑھتا ہوا شعبہ ہے۔ اس لیے بہتر سمجھ اور سہولت کے لیے اسے کئی خصوصی شاخوں میں تقسیم کیا گیا ہے۔ حیاتیات کی بڑی شاخیں درج ذیل ہیں۔',
        'بیولوژي د ساینس په چټکۍ وده کوونکې څانګه ده. له همدې امله د ښه پوهېدو او اسانتیا لپاره په ډېرو ځانګړو څانګو ویشل شوې ده. د بیولوژي اصلي څانګې دا دي.')
    s.callout(SI, [('In biology, “structure” means any part of the living organism that can be seen with the naked eye or with the help of microscope.',
                    'حیاتیات میں ”ساخت“ سے مراد جاندار کا کوئی بھی حصہ ہے جسے کھلی آنکھ سے یا خوردبین کی مدد سے دیکھا جا سکے۔',
                    'په بیولوژي کې ”جوړښت“ د ژوندي موجود هر هغه برخه ده چې په سترګو یا د مایکروسکوپ په مرسته ولیدل شي.')])
    s.lines([
        ('i. Morphology is the study of form, shape and structure of organisms.',
         'i. مارفولوجی جانداروں کی صورت، شکل اور ساخت کا مطالعہ ہے۔',
         'i. مورفولوجي د ژوندیو موجوداتو د بڼې، شکل او جوړښت مطالعه ده.'),
        ('ii. Anatomy is the study of internal structures of organisms.',
         'ii. اناٹومی جانداروں کی اندرونی ساختوں کا مطالعہ ہے۔',
         'ii. اناټومي د ژوندیو موجوداتو د داخلي جوړښتونو مطالعه ده.'),
        ('iii. Histology is the study of the composition, structure and functions of plant and animal tissues.',
         'iii. ہسٹالوجی پودوں اور جانوروں کی بافتوں کی ترکیب، ساخت اور افعال کا مطالعہ ہے۔',
         'iii. هسټولوجي د بوټو او ژویو د نسجونو د ترکیب، جوړښت او دندو مطالعه ده.'),
        ('iv. Physiology deals with the functions of different parts of organisms and the activities occurring in them.',
         'iv. فزیالوجی جانداروں کے مختلف حصوں کے افعال اور ان میں ہونے والی سرگرمیوں سے متعلق ہے۔',
         'iv. فزیولوژي د ژوندیو موجوداتو د بېلابېلو برخو له دندو او په هغو کې له روانو فعالیتونو سره سروکار لري.'),
        ('v. Embryology deals with embryo and the phenomena involved in the formation of embryo and its development into a new organism.',
         'v. ایمبریالوجی جنین اور جنین کی تشکیل اور اس کے نئے جاندار میں نشوونما پانے کے عوامل سے متعلق ہے۔',
         'v. امبریولوژي له جنین او د جنین د جوړېدو او په نوي ژوندي موجود بدلېدو له پېښو سره سروکار لري.'),
    ])
    s.callout(SI, [('In embryology, we study the development of an organism from a fertilized egg.',
                    'ایمبریالوجی میں ہم بارآور انڈے سے جاندار کی نشوونما کا مطالعہ کرتے ہیں۔',
                    'په امبریولوژي کې موږ له القاح شوې هګۍ څخه د ژوندي موجود وده مطالعه کوو.')])
    s.lines([
        ('vi. Taxonomy is the study of classification of organisms and their scientific naming.',
         'vi. ٹیکسانومی جانداروں کی درجہ بندی اور ان کے سائنسی نام رکھنے کا مطالعہ ہے۔',
         'vi. ټکسانومي د ژوندیو موجوداتو د ډلبندۍ او د هغوی د ساینسي نوم ایښودنې مطالعه ده.'),
        ('vii. Cell Biology or cytology is the study of cells and their organelles.',
         'vii. سیل بائیولوجی یا سائٹالوجی خلیات اور ان کے عضیات کا مطالعہ ہے۔',
         'vii. د حجرې بیولوژي یا سایټولوژي د حجرو او د هغوی د اورګانیلونو مطالعه ده.'),
        ('viii. Palaeontology is the study of fossils of past organisms. The study of fossils of plants is called Paleobotany and the study of fossils of animals is called Paleozoology.',
         'viii. پیلیئنٹالوجی گزرے ہوئے جانداروں کے فوسلز کا مطالعہ ہے۔ پودوں کے فوسلز کے مطالعے کو پیلیو باٹنی اور جانوروں کے فوسلز کے مطالعے کو پیلیو زوآلوجی کہتے ہیں۔',
         'viii. پالیونټولوژي د تېرو ژوندیو موجوداتو د فوسیلونو مطالعه ده. د بوټو د فوسیلونو مطالعې ته پالیوباټني او د ژویو د فوسیلونو مطالعې ته پالیوزوولوجي ویل کېږي.'),
        ('ix. Immunology deals with the body\'s system of defence against disease-causing microorganisms.',
         'ix. امیونولوجی بیماری پیدا کرنے والے خرد جانداروں کے خلاف جسم کے دفاعی نظام سے متعلق ہے۔',
         'ix. امیونولوژي د ناروغۍ زېږوونکو مایکرو ژوندیو موجوداتو پر وړاندې د بدن له دفاعي سیسټم سره سروکار لري.'),
        ('x. Entomology deals with the study of insects.',
         'x. اینٹومولوجی کیڑوں (حشرات) کے مطالعے سے متعلق ہے۔',
         'x. انټومولوژي د حشراتو له مطالعې سره سروکار لري.'),
    ])
    s.callout(SI, [('The Greek word “entomon” meaning “notched” refers to the segmented body of the insect.',
                    'یونانی لفظ ”اینٹومون“ جس کا مطلب ”دندانے دار“ ہے، کیڑے کے قطعات میں بٹے ہوئے جسم کی طرف اشارہ کرتا ہے۔',
                    'یوناني کلمه ”انټومون“ چې معنا یې ”غاښ لرونکی/ټوټه ټوټه“ ده، د حشرې ټوټه ټوټه بدن ته اشاره کوي.')])
    s.lines([
        ('xi. Genetics deals with the study of transmission of characters from parents to off springs.',
         'xi. جینیٹکس والدین سے اولاد میں خصوصیات کی منتقلی کے مطالعے سے متعلق ہے۔',
         'xi. جنیټیک له مور او پلار څخه اولاد ته د ځانګړتیاوو د لېږد له مطالعې سره سروکار لري.'),
        ('xii. Biotechnology is the study of the use of organisms for the benefit and welfare of humanity.',
         'xii. بائیو ٹیکنالوجی انسانیت کے فائدے اور بہبود کے لیے جانداروں کے استعمال کا مطالعہ ہے۔',
         'xii. بایوټکنالوژي د بشریت د ګټې او هوساینې لپاره د ژوندیو موجوداتو د کارونې مطالعه ده.'),
        ('xiii. Environmental biology is the branch of biology which deals with inter-relationship of organisms and their environment.',
         'xiii. ماحولیاتی حیاتیات، حیاتیات کی وہ شاخ ہے جو جانداروں اور ان کے ماحول کے باہمی تعلق سے متعلق ہے۔',
         'xiii. چاپېریالي بیولوژي د بیولوژي هغه څانګه ده چې د ژوندیو موجوداتو او د هغوی د چاپېریال له متقابلې اړیکې سره سروکار لري.'),
        ('xiv. Parasitology is the branch of biology which deals with the study of parasites and all aspects of parasitism.',
         'xiv. پیراسائٹالوجی، حیاتیات کی وہ شاخ ہے جو طفیلیوں اور طفیلیت کے تمام پہلوؤں کے مطالعے سے متعلق ہے۔',
         'xiv. پاراسایټولوژي د بیولوژي هغه څانګه ده چې د پرازیتونو او د پرازیتیزم د ټولو اړخونو له مطالعې سره سروکار لري.'),
        ('xv. Socio-biology is concerned with the social behavior of some animals such as humans, bees, ants etc. Socio-biology investigates the beneficial relationship among the animals living in the same area.',
         'xv. سوشیو بائیولوجی بعض جانوروں جیسے انسانوں، شہد کی مکھیوں، چیونٹیوں وغیرہ کے سماجی رویے سے متعلق ہے۔ سوشیو بائیولوجی ایک ہی علاقے میں رہنے والے جانوروں کے درمیان مفید تعلق کی تحقیق کرتی ہے۔',
         'xv. ټولنیزه بیولوژي د ځینو ژویو لکه انسانانو، مچیو، مېږیانو او نورو له ټولنیز چلند سره سروکار لري. ټولنیزه بیولوژي په یوه سیمه کې د اوسېدونکو ژویو ترمنځ ګټوره اړیکه څېړي.'),
        ('xvi. Pharmacology is the scientific study of drugs and their effects on the human body. Pharmacology analyze the synthesis and breakdown, biological activity and effects and delivery of drugs.',
         'xvi. فارماکولوجی ادویات اور انسانی جسم پر ان کے اثرات کا سائنسی مطالعہ ہے۔ فارماکولوجی ادویات کی تیاری اور شکست و ریخت، حیاتیاتی سرگرمی اور اثرات اور ترسیل کا تجزیہ کرتی ہے۔',
         'xvi. فارماکولوژي د درملو او پر انساني بدن د هغوی د اغېزو ساینسي مطالعه ده. فارماکولوژي د درملو جوړښت او تجزیه، بیولوژیکي فعالیت او اغېزې او رسونه شنني.'),
    ])
    out.append(s)

    # PDF 10 (printed 4) — 1.3 opening, 1.3.1, 1.3.2
    s = Section('bio1_3', '1.3', 'Linkage of Biology with other Fields of Study', 'حیاتیات کا دیگر شعبہ ہائے علم سے تعلق', 'د بیولوژي اړیکه د مطالعې له نورو برخو سره', [10, 11])
    s.p('The functions and metabolic pathways occurring in living organisms follow the principles of other fields of study like physics, chemistry, geography, economics etc. This type of linkage makes inter-disciplinary sciences. Some of the inter-disciplinary sciences are mentioned below:',
        'جانداروں میں ہونے والے افعال اور میٹابولک راستے مطالعے کے دوسرے شعبوں مثلاً طبیعیات، کیمیا، جغرافیہ، معاشیات وغیرہ کے اصولوں کی پیروی کرتے ہیں۔ اس طرح کا ربط بین الشعبہ جاتی علوم بناتا ہے۔ کچھ بین الشعبہ جاتی علوم درج ذیل ہیں:',
        'په ژوندیو موجوداتو کې روانې دندې او میټابولیکي لارې د مطالعې د نورو برخو لکه فزیک، کیمیا، جغرافیې، اقتصاد او نورو اصول تعقیبوي. دا ډول اړیکه بین الرشتوي علوم جوړوي. ځینې بین الرشتوي علوم لاندې یاد شوي دي:')
    s.p('1.3.1 Biophysics is an inter-disciplinary study of understanding biological phenomena and problems using the principles and techniques of physics. It is used in physiology, bioenergetics, neurosciences, pharmacology etc. For example, photosynthesis follows the laws of physics during the absorption of light.',
        '1.3.1 بائیو فزکس طبیعیات کے اصولوں اور طریقوں کو استعمال کرتے ہوئے حیاتیاتی مظاہر اور مسائل کو سمجھنے کا بین الشعبہ جاتی مطالعہ ہے۔ یہ فزیالوجی، بائیو انرجیٹکس، نیورو سائنسز، فارماکولوجی وغیرہ میں استعمال ہوتا ہے۔ مثال کے طور پر، ضیائی تالیف روشنی جذب کرنے کے دوران طبیعیات کے قوانین کی پیروی کرتی ہے۔',
        '1.3.1 بایوفزیک د فزیک د اصولو او تخنیکونو په کارولو سره د بیولوژیکي پدیدو او ستونزو د پوهېدو بین الرشتوي مطالعه ده. دا په فزیولوژي، بایوانرژیټیک، نیوروساینس، فارماکولوژي او نورو کې کارول کېږي. د بېلګې په توګه، فوتوسنتز د رڼا د جذبولو پر مهال د فزیک قوانین تعقیبوي.')
    s.p('1.3.2 Biochemistry is concerned with chemical substances and processes that occur in organisms. It involves the structural analysis of the organic compounds that make up cells and of those that play key roles in chemical reactions of life (e.g., photosynthesis and respiration reactions).',
        '1.3.2 بائیو کیمسٹری جانداروں میں پائے جانے والے کیمیائی مادوں اور عوامل سے متعلق ہے۔ اس میں ان نامیاتی مرکبات کا ساختی تجزیہ شامل ہے جن سے خلیات بنتے ہیں اور جو زندگی کے کیمیائی تعاملات (مثلاً ضیائی تالیف اور تنفس کے تعاملات) میں کلیدی کردار ادا کرتے ہیں۔',
        '1.3.2 بایوکیمیا په ژوندیو موجوداتو کې له کیمیاوي موادو او پروسو سره سروکار لري. په دې کې د هغو عضوي مرکبونو جوړښتي تحلیل شامل دی چې حجرې ترې جوړېږي او د ژوند په کیمیاوي تعاملونو (لکه فوتوسنتز او تنفس) کې کلیدي رول لري.')
    out.append(s)
    return out
