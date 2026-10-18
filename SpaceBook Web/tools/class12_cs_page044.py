"""Computer Science XII PDF44 (spread): printed pp.76–77 — Table 3.2 C++ data types; 3.2.5 constant qualifier; 3.2.6 type casting (implicit, explicit begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('A summary of the basic fundamental data types in C++, as well as the range of values that can be represented with each one is given in Table 3.2.',
  'C++ میں بنیادی ڈیٹا ٹائپس کا خلاصہ اور ہر ایک سے ظاہر کی جا سکنے والی قدروں کی حد جدول 3.2 میں دی گئی ہے۔',
  'په C++ کې د بنسټیزو ډېټا ډولونو لنډیز او د هر یوه په مرسته د ښودل کېدونکو ارزښتونو حد په ۳.۲ جدول کې ورکړل شوی.')
G = {'character': ('Character', 'حرف', 'توری'), 'integer': ('Integer', 'انٹیجر', 'صحیح عدد'), 'float': ('Floating Point', 'فلوٹنگ پوائنٹ', 'اعشاري'), 'bool': ('Boolean', 'بولین', 'بولي')}
R = [('character', 'char', ('Character or small integer', 'حرف یا چھوٹا صحیح عدد', 'توری یا کوچنی صحیح عدد'), '1byte', 'signed: -128 to 127; unsigned: 0 to 255'),
     ('integer', 'short int (short)', ('Short Integer', 'شارٹ انٹیجر', 'لنډ صحیح عدد'), '2bytes', 'signed: -32768 to 32767; unsigned: 0 to 65535'),
     ('integer', 'int', ('Integer (16 bit system)', 'انٹیجر (16 بٹ نظام)', 'صحیح عدد (۱۶ بټه سیسټم)'), '2bytes', 'signed: -32768 to 32767; unsigned: 0 to 65535'),
     ('integer', 'int', ('Integer (32 bit system)', 'انٹیجر (32 بٹ نظام)', 'صحیح عدد (۳۲ بټه سیسټم)'), '4bytes', 'signed: -2147483648 to 2147483647; unsigned: 0 to 4294967295'),
     ('integer', 'long int (long)', ('Long integer', 'لانگ انٹیجر', 'اوږد صحیح عدد'), '4bytes', 'signed: -2147483648 to 2147483647; unsigned: 0 to 4294967295'),
     ('float', 'float', ('Floating point number', 'فلوٹنگ پوائنٹ عدد', 'اعشاري عدد'), '4bytes', '3.4 × 10⁻³⁸ to 3.4 × 10³⁸'),
     ('float', 'double', ('Double precision floating point number', 'ڈبل پریسیژن فلوٹنگ پوائنٹ عدد', 'دوه‌ګوني دقت اعشاري عدد'), '8bytes', '1.7 × 10⁻³⁰⁸ to 1.7 × 10³⁰⁸'),
     ('float', 'long double', ('Long double precision floating point number', 'لانگ ڈبل پریسیژن فلوٹنگ پوائنٹ عدد', 'اوږد دوه‌ګوني دقت اعشاري عدد'), '10bytes', '1.7 × 10⁻⁴⁹³² to 1.7 × 10⁴⁹³²'),
     ('bool', 'bool', ('Boolean value. It can take one of two values: true or false.', 'بولین قدر۔ یہ دو قدروں میں سے ایک لے سکتا ہے: true یا false۔', 'بولي ارزښت. له دوو ارزښتونو یو اخیستی شي: true یا false.'), '1byte', 'true (1) or false (0)')]
rows = lambda i: [[G[g][i], n, d[i], s, r] for g, n, d, s, r in R]
t.table('cs12-table-3-2', ['Data Type', 'Name', 'Description', 'Size', 'Range'], rows(0),
        ['ڈیٹا ٹائپ', 'نام', 'وضاحت', 'سائز', 'حد'], ['ډېټا ډول', 'نوم', 'تشریح', 'اندازه', 'حد'], rows(1), rows(2))
P('Table 3.2: C++ Data Types', 'جدول 3.2: C++ ڈیٹا ٹائپس', '۳.۲ جدول: د C++ ډېټا ډولونه')
H('3.2.5 Constant qualifier', '3.2.5 کانسٹنٹ کوالیفائر', '۳.۲.۵ ثابت توصیف‌کوونکی')
P('const keyword is used to define constant identifier whose values remain constant during the whole life of the program. Const identifier must be assigned with a value when declared, and then that value cannot be changed. Here is the segment of code used to define constant using const identifier keyword.',
  'const کی ورڈ ایسے کانسٹنٹ شناخت کنندہ کی تعریف کے لیے استعمال ہوتا ہے جس کی قدر پروگرام کی پوری زندگی میں مستقل رہتی ہے۔ const شناخت کنندہ کو اعلان کے وقت قدر دینا لازمی ہے اور پھر وہ قدر تبدیل نہیں کی جا سکتی۔ const کی ورڈ کے ذریعے کانسٹنٹ کی تعریف کے لیے کوڈ کا حصہ یہ ہے۔',
  'د const کلیدي کلمه د داسې ثابت پېژندونکي د تعریف لپاره کارول کېږي چې ارزښت یې د پروګرام په ټول ژوند کې ثابت پاتې کېږي. const پېژندونکي ته باید د اعلان پر وخت ارزښت ورکړل شي، او بیا هغه ارزښت نه شي بدلېدای. د const کلیدي کلمې په مرسته د ثابت د تعریف لپاره د کوډ برخه دا ده.')
code(t, 'const int DollarRate = 86;')
P('Declaring a variable as const prevents the programmers from unintentionally changing its value. Consider the following lines of code to change the value of variable DollarRate.',
  'کسی ویری ایبل کو const کے طور پر ڈکلیئر کرنا پروگرامرز کو غیر ارادی طور پر اس کی قدر بدلنے سے روکتا ہے۔ ویری ایبل DollarRate کی قدر بدلنے کے لیے کوڈ کی درج ذیل لائنوں پر غور کریں۔',
  'د یوه متغیر د const په توګه اعلانول پروګرام جوړوونکي له ناارادي بدلون څخه منع کوي. د DollarRate متغیر د ارزښت د بدلولو لپاره د کوډ لاندې کرښو ته پام وکړئ.')
code(t, '''const int DollarRate = 86;
DollarRate = 123; // compiler error!''')
P('A compiler error message will be displayed by the compiler because the code at line 2 tries to change the value of the variable DollarRate from 86 to 123, which is declared as constant. It is an alternative to #define preprocessor directive which is used for defining constants in a program.',
  'کمپائلر غلطی کا پیغام دکھائے گا کیونکہ لائن 2 کا کوڈ ویری ایبل DollarRate کی قدر 86 سے 123 کرنے کی کوشش کرتا ہے جسے کانسٹنٹ کے طور پر ڈکلیئر کیا گیا ہے۔ یہ #define پری پروسیسر ڈائریکٹو کا متبادل ہے جو پروگرام میں کانسٹنٹس کی تعریف کے لیے استعمال ہوتا ہے۔',
  'کمپایلر به د تېروتنې پیغام ښکاره کړي، ځکه چې په ۲مه کرښه کې کوډ هڅه کوي د DollarRate متغیر ارزښت له 86 څخه 123 ته بدل کړي، چې د ثابت په توګه اعلان شوی. دا د #define د مخکې پروسس لارښوونې بدیل دی چې په پروګرام کې د ثابتونو د تعریف لپاره کارول کېږي.')
H('3.2.6 Type casting operator', '3.2.6 ٹائپ کاسٹنگ آپریٹر', '۳.۲.۶ د ډول بدلولو چلونکی')
P('The conversion of data from one type to another is called type casting. It has two types.', 'ڈیٹا کو ایک قسم سے دوسری قسم میں تبدیل کرنا ٹائپ کاسٹنگ کہلاتا ہے۔ اس کی دو اقسام ہیں۔', 'له یوه ډوله بل ډول ته د ډېټا اړول د ډول بدلول (type casting) بلل کېږي. دوه ډوله لري.')
t.group('list', [('Implicit type casting', 'ضمنی ٹائپ کاسٹنگ', 'ضمني ډول بدلول'), ('Explicit type casting', 'صریح ٹائپ کاسٹنگ', 'څرګند ډول بدلول')])
P('In Implicit type casting, the compiler automatically converts data from one type to another when they are used in expressions. When a value of one type is assigned to another type, the compiler implicitly converts that value into the value of the new type. For example:',
  'ضمنی ٹائپ کاسٹنگ میں کمپائلر ایکسپریشنز میں استعمال ہونے پر ڈیٹا کو خود بخود ایک قسم سے دوسری قسم میں تبدیل کر دیتا ہے۔ جب ایک قسم کی قدر دوسری قسم کو تفویض کی جاتی ہے تو کمپائلر ضمنی طور پر اس قدر کو نئی قسم کی قدر میں تبدیل کر دیتا ہے۔ مثلاً:',
  'په ضمني ډول بدلولو کې کمپایلر ډېټا په افادو کې د کارونې پر وخت په اتوماتیک ډول له یوه ډوله بل ته اړوي. کله چې د یوه ډول ارزښت بل ډول ته وسپارل شي، کمپایلر هغه ارزښت په ضمني ډول د نوي ډول ارزښت ته اړوي. د بېلګې په توګه:')
code(t, '''double a= 3; // implicit casting to double value 3.0
int b= 3.14156; // implicit casting to integer value 3''')
P('In C++, there are several ways to convert one type to another but the simplest one is to precede the expression to be converted by the new type enclosed in parentheses ( ). Such type of conversion is called explicit type casting.',
  'C++ میں ایک قسم کو دوسری میں تبدیل کرنے کے کئی طریقے ہیں لیکن سب سے آسان یہ ہے کہ تبدیل کیے جانے والے ایکسپریشن سے پہلے قوسین ( ) میں نئی قسم لکھی جائے۔ اس قسم کی تبدیلی صریح ٹائپ کاسٹنگ کہلاتی ہے۔',
  'په C++ کې له یوه ډوله بل ته د اړولو څو لارې شته، خو تر ټولو ساده یې دا ده چې د اړول کېدونکې افادې مخې ته نوی ډول په قوسونو ( ) کې ولیکل شي. دا ډول اړونه څرګند ډول بدلول بلل کېږي.')
P('Consider the following segment of code:', 'کوڈ کے درج ذیل حصے پر غور کریں:', 'د کوډ لاندې برخې ته پام وکړئ:')
rec = BOOK.record(t, 'cs12-u3-text-10', 'Unit 3 text (10)', 'یونٹ 3 — متن (۱۰)', '۳ څپرکی — متن (۱۰)', 44, [76, 77])
rec['sourceNote'] = 'Table 3.2 (with merged group cells in print) is flattened into one row per type, repeating the group label; signed/unsigned ranges share one cell. The code segment announced at the foot of p.77 follows on p.78 (PDF45).'
issues = [{'id': 'cs12-pdf044', 'unit': 3, 'printedPage': 76,
           'description': 'p.76 prints “Const identifier must be assigned with a value”, “segment of code used to define constant using const identifier keyword”; Table 3.2 lists the float range lower bound as 3.4×10⁻³⁸ (signed range is ±). Retained as printed. Owner handwriting “Computer Science (XII)” on p.77 excluded.'}]

if __name__ == '__main__':
    BOOK.save(44, [(3, rec)], issues=issues)
