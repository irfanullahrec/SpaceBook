"""Computer Science XII PDF52 (spread): printed pp.92–93 — b. arithmetic operators; Table 3.4; modulus; arithmetic program + output; c. compound assignment operators (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('b. Arithmetic operators', 'b. حسابی آپریٹرز', 'b. حسابي چلونکي')
P('There are five arithmetic operators used in C++. These are (+, -, *, /, %) that support the following arithmetic operations shown in Table 3.4.',
  'C++ میں پانچ حسابی آپریٹرز استعمال ہوتے ہیں۔ یہ (+، -، *، /، %) ہیں جو جدول 3.4 میں دکھائے گئے درج ذیل حسابی اعمال کی معاونت کرتے ہیں۔',
  'په C++ کې پنځه حسابي چلونکي کارول کېږي. دا (+، -، *، /، %) دي چې په ۳.۴ جدول کې ښودل شوې لاندې حسابي عملیې ملاتړ کوي.')
ops = [('+', ('addition', 'جمع', 'جمع')), ('-', ('subtraction', 'تفریق', 'تفریق')), ('*', ('multiplication', 'ضرب', 'ضرب')), ('/', ('division', 'تقسیم', 'وېش')), ('%', ('modulus', 'باقی (ماڈیولس)', 'پاتې (موډولوس)'))]
rows = lambda i: [[o, n[i]] for o, n in ops]
t.table('cs12-table-3-4', ['Operator', 'Operation'], rows(0), ['آپریٹر', 'عمل'], ['چلونکی', 'عملیه'], rows(1), rows(2))
P('Table 3.4: Arithmetic Operators', 'جدول 3.4: حسابی آپریٹرز', '۳.۴ جدول: حسابي چلونکي')
P('The percentage sign % shown in the above table is used for modulus. Modulus is the operation that gives the remainder of a division of two values. For example, if we write:',
  'اوپر کے جدول میں دکھایا گیا فیصد کا نشان % ماڈیولس کے لیے استعمال ہوتا ہے۔ ماڈیولس وہ عمل ہے جو دو قدروں کی تقسیم کا باقی دیتا ہے۔ مثلاً اگر ہم لکھیں:',
  'په پورته جدول کې ښودل شوې د سلنې نښه % د موډولوس لپاره کارول کېږي. موډولوس هغه عملیه ده چې د دوو ارزښتونو د وېش پاتې برخه ورکوي. د بېلګې په توګه که ولیکو:')
code(t, 'remainder = 11 % 5;')
P('The variable ‘remainder’ will contain the value 1, since 1 is the remainder from dividing 11 by 5. The following program demonstrates the use of these operators.',
  'ویری ایبل ‘remainder’ میں قدر 1 ہوگی کیونکہ 11 کو 5 سے تقسیم کرنے پر باقی 1 بچتا ہے۔ درج ذیل پروگرام ان آپریٹرز کا استعمال دکھاتا ہے۔',
  'متغیر ‘remainder’ به ارزښت 1 ولري، ځکه 11 پر 5 وېشلو کې 1 پاتې کېږي. لاندې پروګرام د دې چلونکو کارونه ښيي.')
code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
int a=11, b=5;
int sum=a+ b;
int difference=a - b;
int product=a * b;
float division=a / b;
int remainder=a % b;
cout<< "sum ="<<sum<<endl;
cout<< "difference ="<< difference <<endl;
cout<< "product ="<< product <<endl;
cout<< "division ="<< division <<endl;
cout<< "remainder ="<< remainder;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''sum =16
difference =6
product =55
division =2.0
remainder =1''')
H('c. Compound or arithmetic assignment operators', 'c. مرکب یا حسابی اسائنمنٹ آپریٹرز', 'c. مرکب یا حسابي د سپارلو چلونکي')
P('Compound assignment operators used in C++ are: (+=, -=, *=, /=, %=). These operators are used to modify the value of a variable by performing an operation on the value that is',
  'C++ میں استعمال ہونے والے مرکب اسائنمنٹ آپریٹرز یہ ہیں: (+=، -=، *=، /=، %=)۔ یہ آپریٹرز ویری ایبل کی قدر میں ترمیم کے لیے استعمال ہوتے ہیں، اس قدر پر کوئی عمل کر کے جو',
  'په C++ کې کارېدونکي مرکب د سپارلو چلونکي دا دي: (+=، -=، *=، /=، %=). دا چلونکي د متغیر د ارزښت د بدلولو لپاره کارول کېږي، د هغه ارزښت پر سر د یوې عملیې په ترسره کولو چې')
rec = BOOK.record(t, 'cs12-u3-text-18', 'Unit 3 text (18)', 'یونٹ 3 — متن (۱۸)', '۳ څپرکی — متن (۱۸)', 52, [92, 93])
rec['sourceNote'] = 'The top lines of p.92 complete the assignment program recorded with PDF51. Table 3.4 is reproduced as a structured table. The compound-assignment paragraph continues on p.94 (PDF53).'
issues = [{'id': 'cs12-pdf052', 'unit': 3, 'printedPage': 93,
           'description': 'The printed output shows “division =2.0”, though with int operands a/b gives 2 and cout prints “2” — retained as printed. The listing uses curly quotes in the cout strings; normalised to straight quotes.'}]

if __name__ == '__main__':
    BOOK.save(52, [(3, rec)], issues=issues)
