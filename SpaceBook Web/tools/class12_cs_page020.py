"""Computer Science XII PDF20 (spread): printed pp.28–29 — Unit 1 exercise Q2 iii–ix; Q3 true/false i–viii."""
from class12_cs_common import BOOK, Builder

e = Builder()
N = ('None of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')
SS, OS, US, AS = ('System software', 'سسٹم سافٹ ویئر', 'سیسټم سافټویر'), ('Operating system', 'آپریٹنگ سسٹم', 'عملیاتي سیسټم'), ('Utility software', 'یوٹیلیٹی سافٹ ویئر', 'ګټور سافټویر'), ('Application software', 'ایپلیکیشن سافٹ ویئر', 'کاريال سافټویر')
e.mcq('iii.', ('Which one of the following is correct for multiprocessing operating systems?', 'ملٹی پروسیسنگ آپریٹنگ سسٹمز کے لیے درج ذیل میں سے کون سا درست ہے؟', 'د څو-پروسسي عملیاتي سیسټمونو لپاره له لاندې څخه کوم یو سم دی؟'),
      [('Used on systems having only one processor', 'صرف ایک پروسیسر والے سسٹمز پر استعمال ہوتے ہیں', 'یوازې پر یو-پروسېسوري سیسټمونو کارول کېږي'),
       ('Cannot execute more than one processes at a time', 'ایک وقت میں ایک سے زیادہ پراسیسز نہیں چلا سکتے', 'په یو وخت له یوې زیاتې پروسې نه شي اجرا کولی'),
       ('Run on systems which having more than one processors', 'ایک سے زیادہ پروسیسر والے سسٹمز پر چلتے ہیں', 'پر هغو سیسټمونو چلېږي چې له یوه زیات پروسېسرونه لري'), N], per_line=1)
e.mcq('iv.', ('Multiprogramming refers to:', 'ملٹی پروگرامنگ سے مراد ہے:', 'څو-پروګرامي کار ته اشاره ده:'),
      [('Having several programs in RAM at the same time', 'ایک ہی وقت میں RAM میں کئی پروگرام موجود ہونا', 'په یو وخت په RAM کې د څو پروګرامونو شتون'), ('Multiprocessing', 'ملٹی پروسیسنگ', 'څو-پروسسي کار'),
       ('Writing programs in multiple languages', 'متعدد زبانوں میں پروگرام لکھنا', 'په ډېرو ژبو پروګرامونه لیکل'), N], per_line=1)
e.mcq('v.', ('The most recently launched operating system of Microsoft is:', 'مائیکروسافٹ کا سب سے حالیہ جاری کردہ آپریٹنگ سسٹم ہے:', 'د مایکروسافټ تر ټولو وروستی خپور شوی عملیاتي سیسټم دی:'), ['Windows 98', 'Windows 8', 'DOS', 'Windows NT'], per_line=1)
e.mcq('vi.', ('Which of the following is not an operating system?', 'درج ذیل میں سے کون سا آپریٹنگ سسٹم نہیں ہے؟', 'له لاندې څخه کوم یو عملیاتي سیسټم نه دی؟'), ['Linux', 'MS Word', 'UNIX', 'Windows XP Professional'], per_line=1)
e.mcq('vii.', ('Which type of software enables you to solve specific problems or perform specific tasks?', 'کس قسم کا سافٹ ویئر آپ کو مخصوص مسائل حل کرنے یا مخصوص کام انجام دینے کے قابل بناتا ہے؟', 'کوم ډول سافټویر تاسو ته د ځانګړو ستونزو د حل یا ځانګړو دندو د ترسره کولو وړتیا درکوي؟'), [SS, OS, US, AS], per_line=1)
e.mcq('viii.', ('Which type of software controls your application software and manages how your hardware devices work together?', 'کس قسم کا سافٹ ویئر آپ کے ایپلیکیشن سافٹ ویئر کو کنٹرول کرتا ہے اور اس کا انتظام کرتا ہے کہ آپ کے ہارڈویئر آلات مل کر کیسے کام کریں؟', 'کوم ډول سافټویر ستاسو کاريال سافټویر کنټرولوي او اداره کوي چې ستاسو هارډویري وسایل څنګه یوځای کار وکړي؟'), [SS, OS, US, AS], per_line=1)
e.mcq('ix.', ('A technique in which a process, executing an application, is divided into threads that can run concurrently is called:', 'وہ تکنیک جس میں کسی ایپلیکیشن کو چلانے والا پراسیس ایسے تھریڈز میں تقسیم ہوتا ہے جو بیک وقت چل سکیں، کہلاتی ہے:', 'هغه تخنیک چې پکې یو کاريال اجرا کوونکې پروسه په داسې تارونو وېشل کېږي چې په یو وخت چلېدای شي، بلل کېږي:'),
      [('Multithreading', 'ملٹی تھریڈنگ', 'څو-تاریز کار'), ('Multiprocessing', 'ملٹی پروسیسنگ', 'څو-پروسسي کار'), ('Batch processing', 'بیچ پراسیسنگ', 'ډله‌ییز پروسس'), N], per_line=1)
e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
e.group('lines', [
 ('i. The operating system acts as an interface between the computer hardware and the human user.', 'i. آپریٹنگ سسٹم کمپیوٹر ہارڈویئر اور انسانی صارف کے درمیان انٹرفیس کا کام کرتا ہے۔', 'i. عملیاتي سیسټم د کمپیوټري هارډویر او انساني کاروونکي ترمنځ د منځګړي کار کوي.'),
 ('ii. Multiprogramming allows the processor to make use of idle time caused by I/O wait.', 'ii. ملٹی پروگرامنگ پروسیسر کو I/O انتظار سے پیدا ہونے والے فارغ وقت کو استعمال کرنے دیتی ہے۔', 'ii. څو-پروګرامي کار پروسېسر ته اجازه ورکوي چې د I/O انتظار له امله له وزګار وخت ګټه واخلي.'),
 ('iii. An operating system controls the execution of applications and acts as an interface between applications and the computer hardware.', 'iii. آپریٹنگ سسٹم ایپلیکیشنز کے چلنے کو کنٹرول کرتا ہے اور ایپلیکیشنز اور کمپیوٹر ہارڈویئر کے درمیان انٹرفیس کا کام کرتا ہے۔', 'iii. عملیاتي سیسټم د کاريالونو اجرا کنټرولوي او د کاريالونو او کمپیوټري هارډویر ترمنځ د منځګړي کار کوي.'),
 ('iv. In the early computers, the operating systems did not exist.', 'iv. ابتدائی کمپیوٹرز میں آپریٹنگ سسٹم موجود نہیں تھے۔', 'iv. په لومړنیو کمپیوټرونو کې عملیاتي سیسټمونه نه وو.'),
 ('v. Multi-programming do not provide better utilization of system resources than multiprogramming.', 'v. ملٹی پروگرامنگ، ملٹی پروگرامنگ کے مقابلے میں سسٹم کے وسائل کا بہتر استعمال فراہم نہیں کرتی۔', 'v. څو-پروګرامي کار د څو-پروګرامي کار په پرتله د سیسټم د سرچینو ښه کارونه نه برابروي.'),
 ('vi. In a time sharing system, when a process is assigned to the CPU for execution, it remains there till its completion.', 'vi. ٹائم شیئرنگ سسٹم میں جب کوئی پراسیس چلانے کے لیے CPU کو تفویض کیا جاتا ہے تو وہ مکمل ہونے تک وہیں رہتا ہے۔', 'vi. په وخت شریکونکي سیسټم کې کله چې یوه پروسه د اجرا لپاره CPU ته وسپارل شي، تر بشپړېدو هلته پاتې کېږي.'),
 ('vii. A process is a dispatchable unit of thread.', 'vii. پراسیس تھریڈ کی ایک قابلِ روانگی اکائی ہے۔', 'vii. پروسه د تار د لېږلو وړ واحد دی.'),
 ('viii. A process is directly assigned to the CPU for processing from a block state when the event for which it is waiting happens.', 'viii. جب وہ واقعہ پیش آ جائے جس کا پراسیس انتظار کر رہا ہو تو اسے بلاک حالت سے براہِ راست پراسیسنگ کے لیے CPU کو تفویض کر دیا جاتا ہے۔', 'viii. کله چې هغه پېښه وشي چې پروسه یې انتظار باسي، پروسه له بند حالت مستقیم د پروسس لپاره CPU ته سپارل کېږي.')])
ex = BOOK.record(e, 'cs12-u1-exercise-2', 'Unit 1 exercise (2)', 'یونٹ 1: مشق (۲)', '۱ څپرکی: تمرین (۲)', 20, [28, 29])
issues = [{'id': 'cs12-pdf020', 'unit': 1, 'printedPage': 28,
           'description': 'Q2(iii) options print “more than one processes” and “systems which having more than one processors”; Q2(v) asks for the most recent Microsoft OS with Windows 8 as the latest option; Q3(v) compares “Multi-programming … than multiprogramming” (likely “uniprogramming” intended). Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(20, [(1, ex)], issues=issues)
