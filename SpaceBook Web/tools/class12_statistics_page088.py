"""PDF88 printed 167–168: Example 5.4 results and verification; Example 5.5 (S.W.O.R) question, population mean/SD and 15-sample table."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
x = r'\overline{x}'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([rf'\text{{Mean}}=\mu_{{{x}}}=\Sigma{x}f({x})=\frac{{72}}{{16}}=4.5', rf'S.E=\sigma_{{{x}}}=\sqrt{{\Sigma{x}^2f({x})-[\Sigma{x}f({x})]^2}}', r'=\sqrt{\frac{378}{16}-\left(\frac{72}{16}\right)^2}', r'=\sqrt{23.625-20.25}=\sqrt{3.375}=1.84'])
b.p('(v) Verification:', '(v) تصدیق:', '(v) تایید:')
b.p(f'(a) As μ = 4.5 and $\\mu_{{{x}}}=4.5$, hence the property $\\mu_{{{x}}}=\\mu$ is satisfied i.e. mean of all sixteen sample means is equal to the population mean.', f'(a) چونکہ μ = 4.5 اور $\\mu_{{{x}}}=4.5$، لہٰذا خاصیت $\\mu_{{{x}}}=\\mu$ پوری ہوتی ہے یعنی تمام سولہ نمونوں کے اوسطوں کا اوسط آبادی کے اوسط کے برابر ہے۔', f'(a) څرنګه چې μ = 4.5 او $\\mu_{{{x}}}=4.5$، نو ځانګړنه $\\mu_{{{x}}}=\\mu$ پوره کېږي یعنې د ټولو شپاړسو نمونو د منځنیو منځنی د نفوس له منځني سره برابر دی.')
b.p('(b) By property S.E in S.W.R case is', '(b) خاصیت کے مطابق S.W.R کی صورت میں معیاری غلطی یہ ہے', '(b) د ځانګړنې له مخې د S.W.R په حالت کې معیاري تېروتنه دا ده')
b.p(f'$\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}=\\frac{{2.598}}{{\\sqrt{{2}}}}=\\frac{{2.598}}{{1.414}}=1.84$. It is same as the computed S.E', f'$\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}=\\frac{{2.598}}{{\\sqrt{{2}}}}=\\frac{{2.598}}{{1.414}}=1.84$۔ یہ معلوم کی گئی معیاری غلطی کے برابر ہے', f'$\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}=\\frac{{2.598}}{{\\sqrt{{2}}}}=\\frac{{2.598}}{{1.414}}=1.84$. دا د محاسبه شوې معیاري تېروتنې سره یو شان ده')
b.p(f'We learnt that if population mean and standard deviation are known, then it is easy to compute $\\mu_{{{x}}}$ and $\\sigma_{{{x}}}$ by property. If σ is unknown and n is large then $\\sigma_{{{x}}}$ can be estimated by $s_{{{x}}}=\\frac{{s}}{{\\sqrt{{n}}}}$, where s is sample standard deviation.',
    f'ہم نے سیکھا کہ اگر آبادی کا اوسط اور معیاری انحراف معلوم ہوں تو خاصیت کے ذریعے $\\mu_{{{x}}}$ اور $\\sigma_{{{x}}}$ معلوم کرنا آسان ہے۔ اگر σ نامعلوم ہو اور n بڑا ہو تو $\\sigma_{{{x}}}$ کا تخمین $s_{{{x}}}=\\frac{{s}}{{\\sqrt{{n}}}}$ سے لگایا جا سکتا ہے، جہاں s نمونے کا معیاری انحراف ہے۔',
    f'زده مو کړل چې که د نفوس منځنی او معیاري انحراف معلوم وي، نو د ځانګړنې له لارې د $\\mu_{{{x}}}$ او $\\sigma_{{{x}}}$ محاسبه اسانه ده. که σ نامعلوم وي او n لوی وي، نو $\\sigma_{{{x}}}$ په $s_{{{x}}}=\\frac{{s}}{{\\sqrt{{n}}}}$ اټکل کېدای شي، چې s د نمونې معیاري انحراف دی.')
ex4 = b.build('stat12-p088-example-5-4-results', 'Example 5.4 — mean, S.E and verification', 'مثال 5.4 — اوسط، معیاری غلطی اور تصدیق', 'بېلګه 5.4 — منځنی، معیاري تېروتنه او تایید', 88, [167])

c = Builder()
c.h('Example 5.5', 'مثال 5.5', 'بېلګه 5.5')
c.p('A population consists of number 2, 4, 8, 8, 10, 10. Samples of size 2 are to be drawn without replacement from this population.', 'ایک آبادی اعداد 2، 4، 8، 8، 10، 10 پر مشتمل ہے۔ اس آبادی سے بغیر واپسی کے 2 کے سائز کے نمونے نکالے جانے ہیں۔', 'یو نفوس له 2، 4، 8، 8، 10، 10 عددونو جوړ دی. له دې نفوس څخه پرته له بېرته اچولو د 2 اندازې نمونې راایستل کېږي.')
c.group('lines', [
    ('(i) Find mean and S.D of this population.', '(i) اس آبادی کا اوسط اور معیاری انحراف معلوم کریں۔', '(i) د دې نفوس منځنی او معیاري انحراف پیدا کړئ.'),
    (f'(ii) Construct the sampling distribution of ${X}$', f'(ii) ${X}$ کی نمونہ جاتی تقسیم بنائیں', f'(ii) د ${X}$ نمونوي وېش جوړ کړئ'),
    (f'(iii) Verify that $E({X})=\\mu$ and $\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}\\sqrt{{\\frac{{N-n}}{{N-1}}}}$', f'(iii) تصدیق کریں کہ $E({X})=\\mu$ اور $\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}\\sqrt{{\\frac{{N-n}}{{N-1}}}}$', f'(iii) تایید کړئ چې $E({X})=\\mu$ او $\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}\\sqrt{{\\frac{{N-n}}{{N-1}}}}$'),
])
c.h(*SOL)
c.p('Given population is 2, 4, 8, 8, 10, 10', 'دی گئی آبادی 2، 4، 8، 8، 10، 10 ہے', 'ورکړل شوی نفوس 2، 4، 8، 8، 10، 10 دی')
c.p('Here N = 6, n = 2', 'یہاں N = 6، n = 2', 'دلته N = 6، n = 2')
c.mlines([r'(i)\quad\mu=\frac{\Sigma x}{N}=\frac{2+4+8+8+10+10}{6}=\frac{42}{6}=7', r'\sigma=\sqrt{\frac{\Sigma x^2}{N}-\left(\frac{\Sigma x}{N}\right)^2}=\sqrt{\frac{348}{6}-\left(\frac{42}{6}\right)^2}=\sqrt{58-49}=\sqrt{9}=3'])
c.p('(iii) Possible samples that could be drawn without replacement $={}^{6}_{2}C=15$', '(iii) بغیر واپسی کے نکالے جا سکنے والے ممکنہ نمونے $={}^{6}_{2}C=15$', '(iii) هغه شونې نمونې چې پرته له بېرته اچولو راایستل کېدای شي $={}^{6}_{2}C=15$')
rows = [['1', '2, 4', '3', '9', '4, 10', '7'], ['2', '2, 8', '5', '10', '8, 8', '8'], ['3', '2, 8', '5', '11', '8, 10', '9'], ['4', '2, 10', '6', '12', '8, 10', '9'],
        ['5', '2, 10', '6', '13', '8, 10', '9'], ['6', '4, 8', '6', '14', '8, 10', '9'], ['7', '4, 8', '6', '15', '10, 10', '10'], ['8', '4, 10', '7', '', '', '']]
c.table('stat12-t-ex5-5-samples', ['S.No.', 'Samples', f'${X}$', 'S.No.', 'Samples', f'${X}$'], rows,
        ['نمبر شمار', 'نمونے', f'${X}$', 'نمبر شمار', 'نمونے', f'${X}$'], ['شمېره', 'نمونې', f'${X}$', 'شمېره', 'نمونې', f'${X}$'])
ex5 = c.build('stat12-p088-example-5-5', 'Example 5.5 — sampling without replacement: population and 15 samples', 'مثال 5.5 — بغیر واپسی کے نمونہ گیری: آبادی اور 15 نمونے', 'بېلګه 5.5 — پرته له بېرته اچولو نمونه اخیستنه: نفوس او 15 نمونې', 88, [167, 168])
issues = [{'id': 'stat12-p168-ex55-part-label', 'unit': 5, 'printedPage': 168, 'description': 'Example 5.5 solution labels the sample-listing step “(iii)”; the question numbers the distribution as (ii). Printed label retained.'}]

if __name__ == '__main__':
    save(88, [(5, ex4), (5, ex5)], issues=issues)
