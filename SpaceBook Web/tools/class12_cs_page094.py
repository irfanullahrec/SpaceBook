"""Computer Science XII PDF94–97: pp.176–183 — introduction, 6.1 functions, 6.1.1 concept and types, built-in sin()/abs() programs,
user-defined functions, defining, addition program, working, 6.1.2 advantages, 6.1.3 signature, 6.1.4 components, a. prototype, b. definition (begins).
Run: python class12_cs_page094.py N (94–97)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u6-text-{n}', f'Unit 6 text ({n})', f'یونٹ 6 — متن ({n})', f'۶ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p94():
    t = Builder()
    P = t.p
    t.h('INTRODUCTION', 'تعارف', 'سریزه')
    P('A good programming technique is to modularize the programs into small segments of codes. These small segments are called modules or procedures and perform some specific tasks. In C++ language, these modules are usually called functions. This unit describes the basic concepts of functions, its parts, parameters and arguments. Here, the concept of function overloading has also been discussed with the help of examples.',
      'ایک اچھی پروگرامنگ تکنیک یہ ہے کہ پروگراموں کو کوڈ کے چھوٹے حصوں میں تقسیم کیا جائے۔ یہ چھوٹے حصے ماڈیولز یا پروسیجرز کہلاتے ہیں اور کچھ مخصوص کام انجام دیتے ہیں۔ C++ زبان میں ان ماڈیولز کو عموماً فنکشنز کہا جاتا ہے۔ یہ یونٹ فنکشنز کے بنیادی تصورات، ان کے حصے، پیرامیٹرز اور آرگیومنٹس بیان کرتا ہے۔ یہاں مثالوں کی مدد سے فنکشن اوورلوڈنگ کے تصور پر بھی بات کی گئی ہے۔',
      'د پروګرام جوړونې ښه تخنیک دا دی چې پروګرامونه د کوډ په وړو برخو ووېشل شي. دا وړې برخې ماډیولونه یا پروسیجرونه بلل کېږي او ځینې ځانګړې دندې ترسره کوي. په C++ ژبه کې دې ماډیولونو ته عموماً فنکشنونه ویل کېږي. دا څپرکی د فنکشنونو بنسټیز مفاهیم، برخې، پاراميټرونه او دلیلونه بیانوي. دلته د بېلګو په مرسته د فنکشن ډېرولو (overloading) مفهوم هم څېړل شوی.')
    t.h('6.1 Functions', '6.1 فنکشنز', '۶.۱ فنکشنونه')
    P('In C++ program, when a set of related statements are grouped together, in a particular format, to accomplish a specific task is called function. Function is one of the main building blocks of any programming language. There are some functions whose work has been fixed by the developers of C++ programming language. These are called built-in functions. Built-in functions are specific in its functionalities; therefore, the programmers develop their own functions called user-defined functions. These functions are the main focus point of this unit.',
      'C++ پروگرام میں جب متعلقہ بیانات کا ایک مجموعہ کسی خاص کام کی انجام دہی کے لیے ایک مخصوص شکل میں اکٹھا کیا جائے تو اسے فنکشن کہتے ہیں۔ فنکشن کسی بھی پروگرامنگ زبان کے بنیادی اجزا میں سے ایک ہے۔ کچھ فنکشنز ایسے ہیں جن کا کام C++ پروگرامنگ زبان کے بنانے والوں نے مقرر کر دیا ہے۔ انھیں بلٹ اِن فنکشنز کہتے ہیں۔ بلٹ اِن فنکشنز اپنی کارکردگی میں مخصوص ہیں؛ اس لیے پروگرامرز اپنے فنکشنز بناتے ہیں جنھیں یوزر ڈیفائنڈ فنکشنز کہتے ہیں۔ یہ فنکشنز اس یونٹ کا مرکزی موضوع ہیں۔',
      'په C++ پروګرام کې کله چې د اړوندو بیانونو یوه ټولګه د یوې ځانګړې دندې د ترسره کولو لپاره په یوه ټاکلې بڼه یوځای شي، فنکشن بلل کېږي. فنکشن د هرې پروګرامي ژبې له اصلي جوړوونکو برخو یو دی. ځینې فنکشنونه شته چې کار یې د C++ پروګرامي ژبې جوړوونکو ټاکلی دی. دا جوړ شوي (built-in) فنکشنونه بلل کېږي. جوړ شوي فنکشنونه په خپلو دندو کې ځانګړي دي؛ نو پروګرام جوړوونکي خپل فنکشنونه جوړوي چې د کاروونکي-تعریف شوي فنکشنونه بلل کېږي. دا فنکشنونه د دې څپرکي اصلي تمرکز دی.')
    t.h('6.1.1 Concept and types of functions', '6.1.1 فنکشنز کا تصور اور اقسام', '۶.۱.۱ د فنکشنونو مفهوم او ډولونه')
    P('Function is an important feature of any programming language. It makes the work easier by writing the code once and executing it again and again. Mainly, functions are divided into two types built-in and user defined.',
      'فنکشن کسی بھی پروگرامنگ زبان کی اہم خصوصیت ہے۔ یہ کوڈ ایک بار لکھ کر بار بار چلانے سے کام آسان بناتا ہے۔ بنیادی طور پر فنکشنز دو اقسام میں تقسیم ہیں: بلٹ اِن اور یوزر ڈیفائنڈ۔',
      'فنکشن د هرې پروګرامي ژبې مهمه ځانګړتیا ده. دا د کوډ یو ځل لیکلو او بیا بیا اجرا کولو له لارې کار اسانوي. په اصل کې فنکشنونه په دوو ډولونو وېشل کېږي: جوړ شوي او د کاروونکي-تعریف شوي.')
    t.h('a. Concept of function', 'a. فنکشن کا تصور', 'a. د فنکشن مفهوم')
    P('Whenever we want to perform a task again and again in a program such as calculating the square or cube for multiple integer values then it is too difficult to write the same code multiple times, say 5 times for 5 different integer values, in the same program.',
      'جب بھی ہم کسی پروگرام میں کوئی کام بار بار کرنا چاہیں، جیسے متعدد صحیح قدروں کا مربع یا مکعب معلوم کرنا، تو ایک ہی پروگرام میں ایک ہی کوڈ کو کئی بار، مثلاً 5 مختلف صحیح قدروں کے لیے 5 بار، لکھنا بہت مشکل ہے۔',
      'کله چې وغواړو په یوه پروګرام کې یوه دنده بیا بیا ترسره کړو، لکه د ډېرو صحیح ارزښتونو مربع یا مکعب موندل، نو په یوه پروګرام کې یو کوډ څو ځله، مثلاً د ۵ بېلو صحیح ارزښتونو لپاره ۵ ځله، لیکل ډېر ستونزمن دي.')
    t.h('b. Types of functions', 'b. فنکشنز کی اقسام', 'b. د فنکشنونو ډولونه')
    P('C++ functions are categorized into two types namely built-in function and user defined functions. The following sections describe these types in detail.', 'C++ فنکشنز دو اقسام میں تقسیم ہیں یعنی بلٹ اِن فنکشن اور یوزر ڈیفائنڈ فنکشنز۔ درج ذیل حصے ان اقسام کو تفصیل سے بیان کرتے ہیں۔', 'C++ فنکشنونه په دوو ډولونو وېشل کېږي، یعنې جوړ شوي فنکشن او د کاروونکي-تعریف شوي فنکشنونه. لاندې برخې دا ډولونه په تفصیل بیانوي.')
    t.h('i. Built-in Functions', 'i. بلٹ اِن فنکشنز', 'i. جوړ شوي فنکشنونه')
    P('C++ language provides a number of pre-compiled functions for some commonly used operations. These functions are called built-in functions. Built-in functions are part of the C++ language and are highly valuable, pre-tested and completely reliable. The C++ built-in functions are made for various assignments ranging from algebra, geometry, trigonometry, finance, text and graphics to some complex operations.',
      'C++ زبان کچھ عام استعمال ہونے والے کاموں کے لیے متعدد پہلے سے کمپائل شدہ فنکشنز فراہم کرتی ہے۔ یہ فنکشنز بلٹ اِن فنکشنز کہلاتے ہیں۔ بلٹ اِن فنکشنز C++ زبان کا حصہ ہیں اور بہت قیمتی، پہلے سے جانچے ہوئے اور مکمل قابلِ اعتماد ہیں۔ C++ کے بلٹ اِن فنکشنز الجبرا، جیومیٹری، ٹرگنومیٹری، مالیات، متن اور گرافکس سے لے کر کچھ پیچیدہ کاموں تک مختلف مقاصد کے لیے بنائے گئے ہیں۔',
      'C++ ژبه د ځینو عام کارېدونکو عملیو لپاره یو شمېر مخکې کمپایل شوي فنکشنونه برابروي. دا فنکشنونه جوړ شوي فنکشنونه بلل کېږي. جوړ شوي فنکشنونه د C++ ژبې برخه دي او ډېر ارزښتناک، مخکې ازمول شوي او بشپړ باوري دي. د C++ جوړ شوي فنکشنونه د الجبر، جیومټرۍ، مثلثاتو، مالي چارو، متن او ګرافیک څخه تر ځینو پېچلو عملیو پورې د بېلابېلو دندو لپاره جوړ شوي.')
    P('Consider the following example that requests the value of angle and calculate its sine and display it on the screen.', 'درج ذیل مثال پر غور کریں جو زاویے کی قدر مانگتی ہے، اس کا sine معلوم کرتی ہے اور اسے اسکرین پر دکھاتی ہے۔', 'لاندې بېلګې ته پام وکړئ چې د زاویې ارزښت غواړي، د هغې sine حسابوي او پر پرده یې ښيي.')
    code(t, '''// built-in function(sin())program
#include <iostream.h>
#include<conio.h>
#include<math.h>
int main()
{
float angle;
cout << "Enter value for angle:"<<endl;
cin >> angle;
cout<<"The Sine of "<<angle<<" degree is =
"<<sin(angle);
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Enter value for angle:
45.0
The Sin of 45.0 degree is = 0.850904''')
    BOOK.save(94, [(6, rec(t, 1, 94, [176, 177, 178], 'The sin() program output is at the top of p.178 (PDF95) and is given here.'))],
              issues=[{'id': 'cs12-pdf094', 'unit': 6, 'printedPage': 177,
                       'description': 'The sin() program prints “The Sine of …” but the output shows “The Sin of 45.0 degree is = 0.850904” (sin() takes radians); the cout string is printed broken across two lines. Retained as printed.'}])


def p95():
    t = Builder()
    P = t.p
    P('Here, sin() is a built-in function defined in the math.h header file. The value inside the sin() is converted to its corresponding sin value and displayed on the screen. Similarly we can calculate cosine, tangent and tangent inverse by using cos(x), tan(x) and cot(x) built-in functions respectively.',
      'یہاں sin() ایک بلٹ اِن فنکشن ہے جو math.h ہیڈر فائل میں بیان کیا گیا ہے۔ sin() کے اندر کی قدر اس کی متعلقہ sin قدر میں بدل کر اسکرین پر دکھائی جاتی ہے۔ اسی طرح ہم بالترتیب cos(x)، tan(x) اور cot(x) بلٹ اِن فنکشنز سے cosine، tangent اور tangent inverse معلوم کر سکتے ہیں۔',
      'دلته sin() یو جوړ شوی فنکشن دی چې د math.h سرپاڼه دوتنه کې تعریف شوی. د sin() دننه ارزښت په اړوند sin ارزښت بدلېږي او پر پرده ښودل کېږي. همداراز کولی شو په ترتیب سره د cos(x)، tan(x) او cot(x) جوړ شویو فنکشنونو په مرسته cosine، tangent او tangent inverse حساب کړو.')
    P('Consider another example:', 'ایک اور مثال پر غور کریں:', 'بلې بېلګې ته پام وکړئ:')
    code(t, '''//built-in function abs( ) program
#include <math.h>
#include <iostream.h>
#include <conio.h>
int main()
{
int X;
cout<<"Enter value for X"<<endl;
cin>>X;
cout<< "Absolute value of " <<X << " is: " <<abs(X);
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Enter value for X
-12
Absolute value of -12 is: 12''')
    P('In this example, the value entered by the user, from the keyboard, is taken into the abs( ) function and the result is displayed on the screen. Like abs( ), some other functions that are included in <math.h> header file are pow(x,n), sqrt(x), etc.',
      'اس مثال میں صارف کی کی بورڈ سے داخل کردہ قدر abs( ) فنکشن میں لی جاتی ہے اور نتیجہ اسکرین پر دکھایا جاتا ہے۔ abs( ) کی طرح <math.h> ہیڈر فائل میں شامل کچھ دوسرے فنکشنز pow(x,n)، sqrt(x) وغیرہ ہیں۔',
      'په دې بېلګه کې هغه ارزښت چې کاروونکی یې له کیبورډ لیکي، abs( ) فنکشن ته ورکول کېږي او پایله پر پرده ښودل کېږي. د abs( ) په څېر په <math.h> سرپاڼه دوتنه کې ځینې نور فنکشنونه pow(x,n)، sqrt(x) او نور دي.')
    P('The built-in functions are defined in the C++ library which should be included in the program before using these functions. These functions are used for the most commonly and frequently used operations and cannot be modified according to the users need. This feature of the functions is its main limitation. To overcome this problem, C++ provides a new set of functions that can be defined by the users itself. The following section describes this set of functions in detail.',
      'بلٹ اِن فنکشنز C++ لائبریری میں بیان کیے گئے ہیں جسے ان فنکشنز کے استعمال سے پہلے پروگرام میں شامل کرنا چاہیے۔ یہ فنکشنز سب سے عام اور بار بار استعمال ہونے والے کاموں کے لیے استعمال ہوتے ہیں اور صارفین کی ضرورت کے مطابق تبدیل نہیں کیے جا سکتے۔ فنکشنز کی یہ خصوصیت ان کی بنیادی حد ہے۔ اس مسئلے پر قابو پانے کے لیے C++ فنکشنز کا ایک نیا مجموعہ فراہم کرتی ہے جسے صارفین خود بیان کر سکتے ہیں۔ درج ذیل حصہ فنکشنز کے اس مجموعے کو تفصیل سے بیان کرتا ہے۔',
      'جوړ شوي فنکشنونه د C++ په کتابتون کې تعریف شوي چې د دې فنکشنونو له کارولو مخکې باید په پروګرام کې شامل شي. دا فنکشنونه د تر ټولو عامو او ډېر کارېدونکو عملیو لپاره کارېږي او د کاروونکو د اړتیا سره سم نه شي بدلېدای. د فنکشنونو دا ځانګړتیا یې اصلي محدودیت دی. د دې ستونزې د حل لپاره C++ د فنکشنونو نوې ټولګه برابروي چې کاروونکي یې پخپله تعریفولی شي. لاندې برخه د فنکشنونو دا ټولګه په تفصیل بیانوي.')
    t.h('ii. User-defined functions', 'ii. یوزر ڈیفائنڈ فنکشنز', 'ii. د کاروونکي-تعریف شوي فنکشنونه')
    P('The functions defined by the users, according to their needs, to perform their own tasks are called users-defined functions. These functions are used to overcome the limitations of build-in functions.',
      'صارفین کی طرف سے اپنی ضرورت کے مطابق اپنے کام انجام دینے کے لیے بیان کیے گئے فنکشنز یوزر ڈیفائنڈ فنکشنز کہلاتے ہیں۔ یہ فنکشنز بلٹ اِن فنکشنز کی حدود پر قابو پانے کے لیے استعمال ہوتے ہیں۔',
      'هغه فنکشنونه چې کاروونکي یې د خپلو اړتیاوو سره سم د خپلو دندو د ترسره کولو لپاره تعریفوي، د کاروونکي-تعریف شوي فنکشنونه بلل کېږي. دا فنکشنونه د جوړ شویو فنکشنونو د محدودیتونو د لرې کولو لپاره کارېږي.')
    t.h('Defining user-defined function', 'یوزر ڈیفائنڈ فنکشن کی تعریف', 'د کاروونکي-تعریف شوي فنکشن تعریفول')
    P('A function must be defined first to use it in the program. The general syntax for defining a user-defined function is given below.', 'پروگرام میں استعمال کرنے کے لیے فنکشن کی پہلے تعریف ضروری ہے۔ یوزر ڈیفائنڈ فنکشن کی تعریف کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے۔', 'فنکشن باید په پروګرام کې د کارولو لپاره لومړی تعریف شي. د کاروونکي-تعریف شوي فنکشن د تعریف عمومي بڼه لاندې ورکړل شوې.')
    code(t, '''type name (parameter1, parameter2, ...)
{
Statements;
}''')
    P('Where:', 'جہاں:', 'چېرته چې:')
    t.group('list', [
     ('Type is the data type specifier of the data returned by the function.', 'Type فنکشن کی طرف سے واپس کیے گئے ڈیٹا کی ڈیٹا ٹائپ بتاتا ہے۔', 'Type د فنکشن له خوا د بېرته ورکړل شوي ډېټا ډول ښيي.'),
     ('Name is the identifier by which a function will be called.', 'Name وہ شناخت کنندہ ہے جس سے فنکشن کو کال کیا جائے گا۔', 'Name هغه پېژندونکی دی چې فنکشن پرې غوښتل کېږي.'),
     ('Parameters are the variables that receive arguments. Each parameter has its data type like variable. There can be as many parameters as needed but they should be separated by commas.', 'Parameters وہ ویری ایبلز ہیں جو آرگیومنٹس وصول کرتے ہیں۔ ہر پیرامیٹر کی ویری ایبل کی طرح اپنی ڈیٹا ٹائپ ہوتی ہے۔ ضرورت کے مطابق جتنے چاہیں پیرامیٹرز ہو سکتے ہیں لیکن انھیں کاموں سے الگ ہونا چاہیے۔', 'Parameters هغه متغیرونه دي چې دلیلونه ترلاسه کوي. هر پاراميټر د متغیر په څېر خپل ډېټا ډول لري. هرڅومره چې اړتیا وي پاراميټرونه کېدای شي خو باید په کامو سره جلا شي.'),
     ('Statements constitute the body of the function. It is a block of statements surrounded by braces { }.', 'Statements فنکشن کا جسم بناتے ہیں۔ یہ بریسز { } میں گھرا بیانات کا بلاک ہے۔', 'Statements د فنکشن بدنه جوړوي. دا د بیانونو بلاک دی چې په لوړو قوسونو { } کې راګېر دی.')])
    BOOK.save(95, [(6, rec(t, 2, 95, [178, 179, 180], 'The top of p.178 (sin() output) is recorded with PDF94; the “Where” list continues on p.180 (PDF96) and is given whole here.'))],
              issues=[{'id': 'cs12-pdf095', 'unit': 6, 'printedPage': 179,
                       'description': 'p.178 lists cot(x) as giving the “tangent inverse”; p.179 “users-defined functions”, “build-in functions”, “defined by the users itself”. Retained as printed.'}])


def p96():
    t = Builder()
    P = t.p
    P('Consider a function named addition to take two integer values, add them together and return the result to the calling program. The following code segment defines this function:',
      'addition نامی فنکشن پر غور کریں جو دو صحیح قدریں لیتا ہے، انھیں جمع کرتا ہے اور نتیجہ کال کرنے والے پروگرام کو واپس کرتا ہے۔ درج ذیل کوڈ کا حصہ یہ فنکشن بیان کرتا ہے:',
      'د addition په نوم فنکشن ته پام وکړئ چې دوه صحیح ارزښتونه اخلي، یوځای یې جمع کوي او پایله غوښتونکي پروګرام ته ورکوي. لاندې د کوډ برخه دا فنکشن تعریفوي:')
    code(t, '''// user-defined function (addition) program
#include <iostream.h>
#include <conio.h>
int addition (int a, int b)
{
int sum;
sum=a+b;
return (sum);
}
int main()
{
int z;
z = addition (55,33);
cout << "The sum of a and b is= " << z;
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'The sum of a and b is =88')
    t.h('Working of user-defined functions', 'یوزر ڈیفائنڈ فنکشنز کا عمل', 'د کاروونکي-تعریف شویو فنکشنونو کار')
    P('In the above program, addition (int a, int b) is the example of user-defined function defined by the user to perform the addition of two integer values (55 and 33 in this case). These values are passed by the function call addition (55,33). After performing addition, the function returns the sum (88) back to calling program (in this case, main) using the following statement.',
      'اوپر کے پروگرام میں addition (int a, int b) یوزر ڈیفائنڈ فنکشن کی مثال ہے جسے صارف نے دو صحیح قدروں (اس صورت میں 55 اور 33) کو جمع کرنے کے لیے بیان کیا ہے۔ یہ قدریں فنکشن کال addition (55,33) سے پاس کی جاتی ہیں۔ جمع کرنے کے بعد فنکشن درج ذیل بیان کے ذریعے حاصلِ جمع (88) کال کرنے والے پروگرام (اس صورت میں main) کو واپس کرتا ہے۔',
      'په پورته پروګرام کې addition (int a, int b) د کاروونکي-تعریف شوي فنکشن بېلګه ده چې کاروونکي د دوو صحیح ارزښتونو (په دې حالت کې 55 او 33) د جمع لپاره تعریف کړی. دا ارزښتونه د addition (55,33) فنکشن غوښتنې له لارې لېږدول کېږي. له جمع وروسته فنکشن د لاندې بیان په مرسته مجموعه (88) غوښتونکي پروګرام (په دې حالت کې main) ته ورګرځوي.')
    code(t, 'return (sum);')
    P('The sum is assigned to the variable z, in main(), as shown below:', 'حاصلِ جمع main() میں ویری ایبل z کو دیا جاتا ہے، جیسا کہ ذیل میں دکھایا گیا ہے:', 'مجموعه په main() کې z متغیر ته ورکول کېږي، لکه لاندې:')
    code(t, 'z = addition (55, 33);')
    P('The following line of code, in main, is used to display the result on the screen as shown in the above program.', 'main میں کوڈ کی درج ذیل لائن نتیجہ اسکرین پر دکھانے کے لیے استعمال ہوتی ہے جیسا کہ اوپر کے پروگرام میں دکھایا گیا ہے۔', 'په main کې د کوډ لاندې کرښه پر پرده د پایلې د ښودلو لپاره کارېږي لکه په پورته پروګرام کې.')
    code(t, 'cout << "The sum of a and b is= " << z;')
    t.h('6.1.2 Advantages of using functions', '6.1.2 فنکشنز کے استعمال کے فوائد', '۶.۱.۲ د فنکشنونو د کارونې ګټې')
    P('Using functions we can structure our programs in a more modularized way. The use of functions provides many benefits, including:', 'فنکشنز کے ذریعے ہم اپنے پروگراموں کو زیادہ ماڈیولر انداز میں ترتیب دے سکتے ہیں۔ فنکشنز کا استعمال بہت سے فوائد فراہم کرتا ہے، جن میں شامل ہیں:', 'د فنکشنونو په مرسته کولی شو خپل پروګرامونه په ډېر ماډیولي ډول جوړ کړو. د فنکشنونو کارونه ډېرې ګټې لري، په شمول:')
    t.group('list', [
     ('Code reusability: The code inside the function can be reused by calling it again and again in the program.', 'کوڈ کا دوبارہ استعمال: فنکشن کے اندر کا کوڈ پروگرام میں اسے بار بار کال کر کے دوبارہ استعمال کیا جا سکتا ہے۔', 'د کوډ بیا کارونه: د فنکشن دننه کوډ په پروګرام کې د بیا بیا غوښتلو له لارې بیا کارول کېدای شي.'),
     ('Updating code: It is much easier to change or update the code in a function, which needs to be done once.', 'کوڈ کی تازہ کاری: فنکشن میں کوڈ تبدیل یا تازہ کرنا بہت آسان ہے، جو صرف ایک بار کرنا ہوتا ہے۔', 'د کوډ تازه کول: په فنکشن کې د کوډ بدلول یا تازه کول ډېر اسانه دي، چې یوازې یو ځل کول غواړي.'),
     ('Readability and understandability: It makes the code easier to read and understand.', 'پڑھنے اور سمجھنے میں آسانی: یہ کوڈ کو پڑھنے اور سمجھنے میں آسان بناتا ہے۔', 'لوستل او پوهېدل: کوډ لوستل او پوهېدل اسانوي.')])
    BOOK.save(96, [(6, rec(t, 3, 96, [180, 181], 'The top of p.180 (end of the “Where” list) is recorded with PDF95.'))],
              issues=[{'id': 'cs12-pdf096', 'unit': 6, 'printedPage': 180,
                       'description': 'The program prints "The sum of a and b is= " but the output shows “The sum of a and b is =88”. Retained as printed.'}])


def p97():
    t = Builder()
    P = t.p
    t.h('6.1.3 Function signature', '6.1.3 فنکشن سگنیچر', '۶.۱.۳ د فنکشن لاسلیک')
    P('The signature of a function comprises of the parts given below.', 'فنکشن کا سگنیچر ذیل میں دیے گئے حصوں پر مشتمل ہوتا ہے۔', 'د فنکشن لاسلیک له لاندې برخو جوړ دی.')
    t.group('list', [('Name of the function', 'فنکشن کا نام', 'د فنکشن نوم'), ('The number, order and data types of the arguments', 'آرگیومنٹس کی تعداد، ترتیب اور ڈیٹا ٹائپس', 'د دلیلونو شمېر، ترتیب او ډېټا ډولونه'), ('Return type of function', 'فنکشن کی ریٹرن ٹائپ', 'د فنکشن د بېرته ورکړې ډول')])
    P('Let us consider the add function to demonstrate function signature', 'فنکشن سگنیچر واضح کرنے کے لیے add فنکشن پر غور کرتے ہیں', 'راځئ د فنکشن لاسلیک د ښودلو لپاره add فنکشن ته پام وکړو')
    code(t, '''double add(int x, double y)
{
return x+y;
}''')
    P('The signature of the above mentioned function is:', 'اوپر بیان کیے گئے فنکشن کا سگنیچر یہ ہے:', 'د پورته یاد شوي فنکشن لاسلیک دا دی:')
    code(t, 'double add(int x, double y)')
    P('The Signature of this add function comprises of:', 'اس add فنکشن کا سگنیچر ان پر مشتمل ہے:', 'د دې add فنکشن لاسلیک له دې جوړ دی:')
    t.group('list', [('Name of the function: add', 'فنکشن کا نام: add', 'د فنکشن نوم: add'), ('The data types of the arguments: int , double', 'آرگیومنٹس کی ڈیٹا ٹائپس: int , double', 'د دلیلونو ډېټا ډولونه: int , double'), ('Return type of the function: double', 'فنکشن کی ریٹرن ٹائپ: double', 'د فنکشن د بېرته ورکړې ډول: double')])
    t.h('6.1.4 Components of functions', '6.1.4 فنکشنز کے اجزا', '۶.۱.۴ د فنکشنونو برخې')
    P('Each function consists of three components. These are:', 'ہر فنکشن تین اجزا پر مشتمل ہوتا ہے۔ یہ ہیں:', 'هر فنکشن درې برخې لري. دا دي:')
    t.group('list', [('Function prototype/declaration', 'فنکشن پروٹوٹائپ/ڈکلیریشن', 'د فنکشن نمونه/اعلان'), ('Function definition', 'فنکشن کی تعریف', 'د فنکشن تعریف'), ('Function call', 'فنکشن کال', 'د فنکشن غوښتنه')])
    t.h('a. Function prototype', 'a. فنکشن پروٹوٹائپ', 'a. د فنکشن نمونه')
    P('A function prototype is that part of a function that tells the compiler the name of the function, the type of data returned by the function, the number of parameters the function expects to receive, the types of the parameters, and the order of parameters.',
      'فنکشن پروٹوٹائپ فنکشن کا وہ حصہ ہے جو کمپائلر کو فنکشن کا نام، فنکشن کی طرف سے واپس کیے جانے والے ڈیٹا کی قسم، فنکشن کے متوقع پیرامیٹرز کی تعداد، پیرامیٹرز کی اقسام اور پیرامیٹرز کی ترتیب بتاتا ہے۔',
      'د فنکشن نمونه د فنکشن هغه برخه ده چې کمپایلر ته د فنکشن نوم، د فنکشن له خوا د بېرته ورکړل شوي ډېټا ډول، د هغو پاراميټرونو شمېر چې فنکشن یې د ترلاسه کولو تمه لري، د پاراميټرونو ډولونه او د پاراميټرونو ترتیب ښيي.')
    P('A function prototype is also called function declaration and is used in situation whenever the function is defined after the main() function. The function prototype ends with a semicolon (;).',
      'فنکشن پروٹوٹائپ کو فنکشن ڈکلیریشن بھی کہتے ہیں اور یہ اس صورت میں استعمال ہوتا ہے جب فنکشن main() فنکشن کے بعد بیان کیا گیا ہو۔ فنکشن پروٹوٹائپ سیمی کولن (;) پر ختم ہوتا ہے۔',
      'د فنکشن نمونه د فنکشن اعلان هم بلل کېږي او هغه وخت کارېږي چې فنکشن د main() فنکشن وروسته تعریف شوی وي. د فنکشن نمونه په سیمي‌کولن (;) پای ته رسېږي.')
    P('The function prototype for a function named “maximum” to calculate maximum number out of three integers is given below:', 'تین صحیح اعداد میں سے سب سے بڑا عدد معلوم کرنے والے ’’maximum‘‘ نامی فنکشن کا پروٹوٹائپ ذیل میں دیا گیا ہے:', 'د "maximum" په نوم د هغه فنکشن نمونه چې له درېیو صحیح عددونو تر ټولو لوی عدد حسابوي، لاندې ورکړل شوې:')
    code(t, 'int maximum( int a, int b, int c);')
    P('The compiler use function prototypes to validate function call. In a prototype, argument names are optional; however, the types are necessary as shown below:', 'کمپائلر فنکشن کال کی توثیق کے لیے فنکشن پروٹوٹائپس استعمال کرتا ہے۔ پروٹوٹائپ میں آرگیومنٹس کے نام اختیاری ہیں؛ تاہم اقسام ضروری ہیں جیسا کہ ذیل میں دکھایا گیا ہے:', 'کمپایلر د فنکشن غوښتنې د تایید لپاره د فنکشن نمونې کاروي. په نمونه کې د دلیلونو نومونه اختیاري دي؛ خو ډولونه اړین دي لکه لاندې:')
    code(t, 'int maximum( int , int , int );')
    P('Function prototype is used in C++ program only when the function is defined after the definition of main() function. If the function definition lies before the main() function then there is no need for the function prototype.',
      'C++ پروگرام میں فنکشن پروٹوٹائپ صرف اس وقت استعمال ہوتا ہے جب فنکشن main() فنکشن کی تعریف کے بعد بیان کیا گیا ہو۔ اگر فنکشن کی تعریف main() فنکشن سے پہلے ہو تو فنکشن پروٹوٹائپ کی ضرورت نہیں۔',
      'په C++ پروګرام کې د فنکشن نمونه یوازې هغه وخت کارېږي چې فنکشن د main() فنکشن له تعریف وروسته تعریف شوی وي. که د فنکشن تعریف د main() فنکشن مخکې وي، د فنکشن نمونې ته اړتیا نشته.')
    t.h('b. Function definition', 'b. فنکشن کی تعریف', 'b. د فنکشن تعریف')
    P('A function definition specifies what a function does. It has two parts: a declaration /header and function body enclosed in { }. Function declarator is similar to function prototype with the only difference that it has the variables name for the parameters and without semicolon (;). Consider the following function declarator.',
      'فنکشن کی تعریف بتاتی ہے کہ فنکشن کیا کرتا ہے۔ اس کے دو حصے ہیں: ڈکلیریشن/ہیڈر اور { } میں بند فنکشن کا جسم۔ فنکشن ڈکلیریٹر فنکشن پروٹوٹائپ جیسا ہے، فرق صرف یہ ہے کہ اس میں پیرامیٹرز کے لیے ویری ایبلز کے نام ہوتے ہیں اور سیمی کولن (;) نہیں ہوتا۔ درج ذیل فنکشن ڈکلیریٹر پر غور کریں۔',
      'د فنکشن تعریف ښيي چې فنکشن څه کوي. دوه برخې لري: اعلان/سرلیک او په { } کې تړلې د فنکشن بدنه. د فنکشن اعلانوونکی د فنکشن نمونې ته ورته دی، یوازینی توپیر یې دا دی چې د پاراميټرونو لپاره د متغیرونو نومونه لري او سیمي‌کولن (;) نه لري. لاندې د فنکشن اعلانوونکي ته پام وکړئ.')
    BOOK.save(97, [(6, rec(t, 4, 97, [182, 183]))], issues=[{'id': 'cs12-pdf097', 'unit': 6, 'printedPage': 183,
               'description': 'p.183 “The compiler use function prototypes”; “used in situation whenever”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 94
    {94: p94, 95: p95, 96: p96, 97: p97}[n]()
