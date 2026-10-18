"""PDF60 printed 111–112: Exercise 3.2 (vii)–(x), 3.3 MCQs (i)–(x), questions 3.4–3.6."""
from class12_statistics_common import Builder, save

B = '______'
b = Builder()
b.group('lines', [
    (f'(vii) Bernoulli random variable takes only two values i.e. {B}.', f'(vii) برنولی تصادفی متغیر صرف دو قیمتیں لیتا ہے یعنی {B}۔', f'(vii) د برنولي تصادفي متغیر یوازې دوه قیمتونه اخلي یعنې {B}.'),
    (f'(viii) Pairs of random digits are called {B}.', f'(viii) تصادفی ہندسوں کے جوڑوں کو {B} کہتے ہیں۔', f'(viii) د تصادفي رقمونو جوړو ته {B} وایي.'),
    (f'(ix) The successive trails in a Binomial experiment are {B}.', f'(ix) دو رقمی تجربے میں یکے بعد دیگرے آزمائشیں {B} ہوتی ہیں۔', f'(ix) په بینومیل تجربه کې پرله پسې ازمېښتونه {B} دي.'),
    (f'(x) The probability of success {B} from trail to trail in a hypergeometric experiment.', f'(x) ہائپر جیومیٹرک تجربے میں کامیابی کا احتمال ایک آزمائش سے دوسری تک {B}۔', f'(x) په هایپرجیومټریک تجربه کې د بریا احتمال له یوه ازمېښت څخه تر بل پورې {B}.'),
])
b.h('3.3 Choose the correct answer.', '3.3 درست جواب منتخب کریں۔', '3.3 سم ځواب وټاکئ.')
b.mcq('i)', ('The Binominal distribution was introduced by', 'دو رقمی تقسیم متعارف کرائی', 'بینومیل وېش معرفي کړ'),
      ['Simon Denis Poisson', 'Jacob Bernoulli', 'Abraham De Moirés', 'R.A. Fisher'])
b.mcq('ii)', ('In a Bernoulli trail the probability of success is denoted by', 'برنولی آزمائش میں کامیابی کا احتمال ظاہر کیا جاتا ہے', 'د برنولي په ازمېښت کې د بریا احتمال ښودل کېږي په'), ['$q$', '$1-p$', '$p$', '$1-q$'])
b.mcq('iii)', ('The mean of the Binomial distribution is', 'دو رقمی تقسیم کا اوسط ہے', 'د بینومیل وېش منځنی دی'), ['$\\sqrt{np}$', '$npq$', '$np$', '$\\sqrt{npq}$'])
b.mcq('iv)', ('If X has a Binomial distribution with $p=\\frac{2}{3}$ and n = 9, then its mean will be equal to', 'اگر X کی دو رقمی تقسیم ہو جس میں $p=\\frac{2}{3}$ اور n = 9 ہو تو اس کا اوسط برابر ہوگا', 'که X بینومیل وېش ولري چې $p=\\frac{2}{3}$ او n = 9 وي، نو منځنی یې برابر دی له'), ['2', '3', '5', '6'])
b.mcq('v)', ('Hypergeometric probability distribution has parameters', 'ہائپر جیومیٹرک احتمالی تقسیم کے پیرامیٹر ہیں', 'هایپرجیومټریک احتمالي وېش پارامټرونه لري'), ['2', '3', '4', '5'])
b.mcq('vi)', ('The Binomial distribution is the', 'دو رقمی تقسیم ہے', 'بینومیل وېش دی'),
      [('equal probability distribution', 'مساوی احتمالی تقسیم', 'مساوي احتمالي وېش'), ('individual probability distribution', 'انفرادی احتمالی تقسیم', 'انفرادي احتمالي وېش'), ('discrete probability distribution', 'منفصل احتمالی تقسیم', 'منفصل احتمالي وېش'), ('continuous probability distribution', 'مسلسل احتمالی تقسیم', 'متصل احتمالي وېش')])
b.mcq('vii)', ('If n = 60, p = 0.7 for a Binomial distribution then its standard deviation is equal to', 'اگر دو رقمی تقسیم میں n = 60، p = 0.7 ہو تو اس کا معیاری انحراف برابر ہے', 'که د بینومیل وېش لپاره n = 60، p = 0.7 وي، نو معیاري انحراف یې برابر دی له'), ['42', '6.48', '18', '3.55'])
b.mcq('viii)', ('If a fair coin is tossed once, the value of p will be', 'اگر ایک منصفانہ سکہ ایک بار اچھالا جائے تو p کی قیمت ہوگی', 'که یوه عادلانه سکه یو ځل واچول شي، د p قیمت به وي'), ['$\\frac{1}{2}$', '$\\frac{1}{3}$', '$\\frac{1}{4}$', '$\\frac{1}{1}$'])
b.mcq('ix)', ('The number of parameters in a Binomial distribution are', 'دو رقمی تقسیم میں پیرامیٹرز کی تعداد ہے', 'په بینومیل وېش کې د پارامټرونو شمېر دی'),
      [('one', 'ایک', 'یو'), ('two', 'دو', 'دوه'), ('three', 'تین', 'درې'), ('four', 'چار', 'څلور')])
b.mcq('x)', ('The range of uniform distribution is equal to;', 'یکساں تقسیم کی حد برابر ہے؛', 'د یونیفارم وېش حد برابر دی له؛'), ['$-\\infty$ to 0', '$0,1,\\ldots,N$', '0 to $\\infty$', '$1,2,3,\\ldots,N$'])
b.group('lines', [
    ('3.4 Describe in brief the discrete uniform probability distribution.', '3.4 منفصل یکساں احتمالی تقسیم مختصراً بیان کریں۔', '3.4 منفصل یونیفارم احتمالي وېش په لنډه توګه بیان کړئ.'),
    ('3.5 What do you know about random digits, random numbers, random number generator and random number table?', '3.5 تصادفی ہندسوں، تصادفی اعداد، تصادفی عدد پیدا کرنے والے اور تصادفی اعداد کے جدول کے بارے میں آپ کیا جانتے ہیں؟', '3.5 د تصادفي رقمونو، تصادفي عددونو، د تصادفي عدد جوړوونکي او د تصادفي عددونو د جدول په اړه څه پوهېږئ؟'),
    ('3.6 Explain how you would select a random sample of 10 colleges form a list of 206 colleges by using a random number table.', '3.6 وضاحت کریں کہ آپ تصادفی اعداد کے جدول کی مدد سے 206 کالجوں کی فہرست سے 10 کالجوں کا تصادفی نمونہ کیسے منتخب کریں گے۔', '3.6 تشریح کړئ چې تاسو به د تصادفي عددونو د جدول په کارولو سره د 206 کالجونو له لیست څخه د 10 کالجونو تصادفي نمونه څنګه وټاکئ.'),
])
rec = b.build('stat12-u3-exercise-b', 'Unit 3 Exercise — 3.2 (vii)–(x), 3.3 and 3.4–3.6', 'یونٹ 3 مشق — 3.2 (vii)–(x)، 3.3 اور 3.4–3.6', 'واحد 3 تمرین — 3.2 (vii)–(x)، 3.3 او 3.4–3.6', 60, [111, 112])
issues = [{'id': 'stat12-p111-binominal-moires', 'unit': 3, 'printedPage': 111, 'description': 'MCQ 3.3(i) prints “Binominal” and “Abraham De Moirés” (for Binomial / De Moivre); printed spellings retained.'}]

if __name__ == '__main__':
    save(60, [(3, rec)], issues=issues)
