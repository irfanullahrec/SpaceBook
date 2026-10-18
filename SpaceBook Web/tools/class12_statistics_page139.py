"""PDF139 printed 269–270: 2×2 contingency table and identities; order of classes with tree; ultimate classes; 8.1.3 association start."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import order_tree

b = Builder()
b.p('Since two attributes are involved, the division of the sample is called two-way classification.', 'چونکہ دو صفات شامل ہیں، لہٰذا نمونے کی تقسیم دو طرفہ درجہ بندی کہلاتی ہے۔', 'څرنګه چې دوه صفتونه شامل دي، نو د نمونې وېش دوه اړخیزه ډلبندي بلل کېږي.')
b.h('2 × 2 Contingency table', '2 × 2 اتفاقی جدول', '2 × 2 احتمالي جدول')
b.p('Classification of data about two attributes each having two classes or categories can be shown in tabular form as given below.', 'دو صفات کے بارے میں مواد کی درجہ بندی، جن میں سے ہر ایک کی دو جماعتیں یا زمرے ہوں، نیچے دیے گئے جدولی انداز میں دکھائی جا سکتی ہے۔', 'د دوو صفتونو په اړه د معلوماتو ډلبندي، چې هر یو یې دوه ټولګي یا کټګورۍ لري، د لاندې جدول په بڼه ښودل کېدای شي.')
b.p('(2 × 2) Contingency table', '(2 × 2) اتفاقی جدول', '(2 × 2) احتمالي جدول')
b.table('stat12-t-2x2', ['Attributes', 'B', 'β', 'Row total'], [['A', '(AB)', '(Aβ)', '(A)'], ['α', '(αB)', '(αβ)', '(α)'], ['Column total', '(B)', '(β)', 'n']],
        ['صفات', 'B', 'β', 'قطار کا میزان'], ['صفتونه', 'B', 'β', 'د قطار ټولټال'],
        [['A', '(AB)', '(Aβ)', '(A)'], ['α', '(αB)', '(αβ)', '(α)'], ['کالم کا میزان', '(B)', '(β)', 'n']],
        [['A', '(AB)', '(Aβ)', '(A)'], ['α', '(αB)', '(αβ)', '(α)'], ['د ستون ټولټال', '(B)', '(β)', 'n']])
b.p('Since the table contains 2 rows and 2 columns is therefore called 2 × 2 contingency table.', 'چونکہ جدول میں 2 قطاریں اور 2 کالم ہیں، اس لیے اسے 2 × 2 اتفاقی جدول کہتے ہیں۔', 'څرنګه چې جدول 2 قطارونه او 2 ستونونه لري، نو 2 × 2 احتمالي جدول بلل کېږي.')
b.p('Remember that:', 'یاد رکھیں کہ:', 'په یاد ولرئ چې:')
b.group('lines', [(t,) * 3 for t in ['n = (A) + (α)', 'n = (B) + (β)', '(A) = (AB) + (Aβ)', '(α) = (αB) + (αβ)', '(B) = (AB) + (αB)', '(β) = (Aβ) + (αβ)']])
b.h('Order of classes', 'جماعتوں کا درجہ', 'د ټولګیو درجه')
b.p('The order of a class is determined by the number of attributes present in a class. For example, the classes which contain only one attribute say “A” or “B” are called classes of first order. The classes which contain two attributes say “AB” are said to be the classes of the second order. Similarly, the classes which contain three attributes say “ABC” are said to be the classes of the third order and so on. The sample size n does not contain any attributes so is called class of order zero. Let us understand the above discussion through tree diagram as;',
    'کسی جماعت کا درجہ اس میں موجود صفات کی تعداد سے طے ہوتا ہے۔ مثلاً وہ جماعتیں جن میں صرف ایک صفت ہو، جیسے “A” یا “B”، پہلے درجے کی جماعتیں کہلاتی ہیں۔ وہ جماعتیں جن میں دو صفات ہوں، جیسے “AB”، دوسرے درجے کی جماعتیں کہلاتی ہیں۔ اسی طرح وہ جماعتیں جن میں تین صفات ہوں، جیسے “ABC”، تیسرے درجے کی جماعتیں کہلاتی ہیں، وغیرہ۔ نمونے کے سائز n میں کوئی صفت نہیں ہوتی اس لیے اسے صفر درجے کی جماعت کہتے ہیں۔ آئیے مندرجہ بالا بحث کو شجری خاکے سے سمجھیں؛',
    'د یوه ټولګي درجه په ټولګي کې د موجودو صفتونو په شمېر ټاکل کېږي. د بېلګې په توګه هغه ټولګي چې یوازې یو صفت لري، لکه “A” یا “B”، د لومړۍ درجې ټولګي بلل کېږي. هغه ټولګي چې دوه صفتونه لري، لکه “AB”، د دویمې درجې ټولګي بلل کېږي. همداسې هغه ټولګي چې درې صفتونه لري، لکه “ABC”، د درېیمې درجې ټولګي بلل کېږي، او داسې نور. د نمونې اندازه n هېڅ صفت نه لري نو د صفر درجې ټولګی بلل کېږي. راځئ پورتنی بحث د ونې د ډیاګرام له لارې وپوهېږو؛')
b.visual('stat12-attr-order-tree', order_tree('en'), order_tree('ur'), order_tree('ps'), ratio=.85)
b.h('Ultimate classes and ultimate class frequencies', 'حتمی جماعتیں اور حتمی جماعتی تعدد', 'وروستي ټولګي او د وروستیو ټولګیو تکرارونه')
b.p('The classes and class frequencies of the highest order are called the ultimate classes and ultimate class frequencies. For example, for one attribute ultimate classes are A, α and ultimate frequencies are (A), (α). For two attributes, ultimate classes are AB, Aβ, αB, αβ and ultimate classes frequencies are (AB), (Aβ), (αB), (αβ). If we are considering three attributes A, B, C, then ultimate classes are ABC, ABγ, AβC, Aβγ, αBC, αBγ, αβC, αβγ and ultimate class frequencies are (ABC), (ABγ), (AβC), (Aβγ), (αBC), (αBγ), (αβC), (αβγ) and so on.',
    'سب سے اونچے درجے کی جماعتیں اور جماعتی تعدد حتمی جماعتیں اور حتمی جماعتی تعدد کہلاتے ہیں۔ مثلاً ایک صفت کے لیے حتمی جماعتیں A، α اور حتمی تعدد (A)، (α) ہیں۔ دو صفات کے لیے حتمی جماعتیں AB، Aβ، αB، αβ اور حتمی جماعتی تعدد (AB)، (Aβ)، (αB)، (αβ) ہیں۔ اگر ہم تین صفات A، B، C پر غور کریں تو حتمی جماعتیں ABC، ABγ، AβC، Aβγ، αBC، αBγ، αβC، αβγ اور حتمی جماعتی تعدد (ABC)، (ABγ)، (AβC)، (Aβγ)، (αBC)، (αBγ)، (αβC)، (αβγ) ہیں، وغیرہ۔',
    'د لوړې درجې ټولګي او د ټولګیو تکرارونه وروستي ټولګي او د وروستیو ټولګیو تکرارونه بلل کېږي. د بېلګې په توګه د یوه صفت لپاره وروستي ټولګي A، α او وروستي تکرارونه (A)، (α) دي. د دوو صفتونو لپاره وروستي ټولګي AB، Aβ، αB، αβ او د وروستیو ټولګیو تکرارونه (AB)، (Aβ)، (αB)، (αβ) دي. که موږ درې صفتونه A، B، C په پام کې ونیسو، نو وروستي ټولګي ABC، ABγ، AβC، Aβγ، αBC، αBγ، αβC، αβγ او د وروستیو ټولګیو تکرارونه (ABC)، (ABγ)، (AβC)، (Aβγ)، (αBC)، (αBγ)، (αβC)، (αβγ) دي، او داسې نور.')
b.h('8.1.3 Association of attributes', '8.1.3 صفات کا تلازم', '8.1.3 د صفتونو تړاو')
b.p('Association is a statistical technique which measures the strength and direction of relationship among qualitative variables.', 'تلازم ایک شماریاتی تکنیک ہے جو کیفیتی متغیرات کے درمیان تعلق کی مضبوطی اور سمت کی پیمائش کرتا ہے۔', 'تړاو یوه احصاییوي تخنیک ده چې د کیفي متغیرونو ترمنځ د اړیکې ځواک او لوری اندازه کوي.')
rec = b.build('stat12-p139-contingency-order', '2 × 2 contingency table, order of classes, ultimate classes; 8.1.3 association', '2 × 2 اتفاقی جدول، جماعتوں کا درجہ، حتمی جماعتیں؛ 8.1.3 تلازم', '2 × 2 احتمالي جدول، د ټولګیو درجه، وروستي ټولګي؛ 8.1.3 تړاو', 139, [269, 270])

if __name__ == '__main__':
    save(139, [(8, rec)])

