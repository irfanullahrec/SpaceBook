"""Computer Science XII PDF120–125: pp.228–239 — introduction, 8.1 classes, 8.1.1 class and object (CRectangle, Test), accessing members,
8.1.2 members (Date), 8.1.3 access specifiers (private/public programs), 8.1.4 data hiding, Table 8.1, 8.1.5 constructor (begins).
Run: python class12_cs_page120.py N (120–125)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u8-text-{n}', f'Unit 8 text ({n})', f'یونٹ 8 — متن ({n})', f'۸ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p120():
    t = Builder()
    P = t.p
    t.h('INTRODUCTION', 'تعارف', 'سریزه')
    P('In structural or traditional programming, the data and actions are considered as two separate entities which cannot provide a very intuitive representation of real world objects and phenomenon. To eliminate this limitation, Object-Oriented Programming (OOP) concept was introduced which combines data and actions together in one package called class. This allows programmers to write programs in more modular fashion to make them easier to understand. This modularization also provides a higher degree of code-reusability. Object-oriented programming also brings several other useful concepts into the field of programming which are: data hiding, inheritance, encapsulation, abstraction, and polymorphism. This Unit is focused on these features of OOP.',
      'ساختی یا روایتی پروگرامنگ میں ڈیٹا اور اعمال کو دو الگ وجود سمجھا جاتا ہے جو حقیقی دنیا کی اشیا اور مظاہر کی بہت فطری نمائندگی فراہم نہیں کر سکتے۔ اس حد کو ختم کرنے کے لیے آبجیکٹ اورینٹڈ پروگرامنگ (OOP) کا تصور متعارف کرایا گیا جو ڈیٹا اور اعمال کو ایک پیکیج میں یکجا کرتا ہے جسے کلاس کہتے ہیں۔ اس سے پروگرامرز زیادہ ماڈیولر انداز میں پروگرام لکھ سکتے ہیں تاکہ انھیں سمجھنا آسان ہو۔ یہ ماڈیولرائزیشن کوڈ کے دوبارہ استعمال کا زیادہ درجہ بھی فراہم کرتی ہے۔ آبجیکٹ اورینٹڈ پروگرامنگ پروگرامنگ کے میدان میں کئی دوسرے مفید تصورات بھی لاتی ہے جو یہ ہیں: ڈیٹا ہائیڈنگ، وراثت، انکیپسولیشن، ایبسٹریکشن اور پولی مورفزم۔ یہ یونٹ OOP کی انھی خصوصیات پر مرکوز ہے۔',
      'په جوړښتي یا دودیز پروګرام‌سازۍ کې ډېټا او کړنې دوه جلا وجودونه ګڼل کېږي چې د ریښتینې نړۍ د شیانو او پدیدو ډېره طبیعي ښودنه نه شي برابرولی. د دې محدودیت د لرې کولو لپاره د شیانو ته متوجه پروګرام‌سازۍ (OOP) مفهوم معرفي شو چې ډېټا او کړنې په یوه بسته کې یوځای کوي چې ټولګی (class) بلل کېږي. دا پروګرام جوړوونکو ته اجازه ورکوي چې پروګرامونه په ډېر ماډیولي ډول ولیکي ترڅو پوهېدل یې اسانه شي. دا ماډیولي کول د کوډ د بیا کارونې لوړه کچه هم برابروي. د شیانو ته متوجه پروګرام‌سازي د پروګرام‌سازۍ ډګر ته نور ګټور مفاهیم هم راوړي چې دا دي: د ډېټا پټول، میراث، کپسول‌کول، تجرید او پولي‌مورفیزم. دا څپرکی د OOP په دې ځانګړتیاوو تمرکز لري.')
    t.h('8.1 Classes', '8.1 کلاسز', '۸.۱ ټولګي')
    P('Class is one of the main features of Object Oriented Programming language. It combines both data and functions into units or packages and makes the programs modularized.', 'کلاس آبجیکٹ اورینٹڈ پروگرامنگ زبان کی بنیادی خصوصیات میں سے ایک ہے۔ یہ ڈیٹا اور فنکشنز دونوں کو اکائیوں یا پیکیجز میں یکجا کرتی ہے اور پروگراموں کو ماڈیولر بناتی ہے۔', 'ټولګی د شیانو ته متوجه پروګرامي ژبې له اصلي ځانګړتیاوو یو دی. ډېټا او فنکشنونه دواړه په واحدونو یا بستو کې یوځای کوي او پروګرامونه ماډیولي کوي.')
    t.h('8.1.1 Class and object', '8.1.1 کلاس اور آبجیکٹ', '۸.۱.۱ ټولګی او شی')
    t.h('a. Class', 'a. کلاس', 'a. ټولګی')
    P('A class consists of both attributes of real world objects and functions that perform operations on these attributes. The attributes are called data members and the operations are called member functions. It is an important feature of object oriented programming (OOP) and is used to hold both data and functions, of real world objects, tightly into a single package.',
      'کلاس حقیقی دنیا کی اشیا کی خصوصیات اور ان خصوصیات پر عمل کرنے والے فنکشنز دونوں پر مشتمل ہوتی ہے۔ خصوصیات کو ڈیٹا ممبرز اور اعمال کو ممبر فنکشنز کہتے ہیں۔ یہ آبجیکٹ اورینٹڈ پروگرامنگ (OOP) کی اہم خصوصیت ہے اور حقیقی دنیا کی اشیا کے ڈیٹا اور فنکشنز دونوں کو مضبوطی سے ایک پیکیج میں رکھنے کے لیے استعمال ہوتی ہے۔',
      'ټولګی د ریښتینې نړۍ د شیانو ځانګړنې او هغه فنکشنونه چې پر دې ځانګړنو عملیې کوي، دواړه لري. ځانګړنې د ډېټا غړي او عملیې غړي فنکشنونه بلل کېږي. دا د شیانو ته متوجه پروګرام‌سازۍ (OOP) مهمه ځانګړتیا ده او د ریښتینې نړۍ د شیانو ډېټا او فنکشنونه دواړه په یوه بسته کې په کلکه ساتي.')
    P('Classes are generally declared using the keyword class, with the following format:', 'کلاسز عموماً کلیدی لفظ class سے درج ذیل شکل میں ڈکلیئر کی جاتی ہیں:', 'ټولګي عموماً د class کلیدي کلمې په مرسته په لاندې بڼه اعلانېږي:')
    code(t, '''class class_name
{
access_specifier_1:
member1;
access_specifier_2: // Body of the class
member2;
...
};''')
    P('Here, class_name is a valid identifier for the class which is followed by the body of the class that is enclosed in pair of braces. The body of the class consists of:', 'یہاں class_name کلاس کا ایک درست شناخت کنندہ ہے جس کے بعد کلاس کا جسم آتا ہے جو بریسز کے جوڑے میں بند ہوتا ہے۔ کلاس کا جسم ان پر مشتمل ہوتا ہے:', 'دلته class_name د ټولګي لپاره یو سم پېژندونکی دی چې وروسته یې د ټولګي بدنه راځي چې د لوړو قوسونو په جوړه کې تړل شوې. د ټولګي بدنه دا لري:')
    t.group('list', [('Data members', 'ڈیٹا ممبرز', 'د ډېټا غړي'), ('Member functions', 'ممبر فنکشنز', 'غړي فنکشنونه')])
    P('Data members and member functions are used with the access specifiers. An access specifier is one of the three types:', 'ڈیٹا ممبرز اور ممبر فنکشنز ایکسس اسپیسیفائرز کے ساتھ استعمال ہوتے ہیں۔ ایکسس اسپیسیفائر تین اقسام میں سے ایک ہوتا ہے:', 'د ډېټا غړي او غړي فنکشنونه د لاسرسي ټاکونکو سره کارېږي. د لاسرسي ټاکونکی له درېیو ډولونو یو دی:')
    t.group('list', [('private', 'private', 'private'), ('public', 'public', 'public'), ('protected', 'protected', 'protected')])
    P('A C++ class ends with a semicolon (;). Consider the following example to understand the concept of class.', 'C++ کلاس سیمی کولن (;) پر ختم ہوتی ہے۔ کلاس کا تصور سمجھنے کے لیے درج ذیل مثال پر غور کریں۔', 'د C++ ټولګی په سیمي‌کولن (;) پای ته رسېږي. د ټولګي د مفهوم د پوهېدو لپاره لاندې بېلګې ته پام وکړئ.')
    code(t, '''// Class declaration example
class CRectangle
{
private:
int x, y; // declaration of data members
public:
void set_values (int a, int b); // declaration of member function
int area (); // declaration of member function
};''')
    P('The above statements declare a class named CRectangle. This class contains four members:', 'اوپر کے بیانات CRectangle نامی کلاس ڈکلیئر کرتے ہیں۔ اس کلاس کے چار اراکین ہیں:', 'پورته بیانونه د CRectangle په نوم ټولګی اعلانوي. دا ټولګی څلور غړي لري:')
    BOOK.save(120, [(8, rec(t, 1, 120, [228, 229], 'The class format begins at the foot of p.228 and ends on p.229; it is given whole.'))])


def p121():
    t = Builder()
    P = t.p
    P('Two data members x and y of type int with private access specifier and two member functions with public access; set_values () and area (). In this example, only declarations for the member functions has given and not their definitions.',
      'int قسم کے دو ڈیٹا ممبرز x اور y، private ایکسس اسپیسیفائر کے ساتھ، اور public رسائی والے دو ممبر فنکشنز set_values () اور area ()۔ اس مثال میں ممبر فنکشنز کی صرف ڈکلیریشنز دی گئی ہیں، ان کی تعریفیں نہیں۔',
      'د int ډول دوه د ډېټا غړي x او y د private لاسرسي ټاکونکي سره، او د public لاسرسي دوه غړي فنکشنونه set_values () او area (). په دې بېلګه کې د غړو فنکشنونو یوازې اعلانونه ورکړل شوي، تعریفونه یې نه.')
    t.h('b. Object', 'b. آبجیکٹ', 'b. شی')
    P('A variable of type class is called object. In C++, when we declare a variable of type class, we call it instantiating the class and the variable itself is called an instance or object of that class. Object is of great importance in OOP, because, a class cannot be used without creating its object. The general syntax for creating an object of a class is given below.',
      'کلاس قسم کا ویری ایبل آبجیکٹ کہلاتا ہے۔ C++ میں جب ہم کلاس قسم کا ویری ایبل ڈکلیئر کرتے ہیں تو اسے کلاس کا انسٹینشی ایٹ کرنا کہتے ہیں اور خود ویری ایبل اس کلاس کا انسٹینس یا آبجیکٹ کہلاتا ہے۔ OOP میں آبجیکٹ کی بڑی اہمیت ہے کیونکہ کلاس کو اس کا آبجیکٹ بنائے بغیر استعمال نہیں کیا جا سکتا۔ کلاس کا آبجیکٹ بنانے کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے۔',
      'د ټولګي ډول متغیر شی (object) بلل کېږي. په C++ کې کله چې د ټولګي ډول متغیر اعلان کړو، دې ته د ټولګي نمونه‌جوړول وایو او پخپله متغیر د هغه ټولګي نمونه یا شی بلل کېږي. په OOP کې شی ډېر اهمیت لري ځکه ټولګی د خپل شي له جوړولو پرته نه شي کارېدای. د یوه ټولګي د شي د جوړولو عمومي بڼه لاندې ورکړل شوې.')
    code(t, 'Class_name Object_name;')
    P('Thus, for the above class CRectangle, the object can be created as follows:', 'یوں اوپر کی کلاس CRectangle کے لیے آبجیکٹ یوں بنایا جا سکتا ہے:', 'نو د پورته CRectangle ټولګي لپاره شی داسې جوړېدای شي:')
    code(t, 'CRectangle R1;')
    P('We can also create more than one objects in a single statement like:', 'ہم ایک ہی بیان میں ایک سے زیادہ آبجیکٹس بھی بنا سکتے ہیں جیسے:', 'موږ کولی شو په یوه بیان کې له یوه ډېر شیان هم جوړ کړو لکه:')
    code(t, 'CRectangle R1, R2, R3;')
    P('Here, R1, R2, R3 are the objects of the same class CRectangle that share the same data member and member functions. The definition of a class does not occupy any memory. It only defines what the class looks like. In order to use a class, a variable of that class type must be declared. When an object is created then memory is set aside for all the data members and member functions of that class.',
      'یہاں R1، R2، R3 ایک ہی کلاس CRectangle کے آبجیکٹس ہیں جو ایک جیسے ڈیٹا ممبر اور ممبر فنکشنز رکھتے ہیں۔ کلاس کی تعریف کوئی میموری نہیں لیتی۔ یہ صرف بتاتی ہے کہ کلاس کیسی ہے۔ کلاس استعمال کرنے کے لیے اس کلاس قسم کا ویری ایبل ڈکلیئر کرنا ضروری ہے۔ جب آبجیکٹ بنتا ہے تو اس کلاس کے تمام ڈیٹا ممبرز اور ممبر فنکشنز کے لیے میموری مختص ہو جاتی ہے۔',
      'دلته R1، R2، R3 د یو ټولګي CRectangle شیان دي چې ورته د ډېټا غړی او غړي فنکشنونه شریکوي. د ټولګي تعریف هېڅ حافظه نه نیسي. یوازې ټاکي چې ټولګی څنګه ښکاري. د ټولګي د کارولو لپاره باید د هغه ټولګي ډول متغیر اعلان شي. کله چې شی جوړ شي، د هغه ټولګي د ټولو ډېټا غړو او غړو فنکشنونو لپاره حافظه ځانګړې کېږي.')
    P('The following program demonstrates the concept of class in C++ and creation of object.', 'درج ذیل پروگرام C++ میں کلاس کا تصور اور آبجیکٹ کی تخلیق واضح کرتا ہے۔', 'لاندې پروګرام په C++ کې د ټولګي مفهوم او د شي جوړول ښيي.')
    code(t, '''#include <iostream.h>
#include <conio.h>
class Test
{
public:
void print()
{
cout<< “Welcome to the class”;
}
}; //End of the class Test
int main()
{
Test t1; // Object creation
t1.print();//call to print() function
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'Welcome to the class')
    t.h('Accessing Members of a Class', 'کلاس کے اراکین تک رسائی', 'د ټولګي غړو ته لاسرسی')
    P('Data members and member functions of a class can be accessed in the main program (i.e. main function) by using the object of that class, and dot operator (.) followed by the name of the member i.e. object member.',
      'کلاس کے ڈیٹا ممبرز اور ممبر فنکشنز تک main پروگرام (یعنی main فنکشن) میں اس کلاس کے آبجیکٹ اور ڈاٹ آپریٹر (.) کے بعد ممبر کا نام لکھ کر یعنی object member سے رسائی ہو سکتی ہے۔',
      'د ټولګي د ډېټا غړو او غړو فنکشنونو ته په main پروګرام (یعنې main فنکشن) کې د هغه ټولګي د شي او د ټکي چلونکي (.) وروسته د غړي د نوم په لیکلو، یعنې object member، لاسرسی کېدای شي.')
    P('For example, in the above program, the member function print() is accessed by using the following statement:', 'مثلاً اوپر کے پروگرام میں ممبر فنکشن print() تک درج ذیل بیان سے رسائی کی گئی ہے:', 'د بېلګې په توګه په پورته پروګرام کې print() غړي فنکشن ته د لاندې بیان په مرسته لاسرسی شوی:')
    code(t, 't1.print ();')
    P('Similarly a data member can be accessed as object_name data member with private data member and public functions.', 'اسی طرح ڈیٹا ممبر تک private ڈیٹا ممبر اور public فنکشنز کے ساتھ object_name data member کے طور پر رسائی ہو سکتی ہے۔', 'همداراز د ډېټا غړي ته د private ډېټا غړي او public فنکشنونو سره د object_name data member په توګه لاسرسی کېدای شي.')
    P('The following program implement the class CRectangle discussed above.', 'درج ذیل پروگرام اوپر زیرِ بحث کلاس CRectangle کو نافذ کرتا ہے۔', 'لاندې پروګرام پورته یاد شوی CRectangle ټولګی پلي کوي.')
    BOOK.save(121, [(8, rec(t, 2, 121, [230, 231], 'The Test program begins at the foot of p.230 and ends on p.231; it is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf121', 'unit': 8, 'printedPage': 231,
                       'description': 'p.230 “only declarations … has given”, “more than one objects”; p.231 “The following program implement the class”, “object_name data member” (dot omitted). Retained as printed.'}])


def p122():
    t = Builder()
    P = t.p
    code(t, '''#include <iostream.h>
#include <conio.h>
class CRectangle
{
private:
int X, Y;
public:
void set_values (int a,int b)
{
X=a;
Y=b;
}
int area()
{
cout<< “area of the rectangle="<<(X*Y);
}
}; //End of class
int main()
{
CRectangle R1; // Object creation
R1.set_values(44,22);//call to set_values function
R1.area(); // call to area function
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'Area of the rectangle=968')
    t.h('8.1.2 Members of a class', '8.1.2 کلاس کے اراکین', '۸.۱.۲ د ټولګي غړي')
    P('Class has two members; data members and member functions.', 'کلاس کے دو اراکین ہیں؛ ڈیٹا ممبرز اور ممبر فنکشنز۔', 'ټولګی دوه غړي لري؛ د ډېټا غړي او غړي فنکشنونه.')
    t.h('a. Data member', 'a. ڈیٹا ممبر', 'a. د ډېټا غړی')
    P('The attributes of a class are called data members. Mostly, data members are declared under the private access specifier to make them private to the class in which they are used. Data members can also be used under public access specifier. For ech object of a class, a separate copy of the data members is created in memory.',
      'کلاس کی خصوصیات ڈیٹا ممبرز کہلاتی ہیں۔ زیادہ تر ڈیٹا ممبرز private ایکسس اسپیسیفائر کے تحت ڈکلیئر کیے جاتے ہیں تاکہ وہ اس کلاس کے لیے نجی رہیں جس میں استعمال ہوتے ہیں۔ ڈیٹا ممبرز public ایکسس اسپیسیفائر کے تحت بھی استعمال ہو سکتے ہیں۔ کلاس کے ہر آبجیکٹ کے لیے میموری میں ڈیٹا ممبرز کی الگ نقل بنتی ہے۔',
      'د ټولګي ځانګړنې د ډېټا غړي بلل کېږي. ډېری وخت د ډېټا غړي د private لاسرسي ټاکونکي لاندې اعلانېږي ترڅو د هغه ټولګي لپاره شخصي وي چې پکې کارېږي. د ډېټا غړي د public لاسرسي ټاکونکي لاندې هم کارېدای شي. د ټولګي د هر شي لپاره په حافظه کې د ډېټا غړو جلا کاپي جوړېږي.')
    t.h('b. Member function', 'b. ممبر فنکشن', 'b. غړی فنکشن')
    P('The functions declared or defined inside the body of the class are called member functions. These member functions are usually written under the public access specifier to operate on the data members of the class. Member functions can also be written in the private area of the class but the practice is to write them in the public area.',
      'کلاس کے جسم کے اندر ڈکلیئر یا بیان کیے گئے فنکشنز ممبر فنکشنز کہلاتے ہیں۔ یہ ممبر فنکشنز عموماً کلاس کے ڈیٹا ممبرز پر عمل کرنے کے لیے public ایکسس اسپیسیفائر کے تحت لکھے جاتے ہیں۔ ممبر فنکشنز کلاس کے private حصے میں بھی لکھے جا سکتے ہیں لیکن رواج انھیں public حصے میں لکھنے کا ہے۔',
      'هغه فنکشنونه چې د ټولګي د بدنې دننه اعلان یا تعریف شي، غړي فنکشنونه بلل کېږي. دا غړي فنکشنونه عموماً د ټولګي پر ډېټا غړو د عملیې لپاره د public لاسرسي ټاکونکي لاندې لیکل کېږي. غړي فنکشنونه د ټولګي په private برخه کې هم لیکل کېدای شي خو دود دا دی چې په public برخه کې ولیکل شي.')
    code(t, '''// Example of a class with its members as public
#include<iostream.h>
#include<conio.h>
class Date
{
public:
int Month;
int Day;
int Year;
void SetDate (int nMonth, int nDay, int nYear)
{
Month = nMonth;
Day = nDay;
Year = nYear;
}
void ShowDate()
{
cout<<"Month of birth:"<<Month<<endl;
cout<<"Day of birth:"<<Day<<endl;
cout<<"Year of birth:"<<Year;
}
};
int main()
{
Date d1; // Object creation
d1.SetDate(01,01,2012);//call to SetDate function
d1.ShowDate(); // call to ShowDate function
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Month of birth: 01
Day of birth: 01
Year of birth: 2012''')
    BOOK.save(122, [(8, rec(t, 3, 122, [232, 233, 234], 'The Date program begins on p.233 and ends on p.234 (PDF123); it is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf122', 'unit': 8, 'printedPage': 232,
                       'description': 'area() is declared int but returns nothing; the program prints “area of the rectangle=” while the output shows “Area of the rectangle=968”; p.233 “For ech object”; the Date output shows “01” although the program would print 1. Retained as printed.'}])


def p123():
    t = Builder()
    P = t.p
    t.h('8.1.3 Access specifiers', '8.1.3 ایکسس اسپیسیفائرز', '۸.۱.۳ د لاسرسي ټاکونکي')
    P('Access specifiers are the determiners that determine which member of a class is accessible in which part of the class/program. The most commonly used access specifiers in C++ are:', 'ایکسس اسپیسیفائرز وہ تعین کنندہ ہیں جو طے کرتے ہیں کہ کلاس کا کون سا ممبر کلاس/پروگرام کے کس حصے میں قابلِ رسائی ہے۔ C++ میں سب سے عام ایکسس اسپیسیفائرز یہ ہیں:', 'د لاسرسي ټاکونکي هغه ټاکونکي دي چې ټاکي د ټولګي کوم غړی د ټولګي/پروګرام په کومه برخه کې د لاسرسي وړ دی. په C++ کې تر ټولو عام د لاسرسي ټاکونکي دا دي:')
    t.group('list', [('private access specifier', 'private ایکسس اسپیسیفائر', 'private د لاسرسي ټاکونکی'), ('public access specifier', 'public ایکسس اسپیسیفائر', 'public د لاسرسي ټاکونکی')])
    t.h('a. private access specifier', 'a. private ایکسس اسپیسیفائر', 'a. private د لاسرسي ټاکونکی')
    P('private access specifier tells the compiler that the members defined in a class by preceding this specifier are accessible only within the class and its friend function. private members are not accessible outside the class.', 'private ایکسس اسپیسیفائر کمپائلر کو بتاتا ہے کہ کلاس میں اس اسپیسیفائر کے بعد بیان کیے گئے اراکین صرف کلاس اور اس کے friend فنکشن کے اندر قابلِ رسائی ہیں۔ private اراکین کلاس کے باہر قابلِ رسائی نہیں ہوتے۔', 'private د لاسرسي ټاکونکی کمپایلر ته وايي چې په ټولګي کې د دې ټاکونکي وروسته تعریف شوي غړي یوازې د ټولګي او د هغه د friend فنکشن دننه د لاسرسي وړ دي. private غړي له ټولګي بهر د لاسرسي وړ نه دي.')
    P('A program explaining the use of private data members within and outside the class is given below.', 'کلاس کے اندر اور باہر private ڈیٹا ممبرز کا استعمال واضح کرنے والا پروگرام ذیل میں دیا گیا ہے۔', 'یو پروګرام چې د ټولګي دننه او بهر د private ډېټا غړو کارونه تشریح کوي لاندې ورکړل شوی.')
    code(t, '''#include<iostream.h>
#include<conio.h>
class Date
{
private:
int Day;
int Month;
int Year;
public:
void SetDate(int nDay, int nMonth, int nYear)
{
Day = nDay;        ┐
Month=nMonth;      ├ Okay: because private members are accessible within the class
Year = nYear;      ┘
cout<< “Today’s date is: "<<Day<< “/"<<Month<< “/"<<Year;
}
};
int main()
{
Date cDate;
//cDate.Day = 10;      ┐
//cDate.Month = 01;    ├ Invalid: because private members cannot be accessible from outside the class
//cDate.Year = 2012;   ┘
cDate.SetDate(15, 01, 2012); //Valid
getch();
return 0;
}''')
    BOOK.save(123, [(8, rec(t, 4, 123, [234, 235], 'The top of p.234 (end of the Date program and its output) is recorded with PDF122. The two callout boxes on p.235 are reproduced as text markers beside the bracketed lines.'))],
              issues=[{'id': 'cs12-pdf123', 'unit': 8, 'printedPage': 235,
                       'description': 'Callout “private members cannot be accessible from outside the class”; the program uses curly opening quotes. Retained as printed.'}])


def p124():
    t = Builder()
    P = t.p
    t.h('b. public access specifier', 'b. public ایکسس اسپیسیفائر', 'b. public د لاسرسي ټاکونکی')
    P('public members are accessible from anywhere where the object is visible i.e. within the class, in the derived classes and in the main function.', 'public اراکین ہر اس جگہ سے قابلِ رسائی ہیں جہاں آبجیکٹ نظر آتا ہو یعنی کلاس کے اندر، ماخوذ کلاسز میں اور main فنکشن میں۔', 'public غړي له هر هغه ځایه د لاسرسي وړ دي چې شی پکې ښکاري، یعنې د ټولګي دننه، په مشتق ټولګیو کې او په main فنکشن کې.')
    P('Consider the following program to demonstrate the visibility of public members of a class.', 'کلاس کے public اراکین کی نمائش واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د ټولګي د public غړو د لیدلو د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''// public access specifier example 1
#include<iostream.h>
#include<conio.h>
class PublicTest
{
public:
int X=10; // Public data member
void showPublic() // Public member function
{
cout<< “X= "<<X;
}
};
int main()
{
PublicTest PT1; //PT1 is an object of class PublicTest
PT1.X; //access private data members
PT1.showPublic(); // access public member function
getch();
return 0;
}''')
    P('In the above program, the class PublicTest is defined which comprise of one data member X and one member function showPublic() in its public part. The data member is accessed within the member function showPublic() and outside the class, i.e. in main() function, without generating any error message. Similarly, the member function showPublic() is also accessed in main() function.',
      'اوپر کے پروگرام میں کلاس PublicTest بیان کی گئی ہے جس کے public حصے میں ایک ڈیٹا ممبر X اور ایک ممبر فنکشن showPublic() ہے۔ ڈیٹا ممبر تک ممبر فنکشن showPublic() کے اندر اور کلاس کے باہر یعنی main() فنکشن میں کسی خرابی کے پیغام کے بغیر رسائی ہوتی ہے۔ اسی طرح ممبر فنکشن showPublic() تک بھی main() فنکشن میں رسائی ہوتی ہے۔',
      'په پورته پروګرام کې PublicTest ټولګی تعریف شوی چې په public برخه کې یې یو د ډېټا غړی X او یو غړی فنکشن showPublic() دی. د ډېټا غړي ته د showPublic() غړي فنکشن دننه او له ټولګي بهر، یعنې په main() فنکشن کې، پرته له تېروتنې پیغامه لاسرسی کېږي. همداراز showPublic() غړي فنکشن ته هم په main() فنکشن کې لاسرسی کېږي.')
    P('If no access specifier is mentioned in a class for a member then it will combined as private by default.', 'اگر کلاس میں کسی ممبر کے لیے کوئی ایکسس اسپیسیفائر نہ لکھا ہو تو وہ بطورِ طے شدہ private شمار ہوگا۔', 'که په ټولګي کې د یوه غړي لپاره هېڅ د لاسرسي ټاکونکی ونه لیکل شي، په ډیفالټ ډول به private وګڼل شي.')
    P('The following program demonstrates private and public access specifier.', 'درج ذیل پروگرام private اور public ایکسس اسپیسیفائر واضح کرتا ہے۔', 'لاندې پروګرام private او public د لاسرسي ټاکونکي ښيي.')
    code(t, '''#include<iostream.h>
#include<conio.h>
class Access
{
int A; // private by default
void GetA() // private by default
{
cout<<"I am private member accessible only through public member function"<<endl;
}
public:
int B; // public
void GetB()
{
GetA();
cout<<"I am B in public"<<endl;
}
};
int main()
{
Access cAccess; //cAccess is an object of the class Access
//cAccess.A = 2; // WRONG because A is private data member
//cAccess.GetA(); //WRONG because GetA() is private member function
cAccess.B=10; // Okay because B is public data member
cAccess.GetB(); // Okay because GetB() is public member function
getch();
return 0;
}''')
    P('The above program explains the scope (or accessibility) of the private and public data members and member functions in detail. Also, comments are added with each line of code in main() program for the explanation of its accessibility level.', 'اوپر کا پروگرام private اور public ڈیٹا ممبرز اور ممبر فنکشنز کا دائرہ (یا رسائی) تفصیل سے واضح کرتا ہے۔ نیز main() پروگرام میں کوڈ کی ہر لائن کے ساتھ اس کی رسائی کی سطح کی وضاحت کے لیے تبصرے شامل کیے گئے ہیں۔', 'پورته پروګرام د private او public ډېټا غړو او غړو فنکشنونو ساحه (یا د لاسرسي وړتیا) په تفصیل تشریح کوي. همداراز په main() پروګرام کې د کوډ له هرې کرښې سره د هغې د لاسرسي د کچې د تشریح لپاره تبصرې ورزیاتې شوې.')
    P('The output of the program is:', 'پروگرام کا آؤٹ پٹ یہ ہے:', 'د پروګرام وتنه دا ده:')
    code(t, '''I am private member accessible only through public member function
I am B in public''')
    BOOK.save(124, [(8, rec(t, 5, 124, [236, 237, 238], 'The Access program runs from p.237 to p.238 (PDF125) and is given whole with its explanation and output.'))],
              issues=[{'id': 'cs12-pdf124', 'unit': 8, 'printedPage': 236,
                       'description': 'The PublicTest program comments “access private data members” for the public member X and initializes int X=10 inside the class; p.236 “which comprise of”; p.237 “it will combined as private by default”. Retained as printed.'}])


def p125():
    t = Builder()
    P = t.p
    t.h('8.1.4 Data hiding', '8.1.4 ڈیٹا ہائیڈنگ', '۸.۱.۴ د ډېټا پټول')
    P('Data Hiding is an important concept of C++ programming language in which the members of a class are protected against illegal access from outside the class. In C language, struct is used but it cannot hide data of its data members. Whereas in C++, we got the facility of hiding data using different access levels: private, protected, public in classes.',
      'ڈیٹا ہائیڈنگ C++ پروگرامنگ زبان کا ایک اہم تصور ہے جس میں کلاس کے اراکین کو کلاس کے باہر سے غیر قانونی رسائی سے محفوظ رکھا جاتا ہے۔ C زبان میں struct استعمال ہوتا ہے لیکن یہ اپنے ڈیٹا ممبرز کا ڈیٹا چھپا نہیں سکتا۔ جبکہ C++ میں ہمیں کلاسز میں مختلف رسائی کی سطحوں private، protected، public کے ذریعے ڈیٹا چھپانے کی سہولت ملی۔',
      'د ډېټا پټول د C++ پروګرامي ژبې مهم مفهوم دی چې پکې د ټولګي غړي له ټولګي بهر د ناقانونه لاسرسي څخه ساتل کېږي. په C ژبه کې struct کارېږي خو د خپلو ډېټا غړو ډېټا نه شي پټولی. په داسې حال کې چې په C++ کې موږ ته په ټولګیو کې د لاسرسي د بېلو کچو private، protected، public په مرسته د ډېټا د پټولو اسانتیا ترلاسه شوه.')
    P('Private data members and member functions can only be accessed by the members of the same class defining them and cannot be accessed from outside the class. Similarly, protected members (data members and member functions) of a class can be accessed only by the class defining them and its derived classes. By using friend function, the private and protected members (data members and member functions) of a class can also be accessed. Except these, private and protected members are not accessible anywhere else and thus provide the facility of data hiding. The public access specifier has global access and can be accessed within the same class, derived classes and main() program.',
      'private ڈیٹا ممبرز اور ممبر فنکشنز تک صرف انھیں بیان کرنے والی کلاس کے اراکین رسائی کر سکتے ہیں اور کلاس کے باہر سے رسائی نہیں ہو سکتی۔ اسی طرح کلاس کے protected اراکین (ڈیٹا ممبرز اور ممبر فنکشنز) تک صرف انھیں بیان کرنے والی کلاس اور اس کی ماخوذ کلاسز رسائی کر سکتی ہیں۔ friend فنکشن کے ذریعے کلاس کے private اور protected اراکین (ڈیٹا ممبرز اور ممبر فنکشنز) تک بھی رسائی ہو سکتی ہے۔ ان کے علاوہ private اور protected اراکین کہیں اور قابلِ رسائی نہیں اور یوں ڈیٹا ہائیڈنگ کی سہولت فراہم کرتے ہیں۔ public ایکسس اسپیسیفائر کی رسائی عالمی ہے اور اسی کلاس، ماخوذ کلاسز اور main() پروگرام میں رسائی ہو سکتی ہے۔',
      'private د ډېټا غړو او غړو فنکشنونو ته یوازې د هغه ټولګي غړي لاسرسی کولی شي چې تعریف کړي یې دي او له ټولګي بهر لاسرسی نه کېږي. همداراز د ټولګي protected غړو (د ډېټا غړي او غړي فنکشنونه) ته یوازې تعریفوونکی ټولګی او د هغه مشتق ټولګي لاسرسی کولی شي. د friend فنکشن په کارولو د ټولګي private او protected غړو ته هم لاسرسی کېدای شي. له دې پرته private او protected غړي بل هېڅ ځای د لاسرسي وړ نه دي او په دې توګه د ډېټا د پټولو اسانتیا برابروي. public د لاسرسي ټاکونکی نړیوال لاسرسی لري او په همغه ټولګي، مشتق ټولګیو او main() پروګرام کې لاسرسی ورته کېدای شي.')
    P('The following table shows the level of hiding members of a class.', 'درج ذیل جدول کلاس کے اراکین کو چھپانے کی سطح دکھاتا ہے۔', 'لاندې جدول د ټولګي د غړو د پټولو کچه ښيي.')
    H = ['Access', 'Public', 'Protected', 'Private']
    R = [['Access of members (data, functions) in the same class', 'Yes', 'Yes', 'Yes'],
         ['Access of members (data, functions) in the derived classes', 'Yes', 'Yes', 'No'],
         ['Access of members (data, functions) from outside the class i.e. from main()', 'Yes', 'No', 'No']]
    Hu = ['رسائی', 'Public', 'Protected', 'Private']
    Ru = [['اسی کلاس میں اراکین (ڈیٹا، فنکشنز) تک رسائی', 'ہاں', 'ہاں', 'ہاں'], ['ماخوذ کلاسز میں اراکین (ڈیٹا، فنکشنز) تک رسائی', 'ہاں', 'ہاں', 'نہیں'], ['کلاس کے باہر یعنی main() سے اراکین (ڈیٹا، فنکشنز) تک رسائی', 'ہاں', 'نہیں', 'نہیں']]
    Hp = ['لاسرسی', 'Public', 'Protected', 'Private']
    Rp = [['په همغه ټولګي کې غړو (ډېټا، فنکشنونه) ته لاسرسی', 'هو', 'هو', 'هو'], ['په مشتق ټولګیو کې غړو (ډېټا، فنکشنونه) ته لاسرسی', 'هو', 'هو', 'نه'], ['له ټولګي بهر یعنې له main() غړو (ډېټا، فنکشنونه) ته لاسرسی', 'هو', 'نه', 'نه']]
    t.table('cs12-table-8-1', H, R, Hu, Hp, Ru, Rp)
    P('Table 8.1: Access Specifiers and Data Hiding', 'جدول 8.1: ایکسس اسپیسیفائرز اور ڈیٹا ہائیڈنگ', '۸.۱ جدول: د لاسرسي ټاکونکي او د ډېټا پټول')
    P('The concept of data hiding, shown in table 8.1, will be demonstrated after the introduction of inheritance.', 'جدول 8.1 میں دکھایا گیا ڈیٹا ہائیڈنگ کا تصور وراثت کے تعارف کے بعد واضح کیا جائے گا۔', 'په ۸.۱ جدول کې ښودل شوی د ډېټا د پټولو مفهوم به د میراث له معرفي وروسته وښودل شي.')
    t.h('8.1.5 Constructor and Destructor', '8.1.5 کنسٹرکٹر اور ڈسٹرکٹر', '۸.۱.۵ جوړوونکی او ړنګوونکی')
    P('Constructors and destructors are special member functions within the class with the same name as that of the class. The following sections discuss them in detail with the help of examples.', 'کنسٹرکٹرز اور ڈسٹرکٹرز کلاس کے اندر خاص ممبر فنکشنز ہیں جن کا نام کلاس کے نام جیسا ہوتا ہے۔ درج ذیل حصے مثالوں کی مدد سے ان پر تفصیل سے بات کرتے ہیں۔', 'جوړوونکي او ړنګوونکي د ټولګي دننه ځانګړي غړي فنکشنونه دي چې نوم یې د ټولګي له نوم سره یو دی. لاندې برخې د بېلګو په مرسته دا په تفصیل څېړي.')
    t.h('a. Constructor', 'a. کنسٹرکٹر', 'a. جوړوونکی')
    P('A constructor is a special kind of member function that is executed automatically when an object of the class is instantiated. Constructors are typically used to initialize data members of the class to appropriate default values, or to allow the user to easily initialize those member variables to whatever values are desired.',
      'کنسٹرکٹر ایک خاص قسم کا ممبر فنکشن ہے جو کلاس کا آبجیکٹ بننے پر خود بخود چلتا ہے۔ کنسٹرکٹرز عموماً کلاس کے ڈیٹا ممبرز کو مناسب ڈیفالٹ قدریں دینے یا صارف کو ان ممبر ویری ایبلز کو حسبِ خواہش قدریں آسانی سے دینے کی اجازت دینے کے لیے استعمال ہوتے ہیں۔',
      'جوړوونکی یو ځانګړی ډول غړی فنکشن دی چې د ټولګي د شي د جوړېدو پر مهال پخپله اجرا کېږي. جوړوونکي عموماً د ټولګي د ډېټا غړو ته د مناسبو ډیفالټ ارزښتونو ورکولو، یا کاروونکي ته د دې اجازې لپاره کارېږي چې دې غړو متغیرونو ته په اسانۍ هر غوښتل شوی ارزښت ورکړي.')
    P('constructors have specific rules for naming:', 'کنسٹرکٹرز کے نام رکھنے کے مخصوص اصول ہیں:', 'جوړوونکي د نوم ایښودلو ځانګړي قواعد لري:')
    t.group('list', [('Constructors have the same name as that of the class', 'کنسٹرکٹرز کا نام کلاس کے نام جیسا ہوتا ہے', 'جوړوونکي د ټولګي په څېر نوم لري'), ('Constructors have no return type (not even void)', 'کنسٹرکٹرز کی کوئی ریٹرن ٹائپ نہیں ہوتی (void بھی نہیں)', 'جوړوونکي د بېرته ورکړې ډول نه لري (حتی void هم نه)')])
    BOOK.save(125, [(8, rec(t, 6, 125, [238, 239], 'The top of p.238 (end of the Access program, explanation and output) is recorded with PDF124. Table 8.1 is reproduced as a structured table; its faint printed caption is given below it.'))],
              issues=[{'id': 'cs12-pdf125', 'unit': 8, 'printedPage': 238,
                       'description': 'p.238 “we got the facility of hiding data”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    {120: p120, 121: p121, 122: p122, 123: p123, 124: p124, 125: p125}[n]()
