"""PDF117 printed 225–226: Unit 6 Exercise 6.1 (T/F), 6.2 blanks (i)–(x), 6.3 MCQs (i)–(viii)."""
from class12_statistics_common import Builder, save

B = '______'
b = Builder()
b.h('Exercise', 'مشق', 'تمرین')
b.h('6.1 Read the following statements carefully and indicate which statement is true or false.', '6.1 درج ذیل بیانات غور سے پڑھیں اور بتائیں کہ کون سا بیان درست یا غلط ہے۔', '6.1 لاندې بیانونه په غور ولولئ او وښایاست چې کوم بیان سم یا ناسم دی.')
b.group('lines', [
    ('i. Statistical inference means making confidence interval for the parameter.', 'i. شماریاتی استنباط کا مطلب پیرامیٹر کے لیے اعتماد کا وقفہ بنانا ہے۔', 'i. احصاییوي استنتاج د پارامټر لپاره د باور واټن جوړول دي.'),
    ('ii. Parameters are constant and statistics are random variables.', 'ii. پیرامیٹرز مستقل اور شماریے تصادفی متغیرات ہیں۔', 'ii. پارامټرونه ثابت او احصاییې تصادفي متغیرونه دي.'),
    ('iii. Inference regarding population parameters can be done in three ways.', 'iii. آبادی کے پیرامیٹرز کے بارے میں استنباط تین طریقوں سے کیا جا سکتا ہے۔', 'iii. د نفوس د پارامټرونو په اړه استنتاج په درېیو لارو کېدای شي.'),
    ('iv. A statistic will always be an unbiased estimator if the sample itself is chosen without bias.', 'iv. اگر نمونہ خود بغیر تعصب کے چنا جائے تو شماریہ ہمیشہ غیر جانبدار تخمین کار ہوگا۔', 'iv. که نمونه پخپله پرته له تعصب وټاکل شي، احصاییه به تل بې‌پلوه اټکلوونکی وي.'),
    ('v. $s^2=\\frac{1}{n-1}\\Sigma(X-\\overline{X})^2$ is an unbiased estimator of $\\sigma^2$.', 'v. $s^2=\\frac{1}{n-1}\\Sigma(X-\\overline{X})^2$، $\\sigma^2$ کا غیر جانبدار تخمین کار ہے۔', 'v. $s^2=\\frac{1}{n-1}\\Sigma(X-\\overline{X})^2$ د $\\sigma^2$ بې‌پلوه اټکلوونکی دی.'),
    ('vi. In estimation procedure we estimate the value of a statistic.', 'vi. تخمین کے طریقے میں ہم شماریے کی قیمت کا تخمین لگاتے ہیں۔', 'vi. د اټکل په طریقه کې موږ د احصاییې قیمت اټکل کوو.'),
    ('vii. A 99% confidence interval will be wider than a 95% confidence interval constructed from the same data.', 'vii. ایک ہی مواد سے بنایا گیا 99% اعتماد کا وقفہ 95% اعتماد کے وقفے سے زیادہ چوڑا ہوگا۔', 'vii. له یو شان معلوماتو جوړ شوی 99% د باور واټن به تر 95% د باور واټن پلن وي.'),
    ('viii. The precision of the confidence interval will increase by increasing the sample size.', 'viii. نمونے کا سائز بڑھانے سے اعتماد کے وقفے کی درستی بڑھ جائے گی۔', 'viii. د نمونې د اندازې په زیاتولو د باور د واټن دقت زیاتېږي.'),
    ('ix. Confidence limits will vary from sample to sample.', 'ix. اعتماد کی حدیں ایک نمونے سے دوسرے تک بدلیں گی۔', 'ix. د باور حدونه به له یوې نمونې څخه تر بلې بدلېږي.'),
    ('x. t-distribution is used for interval estimation of μ when σ is known and n is large.', 'x. t-تقسیم μ کے وقفہ تخمین کے لیے استعمال ہوتی ہے جب σ معلوم اور n بڑا ہو۔', 'x. t-وېش د μ د واټني اټکل لپاره کارول کېږي کله چې σ معلوم او n لوی وي.'),
])
b.h('6.2 Fill in the blanks.', '6.2 خالی جگہیں پُر کریں۔', '6.2 تش ځایونه ډک کړئ.')
b.group('lines', [
    (f'i. An estimator is itself a {B}.', f'i. تخمین کار خود ایک {B} ہے۔', f'i. اټکلوونکی پخپله یو {B} دی.'),
    (f'ii. A value of an estimator is called an {B}.', f'ii. تخمین کار کی قیمت کو {B} کہتے ہیں۔', f'ii. د اټکلوونکي قیمت ته {B} وایي.'),
    (f'iii. If $x_1,x_2\\ldots x_n$ be a random sample, the expression $\\overline{{x}}=\\frac{{\\Sigma x}}{{n}}$ is an {B}.', f'iii. اگر $x_1,x_2\\ldots x_n$ ایک تصادفی نمونہ ہو تو اظہاریہ $\\overline{{x}}=\\frac{{\\Sigma x}}{{n}}$ ایک {B} ہے۔', f'iii. که $x_1,x_2\\ldots x_n$ یوه تصادفي نمونه وي، نو افاده $\\overline{{x}}=\\frac{{\\Sigma x}}{{n}}$ یو {B} دی.'),
    (f'iv. A single value of an estimator for a population parameter is called its {B} estimate.', f'iv. آبادی کے پیرامیٹر کے لیے تخمین کار کی واحد قیمت کو اس کا {B} تخمینہ کہتے ہیں۔', f'iv. د نفوس پارامټر لپاره د اټکلوونکي یوازیني قیمت ته د هغه {B} اټکل وایي.'),
    (f'v. If expected value of an estimator $\\hat{{\\theta}}$ is equal to the value of the parameter θ, then $\\hat{{\\theta}}$ is said to be an {B} estimator of θ.', f'v. اگر تخمین کار $\\hat{{\\theta}}$ کی متوقع قیمت پیرامیٹر θ کی قیمت کے برابر ہو تو $\\hat{{\\theta}}$ کو θ کا {B} تخمین کار کہتے ہیں۔', f'v. که د اټکلوونکي $\\hat{{\\theta}}$ تمه شوی قیمت د θ پارامټر له قیمت سره برابر وي، نو $\\hat{{\\theta}}$ د θ {B} اټکلوونکی بلل کېږي.'),
    (f'vi. If two estimators $T_1$ and $T_2$ such that $Var(T_1)<Var(T_2)$, then $T_1$ is called {B} estimator than $T_2$.', f'vi. اگر دو تخمین کار $T_1$ اور $T_2$ ایسے ہوں کہ $Var(T_1)<Var(T_2)$ تو $T_1$ کو $T_2$ سے {B} تخمین کار کہتے ہیں۔', f'vi. که دوه اټکلوونکي $T_1$ او $T_2$ داسې وي چې $Var(T_1)<Var(T_2)$، نو $T_1$ تر $T_2$ {B} اټکلوونکی بلل کېږي.'),
    (f'vii. An interval estimate with {B} interval is best.', f'vii. {B} وقفے والا وقفہ تخمینہ بہترین ہے۔', f'vii. د {B} واټن لرونکی واټني اټکل غوره دی.'),
    (f'viii. The precision of a confidence interval increases by {B} the sample size.', f'viii. اعتماد کے وقفے کی درستی نمونے کا سائز {B} سے بڑھتی ہے۔', f'viii. د باور د واټن دقت د نمونې د اندازې په {B} زیاتېږي.'),
    (f'ix. Estimation has {B} types.', f'ix. تخمین کی {B} اقسام ہیں۔', f'ix. اټکل {B} ډولونه لري.'),
    (f'x. (1−α) is known as {B}.', f'x. (1−α) کو {B} کہتے ہیں۔', f'x. (1−α) ته {B} وایي.'),
])
b.h('6.3 Choose the Correct answer:', '6.3 درست جواب منتخب کریں:', '6.3 سم ځواب وټاکئ:')
b.mcq('i.', ('Estimate and estimator are:', 'تخمینہ اور تخمین کار ہیں:', 'اټکل او اټکلوونکی دي:'),
      [('synonyms', 'ہم معنی', 'مترادف'), ('different', 'مختلف', 'بېلابېل'), ('related to population', 'آبادی سے متعلق', 'له نفوس سره تړلي'), ('formulae', 'فارمولے', 'فورمولونه')])
b.mcq('ii.', ('Bias of an estimator can be:', 'تخمین کار کی جانبداری ہو سکتی ہے:', 'د اټکلوونکي پلوي کېدای شي:'),
      [('positive', 'مثبت', 'مثبت'), ('negative', 'منفی', 'منفي'), ('either positive or negative', 'مثبت یا منفی', 'یا مثبت یا منفي'), ('always zero', 'ہمیشہ صفر', 'تل صفر')])
b.mcq('iii.', ('If $\\hat{p}=0.5$, then 0.5 is called ;', 'اگر $\\hat{p}=0.5$ ہو تو 0.5 کہلاتا ہے؛', 'که $\\hat{p}=0.5$ وي، نو 0.5 بلل کېږي؛'),
      [('estimator', 'تخمین کار', 'اټکلوونکی'), ('estimate', 'تخمینہ', 'اټکل'), ('interval', 'وقفہ', 'واټن'), ('all of above', 'تمام مندرجہ بالا', 'پورته ټول')])
b.mcq('iv.', ('Estimation has ______ types.', 'تخمین کی ______ اقسام ہیں۔', 'اټکل ______ ډولونه لري.'), ['3', '4', '2', '5'])
b.mcq('v.', ('α is called ;', 'α کہلاتا ہے؛', 'α بلل کېږي؛'),
      [('level of significance', 'معنویت کی سطح', 'د معنی‌داریت کچه'), ('confidence level', 'اعتماد کی سطح', 'د باور کچه'), ('confidence coefficient', 'اعتماد کا ضریب', 'د باور ضریب'), ('all of above', 'تمام مندرجہ بالا', 'پورته ټول')])
b.mcq('vi.', ('The probability statement $P[-Z_{\\alpha/2}<Z<Z_{\\alpha/2}]=?$', 'احتمالی بیان $P[-Z_{\\alpha/2}<Z<Z_{\\alpha/2}]=?$', 'احتمالي بیان $P[-Z_{\\alpha/2}<Z<Z_{\\alpha/2}]=?$'), ['$\\alpha$', '$\\beta$', '$1-\\beta$', '$1-\\alpha$'])
b.mcq('vii.', ('If the average value of an estimator is equal to the true value of the parameter, the property is called;', 'اگر تخمین کار کی اوسط قیمت پیرامیٹر کی حقیقی قیمت کے برابر ہو تو یہ خاصیت کہلاتی ہے؛', 'که د اټکلوونکي منځنی قیمت د پارامټر له رښتیني قیمت سره برابر وي، دې ځانګړنې ته وایي؛'),
      [('efficiency', 'کارکردگی', 'موثریت'), ('sufficiency', 'کفایت', 'کفایت'), ('consistency', 'استقلال', 'ثبات'), ('unbiasedness', 'غیر جانبداری', 'بې‌پلوي')])
b.mcq('viii.', ('Statistical inference makes inferences about', 'شماریاتی استنباط کس کے بارے میں استنباط کرتا ہے', 'احصاییوي استنتاج د څه په اړه استنتاج کوي'),
      [('Sample', 'نمونہ', 'نمونه'), ('population', 'آبادی', 'نفوس'), ('both population and sample', 'آبادی اور نمونہ دونوں', 'نفوس او نمونه دواړه'), ('estimator', 'تخمین کار', 'اټکلوونکی')])
rec = b.build('stat12-u6-exercise-a', 'Unit 6 Exercise — 6.1 to 6.3 (viii)', 'یونٹ 6 مشق — 6.1 تا 6.3 (viii)', 'واحد 6 تمرین — 6.1 تر 6.3 (viii)', 117, [225, 226])

if __name__ == '__main__':
    save(117, [(6, rec)])
