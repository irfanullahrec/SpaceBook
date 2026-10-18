"""PDF77 printed 145–146: Unit 4 Exercise 4.1 (T/F), 4.2 (blanks), 4.3 MCQs (i)–(vii)."""
from class12_statistics_common import Builder, save

B = '______'
b = Builder()
b.h('Exercise', 'مشق', 'تمرین')
b.h('4.1 Read the following statements carefully and indicate which statement is true or false.', '4.1 درج ذیل بیانات غور سے پڑھیں اور بتائیں کہ کون سا بیان درست یا غلط ہے۔', '4.1 لاندې بیانونه په غور ولولئ او وښایاست چې کوم بیان سم یا ناسم دی.')
b.group('lines', [
    ('i. If X is a continuous uniform random variable U(a, b) then $f(x)=\\frac{1}{a-b},\\ a<x<b$.', 'i. اگر X ایک مسلسل یکساں تصادفی متغیر U(a, b) ہو تو $f(x)=\\frac{1}{a-b},\\ a<x<b$۔', 'i. که X یو متصل یونیفارم تصادفي متغیر U(a, b) وي، نو $f(x)=\\frac{1}{a-b},\\ a<x<b$.'),
    ('ii. For a Normal distribution, the mean is always lies between the median and the mode.', 'ii. نارمل تقسیم میں اوسط ہمیشہ وسطانیہ اور عادہ کے درمیان ہوتا ہے۔', 'ii. د نورمال وېش لپاره منځنی تل د منځنۍ او مود ترمنځ پروت وي.'),
    ('iii. The right and left tails of the normal curve extend indefinitely, never touching the horizontal axis.', 'iii. نارمل منحنی کے دائیں اور بائیں کنارے غیر معینہ حد تک پھیلتے ہیں اور کبھی افقی محور کو نہیں چھوتے۔', 'iii. د نورمال منحني ښي او کیڼ لکۍ په بې‌پایه ډول غځېږي او هېڅکله افقي محور نه لمسوي.'),
    ('iv. The tail will be on the right hand side of a Normal distribution for any positive z-score.', 'iv. کسی بھی مثبت z اسکور کے لیے کنارہ نارمل تقسیم کے دائیں جانب ہوگا۔', 'iv. د هر مثبت z نمرې لپاره لکۍ به د نورمال وېش ښي اړخ ته وي.'),
    ('v. Mean = Median = Mode for Normal distribution.', 'v. نارمل تقسیم کے لیے اوسط = وسطانیہ = عادہ۔', 'v. د نورمال وېش لپاره منځنی = منځنۍ = مود.'),
    ('vi. The mean and the S.D of the Standard Normal distribution is 0 and 1 respectively.', 'vi. معیاری نارمل تقسیم کا اوسط اور معیاری انحراف بالترتیب 0 اور 1 ہیں۔', 'vi. د معیاري نورمال وېش منځنی او معیاري انحراف په ترتیب سره 0 او 1 دي.'),
    ('vii. The Normal curve is symmetric around the standard deviation.', 'vii. نارمل منحنی معیاری انحراف کے گرد متشاکل ہوتی ہے۔', 'vii. نورمال منحني د معیاري انحراف شاوخوا متناظره ده.'),
    ('viii. For Normal distribution about 99.7% observations lies within the limits $\\mu\\pm 3\\sigma$.', 'viii. نارمل تقسیم میں تقریباً 99.7% مشاہدات حدود $\\mu\\pm 3\\sigma$ کے اندر ہوتے ہیں۔', 'viii. د نورمال وېش لپاره نږدې 99.7% مشاهدې د $\\mu\\pm 3\\sigma$ په حدونو کې پرتې دي.'),
    ('ix. All even order moments of Normal distribution are zero.', 'ix. نارمل تقسیم کے تمام جفت درجے کے moments صفر ہوتے ہیں۔', 'ix. د نورمال وېش د جفت ترتیب ټول مومنټونه صفر دي.'),
    ('x. In case of Normal distribution the two quartiles $Q_1$ and $Q_3$ are equidistant from the Centre.', 'x. نارمل تقسیم کی صورت میں دونوں ربعیے $Q_1$ اور $Q_3$ مرکز سے برابر فاصلے پر ہوتے ہیں۔', 'x. د نورمال وېش په حالت کې دواړه ربعیې $Q_1$ او $Q_3$ له مرکز څخه مساوي واټن لري.'),
])
b.h('4.2 Fill in the suitable word in the blanks.', '4.2 خالی جگہوں میں مناسب لفظ بھریں۔', '4.2 په تشو ځایونو کې مناسبه کلمه ولیکئ.')
b.group('lines', [
    (f'i. If X has a continuous random variable over the interval (2, 6), the mean of the distribution is equal to {B}', f'i. اگر X وقفہ (2، 6) پر مسلسل تصادفی متغیر ہو تو تقسیم کا اوسط {B} کے برابر ہے', f'i. که X د (2، 6) په واټن کې متصل تصادفي متغیر وي، د وېش منځنی له {B} سره برابر دی'),
    (f'ii. If $X\\sim N(\\mu,\\sigma^2)$, then standard normal variable Z is distributed as {B}.', f'ii. اگر $X\\sim N(\\mu,\\sigma^2)$ ہو تو معیاری نارمل متغیر Z کی تقسیم {B} ہے۔', f'ii. که $X\\sim N(\\mu,\\sigma^2)$ وي، نو معیاري نورمال متغیر Z وېش {B} دی.'),
    (f'iii. The maximum height of the normal curve lies at the point {B}.', f'iii. نارمل منحنی کی زیادہ سے زیادہ بلندی نقطہ {B} پر ہوتی ہے۔', f'iii. د نورمال منحني اعظمي لوړوالی په {B} ټکي کې دی.'),
    (f'iv. For a Normal distribution, the mean deviation from mean is {B}.', f'iv. نارمل تقسیم کے لیے اوسط سے اوسط انحراف {B} ہے۔', f'iv. د نورمال وېش لپاره له منځني څخه منځنی انحراف {B} دی.'),
    (f'v. For a Normal distribution, the odd order moments are equal to {B}.', f'v. نارمل تقسیم کے لیے طاق درجے کے moments {B} کے برابر ہوتے ہیں۔', f'v. د نورمال وېش لپاره د طاق ترتیب مومنټونه له {B} سره برابر دي.'),
    (f'vi. The value of skewness = kurtosis = 0 for {B} distribution.', f'vi. چولاؤ = نوک داری = 0 کی قیمت {B} تقسیم کے لیے ہے۔', f'vi. د کږوالي = کورټوسیس = 0 قیمت د {B} وېش لپاره دی.'),
    ('vii. If for a Normal distribution mean = 10, mode = 10, the value of median =?', 'vii. اگر نارمل تقسیم میں اوسط = 10، عادہ = 10 ہو تو وسطانیہ کی قیمت =؟', 'vii. که د نورمال وېش لپاره منځنی = 10، مود = 10 وي، د منځنۍ قیمت =؟'),
    (f'viii. The normal curve is symmetric around the {B}.', f'viii. نارمل منحنی {B} کے گرد متشاکل ہے۔', f'viii. نورمال منحني د {B} شاوخوا متناظره ده.'),
    (f'ix. The standard normal curve is symmetric around the {B}.', f'ix. معیاری نارمل منحنی {B} کے گرد متشاکل ہے۔', f'ix. معیاري نورمال منحني د {B} شاوخوا متناظره ده.'),
    (f'x. The interval $(\\mu\\pm 2\\sigma)$ under the normal curve always cover about {B} % of the area.', f'x. نارمل منحنی کے نیچے وقفہ $(\\mu\\pm 2\\sigma)$ ہمیشہ تقریباً {B} % رقبے کا احاطہ کرتا ہے۔', f'x. د نورمال منحني لاندې واټن $(\\mu\\pm 2\\sigma)$ تل نږدې {B} % مساحت رانغاړي.'),
])
b.h('4.3 Select one correct alternative out of the given ones.', '4.3 دیے گئے متبادلات میں سے ایک درست متبادل منتخب کریں۔', '4.3 له ورکړل شویو بدیلونو څخه یو سم بدیل وټاکئ.')
b.mcq('i.', ('The random variable of the Normal distribution is:', 'نارمل تقسیم کا تصادفی متغیر ہے:', 'د نورمال وېش تصادفي متغیر دی:'),
      [('discrete', 'منفصل', 'منفصل'), ('continuous', 'مسلسل', 'متصل'), ('positive', 'مثبت', 'مثبت')], per_line=3)
b.mcq('ii.', ('If the distribution follows Normal then Mean = Median = Mode', 'اگر تقسیم نارمل ہو تو اوسط = وسطانیہ = عادہ', 'که وېش نورمال وي نو منځنی = منځنۍ = مود'),
      [('true', 'درست', 'سم'), ('false', 'غلط', 'ناسم'), ('impossible', 'ناممکن', 'ناشونی')], per_line=3)
b.mcq('iii.', ('If X is a uniform variable over the interval (5, 10), then the mean of x is', 'اگر X وقفہ (5، 10) پر یکساں متغیر ہو تو x کا اوسط ہے', 'که X د (5، 10) په واټن کې یونیفارم متغیر وي، نو د x منځنی دی'), ['5', '7.5', '10', '15'], per_line=4)
b.mcq('iv.', ('Use of the standard normal variable Z instead of normal variable X', 'نارمل متغیر X کی جگہ معیاری نارمل متغیر Z کا استعمال', 'د نورمال متغیر X پر ځای د معیاري نورمال متغیر Z کارول'),
      [('complicates the calculation of normal probabilities.', 'نارمل احتمالات کا حساب پیچیدہ بنا دیتا ہے۔', 'د نورمال احتمالونو محاسبه پېچلې کوي.'), ('simplifies the calculation of normal probabilities.', 'نارمل احتمالات کا حساب آسان بنا دیتا ہے۔', 'د نورمال احتمالونو محاسبه اسانه کوي.'),
       ('Does not make any difference.', 'کوئی فرق نہیں ڈالتا۔', 'هېڅ توپیر نه راولي.'), ('gives wrong answer.', 'غلط جواب دیتا ہے۔', 'ناسم ځواب ورکوي.')], per_line=1)
b.mcq('v.', ('The total area under a Normal distribution curve to the left of the mean is always equal to', 'نارمل تقسیم کی منحنی کے نیچے اوسط کے بائیں جانب کل رقبہ ہمیشہ برابر ہے', 'د نورمال وېش د منحني لاندې د منځني کیڼ اړخ ته ټول مساحت تل برابر دی له'), ['1', '0', '0.5', '0.9'], per_line=4)
b.mcq('vi.', ('A normal curve with a small standard deviation will be', 'چھوٹے معیاری انحراف والی نارمل منحنی ہوگی', 'د کوچني معیاري انحراف لرونکې نورمال منحني به وي'),
      [('positively skewed', 'مثبت چولاؤ والی', 'مثبت کږه'), ('more spread out', 'زیادہ پھیلی ہوئی', 'ډېره خپره'), ('less spread out', 'کم پھیلی ہوئی', 'لږه خپره'), ('platy kurtic', 'چپٹی (platykurtic)', 'پلاټي‌کورټیک')])
b.mcq('vii.', ('The tail of the Normal distribution', 'نارمل تقسیم کا کنارہ', 'د نورمال وېش لکۍ'),
      [('meet the horizontal axis at Z = 3.0', 'Z = 3.0 پر افقی محور سے ملتا ہے', 'په Z = 3.0 کې افقي محور سره یوځای کېږي'), ('cross the horizontal axis at Z = 4.0', 'Z = 4.0 پر افقی محور کو کاٹتا ہے', 'په Z = 4.0 کې افقي محور قطع کوي'),
       ('never meet or cross the horizontal axis.', 'کبھی افقی محور سے نہیں ملتا اور نہ اسے کاٹتا ہے۔', 'هېڅکله افقي محور سره نه یوځای کېږي او نه یې قطع کوي.'), ('are asymmetric', 'غیر متشاکل ہیں', 'نامتناظر دي')], per_line=1)
rec = b.build('stat12-u4-exercise-a', 'Unit 4 Exercise — 4.1 to 4.3 (vii)', 'یونٹ 4 مشق — 4.1 تا 4.3 (vii)', 'واحد 4 تمرین — 4.1 تر 4.3 (vii)', 77, [145, 146])

if __name__ == '__main__':
    save(77, [(4, rec)])
