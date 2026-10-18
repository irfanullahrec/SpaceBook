"""PDF137 printed 265–266: Unit 7 Exercise 7.26–7.30 (unit end); Unit 8 opener (learning outcomes)."""
from class12_statistics_common import Builder, save

b = Builder()
b.group('lines', [
    ('7.26 Blood donation society of a college claimed that 5% of the students in our college make blood donation during a given year. If in a random sample 10 of 250 students have given blood during the past year. Test $H_0:p=0.05$ against $H_1:p\\neq 0.05$ with α = 0.05.', '7.26 ایک کالج کی خون عطیہ کرنے والی سوسائٹی نے دعویٰ کیا کہ ہمارے کالج کے 5% طلبہ ایک سال کے دوران خون عطیہ کرتے ہیں۔ اگر ایک تصادفی نمونے میں 250 میں سے 10 طلبہ نے گزشتہ سال خون دیا ہو۔ α = 0.05 کے ساتھ $H_1:p\\neq 0.05$ کے مقابلے میں $H_0:p=0.05$ کی جانچ کریں۔', '7.26 د یوه کالج د وینې ورکولو ټولنې ادعا وکړه چې زموږ د کالج 5% زده کوونکي په یوه ټاکلي کال کې وینه ورکوي. که په یوه تصادفي نمونه کې له 250 زده کوونکو 10 تېر کال وینه ورکړې وي. د α = 0.05 سره د $H_1:p\\neq 0.05$ پر وړاندې $H_0:p=0.05$ وازموئ.'),
    ('7.27 An electric company claimed that at least 85% of the parts which it supplied confirmed to specifications. A sample of 400 parts was tested and 75 did not meet specifications. Can we accept the company’s claim at 1% level of significance?', '7.27 ایک برقی کمپنی نے دعویٰ کیا کہ اس کے فراہم کردہ پرزوں میں سے کم از کم 85% وضاحتوں کے مطابق ہیں۔ 400 پرزوں کے نمونے کی جانچ کی گئی اور 75 وضاحتوں پر پورے نہ اترے۔ کیا ہم 1% معنویت کی سطح پر کمپنی کا دعویٰ قبول کر سکتے ہیں؟', '7.27 یوه برېښنایي شرکت ادعا وکړه چې د هغه د برابرو شویو پرزو لږ تر لږه 85% له مشخصاتو سره سم دي. د 400 پرزو نمونه وازمویل شوه او 75 له مشخصاتو سره سم نه وو. آیا د 1% معنی‌داریت په کچه د شرکت ادعا منلی شو؟'),
    ('7.28 Describe the steps used in hypothesis testing about difference of two population proportions in case of large samples.', '7.28 بڑے نمونوں کی صورت میں دو آبادیوں کے تناسبات کے فرق کے بارے میں مفروضے کی جانچ میں استعمال ہونے والے مراحل بیان کریں۔', '7.28 د لویو نمونو په حالت کې د دوو نفوسونو د تناسبونو د توپیر په اړه د فرضیې په ازموینه کې کارېدونکي ګامونه بیان کړئ.'),
    ('7.29 Test the hypothesis that proportions of men and women favoring a political candidate are different on the basis of a sample survey in which 225 of 500 men and 275 of 500 women favor the candidate. Test at 5% level of significance.', '7.29 ایک نمونہ سروے کی بنیاد پر، جس میں 500 میں سے 225 مرد اور 500 میں سے 275 عورتیں امیدوار کی حمایت کرتی ہیں، اس مفروضے کی جانچ کریں کہ ایک سیاسی امیدوار کی حمایت کرنے والے مردوں اور عورتوں کے تناسب مختلف ہیں۔ 5% معنویت کی سطح پر جانچ کریں۔', '7.29 د یوې نمونوي سروې پر بنسټ، چې پکې له 500 نارینه وو 225 او له 500 ښځو 275 د نوماند ملاتړ کوي، دا فرضیه وازموئ چې د یوه سیاسي نوماند د ملاتړ کوونکو نارینه وو او ښځو تناسبونه بېلابېل دي. د 5% معنی‌داریت په کچه وازموئ.'),
    ('7.30 In a random table of 600 persons from a certain large city 450 are found to be smokers. In another sample of 900 persons from another large city 450 are smokers. Test at α = 0.01 that the two cities are significantly different with respect to the prevalence of smoking.', '7.30 ایک بڑے شہر کے 600 افراد کے تصادفی جدول میں 450 تمباکو نوش پائے گئے۔ ایک دوسرے بڑے شہر کے 900 افراد کے دوسرے نمونے میں 450 تمباکو نوش ہیں۔ α = 0.01 پر جانچ کریں کہ دونوں شہر تمباکو نوشی کے پھیلاؤ کے لحاظ سے معنی خیز طور پر مختلف ہیں۔', '7.30 د یوه ټاکلي لوی ښار د 600 کسانو په تصادفي جدول کې 450 سګرټ څکوونکي وموندل شول. د بل لوی ښار د 900 کسانو په بله نمونه کې 450 سګرټ څکوونکي دي. په α = 0.01 وازموئ چې دواړه ښارونه د سګرټ څکولو د خپرېدو له پلوه په معنی‌دار ډول توپیر لري.'),
])
ex = b.build('stat12-u7-exercise-d', 'Unit 7 Exercise — 7.26 to 7.30', 'یونٹ 7 مشق — 7.26 تا 7.30', 'واحد 7 تمرین — 7.26 تر 7.30', 137, [265])

o = Builder()
o.h('Unit - 8', 'یونٹ - 8', 'واحد - 8')
o.h('Association of Attributes', 'صفات کا تلازم', 'د صفتونو تړاو')
o.p('After studying this unit, the students will be able to', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې')
o.group('list', [
    ('Recall variable and attribute.', 'متغیر اور صفت کو یاد کریں۔', 'متغیر او صفت را په یاد کړي.'),
    ('Recognize the notation and terminology to represent the presence and absence of attributes.', 'صفات کی موجودگی اور غیر موجودگی ظاہر کرنے کے لیے علامات اور اصطلاحات پہچانیں۔', 'د صفتونو د شتون او نشتوالي د ښودلو لپاره نښې او اصطلاحګانې وپېژني.'),
    ('Describe class and class frequency.', 'جماعت اور جماعت کا تعدد بیان کریں۔', 'ټولګی او د ټولګي تکرار بیان کړي.'),
    ('Recognize the categorical data of two attributes.', 'دو صفات کے زمرہ وار مواد کو پہچانیں۔', 'د دوو صفتونو کټګوریکي معلومات وپېژني.'),
    ('Explain independence of two attributes.', 'دو صفات کی آزادی کی وضاحت کریں۔', 'د دوو صفتونو خپلواکي تشریح کړي.'),
    ('Know the criterion of independence of two attributes.', 'دو صفات کی آزادی کا معیار جانیں۔', 'د دوو صفتونو د خپلواکۍ معیار وپېژني.'),
    ('Discuss the association of two attributes; positive association, negative association, complete association and complete disassociation.', 'دو صفات کے تلازم پر بحث کریں؛ مثبت تلازم، منفی تلازم، مکمل تلازم اور مکمل عدم تلازم۔', 'د دوو صفتونو پر تړاو بحث وکړي؛ مثبت تړاو، منفي تړاو، بشپړ تړاو او بشپړ بې‌تړاوي.'),
    ('Define Yule’s coefficient of association.', 'یول کے تلازم کے سر کی تعریف کریں۔', 'د یول د تړاو ضریب تعریف کړي.'),
    ('Find the coefficient of association and interpret its result.', 'تلازم کا سر معلوم کریں اور اس کے نتیجے کی تشریح کریں۔', 'د تړاو ضریب پیدا او پایله یې تفسیر کړي.'),
    ('Define contingency table.', 'اتفاقی جدول کی تعریف کریں۔', 'احتمالي جدول تعریف کړي.'),
    ('Test whether two attributes in a given contingency table are statistically independent or not.', 'جانچ کریں کہ دیے گئے اتفاقی جدول میں دو صفات شماریاتی طور پر آزاد ہیں یا نہیں۔', 'وازمويي چې آیا په ورکړل شوي احتمالي جدول کې دوه صفتونه په احصاییوي ډول خپلواک دي که نه.'),
    ('Describe Pearson’s coefficient of mean square contingencies.', 'پیئرسن کے اوسط مربع اتفاقیت کے سر کو بیان کریں۔', 'د پیرسن د منځني مربع احتمالیت ضریب بیان کړي.'),
    ('Calculate Pearson’s co efficient of mean square contingency for a given contingency table and find its maximum value.', 'دیے گئے اتفاقی جدول کے لیے پیئرسن کے اوسط مربع اتفاقیت کا سر معلوم کریں اور اس کی زیادہ سے زیادہ قیمت معلوم کریں۔', 'د ورکړل شوي احتمالي جدول لپاره د پیرسن د منځني مربع احتمالیت ضریب محاسبه او د هغه اعظمي قیمت پیدا کړي.'),
    ('Describe and apply Yule’s correction for continuity to test the statistical independence of two given attributes.', 'دو دیے گئے صفات کی شماریاتی آزادی کی جانچ کے لیے یول کی تسلسل کی اصلاح بیان کریں اور لاگو کریں۔', 'د دوو ورکړل شویو صفتونو د احصاییوي خپلواکۍ د ازموینې لپاره د یول د پرلپسې‌والي سمون بیان او پلي کړي.'),
])
opening = o.build('stat12-u8-opener', 'Unit 8 — Association of Attributes: learning outcomes', 'یونٹ 8 — صفات کا تلازم: تعلیمی نتائج', 'واحد 8 — د صفتونو تړاو: د زده کړې پایلې', 137, [266])
issues = [{'id': 'stat12-p265-typos', 'unit': 7, 'printedPage': 265, 'description': 'Exercise 7.27 prints “confirmed to specifications” (for “conformed”) and 7.30 “In a random table of 600 persons” (for “random sample”); printed wording retained.'}]

if __name__ == '__main__':
    save(137, [(7, ex), (8, opening)], issues=issues, complete_units=[7])
