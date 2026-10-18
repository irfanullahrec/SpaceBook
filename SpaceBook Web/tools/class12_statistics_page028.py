"""PDF28 printed 47–48: Example 2.12 solution, 2.2.8 variance and S.D., Example 2.13, 2.2.9 properties of variance (i)–(ii start)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
PROOF = ('Proof:', 'ثبوت:', 'ثبوت:')
b = Builder()
b.mlines([r'(i)\ \text{By definition}\quad E(X)=\Sigma x\,p(x)=3', r'(ii)\ \text{By property}\quad E(X+10)=E(X)+10=3+10=13', r'(iii)\quad E(X-10)=E(X)-10=3-10=-7',
          r'(iv)\quad E(10X)=10E(X)=10(3)=30', r'(v)\quad E\left(\frac{X}{10}\right)=\frac{E(X)}{10}=\frac{3}{10}=0.3'])
b.h('2.2.8 Variance and standard deviation of a random variable', '2.2.8 تصادفی متغیر کا تغیر اور معیاری انحراف', '2.2.8 د تصادفي متغیر واریانس او معیاري انحراف')
b.p('If X is a random variable, then its variance is denoted by Var(X) or V(X) and its formula is given by', 'اگر X ایک تصادفی متغیر ہو تو اس کے تغیر کو Var(X) یا V(X) سے ظاہر کرتے ہیں اور اس کا فارمولا یہ ہے', 'که X یو تصادفي متغیر وي، نو واریانس یې په Var(X) یا V(X) ښودل کېږي او فورمول یې دا دی')
b.mlines([r'V(X)=E[X-E(X)]^2', r'\text{Or } V(X)=E[X^2]-[E(X)]^2', r'S.D(X)=\sqrt{V(X)}'])
b.h('Example 2.13', 'مثال 2.13', 'بېلګه 2.13')
b.p('Consider the following discrete probability distribution:', 'درج ذیل منفصل احتمالی تقسیم پر غور کریں:', 'لاندې منفصل احتمالي وېش په پام کې ونیسئ:')
b.dist('stat12-t-ex2-13', ['3', '8', '10'], ['0.2', '0.7', '0.1'], total=None)
b.p('Determine the mean, variance and standard deviation.', 'اوسط، تغیر اور معیاری انحراف معلوم کریں۔', 'منځنی، واریانس او معیاري انحراف یې وټاکئ.')
b.h(*SOL)
b.grid('stat12-t-ex2-13-sol', ['$X$', '$p(x)$', '$X\\,p(x)$', '$X^2p(x)$'],
       [['3', '0.2', '0.6', '1.8'], ['8', '0.7', '5.6', '44.8'], ['10', '0.1', '1', '10.0'], ['Total', '1', '7.2', '56.6']])
b.mlines([r'\text{Mean}=E(X)=\Sigma x\,p(x)=7.2', r'\text{Variance}=V(X)=E(X^2)-[E(X)]^2=\Sigma x^2p(x)-[7.2]^2=56.6-51.84=4.76',
          r'\text{and}\quad S.D(X)=\sqrt{V(X)}=\sqrt{4.76}=2.181'])
b.h('2.2.9 Properties of variance and standard deviation of a random variable', '2.2.9 تصادفی متغیر کے تغیر اور معیاری انحراف کی خصوصیات', '2.2.9 د تصادفي متغیر د واریانس او معیاري انحراف ځانګړنې')
b.p('Following are some of the important properties.', 'ذیل میں چند اہم خصوصیات ہیں۔', 'لاندې ځینې مهمې ځانګړنې دي.')
b.p('(i) The variance and standard deviation of a constant is equal to zero i.e. $V(c)=0$ and $S.D(c)=0$, where c is a constant.',
    '(i) کسی مستقل کا تغیر اور معیاری انحراف صفر کے برابر ہوتا ہے یعنی $V(c)=0$ اور $S.D(c)=0$، جہاں c ایک مستقل ہے۔',
    '(i) د یوه ثابت واریانس او معیاري انحراف له صفر سره برابر دی یعنې $V(c)=0$ او $S.D(c)=0$، چې c یو ثابت دی.')
b.h(*PROOF)
b.p('By definition $V(X)=E[X-E(X)]^2$', 'تعریف کے مطابق $V(X)=E[X-E(X)]^2$', 'د تعریف له مخې $V(X)=E[X-E(X)]^2$')
b.p('As the variable X is taking only a constant value c, therefore', 'چونکہ متغیر X صرف ایک مستقل قیمت c لیتا ہے، اس لیے', 'څرنګه چې متغیر X یوازې یو ثابت قیمت c اخلي، نو')
b.mlines([r'V(c)=E[c-E(c)]^2', r'\phantom{V(c)}=E[c-c]^2\quad\because E(c)=c', r'\phantom{V(c)}=0', r'S.D(c)=\sqrt{0}=0'])
b.p('(ii) Variance and S.D of a random variable are not changed by adding/ subtracting a constant to/from the values of a random variable i.e.',
    '(ii) تصادفی متغیر کی قیمتوں میں کوئی مستقل جمع یا ان سے تفریق کرنے سے تصادفی متغیر کا تغیر اور معیاری انحراف تبدیل نہیں ہوتے، یعنی',
    '(ii) د تصادفي متغیر له قیمتونو سره د یوه ثابت په جمع یا تفریق کولو د تصادفي متغیر واریانس او معیاري انحراف نه بدلېږي، یعنې')
b.eq(r'V(X\pm c)=V(X)')
b.h(*PROOF)
b.p('By definition $V(X)=E[X-E(X)]^2$', 'تعریف کے مطابق $V(X)=E[X-E(X)]^2$', 'د تعریف له مخې $V(X)=E[X-E(X)]^2$')
b.p('As $(X+c)$ is a function of the random variable X, therefore,', 'چونکہ $(X+c)$ تصادفی متغیر X کا تفاعل ہے، اس لیے', 'څرنګه چې $(X+c)$ د تصادفي متغیر X تابع ده، نو')
b.mlines([r'V(X+c)=E[X+c-E(X+c)]^2', r'\phantom{V(X+c)}=E[X+c-E(X)-E(c)]^2'])
rec = b.build('stat12-p028-variance', '2.2.8 Variance and S.D. — Example 2.13 and 2.2.9 properties', '2.2.8 تغیر اور معیاری انحراف — مثال 2.13 اور 2.2.9 خصوصیات', '2.2.8 واریانس او معیاري انحراف — بېلګه 2.13 او 2.2.9 ځانګړنې', 28, [47, 48])

if __name__ == '__main__':
    save(28, [(2, rec)])
