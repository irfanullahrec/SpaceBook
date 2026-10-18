"""Islamic History XII front matter: PDF1 cover, PDF3 title page (p.1), PDF4 credits (p.2) + contents (p.3), PDF5 contents (pp.4–5).
Run: python class12_ihist_page001.py N"""
import sys
from class12_ihist_common import BOOK, Builder, rec, P, LESSONS

TITLE = ('Tarikh-e-Islam (History of Islam): Banu Abbas, Part Two — Class Twelve', 'تاریخِ اسلام — بنوعباس (حصہ دوم) — بارہویں جماعت', 'د اسلام تاریخ: بنو عباس، دویمه برخه — دولسم ټولګی')


def toc(b, rows, tid):
    hdr = ['No.', 'Contents', 'Page']
    b.table(tid, hdr, [[str(n), e, str(pg)] for n, pg, e, u, p in rows], ['نمبر شمار', 'فہرست مضامین', 'صفحہ نمبر'], ['شمېره', 'د منځپانګې لړلیک', 'مخ'],
            [[str(n), u, str(pg)] for n, pg, e, u, p in rows], [[str(n), p, str(pg)] for n, pg, e, u, p in rows])


def p1():
    b = Builder()
    b.h(*TITLE)
    b.p('Not for sale — free from Government', 'NOT FOR SALE — Free From Government', 'د پلور لپاره نه — له حکومت وړیا')
    BOOK.save(1, [('FM', rec(b, 'FM', 1, 1, [None], first=True, kind='cover'))], issues=[{'id': 'ihist12-pdf001', 'unit': 'FM', 'printedPage': None,
               'description': 'Front cover. The red website watermark "awaz e inqilab.com" printed on the scan is a third-party stamp — excluded.'}])


def p3():
    b = Builder()
    b.h('Tarikh-e-Islam', 'تاریخِ اسلام', 'د اسلام تاریخ')
    P(b, [('Banu Abbas', 'بنوعباس', 'بنو عباس'), ('(Part Two)', '(حصہ دوئم)', '(دویمه برخه)'),
          ('for Class Twelve', 'برائے بارہویں جماعت', 'د دولسم ټولګي لپاره'),
          ('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')])
    BOOK.save(3, [('FM', rec(b, 'FM', 3, 3, [1], kind='title'))], issues=[{'id': 'ihist12-pdf003', 'unit': 'FM', 'printedPage': 1,
               'description': 'Title page with board emblem. Student handwriting (owner name and "Personal Group") excluded; "Not For Sale" header excluded.'}])


def p4():
    b = Builder()
    P(b, [('All rights reserved with Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'جملہ حقوق بحق خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور محفوظ ہیں۔', 'ټول حقونه د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور سره خوندي دي.'),
          ('Prepared by: Khyber Pakhtunkhwa Textbook Board, Peshawar', 'تیار کردہ: خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'چمتو کوونکی: د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
          ('Approved by: Federal Ministry of Education (Curriculum Wing), Government of Pakistan, Islamabad', 'منظور کردہ: وفاقی وزارتِ تعلیم (شعبۂ نصاب)، حکومتِ پاکستان اسلام آباد', 'منظور کوونکی: فدرالي د تعلیم وزارت (د نصاب څانګه)، د پاکستان حکومت، اسلام‌اباد'),
          ('Author: Professor Shams al-Rahman Gohar', 'مصنف: پروفیسر شمس الرحمان گوہر', 'لیکوال: پروفیسور شمس الرحمان ګوهر'),
          ('Review: Munawar Gul, Principal, Government Higher Secondary School Pir Pai, Nowshera; Muhammad Riaz, Subject Specialist, Government Higher Secondary School No.1 Peshawar Saddar; Abd al-Qadir, Assistant Professor, Government College, Peshawar; Syed Rafaqat Ali Shah, former Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar', 'نظرِ ثانی: منور گل پرنسپل گورنمنٹ ہائیر سیکنڈری سکول پیر پیائی نوشہرہ؛ محمد ریاض، ماہرِ مضمون گورنمنٹ ہائیر سیکنڈری سکول نمبر 1 پشاور صدر؛ عبدالقادر، اسسٹنٹ پروفیسر گورنمنٹ کالج، پشاور؛ سید رفاقت علی شاہ، سابق ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'بیاکتنه: منور ګل، د پیر پیایي نوښار د دولتي لېسې پرنسپل؛ محمد ریاض، د پېښور صدر د ۱ نمبر دولتي لېسې مضمون‌پوه؛ عبدالقادر، د دولتي کالج پېښور مرستیال پروفیسور؛ سید رفاقت علي شاه، د خیبر پښتونخوا د درسي کتابونو بورډ پخوانی مضمون‌پوه'),
          ('Editor: Muhammad Hussain, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar', 'ایڈیٹر: محمد حسین، ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'اېډیټر: محمد حسین، مضمون‌پوه، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
          ('Printing supervision and guidance: Arshad Khan Afridi (Chairman); Rizwan Ullah Asad, Member (E&P); Khyber Pakhtunkhwa Textbook Board, Peshawar', 'طباعت زیرِ نگرانی و رہنمائی: ارشد خان آفریدی (چیئرمین)؛ رضوان اللہ اسد، ممبر (ای اینڈ پی)؛ خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د چاپ څارنه او لارښوونه: ارشد خان اپریدی (رئیس)؛ رضوان الله اسد، غړی (E&P)؛ د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
          ('Academic year: 2022-23 · Website: www.kptbb.gov.pk · Email: membertbb@yahoo.com · Phone: 091-9217159-60', 'تعلیمی سال: 2022-23 · ویب سائیٹ: www.kptbb.gov.pk · ای میل: membertbb@yahoo.com · فون نمبر: 091-9217159-60', 'تعلیمي کال: 2022-23 · وېب‌پاڼه: www.kptbb.gov.pk · برېښنالیک: membertbb@yahoo.com · ټېلیفون: 091-9217159-60')])
    for x in b.paras[-1:]:
        x['untranslatedByDesign'] = True
    r1 = rec(b, 'FM', 2, 4, [2], kind='credits')
    t = Builder()
    t.h('Contents', 'فہرست', 'لړلیک')
    toc(t, LESSONS[:14], 'ihist12-toc-1')
    BOOK.save(4, [('FM', r1), ('FM', rec(t, 'FM', 3, 4, [3], kind='contents'))], issues=[{'id': 'ihist12-pdf004', 'unit': 'FM', 'printedPage': 2,
               'description': 'Credits and contents (items 1–14). "Not For Sale" headers excluded; student ticks against contents items 8–9 excluded.'}])


def p5():
    b = Builder()
    toc(b, LESSONS[14:31], 'ihist12-toc-2')
    r1 = rec(b, 'FM', 4, 5, [4], kind='contents')
    t = Builder()
    toc(t, LESSONS[31:], 'ihist12-toc-3')
    BOOK.save(5, [('FM', r1), ('FM', rec(t, 'FM', 5, 5, [5], kind='contents'))], complete_units=['FM'], issues=[{'id': 'ihist12-pdf005', 'unit': 'FM', 'printedPage': 4,
               'description': 'Contents items 15–42. Student ticks excluded. Contents item 10 printed "جعفر معتصم بن متوکل باللہ" and item 23 "…معتصم باللہ" (for مستعصم) — kept as printed in Urdu.'}])


if __name__ == '__main__':
    {1: p1, 3: p3, 4: p4, 5: p5}[int(sys.argv[1]) if len(sys.argv) > 1 else 1]()
