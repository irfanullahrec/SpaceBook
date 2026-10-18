"""PDF154 printed 299–300: assumptions (iii)–(iv); 9.3.2 one-way ANOVA data layout table; 9.3.3 components of total SS and F-test; 9.3.4 components of degrees of freedom."""
from class12_statistics_common import Builder, save

b = Builder()
b.group('lines', [
    ('iii) Homogeneity', 'iii) یکسانیت', 'iii) همجنسیت'),
    ('All populations under study have equal variance i.e. $\\sigma_1^2=\\sigma_2^2=\\ldots=\\sigma_k^2=\\sigma^2$', 'زیرِ مطالعہ تمام آبادیوں کا تغیر برابر ہے یعنی $\\sigma_1^2=\\sigma_2^2=\\ldots=\\sigma_k^2=\\sigma^2$', 'تر څېړنې لاندې ټول نفوسونه برابر واریانس لري یعنې $\\sigma_1^2=\\sigma_2^2=\\ldots=\\sigma_k^2=\\sigma^2$'),
    ('iv) Additivity', 'iv) جمع پذیری', 'iv) جمع‌پذیري'),
    ('The random observations $X_{ij}$ can be expressed as the sum of means $\\mu_j$ and the error terms $\\varepsilon_{ij}$ as $X_{ij}=\\mu_j+\\varepsilon_{ij}$', 'تصادفی مشاہدات $X_{ij}$ کو اوسط $\\mu_j$ اور خطا کی رقوم $\\varepsilon_{ij}$ کے مجموعے کے طور پر یوں ظاہر کیا جا سکتا ہے $X_{ij}=\\mu_j+\\varepsilon_{ij}$', 'تصادفي مشاهدې $X_{ij}$ د منځنیو $\\mu_j$ او د تېروتنې د حدونو $\\varepsilon_{ij}$ د مجموعې په توګه داسې ښودل کېدای شي $X_{ij}=\\mu_j+\\varepsilon_{ij}$'),
])
b.p('Note that in practice minor deviations from the assumptions is tolerated but serious violation of these assumptions will damage the ANOVA procedure.', 'نوٹ کریں کہ عملاً مفروضات سے معمولی انحراف برداشت کیا جاتا ہے لیکن ان مفروضات کی سنگین خلاف ورزی ANOVA کے طریقے کو نقصان پہنچائے گی۔', 'پام وکړئ چې په عمل کې له فرضیو لږ انحراف زغمل کېږي خو د دې فرضیو جدي سرغړونه به د ANOVA طریقې ته زیان ورسوي.')
b.h('9.3.2 One way analysis of variance (equal sample size case)', '9.3.2 یک طرفہ تجزیۂ تغیر (برابر نمونہ سائز کی صورت)', '9.3.2 یو اړخیز د واریانس تحلیل (د برابرې نمونې اندازې حالت)')
b.p('The observed data of k samples collected for k treatments, each of size r such that rk = n can be arranged in tabular form as:', 'k علاج کے لیے جمع کیے گئے k نمونوں کا مشاہدہ شدہ مواد، جن میں سے ہر ایک کا سائز r ہو اس طرح کہ rk = n، جدولی شکل میں یوں ترتیب دیا جا سکتا ہے:', 'د k درملنو لپاره د راټولو شویو k نمونو لیدل شوي معلومات، چې هره یوه یې د r اندازې وي داسې چې rk = n، د جدول په بڼه داسې ترتیبېدای شي:')
row = lambda i: [f'${i}$', f'$x_{{{i}1}}$', f'$x_{{{i}2}}$', '…', f'$x_{{{i}j}}$', '…', f'$x_{{{i}k}}$', '']
dots = ['⋮', '⋮', '', '…', '', '…', '', '']
body = [row(1), row(2), dots, row('i'), dots, row('r')]
SS = lambda c: f'$\\sum_{{i=1}}^{{r}}(\\overline{{x}}_{{i{c}}}-\\overline{{x}}_{{{c}}})^2$'
def tail(t, m, s, gt, gm, ts):
    return [[t, '$T_{.1}$', '$T_{.2}$', '…', '$T_{.j}$', '…', '$T_{.k}$', f'$T_{{..}}$ ({gt})'],
            [m, '$\\overline{x}_1$', '$\\overline{x}_2$', '…', '$\\overline{x}_j$', '…', '$\\overline{x}_k$', f'$\\overline{{x}}_{{..}}$ ({gm})'],
            [s, '$\\sum_{i=1}(\\overline{x}_{i1}-\\overline{x}_1)^2$', '$\\sum_{i=1}(\\overline{x}_{i2}-\\overline{x}_2)^2$', '…', '$\\sum_{i=1}(\\overline{x}_{ij}-\\overline{x}_j)^2$', '…', '$\\sum_{i=1}^{r}(x_{ik}-\\overline{x}_k)^2$', f'$\\sum_{{j=1}}^{{k}}\\sum_{{i=1}}^{{r}}(x_{{ij}}-\\overline{{x}}_{{..}})^2$ ({ts})']]
hd = lambda c, t: [c, '1', '2', '…', 'j', '…', 'k', t]
b.table('stat12-t-oneway-layout', hd('Observations \\ Treatments', 'Total'), body + tail('Total $T_j$', 'Means $\\overline{x}_{.j}$', 'Sum of squares', 'Grand total', 'Grand mean', 'Total sum of square'),
        hd('مشاہدات \\ علاج', 'میزان'), hd('مشاهدې \\ درملنې', 'ټول'),
        body + tail('میزان $T_j$', 'اوسط $\\overline{x}_{.j}$', 'مربعوں کا مجموعہ', 'کل میزان', 'کل اوسط', 'مربعوں کا کل مجموعہ'),
        body + tail('ټول $T_j$', 'منځني $\\overline{x}_{.j}$', 'د مربعو مجموعه', 'لوی ټولټال', 'لوی منځنی', 'د مربعو ټوله مجموعه'))
lay = b.build('stat12-p154-oneway-layout', 'ANOVA assumptions (iii)–(iv); 9.3.2 one-way layout', 'تجزیۂ تغیر کے مفروضات (iii)–(iv)؛ 9.3.2 یک طرفہ خاکہ', 'د ANOVA فرضیې (iii)–(iv)؛ 9.3.2 یو اړخیزه نقشه', 154, [299])

c = Builder()
c.h('9.3.3 Components of the total sum of squares (equal sample size)', '9.3.3 مربعوں کے کل مجموعے کے اجزاء (برابر نمونہ سائز)', '9.3.3 د مربعو د ټولې مجموعې برخې (برابره نمونه اندازه)')
c.p('In one way analysis of variance the total variation present in the observed data may be due to two meaningful components i.e. (i) variation among treatments (samples) (ii) variation with in the samples, so the T.S.S is divided in to two components as:', 'یک طرفہ تجزیۂ تغیر میں مشاہدہ شدہ مواد میں موجود کل تغیر دو بامعنی اجزاء کی وجہ سے ہو سکتا ہے یعنی (i) علاج (نمونوں) کے درمیان تغیر (ii) نمونوں کے اندر تغیر، لہٰذا T.S.S کو دو اجزاء میں یوں تقسیم کیا جاتا ہے:', 'په یو اړخیز د واریانس تحلیل کې په لیدل شویو معلوماتو کې موجود ټول تغیر کېدای شي د دوو معنی‌دارو برخو له امله وي یعنې (i) د درملنو (نمونو) ترمنځ تغیر (ii) د نمونو دننه تغیر، نو T.S.S په دوو برخو داسې وېشل کېږي:')
c.mlines([r'\text{T.S.S}=\sum_{j=1}^{k}\sum_{i=1}^{r}(x_{ij}-\overline{x}_{..})^2', r'=\text{within SS}+\text{Treatment SS}'])
c.p('To obtain unbiased estimates for $\\sigma^2$ divide both sides by respective degrees of freedom to have', '$\\sigma^2$ کے غیر جانبدار تخمینے حاصل کرنے کے لیے دونوں اطراف کو متعلقہ درجاتِ آزادی سے تقسیم کریں تاکہ', 'د $\\sigma^2$ د بې‌پلوه اټکلونو د ترلاسه کولو لپاره دواړه خواوې په اړوندو د ازادۍ درجو ووېشئ ترڅو')
c.mlines([r'S_T^2=S_e^2+S_{Tr}^2', r'\text{Or MST}=\text{MSE}+\text{MSTr}'])
c.p('The F-Test is defined as $F=\\frac{\\text{MSTr}}{\\text{MSE}}$ with ($\\nu_1=k-1$ and $\\nu_2=n-k$) df. which is used for testing $H_0:\\mu_1=\\mu_2=\\ldots=\\mu_k$ verses', 'F-جانچ کی تعریف $F=\\frac{\\text{MSTr}}{\\text{MSE}}$ ہے جس کے ($\\nu_1=k-1$ اور $\\nu_2=n-k$) درجاتِ آزادی ہیں، جو $H_0:\\mu_1=\\mu_2=\\ldots=\\mu_k$ کی جانچ کے لیے استعمال ہوتی ہے بمقابلہ', 'F-ازموینه داسې تعریفېږي $F=\\frac{\\text{MSTr}}{\\text{MSE}}$ د ($\\nu_1=k-1$ او $\\nu_2=n-k$) د ازادۍ درجو سره، چې د $H_0:\\mu_1=\\mu_2=\\ldots=\\mu_k$ د ازموینې لپاره کارول کېږي پر وړاندې د')
c.p('$H_1$: Not all means are equal.', '$H_1$: تمام اوسط برابر نہیں۔', '$H_1$: ټول منځني برابر نه دي.')
c.p('$H_0$ is rejected when, $F_c\\ge F_{\\alpha,(\\nu_1,\\nu_2)}$, whereas $F_{\\alpha,(\\nu_1,\\nu_2)}$ is obtained from the percentage points of the F-distribution, Table 9.1.', '$H_0$ رد کیا جاتا ہے جب $F_c\\ge F_{\\alpha,(\\nu_1,\\nu_2)}$، جبکہ $F_{\\alpha,(\\nu_1,\\nu_2)}$ کو F-تقسیم کے فیصدی نقاط، جدول 9.1 سے حاصل کیا جاتا ہے۔', '$H_0$ ردېږي کله چې $F_c\\ge F_{\\alpha,(\\nu_1,\\nu_2)}$، په داسې حال کې چې $F_{\\alpha,(\\nu_1,\\nu_2)}$ د F-وېش له سلنه‌ییزو ټکو، 9.1 جدول څخه ترلاسه کېږي.')
c.h('9.3.4 Components of the total degrees of freedom', '9.3.4 کل درجاتِ آزادی کے اجزاء', '9.3.4 د ازادۍ د ټولو درجو برخې')
c.p('When the total sum of squares is partitioned into component parts then the total degrees of freedom can also be partitioned into component parts accordingly as below:', 'جب مربعوں کے کل مجموعے کو اجزاء میں تقسیم کیا جائے تو کل درجاتِ آزادی کو بھی اسی کے مطابق اجزاء میں یوں تقسیم کیا جا سکتا ہے:', 'کله چې د مربعو ټوله مجموعه په برخو ووېشل شي، نو د ازادۍ ټولې درجې هم ورسره سم په برخو داسې وېشل کېدای شي:')
c.mlines([r'(n-1)=(n-k)+(k-1)', r'\text{Total df}=\text{within df}+\text{between df}'])
comp = c.build('stat12-p154-ss-df-components', '9.3.3 Components of total SS and the F-test; 9.3.4 degrees of freedom', '9.3.3 مربعوں کے کل مجموعے کے اجزاء اور F-جانچ؛ 9.3.4 درجاتِ آزادی', '9.3.3 د مربعو د ټولې مجموعې برخې او F-ازموینه؛ 9.3.4 د ازادۍ درجې', 154, [300])
issues = [{'id': 'stat12-p299-300-anova', 'unit': 9, 'printedPage': 300, 'description': 'p300 prints “MST = MSE + MSTr” (mean squares are not additive; sums of squares and df are), “verses” (versus) and “with in”; p299 layout prints the sum-of-squares row with x̄ᵢⱼ in some columns. Printed text retained.'}]

if __name__ == '__main__':
    save(154, [(9, lay), (9, comp)], issues=issues)
