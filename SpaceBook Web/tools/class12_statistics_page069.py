"""PDF69 printed 129–130: Examples 4.4–4.6 (inverse use), 4.2.8 application to any Normal distribution, Example 4.7 start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import normal_shaded

SOL = ('Solution:', 'حل:', 'حل:')
K = dict(w=300, h=120, zlabel='Z')


def tail(z, inner, outer, label):
    return normal_shaded(z, None, labels=((0, '0'), (z, 'z')), marks=(0, z), notes=((z / 2 + .1, .3, inner), (z + .75, .3, outer)), label=label, **K)


b = Builder()
b.h('Example 4.4', 'مثال 4.4', 'بېلګه 4.4')
b.p('If $P[Z\\ge z]=0.025$, find the value of z.', 'اگر $P[Z\\ge z]=0.025$ ہو تو z کی قیمت معلوم کریں۔', 'که $P[Z\\ge z]=0.025$ وي، د z قیمت پیدا کړئ.')
b.h(*SOL)
b.vpara('stat12-ex4-4-curve', tail(1.96, '0.4750', '0.025', 'Upper tail area 0.025 beyond z'),
        'i) Sketch the given statement graphically as', 'i) دیے گئے بیان کا ترسیمی خاکہ یوں بنائیں', 'i) ورکړل شوی بیان په ګرافیکي ډول داسې رسم کړئ')
b.group('lines', [
    ('ii) From the figure we see that the unknown value z is a positive value because it lies to the right of 0 (the mean) and probability above it is equal to 0.025.', 'ii) شکل سے ہم دیکھتے ہیں کہ نامعلوم قیمت z مثبت ہے کیونکہ یہ 0 (اوسط) کے دائیں جانب ہے اور اس سے اوپر احتمال 0.025 کے برابر ہے۔', 'ii) له شکل څخه وینو چې نامعلوم قیمت z مثبت دی ځکه چې د 0 (منځني) ښي خوا ته پروت دی او له هغه پورته احتمال له 0.025 سره برابر دی.'),
    ('iii) As we know that probability from 0 to ∞ is equal to 0.5, so the probability for 0 to z will definitely be equal to 0.5 − 0.025 = 0.4750, i.e. $P[0\\le Z\\le z]=0.4750$', 'iii) جیسا کہ ہم جانتے ہیں کہ 0 سے ∞ تک احتمال 0.5 ہے، لہٰذا 0 سے z تک احتمال یقیناً 0.5 − 0.025 = 0.4750 ہوگا، یعنی $P[0\\le Z\\le z]=0.4750$', 'iii) لکه څنګه چې پوهېږو له 0 څخه تر ∞ پورې احتمال 0.5 دی، نو له 0 څخه تر z پورې احتمال به یقیناً 0.5 − 0.025 = 0.4750 وي، یعنې $P[0\\le Z\\le z]=0.4750$'),
    ('iv) Now search the figure 0.4750 in the body of the area table to determine the corresponding value of Z. From table 4.1, we observe that the figure 0.4750 corresponds to 1.96. Hence z = 1.96 and the area above this value is equal to 0.025.', 'iv) اب Z کی متعلقہ قیمت معلوم کرنے کے لیے رقبے کے جدول کے متن میں عدد 0.4750 تلاش کریں۔ جدول 4.1 سے ہم دیکھتے ہیں کہ عدد 0.4750، 1.96 کے مطابق ہے۔ لہٰذا z = 1.96 اور اس قیمت سے اوپر رقبہ 0.025 ہے۔', 'iv) اوس د Z د اړوند قیمت د ټاکلو لپاره د مساحت د جدول په متن کې 0.4750 عدد ولټوئ. له 4.1 جدول څخه وینو چې 0.4750 عدد له 1.96 سره سمون لري. نو z = 1.96 او له دې قیمت پورته مساحت 0.025 دی.'),
])
b.p('• Note that if the value we are searching for is not available in the table, then we may pick the nearest value to find Z-values.', '• نوٹ کریں کہ اگر جس قیمت کی ہم تلاش میں ہیں وہ جدول میں دستیاب نہ ہو تو Z کی قیمتیں معلوم کرنے کے لیے قریب ترین قیمت چن سکتے ہیں۔', '• پام وکړئ چې که هغه قیمت چې موږ یې لټوو په جدول کې نه وي، نو د Z قیمتونو د موندلو لپاره تر ټولو نږدې قیمت غوره کولای شو.')
b.h('Example 4.5', 'مثال 4.5', 'بېلګه 4.5')
b.p('Determine z when $P[Z\\ge z]=0.10$', 'z معلوم کریں جب $P[Z\\ge z]=0.10$', 'z وټاکئ کله چې $P[Z\\ge z]=0.10$')
b.h(*SOL)
b.p('The probability $P[Z\\ge z]=0.10$ is graphically shown as:', 'احتمال $P[Z\\ge z]=0.10$ ترسیمی طور پر یوں دکھایا گیا ہے:', 'احتمال $P[Z\\ge z]=0.10$ په ګرافیکي ډول داسې ښودل کېږي:')
b.vpara('stat12-ex4-5-curve', tail(1.28, '0.40', '0.10', 'Upper tail area 0.10 beyond z'),
        'As $P[Z\\ge z]=0.10\\Rightarrow P[0<Z<z]=0.5-0.10=0.40$. In the area table 4.1 we observe that exactly 0.40 is not available we consider the closest area 0.3997, which corresponds to a Z-value 1.28. Hence z = 1.28 and area above it is equal to 0.10 or 10%.',
        'چونکہ $P[Z\\ge z]=0.10\\Rightarrow P[0<Z<z]=0.5-0.10=0.40$۔ رقبے کے جدول 4.1 میں ہم دیکھتے ہیں کہ ٹھیک 0.40 دستیاب نہیں، لہٰذا ہم قریب ترین رقبہ 0.3997 لیتے ہیں جو Z کی قیمت 1.28 کے مطابق ہے۔ لہٰذا z = 1.28 اور اس سے اوپر رقبہ 0.10 یعنی 10% ہے۔',
        'څرنګه چې $P[Z\\ge z]=0.10\\Rightarrow P[0<Z<z]=0.5-0.10=0.40$. د مساحت په 4.1 جدول کې وینو چې دقیقاً 0.40 نشته، نو تر ټولو نږدې مساحت 0.3997 نیسو چې د Z له 1.28 قیمت سره سمون لري. نو z = 1.28 او له هغه پورته مساحت 0.10 یا 10% دی.')
ex = b.build('stat12-p069-inverse-examples', 'Examples 4.4–4.5 — inverse use of the area table', 'مثالیں 4.4–4.5 — رقبے کے جدول کا الٹا استعمال', 'بېلګې 4.4–4.5 — د مساحت د جدول معکوس کارول', 69, [129])

c = Builder()
c.h('Example 4.6', 'مثال 4.6', 'بېلګه 4.6')
c.p('Let $Z\\sim N(0,1)$. If $P[Z\\ge z]=0.5$, what will be the value of z?', 'فرض کریں $Z\\sim N(0,1)$۔ اگر $P[Z\\ge z]=0.5$ ہو تو z کی قیمت کیا ہوگی؟', 'فرض کړئ $Z\\sim N(0,1)$. که $P[Z\\ge z]=0.5$ وي، د z قیمت به څه وي؟')
c.h(*SOL)
c.vpara('stat12-ex4-6-curve', tail(1.645, '0.45', '0.05', 'Upper tail area 0.05 beyond z'), 'Draw the sketch:', 'خاکہ بنائیں:', 'خاکه رسم کړئ:')
c.p('Since $P[Z\\ge z]=0.05$, therefore, $P[0<Z<z]=0.5\\ \\ 0.05\\ \\ 0.45$. In the area table we can see that 0.45 is lying between 0.4495 and 0.4505 whose corresponding Z-values are 1.64 and 1.65 respectively. The Z-value in this case is given as $z=\\frac{1.64+1.65}{2}=1.645$.',
    'چونکہ $P[Z\\ge z]=0.05$، لہٰذا $P[0<Z<z]=0.5\\ \\ 0.05\\ \\ 0.45$۔ رقبے کے جدول میں ہم دیکھ سکتے ہیں کہ 0.45، 0.4495 اور 0.4505 کے درمیان ہے جن کی متعلقہ Z قیمتیں بالترتیب 1.64 اور 1.65 ہیں۔ اس صورت میں Z کی قیمت $z=\\frac{1.64+1.65}{2}=1.645$ ہے۔',
    'څرنګه چې $P[Z\\ge z]=0.05$، نو $P[0<Z<z]=0.5\\ \\ 0.05\\ \\ 0.45$. د مساحت په جدول کې لیدلای شو چې 0.45 د 0.4495 او 0.4505 ترمنځ دی چې اړوند Z قیمتونه یې په ترتیب سره 1.64 او 1.65 دي. په دې حالت کې د Z قیمت $z=\\frac{1.64+1.65}{2}=1.645$ دی.')
c.p('Hence $P[Z\\ge 1.645]=0.05$', 'لہٰذا $P[Z\\ge 1.645]=0.05$', 'نو $P[Z\\ge 1.645]=0.05$')
c.h('4.2.8 Application of area table to any Normal distribution', '4.2.8 کسی بھی نارمل تقسیم پر رقبے کے جدول کا اطلاق', '4.2.8 په هر نورمال وېش د مساحت د جدول کارول')
c.p('After learning the use of areas table and its inverse use, now you would be able to compute probabilities for any Normal random variable X by first converting X to Z by the formula $Z=\\frac{X-\\mu}{\\sigma}$ and then use the table of areas for the standard Normal distribution to obtain the desired probabilities.',
    'رقبوں کے جدول اور اس کے الٹے استعمال کو سیکھنے کے بعد اب آپ کسی بھی نارمل تصادفی متغیر X کے احتمالات معلوم کر سکیں گے، پہلے فارمولا $Z=\\frac{X-\\mu}{\\sigma}$ سے X کو Z میں تبدیل کر کے اور پھر مطلوبہ احتمالات حاصل کرنے کے لیے معیاری نارمل تقسیم کے رقبوں کا جدول استعمال کر کے۔',
    'د مساحتونو د جدول او د هغه د معکوس کارولو له زده کړې وروسته، اوس به تاسو وکولای شئ د هر نورمال تصادفي متغیر X احتمالونه محاسبه کړئ، لومړی د $Z=\\frac{X-\\mu}{\\sigma}$ فورمول په واسطه X په Z بدلول او بیا د اړینو احتمالونو د ترلاسه کولو لپاره د معیاري نورمال وېش د مساحتونو جدول کارول.')
c.h('Example 4.7', 'مثال 4.7', 'بېلګه 4.7')
c.p('If a Normal distribution has mean 40 and standard deviation 5, find the probabilities for the values of X specified as i) $P(X\\ge 44)$, ii) $P(X\\le 25)$, iii) $P(32<X<50)$.', 'اگر کسی نارمل تقسیم کا اوسط 40 اور معیاری انحراف 5 ہو تو X کی ان قیمتوں کے احتمالات معلوم کریں i) $P(X\\ge 44)$، ii) $P(X\\le 25)$، iii) $P(32<X<50)$۔', 'که یو نورمال وېش منځنی 40 او معیاري انحراف 5 ولري، د X د دې قیمتونو احتمالونه پیدا کړئ i) $P(X\\ge 44)$، ii) $P(X\\le 25)$، iii) $P(32<X<50)$.')
c.h(*SOL)
c.p('In order to find the probabilities, we first standardize X by subtracting its mean 40 and dividing the difference by standard deviation 5 to get Z and then find probabilities through area table as follow:', 'احتمالات معلوم کرنے کے لیے پہلے ہم X کو معیاری بناتے ہیں، اس کا اوسط 40 تفریق کر کے اور فرق کو معیاری انحراف 5 پر تقسیم کر کے Z حاصل کرتے ہیں، اور پھر رقبے کے جدول سے احتمالات یوں معلوم کرتے ہیں:', 'د احتمالونو د موندلو لپاره لومړی X معیاري کوو، منځنی یې 40 ترې تفریق او توپیر پر معیاري انحراف 5 وېشو ترڅو Z ترلاسه کړو، او بیا د مساحت له جدول څخه احتمالونه داسې پیدا کوو:')
ex2 = c.build('stat12-p069-example-4-6-4-7', 'Example 4.6, 4.2.8 application to any Normal distribution, Example 4.7', 'مثال 4.6، 4.2.8 کسی بھی نارمل تقسیم پر اطلاق، مثال 4.7', 'بېلګه 4.6، 4.2.8 په هر نورمال وېش کارول، بېلګه 4.7', 69, [130])
issues = [{'id': 'stat12-p130-ex46-0-5', 'unit': 4, 'printedPage': 130, 'description': 'Example 4.6 asks for P[Z ≥ z] = 0.5 but the sketch and solution use 0.05; the solution line also prints “0.5 0.05 0.45” without the minus and equals signs. Printed text retained.'}]

if __name__ == '__main__':
    save(69, [(4, ex), (4, ex2)], issues=issues)
