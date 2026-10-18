"""PDF174 printed 339–340: Index G–Y (end)."""
from class12_statistics_common import save
from class12_statistics_page173 import index_record

IDX = [
    ('G', [('Goldfish bowl method', '159', 'گولڈ فش باؤل کا طریقہ', 'د ګولډفش کاسې طریقه')]),
    ('H', [('Hypergeometric experiment', '98', 'ہائپر جیومیٹرک تجربہ', 'هایپرجیومټریکه تجربه'), ('Hypergeometric probability distribution', '98', 'ہائپر جیومیٹرک احتمالی تقسیم', 'هایپرجیومټریک احتمالي وېش'), ('Hypothesis testing', '232', 'مفروضے کی جانچ', 'د فرضیې ازموینه')]),
    ('I', [('Impossible event', '06', 'ناممکن واقعہ', 'ناشونې پېښه'), ('Independent events', '08', 'آزاد واقعات', 'خپلواکې پېښې'), ('Infinite population', '152', 'لامتناہی آبادی', 'نامحدود نفوس'), ('Interval estimation', '209', 'وقفہ تخمین', 'واټني اټکل')]),
    ('J', [('Joint distribution', '56', 'مشترکہ تقسیم', 'ګډ وېش')]),
    ('L', [('Level of significance', '235', 'معنویت کی سطح', 'د معنی‌داریت کچه'), ('Length of confidence interval', '209', 'اعتماد کے وقفے کی لمبائی', 'د باور د واټن اوږدوالی'), ('Local control', '296', 'مقامی کنٹرول', 'سیمه‌ییز کنټرول')]),
    ('M', [('Mutually exclusive events', '07', 'باہم خارجی واقعات', 'متقابلاً جلا پېښې'), ('Mathematical expectation', '41', 'ریاضیاتی توقع', 'ریاضیاتي تمه'), ('Marginal probability distribution', '57', 'حاشیائی احتمالی تقسیم', 'څنډه‌ییز احتمالي وېش'), ('Multiway classification', '275', 'کثیر طرفہ درجہ بندی', 'څو اړخیزه ډلبندي')]),
    ('N', [('Normal distribution', '120', 'نارمل تقسیم', 'نورمال وېش'), ('Non-Sampling error', '156', 'غیر نمونہ جاتی خطا', 'نانمونوي تېروتنه'), ('Non probability sampling methods', '158', 'غیر احتمالی نمونہ گیری کے طریقے', 'نااحتمالي نمونه‌اخیستنې طریقې'),
           ('Null hypothesis', '233', 'صفری مفروضہ', 'صفري فرضیه'), ('Negative attributes', '267', 'منفی صفات', 'منفي صفتونه')]),
    ('O', [('Outcome', '06', 'نتیجہ', 'پایله'), ('Odds', '24', 'امکانات', 'امکانات'), ('One tailed test', '236', 'یک طرفہ جانچ', 'یو لکۍ ازموینه'), ('One way classification', '268', 'یک طرفہ درجہ بندی', 'یو اړخیزه ډلبندي'), ('Order of classes', '269', 'جماعتوں کا درجہ', 'د ټولګیو درجه')]),
    ('P', [('Permutation', '02', 'ترتیب', 'ترتیب'), ('Probability', '05', 'احتمال', 'احتمال'), ('Probability distribution', '32', 'احتمالی تقسیم', 'احتمالي وېش'), ('Probability function', '34', 'احتمالی فعل', 'احتمالي تابع'),
           ('Probability mass function', '34', 'احتمالی کمیتی فعل', 'احتمالي کتلوي تابع'), ('Probability density function', '51', 'احتمالی کثافتی فعل', 'احتمالي کثافتي تابع'), ('Population', '152', 'آبادی', 'نفوس'), ('Parameter', '155', 'پیرامیٹر', 'پارامټر'),
           ('Probability sampling methods', '158', 'احتمالی نمونہ گیری کے طریقے', 'احتمالي نمونه‌اخیستنې طریقې'), ('Proportion', '176', 'تناسب', 'تناسب'), ('Point estimation', '195', 'نقطہ تخمین', 'ټکي‌ییز اټکل'), ('Pooled estimator', '207', 'مشترکہ تخمین کار', 'ګډ اټکلوونکی'),
           ('Precision of confidence interval', '210', 'اعتماد کے وقفے کی درستی', 'د باور د واټن دقت'), ('Positive attributes', '267', 'مثبت صفات', 'مثبت صفتونه')]),
    ('R', [('Random experiment', '05', 'تصادفی تجربہ', 'تصادفي تجربه'), ('Random variable', '32', 'تصادفی متغیر', 'تصادفي متغیر'), ('Random digits', '75', 'تصادفی ہندسے', 'تصادفي رقمونه'), ('Random numbers', '75', 'تصادفی اعداد', 'تصادفي عددونه'),
           ('Rejection region', '235', 'رد کا علاقہ', 'د ردولو سیمه'), ('Randomization', '295', 'تصادفیت', 'تصادفي کول'), ('Replication', '295', 'تکرار', 'تکرار')]),
    ('S', [('Sample space', '05', 'نمونہ جاتی فضا', 'نمونوي فضا'), ('Simple event', '06', 'سادہ واقعہ', 'ساده پېښه'), ('Sure event', '07', 'یقینی واقعہ', 'ډاډمنه پېښه'), ('Standard normal variable', '122', 'معیاری نارمل متغیر', 'معیاري نورمال متغیر'),
           ('Standard normal distribution', '123', 'معیاری نارمل تقسیم', 'معیاري نورمال وېش'), ('Sampling survey', '152', 'نمونہ جاتی سروے', 'نمونوي سروې'), ('Sampling unit', '152', 'نمونہ جاتی اکائی', 'نمونوي واحد'), ('Sample', '152', 'نمونہ', 'نمونه'),
           ('Survey', '153', 'سروے', 'سروې'), ('Sampling frame', '153', 'نمونہ جاتی فریم', 'نمونوي چوکاټ'), ('Sample design', '153', 'نمونے کا ڈیزائن', 'د نمونې ډیزاین'), ('Survey design', '153', 'سروے کا ڈیزائن', 'د سروې ډیزاین'),
           ('Sampling', '154', 'نمونہ گیری', 'نمونه‌اخیستنه'), ('Statistic', '155', 'شماریہ', 'احصاییه'), ('Sampling error', '155', 'نمونہ جاتی خطا', 'نمونوي تېروتنه'), ('Sampling with replacement', '156', 'واپسی کے ساتھ نمونہ گیری', 'له بېرته اچولو سره نمونه‌اخیستنه'),
           ('Sampling without replacement', '157', 'واپسی کے بغیر نمونہ گیری', 'پرته له بېرته اچولو نمونه‌اخیستنه'), ('Simple random sampling', '158', 'سادہ تصادفی نمونہ گیری', 'ساده تصادفي نمونه‌اخیستنه'), ('Stratified random sampling', '160', 'طبقاتی تصادفی نمونہ گیری', 'طبقه‌ییزه تصادفي نمونه‌اخیستنه'),
           ('Systematic random sampling', '—', 'منظم تصادفی نمونہ گیری', 'منظمه تصادفي نمونه‌اخیستنه'), ('Sampling distribution', '162', 'نمونہ جاتی تقسیم', 'نمونوي وېش'), ('Standard error', '162', 'معیاری خطا', 'معیاري تېروتنه'),
           ('Statistical inference', '194', 'شماریاتی استنباط', 'احصاییوي استنتاج'), ('Significance level', '209', 'معنویت کی سطح', 'د معنی‌داریت کچه'), ('Simple hypothesis', '233', 'سادہ مفروضہ', 'ساده فرضیه')]),
    ('T', [('Type-I error', '233', 'قسم-I کی غلطی', 'د I-ډول تېروتنه'), ('Type- II error', '234', 'قسم-II کی غلطی', 'د II-ډول تېروتنه'), ('Test statistic', '235', 'جانچ کا شماریہ', 'د ازموینې احصاییه'), ('Test of significance', '235', 'معنویت کی جانچ', 'د معنی‌داریت ازموینه'),
           ('Two tailed test', '236', 'دو طرفہ جانچ', 'دوه لکۍ ازموینه'), ('Treatment', '293', 'علاج', 'درملنه'), ('Two-way classification', '268', 'دو طرفہ درجہ بندی', 'دوه اړخیزه ډلبندي')]),
    ('U', [('Unbiasedness', '197', 'غیر جانبداری', 'بې‌پلوه‌توب'), ('Ultimate class', '270', 'حتمی جماعت', 'وروستی ټولګی'), ('Ultimate class frequencies', '270', 'حتمی جماعتی تعدد', 'د وروستیو ټولګیو تکرارونه'), ('Uniformity trial', '294', 'یکسانیت کا تجربہ', 'د یووالي ازمېښت')]),
    ('W', [('Width of confidence interval', '20…', 'اعتماد کے وقفے کی چوڑائی', 'د باور د واټن پلنوالی')]),
    ('Y', [('Yule’s coefficient of association', '27…', 'یول کا تلازم کا سر', 'د یول د تړاو ضریب'), ('Yule’s correction of continuity', '28…', 'تسلسل کی یول کی اصلاح', 'د پرلپسې‌والي د یول سمون'), ('Yield', '29…', 'پیداوار', 'حاصل')]),
]
ix = index_record('stat12-index-b', IDX, 174, [339, 340], ('Index — G to Y', 'اشاریہ — G تا Y', 'لړلیک — G تر Y'))
issues = [{'id': 'stat12-p340-index-clipped', 'unit': 9, 'printedPage': 340, 'description': 'Index p340: the right-hand page numbers for Width of confidence interval (20…), Yule’s coefficient of association (27…), Yule’s correction of continuity (28…) and Yield (29…) are clipped at the scan edge, and the page number for Systematic random sampling is cut off at the top; shown as “…/—”. Index entries are skewed in the scan; numbers were matched by reading order. Uniformity trial read as 294.'}]

if __name__ == '__main__':
    save(174, [(9, ix)], issues=issues)
