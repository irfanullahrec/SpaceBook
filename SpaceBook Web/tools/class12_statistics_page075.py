"""PDF75 printed 141–142: Example 4.14 (ordinates), 4.2.10 fitting a Normal distribution by the ordinate method, Example 4.15 table."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h('Example 4.14', 'مثال 4.14', 'بېلګه 4.14')
b.p('Find the ordinates of the standard normal curve at i) Z = 0.25 ii) Z = 3.18 iii) Z = −1.64', 'معیاری نارمل منحنی کے ordinates معلوم کریں i) Z = 0.25 ii) Z = 3.18 iii) Z = −1.64', 'د معیاري نورمال منحني اورډیناټونه پیدا کړئ i) Z = 0.25 ii) Z = 3.18 iii) Z = −1.64')
b.h(*SOL)
b.group('lines', [
    ('i) Look at table 4.1 and search 0.2 in the z-column, go in the body of the table across this value up to the column headed by 0.05. The desired ordinate is 0.3867.', 'i) جدول 4.1 دیکھیں اور z کالم میں 0.2 تلاش کریں، اس قیمت کے سامنے جدول کے متن میں 0.05 والے کالم تک جائیں۔ مطلوبہ ordinate 0.3867 ہے۔', 'i) 4.1 جدول ته وګورئ او په z ستون کې 0.2 ولټوئ، د دې قیمت په وړاندې د جدول په متن کې تر 0.05 سرلیک لرونکي ستون پورې لاړ شئ. اړین اورډیناټ 0.3867 دی.'),
    ('ii) Similarly ordinate at Z = 3.18 is equal to 0.0025', 'ii) اسی طرح Z = 3.18 پر ordinate 0.0025 کے برابر ہے', 'ii) همداراز په Z = 3.18 کې اورډیناټ له 0.0025 سره برابر دی'),
    ('iii) Ordinate at Z = −1.64 = ordinate at Z = 1.64 = 0.1040 (By symmetry property).', 'iii) Z = −1.64 پر ordinate = Z = 1.64 پر ordinate = 0.1040 (تشاکل کی خاصیت سے)۔', 'iii) په Z = −1.64 کې اورډیناټ = په Z = 1.64 کې اورډیناټ = 0.1040 (د تناظر د ځانګړنې له مخې).'),
])
b.h('4.2.10 Fitting of Normal distribution to observed frequency distribution', '4.2.10 مشاہداتی تعددی تقسیم پر نارمل تقسیم کا انطباق', '4.2.10 په لیدل شوي فریکونسي وېش د نورمال وېش برابرول')
b.p('The fitting of Normal distribution to observe data means to compute theoretical/expected frequencies corresponding to the observed frequencies. This can be done by three methods, the cumulative standard normal probabilities method, the area method and the ordinate method. Here we consider only the ordinate method because it is simple to understand and comparatively less laborious.',
    'مشاہداتی مواد پر نارمل تقسیم منطبق کرنے کا مطلب مشاہداتی تعدد کے مطابق نظری/متوقع تعدد معلوم کرنا ہے۔ یہ تین طریقوں سے کیا جا سکتا ہے: مجموعی معیاری نارمل احتمالات کا طریقہ، رقبے کا طریقہ اور ordinate کا طریقہ۔ یہاں ہم صرف ordinate کا طریقہ لیتے ہیں کیونکہ یہ سمجھنے میں آسان اور نسبتاً کم محنت طلب ہے۔',
    'په لیدل شویو معلوماتو د نورمال وېش برابرول د لیدل شویو فریکونسیو سره سمې نظري/تمه شوې فریکونسۍ محاسبه کول دي. دا په درېیو طریقو کېدای شي: د تجمعي معیاري نورمال احتمالونو طریقه، د مساحت طریقه او د اورډیناټ طریقه. دلته یوازې د اورډیناټ طریقه په پام کې نیسو ځکه چې پوهېدل یې اسانه او نسبتاً لږ زحمت غواړي.')
b.h('◆ Fitting of Normal distribution by ordinate method', '◆ ordinate کے طریقے سے نارمل تقسیم کا انطباق', '◆ د اورډیناټ په طریقه د نورمال وېش برابرول')
b.p('This method involves the following steps:', 'یہ طریقہ درج ذیل مراحل پر مشتمل ہے:', 'دا طریقه لاندې پړاوونه لري:')
b.group('lines', [
    ('(i) Compute $\\overline{x}$ and S from the observed frequency distribution to estimate the unknown parameters μ and σ.', '(i) نامعلوم پیرامیٹرز μ اور σ کا تخمین لگانے کے لیے مشاہداتی تعددی تقسیم سے $\\overline{x}$ اور S معلوم کریں۔', '(i) د نامعلومو پارامټرونو μ او σ د اټکل لپاره له لیدل شوي فریکونسي وېش څخه $\\overline{x}$ او S محاسبه کړئ.'),
    ('(ii) Calculate $Z=\\frac{x-\\overline{x}}{S}$ from the mid-points (x).', '(ii) وسطی نقاط (x) سے $Z=\\frac{x-\\overline{x}}{S}$ معلوم کریں۔', '(ii) له منځنیو ټکو (x) څخه $Z=\\frac{x-\\overline{x}}{S}$ محاسبه کړئ.'),
    ('(iii) Find ordinates corresponding to Z from ordinate table 4.2.', '(iii) ordinate جدول 4.2 سے Z کے مطابق ordinates معلوم کریں۔', '(iii) د اورډیناټ له 4.2 جدول څخه د Z سره سم اورډیناټونه پیدا کړئ.'),
    ('(iv) Multiply the ordinates by $\\left(\\frac{nc}{S}\\right)$, to get the expected frequencies, where n is total frequency and c is the size of class interval.', '(iv) متوقع تعدد حاصل کرنے کے لیے ordinates کو $\\left(\\frac{nc}{S}\\right)$ سے ضرب دیں، جہاں n کل تعدد اور c جماعتی وقفے کا سائز ہے۔', '(iv) د تمه شویو فریکونسیو د ترلاسه کولو لپاره اورډیناټونه په $\\left(\\frac{nc}{S}\\right)$ کې ضرب کړئ، چې n ټوله فریکونسي او c د ټولګي د واټن اندازه ده.'),
])
fit = b.build('stat12-p075-fitting-normal', 'Example 4.14 and 4.2.10 fitting a Normal distribution (ordinate method)', 'مثال 4.14 اور 4.2.10 نارمل تقسیم کا انطباق (ordinate طریقہ)', 'بېلګه 4.14 او 4.2.10 د نورمال وېش برابرول (د اورډیناټ طریقه)', 75, [141])

c = Builder()
c.h('Example 4.15', 'مثال 4.15', 'بېلګه 4.15')
c.p('Fit a Normal distribution to the following table which shows the weight measurements of 60 male workers of a factory.', 'درج ذیل جدول پر نارمل تقسیم منطبق کریں جو ایک کارخانے کے 60 مرد کارکنوں کے وزن کی پیمائشیں دکھاتا ہے۔', 'په لاندې جدول نورمال وېش برابر کړئ چې د یوې فابریکې د 60 نارینه کارګرانو د وزن اندازې ښيي.')
c.table('stat12-t-ex4-15', ['Weights (kg)', '50–54', '55–59', '60–64', '65–69', '70–74', '75–79', '80–84', '85–89'],
        [['Number of workers', '2', '4', '6', '12', '16', '12', '6', '2']],
        ['وزن (kg)', '50–54', '55–59', '60–64', '65–69', '70–74', '75–79', '80–84', '85–89'], ['وزن (kg)', '50–54', '55–59', '60–64', '65–69', '70–74', '75–79', '80–84', '85–89'],
        [['کارکنوں کی تعداد', '2', '4', '6', '12', '16', '12', '6', '2']], [['د کارګرانو شمېر', '2', '4', '6', '12', '16', '12', '6', '2']])
c.h(*SOL)
rows = [['50–54', '2', '52', '104', '5408', '−2.35', '0.0252', '37.37(0.0252) = 1'], ['55–59', '4', '57', '228', '12996', '−1.72', '0.0909', '3.4'],
        ['60–64', '6', '62', '372', '23064', '−1.10', '0.2179', '8.2'], ['65–69', '12', '67', '804', '53868', '−0.48', '0.3555', '13.3'],
        ['70–74', '16', '72', '1152', '82944', '0.15', '0.3945', '15'], ['75–79', '12', '77', '924', '71148', '0.77', '0.2966', '11.1'],
        ['80–84', '6', '82', '492', '40344', '1.39', '0.1518', '6'], ['85–89', '2', '87', '174', '15138', '2.01', '0.0529', '2'],
        ['Total', '60', '–', '4250', '304910', '–', '–', '60']]
head = ['Weights', '$f$', '$x$', '$fx$', '$fx^2$', '$z=\\frac{x-70.833}{8.029}$', '$f(z)$', '$e_f=\\frac{nc}{s}f(z)=37.37f(z)$']
c.table('stat12-t-ex4-15-fit', head, rows, ['وزن'] + head[1:], ['وزن'] + head[1:],
        [r if r[0] != 'Total' else ['کل'] + r[1:] for r in rows], [r if r[0] != 'Total' else ['ټول'] + r[1:] for r in rows])
ex = c.build('stat12-p075-example-4-15', 'Example 4.15 — fitting a Normal distribution to workers’ weights', 'مثال 4.15 — کارکنوں کے وزن پر نارمل تقسیم کا انطباق', 'بېلګه 4.15 — د کارګرانو په وزن نورمال وېش برابرول', 75, [142])
issues = [{'id': 'stat12-p141-ex414-i', 'unit': 4, 'printedPage': 141, 'description': 'Example 4.14(i) tells the reader to use table 4.1 (it should be the ordinates table 4.2); the quoted value 0.3867 is the 4.2 entry. Several fitted values (e.g. 0.0252 for z=−2.35 vs table 0.0252) are kept as printed.'}]

if __name__ == '__main__':
    save(75, [(4, fit), (4, ex)], issues=issues)
