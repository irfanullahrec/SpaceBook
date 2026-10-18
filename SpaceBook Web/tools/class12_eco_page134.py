"""Economics XII PDF134: pp.248–249 — chapter 11 MCQs 4–16 (printed ✓); chapter 12 Foreign Trade of Pakistan: importance 1–4,
major exports 1 (begins). Run: python class12_eco_page134.py"""
from class12_eco_common import BOOK, Builder, rec, P, mcqs, model


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('Zakat is obligatory on which of the following?', 'زکوٰۃ مندرجہ ذیل میں سے کس پر واجب ہوتی ہے۔', 'زکات په لاندې کې پر کوم واجب دی؟'),
  [O('agricultural produce', 'زرعی پیداوار', 'کرنیز تولید'), O('savings', 'بچتیں', 'سپما'), O('residential house', 'رہائشی مکان', 'د استوګنې کور'), O('imports', 'درآمدات', 'واردات')], 1),
 (('How many kinds of recipients of zakat are there?', 'زکوٰۃ کے مستحقین کی کتنی اقسام ہیں۔', 'د زکات مستحقین څو ډوله دي؟'),
  [O('five', 'پانچ', 'پنځه'), O('seven', 'سات', 'اووه'), O('eight', 'آٹھ', 'اته'), O('ten', 'دس', 'لس')], 2),
 (('The rate of zakat is:', 'زکوٰۃ کی شرح ہے۔', 'د زکات نرخ دی:'),
  [O('two per cent', 'دو فیصد', 'دوه سلنه'), O('two and a half per cent', 'اڑھائی فیصد', 'دوه نیمه سلنه'), O('four and a half per cent', 'ساڑھے چار فیصد', 'څلور نیمه سلنه'), O('five per cent', 'پانچ فیصد', 'پنځه سلنه')], 1),
 (('Zakat is:', 'زکوٰۃ ہے۔', 'زکات دی:'),
  [O('financial worship', 'مالی عبادت', 'مالي عبادت'), O('pillar of Islam', 'اسلام کا رکن', 'د اسلام رکن'), O('rate of tax', 'ٹیکس کی شرح', 'د مالیې نرخ'), O('A and B', 'الف اور ب', 'الف او ب')], 3),
 (('These are included in the sources of income of the central government of Pakistan:', 'پاکستان کی مرکزی حکومت کے ذرائع آمدنی میں یہ شامل ہیں', 'د پاکستان د مرکزي حکومت د عاید په سرچینو کې دا شامل دي:'),
  [O('customs', 'کسٹمز', 'ګمرکونه'), O('property tax', 'پراپرٹی ٹیکس', 'د ملکیت مالیه'), O('land revenue', 'مالیہ زمین', 'د ځمکې مالیه'), O('water rate', 'آبیانہ', 'د اوبو محصول')], 0),
 (('In Pakistan the federal budget is presented in parliament by:', 'پاکستان میں وفاقی بجٹ پارلیمنٹ میں پیش کرتا ہے', 'په پاکستان کې فدرالي بودجه پارلمان ته وړاندې کوي:'),
  [O('the President', 'صدرِ مملکت', 'ولسمشر'), O('the federal commerce minister', 'وفاقی وزیرِ تجارت', 'فدرالي سوداګرۍ وزیر'), O('the finance minister', 'وزیرِ خزانہ', 'د مالیې وزیر'), O('the Prime Minister', 'وزیرِ اعظم', 'لومړی وزیر')], 2),
 (('The Government of Pakistan increases its financial resources thus:', 'حکومتِ پاکستان اپنے مالی وسائل یوں بڑھاتی ہے۔', 'د پاکستان حکومت خپلې مالي سرچینې داسې زیاتوي:'),
  [O('by printing notes', 'نوٹ چھاپ کر', 'د نوټونو په چاپولو'), O('by increasing tax on people', 'لوگوں پر ٹیکس بڑھا کر', 'پر خلکو د مالیې په زیاتولو'), O('by taking loans', 'قرض لے کر', 'د پور په اخیستو'), O('by all three of these', 'ان تینوں سے', 'په دې ټولو درېیو')], 3),
 (('The greater part of the budget of the Government of Pakistan is spent on this:', 'حکومتِ پاکستان کے بجٹ کا زیادہ حصہ اس پر خرچ ہوتا ہے۔', 'د پاکستان د حکومت د بودجې ډېره برخه پر دې لګېږي:'),
  [O('education', 'تعلیم', 'زده‌کړه'), O('health', 'صحت', 'روغتیا'), O('defence', 'دفاع', 'دفاع'), O('payment of loans', 'قرضوں کی ادائیگی', 'د پورونو ورکړه')], 2),
 (('The rate of zakat is:', 'زکوٰۃ کی شرح ہے۔', 'د زکات نرخ دی:'),
  [O('proportional', 'متناسب', 'متناسب'), O('fixed', 'معینہ', 'ټاکلی'), O('regressive', 'تنزلی', 'کمېدونکی'), O('none of these', 'ان میں سے کوئی نہیں', 'له دې هېڅ یو')], 1),
 (('Which is not a source of income of the central government?', 'کونسا مرکزی حکومت کا ذریعہ آمدنی نہیں ہے۔', 'کومه د مرکزي حکومت د عاید سرچینه نه ده؟'),
  [O('water rate', 'آبیانہ', 'د اوبو محصول'), O('income tax', 'آمدنی ٹیکس', 'د عاید مالیه'), O('tariff', 'ٹیرف', 'تعرفه'), O('wealth tax', 'دولت ٹیکس', 'د شتمنۍ مالیه')], 0),
 (('Which tax is a direct tax?', 'کونسا ٹیکس براہِ راست ٹیکس ہے۔', 'کومه مالیه مستقیمه مالیه ده؟'),
  [O('sales tax', 'سیلز ٹیکس', 'د پلور مالیه'), O('import tax', 'درآمدی ٹیکس', 'وارداتي مالیه'), O('export tax', 'برآمدی ٹیکس', 'صادراتي مالیه'), O('none of these', 'ان میں سے کوئی نہیں', 'له دې هېڅ یوه')], 3),
 (('In the light of which principle does every person pay tax according to his ability?', 'کس اصول کی روشنی میں ہر شخص اپنی اہلیت کے مطابق ٹیکس ادا کرتا ہے۔', 'د کوم اصل په رڼا کې هر کس د خپل توان سره سم مالیه ورکوي؟'),
  [O('principle of convenience', 'اصولِ سہولت', 'د اسانتیا اصل'), O('principle of elasticity', 'اصولِ لچکداری', 'د نرمښت اصل'), O('principle of equality', 'اصولِ مساوات', 'د برابرۍ اصل'), O('principle of diversity', 'اصولِ تنوع', 'د تنوع اصل')], 2),
 (('In which is the characteristic of keeping one’s income hidden not found?', 'اپنی آمدنی کو پوشیدہ رکھنے کے خصوصیت کس میں نہیں پائی جاتی۔', 'د خپل عاید د پټ ساتلو ځانګړتیا په کوم کې نه موندل کېږي؟'),
  [O('private finance', 'نجی مالیات', 'خصوصي مالیه'), O('public finance', 'سرکاری مالیات', 'دولتي مالیه'), O('business finance', 'کاروباری مالیات', 'سوداګریزه مالیه'), O('private savings', 'نجی بچتیں', 'خصوصي سپما')], 1)]


def p134():
    b = Builder()
    mcqs(b, MCQ, start=4)
    r1 = model(b, 11, 4, 134, 248)
    t = Builder()
    t.h('Chapter 12 — Foreign Trade of Pakistan (Foreign Trade of Pakistan)', 'باب 12 — پاکستان کی بیرونی تجارت (Foreign Trade of Pakistan)', '۱۲ څپرکی — د پاکستان بهرنۍ سوداګري (Foreign Trade of Pakistan)')
    t.h('Importance of foreign trade', 'بیرونی تجارت کی اہمیت:', 'د بهرنۍ سوداګرۍ اهمیت')
    P(t, [('In our economy foreign trade has great importance, as becomes known from the following things:', 'ہماری معیشت میں بیرونی تجارت کو بڑی اہمیت حاصل ہے، جیسا کہ درج ذیل باتوں سے معلوم ہوتا ہے:', 'زموږ په اقتصاد کې بهرنۍ سوداګري ډېر اهمیت لري، لکه څنګه چې له لاندې خبرو معلومېږي:')])
    t.h('1. Important part of domestic production', '1۔ داخلی پیداوار کا اہم حصہ:', '۱. د کورني تولید مهمه برخه')
    P(t, [('The value of the exports and imports of Pakistan is an important part of the gross domestic product (G.D.P) of Pakistan, because goods equal to approximately the eleventh part of GDP are exported.', 'پاکستان کی برآمدات و درآمدات کی مالیت پاکستان کی خام داخلی پیداوار (G.D.P) کا اہم حصہ ہوتی ہے۔ کیونکہ جی۔ ڈی۔ پی کے تقریباً گیارہویں حصہ کے برابر اشیاء برآمد کر دی جاتی ہیں۔', 'د پاکستان د صادراتو او وارداتو ارزښت د پاکستان د ناخالص کورني تولید (G.D.P) مهمه برخه وي، ځکه د GDP د نږدې یوولسمې برخې برابر توکي صادرېږي.')])
    t.h('2. Dependence of industrial development', '2۔ صنعتی ترقی کا دارومدار:', '۲. د صنعتي پرمختګ تکیه')
    P(t, [('The industrial development of Pakistan depends on this, that by exporting as many goods as possible sufficient foreign exchange be earned, and with it machines, raw material, spare parts, chemical goods, mineral oil, petrol, fuel and other development equipment be imported, so that national industry can develop.', 'پاکستان کی صنعتی ترقی کا دارومدار اس بات پر ہے کہ زیادہ سے زیادہ اشیاء برآمد کر کے کافی زرِ مبادلہ کمایا جائے اور اس سے مشینیں، خام مال، فاضل پرزے، کیمیاوی اشیاء، معدنی تیل، پٹرول، ایندھن اور دیگر ترقیاتی ساز و سامان درآمد کیا جائے تاکہ ملکی صنعت ترقی کر سکے۔', 'د پاکستان صنعتي پرمختګ په دې پورې اړه لري چې د ډېرو توکو په صادرولو کافي بهرني اسعار وګټل شي او په هغو ماشینونه، خام مواد، اضافي پرزې، کیمیاوي توکي، کاني تېل، پټرول، سون او نور پراختیايي سامان وارد شي، تر څو هېوادنی صنعت پرمختګ وکړي.')])
    t.h('3. External loans', '3۔ بیرونی قرضہ:', '۳. بهرنی پور')
    P(t, [('Pakistan has taken much loan from abroad to complete economic schemes and development projects; for its return and the payment of interest it is necessary that, by increasing exports, foreign exchange be earned. This loan has been taken from the Consortium (Consortium) (i.e. partner countries). In it these countries and institutions are included: Japan, America, Germany, France, Canada, Italy, World Bank and International Development Agency etc. Besides them Pakistan has also taken loans from Islamic countries, in which these are included: Abu Dhabi, Kuwait, Saudi Arabia and the Islamic Development Bank etc.', 'پاکستان نے معاشی سکیموں اور ترقیاتی پروجیکٹوں کو مکمل کرنے کے لیے بیرونِ ملک سے بہت سا قرضہ لے رکھا ہے، اس کی واپسی اور سود کی ادائیگی کے لئے ضروری ہے کہ برآمدات بڑھا کر زرِ مبادلہ کمایا جائے۔ یہ قرضہ کنسورشیم (Consortium) (یعنی شریکہ ممالک) سے لیا گیا ہے۔ ان میں یہ ممالک اور ادارے شامل ہیں: جاپان، امریکہ، جرمنی، فرانس، کینیڈا، اٹلی، عالمی بنک اور بین الاقوامی ترقیاتی ایجنسی وغیرہ۔ ان کے علاوہ پاکستان نے اسلامی ملکوں سے بھی قرضہ لیا ہے۔ جن میں یہ شامل ہیں: ابوظہبی، کویت، سعودی عرب اور اسلامی ترقیاتی بنک وغیرہ۔', 'پاکستان د اقتصادي طرحو او پراختیايي پروژو د بشپړولو لپاره له بهره ډېر پور اخیستی؛ د هغه د بېرته ورکړې او د سود د ورکړې لپاره اړینه ده چې د صادراتو په زیاتولو بهرني اسعار وګټل شي. دا پور له کنسورشیم (Consortium) (یعنې شریکو هېوادونو) اخیستل شوی. په دې کې دا هېوادونه او ادارې شاملې دي: جاپان، امریکا، جرمني، فرانسه، کاناډا، ایټالیا، نړیوال بانک او نړیواله پراختیايي اداره او نور. سربېره پر دې پاکستان له اسلامي هېوادونو هم پور اخیستی، چې په کې دا شامل دي: ابوظبي، کویټ، سعودي عربستان او اسلامي پراختیايي بانک او نور.')])
    t.h('4. Problem of return of loan and interest', '4۔ قرضہ اور سود کی واپسی کا مسئلہ:', '۴. د پور او سود د بېرته ورکړې ستونزه')
    P(t, [('The imports of Pakistan are more than its exports; therefore a continuous deficit has been running in the balance of payments. Further, for development purposes it has taken much loan from foreign countries, because of which an increase has kept occurring in the annual amount of interest. Therefore there is need that exports be increased as much as possible, so that the burden of loan and interest on the country can be reduced.', 'پاکستان کی درآمدات اس کی برآمدات سے زیادہ ہوتی ہیں، اس لئے ادائیگیوں کے توازن میں مسلسل خسارہ چلا آ رہا ہے۔ نیز ترقیاتی مقاصد کے لئے اس نے غیر ممالک سے بہتر قرضہ لے رکھا ہے جس کے باعث سالانہ سود کی رقم میں اضافہ ہوتا چلا گیا ہے۔ لہٰذا ضرورت اس امر کی ہے کہ برآمدات کو زیادہ سے زیادہ بڑھایا جائے، تاکہ ملک پر قرضہ اور سود کا بوجھ کم کیا جا سکے۔', 'د پاکستان واردات له صادراتو زیات وي، نو د تادیاتو په توازن کې پرله‌پسې کسر روان دی. همداسې یې د پراختیايي موخو لپاره له بهرنیو هېوادونو ډېر پور اخیستی، چې له امله یې د کلني سود په اندازه کې زیاتوالی راغلی. نو اړتیا ده چې صادرات تر ډېره ډېر زیات شي، تر څو پر هېواد د پور او سود بار کم شي.')])
    t.h('Major exports of Pakistan (Major Exports of Pakistan)', 'پاکستان کی اہم برآمدات (Major Exports of Pakistan):', 'د پاکستان مهم صادرات (Major Exports of Pakistan)')
    P(t, [('Here we take a separate review of the exports of Pakistan:', 'یہاں ہم پاکستان کی برآمدات کا الگ الگ جائزہ لیتے ہیں:', 'دلته د پاکستان د صادراتو جلا جلا ارزونه کوو:')])
    t.h('1. Cotton thread (Cotton Yarn)', '1۔ سوتی دھاگہ (Cotton Yarn):', '۱. د پنبې تار (Cotton Yarn)')
    P(t, [('Among the exports of Pakistan the thing earning very much foreign exchange is cotton thread (cotton yarn). In 1970-71 yarn worth only 34 crore rupees was exported, whereas in the first nine months of 2009-10, 121 crore dollars’ worth.', 'پاکستان کی برآمدات میں بہت زیادہ زرِ مبادلہ کمانے والی شے سوتی دھاگہ (کاٹن یارن) ہے۔ 1970-71ء میں صرف 34 کروڑ روپے کا یارن برآمد ہوا تھا جب کہ 2009-10ء کی پہلی نوماہی میں 121 کروڑ ڈالر کا۔', 'د پاکستان په صادراتو کې تر ټولو ډېر بهرني اسعار ګټونکی شی د پنبې تار (کاټن یارن) دی. په ۱۹۷۰-۷۱ کې یوازې د ۳۴ کروړو روپیو تار صادر شوی و، حال دا چې د ۲۰۰۹-۱۰ په لومړیو نهو میاشتو کې د ۱۲۱ کروړو ډالرو.')])
    BOOK.save(134, [(11, r1), (12, rec(t, 12, 1, 134, pages_=[249], first=True))], complete_units=[11], issues=[{'id': 'eco12-pdf134', 'unit': 11, 'printedPage': 248,
               'description': 'Printed ticks kept as printed: MCQ 12 ticks zakat rate as “fixed”; MCQ 13 ticks water rate as not a central source; MCQ 14 ticks “none of these” as a direct tax. Chapter 11 ends on p.248; chapter 12 begins on p.249. Printed “بہتر قرضہ” (for بہت سا) kept.'}])


if __name__ == '__main__':
    p134()
