"""Economics XII PDF156: pp.292–293 — chapter 13 model paper: short questions 1–11, long questions i–vii, MCQs 1–5 (printed ✓).
Run: python class12_eco_page156.py"""
from class12_eco_common import BOOK, Builder, P, L, qa, mcqs, model


def Q(qe, qu, qp, ae, au, ap):
    return (qe, qu, qp, ae, au, ap)


def O(e, u=None, p=None):
    return (e, u or e, p or e)


QA = [
 Q('1. What is meant by an economic system?', '1۔ معاشی نظام سے کیا مراد ہے؟', '1. له اقتصادي نظام څه مراد دی؟',
   'A. “By an economic system is meant such an organisation in which, by using all the resources of any country, goods and services are prepared according to the necessities of life.”', 'جواب: ”معاشی نظام سے مراد ایسی تنظیم ہے جس میں کسی بھی ملک کے تمام ذرائع کو استعمال کر کے ضروریاتِ زندگی کے مطابق اشیاء اور خدمات تیار کی جاتی ہیں“', 'ځواب: ”له اقتصادي نظام مراد داسې تنظیم دی چې په کې د هر هېواد د ټولو سرچینو په کارولو د ژوند د اړتیاوو سره سم توکي او خدمتونه چمتو کېږي.“'),
 Q('2. Write the names of four important economic systems.', '2۔ چار اہم معاشی نظاموں کے نام تحریر کریں؟', '2. د څلورو مهمو اقتصادي نظامونو نومونه ولیکئ.',
   'A. (i) capitalist system; (ii) socialist or government-authority system; (iii) Islamic economic system; (iv) non-intervention or free-business system.', 'جواب: (i) سرمایہ داری نظام (ii) اشتراکی یا سرکاری اختیارات کا نظام (iii) اسلامی معاشی نظام (iv) عدمِ مداخلت یا آزاد کاروبار کا نظام', 'ځواب: (i) د پانګوالۍ نظام؛ (ii) سوسیالیستي یا د دولتي واکونو نظام؛ (iii) اسلامي اقتصادي نظام؛ (iv) د نه مداخلې یا ازاد کاروبار نظام.'),
 Q('3. Define the capitalist system.', '3۔ سرمایہ داری نظام کی تعریف کریں؟', '3. د پانګوالۍ نظام تعریف کړئ.',
   'A. “By the capitalist system is meant such a system of economic organisation whose important characteristic is the ‘right of private ownership’, and also that nature-made and man-made capital be used for the sake of private profit.”', 'جواب: ”سرمایہ داری نظام سے مراد ہے معاشی تنظیم کا ایسا سسٹم، جس کی اہم خصوصیت ہے، ”نجی ملکیت کا حق“ نیز قدرت ساز اور آدم ساز سرمائے کو نجی منافع کی خاطر استعمال کیا جائے۔“', 'ځواب: ”له پانګوالۍ نظام مراد د اقتصادي تنظیم داسې سیسټم دی چې مهمه ځانګړتیا یې ’د شخصي ملکیت حق‘ ده، او همداسې طبیعي او انسان‌جوړه پانګه د شخصي ګټې لپاره وکارول شي.“'),
 Q('4. Write four characteristics of the capitalist system.', '4۔ سرمایہ داری نظام کی چار خصوصیات تحریر کریں؟', '4. د پانګوالۍ نظام څلور ځانګړتیاوې ولیکئ.',
   'A. (i) right of private ownership and system of inheritance; (ii) freedom to do business; (iii) discovery of new technology; (iv) promotion of saving and investment.', 'جواب: (i) نجی ملکیت کا حق اور وراثت کا نظام (ii) کاروبار کرنے کی آزادی (iii) نئی ٹیکنالوجی کی دریافت (iv) بچت اور سرمایہ کاری کا فروغ', 'ځواب: (i) د شخصي ملکیت حق او د میراث نظام؛ (ii) د کاروبار کولو ازادي؛ (iii) د نوې ټکنالوژۍ موندنه؛ (iv) د سپما او پانګونې وده.'),
 Q('5. State four shortcomings of the capitalist system.', '5۔ سرمایہ داری نظام کی چار خامیاں بیان کریں؟', '5. د پانګوالۍ نظام څلور نیمګړتیاوې بیان کړئ.',
   'A. (i) capital is given superiority over man; (ii) improper spending on competition and advertising; (iii) concentration of wealth; (iv) economic ups and downs and instability.', 'جواب: (i) انسان پر سرمائے کو فوقیت دی جاتی ہے (ii) مقابلہ اور اشتہار بازی پر بیجا خرچ (iii) دولت کا ارتکاز (iv) معاشی اتار چڑھاؤ اور عدمِ استحکام', 'ځواب: (i) پانګې ته پر انسان لومړیتوب ورکول کېږي؛ (ii) پر سیالۍ او اعلاناتو بې‌ځایه لګښت؛ (iii) د شتمنۍ تمرکز؛ (iv) اقتصادي لوړې ژورې او بې‌ثباتي.'),
 Q('6. Define the socialist or government-authority system.', '6۔ اشتراکی یا سرکاری اختیارات کے نظام کی تعریف کریں؟', '6. سوسیالیستي یا د دولتي واکونو نظام تعریف کړئ.',
   'A. “By it is meant such a movement whose purpose is that all nature-made and man-made capital goods (which are used for producing things on a large scale) be given, instead of to individuals, into the custody of the nation collectively for ownership and management, so that the increasing national income can be distributed equally; but in this connection no blow should fall on the economic motive of the individual or his occupational freedom and on choice and liking in connection with consuming goods.”', 'جواب: ”اس سے مراد ایسی تحریک ہے جس کا مقصد ہے تمام قدرت ساز اور آدم ساز اشیائے سرمایہ (جو بڑے پیمانے پر چیزیں پیدا کرنے میں استعمال ہوتی ہے) کی ملکیت اور انتظام، افراد کی بجائے اجتماعی طور پر قوم کی تحویل میں دی جائیں تاکہ بڑھتی ہوئی قومی آمدنی مساویانہ طور پر تقسیم کی جا سکے لیکن اس سلسلے میں فرد کے معاشی محرک یا اسکی پیشہ ورانہ آزادی اور اشیائے صرف کرنے کے سلسلے میں انتخاب و پسند پر کوئی ضرب نہ لگے۔“', 'ځواب: ”له دې مراد داسې خوځښت دی چې موخه یې دا ده چې د ټولو طبیعي او انسان‌جوړو پانګیزو توکو (چې په لویه کچه د شیانو په تولید کې کارول کېږي) ملکیت او انتظام د کسانو پر ځای په ټولیز ډول د ملت تحویل ته ورکړل شي، تر څو زیاتېدونکی ملي عاید په برابر ډول ووېشل شي؛ خو په دې برخه کې د فرد پر اقتصادي انګېزې یا د هغه پر مسلکي ازادۍ او د مصرفي توکو په برخه کې پر انتخاب او خوښه هېڅ ګوزار ونه شي.“'),
 Q('7. Write the names of four characteristics of the socialist system.', '7۔ اشتراکی نظام کی چار خصوصیات کے نام لکھیے؟', '7. د سوسیالیستي نظام د څلورو ځانګړتیاوو نومونه ولیکئ.',
   'A. (i) productive resources in collective ownership; (ii) equal opportunities of progress; (iii) economic development; (iv) social security.', 'جواب: (i) پیداواری ذرائع، اجتماعی ملکیت کے (ii) ترقی کے یکساں مواقع (iii) معاشی ترقی (iv) معاشرتی تحفظ', 'ځواب: (i) تولیدي سرچینې په ټولیز ملکیت کې؛ (ii) د پرمختګ برابر فرصتونه؛ (iii) اقتصادي پرمختګ؛ (iv) ټولنیز خوندیتوب.'),
 Q('8. Write four shortcomings of the socialist system.', '8۔ اشتراکی نظام کی چار خامیاں تحریر کریں؟', '8. د سوسیالیستي نظام څلور نیمګړتیاوې ولیکئ.',
   'A. (i) ending of economic freedom; (ii) unsuitability of the government for business; (iii) the allocation of resources is not correct.', 'جواب: (i) معاشی آزادی کا خاتمہ (ii) کاروبار کیلئے سرکار کی ناموزونیت (iii) ذرائع کی تخصیص صحیح نہیں ہوتی۔', 'ځواب: (i) د اقتصادي ازادۍ پای؛ (ii) د کاروبار لپاره د حکومت ناوړتیا؛ (iii) د سرچینو تخصیص سم نه وي.'),
 Q('9. Define the Islamic economic system.', '9۔ اسلامی معاشی نظام کی تعریف کریں؟', '9. اسلامي اقتصادي نظام تعریف کړئ.',
   'A. Such an economic system which is based on Islamic principles. In the Islamic economic system there is opposition to interest, whereas there is no restriction on private property and permissible profits.', 'جواب: ایسا معاشی نظام جو اسلامی اصولوں پر مبنی ہو۔ اسلامی معاشی نظام میں سود کی مخالفت ہے جبکہ نجی جائیداد اور جائز منافع پر کوئی پابندی نہیں۔', 'ځواب: داسې اقتصادي نظام چې پر اسلامي اصولو ولاړ وي. په اسلامي اقتصادي نظام کې د سود مخالفت دی، حال دا چې پر شخصي ملکیت او روا ګټو هېڅ بندیز نشته.'),
 Q('10. Write the names of four characteristics of the Islamic economic system.', '10۔ اسلامی معاشی نظام کی چار خصوصیات کے نام تحریر کریں؟', '10. د اسلامي اقتصادي نظام د څلورو ځانګړتیاوو نومونه ولیکئ.',
   'A. (i) observance of Shariah limits; (ii) wide circulation of money; (iii) non-interest economy; (iv) free of exploitation.', 'جواب: (i) شرعی حدود کی پابندی (ii) زر کی وسیع گردش (iii) غیر سودی معیشت (iv) استحصال سے پاک', 'ځواب: (i) د شرعي حدودو پابندي؛ (ii) د پیسو پراخ دوران؛ (iii) بې‌سوده اقتصاد؛ (iv) له استثمار پاک.'),
 Q('11. Define the system of non-intervention.', '11۔ عدمِ مداخلت نظام کی تعریف کریں؟', '11. د نه مداخلې نظام تعریف کړئ.',
   'A. Such an economic system in which ordinary individuals have complete business freedom, and the government does not interfere in economic matters.', 'جواب: ایسا معاشی نظام جس میں عام افراد کو مکمل کاروباری آزادی حاصل ہو اور حکومت معاشی معاملات میں کوئی دخل نہ دے۔', 'ځواب: داسې اقتصادي نظام چې په کې عامو کسانو ته بشپړه سوداګریزه ازادي وي، او حکومت په اقتصادي چارو کې لاسوهنه نه کوي.')]

MCQ = [
 (('Ushr is applicable on this:', 'عشر اس پر لاگو ہوتا ہے:', 'عشر پر دې لګېږي:'),
  [O('trade goods', 'مالِ تجارت', 'سوداګریز مال'), O('agricultural produce', 'زرعی پیداوار', 'کرنیز تولید'), O('industrial produce', 'صنعتی پیداوار', 'صنعتي تولید'), O('exports', 'برآمدات', 'صادرات')], 1),
 (('This economic system is prevalent in Pakistan:', 'پاکستان میں یہ معاشی نظام رائج ہے:', 'په پاکستان کې دا اقتصادي نظام رواج دی:'),
  [O('Islamic economic system', 'اسلامی معاشی نظام', 'اسلامي اقتصادي نظام'), O('socialist system', 'اشتراکی نظام', 'سوسیالیستي نظام'), O('capitalist system', 'سرمایہ دارانہ نظام', 'د پانګوالۍ نظام')], 2),
 (('In socialism who makes the basic decisions?', 'سوشلزم میں بنیادی فیصلے کون کرتا ہے:', 'په سوسیالیزم کې بنسټیزې پرېکړې څوک کوي؟'),
  [O('the public', 'عوام', 'خلک'), O('the government', 'حکومت', 'حکومت'), O('demand and supply', 'طلب و رسد', 'غوښتنه او عرضه')], 1),
 (('In Pakistan the distribution of wealth is such:', 'پاکستان میں دولت کی تقسیم ایسی ہے:', 'په پاکستان کې د شتمنۍ وېش داسې دی:'),
  [O('equal', 'مساویانہ', 'برابر'), O('unequal', 'غیر مساویانہ', 'نابرابر'), O('just', 'منصفانہ', 'عادلانه'), O('progressive', 'ترقی پسندانہ', 'پرمختګ‌پاله')], 1),
 (('In a non-interest economy employment opportunities:', 'غیر سودی معیشت میں روزگاری مواقع:', 'په بې‌سوده اقتصاد کې د روزګار فرصتونه:'),
  [O('increase', 'بڑھتے ہیں', 'زیاتېږي'), O('do not increase', 'نہیں بڑھتے', 'نه زیاتېږي'), O('remain as they are', 'جوں کے توں رہتے ہیں', 'لکه څنګه چې دي پاتې کېږي')], 0)]


def p156():
    b = Builder()
    b.h('Model paper questions', 'ماڈل پرچہ سوالات', 'د نمونې پرچې پوښتنې')
    b.h('Subjective (Subjective), Section I (Section I)', 'انشائیہ (Subjective) حصہ اول (Section I)', 'تشریحي (Subjective)، لومړۍ برخه (Section I)')
    P(b, [('Question 1. Write short answers to the following questions:', 'سوال نمبر 1۔ درج ذیل سوالات کے مختصر جوابات تحریر کریں:', '۱ پوښتنه. د لاندې پوښتنو لنډ ځوابونه ولیکئ:')])
    qa(b, QA[:8])
    r1 = model(b, 13, 1, 156, 292)
    t = Builder()
    qa(t, QA[8:])
    t.h('Section II (Section II)', 'حصہ دوم (Section II)', 'دویمه برخه (Section II)')
    P(t, [('Question 2. Write detailed answers to the following questions:', 'سوال نمبر 2۔ درج ذیل سوالات کے مفصل جوابات تحریر کریں:', '۲ پوښتنه. د لاندې پوښتنو مفصل ځوابونه ولیکئ:')])
    L(t, [('i) State the characteristics of the capitalist economic system. (Mirpur Azad Kashmir Board 2010, Multan Board 2011)', 'i) سرمایہ دارانہ معاشی نظام کی خصوصیات بیان کریں۔ (میرپور آزاد کشمیر بورڈ 2010ء، ملتان بورڈ 2011ء)', 'i) د پانګوال اقتصادي نظام ځانګړتیاوې بیان کړئ. (میرپور ازاد کشمیر بورډ ۲۰۱۰، ملتان بورډ ۲۰۱۱)'),
          ('ii) State the shortcomings of the capitalist system (Capitalism).', 'ii) سرمایہ داری نظام (Capitalism) کی خامیاں بیان کیجئے۔', 'ii) د پانګوالۍ نظام (Capitalism) نیمګړتیاوې بیان کړئ.'),
          ('iii) Write the shortcomings of socialism.', 'iii) سوشلزم کی خامیاں لکھیے۔', 'iii) د سوسیالیزم نیمګړتیاوې ولیکئ.'),
          ('iv) State the important characteristics of the economic system of Islam. (Multan Board 2009, Bahawalpur Board 2009, Mirpur Azad Kashmir Board 2009, Bahawalpur Board 2010)', 'iv) اسلام کے معاشی نظام کی اہم خصوصیات بیان کیجئے۔ (ملتان بورڈ 2009ء، بہاولپور بورڈ 2009ء، میرپور آزاد کشمیر بورڈ 2009ء، بہاولپور بورڈ 2010ء)', 'iv) د اسلام د اقتصادي نظام مهمې ځانګړتیاوې بیان کړئ. (ملتان بورډ ۲۰۰۹، بهاولپور بورډ ۲۰۰۹، میرپور ازاد کشمیر بورډ ۲۰۰۹، بهاولپور بورډ ۲۰۱۰)'),
          ('v) In the Islamic economic system the concentration of wealth (Concentration of Wealth) has been declared forbidden. Write a note on it.', 'v) اسلامی معاشی نظام میں ارتکازِ دولت (Concentration of Wealth) کو ممنوع قرار دیا گیا ہے۔ اس پر نوٹ لکھیں؟', 'v) په اسلامي اقتصادي نظام کې د شتمنۍ تمرکز (Concentration of Wealth) منع ګڼل شوی. پر هغه یادښت ولیکئ.'),
          ('vi) Present a comparison of the Islamic economic system and the capitalist system.', 'vi) اسلامی معاشی نظام اور سرمایہ دارانہ نظام کا موازنہ پیش کیجئے۔', 'vi) د اسلامي اقتصادي نظام او پانګوال نظام پرتله وړاندې کړئ.'),
          ('vii) Make clear the economic importance of zakat.', 'vii) زکوٰۃ کی معاشی اہمیت واضح کریں۔', 'vii) د زکات اقتصادي اهمیت روښانه کړئ.')])
    t.h('Objective (Objective)', 'معروضی (Objective)', 'معروضي (Objective)')
    P(t, [('Question 3. More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال نمبر 3۔ ہر سوال کے ایک سے زیادہ جوابات دیئے گئے ہیں۔ ان میں سے درست جواب پر (✓) کا نشان لگایئے۔', '۳ پوښتنه. د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(t, MCQ)
    BOOK.save(156, [(13, r1), (13, model(t, 13, 2, 156, 293))], issues=[{'id': 'eco12-pdf156', 'unit': 13, 'printedPage': 292,
               'description': 'Printed: short Q8 asks for four shortcomings but three are given — kept; MCQs 2, 3 and 5 print only three options. Printed ticks kept as printed.'}])


if __name__ == '__main__':
    p156()
