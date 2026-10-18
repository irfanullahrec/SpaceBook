"""PDF63 printed 117–118: 4.1 introduction, 4.1.1–4.1.2 continuous uniform distribution (graph), 4.1.3 mean and variance derivation start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import continuous_uniform

b = Builder()
b.h('4.1 Introduction to continuous probability distributions', '4.1 مسلسل احتمالی تقسیموں کا تعارف', '4.1 د متصلو احتمالي وېشونو پېژندنه')
b.p('As you know that it is difficult to locate a specified value on a continuous random variable, that is why point probability in continuous case is always equal to zero and we compute probabilities for interval of values. In this unit we consider only continuous uniform distribution and the Normal distribution.',
    'جیسا کہ آپ جانتے ہیں کہ مسلسل تصادفی متغیر پر کسی مخصوص قیمت کی نشاندہی مشکل ہے، اسی لیے مسلسل صورت میں نقطے کا احتمال ہمیشہ صفر ہوتا ہے اور ہم قیمتوں کے وقفے کے احتمالات معلوم کرتے ہیں۔ اس یونٹ میں ہم صرف مسلسل یکساں تقسیم اور نارمل تقسیم پر غور کرتے ہیں۔',
    'لکه څنګه چې پوهېږئ په متصل تصادفي متغیر کې د یوه ټاکلي قیمت موندل ستونزمن دي، له همدې امله په متصل حالت کې د ټکي احتمال تل صفر وي او موږ د قیمتونو د واټن احتمالونه محاسبه کوو. په دې واحد کې یوازې متصل یونیفارم وېش او نورمال وېش په پام کې نیسو.')
b.h('4.1.1 Continuous uniform or rectangular probability distribution', '4.1.1 مسلسل یکساں یا مستطیلی احتمالی تقسیم', '4.1.1 متصل یونیفارم یا مستطیلي احتمالي وېش')
b.p('Like discrete case, continuous uniform distribution is the simplest probability distribution. It is used in the situations where the probability density function f(x) remains constant over the entire range of the variable.',
    'منفصل صورت کی طرح مسلسل یکساں تقسیم سب سے سادہ احتمالی تقسیم ہے۔ یہ ان حالات میں استعمال ہوتی ہے جہاں احتمالی کثافتی تفاعل f(x) متغیر کی پوری حد میں مستقل رہتا ہے۔',
    'د منفصل حالت په څېر، متصل یونیفارم وېش تر ټولو ساده احتمالي وېش دی. په هغو حالتونو کې کارول کېږي چې د احتمال کثافت تابع f(x) د متغیر په ټول حد کې ثابته پاتې کېږي.')
b.h('4.1.2 Definition of continuous uniform probability density function', '4.1.2 مسلسل یکساں احتمالی کثافتی تفاعل کی تعریف', '4.1.2 د متصل یونیفارم د احتمال کثافت تابع تعریف')
b.p('The distribution of a continuous random variable X with pdf', 'مسلسل تصادفی متغیر X کی تقسیم جس کا pdf یہ ہو', 'د متصل تصادفي متغیر X وېش چې pdf یې دا وي')
b.eq(r'f(x)=\left\{\begin{matrix}\frac{1}{b-a}, & a\le x\le b\\ 0 & \textit{otherwise}\end{matrix}\right.')
b.p('is called continuous uniform probability distribution or probability density function and the variable X is called continuous uniform random variable. This distribution has two parameters, a and b. This distribution is also known as rectangular distribution because its graph is like a rectangle given as.',
    'مسلسل یکساں احتمالی تقسیم یا احتمالی کثافتی تفاعل کہلاتی ہے اور متغیر X کو مسلسل یکساں تصادفی متغیر کہتے ہیں۔ اس تقسیم کے دو پیرامیٹر a اور b ہیں۔ اسے مستطیلی تقسیم بھی کہتے ہیں کیونکہ اس کا گراف مستطیل جیسا ہے جو یوں ہے۔',
    'متصل یونیفارم احتمالي وېش یا د احتمال کثافت تابع بلل کېږي او متغیر X ته متصل یونیفارم تصادفي متغیر وایي. دا وېش دوه پارامټرونه a او b لري. دې ته مستطیلي وېش هم وایي ځکه چې ګراف یې د مستطیل په څېر دی چې داسې دی.')
b.visual('stat12-continuous-uniform-graph', continuous_uniform(), ratio=.5)
b.h('4.1.3 Properties of continuous uniform probability distribution', '4.1.3 مسلسل یکساں احتمالی تقسیم کی خصوصیات', '4.1.3 د متصل یونیفارم احتمالي وېش ځانګړنې')
b.h('(i) Mean of continuous uniform probability distribution', '(i) مسلسل یکساں احتمالی تقسیم کا اوسط', '(i) د متصل یونیفارم احتمالي وېش منځنی')
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'\text{Mean}=E(X)=\int_x x\,f(x)\,dx', r'=\int_a^b x\frac{1}{b-a}dx', r'=\frac{1}{b-a}\int_a^b x\,dx', r'=\frac{1}{b-a}\left(\left.\frac{x^2}{2}\right|_a^b\right)',
          r'=\frac{1}{b-a}\left(\frac{b^2-a^2}{2}\right)', r'=\frac{1}{b-a}\left\{\frac{(b-a)(b+a)}{2}\right\}', r'=\frac{a+b}{2}'])
b.h('(ii) Variance of continuous uniform probability distribution', '(ii) مسلسل یکساں احتمالی تقسیم کا تغیر', '(ii) د متصل یونیفارم احتمالي وېش واریانس')
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'\text{Variance}=V(X)=E(X^2)-[E(X)]^2\qquad(i)', r'\text{As } E(X)=\frac{a+b}{2}\qquad(ii)', r'E(X^2)=\int_x x^2f(x)\,dx', r'=\int_a^b x^2\frac{1}{b-a}dx',
          r'=\frac{1}{b-a}\int_a^b x^2dx=\frac{1}{b-a}\left.\frac{x^3}{3}\right|_a^b=\frac{1}{b-a}\left[\frac{b^3-a^3}{3}\right]', r'=\frac{1}{b-a}\;\frac{(b-a)(b^2+ab+a^2)}{3}', r'=\frac{b^2+ab+a^2}{3}\qquad(iii)'])
b.p('Put equation (ii) and equation (iii) in equation (i)', 'مساوات (ii) اور (iii) کو مساوات (i) میں رکھیں', 'د (ii) او (iii) معادلې په (i) معادله کې کېږدئ')
rec = b.build('stat12-p063-continuous-uniform', '4.1 Continuous uniform distribution — definition, mean and variance', '4.1 مسلسل یکساں تقسیم — تعریف، اوسط اور تغیر', '4.1 متصل یونیفارم وېش — تعریف، منځنی او واریانس', 63, [117, 118])

if __name__ == '__main__':
    save(63, [(4, rec)])
