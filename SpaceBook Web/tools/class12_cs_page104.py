"""Computer Science XII PDF104–106: pp.196–201 — displayGender program, b. passing by values (foo, addition), c. passing by reference (AddOne, duplicate),
multiple return values, 6.2.2 default arguments (begins).
Run: python class12_cs_page104.py N (104–106)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u6-text-{n}', f'Unit 6 text ({n})', f'یونٹ 6 — متن ({n})', f'۶ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p104():
    t = Builder()
    P = t.p
    P('In the above program, the function call, display (5), passes the constant argument (5) to the function.', 'اوپر کے پروگرام میں فنکشن کال display (5) مستقل آرگیومنٹ (5) فنکشن کو پاس کرتی ہے۔', 'په پورته پروګرام کې د display (5) فنکشن غوښتنه ثابت دلیل (5) فنکشن ته لېږدوي.')
    P('Consider another program defining a function displayGender () that takes a character constant, ‘F’ or ‘M’, as argument from the calling function:', 'ایک اور پروگرام پر غور کریں جو فنکشن displayGender () بیان کرتا ہے جو کال کرنے والے فنکشن سے حرفی مستقل ‘F’ یا ‘M’ بطور آرگیومنٹ لیتا ہے:', 'بل پروګرام ته پام وکړئ چې displayGender () فنکشن تعریفوي چې له غوښتونکي فنکشن د تورو ثابت ‘F’ یا ‘M’ د دلیل په توګه اخلي:')
    code(t, '''// passing character constants as argument
#include<iostream.h>
#include<conio.h>
void displayGender(char ch)
{
cout << "The gender marker you passed is : " << ch << endl;
}
int main()
{
displayGender(‘F’); // function call
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'The gender marker you passed is : F')
    t.h('b. Passing arguments by values', 'b. قدر کے ذریعے آرگیومنٹس پاس کرنا', 'b. د ارزښت له لارې د دلیلونو لېږدول')
    P('By default, arguments in C++ are passed by value. When arguments are passed by value, a copy of the argument value is passed to the function formal parameter.', 'بطورِ طے شدہ C++ میں آرگیومنٹس قدر کے ذریعے پاس ہوتے ہیں۔ جب آرگیومنٹس قدر کے ذریعے پاس ہوں تو آرگیومنٹ کی قدر کی نقل فنکشن کے رسمی پیرامیٹر کو پاس کی جاتی ہے۔', 'په ډیفالټ ډول په C++ کې دلیلونه د ارزښت له لارې لېږدول کېږي. کله چې دلیلونه د ارزښت له لارې ولېږدول شي، د دلیل د ارزښت کاپي د فنکشن رسمي پاراميټر ته لېږدول کېږي.')
    P('Consider the following program to demonstrate the use of passing arguments by value.', 'قدر کے ذریعے آرگیومنٹس پاس کرنے کا استعمال واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د ارزښت له لارې د دلیلونو د لېږدولو د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''// passing parameters by value
#include<iostream.h>
#include<conio.h>
void foo(int y)
{
cout << "y in foo() = " << y << endl;
y = 6;
cout << "y in foo() = " << y << endl;
} // y is destroyed here
int main()
{
int x = 5;
cout << "x in main() before call= " << x << endl;
foo(x); //argument passed by value
cout << "x in main() after call= " << x << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''x in main() before call=5
y in foo() = 5
y in foo() = 6
x in main() after call=5''')
    P('In this program, the original value of x is not changed before and after calling the function foo().', 'اس پروگرام میں فنکشن foo() کو کال کرنے سے پہلے اور بعد x کی اصل قدر تبدیل نہیں ہوتی۔', 'په دې پروګرام کې د foo() فنکشن له غوښتلو مخکې او وروسته د x اصلي ارزښت نه بدلېږي.')
    BOOK.save(104, [(6, rec(t, 11, 104, [196, 197], None))], issues=[{'id': 'cs12-pdf104', 'unit': 6, 'printedPage': 196,
               'description': 'p.196 refers to “display (5)” and “constant argument (5)” though the preceding program calls display(25); displayGender(‘F’) uses curly quotes. Retained as printed.'}])


def p105():
    t = Builder()
    P = t.p
    P('Consider another example that uses a function addition that gets arguments by values.', 'ایک اور مثال پر غور کریں جو فنکشن addition استعمال کرتی ہے جو قدر کے ذریعے آرگیومنٹس لیتا ہے۔', 'بلې بېلګې ته پام وکړئ چې addition فنکشن کاروي چې د ارزښت له لارې دلیلونه اخلي.')
    code(t, '''// passing parameters by value
#include <iostream.h>
#include <conio.h>
int addition (int a, int b)
{
int result;
result=a+b;
return (result);
}
int main()
{
int z, x=5, y=3;
z = addition (x, y); //arguments passed by value
cout << "The sum of both the values is =" << z;
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'The sum of both the values is =8')
    t.h('c. Passing arguments by reference', 'c. حوالے کے ذریعے آرگیومنٹس پاس کرنا', 'c. د حوالې له لارې د دلیلونو لېږدول')
    P('In pass by reference, the reference to the function parameters are passed as arguments rather than value of variables. Using pass by reference, the value of arguments can be changed within the function.', 'حوالے کے ذریعے پاس کرنے میں ویری ایبلز کی قدر کے بجائے فنکشن پیرامیٹرز کا حوالہ آرگیومنٹس کے طور پر پاس کیا جاتا ہے۔ حوالے کے ذریعے پاس کرنے سے آرگیومنٹس کی قدر فنکشن کے اندر تبدیل کی جا سکتی ہے۔', 'د حوالې له لارې لېږدولو کې د متغیرونو د ارزښت پر ځای د فنکشن پاراميټرونو ته حواله د دلیلونو په توګه لېږدول کېږي. د حوالې له لارې لېږدولو سره د دلیلونو ارزښت د فنکشن دننه بدلېدای شي.')
    P('In passing arguments by reference, the formal parameters should precede by the ampersand sign &. Consider the following example.', 'حوالے کے ذریعے آرگیومنٹس پاس کرنے میں رسمی پیرامیٹرز سے پہلے ایمپرسینڈ نشان & ہونا چاہیے۔ درج ذیل مثال پر غور کریں۔', 'د حوالې له لارې د دلیلونو په لېږدولو کې رسمي پاراميټرونو ته باید د امپرسنډ نښه & مخکې وي. لاندې بېلګې ته پام وکړئ.')
    code(t, '''#include<iostream.h>
#include<conio.h>
void AddOne(int &y)
{
y++; // changing values in function
}
int main()
{
int x = 55;
cout<<"x in main() before call= " << x << endl;
AddOne(x); //passing arguments by reference
cout<<"x in main() after call = " << x << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''x in main() before call= 55
x in main() after call = 56''')
    P('In the above example, the value of x is passed by reference and changed inside the function AddOne(). This change affects the values of x in main() because the formal argument &y in the function declarator is a reference to x and any change to y results in change in x.',
      'اوپر کی مثال میں x کی قدر حوالے کے ذریعے پاس کی گئی ہے اور فنکشن AddOne() کے اندر تبدیل کی گئی ہے۔ یہ تبدیلی main() میں x کی قدروں کو متاثر کرتی ہے کیونکہ فنکشن ڈکلیریٹر میں رسمی آرگیومنٹ &y، x کا حوالہ ہے اور y میں کوئی بھی تبدیلی x میں تبدیلی کا باعث بنتی ہے۔',
      'په پورته بېلګه کې د x ارزښت د حوالې له لارې لېږدول شوی او د AddOne() فنکشن دننه بدل شوی. دا بدلون په main() کې د x ارزښتونه اغېزمنوي ځکه د فنکشن په اعلانوونکي کې رسمي دلیل &y د x حواله ده او په y کې هر بدلون په x کې بدلون راولي.')
    BOOK.save(105, [(6, rec(t, 12, 105, [198, 199]))])


def p106():
    t = Builder()
    P = t.p
    P('Consider another example having a function named duplicate that receive arguments by reference:', 'ایک اور مثال پر غور کریں جس میں duplicate نامی فنکشن ہے جو حوالے کے ذریعے آرگیومنٹس لیتا ہے:', 'بلې بېلګې ته پام وکړئ چې duplicate په نوم فنکشن لري چې د حوالې له لارې دلیلونه اخلي:')
    code(t, '''#include <iostream.h>
#include<conio.h>
void duplicate (int& a, int& b, int& c)
{
a=a*2;
b=b*2;
c=c*2;
}
int main()
{
int x=1, y=3, z=7;
cout<<"values of x, y and z in main()before calling function\\n";
cout << "x=" << x << ", y=" << y << ", z=" << z<<endl;
duplicate (x, y, z);
cout<<"values of x, y and z in main() after calling function\\n";
cout << "x=" << x << ", y=" << y << ", z=" << z;
getch() ;
return 0;}''')
    P(*OUT)
    code(t, '''values of x, y and z in main()before calling function
x=1,y=3,z=7
values of x, y and z in main() after calling function
x=2, y=6, z=14''')
    P('Sometimes we need a function to return multiple values. However, functions can only return one value. One way to return multiple values is the use of the method of passing arguments by reference.', 'بعض اوقات ہمیں فنکشن سے متعدد قدریں واپس لینے کی ضرورت ہوتی ہے۔ تاہم فنکشنز صرف ایک قدر واپس کر سکتے ہیں۔ متعدد قدریں واپس کرنے کا ایک طریقہ حوالے کے ذریعے آرگیومنٹس پاس کرنے کا استعمال ہے۔', 'کله کله موږ اړتیا لرو چې یو فنکشن څو ارزښتونه بېرته ورکړي. خو فنکشنونه یوازې یو ارزښت بېرته ورکولی شي. د څو ارزښتونو د بېرته ورکولو یوه لاره د حوالې له لارې د دلیلونو د لېږدولو کارونه ده.')
    P('Passing arguments by this method allow programmers to change the value of the arguments, which is sometimes useful. Similarly, it is a fast approach to passing and processing values in a function and also has the facility of returning multiple values from a function.',
      'اس طریقے سے آرگیومنٹس پاس کرنا پروگرامرز کو آرگیومنٹس کی قدر تبدیل کرنے کی اجازت دیتا ہے، جو بعض اوقات مفید ہوتا ہے۔ اسی طرح یہ فنکشن میں قدریں پاس کرنے اور ان پر عمل کرنے کا تیز طریقہ ہے اور فنکشن سے متعدد قدریں واپس کرنے کی سہولت بھی رکھتا ہے۔',
      'په دې لاره د دلیلونو لېږدول پروګرام جوړوونکو ته اجازه ورکوي چې د دلیلونو ارزښت بدل کړي، چې کله کله ګټور وي. همداراز په فنکشن کې د ارزښتونو د لېږدولو او پروسس کولو چټکه لاره ده او له فنکشن د څو ارزښتونو د بېرته ورکولو اسانتیا هم لري.')
    t.h('6.2.2 Default arguments', '6.2.2 ڈیفالٹ آرگیومنٹس', '۶.۲.۲ ډیفالټ دلیلونه')
    P('When declaring a function we can specify a default value for each of the last parameters. This value will be used if the corresponding argument is left blank when calling to the function. To do this, we simply have to use the assignment operator and a value for the arguments in the function declaration. If a value for that parameter is not passed when the function is called, the default value is used, but if a value is specified this default value is ignored and the passed value is used instead.',
      'فنکشن ڈکلیئر کرتے وقت ہم آخری پیرامیٹرز میں سے ہر ایک کے لیے ڈیفالٹ قدر مقرر کر سکتے ہیں۔ یہ قدر اس وقت استعمال ہوگی جب فنکشن کال کرتے ہوئے متعلقہ آرگیومنٹ خالی چھوڑ دیا جائے۔ اس کے لیے ہمیں بس فنکشن ڈکلیریشن میں آرگیومنٹس کے لیے اسائنمنٹ آپریٹر اور ایک قدر استعمال کرنی ہوتی ہے۔ اگر فنکشن کال کرتے وقت اس پیرامیٹر کی قدر پاس نہ کی جائے تو ڈیفالٹ قدر استعمال ہوتی ہے، لیکن اگر قدر دی جائے تو یہ ڈیفالٹ قدر نظر انداز ہو جاتی ہے اور پاس کی گئی قدر استعمال ہوتی ہے۔',
      'د فنکشن د اعلان پر مهال کولی شو د وروستیو پاراميټرونو هر یوه ته ډیفالټ ارزښت وټاکو. دا ارزښت به هغه وخت وکارول شي چې د فنکشن د غوښتلو پر مهال اړوند دلیل تش پرېښودل شي. د دې لپاره یوازې باید د فنکشن په اعلان کې د دلیلونو لپاره د ګمارنې چلونکی او یو ارزښت وکاروو. که د فنکشن د غوښتلو پر مهال د هغه پاراميټر ارزښت ونه لېږدول شي، ډیفالټ ارزښت کارېږي، خو که ارزښت وټاکل شي دا ډیفالټ ارزښت له پامه غورځول کېږي او لېږدول شوی ارزښت کارېږي.')
    P('To demonstrate the concept of default arguments, consider the following general syntax.', 'ڈیفالٹ آرگیومنٹس کا تصور واضح کرنے کے لیے درج ذیل عمومی طریقۂ تحریر پر غور کریں۔', 'د ډیفالټ دلیلونو د مفهوم د ښودلو لپاره لاندې عمومي بڼې ته پام وکړئ.')
    code(t, 'Type function_name (parameter1=value, .....);')
    P('Here in this line of code, the type is any valid data type, function_name is the name of the function and parameter1 is the parameter having a default value named value assigned to it in the prototype. In the example given below, parameter b has a default value 2 assigned to it in the declaration. Now, if, one value is passed in the function call then the default value of b will be taken as the value of parameter ‘b’.',
      'کوڈ کی اس لائن میں type کوئی بھی درست ڈیٹا ٹائپ ہے، function_name فنکشن کا نام ہے اور parameter1 وہ پیرامیٹر ہے جسے پروٹوٹائپ میں value نامی ڈیفالٹ قدر دی گئی ہے۔ ذیل کی مثال میں پیرامیٹر b کو ڈکلیریشن میں ڈیفالٹ قدر 2 دی گئی ہے۔ اب اگر فنکشن کال میں ایک قدر پاس کی جائے تو b کی ڈیفالٹ قدر پیرامیٹر ‘b’ کی قدر کے طور پر لی جائے گی۔',
      'د کوډ په دې کرښه کې type هر سم ډېټا ډول دی، function_name د فنکشن نوم دی او parameter1 هغه پاراميټر دی چې په نمونه کې د value په نوم ډیفالټ ارزښت ورکړل شوی. په لاندې بېلګه کې b پاراميټر ته په اعلان کې ډیفالټ ارزښت 2 ورکړل شوی. اوس که د فنکشن په غوښتنه کې یو ارزښت ولېږدول شي، د b ډیفالټ ارزښت به د ‘b’ پاراميټر د ارزښت په توګه واخیستل شي.')
    code(t, 'int divide (int a, int b=2)')
    BOOK.save(106, [(6, rec(t, 13, 106, [200, 201]))], issues=[{'id': 'cs12-pdf106', 'unit': 6, 'printedPage': 200,
               'description': 'p.200 “a function named duplicate that receive arguments”; the first output line prints “x=1,y=3,z=7” without the spaces the program would print. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 104
    {104: p104, 105: p105, 106: p106}[n]()
