"""Economics XII PDF162: pp.304–305 — board paper 2019: MCQs 11–20; subjective part I, Q2 (i)–(xii), Q3 (i)–(xii), Q4 (i)–(ii).
Run: python class12_eco_page162.py"""
from class12_eco_common import BOOK, Builder, P, L, mcqs


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('The rate of ushr on produce obtained from artificial means of irrigation is:', 'مصنوعی ذرائع آبپاشی سے حاصل ہونے والی پیداوار پر عشر کی شرح ہے:', 'د اوبو لګولو له مصنوعي وسایلو د ترلاسه شوي تولید پر عشر نرخ دی:'),
  [O('10 per cent', '10% فیصد', '۱۰ سلنه'), O('5 per cent', '5% فیصد', '۵ سلنه'), O('8 per cent', '8% فیصد', '۸ سلنه'), O('25 per cent', '25% فیصد', '۲۵ سلنه')], None),
 (('Stock exchanges working in Pakistan:', 'پاکستان میں سٹاک ایکسچینج کام کر رہے ہیں:', 'په پاکستان کې کار کوونکي سټاک اېکسچینجونه:'),
  [O('four', 'چار', 'څلور'), O('three', 'تین', 'درې'), O('two', 'دو', 'دوه'), O('one', 'ایک', 'یو')], None),
 (('In this period the growth rate of Pakistan was more than the target:', 'اس عرصہ میں پاکستان کی شرحِ نمو سب سے زیادہ تھی:', 'په دې موده کې د پاکستان د ودې نرخ تر ټولو لوړ و:'),
  [O('1950-60', '1950-60', '۱۹۵۰-۶۰'), O('1960-70', '1960-70', '۱۹۶۰-۷۰'), O('1970-80', '1970-80', '۱۹۷۰-۸۰'), O('1980-90', '1980-90', '۱۹۸۰-۹۰')], None),
 (('It provides loans for the construction of houses:', 'مکانات کی تعمیر کے لیے قرضہ فراہم کرتا ہے:', 'د کورونو د جوړولو لپاره پور برابروي:'),
  [O('industrial bank', 'صنعتی بینک', 'صنعتي بانک'), O('agricultural bank', 'زرعی بینک', 'کرنیز بانک'), O('House Building Finance Corporation', 'ہاؤس بلڈنگ فنانس کارپوریشن', 'د کور جوړونې مالي کارپوریشن'), O('commercial bank', 'تجارتی بینک', 'سوداګریز بانک')], None),
 (('Per capita income is equal to:', 'فی کس آمدنی مساوی ہے:', 'سړي سر عاید برابر دی:'),
  [O('total national income ÷ total consumption expenditure', 'کل قومی آمدنی ÷ کل صرفی اخراجات', 'ټول ملي عاید ÷ ټول مصرفي لګښتونه'), O('total national income ÷ total population', 'کل قومی آمدنی ÷ کل آبادی', 'ټول ملي عاید ÷ ټول نفوس'), O('total national income ÷ total labourers', 'کل قومی آمدنی ÷ کل مزدور', 'ټول ملي عاید ÷ ټول کارګران'), O('total national income ÷ total youth', 'کل قومی آمدنی ÷ کل نوجوان', 'ټول ملي عاید ÷ ټول ځوانان')], None),
 (('The most successful five-year plan of Pakistan was:', 'پاکستان کا سب سے کامیاب پانچ سالہ منصوبہ تھا:', 'د پاکستان تر ټولو بریالی پنځه کلن پلان و:'),
  [O('second', 'دوسرا', 'دویم'), O('third', 'تیسرا', 'درېیم'), O('fourth', 'چوتھا', 'څلورم'), O('eighth', 'آٹھواں', 'اتم')], None),
 (('These are included in the means of communications:', 'ذرائع مواصلات میں شامل ہیں:', 'د مخابراتو په وسایلو کې دا شامل دي:'),
  [O('roads', 'سڑکیں', 'سړکونه'), O('railway', 'ریلوے', 'رېل'), O('ports', 'بندرگاہیں', 'بندرونه'), O('radio and television', 'ریڈیو اور ٹیلی ویژن', 'راډیو او ټلویزیون')], None),
 (('Islam is opposed to:', 'اسلام مخالف ہے:', 'اسلام مخالف دی:'),
  [O('monopoly', 'اجارہ داری کا', 'د انحصار'), O('perfect competition', 'مکمل مقابلہ کا', 'د بشپړې سیالۍ'), O('trade', 'تجارت کا', 'د سوداګرۍ'), O('agriculture', 'زراعت کا', 'د کرنې')], None),
 (('Waterlogging and salinity is a problem of:', 'سیم اور تھور مسئلہ ہے:', 'سیم او تور ستونزه ده:'),
  [O('industry', 'صنعت کا', 'د صنعت'), O('agriculture', 'زراعت کا', 'د کرنې'), O('trade', 'تجارت کا', 'د سوداګرۍ'), O('minerals', 'معدنیات کا', 'د کانونو')], None),
 (('The new name of RCD is:', 'آر سی ڈی کا نیا نام ہے:', 'د RCD نوی نوم دی:'),
  [O('WTO', 'ڈبلیو ٹی او', 'WTO'), O('OIC', 'او آئی سی', 'OIC'), O('ECO', 'ای سی او', 'ECO'), O('ASEAN', 'آسیان', 'اسیان')], None)]

Q2 = [('(i) What is meant by agricultural income?', '(i) زرعی آمدنی سے کیا مراد ہے؟', '(i) له کرنیز عاید څه مراد دی؟'),
      ('(ii) Define gross domestic product.', '(ii) خام ملکی پیداوار کی تعریف کیجئے۔', '(ii) ناخالص کورنی تولید تعریف کړئ.'),
      ('(iii) What do you mean by depreciation expenses?', '(iii) فرسودگی کے اخراجات سے آپ کیا مراد لیتے ہیں؟', '(iii) د استهلاک له لګښتونو څه مراد اخلئ؟'),
      ('(iv) What is meant by the average propensity to consume?', '(iv) اوسط میلانِ صرف سے کیا مراد ہے؟', '(iv) د مصرف له اوسط تمایل څه مراد دی؟'),
      ('(v) State the definition of metallic money.', '(v) دھاتی زر کی تعریف بیان کیجئے۔', '(v) د فلزي پیسو تعریف بیان کړئ.'),
      ('(vi) Define a cheque.', '(vi) چیک کی تعریف کیجئے۔', '(vi) چک تعریف کړئ.'),
      ('(vii) What is meant by the demand for money?', '(vii) زر کی طلب سے کیا مراد ہے؟', '(vii) د پیسو له غوښتنې څه مراد دی؟'),
      ('(viii) What is meant by the process of money creation?', '(viii) زر کی تخلیق کے عمل سے کیا مراد ہے؟', '(viii) د پیسو د پیدا کولو له بهیر څه مراد دی؟'),
      ('(ix) What is meant by a bank draft?', '(ix) بینک ڈرافٹ سے کیا مراد ہے؟', '(ix) له بانکي ډرافټ څه مراد دی؟'),
      ('(x) Define a crossed cheque.', '(x) نشان زدہ چیک کی تعریف کیجئے۔', '(x) نښه شوی چک تعریف کړئ.'),
      ('(xi) Define the bank rate.', '(xi) شرحِ بینک کی تعریف کیجئے۔', '(xi) د بانک نرخ تعریف کړئ.'),
      ('(xii) What is meant by a central bank?', '(xii) مرکزی بینک سے کیا مراد ہے؟', '(xii) له مرکزي بانک څه مراد دی؟')]
Q3 = [('(i) What is meant by private finance?', '(i) نجی مالیات سے کیا مراد ہے؟', '(i) له شخصي مالیې څه مراد دی؟'),
      ('(ii) What is meant by public finance?', '(ii) سرکاری مالیات سے کیا مراد ہے؟', '(ii) له دولتي مالیې څه مراد دی؟'),
      ('(iii) What is meant by the policy of deficit?', '(iii) خسارے کی پالیسی سے کیا مراد ہے؟', '(iii) د کسر له پالیسۍ څه مراد دی؟'),
      ('(iv) Write four principles of tax.', '(iv) ٹیکس کے چار اصول تحریر کیجئے۔', '(iv) د مالیې څلور اصول ولیکئ.'),
      ('(v) What is meant by international trade?', '(v) بین الاقوامی تجارت سے کیا مراد ہے؟', '(v) له نړیوالې سوداګرۍ څه مراد دی؟'),
      ('(vi) Define domestic trade.', '(vi) ملکی تجارت کی تعریف کیجئے۔', '(vi) کورنۍ سوداګري تعریف کړئ.'),
      ('(vii) State the difference between the current account and the capital account.', '(vii) حسابِ رواں اور حسابِ سرمایہ میں فرق بیان کیجئے۔', '(vii) د روان حساب او پانګیز حساب توپیر بیان کړئ.'),
      ('(viii) What is meant by a uniform rate of exchange?', '(viii) یکساں شرحِ مبادلہ سے کیا مراد ہے؟', '(viii) له یوشان تبادلې نرخ څه مراد دی؟'),
      ('(ix) Write three lines on the importance of agriculture in Pakistan.', '(ix) پاکستان میں زراعت کی اہمیت پر تین سطور تحریر کیجئے۔', '(ix) په پاکستان کې د کرنې پر اهمیت درې کرښې ولیکئ.'),
      ('(x) Write four reasons for the standard of living being low in Pakistan.', '(x) پاکستان میں معیارِ زندگی پست ہونے کی چار وجوہات تحریر کیجئے۔', '(x) په پاکستان کې د ژوند د معیار د ټیټوالي څلور لاملونه ولیکئ.'),
      ('(xi) Write four proposals for the promotion of industrial development.', '(xi) صنعتی ترقی کے فروغ کے لیے چار تجاویز تحریر کیجئے۔', '(xi) د صنعتي پرمختګ د ودې لپاره څلور وړاندیزونه ولیکئ.'),
      ('(xii) Write four proposals for increase in agricultural production.', '(xii) زرعی پیداوار میں اضافہ کے لیے چار تجاویز تحریر کیجئے۔', '(xii) په کرنیز تولید کې د زیاتوالي لپاره څلور وړاندیزونه ولیکئ.')]
Q4 = [('(i) What is meant by economic planning?', '(i) معاشی منصوبہ بندی سے کیا مراد ہے؟', '(i) له اقتصادي پلان جوړونې څه مراد دی؟'),
      ('(ii) Write four factors affecting economic development. … (continued on p.306)', '(ii) معاشی ترقی پر اثر انداز ہونے والے چار عوامل تحریر کیجئے۔ … (ص 306 پر جاری)', '(ii) پر اقتصادي پرمختګ اغېز کوونکي څلور عوامل ولیکئ. … (په ۳۰۶ مخ دوام)')]


def p162():
    b = Builder()
    mcqs(b, MCQ, start=11)
    b.h('Subjective type, Part I', '(انشائیہ طرز) (حصہ اول)', 'تشریحي بڼه، لومړۍ برخه')
    P(b, [('2. Write short answers to any eight (8) questions:', '2۔ کوئی سے آٹھ (8) سوالات کے مختصر جوابات لکھئے:', '۲. د هرو اتو (۸) پوښتنو لنډ ځوابونه ولیکئ:')])
    L(b, Q2[:2])
    r1 = BOOK.record(b, 'eco12-papers-6', 'Board paper 2019 — objective (2)', 'بورڈ پرچہ 2019ء — معروضی (2)', 'د بورډ پرچه ۲۰۱۹ — معروضي (۲)', 162, [304])
    t = Builder()
    L(t, Q2[2:])
    P(t, [('3. Write short answers to any eight (8) questions:', '3۔ کوئی سے آٹھ (8) سوالات کے مختصر جوابات لکھئے:', '۳. د هرو اتو (۸) پوښتنو لنډ ځوابونه ولیکئ:')])
    L(t, Q3)
    P(t, [('4. Write short answers to any nine (9) questions:', '4۔ کوئی سے نو (9) سوالات کے مختصر جوابات لکھئے:', '۴. د هرو نهو (۹) پوښتنو لنډ ځوابونه ولیکئ:')])
    L(t, Q4)
    r2 = BOOK.record(t, 'eco12-papers-7', 'Board paper 2019 — subjective (1)', 'بورڈ پرچہ 2019ء — انشائیہ (1)', 'د بورډ پرچه ۲۰۱۹ — تشریحي (۱)', 162, [305])
    BOOK.save(162, [(14, r1), (14, r2)], issues=[{'id': 'eco12-pdf162', 'unit': 14, 'printedPage': 304,
               'description': 'Board paper questions transcribed as printed; MCQ 15 options printed as fractions “کل قومی آمدنی / …” rendered with “÷”. MCQ 13 stem “شرحِ نمو سب سے زیادہ تھی” (stem partly reads “ہدف سے زیادہ”) kept by sense. No answers printed.'}])


if __name__ == '__main__':
    p162()
