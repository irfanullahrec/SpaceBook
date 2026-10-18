"""PDF31 printed 53–54: Example 2.15 (iii), 2.3.3 expectation/variance of a continuous r.v., Example 2.16, Example 2.17 question."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'(iii)\ (a)\quad P\left(\frac{1}{4}<X<\frac{1}{2}\right)=\int_{1/4}^{1/2}f(x)\,dx=\int_{1/4}^{1/2}2x\,dx=2\int_{1/4}^{1/2}x\,dx',
          r'=2\left.\left(\frac{x^2}{2}\right)\right|_{1/4}^{1/2}=\left.x^2\right|_{1/4}^{1/2}=\frac{1}{4}-\frac{1}{16}=\frac{4-1}{16}=\frac{3}{16}',
          r'(b)\quad P\left(X>\frac{1}{2}\right)=\int_{\frac{1}{2}}^{1}f(x)\,dx=\int_{\frac{1}{2}}^{1}2x\,dx=2\int_{\frac{1}{2}}^{1}x\,dx=2\left.\frac{x^2}{2}\right|_{1/2}^{1}',
          r'=\left.x^2\right|_{1/2}^{1}=1-\frac{1}{4}=\frac{4-1}{4}=\frac{3}{4}'])
b.p('(c) $P\\left(X=\\frac{1}{2}\\right)=0$, because in continuous case point probability is always equal to zero.',
    '(c) $P\\left(X=\\frac{1}{2}\\right)=0$، کیونکہ مسلسل صورت میں کسی نقطے کا احتمال ہمیشہ صفر ہوتا ہے۔',
    '(c) $P\\left(X=\\frac{1}{2}\\right)=0$، ځکه چې په متصل حالت کې د یوه ټکي احتمال تل له صفر سره برابر وي.')
b.h('2.3.3 Expectation, variance and standard deviation of a continuous random variable', '2.3.3 مسلسل تصادفی متغیر کی توقع، تغیر اور معیاری انحراف', '2.3.3 د متصل تصادفي متغیر تمه، واریانس او معیاري انحراف')
b.p('If X is a continuous random variable, then expected value of X is given by $E(X)=\\int_x x\\,f(x)\\,dx$, provided that it exists.',
    'اگر X ایک مسلسل تصادفی متغیر ہو تو X کی متوقع قیمت $E(X)=\\int_x x\\,f(x)\\,dx$ ہے، بشرطیکہ یہ موجود ہو۔',
    'که X یو متصل تصادفي متغیر وي، نو د X تمه شوی قیمت $E(X)=\\int_x x\\,f(x)\\,dx$ دی، په دې شرط چې شتون ولري.')
b.h('Example 2.16', 'مثال 2.16', 'بېلګه 2.16')
b.p('Let X be a continuous random variable with pdf given by', 'فرض کریں X ایک مسلسل تصادفی متغیر ہے جس کا pdf یہ ہے', 'فرض کړئ X یو متصل تصادفي متغیر دی چې pdf یې دا ده')
b.eq(r'f(x)=\left\{\begin{matrix}\frac{x}{2} & 0\le x\le 2\\ 0 & \textit{otherwise}\end{matrix}\right.')
b.p('Find the mean, variance and standard deviation of X.', 'X کا اوسط، تغیر اور معیاری انحراف معلوم کریں۔', 'د X منځنی، واریانس او معیاري انحراف پیدا کړئ.')
b.h(*SOL)
b.p('(i) By definition', '(i) تعریف کے مطابق', '(i) د تعریف له مخې')
b.mlines([r'\text{Mean}=E(X)=\int_x x\,f(x)\,dx', r'=\int_{0}^{2}x\left(\frac{x}{2}\right)dx=\frac{1}{2}\int_{0}^{2}x^2dx=\frac{1}{2}\left.\left(\frac{x^3}{3}\right)\right|_{0}^{2}',
          r'=\left.\left(\frac{x^3}{6}\right)\right|_{0}^{2}=\frac{8}{6}-0=\frac{4}{3}=1.333'])
b.p('(ii) By definition', '(ii) تعریف کے مطابق', '(ii) د تعریف له مخې')
b.mlines([r'V(X)=E(X^2)-[E(X)]^2', r'=\int_{0}^{2}x^2f(x)\,dx-\left(\frac{4}{3}\right)^2', r'=\int_{0}^{2}x^2\left(\frac{x}{2}\right)dx-\frac{16}{9}',
          r'=\int_{0}^{2}\frac{x^3}{2}dx-\frac{16}{9}=\left.\frac{x^4}{8}\right|_{0}^{2}-\frac{16}{9}=\left(\frac{16}{8}-0\right)-\frac{16}{9}', r'=2-1.78=0.22',
          r'(iii)\quad S.D(X)=\sqrt{0.22}=0.47'])
b.h('Example 2.17', 'مثال 2.17', 'بېلګه 2.17')
b.p('A random variable X has the density function given by', 'ایک تصادفی متغیر X کا کثافتی تفاعل یہ ہے', 'یو تصادفي متغیر X دا کثافت تابع لري')
b.eq(r'f(x)=\left\{\begin{matrix}(2-2x), & 0\le x\le 1\\ 0 & \textit{otherwise}\end{matrix}\right.')
b.p('Find (i) E(X) (ii) E(X²) (iii) E(2X) (iv) E(2X−1) (v) variance and standard deviation of X',
    'معلوم کریں (i) E(X) (ii) E(X²) (iii) E(2X) (iv) E(2X−1) (v) X کا تغیر اور معیاری انحراف',
    'پیدا کړئ (i) E(X) (ii) E(X²) (iii) E(2X) (iv) E(2X−1) (v) د X واریانس او معیاري انحراف')
rec = b.build('stat12-p031-continuous-expectation', '2.3.3 Expectation and variance of a continuous random variable', '2.3.3 مسلسل تصادفی متغیر کی توقع اور تغیر', '2.3.3 د متصل تصادفي متغیر تمه او واریانس', 31, [53, 54])

if __name__ == '__main__':
    save(31, [(2, rec)])
