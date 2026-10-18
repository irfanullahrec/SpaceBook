"""PDF66 printed 123–124: 4.2.4 standard normal pdf, 4.2.5 area under the curve, Table 4.1 (z = 0 … 1.5)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import normal_shaded

PRINTED = '''0 0.0040 0.0080 0.0120 0.0159 0.0199 0.0239 0.0279 0.0319 0.0359
0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0754
0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1106 0.1141
0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517
0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879
0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224
0.2258 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2518 0.2549
0.2580 0.2612 0.2642 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852
0.2881 0.2910 0.2939 0.2967 0.2996 0.3023 0.3051 0.3078 0.3106 0.3133
0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389
0.3413 0.3438 0.3461 0.3485 0.3508 0.3531 0.3554 0.3577 0.3599 0.3621
0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830
0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3990 0.3997 0.4015
0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177
0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319
0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4430 0.4441'''


def table_rows(text, z0):
    rows = []
    for i, line in enumerate(text.split('\n')):
        vals = line.split()
        assert len(vals) == 10, line
        z = round(z0 + i / 10, 1)
        rows.append([('0' if z == 0 else f'{z:.1f}')] + vals)
    return rows


b = Builder()
b.h('4.2.4 Definition of standard Normal probability distribution', '4.2.4 معیاری نارمل احتمالی تقسیم کی تعریف', '4.2.4 د معیاري نورمال احتمالي وېش تعریف')
b.p('The probability density function of the standard normal random variable Z defined as', 'معیاری نارمل تصادفی متغیر Z کا احتمالی کثافتی تفاعل جو یوں متعین ہو', 'د معیاري نورمال تصادفي متغیر Z د احتمال کثافت تابع چې داسې تعریف شوې')
b.eq(r'f(z)=\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}},\qquad -\infty\le z\le\infty')
b.p('is called standard Normal probability distribution.', 'معیاری نارمل احتمالی تقسیم کہلاتا ہے۔', 'معیاري نورمال احتمالي وېش بلل کېږي.')
b.p('Total probability under the density is equal to one i.e. $\\int_{-\\infty}^{\\infty}\\frac{1}{\\sqrt{2\\pi}}e^{-\\frac{z^2}{2}}dz=1$. It is simply written as $Z\\sim N(0,1)$. The reason for using standard Normal probability distribution in place of Normal probability distribution is that:',
    'کثافت کے نیچے کل احتمال ایک کے برابر ہے یعنی $\\int_{-\\infty}^{\\infty}\\frac{1}{\\sqrt{2\\pi}}e^{-\\frac{z^2}{2}}dz=1$۔ اسے سادہ طور پر $Z\\sim N(0,1)$ لکھا جاتا ہے۔ نارمل احتمالی تقسیم کی جگہ معیاری نارمل احتمالی تقسیم استعمال کرنے کی وجہ یہ ہے کہ:',
    'د کثافت لاندې ټول احتمال له یو سره برابر دی یعنې $\\int_{-\\infty}^{\\infty}\\frac{1}{\\sqrt{2\\pi}}e^{-\\frac{z^2}{2}}dz=1$. په ساده ډول داسې لیکل کېږي $Z\\sim N(0,1)$. د نورمال احتمالي وېش پر ځای د معیاري نورمال احتمالي وېش د کارولو لامل دا دی چې:')
b.group('lines', [
    ('(i) To easily calculate the probabilities of Normal distribution i.e. $P[x_1<X<x_2]=P[z_1<Z<z_2]$, and probabilities of Z can directly be taken from table 4.1.', '(i) نارمل تقسیم کے احتمالات آسانی سے معلوم کرنے کے لیے یعنی $P[x_1<X<x_2]=P[z_1<Z<z_2]$، اور Z کے احتمالات براہِ راست جدول 4.1 سے لیے جا سکتے ہیں۔', '(i) د نورمال وېش احتمالونه په اسانۍ محاسبه کول یعنې $P[x_1<X<x_2]=P[z_1<Z<z_2]$، او د Z احتمالونه مستقیم له 4.1 جدول څخه اخیستل کېدای شي.'),
    ('(ii) Z is independent of the unit of measurement.', '(ii) Z پیمائش کی اکائی سے آزاد ہے۔', '(ii) Z د اندازه کولو له واحد څخه خپلواک دی.'),
])
b.h('4.2.5 Area (probability) under the standard normal curve', '4.2.5 معیاری نارمل منحنی کے نیچے رقبہ (احتمال)', '4.2.5 د معیاري نورمال منحني لاندې مساحت (احتمال)')
b.p('To compute probabilities of intervals in case of continuous random variables, it is a blessing that statisticians have designed tables in which areas (probabilities) have been compiled. In case of Normal distribution such a table is available for standard Normal probability distribution.',
    'مسلسل تصادفی متغیرات کی صورت میں وقفوں کے احتمالات معلوم کرنے کے لیے یہ ایک نعمت ہے کہ شماریات دانوں نے ایسے جدول تیار کیے ہیں جن میں رقبے (احتمالات) مرتب کیے گئے ہیں۔ نارمل تقسیم کی صورت میں ایسا جدول معیاری نارمل احتمالی تقسیم کے لیے دستیاب ہے۔',
    'د متصلو تصادفي متغیرونو په حالت کې د واټنونو د احتمالونو د محاسبې لپاره دا یوه نعمت ده چې احصایه پوهانو داسې جدولونه جوړ کړي چې پکې مساحتونه (احتمالونه) راټول شوي. د نورمال وېش په حالت کې داسې جدول د معیاري نورمال احتمالي وېش لپاره شته.')
intro = b.build('stat12-p066-standard-normal', '4.2.4–4.2.5 Standard normal distribution and areas', '4.2.4–4.2.5 معیاری نارمل تقسیم اور رقبے', '4.2.4–4.2.5 معیاري نورمال وېش او مساحتونه', 66, [123])

t = Builder()
t.h('Table 4.1: Areas under the standard Normal curve from 0 to z', 'جدول 4.1: معیاری نارمل منحنی کے نیچے 0 سے z تک رقبے', 'جدول 4.1: د معیاري نورمال منحني لاندې له 0 څخه تر z پورې مساحتونه')
t.p('The entries in this table are the probabilities that random variable having the standard Normal distribution takes on a value between 0 and z (the shaded area in the figure). For negative values of Z, areas are found by symmetry.',
    'اس جدول کے اندراجات وہ احتمالات ہیں کہ معیاری نارمل تقسیم والا تصادفی متغیر 0 اور z کے درمیان کوئی قیمت لے (شکل میں سایہ دار رقبہ)۔ Z کی منفی قیمتوں کے لیے رقبے تشاکل سے معلوم کیے جاتے ہیں۔',
    'د دې جدول درجونه هغه احتمالونه دي چې د معیاري نورمال وېش لرونکی تصادفي متغیر د 0 او z ترمنځ یو قیمت واخلي (په شکل کې سیوري لرونکی مساحت). د Z د منفي قیمتونو لپاره مساحتونه د تناظر له مخې پیدا کېږي.')
t.visual('stat12-table4-1-figure', normal_shaded(0, 1.4, labels=((0, '0'), (1.4, 'z')), marks=(0, 1.4), label='Shaded area under the standard normal curve from 0 to z'), ratio=.55)
cols = ['z', '0', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09']
t.grid('stat12-table4-1-a', cols, table_rows(PRINTED, 0.0))
tab = t.build('stat12-p066-table-4-1a', 'Table 4.1 Areas under the standard normal curve (z = 0 to 1.5)', 'جدول 4.1 معیاری نارمل منحنی کے نیچے رقبے (z = 0 تا 1.5)', 'جدول 4.1 د معیاري نورمال منحني لاندې مساحتونه (z = 0 تر 1.5)', 66, [124])
issues = [{'id': 'stat12-p124-table41-misprints', 'unit': 4, 'printedPage': 124, 'description': 'Table 4.1 entries kept as printed; printed values that differ from the exact standard-normal areas: z=0.04→0.0159 (0.0160), 0.19→0.0754 (0.0753), 0.28→0.1106 (0.1103), 0.60→0.2258 (0.2257), 0.68→0.2518 (0.2517), 0.71→0.2612 (0.2611), 0.84→0.2996 (0.2995), 1.27→0.3990 (0.3980), 1.58→0.4430 (0.4429).'}]

if __name__ == '__main__':
    save(66, [(4, intro), (4, tab)], issues=issues)
