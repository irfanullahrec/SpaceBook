"""PDF120 printed 231–232: Unit 7 opener (learning outcomes); 7.1 introduction, 7.1.1 hypothesis testing, 7.1.2 six steps."""
from class12_statistics_common import Builder, save

o = Builder()
o.h('Unit - 7', 'یونٹ - 7', 'واحد - 7')
o.h('Hypothesis Testing', 'مفروضے کی جانچ', 'د فرضیې ازموینه')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Describe statistical hypothesis and hypothesis testing.', 'شماریاتی مفروضہ اور مفروضے کی جانچ بیان کریں۔', 'احصاییوي فرضیه او د فرضیې ازموینه بیان کړي.'),
    ('Differentiate between null and alternative hypothesis, simple and composite hypothesis.', 'صفری اور متبادل مفروضے، سادہ اور مرکب مفروضے میں فرق کریں۔', 'د صفري او بدیل فرضیې، ساده او مرکبې فرضیې ترمنځ توپیر وکړي.'),
    ('Formulate null and alternative hypothesis.', 'صفری اور متبادل مفروضہ وضع کریں۔', 'صفري او بدیله فرضیه جوړه کړي.'),
    ('Recognize the elements involved in hypothesis testing: test statistic, rejection and non-rejection regions, critical values, one tailed test, two tailed test, type-I and type-II errors, level of significance, decision rule and conclusion.', 'مفروضے کی جانچ میں شامل عناصر پہچانیں: جانچ کا شماریہ، رد اور عدم رد کے علاقے، فیصلہ کن قیمتیں، یک طرفہ جانچ، دو طرفہ جانچ، پہلی قسم اور دوسری قسم کی غلطیاں، معنویت کی سطح، فیصلے کا قاعدہ اور نتیجہ۔', 'د فرضیې په ازموینه کې شامل عناصر وپېژني: د ازموینې احصاییه، د ردولو او نه ردولو سیمې، بحراني قیمتونه، یو لوري ازموینه، دوه لوري ازموینه، لومړی ډول او دویم ډول تېروتنې، د معنی‌داریت کچه، د پرېکړې قاعده او پایله.'),
    ('Apply the test of hypothesis about mean of a normal population (known and unknown standard deviation)', 'نارمل آبادی کے اوسط کے بارے میں مفروضے کی جانچ کا اطلاق کریں (معلوم اور نامعلوم معیاری انحراف)', 'د نورمال نفوس د منځني په اړه د فرضیې ازموینه وکاروي (معلوم او نامعلوم معیاري انحراف)'),
    ('Apply the test of hypothesis about population proportion (large sample).', 'آبادی کے تناسب کے بارے میں مفروضے کی جانچ کا اطلاق کریں (بڑا نمونہ)۔', 'د نفوس د تناسب په اړه د فرضیې ازموینه وکاروي (لویه نمونه).'),
    ('Apply the test of hypothesis about the difference between means of two normal populations (known/unknown standard deviations).', 'دو نارمل آبادیوں کے اوسطوں کے فرق کے بارے میں مفروضے کی جانچ کا اطلاق کریں (معلوم/نامعلوم معیاری انحراف)۔', 'د دوو نورمال نفوسونو د منځنیو د توپیر په اړه د فرضیې ازموینه وکاروي (معلوم/نامعلوم معیاري انحرافونه).'),
    ('Apply the test of hypothesis about the difference between proportions of two populations (large samples).', 'دو آبادیوں کے تناسبوں کے فرق کے بارے میں مفروضے کی جانچ کا اطلاق کریں (بڑے نمونے)۔', 'د دوو نفوسونو د تناسبونو د توپیر په اړه د فرضیې ازموینه وکاروي (لویې نمونې).'),
])
opening = o.build('stat12-u7-opening', 'Unit 7 — Learning outcomes', 'یونٹ 7 — حاصلاتِ تعلم', 'واحد 7 — د زده کړې پایلې', 120, [231])

b = Builder()
b.h('7.1 Introduction', '7.1 تعارف', '7.1 پېژندنه')
b.p('The second important phase of statistical inference is the hypothesis testing. Here decisions are made about the population parameters on the basis of sample information. For example, hypothesis testing procedure can decide whether (i) a new medicine is really effective in curing a particular disease (ii) one educational procedure is better than other etc. The difference between estimation and hypothesis testing is that in estimation parameter values are unknown and are obtained from sample information while in hypothesis testing parameters values are hypothesized and are checked on the basis of sample information whether they are true or false.',
    'شماریاتی استنباط کا دوسرا اہم مرحلہ مفروضے کی جانچ ہے۔ یہاں نمونے کی معلومات کی بنیاد پر آبادی کے پیرامیٹرز کے بارے میں فیصلے کیے جاتے ہیں۔ مثلاً مفروضے کی جانچ کا طریقہ فیصلہ کر سکتا ہے کہ (i) کوئی نئی دوا کسی خاص بیماری کے علاج میں واقعی مؤثر ہے (ii) ایک تعلیمی طریقہ دوسرے سے بہتر ہے وغیرہ۔ تخمین اور مفروضے کی جانچ میں فرق یہ ہے کہ تخمین میں پیرامیٹر کی قیمتیں نامعلوم ہوتی ہیں اور نمونے کی معلومات سے حاصل کی جاتی ہیں جبکہ مفروضے کی جانچ میں پیرامیٹرز کی قیمتیں فرض کی جاتی ہیں اور نمونے کی معلومات کی بنیاد پر جانچا جاتا ہے کہ آیا وہ درست ہیں یا غلط۔',
    'د احصاییوي استنتاج دویم مهم پړاو د فرضیې ازموینه ده. دلته د نمونوي معلوماتو پر بنسټ د نفوس د پارامټرونو په اړه پرېکړې کېږي. د بېلګې په توګه د فرضیې د ازموینې طریقه پرېکړه کولای شي چې (i) یو نوی درمل د یوې ځانګړې ناروغۍ په درملنه کې په رښتیا اغېزمن دی (ii) یوه تعلیمي طریقه له بلې ښه ده او نور. د اټکل او د فرضیې د ازموینې ترمنځ توپیر دا دی چې په اټکل کې د پارامټر قیمتونه نامعلوم وي او له نمونوي معلوماتو ترلاسه کېږي، په داسې حال کې چې د فرضیې په ازموینه کې د پارامټرونو قیمتونه فرض کېږي او د نمونوي معلوماتو پر بنسټ ازمویل کېږي چې سم دي که ناسم.')
b.p('Hypothesis is an unproved claim or assertion or assumption which acts as a starting point in a research irrespective of its probable truthfulness or falsity. Hypothesis may be non-statistical or statistical. A statistical hypothesis is a testable claim about one or more parameters of empirical distributions.',
    'مفروضہ ایک غیر ثابت شدہ دعویٰ یا بیان یا مفروضہ ہے جو تحقیق میں نقطۂ آغاز کا کام دیتا ہے، چاہے اس کے درست یا غلط ہونے کا امکان کچھ بھی ہو۔ مفروضہ غیر شماریاتی یا شماریاتی ہو سکتا ہے۔ شماریاتی مفروضہ تجرباتی تقسیموں کے ایک یا زیادہ پیرامیٹرز کے بارے میں قابلِ جانچ دعویٰ ہے۔',
    'فرضیه یوه نه ثابته شوې ادعا یا بیان یا انګېرنه ده چې په څېړنه کې د پیل ټکي په توګه کار کوي، پرته له دې چې د هغې د سموالي یا ناسموالي احتمال څه وي. فرضیه کېدای شي غیر احصاییوي یا احصاییوي وي. احصاییوي فرضیه د تجربي وېشونو د یوه یا ډېرو پارامټرونو په اړه د ازموینې وړ ادعا ده.')
b.h('7.1.1 Hypothesis testing', '7.1.1 مفروضے کی جانچ', '7.1.1 د فرضیې ازموینه')
b.p('A statistical method that uses sample data to accept or reject a hypothesis about a parameter is called hypothesis testing.', 'وہ شماریاتی طریقہ جو کسی پیرامیٹر کے بارے میں مفروضے کو قبول یا رد کرنے کے لیے نمونے کا مواد استعمال کرے، مفروضے کی جانچ کہلاتا ہے۔', 'هغه احصاییوي طریقه چې د یوه پارامټر په اړه د فرضیې د منلو یا ردولو لپاره نمونوي معلومات کاروي، د فرضیې ازموینه بلل کېږي.')
b.h('7.1.2 Principle steps involved in hypothesis testing', '7.1.2 مفروضے کی جانچ کے بنیادی مراحل', '7.1.2 د فرضیې په ازموینه کې اصلي پړاوونه')
b.p('Hypothesis testing procedure mainly involves the following six steps:', 'مفروضے کی جانچ کا طریقہ بنیادی طور پر درج ذیل چھ مراحل پر مشتمل ہے:', 'د فرضیې د ازموینې طریقه په اصل کې لاندې شپږ پړاوونه لري:')
b.group('lines', [
    ('Step i. State the null and alternative hypothesis.', 'مرحلہ i. صفری اور متبادل مفروضہ بیان کریں۔', 'پړاو i. صفري او بدیله فرضیه بیان کړئ.'),
    ('Step ii. Choose an appropriate level of significance.', 'مرحلہ ii. معنویت کی مناسب سطح منتخب کریں۔', 'پړاو ii. د معنی‌داریت مناسبه کچه وټاکئ.'),
    ('Step iii. Decide about test statistic.', 'مرحلہ iii. جانچ کے شماریے کا فیصلہ کریں۔', 'پړاو iii. د ازموینې د احصاییې په اړه پرېکړه وکړئ.'),
    ('Step iv. Compute test statistic value.', 'مرحلہ iv. جانچ کے شماریے کی قیمت معلوم کریں۔', 'پړاو iv. د ازموینې د احصاییې قیمت محاسبه کړئ.'),
    ('Step v. Obtain critical values for test statistic from respective tables.', 'مرحلہ v. متعلقہ جداول سے جانچ کے شماریے کی فیصلہ کن قیمتیں حاصل کریں۔', 'پړاو v. له اړوندو جدولونو څخه د ازموینې د احصاییې بحراني قیمتونه ترلاسه کړئ.'),
    ('Step vi. Make a decision.', 'مرحلہ vi. فیصلہ کریں۔', 'پړاو vi. پرېکړه وکړئ.'),
])
rec = b.build('stat12-p120-hypothesis-intro', '7.1 Introduction to hypothesis testing — six steps', '7.1 مفروضے کی جانچ کا تعارف — چھ مراحل', '7.1 د فرضیې د ازموینې پېژندنه — شپږ پړاوونه', 120, [232])

if __name__ == '__main__':
    save(120, [(7, opening), (7, rec)])
