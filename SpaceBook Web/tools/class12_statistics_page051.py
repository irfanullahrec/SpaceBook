"""PDF51 printed 93–94: Example 3.16 end, 3.3.4 binomial frequency distribution, Example 3.17 (expected frequencies table)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
h = r'\left(\frac{1}{2}\right)'
b = Builder()
b.mlines([r'q=\frac{8.64}{38}=0.23', r'\therefore p=1-q=1-0.23=0.77'])
b.p('Put in equation (i), the value of p, to have', 'مساوات (i) میں p کی قیمت رکھنے سے', 'په (i) معادله کې د p قیمت ایښودو سره')
b.mlines([r'n(0.77)=38', r'n=\frac{38}{0.77}=49.351\cong 50'])
b.p('Hence the required parameters are $[n=49,\\ p=0.77]$', 'لہٰذا مطلوبہ پیرامیٹر یہ ہیں $[n=49,\\ p=0.77]$', 'نو اړین پارامټرونه دا دي $[n=49,\\ p=0.77]$')
b.h('3.3.4 Binomial frequency distribution', '3.3.4 دو رقمی تعددی تقسیم', '3.3.4 بینومیل فریکونسي وېش')
b.p('If the Binomial probability distribution is multiplied by N, the number of Binomial experiments, i.e. $Np(x)=N\\left[{}^{n}_{x}C\\,p^xq^{n-x}\\right]$, the resulting distribution is known as Binomial frequency distribution. It is used to find the expected frequency ($E_f$) of X successes in N Binomial experiments.',
    'اگر دو رقمی احتمالی تقسیم کو دو رقمی تجربات کی تعداد N سے ضرب دیا جائے یعنی $Np(x)=N\\left[{}^{n}_{x}C\\,p^xq^{n-x}\\right]$، تو حاصل ہونے والی تقسیم دو رقمی تعددی تقسیم کہلاتی ہے۔ اسے N دو رقمی تجربات میں X کامیابیوں کا متوقع تعدد ($E_f$) معلوم کرنے کے لیے استعمال کیا جاتا ہے۔',
    'که بینومیل احتمالي وېش د بینومیل تجربو په شمېر N کې ضرب شي یعنې $Np(x)=N\\left[{}^{n}_{x}C\\,p^xq^{n-x}\\right]$، نو پایله لرونکی وېش بینومیل فریکونسي وېش بلل کېږي. په N بینومیل تجربو کې د X بریاوو د تمه شوې فریکونسۍ ($E_f$) د پیدا کولو لپاره کارول کېږي.')
b.h('Example 3.17', 'مثال 3.17', 'بېلګه 3.17')
b.p('Suppose five fair dice are rolled 96 times. Find the expected frequencies when the number 4, 5 or 6 is regarded as success.', 'فرض کریں پانچ منصفانہ پانسے 96 بار پھینکے جاتے ہیں۔ جب عدد 4، 5 یا 6 کو کامیابی سمجھا جائے تو متوقع تعدد معلوم کریں۔', 'فرض کړئ پنځه عادلانه ډایسونه 96 ځله اچول کېږي. کله چې عدد 4، 5 یا 6 بریا وګڼل شي، تمه شوې فریکونسۍ پیدا کړئ.')
b.h(*SOL)
b.p('We have $N=96$, $n=5$, X: number of dice showing 4, 5 or 6.', 'ہمارے پاس $N=96$، $n=5$، X: 4، 5 یا 6 دکھانے والے پانسوں کی تعداد۔', 'موږ لرو $N=96$، $n=5$، X: د هغو ډایسونو شمېر چې 4، 5 یا 6 ښيي.')
b.eq(r'X=0,1,2,3,4,5')
b.p('$p=P$[resulting 4,5 or 6 on a single die] $=\\frac{3}{6}=\\frac{1}{2}$, $q=\\frac{1}{2}$', '$p=P$[ایک پانسے پر 4، 5 یا 6 آنا] $=\\frac{3}{6}=\\frac{1}{2}$، $q=\\frac{1}{2}$', '$p=P$[په یوه ډایس د 4، 5 یا 6 راتلل] $=\\frac{3}{6}=\\frac{1}{2}$، $q=\\frac{1}{2}$')
b.eq(r'p(x)={}^{5}_{x}C' + h + '^x' + h + r'^{5-x},\ x=0,1,2,3,4,5')
b.p('Now expected frequencies are computed as follows:', 'اب متوقع تعدد یوں معلوم کیے جاتے ہیں:', 'اوس تمه شوې فریکونسۍ داسې محاسبه کېږي:')
rows = []
for k, num, ef in [(0, 1, '$96\\left(\\frac{1}{32}\\right)=03$'), (1, 5, '$96\\left(\\frac{5}{32}\\right)=15$'), (2, 10, '$=30$'), (3, 10, '$=30$'), (4, 5, '$=15$'), (5, 1, '$=03$')]:
    rows.append([str(k), f'${{}}^{{5}}_{{{k}}}C{h}^{{{k}}}{h}^{{5-{k}}}=\\frac{{{num}}}{{32}}$', ef])
rows.append(['Total', '1', '96'])
b.grid('stat12-t-ex3-17', ['$X$', '$p(x)={}^{5}_{x}C' + h + '^x' + h + '^{5-x}$', '$E_f=N\\,p(x)$'], rows)
rec = b.build('stat12-p051-binomial-frequency', 'Example 3.16 end; 3.3.4 binomial frequency distribution — Example 3.17', 'مثال 3.16 کا اختتام؛ 3.3.4 دو رقمی تعددی تقسیم — مثال 3.17', 'د بېلګې 3.16 پای؛ 3.3.4 بینومیل فریکونسي وېش — بېلګه 3.17', 51, [93, 94])
issues = [{'id': 'stat12-p93-n49-50', 'unit': 3, 'printedPage': 93, 'description': 'Example 3.16 rounds n = 49.351 ≅ 50 but states the parameters as n = 49; both printed values retained.'}]

if __name__ == '__main__':
    save(51, [(3, rec)], issues=issues)
