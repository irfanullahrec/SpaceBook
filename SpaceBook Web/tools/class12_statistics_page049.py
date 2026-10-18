"""PDF49 printed 89–90: binomial variance derivation (npq), S.D, Example 3.13, Example 3.14 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'=\sum_x x(x-1)\,p(x)+\sum_x x\,p(x)', r'=\sum_{x=0}^{n}x(x-1)\,{}^{n}_{x}C\,p^xq^{n-x}+\sum_{x=0}^{n}x\,{}^{n}_{x}C\,p^xq^{n-x}',
          r'=\left[0(0-1)\,{}^{n}_{0}C\,p^0q^{n-0}+1(1-1)\,{}^{n}_{1}C\,p^1q^{n-1}+2(2-1)\,{}^{n}_{2}C\,p^2q^{n-2}+\ldots+n(n-1)\,p^nq^{n-n}\right]+[np]',
          r'=[0+0+n(n-1)\,p^2q^{n-2}+\ldots+n(n-1)\,p^n]+(np)', r'=n(n-1)\,p^2\,[q^{n-2}+\ldots+p^{n-2}]+(np)', r'=n(n-1)\,p^2\,[q+p]^{n-2}+(np)',
          r'=n(n-1)\,p^2\,(1)^{n-2}+(np)\qquad\text{As } p+q=1', r'=n^2p^2-np^2+np\qquad(2)'])
b.p('Putting equation (1) and equation (2) in equation (A) we get', 'مساوات (1) اور (2) کو مساوات (A) میں رکھنے سے', 'د (1) او (2) معادلې په (A) معادله کې ایښودو سره')
b.mlines([r'V(X)=n^2p^2-np^2+np-n^2p^2', r'=np-np^2', r'=np(1-p)', r'=npq\qquad(\because q=1-p)'])
b.p('(iii) Standard deviation of Binomial distribution', '(iii) دو رقمی تقسیم کا معیاری انحراف', '(iii) د بینومیل وېش معیاري انحراف')
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'S.D(X)=\sqrt{V(X)}', r'=\sqrt{npq}'])
var = b.build('stat12-p049-binomial-variance', 'Binomial variance (npq) and standard deviation', 'دو رقمی تغیر (npq) اور معیاری انحراف', 'بینومیل واریانس (npq) او معیاري انحراف', 49, [89])

c = Builder()
c.h('Example 3.13', 'مثال 3.13', 'بېلګه 3.13')
c.p('Find the mean, variance and standard deviation of the Binomial distribution whose parameters are n = 20 and $p=\\frac{3}{5}$.', 'اس دو رقمی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں جس کے پیرامیٹر n = 20 اور $p=\\frac{3}{5}$ ہیں۔', 'د هغه بینومیل وېش منځنی، واریانس او معیاري انحراف پیدا کړئ چې پارامټرونه یې n = 20 او $p=\\frac{3}{5}$ دي.')
c.h(*SOL)
c.p('We have $n=20$, $p=\\frac{3}{5}$, $q=\\frac{2}{5}$, therefore,', 'ہمارے پاس $n=20$، $p=\\frac{3}{5}$، $q=\\frac{2}{5}$ ہیں، لہٰذا', 'موږ لرو $n=20$، $p=\\frac{3}{5}$، $q=\\frac{2}{5}$، نو')
c.mlines([r'\text{Mean}=np=20\times\frac{3}{5}=12', r'\text{Variance}=npq=20\times\frac{3}{5}\times\frac{2}{5}=4.8', r'S.D(X)=\sqrt{npq}=\sqrt{4.8}=2.19'])
c.h('Example 3.14', 'مثال 3.14', 'بېلګه 3.14')
c.p('If n = 4, $p=\\frac{1}{3}$, find (i) the complete Binomial probability distribution. (ii) mean and variance of this distribution. (iii) calculate the mean and variance using properties and compare the results.',
    'اگر n = 4، $p=\\frac{1}{3}$ ہو تو معلوم کریں (i) مکمل دو رقمی احتمالی تقسیم۔ (ii) اس تقسیم کا اوسط اور تغیر۔ (iii) خصوصیات کی مدد سے اوسط اور تغیر معلوم کریں اور نتائج کا موازنہ کریں۔',
    'که n = 4، $p=\\frac{1}{3}$ وي، پیدا کړئ (i) بشپړ بینومیل احتمالي وېش. (ii) د دې وېش منځنی او واریانس. (iii) د ځانګړنو په کارولو سره منځنی او واریانس محاسبه کړئ او پایلې پرتله کړئ.')
c.h(*SOL)
c.p('(i) Here $p=\\frac{1}{3}$, $q=\\frac{2}{3}$, $n=4$, $X=0,1,2,3,4$', '(i) یہاں $p=\\frac{1}{3}$، $q=\\frac{2}{3}$، $n=4$، $X=0,1,2,3,4$', '(i) دلته $p=\\frac{1}{3}$، $q=\\frac{2}{3}$، $n=4$، $X=0,1,2,3,4$')
c.eq(r'p(x)=\left\{\begin{matrix}{}^{4}_{x}C\left(\frac{1}{3}\right)^x\left(\frac{2}{3}\right)^{4-x}, & x=0,1,2,3,4\\ 0, & \textit{otherwise}\end{matrix}\right.')
ex = c.build('stat12-p049-examples-3-13-3-14', 'Examples 3.13–3.14 — binomial mean and variance', 'مثالیں 3.13–3.14 — دو رقمی اوسط اور تغیر', 'بېلګې 3.13–3.14 — بینومیل منځنی او واریانس', 49, [90])

if __name__ == '__main__':
    save(49, [(3, var), (3, ex)])
