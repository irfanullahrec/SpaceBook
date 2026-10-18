"""PDF90 printed 171–172: Example 5.6 sampling distribution, results and verification; 5.3 difference between two sample means, 5.3.1 properties."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
x = r'\overline{x}'
D = r'\overline{X}_1-\overline{X}_2'
d = r'\overline{x}_1-\overline{x}_2'
b = Builder()
b.p(f'The sampling distribution of ${X}$ is', f'${X}$ کی نمونہ جاتی تقسیم یہ ہے', f'د ${X}$ نمونوي وېش دا دی')
rows = [['3', '|', '1', '1/27', '3/27', '9/27'], ['4', '|||', '3', '3/27', '12/27', '48/27'], ['5', '||||| |', '6', '6/27', '30/27', '150/27'], ['6', '||||| ||', '7', '7/27', '42/27', '252/27'],
        ['7', '||||| |', '6', '6/27', '42/27', '294/27'], ['8', '|||', '3', '3/27', '24/27', '192/27'], ['9', '|', '1', '1/27', '9/27', '81/27'], ['Total', '', '27', '1', '162/27', '1026/27']]
head = [f'${X}$', 'Tally bar', '$f$', f'$f({x})$', f'${X}f({x})$', f'${X}^2f({x})$']
b.table('stat12-t-ex5-6-dist', head, rows, [head[0], 'ٹیلی بار'] + head[2:], [head[0], 'ټلي بار'] + head[2:],
        [r if r[0] != 'Total' else ['کل'] + r[1:] for r in rows], [r if r[0] != 'Total' else ['ټول'] + r[1:] for r in rows])
b.mlines([rf'\text{{Now }}E({X})=\mu_{{{x}}}=\Sigma{x}f({x})=\frac{{162}}{{27}}=6', rf'\text{{And }}\sigma_{{{x}}}=\sqrt{{\Sigma{x}^2f({x})-[\Sigma{x}f({x})]^2}}=\sqrt{{\frac{{1026}}{{27}}-(6)^2}}=\sqrt{{38-36}}=1.4142'])
b.p('Population mean: $\\mu=\\frac{\\Sigma x}{N}=\\frac{3+6+9}{3}=\\frac{18}{3}=6$', 'آبادی کا اوسط: $\\mu=\\frac{\\Sigma x}{N}=\\frac{3+6+9}{3}=\\frac{18}{3}=6$', 'د نفوس منځنی: $\\mu=\\frac{\\Sigma x}{N}=\\frac{3+6+9}{3}=\\frac{18}{3}=6$')
b.p('Population S.D: $\\sigma=\\sqrt{\\frac{\\Sigma x^2}{N}-\\left(\\frac{\\Sigma x}{N}\\right)^2}=\\sqrt{\\frac{126}{3}-\\left(\\frac{18}{3}\\right)^2}=\\sqrt{42-36}=\\sqrt{6}=2.45$', 'آبادی کا معیاری انحراف: $\\sigma=\\sqrt{\\frac{\\Sigma x^2}{N}-\\left(\\frac{\\Sigma x}{N}\\right)^2}=\\sqrt{\\frac{126}{3}-\\left(\\frac{18}{3}\\right)^2}=\\sqrt{42-36}=\\sqrt{6}=2.45$', 'د نفوس معیاري انحراف: $\\sigma=\\sqrt{\\frac{\\Sigma x^2}{N}-\\left(\\frac{\\Sigma x}{N}\\right)^2}=\\sqrt{\\frac{126}{3}-\\left(\\frac{18}{3}\\right)^2}=\\sqrt{42-36}=\\sqrt{6}=2.45$')
b.p('Verification', 'تصدیق', 'تایید')
b.group('lines', [
    (f'(i) We see that $E({X})=\\mu=6$', f'(i) ہم دیکھتے ہیں کہ $E({X})=\\mu=6$', f'(i) وینو چې $E({X})=\\mu=6$'),
    (f'(ii) The S.E in S.W.R. case is $\\frac{{\\sigma}}{{\\sqrt{{n}}}}=\\frac{{2.45}}{{\\sqrt{{3}}}}=1.4142=\\sigma_{{{x}}}$', f'(ii) S.W.R. کی صورت میں معیاری غلطی $\\frac{{\\sigma}}{{\\sqrt{{n}}}}=\\frac{{2.45}}{{\\sqrt{{3}}}}=1.4142=\\sigma_{{{x}}}$ ہے', f'(ii) د S.W.R. په حالت کې معیاري تېروتنه $\\frac{{\\sigma}}{{\\sqrt{{n}}}}=\\frac{{2.45}}{{\\sqrt{{3}}}}=1.4142=\\sigma_{{{x}}}$ ده'),
])
ex = b.build('stat12-p090-example-5-6-dist', 'Example 5.6 — sampling distribution, mean, S.E and verification', 'مثال 5.6 — نمونہ جاتی تقسیم، اوسط، معیاری غلطی اور تصدیق', 'بېلګه 5.6 — نمونوي وېش، منځنی، معیاري تېروتنه او تایید', 90, [171])

c = Builder()
c.h('5.3 Sampling distribution of the difference between two sample means', '5.3 دو نمونوں کے اوسطوں کے فرق کی نمونہ جاتی تقسیم', '5.3 د دوو نمونو د منځنیو د توپیر نمونوي وېش')
c.p(f'The probability distribution of all possible values of ${D}$ is called sampling distributing of ${D}$. Mean of the sampling distribution of ${D}$ is denoted by $\\mu_{{{d}}}$ and S.E by $\\sigma_{{{d}}}$',
    f'${D}$ کی تمام ممکنہ قیمتوں کی احتمالی تقسیم کو ${D}$ کی نمونہ جاتی تقسیم کہتے ہیں۔ ${D}$ کی نمونہ جاتی تقسیم کے اوسط کو $\\mu_{{{d}}}$ اور معیاری غلطی کو $\\sigma_{{{d}}}$ سے ظاہر کرتے ہیں',
    f'د ${D}$ د ټولو شونو قیمتونو احتمالي وېش ته د ${D}$ نمونوي وېش وایي. د ${D}$ د نمونوي وېش منځنی په $\\mu_{{{d}}}$ او معیاري تېروتنه یې په $\\sigma_{{{d}}}$ ښودل کېږي')
c.h(f'5.3.1 Properties of the sampling distribution of ${D}$', f'5.3.1 ${D}$ کی نمونہ جاتی تقسیم کی خصوصیات', f'5.3.1 د ${D}$ د نمونوي وېش ځانګړنې')
c.p(f'(i). Mean of the sampling distribution of ${D}$ is equal to the difference in population means i.e. $\\mu_{{{d}}}=\\mu_1-\\mu_2$ (both in S.W.R and S.W.O.R)', f'(i). ${D}$ کی نمونہ جاتی تقسیم کا اوسط آبادیوں کے اوسطوں کے فرق کے برابر ہوتا ہے یعنی $\\mu_{{{d}}}=\\mu_1-\\mu_2$ (S.W.R اور S.W.O.R دونوں میں)', f'(i). د ${D}$ د نمونوي وېش منځنی د نفوسونو د منځنیو له توپیر سره برابر دی یعنې $\\mu_{{{d}}}=\\mu_1-\\mu_2$ (په دواړو S.W.R او S.W.O.R کې)')
c.p(f'(ii). Standard error of the sampling distribution of ${D}$ is', f'(ii). ${D}$ کی نمونہ جاتی تقسیم کی معیاری غلطی یہ ہے', f'(ii). د ${D}$ د نمونوي وېش معیاري تېروتنه دا ده')
c.group('lines', [
    (f'$\\sigma_{{{d}}}=\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}$ (in case of S.W.R)', f'$\\sigma_{{{d}}}=\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}$ (S.W.R کی صورت میں)', f'$\\sigma_{{{d}}}=\\sqrt{{\\frac{{\\sigma_1^2}}{{n_1}}+\\frac{{\\sigma_2^2}}{{n_2}}}}$ (د S.W.R په حالت کې)'),
    ('$=\\sqrt{\\frac{\\sigma_1^2}{n_1}\\frac{N_1-n_1}{n_1-1}+\\frac{\\sigma_2^2}{n_2}\\frac{N_2-n_2}{n_2-1}}$ (in case of S.W.O.R)', '$=\\sqrt{\\frac{\\sigma_1^2}{n_1}\\frac{N_1-n_1}{n_1-1}+\\frac{\\sigma_2^2}{n_2}\\frac{N_2-n_2}{n_2-1}}$ (S.W.O.R کی صورت میں)', '$=\\sqrt{\\frac{\\sigma_1^2}{n_1}\\frac{N_1-n_1}{n_1-1}+\\frac{\\sigma_2^2}{n_2}\\frac{N_2-n_2}{n_2-1}}$ (د S.W.O.R په حالت کې)'),
])
c.p(f'(iii). Shape of the sampling distribution of ${D}$', f'(iii). ${D}$ کی نمونہ جاتی تقسیم کی شکل', f'(iii). د ${D}$ د نمونوي وېش بڼه')
c.p('There are two cases:', 'دو صورتیں ہیں:', 'دوه حالتونه دي:')
c.group('lines', [
    (f'a) If the sampled population is normal, then sampling distribution of ${D}$ will also be normal irrespective of the samples size.', f'a) اگر نمونہ لی گئی آبادی نارمل ہو تو ${D}$ کی نمونہ جاتی تقسیم بھی نمونوں کے سائز سے قطع نظر نارمل ہوگی۔', f'a) که نمونه ترې اخیستل شوی نفوس نورمال وي، نو د ${D}$ نمونوي وېش به هم د نمونو له اندازې پرته نورمال وي.'),
    (f'b) If the sampled population is non-normal, then according to central limit theorem, sampling distribution of ${D}$ will approximately be normal provided $n_1$ and $n_2$ both are large.', f'b) اگر نمونہ لی گئی آبادی غیر نارمل ہو تو مرکزی حدی مسئلے کے مطابق ${D}$ کی نمونہ جاتی تقسیم تقریباً نارمل ہوگی بشرطیکہ $n_1$ اور $n_2$ دونوں بڑے ہوں۔', f'b) که نمونه ترې اخیستل شوی نفوس غیر نورمال وي، نو د مرکزي حد د قضیې له مخې د ${D}$ نمونوي وېش به نږدې نورمال وي په دې شرط چې $n_1$ او $n_2$ دواړه لوی وي.'),
])
c.p(f'The variable ${D}$ in standard units is written as', f'متغیر ${D}$ معیاری اکائیوں میں یوں لکھا جاتا ہے', f'متغیر ${D}$ په معیاري واحدونو کې داسې لیکل کېږي')
dm = c.build('stat12-p090-difference-means', '5.3 Sampling distribution of the difference between two sample means', '5.3 دو نمونوں کے اوسطوں کے فرق کی نمونہ جاتی تقسیم', '5.3 د دوو نمونو د منځنیو د توپیر نمونوي وېش', 90, [172])
issues = [{'id': 'stat12-p172-fpc-denominator', 'unit': 5, 'printedPage': 172, 'description': 'The printed S.W.O.R standard-error formula uses (n₁−1), (n₂−1) in the correction factors instead of (N₁−1), (N₂−1); printed formula retained. Also “sampling distributing of” (for distribution).'}]

if __name__ == '__main__':
    save(90, [(5, ex), (5, dm)], issues=issues)
