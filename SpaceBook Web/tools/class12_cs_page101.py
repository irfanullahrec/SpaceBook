"""Computer Science XII PDF101–103: pp.190–195 — 6.1.6 formal and actual parameters, calculate_bill program (whole), 6.1.7 local and global functions,
6.1.8 inline function, min program, 6.2 passing arguments, 6.2.1, a. passing by constants.
Run: python class12_cs_page101.py N (101–103)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u6-text-{n}', f'Unit 6 text ({n})', f'یونٹ 6 — متن ({n})', f'۶ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p101():
    t = Builder()
    P = t.p
    P('Here, the automatic variable Auto_Var losses its values when the control goes out of the function body but the static variable Static_Var keeps its last value even if the control goes out of the function.',
      'یہاں خودکار ویری ایبل Auto_Var اپنی قدریں کھو دیتا ہے جب کنٹرول فنکشن کے جسم سے باہر جاتا ہے، لیکن اسٹیٹک ویری ایبل Static_Var کنٹرول کے فنکشن سے باہر جانے پر بھی اپنی آخری قدر برقرار رکھتا ہے۔',
      'دلته خپلکاره متغیر Auto_Var خپل ارزښتونه له لاسه ورکوي کله چې کنټرول د فنکشن له بدنې ووځي، خو ثابت متغیر Static_Var خپل وروستی ارزښت ساتي حتی که کنټرول له فنکشن ووځي.')
    t.h('6.1.6 Formal parameters and actual parameters', '6.1.6 رسمی پیرامیٹرز اور اصل پیرامیٹرز', '۶.۱.۶ رسمي پاراميټرونه او اصلي پاراميټرونه')
    P('In function prototypes and function calls, variables and values are written in the parenthesis of the functions. These are divided into two categories; formal parameters and actual parameters.', 'فنکشن پروٹوٹائپس اور فنکشن کالز میں ویری ایبلز اور قدریں فنکشنز کی قوسین میں لکھی جاتی ہیں۔ یہ دو زمروں میں تقسیم ہیں؛ رسمی پیرامیٹرز اور اصل پیرامیٹرز۔', 'د فنکشن په نمونو او غوښتنو کې متغیرونه او ارزښتونه د فنکشنونو په قوسونو کې لیکل کېږي. دا په دوو ډلو وېشل کېږي؛ رسمي پاراميټرونه او اصلي پاراميټرونه.')
    t.h('a. Formal parameters', 'a. رسمی پیرامیٹرز', 'a. رسمي پاراميټرونه')
    P('Formal parameters are those parameters which appear in function declarator/header and also in function prototype. These are also called formal arguments and are used to receive values for functions.', 'رسمی پیرامیٹرز وہ پیرامیٹرز ہیں جو فنکشن ڈکلیریٹر/ہیڈر اور فنکشن پروٹوٹائپ میں بھی آتے ہیں۔ انھیں رسمی آرگیومنٹس بھی کہتے ہیں اور یہ فنکشنز کے لیے قدریں وصول کرنے کے لیے استعمال ہوتے ہیں۔', 'رسمي پاراميټرونه هغه پاراميټرونه دي چې د فنکشن په اعلانوونکي/سرلیک او د فنکشن په نمونه کې هم راځي. دا رسمي دلیلونه هم بلل کېږي او د فنکشنونو لپاره د ارزښتونو ترلاسه کولو لپاره کارېږي.')
    P('For example:', 'مثال کے طور پر:', 'د بېلګې په توګه:')
    code(t, '''void foo(int x); // prototype -- x is a formal parameter
void foo(int x) // declarator -- x is a formal parameter
{
body
}''')
    t.h('b. Actual parameters', 'b. اصل پیرامیٹرز', 'b. اصلي پاراميټرونه')
    P('Actual parameters are those parameters which appear in function calls and are used to send data to formal parameters. These are also called actual arguments. Consider the following function call:', 'اصل پیرامیٹرز وہ پیرامیٹرز ہیں جو فنکشن کالز میں آتے ہیں اور رسمی پیرامیٹرز کو ڈیٹا بھیجنے کے لیے استعمال ہوتے ہیں۔ انھیں اصل آرگیومنٹس بھی کہتے ہیں۔ درج ذیل فنکشن کال پر غور کریں:', 'اصلي پاراميټرونه هغه پاراميټرونه دي چې د فنکشن په غوښتنو کې راځي او رسمي پاراميټرونو ته د ډېټا لېږلو لپاره کارېږي. دا اصلي دلیلونه هم بلل کېږي. لاندې د فنکشن غوښتنې ته پام وکړئ:')
    code(t, '''foo(6); // 6 is the argument passed to parameter x
foo(y+1); // the value of (y+1) is the argument passed to parameter x''')
    P('The actual parameters can be fixed values or variables holding values or expressions resulting in some values.', 'اصل پیرامیٹرز مقررہ قدریں، قدریں رکھنے والے ویری ایبلز یا کسی قدر پر منتج ہونے والے ایکسپریشنز ہو سکتے ہیں۔', 'اصلي پاراميټرونه کېدای شي ټاکلي ارزښتونه، ارزښت لرونکي متغیرونه یا داسې افادې وي چې یو ارزښت ورکوي.')
    P('In the function main, in the following example, rice, chicken and fruit are actual parameters when used to call calculate_bill. On the other hand, the corresponding variables in calculate_bill (namely diner1, diner2 and diner3, respectively) are formal parameters because they appear in the function definition and receive values passed in the function call.',
      'درج ذیل مثال میں فنکشن main میں rice، chicken اور fruit اصل پیرامیٹرز ہیں جب انھیں calculate_bill کال کرنے کے لیے استعمال کیا جائے۔ دوسری طرف calculate_bill میں متعلقہ ویری ایبلز (یعنی بالترتیب diner1، diner2 اور diner3) رسمی پیرامیٹرز ہیں کیونکہ یہ فنکشن کی تعریف میں آتے ہیں اور فنکشن کال میں پاس کی گئی قدریں وصول کرتے ہیں۔',
      'په لاندې بېلګه کې د main په فنکشن کې rice، chicken او fruit اصلي پاراميټرونه دي کله چې د calculate_bill د غوښتلو لپاره وکارول شي. له بلې خوا په calculate_bill کې اړوند متغیرونه (یعنې په ترتیب سره diner1، diner2 او diner3) رسمي پاراميټرونه دي ځکه د فنکشن په تعریف کې راځي او د فنکشن په غوښتنه کې لېږدول شوي ارزښتونه ترلاسه کوي.')
    P('Let’s look at calculate_bill function in the following program:', 'آئیے درج ذیل پروگرام میں calculate_bill فنکشن دیکھیں:', 'راځئ په لاندې پروګرام کې calculate_bill فنکشن وګورو:')
    code(t, '''/* formal and actual parameters program */
#include <stdio.h>
#include<conio.h>
#include <iostream.h>
int calculate_bill (int, int, int);
int main()
{
int bill;
int rice = 25;
int chicken = 32;
int fruit = 27;
bill = calculate_bill (rice, chicken, fruit);   // ← Actual Parameters
cout<<"The total bill comes to "<<bill<< “Rs.”;
getch();
return 0;
}
int calculate_bill (int diner1, int diner2, int diner3)   // ← Formal Parameters
{
int total;
total = diner1 + diner2 + diner3;
return total;
}''')
    P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, 'The total bill comes to 84 Rs.')
    BOOK.save(101, [(6, rec(t, 8, 101, [190, 191, 192], 'The “Actual Parameters” and “Formal Parameters” callout boxes on p.191 are reproduced as end-of-line markers in the listing. The program ends on p.192 (PDF102) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf101', 'unit': 6, 'printedPage': 190,
                       'description': 'p.190 “Auto_Var losses its values”; the cout uses curly quotes around “Rs.”. Retained as printed.'}])


def p102():
    t = Builder()
    P = t.p
    P('Although, formal parameters are always variables but actual parameters may not be variables. Numbers, expressions, or even function calls can also be used as actual parameters. Here are some examples of valid actual parameters in the function call to calculate_bill:',
      'اگرچہ رسمی پیرامیٹرز ہمیشہ ویری ایبلز ہوتے ہیں لیکن اصل پیرامیٹرز ضروری نہیں کہ ویری ایبلز ہوں۔ اعداد، ایکسپریشنز یا فنکشن کالز بھی اصل پیرامیٹرز کے طور پر استعمال ہو سکتے ہیں۔ calculate_bill کو فنکشن کال میں درست اصل پیرامیٹرز کی کچھ مثالیں یہ ہیں:',
      'که څه هم رسمي پاراميټرونه تل متغیرونه وي، خو اصلي پاراميټرونه ښايي متغیرونه نه وي. عددونه، افادې یا حتی د فنکشن غوښتنې هم د اصلي پاراميټرونو په توګه کارېدای شي. د calculate_bill په غوښتنه کې د سمو اصلي پاراميټرونو ځینې بېلګې دا دي:')
    code(t, '''bill = calculate_bill (25, 32, 27);
bill = calculate_bill (50+60, 25*2, 100-75);
bill = calculate_bill (rice, chicken, (int) sqrt(27));''')
    t.h('6.1.7 Local and Global functions', '6.1.7 مقامی اور عالمی فنکشنز', '۶.۱.۷ محلي او نړیوال فنکشنونه')
    P('The terms local and global functions specify the scope of functions within programs. Based on the scope of the functions, functions are categorized into two types; local functions and global functions.', 'مقامی اور عالمی فنکشنز کی اصطلاحات پروگراموں میں فنکشنز کا دائرہ بتاتی ہیں۔ فنکشنز کے دائرے کی بنیاد پر فنکشنز دو اقسام میں تقسیم ہیں؛ مقامی فنکشنز اور عالمی فنکشنز۔', 'د محلي او نړیوالو فنکشنونو اصطلاحګانې په پروګرامونو کې د فنکشنونو ساحه ښيي. د فنکشنونو د ساحې پر بنسټ فنکشنونه په دوو ډولونو وېشل کېږي؛ محلي فنکشنونه او نړیوال فنکشنونه.')
    t.h('a. Local functions', 'a. مقامی فنکشنز', 'a. محلي فنکشنونه')
    P('Those functions which are defined inside the body of another function are called local function. Normally, we use built-in function inside the body of main () function to perform our activities. Such declarations are termed as local.', 'وہ فنکشنز جو کسی دوسرے فنکشن کے جسم کے اندر بیان کیے جائیں، مقامی فنکشن کہلاتے ہیں۔ عموماً ہم اپنے کام انجام دینے کے لیے main () فنکشن کے جسم کے اندر بلٹ اِن فنکشن استعمال کرتے ہیں۔ ایسی ڈکلیریشنز مقامی کہلاتی ہیں۔', 'هغه فنکشنونه چې د بل فنکشن د بدنې دننه تعریف شي، محلي فنکشن بلل کېږي. عموماً موږ د خپلو کارونو لپاره د main () فنکشن د بدنې دننه جوړ شوي فنکشن کاروو. داسې اعلانونه محلي بلل کېږي.')
    t.h('b. Global functions', 'b. عالمی فنکشنز', 'b. نړیوال فنکشنونه')
    P('A function declared outside any function is called global function. A global function can be accessed from any part of the program. Normally, user-defined functions are considered as global function if they are defined before the main () function and are thus accessible to every part of the program.',
      'کسی بھی فنکشن کے باہر ڈکلیئر کیا گیا فنکشن عالمی فنکشن کہلاتا ہے۔ عالمی فنکشن تک پروگرام کے کسی بھی حصے سے رسائی ہو سکتی ہے۔ عموماً یوزر ڈیفائنڈ فنکشنز عالمی فنکشن سمجھے جاتے ہیں اگر وہ main () فنکشن سے پہلے بیان کیے گئے ہوں اور یوں پروگرام کے ہر حصے کے لیے قابلِ رسائی ہوتے ہیں۔',
      'هغه فنکشن چې له هر فنکشن بهر اعلان شي، نړیوال فنکشن بلل کېږي. نړیوال فنکشن ته د پروګرام له هرې برخې لاسرسی کېدای شي. عموماً د کاروونکي-تعریف شوي فنکشنونه نړیوال ګڼل کېږي که د main () فنکشن مخکې تعریف شوي وي او په دې توګه د پروګرام هرې برخې ته د لاسرسي وړ وي.')
    t.h('6.1.8 inline function', '6.1.8 inline فنکشن', '۶.۱.۸ inline فنکشن')
    P('Using function calls in program, a lot of time is wasted in passing control from the calling function to the called function and returning control back to the calling function. This limitation can be overcome by the use of inline function.',
      'پروگرام میں فنکشن کالز استعمال کرنے سے کال کرنے والے فنکشن سے کال کیے گئے فنکشن تک کنٹرول منتقل کرنے اور کنٹرول کو واپس کال کرنے والے فنکشن تک لانے میں کافی وقت ضائع ہوتا ہے۔ اس حد پر inline فنکشن کے استعمال سے قابو پایا جا سکتا ہے۔',
      'په پروګرام کې د فنکشن غوښتنو په کارولو، له غوښتونکي فنکشن څخه غوښتل شوي فنکشن ته د کنټرول په لېږدولو او بېرته غوښتونکي فنکشن ته د کنټرول په راګرځولو کې ډېر وخت ضایع کېږي. دا محدودیت د inline فنکشن په کارولو لرې کېدای شي.')
    P('C++ offers a way to combine the advantages of functions with the speed of code written in-place with the help of inline functions. In inline function, the function return type is preceded by the inline keyword which requests the compiler to treat the function as an inline and do not jump again and again to the called function. In the case of inline function, when the compiler compiles the code, all inline functions are expanded in-place, that is, the function call is replaced with a copy of the code of the function itself, which removes the function call overhead.',
      'C++ inline فنکشنز کی مدد سے فنکشنز کے فوائد کو اپنی جگہ لکھے گئے کوڈ کی رفتار کے ساتھ ملانے کا طریقہ فراہم کرتی ہے۔ inline فنکشن میں فنکشن کی ریٹرن ٹائپ سے پہلے inline کلیدی لفظ آتا ہے جو کمپائلر سے درخواست کرتا ہے کہ فنکشن کو inline سمجھے اور بار بار کال کیے گئے فنکشن پر نہ جائے۔ inline فنکشن کی صورت میں جب کمپائلر کوڈ کمپائل کرتا ہے تو تمام inline فنکشنز اپنی جگہ پھیلا دیے جاتے ہیں، یعنی فنکشن کال کو خود فنکشن کے کوڈ کی نقل سے بدل دیا جاتا ہے، جس سے فنکشن کال کا اضافی بوجھ ختم ہو جاتا ہے۔',
      'C++ د inline فنکشنونو په مرسته لاره برابروي چې د فنکشنونو ګټې په ځای لیکل شوي کوډ له سرعت سره یوځای کړي. په inline فنکشن کې د فنکشن د بېرته ورکړې ډول ته inline کلیدي کلمه مخکې لیکل کېږي چې له کمپایلر غوښتنه کوي فنکشن inline وګڼي او بیا بیا غوښتل شوي فنکشن ته ټوپ ونه وهي. د inline فنکشن په حالت کې کله چې کمپایلر کوډ کمپایل کړي، ټول inline فنکشنونه په ځای پراخېږي، یعنې د فنکشن غوښتنه د فنکشن د کوډ په کاپي بدلېږي، چې د فنکشن غوښتنې اضافي بار لرې کوي.')
    P('The disadvantage of the inline function is that it can make the compiled code quite larger, especially if the inline function is long and/or there are many calls to the inline function.', 'inline فنکشن کا نقصان یہ ہے کہ یہ کمپائل شدہ کوڈ کو کافی بڑا کر سکتا ہے، خاص طور پر اگر inline فنکشن لمبا ہو اور/یا inline فنکشن کو بہت سی کالز ہوں۔', 'د inline فنکشن زیان دا دی چې کمپایل شوی کوډ ډېر لویولی شي، په ځانګړي ډول که inline فنکشن اوږد وي او/یا inline فنکشن ته ډېرې غوښتنې وي.')
    P('The format for the declaration of inline function is given in the following segment.', 'inline فنکشن کی ڈکلیریشن کی شکل درج ذیل حصے میں دی گئی ہے۔', 'د inline فنکشن د اعلان بڼه په لاندې برخه کې ورکړل شوې.')
    code(t, '''inline type name ( arguments ... )
{
Statements;
}''')
    BOOK.save(102, [(6, rec(t, 9, 102, [192, 193], 'The top of p.192 (end of the calculate_bill program and its output) is recorded with PDF101.'))])


def p103():
    t = Builder()
    P = t.p
    P('Calling an inline function is simple and is just like the call to any other function. In the call, the inline keyword is not needed to be included.', 'inline فنکشن کو کال کرنا آسان ہے اور کسی بھی دوسرے فنکشن کی کال جیسا ہے۔ کال میں inline کلیدی لفظ شامل کرنے کی ضرورت نہیں۔', 'د inline فنکشن غوښتل اسانه دي او د هر بل فنکشن غوښتنې په څېر دي. په غوښتنه کې د inline کلیدي کلمې شاملولو ته اړتیا نشته.')
    P('The following program demonstrates the use of inline function in a program.', 'درج ذیل پروگرام کسی پروگرام میں inline فنکشن کا استعمال دکھاتا ہے۔', 'لاندې پروګرام په یوه پروګرام کې د inline فنکشن کارونه ښيي.')
    code(t, '''/* use of inline function to find minimum out of two integers*/
#include<iostream.h>
#include<conio.h>
inline int min(int a, int b)
{
return a > b ? b : a;
}
int main()
{
cout <<"Minimum out of 25 and 26 is: "<<min(25, 26);
cout <<"\\nMinimum out of 23 and 22 is:"<<min(23,22);
getch() ;
return 0;
}''')
    P(*OUT)
    code(t, '''Minimum out of 25 and 26 is: 25
Minimum out of 23 and 22 is: 22''')
    t.h('6.2 Passing arguments and returning values', '6.2 آرگیومنٹس پاس کرنا اور قدریں واپس کرنا', '۶.۲ د دلیلونو لېږدول او د ارزښتونو بېرته ورکول')
    P('When we want to execute functions, we need to pass arguments (values) to a function. The result (values) produced within the function body is then returned back to the calling program. The following section describes different methods used for passing arguments (values) to functions.',
      'جب ہم فنکشنز چلانا چاہیں تو ہمیں فنکشن کو آرگیومنٹس (قدریں) پاس کرنی ہوتی ہیں۔ فنکشن کے جسم میں پیدا ہونے والا نتیجہ (قدریں) پھر کال کرنے والے پروگرام کو واپس کیا جاتا ہے۔ درج ذیل حصہ فنکشنز کو آرگیومنٹس (قدریں) پاس کرنے کے مختلف طریقے بیان کرتا ہے۔',
      'کله چې فنکشنونه اجرا کول غواړو، فنکشن ته دلیلونه (ارزښتونه) لېږدول اړین دي. د فنکشن په بدنه کې تولید شوې پایله (ارزښتونه) بیا غوښتونکي پروګرام ته ورګرځول کېږي. لاندې برخه فنکشنونو ته د دلیلونو (ارزښتونو) د لېږدولو بېلې لارې بیانوي.')
    t.h('6.2.1 Passing arguments', '6.2.1 آرگیومنٹس پاس کرنا', '۶.۲.۱ د دلیلونو لېږدول')
    P('The following are the most commonly used methods of passing arguments to functions.', 'فنکشنز کو آرگیومنٹس پاس کرنے کے سب سے عام طریقے درج ذیل ہیں۔', 'فنکشنونو ته د دلیلونو د لېږدولو تر ټولو عامې لارې دا دي.')
    t.group('list', [('Passing arguments by constants', 'مستقل کے ذریعے آرگیومنٹس پاس کرنا', 'د ثابتونو له لارې د دلیلونو لېږدول'), ('Passing arguments by values', 'قدر کے ذریعے آرگیومنٹس پاس کرنا', 'د ارزښت له لارې د دلیلونو لېږدول'), ('Passing arguments by reference', 'حوالے کے ذریعے آرگیومنٹس پاس کرنا', 'د حوالې له لارې د دلیلونو لېږدول')])
    t.h('a. Passing arguments by constants', 'a. مستقل کے ذریعے آرگیومنٹس پاس کرنا', 'a. د ثابتونو له لارې د دلیلونو لېږدول')
    P('While calling a function, arguments are passed to the calling function. In passing constants as arguments, the actual constant values are passed instead of passing the variables.', 'فنکشن کال کرتے وقت آرگیومنٹس کال کرنے والے فنکشن کو پاس کیے جاتے ہیں۔ مستقل کو آرگیومنٹس کے طور پر پاس کرنے میں ویری ایبلز کے بجائے اصل مستقل قدریں پاس کی جاتی ہیں۔', 'د فنکشن د غوښتلو پر مهال دلیلونه غوښتونکي فنکشن ته لېږدول کېږي. د ثابتونو د دلیلونو په توګه لېږدولو کې د متغیرونو پر ځای اصلي ثابت ارزښتونه لېږدول کېږي.')
    P('Consider the following program:', 'درج ذیل پروگرام پر غور کریں:', 'لاندې پروګرام ته پام وکړئ:')
    code(t, '''// passing integer constant as argument.
#include<iostream.h>
#include<conio.h>
void display(int x)
{
cout << " x= " << x << endl;
}.
int main()
{
display(25); // function call
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'x = 25')
    BOOK.save(103, [(6, rec(t, 10, 103, [194, 195]))], issues=[{'id': 'cs12-pdf103', 'unit': 6, 'printedPage': 195,
               'description': 'The display() definition ends with “}.” (stray full stop); p.195 says arguments are passed “to the calling function”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 101
    {101: p101, 102: p102, 103: p103}[n]()
