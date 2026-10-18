"""PDF106 printed 203–204: Example 6.5 conclusion (S² biased), Example 6.6 (proportion of even numbers), 6.2.4 efficiency and relative efficiency."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
P = r'\hat{p}'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'E(S^2)=\Sigma S^2f(S^2)=\frac{160}{16}=10', r'E(S^2)\neq\sigma^2'])
b.p(f'Hence $S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ is a biased estimator of $\\sigma^2$.', f'لہٰذا $S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$، $\\sigma^2$ کا جانبدار تخمین کار ہے۔', f'نو $S^2=\\frac{{1}}{{n}}\\sum_{{i=1}}^{{n}}(X_i-{X})^2$ د $\\sigma^2$ پلوي اټکلوونکی دی.')
b.h('Example 6.6', 'مثال 6.6', 'بېلګه 6.6')
b.p(f'Draw all possible samples of size 2 with replacement from a population consisting of units 1,2,5,6 and find the proportion of even numbers in the samples. Construct the sampling distribution of sample proportion ${P}$ and check that $E({P})=p$ i.e. ${P}$ is an unbiased estimator of p.', f'اکائیوں 1،2،5،6 پر مشتمل آبادی سے واپسی کے ساتھ 2 سائز کے تمام ممکنہ نمونے نکالیں اور نمونوں میں جفت اعداد کا تناسب معلوم کریں۔ نمونے کے تناسب ${P}$ کی نمونہ جاتی تقسیم بنائیں اور جانچیں کہ $E({P})=p$ یعنی ${P}$، p کا غیر جانبدار تخمین کار ہے۔', f'له 1،2،5،6 واحدونو جوړ نفوس څخه له بېرته اچولو سره د 2 اندازې ټولې شونې نمونې راوباسئ او په نمونو کې د جفت عددونو تناسب پیدا کړئ. د نمونې د تناسب ${P}$ نمونوي وېش جوړ کړئ او وګورئ چې $E({P})=p$ یعنې ${P}$ د p بې‌پلوه اټکلوونکی دی.')
b.h(*SOL)
b.p('Given 1, 2, 5, 6 N = 4 n = 2', 'دیا گیا ہے 1، 2، 5، 6 N = 4 n = 2', 'ورکړل شوي 1، 2، 5، 6 N = 4 n = 2')
b.p('Population proportion $p=\\frac{X}{N}=\\frac{2}{4}=0.5$', 'آبادی کا تناسب $p=\\frac{X}{N}=\\frac{2}{4}=0.5$', 'د نفوس تناسب $p=\\frac{X}{N}=\\frac{2}{4}=0.5$')
b.p('Possible samples of size n = 2 in S.W.R. case are $N^n=4^2=16$ which are shown in the table.', 'S.W.R. کی صورت میں n = 2 سائز کے ممکنہ نمونے $N^n=4^2=16$ ہیں جو جدول میں دکھائے گئے ہیں۔', 'د S.W.R. په حالت کې د n = 2 اندازې شونې نمونې $N^n=4^2=16$ دي چې په جدول کې ښودل شوي.')
pop = [1, 2, 5, 6]
fs = {0: '0', 1: '1/2', 2: '1'}
rows = [[str(i + 1), f'{a},{c}', fs[(a % 2 == 0) + (c % 2 == 0)]] for i, (a, c) in enumerate([(a, c) for a in pop for c in pop])]
b.table('stat12-t-ex6-6-samples', ['S.No.', 'Samples', f'${P}$'], rows, ['نمبر شمار', 'نمونے', f'${P}$'], ['شمېره', 'نمونې', f'${P}$'])
b.p(f'The sampling distribution of sample proportions ${P}$', f'نمونوں کے تناسبوں ${P}$ کی نمونہ جاتی تقسیم', f'د نمونو د تناسبونو ${P}$ نمونوي وېش')
d = [['0', '||||', '4', '4/16', '0'], ['1/2', '||||| |||', '8', '8/16', '4/16'], ['1', '||||', '4', '4/16', '4/16'], ['Total', '', '16', '', '8/16']]
h = [f'${P}$', 'Tally bar', '$f$', f'$f({P})$', f'${P}f({P})$']
b.table('stat12-t-ex6-6-dist', h, d, [h[0], 'ٹیلی بار'] + h[2:], [h[0], 'ټلي بار'] + h[2:], [r if r[0] != 'Total' else ['کل'] + r[1:] for r in d], [r if r[0] != 'Total' else ['ټول'] + r[1:] for r in d])
b.eq(rf'E({P})=\mu_{{{P}}}=\Sigma{P}f({P})=\frac{{8}}{{16}}=0.5=p.')
b.p(f'It means that ${P}=\\frac{{X}}{{n}}$ is an unbiased estimator of population proportion p.', f'اس کا مطلب ہے کہ ${P}=\\frac{{X}}{{n}}$ آبادی کے تناسب p کا غیر جانبدار تخمین کار ہے۔', f'مانا یې دا ده چې ${P}=\\frac{{X}}{{n}}$ د نفوس د تناسب p بې‌پلوه اټکلوونکی دی.')
ex = b.build('stat12-p106-examples-6-5-6-6', 'Example 6.5 conclusion and Example 6.6 — sample proportion is unbiased', 'مثال 6.5 کا نتیجہ اور مثال 6.6 — نمونے کا تناسب غیر جانبدار ہے', 'د بېلګې 6.5 پایله او بېلګه 6.6 — د نمونې تناسب بې‌پلوه دی', 106, [203, 204])

c = Builder()
c.h('6.2.4 Efficiency', '6.2.4 کارکردگی (Efficiency)', '6.2.4 موثریت (Efficiency)')
c.p('If there are two estimators, both possessing the property of unbiasedness which can be used for the estimation of a parameter, it is difficult for us to choose the best one between them. The efficiency property decides to prefer the one which has minimum variance. Hence efficiency is a selection criterion for efficient estimator between unbiasead estimators.', 'اگر دو تخمین کار ہوں جن دونوں میں غیر جانبداری کی خاصیت ہو اور جو کسی پیرامیٹر کے تخمین کے لیے استعمال ہو سکیں، تو ہمارے لیے ان میں سے بہترین کا انتخاب مشکل ہوتا ہے۔ کارکردگی کی خاصیت یہ فیصلہ کرتی ہے کہ اس کو ترجیح دی جائے جس کا تغیر کم سے کم ہو۔ لہٰذا کارکردگی غیر جانبدار تخمین کاروں میں سے مؤثر تخمین کار کے انتخاب کا معیار ہے۔', 'که دوه اټکلوونکي وي چې دواړه د بې‌پلوي ځانګړنه ولري او د یوه پارامټر د اټکل لپاره وکارول شي، نو د هغو له منځه د غوره ټاکل موږ ته ستونزمن وي. د موثریت ځانګړنه پرېکړه کوي چې هغه غوره کړو چې لږ تر لږه واریانس لري. نو موثریت د بې‌پلوه اټکلوونکو ترمنځ د موثر اټکلوونکي د ټاکنې معیار دی.')
c.h('Definition of efficient estimator:', 'مؤثر تخمین کار کی تعریف:', 'د موثر اټکلوونکي تعریف:')
c.p('If $\\hat{\\theta}_1$ and $\\hat{\\theta}_2$ are two unbiased estimators of the same parameter θ and $Var(\\hat{\\theta}_1)<Var(\\hat{\\theta}_2)$, then $\\hat{\\theta}_1$ is efficient estimator than $\\hat{\\theta}_2$. Efficiency is generally expressed in relative terms as:', 'اگر $\\hat{\\theta}_1$ اور $\\hat{\\theta}_2$ ایک ہی پیرامیٹر θ کے دو غیر جانبدار تخمین کار ہوں اور $Var(\\hat{\\theta}_1)<Var(\\hat{\\theta}_2)$ ہو تو $\\hat{\\theta}_1$، $\\hat{\\theta}_2$ سے زیادہ مؤثر تخمین کار ہے۔ کارکردگی کو عموماً نسبتی شکل میں یوں ظاہر کیا جاتا ہے:', 'که $\\hat{\\theta}_1$ او $\\hat{\\theta}_2$ د یوه پارامټر θ دوه بې‌پلوه اټکلوونکي وي او $Var(\\hat{\\theta}_1)<Var(\\hat{\\theta}_2)$ وي، نو $\\hat{\\theta}_1$ تر $\\hat{\\theta}_2$ موثر اټکلوونکی دی. موثریت معمولاً په نسبي بڼه داسې ښودل کېږي:')
c.add('equation', '$$R.E=\\frac{\\textit{Variance of efficient estimator}}{\\textit{Variance of other estimator}}$$', '$$R.E=\\frac{\\textit{Variance of efficient estimator}}{\\textit{Variance of other estimator}}$$ (مؤثر تخمین کار کا تغیر / دوسرے تخمین کار کا تغیر)', '$$R.E=\\frac{\\textit{Variance of efficient estimator}}{\\textit{Variance of other estimator}}$$ (د موثر اټکلوونکي واریانس / د بل اټکلوونکي واریانس)')
c.group('lines', [
    ('If $0\\le R.E<1\\Rightarrow\\hat{\\theta}_1$ is efficient', 'اگر $0\\le R.E<1\\Rightarrow\\hat{\\theta}_1$ مؤثر ہے', 'که $0\\le R.E<1\\Rightarrow\\hat{\\theta}_1$ موثر دی'),
    ('If $R.E>1\\Rightarrow\\hat{\\theta}_2$ is efficient.', 'اگر $R.E>1\\Rightarrow\\hat{\\theta}_2$ مؤثر ہے۔', 'که $R.E>1\\Rightarrow\\hat{\\theta}_2$ موثر دی.'),
])
ef = c.build('stat12-p106-efficiency', '6.2.4 Efficiency — relative efficiency', '6.2.4 کارکردگی — نسبتی کارکردگی', '6.2.4 موثریت — نسبي موثریت', 106, [204])

if __name__ == '__main__':
    save(106, [(6, ex), (6, ef)])
