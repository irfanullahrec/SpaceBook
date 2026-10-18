"""PDF140 printed 271–272: kinds of association; 8.1.4 methods of measures; Yule's coefficient Q with interpretation; Example 8.1 start."""
from class12_statistics_common import Builder, save

Q = r'Q=\frac{(AB)(\alpha\beta)-(A\beta)(\alpha B)}{(AB)(\alpha\beta)+(A\beta)(\alpha B)}'
b = Builder()
b.h('Kinds of association', 'تلازم کی اقسام', 'د تړاو ډولونه')
b.p('There are three kinds of associations which ossibly occur between attributes namely (i) positive association, (ii) negative association and (iii) no association.', 'صفات کے درمیان ممکنہ طور پر تین قسم کے تلازم ہوتے ہیں یعنی (i) مثبت تلازم، (ii) منفی تلازم اور (iii) کوئی تلازم نہیں۔', 'د صفتونو ترمنځ احتمالاً درې ډوله تړاو پېښېږي یعنې (i) مثبت تړاو، (ii) منفي تړاو او (iii) بې‌تړاوي.')
b.p('(i) In positive association, the presence of one attribute is accompanied by the presence of other attribute(s). For example education and intelligence, health and hygiene are positively associated. In case of positive association, the observed frequency of the combined positive attributes is greater than the expected frequencies i.e.', '(i) مثبت تلازم میں ایک صفت کی موجودگی کے ساتھ دوسری صفت(وں) کی موجودگی ہوتی ہے۔ مثلاً تعلیم اور ذہانت، صحت اور حفظانِ صحت مثبت طور پر متلازم ہیں۔ مثبت تلازم کی صورت میں مشترکہ مثبت صفات کا مشاہدہ شدہ تعدد متوقع تعدد سے زیادہ ہوتا ہے یعنی', '(i) په مثبت تړاو کې د یوه صفت له شتون سره د بل صفت(ونو) شتون مل وي. د بېلګې په توګه زده کړه او هوښیارتیا، روغتیا او حفظ‌الصحه مثبت تړاو لري. د مثبت تړاو په حالت کې د ګډو مثبتو صفتونو لیدل شوی تکرار له تمه شوي تکرار لوی وي یعنې')
b.eq(r'(AB)>\frac{(A)(B)}{n}.')
b.p('Similar relations hold for other attributes.', 'دوسری صفات کے لیے بھی اسی طرح کے تعلقات درست ہیں۔', 'د نورو صفتونو لپاره هم ورته اړیکې سمې دي.')
b.p('(ii) When the presence of an attributes say, A ensures the absence of another attribute say, B or vice-versa, the attributes A and B are said to be negatively associated. For instance, the vaccination and occurrence of disease for which the vaccine is meant for, are negatively associated. In this situation the actual frequency of the cell for combination of attributes is smaller than the expected frequency i.e.', '(ii) جب ایک صفت، مثلاً A، کی موجودگی دوسری صفت، مثلاً B، کی غیر موجودگی یقینی بنائے یا اس کے برعکس، تو صفات A اور B منفی طور پر متلازم کہلاتی ہیں۔ مثلاً ویکسین لگوانا اور اس بیماری کا ہونا جس کے لیے ویکسین بنی ہے، منفی طور پر متلازم ہیں۔ اس صورت میں صفات کے امتزاج والے خانے کا اصل تعدد متوقع تعدد سے کم ہوتا ہے یعنی', '(ii) کله چې د یوه صفت، لکه A، شتون د بل صفت، لکه B، نشتوالی ډاډمن کړي یا برعکس، نو صفتونه A او B منفي تړاو لري. د بېلګې په توګه واکسین کول او د هغې ناروغۍ پېښېدل چې واکسین ورته جوړ شوی، منفي تړاو لري. په دې حالت کې د صفتونو د ترکیب د خونې اصلي تکرار له تمه شوي تکرار کم وي یعنې')
b.eq(r'(AB)<\frac{(A)(B)}{n}.')
b.p('(iii) If the two attributes are such that the presence or absence of one attribute has nothing to do with the presence or absence of the other, they are said to be independent. For instance, skin colour and intelligence of persons are independent attributes. If the two attributes A and B are independent, then $(AB)=\\frac{(A)(B)}{n}$. This is known as criterion of independence.', '(iii) اگر دو صفات ایسی ہوں کہ ایک صفت کی موجودگی یا غیر موجودگی کا دوسری کی موجودگی یا غیر موجودگی سے کوئی تعلق نہ ہو تو انہیں آزاد کہتے ہیں۔ مثلاً افراد کی جلد کا رنگ اور ذہانت آزاد صفات ہیں۔ اگر دو صفات A اور B آزاد ہوں تو $(AB)=\\frac{(A)(B)}{n}$۔ اسے آزادی کا معیار کہتے ہیں۔', '(iii) که دوه صفتونه داسې وي چې د یوه صفت شتون یا نشتوالی د بل له شتون یا نشتوالي سره هېڅ اړه ونه لري، خپلواک بلل کېږي. د بېلګې په توګه د خلکو د پوستکي رنګ او هوښیارتیا خپلواک صفتونه دي. که دوه صفتونه A او B خپلواک وي، نو $(AB)=\\frac{(A)(B)}{n}$. دې ته د خپلواکۍ معیار وایي.')
b.h('8.1.4 Methods of measures of association', '8.1.4 تلازم کی پیمائش کے طریقے', '8.1.4 د تړاو د اندازه کولو طریقې')
b.p('There are mainly three methods of measures of association.', 'تلازم کی پیمائش کے بنیادی طور پر تین طریقے ہیں۔', 'د تړاو د اندازه کولو اساساً درې طریقې دي.')
b.group('lines', [
    ('(i) Yule’s coefficient of association.', '(i) یول کا تلازم کا سر۔', '(i) د یول د تړاو ضریب.'),
    ('(ii) Chi-square test for testing hypothesis about independence of attributes in contingency tables.', '(ii) اتفاقی جدولوں میں صفات کی آزادی کے بارے میں مفروضے کی جانچ کے لیے کائی مربع جانچ۔', '(ii) په احتمالي جدولونو کې د صفتونو د خپلواکۍ په اړه د فرضیې د ازموینې لپاره د کای مربع ازموینه.'),
    ('(iii) Coefficient of contingency for (r × c) contingency table.', '(iii) (r × c) اتفاقی جدول کے لیے اتفاقیت کا سر۔', '(iii) د (r × c) احتمالي جدول لپاره د احتمالیت ضریب.'),
])
b.h('Yule’s coefficient of association', 'یول کا تلازم کا سر', 'د یول د تړاو ضریب')
b.p('Yule’s coefficient of association is named after its inventor G. Undy Yule. It is a relative measure for the strength of association between two attributes say, A and B. It is defined by the formula given below.', 'یول کا تلازم کا سر اپنے موجد G. Undy Yule کے نام پر رکھا گیا ہے۔ یہ دو صفات، مثلاً A اور B، کے درمیان تلازم کی مضبوطی کا اضافی پیمانہ ہے۔ اس کی تعریف نیچے دیے گئے فارمولے سے کی جاتی ہے۔', 'د یول د تړاو ضریب د خپل ایجادګر G. Undy Yule په نوم نومول شوی. دا د دوو صفتونو، لکه A او B، ترمنځ د تړاو د ځواک نسبي اندازه ده. د لاندې فورمول په واسطه تعریف کېږي.')
b.eq(Q + r',\qquad -1<Q<+1')
b.p('The result of Q is interpreted as:', 'Q کے نتیجے کی تشریح یوں کی جاتی ہے:', 'د Q پایله داسې تفسیرېږي:')
H = ['', '']
b.table('stat12-t-yule-q', H, [['If $Q=-1$', 'Attributes have perfect negative association.'], ['$-1<Q<0$', 'Attributes have negative association.'], ['$Q=0$', 'Attributes have no association means they are independent.'], ['$0<Q<+1$', 'Attributes have positive association.'], ['$Q=+1$', 'Attributes have perfect positive association.']], H, H,
        [['اگر $Q=-1$', 'صفات کا مکمل منفی تلازم ہے۔'], ['$-1<Q<0$', 'صفات کا منفی تلازم ہے۔'], ['$Q=0$', 'صفات کا کوئی تلازم نہیں یعنی وہ آزاد ہیں۔'], ['$0<Q<+1$', 'صفات کا مثبت تلازم ہے۔'], ['$Q=+1$', 'صفات کا مکمل مثبت تلازم ہے۔']],
        [['که $Q=-1$', 'صفتونه بشپړ منفي تړاو لري.'], ['$-1<Q<0$', 'صفتونه منفي تړاو لري.'], ['$Q=0$', 'صفتونه هېڅ تړاو نه لري یعنې خپلواک دي.'], ['$0<Q<+1$', 'صفتونه مثبت تړاو لري.'], ['$Q=+1$', 'صفتونه بشپړ مثبت تړاو لري.']], noHeader=True)
ka = b.build('stat12-p140-kinds-yule', 'Kinds of association; 8.1.4 methods; Yule’s coefficient Q', 'تلازم کی اقسام؛ 8.1.4 طریقے؛ یول کا سر Q', 'د تړاو ډولونه؛ 8.1.4 طریقې؛ د یول ضریب Q', 140, [271, 272])

c = Builder()
c.h('Example 8.1', 'مثال 8.1', 'بېلګه 8.1')
c.p('Discuss the association between two attributes say A and B when:', 'دو صفات، مثلاً A اور B، کے درمیان تلازم پر بحث کریں جب:', 'د دوو صفتونو، لکه A او B، ترمنځ پر تړاو بحث وکړئ کله چې:')
c.group('lines', [('(i) (AB) = 110, (αB) = 96, (Aβ) = 290, (αβ) = 510',) * 3, ('(ii) (A) = 245, (AB) = 147, (α) = 285, (αB) = 190',) * 3])
c.h('Solution:', 'حل:', 'حل:')
c.p('(i) Given (AB) = 110, (αB) = 96, (Aβ) = 290, (αβ) = 510', '(i) دیا گیا ہے (AB) = 110، (αB) = 96، (Aβ) = 290، (αβ) = 510', '(i) ورکړل شوي (AB) = 110، (αB) = 96، (Aβ) = 290، (αβ) = 510')
c.p('Coefficient of association is', 'تلازم کا سر یہ ہے', 'د تړاو ضریب دا دی')
c.eq(Q)
e81 = c.build('stat12-p140-example-8-1', 'Example 8.1 — Yule’s Q (start)', 'مثال 8.1 — یول کا Q (آغاز)', 'بېلګه 8.1 — د یول Q (پیل)', 140, [272])
issues = [{'id': 'stat12-p271-272-typos', 'unit': 8, 'printedPage': 272, 'description': 'p271 prints “ossibly” (possibly); p272 prints inventor as “G. Undy Yule” (G. Udny Yule) and the range as “−1 < Q < +1” although Q = ±1 are interpreted below (should be −1 ≤ Q ≤ +1). Printed text retained.'}]

if __name__ == '__main__':
    save(140, [(8, ka), (8, e81)], issues=issues)
