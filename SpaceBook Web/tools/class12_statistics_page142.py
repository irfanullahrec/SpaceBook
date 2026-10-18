"""PDF142 printed 275–276: Example 8.3 table and Q = 0.71; 8.1.5 multi-way classification; 8.2 contingency table (r × c) and expected frequency."""
from class12_statistics_common import Builder, save

Q = r'Q=\frac{(AB)(\alpha\beta)-(A\beta)(\alpha B)}{(AB)(\alpha\beta)+(A\beta)(\alpha B)}'
b = Builder()
b.table('stat12-t-ex8-3', ['Attributes', 'Successful', 'Not successful', 'Total'],
        [['Coached A', 'AB = 150', 'Aβ = 106', '256'], ['Not coached α', 'αB = 272', 'αβ = 1132', '1404'], ['Total', '422', '1238', '1660']],
        ['صفات', 'کامیاب', 'ناکام', 'میزان'], ['صفتونه', 'بریالي', 'نابریالي', 'ټول'],
        [['کوچنگ لی A', 'AB = 150', 'Aβ = 106', '256'], ['کوچنگ نہیں لی α', 'αB = 272', 'αβ = 1132', '1404'], ['میزان', '422', '1238', '1660']],
        [['کوچنګ شوي A', 'AB = 150', 'Aβ = 106', '256'], ['نا کوچنګ شوي α', 'αB = 272', 'αβ = 1132', '1404'], ['ټول', '422', '1238', '1660']])
b.p('Yule’s coefficient of association is given as', 'یول کا تلازم کا سر یوں دیا گیا ہے', 'د یول د تړاو ضریب داسې ورکړل شوی')
b.mlines([Q, r'Q=\frac{(150)(1132)-(106)(272)}{(150)(1132)+(106)(272)}=\frac{140968}{198632}=0.71'])
b.p('There is high positive association means that coaching helps in success.', 'زیادہ مثبت تلازم ہے جس کا مطلب ہے کہ کوچنگ کامیابی میں مدد دیتی ہے۔', 'لوړ مثبت تړاو شته چې مانا یې دا ده چې کوچنګ په بریا کې مرسته کوي.')
e83 = b.build('stat12-p142-example-8-3', 'Example 8.3 — coaching classes, Q = 0.71', 'مثال 8.3 — کوچنگ کلاسیں، Q = 0.71', 'بېلګه 8.3 — د کوچنګ ټولګي، Q = 0.71', 142, [275])

c = Builder()
c.h('8.1.5 Multi-way classification', '8.1.5 کثیر طرفہ درجہ بندی', '8.1.5 څو اړخیزه ډلبندي')
c.p('When a population or sample is divided into many classes or categories according to an attribute is called multi-way or manifold classification. For example, a population according to “colour of eyes” can be divided as black eyes, grey eyes, green eyes etc. Population of students according to “performance” in an examination can be rated as excellent, good, average and poor. Heights of persons can be categorized as tall, medium and short. The classification of data about such attributes which have many classes can be shown by means of a contingency table.',
    'جب کسی آبادی یا نمونے کو ایک صفت کے مطابق کئی جماعتوں یا زمروں میں تقسیم کیا جائے تو اسے کثیر طرفہ یا متعدد درجہ بندی کہتے ہیں۔ مثلاً “آنکھوں کے رنگ” کے مطابق آبادی کو سیاہ آنکھیں، سرمئی آنکھیں، سبز آنکھیں وغیرہ میں تقسیم کیا جا سکتا ہے۔ امتحان میں “کارکردگی” کے مطابق طلبہ کی آبادی کو بہترین، اچھا، اوسط اور کمزور درجہ دیا جا سکتا ہے۔ افراد کے قد کو لمبا، درمیانہ اور چھوٹا میں زمرہ بند کیا جا سکتا ہے۔ ایسی صفات کے بارے میں مواد کی درجہ بندی، جن کی کئی جماعتیں ہوں، اتفاقی جدول کے ذریعے دکھائی جا سکتی ہے۔',
    'کله چې یو نفوس یا نمونه د یوه صفت له مخې په ډېرو ټولګیو یا کټګوریو ووېشل شي، څو اړخیزه یا ګڼ‌ګونې ډلبندي بلل کېږي. د بېلګې په توګه نفوس د “سترګو د رنګ” له مخې په تورو سترګو، خړو سترګو، شنو سترګو او نورو وېشل کېدای شي. د زده کوونکو نفوس په ازموینه کې د “فعالیت” له مخې عالي، ښه، منځنی او کمزوری درجه بندي کېدای شي. د خلکو قدونه په لوړ، منځني او ټیټ کټګوري کېدای شي. د داسې صفتونو په اړه د معلوماتو ډلبندي چې ډېر ټولګي لري، د احتمالي جدول په واسطه ښودل کېدای شي.')
c.h('8.2 Contingency table', '8.2 اتفاقی جدول', '8.2 احتمالي جدول')
c.p('A table consisting of r-rows and c-columns into which the data are classified according to two attributes is called (r × c) contingency table. For example, if an attribute “A” has $A_1,A_2,\\ldots,A_r$ classes and attributes “B” has $B_1,B_2,\\ldots,B_c$ classes, then the observed data by (r × c) contingency table is shown as:',
    'r قطاروں اور c کالموں پر مشتمل جدول جس میں مواد کو دو صفات کے مطابق درجہ بند کیا جائے (r × c) اتفاقی جدول کہلاتا ہے۔ مثلاً اگر صفت “A” کی $A_1,A_2,\\ldots,A_r$ جماعتیں اور صفت “B” کی $B_1,B_2,\\ldots,B_c$ جماعتیں ہوں تو مشاہدہ شدہ مواد (r × c) اتفاقی جدول کے ذریعے یوں دکھایا جاتا ہے:',
    'هغه جدول چې له r قطارونو او c ستونونو جوړ وي او معلومات پکې د دوو صفتونو له مخې ډلبندي شي، (r × c) احتمالي جدول بلل کېږي. د بېلګې په توګه که صفت “A” د $A_1,A_2,\\ldots,A_r$ ټولګي او صفت “B” د $B_1,B_2,\\ldots,B_c$ ټولګي ولري، نو لیدل شوي معلومات د (r × c) احتمالي جدول په واسطه داسې ښودل کېږي:')
c.p('(r × c) contingency table', '(r × c) اتفاقی جدول', '(r × c) احتمالي جدول')
cols = ['1', '2', 'j', 'c']
def row(i):
    return [f'$A_{i}$', f'$(A_{i}B_1)$', f'$(A_{i}B_2)$', '…', f'$(A_{i}B_j)$', '…', f'$(A_{i}B_c)$', f'$(A_{i})$']
dots = ['⋮', '⋮', '', '…', '⋮', '…', '⋮', '…']
rows = [row(1), row(2), dots, row('i'), dots, row('r')]
def tot(word):
    return rows + [[word, '$(B_1)$', '$(B_2)$', '…', '$(B_j)$', '…', '$(B_c)$', '$n$']]
hd = lambda a, b2: [a, '$B_1$', '$B_2$', '…', '$B_j$', '…', '$B_c$', b2]
c.table('stat12-t-rxc', hd('Classes', 'Row total'), tot('Column total'), hd('جماعتیں', 'قطار کا میزان'), hd('ټولګي', 'د قطار ټولټال'), tot('کالم کا میزان'), tot('د ستون ټولټال'))
c.p('This table is an extension of (2 × 2) contingency table. The values in the cells of contingency table shown in parentheses are called cell frequencies. For each observed frequency $O_f$, the expected frequency $E_f$ is computed as $E_f=\\frac{R\\times C}{n}$, where R is the row total and C is the column total.',
    'یہ جدول (2 × 2) اتفاقی جدول کی توسیع ہے۔ اتفاقی جدول کے خانوں میں قوسین میں دکھائی گئی قیمتیں خانوی تعدد کہلاتی ہیں۔ ہر مشاہدہ شدہ تعدد $O_f$ کے لیے متوقع تعدد $E_f$ یوں معلوم کیا جاتا ہے $E_f=\\frac{R\\times C}{n}$، جہاں R قطار کا میزان اور C کالم کا میزان ہے۔',
    'دا جدول د (2 × 2) احتمالي جدول پراختیا ده. د احتمالي جدول په خونو کې په قوسونو کې ښودل شوي قیمتونه د خونو تکرارونه بلل کېږي. د هر لیدل شوي تکرار $O_f$ لپاره تمه شوی تکرار $E_f$ داسې محاسبه کېږي $E_f=\\frac{R\\times C}{n}$، چې R د قطار ټولټال او C د ستون ټولټال دی.')
c.p('For example; for observed frequency $(A_1B_1)$ given in above table, the corresponding expected frequency will be equal to $\\frac{(A_1)(B_1)}{n}$ and similarly for $(A_1B_2)$ the expected frequency $=\\frac{(A_1)(B_2)}{n}$ and so on. Chi-square test statistic denoted by $\\chi^2$ (pronounced as kai square) is used to test the hypothesis about independence of attributes in the contingency tables.',
    'مثلاً مندرجہ بالا جدول میں دیے گئے مشاہدہ شدہ تعدد $(A_1B_1)$ کے لیے متعلقہ متوقع تعدد $\\frac{(A_1)(B_1)}{n}$ کے برابر ہوگا اور اسی طرح $(A_1B_2)$ کے لیے متوقع تعدد $=\\frac{(A_1)(B_2)}{n}$، وغیرہ۔ کائی مربع جانچ کا شماریہ، جسے $\\chi^2$ (کائی اسکوائر پڑھا جاتا ہے) سے ظاہر کیا جاتا ہے، اتفاقی جدولوں میں صفات کی آزادی کے بارے میں مفروضے کی جانچ کے لیے استعمال ہوتا ہے۔',
    'د بېلګې په توګه په پورتني جدول کې د ورکړل شوي لیدل شوي تکرار $(A_1B_1)$ لپاره اړوند تمه شوی تکرار به له $\\frac{(A_1)(B_1)}{n}$ سره برابر وي او همداسې د $(A_1B_2)$ لپاره تمه شوی تکرار $=\\frac{(A_1)(B_2)}{n}$، او داسې نور. د کای مربع د ازموینې احصاییه چې په $\\chi^2$ (کای سکوېر لوستل کېږي) ښودل کېږي، په احتمالي جدولونو کې د صفتونو د خپلواکۍ په اړه د فرضیې د ازموینې لپاره کارول کېږي.')
ct = c.build('stat12-p142-contingency-table', '8.1.5 Multi-way classification; 8.2 (r × c) contingency table', '8.1.5 کثیر طرفہ درجہ بندی؛ 8.2 (r × c) اتفاقی جدول', '8.1.5 څو اړخیزه ډلبندي؛ 8.2 (r × c) احتمالي جدول', 142, [275, 276])

if __name__ == '__main__':
    save(142, [(8, e83), (8, ct)])
