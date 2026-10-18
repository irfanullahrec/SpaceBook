"""PDF47 printed 85–86: Example 3.9 solution, Example 3.10 (type-A blood), Example 3.11 start (defective items)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('Here $n=20$', 'یہاں $n=20$', 'دلته $n=20$')
b.p('X: number of children to be cured', 'X: ٹھیک ہونے والے بچوں کی تعداد', 'X: د روغېدونکو ماشومانو شمېر')
b.mlines([r'X=0,1,2,3\ldots 20', r'p=0.90,\ q=0.1'])
b.eq(r'p(x)=\left\{\begin{matrix}{}^{20}_{x}C(0.90)^x(0.10)^{20-x}, & x=0,1,2,3,\ldots,20\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('(i) $P$(all 20 will be cured) $=P(X=20)={}^{20}_{20}C(0.90)^{20}(0.10)^{20-20}=0.12158$', '(i) $P$(تمام 20 ٹھیک ہوں) $=P(X=20)={}^{20}_{20}C(0.90)^{20}(0.10)^{20-20}=0.12158$', '(i) $P$(ټول 20 روغ شي) $=P(X=20)={}^{20}_{20}C(0.90)^{20}(0.10)^{20-20}=0.12158$')
b.p('(ii) $P$(exactly 18 will be cured) $=P(X=18)={}^{20}_{18}C(0.90)^{18}(0.10)^{20-18}=0.28518$', '(ii) $P$(ٹھیک 18 ٹھیک ہوں) $=P(X=18)={}^{20}_{18}C(0.90)^{18}(0.10)^{20-18}=0.28518$', '(ii) $P$(دقیقاً 18 روغ شي) $=P(X=18)={}^{20}_{18}C(0.90)^{18}(0.10)^{20-18}=0.28518$')
b.p('(iii) $P$(at least one will be cured) $=1-P$(no one will be cured)', '(iii) $P$(کم از کم ایک ٹھیک ہو) $=1-P$(کوئی ٹھیک نہ ہو)', '(iii) $P$(لږ تر لږه یو روغ شي) $=1-P$(هېڅوک روغ نه شي)')
b.mlines([r'=1-P(X=0)', r'=1-{}^{20}_{0}C(0.90)^0(0.10)^{20-0}'])
b.p('$=1-0$ (approximately)', '$=1-0$ (تقریباً)', '$=1-0$ (نږدې)')
b.eq(r'=1')
b.h('Example 3.10', 'مثال 3.10', 'بېلګه 3.10')
b.p('In Peshawar 42 % of the population has type-A blood. Consider, taking a sample of size 4. Let Y denotes the number of persons in the sample with type-A blood. Find (i) $P(Y=0)$ (ii) $P(Y=1)$ (iii) $P(0\\le Y\\le 2)$ and (iv) $P(0<Y\\le 2)$',
    'پشاور میں 42 % آبادی کا خون ٹائپ-A ہے۔ 4 کے سائز کا نمونہ لینے پر غور کریں۔ فرض کریں Y نمونے میں ٹائپ-A خون والے افراد کی تعداد ظاہر کرتا ہے۔ معلوم کریں (i) $P(Y=0)$ (ii) $P(Y=1)$ (iii) $P(0\\le Y\\le 2)$ اور (iv) $P(0<Y\\le 2)$',
    'په پېښور کې د نفوس 42 % د A ډول وینه لري. د 4 اندازې نمونه اخیستل په پام کې ونیسئ. فرض کړئ Y په نمونه کې د A ډول وینې لرونکو کسانو شمېر ښيي. پیدا کړئ (i) $P(Y=0)$ (ii) $P(Y=1)$ (iii) $P(0\\le Y\\le 2)$ او (iv) $P(0<Y\\le 2)$')
b.h(*SOL)
b.p('Given that $p=0.42$, $q=0.58$, $n=4$', 'دیا گیا ہے $p=0.42$، $q=0.58$، $n=4$', 'ورکړل شوي $p=0.42$، $q=0.58$، $n=4$')
b.p('Y: number of persons in the sample with type-A blood', 'Y: نمونے میں ٹائپ-A خون والے افراد کی تعداد', 'Y: په نمونه کې د A ډول وینې لرونکو کسانو شمېر')
b.mlines([r'Y=0,1,2,3,4', r'\therefore p(y)=\left\{\begin{matrix}{}^{4}_{y}C(0.42)^y(0.58)^{4-y}, & y=0,1,2,3,4\\ 0, & \textit{otherwise}\end{matrix}\right.',
          r'(i)\quad P(Y=0)={}^{4}_{0}C(0.42)^0(0.58)^{4-0}=0.11316', r'(ii)\quad P(Y=1)={}^{4}_{1}C(0.42)^1(0.58)^{4-1}=0.32779',
          r'(iii)\quad P(0\le Y\le 2)=P(Y=0)+P(Y=1)+P(Y=2)', r'=0.11316+0.32779+{}^{4}_{2}C(0.42)^2(0.58)^{4-2}', r'=0.44095+0.35609', r'=0.79700',
          r'(iv)\quad P(0<Y\le 2)=P(Y=1)+P(Y=2)', r'=0.32779+0.35605=0.68384'])
b.h('Example 3.11', 'مثال 3.11', 'بېلګه 3.11')
b.p('A machine produces 10 per cent defective items. Ten items are selected at random. Find the probability of not more than two items being defective.', 'ایک مشین 10 فیصد ناقص اشیاء بناتی ہے۔ دس اشیاء تصادفی طور پر منتخب کی جاتی ہیں۔ دو سے زیادہ اشیاء کے ناقص نہ ہونے کا احتمال معلوم کریں۔', 'یوه ماشین 10 سلنه عیبي توکي جوړوي. لس توکي په تصادفي ډول ټاکل کېږي. له دوو څخه د زیاتو توکو د عیبي نه کېدو احتمال پیدا کړئ.')
b.h(*SOL)
b.mlines([r'\text{We have } p=10\%=\frac{10}{100}=\frac{1}{10}', r'\therefore q=\frac{9}{10}', r'n=10'])
b.p('X: number of defective items', 'X: ناقص اشیاء کی تعداد', 'X: د عیبي توکو شمېر')
b.eq(r'X=0,1,2,3\ldots 10')
rec = b.build('stat12-p047-binomial-examples', 'Examples 3.9–3.11 — binomial applications', 'مثالیں 3.9–3.11 — دو رقمی اطلاقات', 'بېلګې 3.9–3.11 — بینومیل کارونې', 47, [85, 86])
issues = [{'id': 'stat12-p86-p2-value', 'unit': 3, 'printedPage': 86, 'description': 'Example 3.10 uses P(Y=2) = 0.35609 in (iii) but 0.35605 in (iv); both printed values retained.'}]

if __name__ == '__main__':
    save(47, [(3, rec)], issues=issues)
