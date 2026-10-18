"""Economics XII PDF105: pp.190–191 — chapter 9 model paper MCQs i–xiv (printed ✓); chapter 10 Banking System of Pakistan: structure,
State Bank, commercial banks (begins). Run: python class12_eco_page105.py"""
import sys
from class12_eco_common import BOOK, Builder, rec, P, L, mcqs, model


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('These are included in the means of transport:', 'ذرائع نقل و حمل میں یہ شامل ہیں:', 'په ترانسپورټي وسایلو کې دا شامل دي:'),
  [O('telephone', 'ٹیلیفون', 'ټیلیفون'), O('fax', 'فیکس', 'فکس'), O('roads', 'سڑکیں', 'سړکونه'), O('radio', 'ریڈیو', 'راډیو')], 2),
 (('The motorway between Lahore and Islamabad was completed in this year:', 'لاہور، اسلام آباد کے درمیان موٹروے اس سال مکمل ہوا۔', 'د لاهور او اسلام اباد ترمنځ موټروې په دې کال بشپړ شو:'),
  [O('June 1992', 'جون 1992ء', 'جون ۱۹۹۲'), O('December 1994', 'دسمبر 1994ء', 'ډسمبر ۱۹۹۴'), O('July 1995', 'جولائی 1995ء', 'جولای ۱۹۹۵'), O('October 1997', 'اکتوبر 1997ء', 'اکتوبر ۱۹۹۷')], None),
 (('By dry docks is meant:', 'خشک گودیوں سے مراد ہے:', 'له وچو ډنډونو مراد دی:'),
  [O('airports', 'ہوائی اڈے', 'هوايي ډګرونه'), O('motorways', 'موٹروے', 'موټروې ګانې'), O('land ports', 'بری بندرگاہیں', 'وچې بندرونه')], 2),
 (('The first dry port of all was established here:', 'سب سے پہلی ڈرائی پورٹ یہاں قائم ہوئی:', 'تر ټولو لومړی وچ بندر دلته جوړ شو:'),
  [O('Multan', 'ملتان', 'ملتان'), O('Lahore', 'لاہور', 'لاهور'), O('Quetta', 'کوئٹہ', 'کوټه'), O('Peshawar', 'پشاور', 'پېښور')], 1),
 (('These are included in the means of news-giving (communication):', 'ذرائع خبر رسانی میں یہ شامل ہیں:', 'د خبر رسونې په وسایلو کې دا شامل دي:'),
  [O('radio', 'ریڈیو', 'راډیو'), O('railway', 'ریلوے', 'رېل'), O('roads', 'سڑکیں', 'سړکونه'), O('aircraft', 'ہوائی جہاز', 'الوتکه')], 0),
 (('The productivity of labour depends on this:', 'محنت کی پیداواریت کا دارومدار اس پر ہے:', 'د کار تولیدیت په دې پورې اړه لري:'),
  [O('capital', 'راس المال', 'پانګه'), O('conditions of the market', 'منڈی کے حالات', 'د بازار حالات'), O('mental ability', 'ذہنی قابلیت', 'ذهني وړتیا'), O('standard of prices', 'قیمتوں کا معیار', 'د بیو معیار')], 2),
 (('The mobility of labour has this many kinds:', 'محنت کی نقل پذیری کی اتنی اقسام ہیں:', 'د کار لېږد دومره ډولونه لري:'),
  [O('2', '2', '۲'), O('3', '3', '۳'), O('4', '4', '۴'), O('5', '5', '۵')], 2),
 (('With regard to population Pakistan is at this number in the world:', 'آبادی کے لحاظ سے پاکستان دنیا میں اس نمبر پر ہے:', 'د نفوس له پلوه پاکستان په نړۍ کې په دې شمېره دی:'),
  [O('fourth largest country', 'چوتھا بڑا ملک', 'څلورم لوی هېواد'), O('sixth largest country', 'چھٹا بڑا ملک', 'شپږم لوی هېواد'), O('eighth largest country', 'آٹھواں بڑا ملک', 'اتم لوی هېواد'), O('tenth largest country', 'دسواں بڑا ملک', 'لسم لوی هېواد')], 1),
 (('In Pakistan at this time approximately this many individuals are unemployed:', 'پاکستان میں اس وقت تقریباً اتنے افراد بے روزگار ہیں:', 'په پاکستان کې اوس نږدې دومره کسان بې‌روزګاره دي:'),
  [O('twenty lakh', 'بیس لاکھ', 'شل لکه'), O('thirty lakh', 'تیس لاکھ', 'دېرش لکه'), O('thirty-seven lakh', 'سینتیس لاکھ', 'اووه دېرش لکه'), O('fifty lakh', 'پچاس لاکھ', 'پنځوس لکه')], 2),
 (('If a teacher is transferred to another school, then this is:', 'ایک ٹیچر کا دوسرے سکول میں تبادلہ ہو جائے تو یہ ہے:', 'که یو ښوونکی بل ښوونځي ته تبدیل شي، نو دا دی:'),
  [O('vertical mobility', 'عمودی نقل پذیری', 'عمودي لېږد'), O('horizontal mobility', 'افقی نقل پذیری', 'افقي لېږد'), O('occupational mobility', 'پیشہ ورانہ نقل پذیری', 'مسلکي لېږد')], 1),
 (('Which bank rediscounts hundis (bills)?', 'کونسا بنک ہنڈیوں کو دوبارہ بٹہ لگاتا ہے:', 'کوم بانک هنډۍ بیا تخفیفوي؟'),
  [O('Muslim Commercial Bank', 'مسلم کمرشل بنک', 'مسلم کمرشل بانک'), O('commercial bank', 'تجارتی بنک', 'سوداګریز بانک'), O('savings bank', 'بچت بنک', 'د سپما بانک'), O('central bank', 'مرکزی بنک', 'مرکزي بانک')], 3),
 (('Which head (item) is related to the communications sector?', 'کونسی مد کا تعلق مواصلات شعبہ سے ہے؟', 'کوم سرلیک د مخابراتو له برخې سره تړاو لري؟'),
  [O('defence', 'دفاع', 'دفاع'), O('public health', 'صحت عامہ', 'عامه روغتیا'), O('police', 'پولیس', 'پولیس'), O('railway', 'ریلوے', 'رېل')], 3),
 (('Of the following five-year plans of Pakistan, this one met with success:', 'پاکستان کا درج ذیل پانچ سالہ منصوبہ کامیابی سے ہمکنار ہوا:', 'د پاکستان له لاندې پنځه کلنو پلانونو دا یو بریالی شو:'),
  [O('second', 'دوسرا', 'دویم'), O('eighth', 'آٹھواں', 'اتم'), O('third', 'تیسرا', 'درېیم'), O('fourth', 'چوتھا', 'څلورم')], 0),
 (('A clerk progressing and becoming a manager is called:', 'ایک کلرک کا ترقی پا کر منیجر بننا کہلاتا ہے:', 'د یوه کلرک پرمختګ او مدیر کېدل بلل کېږي:'),
  [O('vertical mobility', 'عمودی حرکت پذیری', 'عمودي حرکت'), O('horizontal mobility', 'افقی حرکت پذیری', 'افقي حرکت'), O('social mobility', 'معاشرتی حرکت پذیری', 'ټولنیز حرکت'), O('occupational mobility', 'پیشہ وارانہ حرکت پذیری', 'مسلکي حرکت')], 1)]


def p105():
    b = Builder()
    b.h('Objective (Objective)', 'معروضی (Objective)', 'معروضي (Objective)')
    P(b, [('Question 3: More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال نمبر 3: ہر سوال کے ایک سے زیادہ جوابات دیئے گئے ہیں ان میں سے درست جواب پر (✓) کا نشان لگائیے۔', '۳ پوښتنه: د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(b, MCQ)
    r1 = model(b, 9, 3, 105, 190)
    t = Builder()
    t.h('Chapter 10 — Banking System of Pakistan (Banking System of Pakistan)', 'باب 10 — پاکستان کا بنکاری نظام (Banking System of Pakistan)', '۱۰ څپرکی — د پاکستان بانکي نظام (Banking System of Pakistan)')
    P(t, [('The banking system of Pakistan consists of the following:', 'پاکستان کا بنکاری نظام مندرجہ ذیل پر مشتمل ہے:', 'د پاکستان بانکي نظام له لاندې څخه جوړ دی:')])
    L(t, [('1. The central bank of Pakistan, i.e. the State Bank of Pakistan (State Bank of Pakistan).', '1۔ پاکستان کا مرکزی بنک یعنی سٹیٹ بنک آف پاکستان (State Bank of Pakistan)۔', '۱. د پاکستان مرکزي بانک، یعنې د پاکستان دولتي بانک (State Bank of Pakistan).'),
          ('2. Five in the government sector, i.e. National Bank of Pakistan, First Women Bank Limited, The Bank of Khyber, and The Bank of Punjab and Sindh Bank Limited.', '2۔ پانچ سرکاری شعبوں میں یعنی نیشنل بنک آف پاکستان، فرسٹ ویمن بنک لمیٹڈ، دی بنک آف خیبر اور دی بنک آف پنجاب اور سندھ بنک لمیٹڈ۔', '۲. پنځه په دولتي برخه کې، یعنې د پاکستان ملي بانک، فرسټ ویمن بانک لمیټډ، د خیبر بانک، او د پنجاب بانک او سند بانک لمیټډ.'),
          ('3. Four specialised (Specialized) scheduled banks, i.e. Punjab Provincial Co-operative Bank, Zarai Taraqiati Bank Limited, SME (SME) Bank Limited and Industrial Development Bank of Pakistan Limited.', '3۔ چار تخصیصی (Specialized) شیڈولڈ بنک یعنی پنجاب پراونشل کوآپریٹو بنک، زرعی ترقیاتی بنک لمیٹڈ، ایس ایم ای (SME) بنک لمیٹڈ اور انڈسٹریل ڈویلپمنٹ بنک آف پاکستان لمیٹڈ۔', '۳. څلور تخصصي (Specialized) شېډول شوي بانکونه، یعنې د پنجاب ولایتي کوپراتیف بانک، زرعي ترقیاتي بانک لمیټډ، اېس اېم اي (SME) بانک لمیټډ او د پاکستان صنعتي پراختیايي بانک لمیټډ.'),
          ('4. Thirty domestic private banks, in which these are included: United Bank Limited, Habib Bank Limited, Muslim Commercial Bank Limited, Allied Bank Limited, Bank Alfalah Limited, Meezan Bank, BankIslami Pakistan Limited, Askari Bank Limited, Dubai Islamic Bank Pakistan Limited etc.', '4۔ تیس ملکی پرائیویٹ بنک جن میں یہ شامل ہیں: یونائیٹڈ بنک لمیٹڈ، حبیب بنک لمیٹڈ، مسلم کمرشل بنک لمیٹڈ، الائیڈ بنک لمیٹڈ، بنک الفلاح لمیٹڈ، میزان بنک، بنک اسلامی پاکستان لمیٹڈ، عسکری بنک لمیٹڈ، دوبئی اسلامک بنک پاکستان لمیٹڈ وغیرہ۔', '۴. دېرش هېوادني خصوصي بانکونه، چې په کې دا شامل دي: یونایټډ بانک لمیټډ، حبیب بانک لمیټډ، مسلم کمرشل بانک لمیټډ، الاېډ بانک لمیټډ، بانک الفلاح لمیټډ، میزان بانک، بانک اسلامي پاکستان لمیټډ، عسکري بانک لمیټډ، دوبۍ اسلامیک بانک پاکستان لمیټډ او نور.'),
          ('5. Six foreign banks (Foreign Banks), e.g. Oman International Bank, Bank of Tokyo, Citibank etc.', '5۔ چھ غیر ملکی بنک (Foreign Banks) مثلاً عمان انٹرنیشنل بنک، بنک آف ٹوکیو، سٹی بنک وغیرہ۔', '۵. شپږ بهرني بانکونه (Foreign Banks)، لکه عمان انټرنېشنل بانک، د توکیو بانک، سیټي بانک او نور.'),
          ('6. Eight development financial institutions (Development Financial Institutions), e.g. Pak Kuwait Investment Company of Pakistan Limited, Saudi Pak Industrial and Agricultural Investment Company (Private) Limited, Pak-Iran Joint Investment Company Limited, Pak-Brunei Investment Company Limited, House Building Finance Corporation Limited etc.', '6۔ آٹھ ترقیاتی مالیاتی ادارے (Development Financial Institutions) مثلاً پاک کویت انوسٹمنٹ کمپنی آف پاکستان لمیٹڈ، سعودی پاک انڈسٹریل اینڈ ایگریکلچرل انوسٹمنٹ کمپنی (پرائیویٹ) لمیٹڈ، پاک۔ ایران جائنٹ انوسٹمنٹ کمپنی لمیٹڈ، پاک۔ برونائی انوسٹمنٹ کمپنی لمیٹڈ، ہاؤس بلڈنگ فنانس کارپوریشن لمیٹڈ وغیرہ۔', '۶. اته پراختیايي مالي ادارې (Development Financial Institutions)، لکه د پاکستان پاک کویت پانګونې شرکت لمیټډ، سعودي پاک صنعتي او کرنیز پانګونې شرکت (خصوصي) لمیټډ، پاک-ایران ګډ پانګونې شرکت لمیټډ، پاک-برونای پانګونې شرکت لمیټډ، د کور جوړونې مالي کارپوریشن لمیټډ او نور.'),
          ('7. Eight banks giving small loans, e.g. Khushhali Bank, The First Microfinance Bank Limited, Rozgar Microfinance Bank Limited, Tameer Microfinance Bank Limited etc.', '7۔ آٹھ چھوٹے قرضے دینے والے بنک مثلاً خوشحالی بنک، دی فرسٹ مائیکروفنانس بنک لمیٹڈ، روزگار مائیکروفنانس بنک لمیٹڈ، تعمیر مائیکروفنانس بنک لمیٹڈ وغیرہ۔', '۷. اته د وړو پورونو ورکوونکي بانکونه، لکه خوشحالي بانک، فرسټ مایکروفنانس بانک لمیټډ، روزګار مایکروفنانس بانک لمیټډ، تعمیر مایکروفنانس بانک لمیټډ او نور.')])
    P(t, [('The total number of branches of all banks in 2011 was 9,908.', 'تمام بنکوں کی شاخوں کی مجموعی تعداد 2011ء میں 9,908 تھی۔', 'په ۲۰۱۱ کې د ټولو بانکونو د څانګو ټول شمېر ۹,۹۰۸ و.')])
    t.h('State Bank of Pakistan (State Bank of Pakistan)', 'سٹیٹ بنک آف پاکستان (State Bank of Pakistan)', 'د پاکستان دولتي بانک (State Bank of Pakistan)')
    P(t, [('This is the central bank of Pakistan and it performs all those functions which are the responsibility of the central bank of any country, e.g. issuing notes, working as bank for the government, regulating the banking system of the country, and expanding or contracting the quantity of money and credit as required. We shall state the detailed account of this bank in the coming pages. Here we mention the commercial banks:', 'یہ پاکستان کا مرکزی بنک ہے اور وہ تمام فرائض انجام دیتا ہے جو کسی ملک کے مرکزی بنک کے ذمے ہوتے ہیں۔ مثلاً نوٹ جاری کرنا، حکومت کے لئے بنک کا کام کرنا، ملک کے بنکاری نظام کو منضبط کرنا اور اعتباری زر کی مقدار کو حسبِ ضرورت پھیلانا یا سکیڑنا۔ اس بنک کا مفصل حال ہم اگلے صفحات میں بیان کریں گے۔ یہاں ہم تجارتی بنکوں کا ذکر کرتے ہیں:', 'دا د پاکستان مرکزي بانک دی او هغه ټولې دندې ترسره کوي چې د هر هېواد د مرکزي بانک پر غاړه وي؛ لکه نوټونه صادرول، د حکومت لپاره د بانک کار کول، د هېواد بانکي نظام منظمول، او د اعتباري پیسو اندازه د اړتیا سره سم پراخول یا راټولول. د دې بانک مفصل حال به په راتلونکو مخونو کې بیان کړو. دلته د سوداګریزو بانکونو یادونه کوو:')])
    t.h('Commercial banks (Commercial Banks)', 'تجارتی بنک (Commercial Banks)', 'سوداګریز بانکونه (Commercial Banks)')
    P(t, [('The commercial banks of Pakistan are scheduled (or listed) banks, i.e. their names are entered in the list of the State Bank of Pakistan Order 1948. The whole banking system of the country makes its policy under the instructions of the State Bank of Pakistan. At this time the total number of domestic commercial scheduled banks is 48, and the foreign banks are six. Legally the commercial banks are bound to keep seven per cent of their time and demand liabilities (Liabilities) with the State Bank as “reserved money” (Cash Reserve). Its two purposes are: first, of the public … (continued on p.192)', 'پاکستان کے تجارتی بنک شیڈولڈ (یا فہرستی) بنک ہیں، یعنی ان کے نام سٹیٹ بنک آف پاکستان آرڈر 1948ء کی فہرست میں درج ہیں۔ ملک کا پورا بنکاری نظام سٹیٹ بنک آف پاکستان کی ہدایات کے تحت اپنی پالیسی بناتا ہے۔ اس وقت ملکی کمرشل شیڈولڈ بنکوں کی کل تعداد 48 ہے اور غیر ملکی بنک چھ ہیں۔ قانونی طور پر تجارتی بنک اس بات کے پابند ہیں کہ وہ اپنے میعادی اور غیر میعادی واجبات (Liabilities) کا سات فیصد سٹیٹ بنک کے پاس ”زرِ محفوظ“ (Cash Reserve) کے طور پر رکھیں۔ اس کے دو مقاصد ہیں: اول، عوام کی … (ص 192 پر جاری)', 'د پاکستان سوداګریز بانکونه شېډول شوي (یا لېست شوي) بانکونه دي، یعنې نومونه یې د ۱۹۴۸ د پاکستان دولتي بانک حکم په لېست کې درج دي. د هېواد ټول بانکي نظام د پاکستان دولتي بانک د لارښوونو لاندې خپله پالیسي جوړوي. اوس د هېوادني سوداګریزو شېډول شویو بانکونو ټول شمېر ۴۸ دی او بهرني بانکونه شپږ دي. په قانوني ډول سوداګریز بانکونه مکلف دي چې د خپلو مودې لرونکو او بې‌مودې مسؤلیتونو (Liabilities) اووه سلنه د دولتي بانک سره د ”خوندي پیسو“ (Cash Reserve) په توګه وساتي. دوه موخې یې دي: لومړی، د خلکو … (په ۱۹۲ مخ دوام)')])
    BOOK.save(105, [(9, r1), (10, rec(t, 10, 1, 105, pages_=[191], first=True))], complete_units=[9], issues=[{'id': 'eco12-pdf105', 'unit': 9, 'printedPage': 190,
               'description': 'Printed ticks kept as printed: MCQ ii has no tick; MCQ xiv ticks “horizontal mobility” for a clerk becoming manager (that is vertical mobility per the chapter); MCQ xiii ticks the second plan. MCQs iii and x print only three options. p.191 (chapter 10) lists “تیس ملکی پرائیویٹ بنک” and later states 48 domestic commercial scheduled banks — both kept as printed.'}])


if __name__ == '__main__':
    p105()
