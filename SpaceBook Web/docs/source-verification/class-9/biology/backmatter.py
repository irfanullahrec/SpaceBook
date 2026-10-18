# -*- coding: utf-8 -*-
"""Back matter — PDF 210-223 (printed 207-220): glossary, index, references, authors. PDF 224-225 recorded as excluded."""
from bio9_tools import Section
from gloss_a import G210, G211, G212, G213
from gloss_b import G214, G215, G216, G217

# Index entries: (term, pages, urdu, pashto) — PDF 218-219 (printed 215-216)
INDEX = [
    ('A', [('Abdul Malik Asmai', '12', 'عبدالملک اصمعی', 'عبدالملک اصمعي'), ('Active and Passive transport of matter', '83', 'مادے کی فعال اور غیر فعال نقل و حمل', 'د موادو فعال او غیر فعال لېږد'), ('Aerobic respiration', '139', 'ہوائی تنفس', 'هوايي تنفس'),
           ('Al-Jahiz', '43', 'الجاحظ', 'الجاحظ'), ('Anaerobic Respiration', '139', 'غیر ہوائی تنفس', 'غیر هوايي تنفس'), ('Animal tissues', '92', 'حیوانی بافتیں', 'حیواني نسجونه'), ('Anton van Leeuwenhoek', '65', 'اینٹون وان لیوون ہک', 'انټون وان لیوونهوک'),
           ('Apoptosis', '111', 'ایپوپٹوسس', 'اپوپټوزس'), ('Aristotle', '42', 'ارسطو', 'ارسطو'), ('ATP', '131', 'ATP', 'ATP')]),
    ('B', [('Balanced diet', '159', 'متوازن غذا', 'متوازن خوراک'), ('Binomial nomenclature', '50', 'دو اسمی نظامِ تسمیہ', 'دوه نومیز نوم ایښودنه'), ('Biochemistry', '4', 'حیاتیاتی کیمیا', 'بایوکیمیا'), ('Biodiversity', '38', 'حیاتیاتی تنوع', 'ژوندي تنوع'),
           ('Bioeconomics', '5', 'بائیو اکنامکس', 'بایواکونومیکس'), ('Bioenergetics', '130', 'بائیو انرجیٹکس', 'بایوانرژیټیک'), ('Biogeography', '5', 'حیاتیاتی جغرافیہ', 'ژوندي جغرافیه'), ('Biological diversity', '38', 'حیاتیاتی تنوع', 'بیولوژیکي تنوع'),
           ('Biological Method', '24', 'حیاتیاتی طریقۂ کار', 'بیولوژیکي طریقه'), ('Biophysics', '4', 'حیاتیاتی طبیعیات', 'بایوفزیک'), ('Biosphere', '15', 'حیاتی کرہ', 'ژوندي کره'), ('Biostatistics or biometry', '5', 'حیاتیاتی شماریات یا بائیومیٹری', 'بایوسټاټسټیک یا بایومېټري'),
           ('Blind dolphin', '57', 'نابینا ڈولفن', 'ړوند ډولفین'), ('Blood Disorders', '191', 'خون کی خرابیاں', 'د وینې اختلالات'), ('Blood Vessels', '197', 'خون کی نالیاں', 'د وینې رګونه'), ('Blood', '187', 'خون', 'وینه'),
           ('Branches of Biology', '3', 'حیاتیات کی شاخیں', 'د بیولوژۍ څانګې'), ('Brassica campestris', '18, 42', 'براسیکا کیمپیسٹرس', 'براسیکا کمپسټرس'), ('Bu Ali Sina', '12', 'بو علی سینا', 'بوعلي سینا')]),
    ('C', [('Carbohydrates', '153', 'کاربوہائیڈریٹس', 'کاربوهایډریټونه'), ('Cardiac Cycle', '196', 'کارڈیک سائیکل', 'د زړه دوره'), ('Careers in Biology', '5', 'حیاتیات میں پیشے', 'په بیولوژۍ کې مسلکونه'), ('Carolus Linnaeus', '40', 'کیرولس لینیئس', 'کارولوس لینیوس'),
           ('Cell cycle', '100', 'خلوی چکر', 'حجروي دوره'), ('Cell membrane', '72', 'خلوی جھلی', 'حجروي غشا'), ('Characteristics Of Enzymes', '118', 'انزائمز کی خصوصیات', 'د انزایمونو ځانګړتیاوې'), ('Chlorophyll', '151, 134', 'کلوروفل', 'کلوروفیل'),
           ('Chloroplasts', '76', 'کلوروپلاسٹس', 'کلوروپلاسټونه'), ('Chromoplast', '76', 'کروموپلاسٹ', 'کروموپلاسټ'), ('Conversation of biodiversity', '57', 'حیاتیاتی تنوع کا تحفظ', 'د ژوندي تنوع ساتنه'), ('Classification Systems,', '39', 'درجہ بندی کے نظام', 'د ډلبندۍ سیسټمونه'),
           ('Colonial Organization,', '17', 'کالونیل تنظیم', 'کالونیایي تنظیم'), ('Conservation of biodiversity,', '57', 'حیاتیاتی تنوع کا تحفظ', 'د ژوندي تنوع ساتنه'), ('Constipation,', '173', 'قبض', 'قبضیت'), ('Cranes,', '54', 'کونجیں', 'زانګي'), ('Cytoplasm,', '73', 'سائٹوپلازم', 'سایټوپلازم')]),
    ('D', [('Dark reactions (Calvin Cycle)', '136', 'تاریک تعاملات (کیلون سائیکل)', 'تیاره تعاملونه (کالوین دوره)'), ('Deforestation : Causes and effects', '56', 'جنگلات کی کٹائی: وجوہات اور اثرات', 'د ځنګلونو پرې کول: لاملونه او اغېزې'), ('Diarrhea', '174', 'اسہال', 'اسهال'),
           ('Dietary Fibre', '158', 'غذائی ریشہ', 'غذايي فایبر'), ('Difference between prokaryotic and eukaryotic cell', '79', 'پروکیریوٹک اور یوکیریوٹک خلیے میں فرق', 'د پروکاریوټیک او یوکاریوټیک حجرې توپیر'), ('Diffusion', '83', 'نفوذ', 'خپرېدل'),
           ('Discovery of Blood Circulation', '200', 'دورانِ خون کی دریافت', 'د وینې د دوران کشف'), ('Difference between aerobic and anaerobic respiration', '142', 'ہوائی اور غیر ہوائی تنفس میں فرق', 'د هوايي او غیر هوايي تنفس توپیر')]),
    ('E', [('Endoplasmic Reticulum', '74', 'اینڈوپلازمک ریٹیکولم', 'اندوپلازمیک ریټیکولم'), ('Eukaryotes', '79', 'یوکیریوٹس', 'یوکاریوټونه'), ('Erythrocytes', '189', 'اریتھروسائٹس', 'اریتروسایټونه'), ('Emergence of cell theory', '68', 'خلوی نظریے کا ظہور', 'د حجروي تیورۍ راښکاره کېدل')]),
    ('F', [('Factors Affecting Rate Of Transpiration', '183', 'عملِ تبخیر کی شرح پر اثر انداز عوامل', 'د ټرانسپایرېشن پر کچه اغېزمن عوامل'), ('Factors that influence enzyme reaction rates', '122', 'انزائم تعامل کی شرح پر اثر انداز عوامل', 'د انزایم د تعامل پر کچه اغېزمن عوامل'),
           ('Fats', '154', 'چکنائی', 'غوړ'), ('Five kingdom system of classification', '43', 'درجہ بندی کا پانچ مملکتی نظام', 'د ډلبندۍ پنځه سلطنتي سیسټم'), ('Fluid mosaic model', '73', 'فلوئڈ موزیک ماڈل', 'فلویډ موزاییک ماډل')]),
    ('G', [('Golgi bodies', '74', 'گولجی باڈیز', 'ګولجي اجسام'), ('Guard cell', '133', 'محافظ خلیہ', 'ساتونکې حجره')]),
    ('H', [('Hierarchy of Taxonomy', '40', 'درجہ بندی کی ترتیب', 'د ټکسانومۍ درجه بندي'), ('History of classification system', '42', 'درجہ بندی کے نظام کی تاریخ', 'د ډلبندۍ سیسټم تاریخ'), ('Holy Quran and Biological Science', '8', 'قرآنِ پاک اور حیاتیاتی سائنس', 'قرآن کریم او بیولوژیکي ساینس'),
           ('Houbara bastard', '54', 'تلور', 'تلور'), ('Human Digestive System', '164', 'انسانی نظامِ انہضام', 'د انسان هاضمه سیسټم'), ('Human Heart', '194', 'انسانی دل', 'د انسان زړه')]),
    ('I', [('Ibn - Al - Nafees', '13', 'ابن النفیس', 'ابن النفیس'), ('Impact of human beings on biodiversity', '53', 'حیاتیاتی تنوع پر انسانوں کا اثر', 'پر ژوندي تنوع د انسانانو اغېز'), ('Induce Fit Model', '122', 'انڈیوسڈ فٹ ماڈل', 'انډیوسډ فټ ماډل')]),
    ('J', [('Jabir Bin Hayyan', '12', 'جابر بن حیان', 'جابر بن حیان'), ('Jejunum', '170', 'جیجونم', 'جیجونم')]),
    ('L', [('Leucoplast', '76', 'لیوکوپلاسٹ', 'لوکوپلاسټ'), ('Levels of Biological Organization', '13', 'حیاتیاتی تنظیم کی سطحیں', 'د بیولوژیکي تنظیم کچې'), ('Light microscopy', '66', 'لائٹ مائیکروسکوپی', 'د رڼا مایکروسکوپي'),
           ('Lock and Key Model', '121', 'لاک اینڈ کی ماڈل', 'د قلف او کیلي ماډل'), ('Limiting factor in photosynthesis', '137', 'ضیائی تالیف میں محدود کرنے والا عامل', 'په فوتوسنتز کې محدودوونکی عامل'), ('Leucocytes', '189', 'لیوکوسائٹس', 'لوکوسایټونه')]),
    ('M', [('Microscopy', '65', 'مائیکروسکوپی', 'مایکروسکوپي'), ('Macropolo sheep', '57', 'مارکوپولو بھیڑ', 'مارکوپولو پسه'), ('Magnesium', '151', 'میگنیشیم', 'مګنیزیم'), ('Malnutrition', '161', 'سوئے تغذیہ', 'سوءتغذیه'), ('Marasmus', '162', 'میرازمس', 'مرازمس'),
           ('Markhor', '57', 'مارخور', 'مارخور'), ('Matthias Schleiden', '70', 'میتھیاس شلائیڈن', 'ماتیاس شلایډن'), ('Meiosis', '106', 'مییوسس', 'مییوسس'), ('Mineral Deficiency Disease', '162', 'معدنی کمی کی بیماری', 'د معدني کمښت ناروغي'),
           ('Mineral Nutrition in Plants', '149', 'پودوں میں معدنی غذائیت', 'په بوټو کې معدني تغذیه'), ('Mitochondria', '75', 'مائٹوکونڈریا', 'مایټوکانډریا'), ('Mitosis', '102', 'مائٹوسس', 'مایټوسس'), ('Multicelluar Organization', '18', 'کثیر خلوی تنظیم', 'څو حجروي تنظیم')]),
    ('N', [('Necrosis', '112', 'نیکروسس', 'نیکروزس'), ('Nobel Prizes for malaria', '27', 'ملیریا پر نوبل انعامات', 'د ملاریا لپاره د نوبل جایزې')]),
    ('O', [('Osmosis', '85', 'اوسموسس', 'اوسموزس'), ('Oxidation-Reduction reactions', '131', 'تکسید و تخفیف کے تعاملات', 'د اکسیډیشن-ارجاع تعاملونه')]),
    ('P', [('Photosynthesis', '133', 'ضیائی تالیف', 'فوتوسنتز'), ('Plant tissues', '88', 'نباتاتی بافتیں', 'نباتي نسجونه'), ('Proteins', '154', 'پروٹینز', 'پروټینونه'), ('Plasmolyis', '86', 'پلازمولائسس', 'پلازمولیزس'), ('Plasma', '188', 'پلازما', 'پلازما')]),
    ('R', [('Respiration', '138', 'تنفس', 'تنفس'), ('Ribosomes', '75', 'رائبوسومز', 'رایبوزومونه'), ('Robert Brown', '69', 'رابرٹ براؤن', 'رابرټ براون'), ('Robert Hooke', '68', 'رابرٹ ہُک', 'رابرټ هوک'), ('Role of Calcium', '157', 'کیلشیم کا کردار', 'د کلسیم رول'), ('Role of Iron', '157', 'آئرن کا کردار', 'د اوسپنې رول')]),
    ('S', [('Source and sink', '186', 'منبع اور سنک', 'سرچینه او مصرف ځای'), ('Structure of Euglena', '17', 'یوگلینا کی ساخت', 'د یوګلینا جوړښت'), ('Surface area to volume ratio', '80', 'سطحی رقبے اور حجم کی نسبت', 'د سطحې او حجم نسبت'), ('Stomata', '182', 'اسٹومیٹا', 'سټوماټا')]),
    ('T', [('Theodor Schwann', '70', 'تھیوڈور شوان', 'تیوډور شوان'), ('Tissues', '88', 'بافتیں', 'نسجونه'), ('Translocation of organic solutes (food) in plants', '186', 'پودوں میں نامیاتی منحل (خوراک) کی ترسیل', 'په بوټو کې د عضوي منحلو (خوړو) لېږد'),
           ('Transpiration Pull', '185', 'ٹرانسپائریشنل پُل', 'ټرانسپایرېشنل کشش'), ('Transport In Plants', '180', 'پودوں میں نقل و حمل', 'په بوټو کې لېږد'), ('Transport Of Water', '185', 'پانی کی نقل و حمل', 'د اوبو لېږد'), ('Turgor', '85', 'ٹرگر', 'ټرګر')]),
    ('U', [('Ulcers', '174', 'السر', 'زخمونه'), ('Unicellular Organization', '17', 'یک خلوی تنظیم', 'یو حجروي تنظیم')]),
    ('V', [('Veins', '198', 'وریدیں', 'وریدونه'), ('Viruses', '50', 'وائرس', 'ویروسونه'), ('Vitamin A', '155', 'وٹامن A', 'ویټامین A'), ('Vitamin C', '156', 'وٹامن C', 'ویټامین C'), ('Vitamin D', '156', 'وٹامن D', 'ویټامین D'), ('Volvox', '17', 'وولووکس', 'وولوکس')]),
    ('W', [('Water', '158', 'پانی', 'اوبه'), ('William Harvey', '200', 'ولیم ہاروے', 'ویلیم هاروي'), ('White Blood Cells', '189', 'سفید خونی خلیے', 'سپینې وینې حجرې')]),
    ('Z', [('Zygote', '110', 'زائیگوٹ', 'زایګوټ')]),
]

REFS = [
    'Alberts, B., D. Bray, K. Hopkin, A.D. Johnson, J. Lewis, M. Raff, KJ. Roberts, P.Walter. 2012. Essential Cell Biology, 4th Edition Garland Science. ISBN-13: 978-0815344551, ISBN-10: 0815344554',
    'Brooker R.J, Eric. Widmaier, L.Graham, P.Stiling. 2016. Biology 4th Edition McGraw Hill ISBN-13: 978-1259188121, ISBN-10: 1259188124',
    'Garber, S.D. 2002. Biology: A Self-Teaching Guide, 2nd edition John Wiley & Sons ISBN-13: 978-0471223306, ISBN-10: 0471223301',
    'Johnson. G.B. 2016. Essentials of the Living World (WCB General Biology) 5th Edition McGraw-Hill Education. ISBN-13: 978-0078096945, ISBN-10: 0078096944',
    'Kuriyan, J., B.Konforit, D. Wemmer 2012. The Molecules of Life: Physical and Chemical Principles 1st Edition. ISBN-13: 978-0815341888, ISBN-10: 0815341881',
    'Mader, S.S, M. Windelspecht. Biology 12th Edition. McGraw-Hill Education; ISBN-13: 978-0078024269, ISBN-10: 0078024269',
    'Perry J.W., D. Morton, J.B. Perry, B. Cole. 2008. Lab Manual for Majors General Biology 1st Edition. ISBN-13: 978-0495115052, ISBN-10: 0495115053',
    'Tortora, G.J., B.R. Funke, C.L. Case. 2014. Microbiology: An Introduction 12th Edition ISBN-13: 978-0321929150, ISBN-10: 0321929152',
    'Urry, L.A, M.L. Cain, S.A. Wasserman, PV. Minorsky, J.B. Reece. Pearson. 2016. Campbell Biology 11th Edition. ISBN-13: 978-0134093413, ISBN-10: 0134093410',
]
ONLINE = [
    'http://photosynthesiseducation.com/photosynthesis-for-kids/',
    'http://photosynthesiseducation.com/photosynthesis-in-plants/',
    'http://save-the-endangered-species.weebly.com/top-10-most-endangered-plants.html',
    'http://www.wildlife.pk/index.php?cmd=biodiversity&action=biodiversity',
    'https://en.wikibooks.org/wiki/General_Biology',
    'https://portals.iucn.org/library/sites/library/files/documents/1997-073.pdf',
    'https://www.britannica.com/topic-browse/Health-and-Medicine/Diseases-and-Disorders/Digestive-System-Diseases',
    'https://www.mangobaaz.com/these-15-endangered-animals-in-pakistan-are-at-risk-of-extinction/',
    'https://www.mangobaaz.com/these-15-endangered-animals-in-pakistan-are-at-risk-of-extinction/',
    'https://www.researchgate.net/publication/239936897_Biodiversity_in_Pakistan_Key_issues',
    'https://www.scientificamerican.com/article/are-viruses-alive-2004/',
    'https://www.webmd.com/digestive-disorders/default.htm',
]


def gloss_table(s, tid, rows, pdf, printed):
    s.table(tid, ['Term', 'Meaning'], [[r[0], r[1]] for r in rows],
            ['اصطلاح', 'مفہوم'], [[r[2], r[3]] for r in rows],
            ['اصطلاح', 'مانا'], [[r[4], r[5]] for r in rows], ratio=1,
            caption=(f'Glossary — book page {printed} (PDF {pdf})', f'فرہنگ — کتاب کا صفحہ {printed} (PDF {pdf})', f'لغتنامه — د کتاب مخ {printed} (PDF {pdf})'))


def sections():
    out = []
    s = Section('bio_glossary', 'Glossary', 'Glossary', 'فرہنگِ اصطلاحات', 'د اصطلاحاتو لغتنامه', list(range(210, 218)))
    s.p('The textbook ends with a glossary of the biological terms used in the units. The terms below are given in the order printed in the book.',
        'درسی کتاب کے آخر میں یونٹس میں استعمال ہونے والی حیاتیاتی اصطلاحات کی فرہنگ ہے۔ نیچے اصطلاحات کتاب میں چھپی ترتیب سے دی گئی ہیں۔',
        'درسي کتاب په پای کې په یونټونو کې د کارول شویو بیولوژیکي اصطلاحاتو لغتنامه لري. لاندې اصطلاحات د کتاب د چاپ په ترتیب ورکړل شوي.', editorial=True)
    for i, (rows, pdf) in enumerate(((G210, 210), (G211, 211), (G212, 212), (G213, 213), (G214, 214), (G215, 215), (G216, 216), (G217, 217))):
        gloss_table(s, f'bio-gloss-{pdf}', rows, pdf, pdf - 3)
    s.p('SpaceBook note: the book prints "Chaismata" (Chiasmata) and places chiasmata in "the first metaphase"; chiasmata form during prophase I and are still visible at metaphase I. The printed wording is kept.',
        'اسپیس بک نوٹ: کتاب میں ”Chaismata“ (Chiasmata) چھپا ہے اور کیاسمیٹا کو ”پہلے میٹافیز“ میں بتایا گیا ہے؛ کیاسمیٹا پروفیز I میں بنتے ہیں اور میٹافیز I تک نظر آتے ہیں۔ چھپی عبارت رکھی گئی ہے۔',
        'د سپېس بوک یادونه: کتاب ”Chaismata“ (Chiasmata) چاپ کړی او کیازماټا یې په ”لومړي میټافېز“ کې ښودلي؛ کیازماټا په پروفېز I کې جوړېږي او تر میټافېز I پورې ښکاري. چاپ شوی متن ساتل شوی.', editorial=True)
    out.append(s)

    s = Section('bio_index', 'Index', 'Index', 'اشاریہ', 'لړلیک (انډکس)', [218, 219])
    s.p('The page numbers in this index are the printed page numbers of the textbook.', 'اس اشاریے میں صفحات کے نمبر درسی کتاب کے چھپے ہوئے صفحات کے نمبر ہیں۔', 'په دې لړلیک کې د مخونو شمېرې د درسي کتاب چاپ شوې شمېرې دي.', editorial=True)
    for letter, rows in INDEX:
        s.table(f'bio-index-{letter}', [letter, 'Page'], [[r[0], r[1]] for r in rows], [letter, 'صفحہ'], [[r[2], r[1]] for r in rows], [letter, 'مخ'], [[r[3], r[1]] for r in rows], ratio=.6)
    s.p('SpaceBook note: entries are kept as printed, including "Conversation of biodiversity" (conservation), "Houbara bastard" (bustard), "Macropolo sheep" (Marco Polo sheep), "Multicelluar", "Plasmolyis" and "Induce Fit Model". The page number for "Guard cell" is faint in the scan and reads as 133.',
        'اسپیس بک نوٹ: اندراجات چھپی صورت میں رکھے گئے ہیں، بشمول ”Conversation of biodiversity“ (conservation)، ”Houbara bastard“ (bustard)، ”Macropolo sheep“ (Marco Polo sheep)، ”Multicelluar“، ”Plasmolyis“ اور ”Induce Fit Model“۔ ”Guard cell“ کا صفحہ نمبر اسکین میں دھندلا ہے اور 133 پڑھا گیا ہے۔',
        'د سپېس بوک یادونه: لیکنې لکه چې چاپ شوې ساتل شوې، په ګډون د ”Conversation of biodiversity“ (conservation)، ”Houbara bastard“ (bustard)، ”Macropolo sheep“ (Marco Polo sheep)، ”Multicelluar“، ”Plasmolyis“ او ”Induce Fit Model“. د ”Guard cell“ د مخ شمېره په سکن کې تته ده او 133 لوستل شوې.', editorial=True)
    out.append(s)

    s = Section('bio_references', 'References', 'References', 'حوالہ جات', 'سرچینې', [220, 221, 222, 223])
    s.p('The book lists the following references. Book titles, author names and web addresses are kept in their original English form.', 'کتاب میں درج ذیل حوالہ جات دیے گئے ہیں۔ کتابوں کے عنوانات، مصنفین کے نام اور ویب پتے اپنی اصل انگریزی صورت میں رکھے گئے ہیں۔', 'کتاب لاندې سرچینې لېست کړې. د کتابونو سرلیکونه، د لیکوالو نومونه او وېب پتې په اصلي انګرېزي بڼه ساتل شوې.', editorial=True)
    s.h('References', 'حوالہ جات', 'سرچینې')
    s.ul([(r, r, r) for r in REFS])
    s.h('Online learning', 'آن لائن تعلیم', 'آنلاین زده کړه')
    s.ul([(u, u, u) for u in ONLINE])
    s.p('The online list prints the mangobaaz.com address twice; both lines are kept.', 'آن لائن فہرست میں mangobaaz.com کا پتہ دو بار چھپا ہے؛ دونوں سطریں رکھی گئی ہیں۔', 'په آنلاین لېست کې د mangobaaz.com پته دوه ځله چاپ شوې؛ دواړه کرښې ساتل شوې.', editorial=True)
    s.h('About the Authors', 'مصنفین کا تعارف', 'د لیکوالانو پېژندنه')
    s.ul([
        ('Dr. Izhar Ahmad has received his Ph.D degree in the field of Molecular Plant Physiology from the University of York, UK. He has been teaching in Islamia College Peshawar for the last 18 years. He is also supervising MPhil and PhD research scholars. He has 30 research publications in peer review journals and he has attended various international conferences. He is co-author of several textbooks.',
         'ڈاکٹر اظہار احمد نے یونیورسٹی آف یارک، برطانیہ سے مالیکیولر پلانٹ فزیالوجی میں پی ایچ ڈی کی ڈگری حاصل کی۔ وہ گزشتہ 18 سال سے اسلامیہ کالج پشاور میں پڑھا رہے ہیں۔ وہ ایم فل اور پی ایچ ڈی کے محققین کی نگرانی بھی کر رہے ہیں۔ ان کی 30 تحقیقی اشاعتیں ہم مرتبہ جائزہ رسائل میں ہیں اور وہ مختلف بین الاقوامی کانفرنسوں میں شرکت کر چکے ہیں۔ وہ کئی درسی کتب کے شریک مصنف ہیں۔',
         'ډاکټر اظهار احمد د برتانیې د یارک پوهنتون څخه د مالیکولي نباتي فزیولوژۍ په برخه کې د پي اېچ ډي سند ترلاسه کړی. هغه تېرو 18 کلونو راهیسې په اسلامیه کالج پېښور کې تدریس کوي. د ایم فل او پي اېچ ډي څېړونکو څارنه هم کوي. په همکتنو ژورنالونو کې 30 څېړنیزې خپرونې لري او په بېلابېلو نړیوالو کنفرانسونو کې یې ګډون کړی. د څو درسي کتابونو ګډ لیکوال دی.'),
        ('Dr. Zahir Shah is an eminent botanist of Khyber Pakhtunkhwa. He has a vast experience in writing textbooks, reference books and research papers. He has been associated with the teaching profession for the last many decades.',
         'ڈاکٹر ظاہر شاہ خیبر پختونخوا کے ممتاز ماہرِ نباتات ہیں۔ انہیں درسی کتب، حوالہ جاتی کتب اور تحقیقی مقالے لکھنے کا وسیع تجربہ ہے۔ وہ کئی دہائیوں سے تدریس کے پیشے سے وابستہ ہیں۔',
         'ډاکټر ظاهر شاه د خیبر پښتونخوا نامتو نباتپوه دی. د درسي کتابونو، مرجع کتابونو او څېړنیزو مقالو په لیکلو کې پراخه تجربه لري. تېرو ډېرو لسیزو راهیسې له تدریس سره تړلی دی.'),
        ('Mr. Zaigham Hassan is Associate Professor in Zoology Department, University of Peshawar. Mr. Hassan is an active Biology Teacher and has taught Biology at different levels. He has been involved in writing textbooks of General Science and Biology for different grades.',
         'جناب ضیغم حسن جامعہ پشاور کے شعبۂ حیوانیات میں ایسوسی ایٹ پروفیسر ہیں۔ جناب حسن حیاتیات کے سرگرم استاد ہیں اور مختلف سطحوں پر حیاتیات پڑھا چکے ہیں۔ وہ مختلف جماعتوں کے لیے جنرل سائنس اور حیاتیات کی درسی کتب لکھنے میں شامل رہے ہیں۔',
         'ښاغلی ضیغم حسن د پېښور پوهنتون د ژوپوهنې په څانګه کې اسوسیټ پروفیسر دی. ښاغلی حسن د بیولوژۍ فعال ښوونکی دی او په بېلابېلو کچو یې بیولوژي تدریس کړې. د بېلابېلو ټولګیو لپاره د عمومي ساینس او بیولوژۍ د درسي کتابونو په لیکلو کې ونډه لري.'),
        ('Dr. Hakim Khan is an eminent Forester of Khyber Pakhtunkhwa. He has been involved in teaching Biology at different levels', 'ڈاکٹر حکیم خان خیبر پختونخوا کے ممتاز ماہرِ جنگلات ہیں۔ وہ مختلف سطحوں پر حیاتیات کی تدریس سے وابستہ رہے ہیں', 'ډاکټر حکیم خان د خیبر پښتونخوا نامتو ځنګلپوه دی. په بېلابېلو کچو کې یې د بیولوژۍ په تدریس کې ونډه اخیستې'),
        ('Mr. Maqbool is a lecturer in Hasan Abdal Cadet College. He has been teaching Biology at different levels including O and A level.', 'جناب مقبول کیڈٹ کالج حسن ابدال میں لیکچرر ہیں۔ وہ او اور اے لیول سمیت مختلف سطحوں پر حیاتیات پڑھاتے رہے ہیں۔', 'ښاغلی مقبول په حسن ابدال کېډټ کالج کې لکچرر دی. د O او A لېول په ګډون یې په بېلابېلو کچو بیولوژي تدریس کړې.'),
        ('Mr. Naveed Akhtar is a Associate Prof in Botany Department, Islamia College Peshawar. He has been involved in teaching and research for the last several years.', 'جناب نوید اختر اسلامیہ کالج پشاور کے شعبۂ نباتات میں ایسوسی ایٹ پروفیسر ہیں۔ وہ کئی سالوں سے تدریس اور تحقیق سے وابستہ ہیں۔', 'ښاغلی نوید اختر د اسلامیه کالج پېښور د نباتپوهنې په څانګه کې اسوسیټ پروفیسر دی. تېرو څو کلونو راهیسې په تدریس او څېړنه بوخت دی.'),
    ])
    s.quote([('Allah Almighty says: Sayyiduna Muhammad (peace be upon him) is not the father of any of your men, but he is the Messenger of Allah and the Last of the Prophets. (Surah Al-Ahzab: Ayah 40)',
              'اللہ تعالیٰ کا ارشاد ہے: سیدنا محمد صلی اللہ علیہ وآلہ وسلم تمھارے مردوں میں سے کسی کے باپ نہیں بلکہ اللہ تعالیٰ کے رسول اور خاتم الانبیاء ہیں۔ (سورۃ الاحزاب: آیت ۴۰)',
              'الله تعالی فرمایي: سیدنا محمد صلی الله علیه وآله وسلم ستاسو له نارینه وو څخه د هېچا پلار نه دی بلکې د الله تعالی رسول او خاتم الانبیاء دی. (سورة الاحزاب: آیت ۴۰)', )])
    s.p('The verse box on PDF 223 is printed in Urdu; the English and Pashto lines are SpaceBook translations of that Urdu text. The author note "severl" is printed this way (several).', 'PDF 223 پر آیت والا خانہ اردو میں چھپا ہے؛ انگریزی اور پشتو سطریں اسی اردو متن کا اسپیس بک ترجمہ ہیں۔ مصنف کے تعارف میں ”severl“ اسی طرح چھپا ہے (several)۔', 'په PDF 223 کې د آیت چوکاټ په اردو چاپ شوی؛ انګرېزي او پښتو کرښې د همدې اردو متن د سپېس بوک ژباړې دي. د لیکوال په پېژندنه کې ”severl“ همداسې چاپ شوی (several).', editorial=True)
    s.p('SpaceBook note: the author pages give the names Dr. Izhar Ahmad, Dr. Zahir Shah, Mr. Zigham (Zaigham) Hassan, Prof. Dr. Mirza Hakim Khan, Mr. Rizwan Maqbool and Mr. Naveed Akhtar. Spellings are kept as printed.',
        'اسپیس بک نوٹ: مصنفین کے صفحات پر نام ڈاکٹر اظہار احمد، ڈاکٹر ظاہر شاہ، جناب ضیغم حسن، پروفیسر ڈاکٹر مرزا حکیم خان، جناب رضوان مقبول اور جناب نوید اختر دیے گئے ہیں۔ ہجے چھپی صورت میں رکھے گئے ہیں۔',
        'د سپېس بوک یادونه: د لیکوالانو په مخونو کې نومونه ډاکټر اظهار احمد، ډاکټر ظاهر شاه، ښاغلی ضیغم حسن، پروفیسر ډاکټر میرزا حکیم خان، ښاغلی رضوان مقبول او ښاغلی نوید اختر راغلي. املا لکه چې چاپ شوې ساتل شوې.', editorial=True)
    out.append(s)
    return out
