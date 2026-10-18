"""PDF64 printed 119–120: continuous uniform variance (b−a)²/12, S.D; Examples 4.1–4.2; 4.2 Normal distribution introduction."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'V(X)=\frac{b^2+ab+a^2}{3}-\frac{(a+b)^2}{4}', r'=\frac{4(b^2+ab+a^2)-3(a^2+b^2+2ab)}{12}', r'=\frac{4b^2+4ab+4a^2-3a^2-3b^2-6ab}{12}', r'=\frac{b^2+a^2-2ab}{12}', r'V(X)=\frac{(b-a)^2}{12}'])
b.p('(iii) Standard deviation of continuous uniform probability distribution:', '(iii) مسلسل یکساں احتمالی تقسیم کا معیاری انحراف:', '(iii) د متصل یونیفارم احتمالي وېش معیاري انحراف:')
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.eq(r'S.D(X)=\sqrt{V(X)}=\sqrt{\frac{(b-a)^2}{12}}=\frac{b-a}{\sqrt{12}}')
b.h('Example 4.1', 'مثال 4.1', 'بېلګه 4.1')
b.p('If X has a uniform distribution over the interval (2, 4), find (i) $P(2\\le X\\le 3)$ (ii) $P(3\\le X\\le 4)$', 'اگر X کی وقفہ (2، 4) پر یکساں تقسیم ہو تو معلوم کریں (i) $P(2\\le X\\le 3)$ (ii) $P(3\\le X\\le 4)$', 'که X د (2، 4) په واټن کې یونیفارم وېش ولري، پیدا کړئ (i) $P(2\\le X\\le 3)$ (ii) $P(3\\le X\\le 4)$')
b.h(*SOL)
b.p('Given a = 2 and b = 4, so the pdf of uniform distribution in this case is given by', 'دیا گیا ہے a = 2 اور b = 4، لہٰذا اس صورت میں یکساں تقسیم کا pdf یہ ہے', 'ورکړل شوي a = 2 او b = 4، نو په دې حالت کې د یونیفارم وېش pdf دا ده')
b.eq(r'f(x)=\left\{\begin{matrix}\frac{1}{2}, & 2\le x\le 4\\ 0, & \textit{otherwise}\end{matrix}\right.')
b.p('Now', 'اب', 'اوس')
b.mlines([r'(i)\quad P(2\le X\le 3)=\int_2^3\frac{1}{2}dx=\frac{1}{2}\int_2^3dx', r'=\frac{1}{2}\left[\left.x\right|_2^3\right]=\frac{1}{2}(3-2)=\frac{1}{2}(1)=\frac{1}{2}',
          r'(ii)\quad P(3\le X\le 4)=\int_3^4\frac{1}{2}dx=\frac{1}{2}\int_3^4dx=\frac{1}{2}\left[\left.x\right|_3^4\right]', r'=\frac{1}{2}[4-3]=\frac{1}{2}(1)=\frac{1}{2}'])
b.h('Example 4.2', 'مثال 4.2', 'بېلګه 4.2')
b.p('Let $X\\sim U(-1,3)$. Find mean, variance and standard deviation for this continuous uniform random variable.', 'فرض کریں $X\\sim U(-1,3)$۔ اس مسلسل یکساں تصادفی متغیر کا اوسط، تغیر اور معیاری انحراف معلوم کریں۔', 'فرض کړئ $X\\sim U(-1,3)$. د دې متصل یونیفارم تصادفي متغیر منځنی، واریانس او معیاري انحراف پیدا کړئ.')
b.h(*SOL)
b.p('Here $a=-1$, $b=3$', 'یہاں $a=-1$، $b=3$', 'دلته $a=-1$، $b=3$')
b.p('Now', 'اب', 'اوس')
b.mlines([r'E(X)=\frac{a+b}{2}=\frac{-1+3}{2}=\frac{2}{2}=1', r'V(X)=\frac{(b-a)^2}{12}=\frac{[3-(-1)]^2}{12}=\frac{(3+1)^2}{12}=1.333', r'S.D(X)=\sqrt{1.333}=1.155'])
uni = b.build('stat12-p064-uniform-variance-examples', 'Continuous uniform variance and S.D — Examples 4.1–4.2', 'مسلسل یکساں تغیر اور معیاری انحراف — مثالیں 4.1–4.2', 'متصل یونیفارم واریانس او معیاري انحراف — بېلګې 4.1–4.2', 64, [119, 120])

c = Builder()
c.h('4.2 Normal distribution', '4.2 نارمل تقسیم', '4.2 نورمال وېش')
c.p('Normal distribution is the most common and useful amongst all known distribution. It is considered as the cornerstone of the modern statistical theory. The reason of importance is due to the facts that:',
    'نارمل تقسیم تمام معلوم تقسیموں میں سب سے عام اور مفید ہے۔ اسے جدید شماریاتی نظریے کا سنگِ بنیاد سمجھا جاتا ہے۔ اس کی اہمیت کی وجوہات یہ ہیں:',
    'نورمال وېش د ټولو پېژندل شویو وېشونو له منځه تر ټولو عام او ګټور دی. د عصري احصاییوي نظریې بنسټیزه ډبره ګڼل کېږي. د اهمیت لاملونه یې دا دي:')
c.group('lines', [
    ('i. Many natural phenomena like age, weight, light, I.Q, grade, temperature, income etc. tend to be approximately normal.', 'i. بہت سے فطری مظاہر جیسے عمر، وزن، روشنی، آئی کیو، گریڈ، درجۂ حرارت، آمدنی وغیرہ تقریباً نارمل ہوتے ہیں۔', 'i. ډېرې طبیعي پدیدې لکه عمر، وزن، رڼا، I.Q، درجه، تودوخه، عاید او نور نږدې نورمال وي.'),
    ('ii. Most of the discrete distributions such as Binomial, Poisson, etc. tend to Normal distribution as sample size increases i.e. $n\\to\\infty$.', 'ii. زیادہ تر منفصل تقسیمیں جیسے دو رقمی، پوآسوں وغیرہ نمونے کا سائز بڑھنے پر یعنی $n\\to\\infty$ نارمل تقسیم کی طرف مائل ہوتی ہیں۔', 'ii. ډېری منفصل وېشونه لکه بینومیل، پواسون او نور د نمونې د اندازې په زیاتېدو یعنې $n\\to\\infty$ سره نورمال وېش ته نږدې کېږي.'),
    ('iii. For a sample of size $n\\ge 30$, the distribution is considered as normal.', 'iii. $n\\ge 30$ سائز کے نمونے کے لیے تقسیم کو نارمل سمجھا جاتا ہے۔', 'iii. د $n\\ge 30$ اندازې نمونې لپاره وېش نورمال ګڼل کېږي.'),
    ('iv. Many variables which are not normally distributed can be normalized through suitable transformations.', 'iv. بہت سے متغیرات جو نارمل تقسیم شدہ نہیں، مناسب تبدیلیوں کے ذریعے نارمل بنائے جا سکتے ہیں۔', 'iv. ډېر متغیرونه چې نورمال وېش نه لري، د مناسبو بدلونونو له لارې نورمال کېدای شي.'),
])
nrm = c.build('stat12-p064-normal-intro', '4.2 Normal distribution — importance', '4.2 نارمل تقسیم — اہمیت', '4.2 نورمال وېش — اهمیت', 64, [120])

if __name__ == '__main__':
    save(64, [(4, uni), (4, nrm)])
