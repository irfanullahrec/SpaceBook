"""Economics XII PDF120: pp.220–221 — government institutions for price stability 1 (cont.)–3 (end of chapter 10 text);
chapter 10 model paper short questions 1–9. Run: python class12_eco_page120.py"""
from class12_eco_common import BOOK, Builder, rec, P, L, qa, model, eqx


def Q(qe, qu, qp, ae, au, ap):
    return (qe, qu, qp, ae, au, ap)


def p120():
    b = Builder()
    P(b, [('(continued from p.219) … keeps an eye on the prices and supply of goods, and takes measures to increase supply and also to control prices.', '(ص 219 سے جاری) … اشیاء کی قیمتوں اور رسد پر نگاہ رکھتی ہے، اور رسد بڑھانے، نیز قیمتوں کو کنٹرول کرنے کے لئے اقدامات کرتی ہے۔', '(له ۲۱۹ مخ دوام) … د توکو پر بیو او عرضې سترګې لري، او د عرضې د زیاتولو او همداسې د بیو د کنټرول لپاره ګامونه پورته کوي.')])
    L(b, [('2. Under the chairmanship of the deputy chairman of the Planning Commission a special high-level committee consisting of secretaries, for goods of kitchen need (Committee on Kitchen Items), whose new name is the “Sensitive Items Price Committee” (Sensitive Items Price Committee: SIPC), has been established, which every week reviews the prices of necessary goods, and proposes measures for immediate import to increase the supply of goods in the country and for changing the rate of duty on imports and exports.', '2۔ منصوبہ بندی کمیشن کے ڈپٹی چیئرمین کی سربراہی میں باورچی خانہ کی ضرورت کی اشیاء کے لئے سیکرٹریوں پر مشتمل ایک خصوصی اعلیٰ سطحی کمیٹی (Committee on Kitchen Items) جس کا نیا نام ”حساس اشیاء کی قیمت کمیٹی“ (Sensitive Items Price Committee: SIPC) ہے، قائم کی گئی ہے، جو ہر ہفتے ضروری اشیاء کی قیمتوں کا جائزہ لیتی ہے اور ملک میں اشیاء کی رسد بڑھانے کے لئے فوری درآمد کرنے اور درآمد و برآمد پر ڈیوٹی کی شرح میں ردوبدل کرنے کے لئے اقدامات تجویز کرتی ہے۔', '۲. د پلان جوړونې کمیسیون د مرستیال رئیس تر مشرۍ لاندې د پخلنځي د اړتیا توکو لپاره له منشیانو جوړه یوه ځانګړې لوړپوړې کمېټه (Committee on Kitchen Items)، چې نوی نوم یې ”د حساسو توکو د بیو کمېټه“ (Sensitive Items Price Committee: SIPC) دی، جوړه شوې، چې هره اوونۍ د اړینو توکو بیې ارزوي او په هېواد کې د توکو د عرضې د زیاتولو لپاره د سمدستي واردولو او پر وارداتو او صادراتو د محصول د نرخ د بدلون لپاره ګامونه وړاندیز کوي.'),
          ('3. The government has established an Expert Committee (Expert Committee), which considers the reasons for inflation and proposes measures to control it.', '3۔ حکومت نے ایک ماہرین کمیٹی (Expert Committee) قائم کی ہے جو افراطِ زر کی وجوہات پر غور کرتی ہے اور اسے کنٹرول کرنے کے لئے اقدامات تجویز کرتی ہے۔', '۳. حکومت د متخصصینو کمېټه (Expert Committee) جوړه کړې چې د انفلاسیون پر لاملونو غور کوي او د هغه د کنټرول لپاره ګامونه وړاندیز کوي.')])
    r1 = rec(b, 10, 30, 120, pages_=[220])
    t = Builder()
    t.h('Model paper questions', 'ماڈل پرچہ سوالات', 'د نمونې پرچې پوښتنې')
    t.h('Subjective (Subjective), Section I (Section I)', 'انشائیہ (Subjective) حصہ اول (Section I)', 'تشریحي (Subjective)، لومړۍ برخه (Section I)')
    P(t, [('Question 1: Write short answers to the following questions.', 'سوال نمبر 1: درج ذیل سوالات کے مختصر جوابات تحریر کریں:', '۱ پوښتنه: د لاندې پوښتنو لنډ ځوابونه ولیکئ.')])
    qa(t, [
        Q('1. Of which institutions does the banking system of Pakistan consist?', '1۔ پاکستان کا بنکاری نظام کن اداروں پر مشتمل ہے؟', '1. د پاکستان بانکي نظام له کومو ادارو جوړ دی؟',
          'A. The system of Pakistan is working banking under the State Bank of Pakistan. In it, along with other commercial banks, agricultural and industrial development banks too are included.', 'جواب: پاکستان کا نظام بینک کاری سٹیٹ بینک آف پاکستان کے تحت کام کر رہا ہے۔ اس میں دیگر تجارتی بینکوں کے ساتھ ساتھ زرعی و صنعتی ترقیاتی بینک بھی شامل ہیں۔', 'ځواب: د پاکستان بانکي نظام د پاکستان دولتي بانک تر لاندې کار کوي. په دې کې د نورو سوداګریزو بانکونو ترڅنګ کرنیز او صنعتي پراختیايي بانکونه هم شامل دي.'),
        Q('2. Which functions does the Pakistan Industrial Development Bank perform?', '2۔ پاکستان صنعتی ترقیاتی بنک کونسے فرائض سرانجام دیتا ہے؟', '2. د پاکستان صنعتي پراختیايي بانک کومې دندې ترسره کوي؟',
          'A. It gives loans to small and medium-level industries for long and medium periods; to establish new industries it can provide finance in foreign currency too.', 'جواب: یہ چھوٹی اور اوسط درجہ کی صنعتوں کو لمبی مدت اور اوسط مدت کیلئے قرضہ دیتا ہے نئی صنعتیں قائم کرنے کیلئے غیر ملکی کرنسی میں بھی مالیات فراہم کر سکتا ہے۔', 'ځواب: دا وړو او منځنیو صنعتونو ته د اوږدې او منځنۍ مودې لپاره پور ورکوي؛ د نویو صنعتونو د جوړولو لپاره په بهرنیو اسعارو کې هم مالي سرچینې برابرولی شي.'),
        Q('3. How many departments of the State Bank of Pakistan are there?', '3۔ سٹیٹ بینک آف پاکستان کے کتنے شعبے ہیں؟', '3. د پاکستان دولتي بانک څو څانګې لري؟',
          'A. The four big departments are as follows: (i) issue department; (ii) banking department; (iii) exchange policy department; (iv) research department.', 'جواب: چار بڑے شعبے درج ذیل ہیں۔ (i) شعبہ اجراء (ii) شعبہ بنکاری (iii) شعبہ ایکس چینج پالیسی (iv) شعبہ تحقیق', 'ځواب: څلور لویې څانګې په لاندې ډول دي: (i) د صادرولو څانګه؛ (ii) د بانکدارۍ څانګه؛ (iii) د تبادلې د پالیسۍ څانګه؛ (iv) د څېړنې څانګه.'),
        Q('4. State the kinds of inflation.', '4۔ افراطِ زر کی اقسام بتائیے۔', '4. د انفلاسیون ډولونه ووایاست.',
          'A. Inflation can be of two kinds, e.g. (i) demand-pulled inflation; (ii) cost-pushed inflation.', 'جواب: افراطِ زر کی دو اقسام ہو سکتی ہیں مثلاً (i) طلب کشیدہ افراطِ زر (ii) لاگت فشار افراطِ زر', 'ځواب: انفلاسیون دوه ډوله کېدای شي، لکه (i) د غوښتنې کش شوی انفلاسیون؛ (ii) د لګښت فشار انفلاسیون.'),
        Q('5. What is the formula for finding out the rate of inflation?', '5۔ افراطِ زر کی شرح معلوم کرنے کا فارمولا کیا ہے؟', '5. د انفلاسیون د نرخ د معلومولو فورمول څه دی؟',
          'A. (formula below)', 'جواب: (فارمولا ذیل میں)', 'ځواب: (فورمول لاندې)')])
    eqx(t, r'\text{Inflation in 2015} = \dfrac{\text{CPI in 2015} - \text{CPI in 2014}}{\text{CPI in 2014}} \times 100')
    P(t, [('In words: inflation in 2015 = (index of consumer prices in 2015 − index of prices in 2014) ÷ index of consumer prices in 2014 × 100.', '2015ء میں افراطِ زر = (2015ء میں صارفین کی قیمتوں کا اشاریہ − 2014ء میں قیمتوں کا اشاریہ) ÷ 2014ء میں صارفین کی قیمتوں کا اشاریہ × 100', 'په ټکو کې: په ۲۰۱۵ کې انفلاسیون = (په ۲۰۱۵ کې د مصرفوونکو د بیو شاخص − په ۲۰۱۴ کې د بیو شاخص) ÷ په ۲۰۱۴ کې د مصرفوونکو د بیو شاخص × ۱۰۰.')])
    qa(t, [
        Q('6. Define inflation.', '6۔ افراطِ زر کی تعریف کریں؟', '6. انفلاسیون تعریف کړئ.',
          'A. When aggregate demand is more than aggregate supply, then a tendency of increase in prices is found, which is called inflation.', 'جواب: جب مجموعی طلب مجموعی رسد سے زیادہ ہو تو قیمتوں میں اضافے کا رجحان پایا جاتا ہے جسے افراطِ زر کہا جاتا ہے۔', 'ځواب: کله چې ټوله غوښتنه له ټولې عرضې زیاته وي، نو په بیو کې د زیاتوالي تمایل موندل کېږي چې انفلاسیون بلل کېږي.'),
        Q('7. What is meant by the money market?', '7۔ بازارِ زر سے کیا مراد ہے؟', '7. له پیسو بازار څه مراد دی؟',
          'A. By the money market are meant such financial institutions as do the work of buying and selling commercial papers, e.g. (i) commercial bills; (ii) bills of the government treasury; (iii) guarantees; (iv) shares of joint-stock companies.', 'جواب: بازارِ زر سے مراد ایسے مالی ادارے ہیں جو تجارتی کاغذات کی خرید و فروخت کا کام کرتے ہیں۔ مثلاً (i) تجارتی ہنڈیاں (ii) سرکاری خزانے کی ہنڈیاں (iii) کفالتیں (iv) مشترکہ سرمایہ کی کمپنیوں کے حصص', 'ځواب: له پیسو بازار مراد داسې مالي ادارې دي چې د سوداګریزو کاغذونو د پېر و پلور کار کوي، لکه (i) سوداګریزې هنډۍ؛ (ii) د دولتي خزانې هنډۍ؛ (iii) تضمینونه؛ (iv) د ګډې پانګې شرکتونو ونډې.'),
        Q('8. What is meant by devaluation of money?', '8۔ تخفیفِ قدرِ زر سے کیا مراد ہے؟', '8. د پیسو له ارزښت کمولو څه مراد دی؟',
          'A. When the government, to increase exports and reduce imports, reduces the external value of the currency, then it is given the name of devaluation of money.', 'جواب: جب حکومت برآمدات کو بڑھانے اور درآمدات کو کم کرنے کے لیے کرنسی کی بیرونی قدر میں کمی کر دے تو اسے تخفیفِ قدرِ زر کا نام دیا جاتا ہے۔', 'ځواب: کله چې حکومت د صادراتو د زیاتولو او وارداتو د کمولو لپاره د اسعارو بهرنی ارزښت کم کړي، نو دې ته د پیسو د ارزښت کمول ویل کېږي.')])
    P(t, [('9. When was the State Bank of Pakistan established and where is its head office? (answer continued on p.222)', '9۔ سٹیٹ بینک آف پاکستان کب قائم ہوا اور اس کا مرکزی دفتر کہاں ہے؟ (جواب ص 222 پر)', '9. د پاکستان دولتي بانک کله جوړ شو او مرکزي دفتر یې چېرې دی؟ (ځواب په ۲۲۲ مخ)')])
    BOOK.save(120, [(10, r1), (10, model(t, 10, 1, 120, 221))], issues=[{'id': 'eco12-pdf120', 'unit': 10, 'printedPage': 220,
               'description': 'Chapter 10 text ends on p.220 (rest of page blank). Model paper answer 1 printed “پاکستان کا نظام بینک کاری … کام کر رہا ہے” kept; answer 5 formula uses 2015/2014 (the chapter used 2012/2011) — kept as printed.'}])


if __name__ == '__main__':
    p120()
