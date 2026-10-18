"""PDF150 printed 291–292: Unit 8 Exercise 8.19–8.23 (unit end); Unit 9 opener (learning outcomes)."""
from class12_statistics_common import Builder, save

b = Builder()


def tab(tid, heads, labels, data):
    H = [[h[i] for h in heads] for i in range(3)]
    R = [[[labels[r][i]] + data[r] for r in range(len(data))] for i in range(3)]
    b.table(tid, H[0], R[0], H[1], H[2], R[1], R[2])


ATT = ('Attributes', 'صفات', 'صفتونه')
b.p('8.19 Can we say that education depends on sex at α = 0.05 on the basis of a random sample of 300 persons classified in the following (2 × 3) contingency table:', '8.19 کیا ہم درج ذیل (2 × 3) اتفاقی جدول میں درجہ بند 300 افراد کے تصادفی نمونے کی بنیاد پر α = 0.05 پر کہہ سکتے ہیں کہ تعلیم جنس پر منحصر ہے:', '8.19 آیا د لاندې (2 × 3) احتمالي جدول کې د ډلبندي شویو 300 کسانو د تصادفي نمونې پر بنسټ په α = 0.05 ویلای شو چې زده‌کړه په جنس پورې اړه لري:')
tab('stat12-t-q8-19', [('Sex \\ Education', 'جنس \\ تعلیم', 'جنس \\ زده‌کړه'), ('middle', 'مڈل', 'منځنۍ'), ('SSC', 'SSC', 'SSC'), ('college', 'کالج', 'کالج')],
    [('male', 'مرد', 'نارینه'), ('female', 'عورت', 'ښځینه')], [['30', '45', '75'], ['75', '30', '45']])
b.p('8.20 Find the value of chi-square from the following table and test the hypothesis that there is no relation between the attributes A and B. Use α = 0.05', '8.20 درج ذیل جدول سے کائی مربع کی قیمت معلوم کریں اور اس مفروضے کی جانچ کریں کہ صفات A اور B کے درمیان کوئی تعلق نہیں۔ α = 0.05 استعمال کریں', '8.20 له لاندې جدول د کای مربع قیمت پیدا کړئ او دا فرضیه وازموئ چې د A او B صفتونو ترمنځ هېڅ اړیکه نشته. α = 0.05 وکاروئ')
tab('stat12-t-q8-20', [ATT, ('$B_1$',) * 3, ('$B_2$',) * 3, ('$B_3$',) * 3], [('$A_1$',) * 3, ('$A_2$',) * 3, ('$A_3$',) * 3], [['600', '225', '180'], ['300', '660', '320'], ['200', '275', '600']])
b.group('lines', [
    ('8.21 Discuss coefficient of mean square contingency for an (r × c) contingency table.', '8.21 (r × c) اتفاقی جدول کے لیے اوسط مربع اتفاقیت کے سر پر بحث کریں۔', '8.21 د (r × c) احتمالي جدول لپاره د منځني مربع احتمالیت پر ضریب بحث وکړئ.'),
    ('8.22 Find the Pearson’s coefficient of mean square contingency form the following table of frequencies showing the gender of customer and mode of payment for purchasing articles on a store.', '8.22 درج ذیل تعددی جدول سے، جو ایک دکان پر اشیاء خریدنے کے لیے گاہک کی جنس اور ادائیگی کا طریقہ دکھاتا ہے، پیئرسن کا اوسط مربع اتفاقیت کا سر معلوم کریں۔', '8.22 له لاندې تکراري جدول، چې په یوه پلورنځي کې د توکو د اخیستلو لپاره د پېرودونکي جنس او د تادیې طریقه ښيي، د پیرسن د منځني مربع احتمالیت ضریب پیدا کړئ.'),
])
tab('stat12-t-q8-22', [ATT, ('cash', 'نقد', 'نغدې'), ('loan', 'قرض', 'پور')], [('male', 'مرد', 'نارینه'), ('female', 'عورت', 'ښځینه')], [['431', '5'], ['291', '9']])
b.p('8.23 Calculate the coefficient of contingency from the following data showing resemblance between hair colour and eye colour:', '8.23 بالوں کے رنگ اور آنکھوں کے رنگ کی مشابہت دکھانے والے درج ذیل مواد سے اتفاقیت کا سر معلوم کریں:', '8.23 له لاندې معلوماتو چې د وېښتو د رنګ او سترګو د رنګ ورته‌والی ښيي، د احتمالیت ضریب محاسبه کړئ:')
tab('stat12-t-q8-23', [('Eye colour \\ Hair colour', 'آنکھوں کا رنگ \\ بالوں کا رنگ', 'د سترګو رنګ \\ د وېښتو رنګ'), ('black', 'سیاہ', 'تور'), ('brown', 'بھورا', 'نسواري'), ('red', 'سرخ', 'سور'), ('grey', 'سرمئی', 'خړ')],
    [('grey', 'سرمئی', 'خړې'), ('blue', 'نیلی', 'شنې'), ('brown', 'بھوری', 'نسواري')], [['1768', '807', '47', '189'], ['946', '1287', '53', '746'], ['115', '438', '6', '288']])
ex = b.build('stat12-u8-exercise-d', 'Unit 8 Exercise — 8.19 to 8.23', 'یونٹ 8 مشق — 8.19 تا 8.23', 'واحد 8 تمرین — 8.19 تر 8.23', 150, [291])

o = Builder()
o.h('Unit - 9', 'یونٹ - 9', 'واحد - 9')
o.h('Design of Experiment', 'تجربے کا ڈیزائن', 'د تجربې ډیزاین')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Describe the meaning of the design of experiment.', 'تجربے کے ڈیزائن کا مطلب بیان کریں۔', 'د تجربې د ډیزاین مانا بیان کړي.'),
    ('Explain the elements involved in designing an experiment: the experimental unit, the treatment, the replication and the response.', 'تجربے کے ڈیزائن میں شامل عناصر کی وضاحت کریں: تجرباتی اکائی، علاج (treatment)، تکرار اور ردِعمل۔', 'د تجربې په ډیزاین کې شامل عناصر تشریح کړي: تجربوي واحد، درملنه (treatment)، تکرار او غبرګون.'),
    ('Define randomization, completely randomized design.', 'تصادفیت اور مکمل تصادفی ڈیزائن کی تعریف کریں۔', 'تصادفي کول او بشپړ تصادفي ډیزاین تعریف کړي.'),
    ('Give layout plan of completely randomized design.', 'مکمل تصادفی ڈیزائن کا خاکہ پیش کریں۔', 'د بشپړ تصادفي ډیزاین نقشه وړاندې کړي.'),
    ('Identify the merits and demerits of completely randomized design.', 'مکمل تصادفی ڈیزائن کی خوبیاں اور خامیاں پہچانیں۔', 'د بشپړ تصادفي ډیزاین ګټې او نیمګړتیاوې وپېژني.'),
    ('Know the meaning of analysis of variance.', 'تجزیۂ تغیر کا مطلب جانیں۔', 'د واریانس د تحلیل مانا وپېژني.'),
    ('State the assumptions of analysis of variance.', 'تجزیۂ تغیر کے مفروضات بیان کریں۔', 'د واریانس د تحلیل فرضیې بیان کړي.'),
    ('Describe and calculate: the total sum of squares, the treatment sum of squares, and the error sum of squares.', 'بیان کریں اور حساب لگائیں: مربعوں کا کل مجموعہ، علاج کے مربعوں کا مجموعہ اور خطا کے مربعوں کا مجموعہ۔', 'بیان او محاسبه کړي: د مربعو ټوله مجموعه، د درملنې د مربعو مجموعه او د تېروتنې د مربعو مجموعه.'),
    ('Describe and calculate the degrees of freedom for: the total sum of squares, the treatment sum of squares and the error sum of squares.', 'درج ذیل کے درجاتِ آزادی بیان کریں اور حساب لگائیں: مربعوں کا کل مجموعہ، علاج کے مربعوں کا مجموعہ اور خطا کے مربعوں کا مجموعہ۔', 'د لاندې لپاره د ازادۍ درجې بیان او محاسبه کړي: د مربعو ټوله مجموعه، د درملنې د مربعو مجموعه او د تېروتنې د مربعو مجموعه.'),
    ('Describe and calculate the treatment mean square, the error mean square. Test the equality of means of several normal populations.', 'علاج کا اوسط مربع اور خطا کا اوسط مربع بیان کریں اور حساب لگائیں۔ کئی نارمل آبادیوں کے اوسطوں کی برابری کی جانچ کریں۔', 'د درملنې منځنی مربع او د تېروتنې منځنی مربع بیان او محاسبه کړي. د څو نورمالو نفوسونو د منځنیو برابري وازمويي.'),
])
op = o.build('stat12-u9-opener', 'Unit 9 — Design of Experiment: learning outcomes', 'یونٹ 9 — تجربے کا ڈیزائن: تعلیمی نتائج', 'واحد 9 — د تجربې ډیزاین: د زده کړې پایلې', 150, [292])

if __name__ == '__main__':
    save(150, [(8, ex), (9, op)], complete_units=[8])
