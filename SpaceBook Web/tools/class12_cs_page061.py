"""Computer Science XII PDF61 (spread): printed pp.110–111 — introduction; 4.1 decision statements; 4.1.1; a. if statement; Flowchart 4.1; if program (whole incl. p.112 lines + output)."""
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_4_1

t = Builder()
P = t.p
H = t.h
H('INTRODUCTION', 'تعارف', 'پېژندنه')
P('C++ provides control flow statements, also called flow control statements, which allows the programmer to control the sequence of execution of statements of a program by the processor. The most commonly used control flow statements are decision, repetitions and compound statements.',
  'C++ کنٹرول فلو بیانات فراہم کرتی ہے، جنھیں فلو کنٹرول بیانات بھی کہتے ہیں، جو پروگرامر کو یہ کنٹرول کرنے دیتے ہیں کہ پروسیسر پروگرام کے بیانات کس ترتیب سے چلائے۔ سب سے زیادہ استعمال ہونے والے کنٹرول فلو بیانات فیصلہ، تکرار اور مرکب بیانات ہیں۔',
  'C++ د کنټرول بهیر بیانونه برابروي چې د بهیر کنټرول بیانونه هم بلل کېږي، او پروګرام جوړوونکي ته اجازه ورکوي چې کنټرول کړي پروسېسر د پروګرام بیانونه په کوم ترتیب اجرا کوي. تر ټولو ډېر کارېدونکي د کنټرول بهیر بیانونه پرېکړه‌ییز، تکراري او مرکب بیانونه دي.')
H('4.1 Decision statements', '4.1 فیصلہ کن بیانات', '۴.۱ پرېکړه‌ییز بیانونه')
P('Decision statement is a statement that causes the program to change the path of execution, sequence of execution, based on the value of an expression. It is also called conditional statement. Most commonly used decision support statements are: if, if-else and nested if-else statements. The switch also provides a mechanism for doing conditional branching.',
  'فیصلہ کن بیان وہ بیان ہے جو کسی ایکسپریشن کی قدر کی بنیاد پر پروگرام کے چلنے کا راستہ یعنی عمل کی ترتیب بدل دیتا ہے۔ اسے شرطیہ بیان بھی کہتے ہیں۔ سب سے زیادہ استعمال ہونے والے فیصلہ کن بیانات if، if-else اور نیسٹڈ if-else ہیں۔ switch بھی شرطیہ شاخ بندی کا طریقہ فراہم کرتا ہے۔',
  'پرېکړه‌ییز بیان هغه بیان دی چې د یوې افادې د ارزښت پر بنسټ پروګرام دې ته اړ کوي چې د اجرا لاره، یعنې د اجرا ترتیب، بدل کړي. شرطي بیان هم بلل کېږي. تر ټولو ډېر کارېدونکي پرېکړه‌ییز بیانونه if، if-else او ځالې if-else دي. switch هم د شرطي څانګه‌کولو لاره برابروي.')
H('4.1.1 Use of decision statements', '4.1.1 فیصلہ کن بیانات کا استعمال', '۴.۱.۱ د پرېکړه‌ییزو بیانونو کارونه')
P('In a C++ program, a programmer sometimes needs to execute one statement (or a set of statements) if a certain condition is true and another statement (or set of statements) if it is false. In a C++ program, this is only possible with the use of decision statements. The following are different types of decision statements.',
  'C++ پروگرام میں پروگرامر کو بعض اوقات ایک بیان (یا بیانات کا مجموعہ) چلانا ہوتا ہے اگر کوئی شرط درست ہو اور دوسرا بیان (یا بیانات کا مجموعہ) اگر وہ غلط ہو۔ C++ پروگرام میں یہ صرف فیصلہ کن بیانات کے استعمال سے ممکن ہے۔ فیصلہ کن بیانات کی مختلف اقسام درج ذیل ہیں۔',
  'په C++ پروګرام کې پروګرام جوړوونکی کله کله اړتیا لري چې که یو ټاکلی شرط true وي یو بیان (یا د بیانونو ټولګه) او که false وي بل بیان (یا ټولګه) اجرا کړي. په C++ پروګرام کې دا یوازې د پرېکړه‌ییزو بیانونو په کارولو شونی دی. د پرېکړه‌ییزو بیانونو بېلابېل ډولونه دا دي.')
H('a. if statement', 'a. if بیان', 'a. if بیان')
P('The most basic kind of conditional statement used in C++ is if statement. General syntax of an if statement is given below:', 'C++ میں استعمال ہونے والا سب سے بنیادی شرطیہ بیان if بیان ہے۔ if بیان کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے:', 'په C++ کې تر ټولو بنسټیز شرطي بیان if بیان دی. د if بیان عمومي بڼه لاندې ورکړل شوې:')
P('Single statement if structure', 'ایک بیان والی if ساخت', 'یو-بیانیز if جوړښت')
code(t, '''if (condition)
Statement;''')
P('Multiple statements if structure', 'متعدد بیانات والی if ساخت', 'څو-بیانیز if جوړښت')
code(t, '''if (condition)
{
Statement 1;
Statement 2;
.
.
Statement n;
}''')
P('If the condition is true, the statement after if will be executed and if the condition is false, the statement will be skipped. If we want to execute multiple statements with one if statement then the statements should be enclosed in a pair of curly braces { }.',
  'اگر شرط درست ہو تو if کے بعد والا بیان چلایا جائے گا اور اگر شرط غلط ہو تو بیان چھوڑ دیا جائے گا۔ اگر ہم ایک if بیان کے ساتھ متعدد بیانات چلانا چاہیں تو بیانات کو بریسز { } کے جوڑے میں بند کرنا چاہیے۔',
  'که شرط true وي، د if وروسته بیان اجرا کېږي او که شرط false وي، بیان پرېښودل کېږي. که وغواړو د یوه if بیان سره ډېر بیانونه اجرا کړو، بیانونه باید د لوړو قوسونو { } په یوه جوړه کې وتړل شي.')
P('Flowchart 4.1 shows working of if statement.', 'فلو چارٹ 4.1 if بیان کا عمل دکھاتا ہے۔', '۴.۱ فلوچارټ د if بیان کار ښيي.')
en, ur, ps, ratio = fig_4_1()
t.visual('cs12-fig-4-1', en, ur, ps, ratio)
P('Consider the following program to demonstrate the use of if statement.', 'if بیان کے استعمال کی وضاحت کے لیے درج ذیل پروگرام پر غور کریں۔', 'د if بیان د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
code(t, '''#include <iostream.h>
#include<conio.h>
int main()
{
int X;
cout << "Enter a number: ";
cin >> X;
if (X %2==0)
cout << X << " is even number";
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Enter a number:
12
12 is even number''')
UT = ('Control Structure', 'کنٹرول اسٹرکچر', 'کنټرولي جوړښت')
rec = BOOK.record(t, 'cs12-u4-text-1', 'Unit 4 text (1)', 'یونٹ 4 — متن (۱)', '۴ څپرکی — متن (۱)', 61, [110, 111, 112])
rec['sourceNote'] = 'Flowchart 4.1 is reproduced as a coded diagram. The program starting at the foot of p.111 continues on p.112 (PDF62) and is given whole here with its output.'
issues = [{'id': 'cs12-pdf061', 'unit': 4, 'printedPage': 110,
           'description': 'p.110 prints “control flow statements … which allows the programmer”; the running header reads “Unit-4 Control Structures” while the opener reads “CONTROL STRUCTURE”. Owner pen doodle on p.111 excluded.'}]

if __name__ == '__main__':
    BOOK.save(61, [(4, rec)], issues=issues)
