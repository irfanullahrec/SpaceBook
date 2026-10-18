"""PDF91 printed 173–174: Z for the difference of means, 5.3.2 formulas, Example 5.7 setup, sample tables and 9×9 difference table."""
from class12_statistics_common import Builder, save

D = r'\overline{X}_1-\overline{X}_2'
d = r'\overline{x}_1-\overline{x}_2'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p(f'$Z=\\frac{{({D})-(\\mu_{{{d}}})}}{{\\sigma_{{{d}}}}}=\\frac{{({D})-(\\mu_1-\\mu_2)}}{{\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}}}$ (in S.W.R case)', f'$Z=\\frac{{({D})-(\\mu_{{{d}}})}}{{\\sigma_{{{d}}}}}=\\frac{{({D})-(\\mu_1-\\mu_2)}}{{\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}}}$ (S.W.R کی صورت میں)', f'$Z=\\frac{{({D})-(\\mu_{{{d}}})}}{{\\sigma_{{{d}}}}}=\\frac{{({D})-(\\mu_1-\\mu_2)}}{{\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}}}$ (د S.W.R په حالت کې)')
b.h(f'5.3.2 Formulas for $\\mu_{{{d}}}$ and $\\sigma_{{{d}}}$', f'5.3.2 $\\mu_{{{d}}}$ اور $\\sigma_{{{d}}}$ کے فارمولے', f'5.3.2 د $\\mu_{{{d}}}$ او $\\sigma_{{{d}}}$ فورمولونه')
b.mlines([rf'\mu_{{{d}}}=\Sigma({d})\,f({d})', rf'\sigma_{{{d}}}=\sqrt{{\Sigma({d})^2f({d})-[\Sigma({d})\,f({d})]^2}}'])
b.h('Example 5.7', 'مثال 5.7', 'بېلګه 5.7')
b.p('Draw all possible random samples of size $n_1=2$ with replacement from a finite population (3, 4, 5) and sample of size $n_2=2$ with replacement from another finite population (1, 1, 3).', 'ایک محدود آبادی (3، 4، 5) سے واپسی کے ساتھ $n_1=2$ سائز کے تمام ممکنہ تصادفی نمونے اور ایک اور محدود آبادی (1، 1، 3) سے واپسی کے ساتھ $n_2=2$ سائز کے نمونے نکالیں۔', 'له یوه محدود نفوس (3، 4، 5) څخه له بېرته اچولو سره د $n_1=2$ اندازې ټولې شونې تصادفي نمونې او له بل محدود نفوس (1، 1، 3) څخه له بېرته اچولو سره د $n_2=2$ اندازې نمونې راوباسئ.')
b.group('lines', [
    ('(i) Find the possible differences between the sample means drawn from the populations.', '(i) آبادیوں سے نکالے گئے نمونوں کے اوسطوں کے درمیان ممکنہ فرق معلوم کریں۔', '(i) له نفوسونو څخه د راایستل شویو نمونو د منځنیو ترمنځ شوني توپیرونه پیدا کړئ.'),
    (f'(ii) Construct the sampling distribution of ${D}$ and compute its mean and standard error.', f'(ii) ${D}$ کی نمونہ جاتی تقسیم بنائیں اور اس کا اوسط اور معیاری غلطی معلوم کریں۔', f'(ii) د ${D}$ نمونوي وېش جوړ کړئ او منځنی او معیاري تېروتنه یې محاسبه کړئ.'),
    (f'(iii) Verify that $\\mu_{{{d}}}=\\mu_1-\\mu_2$ and $\\sigma_{{{d}}}=\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}$', f'(iii) تصدیق کریں کہ $\\mu_{{{d}}}=\\mu_1-\\mu_2$ اور $\\sigma_{{{d}}}=\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}$', f'(iii) تایید کړئ چې $\\mu_{{{d}}}=\\mu_1-\\mu_2$ او $\\sigma_{{{d}}}=\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}$'),
])
b.h(*SOL)
b.table('stat12-t-ex5-7-given', ['Given', 'Population-1', 'Population-2'], [['', '[3, 4, 5]', '[1, 1, 3]'], ['', '$N_1=3$', '$N_2=3$'], ['', '$n_1=2$', '$n_2=2$']],
        ['دیا گیا', 'آبادی-1', 'آبادی-2'], ['ورکړل شوي', 'نفوس-1', 'نفوس-2'])
b.p('As the case is that of sampling with replacement therefore possible samples from population-1 are $N_1^{n_1}=3^2=9$ and population-2 are $N_2^{n_2}=3^2=9$.', 'چونکہ یہ واپسی کے ساتھ نمونہ گیری کی صورت ہے، لہٰذا آبادی-1 سے ممکنہ نمونے $N_1^{n_1}=3^2=9$ اور آبادی-2 سے $N_2^{n_2}=3^2=9$ ہیں۔', 'څرنګه چې دا له بېرته اچولو سره د نمونه اخیستنې حالت دی، نو له نفوس-1 څخه شونې نمونې $N_1^{n_1}=3^2=9$ او له نفوس-2 څخه $N_2^{n_2}=3^2=9$ دي.')
p1 = [('3, 3', '3'), ('3, 4', '3.5'), ('3, 5', '4'), ('4, 3', '3.5'), ('4, 4', '4'), ('4, 5', '4.5'), ('5, 3', '4'), ('5, 4', '4.5'), ('5, 5', '5')]
p2 = [('1, 1', '1'), ('1, 1', '1'), ('1, 3', '2'), ('1, 1', '1'), ('1, 1', '1'), ('1, 3', '2'), ('3, 1', '2'), ('3, 1', '2'), ('3, 3', '3')]
b.table('stat12-t-ex5-7-samples', ['No', 'Samples from Population-1', '$\\overline{X}_1$', 'No', 'Samples from Population-2', '$\\overline{X}_2$'],
        [[str(i + 1), a[0], a[1], str(i + 1), c[0], c[1]] for i, (a, c) in enumerate(zip(p1, p2))],
        ['نمبر', 'آبادی-1 سے نمونے', '$\\overline{X}_1$', 'نمبر', 'آبادی-2 سے نمونے', '$\\overline{X}_2$'], ['شمېره', 'له نفوس-1 نمونې', '$\\overline{X}_1$', 'شمېره', 'له نفوس-2 نمونې', '$\\overline{X}_2$'])
b.p(f'(i) The 9 × 9 = 81 possible differences ${D}$ are given in the following table', f'(i) 9 × 9 = 81 ممکنہ فرق ${D}$ درج ذیل جدول میں دیے گئے ہیں', f'(i) 9 × 9 = 81 شوني توپیرونه ${D}$ په لاندې جدول کې ورکړل شوي')
m1 = [float(v) for _, v in p1]
m2 = [float(v) for _, v in p2]
fmt = lambda v: str(int(v)) if v == int(v) else f'{v:g}'
rows = [[fmt(y)] + [fmt(xv - y) for xv in m1] for y in m2]
b.grid('stat12-t-ex5-7-diffs', ['$\\overline{X}_2\\backslash\\overline{X}_1$'] + [fmt(v) for v in m1], rows)
rec = b.build('stat12-p091-example-5-7', '5.3.2 Formulas — Example 5.7 samples and 81 differences', '5.3.2 فارمولے — مثال 5.7 نمونے اور 81 فرق', '5.3.2 فورمولونه — بېلګه 5.7 نمونې او 81 توپیرونه', 91, [173, 174])

if __name__ == '__main__':
    save(91, [(5, rec)])
