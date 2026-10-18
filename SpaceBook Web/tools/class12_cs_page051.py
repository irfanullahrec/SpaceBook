"""Computer Science XII PDF51 (spread): printed pp.90–91 — 3.4 operators; 3.4.1; a. assignment operator + program (whole incl. p.92 lines and output)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('3.4 Operators in C++', '3.4 C++ میں آپریٹرز', '۳.۴ په C++ کې چلونکي')
P('Operators are the symbols which perform operation on operands. The operation may be arithmetic or comparison of data.',
  'آپریٹرز وہ علامات ہیں جو آپرینڈز پر عمل کرتی ہیں۔ یہ عمل حسابی یا ڈیٹا کا موازنہ ہو سکتا ہے۔',
  'چلونکي هغه نښې دي چې پر عملوندونو (operands) عملیه ترسره کوي. عملیه کېدای شي حسابي یا د ډېټا پرتله وي.')
code(t, 'z=x+y;')
P('Here, x, y and z are operands and ‘+’ and ‘=’ are the operators.', 'یہاں x، y اور z آپرینڈز ہیں اور ‘+’ اور ‘=’ آپریٹرز ہیں۔', 'دلته x، y او z عملوندونه دي او ‘+’ او ‘=’ چلونکي دي.')
H('3.4.1 Operators in C++', '3.4.1 C++ میں آپریٹرز', '۳.۴.۱ په C++ کې چلونکي')
P('C++ is rich in operators and supports a wide range of these operators that range from the simplest unary to the complex ternary. Operators are very important because without their use, expressions cannot be evaluated.',
  'C++ آپریٹرز سے بھرپور ہے اور ان آپریٹرز کی ایک وسیع رینج کو سپورٹ کرتی ہے جو سادہ ترین یونری سے پیچیدہ ٹرنری تک ہیں۔ آپریٹرز بہت اہم ہیں کیونکہ ان کے استعمال کے بغیر ایکسپریشنز کی قدر نہیں نکالی جا سکتی۔',
  'C++ په چلونکو بډایه ده او د دې چلونکو پراخه لړۍ ملاتړ کوي چې له تر ټولو ساده یو-عملي تر پېچلي درې-عملي پورې دي. چلونکي ډېر مهم دي، ځکه له کارونې پرته یې افادې نه شي ارزول کېدای.')
P('The following are different types of operators used in C++.', 'C++ میں استعمال ہونے والے آپریٹرز کی مختلف اقسام درج ذیل ہیں۔', 'په C++ کې کارېدونکي بېلابېل ډوله چلونکي دا دي.')
H('a. Assignment = operator', 'a. اسائنمنٹ = آپریٹر', 'a. د سپارلو = چلونکی')
P('The assignment operator assigns a value to a variable. The symbol = is used as an assignment operator. For example:', 'اسائنمنٹ آپریٹر ویری ایبل کو قدر تفویض کرتا ہے۔ علامت = اسائنمنٹ آپریٹر کے طور پر استعمال ہوتی ہے۔ مثلاً:', 'د سپارلو چلونکی متغیر ته ارزښت سپاري. د = نښه د سپارلو چلونکي په توګه کارول کېږي. د بېلګې په توګه:')
code(t, 'VarA = 55;')
P('This statement assigns the integer value 55 to the variable VarA. The part at the left of the assignment operator = is a variable whereas the right side can be a constant value, a variable, the result of an operation or any combination of these.',
  'یہ بیان صحیح عددی قدر 55 ویری ایبل VarA کو تفویض کرتا ہے۔ اسائنمنٹ آپریٹر = کے بائیں طرف کا حصہ ویری ایبل ہوتا ہے جبکہ دائیں طرف کانسٹنٹ قدر، ویری ایبل، کسی عمل کا نتیجہ یا ان کا کوئی مجموعہ ہو سکتا ہے۔',
  'دا بیان صحیح عددي ارزښت 55 د VarA متغیر ته سپاري. د سپارلو چلونکي = چپ اړخ ته برخه متغیر وي، په داسې حال کې چې ښي اړخ کېدای شي ثابت ارزښت، متغیر، د یوې عملیې پایله یا د دوی هر ګډون وي.')
P('The assignment operation always takes place from right to left.', 'اسائنمنٹ کا عمل ہمیشہ دائیں سے بائیں ہوتا ہے۔', 'د سپارلو عملیه تل له ښي څخه کیڼ لوري ته کېږي.')
code(t, 'VarA = VarB;')
P('This statement assigns the value of variable VarB to VarA.', 'یہ بیان ویری ایبل VarB کی قدر VarA کو تفویض کرتا ہے۔', 'دا بیان د VarB متغیر ارزښت VarA ته سپاري.')
P('Consider the following program to demonstrate the use of assignment operator.', 'اسائنمنٹ آپریٹر کے استعمال کی وضاحت کے لیے درج ذیل پروگرام پر غور کریں۔', 'د سپارلو چلونکي د کارونې د ښودلو لپاره لاندې پروګرام ته پام وکړئ.')
code(t, '''#include <iostream.h>
#include <conio.h>
int main()
{
int VarA, VarB;
VarA = 100;
VarB = 400;
cout<<" VarA :"<<VarA;
cout<<endl;
cout<<" VarB :"<<VarB;
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''VarA :100
VarB :400''')
rec = BOOK.record(t, 'cs12-u3-text-17', 'Unit 3 text (17)', 'یونٹ 3 — متن (۱۷)', '۳ څپرکی — متن (۱۷)', 51, [90, 91, 92])
rec['sourceNote'] = 'The first lines of p.90 (setw listing end and output) are recorded with PDF50. The assignment program continues on p.92 (PDF52) and is given whole here with its output.'
issues = [{'id': 'cs12-pdf051', 'unit': 3, 'printedPage': 90,
           'description': 'Section numbers are printed “3.4.” and “3.4.1.”, and 3.4.1 repeats the heading “Operators in C++”. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(51, [(3, rec)], issues=issues)
