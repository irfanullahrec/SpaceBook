"""Computer Science XII PDF47 (spread): printed pp.82–83 — output of cin-strings program; 3.3.3 gets(), puts(), getch(); a. gets() + example; b. puts() + example."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Enter your name please
Mohammad Khalid
Your name is Mohammad Khalid''')
H('3.3.3 gets(), puts() and getch() functions', '3.3.3 gets()، puts() اور getch() فنکشنز', '۳.۳.۳ د gets()، puts() او getch() فنکشنونه')
P('C++ uses a wide range of standard Input/output functions. These functions are defined in standard library header files. The following sub-sections discuss some of the most commonly used I/O built-in functions.',
  'C++ معیاری ان پٹ/آؤٹ پٹ فنکشنز کی ایک وسیع رینج استعمال کرتی ہے۔ یہ فنکشنز معیاری لائبریری کی ہیڈر فائلوں میں متعین ہیں۔ درج ذیل ذیلی حصے سب سے زیادہ استعمال ہونے والے کچھ بلٹ ان I/O فنکشنز پر بحث کرتے ہیں۔',
  'C++ د معیاري ننوتو/وتو فنکشنونو پراخه لړۍ کاروي. دا فنکشنونه د معیاري کتابتون په سرلیک فایلونو کې تعریف شوي. لاندې فرعي برخې د تر ټولو ډېرو کارېدونکو جوړ شویو I/O فنکشنونو په اړه بحث کوي.')
H('a. gets() function', 'a. gets() فنکشن', 'a. gets() فنکشن')
P('gets() is a standard library function defined in stdio.h header file which is used to get a string from the keyboard. Its general syntax is:',
  'gets() معیاری لائبریری کا فنکشن ہے جو stdio.h ہیڈر فائل میں متعین ہے اور کی بورڈ سے اسٹرنگ حاصل کرنے کے لیے استعمال ہوتا ہے۔ اس کا عمومی طریقۂ تحریر یہ ہے:',
  'gets() د معیاري کتابتون فنکشن دی چې په stdio.h سرلیک فایل کې تعریف شوی او له کیبورډ د تار د ترلاسه کولو لپاره کارول کېږي. عمومي بڼه یې دا ده:')
code(t, 'gets(string variable name);')
P('It reads characters from stdin and stores them as a string into ‘string variable’ until a newline character or the EOF is reached. Consider the following example:',
  'یہ stdin سے حروف پڑھتا ہے اور انھیں اسٹرنگ کے طور پر ’string variable‘ میں محفوظ کرتا ہے یہاں تک کہ نئی لائن کا حرف یا EOF آ جائے۔ درج ذیل مثال پر غور کریں:',
  'دا له stdin توري لولي او د تار په توګه یې په ‘string variable’ کې ساتي تر هغه چې د نوې کرښې توری یا EOF ته ورسېږي. لاندې بېلګې ته پام وکړئ:')
code(t, '''/* gets example */
#include <stdio.h>
#include <conio.h>
#include<iostream.h>
int main()
{
char Test Str [150];
cout<<"Insert your full address: ";
gets (TestStr);
cout<<"\\nYour address is:"<<TestStr;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Insert your full address: H.No. 10 Lalazar Colony
Peshawar
Your address is: H.No. 10 Lalazar Colony
Peshawar''')
H('b. puts() function', 'b. puts() فنکشن', 'b. puts() فنکشن')
P('puts() function writes a string to the screen and appends a newline character automatically at the string. The general syntax of puts () function is:',
  'puts() فنکشن اسکرین پر اسٹرنگ لکھتا ہے اور اسٹرنگ کے آخر میں خود بخود نئی لائن کا حرف شامل کر دیتا ہے۔ puts() فنکشن کا عمومی طریقۂ تحریر یہ ہے:',
  'puts() فنکشن پر پرده تار لیکي او د تار په پای کې په اتوماتیک ډول د نوې کرښې توری ورزیاتوي. د puts() فنکشن عمومي بڼه دا ده:')
code(t, 'puts (string variable);')
P('Consider the following example to demonstrate gets() and puts() functions:', 'gets() اور puts() فنکشنز کی وضاحت کے لیے درج ذیل مثال پر غور کریں:', 'د gets() او puts() فنکشنونو د ښودلو لپاره لاندې بېلګې ته پام وکړئ:')
code(t, '''#include <stdio.h>
#include<conio.h>
#include<iostream.h>
int main()
{
char TestStr [100];
cout<< " Enter a string\\n";
gets(TestStr);
cout<< "You entered: ";
puts (TestStr);
getch();
return 0;
}''')
rec = BOOK.record(t, 'cs12-u3-text-13', 'Unit 3 text (13)', 'یونٹ 3 — متن (۱۳)', '۳ څپرکی — متن (۱۳)', 47, [82, 83])
rec['sourceNote'] = 'The gets example begins on p.82 and ends at the top of p.83; it is given whole. Sample outputs (names and addresses) are kept as printed.'
issues = [{'id': 'cs12-pdf047', 'unit': 3, 'printedPage': 82,
           'description': 'The gets example on p.82 declares “char Test Str [150];” (space inside the identifier) while later using TestStr; retained as printed. The puts example output follows on p.84 (PDF48).'}]

if __name__ == '__main__':
    BOOK.save(47, [(3, rec)], issues=issues)
