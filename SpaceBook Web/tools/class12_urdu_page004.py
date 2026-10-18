"""Urdu XII PDF4 (spread): right = حاصلاتِ تعلّم (learning outcomes); left = فہرست (contents) — حصۂ نثر 1–17."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('Learning Outcomes', 'حاصلاتِ تعلّم', 'د زده کړې پایلې')
s.p('After studying this book, students will be able to:', 'اس کتاب کو پڑھنے کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې کتاب له لوستلو وروسته به زده کوونکي وکولای شي چې:')
s.group('list', [
    ('Recognise Urdu prose and verse with an appreciation of their beauties and flaws.', 'اُردو میں منثور اور منظوم کلام کی حُسن و قبح کے ساتھ پہچان کر سکیں۔', 'په اردو کې نثري او منظوم کلام د ښکلا او نیمګړتیا سره وپېژني.'),
    ('Read a passage from an appreciative and critical point of view, and distinguish between ordinary and literary writing with reference to literary merits (rhetoric — ʿilm-e-bayān, ʿilm-e-badīʿ).', 'عبارت کو استحسانی اور تنقیدی نقطۂ نظر سے پڑھ سکیں اور ادبی محاسن (علمِ بیان، علمِ بدیع) کے حوالے سے عام اور ادبی تحریر میں فرق کر سکیں۔', 'متن د ستاینې او نقد له نظره ولولي او د ادبي ښېګڼو (علمِ بیان، علمِ بدیع) په حواله د عامې او ادبي لیکنې ترمنځ توپیر وکړي.'),
    ('Write daily observations and experiences correctly according to the rules.', 'روزمرّہ مشاہدات و تجربات کو قواعد کے مطابق درست طور پر تحریر کر سکیں۔', 'ورځنۍ کتنې او تجربې د قواعدو سره سم په سمه توګه ولیکي.'),
    ('Read with understanding official orders, legal judgments, a power of attorney (wakālat-nāma) and other official and legal terms.', 'دفتری احکامات، قانونی فیصلے، وکالت نامہ اور دیگر سرکاری اور قانونی اصطلاحات کو سمجھ کر پڑھ سکیں۔', 'دفتري حکمونه، قانوني پرېکړې، وکالت‌نامه او نورې دولتي او قانوني اصطلاحګانې په پوهې سره ولولي.'),
    ('Explain the central idea and basic points of a literary piece and other interpretations under critical principles, and quote sayings and verses.', 'ادب پارے کا مرکزی خیال، بنیادی نکات اور دیگر تشریحات تنقیدی اُصولوں کے تحت کر سکیں اور اقوال و اشعار کا حوالہ دے سکیں۔', 'د ادبي ټوټې مرکزي فکر، بنسټیز ټکي او نورې تشریحګانې د نقد د اصولو له مخې وکړي او د اقوالو او شعرونو حواله ورکړي.'),
    ('Write a comprehensive review of any text from newspapers and magazines.', 'اخبارات و رسائل کے کسی بھی متن پر جامع تبصرہ لکھ سکیں۔', 'د ورځپاڼو او مجلو په هر متن جامع تبصره ولیکي.'),
    ('Read a passage, give an opinion on it, and identify and correct the errors in it.', 'کسی عبارت کو پڑھ کر اُس پر رائے دے سکیں اور عبارت میں موجود اغلاط کی نشاندہی کرتے ہوئے درست کر سکیں۔', 'یو متن ولولي، پرې نظر ورکړي او په متن کې شته تېروتنې وپېژني او سمې یې کړي.'),
    ('Read a written speech of at least ten minutes on any literary or academic subject with correct pronunciation.', 'کسی بھی ادبی یا علمی موضوع پر درست تلفّظ کے ساتھ کم از کم دس منٹ تک لکھی ہوئی تقریر پڑھ سکیں۔', 'په هره ادبي یا علمي موضوع لږ تر لږه لس دقیقې لیکلې وینا په سم تلفظ ولولي.'),
    ('Write an essay of at least five hundred words on any academic or literary subject, using reasoning, examples, sayings, synonyms, verses, idioms and everyday usage.', 'کسی بھی علمی یا ادبی موضوع پر استدلال، مثالوں، مقولوں، مترادفات، اشعار و محاورات اور روزمرّہ کے مطابق کم از کم پانچ سو الفاظ کا مضمون لکھ سکیں۔', 'په هره علمي یا ادبي موضوع د استدلال، بېلګو، متلونو، مترادفاتو، شعرونو، محاورو او ورځني کارونې سره لږ تر لږه پنځه سوه کلمې مقاله ولیکي.'),
    ('Recognise poetic and prose terms, e.g. ʿilm-e-bayān, auxiliary verbs and figures of speech (ṣanāʾiʿ-o-badāʾiʿ), and use compound sentences correctly.', 'شعری و نثری اصطلاحات مثلاً علمِ بیان، معاون افعال، صنائع بدائع کی پہچان اور مرکّب جملوں کا درست استعمال کر سکیں۔', 'شعري او نثري اصطلاحګانې لکه علمِ بیان، مرستندوي فعلونه، صنایع او بدایع وپېژني او مرکبې جملې په سمه توګه وکاروي.'),
    ('Learn to use technical dictionaries of various sciences and professions and general dictionaries.', 'مختلف علوم اور پیشوں کی اصطلاحی لغات اور عام لغات کا استعمال سیکھ سکیں۔', 'د بېلابېلو علومو او مسلکونو د اصطلاحي قاموسونو او عامو قاموسونو کارول زده کړي.'),
])
slo = BOOK.record(s, 'urdu12-fm-slos', 'Learning outcomes', 'حاصلاتِ تعلّم', 'د زده کړې پایلې', 4, [None])

c = Builder()
c.p('In the name of Allah, the Most Gracious, the Most Merciful.', '﴿ بِسْمِ اللّٰہِ الرَّحْمٰنِ الرَّحِیْمِ ﴾ — شروع اللہ کے نام سے جو بڑا مہربان، نہایت رحم والا ہے۔', 'د الله په نامه چې ډېر مهربان، بې‌حده رحم کوونکی دی.')
c.h('Contents — Prose section', 'فہرست — حصۂ نثر', 'فهرست — د نثر برخه')
P = [(1, 'مسلمانوں کا قدیم طرزِ تعلیم', 'The Ancient Educational System of the Muslims', 'د مسلمانانو د زده کړې زوړ طرز', 'شبلی نعمانی', 'Shibli Nomani', 'شبلي نعماني', 1),
     (2, 'سُقراط', 'Socrates', 'سقراط', 'مہدی افادی', 'Mahdi Ifadi', 'مهدي افادي', 10),
     (3, 'فاقہ میں روزہ', 'Fasting while Starving', 'په لوږه کې روژه', 'خواجہ حسن نظامی', 'Khwaja Hasan Nizami', 'خواجه حسن نظامي', 16),
     (4, 'پھر وطنیت کی طرف', 'Back towards Patriotism', 'بیا د وطنپالنې پر لور', 'مولانا صلاح الدین احمد', 'Maulana Salahuddin Ahmad', 'مولانا صلاح الدین احمد', 26),
     (5, 'شہرتِ عام اور بقائے دوام کا دربار', 'The Court of Public Fame and Lasting Immortality', 'د عام شهرت او تل پاتې کېدو دربار', 'محمد حسین آزاد', 'Muhammad Husain Azad', 'محمد حسین ازاد', 33),
     (6, 'چند روز ایک روڈ رولر کے ساتھ', 'A Few Days with a Road Roller', 'څو ورځې له یوه روډ رولر سره', 'ڈاکٹر وزیر آغا', 'Dr Wazir Agha', 'ډاکټر وزیر اغا', 47),
     (7, 'منظور', 'Manzoor', 'منظور', 'سعادت حسن منٹو', 'Saadat Hasan Manto', 'سعادت حسن منټو', 54),
     (8, 'کتبہ', 'The Nameplate (Kutba)', 'کتبه', 'غلام عباس', 'Ghulam Abbas', 'غلام عباس', 66),
     (9, 'مائیں', 'Mothers', 'میندې', 'احمد ندیم قاسمی', 'Ahmad Nadeem Qasmi', 'احمد ندیم قاسمي', 78),
     (10, 'سیاہ فام', 'Black-skinned', 'تورپوستی', 'شوکت صدیقی', 'Shaukat Siddiqui', 'شوکت صدیقي', 87),
     (11, 'محسنِ محلّہ', 'Benefactor of the Neighbourhood', 'د محلې محسن', 'اشفاق احمد', 'Ashfaq Ahmad', 'اشفاق احمد', 98),
     (12, 'کنڈکٹر', 'The Conductor', 'کنډکټر', 'الطاف فاطمہ', 'Altaf Fatima', 'الطاف فاطمه', 106),
     (13, 'ایک وصیّت کی تعمیل', 'Fulfilling a Will', 'د یوې وصیت پلي کول', 'فرحت اللہ بیگ', 'Farhatullah Baig', 'فرحت الله بیګ', 119),
     (14, 'علّامہ اقبالؒ', 'Allama Iqbal', 'علامه اقبال', 'چراغ حسن حسرتؔ', 'Chiragh Hasan Hasrat', 'چراغ حسن حسرت', 133),
     (15, 'طائرِ لاہوتی', 'The Celestial Bird', 'لاهوتي مرغه', 'فارغ بخاری', 'Farigh Bukhari', 'فارغ بخاري', 145),
     (16, 'مرید پور کا پیر', 'The Pir of Muridpur', 'د مریدپور پیر', 'پطرس بخاری', 'Patras Bukhari', 'پطرس بخاري', 154),
     (17, 'حاجی اورنگ زیب خان', 'Haji Aurangzeb Khan', 'حاجي اورنګزېب خان', 'مشتاق احمد یوسفی', 'Mushtaq Ahmad Yousufi', 'مشتاق احمد یوسفي', 168)]
U = '۰۱۲۳۴۵۶۷۸۹'
urn = lambda n: ''.join(U[int(d)] for d in str(n))
c.table('urdu12-contents-prose', ['No.', 'Title', 'Author', 'Page'], [[str(n), e, ae, str(p)] for n, u, e, ps, au, ae, aps, p in P],
        ['شمار', 'عنوان', 'مصنف', 'صفحہ'], ['شمېره', 'سرلیک', 'لیکوال', 'مخ'],
        [[urn(n) + '۔', u, au, urn(p)] for n, u, e, ps, au, ae, aps, p in P], [[str(n), ps, aps, str(p)] for n, u, e, ps, au, ae, aps, p in P])
con = BOOK.record(c, 'urdu12-fm-contents-1', 'Contents — prose', 'فہرست — حصۂ نثر', 'فهرست — د نثر برخه', 4, [None])
issues = [{'id': 'urdu12-pdf004', 'unit': 'FM', 'printedPage': None, 'description': 'Spread read right-to-left: right = حاصلاتِ تعلّم, left = فہرست (prose). The legacy dataset’s lesson titles 7–12 (e.g. “نیا قانون”, “اوور کوٹ”, “سفارش”) do not match this contents page (منظور، کتبہ، مائیں، سیاہ فام، محسنِ محلّہ، کنڈکٹر); unit titles are corrected from the source as each lesson is authored.'}]

if __name__ == '__main__':
    BOOK.save(4, [('FM', slo), ('FM', con)], issues=issues)
