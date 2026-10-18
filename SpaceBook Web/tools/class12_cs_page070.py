"""Computer Science XII PDF70–71: pp.128–129 while syntax (from p.127), Flowchart 4.5, while PAKISTAN program; countdown (whole incl. p.130 + output);
pp.130–131 1-to-50 program (whole incl. p.131 + output); sentence-count program (begins; whole with PDF72).
Run: python class12_cs_page070.py N (70 or 71)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_4_5


def p70():
    t = Builder()
    P = t.p
    code(t, '''while (condition)
{
Statement 1;
Statement 2;
.
.
Statement n;
}''')
    P('Flowchart 4.5 shows working of while loop.', 'فلو چارٹ 4.5 while لوپ کا عمل دکھاتا ہے۔', '۴.۵ فلوچارټ د while حلقې کار ښيي.')
    en, ur, ps, ratio = fig_4_5()
    t.visual('cs12-fig-4-5', en, ur, ps, ratio)
    P('Consider the following program to display the string PAKISTAN five times on the screen using while loop.', 'while لوپ کے ذریعے اسکرین پر اسٹرنگ PAKISTAN پانچ بار دکھانے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د while حلقې په مرسته پر پرده د PAKISTAN تار پنځه ځله ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''// displaying PAKISTAN 5 times using while loop
#include <iostream.h>
#include<conio.h>
int main()
{
int i=1;
while (i<6)
{
cout << "PAKISTAN"<<endl;
++i;
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''PAKISTAN
PAKISTAN
PAKISTAN
PAKISTAN
PAKISTAN''')
    P('Like for loop, the while loop has also three parts: initialization, condition and increment/decrement. The difference is that here the initialization is done before the while clause and the increment/decrement is done within the body of the while loop.',
      'for لوپ کی طرح while لوپ کے بھی تین حصے ہیں: ابتدائی قدر، شرط اور اضافہ/کمی۔ فرق یہ ہے کہ یہاں ابتدائی قدر while شق سے پہلے دی جاتی ہے اور اضافہ/کمی while لوپ کے جسم کے اندر کی جاتی ہے۔',
      'د for حلقې په څېر while حلقه هم درې برخې لري: لومړنی ارزښت، شرط او زیاتول/کمول. توپیر دا دی چې دلته لومړنی ارزښت د while برخې مخکې ورکول کېږي او زیاتول/کمول د while حلقې د بدنې دننه کېږي.')
    P('The second example of countdown using while-loop is given below.', 'while لوپ کے ذریعے الٹی گنتی کی دوسری مثال ذیل میں دی گئی ہے۔', 'د while حلقې په مرسته د شاتنۍ شمېرنې دویمه بېلګه لاندې ورکړل شوې.')
    code(t, '''// count down program using while loop
#include <iostream.h>
#include <conio.h>
int main()
{
int n;
cout << "Enter the starting number: ";
cin >> n;
while (n>0)
{
cout << n << ", ";
--n;
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter the starting number:
8
8, 7, 6, 5, 4, 3, 2, 1''')
    rec = BOOK.record(t, 'cs12-u4-text-10', 'Unit 4 text (10)', 'یونٹ 4 — متن (۱۰)', '۴ څپرکی — متن (۱۰)', 70, [127, 128, 129, 130])
    rec['sourceNote'] = 'The while syntax begins at the foot of p.127; the PAKISTAN program ends at the top of p.129; the countdown program continues on p.130 (PDF71); each is given whole. Flowchart 4.5 is reproduced as a coded diagram.'
    BOOK.save(70, [(4, rec)])


def p71():
    t = Builder()
    P = t.p
    P('Here, when the program starts the user enters a number to start the countdown. In this case, the number is 8 and thus the condition n>0 is true, therefore, the block within the braces { } is executed as long as n>0 and the output 8,7,6,5,4,3,2,1 is displayed on the screen.',
      'یہاں پروگرام شروع ہونے پر صارف الٹی گنتی شروع کرنے کے لیے ایک عدد داخل کرتا ہے۔ اس صورت میں عدد 8 ہے، اس لیے شرط n>0 درست ہے اور بریسز { } کے اندر کا بلاک اس وقت تک چلتا ہے جب تک n>0 ہو، اور اسکرین پر آؤٹ پٹ 8,7,6,5,4,3,2,1 دکھائی دیتا ہے۔',
      'دلته کله چې پروګرام پیل شي، کاروونکی د شاتنۍ شمېرنې د پیلولو لپاره یو عدد لیکي. په دې حالت کې عدد 8 دی، نو شرط n>0 true دی، او د لوړو قوسونو { } دننه بلاک تر هغه اجرا کېږي چې n>0 وي، او پر پرده 8,7,6,5,4,3,2,1 ښکاري.')
    P('Consider another program that prints numbers from 1 to 50 in such a way that there should be 10 digits per line.', 'ایک اور پروگرام پر غور کریں جو 1 سے 50 تک کے اعداد اس طرح پرنٹ کرتا ہے کہ ہر لائن میں 10 اعداد ہوں۔', 'بل پروګرام ته پام وکړئ چې له 1 تر 50 عددونه داسې چاپوي چې په هره کرښه کې ۱۰ عددونه وي.')
    code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
int n = 1;
while (n <= 50)
{
cout << n << " ";
if (n % 10 == 0)
cout << endl;
n++;
}
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 49 50''')
    P('Consider another program using while loop to get a sentence from the user and count the number of characters in this sentence.', 'while لوپ کے ذریعے صارف سے جملہ حاصل کرنے اور اس جملے کے حروف گننے والے ایک اور پروگرام پر غور کریں۔', 'بل پروګرام ته پام وکړئ چې د while حلقې په مرسته له کاروونکي جمله اخلي او په دې جمله کې توري شمېري.')
    rec = BOOK.record(t, 'cs12-u4-text-11', 'Unit 4 text (11)', 'یونٹ 4 — متن (۱۱)', '۴ څپرکی — متن (۱۱)', 71, [130, 131])
    rec['sourceNote'] = 'The top of p.130 (end of the countdown program and output) is recorded with PDF70. The 1-to-50 program ends at the top of p.131 and is given whole here. The sentence-count program starting on p.131 is given whole with PDF72.'
    BOOK.save(71, [(4, rec)], issues=[{'id': 'cs12-pdf071', 'unit': 4, 'printedPage': 131,
               'description': 'Owner pen scribbles (digits) on p.131 are excluded.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 70
    p70() if n == 70 else p71()
