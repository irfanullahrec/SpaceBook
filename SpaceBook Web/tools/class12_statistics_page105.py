"""PDF105 printed 201–202: Example 6.5 — 16 samples with X̄, s², S²; sampling distributions of X̄, s², S²."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
x = r'\overline{x}'
b = Builder()
b.p('Since sampling is with replacement therefore possible samples are $N^n=4^2=16$', 'چونکہ نمونہ گیری واپسی کے ساتھ ہے، لہٰذا ممکنہ نمونے $N^n=4^2=16$ ہیں', 'څرنګه چې نمونه اخیستنه له بېرته اچولو سره ده، نو شونې نمونې $N^n=4^2=16$ دي')
pop = [4, 8, 12, 16]
rows = []
for i, (a, c) in enumerate([(a, c) for a in pop for c in pop]):
    m = (a + c) / 2
    ss = (a - m) ** 2 + (c - m) ** 2
    rows.append([str(i + 1), f'({a},{c})', f'{m:g}', f'{ss:g}', f'{ss / 2:g}'])
head = ['S.No', 'Samples', f'${X}$', f'$s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(x-{x})^2$', f'$S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(x-{x})^2$']
b.table('stat12-t-ex6-5-samples', head, rows, ['نمبر شمار', 'نمونے'] + head[2:], ['شمېره', 'نمونې'] + head[2:])
b.p(f'i) The sampling distribution of ${X}$', f'i) ${X}$ کی نمونہ جاتی تقسیم', f'i) د ${X}$ نمونوي وېش')
d1 = [['4', '|', '1', '1/16', '4/16'], ['6', '||', '2', '2/16', '12/16'], ['8', '|||', '3', '3/16', '24/16'], ['10', '||||', '4', '4/16', '40/16'], ['12', '|||', '3', '3/16', '36/16'], ['14', '||', '2', '2/16', '28/16'], ['16', '|', '1', '1/16', '16/16'], ['Total', '-', '16', '1', '160/16']]
h1 = [f'${X}$', 'Tally bar', '$f$', f'$f({x})$', f'${X}f({x})$']
loc = lambda rows, t: [r if r[0] != 'Total' else [t] + r[1:] for r in rows]
b.table('stat12-t-ex6-5-xbar', h1, d1, [h1[0], 'ٹیلی بار'] + h1[2:], [h1[0], 'ټلي بار'] + h1[2:], loc(d1, 'کل'), loc(d1, 'ټول'))
b.eq(rf'E({X})=\mu_{{{x}}}=\Sigma{x}f({x})=\frac{{160}}{{16}}=10=\mu')
b.p(f'As mean of the sampling distribution of ${X}$ is equal to the population mean μ, so by definition of unbiasedness we say that ${X}$ is unbiased estimator of μ.', f'چونکہ ${X}$ کی نمونہ جاتی تقسیم کا اوسط آبادی کے اوسط μ کے برابر ہے، لہٰذا غیر جانبداری کی تعریف کے مطابق ہم کہتے ہیں کہ ${X}$، μ کا غیر جانبدار تخمین کار ہے۔', f'څرنګه چې د ${X}$ د نمونوي وېش منځنی د نفوس له منځني μ سره برابر دی، نو د بې‌پلوي د تعریف له مخې وایو چې ${X}$ د μ بې‌پلوه اټکلوونکی دی.')
b.p('(ii) The sampling distribution of $s^2$', '(ii) $s^2$ کی نمونہ جاتی تقسیم', '(ii) د $s^2$ نمونوي وېش')
d2 = [['0', '||||', '4', '4/16', '0'], ['8', '||||| |', '6', '6/16', '48/16'], ['32', '||||', '4', '4/16', '128/16'], ['72', '||', '2', '2/16', '144/116'], ['Total', '', '16', '1', '320/16']]
h2 = ['$s^2$', 'Tally bar', '$f$', '$f(s^2)$', '$s^2f(s^2)$']
b.table('stat12-t-ex6-5-s2', h2, d2, [h2[0], 'ٹیلی بار'] + h2[2:], [h2[0], 'ټلي بار'] + h2[2:], loc(d2, 'کل'), loc(d2, 'ټول'))
b.eq(r'E(s^2)=\mu_{s^2}=\Sigma s^2f(s^2)=\frac{320}{16}=20=\sigma^2')
b.p(f'Hence $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(x_i-{X})^2$ is an unbiased estimator of $\\sigma^2$.', f'لہٰذا $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(x_i-{X})^2$، $\\sigma^2$ کا غیر جانبدار تخمین کار ہے۔', f'نو $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(x_i-{X})^2$ د $\\sigma^2$ بې‌پلوه اټکلوونکی دی.')
b.p('(iii) The sampling distribution of $S^2$', '(iii) $S^2$ کی نمونہ جاتی تقسیم', '(iii) د $S^2$ نمونوي وېش')
d3 = [['0', '||||', '4', '4/16', '0'], ['4', '||||| |', '6', '6/16', '24/16'], ['16', '||||', '4', '4/16', '64/16'], ['36', '||', '2', '2/16', '72/16'], ['Total', '', '16', '1', '160/16']]
h3 = ['$S^2$', 'Tally bar', '$f$', '$f(S^2)$', '$S^2f(S^2)$']
b.table('stat12-t-ex6-5-S2', h3, d3, [h3[0], 'ٹیلی بار'] + h3[2:], [h3[0], 'ټلي بار'] + h3[2:], loc(d3, 'کل'), loc(d3, 'ټول'))
rec = b.build('stat12-p105-example-6-5-tables', 'Example 6.5 — samples and sampling distributions of X̄, s² and S²', 'مثال 6.5 — نمونے اور X̄، s² اور S² کی نمونہ جاتی تقسیمیں', 'بېلګه 6.5 — نمونې او د X̄، s² او S² نمونوي وېشونه', 105, [201, 202])
issues = [{'id': 'stat12-p202-144-116', 'unit': 6, 'printedPage': 202, 'description': 'The s² sampling-distribution table prints 144/116 for the 72-row (should be 144/16); printed value retained.'}]

if __name__ == '__main__':
    save(105, [(6, rec)], issues=issues)
