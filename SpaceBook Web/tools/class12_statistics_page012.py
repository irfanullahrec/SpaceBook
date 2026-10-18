"""PDF12 printed 15–16: Example 1.13 solution, Example 1.14, 1.3.1 addition law for mutually exclusive events (proof, Venn), Example 1.15 start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import svg_open

SOL = ('Solution:', 'حل:', 'حل:')
disjoint = (svg_open(240, 120, 'Two mutually exclusive events A and B with m1 and m2 cases') +
            '<rect x="50" y="10" width="180" height="100" fill="#bfdbfe" stroke="#1e3a8a" stroke-width="2"/>'
            '<g font-family="Times New Roman,serif" font-size="18" fill="#111" text-anchor="middle"><text x="25" y="68">S =</text>'
            '<text x="110" y="38">A</text><text x="170" y="38">B</text>'
            '<circle cx="110" cy="72" r="22" fill="#e0f2fe" stroke="#111" stroke-width="2"/><circle cx="170" cy="72" r="22" fill="#e0f2fe" stroke="#111" stroke-width="2"/>'
            '<text x="110" y="78" font-size="15" font-style="italic">m₁</text><text x="170" y="78" font-size="15" font-style="italic">m₂</text></g></svg>')

b = Builder()
b.h(*SOL)
b.eq(r'n(S)=2^n=2^5=32')
b.p('Let A: at least one head.', 'فرض کریں A: کم از کم ایک چِت۔', 'فرض کړئ A: لږ تر لږه یو سر.')
b.p('It will be tedious to list the sample space and pick out the favourable results for at least one head. Alternatively,',
    'نمونہ فضا لکھ کر کم از کم ایک چِت کے موافق نتائج چننا دقت طلب ہوگا۔ اس کے بجائے،',
    'د نمونوي فضا لیکل او د لږ تر لږه یو سر لپاره د موافقو پایلو بېلول به ستړی کوونکی وي. پر ځای یې،')
b.p('$\\overline{A}$: No head', '$\\overline{A}$: کوئی چِت نہیں', '$\\overline{A}$: هېڅ سر نه')
b.mlines([r'\overline{A}=(TTTTT)', r'n(\overline{A})=1,', r'P(\overline{A})=\frac{n(\overline{A})}{n(S)}=\frac{1}{32}'])
b.p('Finally, we can obtain the required probability of A by using law of complementation',
    'آخر میں ہم قانونِ تکمیل استعمال کر کے A کا مطلوبہ احتمال حاصل کر سکتے ہیں',
    'په پای کې د بشپړوونې قانون په کارولو سره د A اړین احتمال لاسته راوړلای شو')
b.eq(r'P(A)=1-P(\overline{A})=1-\frac{1}{32}=\frac{31}{32}=0.97')
b.h('Example 1.14', 'مثال 1.14', 'بېلګه 1.14')
b.p('What is the probability that a randomly selected family of four children will have at least one boy?',
    'تصادفی طور پر منتخب کیے گئے چار بچوں والے خاندان میں کم از کم ایک لڑکا ہونے کا احتمال کیا ہے؟',
    'احتمال یې څومره دی چې په تصادفي ډول ټاکل شوې څلور ماشومه کورنۍ کې لږ تر لږه یو هلک وي؟')
b.h(*SOL)
b.eq(r'n(S)=2^4=16')
b.p('Let E: at least one boy in the family', 'فرض کریں E: خاندان میں کم از کم ایک لڑکا', 'فرض کړئ E: په کورنۍ کې لږ تر لږه یو هلک')
b.p('Then $\\overline{E}$ = no boy i.e. all girls', 'تب $\\overline{E}$ = کوئی لڑکا نہیں یعنی سب لڑکیاں', 'بیا $\\overline{E}$ = هېڅ هلک نه یعنې ټولې نجونې')
b.mlines([r'\overline{E}=\{g\,g\,g\,g\}', r'P(\overline{E})=\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{16}'])
b.p('The required probability of E by complementation law is given by', 'قانونِ تکمیل کے ذریعے E کا مطلوبہ احتمال یہ ہے', 'د بشپړوونې د قانون له مخې د E اړین احتمال دا دی')
b.eq(r'P(E)=1-P(\overline{E})=1-\frac{1}{16}=\frac{15}{16}=0.94')
b.h('1.3.1 Addition law of probability for mutually exclusive events', '1.3.1 باہم مانع واقعات کے لیے احتمال کا قانونِ جمع', '1.3.1 د یو بل منع کوونکو پېښو لپاره د احتمال د جمع قانون')
b.h('Statement:', 'بیان:', 'بیان:')
b.p('If A and B are two mutually exclusive events, then the probability that any one of them happens is equal to the sum of individual probabilities of A and B. In symbol, $P(A\\text{ or }B)=P(A\\cup B)=P(A)+P(B)$',
    'اگر A اور B دو باہم مانع واقعات ہوں تو ان میں سے کسی ایک کے واقع ہونے کا احتمال A اور B کے انفرادی احتمالات کے مجموعے کے برابر ہوتا ہے۔ علامتی طور پر $P(A\\text{ or }B)=P(A\\cup B)=P(A)+P(B)$',
    'که A او B دوه یو بل منع کوونکې پېښې وي، نو د هغو څخه د یوې د رامنځته کېدو احتمال د A او B د جلا جلا احتمالونو له مجموعې سره برابر دی. په نښو کې $P(A\\text{ or }B)=P(A\\cup B)=P(A)+P(B)$')
b.h('Proof:', 'ثبوت:', 'ثبوت:')
b.p('Let n be the total number of sample points in the sample space. Let $m_1$ be the favourable cases to the occurrence of an event A, then $P(A)=\\frac{m_1}{n}$. Let $m_2$ be the favourable cases to B, so $P(B)=\\frac{m_2}{n}$. Since A and B are mutually exclusive events, therefore, favourable cases to (A or B) are equal to $m_1+m_2$.',
    'فرض کریں n نمونہ فضا کے نمونہ نقاط کی کل تعداد ہے۔ فرض کریں $m_1$ واقعہ A کے وقوع کے موافق حالات ہیں، تو $P(A)=\\frac{m_1}{n}$۔ فرض کریں $m_2$ واقعہ B کے موافق حالات ہیں، تو $P(B)=\\frac{m_2}{n}$۔ چونکہ A اور B باہم مانع ہیں، اس لیے (A یا B) کے موافق حالات $m_1+m_2$ کے برابر ہیں۔',
    'فرض کړئ n د نمونوي فضا د نمونوي ټکو ټول شمېر دی. فرض کړئ $m_1$ د A پېښې د رامنځته کېدو موافق حالتونه دي، نو $P(A)=\\frac{m_1}{n}$. فرض کړئ $m_2$ د B موافق حالتونه دي، نو $P(B)=\\frac{m_2}{n}$. څرنګه چې A او B یو بل منع کوونکې دي، نو د (A یا B) موافق حالتونه له $m_1+m_2$ سره برابر دي.')
b.visual('stat12-venn-disjoint-m', disjoint, ratio=.35)
b.p('Hence $P(A\\text{ or }B)=P(A\\cup B)=\\frac{m_1+m_2}{n}=\\frac{m_1}{n}+\\frac{m_2}{n}=P(A)+P(B)$',
    'لہٰذا $P(A\\text{ or }B)=P(A\\cup B)=\\frac{m_1+m_2}{n}=\\frac{m_1}{n}+\\frac{m_2}{n}=P(A)+P(B)$',
    'نو $P(A\\text{ or }B)=P(A\\cup B)=\\frac{m_1+m_2}{n}=\\frac{m_1}{n}+\\frac{m_2}{n}=P(A)+P(B)$')
b.h('Example 1.15', 'مثال 1.15', 'بېلګه 1.15')
b.p('A card is drawn from an ordinary deck of playing cards. What is the probability that the card will be either a king or a jack?',
    'تاش کی ایک عام گڈی سے ایک پتا نکالا جاتا ہے۔ احتمال کیا ہے کہ پتا یا تو بادشاہ ہو یا غلام؟',
    'د لوبې د کارتونو له یوې عادي ګډۍ څخه یو کارت راایستل کېږي. احتمال یې څومره دی چې کارت یا باچا وي یا غلام؟')
b.h(*SOL)
b.p('Let the event king be denoted by A and the event jack be denoted by B. These are mutually exclusive events as both cannot occur at a time. Thus we use addition law for mutually exclusive events i.e. $P(A\\text{ or }B)=P(A)+P(B)$',
    'فرض کریں بادشاہ کا واقعہ A اور غلام کا واقعہ B ہے۔ یہ باہم مانع واقعات ہیں کیونکہ دونوں ایک وقت میں واقع نہیں ہو سکتے۔ لہٰذا ہم باہم مانع واقعات کا قانونِ جمع استعمال کرتے ہیں یعنی $P(A\\text{ or }B)=P(A)+P(B)$',
    'فرض کړئ د باچا پېښه په A او د غلام پېښه په B ښودل کېږي. دا یو بل منع کوونکې پېښې دي ځکه چې دواړه په یو وخت نه شي رامنځته کېدای. نو د یو بل منع کوونکو پېښو د جمع قانون کاروو یعنې $P(A\\text{ or }B)=P(A)+P(B)$')
b.p('Now $n(S)={}^{52}_{1}C=52$', 'اب $n(S)={}^{52}_{1}C=52$', 'اوس $n(S)={}^{52}_{1}C=52$')
b.p('Let A: card is king', 'فرض کریں A: پتا بادشاہ ہے', 'فرض کړئ A: کارت باچا دی')
b.mlines([r'n(A)={}^{4}_{1}C=4', r'P(A)=\frac{n(A)}{n(S)}=\frac{4}{52}'])
b.p('Let B: card is a jack', 'فرض کریں B: پتا غلام ہے', 'فرض کړئ B: کارت غلام دی')
b.eq(r'n(B)={}^{4}_{1}C=4')
rec = b.build('stat12-p012-addition-exclusive', 'Examples 1.13–1.15 and 1.3.1 addition law (mutually exclusive)', 'مثالیں 1.13–1.15 اور 1.3.1 قانونِ جمع (باہم مانع)', 'بېلګې 1.13–1.15 او 1.3.1 د جمع قانون (یو بل منع کوونکې)', 12, [15, 16])

if __name__ == '__main__':
    save(12, [(1, rec)])
