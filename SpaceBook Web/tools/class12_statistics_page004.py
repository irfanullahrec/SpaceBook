"""PDF4: credits page and Table of Content."""
from class12_statistics_common import Builder, save

b = Builder()
b.p('All rights reserved with the University Books Printers & Publishers, Peshawar',
    'جملہ حقوق یونیورسٹی بکس پرنٹرز اینڈ پبلشرز، پشاور کے نام محفوظ ہیں',
    'ټول حقوق د یونیورسټي بُکس پرنټرز او پبلشرز، پېښور سره خوندي دي')
b.p('Developed by University Books Printers & Publishers, Peshawar and approved by The Directorate of Curriculum & Teacher Education (DCTE), Abbottabad vide NOC No.5400-5402/F.03/Vol-I/Statistics-XII dated 08-10-2018.',
    'تیار کردہ: یونیورسٹی بکس پرنٹرز اینڈ پبلشرز، پشاور؛ منظور شدہ: ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن (DCTE)، ایبٹ آباد، بذریعہ NOC نمبر 5400-5402/F.03/Vol-I/Statistics-XII مورخہ 08-10-2018۔',
    'جوړوونکی: یونیورسټي بُکس پرنټرز او پبلشرز، پېښور؛ تاییدوونکی: د نصاب او ښوونکو د روزنې ریاست (DCTE)، ایبټ اباد، د NOC شمېره 5400-5402/F.03/Vol-I/Statistics-XII نېټه 08-10-2018.')
rows = [
    ('Author:', 'Prof. Jamal Shah, Principal, Govt. Degree College, Zaida, Swabi.',
     'مصنف:', 'پروفیسر جمال شاہ، پرنسپل، گورنمنٹ ڈگری کالج، زیدہ، صوابی۔',
     'لیکوال:', 'پروفېسر جمال شاه، پرنسپل، دولتي ډګري کالج، زیده، صوابۍ.'),
    ('Review Supervision:', 'Gohar Ali Khan, Director, Curriculum & Teacher Education Khyber Pakhtunkhwa Abbottabad',
     'نگرانِ نظرِ ثانی:', 'گوہر علی خان، ڈائریکٹر، کریکولم اینڈ ٹیچر ایجوکیشن خیبر پختونخوا، ایبٹ آباد',
     'د بیاکتنې څارنه:', 'ګوهر علي خان، رییس، د نصاب او ښوونکو روزنه، خیبر پښتونخوا، ایبټ اباد'),
    ('Focal person:', 'Zulfiqar Khan, Additional Director, Curriculum & Textbook Review, DCTE Abbottabad',
     'فوکل پرسن:', 'ذوالفقار خان، ایڈیشنل ڈائریکٹر، کریکولم اینڈ ٹیکسٹ بک ریویو، DCTE ایبٹ آباد',
     'اصلي اړیکه نیوونکی:', 'ذوالفقار خان، مرستیال رییس، د نصاب او درسي کتابونو بیاکتنه، DCTE ایبټ اباد'),
]
for en_l, en_v, ur_l, ur_v, ps_l, ps_v in rows:
    b.p(f'{en_l} {en_v}', f'{ur_l} {ur_v}', f'{ps_l} {ps_v}')
b.h('Reviewers:', 'نظرِ ثانی کنندگان:', 'بیاکتونکي:')
b.group('list', [
    ('Mr. Zia Shahid, Principal, GHS No. 3, Abbottabad.', 'جناب ضیاء شاہد، پرنسپل، گورنمنٹ ہائی سکول نمبر 3، ایبٹ آباد۔', 'ښاغلی ضیاء شاهد، پرنسپل، دولتي عالي ښوونځی شمېره 3، ایبټ اباد.'),
    ('Mr. Majid Khan, Assistant Professor, GPGC No. 1, Abbottabad.', 'جناب ماجد خان، اسسٹنٹ پروفیسر، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد۔', 'ښاغلی ماجد خان، اسسټنټ پروفېسر، دولتي پوسټ ګرېجوېټ کالج شمېره 1، ایبټ اباد.'),
    ('Mr. Iftikhar Hussain, Senior Subject Specialist GHSS Nawashehr, Abbottabad.', 'جناب افتخار حسین، سینئر سبجیکٹ اسپیشلسٹ، گورنمنٹ ہائر سیکنڈری سکول نواں شہر، ایبٹ آباد۔', 'ښاغلی افتخار حسین، لوړ رتبه مضمون پوه، دولتي لوړ ثانوي ښوونځی نواں ښار، ایبټ اباد.'),
    ('Ms. Samia Danish, (Desk Officer), DCTE, Abbottabad.', 'محترمہ سامعہ دانش، (ڈیسک آفیسر)، DCTE، ایبٹ آباد۔', 'مېرمن سامعه دانش، (ډېسک افسر)، DCTE، ایبټ اباد.'),
    ('Mr. Shakeel Iqbal, Subject Specialist, KP Textbook Board, Peshawar', 'جناب شکیل اقبال، سبجیکٹ اسپیشلسٹ، کے پی ٹیکسٹ بک بورڈ، پشاور', 'ښاغلی شکیل اقبال، مضمون پوه، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
])
b.p('Editor: Mr. Shakeel Iqbal, Subject Specialist, Khyber Pakhtunkhwa Textbook Board Peshawar',
    'مدیر: جناب شکیل اقبال، سبجیکٹ اسپیشلسٹ، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور',
    'سمونګر: ښاغلی شکیل اقبال، مضمون پوه، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
b.h('Printing Supervision:', 'نگرانِ طباعت:', 'د چاپ څارنه:')
b.group('list', [
    ('Mr. Zakir Hussain Afridi, Chairman', 'جناب ذاکر حسین آفریدی، چیئرمین', 'ښاغلی ذاکر حسین اپریدی، رییس'),
    ('Mr. Saeedur Rehman, Member (E&P) Khyber Pakhtunkhwa Textbook Board, Peshawar', 'جناب سعید الرحمٰن، ممبر (E&P)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'ښاغلی سعیدالرحمن، غړی (E&P)، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
])
b.group('lines', [
    ('Academic Year 2019-20', 'تعلیمی سال 2019-20', 'تعلیمي کال 2019-20'),
    ('Website: www.kptbb.gov.pk', 'ویب سائٹ: www.kptbb.gov.pk', 'وېبپاڼه: www.kptbb.gov.pk'),
    ('Email: membertbb@yahoo.com', 'ای میل: membertbb@yahoo.com', 'برېښنالیک: membertbb@yahoo.com'),
    ('Phone: 091- 9217159-60', 'فون: 091- 9217159-60', 'ټیلیفون: 091- 9217159-60'),
])
credits = b.build('stat12-credits', 'Credits', 'اعترافات و تفصیلاتِ اشاعت', 'د خپرونې جزئیات', 4, ['iii'])

c = Builder()
c.h('Table of Content', 'فہرستِ مضامین', 'د منځپانګې لړلیک')
units = [('1.', 'Probability', 'احتمال', 'احتمال', '1'),
         ('2.', 'Random Variables and Probability Distributions', 'تصادفی متغیرات اور احتمالی تقسیمیں', 'تصادفي متغیرونه او احتمالي وېشونه', '31'),
         ('3.', 'Special Discrete Probability Distributions', 'خاص منفصل احتمالی تقسیمیں', 'ځانګړي منفصل احتمالي وېشونه', '70'),
         ('4.', 'Special Continuous Probability Distributions', 'خاص مسلسل احتمالی تقسیمیں', 'ځانګړي متصل احتمالي وېشونه', '116'),
         ('5.', 'Sampling and Sampling Distributions', 'نمونہ گیری اور نمونہ جاتی تقسیمیں', 'نمونه اخیستنه او نمونوي وېشونه', '151'),
         ('6.', 'Estimation', 'تخمین', 'اټکل', '193'),
         ('7.', 'Hypothesis Testing', 'مفروضے کی جانچ', 'د فرضیې ازموینه', '231'),
         ('8.', 'Association of Attributes', 'صفات کا باہمی تعلق', 'د صفتونو اړیکه', '266'),
         ('9.', 'Design of Experiment', 'تجربے کا خاکہ', 'د تجربې ډیزاین', '292'),
         ('A', 'Answers to Exercises', 'مشقوں کے جوابات', 'د تمرینونو ځوابونه', '320'),
         ('G', 'Glossary', 'فرہنگ', 'لغتنامه', '331'),
         ('I', 'Index', 'اشاریہ', 'اشاریه', '338')]
c.table('stat12-contents', ['Unit No.', 'Subject', 'Page No.'], [[u, e, p] for u, e, _, _, p in units],
        ['یونٹ نمبر', 'مضمون', 'صفحہ نمبر'], ['د واحد شمېره', 'موضوع', 'د مخ شمېره'],
        [[u, ur, p] for u, _, ur, _, p in units], [[u, ps, p] for u, _, _, ps, p in units])
contents = c.build('stat12-contents-page', 'Table of Content', 'فہرستِ مضامین', 'د منځپانګې لړلیک', 4, ['iv'])

if __name__ == '__main__':
    save(4, [(1, credits), (1, contents)])
