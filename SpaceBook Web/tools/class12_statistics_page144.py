"""PDF144 printed 279–280: Example 8.4 (mathematical vs general ability, 3×3) — data, steps i–iv, expected frequencies and χ² = 46.994 computation table."""
from class12_statistics_common import Builder, save

CORNER = ('General ability \\ Mathematical ability', 'عمومی قابلیت \\ ریاضیاتی قابلیت', 'عمومي وړتیا \\ ریاضیاتي وړتیا')
LV = {'en': ('Good', 'Fair', 'Poor', 'Total'), 'ur': ('اچھی', 'مناسب', 'کمزور', 'میزان'), 'ps': ('ښه', 'منځنۍ', 'کمزورې', 'ټول')}
def hdr(lang, total=False):
    g, f, p, t = LV[lang]
    h = [CORNER[['en', 'ur', 'ps'].index(lang)], f'{g} $B_1$', f'{f} $B_2$', f'{p} $B_3$']
    return h + [t] if total else h

b = Builder()
b.h('Example 8.4', 'مثال 8.4', 'بېلګه 8.4')
b.p('Consider the data given in the following contingency table', 'درج ذیل اتفاقی جدول میں دیے گئے مواد پر غور کریں', 'په لاندې احتمالي جدول کې ورکړل شوي معلومات په پام کې ونیسئ')
data = [['44', '82', '44'], ['265', '257', '178'], ['41', '91', '98']]
lab = lambda lang: [[LV[lang][i]] + data[i] for i in range(3)]
b.table('stat12-t-ex8-4-data', hdr('en'), lab('en'), hdr('ur'), hdr('ps'), lab('ur'), lab('ps'))
b.p('Discuss the association between the two attributes i.e. mathematical ability and general ability.', 'دو صفات یعنی ریاضیاتی قابلیت اور عمومی قابلیت کے درمیان تلازم پر بحث کریں۔', 'د دوو صفتونو یعنې ریاضیاتي وړتیا او عمومي وړتیا ترمنځ پر تړاو بحث وکړئ.')
b.h('Solution:', 'حل:', 'حل:')
b.group('lines', [
    ('i. $H_0$: There is no association between attributes.', 'i. $H_0$: صفات کے درمیان کوئی تلازم نہیں۔', 'i. $H_0$: د صفتونو ترمنځ هېڅ تړاو نشته.'),
    ('$H_1$: There is association.', '$H_1$: تلازم موجود ہے۔', '$H_1$: تړاو شته.'),
    ('ii. We choose $\\alpha=0.05$', 'ii. ہم $\\alpha=0.05$ منتخب کرتے ہیں', 'ii. موږ $\\alpha=0.05$ ټاکو'),
    ('iii. Test statistic to be used here is', 'iii. یہاں استعمال ہونے والا جانچ کا شماریہ یہ ہے', 'iii. دلته کارېدونکې د ازموینې احصاییه دا ده'),
])
b.eq(r'\chi^2=\sum_{i=1}^{r}\sum_{j=1}^{c}\frac{(O_{ij}-e_{ij})^2}{e_{ij}}\ \text{with}\ \nu=(r-1)(c-1)\ \text{d.f}')
b.p('iv. Calculation', 'iv. حساب', 'iv. محاسبه')
b.p('$(O_{ij})$', '$(O_{ij})$', '$(O_{ij})$')
obs = [['44', '82', '44', '170'], ['265', '257', '178', '700'], ['41', '91', '98', '230']]
def olab(lang):
    return [[f'{LV[lang][i]} $A_{i + 1}$'] + obs[i] for i in range(3)] + [[LV[lang][3], '350', '430', '320', '1100']]
b.table('stat12-t-ex8-4-obs', hdr('en', True), olab('en'), hdr('ur', True), hdr('ps', True), olab('ur'), olab('ps'))
b.p('The expected frequencies are obtained by multiplying respective rows and columns totals and are divided by total sample size n as given in the table.', 'متوقع تعدد متعلقہ قطاروں اور کالموں کے میزان کو ضرب دے کر اور کل نمونے کے سائز n سے تقسیم کر کے حاصل کیے جاتے ہیں جیسا کہ جدول میں دیا گیا ہے۔', 'تمه شوي تکرارونه د اړوندو قطارونو او ستونونو د ټولټالونو په ضربولو او د نمونې په ټولې اندازې n وېشلو سره ترلاسه کېږي لکه څنګه چې په جدول کې ورکړل شوي.')
b.p('$(e_{ij})$', '$(e_{ij})$', '$(e_{ij})$')
F = lambda r, c, v: f'$\\frac{{{r}\\times {c}}}{{1100}}={v}$'
exp = [[F(170, 350, '54.09'), F(170, 430, '66.45'), F(170, 320, '49.45'), '169.99'],
       [F(700, 350, '222.73'), F(700, 430, '273.64'), F(700, 320, '203.63'), '700.01'],
       [F(230, 350, '73.18'), F(230, 430, '89.91'), F(230, 320, '66.91'), '230']]
def elab(lang):
    return [[f'{LV[lang][i]} $A_{i + 1}$'] + exp[i] for i in range(3)] + [[LV[lang][3], '350', '430', '320', '1100']]
b.table('stat12-t-ex8-4-exp', hdr('en', True), elab('en'), hdr('ur', True), hdr('ps', True), elab('ur'), elab('ps'))
b.p('Now $\\chi^2$ test statistic value is computed as;', 'اب $\\chi^2$ جانچ کے شماریے کی قیمت یوں معلوم کی جاتی ہے؛', 'اوس د $\\chi^2$ د ازموینې احصاییې قیمت داسې محاسبه کېږي؛')
C = """44 54.09 −10.09 101.81 1.882
265 222.73 42.27 1786.75 8.022
41 73.18 −32.18 1035.55 14.151
82 66.45 15.55 241.80 3.639
257 273.64 −16.64 276.8896 1.012
91 89.91 1.09 1.188 0.013
44 49.45 −5.45 29.70 0.601
178 203.63 −25.64 657.41 3.228
98 66.91 31.09 966.59 14.446"""
rows = [r.split() for r in C.splitlines()] + [['1100', '1100', '-', '-', '$\\chi^2=46.994$']]
b.grid('stat12-t-ex8-4-chisq', ['$O_{ij}$', '$e_{ij}$', '$(O_{ij}-e_{ij})$', '$(O_{ij}-e_{ij})^2$', '$\\frac{(O_{ij}-e_{ij})^2}{e_{ij}}$'], rows)
rec = b.build('stat12-p144-example-8-4', 'Example 8.4 — χ² test: mathematical and general ability', 'مثال 8.4 — χ² جانچ: ریاضیاتی اور عمومی قابلیت', 'بېلګه 8.4 — χ² ازموینه: ریاضیاتي او عمومي وړتیا', 144, [279, 280])
issues = [{'id': 'stat12-p280-expected-203', 'unit': 8, 'printedPage': 280, 'description': 'Example 8.4 prints e₂₃ = 700×320/1100 = 203.63 (computes to 203.64) and O−e = −25.64 beside it; row totals printed 169.99 and 700.01 from rounding. Printed values retained; χ² = 46.994 verified.'}]

if __name__ == '__main__':
    save(144, [(8, rec)], issues=issues)
