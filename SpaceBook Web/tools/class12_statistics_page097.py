"""PDF97 printed 185–186: Unit 5 key points; Exercise 5.1 (T/F) and 5.2 blanks (i)–(vi)."""
from class12_statistics_common import Builder, save

k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.group('list', [
    ('A group of individuals or objects about which we wish to know something is called population or universe.', 'افراد یا اشیاء کا وہ گروہ جس کے بارے میں ہم کچھ جاننا چاہتے ہیں، آبادی یا کائنات کہلاتا ہے۔', 'د افرادو یا شیانو هغه ډله چې غواړو د هغې په اړه څه پوه شو، نفوس یا کائنات بلل کېږي.'),
    ('If the number of individuals or items of a population are fixed and limited, it is known as finite population.', 'اگر کسی آبادی کے افراد یا اشیاء کی تعداد مقررہ اور محدود ہو تو اسے محدود آبادی کہتے ہیں۔', 'که د یوه نفوس د افرادو یا توکو شمېر ټاکلی او محدود وي، محدود نفوس بلل کېږي.'),
    ('If the population consists of an infinite number of items it is called infinite population.', 'اگر آبادی لامحدود تعداد میں اشیاء پر مشتمل ہو تو اسے لامحدود آبادی کہتے ہیں۔', 'که نفوس له بې‌پایه شمېر توکو جوړ وي، بې‌پایه نفوس بلل کېږي.'),
    ('A single element or group of elements of a population from which required information can be obtained is called sampling unit or unit of the population.', 'آبادی کا وہ واحد عنصر یا عناصر کا گروہ جس سے مطلوبہ معلومات حاصل کی جا سکیں، نمونہ اکائی یا آبادی کی اکائی کہلاتا ہے۔', 'د نفوس هغه یو عنصر یا د عناصرو ډله چې اړین معلومات ترې ترلاسه کېدای شي، نمونوي واحد یا د نفوس واحد بلل کېږي.'),
    ('A part or fraction of a population is called sample.', 'آبادی کے کسی حصے یا جز کو نمونہ کہتے ہیں۔', 'د نفوس یوې برخې یا ټوټې ته نمونه وایي.'),
    ('To ask a question or a series of questions from many people in order to gather information is called survey.', 'معلومات جمع کرنے کے لیے بہت سے لوگوں سے ایک سوال یا سوالات کا سلسلہ پوچھنا سروے کہلاتا ہے۔', 'د معلوماتو د راټولولو لپاره له ډېرو خلکو څخه د یوې پوښتنې یا پوښتنو د لړۍ پوښتل سروې بلل کېږي.'),
    ('A list of all the sampling units or a map or other acceptable material which represent the population to be covered. Such a list or map is called sampling frame.', 'تمام نمونہ اکائیوں کی فہرست یا نقشہ یا کوئی اور قابلِ قبول مواد جو احاطہ کی جانے والی آبادی کی نمائندگی کرے۔ ایسی فہرست یا نقشے کو نمونہ فریم کہتے ہیں۔', 'د ټولو نمونوي واحدونو لیست یا نقشه یا بل منلی مواد چې د پوښل کېدونکي نفوس استازیتوب وکړي. داسې لیست یا نقشې ته نمونوي چوکاټ وایي.'),
    ('The sample design along with some other aspects of the survey e.g. choice and training of interviewers, tabulation plans etc. is called survey design.', 'نمونے کا خاکہ سروے کے کچھ دوسرے پہلوؤں مثلاً انٹرویو لینے والوں کے انتخاب اور تربیت، جدول بندی کے منصوبوں وغیرہ کے ساتھ سروے کا خاکہ کہلاتا ہے۔', 'د نمونې ډیزاین د سروې له ځینو نورو اړخونو لکه د مرکه کوونکو ټاکنه او روزنه، د جدول جوړولو پلانونه او نورو سره د سروې ډیزاین بلل کېږي.'),
    ('Any function of population data is called parameter.', 'آبادی کے مواد کے کسی بھی تفاعل کو پیرامیٹر کہتے ہیں۔', 'د نفوس د معلوماتو هرې تابع ته پارامټر وایي.'),
    ('Any function of sample data is called statistic.', 'نمونے کے مواد کے کسی بھی تفاعل کو شماریہ کہتے ہیں۔', 'د نمونې د معلوماتو هرې تابع ته احصاییه وایي.'),
    ('A statistic which is used for estimation of parameter is called an estimator.', 'وہ شماریہ جو پیرامیٹر کے تخمین کے لیے استعمال ہو، تخمین کار کہلاتا ہے۔', 'هغه احصاییه چې د پارامټر د اټکل لپاره کارول کېږي، اټکلوونکی بلل کېږي.'),
    ('Every estimator is a statistic but every statistic is not an estimator.', 'ہر تخمین کار شماریہ ہے لیکن ہر شماریہ تخمین کار نہیں۔', 'هر اټکلوونکی احصاییه ده خو هره احصاییه اټکلوونکی نه دی.'),
    ('The error which occurs due to the natural differences among the members of the population is called sampling error.', 'وہ غلطی جو آبادی کے ارکان کے درمیان قدرتی فرق کی وجہ سے پیدا ہو، نمونہ جاتی غلطی کہلاتی ہے۔', 'هغه تېروتنه چې د نفوس د غړو ترمنځ د طبیعي توپیرونو له امله رامنځته کېږي، نمونوي تېروتنه بلل کېږي.'),
    ('The error which occurs during the process of collection and processing the data is called non sampling error.', 'وہ غلطی جو مواد جمع کرنے اور اس پر کارروائی کے دوران پیدا ہو، غیر نمونہ جاتی غلطی کہلاتی ہے۔', 'هغه تېروتنه چې د معلوماتو د راټولولو او پروسس کولو پر مهال رامنځته کېږي، غیر نمونوي تېروتنه بلل کېږي.'),
    ('The error which arises due to the personal interest of the investigator is called bias.', 'وہ غلطی جو تحقیق کار کی ذاتی دلچسپی کی وجہ سے پیدا ہو، تعصب کہلاتی ہے۔', 'هغه تېروتنه چې د څېړونکي د شخصي علاقې له امله رامنځته کېږي، تعصب بلل کېږي.'),
    ('The probability distribution of all possible values of an estimator is called sampling distribution of that estimator.', 'کسی تخمین کار کی تمام ممکنہ قیمتوں کی احتمالی تقسیم کو اس تخمین کار کی نمونہ جاتی تقسیم کہتے ہیں۔', 'د یوه اټکلوونکي د ټولو شونو قیمتونو احتمالي وېش ته د هغه اټکلوونکي نمونوي وېش وایي.'),
    ('The standard deviation of the sampling distribution of an estimator is called standard error', 'کسی تخمین کار کی نمونہ جاتی تقسیم کے معیاری انحراف کو معیاری غلطی کہتے ہیں', 'د یوه اټکلوونکي د نمونوي وېش معیاري انحراف ته معیاري تېروتنه وایي'),
    ('An expression which compares a characteristic with the total is called proportion', 'وہ اظہاریہ جو کسی خاصیت کا کل سے موازنہ کرے، تناسب کہلاتا ہے', 'هغه افاده چې یوه ځانګړنه له ټول سره پرتله کوي، تناسب بلل کېږي'),
])
keys = k.build('stat12-u5-key-points', 'Unit 5 — Key points', 'یونٹ 5 — اہم نکات', 'واحد 5 — مهم ټکي', 97, [185])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.h('5.1 Read the fallowing statements carefully and indicate which statement is true or false.', '5.1 درج ذیل بیانات غور سے پڑھیں اور بتائیں کہ کون سا بیان درست یا غلط ہے۔', '5.1 لاندې بیانونه په غور ولولئ او وښایاست چې کوم بیان سم یا ناسم دی.')
e.group('lines', [
    ('i. To perform a census, one would need to examine every item in a population under consideration.', 'i. مردم شماری کرنے کے لیے زیرِ غور آبادی کی ہر شے کا جائزہ لینا ضروری ہوگا۔', 'i. د سرشمېرنې د ترسره کولو لپاره به اړینه وي چې د تر غور لاندې نفوس هر توکی وڅېړل شي.'),
    ('ii. A primary objective of sampling is to choose a sample that is representative of the population under consideration.', 'ii. نمونہ گیری کا بنیادی مقصد ایسا نمونہ چننا ہے جو زیرِ غور آبادی کا نمائندہ ہو۔', 'ii. د نمونه اخیستنې لومړنۍ موخه داسې نمونه ټاکل دي چې د تر غور لاندې نفوس استازې وي.'),
    ('iii. There is no difference between random error and sampling bias.', 'iii. تصادفی غلطی اور نمونہ گیری کے تعصب میں کوئی فرق نہیں۔', 'iii. د تصادفي تېروتنې او د نمونه اخیستنې د تعصب ترمنځ توپیر نشته.'),
    ('iv. An estimator or statistic is characteristic of population.', 'iv. تخمین کار یا شماریہ آبادی کی خاصیت ہے۔', 'iv. اټکلوونکی یا احصاییه د نفوس ځانګړنه ده.'),
    ('v. The sample mean and sample standard deviation are not statistics.', 'v. نمونے کا اوسط اور نمونے کا معیاری انحراف شماریے نہیں ہیں۔', 'v. د نمونې منځنی او د نمونې معیاري انحراف احصاییې نه دي.'),
    ('vi. As the sample size increases, the S.E decreases.', 'vi. جیسے جیسے نمونے کا سائز بڑھتا ہے، معیاری غلطی کم ہوتی ہے۔', 'vi. لکه څنګه چې د نمونې اندازه زیاتېږي، معیاري تېروتنه کمېږي.'),
    ('vii. A sampling procedure that selects items for a sample at uniform intervals is called stratified random sampling.', 'vii. نمونہ گیری کا وہ طریقہ جو نمونے کے لیے اشیاء یکساں وقفوں پر منتخب کرے، طبقاتی تصادفی نمونہ گیری کہلاتا ہے۔', 'vii. د نمونه اخیستنې هغه طریقه چې د نمونې لپاره توکي په یو شان واټنونو کې ټاکي، طبقه‌بندي تصادفي نمونه اخیستنه بلل کېږي.'),
    ('viii. The probability distribution of all possible means of samples is called sampling distribution of sample mean.', 'viii. نمونوں کے تمام ممکنہ اوسطوں کی احتمالی تقسیم کو نمونے کے اوسط کی نمونہ جاتی تقسیم کہتے ہیں۔', 'viii. د نمونو د ټولو شونو منځنیو احتمالي وېش ته د نمونې د منځني نمونوي وېش وایي.'),
    ('ix. The S.E of the mean is as the S.D of the sampling distribution of the sample mean.', 'ix. اوسط کی معیاری غلطی نمونے کے اوسط کی نمونہ جاتی تقسیم کے معیاری انحراف کے برابر ہے۔', 'ix. د منځني معیاري تېروتنه د نمونې د منځني د نمونوي وېش معیاري انحراف دی.'),
    ('x. S.E can be negative.', 'x. معیاری غلطی منفی ہو سکتی ہے۔', 'x. معیاري تېروتنه منفي کېدای شي.'),
])
B = '______'
e.h('5.2 Fill in the blanks.', '5.2 خالی جگہیں پُر کریں۔', '5.2 تش ځایونه ډک کړئ.')
e.group('lines', [
    (f'i. If the number of units in a population is limited, it is known as {B} population.', f'i. اگر کسی آبادی میں اکائیوں کی تعداد محدود ہو تو اسے {B} آبادی کہتے ہیں۔', f'i. که په یوه نفوس کې د واحدونو شمېر محدود وي، {B} نفوس بلل کېږي.'),
    (f'ii. A population consisting of an unlimited number of units is called a {B} population.', f'ii. لامحدود تعداد میں اکائیوں پر مشتمل آبادی کو {B} آبادی کہتے ہیں۔', f'ii. هغه نفوس چې له بې‌حده شمېر واحدونو جوړ وي، {B} نفوس بلل کېږي.'),
    (f'iii. If all units of a population are surveyed, it is called {B}.', f'iii. اگر آبادی کی تمام اکائیوں کا سروے کیا جائے تو اسے {B} کہتے ہیں۔', f'iii. که د نفوس ټول واحدونه سروې شي، {B} بلل کېږي.'),
    (f'iv. The discrepancy between a parameter and its estimator due to sampling process is known as {B}.', f'iv. نمونہ گیری کے عمل کی وجہ سے پیرامیٹر اور اس کے تخمین کار کے درمیان فرق کو {B} کہتے ہیں۔', f'iv. د نمونه اخیستنې د بهیر له امله د پارامټر او د هغه د اټکلوونکي ترمنځ توپیر ته {B} وایي.'),
    (f'v. Standard deviation of all possible estimates from samples of fixed size is called {B}.', f'v. مقررہ سائز کے نمونوں سے تمام ممکنہ تخمینوں کے معیاری انحراف کو {B} کہتے ہیں۔', f'v. د ټاکلې اندازې له نمونو څخه د ټولو شونو اټکلونو معیاري انحراف ته {B} وایي.'),
    (f'vi. The list of all the items of a population is known as {B}.', f'vi. آبادی کی تمام اشیاء کی فہرست کو {B} کہتے ہیں۔', f'vi. د نفوس د ټولو توکو لیست ته {B} وایي.'),
])
ex = e.build('stat12-u5-exercise-a', 'Unit 5 Exercise — 5.1 and 5.2 (i)–(vi)', 'یونٹ 5 مشق — 5.1 اور 5.2 (i)–(vi)', 'واحد 5 تمرین — 5.1 او 5.2 (i)–(vi)', 97, [186])

if __name__ == '__main__':
    save(97, [(5, keys), (5, ex)])
