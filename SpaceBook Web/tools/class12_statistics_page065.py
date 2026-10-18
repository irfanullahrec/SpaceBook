"""PDF65 printed 121–122: Normal reason (v), 4.2.1 definition of the Normal pdf, 4.2.2 properties (i)–(x) with empirical-rule curve, 4.2.3 standard normal variable."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import normal_empirical

b = Builder()
b.p('v. When Normal distribution is shown on a graph paper, it gives a bell-shaped curve called Normal curve which is generally taken as a standard for comparison.', 'v. جب نارمل تقسیم کو گراف پیپر پر دکھایا جائے تو یہ گھنٹی نما منحنی دیتی ہے جسے نارمل منحنی کہتے ہیں اور اسے عموماً موازنے کے معیار کے طور پر لیا جاتا ہے۔', 'v. کله چې نورمال وېش په ګراف کاغذ وښودل شي، د زنګ ډوله منحني ورکوي چې نورمال منحني بلل کېږي او عموماً د پرتلې د معیار په توګه نیول کېږي.')
b.h('4.2.1 Definition of Normal probability distribution', '4.2.1 نارمل احتمالی تقسیم کی تعریف', '4.2.1 د نورمال احتمالي وېش تعریف')
b.p('A random variable X is said to follow a Normal distribution if its probability density function is', 'ایک تصادفی متغیر X نارمل تقسیم کی پیروی کرتا ہے اگر اس کا احتمالی کثافتی تفاعل یہ ہو', 'یو تصادفي متغیر X نورمال وېش تعقیبوي که د احتمال کثافت تابع یې دا وي')
b.eq(r'f(x)=\frac{1}{\sqrt{2\pi}\,\sigma}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2},\quad -\infty\le X\le\infty,\ -\infty\le\mu\le\infty,\ 0\le\sigma\le\infty')
b.p('Where', 'جہاں', 'چې')
b.group('lines', [
    ('X = Normal random variable.', 'X = نارمل تصادفی متغیر۔', 'X = نورمال تصادفي متغیر.'),
    ('f(x) = The height of the curve corresponding to a given value of X.', 'f(x) = X کی دی گئی قیمت کے مطابق منحنی کی بلندی۔', 'f(x) = د X د ورکړل شوي قیمت سره سم د منحني لوړوالی.'),
    ('μ = mean of Normal distribution.', 'μ = نارمل تقسیم کا اوسط۔', 'μ = د نورمال وېش منځنی.'),
    ('σ = standard deviation of Normal distribution', 'σ = نارمل تقسیم کا معیاری انحراف', 'σ = د نورمال وېش معیاري انحراف'),
    ('π = a constant approximately equal to $\\frac{22}{7}=3.1429$', 'π = ایک مستقل جو تقریباً $\\frac{22}{7}=3.1429$ کے برابر ہے', 'π = یو ثابت چې نږدې له $\\frac{22}{7}=3.1429$ سره برابر دی'),
    ('e = a constant approximately equal to 2.7183.', 'e = ایک مستقل جو تقریباً 2.7183 کے برابر ہے۔', 'e = یو ثابت چې نږدې له 2.7183 سره برابر دی.'),
])
b.p('This distribution has two parameters, μ and $\\sigma^2$. Normal distribution is simply written as $X\\sim N(\\mu,\\sigma^2)$.', 'اس تقسیم کے دو پیرامیٹر μ اور $\\sigma^2$ ہیں۔ نارمل تقسیم کو سادہ طور پر $X\\sim N(\\mu,\\sigma^2)$ لکھا جاتا ہے۔', 'دا وېش دوه پارامټرونه μ او $\\sigma^2$ لري. نورمال وېش په ساده ډول داسې لیکل کېږي $X\\sim N(\\mu,\\sigma^2)$.')
b.h('4.2.2 Properties of Normal distribution', '4.2.2 نارمل تقسیم کی خصوصیات', '4.2.2 د نورمال وېش ځانګړنې')
b.p('i) The total probability within its range −∞ to +∞ is always equal to one i.e.', 'i) اس کی حد −∞ سے +∞ کے اندر کل احتمال ہمیشہ ایک کے برابر ہوتا ہے یعنی', 'i) د هغه په حد −∞ څخه تر +∞ کې ټول احتمال تل له یو سره برابر دی یعنې')
b.eq(r'\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}\,\sigma}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}dx=1')
b.group('lines', [
    ('ii) The Normal distribution is symmetrical about the mean and is a bell-shaped.', 'ii) نارمل تقسیم اوسط کے گرد متشاکل اور گھنٹی نما ہوتی ہے۔', 'ii) نورمال وېش د منځني شاوخوا متناظر او د زنګ په بڼه دی.'),
    ('iii) Mean = Median = Mode.', 'iii) اوسط = وسطانیہ = عادہ۔', 'iii) منځنی = منځنۍ (median) = مود.'),
    ('iv) The Normal curve is unimodal.', 'iv) نارمل منحنی یک عادی (unimodal) ہوتی ہے۔', 'iv) نورمال منحني یو مودي ده.'),
    ('v) The first and third quartiles are equidistant from the centre, or Mean μ.', 'v) پہلا اور تیسرا ربعیہ مرکز یعنی اوسط μ سے برابر فاصلے پر ہوتے ہیں۔', 'v) لومړی او درېیم ربعیه له مرکز یعنې منځني μ څخه مساوي واټن لري.'),
    ('vi) $Q.D=\\frac{2}{3}\\sigma$ and $M.D=\\frac{4}{5}\\sigma$', 'vi) $Q.D=\\frac{2}{3}\\sigma$ اور $M.D=\\frac{4}{5}\\sigma$', 'vi) $Q.D=\\frac{2}{3}\\sigma$ او $M.D=\\frac{4}{5}\\sigma$'),
    ('vii) All odd order moments about mean i.e. $\\mu_1,\\mu_3,\\ldots$ are zero.', 'vii) اوسط کے گرد تمام طاق درجے کے معیارِ اثر (moments) یعنی $\\mu_1,\\mu_3,\\ldots$ صفر ہوتے ہیں۔', 'vii) د منځني شاوخوا د طاق ترتیب ټول مومنټونه یعنې $\\mu_1,\\mu_3,\\ldots$ صفر دي.'),
    ('viii) Measures of skewness, $\\beta_1=0$ or $\\gamma_1=0$', 'viii) چولاؤ (skewness) کی پیمائش، $\\beta_1=0$ یا $\\gamma_1=0$', 'viii) د کږوالي (skewness) اندازې، $\\beta_1=0$ یا $\\gamma_1=0$'),
    ('ix) Measures of kurtosis, $\\beta_2=3$ or $\\gamma_2=0$', 'ix) نوک داری (kurtosis) کی پیمائش، $\\beta_2=3$ یا $\\gamma_2=0$', 'ix) د کورټوسیس اندازې، $\\beta_2=3$ یا $\\gamma_2=0$'),
    ('x) For Normal distribution, out of the total observation, 68.3 % lies within the limits $(\\mu\\pm\\sigma)$, 95.4 % lies within the limits $(\\mu\\pm 2\\sigma)$ and 99.7 % lies within the limits $(\\mu\\pm 3\\sigma)$. Graphically this statement is shown as',
     'x) نارمل تقسیم میں کل مشاہدات میں سے 68.3 % حدود $(\\mu\\pm\\sigma)$ کے اندر، 95.4 % حدود $(\\mu\\pm 2\\sigma)$ کے اندر اور 99.7 % حدود $(\\mu\\pm 3\\sigma)$ کے اندر ہوتے ہیں۔ ترسیمی طور پر یہ بیان یوں دکھایا جاتا ہے',
     'x) د نورمال وېش لپاره له ټولو مشاهدو څخه 68.3 % د $(\\mu\\pm\\sigma)$ په حدونو کې، 95.4 % د $(\\mu\\pm 2\\sigma)$ په حدونو کې او 99.7 % د $(\\mu\\pm 3\\sigma)$ په حدونو کې پرتې دي. په ګرافیکي ډول دا بیان داسې ښودل کېږي'),
])
b.visual('stat12-normal-empirical-rule', normal_empirical(), ratio=.75)
b.h('4.2.3 Standard normal variable', '4.2.3 معیاری نارمل متغیر', '4.2.3 معیاري نورمال متغیر')
b.p('Normal random variable X is transformed by subtracting its mean from it and the difference is divided by its standard deviation and is called standard Normal variable, usually denoted by Z, that is', 'نارمل تصادفی متغیر X میں سے اس کا اوسط تفریق کر کے اور فرق کو اس کے معیاری انحراف پر تقسیم کر کے تبدیل کیا جاتا ہے، اسے معیاری نارمل متغیر کہتے ہیں اور عموماً Z سے ظاہر کرتے ہیں، یعنی', 'نورمال تصادفي متغیر X داسې بدلېږي چې منځنی یې ترې تفریق او توپیر یې پر معیاري انحراف ووېشل شي، معیاري نورمال متغیر بلل کېږي او معمولاً په Z ښودل کېږي، یعنې')
b.eq(r'Z=\frac{X-\mu}{\sigma}')
b.p('Possible values of Z are also form −∞ to +∞.', 'Z کی ممکنہ قیمتیں بھی −∞ سے +∞ تک ہیں۔', 'د Z شوني قیمتونه هم له −∞ څخه تر +∞ پورې دي.')
rec = b.build('stat12-p065-normal-definition', '4.2.1–4.2.3 Normal distribution — definition, properties, standard normal variable', '4.2.1–4.2.3 نارمل تقسیم — تعریف، خصوصیات، معیاری نارمل متغیر', '4.2.1–4.2.3 نورمال وېش — تعریف، ځانګړنې، معیاري نورمال متغیر', 65, [121, 122])

if __name__ == '__main__':
    save(65, [(4, rec)])
