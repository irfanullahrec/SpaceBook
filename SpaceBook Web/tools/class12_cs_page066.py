"""Computer Science XII PDF66–67: pp.120–121 nested if-else programs (multiple of 2/3; grades, whole incl. p.122 + output);
pp.122–123 4.1.3 break and exit(); exit() example; 4.2 LOOPS (begins).
Run: python class12_cs_page066.py N (66 or 67)."""
import sys
from class12_cs_common import BOOK, Builder, code


def p66():
    t = Builder()
    P = t.p
    P('Consider another program demonstrating nested if-else structure by displaying whether an entered integer is multiple of 2 or 3 or is some other number.',
      'ایک اور پروگرام پر غور کریں جو نیسٹڈ if-else ساخت کو یہ دکھا کر واضح کرتا ہے کہ داخل کیا گیا صحیح عدد 2 یا 3 کا مضرب ہے یا کوئی اور عدد ہے۔',
      'بل پروګرام ته پام وکړئ چې ځالې if-else جوړښت په دې ښودلو روښانه کوي چې لیکل شوی صحیح عدد د 2 یا 3 مضرب دی که بل عدد.')
    code(t, '''#include <iostream.h>
#include<conio.h>
int main()
{
int n;
cout<<"Enter a number: ";
cin>>n;
if (n%2== 0)
cout << n<< " is multiple of 2";
else
if (n %3== 0)
cout << n<< " is multiple of 3";
else
cout << n<< " is neither multiple of 2 nor 3";
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter a number:
55
55 is neither multiple of 2 nor 3''')
    P('Consider another example demonstrating nested if-else structure to display the grades of students. This program takes percentage marks as input and then using relational and logical operators find its corresponding grade.',
      'ایک اور مثال پر غور کریں جو طلبہ کے گریڈ دکھانے کے لیے نیسٹڈ if-else ساخت کی وضاحت کرتی ہے۔ یہ پروگرام فیصد نمبر ان پٹ کے طور پر لیتا ہے اور پھر ریلیشنل اور منطقی آپریٹرز کے ذریعے متعلقہ گریڈ معلوم کرتا ہے۔',
      'بله بېلګه وګورئ چې د زده‌کوونکو د درجو د ښودلو لپاره ځالې if-else جوړښت ښيي. دا پروګرام سلنیزې نمرې د ننوتنې په توګه اخلي او بیا د اړیکه‌ییزو او منطقي چلونکو په مرسته اړونده درجه پیدا کوي.')
    code(t, '''#include <iostream.h>
#include<conio.h>
int main()
{
float per;
cout<<"Enter percentage marks: "<<endl;
cin>>per;
if (per >= 80)
{
cout << "Your grade is A+"<<endl;
cout<< "Excellent";
} else
{
if (per < 80 && per>=70)
{
cout << "Your grade is A"<<endl;
cout<< "Very good";
} else
{
if(per<70 && per>=60)
{
cout << "Your grade is B"<<endl;
cout<< "Good";
}else
cout<<"You are failed, try again";
}
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter percentage marks:
65.09
Your grade is B
Good''')
    rec = BOOK.record(t, 'cs12-u4-text-6', 'Unit 4 text (6)', 'یونٹ 4 — متن (۶)', '۴ څپرکی — متن (۶)', 66, [120, 121, 122])
    rec['sourceNote'] = 'The grades program continues on p.122 (PDF67) and is given whole here with its output.'
    BOOK.save(66, [(4, rec)], issues=[{'id': 'cs12-pdf066', 'unit': 4, 'printedPage': 121,
               'description': 'The grades listing prints some cout strings with curly quotes; normalised. The program prints “You are failed, try again” for any percentage below 60 — retained.'}])


def p67():
    t = Builder()
    P = t.p
    t.h('4.1.3 break statement and exit() function', '4.1.3 break بیان اور exit() فنکشن', '۴.۱.۳ break بیان او exit() فنکشن')
    P('Sometimes a programmer needs to make use of such statements in a program that are responsible for the jump from one statement of the program to another statement. The most commonly used jump statements of C++ language are: goto, break, and continue. Similarly, the execution of a running program is also sometime needed to be halt and to jump out of a program. A function used to accomplish this is exit(). The following sections discuss the use of break statement and exit () function with the help of examples.',
      'بعض اوقات پروگرامر کو پروگرام میں ایسے بیانات استعمال کرنے پڑتے ہیں جو پروگرام کے ایک بیان سے دوسرے بیان پر چھلانگ کے ذمہ دار ہوں۔ C++ زبان کے سب سے زیادہ استعمال ہونے والے جمپ بیانات goto، break اور continue ہیں۔ اسی طرح بعض اوقات چلتے ہوئے پروگرام کو روکنے اور پروگرام سے باہر نکلنے کی بھی ضرورت ہوتی ہے۔ اس کام کے لیے استعمال ہونے والا فنکشن exit() ہے۔ درج ذیل حصے مثالوں کی مدد سے break بیان اور exit() فنکشن کے استعمال پر بحث کرتے ہیں۔',
      'کله کله پروګرام جوړوونکی اړتیا لري چې په پروګرام کې داسې بیانونه وکاروي چې د پروګرام له یوه بیان څخه بل ته د ټوپ مسؤول وي. د C++ ژبې تر ټولو ډېر کارېدونکي د ټوپ بیانونه goto، break او continue دي. همداراز کله کله د روان پروګرام د اجرا درول او له پروګرام وتل هم اړین وي. د دې کار لپاره کارېدونکی فنکشن exit() دی. لاندې برخې د بېلګو په مرسته د break بیان او exit() فنکشن کارونه بحث کوي.')
    t.h('a. break statement', 'a. break بیان', 'a. break بیان')
    P('break statement is used to make jump from one part of a program to another. In C++, break statement is used in two situations: one in switch-default structure to properly end a case clause and another in loops structure to leave a loop. The use of break in switch-default structure has already been discussed in Section 4.1.3. Its use in loops will be discussed in Section 4.2 with the help of examples.',
      'break بیان پروگرام کے ایک حصے سے دوسرے حصے میں چھلانگ لگانے کے لیے استعمال ہوتا ہے۔ C++ میں break بیان دو حالتوں میں استعمال ہوتا ہے: ایک switch-default ساخت میں case شق کو درست طریقے سے ختم کرنے کے لیے اور دوسرا لوپس کی ساخت میں لوپ سے نکلنے کے لیے۔ switch-default ساخت میں break کے استعمال پر حصہ 4.1.3 میں بحث ہو چکی ہے۔ لوپس میں اس کے استعمال پر حصہ 4.2 میں مثالوں کی مدد سے بحث ہوگی۔',
      'break بیان د پروګرام له یوې برخې بلې ته د ټوپ لپاره کارول کېږي. په C++ کې break بیان په دوو حالتونو کې کارول کېږي: یو په switch-default جوړښت کې د case برخې د سم پای ته رسولو لپاره، او بل د حلقو په جوړښت کې د حلقې د پرېښودلو لپاره. په switch-default جوړښت کې د break کارونه په ۴.۱.۳ برخه کې بحث شوې. په حلقو کې یې کارونه به په ۴.۲ برخه کې د بېلګو په مرسته بحث شي.')
    t.h('b. exit () function', 'b. exit () فنکشن', 'b. exit () فنکشن')
    P('This function tells the program to quit running immediately. This function is responsible for the immediate termination of a C++ program. It is defined in the stdlib header file. The exit function takes an integer, usually 0, as a parameter that is returned to the operating system as an exit code and tells it that the program has terminated normally.',
      'یہ فنکشن پروگرام کو فوراً چلنا بند کرنے کا کہتا ہے۔ یہ فنکشن C++ پروگرام کے فوری خاتمے کا ذمہ دار ہے۔ یہ stdlib ہیڈر فائل میں متعین ہے۔ exit فنکشن ایک صحیح عدد، عموماً 0، بطور پیرامیٹر لیتا ہے جو ایگزٹ کوڈ کے طور پر آپریٹنگ سسٹم کو واپس کیا جاتا ہے اور اسے بتاتا ہے کہ پروگرام معمول کے مطابق ختم ہوا۔',
      'دا فنکشن پروګرام ته وايي چې سمدستي چلېدل ودروي. دا فنکشن د C++ پروګرام د سمدستي پای ته رسولو مسؤول دی. په stdlib سرلیک فایل کې تعریف شوی. د exit فنکشن یو صحیح عدد، عموماً 0، د پارامېټر په توګه اخلي چې د وتو کوډ په توګه عملیاتي سیسټم ته بېرته ورکول کېږي او ورته وايي چې پروګرام په عادي ډول پای ته رسېدلی.')
    P('Consider the following example for demonstrating the use of exit () function.', 'exit() فنکشن کے استعمال کی وضاحت کے لیے درج ذیل مثال پر غور کریں۔', 'د exit() فنکشن د کارونې د ښودلو لپاره لاندې بېلګې ته پام وکړئ.')
    code(t, '''#include<conio.h>
#include <stdlib.h>
#include <iostream.h>
int main()
{
cout << "Statement before exit() function";
exit(0);
//terminate and return 0 to the operating system
// The following statements never execute
cout << "Statement after exit() function";
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, 'Statement before exit() function')
    t.h('4.2 LOOPS', '4.2 لوپس', '۴.۲ حلقې (LOOPS)')
    P('Loops are used to repeat a statement or group of statements a certain number of times until the condition is true. These are also called repetitive or iterative statements.',
      'لوپس کسی بیان یا بیانات کے گروپ کو شرط درست رہنے تک ایک مخصوص تعداد میں دہرانے کے لیے استعمال ہوتے ہیں۔ انھیں تکراری بیانات بھی کہتے ہیں۔',
      'حلقې د یوه بیان یا د بیانونو د ډلې د یو ټاکلي شمېر تکرار لپاره تر هغه کارول کېږي چې شرط true وي. تکراري بیانونه هم بلل کېږي.')
    rec = BOOK.record(t, 'cs12-u4-text-7', 'Unit 4 text (7)', 'یونٹ 4 — متن (۷)', '۴ څپرکی — متن (۷)', 67, [122, 123])
    rec['sourceNote'] = 'The top of p.122 (end of the grades program and its output) is recorded with PDF66.'
    BOOK.save(67, [(4, rec)], issues=[{'id': 'cs12-pdf067', 'unit': 4, 'printedPage': 122,
               'description': 'p.122 says break in switch was discussed in “Section 4.1.3” (it is in 4.1.1 c) and prints “sometime needed to be halt”; the exit() listing prints the cout strings with curly quotes. Retained as printed (quotes normalised).'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 66
    p66() if n == 66 else p67()
