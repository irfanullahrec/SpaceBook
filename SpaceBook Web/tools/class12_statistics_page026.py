"""PDF26 printed 43–44: Example 2.9 end, 2.2.6 expectation of a function of a discrete r.v., Examples 2.10–2.11."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
H = r'\left(\frac{1}{2}\right)'
b = Builder()
b.mlines([r'=3(0.2)+8(0.7)+10(0.1)', r'E(X)=0.6+5.6+1=7.2'])
b.h('2.2.6 Mathematical expectation of a function of discrete random variable', '2.2.6 منفصل تصادفی متغیر کے تفاعل کی ریاضیاتی توقع', '2.2.6 د منفصل تصادفي متغیر د تابع ریاضي تمه')
b.p('If function of a random variable is denoted by H(X), then expected value of the function is denoted by E[H(X)] and its formula is given by $E[H(X)]=\\Sigma H(x_i)p(x_i)$.',
    'اگر تصادفی متغیر کے تفاعل کو H(X) سے ظاہر کیا جائے تو اس تفاعل کی متوقع قیمت کو E[H(X)] سے ظاہر کرتے ہیں اور اس کا فارمولا $E[H(X)]=\\Sigma H(x_i)p(x_i)$ ہے۔',
    'که د تصادفي متغیر تابع په H(X) وښودل شي، نو د تابع تمه شوی قیمت په E[H(X)] ښودل کېږي او فورمول یې $E[H(X)]=\\Sigma H(x_i)p(x_i)$ دی.')
b.h('Example 2.10', 'مثال 2.10', 'بېلګه 2.10')
b.p('A discrete random variable X has the probability distribution:', 'ایک منفصل تصادفی متغیر X کی احتمالی تقسیم یہ ہے:', 'یو منفصل تصادفي متغیر X دا احتمالي وېش لري:')
b.dist('stat12-t-ex2-10', ['−2', '1', '3'], ['$\\frac{1}{3}$', '$\\frac{1}{6}$', '$\\frac{1}{2}$'], total=None)
b.p('Find (i) $E(X^2)$ (ii) $E(2X+5)$', 'معلوم کریں (i) $E(X^2)$ (ii) $E(2X+5)$', 'پیدا کړئ (i) $E(X^2)$ (ii) $E(2X+5)$')
b.h(*SOL)
b.p('Since $X^2$ and $(2X+5)$ are functions of the given random variable X, therefore, we first find their probability distributions and then the means as follows:',
    'چونکہ $X^2$ اور $(2X+5)$ دیے گئے تصادفی متغیر X کے تفاعل ہیں، اس لیے ہم پہلے ان کی احتمالی تقسیمیں اور پھر اوسط یوں معلوم کرتے ہیں:',
    'څرنګه چې $X^2$ او $(2X+5)$ د ورکړل شوي تصادفي متغیر X تابع ګانې دي، نو لومړی د هغو احتمالي وېشونه او بیا منځني داسې پیدا کوو:')
b.grid('stat12-t-ex2-10-sol', ['$X$', '$p(x)$', '$H(X)=X^2$', '$H(X)=2X+5$', '$X^2p(x)$', '$(2X+5)p(x)$'],
       [['−2', '$\\frac{1}{3}$', '4', '1', '$\\frac{4}{3}=1.33$', '$\\frac{1}{3}=0.33$'],
        ['1', '$\\frac{1}{6}$', '1', '7', '$\\frac{1}{6}=0.17$', '$\\frac{7}{6}=1.17$'],
        ['3', '$\\frac{1}{2}$', '9', '11', '$\\frac{9}{2}=4.5$', '$\\frac{11}{2}=5.5$'],
        ['Total', '1', '-', '-', '6', '7']])
b.mlines([r'\text{Now}\quad E\{H(X)\}=\Sigma H(x_i)\,p(x_i)', r'(i)\quad E\{X^2\}=\Sigma x_i^2\,p(x_i)=6', r'(ii)\quad E\{2X+5\}=\Sigma(2x_i+5)\,p(x_i)=7'])
b.h('Example 2.11', 'مثال 2.11', 'بېلګه 2.11')
b.p('The probability function of a discrete random variable Y is given by', 'ایک منفصل تصادفی متغیر Y کا احتمالی تفاعل یہ ہے', 'د یوه منفصل تصادفي متغیر Y احتمالي تابع دا ده')
b.eq(r'p(y)=\left\{\begin{matrix}{}^{3}_{y}C' + H + r'^{y}' + H + r'^{3-y}, & y=0,1,2,3\\ 0 & \textit{otherwise}\end{matrix}\right\}')
b.p('Find E(Y) and E(Y²).', 'E(Y) اور E(Y²) معلوم کریں۔', 'E(Y) او E(Y²) پیدا کړئ.')
b.h(*SOL)
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'E(Y)=\sum_{y=0}^{3}y_i\,p(y_i)', r'=\sum_{y=0}^{3}y\,{}^{3}_{y}C' + H + '^{y}' + H + '^{3-y}',
          r'=0\,{}^{3}_{0}C' + H + '^{0}' + H + r'^{3-0}+1\,{}^{3}_{1}C' + H + '^{1}' + H + r'^{3-1}+2\,{}^{3}_{2}C' + H + '^{2}' + H + r'^{3-2}+3\,{}^{3}_{3}C' + H + '^{3}' + H + '^{3-3}',
          r'=0+3\left(\frac{1}{8}\right)+6\left(\frac{1}{8}\right)+3\left(\frac{1}{8}\right)=\frac{12}{8}=1.5',
          r'E(Y^2)=\sum_{y=0}^{3}y^2\,{}^{3}_{y}C' + H + '^{y}' + H + '^{3-y}',
          r'=0\,{}^{3}_{0}C' + H + '^{0}' + H + r'^{3-0}+1\,{}^{3}_{1}C' + H + '^{1}' + H + r'^{3-1}+4\,{}^{3}_{2}C' + H + '^{2}' + H + r'^{3-2}+9\,{}^{3}_{3}C' + H + '^{3}' + H + '^{3-3}',
          r'=0+3\left(\frac{1}{8}\right)+12\left(\frac{1}{8}\right)+9\left(\frac{1}{8}\right)=\frac{24}{8}=3'])
rec = b.build('stat12-p026-expectation-function', '2.2.6 Expectation of a function — Examples 2.10–2.11', '2.2.6 تفاعل کی توقع — مثالیں 2.10–2.11', '2.2.6 د تابع تمه — بېلګې 2.10–2.11', 26, [43, 44])
issues = [{'id': 'stat12-p44-exponent-scan', 'unit': 2, 'printedPage': 44, 'description': 'In the first expanded line of E(Y) the printed exponents are partly blurred in the scan; they are rendered as 3−0, 3−1, 3−2, 3−3 consistent with the E(Y²) line below.'}]

if __name__ == '__main__':
    save(26, [(2, rec)], issues=issues)
