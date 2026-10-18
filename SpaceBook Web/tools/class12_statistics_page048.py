"""PDF48 printed 87–88: Example 3.11 end, Example 3.12 (bomber), 3.3.3 binomial mean derivation, variance start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
t = lambda a: f'\\left(\\frac{{{a}}}{{10}}\\right)'
f5 = lambda a: f'\\left(\\frac{{{a}}}{{5}}\\right)'
b = Builder()
b.eq(r'p(x)=\left\{\begin{matrix}{}^{10}_{x}C' + t(1) + '^x' + t(9) + r'^{10-x}, & x=0,1,2,\ldots,10\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('Now $P$[not more than two items being defective] $=P[X\\le 2]$', 'اب $P$[دو سے زیادہ اشیاء ناقص نہ ہوں] $=P[X\\le 2]$', 'اوس $P$[له دوو زیات توکي عیبي نه وي] $=P[X\\le 2]$')
b.mlines([r'={}^{10}_{0}C' + t(1) + '^0' + t(9) + r'^{10-0}+{}^{10}_{1}C' + t(1) + '^1' + t(9) + r'^{10-1}+{}^{10}_{2}C' + t(1) + '^2' + t(9) + '^{10-2}',
          '=' + t(9) + '^{10}+10' + t(1) + t(9) + r'^9+45\left(\frac{1}{100}\right)' + t(9) + '^8', r'=0.3487+0.3874+0.1937=0.9298'])
ex11 = b.build('stat12-p048-example-3-11', 'Example 3.11 — solution', 'مثال 3.11 — حل', 'بېلګه 3.11 — حل', 48, [87])

c = Builder()
c.h('Example 3.12', 'مثال 3.12', 'بېلګه 3.12')
c.p('The chances of a bomber hitting the target and missing the target are 3:2. Calculate the probability that the target will be hit at least once in five sorties.', 'ایک بمبار کے ہدف کو نشانہ بنانے اور چوکنے کے امکانات 3:2 ہیں۔ احتمال معلوم کریں کہ پانچ پروازوں میں ہدف کم از کم ایک بار نشانہ بنے گا۔', 'د یوه بمبار د هدف د لګولو او خطا کولو چانسونه 3:2 دي. احتمال یې محاسبه کړئ چې په پنځو الوتنو کې به هدف لږ تر لږه یو ځل ولګېږي.')
c.h(*SOL)
c.p('Given that $p=\\frac{3}{5}$, $q=\\frac{2}{5}$, $n=5$', 'دیا گیا ہے $p=\\frac{3}{5}$، $q=\\frac{2}{5}$، $n=5$', 'ورکړل شوي $p=\\frac{3}{5}$، $q=\\frac{2}{5}$، $n=5$')
c.p('X: denotes the number of hits.', 'X: ہدف پر لگنے کی تعداد ظاہر کرتا ہے۔', 'X: د لګېدو شمېر ښيي.')
c.eq(r'X=0,1,2,3,4,5')
c.p('So', 'لہٰذا', 'نو')
c.eq(r'p(x)=\left\{\begin{matrix}{}^{5}_{x}C' + f5(3) + '^x' + f5(2) + r'^{5-x}, & x=0,1,2,3,4,5\\ 0, & \textit{otherwise}\end{matrix}\right.')
c.p('Now, $P$[at least one will hit the target] $=1-P$[no one will hit the target]', 'اب، $P$[کم از کم ایک ہدف پر لگے] $=1-P$[کوئی ہدف پر نہ لگے]', 'اوس، $P$[لږ تر لږه یو هدف ولګوي] $=1-P$[هېڅ یو هدف ونه لګوي]')
c.mlines([r'P(X\ge 1)=1-P[X=0]', r'=1-{}^{5}_{0}C' + f5(3) + '^0' + f5(2) + '^{5-0}', '=1-' + f5(2) + r'^5=1-0.01024=0.98976'])
ex12 = c.build('stat12-p048-example-3-12', 'Example 3.12 — bomber sorties', 'مثال 3.12 — بمبار کی پروازیں', 'بېلګه 3.12 — د بمبار الوتنې', 48, [87, 88])

d = Builder()
d.h('3.3.3 Properties of Binomial distribution', '3.3.3 دو رقمی تقسیم کی خصوصیات', '3.3.3 د بینومیل وېش ځانګړنې')
d.p('(i) Mean of Binomial distribution', '(i) دو رقمی تقسیم کا اوسط', '(i) د بینومیل وېش منځنی')
d.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
d.mlines([r'\text{Mean}=E(X)=\sum_x x\,p(x)', r'=\sum_{x=0}^{n}x\,{}^{n}_{x}C\,p^xq^{n-x}', r'=0\,{}^{n}_{0}C\,p^0q^{n-0}+1\,{}^{n}_{1}C\,p^1q^{n-1}+2\,{}^{n}_{2}C\,p^2q^{n-2}+\ldots+n\,{}^{n}_{n}C\,p^nq^{n-n}',
          r'=0+npq^{n-1}+\ldots+np^n', r'=np\,[q^{n-1}+\ldots+p^{n-1}]', r'=np\,[q+p]^{n-1}', r'=np\,(1)^{n-1}\qquad\because p+q=1', r'=np'])
d.p('(ii) Variance of Binomial distribution', '(ii) دو رقمی تقسیم کا تغیر', '(ii) د بینومیل وېش واریانس')
d.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
d.mlines([r'\text{Variance}=V(X)=E(X^2)-[E(X)]^2\qquad(A)', r'\text{As } E(X)=np\qquad(1)', r'\text{Now } E(X^2)=\Sigma x^2p(x)', r'=\sum_x[x(x-1)+x]\,p(x)\qquad\because x^2=x(x-1)+x'])
props = d.build('stat12-p048-binomial-properties', '3.3.3 Properties of the binomial distribution — mean', '3.3.3 دو رقمی تقسیم کی خصوصیات — اوسط', '3.3.3 د بینومیل وېش ځانګړنې — منځنی', 48, [88])

if __name__ == '__main__':
    save(48, [(3, ex11), (3, ex12), (3, props)])
