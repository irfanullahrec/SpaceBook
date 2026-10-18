"""Computer Science XII PDF19 (spread): printed pp.26–27 — summary (end); Activities 1–4; Exercise Q1 fill in the blanks; Q2 MCQs i–ii."""
from class12_cs_common import BOOK, Builder

s = Builder()
s.group('list', [('Multitasking, multiprogramming and multithreading are the features of nearly all modern operating systems which enable them to process multiple users jobs simultaneously in a parallel fashion.',
                  'ملٹی ٹاسکنگ، ملٹی پروگرامنگ اور ملٹی تھریڈنگ تقریباً تمام جدید آپریٹنگ سسٹمز کی خصوصیات ہیں جو انھیں متعدد صارفین کی جابز کو بیک وقت متوازی انداز میں پراسیس کرنے کے قابل بناتی ہیں۔',
                  'څو-دندیز، څو-پروګرامي او څو-تاریز کار د نږدې ټولو نویو عملیاتي سیسټمونو ځانګړنې دي چې دوی د ډېرو کاروونکو دندې په یو وخت په موازي ډول پروسس کولو ته وړ کوي.')])
sm = BOOK.record(s, 'cs12-u1-summary-2', 'Unit 1 summary (cont.)', 'یونٹ 1: خلاصہ (جاری)', '۱ څپرکی: لنډیز (دوام)', 19, [26])

a = Builder()
a.h('Activities', 'سرگرمیاں', 'فعالیتونه')
for n, en, ur, ps in [
    (1, 'The instructor should apply a few internal and external commands of MS-DOS to the students in computer lab and then provide a list of most commonly used MS-DOS commands and asks them to practice on these commands.',
     'استاد کو چاہیے کہ کمپیوٹر لیب میں طلبہ کو MS-DOS کی چند اندرونی اور بیرونی کمانڈز استعمال کر کے دکھائے اور پھر سب سے زیادہ استعمال ہونے والی MS-DOS کمانڈز کی فہرست دے کر انھیں ان کمانڈز کی مشق کرنے کو کہے۔',
     'ښوونکی دې په کمپیوټري لابراتوار کې زده‌کوونکو ته د MS-DOS ځینې دننني او بهرني امرونه وکاروي او بیا دې تر ټولو ډېر کارېدونکو MS-DOS امرونو لېست ورکړي او له هغوی دې وغواړي چې پر دې امرونو تمرین وکړي.'),
    (2, 'The instructor should practice the installation steps of Windows XP and Windows 7 Operating System in the class and then should, briefly, describe the main features of these operating systems to the students.',
     'استاد کو چاہیے کہ کلاس میں Windows XP اور Windows 7 آپریٹنگ سسٹم کی تنصیب کے مراحل کی مشق کرائے اور پھر طلبہ کو ان آپریٹنگ سسٹمز کی اہم خصوصیات مختصراً بیان کرے۔',
     'ښوونکی دې په ټولګي کې د Windows XP او Windows 7 عملیاتي سیسټم د نصبولو پړاوونه تمرین کړي او بیا دې زده‌کوونکو ته د دې عملیاتي سیسټمونو اصلي ځانګړنې په لنډه توګه بیان کړي.'),
    (3, 'Utility programs are the programs that are considered as a component of operating system. They are installed automatically with the installation of operating systems. A few examples of utility programs are Notepad, WordPad, Calculator, Image Viewer and Antivirus. The instructor should briefly practice the students on these programs.',
     'یوٹیلیٹی پروگرام وہ پروگرام ہیں جو آپریٹنگ سسٹم کا جز سمجھے جاتے ہیں۔ یہ آپریٹنگ سسٹم کی تنصیب کے ساتھ خود بخود انسٹال ہو جاتے ہیں۔ یوٹیلیٹی پروگراموں کی چند مثالیں Notepad، WordPad، Calculator، Image Viewer اور Antivirus ہیں۔ استاد کو چاہیے کہ طلبہ کو ان پروگراموں کی مختصر مشق کرائے۔',
     'ګټور (utility) پروګرامونه هغه دي چې د عملیاتي سیسټم برخه ګڼل کېږي. د عملیاتي سیسټم له نصبولو سره په خپله نصبېږي. د ګټورو پروګرامونو ځینې بېلګې Notepad، WordPad، Calculator، Image Viewer او Antivirus دي. ښوونکی دې زده‌کوونکو ته پر دې پروګرامونو لنډ تمرین ورکړي.'),
    (4, 'Drivers are the software that are used to interface computer hardware with the operating system and make them available to the users. The instructor should practice the installations of LAN card, Sound card and VGA card to the students.',
     'ڈرائیورز وہ سافٹ ویئر ہیں جو کمپیوٹر ہارڈویئر کو آپریٹنگ سسٹم سے جوڑنے اور اسے صارفین کے لیے دستیاب بنانے کے لیے استعمال ہوتے ہیں۔ استاد کو چاہیے کہ طلبہ کو LAN کارڈ، ساؤنڈ کارڈ اور VGA کارڈ کی تنصیب کی مشق کرائے۔',
     'چلوونکي (drivers) هغه سافټویرونه دي چې د کمپیوټري هارډویر د عملیاتي سیسټم سره د نښلولو او کاروونکو ته د برابرولو لپاره کارول کېږي. ښوونکی دې زده‌کوونکو ته د LAN کارډ، غږ کارډ او VGA کارډ د نصبولو تمرین ورکړي.')]:
    a.h(f'ACTIVITY {n}', f'سرگرمی {n}', f'فعالیت {n}')
    a.p(en, ur, ps)
ac = BOOK.record(a, 'cs12-u1-activities', 'Unit 1 activities', 'یونٹ 1: سرگرمیاں', '۱ څپرکی: فعالیتونه', 19, [26])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
e.group('lines', [
 ('i. The concept of executing multiple programs simultaneously on multiple possessors is known as ________ .', 'i. متعدد پروسیسرز پر بیک وقت متعدد پروگرام چلانے کا تصور ________ کہلاتا ہے۔', 'i. پر ډېرو پروسېسرونو په یو وخت د ډېرو پروګرامونو د اجرا مفهوم ته ________ ویل کېږي.'),
 ('ii. Multitasking operating systems execute ________ simultaneously.', 'ii. ملٹی ٹاسکنگ آپریٹنگ سسٹم بیک وقت ________ چلاتے ہیں۔', 'ii. څو-دندیز عملیاتي سیسټمونه په یو وخت ________ اجرا کوي.'),
 ('iii. The central theme of modern operating systems, based on the concept of switching among multiple programs in memory, is called ________ .', 'iii. جدید آپریٹنگ سسٹمز کا مرکزی موضوع، جو میموری میں متعدد پروگراموں کے درمیان تبدیلی کے تصور پر مبنی ہے، ________ کہلاتا ہے۔', 'iii. د نویو عملیاتي سیسټمونو مرکزي موضوع چې په حافظه کې د ډېرو پروګرامونو ترمنځ د بدلون پر مفهوم ولاړه ده، ________ بلل کېږي.'),
 ('iv. A process consists of five states i.e. new, ready, running, block and ________ .', 'iv. پراسیس پانچ حالتوں پر مشتمل ہوتا ہے یعنی نیا، تیار، چلتا ہوا، بلاک اور ________ ۔', 'iv. یوه پروسه پنځه حالتونه لري یعنې نوی، چمتو، روان، بند او ________ .'),
 ('v. ________ is a multitasking, multi-user operating system for servers, desktops and laptops, originally developed in 1969 by a group of AT&T employees at Bell Labs.', 'v. ________ سرورز، ڈیسک ٹاپس اور لیپ ٹاپس کے لیے ایک ملٹی ٹاسکنگ، ملٹی یوزر آپریٹنگ سسٹم ہے جو اصل میں 1969ء میں بیل لیبز میں AT&T کے ملازمین کے ایک گروپ نے تیار کیا۔', 'v. ________ د سرورونو، ډیسکټاپونو او لپټاپونو لپاره یو څو-دندیز، ډېر-کاروونکي عملیاتي سیسټم دی چې په اصل کې په ۱۹۶۹ز کې په بیل لابز کې د AT&T د کارکوونکو یوې ډلې جوړ کړ.')])
e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
e.mcq('i.', ('Operating system is an:', 'آپریٹنگ سسٹم ہے:', 'عملیاتي سیسټم یو دی:'),
      [('Application software', 'ایپلیکیشن سافٹ ویئر', 'کاريال سافټویر'), ('System software', 'سسٹم سافٹ ویئر', 'سیسټم سافټویر'), ('Driver', 'ڈرائیور', 'چلوونکی'), ('None of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')], per_line=1)
e.mcq('ii.', ('DOS stands for:', 'DOS کا مطلب ہے:', 'DOS معنا لري:'),
      ['Doctor of system', 'Document of system', 'Disk operating system', ('None of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')], per_line=1)
ex = BOOK.record(e, 'cs12-u1-exercise-1', 'Unit 1 exercise (1)', 'یونٹ 1: مشق (۱)', '۱ څپرکی: تمرین (۱)', 19, [27])
ex['sourceNote'] = 'The exercise continues on p.28 (PDF20). MCQ options are shown one per line as printed.'
issues = [{'id': 'cs12-pdf019', 'unit': 1, 'printedPage': 27,
           'description': 'Q1(i) prints “multiple possessors” (for “processors”); Activity 1 “and asks them”. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(19, [(1, sm), (1, ac), (1, ex)], issues=issues)
