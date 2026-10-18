"""Computer Science XII PDF50 (spread): printed pp.88–89 — getchar output; 3.3.6 manipulators; a. endl (+ program); b. setw (+ program, whole incl. p.90 lines and output)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Enter character for gender
M
You have entered: M''')
P('This program reads a character from the keyboard using getchar() function and assign it to a character type variable ‘ch’ which is displayed on the screen by another standard library function putchar().',
  'یہ پروگرام getchar() فنکشن کے ذریعے کی بورڈ سے ایک حرف پڑھتا ہے اور اسے حرفی قسم کے ویری ایبل ‘ch’ کو تفویض کرتا ہے جسے ایک اور معیاری لائبریری فنکشن putchar() اسکرین پر دکھاتا ہے۔',
  'دا پروګرام د getchar() فنکشن په مرسته له کیبورډ یو توری لولي او د توري ډول متغیر ‘ch’ ته یې سپاري، چې بیا یې بل معیاري کتابتون فنکشن putchar() پر پرده ښيي.')
H('3.3.6 endl and setw Manipulator', '3.3.6 endl اور setw مینیپولیٹر', '۳.۳.۶ د endl او setw بدلوونکي')
P('Manipulators are used for formatting output. The data is manipulated by the programmer’s choice of display. There are several manipulators available in C++. The most commonly used manipulators are discussed below:',
  'مینیپولیٹرز آؤٹ پٹ کی فارمیٹنگ کے لیے استعمال ہوتے ہیں۔ ڈیٹا کو پروگرامر کی پسند کے مطابق دکھانے کے لیے ترتیب دیا جاتا ہے۔ C++ میں کئی مینیپولیٹرز دستیاب ہیں۔ سب سے زیادہ استعمال ہونے والے مینیپولیٹرز پر ذیل میں بحث کی گئی ہے:',
  'بدلوونکي (manipulators) د وتنې د بڼې ورکولو لپاره کارول کېږي. ډېټا د پروګرام جوړوونکي د خوښې سره سم د ښودلو لپاره بدلېږي. په C++ کې څو بدلوونکي شته. تر ټولو ډېر کارېدونکي یې لاندې بحث شوي:')
H('a. endl manipulator', 'a. endl مینیپولیٹر', 'a. endl بدلوونکی')
P('This manipulator has the same functionality as the ‘\\n’ newline character but with the difference of flushing the stream. Consider the following example:',
  'اس مینیپولیٹر کا کام نئی لائن کے حرف ‘\\n’ جیسا ہی ہے لیکن فرق یہ ہے کہ یہ اسٹریم کو خالی (flush) بھی کرتا ہے۔ درج ذیل مثال پر غور کریں:',
  'دا بدلوونکی د ‘\\n’ نوې کرښې توري په څېر دنده لري، خو توپیر یې دا دی چې بهیر هم تشوي (flush). لاندې بېلګې ته پام وکړئ:')
code(t, '''// endl manipulator program
#include <iostream.h>
#include <conio.h>
int main()
{
cout << "Welcome" << endl;
cout << "to" << endl;
cout << "the College";
getch();
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Welcome
to
the College''')
H('b. setw manipulator', 'b. setw مینیپولیٹر', 'b. setw بدلوونکی')
P('This manipulator sets the minimum field width on output. The syntax is:', 'یہ مینیپولیٹر آؤٹ پٹ پر کم از کم فیلڈ کی چوڑائی مقرر کرتا ہے۔ اس کا طریقۂ تحریر یہ ہے:', 'دا بدلوونکی په وتنه کې د ساحې لږ تر لږه پلنوالی ټاکي. بڼه یې دا ده:')
code(t, 'setw(x)')
P('Here, setw causes the number or string that follows it to be printed within a field of x characters wide and x is the argument set in setw manipulator. The header file that must be included while using setw manipulator is <iomanip.h>. Consider the following example:',
  'یہاں setw اپنے بعد آنے والے عدد یا اسٹرنگ کو x حروف چوڑے فیلڈ میں پرنٹ کرواتا ہے اور x وہ آرگیومنٹ ہے جو setw مینیپولیٹر میں دیا جاتا ہے۔ setw مینیپولیٹر استعمال کرتے وقت جو ہیڈر فائل شامل کرنا ضروری ہے وہ <iomanip.h> ہے۔ درج ذیل مثال پر غور کریں:',
  'دلته setw هغه عدد یا تار چې ورپسې راځي، د x توري پلنې ساحې دننه چاپوي او x هغه دلیل دی چې په setw بدلوونکي کې ټاکل کېږي. هغه سرلیک فایل چې د setw د کارولو پر وخت باید شامل شي <iomanip.h> دی. لاندې بېلګې ته پام وکړئ:')
code(t, '''//setw manipulator program
#include <iostream.h>
#include <iomanip.h>
#include<conio.h>
int main( )
{
int x1=2,x2= 4, x3=6;
cout<<setw(8)<<"Number"<<setw(20)<<"Square"<<endl
<< setw(8) << "2" << setw(20)<< x1*x1 << endl
<< setw(8) << "4" << setw(20)<< x2*x2 << endl
<< setw(8) << "6" << setw(20)<< x3*x3 << endl;
getch();
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''  Number              Square
       2                   4
       4                  16
       6                  36''')
rec = BOOK.record(t, 'cs12-u3-text-16', 'Unit 3 text (16)', 'یونٹ 3 — متن (۱۶)', '۳ څپرکی — متن (۱۶)', 50, [88, 89, 90])
rec['sourceNote'] = 'The first lines of p.88 complete the getchar()/putchar() listing recorded with PDF49. The setw listing continues on p.90 (PDF51) and is given whole with its output; the output columns are shown right-aligned as setw produces them (the scan shows them loosely aligned).'
issues = [{'id': 'cs12-pdf050', 'unit': 3, 'printedPage': 89,
           'description': 'The setw listing prints the quoted digits with curly quotes (“2”, “4”, “6”); normalised to straight quotes. p.88 “read a character … and assign it”. Retained otherwise.'}]

if __name__ == '__main__':
    BOOK.save(50, [(3, rec)], issues=issues)
