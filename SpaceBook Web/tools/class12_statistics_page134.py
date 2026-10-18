"""PDF134 printed 259–260: Unit 7 key points; Exercise 7.1 (T/F), 7.2 blanks, 7.3 MCQ (i)."""
from class12_statistics_common import Builder, save

B = '______'
k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.group('list', [
    ('Hypothesis is an unproved claim or assertion or assumption which acts as a starting point in a research irrespective of its probable truthfulness or falsity.', 'مفروضہ ایک غیر ثابت شدہ دعویٰ، اظہار یا فرض ہے جو اپنی ممکنہ سچائی یا جھوٹ سے قطع نظر تحقیق میں نقطہ آغاز کا کام دیتا ہے۔', 'فرضیه یوه نه ثابته شوې ادعا، اظهار یا انګېرنه ده چې د خپل احتمالي ریښتینولۍ یا ناسموالي څخه پرته په څېړنه کې د پیل ټکي دنده ترسره کوي.'),
    ('A statistical hypothesis is a testable claim about one or more parameter(s) of empirical distributions.', 'شماریاتی مفروضہ تجرباتی تقسیموں کے ایک یا زیادہ پیرامیٹر(ز) کے بارے میں قابلِ جانچ دعویٰ ہے۔', 'احصاییوي فرضیه د تجربوي وېشونو د یوه یا ډېرو پارامټر(ونو) په اړه د ازموینې وړ ادعا ده.'),
    ('A statistical method that uses sample data to accept or reject a hypothesis about a parameter is called hypothesis testing.', 'وہ شماریاتی طریقہ جو پیرامیٹر کے بارے میں کسی مفروضے کو قبول یا رد کرنے کے لیے نمونے کا مواد استعمال کرتا ہے، مفروضے کی جانچ کہلاتا ہے۔', 'هغه احصاییوي طریقه چې د یوه پارامټر په اړه د فرضیې د منلو یا ردولو لپاره نمونوي معلومات کاروي، د فرضیې ازموینه بلل کېږي.'),
    ('Null hypothesis is a claim about parameter. It is tested for possible rejection under the assumption it is true. It is denoted by $H_0$', 'صفری مفروضہ پیرامیٹر کے بارے میں ایک دعویٰ ہے۔ اسے درست فرض کرتے ہوئے ممکنہ رد کے لیے جانچا جاتا ہے۔ اسے $H_0$ سے ظاہر کیا جاتا ہے', 'صفري فرضیه د پارامټر په اړه یوه ادعا ده. د سم ګڼلو په انګېرنه د احتمالي ردولو لپاره ازمویل کېږي. په $H_0$ ښودل کېږي'),
    ('Alternative hypothesis is also a claim about parameter which is accepted if $H_0$ is rejected. It is tested for possible acceptance under the assumption it is false. It is denoted by $H_1$.', 'متبادل مفروضہ بھی پیرامیٹر کے بارے میں ایک دعویٰ ہے جو $H_0$ رد ہونے پر قبول کیا جاتا ہے۔ اسے غلط فرض کرتے ہوئے ممکنہ قبولیت کے لیے جانچا جاتا ہے۔ اسے $H_1$ سے ظاہر کیا جاتا ہے۔', 'بدیله فرضیه هم د پارامټر په اړه یوه ادعا ده چې که $H_0$ رد شي، منل کېږي. د ناسم ګڼلو په انګېرنه د احتمالي منلو لپاره ازمویل کېږي. په $H_1$ ښودل کېږي.'),
    ('When all parameters of a distribution are well specified, it is called simple hypothesis.', 'جب تقسیم کے تمام پیرامیٹرز اچھی طرح متعین ہوں تو اسے سادہ مفروضہ کہتے ہیں۔', 'کله چې د وېش ټول پارامټرونه ښه ټاکل شوي وي، ساده فرضیه بلل کېږي.'),
    ('When all parameters of a distribution are not well specified, it is called composite hypothesis.', 'جب تقسیم کے تمام پیرامیٹرز اچھی طرح متعین نہ ہوں تو اسے مرکب مفروضہ کہتے ہیں۔', 'کله چې د وېش ټول پارامټرونه ښه نه وي ټاکل شوي، مرکبه فرضیه بلل کېږي.'),
    ('“Reject a null hypothesis when it is true” is called Type-I error.', '“صفری مفروضے کو درست ہونے کے باوجود رد کرنا” قسم-I کی غلطی کہلاتا ہے۔', '“د صفري فرضیې ردول کله چې سمه وي” د I-ډول تېروتنه بلل کېږي.'),
    ('“Accept a null hypothesis when it is false” is called Type-II error.', '“صفری مفروضے کو غلط ہونے کے باوجود قبول کرنا” قسم-II کی غلطی کہلاتا ہے۔', '“د صفري فرضیې منل کله چې ناسمه وي” د II-ډول تېروتنه بلل کېږي.'),
    ('The probability of Type-I error which we are ready to tolerate in making decision about $H_0$ is called significance level', '$H_0$ کے بارے میں فیصلہ کرتے وقت قسم-I کی غلطی کا وہ احتمال جسے ہم برداشت کرنے کو تیار ہوں، معنویت کی سطح کہلاتا ہے', 'د $H_0$ په اړه د پرېکړې پر مهال د I-ډول تېروتنې هغه احتمال چې موږ یې زغملو ته چمتو یو، د معنی‌داریت کچه بلل کېږي'),
    ('A function of sample data is called statistic. When a statistic is used to test a hypothesis it is called test statistic or decision rule.', 'نمونے کے مواد کا فعل شماریہ کہلاتا ہے۔ جب شماریہ کسی مفروضے کی جانچ کے لیے استعمال ہو تو اسے جانچ کا شماریہ یا فیصلہ کن قاعدہ کہتے ہیں۔', 'د نمونوي معلوماتو تابع احصاییه بلل کېږي. کله چې احصاییه د فرضیې د ازموینې لپاره وکارول شي، د ازموینې احصاییه یا د پرېکړې قاعده بلل کېږي.'),
    ('The group of values which would lead us to acceptance of $H_0$ or the part where (1 − α) lies is called acceptance region (AR) for the test.', 'قیمتوں کا وہ گروہ جو ہمیں $H_0$ کی قبولیت تک لے جائے یا وہ حصہ جہاں (1 − α) واقع ہو، جانچ کا قبولیت کا علاقہ (AR) کہلاتا ہے۔', 'د قیمتونو هغه ډله چې موږ د $H_0$ منلو ته رسوي یا هغه برخه چې (1 − α) پکې پروت وي، د ازموینې د منلو سیمه (AR) بلل کېږي.'),
    ('The group of values which would lead us to rejection of $H_0$ or the part where (α) lies is called rejection region (RR) or critical region for the test.', 'قیمتوں کا وہ گروہ جو ہمیں $H_0$ کے رد تک لے جائے یا وہ حصہ جہاں (α) واقع ہو، جانچ کا رد کا علاقہ (RR) یا فیصلہ کن علاقہ کہلاتا ہے۔', 'د قیمتونو هغه ډله چې موږ د $H_0$ ردولو ته رسوي یا هغه برخه چې (α) پکې پروت وي، د ازموینې د ردولو سیمه (RR) یا بحراني سیمه بلل کېږي.'),
    ('The values which separate the (AR) and (RR) are called critical values.', 'وہ قیمتیں جو (AR) اور (RR) کو الگ کرتی ہیں، فیصلہ کن قیمتیں کہلاتی ہیں۔', 'هغه قیمتونه چې (AR) او (RR) بېلوي، بحراني قیمتونه بلل کېږي.'),
    ('When the whole rejection region of size α lies on one tail of the concerned sampling distribution, it is called one-tailed test.', 'جب α سائز کا پورا رد کا علاقہ متعلقہ نمونہ جاتی تقسیم کے ایک سرے پر ہو تو اسے یک طرفہ جانچ کہتے ہیں۔', 'کله چې د α اندازې ټوله د ردولو سیمه د اړوند نمونوي وېش په یوه لکۍ کې وي، یو لکۍ‌والې ازموینه بلل کېږي.'),
    ('When rejection region of size α is equally divided, α/2 lies in the right tail and α/2 lies in the left tail of the concerned sampling distribution, it is called two-tailed test.', 'جب α سائز کا رد کا علاقہ برابر تقسیم ہو، α/2 متعلقہ نمونہ جاتی تقسیم کے دائیں سرے اور α/2 بائیں سرے پر ہو تو اسے دو طرفہ جانچ کہتے ہیں۔', 'کله چې د α اندازې د ردولو سیمه برابره ووېشل شي، α/2 د اړوند نمونوي وېش په ښۍ لکۍ او α/2 په کیڼه لکۍ کې وي، دوه لکۍ‌والې ازموینه بلل کېږي.'),
])
kp = k.build('stat12-u7-key-points', 'Unit 7 — Key points', 'یونٹ 7 — اہم نکات', 'واحد 7 — مهم ټکي', 134, [259])

b = Builder()
b.h('Exercise', 'مشق', 'تمرین')
b.h('7.1 Write “T” for true and “F” for false in the following statement.', '7.1 درج ذیل بیان میں درست کے لیے “T” اور غلط کے لیے “F” لکھیں۔', '7.1 په لاندې بیان کې د سم لپاره “T” او د ناسم لپاره “F” ولیکئ.')
b.group('lines', [
    ('i. A statistical hypothesis is a statement about the value of a statistic.', 'i. شماریاتی مفروضہ شماریے کی قیمت کے بارے میں ایک بیان ہے۔', 'i. احصاییوي فرضیه د احصاییې د قیمت په اړه یو بیان دی.'),
    ('ii. The null hypothesis is framed for possible rejection.', 'ii. صفری مفروضہ ممکنہ رد کے لیے بنایا جاتا ہے۔', 'ii. صفري فرضیه د احتمالي ردولو لپاره جوړېږي.'),
    ('iii. In statistical inference “accept $H_0$” means that there is insufficient information to reject $H_0$.', 'iii. شماریاتی استنباط میں “$H_0$ قبول کریں” کا مطلب ہے کہ $H_0$ کو رد کرنے کے لیے ناکافی معلومات ہیں۔', 'iii. په احصاییوي استنتاج کې “$H_0$ ومنئ” مانا دا ده چې د $H_0$ ردولو لپاره ناکافي معلومات شته.'),
    ('iv. An upper-tailed test occurs when $H_0:\\mu\\ge\\mu_0$ and $H_1:\\mu<\\mu_0$.', 'iv. بالائی سرے کی جانچ تب ہوتی ہے جب $H_0:\\mu\\ge\\mu_0$ اور $H_1:\\mu<\\mu_0$ ہو۔', 'iv. د پورته لکۍ ازموینه هغه وخت وي چې $H_0:\\mu\\ge\\mu_0$ او $H_1:\\mu<\\mu_0$.'),
    ('v. If a null hypothesis $H_0:\\mu=50$ is rejected at 1% level of significance, it will also be rejected a 5% level of significance.', 'v. اگر صفری مفروضہ $H_0:\\mu=50$ معنویت کی 1% سطح پر رد ہو تو یہ 5% معنویت کی سطح پر بھی رد ہوگا۔', 'v. که صفري فرضیه $H_0:\\mu=50$ د معنی‌داریت په 1% کچه رد شي، نو د معنی‌داریت په 5% کچه به هم رد شي.'),
    ('vi. When a true null hypothesis has been rejected, we say that Type-I error might have been committed.', 'vi. جب درست صفری مفروضہ رد کر دیا جائے تو ہم کہتے ہیں کہ قسم-I کی غلطی ہوئی ہو سکتی ہے۔', 'vi. کله چې سمه صفري فرضیه رد شي، وایو چې کېدای شي د I-ډول تېروتنه شوې وي.'),
    ('vii. α and β have an inverse relationship.', 'vii. α اور β کا معکوس تعلق ہے۔', 'vii. α او β معکوسه اړیکه لري.'),
    ('viii. $H_0:\\mu<5$ is a simple null hypothesis.', 'viii. $H_0:\\mu<5$ ایک سادہ صفری مفروضہ ہے۔', 'viii. $H_0:\\mu<5$ یوه ساده صفري فرضیه ده.'),
    ('ix. When the sample size n increases the probability of rejecting a true hypothesis decreases.', 'ix. جب نمونے کا سائز n بڑھتا ہے تو درست مفروضے کو رد کرنے کا احتمال کم ہو جاتا ہے۔', 'ix. کله چې د نمونې اندازه n زیاتېږي، د سمې فرضیې د ردولو احتمال کمېږي.'),
    ('x. Confidence interval estimate of a parameter is the same thing as testing of hypothesis about the population parameter.', 'x. پیرامیٹر کا اعتماد کے وقفے کا تخمینہ اور آبادی کے پیرامیٹر کے بارے میں مفروضے کی جانچ ایک ہی چیز ہے۔', 'x. د پارامټر د باور د واټن اټکل او د نفوس د پارامټر په اړه د فرضیې ازموینه یو شی دی.'),
])
b.h('7.2 Fill in the suitable word in the blanks.', '7.2 خالی جگہوں میں موزوں لفظ بھریں۔', '7.2 په تشو ځایونو کې مناسب ټکی ولیکئ.')
b.group('lines', [
    (f'i. A hypothesis is an {B} about the parameter of a population.', f'i. مفروضہ آبادی کے پیرامیٹر کے بارے میں ایک {B} ہے۔', f'i. فرضیه د نفوس د پارامټر په اړه یو {B} ده.'),
    (f'ii. The hypothesis which is under test for possible rejection is called {B} hypothesis.', f'ii. وہ مفروضہ جو ممکنہ رد کے لیے زیرِ جانچ ہو {B} مفروضہ کہلاتا ہے۔', f'ii. هغه فرضیه چې د احتمالي ردولو لپاره تر ازموینې لاندې وي، {B} فرضیه بلل کېږي.'),
    (f'iii. A hypothesis contrary to null hypothesis is known as {B}.', f'iii. صفری مفروضے کے برعکس مفروضہ {B} کہلاتا ہے۔', f'iii. د صفري فرضیې مخالفه فرضیه {B} بلل کېږي.'),
    (f'iv. The hypothesis $H_0:\\mu>\\mu_0$ is a {B} hypothesis.', f'iv. مفروضہ $H_0:\\mu>\\mu_0$ ایک {B} مفروضہ ہے۔', f'iv. فرضیه $H_0:\\mu>\\mu_0$ یوه {B} فرضیه ده.'),
    (f'v. Type {B} error is more severe than type {B} error.', f'v. قسم {B} کی غلطی قسم {B} کی غلطی سے زیادہ سنگین ہے۔', f'v. د {B} ډول تېروتنه د {B} ډول تېروتنې په پرتله ډېره سخته ده.'),
    (f'vi. Probability of Type-I error is called {B}.', f'vi. قسم-I کی غلطی کا احتمال {B} کہلاتا ہے۔', f'vi. د I-ډول تېروتنې احتمال {B} بلل کېږي.'),
    (f'vii. Level of significance lies between {B} and {B}.', f'vii. معنویت کی سطح {B} اور {B} کے درمیان ہوتی ہے۔', f'vii. د معنی‌داریت کچه د {B} او {B} ترمنځ وي.'),
    (f'viii. Critical region is also known as {B}.', f'viii. فیصلہ کن علاقے کو {B} بھی کہتے ہیں۔', f'viii. بحراني سیمه د {B} په نوم هم یادېږي.'),
    (f'ix. A statistical test is a {B} to decide about $H_0$.', f'ix. شماریاتی جانچ $H_0$ کے بارے میں فیصلہ کرنے کا ایک {B} ہے۔', f'ix. احصاییوي ازموینه د $H_0$ په اړه د پرېکړې لپاره یو {B} ده.'),
    (f'x. The number of independent values in a set of values is known as - {B}.', f'x. قیمتوں کے ایک مجموعے میں آزاد قیمتوں کی تعداد - {B} کہلاتی ہے۔', f'x. د قیمتونو په یوه ټولګه کې د خپلواکو قیمتونو شمېر - {B} بلل کېږي.'),
])
b.h('7.3 Choose the correct answer.', '7.3 درست جواب منتخب کریں۔', '7.3 سم ځواب وټاکئ.')
b.mcq('i.', ('A hypothesis under test is:', 'زیرِ جانچ مفروضہ ہے:', 'تر ازموینې لاندې فرضیه ده:'),
      [('Simple hypothesis', 'سادہ مفروضہ', 'ساده فرضیه'), ('composite hypothesis', 'مرکب مفروضہ', 'مرکبه فرضیه'), ('Null hypothesis', 'صفری مفروضہ', 'صفري فرضیه'), ('alternative hypothesis', 'متبادل مفروضہ', 'بدیله فرضیه')])
ex = b.build('stat12-u7-exercise-a', 'Unit 7 Exercise — 7.1, 7.2 and 7.3 (i)', 'یونٹ 7 مشق — 7.1، 7.2 اور 7.3 (i)', 'واحد 7 تمرین — 7.1، 7.2 او 7.3 (i)', 134, [260])
issues = [{'id': 'stat12-p260-rejected-a-5', 'unit': 7, 'printedPage': 260, 'description': 'Exercise 7.1 (v) prints “rejected a 5% level” (for “at 5% level”); printed wording retained.'}]

if __name__ == '__main__':
    save(134, [(7, kp), (7, ex)], issues=issues)
