"""PDF133 printed 257–258: Example 7.12 steps iv–vi (Z = −0.44); Example 7.13 (heart disease, pooled proportion, Z = 3.41)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
b.mlines([r'\text{Here}\ n_1=200,\quad X_1=56', r'n_2=150,\quad X_2=30', r'\text{So}',
          r'\hat{p}_1=\frac{X_1}{n_1}=\frac{56}{200}=0.28,\ \hat{q}_1=1-\hat{p}_1=1-0.28=0.72',
          r'\hat{p}_2=\frac{X_2}{n_2}=\frac{30}{150}=0.2,\ \hat{q}_2=1-\hat{p}_2=1-0.2=0.8',
          r'\text{Hence } Z=\frac{(0.28-0.2)-0.10}{\sqrt{\frac{(0.28)(0.72)}{200}+\frac{(0.2)(0.8)}{150}}}=\frac{-0.02}{0.0455}=-0.44'])
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.vpara('stat12-ex7-12-cr', tail_test('left', z=1.645, mid='', ticks=((-1.645, '−1.645'), (0, '0')), label='Left-tailed critical region at −1.645'),
        'Reject $H_0$ if Z-calculated value is less than $-Z_\\alpha=-1.645$', '$H_0$ کو رد کریں اگر Z کی معلوم کی گئی قیمت $-Z_\\alpha=-1.645$ سے کم ہو', '$H_0$ رد کړئ که د Z محاسبه شوی قیمت له $-Z_\\alpha=-1.645$ کم وي', ratio=.45)
b.p('vi. Decision:', 'vi. فیصلہ:', 'vi. پرېکړه:')
b.p('As computed value of Z falls in the acceptance region, so we accept $H_0$.', 'چونکہ Z کی معلوم کی گئی قیمت قبولیت کے علاقے میں آتی ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں۔', 'څرنګه چې د Z محاسبه شوی قیمت د منلو په سیمه کې لوېږي، نو $H_0$ منو.')
e712 = b.build('stat12-p133-example-7-12', 'Example 7.12 — difference of proportions (soap brands)', 'مثال 7.12 — تناسبات کا فرق (صابن کے برانڈ)', 'بېلګه 7.12 — د تناسبونو توپیر (د صابون برانډونه)', 133, [257])

c = Builder()
c.h('Example 7.13', 'مثال 7.13', 'بېلګه 7.13')
c.p('The records of a hospital show that 52 men in a sample of 1000 men versus 23 women in a sample of 1000 women were admitted because of heart disease. Do these data present sufficient evidence to indicate a higher rate of heart disease among men admitted to the hospital? Use α = 0.05.',
    'ایک ہسپتال کے ریکارڈ سے ظاہر ہوتا ہے کہ 1000 مردوں کے نمونے میں 52 مرد جبکہ 1000 عورتوں کے نمونے میں 23 عورتیں دل کی بیماری کی وجہ سے داخل ہوئیں۔ کیا یہ مواد ہسپتال میں داخل مردوں میں دل کی بیماری کی زیادہ شرح کا کافی ثبوت پیش کرتا ہے؟ α = 0.05 استعمال کریں۔',
    'د یوه روغتون ریکارډونه ښيي چې د 1000 نارینه وو په نمونه کې 52 نارینه، د 1000 ښځو په نمونه کې د 23 ښځو پر وړاندې، د زړه د ناروغۍ له امله بستر شوي. آیا دا معلومات په روغتون کې د بستر شویو نارینه وو ترمنځ د زړه د ناروغۍ د لوړې کچې لپاره کافي شواهد وړاندې کوي؟ α = 0.05 وکاروئ.')
c.h(*SOL)
c.p('Let $p_1$ denote the proportion of men with heart disease and $p_2$ denote the proportion of women with heart disease.', 'فرض کریں $p_1$ دل کی بیماری والے مردوں کا تناسب اور $p_2$ دل کی بیماری والی عورتوں کا تناسب ظاہر کرتا ہے۔', 'فرض کړئ $p_1$ د زړه د ناروغۍ لرونکو نارینه وو تناسب او $p_2$ د زړه د ناروغۍ لرونکو ښځو تناسب ښيي.')
c.group('lines', [('i $H_0:p_1\\le p_2$ or $p_1-p_2\\le 0$', 'i $H_0:p_1\\le p_2$ یا $p_1-p_2\\le 0$', 'i $H_0:p_1\\le p_2$ یا $p_1-p_2\\le 0$'),
                  ('$H_1:p_1>p_2$ or $p_1-p_2>0$', '$H_1:p_1>p_2$ یا $p_1-p_2>0$', '$H_1:p_1>p_2$ یا $p_1-p_2>0$'),
                  ('ii $\\alpha=0.05$',) * 3, ('iii Test statistic:', 'iii جانچ کا شماریہ:', 'iii د ازموینې احصاییه:')])
ZC = r'Z=\frac{(\hat{p}_1-\hat{p}_2)-(p_1-p_2)}{\sqrt{\hat{p}_c\hat{q}_c(\frac{1}{n_1}+\frac{1}{n_2})}}'
c.p(f'From $H_0$ we see that $p_1=p_2$ but unknown. So it is better to use a pooled estimate for the unknown value of the proportion. The estimated test-statistic to be employed here is ${ZC}$',
    f'$H_0$ سے ہم دیکھتے ہیں کہ $p_1=p_2$ لیکن نامعلوم ہیں۔ لہٰذا تناسب کی نامعلوم قیمت کے لیے مشترکہ تخمین استعمال کرنا بہتر ہے۔ یہاں استعمال ہونے والا تخمینی جانچ کا شماریہ ${ZC}$ ہے',
    f'له $H_0$ څخه وینو چې $p_1=p_2$ خو نامعلوم دي. نو د تناسب د نامعلوم قیمت لپاره د ګډ اټکل کارول غوره دي. دلته کارېدونکې اټکل شوې د ازموینې احصاییه ${ZC}$ ده')
c.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
c.mlines([r'\text{Given } n_1=1000,\ X_1=52,\ \hat{p}_1=\frac{X_1}{n_1}=\frac{52}{1000}=0.052,',
          r'n_2=1000,\ X_2=23,\ \hat{p}_2=\frac{X_2}{n_2}=\frac{23}{1000}=0.023',
          r'\text{Now}\ \hat{p}_c=\frac{n_1\hat{p}_1+n_2\hat{p}_2}{n_1+n_2}=\frac{52+23}{1000+1000}=\frac{75}{2000}=0.0375',
          r'\text{And}\ \hat{q}_c=1-\hat{p}_c=1-0.0375=0.9625',
          r'\text{Hence } Z=\frac{(0.052-0.023)-0}{\sqrt{(0.0375)(0.9625)\left(\frac{1}{1000}+\frac{1}{1000}\right)}}=3.41'])
c.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
c.p('Reject $H_0$ if $Z>Z_\\alpha$, whereas $Z_\\alpha=Z_{0.05}=1.645$', '$H_0$ کو رد کریں اگر $Z>Z_\\alpha$، جبکہ $Z_\\alpha=Z_{0.05}=1.645$', '$H_0$ رد کړئ که $Z>Z_\\alpha$، په داسې حال کې چې $Z_\\alpha=Z_{0.05}=1.645$')
c.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
c.vpara('stat12-ex7-13-cr', tail_test('right', z=1.645, mid='', ticks=((0, '0'), (1.645, '1.645')), label='Right-tailed critical region at 1.645'),
        'Z = 3.41 falls in the rejection region, so we reject $H_0$. This observed data indicates that the percentage of men entering the hospital because of heart disease is higher than that of women.',
        'Z = 3.41 رد کے علاقے میں آتا ہے، لہٰذا ہم $H_0$ رد کرتے ہیں۔ یہ مشاہدہ شدہ مواد ظاہر کرتا ہے کہ دل کی بیماری کی وجہ سے ہسپتال میں داخل ہونے والے مردوں کی فیصد عورتوں سے زیادہ ہے۔',
        'Z = 3.41 د ردولو په سیمه کې لوېږي، نو $H_0$ ردوو. دا لیدل شوي معلومات ښيي چې د زړه د ناروغۍ له امله روغتون ته د راتلونکو نارینه وو سلنه د ښځو په پرتله لوړه ده.', ratio=.4)
e713 = c.build('stat12-p133-example-7-13', 'Example 7.13 — pooled proportion test (heart disease)', 'مثال 7.13 — مشترکہ تناسب کی جانچ (دل کی بیماری)', 'بېلګه 7.13 — د ګډ تناسب ازموینه (د زړه ناروغي)', 133, [257, 258])

if __name__ == '__main__':
    save(133, [(7, e712), (7, e713)])
