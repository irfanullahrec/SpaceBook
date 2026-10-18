"""PDF127 printed 245–246: Example 7.6 steps ii–vi; 7.2.3 test for μ1−μ2 (σ known) with three critical-region figures; Example 7.7 data table."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

D = r'\overline{X}_1-\overline{X}_2'
b = Builder()
b.group('lines', [('ii. α = 0.05',) * 3, ('iii. Test statistic:', 'iii. جانچ کا شماریہ:', 'iii. د ازموینې احصاییه:')])
b.eq(r't=\frac{\overline{X}-\mu}{s/\sqrt{n}},\ \nu=n-1\ \text{d.f}')
b.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
b.eq(r't=\frac{34000-35000}{2000/\sqrt{16}}=\frac{-1000}{2000/4}=-2')
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.vpara('stat12-ex7-6-cr', tail_test('left', z=1.753, mid='', ticks=((-1.753, '−1.753'), (0, '0')), label='Left-tailed t critical region at −1.753'),
        'Reject $H_0$ if $t\\le -t_{\\alpha,(\\nu)}$ Whereas as from t-table $t_{\\alpha(\\nu)}=t_{0.05,(16-1)}=t_{0.05,(15)}=1.753$',
        '$H_0$ کو رد کریں اگر $t\\le -t_{\\alpha,(\\nu)}$، جبکہ t-جدول سے $t_{\\alpha(\\nu)}=t_{0.05,(16-1)}=t_{0.05,(15)}=1.753$',
        '$H_0$ رد کړئ که $t\\le -t_{\\alpha,(\\nu)}$، په داسې حال کې چې له t-جدول څخه $t_{\\alpha(\\nu)}=t_{0.05,(16-1)}=t_{0.05,(15)}=1.753$', ratio=.45)
b.p('vi. Conclusion', 'vi. نتیجہ', 'vi. پایله')
b.p('As t = − 2 lies in the rejection region, so we reject $H_0$', 'چونکہ t = − 2 رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں', 'څرنګه چې t = − 2 د ردولو په سیمه کې پروت دی، نو $H_0$ ردوو')
e76 = b.build('stat12-p127-example-7-6', 'Example 7.6 — left-tailed t test (tire life)', 'مثال 7.6 — بائیں طرفہ t جانچ (ٹائر کی عمر)', 'بېلګه 7.6 — کیڼ لوري t ازموینه (د ټایر عمر)', 127, [245])

c = Builder()
c.h('7.2.3 Procedure for testing hypothesis about difference between two populations means (μ₁ − μ₂) when σ₁² and σ₂² are known', '7.2.3 جب σ₁² اور σ₂² معلوم ہوں تو دو آبادیوں کے اوسطوں کے فرق (μ₁ − μ₂) کے بارے میں مفروضے کی جانچ کا طریقہ', '7.2.3 کله چې σ₁² او σ₂² معلوم وي د دوو نفوسونو د منځنیو د توپیر (μ₁ − μ₂) په اړه د فرضیې د ازموینې طریقه')
c.p('The samples are randomly and independently selected from the two normal populations. The formal testing procedure is explained below:', 'نمونے دو نارمل آبادیوں سے تصادفی اور آزادانہ طور پر منتخب کیے جاتے ہیں۔ جانچ کا باقاعدہ طریقہ نیچے بیان کیا گیا ہے:', 'نمونې له دوو نورمال نفوسونو څخه په تصادفي او خپلواکه توګه ټاکل کېږي. د ازموینې رسمي طریقه لاندې تشریح شوې:')
c.mlines([r'i.\ (a)\quad H_0:\mu_1=\mu_2\ \text{or}\ \mu_1-\mu_2=0', r'H_1:\mu_1\neq\mu_2\ \text{or}\ \mu_1-\mu_2\neq 0', r'(b)\quad H_0:\mu_1\le\mu_2\ \text{or}\ \mu_1-\mu_2\le 0', r'H_1:\mu_1>\mu_2\ \text{or}\ \mu_1-\mu_2>0',
          r'(c)\quad H_0:\mu_1\ge\mu_2\ \text{or}\ \mu_1-\mu_2\ge 0', r'H_1:\mu_1<\mu_2\ \text{or}\ \mu_1-\mu_2<0'])
c.p('ii. Level of significance is decided as 0.01 or 0.05', 'ii. معنویت کی سطح 0.01 یا 0.05 طے کی جاتی ہے', 'ii. د معنی‌داریت کچه 0.01 یا 0.05 ټاکل کېږي')
c.p('iii. Test statistic to be used in this case is', 'iii. اس صورت میں استعمال ہونے والا جانچ کا شماریہ یہ ہے', 'iii. په دې حالت کې کارېدونکې د ازموینې احصاییه دا ده')
c.eq(rf'Z=\frac{{({D})-(\mu_1-\mu_2)}}{{\sqrt{{\frac{{\sigma_1^2}}{{n_1}}+\frac{{\sigma_2^2}}{{n_2}}}}}}\sim N(0,1)\ \text{{under }}H_0.')
c.p('iv. Z-statistic is computed from the given data.', 'iv. Z-شماریہ دیے گئے مواد سے معلوم کیا جاتا ہے۔', 'iv. Z-احصاییه له ورکړل شویو معلوماتو محاسبه کېږي.')
c.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
c.vpara('stat12-diff-cr-a', tail_test('two', ticks=((-1.4, '−Zα/2'), (1.4, 'Zα/2')), label='Two-sided critical region'),
        'For case (a) in $H_1$ Reject $H_0$ if $Z\\le -Z_{\\alpha/2}$ or $Z\\ge Z_{\\alpha/2}$', '$H_1$ میں صورت (a) کے لیے $H_0$ کو رد کریں اگر $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$', 'په $H_1$ کې د (a) حالت لپاره $H_0$ رد کړئ که $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$', ratio=.45)
c.vpara('stat12-diff-cr-b', tail_test('right', ticks=((1.4, 'Zα'),), label='Right-sided critical region'),
        'For case (b) Reject $H_0$ if $Z\\ge Z_\\alpha$', 'صورت (b) کے لیے $H_0$ کو رد کریں اگر $Z\\ge Z_\\alpha$', 'د (b) حالت لپاره $H_0$ رد کړئ که $Z\\ge Z_\\alpha$', ratio=.45)
c.vpara('stat12-diff-cr-c', tail_test('left', ticks=((-1.4, '−Zα'),), label='Left-sided critical region'),
        'For case (c) Reject $H_0$ if $Z\\le -Z_\\alpha$', 'صورت (c) کے لیے $H_0$ کو رد کریں اگر $Z\\le -Z_\\alpha$', 'د (c) حالت لپاره $H_0$ رد کړئ که $Z\\le -Z_\\alpha$', ratio=.45)
c.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
c.p('$H_0$ is rejected when computed value of Z falls in the rejection region.', 'جب Z کی معلوم کی گئی قیمت رد کے علاقے میں آئے تو $H_0$ رد کر دیا جاتا ہے۔', 'کله چې د Z محاسبه شوی قیمت د ردولو په سیمه کې ولوېږي، $H_0$ ردېږي.')
c.h('Example 7.7', 'مثال 7.7', 'بېلګه 7.7')
c.p('To see the effects of a certain sleeping pills on male and female, two independent samples were taken and the following data were recorded.', 'مردوں اور عورتوں پر نیند کی ایک خاص گولی کے اثرات دیکھنے کے لیے دو آزاد نمونے لیے گئے اور درج ذیل مواد ریکارڈ کیا گیا۔', 'پر نارینه او ښځینه د خوب د یوې ټاکلې ګولۍ د اغېزو د لیدلو لپاره دوه خپلواکې نمونې واخیستل شوې او لاندې معلومات ثبت شول.')
c.table('stat12-t-ex7-7', ['', 'male', 'female'], [['sample size', '$n_1=36$', '$n_2=64$'], ['sample mean', '$\\overline{x}_1=8.75$', '$\\overline{x}_2=7.25$'], ['population variance', '$\\sigma_1^2=9$', '$\\sigma_2^2=4$']],
        ['', 'مرد', 'عورت'], ['', 'نارینه', 'ښځینه'],
        [['نمونے کا سائز', '$n_1=36$', '$n_2=64$'], ['نمونے کا اوسط', '$\\overline{x}_1=8.75$', '$\\overline{x}_2=7.25$'], ['آبادی کا تغیر', '$\\sigma_1^2=9$', '$\\sigma_2^2=4$']],
        [['د نمونې اندازه', '$n_1=36$', '$n_2=64$'], ['د نمونې منځنی', '$\\overline{x}_1=8.75$', '$\\overline{x}_2=7.25$'], ['د نفوس واریانس', '$\\sigma_1^2=9$', '$\\sigma_2^2=4$']])
dm = c.build('stat12-p127-diff-means-known', '7.2.3 Test for μ₁ − μ₂ (σ known) — Example 7.7 data', '7.2.3 μ₁ − μ₂ کی جانچ (σ معلوم) — مثال 7.7 کا مواد', '7.2.3 د μ₁ − μ₂ ازموینه (σ معلوم) — د بېلګې 7.7 معلومات', 127, [245, 246])

if __name__ == '__main__':
    save(127, [(7, e76), (7, dm)])
