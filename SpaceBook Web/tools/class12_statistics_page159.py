"""PDF159 printed 309–310: unequal-size SS formulas; Example 9.2 (CRD, three samples of 5, 5, 4) data, steps i–iv, calculation table, C.F, TSS, TrSS start."""
from class12_statistics_common import Builder, save

b = Builder()
b.mlines([r'TSS=\sum_{j=1}^{k}\sum_{i=1}^{r_j}x_{ij}^2-C.F', r'T_rSS=\sum_{j=1}^{k}\frac{T_{.j}^2}{r_j}-C.F'])
f = b.build('stat12-p159-unequal-formulas', '9.3.7 Unequal sample sizes — TSS and TrSS formulas', '9.3.7 غیر برابر نمونہ سائز — TSS اور TrSS کے فارمولے', '9.3.7 نابرابرې نمونې — د TSS او TrSS فورمولونه', 159, [309])

c = Builder()
c.h('Example 9.2', 'مثال 9.2', 'بېلګه 9.2')
c.p('The following observations are collected using a completely randomized design:', 'درج ذیل مشاہدات مکمل تصادفی ڈیزائن استعمال کر کے جمع کیے گئے ہیں:', 'لاندې مشاهدې د بشپړ تصادفي ډیزاین په کارولو راټولې شوې:')
D = [['3', '4', '2'], ['2', '3', '0'], ['4', '5', '2'], ['3', '2', '1'], ['2', '5', '']]
c.table('stat12-t-ex9-2', ['Sample1', 'Sample 2', 'Sample3'], D, ['نمونہ 1', 'نمونہ 2', 'نمونہ 3'], ['نمونه 1', 'نمونه 2', 'نمونه 3'], D, D)
c.p('Construct an ANOVA table for the data and determine whether there is a difference in the three population means. Use α = 0.01', 'مواد کے لیے ANOVA جدول بنائیں اور معلوم کریں کہ کیا تینوں آبادیوں کے اوسطوں میں فرق ہے۔ α = 0.01 استعمال کریں', 'د معلوماتو لپاره د ANOVA جدول جوړ کړئ او وټاکئ چې آیا د درېیو نفوسونو په منځنیو کې توپیر شته. α = 0.01 وکاروئ')
c.h('Solution:', 'حل:', 'حل:')
c.group('lines', [('i. $H_0:\\mu_1=\\mu_2=\\mu_3$',) * 3, ('$H_1$: Not all means are equal', '$H_1$: تمام اوسط برابر نہیں', '$H_1$: ټول منځني برابر نه دي'), ('ii. $\\alpha=0.01$',) * 3,
                  ('iii. Test statistic to be used is', 'iii. استعمال ہونے والا جانچ کا شماریہ یہ ہے', 'iii. کارېدونکې د ازموینې احصاییه دا ده')])
c.eq(r'F=\frac{MSTr}{MSE}\ \text{with}\ (\nu_1=k-1,\nu_2=n-k)\ \text{d.f}')
c.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
H = ['', '$x_1$', '$x_1^2$', '$x_2$', '$x_2^2$', '$x_3$', '$x_3^2$', 'Total']
R = [['', '3', '9', '4', '16', '2', '4', ''], ['', '2', '4', '3', '9', '0', '0', ''], ['', '4', '16', '5', '25', '2', '4', ''], ['', '3', '9', '2', '4', '1', '1', ''], ['', '2', '4', '5', '25', '', '', ''],
     ['$T_{.j}$', '14', '↓', '19', '↓', '5', '↓', '$38=T_{..}$'], ['$T^2_{.j}$', '196', '', '361', '', '25', '', ''],
     ['$\\sum_{i=1}^{5}x_j^2$', '', '42', '', '79', '', '9', '$130=\\sum\\sum x_{ij}^2$']]
c.grid('stat12-t-ex9-2-calc', H, R)
c.mlines([r'n=r_1+r_2+r_3=5+5+4=14', r'C.F=\frac{T_{..}^2}{n}=\frac{(38)^2}{14}=103.1429',
          r'TSS=\sum_{j=1}^{3}\sum_{i=1}^{r_j}x_{ij}^2-C.F=130-103.1429=26.8571',
          r'T_rSS=\sum_{j=1}^{3}\frac{T_{.j}^2}{r_j}-C.F', r'=\left[\frac{T_{.1}^2}{r_1}+\frac{T_{.2}^2}{r_2}+\frac{T_{.3}^2}{r_3}\right]-C.F'])
e92 = c.build('stat12-p159-example-9-2', 'Example 9.2 — one-way ANOVA with unequal sample sizes (calculation)', 'مثال 9.2 — غیر برابر نمونہ سائز کے ساتھ یک طرفہ ANOVA (حساب)', 'بېلګه 9.2 — د نابرابرو نمونو سره یو اړخیز ANOVA (محاسبه)', 159, [309, 310])

if __name__ == '__main__':
    save(159, [(9, f), (9, e92)])
