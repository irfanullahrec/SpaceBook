"""Computer Science XII PDF62–63: pp.112–113 b. if-else statement (syntax); pp.114–115 Flowchart 4.2, if-else programs.
Run: python class12_cs_page062.py N (62 or 63)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_4_2


def p62():
    t = Builder()
    P = t.p
    t.h('b. if-else statement', 'b. if-else بیان', 'b. if-else بیان')
    P('In if construct, the statements in the body of if are executed only if the condition is true and nothing is executed if it is false. Sometimes the programmers need to execute some other part of a program even if the condition in if statement is false. For this purpose, if-else statement is used.',
      'if ساخت میں if کے جسم کے بیانات صرف اسی وقت چلتے ہیں جب شرط درست ہو، اور غلط ہونے پر کچھ نہیں چلتا۔ بعض اوقات پروگرامرز کو if بیان کی شرط غلط ہونے پر بھی پروگرام کا کوئی اور حصہ چلانا ہوتا ہے۔ اس مقصد کے لیے if-else بیان استعمال ہوتا ہے۔',
      'په if جوړښت کې د if د بدنې بیانونه یوازې هغه وخت اجرا کېږي چې شرط true وي، او که false وي هېڅ نه اجرا کېږي. کله کله پروګرام جوړوونکي اړتیا لري چې د if بیان شرط false هم وي، د پروګرام بله برخه اجرا کړي. د دې موخې لپاره if-else بیان کارول کېږي.')
    P('The general syntax of this statement is given below.', 'اس بیان کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے۔', 'د دې بیان عمومي بڼه لاندې ورکړل شوې.')
    P('Single statement if-else structure', 'ایک بیان والی if-else ساخت', 'یو-بیانیز if-else جوړښت')
    code(t, '''if (condition)
Statement;
else
Statement;''')
    P('Multiple statements if-else structure', 'متعدد بیانات والی if-else ساخت', 'څو-بیانیز if-else جوړښت')
    code(t, '''if (condition)
{
Statement 1;
Statement 2;
.
.
Statement n;
}
else
{
Statement 1;
Statement 2;
.
.
Statement n;
}''')
    P('If the condition is true, the body of if is executed. If the condition is false, the body of else is executed. Flowchart 4.2 shows working of if-else Structure.',
      'اگر شرط درست ہو تو if کا جسم چلتا ہے۔ اگر شرط غلط ہو تو else کا جسم چلتا ہے۔ فلو چارٹ 4.2 if-else ساخت کا عمل دکھاتا ہے۔',
      'که شرط true وي، د if بدنه اجرا کېږي. که شرط false وي، د else بدنه اجرا کېږي. ۴.۲ فلوچارټ د if-else جوړښت کار ښيي.')
    rec = BOOK.record(t, 'cs12-u4-text-2', 'Unit 4 text (2)', 'یونٹ 4 — متن (۲)', '۴ څپرکی — متن (۲)', 62, [112, 113])
    rec['sourceNote'] = 'The top of p.112 (rest of the if program and its output) is recorded with PDF61.'
    BOOK.save(62, [(4, rec)])


def p63():
    t = Builder()
    P = t.p
    en, ur, ps, ratio = fig_4_2()
    t.visual('cs12-fig-4-2', en, ur, ps, ratio)
    P('Consider the following program to demonstrate the use of if-else statement.', 'if-else بیان کے استعمال کی وضاحت کے لیے درج ذیل پروگرام پر غور کریں۔', 'د if-else بیان د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''//if-else (even/odd) program
#include <iostream.h>
#include<conio.h>
int main()
{
int X;
cout << "Enter a number: ";
cin >> X;
if (X %2==0)
cout << X << "is even number";
else
cout << X << " is odd number";
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter a number:
9
9 is odd number''')
    P('In order to execute multiple statements, a block should be used. Consider the following program:', 'متعدد بیانات چلانے کے لیے بلاک استعمال کرنا چاہیے۔ درج ذیل پروگرام پر غور کریں:', 'د ډېرو بیانونو د اجرا لپاره باید بلاک وکارول شي. لاندې پروګرام ته پام وکړئ:')
    code(t, '''//if-else (multiple statements) program
#include <iostream.h>
#include<conio.h>
int main()
{
int X;
cout << "Enter a number: ";
cin >> X;
if (X%2==0)
{
cout << "You have entered " << X << endl;
cout << X << "is an even number" << endl;
}
else
{
cout << "You have entered " << X << endl;
cout << X << " is an odd number" << endl;
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter a number:
08
You have entered 08
08 is an even number''')
    rec = BOOK.record(t, 'cs12-u4-text-3', 'Unit 4 text (3)', 'یونٹ 4 — متن (۳)', '۴ څپرکی — متن (۳)', 63, [114, 115])
    rec['sourceNote'] = 'Flowchart 4.2 is reproduced as a coded diagram.'
    BOOK.save(63, [(4, rec)], issues=[{'id': 'cs12-pdf063', 'unit': 4, 'printedPage': 115,
               'description': 'The output on p.115 shows the input echoed as “08” (an int prints as 8); the even branch string lacks a leading space (“is an even number”). Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 62
    p62() if n == 62 else p63()
