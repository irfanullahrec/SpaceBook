"""PDF16 printed 23–24: Example 1.21 solution, Example 1.22, 1.3.6 odds for the occurrence of an event, Example 1.23 start."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h(*SOL)
b.p('Let A: first ball is green, B: second ball is green', 'فرض کریں A: پہلی گیند سبز ہے، B: دوسری گیند سبز ہے', 'فرض کړئ A: لومړی توپ شین دی، B: دویم توپ شین دی')
b.p('Since the first ball drawn is not replaced, therefore, the events are dependent and so we use multiplication law of probability for dependent events i.e. $P(A\\text{ and }B)=P(A)\\,P(B/A)$',
    'چونکہ پہلی نکالی گئی گیند واپس نہیں رکھی جاتی، اس لیے واقعات تابع ہیں اور ہم تابع واقعات کے لیے احتمال کا قانونِ ضرب استعمال کرتے ہیں یعنی $P(A\\text{ and }B)=P(A)\\,P(B/A)$',
    'څرنګه چې لومړی راایستل شوی توپ بېرته نه اچول کېږي، نو پېښې تړلې دي او د تړلو پېښو لپاره د احتمال د ضرب قانون کاروو یعنې $P(A\\text{ and }B)=P(A)\\,P(B/A)$')
b.p('The bag contains $(3W+7G)=10$ balls', 'تھیلے میں $(3W+7G)=10$ گیندیں ہیں', 'په کڅوړه کې $(3W+7G)=10$ توپونه دي')
b.eq(r'P(A)=\frac{{}^{7}_{1}C}{{}^{10}_{1}C}=\frac{7}{10}')
b.p('Since green ball drawn is not replaced, so new position of the bag is $(3W+6G)=9$ balls, so',
    'چونکہ نکالی گئی سبز گیند واپس نہیں رکھی گئی، اس لیے تھیلے کی نئی حالت $(3W+6G)=9$ گیندیں ہے، لہٰذا',
    'څرنګه چې راایستل شوی شین توپ بېرته نه دی اچول شوی، نو د کڅوړې نوی حالت $(3W+6G)=9$ توپونه دي، نو')
b.mlines([r'P(B/A)=\frac{{}^{6}_{1}C}{{}^{9}_{1}C}=\frac{6}{9}',
          r'\text{Hence } P(A\text{ and }B)=P(A\cap B)=P(A)\,P(B/A)=\frac{7}{10}\times\frac{6}{9}=\frac{42}{90}=\frac{7}{15}'])
b.h('Example 1.22', 'مثال 1.22', 'بېلګه 1.22')
b.p('If $P(A)=0.60$, $P(B)=0.40$, $P(A\\cap B)=0.24$. (i) What is the relation between A and B? Also find (ii) $P(\\overline{A})$ (iii) $P(A\\cup B)$ (iv) $P(A/B)$.',
    'اگر $P(A)=0.60$، $P(B)=0.40$، $P(A\\cap B)=0.24$ ہو۔ (i) A اور B کے درمیان کیا تعلق ہے؟ نیز معلوم کریں (ii) $P(\\overline{A})$ (iii) $P(A\\cup B)$ (iv) $P(A/B)$۔',
    'که $P(A)=0.60$، $P(B)=0.40$، $P(A\\cap B)=0.24$ وي. (i) د A او B ترمنځ اړیکه څه ده؟ همداراز پیدا کړئ (ii) $P(\\overline{A})$ (iii) $P(A\\cup B)$ (iv) $P(A/B)$.')
b.h(*SOL)
b.p('(i) Here $P(A)\\,P(B)=(0.60)(0.40)=0.24=P(A\\cap B)$. Multiplication law for independent events is satisfied. Thus, A and B are independent events.',
    '(i) یہاں $P(A)\\,P(B)=(0.60)(0.40)=0.24=P(A\\cap B)$۔ آزاد واقعات کا قانونِ ضرب پورا ہوتا ہے۔ لہٰذا A اور B آزاد واقعات ہیں۔',
    '(i) دلته $P(A)\\,P(B)=(0.60)(0.40)=0.24=P(A\\cap B)$. د خپلواکو پېښو د ضرب قانون پوره کېږي. نو A او B خپلواکې پېښې دي.')
b.p('(ii) By complementation law', '(ii) قانونِ تکمیل کے ذریعے', '(ii) د بشپړوونې د قانون له مخې')
b.eq(r'P(\overline{A})=1-P(A)=1-0.60=0.40')
b.mlines([r'(iii)\quad P(A\cup B)=P(A)+P(B)-P(A\cap B)', r'\phantom{(iii)\quad P(A\cup B)}=0.60+0.40-0.24=0.76',
          r'(iii)\quad P(A/B)=\frac{P(A\cap B)}{P(B)}=\frac{0.24}{0.40}=0.60=P(A)'])
b.p('(This statement also shows that events A and B are independent).', '(یہ بیان بھی ظاہر کرتا ہے کہ واقعات A اور B آزاد ہیں)۔', '(دا بیان هم ښيي چې A او B پېښې خپلواکې دي).')
b.h('1.3.6 Odds for the occurrence of an event', '1.3.6 کسی واقعہ کے وقوع کے حق میں امکان (Odds)', '1.3.6 د یوې پېښې د رامنځته کېدو په ګټه چانس (Odds)')
b.p('The term “odds” refers to the ratio of two probabilities; the ratio of probability of success to the probability of failure. Any kind of probability can be expressed as odds, defined as $d=\\frac{p}{1-p}$ where d = odds and p = Probability of success. For example; in throwing a die the probability of 3 is one in six that is $p=\\frac{1}{6}$. The odds of getting a 3 are $d=\\frac{p}{1-p}=\\frac{1/6}{1-1/6}=\\frac{1/6}{5/6}=\\frac{1}{5}$. That is, odds for 3 are 1 to 5. Odds are used by researchers in different fields.',
    'اصطلاح “odds” دو احتمالات کی نسبت کو کہتے ہیں؛ یعنی کامیابی کے احتمال اور ناکامی کے احتمال کی نسبت۔ کسی بھی احتمال کو odds کی صورت میں ظاہر کیا جا سکتا ہے، جس کی تعریف $d=\\frac{p}{1-p}$ ہے جہاں d = odds اور p = کامیابی کا احتمال۔ مثلاً پانسہ پھینکنے میں 3 آنے کا احتمال چھ میں ایک ہے یعنی $p=\\frac{1}{6}$۔ 3 آنے کے odds یہ ہیں $d=\\frac{p}{1-p}=\\frac{1/6}{1-1/6}=\\frac{1/6}{5/6}=\\frac{1}{5}$۔ یعنی 3 کے حق میں odds ‏1 بمقابلہ 5 ہیں۔ odds مختلف شعبوں میں محققین استعمال کرتے ہیں۔',
    'د “odds” اصطلاح د دوو احتمالونو نسبت ته وایي؛ یعنې د بریا د احتمال او د ناکامۍ د احتمال نسبت. هر ډول احتمال د odds په بڼه ښودل کېدای شي چې تعریف یې $d=\\frac{p}{1-p}$ دی چې d = odds او p = د بریا احتمال. د بېلګې په توګه د ډایس په اچولو کې د 3 احتمال له شپږو یو دی یعنې $p=\\frac{1}{6}$. د 3 د راتلو odds دا دي $d=\\frac{p}{1-p}=\\frac{1/6}{1-1/6}=\\frac{1/6}{5/6}=\\frac{1}{5}$. یعنې د 3 په ګټه odds له 5 سره 1 دي. څېړونکي odds په بېلابېلو برخو کې کاروي.')
b.h('Example 1.23', 'مثال 1.23', 'بېلګه 1.23')
b.p('A card is drawn from a deck of 52 cards. Find (i) the probability and (ii) the odds that the card drawn will be (a) a diamond? (b) a red card? (c) a king?',
    '52 پتوں کی گڈی سے ایک پتا نکالا جاتا ہے۔ معلوم کریں (i) احتمال اور (ii) odds کہ نکالا گیا پتا (a) اینٹ (ڈائمنڈ) ہو؟ (b) سرخ پتا ہو؟ (c) بادشاہ ہو؟',
    'د 52 کارتونو له ګډۍ څخه یو کارت راایستل کېږي. پیدا کړئ (i) احتمال او (ii) odds چې راایستل شوی کارت به (a) ډایمنډ وي؟ (b) سور کارت وي؟ (c) باچا وي؟')
b.h(*SOL)
b.eq(r'n(S)={}^{52}_{1}C=52')
b.mlines([r'(a)\quad p=\frac{{}^{13}_{1}C}{{}^{52}_{1}C}=\frac{13}{52}', r'd=\frac{p}{1-p}=\frac{13/52}{1-13/52}=\frac{13/52}{39/52}=\frac{13}{39}', r'\Rightarrow 13:39\text{ or }1:3'])
rec = b.build('stat12-p016-odds', 'Examples 1.21–1.23 and 1.3.6 odds', 'مثالیں 1.21–1.23 اور 1.3.6 امکانات (Odds)', 'بېلګې 1.21–1.23 او 1.3.6 چانسونه (Odds)', 16, [23, 24])
issues = [{'id': 'stat12-p24-part-label', 'unit': 1, 'printedPage': 24, 'description': 'Example 1.22 solution labels the P(A/B) part “(iii)” although the question numbers it (iv); printed label retained.'}]

if __name__ == '__main__':
    save(16, [(1, rec)], issues=issues)
