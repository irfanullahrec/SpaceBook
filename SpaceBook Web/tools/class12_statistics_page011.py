"""PDF11 printed 13–14: Example 1.11 solution, Example 1.12 (mobile sets), 1.3 complementation law with Venn diagram, Example 1.13 question."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import venn_complement

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h(*SOL)
b.p('The bag contains $(5W+4R+3B)=12$ balls', 'تھیلے میں $(5W+4R+3B)=12$ گیندیں ہیں', 'په کڅوړه کې $(5W+4R+3B)=12$ توپونه دي')
b.mlines([r'n(S)={}^{12}_{2}C=\frac{12!}{(12-2)!\,2!}', r'\phantom{n(S)}=\frac{12\cdot 11\cdot 10!}{10!\,2\cdot 1}=66'])
b.p('(i) Let A: 2 balls drawn are red', '(i) فرض کریں A: نکالی گئی 2 گیندیں سرخ ہیں', '(i) فرض کړئ A: راایستل شوي 2 توپونه سره دي')
b.mlines([r'n(A)={}^{4}_{2}C=6,', r'P(A)=\frac{n(A)}{n(S)}=\frac{6}{66}=\frac{1}{11}'])
b.p('(ii) Let B: one white ball and one black ball', '(ii) فرض کریں B: ایک سفید اور ایک سیاہ گیند', '(ii) فرض کړئ B: یو سپین او یو تور توپ')
b.mlines([r'n(B)={}^{5}_{1}C\times{}^{3}_{1}C=5\times 3=15', r'P(B)=\frac{n(B)}{n(S)}=\frac{15}{66}=\frac{5}{22}'])
b.h('Example 1.12', 'مثال 1.12', 'بېلګه 1.12')
b.p('A retailer wishes to buy two mobile sets from a shop having only 10 Samsung and 5 i-Phone mobiles sets. Find the probability that he will buy (i) two Samsung sets (ii) at least one Samsung set (iii) one Samsung and one i-Phone.',
    'ایک خوردہ فروش ایسی دکان سے دو موبائل سیٹ خریدنا چاہتا ہے جس میں صرف 10 سام سنگ اور 5 آئی فون سیٹ ہیں۔ احتمال معلوم کریں کہ وہ (i) دو سام سنگ سیٹ (ii) کم از کم ایک سام سنگ سیٹ (iii) ایک سام سنگ اور ایک آئی فون خریدے گا۔',
    'یو پرچون پلورونکی غواړي له داسې دوکان څخه دوه موبایلونه واخلي چې یوازې 10 سامسنګ او 5 آی فون موبایلونه لري. احتمال یې پیدا کړئ چې هغه به (i) دوه سامسنګ (ii) لږ تر لږه یو سامسنګ (iii) یو سامسنګ او یو آی فون واخلي.')
b.h(*SOL)
b.p('There are (10 Samsung + 5 i-Phone) = 15 sets', '(10 سام سنگ + 5 آئی فون) = 15 سیٹ ہیں', '(10 سامسنګ + 5 آی فون) = 15 موبایلونه دي')
b.eq(r'n(S)={}^{15}_{2}C=105')
b.p('(i) Let A: 2 Samsung sets', '(i) فرض کریں A: 2 سام سنگ سیٹ', '(i) فرض کړئ A: 2 سامسنګ موبایلونه')
b.mlines([r'n(A)={}^{10}_{2}C=45,', r'P(A)=\frac{n(A)}{n(S)}=\frac{45}{105}=0.43'])
b.p('(ii) Let B: at least one Samsung set', '(ii) فرض کریں B: کم از کم ایک سام سنگ سیٹ', '(ii) فرض کړئ B: لږ تر لږه یو سامسنګ موبایل')
b.group('lines', [
    ('B = 1 Samsung or 2 Samsung sets', 'B = 1 سام سنگ یا 2 سام سنگ سیٹ', 'B = 1 سامسنګ یا 2 سامسنګ موبایلونه'),
    ('= (1 Samsung and 1 i-Phone) or 2 Samsung sets', '= (1 سام سنگ اور 1 آئی فون) یا 2 سام سنگ سیٹ', '= (1 سامسنګ او 1 آی فون) یا 2 سامسنګ موبایلونه'),
])
b.mlines([r'n(B)=\left\{{}^{10}_{1}C\times{}^{5}_{1}C\right\}+{}^{10}_{2}C=(10\times 5)+45=50+45=95', r'P(B)=\frac{n(B)}{n(S)}=\frac{95}{105}=0.90'])
b.p('(iii) Let C: one Samsung and one i-Phone set', '(iii) فرض کریں C: ایک سام سنگ اور ایک آئی فون سیٹ', '(iii) فرض کړئ C: یو سامسنګ او یو آی فون موبایل')
b.mlines([r'n(C)={}^{10}_{1}C\times{}^{5}_{1}C=10\times 5=50', r'P(C)=\frac{n(C)}{n(S)}=\frac{50}{105}=0.48'])
b.h('1.3 Complementation law of probability', '1.3 احتمال کا قانونِ تکمیل', '1.3 د احتمال د بشپړوونې قانون')
b.h('Statement:', 'بیان:', 'بیان:')
b.p('If $\\overline{A}$ is the complement of an event A in the sample space then $P(\\overline{A})=1-P(A)$',
    'اگر نمونہ فضا میں $\\overline{A}$ واقعہ A کا تکملہ ہو تو $P(\\overline{A})=1-P(A)$',
    'که په نمونوي فضا کې $\\overline{A}$ د A پېښې بشپړوونکې وي، نو $P(\\overline{A})=1-P(A)$')
b.h('Proof:', 'ثبوت:', 'ثبوت:')
b.p('As we see from the Venn diagram that event A and $\\overline{A}$ are mutually exclusive and exhaustive so $A\\cup\\overline{A}=S$. Taking probability on both sides',
    'جیسا کہ وین خاکے سے ظاہر ہے کہ واقعہ A اور $\\overline{A}$ باہم مانع اور جامع ہیں، لہٰذا $A\\cup\\overline{A}=S$۔ دونوں طرف احتمال لینے سے',
    'لکه څنګه چې د وېن له ډیاګرام څخه ښکاري، A پېښه او $\\overline{A}$ یو بل منع کوونکې او جامع دي، نو $A\\cup\\overline{A}=S$. دواړو خواوو ته احتمال اخیستلو سره')
b.visual('stat12-venn-complement', venn_complement(), ratio=.45)
b.group('lines', [
    ('$P(A\\cup\\overline{A})=P(S)$',) * 3,
    ('$P(A)+P(\\overline{A})=1$ (Using axiom II and III)', '$P(A)+P(\\overline{A})=1$ (مسلّمہ II اور III کی مدد سے)', '$P(A)+P(\\overline{A})=1$ (د II او III اصولو په کارولو سره)'),
    ('or $P(\\overline{A})=1-P(A)$.', 'یا $P(\\overline{A})=1-P(A)$۔', 'یا $P(\\overline{A})=1-P(A)$.'),
])
b.h('Example 1.13', 'مثال 1.13', 'بېلګه 1.13')
b.p('Five fair coins were tossed once. What is the probability that at least one head occurs?',
    'پانچ منصفانہ سکے ایک بار اچھالے گئے۔ کم از کم ایک چِت آنے کا احتمال کیا ہے؟',
    'پنځه عادلانه سکې یو ځل واچول شوې. د لږ تر لږه یو سر د راتلو احتمال څومره دی؟')
rec = b.build('stat12-p011-complementation', 'Examples 1.11–1.12 and 1.3 Complementation law', 'مثالیں 1.11–1.12 اور 1.3 قانونِ تکمیل', 'بېلګې 1.11–1.12 او 1.3 د بشپړوونې قانون', 11, [13, 14])

if __name__ == '__main__':
    save(11, [(1, rec)])
