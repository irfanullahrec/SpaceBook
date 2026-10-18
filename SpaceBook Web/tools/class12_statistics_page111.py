"""PDF111 printed 213–214: Example 6.11 result; 6.3.4 small-sample CI for μ (t), degrees of freedom; Table 6.1 critical values of Student's t."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import t_two_tail

b = Builder()
b.mlines([r'756\pm 1.96\frac{35}{\sqrt{50}}\qquad\text{or } 756\pm 9.70', r'\text{or } 756-9.70,\ 756+9.70\qquad\text{or } [746.30,\ 765.70]'])
b.p('This means that the mean daily intake of dairy products for males varies from 746.30 to 765.70 grams per day.', 'اس کا مطلب ہے کہ مردوں کے لیے ڈیری مصنوعات کا اوسط یومیہ استعمال 746.30 سے 765.70 گرام فی دن کے درمیان ہے۔', 'مانا یې دا ده چې د نارینه وو لپاره د لبنیاتو منځنی ورځنی مصرف له 746.30 څخه تر 765.70 ګرامه په ورځ پورې دی.')
b.h('6.3.4 Confidence interval for population mean μ when σ is unknown (small sample)', '6.3.4 جب σ نامعلوم ہو تو آبادی کے اوسط μ کے لیے اعتماد کا وقفہ (چھوٹا نمونہ)', '6.3.4 کله چې σ نامعلوم وي د نفوس د منځني μ لپاره د باور واټن (کوچنۍ نمونه)')
b.vpara('stat12-t-ci-figure', t_two_tail(),
        'When σ is known and n is small, then the interval estimator $\\overline{X}\\pm Z_{\\alpha/2}\\frac{\\sigma}{\\sqrt{n}}$ will still be used for μ but if σ is unknown and n < 30, then the statistic $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ is used which has t-distribution with ν = n−1 degrees of freedom and $s=\\sqrt{\\frac{1}{n-1}\\Sigma(x-\\overline{x})^2}$. Probability statement can be made as: $P\\left[-t_{\\alpha/2,(\\upsilon)}<t<t_{\\alpha/2,(\\upsilon)}\\right]=1-\\alpha$',
        'جب σ معلوم ہو اور n چھوٹا ہو تو μ کے لیے وقفہ تخمین کار $\\overline{X}\\pm Z_{\\alpha/2}\\frac{\\sigma}{\\sqrt{n}}$ ہی استعمال ہوگا، لیکن اگر σ نامعلوم ہو اور n < 30 ہو تو شماریہ $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ استعمال ہوتا ہے جس کی t-تقسیم ν = n−1 درجاتِ آزادی کے ساتھ ہے اور $s=\\sqrt{\\frac{1}{n-1}\\Sigma(x-\\overline{x})^2}$۔ احتمالی بیان یوں بنایا جا سکتا ہے: $P\\left[-t_{\\alpha/2,(\\upsilon)}<t<t_{\\alpha/2,(\\upsilon)}\\right]=1-\\alpha$',
        'کله چې σ معلوم وي او n کوچنی وي، نو د μ لپاره واټني اټکلوونکی $\\overline{X}\\pm Z_{\\alpha/2}\\frac{\\sigma}{\\sqrt{n}}$ به بیا هم کارول کېږي، خو که σ نامعلوم وي او n < 30 وي، نو احصاییه $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ کارول کېږي چې د ν = n−1 د ازادۍ درجو سره t-وېش لري او $s=\\sqrt{\\frac{1}{n-1}\\Sigma(x-\\overline{x})^2}$. احتمالي بیان داسې جوړېدای شي: $P\\left[-t_{\\alpha/2,(\\upsilon)}<t<t_{\\alpha/2,(\\upsilon)}\\right]=1-\\alpha$', ratio=.45)
b.p('Putting value of t to have a 100(1−α)% confidence interval for μ when σ is unknown and n is small as;', 't کی قیمت رکھنے سے جب σ نامعلوم اور n چھوٹا ہو تو μ کے لیے 100(1−α)% اعتماد کا وقفہ یہ ہے؛', 'د t قیمت ایښودو سره، کله چې σ نامعلوم او n کوچنی وي، د μ لپاره 100(1−α)% د باور واټن دا دی؛')
b.eq(r'\overline{X}\pm t_{\alpha/2,(\upsilon)}\frac{s}{\sqrt{n}}')
b.h('■ Degrees of freedom', '■ درجاتِ آزادی', '■ د ازادۍ درجې')
b.p('The number of values in the sample that are independent and free to vary is called degrees of freedom e.g. if $x_1+x_2=10$. we can give value only to $x_1$ or $x_2$ the second one will be automatically computed. Hence d.f = 2 − 1 = 1. Generally if we have $x_1+x_2+\\ldots\\ldots x_n=10$ we can gave values to first n−1 scores freely and one score is restricted, so we have degrees freedom d.f = n−1',
    'نمونے میں ان قیمتوں کی تعداد جو آزاد ہوں اور بدلنے میں آزاد ہوں، درجاتِ آزادی کہلاتی ہے، مثلاً اگر $x_1+x_2=10$ ہو تو ہم صرف $x_1$ یا $x_2$ کو قیمت دے سکتے ہیں، دوسری خود بخود معلوم ہو جائے گی۔ لہٰذا d.f = 2 − 1 = 1۔ عام طور پر اگر $x_1+x_2+\\ldots\\ldots x_n=10$ ہو تو ہم پہلے n−1 اسکور کو آزادانہ قیمتیں دے سکتے ہیں اور ایک اسکور پابند ہوتا ہے، لہٰذا درجاتِ آزادی d.f = n−1 ہیں',
    'په نمونه کې د هغو قیمتونو شمېر چې خپلواک وي او د بدلېدو لپاره ازاد وي، د ازادۍ درجې بلل کېږي، لکه که $x_1+x_2=10$ وي، موږ یوازې $x_1$ یا $x_2$ ته قیمت ورکولای شو، دویم به په خپله محاسبه شي. نو d.f = 2 − 1 = 1. په عمومي ډول که $x_1+x_2+\\ldots\\ldots x_n=10$ ولرو، لومړیو n−1 نمرو ته په ازاده توګه قیمتونه ورکولای شو او یوه نمره محدوده ده، نو د ازادۍ درجې d.f = n−1 دي')
ci = b.build('stat12-p111-t-interval', 'Example 6.11 result; 6.3.4 small-sample CI for μ using t', 'مثال 6.11 کا نتیجہ؛ 6.3.4 t کے ذریعے چھوٹے نمونے کا اعتماد کا وقفہ', 'د بېلګې 6.11 پایله؛ 6.3.4 د t په واسطه د کوچنۍ نمونې د باور واټن', 111, [213])

t = Builder()
t.h('TABLE 6.1 [Critical values of student t-distribution]', 'جدول 6.1 [اسٹوڈنٹ t-تقسیم کی فیصلہ کن قیمتیں]', 'جدول 6.1 [د سټوډنټ t-وېش بحراني قیمتونه]')
rows = '''1 3.078 6.314 12.706 31.821 63.657
2 1.886 2.920 4.303 6.965 9.925
3 1.638 2.353 3.182 4.541 5.841
4 1.533 2.132 2.776 3.747 4.604
5 1.476 2.015 2.571 3.365 4.032
6 1.440 1.943 2.447 3.143 3.707
7 1.415 1.895 2.365 2.998 3.499
8 1.397 1.860 2.306 2.896 3.355
9 1.383 1.833 2.262 2.821 3.250
10 1.372 1.812 2.228 2.764 3.169
11 1.363 1.796 2.204 2.718 3.106
12 1.356 1.782 2.179 2.681 3.055
13 1.350 1.771 2.146 2.650 3.012
14 1.345 14.761 2.145 2.624 2.977
15 1.341 1.753 2.131 2.602 2.947
16 1.337 1.746 2.120 2.583 2.921
17 1.333 1.740 2.110 2.567 2.898
18 1.330 1.734 2.101 2.552 2.878
19 1328 1.729 2.093 2.539 2.861
20 1.325 1.725 2.086 2.528 2.845
21 1.323 1.721 2.080 2.518 2.831
22 1.321 1.717 2.074 2.508 2.819
23 1.319 1.714 2.069 2.500 2.807
24 1.318 1.711 2.064 2.492 2.797
25 1.316 1.708 2.060 2.485 2.787
26 1.315 1.706 2.056 2.479 2.779
27 1.314 1.703 2.052 2.473 2.771
28 1.313 1.701 2.048 2.467 2.763
29 1.311 1.699 2.045 2.462 2.756
∞ 1.282 1.645 1.960 2.326 2.576'''.split('\n')
grid = [r.split() + [r.split()[0]] for r in rows]
assert all(len(r) == 7 for r in grid) and len(grid) == 30
t.grid('stat12-table6-1', ['df', '$t_{.100}$', '$t_{.050}$', '$t_{.025}$', '$t_{.010}$', '$t_{.005}$', 'df'], grid)
tab = t.build('stat12-p111-table-6-1', 'Table 6.1 Critical values of Student’s t-distribution', 'جدول 6.1 اسٹوڈنٹ t-تقسیم کی فیصلہ کن قیمتیں', 'جدول 6.1 د سټوډنټ t-وېش بحراني قیمتونه', 111, [214])
issues = [{'id': 'stat12-p214-t-table-misprints', 'unit': 6, 'printedPage': 214, 'description': 'Table 6.1 kept as printed; misprints vs standard t values: df 14, t.050 printed 14.761 (1.761); df 19, t.100 printed 1328 (1.328). The sentence on degrees of freedom prints “we can gave values”.'}]

if __name__ == '__main__':
    save(111, [(6, ci), (6, tab)], issues=issues)
