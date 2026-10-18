"""Computer Science XII PDF36 (spread): printed pp.60–61 — 3.1.3 structure of a C++ program; Hello World; a. preprocessor directives; #define example (whole listing incl. p.62 lines)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('3.1.3 Structure of a C++ program', '3.1.3 C++ پروگرام کی ساخت', '۳.۱.۳ د C++ پروګرام جوړښت')
P('General syntax of a C++ program is given below.', 'C++ پروگرام کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے۔', 'د C++ پروګرام عمومي بڼه لاندې ورکړل شوې.')
code(t, '''Preprocessor directives <header file>
int main()
{
Body of the program
}''')
P('Each C++ program has three main components. These are: Preprocessor directives, main function and body of the main function. Now, consider the following “Hello World” example to explain these components.',
  'ہر C++ پروگرام کے تین بنیادی اجزاء ہیں: پری پروسیسر ڈائریکٹوز، main فنکشن اور main فنکشن کا جسم۔ اب ان اجزاء کی وضاحت کے لیے درج ذیل ’’Hello World‘‘ مثال پر غور کریں۔',
  'هر C++ پروګرام درې اصلي برخې لري: د مخکې پروسس لارښوونې (preprocessor directives)، main فنکشن او د main فنکشن بدنه. اوس د دې برخو د تشریح لپاره لاندې "Hello World" بېلګې ته پام وکړئ.')
code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
cout << "Hello World!";
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'Hello World!')
P('The result of the above program is that it prints "Hello World!" on the screen. It is one of the simplest programs that can be written in C++, but it contains the fundamental components of almost every C++ program.',
  'اوپر والے پروگرام کا نتیجہ یہ ہے کہ یہ اسکرین پر "Hello World!" پرنٹ کرتا ہے۔ یہ C++ میں لکھے جا سکنے والے سادہ ترین پروگراموں میں سے ایک ہے لیکن اس میں تقریباً ہر C++ پروگرام کے بنیادی اجزاء موجود ہیں۔',
  'د پورته پروګرام پایله دا ده چې پر پرده "Hello World!" چاپوي. دا په C++ کې د لیکل کېدونکو تر ټولو ساده پروګرامونو څخه یو دی، خو د نږدې هر C++ پروګرام بنسټیزې برخې لري.')
H('a. Preprocessor directives (#include, #define)', 'a. پری پروسیسر ڈائریکٹوز (#include، #define)', 'a. د مخکې پروسس لارښوونې (#include، #define)')
P('A preprocessor is a collection of special statements which are executed before the compilation process.', 'پری پروسیسر خصوصی بیانات کا مجموعہ ہے جو کمپائلیشن کے عمل سے پہلے چلائے جاتے ہیں۔', 'مخکې پروسسوونکی (preprocessor) د ځانګړو بیانونو ټولګه ده چې د کمپایل له بهیر مخکې اجرا کېږي.')
P('Almost every C++ program contains a preprocessor directive. The #include preprocessor directives is commonly used to insert header files with extension ‘.h’. These header files are already stored in computer in include directory. In the above program, two #include directives have been used, #include<iostream.h> and #include<conio.h>. #include<iostream.h> is used for the C++ object cout and #include<conio.h> for the built-in function getch().',
  'تقریباً ہر C++ پروگرام میں پری پروسیسر ڈائریکٹو ہوتا ہے۔ #include پری پروسیسر ڈائریکٹو عام طور پر ‘.h’ ایکسٹینشن والی ہیڈر فائلیں شامل کرنے کے لیے استعمال ہوتا ہے۔ یہ ہیڈر فائلیں کمپیوٹر میں include ڈائریکٹری میں پہلے سے محفوظ ہوتی ہیں۔ اوپر والے پروگرام میں دو #include ڈائریکٹوز استعمال ہوئے ہیں، #include<iostream.h> اور #include<conio.h>۔ #include<iostream.h> C++ آبجیکٹ cout کے لیے اور #include<conio.h> بلٹ ان فنکشن getch() کے لیے استعمال ہوتا ہے۔',
  'نږدې هر C++ پروګرام د مخکې پروسس لارښوونه لري. د #include لارښوونه عموماً د ‘.h’ پسوند لرونکو سرلیک فایلونو د ورګډولو لپاره کارول کېږي. دا سرلیک فایلونه مخکې له مخکې په کمپیوټر کې په include لارښود کې ساتل شوي. په پورته پروګرام کې دوه #include لارښوونې کارول شوې، #include<iostream.h> او #include<conio.h>. #include<iostream.h> د C++ شي cout لپاره او #include<conio.h> د جوړ شوي فنکشن getch() لپاره کارول کېږي.')
P('In C++, the other commonly used preprocessor directive is #define which is used to define symbolic constants. Its general format is:',
  'C++ میں دوسرا عام استعمال ہونے والا پری پروسیسر ڈائریکٹو #define ہے جو علامتی کانسٹنٹس کی تعریف کے لیے استعمال ہوتا ہے۔ اس کی عمومی شکل یہ ہے:',
  'په C++ کې بله عام کارېدونکې د مخکې پروسس لارښوونه #define ده چې د سمبولیکو ثابتونو د تعریف لپاره کارول کېږي. عمومي بڼه یې دا ده:')
code(t, '#define identifier value')
P('For example:', 'مثال کے طور پر:', 'د بېلګې په توګه:')
code(t, '''#define PI 3.14159
#define NEWLINE '\\n\'''')
P('This defines two new constants: PI and NEWLINE. Once they are defined, they can be used in the rest of the program as if they were any other regular constant, for example:',
  'یہ دو نئے کانسٹنٹس PI اور NEWLINE کی تعریف کرتا ہے۔ ایک بار تعریف ہو جانے کے بعد انھیں باقی پروگرام میں کسی بھی دوسرے عام کانسٹنٹ کی طرح استعمال کیا جا سکتا ہے، مثلاً:',
  'دا دوه نوي ثابتونه PI او NEWLINE تعریفوي. کله چې یو ځل تعریف شي، په پاتې پروګرام کې د هر بل عادي ثابت په څېر کارول کېدای شي، لکه:')
code(t, '''#include <iostream.h>
#include <conio.h>
#define PI 3.14159
#define NEWLINE '\\n'
int main()
{
double r=5.0; // radius
double circle;
circle = 2 * PI * r;
cout << "Area of the Circle: "<<circle;
cout << NEWLINE;
getch();
return 0;
}''')
rec = BOOK.record(t, 'cs12-u3-text-2', 'Unit 3 text (2)', 'یونٹ 3 — متن (۲)', '۳ څپرکی — متن (۲)', 36, [60, 61, 62])
rec['sourceNote'] = 'The last listing begins at the foot of p.61 and continues on p.62 (PDF37); it is given whole here. Its output and the following text are recorded with PDF37.'
issues = [{'id': 'cs12-pdf036', 'unit': 3, 'printedPage': 61,
           'description': 'p.61 prints “The #include preprocessor directives is commonly used”. In the example on p.62 the program labels 2·π·r as “Area of the Circle” (it is the circumference) — retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(36, [(3, rec)], issues=issues)
