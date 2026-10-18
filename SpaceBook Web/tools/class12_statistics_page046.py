"""PDF46 printed 83–84: Example 3.7 solution (binomial n=4 table), Example 3.8 (n=6, p=0.75), Example 3.9 question."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
h = r'\left(\frac{1}{2}\right)'
b = Builder()
b.h(*SOL)
b.p('Here $n=4$ (four Bernoulli trails)', 'یہاں $n=4$ (چار برنولی آزمائشیں)', 'دلته $n=4$ (څلور برنولي ازمېښتونه)')
b.p('X: the number of successes in four trials', 'X: چار آزمائشوں میں کامیابیوں کی تعداد', 'X: په څلورو ازمېښتونو کې د بریاوو شمېر')
b.eq(r'X=0,1,2,3,4')
b.p('$p=\\frac{1}{2}$ (probability of head on a single coin)', '$p=\\frac{1}{2}$ (ایک سکے پر چِت کا احتمال)', '$p=\\frac{1}{2}$ (په یوه سکه د سر احتمال)')
b.eq(r'q=1-p=1-\frac{1}{2}=\frac{1}{2}')
b.p('The Binomial probability function is:', 'دو رقمی احتمالی تفاعل یہ ہے:', 'بینومیل احتمالي تابع دا ده:')
b.eq(r'p(x)=\left\{\begin{matrix}{}^{4}_{x}C' + h + '^x' + h + r'^{4-x}, & x=0,1,2,3,4\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('The Binomial probability distribution is', 'دو رقمی احتمالی تقسیم یہ ہے', 'بینومیل احتمالي وېش دا دی')
rows = [[str(k), f'${{}}^{{4}}_{{{k}}}C{h}^{{{k}}}{h}^{{4-{k}}}=\\frac{{{c}}}{{16}}$'] for k, c in zip(range(5), (1, 4, 6, 4, 1))]
b.grid('stat12-t-ex3-7', ['$X$', f'$p(x)={{}}^{{4}}_{{x}}C{h}^x{h}^{{4-x}}$'], rows + [['Total', '1']])
ex7 = b.build('stat12-p046-example-3-7', 'Example 3.7 — binomial distribution of heads in four tosses', 'مثال 3.7 — چار بار اچھالنے میں چِت کی دو رقمی تقسیم', 'بېلګه 3.7 — په څلورو اچولو کې د سرونو بینومیل وېش', 46, [83])

c = Builder()
c.h('Example 3.8', 'مثال 3.8', 'بېلګه 3.8')
c.p('Suppose X has a Binomial distribution with n = 6 and p = 0.75. Find (i) $P(X=4)$ (ii) $P(X\\ge 5)$ and (iii) $P(X<4)$.', 'فرض کریں X کی دو رقمی تقسیم ہے جس میں n = 6 اور p = 0.75 ہے۔ معلوم کریں (i) $P(X=4)$ (ii) $P(X\\ge 5)$ اور (iii) $P(X<4)$۔', 'فرض کړئ X بینومیل وېش لري چې n = 6 او p = 0.75. پیدا کړئ (i) $P(X=4)$ (ii) $P(X\\ge 5)$ او (iii) $P(X<4)$.')
c.h(*SOL)
c.p('Here $n=6$', 'یہاں $n=6$', 'دلته $n=6$')
c.p('X: number of successes in 6 trials', 'X: 6 آزمائشوں میں کامیابیوں کی تعداد', 'X: په 6 ازمېښتونو کې د بریاوو شمېر')
c.mlines([r'X=0,1,2,3,4,5,6', r'p=0.75', r'q=1-p=-0.75=0.25'])
c.p('The Binomial probability function is', 'دو رقمی احتمالی تفاعل یہ ہے', 'بینومیل احتمالي تابع دا ده')
c.eq(r'p(x)=\left\{\begin{matrix}{}^{6}_{x}C(0.75)^x(0.25)^{6-x}, & x=0,1,2,3,4,5,6\\ 0, & \textit{otherwise}\end{matrix}\right.')
c.mlines([r'(i)\quad P(X=4)={}^{6}_{4}C(0.75)^4(0.25)^{6-4}=0.297',
          r'(ii)\quad P(X\ge 5)={}^{6}_{5}C(0.75)^5(0.25)^{6-5}+{}^{6}_{6}C(0.75)^6(0.25)^{6-6}=0.534',
          r'(iii)\quad P(X<4)={}^{6}_{0}C(0.75)^0(0.25)^{6-0}+{}^{6}_{1}C(0.75)^1(0.25)^{6-1}+{}^{6}_{2}C(0.75)^2(0.25)^{6-2}+',
          r'{}^{6}_{3}C(0.75)^3(0.25)^{6-3}=0.169'])
c.h('Example 3.9', 'مثال 3.9', 'بېلګه 3.9')
c.p('A certain drug treatment cures 90% of cases of hookworm in children. Suppose that 20 children suffering from hookworm are to be treated and that the children can be regarded as a sample from the population. Find the probability that (i) all 20 children will be cured (ii) exactly 18 will be cured (iii) at least one will be cured.',
    'ایک خاص دوا بچوں میں ہک ورم کے 90% کیسوں کو ٹھیک کر دیتی ہے۔ فرض کریں ہک ورم میں مبتلا 20 بچوں کا علاج کیا جانا ہے اور ان بچوں کو آبادی کا نمونہ سمجھا جا سکتا ہے۔ احتمال معلوم کریں کہ (i) تمام 20 بچے ٹھیک ہو جائیں گے (ii) ٹھیک 18 ٹھیک ہوں گے (iii) کم از کم ایک ٹھیک ہوگا۔',
    'یوه ټاکلې درملنه په ماشومانو کې د هوک‌ورم 90% پېښې روغوي. فرض کړئ چې د هوک‌ورم 20 ناروغه ماشومان باید درملنه شي او دا ماشومان د نفوس د نمونې په توګه ګڼل کېدای شي. احتمال یې پیدا کړئ چې (i) ټول 20 ماشومان به روغ شي (ii) دقیقاً 18 به روغ شي (iii) لږ تر لږه یو به روغ شي.')
ex8 = c.build('stat12-p046-examples-3-8-3-9', 'Examples 3.8–3.9 — binomial probabilities', 'مثالیں 3.8–3.9 — دو رقمی احتمالات', 'بېلګې 3.8–3.9 — بینومیل احتمالونه', 46, [84])
issues = [{'id': 'stat12-p84-q-minus', 'unit': 3, 'printedPage': 84, 'description': 'Example 3.8 prints “q = 1 − p = −0.75 = 0.25” (the 1 before −0.75 is missing); printed line retained.'}]

if __name__ == '__main__':
    save(46, [(3, ex7), (3, ex8)], issues=issues)
