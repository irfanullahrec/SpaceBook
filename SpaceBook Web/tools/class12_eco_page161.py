"""Economics XII PDF161: pp.302–303 — board paper 2018: Q3 (x)–(xii), Q4 (i)–(xiii), part II Q5–9; board paper 2019 objective
MCQs 1–10. Run: python class12_eco_page161.py"""
from class12_eco_common import BOOK, Builder, P, L, mcqs


def O(e, u=None, p=None):
    return (e, u or e, p or e)


Q3 = [('(x) What is meant by the low efficiency of labour?', '(x) محنت کی پست استعدادِ کار سے کیا مراد ہے؟', '(x) د کار له ټیټې کاري وړتیا څه مراد دی؟'),
      ('(xi) Write four reasons for per capita income being low.', '(xi) فی کس آمدنی پست ہونے کی چار وجوہات تحریر کیجیے۔', '(xi) د سړي سر عاید د ټیټوالي څلور لاملونه ولیکئ.'),
      ('(xii) Define musharaka.', '(xii) مشارکہ کی تعریف کیجیے۔', '(xii) مشارکه تعریف کړئ.')]
Q4 = [('(i) Why is Pakistan called a developing country?', '(i) پاکستان کو ترقی پذیر ملک کیوں کہتے ہیں؟', '(i) پاکستان ته ولې پرمختیايي هېواد وايي؟'),
      ('(ii) Write four problems of the agricultural sector of Pakistan.', '(ii) پاکستان کے زرعی شعبے کے چار مسائل تحریر کیجیے۔', '(ii) د پاکستان د کرنیزې برخې څلور ستونزې ولیکئ.'),
      ('(iii) Define waterlogging and salinity.', '(iii) سیم و تھور کی تعریف کیجیے۔', '(iii) سیم او تور تعریف کړئ.'),
      ('(iv) What is meant by sick industrial units?', '(iv) بیمار صنعتی یونٹس سے کیا مراد ہے؟', '(iv) له ناروغو صنعتي واحدونو څه مراد دی؟'),
      ('(v) What is meant by geographical mobility?', '(v) جغرافیائی حرکت پذیری سے کیا مراد ہے؟', '(v) له جغرافیايي حرکت څه مراد دی؟'),
      ('(vi) What is meant by a dry port?', '(vi) خشک گودی سے کیا مراد ہے؟', '(vi) له وچ بندر څه مراد دی؟'),
      ('(vii) What is meant by an agricultural market?', '(vii) زرعی منڈی سے کیا مراد ہے؟', '(vii) له کرنیز بازار څه مراد دی؟'),
      ('(viii) Write the names of four important departments of the State Bank of Pakistan.', '(viii) سٹیٹ بینک آف پاکستان کے چار اہم شعبوں کے نام لکھیے۔', '(viii) د پاکستان دولتي بانک د څلورو مهمو څانګو نومونه ولیکئ.'),
      ('(ix) Define ushr.', '(ix) عشر کی تعریف کیجیے۔', '(ix) عشر تعریف کړئ.'),
      ('(x) What is the difference between zakat and tax?', '(x) زکوٰۃ اور ٹیکس میں فرق کیا ہے؟', '(x) د زکات او مالیې ترمنځ څه توپیر دی؟'),
      ('(xi) What is meant by the export bonus scheme?', '(xi) ایکسپورٹ بونس سکیم سے کیا مراد ہے؟', '(xi) د صادراتو د بونس له طرحې څه مراد دی؟'),
      ('(xii) What is meant by the economic system of Islam?', '(xii) اسلام کے معاشی نظام سے کیا مراد ہے؟', '(xii) د اسلام له اقتصادي نظام څه مراد دی؟'),
      ('(xiii) What is the concept of ownership in Islam?', '(xiii) اسلام میں ملکیت کا کیا تصور ہے؟', '(xiii) په اسلام کې د ملکیت تصور څه دی؟')]
LONG = [('5. Write in detail the production method of measuring national income and also write the precautions.', '5۔ قومی آمدنی کی پیمائش کا پیداوار کا طریقہ تفصیل سے لکھیے اور احتیاطیں بھی تحریر کیجیے۔', '۵. د ملي عاید د اندازه کولو د تولید طریقه په تفصیل ولیکئ او احتیاطونه یې هم ولیکئ.'),
        ('6. State the functions of the State Bank of Pakistan.', '6۔ سٹیٹ بینک آف پاکستان کے فرائض بیان کیجیے۔', '۶. د پاکستان دولتي بانک دندې بیان کړئ.'),
        ('7. State the important principles of imposing taxes.', '7۔ ٹیکس عائد کرنے کے اہم اصول بیان کیجیے۔', '۷. د مالیې د لګولو مهم اصول بیان کړئ.'),
        ('8. Write the benefits and harms of international trade.', '8۔ بین الاقوامی تجارت کے فوائد اور نقصانات تحریر کیجیے۔', '۸. د نړیوالې سوداګرۍ ګټې او زیانونه ولیکئ.'),
        ('9. Write the characteristics of the Islamic economic system.', '9۔ اسلامی معاشی نظام کی خصوصیات لکھیے۔', '۹. د اسلامي اقتصادي نظام ځانګړتیاوې ولیکئ.')]

MCQ = [
 (('This is not included in the quantitative methods of monetary policy:', 'زری پالیسی کے مقداری طریقوں میں شامل نہیں:', 'دا د پولي پالیسۍ په مقداري طریقو کې شامل نه دی:'),
  [O('open market operations', 'کھلے بازار کا عمل', 'د خلاص بازار عملیات'), O('bank rate policy', 'بینک ریٹ پالیسی', 'د بانک نرخ پالیسي'), O('rationing', 'راشن بندی', 'راشنینګ'), O('advertising', 'اشتہار بازی', 'اعلانات')], None),
 (('The government policy related to imports and exports is called:', 'درآمدات اور برآمدات سے متعلقہ حکومتی پالیسی کہلاتی ہے:', 'د وارداتو او صادراتو اړوند حکومتي پالیسي بلل کېږي:'),
  [O('monetary policy', 'زری پالیسی', 'پولي پالیسي'), O('fiscal policy', 'مالیاتی پالیسی', 'مالي پالیسي'), O('trade policy', 'تجارتی پالیسی', 'سوداګریزه پالیسي'), O('price policy', 'قیمت پالیسی', 'د بیو پالیسي')], None),
 (('Which is not a transfer payment?', 'کون سی انتقالی ادائیگی نہیں ہے:', 'کومه لېږدونیزه ورکړه نه ده؟'),
  [O('pension', 'پنشن', 'تقاعد'), O('wage', 'اجرت', 'مزدوري'), O('stipend', 'وظیفہ', 'وظیفه'), O('alms', 'خیرات', 'خیرات')], None),
 (('The theory of trade of absolute advantage was presented by:', 'کلی برتری کا نظریہ تجارت پیش کیا:', 'د مطلقې برترۍ د سوداګرۍ نظریه وړاندې کړه:'),
  [O('Adam Smith', 'آدم سمتھ', 'اډم سمیټ'), O('David Ricardo', 'ڈیوڈ ریکارڈو', 'ډېوډ ریکارډو'), O('Pigou', 'پیگو', 'پیګو'), O('Marshall', 'مارشل', 'مارشل')], None),
 (('The consumption function is related to:', 'تفاعلِ صرف کا تعلق ہے:', 'د مصرف تابع تړاو لري:'),
  [O('income and investment', 'آمدنی اور سرمایہ کاری', 'عاید او پانګونه'), O('income and consumption', 'آمدنی اور صرف', 'عاید او مصرف'), O('income and saving', 'آمدنی اور بچت', 'عاید او سپما'), O('income and rate of interest', 'آمدنی اور شرحِ سود', 'عاید او د سود نرخ')], None),
 (('Fiscal policy is related:', 'مالیاتی پالیسی کا تعلق ہے:', 'مالي پالیسي تړاو لري:'),
  [O('to the public', 'عوام سے', 'له خلکو سره'), O('to the government', 'حکومت سے', 'له حکومت سره'), O('to the central bank', 'مرکزی بینک سے', 'له مرکزي بانک سره'), O('to the commercial bank', 'تجارتی بینک سے', 'له سوداګریز بانک سره')], None),
 (('Commercial banks create:', 'تجارتی بینک تخلیق کرتے ہیں:', 'سوداګریز بانکونه پیدا کوي:'),
  [O('credit money', 'اعتباری زر', 'اعتباري پیسې'), O('token money', 'علامتی زر', 'نښه‌یي پیسې'), O('legal tender money', 'قانونی زر', 'قانوني پیسې'), O('metallic money', 'دھاتی زر', 'فلزي پیسې')], None),
 (('The speculative demand for money depends:', 'زر کی تخمینی طلب کا انحصار ہوتا ہے:', 'د پیسو اټکلي غوښتنه اړه لري:'),
  [O('on business conditions', 'کاروباری حالات پر', 'پر سوداګریزو حالاتو'), O('on the rate of interest', 'شرحِ سود پر', 'د سود پر نرخ'), O('on investment', 'سرمایہ کاری پر', 'پر پانګونه'), O('on income', 'آمدنی پر', 'پر عاید')], None),
 (('The biggest source of the government’s income is:', 'حکومت کی آمدنی کا سب سے بڑا ذریعہ ہے:', 'د حکومت د عاید تر ټولو لویه سرچینه ده:'),
  [O('tax', 'ٹیکس', 'مالیه'), O('fines', 'جرمانے', 'جریمې'), O('loans', 'قرضے', 'پورونه'), O('deficit financing', 'خسارے کی سرمایہ کاری', 'کسري تمویل')], None),
 (('That document which the buyer writes to the seller is called:', 'وہ دستاویز جو خریدار فروخت کار کو لکھ دیتا ہے کہلاتی ہے:', 'هغه سند چې پېرودونکی یې پلورونکي ته لیکي، بلل کېږي:'),
  [O('cheque', 'چیک', 'چک'), O('draft', 'ڈرافٹ', 'ډرافټ'), O('crossed cheque', 'نشان زدہ چیک', 'نښه شوی چک'), O('hundi (bill)', 'ہنڈی', 'هنډۍ')], None)]


def p161():
    b = Builder()
    L(b, Q3)
    P(b, [('4. Write short answers to any nine (9) questions:', '4۔ کوئی سے نو (9) سوالات کے مختصر جوابات لکھیے:', '۴. د هرو نهو (۹) پوښتنو لنډ ځوابونه ولیکئ:')])
    L(b, Q4)
    b.h('Part II', '(حصہ دوم)', 'دویمه برخه')
    P(b, [('Note: write answers to any three questions.', 'نوٹ: کوئی سے تین سوالات کے جوابات لکھیے۔', 'یادونه: د هرو درېیو پوښتنو ځوابونه ولیکئ.')])
    L(b, LONG)
    r1 = BOOK.record(b, 'eco12-papers-4', 'Board paper 2018 — subjective (2)', 'بورڈ پرچہ 2018ء — انشائیہ (2)', 'د بورډ پرچه ۲۰۱۸ — تشریحي (۲)', 161, [302])
    t = Builder()
    t.h('Economics Inter Part-II (2019)', 'اکنامکس انٹر پارٹ II (2019)', 'اقتصاد انټر دویمه برخه (۲۰۱۹)')
    P(t, [('Paper II (objective type)', 'پرچہ II (معروضی طرز)', 'دویمه پرچه (معروضي بڼه)'),
          ('Note: four possible answers A, B, C and D have been given for each question. On the answer copy, fill the circle according to the correct answer with a marker or pen in the circles given in front of each question. In case of filling more than one circle or cutting and filling, the said answer will be considered wrong.', 'نوٹ: ہر سوال کے چار ممکنہ جوابات A، B، C اور D دیئے گئے ہیں۔ جوابی کاپی پر ہر سوال کے سامنے دیئے گئے دائروں میں سے درست جواب کے مطابق متعلقہ دائرہ کو مارکر یا پین سے بھر دیجئے۔ ایک سے زیادہ دائروں کو پُر کرنے یا کاٹ کر پُر کرنے کی صورت میں مذکورہ جواب غلط تصور ہو گا۔', 'یادونه: د هرې پوښتنې څلور ممکنه ځوابونه A، B، C او D ورکړل شوي. د ځواب په کاپي کې د هرې پوښتنې مخې ته ورکړل شوو دایرو کې د سم ځواب اړونده دایره په مارکر یا قلم ډکه کړئ. له یوې زیاتې دایرې د ډکولو یا د غوڅولو او ډکولو په صورت کې به ځواب غلط وګڼل شي.')])
    mcqs(t, MCQ)
    r2 = BOOK.record(t, 'eco12-papers-5', 'Board paper 2019 — objective (1)', 'بورڈ پرچہ 2019ء — معروضی (1)', 'د بورډ پرچه ۲۰۱۹ — معروضي (۱)', 161, [303])
    BOOK.save(161, [(14, r1), (14, r2)], issues=[{'id': 'eco12-pdf161', 'unit': 14, 'printedPage': 302,
               'description': 'Board paper questions transcribed as printed; no answers are printed for the MCQs, and none are added.'}])


if __name__ == '__main__':
    p161()
