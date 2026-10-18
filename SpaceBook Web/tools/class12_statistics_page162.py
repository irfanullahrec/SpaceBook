"""PDF162 printed 315–316: Unit 9 Exercise 9.3 MCQs (viii)–(x); questions 9.4–9.16 (two data tables)."""
from class12_statistics_common import Builder, save

b = Builder()
b.mcq('viii.', ('Factors fertilizer, date of sowing and breeds are called', 'کھاد، بوائی کی تاریخ اور نسلیں جیسے عوامل کہلاتے ہیں', 'سره، د کرلو نېټه او نسلونه عوامل بلل کېږي'),
      [('Replicates', 'تکرار', 'تکرارونه'), ('experimental unit', 'تجرباتی اکائی', 'تجربوي واحد'), ('Treatments', 'علاج', 'درملنې'), ('All of the above', 'مندرجہ بالا سب', 'پورتني ټول')])
b.mcq('ix.', ('Local control in the field is maintained through', 'کھیت میں مقامی کنٹرول برقرار رکھا جاتا ہے', 'په ځمکه کې سیمه‌ییز کنټرول ساتل کېږي د'),
      [('Natural factors', 'قدرتی عوامل', 'طبیعي عواملو له لارې'), ('Randomization', 'تصادفیت', 'تصادفي کولو له لارې'), ('Replication', 'تکرار', 'تکرار له لارې'), ('Uniformity trials', 'یکسانیت کے تجربات', 'د یووالي ازمېښتونو له لارې')])
b.mcq('x.', ('Randomization in an experiment helps the researcher to eliminate', 'تجربے میں تصادفیت محقق کو ختم کرنے میں مدد دیتی ہے', 'په تجربه کې تصادفي کول له څېړونکي سره د له منځه وړلو مرسته کوي'),
      [('Dependence among observations', 'مشاہدات کے درمیان انحصار', 'د مشاهدو ترمنځ تړلتیا'), ('Systematic influences', 'منظم اثرات', 'منظم اغېزونه'), ('Human biases', 'انسانی تعصبات', 'انساني تعصبونه'), ('all of the above', 'مندرجہ بالا سب', 'پورتني ټول')], per_line=1)
b.group('lines', [
    ('9.4 Describe the design of an experiment in your own words.', '9.4 اپنے الفاظ میں تجربے کا ڈیزائن بیان کریں۔', '9.4 په خپلو ټکو کې د تجربې ډیزاین بیان کړئ.'),
    ('9.5 Define the following.', '9.5 درج ذیل کی تعریف کریں۔', '9.5 لاندې تعریف کړئ.'),
    ('i. Experimental material', 'i. تجرباتی مواد', 'i. تجربوي توکي'),
    ('ii. Experimental unit', 'ii. تجرباتی اکائی', 'ii. تجربوي واحد'),
    ('iii. Treatment', 'iii. علاج', 'iii. درملنه'),
    ('iv. Uniformity trial', 'iv. یکسانیت کا تجربہ', 'iv. د یووالي ازمېښت'),
    ('v. Block', 'v. بلاک', 'v. بلاک'),
    ('9.6 What do you understand by randomization, replication and local control in experimental design?', '9.6 تجرباتی ڈیزائن میں تصادفیت، تکرار اور مقامی کنٹرول سے آپ کیا سمجھتے ہیں؟', '9.6 په تجربوي ډیزاین کې له تصادفي کولو، تکرار او سیمه‌ییز کنټرول څخه څه پوهېږئ؟'),
    ('9.7 i. What is meant by experimental design?', '9.7 i. تجرباتی ڈیزائن سے کیا مراد ہے؟', '9.7 i. له تجربوي ډیزاین څخه څه مراد دی؟'),
    ('ii. What are the basic principles of design of experiment?', 'ii. تجربے کے ڈیزائن کے بنیادی اصول کیا ہیں؟', 'ii. د تجربې د ډیزاین بنسټیز اصول کوم دي؟'),
    ('9.8 Discuss and define (a) Extraneous factor (b) experimental error.', '9.8 بحث کریں اور تعریف کریں (a) خارجی عامل (b) تجرباتی خطا۔', '9.8 بحث او تعریف کړئ (a) بهرنی عامل (b) تجربوي تېروتنه.'),
    ('9.9 Discuss the need and utility of planning a statistical experiment.', '9.9 شماریاتی تجربے کی منصوبہ بندی کی ضرورت اور افادیت پر بحث کریں۔', '9.9 د احصاییوي تجربې د پلان جوړولو اړتیا او ګټورتیا باندې بحث وکړئ.'),
    ('9.10 What is a completely randomized design? What are the merits and demerits of a completely randomized design?', '9.10 مکمل تصادفی ڈیزائن کیا ہے؟ مکمل تصادفی ڈیزائن کی خوبیاں اور خامیاں کیا ہیں؟', '9.10 بشپړ تصادفي ډیزاین څه دی؟ د بشپړ تصادفي ډیزاین ګټې او نیمګړتیاوې کومې دي؟'),
    ('9.11 Explain the experimental layout for a completely randomized design using 3 treatment and 15 experiment plots.', '9.11 3 علاج اور 15 تجرباتی قطعات استعمال کرتے ہوئے مکمل تصادفی ڈیزائن کے تجرباتی خاکے کی وضاحت کریں۔', '9.11 د 3 درملنو او 15 تجربوي ټوټو په کارولو د بشپړ تصادفي ډیزاین تجربوي نقشه تشریح کړئ.'),
    ('9.12 Write a short note on analysis of variance.', '9.12 تجزیۂ تغیر پر مختصر نوٹ لکھیں۔', '9.12 د واریانس پر تحلیل لنډ یادښت ولیکئ.'),
    ('9.13 What is meant by analysis of variance? What are the assumptions under which this technique is applied?', '9.13 تجزیۂ تغیر سے کیا مراد ہے؟ یہ تکنیک کن مفروضات کے تحت لاگو ہوتی ہے؟', '9.13 د واریانس له تحلیل څخه څه مراد دی؟ دا تخنیک تر کومو فرضیو لاندې پلي کېږي؟'),
    ('9.14 What do you understand by?', '9.14 آپ کیا سمجھتے ہیں؟', '9.14 څه پوهېږئ؟'),
    ('i. Variance among samples', 'i. نمونوں کے درمیان تغیر', 'i. د نمونو ترمنځ واریانس'),
    ('ii. Variance within samples', 'ii. نمونوں کے اندر تغیر', 'ii. د نمونو دننه واریانس'),
    ('iii. Total variation', 'iii. کل تغیر', 'iii. ټول تغیر'),
    ('9.15 Given the data below, perform the analysis of variance and test the hypothesis that the means of the three populations are equal. Let α = 0.05', '9.15 نیچے دیے گئے مواد کے لیے تجزیۂ تغیر کریں اور اس مفروضے کی جانچ کریں کہ تینوں آبادیوں کے اوسط برابر ہیں۔ α = 0.05 لیں', '9.15 لاندې ورکړل شویو معلوماتو ته د واریانس تحلیل ترسره او دا فرضیه وازموئ چې د درېیو نفوسونو منځني برابر دي. α = 0.05 ونیسئ'),
])
D = [['13', '18', '17'], ['14', '19', '20'], ['16', '12', '8'], ['17', '15', '11']]
X = ['$X_1$', '$X_2$', '$X_3$']
b.table('stat12-t-q9-15', X, D, X, X, D, D)
b.p('9.16 Four salesmen were posted in different areas by a company. The numbers of units of commodity “x” sold by them are as follow:', '9.16 ایک کمپنی نے چار سیلز مین مختلف علاقوں میں تعینات کیے۔ ان کی فروخت کردہ جنس “x” کی اکائیوں کی تعداد درج ذیل ہے:', '9.16 یوه شرکت څلور پلورونکي په بېلابېلو سیمو کې وګمارل. د دوی له خوا د پلورل شوي توکي “x” د واحدونو شمېر په لاندې ډول دی:')
S = [['A', '28', '23', '20', '29'], ['B', '30', '32', '25', '21'], ['C', '35', '28', '23', '18'], ['D', '19', '21', '15', '25']]
H = [''] * 5
b.table('stat12-t-q9-16', H, S, H, H, S, S, noHeader=True)
b.p('Is there a significant difference in the performance of these salesmen?', 'کیا ان سیلز مینوں کی کارکردگی میں معنی خیز فرق ہے؟', 'آیا د دې پلورونکو په فعالیت کې معنی‌دار توپیر شته؟')
ex = b.build('stat12-u9-exercise-b', 'Unit 9 Exercise — 9.3 (viii)–(x), 9.4–9.16', 'یونٹ 9 مشق — 9.3 (viii)–(x)، 9.4–9.16', 'واحد 9 تمرین — 9.3 (viii)–(x)، 9.4–9.16', 162, [315, 316])

if __name__ == '__main__':
    save(162, [(9, ex)])
