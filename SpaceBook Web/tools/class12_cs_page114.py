"""Computer Science XII PDF114–119: pp.216–223 Unit 7 text (7.1 pointers … 7.1.6 initialization, null pointers);
p.224 summary; pp.225–226 exercise (unit 7 complete); p.227 Unit 8 opener.
Run: python class12_cs_page114.py N (114–119)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_7_1

OUT = ('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
N = ('None of above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')


def rec(t, n, pdf, pages, note=None):
    r = BOOK.record(t, f'cs12-u7-text-{n}', f'Unit 7 text ({n})', f'یونٹ 7 — متن ({n})', f'۷ څپرکی — متن ({n})', pdf, pages)
    if note:
        r['sourceNote'] = note
    return r


def p114():
    t = Builder()
    P = t.p
    t.h('7.1 Pointers', '7.1 پوائنٹرز', '۷.۱ پوائنټرونه')
    P('Pointer is an important and powerful feature of C++ language, in which a variable points to another variable by holding its address.', 'پوائنٹر C++ زبان کی ایک اہم اور طاقتور خصوصیت ہے جس میں ایک ویری ایبل دوسرے ویری ایبل کا پتہ رکھ کر اس کی طرف اشارہ کرتا ہے۔', 'پوائنټر د C++ ژبې مهمه او پیاوړې ځانګړتیا ده چې پکې یو متغیر د بل متغیر پته ساتي او هغه ته اشاره کوي.')
    t.h('7.1.1 Pointer', '7.1.1 پوائنٹر', '۷.۱.۱ پوائنټر')
    P('A pointer is a variable that holds the address of another variable. In memory, each and every variable has an address assigned to it by the compiler and if a programmer wants to access that address, another variable called “pointer” is needed. For the declaration of pointer, an asterisk * symbol is used between the data type and the variable name.',
      'پوائنٹر ایک ویری ایبل ہے جو دوسرے ویری ایبل کا پتہ رکھتا ہے۔ میموری میں ہر ویری ایبل کو کمپائلر ایک پتہ دیتا ہے اور اگر پروگرامر اس پتے تک رسائی چاہے تو ’’پوائنٹر‘‘ نامی ایک اور ویری ایبل درکار ہوتا ہے۔ پوائنٹر کی ڈکلیریشن کے لیے ڈیٹا ٹائپ اور ویری ایبل کے نام کے درمیان ستارہ * نشان استعمال ہوتا ہے۔',
      'پوائنټر هغه متغیر دی چې د بل متغیر پته ساتي. په حافظه کې هر متغیر ته کمپایلر یوه پته ورکوي او که پروګرام جوړوونکی وغواړي هغې پتې ته لاسرسی ومومي، بل متغیر ته اړتیا ده چې "پوائنټر" بلل کېږي. د پوائنټر د اعلان لپاره د ډېټا ډول او د متغیر د نوم ترمنځ د ستوري * نښه کارېږي.')
    P('Consider the following pointers declaration of the integer variable marks, floating point variable percentage and character type variable name:', 'integer ویری ایبل marks، فلوٹنگ پوائنٹ ویری ایبل percentage اور character قسم کے ویری ایبل name کے درج ذیل پوائنٹرز ڈکلیریشن پر غور کریں:', 'د integer متغیر marks، اعشاري متغیر percentage او د character ډول متغیر name لاندې پوائنټر اعلانونو ته پام وکړئ:')
    code(t, '''int * marks;
float * percentage;
char * name;''')
    t.h('7.1.2 Memory addresses', '7.1.2 میموری پتے', '۷.۱.۲ د حافظې پتې')
    P('When writing a program, variables need to be declared. Declaration of variable is simple and its declaration tells the computer to reserve space in memory for this variable. The name of the variable refers to that memory space. This task is automatically performed by the operating system during runtime. When variables are declared, programmers store data in these variables. Computer refers to that space using an address. Therefore, everything a programmer declares has an address. It is analogous to the home address of some person. Using pointer variables, one can easily find out the address of a particular variable.',
      'پروگرام لکھتے وقت ویری ایبلز ڈکلیئر کرنے ہوتے ہیں۔ ویری ایبل کی ڈکلیریشن آسان ہے اور یہ کمپیوٹر کو اس ویری ایبل کے لیے میموری میں جگہ مختص کرنے کا کہتی ہے۔ ویری ایبل کا نام اس میموری جگہ کی طرف اشارہ کرتا ہے۔ یہ کام رن ٹائم کے دوران آپریٹنگ سسٹم خود بخود کرتا ہے۔ ویری ایبلز ڈکلیئر ہونے کے بعد پروگرامرز ان میں ڈیٹا محفوظ کرتے ہیں۔ کمپیوٹر اس جگہ کا حوالہ پتے سے دیتا ہے۔ اس لیے پروگرامر جو کچھ ڈکلیئر کرتا ہے اس کا ایک پتہ ہوتا ہے۔ یہ کسی شخص کے گھر کے پتے کی طرح ہے۔ پوائنٹر ویری ایبلز کے ذریعے کسی خاص ویری ایبل کا پتہ آسانی سے معلوم کیا جا سکتا ہے۔',
      'د پروګرام د لیکلو پر مهال متغیرونه باید اعلان شي. د متغیر اعلان اسانه دی او کمپیوټر ته وايي چې د دې متغیر لپاره په حافظه کې ځای وساتي. د متغیر نوم هغه حافظه ځای ته اشاره کوي. دا کار د اجرا پر مهال عملیاتي سیسټم پخپله ترسره کوي. کله چې متغیرونه اعلان شي، پروګرام جوړوونکي پکې ډېټا ساتي. کمپیوټر هغه ځای ته د پتې له لارې اشاره کوي. نو هر هغه څه چې پروګرام جوړوونکی یې اعلانوي، یوه پته لري. دا د یوه کس د کور پتې ته ورته ده. د پوائنټر متغیرونو په مرسته د یوه ځانګړي متغیر پته په اسانۍ موندل کېدای شي.')
    t.h('7.1.3 Reference operator &', '7.1.3 حوالہ آپریٹر &', '۷.۱.۳ د حوالې چلونکی &')
    P('As pointers are the variables which hold the addresses of other variables, therefore, while assigning addresses to them, a programmer needs a special type of operator called address-of operator that is denoted by ampersand & symbol. This provides address of a memory location.',
      'چونکہ پوائنٹرز وہ ویری ایبلز ہیں جو دوسرے ویری ایبلز کے پتے رکھتے ہیں، اس لیے انھیں پتے دیتے وقت پروگرامر کو ایک خاص قسم کے آپریٹر کی ضرورت ہوتی ہے جسے address-of آپریٹر کہتے ہیں اور جو ایمپرسینڈ & نشان سے ظاہر ہوتا ہے۔ یہ میموری مقام کا پتہ فراہم کرتا ہے۔',
      'څرنګه چې پوائنټرونه هغه متغیرونه دي چې د نورو متغیرونو پتې ساتي، نو هغوی ته د پتو ورکولو پر مهال پروګرام جوړوونکی یو ځانګړي چلونکي ته اړتیا لري چې address-of چلونکی بلل کېږي او د امپرسنډ & نښې ښودل کېږي. دا د حافظې د یوه ځای پته ورکوي.')
    P('To understand it, consider the following segment of code.', 'اسے سمجھنے کے لیے کوڈ کے درج ذیل حصے پر غور کریں۔', 'د دې د پوهېدو لپاره د کوډ لاندې برخې ته پام وکړئ.')
    code(t, '''float x = 5.5;
float *fPointer;
fPointer;= &x; // assign address of x to fPointer;''')
    P('Conceptually, the above lines of code can be pictorially represented as:', 'تصوراتی طور پر کوڈ کی اوپر کی لائنوں کو تصویری شکل میں یوں ظاہر کیا جا سکتا ہے:', 'په مفهومي توګه د کوډ پورته کرښې په انځوریز ډول داسې ښودل کېدای شي:')
    en, ur, ps, ratio = fig_7_1()
    t.visual('cs12-fig-7-1', en, ur, ps, ratio)
    P('In this pictorial representation, the variable x has a float value 5.5 that is stored at location 1000. The pointer variable fPointer points to the variable x by holding its address 1000 as its value. In this case, if we want to print the value of the variable x it will display 5.5 but if we print the value of fPointer it will display 1000.',
      'اس تصویری نمائندگی میں ویری ایبل x کی float قدر 5.5 ہے جو مقام 1000 پر محفوظ ہے۔ پوائنٹر ویری ایبل fPointer اپنی قدر کے طور پر x کا پتہ 1000 رکھ کر ویری ایبل x کی طرف اشارہ کرتا ہے۔ اس صورت میں اگر ہم ویری ایبل x کی قدر پرنٹ کریں تو 5.5 دکھائے گا لیکن اگر fPointer کی قدر پرنٹ کریں تو 1000 دکھائے گا۔',
      'په دې انځوریزه ښودنه کې x متغیر د float ارزښت 5.5 لري چې په 1000 ځای کې ساتل شوی. د پوائنټر متغیر fPointer د خپل ارزښت په توګه د x پته 1000 ساتي او x متغیر ته اشاره کوي. په دې حالت کې که د x متغیر ارزښت چاپ کړو 5.5 به ښيي، خو که د fPointer ارزښت چاپ کړو 1000 به ښيي.')
    P('Consider the following program:', 'درج ذیل پروگرام پر غور کریں:', 'لاندې پروګرام ته پام وکړئ:')
    code(t, '''/* use of pointer in a program */
#include <iostream.h>
#include<conio.h>
int main()
{
float x = 5.5;
float *fPointer;
fPointer= &x;
cout << “The address of x= "<<&x << endl;
cout<< “The value of x= "<<x<<endl;
cout << “The value of fPointer = "<< fPointer;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''The address of x= 1000
The value of x= 5.5
The value of fPointer =1000''')
    P('This program gives some other output (address) on another computer depending upon the availability of the memory.', 'یہ پروگرام میموری کی دستیابی کے مطابق کسی دوسرے کمپیوٹر پر کوئی اور آؤٹ پٹ (پتہ) دیتا ہے۔', 'دا پروګرام د حافظې د شتون سره سم په بل کمپیوټر کې بله وتنه (پته) ورکوي.')
    BOOK.save(114, [(7, rec(t, 1, 114, [216, 217, 218], 'Figure 7.1 is reproduced as a coded diagram. The pointer program begins at the foot of p.217 and continues on p.218 (PDF115); it is given whole with its output and the note that follows it. The left edge of the p.217 code is lost in the binding gutter; the first characters are supplied from the identical lines of the full program.'))],
              issues=[{'id': 'cs12-pdf114', 'unit': 7, 'printedPage': 217,
                       'description': 'The p.217 segment prints “fPointer;= &x;” with a stray semicolon; the program strings open with curly quotes. Retained as printed.'}])


def p115():
    t = Builder()
    P = t.p
    t.h('7.1.4 Dereference operator *', '7.1.4 ڈی ریفرنس آپریٹر *', '۷.۱.۴ د حوالې‌لرې کولو چلونکی *')
    P('Pointers are used to store the address of another variable. If we want to store the value of the variable through the pointer, then we need a special type of operator called dereference operator denoted by asterisk *. To use dereference operator, precede the pointer variable with asterisk * symbol. This operator can be read as “value pointed by”.',
      'پوائنٹرز دوسرے ویری ایبل کا پتہ محفوظ کرنے کے لیے استعمال ہوتے ہیں۔ اگر ہم پوائنٹر کے ذریعے ویری ایبل کی قدر محفوظ کرنا چاہیں تو ہمیں ایک خاص قسم کے آپریٹر کی ضرورت ہوتی ہے جسے ڈی ریفرنس آپریٹر کہتے ہیں اور جو ستارہ * سے ظاہر ہوتا ہے۔ ڈی ریفرنس آپریٹر استعمال کرنے کے لیے پوائنٹر ویری ایبل سے پہلے ستارہ * نشان لگائیں۔ اس آپریٹر کو ’’value pointed by‘‘ پڑھا جا سکتا ہے۔',
      'پوائنټرونه د بل متغیر د پتې د ساتلو لپاره کارېږي. که وغواړو د پوائنټر له لارې د متغیر ارزښت وساتو، نو یو ځانګړي چلونکي ته اړتیا لرو چې د حوالې‌لرې کولو (dereference) چلونکی بلل کېږي او په ستوري * ښودل کېږي. د دې چلونکي د کارولو لپاره د پوائنټر متغیر ته د ستوري * نښه مخکې ولیکئ. دا چلونکی د "value pointed by" په توګه لوستل کېدای شي.')
    P('Consider the following program to demonstrate the use of dereference operator *.', 'ڈی ریفرنس آپریٹر * کا استعمال واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د حوالې‌لرې کولو چلونکي * د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''/* use of dereference operator (*) in a program */
#include <iostream.h>
#include<conio.h>
int main()
{
int n = 100;
int *Pn; //defines a pointer to n
Pn=&n; //Pn stores the address of n
int valueN;
valueN=*Pn;
cout << “The address of n= "<<&n << endl;
cout<< “The value of n= "<<n<<endl;
cout << “The value of Pn = "<< Pn<<endl;
cout << “The value of *Pn = "<< (*Pn)<<endl;
cout << “The value of valueN = "<< valueN;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''The address of n= 0x8fc5fff4
The value of n= 100
The value of Pn = 0x8fc5fff4
The value of (*Pn) = 100
The value of valueN= 100''')
    P('In this example, the instructions at lines 10 and 14 make use of the dereference operator * and thus access the actual values of the original variable n which is pointed out by the pointer Pn. In pointers, the ampersand operator & is the reference operator and can be read as "address of" and * is the dereference operator that can be read as "value pointed by". These operators are complementary of each other and have opposite meanings. A variable referenced with & can be dereferenced with *.',
      'اس مثال میں لائن 10 اور 14 کی ہدایات ڈی ریفرنس آپریٹر * استعمال کرتی ہیں اور یوں اصل ویری ایبل n کی حقیقی قدروں تک رسائی کرتی ہیں جس کی طرف پوائنٹر Pn اشارہ کرتا ہے۔ پوائنٹرز میں ایمپرسینڈ آپریٹر & حوالہ آپریٹر ہے جسے "address of" پڑھا جا سکتا ہے اور * ڈی ریفرنس آپریٹر ہے جسے "value pointed by" پڑھا جا سکتا ہے۔ یہ آپریٹرز ایک دوسرے کے تکمیلی ہیں اور ان کے معنی متضاد ہیں۔ & سے حوالہ دیا گیا ویری ایبل * سے ڈی ریفرنس کیا جا سکتا ہے۔',
      'په دې بېلګه کې په ۱۰ او ۱۴ کرښو کې لارښوونې د حوالې‌لرې کولو چلونکی * کاروي او په دې توګه د اصلي متغیر n حقیقي ارزښتونو ته لاسرسی کوي چې Pn پوائنټر ورته اشاره کوي. په پوائنټرونو کې امپرسنډ چلونکی & د حوالې چلونکی دی او د "address of" په توګه لوستل کېدای شي او * د حوالې‌لرې کولو چلونکی دی چې د "value pointed by" په توګه لوستل کېدای شي. دا چلونکي یو د بل بشپړوونکي دي او متضادې معناوې لري. هغه متغیر چې په & حواله شوی وي، په * حواله‌لرې کېدای شي.')
    BOOK.save(115, [(7, rec(t, 2, 115, [218, 219, 220], 'The top of p.218 (end of the pointer program, output and note) is recorded with PDF114. The closing sentences of the explanation at the top of p.220 (PDF116) are given here.'))])


def p116():
    t = Builder()
    P = t.p
    t.h('7.1.5 Declaring variables of pointer types', '7.1.5 پوائنٹر اقسام کے ویری ایبلز ڈکلیئر کرنا', '۷.۱.۵ د پوائنټر ډولونو متغیرونه اعلانول')
    P('The declaration of pointer is simple and is similar to the declaration of a regular variable with a minor difference of the use of an asterisk * symbol between the data type and the variable name. Consider the following general format:', 'پوائنٹر کی ڈکلیریشن آسان ہے اور عام ویری ایبل کی ڈکلیریشن جیسی ہے، معمولی فرق یہ ہے کہ ڈیٹا ٹائپ اور ویری ایبل کے نام کے درمیان ستارہ * نشان استعمال ہوتا ہے۔ درج ذیل عمومی شکل پر غور کریں:', 'د پوائنټر اعلان اسانه دی او د عادي متغیر اعلان ته ورته دی، یوازې لږ توپیر دا دی چې د ډېټا ډول او د متغیر د نوم ترمنځ د ستوري * نښه کارېږي. لاندې عمومي بڼې ته پام وکړئ:')
    code(t, 'Data type * nameVariable;')
    P('Here, data type is the type of the value of that variable to which this pointer will point. This date type is not the type of the pointer itself but the type of the data the pointer points to. To understand it, consider the following examples of pointers declaration.',
      'یہاں data type اس ویری ایبل کی قدر کی قسم ہے جس کی طرف یہ پوائنٹر اشارہ کرے گا۔ یہ ڈیٹا ٹائپ خود پوائنٹر کی قسم نہیں بلکہ اس ڈیٹا کی قسم ہے جس کی طرف پوائنٹر اشارہ کرتا ہے۔ اسے سمجھنے کے لیے پوائنٹرز ڈکلیریشن کی درج ذیل مثالوں پر غور کریں۔',
      'دلته data type د هغه متغیر د ارزښت ډول دی چې دا پوائنټر به ورته اشاره کوي. دا ډېټا ډول د پوائنټر خپل ډول نه دی بلکې د هغه ډېټا ډول دی چې پوائنټر ورته اشاره کوي. د دې د پوهېدو لپاره د پوائنټر اعلانونو لاندې بېلګو ته پام وکړئ.')
    code(t, '''int* totalMarks;
char *Name;
float * percentage;''')
    P('In this example, three pointers totalMarks, Name and percentage are declared. Each one is intended to point to a different data type. All these pointers occupy space in memory. The first pointer points to an int, the second to a char and the last one to a float.',
      'اس مثال میں تین پوائنٹرز totalMarks، Name اور percentage ڈکلیئر کیے گئے ہیں۔ ہر ایک کا مقصد مختلف ڈیٹا ٹائپ کی طرف اشارہ کرنا ہے۔ یہ تمام پوائنٹرز میموری میں جگہ لیتے ہیں۔ پہلا پوائنٹر int کی طرف، دوسرا char کی طرف اور آخری float کی طرف اشارہ کرتا ہے۔',
      'په دې بېلګه کې درې پوائنټرونه totalMarks، Name او percentage اعلان شوي. هر یو د یوه بېل ډېټا ډول ته د اشارې لپاره دی. دا ټول پوائنټرونه په حافظه کې ځای نیسي. لومړی پوائنټر int ته، دویم char ته او وروستی float ته اشاره کوي.')
    P('It is notable that the asterisk * symbol used between the data type and the name of the variable is the indication for the pointer declaration and is not used for multiplication. There are three ways to place the asterisk. These are: placing next to the data type, the variable name, or in the middle. All these variations are shown in the above declarations of variables totalMarks, Name and percentage.',
      'قابلِ ذکر ہے کہ ڈیٹا ٹائپ اور ویری ایبل کے نام کے درمیان استعمال ہونے والا ستارہ * نشان پوائنٹر ڈکلیریشن کی علامت ہے اور ضرب کے لیے استعمال نہیں ہوتا۔ ستارہ رکھنے کے تین طریقے ہیں: ڈیٹا ٹائپ کے ساتھ، ویری ایبل کے نام کے ساتھ یا درمیان میں۔ یہ تمام صورتیں ویری ایبلز totalMarks، Name اور percentage کی اوپر کی ڈکلیریشنز میں دکھائی گئی ہیں۔',
      'د یادونې وړ ده چې د ډېټا ډول او د متغیر د نوم ترمنځ کارېدونکې د ستوري * نښه د پوائنټر د اعلان نښه ده او د ضرب لپاره نه کارېږي. د ستوري د ایښودلو درې لارې دي: د ډېټا ډول تر څنګ، د متغیر د نوم تر څنګ، یا په منځ کې. دا ټول بڼې د totalMarks، Name او percentage متغیرونو په پورته اعلانونو کې ښودل شوې.')
    P('A pointer of type int can only points to a variable of type int and cannot to some other type of variable. Same is the case for other data types as well, but, there is a special type of pointer named void pointer or generic pointer that can point to an objects of any data type. Its declaration is similar to the declaration of normal pointers with the only difference of the use of void keyword as the pointer’s type. Consider the following statement of declaration of the void pointer:',
      'int قسم کا پوائنٹر صرف int قسم کے ویری ایبل کی طرف اشارہ کر سکتا ہے، کسی اور قسم کے ویری ایبل کی طرف نہیں۔ دوسری ڈیٹا ٹائپس کا بھی یہی حال ہے، لیکن ایک خاص قسم کا پوائنٹر ہے جسے void پوائنٹر یا عمومی پوائنٹر کہتے ہیں جو کسی بھی ڈیٹا ٹائپ کی شے کی طرف اشارہ کر سکتا ہے۔ اس کی ڈکلیریشن عام پوائنٹرز جیسی ہے، فرق صرف یہ ہے کہ پوائنٹر کی قسم کے طور پر void کلیدی لفظ استعمال ہوتا ہے۔ void پوائنٹر کی ڈکلیریشن کے درج ذیل بیان پر غور کریں:',
      'د int ډول پوائنټر یوازې د int ډول متغیر ته اشاره کولی شي، د بل ډول متغیر ته نه. د نورو ډېټا ډولونو حالت هم همداسې دی، خو یو ځانګړی پوائنټر شته چې void پوائنټر یا عمومي پوائنټر بلل کېږي او د هر ډېټا ډول شي ته اشاره کولی شي. اعلان یې د عادي پوائنټرونو اعلان ته ورته دی، یوازینی توپیر دا دی چې د پوائنټر د ډول په توګه void کلیدي کلمه کارېږي. د void پوائنټر د اعلان لاندې بیان ته پام وکړئ:')
    code(t, 'void *pointerVoid; // pointerVoid is a void pointer')
    P('As, a void pointer can point to objects of any data type, therefore, consider the following statements.', 'چونکہ void پوائنٹر کسی بھی ڈیٹا ٹائپ کی اشیا کی طرف اشارہ کر سکتا ہے، اس لیے درج ذیل بیانات پر غور کریں۔', 'څرنګه چې void پوائنټر د هر ډېټا ډول شیانو ته اشاره کولی شي، نو لاندې بیانونو ته پام وکړئ.')
    code(t, '''int X;
float Y;
void *pointerVoid;
pointerVoid = &X; // valid
pointerVoid = &Y; // valid''')
    P('In this segment of code, pointerVoid, stores the address of both integer variable X and floating point variable Y. The compiler decides at run time that the address of which type of variable should be assigned to this pointer.',
      'کوڈ کے اس حصے میں pointerVoid، integer ویری ایبل X اور فلوٹنگ پوائنٹ ویری ایبل Y دونوں کا پتہ محفوظ کرتا ہے۔ کمپائلر رن ٹائم پر فیصلہ کرتا ہے کہ اس پوائنٹر کو کس قسم کے ویری ایبل کا پتہ دیا جائے۔',
      'د کوډ په دې برخه کې pointerVoid د integer متغیر X او د اعشاري متغیر Y دواړو پته ساتي. کمپایلر د اجرا پر مهال پرېکړه کوي چې دې پوائنټر ته د کوم ډول متغیر پته ورکړل شي.')
    t.h('7.1.6 Pointer initialization', '7.1.6 پوائنٹر کو ابتدائی قدر دینا', '۷.۱.۶ پوائنټر ته لومړنی ارزښت ورکول')
    P('Assigning values to pointers at declaration time is called pointer initialization. As we know that the values of pointers are the addresses of other variables, therefore, sometimes when we declare pointers we may want to explicitly specify to which variables they will point.',
      'ڈکلیریشن کے وقت پوائنٹرز کو قدریں دینا پوائنٹر انیشیلائزیشن کہلاتا ہے۔ جیسا کہ ہم جانتے ہیں کہ پوائنٹرز کی قدریں دوسرے ویری ایبلز کے پتے ہوتی ہیں، اس لیے بعض اوقات پوائنٹرز ڈکلیئر کرتے وقت ہم واضح طور پر بتانا چاہتے ہیں کہ وہ کن ویری ایبلز کی طرف اشارہ کریں گے۔',
      'د اعلان پر مهال پوائنټرونو ته د ارزښتونو ورکول د پوائنټر لومړنی ارزښت ورکول بلل کېږي. لکه څنګه چې پوهېږو چې د پوائنټرونو ارزښتونه د نورو متغیرونو پتې دي، نو کله کله د پوائنټرونو د اعلان پر مهال غواړو په ښکاره وټاکو چې کومو متغیرونو ته به اشاره کوي.')
    P('Consider the following segment of code to understand the concept of pointer initialization:', 'پوائنٹر انیشیلائزیشن کا تصور سمجھنے کے لیے کوڈ کے درج ذیل حصے پر غور کریں:', 'د پوائنټر د لومړني ارزښت ورکولو د مفهوم د پوهېدو لپاره د کوډ لاندې برخې ته پام وکړئ:')
    code(t, '''float Temperature;
float *PTemperature = &Temperature;''')
    BOOK.save(116, [(7, rec(t, 3, 116, [220, 221, 222], 'The opening sentences of p.220 are recorded with PDF115. The initialization segment at the top of p.222 (PDF117) is given here.'))],
              issues=[{'id': 'cs12-pdf116', 'unit': 7, 'printedPage': 220,
                       'description': 'p.220 “This date type is not the type of the pointer”; p.221 “can only points to”, “point to an objects of any data type”, and the claim that the compiler decides “at run time”. Retained as printed.'}])


def p117():
    t = Builder()
    P = t.p
    P('Here, PTemperature is a pointer variable to a floating point variable. As this pointer is created with the statement ‘float *PTemperature’, immediately the address of a float variable ‘Temperature’ is assigned to it. The behavior of the above code is being equivalent to the following code.',
      'یہاں PTemperature ایک فلوٹنگ پوائنٹ ویری ایبل کا پوائنٹر ویری ایبل ہے۔ جیسے ہی یہ پوائنٹر بیان ‘float *PTemperature’ سے بنتا ہے، اسے فوراً float ویری ایبل ‘Temperature’ کا پتہ دے دیا جاتا ہے۔ اوپر کے کوڈ کا رویہ درج ذیل کوڈ کے مساوی ہے۔',
      'دلته PTemperature د یوه اعشاري متغیر لپاره د پوائنټر متغیر دی. کله چې دا پوائنټر د ‘float *PTemperature’ بیان سره جوړ شي، سمدستي د float متغیر ‘Temperature’ پته ورکول کېږي. د پورته کوډ چلند د لاندې کوډ سره برابر دی.')
    code(t, '''float Temperature;
float *PTemperature;
PTemperature = &Temperature;''')
    P('It should be considered that at the moment of declaring a pointer, the asterisk * indicates that it is a pointer variable and not the dereference operator.', 'یہ بات ذہن میں رہنی چاہیے کہ پوائنٹر ڈکلیئر کرتے وقت ستارہ * ظاہر کرتا ہے کہ یہ پوائنٹر ویری ایبل ہے، ڈی ریفرنس آپریٹر نہیں۔', 'باید په پام کې وي چې د پوائنټر د اعلان پر مهال ستوری * ښيي چې دا د پوائنټر متغیر دی نه د حوالې‌لرې کولو چلونکی.')
    P('Consider the following program to explain the concept of pointer initialization.', 'پوائنٹر انیشیلائزیشن کا تصور واضح کرنے کے لیے درج ذیل پروگرام پر غور کریں۔', 'د پوائنټر د لومړني ارزښت ورکولو د مفهوم د تشریح لپاره لاندې پروګرام ته پام وکړئ.')
    code(t, '''/* pointer initialization program */
#include <iostream.h>
#include<conio.h>
int main()
{
float Temperature;
float *PTemperature = &Temperature;
cout << “The address of Temperature is = "
<<&Temperature << endl;
cout<< “The value of *PTemperature is = "
<< PTemperature <<endl;
getch();
return 0;
}''')
    P(*OUT)
    code(t, '''The address of Temperature is = 0x8f98fff2
The value of PTemperature is = 0x8f98fff2''')
    P('Here, the pointer PTemperature is initialized with the address of the variable Temperature.', 'یہاں پوائنٹر PTemperature کو ویری ایبل Temperature کے پتے سے ابتدائی قدر دی گئی ہے۔', 'دلته PTemperature پوائنټر ته د Temperature متغیر پته د لومړني ارزښت په توګه ورکړل شوې.')
    P('Sometimes we need to initialize a pointer to zero. Such pointers are called null pointers and they do not point to anything. Null pointers can be defined by assigning address 0 to them.', 'بعض اوقات ہمیں پوائنٹر کو صفر ابتدائی قدر دینی ہوتی ہے۔ ایسے پوائنٹرز null پوائنٹرز کہلاتے ہیں اور کسی چیز کی طرف اشارہ نہیں کرتے۔ null پوائنٹرز کو پتہ 0 دے کر بیان کیا جا سکتا ہے۔', 'کله کله اړتیا لرو چې پوائنټر ته صفر لومړنی ارزښت ورکړو. داسې پوائنټرونه null پوائنټرونه بلل کېږي او هېڅ شي ته اشاره نه کوي. null پوائنټرونه د 0 پتې په ورکولو تعریفېدای شي.')
    P('Consider the following initialization to demonstrate null pointer:', 'null پوائنٹر واضح کرنے کے لیے درج ذیل انیشیلائزیشن پر غور کریں:', 'د null پوائنټر د ښودلو لپاره لاندې لومړني ارزښت ورکولو ته پام وکړئ:')
    code(t, '''int *NPtr; //defines Null pointer
NPtr = 0; // this assigns address 0 to NPtr''')
    P('The use of NULL pointers is mostly done in dynamic memory allocation.', 'NULL پوائنٹرز کا استعمال زیادہ تر ڈائنامک میموری ایلوکیشن میں ہوتا ہے۔', 'د NULL پوائنټرونو کارونه ډېری په متحرکه حافظه وېش کې کېږي.')
    BOOK.save(117, [(7, rec(t, 4, 117, [222, 223], 'The initialization segment at the top of p.222 is recorded with PDF116. The program ends at the top of p.223 and is given whole.'))],
              issues=[{'id': 'cs12-pdf117', 'unit': 7, 'printedPage': 223,
                       'description': 'The program prints the label “The value of *PTemperature is = ” but the output line reads “The value of PTemperature is =”; “is being equivalent to”. Retained as printed.'}])


def p118():
    s = Builder()
    s.h('Summary', 'خلاصہ', 'لنډیز')
    s.group('list', [
     ('A pointer is a variable that points to or refers to another variable. That is, if we have a pointer variable of type “pointer to int” it might point to the int variable.', 'پوائنٹر ایک ویری ایبل ہے جو دوسرے ویری ایبل کی طرف اشارہ یا حوالہ دیتا ہے۔ یعنی اگر ہمارے پاس ’’pointer to int‘‘ قسم کا پوائنٹر ویری ایبل ہو تو یہ int ویری ایبل کی طرف اشارہ کر سکتا ہے۔', 'پوائنټر هغه متغیر دی چې بل متغیر ته اشاره یا حواله کوي. یعنې که د "pointer to int" ډول پوائنټر متغیر ولرو، کېدای شي int متغیر ته اشاره وکړي.'),
     ('Some tasks in C++ are easier to do with pointers, such as accessing the addresses of variables indirectly and operating their values.', 'C++ میں کچھ کام پوائنٹرز سے کرنا آسان ہوتے ہیں، جیسے ویری ایبلز کے پتوں تک بالواسطہ رسائی اور ان کی قدروں پر عمل کرنا۔', 'په C++ کې ځینې کارونه د پوائنټرونو سره اسانه دي، لکه د متغیرونو پتو ته نامستقیم لاسرسی او د هغو پر ارزښتونو عملیه.'),
     ('Like normal variables, Pointer variables are also declared in programs before using them. To declare a pointer variable, the data type of the variable is followed by * symbol.', 'عام ویری ایبلز کی طرح پوائنٹر ویری ایبلز بھی استعمال سے پہلے پروگراموں میں ڈکلیئر کیے جاتے ہیں۔ پوائنٹر ویری ایبل ڈکلیئر کرنے کے لیے ویری ایبل کی ڈیٹا ٹائپ کے بعد * نشان آتا ہے۔', 'د عادي متغیرونو په څېر د پوائنټر متغیرونه هم په پروګرامونو کې له کارولو مخکې اعلانېږي. د پوائنټر متغیر د اعلان لپاره د متغیر ډېټا ډول وروسته * نښه راځي.'),
     ('While using pointers in C++ programs, address-of-operator denoted by ampersand & symbol is used to assign the address of variables to the pointer variable.', 'C++ پروگراموں میں پوائنٹرز استعمال کرتے وقت ایمپرسینڈ & نشان سے ظاہر ہونے والا address-of آپریٹر پوائنٹر ویری ایبل کو ویری ایبلز کا پتہ دینے کے لیے استعمال ہوتا ہے۔', 'په C++ پروګرامونو کې د پوائنټرونو د کارولو پر مهال د امپرسنډ & نښې ښودل شوی address-of چلونکی د پوائنټر متغیر ته د متغیرونو د پتې ورکولو لپاره کارېږي.'),
     ('In C++ program, if we want to use the value of the variable to which pointer points a special type of operator called dereference operator, denoted by asterisk *; is used with pointers.', 'C++ پروگرام میں اگر ہم اس ویری ایبل کی قدر استعمال کرنا چاہیں جس کی طرف پوائنٹر اشارہ کرتا ہے تو پوائنٹرز کے ساتھ ستارہ * سے ظاہر ہونے والا ایک خاص آپریٹر یعنی ڈی ریفرنس آپریٹر استعمال ہوتا ہے۔', 'په C++ پروګرام کې که وغواړو د هغه متغیر ارزښت وکاروو چې پوائنټر ورته اشاره کوي، د پوائنټرونو سره یو ځانګړی چلونکی چې د حوالې‌لرې کولو چلونکی بلل کېږي او په ستوري * ښودل کېږي، کارېږي.'),
     ('In C++ programs, pointers are initialized to addresses of other variables like the initialization of ordinary variables.', 'C++ پروگراموں میں پوائنٹرز کو عام ویری ایبلز کی ابتدائی قدر کی طرح دوسرے ویری ایبلز کے پتوں سے ابتدائی قدر دی جاتی ہے۔', 'په C++ پروګرامونو کې پوائنټرونو ته د عادي متغیرونو د لومړني ارزښت په څېر د نورو متغیرونو پتې ورکول کېږي.')])
    sm = BOOK.record(s, 'cs12-u7-summary', 'Unit 7 summary', 'یونٹ 7: خلاصہ', '۷ څپرکی: لنډیز', 118, [224])
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. Pointers are special type of variable that store ________ of other variables.', 'i. پوائنٹرز خاص قسم کے ویری ایبلز ہیں جو دوسرے ویری ایبلز کا ________ محفوظ کرتے ہیں۔', 'i. پوائنټرونه ځانګړي ډول متغیرونه دي چې د نورو متغیرونو ________ ساتي.'),
     ('ii. If we have a statement int n; and we want to define a pointer to n then its data type must be of the type ________ .', 'ii. اگر ہمارے پاس بیان int n; ہو اور ہم n کا پوائنٹر بیان کرنا چاہیں تو اس کی ڈیٹا ٹائپ ________ ہونی چاہیے۔', 'ii. که موږ int n; بیان ولرو او وغواړو n ته پوائنټر تعریف کړو، نو ډېټا ډول یې باید ________ وي.'),
     ('iii. Assigning values to a pointer during its declaration time is called ________ .', 'iii. ڈکلیریشن کے وقت پوائنٹر کو قدریں دینا ________ کہلاتا ہے۔', 'iii. د اعلان پر مهال پوائنټر ته د ارزښتونو ورکول ________ بلل کېږي.'),
     ('iv. & is the ________ operator.', 'iv. & ________ آپریٹر ہے۔', 'iv. & د ________ چلونکی دی.'),
     ('v. * is the ________ operator which can be read as "value pointed by" operator.', 'v. * ________ آپریٹر ہے جسے "value pointed by" آپریٹر پڑھا جا سکتا ہے۔', 'v. * د ________ چلونکی دی چې د "value pointed by" چلونکي په توګه لوستل کېدای شي.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    e.mcq('i.', ('If we have the statement int *Ptr; then to what Ptr point?', 'اگر ہمارے پاس بیان int *Ptr; ہو تو Ptr کس کی طرف اشارہ کرتا ہے؟', 'که موږ int *Ptr; بیان ولرو، نو Ptr څه ته اشاره کوي؟'),
          [('Points to an integer type variable', 'integer قسم کے ویری ایبل کی طرف', 'د integer ډول متغیر ته'), ('Points to a character type variable', 'character قسم کے ویری ایبل کی طرف', 'د character ډول متغیر ته'), ('Points to a floating point type variable', 'فلوٹنگ پوائنٹ قسم کے ویری ایبل کی طرف', 'د اعشاري ډول متغیر ته'), N], per_line=1)
    e.mcq('ii.', ('A pointer is:', 'پوائنٹر ہے:', 'پوائنټر دی:'),
          [('A keyword used to create variables', 'ویری ایبلز بنانے کے لیے استعمال ہونے والا کلیدی لفظ', 'د متغیرونو د جوړولو لپاره کارېدونکې کلیدي کلمه'), ('A variable that stores address of an instruction', 'ایک ویری ایبل جو کسی ہدایت کا پتہ محفوظ کرتا ہے', 'هغه متغیر چې د یوې لارښوونې پته ساتي'),
           ('A variable that stores address of another variable', 'ایک ویری ایبل جو دوسرے ویری ایبل کا پتہ محفوظ کرتا ہے', 'هغه متغیر چې د بل متغیر پته ساتي'), ('All of the above', 'مندرجہ بالا سب', 'پورته ټول')], per_line=1)
    e.mcq('iii.', ('The operator used to get value at address stored in a pointer variable is', 'پوائنٹر ویری ایبل میں محفوظ پتے پر قدر حاصل کرنے کے لیے استعمال ہونے والا آپریٹر ہے', 'هغه چلونکی چې په پوائنټر متغیر کې ساتل شوې پته کې ارزښت ترلاسه کوي'), ['*', '&', '&&', '||'], per_line=1)
    e.p('iv. Which of the statements is correct about the following segment code?', 'iv. کوڈ کے درج ذیل حصے کے بارے میں کون سا بیان درست ہے؟', 'iv. د کوډ د لاندې برخې په اړه کوم بیان سم دی؟')
    code(e, '''int i=10;
int *j=&i;''')
    e.group('lines', [('(a) j and i are pointers to an int', '(a) j اور i دونوں int کے پوائنٹرز ہیں', '(a) j او i دواړه int ته پوائنټرونه دي'), ('(b) i is a pointer to an int and stores address of j', '(b) i ایک int کا پوائنٹر ہے اور j کا پتہ محفوظ کرتا ہے', '(b) i یو int ته پوائنټر دی او د j پته ساتي'),
                      ('(c) j is a pointer to an int and stores address of i', '(c) j ایک int کا پوائنٹر ہے اور i کا پتہ محفوظ کرتا ہے', '(c) j یو int ته پوائنټر دی او د i پته ساتي'), ('(d) j is a pointer to a pointer to an int and stores address of i', '(d) j ایک int کے پوائنٹر کا پوائنٹر ہے اور i کا پتہ محفوظ کرتا ہے', '(d) j د int پوائنټر ته پوائنټر دی او د i پته ساتي')])
    e.mcq('v.', ('In pointers, dereference operator * is used to:', 'پوائنٹرز میں ڈی ریفرنس آپریٹر * استعمال ہوتا ہے:', 'په پوائنټرونو کې د حوالې‌لرې کولو چلونکی * کارېږي:'),
          [('Address the value of the pointer variable.', 'پوائنٹر ویری ایبل کی قدر کا پتہ دینے کے لیے', 'د پوائنټر متغیر ارزښت ته پته ورکولو لپاره'), ('Points to the value stored in the variable pointed by the pointer variable', 'پوائنٹر ویری ایبل کی طرف سے اشارہ کردہ ویری ایبل میں محفوظ قدر کی طرف اشارہ کرنے کے لیے', 'هغه ارزښت ته اشاره چې د پوائنټر متغیر په اشاره شوي متغیر کې ساتل شوی'),
           ('Both a and b', 'a اور b دونوں', 'a او b دواړه'), ('None of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')], per_line=1)
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. The statement int *ptr; defines an ordinary C++ variable.', 'i. بیان int *ptr; ایک عام C++ ویری ایبل بیان کرتا ہے۔', 'i. int *ptr; بیان یو عادي C++ متغیر تعریفوي.'),
     ('ii. The following lines of codes assign the value of the variable Temp to the pointer variable PTemp.', 'ii. کوڈ کی درج ذیل لائنیں ویری ایبل Temp کی قدر پوائنٹر ویری ایبل PTemp کو دیتی ہیں۔', 'ii. د کوډ لاندې کرښې د Temp متغیر ارزښت د PTemp پوائنټر متغیر ته ورکوي.')])
    code(e, '''float Temp;
float *PTemp = &Temp;''')
    e.group('lines', [
     ('iii. Pointer variables can be initialized by addresses of the variables to which they refer.', 'iii. پوائنٹر ویری ایبلز کو ان ویری ایبلز کے پتوں سے ابتدائی قدر دی جا سکتی ہے جن کی طرف وہ اشارہ کرتے ہیں۔', 'iii. د پوائنټر متغیرونو ته د هغو متغیرونو پتې لومړنی ارزښت ورکول کېدای شي چې ورته اشاره کوي.'),
     ('iv. To assign addresses to pointers, a programmer needs a special type of operator called address-of-operator &.', 'iv. پوائنٹرز کو پتے دینے کے لیے پروگرامر کو address-of-operator & نامی خاص آپریٹر کی ضرورت ہوتی ہے۔', 'iv. پوائنټرونو ته د پتو ورکولو لپاره پروګرام جوړوونکی د address-of-operator & په نوم ځانګړي چلونکي ته اړتیا لري.'),
     ('v. When a variable is declared in C++, the compiler reserves location for this variable in computer memory to store data.', 'v. جب C++ میں ویری ایبل ڈکلیئر کیا جاتا ہے تو کمپائلر ڈیٹا محفوظ کرنے کے لیے کمپیوٹر میموری میں اس ویری ایبل کے لیے مقام مختص کرتا ہے۔', 'v. کله چې په C++ کې یو متغیر اعلان شي، کمپایلر د ډېټا د ساتلو لپاره د کمپیوټر په حافظه کې د دې متغیر لپاره ځای ساتي.')])
    for q, en, ur, ps in [
        ('Q.4', 'Define the term pointer. Describe the advantages of using pointer variables.', 'پوائنٹر کی اصطلاح کی تعریف کریں۔ پوائنٹر ویری ایبلز کے استعمال کے فوائد بیان کریں۔', 'د پوائنټر اصطلاح تعریف کړئ. د پوائنټر متغیرونو د کارونې ګټې بیان کړئ.'),
        ('Q.5', 'What is the difference between the dereference operator * and reference operator &? Explain with the help of some lines of code.', 'ڈی ریفرنس آپریٹر * اور حوالہ آپریٹر & میں کیا فرق ہے؟ کوڈ کی چند لائنوں کی مدد سے وضاحت کریں۔', 'د حوالې‌لرې کولو چلونکي * او د حوالې چلونکي & ترمنځ څه توپیر دی؟ د کوډ د څو کرښو په مرسته یې تشریح کړئ.'),
        ('Q.6', 'What is meant by the term pointer initialization? Write a simple program to illustrate this concept.', 'پوائنٹر انیشیلائزیشن کی اصطلاح سے کیا مراد ہے؟ اس تصور کی وضاحت کے لیے ایک سادہ پروگرام لکھیں۔', 'د پوائنټر د لومړني ارزښت ورکولو اصطلاح څه معنا لري؟ د دې مفهوم د ښودلو لپاره یو ساده پروګرام ولیکئ.'),
        ('Q.7', 'How the declaration of a pointer variable is different from the declaration of a variable.', 'پوائنٹر ویری ایبل کی ڈکلیریشن عام ویری ایبل کی ڈکلیریشن سے کیسے مختلف ہے۔', 'د پوائنټر متغیر اعلان د یوه متغیر له اعلان څخه څنګه توپیر لري.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    ex = BOOK.record(e, 'cs12-u7-exercise', 'Unit 7 exercise', 'یونٹ 7: مشق', '۷ څپرکی: تمرین', 118, [225, 226])
    ex['sourceNote'] = 'The exercise runs from p.225 to p.226 (PDF119) and is recorded here whole.'
    BOOK.save(118, [(7, sm), (7, ex)], issues=[{'id': 'cs12-pdf118', 'unit': 7, 'printedPage': 225,
               'description': 'Q2(i) “then to what Ptr point?”; Q2(iv) “segment code”; Q3(ii) “lines of codes”; Q7 ends with a full stop instead of a question mark. Retained as printed.'}])


def p119():
    t = Builder()
    t.p('Unit 8', 'یونٹ 8', '۸ څپرکی')
    t.h('OBJECTS AND CLASSES', 'آبجیکٹس اور کلاسز', 'شیان او ټولګي')
    t.h('After the completion of Unit-8, Students will be able to:', 'یونٹ 8 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۸ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    L = lambda *x: t.group('list', list(x))
    L(('Define class and object', 'کلاس اور آبجیکٹ کی تعریف کر سکیں', 'ټولګی او شی تعریف کړي'), ('Know the members of class:', 'کلاس کے اراکین جان سکیں:', 'د ټولګي غړي وپېژني:'))
    L(('Data', 'ڈیٹا', 'ډېټا'), ('Functions', 'فنکشنز', 'فنکشنونه'))
    L(('iii. Understand an access specifiers:', 'iii. ایکسس اسپیسیفائرز سمجھ سکیں:', 'iii. د لاسرسي ټاکونکي وپوهېږي:'))
    L(('Private', 'پرائیویٹ', 'شخصي (Private)'), ('Public', 'پبلک', 'عامه (Public)'))
    L(('Know the concept of data hiding', 'ڈیٹا ہائیڈنگ کا تصور جان سکیں', 'د ډېټا د پټولو مفهوم وپېژني'), ('Define constructor and destructor', 'کنسٹرکٹر اور ڈسٹرکٹر کی تعریف کر سکیں', 'جوړوونکی او ړنګوونکی تعریف کړي'))
    L(('Default constructor/destructor', 'ڈیفالٹ کنسٹرکٹر/ڈسٹرکٹر', 'ډیفالټ جوړوونکی/ړنګوونکی'), ('Users-defined constructor', 'یوزر ڈیفائنڈ کنسٹرکٹر', 'د کاروونکي-تعریف شوی جوړوونکی'), ('Constructors overloading', 'کنسٹرکٹرز اوورلوڈنگ', 'د جوړوونکو ډېرول'))
    L(('Declare objects to access', 'رسائی کے لیے آبجیکٹس ڈکلیئر کر سکیں', 'د لاسرسي لپاره شیان اعلان کړي'))
    L(('Data members', 'ڈیٹا ممبرز', 'د ډېټا غړي'), ('Member functions', 'ممبر فنکشنز', 'غړي فنکشنونه'))
    L(('Understand the concept of the following with daily life examples:', 'روزمرہ زندگی کی مثالوں سے درج ذیل کا تصور سمجھ سکیں:', 'د ورځني ژوند د بېلګو په مرسته د لاندې مفهوم وپوهېږي:'))
    L(('Inheritance', 'وراثت (Inheritance)', 'میراث (Inheritance)'), ('Polymorphism', 'پولی مورفزم', 'پولي‌مورفیزم'))
    rec8 = BOOK.record(t, 'cs12-u8-outcomes', 'Unit 8: learning outcomes', 'یونٹ 8: حاصلاتِ تعلم', '۸ څپرکی: د زده‌کړې پایلې', 119, [227],
                       unit_title=('Objects and Classes', 'آبجیکٹس اور کلاسز', 'شیان او ټولګي'))
    BOOK.save(119, [(8, rec8)], complete_units=[7], issues=[{'id': 'cs12-pdf119', 'unit': 8, 'printedPage': 227,
               'description': 'Outcomes list prints “iii. Understand an access specifiers” (stray numeral) and “Users-defined constructor”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 114
    {114: p114, 115: p115, 116: p116, 117: p117, 118: p118, 119: p119}[n]()
