"""Computer Science XII PDF58 (spread): printed pp.104–105 — Unit 3 summary."""
from class12_cs_common import BOOK, Builder

s = Builder()
s.h('Summary', 'خلاصہ', 'لنډیز')
s.group('list', [
 ('C++ is a programming language developed by Bjarne Stroustrup which derives most of its features from C language.', 'C++ بیارنے اسٹراؤسٹرپ کی تیار کردہ پروگرامنگ زبان ہے جو اپنی زیادہ تر خصوصیات C زبان سے لیتی ہے۔', 'C++ د بیارنې سټراوسټروپ جوړه کړې پروګرامي ژبه ده چې ډېری ځانګړنې یې له C ژبې اخیستې.'),
 ('Each C++ program makes use of header files which have definitions for C++ objects.', 'ہر C++ پروگرام ہیڈر فائلیں استعمال کرتا ہے جن میں C++ آبجیکٹس کی تعریفیں ہوتی ہیں۔', 'هر C++ پروګرام سرلیک فایلونه کاروي چې د C++ شیانو تعریفونه لري.'),
 ('Pre-processor directives are the directives that are used to include header files to the C++ program.', 'پری پروسیسر ڈائریکٹوز وہ ہدایات ہیں جو C++ پروگرام میں ہیڈر فائلیں شامل کرنے کے لیے استعمال ہوتی ہیں۔', 'د مخکې پروسس لارښوونې هغه لارښوونې دي چې C++ پروګرام ته د سرلیک فایلونو د شاملولو لپاره کارول کېږي.'),
 ('C++ Comments are the explanatory statements that are usually added to the source program statements to make them understandable to the readers.', 'C++ تبصرے وضاحتی بیانات ہیں جو عموماً سورس پروگرام کے بیانات میں شامل کیے جاتے ہیں تاکہ قارئین انھیں سمجھ سکیں۔', 'د C++ تبصرې تشریحي بیانونه دي چې عموماً د سرچینې پروګرام بیانونو ته ورزیاتېږي څو لوستونکي پرې پوه شي.'),
 ('A C++ program needs variables to hold data upon which a programmer performs operations.', 'C++ پروگرام کو ایسا ڈیٹا رکھنے کے لیے ویری ایبلز درکار ہوتے ہیں جس پر پروگرامر عمل کرتا ہے۔', 'C++ پروګرام د هغې ډېټا د ساتلو لپاره متغیرونو ته اړتیا لري چې پروګرام جوړوونکی پرې عملیې کوي.'),
 ('Constant are those components of C++ language whose values cannot be changed during the execution of a program.', 'کانسٹنٹس C++ زبان کے وہ اجزاء ہیں جن کی قدریں پروگرام کے چلنے کے دوران تبدیل نہیں ہو سکتیں۔', 'ثابتونه د C++ ژبې هغه برخې دي چې ارزښتونه یې د پروګرام د اجرا پر مهال نه شي بدلېدای.'),
 ('Data types are the qualifiers that tell the compiler what type of data will be stored in a particular variable.', 'ڈیٹا ٹائپس وہ مخصِّصات ہیں جو کمپائلر کو بتاتی ہیں کہ کسی خاص ویری ایبل میں کس قسم کا ڈیٹا محفوظ ہوگا۔', 'ډېټا ډولونه هغه ټاکونکي دي چې کمپایلر ته وايي په یوه ځانګړي متغیر کې به څه ډول ډېټا ساتل کېږي.'),
 ('For the declaration of variables, one needs to select proper data type.', 'ویری ایبلز کے اعلان کے لیے مناسب ڈیٹا ٹائپ کا انتخاب ضروری ہے۔', 'د متغیرونو د اعلان لپاره باید مناسب ډېټا ډول وټاکل شي.'),
 ('C++ supports a wide range of data types, such as, int, float, double char etc.', 'C++ ڈیٹا ٹائپس کی ایک وسیع رینج کو سپورٹ کرتی ہے، جیسے int، float، double، char وغیرہ۔', 'C++ د ډېټا ډولونو پراخه لړۍ ملاتړ کوي، لکه int، float، double، char او نور.'),
 ('For getting input and producing output, C++ has a rich library of pre-defined and pre-compiled objects, cin and cout, and functions such as getch (), getchar (), gets, putch () and putchar ().', 'ان پٹ حاصل کرنے اور آؤٹ پٹ پیدا کرنے کے لیے C++ کے پاس پہلے سے متعین اور کمپائل شدہ آبجیکٹس cin اور cout اور getch()، getchar()، gets، putch() اور putchar() جیسے فنکشنز کی بھرپور لائبریری ہے۔', 'د ننوتنې د ترلاسه کولو او وتنې د تولید لپاره C++ د مخکې تعریف او کمپایل شویو شیانو cin او cout او د getch()، getchar()، gets، putch() او putchar() په څېر فنکشنونو بډای کتابتون لري.'),
 ("Escape sequences are special characters that start with back slash symbol ('\\'). The subsequent character after ('\\') symbol has special meaning.", "ایسکیپ سیکوینسز خاص حروف ہیں جو بیک سلیش علامت ('\\') سے شروع ہوتے ہیں۔ ('\\') علامت کے بعد والے حرف کا خاص مطلب ہوتا ہے۔", "د تېښتې لړۍ ځانګړي توري دي چې د شا سلیش نښې ('\\') سره پیلېږي. د ('\\') نښې وروسته توری ځانګړې معنا لري."),
 ('Operators are those symbols which operate over the operands.', 'آپریٹرز وہ علامات ہیں جو آپرینڈز پر عمل کرتی ہیں۔', 'چلونکي هغه نښې دي چې پر عملوندونو عمل کوي.'),
 ('C++ supports a wide range of operators to perform operations on operands.', 'C++ آپرینڈز پر عمل انجام دینے کے لیے آپریٹرز کی وسیع رینج کو سپورٹ کرتی ہے۔', 'C++ پر عملوندونو د عملیو د ترسره کولو لپاره د چلونکو پراخه لړۍ ملاتړ کوي.'),
 ('Arithmetic operators are those operators that are used in arithmetic expressions and perform arithmetic operations.', 'حسابی آپریٹرز وہ آپریٹرز ہیں جو حسابی ایکسپریشنز میں استعمال ہوتے ہیں اور حسابی اعمال انجام دیتے ہیں۔', 'حسابي چلونکي هغه دي چې په حسابي افادو کې کارول کېږي او حسابي عملیې ترسره کوي.'),
 ('Relational operators are used for comparing two values and return (1) if the condition is TRUE and (0) if FALSE.', 'ریلیشنل آپریٹرز دو قدروں کے موازنے کے لیے استعمال ہوتے ہیں اور شرط درست ہو تو (1) اور غلط ہو تو (0) واپس کرتے ہیں۔', 'اړیکه‌ییز چلونکي د دوو ارزښتونو د پرتلې لپاره کارول کېږي او که شرط TRUE وي (1) او که FALSE وي (0) ورکوي.'),
 ('Unary operators take one operand; binary operators take two operands and ternary operator takes there operands.', 'یونری آپریٹرز ایک آپرینڈ لیتے ہیں؛ بائنری آپریٹرز دو اور ٹرنری آپریٹر تین آپرینڈز لیتا ہے۔', 'یو-عملي چلونکي یو عملوند اخلي؛ دوه-عملي دوه او درې-عملي چلونکی درې عملوندونه اخلي.')])
sm = BOOK.record(s, 'cs12-u3-summary', 'Unit 3 summary', 'یونٹ 3: خلاصہ', '۳ څپرکی: لنډیز', 58, [104, 105])
issues = [{'id': 'cs12-pdf058', 'unit': 3, 'printedPage': 105,
           'description': 'The summary prints “Constant are those components”, “double char” (missing comma), “ternary operator takes there operands” (for “three”). Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(58, [(3, sm)], issues=issues)
