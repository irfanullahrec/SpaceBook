"""Computer Science XII PDF64–65: pp.116–117 c. switch-default statement, Flowchart 4.3; pp.118–119 switch vs if-else listings; 4.1.2 nested if program.
Run: python class12_cs_page064.py N (64 or 65)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_4_3


def p64():
    t = Builder()
    P = t.p
    t.h('c. Switch-default statement', 'c. switch-default بیان', 'c. د switch-default بیان')
    P('Switch statement is a better alternative of the nested if-else structure. The nested if-else structure is sometimes more difficult to understand to find that which if clause is associated with which else clause. The objective of switch statement is to check several possible constant values for an expression and then execute those which match the particular label or case constant value. Its general form is as follows:',
      'switch بیان نیسٹڈ if-else ساخت کا بہتر متبادل ہے۔ نیسٹڈ if-else ساخت کو سمجھنا بعض اوقات زیادہ مشکل ہوتا ہے کہ کون سی if شق کس else شق سے وابستہ ہے۔ switch بیان کا مقصد کسی ایکسپریشن کی کئی ممکنہ مستقل قدروں کی جانچ کرنا اور پھر ان بیانات کو چلانا ہے جو مخصوص لیبل یا case کی مستقل قدر سے مطابقت رکھتے ہوں۔ اس کی عمومی شکل یہ ہے:',
      'switch بیان د ځالې if-else جوړښت ښه بدیل دی. ځالې if-else جوړښت کله کله ډېر ستونزمن وي چې پوه شو کوم if له کوم else سره تړلی دی. د switch بیان موخه دا ده چې د یوې افادې ډېر احتمالي ثابت ارزښتونه وګوري او بیا هغه اجرا کړي چې له ځانګړي لیبل یا د case ثابت ارزښت سره سمون ولري. عمومي بڼه یې دا ده:')
    code(t, '''switch (expression)
{
case constant1:
group of statements 1;
break;
case constant2:
group of statements 2;
break;
.
.
.
default:
default group of statements
}''')
    P('switch evaluates the expression and if the value of the expression equal to constant1, it executes group of statements 1 until it encounters the break statement. When it reaches the break statement the program jumps to the end of the switch. If the value of the expression is not equal to constant1, it is matched with constant2. If it is equal to this constant2, this group of statements 2 is executed until the break keyword is reached, and then a jump will occur to the end of the switch. Finally, if the value of expression does not match with any of the constants then the program executes the statements after the default keyword. The default clause is optional. Flowchart 4.3 shows working of switch Structure.',
      'switch ایکسپریشن کی قدر نکالتا ہے اور اگر وہ constant1 کے برابر ہو تو break بیان آنے تک بیانات کا گروپ 1 چلاتا ہے۔ break بیان پر پہنچ کر پروگرام switch کے آخر پر چلا جاتا ہے۔ اگر قدر constant1 کے برابر نہ ہو تو اسے constant2 سے ملایا جاتا ہے۔ اگر یہ constant2 کے برابر ہو تو break آنے تک بیانات کا گروپ 2 چلتا ہے اور پھر switch کے آخر پر چھلانگ لگتی ہے۔ آخر میں اگر قدر کسی بھی کانسٹنٹ سے نہ ملے تو پروگرام default کی ورڈ کے بعد والے بیانات چلاتا ہے۔ default شق اختیاری ہے۔ فلو چارٹ 4.3 switch ساخت کا عمل دکھاتا ہے۔',
      'switch افاده ارزوي او که د افادې ارزښت له constant1 سره برابر وي، د بیانونو ۱مه ډله تر هغه اجرا کوي چې break بیان ته ورسېږي. کله چې break بیان ته ورسېږي، پروګرام د switch پای ته ټوپ وهي. که ارزښت له constant1 سره برابر نه وي، له constant2 سره پرتله کېږي. که ورسره برابر وي، د بیانونو ۲مه ډله تر break پورې اجرا کېږي او بیا د switch پای ته ټوپ کېږي. په پای کې که ارزښت له هېڅ ثابت سره سمون ونه لري، پروګرام د default کلیدي کلمې وروسته بیانونه اجرا کوي. د default برخه اختیاري ده. ۴.۳ فلوچارټ د switch جوړښت کار ښيي.')
    en, ur, ps, ratio = fig_4_3()
    t.visual('cs12-fig-4-3', en, ur, ps, ratio)
    P('Consider the following two code segments which have the same behavior.', 'کوڈ کے درج ذیل دو حصوں پر غور کریں جن کا رویہ یکساں ہے۔', 'د کوډ لاندې دوو برخو ته پام وکړئ چې یو شان چلند لري.')
    rec = BOOK.record(t, 'cs12-u4-text-4', 'Unit 4 text (4)', 'یونٹ 4 — متن (۴)', '۴ څپرکی — متن (۴)', 64, [116, 117])
    rec['sourceNote'] = 'Flowchart 4.3 is reproduced as a coded diagram. The two code segments follow on p.118 (PDF65).'
    BOOK.save(64, [(4, rec)], issues=[{'id': 'cs12-pdf064', 'unit': 4, 'printedPage': 116,
               'description': 'p.116 prints “find that which if clause”, “if the value of the expression equal to constant1”, “this group of statements 2”. Retained as printed.'}])


def p65():
    t = Builder()
    P = t.p
    P('switch example', 'switch کی مثال', 'د switch بېلګه')
    code(t, '''// Switch program
#include <iostream.h>
#include<conio.h>
int main()
{
int x;
cout<<"Enter value for x";
cin>>x;
switch (x)
{
case 1:
cout << "x is 1";
break;
case 2:
cout << "x is 2";
break;
default:
cout << "value of x is neither 1 nor 2";
}
getch();
return 0;
}''')
    P('if-else equivalent', 'if-else متبادل', 'د if-else معادل')
    code(t, '''// if-else alternative of the switch program
#include <iostream.h>
#include<conio.h>
int main()
{
int x;
cout<<"Enter value for x"<<end;
cin>>x;
if (x == 1)
{
cout << "x is 1";
}else
if (x == 2)
{
cout << "x is 2";
}else
{
cout << " value of x is neither 1 nor 2";
}
getch();
return 0;
}''')
    P('In the above program, if we did not include a break statement after the first group for case 1, the program will not automatically jump to the end of the switch and it would continue executing the rest of statements until it reaches either a break instruction or the end of the switch block.',
      'اوپر والے پروگرام میں اگر ہم case 1 کے پہلے گروپ کے بعد break بیان شامل نہ کرتے تو پروگرام خود بخود switch کے آخر پر نہ جاتا اور باقی بیانات چلاتا رہتا یہاں تک کہ break ہدایت یا switch بلاک کا اختتام آ جاتا۔',
      'په پورته پروګرام کې که موږ د case 1 له لومړۍ ډلې وروسته break بیان نه وای شامل کړی، پروګرام به په خپله د switch پای ته نه تلای او پاتې بیانونه به یې اجرا کول تر هغه چې break لارښوونې یا د switch بلاک پای ته رسېدلی.')
    P('switch statement can only be used to compare the value of the expression with the constants written with each case clause. Therefore, variables cannot be used with constants such as case n or ranges such as case (1..3): because they are not valid C++ constants. These constants be either integers or character type.',
      'switch بیان صرف ایکسپریشن کی قدر کا ہر case شق کے ساتھ لکھے گئے کانسٹنٹس سے موازنہ کرنے کے لیے استعمال ہو سکتا ہے۔ اس لیے کانسٹنٹس کی جگہ ویری ایبلز جیسے case n یا حدود جیسے case (1..3): استعمال نہیں ہو سکتیں کیونکہ یہ درست C++ کانسٹنٹس نہیں ہیں۔ یہ کانسٹنٹس صحیح عدد یا حرفی قسم کے ہوں۔',
      'switch بیان یوازې د افادې ارزښت د هر case سره لیکل شویو ثابتونو سره پرتله کولو ته کارېدای شي. نو د ثابتونو پر ځای متغیرونه لکه case n یا حدونه لکه case (1..3): نه شي کارول کېدای، ځکه دا سم C++ ثابتونه نه دي. دا ثابتونه دې صحیح عدد یا د توري ډول وي.')
    t.h('4.1.2 Nested if statement', '4.1.2 نیسٹڈ if بیان', '۴.۱.۲ ځالې if بیان')
    P('It is possible to chain if-else statements together. When one if-else statement is used inside the body of another if-else structure then it forms a nested if ladder.',
      'if-else بیانات کو ایک ساتھ زنجیر کی طرح جوڑنا ممکن ہے۔ جب ایک if-else بیان دوسری if-else ساخت کے جسم کے اندر استعمال ہو تو یہ نیسٹڈ if سیڑھی بناتا ہے۔',
      'د if-else بیانونه یو بل سره د زنځیر په څېر تړل شوني دي. کله چې یو if-else بیان د بل if-else جوړښت د بدنې دننه وکارول شي، ځالې if زینه جوړوي.')
    P('The following program demonstrates the use of nested if structure.', 'درج ذیل پروگرام نیسٹڈ if ساخت کا استعمال دکھاتا ہے۔', 'لاندې پروګرام د ځالې if جوړښت کارونه ښيي.')
    code(t, '''#include <iostream.h>
#include<conio.h>
int main()
{
int X;
cout << "Enter a number: ";
cin >> X;
if (X > 100)
cout << X << "is greater than 100" << endl;
else if (X < 50)
cout << X << "is less than 50" << endl;
else
cout << X << " is between 50 and 100" << endl;
getch();
return 0;
}''')
    P('Output of the program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
    code(t, '''Enter a number:
96
96 is between 50 and 100''')
    rec = BOOK.record(t, 'cs12-u4-text-5', 'Unit 4 text (5)', 'یونٹ 4 — متن (۵)', '۴ څپرکی — متن (۵)', 65, [118, 119])
    rec['sourceNote'] = 'The printed side-by-side table (“switch example” | “if-else equivalent”) is given as two labelled listings.'
    BOOK.save(65, [(4, rec)], issues=[{'id': 'cs12-pdf065', 'unit': 4, 'printedPage': 118,
               'description': 'The if-else listing prints “<<end;” (for endl) and the cout prompt opens with a curly quote; “These constants be either integers or character type”. Retained as printed (quotes normalised).'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    p64() if n == 64 else p65()
