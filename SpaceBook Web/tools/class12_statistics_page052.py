"""PDF52 printed 95–96: Example 3.18 (fitting a binomial, expected frequencies), Example 3.19 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h('Example 3.18', 'مثال 3.18', 'بېلګه 3.18')
b.p('Fit a Binomial distribution to the following data and compute expected frequencies:', 'درج ذیل مواد پر دو رقمی تقسیم منطبق کریں اور متوقع تعدد معلوم کریں:', 'په لاندې معلوماتو بینومیل وېش برابر کړئ او تمه شوې فریکونسۍ محاسبه کړئ:')
b.grid('stat12-t-ex3-18', ['$X$', '0', '1', '2', '3', '4'], [['$f$', '30', '62', '46', '10', '2']])
b.h(*SOL)
b.p('First we compute mean of the given frequency distribution', 'پہلے ہم دی گئی تعددی تقسیم کا اوسط معلوم کرتے ہیں', 'لومړی د ورکړل شوي فریکونسي وېش منځنی محاسبه کوو')
b.grid('stat12-t-ex3-18-mean', ['$X$', '0', '1', '2', '3', '4', 'Total'], [['$f$', '30', '62', '46', '10', '2', '150'], ['$fx$', '0', '62', '92', '30', '8', '192']])
b.p('Given that n = 4, N = 150. Now for Binomial distribution $\\mu=np$ but here μ is unknown so we replace μ with its estimator $\\overline{X}$.',
    'دیا گیا ہے n = 4، N = 150۔ دو رقمی تقسیم کے لیے $\\mu=np$ ہے لیکن یہاں μ نامعلوم ہے، اس لیے ہم μ کو اس کے تخمین کار $\\overline{X}$ سے بدل دیتے ہیں۔',
    'ورکړل شوي n = 4، N = 150. د بینومیل وېش لپاره $\\mu=np$ دی خو دلته μ نامعلوم دی، نو μ د هغه په اټکلوونکي $\\overline{X}$ بدلوو.')
b.mlines([r'\overline{X}=\frac{\Sigma fx}{\Sigma f}=\frac{192}{150}=1.28', r'\therefore\overline{X}=np\quad\Rightarrow 1.28=np', r'\text{Or } 1.28=4p\quad\Rightarrow p=\frac{1.28}{4}=0.32\quad\therefore q=0.68'])
b.p('The fitted Binomial distribution is:', 'منطبق کی گئی دو رقمی تقسیم یہ ہے:', 'برابره شوې بینومیل وېش دا دی:')
b.eq(r'p(x)=\left\{\begin{matrix}{}^{4}_{x}C(0.32)^x(0.68)^{4-x}, & x=0,1,2,3,4\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('The expected frequencies are computed as:', 'متوقع تعدد یوں معلوم کیے جاتے ہیں:', 'تمه شوې فریکونسۍ داسې محاسبه کېږي:')
rows = []
for k, v, ef in [(0, '0.213814', '$150\\times 0.213814=32$'), (1, '0.402478', '$150\\times 0.402478=60$'), (2, '0.284099', '$=43$'), (3, '0.089129', '$=13$'), (4, '0.010486', '$=02$')]:
    rows.append([str(k), f'${{}}^{{4}}_{{{k}}}C(0.32)^{{{k}}}(0.68)^{{4-{k}}}={v}$', ef])
rows.append(['Total', '1', '150'])
b.grid('stat12-t-ex3-18-fit', ['$X$', '$p(x)={}^{4}_{x}C(0.32)^x(0.68)^{4-x}$', '$E_f=N\\,p(x)$'], rows)
ex18 = b.build('stat12-p052-example-3-18', 'Example 3.18 — fitting a binomial distribution', 'مثال 3.18 — دو رقمی تقسیم کا انطباق', 'بېلګه 3.18 — د بینومیل وېش برابرول', 52, [95, 96])

c = Builder()
c.h('Example 3.19', 'مثال 3.19', 'بېلګه 3.19')
c.p('Suppose that seven coins are tossed and the number of heads noted. This experiment is repeated 128 times (i) fit a Binomial distribution under the hypothesis that the coins are unbiased. (ii) compute the theoretical frequencies. (iii) find its mean and standard deviation.',
    'فرض کریں سات سکے اچھالے جاتے ہیں اور چِت کی تعداد نوٹ کی جاتی ہے۔ یہ تجربہ 128 بار دہرایا جاتا ہے (i) اس مفروضے کے تحت دو رقمی تقسیم منطبق کریں کہ سکے غیر جانبدار ہیں۔ (ii) نظری تعدد معلوم کریں۔ (iii) اس کا اوسط اور معیاری انحراف معلوم کریں۔',
    'فرض کړئ اووه سکې اچول کېږي او د سرونو شمېر لیکل کېږي. دا تجربه 128 ځله تکرارېږي (i) د دې فرضیې لاندې چې سکې بې‌پلوه دي، بینومیل وېش برابر کړئ. (ii) نظري فریکونسۍ محاسبه کړئ. (iii) منځنی او معیاري انحراف یې پیدا کړئ.')
c.h(*SOL)
c.p('(i) We have the following information', '(i) ہمارے پاس درج ذیل معلومات ہیں', '(i) لاندې معلومات لرو')
c.p('$n=7$, $X=0,1,2,3,4,5,6,7$, $N=128$, $p=\\frac{1}{2}$ (coins are unbiased), $q=\\frac{1}{2}$, therefore, the fitted Binomial distribution is',
    '$n=7$، $X=0,1,2,3,4,5,6,7$، $N=128$، $p=\\frac{1}{2}$ (سکے غیر جانبدار ہیں)، $q=\\frac{1}{2}$، لہٰذا منطبق دو رقمی تقسیم یہ ہے',
    '$n=7$، $X=0,1,2,3,4,5,6,7$، $N=128$، $p=\\frac{1}{2}$ (سکې بې‌پلوه دي)، $q=\\frac{1}{2}$، نو برابره شوې بینومیل وېش دا دی')
ex19 = c.build('stat12-p052-example-3-19', 'Example 3.19 — seven coins tossed 128 times', 'مثال 3.19 — سات سکے 128 بار', 'بېلګه 3.19 — اووه سکې 128 ځله', 52, [96])

if __name__ == '__main__':
    save(52, [(3, ex18), (3, ex19)])
