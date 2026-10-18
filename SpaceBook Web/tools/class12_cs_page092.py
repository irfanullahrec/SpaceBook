"""Computer Science XII PDF92–93: p.172 Unit 5 summary; pp.173–174 exercise Q1–Q10 (unit 5 complete); p.175 Unit 6 opener.
Run: python class12_cs_page092.py N (92 or 93)."""
import sys
from class12_cs_common import BOOK, Builder


def p92():
    s = Builder()
    s.h('Summary', 'خلاصہ', 'لنډیز')
    s.group('list', [
     ('A collection of homogeneous data items stored in consecutive memory locations is called array.', 'متصل میموری مقامات میں محفوظ یکساں ڈیٹا آئٹمز کا مجموعہ ایرے کہلاتا ہے۔', 'په پرله‌پسې حافظه ځایونو کې د ساتل شویو ورته ډېټا توکو ټولګه لړۍ بلل کېږي.'),
     ('An array can store data of any valid data type, e.g. integer, floating point and character. An integer array can only store integer data.', 'ایرے کسی بھی درست ڈیٹا ٹائپ کا ڈیٹا محفوظ کر سکتا ہے، مثلاً integer، floating point اور character۔ integer ایرے صرف integer ڈیٹا محفوظ کر سکتا ہے۔', 'لړۍ کولی شي د هر سم ډېټا ډول ډېټا وساتي، لکه integer، floating point او character. integer لړۍ یوازې integer ډېټا ساتلی شي.'),
     ('There are two types of arrays: one dimensional and multi-dimensional. Two dimensional arrays is a type of multi-dimensional array.', 'ایریز کی دو اقسام ہیں: یک جہتی اور کثیر جہتی۔ دو جہتی ایریز کثیر جہتی ایرے کی ایک قسم ہے۔', 'لړۍ دوه ډوله دي: یو-بعدي او څو-بعدي. دوه-بعدي لړۍ د څو-بعدي لړۍ یو ډول دی.'),
     ('One dimensional array can be defined by using a single subscript.', 'یک جہتی ایرے ایک سب اسکرپٹ استعمال کر کے بیان کیا جا سکتا ہے۔', 'یو-بعدي لړۍ د یوه ښکته‌لیک په کارولو تعریفېدای شي.'),
     ('Two dimensional arrays can be represented with the help of two subscripts. It is also called matrix in mathematics and table in business application.', 'دو جہتی ایریز دو سب اسکرپٹس کی مدد سے ظاہر کیے جا سکتے ہیں۔ اسے ریاضی میں میٹرکس اور کاروباری ایپلیکیشن میں ٹیبل بھی کہتے ہیں۔', 'دوه-بعدي لړۍ د دوو ښکته‌لیکونو په مرسته ښودل کېدای شي. په ریاضي کې ماتریکس او په سوداګریز کاريال کې جدول هم بلل کېږي.'),
     ('One dimensional array can be defined by preceding the name of the array by a valid data type and followed by a single subscript.', 'یک جہتی ایرے کو ایرے کے نام سے پہلے درست ڈیٹا ٹائپ اور بعد میں ایک سب اسکرپٹ لگا کر بیان کیا جا سکتا ہے۔', 'یو-بعدي لړۍ د لړۍ له نوم مخکې د سم ډېټا ډول او وروسته د یوه ښکته‌لیک په لیکلو تعریفېدای شي.'),
     ('Two dimensional arrays can also be defined by preceding the name of the array by a valid data type, such as int, long and char etc., and followed by two subscripts.', 'دو جہتی ایریز کو بھی ایرے کے نام سے پہلے درست ڈیٹا ٹائپ، جیسے int، long اور char وغیرہ، اور بعد میں دو سب اسکرپٹس لگا کر بیان کیا جا سکتا ہے۔', 'دوه-بعدي لړۍ هم د لړۍ له نوم مخکې د سم ډېټا ډول، لکه int، long او char او نور، او وروسته د دوو ښکته‌لیکونو په لیکلو تعریفېدای شي.'),
     ('One dimensional and two dimensional arrays can be initialized in the same way during the declaration time.', 'یک جہتی اور دو جہتی ایریز کو ڈکلیریشن کے وقت ایک ہی طریقے سے ابتدائی قدر دی جا سکتی ہے۔', 'یو-بعدي او دوه-بعدي لړیو ته د اعلان پر مهال په یوه ډول لومړنی ارزښت ورکول کېدای شي.'),
     ('Arrays can be efficiently and easily processed with the help of looping structures.', 'ایریز پر لوپنگ ساختوں کی مدد سے مؤثر اور آسان طریقے سے عمل کیا جا سکتا ہے۔', 'لړۍ د حلقوي جوړښتونو په مرسته په اغېزمنه او اسانه توګه پروسس کېدای شي.'),
     ('A sequence of characters enclosed in double quotes is called string.', 'ڈبل کوٹس میں بند حروف کی ترتیب اسٹرنگ کہلاتی ہے۔', 'په دوه‌ګونو نقل‌قولونو کې د تړلو تورو لړۍ تار بلل کېږي.'),
     ('Different operations such as comparison, concatenation, copying, and finding length can be performed on strings.', 'اسٹرنگز پر مختلف عمل جیسے موازنہ، جوڑنا، نقل کرنا اور لمبائی معلوم کرنا کیے جا سکتے ہیں۔', 'پر تارونو بېلابېلې عملیې لکه پرتله، نښلول، کاپي کول او د اوږدوالي موندل ترسره کېدای شي.')])
    sm = BOOK.record(s, 'cs12-u5-summary', 'Unit 5 summary', 'یونٹ 5: خلاصہ', '۵ څپرکی: لنډیز', 92, [172])
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. In C/C++ language, normally the indexing of an array starts from ________ .', 'i. C/C++ زبان میں عموماً ایرے کی انڈیکسنگ ________ سے شروع ہوتی ہے۔', 'i. په C/C++ ژبه کې عموماً د لړۍ شاخص‌ورکول له ________ پیلېږي.'),
     ('ii. The size of the array int x[10] is ________ .', 'ii. ایرے int x[10] کا سائز ________ ہے۔', 'ii. د int x[10] لړۍ اندازه ________ ده.'),
     ('iii. char century [100][365][24][60][60] is an example of ________ array.', 'iii. char century [100][365][24][60][60] ________ ایرے کی مثال ہے۔', 'iii. char century [100][365][24][60][60] د ________ لړۍ بېلګه ده.'),
     ('iv. An array of characters is called ________ .', 'iv. حروف کا ایرے ________ کہلاتا ہے۔', 'iv. د تورو لړۍ ________ بلل کېږي.'),
     ('v. float x[12] defines one dimensional array of type ________ .', 'v. float x[12] ________ قسم کا یک جہتی ایرے بیان کرتا ہے۔', 'v. float x[12] د ________ ډول یو-بعدي لړۍ تعریفوي.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    e.mcq('i.', ('A collection of data items of the same data types placed in contiguous memory locations is called ________ .', 'متصل میموری مقامات میں رکھے گئے ایک ہی ڈیٹا ٹائپ کے ڈیٹا آئٹمز کا مجموعہ ________ کہلاتا ہے۔', 'په پرله‌پسې حافظه ځایونو کې د ایښودل شویو یو ډول ډېټا توکو ټولګه ________ بلل کېږي.'),
          [('Record', 'ریکارڈ', 'ریکارډ'), ('Array', 'ایرے', 'لړۍ'), ('Program', 'پروگرام', 'پروګرام'), ('File', 'فائل', 'دوتنه')], per_line=1)
    e.p('ii. Observe the following statements and decide what they do.', 'ii. درج ذیل بیانات کا مشاہدہ کریں اور فیصلہ کریں کہ یہ کیا کرتے ہیں۔', 'ii. لاندې بیانونو ته وګورئ او پرېکړه وکړئ چې څه کوي.')
    from class12_cs_common import code
    code(e, '''string mystring;
getline(cin, mystring);''')
    e.group('lines', [('(a) reads a line of string from cin into mystring', '(a) cin سے اسٹرنگ کی ایک لائن mystring میں پڑھتا ہے', '(a) له cin څخه د تار یوه کرښه mystring ته لولي'),
                      ('(b) reads a line of string from mystring into cin', '(b) mystring سے اسٹرنگ کی ایک لائن cin میں پڑھتا ہے', '(b) له mystring څخه د تار یوه کرښه cin ته لولي'),
                      ('(c) cin can’t be used this way', '(c) cin اس طرح استعمال نہیں ہو سکتا', '(c) cin په دې ډول نه شي کارېدای'), ('(d) none of the above', '(d) ان میں سے کوئی نہیں', '(d) له پورته هېڅ یو')])
    e.mcq('iii.', ('Which of the header file must be included to use string stream?', 'string stream استعمال کرنے کے لیے کون سی ہیڈر فائل شامل کرنا ضروری ہے؟', 'د string stream د کارولو لپاره کومه سرپاڼه دوتنه باید شامله شي؟'),
          ['<iostream>', '<string>', '<sstring>', '<sstream>'], per_line=1)
    e.mcq('iv.', ('The location number of an item in an array is called ________ .', 'ایرے میں کسی آئٹم کے مقام کا نمبر ________ کہلاتا ہے۔', 'په لړۍ کې د یوه توکي د ځای شمېره ________ بلل کېږي.'),
          [('Data', 'ڈیٹا', 'ډېټا'), ('Value', 'قدر', 'ارزښت'), ('Index', 'انڈیکس', 'شاخص'), ('Constant', 'مستقل', 'ثابت')], per_line=1)
    e.mcq('v.', ('Strings are character arrays. The last index of it contains the null character ________ .', 'اسٹرنگز حروف کے ایرے ہیں۔ اس کے آخری انڈیکس میں null حرف ________ ہوتا ہے۔', 'تارونه د تورو لړۍ دي. د هغې وروستی شاخص null توری ________ لري.'),
          ['\\n', '\\t', '\\0', '\\1'], per_line=1)
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. Array is a collection of heterogeneous type of data.', 'i. ایرے مختلف النوع ڈیٹا کا مجموعہ ہے۔', 'i. لړۍ د ناورته ډول ډېټا ټولګه ده.'),
     ('ii. Array can be initialized during declaration time.', 'ii. ایرے کو ڈکلیریشن کے وقت ابتدائی قدر دی جا سکتی ہے۔', 'ii. لړۍ ته د اعلان پر مهال لومړنی ارزښت ورکول کېدای شي.'),
     ('iii. char vowel[5] declares an integer type array that holds the vowel characters of English language.', 'iii. char vowel[5] ایک integer قسم کا ایرے ڈکلیئر کرتا ہے جس میں انگریزی زبان کے حروفِ علت ہیں۔', 'iii. char vowel[5] د integer ډول لړۍ اعلانوي چې د انګلیسي ژبې ږغیز توري ساتي.'),
     ('iv. Loop is the best tool for handling large arrays.', 'iv. بڑے ایریز کو سنبھالنے کے لیے لوپ بہترین ذریعہ ہے۔', 'iv. د لویو لړیو د چلولو لپاره حلقه غوره وسیله ده.'),
     ('v. Array elements are stored in the memory where ever free space is available.', 'v. ایرے کے عناصر میموری میں جہاں بھی خالی جگہ دستیاب ہو، محفوظ ہوتے ہیں۔', 'v. د لړۍ عناصر په حافظه کې هر چېرې چې تش ځای وي، ساتل کېږي.')])
    for q, en, ur, ps in [
        ('Q.4', 'Declare an array to hold the high temperature (to the nearest tenth of a degree) for each day of a year. Assign a value of 0 to each day.', 'سال کے ہر دن کا زیادہ سے زیادہ درجۂ حرارت (ڈگری کے قریب ترین دسویں حصے تک) رکھنے کے لیے ایرے ڈکلیئر کریں۔ ہر دن کو 0 قدر دیں۔', 'د کال د هرې ورځې د لوړې تودوخې (د درجې تر نږدې لسمې برخې) د ساتلو لپاره یوه لړۍ اعلان کړئ. هرې ورځې ته 0 ارزښت ورکړئ.'),
        ('Q.5', 'Write down a C++ program to find the multiplication of two matrices A[3][2] and B[2][3].', 'دو میٹرکسز A[3][2] اور B[2][3] کا حاصلِ ضرب معلوم کرنے کا C++ پروگرام لکھیں۔', 'د دوو ماتریکسونو A[3][2] او B[2][3] د ضرب موندلو لپاره یو C++ پروګرام ولیکئ.'),
        ('Q.6', 'Write down a C++ program to find the subtraction and addition of two matrices A[3][3] and B[3][3].', 'دو میٹرکسز A[3][3] اور B[3][3] کی تفریق اور جمع معلوم کرنے کا C++ پروگرام لکھیں۔', 'د دوو ماتریکسونو A[3][3] او B[3][3] د تفریق او جمع موندلو لپاره یو C++ پروګرام ولیکئ.'),
        ('Q.7', 'Write a C++ program to find the transpose of a matrix A[3][3].', 'میٹرکس A[3][3] کا ٹرانسپوز معلوم کرنے کا C++ پروگرام لکھیں۔', 'د A[3][3] ماتریکس د ټرانسپوز موندلو لپاره یو C++ پروګرام ولیکئ.'),
        ('Q.8', 'Write a C++ program to read the temperature of the whole week in an array and then find the hottest day of the week.', 'پورے ہفتے کا درجۂ حرارت ایک ایرے میں پڑھنے اور پھر ہفتے کا سب سے گرم دن معلوم کرنے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د ټولې اونۍ تودوخه په یوه لړۍ کې ولولي او بیا د اونۍ تر ټولو ګرمه ورځ پیدا کړي.'),
        ('Q.9', 'Write a C++ program to read ten alphabets of English from the keyboard into a character type array and then sort them in descending order.', 'کی بورڈ سے انگریزی کے دس حروفِ تہجی ایک character قسم کے ایرے میں پڑھنے اور پھر انھیں نزولی ترتیب میں ترتیب دینے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې له کیبورډ د انګلیسي لس توري د character ډول لړۍ ته ولولي او بیا یې په نزولي ترتیب ترتیب کړي.'),
        ('Q.10', 'Write a C++ program to find sum of the values of a two dimensional array int Test[2][3] and display the result on the screen.', 'دو جہتی ایرے int Test[2][3] کی قدروں کا مجموعہ معلوم کرنے اور نتیجہ اسکرین پر دکھانے کا C++ پروگرام لکھیں۔', 'یو C++ پروګرام ولیکئ چې د int Test[2][3] دوه-بعدي لړۍ د ارزښتونو مجموعه پیدا کړي او پایله پر پرده وښيي.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    ex = BOOK.record(e, 'cs12-u5-exercise', 'Unit 5 exercise', 'یونٹ 5: مشق', '۵ څپرکی: تمرین', 92, [173, 174])
    ex['sourceNote'] = 'The exercise runs from p.173 to p.174 (PDF93) and is recorded here whole.'
    BOOK.save(92, [(5, sm), (5, ex)])


def p93():
    t = Builder()
    t.p('Unit 6', 'یونٹ 6', '۶ څپرکی')
    t.h('FUNCTIONS', 'فنکشنز', 'فنکشنونه')
    t.h('After the completion of Unit-6, Students will be able to:', 'یونٹ 6 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۶ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    L = lambda *x: t.group('list', list(x))
    L(('Explain the concept and types of functions', 'فنکشنز کا تصور اور اقسام بیان کر سکیں', 'د فنکشنونو مفهوم او ډولونه تشریح کړي'), ('Explain the advantages of using functions', 'فنکشنز کے استعمال کے فوائد بیان کر سکیں', 'د فنکشنونو د کارونې ګټې تشریح کړي'),
      ('Explain the signature of functions (Name, Arguments, Return type)', 'فنکشنز کا سگنیچر (نام، آرگیومنٹس، ریٹرن ٹائپ) بیان کر سکیں', 'د فنکشنونو لاسلیک (نوم، دلیلونه، د بېرته ورکړې ډول) تشریح کړي'), ('Explain:', 'وضاحت کر سکیں:', 'تشریح کړي:'))
    L(('Function prototype', 'فنکشن پروٹوٹائپ', 'د فنکشن نمونه'), ('Function definition', 'فنکشن کی تعریف', 'د فنکشن تعریف'), ('Function call', 'فنکشن کال', 'د فنکشن غوښتنه'))
    L(('Differentiate among local, global and static variables', 'مقامی، عالمی اور اسٹیٹک ویری ایبلز میں فرق کر سکیں', 'د محلي، نړیوالو او ثابتو متغیرونو ترمنځ توپیر وکړي'), ('Differentiate between formal and actual parameters', 'رسمی اور اصل پیرامیٹرز میں فرق کر سکیں', 'د رسمي او اصلي پاراميټرونو ترمنځ توپیر وکړي'),
      ('Know the concept of local and global functions', 'مقامی اور عالمی فنکشنز کا تصور جان سکیں', 'د محلي او نړیوالو فنکشنونو مفهوم وپېژني'), ('Use inline functions', 'ان لائن فنکشنز استعمال کر سکیں', 'inline فنکشنونه وکاروي'), ('Pass the arguments:', 'آرگیومنٹس پاس کر سکیں:', 'دلیلونه ولېږدوي:'))
    L(('constants', 'مستقل', 'ثابتونه'), ('By value', 'بذریعہ قدر', 'د ارزښت له لارې'), ('By reference', 'بذریعہ حوالہ', 'د حوالې له لارې'))
    L(('Use default arguments', 'ڈیفالٹ آرگیومنٹس استعمال کر سکیں', 'ډیفالټ دلیلونه وکاروي'), ('Use return statement', 'return بیان استعمال کر سکیں', 'return بیان وکاروي'), ('Define function overloading', 'فنکشن اوورلوڈنگ کی تعریف کر سکیں', 'د فنکشن ډېرول (overloading) تعریف کړي'),
      ('Know advantages of function overloading', 'فنکشن اوورلوڈنگ کے فوائد جان سکیں', 'د فنکشن ډېرولو ګټې وپېژني'), ('Understand the use of function overloading with:', 'فنکشن اوورلوڈنگ کا استعمال سمجھ سکیں:', 'د فنکشن ډېرولو کارونه وپوهېږي:'))
    L(('Number of arguments', 'آرگیومنٹس کی تعداد', 'د دلیلونو شمېر'), ('Data types of arguments', 'آرگیومنٹس کی ڈیٹا ٹائپس', 'د دلیلونو ډېټا ډولونه'), ('Return type', 'ریٹرن ٹائپ', 'د بېرته ورکړې ډول'))
    rec = BOOK.record(t, 'cs12-u6-outcomes', 'Unit 6: learning outcomes', 'یونٹ 6: حاصلاتِ تعلم', '۶ څپرکی: د زده‌کړې پایلې', 93, [175],
                      unit_title=('Functions', 'فنکشنز', 'فنکشنونه'))
    BOOK.save(93, [(6, rec)], complete_units=[5])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 92
    p92() if n == 92 else p93()
