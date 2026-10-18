"""PDF94 printed 179–180: Example 5.8 results and verification; 5.5 difference between two sample proportions, 5.5.1 properties, 5.5.2 formulas, Example 5.9 question (start)."""
from class12_statistics_common import Builder, save

P = r'\hat{p}'
DP = r'\hat{p}_1-\hat{p}_2'
b = Builder()
b.mlines([rf'E({P})=\mu_{{{P}}}=\Sigma{P}f({P})=\frac{{10}}{{20}}=0.5', rf'\sigma_{{{P}}}=\sqrt{{\Sigma{P}^2f({P})-[\Sigma{P}f({P})]^2}}', r'=\sqrt{\frac{6}{20}-\left(\frac{10}{20}\right)^2}=\sqrt{0.3-0.25}=\sqrt{0.05}=0.22'])
b.p('Verification:', 'تصدیق:', 'تایید:')
b.p('(i) As even numbers in the population are 3 therefore,', '(i) چونکہ آبادی میں جفت اعداد 3 ہیں، لہٰذا', '(i) څرنګه چې په نفوس کې جفت عددونه 3 دي، نو')
b.p(f'$p=\\frac{{X}}{{N}}=\\frac{{3}}{{6}}=\\frac{{1}}{{2}}=0.5$, hence proved that $\\mu_{{{P}}}=p$', f'$p=\\frac{{X}}{{N}}=\\frac{{3}}{{6}}=\\frac{{1}}{{2}}=0.5$، لہٰذا ثابت ہوا کہ $\\mu_{{{P}}}=p$', f'$p=\\frac{{X}}{{N}}=\\frac{{3}}{{6}}=\\frac{{1}}{{2}}=0.5$، نو ثابته شوه چې $\\mu_{{{P}}}=p$')
b.p('(ii) S.E in without replacement case by property is', '(ii) خاصیت کے مطابق بغیر واپسی کی صورت میں معیاری غلطی یہ ہے', '(ii) د ځانګړنې له مخې پرته له بېرته اچولو په حالت کې معیاري تېروتنه دا ده')
b.eq(rf'\sigma_{{{P}}}=\sqrt{{\frac{{pq}}{{n}}\frac{{N-n}}{{N-1}}}}=\sqrt{{\frac{{(0.5)(0.5)}}{{3}}\cdot\frac{{6-3}}{{6-1}}}}=\sqrt{{\frac{{0.75}}{{15}}}}=\sqrt{{0.05}}=0.22')
b.p(f'This is same as computed value of $\\sigma_{{{P}}}$', f'یہ $\\sigma_{{{P}}}$ کی معلوم کی گئی قیمت کے برابر ہے', f'دا د $\\sigma_{{{P}}}$ د محاسبه شوي قیمت سره یو شان ده')
ex = b.build('stat12-p094-example-5-8-results', 'Example 5.8 — mean, S.E and verification', 'مثال 5.8 — اوسط، معیاری غلطی اور تصدیق', 'بېلګه 5.8 — منځنی، معیاري تېروتنه او تایید', 94, [179])

c = Builder()
c.h('5.5 Sampling distribution of difference between two sample proportions', '5.5 دو نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم', '5.5 د دوو نمونو د تناسبونو د توپیر نمونوي وېش')
c.p(f'The probability distribution of all possible values of ${DP}$ is called sampling distribution of ${DP}$. Its mean is denoted by $E({DP})=\\mu_{{{DP}}}$ and S.E by $\\sigma_{{{DP}}}$', f'${DP}$ کی تمام ممکنہ قیمتوں کی احتمالی تقسیم کو ${DP}$ کی نمونہ جاتی تقسیم کہتے ہیں۔ اس کے اوسط کو $E({DP})=\\mu_{{{DP}}}$ اور معیاری غلطی کو $\\sigma_{{{DP}}}$ سے ظاہر کرتے ہیں', f'د ${DP}$ د ټولو شونو قیمتونو احتمالي وېش ته د ${DP}$ نمونوي وېش وایي. منځنی یې په $E({DP})=\\mu_{{{DP}}}$ او معیاري تېروتنه یې په $\\sigma_{{{DP}}}$ ښودل کېږي')
c.h('5.5.1 Properties of the sampling distribution of difference between two sample proportions', '5.5.1 دو نمونوں کے تناسبوں کے فرق کی نمونہ جاتی تقسیم کی خصوصیات', '5.5.1 د دوو نمونو د تناسبونو د توپیر د نمونوي وېش ځانګړنې')
c.p(f'(i). Mean of the sampling distribution of ${DP}$ is equal to the difference between the population proportions i.e.', f'(i). ${DP}$ کی نمونہ جاتی تقسیم کا اوسط آبادیوں کے تناسبوں کے فرق کے برابر ہوتا ہے یعنی', f'(i). د ${DP}$ د نمونوي وېش منځنی د نفوسونو د تناسبونو له توپیر سره برابر دی یعنې')
c.p(f'$\\mu_{{{DP}}}=p_1-p_2$ (both in S.W.R and S.W.O.R)', f'$\\mu_{{{DP}}}=p_1-p_2$ (S.W.R اور S.W.O.R دونوں میں)', f'$\\mu_{{{DP}}}=p_1-p_2$ (په دواړو S.W.R او S.W.O.R کې)')
c.p(f'(ii). S.E of the sampling distribution of ${DP}$ is', f'(ii). ${DP}$ کی نمونہ جاتی تقسیم کی معیاری غلطی یہ ہے', f'(ii). د ${DP}$ د نمونوي وېش معیاري تېروتنه دا ده')
c.group('lines', [
    (f'$\\sigma_{{{DP}}}=\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}$ (S.W.R case)', f'$\\sigma_{{{DP}}}=\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}$ (S.W.R کی صورت)', f'$\\sigma_{{{DP}}}=\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}$ (د S.W.R حالت)'),
    ('$=\\sqrt{\\frac{p_1q_1}{n_1}\\frac{N_1-n_1}{N_1-1}+\\frac{p_2q_2}{n_2}\\frac{N_2-n_2}{N_2-1}}$ (S.W.O.R case)', '$=\\sqrt{\\frac{p_1q_1}{n_1}\\frac{N_1-n_1}{N_1-1}+\\frac{p_2q_2}{n_2}\\frac{N_2-n_2}{N_2-1}}$ (S.W.O.R کی صورت)', '$=\\sqrt{\\frac{p_1q_1}{n_1}\\frac{N_1-n_1}{N_1-1}+\\frac{p_2q_2}{n_2}\\frac{N_2-n_2}{N_2-1}}$ (د S.W.O.R حالت)'),
])
c.p(f'If $p_1\\neq p_2$ and also unknown, then for large $n_1$, $n_2$ they are replaced with the sample proportions $\\hat{{p}}_1$ and $\\hat{{p}}_2$ respectively. The $\\sigma_{{{DP}}}$ is then estimated by', f'اگر $p_1\\neq p_2$ اور نامعلوم بھی ہوں تو بڑے $n_1$، $n_2$ کے لیے انہیں بالترتیب نمونوں کے تناسبوں $\\hat{{p}}_1$ اور $\\hat{{p}}_2$ سے بدل دیا جاتا ہے۔ پھر $\\sigma_{{{DP}}}$ کا تخمین اس سے لگایا جاتا ہے', f'که $p_1\\neq p_2$ او نامعلوم هم وي، نو د لویو $n_1$، $n_2$ لپاره په ترتیب سره د نمونو په تناسبونو $\\hat{{p}}_1$ او $\\hat{{p}}_2$ بدلېږي. بیا $\\sigma_{{{DP}}}$ په دې اټکل کېږي')
c.eq(rf'S_{{{DP}}}=\sqrt{{\frac{{\hat{{p}}_1\hat{{q}}_1}}{{n_1}}+\frac{{\hat{{p}}_2\hat{{q}}_2}}{{n_2}}}}')
c.p(f'(iii). Shape of the sampling distribution of ${DP}$.', f'(iii). ${DP}$ کی نمونہ جاتی تقسیم کی شکل۔', f'(iii). د ${DP}$ د نمونوي وېش بڼه.')
c.p(f'For sufficiently large $n_1$ and $n_2$ the sampling distribution of ${DP}$ is approximately normal.', f'کافی بڑے $n_1$ اور $n_2$ کے لیے ${DP}$ کی نمونہ جاتی تقسیم تقریباً نارمل ہوتی ہے۔', f'د کافي لویو $n_1$ او $n_2$ لپاره د ${DP}$ نمونوي وېش نږدې نورمال وي.')
c.p(f'The variable ${DP}$ in standard form is written as', f'متغیر ${DP}$ معیاری شکل میں یوں لکھا جاتا ہے', f'متغیر ${DP}$ په معیاري بڼه داسې لیکل کېږي')
c.p(f'$Z=\\frac{{({DP})-\\mu_{{{DP}}}}}{{\\sigma_{{{DP}}}}}=\\frac{{({DP})-(p_1-p_2)}}{{\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}}}$ (in S.W.R case)', f'$Z=\\frac{{({DP})-\\mu_{{{DP}}}}}{{\\sigma_{{{DP}}}}}=\\frac{{({DP})-(p_1-p_2)}}{{\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}}}$ (S.W.R کی صورت میں)', f'$Z=\\frac{{({DP})-\\mu_{{{DP}}}}}{{\\sigma_{{{DP}}}}}=\\frac{{({DP})-(p_1-p_2)}}{{\\sqrt{{\\frac{{p_1q_1}}{{n_1}}+\\frac{{p_2q_2}}{{n_2}}}}}}$ (د S.W.R په حالت کې)')
c.h(f'5.5.2 Formulas for mean and S.E of the sampling distribution of ${DP}$', f'5.5.2 ${DP}$ کی نمونہ جاتی تقسیم کے اوسط اور معیاری غلطی کے فارمولے', f'5.5.2 د ${DP}$ د نمونوي وېش د منځني او معیاري تېروتنې فورمولونه')
c.mlines([rf'\mu_{{{DP}}}=\Sigma({DP})\,f({DP})', rf'\sigma_{{{DP}}}=\sqrt{{\Sigma({DP})^2f({DP})-[\Sigma({DP})\,f({DP})]^2}}'])
c.h('Example 5.9', 'مثال 5.9', 'بېلګه 5.9')
c.p('Let $\\hat{p}_1$ represent the proportion of even numbers in samples of size $n_1=2$ drawn with replacement from a finite population consisting units 7, 8, 9. Let $\\hat{p}_2$ represent the proportion of odd numbers in samples of size $n_2=2$ selected with replacement from another finite population having units 4, 5, and 5. Construct the',
    'فرض کریں $\\hat{p}_1$ ایک محدود آبادی (اکائیاں 7، 8، 9) سے واپسی کے ساتھ نکالے گئے $n_1=2$ سائز کے نمونوں میں جفت اعداد کا تناسب ظاہر کرتا ہے۔ فرض کریں $\\hat{p}_2$ ایک اور محدود آبادی (اکائیاں 4، 5 اور 5) سے واپسی کے ساتھ منتخب $n_2=2$ سائز کے نمونوں میں طاق اعداد کا تناسب ظاہر کرتا ہے۔',
    'فرض کړئ $\\hat{p}_1$ له یوه محدود نفوس (واحدونه 7، 8، 9) څخه له بېرته اچولو سره د راایستل شویو $n_1=2$ اندازې نمونو کې د جفت عددونو تناسب ښيي. فرض کړئ $\\hat{p}_2$ له بل محدود نفوس (واحدونه 4، 5 او 5) څخه له بېرته اچولو سره د ټاکل شویو $n_2=2$ اندازې نمونو کې د طاق عددونو تناسب ښيي.')
dp = c.build('stat12-p094-difference-proportions', '5.5 Difference between two sample proportions — properties and formulas', '5.5 دو نمونوں کے تناسبوں کا فرق — خصوصیات اور فارمولے', '5.5 د دوو نمونو د تناسبونو توپیر — ځانګړنې او فورمولونه', 94, [179, 180])

if __name__ == '__main__':
    save(94, [(5, ex), (5, dp)])
