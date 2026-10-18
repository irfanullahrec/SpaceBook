"""Computer Science XII PDF72 (spread): printed pp.132–133 — sentence-count program (whole, from p.131) + output; while vs for; c. do-while loop; Flowchart 4.6; do-while PAKISTAN program."""
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_4_6

t = Builder()
P = t.p
H = t.h
code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
char ch;
int NumberOfCharacters=0;
ch= getche();
while (ch!= '.')
{
++NumberOfCharacters;
ch= getche();
}
cout<< "The number of characters in the sentence are: "<<NumberOfCharacters;
getch();
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Welcome to the class.
The number of characters in the sentence are: 20''')
P('The main difference of the while loop and for is that in while loop it is not necessary to know the exact number of iterations of the body of the loop in advance as in for loop.',
  'while لوپ اور for میں بنیادی فرق یہ ہے کہ while لوپ میں for لوپ کی طرح لوپ کے جسم کی تکرار کی درست تعداد پہلے سے جاننا ضروری نہیں۔',
  'د while حلقې او for اصلي توپیر دا دی چې په while حلقه کې د for حلقې په څېر د حلقې د بدنې د تکرارونو دقیق شمېر مخکې له مخکې پېژندل اړین نه دي.')
H('c. do- while loop', 'c. do-while لوپ', 'c. do-while حلقه')
P('Sometime a programmer want to execute the loop at least once for some problems. To do this, C++ offers the facility of do while loop. The general format of a do while loop is:',
  'بعض اوقات پروگرامر کچھ مسائل کے لیے لوپ کو کم از کم ایک بار چلانا چاہتا ہے۔ اس کے لیے C++ do while لوپ کی سہولت دیتی ہے۔ do while لوپ کی عمومی شکل یہ ہے:',
  'کله کله پروګرام جوړوونکی غواړي د ځینو ستونزو لپاره حلقه لږ تر لږه یو ځل اجرا کړي. د دې لپاره C++ د do while حلقې اسانتیا برابروي. د do while حلقې عمومي بڼه دا ده:')
code(t, '''do
{
Statement 1;
Statement 2;
.
.
Statement n;
}
while (condition);''')
P('The working of do while loop is the same as the while loop, except that the condition in do while loop is checked after the execution of the body of the loop. The execution of do while loop, guaranties the execution of the statements in its body, at least once, even if the condition is false.',
  'do while لوپ کا کام while لوپ جیسا ہی ہے، سوائے اس کے کہ do while لوپ میں شرط لوپ کے جسم کے چلنے کے بعد جانچی جاتی ہے۔ do while لوپ کا عمل اس کے جسم کے بیانات کے کم از کم ایک بار چلنے کی ضمانت دیتا ہے، چاہے شرط غلط ہی کیوں نہ ہو۔',
  'د do while حلقې کار د while حلقې په څېر دی، پرته له دې چې په do while حلقه کې شرط د حلقې د بدنې له اجرا وروسته کتل کېږي. د do while حلقې اجرا د هغې د بدنې بیانونه لږ تر لږه یو ځل اجرا کول تضمینوي، حتی که شرط false وي.')
P('Flowchart 4.6 shows working of while loop.', 'فلو چارٹ 4.6 while لوپ کا عمل دکھاتا ہے۔', '۴.۶ فلوچارټ د while حلقې کار ښيي.')
en, ur, ps, ratio = fig_4_6()
t.visual('cs12-fig-4-6', en, ur, ps, ratio)
P('Consider the following program that prints the string PAKISTAN once although the condition is false in the start.', 'درج ذیل پروگرام پر غور کریں جو اسٹرنگ PAKISTAN ایک بار پرنٹ کرتا ہے حالانکہ شروع میں شرط غلط ہے۔', 'لاندې پروګرام ته پام وکړئ چې د PAKISTAN تار یو ځل چاپوي، که څه هم په پیل کې شرط false دی.')
code(t, '''// displaying PAKISTAN at least once using do while loop
#include <iostream.h>
#include<conio.h>
int main()
{
int i=10;
{
cout << "PAKISTAN"<<endl;
++i;
} while (i<6);
getch();
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'PAKISTAN')
rec = BOOK.record(t, 'cs12-u4-text-12', 'Unit 4 text (12)', 'یونٹ 4 — متن (۱۲)', '۴ څپرکی — متن (۱۲)', 72, [131, 132, 133])
rec['sourceNote'] = 'The sentence-count program starts on p.131 and ends at the top of p.132; it is given whole here. Flowchart 4.6 is reproduced as a coded diagram.'
issues = [{'id': 'cs12-pdf072', 'unit': 4, 'printedPage': 133,
           'description': 'p.133 says “Flowchart 4.6 shows working of while loop” though it depicts the do-while loop; the do-while PAKISTAN listing omits the keyword “do” before the block; the sentence program uses getche() (prints the typed characters) and the output count 20 excludes the full stop. p.132 “Sometime a programmer want”, “guaranties”. All retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(72, [(4, rec)], issues=issues)
