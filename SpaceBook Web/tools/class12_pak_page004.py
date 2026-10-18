"""Pak Studies XII PDF4 (spread): right = imprint/credits; left = contents (فہرست اسباق)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
b = Builder()
b.p('All rights reserved with Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'جملہ حقوق بحق خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور محفوظ ہیں۔', 'ټول حقونه د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور سره خوندي دي.')
b.p('Reviewed by the Federal Ministry of Education, Islamabad, as the sole textbook for the colleges of Khyber Pakhtunkhwa.', 'ریویو کردہ وفاقی وزارتِ تعلیم اسلام آباد بطور واحد نصابی کتاب برائے جملہ کالجز خیبر پختونخوا', 'د فدرالي پوهنې وزارت اسلام‌اباد له خوا د خیبر پښتونخوا د ټولو کالجونو لپاره د یوازیني درسي کتاب په توګه کتل شوی.')
H = (['Role', 'Names'], ['ذمہ داری', 'نام'], ['دنده', 'نومونه'])
rows = [
 ('Authors', 'Dr Syed Minhaj-ul-Hassan, Dr Fazal Rahim Marwat, Javed Iqbal, Syed Karamat Ali Shah Bukhari.', 'مصنفین', 'ڈاکٹر سید منہاج الحسن، ڈاکٹر فضل رحیم مروت، جاوید اقبال، سید کرامت علی شاہ بخاری۔', 'لیکوالان', 'ډاکټر سید منهاج الحسن، ډاکټر فضل رحیم مروت، جاوید اقبال، سید کرامت علي شاه بخاري.'),
 ('Revision', 'Prof. Muhammad Iqbal, Subject Specialist (Social Sciences); Fauzia Syed, Assistant Subject Specialist (Social Sciences); Muhammad Ilyas, Assistant Subject Specialist (Geography), Khyber Pakhtunkhwa Textbook Board, Peshawar', 'نظرِ ثانی', 'پروفیسر محمد اقبال ماہرِ مضمون (سوشل سائنسز)؛ فوزیہ سید معاون ماہرِ مضمون (سوشل سائنسز)؛ محمد الیاس معاون ماہرِ مضمون (جغرافیہ) خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'بیا کتنه', 'پروفیسر محمد اقبال د مضمون متخصص (ټولنیز علوم)؛ فوزیه سید مرستیال متخصص (ټولنیز علوم)؛ محمد الیاس مرستیال متخصص (جغرافیه)، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور'),
 ('Editor', 'Muhammad Hussain, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar', 'ایڈیٹر', 'محمد حسین ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'مدیر', 'محمد حسین د مضمون متخصص، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور'),
 ('Printing supervision and guidance', 'Rasheed Khan Paindakhel (Chairman); Saeed-ur-Rehman, Member (E & P), Khyber Pakhtunkhwa Textbook Board, Peshawar', 'طباعت زیرِ نگرانی و رہنمائی', 'رشید خان پائندہ خیل (چیئرمین)؛ سعید الرحمٰن، ممبر (ای اینڈ پی) خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د چاپ څارنه او لارښوونه', 'رشید خان پاینده‌خېل (رئیس)؛ سعیدالرحمن، غړی (ای اینډ پي)، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور'),
 ('Academic year', '2021-22', 'تعلیمی سال', '2021-22ء', 'تعلیمي کال', '2021-22'),
 ('Website', 'www.kptbb.gov.pk', 'ویب سائٹ', 'www.kptbb.gov.pk', 'وېب‌پاڼه', 'www.kptbb.gov.pk'),
 ('E-mail', 'membertbb@yahoo.com', 'ای میل', 'membertbb@yahoo.com', 'برېښنالیک', 'membertbb@yahoo.com'),
 ('Phone', '091-9217159-60', 'فون نمبر', '091-9217159-60', 'تلیفون', '091-9217159-60'),
]
b.table('pak12-imprint', H[0], [[r[0], r[1]] for r in rows], H[1], H[2], [[r[2], r[3]] for r in rows], [[r[4], r[5]] for r in rows])
imp = BOOK.record(b, 'pak12-fm-imprint', 'Imprint and credits', 'جملہ حقوق اور اشاعتی معلومات', 'د خپرونې معلومات', 4, [None])

c = Builder()
c.h('Contents', 'فہرستِ اسباق', 'منځپانګه')
CH = [(1, 'Establishment of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کا قیام', 'د پاکستان اسلامي جمهوریت جوړېدل', 1),
      (2, 'Early problems of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کے ابتدائی مسائل', 'د پاکستان اسلامي جمهوریت لومړنۍ ستونزې', 28),
      (3, 'The land of Pakistan', 'ارضِ پاکستان', 'د پاکستان ځمکه', 46),
      (4, 'Steps to make Pakistan an Islamic Republic', 'پاکستان کو اسلامی جمہوریہ بنانے کے اقدامات', 'پاکستان اسلامي جمهوریت جوړولو لپاره ګامونه', 66),
      (5, 'Governmental structure of Pakistan and good governance', 'پاکستان کا حکومتی ڈھانچہ اور اچھا نظامِ حکومت', 'د پاکستان حکومتي جوړښت او ښه حکومتولي', 85),
      (6, 'Culture of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کی ثقافت (کلچر)', 'د پاکستان اسلامي جمهوریت کلتور', 116),
      (7, 'Pakistani languages', 'پاکستانی زبانیں', 'پاکستاني ژبې', 136),
      (8, 'National cohesion and prosperity', 'قومی یک جہتی اور خوشحالی', 'ملي یووالی او سوکالي', 147),
      (9, 'Economic planning and development in the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان میں معاشی منصوبہ بندی اور ترقی', 'په پاکستان کې اقتصادي پلان جوړونه او پرمختګ', 157),
      (10, 'Foreign policy of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کی خارجہ پالیسی', 'د پاکستان اسلامي جمهوریت بهرنۍ تګلاره', 185),
      (11, 'Problems of Pakistan', 'پاکستان کے مسائل', 'د پاکستان ستونزې', 201)]
c.table('pak12-contents', ['No.', 'Title', 'Page'], [[str(n), e, str(p)] for n, e, u, ps, p in CH], ['نمبر شمار', 'عنوانات', 'صفحہ نمبر'], ['شمېره', 'سرلیک', 'مخ'],
        [[f'{n}.', u, str(p)] for n, e, u, ps, p in CH], [[str(n), ps, str(p)] for n, e, u, ps, p in CH])
con = BOOK.record(c, 'pak12-fm-contents', 'Contents', 'فہرستِ اسباق', 'منځپانګه', 4, [None])
issues = [{'id': 'pak12-pdf004', 'unit': 'FM', 'description': 'Contents list 11 chapters (incl. ch.7 Pakistani languages and ch.11 Problems of Pakistan); the legacy app units used different chapter titles — legacy units are superseded chapter by chapter.'}]

if __name__ == '__main__':
    BOOK.save(4, [('FM', imp), ('FM', con)], issues=issues, complete_units=['FM'])
