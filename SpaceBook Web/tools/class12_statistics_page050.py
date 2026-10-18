"""PDF50 printed 91–92: Example 3.14 table and results, Example 3.15 (mean 5, S.D 4 impossible), Example 3.16 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
T = lambda a: f'\\left(\\frac{{1}}{{3}}\\right)^{{{a}}}\\left(\\frac{{2}}{{3}}\\right)^{{4-{a}}}'
b = Builder()
rows = []
for k, pk, xp, x2p in [(0, 16, '0', '0'), (1, 32, '\\frac{32}{81}', '\\frac{32}{81}'), (2, 24, '\\frac{48}{81}', '\\frac{96}{81}'), (3, 8, '\\frac{24}{81}', '\\frac{72}{81}'), (4, 1, '\\frac{4}{81}', '\\frac{16}{81}')]:
    rows.append([str(k), f'${{}}^{{4}}_{{{k}}}C{T(k)}=\\frac{{{pk}}}{{81}}$', f'${xp}$', f'${x2p}$'])
rows.append(['Total', '1', '$\\frac{108}{81}$', '$\\frac{216}{81}$'])
b.grid('stat12-t-ex3-14', ['$X$', '$p(x)={}^{4}_{x}C\\left(\\frac{1}{3}\\right)^x\\left(\\frac{2}{3}\\right)^{4-x}$', '$X\\,p(x)$', '$X^2p(x)$'], rows)
b.mlines([r'(ii)\quad\text{Mean}=E(X)=\Sigma x\,p(x)=\frac{108}{81}=1.333', r'\text{Variance}=E(X^2)-[E(X)]^2', r'=\Sigma x^2p(x)-(1.333)^2',
          r'=\frac{216}{81}-1.778=2.667-1.778=0.889', r'S.D(X)=\sqrt{0.887}=0.943'])
b.p('(iii) Mean and variance by properties:', '(iii) خصوصیات کے ذریعے اوسط اور تغیر:', '(iii) د ځانګړنو له لارې منځنی او واریانس:')
b.p('Mean of Binomial distribution $=np=4\\times\\frac{1}{3}=1.333$', 'دو رقمی تقسیم کا اوسط $=np=4\\times\\frac{1}{3}=1.333$', 'د بینومیل وېش منځنی $=np=4\\times\\frac{1}{3}=1.333$')
b.p('Variance of Binomial distribution $=npq=4\\times\\frac{1}{3}\\times\\frac{2}{3}=0.889$', 'دو رقمی تقسیم کا تغیر $=npq=4\\times\\frac{1}{3}\\times\\frac{2}{3}=0.889$', 'د بینومیل وېش واریانس $=npq=4\\times\\frac{1}{3}\\times\\frac{2}{3}=0.889$')
b.eq(r'S.D(X)=0.943')
b.p('Note that both by calculation and properties, we have the same results.', 'نوٹ کریں کہ حساب اور خصوصیات دونوں سے ہمیں یکساں نتائج ملتے ہیں۔', 'پام وکړئ چې د محاسبې او ځانګړنو دواړو له لارې یو شان پایلې لرو.')
ex14 = b.build('stat12-p050-example-3-14', 'Example 3.14 — distribution, mean and variance', 'مثال 3.14 — تقسیم، اوسط اور تغیر', 'بېلګه 3.14 — وېش، منځنی او واریانس', 50, [91])

c = Builder()
c.h('Example 3.15', 'مثال 3.15', 'بېلګه 3.15')
c.p('Is it possible to have a Binomial distribution with mean = 5 and S.D = 4?', 'کیا ایسی دو رقمی تقسیم ممکن ہے جس کا اوسط = 5 اور معیاری انحراف = 4 ہو؟', 'آیا داسې بینومیل وېش شونی دی چې منځنی = 5 او معیاري انحراف = 4 ولري؟')
c.h(*SOL)
c.p('Given that $np=5$', 'دیا گیا ہے $np=5$', 'ورکړل شوي $np=5$')
c.p('Squaring both sides', 'دونوں طرف مربع لینے سے', 'دواړه خواوې مربع کولو سره')
c.mlines([r'\sqrt{npq}=4', r'\text{Or}\quad npq=16', r'5q=16', r'q=\frac{16}{5}=3.2>1'])
c.p('p or q should not be greater than one because $p+q=1$', 'p یا q ایک سے بڑا نہیں ہونا چاہیے کیونکہ $p+q=1$', 'p یا q باید له یو څخه لوی نه وي ځکه چې $p+q=1$')
c.p('Hence it is not possible to have a Binomial distribution with mean 5 and S.D 4.', 'لہٰذا اوسط 5 اور معیاری انحراف 4 والی دو رقمی تقسیم ممکن نہیں۔', 'نو داسې بینومیل وېش چې منځنی یې 5 او معیاري انحراف یې 4 وي، شونی نه دی.')
c.h('Example 3.16', 'مثال 3.16', 'بېلګه 3.16')
c.p('A random variable X is binomially distributed with mean 38 and S.D 2.94. Find n and p.', 'ایک تصادفی متغیر X کی دو رقمی تقسیم ہے جس کا اوسط 38 اور معیاری انحراف 2.94 ہے۔ n اور p معلوم کریں۔', 'یو تصادفي متغیر X بینومیل وېش لري چې منځنی یې 38 او معیاري انحراف یې 2.94 دی. n او p پیدا کړئ.')
c.h(*SOL)
c.mlines([r'\text{Given}\quad np=38\qquad(i)', r'\sqrt{npq}=2.94', r'\text{Or}\quad npq=8.64\qquad(ii)'])
c.p('Putting value of np in equation (ii), we get', 'مساوات (ii) میں np کی قیمت رکھنے سے', 'په (ii) معادله کې د np قیمت ایښودو سره')
c.eq(r'38q=8.64')
ex15 = c.build('stat12-p050-examples-3-15-3-16', 'Examples 3.15–3.16 — parameters from mean and S.D', 'مثالیں 3.15–3.16 — اوسط اور معیاری انحراف سے پیرامیٹر', 'بېلګې 3.15–3.16 — له منځني او معیاري انحراف څخه پارامټرونه', 50, [92])
issues = [{'id': 'stat12-p91-sd-0887', 'unit': 3, 'printedPage': 91, 'description': 'Example 3.14(ii) computes variance 0.889 but then prints S.D(X) = √0.887 = 0.943; printed value retained.'},
          {'id': 'stat12-p92-squaring-order', 'unit': 3, 'printedPage': 92, 'description': 'Example 3.15 prints “Squaring both sides” before the √npq = 4 line it applies to; printed order retained.'}]

if __name__ == '__main__':
    save(50, [(3, ex14), (3, ex15)], issues=issues)
