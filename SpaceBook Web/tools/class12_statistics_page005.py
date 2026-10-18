"""PDF5 printed 1–2: Unit 1 opener (learning outcomes) and 1.1 Counting Techniques (factorial, permutation rule)."""
from class12_statistics_common import Builder, save

o = Builder()
o.h('Unit - 01', 'یونٹ - 01', 'واحد - 01')
o.h('PROBABILITY', 'احتمال', 'احتمال')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Know n! (n factorial) as the notation to express the product of first n natural numbers.',
     'n! (n فیکٹوریل) کو پہلے n قدرتی اعداد کے حاصلِ ضرب کی علامت کے طور پر جانیں۔',
     'n! (n فکتوریل) د لومړیو n طبیعي عددونو د ضرب حاصل د ښودلو د نښې په توګه وپېژني.'),
    ('Describe fundamental principles of counting and illustrate it using tree diagram.',
     'گنتی کے بنیادی اصول بیان کریں اور درختی خاکے (tree diagram) کی مدد سے ان کی وضاحت کریں۔',
     'د شمېرنې بنسټیز اصول بیان کړي او د ونې ډوله ډیاګرام (tree diagram) په مرسته یې روښانه کړي.'),
    ('Explain the meaning of permutation and interpret the number of permutations of n different objects taken r at a time.',
     'ترتیبِ مبادلہ (permutation) کا مطلب واضح کریں اور n مختلف اشیاء میں سے ایک وقت میں r لینے سے بننے والے ترتیبات کی تعداد کی تشریح کریں۔',
     'د پرمیوټېشن (ترتیب) مانا تشریح کړي او د n بېلابېلو شیانو څخه په یو وخت کې د r اخیستلو د ترتیبونو شمېر تفسیر کړي.'),
    ('Explain the meaning of combination and interpret the number of combinations of n different objects taken r at a time.',
     'انتخاب (combination) کا مطلب واضح کریں اور n مختلف اشیاء میں سے ایک وقت میں r لینے سے بننے والے انتخابات کی تعداد کی تشریح کریں۔',
     'د کمبینېشن (ټاکنې) مانا تشریح کړي او د n بېلابېلو شیانو څخه په یو وخت کې د r اخیستلو د ټاکنو شمېر تفسیر کړي.'),
    ('Define random experiment, sample space, sample point, event, simple and compound events, impossible and sure events, complementary events, equally likely events, exhaustive events, mutually exclusive events.',
     'تصادفی تجربہ، نمونہ فضا، نمونہ نقطہ، واقعہ، سادہ اور مرکب واقعات، ناممکن اور یقینی واقعات، تکمیلی واقعات، مساوی امکان والے واقعات، جامع واقعات اور باہم مانع واقعات کی تعریف کریں۔',
     'تصادفي تجربه، نمونوي فضا، نمونوي ټکی، پېښه، ساده او مرکبې پېښې، ناشونې او حتمي پېښې، بشپړوونکې پېښې، مساوي امکان لرونکې پېښې، جامع پېښې او یو بل منع کوونکې پېښې تعریف کړي.'),
    ("Elaborate the term 'probability' through classical definition, relative frequency definition. Axiomatic definition.",
     "اصطلاح 'احتمال' کی کلاسیکی تعریف، اضافی تعدد کی تعریف اور مسلّماتی تعریف کے ذریعے وضاحت کریں۔",
     "د 'احتمال' اصطلاح د کلاسیک تعریف، نسبي فریکونسۍ تعریف او اصولي (axiomatic) تعریف له لارې تشریح کړي."),
    ('Recognize the formula for probability of occurrence of an event A',
     'کسی واقعہ A کے وقوع کے احتمال کا فارمولا پہچانیں',
     'د یوې پېښې A د رامنځته کېدو د احتمال فورمول وپېژني'),
    ('Apply the formula and using Venn diagrams to find the probability in simple cases for the occurrence of an event.',
     'فارمولا اور وین خاکوں کی مدد سے سادہ صورتوں میں کسی واقعہ کے وقوع کا احتمال معلوم کریں۔',
     'فورمول او د وېن ډیاګرامونو په کارولو سره په ساده حالتونو کې د یوې پېښې د رامنځته کېدو احتمال پیدا کړي.'),
    ('Describe probability of non-occurrence of an event, odds for the occurrence and odds against the occurrence for an event.',
     'کسی واقعہ کے عدمِ وقوع کا احتمال، وقوع کے حق میں امکان (odds for) اور وقوع کے خلاف امکان (odds against) بیان کریں۔',
     'د یوې پېښې د نه رامنځته کېدو احتمال، د رامنځته کېدو په ګټه چانس (odds for) او د رامنځته کېدو پر ضد چانس (odds against) بیان کړي.'),
    ('Recognize the law of probability of complementation.', 'تکمیل کے احتمال کا قانون پہچانیں۔', 'د بشپړوونې (complementation) د احتمال قانون وپېژني.'),
    ('State the laws of probability under addition and apply them to solve real life problems.',
     'جمع کے تحت احتمال کے قوانین بیان کریں اور حقیقی زندگی کے مسائل حل کرنے میں ان کا اطلاق کریں۔',
     'د جمع لاندې د احتمال قوانین بیان کړي او د ورځني ژوند د ستونزو په حل کې یې وکاروي.'),
    ('Differentiate between dependent and independent events.', 'تابع اور آزاد واقعات میں فرق کریں۔', 'د تړلو او خپلواکو پېښو ترمنځ توپیر وکړي.'),
    ('Define the conditional probability and state the laws of probability under multiplication.',
     'مشروط احتمال کی تعریف کریں اور ضرب کے تحت احتمال کے قوانین بیان کریں۔',
     'شرطي احتمال تعریف کړي او د ضرب لاندې د احتمال قوانین بیان کړي.'),
    ('Apply the laws of probability under multiplication to solve real life problems.',
     'حقیقی زندگی کے مسائل حل کرنے کے لیے ضرب کے تحت احتمال کے قوانین کا اطلاق کریں۔',
     'د ورځني ژوند د ستونزو د حل لپاره د ضرب لاندې د احتمال قوانین وکاروي.'),
    ('Compute probabilities for real life problems involving counting techniques and probability trees.',
     'گنتی کی تکنیکوں اور احتمالی درختوں پر مشتمل حقیقی زندگی کے مسائل کے احتمالات معلوم کریں۔',
     'د ورځني ژوند هغه ستونزې چې د شمېرنې تخنیکونه او احتمالي ونې پکې دي، احتمالونه یې محاسبه کړي.'),
])
opening = o.build('stat12-u1-opening', 'Unit 1 — Learning outcomes', 'یونٹ 1 — حاصلاتِ تعلم', 'واحد 1 — د زده کړې پایلې', 5, [1])

b = Builder()
b.h('1.1 Counting Techniques', '1.1 گنتی کی تکنیکیں', '1.1 د شمېرنې تخنیکونه')
b.p('Counting rules help us to know about the number of all possible results of an experiment without actually writing them. A few of the commonly used counting rules to solve the probability problems are:',
    'گنتی کے قواعد ہمیں کسی تجربے کے تمام ممکنہ نتائج کو اصل میں لکھے بغیر ان کی تعداد جاننے میں مدد دیتے ہیں۔ احتمال کے مسائل حل کرنے کے لیے عام طور پر استعمال ہونے والے چند قواعد یہ ہیں:',
    'د شمېرنې قواعد له موږ سره مرسته کوي چې د یوې تجربې د ټولو شونو پایلو شمېر پرته له دې چې هغه ولیکو، معلوم کړو. د احتمال د ستونزو د حل لپاره ځینې عام کارېدونکي قواعد دا دي:')
b.h('Factorial', 'فیکٹوریل', 'فکتوریل')
b.p('The product of first n natural numbers is called factorial and is denoted by the symbol n! (read n factorial). Thus',
    'پہلے n قدرتی اعداد کے حاصلِ ضرب کو فیکٹوریل کہتے ہیں اور اسے علامت n! (پڑھیں n فیکٹوریل) سے ظاہر کرتے ہیں۔ چنانچہ',
    'د لومړیو n طبیعي عددونو د ضرب حاصل ته فکتوریل وایي او په n! نښه ښودل کېږي (n فکتوریل لوستل کېږي). نو')
b.mlines([r'1!=1', r'2!=2\cdot 1=2', r'3!=3\cdot 2\cdot 1=6', r'4!=4\cdot 3\cdot 2\cdot 1=24', r'5!=5\cdot 4\cdot 3\cdot 2\cdot 1=120',
          r'\vdots', r'n!=n\,(n-1)\,(n-2)\ldots 3\cdot 2\cdot 1'])
b.p('This can simply be written as', 'اسے سادہ طور پر یوں لکھا جا سکتا ہے', 'دا په ساده ډول داسې لیکل کېدای شي')
b.mlines([r'n!=n\,(n-1)\,(n-2)!', r'\phantom{n!}=n\,(n-1)!'])
b.p('Remember that the quantity $0!=1$ arbitrarily defined.', 'یاد رکھیں کہ مقدار $0!=1$ اختیاری طور پر متعین کی گئی ہے۔', 'په یاد ولرئ چې کمیت $0!=1$ په اختیاري ډول تعریف شوی دی.')
b.h('Rule of permutation', 'ترتیبِ مبادلہ (Permutation) کا قاعدہ', 'د پرمیوټېشن (ترتیب) قاعده')
b.p('The groups which can be made from a given number of objects by taking together some or all of the objects at a time with regard to the order of the objects are called permutations. For example, if there are three objects A, B and C, then permutations of size two will be AB, BA, AC, CA, BC, CB. Generally, if we have “n” objects, then total number of permutations of size “r” can be obtained by the formula',
    'دی گئی اشیاء میں سے کچھ یا تمام اشیاء کو ایک وقت میں ان کی ترتیب کا لحاظ رکھتے ہوئے اکٹھا لے کر جو گروہ بنائے جا سکتے ہیں، انہیں ترتیبات (permutations) کہتے ہیں۔ مثال کے طور پر اگر تین اشیاء A، B اور C ہوں تو دو کے سائز کی ترتیبات AB، BA، AC، CA، BC، CB ہوں گی۔ عام طور پر اگر ہمارے پاس “n” اشیاء ہوں تو “r” سائز کی ترتیبات کی کل تعداد اس فارمولا سے حاصل کی جا سکتی ہے',
    'هغه ډلې چې له ورکړل شویو شیانو څخه د شیانو د ترتیب په پام کې نیولو سره په یو وخت کې د ځینو یا ټولو شیانو په یوځای اخیستلو جوړېږي، پرمیوټېشنونه (ترتیبونه) بلل کېږي. د بېلګې په توګه که درې شیان A، B او C وي، نو د دوو په اندازه ترتیبونه به AB، BA، AC، CA، BC، CB وي. په عمومي ډول که موږ “n” شیان ولرو، نو د “r” اندازې د ترتیبونو ټول شمېر له دې فورمول څخه لاسته راځي')
b.eq(r'{}^{n}_{r}P=\frac{n!}{(n-r)!}')
counting = b.build('stat12-p005-counting', '1.1 Counting Techniques — factorial and permutations', '1.1 گنتی کی تکنیکیں — فیکٹوریل اور ترتیبات', '1.1 د شمېرنې تخنیکونه — فکتوریل او ترتیبونه', 5, [2])

if __name__ == '__main__':
    save(5, [(1, opening), (1, counting)])
