"""Computer Science XII PDF56 (spread): printed pp.100–101 — conditional-operator program; 3.4.2 unary, binary, ternary; 3.4.3 expression (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
code(t, '''// conditional operator
#include <iostream.h>
#include<conio.h>
int main()
{
int x, y, z;
x=22;
y=77;
z = (x>y) ? x : y;
cout<< "The greater value is: "<<z ;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, 'The greater value is: 77')
H('3.4.2 Unary, Binary and Ternary operators', '3.4.2 یونری، بائنری اور ٹرنری آپریٹرز', '۳.۴.۲ یو-عملي، دوه-عملي او درې-عملي چلونکي')
P('The set of C++ operators is divided into three main categories: unary, binary and ternary. This division is on the basis of number of operands upon which the operators operate. The following sections discuss them.',
  'C++ آپریٹرز کے مجموعے کو تین بنیادی زمروں میں تقسیم کیا جاتا ہے: یونری، بائنری اور ٹرنری۔ یہ تقسیم ان آپرینڈز کی تعداد کی بنیاد پر ہے جن پر آپریٹرز عمل کرتے ہیں۔ درج ذیل حصے ان پر بحث کرتے ہیں۔',
  'د C++ چلونکو ټولګه په درې اصلي ډلو وېشل کېږي: یو-عملي، دوه-عملي او درې-عملي. دا وېش د هغو عملوندونو د شمېر پر بنسټ دی چې چلونکي پرې عمل کوي. لاندې برخې یې بحث کوي.')
H('a. Unary operators', 'a. یونری آپریٹرز', 'a. یو-عملي چلونکي')
P('Unary operators are those operators which need a single operand. There are two arithmetic unary operators: unary plus + and unary -.',
  'یونری آپریٹرز وہ آپریٹرز ہیں جنھیں ایک آپرینڈ درکار ہوتا ہے۔ دو حسابی یونری آپریٹرز ہیں: یونری پلس + اور یونری -۔',
  'یو-عملي چلونکي هغه دي چې یو عملوند ته اړتیا لري. دوه حسابي یو-عملي چلونکي دي: یو-عملي جمع + او یو-عملي منفي -.')
P('Consider the following examples:', 'درج ذیل مثالوں پر غور کریں:', 'لاندې بېلګو ته پام وکړئ:')
code(t, '''x = -y;
a = +b;''')
P('The logical ! operator is also a unary operator. Consider the following examples:', 'منطقی ! آپریٹر بھی یونری آپریٹر ہے۔ درج ذیل مثالوں پر غور کریں:', 'منطقي ! چلونکی هم یو-عملي چلونکی دی. لاندې بېلګو ته پام وکړئ:')
code(t, '''!x;
!(x > y);''')
P('Increment ++ and decrement -- operators are also the examples of unary operators.', 'انکریمنٹ ++ اور ڈیکریمنٹ -- آپریٹرز بھی یونری آپریٹرز کی مثالیں ہیں۔', 'د زیاتولو ++ او کمولو -- چلونکي هم د یو-عملي چلونکو بېلګې دي.')
H('b. Binary operators', 'b. بائنری آپریٹرز', 'b. دوه-عملي چلونکي')
t.group('lines', [
 ('i. Binary operators are those operators which need two operands. For example (+, -, *, /, %)', 'i. بائنری آپریٹرز وہ آپریٹرز ہیں جنھیں دو آپرینڈز درکار ہوں۔ مثلاً (+، -، *، /، %)', 'i. دوه-عملي چلونکي هغه دي چې دوو عملوندونو ته اړتیا لري. لکه (+، -، *، /، %)'),
 ('ii. The assignment operator = is also a binary operator as it requires two operands. The operands are: the receiving variable on the left hand side and the evaluated expression on the right hand side.', 'ii. اسائنمنٹ آپریٹر = بھی بائنری آپریٹر ہے کیونکہ اسے دو آپرینڈز درکار ہیں: بائیں طرف قدر وصول کرنے والا ویری ایبل اور دائیں طرف قدر نکالا گیا ایکسپریشن۔', 'ii. د سپارلو چلونکی = هم دوه-عملي دی، ځکه دوو عملوندونو ته اړتیا لري: کیڼ اړخ ته ترلاسه کوونکی متغیر او ښي اړخ ته ارزول شوې افاده.'),
 ('iii. The logical and relational operators (<, <=, ==, >, >=, !=, &&, || ) are binary operators as well, as they require two operands.', 'iii. منطقی اور ریلیشنل آپریٹرز (<، <=، ==، >، >=، !=، &&، ||) بھی بائنری آپریٹرز ہیں کیونکہ انھیں دو آپرینڈز درکار ہیں۔', 'iii. منطقي او اړیکه‌ییز چلونکي (<، <=، ==، >، >=، !=، &&، ||) هم دوه-عملي دي، ځکه دوو عملوندونو ته اړتیا لري.')])
H('c. Ternary operator', 'c. ٹرنری آپریٹر', 'c. درې-عملي چلونکی')
P('Ternary operator needs three operands. There is only one ternary operator. This operator is conditional operator (? :)', 'ٹرنری آپریٹر کو تین آپرینڈز درکار ہیں۔ صرف ایک ٹرنری آپریٹر ہے اور وہ شرطیہ آپریٹر (? :) ہے۔', 'درې-عملي چلونکی درې عملوندونو ته اړتیا لري. یوازې یو درې-عملي چلونکی شته او هغه شرطي چلونکی (? :) دی.')
H('3.4.3 Expression', '3.4.3 ایکسپریشن', '۳.۴.۳ افاده')
P('An expression consists of operators and operands or it may be the combination of variables and/or constants linked with operators. For example:', 'ایکسپریشن آپریٹرز اور آپرینڈز پر مشتمل ہوتا ہے یا یہ آپریٹرز سے جڑے ویری ایبلز اور/یا کانسٹنٹس کا مجموعہ ہو سکتا ہے۔ مثلاً:', 'افاده له چلونکو او عملوندونو جوړه وي یا کېدای شي د متغیرونو او/یا ثابتونو ګډون وي چې په چلونکو تړل شوي. د بېلګې په توګه:')
code(t, '''x=a + b;
Z= 2+ z / y;
y > 4;''')
rec = BOOK.record(t, 'cs12-u3-text-22', 'Unit 3 text (22)', 'یونٹ 3 — متن (۲۲)', '۳ څپرکی — متن (۲۲)', 56, [100, 101])
rec['sourceNote'] = 'The expression examples continue on p.102 (PDF57).'
issues = [{'id': 'cs12-pdf056', 'unit': 3, 'printedPage': 100,
           'description': 'Section numbers printed “3.4.2.” and “3.4.3.”; the listing prints the cout string with a curly opening quote; normalised. p.100 “need a single operand. There are two arithmetic unary operators”.'}]

if __name__ == '__main__':
    BOOK.save(56, [(3, rec)], issues=issues)
