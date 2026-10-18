"""Computer Science XII PDF14 (spread): printed pp.16–17 — i. embedded OS; 1.1.4 single-/multi-user; 1.2 OS functions; process management; memory management (begins)."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
H('i. Embedded operating system', 'i. ایمبیڈڈ آپریٹنگ سسٹم', 'i. ننښتی (Embedded) عملیاتي سیسټم')
P('Embedded operating systems are those operating systems which are designed for use in embedded computer systems. An embedded computer system is a computer which is a part of another system such as robot, missile etc.',
  'ایمبیڈڈ آپریٹنگ سسٹم وہ آپریٹنگ سسٹم ہیں جو ایمبیڈڈ کمپیوٹر سسٹمز میں استعمال کے لیے بنائے جاتے ہیں۔ ایمبیڈڈ کمپیوٹر سسٹم ایسا کمپیوٹر ہے جو کسی دوسرے نظام کا حصہ ہو، جیسے روبوٹ، میزائل وغیرہ۔',
  'ننښتي عملیاتي سیسټمونه هغه دي چې په ننښتو کمپیوټري سیسټمونو کې د کارولو لپاره ډیزاین شوي. ننښتی کمپیوټري سیسټم داسې کمپیوټر دی چې د بل سیسټم برخه وي، لکه روبوټ، توغندی او نور.')
P('These operating systems are designed for the operations of small machines like Personal Digital Assistant (PDA) with less autonomy. They can operate with limited number of resources. By design, these operating systems are very compact in size and efficient in performance. Windows CE, Embedded Linux and Android are the examples of embedded operating systems.',
  'یہ آپریٹنگ سسٹم کم خود مختاری والی چھوٹی مشینوں جیسے پرسنل ڈیجیٹل اسسٹنٹ (PDA) کے کاموں کے لیے بنائے جاتے ہیں۔ یہ محدود وسائل کے ساتھ کام کر سکتے ہیں۔ ساخت کے لحاظ سے یہ آپریٹنگ سسٹم سائز میں بہت مختصر اور کارکردگی میں مؤثر ہوتے ہیں۔ Windows CE، Embedded Linux اور Android ایمبیڈڈ آپریٹنگ سسٹمز کی مثالیں ہیں۔',
  'دا عملیاتي سیسټمونه د لږ خپلواکۍ لرونکو کوچنیو ماشینونو لکه شخصي ډیجیټل مرستیال (PDA) د چارو لپاره ډیزاین شوي. دوی د محدودو سرچینو سره کار کولی شي. د ډیزاین له مخې دا عملیاتي سیسټمونه په اندازه کې ډېر وړوکي او په کارکردګۍ کې اغېزمن وي. Windows CE، Embedded Linux او Android د ننښتو عملیاتي سیسټمونو بېلګې دي.')
H('1.1.4 Single-user and Multi-user Operating Systems', '1.1.4 سنگل یوزر اور ملٹی یوزر آپریٹنگ سسٹم', '۱.۱.۴ یو-کاروونکی او ډېر-کاروونکي عملیاتي سیسټمونه')
P('Operating systems can be divided into two categories as for as number of users are concerned.',
  'جہاں تک صارفین کی تعداد کا تعلق ہے، آپریٹنگ سسٹمز کو دو زمروں میں تقسیم کیا جا سکتا ہے۔',
  'تر هغه ځایه چې د کاروونکو شمېر ته اړه لري، عملیاتي سیسټمونه په دوو ډلو وېشل کېدای شي.')
H('a. Single-user operating systems', 'a. سنگل یوزر آپریٹنگ سسٹم', 'a. یو-کاروونکی عملیاتي سیسټمونه')
P('Single-user operating systems are those operating systems which are usable by a single user at a time. These operating systems execute a single process at a time on a single processor. Batch processing operating systems are the examples of single user operating systems.',
  'سنگل یوزر آپریٹنگ سسٹم وہ آپریٹنگ سسٹم ہیں جنھیں ایک وقت میں ایک ہی صارف استعمال کر سکتا ہے۔ یہ آپریٹنگ سسٹم ایک وقت میں ایک ہی پروسیسر پر ایک پراسیس چلاتے ہیں۔ بیچ پراسیسنگ آپریٹنگ سسٹم سنگل یوزر آپریٹنگ سسٹمز کی مثالیں ہیں۔',
  'یو-کاروونکي عملیاتي سیسټمونه هغه دي چې په یو وخت کې یوازې یو کاروونکی یې کارولی شي. دا عملیاتي سیسټمونه په یو وخت پر یوه پروسېسر یوه پروسه اجرا کوي. ډله‌ییز پروسس عملیاتي سیسټمونه د یو-کاروونکي عملیاتي سیسټمونو بېلګې دي.')
H('b. Multi-user operating systems', 'b. ملٹی یوزر آپریٹنگ سسٹم', 'b. ډېر-کاروونکي عملیاتي سیسټمونه')
P('Multi-user operating systems are those operating systems which allow multiple users to access a computer system at the same time. Time-sharing operating system is an example of multi-user operating systems as they enable multiple users to access a single computer by sharing of time. UNIX is an example of multi user operating system.',
  'ملٹی یوزر آپریٹنگ سسٹم وہ آپریٹنگ سسٹم ہیں جو متعدد صارفین کو ایک ہی وقت میں کمپیوٹر سسٹم تک رسائی کی اجازت دیتے ہیں۔ ٹائم شیئرنگ آپریٹنگ سسٹم ملٹی یوزر آپریٹنگ سسٹمز کی مثال ہے کیونکہ یہ وقت کی شراکت کے ذریعے متعدد صارفین کو ایک ہی کمپیوٹر تک رسائی دیتے ہیں۔ UNIX ملٹی یوزر آپریٹنگ سسٹم کی ایک مثال ہے۔',
  'ډېر-کاروونکي عملیاتي سیسټمونه هغه دي چې ډېرو کاروونکو ته په یو وخت کمپیوټري سیسټم ته د لاسرسي اجازه ورکوي. وخت شریکونکی عملیاتي سیسټم د ډېر-کاروونکي عملیاتي سیسټمونو بېلګه ده، ځکه د وخت په شریکولو ډېرو کاروونکو ته یوه کمپیوټر ته لاسرسی ورکوي. UNIX د ډېر-کاروونکي عملیاتي سیسټم بېلګه ده.')
H('1.2 OPERATING SYSTEM FUNCTIONS', '1.2 آپریٹنگ سسٹم کے افعال', '۱.۲ د عملیاتي سیسټم دندې')
P('As operating system is the main controller of a computer system, therefore, it provides a variety of services and functions to the computer and its users which are listed below:',
  'چونکہ آپریٹنگ سسٹم کمپیوٹر سسٹم کا مرکزی کنٹرولر ہے، اس لیے یہ کمپیوٹر اور اس کے صارفین کو مختلف خدمات اور افعال فراہم کرتا ہے جو درج ذیل ہیں:',
  'څرنګه چې عملیاتي سیسټم د کمپیوټري سیسټم اصلي کنټرولوونکی دی، نو کمپیوټر او د هغه کاروونکو ته بېلابېل خدمتونه او دندې برابروي چې لاندې لیکل شوي:')
t.group('list', [('Process Management', 'پراسیس مینجمنٹ', 'د پروسې اداره'), ('Memory Management', 'میموری مینجمنٹ', 'د حافظې اداره'), ('File Management', 'فائل مینجمنٹ', 'د فایلونو اداره'),
                 ('Input/output System Management', 'ان پٹ/آؤٹ پٹ سسٹم مینجمنٹ', 'د ننوتو/وتو د سیسټم اداره'), ('Secondary Storage Management', 'ثانوی اسٹوریج مینجمنٹ', 'د ثانوي زېرمې اداره'),
                 ('Network Management', 'نیٹ ورک مینجمنٹ', 'د شبکې اداره'), ('Protection System', 'حفاظتی نظام', 'د ساتنې سیسټم'), ('Command-interpreter', 'کمانڈ انٹرپریٹر', 'د امرونو ژباړونکی')])
H('Process management', 'پراسیس مینجمنٹ', 'د پروسې اداره')
P('A program under execution is called process. Early computer systems were able to run only one process on a single processor, but, now the concepts of multitasking and multiprogramming have enabled computers to run multiple programs on a single processor. Process management is that function of operating system in which it deals with running multiple processes on a single computer. Since, most of the computer systems contain one processor with one core, multitasking is done by simply switching processes quickly. If there are more processes to run on a processor, then the operating system decides whether to shorten the time slice for each process or to make the processes wait long for their next turns of execution.',
  'زیرِ عمل پروگرام کو پراسیس کہتے ہیں۔ ابتدائی کمپیوٹر سسٹم ایک پروسیسر پر صرف ایک پراسیس چلا سکتے تھے، لیکن اب ملٹی ٹاسکنگ اور ملٹی پروگرامنگ کے تصورات نے کمپیوٹرز کو ایک پروسیسر پر متعدد پروگرام چلانے کے قابل بنا دیا ہے۔ پراسیس مینجمنٹ آپریٹنگ سسٹم کا وہ فعل ہے جس میں وہ ایک کمپیوٹر پر متعدد پراسیسز کو چلانے سے نمٹتا ہے۔ چونکہ زیادہ تر کمپیوٹر سسٹمز میں ایک کور والا ایک پروسیسر ہوتا ہے، اس لیے ملٹی ٹاسکنگ صرف پراسیسز کو تیزی سے بدل کر کی جاتی ہے۔ اگر پروسیسر پر چلانے کے لیے زیادہ پراسیسز ہوں تو آپریٹنگ سسٹم فیصلہ کرتا ہے کہ ہر پراسیس کا وقتی حصہ کم کرے یا پراسیسز کو اپنی اگلی باری کا زیادہ دیر انتظار کرائے۔',
  'د اجرا لاندې پروګرام ته پروسه ویل کېږي. لومړني کمپیوټري سیسټمونه پر یوه پروسېسر یوازې یوه پروسه چلولی شوه، خو اوس د څو-دندیز او څو-پروګرامي کار مفهومونو کمپیوټرونه دې وړ کړي چې پر یوه پروسېسر ډېر پروګرامونه وچلوي. د پروسې اداره د عملیاتي سیسټم هغه دنده ده چې پکې پر یوه کمپیوټر د ډېرو پروسو له چلولو سره سروکار لري. څرنګه چې ډېری کمپیوټري سیسټمونه یو پروسېسر د یوه زړه (core) سره لري، څو-دندیز کار یوازې د پروسو په چټک بدلولو کېږي. که پر پروسېسر د چلولو لپاره ډېرې پروسې وي، نو عملیاتي سیسټم پرېکړه کوي چې د هرې پروسې د وخت برخه لنډه کړي یا پروسې د خپل راتلونکي نوبت لپاره اوږد انتظار ته پرېږدي.')
H('Memory management', 'میموری مینجمنٹ', 'د حافظې اداره')
P('Computer memory is a vital hardware resource of the computer system and it should be properly managed. It is grouped into Registers, CPU cache, Random Access Memory (RAM) and Disk Storage. A module of operating system called memory manager is responsible for the coordination of these types of memory by tracking which memory is',
  'کمپیوٹر میموری کمپیوٹر سسٹم کا ایک اہم ہارڈویئر وسیلہ ہے اور اس کا مناسب انتظام ہونا چاہیے۔ اسے رجسٹرز، CPU کیش، رینڈم ایکسیس میموری (RAM) اور ڈسک اسٹوریج میں تقسیم کیا جاتا ہے۔ آپریٹنگ سسٹم کا ایک ماڈیول جسے میموری مینیجر کہتے ہیں، ان اقسام کی میموری کی ہم آہنگی کا ذمہ دار ہے اور یہ ریکارڈ رکھتا ہے کہ کون سی میموری',
  'کمپیوټري حافظه د کمپیوټري سیسټم یوه حیاتي هارډویري سرچینه ده او باید په سم ډول اداره شي. په ثبتونکو (Registers)، د CPU کیش، تصادفي لاسرسي حافظه (RAM) او ډیسکي زېرمه ډلبندي کېږي. د عملیاتي سیسټم یوه ماډیول چې د حافظې مدیر بلل کېږي، د دې ډولونو حافظې د همغږۍ مسؤول دی او څاري چې کومه حافظه')
rec = BOOK.record(t, 'cs12-u1-text-8', 'Unit 1 text (8)', 'یونٹ 1 — متن (۸)', '۱ څپرکی — متن (۸)', 14, [16, 17])
rec['sourceNote'] = 'The memory-management paragraph breaks at the foot of p.17 and continues on p.18 (PDF15).'
issues = [{'id': 'cs12-pdf014', 'unit': 1, 'printedPage': 16,
           'description': 'p.16 prints “as for as number of users are concerned” (for “as far as”). Retained as printed. Owner notes (“function”, circled numbers, a strike line on p.17) excluded.'}]

if __name__ == '__main__':
    BOOK.save(14, [(1, rec)], issues=issues)
