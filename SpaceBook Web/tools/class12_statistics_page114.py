"""PDF114 printed 219–220: Example 6.14 result; 6.3.8 small-sample CI for μ1−μ2 (pooled t); Example 6.15 setup."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
D = r'\overline{X}_1-\overline{X}_2'
b = Builder()
b.mlines([r'1-\alpha=0.95,\ \alpha=0.05,\ \frac{\alpha}{2}=0.025'])
b.p('From area table of normal distribution, we have $Z_{\\alpha/2}=Z_{0.025}=1.96$', 'نارمل تقسیم کے رقبے کے جدول سے ہمارے پاس $Z_{\\alpha/2}=Z_{0.025}=1.96$ ہے', 'د نورمال وېش د مساحت له جدول څخه لرو $Z_{\\alpha/2}=Z_{0.025}=1.96$')
b.p('Hence the 95% confidence interval for $(\\mu_1-\\mu_2)$ is:', 'لہٰذا $(\\mu_1-\\mu_2)$ کے لیے 95% اعتماد کا وقفہ یہ ہے:', 'نو د $(\\mu_1-\\mu_2)$ لپاره 95% د باور واټن دا دی:')
b.mlines([r'(75-73)\pm 1.96\sqrt{\frac{64}{60}+\frac{100}{100}}', r'2\pm 1.96\,(1.44)', r'2\pm 2.8224', r'(-0.8224,\ 4.8224)'])
ex14 = b.build('stat12-p114-example-6-14', 'Example 6.14 — result', 'مثال 6.14 — نتیجہ', 'بېلګه 6.14 — پایله', 114, [219])

c = Builder()
c.h('6.3.8 Confidence interval estimate for the difference between two normal populations means (μ₁ − μ₂) when σ₁², σ₂² are unknown (small sample case)', '6.3.8 جب σ₁²، σ₂² نامعلوم ہوں تو دو نارمل آبادیوں کے اوسطوں کے فرق (μ₁ − μ₂) کا اعتماد کا وقفہ (چھوٹے نمونے کی صورت)', '6.3.8 کله چې σ₁²، σ₂² نامعلوم وي د دوو نورمال نفوسونو د منځنیو د توپیر (μ₁ − μ₂) د باور واټن اټکل (د کوچنۍ نمونې حالت)')
c.p(f'When population variances are not given and $n_1,n_2$ are small (< 30) then we have to make another assumption i.e. $\\sigma_1=\\sigma_2=\\sigma$ and this σ is estimated by unbiased pooled estimator. In this case the statistic ${D}$ has the t-distribution with $(n_1+n_2-2)$ degrees of freedom given below;', f'جب آبادیوں کے تغیرات نہ دیے گئے ہوں اور $n_1,n_2$ چھوٹے (< 30) ہوں تو ہمیں ایک اور مفروضہ لینا ہوگا یعنی $\\sigma_1=\\sigma_2=\\sigma$ اور اس σ کا تخمین غیر جانبدار مشترکہ تخمین کار سے لگایا جاتا ہے۔ اس صورت میں شماریہ ${D}$ کی t-تقسیم $(n_1+n_2-2)$ درجاتِ آزادی کے ساتھ ہے جو نیچے دی گئی ہے؛', f'کله چې د نفوسونو واریانسونه نه وي ورکړل شوي او $n_1,n_2$ کوچني (< 30) وي، نو باید بله فرضیه وکړو یعنې $\\sigma_1=\\sigma_2=\\sigma$ او دا σ د بې‌پلوه ګډ اټکلوونکي په واسطه اټکل کېږي. په دې حالت کې د ${D}$ احصاییه د $(n_1+n_2-2)$ د ازادۍ درجو سره t-وېش لري چې لاندې ورکړل شوی؛')
c.eq(rf't=\frac{{({D})-(\mu_1-\mu_2)}}{{s_p\sqrt{{\frac{{1}}{{n_1}}+\frac{{1}}{{n_2}}}}}}')
c.p('where $s_p=\\sqrt{\\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}$', 'جہاں $s_p=\\sqrt{\\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}$', 'چې $s_p=\\sqrt{\\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}$')
c.p('A 100(1−α)% confidence interval for $(\\mu_1-\\mu_2)$ in this case is given by', 'اس صورت میں $(\\mu_1-\\mu_2)$ کے لیے 100(1−α)% اعتماد کا وقفہ یہ ہے', 'په دې حالت کې د $(\\mu_1-\\mu_2)$ لپاره 100(1−α)% د باور واټن دا دی')
c.eq(rf'({D})\pm t_{{\alpha/2,(n_1+n_2-2)}}\,s_p\sqrt{{\frac{{1}}{{n_1}}+\frac{{1}}{{n_2}}}}')
c.h('Example 6.15', 'مثال 6.15', 'بېلګه 6.15')
c.p('The following two samples were randomly selected from two normal populations for which $\\sigma_1^2=\\sigma_2^2$ but unknown.', 'درج ذیل دو نمونے دو نارمل آبادیوں سے تصادفی طور پر منتخب کیے گئے جن کے لیے $\\sigma_1^2=\\sigma_2^2$ لیکن نامعلوم ہیں۔', 'لاندې دوه نمونې له دوو نورمال نفوسونو څخه په تصادفي ډول ټاکل شوې چې د هغو لپاره $\\sigma_1^2=\\sigma_2^2$ خو نامعلوم دي.')
c.table('stat12-t-ex6-15', ['', '', '', '', '', '', '', ''], [['Sample-I', '103', '94', '110', '87', '98', '', ''], ['Sample-II', '97', '82', '123', '92', '175', '88', '118']], [''] * 8, [''] * 8,
        [['نمونہ-I', '103', '94', '110', '87', '98', '', ''], ['نمونہ-II', '97', '82', '123', '92', '175', '88', '118']], [['نمونه-I', '103', '94', '110', '87', '98', '', ''], ['نمونه-II', '97', '82', '123', '92', '175', '88', '118']], noHeader=True)
c.p('Compute 90% confidence interval for the difference between the two population means.', 'دونوں آبادیوں کے اوسطوں کے فرق کے لیے 90% اعتماد کا وقفہ معلوم کریں۔', 'د دوو نفوسونو د منځنیو د توپیر لپاره 90% د باور واټن محاسبه کړئ.')
c.h(*SOL)
c.p('100(1−α)% confidence Interval for $(\\mu_1-\\mu_2)$ in this case is', 'اس صورت میں $(\\mu_1-\\mu_2)$ کے لیے 100(1−α)% اعتماد کا وقفہ یہ ہے', 'په دې حالت کې د $(\\mu_1-\\mu_2)$ لپاره 100(1−α)% د باور واټن دا دی')
c.eq(r'(\overline{x}_1-\overline{x}_2)\pm t_{\alpha/2,(n_1+n_2-2)}\,s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}')
c.p('Given that', 'دیا گیا ہے', 'ورکړل شوي')
c.mlines([r'n_1=5,\ \Sigma x_1=492,\ \Sigma x_1^2=48718', r'n_2=7,\ \Sigma x_2=775,\ \Sigma x_2^2=92019', r'\text{Now } \overline{x}_1=\frac{\Sigma x_1}{n_1}=\frac{492}{5}=98.4', r'\overline{x}_2=\frac{\Sigma x_2}{n_2}=\frac{775}{7}=110.71',
          r'(n_1-1)s_1^2=\Sigma(x_1-\overline{x}_1)^2=\Sigma x_1^2-\frac{(\Sigma x_1)^2}{n_1}=48718-\frac{(492)^2}{5}=305.2', r'(n_2-1)s_2^2=\Sigma(x_2-\overline{x}_2)^2=\Sigma x_2^2-\frac{(\Sigma x_2)^2}{n_2}=92019-\frac{(775)^2}{7}=6215.4286', r's_p=\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}'])
sm = c.build('stat12-p114-pooled-t-interval', '6.3.8 Small-sample CI for μ₁ − μ₂ (pooled t) — Example 6.15', '6.3.8 چھوٹے نمونے کا μ₁ − μ₂ کا اعتماد کا وقفہ (مشترکہ t) — مثال 6.15', '6.3.8 د کوچنۍ نمونې د μ₁ − μ₂ د باور واټن (ګډ t) — بېلګه 6.15', 114, [219, 220])

if __name__ == '__main__':
    save(114, [(6, ex14), (6, sm)])
