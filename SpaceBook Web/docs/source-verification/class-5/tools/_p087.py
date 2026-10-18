from fractions import Fraction
from decimal import Decimal
out = ['@printed 81',
       '@deco Ant with "Challenge" sign beside "Try It!"; cartoon book mascot on "Exercise 7".',
       'p A factory produced 850 masks in a day. 72% masks are blue. Find the number of blue masks produced by the factory in a day. || ایک فیکٹری نے ایک دن میں 850 ماسک بنائے۔ 72% ماسک نیلے ہیں۔ فیکٹری کے ایک دن میں بنائے گئے نیلے ماسکوں کی تعداد معلوم کریں۔ || یوې فابریکې په یوه ورځ کې 850 ماسکونه جوړ کړل. 72% ماسکونه نیلي دي. د فابریکې په یوه ورځ کې د جوړ شویو نیلي ماسکونو شمېر معلوم کړئ.',
       'p Total number of masks = 850 || ماسکوں کی کل تعداد = 850 || د ماسکونو ټول شمېر = 850',
       r'p Number of blue masks = 72% of 850 $= \dfrac{72}{100} \times 850 = 612$ || نیلے ماسکوں کی تعداد = 850 کا 72% $= \dfrac{72}{100} \times 850 = 612$ || د نیلي ماسکونو شمېر = د 850 72% $= \dfrac{72}{100} \times 850 = 612$',
       'p The factory produces 612 blue masks in a day. || فیکٹری ایک دن میں 612 نیلے ماسک بناتی ہے۔ || فابریکه په یوه ورځ کې 612 نیلي ماسکونه جوړوي.',
       'box check | Try Yourself || خود کوشش کریں || پخپله هڅه وکړئ',
       'p What i 62% of 62? || 62 کا 62% کیا ہے؟ || د 62 62% څو دی؟',
       'p What is 5% of 50? || 50 کا 5% کیا ہے؟ || د 50 5% څو دی؟',
       'endbox',
       '@issue Try Yourself prints "What i 62% of 62?" (for "What is"); kept as printed.',
       'box check | Try It! Challenge || کوشش کریں! چیلنج || هڅه وکړئ! ننګونه',
       'p 20% of an amount is 350 rupees. Find: || کسی رقم کا 20% ، 350 روپے ہے۔ معلوم کریں: || د یوې اندازې پیسو 20% ، 350 روپۍ دي. معلوم کړئ:',
       'qp A | 1% of the amount. || رقم کا 1%۔ || د پیسو 1%.',
       'qp B | 100 % of the amount. || رقم کا 100%۔ || د پیسو 100%.',
       'qp C | 1,000 % of the amount. || رقم کا 1,000%۔ || د پیسو 1,000%.',
       'endbox',
       'exercise 7',
       'q 1 | Express the following in percentage. || درج ذیل کو فیصد میں ظاہر کریں۔ || لاندې په سلنه ښکاره کړئ.']
for l, n in zip('abcdefghij', [4, 35, 76, 12, 28, 47, 45, 66, 89, 1]):
    out.append(rf'qp {l} | $\dfrac{{{n}}}{{100}}$')
    out.append(f'sol {n}% ## A fraction with denominator 100 is read directly as a percentage: {n} out of 100 = {n}%. || 100 نسب نما والا کسر براہِ راست فیصد کے طور پر پڑھا جاتا ہے: 100 میں سے {n} = {n}%۔ || د 100 مخرج لرونکی کسر مستقیم د سلنې په توګه لوستل کېږي: له 100 څخه {n} = {n}%.')
out.append('q 2 | Convert the following percentages into fractions. || درج ذیل فیصد کو کسور میں تبدیل کریں۔ || لاندې سلنې په کسرونو واړوئ.')
for l, n in zip('abcdefghij', [13, 24, 46, 55, 68, 72, 87, 98, 11, 10]):
    f = Fraction(n, 100)
    simp = '' if f.denominator == 100 else rf' = \dfrac{{{f.numerator}}}{{{f.denominator}}}'
    out.append(f'qp {l} | {n}%')
    out.append(rf'sol $\dfrac{{{f.numerator}}}{{{f.denominator}}}$ ## Write over 100 and simplify: $\dfrac{{{n}}}{{100}}{simp}$. || 100 پر لکھیں اور مختصر کریں: $\dfrac{{{n}}}{{100}}{simp}$۔ || پر 100 یې ولیکئ او ساده یې کړئ: $\dfrac{{{n}}}{{100}}{simp}$.')
out.append('q 3 | Convert the following percentages into decimals. || درج ذیل فیصد کو اعشاریہ میں تبدیل کریں۔ || لاندې سلنې په اعشاریو واړوئ.')
for l, n in zip('abcdefghij', [15, 26, 47, 52, 63, 74, 85, 96, 17, 18]):
    out.append(f'qp {l} | {n}%')
    out.append(rf'sol 0.{n:02d} ## $\dfrac{{{n}}}{{100}} = 0.{n:02d}$ (move the point two places left). || $\dfrac{{{n}}}{{100}} = 0.{n:02d}$ (نقطہ دو مقام بائیں)۔ || $\dfrac{{{n}}}{{100}} = 0.{n:02d}$ (ټکی دوه ځایه کیڼ لوري ته).')
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p087.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
