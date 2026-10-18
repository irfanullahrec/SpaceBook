"""PDF128 printed 247–248: Example 7.7 solution (sleeping pills); 7.2.4 test for μ1−μ2 (σ unknown, large samples); Example 7.8 steps i–iv."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
D = r'\overline{X}_1-\overline{X}_2'
b = Builder()
b.p('Test $H_0:\\mu_1=\\mu_2$ against $H_1:\\mu_1\\neq\\mu_2$ at 5% significance level.', '5% معنویت کی سطح پر $H_1:\\mu_1\\neq\\mu_2$ کے مقابلے میں $H_0:\\mu_1=\\mu_2$ کی جانچ کریں۔', 'د 5% د معنی‌داریت په کچه د $H_1:\\mu_1\\neq\\mu_2$ پر وړاندې $H_0:\\mu_1=\\mu_2$ وازموئ.')
b.h(*SOL)
b.group('lines', [
    ('(i) $H_0:\\mu_1=\\mu_2$ means that $\\mu_1-\\mu_2=0$', '(i) $H_0:\\mu_1=\\mu_2$ کا مطلب ہے کہ $\\mu_1-\\mu_2=0$', '(i) $H_0:\\mu_1=\\mu_2$ مانا دا ده چې $\\mu_1-\\mu_2=0$'),
    ('$H_1:\\mu_1\\neq\\mu_2$',) * 3, ('(ii) α = 0.05',) * 3,
    ('(iii) Test statistic that summarizes the sample information in this case is', '(iii) اس صورت میں نمونے کی معلومات کا خلاصہ کرنے والا جانچ کا شماریہ یہ ہے', '(iii) په دې حالت کې د نمونې معلومات لنډوونکې د ازموینې احصاییه دا ده'),
])
b.eq(rf'Z=\frac{{({D})-(\mu_1-\mu_2)}}{{\sqrt{{\frac{{\sigma_1^2}}{{n_1}}+\frac{{\sigma_2^2}}{{n_2}}}}}}')
b.vpara('stat12-ex7-7-cr', tail_test('two', z=1.96, mid='', ticks=((-1.96, '−1.96'), (0, '0'), (1.96, '1.96')), label='Two-sided critical region at ±1.96'),
        '(iv) Calculation: $Z=\\frac{(8.75-7.25)-0}{\\sqrt{\\frac{9}{36}+\\frac{4}{64}}}=\\frac{1.5}{0.559}=2.683$', '(iv) حساب: $Z=\\frac{(8.75-7.25)-0}{\\sqrt{\\frac{9}{36}+\\frac{4}{64}}}=\\frac{1.5}{0.559}=2.683$', '(iv) محاسبه: $Z=\\frac{(8.75-7.25)-0}{\\sqrt{\\frac{9}{36}+\\frac{4}{64}}}=\\frac{1.5}{0.559}=2.683$', ratio=.45)
b.p('(v) Critical region:', '(v) فیصلہ کن علاقہ:', '(v) بحراني سیمه:')
b.p('Reject $H_0$ if $Z\\le -Z_{\\alpha/2}$ or $Z\\ge Z_{\\alpha/2}$ whereas $Z_{\\alpha/2}=Z_{0.025}=1.96$', '$H_0$ کو رد کریں اگر $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$ جبکہ $Z_{\\alpha/2}=Z_{0.025}=1.96$', '$H_0$ رد کړئ که $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$ په داسې حال کې چې $Z_{\\alpha/2}=Z_{0.025}=1.96$')
b.p('(vi) Conclusion:', '(vi) نتیجہ:', '(vi) پایله:')
b.p('As Z = 2.683 falls in the rejection region, therefore, we reject $H_0$ and conclude that effect of sleeping pill on male and female is different.', 'چونکہ Z = 2.683 رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں اور نتیجہ نکالتے ہیں کہ نیند کی گولی کا مردوں اور عورتوں پر اثر مختلف ہے۔', 'څرنګه چې Z = 2.683 د ردولو په سیمه کې لوېږي، نو $H_0$ ردوو او پایله اخلو چې د خوب د ګولۍ اغېز پر نارینه او ښځینه بېلابېل دی.')
e77 = b.build('stat12-p128-example-7-7', 'Example 7.7 — difference of means (σ known), sleeping pills', 'مثال 7.7 — اوسطوں کا فرق (σ معلوم)، نیند کی گولیاں', 'بېلګه 7.7 — د منځنیو توپیر (σ معلوم)، د خوب ګولۍ', 128, [247])

c = Builder()
c.h('7.2.4 Procedure for testing hypothesis about (μ₁ − μ₂) when σ₁² and σ₂² are unknown but sample sizes are large.', '7.2.4 جب σ₁² اور σ₂² نامعلوم ہوں لیکن نمونوں کے سائز بڑے ہوں تو (μ₁ − μ₂) کے بارے میں مفروضے کی جانچ کا طریقہ۔', '7.2.4 کله چې σ₁² او σ₂² نامعلوم وي خو د نمونو اندازې لویې وي د (μ₁ − μ₂) په اړه د فرضیې د ازموینې طریقه.')
c.p('When $\\sigma_1^2$ and $\\sigma_2^2$ are unknown, then for $n_1,n_2\\ge 30$, they are estimated by $S_1^2$ and $S_2^2$ respectively. The test statistic Z in this case is', 'جب $\\sigma_1^2$ اور $\\sigma_2^2$ نامعلوم ہوں تو $n_1,n_2\\ge 30$ کے لیے ان کا تخمین بالترتیب $S_1^2$ اور $S_2^2$ سے لگایا جاتا ہے۔ اس صورت میں جانچ کا شماریہ Z یہ ہے', 'کله چې $\\sigma_1^2$ او $\\sigma_2^2$ نامعلوم وي، نو د $n_1,n_2\\ge 30$ لپاره په ترتیب سره په $S_1^2$ او $S_2^2$ اټکل کېږي. په دې حالت کې د Z احصاییه دا ده')
c.eq(rf'Z=\frac{{({D})-(\mu_1-\mu_2)}}{{\sqrt{{\frac{{S_1^2}}{{n_1}}+\frac{{S_2^2}}{{n_2}}}}}}\sim N(0,1)\ \text{{approximately.}}')
c.p('Rest of the procedure for testing $H_0$ is same.', '$H_0$ کی جانچ کا باقی طریقہ یکساں ہے۔', 'د $H_0$ د ازموینې پاتې طریقه یو شان ده.')
c.h('Example 7.8', 'مثال 7.8', 'بېلګه 7.8')
c.p('To determine whether car ownership affects a student’s academic achievement, two random samples were drawn from the students. The grade point average for the $n_1=100$ car owners had $\\overline{X}_1=2.54$ and $S_1^2=0.40$ while for the $n_2=100$ non-owners of cars, $\\overline{X}_2=2.70$ and $S_2^2=0.36$.', 'یہ معلوم کرنے کے لیے کہ کیا گاڑی کی ملکیت طالب علم کی تعلیمی کارکردگی پر اثر ڈالتی ہے، طلبہ سے دو تصادفی نمونے لیے گئے۔ $n_1=100$ گاڑی مالکان کا گریڈ پوائنٹ اوسط $\\overline{X}_1=2.54$ اور $S_1^2=0.40$ تھا جبکہ $n_2=100$ غیر مالکان کا $\\overline{X}_2=2.70$ اور $S_2^2=0.36$ تھا۔', 'د دې معلومولو لپاره چې آیا د موټر لرل د زده کوونکي پر تعلیمي لاسته راوړنو اغېز کوي، له زده کوونکو دوه تصادفي نمونې واخیستل شوې. د $n_1=100$ موټر لرونکو د درجې د نمرو منځنی $\\overline{X}_1=2.54$ او $S_1^2=0.40$ و، په داسې حال کې چې د $n_2=100$ موټر نه لرونکو لپاره $\\overline{X}_2=2.70$ او $S_2^2=0.36$ و.')
c.p('Do the data present sufficient evidence to indicate a difference in the mean achievements between car owners and non-owners of cars? Test using α = 0.05.', 'کیا مواد گاڑی مالکان اور غیر مالکان کی اوسط کارکردگی میں فرق کا کافی ثبوت پیش کرتا ہے؟ α = 0.05 استعمال کرتے ہوئے جانچ کریں۔', 'آیا معلومات د موټر لرونکو او نه لرونکو د منځنیو لاسته راوړنو ترمنځ د توپیر لپاره کافي شواهد وړاندې کوي؟ د α = 0.05 په کارولو سره وازموئ.')
c.h(*SOL)
c.p('Let $\\mu_1$ denote mean of car owners and $\\mu_2$ denote mean of non-owners of cars, then', 'فرض کریں $\\mu_1$ گاڑی مالکان کا اوسط اور $\\mu_2$ غیر مالکان کا اوسط ظاہر کرتا ہے، تو', 'فرض کړئ $\\mu_1$ د موټر لرونکو منځنی او $\\mu_2$ د نه لرونکو منځنی ښيي، نو')
c.group('lines', [
    ('i. $H_0:\\mu_1-\\mu_2=0$',) * 3, ('$H_1:\\mu_1-\\mu_2\\neq 0$',) * 3, ('ii. α = 0.05',) * 3,
    ('iii. Test statistics:', 'iii. جانچ کا شماریہ:', 'iii. د ازموینې احصاییه:'),
    ('Since $\\sigma_1^2,\\sigma_2^2$ are not given but $n_1,n_2$ are large, so Z-statistic will be of the form', 'چونکہ $\\sigma_1^2,\\sigma_2^2$ نہیں دیے گئے لیکن $n_1,n_2$ بڑے ہیں، لہٰذا Z-شماریہ اس شکل کا ہوگا', 'څرنګه چې $\\sigma_1^2,\\sigma_2^2$ نه دي ورکړل شوي خو $n_1,n_2$ لوی دي، نو Z-احصاییه به دا بڼه ولري'),
])
c.eq(rf'Z=\frac{{({D})-(\mu_1-\mu_2)}}{{\sqrt{{\frac{{S_1^2}}{{n_1}}+\frac{{S_2^2}}{{n_2}}}}}}')
c.p('iv. Computations: Substituting values into the formula we get', 'iv. حساب: فارمولا میں قیمتیں رکھنے سے', 'iv. محاسبه: په فورمول کې د قیمتونو ایښودو سره')
c.eq(r'Z=\frac{(2.54-2.70)-0}{\sqrt{\frac{0.40}{100}+\frac{0.36}{100}}}=-1.84')
e78 = c.build('stat12-p128-example-7-8', '7.2.4 Test for μ₁ − μ₂ (σ unknown, large) — Example 7.8', '7.2.4 μ₁ − μ₂ کی جانچ (σ نامعلوم، بڑے) — مثال 7.8', '7.2.4 د μ₁ − μ₂ ازموینه (σ نامعلوم، لوی) — بېلګه 7.8', 128, [247, 248])

if __name__ == '__main__':
    save(128, [(7, e77), (7, e78)])
