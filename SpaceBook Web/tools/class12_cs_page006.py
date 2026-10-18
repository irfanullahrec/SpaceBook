"""Computer Science XII PDF6: left = contents end (recorded with PDF3); right = p.1 Unit 1 opener — learning outcomes."""
from class12_cs_common import BOOK, Builder

t = Builder()
t.p('Unit 1', 'یونٹ 1', '۱ څپرکی')
t.h('OPERATING SYSTEM', 'آپریٹنگ سسٹم', 'عملیاتي سیسټم')
t.h('After the completion of Unit-1, Students will be able to:', 'یونٹ 1 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۱ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
L = lambda rows: t.group('list', rows)
L([('Define an operating system.', 'آپریٹنگ سسٹم کی تعریف کر سکیں۔', 'عملیاتي سیسټم تعریف کړي.'),
   ('Describe commonly used operating systems (DOS, Windows, Unix, Macintosh).', 'عام استعمال ہونے والے آپریٹنگ سسٹمز (DOS، Windows، Unix، Macintosh) بیان کر سکیں۔', 'عام کارېدونکي عملیاتي سیسټمونه (DOS، Windows، Unix، Macintosh) بیان کړي.'),
   ('Explain the following types of operating systems:', 'آپریٹنگ سسٹمز کی درج ذیل اقسام کی وضاحت کر سکیں:', 'د عملیاتي سیسټمونو لاندې ډولونه تشریح کړي:')])
L([('Batch processing operating system', 'بیچ پراسیسنگ آپریٹنگ سسٹم', 'ډله‌ییز پروسس عملیاتي سیسټم'),
   ('Multiprogramming operating system', 'ملٹی پروگرامنگ آپریٹنگ سسٹم', 'څو-پروګرامي عملیاتي سیسټم'),
   ('Multitasking operating system', 'ملٹی ٹاسکنگ آپریٹنگ سسٹم', 'څو-دندیز عملیاتي سیسټم'),
   ('Time-Sharing operating system', 'ٹائم شیئرنگ آپریٹنگ سسٹم', 'د وخت شریکونکی عملیاتي سیسټم'),
   ('Real Time operating system', 'ریئل ٹائم آپریٹنگ سسٹم', 'سمدستي (Real Time) عملیاتي سیسټم'),
   ('Multiprocessor operating system', 'ملٹی پروسیسر آپریٹنگ سسٹم', 'څو-پروسېسوري عملیاتي سیسټم'),
   ('Parallel processing operating system', 'پیرالل پراسیسنگ آپریٹنگ سسٹم', 'موازي پروسس عملیاتي سیسټم'),
   ('Distributed operating system', 'ڈسٹری بیوٹڈ آپریٹنگ سسٹم', 'وېشل شوی عملیاتي سیسټم'),
   ('Embedded operating system', 'ایمبیڈڈ آپریٹنگ سسٹم', 'ننښتي (Embedded) عملیاتي سیسټم')])
L([('Describe features/characteristics of Single-user and Multi-user operating systems.', 'سنگل یوزر اور ملٹی یوزر آپریٹنگ سسٹمز کی خصوصیات بیان کر سکیں۔', 'د یو-کاروونکي او ډېر-کاروونکو عملیاتي سیسټمونو ځانګړنې بیان کړي.'),
   ('Describe the following functions of operating systems:', 'آپریٹنگ سسٹمز کے درج ذیل افعال بیان کر سکیں:', 'د عملیاتي سیسټمونو لاندې دندې بیان کړي:')])
L([('Process management', 'پراسیس مینجمنٹ', 'د پروسې اداره'), ('Memory management', 'میموری مینجمنٹ', 'د حافظې اداره'), ('File management', 'فائل مینجمنٹ', 'د فایلونو اداره'),
   ('I/O system management', 'ان پٹ/آؤٹ پٹ سسٹم مینجمنٹ', 'د ننوتو/وتو د سیسټم اداره'), ('Secondary storage management', 'ثانوی اسٹوریج مینجمنٹ', 'د ثانوي زېرمې اداره'),
   ('Network management', 'نیٹ ورک مینجمنٹ', 'د شبکې اداره'), ('Protection system', 'حفاظتی نظام', 'د ساتنې سیسټم'), ('Command-interpreter', 'کمانڈ انٹرپریٹر', 'د امرونو ژباړونکی')])
L([('Define a process.', 'پراسیس کی تعریف کر سکیں۔', 'پروسه تعریف کړي.'),
   ('Describe the new, running, waiting/block, ready and terminated states of a process.', 'پراسیس کی نئی، چلتی، انتظار/بلاک، تیار اور ختم شدہ حالتیں بیان کر سکیں۔', 'د پروسې نوی، روان، انتظار/بند، چمتو او پای ته رسېدلي حالتونه بیان کړي.'),
   ('Differentiate between:', 'درج ذیل میں فرق کر سکیں:', 'د لاندې ترمنځ توپیر وکړي:')])
L([('Thread and Process', 'تھریڈ اور پراسیس', 'تار (Thread) او پروسه'), ('Multi-threading and Multi-tasking', 'ملٹی تھریڈنگ اور ملٹی ٹاسکنگ', 'څو-تاریز او څو-دندیز کار'),
   ('Multi-tasking and Multi-programming', 'ملٹی ٹاسکنگ اور ملٹی پروگرامنگ', 'څو-دندیز او څو-پروګرامي کار')])
UT = ('Operating System', 'آپریٹنگ سسٹم', 'عملیاتي سیسټم')
rec = BOOK.record(t, 'cs12-u1-outcomes', 'Unit 1: learning outcomes', 'یونٹ 1: حاصلاتِ تعلم', '۱ څپرکی: د زده‌کړې پایلې', 6, [1], unit_title=UT)
rec['sourceNote'] = 'The left page of PDF6 is the end of the contents (recorded with PDF3). Nested bullet lists are flattened into consecutive lists.'

if __name__ == '__main__':
    BOOK.save(6, [(1, rec)])
