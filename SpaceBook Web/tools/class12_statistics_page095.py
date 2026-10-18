"""PDF95 printed 181–182: Example 5.9 setup, sample tables for both populations and 9×9 table of p̂1 − p̂2."""
from fractions import Fraction
from class12_statistics_common import Builder, save

DP = r'\hat{p}_1-\hat{p}_2'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p(f'sampling distribution of the difference between the sample proportions ${DP}$ and verify that $\\mu_{{{DP}}}=p_1-p_2$ and $\\sigma_{{{DP}}}=\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}$',
    f'نمونوں کے تناسبوں کے فرق ${DP}$ کی نمونہ جاتی تقسیم بنائیں اور تصدیق کریں کہ $\\mu_{{{DP}}}=p_1-p_2$ اور $\\sigma_{{{DP}}}=\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}$',
    f'د نمونو د تناسبونو د توپیر ${DP}$ نمونوي وېش جوړ کړئ او تایید کړئ چې $\\mu_{{{DP}}}=p_1-p_2$ او $\\sigma_{{{DP}}}=\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}$')
b.h(*SOL)
b.table('stat12-t-ex5-9-given', ['Given', 'population-1', 'population-2'], [['', '[7, 8, 9]', '[4, 5, 5]'], ['', '$N_1=3$', '$N_2=3$'], ['', '$n_1=2$', '$n_2=2$']],
        ['دیا گیا', 'آبادی-1', 'آبادی-2'], ['ورکړل شوي', 'نفوس-1', 'نفوس-2'])
b.p('Since sampling is with replacement, therefore, possible samples are $N_1^{n_1}=3^2=9$, $N_2^{n_2}=3^2=9$', 'چونکہ نمونہ گیری واپسی کے ساتھ ہے، لہٰذا ممکنہ نمونے $N_1^{n_1}=3^2=9$، $N_2^{n_2}=3^2=9$ ہیں', 'څرنګه چې نمونه اخیستنه له بېرته اچولو سره ده، نو شونې نمونې $N_1^{n_1}=3^2=9$، $N_2^{n_2}=3^2=9$ دي')
pop1 = [7, 8, 9]
pop2 = [4, 5, 5]
s1 = [(a, c) for a in pop1 for c in pop1]
s2 = [(a, c) for a in pop2 for c in pop2]
f1 = [Fraction(sum(1 for v in s if v % 2 == 0), 2) for s in s1]
f2 = [Fraction(sum(1 for v in s if v % 2 == 1), 2) for s in s2]
fs = lambda f: '0' if f == 0 else ('1' if f == 1 else ('−1' if f == -1 else (f'−{-f.numerator}/{f.denominator}' if f < 0 else f'{f.numerator}/{f.denominator}')))
b.table('stat12-t-ex5-9-samples', ['No', 'Samples (Population-1)', '$\\hat{p}_1$', 'No', 'Samples (Population-2)', '$\\hat{p}_2$'],
        [[str(i + 1), f'({a[0]}, {a[1]})', fs(p1), str(i + 1), f'({c[0]}, {c[1]})', fs(p2)] for i, (a, p1, c, p2) in enumerate(zip(s1, f1, s2, f2))],
        ['نمبر', 'نمونے (آبادی-1)', '$\\hat{p}_1$', 'نمبر', 'نمونے (آبادی-2)', '$\\hat{p}_2$'], ['شمېره', 'نمونې (نفوس-1)', '$\\hat{p}_1$', 'شمېره', 'نمونې (نفوس-2)', '$\\hat{p}_2$'])
b.p('Now 9 × 9 = 81 possible differences are given in the following table.', 'اب 9 × 9 = 81 ممکنہ فرق درج ذیل جدول میں دیے گئے ہیں۔', 'اوس 9 × 9 = 81 شوني توپیرونه په لاندې جدول کې ورکړل شوي.')
rows = [[fs(q)] + [fs(p - q) for p in f1] for q in f2]
b.grid('stat12-t-ex5-9-diffs', ['$\\hat{p}_2\\backslash\\hat{p}_1$'] + [fs(p) for p in f1], rows)
rec = b.build('stat12-p095-example-5-9', 'Example 5.9 — samples and 81 differences of proportions', 'مثال 5.9 — نمونے اور تناسبوں کے 81 فرق', 'بېلګه 5.9 — نمونې او د تناسبونو 81 توپیرونه', 95, [181, 182])
issues = [{'id': 'stat12-p181-pop2-sample-order', 'unit': 5, 'printedPage': 181, 'description': 'The printed population-2 sample list orders samples 4–9 as (5,4),(5,5),(5,5),(5,4),(5,5),(5,5); the table here lists the 9 with-replacement pairs in systematic order (4,4),(4,5),(4,5),(5,4),(5,5),(5,5),(5,4),(5,5),(5,5), giving the same p̂₂ values row by row as printed.'}]

if __name__ == '__main__':
    save(95, [(5, rec)], issues=issues)
