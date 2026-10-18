"""Computer Science XII PDF143–148: pp.274–275 Unit 9 text (Figure 9.8, b. string stream, Figures 9.9 and 9.12); p.276 summary; pp.277–278 exercise
(unit 9 complete); pp.279–281 Bibliography; pp.282–285 Answers.
Run: python class12_cs_page143.py N (143–148)."""
import sys
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import text_window

BM = ('Back Matter', 'آخری صفحات', 'وروستۍ پاڼې')


def win(t, vid, title, lines, caps, dark=False):
    sv = [text_window(title, lines, c, dark) for c in caps]
    t.visual(vid, sv[0][0], sv[1][0], sv[2][0], sv[0][1])


def same(t, kind, items):
    """Reference entries kept as printed in every language view."""
    start = len(t.paras)
    t.group(kind, [(s, s, s) for s in items])
    for p in t.paras[start:]:
        p['untranslatedByDesign'] = True


def p143():
    t = Builder()
    P = t.p
    P('When the above program is executed, characters are entered one by one from the keyboard.The characters entered above are written to the “characterswrite” file stored at secondary storage at location d-drive of the hard disk. The output file generated is shown in figure 9.8.',
      'جب اوپر کا پروگرام چلایا جاتا ہے تو کی بورڈ سے ایک ایک کر کے حروف داخل کیے جاتے ہیں۔ اوپر داخل کیے گئے حروف ہارڈ ڈسک کی d-drive پر ثانوی اسٹوریج میں محفوظ ’’characterswrite‘‘ فائل میں لکھے جاتے ہیں۔ بننے والی آؤٹ پٹ فائل شکل 9.8 میں دکھائی گئی ہے۔',
      'کله چې پورته پروګرام اجرا شي، توري له کیبورډ یو په یو لیکل کېږي. پورته لیکل شوي توري "characterswrite" دوتنې ته لیکل کېږي چې د هارډ ډیسک په d-drive کې په ثانوي زېرمه کې ساتل شوې. جوړه شوې د وتنې دوتنه په ۹.۸ شکل کې ښودل شوې.')
    win(t, 'cs12-fig-9-8', 'C:\\BC5\\BIN\\NONAME00.exe', ['C++ is a powerful language.'], ('Figure 9.8: File Written by Character Stream', 'شکل 9.8: کریکٹر اسٹریم کے ذریعے لکھی گئی فائل', '۹.۸ شکل: د یو توري بهیر په مرسته لیکل شوې دوتنه'), dark=True)
    t.h('b. String stream', 'b. اسٹرنگ اسٹریم', 'b. د تار بهیر')
    P('A string stream is a stream which reads input from or writes output to an associated string.Consider the text file “stringread” shown in figure 9.9.', 'اسٹرنگ اسٹریم وہ اسٹریم ہے جو کسی وابستہ اسٹرنگ سے ان پٹ پڑھتی یا اس میں آؤٹ پٹ لکھتی ہے۔ شکل 9.9 میں دکھائی گئی ٹیکسٹ فائل ’’stringread‘‘ پر غور کریں۔', 'د تار بهیر هغه بهیر دی چې له یوه تړلي تار ننوتنه لولي یا ورته وتنه لیکي. په ۹.۹ شکل کې ښودل شوې "stringread" متني دوتنې ته پام وکړئ.')
    win(t, 'cs12-fig-9-9', 'stringread - Notepad', ['"Intellectual Growth Should Commence At Birth And Cease Only At Death"'],
        ('Figure 9.9: Input File that will be Read using String Stream', 'شکل 9.9: اسٹرنگ اسٹریم کے ذریعے پڑھی جانے والی ان پٹ فائل', '۹.۹ شکل: د تار بهیر په مرسته د لوستلو وړ د ننوتنې دوتنه'))
    P('The following program reads this file (stringread.txt) into string (str) using getline() function and display the result on the screen as shown in figure 9.10.', 'درج ذیل پروگرام getline() فنکشن کے ذریعے اس فائل (stringread.txt) کو اسٹرنگ (str) میں پڑھتا ہے اور نتیجہ اسکرین پر دکھاتا ہے جیسا کہ شکل 9.10 میں دکھایا گیا ہے۔', 'لاندې پروګرام د getline() فنکشن په مرسته دا دوتنه (stringread.txt) په تار (str) کې لولي او پایله پر پرده ښيي لکه په ۹.۱۰ شکل کې.')
    code(t, '''//string stream (read) program
#include <conio.h>
#include <iostream.h>
#include <fstream.h>
#include <string>
int main()
{
char str[20];
ifstream reads("d:\\\\stringread.txt");
while(!reads.eof())
{
reads.getline(str,21);
cout<<str<<endl;
}
reads.close();
getch();
return 0;
}''')
    win(t, 'cs12-fig-9-12', 'C:\\BC5\\BIN\\NONAME0...', ['ôIntellectual Growth', ' Should Commence At', 'Birth And Cease Only', ' At Deathö'],
        ('Figure 9.12: File Read by String Stream', 'شکل 9.12: اسٹرنگ اسٹریم کے ذریعے پڑھی گئی فائل', '۹.۱۲ شکل: د تار بهیر په مرسته لوستل شوې دوتنه'), dark=True)
    r = BOOK.record(t, 'cs12-u9-text-8', 'Unit 9 text (8)', 'یونٹ 9 — متن (۸)', '۹ څپرکی — متن (۸)', 143, [274, 275])
    r['sourceNote'] = 'Figures 9.8, 9.9 and 9.12 (console and Notepad windows) are redrawn as coded mock-ups with their printed contents, including the stray ô/ö marks the console shows in place of the quotation marks. The string-read program runs from p.274 to p.275 and is given whole.'
    BOOK.save(143, [(9, r)], issues=[{'id': 'cs12-pdf143', 'unit': 9, 'printedPage': 275,
               'description': 'The text says the result is “shown in figure 9.10” but the console figure on p.275 is captioned “Figure 9.12”; no Figures 9.6, 9.10 or 9.11 are printed. The program declares char str[20] but reads 21 characters. Retained as printed.'}])


def p144():
    s = Builder()
    s.h('Summary', 'خلاصہ', 'لنډیز')
    s.group('list', [
     ('The combinations of characters, words and records is called files.', 'حروف، الفاظ اور ریکارڈز کے مجموعے فائلز کہلاتے ہیں۔', 'د تورو، کلمو او ریکارډونو ترکیبونه دوتنې بلل کېږي.'),
     ('The process of opening, reading from and writing into files is termed as handling files.', 'فائلز کو کھولنے، ان سے پڑھنے اور ان میں لکھنے کا عمل فائلز ہینڈل کرنا کہلاتا ہے۔', 'د دوتنو د پرانیستلو، له هغو د لوستلو او پکې د لیکلو بهیر د دوتنو چلول بلل کېږي.'),
     ('There are two types of files: text files and binary files.', 'فائلز کی دو اقسام ہیں: ٹیکسٹ فائلز اور بائنری فائلز۔', 'دوتنې دوه ډوله دي: متني دوتنې او باینري دوتنې.'),
     ('Those files that store data in text format and are readable by human are called text file.', 'وہ فائلز جو ڈیٹا کو ٹیکسٹ شکل میں محفوظ کرتی ہیں اور انسان پڑھ سکتے ہیں، ٹیکسٹ فائل کہلاتی ہیں۔', 'هغه دوتنې چې ډېټا په متني بڼه ساتي او انسان یې لوستلی شي، متني دوتنه بلل کېږي.'),
     ('Binary files are those files that store data in binary format which is not readable by the human but readable by the computers. Binary files are directly processed by the computers', 'بائنری فائلز وہ فائلز ہیں جو ڈیٹا کو بائنری شکل میں محفوظ کرتی ہیں جو انسان نہیں بلکہ کمپیوٹر پڑھ سکتے ہیں۔ بائنری فائلز پر کمپیوٹر براہِ راست عمل کرتے ہیں', 'باینري دوتنې هغه دوتنې دي چې ډېټا په باینري بڼه ساتي چې انسان یې نه شي لوستلی خو کمپیوټرونه یې لوستلی شي. پر باینري دوتنو کمپیوټرونه مستقیم پروسس کوي'),
     ('To open a file, the function open() is used.', 'فائل کھولنے کے لیے فنکشن open() استعمال ہوتا ہے۔', 'د دوتنې د پرانیستلو لپاره open() فنکشن کارېږي.'),
     ('There are different modes of opening files i.e. binary mode, input mode and output mode.', 'فائلز کھولنے کے مختلف موڈز ہیں یعنی بائنری موڈ، ان پٹ موڈ اور آؤٹ پٹ موڈ۔', 'د دوتنو د پرانیستلو بېلابېل حالتونه دي، یعنې باینري حالت، د ننوتنې حالت او د وتنې حالت.'),
     ('The bof( ) is a pointer which is true if the current position of the pointer is at the beginning of the input file stream, and false otherwise.', 'bof( ) ایک پوائنٹر ہے جو true ہوتا ہے اگر پوائنٹر کا موجودہ مقام ان پٹ فائل اسٹریم کے آغاز پر ہو، ورنہ false۔', 'bof( ) یو پوائنټر دی چې true وي که د پوائنټر اوسنی ځای د ننوتنې دوتنې بهیر په پیل کې وي، او که نه false.'),
     ('The eof( ) is a pointer which returns true when there are no more data to be read from an input file stream, and false otherwise.', 'eof( ) ایک پوائنٹر ہے جو true واپس کرتا ہے جب ان پٹ فائل اسٹریم سے پڑھنے کے لیے مزید ڈیٹا نہ ہو، ورنہ false۔', 'eof( ) یو پوائنټر دی چې true بېرته ورکوي کله چې د ننوتنې دوتنې له بهیر د لوستلو لپاره نور ډېټا نه وي، او که نه false.'),
     ('A stream can be thought of a sequence of bytes of varying length that is used as a buffer to hold data that is waiting to be processed', 'اسٹریم کو مختلف لمبائی کے بائٹس کی ترتیب سمجھا جا سکتا ہے جو عمل کے منتظر ڈیٹا کو رکھنے کے لیے بفر کے طور پر استعمال ہوتی ہے', 'بهیر د بېلابېل اوږدوالي د بایټونو لړۍ ګڼل کېدای شي چې د پروسس په تمه ډېټا د ساتلو لپاره د بفر په توګه کارېږي')])
    sm = BOOK.record(s, 'cs12-u9-summary', 'Unit 9 summary', 'یونٹ 9: خلاصہ', '۹ څپرکی: لنډیز', 144, [276])
    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. In C++ language, for handling of files, the header file ________ is used.', 'i. C++ زبان میں فائلز ہینڈل کرنے کے لیے ہیڈر فائل ________ استعمال ہوتی ہے۔', 'i. په C++ ژبه کې د دوتنو د چلولو لپاره ________ سرپاڼه دوتنه کارېږي.'),
     ('ii. The function ________ is used for closing a function.', 'ii. فنکشن ________ فنکشن بند کرنے کے لیے استعمال ہوتا ہے۔', 'ii. ________ فنکشن د فنکشن د تړلو لپاره کارېږي.'),
     ('iii. In the statement, open (“xyz.txt”, ios::out); ________ file is opened in output mode.', 'iii. بیان open (“xyz.txt”, ios::out); میں ________ فائل آؤٹ پٹ موڈ میں کھولی جاتی ہے۔', 'iii. په open (“xyz.txt”, ios::out); بیان کې ________ دوتنه د وتنې په حالت کې پرانیستل کېږي.'),
     ('iv. If all output operations are to be performed at the end of the file then ________ should be used in the open function.', 'iv. اگر تمام آؤٹ پٹ عمل فائل کے آخر پر کرنے ہوں تو open فنکشن میں ________ استعمال ہونا چاہیے۔', 'iv. که ټولې د وتنې عملیې د دوتنې په پای کې ترسره کېږي، نو په open فنکشن کې باید ________ وکارول شي.'),
     ('v. A ________ is “a continuous flow or succession of bytes a stream of characters.”', 'v. ________ ’’بائٹس کا مسلسل بہاؤ یا تسلسل، حروف کی ایک اسٹریم‘‘ ہے۔', 'v. ________ "د بایټونو دوامداره بهیر یا لړۍ، د تورو یو بهیر" دی.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    NA = ('none of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')
    e.mcq('i.', ('eof stands for ________ .', 'eof کا مطلب ہے ________ ۔', 'eof د ________ لنډون دی.'), ['errors-on-files', 'end-of-file', 'exit-of-file', NA], per_line=1)
    e.mcq('ii.', ('In file handling open() function is used ________ .', 'فائل ہینڈلنگ میں open() فنکشن ________ استعمال ہوتا ہے۔', 'د دوتنو په چلولو کې open() فنکشن ________ کارېږي.'),
          [('to open C++ compiler', 'C++ کمپائلر کھولنے کے لیے', 'د C++ کمپایلر د پرانیستلو لپاره'), ('to open a file', 'فائل کھولنے کے لیے', 'د دوتنې د پرانیستلو لپاره'), ('both a and b', 'a اور b دونوں', 'a او b دواړه'), NA], per_line=1)
    e.mcq('iii.', ('Default mode parameter for ofstream is ________ .', 'ofstream کا ڈیفالٹ موڈ پیرامیٹر ________ ہے۔', 'د ofstream ډیفالټ حالت پاراميټر ________ دی.'), ['ios::out', 'ios::in', 'ios::binary', ('both a and b', 'a اور b دونوں', 'a او b دواړه')], per_line=1)
    e.mcq('iv.', ('A text file has the extension ________ .', 'ٹیکسٹ فائل کی ایکسٹینشن ________ ہوتی ہے۔', 'متني دوتنه ________ تمدید لري.'), ['.doc', '.docx', '.txt', '.bin'], per_line=1)
    e.mcq('v.', ('ios::binary is used as an argument to open() function for ________ .', 'ios::binary فنکشن open() کو ________ کے لیے بطور آرگیومنٹ استعمال ہوتا ہے۔', 'ios::binary د open() فنکشن ته د ________ لپاره د دلیل په توګه کارېږي.'),
          [('opening file for input operation.', 'ان پٹ عمل کے لیے فائل کھولنا', 'د ننوتنې عملیې لپاره دوتنه پرانیستل'), ('opening file for output operation.', 'آؤٹ پٹ عمل کے لیے فائل کھولنا', 'د وتنې عملیې لپاره دوتنه پرانیستل'),
           ('opening file in binary mode.', 'بائنری موڈ میں فائل کھولنا', 'په باینري حالت کې دوتنه پرانیستل'), ('none of the above.', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')], per_line=1)
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. A string stream is a stream which reads input from or writes output to an associated string.', 'i. اسٹرنگ اسٹریم وہ اسٹریم ہے جو کسی وابستہ اسٹرنگ سے ان پٹ پڑھتی یا اس میں آؤٹ پٹ لکھتی ہے۔', 'i. د تار بهیر هغه بهیر دی چې له یوه تړلي تار ننوتنه لولي یا ورته وتنه لیکي.'),
     ('ii. The eof( )is a pointer which returns false when there are no more data to be read from an input file stream, and true otherwise.', 'ii. eof( ) ایک پوائنٹر ہے جو false واپس کرتا ہے جب ان پٹ فائل اسٹریم سے پڑھنے کے لیے مزید ڈیٹا نہ ہو، ورنہ true۔', 'ii. eof( ) یو پوائنټر دی چې false بېرته ورکوي کله چې د ننوتنې دوتنې له بهیر د لوستلو لپاره نور ډېټا نه وي، او که نه true.'),
     ('iii. To open a file in binary mode, we need to set the file mode to ios::binary.', 'iii. فائل کو بائنری موڈ میں کھولنے کے لیے ہمیں فائل موڈ ios::binary پر سیٹ کرنا ہوتا ہے۔', 'iii. د دوتنې په باینري حالت کې د پرانیستلو لپاره باید د دوتنې حالت ios::binary ته وټاکو.'),
     ('iv. close() Function is used in C++ file handling for opening a new file.', 'iv. close() فنکشن C++ فائل ہینڈلنگ میں نئی فائل کھولنے کے لیے استعمال ہوتا ہے۔', 'iv. close() فنکشن د C++ د دوتنو په چلولو کې د نوې دوتنې د پرانیستلو لپاره کارېږي.'),
     ('v. Those files that store data in text format and are readable by human are called text file', 'v. وہ فائلز جو ڈیٹا کو ٹیکسٹ شکل میں محفوظ کرتی ہیں اور انسان پڑھ سکتے ہیں، ٹیکسٹ فائل کہلاتی ہیں', 'v. هغه دوتنې چې ډېټا په متني بڼه ساتي او انسان یې لوستلی شي، متني دوتنه بلل کېږي')])
    for q, en, ur, ps in [
        ('Q.4', 'Define file. Describe different types of file.', 'فائل کی تعریف کریں۔ فائل کی مختلف اقسام بیان کریں۔', 'دوتنه تعریف کړئ. د دوتنې بېلابېل ډولونه بیان کړئ.'),
        ('Q.5', 'Describe different types of operations performed on the files.', 'فائلز پر کیے جانے والے مختلف قسم کے عمل بیان کریں۔', 'پر دوتنو د ترسره کېدونکو عملیو بېلابېل ډولونه بیان کړئ.'),
        ('Q.6', 'Define streams. Describe input and output streams in detail.', 'اسٹریمز کی تعریف کریں۔ ان پٹ اور آؤٹ پٹ اسٹریمز تفصیل سے بیان کریں۔', 'بهیرونه تعریف کړئ. د ننوتنې او وتنې بهیرونه په تفصیل بیان کړئ.'),
        ('Q.7', 'What is meant by the term mode of file opening? Describe different modes of opening file.', 'فائل کھولنے کے موڈ کی اصطلاح سے کیا مراد ہے؟ فائل کھولنے کے مختلف موڈز بیان کریں۔', 'د دوتنې د پرانیستلو د حالت اصطلاح څه معنا لري؟ د دوتنې د پرانیستلو بېلابېل حالتونه بیان کړئ.'),
        ('Q.8', 'What is file handling? Explain it in detail.', 'فائل ہینڈلنگ کیا ہے؟ تفصیل سے وضاحت کریں۔', 'د دوتنو چلول څه دي؟ په تفصیل یې تشریح کړئ.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    ex = BOOK.record(e, 'cs12-u9-exercise', 'Unit 9 exercise', 'یونٹ 9: مشق', '۹ څپرکی: تمرین', 144, [277, 278])
    ex['sourceNote'] = 'The exercise runs from p.277 to p.278 (PDF145) and is recorded here whole.'
    BOOK.save(144, [(9, sm), (9, ex)], complete_units=[9], issues=[{'id': 'cs12-pdf144', 'unit': 9, 'printedPage': 277,
               'description': 'Summary: “The combinations … is called files”; Q1(ii) asks for the function used “for closing a function”; Q1(v) “bytes a stream of characters”. Retained as printed.'}])


BIB = [
    '1. Basic Computer: Operating System Functions. [Cited 2011 Jun 10]; Available from: http://www.comptechdoc.org/basic/basictut/.',
    '2. Stalling, W., Operating Systems: Internals and Design Principles. Sixth ed. 2009: Macmillan, New York.',
    '3. Operating System. Webopedia (N.D) [cited; Available from: http://www.webopedia.com/TERM/O/operating_system.html.',
    '4. Silberschatz, Galvin, and Gagne, Operating System Concepts. Seventh ed: Addison-Wesley Inc.',
    '5. Ritchie, C., Operating System Incorporating Unix and MS-DOS. 2nd ed. 1997: BPB Publication, Delhi. 232.',
    '6. Common Operating Systems: Microsoft DOS. (N.D) [cited 2011 May, 20th]. Available from: http://www.wiley.com/college/busin/icmis/oakman/outline/chap05/misc/dos.htm.',
    '7. DOS (Disk Operating System). 2004-04-03 [SB] Last Updated: 2010-05-14 [cited 2011 April, 20th]; Available from: http://www.operating-system.org/betriebssystem/_english/bs-msdos.htm.',
    '8. Unix Tutorials: Introduction to the UNIX Operating System 19 October 2001 [cited 2011 April 17]; Available from: http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html.',
    '9. History of Mac OS, in Wikipedia. 2008.',
    '10. Common Operating Systems: Macintosh System 7.5 (Apple). [cited 2011 March 28]; Available from: http://www.wiley.com/college/busin/icmis/oakman/outline/chap05/misc/mac.htm.',
    '11. Harvey M. Deitel, Paul J. Deitel, and D.R. Choffues, Operating Systems (3rd Edition). 3rd ed. 2004.',
    '12. Multi Programming Operating System. June 2, 2011 [cited 2011 Jun 10]; Available from: http://easy2teach.net/operating-system/multi-programming-operating-system.',
    '13. Stankovic, I.A., Real-Time Computing. 1992, Department of Computer Science, University ofMassacusetts.',
    '14. Fry, G. Real Time Systems. [cited 2011 May 10]; Available from: http://cs-people.bu.edu/gfry/realtime.html.',
    '15. Physical Oceanographic Real-Time System (PORTS®). [Cited 2011 April 8]; Available from: http://tidesandcurrents.noaa.gov/ports.html.',
    '16. Tanenbaum, A.S., Modern Operating Systems. 3rd ed. 2008 Prentice-Hall.',
    '17. Blaise Barney and L. Livermore, Introduction to Parallel Computing, National Laboratory.',
    '18. Alecu, F., Operating System for Parallel Processing. Studies in Informatics and Control, 2004. 13(2).',
    '19. Tannenbaum and M.v. Steen, Distributed Systems. 2001: Prentice Hall.',
    '20. Operating Systems Services and Functions. UzEE November 4, 2007 [cited 2011 March 2]; Available from: http://uzeeinc.wordpress.com/2007/11/04/operating-systems-services-and-functions/',
    '21. Muhammad, R..B. Operating Systems Lecture Notes: System Components. [Cited 2011 Jun 01]; Available from: http://www.personal.kent.edu/~rmuhamma/OpSystems/os.html.',
    '22. What Does an Operating System Do? 2009 [cited 2011 May 7]; Available from: http://computerspot.net/what-does-an-operating-system-do/.',
    '23. File management system, in Webopedia, Webopedia.',
    '24. Bhat, P.C.P. Operating Systems/Input Output (IO) management Lecture Notes Volume,',
    '25. Dean, T., Comptia Network+ 2009 in Depth. 2009. 767.',
    '26. Operating System Notes: Threads. [Cited 2011 May 21]; Available from: http://www.personal.kent.edu/~rmuhamma/OpSystems/Myos/threads.htm.',
    '27. Joydip Kanjilal, Operating Systems: Coneeptsand Terminologies, 31 Jul 2006, [cited 12, Dee 2011]',
    '28. Aggarwal, K.K., Software Engineering: Revised Edition ed. 2001: New age international publisher. 494.',
    '29. Goldsmith, R.F. Software development life cycle phases, iterations, explained step by step. Available from: www.SearchSoftwareQuality.com.',
    '30. Gary B. Shelly, Thomas J. Cashman, and H.J. Rosenblatt, System Analysis and Design, Eight ed. 2009.',
    '31. Ankur Patel, Sagar Padaliya, and D. Pande. SDLC Methodologies. [cited 2011 Jun 12]; Available from: http://community.mis.temple.edu/fox20/about/.',
    '32. bijayani. SDLC. 2010 [cited 2011 Jun, 11 ]; Available from: http://bijayani.wordpress.com/2010/02/15/sdlc/.',
    '33. Pressman, R., Software Engineering: A Practitioner\'s Approach. seventh ed. 2010: McGraw-Hill Higher Education.',
    '34. Hemphill, M. MIS for digital age: Systems Development Lifecycle. February 4, 2004 [cited 2011 Jun, 02]; Available from: http://exonous.typepad.com/mis/2004/02/systems_develop.html.',
    '35. Sommerville, Software Enginering. Eight ed. 2008: Addision Wesely Publisher Limited 864.',
    '36. Wasson, C.S., System analysis, design, and development: concepts, principles and Practices.1005 John Wiley & Sons Inc. 818.',
    '37. Glossary of Computer Systems Software Development Terminology (8/95)',
    '38. "What is C++." [cited May 28, 2011]; 2005, Available from: http://www.hitmill.com/programming/cpp/whatiscpp.html.',
    '39. Stair, and Ralph M t et al., Principles of Information Systems. Sixth ed.: Thomson Learning, Inc, 2003.',
    '40. Program. [cited May 28, 2011]; Available from: http://www.webopedia.com/TERM/P/program.html.',
    '41. "C++ : Documentation: C++ Language Tutorial." [Cited May 2. 2011J: Available from: http://www.cplusplus.com.',
    '42. Alex, "The C++ Tutorial.", [cited April, 2011]; available from: http://www.learncpp.com/. 2007.',
    '43. "Types of Constants in C++." [cited May 19, 2011]; Available from: http://www.adiwebs.com/types-of-constants-in-c/.',
    '44. Sripriya, R., "C++ Manipulators." 2007. [last updated lith Nov 2008]. [cited 2011 29th May]; Available from: http://www.exforsys.com/tutorials/c-plus-plus/c-manipulators.html.',
    '45. "C++ lessons and Topics: FunctionX Tutorial", available from: http://www.functionx.com/, Last updated: Monday, June I3, 201 L',
    '46. Robert Lafore, "Object-Oriented Programming in C++", 4th Edition, Dee 29, 2001.',
    '47. Nicolai M. Josuttis, "Object-Oriented Programming in C++", December 30, 2002.',
    '48. Paul Deitel and Harvey M. Deitel, "C++ How to Program", 7th Edition. Aug 16, 2009.',
    '49. Paul Deitel and Harvey Deitel, "C++ How to Program (8th Edition)". Mar 25, 2011.',
    '50. "String in C++", [cited 04, Jan 2012], available from: http://anaturb.net/C/string_exapm.htm',
    '51. Bjarne Stroustrup\'s C++ Glossary, Modified, February 19, 2007, available from: http://www2.research.att.com/~bs/glossary.html',
]


def p145():
    e = Builder()
    rec_note = 'The end of the Unit 9 exercise on p.278 (Q2 iv–v, Q3, Q4–Q8) is recorded whole with PDF144.'
    b = Builder()
    b.h('Bibliography', 'کتابیات', 'کتاب‌نامه')
    same(b, 'lines', BIB[:15])
    r = BOOK.record(b, 'cs12-bm-bibliography-1', 'Bibliography (1)', 'کتابیات (۱)', 'کتاب‌نامه (۱)', 145, [279, 280], unit_title=BM)
    r['sourceNote'] = rec_note + ' Bibliography entries are kept as printed in every language view (titles, typos and dates as in the book). Web addresses blurred by the scan are given in their legible form; entry 15 ends at the top of p.280.'
    BOOK.save(145, [('BM', r)], issues=[{'id': 'cs12-pdf145', 'unit': 'BM', 'printedPage': 279,
               'description': 'Bibliography: “Stalling, W.” (Stallings), “University ofMassacusetts”, “Real-Time System (PORTS®)” as printed. Retained.'}])


def p146():
    b = Builder()
    same(b, 'lines', BIB[15:])
    r = BOOK.record(b, 'cs12-bm-bibliography-2', 'Bibliography (2)', 'کتابیات (۲)', 'کتاب‌نامه (۲)', 146, [280, 281])
    r['sourceNote'] = 'The top line of p.280 (the end of entry 15) is recorded with PDF145. Entries are kept as printed in every language view; web addresses blurred by the scan are given in their legible form.'
    BOOK.save(146, [('BM', r)], issues=[{'id': 'cs12-pdf146', 'unit': 'BM', 'printedPage': 280,
               'description': 'Bibliography entries 27 (“Coneeptsand”, “Dee 2011”), 35 (“Enginering”, “Addision Wesely”), 41 (“2011J”), 44 (“lith Nov”), 45 (“June I3, 201 L”) and 46 (“Dee 29”) contain printing errors. Retained as printed.'}])


ROM = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
QH = [('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں', 'پوښتنه ۱: تش ځایونه'), ('Q.2 Multiple Choice Questions.', 'سوال 2: کثیر الانتخابی سوالات', 'پوښتنه ۲: څو ځوابه پوښتنې'),
      ('Q.3 TRUE/FALSE statements.', 'سوال 3: صحیح/غلط بیانات', 'پوښتنه ۳: سم/ناسم بیانونه')]
ANS = {
    1: (['Multiprocessing', 'Multiple Tasks', 'Multiprogramming', 'Exit', 'UNIX'], list('bccabbdaba'), list('TTTTFFFFFT')),
    2: (['Functional', 'Deployment', 'System Analyst', 'Programmer', 'Project management'], list('cdaabad'), list('TFTFT')),
    3: (['0x', 'Conditional operator', 'True/False', 'Initialization', 'main( )'], list('baaac'), list('FFFTF')),
    4: (['Enclosed within a block', 'The value returned by a conditional expression', 'Default', 'Exit', 'iteration'], list('cbebddcacc'), list('FTTTF')),
    5: (['0', '10', 'Multidimensional', 'String', 'float'], list('badcc'), list('FTFTF')),
    6: (['One', 'Semicolon (;)', 'Throughout the program', 'Function overloading', 'Void'], list('ccaad'), list('TFFFT')),
    7: (['Address', 'int', 'Initialization', 'Reference', 'Dereference'], list('acacb'), list('FFTTT')),
    8: (['Constructor', 'Inheritance', 'Code reusability', 'Class', 'Polymorphism'], list('bcdcc'), list('FTTFT')),
    9: (['<fstream.h>', 'close', 'xyz.txt', 'Ios::app', 'stream'], list('bbacc'), list('TFTFT')),
}


def answers(units, pdf, pages, n, head):
    b = Builder()
    if head:
        b.h('Answers', 'جوابات', 'ځوابونه')
    for u in units:
        b.h(f'Unit {u}', f'یونٹ {u}', f'{u} څپرکی')
        for k, (ans, q) in enumerate(zip(ANS[u], QH)):
            b.p(*q)
            hdr = ROM[:len(ans)]
            b.table(f'cs12-answers-u{u}-q{k + 1}', hdr, [ans], hdr, hdr, [ans], [ans])
    r = BOOK.record(b, f'cs12-bm-answers-{n}', f'Answers ({n})', f'جوابات ({n})', f'ځوابونه ({n})', pdf, pages)
    r['sourceNote'] = 'Each answer grid is reproduced as a structured table (question numbers as the header row, answers as printed below). Answers are given as printed and are kept the same in every language view.'
    return r


def p147():
    BOOK.save(147, [('BM', answers([1, 2, 3, 4], 147, [282, 283], 1, True))], issues=[{'id': 'cs12-pdf147', 'unit': 'BM', 'printedPage': 283,
               'description': 'Unit 4 Q2 lists ten answers (i–x) although the exercise has nine MCQs, and answer iii is “e” (options run a–d); Unit 1 Q1 i is printed as capital “I”. Retained as printed.'}])


def p148():
    BOOK.save(148, [('BM', answers([5, 6, 7, 8, 9], 148, [284, 285], 2, False))], issues=[{'id': 'cs12-pdf148', 'unit': 'BM', 'printedPage': 285,
               'description': 'Unit 9 Q1 iv is printed “Ios::app”. Retained as printed. Unit 7 Q2/Q3 answer grids are printed at the top of p.285 under no unit label and are assigned to Unit 7 as their position shows.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 143
    {143: p143, 144: p144, 145: p145, 146: p146, 147: p147, 148: p148}[n]()
