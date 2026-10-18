"""PDF86 printed 163–164: 5.2.2 sampling distribution of the sample mean, 5.2.3 properties, 5.2.4 formulas, Example 5.4 question."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
x = r'\overline{x}'
b = Builder()
b.h('5.2.2 Sampling distribution of sample mean', '5.2.2 نمونے کے اوسط کی نمونہ جاتی تقسیم', '5.2.2 د نمونې د منځني نمونوي وېش')
b.p(f'The probability distribution of all possible values of the estimator ${X}$ is called sampling distribution of ${X}$ i.e.', f'تخمین کار ${X}$ کی تمام ممکنہ قیمتوں کی احتمالی تقسیم کو ${X}$ کی نمونہ جاتی تقسیم کہتے ہیں یعنی', f'د اټکلوونکي ${X}$ د ټولو شونو قیمتونو احتمالي وېش ته د ${X}$ نمونوي وېش وایي یعنې')
b.p(f'Sampling distribution of ${X}$', f'${X}$ کی نمونہ جاتی تقسیم', f'د ${X}$ نمونوي وېش')
b.grid('stat12-t-sampling-dist-mean', [f'${X}$', f'$f({x})$'], [[f'${x}_1$', f'$f({x}_1)$'], [f'${x}_2$', f'$f({x}_2)$'], ['$\\vdots$', '$\\vdots$'], [f'${x}_k$', f'$f({x}_k)$'], ['Total', '1']])
b.p(f'The mean of the sampling distribution of ${X}$ is denoted by $E({X})=\\mu_{{{x}}}$ (read as mu sub x bar) and its S.E by $\\sigma_{{{x}}}$ (read as sigma sub x bar).', f'${X}$ کی نمونہ جاتی تقسیم کے اوسط کو $E({X})=\\mu_{{{x}}}$ (پڑھیں mu sub x bar) اور اس کی معیاری غلطی کو $\\sigma_{{{x}}}$ (پڑھیں sigma sub x bar) سے ظاہر کرتے ہیں۔', f'د ${X}$ د نمونوي وېش منځنی په $E({X})=\\mu_{{{x}}}$ (mu sub x bar لوستل کېږي) او معیاري تېروتنه یې په $\\sigma_{{{x}}}$ (sigma sub x bar لوستل کېږي) ښودل کېږي.')
b.h(f'5.2.3 Properties of the sampling distribution of ${X}$', f'5.2.3 ${X}$ کی نمونہ جاتی تقسیم کی خصوصیات', f'5.2.3 د ${X}$ د نمونوي وېش ځانګړنې')
b.p(f'i. Mean of the sampling distribution of ${X}$ is always equal to the population mean i.e. $\\mu_{{{x}}}=\\mu$ (both in with and without replacement sampling)', f'i. ${X}$ کی نمونہ جاتی تقسیم کا اوسط ہمیشہ آبادی کے اوسط کے برابر ہوتا ہے یعنی $\\mu_{{{x}}}=\\mu$ (واپسی کے ساتھ اور بغیر دونوں نمونہ گیری میں)', f'i. د ${X}$ د نمونوي وېش منځنی تل د نفوس له منځني سره برابر دی یعنې $\\mu_{{{x}}}=\\mu$ (په دواړو له بېرته اچولو سره او پرته نمونه اخیستنه کې)')
b.p(f'ii. Standard error of the sampling distribution of ${X}$ is', f'ii. ${X}$ کی نمونہ جاتی تقسیم کی معیاری غلطی یہ ہے', f'ii. د ${X}$ د نمونوي وېش معیاري تېروتنه دا ده')
b.group('lines', [
    (f'$\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}$ (in case of sampling with replacement)', f'$\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}$ (واپسی کے ساتھ نمونہ گیری کی صورت میں)', f'$\\sigma_{{{x}}}=\\frac{{\\sigma}}{{\\sqrt{{n}}}}$ (له بېرته اچولو سره د نمونه اخیستنې په حالت کې)'),
    ('$=\\frac{\\sigma}{\\sqrt{n}}\\sqrt{\\frac{N-n}{N-1}}$ (in case of sampling without replacement)', '$=\\frac{\\sigma}{\\sqrt{n}}\\sqrt{\\frac{N-n}{N-1}}$ (بغیر واپسی کے نمونہ گیری کی صورت میں)', '$=\\frac{\\sigma}{\\sqrt{n}}\\sqrt{\\frac{N-n}{N-1}}$ (پرته له بېرته اچولو د نمونه اخیستنې په حالت کې)'),
])
b.p('Note that the factor $\\sqrt{\\frac{N-n}{N-1}}$ is called finite population correction factor (fpc). It is dropped from the formula when n < 5 % N and is used when n ≥ 5 % N.', 'نوٹ کریں کہ عامل $\\sqrt{\\frac{N-n}{N-1}}$ کو محدود آبادی کا تصحیحی عامل (fpc) کہتے ہیں۔ جب n < 5 % N ہو تو اسے فارمولا سے نکال دیا جاتا ہے اور جب n ≥ 5 % N ہو تو استعمال کیا جاتا ہے۔', 'پام وکړئ چې عامل $\\sqrt{\\frac{N-n}{N-1}}$ ته د محدود نفوس سمونې عامل (fpc) وایي. کله چې n < 5 % N وي له فورمول څخه لرې کېږي او کله چې n ≥ 5 % N وي کارول کېږي.')
b.p(f'iii. Shape of the sampling distribution of ${X}$', f'iii. ${X}$ کی نمونہ جاتی تقسیم کی شکل', f'iii. د ${X}$ د نمونوي وېش بڼه')
b.p('There are two cases:', 'دو صورتیں ہیں:', 'دوه حالتونه دي:')
b.group('lines', [
    (f'(a) If the sampled population is normal, then shape of the sampling distribution of ${X}$ will also be normal irrespective of the sample size.', f'(a) اگر نمونہ لی گئی آبادی نارمل ہو تو ${X}$ کی نمونہ جاتی تقسیم کی شکل بھی نمونے کے سائز سے قطع نظر نارمل ہوگی۔', f'(a) که نمونه ترې اخیستل شوی نفوس نورمال وي، نو د ${X}$ د نمونوي وېش بڼه به هم د نمونې له اندازې پرته نورماله وي.'),
    (f'(b) If the sampled population is non-normal, then according to central limit theorem (CLT), shape of the sampling distribution of ${X}$ will approximately be normal provided sample size n is large. Note that statisticians consider $n\\ge 30$ as large sample.', f'(b) اگر نمونہ لی گئی آبادی غیر نارمل ہو تو مرکزی حدی مسئلہ (CLT) کے مطابق ${X}$ کی نمونہ جاتی تقسیم کی شکل تقریباً نارمل ہوگی بشرطیکہ نمونے کا سائز n بڑا ہو۔ نوٹ کریں کہ شماریات دان $n\\ge 30$ کو بڑا نمونہ سمجھتے ہیں۔', f'(b) که نمونه ترې اخیستل شوی نفوس غیر نورمال وي، نو د مرکزي حد د قضیې (CLT) له مخې د ${X}$ د نمونوي وېش بڼه به نږدې نورماله وي په دې شرط چې د نمونې اندازه n لویه وي. پام وکړئ چې احصایه پوهان $n\\ge 30$ لویه نمونه ګڼي.'),
])
b.h(f'5.2.4 Formulas for mean and S.E of the sampling distribution of ${X}$', f'5.2.4 ${X}$ کی نمونہ جاتی تقسیم کے اوسط اور معیاری غلطی کے فارمولے', f'5.2.4 د ${X}$ د نمونوي وېش د منځني او معیاري تېروتنې فورمولونه')
b.group('lines', [
    (f'$\\mu_{{{x}}}=\\Sigma{x}f({x})$ (Mean)', f'$\\mu_{{{x}}}=\\Sigma{x}f({x})$ (اوسط)', f'$\\mu_{{{x}}}=\\Sigma{x}f({x})$ (منځنی)'),
    (f'$\\sigma_{{{x}}}^2=\\Sigma{x}^2f({x})-[\\Sigma{x}f({x})]^2$ (Variance)', f'$\\sigma_{{{x}}}^2=\\Sigma{x}^2f({x})-[\\Sigma{x}f({x})]^2$ (تغیر)', f'$\\sigma_{{{x}}}^2=\\Sigma{x}^2f({x})-[\\Sigma{x}f({x})]^2$ (واریانس)'),
    (f'$\\sigma_{{{x}}}=\\sqrt{{\\Sigma{x}^2f({x})-[\\Sigma{x}f({x})]^2}}$ (S.E)', f'$\\sigma_{{{x}}}=\\sqrt{{\\Sigma{x}^2f({x})-[\\Sigma{x}f({x})]^2}}$ (معیاری غلطی)', f'$\\sigma_{{{x}}}=\\sqrt{{\\Sigma{x}^2f({x})-[\\Sigma{x}f({x})]^2}}$ (معیاري تېروتنه)'),
])
b.p(f'Note that the random variable ${X}$ is standardized as $Z=\\frac{{{X}-\\mu_{{{x}}}}}{{\\sigma_{{{x}}}}}=\\frac{{{X}-\\mu}}{{\\sigma/\\sqrt{{n}}}}$ (In S.W.R. case)', f'نوٹ کریں کہ تصادفی متغیر ${X}$ کو یوں معیاری بنایا جاتا ہے $Z=\\frac{{{X}-\\mu_{{{x}}}}}{{\\sigma_{{{x}}}}}=\\frac{{{X}-\\mu}}{{\\sigma/\\sqrt{{n}}}}$ (S.W.R. کی صورت میں)', f'پام وکړئ چې تصادفي متغیر ${X}$ داسې معیاري کېږي $Z=\\frac{{{X}-\\mu_{{{x}}}}}{{\\sigma_{{{x}}}}}=\\frac{{{X}-\\mu}}{{\\sigma/\\sqrt{{n}}}}$ (د S.W.R. په حالت کې)')
b.h('Example 5.4', 'مثال 5.4', 'بېلګه 5.4')
b.p('Consider a family (population) of four children having ages 2, 2, 6, 8 years.', 'ایک خاندان (آبادی) پر غور کریں جس کے چار بچوں کی عمریں 2، 2، 6، 8 سال ہیں۔', 'یوه کورنۍ (نفوس) په پام کې ونیسئ چې څلور ماشومان یې 2، 2، 6، 8 کلن دي.')
b.group('lines', [
    ('i. Find mean and standard deviation of the population.', 'i. آبادی کا اوسط اور معیاری انحراف معلوم کریں۔', 'i. د نفوس منځنی او معیاري انحراف پیدا کړئ.'),
    (f'ii. Select random samples of two children with replacement and calculate the mean age ${x}$ for each sample.', f'ii. واپسی کے ساتھ دو بچوں کے تصادفی نمونے منتخب کریں اور ہر نمونے کی اوسط عمر ${x}$ معلوم کریں۔', f'ii. له بېرته اچولو سره د دوو ماشومانو تصادفي نمونې وټاکئ او د هرې نمونې منځنی عمر ${x}$ محاسبه کړئ.'),
    (f'iii. Construct sampling distribution of ${X}$', f'iii. ${X}$ کی نمونہ جاتی تقسیم بنائیں', f'iii. د ${X}$ نمونوي وېش جوړ کړئ'),
    ('iv. Find the mean and standard error of the sampling distribution of mean.', 'iv. اوسط کی نمونہ جاتی تقسیم کا اوسط اور معیاری غلطی معلوم کریں۔', 'iv. د منځني د نمونوي وېش منځنی او معیاري تېروتنه پیدا کړئ.'),
    (f'v. Verify the results obtained in (iv) by properties of the sampling distribution of ${X}$', f'v. (iv) میں حاصل نتائج کی ${X}$ کی نمونہ جاتی تقسیم کی خصوصیات سے تصدیق کریں', f'v. په (iv) کې لاسته راغلې پایلې د ${X}$ د نمونوي وېش د ځانګړنو له لارې تایید کړئ'),
])
rec = b.build('stat12-p086-sampling-mean', '5.2.2–5.2.4 Sampling distribution of the sample mean — Example 5.4', '5.2.2–5.2.4 نمونے کے اوسط کی نمونہ جاتی تقسیم — مثال 5.4', '5.2.2–5.2.4 د نمونې د منځني نمونوي وېش — بېلګه 5.4', 86, [163, 164])

if __name__ == '__main__':
    save(86, [(5, rec)])
