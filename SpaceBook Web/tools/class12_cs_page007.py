"""Computer Science XII PDF7 (spread): printed pp.2–3 — 1.1 Introduction; 1.1.1 An operating system; Figure 1.1; 1.1.2 commonly used OS; a. DOS (begins)."""
from class12_cs_common import BOOK, Builder
from class12_cs_figs import fig_1_1

t = Builder()
P = t.p
H = t.h
H('1.1 INTRODUCTION', '1.1 تعارف', '۱.۱ پېژندنه')
P('This unit is focused on introduction to Operating System and its functions and services. It also describes that how an operating system is used to execute processes. At the end, a differentiation is made between thread and process, multithreading, multitasking and multiprogramming.',
  'یہ یونٹ آپریٹنگ سسٹم کے تعارف اور اس کے افعال اور خدمات پر مرکوز ہے۔ یہ بھی بیان کرتا ہے کہ آپریٹنگ سسٹم پراسیسز کو چلانے کے لیے کیسے استعمال ہوتا ہے۔ آخر میں تھریڈ اور پراسیس، ملٹی تھریڈنگ، ملٹی ٹاسکنگ اور ملٹی پروگرامنگ کے درمیان فرق کیا گیا ہے۔',
  'دا څپرکی د عملیاتي سیسټم پر پېژندنې او د هغه پر دندو او خدمتونو تمرکز لري. دا هم بیانوي چې عملیاتي سیسټم د پروسو د چلولو لپاره څنګه کارول کېږي. په پای کې د تار (thread) او پروسې، څو-تاریز، څو-دندیز او څو-پروګرامي کار ترمنځ توپیر شوی.')
P('Operating System is an important component of a computer system and has the same relation with computer hardware as human soul has with human body. As human body is useless without human soul, similarly, a computer is useless without an operating system.',
  'آپریٹنگ سسٹم کمپیوٹر سسٹم کا ایک اہم جز ہے اور کمپیوٹر ہارڈویئر کے ساتھ اس کا وہی تعلق ہے جو انسانی روح کا انسانی جسم کے ساتھ ہے۔ جس طرح انسانی جسم روح کے بغیر بے کار ہے، اسی طرح کمپیوٹر آپریٹنگ سسٹم کے بغیر بے کار ہے۔',
  'عملیاتي سیسټم د کمپیوټري سیسټم یوه مهمه برخه ده او له کمپیوټري هارډویر سره یې هماغه اړیکه ده چې انساني روح یې له انساني بدن سره لري. لکه څنګه چې انساني بدن له روح پرته بې‌ګټې دی، همداسې کمپیوټر له عملیاتي سیسټم پرته بې‌ګټې دی.')
H('1.1.1 An Operating System', '1.1.1 آپریٹنگ سسٹم', '۱.۱.۱ عملیاتي سیسټم')
P('An operating System (OS) is an intermediary between users and computer hardware. It provides users an environment in which a user can execute programs conveniently and efficiently. In technical terms, it is a software which manages hardware. An operating System controls the allocation of resources and services such as memory, processors, devices and information.',
  'آپریٹنگ سسٹم (OS) صارفین اور کمپیوٹر ہارڈویئر کے درمیان ایک واسطہ ہے۔ یہ صارفین کو ایسا ماحول فراہم کرتا ہے جس میں صارف آسانی اور مؤثر طریقے سے پروگرام چلا سکتا ہے۔ تکنیکی اصطلاح میں یہ ایک سافٹ ویئر ہے جو ہارڈویئر کا انتظام کرتا ہے۔ آپریٹنگ سسٹم وسائل اور خدمات مثلاً میموری، پروسیسرز، آلات اور معلومات کی تقسیم کو کنٹرول کرتا ہے۔',
  'عملیاتي سیسټم (OS) د کاروونکو او کمپیوټري هارډویر ترمنځ منځګړی دی. کاروونکو ته داسې چاپېریال برابروي چې پکې کاروونکی پروګرامونه په اسانۍ او اغېزمن ډول چلولی شي. په تخنیکي اصطلاح دا یو سافټویر دی چې هارډویر اداره کوي. عملیاتي سیسټم د سرچینو او خدمتونو لکه حافظې، پروسېسرونو، وسایلو او معلوماتو وېش کنټرولوي.')
P('“An operating system is a program that acts as an interface between the user and the computer hardware and controls the execution of all kinds of programs.”',
  '’’آپریٹنگ سسٹم ایک ایسا پروگرام ہے جو صارف اور کمپیوٹر ہارڈویئر کے درمیان انٹرفیس کا کام کرتا ہے اور ہر قسم کے پروگراموں کے چلنے کو کنٹرول کرتا ہے۔‘‘',
  '"عملیاتي سیسټم داسې پروګرام دی چې د کاروونکي او کمپیوټري هارډویر ترمنځ د منځګړي کار کوي او د هر ډول پروګرامونو چلېدل کنټرولوي."')
P('Some commonly used operating systems that are used for personal computers are: Linux, Mac OS, Microsoft Windows XP, Microsoft Windows Vista, Windows 7 and UNIX.',
  'ذاتی کمپیوٹرز کے لیے عام استعمال ہونے والے کچھ آپریٹنگ سسٹم یہ ہیں: Linux، Mac OS، Microsoft Windows XP، Microsoft Windows Vista، Windows 7 اور UNIX۔',
  'د شخصي کمپیوټرونو لپاره ځینې عام کارېدونکي عملیاتي سیسټمونه دا دي: Linux، Mac OS، Microsoft Windows XP، Microsoft Windows Vista، Windows 7 او UNIX.')
P('A computer without an operating system is just an empty dump of metal. To run application programs on a computer, it must have an operating system installed on it. Operating systems perform basic operations, such as getting input from the input devices, transferring data from main memory to the processor for processing and then sending output to the output devices. It also keeps track of files and directories on the hard disk, and controls peripheral devices.',
  'آپریٹنگ سسٹم کے بغیر کمپیوٹر محض دھات کا ایک خالی ڈھیر ہے۔ کمپیوٹر پر ایپلیکیشن پروگرام چلانے کے لیے اس پر آپریٹنگ سسٹم انسٹال ہونا ضروری ہے۔ آپریٹنگ سسٹم بنیادی کام انجام دیتے ہیں، جیسے ان پٹ آلات سے ان پٹ لینا، ڈیٹا کو پراسیسنگ کے لیے مین میموری سے پروسیسر تک منتقل کرنا اور پھر آؤٹ پٹ کو آؤٹ پٹ آلات تک بھیجنا۔ یہ ہارڈ ڈسک پر فائلوں اور ڈائریکٹریز کا ریکارڈ بھی رکھتا ہے اور بیرونی آلات کو کنٹرول کرتا ہے۔',
  'له عملیاتي سیسټم پرته کمپیوټر یوازې د فلز یو تش ډېری دی. په کمپیوټر د کاريال پروګرامونو د چلولو لپاره باید عملیاتي سیسټم پرې نصب وي. عملیاتي سیسټمونه بنسټیزې چارې ترسره کوي، لکه له ننوتو وسایلو ننوتنه اخیستل، د پروسس لپاره له اصلي حافظې پروسېسر ته د ډېټا لېږدول او بیا وتو وسایلو ته د وتنې لېږل. دا په هارډ ډیسک کې د فایلونو او لارښودونو (directories) ریکارډ هم ساتي او بهرني وسایل کنټرولوي.')
P('Consider Figure 1.1 which shows that operating system is an interface between users and computer hardware.',
  'شکل 1.1 پر غور کیجیے جو ظاہر کرتی ہے کہ آپریٹنگ سسٹم صارفین اور کمپیوٹر ہارڈویئر کے درمیان ایک انٹرفیس ہے۔',
  '۱.۱ شکل ته پام وکړئ چې ښيي عملیاتي سیسټم د کاروونکو او کمپیوټري هارډویر ترمنځ منځګړی دی.')
en, ur, ps = fig_1_1()
t.visual('cs12-fig-1-1', en, ur, ps, 460 / 330)
P('Operating system operates on top of hardware and acts as a virtual machine that hides the hardware level complexities from the users and provides them a convenient way of using the system.',
  'آپریٹنگ سسٹم ہارڈویئر کے اوپر کام کرتا ہے اور ایک ورچوئل مشین کی طرح کام کرتا ہے جو ہارڈویئر کی سطح کی پیچیدگیوں کو صارفین سے چھپاتا ہے اور انھیں سسٹم استعمال کرنے کا آسان طریقہ فراہم کرتا ہے۔',
  'عملیاتي سیسټم د هارډویر پر سر کار کوي او د یوه مجازي ماشین په څېر عمل کوي چې د هارډویر د کچې پېچلتیاوې له کاروونکو پټوي او هغوی ته د سیسټم د کارولو اسانه لاره برابروي.')
H('1.1.2 Commonly used operating systems', '1.1.2 عام استعمال ہونے والے آپریٹنگ سسٹم', '۱.۱.۲ عام کارېدونکي عملیاتي سیسټمونه')
P('The development of operating system has started since 1950’s and different types of operating systems have been developed so far by different companies. The most commonly used operating systems are: DOS, Windows, UNIX and Macintosh.',
  'آپریٹنگ سسٹم کی تیاری 1950ء کی دہائی سے شروع ہوئی اور اب تک مختلف کمپنیوں نے مختلف اقسام کے آپریٹنگ سسٹم تیار کیے ہیں۔ سب سے زیادہ استعمال ہونے والے آپریٹنگ سسٹم یہ ہیں: DOS، Windows، UNIX اور Macintosh۔',
  'د عملیاتي سیسټم جوړول له ۱۹۵۰مو کلونو پیل شوي او تر اوسه بېلابېلو شرکتونو بېلابېل ډوله عملیاتي سیسټمونه جوړ کړي. تر ټولو ډېر کارېدونکي عملیاتي سیسټمونه دا دي: DOS، Windows، UNIX او Macintosh.')
H('a. DOS', 'a. ڈاس (DOS)', 'a. DOS')
P('DOS is the abbreviation for Disk Operating System which was the first operating system used for personal computers.',
  'DOS ڈسک آپریٹنگ سسٹم کا مخفف ہے جو ذاتی کمپیوٹرز کے لیے استعمال ہونے والا پہلا آپریٹنگ سسٹم تھا۔',
  'DOS د Disk Operating System لنډیز دی چې د شخصي کمپیوټرونو لپاره لومړنی کارېدونکی عملیاتي سیسټم و.')
UT = ('Operating System', 'آپریٹنگ سسٹم', 'عملیاتي سیسټم')
rec = BOOK.record(t, 'cs12-u1-text-1', 'Unit 1 text (1)', 'یونٹ 1 — متن (۱)', '۱ څپرکی — متن (۱)', 7, [2, 3])
rec['sourceNote'] = 'Figure 1.1 is reproduced as a coded diagram. The sub-heading printed as “1.1.1 An Operating System” appears with an owner pen mark over the number.'
issues = [{'id': 'cs12-pdf007', 'unit': 1, 'printedPage': 2,
           'description': 'p.2 prints “It also describes that how an operating system …” and “transferring” is cut at the margin; the definition quote ends “programs’.” in print. Owner pen annotations (circled numbers, scribbles) on pp.2–3 are excluded.'}]

if __name__ == '__main__':
    BOOK.save(7, [(1, rec)], issues=issues)
