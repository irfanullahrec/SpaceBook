"""PDF23 printed 37–38: Example 2.4 (ii)–(iv), Example 2.5 (k/15), Example 2.6 start (two-dice sum)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import DICE36

SOL = ('Solution:', 'حل:', 'حل:')
T = lambda n: f'$\\frac{{{n}}}{{12}}$'
b = Builder()
b.p('Putting the value of c in the given probability distribution, we get', 'دی گئی احتمالی تقسیم میں c کی قیمت رکھنے سے', 'په ورکړل شوي احتمالي وېش کې د c قیمت ایښودو سره')
b.dist('stat12-t-ex2-4b', ['-1', '0', '1'], [T(3), T(3), T(6)])
b.mlines([r'(ii)\quad\text{We see that } P(X=0)=\frac{3}{12}', r'(iii)\quad P(X<0)=P(X=-1)=\frac{3}{12}',
          r'(iv)\quad P(X\ge -1)=P(X=-1)+P(X=0)+P(X=1)', r'\phantom{(iv)\quad P(X\ge -1)}=\frac{3}{12}+\frac{3}{12}+\frac{6}{12}=\frac{12}{12}=1'])
b.h('Example 2.5', 'مثال 2.5', 'بېلګه 2.5')
b.p('Find the value of k so that the function can serve as a probability function of the random variable Y', 'k کی وہ قیمت معلوم کریں جس سے یہ تفاعل تصادفی متغیر Y کا احتمالی تفاعل بن سکے', 'د k هغه قیمت پیدا کړئ چې تابع د تصادفي متغیر Y احتمالي تابع شي')
b.p('$p(y)=\\left\\{\\begin{matrix}ky, & y=1,2,3,4,5\\\\ 0 & \\textit{otherwise}\\end{matrix}\\right\\}$. Also find (i) $P(Y=5)$ (ii) $P(Y>3)$',
    '$p(y)=\\left\\{\\begin{matrix}ky, & y=1,2,3,4,5\\\\ 0 & \\textit{otherwise}\\end{matrix}\\right\\}$۔ نیز معلوم کریں (i) $P(Y=5)$ (ii) $P(Y>3)$',
    '$p(y)=\\left\\{\\begin{matrix}ky, & y=1,2,3,4,5\\\\ 0 & \\textit{otherwise}\\end{matrix}\\right\\}$. همداراز پیدا کړئ (i) $P(Y=5)$ (ii) $P(Y>3)$')
b.h(*SOL)
b.p('As we know that', 'جیسا کہ ہم جانتے ہیں', 'لکه څنګه چې پوهېږو')
b.mlines([r'\sum_{y=1}^{5}p(y)=1', r'\sum_{y=1}^{5}ky=1', r'k\sum_{y=1}^{5}y=1', r'k[1+2+3+4+5]=1', r'k(15)=1\quad\Rightarrow k=\frac{1}{15}'])
b.p('Put value of k in the given function we get', 'دیے گئے تفاعل میں k کی قیمت رکھنے سے', 'په ورکړل شوې تابع کې د k قیمت ایښودو سره')
b.eq(r'p(y)=\left\{\begin{matrix}\frac{1}{15}y, & y=1,2,3,4,5\\ 0 & \textit{otherwise}\end{matrix}\right\}')
b.p('(i) Putting Y = 5 in the formula, we have $P(Y=5)=\\frac{5}{15}$', '(i) فارمولا میں Y = 5 رکھنے سے $P(Y=5)=\\frac{5}{15}$', '(i) په فورمول کې Y = 5 ایښودو سره $P(Y=5)=\\frac{5}{15}$')
b.eq(r'(ii)\quad P(Y>3)=P(Y=4)+P(Y=5)=\frac{4}{15}+\frac{5}{15}=\frac{9}{15}')
b.h('Example 2.6', 'مثال 2.6', 'بېلګه 2.6')
b.p('A pair of fair dice is rolled. Find (i) the probability distribution for the sum of dots. (ii) Using the probability distribution, compute the probabilities of (a) sum of dots is equal to 7 (b) sum of dots is less than 6 (c) sum of dots is greater than or equal to 2 but less than 5 (d) sum of dots is 5 or 10.',
    'منصفانہ پانسوں کا ایک جوڑا پھینکا جاتا ہے۔ معلوم کریں (i) نقطوں کے مجموعے کی احتمالی تقسیم۔ (ii) احتمالی تقسیم کی مدد سے احتمالات معلوم کریں کہ (a) نقطوں کا مجموعہ 7 ہو (b) نقطوں کا مجموعہ 6 سے کم ہو (c) نقطوں کا مجموعہ 2 یا اس سے زیادہ لیکن 5 سے کم ہو (d) نقطوں کا مجموعہ 5 یا 10 ہو۔',
    'د عادلانه ډایسونو یوه جوړه اچول کېږي. پیدا کړئ (i) د ټکو د مجموعې احتمالي وېش. (ii) د احتمالي وېش په کارولو سره احتمالونه محاسبه کړئ چې (a) د ټکو مجموعه 7 وي (b) د ټکو مجموعه له 6 کمه وي (c) د ټکو مجموعه له 2 سره برابره یا زیاته خو له 5 کمه وي (d) د ټکو مجموعه 5 یا 10 وي.')
b.h(*SOL)
b.eq(r'(i)\quad n(S)=6^n=6^2=36')
b.p('The sample space for the experiment is:', 'تجربے کی نمونہ فضا یہ ہے:', 'د تجربې نمونوي فضا دا ده:')
b.eq(DICE36)
b.p('Let X is a random variable denoting the sum of dots on the upper faces of the two dice. Its probability distribution is:',
    'فرض کریں X ایک تصادفی متغیر ہے جو دونوں پانسوں کے اوپری رخوں کے نقطوں کا مجموعہ ظاہر کرتا ہے۔ اس کی احتمالی تقسیم یہ ہے:',
    'فرض کړئ X یو تصادفي متغیر دی چې د دواړو ډایسونو د پورتنیو مخونو د ټکو مجموعه ښيي. احتمالي وېش یې دا دی:')
rec = b.build('stat12-p023-examples-2-4-2-6', 'Examples 2.4–2.6', 'مثالیں 2.4–2.6', 'بېلګې 2.4–2.6', 23, [37, 38])

if __name__ == '__main__':
    save(23, [(2, rec)])
