"""Computer Science XII PDF40 (spread): printed pp.68–69 — iii. character constants; b. variables; 3.2.2 rules for naming variables; 3.2.3 a. declaration of variables."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('iii. Character constants', 'iii. حرفی کانسٹنٹس', 'iii. د توري ثابتونه')
P('A character enclosed within single quotes is called character constant. Consider the following examples:',
  'ایک واوین (single quotes) میں بند حرف کو حرفی کانسٹنٹ کہتے ہیں۔ درج ذیل مثالوں پر غور کریں:',
  'په یوګوني نقل‌قولونو کې تړل شوی توری د توري ثابت بلل کېږي. لاندې بېلګو ته پام وکړئ:')
code(t, "'A', 'a', '.', '?'")
H('b. Variables', 'b. ویری ایبلز', 'b. متغیرونه')
P('A variable in C++ is a name for a piece of memory that can be used to store information. A variable can be thought as a mailbox where information can be put and retrieved from. All computers have memory, called Random Access Memory (RAM) that is available for programs to use. When a variable is declared, a piece of that memory is set aside for that variable.',
  'C++ میں ویری ایبل میموری کے ایک حصے کا نام ہے جو معلومات محفوظ کرنے کے لیے استعمال ہو سکتا ہے۔ ویری ایبل کو ایک ڈاک خانے کے ڈبے کی طرح سمجھا جا سکتا ہے جس میں معلومات رکھی اور نکالی جا سکتی ہیں۔ تمام کمپیوٹرز میں میموری ہوتی ہے جسے رینڈم ایکسیس میموری (RAM) کہتے ہیں اور جو پروگراموں کے استعمال کے لیے دستیاب ہوتی ہے۔ جب کوئی ویری ایبل ڈکلیئر کیا جاتا ہے تو اس میموری کا ایک حصہ اس ویری ایبل کے لیے مختص کر دیا جاتا ہے۔',
  'په C++ کې متغیر د حافظې د یوې برخې نوم دی چې د معلوماتو د ساتلو لپاره کارول کېدای شي. متغیر د لیک صندوق په څېر ګڼل کېدای شي چې معلومات پکې ایښودل او ترې اخیستل کېدای شي. ټول کمپیوټرونه حافظه لري چې تصادفي لاسرسي حافظه (RAM) بلل کېږي او د پروګرامونو د کارونې لپاره شته. کله چې یو متغیر اعلان شي، د هغې حافظې یوه برخه د هغه متغیر لپاره ځانګړې کېږي.')
P('Consider the following segment of code.', 'کوڈ کے درج ذیل حصے پر غور کریں۔', 'د کوډ لاندې برخې ته پام وکړئ.')
code(t, '''int a = 5;
int b = 2;
int result = a - b;''')
P('In this segment, a, b and result are the integer variables that reside in RAM and store integer values.',
  'اس حصے میں a، b اور result انٹیجر ویری ایبلز ہیں جو RAM میں موجود ہیں اور صحیح عددی قدریں محفوظ کرتے ہیں۔',
  'په دې برخه کې a، b او result صحیح عددي متغیرونه دي چې په RAM کې اوسي او صحیح عددي ارزښتونه ساتي.')
H('3.2.2 Rules for naming variables', '3.2.2 ویری ایبلز کے نام رکھنے کے قواعد', '۳.۲.۲ د متغیرونو د نوم ایښودو قاعدې')
P('The symbol used for a variable is called an identifier or variable name. A set of rules are used for naming variables. These rules are:',
  'ویری ایبل کے لیے استعمال ہونے والی علامت کو شناخت کنندہ (identifier) یا ویری ایبل کا نام کہتے ہیں۔ ویری ایبلز کے نام رکھنے کے لیے قواعد کا ایک مجموعہ استعمال ہوتا ہے۔ یہ قواعد یہ ہیں:',
  'هغه نښه چې د متغیر لپاره کارول کېږي، پېژندونکی (identifier) یا د متغیر نوم بلل کېږي. د متغیرونو د نوم ایښودو لپاره د قاعدو یوه ټولګه کارول کېږي. دا قاعدې دا دي:')
t.group('list', [
 ('Valid identifier is a sequence of one or more letters, digits or underscores characters (_).', 'درست شناخت کنندہ ایک یا زیادہ حروف، اعداد یا انڈر اسکور (_) کا سلسلہ ہے۔', 'سم پېژندونکی د یوه یا ډېرو تورو، رقمونو یا د انډرسکور (_) لړۍ ده.'),
 ('Neither spaces nor punctuation marks or symbols can be part of an identifier. Only letters, digits and single underscore characters are valid.', 'خالی جگہ، اوقاف یا علامات شناخت کنندہ کا حصہ نہیں ہو سکتیں۔ صرف حروف، اعداد اور ایک انڈر اسکور درست ہیں۔', 'نه تشې، نه د تنقیط نښې یا سمبولونه د پېژندونکي برخه کېدای شي. یوازې توري، رقمونه او یو انډرسکور سم دي.'),
 ('Variable identifiers always have to begin with a letter. They can also begin with an underscore character(_ ).', 'ویری ایبل کا شناخت کنندہ ہمیشہ کسی حرف سے شروع ہونا چاہیے۔ یہ انڈر اسکور (_) سے بھی شروع ہو سکتا ہے۔', 'د متغیر پېژندونکی باید تل په توري پیل شي. په انډرسکور (_) هم پیلېدای شي.'),
 ('In no case, a variable can begin with a digit.', 'کسی صورت میں ویری ایبل کسی عدد سے شروع نہیں ہو سکتا۔', 'په هېڅ صورت کې متغیر په رقم نه شي پیلېدای.'),
 ('A Reserved Word of the C++ language cannot be used as an identifier.', 'C++ زبان کا کوئی مخصوص لفظ شناخت کنندہ کے طور پر استعمال نہیں ہو سکتا۔', 'د C++ ژبې ځانګړې کلمه د پېژندونکي په توګه نه شي کارول کېدای.'),
 ('Names should be meaningful.', 'نام بامعنی ہونے چاہییں۔', 'نومونه باید معنا ولري.'),
 ('Names should not be too long.', 'نام بہت لمبے نہیں ہونے چاہییں۔', 'نومونه باید ډېر اوږده نه وي.')])
P('C++ language is a “case sensitive” language which means that an identifier written in capital letters is not equivalent to the one written in small letters.',
  'C++ زبان ’’کیس سینسیٹو‘‘ زبان ہے جس کا مطلب ہے کہ بڑے حروف میں لکھا گیا شناخت کنندہ چھوٹے حروف میں لکھے گئے شناخت کنندہ کے برابر نہیں ہے۔',
  'C++ ژبه د "لوی او کوچني توري حساسه" ژبه ده، چې معنا یې دا ده چې په لویو تورو لیکل شوی پېژندونکی له هغه سره برابر نه دی چې په کوچنیو تورو لیکل شوی.')
H('3.2.3 Declaration and Initialization of variables', '3.2.3 ویری ایبلز کا اعلان اور ابتدائی قدر', '۳.۲.۳ د متغیرونو اعلان او لومړنی ارزښت')
H('a. Declaration of variables', 'a. ویری ایبلز کا اعلان', 'a. د متغیرونو اعلان')
P('In order to use a variable in C++, we must first declare it. The declaration of a variable specifies that which type of data this variable will store/use. The syntax to declare a new variable is to write the specifier of the desired data type such as int, bool, float etc. followed by a valid identifier. For example:',
  'C++ میں کوئی ویری ایبل استعمال کرنے کے لیے پہلے اس کا اعلان کرنا ضروری ہے۔ ویری ایبل کا اعلان بتاتا ہے کہ یہ ویری ایبل کس قسم کا ڈیٹا محفوظ/استعمال کرے گا۔ نیا ویری ایبل ڈکلیئر کرنے کا طریقہ یہ ہے کہ مطلوبہ ڈیٹا ٹائپ کا مخصِّص جیسے int، bool، float وغیرہ لکھیں اور اس کے بعد ایک درست شناخت کنندہ۔ مثلاً:',
  'په C++ کې د یوه متغیر د کارولو لپاره باید لومړی اعلان شي. د متغیر اعلان ټاکي چې دا متغیر به څه ډول ډېټا ساتي/کاروي. د نوي متغیر د اعلان بڼه دا ده چې د غوښتل شوي ډېټا ډول ټاکونکی لکه int، bool، float او نور ولیکئ او ورپسې یو سم پېژندونکی. د بېلګې په توګه:')
code(t, '''Data type variable_name;

int a;''')
P('When this statement is executed by the CPU, a piece of memory from RAM will be set aside and it will be named as a. More than one variables of the same type can be declared in a single statement by separating them with commas. For example:',
  'جب CPU یہ بیان چلاتا ہے تو RAM سے میموری کا ایک حصہ مختص کر دیا جاتا ہے اور اس کا نام a رکھا جاتا ہے۔ ایک ہی قسم کے ایک سے زیادہ ویری ایبلز کو کاموں سے الگ کر کے ایک ہی بیان میں ڈکلیئر کیا جا سکتا ہے۔ مثلاً:',
  'کله چې CPU دا بیان اجرا کړي، د RAM څخه د حافظې یوه برخه ځانګړې کېږي او a نومول کېږي. د یو ډول له یوه زیات متغیرونه د کامو په جلا کولو سره په یوه بیان کې اعلانېدای شي. د بېلګې په توګه:')
code(t, 'int a, b, c;')
rec = BOOK.record(t, 'cs12-u3-text-6', 'Unit 3 text (6)', 'یونٹ 3 — متن (۶)', '۳ څپرکی — متن (۶)', 40, [68, 69])
issues = [{'id': 'cs12-pdf040', 'unit': 3, 'printedPage': 69,
           'description': 'p.69 prints “specifies that which type”, “More than one variables”; p.68 “underscores characters”. Retained as printed. Owner handwriting on p.69 (“#include <isotream>”, “Using namespace std”) excluded.'}]

if __name__ == '__main__':
    BOOK.save(40, [(3, rec)], issues=issues)
