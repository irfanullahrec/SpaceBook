"""PDF14 printed 19–20: Example 1.17 solution, Example 1.18 (Ahsan), 1.3.3 multiplication law for independent events, Example 1.19 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'\text{Now } n(S)=6^n=6^1=6', r'S=\{1,2,3,4,5,6\}'])
b.p('Let A: an even number occurs', 'فرض کریں A: جفت عدد آتا ہے', 'فرض کړئ A: جفت عدد راځي')
b.mlines([r'A=\{2,4,6\}', r'n(A)=3,\quad P(A)=\frac{n(A)}{n(S)}=\frac{3}{6}'])
b.p('Let B: number is greater than 3', 'فرض کریں B: عدد 3 سے بڑا ہے', 'فرض کړئ B: عدد له 3 څخه لوی دی')
b.mlines([r'B=\{4,5,6\}', r'n(B)=3,\quad P(B)=\frac{n(B)}{n(S)}=\frac{3}{6}', r'A\cap B=\{4,6\}',
          r'n(A\cap B)=2,\quad P(A\cap B)=\frac{n(A\cap B)}{n(S)}=\frac{2}{6}',
          r'\text{Hence } P(A\text{ or }B)=\frac{3}{6}+\frac{3}{6}-\frac{2}{6}=\frac{3+3-2}{6}=\frac{4}{6}=\frac{2}{3}'])
b.h('Example 1.18', 'مثال 1.18', 'بېلګه 1.18')
b.p('Ahsan appeared in the annual examination. The probability that he will pass (i) Mathematics is 0.60 (ii) Statistics is 0.50 and (iii) both Mathematics and Statistics is 0.30. What is the probability that Ahsan will pass either Mathematics or Statistics?',
    'احسن نے سالانہ امتحان دیا۔ اس کے (i) ریاضی میں پاس ہونے کا احتمال 0.60 (ii) شماریات میں 0.50 اور (iii) ریاضی اور شماریات دونوں میں 0.30 ہے۔ احسن کے ریاضی یا شماریات میں پاس ہونے کا احتمال کیا ہے؟',
    'احسن په کلنۍ ازموینه کې ګډون وکړ. د هغه د بریالیتوب احتمال (i) په ریاضي کې 0.60 (ii) په احصایه کې 0.50 او (iii) په ریاضي او احصایه دواړو کې 0.30 دی. احتمال یې څومره دی چې احسن به یا په ریاضي یا په احصایه کې بریالی شي؟')
b.h(*SOL)
b.p('Let M: Ahsan will pass Mathematics, S: Ahsan will pass Statistics', 'فرض کریں M: احسن ریاضی میں پاس ہوگا، S: احسن شماریات میں پاس ہوگا', 'فرض کړئ M: احسن به په ریاضي کې بریالی شي، S: احسن به په احصایه کې بریالی شي')
b.p('Here the events are not mutually exclusive as Ahsan may pass Mathematics or Statistics or both. So we use addition law for not-mutually exclusive events.',
    'یہاں واقعات باہم مانع نہیں کیونکہ احسن ریاضی یا شماریات یا دونوں میں پاس ہو سکتا ہے۔ لہٰذا ہم غیر باہم مانع واقعات کا قانونِ جمع استعمال کرتے ہیں۔',
    'دلته پېښې یو بل منع کوونکې نه دي ځکه چې احسن کېدای شي په ریاضي یا احصایه یا دواړو کې بریالی شي. نو د نه یو بل منع کوونکو پېښو د جمع قانون کاروو.')
b.mlines([r'\text{Given that } P(M)=0.60', r'P(S)=0.50', r'P(M\cap S)=0.30', r'\therefore P(M\text{ or }S)=P(M)+P(S)-P(M\cap S)', r'\phantom{\therefore P(M\text{ or }S)}=0.60+0.5-0.30=0.80'])
b.h('1.3.3 Multiplication law for independent events', '1.3.3 آزاد واقعات کے لیے قانونِ ضرب', '1.3.3 د خپلواکو پېښو لپاره د ضرب قانون')
b.h('Statement:', 'بیان:', 'بیان:')
b.p('If A and B are two independent events, then the probability of their simultaneous happening is equal to the product of their separate probabilities. Symbolically, $P(A\\text{ and }B)=P(A\\cap B)=P(A)\\,P(B)$',
    'اگر A اور B دو آزاد واقعات ہوں تو ان کے بیک وقت واقع ہونے کا احتمال ان کے الگ الگ احتمالات کے حاصلِ ضرب کے برابر ہے۔ علامتی طور پر $P(A\\text{ and }B)=P(A\\cap B)=P(A)\\,P(B)$',
    'که A او B دوه خپلواکې پېښې وي، نو د هغو د یو وخت رامنځته کېدو احتمال د هغو د جلا جلا احتمالونو له ضرب حاصل سره برابر دی. په نښو کې $P(A\\text{ and }B)=P(A\\cap B)=P(A)\\,P(B)$')
b.h('Proof:', 'ثبوت:', 'ثبوت:')
b.p('Let “m” and “n” be the favourable and possible outcomes respectively for an event “A”, then $P(A)=\\frac{m}{n}$.',
    'فرض کریں “m” اور “n” واقعہ “A” کے بالترتیب موافق اور ممکنہ نتائج ہیں، تو $P(A)=\\frac{m}{n}$۔',
    'فرض کړئ “m” او “n” په ترتیب سره د “A” پېښې موافقې او شونې پایلې دي، نو $P(A)=\\frac{m}{n}$.')
b.p('Let M and N be the favourable and possible outcomes respectively for an event “B”, then $P(B)=\\frac{M}{N}$.',
    'فرض کریں M اور N واقعہ “B” کے بالترتیب موافق اور ممکنہ نتائج ہیں، تو $P(B)=\\frac{M}{N}$۔',
    'فرض کړئ M او N په ترتیب سره د “B” پېښې موافقې او شونې پایلې دي، نو $P(B)=\\frac{M}{N}$.')
b.p('Since A and B are independent events, therefore, mM, nN be the favourable and possible outcomes respectively for event (A and B). Thus,',
    'چونکہ A اور B آزاد واقعات ہیں، اس لیے mM اور nN واقعہ (A اور B) کے بالترتیب موافق اور ممکنہ نتائج ہیں۔ چنانچہ،',
    'څرنګه چې A او B خپلواکې پېښې دي، نو mM او nN په ترتیب سره د (A او B) پېښې موافقې او شونې پایلې دي. نو،')
b.eq(r'P(A\text{ and }B)=P(A\cap B)=\frac{mM}{nN}=\frac{m}{n}\cdot\frac{M}{N}=P(A)\,P(B)')
b.h('Example 1.19', 'مثال 1.19', 'بېلګه 1.19')
b.p('Suppose that a bag contains 10 balls of which 4 are red balls and 6 are green balls. Find the probability of drawing two green balls in succession if the ball that is drawn first is replaced.',
    'فرض کریں ایک تھیلے میں 10 گیندیں ہیں جن میں 4 سرخ اور 6 سبز ہیں۔ اگر پہلی نکالی گئی گیند واپس رکھ دی جائے تو یکے بعد دیگرے دو سبز گیندیں نکالنے کا احتمال معلوم کریں۔',
    'فرض کړئ په یوه کڅوړه کې 10 توپونه دي چې 4 یې سره او 6 یې شنه دي. که لومړی راایستل شوی توپ بېرته واچول شي، نو په پرله پسې ډول د دوو شنو توپونو د راایستلو احتمال پیدا کړئ.')
b.h(*SOL)
b.p('Let A: first ball drawn is green, B: second ball drawn is green. The events are independent because the ball drawn first is replaced before the next draw, so probability of both green balls will remain the same.',
    'فرض کریں A: پہلی نکالی گئی گیند سبز ہے، B: دوسری نکالی گئی گیند سبز ہے۔ واقعات آزاد ہیں کیونکہ پہلی گیند اگلی بار نکالنے سے پہلے واپس رکھ دی جاتی ہے، اس لیے دونوں سبز گیندوں کا احتمال یکساں رہے گا۔',
    'فرض کړئ A: لومړی راایستل شوی توپ شین دی، B: دویم راایستل شوی توپ شین دی. پېښې خپلواکې دي ځکه چې لومړی توپ د بل ځل له راایستلو مخکې بېرته اچول کېږي، نو د دواړو شنو توپونو احتمال به یو شان پاتې وي.')
b.p('The bag contains $(4R+6G)=10$ balls', 'تھیلے میں $(4R+6G)=10$ گیندیں ہیں', 'په کڅوړه کې $(4R+6G)=10$ توپونه دي')
b.eq(r'P(A)=\frac{{}^{6}_{1}C}{{}^{10}_{1}C}=\frac{6}{10}')
rec = b.build('stat12-p014-multiplication-independent', 'Examples 1.17–1.19 and 1.3.3 multiplication law (independent events)', 'مثالیں 1.17–1.19 اور 1.3.3 قانونِ ضرب (آزاد واقعات)', 'بېلګې 1.17–1.19 او 1.3.3 د ضرب قانون (خپلواکې پېښې)', 14, [19, 20])

if __name__ == '__main__':
    save(14, [(1, rec)])
