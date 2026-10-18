"""PDF149 printed 289–290: Unit 8 Exercise questions 8.10–8.18 (data tables)."""
from class12_statistics_common import Builder, save

b = Builder()


def tab(tid, heads, labels, data):
    """heads/labels: lists of (en, ur, ps); data: numeric rows (language-neutral)."""
    H = [[h[i] for h in heads] for i in range(3)]
    R = [[[labels[r][i]] + data[r] for r in range(len(data))] for i in range(3)]
    b.table(tid, H[0], R[0], H[1], H[2], R[1], R[2])


ATT = ('Attributes', 'صفات', 'صفتونه')
b.group('lines', [
    ('8.10 Discuss the association when (AB) = 256, (αB) = 768, (Aβ) = 48, (αβ) = 144.', '8.10 تلازم پر بحث کریں جب (AB) = 256، (αB) = 768، (Aβ) = 48، (αβ) = 144۔', '8.10 پر تړاو بحث وکړئ کله چې (AB) = 256، (αB) = 768، (Aβ) = 48، (αβ) = 144.'),
    ('8.11 Do you find any association between the tempers of brothers and sisters from the data given below?', '8.11 کیا آپ نیچے دیے گئے مواد سے بھائیوں اور بہنوں کے مزاج کے درمیان کوئی تلازم پاتے ہیں؟', '8.11 آیا له لاندې ورکړل شویو معلوماتو د وروڼو او خویندو د مزاج ترمنځ کوم تړاو مومئ؟'),
    ('Good natured brothers and good natured sisters = 1230', 'خوش مزاج بھائی اور خوش مزاج بہنیں = 1230', 'ښه مزاجه وروڼه او ښه مزاجه خویندې = 1230'),
    ('Good natured brothers and sullen sisters = 850', 'خوش مزاج بھائی اور ترش مزاج بہنیں = 850', 'ښه مزاجه وروڼه او تریو مزاجه خویندې = 850'),
    ('Sullen brothers and good nature sisters = 530', 'ترش مزاج بھائی اور خوش مزاج بہنیں = 530', 'تریو مزاجه وروڼه او ښه مزاجه خویندې = 530'),
    ('Sullen brothers and sullen sisters = 980', 'ترش مزاج بھائی اور ترش مزاج بہنیں = 980', 'تریو مزاجه وروڼه او تریو مزاجه خویندې = 980'),
    ('8.12 Investigate the association between intelligence in fathers and sons from the following data', '8.12 درج ذیل مواد سے باپوں اور بیٹوں میں ذہانت کے درمیان تلازم کی تحقیق کریں', '8.12 له لاندې معلوماتو د پلرونو او زامنو په هوښیارتیا کې تړاو وڅېړئ'),
])
tab('stat12-t-q8-12', [ATT, ('intelligent sons', 'ذہین بیٹے', 'هوښیار زامن'), ('dull sons', 'کند ذہن بیٹے', 'کم‌ذهنه زامن')],
    [('intelligent fathers', 'ذہین باپ', 'هوښیار پلرونه'), ('dull fathers', 'کند ذہن باپ', 'کم‌ذهنه پلرونه')], [['240', '80'], ['90', '570']])
b.group('lines', [
    ('8.13 Can vaccination be regarded as a preventive measure for small-pox from the data given below?', '8.13 کیا نیچے دیے گئے مواد سے ویکسین کو چیچک کے لیے حفاظتی اقدام سمجھا جا سکتا ہے؟', '8.13 آیا له لاندې معلوماتو واکسین د چیچک لپاره مخنیوونکی اقدام ګڼل کېدای شي؟'),
    ('Of 1482 persons in a locality exposed to smell-pox, 368 in all were attacked. Of 1482 persons, 343 had been vaccinated and of these 35 were attacked.', 'ایک علاقے میں چیچک کا سامنا کرنے والے 1482 افراد میں سے کل 368 متاثر ہوئے۔ 1482 افراد میں سے 343 کو ویکسین لگی تھی اور ان میں سے 35 متاثر ہوئے۔', 'په یوه سیمه کې له چیچک سره مخ شویو 1482 کسانو څخه ټول 368 اخته شول. له 1482 کسانو 343 واکسین شوي وو او له دوی 35 اخته شول.'),
    ('8.14 Consider the data given in the following 2 × 2 contingency table and find out whether vaccination is effective in preventing the attack of B hepatitis disease?', '8.14 درج ذیل 2 × 2 اتفاقی جدول میں دیے گئے مواد پر غور کریں اور معلوم کریں کہ کیا ویکسین ہیپاٹائٹس B کی بیماری کے حملے کو روکنے میں مؤثر ہے؟', '8.14 په لاندې 2 × 2 احتمالي جدول کې ورکړل شوي معلومات په پام کې ونیسئ او معلوم کړئ چې آیا واکسین د B هیپاټایټس ناروغۍ د حملې په مخنیوي کې اغېزمن دی؟'),
])
tab('stat12-t-q8-14', [ATT, ('attacked', 'متاثر', 'اخته'), ('not attacked', 'غیر متاثر', 'نا اخته')],
    [('vaccinated', 'ویکسین شدہ', 'واکسین شوي'), ('not vaccinated', 'غیر ویکسین شدہ', 'نا واکسین شوي')], [['11', '538'], ['70', '464']])
b.p('Test by applying $\\chi^2$-test at 1% level of significance.', '1% معنویت کی سطح پر $\\chi^2$-جانچ لاگو کر کے جانچ کریں۔', 'د 1% معنی‌داریت په کچه د $\\chi^2$-ازموینې په پلي کولو وازموئ.')
b.p('8.15 A random sample of size 1024 was classified according to gender and seat belt usage as shown below.', '8.15 1024 سائز کے تصادفی نمونے کو جنس اور سیٹ بیلٹ کے استعمال کے مطابق درجہ بند کیا گیا جیسا کہ نیچے دکھایا گیا ہے۔', '8.15 د 1024 اندازې تصادفي نمونه د جنس او د سیټ بېلټ د کارولو له مخې ډلبندي شوه لکه لاندې ښودل شوي.')
tab('stat12-t-q8-15', [ATT, ('use seat belt', 'سیٹ بیلٹ استعمال کرتے ہیں', 'سیټ بېلټ کاروي'), ('don’t use seat belt', 'سیٹ بیلٹ استعمال نہیں کرتے', 'سیټ بېلټ نه کاروي')],
    [('male', 'مرد', 'نارینه'), ('female', 'عورت', 'ښځینه')], [['272', '192'], ['276', '284']])
b.p('Do the data suggest an association between gender and seat belt used? Use α = 0.01', 'کیا مواد جنس اور سیٹ بیلٹ کے استعمال کے درمیان تلازم ظاہر کرتا ہے؟ α = 0.01 استعمال کریں', 'آیا معلومات د جنس او د سیټ بېلټ د کارولو ترمنځ تړاو ښيي؟ α = 0.01 وکاروئ')
b.p('8.16 Perform chi square test of independence to decide whether smoking is a cause of lung cancer by considering the date given in the following 2×2 category table.', '8.16 درج ذیل 2×2 زمرہ جدول میں دیے گئے مواد پر غور کر کے آزادی کی کائی مربع جانچ کریں تاکہ فیصلہ ہو سکے کہ کیا تمباکو نوشی پھیپھڑوں کے سرطان کی وجہ ہے۔', '8.16 په لاندې 2×2 کټګوري جدول کې د ورکړل شویو معلوماتو په پام کې نیولو د خپلواکۍ د کای مربع ازموینه ترسره کړئ ترڅو پرېکړه وشي چې آیا سګرټ څکول د سږو د سرطان لامل دی.')
tab('stat12-t-q8-16', [ATT, ('cancer', 'سرطان', 'سرطان'), ('no cancer', 'سرطان نہیں', 'سرطان نشته')],
    [('smoking', 'تمباکو نوشی', 'سګرټ څکول'), ('not smoking', 'تمباکو نوشی نہیں', 'سګرټ نه څکول')], [['75', '34'], ['28', '112']])
b.p('Test at 5% level of significance.', '5% معنویت کی سطح پر جانچ کریں۔', 'د 5% معنی‌داریت په کچه وازموئ.')
b.group('lines', [
    ('8.17 Explain the following:', '8.17 درج ذیل کی وضاحت کریں:', '8.17 لاندې تشریح کړئ:'),
    ('i. Manifold classification', 'i. متعدد درجہ بندی', 'i. ګڼ‌ګونې ډلبندي'),
    ('ii. (r × c) contingency table', 'ii. (r × c) اتفاقی جدول', 'ii. (r × c) احتمالي جدول'),
    ('iii. Chi-square distribution.', 'iii. کائی مربع تقسیم۔', 'iii. د کای مربع وېش.'),
    ('8.18 Find the chi-square to test the hypothesis that there is association between height of fathers and height of sons (at α = 0.01):', '8.18 اس مفروضے کی جانچ کے لیے کائی مربع معلوم کریں کہ باپوں کے قد اور بیٹوں کے قد کے درمیان تلازم ہے (α = 0.01 پر):', '8.18 د دې فرضیې د ازموینې لپاره کای مربع پیدا کړئ چې د پلرونو د قد او د زامنو د قد ترمنځ تړاو شته (په α = 0.01):'),
])
tab('stat12-t-q8-18', [('Sons \\ Fathers', 'بیٹے \\ باپ', 'زامن \\ پلرونه'), ('very tall', 'بہت لمبے', 'ډېر لوړ'), ('tall', 'لمبے', 'لوړ'), ('short', 'چھوٹے', 'ټیټ')],
    [('very tall', 'بہت لمبے', 'ډېر لوړ'), ('tall', 'لمبے', 'لوړ'), ('short', 'چھوٹے', 'ټیټ')], [['600', '280', '300'], ['400', '700', '400'], ['250', '400', '800']])
ex = b.build('stat12-u8-exercise-c', 'Unit 8 Exercise — 8.10 to 8.18', 'یونٹ 8 مشق — 8.10 تا 8.18', 'واحد 8 تمرین — 8.10 تر 8.18', 149, [289, 290])
issues = [{'id': 'stat12-p289-290-typos', 'unit': 8, 'printedPage': 290, 'description': 'Exercise prints “smell-pox” (8.13), “good nature sisters” (8.11), “seat belt used” (8.15) and “the date given” (8.16, for data). Printed wording retained.'}]

if __name__ == '__main__':
    save(149, [(8, ex)], issues=issues)
