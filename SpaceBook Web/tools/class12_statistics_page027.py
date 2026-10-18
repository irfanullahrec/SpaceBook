"""PDF27 printed 45–46: 2.2.7 properties of mathematical expectation (i)–(ii) with proofs, consequences, Example 2.12 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
PROOF = ('Proof:', 'ثبوت:', 'ثبوت:')
b = Builder()
b.h('2.2.7 Properties of mathematical expectation', '2.2.7 ریاضیاتی توقع کی خصوصیات', '2.2.7 د ریاضي تمې ځانګړنې')
b.p('Expected value of a random variable satisfies the following properties.', 'تصادفی متغیر کی متوقع قیمت درج ذیل خصوصیات پوری کرتی ہے۔', 'د تصادفي متغیر تمه شوی قیمت لاندې ځانګړنې پوره کوي.')
b.p('(i) Expectation of a constant is the constant itself i.e. $E(c)=c$, where c is a constant.', '(i) کسی مستقل کی توقع خود وہی مستقل ہے یعنی $E(c)=c$، جہاں c ایک مستقل ہے۔', '(i) د یوه ثابت تمه پخپله هماغه ثابت دی یعنې $E(c)=c$، چې c یو ثابت دی.')
b.h(*PROOF)
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.eq(r'E(X)=\Sigma x\,p(x)')
b.p('As the variable X is taking only a constant value c therefore', 'چونکہ متغیر X صرف ایک مستقل قیمت c لیتا ہے، اس لیے', 'څرنګه چې متغیر X یوازې یو ثابت قیمت c اخلي، نو')
b.mlines([r'E(c)=\Sigma c\,p(x)', r'\phantom{E(c)}=c\Sigma p(x)'])
b.p('$\\phantom{E(c)}=c(1)$, as sum of probabilities $=\\Sigma p(x)=1$', '$\\phantom{E(c)}=c(1)$، کیونکہ احتمالات کا مجموعہ $=\\Sigma p(x)=1$', '$\\phantom{E(c)}=c(1)$، ځکه چې د احتمالونو مجموعه $=\\Sigma p(x)=1$')
b.eq(r'\phantom{E(c)}=c')
b.p('(ii) If a and b are two constants, then $E[aX+b]=a\\,E(X)+b$', '(ii) اگر a اور b دو مستقل ہوں تو $E[aX+b]=a\\,E(X)+b$', '(ii) که a او b دوه ثابتونه وي، نو $E[aX+b]=a\\,E(X)+b$')
b.h(*PROOF)
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.eq(r'E(X)=\Sigma x\,p(x)')
b.p('Here we have a function of the random variable X i.e. $aX+b$, so', 'یہاں ہمارے پاس تصادفی متغیر X کا تفاعل $aX+b$ ہے، لہٰذا', 'دلته د تصادفي متغیر X تابع $aX+b$ لرو، نو')
b.mlines([r'E(aX+b)=\Sigma(ax+b)\,p(x)', r'=\Sigma ax\,p(x)+\Sigma b\,p(x)', r'=a\Sigma x\,p(x)+b\Sigma p(x)', r'=a\,E(X)+b(1)', r'=a\,E(X)+b'])
b.p('This property shows that expectation is changed by that constant which is added to, subtracted from, multiplied with or divided by the values of a variable i.e.',
    'یہ خاصیت ظاہر کرتی ہے کہ توقع اسی مستقل سے بدلتی ہے جو متغیر کی قیمتوں میں جمع کیا جائے، ان سے تفریق کیا جائے، ان سے ضرب دیا جائے یا ان پر تقسیم کیا جائے، یعنی',
    'دا ځانګړنه ښيي چې تمه په هماغه ثابت بدلېږي چې د متغیر له قیمتونو سره جمع، ترې تفریق، ورسره ضرب یا پرې وېشل کېږي، یعنې')
b.mlines([r'(i)\quad E[X+c]=E(X)+c\qquad(ii)\quad E[X-c]=E(X)-c', r'(iii)\quad E(cX)=c\,E(X)\qquad(iv)\quad E\left(\frac{X}{c}\right)=\frac{E(X)}{c}'])
b.p('where X is a random variable and c is any constant.', 'جہاں X ایک تصادفی متغیر اور c کوئی بھی مستقل ہے۔', 'چې X یو تصادفي متغیر او c هر ثابت دی.')
b.h('Example 2.12', 'مثال 2.12', 'بېلګه 2.12')
b.p('Suppose that X is a simple discrete random variable, distributed as follows:', 'فرض کریں X ایک سادہ منفصل تصادفی متغیر ہے جس کی تقسیم یوں ہے:', 'فرض کړئ X یو ساده منفصل تصادفي متغیر دی چې وېش یې داسې دی:')
b.dist('stat12-t-ex2-12', ['2', '4'], ['0.50', '0.50'], total=None, vertical=True)
b.p('Find (i) E(X) (ii) E(X+10) (iii) E(X − 10) (iv) E(10X) (v) $E\\left(\\frac{X}{10}\\right)$', 'معلوم کریں (i) E(X) (ii) E(X+10) (iii) E(X − 10) (iv) E(10X) (v) $E\\left(\\frac{X}{10}\\right)$', 'پیدا کړئ (i) E(X) (ii) E(X+10) (iii) E(X − 10) (iv) E(10X) (v) $E\\left(\\frac{X}{10}\\right)$')
b.h(*SOL)
b.p('Given', 'دیا گیا', 'ورکړل شوي')
b.grid('stat12-t-ex2-12-sol', ['$X$', '$p(x)$', '$X\\,p(x)$'], [['2', '0.50', '1'], ['4', '0.50', '2'], ['Total', '1', '3']])
rec = b.build('stat12-p027-expectation-properties', '2.2.7 Properties of mathematical expectation', '2.2.7 ریاضیاتی توقع کی خصوصیات', '2.2.7 د ریاضي تمې ځانګړنې', 27, [45, 46])

if __name__ == '__main__':
    save(27, [(2, rec)])
