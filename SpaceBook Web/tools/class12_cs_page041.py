"""Computer Science XII PDF41 (spread): printed pp.70–71 — declaration examples; declaration at point of use; b. initialization of variables (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('This line of code declares three variables a, b and c, all of type int. This declaration is exactly the same as shown in the following segment of code:',
  'کوڈ کی یہ لائن تین ویری ایبلز a، b اور c کا اعلان کرتی ہے جو سب int قسم کے ہیں۔ یہ اعلان بالکل ویسا ہی ہے جیسا کوڈ کے درج ذیل حصے میں دکھایا گیا ہے:',
  'د کوډ دا کرښه درې متغیرونه a، b او c اعلانوي چې ټول د int ډول دي. دا اعلان دقیقاً هماغسې دی لکه څنګه چې د کوډ په لاندې برخه کې ښودل شوی:')
code(t, '''int a;
int b;
int c;''')
P('Consider the following example to see the use of variable declaration.', 'ویری ایبل کے اعلان کا استعمال دیکھنے کے لیے درج ذیل مثال پر غور کریں۔', 'د متغیر د اعلان د کارونې لیدلو لپاره لاندې بېلګې ته پام وکړئ.')
code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
// declaring variables:
int a, b;
int result;
// process:
a = 55;
b = 22;
result = a - b;
// print out the result:
cout << "The Result is= "<<result;
// terminate the program:
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'The Result is= 33')
P('The declaration of the variables is not necessary at the start of the program. A variable can be declared in the program where it is needed. Consider the following example.',
  'ویری ایبلز کا اعلان پروگرام کے شروع میں ضروری نہیں۔ ویری ایبل کو پروگرام میں وہاں ڈکلیئر کیا جا سکتا ہے جہاں اس کی ضرورت ہو۔ درج ذیل مثال پر غور کریں۔',
  'د متغیرونو اعلان د پروګرام په پیل کې اړین نه دی. متغیر په پروګرام کې هلته اعلانېدای شي چې ورته اړتیا وي. لاندې بېلګې ته پام وکړئ.')
code(t, '''// variables declaration at the point of application
#include<conio.h>
#include<iostream.h>
int main()
{
cout << "Enter a number: ";
int x; // we need x starting here.
cin >> x;
cout << "Enter another number: ";
int y; // we don't need y until now
cin >> y;
cout << "The sum is: " << x + y << endl;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Enter a number: 4
Enter another number: 10
The sum is: 14''')
H('b. Initialization of variables', 'b. ویری ایبلز کی ابتدائی قدر', 'b. د متغیرونو لومړنی ارزښت')
P('Assigning values to a variable during declaration time is called initialization. When declaring a regular local variable, its value is by default undetermined. But you may want a variable to store a concrete value at the same moment that it is declared. In order to do that, you can initialize the variable.',
  'اعلان کے وقت ویری ایبل کو قدر دینا ابتدائی قدر دینا (initialization) کہلاتا ہے۔ جب کوئی عام لوکل ویری ایبل ڈکلیئر کیا جاتا ہے تو اس کی قدر بطورِ طے شدہ غیر متعین ہوتی ہے۔ لیکن آپ چاہ سکتے ہیں کہ ویری ایبل اسی لمحے ایک معین قدر محفوظ کرے جب اس کا اعلان ہو۔ ایسا کرنے کے لیے آپ ویری ایبل کو ابتدائی قدر دے سکتے ہیں۔',
  'د اعلان پر وخت متغیر ته د ارزښت ورکول لومړنی ارزښت ورکول (initialization) بلل کېږي. کله چې یو عادي سیمه‌ییز متغیر اعلان شي، ارزښت یې په ډیفالټ ډول نامعلوم وي. خو کېدای شي تاسو وغواړئ چې متغیر په همغه شېبه یو ټاکلی ارزښت وساتي چې اعلانېږي. د دې لپاره تاسو متغیر ته لومړنی ارزښت ورکولی شئ.')
rec = BOOK.record(t, 'cs12-u3-text-7', 'Unit 3 text (7)', 'یونٹ 3 — متن (۷)', '۳ څپرکی — متن (۷)', 41, [70, 71])
rec['sourceNote'] = 'The initialization section continues on p.72 (PDF42).'

if __name__ == '__main__':
    BOOK.save(41, [(3, rec)])
