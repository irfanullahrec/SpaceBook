"""PDF72 printed 135–136: Example 4.9 (iii); Example 4.10 (trout) (a)–(b); Example 4.11 (lamps) start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import paired_curves, normal_shaded

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.vpara('stat12-ex4-9-iii', paired_curves(-0.8, 0.8, ((-0.8, '45'), (0, '65'), (0.8, '85')), ((-0.8, '−0.8'), (0, '0'), (0.8, '0.8'))), *(r'iii) $P[45<X<85]$',) * 3)
b.mlines([r'=P\left[\frac{45-\mu}{\sigma}<\frac{X-\mu}{\sigma}<\frac{85-\mu}{\sigma}\right]', r'=P\left[\frac{45-65}{25}<Z<\frac{85-65}{25}\right]', r'=P[-0.80<Z<0.80]', r'=2P[0<Z<0.80]', r'=2(0.2881)=0.5762=57.62\%'])
ex9 = b.build('stat12-p072-example-4-9-iii', 'Example 4.9 — part (iii)', 'مثال 4.9 — حصہ (iii)', 'بېلګه 4.9 — برخه (iii)', 72, [135])

c = Builder()
c.h('Example 4.10', 'مثال 4.10', 'بېلګه 4.10')
c.p('Suppose the yearling trout in a lake have lengths that are approximately normally distributed, about a mean μ = 9.5″ with a standard deviation σ = 1.4″. (a) What percent of the trout caught have length over 12″? (b) If 80 percent of the trout caught have length greater than x, find x.',
    'فرض کریں ایک جھیل میں ایک سالہ ٹراؤٹ مچھلیوں کی لمبائیاں تقریباً نارمل تقسیم شدہ ہیں جن کا اوسط μ = 9.5″ اور معیاری انحراف σ = 1.4″ ہے۔ (a) پکڑی گئی ٹراؤٹ مچھلیوں میں سے کتنے فیصد کی لمبائی 12″ سے زیادہ ہے؟ (b) اگر پکڑی گئی 80 فیصد ٹراؤٹ مچھلیوں کی لمبائی x سے زیادہ ہو تو x معلوم کریں۔',
    'فرض کړئ په یوه جهیل کې د یو کلنو ټراوټ کبانو اوږدوالی نږدې نورمال وېش لري چې منځنی یې μ = 9.5″ او معیاري انحراف یې σ = 1.4″ دی. (a) د نیول شویو ټراوټونو څو سلنه یې له 12″ څخه زیات اوږدوالی لري؟ (b) که د نیول شویو ټراوټونو 80 سلنه له x څخه زیات اوږدوالی ولري، x پیدا کړئ.')
c.h(*SOL)
c.vpara('stat12-ex4-10-a', paired_curves(1.79, None, ((0, '9.5'), (1.79, '12')), ((0, '0'), (1.79, '1.79'))), '(a) We need to find $P[X>12]$', '(a) ہمیں $P[X>12]$ معلوم کرنا ہے', '(a) موږ باید $P[X>12]$ پیدا کړو')
c.mlines([r'=P\left[\frac{X-\mu}{\sigma}>\frac{12-9.5}{1.4}\right]', r'=P\left[Z>\frac{2.5}{1.4}\right]=P[Z>1.79]', r'=P[0<Z<\infty]-P[0<Z<1.79]', r'=0.5-0.4633=0.0367=3.67\%\quad 4\%'])
c.p('(b) We need X-value above which 80% observation will lie. Mathematically this statement can be written as $P[X>x]=0.80$ which in standard units is equal to $P[Z>z]=0.80$, shown in the following figure.',
    '(b) ہمیں X کی وہ قیمت درکار ہے جس سے اوپر 80% مشاہدات ہوں۔ ریاضیاتی طور پر یہ بیان $P[X>x]=0.80$ لکھا جا سکتا ہے جو معیاری اکائیوں میں $P[Z>z]=0.80$ کے برابر ہے، جیسا کہ درج ذیل شکل میں دکھایا گیا ہے۔',
    '(b) موږ د X هغه قیمت ته اړتیا لرو چې له هغه پورته 80% مشاهدې پرتې وي. په ریاضي ډول دا بیان داسې لیکل کېدای شي $P[X>x]=0.80$ چې په معیاري واحدونو کې له $P[Z>z]=0.80$ سره برابر دی، لکه څنګه چې په لاندې شکل کې ښودل شوی.')
c.visual('stat12-ex4-10-b', normal_shaded(-0.52, None, labels=((-0.52, 'z'), (0, '0')), marks=(-0.52, 0), notes=((-1.4, .18, '0.20'), (-0.26, .7, '0.30'), (0.55, .7, '0.50')), zlabel='Z', label='Area 0.80 to the right of z = −0.52'), ratio=.55)
c.p('We see that area below z is equal to 0.20. Search this value 0.20 in the area table 4.1, it corresponds Z = − 0.52 (minus sign is used because Z value lies to the left of 0).',
    'ہم دیکھتے ہیں کہ z سے نیچے رقبہ 0.20 کے برابر ہے۔ یہ قیمت 0.20 رقبے کے جدول 4.1 میں تلاش کریں، یہ Z = − 0.52 کے مطابق ہے (منفی علامت اس لیے استعمال ہوئی کہ Z کی قیمت 0 کے بائیں جانب ہے)۔',
    'وینو چې له z لاندې مساحت له 0.20 سره برابر دی. دا قیمت 0.20 د مساحت په 4.1 جدول کې ولټوئ، له Z = − 0.52 سره سمون لري (منفي نښه ځکه کارول شوې چې د Z قیمت د 0 کیڼ اړخ ته پروت دی).')
c.mlines([r'\text{As } Z=\frac{X-\mu}{\sigma}\quad\Rightarrow X=\mu+Z\sigma=9.5+(-0.52)\,1.4=9.5-0.728=8.8', r'X=8.8'])
c.p('Hence $P[X>8.8'']=0.80=80\\%$. It means that 80 percent of the trout caught from the lake have length greater than $x=8.8''$.', 'لہٰذا $P[X>8.8'']=0.80=80\\%$۔ اس کا مطلب ہے کہ جھیل سے پکڑی گئی 80 فیصد ٹراؤٹ مچھلیوں کی لمبائی $x=8.8''$ سے زیادہ ہے۔', 'نو $P[X>8.8'']=0.80=80\\%$. مانا یې دا ده چې له جهیل څخه د نیول شویو ټراوټونو 80 سلنه له $x=8.8''$ څخه زیات اوږدوالی لري.')
ex10 = c.build('stat12-p072-example-4-10', 'Example 4.10 — trout lengths', 'مثال 4.10 — ٹراؤٹ کی لمبائیاں', 'بېلګه 4.10 — د ټراوټ اوږدوالی', 72, [135, 136])

d = Builder()
d.h('Example 4.11', 'مثال 4.11', 'بېلګه 4.11')
d.p('The Peshawar Municipal Corporation installs 10,000 electric lamps in the streets of Peshawar. Average life of these lamps is 1850 hours with a standard deviation of 200 hours. How many lamps may be expected to burn for more than 2000 hours?',
    'پشاور میونسپل کارپوریشن پشاور کی گلیوں میں 10,000 بجلی کے بلب لگاتی ہے۔ ان بلبوں کی اوسط عمر 1850 گھنٹے اور معیاری انحراف 200 گھنٹے ہے۔ کتنے بلبوں کے 2000 گھنٹے سے زیادہ جلنے کی توقع کی جا سکتی ہے؟',
    'د پېښور ښاروالۍ د پېښور په کوڅو کې 10,000 برېښنايي ګروپونه لګوي. د دې ګروپونو منځنی عمر 1850 ساعته او معیاري انحراف یې 200 ساعته دی. د څو ګروپونو تمه کېدای شي چې له 2000 ساعتونو زیات وسوځي؟')
d.h(*SOL)
d.p('We first find probability and then multiply by the total number of lamps to compute the required expected frequency as', 'ہم پہلے احتمال معلوم کرتے ہیں اور پھر مطلوبہ متوقع تعدد معلوم کرنے کے لیے اسے بلبوں کی کل تعداد سے ضرب دیتے ہیں', 'لومړی احتمال پیدا کوو او بیا د اړینې تمه شوې فریکونسۍ د محاسبې لپاره یې د ګروپونو په ټول شمېر کې ضربوو')
d.vpara('stat12-ex4-11', paired_curves(0.75, None, ((0, '1850'), (0.75, '2000')), ((0, '0'), (0.75, '0.75')), xaxis='x'), *(r'$P[X>2000]$',) * 3)
d.mlines([r'=P\left[\frac{X-\mu}{\sigma}>\frac{2000-\mu}{\sigma}\right]', r'=P\left[Z>\frac{2000-1850}{200}\right]', r'=P\left[Z>\frac{150}{200}\right]', r'=P[Z>0.75]'])
ex11 = d.build('stat12-p072-example-4-11', 'Example 4.11 — street lamps (start)', 'مثال 4.11 — گلیوں کے بلب (آغاز)', 'بېلګه 4.11 — د کوڅو ګروپونه (پیل)', 72, [136])

if __name__ == '__main__':
    save(72, [(4, ex9), (4, ex10), (4, ex11)])
