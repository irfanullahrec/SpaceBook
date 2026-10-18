"""PDF53 printed 97–98: Example 3.19 table and results; 3.4 hypergeometric experiment; 3.4.1 hypergeometric distribution table."""
from class12_statistics_common import Builder, save

h = r'\left(\frac{1}{2}\right)'
b = Builder()
b.eq(r'p(x)=\left\{\begin{matrix}{}^{7}_{x}C(1/2)^x(1/2)^{7-x}, & x=0,1,\ldots,7\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('(ii)', '(ii)', '(ii)')
rows = []
for k, c in zip(range(8), (1, 7, 21, 35, 35, 21, 7, 1)):
    ef = f'$128\\times\\frac{{{c}}}{{128}}={c:02d}$' if k < 2 else f'$={c:02d}$'
    rows.append([str(k), f'${{}}^{{7}}_{{{k}}}C{h}^{{{k}}}{h}^{{7-{k}}}=\\frac{{{c}}}{{128}}$', ef])
rows.append(['Total', '1', '128'])
b.grid('stat12-t-ex3-19', ['$X$', '$p(x)={}^{7}_{x}C' + h + '^x' + h + '^{7-x}$', '$E_f=N\\,p(x)$'], rows)
b.p('(iii) Mean of Binomial distribution $=E(X)=np=7\\left(\\frac{1}{2}\\right)=3.5$', '(iii) دو رقمی تقسیم کا اوسط $=E(X)=np=7\\left(\\frac{1}{2}\\right)=3.5$', '(iii) د بینومیل وېش منځنی $=E(X)=np=7\\left(\\frac{1}{2}\\right)=3.5$')
b.p('Standard deviation of Binomial distribution $=\\sigma_x=\\sqrt{npq}=\\sqrt{7\\times\\frac{1}{2}\\times\\frac{1}{2}}=\\sqrt{\\frac{7}{4}}=1.32$',
    'دو رقمی تقسیم کا معیاری انحراف $=\\sigma_x=\\sqrt{npq}=\\sqrt{7\\times\\frac{1}{2}\\times\\frac{1}{2}}=\\sqrt{\\frac{7}{4}}=1.32$',
    'د بینومیل وېش معیاري انحراف $=\\sigma_x=\\sqrt{npq}=\\sqrt{7\\times\\frac{1}{2}\\times\\frac{1}{2}}=\\sqrt{\\frac{7}{4}}=1.32$')
ex = b.build('stat12-p053-example-3-19', 'Example 3.19 — fitted distribution, frequencies, mean and S.D', 'مثال 3.19 — منطبق تقسیم، تعدد، اوسط اور معیاری انحراف', 'بېلګه 3.19 — برابر وېش، فریکونسۍ، منځنی او معیاري انحراف', 53, [97])

c = Builder()
c.h('3.4 Hypergeometric experiment', '3.4 ہائپر جیومیٹرک تجربہ', '3.4 هایپرجیومټریک تجربه')
c.p('The Binomial distribution is based on the assumption that the successive trials are independent and the probability of success remains unchanged from trial to trial. These assumptions hold only for sampling with replacement from an infinite population but there are experiments in which the conditions of independence is violated and the probability of success does not remain the same/constant for all trails e.g. if sampling is without replacement from a finite population, the probability will change from trail to trail and the successive trails will be dependent. Such experiments are called hypergeometric experiments having the following four properties:',
    'دو رقمی تقسیم اس مفروضے پر مبنی ہے کہ یکے بعد دیگرے آزمائشیں آزاد ہوتی ہیں اور کامیابی کا احتمال ایک آزمائش سے دوسری تک تبدیل نہیں ہوتا۔ یہ مفروضے صرف لامحدود آبادی سے واپسی کے ساتھ نمونہ گیری پر پورے اترتے ہیں، لیکن ایسے تجربات بھی ہیں جن میں آزادی کی شرط ٹوٹ جاتی ہے اور کامیابی کا احتمال تمام آزمائشوں کے لیے یکساں/مستقل نہیں رہتا، مثلاً اگر محدود آبادی سے بغیر واپسی کے نمونہ لیا جائے تو احتمال ایک آزمائش سے دوسری تک بدل جائے گا اور یکے بعد دیگرے آزمائشیں تابع ہوں گی۔ ایسے تجربات ہائپر جیومیٹرک تجربات کہلاتے ہیں جن کی درج ذیل چار خصوصیات ہیں:',
    'بینومیل وېش په دې فرضیه ولاړ دی چې پرله پسې ازمېښتونه خپلواک دي او د بریا احتمال له یوه ازمېښت څخه تر بل پورې نه بدلېږي. دا فرضیې یوازې له بې‌پایه نفوس څخه له بېرته اچولو سره نمونه اخیستنې ته سمې دي، خو داسې تجربې هم شته چې پکې د خپلواکۍ شرط ماتېږي او د بریا احتمال د ټولو ازمېښتونو لپاره یو شان/ثابت نه پاتې کېږي، لکه که له محدود نفوس څخه بې له بېرته اچولو نمونه واخیستل شي، احتمال به له یوه ازمېښت څخه تر بل بدلېږي او پرله پسې ازمېښتونه به تړلي وي. داسې تجربې هایپرجیومټریک تجربې بلل کېږي چې لاندې څلور ځانګړنې لري:')
c.group('lines', [
    ('i. Each trail may have two possible results, success and failure.', 'i. ہر آزمائش کے دو ممکنہ نتائج ہو سکتے ہیں، کامیابی اور ناکامی۔', 'i. هر ازمېښت کېدای شي دوه شونې پایلې ولري، بریا او ناکامي.'),
    ('ii. The probability of success changes on each trail.', 'ii. ہر آزمائش پر کامیابی کا احتمال بدل جاتا ہے۔', 'ii. په هر ازمېښت کې د بریا احتمال بدلېږي.'),
    ('iii. The successive trails are dependent.', 'iii. یکے بعد دیگرے آزمائشیں تابع ہوتی ہیں۔', 'iii. پرله پسې ازمېښتونه تړلي دي.'),
    ('iv. The experiment is repeated a fixed number of time, say n.', 'iv. تجربہ ایک مقررہ تعداد، مثلاً n، بار دہرایا جاتا ہے۔', 'iv. تجربه یو ټاکلی شمېر ځله، لکه n، تکرارېږي.'),
])
c.p('The random variable X denoting the number of successes in a hypergeometric experiment is called hypergeometric random variable and its probability distribution is called hypergeometric probability distribution.',
    'ہائپر جیومیٹرک تجربے میں کامیابیوں کی تعداد ظاہر کرنے والا تصادفی متغیر X ہائپر جیومیٹرک تصادفی متغیر اور اس کی احتمالی تقسیم ہائپر جیومیٹرک احتمالی تقسیم کہلاتی ہے۔',
    'هغه تصادفي متغیر X چې په هایپرجیومټریک تجربه کې د بریاوو شمېر ښيي، هایپرجیومټریک تصادفي متغیر او احتمالي وېش یې هایپرجیومټریک احتمالي وېش بلل کېږي.')
c.h('3.4.1 Hypergeometric probability distribution', '3.4.1 ہائپر جیومیٹرک احتمالی تقسیم', '3.4.1 هایپرجیومټریک احتمالي وېش')
c.p('If values of a hypergeometric random variable along with their associated probabilities are shown in tabular form, then it is called hypergeometric probability distribution i.e.', 'اگر ہائپر جیومیٹرک تصادفی متغیر کی قیمتیں ان کے متعلقہ احتمالات کے ساتھ جدولی شکل میں دکھائی جائیں تو اسے ہائپر جیومیٹرک احتمالی تقسیم کہتے ہیں یعنی', 'که د هایپرجیومټریک تصادفي متغیر قیمتونه له اړوندو احتمالونو سره په جدولي بڼه وښودل شي، هایپرجیومټریک احتمالي وېش بلل کېږي یعنې')
H = lambda x, nx: f'$\\dfrac{{\\binom{{K}}{{{x}}}\\binom{{N-K}}{{{nx}}}}}{{\\binom{{N}}{{n}}}}$'
c.dist('stat12-t-hypergeometric-general', ['0', '1', '2', '$\\cdots$', '$n$'], [H('0', 'n-0'), H('1', 'n-1'), H('2', 'n-2'), '$\\cdots$', H('n', 'n-n')])
hg = c.build('stat12-p053-hypergeometric', '3.4 Hypergeometric experiment and distribution', '3.4 ہائپر جیومیٹرک تجربہ اور تقسیم', '3.4 هایپرجیومټریک تجربه او وېش', 53, [98])

if __name__ == '__main__':
    save(53, [(3, ex), (3, hg)])
