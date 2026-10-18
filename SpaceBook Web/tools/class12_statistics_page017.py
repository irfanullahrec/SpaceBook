"""PDF17 printed 25–26: Example 1.23 parts (b)–(c); Unit 1 Key points."""
from class12_statistics_common import Builder, save

b = Builder()
b.mlines([r'(b)\quad p=\frac{{}^{26}_{1}C}{{}^{52}_{1}C}=\frac{26}{52}', r'd=\frac{p}{1-p}=\frac{26/52}{1-26/52}=\frac{26/52}{26/52}=1',
          r'(c)\quad p=\frac{{}^{4}_{1}C}{{}^{52}_{1}C}=\frac{4}{52}', r'd=\frac{p}{1-p}', r'\phantom{d}=\frac{4/52}{1-4/52}=\frac{4/52}{48/52}=\frac{4}{48}', r'\Rightarrow 1:12'])
ex = b.build('stat12-p017-odds-example', 'Example 1.23 — parts (b) and (c)', 'مثال 1.23 — حصے (b) اور (c)', 'بېلګه 1.23 — برخې (b) او (c)', 17, [25])

k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.group('list', [
    ('Remember that the quantity $0!=1$ arbitrarily defined and $1!=1$', 'یاد رکھیں کہ مقدار $0!=1$ اختیاری طور پر متعین ہے اور $1!=1$', 'په یاد ولرئ چې کمیت $0!=1$ په اختیاري ډول تعریف شوی او $1!=1$'),
    ('${}^{n}_{r}C=\\frac{n!}{(n-r)!\\,r!}$',) * 3,
    ('An experiment whose results cannot be predicted in advance is called random experiment', 'وہ تجربہ جس کے نتائج کی پہلے سے پیش گوئی نہ کی جا سکے، تصادفی تجربہ کہلاتا ہے', 'هغه تجربه چې پایلې یې مخکې له مخکې وړاندوینه نه شي کېدای، تصادفي تجربه بلل کېږي'),
    ('The collection of all possible results of a random experiment is called sample space', 'کسی تصادفی تجربے کے تمام ممکنہ نتائج کے مجموعے کو نمونہ فضا کہتے ہیں', 'د یوې تصادفي تجربې د ټولو شونو پایلو ټولګې ته نمونوي فضا وایي'),
    ('The collection of favourable outcomes to a happening from the sample space is called an event.', 'نمونہ فضا میں سے کسی واقعے کے موافق نتائج کے مجموعے کو واقعہ کہتے ہیں۔', 'له نمونوي فضا څخه د یوې پېښې د موافقو پایلو ټولګې ته پېښه وایي.'),
    ('If two events cannot occur together, then they are called mutually exclusive events.', 'اگر دو واقعات اکٹھے واقع نہ ہو سکیں تو انہیں باہم مانع واقعات کہتے ہیں۔', 'که دوه پېښې یوځای رامنځته نه شي، نو یو بل منع کوونکې پېښې بلل کېږي.'),
    ('If the occurrence of an event affects the probability of occurrence of another event they are called dependent events.', 'اگر ایک واقعہ کا وقوع دوسرے واقعہ کے وقوع کے احتمال پر اثر ڈالے تو انہیں تابع واقعات کہتے ہیں۔', 'که د یوې پېښې رامنځته کېدل د بلې پېښې د رامنځته کېدو پر احتمال اغېز وکړي، تړلې پېښې بلل کېږي.'),
    ('If the occurrence of an event does not affect the probability of occurrence of any other event, they are said to be independent events.', 'اگر کسی واقعہ کا وقوع کسی دوسرے واقعہ کے وقوع کے احتمال پر اثر نہ ڈالے تو انہیں آزاد واقعات کہتے ہیں۔', 'که د یوې پېښې رامنځته کېدل د بلې هرې پېښې د رامنځته کېدو پر احتمال اغېز ونه کړي، خپلواکې پېښې بلل کېږي.'),
    ('$P(A)=\\frac{n(A)}{n(S)}=\\frac{m}{n}$',) * 3,
    ('$0\\le P(E)\\le 1$, where E is any event.', '$0\\le P(E)\\le 1$، جہاں E کوئی بھی واقعہ ہے۔', '$0\\le P(E)\\le 1$، چې E هره پېښه ده.'),
    ('If $\\overline{A}$ is the complement of an event A in the sample space then $P(\\overline{A})=1-P(A)$', 'اگر نمونہ فضا میں $\\overline{A}$ واقعہ A کا تکملہ ہو تو $P(\\overline{A})=1-P(A)$', 'که په نمونوي فضا کې $\\overline{A}$ د A پېښې بشپړوونکې وي، نو $P(\\overline{A})=1-P(A)$'),
    ('$P(A\\text{ or }B)=P(A)+P(B)$ if A and B are mutually exclusive events.', '$P(A\\text{ or }B)=P(A)+P(B)$ اگر A اور B باہم مانع واقعات ہوں۔', '$P(A\\text{ or }B)=P(A)+P(B)$ که A او B یو بل منع کوونکې پېښې وي.'),
    ('$P(A\\text{ or }B)=P(A)+P(B)-P(A\\cap B)$, if A and B are not-mutually exclusive events.', '$P(A\\text{ or }B)=P(A)+P(B)-P(A\\cap B)$، اگر A اور B غیر باہم مانع واقعات ہوں۔', '$P(A\\text{ or }B)=P(A)+P(B)-P(A\\cap B)$، که A او B نه یو بل منع کوونکې پېښې وي.'),
    ('$P(A\\text{ and }B)=P(A\\cap B)=P(A)\\,P(B)$, if A and B are independent', '$P(A\\text{ and }B)=P(A\\cap B)=P(A)\\,P(B)$، اگر A اور B آزاد ہوں', '$P(A\\text{ and }B)=P(A\\cap B)=P(A)\\,P(B)$، که A او B خپلواکې وي'),
    ('$P(A/B)=\\frac{P(A\\cap B)}{P(B)}$, If A and B are dependent.', '$P(A/B)=\\frac{P(A\\cap B)}{P(B)}$، اگر A اور B تابع ہوں۔', '$P(A/B)=\\frac{P(A\\cap B)}{P(B)}$، که A او B تړلې وي.'),
])
keys = k.build('stat12-u1-key-points', 'Unit 1 — Key points', 'یونٹ 1 — اہم نکات', 'واحد 1 — مهم ټکي', 17, [26])

if __name__ == '__main__':
    save(17, [(1, ex), (1, keys)])
