"""Computer Science XII PDF35 (spread): printed pp.58–59 — 3.1 introduction; 3.1.1 program; 3.1.2 header files and reserved words; header example; Table 3.1 keywords."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('3.1 INTRODUCTION', '3.1 تعارف', '۳.۱ پېژندنه')
P('This Unit is about the introduction to Object Oriented Programming Language, C++, and covers its basics in detail. The Unit is focused on basic C++ program structure, variables used in C++, input/output statements and the use of operators in the language.',
  'یہ یونٹ آبجیکٹ اورینٹڈ پروگرامنگ زبان C++ کے تعارف کے بارے میں ہے اور اس کی بنیادی باتوں کا تفصیل سے احاطہ کرتا ہے۔ یونٹ بنیادی C++ پروگرام کی ساخت، C++ میں استعمال ہونے والے ویری ایبلز، ان پٹ/آؤٹ پٹ بیانات اور زبان میں آپریٹرز کے استعمال پر مرکوز ہے۔',
  'دا څپرکی د شیانو ته متوجه پروګرامي ژبې C++ د پېژندنې په اړه دی او بنسټونه یې په تفصیل سره رانغاړي. څپرکی د C++ پر بنسټیز پروګرامي جوړښت، په C++ کې کارېدونکو متغیرونو، د ننوتو/وتو بیانونو او په ژبه کې د چلونکو پر کارونې تمرکز لري.')
P('Bjarne Stroustrup at Bell Labs initially developed C++ during the early 1980’s. It was designed to support the features of C such as efficiency and low-level support for system level coding. Added to this were features such as classes with inheritance and virtual functions, derived from the Simula language, and operator overloading, derived from Algol. C++ is best described as a superset of C, with full support for object-oriented programming. This language is in wide spread use. The first commercial release of the C++ language was in October of 1985.',
  'بیل لیبز میں بیارنے اسٹراؤسٹرپ نے 1980ء کی دہائی کے اوائل میں ابتدائی طور پر C++ تیار کی۔ اسے C کی خصوصیات جیسے کارکردگی اور سسٹم کی سطح کی کوڈنگ کے لیے نچلی سطح کی معاونت کے لیے بنایا گیا تھا۔ اس میں Simula زبان سے ماخوذ وراثت اور ورچوئل فنکشنز والی کلاسز اور Algol سے ماخوذ آپریٹر اوورلوڈنگ جیسی خصوصیات شامل کی گئیں۔ C++ کو بہترین طور پر C کا ایک وسیع تر مجموعہ (superset) کہا جا سکتا ہے جو آبجیکٹ اورینٹڈ پروگرامنگ کی مکمل معاونت کرتا ہے۔ یہ زبان بڑے پیمانے پر استعمال ہوتی ہے۔ C++ زبان کا پہلا تجارتی اجراء اکتوبر 1985ء میں ہوا۔',
  'په بیل لابز کې بیارنې سټراوسټروپ په لومړي ځل د ۱۹۸۰مو کلونو په پیل کې C++ جوړه کړه. دا د C د ځانګړنو لکه اغېزمنتیا او د سیسټم د کچې کوډ لیکنې لپاره د ټیټې کچې ملاتړ لپاره ډیزاین شوې وه. ورسره داسې ځانګړنې ورزیاتې شوې لکه د میراث او مجازي فنکشنونو لرونکي ټولګي چې له Simula ژبې اخیستل شوي، او د چلونکو ډېرول (operator overloading) چې له Algol اخیستل شوی. C++ په ښه توګه د C پراخه ټولګه (superset) بلل کېدای شي چې د شیانو ته متوجه پروګرام‌سازۍ بشپړ ملاتړ کوي. دا ژبه په پراخه کچه کارېږي. د C++ ژبې لومړنی سوداګریز خپرېدل د ۱۹۸۵ز په اکتوبر کې وو.')
H('3.1.1 Computer program', '3.1.1 کمپیوٹر پروگرام', '۳.۱.۱ کمپیوټري پروګرام')
P('A computer program is a set of instructions written in computer languages to perform a specified task for a computer. A computer program tells the computer that what to do and in which order to do. Different types of programming languages are used to develop programs. Some commonly used programming languages are C++, JAVA, SQL, HTML, etc.',
  'کمپیوٹر پروگرام کمپیوٹر زبانوں میں لکھی گئی ہدایات کا ایک مجموعہ ہے جو کمپیوٹر کے لیے ایک مخصوص کام انجام دیتا ہے۔ کمپیوٹر پروگرام کمپیوٹر کو بتاتا ہے کہ کیا کرنا ہے اور کس ترتیب سے کرنا ہے۔ پروگرام تیار کرنے کے لیے مختلف اقسام کی پروگرامنگ زبانیں استعمال ہوتی ہیں۔ کچھ عام استعمال ہونے والی پروگرامنگ زبانیں C++، JAVA، SQL، HTML وغیرہ ہیں۔',
  'کمپیوټري پروګرام په کمپیوټري ژبو لیکل شویو لارښوونو یوه ټولګه ده چې د کمپیوټر لپاره یوه ټاکلې دنده ترسره کوي. کمپیوټري پروګرام کمپیوټر ته وايي چې څه وکړي او په کوم ترتیب یې وکړي. د پروګرامونو د جوړولو لپاره بېلابېل ډوله پروګرامي ژبې کارول کېږي. ځینې عام کارېدونکې پروګرامي ژبې C++، JAVA، SQL، HTML او نورې دي.')
H('3.1.2 Header files and Reserved words', '3.1.2 ہیڈر فائلیں اور مخصوص الفاظ', '۳.۱.۲ سرلیک فایلونه او ځانګړې کلمې')
P('Header files and reserved words are the two important components of almost every C++ programs.', 'ہیڈر فائلیں اور مخصوص الفاظ تقریباً ہر C++ پروگرام کے دو اہم اجزاء ہیں۔', 'سرلیک فایلونه او ځانګړې کلمې د نږدې هر C++ پروګرام دوه مهمې برخې دي.')
H('a. Header files', 'a. ہیڈر فائلیں', 'a. سرلیک فایلونه')
P('Header files also known as include files, are standard library files that have an extension of (.h) and which are used to hold declarations for other files.',
  'ہیڈر فائلیں، جنھیں انکلوڈ فائلیں بھی کہا جاتا ہے، معیاری لائبریری فائلیں ہیں جن کی ایکسٹینشن (.h) ہوتی ہے اور جو دوسری فائلوں کے اعلانات رکھنے کے لیے استعمال ہوتی ہیں۔',
  'سرلیک فایلونه چې شاملې فایلونه (include files) هم بلل کېږي، معیاري کتابتون فایلونه دي چې (.h) پسوند لري او د نورو فایلونو د اعلانونو ساتلو لپاره کارول کېږي.')
P('Consider the following program:', 'درج ذیل پروگرام پر غور کریں:', 'لاندې پروګرام ته پام وکړئ:')
code(t, '''// header file example
#include <iostream.h>
int main()
{
cout << "Hello, world!" << endl;
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'Hello, world!')
P('This program prints the string “Hello, world!” to the screen using cout. However, this program never defines cout, so how does the compiler know about the object cout? The answer for this is that cout has been declared in a header file called “iostream”. When the line #include <iostream.h> is used in the program, the compiler locates and read all the declarations from a header file named “iostream”.',
  'یہ پروگرام cout کے ذریعے اسٹرنگ ’’Hello, world!‘‘ اسکرین پر پرنٹ کرتا ہے۔ تاہم یہ پروگرام کبھی cout کی تعریف نہیں کرتا، تو کمپائلر کو آبجیکٹ cout کا کیسے پتہ چلتا ہے؟ اس کا جواب یہ ہے کہ cout کا اعلان ’’iostream‘‘ نامی ہیڈر فائل میں کیا گیا ہے۔ جب پروگرام میں #include <iostream.h> لائن استعمال ہوتی ہے تو کمپائلر ’’iostream‘‘ نامی ہیڈر فائل کو تلاش کر کے اس کے تمام اعلانات پڑھتا ہے۔',
  'دا پروګرام د cout په مرسته "Hello, world!" تار پر پرده چاپوي. خو دا پروګرام هېڅکله cout نه تعریفوي، نو کمپایلر د cout شي څخه څنګه خبرېږي؟ ځواب یې دا دی چې cout په "iostream" نومي سرلیک فایل کې اعلان شوی. کله چې په پروګرام کې د #include <iostream.h> کرښه وکارول شي، کمپایلر "iostream" نومی سرلیک فایل پیدا کوي او ټول اعلانونه یې لولي.')
H('b. Reserved words', 'b. مخصوص الفاظ', 'b. ځانګړې کلمې')
P('Reserved words or keywords are those words which have their special meaning within the C++ language and are reserved for some specific purpose. C++ reserved words cannot be used for any other purpose in a C++ program and even cannot be used as variables. Here is a list of C++ keywords shown in Table 3.1.',
  'مخصوص الفاظ یا کی ورڈز وہ الفاظ ہیں جن کا C++ زبان میں خاص مطلب ہوتا ہے اور جو کسی مخصوص مقصد کے لیے مختص ہوتے ہیں۔ C++ کے مخصوص الفاظ کسی C++ پروگرام میں کسی اور مقصد کے لیے استعمال نہیں ہو سکتے، حتیٰ کہ ویری ایبلز کے طور پر بھی نہیں۔ جدول 3.1 میں C++ کی ورڈز کی فہرست دی گئی ہے۔',
  'ځانګړې کلمې یا کلیدي کلمې هغه کلمې دي چې د C++ ژبې دننه ځانګړې معنا لري او د یوې ځانګړې موخې لپاره ساتل شوې دي. د C++ ځانګړې کلمې په C++ پروګرام کې د بلې موخې لپاره نه شي کارول کېدای، حتی د متغیرونو په توګه هم نه. د C++ کلیدي کلمو لېست په ۳.۱ جدول کې ښودل شوی.')
kw = ['asm', 'auto', 'bool', 'break', 'case', 'catch', 'char', 'class', 'const', 'const_cast', 'continue', 'default', 'delete', 'do', 'double', 'dynamic_cast',
      'else', 'enum', 'explicit', 'export', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int', 'long', 'mutable', 'namespace',
      'new', 'operator', 'private', 'protected', 'public', 'register', 'reinterpret_cast', 'return', 'short', 'signed', 'sizeof', 'static', 'static_cast', 'struct', 'switch', 'template',
      'this', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while', '']
rows = [kw[i:i + 8] for i in range(0, len(kw), 8)]
hdr = [''] * 8
t.table('cs12-table-3-1', hdr, rows, hdr, hdr, rows, rows, noHeader=True)
P('Table 3.1: List of C++ Keywords', 'جدول 3.1: C++ کی ورڈز کی فہرست', '۳.۱ جدول: د C++ کلیدي کلمو لېست')
UT = ('Object Oriented Programming Using C++', 'سی پلس پلس کے ذریعے آبجیکٹ اورینٹڈ پروگرامنگ', 'د C++ په مرسته شیانو ته متوجه پروګرام‌سازي')
rec = BOOK.record(t, 'cs12-u3-text-1', 'Unit 3 text (1)', 'یونٹ 3 — متن (۱)', '۳ څپرکی — متن (۱)', 35, [58, 59])
rec['sourceNote'] = 'Program listings and C++ keywords are kept in English in all language views. Table 3.1 is reproduced as an 8-column grid in the printed order (the last cell is empty in print).'
issues = [{'id': 'cs12-pdf035', 'unit': 3, 'printedPage': 59,
           'description': 'p.58 prints “C++programs” and “tells the computer that what to do”; p.59 “the compiler locates and read all the declarations”. Retained as printed. The contents list Unit 3 at p.59 and 3.1 at p.58; the opener is printed on p.57.'}]

if __name__ == '__main__':
    BOOK.save(35, [(3, rec)], issues=issues)
