"""PDF161 printed 313–314: Unit 9 Exercise 9.1 (T/F), 9.2 (blanks), 9.3 MCQs (i)–(vii)."""
from class12_statistics_common import Builder, save

B = '______'
b = Builder()
b.h('Exercise', 'مشق', 'تمرین')
b.h('9.1 Read the following statements carefully and indicate which statement is true or false.', '9.1 درج ذیل بیانات غور سے پڑھیں اور بتائیں کہ کون سا بیان درست یا غلط ہے۔', '9.1 لاندې بیانونه په غور ولولئ او وښایاست چې کوم بیان سم یا ناسم دی.')
b.group('lines', [
    ('i. F-distribution is a ratio of sample variances.', 'i. F-تقسیم نمونوں کے تغیرات کی نسبت ہے۔', 'i. F-وېش د نمونو د واریانسونو نسبت دی.'),
    ('ii. ANOVA is a useful technique for testing hypothesis about several means.', 'ii. ANOVA کئی اوسطوں کے بارے میں مفروضے کی جانچ کے لیے مفید تکنیک ہے۔', 'ii. ANOVA د څو منځنیو په اړه د فرضیې د ازموینې لپاره ګټوره تخنیک ده.'),
    ('iii. In ANOVA sample sizes must always be equal.', 'iii. ANOVA میں نمونوں کے سائز ہمیشہ برابر ہونے چاہییں۔', 'iii. په ANOVA کې د نمونو اندازې باید تل برابرې وي.'),
    ('iv. In ANOVA it is assumed that the populations from which samples are drawn are normally distributed', 'iv. ANOVA میں فرض کیا جاتا ہے کہ جن آبادیوں سے نمونے لیے جاتے ہیں وہ نارمل تقسیم شدہ ہیں', 'iv. په ANOVA کې فرض کېږي چې هغه نفوسونه چې نمونې ترې اخیستل کېږي نورمال وېش لري'),
    ('v. F-test is used in ANOVA to test the null hypothesis about several means.', 'v. ANOVA میں کئی اوسطوں کے بارے میں صفری مفروضے کی جانچ کے لیے F-جانچ استعمال ہوتی ہے۔', 'v. په ANOVA کې د څو منځنیو په اړه د صفري فرضیې د ازموینې لپاره F-ازموینه کارول کېږي.'),
    ('vi. The range of F-distribution is from 0 to ∞.', 'vi. F-تقسیم کی حد 0 سے ∞ تک ہے۔', 'vi. د F-وېش حد له 0 تر ∞ دی.'),
    ('vii. The plan of an experiment which controls all factors, as much as possible except the treatment is called design of experiment.', 'vii. تجربے کا وہ منصوبہ جو علاج کے علاوہ تمام عوامل کو جہاں تک ممکن ہو قابو کرے، تجربے کا ڈیزائن کہلاتا ہے۔', 'vii. د تجربې هغه پلان چې د درملنې پرته ټول عوامل تر وسه وسه کنټرولوي، د تجربې ډیزاین بلل کېږي.'),
    ('viii. Larger the experimental error, more efficient is the design.', 'viii. تجرباتی خطا جتنی زیادہ ہو، ڈیزائن اتنا زیادہ مؤثر ہے۔', 'viii. تجربوي تېروتنه څومره لویه وي، ډیزاین هومره موثر دی.'),
    ('ix. A completely randomized design is used when all experimental units are homogeneous.', 'ix. مکمل تصادفی ڈیزائن اس وقت استعمال ہوتا ہے جب تمام تجرباتی اکائیاں یکساں ہوں۔', 'ix. بشپړ تصادفي ډیزاین هغه وخت کارول کېږي چې ټول تجربوي واحدونه همجنسه وي.'),
    ('x. Missing observation in a CRD creates a serious problem.', 'x. CRD میں گمشدہ مشاہدہ سنگین مسئلہ پیدا کرتا ہے۔', 'x. په CRD کې ورکه مشاهده جدي ستونزه پیدا کوي.'),
])
b.h('9.2 Fill in the blanks.', '9.2 خالی جگہیں پُر کریں۔', '9.2 تش ځایونه ډک کړئ.')
b.group('lines', [
    (f'i. A subject receiving a treatment in an experiment is called {B}.', f'i. تجربے میں علاج پانے والا موضوع {B} کہلاتا ہے۔', f'i. په تجربه کې درملنه ترلاسه کوونکی موضوع {B} بلل کېږي.'),
    (f'ii The allocation of treatments to experimental units with equal probability is known as {B}.', f'ii تجرباتی اکائیوں کو برابر احتمال کے ساتھ علاج کی تفویض {B} کہلاتی ہے۔', f'ii تجربوي واحدونو ته د برابر احتمال سره د درملنو ورکول {B} بلل کېږي.'),
    (f'iii. The number of times a treatment is repeated in an experiment is called its {B}.', f'iii. تجربے میں کسی علاج کے دہرائے جانے کی تعداد اس کا {B} کہلاتی ہے۔', f'iii. په تجربه کې د یوې درملنې د تکرار شمېر د هغې {B} بلل کېږي.'),
    (f'iv. Experimental error is the error caused by {B}.', f'iv. تجرباتی خطا وہ خطا ہے جو {B} سے پیدا ہو۔', f'iv. تجربوي تېروتنه هغه تېروتنه ده چې د {B} له امله رامنځته شي.'),
    (f'v. Smaller the experimental error, more {B} is the design.', f'v. تجرباتی خطا جتنی کم ہو، ڈیزائن اتنا {B} ہے۔', f'v. تجربوي تېروتنه څومره کوچنۍ وي، ډیزاین هومره {B} دی.'),
    (f'vi. ANOVA splits the total variance is into {B}.', f'vi. ANOVA کل تغیر کو {B} میں تقسیم کرتا ہے۔', f'vi. ANOVA ټول واریانس په {B} وېشي.'),
    (f'vii. Missing observation in a completely randomized design creates {B}.', f'vii. مکمل تصادفی ڈیزائن میں گمشدہ مشاہدہ {B} پیدا کرتا ہے۔', f'vii. په بشپړ تصادفي ډیزاین کې ورکه مشاهده {B} پیدا کوي.'),
    (f'viii. Error sum of squares {B} be negative.', f'viii. خطا کے مربعوں کا مجموعہ منفی {B} ہو سکتا۔', f'viii. د تېروتنې د مربعو مجموعه منفي {B} کېدای.'),
    (f'ix. The average performance of a treatment is better reflected through {B}.', f'ix. کسی علاج کی اوسط کارکردگی {B} کے ذریعے بہتر ظاہر ہوتی ہے۔', f'ix. د یوې درملنې منځنی فعالیت د {B} له لارې ښه منعکس کېږي.'),
    (f'x. The designs of experiments were originated mainly for {B}.', f'x. تجربات کے ڈیزائن بنیادی طور پر {B} کے لیے شروع ہوئے۔', f'x. د تجربو ډیزاینونه اساساً د {B} لپاره رامنځته شول.'),
])
b.h('9.3 Choose the correct answer.', '9.3 درست جواب منتخب کریں۔', '9.3 سم ځواب وټاکئ.')
b.mcq('i.', ('An experimental design is', 'تجرباتی ڈیزائن ہے', 'تجربوي ډیزاین دی'), [('An architect', 'ایک معمار', 'یو معمار'), ('a map', 'ایک نقشہ', 'یوه نقشه'), ('a plan of experiment', 'تجربے کا منصوبہ', 'د تجربې پلان'), ('all of the above', 'مندرجہ بالا سب', 'پورتني ټول')])
b.mcq('ii.', ('Randomization is a process in which the treatments are allocated to the experimental units:', 'تصادفیت ایک عمل ہے جس میں علاج تجرباتی اکائیوں کو تفویض کیے جاتے ہیں:', 'تصادفي کول یو بهیر دی چې پکې درملنې تجربوي واحدونو ته ورکول کېږي:'),
      [('In a sequence', 'ترتیب سے', 'په ترتیب'), ('at the will of the investigator', 'محقق کی مرضی سے', 'د څېړونکي په خوښه'), ('With equal probability', 'برابر احتمال کے ساتھ', 'د برابر احتمال سره'), ('with unequal probability', 'غیر برابر احتمال کے ساتھ', 'د نابرابر احتمال سره')])
b.mcq('iii.', ('Replication in an experiment means:', 'تجربے میں تکرار کا مطلب ہے:', 'په تجربه کې تکرار مانا لري:'),
      [('The number of times a treatment occurs in an experiment', 'تجربے میں کسی علاج کے آنے کی تعداد', 'په تجربه کې د یوې درملنې د راتلو شمېر'), ('The numbers of blocks', 'بلاکوں کی تعداد', 'د بلاکونو شمېر'), ('Total number of treatments', 'علاج کی کل تعداد', 'د درملنو ټول شمېر'), ('The reduction of blocks', 'بلاکوں میں کمی', 'د بلاکونو کمښت')], per_line=1)
b.mcq('iv.', ('Local control is a method to maintain', 'مقامی کنٹرول برقرار رکھنے کا طریقہ ہے', 'سیمه‌ییز کنټرول د ساتلو طریقه ده'),
      [('Homogeneity among blocks', 'بلاکوں کے درمیان یکسانیت', 'د بلاکونو ترمنځ همجنسیت'), ('Homogeneity within blocks', 'بلاکوں کے اندر یکسانیت', 'د بلاکونو دننه همجنسیت'), ('both (a) and (b)', '(a) اور (b) دونوں', '(a) او (b) دواړه'), ('all of the above', 'مندرجہ بالا سب', 'پورتني ټول')])
b.mcq('v.', ('Experimental error is due to', 'تجرباتی خطا کی وجہ ہے', 'تجربوي تېروتنه له امله ده'),
      [('Variation in treatment effects', 'علاج کے اثرات میں تغیر', 'د درملنې په اغېزو کې تغیر'), ('extraneous factors', 'خارجی عوامل', 'بهرني عوامل'), ('Experimenter’s mistake', 'تجربہ کرنے والے کی غلطی', 'د تجربه کوونکي غلطي'), ('lack of experience', 'تجربے کی کمی', 'د تجربې کمښت')])
b.mcq('vi.', ('Completely randomized designs are mostly used in', 'مکمل تصادفی ڈیزائن زیادہ تر استعمال ہوتے ہیں', 'بشپړ تصادفي ډیزاینونه ډېری کارول کېږي په'),
      [('Pot experiments', 'گملوں کے تجربات', 'د ګملو تجربو'), ('Experiments on animals', 'جانوروں پر تجربات', 'پر حیواناتو تجربو'), ('Field experiments', 'کھیت کے تجربات', 'ځمکنیو تجربو'), ('all of the above', 'مندرجہ بالا سب', 'پورتني ټول')])
b.mcq('vii.', ('An experimental unit in a research work is', 'تحقیقی کام میں تجرباتی اکائی ہے', 'په څېړنیز کار کې تجربوي واحد دی'),
      [('A patient', 'ایک مریض', 'یو ناروغ'), ('A field plots', 'کھیت کا قطعہ', 'د ځمکې ټوټه'), ('An animal', 'ایک جانور', 'یو حیوان'), ('All of the above', 'مندرجہ بالا سب', 'پورتني ټول')])
ex = b.build('stat12-u9-exercise-a', 'Unit 9 Exercise — 9.1, 9.2, 9.3 (i)–(vii)', 'یونٹ 9 مشق — 9.1، 9.2، 9.3 (i)–(vii)', 'واحد 9 تمرین — 9.1، 9.2، 9.3 (i)–(vii)', 161, [313, 314])

if __name__ == '__main__':
    save(161, [(9, ex)])
