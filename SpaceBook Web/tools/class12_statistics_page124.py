"""PDF124 printed 239–240: Example 7.1 conclusion; Example 7.2 (hens, left-tailed Z); Example 7.3 (teaching method, right-tailed Z) steps i–v."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('As computed value of Z = − 1.8 falls in the acceptance region, therefore, we accept $H_0$ i.e. mean life of the bulbs produced by this firm is equal to 812 hours.', 'چونکہ Z کی معلوم کی گئی قیمت = − 1.8 قبولیت کے علاقے میں ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں یعنی اس کمپنی کے بنائے گئے بلبوں کی اوسط عمر 812 گھنٹے کے برابر ہے۔', 'څرنګه چې د Z محاسبه شوی قیمت = − 1.8 د منلو په سیمه کې لوېږي، نو $H_0$ منو یعنې د دې شرکت د جوړو شویو ګروپونو منځنی عمر له 812 ساعتونو سره برابر دی.')
c71 = b.build('stat12-p124-example-7-1-end', 'Example 7.1 — conclusion', 'مثال 7.1 — نتیجہ', 'بېلګه 7.1 — پایله', 124, [239])

c = Builder()
c.h('Example 7.2', 'مثال 7.2', 'بېلګه 7.2')
c.p('A random sample of 25 hens from a normal population showed that the average laying is 250 eggs per year. The company claims that the average laying is 285 eggs per year with a standard deviation of 25 eggs per year. Test the claim of the company against the alternative that average laying is less than 285 eggs at α = 0.05', 'ایک نارمل آبادی سے 25 مرغیوں کے تصادفی نمونے نے ظاہر کیا کہ اوسطاً سالانہ 250 انڈے دیے جاتے ہیں۔ کمپنی کا دعویٰ ہے کہ اوسط سالانہ 285 انڈے ہیں اور معیاری انحراف سالانہ 25 انڈے ہے۔ α = 0.05 پر اس متبادل کے مقابلے میں کمپنی کے دعوے کی جانچ کریں کہ اوسط 285 انڈوں سے کم ہے۔', 'له یوه نورمال نفوس څخه د 25 چرګانو تصادفي نمونې وښوده چې منځنۍ هګۍ اچونه په کال کې 250 هګۍ ده. شرکت ادعا کوي چې منځنۍ هګۍ اچونه په کال کې 285 هګۍ ده او معیاري انحراف یې په کال کې 25 هګۍ دی. په α = 0.05 د شرکت ادعا د دې بدیل پر وړاندې وازموئ چې منځنۍ هګۍ اچونه له 285 هګیو کمه ده.')
c.h(*SOL)
c.group('lines', [
    ('i. $H_0:\\mu=285$',) * 3, ('$H_1:\\mu<285$',) * 3, ('ii. α = 0.05',) * 3,
    ('iii. Test statistic: As n = 25 is small but σ is known, therefore, we use test statistic for μ as $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$', 'iii. جانچ کا شماریہ: چونکہ n = 25 چھوٹا ہے لیکن σ معلوم ہے، لہٰذا ہم μ کے لیے یہ جانچ کا شماریہ استعمال کرتے ہیں $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$', 'iii. د ازموینې احصاییه: څرنګه چې n = 25 کوچنی دی خو σ معلوم دی، نو د μ لپاره دا د ازموینې احصاییه کاروو $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$'),
    ('iv. Computation:', 'iv. حساب:', 'iv. محاسبه:'),
    ('Given n = 25, $\\overline{X}=250$, σ = 25', 'دیا گیا ہے n = 25، $\\overline{X}=250$، σ = 25', 'ورکړل شوي n = 25، $\\overline{X}=250$، σ = 25'),
])
c.eq(r'Z=\frac{250-285}{25/\sqrt{25}}=\frac{-35}{25/5}=\frac{-35}{5}=-7')
c.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
c.vpara('stat12-ex7-2-cr', tail_test('left', z=1.645, ticks=((-1.645, '−1.645'),), label='Left-tailed critical region at −1.645'),
        'Given α = 0.05 since we have one tailed test, so 0.5 − 0.05 = 0.4500. Make inverse use of area table we have $Z_\\alpha=Z_{0.05}=1.645$ i.e. reject $H_0$ if Z calculated is less than or equal to −1.645.',
        'دیا گیا ہے α = 0.05، چونکہ ہماری یک طرفہ جانچ ہے، لہٰذا 0.5 − 0.05 = 0.4500۔ رقبے کے جدول کا الٹا استعمال کرنے سے $Z_\\alpha=Z_{0.05}=1.645$ ملتا ہے یعنی $H_0$ کو رد کریں اگر معلوم کیا گیا Z، −1.645 سے کم یا اس کے برابر ہو۔',
        'ورکړل شوي α = 0.05، څرنګه چې یو لوري ازموینه لرو، نو 0.5 − 0.05 = 0.4500. د مساحت د جدول په معکوس کارولو $Z_\\alpha=Z_{0.05}=1.645$ ترلاسه کوو یعنې $H_0$ رد کړئ که محاسبه شوی Z له −1.645 کم یا ورسره برابر وي.', ratio=.45)
c.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
c.p('Since our calculated value of Z lies in the rejection region, therefore, we reject $H_0$ and accept $H_1$.', 'چونکہ Z کی ہماری معلوم کی گئی قیمت رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں اور $H_1$ قبول کرتے ہیں۔', 'څرنګه چې زموږ د Z محاسبه شوی قیمت د ردولو په سیمه کې پروت دی، نو $H_0$ ردوو او $H_1$ منو.')
c72 = c.build('stat12-p124-example-7-2', 'Example 7.2 — left-tailed Z test (egg laying)', 'مثال 7.2 — بائیں طرفہ Z جانچ (انڈے دینا)', 'بېلګه 7.2 — کیڼ لوري Z ازموینه (هګۍ اچونه)', 124, [239, 240])

d = Builder()
d.h('Example 7.3', 'مثال 7.3', 'بېلګه 7.3')
d.p('Past records show that the average score of students in statistics is 57 with standard deviation 10. A new method of teaching is employed and a random sample of 70 students is selected. The sample average is 60. Can we conclude on the basis of these results, at 5% level of significance, that the average score has increased?', 'گزشتہ ریکارڈ ظاہر کرتا ہے کہ شماریات میں طلبہ کا اوسط اسکور 57 اور معیاری انحراف 10 ہے۔ پڑھانے کا ایک نیا طریقہ اپنایا جاتا ہے اور 70 طلبہ کا تصادفی نمونہ منتخب کیا جاتا ہے۔ نمونے کا اوسط 60 ہے۔ کیا ہم ان نتائج کی بنیاد پر 5% معنویت کی سطح پر یہ نتیجہ اخذ کر سکتے ہیں کہ اوسط اسکور بڑھ گیا ہے؟', 'پخوانی ریکارډ ښيي چې په احصایه کې د زده کوونکو منځنۍ نمره 57 او معیاري انحراف یې 10 دی. د تدریس نوې طریقه کارول کېږي او د 70 زده کوونکو تصادفي نمونه ټاکل کېږي. د نمونې منځنی 60 دی. آیا د دې پایلو پر بنسټ د 5% د معنی‌داریت په کچه دا پایله اخیستلای شو چې منځنۍ نمره زیاته شوې؟')
d.h(*SOL)
d.group('lines', [
    ('i. $H_0:\\mu=57$',) * 3, ('$H_1:\\mu>57$',) * 3, ('ii. α = 5% = 0.05',) * 3,
    ('iii. Test statistic: since σ is known, therefore, test statistic for μ in this case is $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$', 'iii. جانچ کا شماریہ: چونکہ σ معلوم ہے، لہٰذا اس صورت میں μ کے لیے جانچ کا شماریہ $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$ ہے', 'iii. د ازموینې احصاییه: څرنګه چې σ معلوم دی، نو په دې حالت کې د μ لپاره د ازموینې احصاییه $Z=\\frac{\\overline{X}-\\mu}{\\sigma/\\sqrt{n}}$ ده'),
    ('iv. Calculation: Given that n = 70, $\\overline{X}=60$, σ = 10, therefore,', 'iv. حساب: دیا گیا ہے n = 70، $\\overline{X}=60$، σ = 10، لہٰذا', 'iv. محاسبه: ورکړل شوي n = 70، $\\overline{X}=60$، σ = 10، نو'),
])
d.eq(r'Z=\frac{60-57}{10/\sqrt{70}}=\frac{(3)\sqrt{70}}{10}=2.51')
d.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
d.vpara('stat12-ex7-3-cr', tail_test('right', z=1.645, mid='', tail='', ticks=((0, '0'), (1.645, '1.645')), label='Right-tailed critical region at 1.645'),
        'As we see in $H_1$, we need to use one-sided test to the right. Here α = 0.05 (from the area table of S.N.D, we have $Z_\\alpha=Z_{0.05}=1.645$).',
        'جیسا کہ ہم $H_1$ میں دیکھتے ہیں، ہمیں دائیں جانب یک طرفہ جانچ استعمال کرنی ہے۔ یہاں α = 0.05 (S.N.D کے رقبے کے جدول سے ہمارے پاس $Z_\\alpha=Z_{0.05}=1.645$ ہے)۔',
        'لکه څنګه چې په $H_1$ کې وینو، باید ښي لوري ته یو اړخیزه ازموینه وکاروو. دلته α = 0.05 (د S.N.D د مساحت له جدول څخه لرو $Z_\\alpha=Z_{0.05}=1.645$).', ratio=.45)
c73 = d.build('stat12-p124-example-7-3', 'Example 7.3 — right-tailed Z test (teaching method)', 'مثال 7.3 — دائیں طرفہ Z جانچ (تدریسی طریقہ)', 'بېلګه 7.3 — ښي لوري Z ازموینه (د تدریس طریقه)', 124, [240])

if __name__ == '__main__':
    save(124, [(7, c71), (7, c72), (7, c73)])
