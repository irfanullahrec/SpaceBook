"""Computer Science XII PDF82–85: pp.152–153 writing at an index, loop writing program (whole incl. p.154);
pp.154–155 5.1.6 traversing, search program, odd-values program; pp.156–157 5.1.7 sizeof(), 5.2 two-dimensional arrays, 5.2.1 concept;
pp.158–159 array X diagram, 5.2.2 definition and initialization, 5.2.3 accessing (begins).
Run: python class12_cs_page082.py N (82–85)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import array_2d

OUT = ('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')


def p82():
    t = Builder()
    P = t.p
    t.h('Writing at an index in an array', 'ایرے میں کسی انڈیکس پر لکھنا', 'په لړۍ کې پر یوه شاخص لیکل')
    P('Accessing of an index of an array is followed by the writing operation, only in the case, if we want to store a new value at that index or to update the existing one. For example, if we want to add the values in the array A, we can individually access each array location and write the value using assignment operator or using input statement (cin) It is shown in the following program.',
      'ایرے کے کسی انڈیکس تک رسائی کے بعد لکھنے کا عمل صرف اس صورت میں ہوتا ہے جب ہم اس انڈیکس پر نئی قدر محفوظ کرنا یا موجودہ قدر کو تازہ کرنا چاہیں۔ مثلاً اگر ہم ایرے A میں قدریں شامل کرنا چاہیں تو ہم ایرے کے ہر مقام تک الگ الگ رسائی کر کے اسائنمنٹ آپریٹر یا ان پٹ بیان (cin) کے ذریعے قدر لکھ سکتے ہیں۔ یہ درج ذیل پروگرام میں دکھایا گیا ہے۔',
      'د لړۍ یوه شاخص ته له لاسرسي وروسته د لیکلو عملیه یوازې هغه وخت کېږي چې په هغه شاخص کې نوی ارزښت ساتل یا موجود تازه کول غواړو. د بېلګې په توګه که په A لړۍ کې ارزښتونه اچول غواړو، کولی شو د لړۍ هر ځای ته جلا لاسرسی وکړو او د ګمارنې چلونکي یا د ننوتنې بیان (cin) په مرسته ارزښت ولیکو. دا په لاندې پروګرام کې ښودل شوی.')
    code(t, '''// writing at in index of an array
#include <iostream.h>
#include <conio.h>
int main()
{
int A[5];
A[0]=12;
A[1]=-20
cout<< "Enter number"<<endl;
cin >> A[2];
cout<< "Enter number"<<endl;
cin >> A[3];
cout<< "Enter number"<<endl;
cin >> A[4];
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Enter number
7
Enter number
5
Enter number
8''')
    P('Loops can also be used for writing at all indexes of an array. Consider the following example having an array Temperature that accepts the values of weekly temperature from the users at run time and write them into their respective indexes.',
      'لوپس ایرے کے تمام انڈیکسز پر لکھنے کے لیے بھی استعمال ہو سکتے ہیں۔ درج ذیل مثال پر غور کریں جس میں ایرے Temperature رن ٹائم پر صارفین سے ہفتہ وار درجۂ حرارت کی قدریں لیتا ہے اور انھیں متعلقہ انڈیکسز پر لکھتا ہے۔',
      'حلقې د لړۍ پر ټولو شاخصونو د لیکلو لپاره هم کارول کېدای شي. لاندې بېلګې ته پام وکړئ چې Temperature لړۍ لري چې د اجرا پر مهال له کاروونکو د اونۍ د تودوخې ارزښتونه اخلي او په اړوندو شاخصونو کې یې لیکي.')
    code(t, '''// writing an array using loop
#include <iostream.h>
#include <conio.h>
int main()
{
float Temperature[7];
cout<< "Enter 7 days temperature:"<<endl;
for(int i=0; i<7; ++i)
cin >>Temperature[i]; // writing at indexes
cout<< "The last week temperature was:"<<endl;
for(int i=0; i<7; ++i)
cout<<Temperature[i] << ", "; // accessing the elements
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Enter 7 days temperature:
35.9 22.0 27.3 25.5 28.3 31.2 33.7
The last week temperature was:
35.9, 22.0, 27.3, 25.5, 28.3, 31.2, 33.7''')
    rec = BOOK.record(t, 'cs12-u5-text-4', 'Unit 5 text (4)', 'یونٹ 5 — متن (۴)', '۵ څپرکی — متن (۴)', 82, [152, 153, 154])
    rec['sourceNote'] = 'The output of the Temperature program ends at the top of p.154 (PDF83) and is given whole here.'
    BOOK.save(82, [(5, rec)], issues=[{'id': 'cs12-pdf082', 'unit': 5, 'printedPage': 152,
               'description': 'The writing program prints “A[1]=-20” without a semicolon; its comment reads “writing at in index”; the paragraph lacks a full stop after “(cin)”. Retained as printed.'}])


def p83():
    t = Builder()
    P = t.p
    t.h('5.1.6 Traversing an array', '5.1.6 ایرے کو عبور کرنا', '۵.۱.۶ د لړۍ تېرېدل')
    P('Accessing the elements of an array is called traversing of array.', 'ایرے کے عناصر تک رسائی ایرے کو عبور کرنا (traversing) کہلاتی ہے۔', 'د لړۍ عناصرو ته لاسرسی د لړۍ تېرېدل (traversing) بلل کېږي.')
    code(t, '''// reading numbers into an array and then searching for an item
#include <iostream.h>
#include <conio.h>
int main()
{
int a[10]; // Declare an array of 10 integers
int n = 0;
cout<< "Enter 10 integer values"<<endl;
while (n<10)
{
cin >> a[n];
n++;
}
int item; // declare an item to search
cout<< "Enter an item to search"<<endl;
cin>>item;
for (int i=0; i<10; i++) //traverse array
{
if(item!=a[i]) // comparison
continue;
else
{
cout<< "Item "<<item<<" is found at location "<<i+1;
goto end;
}
}
cout << "Search unsuccessful: "<<item<< " is not found";
end:
getch();
return 0;
}''')
    P('Consider another program of array traversal using for loop to display those values from the array which are odd.', 'for لوپ کے ذریعے ایرے کو عبور کرنے کے ایک اور پروگرام پر غور کریں جو ایرے میں سے طاق قدریں دکھاتا ہے۔', 'د for حلقې په مرسته د لړۍ د تېرېدو بل پروګرام ته پام وکړئ چې د لړۍ طاق ارزښتونه ښيي.')
    code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
int A [] = {3, 2, 7, 5, 8};
for ( int i=0 ; i<5 ; i++ )
{
if (A[i] % 2 !=0)
cout<< A[i] << endl;
}
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''3
7
5''')
    rec = BOOK.record(t, 'cs12-u5-text-5', 'Unit 5 text (5)', 'یونٹ 5 — متن (۵)', '۵ څپرکی — متن (۵)', 83, [154, 155])
    rec['sourceNote'] = 'The top of p.154 (end of the Temperature output) is recorded with PDF82. The search program runs from p.154 to p.155 and is given whole; the book prints no output for it.'
    BOOK.save(83, [(5, rec)], issues=[{'id': 'cs12-pdf083', 'unit': 5, 'printedPage': 155,
               'description': 'Owner pen scribbles and the words “checked”/“charity” on p.155 are excluded.'}])


def p84():
    t = Builder()
    P = t.p
    t.h('5.1.7 sizeof() Operator', '5.1.7 sizeof() آپریٹر', '۵.۱.۷ sizeof() چلونکی')
    P('The sizeof() operator can be used with arrays to return the size allocated for the entire array. Consider the following program:', 'sizeof() آپریٹر ایریز کے ساتھ پورے ایرے کے لیے مختص سائز واپس کرنے کے لیے استعمال ہو سکتا ہے۔ درج ذیل پروگرام پر غور کریں:', 'sizeof() چلونکی د لړیو سره د ټولې لړۍ لپاره د ټاکل شوې اندازې د بېرته ورکولو لپاره کارول کېدای شي. لاندې پروګرام ته پام وکړئ:')
    code(t, '''// size of an array example
#include <iostream.h>
#include <conio.h>
int main()
{
int A[] = { 0, 1, 2, 3, 4 };
cout << "Size of the array A is: " <<sizeof (A); // 5 elements * 2 bytes for each element
getch();
return 0;
}''')
    P(*OUT)
    code(t, 'Size of the array A is: 10')
    P('Using the sizeof() operator, we can also find out the number of elements in an array. Consider the following example:', 'sizeof() آپریٹر کے ذریعے ہم ایرے میں عناصر کی تعداد بھی معلوم کر سکتے ہیں۔ درج ذیل مثال پر غور کریں:', 'د sizeof() چلونکي په مرسته کولی شو د لړۍ د عناصرو شمېر هم پیدا کړو. لاندې بېلګې ته پام وکړئ:')
    code(t, '''/* to find the number of elements in array using
sizeof() operator*/
# include <iostream.h>
#include <conio.h>
int main()
{
int A[] = { 0, 1, 2, 3, 4 };
cout << "Size of the array ="<<sizeof(A)<<" bytes ";
int Total_Elements = sizeof(A) / sizeof(A[0]);
cout<<"\\nTotal number of elements in the array A
are: "<<Total_Elements;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''Size of the array =10 bytes
Total number of elements in
the array A are: 05''')
    t.h('5.2 Two-dimensional arrays', '5.2 دو جہتی ایریز', '۵.۲ دوه-بعدي لړۍ')
    P('An array having more than one subscripts is called multidimensional array. A multidimensional array is an “array of arrays”. It is not limited to two indices i.e., two dimensions, but can also have three-dimensions and four-dimensions etc.',
      'ایک سے زیادہ سب اسکرپٹس والا ایرے کثیر جہتی ایرے کہلاتا ہے۔ کثیر جہتی ایرے ’’ایریز کا ایرے‘‘ ہے۔ یہ دو انڈیسز یعنی دو جہتوں تک محدود نہیں بلکہ تین جہتی اور چار جہتی وغیرہ بھی ہو سکتا ہے۔',
      'هغه لړۍ چې له یوه ډېر ښکته‌لیکونه ولري، څو-بعدي لړۍ بلل کېږي. څو-بعدي لړۍ "د لړیو لړۍ" ده. دا په دوو شاخصونو یعنې دوو بعدونو پورې محدوده نه ده، بلکې درې-بعدي او څلور-بعدي او نور هم کېدای شي.')
    t.h('5.2.1 Concept of two dimensional arrays', '5.2.1 دو جہتی ایریز کا تصور', '۵.۲.۱ د دوه-بعدي لړیو مفهوم')
    P('The most communally used multidimensional array is two dimensional arrays which is also called bi-dimensional array. It is used for storing of tabular data arranged in rows and columns. It can be represented by two indices i.e. row index and columns index.',
      'سب سے زیادہ استعمال ہونے والا کثیر جہتی ایرے دو جہتی ایرے ہے جسے bi-dimensional ایرے بھی کہتے ہیں۔ یہ قطاروں اور کالموں میں ترتیب دیے گئے جدولی ڈیٹا کو محفوظ کرنے کے لیے استعمال ہوتا ہے۔ اسے دو انڈیسز یعنی قطار انڈیکس اور کالم انڈیکس سے ظاہر کیا جا سکتا ہے۔',
      'تر ټولو ډېره کارېدونکې څو-بعدي لړۍ دوه-بعدي لړۍ ده چې bi-dimensional لړۍ هم بلل کېږي. دا په قطارونو او ستنو کې د ترتیب شوي جدولي ډېټا د ساتلو لپاره کارېږي. دا په دوو شاخصونو یعنې د قطار شاخص او د ستنې شاخص ښودل کېدای شي.')
    P('All the elements of two dimensional array are of the same data type. Consider the following array:', 'دو جہتی ایرے کے تمام عناصر ایک ہی ڈیٹا ٹائپ کے ہوتے ہیں۔ درج ذیل ایرے پر غور کریں:', 'د دوه-بعدي لړۍ ټول عناصر یو ډېټا ډول لري. لاندې لړۍ ته پام وکړئ:')
    code(t, 'int X[3][5];')
    rec = BOOK.record(t, 'cs12-u5-text-6', 'Unit 5 text (6)', 'یونٹ 5 — متن (۶)', '۵ څپرکی — متن (۶)', 84, [156, 157])
    rec['sourceNote'] = 'The second sizeof() program runs from p.156 to p.157 and is given whole; its cout string is printed broken across two lines and is kept so.'
    BOOK.save(84, [(5, rec)], issues=[{'id': 'cs12-pdf084', 'unit': 5, 'printedPage': 157,
               'description': 'p.157 “most communally used”, “two dimensional arrays which is”; the output “05” and the cout string split across lines are as printed. Retained.'}])


def p85():
    t = Builder()
    P = t.p
    P('Array X consisting of three rows and five columns. It can be represented as:', 'تین قطاروں اور پانچ کالموں پر مشتمل ایرے X۔ اسے یوں ظاہر کیا جا سکتا ہے:', 'د درېیو قطارونو او پنځو ستنو لړۍ X. داسې ښودل کېدای شي:')
    R = [['12', '-123', '58', '95', '67'], ['56', '45', '23', '45', '176'], ['78', '-56', '90', '55', '74']]
    sv = [array_2d(R, c) for c in ('Two-dimensional array X[3][5]', 'دو جہتی ایرے X[3][5]', 'دوه-بعدي لړۍ X[3][5]')]
    t.visual('cs12-fig-array-2d', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    P('Two dimensional array is also called matrix in mathematics and table in business applications.', 'دو جہتی ایرے کو ریاضی میں میٹرکس اور کاروباری ایپلیکیشنز میں ٹیبل بھی کہتے ہیں۔', 'دوه-بعدي لړۍ په ریاضي کې ماتریکس او په سوداګریزو کاريالونو کې جدول هم بلل کېږي.')
    t.h('5.2.2 Definition and initialization of two dimensional arrays', '5.2.2 دو جہتی ایریز کی تعریف اور ابتدائی قدر', '۵.۲.۲ د دوه-بعدي لړیو تعریف او لومړنی ارزښت')
    P('Like one-dimensional array, a two-dimensional array is defined and initialized before using it in a program. The following sections describe its definition and initialization with the help of examples.',
      'یک جہتی ایرے کی طرح دو جہتی ایرے کی بھی پروگرام میں استعمال سے پہلے تعریف اور ابتدائی قدر دی جاتی ہے۔ درج ذیل حصے مثالوں کی مدد سے اس کی تعریف اور ابتدائی قدر بیان کرتے ہیں۔',
      'د یو-بعدي لړۍ په څېر دوه-بعدي لړۍ هم په پروګرام کې له کارولو مخکې تعریفېږي او لومړنی ارزښت ورکول کېږي. لاندې برخې د بېلګو په مرسته د هغې تعریف او لومړنی ارزښت بیانوي.')
    t.h('a. Defining two dimensional array', 'a. دو جہتی ایرے کی تعریف', 'a. د دوه-بعدي لړۍ تعریف')
    P('The general syntax for the declaration of two dimensional arrays is given below.', 'دو جہتی ایریز کی ڈکلیریشن کا عمومی طریقۂ تحریر ذیل میں دیا گیا ہے۔', 'د دوه-بعدي لړیو د اعلان عمومي بڼه لاندې ورکړل شوې.')
    code(t, 'Data Type Array name [row index] [column index];')
    P('In the above syntax, the data type is any valid data type, such as int, float, long etc., which is followed by array name and two indices. The first index is for number of rows and the second index is for number of columns in the array.',
      'اوپر کے طریقۂ تحریر میں data type کوئی بھی درست ڈیٹا ٹائپ ہے، جیسے int، float، long وغیرہ، جس کے بعد ایرے کا نام اور دو انڈیسز آتے ہیں۔ پہلا انڈیکس قطاروں کی تعداد اور دوسرا انڈیکس ایرے میں کالموں کی تعداد کے لیے ہے۔',
      'په پورته بڼه کې data type هر سم ډېټا ډول دی، لکه int، float، long او نور، چې وروسته یې د لړۍ نوم او دوه شاخصونه راځي. لومړی شاخص د قطارونو شمېر او دویم شاخص په لړۍ کې د ستنو شمېر لپاره دی.')
    P('A float type array, tdArray, consisting of 2 rows and 2 columns can be defined by using the following statement.', 'float قسم کا ایرے tdArray، جو 2 قطاروں اور 2 کالموں پر مشتمل ہو، درج ذیل بیان سے بیان کیا جا سکتا ہے۔', 'د float ډول لړۍ tdArray چې ۲ قطارونه او ۲ ستنې ولري، په لاندې بیان تعریفېدای شي.')
    code(t, 'float tdArray [2][2];')
    t.h('b. Initializing two dimensional arrays', 'b. دو جہتی ایریز کو ابتدائی قدر دینا', 'b. دوه-بعدي لړیو ته لومړنی ارزښت ورکول')
    P('To initialize a two-dimensional array, it is easiest to use nested braces, with each set of numbers representing a row:', 'دو جہتی ایرے کو ابتدائی قدر دینے کے لیے نیسٹڈ بریسز استعمال کرنا سب سے آسان ہے، جن میں اعداد کا ہر مجموعہ ایک قطار ظاہر کرتا ہے:', 'دوه-بعدي لړۍ ته د لومړني ارزښت ورکولو لپاره ځالې لوړ قوسونه کارول تر ټولو اسانه دي، چې د عددونو هره ټولګه یو قطار ښيي:')
    code(t, '''// two dimensional array initialization
int anArray[3][5] =
{
{ 1, 2, 3, 4, 5 }, // row 0
{ 6, 7, 8, 9, 10 }, // row 1
{ 11, 12, 13, 14, 15 } // row 2
};''')
    P('If we want to initialize a two-dimensional array to 0 then it can be done as follows:', 'اگر ہم دو جہتی ایرے کو 0 ابتدائی قدر دینا چاہیں تو یوں کیا جا سکتا ہے:', 'که وغواړو دوه-بعدي لړۍ ته 0 لومړنی ارزښت ورکړو، داسې کېدای شي:')
    code(t, 'int anArray[3][5] = { 0 };')
    t.h('5.2 .3 Accessing and writing at an index in a two dimensional array', '5.2.3 دو جہتی ایرے میں کسی انڈیکس پر رسائی اور لکھنا', '۵.۲.۳ په دوه-بعدي لړۍ کې پر یوه شاخص لاسرسی او لیکل')
    P('To operate on the elements of two dimensional arrays, the elements should be first accessed and then updated. Writing at an index of an array is also done when a new two dimensional array is declared. Accessing and writing at an index of a two dimensional array is similar to one dimensional array. The following sections discuss them with the help of examples.',
      'دو جہتی ایریز کے عناصر پر عمل کرنے کے لیے پہلے عناصر تک رسائی اور پھر انھیں تازہ کرنا چاہیے۔ نیا دو جہتی ایرے ڈکلیئر کرتے وقت بھی ایرے کے کسی انڈیکس پر لکھا جاتا ہے۔ دو جہتی ایرے کے کسی انڈیکس پر رسائی اور لکھنا یک جہتی ایرے جیسا ہے۔ درج ذیل حصے مثالوں کی مدد سے ان پر بات کرتے ہیں۔',
      'د دوه-بعدي لړیو پر عناصرو د عملیې لپاره، لومړی باید عناصرو ته لاسرسی وشي او بیا تازه شي. د نوې دوه-بعدي لړۍ د اعلان پر مهال هم د لړۍ پر یوه شاخص لیکل کېږي. د دوه-بعدي لړۍ پر یوه شاخص لاسرسی او لیکل د یو-بعدي لړۍ په څېر دي. لاندې برخې د بېلګو په مرسته دا څېړي.')
    t.h('a. Accessing two dimensional arrays', 'a. دو جہتی ایریز تک رسائی', 'a. دوه-بعدي لړیو ته لاسرسی')
    P('Accessing two dimensional arrays need two indices, one for the row and the other for the column. For example, if we have an array anArray[3][5] and want to access an element at second row and third column. Then it can be written as:',
      'دو جہتی ایریز تک رسائی کے لیے دو انڈیسز درکار ہیں، ایک قطار کے لیے اور دوسرا کالم کے لیے۔ مثلاً اگر ہمارے پاس ایرے anArray[3][5] ہو اور ہم دوسری قطار اور تیسرے کالم کے عنصر تک رسائی چاہیں تو اسے یوں لکھا جا سکتا ہے:',
      'دوه-بعدي لړیو ته لاسرسی دوو شاخصونو ته اړتیا لري، یو د قطار لپاره او بل د ستنې لپاره. د بېلګې په توګه که anArray[3][5] لړۍ ولرو او د دویم قطار او درېیمې ستنې عنصر ته لاسرسی وغواړو، داسې لیکل کېدای شي:')
    code(t, 'anArray[1][2];')
    rec = BOOK.record(t, 'cs12-u5-text-7', 'Unit 5 text (7)', 'یونٹ 5 — متن (۷)', '۵ څپرکی — متن (۷)', 85, [158, 159])
    rec['sourceNote'] = 'The uncaptioned 3×5 array X diagram is reproduced as a coded diagram with a descriptive label; values as printed.'
    BOOK.save(85, [(5, rec)], issues=[{'id': 'cs12-pdf085', 'unit': 5, 'printedPage': 159,
               'description': 'Heading printed “5.2 .3”; “Accessing two dimensional arrays need two indices”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 82
    {82: p82, 83: p83, 84: p84, 85: p85}[n]()
