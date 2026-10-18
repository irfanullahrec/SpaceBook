"""Computer Science XII PDF79–81: pp.146–147 introduction, 5.1 array, 5.1.1 concept, array X diagram, 5.1.2 representation, Figures 5.1–5.2, 5.1.3 terminology;
pp.148–149 name/size/index, 5.1.4 definition, one-dimensional array, declaration, b. initializing (program whole incl. p.150);
pp.150–151 partial initialization, 5.1.5 accessing and writing, loop access program.
Run: python class12_cs_page079.py N (79–81)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import array_1d

I7 = [str(i) for i in range(7)]


def p79():
    t = Builder()
    P = t.p
    t.h('INTRODUCTION', 'تعارف', 'سریزه')
    P('This unit is about arrays i.e. its definition, representation, accessing and traversing. There are two types of array data structures, one dimensional and two dimensional. The unit also focuses on strings and its most commonly used functions.',
      'یہ یونٹ ایریز کے بارے میں ہے یعنی ان کی تعریف، نمائندگی، رسائی اور عبور۔ ایرے ڈیٹا اسٹرکچر کی دو اقسام ہیں، یک جہتی اور دو جہتی۔ یونٹ اسٹرنگز اور ان کے سب سے زیادہ استعمال ہونے والے فنکشنز پر بھی توجہ دیتا ہے۔',
      'دا څپرکی د لړیو په اړه دی، یعنې د هغو تعریف، ښودنه، لاسرسی او تېرېدل. د لړۍ ډېټا جوړښت دوه ډوله دی، یو-بعدي او دوه-بعدي. څپرکی په تارونو او د هغو په تر ټولو ډېر کارېدونکو فنکشنونو هم تمرکز کوي.')
    t.h('5.1 Introduction to array', '5.1 ایرے کا تعارف', '۵.۱ د لړۍ پېژندنه')
    P('We group our everyday data into conceptual units rather than storing in individual pieces. We collect the data items into conceptual units and assign names to them. For a single conceptual unit we have a single name. This conceptual unit of homogeneous data having the same name for all the data items is called array. The array is used to store many items of the same type as a single unit or group. Consider the examples of storing the scores of all the students of a class in an array or storing their names.',
      'ہم اپنے روزمرہ ڈیٹا کو الگ الگ ٹکڑوں میں رکھنے کے بجائے تصوراتی اکائیوں میں گروپ کرتے ہیں۔ ہم ڈیٹا آئٹمز کو تصوراتی اکائیوں میں جمع کر کے انھیں نام دیتے ہیں۔ ایک تصوراتی اکائی کا ایک ہی نام ہوتا ہے۔ یکساں ڈیٹا کی یہ تصوراتی اکائی جس کے تمام ڈیٹا آئٹمز کا نام ایک ہو، ایرے کہلاتی ہے۔ ایرے ایک ہی قسم کے بہت سے آئٹمز کو ایک اکائی یا گروپ کے طور پر محفوظ کرنے کے لیے استعمال ہوتا ہے۔ مثلاً کسی جماعت کے تمام طلبہ کے نمبر یا ان کے نام ایک ایرے میں محفوظ کرنا۔',
      'موږ خپل ورځنی ډېټا د جلا ټوټو پر ځای په مفهومي واحدونو کې ډله کوو. ډېټا توکي په مفهومي واحدونو کې راټولوو او نومونه ورکوو. د یوه مفهومي واحد لپاره یو نوم لرو. د ورته ډېټا دا مفهومي واحد چې ټول توکي یې یو نوم ولري، لړۍ بلل کېږي. لړۍ د یو ډول ډېرو توکو د یوه واحد یا ډلې په توګه ساتلو لپاره کارېږي. د بېلګې په توګه د یوه ټولګي د ټولو زده‌کوونکو نمرې یا نومونه په یوه لړۍ کې ساتل.')
    t.h('5.1.1 Concept of arrays', '5.1.1 ایریز کا تصور', '۵.۱.۱ د لړیو مفهوم')
    P('An array is a collection of data items of the same data types placed in contiguous memory locations that can individually be referenced by using an index to a unique identifier. Consider the example for storing 7 values of type int in an array without having to declare 7 different variables each one with a different variable name. Instead of that, using an array we can store 7 different values of the same data type with a unique variable name. Consider an array X that contains 7 integer values of type int. It can be represented as:',
      'ایرے ایک ہی ڈیٹا ٹائپ کے ڈیٹا آئٹمز کا مجموعہ ہے جو متصل میموری مقامات پر رکھے جاتے ہیں اور ایک منفرد شناخت کنندہ کے ساتھ انڈیکس استعمال کر کے انفرادی طور پر حوالہ دیے جا سکتے ہیں۔ int قسم کی 7 قدریں ایک ایرے میں محفوظ کرنے کی مثال لیں، جس میں 7 مختلف ناموں کے 7 الگ ویری ایبلز ڈکلیئر نہیں کرنے پڑتے۔ اس کے بجائے ایرے کے ذریعے ہم ایک ہی ڈیٹا ٹائپ کی 7 مختلف قدریں ایک منفرد ویری ایبل نام سے محفوظ کر سکتے ہیں۔ ایک ایرے X پر غور کریں جس میں int قسم کی 7 صحیح قدریں ہیں۔ اسے یوں ظاہر کیا جا سکتا ہے:',
      'لړۍ د یو ډول ډېټا ډولونو د ډېټا توکو ټولګه ده چې په پرله‌پسې حافظه ځایونو کې ایښودل کېږي او هر یو یې د یوه ځانګړي پېژندونکي سره د شاخص په کارولو جلا ګوتنیولای شي. په یوه لړۍ کې د int ډول ۷ ارزښتونو ساتلو بېلګه وګورئ، پرته له دې چې ۷ بېل متغیرونه د بېلو نومونو سره اعلان کړو. د دې پر ځای د لړۍ په مرسته کولی شو د یو ډېټا ډول ۷ بېل ارزښتونه د یوه ځانګړي متغیر نوم سره وساتو. یوه لړۍ X ته پام وکړئ چې د int ډول ۷ صحیح ارزښتونه لري. داسې ښودل کېدای شي:')
    caps = ('Array X of seven locations', 'سات مقامات والا ایرے X', 'د اوو ځایونو لړۍ X')
    sv = [array_1d('X', I7, None, None, c) for c in caps]
    t.visual('cs12-fig-array-x', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    P('These elements are numbered from 0 to 6 since in arrays the first index is always 0.', 'ان عناصر کو 0 سے 6 تک نمبر دیا گیا ہے کیونکہ ایریز میں پہلا انڈیکس ہمیشہ 0 ہوتا ہے۔', 'دا عناصر له 0 تر 6 شمېره شوي ځکه په لړیو کې لومړی شاخص تل 0 وي.')
    t.h('5.1.2 Representation of array', '5.1.2 ایرے کی نمائندگی', '۵.۱.۲ د لړۍ ښودنه')
    P('Array elements are stored in consecutive memory locations inside the computer memory. For example, if in the above array X we store the marks of seven students and the first element X[0] is stored at address 100, inside the computer memory, then X[1], X[2], X[3], X[4], X[5], X[6] will be stored at memory addresses 102,104,106, 108, 110, and 112 respectively. Here, the difference in the values of the memory addresses is two numbers because an int data type occupies 2 bytes of memory space. It is shown in figure 5.1.',
      'ایرے کے عناصر کمپیوٹر میموری کے اندر لگاتار میموری مقامات پر محفوظ ہوتے ہیں۔ مثلاً اگر اوپر کے ایرے X میں ہم سات طلبہ کے نمبر محفوظ کریں اور پہلا عنصر X[0] کمپیوٹر میموری میں پتہ 100 پر محفوظ ہو تو X[1]، X[2]، X[3]، X[4]، X[5]، X[6] بالترتیب میموری پتوں 102، 104، 106، 108، 110 اور 112 پر محفوظ ہوں گے۔ یہاں میموری پتوں کی قدروں میں دو کا فرق ہے کیونکہ int ڈیٹا ٹائپ میموری میں 2 بائٹس جگہ لیتی ہے۔ یہ شکل 5.1 میں دکھایا گیا ہے۔',
      'د لړۍ عناصر د کمپیوټر د حافظې دننه په پرله‌پسې حافظه ځایونو کې ساتل کېږي. د بېلګې په توګه که په پورته لړۍ X کې د اوو زده‌کوونکو نمرې وساتو او لومړی عنصر X[0] د کمپیوټر په حافظه کې په 100 پته وساتل شي، نو X[1]، X[2]، X[3]، X[4]، X[5]، X[6] به په ترتیب سره په 102، 104، 106، 108، 110 او 112 پتو کې وساتل شي. دلته د حافظې د پتو په ارزښتونو کې دوه شمېرې توپیر دی ځکه int ډېټا ډول په حافظه کې ۲ بایټه ځای نیسي. دا په ۵.۱ شکل کې ښودل شوی.')
    V = ['10', '02', '24', '06', '13', '11', '0']
    A = ['100', '102', '104', '106', '108', '110', '112']
    f1 = [array_1d('X', I7, V, A, c, notes=n) for c, n in [
        ('Figure 5.1: Memory Representation of 1-D Array for an int Data Type', ('Indices', 'Data Items', 'Memory Address')),
        ('شکل 5.1: int ڈیٹا ٹائپ کے لیے یک جہتی ایرے کی میموری نمائندگی', ('انڈیسز', 'ڈیٹا آئٹمز', 'میموری پتہ')),
        ('۵.۱ شکل: د int ډېټا ډول لپاره د یو-بعدي لړۍ د حافظې ښودنه', ('شاخصونه', 'ډېټا توکي', 'د حافظې پته'))]]
    t.visual('cs12-fig-5-1', f1[0][0], f1[1][0], f1[2][0], f1[0][1])
    P('Consider another example, shown in figure 5.2, of one dimensional array named SUBJ for storing the title of a subject whose length is 7 characters, such as, PHYSICS.',
      'ایک اور مثال پر غور کریں، جو شکل 5.2 میں دکھائی گئی ہے، SUBJ نامی یک جہتی ایرے کی جو کسی مضمون کا عنوان محفوظ کرنے کے لیے ہے جس کی لمبائی 7 حروف ہے، جیسے PHYSICS۔',
      'بلې بېلګې ته پام وکړئ چې په ۵.۲ شکل کې ښودل شوې، د SUBJ په نوم یو-بعدي لړۍ چې د یوه مضمون سرلیک ساتي چې اوږدوالی یې ۷ توري دي، لکه PHYSICS.')
    f2 = [array_1d('SUB', I7, list('PHYSICS'), [str(100 + i) for i in range(7)], c) for c in (
        'Figure 5.2: Memory Representation of 1-D Array for a char Data Type', 'شکل 5.2: char ڈیٹا ٹائپ کے لیے یک جہتی ایرے کی میموری نمائندگی', '۵.۲ شکل: د char ډېټا ډول لپاره د یو-بعدي لړۍ د حافظې ښودنه')]
    t.visual('cs12-fig-5-2', f2[0][0], f2[1][0], f2[2][0], f2[0][1])
    t.h('5.1.3 Terminology used in Arrays', '5.1.3 ایریز میں استعمال ہونے والی اصطلاحات', '۵.۱.۳ په لړیو کې کارېدونکې اصطلاحګانې')
    P('Arrays can be understood well by first knowing some commonly used terminologies such as name, size, and index.', 'ایریز کو پہلے کچھ عام اصطلاحات جیسے نام، سائز اور انڈیکس جان کر اچھی طرح سمجھا جا سکتا ہے۔', 'لړۍ ښه پوهېدای شو که لومړی ځینې عام اصطلاحګانې لکه نوم، اندازه او شاخص وپېژنو.')
    rec = BOOK.record(t, 'cs12-u5-text-1', 'Unit 5 text (1)', 'یونٹ 5 — متن (۱)', '۵ څپرکی — متن (۱)', 79, [146, 147])
    rec['sourceNote'] = 'The array diagrams and Figures 5.1–5.2 are reproduced as coded diagrams; data values and addresses are kept as printed.'
    BOOK.save(79, [(5, rec)], issues=[{'id': 'cs12-pdf079', 'unit': 5, 'printedPage': 147,
               'description': 'The text names the array “SUBJ” while Figure 5.2 labels it “SUB”; X[1] is printed as “02”. Retained as printed. Owner handwriting on pp.146–147 (“same”, “one for Row / one for column”, strike-through of “dimensional”) excluded.'}])


def p80():
    t = Builder()
    P = t.p
    t.h('a. Name of an array', 'a. ایرے کا نام', 'a. د لړۍ نوم')
    P('The name of the array can be any valid identifier. Each location of the array has the same name with different index. In the above example, all the 7 locations of the array X has the same name X but different indices, X[0], X[1], X[2], X[3], X[4], X[5], and X[6].',
      'ایرے کا نام کوئی بھی درست شناخت کنندہ ہو سکتا ہے۔ ایرے کے ہر مقام کا نام ایک ہی ہوتا ہے مگر انڈیکس مختلف۔ اوپر کی مثال میں ایرے X کے تمام 7 مقامات کا نام X ہے لیکن انڈیسز مختلف ہیں: X[0]، X[1]، X[2]، X[3]، X[4]، X[5] اور X[6]۔',
      'د لړۍ نوم هر سم پېژندونکی کېدای شي. د لړۍ هر ځای یو نوم لري خو بېل شاخص. په پورته بېلګه کې د لړۍ X ټول ۷ ځایونه یو نوم X لري خو بېل شاخصونه: X[0]، X[1]، X[2]، X[3]، X[4]، X[5] او X[6].')
    t.h('b. Size of the array', 'b. ایرے کا سائز', 'b. د لړۍ اندازه')
    P('The number of elements that can be stored in an array is called the size or length of that array.', 'ایرے میں جتنے عناصر محفوظ کیے جا سکتے ہیں ان کی تعداد اس ایرے کا سائز یا لمبائی کہلاتی ہے۔', 'د هغو عناصرو شمېر چې په یوه لړۍ کې ساتل کېدای شي، د هغې لړۍ اندازه یا اوږدوالی بلل کېږي.')
    P('For example:', 'مثال کے طور پر:', 'د بېلګې په توګه:')
    code(t, 'float Z [10];')
    P('Here, size of the array Z is 10, which means that we can store 10 floating point values in this array.', 'یہاں ایرے Z کا سائز 10 ہے، یعنی ہم اس ایرے میں 10 فلوٹنگ پوائنٹ قدریں محفوظ کر سکتے ہیں۔', 'دلته د Z لړۍ اندازه 10 ده، یعنې موږ کولی شو په دې لړۍ کې ۱۰ اعشاري ارزښتونه وساتو.')
    t.h('c. Index', 'c. انڈیکس', 'c. شاخص')
    P('The location number of an item in an array is called index or subscript of that element. For example 0,1,2,3,4,5 and 6 are the indices of the elements of the array int X[7].',
      'ایرے میں کسی آئٹم کے مقام کا نمبر اس عنصر کا انڈیکس یا سب اسکرپٹ کہلاتا ہے۔ مثلاً 0،1،2،3،4،5 اور 6 ایرے int X[7] کے عناصر کے انڈیسز ہیں۔',
      'په یوه لړۍ کې د یوه توکي د ځای شمېره د هغه عنصر شاخص یا ښکته‌لیک بلل کېږي. د بېلګې په توګه 0،1،2،3،4،5 او 6 د int X[7] لړۍ د عناصرو شاخصونه دي.')
    t.h('5.1.4 Definition and initialization of an array', '5.1.4 ایرے کی تعریف اور ابتدائی قدر', '۵.۱.۴ د لړۍ تعریف او لومړنی ارزښت')
    P('As we have two types of arrays, one dimensional and two dimensional, both have their own ways of definition. Here, we are defining and initializing one dimensional array.',
      'چونکہ ہمارے پاس دو قسم کے ایریز ہیں، یک جہتی اور دو جہتی، دونوں کی تعریف کے اپنے طریقے ہیں۔ یہاں ہم یک جہتی ایرے کی تعریف اور ابتدائی قدر دے رہے ہیں۔',
      'څرنګه چې موږ دوه ډوله لړۍ لرو، یو-بعدي او دوه-بعدي، دواړه د تعریف خپلې لارې لري. دلته موږ یو-بعدي لړۍ تعریفوو او لومړنی ارزښت ورکوو.')
    t.h('a. One dimensional array', 'a. یک جہتی ایرے', 'a. یو-بعدي لړۍ')
    P('A one-dimensional array or linear array can be represented as a single row of contiguous memory locations. Accessing of its elements involves a single subscript.',
      'یک جہتی یا لکیری ایرے کو متصل میموری مقامات کی ایک قطار کے طور پر ظاہر کیا جا سکتا ہے۔ اس کے عناصر تک رسائی میں ایک سب اسکرپٹ شامل ہوتا ہے۔',
      'یو-بعدي یا خطي لړۍ د پرله‌پسې حافظه ځایونو د یوې قطار په توګه ښودل کېدای شي. د هغې عناصرو ته لاسرسی یو ښکته‌لیک لري.')
    fv = [array_1d('Vowel', [str(i) for i in range(5)], list('aeiou'), [str(100 + i) for i in range(5)], c) for c in
          ('One-dimensional array Vowel', 'یک جہتی ایرے Vowel', 'یو-بعدي لړۍ Vowel')]
    t.visual('cs12-fig-array-vowel', fv[0][0], fv[1][0], fv[2][0], fv[0][1])
    P('Like a regular variable, an array must be declared before it is used. A typical declaration for a one dimensional array in C++ is:', 'عام ویری ایبل کی طرح ایرے کو بھی استعمال سے پہلے ڈکلیئر کرنا ضروری ہے۔ C++ میں یک جہتی ایرے کی ایک عام ڈکلیریشن یہ ہے:', 'د عادي متغیر په څېر لړۍ هم باید له کارولو مخکې اعلان شي. په C++ کې د یو-بعدي لړۍ یو عادي اعلان دا دی:')
    code(t, 'data type name [size];')
    P('Here, the data type is a valid data type (such as int, float...), name is a valid identifier and enclosed in square brackets [ ] is the size of the array which means that how many elements this array can accommodate.',
      'یہاں data type ایک درست ڈیٹا ٹائپ ہے (جیسے int، float...)، name ایک درست شناخت کنندہ ہے اور مربع بریکٹس [ ] میں ایرے کا سائز ہے یعنی یہ ایرے کتنے عناصر سما سکتا ہے۔',
      'دلته data type یو سم ډېټا ډول دی (لکه int، float...)، name یو سم پېژندونکی دی او په مربع قوسونو [ ] کې د لړۍ اندازه ده، یعنې دا لړۍ څو عناصر ځایولی شي.')
    P('For Example:', 'مثال کے طور پر:', 'د بېلګې په توګه:')
    code(t, '''int x[7];
char vowel[5];
float temperature[7];''')
    t.h('b. Initializing one dimensional array', 'b. یک جہتی ایرے کو ابتدائی قدر دینا', 'b. یو-بعدي لړۍ ته لومړنی ارزښت ورکول')
    P('Arrays can be initialized, like variables, when created. C++ provides a convenient way to initialize entire array via use of an initializer list.', 'ایریز کو ویری ایبلز کی طرح بنتے وقت ابتدائی قدر دی جا سکتی ہے۔ C++ ابتدائی فہرست (initializer list) کے ذریعے پورے ایرے کو ابتدائی قدر دینے کا آسان طریقہ فراہم کرتی ہے۔', 'لړیو ته د متغیرونو په څېر د جوړېدو پر مهال لومړنی ارزښت ورکول کېدای شي. C++ د لومړني ارزښت لړلیک (initializer list) په کارولو د ټولې لړۍ د لومړني ارزښت ورکولو اسانه لاره برابروي.')
    P('The following example shows the initialization of an integer array.', 'درج ذیل مثال ایک integer ایرے کی ابتدائی قدر دکھاتی ہے۔', 'لاندې بېلګه د integer لړۍ لومړنی ارزښت ښيي.')
    code(t, '''// initializing array using initializer list method
#include <iostream.h>
#include <conio.h>
int main()
{
int A[5] = { 3, 2, 7, 5, 8 };
cout << A[0] << endl;
cout << A [1] << endl;
cout << A [2] << endl;
cout << A [3] << endl;
cout << A [4] << endl;
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''3
2
7
5
8''')
    rec = BOOK.record(t, 'cs12-u5-text-2', 'Unit 5 text (2)', 'یونٹ 5 — متن (۲)', '۵ څپرکی — متن (۲)', 80, [148, 149, 150])
    rec['sourceNote'] = 'The initializer-list program continues on p.150 (PDF81) and is given whole with its output. The uncaptioned Vowel array diagram is reproduced as a coded diagram with a descriptive label.'
    BOOK.save(80, [(5, rec)], issues=[{'id': 'cs12-pdf080', 'unit': 5, 'printedPage': 148,
               'description': 'p.148 “all the 7 locations of the array X has the same name”. Retained as printed. Owner handwriting and scribbles in English and Urdu on p.149 excluded.'}])


def p81():
    t = Builder()
    P = t.p
    P('If we do not initialize all of the elements in an array then the remaining elements will be initialized to 0.', 'اگر ہم ایرے کے تمام عناصر کو ابتدائی قدر نہ دیں تو باقی عناصر کو 0 ابتدائی قدر مل جاتی ہے۔', 'که د لړۍ ټولو عناصرو ته لومړنی ارزښت ورنه کړو، پاتې عناصر 0 لومړنی ارزښت اخلي.')
    P('Similarly, to initialize all the elements of an array to 0, we can define that array as:', 'اسی طرح ایرے کے تمام عناصر کو 0 ابتدائی قدر دینے کے لیے ہم اس ایرے کی تعریف یوں کر سکتے ہیں:', 'همداراز د لړۍ ټولو عناصرو ته د 0 لومړني ارزښت ورکولو لپاره هغه لړۍ داسې تعریفولی شو:')
    code(t, 'int A[5]={0};')
    t.h('5.1.5 Accessing and writing at an index in an array', '5.1.5 ایرے میں کسی انڈیکس پر رسائی اور لکھنا', '۵.۱.۵ په لړۍ کې پر یوه شاخص لاسرسی او لیکل')
    P('Accessing of array means to get into an index in an array and take its value for some operation while by writing at an index of an array is storing some value at a particular index of the array. These are the two important actions that should be taken while dealing with arrays.',
      'ایرے تک رسائی کا مطلب ایرے کے کسی انڈیکس تک پہنچ کر کسی عمل کے لیے اس کی قدر لینا ہے، جبکہ ایرے کے کسی انڈیکس پر لکھنے سے مراد ایرے کے کسی خاص انڈیکس پر کوئی قدر محفوظ کرنا ہے۔ ایریز سے کام کرتے ہوئے یہ دو اہم کام ہیں۔',
      'د لړۍ لاسرسي معنا ده چې د لړۍ یوه شاخص ته ورسېږو او د یوې عملیې لپاره یې ارزښت واخلو، او د لړۍ پر یوه شاخص لیکل په یوه ځانګړي شاخص کې د یوه ارزښت ساتل دي. دا دوه مهم کارونه دي چې د لړیو سره د کار پر مهال باید وشي.')
    P('The following section addresses them with examples.', 'درج ذیل حصہ مثالوں کے ساتھ ان پر بات کرتا ہے۔', 'لاندې برخه دا د بېلګو سره څېړي.')
    t.h('Accessing an array', 'ایرے تک رسائی', 'لړۍ ته لاسرسی')
    P('Array elements are accessed by using respective indices. The format for accessing is as follows:', 'ایرے کے عناصر تک متعلقہ انڈیسز کے ذریعے رسائی ہوتی ہے۔ رسائی کی شکل یہ ہے:', 'د لړۍ عناصرو ته د اړوندو شاخصونو په کارولو لاسرسی کېږي. د لاسرسي بڼه دا ده:')
    code(t, 'Array name[index];')
    P('Looking at the example discussed in the above section, in which A has 5 elements, each of the element has been accessed as A[0], A[1], …, A[4] using cout statement.',
      'اوپر کے حصے میں زیرِ بحث مثال کو دیکھیں جس میں A کے 5 عناصر ہیں، ہر عنصر تک cout بیان کے ذریعے A[0]، A[1]، …، A[4] کے طور پر رسائی کی گئی ہے۔',
      'پورته برخه کې بحث شوې بېلګې ته وګورئ چې پکې A ۵ عناصر لري، هر عنصر ته د cout بیان په مرسته د A[0]، A[1]، …، A[4] په توګه لاسرسی شوی.')
    P('To access all elements of an array we use loops instead of individual reference to each element, For Example:', 'ایرے کے تمام عناصر تک رسائی کے لیے ہم ہر عنصر کے انفرادی حوالے کے بجائے لوپس استعمال کرتے ہیں، مثال کے طور پر:', 'د لړۍ ټولو عناصرو ته د لاسرسي لپاره د هر عنصر د جلا ګوتنیونې پر ځای حلقې کاروو، د بېلګې په توګه:')
    code(t, '''// accessing array using loop
#include <iostream.h>
#include <conio.h>
int main()
{
int A[5] = { 3, 2, 7, 5, 8 };
for(int i=0; i<=4; ++i)
cout << A[i] << endl;
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''3
2
7
5
8''')
    P('Here, for loop has been used to access the elements of the array one by one and print the result on the screen.', 'یہاں for لوپ ایرے کے عناصر تک ایک ایک کر کے رسائی اور نتیجہ اسکرین پر پرنٹ کرنے کے لیے استعمال ہوا ہے۔', 'دلته for حلقه د لړۍ عناصرو ته یو په یو لاسرسي او پر پرده د پایلې چاپولو لپاره کارول شوې.')
    rec = BOOK.record(t, 'cs12-u5-text-3', 'Unit 5 text (3)', 'یونٹ 5 — متن (۳)', '۵ څپرکی — متن (۳)', 81, [150, 151])
    rec['sourceNote'] = 'The top of p.150 (end of the initializer-list program and its output) is recorded with PDF80.'
    BOOK.save(81, [(5, rec)])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 79
    {79: p79, 80: p80, 81: p81}[n]()
