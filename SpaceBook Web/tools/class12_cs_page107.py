"""Computer Science XII PDF107–111: pp.202–211 — default arguments program, 6.2.3 return statement, 6.3 function overloading (display, multiply),
6.3.2 advantages, 6.3.3 concept: a. number (Addition), b. data types (print), c. return type; Unit 6 summary (pp.210–211).
Run: python class12_cs_page107.py N (107–111)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u6-text-{n}', f'Unit 6 text ({n})', f'یونٹ 6 — متن ({n})', f'۶ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p107():
    t = Builder()
    P = t.p
    P('The following program demonstrates the concept of default arguments.', 'درج ذیل پروگرام ڈیفالٹ آرگیومنٹس کا تصور واضح کرتا ہے۔', 'لاندې پروګرام د ډیفالټ دلیلونو مفهوم ښيي.')
    code(t, '''#include <iostream.h>
#include<conio.h>
int divide (int a, int b=2)
{
int r;
r=a/b;
return (r);
}
int main()
{
cout<<“Result by providing one argument="
<< divide (12); // function call with one arguments
cout<< endl;
cout<<“Result by providing both the
arguments=" <<divide (20,4);
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Result by providing one argument=6
Result by providing both the arguments=5''')
    P('As we can see in the body of the program there are two calls to function divide(). In the first one, we have only passed one argument, but the function divide() gets the second value from the default argument, int b=2, in the function prototype and thus results is 6.',
      'جیسا کہ ہم پروگرام کے جسم میں دیکھ سکتے ہیں، فنکشن divide() کو دو کالز ہیں۔ پہلی میں ہم نے صرف ایک آرگیومنٹ پاس کیا ہے، لیکن فنکشن divide() دوسری قدر فنکشن پروٹوٹائپ میں ڈیفالٹ آرگیومنٹ int b=2 سے لیتا ہے اور یوں نتیجہ 6 آتا ہے۔',
      'لکه څنګه چې د پروګرام په بدنه کې وینو، divide() فنکشن ته دوه غوښتنې دي. په لومړۍ کې موږ یوازې یو دلیل لېږدولی، خو divide() فنکشن دویم ارزښت د فنکشن په نمونه کې له ډیفالټ دلیل int b=2 اخلي او پایله 6 کېږي.')
    P('In the second call, there are two parameters passed, so the default value for b is ignored and b takes the value passed as argument, that is 4, making the result returned equal to 5.',
      'دوسری کال میں دو پیرامیٹرز پاس کیے گئے ہیں، اس لیے b کی ڈیفالٹ قدر نظر انداز ہو جاتی ہے اور b آرگیومنٹ کے طور پر پاس کی گئی قدر یعنی 4 لیتا ہے، جس سے واپس آنے والا نتیجہ 5 کے برابر ہوتا ہے۔',
      'په دویمه غوښتنه کې دوه پاراميټرونه لېږدول شوي، نو د b ډیفالټ ارزښت له پامه غورځول کېږي او b د دلیل په توګه لېږدول شوی ارزښت یعنې 4 اخلي، او بېرته ورکړل شوې پایله 5 کېږي.')
    t.h('6.2.3 return statement', '6.2.3 return بیان', '۶.۲.۳ return بیان')
    P('If the return type of a function is any valid data type such as int, long, float, double, long double or char then return statement should be used in the function body to return the result to the calling program.',
      'اگر فنکشن کی ریٹرن ٹائپ کوئی درست ڈیٹا ٹائپ ہو جیسے int، long، float، double، long double یا char تو کال کرنے والے پروگرام کو نتیجہ واپس کرنے کے لیے فنکشن کے جسم میں return بیان استعمال ہونا چاہیے۔',
      'که د فنکشن د بېرته ورکړې ډول هر سم ډېټا ډول وي لکه int، long، float، double، long double یا char، نو غوښتونکي پروګرام ته د پایلې د بېرته ورکولو لپاره باید د فنکشن په بدنه کې return بیان وکارول شي.')
    P('The general syntax of the use of return statement is given below.', 'return بیان کے استعمال کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے۔', 'د return بیان د کارونې عمومي بڼه لاندې ورکړل شوې.')
    code(t, 'return (expression or variable holding results or constant);')
    P('Consider the following function:', 'درج ذیل فنکشن پر غور کریں:', 'لاندې فنکشن ته پام وکړئ:')
    code(t, '''// the use of return statement in the cube() function
int cube(int x)
{
int c;
c= x*x*x;
return c; // or return (c);
}''')
    P('If a function returns a value by the use of return statement then the call to the function should be from a statement or an expression that utilizes it.', 'اگر فنکشن return بیان کے ذریعے قدر واپس کرے تو فنکشن کی کال ایسے بیان یا ایکسپریشن سے ہونی چاہیے جو اسے استعمال کرے۔', 'که یو فنکشن د return بیان په مرسته ارزښت بېرته ورکړي، نو فنکشن ته غوښتنه باید له داسې بیان یا افادې وي چې هغه وکاروي.')
    P('For example:', 'مثال کے طور پر:', 'د بېلګې په توګه:')
    code(t, '''cout<<cube(x);
int y=cube(x);''')
    BOOK.save(107, [(6, rec(t, 14, 107, [202, 203, 204], 'The second example call at the top of p.204 (PDF108) is given here with the first.'))],
              issues=[{'id': 'cs12-pdf107', 'unit': 6, 'printedPage': 202,
                       'description': 'The divide() program opens its strings with curly quotes (“Result …") and breaks a string across lines; comment “with one arguments”; “thus results is 6”. Retained as printed.'}])


def p108():
    t = Builder()
    P = t.p
    t.h('6.3 Function overloading', '6.3 فنکشن اوورلوڈنگ', '۶.۳ د فنکشن ډېرول (overloading)')
    t.h('6.3.1 Definition', '6.3.1 تعریف', '۶.۳.۱ تعریف')
    P('In programming languages, two or more variables or functions with the same name cannot be used in a single program or block of code. Function overloading is a feature of C++ that allows us to create multiple functions with the same name, so long as they have different number or types of parameters.',
      'پروگرامنگ زبانوں میں ایک ہی نام کے دو یا زیادہ ویری ایبلز یا فنکشنز ایک پروگرام یا کوڈ کے بلاک میں استعمال نہیں ہو سکتے۔ فنکشن اوورلوڈنگ C++ کی ایک خصوصیت ہے جو ہمیں ایک ہی نام کے متعدد فنکشنز بنانے دیتی ہے، بشرطیکہ ان کے پیرامیٹرز کی تعداد یا اقسام مختلف ہوں۔',
      'په پروګرامي ژبو کې د یو نوم دوه یا ډېر متغیرونه یا فنکشنونه په یوه پروګرام یا د کوډ په یوه بلاک کې نه شي کارېدای. د فنکشن ډېرول د C++ ځانګړتیا ده چې موږ ته اجازه راکوي د یو نوم څو فنکشنونه جوړ کړو، تر هغه چې د پاراميټرونو شمېر یا ډولونه یې بېل وي.')
    P('Consider the following example having two functions with the same name display used to perform slightly different tasks in over loaded form.', 'درج ذیل مثال پر غور کریں جس میں display نام کے دو فنکشنز ہیں جو اوورلوڈ شکل میں قدرے مختلف کام انجام دیتے ہیں۔', 'لاندې بېلګې ته پام وکړئ چې د display په نوم دوه فنکشنونه لري چې په ډېر شوي (overloaded) بڼه یو څه بېلې دندې ترسره کوي.')
    code(t, '''#include <iostream.h>
#include<conio.h>
void display (int a)
{
cout<<a;
}
void display()
{
cout<< “Welcome”<<endl;
}
int main()
{
display() ;
display(55) ;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Welcome
55''')
    P('Here, the function display is overloaded with two tasks: one for displaying an integer value and the other for displaying a welcome message. While calling the overloaded functions, the compiler decides at run time that which display function should be called. To determine which display to call is decided by looking at the number and types of the arguments or parameters of the functions. In this example, void display () is called for display () and void display (int a) for display (55).',
      'یہاں فنکشن display دو کاموں کے ساتھ اوورلوڈ کیا گیا ہے: ایک صحیح قدر دکھانے کے لیے اور دوسرا خوش آمدیدی پیغام دکھانے کے لیے۔ اوورلوڈ فنکشنز کال کرتے وقت کمپائلر رن ٹائم پر فیصلہ کرتا ہے کہ کون سا display فنکشن کال کیا جائے۔ کون سا display کال کرنا ہے یہ فنکشنز کے آرگیومنٹس یا پیرامیٹرز کی تعداد اور اقسام دیکھ کر طے ہوتا ہے۔ اس مثال میں display () کے لیے void display () اور display (55) کے لیے void display (int a) کال ہوتا ہے۔',
      'دلته display فنکشن په دوو دندو ډېر شوی: یوه د صحیح ارزښت د ښودلو لپاره او بله د ښه راغلاست پیغام د ښودلو لپاره. د ډېر شویو فنکشنونو د غوښتلو پر مهال کمپایلر د اجرا پر مهال پرېکړه کوي چې کوم display فنکشن وغوښتل شي. دا چې کوم display وغوښتل شي، د فنکشنونو د دلیلونو یا پاراميټرونو د شمېر او ډولونو په کتلو ټاکل کېږي. په دې بېلګه کې د display () لپاره void display () او د display (55) لپاره void display (int a) غوښتل کېږي.')
    P('Consider another program having two functions with the same name multiply that operate on integers and floating points numbers.', 'ایک اور پروگرام پر غور کریں جس میں multiply نام کے دو فنکشنز ہیں جو صحیح اعداد اور فلوٹنگ پوائنٹ اعداد پر کام کرتے ہیں۔', 'بل پروګرام ته پام وکړئ چې د multiply په نوم دوه فنکشنونه لري چې پر صحیح او اعشاري عددونو کار کوي.')
    code(t, '''#include <iostream.h>
#include<conio.h>
int multiply (int a, int b)
{
return (a*b);
}
float multiply (float a, float b)
{
return (a*b);
}
int main()
{
cout << “Output of integers="<< multiply (5, 33)<<endl;
cout << “Output of floats="<< multiply (2.1, 3.0);
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Output of integers=165
Output of floats=6.3''')
    BOOK.save(108, [(6, rec(t, 15, 108, [204, 205, 206], 'The int y=cube(x); line at the top of p.204 is recorded with PDF107. The multiply program ends on p.206 (PDF109) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf108', 'unit': 6, 'printedPage': 205,
                       'description': 'p.205 says the compiler decides “at run time” (overload resolution is at compile time); “over loaded form”; curly opening quotes in the listings; multiply (2.1, 3.0) passes double literals. Retained as printed.'}])


def p109():
    t = Builder()
    P = t.p
    P('In this case, we have defined two functions with the same name, multiply, that accept two arguments. One accepts two arguments of type int and the second of type float. The compiler looks at the arguments and calls the respective function. Here, multiply (int a, int b) is called for multiply (5, 33) because the arguments match with the data types of the formal parameters. Similarly, multiply (float a, float b) is called for the call multiply (2.1, 3.0) because the arguments and formal parameters match each other in types.',
      'اس صورت میں ہم نے ایک ہی نام multiply کے دو فنکشنز بیان کیے ہیں جو دو آرگیومنٹس لیتے ہیں۔ ایک int قسم کے دو آرگیومنٹس لیتا ہے اور دوسرا float قسم کے۔ کمپائلر آرگیومنٹس دیکھ کر متعلقہ فنکشن کال کرتا ہے۔ یہاں multiply (5, 33) کے لیے multiply (int a, int b) کال ہوتا ہے کیونکہ آرگیومنٹس رسمی پیرامیٹرز کی ڈیٹا ٹائپس سے ملتے ہیں۔ اسی طرح کال multiply (2.1, 3.0) کے لیے multiply (float a, float b) کال ہوتا ہے کیونکہ آرگیومنٹس اور رسمی پیرامیٹرز کی اقسام آپس میں ملتی ہیں۔',
      'په دې حالت کې موږ د یو نوم multiply دوه فنکشنونه تعریف کړي چې دوه دلیلونه مني. یو د int ډول دوه دلیلونه مني او دویم د float ډول. کمپایلر دلیلونو ته ګوري او اړوند فنکشن غواړي. دلته د multiply (5, 33) لپاره multiply (int a, int b) غوښتل کېږي ځکه دلیلونه د رسمي پاراميټرونو له ډېټا ډولونو سره سمون لري. همداراز د multiply (2.1, 3.0) غوښتنې لپاره multiply (float a, float b) غوښتل کېږي ځکه دلیلونه او رسمي پاراميټرونه په ډولونو کې سره سمون لري.')
    t.h('6.3.2 Advantages of function overloading', '6.3.2 فنکشن اوورلوڈنگ کے فوائد', '۶.۳.۲ د فنکشن ډېرولو ګټې')
    t.group('list', [
     ('Function overloading can significantly reduce complexity of programs.', 'فنکشن اوورلوڈنگ پروگراموں کی پیچیدگی نمایاں طور پر کم کر سکتی ہے۔', 'د فنکشن ډېرول د پروګرامونو پېچلتیا د پام وړ کمولی شي.'),
     ('Using function overloading, we can declare multiple functions with the same name that have slightly different purposes.', 'فنکشن اوورلوڈنگ کے ذریعے ہم ایک ہی نام کے متعدد فنکشنز ڈکلیئر کر سکتے ہیں جن کے مقاصد قدرے مختلف ہوں۔', 'د فنکشن ډېرولو په مرسته کولی شو د یو نوم څو فنکشنونه اعلان کړو چې یو څه بېلې موخې لري.'),
     ('As multiple functions have same name, therefore, remembering them is easier as compared to remembering more names.', 'چونکہ متعدد فنکشنز کا نام ایک ہے، اس لیے انھیں یاد رکھنا زیادہ ناموں کو یاد رکھنے کے مقابلے میں آسان ہے۔', 'څرنګه چې څو فنکشنونه یو نوم لري، نو یادول یې د ډېرو نومونو له یادولو اسانه دي.'),
     ('It increases the readability of programs.', 'یہ پروگراموں کی پڑھنے میں آسانی بڑھاتی ہے۔', 'دا د پروګرامونو لوستل اسانوي.'),
     ('It exhibits the behavior of polymorphism.', 'یہ پولی مورفزم کا رویہ ظاہر کرتی ہے۔', 'دا د پولي‌مورفیزم چلند ښيي.')])
    t.h('6.3.3 Understanding function overloading concept', '6.3.3 فنکشن اوورلوڈنگ کے تصور کو سمجھنا', '۶.۳.۳ د فنکشن ډېرولو مفهوم پوهېدل')
    P('For the complete understanding of the concept of function overloading, one should know those features of the overloaded functions which disambiguate them and make them unique in a single program. These features are listed below:',
      'فنکشن اوورلوڈنگ کے تصور کو مکمل طور پر سمجھنے کے لیے اوورلوڈ فنکشنز کی وہ خصوصیات جاننی چاہییں جو انھیں ایک دوسرے سے ممیز کرتی ہیں اور ایک پروگرام میں منفرد بناتی ہیں۔ یہ خصوصیات ذیل میں درج ہیں:',
      'د فنکشن ډېرولو د مفهوم د بشپړ پوهېدو لپاره باید د ډېر شویو فنکشنونو هغه ځانګړتیاوې وپېژنو چې یو له بله یې جلا کوي او په یوه پروګرام کې یې ځانګړي کوي. دا ځانګړتیاوې لاندې دي:')
    t.group('list', [('Number of arguments', 'آرگیومنٹس کی تعداد', 'د دلیلونو شمېر'), ('Data types of arguments', 'آرگیومنٹس کی ڈیٹا ٹائپس', 'د دلیلونو ډېټا ډولونه'), ('Return type', 'ریٹرن ٹائپ', 'د بېرته ورکړې ډول')])
    t.h('a. Number of arguments', 'a. آرگیومنٹس کی تعداد', 'a. د دلیلونو شمېر')
    P('Functions can be overloaded if they have different numbers of parameters. More than one functions with the same name but different number of parameters can be used in a single program. In the calls to these functions, the compiler disambiguates the calls by looking at the number of arguments and formal parameters in the function decelerators. Consider the following example:',
      'فنکشنز اوورلوڈ کیے جا سکتے ہیں اگر ان کے پیرامیٹرز کی تعداد مختلف ہو۔ ایک ہی نام لیکن مختلف تعداد کے پیرامیٹرز والے ایک سے زیادہ فنکشنز ایک پروگرام میں استعمال ہو سکتے ہیں۔ ان فنکشنز کی کالز میں کمپائلر فنکشن ڈکلیریٹرز میں آرگیومنٹس اور رسمی پیرامیٹرز کی تعداد دیکھ کر کالز میں امتیاز کرتا ہے۔ درج ذیل مثال پر غور کریں:',
      'فنکشنونه ډېرېدای شي که د پاراميټرونو شمېر یې بېل وي. د یو نوم خو د بېل شمېر پاراميټرونو له یوه ډېر فنکشنونه په یوه پروګرام کې کارېدای شي. دې فنکشنونو ته په غوښتنو کې کمپایلر د فنکشن په اعلانوونکو کې د دلیلونو او رسمي پاراميټرونو شمېر ته په کتلو غوښتنې جلا کوي. لاندې بېلګې ته پام وکړئ:')
    code(t, '''/* overloaded functions with different number of parameters */
#include <iostream.h>
#include <conio.h>
int Addition(int X, int Y)
{
return (X + Y);
}
int Addition(int X, int Y, int Z)
{
return (X + Y + Z);
}
int main()
{
int a=55, b=22, c=100;
cout << “Output of 2 integers="<<Addition (a,b);
cout << endl;
cout << “Output of 3 integers="<<Addition (a,b,c);
cout << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Output of 2 integers=77
Output of 3 integers=177''')
    BOOK.save(109, [(6, rec(t, 16, 109, [206, 207, 208], 'The top of p.206 (end of the multiply program and its output) is recorded with PDF108. The Addition program ends on p.208 (PDF110) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf109', 'unit': 6, 'printedPage': 207,
                       'description': 'p.207 “function decelerators” (for declarators); “More than one functions”; p.206 “that accept two arguments”. Retained as printed.'}])


def p110():
    t = Builder()
    P = t.p
    P('In this example, two functions have been used with the name Addition. One has two parameters and the second has three parameters. In the main() function there are two calls Addition (a,b) and Addition (a,b,c) which call functions int Addition(int X, int Y) and int Addition(int X, int Y, int Z) respectively by looking at the number of parameters.',
      'اس مثال میں Addition نام کے دو فنکشنز استعمال ہوئے ہیں۔ ایک کے دو پیرامیٹرز ہیں اور دوسرے کے تین۔ main() فنکشن میں دو کالز Addition (a,b) اور Addition (a,b,c) ہیں جو پیرامیٹرز کی تعداد دیکھ کر بالترتیب فنکشنز int Addition(int X, int Y) اور int Addition(int X, int Y, int Z) کو کال کرتی ہیں۔',
      'په دې بېلګه کې د Addition په نوم دوه فنکشنونه کارول شوي. یو دوه پاراميټرونه لري او دویم درې. په main() فنکشن کې دوه غوښتنې Addition (a,b) او Addition (a,b,c) دي چې د پاراميټرونو شمېر ته په کتلو په ترتیب سره int Addition(int X, int Y) او int Addition(int X, int Y, int Z) فنکشنونه غواړي.')
    t.h('b. Data types of arguments', 'b. آرگیومنٹس کی ڈیٹا ٹائپس', 'b. د دلیلونو ډېټا ډولونه')
    P('One way to achieve function overloading is to define multiple functions with the same name but different types of parameters. Consider the following example:', 'فنکشن اوورلوڈنگ حاصل کرنے کا ایک طریقہ یہ ہے کہ ایک ہی نام لیکن مختلف اقسام کے پیرامیٹرز والے متعدد فنکشنز بیان کیے جائیں۔ درج ذیل مثال پر غور کریں:', 'د فنکشن ډېرولو یوه لاره دا ده چې د یو نوم خو د بېلو ډولونو پاراميټرونو څو فنکشنونه تعریف شي. لاندې بېلګې ته پام وکړئ:')
    code(t, '''/*overloaded functions print()with different types of
parameters*/
#include <iostream.h>
#include <conio.h>
void print (int X)
{
cout<< “X="<<X<<endl;
}
void print (float Y)
{
cout<< “Y="<<Y<<endl;
}
int main()
{
print(55);
print(33.66);
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''X=55
Y=33.66''')
    P('Here, two functions, print (int X) and print (float Y), have been used with different types of parameters, int and float. In main() function, two calls are used print(55) and print(33.66). The compiler looks at the type of arguments and calls the corresponding function.',
      'یہاں دو فنکشنز print (int X) اور print (float Y) مختلف اقسام کے پیرامیٹرز int اور float کے ساتھ استعمال ہوئے ہیں۔ main() فنکشن میں دو کالز print(55) اور print(33.66) استعمال ہوئی ہیں۔ کمپائلر آرگیومنٹس کی قسم دیکھ کر متعلقہ فنکشن کال کرتا ہے۔',
      'دلته دوه فنکشنونه print (int X) او print (float Y) د بېلو ډولونو پاراميټرونو int او float سره کارول شوي. په main() فنکشن کې دوه غوښتنې print(55) او print(33.66) کارول شوې. کمپایلر د دلیلونو ډول ته ګوري او اړوند فنکشن غواړي.')
    t.h('c. Return type', 'c. ریٹرن ٹائپ', 'c. د بېرته ورکړې ډول')
    P('The return type of a function is not considered when functions are overloaded. It means that if two or more functions with the same name have same function signatures but different return types then they are not considered as overloaded and the compiler will generate error message.',
      'فنکشنز اوورلوڈ کرتے وقت فنکشن کی ریٹرن ٹائپ پر غور نہیں کیا جاتا۔ اس کا مطلب ہے کہ اگر ایک ہی نام کے دو یا زیادہ فنکشنز کے فنکشن سگنیچر ایک جیسے لیکن ریٹرن ٹائپس مختلف ہوں تو انھیں اوورلوڈ نہیں سمجھا جاتا اور کمپائلر خرابی کا پیغام دے گا۔',
      'کله چې فنکشنونه ډېرېږي، د فنکشن د بېرته ورکړې ډول ته پام نه کېږي. معنا دا چې که د یو نوم دوه یا ډېر فنکشنونه ورته لاسلیکونه خو بېل د بېرته ورکړې ډولونه ولري، ډېر شوي نه ګڼل کېږي او کمپایلر به د تېروتنې پیغام ورکړي.')
    P('Consider the following case:', 'درج ذیل صورت پر غور کریں:', 'لاندې حالت ته پام وکړئ:')
    code(t, '''int display();
double display(); // This prototype generates error message''')
    P('Consider another example:', 'ایک اور مثال پر غور کریں:', 'بلې بېلګې ته پام وکړئ:')
    code(t, '''int RandomNumber();
double RandomNumber(); // This prototype generates error message''')
    P('Here, the compiler generates an error message of re-declaration for the second declaration at line number 2. It is because that both the declarations have same number of parameters (zero in this case) but only the return types are different which do not play any role in the overloading. If we want to do it, for then, these functions will need to be given different names.',
      'یہاں کمپائلر لائن نمبر 2 پر دوسری ڈکلیریشن کے لیے دوبارہ ڈکلیریشن کی خرابی کا پیغام دیتا ہے۔ اس کی وجہ یہ ہے کہ دونوں ڈکلیریشنز میں پیرامیٹرز کی تعداد ایک ہے (اس صورت میں صفر) لیکن صرف ریٹرن ٹائپس مختلف ہیں جو اوورلوڈنگ میں کوئی کردار ادا نہیں کرتیں۔ اگر ہم ایسا کرنا چاہیں تو ان فنکشنز کو مختلف نام دینے ہوں گے۔',
      'دلته کمپایلر په ۲ کرښه کې د دویم اعلان لپاره د بیا اعلان د تېروتنې پیغام ورکوي. لامل یې دا دی چې دواړه اعلانونه د پاراميټرونو یو شمېر لري (په دې حالت کې صفر) خو یوازې د بېرته ورکړې ډولونه بېل دي چې په ډېرولو کې هېڅ رول نه لري. که دا کار وغواړو، دې فنکشنونو ته به بېل نومونه ورکول اړین وي.')
    BOOK.save(110, [(6, rec(t, 17, 110, [208, 209], 'The top of p.208 (end of the Addition program and its output) is recorded with PDF109.'))],
              issues=[{'id': 'cs12-pdf110', 'unit': 6, 'printedPage': 209,
                       'description': 'print(33.66) passes a double literal, which is ambiguous between print(int) and print(float) in standard C++; “It is because that both”, “If we want to do it, for then”. Retained as printed.'}])


def p111():
    s = Builder()
    s.h('Summary', 'خلاصہ', 'لنډیز')
    s.group('list', [
     ('A function is a self-contained program that performs a specific task.', 'فنکشن ایک خود مختار پروگرام ہے جو ایک مخصوص کام انجام دیتا ہے۔', 'فنکشن یو ځان‌بسیا پروګرام دی چې یوه ځانګړې دنده ترسره کوي.'),
     ('C++ has two types of functions, built-in and user-defined. Built-in functions are specific in their activities and cannot be used for general type of tasks.', 'C++ میں دو قسم کے فنکشنز ہیں، بلٹ اِن اور یوزر ڈیفائنڈ۔ بلٹ اِن فنکشنز اپنی سرگرمیوں میں مخصوص ہیں اور عمومی قسم کے کاموں کے لیے استعمال نہیں ہو سکتے۔', 'C++ دوه ډوله فنکشنونه لري، جوړ شوي او د کاروونکي-تعریف شوي. جوړ شوي فنکشنونه په خپلو کړنو کې ځانګړي دي او د عمومي ډول دندو لپاره نه شي کارېدای.'),
     ('Every C++ program comprise of one function called main (). It is the point from where the compiler starts the execution of every C++ program.', 'ہر C++ پروگرام main () نامی ایک فنکشن پر مشتمل ہوتا ہے۔ یہ وہ مقام ہے جہاں سے کمپائلر ہر C++ پروگرام کا عمل شروع کرتا ہے۔', 'هر C++ پروګرام د main () په نوم یو فنکشن لري. دا هغه ټکی دی چې کمپایلر له هغه ځایه د هر C++ پروګرام اجرا پیلوي.'),
     ('A good C++ programmer writes programs that comprise of small functions.', 'ایک اچھا C++ پروگرامر ایسے پروگرام لکھتا ہے جو چھوٹے فنکشنز پر مشتمل ہوں۔', 'ښه C++ پروګرام جوړوونکی داسې پروګرامونه لیکي چې له وړو فنکشنونو جوړ وي.'),
     ('Functions are one of the main building blocks of C++ programs. It modularizes large programs into segments and thus increase the program readability and also provides the facility of code reusability.', 'فنکشنز C++ پروگراموں کے بنیادی اجزا میں سے ایک ہیں۔ یہ بڑے پروگراموں کو حصوں میں تقسیم کرتے ہیں اور یوں پروگرام کی پڑھنے میں آسانی بڑھاتے ہیں اور کوڈ کے دوبارہ استعمال کی سہولت بھی دیتے ہیں۔', 'فنکشنونه د C++ پروګرامونو له اصلي جوړوونکو برخو یو دي. لوی پروګرامونه په برخو وېشي او په دې توګه د پروګرام لوستل اسانوي او د کوډ د بیا کارونې اسانتیا هم برابروي.'),
     ('Each function has its own name and when the function is called the execution of the program branches to the body of that function. When the function is finished, execution returns to the area of the program code from which it was called, and the program continues on to the next line of code.', 'ہر فنکشن کا اپنا نام ہوتا ہے اور جب فنکشن کال کیا جائے تو پروگرام کا عمل اس فنکشن کے جسم کی طرف شاخ بناتا ہے۔ فنکشن ختم ہونے پر عمل پروگرام کوڈ کے اس حصے کی طرف واپس آتا ہے جہاں سے اسے کال کیا گیا تھا اور پروگرام کوڈ کی اگلی لائن پر جاری رہتا ہے۔', 'هر فنکشن خپل نوم لري او کله چې فنکشن وغوښتل شي، د پروګرام اجرا د هغه فنکشن بدنې ته ځي. کله چې فنکشن پای ته ورسېږي، اجرا د پروګرام کوډ هغې سیمې ته ستنېږي چې له هغه ځایه غوښتل شوی و او پروګرام د کوډ راتلونکې کرښې ته دوام ورکوي.'),
     ('Function prototype tells the compiler the name of the function, number, types and order of parameters.', 'فنکشن پروٹوٹائپ کمپائلر کو فنکشن کا نام، پیرامیٹرز کی تعداد، اقسام اور ترتیب بتاتا ہے۔', 'د فنکشن نمونه کمپایلر ته د فنکشن نوم، د پاراميټرونو شمېر، ډولونه او ترتیب ښيي.'),
     ('A function definition is a set of instructions enclosed in a block which performs the intended task of the function.', 'فنکشن کی تعریف ایک بلاک میں بند ہدایات کا مجموعہ ہے جو فنکشن کا مطلوبہ کام انجام دیتا ہے۔', 'د فنکشن تعریف په یوه بلاک کې د تړلو لارښوونو ټولګه ده چې د فنکشن غوښتل شوې دنده ترسره کوي.'),
     ('Local/Automatic variables have local scope and can only be accessed in the block in which they are declared. These variables cannot be accessed from outside the block.', 'مقامی/خودکار ویری ایبلز کا دائرہ مقامی ہوتا ہے اور ان تک صرف اسی بلاک میں رسائی ہو سکتی ہے جس میں وہ ڈکلیئر کیے گئے ہوں۔ ان ویری ایبلز تک بلاک کے باہر سے رسائی نہیں ہو سکتی۔', 'محلي/خپلکاره متغیرونه محلي ساحه لري او یوازې په هغه بلاک کې چې اعلان شوي لاسرسی ورته کېدای شي. دې متغیرونو ته له بلاک بهر لاسرسی نه کېږي.'),
     ('Global variables have global access and their visibility is throughout the program in which they are defined.', 'عالمی ویری ایبلز کی رسائی عالمی ہوتی ہے اور ان کی نمائش اس پورے پروگرام میں ہوتی ہے جس میں وہ بیان کیے گئے ہوں۔', 'نړیوال متغیرونه نړیوال لاسرسی لري او په هغه ټول پروګرام کې لیدل کېږي چې پکې تعریف شوي.'),
     ('Static variables have scope of local variables and retain its values throughout the life of the program.', 'اسٹیٹک ویری ایبلز کا دائرہ مقامی ویری ایبلز جیسا ہوتا ہے اور یہ پروگرام کی پوری زندگی میں اپنی قدریں برقرار رکھتے ہیں۔', 'ثابت متغیرونه د محلي متغیرونو ساحه لري او د پروګرام د ټول ژوند په اوږدو کې خپل ارزښتونه ساتي.'),
     ('The variables that appear in the function prototype and function declaration are called formal parameters.', 'فنکشن پروٹوٹائپ اور فنکشن ڈکلیریشن میں آنے والے ویری ایبلز رسمی پیرامیٹرز کہلاتے ہیں۔', 'هغه متغیرونه چې د فنکشن په نمونه او د فنکشن په اعلان کې راځي، رسمي پاراميټرونه بلل کېږي.'),
     ('The variables in function calls that hold the values to be passed to the function are called actual parameters.', 'فنکشن کالز میں وہ ویری ایبلز جو فنکشن کو پاس کی جانے والی قدریں رکھتے ہیں، اصل پیرامیٹرز کہلاتے ہیں۔', 'د فنکشن په غوښتنو کې هغه متغیرونه چې فنکشن ته د لېږدول کېدونکو ارزښتونو ساتونکي دي، اصلي پاراميټرونه بلل کېږي.'),
     ('inline functions are special functions with inline keyword that are used to minimize the problem of function call overhead with the expenses of memory wastage.', 'inline فنکشنز inline کلیدی لفظ والے خاص فنکشنز ہیں جو میموری کے ضیاع کی قیمت پر فنکشن کال کے اضافی بوجھ کا مسئلہ کم کرنے کے لیے استعمال ہوتے ہیں۔', 'inline فنکشنونه د inline کلیدي کلمې سره ځانګړي فنکشنونه دي چې د حافظې د ضایع کېدو په بیه د فنکشن غوښتنې د اضافي بار ستونزې کمولو لپاره کارېږي.'),
     ('C++ provides the facility of calling a function with fewer arguments with the help of default arguments.', 'C++ ڈیفالٹ آرگیومنٹس کی مدد سے کم آرگیومنٹس کے ساتھ فنکشن کال کرنے کی سہولت فراہم کرتی ہے۔', 'C++ د ډیفالټ دلیلونو په مرسته د لږو دلیلونو سره د فنکشن د غوښتلو اسانتیا برابروي.'),
     ('The phenomenon of using same function name for related but slightly different tasks is called function overloading.', 'متعلقہ لیکن قدرے مختلف کاموں کے لیے ایک ہی فنکشن نام استعمال کرنے کا عمل فنکشن اوورلوڈنگ کہلاتا ہے۔', 'د اړوندو خو یو څه بېلو دندو لپاره د یو فنکشن نوم کارولو پدیده د فنکشن ډېرول بلل کېږي.'),
     ('In overloaded function, the function signature, number, types and order of arguments should be different from each other.', 'اوورلوڈ فنکشن میں فنکشن سگنیچر، آرگیومنٹس کی تعداد، اقسام اور ترتیب ایک دوسرے سے مختلف ہونی چاہیے۔', 'په ډېر شوي فنکشن کې د فنکشن لاسلیک، د دلیلونو شمېر، ډولونه او ترتیب باید یو له بله بېل وي.')])
    sm = BOOK.record(s, 'cs12-u6-summary', 'Unit 6 summary', 'یونٹ 6: خلاصہ', '۶ څپرکی: لنډیز', 111, [210, 211])
    BOOK.save(111, [(6, sm)], issues=[{'id': 'cs12-pdf111', 'unit': 6, 'printedPage': 210,
               'description': 'Summary: “Every C++ program comprise of”, “thus increase the program readability”, “retain its values”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 107
    {107: p107, 108: p108, 109: p109, 110: p110, 111: p111}[n]()
