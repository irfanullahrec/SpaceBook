"""PDF145 printed 281–282: Example 8.4 steps iv–vi (χ² = 46.994 > 9.49); 8.2.2 shortcut χ² for 2×2; Example 8.5 (education vs football, χ² = 1.5625); 8.2.3 start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import chi_tail

SHORT = r'\chi^2=\frac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}\ \text{with 1 d.f}'
b = Builder()
b.eq(r'\chi^2=\sum_{i=1}^{3}\sum_{j=1}^{3}\frac{(O_{ij}-e_{ij})^2}{e_{ij}}=46.994')
b.p('v. Critical region', 'v. فیصلہ کن علاقہ', 'v. بحراني سیمه')
b.vpara('stat12-ex8-4-cr', chi_tail(9.49, df=4, label='χ² curve (4 d.f.) with rejection region beyond 9.49, α = 0.05'),
        'Reject $H_0$ if $\\chi_c^2\\ge\\chi^2_{\\alpha,\\nu}$ whereas from table 8.1 of $\\chi^2$ distribution, we have $\\chi^2_{\\alpha,\\nu}=\\chi^2_{0.05,(3-1)(3-1)}=\\chi^2_{0.05,4}=9.49\\ \\chi^2$',
        '$H_0$ کو رد کریں اگر $\\chi_c^2\\ge\\chi^2_{\\alpha,\\nu}$ جبکہ $\\chi^2$ تقسیم کے جدول 8.1 سے ہمارے پاس $\\chi^2_{\\alpha,\\nu}=\\chi^2_{0.05,(3-1)(3-1)}=\\chi^2_{0.05,4}=9.49\\ \\chi^2$ ہے',
        '$H_0$ رد کړئ که $\\chi_c^2\\ge\\chi^2_{\\alpha,\\nu}$ په داسې حال کې چې د $\\chi^2$ وېش له 8.1 جدول څخه لرو $\\chi^2_{\\alpha,\\nu}=\\chi^2_{0.05,(3-1)(3-1)}=\\chi^2_{0.05,4}=9.49\\ \\chi^2$', ratio=.45)
b.p('vi. Conclusion', 'vi. نتیجہ', 'vi. پایله')
b.p('Since our computed value of chi-square lies in the rejection region, therefore, we reject $H_0$ and conclude that there is association between mathematical ability and general ability.', 'چونکہ کائی مربع کی ہماری معلوم کی گئی قیمت رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں اور نتیجہ نکالتے ہیں کہ ریاضیاتی قابلیت اور عمومی قابلیت کے درمیان تلازم ہے۔', 'څرنګه چې زموږ د کای مربع محاسبه شوی قیمت د ردولو په سیمه کې پروت دی، نو $H_0$ ردوو او پایله اخلو چې د ریاضیاتي وړتیا او عمومي وړتیا ترمنځ تړاو شته.')
e84 = b.build('stat12-p145-example-8-4-end', 'Example 8.4 — critical region and conclusion', 'مثال 8.4 — فیصلہ کن علاقہ اور نتیجہ', 'بېلګه 8.4 — بحراني سیمه او پایله', 145, [281])

c = Builder()
c.h('8.2.2 Shortcut method of calculating χ² in case of (2 × 2) contingency table', '8.2.2 (2 × 2) اتفاقی جدول کی صورت میں χ² معلوم کرنے کا مختصر طریقہ', '8.2.2 د (2 × 2) احتمالي جدول په حالت کې د χ² د محاسبې لنډه طریقه')
c.p('When we have (2 × 2) contingency table having four cell frequencies as given below;', 'جب ہمارے پاس چار خانوی تعدد والا (2 × 2) اتفاقی جدول ہو جیسا کہ نیچے دیا گیا ہے؛', 'کله چې موږ د څلورو خونو تکرارونو لرونکی (2 × 2) احتمالي جدول ولرو لکه لاندې؛')
R = [['A', '$a$', '$b$', '$a+b$'], ['α', '$c$', '$d$', '$c+d$']]
c.table('stat12-t-2x2-abcd', ['Attributes', 'B', 'β', 'Total'], R + [['Total', '$a+c$', '$b+d$', '$a+b+c+d=n$']],
        ['صفات', 'B', 'β', 'میزان'], ['صفتونه', 'B', 'β', 'ټول'], R + [['میزان', '$a+c$', '$b+d$', '$a+b+c+d=n$']], R + [['ټول', '$a+c$', '$b+d$', '$a+b+c+d=n$']])
c.p('The value of $\\chi^2$ can be calculated directly without computing the expected frequencies by using the following formula', 'درج ذیل فارمولا استعمال کرتے ہوئے متوقع تعدد معلوم کیے بغیر $\\chi^2$ کی قیمت براہِ راست معلوم کی جا سکتی ہے', 'د لاندې فورمول په کارولو د تمه شویو تکرارونو له محاسبې پرته د $\\chi^2$ قیمت مستقیماً محاسبه کېدای شي')
c.eq(SHORT)
c.h('Example 8.5', 'مثال 8.5', 'بېلګه 8.5')
c.p('A random sample of 100 educated and 200 uneducated people were asked about liking and disliking of football game and the following data were recorded.', '100 تعلیم یافتہ اور 200 غیر تعلیم یافتہ لوگوں کے تصادفی نمونے سے فٹ بال کے کھیل کو پسند اور ناپسند کرنے کے بارے میں پوچھا گیا اور درج ذیل مواد ریکارڈ کیا گیا۔', 'د 100 زده‌کړو او 200 نازده‌کړو خلکو له تصادفي نمونې څخه د فوټبال لوبې د خوښولو او نه خوښولو په اړه وپوښتل شول او لاندې معلومات ثبت شول.')
c.table('stat12-t-ex8-5', ['Attributes', 'Like football', 'Dislike football', 'Total'], [['Educated', '55', '45', '100'], ['Uneducated', '125', '75', '200'], ['Total', '180', '120', '300']],
        ['صفات', 'فٹ بال پسند', 'فٹ بال ناپسند', 'میزان'], ['صفتونه', 'فوټبال خوښوي', 'فوټبال نه خوښوي', 'ټول'],
        [['تعلیم یافتہ', '55', '45', '100'], ['غیر تعلیم یافتہ', '125', '75', '200'], ['میزان', '180', '120', '300']],
        [['زده‌کړي', '55', '45', '100'], ['نازده‌کړي', '125', '75', '200'], ['ټول', '180', '120', '300']])
c.p('Test the hypothesis about independence between education and liking of football at α = 0.05', 'α = 0.05 پر تعلیم اور فٹ بال پسند کرنے کے درمیان آزادی کے بارے میں مفروضے کی جانچ کریں', 'په α = 0.05 د زده‌کړې او فوټبال خوښولو ترمنځ د خپلواکۍ په اړه فرضیه وازموئ')
c.h('Solution:', 'حل:', 'حل:')
c.group('lines', [
    ('i. $H_0$: There is no association between education and liking of football.', 'i. $H_0$: تعلیم اور فٹ بال پسند کرنے کے درمیان کوئی تلازم نہیں۔', 'i. $H_0$: د زده‌کړې او فوټبال خوښولو ترمنځ هېڅ تړاو نشته.'),
    ('$H_1$: There is association', '$H_1$: تلازم موجود ہے', '$H_1$: تړاو شته'),
    ('ii. $\\alpha=0.05$',) * 3,
    ('iii. Test statistic to be used in this case by direct method is', 'iii. اس صورت میں براہِ راست طریقے سے استعمال ہونے والا جانچ کا شماریہ یہ ہے', 'iii. په دې حالت کې د مستقیمې طریقې له لارې کارېدونکې د ازموینې احصاییه دا ده'),
])
c.eq(SHORT)
c.p('iv. Calculation', 'iv. حساب', 'iv. محاسبه')
c.vpara('stat12-ex8-5-cr', chi_tail(3.84, df=2.6, xmax=5.6, label='χ² curve (1 d.f.) with rejection region beyond 3.84, α = 0.05'),
        '$\\chi^2=\\frac{300(55\\times 75-45\\times 125)^2}{(100)(200)(180)(120)}=\\frac{675}{432}=1.5625$', '$\\chi^2=\\frac{300(55\\times 75-45\\times 125)^2}{(100)(200)(180)(120)}=\\frac{675}{432}=1.5625$', '$\\chi^2=\\frac{300(55\\times 75-45\\times 125)^2}{(100)(200)(180)(120)}=\\frac{675}{432}=1.5625$', ratio=.42)
c.p('v. Critical region', 'v. فیصلہ کن علاقہ', 'v. بحراني سیمه')
c.p('Reject $H_0$ if $\\chi_c^2\\ge\\chi^2_{0.05,(1)}=3.84$', '$H_0$ کو رد کریں اگر $\\chi_c^2\\ge\\chi^2_{0.05,(1)}=3.84$', '$H_0$ رد کړئ که $\\chi_c^2\\ge\\chi^2_{0.05,(1)}=3.84$')
c.p('vi. Conclusion.', 'vi. نتیجہ۔', 'vi. پایله.')
c.p('Since $\\chi_c^2=1.5625$ falls in the acceptance $\\chi^2$ region, therefore, we accept $H_0$.', 'چونکہ $\\chi_c^2=1.5625$ قبولیت کے $\\chi^2$ علاقے میں آتا ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں۔', 'څرنګه چې $\\chi_c^2=1.5625$ د منلو په $\\chi^2$ سیمه کې لوېږي، نو $H_0$ منو.')
c.h('8.2.3 Coefficient of contingency for (r × c) contingency table', '8.2.3 (r × c) اتفاقی جدول کے لیے اتفاقیت کا سر', '8.2.3 د (r × c) احتمالي جدول لپاره د احتمالیت ضریب')
c.p('The chi-square test-statistic only decides about the independence or association of attributes in contingency tables but when $H_0$ is rejected it does not', 'کائی مربع جانچ کا شماریہ صرف اتفاقی جدولوں میں صفات کی آزادی یا تلازم کے بارے میں فیصلہ کرتا ہے لیکن جب $H_0$ رد ہو جائے تو یہ نہیں', 'د کای مربع د ازموینې احصاییه یوازې په احتمالي جدولونو کې د صفتونو د خپلواکۍ یا تړاو په اړه پرېکړه کوي خو کله چې $H_0$ رد شي، دا نه')
sh = c.build('stat12-p145-shortcut-chi-square', '8.2.2 Shortcut χ² for 2 × 2 tables — Example 8.5; 8.2.3 start', '8.2.2 2 × 2 جدول کے لیے مختصر χ² — مثال 8.5؛ 8.2.3 کا آغاز', '8.2.2 د 2 × 2 جدول لپاره لنډ χ² — بېلګه 8.5؛ د 8.2.3 پیل', 145, [281, 282])
issues = [{'id': 'stat12-p281-stray-chi', 'unit': 8, 'printedPage': 281, 'description': 'Example 8.4 step v prints a stray “χ²” after “= 9.49”; Example 8.5 prints the shortcut result as 675/432 (scaled by 10⁶). Printed text retained.'}]

if __name__ == '__main__':
    save(145, [(8, e84), (8, sh)], issues=issues)
