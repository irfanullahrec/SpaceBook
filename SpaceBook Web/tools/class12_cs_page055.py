"""Computer Science XII PDF55 (spread): printed pp.98–99 — logical NOT (Table 3.10), AND (Table 3.11), OR (Table 3.12); g. ternary operator (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
TF = {'True': ('True', 'درست', 'سم'), 'False': ('False', 'غلط', 'ناسم')}
def tt(tid, head, rows):
    tr = lambda i: [[TF[c][i] if c in TF else c for c in r] for r in rows]
    t.table(tid, head, tr(0), head, head, tr(1), tr(2))
H('i. Logical NOT', 'i. منطقی NOT', 'i. منطقي NOT')
P('The ! operator is the C++ unary operator that is used to perform the Boolean NOT operation. The output of this operator is the inverse of the value of its operand. It produces false if its operand is true and true if its operand is false. The effects of logical NOT operator is summarized in the truth Table 3.10.',
  '! آپریٹر C++ کا یونری آپریٹر ہے جو بولین NOT عمل انجام دینے کے لیے استعمال ہوتا ہے۔ اس آپریٹر کا آؤٹ پٹ اس کے آپرینڈ کی قدر کا الٹ ہوتا ہے۔ اگر آپرینڈ true ہو تو یہ false دیتا ہے اور اگر آپرینڈ false ہو تو true۔ منطقی NOT آپریٹر کے اثرات کا خلاصہ ٹروتھ جدول 3.10 میں دیا گیا ہے۔',
  '! چلونکی د C++ یو-عملي چلونکی دی چې د بولي NOT عملیې لپاره کارول کېږي. د دې چلونکي وتنه د هغه د عملوند د ارزښت سرچپه ده. که عملوند یې true وي false ورکوي او که false وي true. د منطقي NOT چلونکي اغېزې د ریښتینولۍ په ۳.۱۰ جدول کې لنډې شوې.')
tt('cs12-table-3-10', ['X', '!X'], [['True', 'False'], ['False', 'True']])
P('Table 3.10: Logical NOT Operator', 'جدول 3.10: منطقی NOT آپریٹر', '۳.۱۰ جدول: منطقي NOT چلونکی')
P('The following lines of code demonstrate the working of NOT operator.', 'کوڈ کی درج ذیل لائنیں NOT آپریٹر کا کام دکھاتی ہیں۔', 'د کوډ لاندې کرښې د NOT چلونکي کار ښيي.')
code(t, '''!(5 == 5) // evaluates to false because the expression (5 == 5) is true.
!(6 <= 4) // evaluates to true because (6 <= 4) would be false.
!true// evaluates to false
!false// evaluates to true.''')
H('ii. Logical AND', 'ii. منطقی AND', 'ii. منطقي AND')
P('Logical && operator is a binary operator that needs two operands. It is used to test whether both conditions are true or not. If both the conditions are true, the logical && returns true, otherwise, it returns false. Truth Table 3.11 shows the results of logical && operator.',
  'منطقی && آپریٹر بائنری آپریٹر ہے جسے دو آپرینڈز درکار ہوتے ہیں۔ یہ جانچنے کے لیے استعمال ہوتا ہے کہ آیا دونوں شرائط درست ہیں یا نہیں۔ اگر دونوں شرائط true ہوں تو منطقی && true واپس کرتا ہے، ورنہ false۔ ٹروتھ جدول 3.11 منطقی && آپریٹر کے نتائج دکھاتی ہے۔',
  'منطقي && چلونکی دوه-عملي چلونکی دی چې دوو عملوندونو ته اړتیا لري. د دې ازمویلو لپاره کارول کېږي چې ایا دواړه شرطونه true دي که نه. که دواړه شرطونه true وي، منطقي && true ورکوي، که نه false. د ریښتینولۍ ۳.۱۱ جدول د منطقي && چلونکي پایلې ښيي.')
tt('cs12-table-3-11', ['X', 'Y', 'X && Y'], [['False', 'False', 'False'], ['False', 'True', 'False'], ['True', 'False', 'False'], ['True', 'True', 'True']])
P('Table 3.11: Logical AND Operator', 'جدول 3.11: منطقی AND آپریٹر', '۳.۱۱ جدول: منطقي AND چلونکی')
H('iii. Logical OR', 'iii. منطقی OR', 'iii. منطقي OR')
P('The logical || operator is used to test whether either of two conditions is true. If either of the left operand or right operand evaluates to true, the logical || operator returns true. Also, if both the operands are true, logical || returns to true but if both are false it returns to false. Truth Table 3.12 shows the operations of logical || operator.',
  'منطقی || آپریٹر یہ جانچنے کے لیے استعمال ہوتا ہے کہ دو شرائط میں سے کوئی ایک درست ہے یا نہیں۔ اگر بائیں یا دائیں آپرینڈ میں سے کوئی true ہو تو منطقی || آپریٹر true واپس کرتا ہے۔ نیز اگر دونوں آپرینڈز true ہوں تو بھی || true دیتا ہے لیکن اگر دونوں false ہوں تو false دیتا ہے۔ ٹروتھ جدول 3.12 منطقی || آپریٹر کے اعمال دکھاتی ہے۔',
  'منطقي || چلونکی د دې ازمویلو لپاره کارول کېږي چې ایا له دوو شرطونو یو true دی. که کیڼ یا ښي عملوند کوم یو true وي، منطقي || چلونکی true ورکوي. همداراز که دواړه عملوندونه true وي، || true ورکوي، خو که دواړه false وي false ورکوي. د ریښتینولۍ ۳.۱۲ جدول د منطقي || چلونکي عملیې ښيي.')
tt('cs12-table-3-12', ['X', 'Y', 'X || Y'], [['False', 'False', 'False'], ['False', 'True', 'True'], ['True', 'False', 'True'], ['True', 'True', 'True']])
P('Table 3.12: Logical OR Operator', 'جدول 3.12: منطقی OR آپریٹر', '۳.۱۲ جدول: منطقي OR چلونکی')
H('g. Ternary (or conditional) operator (? : )', 'g. ٹرنری (یا شرطیہ) آپریٹر (? : )', 'g. درې-عملي (یا شرطي) چلونکی (? : )')
P('The conditional operator takes three operands and is therefore also called ternary operator. It evaluates an expression and returns a value if that expression is true and a different value if the expression is false. The general syntax used for conditional operator is:',
  'شرطیہ آپریٹر تین آپرینڈز لیتا ہے اس لیے اسے ٹرنری آپریٹر بھی کہتے ہیں۔ یہ کسی ایکسپریشن کی قدر نکالتا ہے اور اگر ایکسپریشن درست ہو تو ایک قدر اور غلط ہو تو دوسری قدر واپس کرتا ہے۔ شرطیہ آپریٹر کا عمومی طریقۂ تحریر یہ ہے:',
  'شرطي چلونکی درې عملوندونه اخلي، له همدې امله ورته درې-عملي چلونکی هم ویل کېږي. دا یوه افاده ارزوي او که افاده true وي یو ارزښت او که false وي بل ارزښت ورکوي. د شرطي چلونکي عمومي بڼه دا ده:')
code(t, 'condition ? result1: result2;')
P('Here, if condition is true the expression will return result1, and if condition is false it will return result2. Consider the following lines of code to demonstrate the use of conditional operator.',
  'یہاں اگر شرط درست ہو تو ایکسپریشن result1 واپس کرے گا اور اگر شرط غلط ہو تو result2 واپس کرے گا۔ شرطیہ آپریٹر کے استعمال کی وضاحت کے لیے کوڈ کی درج ذیل لائنوں پر غور کریں۔',
  'دلته که شرط true وي، افاده به result1 ورکړي او که شرط false وي result2 به ورکړي. د شرطي چلونکي د کارونې د ښودلو لپاره د کوډ لاندې کرښو ته پام وکړئ.')
code(t, '''7==5 ?4 : 3; // returns 3, since 7 is not equal to 5.
7==5+2 ?4 : 3; // returns 4, since 7 is equal to 5+2.
5>3 ?a : b; // returns the value of a, since 5 is greater than 3.''')
P('The following program demonstrates the use of conditional operator.', 'درج ذیل پروگرام شرطیہ آپریٹر کا استعمال دکھاتا ہے۔', 'لاندې پروګرام د شرطي چلونکي کارونه ښيي.')
rec = BOOK.record(t, 'cs12-u3-text-21', 'Unit 3 text (21)', 'یونٹ 3 — متن (۲۱)', '۳ څپرکی — متن (۲۱)', 55, [98, 99])
rec['sourceNote'] = 'Truth Tables 3.10–3.12 are reproduced as structured tables (True/False localised in the Urdu and Pashto views). The conditional-operator program follows on p.100 (PDF56).'
issues = [{'id': 'cs12-pdf055', 'unit': 3, 'printedPage': 98,
           'description': 'p.98 prints “The effects of logical NOT operator is summarized”, “&&returns”; p.99 “||returns to true … it returns to false”. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(55, [(3, rec)], issues=issues)
