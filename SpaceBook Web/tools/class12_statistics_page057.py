"""PDF57 printed 105–106: hypergeometric variance npq(N−n)/(N−1), S.D; Example 3.22 (bowl of balls) start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import population_box

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'=\frac{k(k-1)\,n(n-1)(n-2)!}{N(N-1)(N-2)!}\;\frac{(N-2)!}{(n-2)!}+\frac{nk}{N}', r'=\frac{n(n-1)k(k-1)}{N(N-1)}+\frac{nk}{N}\ldots\ldots\ldots(2)'])
b.p('Putting equation (1) or equation (2) in equation (A)', 'مساوات (1) یا (2) کو مساوات (A) میں رکھنے سے', 'د (1) یا (2) معادله په (A) معادله کې ایښودو سره')
b.mlines([r'V(X)=\frac{n(n-1)k(k-1)}{N(N-1)}+\frac{nk}{N}-\frac{n^2k^2}{N^2}', r'=\frac{nk}{N}\left[\frac{(n-1)(k-1)}{N-1}+1-\frac{nk}{N}\right]',
          r'V(X)=\frac{nk}{N}\left[\frac{N(n-1)(k-1)+N(N-1)-nk(N-1)}{N(N-1)}\right]', r'=\frac{nk}{N}\left[\frac{nNk-nN-Nk+N+N^2-N-nkN+nk}{N(N-1)}\right]',
          r'=\frac{nk}{N}\left[\frac{N^2-Nk+nk-nN}{N(N-1)}\right]', r'=\frac{nk}{N}\left[\frac{N(N-k)-n(N-k)}{N(N-1)}\right]', r'=\frac{nk}{N}\left[\frac{(N-k)(N-n)}{N(N-1)}\right]',
          r'=n\frac{k}{N}\;\frac{N-k}{N}\;\frac{N-n}{N-1}', r'=npq\frac{N-n}{N-1}\qquad\left(\because p=\frac{k}{N},\ q=1-p=1-\frac{k}{N}=\frac{N-k}{N}\right)'])
b.p('◆ Standard deviation of hypergeometric probability distribution is', '◆ ہائپر جیومیٹرک احتمالی تقسیم کا معیاری انحراف یہ ہے', '◆ د هایپرجیومټریک احتمالي وېش معیاري انحراف دا دی')
b.eq(r'S.D(X)=\sqrt{npq\frac{N-n}{N-1}}')
var = b.build('stat12-p057-hypergeometric-variance-end', 'Hypergeometric variance and standard deviation', 'ہائپر جیومیٹرک تغیر اور معیاری انحراف', 'د هایپرجیومټریک واریانس او معیاري انحراف', 57, [105])

c = Builder()
c.h('Example 3.22', 'مثال 3.22', 'بېلګه 3.22')
c.p('A bowl contains 4 green and 7 red balls. A sample of 5 balls is selected from the bowl without replacement. Find the probability distribution for the number of green balls. Compute the mean and variance of this probability distribution and compare them with the theoretical mean and variance.',
    'ایک پیالے میں 4 سبز اور 7 سرخ گیندیں ہیں۔ پیالے سے بغیر واپسی کے 5 گیندوں کا نمونہ منتخب کیا جاتا ہے۔ سبز گیندوں کی تعداد کی احتمالی تقسیم معلوم کریں۔ اس احتمالی تقسیم کا اوسط اور تغیر معلوم کریں اور ان کا نظری اوسط اور تغیر سے موازنہ کریں۔',
    'په یوه لوښي کې 4 شنه او 7 سره توپونه دي. له لوښي څخه بې له بېرته اچولو د 5 توپونو نمونه ټاکل کېږي. د شنو توپونو د شمېر احتمالي وېش پیدا کړئ. د دې احتمالي وېش منځنی او واریانس محاسبه کړئ او له نظري منځني او واریانس سره یې پرتله کړئ.')
c.h(*SOL)
c.p('The bowl contains', 'پیالے میں ہیں', 'لوښي کې دي')
balls = {'en': '11 balls', 'ur': '11 گیندیں', 'ps': '11 توپونه'}
c.visual('stat12-ex3-22-box', population_box(('4 G', ''), ('7 R', ''), True, balls['en']), population_box(('4 G', ''), ('7 R', ''), True, balls['ur']), population_box(('4 G', ''), ('7 R', ''), True, balls['ps']), ratio=.4)
c.p('Here $n=5$', 'یہاں $n=5$', 'دلته $n=5$')
c.p('X: number of green balls selected', 'X: منتخب سبز گیندوں کی تعداد', 'X: د ټاکل شویو شنو توپونو شمېر')
c.p('$X=0,1,2,3,4$. [5 is not possible as there are only 4 green balls.].', '$X=0,1,2,3,4$۔ [5 ممکن نہیں کیونکہ صرف 4 سبز گیندیں ہیں۔]۔', '$X=0,1,2,3,4$. [5 شونی نه دی ځکه چې یوازې 4 شنه توپونه دي.].')
c.eq(r'\therefore p(x)=\left\{\begin{matrix}\dfrac{\binom{4}{x}\binom{11-4}{5-x}}{\binom{11}{5}}, & x=0,1,2,3,4\\ 0 & \textit{otherwise}\end{matrix}\right.')
c.p('Now hypergeometric probability distribution of X is given as', 'اب X کی ہائپر جیومیٹرک احتمالی تقسیم یہ ہے', 'اوس د X هایپرجیومټریک احتمالي وېش داسې دی')
ex = c.build('stat12-p057-example-3-22', 'Example 3.22 — green and red balls', 'مثال 3.22 — سبز اور سرخ گیندیں', 'بېلګه 3.22 — شنه او سره توپونه', 57, [106])

if __name__ == '__main__':
    save(57, [(3, var), (3, ex)])
