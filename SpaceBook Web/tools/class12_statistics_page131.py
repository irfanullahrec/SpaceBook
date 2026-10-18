"""PDF131 printed 253–254: Example 7.10 steps iv–vi (t = 0.187); 7.2.6 test for proportion p (large sample) with three figures; Example 7.11 start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
Z = r'Z=\frac{\hat{p}-p}{\sqrt{\frac{pq}{n}}}'
b = Builder()
b.mlines([r's_2^2=\frac{1}{n_2-1}\left[\Sigma x_2^2-\frac{(\Sigma x_2)^2}{n_2}\right]',
          r'\text{Or}\ (n_2-1)s_2^2=\Sigma x_2^2-\frac{(\Sigma x_2)^2}{n_2}=31707-\frac{(551)^2}{10}=1346.9',
          r'\text{Now}\quad s_p=\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}=\sqrt{\frac{754.9167+1346.9}{12+10-2}}',
          r'=\sqrt{\frac{2101.8167}{20}}=10.25',
          r'\text{Hence } t=\frac{(55.92-55.1)-0}{10.25\sqrt{\frac{1}{12}+\frac{1}{10}}}=\frac{0.82}{4.3888}=0.187'])
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.p('We will reject $H_0$ if $t<t_{\\alpha/2,\\nu}$ of $t>t_{\\alpha/2,\\nu}$ where as', 'ہم $H_0$ کو رد کریں گے اگر $t<t_{\\alpha/2,\\nu}$ یا $t>t_{\\alpha/2,\\nu}$ جبکہ', 'موږ به $H_0$ رد کړو که $t<t_{\\alpha/2,\\nu}$ یا $t>t_{\\alpha/2,\\nu}$ په داسې حال کې چې')
b.eq(r't_{\alpha/2,\nu}=t_{0.05/2,(12+10-2)}=t_{0.025,(20)}=2.086')
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('As our computed value of t lies in the acceptance region, therefore, we accept $H_0$.', 'چونکہ ہماری معلوم کی گئی t کی قیمت قبولیت کے علاقے میں ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں۔', 'څرنګه چې زموږ د t محاسبه شوی قیمت د منلو په سیمه کې پروت دی، نو $H_0$ منو.')
e710 = b.build('stat12-p131-example-7-10-end', 'Example 7.10 — pooled variance, t value and conclusion', 'مثال 7.10 — مشترکہ تغیر، t کی قیمت اور نتیجہ', 'بېلګه 7.10 — ګډ واریانس، د t قیمت او پایله', 131, [253])

c = Builder()
c.h('7.2.6 Procedure of testing hypothesis about population pro ortion p [large sample]', '7.2.6 آبادی کے تناسب p کے بارے میں مفروضے کی جانچ کا طریقہ [بڑا نمونہ]', '7.2.6 د نفوس د تناسب p په اړه د فرضیې د ازموینې طریقه [لویه نمونه]')
c.p('For large n, (n ≥ 30), and the hypothesis testing procedure is out lined as below:', 'بڑے n کے لیے (n ≥ 30)، مفروضے کی جانچ کا طریقہ نیچے بیان کیا گیا ہے:', 'د لوی n لپاره (n ≥ 30)، د فرضیې د ازموینې طریقه لاندې بیان شوې:')
c.mlines([r'i.\ (a)\quad H_0:p=p_0\quad\text{versus}\quad H_1:p\neq p_0', r'(b)\quad H_0:p\le p_0\quad\text{versus}\quad H_1:p>p_0', r'(c)\quad H_0:p\ge p_0\quad\text{versus}\quad H_1:p<p_0'])
c.p('ii. Choose $\\alpha=0.01$ or 0.05 etc.', 'ii. $\\alpha=0.01$ یا 0.05 وغیرہ منتخب کریں۔', 'ii. $\\alpha=0.01$ یا 0.05 او نور وټاکئ.')
c.vpara('stat12-prop-cr-a', tail_test('two', ticks=((-1.4, '−Zα/2'), (1.4, 'Zα/2')), label='Two-sided critical region'),
        f'iii. Test statistic to be used in this case is ${Z}\\sim N(0,1)$ under $H_0$, when n ≥ 30', f'iii. اس صورت میں استعمال ہونے والا جانچ کا شماریہ ${Z}\\sim N(0,1)$ ہے، $H_0$ کے تحت جب n ≥ 30', f'iii. په دې حالت کې کارېدونکې د ازموینې احصاییه ${Z}\\sim N(0,1)$ ده، د $H_0$ لاندې کله چې n ≥ 30', ratio=.45)
c.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
c.vpara('stat12-prop-cr-b', tail_test('right', ticks=((1.4, 'Zα'),), label='Right-sided critical region'),
        'v. Critical region according to $H_1$ is stated as', 'v. $H_1$ کے مطابق فیصلہ کن علاقہ یوں بیان کیا جاتا ہے', 'v. د $H_1$ له مخې بحراني سیمه داسې بیانېږي', ratio=.45)
c.group('lines', [('(a) Reject $H_0$ if $Z\\le -Z_{\\alpha/2}$ or $Z\\ge Z_{\\alpha/2}$', '(a) $H_0$ کو رد کریں اگر $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$', '(a) $H_0$ رد کړئ که $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$'),
                  ('(b) Reject $H_0$ if $Z>Z_\\alpha$', '(b) $H_0$ کو رد کریں اگر $Z>Z_\\alpha$', '(b) $H_0$ رد کړئ که $Z>Z_\\alpha$')])
c.vpara('stat12-prop-cr-c', tail_test('left', ticks=((-1.4, '−Zα'),), label='Left-sided critical region'),
        '(c) Reject $H_0$ if $Z<-Z_\\alpha$', '(c) $H_0$ کو رد کریں اگر $Z<-Z_\\alpha$', '(c) $H_0$ رد کړئ که $Z<-Z_\\alpha$', ratio=.45)
c.p('vi. Conclusion.', 'vi. نتیجہ۔', 'vi. پایله.')
c.h('Example 7.11', 'مثال 7.11', 'بېلګه 7.11')
c.p('A producer of orange juice claims that 35 percent of all orange juice drinkers prefer its product. To test the claim, a random sample of 200 orange juice drinkers was taken at random and it was found that only 62 of them preferred the producer’s brand. Test the producer’s claim at five percent level of significance.',
    'مالٹے کے رس کا ایک پروڈیوسر دعویٰ کرتا ہے کہ مالٹے کا رس پینے والوں میں سے 35 فیصد اس کی مصنوعات کو ترجیح دیتے ہیں۔ دعوے کی جانچ کے لیے مالٹے کا رس پینے والے 200 افراد کا تصادفی نمونہ لیا گیا اور معلوم ہوا کہ ان میں سے صرف 62 نے پروڈیوسر کے برانڈ کو ترجیح دی۔ پانچ فیصد معنویت کی سطح پر پروڈیوسر کے دعوے کی جانچ کریں۔',
    'د مالټې د جوس یو تولیدوونکی ادعا کوي چې د مالټې د جوس له ټولو څښونکو 35 سلنه د هغه محصول غوره ګڼي. د ادعا د ازمویلو لپاره د مالټې د جوس د 200 څښونکو تصادفي نمونه واخیستل شوه او معلومه شوه چې یوازې 62 یې د تولیدوونکي برانډ غوره کړ. د پنځه سلنه معنی‌داریت په کچه د تولیدوونکي ادعا وازموئ.')
c.h(*SOL)
c.group('lines', [('i. $H_0:p=35\\%=0.35$',) * 3, ('$H_1:p\\neq 0.35$',) * 3, ('ii. $\\alpha=0.05$',) * 3,
                  (f'iii. Test statistic to be used here is ${Z}$', f'iii. یہاں استعمال ہونے والا جانچ کا شماریہ ${Z}$ ہے', f'iii. دلته کارېدونکې د ازموینې احصاییه ${Z}$ ده'),
                  ('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')])
pr = c.build('stat12-p131-proportion-test', '7.2.6 Test for a population proportion — procedure; Example 7.11 start', '7.2.6 آبادی کے تناسب کی جانچ — طریقہ؛ مثال 7.11 کا آغاز', '7.2.6 د نفوس د تناسب ازموینه — طریقه؛ د بېلګې 7.11 پیل', 131, [253, 254])
issues = [{'id': 'stat12-p253-critical-region-typos', 'unit': 7, 'printedPage': 253, 'description': 'Example 7.10 step v prints “t < tα/2,ν of t > tα/2,ν” (missing minus sign and “of” for “or”); 7.2.6 heading prints “pro ortion” and body “out lined”. Printed text retained.'}]

if __name__ == '__main__':
    save(131, [(7, e710), (7, pr)], issues=issues)
