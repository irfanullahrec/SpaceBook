"""PDF96 printed 183–184: Example 5.9 sampling distribution of p̂1 − p̂2, mean/S.E and verification; Example 5.10 (men/women proportions)."""
from class12_statistics_common import Builder, save

DP = r'\hat{p}_1-\hat{p}_2'
SOL = ('Solution:', 'حل:', 'حل:')
F = lambda a: f'$\\frac{{{a}}}{{81}}$'
b = Builder()
b.p(f'The sampling distribution of ${DP}$', f'${DP}$ کی نمونہ جاتی تقسیم', f'د ${DP}$ نمونوي وېش')
rows = [['−1', '16', F(16), '$-\\frac{16}{81}$', F(16)], ['$-\\frac{1}{2}$', '32', F(32), '$-\\frac{16}{81}$', F(8)], ['0', '24', F(24), '0', '0'],
        ['$\\frac{1}{2}$', '08', F(8), '$-\\frac{4}{81}$', F(2)], ['1', '01', F(1), F(1), F(1)], ['Total', '81', '1', '$\\frac{-27}{81}=-\\frac{1}{3}$', '$\\frac{27}{81}=\\frac{1}{3}$']]
b.grid('stat12-t-ex5-9-dist', [f'${DP}$', '$f$', f'$f({DP})$', f'$({DP})f({DP})$', f'$({DP})^2f({DP})$'], rows)
b.p('Mean of sampling distribution is;', 'نمونہ جاتی تقسیم کا اوسط یہ ہے؛', 'د نمونوي وېش منځنی دا دی؛')
b.eq(rf'\mu_{{{DP}}}=\Sigma({DP})\,f({DP})=-\frac{{27}}{{81}}=-\frac{{1}}{{3}}')
b.p('S.E of sampling distribution is;', 'نمونہ جاتی تقسیم کی معیاری غلطی یہ ہے؛', 'د نمونوي وېش معیاري تېروتنه دا ده؛')
b.mlines([rf'\sigma_{{{DP}}}=\sqrt{{\Sigma({DP})^2f({DP})-[\Sigma({DP})\,f({DP})]^2}}', r'=\sqrt{\frac{1}{3}-\left(-\frac{1}{3}\right)^2}=\sqrt{\frac{1}{3}-\frac{1}{9}}=\sqrt{\frac{2}{9}}=0.47'])
b.p('Verification:', 'تصدیق:', 'تایید:')
b.p('There is one even digit in population-1 so $p_1=\\frac{X_1}{N_1}=\\frac{1}{3}$', 'آبادی-1 میں ایک جفت ہندسہ ہے لہٰذا $p_1=\\frac{X_1}{N_1}=\\frac{1}{3}$', 'په نفوس-1 کې یو جفت رقم دی نو $p_1=\\frac{X_1}{N_1}=\\frac{1}{3}$')
b.p('There are two odd digits in population-2 so $p_2=\\frac{X_2}{N_2}=\\frac{2}{3}$', 'آبادی-2 میں دو طاق ہندسے ہیں لہٰذا $p_2=\\frac{X_2}{N_2}=\\frac{2}{3}$', 'په نفوس-2 کې دوه طاق رقمونه دي نو $p_2=\\frac{X_2}{N_2}=\\frac{2}{3}$')
b.p(f'Now $p_1-p_2=\\frac{{1}}{{3}}-\\frac{{2}}{{3}}=-\\frac{{1}}{{3}}=\\mu_{{{DP}}}$.', f'اب $p_1-p_2=\\frac{{1}}{{3}}-\\frac{{2}}{{3}}=-\\frac{{1}}{{3}}=\\mu_{{{DP}}}$۔', f'اوس $p_1-p_2=\\frac{{1}}{{3}}-\\frac{{2}}{{3}}=-\\frac{{1}}{{3}}=\\mu_{{{DP}}}$.')
b.p('Now by property, the S.E in S.W.R case is', 'اب خاصیت کے مطابق S.W.R کی صورت میں معیاری غلطی یہ ہے', 'اوس د ځانګړنې له مخې د S.W.R په حالت کې معیاري تېروتنه دا ده')
b.eq(rf'\sigma_{{{DP}}}=\sqrt{{\frac{{p_1q_1}}{{n_1}}+\frac{{p_2q_2}}{{n_2}}}}=\sqrt{{\frac{{\left(\frac{{1}}{{3}}\right)\left(\frac{{2}}{{3}}\right)}}{{2}}+\frac{{\left(\frac{{2}}{{3}}\right)\left(\frac{{1}}{{3}}\right)}}{{2}}}}=\sqrt{{\frac{{1}}{{9}}+\frac{{1}}{{9}}}}=\sqrt{{\frac{{2}}{{9}}}}=0.47.')
ex9 = b.build('stat12-p096-example-5-9-dist', 'Example 5.9 — sampling distribution of p̂₁ − p̂₂ and verification', 'مثال 5.9 — p̂₁ − p̂₂ کی نمونہ جاتی تقسیم اور تصدیق', 'بېلګه 5.9 — د p̂₁ − p̂₂ نمونوي وېش او تایید', 96, [183, 184])

c = Builder()
c.h('Example 5.10', 'مثال 5.10', 'بېلګه 5.10')
c.p('Suppose that 43% of men and 32% of women of a city are in favor of a proposed recreational facility. Describe the sampling distribution of the difference between sample proportions from samples of sizes 350 men and 270 women.', 'فرض کریں کسی شہر کے 43% مرد اور 32% خواتین ایک مجوزہ تفریحی سہولت کے حق میں ہیں۔ 350 مردوں اور 270 خواتین کے نمونوں سے نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم بیان کریں۔', 'فرض کړئ د یوه ښار 43% نارینه او 32% ښځینه د یوې وړاندیز شوې تفریحي اسانتیا په ګټه دي. د 350 نارینه وو او 270 ښځو له نمونو څخه د نمونو د تناسبونو د توپیر نمونوي وېش بیان کړئ.')
c.h(*SOL)
c.p('Let proportion of men is denoted by $p_1$ and proportion of women by $p_2$, then given information is symbolized as;', 'فرض کریں مردوں کے تناسب کو $p_1$ اور خواتین کے تناسب کو $p_2$ سے ظاہر کیا جائے، تو دی گئی معلومات کو علامتی طور پر یوں لکھا جاتا ہے؛', 'فرض کړئ د نارینه وو تناسب په $p_1$ او د ښځو تناسب په $p_2$ ښودل کېږي، نو ورکړل شوي معلومات په نښو داسې لیکل کېږي؛')
c.mlines([r'p_1=43\%=0.43\qquad p_2=32\%=0.32', r'q_1=1-P_1=1-0.43=0.57\qquad q_2=1-P_2=1-0.32=0.68', r'n_1=350\qquad n_2=270.'])
c.p('Describing the sampling distribution of the difference between sample proportions means to find its mean, S.E and the shape.', 'نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم بیان کرنے کا مطلب اس کا اوسط، معیاری غلطی اور شکل معلوم کرنا ہے۔', 'د نمونو د تناسبونو د توپیر د نمونوي وېش بیانول د هغه د منځني، معیاري تېروتنې او بڼې پیدا کول دي.')
c.p('By property we know that:', 'خاصیت کے مطابق ہم جانتے ہیں کہ:', 'د ځانګړنې له مخې پوهېږو چې:')
c.mlines([rf'\mu_{{{DP}}}=P_1-P_2=0.43-0.32=0.11', rf'\sigma_{{{DP}}}=\sqrt{{\frac{{p_1q_1}}{{n_1}}+\frac{{p_2q_2}}{{n_2}}}}', r'=\sqrt{\frac{(0.43)(0.57)}{350}+\frac{(0.32)(0.68)}{270}}=\sqrt{0.0007+0.0008}=\sqrt{0.00151}=0.04'])
c.p(f'Since the samples are sufficiently large, it means that sampling distribution of ${DP}$ has approximately normal distribution with mean 0.11 and standard deviation 0.04.', f'چونکہ نمونے کافی بڑے ہیں، اس کا مطلب ہے کہ ${DP}$ کی نمونہ جاتی تقسیم تقریباً نارمل ہے جس کا اوسط 0.11 اور معیاری انحراف 0.04 ہے۔', f'څرنګه چې نمونې کافي لویې دي، مانا یې دا ده چې د ${DP}$ نمونوي وېش نږدې نورمال دی چې منځنی یې 0.11 او معیاري انحراف یې 0.04 دی.')
ex10 = c.build('stat12-p096-example-5-10', 'Example 5.10 — difference between proportions of men and women', 'مثال 5.10 — مردوں اور خواتین کے تناسبوں کا فرق', 'بېلګه 5.10 — د نارینه وو او ښځو د تناسبونو توپیر', 96, [184])
issues = [{'id': 'stat12-p183-ex59-table', 'unit': 5, 'printedPage': 183, 'description': 'Example 5.9 sampling-distribution table prints (p̂₁−p̂₂)f entries −16/81 for the −1/2 row and −4/81 for the +1/2 row (expected −16/81 and +4/81); printed values retained.'}]

if __name__ == '__main__':
    save(96, [(5, ex9), (5, ex10)], issues=issues)
