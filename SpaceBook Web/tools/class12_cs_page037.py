"""Computer Science XII PDF37 (spread): printed pp.62–63 — output of #define example; b. main() function; c. body of main(); C++ statements; getch(); return 0; multi-line program (whole, incl. p.64 lines)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'Area of the Circle: 31.4159')
P('The #define directive is not a C++ statement but a directive for the preprocessor; therefore it assumes the entire line as the directive and does not require a semicolon (;) at its end.',
  '#define ڈائریکٹو C++ بیان نہیں بلکہ پری پروسیسر کے لیے ایک ہدایت ہے؛ اس لیے یہ پوری لائن کو ڈائریکٹو سمجھتا ہے اور اس کے آخر میں سیمی کولن (;) کی ضرورت نہیں ہوتی۔',
  '#define لارښوونه د C++ بیان نه، بلکې د مخکې پروسسوونکي لپاره لارښوونه ده؛ نو ټوله کرښه لارښوونه ګڼي او په پای کې یې سیمي‌کولن (;) ته اړتیا نه لري.')
H('b. main( ) Function', 'b. main( ) فنکشن', 'b. main( ) فنکشن')
P('The main function is the point by where all C++ programs start their execution. It does not matter whether there are other functions with other names defined before or after it, the instructions contained within this function’s definition will always be the first ones to be executed in any C++ program. For that same reason, it is essential that all C++ programs have a main function.',
  'main فنکشن وہ نقطہ ہے جہاں سے تمام C++ پروگرام اپنا عمل شروع کرتے ہیں۔ اس سے کوئی فرق نہیں پڑتا کہ اس سے پہلے یا بعد میں دوسرے ناموں کے دوسرے فنکشن متعین ہیں یا نہیں، اس فنکشن کی تعریف میں موجود ہدایات ہمیشہ کسی بھی C++ پروگرام میں سب سے پہلے چلائی جائیں گی۔ اسی وجہ سے ضروری ہے کہ تمام C++ پروگراموں میں main فنکشن ہو۔',
  'main فنکشن هغه ټکی دی چې له هغه ټول C++ پروګرامونه خپله اجرا پیلوي. توپیر نه کوي چې له هغه مخکې یا وروسته د نورو نومونو نور فنکشنونه تعریف شوي که نه، د دې فنکشن په تعریف کې شته لارښوونې به په هر C++ پروګرام کې تل لومړی اجرا کېږي. له همدې امله اړینه ده چې ټول C++ پروګرامونه main فنکشن ولري.')
P('The word main is followed in the code by a pair of parentheses ( ).', 'کوڈ میں لفظ main کے بعد قوسین کا ایک جوڑا ( ) آتا ہے۔', 'په کوډ کې د main کلمې وروسته د قوسونو یوه جوړه ( ) راځي.')
H('c. Body of the main( ) function', 'c. main( ) فنکشن کا جسم', 'c. د main( ) فنکشن بدنه')
P('After the parentheses of the main function, the body of main function starts which is enclosed in braces { }. When this function is executed, the instructions written within it perform their task. Inside the body of main function, C++ statements are written.',
  'main فنکشن کی قوسین کے بعد main فنکشن کا جسم شروع ہوتا ہے جو بریسز { } میں بند ہوتا ہے۔ جب یہ فنکشن چلایا جاتا ہے تو اس کے اندر لکھی گئی ہدایات اپنا کام انجام دیتی ہیں۔ main فنکشن کے جسم کے اندر C++ بیانات لکھے جاتے ہیں۔',
  'د main فنکشن له قوسونو وروسته د main فنکشن بدنه پیلېږي چې په لوړو قوسونو { } کې تړل شوې وي. کله چې دا فنکشن اجرا شي، په هغه کې لیکل شوې لارښوونې خپله دنده ترسره کوي. د main فنکشن د بدنې دننه د C++ بیانونه لیکل کېږي.')
H('C++ Statements', 'C++ بیانات', 'د C++ بیانونه')
P('A C++ statement is a simple or compound expression that can actually produce some effect. It is actually an instruction to the computer for taking an action. For example cout << "Hello World!"; is a C++ statement. The following are some examples of statements.',
  'C++ بیان ایک سادہ یا مرکب ایکسپریشن ہے جو واقعی کوئی اثر پیدا کر سکتا ہے۔ یہ دراصل کمپیوٹر کو کوئی عمل کرنے کی ہدایت ہے۔ مثال کے طور پر cout << "Hello World!"; ایک C++ بیان ہے۔ درج ذیل بیانات کی کچھ مثالیں ہیں۔',
  'د C++ بیان یوه ساده یا مرکبه افاده ده چې په رښتیا یو اغېز پیدا کولی شي. په حقیقت کې دا کمپیوټر ته د یوې کړنې لارښوونه ده. د بېلګې په توګه cout << "Hello World!"; د C++ بیان دی. لاندې د بیانونو ځینې بېلګې دي.')
code(t, 'cout << "Hello World!";')
P('In fact, this statement performs the only action of displaying the result “Hello World!” on the screen. cout is the name of the standard output stream in C++, and the meaning of the entire statement is to insert a sequence of characters (in this case the Hello World sequence of characters) into the standard output stream. cout is declared in the <iostream.h> standard header file.',
  'درحقیقت یہ بیان اسکرین پر نتیجہ ’’Hello World!‘‘ دکھانے کا واحد عمل کرتا ہے۔ cout C++ میں معیاری آؤٹ پٹ اسٹریم کا نام ہے، اور پورے بیان کا مطلب حروف کا ایک سلسلہ (اس صورت میں Hello World کے حروف) معیاری آؤٹ پٹ اسٹریم میں داخل کرنا ہے۔ cout کا اعلان <iostream.h> معیاری ہیڈر فائل میں ہوتا ہے۔',
  'په حقیقت کې دا بیان یوازې پر پرده د "Hello World!" پایلې د ښودلو کړنه کوي. cout په C++ کې د معیاري وتنې بهیر نوم دی، او د ټول بیان معنا د تورو یوه لړۍ (په دې صورت کې د Hello World توري) معیاري وتنې بهیر ته ورننویستل دي. cout په <iostream.h> معیاري سرلیک فایل کې اعلان شوی.')
code(t, 'getch ();')
P('This is a standard library function defined in the header file <conio.h> and is used to wait for the user to input a character from the keyboard.',
  'یہ ہیڈر فائل <conio.h> میں متعین ایک معیاری لائبریری فنکشن ہے جو صارف کے کی بورڈ سے کوئی حرف داخل کرنے کا انتظار کرنے کے لیے استعمال ہوتا ہے۔',
  'دا په <conio.h> سرلیک فایل کې تعریف شوی معیاري کتابتون فنکشن دی چې د دې انتظار لپاره کارول کېږي چې کاروونکی له کیبورډ یو توری ولیکي.')
code(t, 'return 0;')
P('The return statement causes the main function to return control to the operating system. Return may be followed by a return code. The code 0 returned by the return statement tells the operating system that the program terminates normally.',
  'return بیان main فنکشن کو کنٹرول آپریٹنگ سسٹم کو واپس کرنے کا باعث بنتا ہے۔ return کے بعد ایک ریٹرن کوڈ ہو سکتا ہے۔ return بیان کا واپس کیا گیا کوڈ 0 آپریٹنگ سسٹم کو بتاتا ہے کہ پروگرام معمول کے مطابق ختم ہوا۔',
  'return بیان main فنکشن دې ته اړ کوي چې کنټرول عملیاتي سیسټم ته بېرته ورکړي. له return وروسته کېدای شي د بېرته ورکولو کوډ راشي. د return بیان له خوا بېرته ورکړل شوی کوډ 0 عملیاتي سیسټم ته وايي چې پروګرام په عادي ډول پای ته ورسېد.')
P('The program has been structured in different lines in order to be more readable, but in C++, we do not have strict rules on how to separate instructions in different lines. For example, the following program can also be written in a single line.',
  'پروگرام کو زیادہ قابلِ مطالعہ بنانے کے لیے مختلف لائنوں میں ترتیب دیا گیا ہے، لیکن C++ میں ہدایات کو مختلف لائنوں میں الگ کرنے کے سخت قواعد نہیں ہیں۔ مثال کے طور پر درج ذیل پروگرام ایک ہی لائن میں بھی لکھا جا سکتا ہے۔',
  'پروګرام د لا د لوستلو وړ کېدو لپاره په بېلابېلو کرښو کې ترتیب شوی، خو په C++ کې د لارښوونو په بېلابېلو کرښو کې د جلا کولو کلکې قاعدې نه لرو. د بېلګې په توګه لاندې پروګرام په یوه کرښه کې هم لیکل کېدای شي.')
code(t, '''int main()
{
cout << " Hello World!";
return 0;
}''')
rec = BOOK.record(t, 'cs12-u3-text-3', 'Unit 3 text (3)', 'یونٹ 3 — متن (۳)', '۳ څپرکی — متن (۳)', 37, [62, 63, 64])
rec['sourceNote'] = 'The program listing starting “int main()” at the foot of p.63 continues on p.64 (PDF38); it is given whole here. The rest of the #define example listing (top of p.62) was recorded with PDF36.'
issues = [{'id': 'cs12-pdf037', 'unit': 3, 'printedPage': 62,
           'description': 'p.62 prints “the point by where all C++ programs start their execution”. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(37, [(3, rec)], issues=issues)
