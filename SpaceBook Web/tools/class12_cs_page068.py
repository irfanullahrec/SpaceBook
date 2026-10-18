"""Computer Science XII PDF68–69: pp.124–125 4.2.1 types of loops, a. for loop, Flowchart 4.4, steps, PAKISTAN program (whole incl. p.126);
pp.126–127 countdown, optional fields, b. while loop (begins).
Run: python class12_cs_page068.py N (68 or 69)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_4_4


def p68():
    t = Builder()
    P = t.p
    t.h('4.2.1 Types of loops', '4.2.1 لوپس کی اقسام', '۴.۲.۱ د حلقو ډولونه')
    P('There are three types of loops.', 'لوپس کی تین اقسام ہیں۔', 'د حلقو درې ډولونه دي.')
    t.group('list', [('for', 'for', 'for'), ('while', 'while', 'while'), ('do-while', 'do-while', 'do-while')])
    t.h('a. for loop', 'a. for لوپ', 'a. for حلقه')
    P('The most commonly used looping structure in C++ is for loop. for loop is ideal in situation when we know in advance the exact number of iteration. Its general syntax is:',
      'C++ میں سب سے زیادہ استعمال ہونے والی لوپنگ ساخت for لوپ ہے۔ for لوپ اس صورت میں مثالی ہے جب ہمیں تکرار کی درست تعداد پہلے سے معلوم ہو۔ اس کا عمومی طریقۂ تحریر یہ ہے:',
      'په C++ کې تر ټولو ډېر کارېدونکی حلقوي جوړښت for حلقه ده. for حلقه هغه وخت غوره ده چې موږ د تکرار دقیق شمېر مخکې له مخکې پېژنو. عمومي بڼه یې دا ده:')
    P('Single statement for-loop', 'ایک بیان والا for لوپ', 'یو-بیانیزه for حلقه')
    code(t, '''for (initialization; condition; increment/decrement)
statement;''')
    P('Multiple statements for-loop', 'متعدد بیانات والا for لوپ', 'څو-بیانیزه for حلقه')
    code(t, '''for (initialization; condition; increment/decrement)
{
Statement 1;
Statement 2;
.
.
Statement n;
}''')
    P('In the above two general forms of for loop, the first one has only one statement in its body and has no need for braces { } while in the second form multiple statements are used so they are enclosed in the pair of braces { }.',
      'for لوپ کی اوپر کی دو عمومی شکلوں میں پہلی کے جسم میں صرف ایک بیان ہے اور اسے بریسز { } کی ضرورت نہیں، جبکہ دوسری شکل میں متعدد بیانات استعمال ہوتے ہیں اس لیے انھیں بریسز { } کے جوڑے میں بند کیا جاتا ہے۔',
      'د for حلقې په پورته دوو عمومي بڼو کې لومړۍ په بدنه کې یوازې یو بیان لري او لوړو قوسونو { } ته اړتیا نه لري، په داسې حال کې چې په دویمه بڼه کې ډېر بیانونه کارېږي نو د لوړو قوسونو { } په جوړه کې تړل کېږي.')
    P('The main function of for loop is to repeat statement(s) while condition remains true. It works in the following way shown in Flowchart 4.4.',
      'for لوپ کا بنیادی کام شرط درست رہنے تک بیان (بیانات) دہرانا ہے۔ یہ فلو چارٹ 4.4 میں دکھائے گئے طریقے سے کام کرتا ہے۔',
      'د for حلقې اصلي دنده د بیان (بیانونو) تکرار دی تر هغه چې شرط true پاتې وي. دا په ۴.۴ فلوچارټ کې ښودل شوي ډول کار کوي.')
    en, ur, ps, ratio = fig_4_4()
    t.visual('cs12-fig-4-4', en, ur, ps, ratio)
    t.group('lines', [
     ('1. Initialization: Generally it is an initial value setting for a counter variable. This is executed only once.', '1۔ ابتدائی قدر: عموماً یہ کاؤنٹر ویری ایبل کی ابتدائی قدر مقرر کرنا ہے۔ یہ صرف ایک بار چلتا ہے۔', '۱. لومړنی ارزښت: عموماً دا د شمېرونکي متغیر لومړنی ارزښت ټاکل دي. دا یوازې یو ځل اجرا کېږي.'),
     ('2. Condition: If it is true the loop continues, otherwise the loop ends and statement is skipped (not executed).', '2۔ شرط: اگر یہ درست ہو تو لوپ جاری رہتا ہے، ورنہ لوپ ختم ہو جاتا ہے اور بیان چھوڑ دیا جاتا ہے (نہیں چلتا)۔', '۲. شرط: که true وي حلقه دوام کوي، که نه حلقه پای ته رسېږي او بیان پرېښودل کېږي (نه اجرا کېږي).'),
     ('3. Loop Body: It can either be a single statement or a block enclosed in braces { }, for multiple statements.', '3۔ لوپ کا جسم: یہ ایک بیان یا متعدد بیانات کے لیے بریسز { } میں بند بلاک ہو سکتا ہے۔', '۳. د حلقې بدنه: کېدای شي یو بیان یا د ډېرو بیانونو لپاره په لوړو قوسونو { } کې تړلی بلاک وي.'),
     ('4. Finally, the loop counter is incremented/decremented and control goes back to step2.', '4۔ آخر میں لوپ کاؤنٹر میں اضافہ/کمی ہوتی ہے اور کنٹرول مرحلہ 2 پر واپس جاتا ہے۔', '۴. په پای کې د حلقې شمېرونکی زیاتېږي/کمېږي او کنټرول دویم ګام ته ستنېږي.')])
    P('Consider the following program to display the string PAKISTAN five times on the screen.', 'اسکرین پر اسٹرنگ PAKISTAN پانچ بار دکھانے کے لیے درج ذیل پروگرام پر غور کریں۔', 'پر پرده د PAKISTAN تار پنځه ځله ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''#include <iostream.h>
#include<conio.h>
int main()
{
for (int i=1; i<6; i++)
cout << "PAKISTAN"<<endl;
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''PAKISTAN
PAKISTAN
PAKISTAN
PAKISTAN
PAKISTAN''')
    rec = BOOK.record(t, 'cs12-u4-text-8', 'Unit 4 text (8)', 'یونٹ 4 — متن (۸)', '۴ څپرکی — متن (۸)', 68, [124, 125, 126])
    rec['sourceNote'] = 'Flowchart 4.4 is reproduced as a coded diagram. The PAKISTAN program continues on p.126 (PDF69) and is given whole with its output.'
    BOOK.save(68, [(4, rec)], issues=[{'id': 'cs12-pdf068', 'unit': 4, 'printedPage': 124,
               'description': 'p.124 prints “for loop is ideal in situation when we know … the exact number of iteration”; p.125 “goes back to step2”. Retained as printed. A tear across the top-left corner of p.125 does not affect the text.'}])


def p69():
    t = Builder()
    P = t.p
    P('Here is an example of countdown using for loop:', 'for لوپ کے ذریعے الٹی گنتی کی ایک مثال یہ ہے:', 'دلته د for حلقې په مرسته د شاتنۍ شمېرنې یوه بېلګه ده:')
    code(t, '''// countdown using a for loop
#include <iostream.h>
#include<conio.h>
int main()
{
for (int n=10; n>0; n--)
cout << n << ", ";
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '10, 9, 8, 7, 6, 5, 4, 3, 2, 1')
    P('The initialization and increment/decrement fields are optional. They can remain empty, but in all cases the semicolon signs between them must be written. For example, we could write: for (;n<10;) if we want to specify no initialization and no increase.',
      'ابتدائی قدر اور اضافہ/کمی کے فیلڈز اختیاری ہیں۔ یہ خالی رہ سکتے ہیں، لیکن ہر صورت میں ان کے درمیان سیمی کولن لکھنا لازمی ہے۔ مثلاً اگر ہم نہ ابتدائی قدر دینا چاہیں نہ اضافہ تو ہم لکھ سکتے ہیں: for (;n<10;)',
      'د لومړني ارزښت او زیاتولو/کمولو ساحې اختیاري دي. تشې پاتې کېدای شي، خو په هر حال کې د هغوی ترمنځ سیمي‌کولنونه باید ولیکل شي. د بېلګې په توګه که نه لومړنی ارزښت او نه زیاتوالی وغواړو، لیکلی شو: for (;n<10;)')
    code(t, '''int n=0;
for ( ; n < 10; )
{
cout << n << ",";
n++;
}''')
    P('Output of the code segment', 'کوڈ کے حصے کا آؤٹ پٹ', 'د کوډ د برخې وتنه')
    code(t, '0,1,2,3,4,5,6,7,8,9')
    P('Similarly, for loop can also be used as: for (;n<10;n++) if we want to include an increment/decrement expression but no initialization.',
      'اسی طرح اگر ہم اضافہ/کمی کا ایکسپریشن شامل کرنا چاہیں لیکن ابتدائی قدر نہیں تو for لوپ کو یوں بھی استعمال کیا جا سکتا ہے: for (;n<10;n++)',
      'همداراز که وغواړو د زیاتولو/کمولو افاده شامله کړو خو لومړنی ارزښت نه، for حلقه داسې هم کارول کېدای شي: for (;n<10;n++)')
    t.h('b. while loop', 'b. while لوپ', 'b. while حلقه')
    P('while loop is another structure that is used in computer programs to repeat a statement or a group of statements until the condition is true.',
      'while لوپ ایک اور ساخت ہے جو کمپیوٹر پروگراموں میں کسی بیان یا بیانات کے گروپ کو شرط درست رہنے تک دہرانے کے لیے استعمال ہوتی ہے۔',
      'while حلقه بل جوړښت دی چې په کمپیوټري پروګرامونو کې د یوه بیان یا د بیانونو د ډلې د تکرار لپاره تر هغه کارول کېږي چې شرط true وي.')
    rec = BOOK.record(t, 'cs12-u4-text-9', 'Unit 4 text (9)', 'یونٹ 4 — متن (۹)', '۴ څپرکی — متن (۹)', 69, [126, 127])
    rec['sourceNote'] = 'The top of p.126 (end of the PAKISTAN program and output) is recorded with PDF68. The while syntax starting at the foot of p.127 is given whole with PDF70.'
    BOOK.save(69, [(4, rec)], issues=[{'id': 'cs12-pdf069', 'unit': 4, 'printedPage': 127,
               'description': 'The countdown output prints “10, 9, …, 1” without the trailing “, ” the program would print. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 68
    p68() if n == 68 else p69()
