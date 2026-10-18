"""PDF30 printed 51–52: Example 2.14 (vi), 2.3 continuous r.v. distribution, 2.3.1 pdf, 2.3.2 properties, Example 2.15 (i)–(ii)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'(vi)\quad S.D\left(\frac{X}{3}\right)=\frac{S.D(X)}{|3|}\qquad\because S.D(x)=\sqrt{0.89}=0.94', r'=\frac{0.94}{3}=0.314'])
b.h('2.3 Probability distribution of a continuous random variable', '2.3 مسلسل تصادفی متغیر کی احتمالی تقسیم', '2.3 د متصل تصادفي متغیر احتمالي وېش')
b.p('All possible values of a continuous random variable along with probability cannot be presented in tabular form. This purpose is only achieved by formula, called probability density function of the continuous random variable.',
    'مسلسل تصادفی متغیر کی تمام ممکنہ قیمتیں احتمالات کے ساتھ جدولی شکل میں پیش نہیں کی جا سکتیں۔ یہ مقصد صرف فارمولا سے حاصل ہوتا ہے جسے مسلسل تصادفی متغیر کا احتمالی کثافتی تفاعل کہتے ہیں۔',
    'د متصل تصادفي متغیر ټول شوني قیمتونه له احتمال سره په جدولي بڼه نه شي وړاندې کېدای. دا موخه یوازې د فورمول په واسطه ترلاسه کېږي چې د متصل تصادفي متغیر د احتمال کثافت تابع بلل کېږي.')
b.h('2.3.1 Probability density function', '2.3.1 احتمالی کثافتی تفاعل', '2.3.1 د احتمال کثافت تابع')
b.p('If probability distribution of a continuous random variable is expressed by a formula, then it is called probability density function (pdf) or simply density function and is denoted by f(x).',
    'اگر کسی مسلسل تصادفی متغیر کی احتمالی تقسیم فارمولا سے ظاہر کی جائے تو اسے احتمالی کثافتی تفاعل (pdf) یا صرف کثافتی تفاعل کہتے ہیں اور اسے f(x) سے ظاہر کرتے ہیں۔',
    'که د یوه متصل تصادفي متغیر احتمالي وېش د فورمول په واسطه وښودل شي، نو د احتمال کثافت تابع (pdf) یا یوازې کثافت تابع بلل کېږي او په f(x) ښودل کېږي.')
b.h('2.3.2 Properties of probability density function', '2.3.2 احتمالی کثافتی تفاعل کی خصوصیات', '2.3.2 د احتمال کثافت تابع ځانګړنې')
b.p('A pdf must satisfy the following important properties:', 'pdf کو درج ذیل اہم خصوصیات پوری کرنی چاہئیں:', 'pdf باید لاندې مهمې ځانګړنې پوره کړي:')
b.mlines([r'(i)\quad f(x)\ge 0,\ a\le x\le b', r'(ii)\quad\int_{-\infty}^{\infty}f(x)\,dx=1'])
b.h('Example: 2.15', 'مثال: 2.15', 'بېلګه: 2.15')
b.p('A continuous random variable X has the probability function given by', 'ایک مسلسل تصادفی متغیر X کا احتمالی تفاعل یہ ہے', 'یو متصل تصادفي متغیر X دا احتمالي تابع لري')
b.eq(r'f(x)=\left\{\begin{matrix}cx, & 0<x<1\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.group('lines', [
    ('i. Find value of the constant c.', 'i. مستقل c کی قیمت معلوم کریں۔', 'i. د ثابت c قیمت پیدا کړئ.'),
    ('ii. Check that the function is a p.d.f', 'ii. جانچیں کہ تفاعل p.d.f ہے', 'ii. وګورئ چې تابع p.d.f ده'),
    ('iii. Compute (a) $P\\left[\\frac{1}{4}<X<\\frac{1}{2}\\right]$ (b) $P\\left(X>\\frac{1}{2}\\right)$ (c) $P\\left(X=\\frac{1}{2}\\right)$',
     'iii. معلوم کریں (a) $P\\left[\\frac{1}{4}<X<\\frac{1}{2}\\right]$ (b) $P\\left(X>\\frac{1}{2}\\right)$ (c) $P\\left(X=\\frac{1}{2}\\right)$',
     'iii. محاسبه کړئ (a) $P\\left[\\frac{1}{4}<X<\\frac{1}{2}\\right]$ (b) $P\\left(X>\\frac{1}{2}\\right)$ (c) $P\\left(X=\\frac{1}{2}\\right)$'),
])
b.h(*SOL)
b.p('(i) We know that sum of all probabilities is equal to one i.e.', '(i) ہم جانتے ہیں کہ تمام احتمالات کا مجموعہ ایک کے برابر ہوتا ہے یعنی', '(i) پوهېږو چې د ټولو احتمالونو مجموعه له یو سره برابره ده یعنې')
b.mlines([r'\int_{0}^{1}f(x)\,dx=1', r'\int_{0}^{1}cx\,dx=1', r'c\int_{0}^{1}x\,dx=1', r'c\left[\frac{x^2}{2}\right]_{0}^{1}=1', r'c\left(\frac{1}{2}-0\right)=1', r'\frac{c}{2}=1\quad\Rightarrow c=2'])
b.p('Put the value of c in the given function, we have', 'دیے گئے تفاعل میں c کی قیمت رکھنے سے', 'په ورکړل شوې تابع کې د c قیمت ایښودو سره')
b.eq(r'f(x)=\left\{\begin{matrix}2x & 0<x<1\\ 0 & \textit{otherwise}\end{matrix}\right\}')
b.p('(ii) a) $f(x)\\ge 0$ for the given range', '(ii) a) دی گئی حد میں $f(x)\\ge 0$', '(ii) a) په ورکړل شوي حد کې $f(x)\\ge 0$')
b.p('b) $\\int_x f(x)\\,dx=1$', 'b) $\\int_x f(x)\\,dx=1$', 'b) $\\int_x f(x)\\,dx=1$')
b.p('Taking L.H.S', 'بائیں طرف (L.H.S) لینے سے', 'کیڼ اړخ (L.H.S) اخیستلو سره')
b.eq(r'\int_x f(x)\,dx=\int_{0}^{1}2x\,dx=2\int_{0}^{1}x\,dx=2\left.\frac{x^2}{2}\right|_{0}^{1}=\left.x^2\right|_{0}^{1}=1-0=1=R.H.S')
b.p('Since both properties are satisfied, therefore, the given function is a p.d.f.', 'چونکہ دونوں خصوصیات پوری ہوتی ہیں، لہٰذا دیا گیا تفاعل p.d.f ہے۔', 'څرنګه چې دواړه ځانګړنې پوره دي، نو ورکړل شوې تابع p.d.f ده.')
rec = b.build('stat12-p030-pdf', '2.3 Continuous random variables — probability density function', '2.3 مسلسل تصادفی متغیرات — احتمالی کثافتی تفاعل', '2.3 متصل تصادفي متغیرونه — د احتمال کثافت تابع', 30, [51, 52])
issues = [{'id': 'stat12-p52-x2-typeset', 'unit': 2, 'printedPage': 52, 'description': 'Example 2.15(i) prints the antiderivative as “x2/2” with the exponent set on the line; rendered as x²/2.'}]

if __name__ == '__main__':
    save(30, [(2, rec)], issues=issues)
