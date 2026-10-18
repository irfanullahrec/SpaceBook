"""PDF71 printed 133–134: Example 4.8 parts (ii)–(iii); Example 4.9 (sucrose) parts (i)–(ii)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import paired_curves

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.vpara('stat12-ex4-8-ii', paired_curves(-0.33, None, ((-0.33, '10'), (0, '11')), ((-0.33, '−0.33'), (0, '0')), zaxis='X'), *(r'ii) $P[X>10]$',) * 3)
b.mlines([r'=P\left[\frac{X-\mu}{\sigma}>\frac{10-\mu}{\sigma}\right]', r'=P\left[Z>\frac{10-11}{3}\right]', r'=P\left[Z>\frac{-1}{3}\right]', r'=P[Z>-0.33]', r'=P[-0.33<Z<0]+P[0<Z<\infty]', r'=0.1293+0.5=0.6293'])
b.vpara('stat12-ex4-8-iii', paired_curves(None, 0.33, ((0, '11'), (0.33, '12')), ((0, '0'), (0.33, '0.33'))), *(r'iii) $P[X<12]$',) * 3)
b.mlines([r'=P\left[\frac{X-\mu}{\sigma}<\frac{12-\mu}{\sigma}\right]', r'=P\left[Z<\frac{12-11}{3}\right]', r'=P[Z<0.33]', r'=P[-\infty<Z<0]+P[0<Z<0.33]', r'=0.5+0.1293', r'=0.6293'])
ex8 = b.build('stat12-p071-example-4-8', 'Example 4.8 — parts (ii) and (iii)', 'مثال 4.8 — حصے (ii) اور (iii)', 'بېلګه 4.8 — برخې (ii) او (iii)', 71, [133])

c = Builder()
c.h('Example 4.9', 'مثال 4.9', 'بېلګه 4.9')
c.p('The sucrose concentration in a population is normally distributed with a mean = 65 mg and S.D = 25 mg.', 'کسی آبادی میں سکروز کا ارتکاز نارمل تقسیم شدہ ہے جس کا اوسط = 65 mg اور معیاری انحراف = 25 mg ہے۔', 'په یوه نفوس کې د سکروز غلظت نورمال وېش لري چې منځنی = 65 mg او معیاري انحراف = 25 mg دی.')
c.group('lines', [
    ('i. What proportion of the population is greater than sucrose concentration of 85 mg?', 'i. آبادی کا کتنا تناسب 85 mg سکروز ارتکاز سے زیادہ ہے؟', 'i. د نفوس څومره برخه له 85 mg د سکروز غلظت څخه زیاته ده؟'),
    ('ii. What proportion of the population is less than sucrose concentration of 45 mg?', 'ii. آبادی کا کتنا تناسب 45 mg سکروز ارتکاز سے کم ہے؟', 'ii. د نفوس څومره برخه له 45 mg د سکروز غلظت څخه کمه ده؟'),
    ('iii. What proportion of the population are lies between 45 and 85 mg?', 'iii. آبادی کا کتنا تناسب 45 اور 85 mg کے درمیان ہے؟', 'iii. د نفوس څومره برخه د 45 او 85 mg ترمنځ ده؟'),
])
c.h(*SOL)
c.mlines([r'\text{Given }\mu=65\text{ mg}', r'\sigma=25\text{ mg}'])
c.vpara('stat12-ex4-9-i', paired_curves(0.8, None, ((0, '65'), (0.8, '85')), ((0, '0'), (0.8, '0.8')), zaxis='X'), *(r'i) $P[X>85]$',) * 3)
c.mlines([r'=P\left[\frac{X-\mu}{\sigma}>\frac{85-\mu}{\sigma}\right]', r'=P\left[Z>\frac{85-65}{25}\right]', r'=P\left[Z>\frac{20}{25}\right]', r'=P[Z>0.80]', r'=P[0<Z<\infty]-P[0<Z<0.80]', r'=0.5-0.2881=0.2119=21.19\%'])
c.vpara('stat12-ex4-9-ii', paired_curves(None, -0.8, ((-0.8, '45'), (0, '65')), ((-0.8, '−0.8'), (0, '0')), zaxis='X'), *(r'ii) $P[X<45]$',) * 3)
c.mlines([r'=P\left[\frac{X-\mu}{\sigma}<\frac{45-\mu}{\sigma}\right]', r'=P\left[Z<\frac{45-65}{25}\right]', r'=P[Z<-0.8]', r'=P[-\infty<Z<0]-P[-0.80<Z<0]', r'=0.5-0.2881=0.2119=21.19\%'])
ex9 = c.build('stat12-p071-example-4-9', 'Example 4.9 — sucrose concentration (parts i–ii)', 'مثال 4.9 — سکروز کا ارتکاز (حصے i–ii)', 'بېلګه 4.9 — د سکروز غلظت (برخې i–ii)', 71, [133, 134])

if __name__ == '__main__':
    save(71, [(4, ex8), (4, ex9)])
