"""PDF102 printed 195–196: 6.1.3 estimator vs estimate, 6.2 point estimation, Example 6.1, 6.2.2 properties of a good point estimator (start)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
EST = ('estimator', 'تخمین کار', 'اټکلوونکی')
PE = ('point estimate', 'نقطہ تخمینہ', 'ټکي‌ییز اټکل')
b = Builder()
b.h('6.1.3 Difference between an estimator and an estimate', '6.1.3 تخمین کار اور تخمینہ میں فرق', '6.1.3 د اټکلوونکي او اټکل شوي قیمت ترمنځ توپیر')
b.p('A rule, usually expressed as a formula that tells us how to calculate an estimate from the sample data is called an estimator and the resulting number is called an estimate.', 'وہ قاعدہ جو عموماً فارمولا کی شکل میں ہو اور ہمیں بتائے کہ نمونے کے مواد سے تخمینہ کیسے معلوم کیا جائے، تخمین کار کہلاتا ہے اور حاصل عدد کو تخمینہ کہتے ہیں۔', 'هغه قاعده چې معمولاً د فورمول په بڼه وي او موږ ته وایي چې له نمونوي معلوماتو څخه اټکل څنګه محاسبه کړو، اټکلوونکی بلل کېږي او لاسته راغلي عدد ته اټکل شوی قیمت وایي.')
b.p('For example; if $\\overline{X}=\\frac{\\sum_{i=1}^{n}x_i}{n}=100$ then $\\overline{X}=\\frac{\\sum_{i=1}^{n}x_i}{n}$ is an estimator and 100 is an estimate. Similarly, if $s^2=\\frac{\\Sigma(x-\\overline{x})^2}{n-1}=2.63$ then $s^2=\\frac{\\Sigma(x-\\overline{x})^2}{n-1}$ is an estimator and its numerical value 2.63 is an estimate.',
    'مثلاً؛ اگر $\\overline{X}=\\frac{\\sum_{i=1}^{n}x_i}{n}=100$ ہو تو $\\overline{X}=\\frac{\\sum_{i=1}^{n}x_i}{n}$ تخمین کار اور 100 تخمینہ ہے۔ اسی طرح اگر $s^2=\\frac{\\Sigma(x-\\overline{x})^2}{n-1}=2.63$ ہو تو $s^2=\\frac{\\Sigma(x-\\overline{x})^2}{n-1}$ تخمین کار اور اس کی عددی قیمت 2.63 تخمینہ ہے۔',
    'د بېلګې په توګه؛ که $\\overline{X}=\\frac{\\sum_{i=1}^{n}x_i}{n}=100$ وي نو $\\overline{X}=\\frac{\\sum_{i=1}^{n}x_i}{n}$ اټکلوونکی او 100 اټکل شوی قیمت دی. همداراز که $s^2=\\frac{\\Sigma(x-\\overline{x})^2}{n-1}=2.63$ وي نو $s^2=\\frac{\\Sigma(x-\\overline{x})^2}{n-1}$ اټکلوونکی او شمېریز قیمت یې 2.63 اټکل شوی قیمت دی.')
b.h('6.2 Point estimation', '6.2 نقطہ تخمین', '6.2 ټکي‌ییز اټکل')
b.p('This process provides a single value which is calculated from the sample data as an estimate for the unknown population parameter. Point estimate may or may not be close to the parameter because the random sample used is one of the many possible samples which could be selected from the population.', 'یہ عمل ایک واحد قیمت فراہم کرتا ہے جو نمونے کے مواد سے نامعلوم آبادی کے پیرامیٹر کے تخمینے کے طور پر معلوم کی جاتی ہے۔ نقطہ تخمینہ پیرامیٹر کے قریب ہو بھی سکتا ہے اور نہیں بھی، کیونکہ استعمال ہونے والا تصادفی نمونہ ان بہت سے ممکنہ نمونوں میں سے ایک ہے جو آبادی سے منتخب کیے جا سکتے تھے۔', 'دا بهیر یو یوازینی قیمت ورکوي چې له نمونوي معلوماتو څخه د نامعلوم نفوس پارامټر د اټکل په توګه محاسبه کېږي. ټکي‌ییز اټکل کېدای شي پارامټر ته نږدې وي یا نه، ځکه چې کارول شوې تصادفي نمونه له هغو ډېرو شونو نمونو یوه ده چې له نفوس څخه ټاکل کېدای شوې.')
b.h('Example 6.1', 'مثال 6.1', 'بېلګه 6.1')
b.p('A random sample has ten observations 4, 3, 7, 8, 4, 10, 5, 5, 4 and 9. Compute a point estimate of (i) population mean (ii) population standard deviation (iii) standard error of the mean (iv) population proportion of even numbers.', 'ایک تصادفی نمونے میں دس مشاہدات 4، 3، 7، 8، 4، 10، 5، 5، 4 اور 9 ہیں۔ نقطہ تخمینہ معلوم کریں (i) آبادی کا اوسط (ii) آبادی کا معیاری انحراف (iii) اوسط کی معیاری غلطی (iv) جفت اعداد کا آبادی میں تناسب۔', 'یوه تصادفي نمونه لس مشاهدې 4، 3، 7، 8، 4، 10، 5، 5، 4 او 9 لري. ټکي‌ییز اټکل یې محاسبه کړئ (i) د نفوس منځنی (ii) د نفوس معیاري انحراف (iii) د منځني معیاري تېروتنه (iv) د جفت عددونو په نفوس کې تناسب.')
b.h(*SOL)
b.p('(i) Point estimate of the population mean μ is;', '(i) آبادی کے اوسط μ کا نقطہ تخمینہ یہ ہے؛', '(i) د نفوس د منځني μ ټکي‌ییز اټکل دا دی؛')
b.lab(r'\overline{X}=\frac{\Sigma x}{n}', *EST)
b.lab(r'=\frac{59}{10}=5.9', *PE)
b.p('(ii) Point estimate of the population standard deviation σ is;', '(ii) آبادی کے معیاری انحراف σ کا نقطہ تخمینہ یہ ہے؛', '(ii) د نفوس د معیاري انحراف σ ټکي‌ییز اټکل دا دی؛')
b.lab(r's=\sqrt{\frac{1}{n-1}\left[\Sigma x^2-\frac{(\Sigma x)^2}{n}\right]}', *EST)
b.mlines([r'=\sqrt{\frac{1}{10-1}\left[401-\frac{(59)^2}{10}\right]}', r'=\sqrt{\frac{1}{9}[401-348.1]}'])
b.lab(r'=\sqrt{\frac{52.9}{9}}=2.42', *PE)
b.p('(iii) Point estimate of the standard error $\\sigma_{\\overline{x}}$ is;', '(iii) معیاری غلطی $\\sigma_{\\overline{x}}$ کا نقطہ تخمینہ یہ ہے؛', '(iii) د معیاري تېروتنې $\\sigma_{\\overline{x}}$ ټکي‌ییز اټکل دا دی؛')
b.lab(r's_{\overline{x}}=\frac{s}{\sqrt{n}}', *EST)
b.lab(r'=\frac{2.42}{\sqrt{10}}=0.77', *PE)
b.p('(iv) Point estimate of the population proportion p is;', '(iv) آبادی کے تناسب p کا نقطہ تخمینہ یہ ہے؛', '(iv) د نفوس د تناسب p ټکي‌ییز اټکل دا دی؛')
b.lab(r'\hat{p}=\frac{X}{n}', *EST)
b.lab(r'=\frac{5}{10}=0.5', *PE)
b.h('6.2.2 Properties of a good point estimator', '6.2.2 اچھے نقطہ تخمین کار کی خصوصیات', '6.2.2 د ښه ټکي‌ییز اټکلوونکي ځانګړنې')
b.p('In point estimation the unknown value of a parameter is estimated by a single number which is quite risky job. This single value may or may not be equal to the true value of the parameter. The closeness of the estimate to the parameter value depends on random sample and the estimator. An ideal estimator is one which gives exactly the correct value of the parameter but such estimator does not exist in general. Hence to search a point estimate close to the parameter, it is necessary that the choice of one appropriate estimator in a given circumstance should be made on the basis of certain properties, called criteria for a good point estimator. A good point estimator is one which is unbiased, consistent,',
    'نقطہ تخمین میں پیرامیٹر کی نامعلوم قیمت کا تخمین ایک واحد عدد سے لگایا جاتا ہے جو کافی خطرناک کام ہے۔ یہ واحد قیمت پیرامیٹر کی حقیقی قیمت کے برابر ہو بھی سکتی ہے اور نہیں بھی۔ تخمینے کی پیرامیٹر کی قیمت سے قربت تصادفی نمونے اور تخمین کار پر منحصر ہے۔ مثالی تخمین کار وہ ہے جو پیرامیٹر کی بالکل درست قیمت دے لیکن عام طور پر ایسا تخمین کار موجود نہیں۔ لہٰذا پیرامیٹر کے قریب نقطہ تخمینہ تلاش کرنے کے لیے ضروری ہے کہ کسی صورتِ حال میں ایک موزوں تخمین کار کا انتخاب کچھ خصوصیات کی بنیاد پر کیا جائے جنہیں اچھے نقطہ تخمین کار کے معیارات کہتے ہیں۔ اچھا نقطہ تخمین کار وہ ہے جو غیر جانبدار، مستقل (consistent)،',
    'په ټکي‌ییز اټکل کې د پارامټر نامعلوم قیمت په یوه عدد اټکل کېږي چې ډېر خطرناک کار دی. دا یوازینی قیمت کېدای شي د پارامټر له رښتیني قیمت سره برابر وي یا نه. د اټکل نږدېوالی د پارامټر قیمت ته په تصادفي نمونه او اټکلوونکي پورې اړه لري. مثالي اټکلوونکی هغه دی چې د پارامټر دقیق سم قیمت ورکړي خو په عمومي ډول داسې اټکلوونکی نشته. نو د پارامټر ته د نږدې ټکي‌ییز اټکل د موندلو لپاره اړینه ده چې په یوه ورکړل شوي حالت کې د یوه مناسب اټکلوونکي ټاکنه د ځینو ځانګړنو پر بنسټ وشي چې د ښه ټکي‌ییز اټکلوونکي معیارونه بلل کېږي. ښه ټکي‌ییز اټکلوونکی هغه دی چې بې‌پلوه، ثابت (consistent)،')
rec = b.build('stat12-p102-point-estimation', '6.1.3–6.2 Estimator vs estimate, point estimation — Example 6.1', '6.1.3–6.2 تخمین کار بمقابلہ تخمینہ، نقطہ تخمین — مثال 6.1', '6.1.3–6.2 اټکلوونکی او اټکل، ټکي‌ییز اټکل — بېلګه 6.1', 102, [195, 196])
issues = [{'id': 'stat12-p196-numbering-gap', 'unit': 6, 'printedPage': 196, 'description': 'Section numbering jumps from 6.2 to 6.2.2 (no 6.2.1 printed); kept as printed.'}]

if __name__ == '__main__':
    save(102, [(6, rec)], issues=issues)
