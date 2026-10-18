"""Computer Science XII PDF73–74: pp.134–135 do-while explanation, echo program; 4.2.2 continue; 4.2.3 nested loops; nested while (whole incl. p.136);
pp.136–137 nested for loop.
Run: python class12_cs_page073.py N (73 or 74)."""
import sys
from class12_cs_common import BOOK, Builder, code


def p73():
    t = Builder()
    P = t.p
    P('In the above program, the loop control variable ‘i’ is initially set to 10 and in the condition it is restricted to be less than 6 (which is violated in the start) but still it is executed once and have displayed the message PAKISTAN.',
      'اوپر والے پروگرام میں لوپ کنٹرول ویری ایبل ‘i’ کو شروع میں 10 مقرر کیا گیا ہے اور شرط میں اسے 6 سے کم ہونے کا پابند کیا گیا ہے (جو شروع ہی میں پوری نہیں ہوتی) لیکن پھر بھی لوپ ایک بار چلتا ہے اور پیغام PAKISTAN دکھاتا ہے۔',
      'په پورته پروګرام کې د حلقې کنټرول متغیر ‘i’ په پیل کې 10 ټاکل شوی او په شرط کې دا محدود شوی چې له 6 کوچنی وي (چې په پیل کې نه پوره کېږي)، خو بیا هم حلقه یو ځل اجرا کېږي او د PAKISTAN پیغام ښيي.')
    P('Consider another program that echoes any number you enter from the keyboard to the screen until you enter 0 using do-while loop.',
      'ایک اور پروگرام پر غور کریں جو do-while لوپ کے ذریعے کی بورڈ سے داخل کیا گیا ہر عدد اسکرین پر دکھاتا ہے یہاں تک کہ آپ 0 داخل کریں۔',
      'بل پروګرام ته پام وکړئ چې د do-while حلقې په مرسته هر هغه عدد چې له کیبورډ لیکئ پر پرده ښيي تر هغه چې 0 ولیکئ.')
    code(t, '''#include <conio.h>
#include <iostream.h>
int main()
{
int x;
do {
cout << "Enter number (0 is for ending): ";
cin >> x;
cout << "You entered: " << x << "\\n";
} while (x != 0);
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter number (0 is for ending): 12
You entered: 12
Enter number (0 is for ending): 16
You entered: 16
Enter number (0 is for ending): 0
You entered: 0''')
    t.h('4.2.2 continue statement', '4.2.2 continue بیان', '۴.۲.۲ continue بیان')
    P('The continue statement provides a convenient way to jump to the start of a next iteration by passing the remaining part of the loop for an iteration. For example, we are going to skip the number 5 in our countdown:',
      'continue بیان کسی تکرار میں لوپ کا باقی حصہ چھوڑ کر اگلی تکرار کے آغاز پر جانے کا آسان طریقہ فراہم کرتا ہے۔ مثال کے طور پر ہم اپنی الٹی گنتی میں عدد 5 کو چھوڑنے جا رہے ہیں:',
      'continue بیان د یوه تکرار لپاره د حلقې پاتې برخه پرېښودو سره د راتلونکي تکرار پیل ته د ټوپ اسانه لاره برابروي. د بېلګې په توګه موږ په خپله شاتنۍ شمېرنه کې 5 عدد پرېږدو:')
    code(t, '''// use of continue statement in loop
#include <iostream.h>
#include <conio.h>
int main()
{
for (int n=10; n>0; n--)
{
if (n==5) continue;
cout << n << ", ";
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '10, 9, 8, 7, 6, 4, 3, 2, 1')
    t.h('4.2.3 Nested loops', '4.2.3 نیسٹڈ لوپس', '۴.۲.۳ ځالې حلقې')
    P('The use of a loop inside the body of another loop is called nested loop. The enclosing loop is called outer loop and the enclosed loop is called inner loop. The following example demonstrates the concept of nested loop.',
      'ایک لوپ کے جسم کے اندر دوسرے لوپ کا استعمال نیسٹڈ لوپ کہلاتا ہے۔ گھیرنے والے لوپ کو بیرونی لوپ اور اندر والے لوپ کو اندرونی لوپ کہتے ہیں۔ درج ذیل مثال نیسٹڈ لوپ کا تصور واضح کرتی ہے۔',
      'د یوې حلقې د بدنې دننه د بلې حلقې کارونه ځالې حلقه بلل کېږي. راګېروونکې حلقه بهرنۍ حلقه او دننه حلقه دننۍ حلقه بلل کېږي. لاندې بېلګه د ځالې حلقې مفهوم ښيي.')
    code(t, '''// nested while loop program
#include <iostream.h>
#include <conio.h>
int main()
{
// Outer Loop between 1 and 5
int O=1;
while (O<=5)
{
int I = 1;
while (I <= O)
{
cout << I++;
}// end of inner loop
// print a newline at the end of each row
cout << endl;
O++;
}// end of outer loop
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''1
1 2
1 2 3
1 2 3 4
1 2 3 4 5''')
    rec = BOOK.record(t, 'cs12-u4-text-13', 'Unit 4 text (13)', 'یونٹ 4 — متن (۱۳)', '۴ څپرکی — متن (۱۳)', 73, [134, 135, 136])
    rec['sourceNote'] = 'The nested while program starts at the foot of p.135 and continues on p.136 (PDF74); it is given whole here with its output.'
    BOOK.save(73, [(4, rec)], issues=[{'id': 'cs12-pdf073', 'unit': 4, 'printedPage': 134,
               'description': 'p.134 “it is executed once and have displayed”; the nested-while output shows digits separated by spaces although the program prints none (cout << I++). Retained as printed. Owner scribbles on p.135 excluded.'}])


def p74():
    t = Builder()
    P = t.p
    P('Consider another example:', 'ایک اور مثال پر غور کریں:', 'بلې بېلګې ته پام وکړئ:')
    code(t, '''// nested for loop
#include <iostream.h>
#include <conio.h>
int main()
{
for (int i=1; i<=5; i++) //outer loop
{
for (int j=1; j<=i; j++) //inner loop
cout << "$";
cout << endl;
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''$
$$
$$$
$$$$
$$$$$''')
    rec = BOOK.record(t, 'cs12-u4-text-14', 'Unit 4 text (14)', 'یونٹ 4 — متن (۱۴)', '۴ څپرکی — متن (۱۴)', 74, [136, 137])
    rec['sourceNote'] = 'The top of p.136 (end of the nested while program and its output) is recorded with PDF73.'
    BOOK.save(74, [(4, rec)])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 73
    p73() if n == 73 else p74()
