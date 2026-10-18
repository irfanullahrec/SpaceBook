"""Computer Science XII PDF43 (spread): printed pp.74–75 — int / short int / long int; c. floating point (float, double, long double); d. Boolean; e. unsigned."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('i. int data type', 'i. int ڈیٹا ٹائپ', 'i. د int ډېټا ډول')
P('The keyword int stands for the integer data type in C++ and normally has two bytes of memory (16 bits). A 16 bit integer may fall in the range of $-2^{15}$ to $2^{15}-1$, which means that it can store values in the range of -32768 to 32767.',
  'کی ورڈ int، C++ میں انٹیجر ڈیٹا ٹائپ کے لیے ہے اور عام طور پر میموری کے دو بائٹس (16 بٹس) لیتا ہے۔ 16 بٹ کا انٹیجر $-2^{15}$ سے $2^{15}-1$ کی حد میں ہو سکتا ہے، یعنی یہ -32768 سے 32767 تک کی قدریں محفوظ کر سکتا ہے۔',
  'د int کلیدي کلمه په C++ کې د صحیح عدد ډېټا ډول ښيي او عموماً د حافظې دوه بایټه (۱۶ بټه) لري. یو ۱۶-بټه صحیح عدد د $-2^{15}$ تر $2^{15}-1$ په حد کې کېدای شي، یعنې د -32768 تر 32767 پورې ارزښتونه ساتلی شي.')
H('ii. short int data type', 'ii. short int ڈیٹا ٹائپ', 'ii. د short int ډېټا ډول')
P('short int is used to declare the short integer data type in C++. The maximum size of the short int data type is 2 bytes (16 bits). It may fall in the range $-2^{15}$ to $2^{15}-1$, which means that it can store the values from -32768 to 32767.',
  'short int، C++ میں شارٹ انٹیجر ڈیٹا ٹائپ ڈکلیئر کرنے کے لیے استعمال ہوتا ہے۔ short int ڈیٹا ٹائپ کا زیادہ سے زیادہ سائز 2 بائٹس (16 بٹس) ہے۔ یہ $-2^{15}$ سے $2^{15}-1$ کی حد میں ہو سکتا ہے، یعنی -32768 سے 32767 تک کی قدریں محفوظ کر سکتا ہے۔',
  'short int په C++ کې د لنډ صحیح عدد ډېټا ډول د اعلان لپاره کارول کېږي. د short int اعظمي اندازه ۲ بایټه (۱۶ بټه) ده. د $-2^{15}$ تر $2^{15}-1$ په حد کې کېدای شي، یعنې له -32768 تر 32767 ارزښتونه ساتلی شي.')
H('iii. long int data type', 'iii. long int ڈیٹا ٹائپ', 'iii. د long int ډېټا ډول')
P('long int stands for long integer data type and is used in C++ to store larger integer values. Its size is 4 bytes (32 bits) which means that it can stores values in the range of -2147483648 to 2147483647.',
  'long int سے مراد لانگ انٹیجر ڈیٹا ٹائپ ہے اور یہ C++ میں بڑی صحیح عددی قدریں محفوظ کرنے کے لیے استعمال ہوتا ہے۔ اس کا سائز 4 بائٹس (32 بٹس) ہے، یعنی یہ -2147483648 سے 2147483647 تک کی قدریں محفوظ کر سکتا ہے۔',
  'long int د اوږد صحیح عدد ډېټا ډول دی او په C++ کې د لویو صحیح عددي ارزښتونو د ساتلو لپاره کارول کېږي. اندازه یې ۴ بایټه (۳۲ بټه) ده، یعنې له -2147483648 تر 2147483647 پورې ارزښتونه ساتلی شي.')
H('c. Floating point data type', 'c. فلوٹنگ پوائنٹ ڈیٹا ٹائپ', 'c. اعشاري ډېټا ډول')
P('Integers are only used for storing whole numbers, but sometimes we need to store very large numbers, or numbers with a decimal point. The data types which are used to store such type of data are called floating point data types. Variables of floating point types hold real numbers, such as 4.0, 2.5, 3.33, or 0.1226. There are three different types of floating point data types:',
  'انٹیجرز صرف مکمل اعداد محفوظ کرنے کے لیے استعمال ہوتے ہیں، لیکن بعض اوقات ہمیں بہت بڑے اعداد یا اعشاریہ والے اعداد محفوظ کرنے پڑتے ہیں۔ ایسے ڈیٹا کو محفوظ کرنے والی ڈیٹا ٹائپس فلوٹنگ پوائنٹ ڈیٹا ٹائپس کہلاتی ہیں۔ فلوٹنگ پوائنٹ ویری ایبلز حقیقی اعداد جیسے 4.0، 2.5، 3.33 یا 0.1226 رکھتے ہیں۔ فلوٹنگ پوائنٹ ڈیٹا ٹائپس کی تین مختلف اقسام ہیں:',
  'صحیح عددونه یوازې د بشپړو عددونو د ساتلو لپاره کارول کېږي، خو کله کله موږ ډېر لوی عددونه یا اعشاري ټکي لرونکي عددونه ساتلو ته اړتیا لرو. هغه ډېټا ډولونه چې دا ډول ډېټا ساتي، اعشاري ډېټا ډولونه بلل کېږي. د اعشاري ډول متغیرونه حقیقي عددونه لکه 4.0، 2.5، 3.33 یا 0.1226 ساتي. د اعشاري ډېټا ډولونو درې بېل ډولونه دي:')
t.group('list', [('float', 'float', 'float'), ('double', 'double', 'double'), ('long double', 'long double', 'long double')])
H('i. float data type', 'i. float ڈیٹا ٹائپ', 'i. د float ډېټا ډول')
P('In C++, the float data type is used to declare floating point type of variables to store numbers with decimal point. It needs 4 bytes (32 bits) of memory to store values.',
  'C++ میں float ڈیٹا ٹائپ اعشاریہ والے اعداد محفوظ کرنے کے لیے فلوٹنگ پوائنٹ قسم کے ویری ایبلز ڈکلیئر کرنے کے لیے استعمال ہوتی ہے۔ قدریں محفوظ کرنے کے لیے اسے میموری کے 4 بائٹس (32 بٹس) درکار ہوتے ہیں۔',
  'په C++ کې د float ډېټا ډول د اعشاري ټکي لرونکو عددونو د ساتلو لپاره د اعشاري ډول متغیرونو د اعلان لپاره کارول کېږي. د ارزښتونو د ساتلو لپاره د حافظې ۴ بایټه (۳۲ بټه) ته اړتیا لري.')
H('ii. double data type', 'ii. double ڈیٹا ٹائپ', 'ii. د double ډېټا ډول')
P('double is a keyword to represent double precision floating point numbers in C++. double data type occupies 8 bytes (64 bits) of memory. The size of double data type is a rational number in the same range as long float and is stored in the form of floating point representation with binary mantissa and exponent.',
  'double، C++ میں ڈبل پریسیژن فلوٹنگ پوائنٹ اعداد کی نمائندگی کے لیے کی ورڈ ہے۔ double ڈیٹا ٹائپ میموری کے 8 بائٹس (64 بٹس) لیتی ہے۔ double ڈیٹا ٹائپ کا سائز long float جیسی حد میں ایک ناطق عدد ہے اور یہ بائنری مینٹیسا اور قوت نما کے ساتھ فلوٹنگ پوائنٹ نمائندگی کی شکل میں محفوظ ہوتا ہے۔',
  'double په C++ کې د دوه‌ګوني دقت اعشاري عددونو د ښودلو کلیدي کلمه ده. د double ډېټا ډول د حافظې ۸ بایټه (۶۴ بټه) نیسي. د double ډېټا ډول اندازه د long float په څېر حد کې یو ناطق عدد دی او د دوه‌ییزې مانتیسا او توان سره د اعشاري ښودنې په بڼه ساتل کېږي.')
H('iii. long double data type', 'iii. long double ڈیٹا ٹائپ', 'iii. د long double ډېټا ډول')
P('In C++, the long double data type is used to declare long double type of variables to represent long double precision floating point numbers in C++. It needs 10 bytes (80 bits) of memory space in the RAM.',
  'C++ میں long double ڈیٹا ٹائپ لانگ ڈبل پریسیژن فلوٹنگ پوائنٹ اعداد ظاہر کرنے کے لیے long double قسم کے ویری ایبلز ڈکلیئر کرنے کے لیے استعمال ہوتی ہے۔ اسے RAM میں 10 بائٹس (80 بٹس) میموری درکار ہوتی ہے۔',
  'په C++ کې د long double ډېټا ډول د اوږد دوه‌ګوني دقت اعشاري عددونو د ښودلو لپاره د long double ډول متغیرونو د اعلان لپاره کارول کېږي. په RAM کې ۱۰ بایټه (۸۰ بټه) حافظې ته اړتیا لري.')
H('d. Boolean data type', 'd. بولین ڈیٹا ٹائپ', 'd. بولي ډېټا ډول')
P('bool is the keyword used to represent Boolean data type. It is capable of holding one of the two values: true (1) or false (0). It occupies 1 byte of memory.',
  'bool وہ کی ورڈ ہے جو بولین ڈیٹا ٹائپ کی نمائندگی کے لیے استعمال ہوتا ہے۔ یہ دو قدروں میں سے ایک رکھ سکتا ہے: true (1) یا false (0)۔ یہ میموری کا 1 بائٹ لیتا ہے۔',
  'bool هغه کلیدي کلمه ده چې د بولي ډېټا ډول د ښودلو لپاره کارېږي. له دوو ارزښتونو یو ساتلی شي: true (1) یا false (0). د حافظې ۱ بایټ نیسي.')
code(t, 'bool flag;')
H('e. Unsigned data type', 'e. ان سائنڈ ڈیٹا ٹائپ', 'e. بې‌نښې ډېټا ډول')
P('The data types discussed so far are signed data types which means that one bit is reserved for the sign of the value (i.e. +/-). The unsigned numbers are whole numbers and always hold positive values starting from 0 till its maximum size. Here, the sign bit also used for the value which means no bit is reserved for holding a sign (+/-). The unsigned numbers may be classified into four types:',
  'اب تک زیرِ بحث ڈیٹا ٹائپس سائنڈ ڈیٹا ٹائپس ہیں، یعنی قدر کی علامت (+/-) کے لیے ایک بٹ مختص ہوتا ہے۔ ان سائنڈ اعداد مکمل اعداد ہیں اور ہمیشہ 0 سے لے کر اپنے زیادہ سے زیادہ سائز تک مثبت قدریں رکھتے ہیں۔ یہاں علامت کا بٹ بھی قدر کے لیے استعمال ہوتا ہے، یعنی علامت (+/-) رکھنے کے لیے کوئی بٹ مختص نہیں ہوتا۔ ان سائنڈ اعداد کو چار اقسام میں تقسیم کیا جا سکتا ہے:',
  'تر اوسه بحث شوي ډېټا ډولونه نښه‌لرونکي ډولونه دي، یعنې د ارزښت د نښې (+/-) لپاره یو بټ ساتل کېږي. بې‌نښې عددونه بشپړ عددونه دي او تل له 0 تر خپلې اعظمي اندازې مثبت ارزښتونه لري. دلته د نښې بټ هم د ارزښت لپاره کارول کېږي، یعنې د نښې (+/-) د ساتلو لپاره هېڅ بټ نه ساتل کېږي. بې‌نښې عددونه په څلورو ډولونو وېشل کېدای شي:')
t.group('list', [('unsigned char', 'unsigned char', 'unsigned char'), ('unsigned integer', 'unsigned integer', 'unsigned integer'), ('unsigned short integer', 'unsigned short integer', 'unsigned short integer'), ('unsigned long integer', 'unsigned long integer', 'unsigned long integer')])
rec = BOOK.record(t, 'cs12-u3-text-9', 'Unit 3 text (9)', 'یونٹ 3 — متن (۹)', '۳ څپرکی — متن (۹)', 43, [74, 75])
issues = [{'id': 'cs12-pdf043', 'unit': 3, 'printedPage': 75,
           'description': 'p.74 prints “it can stores values”; p.75 “The size of double data type is a rational number in the same range as long float”, “the sign bit also used”. Retained as printed. Owner handwriting (“long distance”, “unit 3”) excluded.'}]

if __name__ == '__main__':
    BOOK.save(43, [(3, rec)], issues=issues)
