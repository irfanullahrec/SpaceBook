"""Computer Science XII PDF98–100: pp.184–189 — function declarator and body, c. function call, maximum program, 6.1.5 scope of variables,
a. local variables, square program, b. global variables, global program (whole), c. static variables, static/auto program.
Run: python class12_cs_page098.py N (98–100)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u6-text-{n}', f'Unit 6 text ({n})', f'یونٹ 6 — متن ({n})', f'۶ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p98():
    t = Builder()
    P = t.p
    code(t, 'int maximum( int x, int y, int z)')
    P('The second part of function definition is the function body. It contains the actual statements that perform the intended task and is always enclosed in { }.', 'فنکشن کی تعریف کا دوسرا حصہ فنکشن کا جسم ہے۔ اس میں وہ اصل بیانات ہوتے ہیں جو مطلوبہ کام انجام دیتے ہیں اور یہ ہمیشہ { } میں بند ہوتا ہے۔', 'د فنکشن د تعریف دویمه برخه د فنکشن بدنه ده. هغه اصلي بیانونه لري چې غوښتل شوې دنده ترسره کوي او تل په { } کې تړل کېږي.')
    P('The whole function definition is shown below:', 'پوری فنکشن کی تعریف ذیل میں دکھائی گئی ہے:', 'د فنکشن بشپړ تعریف لاندې ښودل شوی:')
    code(t, '''int maximum(int x. int y, int z) // function declarator
{
int max = x;          ┐
if ( y > max )        │
max = y;              │
if ( z > max )        ├ function body
max = z;              │
return max;           ┘
}''')
    t.h('c. Function call', 'c. فنکشن کال', 'c. د فنکشن غوښتنه')
    P('A function call is a statement in the calling function (e.g. main() function) to execute the code of the function. Consider the following statement:', 'فنکشن کال، کال کرنے والے فنکشن (مثلاً main() فنکشن) میں ایک بیان ہے جو فنکشن کا کوڈ چلاتا ہے۔ درج ذیل بیان پر غور کریں:', 'د فنکشن غوښتنه په غوښتونکي فنکشن (لکه main() فنکشن) کې یو بیان دی چې د فنکشن کوډ اجرا کوي. لاندې بیان ته پام وکړئ:')
    code(t, 'maximum( a, b, c );')
    P('The function call has the list of arguments that are passed to the function declarator. The arguments in this call are a, b and c. The following program shows different parts of the function i.e. prototype, definition and call.',
      'فنکشن کال میں آرگیومنٹس کی فہرست ہوتی ہے جو فنکشن ڈکلیریٹر کو پاس کی جاتی ہے۔ اس کال میں آرگیومنٹس a، b اور c ہیں۔ درج ذیل پروگرام فنکشن کے مختلف حصے یعنی پروٹوٹائپ، تعریف اور کال دکھاتا ہے۔',
      'د فنکشن غوښتنه د دلیلونو لړلیک لري چې د فنکشن اعلانوونکي ته لېږدول کېږي. په دې غوښتنه کې دلیلونه a، b او c دي. لاندې پروګرام د فنکشن بېلې برخې یعنې نمونه، تعریف او غوښتنه ښيي.')
    code(t, '''// finding maximum out of three integers using function
#include <conio.h>
#include <iostream.h>
int maximum( int, int, int ); // function prototype
int main()
{
int a, b, c;
cout << "Enter three integers: ";
cin >> a >> b >> c;
cout << "Maximum is: " << maximum ( a, b, c ) << endl; // Function call
getch();
return 0;
}
int maximum( int x, int y, int z ) // function definition
{
int max = x;
if ( y > max )
max = y;
if ( z > max )
max = z;
return max;
}''')
    P(*OUT)
    code(t, '''Enter three integers: 4 -2 6
Maximum is: 6''')
    t.h('6.1.5 Scope of variables', '6.1.5 ویری ایبلز کا دائرہ', '۶.۱.۵ د متغیرونو ساحه')
    P('By the scope of a variable we mean that if a variable is defined in a program then in which parts of the same program this variable can be accessed. There are three scopes of variables.', 'ویری ایبل کے دائرے سے مراد یہ ہے کہ اگر کسی پروگرام میں ویری ایبل بیان کیا گیا ہو تو اسی پروگرام کے کن حصوں میں اس ویری ایبل تک رسائی ہو سکتی ہے۔ ویری ایبلز کے تین دائرے ہیں۔', 'د متغیر له ساحې موخه دا ده چې که یو متغیر په یوه پروګرام کې تعریف شي، د همغه پروګرام په کومو برخو کې دې متغیر ته لاسرسی کېدای شي. د متغیرونو درې ساحې دي.')
    t.group('list', [('Local scope', 'مقامی دائرہ', 'محلي ساحه'), ('Global scope', 'عالمی دائرہ', 'نړیواله ساحه'), ('Static scope', 'اسٹیٹک دائرہ', 'ثابته ساحه')])
    BOOK.save(98, [(6, rec(t, 5, 98, [184, 185, 186], 'The function-body brace and label beside the definition on p.184 are reproduced as text markers in the code listing. The list of scopes at the top of p.186 (PDF99) is given here.'))],
              issues=[{'id': 'cs12-pdf098', 'unit': 6, 'printedPage': 184,
                       'description': 'The whole function definition is printed “int maximum(int x. int y, int z)” with a full stop instead of a comma. Retained as printed.'}])


def p99():
    t = Builder()
    P = t.p
    t.h('a. Local/Automatic variables', 'a. مقامی/خودکار ویری ایبلز', 'a. محلي/خپلکاره متغیرونه')
    P('The variables defined within a block are called local variables and its scope is local to block. These variables are not accessible from outside the block and thus their visibility remains only to that block. For example, in the following code segment, the variables a, b and c are local variables and cannot be used outside this boundary.',
      'کسی بلاک کے اندر بیان کیے گئے ویری ایبلز مقامی ویری ایبلز کہلاتے ہیں اور ان کا دائرہ بلاک تک محدود ہوتا ہے۔ یہ ویری ایبلز بلاک کے باہر سے قابلِ رسائی نہیں ہوتے اور یوں ان کی نمائش صرف اسی بلاک تک رہتی ہے۔ مثلاً درج ذیل کوڈ کے حصے میں ویری ایبلز a، b اور c مقامی ویری ایبلز ہیں اور اس حد کے باہر استعمال نہیں ہو سکتے۔',
      'هغه متغیرونه چې د یوه بلاک دننه تعریف شي، محلي متغیرونه بلل کېږي او ساحه یې په بلاک پورې محدوده ده. دا متغیرونه له بلاک بهر د لاسرسي وړ نه دي او لیدل یې یوازې په همغه بلاک پورې پاتې کېږي. د بېلګې په توګه په لاندې کوډ کې a، b او c محلي متغیرونه دي او له دې پولې بهر نه شي کارېدای.')
    code(t, '''int main()
{
int a, b, c;
cout << "Enter three integers: ";
cin >> a >> b >> c;
// a, b and c are the local variables and cannot be used outside the {} block
cout << "Maximum is: " << maximum ( a, b, c ) << endl; getch();
return 0;
}''')
    P('It is impossible to use the variables x, y or z defined in maximum( ) function directly within main function because these variables are local to the maximum function.', 'maximum( ) فنکشن میں بیان کیے گئے ویری ایبلز x، y یا z کو main فنکشن میں براہِ راست استعمال کرنا ناممکن ہے کیونکہ یہ ویری ایبلز maximum فنکشن کے لیے مقامی ہیں۔', 'په maximum( ) فنکشن کې تعریف شوي x، y یا z متغیرونه په main فنکشن کې مستقیم کارول ناشوني دي ځکه دا متغیرونه د maximum فنکشن لپاره محلي دي.')
    P('The following program makes use of a function square() that has its own local variable ‘y’ which is not accessible in the main() function.', 'درج ذیل پروگرام فنکشن square() استعمال کرتا ہے جس کا اپنا مقامی ویری ایبل ‘y’ ہے جو main() فنکشن میں قابلِ رسائی نہیں۔', 'لاندې پروګرام square() فنکشن کاروي چې خپل محلي متغیر ‘y’ لري چې په main() فنکشن کې د لاسرسي وړ نه دی.')
    code(t, '''// local variables (example) to calculate square of integers
#include <iostream.h>
#include<conio.h>
int square( int y); // function prototype
int main()
{
for ( int x = 1; x <= 10; x++ )
cout << square( x ) << " ";
cout << endl;
getch();
return 0;
}
// Function definition
int square( int y )
{
return y * y;
}''')
    t.h('b. Global variables', 'b. عالمی ویری ایبلز', 'b. نړیوال متغیرونه')
    P('The variables defined usually at the top of a program before the main() function are called global variables. The variables declared globally are visible from any point of the code. They are accessible from inside and outside of all the functions of the same program. In order to declare global variables we simply have to declare the variable outside any function or block; i.e. directly in the body of the program.',
      'عموماً پروگرام کے شروع میں main() فنکشن سے پہلے بیان کیے گئے ویری ایبلز عالمی ویری ایبلز کہلاتے ہیں۔ عالمی طور پر ڈکلیئر کیے گئے ویری ایبلز کوڈ کے کسی بھی مقام سے نظر آتے ہیں۔ یہ اسی پروگرام کے تمام فنکشنز کے اندر اور باہر سے قابلِ رسائی ہوتے ہیں۔ عالمی ویری ایبلز ڈکلیئر کرنے کے لیے ہمیں بس ویری ایبل کو کسی فنکشن یا بلاک کے باہر یعنی براہِ راست پروگرام کے جسم میں ڈکلیئر کرنا ہوتا ہے۔',
      'هغه متغیرونه چې عموماً د پروګرام په سر کې د main() فنکشن مخکې تعریف شي، نړیوال متغیرونه بلل کېږي. نړیوال اعلان شوي متغیرونه د کوډ له هر ځایه لیدل کېږي. د همغه پروګرام د ټولو فنکشنونو له دننه او بهر د لاسرسي وړ دي. د نړیوالو متغیرونو د اعلان لپاره یوازې باید متغیر له هر فنکشن یا بلاک بهر، یعنې مستقیم د پروګرام په بدنه کې، اعلان کړو.')
    P('The following program describes local and global variables.', 'درج ذیل پروگرام مقامی اور عالمی ویری ایبلز بیان کرتا ہے۔', 'لاندې پروګرام محلي او نړیوال متغیرونه بیانوي.')
    code(t, '''#include <iostream.h>
#include <conio.h>
int add(); /* function prototype */
int val1, val2, val3; /*These are global variables */
int add()
{
int sum; // here, sum is local variable
sum = val1 + val2 + val3;
return sum;
}
int main()
{
int total; //here, total is local variable
val1 = 10;
val2 = 20;
val3 = 30;
total = add();
cout<<"The sum of the three global variables="<<total;
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'The sum of the three global variables=60')
    BOOK.save(99, [(6, rec(t, 6, 99, [186, 187, 188], 'The list of scopes at the top of p.186 is recorded with PDF98. The global-variables program runs to p.188 (PDF100) and is given whole with its output. The book prints no output for the square() program.'))])


def p100():
    t = Builder()
    P = t.p
    P('In this example, the variables val1, val2, val3 are defined globally and can be accessed both in main() function and add() function without generating any error message. Here in the same program, the variables sum in function add() and total in function main() are local to the respective functions and are not visible outside the boundaries of these functions.',
      'اس مثال میں ویری ایبلز val1، val2، val3 عالمی طور پر بیان کیے گئے ہیں اور کسی خرابی کے پیغام کے بغیر main() فنکشن اور add() فنکشن دونوں میں قابلِ رسائی ہیں۔ یہاں اسی پروگرام میں فنکشن add() میں ویری ایبل sum اور فنکشن main() میں total اپنے اپنے فنکشنز کے لیے مقامی ہیں اور ان فنکشنز کی حدود کے باہر نظر نہیں آتے۔',
      'په دې بېلګه کې val1، val2، val3 متغیرونه نړیوال تعریف شوي او پرته له تېروتنې پیغامه په main() او add() دواړو فنکشنونو کې د لاسرسي وړ دي. دلته په همدې پروګرام کې د add() فنکشن متغیر sum او د main() فنکشن total په خپلو فنکشنونو پورې محلي دي او د دې فنکشنونو له پولو بهر نه لیدل کېږي.')
    t.h('c. Static variables', 'c. اسٹیٹک ویری ایبلز', 'c. ثابت متغیرونه')
    P('Static variables are those variables which are preceded by the keyword static while declaring. For example:', 'اسٹیٹک ویری ایبلز وہ ویری ایبلز ہیں جن سے ڈکلیئر کرتے وقت کلیدی لفظ static پہلے لکھا جاتا ہے۔ مثلاً:', 'ثابت متغیرونه هغه متغیرونه دي چې د اعلان پر مهال ورته static کلیدي کلمه مخکې لیکل کېږي. د بېلګې په توګه:')
    code(t, 'static Static_Var;')
    P('Static variables are initialized once in the program and remains in memory until the end of the program. These variables have the capability to preserve information about the last value a function returned, until the program completely ends. Static variables are local in scope to their module or function in which they are defined, but life is throughout the program.',
      'اسٹیٹک ویری ایبلز کو پروگرام میں ایک بار ابتدائی قدر دی جاتی ہے اور یہ پروگرام کے اختتام تک میموری میں رہتے ہیں۔ یہ ویری ایبلز فنکشن کی واپس کی گئی آخری قدر کے بارے میں معلومات پروگرام کے مکمل ختم ہونے تک محفوظ رکھنے کی صلاحیت رکھتے ہیں۔ اسٹیٹک ویری ایبلز کا دائرہ اس ماڈیول یا فنکشن تک مقامی ہوتا ہے جس میں وہ بیان کیے گئے ہوں، لیکن ان کی زندگی پورے پروگرام تک ہوتی ہے۔',
      'ثابت متغیرونو ته په پروګرام کې یو ځل لومړنی ارزښت ورکول کېږي او د پروګرام تر پایه په حافظه کې پاتې کېږي. دا متغیرونه وړتیا لري چې د فنکشن د وروستي بېرته ورکړل شوي ارزښت معلومات د پروګرام تر بشپړ پای ساتي. ثابت متغیرونه په ساحه کې په هغه ماډیول یا فنکشن پورې محلي دي چې پکې تعریف شوي، خو ژوند یې د ټول پروګرام په اوږدو کې دی.')
    P('Consider the following example to demonstrate the use of static variables.', 'اسٹیٹک ویری ایبلز کا استعمال واضح کرنے کے لیے درج ذیل مثال پر غور کریں۔', 'د ثابتو متغیرونو د کارونې د ښودلو لپاره لاندې بېلګې ته پام وکړئ.')
    code(t, '''/* static and automatic variables program*/
#include <conio.h>
#include <iostream.h>
void demo(){
auto int Auto_Var = 0; // automatic variable
static int Static_Var = 0; // static variable
cout<<"Auto ="<<Auto_Var<< ","<< "Static="<<Static_Var<<endl;
++ Auto_Var; ++ Static_Var; }
int main()
{
int i=0;
while( i < 3 )
{ demo(); i++; }
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Auto = 0, Static = 0
Auto = 0, Static = 1
Auto = 0, Static = 2''')
    BOOK.save(100, [(6, rec(t, 7, 100, [188, 189], 'The top of p.188 (end of the global-variables program and its output) is recorded with PDF99.'))],
              issues=[{'id': 'cs12-pdf100', 'unit': 6, 'printedPage': 188,
                       'description': 'The example declaration “static Static_Var;” omits a data type; p.189 “Static variables are initialized once … and remains in memory”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 98
    {98: p98, 99: p99, 100: p100}[n]()
