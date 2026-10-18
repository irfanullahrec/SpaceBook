"""Pak Studies XII PDF94 (spread): printed pp.177–178 — Ch.9 Third Plan aims 7–10, outlay, review; Fourth Plan (1970–75); annual plans 1971–78; Fifth Plan (1978–83) aims 1–3."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h
L = lambda rows: t.group('lines', rows)
L([('7. Giving preference to the establishment of basic industries.', '7۔ بنیادی صنعتوں کے قیام کو ترجیح دینا۔', '۷. د بنسټیزو صنعتونو جوړولو ته لومړیتوب ورکول.'),
   ('8. Creating stability in the balance of payments by increasing foreign exchange.', '8۔ زرِ مبادلہ میں اضافہ کر کے ادائیگیوں کے توازن میں استحکام پیدا کرنا۔', '۸. د اسعارو د زیاتولو له لارې د تادیاتو په توازن کې ټیکاو پیدا کول.'),
   ('9. Trying to increase basic facilities.', '9۔ بنیادی سہولتوں میں اضافے کی کوشش کرنا۔', '۹. د بنسټیزو اسانتیاوو د زیاتولو هڅه.'),
   ('10. Providing social security.', '10۔ معاشرتی تحفظ مہیا کرنا۔', '۱۰. ټولنیز خوندیتوب برابرول.')])
P('For the attainment of these objectives a total of 52 billion rupees had been allocated. Of this, 30 billion were dedicated to the government sector and 22 billion to the private sector.',
  'ان مقاصد کے حصول کے لیے کل 52 بلین روپے مختص کیے گئے تھے۔ ان میں سے 30 بلین سرکاری شعبہ جات کے لیے اور 22 بلین نجی شعبے کے لیے وقف تھے۔',
  'د دې موخو د ترلاسه کولو لپاره ټولټال ۵۲ میلیارده روپۍ ځانګړې شوې وې. له دې څخه ۳۰ میلیارده دولتي برخو ته او ۲۲ میلیارده خصوصي سکتور ته ځانګړې وې.')
P('From the above objectives and facts it appears that the Third Five-Year Plan possessed many merits, but after reviewing its progress the picture that comes forward — its outline is something like this:',
  'درج بالا مقاصد و کوائف سے ظاہر ہوتا ہے کہ تیسرا پانچ سالہ منصوبہ بہت سی خوبیوں کا حامل تھا مگر اس کی ترقی کا جائزہ لینے کے بعد جو تصویر سامنے آتی ہے۔ اس کا خاکہ کچھ یوں ہے:۔',
  'له پورته موخو او معلوماتو څرګندېږي چې درېیم پنځه کلن پلان ډېرې ښېګڼې درلودې، خو د هغه د پرمختګ له کتنې وروسته چې کوم انځور مخې ته راځي، خاکه یې داسې ده:')
L([('1. The pace of agricultural progress remained lower than the expected pace; that is, only 4.5 per cent annual progress could occur.', '1۔ زرعی ترقی کی رفتار متوقع رفتار سے کم رہی یعنی صرف 4.5 فیصد سالانہ ترقی ہو سکی۔', '۱. د کرنیز پرمختګ چټکتیا له متوقع چټکتیا ټیټه وه، یعنې یوازې ۴.۵ سلنه کلنی پرمختګ وشو.'),
   ('2. An increase of 9.5 per cent was expected in exports, but as against that this increase remained only 7 per cent.', '2۔ برآمدات میں 9.5 فیصد اضافے کی توقع تھی مگر اس کے مقابلے میں یہ اضافہ صرف 7 فیصد رہا۔', '۲. په صادراتو کې د ۹.۵ سلنه زیاتوالي تمه وه، خو د هغې په پرتله دا زیاتوالی یوازې ۷ سلنه و.'),
   ('3. In the industrial field progress could be only 9 per cent, whereas this target was 13 per cent.', '3۔ صنعتی میدان میں ترقی صرف 9 فیصد ہو سکی حالانکہ یہ ہدف 13 فیصد کا تھا۔', '۳. په صنعتي ډګر کې پرمختګ یوازې ۹ سلنه شو، په داسې حال کې چې هدف ۱۳ سلنه و.'),
   ('4. In the rate of investment there was a reduction of about four per cent.', '4۔ سرمایہ کاری کی شرح میں تقریباً چار فیصد کی ہو گئی۔', '۴. د پانګونې په کچه کې شاوخوا څلور سلنه کمښت راغی.')])
P('In short, the Third Five-Year Plan could not be fully crowned with success, and in most sectors the fixed target could not be reached. In fact difficult conditions surrounded the third plan from its very beginning. In the first two years the country had to face drought, by which crops were badly affected. Because of the Pakistan–India war of 1965 defence expenses increased, because of which a shortage arose in the resources proposed for development expenses. A reduction of 27 per cent in foreign aid had to be faced. Agricultural progress decreased. Conditions inside the country fell victim to disturbances, by which industrial production was badly affected. In short, the real resources and favourable conditions proposed for the Third Five-Year Plan, which were needed for the programme of economic progress, could not be obtained.',
  'مختصراً یہ کہ تیسرا پانچ سالہ منصوبہ پورے طور پر کامیابی سے ہمکنار نہ ہو سکا اور بیشتر شعبوں میں مقرر کردہ ہدف تک نہ جا سکا۔ دراصل مشکل حالات نے ابتداء ہی سے تیسرے منصوبے کو گھیر لیا۔ ابتدائی دو سالوں میں ملک کو خشک سالی کا سامنا کرنا پڑا۔ جس سے فصلیں بری طرح متاثر ہوئیں۔ 1965ء کی پاک بھارت جنگ کی وجہ سے دفاعی اخراجات بڑھ گئے۔ جس کی وجہ سے ترقیاتی اخراجات کے لیے مجوزہ وسائل میں کمی پیدا ہو گئی۔ غیر ملکی امداد میں 27 فیصد کمی کا سامنا کرنا پڑا۔ زرعی ترقی میں کمی ہوئی۔ اندرونِ ملک حالات ہنگاموں کی نذر ہو گئے۔ جس سے صنعتی پیداوار پر برا اثر پڑا۔ مختصراً تیسرے پانچ سالہ منصوبے کو مجوزہ حقیقی وسائل و سازگار حالات میسر نہ آ سکے جو معاشی ترقی کے پروگرام کے لیے درکار تھے۔',
  'لنډه دا چې درېیم پنځه کلن پلان په بشپړ ډول بریالی نه شو او په ډېرو برخو کې ټاکل شوي هدف ته ونه رسېد. په حقیقت کې سختو حالاتو له پیله درېیم پلان راګېر کړ. په لومړیو دوو کلونو کې هېواد له وچکالۍ سره مخ شو، چې له امله یې فصلونه بد اغېزمن شول. د ۱۹۶۵ز د پاک-هند جګړې له امله دفاعي لګښتونه زیات شول، چې له امله یې د پراختیايي لګښتونو لپاره په وړاندیز شویو سرچینو کې کمښت راغی. په بهرنۍ مرسته کې له ۲۷ سلنه کمښت سره مخ شو. کرنیز پرمختګ کم شو. د هېواد دننه حالات د ګډوډیو ښکار شول، چې پر صنعتي تولید یې بد اغېز وکړ. لنډه دا چې درېیم پنځه کلن پلان ته هغه وړاندیز شوې حقیقي سرچینې او مناسب حالات برابر نه شول چې د اقتصادي پرمختګ د پروګرام لپاره اړین وو.')
H('Fourth Five-Year Plan (1970 to 1975)', 'چوتھا پانچ سالہ منصوبہ (1970ء تا 1975ء)', 'څلورم پنځه کلن پلان (۱۹۷۰ تر ۱۹۷۵ز)')
P('The Fourth Five-Year Plan was the third link of the twenty-year perspective plan (1965 to 1985). The important basic aims and objectives of this plan were as follows:',
  'چوتھا پانچ سالہ منصوبہ بیس سالہ تناظری منصوبے (1965ء تا 1985ء) کی تیسری کڑی تھی۔ اس منصوبے کے اہم بنیادی اغراض و مقاصد درج ذیل تھے:۔',
  'څلورم پنځه کلن پلان د شل کلن لیدلوري پلان (۱۹۶۵ تر ۱۹۸۵ز) درېیمه کړۍ وه. د دې پلان مهمې بنسټیزې موخې دا وې:')
L([('1. Maintaining the pace of economic progress, that is, increasing national production at a rate of 6.5 per cent annually.', '1۔ معاشی ترقی کی رفتار کو برقرار رکھنا یعنی قومی پیداوار میں 6.5 فیصد شرح سالانہ سے اضافہ کرنا۔', '۱. د اقتصادي پرمختګ چټکتیا ساتل، یعنې په ملي تولید کې په کلنۍ ۶.۵ سلنه کچه زیاتوالی.'),
   ('2. Creating employment opportunities for 7.5 million new individuals.', '2۔ 7.5 ملین نئے افراد کے لیے روزگار کے مواقع پیدا کرنا۔', '۲. د ۷.۵ میلیونو نویو کسانو لپاره د روزګار فرصتونه پیدا کول.'),
   ('3. Reducing the difference in per-capita income between various parts of the country.', '3۔ ملک کے مختلف حصوں کے مابین فی کس آمدنی کے فرق کو کم کرنا۔', '۳. د هېواد د بېلابېلو برخو ترمنځ د سړي سر عاید توپیر کمول.'),
   ('4. Increasing the production of food grains by 8.5 million tons.', '4۔ غذائی اجناس کی پیداوار میں 8.5 ملین ٹن کا اضافہ کرنا۔', '۴. د خوراکي غلو په تولید کې ۸.۵ میلیونه ټنه زیاتوالی.'),
   ('5. Establishing social justice, that is, creating harmony between economic progress and social justice with the help of practicable policies.', '5۔ سماجی انصاف قائم کرنا یعنی قابلِ عمل پالیسیوں کی مدد سے معاشی ترقی اور سماجی انصاف میں ہم آہنگی پیدا کرنا۔', '۵. ټولنیز عدالت ټینګول، یعنې د عملي پالیسیو په مرسته د اقتصادي پرمختګ او ټولنیز عدالت ترمنځ همغږي پیدا کول.'),
   ('6. Increasing exports by eight and a half per cent annually.', '6۔ برآمدات میں ساڑھے آٹھ فیصد سالانہ اضافہ کرنا۔', '۶. په صادراتو کې کلنۍ اته نیم سلنه زیاتوالی.')])
P('For the attainment of these objectives and targets 75 billion rupees had been allocated. Of these, 49 billion had been kept for government sectors and 26 billion rupees for private sectors.',
  'ان مقاصد و اہداف کے حصول کے لیے 75 بلین روپے مختص کیے گئے تھے۔ ان میں سے 49 بلین سرکاری شعبہ جات کے لیے اور 26 بلین نجی شعبوں کے لیے رکھے گئے تھے۔',
  'د دې موخو او هدفونو د ترلاسه کولو لپاره ۷۵ میلیارده روپۍ ځانګړې شوې وې. له دې څخه ۴۹ میلیارده دولتي برخو ته او ۲۶ میلیارده روپۍ خصوصي برخو ته ایښودل شوې وې.')
P('The Fourth Five-Year Plan could not be implemented because of the Pakistan–India war and other unfavourable conditions inside the country, and this plan had to be cancelled.',
  'چوتھے پانچ سالہ منصوبے پر بوجہ پاک بھارت جنگ و دیگر اندرونِ ملک ناموافق حالات عمل درآمد نہ ہو سکا اور اس منصوبے کو منسوخ کرنا پڑا۔',
  'پر څلورم پنځه کلن پلان د پاک-هند جګړې او د هېواد دننه د نورو نامناسبو حالاتو له امله عمل ونه شو، او دا پلان لغوه کړل شو.')
P('Because of economic and political conditions in the country being unfavourable, only year-to-year short-term planning could be done during 1971 to 1978. In the opinion of experts, medium-term planning becomes difficult because of instability. Through short-term planning the completion of long-term plans does not take place in an appropriate way. Desired results cannot generally be obtained from one-year development plans. That is why, mostly through short-term planning, the pace of economic progress could not be maintained. Therefore during the five-year plan satisfactory results could not be obtained.',
  'ملک میں معاشی و سیاسی حالات کے ناسازگار ہونے کی وجہ سے 1971ء تا 1978ء کے دوران میں سال بہ سال قلیل المیعاد منصوبہ بندی ہی کی جا سکی۔ ماہرین کی رائے میں اوسط المیعاد منصوبہ بندی عدمِ استحکام کی وجہ سے مشکل ہو جاتی ہے۔ قلیل المیعاد منصوبہ بندی کے ذریعے سے طویل المیعاد منصوبوں کی تکمیل مناسب انداز میں نہیں ہو پاتی۔ یک سالہ ترقیاتی منصوبوں سے عام طور پر مطلوبہ نتائج حاصل نہیں کیے جا سکتے۔ یہی وجہ ہے کہ اکثر و بیشتر قلیل المیعاد منصوبہ بندی کی مدد سے معاشی ترقی کی رفتار کو برقرار نہیں رکھا جا سکتا۔ لہٰذا پانچ سالہ منصوبہ کے دوران میں خاطر خواہ نتائج حاصل نہ ہو سکے۔',
  'په هېواد کې د اقتصادي او سیاسي حالاتو د نامناسبوالي له امله د ۱۹۷۱ تر ۱۹۷۸ز په موده کې یوازې کال په کال لنډمهاله پلان جوړونه وشوه. د پوهانو په نظر منځمهاله پلان جوړونه د بې‌ثباتۍ له امله ستونزمنه کېږي. د لنډمهاله پلان جوړونې له لارې اوږدمهاله پلانونه په مناسب ډول نه بشپړېږي. له یو کلنو پراختیايي پلانونو عموماً مطلوبې پایلې نه ترلاسه کېږي. همدا لامل دی چې ډېری وخت د لنډمهاله پلان جوړونې په مرسته د اقتصادي پرمختګ چټکتیا نه ساتل کېږي. نو د پنځه کلن پلان په موده کې د قناعت وړ پایلې ترلاسه نه شوې.')
H('Fifth Five-Year Plan (1978 to 1983)', 'پانچواں پانچ سالہ منصوبہ (1978ء تا 1983ء)', 'پنځم پنځه کلن پلان (۱۹۷۸ تر ۱۹۸۳ز)')
P('The major targets of the fifth plan were as follows:',
  'پانچویں منصوبے کے بڑے بڑے اہداف مندرجہ ذیل تھے:۔',
  'د پنځم پلان لوی هدفونه دا وو:')
L([('1. Increasing national production by 7.2 per cent annually.', '1۔ قومی پیداوار میں 7.2 فیصد سالانہ اضافہ کرنا۔', '۱. په ملي تولید کې کلنۍ ۷.۲ سلنه زیاتوالی.'),
   ('2. Progress of 6 per cent annually in the agricultural sector.', '2۔ زرعی شعبے میں 6 فیصد سالانہ ترقی کرنا۔', '۲. په کرنیزه برخه کې کلنی ۶ سلنه پرمختګ.'),
   ('3. Progressing in the industrial field overall at the rate of 10 per cent annually.', '3۔ صنعتی میدان میں مجموعی طور پر 10 فیصد سالانہ کے حساب سے ترقی کرنا۔', '۳. په صنعتي ډګر کې په ټولیز ډول په کلنۍ ۱۰ سلنه حساب پرمختګ.')])
rec = BOOK.record(t, 'pak12-ch9-text-11', 'Chapter 9 text (11)', 'بابِ نہم — متن (۱۱)', 'نهم څپرکی — متن (۱۱)', 94, [177, 178])
rec['sourceNote'] = 'The first list continues the Third Plan aims from p.176. The Fifth Plan targets list continues on p.179 (PDF95).'
issues = [{'id': 'pak12-pdf094', 'unit': 9, 'printedPage': 177,
           'description': 'Third-Plan review item 4 on p.177 prints “… چار فیصد کی ہو گئی” (missing “کمی”); p.178 says “during the five-year plan” after describing annual plans; retained as printed. Decorative pink borders on pp.177–178 are not reproduced.'}]

if __name__ == '__main__':
    BOOK.save(94, [(9, rec)], issues=issues)
