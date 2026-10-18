"""Computer Science XII PDF57 (spread): printed pp.102–103 — expression categories; 3.4.4 precedence; Table 3.13; 3.4.5 compound expression."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('The expressions are categorized as below:', 'ایکسپریشنز کی درجہ بندی ذیل کے مطابق ہے:', 'افادې په لاندې ډول ډلبندي کېږي:')
t.group('lines', [('i. Arithmetic Expressions having numeric operands and arithmetic operators and give numeric results. For example', 'i. حسابی ایکسپریشنز جن میں عددی آپرینڈز اور حسابی آپریٹرز ہوں اور عددی نتائج دیں۔ مثلاً', 'i. حسابي افادې چې شمېریز عملوندونه او حسابي چلونکي لري او شمېریزې پایلې ورکوي. د بېلګې په توګه')])
code(t, '''x = y + 25;
sum = x + y;''')
t.group('lines', [('ii. Relational Expressions having operands and relational operators for comparison of data. For example', 'ii. ریلیشنل ایکسپریشنز جن میں ڈیٹا کے موازنے کے لیے آپرینڈز اور ریلیشنل آپریٹرز ہوں۔ مثلاً', 'ii. اړیکه‌ییزې افادې چې د ډېټا د پرتلې لپاره عملوندونه او اړیکه‌ییز چلونکي لري. د بېلګې په توګه')])
code(t, '''x > y;
z >=10;''')
t.group('lines', [('iii. Logical Expressions for testing of two or more Boolean expressions. For example', 'iii. منطقی ایکسپریشنز جو دو یا زیادہ بولین ایکسپریشنز کی جانچ کے لیے ہوں۔ مثلاً', 'iii. منطقي افادې چې د دوو یا ډېرو بولي افادو د ازمویلو لپاره وي. د بېلګې په توګه')])
code(t, '''(x > y) || (x = 10);
(n=5) && (m > n);''')
H('3.4.4 Precedence of operators', '3.4.4 آپریٹرز کی ترجیح', '۳.۴.۴ د چلونکو لومړیتوب')
P('Precedence of operator means that which operand will be evaluated first and which one will be evaluated later if the expression is a complex one. For example, in the following expression % will be evaluated first and then addition.',
  'آپریٹر کی ترجیح کا مطلب یہ ہے کہ پیچیدہ ایکسپریشن میں کون سا آپرینڈ پہلے اور کون سا بعد میں قدر نکالا جائے گا۔ مثال کے طور پر درج ذیل ایکسپریشن میں % پہلے اور پھر جمع کی قدر نکالی جائے گی۔',
  'د چلونکي لومړیتوب دا معنا لري چې په پېچلې افاده کې کوم عملوند لومړی او کوم وروسته ارزول کېږي. د بېلګې په توګه په لاندې افاده کې % لومړی او بیا جمع ارزول کېږي.')
code(t, 'a = 5 + 7 % 2 /')
P('From highest to lowest the priority is given below.', 'سب سے زیادہ سے سب سے کم ترجیح ذیل میں دی گئی ہے۔', 'له تر ټولو لوړ تر ټولو ټیټ لومړیتوب لاندې ورکړل شوی.')
t.group('lines', [('1. The parentheses are evaluated first.', '1۔ قوسین کی قدر سب سے پہلے نکالی جاتی ہے۔', '۱. قوسونه لومړی ارزول کېږي.'),
                  ('2. Multiplication, division and modulus operators are performed next, from left to right at same level.', '2۔ ضرب، تقسیم اور ماڈیولس آپریٹرز اس کے بعد ایک ہی سطح پر بائیں سے دائیں انجام پاتے ہیں۔', '۲. د ضرب، وېش او موډولوس چلونکي ورپسې په یوه کچه له کیڼ څخه ښي ته ترسره کېږي.'),
                  ('3. Addition and subtraction operators are resolved last, from left to right with same priority.', '3۔ جمع اور تفریق آپریٹرز آخر میں یکساں ترجیح کے ساتھ بائیں سے دائیں حل ہوتے ہیں۔', '۳. د جمع او تفریق چلونکي په پای کې په یو شان لومړیتوب له کیڼ څخه ښي ته حلېږي.')])
P('The following table shows the list of all operators with their precedence level.', 'درج ذیل جدول تمام آپریٹرز کی فہرست ان کی ترجیحی سطح کے ساتھ دکھاتی ہے۔', 'لاندې جدول د ټولو چلونکو لېست د هغوی د لومړیتوب کچې سره ښيي.')
LR = ('left-to-right', 'بائیں سے دائیں', 'له کیڼ څخه ښي')
RL = ('right-to-left', 'دائیں سے بائیں', 'له ښي څخه کیڼ')
R = [('1', '++ --', ('Postfix increment/decrement', 'پوسٹ فکس انکریمنٹ/ڈیکریمنٹ', 'وروستی زیاتول/کمول'), LR),
     ('2', '++ --  + -  !', ('Prefix increment/decrement; Unary plus/minus; Logical negation', 'پری فکس انکریمنٹ/ڈیکریمنٹ؛ یونری جمع/منفی؛ منطقی نفی', 'مخکینی زیاتول/کمول؛ یو-عملي جمع/منفي؛ منطقي نفي'), RL),
     ('3', '* / %', ('Multiplication/division/modulus', 'ضرب/تقسیم/ماڈیولس', 'ضرب/وېش/موډولوس'), LR),
     ('4', '+ -', ('Addition/subtraction', 'جمع/تفریق', 'جمع/تفریق'), LR),
     ('5', '< <=  > >=', ('Relational less than/less than or equal to; Relational greater than/greater than or equal to', 'ریلیشنل چھوٹا/چھوٹا یا برابر؛ ریلیشنل بڑا/بڑا یا برابر', 'اړیکه‌ییز کوچنی/کوچنی یا برابر؛ اړیکه‌ییز لوی/لوی یا برابر'), LR),
     ('6', '== !=', ('Relational is equal to/is not equal to', 'ریلیشنل برابر ہے/برابر نہیں', 'اړیکه‌ییز برابر دی/برابر نه دی'), LR),
     ('7', '&&', ('Logical AND', 'منطقی AND', 'منطقي AND'), LR),
     ('8', '||', ('Logical OR', 'منطقی OR', 'منطقي OR'), LR),
     ('9', '?:', ('Ternary conditional', 'ٹرنری شرطیہ', 'درې-عملي شرطي'), RL),
     ('10', '=  += -=  *= /=  %=', ('Assignment; Addition/subtraction assignment; Multiplication/division assignment; Modulus assignment', 'اسائنمنٹ؛ جمع/تفریق اسائنمنٹ؛ ضرب/تقسیم اسائنمنٹ؛ ماڈیولس اسائنمنٹ', 'سپارنه؛ د جمع/تفریق سپارنه؛ د ضرب/وېش سپارنه؛ د موډولوس سپارنه'), RL)]
rows = lambda i: [[l, o, d[i], a[i]] for l, o, d, a in R]
t.table('cs12-table-3-13', ['Level', 'Operator', 'Description', 'Associativity'], rows(0), ['سطح', 'آپریٹر', 'وضاحت', 'سمت (ایسوسی ایٹیوٹی)'], ['کچه', 'چلونکی', 'تشریح', 'تړاو (Associativity)'], rows(1), rows(2))
P('Table 3.13 Operators Precedence', 'جدول 3.13 آپریٹرز کی ترجیح', '۳.۱۳ جدول: د چلونکو لومړیتوب')
H('3.4.5 Compound expression', '3.4.5 مرکب ایکسپریشن', '۳.۴.۵ مرکبه افاده')
P('Compound expression is an expression that involves more than one sub-expressions linked with operators. Usually two or more relational expressions are linked with logical operators to form compound Boolean expression.',
  'مرکب ایکسپریشن وہ ایکسپریشن ہے جس میں آپریٹرز سے جڑے ایک سے زیادہ ذیلی ایکسپریشنز ہوں۔ عموماً دو یا زیادہ ریلیشنل ایکسپریشنز کو منطقی آپریٹرز سے جوڑ کر مرکب بولین ایکسپریشن بنایا جاتا ہے۔',
  'مرکبه افاده هغه افاده ده چې په چلونکو تړل شوې له یوې زیاتې فرعي افادې لري. عموماً دوه یا ډېرې اړیکه‌ییزې افادې د منطقي چلونکو په مرسته تړل کېږي څو مرکبه بولي افاده جوړه شي.')
P('Following are the examples of compound expressions.', 'مرکب ایکسپریشنز کی مثالیں درج ذیل ہیں۔', 'د مرکبو افادو بېلګې دا دي.')
code(t, '''X1= (- B + sqrt( B*B – 4*A*C))/(2*A);
( (b * b) - 4 * a * c ) > 0
(age <= 20) && (height >= 5)
(m > 5) || (j > 0)''')
rec = BOOK.record(t, 'cs12-u3-text-23', 'Unit 3 text (23)', 'یونٹ 3 — متن (۲۳)', '۳ څپرکی — متن (۲۳)', 57, [102, 103])
rec['sourceNote'] = 'Table 3.13 is reproduced as a structured table; operator groups that are stacked in one printed cell are separated by spaces/semicolons.'
issues = [{'id': 'cs12-pdf057', 'unit': 3, 'printedPage': 102,
           'description': 'p.102 prints the precedence example as “a = 5 + 7 % 2 /” (truncated; probably “a = 5 + 7 % 2;”), and the logical-expression examples use “=” (assignment) inside conditions, e.g. “(x = 10)”, “(n=5)”; the compound example uses an en dash “–” for minus. All retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(57, [(3, rec)], issues=issues)
