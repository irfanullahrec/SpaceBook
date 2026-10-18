"""PDF129 printed 249–250: Example 7.8 steps v–vi; 7.2.5 pooled two-sample t test (assumptions, steps, figures); Example 7.9 start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
D = r'\overline{X}_1-\overline{X}_2'
b = Builder()
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.vpara('stat12-ex7-8-cr', tail_test('two', z=1.96, mid='', ticks=((-1.96, '−1.96'), (0, '0'), (1.96, '1.96')), label='Two-sided critical region at ±1.96'),
        'Reject $H_0$ if $Z\\ge Z_{\\alpha/2}$ or $Z\\le -Z_{\\alpha/2}$ where $Z_{\\alpha/2}=1.96$', '$H_0$ کو رد کریں اگر $Z\\ge Z_{\\alpha/2}$ یا $Z\\le -Z_{\\alpha/2}$ جہاں $Z_{\\alpha/2}=1.96$', '$H_0$ رد کړئ که $Z\\ge Z_{\\alpha/2}$ یا $Z\\le -Z_{\\alpha/2}$ چې $Z_{\\alpha/2}=1.96$', ratio=.45)
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('We see that Z = − 1.84 is lying in the acceptance region. Hence $H_0$ cannot be rejected.', 'ہم دیکھتے ہیں کہ Z = − 1.84 قبولیت کے علاقے میں ہے۔ لہٰذا $H_0$ کو رد نہیں کیا جا سکتا۔', 'وینو چې Z = − 1.84 د منلو په سیمه کې پروت دی. نو $H_0$ نه شي ردېدای.')
e78 = b.build('stat12-p129-example-7-8-end', 'Example 7.8 — critical region and conclusion', 'مثال 7.8 — فیصلہ کن علاقہ اور نتیجہ', 'بېلګه 7.8 — بحراني سیمه او پایله', 129, [249])

c = Builder()
c.h('7.2.5 Procedure for testing hypothesis about (μ₁ − μ₂) when σ₁² = σ₂² = σ² but unknown [small samples]', '7.2.5 جب σ₁² = σ₂² = σ² لیکن نامعلوم ہوں تو (μ₁ − μ₂) کے بارے میں مفروضے کی جانچ کا طریقہ [چھوٹے نمونے]', '7.2.5 کله چې σ₁² = σ₂² = σ² خو نامعلوم وي د (μ₁ − μ₂) په اړه د فرضیې د ازموینې طریقه [کوچنۍ نمونې]')
c.p('When population variances are unknown and samples are of small size then the following assumption are made to use a two-sample t-test.', 'جب آبادیوں کے تغیرات نامعلوم ہوں اور نمونے چھوٹے سائز کے ہوں تو دو نمونوں کی t-جانچ استعمال کرنے کے لیے درج ذیل مفروضے لیے جاتے ہیں۔', 'کله چې د نفوسونو واریانسونه نامعلوم وي او نمونې کوچنۍ وي، نو د دوه‌نمونوي t-ازموینې د کارولو لپاره لاندې فرضیې کېږي.')
c.group('lines', [
    ('(i) The sampled populations are normal.', '(i) نمونہ لی گئی آبادیاں نارمل ہیں۔', '(i) نمونه ترې اخیستل شوي نفوسونه نورمال دي.'),
    ('(ii) $\\sigma_1^2$ and $\\sigma_2^2$ are assumed to be equal but unknown', '(ii) $\\sigma_1^2$ اور $\\sigma_2^2$ کو برابر لیکن نامعلوم فرض کیا جاتا ہے', '(ii) $\\sigma_1^2$ او $\\sigma_2^2$ برابر خو نامعلوم ګڼل کېږي'),
    ('(iii) The samples are drawn randomly.', '(iii) نمونے تصادفی طور پر نکالے جاتے ہیں۔', '(iii) نمونې په تصادفي ډول راایستل کېږي.'),
])
c.p('Procedure for testing $H_0$ is given below:', '$H_0$ کی جانچ کا طریقہ نیچے دیا گیا ہے:', 'د $H_0$ د ازموینې طریقه لاندې ورکړل شوې:')
c.mlines([r'i.\ (a)\quad H_0:\mu_1-\mu_2=0\ \text{versus}\ H_1:\mu_1-\mu_2\neq 0', r'(b)\quad H_0:\mu_1-\mu_2\ge 0\ \text{versus}\ H_1:\mu_1-\mu_2<0', r'(c)\quad H_0:\mu_1-\mu_2\le 0\ \text{versus}\ H_1:\mu_1-\mu_2>0'])
c.p('ii. Choose α = 0.01 or 0.05 etc.', 'ii. α = 0.01 یا 0.05 وغیرہ منتخب کریں۔', 'ii. α = 0.01 یا 0.05 او نور وټاکئ.')
c.p('iii. Test statistic to be used in this case is', 'iii. اس صورت میں استعمال ہونے والا جانچ کا شماریہ یہ ہے', 'iii. په دې حالت کې کارېدونکې د ازموینې احصاییه دا ده')
c.p(f'$t=\\frac{{({D})-(\\mu_1-\\mu_2)}}{{s_p\\sqrt{{\\frac{{1}}{{n_1}}+\\frac{{1}}{{n_2}}}}}}$, Which has t-distribution with $\\nu=n_1+n_2-2$ d.f.', f'$t=\\frac{{({D})-(\\mu_1-\\mu_2)}}{{s_p\\sqrt{{\\frac{{1}}{{n_1}}+\\frac{{1}}{{n_2}}}}}}$، جس کی t-تقسیم $\\nu=n_1+n_2-2$ درجاتِ آزادی کے ساتھ ہے۔', f'$t=\\frac{{({D})-(\\mu_1-\\mu_2)}}{{s_p\\sqrt{{\\frac{{1}}{{n_1}}+\\frac{{1}}{{n_2}}}}}}$، چې د $\\nu=n_1+n_2-2$ د ازادۍ درجو سره t-وېش لري.')
c.p('iv. Computation of t-statistic value.', 'iv. t-شماریے کی قیمت کا حساب۔', 'iv. د t-احصاییې د قیمت محاسبه.')
c.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
c.vpara('stat12-pooled-cr-a', tail_test('two', ticks=((-1.4, '−tα/2,ν'), (1.4, 'tα/2,ν')), label='Two-sided t critical region'),
        'For case (a) Reject $H_0$ if $t_c\\le -t_{\\alpha/2,\\nu}$ or $t\\ge t_{\\alpha/2,\\nu}$', 'صورت (a) کے لیے $H_0$ کو رد کریں اگر $t_c\\le -t_{\\alpha/2,\\nu}$ یا $t\\ge t_{\\alpha/2,\\nu}$', 'د (a) حالت لپاره $H_0$ رد کړئ که $t_c\\le -t_{\\alpha/2,\\nu}$ یا $t\\ge t_{\\alpha/2,\\nu}$', ratio=.45)
c.vpara('stat12-pooled-cr-b', tail_test('left', ticks=((-1.4, '−tα,ν'),), label='Left-sided t critical region'),
        'For case (b) Reject $H_0$ if $t_c\\le -t_{\\alpha,\\nu}$', 'صورت (b) کے لیے $H_0$ کو رد کریں اگر $t_c\\le -t_{\\alpha,\\nu}$', 'د (b) حالت لپاره $H_0$ رد کړئ که $t_c\\le -t_{\\alpha,\\nu}$', ratio=.45)
c.vpara('stat12-pooled-cr-c', tail_test('right', ticks=((1.4, 'tα,ν'),), label='Right-sided t critical region'),
        'For case (c) Reject $H_0$ if $t_c\\ge t_{\\alpha,\\nu}$', 'صورت (c) کے لیے $H_0$ کو رد کریں اگر $t_c\\ge t_{\\alpha,\\nu}$', 'د (c) حالت لپاره $H_0$ رد کړئ که $t_c\\ge t_{\\alpha,\\nu}$', ratio=.45)
c.p('vi. Conclusion.', 'vi. نتیجہ۔', 'vi. پایله.')
c.h('Example 7.9', 'مثال 7.9', 'بېلګه 7.9')
c.p('An examination was given to two classes of 8 and 10 students respectively. In the first class mean grade was 95 with a standard deviation of 6.8556, while in the second class, the mean grade was 97 with a standard deviation of 5.4772. It is assumed that the two classes of students are normally distributed having identical variances. Is there a significance difference between the mean grades? Test at α = 0.01.',
    'بالترتیب 8 اور 10 طلبہ کی دو جماعتوں کا امتحان لیا گیا۔ پہلی جماعت میں اوسط گریڈ 95 اور معیاری انحراف 6.8556 تھا، جبکہ دوسری جماعت میں اوسط گریڈ 97 اور معیاری انحراف 5.4772 تھا۔ فرض کیا جاتا ہے کہ طلبہ کی دونوں جماعتیں یکساں تغیرات کے ساتھ نارمل تقسیم شدہ ہیں۔ کیا اوسط گریڈوں کے درمیان معنی خیز فرق ہے؟ α = 0.01 پر جانچ کریں۔',
    'په ترتیب سره د 8 او 10 زده کوونکو دوو ټولګیو ته ازموینه ورکړل شوه. په لومړي ټولګي کې منځنۍ درجه 95 او معیاري انحراف 6.8556 و، په داسې حال کې چې په دویم ټولګي کې منځنۍ درجه 97 او معیاري انحراف 5.4772 و. انګېرل کېږي چې د زده کوونکو دواړه ټولګي د یو شان واریانسونو سره نورمال وېش لري. آیا د منځنیو درجو ترمنځ معنی‌دار توپیر شته؟ په α = 0.01 وازموئ.')
c.h(*SOL)
c.group('lines', [('i. $H_0:\\mu_1=\\mu_2$ versus $H_1:\\mu_1\\neq\\mu_2$', 'i. $H_0:\\mu_1=\\mu_2$ بمقابلہ $H_1:\\mu_1\\neq\\mu_2$', 'i. $H_0:\\mu_1=\\mu_2$ د $H_1:\\mu_1\\neq\\mu_2$ پر وړاندې'), ('ii. α = 0.01',) * 3, ('iii. Test statistic:', 'iii. جانچ کا شماریہ:', 'iii. د ازموینې احصاییه:')])
pt = c.build('stat12-p129-pooled-t-test', '7.2.5 Pooled two-sample t test — procedure; Example 7.9 start', '7.2.5 مشترکہ دو نمونوں کی t جانچ — طریقہ؛ مثال 7.9 کا آغاز', '7.2.5 ګډه دوه‌نمونوي t ازموینه — طریقه؛ د بېلګې 7.9 پیل', 129, [249, 250])
issues = [{'id': 'stat12-p250-significance-difference', 'unit': 7, 'printedPage': 250, 'description': 'Example 7.9 prints “significance difference” (for significant difference); printed wording retained.'}]

if __name__ == '__main__':
    save(129, [(7, e78), (7, pt)], issues=issues)
