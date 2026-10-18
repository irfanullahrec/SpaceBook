"""PDF21 printed 33–34: general discrete distribution table, Examples 2.1–2.2, 2.2.1 probability mass function, 2.2.2 properties."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('Discrete probability distribution', 'منفصل احتمالی تقسیم', 'منفصل احتمالي وېش')
b.table('stat12-t-general-discrete', ['$X$', '$p(x)$'],
        [['$x_1$', '$p(x_1)$'], ['$x_2$', '$p(x_2)$'], ['$\\vdots$', '$\\vdots$'], ['$x_n$', '$p(x_n)$'], ['Total', '$\\sum_{i=1}^{n}p(x_i)=1$']],
        ['$X$', '$p(x)$'], ['$X$', '$p(x)$'],
        [['$x_1$', '$p(x_1)$'], ['$x_2$', '$p(x_2)$'], ['$\\vdots$', '$\\vdots$'], ['$x_n$', '$p(x_n)$'], ['کل', '$\\sum_{i=1}^{n}p(x_i)=1$']],
        [['$x_1$', '$p(x_1)$'], ['$x_2$', '$p(x_2)$'], ['$\\vdots$', '$\\vdots$'], ['$x_n$', '$p(x_n)$'], ['ټول', '$\\sum_{i=1}^{n}p(x_i)=1$']])
b.h('Example 2.1', 'مثال 2.1', 'بېلګه 2.1')
b.p('Three children were born in a government hospital on Sunday. Find the probability distribution for the number of girls.',
    'اتوار کو ایک سرکاری ہسپتال میں تین بچے پیدا ہوئے۔ لڑکیوں کی تعداد کی احتمالی تقسیم معلوم کریں۔',
    'د یکشنبې په ورځ په یوه دولتي روغتون کې درې ماشومان وزېږېدل. د نجونو د شمېر احتمالي وېش پیدا کړئ.')
b.h(*SOL)
b.mlines([r'\text{Here } n(S)=2^n=2^3=8', r'S=\{BBB,BBG,BGB,BGG,GBB,GBG,GGB,GGG\}'])
b.p('X: the number of girls', 'X: لڑکیوں کی تعداد', 'X: د نجونو شمېر')
b.eq(r'=\{0,1,1,2,1,2,2,3\}')
b.p('Probability distribution for X', 'X کی احتمالی تقسیم', 'د X احتمالي وېش')
rows = [['0', '$\\frac{1}{8}$'], ['1', '$\\frac{3}{8}$'], ['2', '$\\frac{3}{8}$'], ['3', '$\\frac{1}{8}$']]
b.table('stat12-t-ex2-1', ['$X$', '$p(x)$'], rows + [['Total', '1']], ['$X$', '$p(x)$'], ['$X$', '$p(x)$'], rows + [['کل', '1']], rows + [['ټول', '1']])
b.h('Example 2.2', 'مثال 2.2', 'بېلګه 2.2')
b.p('A fair die is rolled once. Find the probability distribution for up turned faces.', 'ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ اوپر آنے والے رخوں کی احتمالی تقسیم معلوم کریں۔', 'یو عادلانه ډایس یو ځل اچول کېږي. د پورته راغلو مخونو احتمالي وېش پیدا کړئ.')
b.h(*SOL)
b.p('When a die is rolled we may get 1 or 2 or 3 or 4 or 5 or 6 each with same probability $1/6$ of its occurrence because the die is fair. It can be shown in tabular form, called probability distribution as follows:',
    'جب پانسہ پھینکا جائے تو ہمیں 1 یا 2 یا 3 یا 4 یا 5 یا 6 مل سکتا ہے، ہر ایک کے آنے کا احتمال یکساں $1/6$ ہے کیونکہ پانسہ منصفانہ ہے۔ اسے جدولی شکل میں دکھایا جا سکتا ہے جسے احتمالی تقسیم کہتے ہیں:',
    'کله چې ډایس واچول شي، کېدای شي 1 یا 2 یا 3 یا 4 یا 5 یا 6 ترلاسه کړو، هر یو د راتلو یو شان احتمال $1/6$ لري ځکه چې ډایس عادلانه دی. دا په جدولي بڼه ښودل کېدای شي چې احتمالي وېش بلل کېږي:')
six = ['$\\frac{1}{6}$'] * 6
b.table('stat12-t-ex2-2', ['$X$', '1', '2', '3', '4', '5', '6', 'Total'], [['$p(x)$'] + six + ['1']],
        ['$X$', '1', '2', '3', '4', '5', '6', 'کل'], ['$X$', '1', '2', '3', '4', '5', '6', 'ټول'])
b.h('2.2.1 Probability mass function', '2.2.1 احتمالی کمیتی تفاعل', '2.2.1 د احتمال کتلوي تابع')
b.p('If probability distribution of a random variable X is expressed in a mathematical form or formula, then it is called probability mass function or probability function. It is denoted by $p(x_i)$ and is presented as:',
    'اگر کسی تصادفی متغیر X کی احتمالی تقسیم ریاضیاتی شکل یا فارمولا میں ظاہر کی جائے تو اسے احتمالی کمیتی تفاعل یا احتمالی تفاعل کہتے ہیں۔ اسے $p(x_i)$ سے ظاہر کرتے ہیں اور یوں پیش کرتے ہیں:',
    'که د یوه تصادفي متغیر X احتمالي وېش په ریاضي بڼه یا فورمول کې وښودل شي، نو د احتمال کتلوي تابع یا احتمالي تابع بلل کېږي. په $p(x_i)$ ښودل کېږي او داسې وړاندې کېږي:')
b.eq(r'p(x_i)=\left\{\begin{matrix}p(X=x_i), & i=1,2,\ldots,n\\ 0 & \textit{otherwise}\end{matrix}\right\}')
b.p('Remember that the objective of probability distribution and probability function is same. Some writers make no distinction and they use probability distribution and probability function interchangeably.',
    'یاد رکھیں کہ احتمالی تقسیم اور احتمالی تفاعل کا مقصد ایک ہی ہے۔ بعض مصنفین ان میں فرق نہیں کرتے اور احتمالی تقسیم اور احتمالی تفاعل کو ایک دوسرے کی جگہ استعمال کرتے ہیں۔',
    'په یاد ولرئ چې د احتمالي وېش او احتمالي تابع موخه یوه ده. ځینې لیکوال توپیر نه کوي او احتمالي وېش او احتمالي تابع یو د بل پر ځای کاروي.')
b.h('2.2.2 Properties of discrete probability distribution', '2.2.2 منفصل احتمالی تقسیم کی خصوصیات', '2.2.2 د منفصل احتمالي وېش ځانګړنې')
b.p('A probability distribution and probability mass function $p(x_i)$ must satisfy the following two properties:',
    'احتمالی تقسیم اور احتمالی کمیتی تفاعل $p(x_i)$ کو درج ذیل دو خصوصیات پوری کرنی چاہئیں:',
    'احتمالي وېش او د احتمال کتلوي تابع $p(x_i)$ باید لاندې دوه ځانګړنې پوره کړي:')
b.mlines([r'(i)\quad 0\le p(x_i)\le 1', r'(ii)\quad \sum_{i=1}^{n}p(x_i)=1'])
rec = b.build('stat12-p021-pmf', 'Examples 2.1–2.2, 2.2.1 probability mass function and 2.2.2 properties', 'مثالیں 2.1–2.2، 2.2.1 احتمالی کمیتی تفاعل اور 2.2.2 خصوصیات', 'بېلګې 2.1–2.2، 2.2.1 د احتمال کتلوي تابع او 2.2.2 ځانګړنې', 21, [33, 34])
issues = [{'id': 'stat12-p33-caption-clipped', 'unit': 2, 'printedPage': 33, 'description': 'The caption above the general table is clipped at the top edge of the scan (only “Discrete probabili…” is visible); rendered as “Discrete probability distribution”.'}]

if __name__ == '__main__':
    save(21, [(2, rec)], issues=issues)
