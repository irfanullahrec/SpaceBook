"""PDF135 printed 261–262: Unit 7 Exercise 7.3 MCQs (ii)–(x); questions 7.4–7.10."""
from class12_statistics_common import Builder, save

b = Builder()
b.mcq('ii.', ('Whether a test is one-sided or two-sided depends on:', 'کوئی جانچ یک طرفہ ہے یا دو طرفہ، اس کا انحصار ہے:', 'آیا ازموینه یو اړخیزه ده که دوه اړخیزه، په دې پورې اړه لري:'),
      [('Alternative hypothesis', 'متبادل مفروضہ', 'بدیله فرضیه'), ('Composite hypothesis', 'مرکب مفروضہ', 'مرکبه فرضیه'), ('null hypothesis', 'صفری مفروضہ', 'صفري فرضیه'), ('Simple hypothesis', 'سادہ مفروضہ', 'ساده فرضیه')])
b.mcq('iii.', ('A wrong decision about $H_0$ leads to:', '$H_0$ کے بارے میں غلط فیصلہ لے جاتا ہے:', 'د $H_0$ په اړه ناسمه پرېکړه رسوي:'),
      [('One kind of error', 'ایک قسم کی غلطی', 'یو ډول تېروتنې ته'), ('Two kind of error', 'دو قسم کی غلطی', 'دوه ډوله تېروتنې ته'), ('Three kind of error', 'تین قسم کی غلطی', 'درې ډوله تېروتنې ته'), ('Four kind of error.', 'چار قسم کی غلطی۔', 'څلور ډوله تېروتنې ته.')])
b.mcq('iv.', ('Level of significance is the probability of:', 'معنویت کی سطح کس کا احتمال ہے:', 'د معنی‌داریت کچه د څه احتمال دی:'),
      [('Type-I error', 'قسم-I کی غلطی', 'I-ډول تېروتنه'), ('Type-II error', 'قسم-II کی غلطی', 'II-ډول تېروتنه'), ('Not committing error', 'غلطی نہ کرنا', 'تېروتنه نه کول'), ('Any of the above', 'مندرجہ بالا میں سے کوئی بھی', 'له پورتنیو هر یو')])
b.mcq('v.', ('Degrees of freedom is related to:', 'درجاتِ آزادی کا تعلق ہے:', 'د ازادۍ درجې تړاو لري:'),
      [('Number of observations in a set', 'ایک مجموعے میں مشاہدات کی تعداد', 'په یوه ټولګه کې د مشاهدو شمېر'), ('Hypothesis under test', 'زیرِ جانچ مفروضہ', 'تر ازموینې لاندې فرضیه'),
       ('Number of independent observation in set', 'مجموعے میں آزاد مشاہدات کی تعداد', 'په ټولګه کې د خپلواکو مشاهدو شمېر'), ('confidence interval', 'اعتماد کا وقفہ', 'د باور واټن')], per_line=1)
b.mcq('vi.', ('As compared to normal distribution, the t-distribution is:', 'نارمل تقسیم کے مقابلے میں t-تقسیم ہے:', 'د نورمال وېش په پرتله t-وېش دی:'),
      [('Flatter', 'زیادہ چپٹی', 'ډېر هوار'), ('More peaked', 'زیادہ نوکیلی', 'ډېر څوکدار'), ('Symmetric', 'متناسب', 'متناظر'), ('Negatively skewed.', 'منفی طور پر ترچھی۔', 'منفي کږ.')])
b.mcq('vii.', ('Student’s t-test is applicable in case of:', 'سٹوڈنٹ کی t-جانچ اس صورت میں قابلِ اطلاق ہے:', 'د سټوډنټ t-ازموینه په دې حالت کې د کارولو وړ ده:'),
      [('Small samples', 'چھوٹے نمونے', 'کوچنۍ نمونې'), ('Large samples', 'بڑے نمونے', 'لویې نمونې'), ('For samples of size between 5 and 29.', '5 اور 29 کے درمیان سائز کے نمونوں کے لیے۔', 'د 5 او 29 ترمنځ اندازې نمونو لپاره.'), ('biased samples', 'جانبدار نمونے', 'پلوي نمونې')], per_line=1)
b.mcq('viii.', ('To test $H_0:\\mu=\\mu_0$ vs $H_1:\\mu>\\mu_0$ when the population S.D is known, the appropriate test is:', 'جب آبادی کا معیاری انحراف معلوم ہو تو $H_1:\\mu>\\mu_0$ کے مقابلے میں $H_0:\\mu=\\mu_0$ کی جانچ کے لیے موزوں جانچ ہے:', 'کله چې د نفوس معیاري انحراف معلوم وي، د $H_1:\\mu>\\mu_0$ پر وړاندې د $H_0:\\mu=\\mu_0$ د ازموینې لپاره مناسبه ازموینه ده:'),
      [('t-test', 't-جانچ', 't-ازموینه'), ('Z-test', 'Z-جانچ', 'Z-ازموینه'), ('Chi-square', 'کائی مربع', 'کای مربع'), ('F-test.', 'F-جانچ۔', 'F-ازموینه.')])
b.mcq('ix.', ('Testing hypothesis $H_0:\\mu=10$ vs $H_1:\\mu>10$ leads to:', 'مفروضے $H_0:\\mu=10$ بمقابلہ $H_1:\\mu>10$ کی جانچ لے جاتی ہے:', 'د $H_0:\\mu=10$ د $H_1:\\mu>10$ پر وړاندې ازموینه رسوي:'),
      [('One sided left tailed test', 'یک طرفہ بائیں سرے کی جانچ', 'یو اړخیزه کیڼ لکۍ ازموینې ته'), ('one sided right tailed test', 'یک طرفہ دائیں سرے کی جانچ', 'یو اړخیزه ښي لکۍ ازموینې ته'), ('Two-tailed test', 'دو طرفہ جانچ', 'دوه لکۍ ازموینې ته'), ('all of the above', 'مندرجہ بالا سب', 'پورتني ټول')])
b.mcq('x.', ('Range of statistic-t is:', 'شماریہ-t کی حد ہے:', 'د t-احصاییې حد دی:'), ['$-1$ to $+1$,', '$-\\infty$ to $\\infty$', '$0$ to $\\infty$', '$0$ to $1$'])
b.group('lines', [
    ('7.4 Define hypothesis, statistical hypothesis and testing of hypothesis?', '7.4 مفروضہ، شماریاتی مفروضہ اور مفروضے کی جانچ کی تعریف کریں؟', '7.4 فرضیه، احصاییوي فرضیه او د فرضیې ازموینه تعریف کړئ؟'),
    ('7.5 Explain in your own words (i) Hypothesis testing (ii) Estimation. What are the principle steps involved in hypothesis testing procedure?', '7.5 اپنے الفاظ میں وضاحت کریں (i) مفروضے کی جانچ (ii) تخمین۔ مفروضے کی جانچ کے طریقے میں شامل بنیادی مراحل کیا ہیں؟', '7.5 په خپلو ټکو کې تشریح کړئ (i) د فرضیې ازموینه (ii) اټکل. د فرضیې د ازموینې په طریقه کې اصلي ګامونه کوم دي؟'),
    ('7.6 Differentiate between:', '7.6 فرق بیان کریں:', '7.6 توپیر وښایاست:'),
    ('(i) Null and alternative hypothesis.', '(i) صفری اور متبادل مفروضہ۔', '(i) صفري او بدیله فرضیه.'),
    ('(ii) Simple and composite hypothesis.', '(ii) سادہ اور مرکب مفروضہ۔', '(ii) ساده او مرکبه فرضیه.'),
    ('(iii) Type-I and Type-II Errors.', '(iii) قسم-I اور قسم-II کی غلطیاں۔', '(iii) د I-ډول او II-ډول تېروتنې.'),
    ('(iv) Acceptance and rejection region.', '(iv) قبولیت اور رد کا علاقہ۔', '(iv) د منلو او ردولو سیمه.'),
    ('7.7 Explain the following terms:', '7.7 درج ذیل اصطلاحات کی وضاحت کریں:', '7.7 لاندې اصطلاحګانې تشریح کړئ:'),
    ('(a) Level of significance.', '(a) معنویت کی سطح۔', '(a) د معنی‌داریت کچه.'),
    ('(b) Test statistic and test of significance.', '(b) جانچ کا شماریہ اور معنویت کی جانچ۔', '(b) د ازموینې احصاییه او د معنی‌داریت ازموینه.'),
    ('(c) Small sample and large sample.', '(c) چھوٹا نمونہ اور بڑا نمونہ۔', '(c) کوچنۍ نمونه او لویه نمونه.'),
    ('7.8 What do you mean by one-sided test and two sided test? Explain your idea with diagrams?', '7.8 یک طرفہ جانچ اور دو طرفہ جانچ سے آپ کیا مراد لیتے ہیں؟ اپنے خیال کی اشکال کے ساتھ وضاحت کریں؟', '7.8 له یو اړخیزې ازموینې او دوه اړخیزې ازموینې څخه ستاسو مطلب څه دی؟ خپل نظر د شکلونو سره تشریح کړئ؟'),
    ('7.9 Describe the general procedure (steps) for testing hypothesis about mean of a normal population when population standard deviation is known and sample size is large.', '7.9 جب آبادی کا معیاری انحراف معلوم ہو اور نمونے کا سائز بڑا ہو تو نارمل آبادی کے اوسط کے بارے میں مفروضے کی جانچ کا عمومی طریقہ (مراحل) بیان کریں۔', '7.9 کله چې د نفوس معیاري انحراف معلوم وي او د نمونې اندازه لویه وي، د نورمال نفوس د منځني په اړه د فرضیې د ازموینې عمومي طریقه (ګامونه) بیان کړئ.'),
    ('7.10 A random sample of size n = 900 plants and its mean is computed which is equal to 34 cm. Can it be reasonably regarded as a random sample from a large population with mean 32 cm and standard deviation 23 cm. Testing at α = 0.05.', '7.10 n = 900 پودوں کا ایک تصادفی نمونہ لیا گیا اور اس کا اوسط معلوم کیا گیا جو 34 cm کے برابر ہے۔ کیا اسے معقول طور پر 32 cm اوسط اور 23 cm معیاری انحراف والی بڑی آبادی کا تصادفی نمونہ سمجھا جا سکتا ہے؟ α = 0.05 پر جانچ کریں۔', '7.10 د n = 900 بوټو تصادفي نمونه او د هغې منځنی محاسبه شو چې له 34 cm سره برابر دی. آیا دا په معقول ډول د یوه لوی نفوس تصادفي نمونه ګڼل کېدای شي چې منځنی یې 32 cm او معیاري انحراف یې 23 cm وي؟ په α = 0.05 وازموئ.'),
])
ex = b.build('stat12-u7-exercise-b', 'Unit 7 Exercise — 7.3 (ii)–(x), 7.4–7.10', 'یونٹ 7 مشق — 7.3 (ii)–(x)، 7.4–7.10', 'واحد 7 تمرین — 7.3 (ii)–(x)، 7.4–7.10', 135, [261, 262])

if __name__ == '__main__':
    save(135, [(7, ex)])
