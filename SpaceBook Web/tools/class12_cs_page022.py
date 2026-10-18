"""Computer Science XII PDF22 (spread): printed pp.32–33 — 2.1 introduction; 2.1.1 a system; SDLC; 2.1.2 SDLC and its importance; 2.1.3 objectives (begins)."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
H('2.1 INTRODUCTION', '2.1 تعارف', '۲.۱ پېژندنه')
P('Systems are created to solve problems. Nowadays, systems are so big and complex that teams of architects, analysts, programmers, testers and users must work together to create the millions of lines of custom-written code that drive our enterprises. To manage this, a number of system development life cycle (SDLC) models have been created. This Unit is focused on SDLC, its importance, objectives, stakeholders and logical phases that are followed for the development of a software product.',
  'نظام مسائل حل کرنے کے لیے بنائے جاتے ہیں۔ آج کل نظام اتنے بڑے اور پیچیدہ ہیں کہ معماروں، تجزیہ کاروں، پروگرامرز، ٹیسٹرز اور صارفین کی ٹیموں کو مل کر کام کرنا پڑتا ہے تاکہ اپنی ضرورت کے مطابق لکھے گئے کوڈ کی وہ لاکھوں سطریں تیار کی جا سکیں جو ہمارے اداروں کو چلاتی ہیں۔ اس کے انتظام کے لیے سسٹم ڈویلپمنٹ لائف سائیکل (SDLC) کے کئی ماڈل بنائے گئے ہیں۔ یہ یونٹ SDLC، اس کی اہمیت، مقاصد، اسٹیک ہولڈرز اور ان منطقی مراحل پر مرکوز ہے جو کسی سافٹ ویئر پروڈکٹ کی تیاری کے لیے اختیار کیے جاتے ہیں۔',
  'سیسټمونه د ستونزو د حل لپاره جوړېږي. نن ورځ سیسټمونه دومره لوی او پېچلي دي چې د معمارانو، شنونکو، پروګرام جوړوونکو، ازموونکو او کاروونکو ټیمونه باید یوځای کار وکړي، څو د ځانګړي لیکل شوي کوډ هغه میلیونونه کرښې جوړې کړي چې زموږ موسسې چلوي. د دې د ادارې لپاره د سیسټم د پراختیا د ژوند دورې (SDLC) څو ماډلونه جوړ شوي. دا څپرکی پر SDLC، اهمیت، موخو، ښکېلو اړخونو او هغو منطقي پړاوونو تمرکز لري چې د یوه سافټویري محصول د جوړولو لپاره تعقیبېږي.')
H('2.1.1 A System', '2.1.1 سسٹم', '۲.۱.۱ سیسټم')
P('The term system is originated from the Greek term systēma, which means to “place together.” It can be defined as a set of interrelated components having a clearly defined boundary that work together to achieve a common set of objectives.',
  'لفظ سسٹم یونانی اصطلاح systēma سے نکلا ہے جس کا مطلب ہے ’’ایک ساتھ رکھنا‘‘۔ اسے باہم مربوط اجزاء کے ایسے مجموعے کے طور پر بیان کیا جا سکتا ہے جس کی حد واضح طور پر متعین ہو اور جو مشترکہ مقاصد حاصل کرنے کے لیے مل کر کام کریں۔',
  'د سیسټم اصطلاح له یوناني اصطلاح systēma څخه راوتلې چې معنا یې "یوځای ایښودل" ده. دا د یو له بل سره تړلو برخو د داسې ټولګې په توګه تعریف کېدای شي چې روښانه ټاکلې پوله لري او د ګډو موخو د ترلاسه کولو لپاره یوځای کار کوي.')
P('A system can be developed by applying a set of methods, procedures and routines in a proper sequence to carry out some specific task. When all these functions are applied to build software then the system will be called as a software system.',
  'کسی مخصوص کام کو انجام دینے کے لیے طریقوں، ضابطوں اور معمولات کے ایک مجموعے کو مناسب ترتیب سے لاگو کر کے نظام تیار کیا جا سکتا ہے۔ جب یہ تمام افعال سافٹ ویئر بنانے کے لیے لاگو کیے جائیں تو نظام کو سافٹ ویئر سسٹم کہا جائے گا۔',
  'یو سیسټم د یوې ځانګړې دندې د ترسره کولو لپاره د طریقو، کړنلارو او معمولاتو د یوې ټولګې په سم ترتیب پلي کولو سره جوړېدای شي. کله چې دا ټولې دندې د سافټویر د جوړولو لپاره پلي شي، نو سیسټم ته سافټویري سیسټم ویل کېږي.')
H('System Development Life Cycle (SDLC)', 'سسٹم ڈویلپمنٹ لائف سائیکل (SDLC)', 'د سیسټم د پراختیا د ژوند دوره (SDLC)')
P('The systems development life cycle (SDLC) is a conceptual model used in project management that describes the stages involved in an information system development project from an initial feasibility study through maintenance of the completed application.',
  'سسٹمز ڈویلپمنٹ لائف سائیکل (SDLC) پروجیکٹ مینجمنٹ میں استعمال ہونے والا ایک تصوراتی ماڈل ہے جو کسی انفارمیشن سسٹم کی تیاری کے منصوبے میں ابتدائی فیزیبلٹی اسٹڈی سے لے کر مکمل ایپلیکیشن کی دیکھ بھال تک کے مراحل بیان کرتا ہے۔',
  'د سیسټمونو د پراختیا د ژوند دوره (SDLC) د پروژې په مدیریت کې کارېدونکی مفهومي ماډل دی چې د معلوماتي سیسټم د جوړولو په پروژه کې له لومړنۍ د عملي کېدو وړتیا څېړنې تر بشپړ شوي کاريال ساتنې پورې پړاوونه بیانوي.')
H('2.1.2 System development life cycle and its importance', '2.1.2 سسٹم ڈویلپمنٹ لائف سائیکل اور اس کی اہمیت', '۲.۱.۲ د سیسټم د پراختیا د ژوند دوره او اهمیت یې')
P('System Development Life Cycle (SDLC) is a step wise process of creating computer systems. It is also known as information system development or application development. It is a conceptual model which represents the necessary steps used for the development process of a software system.',
  'سسٹم ڈویلپمنٹ لائف سائیکل (SDLC) کمپیوٹر سسٹمز بنانے کا ایک مرحلہ وار عمل ہے۔ اسے انفارمیشن سسٹم ڈویلپمنٹ یا ایپلیکیشن ڈویلپمنٹ بھی کہا جاتا ہے۔ یہ ایک تصوراتی ماڈل ہے جو سافٹ ویئر سسٹم کی تیاری کے عمل کے لیے ضروری مراحل کی نمائندگی کرتا ہے۔',
  'د سیسټم د پراختیا د ژوند دوره (SDLC) د کمپیوټري سیسټمونو د جوړولو ګام په ګام بهیر دی. د معلوماتي سیسټم د پراختیا یا د کاريال د پراختیا په نوم هم یادېږي. دا یو مفهومي ماډل دی چې د سافټویري سیسټم د جوړولو د بهیر اړین ګامونه ښيي.')
P('The SDLC is a problem-solving process through which a series of steps helps to produce a new computer information system. The entire steps conducted in a sequence should provide the answers to a problem or opportunity. This step-wise procedure to build a system has a lot of importance.',
  'SDLC مسائل حل کرنے کا ایک عمل ہے جس کے ذریعے مراحل کا ایک سلسلہ نیا کمپیوٹر انفارمیشن سسٹم تیار کرنے میں مدد دیتا ہے۔ ترتیب سے کیے گئے تمام مراحل کو کسی مسئلے یا موقع کا جواب فراہم کرنا چاہیے۔ نظام بنانے کے اس مرحلہ وار طریقۂ کار کی بہت اہمیت ہے۔',
  'SDLC د ستونزو د حل بهیر دی چې پکې د ګامونو یوه لړۍ د نوي کمپیوټري معلوماتي سیسټم په جوړولو کې مرسته کوي. په ترتیب ترسره شوي ټول ګامونه باید یوې ستونزې یا فرصت ته ځواب ورکړي. د سیسټم د جوړولو دا ګام په ګام کړنلاره ډېر اهمیت لري.')
H('Importance of SDLC', 'ایس ڈی ایل سی کی اہمیت', 'د SDLC اهمیت')
P('The following points summarize the importance of the use of SDLC.', 'درج ذیل نکات SDLC کے استعمال کی اہمیت کا خلاصہ پیش کرتے ہیں۔', 'لاندې ټکي د SDLC د کارونې اهمیت لنډوي.')
t.group('list', [
 ('SDLC is important because it breaks down the entire life cycle of software development into phases thus making it easier for the development team members to easily evaluate each part of software development.', 'SDLC اس لیے اہم ہے کہ یہ سافٹ ویئر کی تیاری کے پورے لائف سائیکل کو مراحل میں تقسیم کرتا ہے، جس سے ٹیم کے اراکین کے لیے سافٹ ویئر کی تیاری کے ہر حصے کو آسانی سے جانچنا آسان ہو جاتا ہے۔', 'SDLC ځکه مهم دی چې د سافټویر د جوړولو ټوله د ژوند دوره په پړاوونو وېشي، چې له امله یې د جوړوونکي ټیم غړو ته د سافټویر د جوړولو د هرې برخې ارزونه اسانه کېږي.'),
 ('SDLC makes it easier for programmers to work concurrently on each phase.', 'SDLC پروگرامرز کے لیے ہر مرحلے پر بیک وقت کام کرنا آسان بناتا ہے۔', 'SDLC پروګرام جوړوونکو ته پر هر پړاو په یو وخت کار اسانه کوي.'),
 ('It provides a rough time estimate that when the software will be available for use.', 'یہ ایک اندازاً وقت فراہم کرتا ہے کہ سافٹ ویئر کب استعمال کے لیے دستیاب ہوگا۔', 'دا یو اټکلي وخت برابروي چې سافټویر به کله د کارونې لپاره چمتو وي.'),
 ('It delivers quality software which meet or exceed customer expectations.', 'یہ معیاری سافٹ ویئر فراہم کرتا ہے جو گاہک کی توقعات پر پورا اترے یا ان سے بڑھ کر ہو۔', 'دا باکیفیته سافټویر وړاندې کوي چې د پېرودونکي تمې پوره کوي یا ترې زیات وي.'),
 ('It provides the basic framework for the developing of quality software.', 'یہ معیاری سافٹ ویئر کی تیاری کے لیے بنیادی ڈھانچہ فراہم کرتا ہے۔', 'دا د باکیفیته سافټویر د جوړولو لپاره بنسټیز چوکاټ برابروي.'),
 ('SDLC helps the project managers to establish a project management structure to be followed strictly during the system development.', 'SDLC پروجیکٹ مینیجرز کو ایک پروجیکٹ مینجمنٹ ڈھانچہ قائم کرنے میں مدد دیتا ہے جس پر نظام کی تیاری کے دوران سختی سے عمل کیا جائے۔', 'SDLC د پروژې مدیرانو سره د پروژې د مدیریت یو جوړښت په جوړولو کې مرسته کوي چې د سیسټم د جوړولو پر مهال په کلکه تعقیب شي.'),
 ('SDLC clearly defines and assigns the roles and responsibilities of all the involved parties.', 'SDLC تمام شامل فریقوں کے کردار اور ذمہ داریاں واضح طور پر متعین اور تفویض کرتا ہے۔', 'SDLC د ټولو ښکېلو اړخونو رولونه او مسؤولیتونه په روښانه ډول ټاکي او سپاري.'),
 ('It ensures that the requirements for the development of the software system are well defined and subsequently satisfied.', 'یہ یقینی بناتا ہے کہ سافٹ ویئر سسٹم کی تیاری کی ضروریات اچھی طرح متعین ہوں اور بعد ازاں پوری ہوں۔', 'دا ډاډ ورکوي چې د سافټویري سیسټم د جوړولو اړتیاوې ښې ټاکل شوې او وروسته پوره شوې وي.')])
H('2.1.3 Objectives of SDLC', '2.1.3 ایس ڈی ایل سی کے مقاصد', '۲.۱.۳ د SDLC موخې')
P('The objectives of the System Development Life Cycle (SDLC) are as follows:', 'سسٹم ڈویلپمنٹ لائف سائیکل (SDLC) کے مقاصد درج ذیل ہیں:', 'د سیسټم د پراختیا د ژوند دورې (SDLC) موخې دا دي:')
t.group('list', [
 ('Delivery of quality software that meet the customer expectations.', 'ایسے معیاری سافٹ ویئر کی فراہمی جو گاہک کی توقعات پر پورا اترے۔', 'د داسې باکیفیته سافټویر وړاندې کول چې د پېرودونکي تمې پوره کړي.'),
 ('Delivery of inexpensive and cost-effective software which are easily maintainable.', 'کم خرچ اور کفایتی سافٹ ویئر کی فراہمی جس کی دیکھ بھال آسان ہو۔', 'د ارزانه او اقتصادي سافټویر وړاندې کول چې ساتنه یې اسانه وي.'),
 ('Maximize productivity in terms of the software systems delivered.', 'فراہم کردہ سافٹ ویئر سسٹمز کے لحاظ سے پیداواری صلاحیت کو زیادہ سے زیادہ کرنا۔', 'د وړاندې شویو سافټویري سیسټمونو له پلوه د تولید وړتیا تر ټولو لوړول.')])
rec = BOOK.record(t, 'cs12-u2-text-1', 'Unit 2 text (1)', 'یونٹ 2 — متن (۱)', '۲ څپرکی — متن (۱)', 22, [32, 33])
rec['sourceNote'] = 'The objectives list continues on p.34 (PDF23).'
issues = [{'id': 'cs12-pdf022', 'unit': 2, 'printedPage': 33,
           'description': 'p.33 prints “software which meet”, “for the developing of”, “software which are easily maintainable”. Retained as printed. Owner pen circling/scribbles on pp.32–33 excluded.'}]

if __name__ == '__main__':
    BOOK.save(22, [(2, rec)], issues=issues)
