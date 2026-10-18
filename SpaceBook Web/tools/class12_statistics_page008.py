"""PDF8 printed 7–8: compound, sure, complementary, equally likely, mutually exclusive, exhaustive, dependent and
independent events; 1.2.4 definitions of probability (classical, relative frequency, axiomatic — Axiom I)."""
from class12_statistics_common import Builder, save

b = Builder()
b.h('Compound event', 'مرکب واقعہ', 'مرکبه پېښه')
b.p('An event which contains more than one outcome is called compound event. For example, event $A=\\{4,6\\}$ or event $A=\\{1,3,5\\}$ etc. in rolling of a die are examples of compound event.',
    'وہ واقعہ جس میں ایک سے زیادہ نتائج ہوں، مرکب واقعہ کہلاتا ہے۔ مثلاً پانسہ پھینکنے میں واقعہ $A=\\{4,6\\}$ یا واقعہ $A=\\{1,3,5\\}$ وغیرہ مرکب واقعات کی مثالیں ہیں۔',
    'هغه پېښه چې له یوې څخه زیاتې پایلې ولري، مرکبه پېښه بلل کېږي. د بېلګې په توګه د ډایس په اچولو کې پېښه $A=\\{4,6\\}$ یا پېښه $A=\\{1,3,5\\}$ او نور د مرکبې پېښې بېلګې دي.')
b.h('Sure event', 'یقینی واقعہ', 'حتمي پېښه')
b.p('An event which contains all results of the sample space is called sure or certain event. For example, event $A=\\{1,2,3,4,5,6\\}$ when a die is rolled once, is a sure event.',
    'وہ واقعہ جس میں نمونہ فضا کے تمام نتائج شامل ہوں، یقینی یا حتمی واقعہ کہلاتا ہے۔ مثلاً پانسہ ایک بار پھینکنے پر واقعہ $A=\\{1,2,3,4,5,6\\}$ یقینی واقعہ ہے۔',
    'هغه پېښه چې د نمونوي فضا ټولې پایلې ولري، حتمي یا یقیني پېښه بلل کېږي. د بېلګې په توګه د ډایس په یو ځل اچولو کې پېښه $A=\\{1,2,3,4,5,6\\}$ حتمي پېښه ده.')
b.h('Complementary event', 'تکمیلی واقعہ', 'بشپړوونکې پېښه')
b.p('An event, denoted by “$\\overline{A}$” is said to be complementary to an event “A” in a sample space, if $\\overline{A}$ consists of all those sample points which are not contained in A. For example, if we roll a die, then $S=\\{1,2,3,4,5,6\\}$. Let $A=\\{1,3,5\\}$, then $\\overline{A}=\\{2,4,6\\}$.',
    'کسی نمونہ فضا میں “$\\overline{A}$” سے ظاہر کیا گیا واقعہ، واقعہ “A” کا تکمیلی کہلاتا ہے اگر $\\overline{A}$ میں وہ تمام نمونہ نقاط ہوں جو A میں شامل نہیں۔ مثلاً اگر ہم پانسہ پھینکیں تو $S=\\{1,2,3,4,5,6\\}$۔ فرض کریں $A=\\{1,3,5\\}$، تو $\\overline{A}=\\{2,4,6\\}$۔',
    'په یوه نمونوي فضا کې هغه پېښه چې په “$\\overline{A}$” ښودل کېږي، د “A” پېښې بشپړوونکې ویل کېږي که $\\overline{A}$ هغه ټول نمونوي ټکي ولري چې په A کې نه دي. د بېلګې په توګه که ډایس واچوو، نو $S=\\{1,2,3,4,5,6\\}$. فرض کړئ $A=\\{1,3,5\\}$، نو $\\overline{A}=\\{2,4,6\\}$.')
b.p('Remember that $A\\cup\\overline{A}=S$.', 'یاد رکھیں کہ $A\\cup\\overline{A}=S$۔', 'په یاد ولرئ چې $A\\cup\\overline{A}=S$.')
b.h('Equally likely events', 'مساوی امکان والے واقعات', 'مساوي امکان لرونکې پېښې')
b.p('Events are said to be equally likely if they have the same chance of occurrence. For example, if we toss a fair coin, then head (H) and tail (T) have same chance of occurrence. So head and tail are equally likely events.',
    'واقعات مساوی امکان والے کہلاتے ہیں اگر ان کے وقوع کا موقع یکساں ہو۔ مثلاً اگر ہم ایک منصفانہ سکہ اچھالیں تو چِت (H) اور پَٹ (T) کے آنے کا موقع یکساں ہے۔ لہٰذا چِت اور پَٹ مساوی امکان والے واقعات ہیں۔',
    'پېښې هغه وخت مساوي امکان لرونکې بلل کېږي چې د رامنځته کېدو یو شان چانس ولري. د بېلګې په توګه که یوه عادلانه سکه واچوو، نو سر (H) او لکۍ (T) د راتلو یو شان چانس لري. نو سر او لکۍ مساوي امکان لرونکې پېښې دي.')
b.h('Mutually exclusive events', 'باہم مانع واقعات', 'یو بل منع کوونکې پېښې')
b.p('If two events cannot occur simultaneously then they are called mutually exclusive events. For example, if we toss a coin, H and T cannot occur together so they are mutually exclusive events. Similarly, success and failure, male and female births etc. are mutually exclusive events.',
    'اگر دو واقعات بیک وقت واقع نہ ہو سکیں تو انہیں باہم مانع واقعات کہتے ہیں۔ مثلاً سکہ اچھالنے پر H اور T اکٹھے نہیں آ سکتے، لہٰذا یہ باہم مانع واقعات ہیں۔ اسی طرح کامیابی اور ناکامی، لڑکے اور لڑکی کی پیدائش وغیرہ باہم مانع واقعات ہیں۔',
    'که دوه پېښې په یو وخت رامنځته نه شي، نو یو بل منع کوونکې پېښې بلل کېږي. د بېلګې په توګه د سکې په اچولو کې H او T یوځای نه شي راتلای، نو دا یو بل منع کوونکې پېښې دي. همداراز بریا او ناکامي، د هلک او نجلۍ زېږون او نور یو بل منع کوونکې پېښې دي.')
b.h('Exhaustive events', 'جامع واقعات', 'جامع پېښې')
b.p('Events are called exhaustive if (i) they are mutually exclusive events and (ii) their union makes again the entire sample space.',
    'واقعات جامع کہلاتے ہیں اگر (i) وہ باہم مانع ہوں اور (ii) ان کا اتصال دوبارہ پوری نمونہ فضا بنا دے۔',
    'پېښې جامع بلل کېږي که (i) یو بل منع کوونکې وي او (ii) د هغو یووالی بیا ټوله نمونوي فضا جوړه کړي.')
b.h('Dependent events', 'تابع واقعات', 'تړلې پېښې')
b.p('If the occurrence of an event affects the probability of occurrence of another event, they are called dependent events. Without replacement sampling is an example of dependent events.',
    'اگر ایک واقعہ کا وقوع کسی دوسرے واقعہ کے وقوع کے احتمال پر اثر ڈالے تو انہیں تابع واقعات کہتے ہیں۔ بغیر واپسی (without replacement) نمونہ گیری تابع واقعات کی ایک مثال ہے۔',
    'که د یوې پېښې رامنځته کېدل د بلې پېښې د رامنځته کېدو پر احتمال اغېز وکړي، نو تړلې پېښې بلل کېږي. بې له بېرته اچولو (without replacement) نمونه اخیستنه د تړلو پېښو بېلګه ده.')
b.h('Independent events', 'آزاد واقعات', 'خپلواکې پېښې')
b.p('If the occurrence of an event does not affect the probability of occurrence of any other event, then they are said to be independent events. With replacement sampling is an example of independent events. Similarly, results of two fair coins or examination results of students are independent of each other.',
    'اگر کسی واقعہ کا وقوع کسی دوسرے واقعہ کے وقوع کے احتمال پر اثر نہ ڈالے تو انہیں آزاد واقعات کہتے ہیں۔ واپسی کے ساتھ (with replacement) نمونہ گیری آزاد واقعات کی مثال ہے۔ اسی طرح دو منصفانہ سکوں کے نتائج یا طلبہ کے امتحانی نتائج ایک دوسرے سے آزاد ہیں۔',
    'که د یوې پېښې رامنځته کېدل د بلې هرې پېښې د رامنځته کېدو پر احتمال اغېز ونه کړي، نو خپلواکې پېښې بلل کېږي. له بېرته اچولو سره (with replacement) نمونه اخیستنه د خپلواکو پېښو بېلګه ده. همداراز د دوو عادلانه سکو پایلې یا د زده کوونکو د ازموینو پایلې له یو بل څخه خپلواکې دي.')
b.h('1.2.4 Definitions of probability', '1.2.4 احتمال کی تعریفیں', '1.2.4 د احتمال تعریفونه')
b.h('The Classical definition of probability', 'احتمال کی کلاسیکی تعریف', 'د احتمال کلاسیک تعریف')
b.p('If a sample space has “n” equally likely and mutually exclusive outcomes and if “m” outcomes of them are favourable to the occurrence of an event “A”, then the probability of the event A, denoted by P(A), is given by',
    'اگر کسی نمونہ فضا میں “n” مساوی امکان والے اور باہم مانع نتائج ہوں اور ان میں سے “m” نتائج واقعہ “A” کے وقوع کے موافق ہوں، تو واقعہ A کا احتمال، جسے P(A) سے ظاہر کرتے ہیں، یہ ہے',
    'که یوه نمونوي فضا “n” مساوي امکان لرونکې او یو بل منع کوونکې پایلې ولري او له هغو څخه “m” پایلې د “A” پېښې د رامنځته کېدو موافقې وي، نو د A پېښې احتمال چې په P(A) ښودل کېږي، دا دی')
b.eq(r'P(A)=\frac{n(A)}{n(S)}=\frac{m}{n}')
b.p('Since events in practical life may not always be equally likely that is why this definition has the shortcoming that it can only be applied to pattern experiments like tossing of a coin, rolling of a die, drawing of a playing card. This definition was given by Laplace. It is also called mathematical or priori definition of probability.',
    'چونکہ عملی زندگی میں واقعات ہمیشہ مساوی امکان والے نہیں ہوتے، اس لیے اس تعریف کی یہ خامی ہے کہ اس کا اطلاق صرف نمونہ دار تجربات جیسے سکہ اچھالنے، پانسہ پھینکنے اور تاش کا پتا نکالنے پر ہو سکتا ہے۔ یہ تعریف لاپلاس نے دی۔ اسے احتمال کی ریاضیاتی یا قبلی (priori) تعریف بھی کہتے ہیں۔',
    'څرنګه چې په عملي ژوند کې پېښې تل مساوي امکان لرونکې نه وي، نو د دې تعریف کمزوري دا ده چې یوازې په نمونوي تجربو لکه د سکې اچول، د ډایس اچول او د لوبې کارت راایستلو کې کارېدای شي. دا تعریف لاپلاس ورکړ. دې ته د احتمال ریاضي یا مخکینی (priori) تعریف هم وایي.')
b.h('The Relative frequency definition of probability', 'احتمال کی اضافی تعدد والی تعریف', 'د احتمال نسبي فریکونسۍ تعریف')
b.p('This definition uses the relative frequency of the occurrence of an event A, over a very large number of trials, that is,',
    'یہ تعریف بہت بڑی تعداد میں آزمائشوں کے دوران واقعہ A کے وقوع کے اضافی تعدد کو استعمال کرتی ہے، یعنی',
    'دا تعریف د ډېرو زیاتو ازمېښتونو په ترڅ کې د A پېښې د رامنځته کېدو نسبي فریکونسي کاروي، یعنې')
b.eq(r'P(A)=\lim_{n\to\infty}\frac{m}{n}')
b.p('This definition, given by Von Mises, has the shortcoming that the experiment needs to be performed a large number of times which is practically time consuming and expensive. It is also called statistical or posteriori definition of probability because it is calculated after conducting the actual experiment.',
    'وان مائزز کی دی ہوئی اس تعریف کی خامی یہ ہے کہ تجربہ بہت زیادہ مرتبہ کرنا پڑتا ہے جو عملاً وقت طلب اور مہنگا ہے۔ اسے احتمال کی شماریاتی یا بعدی (posteriori) تعریف بھی کہتے ہیں کیونکہ یہ اصل تجربہ کرنے کے بعد معلوم کی جاتی ہے۔',
    'د وان مایزس دا تعریف دا کمزوري لري چې تجربه باید ډېر ځله ترسره شي چې عملاً وخت نیوونکې او ګرانه ده. دې ته د احتمال احصاییوي یا وروستنی (posteriori) تعریف هم وایي ځکه چې له اصلي تجربې وروسته محاسبه کېږي.')
b.h('Axiomatic definition of probability', 'احتمال کی مسلّماتی (Axiomatic) تعریف', 'د احتمال اصولي (Axiomatic) تعریف')
b.p('Axiom means a rule or principle that many people accept as true. To avoid different shortcoming and compute probability, Russian mathematician Kolmogorov imposed some axioms on the probability of an event given below:',
    'Axiom (مسلّمہ) سے مراد وہ قاعدہ یا اصول ہے جسے بہت سے لوگ درست مانتے ہیں۔ مختلف خامیوں سے بچنے اور احتمال معلوم کرنے کے لیے روسی ریاضی دان کولموگوروف نے کسی واقعہ کے احتمال پر چند مسلّمات عائد کیے جو نیچے دیے گئے ہیں:',
    'Axiom (اصل) هغه قاعده یا اصل دی چې ډېر خلک یې سم مني. د بېلابېلو کمزوریو د مخنیوي او د احتمال د محاسبې لپاره روسي ریاضي پوه کولموګوروف د یوې پېښې پر احتمال ځینې اصول وضع کړل چې لاندې ورکړل شوي دي:')
b.p('Axiom (I) $\\;0\\le P(E)\\le 1$, where E is any event.', 'مسلّمہ (I) $\\;0\\le P(E)\\le 1$، جہاں E کوئی بھی واقعہ ہے۔', 'اصل (I) $\\;0\\le P(E)\\le 1$، چې E هره پېښه ده.')
rec = b.build('stat12-p008-events-definitions', 'Types of events and definitions of probability', 'واقعات کی اقسام اور احتمال کی تعریفیں', 'د پېښو ډولونه او د احتمال تعریفونه', 8, [7, 8])

if __name__ == '__main__':
    save(8, [(1, rec)])
