"""HPE XII front matter: PDF1 cover; PDF2 download-site advertisement (excluded, no record); PDF3 Quranic verse page; PDF4 imprint; PDF5 contents.
Run: python class12_hpe_page001.py N (1, 3, 4, 5)."""
import sys
from class12_hpe_common import BOOK, Builder

FM = ('Front matter', 'ابتدائیہ', 'سریزه')
BANNER = ('The download-site banners (“awaz e inqilab.com”) at the top and bottom of every scan and the diagonal watermark are third-party additions '
          'and are excluded throughout the book.')


def p1():
    b = Builder()
    b.h('Health and Physical Education — for Class Twelve', 'صحت و جسمانی تعلیم — برائے بارھویں جماعت', 'روغتیا او فزیکي زده‌کړه — د دولسم ټولګي لپاره')
    b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
    b.p('FREE FROM GOVT — NOT FOR SALE', 'FREE FROM GOVT — NOT FOR SALE', 'FREE FROM GOVT — NOT FOR SALE')
    b.paras[-1]['untranslatedByDesign'] = True
    r = BOOK.record(b, 'hpe12-fm-cover', 'Front cover', 'سرورق', 'پښتۍ', 1, [None], unit_title=FM)
    r['sourceCoverIllustrationReview'] = 'Cover artwork (coloured silhouettes of athletes) and the Board logo are decorative; not reproduced.'
    BOOK.save(1, [('FM', r)], issues=[{'id': 'hpe12-pdf001', 'unit': 'FM', 'printedPage': None, 'description': BANNER + ' A pencilled owner signature on the cover is excluded.'}])


def p3():
    b = Builder()
    b.p('The believers are but brothers, so make peace between your two brothers, and fear Allah so that you may be shown mercy. (Surah Al-Hujurat: 10)',
        'مومن تو آپس میں بھائی بھائی ہیں۔ پس تو اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحم کیا جائے۔ (سورۃ الحجرات: ۱۰)',
        'مومنان خو سره ورونه دي، نو د خپلو دوو ورونو ترمنځ روغه وکړئ او له الله وډار اوسئ ترڅو پر تاسو رحم وشي. (سورة الحجرات: ۱۰)')
    r = BOOK.record(b, 'hpe12-fm-verse', 'Quranic verse', 'آیتِ مبارکہ', 'مبارکه آیت', 3, [None])
    BOOK.save(3, [('FM', r)], issues=[{'id': 'hpe12-pdf003', 'unit': 'FM', 'printedPage': None,
               'description': 'The upper third and lower margin of this page carry extensive owner handwriting (names, scribbles and ballpoint doodles); all excluded. The floral border is decorative.'}])


def p4():
    b = Builder()
    b.h('All rights reserved with University Book Publishers, Peshawar', 'جملہ حقوق بحق یونیورسٹی بک پبلشرز، پشاور محفوظ ہیں۔', 'ټول حقونه یونیورسټي بک پبلشرز، پېښور ته خوندي دي.')
    for x in [
        ('Approved by: Letter No. 6347-50/F.03/Vol-I/HPE-XII (UBP), dated 28-11-2018', 'منظور کردہ: مراسلہ نمبر: No. 6347-50/F.03/Vol-I/HPE-XII (UBP) مورخہ: 28-11-2018', 'منظور شوی: لیک شمېره No. 6347-50/F.03/Vol-I/HPE-XII (UBP)، نېټه 28-11-2018'),
        ('Authors:', 'مصنفین:', 'لیکوالان:'),
    ]:
        b.p(*x)
    b.group('list', [
        ('Malik Asif (Gold Medalist): former Chairman, Health and Physical Education Department, Government Post Graduate College No. 1, Abbottabad', 'ملک آصف: (گولڈ میڈلسٹ) سابقہ چیئرمین ہیلتھ اینڈ فزیکل ایجوکیشن ڈیپارٹمنٹ، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد', 'ملک آصف (د سرو زرو مډال ګټونکی): د روغتیا او فزیکي زده‌کړې څانګې پخوانی مشر، حکومتي پوسټ ګرېجوېټ کالج ۱ شمېره، ایبټ آباد'),
        ('Rasheedullah: Lecturer, Government College Sherwan, Abbottabad', 'رشید اللہ: لیکچرر، گورنمنٹ کالج شیر وان، ایبٹ آباد', 'رشیدالله: لکچرر، حکومتي کالج شېروان، ایبټ آباد'),
        ('Samiullah Marwat: S.I.P.E, Government Higher Secondary School Nawan Shehr, Abbottabad', 'سمیع اللہ مروت: S.I.P.E گورنمنٹ ہائیر سیکنڈری سکول نواں شہر، ایبٹ آباد', 'سمیع‌الله مروت: S.I.P.E، حکومتي عالي ثانوي ښوونځی نواں ښار، ایبټ آباد'),
        ('Arif Ali Shah: Chairman, Health and Physical Education Department, Government Post Graduate College No. 1, Abbottabad', 'عارف علی شاہ: چیئرمین ہیلتھ اینڈ فزیکل ایجوکیشن ڈیپارٹمنٹ، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد', 'عارف علي شاه: د روغتیا او فزیکي زده‌کړې څانګې مشر، حکومتي پوسټ ګرېجوېټ کالج ۱ شمېره، ایبټ آباد')])
    for x in [
        ('Under the patronage of: Gohar Ali Khan, Director, Directorate of Curriculum and Teacher Education Khyber Pakhtunkhwa, Abbottabad', 'زیرِ سرپرستی: گوہر علی خان، ناظم نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا، ایبٹ آباد', 'تر سرپرستۍ لاندې: ګوهر علي خان، د خیبر پښتونخوا د نصاب او د ښوونکو د روزنې ریاست رییس، ایبټ آباد'),
        ('Focal person: Zulfiqar Khan, Additional Director (Curriculum and Review of Books), Directorate of Curriculum and Teacher Education Abbottabad, Khyber Pakhtunkhwa', 'فوکل پرسن: ذوالفقار خان، ایڈیشنل ڈائریکٹر (نصاب و نظرِ ثانی کتب) نظامت نصاب و تعلیم اساتذہ ایبٹ آباد خیبر پختونخوا', 'فوکل پرسن: ذوالفقار خان، اضافي رییس (نصاب او د کتابونو بیاکتنه)، د نصاب او د ښوونکو د روزنې ریاست ایبټ آباد، خیبر پښتونخوا'),
        ('Review:', 'نظرِ ثانی:', 'بیاکتنه:'),
    ]:
        b.p(*x)
    b.group('list', [
        ('Nighat Seema Kakakhel, SIPE, Government Girls Higher Secondary School, Kalu Khan, Swabi', 'نگہت سیما کاکاخیل، SIPE، گورنمنٹ گرلز ہائیر سیکنڈری سکول، کالو خان صوابی۔', 'نګهت سیما کاکاخېل، SIPE، د نجونو حکومتي عالي ثانوي ښوونځی، کالو خان صوابی'),
        ('Muhammad Nadeem, Lecturer HPE, Government Post Graduate College No. 1, Abbottabad', 'محمد ندیم، لیکچرر HPE، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد', 'محمد ندیم، د HPE لکچرر، حکومتي پوسټ ګرېجوېټ کالج ۱ شمېره، ایبټ آباد'),
        ('Muhammad Sabir, SIPE, Government High School Harnoi, Abbottabad', 'محمد صابر، SIPE، گورنمنٹ ہائی سکول ہرنو، ایبٹ آباد', 'محمد صابر، SIPE، حکومتي لېسه هرنوی، ایبټ آباد'),
        ('Samiullah, Desk Officer, Directorate of Curriculum and Teacher Education Khyber Pakhtunkhwa, Abbottabad', 'سمیع اللہ، ڈیسک آفیسر، نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا، ایبٹ آباد', 'سمیع‌الله، ډیسک افسر، د خیبر پښتونخوا د نصاب او د ښوونکو د روزنې ریاست، ایبټ آباد'),
        ('Muhammad Ilyas, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar', 'محمد الیاس، ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'محمد الیاس، د مضمون متخصص، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')])
    for x in [
        ('Editor: Muhammad Ilyas, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar', 'ایڈیٹر: محمد الیاس، ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'اېډیټر: محمد الیاس، د مضمون متخصص، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
        ('Printing under the supervision of: Zakir Hussain Afridi, Chairman; Saeed-ur-Rahman, Member (E&P); Khyber Pakhtunkhwa Textbook Board, Peshawar', 'طباعت زیرِ نگرانی: ذاکر حسین آفریدی، چیئرمین؛ سعید الرحمٰن، ممبر (ای اینڈ پی)؛ خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'چاپ تر څارنې لاندې: ذاکر حسین اپریدی، رییس؛ سعیدالرحمن، غړی (E&P)؛ د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
        ('Academic year: 2019-20; Website: www.kptbb.gov.pk; E-mail: membertbb@yahoo.com; Phone No.: 091-9217159-60', 'تعلیمی سال: 2019-20؛ ویب سائٹ: www.kptbb.gov.pk؛ ای میل: membertbb@yahoo.com؛ فون نمبر: 091-9217159-60', 'تعلیمي کال: 2019-20؛ وېبپاڼه: www.kptbb.gov.pk؛ برېښنالیک: membertbb@yahoo.com؛ ټیلیفون: 091-9217159-60'),
    ]:
        b.p(*x)
    r = BOOK.record(b, 'hpe12-fm-imprint', 'Imprint', 'طباعتی تفصیلات', 'د چاپ جزییات', 4, [None])
    BOOK.save(4, [('FM', r)])


TOC = [('1', 'Non-Communicable Diseases', 'غیر متعدی امراض', 'غیر ساري ناروغۍ', '1'),
       ('2', 'Circulatory System and the Effects of Exercise', 'نظام دوران خون اور ورزش کے اثرات', 'د وینې د جریان سیستم او د تمرین اغېزې', '11'),
       ('3', 'Doping', 'ڈوپنگ', 'ډوپینګ', '23'),
       ('4', 'Emergency Situation', 'ہنگامی صورت حال', 'بیړنی حالت', '28'),
       ('5', 'Verbal and Physical Violence', 'زبانی و جسمانی تشدد', 'ژبنی او فزیکي تاوتریخوالی', '49'),
       ('6', 'Sports and Biomechanical Principles', 'کھیل اور بائیو مکینیکل اصول', 'لوبې او بایومیخانیکي اصول', '53'),
       ('7', 'Rules and Skills of Games', 'کھیلوں کے قوانین اور مہارتیں', 'د لوبو قوانین او مهارتونه', '69')]


def p5():
    b = Builder()
    b.h('Contents', 'فہرستِ مضامین', 'نیوولیک')
    b.table('hpe12-toc', ['Chapter No.', 'Topics', 'Page No.'], [[n, e, p] for n, e, u, s, p in TOC], ['باب نمبر', 'عنوانات', 'صفحہ نمبر'], ['د څپرکي شمېره', 'سرلیکونه', 'مخ'],
            [[n, u, p] for n, e, u, s, p in TOC], [[n, s, p] for n, e, u, s, p in TOC])
    r = BOOK.record(b, 'hpe12-fm-contents', 'Contents', 'فہرستِ مضامین', 'نیوولیک', 5, [None])
    r['sourceDecorativeImages'] = 'A photograph of sports balls, a racket and a bat at the foot of the page is decorative.'
    BOOK.save(5, [('FM', r)], complete_units=['FM'], issues=[{'id': 'hpe12-pdf005', 'unit': 'FM', 'printedPage': None,
               'description': 'Owner ballpoint notes across the contents list (e.g. against chapters 1, 3, 5 and 6) are excluded.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    {1: p1, 3: p3, 4: p4, 5: p5}[n]()
