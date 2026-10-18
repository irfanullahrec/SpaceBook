"""Computer Science XII PDF59–60: pp.106–108 Unit 3 exercise Q1–Q10 (unit 3 complete); p.109 Unit 4 opener.
Run: python class12_cs_page059.py N (59 or 60)."""
import sys
from class12_cs_common import BOOK, Builder, code

N = ('None of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')


def p59():
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. In C/C++ language, a hexadecimal number is represented by writing ________ symbol.', 'i. C/C++ زبان میں ہیکسا ڈیسیمل عدد ________ علامت لکھ کر ظاہر کیا جاتا ہے۔', 'i. په C/C++ ژبه کې شپاړسیز عدد د ________ نښې په لیکلو ښودل کېږي.'),
     ('ii. (?) is the ________ operator used in C++.', 'ii. (?) C++ میں استعمال ہونے والا ________ آپریٹر ہے۔', 'ii. (?) په C++ کې کارېدونکی ________ چلونکی دی.'),
     ('iii. Output of the logical and relational operators is ________ .', 'iii. منطقی اور ریلیشنل آپریٹرز کا آؤٹ پٹ ________ ہوتا ہے۔', 'iii. د منطقي او اړیکه‌ییزو چلونکو وتنه ________ ده.'),
     ('iv. Assigning values to a variable during declaration time is called ________ .', 'iv. اعلان کے وقت ویری ایبل کو قدر دینا ________ کہلاتا ہے۔', 'iv. د اعلان پر وخت متغیر ته ارزښت ورکول ________ بلل کېږي.'),
     ('v. Each C++ program has ________ function from where the execution of the program starts.', 'v. ہر C++ پروگرام میں ________ فنکشن ہوتا ہے جہاں سے پروگرام کا عمل شروع ہوتا ہے۔', 'v. هر C++ پروګرام ________ فنکشن لري چې د پروګرام اجرا له هغه پیلېږي.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    e.mcq('i.', ('What does the given expression evaluate to? E=6 + 5 * 4 % 3', 'دیا گیا ایکسپریشن کس قدر کے برابر ہوگا؟ E=6 + 5 * 4 % 3', 'ورکړل شوې افاده څه ارزښت ورکوي؟ E=6 + 5 * 4 % 3'), ['1', '8', '11', N], per_line=1)
    e.mcq('ii.', ('(true && true) || false', '(true && true) || false', '(true && true) || false'),
          ['true', 'false', ('both a and b', 'a اور b دونوں', 'a او b دواړه'), ('none of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')], per_line=1)
    e.mcq('iii.', ('Expression C=i++ causes', 'ایکسپریشن C=i++ کا نتیجہ', 'افاده C=i++ لامل کېږي'),
          [('Value of i assigned to C and then i incremented by 1', 'i کی قدر C کو تفویض ہوتی ہے اور پھر i میں 1 کا اضافہ ہوتا ہے', 'د i ارزښت C ته سپارل کېږي او بیا i په 1 زیاتېږي'),
           ('i to be incremented by 1 and then value of i assigned to C', 'i میں 1 کا اضافہ اور پھر i کی قدر C کو تفویض', 'i په 1 زیاتېږي او بیا د i ارزښت C ته سپارل کېږي'),
           ('Value of i assigned to C', 'i کی قدر C کو تفویض', 'د i ارزښت C ته سپارل'), ('i to be incremented by 1', 'i میں 1 کا اضافہ', 'i په 1 زیاتېدل')], per_line=1)
    e.mcq('iv.', ('Which of the following languages is a subset of C++ language?', 'درج ذیل میں سے کون سی زبان C++ زبان کا ذیلی مجموعہ ہے؟', 'له لاندې ژبو څخه کومه د C++ ژبې فرعي ټولګه ده؟'),
          [('C language', 'C زبان', 'C ژبه'), ('Java language', 'جاوا زبان', 'Java ژبه'), ('B language', 'B زبان', 'B ژبه'), ('C# language', 'C# زبان', 'C# ژبه')], per_line=1)
    e.mcq('v.', ("In C++ language char ch='3' represents:", "C++ زبان میں char ch='3' ظاہر کرتا ہے:", "په C++ ژبه کې char ch='3' ښيي:"),
          [('A digit', 'ایک عدد', 'یو رقم'), ('An integer constant', 'ایک انٹیجر کانسٹنٹ', 'یو صحیح عدد ثابت'), ('A character constant', 'ایک حرفی کانسٹنٹ', 'د توري ثابت'), ('A word', 'ایک لفظ', 'یوه کلمه')], per_line=1)
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. Definition for the C++ object cout is stored in header file conio.h.', 'i. C++ آبجیکٹ cout کی تعریف ہیڈر فائل conio.h میں محفوظ ہے۔', 'i. د C++ شي cout تعریف په conio.h سرلیک فایل کې ساتل شوی.'),
     ("ii. In C++ a statement ends with ':' symbol.", "ii. C++ میں بیان ':' علامت پر ختم ہوتا ہے۔", "ii. په C++ کې بیان د ':' نښې سره پای ته رسېږي."),
     ('iii. int 20sum is the correct declaration of the variable 20sum.', 'iii. int 20sum ویری ایبل 20sum کا درست اعلان ہے۔', 'iii. int 20sum د 20sum متغیر سم اعلان دی.'),
     ('iv. In C++ the statement a=a+20 is the same as a+=20.', 'iv. C++ میں بیان a=a+20، a+=20 کے برابر ہے۔', 'iv. په C++ کې بیان a=a+20 له a+=20 سره یو شان دی.'),
     ('v. Size of short int data type is 4 bytes.', 'v. short int ڈیٹا ٹائپ کا سائز 4 بائٹس ہے۔', 'v. د short int ډېټا ډول اندازه ۴ بایټه ده.')])
    e.h('Q.4 Evaluate the following:', 'سوال 4: درج ذیل کی قدر نکالیں:', 'پوښتنه ۴: لاندې ارزونه وکړئ:')
    code(e, '''1) (false && true) || true
2) (false && true) || false || true
3) (5 > 6 || 4 > 3) && (7 > 8)
4) !(7 > 6 || 3 > 4)''')
    e.p('Q.5 Pick those variables from the following list which are improperly declared and named. Also, describe the reason of its invalidity?',
        'سوال 5: درج ذیل فہرست سے وہ ویری ایبلز منتخب کریں جن کا اعلان اور نام غلط ہے۔ نیز ان کے غلط ہونے کی وجہ بیان کریں؟',
        'پوښتنه ۵: له لاندې لېست هغه متغیرونه وټاکئ چې ناسم اعلان او نومول شوي. همداراز د ناسموالي لامل یې بیان کړئ؟')
    code(e, '''1) int sum;
2) int cats=5, dogs=5;
3) int my variable name;
4) int void = 5;
5) int nAngle;
6) int 3some;
7) int meters_of_pipe;
8) int length, width=5;''')
    for q, en, ur, ps in [
        ('Q.6', 'Write a C++ program to get six subjects marks of a student and then calculate its total, average and percentage and display them on the screen.', 'ایک طالب علم کے چھ مضامین کے نمبر حاصل کر کے ان کا مجموعہ، اوسط اور فیصد نکالنے اور اسکرین پر دکھانے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د یوه زده‌کوونکي د شپږو مضامینو نمرې واخلي او ټول، اوسط او سلنه یې وشمېري او پر پرده یې وښيي.'),
        ('Q.7', 'Write a C++ program to find out maximum value out of three integers using conditional operator.', 'شرطیہ آپریٹر کے ذریعے تین صحیح اعداد میں سے سب سے بڑی قدر معلوم کرنے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د شرطي چلونکي په مرسته له دریو صحیح عددونو تر ټولو لوی ارزښت پیدا کړي.'),
        ('Q.8', 'Write a C++ program to find out the roots of a quadratic equation.', 'دو درجی مساوات کے جذر معلوم کرنے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د دوه-درجه‌ییزې معادلې ریښې پیدا کړي.'),
        ('Q.9', 'Write a C++ program to find out the area of a rectangle and display the result on the screen.', 'مستطیل کا رقبہ معلوم کرنے اور نتیجہ اسکرین پر دکھانے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د مستطیل مساحت پیدا کړي او پایله پر پرده وښيي.'),
        ('Q.10', 'Write a C++ program to get the age of a student from the user at run time and display it on the screen.', 'چلنے کے وقت صارف سے طالب علم کی عمر حاصل کرنے اور اسے اسکرین پر دکھانے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د اجرا پر وخت له کاروونکي د زده‌کوونکي عمر واخلي او پر پرده یې وښيي.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    ex = BOOK.record(e, 'cs12-u3-exercise', 'Unit 3 exercise', 'یونٹ 3: مشق', '۳ څپرکی: تمرین', 59, [106, 107, 108])
    ex['sourceNote'] = 'The Q5 list continues on p.108 (PDF60) together with Q6–Q10; the whole exercise is recorded here.'
    BOOK.save(59, [(3, ex)], issues=[{'id': 'cs12-pdf059', 'unit': 3, 'printedPage': 106,
               'description': 'Q2(iii) options b and d print “to be incremented”; Q5 “the reason of its invalidity”. Retained as printed.'}])


def p60():
    t = Builder()
    t.p('Unit 4', 'یونٹ 4', '۴ څپرکی')
    t.h('CONTROL STRUCTURE', 'کنٹرول اسٹرکچر', 'کنټرولي جوړښت')
    t.h('After the completion of Unit-4, Students will be able to:', 'یونٹ 4 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۴ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    t.group('list', [('Explain the use of the following decision statements:', 'درج ذیل فیصلہ کن بیانات کا استعمال بیان کر سکیں:', 'د لاندې پرېکړه‌ییزو بیانونو کارونه تشریح کړي:')])
    t.group('list', [('if statement', 'if بیان', 'if بیان'), ('if-else statement', 'if-else بیان', 'if-else بیان'), ('switch statement', 'switch بیان', 'switch بیان')])
    t.group('list', [('Know the concept of nested if statement', 'نیسٹڈ if بیان کا تصور جان سکیں', 'د ځالې if بیان مفهوم وپېژني'),
                     ('Use break statement and exit function', 'break بیان اور exit فنکشن استعمال کر سکیں', 'break بیان او exit فنکشن وکاروي'),
                     ('Explain the use of the following looping structure:', 'درج ذیل لوپنگ ساخت کا استعمال بیان کر سکیں:', 'د لاندې حلقوي جوړښت کارونه تشریح کړي:')])
    t.group('list', [('for loop', 'for لوپ', 'for حلقه'), ('while loop', 'while لوپ', 'while حلقه'), ('do-while loop', 'do-while لوپ', 'do-while حلقه')])
    t.group('list', [('Use continue statement', 'continue بیان استعمال کر سکیں', 'continue بیان وکاروي'), ('Know the concept of nested loop', 'نیسٹڈ لوپ کا تصور جان سکیں', 'د ځالې حلقې مفهوم وپېژني')])
    UT = ('Control Structure', 'کنٹرول اسٹرکچر', 'کنټرولي جوړښت')
    rec = BOOK.record(t, 'cs12-u4-outcomes', 'Unit 4: learning outcomes', 'یونٹ 4: حاصلاتِ تعلم', '۴ څپرکی: د زده‌کړې پایلې', 60, [109], unit_title=UT)
    rec['sourceNote'] = 'The left page of PDF60 (p.108, end of the Unit 3 exercise) is recorded with PDF59.'
    BOOK.save(60, [(4, rec)], complete_units=[3])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 59
    p59() if n == 59 else p60()
