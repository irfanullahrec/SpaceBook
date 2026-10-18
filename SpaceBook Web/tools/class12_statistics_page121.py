"""PDF121 printed 233–234: 7.1.3 key terms — null/alternative, simple/composite hypotheses, type-I and type-II errors with examples."""
from class12_statistics_common import Builder, save

b = Builder()
b.h('7.1.3 Definitions of key terms', '7.1.3 اہم اصطلاحات کی تعریفیں', '7.1.3 د کلیدي اصطلاحګانو تعریفونه')
b.h('• Null hypothesis', '• صفری مفروضہ', '• صفري فرضیه')
b.p('It is a claim about parameter. It is tested for possible rejection under the assumption that it is true. It is denoted by $H_0$.', 'یہ پیرامیٹر کے بارے میں ایک دعویٰ ہے۔ اسے درست مان کر ممکنہ رد کے لیے جانچا جاتا ہے۔ اسے $H_0$ سے ظاہر کرتے ہیں۔', 'دا د پارامټر په اړه یوه ادعا ده. په دې انګېرنه چې سمه ده، د شوني ردولو لپاره ازمویل کېږي. په $H_0$ ښودل کېږي.')
b.h('• Alternative hypothesis', '• متبادل مفروضہ', '• بدیله فرضیه')
b.p('It is also a claim about parameter which is accepted if $H_0$ is rejected. It is denoted by $H_1$. It may be directional or non-directional.', 'یہ بھی پیرامیٹر کے بارے میں ایک دعویٰ ہے جو $H_0$ کے رد ہونے پر قبول کیا جاتا ہے۔ اسے $H_1$ سے ظاہر کرتے ہیں۔ یہ سمتی یا غیر سمتی ہو سکتا ہے۔', 'دا هم د پارامټر په اړه یوه ادعا ده چې که $H_0$ رد شي منل کېږي. په $H_1$ ښودل کېږي. کېدای شي لوري لرونکې یا بې‌لوري وي.')
b.h('• Simple hypothesis', '• سادہ مفروضہ', '• ساده فرضیه')
b.p('When all parameters of a distribution are well specified under the hypothesis it is called simple hypothesis. For example in case of normal distribution if $H_0:\\mu=5,\\ \\sigma^2=2.5$, it is simple hypothesis because all parameters values are well specified under $H_0$.', 'جب مفروضے کے تحت کسی تقسیم کے تمام پیرامیٹرز واضح طور پر مقرر ہوں تو اسے سادہ مفروضہ کہتے ہیں۔ مثلاً نارمل تقسیم کی صورت میں اگر $H_0:\\mu=5,\\ \\sigma^2=2.5$ ہو تو یہ سادہ مفروضہ ہے کیونکہ $H_0$ کے تحت تمام پیرامیٹرز کی قیمتیں واضح طور پر مقرر ہیں۔', 'کله چې د فرضیې لاندې د یوه وېش ټول پارامټرونه په ښه ډول مشخص وي، ساده فرضیه بلل کېږي. د بېلګې په توګه د نورمال وېش په حالت کې که $H_0:\\mu=5,\\ \\sigma^2=2.5$ وي، ساده فرضیه ده ځکه چې د $H_0$ لاندې د ټولو پارامټرونو قیمتونه ښه مشخص دي.')
b.h('• Composite hypothesis', '• مرکب مفروضہ', '• مرکبه فرضیه')
b.p('When all parameters of a distribution are not well specified under the hypothesis it is called composite hypothesis. For example for normal distribution $H_0:\\mu=5,\\ \\sigma^2\\le 2.5$ or $H_0:\\mu<5,\\ \\sigma^2=2.5$ or $H_0:\\mu=5$, σ unknown etc. are composite hypothesis because in the first two cases values are not well specified and in the third case all parameters are not considered. The concept of simple and composite hypothesis is applicable to both $H_0$ and $H_1$.',
    'جب مفروضے کے تحت کسی تقسیم کے تمام پیرامیٹرز واضح طور پر مقرر نہ ہوں تو اسے مرکب مفروضہ کہتے ہیں۔ مثلاً نارمل تقسیم کے لیے $H_0:\\mu=5,\\ \\sigma^2\\le 2.5$ یا $H_0:\\mu<5,\\ \\sigma^2=2.5$ یا $H_0:\\mu=5$، σ نامعلوم وغیرہ مرکب مفروضے ہیں کیونکہ پہلی دو صورتوں میں قیمتیں واضح طور پر مقرر نہیں اور تیسری صورت میں تمام پیرامیٹرز زیرِ غور نہیں۔ سادہ اور مرکب مفروضے کا تصور $H_0$ اور $H_1$ دونوں پر لاگو ہوتا ہے۔',
    'کله چې د فرضیې لاندې د یوه وېش ټول پارامټرونه ښه مشخص نه وي، مرکبه فرضیه بلل کېږي. د بېلګې په توګه د نورمال وېش لپاره $H_0:\\mu=5,\\ \\sigma^2\\le 2.5$ یا $H_0:\\mu<5,\\ \\sigma^2=2.5$ یا $H_0:\\mu=5$، σ نامعلوم او نور مرکبې فرضیې دي ځکه چې په لومړیو دوو حالتونو کې قیمتونه ښه مشخص نه دي او په درېیم حالت کې ټول پارامټرونه په پام کې نه دي نیول شوي. د ساده او مرکبې فرضیې مفهوم پر دواړو $H_0$ او $H_1$ تطبیقېږي.')
b.h('• Type-I and Type-II errors', '• پہلی قسم اور دوسری قسم کی غلطیاں', '• لومړی ډول او دویم ډول تېروتنې')
b.p('Two types of errors are possible in making a decision about a hypothesis.', 'کسی مفروضے کے بارے میں فیصلہ کرنے میں دو قسم کی غلطیاں ممکن ہیں۔', 'د یوې فرضیې په اړه د پرېکړې په کولو کې دوه ډوله تېروتنې شونې دي.')
b.h('(1) Type-I error', '(1) پہلی قسم کی غلطی', '(1) لومړی ډول تېروتنه')
b.p('“To reject a null hypothesis when it is true, it is called type-I error”', '“صفری مفروضے کو درست ہونے کے باوجود رد کرنا پہلی قسم کی غلطی کہلاتا ہے”', '“صفري فرضیه ردول په داسې حال کې چې سمه وي، لومړی ډول تېروتنه بلل کېږي”')
b.h('Examples', 'مثالیں', 'بېلګې')
b.group('lines', [
    ('i. If a medicine is given to a few patients of a particular disease to cure them and the medicine is curing the disease, but it is claimed that it has no effect or has an adverse effect and hence discontinued. This is Type-I error.', 'i. اگر کسی خاص بیماری کے چند مریضوں کو علاج کے لیے دوا دی جائے اور دوا بیماری کو ٹھیک کر رہی ہو، لیکن دعویٰ کیا جائے کہ اس کا کوئی اثر نہیں یا الٹا اثر ہے اور اس لیے اسے بند کر دیا جائے۔ یہ پہلی قسم کی غلطی ہے۔', 'i. که د یوې ځانګړې ناروغۍ څو ناروغانو ته د روغتیا لپاره درمل ورکړل شي او درمل ناروغي روغوي، خو ادعا وشي چې هېڅ اغېز نه لري یا منفي اغېز لري او له همدې امله بند شي. دا لومړی ډول تېروتنه ده.'),
    ('ii. To fail an intelligent student.', 'ii. ذہین طالب علم کو فیل کرنا۔', 'ii. یو هوښیار زده کوونکی ناکام کول.'),
    ('iii. To punish an innocent person.', 'iii. بے گناہ شخص کو سزا دینا۔', 'iii. یو بې‌ګناه کس ته سزا ورکول.'),
    ('iv. When a good player is not played in the cricket match.', 'iv. جب کرکٹ میچ میں اچھے کھلاڑی کو نہ کھلایا جائے۔', 'iv. کله چې په کرکټ لوبه کې ښه لوبغاړی ونه لوبول شي.'),
    ('v. To reject a good item.', 'v. اچھی شے کو رد کرنا۔', 'v. یو ښه توکی ردول.'),
])
b.p('The probability of committing type-I error is denoted by α i.e. $\\alpha=p(\\text{reject }H_0/H_0\\text{ is true})$', 'پہلی قسم کی غلطی کے ارتکاب کے احتمال کو α سے ظاہر کرتے ہیں یعنی $\\alpha=p(\\text{reject }H_0/H_0\\text{ is true})$', 'د لومړي ډول تېروتنې د کولو احتمال په α ښودل کېږي یعنې $\\alpha=p(\\text{reject }H_0/H_0\\text{ is true})$')
b.h('(2) Type-II error', '(2) دوسری قسم کی غلطی', '(2) دویم ډول تېروتنه')
b.p('“To accept a null hypothesis when it is false, it is called type-II error.”', '“صفری مفروضے کو غلط ہونے کے باوجود قبول کرنا دوسری قسم کی غلطی کہلاتا ہے۔”', '“صفري فرضیه منل په داسې حال کې چې ناسمه وي، دویم ډول تېروتنه بلل کېږي.”')
b.h('Examples', 'مثالیں', 'بېلګې')
b.group('lines', [
    ('i. If the medicine has adverse effect and is claimed to have good effect and the treatment is continued. This is type-II error.', 'i. اگر دوا کا الٹا اثر ہو اور دعویٰ کیا جائے کہ اس کا اچھا اثر ہے اور علاج جاری رکھا جائے۔ یہ دوسری قسم کی غلطی ہے۔', 'i. که درمل منفي اغېز ولري او ادعا وشي چې ښه اغېز لري او درملنه دوام وکړي. دا دویم ډول تېروتنه ده.'),
    ('ii. To pass a dull student.', 'ii. کند ذہن طالب علم کو پاس کرنا۔', 'ii. یو کمزوری زده کوونکی بریالی کول.'),
    ('iii. To release a guilty person.', 'iii. مجرم کو رہا کرنا۔', 'iii. یو مجرم خوشې کول.'),
    ('iv. To allow a non-deserving player in the cricket match.', 'iv. کرکٹ میچ میں غیر مستحق کھلاڑی کو اجازت دینا۔', 'iv. په کرکټ لوبه کې نامستحق لوبغاړي ته اجازه ورکول.'),
    ('v. To accept a bad item.', 'v. خراب شے کو قبول کرنا۔', 'v. یو خراب توکی منل.'),
])
b.p('The probability of committing type-II error is denoted by β i.e. $\\beta=p(\\text{accept }H_0/H_0\\text{ is false})$', 'دوسری قسم کی غلطی کے ارتکاب کے احتمال کو β سے ظاہر کرتے ہیں یعنی $\\beta=p(\\text{accept }H_0/H_0\\text{ is false})$', 'د دویم ډول تېروتنې د کولو احتمال په β ښودل کېږي یعنې $\\beta=p(\\text{accept }H_0/H_0\\text{ is false})$')
b.h('Remember that', 'یاد رکھیں کہ', 'په یاد ولرئ چې')
b.group('lines', [
    ('(i) Type-I error is more serious than type-II error.', '(i) پہلی قسم کی غلطی دوسری قسم کی غلطی سے زیادہ سنگین ہے۔', '(i) لومړی ډول تېروتنه تر دویم ډول تېروتنې ډېره جدي ده.'),
    ('(ii) α and β have an inverse relation i.e. if one increases the other decreases and vice-versa.', '(ii) α اور β کا معکوس تعلق ہے یعنی اگر ایک بڑھے تو دوسرا کم ہوتا ہے اور اس کے برعکس۔', '(ii) α او β معکوسه اړیکه لري یعنې که یو زیات شي بل کمېږي او برعکس.'),
    ('(iii) Both α and β can be decreased by increasing n.', '(iii) n بڑھا کر α اور β دونوں کم کیے جا سکتے ہیں۔', '(iii) د n په زیاتولو α او β دواړه کمېدای شي.'),
])
rec = b.build('stat12-p121-key-terms-errors', '7.1.3 Key terms — hypotheses and type-I/type-II errors', '7.1.3 اہم اصطلاحات — مفروضے اور پہلی/دوسری قسم کی غلطیاں', '7.1.3 کلیدي اصطلاحګانې — فرضیې او لومړی/دویم ډول تېروتنې', 121, [233, 234])

if __name__ == '__main__':
    save(121, [(7, rec)])
