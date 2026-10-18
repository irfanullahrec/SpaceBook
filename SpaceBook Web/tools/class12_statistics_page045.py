"""PDF45 printed 81–82: Bernoulli variance end, S.D, Example 3.6; 3.3 binomial experiment, 3.3.1 distribution, 3.3.2 pmf, Example 3.7 question."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'=\sum_{x=0}^{1}x^2p^xq^{1-x}-p^2', r'=0p^0q^{1-0}+1p^1q^{1-1}-p^2', r'=0+p-p^2=p(1-p)=pq,\ (\because q=1-p)'])
b.p('◆ Standard deviation $=\\sqrt{pq}$', '◆ معیاری انحراف $=\\sqrt{pq}$', '◆ معیاري انحراف $=\\sqrt{pq}$')
b.h('Example 3.6', 'مثال 3.6', 'بېلګه 3.6')
b.p('For a Bernoulli random variable X, the probability of success is equal to 0.6. Find the mean, variance and standard deviation for this Bernoulli probability distribution.',
    'ایک برنولی تصادفی متغیر X کے لیے کامیابی کا احتمال 0.6 ہے۔ اس برنولی احتمالی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں۔',
    'د برنولي تصادفي متغیر X لپاره د بریا احتمال 0.6 دی. د دې برنولي احتمالي وېش منځنی، واریانس او معیاري انحراف پیدا کړئ.')
b.h(*SOL)
b.p('(i) By calculation:', '(i) حساب سے:', '(i) د محاسبې له لارې:')
b.grid('stat12-t-ex3-6', ['$X$', '$p(x)$', '$X\\,p(x)$', '$X^2p(x)$'], [['0', '0.4', '0', '0'], ['1', '0.6', '0.6', '0.60'], ['Total', '1', '0.6', '0.60']])
b.mlines([r'\text{Mean}=E(X)=\Sigma x\,p(x)=0.6', r'\text{Variance}=V(X)=E(X^2)-[E(X)]^2=\Sigma x^2p(x)-(0.6)^2=0.6-0.36=0.24'])
b.p('(ii) By properties:', '(ii) خصوصیات سے:', '(ii) د ځانګړنو له لارې:')
b.p('Given that $p=0.60$, $q=1-p=1-0.6=0.40$', 'دیا گیا ہے $p=0.60$، $q=1-p=1-0.6=0.40$', 'ورکړل شوي $p=0.60$، $q=1-p=1-0.6=0.40$')
b.p('Mean of Bernoulli distribution $=p=0.60$', 'برنولی تقسیم کا اوسط $=p=0.60$', 'د برنولي وېش منځنی $=p=0.60$')
b.p('Variance of Bernoulli distribution $=pq=(0.60)(0.40)=0.24$', 'برنولی تقسیم کا تغیر $=pq=(0.60)(0.40)=0.24$', 'د برنولي وېش واریانس $=pq=(0.60)(0.40)=0.24$')
b.eq(r'S.D(X)=\sqrt{0.24}=0.49')
ex = b.build('stat12-p045-bernoulli-example', 'Bernoulli variance and S.D — Example 3.6', 'برنولی تغیر اور معیاری انحراف — مثال 3.6', 'د برنولي واریانس او معیاري انحراف — بېلګه 3.6', 45, [81])

c = Builder()
c.h('3.3 Binomial experiment', '3.3 دو رقمی (Binomial) تجربہ', '3.3 بینومیل تجربه')
c.p('If a Bernoulli trail is repeated a fixed number of times, say n, then such an experiment is called Binomial experiment. It has the following four properties:', 'اگر برنولی آزمائش کو ایک مقررہ تعداد، مثلاً n، بار دہرایا جائے تو ایسا تجربہ دو رقمی تجربہ کہلاتا ہے۔ اس کی درج ذیل چار خصوصیات ہیں:', 'که د برنولي ازمېښت یو ټاکلی شمېر ځله، لکه n، تکرار شي، نو داسې تجربه بینومیل تجربه بلل کېږي. لاندې څلور ځانګړنې لري:')
c.group('lines', [
    ('i. Each trial has only two possible outcomes i.e. success and failure.', 'i. ہر آزمائش کے صرف دو ممکنہ نتائج ہوتے ہیں یعنی کامیابی اور ناکامی۔', 'i. هر ازمېښت یوازې دوه شونې پایلې لري یعنې بریا او ناکامي.'),
    ('ii. The probability of success remains constant for all trails.', 'ii. تمام آزمائشوں کے لیے کامیابی کا احتمال مستقل رہتا ہے۔', 'ii. د ټولو ازمېښتونو لپاره د بریا احتمال ثابت پاتې کېږي.'),
    ('iii. The successive trails are all independent.', 'iii. یکے بعد دیگرے آزمائشیں سب آزاد ہوتی ہیں۔', 'iii. پرله پسې ازمېښتونه ټول خپلواک دي.'),
    ('iv. The Bernoulli trail is repeated a fixed number of times, say n.', 'iv. برنولی آزمائش ایک مقررہ تعداد، مثلاً n، بار دہرائی جاتی ہے۔', 'iv. د برنولي ازمېښت یو ټاکلی شمېر ځله، لکه n، تکرارېږي.'),
])
c.p('The variable denoting the number of successes of a Binomial experiment is called Binomial random variable i.e. $X=0,1,2,\\ldots,n$.', 'دو رقمی تجربے کی کامیابیوں کی تعداد ظاہر کرنے والا متغیر دو رقمی تصادفی متغیر کہلاتا ہے یعنی $X=0,1,2,\\ldots,n$۔', 'هغه متغیر چې د بینومیل تجربې د بریاوو شمېر ښيي، بینومیل تصادفي متغیر بلل کېږي یعنې $X=0,1,2,\\ldots,n$.')
c.h('3.3.1 Binomial probability distribution', '3.3.1 دو رقمی احتمالی تقسیم', '3.3.1 بینومیل احتمالي وېش')
c.p('The binomial probability distribution is given as:', 'دو رقمی احتمالی تقسیم یوں دی جاتی ہے:', 'بینومیل احتمالي وېش داسې ورکول کېږي:')
c.dist('stat12-t-binomial-general', ['0', '1', '2', '$\\cdots$', '$n$'],
       ['${}^{n}_{0}C\\,p^0q^{n-0}$', '${}^{n}_{1}C\\,p^1q^{n-1}$', '${}^{n}_{2}C\\,p^2q^{n-2}$', '$\\cdots$', '${}^{n}_{n}C\\,p^nq^{n-n}$'])
c.h('3.3.2 Binomial probability mass function', '3.3.2 دو رقمی احتمالی کمیتی تفاعل', '3.3.2 د بینومیل د احتمال کتلوي تابع')
c.p('The Binomial probability mass function is given by the formula:', 'دو رقمی احتمالی کمیتی تفاعل اس فارمولا سے دیا جاتا ہے:', 'د بینومیل د احتمال کتلوي تابع په دې فورمول ورکول کېږي:')
c.eq(r'p(x)=\left\{\begin{matrix}{}^{n}_{x}C\,p^xq^{n-x}, & x=0,1,2,\ldots,n\\ 0, & \textit{otherwise}\end{matrix}\right.')
c.p('This distribution has two parameters n, p whereas n denotes the number of independent Bernoulli trails and p denotes the probability of success on a single Bernoulli trail. Note that if n = 1, the Binomial distribution reduces to Bernoulli distribution.',
    'اس تقسیم کے دو پیرامیٹر n اور p ہیں جہاں n آزاد برنولی آزمائشوں کی تعداد اور p ایک برنولی آزمائش میں کامیابی کا احتمال ظاہر کرتا ہے۔ نوٹ کریں کہ اگر n = 1 ہو تو دو رقمی تقسیم برنولی تقسیم بن جاتی ہے۔',
    'دا وېش دوه پارامټرونه n او p لري چې n د خپلواکو برنولي ازمېښتونو شمېر او p په یوه برنولي ازمېښت کې د بریا احتمال ښيي. پام وکړئ چې که n = 1 وي، بینومیل وېش په برنولي وېش بدلېږي.')
c.h('Example 3.7', 'مثال 3.7', 'بېلګه 3.7')
c.p('A fair coin is tossed four times. Find the probability distribution for obtaining various numbers of heads.', 'ایک منصفانہ سکہ چار بار اچھالا جاتا ہے۔ چِت کی مختلف تعداد حاصل کرنے کی احتمالی تقسیم معلوم کریں۔', 'یوه عادلانه سکه څلور ځله اچول کېږي. د سرونو د بېلابېلو شمېرو د ترلاسه کولو احتمالي وېش پیدا کړئ.')
bn = c.build('stat12-p045-binomial', '3.3 Binomial experiment, distribution and probability mass function', '3.3 دو رقمی تجربہ، تقسیم اور احتمالی کمیتی تفاعل', '3.3 بینومیل تجربه، وېش او د احتمال کتلوي تابع', 45, [82])

if __name__ == '__main__':
    save(45, [(3, ex), (3, bn)])
