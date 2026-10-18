"""PDF89 printed 169–170: Example 5.5 sampling distribution, calculation, verification; Example 5.6 (27 samples of size 3, S.W.R)."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
x = r'\overline{x}'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p(f'The sampling distribution of ${X}$ is given below:', f'${X}$ کی نمونہ جاتی تقسیم نیچے دی گئی ہے:', f'د ${X}$ نمونوي وېش لاندې ورکړل شوی:')
tal = [['3', '|', '1', '1/15'], ['5', '||', '2', '2/15'], ['6', '||||', '4', '4/15'], ['7', '||', '2', '2/15'], ['8', '|', '1', '1/15'], ['9', '||||', '4', '4/15'], ['10', '|', '1', '1/15'], ['Total', '', '15', '1']]
b.table('stat12-t-ex5-5-dist', [f'${X}$', 'Tally bar', '$f$', f'$f({x})$'], tal, [f'${X}$', 'ٹیلی بار', '$f$', f'$f({x})$'], [f'${X}$', 'ټلي بار', '$f$', f'$f({x})$'],
        [r if r[0] != 'Total' else ['کل'] + r[1:] for r in tal], [r if r[0] != 'Total' else ['ټول'] + r[1:] for r in tal])
b.p(f'(iii) Calculation for mean and S.E of the sampling distribution of ${X}$', f'(iii) ${X}$ کی نمونہ جاتی تقسیم کے اوسط اور معیاری غلطی کا حساب', f'(iii) د ${X}$ د نمونوي وېش د منځني او معیاري تېروتنې محاسبه')
b.grid('stat12-t-ex5-5-calc', [f'${X}$', f'$f({x})$', f'${X}f({x})$', f'${X}^2f({x})$'],
       [['3', '1/15', '3/15', '9/19'], ['5', '2/15', '10/15', '50/15'], ['6', '4/15', '24/15', '144/15'], ['7', '2/15', '14/15', '98/15'], ['8', '1/15', '8/15', '64/15'], ['9', '4/15', '36/15', '324/15'], ['10', '1/15', '10/15', '100/15'], ['Total', '1', '105/15', '789/15']])
b.mlines([rf'E({X})=\mu_{{{x}}}=\Sigma{x}f({x})=\frac{{105}}{{15}}=7', rf'\sigma_{{{x}}}=\sqrt{{\Sigma{x}^2f({x})-[\Sigma{x}f({x})]^2}}=\sqrt{{\frac{{789}}{{15}}-\left(\frac{{105}}{{15}}\right)^2}}', r'=\sqrt{52.6-49}=\sqrt{3.6}=1.9'])
b.p('Now verification of the properties:', 'اب خصوصیات کی تصدیق:', 'اوس د ځانګړنو تایید:')
b.p(f'(i) As we see that μ = 7, $E({X})=7$, hence proved that $E({X})=\\mu$', f'(i) جیسا کہ ہم دیکھتے ہیں کہ μ = 7، $E({X})=7$، لہٰذا ثابت ہوا کہ $E({X})=\\mu$', f'(i) لکه څنګه چې وینو μ = 7، $E({X})=7$، نو ثابته شوه چې $E({X})=\\mu$')
b.p('(ii) In S.W.O.R case, the S.E is', '(ii) S.W.O.R کی صورت میں معیاری غلطی یہ ہے', '(ii) د S.W.O.R په حالت کې معیاري تېروتنه دا ده')
b.eq(rf'\sigma_{{{x}}}=\frac{{\sigma}}{{\sqrt{{n}}}}\cdot\sqrt{{\frac{{N-n}}{{N-n}}}}=\frac{{3}}{{\sqrt{{2}}}}\sqrt{{\frac{{6-2}}{{6-1}}}}=\frac{{3}}{{\sqrt{{2}}}}\sqrt{{\frac{{4}}{{5}}}}=1.9')
b.p(f'This is exactly the same as computed $\\sigma_{{{x}}}$.', f'یہ بالکل معلوم کی گئی $\\sigma_{{{x}}}$ کے برابر ہے۔', f'دا دقیقاً د محاسبه شوې $\\sigma_{{{x}}}$ سره یو شان ده.')
ex5 = b.build('stat12-p089-example-5-5-dist', 'Example 5.5 — sampling distribution, mean, S.E and verification', 'مثال 5.5 — نمونہ جاتی تقسیم، اوسط، معیاری غلطی اور تصدیق', 'بېلګه 5.5 — نمونوي وېش، منځنی، معیاري تېروتنه او تایید', 89, [169, 170])

c = Builder()
c.h('Example 5.6', 'مثال 5.6', 'بېلګه 5.6')
c.p('Draw all possible random samples of size 3 with replacement from a population of three values 3, 6, 9. Obtain the sampling distribution of sample mean and verify the theoretical results.', 'تین قیمتوں 3، 6، 9 کی آبادی سے واپسی کے ساتھ 3 کے سائز کے تمام ممکنہ تصادفی نمونے نکالیں۔ نمونے کے اوسط کی نمونہ جاتی تقسیم حاصل کریں اور نظری نتائج کی تصدیق کریں۔', 'د درېیو قیمتونو 3، 6، 9 له نفوس څخه له بېرته اچولو سره د 3 اندازې ټولې شونې تصادفي نمونې راوباسئ. د نمونې د منځني نمونوي وېش ترلاسه کړئ او نظري پایلې تایید کړئ.')
c.h(*SOL)
c.p('Given population: 3, 6, 9, N = 3, n = 3', 'دی گئی آبادی: 3، 6، 9، N = 3، n = 3', 'ورکړل شوی نفوس: 3، 6، 9، N = 3، n = 3')
c.p('Here sampling is done with replacement, therefore, possible samples are $N^n=3^3=27$. The possible samples and the sample means are listed in the following table.', 'یہاں نمونہ گیری واپسی کے ساتھ کی گئی ہے، لہٰذا ممکنہ نمونے $N^n=3^3=27$ ہیں۔ ممکنہ نمونے اور نمونوں کے اوسط درج ذیل جدول میں دیے گئے ہیں۔', 'دلته نمونه اخیستنه له بېرته اچولو سره شوې، نو شونې نمونې $N^n=3^3=27$ دي. شونې نمونې او د نمونو منځني په لاندې جدول کې لیکل شوي.')
vals = (3, 6, 9)
samples = [(a, b2, c2) for a in vals for b2 in vals for c2 in vals]
rows = []
for i in range(9):
    row = []
    for blk in range(3):
        k = blk * 9 + i
        s = samples[k]
        row += [str(k + 1), ', '.join(map(str, s)), str(sum(s) // 3)]
    rows.append(row)
H = ['S.No.', 'Samples', f'${X}$'] * 3
c.table('stat12-t-ex5-6-samples', H, rows, ['نمبر شمار', 'نمونے', f'${X}$'] * 3, ['شمېره', 'نمونې', f'${X}$'] * 3)
ex6 = c.build('stat12-p089-example-5-6', 'Example 5.6 — 27 samples of size 3 with replacement', 'مثال 5.6 — واپسی کے ساتھ 3 کے سائز کے 27 نمونے', 'بېلګه 5.6 — له بېرته اچولو سره د 3 اندازې 27 نمونې', 89, [170])
issues = [{'id': 'stat12-p169-170-ex55', 'unit': 5, 'printedPage': 169, 'description': 'Example 5.5 table prints 9/19 for the first X̄²f(x̄) entry (should be 9/15) and the S.W.O.R formula as √((N−n)/(N−n)); printed forms retained.'}]

if __name__ == '__main__':
    save(89, [(5, ex5), (5, ex6)], issues=issues)
