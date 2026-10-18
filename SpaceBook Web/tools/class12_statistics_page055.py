"""PDF55 printed 101–102: Example 3.21 (recitation judges), 3.4.3 properties — mean derivation."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import population_box

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h('Example 3.21', 'مثال 3.21', 'بېلګه 3.21')
b.p('In an international recitation competition of the Holy Quran, a panel of 11 judges is formed to judge the best recitation. Two recitations $R_A$ and $R_B$ were considered to be the best where the opinion of judges got divided. Six judges were in favour of $R_A$ whereas five in favour of $R_B$. A random sample of five judges was drawn from the panel. Find the probability that out of five judges three are in favour of recitation $R_A$.',
    'قرآن پاک کی تلاوت کے ایک بین الاقوامی مقابلے میں بہترین تلاوت کا فیصلہ کرنے کے لیے 11 ججوں کا پینل بنایا گیا۔ دو تلاوتیں $R_A$ اور $R_B$ بہترین سمجھی گئیں جہاں ججوں کی رائے تقسیم ہو گئی۔ چھ جج $R_A$ کے حق میں تھے جبکہ پانچ $R_B$ کے حق میں۔ پینل سے پانچ ججوں کا تصادفی نمونہ لیا گیا۔ احتمال معلوم کریں کہ پانچ ججوں میں سے تین تلاوت $R_A$ کے حق میں ہوں۔',
    'د قرآن کریم د تلاوت په یوې نړیوالې سیالۍ کې د غوره تلاوت د ټاکلو لپاره د 11 قاضیانو یوه هیئت جوړ شو. دوه تلاوتونه $R_A$ او $R_B$ غوره وګڼل شول چې پکې د قاضیانو نظر ووېشل شو. شپږ قاضیان د $R_A$ په ګټه او پنځه د $R_B$ په ګټه وو. له هیئت څخه د پنځو قاضیانو تصادفي نمونه واخیستل شوه. احتمال یې پیدا کړئ چې له پنځو قاضیانو درې د $R_A$ تلاوت په ګټه وي.')
b.h(*SOL)
b.p('In the given problem', 'دیے گئے سوال میں', 'په ورکړل شوې پوښتنه کې')
b.visual('stat12-ex3-21-box', population_box(('6R', 'A'), ('5R', 'B'), True, '11'), ratio=.4)
b.p('$n=5$, $X=0,1,2,3,4,5$ $\\{\\because X=0,1,2,\\ldots\\min(n,k)\\}$', '$n=5$، $X=0,1,2,3,4,5$ $\\{\\because X=0,1,2,\\ldots\\min(n,k)\\}$', '$n=5$، $X=0,1,2,3,4,5$ $\\{\\because X=0,1,2,\\ldots\\min(n,k)\\}$')
b.eq(r'p(x)=\left\{\begin{matrix}\dfrac{\binom{6}{x}\binom{11-6}{5-x}}{\binom{N}{n}}, & x=0,1,2,3,4,5\\ 0 & \textit{otherwise}\end{matrix}\right.')
b.p('Now', 'اب', 'اوس')
b.eq(r'P(X=3)=\dfrac{\binom{6}{3}\binom{5}{5-3}}{\binom{11}{5}}=\frac{200}{231}')
b.h('3.4.3 Properties of hypergeometric probability distribution', '3.4.3 ہائپر جیومیٹرک احتمالی تقسیم کی خصوصیات', '3.4.3 د هایپرجیومټریک احتمالي وېش ځانګړنې')
b.p('◆ Mean of hypergeometric probability distribution by definition is given by', '◆ تعریف کے مطابق ہائپر جیومیٹرک احتمالی تقسیم کا اوسط یہ ہے', '◆ د تعریف له مخې د هایپرجیومټریک احتمالي وېش منځنی دا دی')
NK = r'{\binom{N}{n}}'
b.mlines([r'\text{Mean}=E(X)=\sum_x x\,p(x)=\sum_{x=0}^{n}x\dfrac{\binom{k}{x}\binom{N-k}{n-k}}' + NK,
          r'=0\dfrac{\binom{k}{0}\binom{N-k}{n-0}}' + NK + r'+\sum_{x=1}^{n}x\dfrac{\binom{k}{x}\binom{N-k}{n-k}}' + NK,
          r'=\dfrac{1}' + NK + r'\sum_{x=1}^{n}x\frac{k!}{(k-x)!\,x!}\binom{N-k}{n-x}',
          r'=\dfrac{1}' + NK + r'\sum_{x=1}^{n}x\frac{k(k-1)!}{(k-x)!\,x(x-1)!}\binom{N-k}{n-x}',
          r'=\dfrac{k}' + NK + r'\sum_{x=1}^{n}\frac{(k-1)!}{(k-x)!\,(x-1)!}\binom{N-k}{n-x}=\dfrac{k}' + NK + r'\sum_{x=1}^{n}\binom{k-1}{x-1}\binom{N-k}{n-x}'])
b.mlines([r'\text{Let } y=x-1\Rightarrow x=y+1', r'\text{If } x=1,\ y=0', r'\text{If } x=n,\ y=n-1',
          r'\therefore E(X)=\dfrac{k}' + NK + r'\sum_{y=0}^{n-1}\binom{k-1}{y}\binom{N-k}{n-y-1}'])
b.p('Apply the hypergeometric identity $\\sum_{r=0}^{k}\\binom{m}{r}\\binom{n}{k-r}=\\binom{m+n}{k}$', 'ہائپر جیومیٹرک شناخت $\\sum_{r=0}^{k}\\binom{m}{r}\\binom{n}{k-r}=\\binom{m+n}{k}$ کا اطلاق کریں', 'د هایپرجیومټریک پېژندنه $\\sum_{r=0}^{k}\\binom{m}{r}\\binom{n}{k-r}=\\binom{m+n}{k}$ وکاروئ')
rec = b.build('stat12-p055-hypergeometric-mean', 'Example 3.21 and 3.4.3 hypergeometric mean', 'مثال 3.21 اور 3.4.3 ہائپر جیومیٹرک اوسط', 'بېلګه 3.21 او 3.4.3 د هایپرجیومټریک منځنی', 55, [101, 102])
issues = [{'id': 'stat12-p101-200-231', 'unit': 3, 'printedPage': 101, 'description': 'Example 3.21 prints P(X=3) = 200/231; the computed value is C(6,3)C(5,2)/C(11,5) = 200/462 = 100/231. Printed value retained.'},
          {'id': 'stat12-p102-mean-index', 'unit': 3, 'printedPage': 102, 'description': 'The first two lines of the mean derivation print the second binomial as C(N−k, n−k) instead of C(N−k, n−x); printed form retained.'}]

if __name__ == '__main__':
    save(55, [(3, rec)], issues=issues)
