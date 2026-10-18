"""PDF104 printed 199–200: proof that s² is unbiased for σ²; Example 6.5 question and population mean/variance."""
from class12_statistics_common import Builder, save

PROOF = ('Proof:', 'ثبوت:', 'ثبوت:')
SOL = ('Solution:', 'حل:', 'حل:')
X = r'\overline{X}'
b = Builder()
b.h(*PROOF)
b.p(f'By definition $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$', f'تعریف کے مطابق $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$', f'د تعریف له مخې $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$')
b.eq(rf'(n-1)\,s^2=\sum_{{i=1}}^{{n}}(X_i-{X})^2')
b.p(f'$=\\sum_{{i=1}}^{{n}}(X_i-\\mu+\\mu-{X})^2$ i.e. μ is added and subtracted', f'$=\\sum_{{i=1}}^{{n}}(X_i-\\mu+\\mu-{X})^2$ یعنی μ جمع اور تفریق کیا گیا', f'$=\\sum_{{i=1}}^{{n}}(X_i-\\mu+\\mu-{X})^2$ یعنې μ جمع او تفریق شوی')
b.mlines([rf'=\sum_{{i=1}}^{{n}}[(X_i-\mu)-({X}-\mu)]^2', rf'=\sum_{{i=1}}^{{n}}[(X_i-\mu)^2+({X}-\mu)^2-2(X_i-\mu)({X}-\mu)]', rf'=\sum_{{i=1}}^{{n}}(X_i-\mu)^2+n({X}-\mu)^2-2({X}-\mu)\sum_{{i=1}}^{{n}}(X_i-\mu)'])
b.p(f'$=\\sum_{{i=1}}^{{n}}(X_i-\\mu)^2+n({X}-\\mu)^2-2({X}-\\mu)\\,n({X}-\\mu)$ As $\\sum_{{i=1}}^{{n}}(X_i-\\mu)=n({X}-\\mu)$', f'$=\\sum_{{i=1}}^{{n}}(X_i-\\mu)^2+n({X}-\\mu)^2-2({X}-\\mu)\\,n({X}-\\mu)$ کیونکہ $\\sum_{{i=1}}^{{n}}(X_i-\\mu)=n({X}-\\mu)$', f'$=\\sum_{{i=1}}^{{n}}(X_i-\\mu)^2+n({X}-\\mu)^2-2({X}-\\mu)\\,n({X}-\\mu)$ ځکه چې $\\sum_{{i=1}}^{{n}}(X_i-\\mu)=n({X}-\\mu)$')
b.mlines([rf'=\sum_{{i=1}}^{{n}}(X_i-\mu)^2+n({X}-\mu)^2-2n({X}-\mu)^2', rf'=\sum_{{i=1}}^{{n}}(X_i-\mu)^2-n({X}-\mu)^2'])
b.p('Now taking expectation on both sides', 'اب دونوں طرف توقع لینے سے', 'اوس دواړو خواوو ته تمه اخیستلو سره')
b.eq(rf'(n-1)\,E(s^2)=n\,E(X_i-\mu)^2-n\,E({X}-\mu)^2')
b.p('$=n\\sigma^2-n\\sigma_{\\overline{x}}^2$ As $\\sigma_{\\overline{x}}^2=\\frac{\\sigma^2}{n}$', '$=n\\sigma^2-n\\sigma_{\\overline{x}}^2$ کیونکہ $\\sigma_{\\overline{x}}^2=\\frac{\\sigma^2}{n}$', '$=n\\sigma^2-n\\sigma_{\\overline{x}}^2$ ځکه چې $\\sigma_{\\overline{x}}^2=\\frac{\\sigma^2}{n}$')
b.mlines([r'=(n-1)\sigma^2', r'E(s^2)=\sigma^2'])
b.p(f'This implies that $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ is an unbiased estimator of $\\sigma^2$.', f'اس کا مطلب ہے کہ $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$، $\\sigma^2$ کا غیر جانبدار تخمین کار ہے۔', f'دا ښيي چې $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ د $\\sigma^2$ بې‌پلوه اټکلوونکی دی.')
pr = b.build('stat12-p104-example-6-4-proof', 'Example 6.4 — proof that s² is unbiased', 'مثال 6.4 — s² کے غیر جانبدار ہونے کا ثبوت', 'بېلګه 6.4 — د s² د بې‌پلوه کېدو ثبوت', 104, [199, 200])

c = Builder()
c.h('Example 6.5', 'مثال 6.5', 'بېلګه 6.5')
c.p('Draw all possible samples of size 2 with replacement from a population having elements 4, 8, 12, 16 and show that;', 'عناصر 4، 8، 12، 16 والی آبادی سے واپسی کے ساتھ 2 سائز کے تمام ممکنہ نمونے نکالیں اور ثابت کریں کہ؛', 'له 4، 8، 12، 16 عناصرو لرونکي نفوس څخه له بېرته اچولو سره د 2 اندازې ټولې شونې نمونې راوباسئ او وښایاست چې؛')
c.group('lines', [
    (f'i) $E({X})=\\mu$ i.e. ${X}$ is an unbiased estimator of μ.', f'i) $E({X})=\\mu$ یعنی ${X}$، μ کا غیر جانبدار تخمین کار ہے۔', f'i) $E({X})=\\mu$ یعنې ${X}$ د μ بې‌پلوه اټکلوونکی دی.'),
    (f'ii) $E(s^2)=\\sigma^2$ i.e. $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ is an unbiased estimator of $\\sigma^2$.', f'ii) $E(s^2)=\\sigma^2$ یعنی $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$، $\\sigma^2$ کا غیر جانبدار تخمین کار ہے۔', f'ii) $E(s^2)=\\sigma^2$ یعنې $s^2=\\frac{{1}}{{n-1}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ د $\\sigma^2$ بې‌پلوه اټکلوونکی دی.'),
    (f'iii) $E(S^2)\\neq\\sigma^2$ i.e $S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ is a biased estimator of $\\sigma^2$.', f'iii) $E(S^2)\\neq\\sigma^2$ یعنی $S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$، $\\sigma^2$ کا جانبدار تخمین کار ہے۔', f'iii) $E(S^2)\\neq\\sigma^2$ یعنې $S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ د $\\sigma^2$ پلوي اټکلوونکی دی.'),
])
c.h(*SOL)
c.p('Given 4, 8, 12, 16; N = 4; and n = 2', 'دیا گیا ہے 4، 8، 12، 16؛ N = 4؛ اور n = 2', 'ورکړل شوي 4، 8، 12، 16؛ N = 4؛ او n = 2')
c.p('Population mean $\\mu=\\frac{\\Sigma X}{N}=\\frac{4+8+12+16}{4}=\\frac{40}{4}=10$', 'آبادی کا اوسط $\\mu=\\frac{\\Sigma X}{N}=\\frac{4+8+12+16}{4}=\\frac{40}{4}=10$', 'د نفوس منځنی $\\mu=\\frac{\\Sigma X}{N}=\\frac{4+8+12+16}{4}=\\frac{40}{4}=10$')
c.p('Population variance $\\sigma^2=\\frac{\\Sigma X^2}{N}-\\left(\\frac{\\Sigma X}{N}\\right)^2=\\frac{480}{4}-\\left(\\frac{40}{4}\\right)^2=20$', 'آبادی کا تغیر $\\sigma^2=\\frac{\\Sigma X^2}{N}-\\left(\\frac{\\Sigma X}{N}\\right)^2=\\frac{480}{4}-\\left(\\frac{40}{4}\\right)^2=20$', 'د نفوس واریانس $\\sigma^2=\\frac{\\Sigma X^2}{N}-\\left(\\frac{\\Sigma X}{N}\\right)^2=\\frac{480}{4}-\\left(\\frac{40}{4}\\right)^2=20$')
ex = c.build('stat12-p104-example-6-5', 'Example 6.5 — unbiasedness check with all samples', 'مثال 6.5 — تمام نمونوں سے غیر جانبداری کی جانچ', 'بېلګه 6.5 — له ټولو نمونو سره د بې‌پلوي ازموینه', 104, [200])

if __name__ == '__main__':
    save(104, [(6, pr), (6, ex)])
