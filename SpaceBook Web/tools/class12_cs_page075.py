"""Computer Science XII PDF75–78: pp.138–139 Unit 4 summary + exercise Q1; pp.140–143 Q2 i–ix, Q3, Q4–Q7; p.144 Q8–Q10 (unit 4 complete); p.145 Unit 5 opener.
Run: python class12_cs_page075.py N (75–78)."""
import sys
from class12_cs_common import BOOK, Builder, code

N = ('None of above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')


def p75():
    s = Builder()
    s.h('Summary', 'خلاصہ', 'لنډیز')
    s.group('list', [
     ('A decision statement causes the control to pass to different parts of the program based on the value of an expression. Decision can be made in C++ in several ways.', 'فیصلہ کن بیان کسی ایکسپریشن کی قدر کی بنیاد پر کنٹرول کو پروگرام کے مختلف حصوں تک منتقل کرتا ہے۔ C++ میں فیصلہ کئی طریقوں سے کیا جا سکتا ہے۔', 'پرېکړه‌ییز بیان د یوې افادې د ارزښت پر بنسټ کنټرول د پروګرام بېلابېلو برخو ته لېږدوي. په C++ کې پرېکړه په څو لارو کېدای شي.'),
     ('The most important decision statements in C++ are if, if-else and switch Statements.', 'C++ میں سب سے اہم فیصلہ کن بیانات if، if-else اور switch ہیں۔', 'په C++ کې تر ټولو مهم پرېکړه‌ییز بیانونه if، if-else او switch دي.'),
     ('if statement uses a condition and based on the values of the condition, the body of if is executed. If the condition is true then body is executed otherwise nothing is executed.', 'if بیان ایک شرط استعمال کرتا ہے اور شرط کی قدر کی بنیاد پر if کا جسم چلتا ہے۔ اگر شرط درست ہو تو جسم چلتا ہے ورنہ کچھ نہیں چلتا۔', 'if بیان یو شرط کاروي او د شرط د ارزښت پر بنسټ د if بدنه اجرا کېږي. که شرط true وي، بدنه اجرا کېږي، که نه هېڅ نه اجرا کېږي.'),
     ('if -else statement selects either the body of if or else based on the result of the condition. If condition is true then body of if is executed and if false then body of else is executed.', 'if-else بیان شرط کے نتیجے کی بنیاد پر if یا else کا جسم منتخب کرتا ہے۔ اگر شرط درست ہو تو if کا جسم اور غلط ہو تو else کا جسم چلتا ہے۔', 'if-else بیان د شرط د پایلې پر بنسټ د if یا else بدنه ټاکي. که شرط true وي د if بدنه او که false وي د else بدنه اجرا کېږي.'),
     ('if-else statement can be nested within each other.', 'if-else بیانات ایک دوسرے کے اندر نیسٹ کیے جا سکتے ہیں۔', 'if-else بیانونه یو د بل دننه ځالې کېدای شي.'),
     ('switch statement is used to select from a number of choices and is a better alternative of nested if-else statement.', 'switch بیان کئی انتخابات میں سے ایک منتخب کرنے کے لیے استعمال ہوتا ہے اور نیسٹڈ if-else بیان کا بہتر متبادل ہے۔', 'switch بیان له څو انتخابونو د ټاکلو لپاره کارول کېږي او د ځالې if-else بیان ښه بدیل دی.'),
     ('Loops are the iterative statements used to repeat a statement or group of statements until a terminating condition is true.', 'لوپس تکراری بیانات ہیں جو کسی بیان یا بیانات کے گروپ کو اختتامی شرط درست ہونے تک دہرانے کے لیے استعمال ہوتے ہیں۔', 'حلقې تکراري بیانونه دي چې د یوه بیان یا د بیانونو د ډلې د تکرار لپاره تر هغه کارول کېږي چې د پای شرط true شي.'),
     ('for loop is the most commonly used iterative statement in C++ which is used in the situation when one knows the number of iterations in advance.', 'for لوپ C++ میں سب سے زیادہ استعمال ہونے والا تکراری بیان ہے جو اس صورت میں استعمال ہوتا ہے جب تکرار کی تعداد پہلے سے معلوم ہو۔', 'for حلقه په C++ کې تر ټولو ډېر کارېدونکی تکراري بیان دی چې هغه وخت کارېږي چې د تکرارونو شمېر مخکې له مخکې معلوم وي.'),
     ('while loop is similar to if-else structure in which the condition is checked first and then the body is executed.', 'while لوپ if-else ساخت جیسا ہے جس میں پہلے شرط جانچی جاتی ہے اور پھر جسم چلتا ہے۔', 'while حلقه د if-else جوړښت ته ورته ده چې پکې لومړی شرط کتل کېږي او بیا بدنه اجرا کېږي.'),
     ('In do while structure the body of the loop is executed at least once even if the condition is false.', 'do while ساخت میں لوپ کا جسم کم از کم ایک بار چلتا ہے چاہے شرط غلط ہو۔', 'په do while جوړښت کې د حلقې بدنه لږ تر لږه یو ځل اجرا کېږي حتی که شرط false وي.'),
     ('Sometimes, the programmers need to shift the control and make jump from one statement of the program to another statement or part. Commonly used jump statements of C++ language are: break and continue.', 'بعض اوقات پروگرامرز کو کنٹرول منتقل کر کے پروگرام کے ایک بیان سے دوسرے بیان یا حصے پر جانا ہوتا ہے۔ C++ زبان کے عام استعمال ہونے والے جمپ بیانات break اور continue ہیں۔', 'کله کله پروګرام جوړوونکي اړتیا لري چې کنټرول ولېږدوي او د پروګرام له یوه بیان بل بیان یا برخې ته ټوپ ووهي. د C++ ژبې عام کارېدونکي د ټوپ بیانونه break او continue دي.')])
    sm = BOOK.record(s, 'cs12-u4-summary', 'Unit 4 summary', 'یونٹ 4: خلاصہ', '۴ څپرکی: لنډیز', 75, [138, 139])
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. An if statement can include multiple statements provided that they are ________ .', 'i. if بیان میں متعدد بیانات شامل ہو سکتے ہیں بشرطیکہ وہ ________ ہوں۔', 'i. if بیان کولی شي ډېر بیانونه ولري په دې شرط چې ________ وي.'),
     ('ii. The switch statement controls program flow by executing a specific set of statements, depending on ________ .', 'ii. switch بیان ________ کی بنیاد پر بیانات کا ایک مخصوص مجموعہ چلا کر پروگرام کے بہاؤ کو کنٹرول کرتا ہے۔', 'ii. switch بیان د ________ پر بنسټ د بیانونو یوه ټاکلې ټولګه اجرا کوي او د پروګرام بهیر کنټرولوي.'),
     ('iii. When the value returned by a switch statement expression does not match a case label, the ________ statements within the label execute.', 'iii. جب switch بیان کے ایکسپریشن کی قدر کسی case لیبل سے نہ ملے تو لیبل کے اندر ________ بیانات چلتے ہیں۔', 'iii. کله چې د switch بیان د افادې بېرته ورکړل شوی ارزښت له کوم case لیبل سره سمون ونه لري، د لیبل دننه ________ بیانونه اجرا کېږي.'),
     ('iv. You can exit a switch statement using a(n) ________ statement.', 'iv. آپ ________ بیان کے ذریعے switch بیان سے نکل سکتے ہیں۔', 'iv. تاسو د ________ بیان په مرسته له switch بیان وتلی شئ.'),
     ('v. Each repetition of a looping statement is called a ________ .', 'v. لوپنگ بیان کی ہر تکرار ________ کہلاتی ہے۔', 'v. د حلقوي بیان هر تکرار ________ بلل کېږي.')])
    ex = BOOK.record(e, 'cs12-u4-exercise-1', 'Unit 4 exercise (1)', 'یونٹ 4: مشق (۱)', '۴ څپرکی: تمرین (۱)', 75, [139])
    BOOK.save(75, [(4, sm), (4, ex)])


def p76():
    e = Builder()
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    e.p('i. Find out the error in following block of code.', 'i. کوڈ کے درج ذیل بلاک میں غلطی تلاش کریں۔', 'i. د کوډ په لاندې بلاک کې تېروتنه ومومئ.')
    code(e, '''if (x = 100)
cout << "x is 100";''')
    e.group('lines', [('(a) 100 should be enclosed in quotations', '(a) 100 کو واوین میں بند ہونا چاہیے', '(a) 100 باید په نقل‌قولونو کې وتړل شي'),
                      ('(b) There is no semicolon at the end of first line', '(b) پہلی لائن کے آخر میں سیمی کولن نہیں ہے', '(b) د لومړۍ کرښې په پای کې سیمي‌کولن نشته'),
                      ('(c) Equals to operator mistake', '(c) برابری کے آپریٹر کی غلطی', '(c) د برابرۍ چلونکي تېروتنه'),
                      ('(d) Variable x should not be inside quotation', '(d) ویری ایبل x واوین کے اندر نہیں ہونا چاہیے', '(d) متغیر x باید د نقل‌قول دننه نه وي')])
    e.mcq('ii.', ('Looping in a program means', 'پروگرام میں لوپنگ کا مطلب ہے', 'په پروګرام کې حلقه کول معنا لري'),
          [('Jumping to the specified branch of program', 'پروگرام کی مخصوص شاخ پر جانا', 'د پروګرام ټاکلې څانګې ته ټوپ'), ('Repeat the specified lines of code', 'کوڈ کی مخصوص لائنیں دہرانا', 'د کوډ ټاکلې کرښې تکرارول'),
           ('Both of above', 'دونوں', 'دواړه پورته'), N], per_line=1)
    e.mcq('iii.', ('Which of the following is not a looping statement in C++?', 'درج ذیل میں سے کون سا C++ میں لوپنگ بیان نہیں ہے؟', 'له لاندې څخه کوم یو په C++ کې حلقوي بیان نه دی؟'), ['while', 'until', 'do', 'for'], per_line=1)
    e.mcq('iv.', ('Which of the following is not a jump statement in C++?', 'درج ذیل میں سے کون سا C++ میں جمپ بیان نہیں ہے؟', 'له لاندې څخه کوم یو په C++ کې د ټوپ بیان نه دی؟'), ['break', 'goto', 'exit', 'switch'], per_line=1)
    e.mcq('v.', ('Which of the following is selection statement in C++?', 'درج ذیل میں سے کون سا C++ میں انتخابی بیان ہے؟', 'له لاندې څخه کوم یو په C++ کې د ټاکنې بیان دی؟'), ['break', 'goto', 'exit', 'switch'], per_line=1)
    e.mcq('vi.', ('The continue statement', 'continue بیان', 'continue بیان'),
          [('resumes the program if it is hanged', 'اگر پروگرام رک جائے تو اسے دوبارہ شروع کرتا ہے', 'که پروګرام ودرېږي، بیا یې پیلوي'), ('resumes the program if break was applied', 'اگر break لگا ہو تو پروگرام دوبارہ شروع کرتا ہے', 'که break کارول شوی وي، پروګرام بیا پیلوي'),
           ('skips the rest of the loop in current iteration', 'موجودہ تکرار میں لوپ کا باقی حصہ چھوڑ دیتا ہے', 'په اوسني تکرار کې د حلقې پاتې برخه پرېږدي'), ('all of above', 'مندرجہ بالا سب', 'پورته ټول')], per_line=1)
    e.p('vii. Consider the following two pieces of codes and choose the best answer', 'vii. کوڈ کے درج ذیل دو ٹکڑوں پر غور کریں اور بہترین جواب منتخب کریں', 'vii. د کوډ لاندې دوو ټوټو ته پام وکړئ او غوره ځواب وټاکئ')
    code(e, '''1.
switch (x) {
case 1:
cout <<"x is 1";
break;
case 2:
cout <<"x is 2";
break;
default:
cout <<"value of x unknown";
}
2.
if (x==1){
cout <<"x is 1";
}
else if (x==2){
cout << "x is 2";
}
else{
cout <<"value of x unknown";
}''')
    e.group('lines', [('(a) Both of the above code fragments have the same behaviour', '(a) اوپر کے دونوں کوڈ ٹکڑوں کا رویہ یکساں ہے', '(a) پورته د کوډ دواړه ټوټې یو شان چلند لري'),
                      ('(b) Both of the above code fragments produce different effects', '(b) اوپر کے دونوں کوڈ ٹکڑے مختلف اثرات پیدا کرتے ہیں', '(b) پورته د کوډ دواړه ټوټې بېل اغېزونه پیدا کوي'),
                      ('(c) The first code produces more results than second', '(c) پہلا کوڈ دوسرے سے زیادہ نتائج دیتا ہے', '(c) لومړی کوډ تر دویم ډېرې پایلې ورکوي'),
                      ('(d) The second code produces more results than first', '(d) دوسرا کوڈ پہلے سے زیادہ نتائج دیتا ہے', '(d) دویم کوډ تر لومړي ډېرې پایلې ورکوي')])
    e.p('viii. Observe the following block of code and determine what happens when x=2?', 'viii. کوڈ کے درج ذیل بلاک کا مشاہدہ کریں اور بتائیں کہ x=2 ہونے پر کیا ہوتا ہے؟', 'viii. د کوډ لاندې بلاک ته وګورئ او وټاکئ چې کله x=2 وي څه کېږي؟')
    code(e, '''switch (x)
{
case 1:
case 2:
case 3:
cout<< "x is between 1 .. 3";
break;
default:
cout<<"x is not within the range, so need to say Thank You!";
}''')
    e.group('lines', [('(a) Program jumps to the end of switch statement', '(a) پروگرام switch بیان کے آخر پر چلا جاتا ہے', '(a) پروګرام د switch بیان پای ته ټوپ وهي'),
                      ('(b) The code after default will run since there is no task for x=2', '(b) default کے بعد والا کوڈ چلے گا کیونکہ x=2 کے لیے کوئی کام نہیں', '(b) د default وروسته کوډ به اجرا شي ځکه د x=2 لپاره کار نشته'),
                      ('(c) Will display x is between 1 ... 3', '(c) x is between 1 ... 3 دکھائے گا', '(c) x is between 1 ... 3 به ښيي'), ('(d) None of above', '(d) ان میں سے کوئی نہیں', '(d) له پورته هېڅ یو')])
    e.mcq('ix.', ('Which of the following is false for switch statement in C++?', 'C++ میں switch بیان کے لیے درج ذیل میں سے کون سا غلط ہے؟', 'په C++ کې د switch بیان لپاره له لاندې څخه کوم یو ناسم دی؟'),
          [('It uses labels instead of blocks', 'یہ بلاکس کے بجائے لیبلز استعمال کرتا ہے', 'د بلاکونو پر ځای لیبلونه کاروي'), ('we need to put break statement at the end of the group of statement', 'ہمیں بیانات کے گروپ کے آخر میں break بیان رکھنا ہوتا ہے', 'موږ باید د بیانونو د ډلې په پای کې break بیان کېږدو'),
           ('we can put range for case such as case 1..3', 'ہم case کے لیے حد رکھ سکتے ہیں جیسے case 1..3', 'موږ کولی شو د case لپاره حد کېږدو لکه case 1..3'), N], per_line=1)
    ex = BOOK.record(e, 'cs12-u4-exercise-2', 'Unit 4 exercise (2)', 'یونٹ 4: مشق (۲)', '۴ څپرکی: تمرین (۲)', 76, [139, 140, 141, 142])
    ex['sourceNote'] = 'Q2 runs from the foot of p.139 to p.142 (PDF75–77) and is recorded here whole. Code options are kept in English in all language views.'
    BOOK.save(76, [(4, ex)])


def p77():
    e = Builder()
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. Decision-making structures cannot be nested.', 'i. فیصلہ سازی کی ساختیں نیسٹ نہیں کی جا سکتیں۔', 'i. پرېکړه‌ییز جوړښتونه ځالې کېدای نه شي.'),
     ('ii. Body of do while loop is executed at least once if the condition is false.', 'ii. شرط غلط ہو تو بھی do while لوپ کا جسم کم از کم ایک بار چلتا ہے۔', 'ii. که شرط false وي، د do while حلقې بدنه لږ تر لږه یو ځل اجرا کېږي.'),
     ('iii. When for statement begins executing, at the same time the initialization expression is also executed?', 'iii. جب for بیان چلنا شروع ہوتا ہے تو اسی وقت ابتدائی قدر کا ایکسپریشن بھی چلتا ہے؟', 'iii. کله چې for بیان اجرا پیل کړي، په همغه وخت د لومړني ارزښت افاده هم اجرا کېږي؟'),
     ('iv. switch statement is a better alternative of nested if-else structure.', 'iv. switch بیان نیسٹڈ if-else ساخت کا بہتر متبادل ہے۔', 'iv. switch بیان د ځالې if-else جوړښت ښه بدیل دی.'),
     ('v. Syntax of if-else statement is:', 'v. if-else بیان کا طریقۂ تحریر یہ ہے:', 'v. د if-else بیان بڼه دا ده:')])
    code(e, '''else {
}
if (condition) {
}''')
    for q, en, ur, ps in [
        ('Q.4', 'Write a C++ program that takes two integers and a chararacter representing one of the following mathematical operations: +, -, /, or *. Use a switch statement to perform the appropriate mathematical operation on the integers, and display the result. If an invalid operator is entered then “Error” message should be displayed and the program should exit (use the exit() function).', 'ایک C++ پروگرام لکھیں جو دو صحیح اعداد اور درج ذیل ریاضی کے اعمال میں سے کسی ایک کو ظاہر کرنے والا حرف لے: +، -، / یا *۔ صحیح اعداد پر مناسب عمل کرنے کے لیے switch بیان استعمال کریں اور نتیجہ دکھائیں۔ اگر غلط آپریٹر داخل کیا جائے تو ’’Error‘‘ پیغام دکھایا جائے اور پروگرام بند ہو جائے (exit() فنکشن استعمال کریں)۔', 'یو C++ پروګرام ولیکئ چې دوه صحیح عددونه او یو توری واخلي چې له لاندې ریاضي عملیو یوه ښيي: +، -، / یا *. پر صحیح عددونو د مناسبې عملیې لپاره switch بیان وکاروئ او پایله وښایاست. که ناسم چلونکی ولیکل شي، "Error" پیغام دې وښودل شي او پروګرام دې ووځي (exit() فنکشن وکاروئ).'),
        ('Q.5', 'Write a program using for loop that prints even numbers from 0 to 20.', 'for لوپ کے ذریعے 0 سے 20 تک کے جفت اعداد پرنٹ کرنے کا پروگرام لکھیں۔', 'د for حلقې په مرسته له 0 تر 20 جفت عددونه چاپولو پروګرام ولیکئ.'),
        ('Q.6', 'Write a program using while loop that takes an integer for a variable nValue, and returns the sum of all the numbers from 1 to nValue. Hint: For example, nValue=5 should return 15, which is 1 + 2 + 3 + 4 + 5.', 'while لوپ کے ذریعے ایسا پروگرام لکھیں جو ویری ایبل nValue کے لیے صحیح عدد لے اور 1 سے nValue تک کے تمام اعداد کا مجموعہ واپس کرے۔ اشارہ: مثلاً nValue=5 پر 15 واپس آنا چاہیے، یعنی 1 + 2 + 3 + 4 + 5۔', 'د while حلقې په مرسته پروګرام ولیکئ چې د nValue متغیر لپاره صحیح عدد واخلي او له 1 تر nValue د ټولو عددونو مجموعه ورکړي. اشاره: د بېلګې په توګه nValue=5 باید 15 ورکړي، یعنې 1 + 2 + 3 + 4 + 5.'),
        ('Q.7', 'What is wrong with the following for loop?', 'درج ذیل for لوپ میں کیا غلطی ہے؟', 'په لاندې for حلقه کې څه ستونزه ده؟')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    code(e, '''// Print all numbers from 9 to 0
for (unsigned int nCount = 9; nCount >= 0; nCount--)
cout << nCount << " ";''')
    ex = BOOK.record(e, 'cs12-u4-exercise-3', 'Unit 4 exercise (3)', 'یونٹ 4: مشق (۳)', '۴ څپرکی: تمرین (۳)', 77, [142, 143])
    ex['sourceNote'] = 'The top of p.142 (Q2 vii options–ix) is recorded with PDF76.'
    BOOK.save(77, [(4, ex)], issues=[{'id': 'cs12-pdf077', 'unit': 4, 'printedPage': 143,
               'description': 'Q4 prints “chararacter”; Q3(iii) ends with “?”; Q3(v) gives the if-else syntax in reversed order (else before if) as a TRUE/FALSE item. Retained as printed. Owner handwritten solution for Q6 in the margin of p.143 excluded.'}])


def p78():
    e = Builder()
    for q, en, ur, ps in [
        ('Q.8', 'Write a C++ program to read the address of a person and exit when the user enters dot (.) from the keyboard.', 'کسی شخص کا پتہ پڑھنے اور صارف کے کی بورڈ سے نقطہ (.) داخل کرنے پر بند ہونے والا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د یوه کس پته ولولي او کله چې کاروونکی له کیبورډ ټکی (.) ولیکي، ووځي.'),
        ('Q.9', 'Write a C++ program to find out the area of a triangle and if any side is zero then display the message “There is no triangle”.', 'مثلث کا رقبہ معلوم کرنے کا C++ پروگرام لکھیں اور اگر کوئی ضلع صفر ہو تو پیغام ’’There is no triangle‘‘ دکھائیں۔', 'یو C++ پروګرام ولیکئ چې د مثلث مساحت پیدا کړي او که کومه ضلع صفر وي، "There is no triangle" پیغام وښيي.'),
        ('Q.10', 'Write a C++ program to input a character from the keyboard and display the message after testing whether it is Vowel or Consonant.', 'کی بورڈ سے ایک حرف لے کر یہ جانچنے کے بعد پیغام دکھانے کا C++ پروگرام لکھیں کہ آیا یہ حرفِ علت ہے یا حرفِ صحیح۔', 'یو C++ پروګرام ولیکئ چې له کیبورډ یو توری واخلي او د دې له ازمویلو وروسته چې ږغیز (Vowel) دی که بې‌ږغه (Consonant)، پیغام وښيي.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    ex = BOOK.record(e, 'cs12-u4-exercise-4', 'Unit 4 exercise (4)', 'یونٹ 4: مشق (۴)', '۴ څپرکی: تمرین (۴)', 78, [144])
    t = Builder()
    t.p('Unit 5', 'یونٹ 5', '۵ څپرکی')
    t.h('ARRAYS AND STRINGS', 'ایریز اور اسٹرنگز', 'لړۍ او تارونه')
    t.h('After the completion of Unit-5, Students will be able to:', 'یونٹ 5 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۵ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    t.group('list', [('Explain the concept of an array', 'ایرے کا تصور بیان کر سکیں', 'د لړۍ مفهوم تشریح کړي'), ('Know how array elements are arranged in memory', 'جان سکیں کہ ایرے کے عناصر میموری میں کیسے ترتیب پاتے ہیں', 'وپېژني چې د لړۍ عناصر په حافظه کې څنګه ترتیبېږي'),
                     ('Explain the following array terminology', 'ایرے کی درج ذیل اصطلاحات بیان کر سکیں', 'د لړۍ لاندې اصطلاحګانې تشریح کړي')])
    t.group('list', [('Name', 'نام', 'نوم'), ('Size', 'سائز', 'اندازه'), ('Index', 'انڈیکس', 'شاخص')])
    t.group('list', [
     ('Explain how to define and initialize an array of different size and data types', 'مختلف سائز اور ڈیٹا ٹائپس کے ایرے کی تعریف اور ابتدائی قدر دینے کا طریقہ بیان کر سکیں', 'د بېلابېلو اندازو او ډېټا ډولونو لړۍ د تعریف او لومړني ارزښت ورکولو لاره تشریح کړي'),
     ('Explain how to access and write at an index in an array', 'ایرے میں کسی انڈیکس پر رسائی اور لکھنے کا طریقہ بیان کر سکیں', 'په لړۍ کې پر یوه شاخص د لاسرسي او لیکلو لاره تشریح کړي'),
     ('Explain how to traverse an array using all loop structures', 'تمام لوپ ساختوں کے ذریعے ایرے کو عبور کرنے کا طریقہ بیان کر سکیں', 'د ټولو حلقوي جوړښتونو په مرسته د لړۍ د تېرېدو لاره تشریح کړي'),
     ('Use the sizeof() operator to find the size of an array', 'ایرے کا سائز معلوم کرنے کے لیے sizeof() آپریٹر استعمال کر سکیں', 'د لړۍ د اندازې پیدا کولو لپاره sizeof() چلونکی وکاروي'),
     ('Explain two dimensional array', 'دو جہتی ایرے بیان کر سکیں', 'دوه-بعدي لړۍ تشریح کړي'),
     ('Explain how to define and initialize a two dimensional array of different size and data types', 'مختلف سائز اور ڈیٹا ٹائپس کے دو جہتی ایرے کی تعریف اور ابتدائی قدر کا طریقہ بیان کر سکیں', 'د بېلابېلو اندازو او ډېټا ډولونو دوه-بعدي لړۍ د تعریف او لومړني ارزښت لاره تشریح کړي'),
     ('Explain how to access and write at an index in a two dimensional array', 'دو جہتی ایرے میں کسی انڈیکس پر رسائی اور لکھنے کا طریقہ بیان کر سکیں', 'په دوه-بعدي لړۍ کې پر یوه شاخص د لاسرسي او لیکلو لاره تشریح کړي'),
     ('Explain strings', 'اسٹرنگز بیان کر سکیں', 'تارونه تشریح کړي'),
     ('Explain how to define and initialize a string', 'اسٹرنگ کی تعریف اور ابتدائی قدر کا طریقہ بیان کر سکیں', 'د تار د تعریف او لومړني ارزښت لاره تشریح کړي'),
     ('Explain the most commonly used string functions', 'سب سے زیادہ استعمال ہونے والے اسٹرنگ فنکشنز بیان کر سکیں', 'تر ټولو ډېر کارېدونکي د تار فنکشنونه تشریح کړي')])
    UT = ('Arrays and Strings', 'ایریز اور اسٹرنگز', 'لړۍ او تارونه')
    rec = BOOK.record(t, 'cs12-u5-outcomes', 'Unit 5: learning outcomes', 'یونٹ 5: حاصلاتِ تعلم', '۵ څپرکی: د زده‌کړې پایلې', 78, [145], unit_title=UT)
    BOOK.save(78, [(4, ex), (5, rec)], complete_units=[4])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 75
    {75: p75, 76: p76, 77: p77, 78: p78}[n]()
