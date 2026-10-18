"""PDF107 printed 205–206: relative efficiency of mean vs median; Example 6.7 (unbiasedness and variances of θ̂1, θ̂2)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
T1, T2 = r'\hat{\theta}_1', r'\hat{\theta}_2'
b = Builder()
b.p('If $R.E=1\\Rightarrow$ both estimators are equally efficient.', 'اگر $R.E=1\\Rightarrow$ دونوں تخمین کار یکساں مؤثر ہیں۔', 'که $R.E=1\\Rightarrow$ دواړه اټکلوونکي یو شان موثر دي.')
b.p('For example, in case of normal distribution both sample mean and sample median are unbiased estimators for μ. However $Var(\\overline{X})=\\frac{\\sigma^2}{n}$ and $Var(\\text{median})=\\frac{\\pi\\sigma^2}{2n}$. Now comparing these estimators by relative efficiency criteria as:',
    'مثلاً نارمل تقسیم کی صورت میں نمونے کا اوسط اور نمونے کا وسطانیہ دونوں μ کے غیر جانبدار تخمین کار ہیں۔ تاہم $Var(\\overline{X})=\\frac{\\sigma^2}{n}$ اور $Var(\\text{median})=\\frac{\\pi\\sigma^2}{2n}$۔ اب نسبتی کارکردگی کے معیار سے ان تخمین کاروں کا موازنہ یوں کرتے ہیں:',
    'د بېلګې په توګه د نورمال وېش په حالت کې د نمونې منځنی او د نمونې منځنۍ (median) دواړه د μ بې‌پلوه اټکلوونکي دي. خو $Var(\\overline{X})=\\frac{\\sigma^2}{n}$ او $Var(\\text{median})=\\frac{\\pi\\sigma^2}{2n}$. اوس دا اټکلوونکي د نسبي موثریت د معیار له مخې داسې پرتله کوو:')
b.mlines([r'R.E=\frac{Var(\overline{X})}{Var(\text{median})}=\frac{\sigma^2/n}{\pi\sigma^2/2n}=\frac{\sigma^2}{n}\cdot\frac{2n}{\pi\sigma^2}=\frac{2}{\pi}', r'=\frac{2}{22/7}=\frac{14}{22}=0.64<1'])
b.p('This implies that $\\overline{X}$ is more efficient than median for μ. Thus, an unbiased estimator which has minimum variance is called the best or the most efficient estimator.', 'اس کا مطلب ہے کہ μ کے لیے $\\overline{X}$ وسطانیہ سے زیادہ مؤثر ہے۔ لہٰذا وہ غیر جانبدار تخمین کار جس کا تغیر کم سے کم ہو، بہترین یا سب سے مؤثر تخمین کار کہلاتا ہے۔', 'دا ښيي چې د μ لپاره $\\overline{X}$ تر منځنۍ موثر دی. نو هغه بې‌پلوه اټکلوونکی چې لږ تر لږه واریانس ولري، غوره یا تر ټولو موثر اټکلوونکی بلل کېږي.')
b.h('Example 6.7', 'مثال 6.7', 'بېلګه 6.7')
b.p(f'A random sample $X_1,X_2,X_3$ is drawn from a normal population having mean μ and variance $\\sigma^2$. Let ${T1}=\\frac{{X_1+2X_2+X_3}}{{4}}$ and ${T2}=\\frac{{X_1+X_2+X_3}}{{3}}$ are the estimators for μ.', f'μ اوسط اور $\\sigma^2$ تغیر والی نارمل آبادی سے ایک تصادفی نمونہ $X_1,X_2,X_3$ لیا جاتا ہے۔ فرض کریں ${T1}=\\frac{{X_1+2X_2+X_3}}{{4}}$ اور ${T2}=\\frac{{X_1+X_2+X_3}}{{3}}$، μ کے تخمین کار ہیں۔', f'له μ منځني او $\\sigma^2$ واریانس لرونکي نورمال نفوس څخه یوه تصادفي نمونه $X_1,X_2,X_3$ اخیستل کېږي. فرض کړئ ${T1}=\\frac{{X_1+2X_2+X_3}}{{4}}$ او ${T2}=\\frac{{X_1+X_2+X_3}}{{3}}$ د μ اټکلوونکي دي.')
b.group('lines', [
    ('i) Which of the estimators is unbiased?', 'i) کون سا تخمین کار غیر جانبدار ہے؟', 'i) کوم اټکلوونکی بې‌پلوه دی؟'),
    (f'ii) Show that ${T1}$ is efficient estimator for μ than ${T2}$.', f'ii) ثابت کریں کہ μ کے لیے ${T1}$، ${T2}$ سے زیادہ مؤثر تخمین کار ہے۔', f'ii) وښایاست چې د μ لپاره ${T1}$ تر ${T2}$ موثر اټکلوونکی دی.'),
])
b.h(*SOL)
b.p('i) To check unbiasedness, we first consider:', 'i) غیر جانبداری جانچنے کے لیے ہم پہلے لیتے ہیں:', 'i) د بې‌پلوي د ازمویلو لپاره لومړی په پام کې نیسو:')
b.eq(rf'{T1}=\frac{{X_1+2X_2+X_3}}{{4}}')
b.p('Take expectation on both sides', 'دونوں طرف توقع لیں', 'دواړو خواوو ته تمه واخلئ')
b.mlines([rf'E({T1})=\frac{{1}}{{4}}E[X_1+2X_2+X_3]', r'=\frac{1}{4}[E(X_1)+2E(X_2)+E(X_3)]'])
b.p('$=\\frac{1}{4}[\\mu+2\\mu+\\mu]$, As all $X_i$’s have same mean μ', '$=\\frac{1}{4}[\\mu+2\\mu+\\mu]$، کیونکہ تمام $X_i$ کا اوسط μ ہے', '$=\\frac{1}{4}[\\mu+2\\mu+\\mu]$، ځکه چې ټول $X_i$ یو شان منځنی μ لري')
b.p(f'$=\\frac{{4\\mu}}{{4}}=\\mu$ Hence ${T1}$ is unbiased estimator of μ.', f'$=\\frac{{4\\mu}}{{4}}=\\mu$ لہٰذا ${T1}$، μ کا غیر جانبدار تخمین کار ہے۔', f'$=\\frac{{4\\mu}}{{4}}=\\mu$ نو ${T1}$ د μ بې‌پلوه اټکلوونکی دی.')
b.p('Now consider the second estimator:', 'اب دوسرے تخمین کار کو لیں:', 'اوس دویم اټکلوونکی په پام کې ونیسئ:')
b.mlines([rf'{T2}=\frac{{X_1+X_2+X_3}}{{3}}.', rf'E({T2})=\frac{{1}}{{3}}[E(X_1)+E(X_2)+E(X_3)]', r'=\frac{1}{3}[\mu+\mu+\mu]'])
b.p(f'$=\\frac{{3\\mu}}{{3}}=\\mu$ Thus, ${T2}$ is also an unbiased estimator of μ.', f'$=\\frac{{3\\mu}}{{3}}=\\mu$ لہٰذا ${T2}$ بھی μ کا غیر جانبدار تخمین کار ہے۔', f'$=\\frac{{3\\mu}}{{3}}=\\mu$ نو ${T2}$ هم د μ بې‌پلوه اټکلوونکی دی.')
b.p('(ii) To check the efficiency, we have first compute variances for both estimators.', '(ii) کارکردگی جانچنے کے لیے ہمیں پہلے دونوں تخمین کاروں کے تغیر معلوم کرنے ہیں۔', '(ii) د موثریت د ازمویلو لپاره باید لومړی د دواړو اټکلوونکو واریانسونه محاسبه کړو.')
b.mlines([rf'Var({T1})=Var\left[\frac{{X_1+2X_2+X_3}}{{4}}\right]', r'=\frac{1}{16}[Var(X_1)+4Var(X_2)+Var(X_3)]'])
b.p('$=\\frac{1}{16}[\\sigma^2+4\\sigma^2+\\sigma^2]$, As $X_i$’s are drawn from the population having variance $\\sigma^2$.', '$=\\frac{1}{16}[\\sigma^2+4\\sigma^2+\\sigma^2]$، کیونکہ $X_i$ ایسی آبادی سے نکالے گئے ہیں جس کا تغیر $\\sigma^2$ ہے۔', '$=\\frac{1}{16}[\\sigma^2+4\\sigma^2+\\sigma^2]$، ځکه چې $X_i$ له داسې نفوس څخه راایستل شوي چې واریانس یې $\\sigma^2$ دی.')
b.eq(r'=\frac{6\sigma^2}{16}=\frac{3\sigma^2}{8}.')
b.p(f'Similarly $Var({T2})=Var\\left[\\frac{{X_1+X_2+X_3}}{{3}}\\right]$', f'اسی طرح $Var({T2})=Var\\left[\\frac{{X_1+X_2+X_3}}{{3}}\\right]$', f'همداراز $Var({T2})=Var\\left[\\frac{{X_1+X_2+X_3}}{{3}}\\right]$')
rec = b.build('stat12-p107-efficiency-example-6-7', 'Relative efficiency of mean vs median — Example 6.7', 'اوسط بمقابلہ وسطانیہ کی نسبتی کارکردگی — مثال 6.7', 'د منځني او منځنۍ نسبي موثریت — بېلګه 6.7', 107, [205, 206])

if __name__ == '__main__':
    save(107, [(6, rec)])
