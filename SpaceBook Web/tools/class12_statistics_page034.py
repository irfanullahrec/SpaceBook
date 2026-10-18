"""PDF34 printed 59–60: proof of E(X+Y)=E(X)+E(Y) completed; property (ii) E(XY)=E(X)E(Y) with proof; Example 2.18 tables."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
PROOF = ('Proof:', 'ثبوت:', 'ثبوت:')
b = Builder()
b.mlines([r'=\sum_{i=1}^{m}x_i\,[p(x_i,y_1)+p(x_i,y_2)+\ldots+p(x_i,y_n)]'])
b.p('$=\\sum_{i=1}^{m}x_i\\,[p(x_i)\\,p(y_1)+p(x_i)\\,p(y_2)+\\ldots+p(x_i)\\,p(y_n)]$ (as X and Y are independent)',
    '$=\\sum_{i=1}^{m}x_i\\,[p(x_i)\\,p(y_1)+p(x_i)\\,p(y_2)+\\ldots+p(x_i)\\,p(y_n)]$ (کیونکہ X اور Y آزاد ہیں)',
    '$=\\sum_{i=1}^{m}x_i\\,[p(x_i)\\,p(y_1)+p(x_i)\\,p(y_2)+\\ldots+p(x_i)\\,p(y_n)]$ (ځکه چې X او Y خپلواک دي)')
b.mlines([r'=\sum_{i=1}^{m}x_i\,p(x_i)\,[p(y_1)+p(y_2)+\ldots+p(y_n)]'])
b.p('$=\\sum_{i=1}^{m}x_i\\,p(x_i)\\,(1)$ (as sum of probabilities is equal to one.)', '$=\\sum_{i=1}^{m}x_i\\,p(x_i)\\,(1)$ (کیونکہ احتمالات کا مجموعہ ایک کے برابر ہے۔)', '$=\\sum_{i=1}^{m}x_i\\,p(x_i)\\,(1)$ (ځکه چې د احتمالونو مجموعه له یو سره برابره ده.)')
b.mlines([r'=\sum_{i=1}^{m}x_i\,p(x_i)', r'=E(X)\qquad(2)'])
b.p('Again consider $\\sum_{i=1}^{m}\\sum_{j=1}^{n}y_j\\,p(x_i,y_j)$', 'دوبارہ غور کریں $\\sum_{i=1}^{m}\\sum_{j=1}^{n}y_j\\,p(x_i,y_j)$', 'بیا په پام کې ونیسئ $\\sum_{i=1}^{m}\\sum_{j=1}^{n}y_j\\,p(x_i,y_j)$')
b.mlines([r'=\sum_{i=1}^{n}y_j\sum_{j=1}^{m}p(x_i,y_j)', r'=\sum_{j=1}^{n}y_j\,[p(x_1,y_j)+p(x_2,y_j)+\ldots+p(x_m,y_j)]', r'=\sum_{j=1}^{n}y_j\,[p(x_1)\,p(y_j)+p(x_2)\,p(y_j)+\ldots+p(x_m)\,p(y_j)]',
          r'=\sum_{j=1}^{n}y_j\,p(y_j)\,[p(x_1)+p(x_2)+\ldots+p(x_m)]', r'=\sum_{j=1}^{n}y_j\,p(y_j)\,(1)', r'=\sum_{j=1}^{n}y_j\,p(y_j)', r'=E(Y)\qquad(3)'])
b.p('Put equation (2) and (3) in equation (1), we get $E(X+Y)=E(X)+E(Y)$', 'مساوات (2) اور (3) کو مساوات (1) میں رکھنے سے $E(X+Y)=E(X)+E(Y)$', 'د (2) او (3) معادلې په (1) معادله کې ایښودو سره $E(X+Y)=E(X)+E(Y)$')
b.p('(ii) The expected value of the product of two independent random variables is equal to the product of their individual expected values i.e. $E(XY)=E(X)\\,E(Y)$',
    '(ii) دو آزاد تصادفی متغیرات کے حاصلِ ضرب کی متوقع قیمت ان کی انفرادی متوقع قیمتوں کے حاصلِ ضرب کے برابر ہے یعنی $E(XY)=E(X)\\,E(Y)$',
    '(ii) د دوو خپلواکو تصادفي متغیرونو د ضرب حاصل تمه شوی قیمت د هغو د جلا جلا تمه شویو قیمتونو له ضرب حاصل سره برابر دی یعنې $E(XY)=E(X)\\,E(Y)$')
b.h(*PROOF)
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.eq(r'E(XY)=\sum_{i=1}^{m}\sum_{j=1}^{n}(x_iy_j)\,p(x_i,y_j)')
b.p('$=\\sum_{i=1}^{m}\\sum_{j=1}^{n}x_iy_j\\,p(x_i)\\,p(y_j)$ (as X and Y are independent)', '$=\\sum_{i=1}^{m}\\sum_{j=1}^{n}x_iy_j\\,p(x_i)\\,p(y_j)$ (کیونکہ X اور Y آزاد ہیں)', '$=\\sum_{i=1}^{m}\\sum_{j=1}^{n}x_iy_j\\,p(x_i)\\,p(y_j)$ (ځکه چې X او Y خپلواک دي)')
b.mlines([r'=\sum_{i=1}^{m}x_i\,p(x_i)\sum_{j=1}^{n}y_j\,p(y_j)', r'=E(X)\,E(Y)'])
b.h('Example 2.18', 'مثال 2.18', 'بېلګه 2.18')
b.p('Let X and Y are two discrete random variables with the following joint probability distribution:', 'فرض کریں X اور Y دو منفصل تصادفی متغیرات ہیں جن کی مشترکہ احتمالی تقسیم یہ ہے:', 'فرض کړئ X او Y دوه منفصل تصادفي متغیرونه دي چې دا ګډ احتمالي وېش لري:')
b.grid('stat12-t-ex2-18', ['$X\\backslash Y$', '1', '3', '5'], [['2', '0.10', '0.20', '0.10'], ['4', '0.15', '0.30', '0.15']])
b.p('Compute; E(X), E(Y), E(X+Y), E(2X−3Y) and E(XY).', 'معلوم کریں؛ E(X)، E(Y)، E(X+Y)، E(2X−3Y) اور E(XY)۔', 'محاسبه کړئ؛ E(X)، E(Y)، E(X+Y)، E(2X−3Y) او E(XY).')
b.h(*SOL)
b.p('Adding rows and columns to find p(x) and p(y) shown in the following table.', 'p(x) اور p(y) معلوم کرنے کے لیے قطاروں اور کالموں کو جمع کیا گیا ہے جیسا کہ درج ذیل جدول میں دکھایا گیا ہے۔', 'د p(x) او p(y) د پیدا کولو لپاره کتارونه او ستونونه جمع شوي لکه څنګه چې په لاندې جدول کې ښودل شوي.')
b.grid('stat12-t-ex2-18-marg', ['$X\\backslash Y$', '1', '3', '5', '$p(x)$'],
       [['2', '0.10', '0.20', '0.10', '0.40'], ['4', '0.15', '0.30', '0.15', '0.60'], ['$p(y)$', '0.25', '0.50', '0.25', '1']])
rec = b.build('stat12-p034-expectation-two-proofs', 'Proofs of E(X+Y) and E(XY); Example 2.18', 'E(X+Y) اور E(XY) کے ثبوت؛ مثال 2.18', 'د E(X+Y) او E(XY) ثبوتونه؛ بېلګه 2.18', 34, [59, 60])
issues = [{'id': 'stat12-p59-proof-index-typos', 'unit': 2, 'printedPage': 59, 'description': 'In the second half of the E(X+Y) proof the printed sums swap the limits (Σ_{i=1}^{n} y_j Σ_{j=1}^{m}) and print “p x2, yj)”, “(p x2)” with misplaced parentheses; the summation limits are kept as printed, the parentheses are normalised.'}]

if __name__ == '__main__':
    save(34, [(2, rec)], issues=issues)
