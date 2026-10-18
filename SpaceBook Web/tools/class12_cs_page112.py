"""Computer Science XII PDF112–113: pp.212–214 Unit 6 exercise Q1–Q15 (unit 6 complete); p.215 Unit 7 opener + introduction.
Run: python class12_cs_page112.py N (112 or 113)."""
import sys
from class12_cs_common import BOOK, Builder, code


def p112():
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. Normally a function can return ________ value.', 'i. عموماً فنکشن ________ قدر واپس کر سکتا ہے۔', 'i. عموماً یو فنکشن ________ ارزښت بېرته ورکولی شي.'),
     ('ii. The only difference between the function declarator and function prototype is the use of ________ .', 'ii. فنکشن ڈکلیریٹر اور فنکشن پروٹوٹائپ میں واحد فرق ________ کا استعمال ہے۔', 'ii. د فنکشن اعلانوونکي او د فنکشن نمونې ترمنځ یوازینی توپیر د ________ کارونه ده.'),
     ('iii. The scope of global variable declared in a C++ program, is ________ .', 'iii. C++ پروگرام میں ڈکلیئر کیے گئے عالمی ویری ایبل کا دائرہ ________ ہے۔', 'iii. په C++ پروګرام کې د اعلان شوي نړیوال متغیر ساحه ________ ده.'),
     ('iv. Using ________ , we can declare multiple functions with the same name, having slightly different purpose.', 'iv. ________ کے ذریعے ہم ایک ہی نام کے متعدد فنکشنز ڈکلیئر کر سکتے ہیں جن کا مقصد قدرے مختلف ہو۔', 'iv. د ________ په مرسته کولی شو د یو نوم څو فنکشنونه اعلان کړو چې موخه یې یو څه بېله وي.'),
     ('v. If a function needs to return a value to the calling function then its return type should not use the keyword ________ .', 'v. اگر فنکشن کو کال کرنے والے فنکشن کو قدر واپس کرنی ہو تو اس کی ریٹرن ٹائپ میں کلیدی لفظ ________ استعمال نہیں ہونا چاہیے۔', 'v. که یو فنکشن غوښتونکي فنکشن ته ارزښت بېرته ورکوي، نو د بېرته ورکړې په ډول کې یې باید ________ کلیدي کلمه ونه کارول شي.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    e.mcq('i.', ('The phenomenon of having two or more functions in a program with the same names but different number and types of parameters is known as:', 'کسی پروگرام میں ایک ہی نام لیکن مختلف تعداد اور اقسام کے پیرامیٹرز والے دو یا زیادہ فنکشنز ہونے کا عمل کہلاتا ہے:', 'په یوه پروګرام کې د یو نوم خو د بېل شمېر او ډول پاراميټرونو د دوو یا ډېرو فنکشنونو درلودو پدیده بلل کېږي:'),
          [('Inline Function', 'ان لائن فنکشن', 'inline فنکشن'), ('Nested Function', 'نیسٹڈ فنکشن', 'ځالې فنکشن'), ('Function overloading', 'فنکشن اوورلوڈنگ', 'د فنکشن ډېرول'), ('Recursive Function', 'ریکرسیو فنکشن', 'تکراري فنکشن')], per_line=1)
    e.mcq('ii.', ('We declare a function with ________ if it does not have any return type', 'اگر فنکشن کی کوئی ریٹرن ٹائپ نہ ہو تو ہم اسے ________ کے ساتھ ڈکلیئر کرتے ہیں', 'که فنکشن د بېرته ورکړې هېڅ ډول ونه لري، موږ یې د ________ سره اعلانوو'), ['long', 'double', 'void', 'int'], per_line=1)
    e.mcq('iii.', ('Arguments of a functions are separated with ________ .', 'فنکشن کے آرگیومنٹس ________ سے الگ کیے جاتے ہیں۔', 'د فنکشن دلیلونه په ________ جلا کېږي.'),
          [('Comma (,)', 'کاما (,)', 'کامه (,)'), ('Semicolon (;)', 'سیمی کولن (;)', 'سیمي‌کولن (;)'), ('Colon (:)', 'کولن (:)', 'کولن (:)'), ('None of these', 'ان میں سے کوئی نہیں', 'له دې هېڅ یو')], per_line=1)
    e.mcq('iv.', ('Variables inside parenthesis of functions declarations have ________ level access.', 'فنکشنز کی ڈکلیریشنز کی قوسین کے اندر ویری ایبلز کی رسائی ________ سطح کی ہوتی ہے۔', 'د فنکشنونو د اعلانونو د قوسونو دننه متغیرونه د ________ کچې لاسرسی لري.'),
          [('Local', 'مقامی', 'محلي'), ('Global', 'عالمی', 'نړیوال'), ('Module', 'ماڈیول', 'ماډیول'), ('Universal', 'آفاقی', 'نړیوال‌شمول')], per_line=1)
    e.p('v. Observe the following function declaration and choose the best answer:', 'v. درج ذیل فنکشن ڈکلیریشن کا مشاہدہ کریں اور بہترین جواب منتخب کریں:', 'v. لاندې د فنکشن اعلان ته وګورئ او غوره ځواب وټاکئ:')
    code(e, 'int divide ( int a, int b = 2 )')
    e.group('lines', [('(a) Variable b is of integer type and will always have value 2', '(a) ویری ایبل b صحیح عدد کی قسم کا ہے اور ہمیشہ اس کی قدر 2 ہوگی', '(a) متغیر b د صحیح عدد ډول دی او تل به 2 ارزښت ولري'),
                      ('(b) Variable a and b are of int type and the initial value of both variables is 2', '(b) ویری ایبلز a اور b، int قسم کے ہیں اور دونوں کی ابتدائی قدر 2 ہے', '(b) متغیرونه a او b د int ډول دي او د دواړو لومړنی ارزښت 2 دی'),
                      ('(c) Variable b is international scope and will have value 2', '(c) ویری ایبل b بین الاقوامی دائرے کا ہے اور اس کی قدر 2 ہوگی', '(c) متغیر b نړیواله ساحه لري او 2 ارزښت به ولري'),
                      ('(d) Variable b will have value 2 if not specified when calling function', '(d) فنکشن کال کرتے وقت مقرر نہ کی جائے تو ویری ایبل b کی قدر 2 ہوگی', '(d) که د فنکشن د غوښتلو پر مهال ونه ټاکل شي، متغیر b به 2 ارزښت ولري')])
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. A function cannot be overloaded only by its return type.', 'i. فنکشن کو صرف اس کی ریٹرن ٹائپ سے اوورلوڈ نہیں کیا جا سکتا۔', 'i. فنکشن یوازې د بېرته ورکړې په ډول نه شي ډېرېدای.'),
     ('ii. A function can be overloaded with a different return type if it has all the parameters same.', 'ii. اگر فنکشن کے تمام پیرامیٹرز ایک جیسے ہوں تو اسے مختلف ریٹرن ٹائپ کے ساتھ اوورلوڈ کیا جا سکتا ہے۔', 'ii. که د فنکشن ټول پاراميټرونه ورته وي، د بېل د بېرته ورکړې ډول سره ډېرېدای شي.'),
     ('iii. Inline functions minimize the size of the program.', 'iii. ان لائن فنکشنز پروگرام کا سائز کم کرتے ہیں۔', 'iii. inline فنکشنونه د پروګرام اندازه کموي.'),
     ('iv. If we have a function: int sum (int x, int y), then it will return float value to the calling program.', 'iv. اگر ہمارے پاس فنکشن int sum (int x, int y) ہو تو یہ کال کرنے والے پروگرام کو float قدر واپس کرے گا۔', 'iv. که موږ int sum (int x, int y) فنکشن ولرو، نو غوښتونکي پروګرام ته به float ارزښت بېرته ورکړي.'),
     ('v. Passing arguments by address allows the function to change the value of the argument.', 'v. پتے کے ذریعے آرگیومنٹس پاس کرنا فنکشن کو آرگیومنٹ کی قدر تبدیل کرنے کی اجازت دیتا ہے۔', 'v. د پتې له لارې د دلیلونو لېږدول فنکشن ته اجازه ورکوي چې د دلیل ارزښت بدل کړي.')])
    for q, en, ur, ps in [
        ('Q.4', 'Write a program with a function that takes two int parameters, adds them together, and then returns the sum.', 'ایسا پروگرام لکھیں جس میں فنکشن دو int پیرامیٹرز لے، انھیں جمع کرے اور پھر حاصلِ جمع واپس کرے۔', 'یو پروګرام ولیکئ چې یو فنکشن ولري چې دوه int پاراميټرونه واخلي، جمع یې کړي او بیا مجموعه بېرته ورکړي.'),
        ('Q.5', 'Write a program with a function name “mean” to read in three integers from the keyboard to find the arithmetic mean.', 'ایسا پروگرام لکھیں جس میں ’’mean‘‘ نامی فنکشن کی بورڈ سے تین صحیح اعداد پڑھ کر حسابی اوسط معلوم کرے۔', 'یو پروګرام ولیکئ چې د "mean" په نوم فنکشن ولري چې له کیبورډ درې صحیح عددونه ولولي او حسابي منځنی پیدا کړي.'),
        ('Q.6', 'Write a C++ program having a function name rectangle to read the length and width of a rectangle from the keyboard and find the area of the rectangle. The result should be returned to the main program for displaying on the screen.', 'ایسا C++ پروگرام لکھیں جس میں rectangle نامی فنکشن کی بورڈ سے مستطیل کی لمبائی اور چوڑائی پڑھ کر مستطیل کا رقبہ معلوم کرے۔ نتیجہ اسکرین پر دکھانے کے لیے main پروگرام کو واپس کیا جائے۔', 'یو C++ پروګرام ولیکئ چې د rectangle په نوم فنکشن ولري چې له کیبورډ د مستطیل اوږدوالی او پلنوالی ولولي او د مستطیل مساحت پیدا کړي. پایله دې د پرده پر ښودلو لپاره main پروګرام ته ورګرځول شي.'),
        ('Q.7', 'Write a C++ program having two function names area and perimeter to find the area and perimeter of a square.', 'ایسا C++ پروگرام لکھیں جس میں area اور perimeter نامی دو فنکشنز مربع کا رقبہ اور احاطہ معلوم کریں۔', 'یو C++ پروګرام ولیکئ چې د area او perimeter په نوم دوه فنکشنونه ولري چې د مربع مساحت او محیط پیدا کړي.'),
        ('Q.8', 'Write a C++ program to read a number from the keyboard and then pass it to a function to determine whether it is prime or composite.', 'کی بورڈ سے ایک عدد پڑھ کر اسے فنکشن کو پاس کرنے کا C++ پروگرام لکھیں جو معلوم کرے کہ یہ مفرد ہے یا مرکب۔', 'یو C++ پروګرام ولیکئ چې له کیبورډ یو عدد ولولي او بیا یې فنکشن ته ولېږدوي ترڅو وټاکي چې اولي دی که مرکب.'),
        ('Q.10', 'Write a C++ program to get an integer number from keyboard in main program and pass it as an argument to a function where it calculate and display the table.', 'main پروگرام میں کی بورڈ سے ایک صحیح عدد لے کر اسے بطور آرگیومنٹ ایسے فنکشن کو پاس کرنے کا C++ پروگرام لکھیں جو پہاڑا حساب کر کے دکھائے۔', 'یو C++ پروګرام ولیکئ چې په main پروګرام کې له کیبورډ یو صحیح عدد واخلي او د دلیل په توګه یې یوه فنکشن ته ولېږدوي چې جدول (ضرب) حساب او ښکاره کړي.'),
        ('Q.11', 'Define function and differentiate between built-in and user-defined functions with the help of examples.', 'فنکشن کی تعریف کریں اور مثالوں کی مدد سے بلٹ اِن اور یوزر ڈیفائنڈ فنکشنز میں فرق کریں۔', 'فنکشن تعریف کړئ او د بېلګو په مرسته د جوړ شویو او د کاروونکي-تعریف شویو فنکشنونو ترمنځ توپیر وکړئ.'),
        ('Q.12', 'How function prototype and declarator differ from each other? Explain with the help of examples.', 'فنکشن پروٹوٹائپ اور ڈکلیریٹر ایک دوسرے سے کیسے مختلف ہیں؟ مثالوں کی مدد سے وضاحت کریں۔', 'د فنکشن نمونه او اعلانوونکی یو له بله څنګه توپیر لري؟ د بېلګو په مرسته یې تشریح کړئ.'),
        ('Q.13', 'Define default arguments. Describe the advantages and disadvantages of default argument.', 'ڈیفالٹ آرگیومنٹس کی تعریف کریں۔ ڈیفالٹ آرگیومنٹ کے فوائد اور نقصانات بیان کریں۔', 'ډیفالټ دلیلونه تعریف کړئ. د ډیفالټ دلیل ګټې او زیانونه بیان کړئ.'),
        ('Q.14', 'What is meant by the term function overloading? How a function can be overloaded in C++? Describe it with the help of an example program.', 'فنکشن اوورلوڈنگ کی اصطلاح سے کیا مراد ہے؟ C++ میں فنکشن کو کیسے اوورلوڈ کیا جا سکتا ہے؟ ایک مثالی پروگرام کی مدد سے بیان کریں۔', 'د فنکشن ډېرولو اصطلاح څه معنا لري؟ په C++ کې یو فنکشن څنګه ډېرېدای شي؟ د یوه بېلګه‌ییز پروګرام په مرسته یې بیان کړئ.'),
        ('Q.15', 'Describe the role of the following in function overloading.', 'فنکشن اوورلوڈنگ میں درج ذیل کا کردار بیان کریں۔', 'د فنکشن په ډېرولو کې د لاندې رول بیان کړئ.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    e.group('list', [('Data types of arguments', 'آرگیومنٹس کی ڈیٹا ٹائپس', 'د دلیلونو ډېټا ډولونه'), ('Number of arguments', 'آرگیومنٹس کی تعداد', 'د دلیلونو شمېر'), ('Order of arguments', 'آرگیومنٹس کی ترتیب', 'د دلیلونو ترتیب')])
    ex = BOOK.record(e, 'cs12-u6-exercise', 'Unit 6 exercise', 'یونٹ 6: مشق', '۶ څپرکی: تمرین', 112, [212, 213, 214])
    ex['sourceNote'] = 'The exercise runs from p.212 to p.214 (PDF113) and is recorded here whole. The book numbers the questions on p.214 Q.7, Q.8, Q.10 … (no Q.9); kept as printed.'
    BOOK.save(112, [(6, ex)], issues=[{'id': 'cs12-pdf112', 'unit': 6, 'printedPage': 214,
               'description': 'Question numbering skips Q.9 (Q.8 → Q.10); Q2(iii) “Arguments of a functions”; Q2(v)(c) “international scope”; Q10 “where it calculate”. Retained as printed. Owner tick on Q.7 and bracket around Q.15 on p.214 excluded.'}])


def p113():
    t = Builder()
    t.p('Unit 7', 'یونٹ 7', '۷ څپرکی')
    t.h('POINTERS', 'پوائنٹرز', 'پوائنټرونه')
    t.h('After the completion of Unit-7, Students will be able to:', 'یونٹ 7 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۷ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    t.group('list', [('Define pointers', 'پوائنٹرز کی تعریف کر سکیں', 'پوائنټرونه تعریف کړي'), ('Understand memory addresses', 'میموری پتے سمجھ سکیں', 'د حافظې پتې وپوهېږي'),
                     ('Know the use of reference operator &', 'حوالہ آپریٹر & کا استعمال جان سکیں', 'د حوالې چلونکي & کارونه وپېژني'), ('Know the use of dereference operator *', 'ڈی ریفرنس آپریٹر * کا استعمال جان سکیں', 'د حوالې‌لرې کولو چلونکي * کارونه وپېژني'),
                     ('Declare variables of pointer types', 'پوائنٹر اقسام کے ویری ایبلز ڈکلیئر کر سکیں', 'د پوائنټر ډولونو متغیرونه اعلان کړي'), ('Initialize the pointers', 'پوائنٹرز کو ابتدائی قدر دے سکیں', 'پوائنټرونو ته لومړنی ارزښت ورکړي')])
    t.h('INTRODUCTION', 'تعارف', 'سریزه')
    t.p('When variables are declared, computer reserves space in its memory for some objects. The variable name refers to that memory space that is occupied by that object. This allows us to store the value of those variables in the space reserved. Computer refers to these spaces using their addresses. To refer to memory addresses, C++ provides the facility of pointers. The objective of this Unit is to understand how variables are stored in computer memory and how spaces are allocated to them. Sometimes, a programmer needs to refer to another memory location which can only be done by the use of pointers. Pointer is one of the most powerful tool to handle memory addresses. This Unit covers the concept of memory addresses in detail and explains the working of reference operator & and dereference operator * with the help of examples. It also focuses on how to declare pointer type variables and how to initialize them in a program.',
        'جب ویری ایبلز ڈکلیئر کیے جاتے ہیں تو کمپیوٹر کچھ اشیا کے لیے اپنی میموری میں جگہ مختص کرتا ہے۔ ویری ایبل کا نام اس میموری جگہ کی طرف اشارہ کرتا ہے جو اس شے نے گھیری ہوتی ہے۔ اس سے ہم ان ویری ایبلز کی قدر مختص جگہ میں محفوظ کر سکتے ہیں۔ کمپیوٹر ان جگہوں کا حوالہ ان کے پتوں سے دیتا ہے۔ میموری پتوں کا حوالہ دینے کے لیے C++ پوائنٹرز کی سہولت فراہم کرتی ہے۔ اس یونٹ کا مقصد یہ سمجھنا ہے کہ ویری ایبلز کمپیوٹر میموری میں کیسے محفوظ ہوتے ہیں اور انھیں جگہیں کیسے مختص کی جاتی ہیں۔ بعض اوقات پروگرامر کو کسی دوسرے میموری مقام کا حوالہ دینا ہوتا ہے جو صرف پوائنٹرز کے استعمال سے ممکن ہے۔ پوائنٹر میموری پتوں کو سنبھالنے کا سب سے طاقتور ذریعہ ہے۔ یہ یونٹ میموری پتوں کا تصور تفصیل سے بیان کرتا ہے اور مثالوں کی مدد سے حوالہ آپریٹر & اور ڈی ریفرنس آپریٹر * کا عمل واضح کرتا ہے۔ یہ اس پر بھی توجہ دیتا ہے کہ پوائنٹر قسم کے ویری ایبلز کیسے ڈکلیئر کیے جائیں اور پروگرام میں انھیں ابتدائی قدر کیسے دی جائے۔',
        'کله چې متغیرونه اعلان شي، کمپیوټر د ځینو شیانو لپاره په خپله حافظه کې ځای ساتي. د متغیر نوم هغه حافظه ځای ته اشاره کوي چې هغه شي نیولی. دا موږ ته اجازه راکوي چې د دې متغیرونو ارزښت په ساتل شوي ځای کې وساتو. کمپیوټر دې ځایونو ته د پتو له لارې اشاره کوي. د حافظې پتو ته د اشارې لپاره C++ د پوائنټرونو اسانتیا برابروي. د دې څپرکي موخه دا پوهېدل دي چې متغیرونه د کمپیوټر په حافظه کې څنګه ساتل کېږي او ځایونه ورته څنګه ټاکل کېږي. کله کله پروګرام جوړوونکی اړتیا لري چې بل حافظه ځای ته اشاره وکړي چې یوازې د پوائنټرونو په کارولو کېدای شي. پوائنټر د حافظې پتو د چلولو تر ټولو پیاوړې وسیله ده. دا څپرکی د حافظې د پتو مفهوم په تفصیل بیانوي او د بېلګو په مرسته د حوالې چلونکي & او د حوالې‌لرې کولو چلونکي * کار تشریح کوي. همداراز په دې تمرکز کوي چې د پوائنټر ډول متغیرونه څنګه اعلان شي او په پروګرام کې څنګه لومړنی ارزښت ورکړل شي.')
    rec = BOOK.record(t, 'cs12-u7-outcomes', 'Unit 7: learning outcomes and introduction', 'یونٹ 7: حاصلاتِ تعلم اور تعارف', '۷ څپرکی: د زده‌کړې پایلې او سریزه', 113, [215],
                      unit_title=('Pointers', 'پوائنٹرز', 'پوائنټرونه'))
    BOOK.save(113, [(7, rec)], complete_units=[6], issues=[{'id': 'cs12-pdf113', 'unit': 7, 'printedPage': 215,
               'description': 'Introduction: “one of the most powerful tool”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 112
    p112() if n == 112 else p113()
