"""PDF76 printed 143–144: Example 4.15 computations (x̄, S, factor 37.37); Unit 4 key points."""
from class12_statistics_common import Builder, save

b = Builder()
b.mlines([r'\text{Here}\quad n=\Sigma f=60', r'c=5', r'\overline{x}=\frac{\Sigma fx}{\Sigma f}=\frac{4250}{60}=70.833\text{ kg}',
          r'S=\sqrt{\frac{\Sigma fx^2}{\Sigma f}-\left(\frac{\Sigma fx}{\Sigma f}\right)^2}=\sqrt{\frac{304910}{60}-\left(\frac{4250}{60}\right)^2}=\sqrt{5081.83-5017.36}', r'=\sqrt{64.472}=8.029'])
b.p('As μ and σ are unknown, therefore, $Z=\\frac{x-\\overline{x}}{S}=\\frac{x-70.833}{8.029}$', 'چونکہ μ اور σ نامعلوم ہیں، لہٰذا $Z=\\frac{x-\\overline{x}}{S}=\\frac{x-70.833}{8.029}$', 'څرنګه چې μ او σ نامعلوم دي، نو $Z=\\frac{x-\\overline{x}}{S}=\\frac{x-70.833}{8.029}$')
b.p('Put values of x (mid-points) one by one to get z-values as shown above in the table. Ordinates f(z) is obtained from table 4.2. The factor $\\frac{nc}{s}=\\frac{60(5)}{8.029}=37.37$',
    'z کی قیمتیں حاصل کرنے کے لیے x (وسطی نقاط) کی قیمتیں ایک ایک کر کے رکھیں جیسا کہ اوپر جدول میں دکھایا گیا ہے۔ ordinates f(z) جدول 4.2 سے حاصل کیے جاتے ہیں۔ ضربی عامل $\\frac{nc}{s}=\\frac{60(5)}{8.029}=37.37$',
    'د z قیمتونو د ترلاسه کولو لپاره د x (منځنیو ټکو) قیمتونه یو په یو کېږدئ لکه څنګه چې پورته په جدول کې ښودل شوي. اورډیناټونه f(z) له 4.2 جدول څخه لاسته راځي. ضربي عامل $\\frac{nc}{s}=\\frac{60(5)}{8.029}=37.37$')
ex = b.build('stat12-p076-example-4-15-calc', 'Example 4.15 — mean, standard deviation and the factor nc/s', 'مثال 4.15 — اوسط، معیاری انحراف اور ضربی عامل nc/s', 'بېلګه 4.15 — منځنی، معیاري انحراف او ضربي عامل nc/s', 76, [143])

k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.group('list', [
    ('A density function defined as $f(x)=\\left\\{\\begin{matrix}\\frac{1}{b-a}, & a\\le x\\le b\\\\ 0, & \\textit{otherwise}\\end{matrix}\\right\\}$ is the pdf of continuous uniform probability distribution.', 'اس طرح متعین کثافتی تفاعل $f(x)=\\left\\{\\begin{matrix}\\frac{1}{b-a}, & a\\le x\\le b\\\\ 0, & \\textit{otherwise}\\end{matrix}\\right\\}$ مسلسل یکساں احتمالی تقسیم کا pdf ہے۔', 'هغه کثافت تابع چې داسې تعریف شوې $f(x)=\\left\\{\\begin{matrix}\\frac{1}{b-a}, & a\\le x\\le b\\\\ 0, & \\textit{otherwise}\\end{matrix}\\right\\}$ د متصل یونیفارم احتمالي وېش pdf ده.'),
    ('Uniform distribution has two parameters, a and b.', 'یکساں تقسیم کے دو پیرامیٹر a اور b ہیں۔', 'یونیفارم وېش دوه پارامټرونه a او b لري.'),
    ('The range of Normal distribution is from −∞ to +∞.', 'نارمل تقسیم کی حد −∞ سے +∞ تک ہے۔', 'د نورمال وېش حد له −∞ څخه تر +∞ پورې دی.'),
    ('For Normal distribution the total probability within its range is always equal to one.', 'نارمل تقسیم میں اس کی حد کے اندر کل احتمال ہمیشہ ایک کے برابر ہوتا ہے۔', 'د نورمال وېش لپاره د هغه په حد کې ټول احتمال تل له یو سره برابر دی.'),
    ('Normal distribution has two parameters, μ and σ.', 'نارمل تقسیم کے دو پیرامیٹر μ اور σ ہیں۔', 'نورمال وېش دوه پارامټرونه μ او σ لري.'),
    ('For Normal distribution Mean = Median = Mode.', 'نارمل تقسیم کے لیے اوسط = وسطانیہ = عادہ۔', 'د نورمال وېش لپاره منځنی = منځنۍ = مود.'),
    ('For Normal distribution $M.D=\\frac{4}{5}\\sigma$', 'نارمل تقسیم کے لیے $M.D=\\frac{4}{5}\\sigma$', 'د نورمال وېش لپاره $M.D=\\frac{4}{5}\\sigma$'),
    ('For Normal distribution out of the total observations 68.3 % lies within the limits $\\mu\\pm\\sigma$, 95.4 % lies within the limits $\\mu\\pm 2\\sigma$ and 99.7 % lies within the limits $\\mu\\pm 3\\sigma$.', 'نارمل تقسیم میں کل مشاہدات میں سے 68.3 % حدود $\\mu\\pm\\sigma$ کے اندر، 95.4 % حدود $\\mu\\pm 2\\sigma$ کے اندر اور 99.7 % حدود $\\mu\\pm 3\\sigma$ کے اندر ہوتے ہیں۔', 'د نورمال وېش لپاره له ټولو مشاهدو څخه 68.3 % د $\\mu\\pm\\sigma$ په حدونو کې، 95.4 % د $\\mu\\pm 2\\sigma$ په حدونو کې او 99.7 % د $\\mu\\pm 3\\sigma$ په حدونو کې پرتې دي.'),
    ('$Z=\\frac{X-\\mu}{\\sigma}$ (standard Z-score)', '$Z=\\frac{X-\\mu}{\\sigma}$ (معیاری Z اسکور)', '$Z=\\frac{X-\\mu}{\\sigma}$ (معیاري Z نمره)'),
    ('$P[0<Z<1.2]=P[-1.2<Z<0]$',) * 3,
    ('Ordinate mean (height) of the standard normal curve corresponding to a specified z-value. It is denoted by f(z)', 'Ordinate سے مراد کسی مخصوص z قیمت کے مطابق معیاری نارمل منحنی کی بلندی ہے۔ اسے f(z) سے ظاہر کرتے ہیں', 'اورډیناټ د یوه ټاکلي z قیمت سره سم د معیاري نورمال منحني لوړوالي ته وایي. په f(z) ښودل کېږي'),
    ('Point probability in continuous case is always equal to zero.', 'مسلسل صورت میں نقطے کا احتمال ہمیشہ صفر ہوتا ہے۔', 'په متصل حالت کې د ټکي احتمال تل صفر وي.'),
    ('Continuous probability distributions give interval probability.', 'مسلسل احتمالی تقسیمیں وقفے کا احتمال دیتی ہیں۔', 'متصل احتمالي وېشونه د واټن احتمال ورکوي.'),
    ('When Normal distribution is shown on a graph paper, it gives a bell-shaped curve called normal curve which is generally taken as a standard for comparison.', 'جب نارمل تقسیم کو گراف پیپر پر دکھایا جائے تو یہ گھنٹی نما منحنی دیتی ہے جسے نارمل منحنی کہتے ہیں اور عموماً موازنے کے معیار کے طور پر لیا جاتا ہے۔', 'کله چې نورمال وېش په ګراف کاغذ وښودل شي، د زنګ ډوله منحني ورکوي چې نورمال منحني بلل کېږي او عموماً د پرتلې د معیار په توګه نیول کېږي.'),
    ('For Normal distribution $\\beta_1=0$ and $\\beta_2=3$.', 'نارمل تقسیم کے لیے $\\beta_1=0$ اور $\\beta_2=3$۔', 'د نورمال وېش لپاره $\\beta_1=0$ او $\\beta_2=3$.'),
])
keys = k.build('stat12-u4-key-points', 'Unit 4 — Key points', 'یونٹ 4 — اہم نکات', 'واحد 4 — مهم ټکي', 76, [144])

if __name__ == '__main__':
    save(76, [(4, ex), (4, keys)])
