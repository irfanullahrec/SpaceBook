"""PDF40 printed 71–72: 3.1 discrete distributions, 3.1.1–3.1.2 discrete uniform distribution, Examples 3.1–3.2, 3.1.3 probability function."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
N = '$\\frac{1}{N}$'
b = Builder()
b.h('3.1 When to use discrete probability distributions', '3.1 منفصل احتمالی تقسیمیں کب استعمال کی جائیں', '3.1 منفصل احتمالي وېشونه کله وکارول شي')
b.p('Discrete probability distributions are used to compute probabilities for all possible values of discrete random variables, by an easy way. In this unit a few simple and commonly used distributions are given that cover many areas in our surrounding. It is important to know and remember that which probability distribution is suitable for a particular situation.',
    'منفصل احتمالی تقسیمیں منفصل تصادفی متغیرات کی تمام ممکنہ قیمتوں کے احتمالات آسان طریقے سے معلوم کرنے کے لیے استعمال ہوتی ہیں۔ اس یونٹ میں چند سادہ اور عام استعمال ہونے والی تقسیمیں دی گئی ہیں جو ہمارے اردگرد کے بہت سے شعبوں کا احاطہ کرتی ہیں۔ یہ جاننا اور یاد رکھنا اہم ہے کہ کسی خاص صورتِ حال کے لیے کون سی احتمالی تقسیم موزوں ہے۔',
    'منفصل احتمالي وېشونه د منفصلو تصادفي متغیرونو د ټولو شونو قیمتونو د احتمالونو د اسانه محاسبې لپاره کارول کېږي. په دې واحد کې ځینې ساده او عام کارېدونکي وېشونه ورکړل شوي چې زموږ د شاوخوا ډېرې برخې رانغاړي. دا پوهېدل او په یاد ساتل مهم دي چې کوم احتمالي وېش د یوه ځانګړي حالت لپاره مناسب دی.')
b.h('3.1.1 Introduction to discrete uniform distribution', '3.1.1 منفصل یکساں تقسیم کا تعارف', '3.1.1 د منفصل یونیفارم وېش پېژندنه')
b.p('This is the simplest probability distribution among the discrete probability distributions. It is used in the experiments/situations where probability at every point remains the same e.g. the outcomes of rolling a fair die, drawing cards from a well shuffled deck of cards, drawing of prize bond number etc. follow uniform distribution. A variable denoting the outcomes of such uniform experiments is called discrete uniform random variable and its probability distribution is called discrete uniform probability distribution. The most important application of the uniform distribution is in the generation of random numbers.',
    'یہ منفصل احتمالی تقسیموں میں سب سے سادہ احتمالی تقسیم ہے۔ یہ ان تجربات/حالات میں استعمال ہوتی ہے جہاں ہر نقطے پر احتمال یکساں رہتا ہے، مثلاً منصفانہ پانسہ پھینکنے کے نتائج، اچھی طرح پھینٹی گئی گڈی سے پتے نکالنا، پرائز بانڈ نمبر کی قرعہ اندازی وغیرہ یکساں تقسیم کی پیروی کرتے ہیں۔ ایسے یکساں تجربات کے نتائج ظاہر کرنے والے متغیر کو منفصل یکساں تصادفی متغیر اور اس کی احتمالی تقسیم کو منفصل یکساں احتمالی تقسیم کہتے ہیں۔ یکساں تقسیم کا سب سے اہم اطلاق تصادفی اعداد پیدا کرنے میں ہے۔',
    'دا د منفصلو احتمالي وېشونو له منځه تر ټولو ساده احتمالي وېش دی. په هغو تجربو/حالتونو کې کارول کېږي چې په هر ټکي کې احتمال یو شان پاتې کېږي، لکه د عادلانه ډایس د اچولو پایلې، له ښه ګډې شوې ګډۍ څخه د کارتونو راایستل، د پرایز بانډ د شمېرې قرعه او نور یونیفارم وېش تعقیبوي. هغه متغیر چې د داسې یونیفارم تجربو پایلې ښيي، منفصل یونیفارم تصادفي متغیر او احتمالي وېش یې منفصل یونیفارم احتمالي وېش بلل کېږي. د یونیفارم وېش تر ټولو مهم کارول د تصادفي عددونو په جوړولو کې دي.')
b.h('3.1.2 Definition', '3.1.2 تعریف', '3.1.2 تعریف')
b.p('A probability distribution of the type:', 'اس قسم کی احتمالی تقسیم:', 'د دې ډول احتمالي وېش:')
b.dist('stat12-t-uniform-general', ['$x_1$', '$x_2$', '$x_3$', '$\\cdots$', '$x_N$'], [N] * 5)
b.p('is called discrete uniform probability distribution.', 'منفصل یکساں احتمالی تقسیم کہلاتی ہے۔', 'منفصل یونیفارم احتمالي وېش بلل کېږي.')
b.h('Example 3.1', 'مثال 3.1', 'بېلګه 3.1')
b.p('Find probability distribution for the outcomes of a fair die when it is rolled once.', 'منصفانہ پانسہ ایک بار پھینکنے پر نتائج کی احتمالی تقسیم معلوم کریں۔', 'کله چې یو عادلانه ډایس یو ځل واچول شي، د پایلو احتمالي وېش پیدا کړئ.')
b.h(*SOL)
b.p('When a fair die is rolled once, then all outcomes are equally likely, therefore, its probability distribution is given by', 'جب منصفانہ پانسہ ایک بار پھینکا جائے تو تمام نتائج مساوی امکان والے ہوتے ہیں، لہٰذا اس کی احتمالی تقسیم یہ ہے', 'کله چې عادلانه ډایس یو ځل واچول شي، ټولې پایلې مساوي امکان لري، نو احتمالي وېش یې دا دی')
b.dist('stat12-t-ex3-1', ['1', '2', '3', '4', '5', '6'], ['$\\frac{1}{6}$'] * 6)
b.p('Note that X follows discrete uniform distribution.', 'نوٹ کریں کہ X منفصل یکساں تقسیم کی پیروی کرتا ہے۔', 'پام وکړئ چې X منفصل یونیفارم وېش تعقیبوي.')
b.h('3.1.3 Definition of discrete uniform probability function', '3.1.3 منفصل یکساں احتمالی تفاعل کی تعریف', '3.1.3 د منفصل یونیفارم احتمالي تابع تعریف')
b.p('A probability function defined as $p(x)=\\left\\{\\begin{matrix}\\frac{1}{N}, & x=1,2,\\cdots,N\\\\ 0, & \\textit{otherwise}\\end{matrix}\\right.$ is called discrete uniform probability function and the variable X is called discrete uniform random variable. This distribution has only one parameter “N”, the total number of results /items of a uniform experiment.',
    'اس طرح متعین احتمالی تفاعل $p(x)=\\left\\{\\begin{matrix}\\frac{1}{N}, & x=1,2,\\cdots,N\\\\ 0, & \\textit{otherwise}\\end{matrix}\\right.$ منفصل یکساں احتمالی تفاعل کہلاتا ہے اور متغیر X کو منفصل یکساں تصادفی متغیر کہتے ہیں۔ اس تقسیم کا صرف ایک پیرامیٹر “N” ہے، یعنی یکساں تجربے کے نتائج/اشیاء کی کل تعداد۔',
    'هغه احتمالي تابع چې داسې تعریف شوې $p(x)=\\left\\{\\begin{matrix}\\frac{1}{N}, & x=1,2,\\cdots,N\\\\ 0, & \\textit{otherwise}\\end{matrix}\\right.$ منفصل یونیفارم احتمالي تابع بلل کېږي او متغیر X ته منفصل یونیفارم تصادفي متغیر وایي. دا وېش یوازې یو پارامټر “N” لري، یعنې د یونیفارم تجربې د پایلو/شیانو ټول شمېر.')
b.h('Example 3.2', 'مثال 3.2', 'بېلګه 3.2')
b.p('Write discrete uniform probability function for the results of a fair die when it is rolled once.', 'منصفانہ پانسہ ایک بار پھینکنے کے نتائج کے لیے منفصل یکساں احتمالی تفاعل لکھیں۔', 'د عادلانه ډایس د یو ځل اچولو د پایلو لپاره منفصل یونیفارم احتمالي تابع ولیکئ.')
b.h(*SOL)
b.p('Here random variable X takes all of its values with equal probability $\\frac{1}{6}$. Thus, discrete uniform probability function will be of the form:', 'یہاں تصادفی متغیر X اپنی تمام قیمتیں یکساں احتمال $\\frac{1}{6}$ کے ساتھ لیتا ہے۔ لہٰذا منفصل یکساں احتمالی تفاعل اس شکل کا ہوگا:', 'دلته تصادفي متغیر X خپل ټول قیمتونه په مساوي احتمال $\\frac{1}{6}$ اخلي. نو منفصل یونیفارم احتمالي تابع به دا بڼه ولري:')
b.eq(r'p(x)=\begin{bmatrix}\frac{1}{6}, & x=1,2,3,4,5,6\\ 0, & \textit{otherwise}\end{bmatrix}')
b.p('◆ Graphical representation of discrete uniform distribution by means of a histogram is a set of adjacent rectangles with equal heights i.e.', '◆ ہسٹوگرام کے ذریعے منفصل یکساں تقسیم کی ترسیمی نمائندگی مساوی بلندی والے ملحقہ مستطیلوں کا مجموعہ ہے یعنی', '◆ د هسټوګرام په واسطه د منفصل یونیفارم وېش ګرافیکي ښودنه د مساوي لوړوالي لرونکو نښتو مستطیلونو ټولګه ده یعنې')
rec = b.build('stat12-p040-discrete-uniform', '3.1 Discrete uniform distribution — definition and Examples 3.1–3.2', '3.1 منفصل یکساں تقسیم — تعریف اور مثالیں 3.1–3.2', '3.1 منفصل یونیفارم وېش — تعریف او بېلګې 3.1–3.2', 40, [71, 72])

if __name__ == '__main__':
    save(40, [(3, rec)])
