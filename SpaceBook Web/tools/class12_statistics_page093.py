"""PDF93 printed 177–178: 5.4.2 properties of the sampling distribution of p̂, 5.4.3 formulas, Example 5.8 (20 samples, distribution)."""
from itertools import combinations
from fractions import Fraction
from class12_statistics_common import Builder, save

P = r'\hat{p}'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h(f'5.4.2 Properties of the sampling distribution of ${P}$', f'5.4.2 ${P}$ کی نمونہ جاتی تقسیم کی خصوصیات', f'5.4.2 د ${P}$ د نمونوي وېش ځانګړنې')
b.p(f'(i). Mean of the sampling distribution of sample proportion is always equal to the population proportion i.e. $\\mu_{{{P}}}=p$ (both in S.W.R and S.W.O.R cases)', f'(i). نمونے کے تناسب کی نمونہ جاتی تقسیم کا اوسط ہمیشہ آبادی کے تناسب کے برابر ہوتا ہے یعنی $\\mu_{{{P}}}=p$ (S.W.R اور S.W.O.R دونوں صورتوں میں)', f'(i). د نمونې د تناسب د نمونوي وېش منځنی تل د نفوس له تناسب سره برابر دی یعنې $\\mu_{{{P}}}=p$ (په دواړو S.W.R او S.W.O.R حالتونو کې)')
b.p(f'(ii). S.E of the sampling distribution of ${P}$ is:', f'(ii). ${P}$ کی نمونہ جاتی تقسیم کی معیاری غلطی یہ ہے:', f'(ii). د ${P}$ د نمونوي وېش معیاري تېروتنه دا ده:')
b.group('lines', [
    (f'$\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}}}$, q=1−p (in case of S.W.R)', f'$\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}}}$، q=1−p (S.W.R کی صورت میں)', f'$\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}}}$، q=1−p (د S.W.R په حالت کې)'),
    (f'$\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}\\frac{{N-n}}{{N-1}}}}$ (in case S.W.O.R)', f'$\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}\\frac{{N-n}}{{N-1}}}}$ (S.W.O.R کی صورت میں)', f'$\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}\\frac{{N-n}}{{N-1}}}}$ (د S.W.O.R په حالت کې)'),
])
b.p(f'Note that if p is unknown and n is large, then $\\sigma_{{{P}}}$ can be estimated by $S_{{{P}}}=\\sqrt{{\\frac{{{P}\\hat{{q}}}}{{n}}}}$.', f'نوٹ کریں کہ اگر p نامعلوم ہو اور n بڑا ہو تو $\\sigma_{{{P}}}$ کا تخمین $S_{{{P}}}=\\sqrt{{\\frac{{{P}\\hat{{q}}}}{{n}}}}$ سے لگایا جا سکتا ہے۔', f'پام وکړئ چې که p نامعلوم وي او n لوی وي، نو $\\sigma_{{{P}}}$ په $S_{{{P}}}=\\sqrt{{\\frac{{{P}\\hat{{q}}}}{{n}}}}$ اټکل کېدای شي.')
b.p(f'(iii). Shape of the sampling distribution of ${P}$', f'(iii). ${P}$ کی نمونہ جاتی تقسیم کی شکل', f'(iii). د ${P}$ د نمونوي وېش بڼه')
b.p(f'For small n, its shape will be like binomial distribution but for sufficiently large sample sizes, the shape of the sampling distribution of ${P}$ will be approximately normal.', f'چھوٹے n کے لیے اس کی شکل دو رقمی تقسیم جیسی ہوگی لیکن کافی بڑے نمونوں کے لیے ${P}$ کی نمونہ جاتی تقسیم کی شکل تقریباً نارمل ہوگی۔', f'د کوچني n لپاره به بڼه یې د بینومیل وېش په څېر وي خو د کافي لویو نمونو لپاره به د ${P}$ د نمونوي وېش بڼه نږدې نورماله وي.')
b.p(f'The variable ${P}$ can be standardized as $Z=\\frac{{{P}-\\mu_{{{P}}}}}{{\\sigma_{{{P}}}}}=\\frac{{{P}-p}}{{\\sqrt{{\\frac{{pq}}{{n}}}}}}$ (in S.W.R case)', f'متغیر ${P}$ کو یوں معیاری بنایا جا سکتا ہے $Z=\\frac{{{P}-\\mu_{{{P}}}}}{{\\sigma_{{{P}}}}}=\\frac{{{P}-p}}{{\\sqrt{{\\frac{{pq}}{{n}}}}}}$ (S.W.R کی صورت میں)', f'متغیر ${P}$ داسې معیاري کېدای شي $Z=\\frac{{{P}-\\mu_{{{P}}}}}{{\\sigma_{{{P}}}}}=\\frac{{{P}-p}}{{\\sqrt{{\\frac{{pq}}{{n}}}}}}$ (د S.W.R په حالت کې)')
b.h(f'5.4.3 Formulas for $\\mu_{{{P}}}$ and $\\sigma_{{{P}}}$.', f'5.4.3 $\\mu_{{{P}}}$ اور $\\sigma_{{{P}}}$ کے فارمولے۔', f'5.4.3 د $\\mu_{{{P}}}$ او $\\sigma_{{{P}}}$ فورمولونه.')
b.group('lines', [
    (f'Mean $E({P})=\\mu_{{{P}}}=\\Sigma{P}f({P})$', f'اوسط $E({P})=\\mu_{{{P}}}=\\Sigma{P}f({P})$', f'منځنی $E({P})=\\mu_{{{P}}}=\\Sigma{P}f({P})$'),
    (f'S.E $\\sigma_{{{P}}}=\\sqrt{{\\Sigma{P}^2f({P})-[\\Sigma{P}f({P})]^2}}$', f'معیاری غلطی $\\sigma_{{{P}}}=\\sqrt{{\\Sigma{P}^2f({P})-[\\Sigma{P}f({P})]^2}}$', f'معیاري تېروتنه $\\sigma_{{{P}}}=\\sqrt{{\\Sigma{P}^2f({P})-[\\Sigma{P}f({P})]^2}}$'),
])
props = b.build('stat12-p093-proportion-properties', '5.4.2–5.4.3 Properties and formulas of the sampling distribution of p̂', '5.4.2–5.4.3 p̂ کی نمونہ جاتی تقسیم کی خصوصیات اور فارمولے', '5.4.2–5.4.3 د p̂ د نمونوي وېش ځانګړنې او فورمولونه', 93, [177])

c = Builder()
c.h('Example 5.8', 'مثال 5.8', 'بېلګه 5.8')
c.p('Draw all possible samples of size n = 3 without replacement from the population consists of six numbers 3, 4, 5, 6, 7, 8 and find the proportion of even numbers in the samples. Construct the sampling distribution of sample proportion and verify that;', 'چھ اعداد 3، 4، 5، 6، 7، 8 پر مشتمل آبادی سے بغیر واپسی کے n = 3 سائز کے تمام ممکنہ نمونے نکالیں اور نمونوں میں جفت اعداد کا تناسب معلوم کریں۔ نمونے کے تناسب کی نمونہ جاتی تقسیم بنائیں اور تصدیق کریں کہ؛', 'له شپږو عددونو 3، 4، 5، 6، 7، 8 جوړ نفوس څخه پرته له بېرته اچولو د n = 3 اندازې ټولې شونې نمونې راوباسئ او په نمونو کې د جفت عددونو تناسب پیدا کړئ. د نمونې د تناسب نمونوي وېش جوړ کړئ او تایید کړئ چې؛')
c.group('lines', [(f'(a) $\\mu_{{{P}}}=p$',) * 3, (f'(b) $\\sigma_{{{P}}}=\\sqrt{{\\frac{{pq}}{{n}}\\frac{{N-n}}{{N-1}}}}$',) * 3])
c.h(*SOL)
c.p('The number of possible samples of size 3 in without replacement case are ${}^{6}_{3}C=20$. The samples and the proportion of even numbers in the samples are:', 'بغیر واپسی کی صورت میں 3 سائز کے ممکنہ نمونوں کی تعداد ${}^{6}_{3}C=20$ ہے۔ نمونے اور ان میں جفت اعداد کا تناسب یہ ہیں:', 'پرته له بېرته اچولو په حالت کې د 3 اندازې د شونو نمونو شمېر ${}^{6}_{3}C=20$ دی. نمونې او په هغو کې د جفت عددونو تناسب دا دي:')
samples = list(combinations([3, 4, 5, 6, 7, 8], 3))
frac = lambda s: Fraction(sum(1 for v in s if v % 2 == 0), 3)
fs = lambda f: '0' if f == 0 else '1' if f == 1 else f'{f.numerator}/{f.denominator}'
cells = [(str(i + 1), ', '.join(map(str, s)), fs(frac(s))) for i, s in enumerate(samples)]
rows = []
for r in range(7):
    row = []
    for blk in range(3):
        k = blk * 7 + r
        row += list(cells[k]) if k < 20 else ['', '', '']
    rows.append(row)
H = ['S.No.', 'Samples', f'${P}$'] * 3
c.table('stat12-t-ex5-8-samples', H, rows, ['نمبر شمار', 'نمونے', f'${P}$'] * 3, ['شمېره', 'نمونې', f'${P}$'] * 3)
c.p(f'The sampling distribution of ${P}$', f'${P}$ کی نمونہ جاتی تقسیم', f'د ${P}$ نمونوي وېش')
c.grid('stat12-t-ex5-8-dist', [f'${P}$', '$f$', f'$f({P})$', f'${P}f({P})$', f'${P}^2f({P})$'],
       [['0', '1', '1/20', '0', '0'], ['1/3', '9', '9/20', '3/20', '1/20'], ['2/3', '9', '9/20', '6/20', '4/20'], ['1', '1', '1/20', '1/20', '1/20'], ['Total', '20', '1', '10/20', '6/20']])
ex = c.build('stat12-p093-example-5-8', 'Example 5.8 — proportion of even numbers in samples of size 3', 'مثال 5.8 — 3 سائز کے نمونوں میں جفت اعداد کا تناسب', 'بېلګه 5.8 — د 3 اندازې په نمونو کې د جفت عددونو تناسب', 93, [178])

if __name__ == '__main__':
    save(93, [(5, props), (5, ex)])
