"""PDF92 printed 175–176: Example 5.7 sampling distribution of X̄1−X̄2, mean/S.E, verification; 5.4 proportion; 5.4.1 sampling distribution of p̂ (start)."""
from class12_statistics_common import Builder, save

D = r'\overline{X}_1-\overline{X}_2'
d = r'\overline{x}_1-\overline{x}_2'
b = Builder()
b.p(f'(ii) The sampling distribution of ${D}$', f'(ii) ${D}$ کی نمونہ جاتی تقسیم', f'(ii) د ${D}$ نمونوي وېش')
rows = [['0', '|', '1', '1/81', '0', '0'], ['0.5', '||', '2', '2/81', '1/81', '0.5/81'], ['1', '||||| ||', '7', '7/81', '7/81', '7/81'], ['1.5', '||||| |||||', '10', '10/81', '15/81', '22.5/81'],
        ['2', '||||| ||||| ||||| ||', '17', '17/81', '34/81', '68/81'], ['2.5', '||||| ||||| ||||| |', '16', '16/81', '40/81', '100/81'], ['3', '||||| ||||| ||||| |', '16', '16/81', '48/81', '144/81'],
        ['3.5', '||||| |||', '8', '8/81', '28/81', '98/81'], ['4', '||||', '4', '4/81', '16/81', '64/81'], ['Total', '', '81', '1', '189/81', '504/81']]
head = [f'$({D})$', 'Tally', '$f$', f'$f({d})$', f'$({D})f({d})$', f'$({D})^2f({d})$']
b.table('stat12-t-ex5-7-dist', head, rows, [head[0], 'ٹیلی'] + head[2:], [head[0], 'ټلي'] + head[2:],
        [r if r[0] != 'Total' else ['کل'] + r[1:] for r in rows], [r if r[0] != 'Total' else ['ټول'] + r[1:] for r in rows])
b.mlines([rf'\text{{Now}}\quad\mu_{{{d}}}=\Sigma({d})\,f({d})=\frac{{189}}{{81}}=2.33', rf'\sigma_{{{d}}}=\sqrt{{\Sigma({d})^2f({d})-[\Sigma({d})\,f({d})]^2}}', r'=\sqrt{\frac{504}{81}-\left(\frac{189}{81}\right)^2}=\sqrt{6.222-5.429}=\sqrt{0.7931}=0.88'])
b.p('(iii) Verification:', '(iii) تصدیق:', '(iii) تایید:')
b.p('Mean and variance of population 1:', 'آبادی 1 کا اوسط اور تغیر:', 'د نفوس 1 منځنی او واریانس:')
b.mlines([r'\mu_1=\frac{3+4+5}{3}=\frac{12}{3}=4', r'\sigma_1^2=\frac{\Sigma x_1^2}{N_1}-\left(\frac{\Sigma x_1}{N_1}\right)^2=\frac{50}{3}-\left(\frac{12}{3}\right)^2=16.67-16=0.67'])
b.p('Mean and variance of population 2:', 'آبادی 2 کا اوسط اور تغیر:', 'د نفوس 2 منځنی او واریانس:')
b.mlines([r'\mu_2=\frac{1+1+3}{3}=\frac{5}{3}=1.67', r'\sigma_2^2=\frac{\Sigma x_2^2}{N_2}-\left(\frac{\Sigma x_2}{N_2}\right)^2=\frac{11}{3}-\left(\frac{5}{3}\right)^2=3.67-2.789=0.88'])
b.p('By property:', 'خاصیت کے مطابق:', 'د ځانګړنې له مخې:')
b.mlines([rf'\mu_{{{d}}}=\mu_1-\mu_2=4-1.67=2.33', rf'\sigma_{{{d}}}=\sqrt{{\frac{{\sigma_1^2}}{{n_1}}+\frac{{\sigma_2^2}}{{n_2}}}}=\sqrt{{\frac{{0.67}}{{2}}+\frac{{0.88}}{{2}}}}=\sqrt{{0.335+0.44}}=0.775=0.88'])
b.p('These are same as computed results.', 'یہ معلوم کیے گئے نتائج کے برابر ہیں۔', 'دا د محاسبه شویو پایلو سره یو شان دي.')
ex = b.build('stat12-p092-example-5-7-dist', 'Example 5.7 — sampling distribution of X̄₁ − X̄₂ and verification', 'مثال 5.7 — X̄₁ − X̄₂ کی نمونہ جاتی تقسیم اور تصدیق', 'بېلګه 5.7 — د X̄₁ − X̄₂ نمونوي وېش او تایید', 92, [175, 176])

c = Builder()
c.h('5.4 Proportion', '5.4 تناسب', '5.4 تناسب')
c.p('An expression which compares a characteristic with the total is called proportion i.e.', 'وہ اظہاریہ جو کسی خاصیت کا کل سے موازنہ کرے، تناسب کہلاتا ہے یعنی', 'هغه افاده چې یوه ځانګړنه له ټول سره پرتله کوي، تناسب بلل کېږي یعنې')
c.group('lines', [
    ('$p=\\frac{X}{N}$ (parameter)', '$p=\\frac{X}{N}$ (پیرامیٹر)', '$p=\\frac{X}{N}$ (پارامټر)'),
    ('$\\hat{p}=\\frac{X}{n}$ (estimator)', '$\\hat{p}=\\frac{X}{n}$ (تخمین کار)', '$\\hat{p}=\\frac{X}{n}$ (اټکلوونکی)'),
])
c.p('Where X denotes the number of individuals having a specified characteristic and is a binomial random variable because each individual has two possibilities i.e. may or may not have the specified characteristic. Thus X~B (n, p).', 'جہاں X مخصوص خاصیت رکھنے والے افراد کی تعداد ظاہر کرتا ہے اور یہ دو رقمی تصادفی متغیر ہے کیونکہ ہر فرد کے دو امکانات ہیں یعنی اس میں مخصوص خاصیت ہو یا نہ ہو۔ لہٰذا X~B (n, p)۔', 'چې X د ټاکلې ځانګړنې لرونکو افرادو شمېر ښيي او بینومیل تصادفي متغیر دی ځکه چې هر فرد دوه امکانونه لري یعنې کېدای شي ټاکلې ځانګړنه ولري یا ونه لري. نو X~B (n, p).')
c.h('5.4.1 Sampling distribution of sample proportion $\\hat{p}$', '5.4.1 نمونے کے تناسب $\\hat{p}$ کی نمونہ جاتی تقسیم', '5.4.1 د نمونې د تناسب $\\hat{p}$ نمونوي وېش')
c.p('The probability distribution of all possible values of $\\hat{p}$ is called sampling distribution of $\\hat{p}$. Mean of the sampling distribution of $\\hat{p}$ is denoted by $\\mu_{\\hat{p}}$ and it’s S.E by $\\sigma_{\\hat{p}}$', '$\\hat{p}$ کی تمام ممکنہ قیمتوں کی احتمالی تقسیم کو $\\hat{p}$ کی نمونہ جاتی تقسیم کہتے ہیں۔ $\\hat{p}$ کی نمونہ جاتی تقسیم کے اوسط کو $\\mu_{\\hat{p}}$ اور معیاری غلطی کو $\\sigma_{\\hat{p}}$ سے ظاہر کرتے ہیں', 'د $\\hat{p}$ د ټولو شونو قیمتونو احتمالي وېش ته د $\\hat{p}$ نمونوي وېش وایي. د $\\hat{p}$ د نمونوي وېش منځنی په $\\mu_{\\hat{p}}$ او معیاري تېروتنه یې په $\\sigma_{\\hat{p}}$ ښودل کېږي')
pr = c.build('stat12-p092-proportion', '5.4 Proportion and 5.4.1 sampling distribution of p̂', '5.4 تناسب اور 5.4.1 p̂ کی نمونہ جاتی تقسیم', '5.4 تناسب او 5.4.1 د p̂ نمونوي وېش', 92, [176])
issues = [{'id': 'stat12-p176-sd-0775', 'unit': 5, 'printedPage': 176, 'description': 'Example 5.7 verification prints √(0.335+0.44) = 0.775 = 0.88 (√0.775 ≈ 0.88); printed line retained. The Tally column of the X̄₁−X̄₂ table is shown as grouped strokes.'}]

if __name__ == '__main__':
    save(92, [(5, ex), (5, pr)], issues=issues)
