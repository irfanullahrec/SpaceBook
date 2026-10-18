"""PDF112 printed 215–216: Example 6.12 (99% t-interval), 6.3.5 interpreting the confidence interval (ladder figure), 6.3.6 CI for μ1−μ2 (σ known)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import ci_ladder, two_tail

SOL = ('Solution:', 'حل:', 'حل:')
D = r'\overline{X}_1-\overline{X}_2'
b = Builder()
b.h('Example 6.12', 'مثال 6.12', 'بېلګه 6.12')
b.p('Find a 99% confidence interval for population mean when a random sample selected from the population gives the values 1.03, 1.01, 0.097, 1.04, 0.99, 0.98, 1.03, 1.01, 0.99.', 'آبادی کے اوسط کے لیے 99% اعتماد کا وقفہ معلوم کریں جب آبادی سے منتخب کردہ تصادفی نمونہ یہ قیمتیں دے: 1.03، 1.01، 0.097، 1.04، 0.99، 0.98، 1.03، 1.01، 0.99۔', 'د نفوس منځني لپاره 99% د باور واټن پیدا کړئ کله چې له نفوس څخه ټاکل شوې تصادفي نمونه دا قیمتونه ورکړي: 1.03، 1.01، 0.097، 1.04، 0.99، 0.98، 1.03، 1.01، 0.99.')
b.h(*SOL)
b.p('A 100(1−α)% confidence interval for μ is $\\overline{X}\\pm t_{\\frac{\\alpha}{2},(n-1)}\\frac{s}{\\sqrt{n}}$', 'μ کے لیے 100(1−α)% اعتماد کا وقفہ $\\overline{X}\\pm t_{\\frac{\\alpha}{2},(n-1)}\\frac{s}{\\sqrt{n}}$ ہے', 'د μ لپاره 100(1−α)% د باور واټن $\\overline{X}\\pm t_{\\frac{\\alpha}{2},(n-1)}\\frac{s}{\\sqrt{n}}$ دی')
b.p('We have values 1.03, 1.01, 0.97, 1.04, 0.99, 0.98, 1.03, 1.01, 0.99.', 'ہمارے پاس قیمتیں 1.03، 1.01، 0.97، 1.04، 0.99، 0.98، 1.03، 1.01، 0.99 ہیں۔', 'موږ قیمتونه 1.03، 1.01، 0.97، 1.04، 0.99، 0.98، 1.03، 1.01، 0.99 لرو.')
b.p('Here n = 9, Σx = 9.05, Σx² = 9.1051, therefore,', 'یہاں n = 9، Σx = 9.05، Σx² = 9.1051، لہٰذا', 'دلته n = 9، Σx = 9.05، Σx² = 9.1051، نو')
b.mlines([r'\overline{x}=\frac{\Sigma x}{n}=\frac{9.05}{9}=1.0056,', r's=\sqrt{\frac{1}{n-1}\left[\Sigma x^2-\left(\frac{\Sigma x}{n}\right)^2\right]}=\sqrt{\frac{1}{9-1}\left[9.1051-\frac{(9.05)^2}{9}\right]}=0.02245', r'1-\alpha=0.99\quad\text{or}\quad\alpha=0.01'])
b.p('Now form t-table 6.1, we have $t_{\\alpha/2,(n-1)}=t_{0.01/2,(9-1)}=t_{0.005,(8)}=3.355$', 'اب t-جدول 6.1 سے ہمارے پاس $t_{\\alpha/2,(n-1)}=t_{0.01/2,(9-1)}=t_{0.005,(8)}=3.355$ ہے', 'اوس له t-جدول 6.1 څخه لرو $t_{\\alpha/2,(n-1)}=t_{0.01/2,(9-1)}=t_{0.005,(8)}=3.355$')
b.p('Putting values in expression for confidence interval, we get 99% confidence interval for μ as', 'اعتماد کے وقفے کے اظہاریے میں قیمتیں رکھنے سے μ کے لیے 99% اعتماد کا وقفہ یہ ملتا ہے', 'د باور د واټن په افاده کې قیمتونه ایښودو سره د μ لپاره 99% د باور واټن داسې لاسته راځي')
b.eq(r'1.0056\pm 3.355\left(\frac{0.0245}{\sqrt{9}}\right)\ \text{or}\ [1.0056\pm 0.0274],\ [0.9782,\ 1.033]')
ex = b.build('stat12-p112-example-6-12', 'Example 6.12 — 99% t-interval for μ', 'مثال 6.12 — μ کے لیے 99% t-وقفہ', 'بېلګه 6.12 — د μ لپاره 99% t-واټن', 112, [215])

c = Builder()
c.h('6.3.5 Interpreting the confidence interval', '6.3.5 اعتماد کے وقفے کی تشریح', '6.3.5 د باور د واټن تفسیر')
c.p('What does it mean to say we are 98% confidant that the true value of the population mean μ is within a given interval? It means that if we construct 100 such intervals for different samples, almost 98 out of 100 will contain the parameter and only 2 out of 100 will not contain the true value of the parameter. It can diagrammatically be shown as given in the Figure. Two of the intervals at serial number 3 and 97 do not contain the parameter μ while remaining 98 intervals contain the parameter. Remember that we cannot be absolutely sure that any one particular interval contains the mean μ.',
    'یہ کہنے کا کیا مطلب ہے کہ ہمیں 98% یقین ہے کہ آبادی کے اوسط μ کی حقیقی قیمت دیے گئے وقفے کے اندر ہے؟ اس کا مطلب ہے کہ اگر ہم مختلف نمونوں کے لیے ایسے 100 وقفے بنائیں تو 100 میں سے تقریباً 98 میں پیرامیٹر شامل ہوگا اور 100 میں سے صرف 2 میں پیرامیٹر کی حقیقی قیمت شامل نہیں ہوگی۔ اسے شکل میں دکھائے گئے خاکے کی طرح ظاہر کیا جا سکتا ہے۔ سیریل نمبر 3 اور 97 والے دو وقفوں میں پیرامیٹر μ شامل نہیں جبکہ باقی 98 وقفوں میں پیرامیٹر شامل ہے۔ یاد رکھیں کہ ہم مکمل طور پر یقین نہیں کر سکتے کہ کسی ایک خاص وقفے میں اوسط μ شامل ہے۔',
    'دا ویلو مانا څه ده چې موږ 98% ډاډه یو چې د نفوس د منځني μ رښتینی قیمت په ورکړل شوي واټن کې دی؟ مانا یې دا ده چې که د بېلابېلو نمونو لپاره داسې 100 واټنونه جوړ کړو، له 100 څخه نږدې 98 به پارامټر ولري او له 100 څخه یوازې 2 به د پارامټر رښتینی قیمت ونه لري. دا په شکل کې ښودل شوي ډیاګرام په څېر ښودل کېدای شي. د 3 او 97 سریال شمېرو دوه واټنونه μ پارامټر نه لري په داسې حال کې چې پاتې 98 واټنونه پارامټر لري. په یاد ولرئ چې موږ بشپړ ډاډه نه شو کېدای چې کوم یو ځانګړی واټن منځنی μ لري.')
c.visual('stat12-ci-ladder', ci_ladder('en'), ci_ladder('ur'), ci_ladder('ps'), ratio=.45)
c.h('6.3.6 Confidence interval estimate for the difference between two populations means when σ₁ and σ₂ are known', '6.3.6 جب σ₁ اور σ₂ معلوم ہوں تو دو آبادیوں کے اوسطوں کے فرق کا اعتماد کا وقفہ', '6.3.6 کله چې σ₁ او σ₂ معلوم وي د دوو نفوسونو د منځنیو د توپیر د باور واټن اټکل')
c.p(f'In this case ${D}$ is the point estimator of $(\\mu_1-\\mu_2)$ which in standard form can be written as;', f'اس صورت میں ${D}$، $(\\mu_1-\\mu_2)$ کا نقطہ تخمین کار ہے جسے معیاری شکل میں یوں لکھا جا سکتا ہے؛', f'په دې حالت کې ${D}$ د $(\\mu_1-\\mu_2)$ ټکي‌ییز اټکلوونکی دی چې په معیاري بڼه داسې لیکل کېدای شي؛')
c.eq(rf'Z=\frac{{({D})-(\mu_1-\mu_2)}}{{\sqrt{{\frac{{\sigma_1^2}}{{n_1}}+\frac{{\sigma_2^2}}{{n_2}}}}}}.')
c.vpara('stat12-ci-diff-z', two_tail('−Zα/2', 'Zα/2', label='Standard normal with critical values ±Z(α/2)'),
        'Probability statement for the random variable Z can be made as $P[-Z_{\\alpha/2}<Z<Z_{\\alpha/2}]=1-\\alpha$.', 'تصادفی متغیر Z کے لیے احتمالی بیان یوں بنایا جا سکتا ہے $P[-Z_{\\alpha/2}<Z<Z_{\\alpha/2}]=1-\\alpha$۔', 'د تصادفي متغیر Z لپاره احتمالي بیان داسې جوړېدای شي $P[-Z_{\\alpha/2}<Z<Z_{\\alpha/2}]=1-\\alpha$.', ratio=.45)
c.p('The 100(1−α)% confidence interval for $(\\mu_1-\\mu_2)$ in this case is given by', 'اس صورت میں $(\\mu_1-\\mu_2)$ کے لیے 100(1−α)% اعتماد کا وقفہ یہ ہے', 'په دې حالت کې د $(\\mu_1-\\mu_2)$ لپاره 100(1−α)% د باور واټن دا دی')
c.eq(rf'({D})\pm Z_{{\alpha/2}}\sqrt{{\frac{{\sigma_1^2}}{{n_1}}+\frac{{\sigma_2^2}}{{n_2}}}}')
it = c.build('stat12-p112-interpret-diff-means', '6.3.5 Interpreting a confidence interval; 6.3.6 CI for μ₁ − μ₂ (σ known)', '6.3.5 اعتماد کے وقفے کی تشریح؛ 6.3.6 μ₁ − μ₂ کا اعتماد کا وقفہ (σ معلوم)', '6.3.5 د باور د واټن تفسیر؛ 6.3.6 د μ₁ − μ₂ د باور واټن (σ معلوم)', 112, [216])
issues = [{'id': 'stat12-p215-ex612-values', 'unit': 6, 'printedPage': 215, 'description': 'Example 6.12 question lists 0.097 where the solution uses 0.97; the CI line uses 0.0245 where s = 0.02245 was computed; “form t-table” and “confidant” are printed slips. Printed text retained.'}]

if __name__ == '__main__':
    save(112, [(6, ex), (6, it)], issues=issues)
