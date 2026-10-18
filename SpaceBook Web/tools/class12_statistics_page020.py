"""PDF20 printed 31–32: Unit 2 opener (learning outcomes), 2.1 random variable, 2.1.1–2.1.2, 2.2 opening."""
from class12_statistics_common import Builder, save

o = Builder()
o.h('Unit - 02', 'یونٹ - 02', 'واحد - 02')
o.h('Random Variables and Probability Distributions', 'تصادفی متغیرات اور احتمالی تقسیمیں', 'تصادفي متغیرونه او احتمالي وېشونه')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Define random variable and differentiate between discrete and continuous random variables with real life examples.', 'تصادفی متغیر کی تعریف کریں اور حقیقی زندگی کی مثالوں کے ساتھ منفصل اور مسلسل تصادفی متغیرات میں فرق کریں۔', 'تصادفي متغیر تعریف کړي او د ورځني ژوند له بېلګو سره د منفصلو او متصلو تصادفي متغیرونو ترمنځ توپیر وکړي.'),
    ('Describe probability distribution of a discrete random variable', 'منفصل تصادفی متغیر کی احتمالی تقسیم بیان کریں', 'د منفصل تصادفي متغیر احتمالي وېش بیان کړي'),
    ('Find probability distribution of a discrete random variable', 'منفصل تصادفی متغیر کی احتمالی تقسیم معلوم کریں', 'د منفصل تصادفي متغیر احتمالي وېش پیدا کړي'),
    ('Recognize probability mass function and its properties', 'احتمالی کمیتی تفاعل (probability mass function) اور اس کی خصوصیات پہچانیں', 'د احتمال کتلوي تابع (probability mass function) او ځانګړنې یې وپېژني'),
    ('Describe and find the probability distribution of a function of discrete random variable.', 'منفصل تصادفی متغیر کے کسی تفاعل کی احتمالی تقسیم بیان کریں اور معلوم کریں۔', 'د منفصل تصادفي متغیر د یوې تابع احتمالي وېش بیان او پیدا کړي.'),
    ('Define and find the expected value of a discrete random variable.', 'منفصل تصادفی متغیر کی متوقع قیمت کی تعریف کریں اور اسے معلوم کریں۔', 'د منفصل تصادفي متغیر تمه شوی قیمت تعریف او پیدا کړي.'),
    ('Find the expected value of a linear function of a discrete random variable.', 'منفصل تصادفی متغیر کے خطی تفاعل کی متوقع قیمت معلوم کریں۔', 'د منفصل تصادفي متغیر د خطي تابع تمه شوی قیمت پیدا کړي.'),
    ('Describe and verify properties of expected value of a discrete random variable.', 'منفصل تصادفی متغیر کی متوقع قیمت کی خصوصیات بیان کریں اور ان کی تصدیق کریں۔', 'د منفصل تصادفي متغیر د تمه شوي قیمت ځانګړنې بیان او تایید کړي.'),
    ('Apply the properties of expected value of a discrete random variable.', 'منفصل تصادفی متغیر کی متوقع قیمت کی خصوصیات کا اطلاق کریں۔', 'د منفصل تصادفي متغیر د تمه شوي قیمت ځانګړنې وکاروي.'),
    ('Define variance and standard deviation of a discrete random variable', 'منفصل تصادفی متغیر کے تغیر (variance) اور معیاری انحراف کی تعریف کریں', 'د منفصل تصادفي متغیر واریانس او معیاري انحراف تعریف کړي'),
    ('Find mean, variance and standard deviation of a discrete random variable.', 'منفصل تصادفی متغیر کا اوسط، تغیر اور معیاری انحراف معلوم کریں۔', 'د منفصل تصادفي متغیر منځنی، واریانس او معیاري انحراف پیدا کړي.'),
    ('Define and find variance and standard deviation of a linear function of a discrete random variable.', 'منفصل تصادفی متغیر کے خطی تفاعل کے تغیر اور معیاری انحراف کی تعریف کریں اور انہیں معلوم کریں۔', 'د منفصل تصادفي متغیر د خطي تابع واریانس او معیاري انحراف تعریف او پیدا کړي.'),
    ('Describe, verify and apply the properties of variance and standard deviation of a discrete random variable.', 'منفصل تصادفی متغیر کے تغیر اور معیاری انحراف کی خصوصیات بیان کریں، ان کی تصدیق کریں اور ان کا اطلاق کریں۔', 'د منفصل تصادفي متغیر د واریانس او معیاري انحراف ځانګړنې بیان، تایید او وکاروي.'),
    ('Define probability distribution and probability density function of a continuous random variable.', 'مسلسل تصادفی متغیر کی احتمالی تقسیم اور احتمالی کثافتی تفاعل کی تعریف کریں۔', 'د متصل تصادفي متغیر احتمالي وېش او د احتمال کثافت تابع تعریف کړي.'),
    ('Define and expected value, variance and standard deviation of a continuous random variable.', 'مسلسل تصادفی متغیر کی متوقع قیمت، تغیر اور معیاری انحراف کی تعریف کریں۔', 'د متصل تصادفي متغیر تمه شوی قیمت، واریانس او معیاري انحراف تعریف کړي.'),
    ('Describe the properties about the expected value and variance for the sum/difference of two independent random variable x and y also apply these properties to solve real life problems.', 'دو آزاد تصادفی متغیرات x اور y کے مجموعے/فرق کی متوقع قیمت اور تغیر کی خصوصیات بیان کریں اور حقیقی زندگی کے مسائل حل کرنے میں ان کا اطلاق کریں۔', 'د دوو خپلواکو تصادفي متغیرونو x او y د مجموعې/توپیر د تمه شوي قیمت او واریانس ځانګړنې بیان کړي او د ورځني ژوند د ستونزو په حل کې یې وکاروي.'),
])
opening = o.build('stat12-u2-opening', 'Unit 2 — Learning outcomes', 'یونٹ 2 — حاصلاتِ تعلم', 'واحد 2 — د زده کړې پایلې', 20, [31])

b = Builder()
b.h('2.1 Random variable', '2.1 تصادفی متغیر', '2.1 تصادفي متغیر')
b.p('Probability distributions, which shall be studied in the coming units, are very easy methods for calculation of probabilities in respective situations but they need quantification of the outcomes of a random experiment. For this purpose, sample space of a random experiment is expressed in numerical form according to a characteristic of interest. This numerical presentation of the sample space is termed as random variable (r.v). It is denoted by English letters X, Y, Z or $X_1, X_2, X_3\\ldots$',
    'احتمالی تقسیمیں، جو آنے والے یونٹوں میں پڑھی جائیں گی، متعلقہ حالات میں احتمالات معلوم کرنے کے بہت آسان طریقے ہیں، لیکن انہیں تصادفی تجربے کے نتائج کو عددی صورت دینے کی ضرورت ہوتی ہے۔ اس مقصد کے لیے تصادفی تجربے کی نمونہ فضا کو دلچسپی کی کسی خاصیت کے مطابق عددی شکل میں ظاہر کیا جاتا ہے۔ نمونہ فضا کی اس عددی پیشکش کو تصادفی متغیر (r.v) کہتے ہیں۔ اسے انگریزی حروف X، Y، Z یا $X_1, X_2, X_3\\ldots$ سے ظاہر کرتے ہیں۔',
    'احتمالي وېشونه چې په راتلونکو واحدونو کې به ولوستل شي، په اړوندو حالتونو کې د احتمالونو د محاسبې ډېرې اسانه طریقې دي، خو د تصادفي تجربې د پایلو شمېریز کولو ته اړتیا لري. د دې لپاره د تصادفي تجربې نمونوي فضا د یوې ګټورې ځانګړنې له مخې په شمېریزه بڼه ښودل کېږي. د نمونوي فضا دې شمېریز وړاندې کولو ته تصادفي متغیر (r.v) وایي. په انګلیسي تورو X، Y، Z یا $X_1, X_2, X_3\\ldots$ ښودل کېږي.')
b.h('2.1.1 Definition of random variable', '2.1.1 تصادفی متغیر کی تعریف', '2.1.1 د تصادفي متغیر تعریف')
b.p('A random variable is a numerical description of a random experiment.', 'تصادفی متغیر کسی تصادفی تجربے کی عددی وضاحت ہے۔', 'تصادفي متغیر د یوې تصادفي تجربې شمېریز تشریح ده.')
b.h('2.1.2 Types of random variable', '2.1.2 تصادفی متغیر کی اقسام', '2.1.2 د تصادفي متغیر ډولونه')
b.p('Random variable can be classified as follow:', 'تصادفی متغیر کی درجہ بندی یوں کی جا سکتی ہے:', 'تصادفي متغیر داسې ډلبندي کېدای شي:')
b.h('(i) Discrete random variable', '(i) منفصل تصادفی متغیر', '(i) منفصل تصادفي متغیر')
b.p('A variable which takes jumping values or isolated values is called discrete random variable. For example, number of rotten tomatoes in a crate, number of children per house in a street etc. Its probability distribution is called discrete probability distribution.',
    'وہ متغیر جو جست والی یا الگ تھلگ قیمتیں لیتا ہے، منفصل تصادفی متغیر کہلاتا ہے۔ مثلاً کسی کریٹ میں گلے سڑے ٹماٹروں کی تعداد، کسی گلی میں فی گھر بچوں کی تعداد وغیرہ۔ اس کی احتمالی تقسیم کو منفصل احتمالی تقسیم کہتے ہیں۔',
    'هغه متغیر چې ټوپ وهونکي یا جلا قیمتونه اخلي، منفصل تصادفي متغیر بلل کېږي. د بېلګې په توګه په یوه کریټ کې د خرابو رومیانو شمېر، په یوه کوڅه کې په هر کور کې د ماشومانو شمېر او نور. احتمالي وېش یې منفصل احتمالي وېش بلل کېږي.')
b.h('(ii) Continuous random variable', '(ii) مسلسل تصادفی متغیر', '(ii) متصل تصادفي متغیر')
b.p('A variable which takes any value between two limits, $[a,b]$, $a<b$, is called continuous random variable. For example, life of a mobile set, speed of a car etc. It is written as $a\\le X\\le b$. Its probability distribution is called continuous probability distribution.',
    'وہ متغیر جو دو حدوں $[a,b]$، $a<b$ کے درمیان کوئی بھی قیمت لے، مسلسل تصادفی متغیر کہلاتا ہے۔ مثلاً موبائل سیٹ کی عمر، گاڑی کی رفتار وغیرہ۔ اسے $a\\le X\\le b$ لکھا جاتا ہے۔ اس کی احتمالی تقسیم کو مسلسل احتمالی تقسیم کہتے ہیں۔',
    'هغه متغیر چې د دوو حدونو $[a,b]$، $a<b$ ترمنځ هر قیمت اخلي، متصل تصادفي متغیر بلل کېږي. د بېلګې په توګه د موبایل عمر، د موټر سرعت او نور. داسې لیکل کېږي $a\\le X\\le b$. احتمالي وېش یې متصل احتمالي وېش بلل کېږي.')
b.h('2.2 Probability distribution of a discrete random variable', '2.2 منفصل تصادفی متغیر کی احتمالی تقسیم', '2.2 د منفصل تصادفي متغیر احتمالي وېش')
b.p('If all possible values of a random variable along with their respective probabilities are shown in tabular form and sum of probabilities is equal to one, then it is called probability distribution. For example, discrete probability distribution of X is presented as',
    'اگر کسی تصادفی متغیر کی تمام ممکنہ قیمتیں ان کے متعلقہ احتمالات کے ساتھ جدولی شکل میں دکھائی جائیں اور احتمالات کا مجموعہ ایک کے برابر ہو، تو اسے احتمالی تقسیم کہتے ہیں۔ مثلاً X کی منفصل احتمالی تقسیم یوں پیش کی جاتی ہے',
    'که د یوه تصادفي متغیر ټول شوني قیمتونه له خپلو اړوندو احتمالونو سره په جدولي بڼه وښودل شي او د احتمالونو مجموعه له یو سره برابره وي، نو احتمالي وېش بلل کېږي. د بېلګې په توګه د X منفصل احتمالي وېش داسې وړاندې کېږي')
rv = b.build('stat12-p020-random-variable', '2.1 Random variable and 2.2 discrete probability distribution', '2.1 تصادفی متغیر اور 2.2 منفصل احتمالی تقسیم', '2.1 تصادفي متغیر او 2.2 منفصل احتمالي وېش', 20, [32])

if __name__ == '__main__':
    save(20, [(2, opening), (2, rv)])
