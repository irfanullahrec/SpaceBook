"""PDF32 printed 55–56: Example 2.17 solution; 2.4 two independent random variables, 2.4.1 joint distributions, 2.4.2 bivariate table."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h(*SOL)
b.mlines([r'(i)\quad E(X)=\int_x x\,f(x)\,dx=\int_{0}^{1}x(2-2x)\,dx=\int_{0}^{1}(2x-2x^2)\,dx',
          r'=\int_{0}^{1}2x\,dx-\int_{0}^{1}2x^2\,dx=2\int_{0}^{1}x\,dx-2\int_{0}^{1}x^2dx', r'=\left.x^2\right|_{0}^{1}-2\left.\frac{x^3}{3}\right|_{0}^{1}',
          r'=(1-0)-\left(\frac{2}{3}-0\right)=1-\frac{2}{3}=\frac{3-2}{3}=\frac{1}{3}',
          r'(ii)\quad E(X^2)=\int_x x^2f(x)\,dx=\int_{0}^{1}x^2(2-2x)\,dx=\int_{0}^{1}(2x^2-2x^3)\,dx',
          r'=2\int_{0}^{1}x^2dx-2\int_{0}^{1}x^3dx=2\left(\left.\frac{x^3}{3}\right|_{0}^{1}\right)-2\left(\left.\frac{x^4}{4}\right|_{0}^{1}\right)',
          r'=2\left(\frac{1}{3}-0\right)-2\left(\frac{1}{4}-0\right)=\frac{2}{3}-\frac{1}{2}=\frac{4-3}{6}=\frac{1}{6}'])
b.p('(iii) $E(2X)=2E(X)$, (By property)', '(iii) $E(2X)=2E(X)$، (خاصیت کے مطابق)', '(iii) $E(2X)=2E(X)$، (د ځانګړنې له مخې)')
b.mlines([r'=2(1/3)=2/3', r'(iv)\quad E(2X-1)=2E(X)-1=2\left(\tfrac{1}{3}\right)-1=-1/3', r'(v)\quad\text{Variance}=V(X)=E(X^2)-[E(X)]^2',
          r'=\frac{1}{6}-\left(\frac{1}{3}\right)^2=\frac{1}{6}-\frac{1}{9}=\frac{3-2}{18}=\frac{1}{18}=0.056', r'S.D(X)=\sqrt{0.056}=0.24'])
ex = b.build('stat12-p032-example-2-17', 'Example 2.17 — solution', 'مثال 2.17 — حل', 'بېلګه 2.17 — حل', 32, [55])

c = Builder()
c.h('2.4 Two independent random variables', '2.4 دو آزاد تصادفی متغیرات', '2.4 دوه خپلواک تصادفي متغیرونه')
c.p('This is an extension of the one random variable case. The problem will be to recognize the old ideas behind the new names.',
    'یہ ایک تصادفی متغیر والی صورت کی توسیع ہے۔ مسئلہ یہ ہوگا کہ نئے ناموں کے پیچھے پرانے تصورات کو پہچانا جائے۔',
    'دا د یوه تصادفي متغیر د حالت پراختیا ده. ستونزه به دا وي چې د نویو نومونو تر شا زاړه مفهومونه وپېژنو.')
c.h('2.4.1 Joint distributions', '2.4.1 مشترکہ تقسیمیں', '2.4.1 ګډ وېشونه')
c.p('The distribution of two or more random variables is called joint distribution. Specifically;', 'دو یا زیادہ تصادفی متغیرات کی تقسیم کو مشترکہ تقسیم کہتے ہیں۔ خاص طور پر؛', 'د دوو یا ډېرو تصادفي متغیرونو وېش ته ګډ وېش وایي. په ځانګړې توګه؛')
c.group('lines', [
    ('The distribution of one random variable is called univariate probability distribution.', 'ایک تصادفی متغیر کی تقسیم کو یک متغیری احتمالی تقسیم کہتے ہیں۔', 'د یوه تصادفي متغیر وېش ته یو متغیره احتمالي وېش وایي.'),
    ('The distribution of two random variables is called bivariate probability distribution.', 'دو تصادفی متغیرات کی تقسیم کو دو متغیری احتمالی تقسیم کہتے ہیں۔', 'د دوو تصادفي متغیرونو وېش ته دوه متغیره احتمالي وېش وایي.'),
    ('The distribution of three random variables is called trivariate probability distribution.', 'تین تصادفی متغیرات کی تقسیم کو سہ متغیری احتمالی تقسیم کہتے ہیں۔', 'د درېیو تصادفي متغیرونو وېش ته درې متغیره احتمالي وېش وایي.'),
    ('The distribution of many random variables is called multivariate probability distribution.', 'بہت سے تصادفی متغیرات کی تقسیم کو کثیر متغیری احتمالی تقسیم کہتے ہیں۔', 'د ډېرو تصادفي متغیرونو وېش ته څو متغیره احتمالي وېش وایي.'),
])
c.h('2.4.2 Bivariate probability distribution', '2.4.2 دو متغیری احتمالی تقسیم', '2.4.2 دوه متغیره احتمالي وېش')
c.p('If all possible values of two random variables along with their joint probabilities are presented in tabular form then, it is called bivariate probability distribution. Suppose X and Y are two discrete random variables, where X has “m” values and Y has “n” values, then bivariate probability distribution of X and Y is given by',
    'اگر دو تصادفی متغیرات کی تمام ممکنہ قیمتیں ان کے مشترکہ احتمالات کے ساتھ جدولی شکل میں پیش کی جائیں تو اسے دو متغیری احتمالی تقسیم کہتے ہیں۔ فرض کریں X اور Y دو منفصل تصادفی متغیرات ہیں جن میں X کی “m” قیمتیں اور Y کی “n” قیمتیں ہیں، تو X اور Y کی دو متغیری احتمالی تقسیم یہ ہے',
    'که د دوو تصادفي متغیرونو ټول شوني قیمتونه له ګډو احتمالونو سره په جدولي بڼه وړاندې شي، نو دوه متغیره احتمالي وېش بلل کېږي. فرض کړئ X او Y دوه منفصل تصادفي متغیرونه دي، چې X “m” قیمتونه او Y “n” قیمتونه لري، نو د X او Y دوه متغیره احتمالي وېش دا دی')
D = r'\cdots'
c.grid('stat12-t-bivariate-general', ['$X\\backslash Y$', '$y_1$', '$y_2$', '$\\cdots$', '$y_j$', '$\\cdots$', '$y_n$', '$p(x)$'], [
    ['$x_1$', '$p(x_1,y_1)$', '$p(x_1,y_2)$', f'${D}$', '$p(x_1,y_j)$', f'${D}$', '$p(x_1,y_n)$', '$p(x_1)$'],
    ['$x_2$', '$p(x_2,y_1)$', '$p(x_2,y_2)$', f'${D}$', '$p(x_2,y_j)$', f'${D}$', '$p(x_2,y_n)$', '$p(x_2)$'],
    ['$\\vdots$', '', '', '$\\vdots$', '', '$\\vdots$', '$\\vdots$', '$\\vdots$'],
    ['$x_i$', '$p(x_i,y_1)$', '$p(x_i,y_2)$', f'${D}$', '$p(x_i,y_j)$', f'${D}$', '$p(x_i,y_n)$', '$p(x_i)$'],
    ['$\\vdots$', '', '', '$\\vdots$', '', '$\\vdots$', '$\\vdots$', '$\\vdots$'],
    ['$x_m$', '$p(x_m,y_1)$', '$p(x_m,y_2)$', f'${D}$', '$p(x_m,y_j)$', f'${D}$', '$p(x_m,y_n)$', '$p(x_m)$'],
    ['$p(y)$', '$p(y_1)$', '$p(y_2)$', f'${D}$', '$p(y_j)$', f'${D}$', '$p(y_n)$', '1']])
bv = c.build('stat12-p032-joint-distributions', '2.4 Two independent random variables — joint and bivariate distributions', '2.4 دو آزاد تصادفی متغیرات — مشترکہ اور دو متغیری تقسیمیں', '2.4 دوه خپلواک تصادفي متغیرونه — ګډ او دوه متغیره وېشونه', 32, [56])

if __name__ == '__main__':
    save(32, [(2, ex), (2, bv)])
