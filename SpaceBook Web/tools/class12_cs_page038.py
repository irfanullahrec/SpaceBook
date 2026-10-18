"""Computer Science XII PDF38 (spread): printed pp.64–65 — single-line version; 3.1.4 statement terminator; 3.1.5 comments; comments example; 3.2 constants and variables; 3.2.1 a. constants."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Its single line version will be:', 'اس کا ایک لائن والا ورژن یہ ہوگا:', 'د هغه یو-کرښیزه نسخه به دا وي:')
code(t, 'int main() { cout << "Hello World!"; return 0; }')
H('3.1.4 Statement terminator (;)', '3.1.4 اسٹیٹمنٹ ٹرمینیٹر (;)', '۳.۱.۴ د بیان پای‌ټکی (;)')
P('Each C++ statement is terminated by a symbol named semicolon (;) which is called statement terminator. In C++, the separation between statements is specified with this ending semicolon (;) at the end of each statement. It does not matter to write more than one statement on a single line but matter if you do not separate them with semicolons. The use of each statement on a separate line is only to add clarity in the program.',
  'ہر C++ بیان سیمی کولن (;) نامی علامت سے ختم ہوتا ہے جسے اسٹیٹمنٹ ٹرمینیٹر کہتے ہیں۔ C++ میں بیانات کے درمیان علیحدگی ہر بیان کے آخر میں اس سیمی کولن (;) سے ظاہر کی جاتی ہے۔ ایک لائن پر ایک سے زیادہ بیان لکھنے سے کوئی فرق نہیں پڑتا لیکن انھیں سیمی کولنز سے الگ نہ کرنے سے فرق پڑتا ہے۔ ہر بیان کو الگ لائن پر لکھنا صرف پروگرام میں وضاحت پیدا کرنے کے لیے ہے۔',
  'هر C++ بیان د سیمي‌کولن (;) په نوم یوې نښې پای ته رسېږي چې د بیان پای‌ټکی بلل کېږي. په C++ کې د بیانونو ترمنځ جلاوالی د هر بیان په پای کې په دې سیمي‌کولن (;) ښودل کېږي. په یوه کرښه له یوه زیات بیانونه لیکل توپیر نه کوي، خو که یې په سیمي‌کولنونو جلا نه کړئ، توپیر کوي. په جلا کرښه د هر بیان لیکل یوازې پروګرام ته روښانتیا ورکوي.')
H('3.1.5 Comments and their syntax in C++', '3.1.5 C++ میں تبصرے اور ان کا طریقۂ تحریر', '۳.۱.۵ په C++ کې تبصرې او د لیکلو بڼه یې')
P('Comments are parts of the source code ignored by the compiler. They do nothing but simply increase the readability and understandability of a program. Their purpose is only to allow the programmers to insert notes or descriptions within the source code. C++ supports two types of comments:',
  'تبصرے سورس کوڈ کے وہ حصے ہیں جنھیں کمپائلر نظر انداز کرتا ہے۔ یہ کچھ نہیں کرتے بلکہ صرف پروگرام کو پڑھنے اور سمجھنے میں آسانی بڑھاتے ہیں۔ ان کا مقصد صرف پروگرامرز کو سورس کوڈ کے اندر نوٹس یا وضاحتیں شامل کرنے کی اجازت دینا ہے۔ C++ دو قسم کے تبصروں کو سپورٹ کرتی ہے:',
  'تبصرې د سرچینې کوډ هغه برخې دي چې کمپایلر یې له پامه غورځوي. هېڅ نه کوي، یوازې د پروګرام د لوستلو او پوهېدو وړتیا زیاتوي. موخه یې یوازې دا ده چې پروګرام جوړوونکي د سرچینې کوډ دننه یادښتونه یا تشریحات ورګډ کړي. C++ د دوو ډوله تبصرو ملاتړ کوي:')
H('a. Single line comment', 'a. ایک لائن کا تبصرہ', 'a. یو-کرښیزه تبصره')
P('It is represented by the double slash symbol //. It discards everything from where the pair of slashes signs // is found up to the end of the same line.',
  'اسے دوہری سلیش علامت // سے ظاہر کیا جاتا ہے۔ یہ جہاں سلیش کا جوڑا // ملے وہاں سے اسی لائن کے آخر تک ہر چیز کو نظر انداز کر دیتا ہے۔',
  'دا د دوه‌ګوني سلیش نښې // په مرسته ښودل کېږي. له هغه ځایه چې د سلیشونو جوړه // پیدا شي، د همغې کرښې تر پایه هر څه پرېږدي.')
H('b. Multiline comment', 'b. متعدد لائنوں کا تبصرہ', 'b. څو-کرښیزه تبصره')
P('These types of comments are represented by the symbols /* ....... */. It ignores everything between the /* characters and the first appearance of the */ characters, with the possibility of including more than one line.',
  'اس قسم کے تبصرے علامات /* ....... */ سے ظاہر کیے جاتے ہیں۔ یہ /* حروف اور */ حروف کی پہلی موجودگی کے درمیان ہر چیز کو نظر انداز کرتا ہے، اور اس میں ایک سے زیادہ لائنیں شامل ہو سکتی ہیں۔',
  'دا ډول تبصرې د /* ....... */ نښو په مرسته ښودل کېږي. د /* تورو او د */ تورو د لومړي راتلو ترمنځ هر څه پرېږدي، او کېدای شي له یوې زیاتې کرښې پکې شاملې وي.')
P('Consider the following program to demonstrate comments.', 'تبصروں کی وضاحت کے لیے درج ذیل پروگرام پر غور کریں۔', 'د تبصرو د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
code(t, '''/* program to demonstrate comments in C++*/
#include <iostream.h>
#include<conio.h>
int main()
{
cout << "Welcome! "; // prints Welcome!
cout << "I'm a C++ program demonstrating comments";
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Welcome!
I'm a C++ program''')
P('In the above example, the first two lines are multi-line comments while the comment at line 7 is a single line comment.',
  'اوپر والی مثال میں پہلی دو لائنیں متعدد لائنوں والے تبصرے ہیں جبکہ لائن 7 کا تبصرہ ایک لائن کا تبصرہ ہے۔',
  'په پورته بېلګه کې لومړۍ دوه کرښې څو-کرښیزې تبصرې دي، په داسې حال کې چې په ۷مه کرښه کې تبصره یو-کرښیزه ده.')
P('Comments are always ignored by the compiler when it compiles the program. If comments are included within the source code of your programs without using // or /*, the compiler will take them as if they were C++ expressions.',
  'کمپائلر پروگرام کمپائل کرتے وقت تبصروں کو ہمیشہ نظر انداز کرتا ہے۔ اگر آپ کے پروگراموں کے سورس کوڈ میں تبصرے // یا /* کے بغیر شامل کیے جائیں تو کمپائلر انھیں C++ ایکسپریشنز سمجھے گا۔',
  'کمپایلر د پروګرام د کمپایلولو پر وخت تبصرې تل له پامه غورځوي. که ستاسو د پروګرامونو په سرچینې کوډ کې تبصرې پرته د // یا /* کارولو ورګډې شي، کمپایلر به یې د C++ افادو په توګه ونیسي.')
H('3.2 C++ Constants and Variables', '3.2 C++ کانسٹنٹس اور ویری ایبلز', '۳.۲ د C++ ثابتونه او متغیرونه')
P('Variables and constants are the important components of every programming language.', 'ویری ایبلز اور کانسٹنٹس ہر پروگرامنگ زبان کے اہم اجزاء ہیں۔', 'متغیرونه او ثابتونه د هرې پروګرامي ژبې مهمې برخې دي.')
H('3.2.1 Constants and Variables', '3.2.1 کانسٹنٹس اور ویری ایبلز', '۳.۲.۱ ثابتونه او متغیرونه')
H('a. Constants', 'a. کانسٹنٹس', 'a. ثابتونه')
P('Constants are the expressions which have fixed value. Constants are generally categorized into: Literal, Boolean and Symbolic constants. They are used to express particular values within the source code of a program.',
  'کانسٹنٹس وہ ایکسپریشنز ہیں جن کی قدر مقررہ ہوتی ہے۔ کانسٹنٹس کو عموماً لٹرل، بولین اور علامتی کانسٹنٹس میں تقسیم کیا جاتا ہے۔ یہ کسی پروگرام کے سورس کوڈ میں مخصوص قدریں ظاہر کرنے کے لیے استعمال ہوتے ہیں۔',
  'ثابتونه هغه افادې دي چې ټاکلی ارزښت لري. ثابتونه عموماً په لفظي (literal)، بولي (Boolean) او سمبولیکو ثابتونو وېشل کېږي. د یوه پروګرام د سرچینې کوډ دننه د ځانګړو ارزښتونو د ښودلو لپاره کارول کېږي.')
rec = BOOK.record(t, 'cs12-u3-text-4', 'Unit 3 text (4)', 'یونٹ 3 — متن (۴)', '۳ څپرکی — متن (۴)', 38, [64, 65])
rec['sourceNote'] = 'The first three lines of p.64 complete the listing recorded with PDF37.'
issues = [{'id': 'cs12-pdf038', 'unit': 3, 'printedPage': 65,
           'description': 'p.65 says the comment “at line 7” is single-line but in the listing as printed it is on line 7 counting from the first comment line (retained). The output shown omits “demonstrating comments” (printed “I’m a C++ program”) — retained as printed. p.64 “pair of slashes signs”, “does not matter … but matter if”. Section number printed “3.2.”'}]

if __name__ == '__main__':
    BOOK.save(38, [(3, rec)], issues=issues)
