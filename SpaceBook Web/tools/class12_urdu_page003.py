"""Urdu XII PDF3 (spread): inner title page (left) and imprint / credits page (right)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.h('Urdu (Compulsory) — for Class Twelve', 'اُردو (لازمی) — بارھویں جماعت کے لیے', 'اردو (لازمي) — د دولسم ټولګي لپاره')
t.p('Khyber Pakhtunkhwa Textbook Board Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ پېښور')
title = BOOK.record(t, 'urdu12-fm-title', 'Title page', 'اندرونی سرورق', 'دننۍ پښتۍ', 3, [None])

c = Builder()
c.h('All rights reserved with Leading Publishers', 'جملہ حقوق بحق لیڈنگ پبلشرز محفوظ ہیں', 'ټول حقونه له لیډنګ پبلشرز سره خوندي دي')
for x in [
    ('Approved by: Federal Ministry of Education (Curriculum Wing), Government of Pakistan, Islamabad', 'منظور کردہ: وفاقی وزارتِ تعلیم (شعبۂ نصاب) حکومتِ پاکستان، اسلام آباد', 'منظور کړی: د پاکستان د حکومت فدرالي د پوهنې وزارت (د نصاب څانګه)، اسلام اباد'),
    ('According to: National Curriculum 2006', 'بمطابق: قومی نصاب 2006ء', 'د دې مطابق: ملي نصاب 2006ز'),
    ('Letter No. F.1-22/2010-Urdu, dated 04-04-2011', 'مراسلہ نمبر F.1-22/2010-Urdu مؤرخہ 04-04-2011', 'د لیک شمېره F.1-22/2010-Urdu، نېټه 04-04-2011'),
    ('Author: Professor Muhammad Jamal', 'مؤلف: پروفیسر محمد جمال', 'لیکوال: پروفیسر محمد جمال'),
    ('Patronage: Syed Bashir Hussain Shah, Director, Directorate of Curriculum and Teacher Education Khyber Pakhtunkhwa, Abbottabad', 'سرپرستی: سید بشیر حسین شاہ ناظم، نظامتِ نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد', 'سرپرستي: سید بشیر حسین شاه، ناظم، د خیبر پښتونخوا د نصاب او د ښوونکو د روزنې ریاست، ایبټ اباد'),
    ('Review and amendments: Syeda Tahira Jabeen, S.S., D.C.T.E., Abbottabad; Saira Bibi, S.S., Government Girls Higher Secondary School Hajia Gali, Abbottabad; Mushtaq Ahmad, Professor, Government College Khanpur (Haripur); Ijaz Khan, Assistant Professor, Government College Mandian, Abbottabad; Ahmad Rasheed, S.S., Textbook Board Khyber Pakhtunkhwa Peshawar',
     'نظرِ ثانی و ترامیم: سیدہ طاہرہ جبین، ایس ایس۔ ڈی سی ٹی ای، ایبٹ آباد؛ سائرہ بی بی، ایس ایس، گورنمنٹ گرلز ہائر سیکنڈری سکول حاجیہ گلی ایبٹ آباد؛ مشتاق احمد، پروفیسر، گورنمنٹ کالج خان پور (ہری پور)؛ اعجاز خان، اسسٹنٹ پروفیسر، گورنمنٹ کالج منڈیاں ایبٹ آباد؛ احمد رشید، ایس ایس۔ ٹیکسٹ بک بورڈ خیبر پختونخوا پشاور',
     'بیا کتنه او سمونې: سیده طاهره جبین، ایس ایس، ډي سي ټي اي، ایبټ اباد؛ سایره بي بي، ایس ایس، د حاجیه ګلي د نجونو دولتي لوړ ثانوي ښوونځی، ایبټ اباد؛ مشتاق احمد، پروفیسر، دولتي کالج خانپور (هریپور)؛ اعجاز خان، اسسټنټ پروفیسر، دولتي کالج منډیان، ایبټ اباد؛ احمد رشید، ایس ایس، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور'),
    ('Editor: Saleemullah Alvi, Subject Specialist (Urdu), Khyber Pakhtunkhwa Textbook Board Peshawar', 'مدیر: سلیم اللہ علوی، ماہرِ مضمون (اُردو) خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'مدیر: سلیم الله علوي، د مضمون کارپوه (اردو)، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور'),
    ('Under the supervision and guidance of: Ismatullah Khan Gandapur, Chairman; Saeed-ur-Rahman, Member (E & P), Khyber Pakhtunkhwa Textbook Board Peshawar', 'زیرِ نگرانی و رہنمائی: عصمت اللہ خان گنڈاپور، چیئرمین؛ سعید الرحمٰن، ممبر (ای اینڈ پی)، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د څارنې او لارښوونې لاندې: عصمت الله خان ګنډاپور، رییس؛ سعید الرحمن، غړی (ای اینډ پي)، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور'),
    ('Academic year 2020–21. Website: www.kptbb.gov.pk · Email: membertbb@yahoo.com · Phone: 091-9217159-60', 'تعلیمی سال 2020–21ء۔ ویب سائٹ: www.kptbb.gov.pk · ای میل: membertbb@yahoo.com · فون نمبر: 091-9217159-60', 'تعلیمي کال 2020–21. وېبپاڼه: www.kptbb.gov.pk · برېښنالیک: membertbb@yahoo.com · ټیلیفون: 091-9217159-60'),
]: c.p(*x)
imprint = BOOK.record(c, 'urdu12-fm-imprint', 'Imprint and credits', 'جملہ حقوق اور مرتبین', 'چاپ او همکاران', 3, [None])
issues = [{'id': 'urdu12-pdf003', 'unit': 'FM', 'printedPage': None, 'description': 'PDF3 is a two-page spread: left = inner title page, right = imprint/credits. Handwritten owner notes on the title page (a name and a marks table) are not part of the book and are excluded.'}]

if __name__ == '__main__':
    BOOK.save(3, [('FM', title), ('FM', imprint)], issues=issues)
