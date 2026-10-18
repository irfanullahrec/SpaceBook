"""PDF29 printed 49–50: proof of property (ii) end, properties (iii)–(iv) of variance, Example 2.14 (i)–(v)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
PROOF = ('Proof:', 'ثبوت:', 'ثبوت:')
t = lambda n: f'$\\frac{{{n}}}{{10}}$'
b = Builder()
b.mlines([r'=E[X+c-E(X)-c]^2\quad\because E(c)=c', r'=E[X-E(X)]^2', r'=V(X)', r'\text{Similarly } V(X-c)=V(X)', r'S.D(X\pm c)=S.D(X)'])
b.p('(iii) If the values of a random variable are multiplied or divided by a constant, then its variance will change by the square of that constant i.e.',
    '(iii) اگر تصادفی متغیر کی قیمتوں کو کسی مستقل سے ضرب یا تقسیم کیا جائے تو اس کا تغیر اس مستقل کے مربع کے حساب سے بدل جائے گا، یعنی',
    '(iii) که د تصادفي متغیر قیمتونه په یوه ثابت کې ضرب یا پرې ووېشل شي، نو واریانس یې د هغه ثابت د مربع په اندازه بدلېږي، یعنې')
b.mlines([r'V(cX)=c^2\,V(X)', r'V\left(\frac{X}{c}\right)=\frac{V(X)}{c^2}'])
b.h(*PROOF)
b.p('By definition $V(X)=E[X-E(X)]^2$', 'تعریف کے مطابق $V(X)=E[X-E(X)]^2$', 'د تعریف له مخې $V(X)=E[X-E(X)]^2$')
b.p('As (cX) is function of the random variable X so,', 'چونکہ (cX) تصادفی متغیر X کا تفاعل ہے، لہٰذا', 'څرنګه چې (cX) د تصادفي متغیر X تابع ده، نو')
b.mlines([r'V(cX)=E[cX-E(cX)]^2', r'=E[cX-cE(X)]^2', r'=c^2E[X-E(X)]^2', r'=c^2\,V(X)',
          r'\text{Similarly } V\left(\frac{X}{c}\right)=\frac{V(X)}{c^2}', r'S.D(cX)=|c|\,S.D(X)', r'S.D\left(\frac{X}{c}\right)=\frac{S.D(X)}{|c|}'])
b.p('(iv) Variance and standard deviation can never be negative i.e. $V(X)\\ge 0$ and $S.D(X)\\ge 0$',
    '(iv) تغیر اور معیاری انحراف کبھی منفی نہیں ہو سکتے یعنی $V(X)\\ge 0$ اور $S.D(X)\\ge 0$',
    '(iv) واریانس او معیاري انحراف هېڅکله منفي نه شي کېدای یعنې $V(X)\\ge 0$ او $S.D(X)\\ge 0$')
b.h('Example 2.14', 'مثال 2.14', 'بېلګه 2.14')
b.p('A random variable X has the probability distribution given below', 'ایک تصادفی متغیر X کی احتمالی تقسیم نیچے دی گئی ہے', 'یو تصادفي متغیر X لاندې ورکړل شوی احتمالي وېش لري')
b.dist('stat12-t-ex2-14', ['0', '1', '2', '3'], [t(3), t(4), t(2), t(1)], total=None)
b.p('Find i) E(X), ii) V(X), iii) V(X+5), iv) V(X − 3), v) V(3X) vi) $S.D\\left(\\frac{X}{3}\\right)$',
    'معلوم کریں i) E(X)، ii) V(X)، iii) V(X+5)، iv) V(X − 3)، v) V(3X) vi) $S.D\\left(\\frac{X}{3}\\right)$',
    'پیدا کړئ i) E(X)، ii) V(X)، iii) V(X+5)، iv) V(X − 3)، v) V(3X) vi) $S.D\\left(\\frac{X}{3}\\right)$')
b.h(*SOL)
b.grid('stat12-t-ex2-14-sol', ['$X$', '$p(x)$', '$X\\,p(x)$', '$X^2p(x)$'],
       [['0', '3/10', '0', '0'], ['1', '4/10', '4/10', '4/10'], ['2', '2/10', '4/10', '8/10'], ['3', '1/10', '3/10', '9/10'], ['Total', '1', '11/10', '21/10']])
b.mlines([r'(i)\quad E(X)=\Sigma x\,p(x)=\frac{11}{10}=1.1', r'(ii)\quad V(X)=E(X^2)-[E(X)]^2=\Sigma x^2p(x)-(1.1)^2', r'=\frac{21}{10}-1.21', r'=2.1-1.21=0.89',
          r'(iii)\ \text{By property of variance}\ V(X+5)=V(X)=0.89', r'(iv)\quad V(X-3)=V(X)=0.89', r'(v)\quad V(3X)=3^2V(X)=9(0.89)=8.01'])
rec = b.build('stat12-p029-variance-properties', 'Properties (ii)–(iv) of variance — Example 2.14', 'تغیر کی خصوصیات (ii)–(iv) — مثال 2.14', 'د واریانس ځانګړنې (ii)–(iv) — بېلګه 2.14', 29, [49, 50])

if __name__ == '__main__':
    save(29, [(2, rec)])
