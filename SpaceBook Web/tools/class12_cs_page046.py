"""Computer Science XII PDF46 (spread): printed pp.80–81 — cin behaviour; cin/cout example; multiple inputs; cin and strings; example."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
P('The object cin can only process the input from the keyboard once the enter key is pressed. Therefore, even if you request a single character, the extraction from cin will not process the input until the user presses enter after the character has been introduced. Consider the following example to demonstrate cin and cout objects.',
  'آبجیکٹ cin کی بورڈ سے ان پٹ صرف اسی وقت پراسیس کر سکتا ہے جب انٹر کی دبائی جائے۔ اس لیے اگر آپ ایک ہی حرف بھی مانگیں تو cin سے نکالنا اس وقت تک ان پٹ پراسیس نہیں کرے گا جب تک صارف حرف داخل کرنے کے بعد انٹر نہ دبائے۔ cin اور cout آبجیکٹس کی وضاحت کے لیے درج ذیل مثال پر غور کریں۔',
  'cin شی له کیبورډ ننوتنه یوازې هغه وخت پروسس کولی شي چې انټر کیلي کېښکېکښل شي. نو که تاسو یوازې یو توری هم وغواړئ، له cin څخه راایستل تر هغه ننوتنه نه پروسس کوي چې کاروونکی د توري له لیکلو وروسته انټر کېکښي. د cin او cout شیانو د ښودلو لپاره لاندې بېلګې ته پام وکړئ.')
code(t, '''// program to demonstrate cin and cout objects
#include <iostream.h>
#include<conio.h>
int main()
{
int i;
float age;
cout << "Please enter your age: ";
cin >> age;
cout << "The age you entered is " << age <<" years";
getch();
return 0;
}''')
P('Output of the Program', 'پروگرام کا آؤٹ پٹ', 'د پروګرام وتنه')
code(t, '''Please enter your age:
16
The age you entered is 16 years''')
P('cin can also be used to request more than one input from the user. Consider the following line of code:',
  'cin کو صارف سے ایک سے زیادہ ان پٹ مانگنے کے لیے بھی استعمال کیا جا سکتا ہے۔ کوڈ کی درج ذیل لائن پر غور کریں:',
  'cin له کاروونکي څخه د یوې زیاتې ننوتنې غوښتلو لپاره هم کارول کېدای شي. د کوډ لاندې کرښې ته پام وکړئ:')
code(t, 'cin >> x >> y;')
P('is equivalent to:', 'جو اس کے برابر ہے:', 'چې له دې سره برابر دی:')
code(t, '''cin >> x;
cin >> y;''')
P('Here, in both the cases, the user need to enter two values, one for variable x and another one for variable y.',
  'یہاں دونوں صورتوں میں صارف کو دو قدریں داخل کرنی ہوں گی، ایک ویری ایبل x کے لیے اور دوسری ویری ایبل y کے لیے۔',
  'دلته په دواړو حالتونو کې کاروونکی باید دوه ارزښتونه ولیکي، یو د x متغیر لپاره او بل د y متغیر لپاره.')
H('cin and strings', 'cin اور اسٹرنگز', 'cin او تارونه')
P('cin can also be used to get strings with the extraction operator >> in the same way as it is used to get values for variables. Consider the following line of code:',
  'cin کو ایکسٹریکشن آپریٹر >> کے ساتھ اسٹرنگز حاصل کرنے کے لیے بھی اسی طرح استعمال کیا جا سکتا ہے جیسے ویری ایبلز کی قدریں حاصل کرنے کے لیے۔ کوڈ کی درج ذیل لائن پر غور کریں:',
  'cin د راایستلو چلونکي >> سره د تارونو د ترلاسه کولو لپاره هم همداسې کارول کېدای شي لکه د متغیرونو د ارزښتونو لپاره. د کوډ لاندې کرښې ته پام وکړئ:')
code(t, 'cin >> TestStr;')
P('cin object stops reading characters when it gets any blank space character, so in this case of entering strings, the object will get only one word. For example, if one wants to input a sentence using cin object, it will only accept the first word of the sentence and will discard the rest of the words.',
  'cin آبجیکٹ جب کوئی خالی جگہ (space) پاتا ہے تو حروف پڑھنا بند کر دیتا ہے، اس لیے اسٹرنگز داخل کرنے کی اس صورت میں آبجیکٹ صرف ایک لفظ حاصل کرے گا۔ مثال کے طور پر اگر کوئی cin آبجیکٹ کے ذریعے جملہ داخل کرنا چاہے تو یہ صرف جملے کا پہلا لفظ قبول کرے گا اور باقی الفاظ ترک کر دے گا۔',
  'cin شی کله چې کومه تشه (space) ومومي، د تورو لوستل بندوي، نو د تارونو د لیکلو په دې حالت کې شی یوازې یوه کلمه ترلاسه کوي. د بېلګې په توګه که څوک وغواړي د cin په مرسته یوه جمله ولیکي، یوازې د جملې لومړۍ کلمه مني او پاتې کلمې پرېږدي.')
P('In order to get entire line with spaces between the words, the function gets is used which is recommended by the programmers as compared to cin. Consider the following program demonstrating cin object for string.',
  'الفاظ کے درمیان خالی جگہوں سمیت پوری لائن حاصل کرنے کے لیے gets فنکشن استعمال ہوتا ہے جسے پروگرامرز cin کے مقابلے میں تجویز کرتے ہیں۔ اسٹرنگ کے لیے cin آبجیکٹ کی وضاحت کرنے والے درج ذیل پروگرام پر غور کریں۔',
  'د کلمو ترمنځ تشو سره د ټولې کرښې د ترلاسه کولو لپاره gets فنکشن کارول کېږي چې پروګرام جوړوونکي یې د cin په پرتله سپارښتنه کوي. د تار لپاره د cin شي ښودونکي لاندې پروګرام ته پام وکړئ.')
code(t, '''// cin with strings
#include <iostream.h>
#include<conio.h>
int main()
{
char TestStr[60];
cout << " Enter your name please \\n";
cin >>Test Str;
cout << "\\nYour name is" << TestStr;
getch();
return 0;
}''')
rec = BOOK.record(t, 'cs12-u3-text-12', 'Unit 3 text (12)', 'یونٹ 3 — متن (۱۲)', '۳ څپرکی — متن (۱۲)', 46, [80, 81])
rec['sourceNote'] = 'The output of the last program follows on p.82 (PDF47).'
issues = [{'id': 'cs12-pdf046', 'unit': 3, 'printedPage': 81,
           'description': 'The listing on p.81 prints “cin >>Test Str;” with a space inside the identifier (would not compile); p.80 prints the closing quote of “ years” as a curly quote. Both retained as printed. p.81 “the user need to enter”.'}]

if __name__ == '__main__':
    BOOK.save(46, [(3, rec)], issues=issues)
