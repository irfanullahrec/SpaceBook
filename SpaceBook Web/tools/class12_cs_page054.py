"""Computer Science XII PDF54 (spread): printed pp.96–97 — prefix segment (from p.95) + output; postfix; increment/decrement program; e. relational operators (Table 3.8); f. logical operators (Table 3.9)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
code(t, '''// Prefix Increment and Decrement Operators
int x = 5;
cout<< "increment in prefix form ="<<++x;
cout<< "decrement in prefix form ="<<--x;''')
P('Output of the Segment', 'حصے کا آؤٹ پٹ', 'د برخې وتنه')
code(t, '''increment in prefix form =6
decrement in prefix form =4''')
P('In postfix form of the increment and decrement operators, the operands precede their operators, e.g. x++, z--',
  'انکریمنٹ اور ڈیکریمنٹ آپریٹرز کی پوسٹ فکس شکل میں آپرینڈز اپنے آپریٹرز سے پہلے آتے ہیں، مثلاً x++، z--',
  'د زیاتولو او کمولو چلونکو په وروستۍ بڼه کې عملوندونه له خپلو چلونکو مخکې راځي، لکه x++، z--')
P('Consider the following program to demonstrate the use of increment and decrement operators.', 'انکریمنٹ اور ڈیکریمنٹ آپریٹرز کے استعمال کی وضاحت کے لیے درج ذیل پروگرام پر غور کریں۔', 'د زیاتولو او کمولو چلونکو د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
code(t, '''// increment and Decrement Operators
#include<iostream.h>
#include<conio.h>
int main()
{
int x = 25, y = 25;
cout<< x << " " << y <<endl;
cout<< ++x << " " << --y <<endl; // prefix
cout<< x << " " << y <<endl;
cout<< x++ << " " << y-- <<endl; // postfix
cout<< x << " " << y <<endl;
getch();
return 0;
}''')
P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''25 25
26 24
26 24
26 24
27 23''')
H('e. Relational operators', 'e. ریلیشنل آپریٹرز', 'e. اړیکه‌ییز چلونکي')
P('Relational operators are used for the comparison between two expressions. These operators are: ==, !=, >, >=, <, <=. The result of these operators can be either true or false. The list of all relational operators used in C++ is given in Table 3.8.',
  'ریلیشنل آپریٹرز دو ایکسپریشنز کے درمیان موازنے کے لیے استعمال ہوتے ہیں۔ یہ آپریٹرز ہیں: ==، !=، >، >=، <، <=۔ ان آپریٹرز کا نتیجہ true یا false ہو سکتا ہے۔ C++ میں استعمال ہونے والے تمام ریلیشنل آپریٹرز کی فہرست جدول 3.8 میں دی گئی ہے۔',
  'اړیکه‌ییز چلونکي د دوو افادو ترمنځ د پرتلې لپاره کارول کېږي. دا چلونکي دا دي: ==، !=، >، >=، <، <=. د دې چلونکو پایله کېدای شي true یا false وي. په C++ کې د کارېدونکو ټولو اړیکه‌ییزو چلونکو لېست په ۳.۸ جدول کې ورکړل شوی.')
REL = [(('Greater than', 'سے بڑا', 'لوی تر'), '>', 'x > y', ('true if x is greater than y, false otherwise', 'اگر x، y سے بڑا ہو تو true، ورنہ false', 'که x له y لوی وي true، که نه false')),
       (('Less than', 'سے چھوٹا', 'کوچنی تر'), '<', 'x < y', ('true if x is less than y, false otherwise', 'اگر x، y سے چھوٹا ہو تو true، ورنہ false', 'که x له y کوچنی وي true، که نه false')),
       (('Greater than or equals', 'سے بڑا یا برابر', 'لوی یا برابر'), '>=', 'x >= y', ('true if x is greater than or equal to y, false otherwise', 'اگر x، y سے بڑا یا برابر ہو تو true، ورنہ false', 'که x له y لوی یا ورسره برابر وي true، که نه false')),
       (('Less than or equals', 'سے چھوٹا یا برابر', 'کوچنی یا برابر'), '<=', 'x <= y', ('true if x is less than or equal to y, false otherwise', 'اگر x، y سے چھوٹا یا برابر ہو تو true، ورنہ false', 'که x له y کوچنی یا ورسره برابر وي true، که نه false')),
       (('Equality', 'مساوات', 'برابري'), '==', 'x == y', ('true if x equals y, false otherwise', 'اگر x، y کے برابر ہو تو true، ورنہ false', 'که x له y سره برابر وي true، که نه false')),
       (('Inequality', 'عدم مساوات', 'نابرابري'), '!=', 'x != y', ('true if x does not equal y, false otherwise', 'اگر x، y کے برابر نہ ہو تو true، ورنہ false', 'که x له y سره برابر نه وي true، که نه false'))]
rows = lambda D, i: [[o[i], s, f, op[i]] for o, s, f, op in D]
H4 = (['Operator', 'Symbol', 'Form', 'Operation'], ['آپریٹر', 'علامت', 'شکل', 'عمل'], ['چلونکی', 'نښه', 'بڼه', 'عملیه'])
t.table('cs12-table-3-8', H4[0], rows(REL, 0), H4[1], H4[2], rows(REL, 1), rows(REL, 2))
P('Table 3.8: List of Relational Operators', 'جدول 3.8: ریلیشنل آپریٹرز کی فہرست', '۳.۸ جدول: د اړیکه‌ییزو چلونکو لېست')
P('Consider the following lines of code:', 'کوڈ کی درج ذیل لائنوں پر غور کریں:', 'د کوډ لاندې کرښو ته پام وکړئ:')
code(t, '''(7 == 5) // false.
(5 > 4) // true.
(3 != 2) // true.
(6 >= 6) // true.
(5 < 5) // false.''')
H('f. Logical operators', 'f. منطقی آپریٹرز', 'f. منطقي چلونکي')
P('There are three logical operators used in C++. These are: !, &&, || that are shown in Table 3.9 along with their operations.', 'C++ میں تین منطقی آپریٹرز استعمال ہوتے ہیں: !، &&، || جو جدول 3.9 میں ان کے اعمال کے ساتھ دکھائے گئے ہیں۔', 'په C++ کې درې منطقي چلونکي کارول کېږي: !، &&، || چې په ۳.۹ جدول کې د عملیو سره ښودل شوي.')
LOG = [(('Logical NOT', 'منطقی NOT', 'منطقي NOT'), '!', '!x', ('true if x is false, or false if x is true', 'اگر x غلط ہو تو true، یا اگر x درست ہو تو false', 'که x false وي true، یا که x true وي false')),
       (('Logical AND', 'منطقی AND', 'منطقي AND'), '&&', 'x && y', ('true if both x and y are true, false otherwise', 'اگر x اور y دونوں درست ہوں تو true، ورنہ false', 'که x او y دواړه true وي true، که نه false')),
       (('Logical OR', 'منطقی OR', 'منطقي OR'), '||', 'x || y', ('true if either x or y are true, false otherwise', 'اگر x یا y میں سے کوئی درست ہو تو true، ورنہ false', 'که x یا y کوم یو true وي true، که نه false'))]
t.table('cs12-table-3-9', H4[0], rows(LOG, 0), H4[1], H4[2], rows(LOG, 1), rows(LOG, 2))
P('Table 3.9: List of Logical Operators', 'جدول 3.9: منطقی آپریٹرز کی فہرست', '۳.۹ جدول: د منطقي چلونکو لېست')
rec = BOOK.record(t, 'cs12-u3-text-20', 'Unit 3 text (20)', 'یونٹ 3 — متن (۲۰)', '۳ څپرکی — متن (۲۰)', 54, [95, 96, 97])
rec['sourceNote'] = 'The prefix segment begins at the foot of p.95. Tables 3.8 and 3.9 are reproduced as structured tables (the book numbers them 3.8/3.9 directly after 3.5; there are no Tables 3.6–3.7).'
issues = [{'id': 'cs12-pdf054', 'unit': 3, 'printedPage': 97,
           'description': 'Table numbering jumps from 3.5 to 3.8 (no 3.6/3.7) — retained as printed. Table 3.9 prints “true if either x or y are true”. The output line “26 24” is shown three times as printed (the fourth line, postfix, also prints 26 24).'}]

if __name__ == '__main__':
    BOOK.save(54, [(3, rec)], issues=issues)
