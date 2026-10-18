"""PDF98 printed 187–188: Exercise 5.2 (vii)–(x), 5.3 MCQs (i)–(x), questions 5.4–5.8 (matching table)."""
from class12_statistics_common import Builder, save

B = '______'
b = Builder()
b.group('lines', [
    (f'vii. Under simple random sampling with replacement the same unit can occur {B} in the sample.', f'vii. واپسی کے ساتھ سادہ تصادفی نمونہ گیری میں ایک ہی اکائی نمونے میں {B} آ سکتی ہے۔', f'vii. له بېرته اچولو سره په ساده تصادفي نمونه اخیستنه کې یو واحد په نمونه کې {B} راتلای شي.'),
    (f'viii. The expression $\\frac{{n}}{{N}}$ is known as {B}.', f'viii. اظہاریہ $\\frac{{n}}{{N}}$ کو {B} کہتے ہیں۔', f'viii. افادې $\\frac{{n}}{{N}}$ ته {B} وایي.'),
    (f'ix. The quantity $\\sqrt{{\\frac{{N-n}}{{N-1}}}}$ is called {B}.', f'ix. مقدار $\\sqrt{{\\frac{{N-n}}{{N-1}}}}$ کو {B} کہتے ہیں۔', f'ix. کمیت $\\sqrt{{\\frac{{N-n}}{{N-1}}}}$ ته {B} وایي.'),
    (f'x. fpc is dropped from the S.E formula if {B}.', f'x. fpc کو معیاری غلطی کے فارمولے سے نکال دیا جاتا ہے اگر {B}۔', f'x. fpc د معیاري تېروتنې له فورمول څخه لرې کېږي که {B}.'),
])
b.h('5.3 Choose the correct answer.', '5.3 درست جواب منتخب کریں۔', '5.3 سم ځواب وټاکئ.')
b.mcq('i.', ('A characteristic of population is called', 'آبادی کی خاصیت کہلاتی ہے', 'د نفوس ځانګړنه بلل کېږي'),
      [('parameter', 'پیرامیٹر', 'پارامټر'), ('statistic', 'شماریہ', 'احصاییه'), ('sample', 'نمونہ', 'نمونه'), ('constant', 'مستقل', 'ثابت')])
b.mcq('ii.', ('As the sample size increases the standard error of the sampling distribution of mean:', 'جیسے جیسے نمونے کا سائز بڑھتا ہے، اوسط کی نمونہ جاتی تقسیم کی معیاری غلطی:', 'لکه څنګه چې د نمونې اندازه زیاتېږي، د منځني د نمونوي وېش معیاري تېروتنه:'),
      [('increases', 'بڑھتی ہے', 'زیاتېږي'), ('decreases', 'کم ہوتی ہے', 'کمېږي'), ('remains the same', 'یکساں رہتی ہے', 'یو شان پاتې کېږي'), ('becomes negative', 'منفی ہو جاتی ہے', 'منفي کېږي')])
b.mcq('iii.', ('Probability of selection varies at each subsequent draw in:', 'ہر اگلی بار انتخاب کا احتمال بدلتا ہے:', 'په هر راتلونکي ځل د ټاکل کېدو احتمال بدلېږي په:'),
      ['S.W.R', 'S.W.O.R', ('both (a) and (b)', '(a) اور (b) دونوں', '(a) او (b) دواړه'), ('neither (a) and (b)', 'نہ (a) نہ (b)', 'نه (a) او نه (b)')])
b.mcq('iv.', ('Which of the following statement is true?', 'درج ذیل میں سے کون سا بیان درست ہے؟', 'له لاندې څخه کوم بیان سم دی؟'),
      [('S.E is always zero', 'معیاری غلطی ہمیشہ صفر ہوتی ہے', 'معیاري تېروتنه تل صفر وي'), ('S.E is always unity', 'معیاری غلطی ہمیشہ اکائی ہوتی ہے', 'معیاري تېروتنه تل یو وي'), ('more the S.E, better it is', 'معیاری غلطی جتنی زیادہ، اتنی بہتر', 'څومره چې معیاري تېروتنه زیاته، هومره ښه'), ('less the S.E, better it is', 'معیاری غلطی جتنی کم، اتنی بہتر', 'څومره چې معیاري تېروتنه کمه، هومره ښه')])
b.mcq('v.', ('fpc can be dropped from the S.E formula if', 'fpc کو معیاری غلطی کے فارمولے سے نکالا جا سکتا ہے اگر', 'fpc د معیاري تېروتنې له فورمول څخه لرې کېدای شي که'),
      ['$n<5\\%N$', '$n<0.05N$', '$\\frac{n}{N}<5\\%$', ('all of the above', 'تمام مندرجہ بالا', 'پورته ټول')])
b.mcq('vi.', ('If μ = 40, σ = 10, n = 25, then value of $\\sigma_{\\overline{x}}$ is', 'اگر μ = 40، σ = 10، n = 25 ہو تو $\\sigma_{\\overline{x}}$ کی قیمت ہے', 'که μ = 40، σ = 10، n = 25 وي، نو د $\\sigma_{\\overline{x}}$ قیمت دی'), ['40', '10', '2', '0.4'], per_line=4)
b.mcq('vii.', ('The number of random samples of size 2 that can be selected W.O.R from a population having 7 items are equal to', '7 اشیاء والی آبادی سے بغیر واپسی کے منتخب کیے جا سکنے والے 2 سائز کے تصادفی نمونوں کی تعداد برابر ہے', 'له 7 توکو لرونکي نفوس څخه پرته له بېرته اچولو د ټاکل کېدونکو د 2 اندازې تصادفي نمونو شمېر برابر دی له'), ['12', '49', '21', '14'], per_line=4)
b.mcq('viii.', ('A characteristic of sample is called', 'نمونے کی خاصیت کہلاتی ہے', 'د نمونې ځانګړنه بلل کېږي'),
      [('parameter', 'پیرامیٹر', 'پارامټر'), ('sample', 'نمونہ', 'نمونه'), ('statistic', 'شماریہ', 'احصاییه'), ('constant', 'مستقل', 'ثابت')], per_line=4)
b.mcq('ix.', ('The finite population correction factor is', 'محدود آبادی کا تصحیحی عامل ہے', 'د محدود نفوس د سمونې عامل دی'),
      ['$\\sqrt{\\frac{n-1}{n-N}}$', '$\\sqrt{\\frac{N-1}{N}}$', '$\\sqrt{\\frac{N-n}{n-1}}$', '$\\sqrt{\\frac{N-n}{N-1}}$'], per_line=4)
b.mcq('x.', ('An estimator is a', 'تخمین کار ہے ایک', 'اټکلوونکی یو دی'),
      [('variable', 'متغیر', 'متغیر'), ('constant', 'مستقل', 'ثابت'), ('fixed value', 'مقررہ قیمت', 'ټاکلی قیمت'), ('random variable', 'تصادفی متغیر', 'تصادفي متغیر')])
Q = lambda n, e, u, p: b.p(f'{n} {e}', f'{n} {u}', f'{n} {p}')
Q('5.4', 'What is meant by population, sample and sampling?', 'آبادی، نمونہ اور نمونہ گیری سے کیا مراد ہے؟', 'له نفوس، نمونې او نمونه اخیستنې څخه مطلب څه دی؟')
Q('5.5', 'What is the need of sampling as compared to complete enumeration?', 'مکمل شمار کے مقابلے میں نمونہ گیری کی کیا ضرورت ہے؟', 'د بشپړې شمېرنې په پرتله نمونه اخیستنې ته څه اړتیا ده؟')
Q('5.6', 'Write short notes on: (i) sampling frame (ii) sample design (iii) survey', 'مختصر نوٹ لکھیں: (i) نمونہ فریم (ii) نمونے کا خاکہ (iii) سروے', 'لنډ یادښتونه ولیکئ: (i) نمونوي چوکاټ (ii) د نمونې ډیزاین (iii) سروې')
Q('5.7', 'Differentiate between:', 'فرق واضح کریں:', 'توپیر یې وښایاست:')
b.group('lines', [
    ('(i) Finite and infinite population.', '(i) محدود اور لامحدود آبادی۔', '(i) محدود او بې‌پایه نفوس.'),
    ('(ii) Sampling with and without replacement', '(ii) واپسی کے ساتھ اور بغیر نمونہ گیری', '(ii) له بېرته اچولو سره او پرته نمونه اخیستنه'),
    ('(iii) Sampling and non-sampling errors', '(iii) نمونہ جاتی اور غیر نمونہ جاتی غلطیاں', '(iii) نمونوي او غیر نمونوي تېروتنې'),
])
Q('5.8', 'Match the symbols on the left with the phrase on the right.', 'بائیں جانب کی علامتوں کو دائیں جانب کے جملوں سے ملائیں۔', 'په کیڼ اړخ کې نښې په ښي اړخ کې له عبارتونو سره سمې کړئ.')
syms = ['$\\mu$', '$\\overline{X}$', '$\\sigma^2$', '$S^2$', '$p$', '$\\hat{p}$']
en = ['Sample mean', 'Sample variance', 'Population proportion', 'Population variance', 'Sample proportion', 'population mean']
ur = ['نمونے کا اوسط', 'نمونے کا تغیر', 'آبادی کا تناسب', 'آبادی کا تغیر', 'نمونے کا تناسب', 'آبادی کا اوسط']
ps = ['د نمونې منځنی', 'د نمونې واریانس', 'د نفوس تناسب', 'د نفوس واریانس', 'د نمونې تناسب', 'د نفوس منځنی']
b.table('stat12-t-q5-8', ['symbol', 'phrase'], [[s, p] for s, p in zip(syms, en)], ['علامت', 'جملہ'], ['نښه', 'عبارت'], [[s, p] for s, p in zip(syms, ur)], [[s, p] for s, p in zip(syms, ps)])
rec = b.build('stat12-u5-exercise-b', 'Unit 5 Exercise — 5.2 (vii)–(x), 5.3 and 5.4–5.8', 'یونٹ 5 مشق — 5.2 (vii)–(x)، 5.3 اور 5.4–5.8', 'واحد 5 تمرین — 5.2 (vii)–(x)، 5.3 او 5.4–5.8', 98, [187, 188])

if __name__ == '__main__':
    save(98, [(5, rec)])
