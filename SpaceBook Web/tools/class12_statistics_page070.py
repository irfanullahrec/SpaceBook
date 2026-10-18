"""PDF70 printed 131–132: Example 4.7 solutions (i)–(iii); Example 4.8 part (i), each with paired X/Z curves."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import paired_curves

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()


def part(bid, svg, lines):
    b.vpara(bid, svg, *(lines[0],) * 3)
    b.mlines(lines[1:])


part('stat12-ex4-7-i', paired_curves(0.8, None, ((0, '40'), (0.8, '44')), ((0, '0'), (0.8, '0.8')), zaxis='X'),
     [r'(i)\ P[X\ge 44]', r'=P\left[\frac{X-\mu}{\sigma}\ge\frac{44-\mu}{\sigma}\right]', r'=P\left[Z\ge\frac{44-40}{5}\right]', r'=P\left[Z\ge\frac{4}{5}\right]', r'=P[Z\ge 0.8]',
      r'=P[0<Z<\infty]-P[0<Z<0.80]', r'=0.5-0.2881=0.2119'])
part('stat12-ex4-7-ii', paired_curves(None, -3, ((-3, '25'), (0, '40')), ((-3, '-3'), (0, '0')), zaxis='X'),
     [r'(ii)\ P(X\le 25)', r'=P\left[\frac{X-\mu}{\sigma}\le\frac{25-\mu}{\sigma}\right]', r'=P\left[Z\le\frac{25-40}{5}\right]', r'=P\left[Z\le\frac{-15}{5}\right]', r'=P[Z<-3]',
      r'=[-\infty<Z<0]-P[-3<Z<0]', r'=0.5-0.4987=0.0013'])
part('stat12-ex4-7-iii', paired_curves(-1.6, 2, ((-1.6, '32'), (0, '40'), (2, '50')), ((-1.6, '-1.6'), (0, '0'), (2, '2'))),
     [r'(iii)\ P(32\le X\le 50)', r'=P\left[\frac{32-\mu}{\sigma}<\frac{X-\mu}{\sigma}<\frac{50-\mu}{\sigma}\right]', r'=P\left[\frac{32-40}{5}<Z<\frac{50-40}{5}\right]', r'=P\left[\frac{-8}{5}<Z<\frac{10}{5}\right]',
      r'=P[-1.6<Z<2]', r'=P[-1.6<Z<0]+P(0<Z<2)', r'=0.4452+0.4772=0.9224'])
ex7 = b.build('stat12-p070-example-4-7', 'Example 4.7 — probabilities for N(40, 5²)', 'مثال 4.7 — N(40, 5²) کے احتمالات', 'بېلګه 4.7 — د N(40, 5²) احتمالونه', 70, [131, 132])

b = Builder()
b.h('Example 4.8', 'مثال 4.8', 'بېلګه 4.8')
b.p('Suppose the ages at time of onset of a certain disease are approximately normally distributed with a mean of 11 years and standard deviation of 3 years. A child has just come down with disease. What is the probability that the child is i) between the ages of 8 and 14 years? ii) over 10 years of age? iii) under 12 years?',
    'فرض کریں ایک خاص بیماری کے آغاز کے وقت عمریں تقریباً نارمل تقسیم شدہ ہیں جن کا اوسط 11 سال اور معیاری انحراف 3 سال ہے۔ ایک بچہ ابھی اس بیماری میں مبتلا ہوا ہے۔ احتمال کیا ہے کہ بچہ i) 8 اور 14 سال کی عمر کے درمیان ہو؟ ii) 10 سال سے زیادہ عمر کا ہو؟ iii) 12 سال سے کم ہو؟',
    'فرض کړئ د یوې ټاکلې ناروغۍ د پیل پر مهال عمرونه نږدې نورمال وېش لري چې منځنی یې 11 کاله او معیاري انحراف یې 3 کاله دی. یو ماشوم همدا اوس په ناروغۍ اخته شوی. احتمال یې څومره دی چې ماشوم i) د 8 او 14 کلونو ترمنځ وي؟ ii) له 10 کلونو زیات عمر ولري؟ iii) له 12 کلونو کم وي؟')
b.h(*SOL)
b.p('Given $\\mu=11$ years, $\\sigma=3$ years', 'دیا گیا ہے $\\mu=11$ سال، $\\sigma=3$ سال', 'ورکړل شوي $\\mu=11$ کاله، $\\sigma=3$ کاله')
b.vpara('stat12-ex4-8-i', paired_curves(-1, 1, ((-1, '8'), (0, '11'), (1, '14')), ((-1, '-1'), (0, '0'), (1, '1'))), *(r'i) $P[8<X<14]$',) * 3)
b.mlines([r'=P\left[\frac{8-\mu}{\sigma}<\frac{X-\mu}{\sigma}<\frac{14-\mu}{\sigma}\right]', r'=P\left[\frac{8-11}{3}<Z<\frac{14-11}{3}\right]', r'=P\left[\frac{-3}{3}<Z<\frac{3}{3}\right]',
          r'=P[-1<Z<1]', r'=P[-1<Z<0]+P[0<Z<1]', r'=0.3413+0.3413=0.6826'])
ex8 = b.build('stat12-p070-example-4-8', 'Example 4.8 — onset age of a disease (part i)', 'مثال 4.8 — بیماری کے آغاز کی عمر (حصہ i)', 'بېلګه 4.8 — د ناروغۍ د پیل عمر (برخه i)', 70, [132])
issues = [{'id': 'stat12-p131-ex47-ii', 'unit': 4, 'printedPage': 131, 'description': 'Example 4.7(ii) prints “=[−∞<Z<0] − P[−3<Z<0]” (the leading P is missing), and part (iii) is asked with strict inequalities but solved with ≤; printed forms retained.'}]

if __name__ == '__main__':
    save(70, [(4, ex7), (4, ex8)], issues=issues)
