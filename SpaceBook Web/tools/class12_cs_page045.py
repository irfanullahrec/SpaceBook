"""Computer Science XII PDF45 (spread): printed pp.78–79 — explicit casting example; 3.3 I/O handling; 3.3.1 cout; 3.3.2 cin (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
code(t, '''int x;
float pi = 3.14;
x = (int) pi;''')
P('In the above code, the float number 3.14 is converted to an integer value 3 and the remainder is discarded. Here, the type casting operator is (int). Another way for explicit type casting is to precede the expression to be converted by the type and enclose the expression in parentheses. Consider the following line of code:',
  'اوپر والے کوڈ میں فلوٹ عدد 3.14 کو صحیح عدد 3 میں تبدیل کیا جاتا ہے اور باقی حصہ ترک کر دیا جاتا ہے۔ یہاں ٹائپ کاسٹنگ آپریٹر (int) ہے۔ صریح ٹائپ کاسٹنگ کا دوسرا طریقہ یہ ہے کہ تبدیل کیے جانے والے ایکسپریشن سے پہلے قسم لکھی جائے اور ایکسپریشن کو قوسین میں بند کیا جائے۔ کوڈ کی درج ذیل لائن پر غور کریں:',
  'په پورته کوډ کې اعشاري عدد 3.14 صحیح عدد 3 ته اړول کېږي او پاتې برخه پرېښودل کېږي. دلته د ډول بدلولو چلونکی (int) دی. د څرګند ډول بدلولو بله لاره دا ده چې د اړول کېدونکې افادې مخې ته ډول ولیکل شي او افاده په قوسونو کې وتړل شي. د کوډ لاندې کرښې ته پام وکړئ:')
code(t, 'x = int ( pi );')
H('3.3 Input/Output Handling', '3.3 ان پٹ/آؤٹ پٹ کا انتظام', '۳.۳ د ننوتو/وتو اداره')
P('For input/output operations, C++ uses streams in sequential media such as the screen or the keyboard. A stream is an object where a C++ program inserts characters to or extracts the characters from stream. All the standard input and output stream objects are declared within the header file iostream which is a part of the standard C++ library.',
  'ان پٹ/آؤٹ پٹ کے عمل کے لیے C++ ترتیبی ذرائع جیسے اسکرین یا کی بورڈ میں اسٹریمز استعمال کرتی ہے۔ اسٹریم ایک آبجیکٹ ہے جس میں C++ پروگرام حروف داخل کرتا ہے یا اس سے حروف نکالتا ہے۔ تمام معیاری ان پٹ اور آؤٹ پٹ اسٹریم آبجیکٹس ہیڈر فائل iostream میں ڈکلیئر ہوتے ہیں جو معیاری C++ لائبریری کا حصہ ہے۔',
  'د ننوتو/وتو عملیو لپاره C++ په ترتیبي رسنیو لکه پرده یا کیبورډ کې بهیرونه (streams) کاروي. بهیر یو شی دی چې C++ پروګرام پکې توري ورننباسي یا ترې توري راباسي. ټول معیاري د ننوتو او وتو بهیر شیان په iostream سرلیک فایل کې اعلان شوي چې د معیاري C++ کتابتون برخه ده.')
H('3.3.1 Standard output (cout)', '3.3.1 معیاری آؤٹ پٹ (cout)', '۳.۳.۱ معیاري وتنه (cout)')
P('The default standard output of a C++ program is the screen, and cout is the C++ stream object which defines it. cout is used in conjunction with the insertion operator, which is written as <<. Consider the following segment of code:',
  'C++ پروگرام کا طے شدہ معیاری آؤٹ پٹ اسکرین ہے، اور cout وہ C++ اسٹریم آبجیکٹ ہے جو اسے متعین کرتا ہے۔ cout کو انسرشن آپریٹر کے ساتھ استعمال کیا جاتا ہے جو << لکھا جاتا ہے۔ کوڈ کے درج ذیل حصے پر غور کریں:',
  'د C++ پروګرام ډیفالټ معیاري وتنه پرده ده، او cout د C++ هغه بهیر شی دی چې دا ټاکي. cout د ورننویستلو (insertion) چلونکي سره چې << لیکل کېږي، کارول کېږي. د کوډ لاندې برخې ته پام وکړئ:')
code(t, '''cout << "Output"; // prints Output on the screen
cout << 121; // prints number 121 on the screen
cout << var; // prints the content of 'var' on the screen''')
P('The insertion operator << inserts the data that follows it into the stream. In the above examples, it inserts the string “Output”, the numerical constant 121 and the value of the variable var into the standard output stream cout.',
  'انسرشن آپریٹر << اپنے بعد آنے والے ڈیٹا کو اسٹریم میں داخل کرتا ہے۔ اوپر کی مثالوں میں یہ اسٹرنگ ’’Output‘‘، عددی کانسٹنٹ 121 اور ویری ایبل var کی قدر کو معیاری آؤٹ پٹ اسٹریم cout میں داخل کرتا ہے۔',
  'د ورننویستلو چلونکی << له ځانه وروسته ډېټا بهیر ته ورننباسي. په پورته بېلګو کې دا "Output" تار، شمېریز ثابت 121 او د var متغیر ارزښت معیاري وتنې بهیر cout ته ورننباسي.')
P('The insertion operator << may be used more than once in a single statement. Consider the following line of code.',
  'انسرشن آپریٹر << ایک ہی بیان میں ایک سے زیادہ بار استعمال ہو سکتا ہے۔ کوڈ کی درج ذیل لائن پر غور کریں۔',
  'د ورننویستلو چلونکی << په یوه بیان کې له یو ځل زیات کارول کېدای شي. د کوډ لاندې کرښې ته پام وکړئ.')
code(t, 'cout << "Welcome " << "to " << "the first C++ statement";')
P('This statement prints the message “Welcome to the first C++ statement” on the screen as an output. The repetition of the insertion operator << is needed when more than one variables or combination of variables and constants are needed to print. Consider the following line of code.',
  'یہ بیان اسکرین پر آؤٹ پٹ کے طور پر پیغام ’’Welcome to the first C++ statement‘‘ پرنٹ کرتا ہے۔ انسرشن آپریٹر << کی تکرار اس وقت ضروری ہے جب ایک سے زیادہ ویری ایبلز یا ویری ایبلز اور کانسٹنٹس کا مجموعہ پرنٹ کرنا ہو۔ کوڈ کی درج ذیل لائن پر غور کریں۔',
  'دا بیان پر پرده د وتنې په توګه "Welcome to the first C++ statement" پیغام چاپوي. د ورننویستلو چلونکي << تکرار هغه وخت اړین دی چې له یوه زیات متغیرونه یا د متغیرونو او ثابتونو ګډون چاپ کړو. د کوډ لاندې کرښې ته پام وکړئ.')
code(t, 'cout << "Assalamoalaikum, I am a student of " << class << " Class";')
P('If the value of the variable class1 is 12 then the above statement would be:', 'اگر ویری ایبل class1 کی قدر 12 ہو تو اوپر والا بیان یوں ہوگا:', 'که د class1 متغیر ارزښت 12 وي، نو پورته بیان به داسې وي:')
code(t, 'Assalamoalaikum, I am a student of 12 Class')
H('3.3.2 Standard input (cin)', '3.3.2 معیاری ان پٹ (cin)', '۳.۳.۲ معیاري ننوتنه (cin)')
P('The standard input device used for entering input to the computer is keyboard. In C++, the stream extraction operator >> and object cin are used to handle the standard input. The operator >> must be followed by the variable that will store the data that is going to be extracted from the stream. Consider the following lines of code:',
  'کمپیوٹر میں ان پٹ داخل کرنے کے لیے استعمال ہونے والا معیاری ان پٹ آلہ کی بورڈ ہے۔ C++ میں اسٹریم ایکسٹریکشن آپریٹر >> اور آبجیکٹ cin معیاری ان پٹ کو سنبھالنے کے لیے استعمال ہوتے ہیں۔ آپریٹر >> کے بعد وہ ویری ایبل ہونا چاہیے جو اسٹریم سے نکالا جانے والا ڈیٹا محفوظ کرے گا۔ کوڈ کی درج ذیل لائنوں پر غور کریں:',
  'کمپیوټر ته د ننوتنې د لیکلو معیاري وسیله کیبورډ دی. په C++ کې د بهیر د راایستلو (extraction) چلونکی >> او cin شی د معیاري ننوتنې د سمبالولو لپاره کارول کېږي. د >> چلونکي وروسته باید هغه متغیر راشي چې له بهیر راایستل کېدونکې ډېټا ساتي. د کوډ لاندې کرښو ته پام وکړئ:')
code(t, '''int marks;
cin >> marks;''')
P('Here, the first statement, int marks; declares a variable of type int called ‘marks’, and the second statement waits for an input from cin in order to store it in this integer variable.',
  'یہاں پہلا بیان int marks; ایک int قسم کا ویری ایبل ’marks‘ ڈکلیئر کرتا ہے، اور دوسرا بیان cin سے ان پٹ کا انتظار کرتا ہے تاکہ اسے اس انٹیجر ویری ایبل میں محفوظ کیا جائے۔',
  'دلته لومړی بیان int marks; د int ډول یو متغیر چې ‘marks’ نومېږي اعلانوي، او دویم بیان له cin د ننوتنې انتظار کوي څو یې په دې صحیح عددي متغیر کې وساتي.')
rec = BOOK.record(t, 'cs12-u3-text-11', 'Unit 3 text (11)', 'یونٹ 3 — متن (۱۱)', '۳ څپرکی — متن (۱۱)', 45, [78, 79])
rec['sourceNote'] = 'The first listing is the code segment announced at the foot of p.77.'
issues = [{'id': 'cs12-pdf045', 'unit': 3, 'printedPage': 79,
           'description': 'p.79 uses the variable name “class” in the statement but refers to “class1” in the explanation (class is a C++ keyword); retained as printed. Also “when more than one variables … are needed to print”.'}]

if __name__ == '__main__':
    BOOK.save(45, [(3, rec)], issues=issues)
