"""PDF13 printed 17–18: Example 1.15 end, Example 1.16 (sum 6 or 9), 1.3.2 addition law for not-mutually exclusive events (proof, Venn), Example 1.17 start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import DICE36, venn_regions

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'P(B)=\frac{n(B)}{n(S)}=\frac{4}{52}', r'\therefore P(A\text{ or }B)=P(A)+P(B)', r'\phantom{\therefore P(A\text{ or }B)}=\frac{4}{52}+\frac{4}{52}=\frac{8}{52}=\frac{2}{13}'])
b.h('Example 1.16', 'مثال 1.16', 'بېلګه 1.16')
b.p('A pair of fair dice is rolled once. Find the probability that the sum of the upper dots is either 6 or 9.',
    'منصفانہ پانسوں کا ایک جوڑا ایک بار پھینکا جاتا ہے۔ اوپر والے نقطوں کا مجموعہ 6 یا 9 ہونے کا احتمال معلوم کریں۔',
    'د عادلانه ډایسونو یوه جوړه یو ځل اچول کېږي. احتمال یې پیدا کړئ چې د پورتنیو ټکو مجموعه یا 6 وي یا 9.')
b.h(*SOL)
b.p('Let A: Sum of dots is 6 and B: sum of dots is 9. The events are mutually exclusive because they cannot occur together. Hence we use addition rule for mutually exclusive events i.e. $P(A\\text{ or }B)=P(A)+P(B)$',
    'فرض کریں A: نقطوں کا مجموعہ 6 ہے اور B: نقطوں کا مجموعہ 9 ہے۔ یہ واقعات باہم مانع ہیں کیونکہ اکٹھے واقع نہیں ہو سکتے۔ لہٰذا ہم باہم مانع واقعات کا قاعدۂ جمع استعمال کرتے ہیں یعنی $P(A\\text{ or }B)=P(A)+P(B)$',
    'فرض کړئ A: د ټکو مجموعه 6 ده او B: د ټکو مجموعه 9 ده. دا پېښې یو بل منع کوونکې دي ځکه چې یوځای نه شي رامنځته کېدای. نو د یو بل منع کوونکو پېښو د جمع قاعده کاروو یعنې $P(A\\text{ or }B)=P(A)+P(B)$')
b.mlines([r'\text{Now } n(S)=6^2=36', DICE36])
b.mlines([r'\therefore A=\{(1,5),(2,4),(3,3),(4,2),(5,1)\}', r'n(A)=5,', r'P(A)=\frac{n(A)}{n(S)}=\frac{5}{36}',
          r'B=\{(3,6),(4,5),(5,4),(6,3)\}', r'n(B)=4,', r'P(B)=\frac{n(B)}{n(S)}=\frac{4}{36}',
          r'\therefore P(A\text{ or }B)=P(A\cup B)=\frac{5}{36}+\frac{4}{36}=\frac{9}{36}=\frac{1}{4}.'])
b.h('1.3.2 Addition law of probability for not-mutually exclusive events', '1.3.2 غیر باہم مانع واقعات کے لیے احتمال کا قانونِ جمع', '1.3.2 د نه یو بل منع کوونکو پېښو لپاره د احتمال د جمع قانون')
b.h('Statement:', 'بیان:', 'بیان:')
b.p('If A and B are two not-mutually exclusive events, then the probability that at least one of the two events A and B occurs is equal to the probability that A occurs plus the probability that B occurs minus the probability that both events A and B occur together. In symbol, $P(A\\text{ or }B)=P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$',
    'اگر A اور B دو غیر باہم مانع واقعات ہوں، تو دونوں واقعات A اور B میں سے کم از کم ایک کے واقع ہونے کا احتمال، A کے واقع ہونے کے احتمال جمع B کے واقع ہونے کے احتمال تفریق دونوں واقعات A اور B کے اکٹھے واقع ہونے کے احتمال کے برابر ہے۔ علامتی طور پر $P(A\\text{ or }B)=P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$',
    'که A او B دوه نه یو بل منع کوونکې پېښې وي، نو د A او B له دوو پېښو څخه د لږ تر لږه یوې د رامنځته کېدو احتمال د A د رامنځته کېدو له احتمال جمع د B د رامنځته کېدو احتمال منفي د A او B دواړو د یوځای رامنځته کېدو له احتمال سره برابر دی. په نښو کې $P(A\\text{ or }B)=P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$')
b.h('Proof:', 'ثبوت:', 'ثبوت:')
b.p('From the Venn diagram we see that', 'وین خاکے سے ہم دیکھتے ہیں کہ', 'د وېن له ډیاګرام څخه وینو چې')
b.visual('stat12-venn-regions', venn_regions(), ratio=.45)
b.mlines([r'A\cup B=\{A\cup(\overline{A}\cap B)\}', r'P(A\cup B)=P\{A\cup(\overline{A}\cap B)\}'])
b.p('$\\phantom{P(A\\cup B)}=P(A)+P(\\overline{A}\\cap B)$, as A and $(\\overline{A}\\cap B)$ are mutually exclusive ……(i)',
    '$\\phantom{P(A\\cup B)}=P(A)+P(\\overline{A}\\cap B)$، کیونکہ A اور $(\\overline{A}\\cap B)$ باہم مانع ہیں ……(i)',
    '$\\phantom{P(A\\cup B)}=P(A)+P(\\overline{A}\\cap B)$، ځکه چې A او $(\\overline{A}\\cap B)$ یو بل منع کوونکې دي ……(i)')
b.p('Again see the diagram, the set B is given by', 'دوبارہ خاکہ دیکھیں، سیٹ B یوں ہے', 'بیا ډیاګرام ته وګورئ، B ټولګه داسې ده')
b.mlines([r'B=(A\cap B)\cup(\overline{A}\cap B)', r'P(B)=P[(A\cap B)\cup(\overline{A}\cap B)]'])
b.p('$\\phantom{P(B)}=P(A\\cap B)+P(\\overline{A}\\cap B)$ (as $(A\\cap B)$ and $(\\overline{A}\\cap B)$ are mutually exclusive events)',
    '$\\phantom{P(B)}=P(A\\cap B)+P(\\overline{A}\\cap B)$ (کیونکہ $(A\\cap B)$ اور $(\\overline{A}\\cap B)$ باہم مانع واقعات ہیں)',
    '$\\phantom{P(B)}=P(A\\cap B)+P(\\overline{A}\\cap B)$ (ځکه چې $(A\\cap B)$ او $(\\overline{A}\\cap B)$ یو بل منع کوونکې پېښې دي)')
b.p('or $P(\\overline{A}\\cap B)=P(B)-P(A\\cap B)$, put in equation (i) we get,', 'یا $P(\\overline{A}\\cap B)=P(B)-P(A\\cap B)$، مساوات (i) میں رکھنے سے',
    'یا $P(\\overline{A}\\cap B)=P(B)-P(A\\cap B)$، په (i) معادله کې یې ایښودو سره')
b.eq(r'P(A\cup B)=P(A)+P(B)-P(A\cap B).')
b.h('Example 1.17', 'مثال 1.17', 'بېلګه 1.17')
b.p('A fair die is thrown once. What is the chance that either an even number or a number greater than 3 will turn up?',
    'ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ جفت عدد یا 3 سے بڑا عدد آنے کا امکان کیا ہے؟',
    'یو عادلانه ډایس یو ځل اچول کېږي. د جفت عدد یا له 3 څخه د لوی عدد د راتلو چانس څومره دی؟')
b.h(*SOL)
b.p('Let A: an even number occur and B: a number greater than 3 occurs. The events are not mutually exclusive because A may happen, B may happen or both A and B happen. So we use addition law for not-mutually exclusive events:',
    'فرض کریں A: جفت عدد آتا ہے اور B: 3 سے بڑا عدد آتا ہے۔ یہ واقعات باہم مانع نہیں کیونکہ A ہو سکتا ہے، B ہو سکتا ہے یا A اور B دونوں ہو سکتے ہیں۔ لہٰذا ہم غیر باہم مانع واقعات کا قانونِ جمع استعمال کرتے ہیں:',
    'فرض کړئ A: جفت عدد راځي او B: له 3 څخه لوی عدد راځي. دا پېښې یو بل منع کوونکې نه دي ځکه چې A کېدای شي، B کېدای شي یا A او B دواړه کېدای شي. نو د نه یو بل منع کوونکو پېښو د جمع قانون کاروو:')
b.eq(r'P(A\text{ or }B)=P(A)+P(B)-P(A\cap B)')
rec = b.build('stat12-p013-addition-general', 'Examples 1.15–1.17 and 1.3.2 addition law (not mutually exclusive)', 'مثالیں 1.15–1.17 اور 1.3.2 قانونِ جمع (غیر باہم مانع)', 'بېلګې 1.15–1.17 او 1.3.2 د جمع قانون (نه یو بل منع کوونکې)', 13, [17, 18])

if __name__ == '__main__':
    save(13, [(1, rec)])
