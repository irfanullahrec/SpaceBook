"""PDF33 printed 57–58: marginal distributions, 2.4.3 bivariate probability function, 2.4.4 independence, 2.4.5 expectation of two r.v.s, 2.4.6 property (i) proof start."""
from class12_statistics_common import Builder, save

PROOF = ('Proof:', 'ثبوت:', 'ثبوت:')
b = Builder()
b.h('Marginal probability distributions', 'حاشیائی احتمالی تقسیمیں', 'څنډې احتمالي وېشونه')
b.p('From the bivariate probability distribution we can obtain univariate probability distributions as:', 'دو متغیری احتمالی تقسیم سے ہم یک متغیری احتمالی تقسیمیں یوں حاصل کر سکتے ہیں:', 'له دوه متغیره احتمالي وېش څخه یو متغیره احتمالي وېشونه داسې لاسته راوړلای شو:')
b.p('(i) The marginal probability distribution of X', '(i) X کی حاشیائی احتمالی تقسیم', '(i) د X څنډې احتمالي وېش')
b.grid('stat12-t-marginal-x', ['$X$', '$p(x)$'], [['$x_1$', '$p(x_1)$'], ['$x_2$', '$p(x_2)$'], ['$\\vdots$', '$\\vdots$'], ['$x_i$', '$p(x_i)$'], ['$\\vdots$', '$\\vdots$'], ['$x_m$', '$p(x_m)$'], ['Total', '1']])
b.p('(ii) The marginal probability distribution of Y', '(ii) Y کی حاشیائی احتمالی تقسیم', '(ii) د Y څنډې احتمالي وېش')
b.grid('stat12-t-marginal-y', ['$Y$', '$p(y)$'], [['$y_1$', '$p(y_1)$'], ['$y_2$', '$p(y_2)$'], ['$\\vdots$', '$\\vdots$'], ['$y_j$', '$p(y_j)$'], ['$\\vdots$', '$\\vdots$'], ['$y_n$', '$p(y_n)$'], ['Total', '1']])
b.h('2.4.3 Bivariate probability function', '2.4.3 دو متغیری احتمالی تفاعل', '2.4.3 دوه متغیره احتمالي تابع')
b.p('If all possible values of two random variables with their associated probabilities are shown by a formula, then it is called bivariate probability function. It is denoted by $p(x_i,y_j)$ (discrete case) and $f(x_i,y_j)$ (continuous case); for all $x_i$ and $y_j$.',
    'اگر دو تصادفی متغیرات کی تمام ممکنہ قیمتیں ان کے متعلقہ احتمالات کے ساتھ کسی فارمولا سے دکھائی جائیں تو اسے دو متغیری احتمالی تفاعل کہتے ہیں۔ اسے تمام $x_i$ اور $y_j$ کے لیے $p(x_i,y_j)$ (منفصل صورت) اور $f(x_i,y_j)$ (مسلسل صورت) سے ظاہر کرتے ہیں۔',
    'که د دوو تصادفي متغیرونو ټول شوني قیمتونه له اړوندو احتمالونو سره د یوه فورمول په واسطه وښودل شي، نو دوه متغیره احتمالي تابع بلل کېږي. د ټولو $x_i$ او $y_j$ لپاره په $p(x_i,y_j)$ (منفصل حالت) او $f(x_i,y_j)$ (متصل حالت) ښودل کېږي.')
b.h('2.4.4 Independence of two random variables', '2.4.4 دو تصادفی متغیرات کی آزادی', '2.4.4 د دوو تصادفي متغیرونو خپلواکي')
b.p('Two random variables X and Y are statistically independent if and only if their bivariate probability function can be expressed as the product of the marginal probability functions i.e.',
    'دو تصادفی متغیرات X اور Y شماریاتی طور پر آزاد ہوتے ہیں اگر اور صرف اگر ان کے دو متغیری احتمالی تفاعل کو حاشیائی احتمالی تفاعلات کے حاصلِ ضرب کے طور پر ظاہر کیا جا سکے یعنی',
    'دوه تصادفي متغیرونه X او Y هغه وخت او یوازې هغه وخت احصاییوي خپلواک دي چې د هغو دوه متغیره احتمالي تابع د څنډو احتمالي تابع ګانو د ضرب په بڼه وښودل شي یعنې')
b.eq(r'f(x_i,y_j)=f(x_i)\,f(y_j)')
b.h('2.4.5 Mathematical expectation of two random variables', '2.4.5 دو تصادفی متغیرات کی ریاضیاتی توقع', '2.4.5 د دوو تصادفي متغیرونو ریاضي تمه')
b.p('If X and Y are two random variables then mean or expected value of their sum or difference is denoted by $E(X\\pm Y)$ and is defined as:',
    'اگر X اور Y دو تصادفی متغیرات ہوں تو ان کے مجموعے یا فرق کا اوسط یا متوقع قیمت $E(X\\pm Y)$ سے ظاہر کی جاتی ہے اور اس کی تعریف یہ ہے:',
    'که X او Y دوه تصادفي متغیرونه وي، نو د هغو د مجموعې یا توپیر منځنی یا تمه شوی قیمت په $E(X\\pm Y)$ ښودل کېږي او داسې تعریف کېږي:')
b.group('lines', [
    ('$E(X\\pm Y)=\\sum_i\\sum_j(x_i\\pm y_j)\\,p(x_i,y_j)$ (discrete random variables case)', '$E(X\\pm Y)=\\sum_i\\sum_j(x_i\\pm y_j)\\,p(x_i,y_j)$ (منفصل تصادفی متغیرات کی صورت)', '$E(X\\pm Y)=\\sum_i\\sum_j(x_i\\pm y_j)\\,p(x_i,y_j)$ (د منفصلو تصادفي متغیرونو حالت)'),
    ('$\\phantom{E(X\\pm Y)}=\\iint_{xy}(x_i\\pm y_j)\\,f(x_i,y_j)\\,dx_i\\,dy_j$ (continuous random variables case)', '$\\phantom{E(X\\pm Y)}=\\iint_{xy}(x_i\\pm y_j)\\,f(x_i,y_j)\\,dx_i\\,dy_j$ (مسلسل تصادفی متغیرات کی صورت)', '$\\phantom{E(X\\pm Y)}=\\iint_{xy}(x_i\\pm y_j)\\,f(x_i,y_j)\\,dx_i\\,dy_j$ (د متصلو تصادفي متغیرونو حالت)'),
])
b.p('Expected value of their product is', 'ان کے حاصلِ ضرب کی متوقع قیمت یہ ہے', 'د هغو د ضرب حاصل تمه شوی قیمت دا دی')
b.group('lines', [
    ('$E(XY)=\\sum_j\\sum_i(x_iy_j)\\,p(x_i,y_j)$ (for discrete case)', '$E(XY)=\\sum_j\\sum_i(x_iy_j)\\,p(x_i,y_j)$ (منفصل صورت کے لیے)', '$E(XY)=\\sum_j\\sum_i(x_iy_j)\\,p(x_i,y_j)$ (د منفصل حالت لپاره)'),
    ('$\\phantom{E(XY)}=\\iint_{xy}(x_iy_j)\\,f(x_i,y_j)\\,dx_i\\,dy_j$ (for continuous case)', '$\\phantom{E(XY)}=\\iint_{xy}(x_iy_j)\\,f(x_i,y_j)\\,dx_i\\,dy_j$ (مسلسل صورت کے لیے)', '$\\phantom{E(XY)}=\\iint_{xy}(x_iy_j)\\,f(x_i,y_j)\\,dx_i\\,dy_j$ (د متصل حالت لپاره)'),
])
b.h('2.4.6 Properties of mathematical expectation of two random variables', '2.4.6 دو تصادفی متغیرات کی ریاضیاتی توقع کی خصوصیات', '2.4.6 د دوو تصادفي متغیرونو د ریاضي تمې ځانګړنې')
b.p('Let X and Y are two independent random variables and then they jointly have the following properties:', 'فرض کریں X اور Y دو آزاد تصادفی متغیرات ہیں، تو ان کی مشترکہ طور پر درج ذیل خصوصیات ہیں:', 'فرض کړئ X او Y دوه خپلواک تصادفي متغیرونه دي، نو په ګډه لاندې ځانګړنې لري:')
b.p('(i) The expected value of the sum of two random variables is equal to the sum of the expected values of the individual random variables i.e.',
    '(i) دو تصادفی متغیرات کے مجموعے کی متوقع قیمت انفرادی تصادفی متغیرات کی متوقع قیمتوں کے مجموعے کے برابر ہے یعنی',
    '(i) د دوو تصادفي متغیرونو د مجموعې تمه شوی قیمت د جلا جلا تصادفي متغیرونو د تمه شویو قیمتونو له مجموعې سره برابر دی یعنې')
b.eq(r'E(X+Y)=E(X)+E(Y)')
b.h(*PROOF)
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'E(X+Y)=\sum_{i=1}^{m}\sum_{j=1}^{n}(x_i+y_j)\,p(x_i,y_j)', r'=\sum_{i=1}^{m}\sum_{j=1}^{n}x_i\,p(x_i,y_j)+\sum_{i=1}^{m}\sum_{j=1}^{n}y_j\,p(x_i,y_j)\qquad(1)',
          r'\text{Consider }\sum_{i=1}^{m}\sum_{j=1}^{n}x_i\,p(x_i,y_j)', r'=\sum_{i=1}^{m}x_i\sum_{j=1}^{n}p(x_i,y_j)'])
rec = b.build('stat12-p033-two-variables', 'Marginal distributions, independence and expectation of two random variables', 'حاشیائی تقسیمیں، آزادی اور دو تصادفی متغیرات کی توقع', 'څنډې وېشونه، خپلواکي او د دوو تصادفي متغیرونو تمه', 33, [57, 58])

if __name__ == '__main__':
    save(33, [(2, rec)])
