"""PDF56 printed 103–104: hypergeometric mean nK/N; variance derivation — E(X^2) via x(x−1)+x and identity."""
from class12_statistics_common import Builder, save

NK = r'{\binom{N}{n}}'
b = Builder()
b.mlines([r'E(X)=\dfrac{k}' + NK + r'\binom{N-1}{n-1}',
          r'=\dfrac{K}{\dfrac{N!}{(N-n)!\,n!}}\;\frac{(N-1)!}{(N-n)!\,(n-1)!}=\frac{K\,n(n-1)!\,(N-1)!}{N(N-1)!\,(n-1)!}', r'=n\frac{K}{N}'])
b.p('◆ Variance of hypergeometric probability distribution', '◆ ہائپر جیومیٹرک احتمالی تقسیم کا تغیر', '◆ د هایپرجیومټریک احتمالي وېش واریانس')
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'\text{Variance}=V(X)=E(X^2)-[E(X)]^2\qquad(A)', r'\text{As } E(X)=\frac{nK}{N}\ldots\ldots\ldots(1)', r'\text{Now } E(X^2)=\sum_x x^2\,p(x)',
          r'=\sum_{x=0}^{n}x^2\dfrac{\binom{k}{x}\binom{N-k}{n-x}}' + NK + r'=(0)^2\dfrac{\binom{k}{0}\binom{N-k}{n-0}}' + NK + r'+\sum_{x=1}^{n}x^2\dfrac{\binom{k}{x}\binom{N-k}{N-x}}' + NK])
b.p('$=\\sum_{x=1}^{n}[x(x-1)+x]\\binom{k}{x}\\binom{N-k}{n-x}\\qquad\\because x^2=x(x-1)+x$', '$=\\sum_{x=1}^{n}[x(x-1)+x]\\binom{k}{x}\\binom{N-k}{n-x}\\qquad\\because x^2=x(x-1)+x$', '$=\\sum_{x=1}^{n}[x(x-1)+x]\\binom{k}{x}\\binom{N-k}{n-x}\\qquad\\because x^2=x(x-1)+x$')
b.mlines([r'=\sum_{x=1}^{n}x(x-1)\dfrac{\binom{k}{x}\binom{N-k}{n-x}}' + NK + r'+\sum_{x=1}^{n}x\dfrac{\binom{k}{x}\binom{N-k}{n-x}}{\binom{N}{x}}=\left[1(1-1)\dfrac{\binom{k}{1}\binom{N-k}{n-0}}' + NK + r'\right]+\sum_{x=2}^{n}x(x-1)\dfrac{\binom{k}{x}\binom{N-k}{n-x}}' + NK + r'+\frac{nk}{N}',
          r'E(X^2)=\left[\dfrac{1}' + NK + r'\sum_{x=2}^{n}x(x-1)\frac{k!}{(k-x)!\,x!}\binom{N-k}{n-x}\right]+\left(\frac{nk}{N}\right)',
          r'=\dfrac{1}{\binom{N}{x}}\sum_{x=2}^{n}x(x-1)\frac{k(k-1)(k-2)!}{(k-x)!\,x(x-1)(x-2)!}\binom{N-k}{n-x}+\frac{nk}{N}',
          r'=\dfrac{k(k-1)}' + NK + r'\sum_{x=2}^{n}\frac{(k-2)!}{(k-x)!\,(x-2)!}\binom{N-k}{n-x}+\frac{nk}{N}',
          r'=\dfrac{k(k-1)}' + NK + r'\sum_{x=2}^{n}\binom{k-2}{x-2}\binom{N-k}{n-x}+\frac{nk}{N}'])
b.mlines([r'\text{Let}\quad y=x-2,\qquad x=y+2', r'\text{If}\quad x=2,\qquad y=0'])
b.p('If $x=n$, $y=n-2$, therefore,', 'اگر $x=n$، $y=n-2$، لہٰذا', 'که $x=n$، $y=n-2$، نو')
b.eq(r'E(X^2)=\dfrac{k(k-1)}' + NK + r'\sum_{y=0}^{n-2}\binom{k-2}{y}\binom{N-k}{n-y-2}+\frac{nk}{N}')
b.p('Using the hypergeometric identity $\\sum_{r=0}^{k}\\binom{m}{r}\\binom{n}{k-r}=\\binom{m+n}{k}$', 'ہائپر جیومیٹرک شناخت $\\sum_{r=0}^{k}\\binom{m}{r}\\binom{n}{k-r}=\\binom{m+n}{k}$ استعمال کرتے ہوئے', 'د هایپرجیومټریک پېژندنې $\\sum_{r=0}^{k}\\binom{m}{r}\\binom{n}{k-r}=\\binom{m+n}{k}$ په کارولو سره')
b.mlines([r'E(X^2)=\dfrac{k(k-1)}' + NK + r'\binom{N-2}{n-2}+\frac{nk}{N}', r'=\dfrac{k(k-1)}{\dfrac{N!}{(N-n)!\,n!}}\;\frac{(N-2)!}{(N-n)!\,(n-2)!}+\frac{nk}{N}'])
rec = b.build('stat12-p056-hypergeometric-variance', 'Hypergeometric mean (nK/N) and variance derivation', 'ہائپر جیومیٹرک اوسط (nK/N) اور تغیر کا اخذ', 'د هایپرجیومټریک منځنی (nK/N) او د واریانس استخراج', 56, [103, 104])
issues = [{'id': 'stat12-p103-104-binom-misprints', 'unit': 3, 'printedPage': 103, 'description': 'The E(X²) derivation prints several binomial misprints (C(N−k, N−x), C(N, x) in denominators, C(N−k, n−0) with k choose 1); printed forms retained.'}]

if __name__ == '__main__':
    save(56, [(3, rec)], issues=issues)
