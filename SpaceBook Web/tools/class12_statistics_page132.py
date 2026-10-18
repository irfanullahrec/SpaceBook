"""PDF132 printed 255–256: Example 7.11 steps iv–vi (Z = −1.19); 7.2.7 test for p1−p2 (large sample) with three figures; Example 7.12 steps i–iii."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
Z2 = r'Z=\frac{(\hat{p}_1-\hat{p}_2)-(p_1-p_2)}{\sqrt{\frac{\hat{p}_1\hat{q}_1}{n_1}+\frac{\hat{p}_2\hat{q}_2}{n_2}}}\sim N(0,1)\ \text{under }H_0.'
b = Builder()
b.mlines([r'\text{Given that } p=0.35,\ q=1-p=1-0.35=0.65,\ n=200,\ X=62,',
          r'\therefore\ \hat{p}=\frac{X}{n}=\frac{62}{200}=0.31,',
          r'Z=\frac{0.31-0.35}{\sqrt{\frac{(0.35)(0.65)}{200}}}=-1.19'])
b.p('v. Critical region is stated as:', 'v. فیصلہ کن علاقہ یوں بیان کیا جاتا ہے:', 'v. بحراني سیمه داسې بیانېږي:')
b.vpara('stat12-ex7-11-cr', tail_test('two', z=1.96, mid='', ticks=((-1.96, '−1.96'), (0, '0'), (1.96, '1.96')), label='Two-sided critical region at ±1.96'),
        'Reject $H_0$ if $Z\\le -Z_{\\alpha/2}$ or $Z\\ge Z_{\\alpha/2}$ where $Z_{\\alpha/2}=Z_{0.05/2}=Z_{0.025}=1.96$',
        '$H_0$ کو رد کریں اگر $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$ جہاں $Z_{\\alpha/2}=Z_{0.05/2}=Z_{0.025}=1.96$',
        '$H_0$ رد کړئ که $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$ چې $Z_{\\alpha/2}=Z_{0.05/2}=Z_{0.025}=1.96$', ratio=.45)
b.p('vi. conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('As Z =− 1.19 falls in the acceptance region, therefore, we accept $H_0$ i.e. we do not reject producer’s claim is correct.', 'چونکہ Z =− 1.19 قبولیت کے علاقے میں ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں یعنی ہم پروڈیوسر کے دعوے کو رد نہیں کرتے، دعویٰ درست ہے۔', 'څرنګه چې Z =− 1.19 د منلو په سیمه کې لوېږي، نو $H_0$ منو یعنې د تولیدوونکي ادعا نه ردوو، ادعا سمه ده.')
e711 = b.build('stat12-p132-example-7-11', 'Example 7.11 — proportion test (orange juice)', 'مثال 7.11 — تناسب کی جانچ (مالٹے کا رس)', 'بېلګه 7.11 — د تناسب ازموینه (د مالټې جوس)', 132, [255])

c = Builder()
c.h('7.2.7 Procedure for testing hypothesis about difference of two population proportions (p₁−p₂) [large sample]', '7.2.7 دو آبادیوں کے تناسبات کے فرق (p₁−p₂) کے بارے میں مفروضے کی جانچ کا طریقہ [بڑا نمونہ]', '7.2.7 د دوو نفوسونو د تناسبونو د توپیر (p₁−p₂) په اړه د فرضیې د ازموینې طریقه [لویه نمونه]')
c.p('The testing of hypothesis procedure in this case is given below.', 'اس صورت میں مفروضے کی جانچ کا طریقہ نیچے دیا گیا ہے۔', 'په دې حالت کې د فرضیې د ازموینې طریقه لاندې ورکړل شوې.')
c.mlines([r'i.\ (a)\ H_0:p_1-p_2=0\quad (b)\ H_0:p_1-p_2\le 0\quad (c)\ H_0:p_1-p_2\ge 0',
          r'H_1:p_1-p_2\neq 0\qquad H_1:p_1-p_2>0\qquad H_1:p_1-p_2<0'])
c.p('ii. Choose an appropriate level of significance.', 'ii. معنویت کی موزوں سطح منتخب کریں۔', 'ii. د معنی‌داریت مناسبه کچه وټاکئ.')
c.p('iii. Z-test is used where as', 'iii. Z-جانچ استعمال کی جاتی ہے جبکہ', 'iii. Z-ازموینه کارول کېږي په داسې حال کې چې')
c.eq(Z2)
c.p('iv Calculation:', 'iv حساب:', 'iv محاسبه:')
c.vpara('stat12-pdiff-cr-a', tail_test('two', ticks=((-1.4, '−Zα/2'), (1.4, 'Zα/2')), label='Two-sided critical region'),
        'v. Critical region is constructed according to $H_1$ as;', 'v. فیصلہ کن علاقہ $H_1$ کے مطابق یوں بنایا جاتا ہے؛', 'v. بحراني سیمه د $H_1$ له مخې داسې جوړېږي؛', ratio=.45)
c.p('Case (a) Reject $H_0$ if $Z_c\\le -Z_{\\alpha/2}$ or $Z_c\\ge Z_{\\alpha/2}$ i.e.', 'صورت (a) $H_0$ کو رد کریں اگر $Z_c\\le -Z_{\\alpha/2}$ یا $Z_c\\ge Z_{\\alpha/2}$ یعنی', 'حالت (a) $H_0$ رد کړئ که $Z_c\\le -Z_{\\alpha/2}$ یا $Z_c\\ge Z_{\\alpha/2}$ یعنې')
c.vpara('stat12-pdiff-cr-b', tail_test('right', ticks=((1.4, 'Zα'),), label='Right-sided critical region'),
        'Case (b) Reject $H_0$ if $Z_c\\ge Z_\\alpha$ i.e.', 'صورت (b) $H_0$ کو رد کریں اگر $Z_c\\ge Z_\\alpha$ یعنی', 'حالت (b) $H_0$ رد کړئ که $Z_c\\ge Z_\\alpha$ یعنې', ratio=.45)
c.vpara('stat12-pdiff-cr-c', tail_test('left', ticks=((-1.4, '−Zα'),), label='Left-sided critical region'),
        'Case (c) Reject $H_0$ if $Z_c\\le -Z_\\alpha$ i.e.', 'صورت (c) $H_0$ کو رد کریں اگر $Z_c\\le -Z_\\alpha$ یعنی', 'حالت (c) $H_0$ رد کړئ که $Z_c\\le -Z_\\alpha$ یعنې', ratio=.45)
c.p('v. Conclusion.', 'v. نتیجہ۔', 'v. پایله.')
c.h('Example7.12', 'مثال 7.12', 'بېلګه 7.12')
c.p('A soap-manufacturing factory produces two brands of soap. A sample survey was conducted and it was found that 56 users out of 200 preferred brand “A” and that 30 users out of 150 preferred brand “B”. Test the hypothesis that sale of brand A is at least 10% greater than brand B at 5% level of significance.',
    'صابن بنانے والا ایک کارخانہ صابن کے دو برانڈ تیار کرتا ہے۔ ایک نمونہ سروے کیا گیا اور معلوم ہوا کہ 200 میں سے 56 صارفین نے برانڈ “A” کو اور 150 میں سے 30 صارفین نے برانڈ “B” کو ترجیح دی۔ 5% معنویت کی سطح پر اس مفروضے کی جانچ کریں کہ برانڈ A کی فروخت برانڈ B سے کم از کم 10% زیادہ ہے۔',
    'د صابون جوړولو یوه فابریکه د صابون دوه برانډه تولیدوي. یوه نمونه‌یي سروې وشوه او معلومه شوه چې له 200 کاروونکو 56 برانډ “A” او له 150 کاروونکو 30 برانډ “B” غوره کړ. د 5% معنی‌داریت په کچه دا فرضیه وازموئ چې د A برانډ پلور د B برانډ په پرتله لږ تر لږه 10% زیات دی.')
c.h(*SOL)
c.p('Let $p_1$ denote the proportion of brand-A users and $p_2$ denote the proportion of brand-B users.', 'فرض کریں $p_1$ برانڈ-A کے صارفین کا تناسب اور $p_2$ برانڈ-B کے صارفین کا تناسب ظاہر کرتا ہے۔', 'فرض کړئ $p_1$ د A-برانډ د کاروونکو تناسب او $p_2$ د B-برانډ د کاروونکو تناسب ښيي.')
c.group('lines', [('i. $H_0:p_1-p_2\\ge 0.10$',) * 3, ('$H_1:p_1-p_2<0.10$',) * 3, ('ii. $\\alpha=0.05$',) * 3, ('iii. Test statistic:', 'iii. جانچ کا شماریہ:', 'iii. د ازموینې احصاییه:')])
c.p('From $H_0$ we see that $p_1\\neq p_2$ and they are unknown therefore they are estimated by $\\hat{p}_1$ and $\\hat{p}_2$ respectively. The test statistic to be used is;', '$H_0$ سے ہم دیکھتے ہیں کہ $p_1\\neq p_2$ اور یہ نامعلوم ہیں، لہٰذا ان کا تخمین بالترتیب $\\hat{p}_1$ اور $\\hat{p}_2$ سے لگایا جاتا ہے۔ استعمال ہونے والا جانچ کا شماریہ یہ ہے؛', 'له $H_0$ څخه وینو چې $p_1\\neq p_2$ او نامعلوم دي، نو په ترتیب سره په $\\hat{p}_1$ او $\\hat{p}_2$ اټکل کېږي. کارېدونکې د ازموینې احصاییه دا ده؛')
c.eq(Z2)
pd = c.build('stat12-p132-proportion-difference', '7.2.7 Test for p₁ − p₂ — procedure; Example 7.12 start', '7.2.7 p₁ − p₂ کی جانچ — طریقہ؛ مثال 7.12 کا آغاز', '7.2.7 د p₁ − p₂ ازموینه — طریقه؛ د بېلګې 7.12 پیل', 132, [255, 256])
issues = [{'id': 'stat12-p256-step-numbering', 'unit': 7, 'printedPage': 256, 'description': '7.2.7 numbers the conclusion step “v.” (repeating v; should be vi); heading printed “Example7.12” without a space. Printed numbering retained.'}]

if __name__ == '__main__':
    save(132, [(7, e711), (7, pd)], issues=issues)
