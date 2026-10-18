"""PDF59 printed 109–110: Unit 3 key points; Exercise 3.1 (T/F) and 3.2 (i)–(vi)."""
from class12_statistics_common import Builder, save

k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.p('■ A probability function defined as', '■ اس طرح متعین احتمالی تفاعل', '■ هغه احتمالي تابع چې داسې تعریف شوې')
k.eq(r'p(x)=\left\{\begin{matrix}\frac{1}{N}, & x=1,2,\cdots,N\\ 0, & \textit{otherwise}\end{matrix}\right.')
k.p('is called discrete uniform probability function', 'منفصل یکساں احتمالی تفاعل کہلاتا ہے', 'منفصل یونیفارم احتمالي تابع بلل کېږي')
k.group('list', [
    ('A random experiment which has two possible outcomes, classified as success and failure, is called a Bernoulli trial.', 'ایسا تصادفی تجربہ جس کے دو ممکنہ نتائج کامیابی اور ناکامی کے طور پر درجہ بند ہوں، برنولی آزمائش کہلاتا ہے۔', 'هغه تصادفي تجربه چې دوه شونې پایلې ولري چې د بریا او ناکامۍ په توګه ډلبندي شوې وي، د برنولي ازمېښت بلل کېږي.'),
    ('If a Bernoulli trail is repeated a fixed number of times, say n, then such an experiment is called Binomial experiment.', 'اگر برنولی آزمائش ایک مقررہ تعداد، مثلاً n، بار دہرائی جائے تو ایسا تجربہ دو رقمی تجربہ کہلاتا ہے۔', 'که د برنولي ازمېښت یو ټاکلی شمېر ځله، لکه n، تکرار شي، نو داسې تجربه بینومیل تجربه بلل کېږي.'),
    ('The Binomial probability mass function is given by the formula:', 'دو رقمی احتمالی کمیتی تفاعل اس فارمولا سے دیا جاتا ہے:', 'د بینومیل د احتمال کتلوي تابع په دې فورمول ورکول کېږي:'),
])
k.eq(r'p(x)=\left\{\begin{matrix}{}^{n}_{x}C\,p^xq^{n-x}, & x=0,1,2,\ldots,n\\ 0, & \textit{otherwise}\end{matrix}\right.')
k.group('list', [
    ('Mean of Binomial distribution is np', 'دو رقمی تقسیم کا اوسط np ہے', 'د بینومیل وېش منځنی np دی'),
    ('Binomial distribution has two parameters i.e. n and p. Its range is from 0 to n', 'دو رقمی تقسیم کے دو پیرامیٹر ہیں یعنی n اور p۔ اس کی حد 0 سے n تک ہے', 'بینومیل وېش دوه پارامټرونه لري یعنې n او p. حد یې له 0 څخه تر n پورې دی'),
    ('Variance of Binomial distribution is npq', 'دو رقمی تقسیم کا تغیر npq ہے', 'د بینومیل وېش واریانس npq دی'),
    ('The hypergeometric probability distribution is', 'ہائپر جیومیٹرک احتمالی تقسیم یہ ہے', 'هایپرجیومټریک احتمالي وېش دا دی'),
])
k.eq(r'p(x)=\left\{\begin{matrix}\dfrac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}, & x=0,1,2,\ldots,\min(n,K)\\ 0 & \textit{otherwise}\end{matrix}\right.')
k.group('list', [('Hypergeometric distribution has three parameters and its range is from 0 to min(n,k)', 'ہائپر جیومیٹرک تقسیم کے تین پیرامیٹر ہیں اور اس کی حد 0 سے min(n,k) تک ہے', 'هایپرجیومټریک وېش درې پارامټرونه لري او حد یې له 0 څخه تر min(n,k) پورې دی')])
keys = k.build('stat12-u3-key-points', 'Unit 3 — Key points', 'یونٹ 3 — اہم نکات', 'واحد 3 — مهم ټکي', 59, [109])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.h('3.1 Write T for true and F for false in the following statement.', '3.1 درج ذیل بیانات میں درست کے لیے T اور غلط کے لیے F لکھیں۔', '3.1 په لاندې بیانونو کې د سم لپاره T او د ناسم لپاره F ولیکئ.')
e.p('i) If', 'i) اگر', 'i) که')
e.dist('stat12-t-q3-1-i', ['0', '1'], ['$\\frac{1}{2}$', '$\\frac{1}{2}$'], total=None)
e.p('then X is not uniform random variable.', 'تو X یکساں تصادفی متغیر نہیں ہے۔', 'نو X یونیفارم تصادفي متغیر نه دی.')
e.group('lines', [
    ('ii. Bernoulli experiment will always give only two results.', 'ii. برنولی تجربہ ہمیشہ صرف دو نتائج دے گا۔', 'ii. د برنولي تجربه به تل یوازې دوه پایلې ورکوي.'),
    ('iii. Tossing a fair coin a large number of times is a Binomial experiment', 'iii. منصفانہ سکہ بہت زیادہ مرتبہ اچھالنا دو رقمی تجربہ ہے', 'iii. د یوې عادلانه سکې ډېر ځله اچول بینومیل تجربه ده'),
    ('iv. Binomial probability distribution has only two parameters i.e. n and p.', 'iv. دو رقمی احتمالی تقسیم کے صرف دو پیرامیٹر ہیں یعنی n اور p۔', 'iv. بینومیل احتمالي وېش یوازې دوه پارامټرونه لري یعنې n او p.'),
    ('v. A Binomial random variable is discrete.', 'v. دو رقمی تصادفی متغیر منفصل ہوتا ہے۔', 'v. بینومیل تصادفي متغیر منفصل دی.'),
    ('vi. Mean and variance of binomial distribution are equal.', 'vi. دو رقمی تقسیم کا اوسط اور تغیر برابر ہوتے ہیں۔', 'vi. د بینومیل وېش منځنی او واریانس سره برابر دي.'),
    ('vii. If each digit from 0 to 9 has the same probability i.e. $\\frac{1}{10}$, they are called random digits.', 'vii. اگر 0 سے 9 تک ہر ہندسے کا احتمال یکساں یعنی $\\frac{1}{10}$ ہو تو انہیں تصادفی ہندسے کہتے ہیں۔', 'vii. که له 0 څخه تر 9 پورې هر رقم یو شان احتمال یعنې $\\frac{1}{10}$ ولري، تصادفي رقمونه بلل کېږي.'),
    ('viii. The Binomial distribution will be symmetrical if $p=q=\\frac{1}{2}$', 'viii. دو رقمی تقسیم متشاکل ہوگی اگر $p=q=\\frac{1}{2}$', 'viii. بینومیل وېش به متناظر وي که $p=q=\\frac{1}{2}$'),
    ('ix. The hypergeometric random variable cannot assume the negative values.', 'ix. ہائپر جیومیٹرک تصادفی متغیر منفی قیمتیں نہیں لے سکتا۔', 'ix. هایپرجیومټریک تصادفي متغیر منفي قیمتونه نه شي اخیستلای.'),
    ('x. Hypergeometric probability distribution has three parameters i.e. N, K, and n.', 'x. ہائپر جیومیٹرک احتمالی تقسیم کے تین پیرامیٹر ہیں یعنی N، K اور n۔', 'x. هایپرجیومټریک احتمالي وېش درې پارامټرونه لري یعنې N، K او n.'),
])
B = '______'
e.h('3.2 Fill in the blanks.', '3.2 خالی جگہیں پُر کریں۔', '3.2 تش ځایونه ډک کړئ.')
e.group('lines', [
    (f'(i) Bernoulli trail has {B} possible outcomes.', f'(i) برنولی آزمائش کے {B} ممکنہ نتائج ہوتے ہیں۔', f'(i) د برنولي ازمېښت {B} شونې پایلې لري.'),
    (f'(ii) Bernoulli distribution has {B} parameter.', f'(ii) برنولی تقسیم کا {B} پیرامیٹر ہوتا ہے۔', f'(ii) د برنولي وېش {B} پارامټر لري.'),
    (f'(iii) Range of Binomial random variable is from 0 to {B}.', f'(iii) دو رقمی تصادفی متغیر کی حد 0 سے {B} تک ہے۔', f'(iii) د بینومیل تصادفي متغیر حد له 0 څخه تر {B} پورې دی.'),
    (f'(iv) Parameters of Binomial distribution are {B}.', f'(iv) دو رقمی تقسیم کے پیرامیٹر {B} ہیں۔', f'(iv) د بینومیل وېش پارامټرونه {B} دي.'),
    (f'(v) Mean of Binomial distribution is {B} and variance is {B}.', f'(v) دو رقمی تقسیم کا اوسط {B} اور تغیر {B} ہے۔', f'(v) د بینومیل وېش منځنی {B} او واریانس یې {B} دی.'),
    (f'(vi) The number of trails in hypergeometric distribution is {B}.', f'(vi) ہائپر جیومیٹرک تقسیم میں آزمائشوں کی تعداد {B} ہے۔', f'(vi) په هایپرجیومټریک وېش کې د ازمېښتونو شمېر {B} دی.'),
])
ex = e.build('stat12-u3-exercise-a', 'Unit 3 Exercise — 3.1 and 3.2 (i)–(vi)', 'یونٹ 3 مشق — 3.1 اور 3.2 (i)–(vi)', 'واحد 3 تمرین — 3.1 او 3.2 (i)–(vi)', 59, [110])

if __name__ == '__main__':
    save(59, [(3, keys), (3, ex)])
