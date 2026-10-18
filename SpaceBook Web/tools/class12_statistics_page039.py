"""PDF39 printed 69–70: Unit 2 questions 2.21–2.24 (end of Unit 2); Unit 3 opener with learning outcomes."""
from class12_statistics_common import Builder, save

b = Builder()
Q = lambda n, e, u, p: b.p(f'{n} {e}', f'{n} {u}', f'{n} {p}')
Q('2.21', 'Find mean, variance and standard deviation for the random variable Y whose p.d.f is $f(y)=\\left\\{\\begin{matrix}\\frac{2}{3}(2-y), & 0\\le y\\le 1\\\\ 0, & \\textit{elsewhere}\\end{matrix}\\right.$',
  'تصادفی متغیر Y کا اوسط، تغیر اور معیاری انحراف معلوم کریں جس کا p.d.f یہ ہے $f(y)=\\left\\{\\begin{matrix}\\frac{2}{3}(2-y), & 0\\le y\\le 1\\\\ 0, & \\textit{elsewhere}\\end{matrix}\\right.$',
  'د تصادفي متغیر Y منځنی، واریانس او معیاري انحراف پیدا کړئ چې p.d.f یې دا ده $f(y)=\\left\\{\\begin{matrix}\\frac{2}{3}(2-y), & 0\\le y\\le 1\\\\ 0, & \\textit{elsewhere}\\end{matrix}\\right.$')
Q('2.22', 'The joint distribution of two independent random variables X and Y is', 'دو آزاد تصادفی متغیرات X اور Y کی مشترکہ تقسیم یہ ہے', 'د دوو خپلواکو تصادفي متغیرونو X او Y ګډ وېش دا دی')
b.grid('stat12-t-q2-22', ['$X\\backslash Y$', '0', '1'], [['1', '1/6', '1/6'], ['2', '1/6', '1/6'], ['3', '1/6', '1/6']])
b.p('Find E(X), E(Y), E(X+Y), E(XY)', 'معلوم کریں E(X)، E(Y)، E(X+Y)، E(XY)', 'پیدا کړئ E(X)، E(Y)، E(X+Y)، E(XY)')
Q('2.23', 'Suppose that X and Y have the following joint distribution.', 'فرض کریں X اور Y کی مشترکہ تقسیم یہ ہے۔', 'فرض کړئ X او Y لاندې ګډ وېش لري.')
b.grid('stat12-t-q2-23', ['$X\\backslash Y$', '10', '20', '40', '80'], [['20', '0.04', '0.08', '0.08', '0.05'], ['40', '0.12', '0.24', '0.24', '0.15']])
b.group('lines', [
    ('(i) Are X and Y independent?', '(i) کیا X اور Y آزاد ہیں؟', '(i) آیا X او Y خپلواک دي؟'),
    ('(ii) Find E(X), E(Y), E(X+Y), E(XY)', '(ii) معلوم کریں E(X)، E(Y)، E(X+Y)، E(XY)', '(ii) پیدا کړئ E(X)، E(Y)، E(X+Y)، E(XY)'),
])
Q('2.24', 'For the following joint distribution:', 'درج ذیل مشترکہ تقسیم کے لیے:', 'د لاندې ګډ وېش لپاره:')
b.grid('stat12-t-q2-24', ['$X\\backslash Y$', '1', '2'], [['0', '.06', '.04'], ['1', '.30', '.20'], ['2', '.24', '.16']])
b.p('Find (i) V(X) (ii) V(Y) (iii) V(X+Y) (iv) V(X−Y)', 'معلوم کریں (i) V(X) (ii) V(Y) (iii) V(X+Y) (iv) V(X−Y)', 'پیدا کړئ (i) V(X) (ii) V(Y) (iii) V(X+Y) (iv) V(X−Y)')
ex = b.build('stat12-u2-exercise-d', 'Unit 2 Exercise — questions 2.21 to 2.24', 'یونٹ 2 مشق — سوالات 2.21 تا 2.24', 'واحد 2 تمرین — پوښتنې 2.21 تر 2.24', 39, [69])

o = Builder()
o.h('Unit - 03', 'یونٹ - 03', 'واحد - 03')
o.h('Special Discrete Probability Distributions', 'خاص منفصل احتمالی تقسیمیں', 'ځانګړي منفصل احتمالي وېشونه')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Define discrete uniform random variable, discrete uniform probability distribution and discrete uniform probability mass function.', 'منفصل یکساں تصادفی متغیر، منفصل یکساں احتمالی تقسیم اور منفصل یکساں احتمالی کمیتی تفاعل کی تعریف کریں۔', 'منفصل یونیفارم تصادفي متغیر، منفصل یونیفارم احتمالي وېش او منفصل یونیفارم د احتمال کتلوي تابع تعریف کړي.'),
    ('Calculate mean, variance and standard deviation of discrete uniform probability distribution', 'منفصل یکساں احتمالی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں', 'د منفصل یونیفارم احتمالي وېش منځنی، واریانس او معیاري انحراف محاسبه کړي'),
    ('Define random digits/numbers and to know, how the random digits/numbers are generated.', 'تصادفی ہندسوں/اعداد کی تعریف کریں اور جانیں کہ تصادفی ہندسے/اعداد کیسے پیدا کیے جاتے ہیں۔', 'تصادفي رقمونه/عددونه تعریف کړي او پوه شي چې تصادفي رقمونه/عددونه څنګه جوړېږي.'),
    ('Solve real life problems using discrete uniform probability distribution.', 'منفصل یکساں احتمالی تقسیم کی مدد سے حقیقی زندگی کے مسائل حل کریں۔', 'د منفصل یونیفارم احتمالي وېش په کارولو سره د ورځني ژوند ستونزې حل کړي.'),
    ('Define Bernoulli trials, Bernoulli probability distribution and Bernoulli mass function.', 'برنولی آزمائشوں، برنولی احتمالی تقسیم اور برنولی کمیتی تفاعل کی تعریف کریں۔', 'د برنولي ازمېښتونه، د برنولي احتمالي وېش او د برنولي کتلوي تابع تعریف کړي.'),
    ('Calculate mean, variance and standard deviation of Bernoulli probability distribution.', 'برنولی احتمالی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں۔', 'د برنولي احتمالي وېش منځنی، واریانس او معیاري انحراف محاسبه کړي.'),
    ('Solve real life problems using Bernoulli probability distribution.', 'برنولی احتمالی تقسیم کی مدد سے حقیقی زندگی کے مسائل حل کریں۔', 'د برنولي احتمالي وېش په کارولو سره د ورځني ژوند ستونزې حل کړي.'),
    ('Define Binomial experiment, Binomial random variable, Binomial probability distribution, Binomial probability mass function and Binomial frequency distribution.', 'دو رقمی (Binomial) تجربہ، دو رقمی تصادفی متغیر، دو رقمی احتمالی تقسیم، دو رقمی احتمالی کمیتی تفاعل اور دو رقمی تعددی تقسیم کی تعریف کریں۔', 'بینومیل تجربه، بینومیل تصادفي متغیر، بینومیل احتمالي وېش، بینومیل د احتمال کتلوي تابع او بینومیل فریکونسي وېش تعریف کړي.'),
    ('Calculate mean, variance and standard deviation of Binomial probability distribution', 'دو رقمی احتمالی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں', 'د بینومیل احتمالي وېش منځنی، واریانس او معیاري انحراف محاسبه کړي'),
    ('Solve real life problems using Binomial probability distribution.', 'دو رقمی احتمالی تقسیم کی مدد سے حقیقی زندگی کے مسائل حل کریں۔', 'د بینومیل احتمالي وېش په کارولو سره د ورځني ژوند ستونزې حل کړي.'),
    ('Define hypergeometric experiment, hypergeometric random variable, hypergeometric probability distribution and hypergeometric probability mass function.', 'ہائپر جیومیٹرک تجربہ، ہائپر جیومیٹرک تصادفی متغیر، ہائپر جیومیٹرک احتمالی تقسیم اور ہائپر جیومیٹرک احتمالی کمیتی تفاعل کی تعریف کریں۔', 'هایپرجیومټریک تجربه، هایپرجیومټریک تصادفي متغیر، هایپرجیومټریک احتمالي وېش او هایپرجیومټریک د احتمال کتلوي تابع تعریف کړي.'),
    ('Calculate mean, variance and standard deviation of hypergeometric probability distribution', 'ہائپر جیومیٹرک احتمالی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں', 'د هایپرجیومټریک احتمالي وېش منځنی، واریانس او معیاري انحراف محاسبه کړي'),
    ('Solve real life problems using hypergeometric probability distribution.', 'ہائپر جیومیٹرک احتمالی تقسیم کی مدد سے حقیقی زندگی کے مسائل حل کریں۔', 'د هایپرجیومټریک احتمالي وېش په کارولو سره د ورځني ژوند ستونزې حل کړي.'),
])
opening = o.build('stat12-u3-opening', 'Unit 3 — Learning outcomes', 'یونٹ 3 — حاصلاتِ تعلم', 'واحد 3 — د زده کړې پایلې', 39, [70])

if __name__ == '__main__':
    save(39, [(2, ex), (3, opening)], complete_units=[2])
