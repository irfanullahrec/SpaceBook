"""PDF158 printed 307–308: Example 9.1 calculation table, C.F, TSS, TrSS, ESS, ANOVA table, F = 4.93 > 3.89; 9.3.7 one-way ANOVA (unequal sample sizes) start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import chi_tail

b = Builder()
b.p('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:')
H = ['', '$x_1$', '$x_1^2$', '$x_2$', '$x_2^2$', '$x_3$', '$x_3^2$', 'Total']
R = [['', '8', '64', '14', '196', '10', '100', ''], ['', '7', '49', '16', '256', '12', '144', ''], ['', '9', '81', '12', '144', '16', '256', ''],
     ['', '13', '169', '17', '289', '15', '225', ''], ['', '10', '100', '11', '121', '12', '144', ''],
     ['$T_{.j}$', '47', '↓', '70', '↓', '65', '↓', '$182=T_{..}$'],
     ['$T^2_{.j}$', '2209', '', '4900', '', '4225', '', '$11334=\\sum_{j=1}^{3}T_j^2$'],
     ['$\\sum_{i=1}^{5}x_j^2$', '', '463', '', '1006', '', '869', '$\\rightarrow 2338=\\sum_{i=1}^{5}\\sum_{j=1}^{3}x_{ij}^2$']]
b.grid('stat12-t-ex9-1-calc', H, R)
b.mlines([r'C.F=\frac{T_{..}^2}{n}=\frac{(182)^2}{15}=2208.2667',
          r'TSS=\sum_{j=1}^{3}\sum_{i=1}^{5}x_{ij}^2-C.F=2338-2208.2667=129.7333',
          r'T_rSS=\frac{\sum_{j=1}^{3}T_{.j}^2}{r}-C.F=\frac{11334}{5}-2208.2667=58.5333',
          r'ESS=TSS-T_rSS=129.7333-58.5333=71.2'])
b.p('ANOVA table', 'ANOVA جدول', 'د ANOVA جدول')
AH = ['S.O.V', 'd.f', 'S.S', 'M.S', 'F']
AR = lambda t, e, to: [[t, '$3-1=2$', '58.5333', '$\\frac{58.5333}{2}=29.27$ MSTr', '$\\frac{MSTr}{MSE}=\\frac{29.27}{5.93}=4.93$'],
                       [e, '$15-3=12$', '71.2', '$\\frac{71.2}{12}=5.93$ MSE', '—'], [to, '$15-1=14$', '129.7333', '—', '—']]
b.table('stat12-t-ex9-1-anova', AH, AR('Treatments', 'Error', 'Total'), AH, AH, AR('علاج', 'خطا', 'میزان'), AR('درملنې', 'تېروتنه', 'ټول'))
b.p('v. Critical region', 'v. فیصلہ کن علاقہ', 'v. بحراني سیمه')
b.vpara('stat12-ex9-1-cr', chi_tail(3.89, df=4, xmax=7.5, label='F curve with rejection region beyond 3.89, α = 0.05'),
        'Reject $H_0$ if $F_c\\ge F_{tab}$ whereas from F-table 9.1 $F_{tab}=F_{\\alpha,(\\nu_1,\\nu_2)}=F_{0.05,(2,12)}=3.89$',
        '$H_0$ کو رد کریں اگر $F_c\\ge F_{tab}$ جبکہ F-جدول 9.1 سے $F_{tab}=F_{\\alpha,(\\nu_1,\\nu_2)}=F_{0.05,(2,12)}=3.89$',
        '$H_0$ رد کړئ که $F_c\\ge F_{tab}$ په داسې حال کې چې له 9.1 F-جدول څخه $F_{tab}=F_{\\alpha,(\\nu_1,\\nu_2)}=F_{0.05,(2,12)}=3.89$', ratio=.45)
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('Since $F_c=4.93$ falls in the rejection region, therefore, we reject $H_0$ and conclude that average attention span of students is different for the three treatments (types of breakfast).', 'چونکہ $F_c=4.93$ رد کے علاقے میں آتا ہے، لہٰذا ہم $H_0$ رد کرتے ہیں اور نتیجہ نکالتے ہیں کہ طلبہ کا اوسط توجہ کا دورانیہ تینوں علاج (ناشتے کی اقسام) کے لیے مختلف ہے۔', 'څرنګه چې $F_c=4.93$ د ردولو په سیمه کې لوېږي، نو $H_0$ ردوو او پایله اخلو چې د زده کوونکو د پاملرنې منځنۍ موده د درېیو درملنو (د ناري ډولونو) لپاره بېلابېله ده.')
e91 = b.build('stat12-p158-example-9-1', 'Example 9.1 — calculation, ANOVA table and conclusion', 'مثال 9.1 — حساب، ANOVA جدول اور نتیجہ', 'بېلګه 9.1 — محاسبه، د ANOVA جدول او پایله', 158, [307, 308])

c = Builder()
c.h('9.3.7 One way ANOVA (unequal sample sizes)', '9.3.7 یک طرفہ ANOVA (غیر برابر نمونہ سائز)', '9.3.7 یو اړخیز ANOVA (نابرابرې نمونې اندازې)')
c.p('Practically sample sizes may not always be equal. One way ANOVA for equal sample sizes will still be used with minor changes in the sum of square formulas as follows:', 'عملاً نمونوں کے سائز ہمیشہ برابر نہیں ہوتے۔ برابر نمونہ سائز کے لیے یک طرفہ ANOVA مربعوں کے مجموعے کے فارمولوں میں معمولی تبدیلیوں کے ساتھ اب بھی یوں استعمال ہوگا:', 'په عمل کې د نمونو اندازې تل برابرې نه وي. د برابرو نمونو لپاره یو اړخیز ANOVA به د مربعو د مجموعې په فورمولونو کې د لږو بدلونونو سره داسې وکارول شي:')
c.eq(r'n=r_1+r_2+\ldots\ldots+r_k=\sum_{j=1}^{k}r_j')
un = c.build('stat12-p158-unequal-start', '9.3.7 One-way ANOVA with unequal sample sizes (start)', '9.3.7 غیر برابر نمونہ سائز کے ساتھ یک طرفہ ANOVA (آغاز)', '9.3.7 د نابرابرو نمونو سره یو اړخیز ANOVA (پیل)', 158, [308])

if __name__ == '__main__':
    save(158, [(9, e91), (9, un)])
