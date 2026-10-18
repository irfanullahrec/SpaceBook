"""Computer Science XII PDF42 (spread): printed pp.72–73 — initialization example; 3.2.4 fundamental data types; a. character; b. integer (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Consider the following program to demonstrate the initialization of variables.', 'ویری ایبلز کی ابتدائی قدر کی وضاحت کے لیے درج ذیل پروگرام پر غور کریں۔', 'د متغیرونو د لومړني ارزښت د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
code(t, '''#include<conio.h>
#include <iostream.h>
int main()
{
int Vara=55; // initial value = 55
int Varb(22); // initial value = 22
int result; // initial value undetermined
result = Vara - Varb;
cout << "The Result is= "<<result;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'The Result is= 33')
H('3.2.4 Fundamental data types in C++', '3.2.4 C++ میں بنیادی ڈیٹا ٹائپس', '۳.۲.۴ په C++ کې بنسټیز ډېټا ډولونه')
P('While programming, we store the variables in computer’s memory, but the computers have to know that what kind of data we want to store in them.',
  'پروگرامنگ کرتے وقت ہم ویری ایبلز کو کمپیوٹر کی میموری میں محفوظ کرتے ہیں، لیکن کمپیوٹر کو معلوم ہونا چاہیے کہ ہم ان میں کس قسم کا ڈیٹا محفوظ کرنا چاہتے ہیں۔',
  'د پروګرام‌سازۍ پر وخت موږ متغیرونه د کمپیوټر په حافظه کې ساتو، خو کمپیوټر باید پوه شي چې موږ پکې څه ډول ډېټا ساتل غواړو.')
P('Data type tells the compiler that what types of data, means integer, character or floating point etc. the variable will store and what will be the range of the values.',
  'ڈیٹا ٹائپ کمپائلر کو بتاتی ہے کہ ویری ایبل کس قسم کا ڈیٹا، یعنی صحیح عدد، حرف یا فلوٹنگ پوائنٹ وغیرہ، محفوظ کرے گا اور قدروں کی حد کیا ہوگی۔',
  'ډېټا ډول کمپایلر ته وايي چې متغیر به څه ډول ډېټا، یعنې صحیح عدد، توری یا اعشاري عدد او نور، ساتي او د ارزښتونو حد به څه وي.')
P('The most commonly used data types in C++ are:', 'C++ میں سب سے زیادہ استعمال ہونے والی ڈیٹا ٹائپس یہ ہیں:', 'په C++ کې تر ټولو ډېر کارېدونکي ډېټا ډولونه دا دي:')
t.group('list', [('Character', 'حرف (کریکٹر)', 'توری'), ('Integer', 'صحیح عدد (انٹیجر)', 'صحیح عدد'), ('Floating point', 'فلوٹنگ پوائنٹ', 'اعشاري عدد'), ('Boolean', 'بولین', 'بولي'), ('Unsigned', 'ان سائنڈ', 'بې‌نښې (Unsigned)')])
H('a. Character data type', 'a. حرفی ڈیٹا ٹائپ', 'a. د توري ډېټا ډول')
P('The char keyword represents the character data type in C++. Any character belonging to the ASCII character set is called a character data type. The maximum size of char data type is 8 bits (1 byte). Signed char and unsigned char are its two distinct types. They occupy the same amount of memory space. Consider the following line of code:',
  'char کی ورڈ C++ میں حرفی ڈیٹا ٹائپ کی نمائندگی کرتا ہے۔ ASCII حروف کے مجموعے سے تعلق رکھنے والا کوئی بھی حرف حرفی ڈیٹا ٹائپ کہلاتا ہے۔ char ڈیٹا ٹائپ کا زیادہ سے زیادہ سائز 8 بٹس (1 بائٹ) ہے۔ signed char اور unsigned char اس کی دو الگ اقسام ہیں جو میموری میں یکساں جگہ لیتی ہیں۔ کوڈ کی درج ذیل لائن پر غور کریں:',
  'د char کلیدي کلمه په C++ کې د توري ډېټا ډول ښيي. هر توری چې د ASCII تورو له ټولګې سره تړاو ولري، د توري ډېټا ډول بلل کېږي. د char ډېټا ډول اعظمي اندازه ۸ بټه (۱ بایټ) ده. signed char او unsigned char یې دوه جلا ډولونه دي چې په حافظه کې یو شان ځای نیسي. د کوډ لاندې کرښې ته پام وکړئ:')
code(t, 'char x;')
P('Here, x is a character type variable that occupies 1 byte of memory. Variables declared as char data type are used to store character constants. Character constants are always represented with single quotes. For example:',
  'یہاں x حرفی قسم کا ویری ایبل ہے جو میموری کا 1 بائٹ لیتا ہے۔ char ڈیٹا ٹائپ کے طور پر ڈکلیئر کیے گئے ویری ایبلز حرفی کانسٹنٹس محفوظ کرنے کے لیے استعمال ہوتے ہیں۔ حرفی کانسٹنٹس ہمیشہ ایک واوین میں ظاہر کیے جاتے ہیں۔ مثلاً:',
  'دلته x د توري ډول متغیر دی چې د حافظې ۱ بایټ نیسي. هغه متغیرونه چې د char ډېټا ډول په توګه اعلان شوي، د توري ثابتونو د ساتلو لپاره کارول کېږي. د توري ثابتونه تل په یوګوني نقل‌قولونو کې ښودل کېږي. د بېلګې په توګه:')
code(t, '''char gender;
gender= 'M';''')
P('Here, gender is a character type variable that occupies 1 byte of memory and store character constant, M, which stands for Male.',
  'یہاں gender حرفی قسم کا ویری ایبل ہے جو میموری کا 1 بائٹ لیتا ہے اور حرفی کانسٹنٹ M محفوظ کرتا ہے جس کا مطلب Male (مرد) ہے۔',
  'دلته gender د توري ډول متغیر دی چې د حافظې ۱ بایټ نیسي او د توري ثابت M ساتي چې د Male (نارینه) معنا لري.')
H('b. Integer data types', 'b. انٹیجر ڈیٹا ٹائپس', 'b. صحیح عدد ډېټا ډولونه')
P('The data types which store only integer numbers such as 100, -200 etc. are called integer data types. Its sub types are:',
  'وہ ڈیٹا ٹائپس جو صرف صحیح اعداد جیسے 100، -200 وغیرہ محفوظ کرتی ہیں، انٹیجر ڈیٹا ٹائپس کہلاتی ہیں۔ اس کی ذیلی اقسام یہ ہیں:',
  'هغه ډېټا ډولونه چې یوازې صحیح عددونه لکه 100، -200 او نور ساتي، صحیح عدد ډېټا ډولونه بلل کېږي. فرعي ډولونه یې دا دي:')
t.group('list', [('int', 'int', 'int'), ('short int', 'short int', 'short int'), ('long', 'long', 'long')])
rec = BOOK.record(t, 'cs12-u3-text-8', 'Unit 3 text (8)', 'یونٹ 3 — متن (۸)', '۳ څپرکی — متن (۸)', 42, [72, 73])
issues = [{'id': 'cs12-pdf042', 'unit': 3, 'printedPage': 72,
           'description': 'p.72 prints “know that what kind of data”, “tells the compiler that what types of data, means integer”; p.73 “occupies 1 byte of memory and store”. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(42, [(3, rec)], issues=issues)
