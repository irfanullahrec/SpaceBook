"""PDF123 printed 237–238: 7.2 steps ii–vi (critical regions for cases a–c with figures), conclusion; Example 7.1 (two-tailed Z test)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('ii. α = 0.01 or 0.05 etc.', 'ii. α = 0.01 یا 0.05 وغیرہ۔', 'ii. α = 0.01 یا 0.05 او نور.')
b.p('iii. Test statistic to be used is $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$, which follows N(0,1) when $H_0$ is true.', 'iii. استعمال ہونے والا جانچ کا شماریہ $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$ ہے جو $H_0$ کے درست ہونے پر N(0,1) کی پیروی کرتا ہے۔', 'iii. د ازموینې کارېدونکې احصاییه $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$ ده چې کله $H_0$ سمه وي N(0,1) تعقیبوي.')
b.p('iv. Calculation of Z value from the given data.', 'iv. دیے گئے مواد سے Z کی قیمت کا حساب۔', 'iv. له ورکړل شویو معلوماتو څخه د Z قیمت محاسبه.')
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.p('The critical region depends on $H_1$.', 'فیصلہ کن علاقہ $H_1$ پر منحصر ہے۔', 'بحراني سیمه په $H_1$ پورې اړه لري.')
b.vpara('stat12-cr-case-a', tail_test('two', ticks=((-1.4, '−Zα/2'), (1.4, 'Zα/2')), label='Two-sided critical region'),
        'For case (a) two sided critical region is used as; Reject $H_0$ if $Z\\le -Z_{\\alpha/2}$ or $Z\\ge Z_{\\alpha/2}$.', 'صورت (a) کے لیے دو طرفہ فیصلہ کن علاقہ یوں استعمال ہوتا ہے؛ $H_0$ کو رد کریں اگر $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$۔', 'د (a) حالت لپاره دوه اړخیزه بحراني سیمه داسې کارول کېږي؛ $H_0$ رد کړئ که $Z\\le -Z_{\\alpha/2}$ یا $Z\\ge Z_{\\alpha/2}$.', ratio=.45)
b.vpara('stat12-cr-case-b', tail_test('left', ticks=((-1.4, '−Zα'),), label='Left-sided critical region'),
        'For case (b) one sided critical region is used as; Reject $H_0$ if $Z\\le -Z_{\\alpha}$', 'صورت (b) کے لیے یک طرفہ فیصلہ کن علاقہ یوں استعمال ہوتا ہے؛ $H_0$ کو رد کریں اگر $Z\\le -Z_{\\alpha}$', 'د (b) حالت لپاره یو اړخیزه بحراني سیمه داسې کارول کېږي؛ $H_0$ رد کړئ که $Z\\le -Z_{\\alpha}$', ratio=.45)
b.vpara('stat12-cr-case-c', tail_test('right', ticks=((1.4, 'Zα'),), label='Right-sided critical region'),
        'For Case (c) one sided critical region is used as; Reject $H_0$ if $Z\\ge Z_{\\alpha}$', 'صورت (c) کے لیے یک طرفہ فیصلہ کن علاقہ یوں استعمال ہوتا ہے؛ $H_0$ کو رد کریں اگر $Z\\ge Z_{\\alpha}$', 'د (c) حالت لپاره یو اړخیزه بحراني سیمه داسې کارول کېږي؛ $H_0$ رد کړئ که $Z\\ge Z_{\\alpha}$', ratio=.45)
b.p('Where Z is computed value of Z-test and $Z_{\\alpha/2}$ or $Z_{\\alpha}$ is table value.', 'جہاں Z جانچ کی معلوم کی گئی قیمت ہے اور $Z_{\\alpha/2}$ یا $Z_{\\alpha}$ جدول کی قیمت ہے۔', 'چې Z د Z-ازموینې محاسبه شوی قیمت او $Z_{\\alpha/2}$ یا $Z_{\\alpha}$ د جدول قیمت دی.')
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('If the computed value of Z falls in the acceptance region, accept $H_0$, otherwise reject $H_0$. Remember that acceptance of a hypothesis does not mean that it is really true. We may interpret it as that sample data is in the support of $H_0$ that is why we are accepting $H_0$.', 'اگر Z کی معلوم کی گئی قیمت قبولیت کے علاقے میں آئے تو $H_0$ قبول کریں، ورنہ $H_0$ رد کریں۔ یاد رکھیں کہ مفروضے کو قبول کرنے کا مطلب یہ نہیں کہ وہ واقعی درست ہے۔ ہم اس کی تشریح یوں کر سکتے ہیں کہ نمونے کا مواد $H_0$ کی حمایت میں ہے، اسی لیے ہم $H_0$ قبول کر رہے ہیں۔', 'که د Z محاسبه شوی قیمت د منلو په سیمه کې ولوېږي، $H_0$ ومنئ، که نه $H_0$ رد کړئ. په یاد ولرئ چې د یوې فرضیې منل دا مانا نه لري چې هغه په رښتیا سمه ده. موږ یې داسې تفسیرولای شو چې نمونوي معلومات د $H_0$ په ملاتړ کې دي له همدې امله $H_0$ منو.')
st = b.build('stat12-p123-procedure-steps', '7.2 Procedure — test statistic, critical regions for cases (a)–(c) and conclusion', '7.2 طریقہ — جانچ کا شماریہ، صورتوں (a)–(c) کے فیصلہ کن علاقے اور نتیجہ', '7.2 طریقه — د ازموینې احصاییه، د (a)–(c) حالتونو بحراني سیمې او پایله', 123, [237, 238])

c = Builder()
c.h('Example 7.1', 'مثال 7.1', 'بېلګه 7.1')
c.p('An electrical firm manufactures light bulbs that have a length of life that is approximately normally distributed with a mean of 812 hours and a standard deviation of 40 hours. Test the hypothesis that μ = 812 hours against the alternative μ ≠ 812 hours if a random sample of 36 bulbs has an average life of 800 hours. Use a 5% level of significance.', 'ایک برقی کمپنی ایسے بلب بناتی ہے جن کی عمر تقریباً نارمل تقسیم شدہ ہے جس کا اوسط 812 گھنٹے اور معیاری انحراف 40 گھنٹے ہے۔ اگر 36 بلبوں کے تصادفی نمونے کی اوسط عمر 800 گھنٹے ہو تو متبادل μ ≠ 812 گھنٹے کے مقابلے میں مفروضے μ = 812 گھنٹے کی جانچ کریں۔ 5% معنویت کی سطح استعمال کریں۔', 'یوه برېښنايي شرکت داسې ګروپونه جوړوي چې عمر یې نږدې نورمال وېش لري او منځنی یې 812 ساعته او معیاري انحراف یې 40 ساعته دی. که د 36 ګروپونو تصادفي نمونه منځنی عمر 800 ساعته ولري، د بدیل μ ≠ 812 ساعته پر وړاندې د μ = 812 ساعته فرضیه وازموئ. د 5% د معنی‌داریت کچه وکاروئ.')
c.h(*SOL)
c.group('lines', [
    ('i. Null hypothesis $H_0:\\mu=812$', 'i. صفری مفروضہ $H_0:\\mu=812$', 'i. صفري فرضیه $H_0:\\mu=812$'),
    ('Alternative hypothesis $H_1:\\mu\\neq 812$', 'متبادل مفروضہ $H_1:\\mu\\neq 812$', 'بدیله فرضیه $H_1:\\mu\\neq 812$'),
    ('ii. Significance level α = 0.05', 'ii. معنویت کی سطح α = 0.05', 'ii. د معنی‌داریت کچه α = 0.05'),
    ('iii. Test statistic to be used here is; $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$', 'iii. یہاں استعمال ہونے والا جانچ کا شماریہ یہ ہے؛ $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$', 'iii. دلته کارېدونکې د ازموینې احصاییه دا ده؛ $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$'),
    ('iv. Calculation: Given n = 36, $\\overline{X}=800$, σ = 40', 'iv. حساب: دیا گیا ہے n = 36، $\\overline{X}=800$، σ = 40', 'iv. محاسبه: ورکړل شوي n = 36، $\\overline{X}=800$، σ = 40'),
])
c.eq(r'\text{Hence } Z=\frac{800-812}{40/\sqrt{36}}=\frac{-12}{40/6}=\frac{-12\times 6}{40}=-1.8')
c.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
c.p('Here the test is two sided, so α/2 = 0.025 Now 0.5 − 0.025 = 0.4750 search this value in the body of the area table of standard normal distribution which correspond to $Z_{\\alpha/2}=Z_{0.05}=1.96$.', 'یہاں جانچ دو طرفہ ہے، لہٰذا α/2 = 0.025۔ اب 0.5 − 0.025 = 0.4750؛ یہ قیمت معیاری نارمل تقسیم کے رقبے کے جدول کے متن میں تلاش کریں جو $Z_{\\alpha/2}=Z_{0.05}=1.96$ کے مطابق ہے۔', 'دلته ازموینه دوه اړخیزه ده، نو α/2 = 0.025. اوس 0.5 − 0.025 = 0.4750؛ دا قیمت د معیاري نورمال وېش د مساحت د جدول په متن کې ولټوئ چې له $Z_{\\alpha/2}=Z_{0.05}=1.96$ سره سمون لري.')
c.vpara('stat12-ex7-1-cr', tail_test('two', z=1.96, mid='', ticks=((-1.96, '−1.96'), (0, '0'), (1.96, '1.96')), label='Two-sided critical region at ±1.96'),
        'Thus reject $H_0$ if Z ≤ − 1.96 or Z ≥ 1.96.', 'لہٰذا $H_0$ کو رد کریں اگر Z ≤ − 1.96 یا Z ≥ 1.96۔', 'نو $H_0$ رد کړئ که Z ≤ − 1.96 یا Z ≥ 1.96.', ratio=.45)
ex = c.build('stat12-p123-example-7-1', 'Example 7.1 — two-tailed Z test for a mean', 'مثال 7.1 — اوسط کے لیے دو طرفہ Z جانچ', 'بېلګه 7.1 — د منځني لپاره دوه لوري Z ازموینه', 123, [238])
issues = [{'id': 'stat12-p238-z005', 'unit': 7, 'printedPage': 238, 'description': 'Example 7.1 writes Z_{α/2} = Z_{0.05} = 1.96 (should be Z_{0.025}); printed notation retained.'}]

if __name__ == '__main__':
    save(123, [(7, st), (7, ex)], issues=issues)
