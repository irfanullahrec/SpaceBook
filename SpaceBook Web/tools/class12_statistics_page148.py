"""PDF148 printed 287–288: Unit 8 Exercise 8.3 MCQs (i)–(x); questions 8.4–8.9 (with data table)."""
from class12_statistics_common import Builder, save

b = Builder()
b.h('8.3 Choose the correct answer.', '8.3 درست جواب منتخب کریں۔', '8.3 سم ځواب وټاکئ.')
b.mcq('i.', ('Relationship between two categorical variables is called', 'دو زمرہ وار متغیرات کے درمیان تعلق کہلاتا ہے', 'د دوو کټګوریکو متغیرونو ترمنځ اړیکه بلل کېږي'),
      [('regression', 'رجعت', 'رجعت'), ('correlation', 'ارتباط', 'همبستګي'), ('association', 'تلازم', 'تړاو'), ('coefficient of variation', 'تغیر کا سر', 'د تغیر ضریب')])
b.mcq('ii.', ('The combination AB of attributes is known as the class of', 'صفات کا امتزاج AB جماعت کہلاتا ہے', 'د صفتونو ترکیب AB د دې ټولګي په نوم یادېږي'),
      [('first order', 'پہلے درجے', 'لومړۍ درجې'), ('second order', 'دوسرے درجے', 'دویمې درجې'), ('third order', 'تیسرے درجے', 'درېیمې درجې'), ('zero order', 'صفر درجے', 'صفر درجې')])
b.mcq('iii.', ('For a 4 × 5 contingency table the degrees of freedom for the $\\chi^2$ is', '4 × 5 اتفاقی جدول کے لیے $\\chi^2$ کے درجاتِ آزادی ہیں', 'د 4 × 5 احتمالي جدول لپاره د $\\chi^2$ د ازادۍ درجې دي'), ['20', '16', '15', '12'], per_line=4)
b.mcq('iv.', ('The range of Yule’s coefficient of association is', 'یول کے تلازم کے سر کی حد ہے', 'د یول د تړاو د ضریب حد دی'), ['$0$ to $\\infty$', '$-\\infty$ to $0$', '$0$ to $1$', '$-1$ to $+1$'])
b.mcq('v.', ('With two attributes, the total number of ultimate class frequency is', 'دو صفات کے ساتھ حتمی جماعتی تعدد کی کل تعداد ہے', 'د دوو صفتونو سره د وروستیو ټولګیو د تکرار ټول شمېر دی'),
      [('two', 'دو', 'دوه'), ('four', 'چار', 'څلور'), ('six', 'چھ', 'شپږ'), ('five', 'پانچ', 'پنځه')])
b.mcq('vi.', ('If $(AB)<\\frac{(A)(B)}{n}$, then the attributes are', 'اگر $(AB)<\\frac{(A)(B)}{n}$ ہو تو صفات ہیں', 'که $(AB)<\\frac{(A)(B)}{n}$ وي، نو صفتونه دي'),
      [('independent', 'آزاد', 'خپلواک'), ('positively associated', 'مثبت طور پر متلازم', 'مثبت تړاو لرونکي'), ('negatively associated', 'منفی طور پر متلازم', 'منفي تړاو لرونکي'), ('no association', 'کوئی تلازم نہیں', 'بې‌تړاوه')])
b.mcq('vii.', ('$\\chi^2$ test statistic value varies form', '$\\chi^2$ جانچ کے شماریے کی قیمت بدلتی ہے', 'د $\\chi^2$ د ازموینې احصاییې قیمت بدلېږي'), ['$-\\infty$ to $0$', '$0$ to $\\infty$', '$-\\infty$ to $\\infty$', '$-1$ to $+1$'], per_line=4)
b.mcq('viii.', ('If A and B are independent attributes then the coefficient of association is equal to', 'اگر A اور B آزاد صفات ہوں تو تلازم کا سر برابر ہے', 'که A او B خپلواک صفتونه وي، نو د تړاو ضریب برابر دی'), ['−1', '+1', '0', '0.5'], per_line=4)
b.mcq('ix.', ('The degrees of freedom for a (2 × 2) contingency table will always be equal to', '(2 × 2) اتفاقی جدول کے درجاتِ آزادی ہمیشہ برابر ہوں گے', 'د (2 × 2) احتمالي جدول د ازادۍ درجې به تل برابرې وي'), ['4', '2', '1', '0'], per_line=4)
b.mcq('x.', ('In case of consistent data, no class frequency can be', 'مستقل مواد کی صورت میں کوئی جماعتی تعدد نہیں ہو سکتا', 'د همغږو معلوماتو په حالت کې هېڅ د ټولګي تکرار نه شي کېدای'),
      [('positive', 'مثبت', 'مثبت'), ('negative', 'منفی', 'منفي'), ('zero', 'صفر', 'صفر'), ('one', 'ایک', 'یو')])
b.group('lines', [
    ('8.4 What is meant by attributes and how they are classified?', '8.4 صفات سے کیا مراد ہے اور ان کی درجہ بندی کیسے کی جاتی ہے؟', '8.4 له صفتونو څخه څه مراد دی او څنګه ډلبندي کېږي؟'),
    ('8.5 Write short notes on the following:', '8.5 درج ذیل پر مختصر نوٹ لکھیں:', '8.5 په لاندې لنډې یادښتونه ولیکئ:'),
    ('i. Class symbol and class frequency', 'i. جماعت کی علامت اور جماعتی تعدد', 'i. د ټولګي نښه او د ټولګي تکرار'),
    ('ii. Positive and negative classes', 'ii. مثبت اور منفی جماعتیں', 'ii. مثبت او منفي ټولګي'),
    ('iii. Order of classes', 'iii. جماعتوں کا درجہ', 'iii. د ټولګیو درجه'),
    ('iv. Ultimate class frequencies', 'iv. حتمی جماعتی تعدد', 'iv. د وروستیو ټولګیو تکرارونه'),
    ('8.6 Explain the following:', '8.6 درج ذیل کی وضاحت کریں:', '8.6 لاندې تشریح کړئ:'),
    ('i. Two-way classification', 'i. دو طرفہ درجہ بندی', 'i. دوه اړخیزه ډلبندي'),
    ('ii. Association of attributes', 'ii. صفات کا تلازم', 'ii. د صفتونو تړاو'),
    ('iii. Positive and negative association', 'iii. مثبت اور منفی تلازم', 'iii. مثبت او منفي تړاو'),
    ('iv. Criterion of independence of attributes.', 'iv. صفات کی آزادی کا معیار۔', 'iv. د صفتونو د خپلواکۍ معیار.'),
    ('v. Yule’s coefficient of association.', 'v. یول کا تلازم کا سر۔', 'v. د یول د تړاو ضریب.'),
    ('8.7 Distinguish between associations and correlation?', '8.7 تلازم اور ارتباط میں فرق کریں؟', '8.7 د تړاو او همبستګۍ ترمنځ توپیر وکړئ؟'),
    ('8.8 When are two attributes said to be', '8.8 دو صفات کب کہلاتی ہیں', '8.8 دوه صفتونه کله بلل کېږي'),
    ('i. Independent', 'i. آزاد', 'i. خپلواک'),
    ('ii. Positively associated', 'ii. مثبت طور پر متلازم', 'ii. مثبت تړاو لرونکي'),
    ('iii. Negatively associated', 'iii. منفی طور پر متلازم', 'iii. منفي تړاو لرونکي'),
    ('8.9 Calculate the coefficient of association between extravagance in fathers and sons:', '8.9 باپوں اور بیٹوں میں فضول خرچی کے درمیان تلازم کا سر معلوم کریں:', '8.9 د پلرونو او زامنو په اسراف کې د تړاو ضریب محاسبه کړئ:'),
])
b.table('stat12-t-q8-9', ['Attributes', 'extravagant sons', 'miserly sons'], [['extravagant fathers', '237', '545'], ['miserly fathers', '741', '235']],
        ['صفات', 'فضول خرچ بیٹے', 'کنجوس بیٹے'], ['صفتونه', 'مسرف زامن', 'بخیل زامن'],
        [['فضول خرچ باپ', '237', '545'], ['کنجوس باپ', '741', '235']], [['مسرف پلرونه', '237', '545'], ['بخیل پلرونه', '741', '235']])
ex = b.build('stat12-u8-exercise-b', 'Unit 8 Exercise — 8.3 MCQs, 8.4–8.9', 'یونٹ 8 مشق — 8.3 کثیر انتخابی، 8.4–8.9', 'واحد 8 تمرین — 8.3 څوځوابه، 8.4–8.9', 148, [287, 288])

if __name__ == '__main__':
    save(148, [(8, ex)])
