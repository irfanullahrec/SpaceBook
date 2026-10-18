"""PDF130 printed 251–252: Example 7.9 steps iii–vi (pooled t, t = −0.689); Example 7.10 (two samples) steps i–iv start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
D = r'\overline{X}_1-\overline{X}_2'
T = rf't=\frac{{({D})-(\mu_1-\mu_2)}}{{s_p\sqrt{{\frac{{1}}{{n_1}}+\frac{{1}}{{n_2}}}}}}'
b = Builder()
b.p(f'As $\\sigma_1^2$ and $\\sigma_2^2$ are unknown and $n_1,n_2$ are small ,therefore, test statistic to be used here is ${T}$ with $\\nu=n_1+n_2-2$ d.f',
    f'چونکہ $\\sigma_1^2$ اور $\\sigma_2^2$ نامعلوم ہیں اور $n_1,n_2$ چھوٹے ہیں، لہٰذا یہاں استعمال ہونے والا جانچ کا شماریہ ${T}$ ہے جس کے درجاتِ آزادی $\\nu=n_1+n_2-2$ ہیں',
    f'څرنګه چې $\\sigma_1^2$ او $\\sigma_2^2$ نامعلوم دي او $n_1,n_2$ کوچني دي، نو دلته کارېدونکې د ازموینې احصاییه ${T}$ ده چې د ازادۍ درجې یې $\\nu=n_1+n_2-2$ دي')
b.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
b.mlines([r'\text{Given that } n_1=8,\ n_2=10,\ \overline{X}_1=95,\ \overline{X}_2=97,\ s_1^2=47,\ s_2^2=30',
          r'\text{Now}\quad s_p=\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}=\sqrt{\frac{(8-1)47+(10-1)30}{8+10-2}}',
          r'=\sqrt{\frac{329+270}{16}}=6.12',
          r'\text{Hence } t=\frac{(95-97)-0}{6.12\sqrt{\frac{1}{8}+\frac{1}{10}}}=\frac{-2}{2.930}=-0.689'])
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.vpara('stat12-ex7-9-cr', tail_test('two', z=2.92, mid='', ticks=((-2.92, '−2.92'), (0, '0'), (2.92, '2.92')), label='Two-sided t critical region at ±2.92'),
        'Reject $H_0$ if $t\\le -t_{\\alpha/2,\\nu}$ or $t\\ge t_{\\alpha/2,\\nu}$, whereas $t_{\\alpha/2,\\nu}=t_{0.01/2,\\,8+10-2}=t_{0.005,(16)}=2.92$',
        '$H_0$ کو رد کریں اگر $t\\le -t_{\\alpha/2,\\nu}$ یا $t\\ge t_{\\alpha/2,\\nu}$، جبکہ $t_{\\alpha/2,\\nu}=t_{0.01/2,\\,8+10-2}=t_{0.005,(16)}=2.92$',
        '$H_0$ رد کړئ که $t\\le -t_{\\alpha/2,\\nu}$ یا $t\\ge t_{\\alpha/2,\\nu}$، په داسې حال کې چې $t_{\\alpha/2,\\nu}=t_{0.01/2,\\,8+10-2}=t_{0.005,(16)}=2.92$', ratio=.45)
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('Our calculated value of t falls in the acceptance region, so we accept $H_0$.', 'ہماری معلوم کی گئی t کی قیمت قبولیت کے علاقے میں آتی ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں۔', 'زموږ د t محاسبه شوی قیمت د منلو په سیمه کې لوېږي، نو $H_0$ منو.')
e79 = b.build('stat12-p130-example-7-9', 'Example 7.9 — pooled t test (class grades)', 'مثال 7.9 — مشترکہ t جانچ (جماعتوں کے گریڈ)', 'بېلګه 7.9 — ګډه t ازموینه (د ټولګیو درجې)', 130, [251])

c = Builder()
c.h('Example 7.10', 'مثال 7.10', 'بېلګه 7.10')
c.p('The following two samples are drawn from the normally distributed population with identical but unknown variances.', 'درج ذیل دو نمونے یکساں لیکن نامعلوم تغیرات والی نارمل تقسیم شدہ آبادی سے نکالے گئے ہیں۔', 'لاندې دوه نمونې د یو شان خو نامعلومو واریانسونو لرونکي نورمال وېش لرونکي نفوس څخه راایستل شوې دي.')
c.group('lines', [
    ('Sample 1: 70 68 63 60 59 57 53 51 50 49 46 45', 'نمونہ 1: 70 68 63 60 59 57 53 51 50 49 46 45', 'نمونه 1: 70 68 63 60 59 57 53 51 50 49 46 45'),
    ('Sample 2: 75 72 70 50 48 43 52 50 46 45', 'نمونہ 2: 75 72 70 50 48 43 52 50 46 45', 'نمونه 2: 75 72 70 50 48 43 52 50 46 45'),
])
c.p('Test the equality of means at α = 0.05 level of significance.', 'α = 0.05 معنویت کی سطح پر اوسطوں کی برابری کی جانچ کریں۔', 'د α = 0.05 د معنی‌داریت په کچه د منځنیو برابري وازموئ.')
c.h(*SOL)
c.group('lines', [('i. $H_0:\\mu_1=\\mu_2$',) * 3, ('$H_1:\\mu_1\\neq\\mu_2$',) * 3, ('ii. $\\alpha=0.05$',) * 3,
                  ('iii t-test statistic to be used here is', 'iii یہاں استعمال ہونے والا t-جانچ کا شماریہ یہ ہے', 'iii دلته کارېدونکې د t-ازموینې احصاییه دا ده')])
c.p(f'${T}$ with $\\nu=n_1+n_2-2$ degrees of freedom', f'${T}$ جس کے درجاتِ آزادی $\\nu=n_1+n_2-2$ ہیں', f'${T}$ چې د ازادۍ درجې یې $\\nu=n_1+n_2-2$ دي')
c.p('(iv) Calculation:', '(iv) حساب:', '(iv) محاسبه:')
c.p('For sample-1:', 'نمونہ-1 کے لیے:', 'د نمونې-1 لپاره:')
c.mlines([r'n_1=12,\ \Sigma x_1=671,\ \Sigma x_1^2=38275,\ \overline{X}_1=55.92',
          r's_1^2=\frac{1}{n_1-1}\left[\Sigma x_1^2-\frac{(\Sigma x_1)^2}{n_1}\right]',
          r'\text{or}\ (n_1-1)s_1^2=\Sigma x_1^2-\frac{(\Sigma x_1)^2}{n_1}=38275-\frac{(671)^2}{12}=754.9167'])
c.p('For sample-2:', 'نمونہ-2 کے لیے:', 'د نمونې-2 لپاره:')
c.eq(r'n_2=10,\ \Sigma x_2=551,\ \Sigma x_2^2=31707,\ \overline{X}_2=55.1')
e710 = c.build('stat12-p130-example-7-10', 'Example 7.10 — pooled t test from raw samples (start)', 'مثال 7.10 — خام نمونوں سے مشترکہ t جانچ (آغاز)', 'بېلګه 7.10 — له خامو نمونو ګډه t ازموینه (پیل)', 130, [252])
issues = [{'id': 'stat12-p251-denominator-2930', 'unit': 7, 'printedPage': 251, 'description': 'Example 7.9 prints the denominator 6.12√(1/8+1/10) as 2.930; it computes to 2.903 (−2/2.903 = −0.689, the printed result). Printed 2.930 retained.'}]

if __name__ == '__main__':
    save(130, [(7, e79), (7, e710)], issues=issues)
