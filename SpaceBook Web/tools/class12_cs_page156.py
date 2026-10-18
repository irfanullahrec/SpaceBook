"""Computer Science XII PDF156–166: p.300 glossary end + pp.301–302 Index; pp.303–304 Annexure 1 (figures); p.305 Annexure 2 (tables);
pp.306–307 Annexures 3–4 (symbols, commands); pp.308–309 Annexure 5 (built-in functions); pp.310–314 Annexure 6 (ASCII codes);
pp.315–316 About Authors; unnumbered Al-Hujurat page; back cover (National Anthem, imprint).
Run: python class12_cs_page156.py N (156–166)."""
import sys
from class12_cs_common import BOOK, Builder
from class12_cs_page149 import build as glossary
from class12_cs_figs import symbols_table

BM = 'BM'


def same(b, kind, items):
    start = len(b.paras)
    b.group(kind, [(s, s, s) for s in items])
    for p in b.paras[start:]:
        p['untranslatedByDesign'] = True


def neutral_table(b, tid, H, rows, Hu, Hp):
    b.table(tid, H, rows, Hu, Hp, rows, rows)


IDX1 = {'A': [('Algorithms', 42), ('Array', 146)],
        'B': [('Batch processing operating system', 8), ('Binary files', 260), ('bof()', 268), ('break statement', 122), ('Built-in Functions', 177)],
        'C': [('cin', 79), ('Class', 228), ('Coding', 44), ('Compound expression', 103), ('Constants', 65), ('Constructor', 239), ('continue statement', 135), ('cout', 78), ('Customer', 51)],
        'D': [('Data hiding', 238), ('Decision statements', 110), ('Dereference operator *', 218), ('Destructors', 247), ('Distributed operating system', 15), ('do- while loop', 132), ('DOS', 3)],
        'E': [('Embedded operating system', 16), ('eof()', 268), ('Escape sequences', 85), ('exit () function', 123), ('Expression', 101)],
        'F': [('File handling', 259), ('Flow chart', 42), ('for loop', 124), ('Function', 176), ('Function overloading', 204)],
        'G': [('Global variables', 187)],
        'I': [('if statement', 110), ('Inheritance', 249)],
        'L': [('Local/Automatic variables', 186), ('LOOPS', 123)],
        'M': [('Mac OS', 7), ('main ( )', 62), ('Memory addresses', 216), ('Multiprocessor operating system', 13)]}
IDX2 = {'M': [('Multiprogramming', 24), ('Multiprogramming operating system', 8), ('Multitasking', 24), ('Multi-tasking operating system', 10), ('Multithreading', 24), ('Multi-user operating systems', 16)],
        'N': [('Nested if', 119), ('Nested loops', 135)],
        'O': [('Object in C++', 230), ('One dimensional array', 148), ('Operating System', 2), ('Operators', 90)],
        'P': [('Parallel processing operating system', 14), ('parameters', 190), ('Pointer', 216), ('Polymorphism', 253), ('Preprocessor directives', 61), ('private access specifier', 234), ('Process', 22), ('Process States', 22),
              ('program', 58), ('Programmer', 50), ('Project Manager', 48), ('Pseudo code', 44), ('public access specifier', 236)],
        'R': [('Real-Time operating system', 12), ('Reference operator', 217), ('Reserved words', 59), ('return statement', 203)],
        'S': [('SDLC', 32), ('SDLC Phases', 35), ('Single-user operating systems', 16), ('Software Tester', 50), ('Static variables', 188), ('Stream', 269), ('Strings', 162), ('Switch-default statement', 116), ('System', 32), ('System Analyst', 49)],
        'T': [('Text files', 260), ('thread', 23), ('Time-Sharing operating system', 10), ('Traversing an array', 154), ('Two-dimensional array', 157), ('Type casting', 77)],
        'U': [('UNIX', 6), ('User-defined functions', 181)], 'V': [('Variables', 68)], 'W': [('while loop', 127), ('Windows', 5)]}


def index(idx, n, pdf, pages, head):
    b = Builder()
    if head:
        b.h('Index', 'اشاریہ', 'نښلیک')
    for letter, rows in idx.items():
        b.h(letter, letter, letter)
        same(b, 'lines', [f'{t} — {p}' for t, p in rows])
    r = BOOK.record(b, f'cs12-bm-index-{n}', f'Index ({n})', f'اشاریہ ({n})', f'نښلیک ({n})', pdf, pages)
    r['sourceNote'] = 'Index entries (term — printed page) are kept as printed in every language view; the dotted leaders are not reproduced.'
    return r


def p156():
    g, iss = glossary(156)
    iss.append({'id': 'cs12-pdf156-index', 'unit': BM, 'printedPage': 301, 'description': 'Index page numbers are retained as printed even where they differ from the pages on which the topics now fall (e.g. Constructor 239, Inheritance 249).'})
    BOOK.save(156, [(BM, g), (BM, index(IDX1, 1, 156, [301], True))], issues=iss)


FIG1 = [('Figure 1.1: Operating System as an Interface', '3'), ('Figure 1.2 MS DOS Operating System', '4'), ('Figure 1.3: Windows 7 Desktop', '6'), ('Figure 1.4 UNIX Prompt', '7'),
        ('Figure 1.5: Mac OS Desktop', '7'), ('Figure 1.6 Main Memory Partitioning in Multiprogramming', '9'), ('Figure 1.7: File Structure in Computer', '18'), ('Figure 1.8: Hierarchical File System', '19'),
        ('Figure 1.9 Device Drivers and Operating System', '20'), ('Figure 1.10: Five-State Process Model', '23'), ('Figure 2.1: Phases of System Development Life Cycle', '36'), ('Figure 2.2 Flowchart Symbols', '43'),
        ('Figure 2.3 Flowchart', '43'), ('Figure 5.1: Memory Representation of 1-D Array for an int Data Type', '147'), ('Figure 5.2: Memory Representation of 1-D Array for a char Data Type', '147'),
        ('Figure 7.1: Use of the Pointer Variable', '219'), ('Figure 8.1: Inheritance of Fruit Class', '254'), ('Figure 8.2: Inheritance of Shape Class', '254')]
FIG2 = [('Figure 8.3: Inheritance of Patient Class', '255'), ('Figure 8.4: Multiple Inheritance', '257'), ('Figure 9.1: Opening and Writing into a Text File', '267'), ('Figure 9.2: Input File to be Read', '268'),
        ('Figure 9.3: Output of Reading Program', '269'), ('Figure 9.4: Input File to be Read', '269'), ('Figure 9.5: Output of the Program that is Read from Input File “myFile.txt”', '271'),
        ('Figure 9.6: Input File to be Read Character by Character', '277'), ('Figure 9.7: File Written by Character Stream', '278'), ('Figure 9.8: Input File that will be Read using String Stream', '278'),
        ('Figure 9.9: File Read by String Stream', '279')]
FH = (['Figure', 'Page No'], ['شکل', 'صفحہ نمبر'], ['شکل', 'مخ شمېره'])


def p157():
    i2 = index(IDX2, 2, 157, [302], False)
    b = Builder()
    b.h('Annexure 1', 'ضمیمہ 1', '۱ ضمیمه')
    b.h('List of Figures', 'اشکال کی فہرست', 'د شکلونو لړلیک')
    neutral_table(b, 'cs12-annex1-a', FH[0], [list(x) for x in FIG1], FH[1], FH[2])
    r = BOOK.record(b, 'cs12-bm-annex-1a', 'Annexure 1: List of Figures (1)', 'ضمیمہ 1: اشکال کی فہرست (۱)', '۱ ضمیمه: د شکلونو لړلیک (۱)', 157, [303])
    r['sourceNote'] = 'Figure captions are kept as printed (English) in every language view; the right page of PDF157 is Annexure 1.'
    BOOK.save(157, [(BM, i2), (BM, r)], issues=[{'id': 'cs12-pdf157', 'unit': BM, 'printedPage': 303,
               'description': 'Annexure 1 numbers the inheritance figures 8.1–8.4 and the Unit 9 figures 9.1–9.9, whereas the unit text captions them 8.2, 8.2, 8.3, 8.4 and 9.1–9.5, 9.7, 9.8, 9.9, 9.12, and gives page numbers that differ from the text. Retained as printed. The partly cut first entry of the right index column on p.302 is read as “Reference operator — 217”.'}])


TABLES = [('Table 3.1: List of C++ Keywords', '59'), ('Table 3.2: C++ Data Types', '76'), ('Table 3.3: Escape Sequences', '85'), ('Table 3.4: Arithmetic Operators', '92'),
          ('Table 3.5: Arithmetic Assignment Operators', '94'), ('Table 3.8: List of Relational Operators', '97'), ('Table 3.9: List of Logical Operators', '97'), ('Table 3.10: Logical NOT Operator', '98'),
          ('Table 3.11: Logical AND Operator', '98'), ('Table 3.12: Logical OR Operator', '99'), ('Table 3.13 Operators Precedence', '103'), ('Table 8.1: Access Specifiers and Data Hiding', '243')]


def p158():
    b = Builder()
    neutral_table(b, 'cs12-annex1-b', FH[0], [list(x) for x in FIG2], FH[1], FH[2])
    r1 = BOOK.record(b, 'cs12-bm-annex-1b', 'Annexure 1: List of Figures (2)', 'ضمیمہ 1: اشکال کی فہرست (۲)', '۱ ضمیمه: د شکلونو لړلیک (۲)', 158, [304])
    t = Builder()
    t.h('Annexure 2', 'ضمیمہ 2', '۲ ضمیمه')
    t.h('List of Tables', 'جداول کی فہرست', 'د جدولونو لړلیک')
    neutral_table(t, 'cs12-annex2', ['Table', 'Page No'], [list(x) for x in TABLES], ['جدول', 'صفحہ نمبر'], ['جدول', 'مخ شمېره'])
    r2 = BOOK.record(t, 'cs12-bm-annex-2', 'Annexure 2: List of Tables', 'ضمیمہ 2: جداول کی فہرست', '۲ ضمیمه: د جدولونو لړلیک', 158, [305])
    r2['sourceNote'] = 'Table captions are kept as printed (English) in every language view.'
    BOOK.save(158, [(BM, r1), (BM, r2)], issues=[{'id': 'cs12-pdf158', 'unit': BM, 'printedPage': 305, 'description': 'Annexure 2 skips Tables 3.6–3.7. Retained as printed.'}])


def p159():
    b = Builder()
    b.h('Annexure 3', 'ضمیمہ 3', '۳ ضمیمه')
    b.h('List of Symbols', 'علامات کی فہرست', 'د نښو لړلیک')
    rows = [('Oval', 'terminal', 'Start/ End of Program'), ('Flow Line', 'line', 'Direction of Flow'), ('Parallelogram', 'io', 'Input or Output'), ('Rectangle', 'process', 'Processing'), ('Diamond', 'decision', 'Decision Making')]
    ur = [('بیضوی', 'terminal', 'پروگرام کا آغاز/ اختتام'), ('بہاؤ کی لکیر', 'line', 'بہاؤ کی سمت'), ('متوازی الاضلاع', 'io', 'ان پٹ یا آؤٹ پٹ'), ('مستطیل', 'process', 'پروسیسنگ'), ('معین', 'decision', 'فیصلہ سازی')]
    ps = [('هګۍ ډوله', 'terminal', 'د پروګرام پیل/ پای'), ('د بهیر کرښه', 'line', 'د بهیر لوری'), ('متوازي الاضلاع', 'io', 'ننوتنه یا وتنه'), ('مستطیل', 'process', 'پروسس'), ('معین', 'decision', 'پرېکړه کول')]
    en, h = symbols_table(rows, ('Name', 'Symbol', 'Use'), 'Annexure 3: List of Symbols')
    u, _ = symbols_table(ur, ('نام', 'علامت', 'استعمال'), 'ضمیمہ 3: علامات کی فہرست')
    p, _ = symbols_table(ps, ('نوم', 'نښه', 'کارونه'), '۳ ضمیمه: د نښو لړلیک')
    b.visual('cs12-annex3-symbols', en, u, p, 560 / h)
    r1 = BOOK.record(b, 'cs12-bm-annex-3', 'Annexure 3: List of Symbols', 'ضمیمہ 3: علامات کی فہرست', '۳ ضمیمه: د نښو لړلیک', 159, [306])
    r1['sourceNote'] = 'The symbols table is redrawn as a coded diagram (shape, name and use), with the flat colours of the flowchart figures.'
    c = Builder()
    c.h('Annexure 4', 'ضمیمہ 4', '۴ ضمیمه')
    c.h('List of Commands', 'کمانڈز کی فہرست', 'د امرونو لړلیک')
    C = [('CD', 'changes the current directory', 'موجودہ ڈائریکٹری تبدیل کرتا ہے', 'اوسنی لارښود بدلوي'), ('COPY', 'copies a file', 'فائل نقل کرتا ہے', 'دوتنه کاپي کوي'),
         ('DEL', 'deletes a file', 'فائل حذف کرتا ہے', 'دوتنه ړنګوي'), ('DIR', 'lists directory contents', 'ڈائریکٹری کا مواد دکھاتا ہے', 'د لارښود منځپانګه لړلیکوي'),
         ('EDIT', 'starts an editor to create or edit plain text files', 'سادہ ٹیکسٹ فائلز بنانے یا ان میں ترمیم کے لیے ایڈیٹر شروع کرتا ہے', 'د ساده متني دوتنو د جوړولو یا سمولو لپاره سمونګر پیلوي'),
         ('FORMAT', 'formats a disk to accept DOS files', 'ڈسک کو DOS فائلز قبول کرنے کے لیے فارمیٹ کرتا ہے', 'ډیسک د DOS دوتنو منلو ته بڼه ورکوي'), ('HELP', 'displays information about a command', 'کسی کمانڈ کے بارے میں معلومات دکھاتا ہے', 'د یوه امر په اړه معلومات ښيي'),
         ('MKDIR', 'creates a new directory', 'نئی ڈائریکٹری بناتا ہے', 'نوی لارښود جوړوي'), ('RD', 'removes a directory', 'ڈائریکٹری ہٹاتا ہے', 'لارښود لرې کوي'), ('REN', 'renames a file', 'فائل کا نام تبدیل کرتا ہے', 'د دوتنې نوم بدلوي'),
         ('TYPE', 'displays contents of a file on the screen', 'اسکرین پر فائل کا مواد دکھاتا ہے', 'پر پرده د دوتنې منځپانګه ښيي')]
    c.table('cs12-annex4', ['Command', 'Action'], [[a, e] for a, e, _, _ in C], ['کمانڈ', 'عمل'], ['امر', 'کړنه'], [[a, u] for a, _, u, _ in C], [[a, q] for a, _, _, q in C])
    r2 = BOOK.record(c, 'cs12-bm-annex-4', 'Annexure 4: List of Commands', 'ضمیمہ 4: کمانڈز کی فہرست', '۴ ضمیمه: د امرونو لړلیک', 159, [307])
    BOOK.save(159, [(BM, r1), (BM, r2)])


FN = [('getch()', 'conio.h', 'Used to get the character input from the keyboard', 'کی بورڈ سے حرفی ان پٹ لینے کے لیے', 'له کیبورډ د توري ننوتنې اخیستلو لپاره'),
      ('getche()', 'conio.h', 'Used to get character input form the keyboard and echo it on the screen', 'کی بورڈ سے حرفی ان پٹ لے کر اسے اسکرین پر دکھانے کے لیے', 'له کیبورډ د توري ننوتنې اخیستلو او پر پرده یې ښودلو لپاره'),
      ('gets()', 'stdio.h', 'Stands for get string and is used to get a string input', 'get string کا مخفف ہے اور اسٹرنگ ان پٹ لینے کے لیے استعمال ہوتا ہے', 'د get string لنډون دی او د تار ننوتنې اخیستلو لپاره کارېږي'),
      ('puts()', 'stdio.h', 'Used to display the string', 'اسٹرنگ دکھانے کے لیے', 'د تار ښودلو لپاره'),
      ('getchar()', 'stdio.h', 'Stands for get character it is used to input as single character from the keyboard. This function receives no argument.', 'get character کا مخفف ہے، کی بورڈ سے ایک حرف داخل کرنے کے لیے استعمال ہوتا ہے۔ یہ فنکشن کوئی آرگیومنٹ نہیں لیتا۔', 'د get character لنډون دی، له کیبورډ د یوه توري ننوتلو لپاره کارېږي. دا فنکشن هېڅ دلیل نه اخلي.'),
      ('putchar()', 'stdio.h', 'Standard output function used to display the character, on the output screen, received as an argument.', 'معیاری آؤٹ پٹ فنکشن جو بطور آرگیومنٹ ملنے والا حرف آؤٹ پٹ اسکرین پر دکھاتا ہے۔', 'معیاري د وتنې فنکشن چې د دلیل په توګه ترلاسه شوی توری د وتنې پر پرده ښيي.'),
      ('strcat()', 'string.h', 'Stands for String concatenation. It combines two strings into a single string.', 'String concatenation کا مخفف۔ یہ دو اسٹرنگز کو ایک اسٹرنگ میں جوڑتا ہے۔', 'د String concatenation لنډون. دوه تارونه په یوه تار کې یوځای کوي.'),
      ('copy()', 'string.h', 'This function copy one string into another string.', 'یہ فنکشن ایک اسٹرنگ کو دوسری اسٹرنگ میں نقل کرتا ہے۔', 'دا فنکشن یو تار بل تار ته کاپي کوي.'),
      ('strcpy()', 'string.h', 'It is also used to copy one string into another string', 'یہ بھی ایک اسٹرنگ کو دوسری اسٹرنگ میں نقل کرنے کے لیے استعمال ہوتا ہے', 'دا هم د یوه تار بل تار ته د کاپي کولو لپاره کارېږي'),
      ('find()', 'string.h', 'To find a particular word or a character in a string', 'اسٹرنگ میں کوئی خاص لفظ یا حرف تلاش کرنے کے لیے', 'په تار کې د یوې ځانګړې کلمې یا توري موندلو لپاره'),
      ('length()', 'string.h', 'Used to find the length of a string.', 'اسٹرنگ کی لمبائی معلوم کرنے کے لیے۔', 'د تار د اوږدوالي موندلو لپاره.'),
      ('swap()', 'string.h', 'To swap the values of two strings.', 'دو اسٹرنگز کی قدروں کا تبادلہ کرنے کے لیے۔', 'د دوو تارونو د ارزښتونو د تبادلې لپاره.'),
      ('sin()', 'math.h', 'Used to find the sin value of an angle.', 'زاویے کی sin قدر معلوم کرنے کے لیے۔', 'د زاویې د sin ارزښت موندلو لپاره.'),
      ('cos()', 'math.h', 'Used to find the cos value of an angle.', 'زاویے کی cos قدر معلوم کرنے کے لیے۔', 'د زاویې د cos ارزښت موندلو لپاره.'),
      ('tan()', 'math.h', 'Used to ding the tangent value of an anbgle.', 'زاویے کی tangent قدر معلوم کرنے کے لیے۔', 'د زاویې د tangent ارزښت موندلو لپاره.'),
      ('cot()', 'math.h', 'Used to find the cotangent value of an angle.', 'زاویے کی cotangent قدر معلوم کرنے کے لیے۔', 'د زاویې د cotangent ارزښت موندلو لپاره.'),
      ('abs()', 'math.h', 'Used to find the absolute value of a variable or expression.', 'کسی ویری ایبل یا ایکسپریشن کی مطلق قدر معلوم کرنے کے لیے۔', 'د یوه متغیر یا افادې د مطلق ارزښت موندلو لپاره.'),
      ('pow()', 'math.h', 'Used to find the power of a number. It takes two arguments first shows the number and second shows the power to which the number is raised.', 'کسی عدد کی طاقت معلوم کرنے کے لیے۔ یہ دو آرگیومنٹس لیتا ہے، پہلا عدد اور دوسرا وہ طاقت ظاہر کرتا ہے جس تک عدد کو بڑھایا جائے۔', 'د یوه عدد د توان موندلو لپاره. دوه دلیلونه اخلي، لومړی عدد او دویم هغه توان ښيي چې عدد ورته پورته کېږي.'),
      ('sqrt()', 'math.h', 'Used to find the square root of an number received as an argument.', 'بطور آرگیومنٹ ملنے والے عدد کا جذر معلوم کرنے کے لیے۔', 'د دلیل په توګه ترلاسه شوي عدد د جذر موندلو لپاره.'),
      ('open()', 'fstream.h', 'Used to open a file.', 'فائل کھولنے کے لیے۔', 'د دوتنې د پرانیستلو لپاره.'),
      ('close()', 'fstream.h', 'Used to close a file.', 'فائل بند کرنے کے لیے۔', 'د دوتنې د تړلو لپاره.'),
      ('bof()', 'fstream.h', 'used to set the pointers to the beginning of a file', 'پوائنٹرز کو فائل کے آغاز پر سیٹ کرنے کے لیے', 'پوائنټرونه د دوتنې پیل ته ټاکلو لپاره'),
      ('eof()', 'fstream.h', 'used to set the pointers at the end of a file', 'پوائنٹرز کو فائل کے اختتام پر سیٹ کرنے کے لیے', 'پوائنټرونه د دوتنې پای ته ټاکلو لپاره')]


def p160():
    b = Builder()
    b.h('Annexure 5', 'ضمیمہ 5', '۵ ضمیمه')
    b.h('List of Built-in Functions', 'بلٹ اِن فنکشنز کی فہرست', 'د جوړ شویو فنکشنونو لړلیک')
    b.table('cs12-annex5', ['Function', 'Header File', 'Purpose'], [[f, h, e] for f, h, e, _, _ in FN], ['فنکشن', 'ہیڈر فائل', 'مقصد'], ['فنکشن', 'سرپاڼه دوتنه', 'موخه'],
            [[f, h, u] for f, h, _, u, _ in FN], [[f, h, p] for f, h, _, _, p in FN])
    r = BOOK.record(b, 'cs12-bm-annex-5', 'Annexure 5: List of Built-in Functions', 'ضمیمہ 5: بلٹ اِن فنکشنز کی فہرست', '۵ ضمیمه: د جوړ شویو فنکشنونو لړلیک', 160, [308, 309])
    r['sourceNote'] = 'The table spans pp.308–309 and is given as one structured table; function and header names are kept in English.'
    BOOK.save(160, [(BM, r)], issues=[{'id': 'cs12-pdf160', 'unit': BM, 'printedPage': 309,
               'description': 'Annexure 5: running head “List of Build-in Functions”; “input form the keyboard”, “This function copy”, “Used to ding the tangent value of an anbgle”, “an number”. Retained as printed (the English column).'}])


def _ascii():
    C0 = ['NULL', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL', 'BS', 'HT', 'LF', 'VT', 'FF', 'CR', 'SO', 'SI', 'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB', 'CAN', 'EM', 'SUB', 'ESC', 'FS', 'GS', 'RS', 'US']
    D0 = ['Null character', 'Start of Header', 'Start of Text', 'End of Text', 'End of Transmission', 'Enquiry', 'Acknowledgement', 'Bell', 'Backspace', 'Horizontal Tab', 'Line feed', 'Vertical Tab',
          'Form feed', 'Carriage return', 'Shift Out', 'Shift In', 'Data link escape', 'Device control 1', 'Device control 2', 'Device control 3', 'Device control 4', 'Negative acknowledgement',
          'Synchronous idle', 'End of transmission block', 'Cancel', 'End of medium', 'Substitute', 'Escape', 'File separator', 'Group separator', 'Record separator', 'Unit separator']
    rows = [[str(i), C0[i], f'({D0[i]})'] for i in range(32)]
    P = {32: ('', 'space'), 33: ('!', 'exclamation mark'), 34: ('"', 'Quotation mark'), 35: ('#', 'Number sign'), 36: ('$', 'Dollar sign'), 37: ('%', 'Percent sign'), 38: ('&', 'Ampersand'),
         39: ("'", 'Apostrophe'), 40: ('(', 'round brackets or parentheses'), 41: (')', 'round brackets or parentheses'), 42: ('*', 'Asterisk'), 43: ('+', 'Plus sign'), 44: (',', 'Comma'),
         45: ('-', 'Hyphen'), 46: ('.', 'Full stop , dot'), 47: ('/', 'Slash'), 58: (':', 'Colon'), 59: (';', 'Semicolon'), 60: ('<', 'Less-than sign '), 61: ('=', 'Equals sign'),
         62: ('>', 'Greater-than sign ; Inequality'), 63: ('?', 'Question mark'), 64: ('@', 'At sign'), 91: ('[', 'square brackets or box brackets'), 92: ('\\', 'Backslash'),
         93: (']', 'square brackets or box brackets'), 94: ('^', 'Caret or circumflex accent'), 95: ('_', 'underscore, under strike, underbar or low line'), 96: ('`', 'Grave accent'),
         123: ('{', 'curly brackets or braces'), 124: ('|', 'vertical-bar, vbar, vertical line or vertical slash'), 125: ('}', 'curly brackets or braces'), 126: ('~', 'Tilde ; swung dash'), 127: ('DEL', 'Delete')}
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        P[48 + i] = (str(i), f'number {num[i]}')
    for i in range(26):
        P[65 + i] = (chr(65 + i), f'Capital {chr(65 + i)} ')
        P[97 + i] = (chr(97 + i), f'Lowercase  {chr(97 + i)} ')
    E = {128: ('Ç', 'Majuscule C-cedilla '), 129: ('ü', 'letter "u" with umlaut or diaeresis ; "u-umlaut"'), 130: ('é', 'letter "e" with acute accent or "e-acute"'),
         131: ('â', 'letter "a" with circumflex accent or "a-circumflex"'), 132: ('ä', 'letter "a" with umlaut or diaeresis ; "a-umlaut"'), 133: ('à', 'letter "a" with grave accent'),
         134: ('å', 'letter "a"  with a ring'), 135: ('ç', 'Minuscule c-cedilla'), 136: ('ê', 'letter "e" with circumflex accent or "e-circumflex"'), 137: ('ë', 'letter "e" with umlaut or diaeresis ; "e-umlaut"'),
         138: ('è', 'letter "e" with grave accent'), 139: ('ï', 'letter "i" with umlaut or diaeresis ; "i-umlaut"'), 140: ('î', 'letter "i" with circumflex accent or "i-circumflex"'),
         141: ('ì', 'letter "i" with grave accent'), 142: ('Ä', 'letter "A" with umlaut or diaeresis ; "A-umlaut"'), 143: ('Å', 'letter "A"  with a ring'), 144: ('É', 'Capital letter "E" with acute accent or "E-acute"'),
         145: ('æ', 'Latin diphthong "ae"'), 146: ('Æ', 'Latin diphthong "AE"'), 147: ('ô', 'letter "o" with circumflex accent or "o-circumflex"'), 148: ('ö', 'letter "o" with umlaut or diaeresis ; "o-umlaut"'),
         149: ('ò', 'letter "o" with grave accent'), 150: ('û', 'letter "u" with circumflex accent or "u-circumflex"'), 151: ('ù', 'letter "u" with grave accent'), 152: ('ÿ', 'letter "y" with diaeresis'),
         153: ('Ö', 'letter "O" with umlaut or diaeresis ; "O-umlaut"'), 154: ('Ü', 'letter "U" with umlaut or diaeresis ; "U-umlaut"'), 155: ('ø', 'slashed zero or empty set'),
         156: ('£', 'Pound sign ; symbol for the pound sterling'), 157: ('Ø', 'slashed zero or empty set'), 158: ('×', 'multiplication sign'), 159: ('ƒ', 'function sign ; f with hook sign ; florin sign '),
         160: ('á', 'letter "a" with acute accent or "a-acute"'), 161: ('í', 'letter "i" with acute accent or "i-acute"'), 162: ('ó', 'letter "o" with acute accent or "o-acute"'),
         163: ('ú', 'letter "u" with acute accent or "u-acute"'), 164: ('ñ', 'letter "n" with tilde ; enye'), 165: ('Ñ', 'letter "N" with tilde ; enye'), 166: ('ª', 'feminine ordinal indicator '),
         167: ('º', 'masculine ordinal indicator'), 168: ('¿', 'Inverted question marks'), 169: ('®', 'Registered trademark symbol'), 170: ('¬', 'Logical negation symbol'), 171: ('½', 'One half'),
         172: ('¼', 'Quarter or  one fourth'), 173: ('¡', 'Inverted exclamation marks'), 174: ('«', 'Guillemets or  angle quotes'), 175: ('»', 'Guillemets or  angle quotes'), 176: ('░', None), 177: ('▒', None),
         178: ('▓', None), 179: ('│', 'Box drawing character'), 180: ('┤', 'Box drawing character'), 181: ('Á', 'Capital letter "A" with acute accent or "A-acute"'),
         182: ('Â', 'letter "A" with circumflex accent or "A-circumflex"'), 183: ('À', 'letter "A" with grave accent'), 184: ('©', 'Copyright symbol'), 189: ('¢', 'Cent symbol'), 190: ('¥', 'YEN and YUAN sign'),
         198: ('ã', 'letter "a" with tilde or "a-tilde"'), 199: ('Ã', 'letter "A" with tilde or "A-tilde"'), 206: ('╬', None), 207: ('¤', 'generic currency sign '), 208: ('ð', 'lowercase "eth"'),
         209: ('Ð', 'Capital letter "Eth"'), 210: ('Ê', 'letter "E" with circumflex accent or "E-circumflex"'), 211: ('Ë', 'letter "E" with umlaut or diaeresis ; "E-umlaut"'), 212: ('È', 'letter "E" with grave accent'),
         213: ('ı', 'lowercase dot less i'), 214: ('Í', 'Capital letter "I" with acute accent or "I-acute"'), 215: ('Î', 'letter "I" with circumflex accent or "I-circumflex"'),
         216: ('Ï', 'letter "I" with umlaut or diaeresis ; "I-umlaut"'), 217: ('┘', 'Box drawing character'), 218: ('┌', 'Box drawing character'), 219: ('█', 'Block'), 220: ('▄', None),
         221: ('¦', 'vertical broken bar '), 222: ('Ì', 'letter "I" with grave accent'), 223: ('▀', None), 224: ('Ó', 'Capital letter "O" with acute accent or "O-acute"'),
         225: ('ß', 'letter "Eszett" ; "scharfes S" or "sharp S"'), 226: ('Ô', 'letter "O" with circumflex accent or "O-circumflex"'), 227: ('Ò', 'letter "O" with grave accent'),
         228: ('õ', 'letter "o" with tilde or "o-tilde"'), 229: ('Õ', 'letter "O" with tilde or "O-tilde"'), 230: ('µ', 'Lowercase letter "Mu" ; micro sign or micron'), 231: ('þ', 'capital letter "Thorn"'),
         232: ('Þ', 'lowercase letter "thorn"'), 233: ('Ú', 'Capital letter "U" with acute accent or "U-acute"'), 234: ('Û', 'letter "U" with circumflex accent or "U-circumflex"'),
         235: ('Ù', 'letter "U" with grave accent'), 236: ('ý', 'letter "y" with acute accent'), 237: ('Ý', 'Capital letter "Y" with acute accent'), 238: ('¯', 'macron symbol'), 239: ('´', 'Acute accent'),
         240: ('­', 'Hyphen'), 241: ('±', 'Plus-minus sign'), 242: ('‗', 'underline or underscore'), 243: ('¾', 'three quarters'), 244: ('¶', 'paragraph sign or pilcrow'), 245: ('§', 'Section sign'),
         246: ('÷', 'The division sign ; Obelus'), 247: ('¸', 'cedilla'), 248: ('°', 'degree symbol '), 249: ('¨', 'Diaeresis'), 250: ('·', 'Interpunct or space dot'), 251: ('¹', 'superscript one'),
         252: ('³', 'cube or superscript three'), 253: ('²', 'Square or superscript two'), 254: ('■', 'black square'), 255: ('nbsp', 'non-breaking space or no-break space')}
    for k, s in zip(range(185, 189), '╣║╗╝'):
        E[k] = (s, 'Box drawing character')
    for k, s in zip(range(191, 198), '┐└┴┬├─┼'):
        E[k] = (s, 'Box drawing character')
    for k, s in zip(range(200, 206), '╚╔╩╦╠═'):
        E[k] = (s, 'Box drawing character')
    P.update(E)
    for i in range(32, 256):
        s, d = P[i]
        rows.append(['' if i == 163 else str(i), s, f'({d})' if d else ''])
    return rows


ASCII = _ascii()
AH = (['ASCII code', 'symbol', 'Description'], ['ASCII کوڈ', 'علامت', 'وضاحت'], ['ASCII کوډ', 'نښه', 'تشریح'])
ASPLIT = {161: (0, 92, [310, 311], True), 162: (92, 199, [312, 313], False), 163: (199, 256, [314], False)}


def ascii_rec(pdf):
    a, z, pages, head = ASPLIT[pdf]
    b = Builder()
    if head:
        b.h('Annexure 6', 'ضمیمہ 6', '۶ ضمیمه')
        b.h('Complete list of ASCII Codes', 'ASCII کوڈز کی مکمل فہرست', 'د ASCII کوډونو بشپړ لړلیک')
    neutral_table(b, f'cs12-annex6-{pdf}', AH[0], ASCII[a:z], AH[1], AH[2])
    k = pdf - 160
    r = BOOK.record(b, f'cs12-bm-annex-6-{k}', f'Annexure 6: ASCII Codes ({k})', f'ضمیمہ 6: ASCII کوڈز ({k})', f'۶ ضمیمه: ASCII کوډونه ({k})', pdf, pages)
    r['sourceNote'] = 'The ASCII table is reproduced as a structured table with codes, symbols and descriptions as printed (kept in English in every language view; blank description cells as printed). Symbols for codes 128–255 follow the extended (code page 850) set the book prints.'
    return r


def p161():
    BOOK.save(161, [(BM, ascii_rec(161))])


def p162():
    BOOK.save(162, [(BM, ascii_rec(162))], issues=[{'id': 'cs12-pdf162', 'unit': BM, 'printedPage': 313,
               'description': 'On p.313 the code number 163 is not printed (its row shows only ú and “letter u with acute accent”); codes 176–178 have no description. Retained as printed.'}])


def p163():
    a = Builder()
    a.h('About Authors', 'مصنفین کا تعارف', 'د لیکوالانو په اړه')
    a.p('1. RAHMAN ALI earned M.Phil (MS) degree in Computer Science from the Department of Computer Science, University of Peshawar in 2009. He earned his Master (M.Sc) degree in Computer Science from Hazara University, Mansehra in 2005. He did his B.Sc and F.Sc from Govt. Post Graduate Iehanzeb College, Saidu Sharif, Swat in 2002 and 1999 respectively. He did SSC from Govt. High School Kishawara, Swat in 1997. He also holds bachelor degree in Education (B.Ed), earned from University of Peshawar in 2006.',
        '1۔ رحمان علی نے 2009 میں شعبہ کمپیوٹر سائنس، جامعہ پشاور سے کمپیوٹر سائنس میں ایم فل (MS) کی ڈگری حاصل کی۔ انھوں نے 2005 میں ہزارہ یونیورسٹی مانسہرہ سے کمپیوٹر سائنس میں ماسٹر (M.Sc) کی ڈگری حاصل کی۔ انھوں نے بالترتیب 2002 اور 1999 میں گورنمنٹ پوسٹ گریجویٹ جہانزیب کالج سیدو شریف سوات سے B.Sc اور F.Sc کیا۔ انھوں نے 1997 میں گورنمنٹ ہائی اسکول کشاورہ سوات سے SSC کیا۔ ان کے پاس 2006 میں جامعہ پشاور سے حاصل کردہ بیچلر ان ایجوکیشن (B.Ed) کی ڈگری بھی ہے۔',
        '۱. رحمان علي په ۲۰۰۹ کال کې د پېښور پوهنتون د کمپیوټر ساینس له څانګې څخه په کمپیوټر ساینس کې د ایم فل (MS) سند واخیست. په ۲۰۰۵ کال کې یې د هزارې پوهنتون مانسهره څخه په کمپیوټر ساینس کې د ماسټرۍ (M.Sc) سند واخیست. په ترتیب سره په ۲۰۰۲ او ۱۹۹۹ کلونو کې یې د حکومتي پوسټ ګرېجویټ جهانزېب کالج سیدو شریف سوات څخه B.Sc او F.Sc وکړل. په ۱۹۹۷ کال کې یې د حکومتي عالي ښوونځي کشاوره سوات څخه SSC وکړ. همداراز په ۲۰۰۶ کال کې د پېښور پوهنتون څخه د ښوونې او روزنې د لیسانس (B.Ed) سند لري.')
    a.p('He served Govt. Degree College, Kabal, Swat as a lecturer in Computer Science selected from September 2007 to August 2009. He also served Institute of IT, University of Science & Technology, Bannu as a lecturer in Computer Science from August 2009 to December 2009.',
        'انھوں نے ستمبر 2007 سے اگست 2009 تک گورنمنٹ ڈگری کالج کبل سوات میں کمپیوٹر سائنس کے لیکچرر کے طور پر خدمات انجام دیں۔ انھوں نے اگست 2009 سے دسمبر 2009 تک انسٹی ٹیوٹ آف آئی ٹی، یونیورسٹی آف سائنس اینڈ ٹیکنالوجی بنوں میں بھی کمپیوٹر سائنس کے لیکچرر کے طور پر خدمات انجام دیں۔',
        'هغه د ۲۰۰۷ کال له سپټمبر تر ۲۰۰۹ کال اګست پورې په حکومتي ډګري کالج کبل سوات کې د کمپیوټر ساینس د لکچرر په توګه دنده ترسره کړه. همداراز یې د ۲۰۰۹ کال له اګست تر ډسمبر پورې د بنو د ساینس او ټکنالوژۍ پوهنتون د IT انسټیټیوټ کې د کمپیوټر ساینس د لکچرر په توګه دنده ترسره کړه.')
    a.p('Rahman Ali is serving is a Lecturer in Computer Science at Quaid-e-Azam College of Commerce, University of Peshawar since December 2009.',
        'رحمان علی دسمبر 2009 سے قائدِ اعظم کالج آف کامرس، جامعہ پشاور میں کمپیوٹر سائنس کے لیکچرر کے طور پر خدمات انجام دے رہے ہیں۔',
        'رحمان علي له ۲۰۰۹ کال ډسمبر راهیسې د پېښور پوهنتون په قائد اعظم کالج آف کامرس کې د کمپیوټر ساینس د لکچرر په توګه دنده ترسره کوي.')
    a.p('Ali has his MS major in Artificial Intelligence (AI) and worked in Natural Language Processing (NLP). He has worked in anaphora, ambiguity and ellipsis resolution, Part-of- Speech (POS) tagging, natural language interfaces to databases, corpus linguistics, and machine translation and transliteration. He has published his research work in well reputed journals and conferences.',
        'علی کا MS میں اختصاص مصنوعی ذہانت (AI) ہے اور انھوں نے نیچرل لینگویج پروسیسنگ (NLP) میں کام کیا ہے۔ انھوں نے anaphora، ابہام اور ellipsis کے حل، Part-of-Speech (POS) ٹیگنگ، ڈیٹا بیسز کے لیے فطری زبان کے انٹرفیسز، corpus linguistics اور مشینی ترجمہ و transliteration میں کام کیا ہے۔ انھوں نے اپنا تحقیقی کام معتبر جرائد اور کانفرنسوں میں شائع کیا ہے۔',
        'علي په MS کې په مصنوعي ځیرکتیا (AI) کې تخصص لري او په طبیعي ژبې پروسس (NLP) کې یې کار کړی. هغه د anaphora، ابهام او ellipsis په حل، د Part-of-Speech (POS) نښه کولو، ډېټابېسونو ته د طبیعي ژبې منځګړو، corpus linguistics او ماشیني ژباړې او transliteration کې کار کړی. خپل څېړنیز کار یې په معتبرو مجلو او کنفرانسونو کې خپور کړی.')
    ra = BOOK.record(a, 'cs12-bm-authors-1', 'About Authors (1)', 'مصنفین کا تعارف (۱)', 'د لیکوالانو په اړه (۱)', 163, [315])
    BOOK.save(163, [(BM, ascii_rec(163)), (BM, ra)], issues=[{'id': 'cs12-pdf163', 'unit': BM, 'printedPage': 315,
               'description': 'About Authors: “Govt. Post Graduate Iehanzeb College” (Jehanzeb), “selected from September 2007”, “is serving is a Lecturer”. Retained as printed. Owner handwriting (signatures and a column of numbers beside the ASCII table) on pp.314–315 excluded.'}])


def p164():
    a = Builder()
    a.p('Mohammad Khalid is Head of Computer Science Department at OPF Boys College, Islamabad. Throughout his educational career he has got first-class first division. He did his M.Sc in Computer Science from the University of Peshawar in 1996 and earned his B.Ed degree in Science from Institute of Education and Research, University of Peshawar in 1997. He has been instructor and teacher in Computer Science for the last seventeen years. He has vast teaching experience from Secondary to Masters Level. He has attended many national and International level seminars and meetings for the promotion of teaching Computer Science at different levels.',
        'محمد خالد او پی ایف بوائز کالج اسلام آباد میں شعبہ کمپیوٹر سائنس کے سربراہ ہیں۔ اپنے پورے تعلیمی سفر میں انھوں نے فرسٹ کلاس فرسٹ ڈویژن حاصل کی۔ انھوں نے 1996 میں جامعہ پشاور سے کمپیوٹر سائنس میں M.Sc کیا اور 1997 میں انسٹی ٹیوٹ آف ایجوکیشن اینڈ ریسرچ، جامعہ پشاور سے سائنس میں B.Ed کی ڈگری حاصل کی۔ وہ گزشتہ سترہ برس سے کمپیوٹر سائنس کے انسٹرکٹر اور استاد ہیں۔ انھیں ثانوی سے ماسٹرز سطح تک تدریس کا وسیع تجربہ ہے۔ انھوں نے مختلف سطحوں پر کمپیوٹر سائنس کی تدریس کے فروغ کے لیے بہت سے قومی اور بین الاقوامی سیمینارز اور اجلاسوں میں شرکت کی ہے۔',
        'محمد خالد د اسلام اباد په OPF بویز کالج کې د کمپیوټر ساینس د څانګې مشر دی. د خپل ټول تعلیمي ژوند په اوږدو کې یې لومړۍ درجه لومړۍ ډله ترلاسه کړې. په ۱۹۹۶ کال کې یې د پېښور پوهنتون څخه په کمپیوټر ساینس کې M.Sc وکړ او په ۱۹۹۷ کال کې یې د پېښور پوهنتون د ښوونې او څېړنې له انسټیټیوټ څخه په ساینس کې د B.Ed سند واخیست. هغه تېرو اوولسو کلونو راهیسې د کمپیوټر ساینس لارښود او ښوونکی دی. له ثانوي تر ماسټرۍ کچې د تدریس پراخه تجربه لري. په بېلابېلو کچو د کمپیوټر ساینس د تدریس د ودې لپاره یې په ډېرو ملي او نړیوالو سیمینارونو او غونډو کې ګډون کړی.')
    a.p('He has been member of the National Curriculum development team sicne 2007. He has contributed a great deal in writing the Curriculum of Computer Education from Grades VI-VIII and Curriculum of Computer Science from Grades IX-XII.',
        'وہ 2007 سے قومی نصاب سازی ٹیم کے رکن ہیں۔ انھوں نے جماعت VI-VIII کے لیے کمپیوٹر ایجوکیشن کے نصاب اور جماعت IX-XII کے لیے کمپیوٹر سائنس کے نصاب کی تحریر میں نمایاں حصہ لیا ہے۔',
        'هغه له ۲۰۰۷ کال راهیسې د ملي نصاب جوړونې ټیم غړی دی. د VI-VIII ټولګیو لپاره د کمپیوټر زده‌کړې نصاب او د IX-XII ټولګیو لپاره د کمپیوټر ساینس نصاب په لیکلو کې یې ډېره ونډه اخیستې.')
    a.p('As an author he has written a textbook of Computer Science for grade IX for KPK Textbook Board and a textbook of Computer Education for grade VII for National Books Foundation.',
        'بطور مصنف انھوں نے KPK ٹیکسٹ بک بورڈ کے لیے جماعت نہم کی کمپیوٹر سائنس کی درسی کتاب اور نیشنل بک فاؤنڈیشن کے لیے جماعت ہفتم کی کمپیوٹر ایجوکیشن کی درسی کتاب لکھی ہے۔',
        'د لیکوال په توګه یې د KPK درسي کتابونو بورډ لپاره د نهم ټولګي د کمپیوټر ساینس درسي کتاب او د ملي کتابونو بنسټ لپاره د اووم ټولګي د کمپیوټر زده‌کړې درسي کتاب لیکلی.')
    a.p('Keeping in view his experience and expertise in the subject, this book will prove to be an asset both for the students and the teachers.',
        'مضمون میں ان کے تجربے اور مہارت کو دیکھتے ہوئے یہ کتاب طلبہ اور اساتذہ دونوں کے لیے سرمایہ ثابت ہوگی۔',
        'په مضمون کې د هغه تجربې او مهارت ته په کتو، دا کتاب به د زده‌کوونکو او ښوونکو دواړو لپاره شتمني ثابته شي.')
    r = BOOK.record(a, 'cs12-bm-authors-2', 'About Authors (2)', 'مصنفین کا تعارف (۲)', 'د لیکوالانو په اړه (۲)', 164, [316])
    BOOK.save(164, [(BM, r)], issues=[{'id': 'cs12-pdf164', 'unit': BM, 'printedPage': 316,
               'description': 'About Authors: “National Curriculum development team sicne 2007”. Retained as printed. Owner handwriting on p.316 (a name, sums, the words “chat gpt” and two lines copying the printed text) excluded.'}])


def p165():
    b = Builder()
    b.h('Back matter: Al-Hujurat 10', 'آخری صفحات: سورۃ الحجرات ۱۰', 'وروستۍ پاڼې: سورة الحجرات ۱۰')
    b.p('“The believers are but brothers to one another; so make peace between your two brothers, and keep fearing Allah, so that mercy may be shown to you.” (Surah Al-Hujurat: 10)',
        'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحم کیا جائے۔ (سورۃ الحجرات: ۱۰)',
        '"مؤمنان خو یو د بل وروڼه دي؛ نو د خپلو دوو وروڼو ترمنځ روغه وکړئ، او له الله ووېرېږئ، څو پر تاسو رحم وشي." (سورة الحجرات: ۱۰)')
    r = BOOK.record(b, 'cs12-bm-hujurat', 'Back matter: Al-Hujurat 10', 'آخری صفحات: سورۃ الحجرات ۱۰', 'وروستۍ پاڼې: سورة الحجرات ۱۰', 165, [])
    r['sourceNote'] = 'Unnumbered framed page printed in Urdu (floral border not reproduced); the English and Pashto views carry translations.'
    BOOK.save(165, [(BM, r)], issues=[{'id': 'cs12-pdf165', 'unit': BM, 'printedPage': None,
               'description': 'Two handwritten copies of the verse (above and below the frame) are owner handwriting and are excluded.'}])


def p166():
    b = Builder()
    b.h('Back cover: National Anthem and printing details', 'پچھلا سرورق: قومی ترانہ اور طباعت کی تفصیلات', 'شاتنۍ پوښ: ملي سرود او د چاپ جزییات')
    b.h('قومی ترانہ', 'قومی ترانہ', 'قومی ترانہ')
    for ln in ['پاک سرزمین شاد باد — کشورِ حسین شاد باد', 'تو نشانِ عزمِ عالی شان — ارضِ پاکستان', 'مرکزِ یقین شاد باد', 'پاک سرزمین کا نظام — قوتِ اخوتِ عوام',
               'قوم، ملک، سلطنت — پائندہ تابندہ باد', 'شاد باد منزلِ مراد', 'پرچمِ ستارہ و ہلال — رہبرِ ترقی و کمال', 'ترجمانِ ماضی شانِ حال — جانِ استقبال', 'سایۂ خدائے ذوالجلال']:
        b.p(ln, ln, ln)
    b.p('LEADING BOOKS PUBLISHER, JAMRUD ROAD, PESHAWAR', 'لیڈنگ بکس پبلشر، جمرود روڈ، پشاور', 'لیډنګ بکس پبلشر، جمرود روډ، پېښور')
    b.p('Printer: Creative Printers & Publishers | Price: 184.00 | Quantity: 8,962 | Code No.: PSP/CTV-44-228-1819(O)',
        'مطبع: Creative Printers & Publishers | قیمت: 184.00 | تعداد: 8,962 | کوڈ نمبر: PSP/CTV-44-228-1819(O)',
        'چاپخونه: Creative Printers & Publishers | بیه: 184.00 | شمېر: 8,962 | کوډ شمېره: PSP/CTV-44-228-1819(O)')
    r = BOOK.record(b, 'cs12-back-cover', 'Back cover: National Anthem and printing details', 'پچھلا سرورق: قومی ترانہ اور طباعت کی تفصیلات', 'شاتنۍ پوښ: ملي سرود او د چاپ جزییات', 166, [])
    r['sourceNote'] = 'The National Anthem is shown in Urdu in all language views (same treatment as the other Class 12 books). The cover photograph of a fort and the publisher logo are decorative and not reproduced.'
    BOOK.save(166, [(BM, r)], complete_units=[BM], issues=[{'id': 'cs12-pdf166', 'unit': BM, 'printedPage': None,
               'description': 'Owner pen scribbles over the cover photograph excluded.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 156
    {156: p156, 157: p157, 158: p158, 159: p159, 160: p160, 161: p161, 162: p162, 163: p163, 164: p164, 165: p165, 166: p166}[n]()
