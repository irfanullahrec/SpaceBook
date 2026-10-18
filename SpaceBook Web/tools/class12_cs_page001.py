"""Computer Science XII PDF1–3 front matter. PDF1 cover; PDF2 inside spread (anti-bribery slogan + title page);
PDF3 imprint (left) + contents begins (right). The whole contents (PDF3 right → PDF6 left) is recorded here as one table.
Run: python class12_cs_page001.py N (N = 1, 2 or 3)."""
import sys
from class12_cs_common import BOOK, Builder

UT = ('Front matter', 'ابتدائیہ', 'سریزه')


def cover():
    b = Builder()
    b.h('Computer Science — Grade XII', 'کمپیوٹر سائنس — بارھویں جماعت', 'کمپیوټر ساینس — دولسم ټولګی')
    b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
    b.p('Leading Books Publisher', 'لیڈنگ بکس پبلشر', 'لیډنګ بکس خپرندوی')
    b.p('Free From Government — NOT FOR SALE', 'حکومت کی طرف سے مفت — برائے فروخت نہیں', 'د حکومت له خوا وړیا — د پلور لپاره نه')
    r = BOOK.record(b, 'cs12-fm-cover', 'Front cover', 'سرورق', 'پښتۍ', 1, [None], unit_title=UT)
    r['sourceCoverIllustrationReview'] = 'Cover photograph (desktop computer, keyboard, mouse; figure on jigsaw pieces with devices) and the Board logo are decorative; not reproduced.'
    return r


def title():
    b = Builder()
    b.p('“The giver of a bribe and the taker of a bribe are both destined for Hell.”',
        'رشوت دینے والا اور رشوت لینے والا دونوں جہنمی ہیں۔',
        '"بډه ورکوونکی او بډه اخیستونکی دواړه دوزخیان دي."')
    b.h('Computer Science — Grade XII', 'کمپیوٹر سائنس — بارھویں جماعت', 'کمپیوټر ساینس — دولسم ټولګی')
    b.p('Leading Books Publisher, University Road, Peshawar', 'لیڈنگ بکس پبلشر، یونیورسٹی روڈ، پشاور', 'لیډنګ بکس خپرندوی، پوهنتون سړک، پېښور')
    b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
    r = BOOK.record(b, 'cs12-fm-title', 'Title page', 'سرِ ورق', 'سرلیک پاڼه', 2, [None], unit_title=UT)
    r['sourceNote'] = 'Left page: framed Urdu slogan (rendered in all languages). Right page: title page.'
    return r


def imprint():
    b = Builder()
    b.p('All rights reserved with Leading Books Publisher, Peshawar.', 'جملہ حقوق بحق لیڈنگ بکس پبلشر، پشاور محفوظ ہیں۔', 'ټول حقونه د لیډنګ بکس خپرندوی، پېښور سره خوندي دي.')
    rows = [
        ('Approved by', 'Directorate of Curriculum and Teacher Education, Abbottabad, according to the National Curriculum 2006. NOC No.5385-87/SS-V dated: 11.09.2015',
         'منظور کنندہ', 'ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن، ایبٹ آباد، قومی نصاب 2006ء کے مطابق۔ این او سی نمبر 5385-87/SS-V مورخہ 11.09.2015',
         'تصویب کوونکی', 'د نصاب او ښوونکو د روزنې ریاست، ایبټ‌اباد، د ۲۰۰۶ز ملي نصاب سره سم. NOC شمېره 5385-87/SS-V، نېټه 11.09.2015'),
        ('Authors', 'Mohammad Khalid, Head of Computer Science Department at OPF Boys College, Islamabad; Rahman Ali, M.Phil, M.Sc, University of Peshawar',
         'مصنفین', 'محمد خالد، صدر شعبہ کمپیوٹر سائنس، او پی ایف بوائز کالج، اسلام آباد؛ رحمان علی، ایم فل، ایم ایس سی، پشاور یونیورسٹی',
         'لیکوالان', 'محمد خالد، د OPF هلکانو کالج اسلام‌اباد د کمپیوټر ساینس د څانګې مشر؛ رحمان علي، ایم فل، ایم ایس سي، پېښور پوهنتون'),
        ('Review Supervision', 'Syed Bashir Hussain Shah, Director Curriculum & Teacher Education Abbottabad',
         'نگرانِ نظرِ ثانی', 'سید بشیر حسین شاہ، ڈائریکٹر کریکولم اینڈ ٹیچر ایجوکیشن ایبٹ آباد',
         'د بیاکتنې څارنه', 'سید بشیر حسین شاه، د نصاب او ښوونکو د روزنې رئیس، ایبټ‌اباد'),
        ('Reviewers', 'Mr. Muhammad Zahid, Associate Professor, Chairman Department of Computer Science, GPGC No.1 Abbotabad; Mr. Muhammad Daud, Assistant Professor GPGC Mandian Abbotabad; Dr. Muhammad Naeem, IT Department Hazara University Mansehra; Mr. Waqar Ahmed, Assistant Subject Specialist Text Book Board Peshawar; Mr. Ibrar Ahmed, Subject Specialist, DCTE Abbotabad',
         'نظرِ ثانی کنندگان', 'جناب محمد زاہد، ایسوسی ایٹ پروفیسر، چیئرمین شعبہ کمپیوٹر سائنس، جی پی جی سی نمبر 1 ایبٹ آباد؛ جناب محمد داؤد، اسسٹنٹ پروفیسر جی پی جی سی منڈیاں ایبٹ آباد؛ ڈاکٹر محمد نعیم، آئی ٹی ڈیپارٹمنٹ ہزارہ یونیورسٹی مانسہرہ؛ جناب وقار احمد، اسسٹنٹ سبجیکٹ اسپیشلسٹ ٹیکسٹ بک بورڈ پشاور؛ جناب ابرار احمد، سبجیکٹ اسپیشلسٹ، ڈی سی ٹی ای ایبٹ آباد',
         'بیاکتونکي', 'ښاغلی محمد زاهد، اسوسیېټ پروفیسر، د GPGC نمبر ۱ ایبټ‌اباد د کمپیوټر ساینس د څانګې رئیس؛ ښاغلی محمد داود، اسسټنټ پروفیسر GPGC منډیان ایبټ‌اباد؛ ډاکټر محمد نعیم، د هزاره پوهنتون مانسهره IT څانګه؛ ښاغلی وقار احمد، د درسي کتابونو بورډ پېښور مرستیال مضمون‌پوه؛ ښاغلی ابرار احمد، مضمون‌پوه، DCTE ایبټ‌اباد'),
        ('Editor', 'Shakeel Ahmed, Subject Specialist (Maths), Khyber Pakhtunkhwa Textbook Board Peshawar',
         'مدیر', 'شکیل احمد، سبجیکٹ اسپیشلسٹ (ریاضی)، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور',
         'مدیر', 'شکیل احمد، مضمون‌پوه (ریاضي)، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور'),
        ('Printing Supervision', 'Masood Ahmed, Chairman, Khyber Pakhtunkhwa Textbook Board Peshawar; Saeedur Rehman, Member (E & P), Khyber Pakhtunkhwa Textbook Board Peshawar',
         'نگرانِ طباعت', 'مسعود احمد، چیئرمین، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور؛ سعید الرحمن، ممبر (ای اینڈ پی)، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور',
         'د چاپ څارنه', 'مسعود احمد، رئیس، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور؛ سعید الرحمن، غړی (E & P)، د خیبر پښتونخوا د درسي کتابونو بورډ پېښور'),
        ('Academic Year', '2018-19 | Website: www.kptbb.gov.pk | Email: membertbb@yahoo.com | Phone: 091-9217159-60',
         'تعلیمی سال', '2018-19 | ویب سائٹ: www.kptbb.gov.pk | ای میل: membertbb@yahoo.com | فون: 091-9217159-60',
         'تعلیمي کال', '2018-19 | وېب‌پاڼه: www.kptbb.gov.pk | برېښنالیک: membertbb@yahoo.com | ټیلیفون: 091-9217159-60')]
    b.table('cs12-imprint', ['Role', 'Details'], [[r[0], r[1]] for r in rows], ['ذمہ داری', 'تفصیل'], ['دنده', 'جزییات'],
            [[r[2], r[3]] for r in rows], [[r[4], r[5]] for r in rows])
    imp = BOOK.record(b, 'cs12-fm-imprint', 'Imprint', 'طباعتی تفصیلات', 'د چاپ جزییات', 3, [None], unit_title=UT)

    c = Builder()
    c.h('Contents', 'فہرستِ مضامین', 'فهرست')
    T = []  # (number, en, ur, ps, page)
    def U(n, en, ur, ps, pg): T.append((f'UNIT-{n}', en, ur, ps, pg))
    def S(n, en, ur, ps, pg): T.append((n, en, ur, ps, pg))
    def E(pg_s, pg_a, pg_e):
        T.append(('', 'SUMMARY', 'خلاصہ', 'لنډیز', pg_s))
        if pg_a: T.append(('', 'ACTIVITIES', 'سرگرمیاں', 'فعالیتونه', pg_a))
        T.append(('', 'EXERCISE', 'مشق', 'تمرین', pg_e))
    U(1, 'OPERATING SYSTEM', 'آپریٹنگ سسٹم', 'عملیاتي سیسټم', '1')
    S('1.1', 'INTRODUCTION', 'تعارف', 'پېژندنه', '2'); S('1.1.1', 'An Operating System', 'آپریٹنگ سسٹم', 'عملیاتي سیسټم', '2')
    S('1.1.2', 'Commonly used operating systems', 'عام استعمال ہونے والے آپریٹنگ سسٹم', 'عام کارېدونکي عملیاتي سیسټمونه', '3')
    S('1.1.3', 'Types of Operating Systems', 'آپریٹنگ سسٹم کی اقسام', 'د عملیاتي سیسټمونو ډولونه', '8')
    S('1.1.4', 'Single-user and Multi-user Operating Systems', 'سنگل یوزر اور ملٹی یوزر آپریٹنگ سسٹم', 'یو-کاروونکی او ډېر-کاروونکي عملیاتي سیسټمونه', '16')
    S('1.2', 'OPERATING SYSTEM FUNCTIONS', 'آپریٹنگ سسٹم کے افعال', 'د عملیاتي سیسټم دندې', '17')
    S('1.3', 'PROCESS MANAGEMENT', 'پراسیس مینجمنٹ', 'د پروسې اداره', '22'); S('1.3.1', 'Process', 'پراسیس', 'پروسه', '22')
    S('1.3.2', 'Process States', 'پراسیس کی حالتیں', 'د پروسې حالتونه', '22'); S('1.3.3', 'Threads and processes', 'تھریڈز اور پراسیسز', 'تارونه (Threads) او پروسې', '23')
    S('1.3.4', 'Multitasking and Multithreading', 'ملٹی ٹاسکنگ اور ملٹی تھریڈنگ', 'څو-دندیز او څو-تاریز کار', '24')
    S('1.3.5', 'Multitasking and Multiprogramming', 'ملٹی ٹاسکنگ اور ملٹی پروگرامنگ', 'څو-دندیز کار او څو-پروګرامي کار', '24')
    E('25', '26', '27')
    U(2, 'SYSTEM DEVELOPMENT LIFE CYCLE', 'سسٹم ڈویلپمنٹ لائف سائیکل', 'د سیسټم د پراختیا د ژوند دوره', '31')
    S('2.1', 'INTRODUCTION', 'تعارف', 'پېژندنه', '32'); S('2.1.1', 'A System', 'سسٹم', 'سیسټم', '32')
    S('2.1.2', 'System development life cycle and its importance', 'سسٹم ڈویلپمنٹ لائف سائیکل اور اس کی اہمیت', 'د سیسټم د پراختیا د ژوند دوره او اهمیت یې', '32')
    S('2.1.3', 'Objectives of SDLC', 'ایس ڈی ایل سی کے مقاصد', 'د SDLC موخې', '33'); S('2.1.4', 'Stakeholders of SDLC', 'ایس ڈی ایل سی کے اسٹیک ہولڈرز', 'د SDLC ښکېل اړخونه', '34')
    S('2.1.5', 'System development life cycle phases', 'سسٹم ڈویلپمنٹ لائف سائیکل کے مراحل', 'د سیسټم د پراختیا د ژوند دورې پړاوونه', '35')
    S('2.1.6', 'Role of the Personnel involved in SDLC', 'ایس ڈی ایل سی میں شامل افراد کا کردار', 'په SDLC کې د ښکېلو کسانو رول', '47')
    E('52', '53', '54')
    U(3, 'OBJECT ORIENTED PROGRAMMING USING C++', 'سی پلس پلس کے ذریعے آبجیکٹ اورینٹڈ پروگرامنگ', 'د C++ په مرسته شیانو ته متوجه پروګرام‌سازي', '59')
    S('3.1', 'INTRODUCTION', 'تعارف', 'پېژندنه', '58'); S('3.1.1', 'Computer program', 'کمپیوٹر پروگرام', 'کمپیوټري پروګرام', '58')
    S('3.1.2', 'Header files and Reserved words', 'ہیڈر فائلیں اور مخصوص الفاظ', 'سرلیک فایلونه او ځانګړې کلمې', '58')
    S('3.1.3', 'Structure of a C++ program', 'سی پلس پلس پروگرام کی ساخت', 'د C++ پروګرام جوړښت', '60')
    S('3.1.4', 'Statement terminator (;)', 'اسٹیٹمنٹ ٹرمینیٹر (;)', 'د بیان پای‌ټکی (;)', '64')
    S('3.1.5', 'Comments and their syntax in C++', 'سی پلس پلس میں تبصرے اور ان کا طریقۂ تحریر', 'په C++ کې تبصرې او د لیکلو بڼه یې', '64')
    S('3.2', 'C++ Constants and Variables', 'سی پلس پلس کے کانسٹنٹس اور ویری ایبلز', 'د C++ ثابتونه او متغیرونه', '65')
    S('3.2.1', 'Constants and Variables', 'کانسٹنٹس اور ویری ایبلز', 'ثابتونه او متغیرونه', '65')
    S('3.2.2', 'Rules for naming variables', 'ویری ایبلز کے نام رکھنے کے قواعد', 'د متغیرونو د نوم ایښودو قواعد', '68')
    S('3.2.3', 'Declaration and Initialization of variables', 'ویری ایبلز کا اعلان اور ابتدائی قدر', 'د متغیرونو اعلان او لومړنی ارزښت', '69')
    S('3.2.4', 'Fundamental data types in C++', 'سی پلس پلس میں بنیادی ڈیٹا ٹائپس', 'په C++ کې بنسټیز ډېټا ډولونه', '72')
    S('3.2.5', 'Constant qualifier', 'کانسٹنٹ کوالیفائر', 'ثابت توصیف‌کوونکی', '76'); S('3.2.6', 'Type casting operator', 'ٹائپ کاسٹنگ آپریٹر', 'د ډول بدلولو چلونکی', '77')
    S('3.3', 'Input/output Handling', 'ان پٹ/آؤٹ پٹ کا انتظام', 'د ننوتو/وتو اداره', '78'); S('3.3.1', 'Standard output (cout)', 'معیاری آؤٹ پٹ (cout)', 'معیاري وتنه (cout)', '78')
    S('3.3.2', 'Standard input (cin)', 'معیاری ان پٹ (cin)', 'معیاري ننوتنه (cin)', '79')
    S('3.3.3', 'gets(), puts() and getch() functions', 'gets()، puts() اور getch() فنکشنز', 'د gets()، puts() او getch() فنکشنونه', '82')
    S('3.3.4', 'Escape sequences', 'ایسکیپ سیکوینسز', 'د تېښتې لړۍ (Escape sequences)', '85'); S('3.3.5', 'I/O handling functions', 'ان پٹ/آؤٹ پٹ کے فنکشنز', 'د ننوتو/وتو فنکشنونه', '87')
    S('3.3.6', 'endl and setw Manipulator', 'endl اور setw مینیپولیٹر', 'endl او setw بدلوونکي', '88')
    S('3.4', 'Operators in C++', 'سی پلس پلس میں آپریٹرز', 'په C++ کې چلونکي', '90'); S('3.4.1', 'Operators in C++', 'سی پلس پلس میں آپریٹرز', 'په C++ کې چلونکي', '90')
    S('3.4.2', 'Unary, Binary and Ternary operators', 'یونری، بائنری اور ٹرنری آپریٹرز', 'یو-عملي، دوه-عملي او درې-عملي چلونکي', '100')
    S('3.4.3', 'Expression', 'ایکسپریشن', 'افاده', '101'); S('3.4.4', 'Precedence of operators', 'آپریٹرز کی ترجیح', 'د چلونکو لومړیتوب', '102')
    E('104', None, '106')
    U(4, 'CONTROL STRUCTURE', 'کنٹرول اسٹرکچر', 'کنټرولي جوړښت', '109')
    S('4.1', 'Decision statements', 'فیصلہ کن بیانات', 'پرېکړه‌ییز بیانونه', '110'); S('4.1.1', 'Use of decision statements', 'فیصلہ کن بیانات کا استعمال', 'د پرېکړه‌ییزو بیانونو کارونه', '110')
    S('4.1.2', 'Nested if statement', 'نیسٹڈ اِف اسٹیٹمنٹ', 'ځالې if بیان', '119'); S('4.1.3', 'break statement and exit() function', 'بریک اسٹیٹمنٹ اور exit() فنکشن', 'break بیان او exit() فنکشن', '122')
    S('4.2', 'LOOPS', 'لوپس', 'حلقې (Loops)', '123'); S('4.2.1', 'Types of loops', 'لوپس کی اقسام', 'د حلقو ډولونه', '124')
    S('4.2.2', 'continue statement', 'کنٹینیو اسٹیٹمنٹ', 'continue بیان', '135'); S('4.2.3', 'Nested loops', 'نیسٹڈ لوپس', 'ځالې حلقې', '135')
    E('138', None, '139')
    U(5, 'ARRAYS AND STRINGS', 'ایریز اور اسٹرنگز', 'لړۍ (Arrays) او تارونه (Strings)', '145')
    S('5.1', 'Introduction to array', 'ایرے کا تعارف', 'د لړۍ پېژندنه', '146'); S('5.1.1', 'Concept of arrays', 'ایریز کا تصور', 'د لړیو مفهوم', '146')
    S('5.1.2', 'Representation of array', 'ایرے کی نمائندگی', 'د لړۍ ښودنه', '147'); S('5.1.3', 'Terminology used in Arrays', 'ایریز میں مستعمل اصطلاحات', 'په لړیو کې کارېدونکې اصطلاحګانې', '147')
    S('5.1.4', 'Definition and initialization of an array', 'ایرے کی تعریف اور ابتدائی قدر', 'د لړۍ تعریف او لومړنی ارزښت', '148')
    S('5.1.5', 'Accessing and Writing at Index in an array', 'ایرے میں انڈیکس پر رسائی اور لکھنا', 'په لړۍ کې پر شاخص لاسرسی او لیکل', '150')
    S('5.1.6', 'Traversing an array', 'ایرے کو عبور کرنا', 'د لړۍ تېرېدل', '154'); S('5.1.7', 'size of () Operator', 'sizeof () آپریٹر', 'sizeof () چلونکی', '156')
    S('5.2', 'Two-dimensional arrays', 'دو جہتی ایریز', 'دوه-بعدي لړۍ', '157'); S('5.2.1', 'Concept of two dimensional arrays', 'دو جہتی ایریز کا تصور', 'د دوه-بعدي لړیو مفهوم', '157')
    S('5.2.2', 'Definition and initialization of two dimensional arrays', 'دو جہتی ایریز کی تعریف اور ابتدائی قدر', 'د دوه-بعدي لړیو تعریف او لومړنی ارزښت', '158')
    S('5.2.3', 'Accessing and writing at an index in a two dimensional array', 'دو جہتی ایرے میں انڈیکس پر رسائی اور لکھنا', 'په دوه-بعدي لړۍ کې پر شاخص لاسرسی او لیکل', '159')
    S('5.3', 'Strings', 'اسٹرنگز', 'تارونه', '162'); S('5.3.1', 'What are strings?', 'اسٹرنگز کیا ہیں؟', 'تارونه څه دي؟', '162'); S('5.3.2', 'A string', 'اسٹرنگ', 'تار', '162')
    S('5.3.3', 'Initializing string', 'اسٹرنگ کی ابتدائی قدر', 'د تار لومړنی ارزښت', '163'); S('5.3.4', 'Commonly used string functions', 'عام استعمال ہونے والے اسٹرنگ فنکشنز', 'عام کارېدونکي د تار فنکشنونه', '166')
    E('172', None, '173')
    U(6, 'FUNCTIONS', 'فنکشنز', 'فنکشنونه', '175')
    S('6.1', 'Functions', 'فنکشنز', 'فنکشنونه', '176'); S('6.1.1', 'Concept and types of functions', 'فنکشنز کا تصور اور اقسام', 'د فنکشنونو مفهوم او ډولونه', '176')
    S('6.1.2', 'Advantages of using functions', 'فنکشنز کے استعمال کے فوائد', 'د فنکشنونو د کارونې ګټې', '181'); S('6.1.3', 'Function signature', 'فنکشن سگنیچر', 'د فنکشن لاسلیک', '182')
    S('6.1.4', 'Components of functions', 'فنکشنز کے اجزاء', 'د فنکشنونو برخې', '182'); S('6.1.5', 'Scope of variables', 'ویری ایبلز کا دائرۂ کار', 'د متغیرونو ساحه', '185')
    S('6.1.6', 'Formal parameters and actual parameters', 'رسمی پیرامیٹرز اور حقیقی پیرامیٹرز', 'رسمي پارامېټرونه او اصلي پارامېټرونه', '190')
    S('6.1.7', 'Local and Global functions', 'لوکل اور گلوبل فنکشنز', 'سیمه‌ییز او نړیوال فنکشنونه', '192'); S('6.1.8', 'inline function', 'ان لائن فنکشن', 'inline فنکشن', '193')
    S('6.2', 'Passing arguments and returning values', 'آرگیومنٹس بھیجنا اور ویلیوز واپس کرنا', 'د دلیلونو لېږل او د ارزښتونو بېرته ورکول', '194')
    S('6.2.1', 'Passing arguments', 'آرگیومنٹس بھیجنا', 'د دلیلونو لېږل', '195'); S('6.2.2', 'Default arguments', 'ڈیفالٹ آرگیومنٹس', 'ډیفالټ دلیلونه', '201')
    S('6.2.3', 'return statement', 'ریٹرن اسٹیٹمنٹ', 'return بیان', '203')
    S('6.3', 'Function overloading', 'فنکشن اوورلوڈنگ', 'د فنکشن ډېرول (overloading)', '204'); S('6.3.1', 'Definition', 'تعریف', 'تعریف', '204')
    S('6.3.2', 'Advantages of function overloading', 'فنکشن اوورلوڈنگ کے فوائد', 'د فنکشن د ډېرولو ګټې', '206'); S('6.3.3', 'Use of function overloading', 'فنکشن اوورلوڈنگ کا استعمال', 'د فنکشن د ډېرولو کارونه', '207')
    E('210', None, '212')
    U(7, 'POINTERS', 'پوائنٹرز', 'نښې (Pointers)', '215')
    S('7.1', 'INTRODUCTION', 'تعارف', 'پېژندنه', '215'); S('7.1.1', 'Pointer', 'پوائنٹر', 'نښه (Pointer)', '216'); S('7.1.2', 'Memory addresses', 'میموری ایڈریسز', 'د حافظې پتې', '216')
    S('7.1.3', 'Reference operator (&)', 'ریفرنس آپریٹر (&)', 'د حوالې چلونکی (&)', '217'); S('7.1.4', 'Dereference operator (*)', 'ڈی ریفرنس آپریٹر (*)', 'د حوالې لرې کولو چلونکی (*)', '218')
    S('7.1.5', 'Declaring variables of pointer types', 'پوائنٹر ٹائپ کے ویری ایبلز کا اعلان', 'د نښې ډول متغیرونو اعلان', '220'); S('7.1.6', 'Pointer initialization', 'پوائنٹر کی ابتدائی قدر', 'د نښې لومړنی ارزښت', '221')
    E('224', None, '225')
    U(8, 'OBJECTS AND CLASSES', 'آبجیکٹس اور کلاسز', 'شیان او ټولګي (Classes)', '227')
    S('8.1', 'Classes', 'کلاسز', 'ټولګي', '228'); S('8.1.1', 'Class and object', 'کلاس اور آبجیکٹ', 'ټولګی او شی', '228'); S('8.1.2', 'Member of a class', 'کلاس کا رکن', 'د ټولګي غړی', '233')
    S('8.1.3', 'Access specifiers', 'ایکسیس اسپیسیفائرز', 'د لاسرسي ټاکونکي', '234'); S('8.1.4', 'Data hiding', 'ڈیٹا ہائیڈنگ', 'د ډېټا پټول', '238')
    S('8.1.5', 'Constructor and destructor', 'کنسٹرکٹر اور ڈسٹرکٹر', 'جوړوونکی او ړنګوونکی', '239'); S('8.1.6', 'Inheritance and Polymorphism', 'وراثت اور پولی مارفزم', 'میراث او څوبڼیزتوب', '248')
    E('255', None, '256')
    U(9, 'FILE HANDLING', 'فائل ہینڈلنگ', 'د فایلونو اداره', '259')
    S('9.1', 'File handling', 'فائل ہینڈلنگ', 'د فایلونو اداره', '259'); S('9.1.1', 'Types of files', 'فائلوں کی اقسام', 'د فایلونو ډولونه', '260'); S('9.1.2', 'Opening file', 'فائل کھولنا', 'د فایل پرانیستل', '260')
    S('9.1.3', 'bof() and eof()', 'bof() اور eof()', 'bof() او eof()', '268'); S('9.1.4', 'Stream', 'اسٹریم', 'بهیر (Stream)', '269'); S('9.1.5', 'Use of the Streams', 'اسٹریمز کا استعمال', 'د بهیرونو کارونه', '271')
    E('276', None, '277')
    for en, ur, ps, pg in [('BIBLIOGRAPHY', 'کتابیات', 'کتاب‌نامه', '279'), ('ANSWERS', 'جوابات', 'ځوابونه', '282'), ('GLOSSARY', 'فرہنگ', 'وییپانګه', '286'), ('INDEX', 'اشاریہ', 'نښلیک', '301'), ('ABOUT AUTHORS', 'مصنفین کا تعارف', 'د لیکوالانو په اړه', '303')]:
        T.append(('', en, ur, ps, pg))
    c.table('cs12-contents', ['No.', 'Title', 'Page'], [[t[0], t[1], t[4]] for t in T], ['نمبر', 'عنوان', 'صفحہ'], ['شمېره', 'سرلیک', 'مخ'],
            [[t[0], t[2], t[4]] for t in T], [[t[0], t[3], t[4]] for t in T])
    con = BOOK.record(c, 'cs12-fm-contents', 'Contents', 'فہرستِ مضامین', 'فهرست', 3, [None], unit_title=UT)
    con['sourceNote'] = 'The contents run from the right page of PDF3 to the left page of PDF6 and are reproduced here as one structured table. In print the page-number column is offset by one row in several blocks; numbers are aligned to the entries here. Item “1.3.5” is printed as “1.3.5” and “2.1.5” as “2.1.5”.'
    return imp, con


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if n == 1:
        BOOK.save(1, [('FM', cover())])
    elif n == 2:
        BOOK.save(2, [('FM', title())], issues=[{'id': 'cs12-pdf002', 'unit': 'FM', 'description': 'Owner names/signatures (“Abdul Haseeb”, “عبد الحسیب”) and pen scribbles on the title page are excluded.'}])
    elif n == 3:
        imp, con = imprint()
        BOOK.save(3, [('FM', imp), ('FM', con)], issues=[{'id': 'cs12-pdf003', 'unit': 'FM', 'description': 'Contents pages (PDF3–6) carry heavy owner pen circling/crossing of entries; excluded. The printed page-number column is shifted by one row in several blocks (e.g. Unit 3 lists 3.1 at 58 while the unit starts at 59).'}],
                  complete_units=['FM'])
