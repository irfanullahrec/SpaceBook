"""PDF155 printed 301–302: 9.3.5 ANOVA table and sum-of-squares formulas; 9.3.6 general procedure for one-way ANOVA."""
from class12_statistics_common import Builder, save

b = Builder()
b.h('9.3.5 ANOVA table', '9.3.5 ANOVA جدول', '9.3.5 د ANOVA جدول')
b.p('For convenience all sources of variation (S.O.V), degrees of freedom (df), sum of squares (S.S), mean squares (M.S) are presented in tabular form, called ANOVA table given below:', 'سہولت کے لیے تغیر کے تمام ذرائع (S.O.V)، درجاتِ آزادی (df)، مربعوں کے مجموعے (S.S) اور اوسط مربعے (M.S) جدولی شکل میں پیش کیے جاتے ہیں جسے ANOVA جدول کہتے ہیں، جو نیچے دیا گیا ہے:', 'د اسانتیا لپاره د تغیر ټولې سرچینې (S.O.V)، د ازادۍ درجې (df)، د مربعو مجموعې (S.S) او منځني مربعې (M.S) د جدول په بڼه وړاندې کېږي چې د ANOVA جدول بلل کېږي، لاندې ورکړل شوی:')
b.p('ANOVA table', 'ANOVA جدول', 'د ANOVA جدول')
R = lambda tr, er, to: [[tr, '$k-1$', '$T_rSS$', '$\\frac{TrSS}{k-1}=MSTr$', '$F_c=\\frac{MSTr}{MSE}$'], [er, '$n-k$', 'ESS', '$\\frac{ESS}{n-k}=MSE$', '—'], [to, '$n-1$', 'TSS', '$\\frac{TSS}{n-1}=MST$', '—']]
H = ['S.O.V', 'df', 'S.S', 'M.S', '$F_{cal}$']
b.table('stat12-t-anova', H, R('Treatment', 'Error', 'Total'), H, H, R('علاج', 'خطا', 'میزان'), R('درملنه', 'تېروتنه', 'ټول'))
b.p('This table is used for testing hypothesis $H_0:\\mu_1=\\mu_2=\\cdots=\\mu_k$ in one way analysis of variance.', 'یہ جدول یک طرفہ تجزیۂ تغیر میں مفروضے $H_0:\\mu_1=\\mu_2=\\cdots=\\mu_k$ کی جانچ کے لیے استعمال ہوتا ہے۔', 'دا جدول په یو اړخیز د واریانس تحلیل کې د $H_0:\\mu_1=\\mu_2=\\cdots=\\mu_k$ فرضیې د ازموینې لپاره کارول کېږي.')
b.h('Formulas for sum of squares', 'مربعوں کے مجموعے کے فارمولے', 'د مربعو د مجموعې فورمولونه')
b.lab(r'\text{C.F}=\frac{T_{..}^2}{n}', 'Correction factor', 'تصحیحی عامل', 'د سمون عامل')
b.lab(r'\text{TSS}=\sum_{j=1}^{k}\sum_{i=1}^{r}x_{ij}^2-\text{C.F}', 'Total sum of squares', 'مربعوں کا کل مجموعہ', 'د مربعو ټوله مجموعه')
b.lab(r'TrSS=\frac{\sum_{j=1}^{k}T_j^2}{r}-C.F', 'Treatment sum of squares', 'علاج کے مربعوں کا مجموعہ', 'د درملنې د مربعو مجموعه')
b.lab(r'\text{ESS}=\text{TSS}-T_r\text{SS}', 'Error sum of squares', 'خطا کے مربعوں کا مجموعہ', 'د تېروتنې د مربعو مجموعه')
at = b.build('stat12-p155-anova-table', '9.3.5 ANOVA table and sum-of-squares formulas', '9.3.5 ANOVA جدول اور مربعوں کے مجموعے کے فارمولے', '9.3.5 د ANOVA جدول او د مربعو د مجموعې فورمولونه', 155, [301])

c = Builder()
c.h('9.3.6 General procedure for testing hypothesis in case of one way ANOVA (equal sample size case)', '9.3.6 یک طرفہ ANOVA کی صورت میں مفروضے کی جانچ کا عمومی طریقہ (برابر نمونہ سائز کی صورت)', '9.3.6 د یو اړخیز ANOVA په حالت کې د فرضیې د ازموینې عمومي طریقه (د برابرې نمونې اندازې حالت)')
c.group('lines', [
    ('i. $H_0:\\mu_1=\\mu_2=\\cdots=\\mu_k$',) * 3,
    ('$H_1$: Not all means are equal', '$H_1$: تمام اوسط برابر نہیں', '$H_1$: ټول منځني برابر نه دي'),
    ('ii. Choose an appropriate level of significance', 'ii. معنویت کی موزوں سطح منتخب کریں', 'ii. د معنی‌داریت مناسبه کچه وټاکئ'),
    ('iii. Test statistic to be used in this case is', 'iii. اس صورت میں استعمال ہونے والا جانچ کا شماریہ یہ ہے', 'iii. په دې حالت کې کارېدونکې د ازموینې احصاییه دا ده'),
])
c.eq(r'F_c=\frac{MSTr}{MSE}\ \text{with}\ (\nu_1=k-1,\nu_2=n-k)\ \text{d.f}')
c.group('lines', [
    ('iv. Computations.', 'iv. حساب۔', 'iv. محاسبې.'),
    ('v. Critical region: reject $H_0$ if $F_{cal}\\ge F_{tab}$', 'v. فیصلہ کن علاقہ: $H_0$ کو رد کریں اگر $F_{cal}\\ge F_{tab}$', 'v. بحراني سیمه: $H_0$ رد کړئ که $F_{cal}\\ge F_{tab}$'),
    ('vi. Conclusion', 'vi. نتیجہ', 'vi. پایله'),
])
gp = c.build('stat12-p155-anova-procedure', '9.3.6 One-way ANOVA — general procedure', '9.3.6 یک طرفہ ANOVA — عمومی طریقہ', '9.3.6 یو اړخیز ANOVA — عمومي طریقه', 155, [302])

if __name__ == '__main__':
    save(155, [(9, at), (9, gp)])
