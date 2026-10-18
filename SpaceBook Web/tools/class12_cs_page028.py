"""Computer Science XII PDF28 (spread): printed pp.44–45 — iii. pseudo code (example); f. coding; Example 1 (C++ listing); Example 2 (begins)."""
from class12_cs_common import BOOK, Builder, code

t = Builder()
P = t.p
H = t.h
H('iii. Pseudo code', 'iii. سوڈو کوڈ', 'iii. شبه کوډ')
P('Pseudo code is an outline of a program, written in a form that can easily be converted into real programming statements. Pseudo code neither is compiled nor executed, and there is no specific formatting and syntax rules for it.',
  'سوڈو کوڈ کسی پروگرام کا خاکہ ہے جو ایسی شکل میں لکھا جاتا ہے جسے آسانی سے حقیقی پروگرامنگ بیانات میں تبدیل کیا جا سکے۔ سوڈو کوڈ نہ تو کمپائل ہوتا ہے نہ چلایا جاتا ہے، اور اس کے لیے کوئی مخصوص فارمیٹنگ اور نحوی قواعد نہیں ہیں۔',
  'شبه کوډ د پروګرام یوه خاکه ده چې په داسې بڼه لیکل کېږي چې په اسانۍ رښتینو پروګرامي بیانونو ته اړول کېدای شي. شبه کوډ نه کمپایل کېږي او نه اجرا کېږي، او ځانګړې بڼه‌ییزې او نحوي قاعدې نه لري.')
P('Pseudo code is beneficial in the sense that it enables the programmer to focus on the algorithms without worrying about all the syntactic details of a particular programming language. In fact, one can write pseudo code without even knowing what programming language will be used for the final implementation.',
  'سوڈو کوڈ اس لحاظ سے فائدہ مند ہے کہ یہ پروگرامر کو کسی خاص پروگرامنگ زبان کی تمام نحوی تفصیلات کی فکر کیے بغیر الگورتھمز پر توجہ مرکوز کرنے کے قابل بناتا ہے۔ درحقیقت سوڈو کوڈ یہ جانے بغیر بھی لکھا جا سکتا ہے کہ حتمی نفاذ کے لیے کون سی پروگرامنگ زبان استعمال ہوگی۔',
  'شبه کوډ په دې ګټور دی چې پروګرام جوړوونکي ته اجازه ورکوي چې د یوې ځانګړې پروګرامي ژبې د ټولو نحوي جزییاتو له فکر پرته پر الګوریتمونو تمرکز وکړي. په حقیقت کې شبه کوډ پرته له دې چې پوه شي د وروستي پلي کولو لپاره کومه پروګرامي ژبه کارېږي، لیکل کېدای شي.')
P('The following example shows a pseudo code to display the result of a student as “Pass” if the percentage is greater than or equal to 60% and “Fail” otherwise.',
  'درج ذیل مثال ایک سوڈو کوڈ دکھاتی ہے جو طالب علم کا نتیجہ ’’Pass‘‘ دکھاتا ہے اگر فیصد 60% یا اس سے زیادہ ہو، ورنہ ’’Fail‘‘۔',
  'لاندې بېلګه یو شبه کوډ ښيي چې د زده‌کوونکي پایله "Pass" ښيي که سلنه له ۶۰٪ لویه یا ورسره برابره وي، او که نه "Fail".')
code(t, '''IF Percentage >= 60%
Print "Pass"
Else
Print "Fail"''')
H('f. Coding', 'f. کوڈنگ', 'f. کوډ لیکنه')
P('Coding is the process of designing, writing, testing, debugging, and maintaining the source code of computer programs. This source code is written in programming languages. The purpose of coding is to create a program that shows a certain desired behavior. For coding some other specialties are also needed. These include knowledge of the application domain, specialized algorithms and formal logic. Coding is also called computer programming.',
  'کوڈنگ کمپیوٹر پروگراموں کے سورس کوڈ کو ڈیزائن کرنے، لکھنے، جانچنے، خرابیاں دور کرنے اور برقرار رکھنے کا عمل ہے۔ یہ سورس کوڈ پروگرامنگ زبانوں میں لکھا جاتا ہے۔ کوڈنگ کا مقصد ایسا پروگرام بنانا ہے جو ایک مطلوبہ رویہ ظاہر کرے۔ کوڈنگ کے لیے کچھ اور مہارتیں بھی درکار ہیں، جن میں ایپلیکیشن کے شعبے کا علم، خصوصی الگورتھمز اور رسمی منطق شامل ہیں۔ کوڈنگ کو کمپیوٹر پروگرامنگ بھی کہتے ہیں۔',
  'کوډ لیکنه د کمپیوټري پروګرامونو د سرچینې کوډ د ډیزاین، لیکلو، ازمویلو، د تېروتنو لرې کولو او ساتلو بهیر دی. دا د سرچینې کوډ په پروګرامي ژبو لیکل کېږي. د کوډ لیکنې موخه داسې پروګرام جوړول دي چې یو ټاکلی مطلوب چلند وښيي. د کوډ لیکنې لپاره ځینې نور مهارتونه هم اړین دي، لکه د کاريال د ساحې پوهه، ځانګړي الګوریتمونه او رسمي منطق. کوډ لیکنې ته کمپیوټري پروګرام‌سازي هم ویل کېږي.')
P('For coding computer programming languages are used. There are different types of programming languages such as procedural languages and object oriented programming (OOP) languages. Nowadays, object oriented programming languages are the most commonly used languages. C++, Java, C#.Net, and VB.Net etc. are the examples of this group of languages.',
  'کوڈنگ کے لیے کمپیوٹر پروگرامنگ زبانیں استعمال ہوتی ہیں۔ پروگرامنگ زبانوں کی مختلف اقسام ہیں جیسے پروسیجرل زبانیں اور آبجیکٹ اورینٹڈ پروگرامنگ (OOP) زبانیں۔ آج کل آبجیکٹ اورینٹڈ پروگرامنگ زبانیں سب سے زیادہ استعمال ہوتی ہیں۔ C++، Java، C#.Net اور VB.Net وغیرہ اس گروپ کی زبانوں کی مثالیں ہیں۔',
  'د کوډ لیکنې لپاره کمپیوټري پروګرامي ژبې کارول کېږي. د پروګرامي ژبو بېلابېل ډولونه شته لکه کړنلاریزې ژبې او شیانو ته متوجه پروګرام‌سازۍ (OOP) ژبې. نن ورځ شیانو ته متوجه ژبې تر ټولو ډېرې کارېږي. C++، Java، C#.Net او VB.Net او نورې د دې ډلې ژبو بېلګې دي.')
P('The coding style of the C++ programming language is shown as follows.', 'C++ پروگرامنگ زبان کا کوڈنگ انداز ذیل میں دکھایا گیا ہے۔', 'د C++ پروګرامي ژبې د کوډ لیکنې طرز لاندې ښودل شوی.')
H('Example 1', 'مثال 1', '۱ بېلګه')
code(t, '''/* program to add N numbers*/
#include <iostream.h>
#include<conio.h>
int main ()
{
int N, sum=0, y ;
cout<< "Enter value for N"<<endl;
cin>>N ;
for (int x=1 ; x<=N ; ++x)
{
cin>>y ;
sum= sum+y ;
}
cout<< "The sum of N values is: "<<sum;
getch();
return 0;
}''')
H('Example 2', 'مثال 2', '۲ بېلګه')
rec = BOOK.record(t, 'cs12-u2-text-7', 'Unit 2 text (7)', 'یونٹ 2 — متن (۷)', '۲ څپرکی — متن (۷)', 28, [44, 45])
rec['sourceNote'] = 'Program listings are kept exactly as printed (pre-standard headers such as <iostream.h> and getch()). Example 2 begins at the foot of p.45 and is given whole with PDF29.'

if __name__ == '__main__':
    BOOK.save(28, [(2, rec)])
