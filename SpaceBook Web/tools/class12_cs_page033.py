"""Computer Science XII PDF33–34: pp.54–56 Unit 2 activities 5–6 and exercise Q1–Q9 (unit 2 complete); p.57 Unit 3 opener — learning outcomes.
Run: python class12_cs_page033.py N (33 or 34)."""
import sys
from class12_cs_common import BOOK, Builder, code


def p33():
    a = Builder()
    for n, en, ur, ps in [
        (5, 'A large travel agency has contacted your IT department within the travel agency to upgrade the current outdated computerized system which the company is using to book seats.', 'ایک بڑی ٹریول ایجنسی نے ایجنسی کے اندر آپ کے آئی ٹی شعبے سے رابطہ کیا ہے تاکہ نشستوں کی بکنگ کے لیے کمپنی کے موجودہ پرانے کمپیوٹرائزڈ نظام کو اپ گریڈ کیا جائے۔', 'یوې لویې سفري ادارې د ادارې دننه ستاسو د IT څانګې سره اړیکه نیولې څو هغه اوسنی زوړ کمپیوټري سیسټم لوړ کړي چې شرکت یې د څوکیو د بکولو لپاره کاروي.'),
        (6, 'Teacher should help the students in drawing flowcharts for the above five (5) projects mentioned in activities 1, 2, 3, 4, and 5, and assign some new problems as well as assignments to draw flowcharts for them.', 'استاد کو چاہیے کہ سرگرمی 1، 2، 3، 4 اور 5 میں مذکور اوپر کے پانچ (5) منصوبوں کے فلو چارٹس بنانے میں طلبہ کی مدد کرے، اور کچھ نئے مسائل اور ان کے فلو چارٹس بنانے کے لیے اسائنمنٹس دے۔', 'ښوونکی دې د ۱، ۲، ۳، ۴ او ۵ فعالیتونو کې د یادو شویو پنځو (۵) پروژو د فلوچارټونو په رسمولو کې له زده‌کوونکو سره مرسته وکړي، او ځینې نوې ستونزې او د هغو د فلوچارټونو د رسمولو دندې دې ورکړي.')]:
        a.h(f'ACTIVITY {n}', f'سرگرمی {n}', f'فعالیت {n}')
        a.p(en, ur, ps)
    ac = BOOK.record(a, 'cs12-u2-activities-2', 'Unit 2 activities (cont.)', 'یونٹ 2: سرگرمیاں (جاری)', '۲ څپرکی: فعالیتونه (دوام)', 33, [54])

    e = Builder()
    e.h('Exercise', 'مشق', 'تمرین')
    e.h('Q.1 Fill in the Blanks.', 'سوال 1: خالی جگہیں پُر کریں۔', 'پوښتنه ۱: تش ځایونه ډک کړئ.')
    e.group('lines', [
     ('i. The requirements which define the function of a software system are called ________ requirements.', 'i. وہ ضروریات جو سافٹ ویئر سسٹم کے فعل کو بیان کرتی ہیں ________ ضروریات کہلاتی ہیں۔', 'i. هغه اړتیاوې چې د سافټویري سیسټم دنده ټاکي ________ اړتیاوې بلل کېږي.'),
     ('ii. All the activities that make a software system available for use is known as software ________ .', 'ii. وہ تمام سرگرمیاں جو سافٹ ویئر سسٹم کو استعمال کے لیے دستیاب بناتی ہیں سافٹ ویئر ________ کہلاتی ہیں۔', 'ii. هغه ټول فعالیتونه چې سافټویري سیسټم د کارونې لپاره برابروي، د سافټویر ________ بلل کېږي.'),
     ('iii. The person who is familiar with a variety of programming languages, operating systems and computer hardware is known as ________ .', 'iii. وہ شخص جو مختلف پروگرامنگ زبانوں، آپریٹنگ سسٹمز اور کمپیوٹر ہارڈویئر سے واقف ہو ________ کہلاتا ہے۔', 'iii. هغه کس چې له بېلابېلو پروګرامي ژبو، عملیاتي سیسټمونو او کمپیوټري هارډویر سره اشنا وي ________ بلل کېږي.'),
     ('iv. A software tester is basically a ________ having a specialty in testing the computer programs.', 'iv. سافٹ ویئر ٹیسٹر بنیادی طور پر ایک ________ ہے جو کمپیوٹر پروگراموں کی جانچ میں مہارت رکھتا ہے۔', 'iv. د سافټویر ازموونکی په اصل کې یو ________ دی چې د کمپیوټري پروګرامونو په ازموینه کې ځانګړی مهارت لري.'),
     ('v. A project manager is a professional in the field of ________ .', 'v. پروجیکٹ مینیجر ________ کے شعبے کا ماہر ہوتا ہے۔', 'v. د پروژې مدیر د ________ په برخه کې مسلکي کس دی.')])
    e.h('Q.2 Select the correct choice for the following Multiple Choice Questions.', 'سوال 2: درج ذیل کثیر الانتخابی سوالات کا درست انتخاب کریں۔', 'پوښتنه ۲: د لاندې څو ځوابه پوښتنو سم ځواب وټاکئ.')
    N = ('None of the above', 'ان میں سے کوئی نہیں', 'له پورته هېڅ یو')
    e.mcq('i.', ('The first step in the system development life cycle is:', 'سسٹم ڈویلپمنٹ لائف سائیکل کا پہلا مرحلہ ہے:', 'د سیسټم د پراختیا د ژوند دورې لومړی ګام دی:'),
          [('Analysis', 'تجزیہ', 'تحلیل'), ('Design', 'ڈیزائن', 'ډیزاین'), ('Problem Identification', 'مسئلے کی نشاندہی', 'د ستونزې پېژندنه'), ('Development and Documentation', 'تیاری اور دستاویز بندی', 'جوړونه او اسناد')], per_line=1)
    e.mcq('ii.', ('The organized process or set of steps that needs to be followed to develop an information system is known as:', 'وہ منظم عمل یا مراحل کا مجموعہ جس پر انفارمیشن سسٹم تیار کرنے کے لیے عمل کرنا ضروری ہو، کہلاتا ہے:', 'هغه منظم بهیر یا د ګامونو ټولګه چې د معلوماتي سیسټم د جوړولو لپاره تعقیبول اړین دي، بلل کېږي:'),
          [('Analytical cycle', 'تجزیاتی سائیکل', 'تحلیلي دوره'), ('Design cycle', 'ڈیزائن سائیکل', 'د ډیزاین دوره'), ('Program specifications', 'پروگرام کی تفصیلات', 'د پروګرام مشخصات'), ('System development life cycle', 'سسٹم ڈویلپمنٹ لائف سائیکل', 'د سیسټم د پراختیا د ژوند دوره')], per_line=1)
    e.mcq('iii.', ('Enhancements, upgradation and bugs fixation are done during the ________ step in the SDLC.', 'SDLC میں بہتری، اپ گریڈیشن اور خامیوں کی درستی ________ مرحلے میں کی جاتی ہے۔', 'په SDLC کې ښه والی، لوړول او د نیمګړتیاوو سمول د ________ ګام پر مهال کېږي.'),
          [('Maintenance and Evaluation', 'دیکھ بھال اور جائزہ', 'ساتنه او ارزونه'), ('Problem Identification', 'مسئلے کی نشاندہی', 'د ستونزې پېژندنه'), ('Design', 'ڈیزائن', 'ډیزاین'), ('Development and Documentation', 'تیاری اور دستاویز بندی', 'جوړونه او اسناد')], per_line=1)
    e.mcq('iv.', ('The ________ determines whether the project should go forward.', '________ طے کرتا ہے کہ آیا منصوبہ آگے بڑھنا چاہیے۔', '________ ټاکي چې ایا پروژه دې مخ ته ولاړه شي.'),
          [('Feasibility', 'فیزیبلٹی', 'د عملي کېدو وړتیا'), ('Problem identification', 'مسئلے کی نشاندہی', 'د ستونزې پېژندنه'), ('System evaluation', 'نظام کا جائزہ', 'د سیسټم ارزونه'), ('Program specification', 'پروگرام کی تفصیل', 'د پروګرام مشخصات')], per_line=1)
    e.mcq('v.', ('________ spend most of their time in the beginning stages of the SDLC, talking with end-users, gathering requirements, documenting systems and proposing solutions.', '________ اپنا زیادہ تر وقت SDLC کے ابتدائی مراحل میں صارفین سے بات چیت، ضروریات جمع کرنے، نظاموں کی دستاویز بندی اور حل تجویز کرنے میں گزارتے ہیں۔', '________ خپل ډېری وخت د SDLC په لومړنیو پړاوونو کې له وروستیو کاروونکو سره په خبرو، د اړتیاوو په راټولولو، د سیسټمونو په اسنادو او د حلونو په وړاندیز کې تېروي.'),
          [('Project managers', 'پروجیکٹ مینیجرز', 'د پروژې مدیران'), ('System analysts', 'سسٹم اینالسٹس', 'د سیسټم شنونکي'), ('Network engineers', 'نیٹ ورک انجینئرز', 'د شبکې انجنیران'), ('Database administrators', 'ڈیٹا بیس ایڈمنسٹریٹرز', 'د ډېټابېس مدیران')], per_line=1)
    e.mcq('vi.', ('The entities having a positive or negative influence in the project completion are known as ________ .', 'منصوبے کی تکمیل پر مثبت یا منفی اثر رکھنے والے ادارے ________ کہلاتے ہیں۔', 'هغه اړخونه چې د پروژې پر بشپړېدو مثبت یا منفي اغېز لري ________ بلل کېږي.'),
          [('Stakeholders', 'اسٹیک ہولڈرز', 'ښکېل اړخونه'), ('Stake supervisors', 'اسٹیک سپروائزرز', 'Stake supervisors'), ('Stake owners', 'اسٹیک اونرز', 'Stake owners'), N], per_line=1)
    ex = BOOK.record(e, 'cs12-u2-exercise-1', 'Unit 2 exercise (1)', 'یونٹ 2: مشق (۱)', '۲ څپرکی: تمرین (۱)', 33, [54, 55])
    ex['sourceNote'] = 'The exercise continues on p.56 (PDF34).'
    BOOK.save(33, [(2, ac), (2, ex)], issues=[{'id': 'cs12-pdf033', 'unit': 2, 'printedPage': 54,
               'description': 'Q1(ii) prints “All the activities … is known as”; Q2(i) offers “Problem Identification” as a first step although the unit names Planning as the first phase. Retained as printed.'}])


def p34():
    e = Builder()
    e.mcq('vii.', ('System maintenance is performed in response to ________ .', 'نظام کی دیکھ بھال ________ کے جواب میں کی جاتی ہے۔', 'د سیسټم ساتنه د ________ په ځواب کې کېږي.'),
          [('Business changes', 'کاروباری تبدیلیوں', 'سوداګریزو بدلونونو'), ('Hardware and software changes', 'ہارڈویئر اور سافٹ ویئر کی تبدیلیوں', 'د هارډویر او سافټویر بدلونونو'),
           ('User’s requests for additional features', 'اضافی خصوصیات کے لیے صارف کی درخواستوں', 'د اضافي ځانګړنو لپاره د کاروونکي غوښتنو'), ('All of the above', 'مندرجہ بالا سب', 'پورته ټول')], per_line=1)
    e.h('Q.3 Write TRUE/FALSE against the following statements.', 'سوال 3: درج ذیل بیانات کے سامنے صحیح/غلط لکھیں۔', 'پوښتنه ۳: د لاندې بیانونو مخې ته سم/ناسم ولیکئ.')
    e.group('lines', [
     ('i. A stakeholder is any person or organization who has a direct or indirect interest in the project.', 'i. اسٹیک ہولڈر کوئی بھی شخص یا تنظیم ہے جو منصوبے میں براہِ راست یا بالواسطہ دلچسپی رکھتی ہو۔', 'i. ښکېل اړخ هر هغه کس یا سازمان دی چې په پروژه کې مستقیمه یا غیر مستقیمه لېوالتیا لري.'),
     ('ii. System maintenance is performed to gather the requirements of the proposed system.', 'ii. نظام کی دیکھ بھال مجوزہ نظام کی ضروریات جمع کرنے کے لیے کی جاتی ہے۔', 'ii. د سیسټم ساتنه د وړاندیز شوي سیسټم د اړتیاوو د راټولولو لپاره کېږي.'),
     ('iii. The how, when, what type of questions are answered in the planning phase of SDLC.', 'iii. کیسے، کب، کیا قسم کے سوالات کے جواب SDLC کے منصوبہ بندی کے مرحلے میں دیے جاتے ہیں۔', 'iii. د څنګه، کله، څه ډول پوښتنو ځوابونه د SDLC د پلان جوړونې په پړاو کې ورکول کېږي.'),
     ('iv. The three architectures i.e. algorithms, pseudo code and flowcharts are used in the implementation phase of SDLC.', 'iv. تین ساختیں یعنی الگورتھمز، سوڈو کوڈ اور فلو چارٹس SDLC کے نفاذ کے مرحلے میں استعمال ہوتی ہیں۔', 'iv. درې جوړښتونه یعنې الګوریتمونه، شبه کوډ او فلوچارټونه د SDLC د پلي کولو په پړاو کې کارول کېږي.'),
     ('v. Each phase of SDLC is accomplished as a discrete, separate step.', 'v. SDLC کا ہر مرحلہ ایک الگ اور جداگانہ قدم کے طور پر مکمل کیا جاتا ہے۔', 'v. د SDLC هر پړاو د یوه جلا او بېل ګام په توګه بشپړېږي.')])
    for q, en, ur, ps in [
        ('Q.4', 'Define software development life cycle (SDLC). What are its objectives?', 'سافٹ ویئر ڈویلپمنٹ لائف سائیکل (SDLC) کی تعریف کریں۔ اس کے مقاصد کیا ہیں؟', 'د سافټویر د پراختیا د ژوند دوره (SDLC) تعریف کړئ. موخې یې کومې دي؟'),
        ('Q.5', 'What is a system? Where exactly the testing activities begin in SDLC?', 'نظام کیا ہے؟ SDLC میں جانچ کی سرگرمیاں ٹھیک کہاں سے شروع ہوتی ہیں؟', 'سیسټم څه دی؟ په SDLC کې د ازموینې فعالیتونه په سمه توګه له کومه ځایه پیلېږي؟'),
        ('Q.6', 'Why software development life cycle is important for the development of software?', 'سافٹ ویئر کی تیاری کے لیے سافٹ ویئر ڈویلپمنٹ لائف سائیکل کیوں اہم ہے؟', 'د سافټویر د جوړولو لپاره د سافټویر د پراختیا د ژوند دوره ولې مهمه ده؟'),
        ('Q.7', 'Who are stakeholders of SDLC? Describe their responsibilities.', 'SDLC کے اسٹیک ہولڈرز کون ہیں؟ ان کی ذمہ داریاں بیان کریں۔', 'د SDLC ښکېل اړخونه څوک دي؟ مسؤولیتونه یې بیان کړئ.'),
        ('Q.8', 'What is meant by the term software requirement? Differentiate between functional and non-functional requirements.', 'سافٹ ویئر کی ضرورت سے کیا مراد ہے؟ فعالیاتی اور غیر فعالیاتی ضروریات میں فرق کریں۔', 'د سافټویر اړتیا څه معنا لري؟ د دندیزو او نادندیزو اړتیاوو ترمنځ توپیر وکړئ.'),
        ('Q.9', 'Design a flowchart for the following algorithm.', 'درج ذیل الگورتھم کے لیے فلو چارٹ بنائیں۔', 'د لاندې الګوریتم لپاره فلوچارټ جوړ کړئ.')]:
        e.p(f'{q} {en}', f'{q} {ur}', f'{q} {ps}')
    code(e, '''sum = 0, N=5
x = 1
while x ≤ N do
sum = sum + x
x = x + 1
end while
print sum''')
    ex = BOOK.record(e, 'cs12-u2-exercise-2', 'Unit 2 exercise (2)', 'یونٹ 2: مشق (۲)', '۲ څپرکی: تمرین (۲)', 34, [56])

    t = Builder()
    t.p('Unit 3', 'یونٹ 3', '۳ څپرکی')
    t.h('PROGRAMMING USING C++', 'سی پلس پلس کے ذریعے پروگرامنگ', 'د C++ په مرسته پروګرام‌سازي')
    t.h('After the completion of Unit-3, Students will be able to:', 'یونٹ 3 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۳ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
    t.group('list', [
     ('Define Program.', 'پروگرام کی تعریف کر سکیں۔', 'پروګرام تعریف کړي.'),
     ('Define header file and reserved words.', 'ہیڈر فائل اور مخصوص الفاظ کی تعریف کر سکیں۔', 'سرلیک فایل او ځانګړې کلمې تعریف کړي.'),
     ('Describe the structure of a C++ program.', 'C++ پروگرام کی ساخت بیان کر سکیں۔', 'د C++ پروګرام جوړښت بیان کړي.'),
     ('Know the use of statement terminator (;).', 'اسٹیٹمنٹ ٹرمینیٹر (;) کا استعمال جان سکیں۔', 'د بیان د پای‌ټکي (;) کارونه وپېژني.'),
     ('Explain the purpose of comments and their syntax.', 'تبصروں کا مقصد اور ان کا طریقۂ تحریر بیان کر سکیں۔', 'د تبصرو موخه او د لیکلو بڼه یې تشریح کړي.'),
     ('Differentiate between Constant and Variable.', 'کانسٹنٹ اور ویری ایبل میں فرق کر سکیں۔', 'د ثابت او متغیر ترمنځ توپیر وکړي.'),
     ('Explain the rules for specifying variable names.', 'ویری ایبل کے نام رکھنے کے قواعد بیان کر سکیں۔', 'د متغیرونو د نوم ایښودو قاعدې تشریح کړي.'),
     ('Know different Data types in C++ and their size in bytes.', 'C++ میں مختلف ڈیٹا ٹائپس اور بائٹس میں ان کا سائز جان سکیں۔', 'په C++ کې بېلابېل ډېټا ډولونه او په بایټ کې اندازه یې وپېژني.'),
     ('Define constant qualifier- const.', 'کانسٹنٹ کوالیفائر const کی تعریف کر سکیں۔', 'ثابت توصیف‌کوونکی const تعریف کړي.'),
     ('Explain the process of declaring and initializing variables', 'ویری ایبلز کے اعلان اور ابتدائی قدر دینے کے عمل کی وضاحت کر سکیں', 'د متغیرونو د اعلان او لومړني ارزښت ورکولو بهیر تشریح کړي'),
     ('Use type casting.', 'ٹائپ کاسٹنگ استعمال کر سکیں۔', 'د ډول بدلول وکاروي.'),
     ('Explain the use of cout and cin statements.', 'cout اور cin بیانات کا استعمال بیان کر سکیں۔', 'د cout او cin بیانونو کارونه تشریح کړي.'),
     ('Define getch(), gets() and puts() functions.', 'getch()، gets() اور puts() فنکشنز کی تعریف کر سکیں۔', 'د getch()، gets() او puts() فنکشنونه تعریف کړي.'),
     ("Define and use escape sequences (\\a, \\b, \\r, \\t, \\\\, \\', \\\").", "ایسکیپ سیکوینسز (\\a، \\b، \\r، \\t، \\\\، \\'، \\\") کی تعریف اور استعمال کر سکیں۔", "د تېښتې لړۍ (\\a، \\b، \\r، \\t، \\\\، \\'، \\\") تعریف او وکاروي."),
     ('Make use of commonly used I/O handling functions.', 'عام استعمال ہونے والے I/O فنکشنز استعمال کر سکیں۔', 'عام کارېدونکي د I/O فنکشنونه وکاروي.'),
     ('Use manipulators endl and setw.', 'endl اور setw مینیپولیٹرز استعمال کر سکیں۔', 'د endl او setw بدلوونکي وکاروي.'),
     ('Define and use different types of operators in C++.', 'C++ میں مختلف اقسام کے آپریٹرز کی تعریف اور استعمال کر سکیں۔', 'په C++ کې بېلابېل ډوله چلونکي تعریف او وکاروي.'),
     ('Identify Unary, binary and ternary operators.', 'یونری، بائنری اور ٹرنری آپریٹرز کی پہچان کر سکیں۔', 'یو-عملي، دوه-عملي او درې-عملي چلونکي وپېژني.'),
     ('Define and explain expression and compound expression.', 'ایکسپریشن اور مرکب ایکسپریشن کی تعریف اور وضاحت کر سکیں۔', 'افاده او مرکبه افاده تعریف او تشریح کړي.'),
     ('Explain the order of precedence of operators.', 'آپریٹرز کی ترجیحی ترتیب بیان کر سکیں۔', 'د چلونکو د لومړیتوب ترتیب تشریح کړي.')])
    UT = ('Object Oriented Programming Using C++', 'سی پلس پلس کے ذریعے آبجیکٹ اورینٹڈ پروگرامنگ', 'د C++ په مرسته شیانو ته متوجه پروګرام‌سازي')
    rec = BOOK.record(t, 'cs12-u3-outcomes', 'Unit 3: learning outcomes', 'یونٹ 3: حاصلاتِ تعلم', '۳ څپرکی: د زده‌کړې پایلې', 34, [57], unit_title=UT)
    rec['sourceNote'] = 'The unit opener is titled “PROGRAMMING USING C++”; the contents page titles the unit “OBJECT ORIENTED PROGRAMMING USING C++”, which is used as the unit title.'
    BOOK.save(34, [(2, ex), (3, rec)], issues=[{'id': 'cs12-pdf034', 'unit': 2, 'printedPage': 56,
               'description': 'Q5 prints “Where exactly the testing activities begin in SDLC?”; Q6 “Why software development life cycle is important”. Owner handwriting next to Q9 excluded. Unit-3 opener title differs from the contents (see sourceNote).'}], complete_units=[2])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 33
    p33() if n == 33 else p34()
