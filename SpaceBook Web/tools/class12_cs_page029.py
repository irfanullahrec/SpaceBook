"""Computer Science XII PDF29 (spread): printed pp.46–47 — Example 2 listing (whole, from p.45); g. testing; h. deployment; i. maintenance; 2.1.6 role of personnel (list)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
code(t, '''/* program to display result s of the students*/
#include <iostream.h>
#include<conio.h>
int main ()
{
float Percentage;
cout<< "Enter Percentage of the student"<<endl;
cin>> Percentage;
if (Percentage >=60.0)
cout<< "Passed";
else
cout<< "Failed";
getch();
return 0;
}''')
H('g. Testing/Verification', 'g. جانچ/تصدیق', 'g. ازموینه/تایید')
P('The execution of a program to find its errors is called testing. Here, the bugs are identified in the programmed modules. The purpose of testing is to evaluate an attribute or capability of a program or system and determine that whether it meets its required results. Testing/verification the software is actually operating the software under controlled conditions. It is the process of checking the items for consistency by evaluating the results against pre-specified requirements.',
  'کسی پروگرام کو اس کی خرابیاں تلاش کرنے کے لیے چلانا جانچ (ٹیسٹنگ) کہلاتا ہے۔ یہاں پروگرام شدہ ماڈیولز میں خامیوں (bugs) کی نشاندہی کی جاتی ہے۔ جانچ کا مقصد کسی پروگرام یا نظام کی کسی خصوصیت یا صلاحیت کا جائزہ لینا اور یہ طے کرنا ہے کہ آیا وہ مطلوبہ نتائج پورے کرتا ہے۔ سافٹ ویئر کی جانچ/تصدیق دراصل سافٹ ویئر کو کنٹرول شدہ حالات میں چلانا ہے۔ یہ پہلے سے متعین ضروریات کے مقابلے میں نتائج کا جائزہ لے کر اشیاء کی ہم آہنگی جانچنے کا عمل ہے۔',
  'د یوه پروګرام اجرا د هغه د تېروتنو د موندلو لپاره ازموینه بلل کېږي. دلته په پروګرام شویو ماډیولونو کې نیمګړتیاوې (bugs) پېژندل کېږي. د ازموینې موخه د یوه پروګرام یا سیسټم د یوې ځانګړنې یا وړتیا ارزونه او دا ټاکل دي چې ایا اړینې پایلې پوره کوي. د سافټویر ازموینه/تایید په حقیقت کې د سافټویر په کنټرول شوو شرایطو کې چلول دي. دا د مخکې ټاکل شوو اړتیاوو په وړاندې د پایلو په ارزونې سره د توکو د همغږۍ د کتنې بهیر دی.')
H('h. Deployment / Implementation', 'h. تعیناتی / نفاذ', 'h. ځای پر ځای کول / پلي کول')
P('Software deployment is a set of activities that are used to make the software system available for use. The deployment is also called implementation. Its activities occur at the producer site or at the consumer site or both. Because every software system is unique, the precise processes or procedures within each activity are different from others and thus cannot be clearly defined.',
  'سافٹ ویئر کی تعیناتی سرگرمیوں کا ایک مجموعہ ہے جو سافٹ ویئر سسٹم کو استعمال کے لیے دستیاب بنانے کے لیے کی جاتی ہیں۔ تعیناتی کو نفاذ بھی کہا جاتا ہے۔ اس کی سرگرمیاں تیار کنندہ کے مقام پر یا صارف کے مقام پر یا دونوں جگہ ہوتی ہیں۔ چونکہ ہر سافٹ ویئر سسٹم منفرد ہوتا ہے، اس لیے ہر سرگرمی کے اندر درست عمل یا طریقۂ کار دوسروں سے مختلف ہوتے ہیں اور انھیں واضح طور پر متعین نہیں کیا جا سکتا۔',
  'د سافټویر ځای پر ځای کول د فعالیتونو یوه ټولګه ده چې سافټویري سیسټم د کارونې لپاره برابرولو ته کارول کېږي. ځای پر ځای کولو ته پلي کول هم ویل کېږي. فعالیتونه یې د جوړوونکي په ځای یا د مصرفوونکي په ځای یا دواړو کې کېږي. څرنګه چې هر سافټویري سیسټم ځانګړی دی، د هر فعالیت دننه دقیقې پروسې یا کړنلارې له نورو توپیر لري او په روښانه ډول نه شي ټاکل کېدای.')
P('The main activities that are involved during deployment are:', 'تعیناتی کے دوران شامل اہم سرگرمیاں یہ ہیں:', 'د ځای پر ځای کولو پر مهال اصلي فعالیتونه دا دي:')
t.group('list', [('Installation and activation of the equipments and software.', 'آلات اور سافٹ ویئر کی تنصیب اور فعالیت۔', 'د وسایلو او سافټویر نصبول او فعالول.'),
                 ('In some cases the users and the computer operation personals are trained on the developed software system.', 'بعض صورتوں میں صارفین اور کمپیوٹر آپریشن کے عملے کو تیار شدہ سافٹ ویئر سسٹم کی تربیت دی جاتی ہے۔', 'په ځینو حالاتو کې کاروونکي او د کمپیوټري چارو کارکوونکي پر جوړ شوي سافټویري سیسټم روزل کېږي.'),
                 ('Conversion: The process of changing from the old system to the new one is called conversion.', 'تبدیلی: پرانے نظام سے نئے نظام میں تبدیلی کے عمل کو کنورژن کہتے ہیں۔', 'بدلون: له زوړ سیسټم څخه نوي ته د بدلون بهیر ته کنورژن (conversion) ویل کېږي.')])
H('i. Maintenance / Support', 'i. دیکھ بھال / معاونت', 'i. ساتنه / ملاتړ')
P('Keeping a system in its proper working condition is called maintenance. In other words, it can also be defined as the modification of a software product after delivery to correct faults, to improve performance. Maintenance is an important activity that takes place throughout the life of software in both the computer equipments and computer software. Programmers spend more time in maintaining programs than writing them.',
  'کسی نظام کو اس کی درست کام کرنے کی حالت میں رکھنا دیکھ بھال (مینٹیننس) کہلاتا ہے۔ دوسرے لفظوں میں اسے خرابیاں دور کرنے اور کارکردگی بہتر بنانے کے لیے فراہمی کے بعد سافٹ ویئر پروڈکٹ میں ترمیم کے طور پر بھی بیان کیا جا سکتا ہے۔ دیکھ بھال ایک اہم سرگرمی ہے جو کمپیوٹر آلات اور کمپیوٹر سافٹ ویئر دونوں میں سافٹ ویئر کی پوری زندگی میں جاری رہتی ہے۔ پروگرامرز پروگرام لکھنے سے زیادہ وقت ان کی دیکھ بھال میں صرف کرتے ہیں۔',
  'د یوه سیسټم په سم کاري حالت کې ساتل ساتنه بلل کېږي. په بل عبارت، دا د تېروتنو د سمولو او د کارکردګۍ د ښه کولو لپاره له سپارلو وروسته د سافټویري محصول د بدلون په توګه هم تعریفېدای شي. ساتنه یو مهم فعالیت دی چې د سافټویر په ټول ژوند کې په کمپیوټري وسایلو او کمپیوټري سافټویر دواړو کې ترسره کېږي. پروګرام جوړوونکي د پروګرامونو په ساتنه کې تر لیکلو ډېر وخت لګوي.')
P('In SDLC, the system maintenance is an ongoing process. The system is monitored continually for performance in accordance with user requirements and needed system modifications are incorporated. When modifications are identified, the system may reenter the planning phase. This process continues until a complete solution is provided to the customer. Maintenance can be either be repairing or modification or some enhancement in the existing system.',
  'SDLC میں نظام کی دیکھ بھال ایک جاری عمل ہے۔ صارف کی ضروریات کے مطابق کارکردگی کے لیے نظام کی مسلسل نگرانی کی جاتی ہے اور ضروری ترامیم شامل کی جاتی ہیں۔ جب ترامیم کی نشاندہی ہو تو نظام دوبارہ منصوبہ بندی کے مرحلے میں داخل ہو سکتا ہے۔ یہ عمل اس وقت تک جاری رہتا ہے جب تک گاہک کو مکمل حل فراہم نہ ہو جائے۔ دیکھ بھال موجودہ نظام کی مرمت، ترمیم یا کچھ بہتری ہو سکتی ہے۔',
  'په SDLC کې د سیسټم ساتنه دوامداره بهیر دی. سیسټم د کاروونکي د اړتیاوو سره سم د کارکردګۍ لپاره په دوامداره ډول څارل کېږي او اړین بدلونونه پکې شاملېږي. کله چې بدلونونه وپېژندل شي، سیسټم کېدای شي بېرته د پلان جوړونې پړاو ته ننوځي. دا بهیر تر هغه دوام کوي چې پېرودونکي ته بشپړ حل برابر شي. ساتنه کېدای شي په اوسني سیسټم کې ترمیم، بدلون یا یو څه ښه والی وي.')
H('2.1.6 Role of the Personnel involved in SDLC', '2.1.6 ایس ڈی ایل سی میں شامل افراد کا کردار', '۲.۱.۶ په SDLC کې د ښکېلو کسانو رول')
P('The activities of all the phases of software development life cycle are being performed by different groups of people and individual personnel. These personnel are professionals in performing their particular jobs and include:',
  'سافٹ ویئر ڈویلپمنٹ لائف سائیکل کے تمام مراحل کی سرگرمیاں لوگوں کے مختلف گروہ اور انفرادی افراد انجام دیتے ہیں۔ یہ افراد اپنے مخصوص کام انجام دینے میں ماہر ہوتے ہیں اور ان میں شامل ہیں:',
  'د سافټویر د پراختیا د ژوند دورې د ټولو پړاوونو فعالیتونه د خلکو بېلابېلې ډلې او جلا کسان ترسره کوي. دا کسان د خپلو ځانګړو دندو په ترسره کولو کې مسلکي دي او په دوی کې شامل دي:')
t.group('list', [('Management', 'انتظامیہ', 'مدیریت'), ('Project Manager', 'پروجیکٹ مینیجر', 'د پروژې مدیر'), ('System Analyst', 'سسٹم اینالسٹ', 'د سیسټم شنونکی'),
                 ('Programmer', 'پروگرامر', 'پروګرام جوړوونکی'), ('Software Tester', 'سافٹ ویئر ٹیسٹر', 'د سافټویر ازموونکی'), ('Customer', 'گاہک', 'پېرودونکی')])
rec = BOOK.record(t, 'cs12-u2-text-8', 'Unit 2 text (8)', 'یونٹ 2 — متن (۸)', '۲ څپرکی — متن (۸)', 29, [45, 46, 47])
rec['sourceNote'] = 'Example 2 begins at the foot of p.45 (heading, comment, #include lines and int main ()) and continues on p.46; it is given whole here.'
issues = [{'id': 'cs12-pdf029', 'unit': 2, 'printedPage': 46,
           'description': 'The Example 2 comment prints “result s” (stray space); p.46 “determine that whether”, “Testing/verification the software is”; p.47 “operation personals”, “can be either be repairing”. Retained as printed. Heavy owner doodles/handwriting (“chart”, boxes) on pp.46–47 excluded.'}]

if __name__ == '__main__':
    BOOK.save(29, [(2, rec)], issues=issues)
