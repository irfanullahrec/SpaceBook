"""PDF58 printed 107–108: Example 3.22 distribution table, mean/variance and verification."""
from class12_statistics_common import Builder, save

b = Builder()
P = lambda k: f'$\\dfrac{{\\binom{{4}}{{{k}}}\\binom{{7}}{{5-{k}}}}}{{\\binom{{11}}{{5}}}}'
rows = []
for k, pk, xp, x2p in [(0, 21, '0', '0'), (1, 140, '140', '140'), (2, 210, '420', '840'), (3, 84, '252', '756'), (4, 7, '28', '112')]:
    rows.append([str(k), P(k) + f'=\\frac{{{pk}}}{{462}}$', '0' if xp == '0' else f'$\\frac{{{xp}}}{{462}}$', '0' if x2p == '0' else f'$\\frac{{{x2p}}}{{462}}$'])
rows.append(['Total', '1', '$\\frac{840}{462}$', '$\\frac{1848}{462}$'])
b.grid('stat12-t-ex3-22', ['$X$', '$p(x)=\\dfrac{\\binom{4}{x}\\binom{7}{5-x}}{\\binom{11}{5}}$', '$X\\,p(x)$', '$X^2p(x)$'], rows)
b.mlines([r'\text{Mean}=E(X)=\sum_{x=0}^{4}x\,p(x)=\frac{840}{462}=1.8182', r'\text{Variance}=V(X)=E(X^2)-[E(X)]^2', r'=\sum_{x=0}^{4}x^2p(x)-(1.8182)^2',
          r'=\frac{1848}{462}-(1.8182)^2=4-3.3059=0.694'])
b.p('• Verification', '• تصدیق', '• تایید')
b.p('Mean of hypergeometric distribution $=E(X)=\\frac{nk}{N}=\\frac{5(4)}{11}=\\frac{20}{11}=1.8182$', 'ہائپر جیومیٹرک تقسیم کا اوسط $=E(X)=\\frac{nk}{N}=\\frac{5(4)}{11}=\\frac{20}{11}=1.8182$', 'د هایپرجیومټریک وېش منځنی $=E(X)=\\frac{nk}{N}=\\frac{5(4)}{11}=\\frac{20}{11}=1.8182$')
b.p('Variance of hypergeometric distribution $V(X)=\\frac{nk}{N}\\;\\frac{N-k}{N}\\;\\frac{N-n}{N-1}$', 'ہائپر جیومیٹرک تقسیم کا تغیر $V(X)=\\frac{nk}{N}\\;\\frac{N-k}{N}\\;\\frac{N-n}{N-1}$', 'د هایپرجیومټریک وېش واریانس $V(X)=\\frac{nk}{N}\\;\\frac{N-k}{N}\\;\\frac{N-n}{N-1}$')
b.mlines([r'=1.8182\frac{(11-4)}{11}\left(\frac{11-5}{11-1}\right)', r'=0.694'])
rec = b.build('stat12-p058-example-3-22-table', 'Example 3.22 — distribution table, mean, variance and verification', 'مثال 3.22 — تقسیم کا جدول، اوسط، تغیر اور تصدیق', 'بېلګه 3.22 — د وېش جدول، منځنی، واریانس او تایید', 58, [107, 108])

if __name__ == '__main__':
    save(58, [(3, rec)])
