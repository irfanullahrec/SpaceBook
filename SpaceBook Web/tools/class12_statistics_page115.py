"""PDF115 printed 221–222: Example 6.15 result; 6.3.9 CI for p (large sample); Example 6.16; 6.3.10 CI for p1 − p2."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
DP = r'\hat{p}_1-\hat{p}_2'
b = Builder()
b.mlines([r'=\sqrt{\frac{305.2+6215.4286}{5+7-2}}=\sqrt{\frac{6520.6286}{10}}=25.54', r'\text{Here } 1-\alpha=0.90,\ \alpha=0.10'])
b.p('From t − table 6.1 we have $t_{\\alpha/2,(n_1+n_2-2)}=t_{0.10/2,(5+7-2)}=t_{0.05,(10)}=1.812$', 't − جدول 6.1 سے ہمارے پاس $t_{\\alpha/2,(n_1+n_2-2)}=t_{0.10/2,(5+7-2)}=t_{0.05,(10)}=1.812$ ہے', 'له t − جدول 6.1 څخه لرو $t_{\\alpha/2,(n_1+n_2-2)}=t_{0.10/2,(5+7-2)}=t_{0.05,(10)}=1.812$')
b.p('Hence 90% confidence Interval for $(\\mu_1-\\mu_2)$ is', 'لہٰذا $(\\mu_1-\\mu_2)$ کے لیے 90% اعتماد کا وقفہ یہ ہے', 'نو د $(\\mu_1-\\mu_2)$ لپاره 90% د باور واټن دا دی')
b.mlines([r'(98.4-110.71)\pm 1.812(25.54)\sqrt{\frac{1}{5}+\frac{1}{7}}', r'-12.31\pm 27.10', r'[-39\ 41<\mu_1-\mu_2<14.79]'])
ex15 = b.build('stat12-p115-example-6-15', 'Example 6.15 — result', 'مثال 6.15 — نتیجہ', 'بېلګه 6.15 — پایله', 115, [221])
issues = [{'id': 'stat12-p221-39-41', 'unit': 6, 'printedPage': 221, 'description': 'Example 6.15 prints the lower limit as “−39 41” (decimal point missing; −39.41); printed form retained.'}]

c = Builder()
c.h('6.3.9 Confidence interval estimate for population proportion p (large sample case)', '6.3.9 آبادی کے تناسب p کا اعتماد کا وقفہ (بڑے نمونے کی صورت)', '6.3.9 د نفوس د تناسب p د باور واټن اټکل (د لویې نمونې حالت)')
c.p('When the sample size is large the sample proportion $\\hat{p}$ has the sampling distribution which is approximately normal with mean p and $S.E=\\sqrt{\\frac{pq}{n}}$ i.e.', 'جب نمونے کا سائز بڑا ہو تو نمونے کے تناسب $\\hat{p}$ کی نمونہ جاتی تقسیم تقریباً نارمل ہوتی ہے جس کا اوسط p اور $S.E=\\sqrt{\\frac{pq}{n}}$ ہے یعنی', 'کله چې د نمونې اندازه لویه وي، د نمونې تناسب $\\hat{p}$ داسې نمونوي وېش لري چې نږدې نورمال دی او منځنی یې p او $S.E=\\sqrt{\\frac{pq}{n}}$ دی یعنې')
c.eq(r'Z=\frac{\hat{p}-p}{\sqrt{\frac{pq}{n}}}\sim N(0,1)\ \text{as}\ n\to\infty')
c.p('A 100(1−α)% confidence interval for p is written as;', 'p کے لیے 100(1−α)% اعتماد کا وقفہ یوں لکھا جاتا ہے؛', 'د p لپاره 100(1−α)% د باور واټن داسې لیکل کېږي؛')
c.eq(r'\hat{p}\pm Z_{\alpha/2}\sqrt{\frac{pq}{n}}')
c.p('If p is unknown then the confidence interval for p is computed by $\\hat{p}\\pm Z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}\\hat{q}}{n}}$', 'اگر p نامعلوم ہو تو p کا اعتماد کا وقفہ $\\hat{p}\\pm Z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}\\hat{q}}{n}}$ سے معلوم کیا جاتا ہے', 'که p نامعلوم وي، نو د p د باور واټن په $\\hat{p}\\pm Z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}\\hat{q}}{n}}$ محاسبه کېږي')
c.h('Example 6.16', 'مثال 6.16', 'بېلګه 6.16')
c.p('A random sample of 200 persons from a city was interviewed and 50 of them were found to be literate. Calculate a 90% confidence interval for the proportion of literate persons in the city.', 'ایک شہر سے 200 افراد کے تصادفی نمونے کا انٹرویو کیا گیا اور ان میں سے 50 خواندہ پائے گئے۔ شہر میں خواندہ افراد کے تناسب کے لیے 90% اعتماد کا وقفہ معلوم کریں۔', 'له یوه ښار څخه د 200 کسانو تصادفي نمونې سره مرکه وشوه او 50 یې باسواده وموندل شول. په ښار کې د باسوادو کسانو د تناسب لپاره 90% د باور واټن محاسبه کړئ.')
c.h(*SOL)
c.p('A 100 (1−α)% confidence interval for p (literate persons) is $\\hat{p}\\pm Z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}\\hat{q}}{n}}$', 'p (خواندہ افراد) کے لیے 100 (1−α)% اعتماد کا وقفہ $\\hat{p}\\pm Z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}\\hat{q}}{n}}$ ہے', 'د p (باسواده کسان) لپاره 100 (1−α)% د باور واټن $\\hat{p}\\pm Z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}\\hat{q}}{n}}$ دی')
c.p('Given', 'دیا گیا', 'ورکړل شوي')
c.p('n = 200, X = 50 (Number of literate persons), therefore $\\hat{p}=\\frac{X}{n}=\\frac{50}{200}=0.25$, $\\hat{q}=1-\\hat{p}=1-0.25=0.75$,', 'n = 200، X = 50 (خواندہ افراد کی تعداد)، لہٰذا $\\hat{p}=\\frac{X}{n}=\\frac{50}{200}=0.25$، $\\hat{q}=1-\\hat{p}=1-0.25=0.75$،', 'n = 200، X = 50 (د باسوادو کسانو شمېر)، نو $\\hat{p}=\\frac{X}{n}=\\frac{50}{200}=0.25$، $\\hat{q}=1-\\hat{p}=1-0.25=0.75$،')
c.p('$1-\\alpha=0.90$, $\\alpha=0.10$. From area table of standard normal distribution, we have $Z_{\\alpha/2}=Z_{\\frac{0.10}{2}}=Z_{0.05}=1.645$', '$1-\\alpha=0.90$، $\\alpha=0.10$۔ معیاری نارمل تقسیم کے رقبے کے جدول سے ہمارے پاس $Z_{\\alpha/2}=Z_{\\frac{0.10}{2}}=Z_{0.05}=1.645$ ہے', '$1-\\alpha=0.90$، $\\alpha=0.10$. د معیاري نورمال وېش د مساحت له جدول څخه لرو $Z_{\\alpha/2}=Z_{\\frac{0.10}{2}}=Z_{0.05}=1.645$')
c.p('Hence the 90% confidence interval for p is $0.25\\pm 1.645\\sqrt{\\frac{(0.25)(0.75)}{200}}$', 'لہٰذا p کے لیے 90% اعتماد کا وقفہ $0.25\\pm 1.645\\sqrt{\\frac{(0.25)(0.75)}{200}}$ ہے', 'نو د p لپاره 90% د باور واټن $0.25\\pm 1.645\\sqrt{\\frac{(0.25)(0.75)}{200}}$ دی')
c.eq(r'\text{or } 0.25\pm 0.05\quad\text{or } (0.2,\ 0.3)\quad\text{or } (0.2<p<0.3)')
c.h('6.3.10 Large sample confidence interval estimate for the difference between two population proportions (p₁ − p₂)', '6.3.10 دو آبادیوں کے تناسبوں کے فرق (p₁ − p₂) کا بڑے نمونے کا اعتماد کا وقفہ', '6.3.10 د دوو نفوسونو د تناسبونو د توپیر (p₁ − p₂) لپاره د لویې نمونې د باور واټن اټکل')
c.p(f'A simple extension of the estimation of a binomial proportion p is the estimation of the difference between two binomial proportions. For sufficiently large sample sizes the sampling distribution of ${DP}$ can be approximated by a normal distribution i.e.', f'دو رقمی تناسب p کے تخمین کی ایک سادہ توسیع دو دو رقمی تناسبوں کے فرق کا تخمین ہے۔ کافی بڑے نمونوں کے لیے ${DP}$ کی نمونہ جاتی تقسیم کو نارمل تقسیم سے تقریباً ظاہر کیا جا سکتا ہے یعنی', f'د بینومیل تناسب p د اټکل یوه ساده پراختیا د دوو بینومیل تناسبونو د توپیر اټکل دی. د کافي لویو نمونو لپاره د ${DP}$ نمونوي وېش د نورمال وېش په واسطه نږدې ښودل کېدای شي یعنې')
c.eq(rf'Z=\frac{{({DP})-(p_1-p_2)}}{{\sqrt{{\frac{{\hat{{p}}_1\hat{{q}}_1}}{{n_1}}+\frac{{\hat{{p}}_2\hat{{q}}_2}}{{n_2}}}}}}\sim N(0,1)')
c.p('The approximate 100(1−α)% confidence interval for $(p_1-p_2)$ is given by:', '$(p_1-p_2)$ کے لیے تقریبی 100(1−α)% اعتماد کا وقفہ یہ ہے:', 'د $(p_1-p_2)$ لپاره نږدې 100(1−α)% د باور واټن دا دی:')
c.eq(rf'({DP})\pm Z_{{\alpha/2}}\sqrt{{\frac{{\hat{{p}}_1\hat{{q}}_1}}{{n_1}}+\frac{{\hat{{p}}_2\hat{{q}}_2}}{{n_2}}}}')
pr = c.build('stat12-p115-ci-proportions', '6.3.9–6.3.10 Confidence intervals for p and p₁ − p₂ — Example 6.16', '6.3.9–6.3.10 p اور p₁ − p₂ کے اعتماد کے وقفے — مثال 6.16', '6.3.9–6.3.10 د p او p₁ − p₂ د باور واټنونه — بېلګه 6.16', 115, [221, 222])

if __name__ == '__main__':
    save(115, [(6, ex15), (6, pr)], issues=issues)
