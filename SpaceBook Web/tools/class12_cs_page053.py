"""Computer Science XII PDF53 (spread): printed pp.94–95 — compound assignment (cont.); Table 3.5; example + output; d. increment/decrement; prefix form (segment begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('… currently stored in that variable. For example, if we want to add the value of a variable y to the value of another variable x then the following statement is used.',
  '… اس ویری ایبل میں اس وقت محفوظ ہے۔ مثال کے طور پر اگر ہم ویری ایبل y کی قدر کو دوسرے ویری ایبل x کی قدر میں جمع کرنا چاہیں تو درج ذیل بیان استعمال ہوتا ہے۔',
  '… اوس په هغه متغیر کې ساتل شوی. د بېلګې په توګه که وغواړو د y متغیر ارزښت د بل متغیر x ارزښت سره جمع کړو، نو لاندې بیان کارول کېږي.')
code(t, '''x+=y;
i.e. x=x+y;''')
P('The list of these compound assignment operators along with their use is given in the Table 3.5.', 'ان مرکب اسائنمنٹ آپریٹرز کی فہرست ان کے استعمال کے ساتھ جدول 3.5 میں دی گئی ہے۔', 'د دې مرکب د سپارلو چلونکو لېست د کارونې سره په ۳.۵ جدول کې ورکړل شوی.')
R = [(('Addition assignment', 'جمع اسائنمنٹ', 'د جمع سپارنه'), '+=', 'x += y', ('Add y to x', 'y کو x میں جمع کریں', 'y له x سره جمع کړئ')),
     (('Subtraction assignment', 'تفریق اسائنمنٹ', 'د تفریق سپارنه'), '-=', 'x -= y', ('Subtract y from x', 'x میں سے y تفریق کریں', 'y له x څخه کم کړئ')),
     (('Multiplication assignment', 'ضرب اسائنمنٹ', 'د ضرب سپارنه'), '*=', 'x *= y', ('Multiply x by y', 'x کو y سے ضرب دیں', 'x په y ضرب کړئ')),
     (('Division assignment', 'تقسیم اسائنمنٹ', 'د وېش سپارنه'), '/=', 'x /= y', ('Divide x by y', 'x کو y سے تقسیم کریں', 'x پر y ووېشئ')),
     (('Modulus assignment', 'ماڈیولس اسائنمنٹ', 'د پاتې سپارنه'), '%=', 'x %= y', ('Put the remainder of x / y in x', 'x / y کا باقی x میں رکھیں', 'د x / y پاتې برخه په x کې کېږدئ'))]
rows = lambda i: [[o[i], s, f, op[i]] for o, s, f, op in R]
t.table('cs12-table-3-5', ['Operator', 'Symbol', 'Form', 'Operation'], rows(0), ['آپریٹر', 'علامت', 'شکل', 'عمل'], ['چلونکی', 'نښه', 'بڼه', 'عملیه'], rows(1), rows(2))
P('Table 3.5: Arithmetic Assignment Operators', 'جدول 3.5: حسابی اسائنمنٹ آپریٹرز', '۳.۵ جدول: حسابي د سپارلو چلونکي')
P('Consider the following example to demonstrate the use of compound assignment operators.', 'مرکب اسائنمنٹ آپریٹرز کے استعمال کی وضاحت کے لیے درج ذیل مثال پر غور کریں۔', 'د مرکب د سپارلو چلونکو د کارونې د ښودلو لپاره لاندې بېلګې ته پام وکړئ.')
code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
int VarA, VarB=300;
VarA = VarB;
VarA +=200; // equivalent to VarA=VarA+200
cout<< "Value after addition="<<VarA;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'Value after addition=500')
H('d. Increment and decrement operators', 'd. انکریمنٹ اور ڈیکریمنٹ آپریٹرز', 'd. د زیاتولو او کمولو چلونکي')
P('These operators are also called unary arithmetic operators. These operators are used to make expressions short. The increment operator ++ and the decrement operator -- increase or decrease the value stored in a variable by 1. For example the following statements are equivalent and all perform the same operation of increasing the value of the variable ‘VarC’ by 1.',
  'ان آپریٹرز کو یونری حسابی آپریٹرز بھی کہا جاتا ہے۔ یہ آپریٹرز ایکسپریشنز کو مختصر بنانے کے لیے استعمال ہوتے ہیں۔ انکریمنٹ آپریٹر ++ اور ڈیکریمنٹ آپریٹر -- ویری ایبل میں محفوظ قدر کو 1 بڑھاتے یا گھٹاتے ہیں۔ مثلاً درج ذیل بیانات برابر ہیں اور سب ویری ایبل ‘VarC’ کی قدر 1 بڑھانے کا یکساں کام کرتے ہیں۔',
  'دې چلونکو ته یو-عملي حسابي چلونکي هم ویل کېږي. دا چلونکي د افادو د لنډولو لپاره کارول کېږي. د زیاتولو چلونکی ++ او د کمولو چلونکی -- په متغیر کې ساتل شوی ارزښت په 1 زیاتوي یا کموي. د بېلګې په توګه لاندې بیانونه برابر دي او ټول د ‘VarC’ متغیر ارزښت په 1 زیاتولو یوه عملیه کوي.')
code(t, '''VarC ++;
VarC +=1;
VarC = VarC +1;''')
P('There are two versions of each of these increment and decrement operators. These are: a prefix version and a postfix version.', 'ان انکریمنٹ اور ڈیکریمنٹ آپریٹرز میں سے ہر ایک کے دو ورژن ہیں: پری فکس ورژن اور پوسٹ فکس ورژن۔', 'د دې زیاتولو او کمولو چلونکو هر یو دوه نسخې لري: مخکینۍ (prefix) نسخه او وروستۍ (postfix) نسخه.')
H('Prefix and Postfix forms', 'پری فکس اور پوسٹ فکس شکلیں', 'مخکینۍ او وروستۍ بڼې')
P('In prefix form of the increment and decrement operators, the operators precede their operands, e.g. ++x, --z', 'انکریمنٹ اور ڈیکریمنٹ آپریٹرز کی پری فکس شکل میں آپریٹرز اپنے آپرینڈز سے پہلے آتے ہیں، مثلاً ++x، --z', 'د زیاتولو او کمولو چلونکو په مخکینۍ بڼه کې چلونکي له خپلو عملوندونو مخکې راځي، لکه ++x، --z')
P('Consider the following segment of code:', 'کوڈ کے درج ذیل حصے پر غور کریں:', 'د کوډ لاندې برخې ته پام وکړئ:')
rec = BOOK.record(t, 'cs12-u3-text-19', 'Unit 3 text (19)', 'یونٹ 3 — متن (۱۹)', '۳ څپرکی — متن (۱۹)', 53, [94, 95])
rec['sourceNote'] = 'The prefix code segment that starts at the foot of p.95 is given whole with PDF54. Table 3.5 is reproduced as a structured table.'

if __name__ == '__main__':
    BOOK.save(53, [(3, rec)])
