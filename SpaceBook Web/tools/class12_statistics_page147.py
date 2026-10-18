"""PDF147 printed 285–286: Unit 8 key points; Exercise 8.1 (T/F) and 8.2 (blanks)."""
from class12_statistics_common import Builder, save

B = '______'
QF = r'Q=\frac{(AB)(\alpha\beta)-(A\beta)(\alpha B)}{(AB)(\alpha\beta)+(A\beta)(\alpha B)}'
k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.p('Descriptive or qualitative characteristics are called attributes.', 'بیانیہ یا کیفیتی خصوصیات صفات کہلاتی ہیں۔', 'تشریحي یا کیفي ځانګړنې صفتونه بلل کېږي.')
k.group('list', [
    ('For the sake of convenience capital English letters A, B, C… are used to denote presence of attributes and the Greek letters α, β, γ… denote the absence of these attributes respectively.', 'سہولت کے لیے انگریزی کے بڑے حروف A، B، C… صفات کی موجودگی اور یونانی حروف α، β، γ… بالترتیب ان صفات کی غیر موجودگی ظاہر کرتے ہیں۔', 'د اسانتیا لپاره د انګلیسي لوی توري A، B، C… د صفتونو شتون او یوناني توري α، β، γ… په ترتیب سره د دې صفتونو نشتوالی ښيي.'),
    ('The classes A, B, AB are called positive classes because they contain the presence of attributes.', 'جماعتیں A، B، AB مثبت جماعتیں کہلاتی ہیں کیونکہ ان میں صفات کی موجودگی ہوتی ہے۔', 'ټولګي A، B، AB مثبت ټولګي بلل کېږي ځکه چې د صفتونو شتون لري.'),
    ('The classes α, β, αβ are called negative classes because they contain absence of the attributes.', 'جماعتیں α، β، αβ منفی جماعتیں کہلاتی ہیں کیونکہ ان میں صفات کی غیر موجودگی ہوتی ہے۔', 'ټولګي α، β، αβ منفي ټولګي بلل کېږي ځکه چې د صفتونو نشتوالی لري.'),
    ('For attributes class frequencies are denoted by enclosing the class symbols in parentheses.', 'صفات کے لیے جماعتی تعدد کو جماعت کی علامات قوسین میں بند کر کے ظاہر کیا جاتا ہے۔', 'د صفتونو لپاره د ټولګي تکرارونه د ټولګي نښې په قوسونو کې ایښودو سره ښودل کېږي.'),
    ('When a single attribute is under study then simple process of classifying the whole data in two groups is called dichotomy.', 'جب ایک ہی صفت زیرِ مطالعہ ہو تو پورے مواد کو دو گروہوں میں درجہ بند کرنے کا سادہ عمل dichotomy کہلاتا ہے۔', 'کله چې یو صفت تر څېړنې لاندې وي، نو ټول معلومات په دوو ډلو ډلبندي کولو ساده بهیر dichotomy بلل کېږي.'),
    ('The order of a class is determined by the number of attributes present in a class.', 'کسی جماعت کا درجہ اس میں موجود صفات کی تعداد سے طے ہوتا ہے۔', 'د ټولګي درجه په ټولګي کې د موجودو صفتونو په شمېر ټاکل کېږي.'),
    ('The classes and class frequencies of the highest order are called the ultimate classes and ultimate class frequencies.', 'سب سے اونچے درجے کی جماعتیں اور جماعتی تعدد حتمی جماعتیں اور حتمی جماعتی تعدد کہلاتے ہیں۔', 'د لوړې درجې ټولګي او د ټولګیو تکرارونه وروستي ټولګي او د وروستیو ټولګیو تکرارونه بلل کېږي.'),
    ('Association is a statistical technique which measures the strength and direction of relationship among qualitative variables.', 'تلازم ایک شماریاتی تکنیک ہے جو کیفیتی متغیرات کے درمیان تعلق کی مضبوطی اور سمت کی پیمائش کرتا ہے۔', 'تړاو یوه احصاییوي تخنیک ده چې د کیفي متغیرونو ترمنځ د اړیکې ځواک او لوری اندازه کوي.'),
    ('$(AB)=\\frac{(A)(B)}{n}$. This is known as criterion of independence for attributes.', '$(AB)=\\frac{(A)(B)}{n}$۔ اسے صفات کے لیے آزادی کا معیار کہتے ہیں۔', '$(AB)=\\frac{(A)(B)}{n}$. دې ته د صفتونو لپاره د خپلواکۍ معیار وایي.'),
    (f'${QF}$ is Yule’s coefficient of association.', f'${QF}$ یول کا تلازم کا سر ہے۔', f'${QF}$ د یول د تړاو ضریب دی.'),
    ('When a population or sample is divided into many classes or categories according to an attribute is called multi-way or manifold classification.', 'جب کسی آبادی یا نمونے کو ایک صفت کے مطابق کئی جماعتوں یا زمروں میں تقسیم کیا جائے تو اسے کثیر طرفہ یا متعدد درجہ بندی کہتے ہیں۔', 'کله چې یو نفوس یا نمونه د یوه صفت له مخې په ډېرو ټولګیو یا کټګوریو ووېشل شي، څو اړخیزه یا ګڼ‌ګونې ډلبندي بلل کېږي.'),
    ('A table consisting of r-rows and c-columns into which the data are classified according to two attributes is called (r × c) contingency table.', 'r قطاروں اور c کالموں پر مشتمل جدول جس میں مواد کو دو صفات کے مطابق درجہ بند کیا جائے (r × c) اتفاقی جدول کہلاتا ہے۔', 'هغه جدول چې له r قطارونو او c ستونونو جوړ وي او معلومات پکې د دوو صفتونو له مخې ډلبندي شي، (r × c) احتمالي جدول بلل کېږي.'),
    ('Chi-square test statistic is used to test the hypothesis about independence of attributes in the contingency tables.', 'کائی مربع جانچ کا شماریہ اتفاقی جدولوں میں صفات کی آزادی کے بارے میں مفروضے کی جانچ کے لیے استعمال ہوتا ہے۔', 'د کای مربع د ازموینې احصاییه په احتمالي جدولونو کې د صفتونو د خپلواکۍ په اړه د فرضیې د ازموینې لپاره کارول کېږي.'),
])
kp = k.build('stat12-u8-key-points', 'Unit 8 — Key points', 'یونٹ 8 — اہم نکات', 'واحد 8 — مهم ټکي', 147, [285])

b = Builder()
b.h('Exercise', 'مشق', 'تمرین')
b.h('8.1 Mark the following statements as true and false.', '8.1 درج ذیل بیانات کو درست اور غلط کے طور پر نشان زد کریں۔', '8.1 لاندې بیانونه د سم او ناسم په توګه نښه کړئ.')
b.group('lines', [
    ('i. Data recorded on attributes are called quantitative data.', 'i. صفات پر ریکارڈ کیا گیا مواد مقداری مواد کہلاتا ہے۔', 'i. پر صفتونو ثبت شوي معلومات کمي معلومات بلل کېږي.'),
    ('ii. A, B, AB, ABC are called positive classes.', 'ii. A، B، AB، ABC مثبت جماعتیں کہلاتی ہیں۔', 'ii. A، B، AB، ABC مثبت ټولګي بلل کېږي.'),
    ('iii. (B) + (β) = n',) * 3,
    ('iv. If $(AB)=\\frac{(A)(B)}{n}$ means A and B are positively associated.', 'iv. اگر $(AB)=\\frac{(A)(B)}{n}$ ہو تو اس کا مطلب ہے کہ A اور B مثبت طور پر متلازم ہیں۔', 'iv. که $(AB)=\\frac{(A)(B)}{n}$ وي، مانا دا ده چې A او B مثبت تړاو لري.'),
    ('v. If Q = 0, then attributes are independent.', 'v. اگر Q = 0 ہو تو صفات آزاد ہیں۔', 'v. که Q = 0 وي، نو صفتونه خپلواک دي.'),
    ('vi. Relationship between two qualitative variables is called correlation.', 'vi. دو کیفیتی متغیرات کے درمیان تعلق کو ارتباط کہتے ہیں۔', 'vi. د دوو کیفي متغیرونو ترمنځ اړیکې ته همبستګي وایي.'),
    ('vii. $\\chi^2$ test has $\\nu=(r-1)(c-1)$ df for an (r × c) contingency table.', 'vii. (r × c) اتفاقی جدول کے لیے $\\chi^2$ جانچ کے $\\nu=(r-1)(c-1)$ درجاتِ آزادی ہیں۔', 'vii. د (r × c) احتمالي جدول لپاره د $\\chi^2$ ازموینه $\\nu=(r-1)(c-1)$ د ازادۍ درجې لري.'),
    ('viii. For a (4 × 5) contingency table the degrees of freedom for $\\chi^2$ test is 20.', 'viii. (4 × 5) اتفاقی جدول کے لیے $\\chi^2$ جانچ کے درجاتِ آزادی 20 ہیں۔', 'viii. د (4 × 5) احتمالي جدول لپاره د $\\chi^2$ ازموینې د ازادۍ درجې 20 دي.'),
    ('ix. The range of $\\chi^2$ distribution is from 0 to ∞.', 'ix. $\\chi^2$ تقسیم کی حد 0 سے ∞ تک ہے۔', 'ix. د $\\chi^2$ وېش حد له 0 تر ∞ دی.'),
    ('x. (2 × 2) contingency table contains 3-rows and 3 columns.', 'x. (2 × 2) اتفاقی جدول میں 3 قطاریں اور 3 کالم ہوتے ہیں۔', 'x. (2 × 2) احتمالي جدول 3 قطارونه او 3 ستونونه لري.'),
])
b.h('8.2 Fill in the suitable words in the blanks.', '8.2 خالی جگہوں میں موزوں الفاظ بھریں۔', '8.2 په تشو ځایونو کې مناسب ټکي ولیکئ.')
b.group('lines', [
    (f'i. If an attribute has two classes, it is said to be {B}.', f'i. اگر کسی صفت کی دو جماعتیں ہوں تو اسے {B} کہا جاتا ہے۔', f'i. که یو صفت دوه ټولګي ولري، {B} بلل کېږي.'),
    (f'ii. The number of letters representing a class determines the {B} of the class.', f'ii. کسی جماعت کو ظاہر کرنے والے حروف کی تعداد جماعت کا {B} طے کرتی ہے۔', f'ii. د یوه ټولګي ښوونکو تورو شمېر د ټولګي {B} ټاکي.'),
    (f'iii. The class represented by AB is of {B} order.', f'iii. AB سے ظاہر کی گئی جماعت {B} درجے کی ہے۔', f'iii. په AB ښودل شوی ټولګی د {B} درجې دی.'),
    (f'iv. The total of all frequencies n is of order {B}.', f'iv. تمام تعدد کا میزان n درجہ {B} کا ہے۔', f'iv. د ټولو تکرارونو ټولټال n د {B} درجې دی.'),
    (f'v. If the attributes A and B are independent, frequency (AB) is equal to {B}.', f'v. اگر صفات A اور B آزاد ہوں تو تعدد (AB) {B} کے برابر ہے۔', f'v. که صفتونه A او B خپلواک وي، تکرار (AB) له {B} سره برابر دی.'),
    (f'vi. If A and B are independent, Yule’s coefficient of association Q is equal to {B}.', f'vi. اگر A اور B آزاد ہوں تو یول کا تلازم کا سر Q {B} کے برابر ہے۔', f'vi. که A او B خپلواک وي، د یول د تړاو ضریب Q له {B} سره برابر دی.'),
    (f'vii. Association and correlation are {B}.', f'vii. تلازم اور ارتباط {B} ہیں۔', f'vii. تړاو او همبستګي {B} دي.'),
    (f'viii. Yule’s coefficient Q is ranging from {B}.', f'viii. یول کے سر Q کی حد {B} ہے۔', f'viii. د یول ضریب Q حد {B} دی.'),
    (f'ix. For an (r × c) contingency table, the sum of observed and expected frequencies must be {B}.', f'ix. (r × c) اتفاقی جدول کے لیے مشاہدہ شدہ اور متوقع تعدد کا مجموعہ {B} ہونا چاہیے۔', f'ix. د (r × c) احتمالي جدول لپاره د لیدل شویو او تمه شویو تکرارونو مجموعه باید {B} وي.'),
    (f'x. For (5 × 6) contingency table the degree of freedom for $\\chi^2$ test is equal to {B}.', f'x. (5 × 6) اتفاقی جدول کے لیے $\\chi^2$ جانچ کے درجاتِ آزادی {B} کے برابر ہیں۔', f'x. د (5 × 6) احتمالي جدول لپاره د $\\chi^2$ ازموینې د ازادۍ درجې له {B} سره برابرې دي.'),
])
ex = b.build('stat12-u8-exercise-a', 'Unit 8 Exercise — 8.1 and 8.2', 'یونٹ 8 مشق — 8.1 اور 8.2', 'واحد 8 تمرین — 8.1 او 8.2', 147, [286])

if __name__ == '__main__':
    save(147, [(8, kp), (8, ex)])
