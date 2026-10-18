"""PDF44 printed 79–80: 3.2 Bernoulli trial, 3.2.1 Bernoulli distribution and pmf, Example 3.5, 3.2.3 properties (mean, variance start)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
h = r'\left(\frac{1}{2}\right)'
b = Builder()
b.h('3.2 Bernoulli trail', '3.2 برنولی آزمائش', '3.2 د برنولي ازمېښت')
b.p('A random experiment which has two possible outcomes classified as success and failure is called a Bernoulli trial. For example, gender of a child (male or female), performance of a student in an examination (pass or fail), result of tossing a coin (head or tail) etc. The random variable is taking only two values i.e. “0” for failure and “1” for success. Further, probability of success is denoted by p and failure by q such that $p+q=1$.',
    'ایسا تصادفی تجربہ جس کے دو ممکنہ نتائج کامیابی اور ناکامی کے طور پر درجہ بند ہوں، برنولی آزمائش کہلاتا ہے۔ مثلاً بچے کی جنس (لڑکا یا لڑکی)، امتحان میں طالب علم کی کارکردگی (پاس یا فیل)، سکہ اچھالنے کا نتیجہ (چِت یا پَٹ) وغیرہ۔ تصادفی متغیر صرف دو قیمتیں لیتا ہے یعنی ناکامی کے لیے “0” اور کامیابی کے لیے “1”۔ مزید یہ کہ کامیابی کے احتمال کو p اور ناکامی کو q سے ظاہر کیا جاتا ہے کہ $p+q=1$۔',
    'هغه تصادفي تجربه چې دوه شونې پایلې ولري چې د بریا او ناکامۍ په توګه ډلبندي شوې وي، د برنولي ازمېښت بلل کېږي. د بېلګې په توګه د ماشوم جنس (هلک یا نجلۍ)، په ازموینه کې د زده کوونکي کړنه (بریالی یا ناکام)، د سکې د اچولو پایله (سر یا لکۍ) او نور. تصادفي متغیر یوازې دوه قیمتونه اخلي یعنې د ناکامۍ لپاره “0” او د بریا لپاره “1”. سربېره پر دې د بریا احتمال په p او د ناکامۍ په q ښودل کېږي داسې چې $p+q=1$.')
b.h('3.2.1 Bernoulli probability distribution', '3.2.1 برنولی احتمالی تقسیم', '3.2.1 د برنولي احتمالي وېش')
b.p('A probability distribution of the type:', 'اس قسم کی احتمالی تقسیم:', 'د دې ډول احتمالي وېش:')
b.dist('stat12-t-bernoulli', ['0', '1'], ['$q$', '$p$'], vertical=True)
b.p('is called Bernoulli probability distribution and the variable X which denotes the results of a Bernoulli trail is called Bernoulli random variable. This distribution was introduced by a Swiss mathematician Jacob Bernoulli (1654–1705). It is also known as point Binomial distribution because it has only two classes of events. Mathematically',
    'برنولی احتمالی تقسیم کہلاتی ہے اور متغیر X جو برنولی آزمائش کے نتائج ظاہر کرتا ہے، برنولی تصادفی متغیر کہلاتا ہے۔ یہ تقسیم سوئس ریاضی دان جیکب برنولی (1654–1705) نے متعارف کرائی۔ اسے نقطہ دو رقمی (point Binomial) تقسیم بھی کہتے ہیں کیونکہ اس میں واقعات کی صرف دو جماعتیں ہیں۔ ریاضیاتی طور پر',
    'د برنولي احتمالي وېش بلل کېږي او متغیر X چې د برنولي ازمېښت پایلې ښيي، د برنولي تصادفي متغیر بلل کېږي. دا وېش سویسي ریاضي پوه جیکب برنولي (1654–1705) معرفي کړ. د ټکي بینومیل (point Binomial) وېش په نوم هم یادېږي ځکه چې یوازې د پېښو دوه ټولګي لري. په ریاضي ډول')
b.eq(r'p(x)=\left\{\begin{matrix}p^xq^{1-x}, & x=0,1\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('is called Bernoulli probability mass function. This distribution has only one parameter i.e. p.', 'برنولی احتمالی کمیتی تفاعل کہلاتا ہے۔ اس تقسیم کا صرف ایک پیرامیٹر ہے یعنی p۔', 'د برنولي د احتمال کتلوي تابع بلل کېږي. دا وېش یوازې یو پارامټر لري یعنې p.')
b.h('Example 3.5', 'مثال 3.5', 'بېلګه 3.5')
b.p('A fair coin is tossed o ce. What is the probability that (i) no head occurs? (ii) one head occurs?', 'ایک منصفانہ سکہ ایک بار اچھالا جاتا ہے۔ احتمال کیا ہے کہ (i) کوئی چِت نہ آئے؟ (ii) ایک چِت آئے؟', 'یوه عادلانه سکه یو ځل اچول کېږي. احتمال یې څومره دی چې (i) هېڅ سر رانه شي؟ (ii) یو سر راشي؟')
b.h(*SOL)
b.p('Tossing a coin is Bernoulli experiment. Let us define a random variable as', 'سکہ اچھالنا برنولی تجربہ ہے۔ آئیے ایک تصادفی متغیر یوں متعین کریں', 'د سکې اچول د برنولي تجربه ده. راځئ یو تصادفي متغیر داسې وټاکو')
b.p('X: number of heads', 'X: چِت کی تعداد', 'X: د سرونو شمېر')
b.eq(r'=0,\ 1')
b.p('$p=$ probability of head $=\\frac{1}{2}$ (as coin is fair).', '$p=$ چِت کا احتمال $=\\frac{1}{2}$ (کیونکہ سکہ منصفانہ ہے)۔', '$p=$ د سر احتمال $=\\frac{1}{2}$ (ځکه چې سکه عادلانه ده).')
b.eq(r'q=1-p=1-\frac{1}{2}=\frac{1}{2}')
b.p('The Bernoulli probability function is given by', 'برنولی احتمالی تفاعل یہ ہے', 'د برنولي احتمالي تابع دا ده')
b.eq(r'p(x)=\left\{\begin{matrix}' + h + '^x' + h + r'^{1-x}, & x=0,1\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p(f'(i) probability of no head $=P(X=0)={h}^0{h}^{{1-0}}=(1){h}={h}$', f'(i) کوئی چِت نہ آنے کا احتمال $=P(X=0)={h}^0{h}^{{1-0}}=(1){h}={h}$', f'(i) د هېڅ سر نه راتلو احتمال $=P(X=0)={h}^0{h}^{{1-0}}=(1){h}={h}$')
b.p(f'(ii) Probability of one head $=P(X=1)={h}^1{h}^{{1-1}}={h}{h}^0={h}$', f'(ii) ایک چِت آنے کا احتمال $=P(X=1)={h}^1{h}^{{1-1}}={h}{h}^0={h}$', f'(ii) د یو سر د راتلو احتمال $=P(X=1)={h}^1{h}^{{1-1}}={h}{h}^0={h}$')
b.h('3.2.3 Properties of Bernoulli distribution', '3.2.3 برنولی تقسیم کی خصوصیات', '3.2.3 د برنولي وېش ځانګړنې')
b.p('◆ Mean of Bernoulli distribution', '◆ برنولی تقسیم کا اوسط', '◆ د برنولي وېش منځنی')
b.p('By definition mean $=E(X)=\\sum_x x\\,p(x)$', 'تعریف کے مطابق اوسط $=E(X)=\\sum_x x\\,p(x)$', 'د تعریف له مخې منځنی $=E(X)=\\sum_x x\\,p(x)$')
b.mlines([r'=\sum_{x=0}^{1}x\,p^x\,q^{1-x}', r'=0p^0q^{1-0}+1p^1q^{1-1}=0+p=p'])
b.p('◆ Variance of Bernoulli distribution', '◆ برنولی تقسیم کا تغیر', '◆ د برنولي وېش واریانس')
b.p('By definition variance $=E(X^2)-[E(X)]^2$', 'تعریف کے مطابق تغیر $=E(X^2)-[E(X)]^2$', 'د تعریف له مخې واریانس $=E(X^2)-[E(X)]^2$')
b.eq(r'=\sum_x x^2p(x)-(p)^2')
rec = b.build('stat12-p044-bernoulli', '3.2 Bernoulli distribution — Example 3.5 and properties', '3.2 برنولی تقسیم — مثال 3.5 اور خصوصیات', '3.2 د برنولي وېش — بېلګه 3.5 او ځانګړنې', 44, [79, 80])
issues = [{'id': 'stat12-p79-trail-once', 'unit': 3, 'printedPage': 79, 'description': 'Printed “Bernoulli trail” (section 3.2 heading and text) for “trial”, and “tossed o ce” (missing n) in Example 3.5; printed spellings retained. Section numbering jumps from 3.2.1 to 3.2.3 as printed.'}]

if __name__ == '__main__':
    save(44, [(3, rec)], issues=issues)
