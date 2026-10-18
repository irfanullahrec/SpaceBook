"""Computer Science XII PDF134–142: pp.256–258 Unit 8 exercise (unit 8 complete); p.259 Unit 9 opener; pp.260–273 Unit 9 text
(9.1 file handling … 9.1.5 single character stream, writing program).
Run: python class12_cs_page134.py N (134–142)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import text_window

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u9-text-{n}', f'Unit 9 text ({n})', f'یونٹ 9 — متن ({n})', f'۹ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def win(t, vid, title, lines, caps, dark=False):
    sv = [text_window(title, lines, c, dark) for c in caps]
    t.visual(vid, sv[0][0], sv[1][0], sv[2][0], sv[0][1])


def p134():
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. ________ is a member of function that is called automatically when an object is created..', 'i. ________ فنکشن کا ایک ممبر ہے جو آبجیکٹ بننے پر خود بخود کال ہوتا ہے۔', 'i. ________ د فنکشن یو غړی دی چې د شي د جوړېدو پر مهال پخپله غوښتل کېږي.'),
     ('ii. The ability to reuse code already defined for the new purpose, is referred to as ________ .', 'ii. پہلے سے بیان کیے گئے کوڈ کو نئے مقصد کے لیے دوبارہ استعمال کرنے کی صلاحیت ________ کہلاتی ہے۔', 'ii. د نوې موخې لپاره د مخکې تعریف شوي کوډ د بیا کارولو وړتیا ________ بلل کېږي.'),
     ('iii. In OOP the main advantage of inheritance include ________ .', 'iii. OOP میں وراثت کے بنیادی فائدے میں ________ شامل ہے۔', 'iii. په OOP کې د میراث اصلي ګټه ________ لري.'),
     ('iv. An object of a class can be defined as “ a variable of type ________ ”', 'iv. کلاس کے آبجیکٹ کو ’’________ قسم کا ویری ایبل‘‘ کہا جا سکتا ہے', 'iv. د ټولګي شی د "د ________ ډول متغیر" په توګه تعریفېدای شي'),
     ('v. Function overloading is used to achieve ________ .', 'v. فنکشن اوورلوڈنگ ________ حاصل کرنے کے لیے استعمال ہوتی ہے۔', 'v. د فنکشن ډېرول د ________ د ترلاسه کولو لپاره کارېږي.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    e.mcq('i.', ('A constructor is called whenever ________ .', 'کنسٹرکٹر اس وقت کال ہوتا ہے جب ________ ۔', 'جوړوونکی هغه وخت غوښتل کېږي چې ________ .'),
          [('An object is destroyed', 'آبجیکٹ ختم ہو', 'شی ړنګ شي'), ('An object is created', 'آبجیکٹ بنے', 'شی جوړ شي'), ('A class is declared', 'کلاس ڈکلیئر ہو', 'ټولګی اعلان شي'), ('A class is used', 'کلاس استعمال ہو', 'ټولګی وکارول شي')], per_line=1)
    e.mcq('ii.', ('Destructor is used for ________ .', 'ڈسٹرکٹر ________ کے لیے استعمال ہوتا ہے۔', 'ړنګوونکی د ________ لپاره کارېږي.'),
          [('Initializing the values of data members in an object', 'آبجیکٹ میں ڈیٹا ممبرز کی قدروں کو ابتدائی قدر دینا', 'په شي کې د ډېټا غړو ارزښتونو ته لومړنی ارزښت ورکول'), ('Initializing arrays', 'ایریز کو ابتدائی قدر دینا', 'لړیو ته لومړنی ارزښت ورکول'),
           ('Freeing memory allocated to the object of the class when it was created', 'کلاس کے آبجیکٹ کو بنتے وقت دی گئی میموری آزاد کرنا', 'د ټولګي شي ته د جوړېدو پر مهال ورکړل شوې حافظه ازادول'), ('Creating an object', 'آبجیکٹ بنانا', 'شی جوړول')], per_line=1)
    e.mcq('iii.', ('The name of destructor is always preceded by the symbol ________', 'ڈسٹرکٹر کے نام سے پہلے ہمیشہ نشان ________ ہوتا ہے', 'د ړنګوونکي نوم ته تل ________ نښه مخکې وي'), ['+', '%', '-', '~'], per_line=1)
    e.mcq('iv.', ('Constructors are usually used for ________ .', 'کنسٹرکٹرز عموماً ________ کے لیے استعمال ہوتے ہیں۔', 'جوړوونکي عموماً د ________ لپاره کارېږي.'),
          [('Constructing programs', 'پروگرام بنانے', 'پروګرامونو جوړولو'), ('Running classes', 'کلاسز چلانے', 'ټولګیو چلولو'), ('Initializing objects', 'آبجیکٹس کو ابتدائی قدر دینے', 'شیانو ته لومړني ارزښت ورکولو'), ('All of the above', 'مندرجہ بالا سب', 'پورته ټول')], per_line=1)
    e.mcq('v.', ('Inheritance is used to ________ .', 'وراثت ________ کے لیے استعمال ہوتی ہے۔', 'میراث د ________ لپاره کارېږي.'),
          [('Increase the size of a program', 'پروگرام کا سائز بڑھانے', 'د پروګرام د اندازې زیاتولو'), ('Make the program simpler', 'پروگرام کو آسان بنانے', 'د پروګرام ساده کولو'),
           ('Provide the facility of code reusability', 'کوڈ کے دوبارہ استعمال کی سہولت فراہم کرنے', 'د کوډ د بیا کارونې اسانتیا برابرولو'), ('Provide the facility of data hiding', 'ڈیٹا ہائیڈنگ کی سہولت فراہم کرنے', 'د ډېټا د پټولو اسانتیا برابرولو')], per_line=1)
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. C++ is a pure object-oriented programming language.', 'i. C++ خالص آبجیکٹ اورینٹڈ پروگرامنگ زبان ہے۔', 'i. C++ خالصه د شیانو ته متوجه پروګرامي ژبه ده.'),
     ('ii. One of the main features of object oriented programming language is data hiding.', 'ii. آبجیکٹ اورینٹڈ پروگرامنگ زبان کی بنیادی خصوصیات میں سے ایک ڈیٹا ہائیڈنگ ہے۔', 'ii. د شیانو ته متوجه پروګرامي ژبې له اصلي ځانګړتیاوو یوه د ډېټا پټول دي.'),
     ('iii. If you do not declare a constructor in a class, the compiler will furnish a default constructor for you automatically.', 'iii. اگر آپ کلاس میں کنسٹرکٹر ڈکلیئر نہ کریں تو کمپائلر آپ کے لیے خود بخود ڈیفالٹ کنسٹرکٹر فراہم کر دے گا۔', 'iii. که تاسو په ټولګي کې جوړوونکی اعلان نه کړئ، کمپایلر به ستاسو لپاره پخپله ډیفالټ جوړوونکی برابر کړي.'),
     ('iv. A constructor is a function that is called when an instance of a class is deleted.', 'iv. کنسٹرکٹر وہ فنکشن ہے جو کلاس کا انسٹینس حذف ہونے پر کال ہوتا ہے۔', 'iv. جوړوونکی هغه فنکشن دی چې د ټولګي د نمونې د ړنګېدو پر مهال غوښتل کېږي.'),
     ('v. Function overloading is an example of polymorphism.', 'v. فنکشن اوورلوڈنگ پولی مورفزم کی ایک مثال ہے۔', 'v. د فنکشن ډېرول د پولي‌مورفیزم یوه بېلګه ده.')])
    for q, en, ur, ps in [
        ('Q.4', 'Write a C++ program implementing a class with the name Circle having two functions with the names: GetRadius and CalArea. The functions should get the value for the radius from the user and then calculate the area of the circle and display the results.', 'Circle نامی کلاس نافذ کرنے والا C++ پروگرام لکھیں جس میں GetRadius اور CalArea نام کے دو فنکشنز ہوں۔ فنکشنز صارف سے نصف قطر کی قدر لیں اور پھر دائرے کا رقبہ حساب کر کے نتائج دکھائیں۔', 'یو C++ پروګرام ولیکئ چې د Circle په نوم ټولګی پلي کړي چې د GetRadius او CalArea په نوم دوه فنکشنونه ولري. فنکشنونه دې له کاروونکي د شعاع ارزښت واخلي او بیا د دایرې مساحت حساب او پایلې وښيي.'),
        ('Q.5', 'Write a C++ program implementing inheritance between Employee (base class) and Manager (derived class).', 'Employee (بیس کلاس) اور Manager (ڈیرائیوڈ کلاس) کے درمیان وراثت نافذ کرنے والا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د Employee (اساسي ټولګی) او Manager (مشتق ټولګی) ترمنځ میراث پلي کړي.'),
        ('Q.6', 'Diagrammatically represent the following scenario of inheritance:', 'وراثت کے درج ذیل منظرنامے کو خاکے کی صورت میں ظاہر کریں:', 'د میراث لاندې سناریو په ډیاګرام کې وښایاست:')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    e.group('list', [('We have Shape as a base class and Circle, Rectangle, Triangle and Square as its derived classes.', 'ہمارے پاس Shape بیس کلاس ہے اور Circle، Rectangle، Triangle اور Square اس کی ڈیرائیوڈ کلاسز ہیں۔', 'موږ Shape د اساسي ټولګي په توګه او Circle، Rectangle، Triangle او Square د هغې د مشتق ټولګیو په توګه لرو.')])
    for q, en, ur, ps in [
        ('Q.7', 'Write a C++ program implementing a class with the name ConstDest having constructor and destructor functions in its body.', 'ConstDest نامی کلاس نافذ کرنے والا C++ پروگرام لکھیں جس کے جسم میں کنسٹرکٹر اور ڈسٹرکٹر فنکشنز ہوں۔', 'یو C++ پروګرام ولیکئ چې د ConstDest په نوم ټولګی پلي کړي چې په بدنه کې یې جوړوونکی او ړنګوونکی فنکشنونه وي.'),
        ('Q.8', 'Write a C++ program implementing a class with the name Time. This class should have a constructor to initialize the time, hours, minutes and seconds. The class should have another function named ToSecond() to convert and display the time into seconds.', 'Time نامی کلاس نافذ کرنے والا C++ پروگرام لکھیں۔ اس کلاس میں وقت، گھنٹے، منٹ اور سیکنڈ کو ابتدائی قدر دینے کے لیے کنسٹرکٹر ہونا چاہیے۔ کلاس میں ToSecond() نامی ایک اور فنکشن ہونا چاہیے جو وقت کو سیکنڈز میں بدل کر دکھائے۔', 'یو C++ پروګرام ولیکئ چې د Time په نوم ټولګی پلي کړي. دا ټولګی باید د وخت، ساعتونو، دقیقو او ثانیو د لومړني ارزښت لپاره جوړوونکی ولري. ټولګی باید د ToSecond() په نوم بل فنکشن ولري چې وخت په ثانیو بدل او وښيي.'),
        ('Q.9', 'What is object? How objects are created to access members of a class?', 'آبجیکٹ کیا ہے؟ کلاس کے اراکین تک رسائی کے لیے آبجیکٹس کیسے بنائے جاتے ہیں؟', 'شی څه دی؟ د ټولګي غړو ته د لاسرسي لپاره شیان څنګه جوړېږي؟'),
        ('Q.10', 'Explain inheritance and polymorphism with examples.', 'وراثت اور پولی مورفزم کو مثالوں کے ساتھ واضح کریں۔', 'میراث او پولي‌مورفیزم د بېلګو سره تشریح کړئ.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    ex = BOOK.record(e, 'cs12-u8-exercise', 'Unit 8 exercise', 'یونٹ 8: مشق', '۸ څپرکی: تمرین', 134, [256, 257, 258])
    ex['sourceNote'] = 'The exercise runs from p.256 to p.258 (PDF135) and is recorded here whole.'
    BOOK.save(134, [(8, ex)], issues=[{'id': 'cs12-pdf134', 'unit': 8, 'printedPage': 256,
               'description': 'Q1(i) “is a member of function … created..” (double full stop); Q1(iii) “include”. Retained as printed.'}])


def p135():
    t = Builder()
    t.p('Unit 9', 'یونٹ 9', '۹ څپرکی')
    t.h('FILE HANDLING', 'فائل ہینڈلنگ', 'د دوتنو چلول')
    t.h('After the completion of Unit-9, Students will be able to:', 'یونٹ 9 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۹ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    L = lambda *x: t.group('list', list(x))
    L(('Know the binary and text file', 'بائنری اور ٹیکسٹ فائل جان سکیں', 'باینري او متني دوتنه وپېژني'), ('Open the file in different modes', 'فائل کو مختلف موڈز میں کھول سکیں', 'دوتنه په بېلو حالتونو کې پرانیزي'), ('Know the concept of', 'درج ذیل کا تصور جان سکیں', 'د لاندې مفهوم وپېژني'))
    L(('bof()', 'bof()', 'bof()'), ('eof()', 'eof()', 'eof()'))
    L(('Define stream', 'اسٹریم کی تعریف کر سکیں', 'بهیر (stream) تعریف کړي'), ('Use the following stream', 'درج ذیل اسٹریم استعمال کر سکیں', 'لاندې بهیر وکاروي'))
    L(('Single character', 'سنگل کریکٹر', 'یو توری'), ('String', 'اسٹرنگ', 'تار'))
    t.h('INTRODUCTION', 'تعارف', 'سریزه')
    t.p('A file is a collection of related records that are permanently stored in secondary storage. File handling is an important feature of C++ language. This unit describes different types of files such as text files and binary files and describes how different operations like opening, reading, writing and closing are performed on files.',
        'فائل متعلقہ ریکارڈز کا مجموعہ ہے جو ثانوی اسٹوریج میں مستقل طور پر محفوظ ہوتے ہیں۔ فائل ہینڈلنگ C++ زبان کی اہم خصوصیت ہے۔ یہ یونٹ مختلف اقسام کی فائلز جیسے ٹیکسٹ فائلز اور بائنری فائلز بیان کرتا ہے اور بتاتا ہے کہ فائلز پر کھولنا، پڑھنا، لکھنا اور بند کرنا جیسے مختلف عمل کیسے کیے جاتے ہیں۔',
        'دوتنه د اړوندو ریکارډونو ټولګه ده چې په ثانوي زېرمه کې په دایمي توګه ساتل کېږي. د دوتنو چلول د C++ ژبې مهمه ځانګړتیا ده. دا څپرکی د دوتنو بېلابېل ډولونه لکه متني دوتنې او باینري دوتنې بیانوي او ښيي چې پر دوتنو بېلابېلې عملیې لکه پرانیستل، لوستل، لیکل او تړل څنګه ترسره کېږي.')
    t.h('9.1 File handling', '9.1 فائل ہینڈلنگ', '۹.۱ د دوتنو چلول')
    t.p('The combinations of characters, words and records are called files. The operations on these files are the major focus point of file handling. Suppose we have a file on the disk and want to open it then reading from or writing into the file before closing it will be termed as handling files. The basic steps involved in file handling are:',
        'حروف، الفاظ اور ریکارڈز کے مجموعے فائلز کہلاتے ہیں۔ ان فائلز پر عمل فائل ہینڈلنگ کا بنیادی مرکز ہیں۔ فرض کریں ہمارے پاس ڈسک پر ایک فائل ہے اور ہم اسے کھولنا چاہتے ہیں، پھر بند کرنے سے پہلے فائل سے پڑھنا یا اس میں لکھنا فائلز ہینڈل کرنا کہلائے گا۔ فائل ہینڈلنگ کے بنیادی مراحل یہ ہیں:',
        'د تورو، کلمو او ریکارډونو ترکیبونه دوتنې بلل کېږي. پر دې دوتنو عملیې د دوتنو د چلولو اصلي تمرکز دی. فرض کړئ په ډیسک کې یوه دوتنه لرو او غواړو پرانیزو یې، بیا له تړلو مخکې له دوتنې لوستل یا پکې لیکل د دوتنو چلول بلل کېږي. د دوتنو د چلولو بنسټیز ګامونه دا دي:')
    t.group('list', [('Opening file', 'فائل کھولنا', 'دوتنه پرانیستل'), ('Reading and writing a file', 'فائل پڑھنا اور لکھنا', 'دوتنه لوستل او لیکل'), ('Closing file', 'فائل بند کرنا', 'دوتنه تړل')])
    rec9 = BOOK.record(t, 'cs12-u9-outcomes', 'Unit 9: learning outcomes and introduction', 'یونٹ 9: حاصلاتِ تعلم اور تعارف', '۹ څپرکی: د زده‌کړې پایلې او سریزه', 135, [259, 260],
                       unit_title=('File Handling', 'فائل ہینڈلنگ', 'د دوتنو چلول'))
    rec9['sourceNote'] = 'The list of basic steps at the top of p.260 (PDF136) is given here with its lead-in.'
    BOOK.save(135, [(9, rec9)], complete_units=[8])


def p136():
    t = Builder()
    P = t.p
    t.h('9.1.1 Types of files', '9.1.1 فائلز کی اقسام', '۹.۱.۱ د دوتنو ډولونه')
    P('C++ divides files into two different types based on how they store data. These are:', 'C++ فائلز کو ڈیٹا محفوظ کرنے کے طریقے کی بنیاد پر دو مختلف اقسام میں تقسیم کرتی ہے۔ یہ ہیں:', 'C++ دوتنې د ډېټا د ساتلو د طریقې پر بنسټ په دوو بېلو ډولونو وېشي. دا دي:')
    t.group('list', [('Text files', 'ٹیکسٹ فائلز', 'متني دوتنې'), ('Binary files', 'بائنری فائلز', 'باینري دوتنې')])
    P('Text files are those files that store data in text format which is readable by humans. Example of text file is the C++ source program which can be read by human.', 'ٹیکسٹ فائلز وہ فائلز ہیں جو ڈیٹا کو ٹیکسٹ شکل میں محفوظ کرتی ہیں جو انسان پڑھ سکتے ہیں۔ ٹیکسٹ فائل کی مثال C++ سورس پروگرام ہے جسے انسان پڑھ سکتا ہے۔', 'متني دوتنې هغه دوتنې دي چې ډېټا په متني بڼه ساتي چې انسانان یې لوستلی شي. د متني دوتنې بېلګه د C++ سرچینه پروګرام دی چې انسان یې لوستلی شي.')
    P('Binary files store data in binary format which is not readable by the humans but readable by the computers. Binary files are directly processed by the computers. Binary files are normally used to store large data files. They take less space to store data as compared to text files. For example, an integer having length of six digits will take six bytes to accommodate in a text file while in binary files they will take only two bytes. The best example of binary file is the object file of a C++ source file that is generated by the compiler of C++.',
      'بائنری فائلز ڈیٹا کو بائنری شکل میں محفوظ کرتی ہیں جو انسان نہیں پڑھ سکتے لیکن کمپیوٹر پڑھ سکتے ہیں۔ بائنری فائلز پر کمپیوٹر براہِ راست عمل کرتے ہیں۔ بائنری فائلز عموماً بڑی ڈیٹا فائلز محفوظ کرنے کے لیے استعمال ہوتی ہیں۔ یہ ٹیکسٹ فائلز کے مقابلے میں ڈیٹا محفوظ کرنے کے لیے کم جگہ لیتی ہیں۔ مثلاً چھ ہندسوں والا صحیح عدد ٹیکسٹ فائل میں چھ بائٹس لے گا جبکہ بائنری فائلز میں صرف دو بائٹس۔ بائنری فائل کی بہترین مثال C++ سورس فائل کی آبجیکٹ فائل ہے جو C++ کا کمپائلر بناتا ہے۔',
      'باینري دوتنې ډېټا په باینري بڼه ساتي چې انسانان یې نه شي لوستلی خو کمپیوټرونه یې لوستلی شي. پر باینري دوتنو کمپیوټرونه مستقیم پروسس کوي. باینري دوتنې عموماً د لویو ډېټا دوتنو د ساتلو لپاره کارېږي. د متني دوتنو په پرتله د ډېټا د ساتلو لپاره لږ ځای نیسي. د بېلګې په توګه د شپږو عددي رقمونو اوږدوالي صحیح عدد په متني دوتنه کې شپږ بایټه نیسي، په داسې حال کې چې په باینري دوتنو کې یوازې دوه بایټه نیسي. د باینري دوتنې غوره بېلګه د C++ سرچینه دوتنې شي دوتنه (object file) ده چې د C++ کمپایلر یې جوړوي.')
    t.h('9.1.2 Opening file', '9.1.2 فائل کھولنا', '۹.۱.۲ دوتنه پرانیستل')
    P('To open a file, the function open () is used whose syntax is:', 'فائل کھولنے کے لیے فنکشن open () استعمال ہوتا ہے جس کا طریقۂ تحریر یہ ہے:', 'د دوتنې د پرانیستلو لپاره open () فنکشن کارېږي چې بڼه یې دا ده:')
    code(t, 'myFile.open(filename);')
    P('Here, myFile is an internal variable, actually an object, used to handle the file whose name is written in the parenthesis. To declare this variable the following statement is used:', 'یہاں myFile ایک اندرونی ویری ایبل، دراصل ایک آبجیکٹ، ہے جو اس فائل کو ہینڈل کرنے کے لیے استعمال ہوتا ہے جس کا نام قوسین میں لکھا ہے۔ اس ویری ایبل کو ڈکلیئر کرنے کے لیے درج ذیل بیان استعمال ہوتا ہے:', 'دلته myFile یو داخلي متغیر، په اصل کې یو شی، دی چې د هغې دوتنې د چلولو لپاره کارېږي چې نوم یې په قوسونو کې لیکل شوی. د دې متغیر د اعلان لپاره لاندې بیان کارېږي:')
    code(t, 'Ifstream myFile;')
    P('The dot . operator is used between the variable myFile and open function. myFile is an object of ifstream while open() is a function of ifstream. The argument for open function is the name of the file on the disk which should be enclosed in double quotes. The file name can be simple file name like “sale.txt”. It can also fully qualify path name like “C:\\myprogs\\sale.txt”.',
      'ویری ایبل myFile اور open فنکشن کے درمیان ڈاٹ . آپریٹر استعمال ہوتا ہے۔ myFile، ifstream کا آبجیکٹ ہے جبکہ open()، ifstream کا فنکشن ہے۔ open فنکشن کا آرگیومنٹ ڈسک پر فائل کا نام ہے جو ڈبل کوٹس میں بند ہونا چاہیے۔ فائل کا نام سادہ ہو سکتا ہے جیسے ’’sale.txt‘‘۔ یہ مکمل راستے والا نام بھی ہو سکتا ہے جیسے ’’C:\\myprogs\\sale.txt‘‘۔',
      'د myFile متغیر او open فنکشن ترمنځ د ټکي . چلونکی کارېږي. myFile د ifstream شی دی او open() د ifstream فنکشن دی. د open فنکشن دلیل په ډیسک کې د دوتنې نوم دی چې باید په دوه‌ګونو نقل‌قولونو کې وتړل شي. د دوتنې نوم کېدای شي ساده نوم وي لکه "sale.txt". همداراز کېدای شي بشپړ د لارې نوم وي لکه "C:\\myprogs\\sale.txt".')
    t.h('a. Modes of opening a file', 'a. فائل کھولنے کے موڈز', 'a. د دوتنې د پرانیستلو حالتونه')
    P('While opening a file, we tell the compiler what we want to do with it i.e. we want to read the file or write into the file or want to modify it. In order to open a file in any desired mode the member function open () should take mode as an argument along with the file name. Its general syntax is shown below:',
      'فائل کھولتے وقت ہم کمپائلر کو بتاتے ہیں کہ ہم اس کے ساتھ کیا کرنا چاہتے ہیں یعنی فائل پڑھنا، فائل میں لکھنا یا اسے تبدیل کرنا چاہتے ہیں۔ فائل کو کسی بھی مطلوبہ موڈ میں کھولنے کے لیے ممبر فنکشن open () کو فائل کے نام کے ساتھ موڈ بطور آرگیومنٹ لینا چاہیے۔ اس کا عمومی طریقۂ تحریر ذیل میں ہے:',
      'د دوتنې د پرانیستلو پر مهال کمپایلر ته وایو چې ورسره څه کول غواړو، یعنې غواړو دوتنه ولولو، پکې ولیکو یا یې بدله کړو. د دوتنې په هر غوښتل شوي حالت کې د پرانیستلو لپاره open () غړی فنکشن باید د دوتنې له نوم سره حالت هم د دلیل په توګه واخلي. عمومي بڼه یې لاندې ده:')
    code(t, 'open (filename, mode);')
    P('Here, file name representing the name of the file to be opened, and mode is an optional parameter with a combination of the following flags:', 'یہاں file name کھولی جانے والی فائل کا نام ظاہر کرتا ہے اور mode درج ذیل فلیگز کے مجموعے والا اختیاری پیرامیٹر ہے:', 'دلته file name د پرانیستل کېدونکې دوتنې نوم ښيي او mode د لاندې بیرغونو (flags) د ترکیب سره اختیاري پاراميټر دی:')
    R = [['ios::in', 'Open for input operations.'], ['ios::out', 'Open for output operations.'], ['ios::binary', 'Open in binary mode.'],
         ['ios::ate', 'Set the initial position at the end of the file. If this flag is not set to any value, the initial position is the beginning of the file.'],
         ['ios::app', 'All output operations are performed at the end of the file, appending the content to the current content of the file. This flag can only be used in streams open for output-only operations.'],
         ['ios::trunk', 'If the file opened for output operations already exists then its previous contents are deleted and replaced by the new one.']]
    Ru = [['ios::in', 'ان پٹ عمل کے لیے کھولیں۔'], ['ios::out', 'آؤٹ پٹ عمل کے لیے کھولیں۔'], ['ios::binary', 'بائنری موڈ میں کھولیں۔'],
          ['ios::ate', 'ابتدائی مقام فائل کے آخر پر رکھیں۔ اگر یہ فلیگ کسی قدر پر سیٹ نہ ہو تو ابتدائی مقام فائل کا آغاز ہوتا ہے۔'],
          ['ios::app', 'تمام آؤٹ پٹ عمل فائل کے آخر پر کیے جاتے ہیں اور مواد فائل کے موجودہ مواد کے ساتھ جوڑا جاتا ہے۔ یہ فلیگ صرف آؤٹ پٹ کے لیے کھلی اسٹریمز میں استعمال ہو سکتا ہے۔'],
          ['ios::trunk', 'اگر آؤٹ پٹ کے لیے کھولی گئی فائل پہلے سے موجود ہو تو اس کا پچھلا مواد حذف ہو کر نئے مواد سے بدل جاتا ہے۔']]
    Rp = [['ios::in', 'د ننوتنې عملیو لپاره پرانیزئ.'], ['ios::out', 'د وتنې عملیو لپاره پرانیزئ.'], ['ios::binary', 'په باینري حالت کې پرانیزئ.'],
          ['ios::ate', 'لومړنی ځای د دوتنې پای ته وټاکئ. که دا بیرغ هېڅ ارزښت ته ونه ټاکل شي، لومړنی ځای د دوتنې پیل دی.'],
          ['ios::app', 'ټولې د وتنې عملیې د دوتنې په پای کې ترسره کېږي او منځپانګه د دوتنې اوسنۍ منځپانګې ته ورزیاتېږي. دا بیرغ یوازې په هغو بهیرونو کې کارېدای شي چې یوازې د وتنې لپاره پرانیستل شوي.'],
          ['ios::trunk', 'که د وتنې لپاره پرانیستل شوې دوتنه مخکې شتون ولري، پخوانۍ منځپانګه یې ړنګېږي او په نوې بدلېږي.']]
    t.table('cs12-table-9-modes', ['Flag', 'Meaning'], R, ['فلیگ', 'مطلب'], ['بیرغ', 'معنا'], Ru, Rp, noHeader=True)
    BOOK.save(136, [(9, rec(t, 1, 136, [260, 261], 'The list of basic steps at the top of p.260 is recorded with PDF135. The modes table is reproduced as a structured table; the printed table has no header row.'))],
              issues=[{'id': 'cs12-pdf136', 'unit': 9, 'printedPage': 261,
                       'description': 'The modes table prints “ios::trunk” (the C++ flag is ios::trunc); p.260 declares “Ifstream myFile;” with a capital I; p.261 “file name representing the name”, “It can also fully qualify path name”. Retained as printed.'}])


def p137():
    t = Builder()
    P = t.p
    P('All these flags can be combined using the bitwise operator OR |. For example, if we want to open the file test.bin in binary mode to add data we could do it by the following call to member function open().', 'یہ تمام فلیگز bitwise آپریٹر OR | کے ذریعے ملائے جا سکتے ہیں۔ مثلاً اگر ہم فائل test.bin کو ڈیٹا شامل کرنے کے لیے بائنری موڈ میں کھولنا چاہیں تو ممبر فنکشن open() کو درج ذیل کال سے ایسا کر سکتے ہیں۔', 'دا ټول بیرغونه د bitwise چلونکي OR | په مرسته یوځای کېدای شي. د بېلګې په توګه که وغواړو test.bin دوتنه د ډېټا د زیاتولو لپاره په باینري حالت کې پرانیزو، د open() غړي فنکشن ته د لاندې غوښتنې په مرسته یې کولی شو.')
    code(t, '''Ofstream myfile;
myfile.open ("test.bin", ios::out | ios::app | ios::binary);''')
    P('Each one of the open() member functions of the classes of stream, ifstream and fstream has a default mode that is used if the file is opened without a second argument:', 'کلاسز of stream، ifstream اور fstream کے ہر open() ممبر فنکشن کا ایک ڈیفالٹ موڈ ہوتا ہے جو اس وقت استعمال ہوتا ہے جب فائل دوسرے آرگیومنٹ کے بغیر کھولی جائے:', 'د of stream، ifstream او fstream ټولګیو د open() هر غړي فنکشن یو ډیفالټ حالت لري چې هغه وخت کارېږي چې دوتنه پرته له دویم دلیل پرانیستل شي:')
    t.table('cs12-table-9-default', ['class', 'default mode parameter'], [['ofstream', 'ios::out'], ['ifstream', 'ios::in'], ['fstream', 'ios::in | ios::out']],
            ['کلاس', 'ڈیفالٹ موڈ پیرامیٹر'], ['ټولګی', 'ډیفالټ حالت پاراميټر'], [['ofstream', 'ios::out'], ['ifstream', 'ios::in'], ['fstream', 'ios::in | ios::out']], [['ofstream', 'ios::out'], ['ifstream', 'ios::in'], ['fstream', 'ios::in | ios::out']])
    P('For ifstream and ofstream classes, ios::in and ios::out are automatically and respectively assumed, even if a mode that does not include them is passed as second argument to the open() member function.', 'ifstream اور ofstream کلاسز کے لیے بالترتیب ios::in اور ios::out خود بخود فرض کر لیے جاتے ہیں، چاہے open() ممبر فنکشن کو دوسرے آرگیومنٹ کے طور پر ایسا موڈ پاس کیا جائے جس میں یہ شامل نہ ہوں۔', 'د ifstream او ofstream ټولګیو لپاره په ترتیب سره ios::in او ios::out پخپله ګڼل کېږي، حتی که open() غړي فنکشن ته د دویم دلیل په توګه داسې حالت ولېږدول شي چې دا پکې شامل نه وي.')
    P('Let us see an example program that creates a text file “example1.txt” and writes a line of text in it.', 'آئیے ایک مثالی پروگرام دیکھیں جو ٹیکسٹ فائل ’’example1.txt‘‘ بناتا ہے اور اس میں متن کی ایک لائن لکھتا ہے۔', 'راځئ یو بېلګه‌ییز پروګرام وګورو چې "example1.txt" متني دوتنه جوړوي او پکې د متن یوه کرښه لیکي.')
    code(t, '''//opening a file and writing into it
#include <iostream.h>
#include <fstream.h>
#include <conio.h>
int main()
{
Ofstream myfile;
myfile.open ("example1.txt");
myfile<< "This is a program that tells you how to write to a file.\\n";
myfile.close();
getch();
return 0;
}''')
    P('This code creates a file called example1.txt and inserts a sentence into it in the same way as we do with cout, but using the file stream myfile instead. Figure 9.1 shows the output of the above program in the form of a text file that is created in the same working directory.',
      'یہ کوڈ example1.txt نامی فائل بناتا ہے اور اس میں ایک جملہ اسی طرح داخل کرتا ہے جیسے ہم cout سے کرتے ہیں، لیکن اس کے بجائے فائل اسٹریم myfile استعمال کر کے۔ شکل 9.1 اوپر کے پروگرام کا آؤٹ پٹ ایک ٹیکسٹ فائل کی صورت میں دکھاتی ہے جو اسی ورکنگ ڈائریکٹری میں بنتی ہے۔',
      'دا کوډ example1.txt په نوم دوتنه جوړوي او پکې یوه جمله همداسې ورګډوي لکه څنګه چې یې د cout سره کوو، خو د دې پر ځای د myfile د دوتنې بهیر کاروي. ۹.۱ شکل د پورته پروګرام وتنه د یوې متني دوتنې په بڼه ښيي چې په همغه کاري لارښود کې جوړېږي.')
    win(t, 'cs12-fig-9-1', 'example1.txt - Notepad', ['This is a program that tells you how to write to a file.'],
        ('Figure 9.1: Opening and Writing into a Text File', 'شکل 9.1: ٹیکسٹ فائل کھولنا اور اس میں لکھنا', '۹.۱ شکل: متني دوتنه پرانیستل او پکې لیکل'))
    t.h('b. Reading input file', 'b. ان پٹ فائل پڑھنا', 'b. د ننوتنې دوتنه لوستل')
    P('To read a word from the file we can write as:', 'فائل سے ایک لفظ پڑھنے کے لیے ہم یوں لکھ سکتے ہیں:', 'له دوتنې د یوې کلمې د لوستلو لپاره داسې لیکلی شو:')
    code(t, 'myFile>> c;')
    P('So, the first word of the file will be read in c, where c is a character array. It is similar as we used with cin. There are certain limitations to this. It can read just one word at one time. It means, on encountering a space, it will stop reading further. Therefore, we have to use it repeatedly to read the complete file. We can also read multiple words at a time as:',
      'یوں فائل کا پہلا لفظ c میں پڑھا جائے گا، جہاں c حروف کا ایرے ہے۔ یہ اسی طرح ہے جیسے ہم نے cin کے ساتھ استعمال کیا۔ اس کی کچھ حدود ہیں۔ یہ ایک وقت میں صرف ایک لفظ پڑھ سکتا ہے۔ یعنی خالی جگہ آنے پر یہ مزید پڑھنا بند کر دے گا۔ اس لیے پوری فائل پڑھنے کے لیے ہمیں اسے بار بار استعمال کرنا ہوگا۔ ہم ایک وقت میں متعدد الفاظ بھی یوں پڑھ سکتے ہیں:',
      'نو د دوتنې لومړۍ کلمه به په c کې ولوستل شي، چېرته چې c د تورو لړۍ ده. دا هماغسې ده لکه د cin سره مو چې کارولې. دا ځینې محدودیتونه لري. په یوه وخت کې یوازې یوه کلمه لوستلی شي. یعنې د تش ځای په لیدو به نور لوستل ودروي. نو د ټولې دوتنې د لوستلو لپاره باید بیا بیا وکارول شي. موږ کولی شو په یوه وخت کې څو کلمې هم داسې ولولو:')
    code(t, 'myFile>> c1 >> c2 >> c3;')
    BOOK.save(137, [(9, rec(t, 2, 137, [262, 263, 264], 'Figure 9.1 (a Notepad window) is redrawn as a coded mock-up. The paragraph on reading words continues on p.264 (PDF138) and is given whole here.'))],
              issues=[{'id': 'cs12-pdf137', 'unit': 9, 'printedPage': 262,
                       'description': 'p.262 writes “Ofstream myfile;” with a capital O and “classes of stream” for ofstream; p.263 “read just one word at one time”. Retained as printed.'}])


def p138():
    t = Builder()
    P = t.p
    P('The first word will be read in c1, second in c2 and third in c3. Before reading the file, we should know some information regarding the structure of the file. If we have a file of an employee, we should know that the first word is employee’s name, second word is salary etc,so that we can read the first word in a string and second word in an int variable.',
      'پہلا لفظ c1 میں، دوسرا c2 میں اور تیسرا c3 میں پڑھا جائے گا۔ فائل پڑھنے سے پہلے ہمیں فائل کے ڈھانچے کے بارے میں کچھ معلومات ہونی چاہییں۔ اگر ہمارے پاس کسی ملازم کی فائل ہو تو ہمیں معلوم ہونا چاہیے کہ پہلا لفظ ملازم کا نام، دوسرا لفظ تنخواہ وغیرہ ہے، تاکہ ہم پہلا لفظ string میں اور دوسرا لفظ int ویری ایبل میں پڑھ سکیں۔',
      'لومړۍ کلمه به په c1، دویمه په c2 او درېیمه په c3 کې ولوستل شي. د دوتنې له لوستلو مخکې باید د دوتنې د جوړښت په اړه ځینې معلومات ولرو. که د یوه کارمند دوتنه ولرو، باید پوه شو چې لومړۍ کلمه د کارمند نوم، دویمه کلمه معاش او نور دي، ترڅو لومړۍ کلمه په string او دویمه کلمه په int متغیر کې ولولو.')
    P('Consider the following input file “inputfile.txt”, shown in figure 9.2, which is read and displayed on the screen.', 'درج ذیل ان پٹ فائل ’’inputfile.txt‘‘ پر غور کریں جو شکل 9.2 میں دکھائی گئی ہے اور جسے پڑھ کر اسکرین پر دکھایا جاتا ہے۔', 'لاندې د ننوتنې دوتنې "inputfile.txt" ته پام وکړئ چې په ۹.۲ شکل کې ښودل شوې او لوستل کېږي او پر پرده ښودل کېږي.')
    win(t, 'cs12-fig-9-2', 'inputfile - Notepad', ['Ali       20'], ('Figure 9.2: Input File to be Read', 'شکل 9.2: پڑھی جانے والی ان پٹ فائل', '۹.۲ شکل: د لوستلو وړ د ننوتنې دوتنه'))
    code(t, '''//reading input file program
#include <iostream.h>
#include <fstream.h>
#include <conio.h>
int main()
{
Ifstream myfile("c:\\\\inputfile.txt");
Char ch [20];
int m;
myfile>>ch>>m;
cout<<ch<<"\\t"<<m;
myfile.close();
getch();
return 0;
}''')
    P('The output of the above program is shown in figure 9.3:', 'اوپر کے پروگرام کا آؤٹ پٹ شکل 9.3 میں دکھایا گیا ہے:', 'د پورته پروګرام وتنه په ۹.۳ شکل کې ښودل شوې:')
    win(t, 'cs12-fig-9-3', 'C:\\BC5\\...', ['Ali       20'], ('Figure 9.3: Output of Reading Program', 'شکل 9.3: پڑھنے والے پروگرام کا آؤٹ پٹ', '۹.۳ شکل: د لوستلو پروګرام وتنه'), dark=True)
    P('Let us write another simple program, to read from a file ‘myfile.txt’ that is in the current directory, and print it on the screen. “myfile.txt” contains employee’s name, salary and department in which they are employed. Figure 9.4 shows myfile.txt which is followed by the complete program to describe how it is opened, read and closed.',
      'آئیے ایک اور سادہ پروگرام لکھیں جو موجودہ ڈائریکٹری میں موجود فائل ‘myfile.txt’ سے پڑھ کر اسے اسکرین پر پرنٹ کرے۔ ’’myfile.txt‘‘ میں ملازم کا نام، تنخواہ اور وہ شعبہ ہے جس میں وہ ملازم ہیں۔ شکل 9.4 میں myfile.txt دکھائی گئی ہے جس کے بعد مکمل پروگرام ہے جو بتاتا ہے کہ اسے کیسے کھولا، پڑھا اور بند کیا جاتا ہے۔',
      'راځئ بل ساده پروګرام ولیکو چې په اوسني لارښود کې له ‘myfile.txt’ دوتنې ولولي او پر پرده یې چاپ کړي. "myfile.txt" د کارمند نوم، معاش او هغه څانګه لري چې پکې کار کوي. ۹.۴ شکل myfile.txt ښيي چې وروسته یې بشپړ پروګرام راځي ترڅو وښيي چې څنګه پرانیستل کېږي، لوستل کېږي او تړل کېږي.')
    win(t, 'cs12-fig-9-4', 'myfile.txt - Notepad', ['Name Salary Department', '', 'Hashim 12000 Sales', 'Amara 15000 HR', 'Athar 13000 IT', 'Afzal 11500 Marketing'],
        ('Figure 9.4: Input File to be Read', 'شکل 9.4: پڑھی جانے والی ان پٹ فائل', '۹.۴ شکل: د لوستلو وړ د ننوتنې دوتنه'))
    BOOK.save(138, [(9, rec(t, 3, 138, [264, 265], 'The opening lines of p.264 are recorded with PDF137. Figures 9.2–9.4 (Notepad and console windows) are redrawn as coded mock-ups with their printed contents.'))],
              issues=[{'id': 'cs12-pdf138', 'unit': 9, 'printedPage': 264,
                       'description': 'The reading program writes “Ifstream” and “Char” with capitals; p.264 “salary etc,so”. Retained as printed.'}])


def p139():
    t = Builder()
    P = t.p
    code(t, '''#include <iostream.h>
#include <fstream.h>
#include <conio.h>
main()
{
Char name[50]; // used to read name of employee from file
Char sal[10]; // used to read salary of employee from file
Char dept[30]; // used to read dept of employee from file
Ifstream inFile; // Handle for the input file
Charin putFileName[] = "myfile.txt"; // file name, this file is in the current directory
inFile.open(inputFileName); // Opening the file
// checking that file is successfully opened or not
if (!inFile)
{
cout<< "Can't open input file named " <<inputFileName<<endl;
exit(1);
}
// Reading the complete file word by word and printing on screen
while (!inFile.eof())
{
inFile>> name >>sal>>dept;
cout<< name << "\\t" <<sal<< " \\t" <<dept<<endl;
}
inFile.close();
getch();
return 0;
}''')
    win(t, 'cs12-fig-9-5', 'C:\\Documents and Settings\\shaukat\\My Documents\\C Examples ...', ['Name    Salary  Department', 'Hashim  12000   Sales', 'Amara   15000   HR', 'Athar   13000   IT', 'Afzal   11500   Marketing'],
        ('Figure 9.5: Output of the rogram that is Read from Input File myFile txt', 'شکل 9.5: ان پٹ فائل myFile txt سے پڑھنے والے پروگرام کا آؤٹ پٹ', '۹.۵ شکل: د هغه پروګرام وتنه چې د myFile txt له ننوتنې دوتنې لولي'), dark=True)
    t.h('c. Closing file', 'c. فائل بند کرنا', 'c. دوتنه تړل')
    P('Once we have read the file, it must be closed. It is the responsibility of the programmer to close the file. We can close the file by using the following statement:', 'فائل پڑھنے کے بعد اسے بند کرنا ضروری ہے۔ فائل بند کرنا پروگرامر کی ذمہ داری ہے۔ ہم درج ذیل بیان سے فائل بند کر سکتے ہیں:', 'کله چې دوتنه مو ولوستله، باید وتړل شي. د دوتنې تړل د پروګرام جوړوونکي مسؤلیت دی. موږ کولی شو د لاندې بیان په مرسته دوتنه وتړو:')
    code(t, 'myFile.close();')
    P('The function close() does not require any argument, as we are going to close the file associated with myFile. Once we close the file, no file will be associated with myfile.', 'فنکشن close() کو کسی آرگیومنٹ کی ضرورت نہیں کیونکہ ہم myFile سے وابستہ فائل بند کرنے جا رہے ہیں۔ فائل بند کرنے کے بعد myfile سے کوئی فائل وابستہ نہیں رہے گی۔', 'close() فنکشن هېڅ دلیل ته اړتیا نه لري، ځکه موږ هغه دوتنه تړو چې له myFile سره تړلې ده. کله چې دوتنه وتړو، له myfile سره به هېڅ دوتنه تړلې نه وي.')
    t.h('d. Opening files in binary mode', 'd. بائنری موڈ میں فائلز کھولنا', 'd. په باینري حالت کې دوتنې پرانیستل')
    P('To open a file in binary mode, we need to set the file mode to ios::binary. Suppose we have a binary file named as “test.dat”. To open this file in binary mode, we write the statement as:', 'فائل کو بائنری موڈ میں کھولنے کے لیے ہمیں فائل موڈ ios::binary پر سیٹ کرنا ہوتا ہے۔ فرض کریں ہمارے پاس ’’test.dat‘‘ نامی بائنری فائل ہے۔ اس فائل کو بائنری موڈ میں کھولنے کے لیے ہم یہ بیان لکھتے ہیں:', 'د دوتنې په باینري حالت کې د پرانیستلو لپاره باید د دوتنې حالت ios::binary ته وټاکو. فرض کړئ د "test.dat" په نوم باینري دوتنه لرو. د دې دوتنې په باینري حالت کې د پرانیستلو لپاره بیان داسې لیکو:')
    code(t, '''ofstream myFile;
myFile.open (“test.dat”, ios::binary);''')
    P('In order to write the data to a binary file, “write” method is used. This method is a member function of ofstream or fstream class.', 'بائنری فائل میں ڈیٹا لکھنے کے لیے ’’write‘‘ میتھڈ استعمال ہوتا ہے۔ یہ میتھڈ ofstream یا fstream کلاس کا ممبر فنکشن ہے۔', 'باینري دوتنې ته د ډېټا د لیکلو لپاره "write" میتود کارېږي. دا میتود د ofstream یا fstream ټولګي غړی فنکشن دی.')
    BOOK.save(139, [(9, rec(t, 4, 139, [266, 267], 'The program on p.266 belongs to Figure 9.4; Figure 9.5 (console output) is redrawn as a coded mock-up. The partly cut console title is given as far as it is legible.'))],
              issues=[{'id': 'cs12-pdf139', 'unit': 9, 'printedPage': 266,
                       'description': 'The program declares “Charin putFileName[]” (split identifier) and uses “Char”, “Ifstream” and main() without a return type; the Figure 9.5 caption reads “Output of the rogram”. Retained as printed. The heading letter “d.” is lost in the gutter of p.267 and is supplied from the a–c sequence.'}])


def p140():
    t = Builder()
    P = t.p
    t.h('9.1.3 bof() and eof()', '9.1.3 bof() اور eof()', '۹.۱.۳ bof() او eof()')
    P('C++ provides special functions bof() and eof() that are used to set the pointers to the beginning of a file and at the end of a file respectively. The following sections explain them with the help of proper examples.', 'C++ خاص فنکشنز bof() اور eof() فراہم کرتی ہے جو بالترتیب پوائنٹرز کو فائل کے آغاز اور فائل کے اختتام پر سیٹ کرنے کے لیے استعمال ہوتے ہیں۔ درج ذیل حصے مناسب مثالوں کی مدد سے ان کی وضاحت کرتے ہیں۔', 'C++ ځانګړي فنکشنونه bof() او eof() برابروي چې په ترتیب سره پوائنټرونه د دوتنې پیل او د دوتنې پای ته ټاکي. لاندې برخې د مناسبو بېلګو په مرسته دا تشریح کوي.')
    t.h('a. bof() – beginning-of-file', 'a. bof() – فائل کا آغاز', 'a. bof() – د دوتنې پیل')
    P('The bof() is a pointer which returns true if the current position of the pointer is at the beginning of the input file stream, and false otherwise. It means that it tells the compiler whether the cursor is at the beginning of file or not.', 'bof() ایک پوائنٹر ہے جو true واپس کرتا ہے اگر پوائنٹر کا موجودہ مقام ان پٹ فائل اسٹریم کے آغاز پر ہو، ورنہ false۔ یعنی یہ کمپائلر کو بتاتا ہے کہ کرسر فائل کے آغاز پر ہے یا نہیں۔', 'bof() یو پوائنټر دی چې true بېرته ورکوي که د پوائنټر اوسنی ځای د ننوتنې دوتنې بهیر په پیل کې وي، او که نه false. یعنې کمپایلر ته وايي چې کرسر د دوتنې په پیل کې دی که نه.')
    code(t, 'myFile.close();')
    t.h('b. eof() – end-of-file', 'b. eof() – فائل کا اختتام', 'b. eof() – د دوتنې پای')
    P('The eof() is a pointer which returns true when there are no more data to be read from an input file stream, and false otherwise. It means that this function checks whether control has reached to the end of file or not. This function is very useful in the case when we do not know the exact number of records in a file.',
      'eof() ایک پوائنٹر ہے جو true واپس کرتا ہے جب ان پٹ فائل اسٹریم سے پڑھنے کے لیے مزید ڈیٹا نہ ہو، ورنہ false۔ یعنی یہ فنکشن جانچتا ہے کہ کنٹرول فائل کے اختتام تک پہنچ گیا ہے یا نہیں۔ یہ فنکشن اس صورت میں بہت مفید ہے جب ہمیں فائل میں ریکارڈز کی درست تعداد معلوم نہ ہو۔',
      'eof() یو پوائنټر دی چې true بېرته ورکوي کله چې د ننوتنې دوتنې له بهیر د لوستلو لپاره نور ډېټا پاتې نه وي، او که نه false. یعنې دا فنکشن ګوري چې کنټرول د دوتنې پای ته رسېدلی که نه. دا فنکشن هغه وخت ډېر ګټور دی چې په دوتنه کې د ریکارډونو دقیق شمېر ونه پېژنو.')
    P('Rules for using eof( )', 'eof( ) کے استعمال کے اصول', 'د eof( ) د کارونې قواعد')
    t.group('list', [('Always test for the end-of-file condition before processing data.', 'ڈیٹا پر عمل کرنے سے پہلے ہمیشہ فائل کے اختتام کی شرط جانچیں۔', 'د ډېټا له پروسس مخکې تل د دوتنې د پای شرط وازمویئ.'),
                     ('Use a while loop for getting data from an input file stream. A for loop is desirable only when you know the exact number of data items in the file', 'ان پٹ فائل اسٹریم سے ڈیٹا لینے کے لیے while لوپ استعمال کریں۔ for لوپ صرف اس وقت مناسب ہے جب آپ کو فائل میں ڈیٹا آئٹمز کی درست تعداد معلوم ہو', 'د ننوتنې دوتنې له بهیر د ډېټا د اخیستلو لپاره while حلقه وکاروئ. for حلقه یوازې هغه وخت غوره ده چې په دوتنه کې د ډېټا توکو دقیق شمېر وپېژنئ')])
    code(t, '''// reading a text file using eof() function
#include <iostream.h>
#include <conio.h>
#include <fstream.h>
int main()
{
char ch [50];
ifstream flag ("c:\\\\TestRecord.txt");
cout<<"Output is"<<endl;
while(!flag.eof())
{
flag>>ch;
cout<<ch<<endl;
}
flag.close();
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Output is
Ali     20
Anwar 15
Zainab 17
Zonash21''')
    P('In the above program, the input file TestRecord is loaded and the eof () function detects the end of file. The program reads the file record by record into the string variable ch which is then displayed on the screen.', 'اوپر کے پروگرام میں ان پٹ فائل TestRecord لوڈ کی جاتی ہے اور eof () فنکشن فائل کا اختتام معلوم کرتا ہے۔ پروگرام فائل کو ریکارڈ بہ ریکارڈ اسٹرنگ ویری ایبل ch میں پڑھتا ہے جسے پھر اسکرین پر دکھایا جاتا ہے۔', 'په پورته پروګرام کې د ننوتنې دوتنه TestRecord پورته کېږي او eof () فنکشن د دوتنې پای پېژني. پروګرام دوتنه ریکارډ په ریکارډ د ch تار متغیر ته لولي چې بیا پر پرده ښودل کېږي.')
    t.h('9.1.4 Stream', '9.1.4 اسٹریم', '۹.۱.۴ بهیر (Stream)')
    P('A stream can be thought of as a sequence of bytes of infinite length that is used as a buffer to hold data to be processed. In C++ a stream is a sequence of bytes associated with a file. Most of the times streams are used to assure a good and secure flow of data between an application and file.',
      'اسٹریم کو لامحدود لمبائی کے بائٹس کی ترتیب سمجھا جا سکتا ہے جو عمل کیے جانے والے ڈیٹا کو رکھنے کے لیے بفر کے طور پر استعمال ہوتی ہے۔ C++ میں اسٹریم فائل سے وابستہ بائٹس کی ترتیب ہے۔ زیادہ تر اسٹریمز ایپلیکیشن اور فائل کے درمیان ڈیٹا کے اچھے اور محفوظ بہاؤ کو یقینی بنانے کے لیے استعمال ہوتی ہیں۔',
      'بهیر (stream) د نامحدود اوږدوالي د بایټونو لړۍ ګڼل کېدای شي چې د پروسس کېدونکي ډېټا د ساتلو لپاره د بفر په توګه کارېږي. په C++ کې بهیر له یوې دوتنې سره تړلې د بایټونو لړۍ ده. ډېری وخت بهیرونه د کاريال او دوتنې ترمنځ د ډېټا د ښه او خوندي بهیر د ډاډ لپاره کارېږي.')
    P('In C++ there are two types of streams, input stream and output stream.', 'C++ میں اسٹریمز کی دو اقسام ہیں، ان پٹ اسٹریم اور آؤٹ پٹ اسٹریم۔', 'په C++ کې دوه ډوله بهیرونه دي، د ننوتنې بهیر او د وتنې بهیر.')
    BOOK.save(140, [(9, rec(t, 5, 140, [268, 269]))], issues=[{'id': 'cs12-pdf140', 'unit': 9, 'printedPage': 268,
               'description': 'Under “a. bof()” the book prints the unrelated statement “myFile.close();”; bof() is not a standard C++ function and both bof()/eof() are called “a pointer”; the output shows “Zonash21” without a space and “Ali 20” pairs although the program prints one word per line. Retained as printed.'}])


def p141():
    t = Builder()
    P = t.p
    P('Input streams take any sequence of bytes from an input device such as a keyboard, a file, or a network, while output streams are used to hold output for a particular data consumer, such as a monitor, a file, or a printer. When writing data to an output device, the device may not be ready to accept that data e.g. the printer may still be warming up when the program writes data to its output stream. The data will reside in the output stream until the printer starts consuming it.',
      'ان پٹ اسٹریمز کسی ان پٹ ڈیوائس جیسے کی بورڈ، فائل یا نیٹ ورک سے بائٹس کی کوئی بھی ترتیب لیتی ہیں، جبکہ آؤٹ پٹ اسٹریمز کسی خاص ڈیٹا صارف جیسے مانیٹر، فائل یا پرنٹر کے لیے آؤٹ پٹ رکھنے کے لیے استعمال ہوتی ہیں۔ آؤٹ پٹ ڈیوائس پر ڈیٹا لکھتے وقت ممکن ہے ڈیوائس ڈیٹا قبول کرنے کے لیے تیار نہ ہو، مثلاً جب پروگرام اپنی آؤٹ پٹ اسٹریم میں ڈیٹا لکھتا ہے تو پرنٹر ابھی گرم ہو رہا ہو۔ ڈیٹا اس وقت تک آؤٹ پٹ اسٹریم میں رہے گا جب تک پرنٹر اسے استعمال کرنا شروع نہ کرے۔',
      'د ننوتنې بهیرونه له یوې د ننوتنې وسیلې لکه کیبورډ، دوتنې یا شبکې د بایټونو هره لړۍ اخلي، په داسې حال کې چې د وتنې بهیرونه د یوه ځانګړي ډېټا مصرفوونکي لکه مانیټر، دوتنې یا چاپګر لپاره د وتنې د ساتلو لپاره کارېږي. د وتنې وسیلې ته د ډېټا د لیکلو پر مهال ښايي وسیله د ډېټا منلو ته چمتو نه وي، د بېلګې په توګه چاپګر لا تودېږي کله چې پروګرام خپل د وتنې بهیر ته ډېټا لیکي. ډېټا به تر هغه په د وتنې بهیر کې پاتې وي چې چاپګر یې مصرف پیل کړي.')
    P('The act of taking data from the input devices is called extraction and the operator used for this purpose is called stream extraction operator >>. Similarly, the act of displaying data on the screen is called insertion and the operator used for this purpose is called stream insertion operator <<.',
      'ان پٹ ڈیوائسز سے ڈیٹا لینے کا عمل extraction کہلاتا ہے اور اس مقصد کے لیے استعمال ہونے والا آپریٹر stream extraction operator >> کہلاتا ہے۔ اسی طرح اسکرین پر ڈیٹا دکھانے کا عمل insertion کہلاتا ہے اور اس مقصد کے لیے استعمال ہونے والا آپریٹر stream insertion operator << کہلاتا ہے۔',
      'له د ننوتنې وسیلو د ډېټا اخیستل extraction بلل کېږي او د دې موخې لپاره کارېدونکی چلونکی stream extraction operator >> بلل کېږي. همداراز پر پرده د ډېټا ښودل insertion بلل کېږي او د دې موخې لپاره کارېدونکی چلونکی stream insertion operator << بلل کېږي.')
    P('Sometimes, both operations input/output may need to be used at the same time. Standard streams in C++ consist of four predefined standard stream objects. These are: cin, cout, cerr and clog. C++ language handles files using these streams objects. For this purpose, the header file <fstream.h> is needed to be included.',
      'بعض اوقات ان پٹ/آؤٹ پٹ دونوں عمل ایک ساتھ استعمال کرنے پڑ سکتے ہیں۔ C++ میں معیاری اسٹریمز چار پہلے سے طے شدہ معیاری اسٹریم آبجیکٹس پر مشتمل ہیں۔ یہ ہیں: cin، cout، cerr اور clog۔ C++ زبان ان اسٹریم آبجیکٹس کے ذریعے فائلز ہینڈل کرتی ہے۔ اس مقصد کے لیے ہیڈر فائل <fstream.h> شامل کرنا ضروری ہے۔',
      'کله کله ښايي د ننوتنې/وتنې دواړه عملیې په یوه وخت وکارول شي. په C++ کې معیاري بهیرونه له څلورو مخکې ټاکل شویو معیاري بهیر شیانو جوړ دي. دا دي: cin، cout، cerr او clog. C++ ژبه د دې بهیر شیانو په مرسته دوتنې چلوي. د دې موخې لپاره د <fstream.h> سرپاڼه دوتنې شاملول اړین دي.')
    P('If the file is only used for reading purpose then the header file ifstream (input file stream) is needed to be included. Similarly, if one wants to write in some file then header file ofstream (output file stream) is needed. One can read, write and manipulate the same file by using the header file fstream.',
      'اگر فائل صرف پڑھنے کے مقصد کے لیے استعمال ہو تو ہیڈر فائل ifstream (ان پٹ فائل اسٹریم) شامل کرنا ضروری ہے۔ اسی طرح اگر کوئی کسی فائل میں لکھنا چاہے تو ہیڈر فائل ofstream (آؤٹ پٹ فائل اسٹریم) درکار ہے۔ ہیڈر فائل fstream کے ذریعے ایک ہی فائل کو پڑھا، لکھا اور تبدیل کیا جا سکتا ہے۔',
      'که دوتنه یوازې د لوستلو لپاره وکارول شي، د ifstream (د ننوتنې دوتنې بهیر) سرپاڼه دوتنه شاملول اړین دي. همداراز که څوک غواړي په کومه دوتنه کې ولیکي، د ofstream (د وتنې دوتنې بهیر) سرپاڼه دوتنې ته اړتیا ده. د fstream سرپاڼه دوتنې په کارولو یوه دوتنه لوستل، لیکل او بدلول کېدای شي.')
    P('Consider the following example of input and output using the standard streams:', 'معیاری اسٹریمز کے ذریعے ان پٹ اور آؤٹ پٹ کی درج ذیل مثال پر غور کریں:', 'د معیاري بهیرونو په مرسته د ننوتنې او وتنې لاندې بېلګې ته پام وکړئ:')
    code(t, '''// input/output stream example
#include <conio.h>
#include <iostream.h>
#include <process.h>
int main()
{
float height;
cout<< "Enter your height: " <<endl; // output stream
cin>> height; // input stream
if (height <= 0)
{
cerr<< "You entered an invalid height!" <<endl;
exit(1);
}
cout<< "Your height is " << height << " feet" <<endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Enter your height:5.8
Your height is 5.8 feet''')
    t.h('9.1.5 Use of the Streams', '9.1.5 اسٹریمز کا استعمال', '۹.۱.۵ د بهیرونو کارونه')
    P('The data can be read from and written to files with the help of single character stream and string stream.', 'سنگل کریکٹر اسٹریم اور اسٹرنگ اسٹریم کی مدد سے فائلز سے ڈیٹا پڑھا اور ان میں لکھا جا سکتا ہے۔', 'د یو توري بهیر او د تار بهیر په مرسته له دوتنو ډېټا لوستل او پکې لیکل کېدای شي.')
    t.h('a. Single character stream', 'a. سنگل کریکٹر اسٹریم', 'a. د یو توري بهیر')
    P('Using single character stream, the data can be read from and written to files character by character.', 'سنگل کریکٹر اسٹریم کے ذریعے فائلز سے ڈیٹا حرف بہ حرف پڑھا اور لکھا جا سکتا ہے۔', 'د یو توري بهیر په مرسته له دوتنو ډېټا توری په توری لوستل او لیکل کېدای شي.')
    t.h('i. Reading files character by character', 'i. فائلز کو حرف بہ حرف پڑھنا', 'i. دوتنې توری په توری لوستل')
    P('The function get() is used to read data character by character from files.', 'فنکشن get() فائلز سے ڈیٹا حرف بہ حرف پڑھنے کے لیے استعمال ہوتا ہے۔', 'get() فنکشن له دوتنو د ډېټا د توري په توري لوستلو لپاره کارېږي.')
    P('Consider the following program that reads the data one character at a time from the file “characters file.txt”,shown in figure 9.7, and display them on the screen.', 'درج ذیل پروگرام پر غور کریں جو شکل 9.7 میں دکھائی گئی فائل ’’characters file.txt‘‘ سے ایک وقت میں ایک حرف پڑھ کر اسکرین پر دکھاتا ہے۔', 'لاندې پروګرام ته پام وکړئ چې په ۹.۷ شکل کې ښودل شوې "characters file.txt" دوتنې څخه په یوه وخت کې یو توری لولي او پر پرده یې ښيي.')
    BOOK.save(141, [(9, rec(t, 6, 141, [270, 271], 'The character-stream (read) program that begins at the foot of p.271 is given whole with PDF142.'))],
              issues=[{'id': 'cs12-pdf141', 'unit': 9, 'printedPage': 271,
                       'description': 'p.271 refers to the file “characters file.txt” (the program opens charactersfile.txt) and to Figure 9.7, though no Figure 9.6 is printed in the unit; p.270 “consumer, such as” printed “consumer; such as”. Retained as printed.'}])


def p142():
    t = Builder()
    P = t.p
    code(t, '''//character stream (read) program
#include <conio.h>
#include <iostream.h>
#include <fstream.h>
int main()
{
char ch;
ifstream reads("c:\\\\charactersfile.txt");
while(!reads.eof())
{
read.get(ch);
cout<<ch<<endl;
}
read.close();
getch();
return 0;
}''')
    P(*OUT)
    code(t, '\n'.join(list('read') + [''] + list('the') + [''] + list('file') + [''] + list('please.')))
    win(t, 'cs12-fig-9-7', 'charactersfile - Notepad', ['read the file please.'], ('Figure 9.7: Input File to be Read Character by Character', 'شکل 9.7: حرف بہ حرف پڑھی جانے والی ان پٹ فائل', '۹.۷ شکل: توری په توری د لوستلو وړ د ننوتنې دوتنه'))
    t.h('ii. Writing files character by character', 'ii. فائلز میں حرف بہ حرف لکھنا', 'ii. دوتنو ته توری په توری لیکل')
    P('Similarly, using single character stream, data can be written to files character by character by using the function put (). Consider the following program that writes data character by character to an empty file “characterswrite.txt”.', 'اسی طرح سنگل کریکٹر اسٹریم کے ذریعے فنکشن put () سے فائلز میں ڈیٹا حرف بہ حرف لکھا جا سکتا ہے۔ درج ذیل پروگرام پر غور کریں جو خالی فائل ’’characterswrite.txt‘‘ میں ڈیٹا حرف بہ حرف لکھتا ہے۔', 'همداراز د یو توري بهیر په مرسته د put () فنکشن په کارولو دوتنو ته ډېټا توری په توری لیکل کېدای شي. لاندې پروګرام ته پام وکړئ چې "characterswrite.txt" تشې دوتنې ته ډېټا توری په توری لیکي.')
    code(t, '''//character stream ( write) program
#include <conio.h>
#include <iostream.h>
#include <fstream.h>
int main()
{
char ch;
ofstream writes("d:\\\\characterswrite.txt");
for (int i=0; i<=20; ++i)
{
cin>>ch;
cout<<writes.put(ch);
}
writes.close();
getch();
return 0;
}''')
    BOOK.save(142, [(9, rec(t, 7, 142, [271, 272, 273], 'The read program begins at the foot of p.271 and is given whole here. The vertical one-character-per-line output is kept as printed. Figure 9.7 (a Notepad window) is redrawn as a coded mock-up.'))],
              issues=[{'id': 'cs12-pdf142', 'unit': 9, 'printedPage': 272,
                       'description': 'The read program declares the stream as “reads” but calls read.get(ch) and read.close(). Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 134
    {134: p134, 135: p135, 136: p136, 137: p137, 138: p138, 139: p139, 140: p140, 141: p141, 142: p142}[n]()
