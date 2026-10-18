"""PDF22 printed 35–36: meaning of the two properties, Example 2.3 (binomial-type pmf), Example 2.4 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
F = lambda n: f'$\\frac{{{n}}}{{8}}$'
b = Builder()
b.p('First property means that answer of probability must be within the range 0 to 1 (inclusive) and second property means that the sum of probabilities for all possible values of a random variable must be equal to one.',
    'پہلی خصوصیت کا مطلب ہے کہ احتمال کا جواب 0 سے 1 (بشمول) کی حد میں ہونا چاہیے اور دوسری خصوصیت کا مطلب ہے کہ تصادفی متغیر کی تمام ممکنہ قیمتوں کے احتمالات کا مجموعہ ایک کے برابر ہونا چاہیے۔',
    'لومړۍ ځانګړنه دا مانا لري چې د احتمال ځواب باید د 0 څخه تر 1 (په شمول) حد کې وي او دویمه ځانګړنه دا مانا لري چې د تصادفي متغیر د ټولو شونو قیمتونو د احتمالونو مجموعه باید له یو سره برابره وي.')
b.h('Example 2.3', 'مثال 2.3', 'بېلګه 2.3')
b.p('A discrete random variable has the probability function', 'ایک منفصل تصادفی متغیر کا احتمالی تفاعل یہ ہے', 'یو منفصل تصادفي متغیر دا احتمالي تابع لري')
b.eq(r'p(x)=\left\{\begin{matrix}{}^{3}_{x}C\left(\frac{1}{2}\right)^{3} & \textit{for}\ \ x=0,1,2,3\\ 0 & \textit{otherwise}\end{matrix}\right\}')
b.group('lines', [
    ('i) Compute probabilities for all values of X.', 'i) X کی تمام قیمتوں کے احتمالات معلوم کریں۔', 'i) د X د ټولو قیمتونو احتمالونه محاسبه کړئ.'),
    ('ii) Check that this is a probability mass function.', 'ii) جانچیں کہ یہ احتمالی کمیتی تفاعل ہے۔', 'ii) وګورئ چې دا د احتمال کتلوي تابع ده.'),
    ('iii) Find the probability distribution of X.', 'iii) X کی احتمالی تقسیم معلوم کریں۔', 'iii) د X احتمالي وېش پیدا کړئ.'),
])
b.h(*SOL)
b.p('i) Given $p(x)={}^{3}_{x}C\\left(\\frac{1}{2}\\right)^{3},\\ x=0,1,2,3$', 'i) دیا گیا ہے $p(x)={}^{3}_{x}C\\left(\\frac{1}{2}\\right)^{3},\\ x=0,1,2,3$', 'i) ورکړل شوي $p(x)={}^{3}_{x}C\\left(\\frac{1}{2}\\right)^{3},\\ x=0,1,2,3$')
b.p('Putting values of x, we get', 'x کی قیمتیں رکھنے سے', 'د x قیمتونه ایښودو سره')
b.mlines([rf'p({k})={{}}^{{3}}_{{{k}}}C\left(\frac{{1}}{{2}}\right)^{{3}}=({c})\left(\frac{{1}}{{8}}\right)=\frac{{{c}}}{{8}}' for k, c in [(0, 1), (1, 3), (2, 3), (3, 1)]])
b.p('ii) All probabilities are lying between 0 and 1, and', 'ii) تمام احتمالات 0 اور 1 کے درمیان ہیں، اور', 'ii) ټول احتمالونه د 0 او 1 ترمنځ دي، او')
b.eq(r'\sum_{x=0}^{3}p(x_i)=p(0)+p(1)+p(2)+p(3)=\frac{1}{8}+\frac{3}{8}+\frac{3}{8}+\frac{1}{8}=1')
b.p('Since both properties are satisfied, therefore, the given formula is a probability mass function or probability function.',
    'چونکہ دونوں خصوصیات پوری ہوتی ہیں، لہٰذا دیا گیا فارمولا احتمالی کمیتی تفاعل یا احتمالی تفاعل ہے۔',
    'څرنګه چې دواړه ځانګړنې پوره دي، نو ورکړل شوی فورمول د احتمال کتلوي تابع یا احتمالي تابع ده.')
b.p('iii) The probability distribution of X', 'iii) X کی احتمالی تقسیم', 'iii) د X احتمالي وېش')
b.dist('stat12-t-ex2-3', ['0', '1', '2', '3'], [F(1), F(3), F(3), F(1)])
b.h('Example 2.4', 'مثال 2.4', 'بېلګه 2.4')
b.p('Suppose a discrete probability distribution of random variable X is given in the following table:', 'فرض کریں تصادفی متغیر X کی منفصل احتمالی تقسیم درج ذیل جدول میں دی گئی ہے:', 'فرض کړئ د تصادفي متغیر X منفصل احتمالي وېش په لاندې جدول کې ورکړل شوی دی:')
b.dist('stat12-t-ex2-4', ['-1', '0', '1'], ['3c', '3c', '6c'], total=None)
b.p('Find (i) the value of c (ii) $P(X=0)$ (iii) $P(X<0)$ (iv) $P(X\\ge -1)$', 'معلوم کریں (i) c کی قیمت (ii) $P(X=0)$ (iii) $P(X<0)$ (iv) $P(X\\ge -1)$', 'پیدا کړئ (i) د c قیمت (ii) $P(X=0)$ (iii) $P(X<0)$ (iv) $P(X\\ge -1)$')
b.h(*SOL)
b.mlines([r'(i)\quad\text{As }\sum_{x=-1}^{1}p(x)=1', r'\text{or } p(-1)+p(0)+p(1)=1', r'3c+3c+6c=1', r'12c=1\quad\Rightarrow c=\frac{1}{12}'])
rec = b.build('stat12-p022-pmf-examples', 'Examples 2.3–2.4 — probability mass functions', 'مثالیں 2.3–2.4 — احتمالی کمیتی تفاعل', 'بېلګې 2.3–2.4 — د احتمال کتلوي تابع', 22, [35, 36])

if __name__ == '__main__':
    save(22, [(2, rec)])
