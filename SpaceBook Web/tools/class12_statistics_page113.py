"""PDF113 printed 217–218: Example 6.13 (tires, σ known), 6.3.7 CI for μ1−μ2 when σ unknown (large samples), Example 6.14 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
D = r'\overline{X}_1-\overline{X}_2'
b = Builder()
b.h('Example 6.13', 'مثال 6.13', 'بېلګه 6.13')
b.p('The wearing qualities of two types of automobile tires were compared by road – testing samples of $n_1=n_2=100$ tires of each type. The test results are $\\overline{x}_1=26400$ miles and $\\overline{x}_2=25100$ miles. The standard deviations for the two types of populations are $\\sigma_1=37.9473$ and $\\sigma_2=44.2719$ respectively. Estimate $(\\mu_1-\\mu_2)$, the difference in mean miles to wear out, using a 99% confidence interval.',
    'گاڑیوں کے دو قسم کے ٹائروں کی گھساؤ کی خصوصیات کا موازنہ ہر قسم کے $n_1=n_2=100$ ٹائروں کے نمونوں کی سڑک پر جانچ سے کیا گیا۔ جانچ کے نتائج $\\overline{x}_1=26400$ میل اور $\\overline{x}_2=25100$ میل ہیں۔ دونوں قسم کی آبادیوں کے معیاری انحراف بالترتیب $\\sigma_1=37.9473$ اور $\\sigma_2=44.2719$ ہیں۔ 99% اعتماد کے وقفے کی مدد سے $(\\mu_1-\\mu_2)$، یعنی گھس جانے تک اوسط میلوں کے فرق کا تخمین لگائیں۔',
    'د موټرو د دوو ډوله ټایرونو د خوړل کېدو ځانګړنې د هر ډول د $n_1=n_2=100$ ټایرونو د نمونو په سړک ازمویلو سره پرتله شوې. د ازموینې پایلې $\\overline{x}_1=26400$ میله او $\\overline{x}_2=25100$ میله دي. د دواړو ډولونو د نفوسونو معیاري انحرافونه په ترتیب سره $\\sigma_1=37.9473$ او $\\sigma_2=44.2719$ دي. د 99% د باور واټن په کارولو سره $(\\mu_1-\\mu_2)$، یعنې تر خوړل کېدو پورې د منځنیو میلونو توپیر، اټکل کړئ.')
b.h(*SOL)
b.p('The 100(1−α)% confidence interval for $(\\mu_1-\\mu_2)$ in this case is given by', 'اس صورت میں $(\\mu_1-\\mu_2)$ کے لیے 100(1−α)% اعتماد کا وقفہ یہ ہے', 'په دې حالت کې د $(\\mu_1-\\mu_2)$ لپاره 100(1−α)% د باور واټن دا دی')
b.eq(rf'({D})\pm Z_{{\alpha/2}}\sqrt{{\frac{{\sigma_1^2}}{{n_1}}+\frac{{\sigma_2^2}}{{n_2}}}}')
b.table('stat12-t-ex6-13-given', ['Given', '', '', ''], [['$n_1=100$', '$\\overline{x}_1=26400$', '$\\sigma_1=37.9473$', '$\\sigma_1^2=1440$'], ['$n_2=100$', '$\\overline{x}_2=25100$', '$\\sigma_2=44.2719$', '$\\sigma_2^2=1960$'], ['$1-\\alpha=0.99$', '$\\alpha=0.01$', '$\\frac{\\alpha}{2}=0.005$', '']],
        ['دیا گیا', '', '', ''], ['ورکړل شوي', '', '', ''])
b.p('Hence $z_{\\alpha/2}=2.57$', 'لہٰذا $z_{\\alpha/2}=2.57$', 'نو $z_{\\alpha/2}=2.57$')
b.p('Putting values in the expression, we have 99% confidence interval for $(\\mu_1-\\mu_2)$ as;', 'اظہاریے میں قیمتیں رکھنے سے $(\\mu_1-\\mu_2)$ کے لیے 99% اعتماد کا وقفہ یہ ہے؛', 'په افاده کې قیمتونه ایښودو سره د $(\\mu_1-\\mu_2)$ لپاره 99% د باور واټن دا دی؛')
b.mlines([r'(26400-25100)\pm 2.57\sqrt{\frac{1440}{100}+\frac{1960}{100}}', r'1300\pm 2.57(5.831)', r'\text{or } [1285.014<(\mu_1-\mu_2)<1314.986]'])
ex13 = b.build('stat12-p113-example-6-13', 'Example 6.13 — difference of mean tire life (σ known)', 'مثال 6.13 — ٹائر کی اوسط عمر کا فرق (σ معلوم)', 'بېلګه 6.13 — د ټایر د منځني عمر توپیر (σ معلوم)', 113, [217])

c = Builder()
c.h('6.3.7 Confidence interval for (μ₁ − μ₂) when σ₁ and σ₂ are unknown (large sample case)', '6.3.7 جب σ₁ اور σ₂ نامعلوم ہوں تو (μ₁ − μ₂) کا اعتماد کا وقفہ (بڑے نمونے کی صورت)', '6.3.7 کله چې σ₁ او σ₂ نامعلوم وي د (μ₁ − μ₂) د باور واټن (د لویې نمونې حالت)')
c.p('When population variances are unknown but sample sizes $n_1$ and $n_2$ are large (≥30) then $\\sigma_1^2,\\sigma_2^2$ are estimated by sample variances $S_1^2,S_2^2$ respectively. The statistic Z in this case will be of the form', 'جب آبادیوں کے تغیرات نامعلوم ہوں لیکن نمونوں کے سائز $n_1$ اور $n_2$ بڑے (≥30) ہوں تو $\\sigma_1^2,\\sigma_2^2$ کا تخمین بالترتیب نمونوں کے تغیرات $S_1^2,S_2^2$ سے لگایا جاتا ہے۔ اس صورت میں شماریہ Z کی شکل یہ ہوگی', 'کله چې د نفوسونو واریانسونه نامعلوم وي خو د نمونو اندازې $n_1$ او $n_2$ لویې (≥30) وي، نو $\\sigma_1^2,\\sigma_2^2$ په ترتیب سره د نمونو په واریانسونو $S_1^2,S_2^2$ اټکل کېږي. په دې حالت کې د Z احصاییه به دا بڼه ولري')
c.eq(rf'Z=\frac{{({D})-(\mu_1-\mu_2)}}{{\sqrt{{\frac{{S_1^2}}{{n_1}}+\frac{{S_2^2}}{{n_2}}}}}}')
c.p('The 100 (1−α)% confidence interval for $(\\mu_1-\\mu_2)$ is then', 'پھر $(\\mu_1-\\mu_2)$ کے لیے 100 (1−α)% اعتماد کا وقفہ یہ ہے', 'بیا د $(\\mu_1-\\mu_2)$ لپاره 100 (1−α)% د باور واټن دا دی')
c.eq(rf'({D})\pm Z_{{\alpha/2}}\sqrt{{\frac{{S_1^2}}{{n_1}}+\frac{{S_2^2}}{{n_2}}}}')
c.h('Example 6.14', 'مثال 6.14', 'بېلګه 6.14')
c.p('Intelligence test of two groups of boys and girls gave the following results:', 'لڑکوں اور لڑکیوں کے دو گروہوں کے ذہانت کے امتحان نے درج ذیل نتائج دیے:', 'د هلکانو او نجونو د دوو ډلو د هوښیارۍ ازموینې لاندې پایلې ورکړې:')
c.table('stat12-t-ex6-14', ['', '', '', ''], [['Girls:', '$n_1=60$', 'mean = 75', 'S.D = 8'], ['Boys:', '$n_2=100$', 'mean = 73', 'S.D = 10']], ['', '', '', ''], ['', '', '', ''],
        [['لڑکیاں:', '$n_1=60$', 'اوسط = 75', 'S.D = 8'], ['لڑکے:', '$n_2=100$', 'اوسط = 73', 'S.D = 10']], [['نجونې:', '$n_1=60$', 'منځنی = 75', 'S.D = 8'], ['هلکان:', '$n_2=100$', 'منځنی = 73', 'S.D = 10']], noHeader=True)
c.p('Compute a 95% confidence interval for $(\\mu_1-\\mu_2)$ where $\\mu_1$ is the mean score of girls and $\\mu_2$ is the mean score of boys in respective populations.', 'متعلقہ آبادیوں میں $(\\mu_1-\\mu_2)$ کے لیے 95% اعتماد کا وقفہ معلوم کریں جہاں $\\mu_1$ لڑکیوں کا اوسط اسکور اور $\\mu_2$ لڑکوں کا اوسط اسکور ہے۔', 'په اړوندو نفوسونو کې د $(\\mu_1-\\mu_2)$ لپاره 95% د باور واټن محاسبه کړئ چې $\\mu_1$ د نجونو منځنۍ نمره او $\\mu_2$ د هلکانو منځنۍ نمره ده.')
c.h(*SOL)
c.p('Here $\\sigma_1,\\sigma_2$ are not given but $n_1,n_2$ are large, so 100(1−α)% confidence interval for $(\\mu_1-\\mu_2)$ in this case is', 'یہاں $\\sigma_1,\\sigma_2$ نہیں دیے گئے لیکن $n_1,n_2$ بڑے ہیں، لہٰذا اس صورت میں $(\\mu_1-\\mu_2)$ کے لیے 100(1−α)% اعتماد کا وقفہ یہ ہے', 'دلته $\\sigma_1,\\sigma_2$ نه دي ورکړل شوي خو $n_1,n_2$ لوی دي، نو په دې حالت کې د $(\\mu_1-\\mu_2)$ لپاره 100(1−α)% د باور واټن دا دی')
c.eq(rf'({D})\pm Z_{{\alpha/2}}\sqrt{{\frac{{S_1^2}}{{n_1}}+\frac{{S_2^2}}{{n_2}}}}')
c.mlines([r'\text{We have } n_1=60,\ \overline{x}_1=75,\ S_1=8', r'n_2=100,\ \overline{x}_2=73,\ S_2=10'])
un = c.build('stat12-p113-ci-diff-unknown', '6.3.7 CI for μ₁ − μ₂ (σ unknown, large samples) — Example 6.14', '6.3.7 μ₁ − μ₂ کا اعتماد کا وقفہ (σ نامعلوم، بڑے نمونے) — مثال 6.14', '6.3.7 د μ₁ − μ₂ د باور واټن (σ نامعلوم، لویې نمونې) — بېلګه 6.14', 113, [218])
issues = [{'id': 'stat12-p217-z-257', 'unit': 6, 'printedPage': 217, 'description': 'Example 6.13 uses z(α/2) = 2.57 for 99% (table gives 2.576/2.58); printed value retained.'}]

if __name__ == '__main__':
    save(113, [(6, ex13), (6, un)], issues=issues)
