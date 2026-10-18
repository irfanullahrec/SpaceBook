"""Computer Science XII PDF39 (spread): printed pp.66–67 — literal constants: string; numeric (integer, floating point, hexadecimal, octal)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Consider the following line of code:', 'کوڈ کی درج ذیل لائن پر غور کریں:', 'د کوډ لاندې کرښې ته پام وکړئ:')
code(t, 'VarA = 555;')
P('In this line of code, 555 is a literal constant. The literal constants are further categorized into the following types.',
  'کوڈ کی اس لائن میں 555 ایک لٹرل کانسٹنٹ ہے۔ لٹرل کانسٹنٹس کو مزید درج ذیل اقسام میں تقسیم کیا جاتا ہے۔',
  'د کوډ په دې کرښه کې 555 لفظي ثابت دی. لفظي ثابتونه بیا په لاندې ډولونو وېشل کېږي.')
t.group('list', [('String constants', 'اسٹرنگ کانسٹنٹس', 'د تار ثابتونه'), ('Numeric constants', 'عددی کانسٹنٹس', 'شمېریز ثابتونه'), ('Character constants', 'حرفی کانسٹنٹس', 'د توري ثابتونه')])
H('i. String constants', 'i. اسٹرنگ کانسٹنٹس', 'i. د تار ثابتونه')
P('A string constant is a sequence of characters enclosed in double quotation marks is called string constant. Its maximum length is 256 characters. Following are some examples of valid string constants.',
  'دوہرے واوین میں بند حروف کا سلسلہ اسٹرنگ کانسٹنٹ کہلاتا ہے۔ اس کی زیادہ سے زیادہ لمبائی 256 حروف ہے۔ درست اسٹرنگ کانسٹنٹس کی کچھ مثالیں درج ذیل ہیں۔',
  'په دوه‌ګونو نقل‌قولونو کې تړل شوې د تورو لړۍ د تار ثابت بلل کېږي. اعظمي اوږدوالی یې ۲۵۶ توري دي. د سمو تاري ثابتونو ځینې بېلګې دا دي.')
code(t, '''"Welcome to the first C++ Program"
"The result="''')
H('ii. Numeric constants', 'ii. عددی کانسٹنٹس', 'ii. شمېریز ثابتونه')
P('Numeric constants consist of positive or negative signed numerals. There are four types of numeric constants. These are:', 'عددی کانسٹنٹس مثبت یا منفی علامت والے اعداد پر مشتمل ہوتے ہیں۔ عددی کانسٹنٹس کی چار اقسام ہیں:', 'شمېریز ثابتونه له مثبت یا منفي نښه لرونکو عددونو جوړ وي. د شمېریزو ثابتونو څلور ډولونه دي:')
t.group('list', [('Integer constant', 'انٹیجر کانسٹنٹ', 'صحیح عدد ثابت'), ('Floating point constant', 'فلوٹنگ پوائنٹ کانسٹنٹ', 'اعشاري ثابت'), ('Hexadecimal constant', 'ہیکسا ڈیسیمل کانسٹنٹ', 'شپاړسیز ثابت'), ('Octal constant', 'آکٹل کانسٹنٹ', 'اتیز ثابت')])
P('Integer constants: Integer constants are those positives or negative signed numbers that do not contain a decimal point e.g. 2010, -321 etc.',
  'انٹیجر کانسٹنٹس: انٹیجر کانسٹنٹس وہ مثبت یا منفی علامت والے اعداد ہیں جن میں اعشاریہ نہ ہو، مثلاً 2010، -321 وغیرہ۔',
  'صحیح عدد ثابتونه: صحیح عدد ثابتونه هغه مثبت یا منفي نښه لرونکي عددونه دي چې اعشاري ټکی نه لري، لکه 2010، -321 او نور.')
P('Floating point constants: The numeric constants having a decimal point are called floating point constants e.g. 33.55 and -0.22 etc. These constants can be either positive signed or negative signed. These constants can also be represented in its exponential form by the use of alphabet ‘e’ or ‘E’ to denote the exponents of the numbers. For example.',
  'فلوٹنگ پوائنٹ کانسٹنٹس: اعشاریہ والے عددی کانسٹنٹس فلوٹنگ پوائنٹ کانسٹنٹس کہلاتے ہیں، مثلاً 33.55 اور -0.22 وغیرہ۔ یہ کانسٹنٹس مثبت یا منفی علامت والے ہو سکتے ہیں۔ ان کانسٹنٹس کو اعداد کی قوت (exponent) ظاہر کرنے کے لیے حرف ‘e’ یا ‘E’ کے استعمال سے قوت نما شکل میں بھی ظاہر کیا جا سکتا ہے۔ مثلاً:',
  'اعشاري ثابتونه: هغه شمېریز ثابتونه چې اعشاري ټکی لري، اعشاري (floating point) ثابتونه بلل کېږي، لکه 33.55 او -0.22 او نور. دا ثابتونه کېدای شي مثبت یا منفي نښه ولري. دا ثابتونه د عددونو د توان (exponent) د ښودلو لپاره د ‘e’ یا ‘E’ توري په کارولو په توانیزه بڼه هم ښودل کېدای شي. د بېلګې په توګه:')
code(t, '''9010E10
7810.11E-11
-10.990e8
-1.001e-1''')
P('Hexadecimal constants: The constants represented in hexadecimal number system are called hexadecimal constants. To represent a hexadecimal constant, begin the constant with 0x or 0X, followed by a sequence of digits in the range 0 through 9 and a through f (or A through F). The digits a to f (or A to F) represent values in the range 10 through 15. For example.',
  'ہیکسا ڈیسیمل کانسٹنٹس: ہیکسا ڈیسیمل عددی نظام میں ظاہر کیے گئے کانسٹنٹس ہیکسا ڈیسیمل کانسٹنٹس کہلاتے ہیں۔ ہیکسا ڈیسیمل کانسٹنٹ ظاہر کرنے کے لیے اسے 0x یا 0X سے شروع کریں، اس کے بعد 0 سے 9 اور a سے f (یا A سے F) کے اعداد کا سلسلہ۔ اعداد a سے f (یا A سے F) 10 سے 15 تک کی قدریں ظاہر کرتے ہیں۔ مثلاً:',
  'شپاړسیز ثابتونه: هغه ثابتونه چې په شپاړسیز عددي سیسټم کې ښودل کېږي، شپاړسیز ثابتونه بلل کېږي. د شپاړسیز ثابت د ښودلو لپاره یې په 0x یا 0X پیل کړئ، وروسته د 0 تر 9 او a تر f (یا A تر F) د عددونو لړۍ. عددونه a تر f (یا A تر F) له ۱۰ تر ۱۵ پورې ارزښتونه ښيي. د بېلګې په توګه:')
code(t, '''int i = 0x3fff; // Hexadecimal constant
int j = 0X3FFF; // Hexadecimal constant''')
P('Octal constants: The representation of constants in octal number system is called octal constants. To specify an octal constant, begin the specification with 0, followed by a sequence of digits in the range 0 through 7. Consider the following example:',
  'آکٹل کانسٹنٹس: آکٹل عددی نظام میں کانسٹنٹس کی نمائندگی آکٹل کانسٹنٹس کہلاتی ہے۔ آکٹل کانسٹنٹ متعین کرنے کے لیے اسے 0 سے شروع کریں، اس کے بعد 0 سے 7 تک کے اعداد کا سلسلہ۔ درج ذیل مثال پر غور کریں:',
  'اتیز ثابتونه: په اتیز عددي سیسټم کې د ثابتونو ښودنه اتیز ثابتونه بلل کېږي. د اتیز ثابت د ټاکلو لپاره یې په 0 پیل کړئ، وروسته د 0 تر 7 پورې د عددونو لړۍ. لاندې بېلګې ته پام وکړئ:')
code(t, '''int i = 0377; // Octal constant
int j = 0397; // Error: 9 is not an octal digit''')
P('Octal numbers are integer numbers of base 8 and their digits are 0 to 7.', 'آکٹل اعداد 8 کی اساس والے صحیح اعداد ہیں اور ان کے اعداد 0 سے 7 تک ہیں۔', 'اتیز عددونه د ۸ اساس صحیح عددونه دي او رقمونه یې له 0 تر 7 دي.')
rec = BOOK.record(t, 'cs12-u3-text-5', 'Unit 3 text (5)', 'یونٹ 3 — متن (۵)', '۳ څپرکی — متن (۵)', 39, [66, 67])
issues = [{'id': 'cs12-pdf039', 'unit': 3, 'printedPage': 66,
           'description': 'p.66 prints “A string constant is a sequence … is called string constant”, “those positives or negative”; p.67 “represented in its exponential form”. Retained as printed. Owner pen calculations on p.67 excluded.'}]

if __name__ == '__main__':
    BOOK.save(39, [(3, rec)], issues=issues)
