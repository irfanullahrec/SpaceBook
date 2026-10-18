"""Economics XII PDF89–90: pp.158–161 — chapter 8 model paper: short questions 1–18 (with formula), long questions, MCQs i–xiii (printed ✓).
Run: python class12_eco_page089.py N (89–90)."""
import sys
from class12_eco_common import BOOK, Builder, P, L, qa, mcqs, model, eqx


def Q(qe, qu, qp, ae, au, ap):
    return (qe, qu, qp, ae, au, ap)


QA = [
 Q('1. What is meant by a semi-developed country?', '1۔ نیم ترقی یافتہ ملک سے کیا مراد ہے؟', '1. له نیمه پرمختللي هېواد څه مراد دی؟',
   'A. “A semi-developed country means such a country whose per capita income is less compared with the per capita income of developed countries, e.g. Canada, America, Britain, France and Japan, but in which those abilities and resources certainly exist by virtue of which it can progress.”', 'جواب: ”نیم ترقی یافتہ ملک سے مراد ایسا ملک ہے جس کی فی کس آمدنی ترقی یافتہ ممالک مثلاً کینیڈا، امریکہ، برطانیہ، فرانس اور جاپان کی فی کس آمدنی کے مقابلہ میں کم ہو البتہ اس میں وہ صلاحیتیں اور ذرائع ضرور موجود ہوں جن کی بدولت وہ ترقی کر سکتا ہو۔“', 'ځواب: ”له نیمه پرمختللي هېواد مراد داسې هېواد دی چې سړي سر عاید یې د پرمختللو هېوادونو، لکه کاناډا، امریکا، برتانیې، فرانسې او جاپان د سړي سر عاید په پرتله لږ وي، خو په کې هغه وړتیاوې او سرچینې خامخا وي چې د هغو په برکت پرمختګ کولی شي.“'),
 Q('2. State five basic problems of developing countries.', '2۔ ترقی پذیر ملکوں کے پانچ بنیادی مسائل بتائیں؟', '2. د پرمختیايي هېوادونو پنځه بنسټیزې ستونزې ووایاست.',
   'A. (i) low per capita income; (ii) over-population; (iii) natural resources lying idle; (iv) low efficiency; (v) shortage of capital.', 'جواب: (i) پست فی کس آمدنی (ii) افراطِ آبادی (iii) قدرتی ذرائع کے بے کار پڑے رہنا (iv) پست استعدادِ کار (v) سرمائے کی قلت', 'ځواب: (i) ټیټ سړي سر عاید؛ (ii) د نفوس زیاتوالی؛ (iii) د طبیعي سرچینو بې‌کاره پاتې کېدل؛ (iv) ټیټه کاري وړتیا؛ (v) د پانګې کمښت.'),
 Q('3. Write four factors of economic development.', '3۔ معاشی ترقی کے چار عوامل لکھیں؟', '3. د اقتصادي پرمختګ څلور عوامل ولیکئ.',
   'A. (i) human resources (labour force); (ii) natural resources (oil, gas, land and climate); (iii) capital formation (equipment etc.); (iv) technology (information of science and engineering).', 'جواب: (i) انسانی ذرائع (لیبر فورس) (ii) قدرتی ذرائع (تیل، گیس، زمین اور آب و ہوا) (iii) تشکیلِ سرمایہ (ساز و سامان وغیرہ) (iv) ٹیکنالوجی (سائنس اور انجینئرنگ کی معلومات)', 'ځواب: (i) بشري سرچینې (کاري ځواک)؛ (ii) طبیعي سرچینې (تېل، ګاز، ځمکه او اقلیم)؛ (iii) د پانګې جوړښت (وسایل او نور)؛ (iv) ټکنالوژي (د ساینس او انجنیرۍ معلومات).'),
 Q('4. Explain capital formation briefly.', '4۔ تشکیلِ سرمایہ کی مختصر تشریح کریں؟', '4. د پانګې جوړښت په لنډه توګه تشریح کړئ.',
   'A. By capital formation is meant equipment, factories, social overhead capital, i.e. roads, irrigation projects, measures for public health, and infrastructure, which are generally made at the government level.', 'جواب: تشکیلِ سرمایہ سے مراد ساز و سامان، کارخانے، معاشرتی بالائی سرمایہ یعنی سڑکیں، آبپاشی کے منصوبے، صحتِ عامہ کے لیے اقدامات، تحتی ڈھانچہ جو عموماً سرکاری سطح پر کیے جاتے ہیں۔', 'ځواب: د پانګې له جوړښت مراد وسایل، فابریکې، ټولنیزه پورتنۍ پانګه یعنې سړکونه، د اوبو لګولو پروژې، د عامې روغتیا ګامونه او زیربنا ده چې عموماً په دولتي کچه کېږي.'),
 Q('5. State the definition of economic development.', '5۔ معاشی ترقی کی تعریف بیان کریں؟', '5. د اقتصادي پرمختګ تعریف بیان کړئ.',
   'A. Professors Meier and Baldwin have defined economic development thus: “By economic development is meant such a process because of which the real national income of a country increases over a long period, and if the rate of economic development is more than the rate of population growth, then real per capita income increases.”', 'جواب: پروفیسر مائر و بالڈون نے معاشی ترقی کی تعریف یوں کی ہے: ”معاشی ترقی سے مراد ایسا عمل ہے جس کے باعث کسی ملک کی حقیقی قومی آمدنی ایک طویل عرصہ وقت میں بڑھ جائے اور اگر معاشی ترقی کی شرح، آبادی کی شرحِ افزائش سے زیادہ ہو تو فی کس حقیقی آمدنی بڑھ جاتی ہے۔“', 'ځواب: پروفېسرانو مایر او بالډوین اقتصادي پرمختګ داسې تعریف کړی: ”له اقتصادي پرمختګ مراد داسې عمل دی چې له امله یې د یوه هېواد حقیقي ملي عاید په اوږده موده کې زیات شي، او که د اقتصادي پرمختګ نرخ د نفوس د ودې له نرخ ډېر وي، نو حقیقي سړي سر عاید زیاتېږي.“'),
 Q('6. What is meant by economic planning?', '6۔ معاشی منصوبہ بندی سے کیا مراد ہے؟', '6. له اقتصادي پلان جوړونې څه مراد دی؟',
   'A. “By economic planning is meant such an arrangement of economic organisation in which different factories, business organisations and industries are conceived as mutually helpful units of one single system, so that in a fixed period, utilising all existing means and resources, the needs of people are fulfilled in the best way.”', 'جواب: ”معاشی منصوبہ بندی سے مراد معاشی تنظیم کی ایک ایسی تدبیر ہے جس میں مختلف کارخانوں کاروباری تنظیموں اور صنعتوں کو کسی ایک واحد نظام کی معاون باہم اکائیاں تصور کیا جاتا ہے تاکہ ایک معینہ مدت میں تمام موجودہ ذرائع اور وسائل سے استفادہ کر کے لوگوں کی ضروریات کو بدرجہ احسن پورا کیا جائے۔“', 'ځواب: ”له اقتصادي پلان جوړونې مراد د اقتصادي سازمان داسې تدبیر دی چې په هغه کې بېلابېلې فابریکې، سوداګریز سازمانونه او صنعتونه د یوه واحد نظام دوه اړخیز مرستندوی واحدونه ګڼل کېږي، تر څو په یوه ټاکلې موده کې له ټولو موجودو سرچینو او وسایلو ګټه پورته شي او د خلکو اړتیاوې په غوره توګه پوره شي.“'),
 Q('7. Write the methods of measuring economic development.', '7۔ معاشی ترقی کی پیمائش کے طریقے لکھیں؟', '7. د اقتصادي پرمختګ د اندازه کولو طریقې ولیکئ.',
   'A. (i) increase in national production; (ii) increase in per capita income; (iii) increase in production per labourer; (iv) increase in the rate of capital.', 'جواب: (i) قومی پیداوار میں اضافہ (ii) فی کس آمدنی میں اضافہ (iii) فی مزدور پیداوار میں اضافہ (iv) سرمائے کی شرح میں اضافہ', 'ځواب: (i) په ملي تولید کې زیاتوالی؛ (ii) په سړي سر عاید کې زیاتوالی؛ (iii) د هر کارګر په تولید کې زیاتوالی؛ (iv) د پانګې په نرخ کې زیاتوالی.'),
 Q('8. State the importance of economic planning.', '8۔ معاشی منصوبہ بندی کی اہمیت بتائیں؟', '8. د اقتصادي پلان جوړونې اهمیت ووایاست.',
   'A. Economic planning has the following importance: (i) removing the weaknesses of the private sector; (ii) removing the shortage of capital; (iii) reform of the distribution of wealth; (iv) control of luxurious consumption.', 'جواب: معاشی منصوبہ بندی کی درج ذیل اہمیت ہے: (i) نجی شعبہ کی کمزوریاں دور کرنا (ii) سرمائے کی قلت دور کرنا (iii) تقسیمِ دولت کی اصلاح (iv) تعیشانہ مصرف پر کنٹرول', 'ځواب: اقتصادي پلان جوړونه دا اهمیت لري: (i) د خصوصي برخې د کمزوریو لرې کول؛ (ii) د پانګې د کمښت لرې کول؛ (iii) د شتمنۍ د وېش سمون؛ (iv) پر عیاشي مصرف کنټرول.'),
 Q('9. Mention any two steps of the Government of Pakistan for ending poverty from the country.', '9۔ حکومتِ پاکستان کے ملک سے غربت ختم کرنے کے لیے کوئی سے دو اقدامات کا ذکر کیجیے؟', '9. له هېواده د بېوزلۍ د ختمولو لپاره د پاکستان د حکومت کوم دوه ګامونه یاد کړئ.',
   'A. The Government of Pakistan took the following two steps to end poverty from the country: (i) Benazir Income Support Programme; (ii) the system of zakat and ushr.', 'جواب: حکومتِ پاکستان نے ملک سے غربت ختم کرنے کے لیے درج ذیل دو اقدامات کیے: (i) بینظیر انکم سپورٹ پروگرام (ii) زکوٰۃ اور عشر کا نظام', 'ځواب: د پاکستان حکومت له هېواده د بېوزلۍ د ختمولو لپاره دا دوه ګامونه پورته کړل: (i) د بې‌نظیر د عاید ملاتړ پروګرام؛ (ii) د زکات او عشر نظام.'),
 Q('10. What is meant by the medium-term development plan (MTDF)?', '10۔ اوسط المیعاد ترقیاتی منصوبہ (MTDF) سے کیا مراد ہے؟', '10. له منځمهاله پراختیايي پلان (MTDF) څه مراد دی؟',
   'A. The Pakistan Planning Commission prepared a five-year plan, July 2005 to June 2010. This is a form of the strategy document for poverty reduction, which actually consists of annual plans, so that in view of changes in conditions the required amendment can be made in it. This framework is in reality part of a twenty-five-year long-term vision for 2005 to 2030.', 'جواب: پاکستان منصوبہ بندی کمیشن نے ایک پانچ سالہ منصوبہ جولائی 2005ء تا جون 2010ء تیار کیا۔ یہ حکمتِ عملی برائے تخفیفِ غربت کے دستاویز کی ایک شکل ہے جو دراصل سالانہ منصوبوں پر مشتمل ہے تاکہ حالات کے تغیرات کے پیشِ نظر اس میں مطلوبہ ترمیم کی جا سکے یہ ڈھانچہ درحقیقت پچیس سالہ ایک طویل مدتی تناظر برائے 2005ء تا 2030ء کا حصہ ہے۔', 'ځواب: د پاکستان د پلان جوړونې کمیسیون د ۲۰۰۵ له جولای تر ۲۰۱۰ جون یو پنځه کلن پلان جوړ کړ. دا د بېوزلۍ د کمولو د تګلارې د سند یوه بڼه ده چې په اصل کې له کلنیو پلانونو جوړه ده، تر څو د حالاتو د بدلونونو په پام کې نیولو سره په کې اړین تعدیل وشي. دا چوکاټ په حقیقت کې د ۲۰۰۵ تر ۲۰۳۰ لپاره د یوه پنځه ویشت کلن اوږدمهاله لید برخه ده.'),
 Q('11. Write four causes of the low per capita income in Pakistan.', '11۔ پاکستان میں فی کس آمدنی میں کمی کے چار اسباب لکھیں؟', '11. په پاکستان کې د سړي سر عاید د کمښت څلور لاملونه ولیکئ.',
   'A. (i) shortage of natural resources; (ii) increase in population; (iii) shortage of capital; (iv) unemployment.', 'جواب: (i) قدرتی ذرائع کی کمی (ii) آبادی میں اضافہ (iii) سرمائے کی قلت (iv) بیروزگاری', 'ځواب: (i) د طبیعي سرچینو کمښت؛ (ii) د نفوس زیاتوالی؛ (iii) د پانګې کمښت؛ (iv) بې‌روزګاري.'),
 Q('12. Write the formula of per capita income.', '12۔ فی کس آمدنی کا فارمولا لکھیں۔', '12. د سړي سر عاید فورمول ولیکئ.', 'A. (formula below)', 'جواب: (فارمولا نیچے)', 'ځواب: (فورمول لاندې)')]

QB = [
 Q('13. What is meant by tax culture?', '13۔ ٹیکس کلچر سے کیا مراد ہے؟', '13. له مالیاتي کلتور څه مراد دی؟',
   'A. The government has to fulfil big objectives in fiscal policy. Therefore it is necessary that such a system of taxes be established from which the government gets so much income that government expenses are met and there is no need of loans; this action is called tax culture.', 'جواب: حکومت کی مالیاتی پالیسی میں بڑے بڑے مقاصد کو پورا کرنا ہوتا ہے۔ اس لیے ضروری ہے کہ نظامِ محصولات ایسا قائم کیا جائے جس سے حکومت کو اتنی آمدنی ہو کہ سرکاری اخراجات پورے ہو سکیں اور قرضہ کی ضرورت نہ پڑے اس عمل کو ٹیکس کلچر کہا جاتا ہے۔', 'ځواب: حکومت باید په مالي پالیسۍ کې لویې موخې پوره کړي. نو اړینه ده چې داسې مالیاتي نظام جوړ شي چې حکومت ته دومره عاید ورکړي چې دولتي لګښتونه پوره شي او پور ته اړتیا پېښه نه شي؛ دې عمل ته مالیاتي کلتور ویل کېږي.'),
 Q('14. Write four methods of increasing per capita income.', '14۔ فی کس آمدنی بڑھانے کے چار طریقے تحریر کیجیے؟', '14. د سړي سر عاید د زیاتولو څلور طریقې ولیکئ.',
   'A. (i) development of agriculture; (ii) development of industry; (iii) capital formation; (iv) population planning.', 'جواب: (i) زراعت کی ترقی (ii) صنعت کی ترقی (iii) سرمائے کی تشکیل (iv) آبادی کی منصوبہ بندی', 'ځواب: (i) د کرنې پرمختګ؛ (ii) د صنعت پرمختګ؛ (iii) د پانګې جوړښت؛ (iv) د نفوس پلان جوړونه.'),
 Q('15. State four problems of the agricultural sector.', '15۔ زرعی شعبہ کے چار مسائل بیان کریں۔', '15. د کرنیزې برخې څلور ستونزې بیان کړئ.',
   'A. (a) illiterate farmers; (b) little use of fertilisers; (c) obsolete method of cultivation; (d) natural calamities.', 'جواب: (الف) ان پڑھ کسان (ب) کھادوں کا کم استعمال (ج) فرسودہ طریقہ کاشت کاری (د) قدرتی آفات', 'ځواب: (الف) بې‌سواده بزګران؛ (ب) د سرو لږه کارونه؛ (ج) د کرنې زړه طریقه؛ (د) طبیعي افتونه.'),
 Q('16. Write the solution of the problems of the agricultural sector.', '16۔ زرعی شعبہ کے مسائل کا حل لکھیں۔', '16. د کرنیزې برخې د ستونزو حل ولیکئ.',
   'A. (a) provision of loans to farmers; (b) training of farmers; (c) availability of good seeds; (d) suitable prices of agricultural commodities.', 'جواب: (الف) کسانوں کو قرض کی فراہمی (ب) کسانوں کی تربیت (ج) عمدہ بیجوں کی دستیابی (د) زرعی اجناس کی مناسب قیمتیں', 'ځواب: (الف) بزګرانو ته د پور برابرول؛ (ب) د بزګرانو روزنه؛ (ج) د ښو تخمونو موندل؛ (د) د کرنیزو توکو مناسبې بیې.'),
 Q('17. State four problems of the industrial sector.', '17۔ صنعتی شعبہ کے چار مسائل بیان کریں۔', '17. د صنعتي برخې څلور ستونزې بیان کړئ.',
   'A. (a) weak industrial inheritance; (b) shortage of trained staff; (c) non-availability of power resources; (d) shortage of raw material.', 'جواب: (الف) کمزور صنعتی وراثت (ب) تربیت یافتہ عملہ کی کمی (ج) ذرائع قوت کی عدمِ دستیابی (د) خام مال کی قلت', 'ځواب: (الف) کمزوری صنعتي میراث؛ (ب) د روزل شویو کارکوونکو کمښت؛ (ج) د ځواک د سرچینو نشتوالی؛ (د) د خامو موادو کمښت.'),
 Q('18. Write the solution of the problems of the industrial sector.', '18۔ صنعتی شعبہ کے مسائل کا حل لکھیں۔', '18. د صنعتي برخې د ستونزو حل ولیکئ.',
   'A. (a) encouragement of the private sector; (b) foreign investment; (c) concessions in taxes; (d) availability of modern machinery.', 'جواب: (الف) نجی شعبہ کی حوصلہ افزائی (ب) غیر ملکی سرمایہ کاری (ج) ٹیکسوں میں مراعات (د) جدید مشینری کی دستیابی', 'ځواب: (الف) د خصوصي برخې هڅونه؛ (ب) بهرنۍ پانګونه؛ (ج) په مالیو کې امتیازات؛ (د) د نوې ماشینرۍ موندل.')]

LONG = [('(i) State the causes of the standard of living being low in Pakistan. (Lahore Board 2009)', '(i) پاکستان میں معیارِ زندگی پست ہونے کے اسباب بیان کیجیے۔ (لاہور بورڈ 2009ء)', '(i) په پاکستان کې د ژوند د معیار د ټیټوالي لاملونه بیان کړئ. (لاهور بورډ ۲۰۰۹)'),
        ('(ii) Write the causes of the low per capita income in Pakistan. (Multan Board 2009, Lahore Board 2010)', '(ii) پاکستان میں فی کس آمدنی کی کمی کے اسباب تحریر کیجیے۔ (ملتان بورڈ 2009ء، لاہور بورڈ 2010ء)', '(ii) په پاکستان کې د سړي سر عاید د کمښت لاملونه ولیکئ. (ملتان بورډ ۲۰۰۹، لاهور بورډ ۲۰۱۰)'),
        ('(iii) Write the reasons for Pakistan’s per capita income being low. (Multan Board 2011)', '(iii) پاکستان کی فی کس آمدنی پست ہونے کی وجوہات تحریر کریں۔ (ملتان بورڈ 2011ء)', '(iii) د پاکستان د سړي سر عاید د ټیټوالي لاملونه ولیکئ. (ملتان بورډ ۲۰۱۱)'),
        ('(iv) How can an increase be made in the national income of Pakistan?', '(iv) پاکستان کی قومی آمدنی میں اضافہ کس طرح کیا جا سکتا ہے؟', '(iv) د پاکستان په ملي عاید کې څنګه زیاتوالی راتلی شي؟'),
        ('(v) Which factors are necessary for economic development?', '(v) معاشی ترقی کے لیے کون سے عوامل ضروری ہوتے ہیں؟', '(v) د اقتصادي پرمختګ لپاره کوم عوامل اړین دي؟'),
        ('(vi) State the big problems of the industrial sector of Pakistan.', '(vi) پاکستان کے صنعتی شعبہ کے بڑے بڑے مسائل بیان کیجیے۔', '(vi) د پاکستان د صنعتي برخې لویې ستونزې بیان کړئ.'),
        ('(vii) State the importance and benefits of economic planning. (Lahore Board 2009, Gujranwala Board 2009)', '(vii) معاشی منصوبہ بندی کی اہمیت اور فوائد بیان کیجیے۔ (لاہور بورڈ 2009ء، گوجرانوالہ بورڈ 2009ء)', '(vii) د اقتصادي پلان جوړونې اهمیت او ګټې بیان کړئ. (لاهور بورډ ۲۰۰۹، ګوجرانواله بورډ ۲۰۰۹)'),
        ('(viii) What are the important objectives of economic planning in Pakistan?', '(viii) پاکستان میں معاشی منصوبہ بندی کے اہم مقاصد کیا ہوتے ہیں؟', '(viii) په پاکستان کې د اقتصادي پلان جوړونې مهمې موخې کومې دي؟')]


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('Problems like national income are studied in this branch of economics:', 'قومی آمدنی جیسے مسائل کا مطالعہ معاشیات کی اس برانچ میں کیا جاتا ہے۔', 'د ملي عاید په څېر ستونزې د اقتصاد په دې څانګه کې مطالعه کېږي:'),
  [O('micro', 'جزوی', 'جزوي'), O('fiscal', 'مالیاتی', 'مالي'), O('macro', 'کلیاتی', 'کلي'), O('mathematical', 'ریاضیاتی', 'ریاضیاتي')], 2),
 (('For measuring the national income of Pakistan this method is used:', 'پاکستان کی قومی آمدنی کی پیمائش کے لیے یہ طریقہ استعمال کیا جاتا ہے۔', 'د پاکستان د ملي عاید د اندازه کولو لپاره دا طریقه کارول کېږي:'),
  [O('method of production', 'پیداوار کا طریقہ', 'د تولید طریقه'), O('method of total expenditure', 'کل خرچ کا طریقہ', 'د ټول لګښت طریقه'), O('method of the sum of incomes of factors', 'عاملین کی آمدنیوں کے مجموعہ کا طریقہ', 'د عواملو د عایداتو د مجموعې طریقه'), O('all three above', 'درج بالا تینوں', 'پورته درې واړه')], 3),
 (('Pakistan is basically such a country:', 'پاکستان بنیادی طور پر ایسا ملک ہے۔', 'پاکستان په بنسټیز ډول داسې هېواد دی:'),
  [O('industrial', 'صنعتی', 'صنعتي'), O('commercial', 'تجارتی', 'سوداګریز'), O('agricultural', 'زرعی', 'کرنیز'), O('developed', 'ترقی یافتہ', 'پرمختللی')], 2),
 (('In Pakistan’s real gross domestic product (GDP) the share of this sector is greater:', 'پاکستان کی حقیقی داخلی پیداوار (GDP) میں اس شعبہ کا حصہ زیادہ ہوتا ہے۔', 'د پاکستان په حقیقي کورني تولید (GDP) کې د دې برخې ونډه ډېره ده:'),
  [O('trade', 'تجارت', 'سوداګري'), O('agriculture', 'زراعت', 'کرنه'), O('industry', 'صنعت', 'صنعت'), O('communications', 'مواصلات', 'مخابرات')], 1),
 (('This is a cottage industry:', 'یہ گھریلو صنعت ہے۔', 'دا کورنی صنعت دی:'),
  [O('ghee industry', 'گھی کی صنعت', 'د غوړیو صنعت'), O('steel mill', 'سٹیل مل', 'د فولادو فابریکه'), O('sports goods', 'کھیلوں کا سامان', 'د لوبو سامان'), O('textile industry', 'ٹیکسٹائل انڈسٹری', 'د ټوکر صنعت')], 2),
 (('The better and comprehensive definition of economic development was presented by:', 'معاشی ترقی کی بہتر اور جامع تعریف پیش کی ہے۔', 'د اقتصادي پرمختګ ښه او جامع تعریف چا وړاندې کړی؟'),
  [O('Kindleberger', 'کنڈل برگر', 'کنډلبرګر'), O('Arthur Lewis', 'آرتھر لیوس', 'ارتر لیوس'), O('Meier and Baldwin', 'مائر اینڈ بالڈون', 'مایر او بالډوین'), O('Professor Snider', 'پروفیسر سنائیڈر', 'پروفېسر سنایډر')], 2),
 (('Of the following, one does not affect economic development:', 'درج ذیل میں سے ایک معاشی ترقی پر اثر انداز نہیں ہوتا:', 'له لاندې څخه یو پر اقتصادي پرمختګ اغېز نه کوي:'),
  [O('natural resources', 'قدرتی وسائل', 'طبیعي سرچینې'), O('language (Language)', 'زبان (Language)', 'ژبه (Language)'), O('political situation', 'سیاسی صورتِ حال', 'سیاسي حالت'), O('social evils (Social Evils)', 'سماجی برائیں (Social Evils)', 'ټولنیزې بدۍ (Social Evils)')], 1),
 (('The concept of economic development is this:', 'معاشی ترقی کا مفہوم یہ ہے۔', 'د اقتصادي پرمختګ مفهوم دا دی:'),
  [O('agricultural development', 'زرعی ترقی', 'کرنیز پرمختګ'), O('industrial development', 'صنعتی ترقی', 'صنعتي پرمختګ'), O('increase in real national income', 'حقیقی قومی آمدنی میں اضافہ', 'په حقیقي ملي عاید کې زیاتوالی'), O('increase in population', 'آبادی میں اضافہ', 'په نفوس کې زیاتوالی')], 2),
 (('This plan of Pakistan remained the most successful:', 'پاکستان کا یہ منصوبہ سب سے زیادہ کامیاب رہا۔', 'د پاکستان دا پلان تر ټولو بریالی و:'),
  [O('second plan', 'دوسرا منصوبہ', 'دویم پلان'), O('third plan', 'تیسرا منصوبہ', 'درېیم پلان'), O('fifth plan', 'پانچواں منصوبہ', 'پنځم پلان'), O('eighth plan', 'آٹھواں منصوبہ', 'اتم پلان')], 1),
 (('The period of Pakistan’s second five-year plan was:', 'پاکستان کے دوسرے پانچ سالہ منصوبے کی مدت یہ تھی۔', 'د پاکستان د دویم پنځه کلن پلان موده دا وه:'),
  [O('1950 to 1955'), O('1955 to 1960'), O('1960 to 1965'), O('1965 to 1970')], 2),
 (('This is not included in the characteristics of developing countries:', 'ترقی پذیر ممالک کی خصوصیات میں یہ شامل نہیں۔', 'دا د پرمختیايي هېوادونو په ځانګړنو کې شامل نه دی:'),
  [O('over-population', 'افراطِ آبادی', 'د نفوس زیاتوالی'), O('heavy quantity of capital', 'سرمائے کی بھاری مقدار', 'د پانګې دروند مقدار'), O('dependence on agriculture', 'زراعت پر انحصار', 'پر کرنې تکیه'), O('export of raw material', 'خام مال کی برآمد', 'د خامو موادو صادرول')], 1),
 (('In Pakistan industries were taken into national custody in:', 'پاکستان میں صنعتوں کو قومی تحویل میں لیا گیا۔', 'په پاکستان کې صنعتونه ملي تحویل ته واخیستل شول په:'),
  [O('1972'), O('1974'), O('1975'), O('1976')], 0),
 (('The period of Pakistan’s eighth five-year plan was:', 'پاکستان کے آٹھویں پانچ سالہ منصوبے کی مدت تھی۔', 'د پاکستان د اتم پنځه کلن پلان موده وه:'),
  [O('1960-65'), O('1993-98'), O('1989-94'), O('1998-2003')], 1)]


def p89():
    b = Builder()
    b.h('Model paper questions — short questions', 'ماڈل پرچہ سوالات — مختصر سوالات', 'د نمونې پرچې پوښتنې — لنډې پوښتنې')
    b.h('Subjective (Subjective), Section I (Section I)', 'انشائیہ (Subjective) حصہ اول (Section I)', 'تشریحي (Subjective)، لومړۍ برخه (Section I)')
    P(b, [('Question 1: Write short answers to the following questions:', 'سوال نمبر 1: درج ذیل سوالات کے مختصر جوابات تحریر کریں:', '۱ پوښتنه: د لاندې پوښتنو لنډ ځوابونه ولیکئ:')])
    qa(b, QA[:8])
    r1 = model(b, 8, 1, 89, 158)
    t = Builder()
    qa(t, QA[8:])
    eqx(t, r'\text{Per capita income} = \dfrac{\text{National income}}{\text{Total population}}')
    qa(t, QB[:5])
    BOOK.save(89, [(8, r1), (8, model(t, 8, 2, 89, 159))], issues=[{'id': 'eco12-pdf089', 'unit': 8, 'printedPage': 158,
               'description': 'The chapter 8 model paper (pp.158–161) follows the chapter text. The left edge of p.159 is cut off in the scan (question numbers 9–17 partly missing); numbering restored in sequence. Answer 4 “معشرتی نالائی سرمایہ” (for معاشرتی بالائی) kept as printed in substance. Formula for per capita income given as printed.'}])


def p90():
    b = Builder()
    qa(b, QB[5:])
    b.h('Section II (Section II)', 'حصہ دوم (Section II)', 'دویمه برخه (Section II)')
    P(b, [('Question 2: Write detailed answers to the following questions.', 'سوال نمبر 2: درج ذیل سوالات کے مفصل جوابات تحریر کریں۔', '۲ پوښتنه: د لاندې پوښتنو مفصل ځوابونه ولیکئ.')])
    L(b, LONG)
    b.h('Objective (Objective)', 'معروضی (Objective)', 'معروضي (Objective)')
    P(b, [('Question 3: More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال نمبر 3: ہر سوال کے ایک سے زیادہ جوابات دیئے گئے ہیں۔ ان میں سے درست جواب پر (P) کا نشان لگائیے۔', '۳ پوښتنه: د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(b, MCQ[:6])
    r1 = model(b, 8, 3, 90, 160)
    t = Builder()
    mcqs(t, MCQ[6:], start=7)
    BOOK.save(90, [(8, r1), (8, model(t, 8, 4, 90, 161))], complete_units=[8], issues=[{'id': 'eco12-pdf090', 'unit': 8, 'printedPage': 160,
               'description': 'Printed ticks kept as printed, including MCQ ix ticking the “third plan” as the most successful (the chapter text says the fifth plan was 90% successful). Q3 instruction prints “(P)” for the tick. Chapter 8 ends on p.161.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 89
    {89: p89, 90: p90}[n]()
