"""Computer Science XII PDF86–91: pp.160–171 — 2-D access/write programs; 5.3 strings, defining, initializing (C and C++), concatenation program;
5.3.4 string functions: strcat(), copy(), strcpy(), find(), length(), swap().
Run: python class12_cs_page086.py N (86–91)."""
import sys
from class12_cs_common import BOOK, Builder, code

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
HDR = '''#include <iostream.h>
#include <string>
#include<conio.h>'''


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u5-text-{n}', f'Unit 5 text ({n})', f'یونٹ 5 — متن ({n})', f'۵ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p86():
    t = Builder()
    P = t.p
    P('Accessing elements of a two-dimensional array individually is very difficult and time consuming. A better solution to this is the application of loop. Normally, nested loops are used for this purpose: outer loop for the row, and inner loop for the columns. Since, two-dimensional arrays are typically accessed row by row, therefore, the row index is used as the outer loop and the column index is used as the inner loop.',
      'دو جہتی ایرے کے عناصر تک انفرادی طور پر رسائی بہت مشکل اور وقت طلب ہے۔ اس کا بہتر حل لوپ کا استعمال ہے۔ عموماً اس مقصد کے لیے نیسٹڈ لوپس استعمال ہوتے ہیں: بیرونی لوپ قطار کے لیے اور اندرونی لوپ کالموں کے لیے۔ چونکہ دو جہتی ایریز تک عموماً قطار بہ قطار رسائی کی جاتی ہے، اس لیے قطار انڈیکس بیرونی لوپ اور کالم انڈیکس اندرونی لوپ کے طور پر استعمال ہوتا ہے۔',
      'د دوه-بعدي لړۍ عناصرو ته جلا جلا لاسرسی ډېر ستونزمن او وخت نیوونکی دی. د دې ښه حل د حلقې کارونه ده. عموماً د دې موخې لپاره ځالې حلقې کارېږي: بهرنۍ حلقه د قطار لپاره او دننۍ حلقه د ستنو لپاره. څرنګه چې دوه-بعدي لړیو ته عموماً قطار په قطار لاسرسی کېږي، نو د قطار شاخص د بهرنۍ حلقې او د ستنې شاخص د دننۍ حلقې په توګه کارېږي.')
    P('Consider the following program used to access the elements of the array, anArray[3][5], initialized in the above section and display them on the screen in a matrix form.',
      'درج ذیل پروگرام پر غور کریں جو اوپر کے حصے میں ابتدائی قدر دیے گئے ایرے anArray[3][5] کے عناصر تک رسائی کر کے انھیں اسکرین پر میٹرکس کی شکل میں دکھاتا ہے۔',
      'لاندې پروګرام ته پام وکړئ چې په پورته برخه کې د لومړني ارزښت ورکړل شوې anArray[3][5] لړۍ عناصرو ته لاسرسی کوي او پر پرده یې د ماتریکس په بڼه ښيي.')
    code(t, '''// accessing two dimensional array using loop
#include <iostream.h>
#include <conio.h>
int main()
{
int anArray[3][5] =
{{ 1, 2, 3, 4, 5 },
{ 6, 7, 8, 9, 10 },
{ 11, 12, 13, 14, 15 }};
for ( int row=0; row<3; ++row)
{
for (int col=0; col<5; ++col)
cout<<anArray [row][col]<< ", ";
cout<<endl;
}
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''1, 2, 3, 4, 5
6, 7, 8, 9, 10
11, 12, 13, 14, 15''')
    t.h('b. Writing at an index of two dimensional array', 'b. دو جہتی ایرے کے کسی انڈیکس پر لکھنا', 'b. د دوه-بعدي لړۍ پر یوه شاخص لیکل')
    P('Loop is a better way of writing to the indices of a two dimensional array. Consider the following example:', 'دو جہتی ایرے کے انڈیسز پر لکھنے کا بہتر طریقہ لوپ ہے۔ درج ذیل مثال پر غور کریں:', 'د دوه-بعدي لړۍ پر شاخصونو د لیکلو ښه لاره حلقه ده. لاندې بېلګې ته پام وکړئ:')
    code(t, '''// writing in a two dimensional array using loop
#include <iostream.h>
#include <conio.h>
int main()
{
int A[2][3];
cout<< "Kindly enter values for the array"<<endl;
for (int i = 0; i < 2; i++)
for (int j = 0; j < 3; j++)
cin>> A[i][j]; // writing to the array
cout<< "Values of the array are:"<<endl;
for (int i = 0; i < 2; i++)
{
for (int j = 0; j < 3; j++)
cout << A[i][j]<< "\\t"; //accessing of the array
cout<<endl;
}
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''2 -1 7 1 0 10
Values of the array are:
2 -1 7
1 0 10''')
    BOOK.save(86, [(5, rec(t, 8, 86, [160, 161]))], issues=[{'id': 'cs12-pdf086', 'unit': 5, 'printedPage': 161,
               'description': 'The writing program output omits the “Kindly enter values for the array” prompt; the accessing output omits the trailing “, ”. Retained as printed.'}])


def p87():
    t = Builder()
    P = t.p
    t.h('5.3 Strings', '5.3 اسٹرنگز', '۵.۳ تارونه')
    t.h('5.3.1 What is String?', '5.3.1 اسٹرنگ کیا ہے؟', '۵.۳.۱ تار څه دی؟')
    P('The sequence of characters enclosed in quotation marks and is used to handle non-numeric data i.e. names, addresses etc. are called strings.',
      'واوین میں بند حروف کی ترتیب جو غیر عددی ڈیٹا یعنی نام، پتے وغیرہ سنبھالنے کے لیے استعمال ہوتی ہے، اسٹرنگز کہلاتی ہے۔',
      'په نقل‌قولونو کې تړلې د تورو لړۍ چې د غیر عددي ډېټا یعنې نومونو، پتو او نورو د چلولو لپاره کارېږي، تارونه (strings) بلل کېږي.')
    t.h('5.3.2 Defining a C String', '5.3.2 C اسٹرنگ کی تعریف', '۵.۳.۲ د C تار تعریف')
    P('General syntax for defining string in C is given below:', 'C میں اسٹرنگ کی تعریف کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے:', 'په C کې د تار د تعریف عمومي بڼه لاندې ورکړل شوې:')
    code(t, 'data type name_of_string [size of string];')
    P('In the above general syntax, data type, is char data type and name_of_string is the name of the string. The size (number of characters) of the string is specified in square brackets, [ ]. The following statement defines a string with the name str having size 20.',
      'اوپر کے عمومی طریقۂ تحریر میں data type، char ڈیٹا ٹائپ ہے اور name_of_string اسٹرنگ کا نام ہے۔ اسٹرنگ کا سائز (حروف کی تعداد) مربع بریکٹس [ ] میں بتایا جاتا ہے۔ درج ذیل بیان str نام کی 20 سائز والی اسٹرنگ کی تعریف کرتا ہے۔',
      'په پورته عمومي بڼه کې data type د char ډېټا ډول دی او name_of_string د تار نوم دی. د تار اندازه (د تورو شمېر) په مربع قوسونو [ ] کې ښودل کېږي. لاندې بیان د str په نوم د ۲۰ اندازې تار تعریفوي.')
    code(t, 'char str [20];')
    P('For handling strings, the header file <cstring> is needed but in some implementations this library may be automatically included when the header file <iostream> is included. There are some limitations of strings in C. To overcome and remove these problems, C++ provides a class <string> that removes many of these problems. This class provides some typical string operations like comparison, concatenation, find and replace, and a function for obtaining substrings. The general syntax for defining strings in C++ is given below:',
      'اسٹرنگز سنبھالنے کے لیے ہیڈر فائل <cstring> درکار ہے لیکن بعض نفاذ میں یہ لائبریری ہیڈر فائل <iostream> شامل کرنے پر خود بخود شامل ہو سکتی ہے۔ C میں اسٹرنگز کی کچھ حدود ہیں۔ ان مسائل پر قابو پانے اور انھیں دور کرنے کے لیے C++ ایک کلاس <string> فراہم کرتی ہے جو ان میں سے بہت سے مسائل دور کرتی ہے۔ یہ کلاس کچھ عام اسٹرنگ آپریشنز جیسے موازنہ، جوڑنا، تلاش اور تبدیلی، اور ذیلی اسٹرنگز حاصل کرنے کا فنکشن فراہم کرتی ہے۔ C++ میں اسٹرنگز کی تعریف کا عمومی طریقۂ تحریر ذیل میں ہے:',
      'د تارونو د چلولو لپاره د <cstring> سرپاڼه دوتنې ته اړتیا ده، خو په ځینو پلیو کې دا کتابتون د <iostream> سرپاڼه دوتنې په شاملولو پخپله شامل کېدای شي. په C کې د تارونو ځینې محدودیتونه دي. د دې ستونزو د لرې کولو لپاره C++ د <string> ټولګی برابروي چې ډېرې دا ستونزې لرې کوي. دا ټولګی ځینې عادي د تار عملیې لکه پرتله، نښلول، موندل او بدلول، او د فرعي تارونو د ترلاسه کولو فنکشن برابروي. په C++ کې د تارونو د تعریف عمومي بڼه لاندې ده:')
    code(t, 'string str;')
    P('This statement defines a string name str of type string.', 'یہ بیان string قسم کی str نام کی اسٹرنگ کی تعریف کرتا ہے۔', 'دا بیان د string ډول د str په نوم تار تعریفوي.')
    t.h('5.3.3 Initializing string', '5.3.3 اسٹرنگ کو ابتدائی قدر دینا', '۵.۳.۳ تار ته لومړنی ارزښت ورکول')
    P('1. Strings in C can be initialized as arrays are initialized because string is a character array.', '1۔ C میں اسٹرنگز کو اسی طرح ابتدائی قدر دی جا سکتی ہے جیسے ایریز کو، کیونکہ اسٹرنگ حروف کا ایرے ہے۔', '۱. په C کې تارونو ته د لړیو په څېر لومړنی ارزښت ورکول کېدای شي ځکه تار د تورو لړۍ ده.')
    P('Consider the following example:', 'درج ذیل مثال پر غور کریں:', 'لاندې بېلګې ته پام وکړئ:')
    code(t, "char greeting [6] = { 'H', 'e', 'l', 'l', 'o', '\\0' };")
    P('The above statement declares a string named “greeting” with six elements of type char that are initialized with the characters that form the word "Hello" plus a null character \'\\0\' at the end. Another method for initializing a string in C is to enclose the string in double quotes, "" as shown below:',
      'اوپر کا بیان ’’greeting‘‘ نام کی اسٹرنگ ڈکلیئر کرتا ہے جس کے char قسم کے چھ عناصر ہیں جنھیں لفظ "Hello" بنانے والے حروف اور آخر میں ایک null حرف \'\\0\' سے ابتدائی قدر دی گئی ہے۔ C میں اسٹرنگ کو ابتدائی قدر دینے کا ایک اور طریقہ اسٹرنگ کو ڈبل کوٹس "" میں بند کرنا ہے جیسا کہ ذیل میں دکھایا گیا ہے:',
      'پورته بیان د "greeting" په نوم یو تار اعلانوي چې د char ډول شپږ عناصر لري او د "Hello" کلمې جوړوونکو تورو او په پای کې د null توري \'\\0\' سره لومړنی ارزښت ورکړل شوی. په C کې تار ته د لومړني ارزښت ورکولو بله لاره دا ده چې تار په دوه‌ګونو نقل‌قولونو "" کې وتړل شي لکه لاندې:')
    code(t, 'char greeting [ ] = “Hello”;')
    P('In both cases, the array of characters greeting is declared with a size of 6 elements of type char: the 5 characters that compose the word “Hello” plus a final null character (\'\\0\') which specifies the end of the sequence and that, in the second case, when using double quotes (") it is appended automatically.',
      'دونوں صورتوں میں حروف کا ایرے greeting، char قسم کے 6 عناصر کے سائز سے ڈکلیئر ہوتا ہے: لفظ ’’Hello‘‘ بنانے والے 5 حروف اور ایک آخری null حرف (\'\\0\') جو ترتیب کا اختتام بتاتا ہے، اور دوسری صورت میں ڈبل کوٹس (") استعمال کرنے پر یہ خود بخود شامل ہو جاتا ہے۔',
      'په دواړو حالتونو کې د تورو لړۍ greeting د char ډول ۶ عناصرو په اندازه اعلانېږي: د "Hello" کلمې جوړوونکي ۵ توري او یو وروستی null توری (\'\\0\') چې د لړۍ پای ښيي، او په دویم حالت کې د دوه‌ګونو نقل‌قولونو (") په کارولو پخپله ورزیاتېږي.')
    P('Consider an example to ask for your name and then display a greeting message on the screen as shown below using string:', 'ایک مثال پر غور کریں جو اسٹرنگ کے ذریعے آپ کا نام پوچھتی ہے اور پھر اسکرین پر خوش آمدیدی پیغام دکھاتی ہے جیسا کہ ذیل میں ہے:', 'یوې بېلګې ته پام وکړئ چې د تار په مرسته ستاسو نوم پوښتي او بیا پر پرده د ښه راغلاست پیغام ښيي لکه لاندې:')
    code(t, '''#include <iostream.h>
#include<conio.h>
int main()
{
char question[] = "Please, enter your first name: ";
char greeting[] = "Hello, ";
char yourname [80];
cout << question;
cin >> yourname;
cout << greeting << yourname << "!";
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Please, enter your first name:
Rahman
Hello, Rahman!''')
    BOOK.save(87, [(5, rec(t, 9, 87, [162, 163, 164], 'The greeting program continues on p.164 (PDF88) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf087', 'unit': 5, 'printedPage': 163,
                       'description': 'p.162 “The sequence of characters … and is used … are called strings”; p.163 prints “type char:” as “type char.” and uses curly quotes in char greeting [ ] = “Hello”;. Retained as printed.'}])


def p88():
    t = Builder()
    P = t.p
    P('2. Strings in C++ can be initialized both ways like in C and directly like ordinary variables with the only difference that the string should be enclosed in double quotes. Consider the following initialization examples:',
      '2۔ C++ میں اسٹرنگز کو C کی طرح دونوں طریقوں سے اور عام ویری ایبلز کی طرح براہِ راست ابتدائی قدر دی جا سکتی ہے، فرق صرف یہ ہے کہ اسٹرنگ ڈبل کوٹس میں بند ہونی چاہیے۔ درج ذیل مثالوں پر غور کریں:',
      '۲. په C++ کې تارونو ته د C په څېر په دواړو لارو او د عادي متغیرونو په څېر مستقیم لومړنی ارزښت ورکول کېدای شي، یوازینی توپیر دا دی چې تار باید په دوه‌ګونو نقل‌قولونو کې وتړل شي. لاندې بېلګو ته پام وکړئ:')
    code(t, '''string str1("Call me");
string str2 = "Send sms!";
string str3("OKay");''')
    P('Here, in these examples three strings: str1, str2 and str3 are directly initialized to “Call me”, “Send sms” and “OKay” respectively. Note that while using C++ string in programs, the class string must be included.',
      'یہاں ان مثالوں میں تین اسٹرنگز str1، str2 اور str3 کو بالترتیب ’’Call me‘‘، ’’Send sms‘‘ اور ’’OKay‘‘ سے براہِ راست ابتدائی قدر دی گئی ہے۔ یاد رہے کہ پروگراموں میں C++ اسٹرنگ استعمال کرتے وقت string کلاس شامل کرنا ضروری ہے۔',
      'دلته په دې بېلګو کې درې تارونه str1، str2 او str3 په ترتیب سره "Call me"، "Send sms" او "OKay" ته مستقیم لومړنی ارزښت ورکړل شوي. پام وکړئ چې په پروګرامونو کې د C++ تار کارولو پر مهال باید string ټولګی شامل شي.')
    P('Consider the following program to demonstrate initialization of C++ string:', 'C++ اسٹرنگ کی ابتدائی قدر واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں:', 'د C++ تار د لومړني ارزښت د ښودلو لپاره لاندې پروګرام ته پام وکړئ:')
    code(t, '''// C++ strings initialization program
#include <iostream.h>
#include<conio.h>
#include<string>
int main()
{
string str1("Call me");
string str2 = "Send SMS";
string str3("OKay");
cout<< "First string str1 is: "<<str1<<endl;
cout<< "Second string str2 is: "<<str2<<endl;
cout<< "Third string str3 is: "<<str3<<endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''First string str1 is: Call me
Second string str2 is: Send SMS
Third string str3 is: Okay''')
    P('The following program demonstrates some more features of C++ string e.g. concatenation, copying and finding size of string.', 'درج ذیل پروگرام C++ اسٹرنگ کی کچھ مزید خصوصیات جیسے جوڑنا، نقل کرنا اور اسٹرنگ کا سائز معلوم کرنا واضح کرتا ہے۔', 'لاندې پروګرام د C++ تار نور ځانګړتیاوې لکه نښلول، کاپي کول او د تار اندازه موندل ښيي.')
    code(t, '''#include <iostream.h>
#include<conio.h>
#include<string>
int main()
{
string str1="Hello";
string str2 = "World";
string str3, str4;
int len;
str3 = str1; // String copying
str4 = str1 + str2; // String concatenation
len = str4.size( ); // Finds string size
cout<<"str3=\\t"<<str3<<endl;
cout<<"str4=\\t"<<str4<<endl;
cout<<"length of str4 = \\t"<<len<<endl;
getch();
}''')
    P(*OUT)
    code(t, '''str3=   Hello
str4=   HelloWorld
length of str4      = 10''')
    BOOK.save(88, [(5, rec(t, 10, 88, [164, 165, 166], 'The top of p.164 (end of the greeting program and its output) is recorded with PDF87. The concatenation/size program runs to p.166 (PDF89) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf088', 'unit': 5, 'printedPage': 165,
                       'description': 'The initialization program sets str3 to "OKay" but the printed output shows “Okay”; the example list uses "Send sms!" while the text says “Send sms”. Retained as printed.'}])


def p89():
    t = Builder()
    P = t.p
    t.h('5.3.4 Commonly used string functions', '5.3.4 عام استعمال ہونے والے اسٹرنگ فنکشنز', '۵.۳.۴ عام کارېدونکي د تار فنکشنونه')
    P('The header file string provides many string manipulation functions. These are discussed with the help of programs as follows.', 'ہیڈر فائل string اسٹرنگ میں تبدیلی کے بہت سے فنکشنز فراہم کرتی ہے۔ ان پر پروگراموں کی مدد سے ذیل میں بات کی گئی ہے۔', 'د string سرپاڼه دوتنه د تار د بدلون ډېر فنکشنونه برابروي. دا د پروګرامونو په مرسته لاندې څېړل شوي.')
    t.h('a. Concatenation of strings', 'a. اسٹرنگز کو جوڑنا', 'a. د تارونو نښلول')
    t.h('Strcat() function', 'Strcat() فنکشن', 'Strcat() فنکشن')
    P('Combining two strings into a single string is called string concatenation. Strcat() function is used for this purpose. The following program demonstrates the implementation of strcat() function for the concatenation of the two strings.',
      'دو اسٹرنگز کو ایک اسٹرنگ میں ملانا اسٹرنگ کنکیٹینیشن کہلاتا ہے۔ اس مقصد کے لیے Strcat() فنکشن استعمال ہوتا ہے۔ درج ذیل پروگرام دو اسٹرنگز کو جوڑنے کے لیے strcat() فنکشن کا نفاذ دکھاتا ہے۔',
      'د دوو تارونو یو تار ته یوځای کول د تار نښلول بلل کېږي. د دې موخې لپاره Strcat() فنکشن کارېږي. لاندې پروګرام د دوو تارونو د نښلولو لپاره د strcat() فنکشن پلي کول ښيي.')
    code(t, '''// strings concatenation program
#include <iostream.h>
#include <string.h>
#include<conio.h>
int main()
{
char FirstName[15] = "SSC ";
char LastName[15] = "Computer";
strcat(FirstName, LastName);
cout << FirstName;
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'SSC Computer')
    t.h('b. Copying of strings', 'b. اسٹرنگز کی نقل', 'b. د تارونو کاپي کول')
    t.h('copy() function', 'copy() فنکشن', 'copy() فنکشن')
    P('copy() function is used to copy one string to another string. The general syntax of copy function is given below:', 'copy() فنکشن ایک اسٹرنگ کو دوسری اسٹرنگ میں نقل کرنے کے لیے استعمال ہوتا ہے۔ copy فنکشن کا عمومی طریقۂ تحریر ذیل میں ہے:', 'copy() فنکشن د یوه تار بل تار ته د کاپي کولو لپاره کارېږي. د copy فنکشن عمومي بڼه لاندې ده:')
    code(t, 'str.copy (string_name, number_of_characters, starting_pointer)')
    P('Here, the string_name is the name of the string to which the string is to be copied. number_of_characters represents the exacts number of characters to be copied and starting_pointer indicates the starting point from where to copy. Consider the following program:',
      'یہاں string_name اس اسٹرنگ کا نام ہے جس میں اسٹرنگ نقل کی جانی ہے۔ number_of_characters نقل کیے جانے والے حروف کی درست تعداد ظاہر کرتا ہے اور starting_pointer وہ نقطۂ آغاز بتاتا ہے جہاں سے نقل کرنا ہے۔ درج ذیل پروگرام پر غور کریں:',
      'دلته string_name د هغه تار نوم دی چې تار پکې کاپي کېږي. number_of_characters د کاپي کېدونکو تورو دقیق شمېر ښيي او starting_pointer د پیل ټکی ښيي چې له کومه ځایه کاپي شي. لاندې پروګرام ته پام وکړئ:')
    code(t, '''// strings copying program using copy() function
''' + HDR + '''
int main()
{
string str = "Welcome to C++ Strings";
char x[55];
cout << "str is: " << str << endl;
str.copy(x, 7, 0); // copy 7 characters of string str into string x, starting from position zero
cout << "The copied string is: " << x << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Welcome to C++ Strings
The copied string is: Welcome''')
    BOOK.save(89, [(5, rec(t, 11, 89, [166, 167, 168], 'The top of p.166 (end of the concatenation/size program) is recorded with PDF88. The copy() program runs from p.167 to p.168 (PDF90) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf089', 'unit': 5, 'printedPage': 167,
                       'description': 'p.167 “represents the exacts number of characters”; the copy() output omits the “str is: ” prefix. Retained as printed. Owner signature on p.167 excluded.'}])


def p90():
    t = Builder()
    P = t.p
    t.h('strcpy() function', 'strcpy() فنکشن', 'strcpy() فنکشن')
    P('For copying string, another string function strcpy() can also be used. Consider the following program to demonstrate the use of strcpy().', 'اسٹرنگ نقل کرنے کے لیے ایک اور اسٹرنگ فنکشن strcpy() بھی استعمال ہو سکتا ہے۔ strcpy() کا استعمال واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د تار د کاپي کولو لپاره د تار بل فنکشن strcpy() هم کارول کېدای شي. د strcpy() د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''// copying string using strcpy() function
''' + HDR + '''
main()
{
string SS;
char CC[17];
SS = "This is a string";
strcpy(CC,"This is a string");
cout << SS << endl; cout << CC << endl;
getch();
}''')
    P(*OUT)
    code(t, '''This is a string
This is a string''')
    t.h('c. Finding a character or word in a strings', 'c. اسٹرنگ میں کوئی حرف یا لفظ تلاش کرنا', 'c. په تار کې یو توری یا کلمه موندل')
    t.h('find() function', 'find() فنکشن', 'find() فنکشن')
    P('To find a particular word or a character in a string, find () function is used. find () function takes only one argument which is the desired character or word within the string. The following program demonstrates how find() function is used to search the word interesting and character g in the string “C++ is a very interesting programming language”.',
      'اسٹرنگ میں کوئی خاص لفظ یا حرف تلاش کرنے کے لیے find () فنکشن استعمال ہوتا ہے۔ find () فنکشن صرف ایک آرگیومنٹ لیتا ہے جو اسٹرنگ کے اندر مطلوبہ حرف یا لفظ ہے۔ درج ذیل پروگرام دکھاتا ہے کہ اسٹرنگ ’’C++ is a very interesting programming language‘‘ میں لفظ interesting اور حرف g تلاش کرنے کے لیے find() فنکشن کیسے استعمال ہوتا ہے۔',
      'په تار کې د یوې ځانګړې کلمې یا توري موندلو لپاره find () فنکشن کارېږي. find () فنکشن یوازې یو دلیل اخلي چې د تار دننه غوښتل شوی توری یا کلمه ده. لاندې پروګرام ښيي چې په "C++ is a very interesting programming language" تار کې د interesting کلمې او g توري د لټولو لپاره find() فنکشن څنګه کارېږي.')
    code(t, '''// finding a word or character using find() function
#include <iostream.h>
#include <string>
#include<conio.h>
main()
{
string str("C++ is a very interesting programming language");
int loc1, loc2;
loc1 = str.find ("interesting ");
cout << "Word interesting is found on position: " <<loc1+1;
loc2 = str.find('g');
cout << "\\nFirst character 'g' found on position: "<< loc2;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Word interesting is found on position: 15

First character 'g' found on position: 24''')
    BOOK.save(90, [(5, rec(t, 12, 90, [168, 169, 170], 'The top of p.168 (end of the copy() program) is recorded with PDF89. The find() program continues on p.170 (PDF91) and is given whole with its output.'))],
              issues=[{'id': 'cs12-pdf090', 'unit': 5, 'printedPage': 169,
                       'description': 'Heading “Finding a character or word in a strings”; main() without a return type; the “g” position output (24) is printed as given. Retained as printed.'}])


def p91():
    t = Builder()
    P = t.p
    t.h('d. Finding length of a strings', 'd. اسٹرنگ کی لمبائی معلوم کرنا', 'd. د تار اوږدوالی موندل')
    t.h('length() function', 'length() فنکشن', 'length() فنکشن')
    P('To find the length of a string, length () function is used. Consider the following program to demonstrate working of the length () function.', 'اسٹرنگ کی لمبائی معلوم کرنے کے لیے length () فنکشن استعمال ہوتا ہے۔ length () فنکشن کا عمل واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د تار د اوږدوالي موندلو لپاره length () فنکشن کارېږي. د length () فنکشن د کار د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, HDR + '''
main()
{
string str("C++ is a very interesting programming language");
cout << "Length of the given string is: "<< str.length();
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'Length of the given string is: 46')
    t.h('e. Swapping strings', 'e. اسٹرنگز کا تبادلہ', 'e. د تارونو تبادله')
    t.h('swap() function', 'swap() فنکشن', 'swap() فنکشن')
    P('To swap (or interchange) values of two strings, swap() function is used. Consider the following program to demonstrate working of swap () function.', 'دو اسٹرنگز کی قدروں کا تبادلہ (یا ادل بدل) کرنے کے لیے swap() فنکشن استعمال ہوتا ہے۔ swap () فنکشن کا عمل واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د دوو تارونو د ارزښتونو د تبادلې (یا اړول) لپاره swap() فنکشن کارېږي. د swap () فنکشن د کار د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, HDR + '''
int main()
{
string str1 = "F.Sc Part I";
string str2 = "F.Sc Part II";
cout << "str1 is: " << str1 << endl;
cout << "str2 is: " << str2 << endl;
str1.swap(str2);
cout << "str1 is: " << str1 << endl;
cout << "str2 is: " << str2 << endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''str1 is: F.Sc Part I
str2 is: F.Sc Part II
str1 is: F.Sc Part II
str2 is: F.Sc Part I''')
    BOOK.save(91, [(5, rec(t, 13, 91, [170, 171], 'The top of p.170 (end of the find() program and its output) is recorded with PDF90.'))])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 86
    {86: p86, 87: p87, 88: p88, 89: p89, 90: p90, 91: p91}[n]()
