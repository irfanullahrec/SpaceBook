"""Computer Science XII PDF49 (spread): printed pp.86–87 — \\n and \\t programs; 3.3.5 I/O handling functions: getchar(), putchar(); getchar/putchar example (whole, incl. p.88 lines)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
code(t, '''// \\n escape sequence program
#include <iostream.h>
#include<conio.h>
int main()
{
cout<< "Welcome to \\nthe College " <<endl;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Welcome to
the College''')
P('Consider another program for escape sequence character “\\t”.', 'ایسکیپ سیکوینس حرف ’’\\t‘‘ کے لیے ایک اور پروگرام پر غور کریں۔', 'د تېښتې لړۍ توري "\\t" لپاره بل پروګرام ته پام وکړئ.')
code(t, '''// escape sequence \\t program
#include <iostream.h>
#include<conio.h>
int main()
{
cout<< "First part\\tSecond part";
getch();
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'First part      Second part')
H('3.3.5 I/O handling functions', '3.3.5 ان پٹ/آؤٹ پٹ کے فنکشنز', '۳.۳.۵ د ننوتو/وتو فنکشنونه')
P('Most commonly used', 'سب سے زیادہ استعمال ہونے والے', 'تر ټولو ډېر کارېدونکي')
t.group('list', [('getchar() stands for get character and is used to get a single character from standard input device (keyboard). getchar() is defined in stdio.h header file. The general syntax for the use of getchar () function is:',
                  'getchar() کا مطلب ’’گیٹ کریکٹر‘‘ ہے اور یہ معیاری ان پٹ آلے (کی بورڈ) سے ایک حرف حاصل کرنے کے لیے استعمال ہوتا ہے۔ getchar() stdio.h ہیڈر فائل میں متعین ہے۔ getchar() فنکشن کے استعمال کا عمومی طریقۂ تحریر یہ ہے:',
                  'getchar() د "توری ترلاسه کول" معنا لري او له معیاري ننوتو وسیلې (کیبورډ) یو توری ترلاسه کولو ته کارېږي. getchar() په stdio.h سرلیک فایل کې تعریف شوی. د getchar() فنکشن د کارونې عمومي بڼه دا ده:')])
code(t, 'int getchar ();')
P('This function gets no parameters.', 'یہ فنکشن کوئی پیرامیٹر نہیں لیتا۔', 'دا فنکشن هېڅ پارامېټر نه اخلي.')
t.group('list', [('putchar() is a standard output function defined in stdio.h header file and is used to display a single character, received as an argument, on the screen. Its general syntax is:',
                  'putchar() معیاری آؤٹ پٹ فنکشن ہے جو stdio.h ہیڈر فائل میں متعین ہے اور آرگیومنٹ کے طور پر ملنے والے ایک حرف کو اسکرین پر دکھانے کے لیے استعمال ہوتا ہے۔ اس کا عمومی طریقۂ تحریر یہ ہے:',
                  'putchar() یو معیاري وتنې فنکشن دی چې په stdio.h سرلیک فایل کې تعریف شوی او د دلیل په توګه ترلاسه شوی یو توری پر پرده ښودلو ته کارېږي. عمومي بڼه یې دا ده:')])
code(t, 'putchar (ch); // where ch is a char type variable holding a character constant')
P('This putchar() display the character constant stored in ‘ch’ on the screen. Consider the following example:',
  'یہ putchar() ‘ch’ میں محفوظ حرفی کانسٹنٹ کو اسکرین پر دکھاتا ہے۔ درج ذیل مثال پر غور کریں:',
  'دا putchar() په ‘ch’ کې ساتل شوی د توري ثابت پر پرده ښيي. لاندې بېلګې ته پام وکړئ:')
code(t, '''// getchar() and putchar() example
#include <conio.h>
#include <stdio.h>
#include<iostream.h>
int main()
{
char ch;
cout<<"Enter character for gender\\n";
ch=getchar();
cout<< "You have entered: ";
putchar (ch);
getch();
return 0;
}''')
rec = BOOK.record(t, 'cs12-u3-text-15', 'Unit 3 text (15)', 'یونٹ 3 — متن (۱۵)', '۳ څپرکی — متن (۱۵)', 49, [86, 87, 88])
rec['sourceNote'] = 'The \\n program is the example announced at the foot of p.85. The getchar()/putchar() listing continues on p.88 (PDF50) and is given whole here. The \\t output shows a tab gap between the two words.'
issues = [{'id': 'cs12-pdf049', 'unit': 3, 'printedPage': 87,
           'description': 'p.87 prints “This putchar() display the character”; the putchar syntax comment “where ch is a char type variable holding a character constant” is part of the printed line. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(49, [(3, rec)], issues=issues)
