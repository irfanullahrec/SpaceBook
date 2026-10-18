"""PDF54 printed 99–100: 3.4.2 hypergeometric pmf and parameters; Example 3.20 (committee) with distribution table."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import svg_open

SOL = ('Solution:', 'حل:', 'حل:')


def box_svg(lang):
    persons = {'en': '6 persons', 'ur': '6 افراد', 'ps': '6 کسان'}[lang]
    return (svg_open(260, 120, 'Population of 4 men and 2 women; K marks the 2 women, N the 6 persons') +
            '<g font-family="Times New Roman,serif" font-size="18" fill="#111">'
            '<rect x="100" y="10" width="44" height="54" fill="none" stroke="#111"/><path d="M100 37H144" stroke="#111"/>'
            '<text x="106" y="31" font-style="italic">4M</text><text x="106" y="58" font-style="italic">2W</text>'
            '<path d="M152 50H200" stroke="#111"/><path d="M152 50l9-4v8z" fill="#111"/><text x="208" y="56" font-style="italic">K</text>'
            '<text x="40" y="100" font-style="italic">N</text><path d="M58 94H96" stroke="#111"/><path d="M104 94l-9-4v8z" fill="#111"/>'
            f'<text x="110" y="100">{persons}</text></g></svg>')


b = Builder()
b.h('3.4.2 Hypergeometric probability mass function', '3.4.2 ہائپر جیومیٹرک احتمالی کمیتی تفاعل', '3.4.2 د هایپرجیومټریک د احتمال کتلوي تابع')
b.p('The probability mass function of hypergeometric random variable X is given as:', 'ہائپر جیومیٹرک تصادفی متغیر X کا احتمالی کمیتی تفاعل یہ ہے:', 'د هایپرجیومټریک تصادفي متغیر X د احتمال کتلوي تابع دا ده:')
b.eq(r'p(x)=\left\{\begin{matrix}\dfrac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}, & x=0,1,2,\ldots,\min(n,K)\\ 0 & \textit{otherwise}\end{matrix}\right.')
b.p('This distribution has three parameters N, K, n, whereas', 'اس تقسیم کے تین پیرامیٹر N، K، n ہیں، جہاں', 'دا وېش درې پارامټرونه N، K، n لري، چې')
b.group('list', [
    ('N denotes total number of items in the population.', 'N آبادی میں اشیاء کی کل تعداد ظاہر کرتا ہے۔', 'N په نفوس کې د توکو ټول شمېر ښيي.'),
    ('K denotes the number of successes in the population.', 'K آبادی میں کامیابیوں کی تعداد ظاہر کرتا ہے۔', 'K په نفوس کې د بریاوو شمېر ښيي.'),
    ('n denotes the number of elements in the sample drawn at random.', 'n تصادفی طور پر لیے گئے نمونے میں عناصر کی تعداد ظاہر کرتا ہے۔', 'n په تصادفي ډول اخیستل شوې نمونه کې د عناصرو شمېر ښيي.'),
    ('X denotes the number of successes in the sample.', 'X نمونے میں کامیابیوں کی تعداد ظاہر کرتا ہے۔', 'X په نمونه کې د بریاوو شمېر ښيي.'),
])
b.h('Example 3.20', 'مثال 3.20', 'بېلګه 3.20')
b.p('A committee of size three is selected from 4 men and 2 women. Find the probability distribution for the number of women in the committee.', '4 مردوں اور 2 عورتوں میں سے تین افراد کی کمیٹی منتخب کی جاتی ہے۔ کمیٹی میں عورتوں کی تعداد کی احتمالی تقسیم معلوم کریں۔', 'له 4 سړیو او 2 ښځو څخه د درېیو کسانو یوه کمېټه ټاکل کېږي. په کمېټه کې د ښځو د شمېر احتمالي وېش پیدا کړئ.')
b.h(*SOL)
b.p('we have', 'ہمارے پاس ہے', 'موږ لرو')
b.visual('stat12-ex3-20-box', box_svg('en'), box_svg('ur'), box_svg('ps'), ratio=.4)
b.p('As it has not been mentioned that an object selected is returned to the population before next draw so, we consider it without replacement sampling case and hence hypergeometric probability distribution is required.',
    'چونکہ یہ ذکر نہیں کیا گیا کہ منتخب شے اگلی بار نکالنے سے پہلے آبادی میں واپس رکھی جاتی ہے، اس لیے ہم اسے بغیر واپسی نمونہ گیری کی صورت سمجھتے ہیں اور لہٰذا ہائپر جیومیٹرک احتمالی تقسیم درکار ہے۔',
    'څرنګه چې دا نه دي ویل شوي چې ټاکل شوی شی د بل ځل له راایستلو مخکې نفوس ته بېرته ورکول کېږي، نو دا د بې له بېرته اچولو نمونه اخیستنې حالت ګڼو او له همدې امله هایپرجیومټریک احتمالي وېش ته اړتیا ده.')
b.p('Now $n=3$ (size of committee)', 'اب $n=3$ (کمیٹی کا سائز)', 'اوس $n=3$ (د کمېټې اندازه)')
b.p('$K=2$ (number of successes)', '$K=2$ (کامیابیوں کی تعداد)', '$K=2$ (د بریاوو شمېر)')
b.p('$X=0,1,2$ (number of women in the committee)', '$X=0,1,2$ (کمیٹی میں عورتوں کی تعداد)', '$X=0,1,2$ (په کمېټه کې د ښځو شمېر)')
b.p('Hence the fitted hypergeometric probability function is:', 'لہٰذا منطبق ہائپر جیومیٹرک احتمالی تفاعل یہ ہے:', 'نو برابره شوې هایپرجیومټریک احتمالي تابع دا ده:')
b.eq(r'p(x)=\left\{\begin{matrix}\dfrac{\binom{2}{x}\binom{6-2}{3-x}}{\binom{6}{3}}, & x=0,1,2\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('The hypergeometric probability distribution is:', 'ہائپر جیومیٹرک احتمالی تقسیم یہ ہے:', 'هایپرجیومټریک احتمالي وېش دا دی:')
rows = [[str(k), f'$\\dfrac{{\\binom{{2}}{{{k}}}\\binom{{4}}{{3-{k}}}}}{{\\binom{{6}}{{3}}}}=\\frac{{{v}}}{{20}}$'] for k, v in [(0, 4), (1, 12), (2, 4)]]
b.grid('stat12-t-ex3-20', ['$X$', '$p(x)=\\dfrac{\\binom{2}{x}\\binom{4}{3-x}}{\\binom{6}{3}}$'], rows + [['Total', '1']])
rec = b.build('stat12-p054-hypergeometric-pmf', '3.4.2 Hypergeometric pmf — Example 3.20', '3.4.2 ہائپر جیومیٹرک تفاعل — مثال 3.20', '3.4.2 هایپرجیومټریک تابع — بېلګه 3.20', 54, [99, 100])

if __name__ == '__main__':
    save(54, [(3, rec)])
