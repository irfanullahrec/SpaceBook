"""Computer Science XII PDF8 (spread): printed pp.4–5 — DOS history, Figure 1.2 (MS-DOS screen as code block), DOS commands; b. Windows: history and features."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('DOS operating system was developed in 1980 by Microsoft when, in July 1980, the IBM assigned a project to Microsoft for the development of a 16-bit operating system for their personal computer. Microsoft developed the first version of DOS for the personal computer and named it PC-DOS. After this, Microsoft developed a Microsoft version of the same PC-DOS operating system and named it MS-DOS. Both PC-DOS and MS-DOS are almost similar and now users refer them with only DOS.',
  'DOS آپریٹنگ سسٹم 1980ء میں مائیکروسافٹ نے اس وقت تیار کیا جب جولائی 1980ء میں IBM نے اپنے ذاتی کمپیوٹر کے لیے 16-بٹ آپریٹنگ سسٹم کی تیاری کا منصوبہ مائیکروسافٹ کو سونپا۔ مائیکروسافٹ نے ذاتی کمپیوٹر کے لیے DOS کا پہلا ورژن تیار کیا اور اس کا نام PC-DOS رکھا۔ اس کے بعد مائیکروسافٹ نے اسی PC-DOS آپریٹنگ سسٹم کا مائیکروسافٹ ورژن تیار کیا اور اس کا نام MS-DOS رکھا۔ PC-DOS اور MS-DOS دونوں تقریباً یکساں ہیں اور اب صارفین انھیں صرف DOS کہتے ہیں۔',
  'DOS عملیاتي سیسټم په ۱۹۸۰ز کې مایکروسافټ هغه وخت جوړ کړ چې د ۱۹۸۰ز په جولای کې IBM مایکروسافټ ته د خپل شخصي کمپیوټر لپاره د ۱۶-بټه عملیاتي سیسټم د جوړولو پروژه وسپارله. مایکروسافټ د شخصي کمپیوټر لپاره د DOS لومړۍ نسخه جوړه کړه او PC-DOS یې ونوماوه. له دې وروسته مایکروسافټ د همدې PC-DOS عملیاتي سیسټم د مایکروسافټ نسخه جوړه کړه او MS-DOS یې ونوماوه. PC-DOS او MS-DOS دواړه نږدې یو شان دي او اوس کاروونکي یې یوازې DOS بولي.')
P('In Figure 1.2 a snapshot of Microsoft DOS Operating System is shown with some basic commands: DIR and VER.',
  'شکل 1.2 میں مائیکروسافٹ DOS آپریٹنگ سسٹم کی ایک تصویر کچھ بنیادی کمانڈز DIR اور VER کے ساتھ دکھائی گئی ہے۔',
  'په ۱.۲ شکل کې د مایکروسافټ DOS عملیاتي سیسټم یو انځور د ځینو بنسټیزو امرونو DIR او VER سره ښودل شوی.')
code(t, r'''C:\>dir

Volume in drive C is MS-DOS 6_0
Volume Serial Number is 446B-2781
Directory of C:\

COMMAND  COM      52925 03-10-93   6:00a
        1 file(s)        52925 bytes
                      10219520 bytes free

C:\>ver

MS-DOS Version 6.00

C:\>''')
P('Figure 1.2 MS DOS Operating System', 'شکل 1.2 ایم ایس ڈاس آپریٹنگ سسٹم', '۱.۲ شکل: MS DOS عملیاتي سیسټم')
P('The most commonly used DOS commands are:', 'سب سے زیادہ استعمال ہونے والی DOS کمانڈز یہ ہیں:', 'تر ټولو ډېر کارېدونکي DOS امرونه دا دي:')
cmds = [('CD', 'changes the current directory', 'موجودہ ڈائریکٹری بدلتی ہے', 'اوسنی لارښود بدلوي'), ('COPY', 'copies a file', 'فائل کاپی کرتی ہے', 'فایل کاپي کوي'),
        ('DEL', 'deletes a file', 'فائل حذف کرتی ہے', 'فایل ړنګوي'), ('DIR', 'lists directory contents', 'ڈائریکٹری کے مندرجات کی فہرست دکھاتی ہے', 'د لارښود منځپانګې لېست کوي'),
        ('EDIT', 'starts an editor to create or edit plain text files', 'سادہ ٹیکسٹ فائلیں بنانے یا ان میں ترمیم کے لیے ایڈیٹر شروع کرتی ہے', 'د ساده متني فایلونو د جوړولو یا سمولو لپاره سمونګر پیلوي'),
        ('FORMAT', 'formats a disk to accept DOS files', 'ڈسک کو DOS فائلیں قبول کرنے کے لیے فارمیٹ کرتی ہے', 'ډیسک د DOS فایلونو منلو لپاره بڼه‌کوي'),
        ('HELP', 'displays information about a command', 'کسی کمانڈ کے بارے میں معلومات دکھاتی ہے', 'د یوه امر په اړه معلومات ښيي'), ('MKDIR', 'creates a new directory', 'نئی ڈائریکٹری بناتی ہے', 'نوی لارښود جوړوي'),
        ('RD', 'removes a directory', 'ڈائریکٹری ہٹاتی ہے', 'لارښود لرې کوي'), ('REN', 'renames a file', 'فائل کا نام بدلتی ہے', 'د فایل نوم بدلوي'),
        ('TYPE', 'displays contents of a file on the screen', 'فائل کے مندرجات اسکرین پر دکھاتی ہے', 'د فایل منځپانګه پر پرده ښيي')]
t.group('lines', [(f'{c} - {e}', f'{c} - {u}', f'{c} - {p}') for c, e, u, p in cmds])
H('b. Windows', 'b. ونڈوز', 'b. وینډوز')
P('Windows operating systems are the most commonly used operating systems that are based on Graphical User Interfaces (GUI).',
  'ونڈوز آپریٹنگ سسٹم سب سے زیادہ استعمال ہونے والے آپریٹنگ سسٹم ہیں جو گرافیکل یوزر انٹرفیس (GUI) پر مبنی ہیں۔',
  'وینډوز عملیاتي سیسټمونه تر ټولو ډېر کارېدونکي عملیاتي سیسټمونه دي چې پر ګرافیکي کاروونکي منځګړي (GUI) ولاړ دي.')
H('i. Brief history of windows operating system', 'i. ونڈوز آپریٹنگ سسٹم کی مختصر تاریخ', 'i. د وینډوز عملیاتي سیسټم لنډ تاریخ')
P('The history of windows operating system goes back to 1983. The first windows operating system “Windows 1.0” was launched on November 20, 1985. The graphical support with desktop icons was introduced in “windows 2.0” that was launched on December 9, 1987. On August 24, 1995, “windows 95” was launched. Windows 98, XP and Vista were released on June 25, 1998, October 25, 2001 and 2006 respectively. In October 2009 windows 7 was released and Windows 8 was released on October 2012.',
  'ونڈوز آپریٹنگ سسٹم کی تاریخ 1983ء تک جاتی ہے۔ پہلا ونڈوز آپریٹنگ سسٹم ’’Windows 1.0‘‘ 20 نومبر 1985ء کو جاری ہوا۔ ڈیسک ٹاپ آئیکنز کے ساتھ گرافیکل معاونت ’’windows 2.0‘‘ میں متعارف ہوئی جو 9 دسمبر 1987ء کو جاری ہوا۔ 24 اگست 1995ء کو ’’windows 95‘‘ جاری ہوا۔ Windows 98، XP اور Vista بالترتیب 25 جون 1998ء، 25 اکتوبر 2001ء اور 2006ء میں جاری ہوئے۔ اکتوبر 2009ء میں windows 7 اور اکتوبر 2012ء میں Windows 8 جاری ہوا۔',
  'د وینډوز عملیاتي سیسټم تاریخ ۱۹۸۳ز ته رسېږي. لومړنی وینډوز عملیاتي سیسټم "Windows 1.0" د ۱۹۸۵ز د نومبر په ۲۰مه خپور شو. د ډیسکټاپ نښو سره ګرافیکي ملاتړ په "windows 2.0" کې معرفي شو چې د ۱۹۸۷ز د ډسمبر په ۹مه خپور شو. د ۱۹۹۵ز د اګست په ۲۴مه "windows 95" خپور شو. Windows 98، XP او Vista په ترتیب سره د ۱۹۹۸ز د جون په ۲۵مه، د ۲۰۰۱ز د اکتوبر په ۲۵مه او په ۲۰۰۶ز کې خپاره شول. د ۲۰۰۹ز په اکتوبر کې windows 7 او د ۲۰۱۲ز په اکتوبر کې Windows 8 خپور شو.')
H('ii. Features of windows operating system', 'ii. ونڈوز آپریٹنگ سسٹم کی خصوصیات', 'ii. د وینډوز عملیاتي سیسټم ځانګړنې')
t.group('list', [
 ('Windows operating system has improved graphical user interface that can be easily used by every type of user.', 'ونڈوز آپریٹنگ سسٹم کا گرافیکل یوزر انٹرفیس بہتر ہے جسے ہر قسم کا صارف آسانی سے استعمال کر سکتا ہے۔', 'د وینډوز عملیاتي سیسټم ښه شوی ګرافیکي کاروونکي منځګړی لري چې هر ډول کاروونکی یې په اسانۍ کارولی شي.'),
 ('Windows operating systems are user friendly.', 'ونڈوز آپریٹنگ سسٹم صارف دوست ہیں۔', 'وینډوز عملیاتي سیسټمونه کاروونکي-دوست دي.'),
 ('These are the best operating systems running on PCs.', 'یہ ذاتی کمپیوٹرز پر چلنے والے بہترین آپریٹنگ سسٹم ہیں۔', 'دا په شخصي کمپیوټرونو چلېدونکي تر ټولو ښه عملیاتي سیسټمونه دي.'),
 ('Windows series of operating systems are not very expensive for home users.', 'ونڈوز کے آپریٹنگ سسٹم گھریلو صارفین کے لیے زیادہ مہنگے نہیں ہیں۔', 'د وینډوز لړۍ عملیاتي سیسټمونه د کور کاروونکو لپاره ډېر ګران نه دي.'),
 ('Windows operating systems are supported by most of the software.', 'زیادہ تر سافٹ ویئر ونڈوز آپریٹنگ سسٹم کو سپورٹ کرتے ہیں۔', 'ډېری سافټویرونه د وینډوز عملیاتي سیسټمونو ملاتړ کوي.')])
rec = BOOK.record(t, 'cs12-u1-text-2', 'Unit 1 text (2)', 'یونٹ 1 — متن (۲)', '۱ څپرکی — متن (۲)', 8, [4, 5])
rec['sourceNote'] = 'Figure 1.2 (an MS-DOS screen photograph) is reproduced as a monospaced code listing of the screen text. Command names are kept in English in all language views.'
issues = [{'id': 'cs12-pdf008', 'unit': 1, 'printedPage': 5,
           'description': 'p.5 prints “Windows 8 was released on October 2012” (missing “in”); the DOS screen prints “MS-DOS 6_0” and serial “446B-2781”. Owner pen notes (“Bill gates”, circled numbers, scribbles) on pp.4–5 are excluded.'}]

if __name__ == '__main__':
    BOOK.save(8, [(1, rec)], issues=issues)
