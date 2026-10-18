"""PDF41 printed 73–74: uniform histogram, 3.1.4 properties (mean, variance, S.D) with derivations, Example 3.3."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import uniform_histogram

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.visual('stat12-uniform-histogram', uniform_histogram(), ratio=.55)
b.p('Due to rectangular shape, uniform distribution is also known as rectangular distribution', 'مستطیلی شکل کی وجہ سے یکساں تقسیم کو مستطیلی تقسیم بھی کہتے ہیں', 'د مستطیلي بڼې له امله یونیفارم وېش ته مستطیلي وېش هم وایي')
b.h('3.1.4 Properties of discrete uniform probability distribution', '3.1.4 منفصل یکساں احتمالی تقسیم کی خصوصیات', '3.1.4 د منفصل یونیفارم احتمالي وېش ځانګړنې')
b.p('(i) Mean of discrete uniform distribution', '(i) منفصل یکساں تقسیم کا اوسط', '(i) د منفصل یونیفارم وېش منځنی')
b.p('By definition mean $=E(X)=\\sum_x x\\,p(x)$', 'تعریف کے مطابق اوسط $=E(X)=\\sum_x x\\,p(x)$', 'د تعریف له مخې منځنی $=E(X)=\\sum_x x\\,p(x)$')
b.p('Put range and formula of discrete uniform distribution, we get', 'منفصل یکساں تقسیم کی حد اور فارمولا رکھنے سے', 'د منفصل یونیفارم وېش حد او فورمول ایښودو سره')
b.eq(r'E(X)=\sum_{x=1}^{N}x\frac{1}{N}=\frac{1}{N}\sum_{x=1}^{N}x=\frac{1}{N}[1+2+3+\cdots+N]')
b.p('$=\\frac{1}{N}\\left[\\frac{N(N+1)}{2}\\right]$ as $1+2+3+\\ldots+N=\\frac{N(N+1)}{2}$', '$=\\frac{1}{N}\\left[\\frac{N(N+1)}{2}\\right]$ کیونکہ $1+2+3+\\ldots+N=\\frac{N(N+1)}{2}$', '$=\\frac{1}{N}\\left[\\frac{N(N+1)}{2}\\right]$ ځکه چې $1+2+3+\\ldots+N=\\frac{N(N+1)}{2}$')
b.eq(r'=\frac{N+1}{2}')
b.p('(ii) Variance of discrete uniform distribution', '(ii) منفصل یکساں تقسیم کا تغیر', '(ii) د منفصل یونیفارم وېش واریانس')
b.p('By definition variance: $V(X)=E(X^2)-[E(X)]^2\\qquad(1)$', 'تعریف کے مطابق تغیر: $V(X)=E(X^2)-[E(X)]^2\\qquad(1)$', 'د تعریف له مخې واریانس: $V(X)=E(X^2)-[E(X)]^2\\qquad(1)$')
b.p('We know that $E(X)=\\frac{N+1}{2}\\qquad(2)$', 'ہم جانتے ہیں کہ $E(X)=\\frac{N+1}{2}\\qquad(2)$', 'پوهېږو چې $E(X)=\\frac{N+1}{2}\\qquad(2)$')
b.p('Now $E(X^2)=\\sum_{x=1}^{N}x^2\\frac{1}{N}=\\frac{1}{N}\\sum_{x=1}^{N}x^2=\\frac{1}{N}[1^2+2^2+\\cdots+N^2]$', 'اب $E(X^2)=\\sum_{x=1}^{N}x^2\\frac{1}{N}=\\frac{1}{N}\\sum_{x=1}^{N}x^2=\\frac{1}{N}[1^2+2^2+\\cdots+N^2]$', 'اوس $E(X^2)=\\sum_{x=1}^{N}x^2\\frac{1}{N}=\\frac{1}{N}\\sum_{x=1}^{N}x^2=\\frac{1}{N}[1^2+2^2+\\cdots+N^2]$')
b.p('$=\\frac{1}{N}\\left[\\frac{N(N+1)(2N+1)}{6}\\right]$, as $1^2+2^2+\\cdots+N^2=\\frac{N(N+1)(2N+1)}{6}$', '$=\\frac{1}{N}\\left[\\frac{N(N+1)(2N+1)}{6}\\right]$، کیونکہ $1^2+2^2+\\cdots+N^2=\\frac{N(N+1)(2N+1)}{6}$', '$=\\frac{1}{N}\\left[\\frac{N(N+1)(2N+1)}{6}\\right]$، ځکه چې $1^2+2^2+\\cdots+N^2=\\frac{N(N+1)(2N+1)}{6}$')
b.eq(r'=\frac{(N+1)(2N+1)}{6}\qquad(3)')
b.p('Put equation (2) and (3) in equation (1) we get,', 'مساوات (2) اور (3) کو مساوات (1) میں رکھنے سے', 'د (2) او (3) معادلې په (1) کې ایښودو سره')
b.mlines([r'V(X)=\frac{(N+1)(2N+1)}{6}-\left(\frac{N+1}{2}\right)^2=\frac{N+1}{2}\left[\frac{2N+1}{3}-\frac{N+1}{2}\right]',
          r'=\frac{N+1}{2}\left[\frac{4N+2-3N-3}{6}\right]=\frac{N+1}{2}\left[\frac{N-1}{6}\right]', r'=\frac{N^2-1}{12}'])
b.p('(iii) Standard deviation of uniform distribution', '(iii) یکساں تقسیم کا معیاری انحراف', '(iii) د یونیفارم وېش معیاري انحراف')
b.p('By definition $S.D(X)=\\sqrt{V(X)}=\\sqrt{\\frac{N^2-1}{12}}$', 'تعریف کے مطابق $S.D(X)=\\sqrt{V(X)}=\\sqrt{\\frac{N^2-1}{12}}$', 'د تعریف له مخې $S.D(X)=\\sqrt{V(X)}=\\sqrt{\\frac{N^2-1}{12}}$')
b.h('Example 3.3', 'مثال 3.3', 'بېلګه 3.3')
b.p('If X is a discrete uniform random variable taking values 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 each with probability equal to $\\frac{1}{10}$. Find its mean, variance and standard deviation.',
    'اگر X ایک منفصل یکساں تصادفی متغیر ہو جو قیمتیں 1، 2، 3، 4، 5، 6، 7، 8، 9 اور 10 لیتا ہو اور ہر ایک کا احتمال $\\frac{1}{10}$ ہو۔ اس کا اوسط، تغیر اور معیاری انحراف معلوم کریں۔',
    'که X یو منفصل یونیفارم تصادفي متغیر وي چې قیمتونه 1، 2، 3، 4، 5، 6، 7، 8، 9 او 10 اخلي او د هر یوه احتمال $\\frac{1}{10}$ وي. منځنی، واریانس او معیاري انحراف یې پیدا کړئ.')
b.h(*SOL)
b.p('Here total number of observations $=N=10$', 'یہاں مشاہدات کی کل تعداد $=N=10$', 'دلته د مشاهدو ټول شمېر $=N=10$')
b.mlines([r'\therefore\text{Mean}=\frac{N+1}{2}=\frac{10+1}{2}=\frac{11}{2}=5.5', r'\text{Variance}=\frac{N^2-1}{12}=\frac{10^2-1}{12}=\frac{100-1}{12}=\frac{99}{12}=8.25', r'\text{Standard deviation}=\sqrt{8.25}=2.87'])
rec = b.build('stat12-p041-uniform-properties', '3.1.4 Properties of the discrete uniform distribution — Example 3.3', '3.1.4 منفصل یکساں تقسیم کی خصوصیات — مثال 3.3', '3.1.4 د منفصل یونیفارم وېش ځانګړنې — بېلګه 3.3', 41, [73, 74])

if __name__ == '__main__':
    save(41, [(3, rec)])
