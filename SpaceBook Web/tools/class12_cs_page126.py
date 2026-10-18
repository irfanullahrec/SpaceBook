"""Computer Science XII PDF126–133: pp.240–255 — constructor programs (ConstTest, CRectangle), i. default, ii. user-defined (CExample, CNonParameter),
iii. constructor overloading, b. destructors, 8.1.6 inheritance and polymorphism (Figures 8.2, 8.2, 8.3, 8.4), b. polymorphism; p.255 Unit 8 summary.
Run: python class12_cs_page126.py N (126–133)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_8_2a, fig_8_2b, fig_8_3, fig_8_4

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u8-text-{n}', f'Unit 8 text ({n})', f'یونٹ 8 — متن ({n})', f'۸ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def vis(t, vid, f):
    en, ur, ps, ratio = f()
    t.visual(vid, en, ur, ps, ratio)


def p126():
    t = Builder()
    P = t.p
    P('Consider the following simple program to explain the concept of constructor in a class.', 'کلاس میں کنسٹرکٹر کا تصور واضح کرنے کے لیے درج ذیل سادہ پروگرام پر غور کریں۔', 'په ټولګي کې د جوړوونکي د مفهوم د تشریح لپاره لاندې ساده پروګرام ته پام وکړئ.')
    code(t, '''#include <iostream.h>
#include <conio.h>
class ConstTest
{
public:
ConstTest () // Constructor
{
cout<< “I am Constructor”;
}
};
int main()
{
ConstTest CT; // CT is an object to the class ConstTest
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'I am Constructor')
    P('In the above example, a class ConstTest is defined which have the constructor ConstTest() in its public part. In main() program, there is no explicit call to this constructor and it is automatically called when the object CT of this class is created. It should be noted that Constructors are always called at the moment when objects are created. They cannot be called explicitly as member functions are called.',
      'اوپر کی مثال میں کلاس ConstTest بیان کی گئی ہے جس کے public حصے میں کنسٹرکٹر ConstTest() ہے۔ main() پروگرام میں اس کنسٹرکٹر کو واضح طور پر کال نہیں کیا گیا اور یہ اس کلاس کا آبجیکٹ CT بننے پر خود بخود کال ہوتا ہے۔ یاد رہے کہ کنسٹرکٹرز ہمیشہ آبجیکٹس بننے کے لمحے کال ہوتے ہیں۔ انھیں ممبر فنکشنز کی طرح واضح طور پر کال نہیں کیا جا سکتا۔',
      'په پورته بېلګه کې ConstTest ټولګی تعریف شوی چې په public برخه کې یې ConstTest() جوړوونکی دی. په main() پروګرام کې دې جوړوونکي ته ښکاره غوښتنه نشته او د دې ټولګي د CT شي د جوړېدو پر مهال پخپله غوښتل کېږي. باید یاد ولرو چې جوړوونکي تل د شیانو د جوړېدو په شېبه کې غوښتل کېږي. د غړو فنکشنونو په څېر په ښکاره نه شي غوښتل کېدای.')
    P('Consider another program to implement the class CRectangle including a constructor:', 'ایک اور پروگرام پر غور کریں جو کنسٹرکٹر سمیت کلاس CRectangle کو نافذ کرتا ہے:', 'بل پروګرام ته پام وکړئ چې د جوړوونکي په ګډون CRectangle ټولګی پلي کوي:')
    code(t, '''#include <iostream.h>
#include <conio.h>
class CRectangle
{
int width, height;
public:
CRectangle (int a, int b) // constructor
{
width = a;
height = b;
}
int area()
{
return (width*height);
}
};
int main()
{
CRectangle r1 (13,14);
CRectangle r2 (15,16);
cout << "Area of Rectangle 1: " << r1.area() << endl;
cout << " Area of Rectangle 2: " << r2.area() << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Area of Rectangle 1: 182
Area of Rectangle 2: 240''')
    BOOK.save(126, [(8, rec(t, 7, 126, [240, 241, 242], 'The CRectangle output at the top of p.242 (PDF127) is given here with its program.'))],
              issues=[{'id': 'cs12-pdf126', 'unit': 8, 'printedPage': 240,
                       'description': 'p.240 “a class ConstTest is defined which have the constructor”. Retained as printed.'}])


def p127():
    t = Builder()
    P = t.p
    P('In the above example, the constructor CRectangle (int a, int b) is defined in the class CRectangle that initializes the values of width and height with the parameters that are passed to it when objects, r1 and r2, are created with the statement CRectangle r1 (13,14) and CRectangle r1 (13,14).',
      'اوپر کی مثال میں کنسٹرکٹر CRectangle (int a, int b) کلاس CRectangle میں بیان کیا گیا ہے جو width اور height کی قدروں کو ان پیرامیٹرز سے ابتدائی قدر دیتا ہے جو اسے آبجیکٹس r1 اور r2 بنتے وقت بیان CRectangle r1 (13,14) اور CRectangle r1 (13,14) سے پاس کیے جاتے ہیں۔',
      'په پورته بېلګه کې CRectangle (int a, int b) جوړوونکی په CRectangle ټولګي کې تعریف شوی چې د width او height ارزښتونو ته هغه پاراميټرونه لومړنی ارزښت ورکوي چې د r1 او r2 شیانو د جوړېدو پر مهال د CRectangle r1 (13,14) او CRectangle r1 (13,14) بیان سره ورته لېږدول کېږي.')
    t.h('i. Default constructor', 'i. ڈیفالٹ کنسٹرکٹر', 'i. ډیفالټ جوړوونکی')
    P('If we do not declare any constructor in a class definition, the compiler assumes that a class has a default constructor with no arguments.', 'اگر ہم کلاس کی تعریف میں کوئی کنسٹرکٹر ڈکلیئر نہ کریں تو کمپائلر فرض کرتا ہے کہ کلاس کا بغیر آرگیومنٹس کے ڈیفالٹ کنسٹرکٹر ہے۔', 'که د ټولګي په تعریف کې هېڅ جوړوونکی اعلان نه کړو، کمپایلر ګڼي چې ټولګی پرته له دلیلونو یو ډیفالټ جوړوونکی لري.')
    code(t, '''// default constructor
class DConstructor
{
public:
int a,b,c;
void multiply (int n, int m)
{
a=n;
b=m;
c=a*b;
}
};''')
    P('The compiler assumes that the class DConstructor has a default constructor, so the object of this class can be declared by specifying no arguments as given below:', 'کمپائلر فرض کرتا ہے کہ کلاس DConstructor کا ڈیفالٹ کنسٹرکٹر ہے، اس لیے اس کلاس کا آبجیکٹ بغیر آرگیومنٹس کے ڈکلیئر کیا جا سکتا ہے جیسا کہ ذیل میں ہے:', 'کمپایلر ګڼي چې DConstructor ټولګی ډیفالټ جوړوونکی لري، نو د دې ټولګي شی پرته له دلیلونو اعلانېدای شي لکه لاندې:')
    code(t, 'DConstructor DC;')
    P('Here, DC is an object to the class DConstructor with no arguments. Default constructors are also called implicit constructors.', 'یہاں DC کلاس DConstructor کا بغیر آرگیومنٹس کا آبجیکٹ ہے۔ ڈیفالٹ کنسٹرکٹرز کو implicit کنسٹرکٹرز بھی کہتے ہیں۔', 'دلته DC د DConstructor ټولګي پرته له دلیلونو شی دی. ډیفالټ جوړوونکي ضمني (implicit) جوړوونکي هم بلل کېږي.')
    t.h('ii. User-defined constructor/ Explicit constructor', 'ii. یوزر ڈیفائنڈ کنسٹرکٹر/ واضح کنسٹرکٹر', 'ii. د کاروونکي-تعریف شوی جوړوونکی/ ښکاره جوړوونکی')
    P('When users define constructors in class for their own purpose, especially for initialization of variables, then such types of constructors are called user defined constructors. When constructor is declared for a class, the compiler no longer provides an implicit default constructor. So, the objects should be declared according to the constructor prototypes that have been defined for the class.',
      'جب صارفین اپنے مقصد کے لیے، خاص طور پر ویری ایبلز کو ابتدائی قدر دینے کے لیے، کلاس میں کنسٹرکٹرز بیان کرتے ہیں تو ایسے کنسٹرکٹرز یوزر ڈیفائنڈ کنسٹرکٹرز کہلاتے ہیں۔ جب کلاس کے لیے کنسٹرکٹر ڈکلیئر کیا جائے تو کمپائلر مزید implicit ڈیفالٹ کنسٹرکٹر فراہم نہیں کرتا۔ اس لیے آبجیکٹس کو کلاس کے لیے بیان کیے گئے کنسٹرکٹر پروٹوٹائپس کے مطابق ڈکلیئر کرنا چاہیے۔',
      'کله چې کاروونکي د خپلې موخې لپاره، په ځانګړي ډول د متغیرونو د لومړني ارزښت لپاره، په ټولګي کې جوړوونکي تعریف کړي، داسې جوړوونکي د کاروونکي-تعریف شوي جوړوونکي بلل کېږي. کله چې د ټولګي لپاره جوړوونکی اعلان شي، کمپایلر نور ضمني ډیفالټ جوړوونکی نه برابروي. نو شیان باید د هغو جوړوونکو نمونو سره سم اعلان شي چې د ټولګي لپاره تعریف شوې.')
    code(t, '''// user-defined ( parameterized) constructor example
#include <iostream.h>
#include <conio.h>
class CExample
{
public:
int a,b,c;
CExample (int n, int m)
{
a=n;
b=m;
}
int multiply ()
{
c=a*b;
return c;
}
};
int main()
{
CExample CObj (50,10);
int result=CObj.multiply();
cout<<"Multiplication Results is: "<<result;
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'Multiplication Result is: 500')
    BOOK.save(127, [(8, rec(t, 8, 127, [242, 243, 244], 'The CRectangle output at the top of p.242 is recorded with PDF126. The CExample program ends on p.244 (PDF128) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf127', 'unit': 8, 'printedPage': 242,
                       'description': 'p.242 names the second statement “CRectangle r1 (13,14)” twice (the program declares r2 (15,16)); the CExample program prints “Multiplication Results is:” but the output reads “Multiplication Result is: 500”. Retained as printed.'}])


def p128():
    t = Builder()
    P = t.p
    P('Here, a constructor CExample with two parameters of type int has been declared that initializes private variables a and b. When the object declaration is done as follows:', 'یہاں int قسم کے دو پیرامیٹرز والا کنسٹرکٹر CExample ڈکلیئر کیا گیا ہے جو private ویری ایبلز a اور b کو ابتدائی قدر دیتا ہے۔ جب آبجیکٹ کی ڈکلیریشن یوں کی جائے:', 'دلته د int ډول دوه پاراميټرونو سره CExample جوړوونکی اعلان شوی چې private متغیرونو a او b ته لومړنی ارزښت ورکوي. کله چې د شي اعلان داسې وشي:')
    code(t, 'CExample CObj (5,10);')
    P('The following declaration is not correct, because, we have declared the class to have an explicit constructor (user-defined constructor) to which the values should be passed.', 'درج ذیل ڈکلیریشن درست نہیں، کیونکہ ہم نے کلاس کو واضح کنسٹرکٹر (یوزر ڈیفائنڈ کنسٹرکٹر) کے ساتھ ڈکلیئر کیا ہے جسے قدریں پاس کرنی چاہییں۔', 'لاندې اعلان سم نه دی، ځکه موږ ټولګی د ښکاره جوړوونکي (د کاروونکي-تعریف شوي جوړوونکي) سره اعلان کړی چې باید ارزښتونه ورته ولېږدول شي.')
    code(t, 'CExample CObj;')
    P('A user-defined constructor can be either parameterized or non-parameterized. A parameterized constructor is the one which accepts arguments while the object is declared and nonparameterized constructor is the one whose object declaration is done without specifying arguments. The program given above defines parameterized constructor. The following program explains non-parameterized constructor.',
      'یوزر ڈیفائنڈ کنسٹرکٹر پیرامیٹرائزڈ یا نان پیرامیٹرائزڈ ہو سکتا ہے۔ پیرامیٹرائزڈ کنسٹرکٹر وہ ہے جو آبجیکٹ ڈکلیئر ہوتے وقت آرگیومنٹس قبول کرتا ہے اور نان پیرامیٹرائزڈ کنسٹرکٹر وہ ہے جس کے آبجیکٹ کی ڈکلیریشن آرگیومنٹس کے بغیر ہوتی ہے۔ اوپر دیا گیا پروگرام پیرامیٹرائزڈ کنسٹرکٹر بیان کرتا ہے۔ درج ذیل پروگرام نان پیرامیٹرائزڈ کنسٹرکٹر واضح کرتا ہے۔',
      'د کاروونکي-تعریف شوی جوړوونکی کېدای شي پاراميټر لرونکی یا بې‌پاراميټره وي. پاراميټر لرونکی جوړوونکی هغه دی چې د شي د اعلان پر مهال دلیلونه مني او بې‌پاراميټره جوړوونکی هغه دی چې د شي اعلان یې پرته له دلیلونو کېږي. پورته ورکړل شوی پروګرام پاراميټر لرونکی جوړوونکی تعریفوي. لاندې پروګرام بې‌پاراميټره جوړوونکی تشریح کوي.')
    code(t, '''#include <iostream.h>
#include <conio.h>
class CNonParameter
{
public:
CNonParameter ()
{
cout<< “I am non-parameterized constructor”;
}
};
int main()
{
CNonParameter NP;
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'I am non-parameterized constructor')
    P('In this example, the constructor CNonParameter() has no parameters and thus the object creation statement, CNonParameter NP;, passes no arguments.', 'اس مثال میں کنسٹرکٹر CNonParameter() کے کوئی پیرامیٹرز نہیں اور اس لیے آبجیکٹ بنانے کا بیان CNonParameter NP; کوئی آرگیومنٹ پاس نہیں کرتا۔', 'په دې بېلګه کې CNonParameter() جوړوونکی هېڅ پاراميټر نه لري او له دې امله د شي د جوړولو بیان CNonParameter NP; هېڅ دلیل نه لېږدوي.')
    t.h('iii. Constructor overloading', 'iii. کنسٹرکٹر اوورلوڈنگ', 'iii. د جوړوونکي ډېرول')
    P('Using more than one constructors in the same class is called constructor overloading. Like any other function, a constructor can also be overloaded with more than one function that have the same name but different types or number of parameters. For an overloaded function, the compiler calls the function whose parameters match the arguments used in the function call. In the case of constructor overloading, that constructor is executed whose parameters match the arguments passed to the object declaration. Consider the following program.',
      'ایک ہی کلاس میں ایک سے زیادہ کنسٹرکٹرز استعمال کرنا کنسٹرکٹر اوورلوڈنگ کہلاتا ہے۔ کسی بھی دوسرے فنکشن کی طرح کنسٹرکٹر کو بھی ایک سے زیادہ ایسے فنکشنز کے ساتھ اوورلوڈ کیا جا سکتا ہے جن کا نام ایک لیکن پیرامیٹرز کی اقسام یا تعداد مختلف ہو۔ اوورلوڈ فنکشن کے لیے کمپائلر وہ فنکشن کال کرتا ہے جس کے پیرامیٹرز فنکشن کال میں استعمال ہونے والے آرگیومنٹس سے ملتے ہوں۔ کنسٹرکٹر اوورلوڈنگ کی صورت میں وہ کنسٹرکٹر چلتا ہے جس کے پیرامیٹرز آبجیکٹ ڈکلیریشن کو پاس کیے گئے آرگیومنٹس سے ملتے ہوں۔ درج ذیل پروگرام پر غور کریں۔',
      'په یوه ټولګي کې له یوه ډېر جوړوونکي کارول د جوړوونکي ډېرول بلل کېږي. د هر بل فنکشن په څېر جوړوونکی هم له یوه ډېرو داسې فنکشنونو سره ډېرېدای شي چې نوم یې یو خو د پاراميټرونو ډولونه یا شمېر یې بېل وي. د ډېر شوي فنکشن لپاره کمپایلر هغه فنکشن غواړي چې پاراميټرونه یې د فنکشن په غوښتنه کې کارول شویو دلیلونو سره سمون ولري. د جوړوونکي د ډېرولو په حالت کې هغه جوړوونکی اجرا کېږي چې پاراميټرونه یې د شي اعلان ته لېږدول شویو دلیلونو سره سمون ولري. لاندې پروګرام ته پام وکړئ.')
    code(t, '''// constructors overloading
#include <iostream.h>
#include <conio.h>
class CRectangle
{
int width, length;
public:
CRectangle()
{
width = 5;
length = 15;
}
CRectangle (int a, int b)
{
width = a;
length = b;
}
int area()
{
return (width*length);
}
};
int main()
{
CRectangle r1 (5,14);
CRectangle r2;
cout << "Area of first rectangle: " << r1.area() << endl;
cout << "Area of second rectangle: " << r2.area() << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Area of first rectangle: 70
Area of second rectangle: 75''')
    BOOK.save(128, [(8, rec(t, 9, 128, [244, 245, 246], 'The top of p.244 (end of the CExample program and its output) is recorded with PDF127. The overloading program runs from p.245 to p.246 (PDF129) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf128', 'unit': 8, 'printedPage': 244,
                       'description': 'p.244 says CExample “initializes private variables a and b” though they are declared public; the example declaration uses CObj (5,10) while the program uses (50,10); p.245 “more than one constructors”. Retained as printed.'}])


def p129():
    t = Builder()
    P = t.p
    P('In the above example, the first object r1 passes the arguments (5,14) to the second constructor and thus the output generated is 70. The second object r2 calls the non-parameterized constructor of the class and initializes the variables width with 5 and length with 15 and thus the result calculated is 75.',
      'اوپر کی مثال میں پہلا آبجیکٹ r1 دوسرے کنسٹرکٹر کو آرگیومنٹس (5,14) پاس کرتا ہے اور یوں آؤٹ پٹ 70 بنتا ہے۔ دوسرا آبجیکٹ r2 کلاس کے نان پیرامیٹرائزڈ کنسٹرکٹر کو کال کرتا ہے اور ویری ایبلز width کو 5 اور length کو 15 سے ابتدائی قدر دیتا ہے اور یوں حساب شدہ نتیجہ 75 آتا ہے۔',
      'په پورته بېلګه کې لومړی شی r1 دویم جوړوونکي ته دلیلونه (5,14) لېږدوي او په دې توګه وتنه 70 کېږي. دویم شی r2 د ټولګي بې‌پاراميټره جوړوونکی غواړي او width متغیر ته 5 او length ته 15 لومړنی ارزښت ورکوي او په دې توګه حساب شوې پایله 75 کېږي.')
    t.h('b. Destructors', 'b. ڈسٹرکٹرز', 'b. ړنګوونکي')
    P('Destructors are special member functions that are executed when an object is destroyed. Destructor fulfills the opposite functionality of constructor and thus de-allocates the memory allocated to an object during its creation. They are called automatically when objects are destroyed.',
      'ڈسٹرکٹرز خاص ممبر فنکشنز ہیں جو آبجیکٹ ختم ہونے پر چلتے ہیں۔ ڈسٹرکٹر کنسٹرکٹر کے برعکس کام انجام دیتا ہے اور یوں آبجیکٹ کی تخلیق کے دوران اسے دی گئی میموری واپس لیتا ہے۔ یہ آبجیکٹس ختم ہونے پر خود بخود کال ہوتے ہیں۔',
      'ړنګوونکي ځانګړي غړي فنکشنونه دي چې د شي د ړنګېدو پر مهال اجرا کېږي. ړنګوونکی د جوړوونکي برعکس دنده ترسره کوي او په دې توګه هغه حافظه بېرته اخلي چې د شي د جوړېدو پر مهال ورته ورکړل شوې وه. د شیانو د ړنګېدو پر مهال پخپله غوښتل کېږي.')
    P('Like constructors, destructors have the following specific features:', 'کنسٹرکٹرز کی طرح ڈسٹرکٹرز کی بھی درج ذیل مخصوص خصوصیات ہیں:', 'د جوړوونکو په څېر ړنګوونکي هم لاندې ځانګړتیاوې لري:')
    t.group('list', [('Destructor has the same name as that of the class, preceded by a tilde symbol ~.', 'ڈسٹرکٹر کا نام کلاس کے نام جیسا ہوتا ہے جس سے پہلے ٹلڈا نشان ~ ہوتا ہے۔', 'ړنګوونکی د ټولګي په څېر نوم لري چې مخکې یې د ټیلډ نښه ~ وي.'),
                     ('Destructor cannot take arguments.', 'ڈسٹرکٹر آرگیومنٹس نہیں لے سکتا۔', 'ړنګوونکی دلیلونه نه شي اخیستی.'),
                     ('Destructor has no return type.', 'ڈسٹرکٹر کی کوئی ریٹرن ٹائپ نہیں ہوتی۔', 'ړنګوونکی د بېرته ورکړې ډول نه لري.')])
    P('The second feature given above, implies that only one destructor may exist per class, as there is no way to overload destructors since they cannot be differentiated from each other based on arguments.', 'اوپر دی گئی دوسری خصوصیت کا مطلب ہے کہ ہر کلاس میں صرف ایک ڈسٹرکٹر ہو سکتا ہے، کیونکہ ڈسٹرکٹرز کو اوورلوڈ کرنے کا کوئی طریقہ نہیں کہ انھیں آرگیومنٹس کی بنیاد پر ایک دوسرے سے ممیز نہیں کیا جا سکتا۔', 'پورته دویمه ځانګړتیا دا معنا لري چې په هر ټولګي کې یوازې یو ړنګوونکی کېدای شي، ځکه د ړنګوونکو د ډېرولو هېڅ لاره نشته، ځکه د دلیلونو پر بنسټ یو له بله نه شي جلا کېدای.')
    P('Consider the following program to explain the concept of both constructor and destructor.', 'کنسٹرکٹر اور ڈسٹرکٹر دونوں کا تصور واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د جوړوونکي او ړنګوونکي دواړو د مفهوم د تشریح لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''#include <iostream.h>
#include <conio.h>
class A
{
public:
A () //constructor
{
cout<<"I am constructor"<<endl;
}
~A () // destructor
{
cout<<"I am destructor";
}
};
int main()
{
A a1;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''I am constructor
I am destructor''')
    BOOK.save(129, [(8, rec(t, 10, 129, [246, 247, 248], 'The top of p.246 (end of the overloading program and its output) is recorded with PDF128. The constructor/destructor program runs from p.247 to p.248 (PDF130) and is given whole with its output.'))])


def p130():
    t = Builder()
    P = t.p
    P('In this example, ~A () is a destructor. When the program runs and the object a1 is created, constructor A() is called displaying the message “I am constructor”. But, when the control goes out of the program and the object is destroyed, the destructor ~A () is called to de-allocate the memory reserved by the object of the class and a message, “I am destructor”, is displayed to verify that the destructor is executed.',
      'اس مثال میں ~A () ایک ڈسٹرکٹر ہے۔ جب پروگرام چلتا ہے اور آبجیکٹ a1 بنتا ہے تو کنسٹرکٹر A() کال ہوتا ہے جو پیغام ’’I am constructor‘‘ دکھاتا ہے۔ لیکن جب کنسٹرکٹر پروگرام سے باہر جاتا ہے اور آبجیکٹ ختم ہوتا ہے تو ڈسٹرکٹر ~A () کال ہوتا ہے جو کلاس کے آبجیکٹ کی مختص میموری واپس لیتا ہے اور یہ تصدیق کرنے کے لیے کہ ڈسٹرکٹر چلا ہے، پیغام ’’I am destructor‘‘ دکھایا جاتا ہے۔',
      'په دې بېلګه کې ~A () ړنګوونکی دی. کله چې پروګرام اجرا شي او a1 شی جوړ شي، A() جوړوونکی غوښتل کېږي چې د "I am constructor" پیغام ښيي. خو کله چې کنټرول له پروګرام ووځي او شی ړنګ شي، ~A () ړنګوونکی غوښتل کېږي ترڅو د ټولګي د شي ساتل شوې حافظه بېرته واخلي او د دې تایید لپاره چې ړنګوونکی اجرا شو، د "I am destructor" پیغام ښودل کېږي.')
    t.h('8.1. 6 Inheritance and Polymorphism', '8.1.6 وراثت اور پولی مورفزم', '۸.۱.۶ میراث او پولي‌مورفیزم')
    P('Object Oriented Programming (OOP) languages have the features of code reusability and polymorphism. Code reusability is the key feature among all other features of OOP which can be achieved by the use of inheritance. Similarly, C++ has the ability to use function name and operator for multiple tasks.',
      'آبجیکٹ اورینٹڈ پروگرامنگ (OOP) زبانوں میں کوڈ کے دوبارہ استعمال اور پولی مورفزم کی خصوصیات ہیں۔ کوڈ کا دوبارہ استعمال OOP کی تمام دوسری خصوصیات میں کلیدی خصوصیت ہے جو وراثت کے استعمال سے حاصل کی جا سکتی ہے۔ اسی طرح C++ متعدد کاموں کے لیے فنکشن نام اور آپریٹر استعمال کرنے کی صلاحیت رکھتی ہے۔',
      'د شیانو ته متوجه پروګرام‌سازۍ (OOP) ژبې د کوډ د بیا کارونې او پولي‌مورفیزم ځانګړتیاوې لري. د کوډ بیا کارونه د OOP د ټولو نورو ځانګړتیاوو ترمنځ کلیدي ځانګړتیا ده چې د میراث په کارولو ترلاسه کېږي. همداراز C++ دا وړتیا لري چې د فنکشن نوم او چلونکی د ډېرو دندو لپاره وکاروي.')
    t.h('a. Inheritance', 'a. وراثت', 'a. میراث')
    P('A key feature of C++ classes in which new classes are created from existing classes is called inheritance. Inheritance uses the concept of parent and child class. A Parent Class is the class from which others classes are derived. It is also called base class. A Sub Class is a class which inherits features from the base class. A sub-class is also called child class or derived class. A few examples of inheritance from daily life are given below:',
      'C++ کلاسز کی کلیدی خصوصیت جس میں موجودہ کلاسز سے نئی کلاسز بنائی جاتی ہیں، وراثت کہلاتی ہے۔ وراثت پیرنٹ اور چائلڈ کلاس کا تصور استعمال کرتی ہے۔ پیرنٹ کلاس وہ کلاس ہے جس سے دوسری کلاسز اخذ کی جاتی ہیں۔ اسے بیس کلاس بھی کہتے ہیں۔ سب کلاس وہ کلاس ہے جو بیس کلاس سے خصوصیات ورثے میں لیتی ہے۔ سب کلاس کو چائلڈ کلاس یا ڈیرائیوڈ کلاس بھی کہتے ہیں۔ روزمرہ زندگی سے وراثت کی چند مثالیں ذیل میں دی گئی ہیں:',
      'د C++ ټولګیو کلیدي ځانګړتیا چې پکې له موجودو ټولګیو نوي ټولګي جوړېږي، میراث بلل کېږي. میراث د مور/پلار او ماشوم ټولګي مفهوم کاروي. مور/پلار ټولګی هغه ټولګی دی چې نور ټولګي ترې مشتق کېږي. اساسي ټولګی (base class) هم بلل کېږي. فرعي ټولګی هغه ټولګی دی چې له اساسي ټولګي ځانګړتیاوې په میراث اخلي. فرعي ټولګی ماشوم ټولګی یا مشتق ټولګی هم بلل کېږي. د ورځني ژوند څو بېلګې لاندې ورکړل شوې:')
    t.group('list', [('Consider an apple and a banana. Although an apple and banana are different fruits, both have common feature that they are fruits. Because, apples and bananas are fruits, anything that is true for fruits is also true for apples and bananas. For example, all fruits have a name, a flavor, and are tangible objects. Thus, apples and bananas also have a name, a flavor, and are tangible objects. Apples and bananas inherit these properties from the concept of fruit because they are fruit. Apples and bananas then define some of the properties in different ways as bananas shape is different from apple, also apples have seeds but bananas have no seeds, which make them different from each other.',
                      'سیب اور کیلے پر غور کریں۔ اگرچہ سیب اور کیلا مختلف پھل ہیں، دونوں کی مشترکہ خصوصیت یہ ہے کہ دونوں پھل ہیں۔ چونکہ سیب اور کیلے پھل ہیں، اس لیے جو کچھ پھلوں کے لیے درست ہے وہ سیب اور کیلے کے لیے بھی درست ہے۔ مثلاً تمام پھلوں کا نام اور ذائقہ ہوتا ہے اور وہ ٹھوس اشیا ہیں۔ یوں سیب اور کیلے کا بھی نام اور ذائقہ ہے اور وہ ٹھوس اشیا ہیں۔ سیب اور کیلے یہ خصوصیات پھل کے تصور سے ورثے میں لیتے ہیں کیونکہ وہ پھل ہیں۔ پھر سیب اور کیلے کچھ خصوصیات مختلف طریقوں سے بیان کرتے ہیں، جیسے کیلے کی شکل سیب سے مختلف ہے، نیز سیب میں بیج ہوتے ہیں لیکن کیلے میں نہیں، جو انھیں ایک دوسرے سے مختلف بناتا ہے۔',
                      'مڼې او کېلې ته پام وکړئ. که څه هم مڼه او کېله بېلې مېوې دي، دواړه ګډه ځانګړتیا لري چې مېوې دي. څرنګه چې مڼې او کېلې مېوې دي، هر هغه څه چې د مېوو لپاره سم وي د مڼو او کېلو لپاره هم سم دي. د بېلګې په توګه ټولې مېوې نوم او خوند لري او محسوس شیان دي. نو مڼې او کېلې هم نوم او خوند لري او محسوس شیان دي. مڼې او کېلې دا ځانګړنې د مېوې له مفهوم څخه په میراث اخلي ځکه چې مېوې دي. بیا مڼې او کېلې ځینې ځانګړنې په بېلو لارو ټاکي، لکه د کېلې بڼه له مڼې بېله ده، همداراز مڼې زړي لري خو کېلې زړي نه لري، چې یو له بله یې بېلوي.')])
    vis(t, 'cs12-fig-8-2-fruit', fig_8_2a)
    BOOK.save(130, [(8, rec(t, 11, 130, [248, 249], 'Figure 8.2 (Fruit) is reproduced as a coded diagram.'))],
              issues=[{'id': 'cs12-pdf130', 'unit': 8, 'printedPage': 249,
                       'description': 'p.249 “others classes are derived”; two different figures on pp.249–250 are both captioned “Figure 8.2”; the heading is printed “8.1. 6”. Retained as printed.'}])


def p131():
    t = Builder()
    P = t.p
    t.group('list', [('Here is another example of shape class which has a series of child classes that describe shapes Rectangle and Triangle. They have certain common properties, such as both can be described by means of their sides but they have their own characteristics i.e. triangle has three sides and rectangle has four sides. Square is more special case with four sides of equal length.',
                      'یہ شیپ کلاس کی ایک اور مثال ہے جس کی چائلڈ کلاسز کا سلسلہ شکلیں مستطیل اور مثلث بیان کرتا ہے۔ ان کی کچھ مشترکہ خصوصیات ہیں، جیسے دونوں کو ان کے اضلاع سے بیان کیا جا سکتا ہے لیکن ان کی اپنی خصوصیات ہیں یعنی مثلث کے تین اضلاع اور مستطیل کے چار اضلاع ہیں۔ مربع چار برابر لمبائی کے اضلاع والی زیادہ خاص صورت ہے۔',
                      'دا د بڼې ټولګي بله بېلګه ده چې د ماشوم ټولګیو لړۍ لري چې مستطیل او مثلث بڼې بیانوي. ځینې ګډې ځانګړنې لري، لکه دواړه د خپلو ضلعو په مرسته بیانېدای شي، خو خپلې ځانګړنې هم لري، یعنې مثلث درې ضلعې او مستطیل څلور ضلعې لري. مربع د څلورو مساوي اوږدو ضلعو سره ځانګړی حالت دی.')])
    vis(t, 'cs12-fig-8-2-shape', fig_8_2b)
    t.group('list', [('We can also represent patients into indoor and outdoor patients in which both have some common features like name, father name, age, address and disease but indoor patient have ‘Ward No’ and ‘Bed No’ as its unique features and the outdoor patient have ‘Next date of visit’ as its unique feature. It can be represented as follows:',
                      'ہم مریضوں کو اِن ڈور اور آؤٹ ڈور مریضوں میں بھی ظاہر کر سکتے ہیں جن دونوں کی کچھ مشترکہ خصوصیات ہیں جیسے نام، والد کا نام، عمر، پتہ اور بیماری، لیکن اِن ڈور مریض کی منفرد خصوصیات ’وارڈ نمبر‘ اور ’بیڈ نمبر‘ ہیں اور آؤٹ ڈور مریض کی منفرد خصوصیت ’اگلی ملاقات کی تاریخ‘ ہے۔ اسے یوں ظاہر کیا جا سکتا ہے:',
                      'موږ کولی شو ناروغان په داخلي او بهرنیو ناروغانو هم وښیو چې دواړه ځینې ګډې ځانګړنې لري لکه نوم، د پلار نوم، عمر، پته او ناروغي، خو داخلي ناروغ ‘د وارډ شمېره’ او ‘د بستر شمېره’ د ځانګړو ځانګړنو په توګه لري او بهرنی ناروغ ‘د راتلونکې کتنې نېټه’ د ځانګړې ځانګړنې په توګه لري. داسې ښودل کېدای شي:')])
    vis(t, 'cs12-fig-8-3', fig_8_3)
    P('In order to derive the child class Indoor from the base class patient, the following statement is used.', 'بیس کلاس patient سے چائلڈ کلاس Indoor اخذ کرنے کے لیے درج ذیل بیان استعمال ہوتا ہے۔', 'له اساسي ټولګي patient څخه د Indoor ماشوم ټولګي د مشتق کولو لپاره لاندې بیان کارېږي.')
    code(t, '''class Indoor: public Patient
{
};''')
    P('The public access specifier is used to derive a class from its parent class. The keyword public may be replaced by any one of the other access specifiers protected and private.', 'کلاس کو اس کی پیرنٹ کلاس سے اخذ کرنے کے لیے public ایکسس اسپیسیفائر استعمال ہوتا ہے۔ کلیدی لفظ public کو دوسرے ایکسس اسپیسیفائرز protected اور private میں سے کسی سے بدلا جا سکتا ہے۔', 'یو ټولګی د هغه له مور/پلار ټولګي څخه د مشتق کولو لپاره public د لاسرسي ټاکونکی کارېږي. public کلیدي کلمه د نورو لاسرسي ټاکونکو protected او private له هر یوه سره بدلېدای شي.')
    P('The following lines of code give the general syntax of using inheritance.', 'کوڈ کی درج ذیل لائنیں وراثت کے استعمال کا عمومی طریقۂ تحریر دیتی ہیں۔', 'د کوډ لاندې کرښې د میراث د کارونې عمومي بڼه ورکوي.')
    code(t, '''class A // base class
{
};
class B: public A //class B is derived from class A
{
};''')
    P('A complete C++ program for the above sketch is given below.', 'اوپر کے خاکے کے لیے مکمل C++ پروگرام ذیل میں دیا گیا ہے۔', 'د پورته سکېچ لپاره بشپړ C++ پروګرام لاندې ورکړل شوی.')
    code(t, '''#include <iostream.h>
#include <conio.h>
class A
{
public:
void showa()
{
cout<<"I am in base class A"<<endl;
}
};
class B: public A
{
public:
void showb()
{
cout<<"I am in derived class B"<<endl;
}
};
int main()
{
B b1; // object of the derived class
b1.showa(); // object of B calling function of base class A
b1.showb(); // object of B calling own function
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''I am in base class A
I am in derived class B''')
    BOOK.save(131, [(8, rec(t, 12, 131, [250, 251, 252], 'Figures 8.2 (Shape) and 8.3 are reproduced as coded diagrams. The complete inheritance program begins at the foot of p.251 and continues on p.252 (PDF132); it is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf131', 'unit': 8, 'printedPage': 251,
                       'description': 'p.250 “indoor patient have … its unique features”; p.251 “base class patient” (lower case) while the code uses Patient. Retained as printed.'}])


def p132():
    t = Builder()
    P = t.p
    P('In this example, we have two classes A and B. Class B is publically derived from class A and has therefore right to access the member function of class A. In main (), we have created only object b1 for class B and have called the member functions showa() of base class A and showb() of derived class B that have produced the output as shown above.',
      'اس مثال میں ہمارے پاس دو کلاسز A اور B ہیں۔ کلاس B، کلاس A سے public طور پر اخذ کی گئی ہے اور اس لیے اسے کلاس A کے ممبر فنکشن تک رسائی کا حق ہے۔ main () میں ہم نے کلاس B کا صرف آبجیکٹ b1 بنایا ہے اور بیس کلاس A کا ممبر فنکشن showa() اور ڈیرائیوڈ کلاس B کا showb() کال کیا ہے جنھوں نے اوپر دکھایا گیا آؤٹ پٹ پیدا کیا ہے۔',
      'په دې بېلګه کې دوه ټولګي A او B لرو. B ټولګی له A ټولګي څخه په public ډول مشتق شوی او له دې امله د A ټولګي غړي فنکشن ته د لاسرسي حق لري. په main () کې موږ د B ټولګي یوازې b1 شی جوړ کړی او د اساسي ټولګي A غړی فنکشن showa() او د مشتق ټولګي B showb() مو غوښتي چې پورته ښودل شوې وتنه یې جوړه کړې.')
    P('In inheritance, sometimes a class is derived from more than one parent classes and the phenomenon is called multiple inheritance. In this case the derived class has properties of base classes as well as its own.', 'وراثت میں بعض اوقات ایک کلاس ایک سے زیادہ پیرنٹ کلاسز سے اخذ کی جاتی ہے اور اس عمل کو متعدد وراثت کہتے ہیں۔ اس صورت میں ڈیرائیوڈ کلاس میں بیس کلاسز کی خصوصیات کے ساتھ اپنی خصوصیات بھی ہوتی ہیں۔', 'په میراث کې کله کله یو ټولګی له یوه ډېرو مور/پلار ټولګیو مشتق کېږي او دې پدیدې ته څو ګونی میراث وایي. په دې حالت کې مشتق ټولګی د اساسي ټولګیو ځانګړنې او خپلې ځانګړنې هم لري.')
    code(t, '''class A
{ };
class B
{ };
class c: public A, public B
{ };''')
    vis(t, 'cs12-fig-8-4', fig_8_4)
    t.h('b. Polymorphism', 'b. پولی مورفزم', 'b. پولي‌مورفیزم')
    P('Polymorphism is the ability to use an operator or function in multiple ways. Polymorphism gives different meanings or functionality to the operators or functions. Poly, refers to many, signifies that there are many uses of these operators and functions.',
      'پولی مورفزم کسی آپریٹر یا فنکشن کو متعدد طریقوں سے استعمال کرنے کی صلاحیت ہے۔ پولی مورفزم آپریٹرز یا فنکشنز کو مختلف معنی یا کارکردگی دیتا ہے۔ Poly یعنی بہت سے، ظاہر کرتا ہے کہ ان آپریٹرز اور فنکشنز کے بہت سے استعمالات ہیں۔',
      'پولي‌مورفیزم د یوه چلونکي یا فنکشن په ډېرو لارو د کارولو وړتیا ده. پولي‌مورفیزم چلونکو یا فنکشنونو ته بېلې معناوې یا دندې ورکوي. Poly چې ډېر معنا لري، ښيي چې د دې چلونکو او فنکشنونو ډېرې کارونې دي.')
    P('In C++, polymorphism can be achieved by one of the following concepts.', 'C++ میں پولی مورفزم درج ذیل تصورات میں سے کسی ایک سے حاصل کیا جا سکتا ہے۔', 'په C++ کې پولي‌مورفیزم د لاندې مفاهیمو له یوه په مرسته ترلاسه کېدای شي.')
    t.group('list', [('Function overloading', 'فنکشن اوورلوڈنگ', 'د فنکشن ډېرول'), ('Operator overloading', 'آپریٹر اوورلوڈنگ', 'د چلونکي ډېرول'), ('Virtual functions', 'ورچوئل فنکشنز', 'مجازي فنکشنونه')])
    BOOK.save(132, [(8, rec(t, 13, 132, [252, 253], 'The inheritance program at the top of p.252 is recorded with PDF131. Figure 8.4 is reproduced as a coded diagram.'))],
              issues=[{'id': 'cs12-pdf132', 'unit': 8, 'printedPage': 252,
                       'description': 'p.252 “publically derived”; p.253 “more than one parent classes”, class name “c” in lower case. Retained as printed.'}])


def p133():
    t = Builder()
    P = t.p
    P('Function overloading is the concept of using same function name for related but slightly different purposes in a single program. We have discussed it in detail in unit 6 with the help of programming examples.', 'فنکشن اوورلوڈنگ ایک پروگرام میں متعلقہ لیکن قدرے مختلف مقاصد کے لیے ایک ہی فنکشن نام استعمال کرنے کا تصور ہے۔ ہم نے یونٹ 6 میں پروگرامنگ مثالوں کی مدد سے اس پر تفصیل سے بات کی ہے۔', 'د فنکشن ډېرول په یوه پروګرام کې د اړوندو خو یو څه بېلو موخو لپاره د یو فنکشن نوم د کارولو مفهوم دی. موږ په ۶ څپرکي کې د پروګرامي بېلګو په مرسته په تفصیل څېړلی.')
    P('Consider the following simple examples to understand the concept of polymorphism with respect to operator overloading.', 'آپریٹر اوورلوڈنگ کے حوالے سے پولی مورفزم کا تصور سمجھنے کے لیے درج ذیل سادہ مثالوں پر غور کریں۔', 'د چلونکي ډېرولو په اړه د پولي‌مورفیزم د مفهوم د پوهېدو لپاره لاندې ساده بېلګو ته پام وکړئ.')
    code(t, '6 + 10;')
    P('The above statement refers to integer addition with the help of + operator. The same + operator can also be used for addition of two floating point numbers or two strings (concatenation) as shown below.', 'اوپر کا بیان + آپریٹر کی مدد سے صحیح اعداد کی جمع ظاہر کرتا ہے۔ یہی + آپریٹر دو فلوٹنگ پوائنٹ اعداد یا دو اسٹرنگز کی جمع (کنکیٹینیشن) کے لیے بھی استعمال ہو سکتا ہے جیسا کہ ذیل میں دکھایا گیا ہے۔', 'پورته بیان د + چلونکي په مرسته د صحیح عددونو جمع ته اشاره کوي. همدا + چلونکی د دوو اعشاري عددونو یا دوو تارونو د جمع (نښلولو) لپاره هم کارېدای شي لکه لاندې.')
    code(t, '''7.15 + 3.78
"Computer" + "Training"''')
    P('Polymorphism is a powerful feature of every Object Oriented Programming (OOP) language, especially of C++. A single operator ‘+’ behaves differently in different contexts such as integer and float addition and strings concatenation. This concept is known as operator overloading.',
      'پولی مورفزم ہر آبجیکٹ اورینٹڈ پروگرامنگ (OOP) زبان، خاص طور پر C++ کی ایک طاقتور خصوصیت ہے۔ ایک ہی آپریٹر ‘+’ مختلف سیاق میں مختلف رویہ اختیار کرتا ہے جیسے integer اور float کی جمع اور اسٹرنگز کو جوڑنا۔ اس تصور کو آپریٹر اوورلوڈنگ کہتے ہیں۔',
      'پولي‌مورفیزم د هرې د شیانو ته متوجه پروګرامي (OOP) ژبې، په ځانګړي ډول د C++، پیاوړې ځانګړتیا ده. یو چلونکی ‘+’ په بېلو شرایطو کې بېل چلند کوي لکه د integer او float جمع او د تارونو نښلول. دې مفهوم ته د چلونکي ډېرول (operator overloading) وایي.')
    P('A virtual function or virtual method is a function or method whose behavior can be overridden within an inheriting class by a function with the same signature. This concept is a very important part of the polymorphism portion of object-oriented programming (OOP).',
      'ورچوئل فنکشن یا ورچوئل میتھڈ وہ فنکشن یا میتھڈ ہے جس کا رویہ وراثت لینے والی کلاس میں اسی سگنیچر والے فنکشن سے بدلا جا سکتا ہے۔ یہ تصور آبجیکٹ اورینٹڈ پروگرامنگ (OOP) کے پولی مورفزم حصے کا بہت اہم جزو ہے۔',
      'مجازي فنکشن یا مجازي میتود هغه فنکشن یا میتود دی چې چلند یې په میراث اخیستونکي ټولګي کې د ورته لاسلیک لرونکي فنکشن په مرسته بدلېدای شي. دا مفهوم د شیانو ته متوجه پروګرام‌سازۍ (OOP) د پولي‌مورفیزم برخې ډېره مهمه برخه ده.')
    tx = rec(t, 14, 133, [254])
    s = Builder()
    s.h('Summary', 'خلاصہ', 'لنډیز')
    s.group('list', [
     ('A class consists of attributes called data members and function called member function.', 'کلاس ڈیٹا ممبرز کہلانے والی خصوصیات اور ممبر فنکشن کہلانے والے فنکشن پر مشتمل ہوتی ہے۔', 'ټولګی د ډېټا غړو په نوم ځانګړنې او د غړي فنکشن په نوم فنکشن لري.'),
     ('A variable of type class is called object. In C++, when variables of type class are declared they create objects.', 'کلاس قسم کا ویری ایبل آبجیکٹ کہلاتا ہے۔ C++ میں جب کلاس قسم کے ویری ایبلز ڈکلیئر ہوتے ہیں تو وہ آبجیکٹس بناتے ہیں۔', 'د ټولګي ډول متغیر شی بلل کېږي. په C++ کې کله چې د ټولګي ډول متغیرونه اعلان شي، شیان جوړوي.'),
     ('The attributes of a real world objects are called data members.', 'حقیقی دنیا کی اشیا کی خصوصیات ڈیٹا ممبرز کہلاتی ہیں۔', 'د ریښتینې نړۍ د شیانو ځانګړنې د ډېټا غړي بلل کېږي.'),
     ('The functions declared or defined inside the body of the class are called member functions.', 'کلاس کے جسم کے اندر ڈکلیئر یا بیان کیے گئے فنکشنز ممبر فنکشنز کہلاتے ہیں۔', 'د ټولګي د بدنې دننه اعلان یا تعریف شوي فنکشنونه غړي فنکشنونه بلل کېږي.'),
     ('Access specifiers determine that which member of a class is accessible by which member of the class/program.', 'ایکسس اسپیسیفائرز طے کرتے ہیں کہ کلاس کا کون سا ممبر کلاس/پروگرام کے کس ممبر کے لیے قابلِ رسائی ہے۔', 'د لاسرسي ټاکونکي ټاکي چې د ټولګي کوم غړی د ټولګي/پروګرام د کوم غړي لپاره د لاسرسي وړ دی.'),
     ('private access specifier tells the compiler that the members defined in a class by preceding this specifier are accessible only within the class and its friend function.', 'private ایکسس اسپیسیفائر کمپائلر کو بتاتا ہے کہ کلاس میں اس اسپیسیفائر کے بعد بیان کیے گئے اراکین صرف کلاس اور اس کے friend فنکشن کے اندر قابلِ رسائی ہیں۔', 'private د لاسرسي ټاکونکی کمپایلر ته وايي چې په ټولګي کې د دې ټاکونکي وروسته تعریف شوي غړي یوازې د ټولګي او د هغه د friend فنکشن دننه د لاسرسي وړ دي.'),
     ('public members are accessible from anywhere where the object is visible.', 'public اراکین ہر اس جگہ سے قابلِ رسائی ہیں جہاں آبجیکٹ نظر آتا ہو۔', 'public غړي له هر هغه ځایه د لاسرسي وړ دي چې شی پکې ښکاري.'),
     ('Data Hiding is the concept in which the members of a class are protected against illegal access from outside the class.', 'ڈیٹا ہائیڈنگ وہ تصور ہے جس میں کلاس کے اراکین کو کلاس کے باہر سے غیر قانونی رسائی سے محفوظ رکھا جاتا ہے۔', 'د ډېټا پټول هغه مفهوم دی چې پکې د ټولګي غړي له ټولګي بهر د ناقانونه لاسرسي څخه ساتل کېږي.'),
     ('A constructor is a special kind of class member function that is executed when an object of the class is instantiated.', 'کنسٹرکٹر کلاس کا ایک خاص قسم کا ممبر فنکشن ہے جو کلاس کا آبجیکٹ بننے پر چلتا ہے۔', 'جوړوونکی د ټولګي یو ځانګړی ډول غړی فنکشن دی چې د ټولګي د شي د جوړېدو پر مهال اجرا کېږي.'),
     ('Destructors are special member functions having the same name as that of the class with a tiled symbol ~ and executed when an object is destroyed.', 'ڈسٹرکٹرز خاص ممبر فنکشنز ہیں جن کا نام ٹلڈا نشان ~ کے ساتھ کلاس کے نام جیسا ہوتا ہے اور آبجیکٹ ختم ہونے پر چلتے ہیں۔', 'ړنګوونکي ځانګړي غړي فنکشنونه دي چې د ټیلډ نښې ~ سره د ټولګي په څېر نوم لري او د شي د ړنګېدو پر مهال اجرا کېږي.'),
     ('To access members of a class, dot operator (.) is used with the member name.', 'کلاس کے اراکین تک رسائی کے لیے ممبر کے نام کے ساتھ ڈاٹ آپریٹر (.) استعمال ہوتا ہے۔', 'د ټولګي غړو ته د لاسرسي لپاره د غړي له نوم سره د ټکي چلونکی (.) کارېږي.'),
     ('The phenomenon of creating new classes from existing classes is called inheritance.', 'موجودہ کلاسز سے نئی کلاسز بنانے کا عمل وراثت کہلاتا ہے۔', 'له موجودو ټولګیو د نویو ټولګیو د جوړولو پدیده میراث بلل کېږي.'),
     ('Polymorphism is the ability to use an operator or function in multiple ways.', 'پولی مورفزم کسی آپریٹر یا فنکشن کو متعدد طریقوں سے استعمال کرنے کی صلاحیت ہے۔', 'پولي‌مورفیزم د یوه چلونکي یا فنکشن په ډېرو لارو د کارولو وړتیا ده.')])
    sm = BOOK.record(s, 'cs12-u8-summary', 'Unit 8 summary', 'یونٹ 8: خلاصہ', '۸ څپرکی: لنډیز', 133, [255])
    BOOK.save(133, [(8, tx), (8, sm)], issues=[{'id': 'cs12-pdf133', 'unit': 8, 'printedPage': 255,
               'description': 'Summary: “The attributes of a real world objects”, “with a tiled symbol ~”, “determine that which member … is accessible by which member”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 126
    {126: p126, 127: p127, 128: p128, 129: p129, 130: p130, 131: p131, 132: p132, 133: p133}[n]()
