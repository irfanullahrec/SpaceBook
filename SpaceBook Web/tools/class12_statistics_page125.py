"""PDF125 printed 241–242: Example 7.3 end; 7.2.1 large-sample test for μ (σ unknown); Example 7.4; 7.2.2 small-sample t test (forms, three t figures)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('Hence reject $H_0$ if Z ≥ 1.645.', 'لہٰذا $H_0$ کو رد کریں اگر Z ≥ 1.645۔', 'نو $H_0$ رد کړئ که Z ≥ 1.645.')
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('We see that Z = 2.51 lies in the rejection region, so we reject $H_0$ and conclude that the average score has increased.', 'ہم دیکھتے ہیں کہ Z = 2.51 رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں اور نتیجہ نکالتے ہیں کہ اوسط اسکور بڑھ گیا ہے۔', 'وینو چې Z = 2.51 د ردولو په سیمه کې پروت دی، نو $H_0$ ردوو او پایله اخلو چې منځنۍ نمره زیاته شوې.')
e73 = b.build('stat12-p125-example-7-3-end', 'Example 7.3 — conclusion', 'مثال 7.3 — نتیجہ', 'بېلګه 7.3 — پایله', 125, [241])

c = Builder()
c.h('7.2.1 Procedure for hypothesis testing about μ when σ is unknown [large sample]', '7.2.1 جب σ نامعلوم ہو تو μ کے بارے میں مفروضے کی جانچ کا طریقہ [بڑا نمونہ]', '7.2.1 کله چې σ نامعلوم وي د μ په اړه د فرضیې د ازموینې طریقه [لویه نمونه]')
c.p('When σ is unknown but n ≥ 30, then central limit theorem allows us to consider sampling distribution of $\\overline{x}$ as approximately normal with mean μ and $S.E=\\frac{S}{\\sqrt{n}}$. Hence the test statistic is $Z=\\frac{\\overline{X}-\\mu}{S/\\sqrt{n}}$ i.e. only σ is replaced by S. All other steps of hypothesis testing procedure are exactly the same as when σ² is known.', 'جب σ نامعلوم ہو لیکن n ≥ 30 ہو تو مرکزی حدی مسئلہ ہمیں اجازت دیتا ہے کہ $\\overline{x}$ کی نمونہ جاتی تقسیم کو تقریباً نارمل سمجھیں جس کا اوسط μ اور $S.E=\\frac{S}{\\sqrt{n}}$ ہو۔ لہٰذا جانچ کا شماریہ $Z=\\frac{\\overline{X}-\\mu}{S/\\sqrt{n}}$ ہے یعنی صرف σ کو S سے بدل دیا جاتا ہے۔ مفروضے کی جانچ کے باقی تمام مراحل بالکل وہی ہیں جو σ² معلوم ہونے کی صورت میں ہیں۔', 'کله چې σ نامعلوم وي خو n ≥ 30 وي، نو د مرکزي حد قضیه موږ ته اجازه راکوي چې د $\\overline{x}$ نمونوي وېش نږدې نورمال وګڼو چې منځنی یې μ او $S.E=\\frac{S}{\\sqrt{n}}$ وي. نو د ازموینې احصاییه $Z=\\frac{\\overline{X}-\\mu}{S/\\sqrt{n}}$ ده یعنې یوازې σ په S بدلېږي. د فرضیې د ازموینې نور ټول پړاوونه دقیقاً هماغه دي لکه کله چې σ² معلوم وي.')
c.h('Example 7.4', 'مثال 7.4', 'بېلګه 7.4')
c.p('The daily yield for a local chemical plant has average 880 tons for the last several years. The quality control manager would like to know whether this average has changed in recent months. She randomly selects 50 days from the computer database and computes the average and standard deviation of the n = 50 yields as $\\overline{X}=871$ tons and S = 21 tons respectively. Test the appropriate hypothesis using α = 0.05',
    'ایک مقامی کیمیائی کارخانے کی یومیہ پیداوار گزشتہ کئی سالوں سے اوسطاً 880 ٹن ہے۔ کوالٹی کنٹرول مینیجر جاننا چاہتی ہے کہ کیا حالیہ مہینوں میں یہ اوسط بدل گیا ہے۔ وہ کمپیوٹر ڈیٹا بیس سے تصادفی طور پر 50 دن منتخب کرتی ہے اور n = 50 پیداواروں کا اوسط اور معیاری انحراف بالترتیب $\\overline{X}=871$ ٹن اور S = 21 ٹن معلوم کرتی ہے۔ α = 0.05 استعمال کرتے ہوئے مناسب مفروضے کی جانچ کریں۔',
    'د یوې محلي کیمیاوي فابریکې ورځنی تولید د تېرو څو کلونو لپاره منځنی 880 ټنه دی. د کیفیت کنټرول مدیره غواړي پوه شي چې آیا دا منځنی په وروستیو میاشتو کې بدل شوی. هغه له کمپیوټري ډېټابېس څخه په تصادفي ډول 50 ورځې ټاکي او د n = 50 تولیداتو منځنی او معیاري انحراف په ترتیب سره $\\overline{X}=871$ ټنه او S = 21 ټنه محاسبه کوي. د α = 0.05 په کارولو سره مناسبه فرضیه وازموئ.')
c.h(*SOL)
c.group('lines', [
    ('i. $H_0:\\mu=880$ versus $H_1:\\mu\\neq 880$', 'i. $H_0:\\mu=880$ بمقابلہ $H_1:\\mu\\neq 880$', 'i. $H_0:\\mu=880$ د $H_1:\\mu\\neq 880$ پر وړاندې'),
    ('ii. α = 0.05',) * 3,
    ('iii. Test statistic:', 'iii. جانچ کا شماریہ:', 'iii. د ازموینې احصاییه:'),
    ('Here σ is not known but n = 50 is large, so we use $Z=\\frac{\\overline{X}-\\mu}{S/\\sqrt{n}}$ as test statistic for μ.', 'یہاں σ معلوم نہیں لیکن n = 50 بڑا ہے، لہٰذا ہم μ کے لیے جانچ کے شماریے کے طور پر $Z=\\frac{\\overline{X}-\\mu}{S/\\sqrt{n}}$ استعمال کرتے ہیں۔', 'دلته σ معلوم نه دی خو n = 50 لوی دی، نو د μ لپاره د ازموینې د احصاییې په توګه $Z=\\frac{\\overline{X}-\\mu}{S/\\sqrt{n}}$ کاروو.'),
    ('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:'),
])
c.eq(r'Z=\frac{871-880}{21/\sqrt{50}}=-3.03')
c.p('v. Rejection region:', 'v. رد کا علاقہ:', 'v. د ردولو سیمه:')
c.vpara('stat12-ex7-4-cr', tail_test('two', z=1.96, mid='', ticks=((-1.96, '−1.96'), (0, '0'), (1.96, '1.96')), label='Two-sided rejection region at ±1.96'),
        'For two-tailed test we use α/2 = 0.025 so 0.5 − 0.025 = 0.4750 which corresponds to $Z_{\\alpha/2}=1.96$ in the area table of S.N.D. We will reject if Z ≤ − 1.96 or Z ≥ 1.96',
        'دو طرفہ جانچ کے لیے ہم α/2 = 0.025 استعمال کرتے ہیں لہٰذا 0.5 − 0.025 = 0.4750 جو S.N.D کے رقبے کے جدول میں $Z_{\\alpha/2}=1.96$ کے مطابق ہے۔ ہم رد کریں گے اگر Z ≤ − 1.96 یا Z ≥ 1.96',
        'د دوه لوري ازموینې لپاره α/2 = 0.025 کاروو نو 0.5 − 0.025 = 0.4750 چې د S.N.D د مساحت په جدول کې له $Z_{\\alpha/2}=1.96$ سره سمون لري. رد به یې کړو که Z ≤ − 1.96 یا Z ≥ 1.96', ratio=.45)
c.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
c.p('Since Z = −3.03 falls in the rejection region, therefore, we reject $H_0$.', 'چونکہ Z = −3.03 رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں۔', 'څرنګه چې Z = −3.03 د ردولو په سیمه کې لوېږي، نو $H_0$ ردوو.')
e74 = c.build('stat12-p125-example-7-4', '7.2.1 Large-sample test for μ (σ unknown) — Example 7.4', '7.2.1 μ کے لیے بڑے نمونے کی جانچ (σ نامعلوم) — مثال 7.4', '7.2.1 د μ لپاره د لویې نمونې ازموینه (σ نامعلوم) — بېلګه 7.4', 125, [241, 242])

d = Builder()
d.h('7.2.2 Procedure for hypothesis testing about μ when σ is unknown [small sample]', '7.2.2 جب σ نامعلوم ہو تو μ کے بارے میں مفروضے کی جانچ کا طریقہ [چھوٹا نمونہ]', '7.2.2 کله چې σ نامعلوم وي د μ په اړه د فرضیې د ازموینې طریقه [کوچنۍ نمونه]')
d.vpara('stat12-t-two', tail_test('two', ticks=((-1.4, '−tα/2,ν'), (1.4, 'tα/2,ν')), label='Two-tailed t test'),
        'i. a) $H_0:\\mu=\\mu_0$ versus $H_1:\\mu\\neq\\mu_0$ b) $H_0:\\mu\\le\\mu_0$ versus $H_1:\\mu>\\mu_0$ c) $H_0:\\mu\\ge\\mu_0$ versus $H_1:\\mu<\\mu_0$',
        'i. a) $H_0:\\mu=\\mu_0$ بمقابلہ $H_1:\\mu\\neq\\mu_0$ b) $H_0:\\mu\\le\\mu_0$ بمقابلہ $H_1:\\mu>\\mu_0$ c) $H_0:\\mu\\ge\\mu_0$ بمقابلہ $H_1:\\mu<\\mu_0$',
        'i. a) $H_0:\\mu=\\mu_0$ د $H_1:\\mu\\neq\\mu_0$ پر وړاندې b) $H_0:\\mu\\le\\mu_0$ د $H_1:\\mu>\\mu_0$ پر وړاندې c) $H_0:\\mu\\ge\\mu_0$ د $H_1:\\mu<\\mu_0$ پر وړاندې', ratio=.45)
d.vpara('stat12-t-right', tail_test('right', ticks=((1.4, 'tα,ν'),), label='Right-tailed t test'),
        'ii. Choose α = 0.01 or 0.05 etc.', 'ii. α = 0.01 یا 0.05 وغیرہ منتخب کریں۔', 'ii. α = 0.01 یا 0.05 او نور وټاکئ.', ratio=.45)
d.vpara('stat12-t-left', tail_test('left', ticks=((-1.4, '−tα,ν'),), label='Left-tailed t test'),
        'iii. Test statistic: When σ is unknown and n < 30, then test statistic to be used for μ is $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ which has t-distribution with ν = n − 1 degrees of freedom,',
        'iii. جانچ کا شماریہ: جب σ نامعلوم ہو اور n < 30 ہو تو μ کے لیے استعمال ہونے والا جانچ کا شماریہ $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ ہے جس کی t-تقسیم ν = n − 1 درجاتِ آزادی کے ساتھ ہے،',
        'iii. د ازموینې احصاییه: کله چې σ نامعلوم وي او n < 30 وي، نو د μ لپاره کارېدونکې د ازموینې احصاییه $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ ده چې د ν = n − 1 د ازادۍ درجو سره t-وېش لري،', ratio=.45)
t22 = d.build('stat12-p125-small-sample-t', '7.2.2 Small-sample t test for μ — hypotheses and critical regions', '7.2.2 μ کے لیے چھوٹے نمونے کی t جانچ — مفروضے اور فیصلہ کن علاقے', '7.2.2 د μ لپاره د کوچنۍ نمونې t ازموینه — فرضیې او بحراني سیمې', 125, [242])

if __name__ == '__main__':
    save(125, [(7, e73), (7, e74), (7, t22)])
