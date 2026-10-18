"""PDF173 printed 337–338: Glossary (Type I error … Z-score, end); Index A–F."""
from class12_statistics_common import Builder, save

G = [
    ('Type I error', 'Rejecting the null hypothesis when it is true.', 'قسم-I کی غلطی', 'صفری مفروضے کو درست ہونے کے باوجود رد کرنا۔', 'د I-ډول تېروتنه', 'د صفري فرضیې ردول کله چې سمه وي.'),
    ('Type II error', 'Accept the null hypothesis when it is false.', 'قسم-II کی غلطی', 'صفری مفروضے کو غلط ہونے کے باوجود قبول کرنا۔', 'د II-ډول تېروتنه', 'د صفري فرضیې منل کله چې ناسمه وي.'),
    ('Unbiased estimator', 'Sample statistic that tends to target the population parameter that it is used to estimate.', 'غیر جانبدار تخمین کار', 'نمونے کا شماریہ جو اس آبادی کے پیرامیٹر کو ہدف بنانے کا رجحان رکھتا ہو جس کے تخمینے کے لیے اسے استعمال کیا جائے۔', 'بې‌پلوه اټکلوونکی', 'د نمونې احصاییه چې د هغه نفوس پارامټر ته د رسېدو میلان لري چې د اټکل لپاره یې کارول کېږي.'),
    ('Uniform distribution', 'Probability distribution in which every value of the random variable is equally likely.', 'یکساں تقسیم', 'احتمالی تقسیم جس میں تصادفی متغیر کی ہر قیمت یکساں ممکن ہو۔', 'یونیفورم وېش', 'احتمالي وېش چې پکې د تصادفي متغیر هر قیمت یو شان امکان لري.'),
    ('Variable', 'A characteristic under study or investigation that assumes different values for different elements.', 'متغیر', 'زیرِ مطالعہ یا زیرِ تحقیق خصوصیت جو مختلف عناصر کے لیے مختلف قیمتیں لیتی ہے۔', 'متغیر', 'تر څېړنې لاندې ځانګړنه چې د بېلابېلو عناصرو لپاره بېلابېل قیمتونه اخلي.'),
    ('Variance between samples', 'In analysis of variance, the variation among the different samples.', 'نمونوں کے درمیان تغیر', 'تجزیۂ تغیر میں مختلف نمونوں کے درمیان تغیر۔', 'د نمونو ترمنځ واریانس', 'د واریانس په تحلیل کې د بېلابېلو نمونو ترمنځ تغیر.'),
    ('Variation within samples', 'In analysis of variance, the variation that is due to chance.', 'نمونوں کے اندر تغیر', 'تجزیۂ تغیر میں وہ تغیر جو اتفاق کی وجہ سے ہو۔', 'د نمونو دننه تغیر', 'د واریانس په تحلیل کې هغه تغیر چې د تصادف له امله وي.'),
    ('Z-score', 'Number of standard deviations that a given value is above or below the mean.', 'Z-اسکور', 'معیاری انحرافات کی وہ تعداد جتنی کوئی دی گئی قیمت اوسط سے اوپر یا نیچے ہو۔', 'Z-نمره', 'د معیاري انحرافونو هغه شمېر چې یو ورکړل شوی قیمت له منځني پورته یا لاندې وي.'),
]
b = Builder()
b.group('list', [(f'{e}: {d}', f'{u} ({e}): {ud}', f'{p} ({e}): {pd}') for e, d, u, ud, p, pd in G])
gl = b.build('stat12-glossary-d', 'Glossary — Type I error to Z-score', 'فرہنگ — قسم-I کی غلطی تا Z-اسکور', 'وییپانګه — د I-ډول تېروتنه تر Z-نمرې', 173, [337])

# Index entries exactly as printed (term, printed page); localised terms in Urdu / Pashto.
IDX = [
    ('A', [('Alternative hypothesis', '233', 'متبادل مفروضہ', 'بدیله فرضیه'), ('Acceptance region', '235', 'قبولیت کا علاقہ', 'د منلو سیمه'), ('Attributes', '267', 'صفات', 'صفتونه'),
           ('Association of attributes', '270', 'صفات کا تلازم', 'د صفتونو تړاو'), ('Analysis of variance', '298', 'تجزیۂ تغیر', 'د واریانس تحلیل'), ('ANOVA table', '301', 'ANOVA جدول', 'د ANOVA جدول')]),
    ('B', [('Bivariate probability distribution', '56', 'دو متغیری احتمالی تقسیم', 'دوه‌متغیره احتمالي وېش'), ('Bivariate probability function', '57', 'دو متغیری احتمالی فعل', 'دوه‌متغیره احتمالي تابع'),
           ('Bernoulli trial', '79', 'برنولی تجربہ', 'د برنولي ازمېښت'), ('Binomial experiment', '82', 'دو رقمی تجربہ', 'دوه‌حدي تجربه'), ('Binomial probability mass function', '82', 'دو رقمی احتمالی کمیتی فعل', 'دوه‌حدي احتمالي کتلوي تابع'),
           ('Binomial frequency distribution', '93', 'دو رقمی تعددی تقسیم', 'دوه‌حدي تکراري وېش'), ('Bias', '156', 'جانبداری', 'پلوي'), ('Block', '294', 'بلاک', 'بلاک')]),
    ('C', [('Combination', '04', 'توافیق', 'ترکیب'), ('Compound event', '07', 'مرکب واقعہ', 'مرکبه پېښه'), ('Complementary event', '07', 'تکمیلی واقعہ', 'متممه پېښه'),
           ('Conditional probability', '21', 'مشروط احتمال', 'شرطي احتمال'), ('Continuous random variable', '32', 'مسلسل تصادفی متغیر', 'پرلپسې تصادفي متغیر'),
           ('Continuous uniform distribution', '117', 'مسلسل یکساں تقسیم', 'پرلپسې یونیفورم وېش'), ('Census', '154', 'مردم شماری', 'سرشمېرنه'), ('Confidence interval', '209', 'اعتماد کا وقفہ', 'د باور واټن'),
           ('Confidence limits', '209', 'اعتماد کی حدیں', 'د باور حدونه'), ('Confidence region', '209', 'اعتماد کا علاقہ', 'د باور سیمه'), ('Confidence coefficient', '209', 'اعتماد کا سر', 'د باور ضریب'),
           ('Confidence level', '209', 'اعتماد کی سطح', 'د باور کچه'), ('Composite hypothesis', '233', 'مرکب مفروضہ', 'مرکبه فرضیه'), ('Class Frequency', '268', 'جماعتی تعدد', 'د ټولګي تکرار'),
           ('Classification of attributes', '268', 'صفات کی درجہ بندی', 'د صفتونو ډلبندي'), ('Contingency table', '275', 'اتفاقی جدول', 'احتمالي جدول'), ('Coefficient of contingency', '282', 'اتفاقیت کا سر', 'د احتمالیت ضریب'),
           ('Completely randomized design', '296', 'مکمل تصادفی ڈیزائن', 'بشپړ تصادفي ډیزاین')]),
    ('D', [('Dependent events', '07', 'منحصر واقعات', 'تړلې پېښې'), ('Discrete random variable', '32', 'غیر مسلسل تصادفی متغیر', 'ناپرلپسې تصادفي متغیر'), ('Discrete uniform distribution', '71', 'غیر مسلسل یکساں تقسیم', 'ناپرلپسې یونیفورم وېش'),
           ('Degrees of freedom', '213', 'درجاتِ آزادی', 'د ازادۍ درجې'), ('Dichotomy classification', '268', 'دو حصوں میں درجہ بندی', 'دوه‌ګونې ډلبندي')]),
    ('E', [('Event', '06', 'واقعہ', 'پېښه'), ('Equally likely Events', '07', 'یکساں ممکن واقعات', 'یو شان امکان لرونکې پېښې'), ('Exhaustive events', '07', 'جامع واقعات', 'جامعې پېښې'), ('Estimation', '194', 'تخمین', 'اټکل کول'),
           ('Estimator', '195', 'تخمین کار', 'اټکلوونکی'), ('Estimate', '195', 'تخمینہ', 'اټکل'), ('Efficiency', '204', 'کارکردگی', 'موثریت'), ('Experimental design', '293', 'تجرباتی ڈیزائن', 'تجربوي ډیزاین'),
           ('Experimental material', '293', 'تجرباتی مواد', 'تجربوي توکي'), ('Experimental unit', '293', 'تجرباتی اکائی', 'تجربوي واحد'), ('Extraneous factor', '294', 'خارجی عامل', 'بهرنی عامل'), ('Experimental error', '294', 'تجرباتی خطا', 'تجربوي تېروتنه')]),
    ('F', [('Factorial', '02', 'فیکٹوریل', 'فکتوریل'), ('Finite population', '152', 'متناہی آبادی', 'محدود نفوس')]),
]


def index_record(rec_id, groups, pdf, printed, title):
    x = Builder()
    if pdf == 173:
        x.h('INDEX', 'اشاریہ', 'لړلیک')
    rows = {'en': [], 'ur': [], 'ps': []}
    for letter, items in groups:
        for i, (en, pg, ur, ps) in enumerate(items):
            L = letter if i == 0 else ''
            rows['en'].append([L, en, pg]); rows['ur'].append([L, f'{ur} ({en})', pg]); rows['ps'].append([L, f'{ps} ({en})', pg])
    x.table(rec_id + '-t', ['', 'Term', 'Page'], rows['en'], ['', 'اصطلاح', 'صفحہ'], ['', 'اصطلاح', 'مخ'], rows['ur'], rows['ps'])
    return x.build(rec_id, *title, pdf, printed)


ix = index_record('stat12-index-a', IDX, 173, [338], ('Index — A to F', 'اشاریہ — A تا F', 'لړلیک — A تر F'))

if __name__ == '__main__':
    save(173, [(9, gl), (9, ix)])
