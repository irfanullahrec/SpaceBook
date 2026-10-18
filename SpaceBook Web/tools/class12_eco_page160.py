"""Economics XII PDF160: pp.300–301 — board paper 2018: MCQs 11–20; subjective part I, Q2 (i)–(xii) and Q3 (i)–(ix).
Run: python class12_eco_page160.py"""
from class12_eco_common import BOOK, Builder, P, L, mcqs


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('To make the pace of capital formation fast:', 'تشکیلِ سرمایہ کی رفتار تیز کرنے کے لیے:', 'د پانګې د جوړېدو د سرعت د چټکولو لپاره:'),
  [O('increase in savings', 'بچتوں میں اضافہ', 'په سپما کې زیاتوالی'), O('increase in tax', 'ٹیکس میں اضافہ', 'په مالیه کې زیاتوالی'), O('increase in loans', 'قرضوں میں اضافہ', 'په پورونو کې زیاتوالی'), O('increase in consumption expenditure', 'صرفی خرچ میں اضافہ', 'په مصرفي لګښت کې زیاتوالی')], None),
 (('In Pakistan income tax is:', 'پاکستان میں انکم ٹیکس ہے:', 'په پاکستان کې د عاید مالیه ده:'),
  [O('proportional tax', 'متناسب ٹیکس', 'متناسبه مالیه'), O('indirect tax', 'بالواسطہ ٹیکس', 'غیرمستقیمه مالیه'), O('progressive tax', 'متزائد ٹیکس', 'مخ په زیاتېدو مالیه'), O('regressive tax', 'تنزلی ٹیکس', 'کمېدونکې مالیه')], None),
 (('Economic development is:', 'معاشی ترقی ہے:', 'اقتصادي پرمختګ دی:'),
  [O('development of means of transport', 'ذرائع نقل و حمل کی ترقی', 'د ترانسپورټ د وسایلو پرمختګ'), O('increase in agricultural production', 'زرعی پیداوار میں اضافہ', 'په کرنیز تولید کې زیاتوالی'), O('increase in real national income', 'حقیقی قومی آمدنی میں اضافہ', 'په حقیقي ملي عاید کې زیاتوالی'), O('increase in industrial production', 'صنعتی پیداوار میں اضافہ', 'په صنعتي تولید کې زیاتوالی')], None),
 (('The State Bank of Pakistan was inaugurated by:', 'سٹیٹ بینک آف پاکستان کا افتتاح کیا:', 'د پاکستان دولتي بانک پرانیسته وکړه:'),
  [O('Malik Feroz Khan', 'ملک فیروز خان', 'ملک فیروز خان'), O('Liaquat Ali Khan', 'لیاقت علی خان', 'لیاقت علي خان'), O('Quaid-e-Azam', 'قائدِ اعظمؒ', 'قائد اعظم (رح)'), O('Chaudhry Muhammad Ali', 'چودھری محمد علی', 'چودري محمد علي')], None),
 (('Economically Pakistan is included:', 'پاکستان معاشی لحاظ سے شامل ہوتا ہے:', 'پاکستان له اقتصادي پلوه شامل دی:'),
  [O('in backward countries', 'پس ماندہ ممالک میں', 'په وروسته پاتې هېوادونو کې'), O('in industrial countries', 'صنعتی ممالک میں', 'په صنعتي هېوادونو کې'), O('in developed countries', 'ترقی یافتہ ممالک میں', 'په پرمختللو هېوادونو کې'), O('in developing countries', 'ترقی پذیر ممالک میں', 'په پرمختیايي هېوادونو کې')], None),
 (('The friend of Allah is:', 'اللہ کا دوست ہوتا ہے:', 'د الله دوست وي:'),
  [O('the labourer', 'مزدور', 'کارګر'), O('the capitalist', 'سرمایہ دار', 'پانګوال'), O('the rich man', 'امیر آدمی', 'شتمن سړی'), O('the doctor', 'ڈاکٹر', 'ډاکټر')], None),
 (('In Pakistan the policy of nationalisation was adopted in:', 'پاکستان میں قومیانے کی پالیسی اختیار کی گئی:', 'په پاکستان کې د ملي کولو پالیسي غوره شوه:'),
  [O('1957', '1957', '۱۹۵۷'), O('1961', '1961', '۱۹۶۱'), O('1972', '1972', '۱۹۷۲'), O('1999', '1999', '۱۹۹۹')], None),
 (('This is included in the modern means of transport:', 'نقل و حمل کے جدید ذرائع میں شامل ہے:', 'د ترانسپورټ په عصري وسایلو کې دا شامل دی:'),
  [O('motorway', 'موٹروے', 'موټروې'), O('shipping', 'کشتی رانی', 'کښتۍ چلول'), O('phone', 'فون', 'ټیلیفون'), O('internet', 'انٹرنیٹ', 'انټرنېټ')], None),
 (('By E.C.O is meant:', 'ای سی او (E.C.O) سے مراد:', 'له E.C.O مراد:'),
  [O('Regional Cooperation for Development', 'علاقائی تعاون برائے ترقی', 'د پرمختګ لپاره سیمه‌ییزه همکاري'), O('institution of exporters', 'برآمد کنندگان کا ادارہ', 'د صادروونکو اداره'), O('Economic Cooperation Organisation', 'معاشی تعاون کی تنظیم', 'د اقتصادي همکارۍ سازمان'), O('OPEC', 'اوپیک', 'اوپېک')], None),
 (('Economic planning is:', 'معاشی منصوبہ بندی ہے:', 'اقتصادي پلان جوړونه ده:'),
  [O('plans of industrial development', 'صنعتی ترقی کے منصوبے', 'د صنعتي پرمختګ پلانونه'), O('increase in population', 'آبادی میں اضافہ', 'په نفوس کې زیاتوالی'), O('increase in real income over a long period', 'عرصہ طویل میں حقیقی آمدنی میں اضافہ', 'په اوږده موده کې په حقیقي عاید کې زیاتوالی'), O('increase in agricultural production', 'زرعی پیداوار میں اضافہ', 'په کرنیز تولید کې زیاتوالی')], None)]

Q2 = [('(i) State the definition of gross domestic product.', '(i) خام ملکی پیداوار کی تعریف بیان کیجیے۔', '(i) د ناخالص کورني تولید تعریف بیان کړئ.'),
      ('(ii) Define the marginal propensity to consume.', '(ii) مختتم میلانِ صرف کی تعریف کیجیے۔', '(ii) د مصرف حاشیوي تمایل تعریف کړئ.'),
      ('(iii) What is meant by investment?', '(iii) سرمایہ کاری سے کیا مراد ہے؟', '(iii) له پانګونې څه مراد دی؟'),
      ('(iv) Define personal income.', '(iv) شخصی آمدنی کی تعریف کیجیے۔', '(iv) شخصي عاید تعریف کړئ.'),
      ('(v) What is meant by near money?', '(v) قریبی زر سے کیا مراد ہے؟', '(v) له نږدې پیسو څه مراد دی؟'),
      ('(vi) What is a credit card?', '(vi) کریڈٹ کارڈ کیا ہے؟', '(vi) کریډیټ کارت څه دی؟'),
      ('(vii) What is meant by a crossed cheque?', '(vii) نشان زدہ چیک سے کیا مراد ہے؟', '(vii) له نښه شوي چک څه مراد دی؟'),
      ('(viii) What is meant by paper money?', '(viii) کاغذی زر سے کیا مراد ہے؟', '(viii) له کاغذي پیسو څه مراد دی؟'),
      ('(ix) Define an agricultural bank.', '(ix) زرعی بینک کی تعریف کیجیے۔', '(ix) کرنیز بانک تعریف کړئ.'),
      ('(x) What is meant by demand deposits?', '(x) طلبی امانتوں سے کیا مراد ہے؟', '(x) له غوښتنې امانتونو څه مراد دی؟'),
      ('(xi) Define qarz-e-hasana.', '(xi) قرضِ حسنہ کی تعریف کیجیے۔', '(xi) قرض حسنه تعریف کړئ.'),
      ('(xii) Write four functions of a commercial bank.', '(xii) تجارتی بینک کے چار فرائض تحریر کیجیے۔', '(xii) د سوداګریز بانک څلور دندې ولیکئ.')]
Q3 = [('(i) What is meant by the budget?', '(i) بجٹ سے کیا مراد ہے؟', '(i) له بودجې څه مراد دی؟'),
      ('(ii) What is meant by the policy of protection?', '(ii) تامین کی پالیسی سے کیا مراد ہے؟', '(ii) د ساتنې له پالیسۍ څه مراد دی؟'),
      ('(iii) State the difference between public and private finance.', '(iii) سرکاری اور نجی مالیات میں فرق بیان کیجیے۔', '(iii) د دولتي او شخصي مالیې توپیر بیان کړئ.'),
      ('(iv) What is meant by a direct tax?', '(iv) براہِ راست ٹیکس سے کیا مراد ہے؟', '(iv) له مستقیمې مالیې څه مراد دی؟'),
      ('(v) What is meant by the word specialisation in trade?', '(v) تجارت میں لفظ تخصیص کار سے کیا مراد ہے؟', '(v) په سوداګرۍ کې د ”تخصص“ له کلمې څه مراد دی؟'),
      ('(vi) State the difference between the current account and the capital account.', '(vi) حسابِ رواں اور حسابِ سرمایہ میں فرق بیان کیجیے۔', '(vi) د روان حساب او پانګیز حساب توپیر بیان کړئ.'),
      ('(vii) What is meant by services without compensation?', '(vii) بلا معاوضہ خدمات سے کیا مراد ہے؟', '(vii) له بې‌عوضه خدمتونو څه مراد دی؟'),
      ('(viii) What is meant by multinational corporations?', '(viii) ملٹی نیشنل کارپوریشنز سے کیا مراد ہے؟', '(viii) له څوملیتي کارپوریشنونو څه مراد دی؟'),
      ('(ix) Write four important imports of Pakistan.', '(ix) پاکستان کی چار اہم درآمدات تحریر کیجیے۔', '(ix) د پاکستان څلور مهم واردات ولیکئ.')]


def p160():
    b = Builder()
    mcqs(b, MCQ, start=11)
    r1 = BOOK.record(b, 'eco12-papers-2', 'Board paper 2018 — objective (2)', 'بورڈ پرچہ 2018ء — معروضی (2)', 'د بورډ پرچه ۲۰۱۸ — معروضي (۲)', 160, [300])
    t = Builder()
    t.h('Subjective type, Part I', '(انشائیہ طرز) (حصہ اول)', 'تشریحي بڼه، لومړۍ برخه')
    P(t, [('2. Write short answers to any eight (8) questions:', '2۔ کوئی سے آٹھ (8) سوالات کے مختصر جوابات لکھیے:', '۲. د هرو اتو (۸) پوښتنو لنډ ځوابونه ولیکئ:')])
    L(t, Q2)
    P(t, [('3. Write short answers to any eight (8) questions:', '3۔ کوئی سے آٹھ (8) سوالات کے مختصر جوابات لکھیے:', '۳. د هرو اتو (۸) پوښتنو لنډ ځوابونه ولیکئ:')])
    L(t, Q3)
    r2 = BOOK.record(t, 'eco12-papers-3', 'Board paper 2018 — subjective part I', 'بورڈ پرچہ 2018ء — انشائیہ حصہ اول', 'د بورډ پرچه ۲۰۱۸ — تشریحي لومړۍ برخه', 160, [301])
    BOOK.save(160, [(14, r1), (14, r2)], issues=[{'id': 'eco12-pdf160', 'unit': 14, 'printedPage': 300,
               'description': 'Board paper MCQs print no answer ticks. On p.301 the right edge of Q3 numbering is cut off by the binding; numbering restored in sequence.'}])


if __name__ == '__main__':
    p160()
