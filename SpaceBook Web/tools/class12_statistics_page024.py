"""PDF24 printed 39–40: Example 2.6 distribution and parts (a)–(d); 2.2.3 distribution of a function of a discrete r.v.; Example 2.7 (X^2)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
f36 = lambda n: f'$\\frac{{{n}}}{{36}}$'
b = Builder()
b.dist('stat12-t-ex2-6', [str(x) for x in range(2, 13)], [f36(n) for n in (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)])
b.p('This distribution can also be shown by the formula called probability function as', 'اس تقسیم کو فارمولا کے ذریعے بھی دکھایا جا سکتا ہے جسے احتمالی تفاعل کہتے ہیں', 'دا وېش د فورمول په واسطه هم ښودل کېدای شي چې احتمالي تابع بلل کېږي')
b.eq(r'p(x)=\left\{\begin{matrix}\frac{6-|7-x|}{36}, & x=2,3,4,\ldots 12\\ 0 & \textit{otherwise}\end{matrix}\right\}')
b.p('(ii) Now using the probability distribution, we get:', '(ii) اب احتمالی تقسیم استعمال کرتے ہوئے:', '(ii) اوس د احتمالي وېش په کارولو سره:')
b.mlines([r'a)\quad P(X=7)=\frac{6}{36}',
          r'b)\quad P(X<6)=P(X=5)+P(X=4)+P(X=3)+P(X=2)', r'\phantom{b)\quad P(X<6)}=\frac{4}{36}+\frac{3}{36}+\frac{2}{36}+\frac{1}{36}=\frac{10}{36}',
          r'c)\quad P(2\le X<5)=P(X=2)+P(X=3)+P(X=4)', r'\phantom{c)\quad P(2\le X<5)}=\frac{1}{36}+\frac{2}{36}+\frac{3}{36}=\frac{6}{36}',
          r'd)\quad P(X=5\text{ or }10)=P(X=5)+P(X=10),', r'\phantom{d)\quad P(X=5\text{ or }10)}=\frac{4}{36}+\frac{3}{36}=\frac{7}{36}'])
ex = b.build('stat12-p024-two-dice-sum', 'Example 2.6 — distribution of the sum of two dice', 'مثال 2.6 — دو پانسوں کے مجموعے کی تقسیم', 'بېلګه 2.6 — د دوو ډایسونو د مجموعې وېش', 24, [39])

c = Builder()
c.h('2.2.3 Probability distribution of a function of discrete random variable', '2.2.3 منفصل تصادفی متغیر کے تفاعل کی احتمالی تقسیم', '2.2.3 د منفصل تصادفي متغیر د تابع احتمالي وېش')
c.p('If X is a random variable, then its functions like $X^2$, $\\frac{1}{X}$, $aX+b$ etc. are also random variables and thus have probability distributions. In case of two random variables, say X and Y, their functions like $X+Y$, $X-Y$, $aX+bY$ etc. are also random variables where a and b are any two non-zero constants. The function of a random variable is usually denoted by H(X).',
    'اگر X ایک تصادفی متغیر ہو تو اس کے تفاعل جیسے $X^2$، $\\frac{1}{X}$، $aX+b$ وغیرہ بھی تصادفی متغیرات ہیں اور اس طرح ان کی بھی احتمالی تقسیمیں ہوتی ہیں۔ دو تصادفی متغیرات مثلاً X اور Y کی صورت میں ان کے تفاعل جیسے $X+Y$، $X-Y$، $aX+bY$ وغیرہ بھی تصادفی متغیرات ہیں جہاں a اور b کوئی سے دو غیر صفر مستقل ہیں۔ تصادفی متغیر کے تفاعل کو عموماً H(X) سے ظاہر کرتے ہیں۔',
    'که X یو تصادفي متغیر وي، نو د هغه تابع ګانې لکه $X^2$، $\\frac{1}{X}$، $aX+b$ او نور هم تصادفي متغیرونه دي او احتمالي وېشونه لري. د دوو تصادفي متغیرونو لکه X او Y په حالت کې د هغو تابع ګانې لکه $X+Y$، $X-Y$، $aX+bY$ او نور هم تصادفي متغیرونه دي چې a او b هر دوه غیر صفر ثابتونه دي. د تصادفي متغیر تابع معمولاً په H(X) ښودل کېږي.')
c.h('Example 2.7', 'مثال 2.7', 'بېلګه 2.7')
c.p('If a discrete random variable X has the following probability distribution.', 'اگر ایک منفصل تصادفی متغیر X کی احتمالی تقسیم درج ذیل ہو۔', 'که یو منفصل تصادفي متغیر X لاندې احتمالي وېش ولري.')
c.dist('stat12-t-ex2-7', ['−2', '2', '1'], ['$\\frac{1}{3}$', '$\\frac{1}{2}$', '$\\frac{1}{6}$'], total=None)
c.p('Find probability distribution for $X^2$, $2X+4$.', '$X^2$ اور $2X+4$ کی احتمالی تقسیم معلوم کریں۔', 'د $X^2$ او $2X+4$ احتمالي وېش پیدا کړئ.')
c.h(*SOL)
c.p('The probability distribution of the random variable $X^2$ is', 'تصادفی متغیر $X^2$ کی احتمالی تقسیم یہ ہے', 'د تصادفي متغیر $X^2$ احتمالي وېش دا دی')
c.dist('stat12-t-ex2-7-sq', ['4', '4', '1'], ['$\\frac{1}{3}$', '$\\frac{1}{2}$', '$\\frac{1}{6}$'], xlabel='$H(X)=X^2$', vertical=True)
fn = c.build('stat12-p024-function-rv', '2.2.3 Distribution of a function of a discrete random variable', '2.2.3 منفصل تصادفی متغیر کے تفاعل کی تقسیم', '2.2.3 د منفصل تصادفي متغیر د تابع وېش', 24, [40])

if __name__ == '__main__':
    save(24, [(2, ex), (2, fn)])
