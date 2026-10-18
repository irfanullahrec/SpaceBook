"""Computer Science XII PDF48 (spread): printed pp.84–85 — puts() output; c. getch() + example; 3.3.4 escape sequences; Table 3.3."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Enter a string
Hello World
You entered: Hello World''')
H('c. getch() function', 'c. getch() فنکشن', 'c. getch() فنکشن')
P('getch() function is a function that obtains the next available keystroke or character from the console. As a result of this function, nothing is echoed on the screen. When no keystroke is available, the function waits until a key is pressed. The value of the keystroke is returned by the function when a key is pressed. Its general syntax is:',
  'getch() فنکشن کنسول سے اگلی دستیاب کلید یا حرف حاصل کرتا ہے۔ اس فنکشن کے نتیجے میں اسکرین پر کچھ ظاہر نہیں ہوتا۔ جب کوئی کلید دستیاب نہ ہو تو فنکشن کسی کلید کے دبنے تک انتظار کرتا ہے۔ کلید دبنے پر فنکشن اس کی قدر واپس کرتا ہے۔ اس کا عمومی طریقۂ تحریر یہ ہے:',
  'getch() فنکشن له کنسول څخه راتلونکې شته کیلي یا توری ترلاسه کوي. د دې فنکشن په پایله کې پر پرده هېڅ نه ښکاري. کله چې هېڅ کیلي نه وي کېکښل شوې، فنکشن تر هغه انتظار کوي چې کیلي کېکښل شي. د کیلي ارزښت د کېکښلو پر وخت فنکشن بېرته ورکوي. عمومي بڼه یې دا ده:')
code(t, 'getch( );')
P('Consider the following C++ program that demonstrates the use of getch() function.', 'درج ذیل C++ پروگرام پر غور کریں جو getch() فنکشن کا استعمال دکھاتا ہے۔', 'لاندې C++ پروګرام ته پام وکړئ چې د getch() فنکشن کارونه ښيي.')
code(t, '''/* getch() example */
#include <stdio.h>
#include <conio.h>
#include <iostream.h>
int main()
{
char ch;
cout<< "Press any key\\n";
ch = getch();
cout<<"You pressed: " << ch <<endl;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Press any key
S
You pressed: S''')
H('3.3.4 Escape sequences', '3.3.4 ایسکیپ سیکوینسز', '۳.۳.۴ د تېښتې لړۍ (Escape sequences)')
P('C++ has some characters that have special meaning. These characters are called escape sequences. An escape sequence starts with a \\ followed by a letter or number.',
  'C++ میں کچھ حروف کا خاص مطلب ہوتا ہے۔ ان حروف کو ایسکیپ سیکوینسز کہتے ہیں۔ ایسکیپ سیکوینس \\ سے شروع ہوتا ہے اور اس کے بعد کوئی حرف یا عدد آتا ہے۔',
  'C++ ځینې داسې توري لري چې ځانګړې معنا لري. دې تورو ته د تېښتې لړۍ (escape sequences) ویل کېږي. د تېښتې لړۍ په \\ پیلېږي او ورپسې یو توری یا عدد راځي.')
P('Table 3.3 shows the list of all escape sequences that are used in C++ along with their purpose.', 'جدول 3.3 میں C++ میں استعمال ہونے والے تمام ایسکیپ سیکوینسز کی فہرست ان کے مقصد کے ساتھ دکھائی گئی ہے۔', '۳.۳ جدول په C++ کې د کارېدونکو ټولو د تېښتې لړیو لېست د هغوی د موخې سره ښيي.')
E = [(('Alert', 'الرٹ', 'خبرتیا'), '\\a', ('Makes an alert, such as a beep', 'ایک الرٹ مثلاً بیپ کی آواز پیدا کرتا ہے', 'خبرتیا لکه بیپ پیدا کوي')),
     (('Backspace', 'بیک اسپیس', 'شاتګ'), '\\b', ('Moves the cursor back one space', 'کرسر کو ایک خانہ پیچھے لے جاتا ہے', 'کرسر یو ځای شاته وړي')),
     (('Formfeed', 'فارم فیڈ', 'د پاڼې بدلون'), '\\f', ('Moves the cursor to next logical page', 'کرسر کو اگلے منطقی صفحے پر لے جاتا ہے', 'کرسر راتلونکي منطقي مخ ته وړي')),
     (('Newline', 'نئی لائن', 'نوې کرښه'), '\\n', ('Moves cursor to next line', 'کرسر کو اگلی لائن پر لے جاتا ہے', 'کرسر راتلونکې کرښې ته وړي')),
     (('Carriage return', 'کیرج ریٹرن', 'د کرښې پیل ته ستنېدل'), '\\r', ('Moves cursor to beginning of line', 'کرسر کو لائن کے شروع میں لے جاتا ہے', 'کرسر د کرښې پیل ته وړي')),
     (('Horizontal tab', 'افقی ٹیب', 'افقي ټب'), '\\t', ('Prints a horizontal tab', 'افقی ٹیب پرنٹ کرتا ہے', 'افقي ټب چاپوي')),
     (('Vertical tab', 'عمودی ٹیب', 'عمودي ټب'), '\\v', ('Prints a vertical tab', 'عمودی ٹیب پرنٹ کرتا ہے', 'عمودي ټب چاپوي')),
     (('Single quote', 'سنگل کوٹ', 'یوګونی نقل‌قول'), "\\'", ('Prints a single quote', 'سنگل کوٹ پرنٹ کرتا ہے', 'یوګونی نقل‌قول چاپوي')),
     (('Double quote', 'ڈبل کوٹ', 'دوه‌ګونی نقل‌قول'), '\\"', ('Prints a double quote', 'ڈبل کوٹ پرنٹ کرتا ہے', 'دوه‌ګونی نقل‌قول چاپوي')),
     (('Backslash', 'بیک سلیش', 'شا سلیش'), '\\\\', ('Prints a backslash', 'بیک سلیش پرنٹ کرتا ہے', 'شا سلیش چاپوي')),
     (('Question mark', 'سوالیہ نشان', 'د پوښتنې نښه'), '\\?', ('Prints a question mark', 'سوالیہ نشان پرنٹ کرتا ہے', 'د پوښتنې نښه چاپوي')),
     (('Octal/hex number', 'آکٹل/ہیکس عدد', 'اتیز/شپاړسیز عدد'), '\\(number)', ('Translates into char represented by octal/hex number', 'آکٹل/ہیکس عدد سے ظاہر کردہ حرف میں تبدیل ہوتا ہے', 'د اتیز/شپاړسیز عدد له مخې ښودل شوي توري ته اړول کېږي'))]
rows = lambda i: [[n[i], s, m[i]] for n, s, m in E]
t.table('cs12-table-3-3', ['Name', 'Symbol', 'Meaning'], rows(0), ['نام', 'علامت', 'مطلب'], ['نوم', 'نښه', 'معنا'], rows(1), rows(2))
P('Table 3.3: Escape Sequences', 'جدول 3.3: ایسکیپ سیکوینسز', '۳.۳ جدول: د تېښتې لړۍ')
P('The most common escape sequence is \\n, which can be used to embed a newline in a string of text:',
  'سب سے عام ایسکیپ سیکوینس \\n ہے جو متن کی اسٹرنگ میں نئی لائن شامل کرنے کے لیے استعمال کیا جا سکتا ہے:',
  'تر ټولو عامه د تېښتې لړۍ \\n ده چې د متن په تار کې د نوې کرښې د ننویستلو لپاره کارول کېدای شي:')
rec = BOOK.record(t, 'cs12-u3-text-14', 'Unit 3 text (14)', 'یونٹ 3 — متن (۱۴)', '۳ څپرکی — متن (۱۴)', 48, [84, 85])
rec['sourceNote'] = 'Table 3.3 is reproduced as a structured table; escape symbols are identical in all language views. The example announced at the foot of p.85 follows on p.86 (PDF49).'
issues = [{'id': 'cs12-pdf048', 'unit': 3, 'printedPage': 84,
           'description': 'p.84 prints “Consider the follow ing C++ program” (split word); Table 3.3 prints the quote symbols as curly quotes (\\’ and \\”); normalised to straight quotes as used in code. Section number printed “3.3.4.”'}]

if __name__ == '__main__':
    BOOK.save(48, [(3, rec)], issues=issues)
