"""Computer Science XII PDF25 (spread): printed pp.38–39 — iv. schedule feasibility; c. analysis phase; d. requirement engineering; requirement gathering; functional requirements a–d."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
H('iv. Schedule feasibility', 'iv. شیڈول فیزیبلٹی', 'iv. د مهالوېش وړتیا')
P('It means that a project can be implemented in an acceptable time frame.', 'اس کا مطلب ہے کہ منصوبہ قابلِ قبول وقت میں نافذ کیا جا سکتا ہے۔', 'مطلب یې دا دی چې پروژه د منلو وړ وخت کې پلي کېدای شي.')
H('c. Analysis phase', 'c. تجزیے کا مرحلہ', 'c. د تحلیل پړاو')
P('In this phase, the incharge of the project team must decide if the project should go ahead with the available resources or not. Analysis is also looking at the existing system to see what and how it is doing its job. The project team asks the following questions during the analysis.',
  'اس مرحلے میں پروجیکٹ ٹیم کے انچارج کو فیصلہ کرنا ہوتا ہے کہ آیا منصوبہ دستیاب وسائل کے ساتھ آگے بڑھنا چاہیے یا نہیں۔ تجزیے میں موجودہ نظام کو بھی دیکھا جاتا ہے کہ وہ کیا اور کیسے اپنا کام کر رہا ہے۔ تجزیے کے دوران پروجیکٹ ٹیم درج ذیل سوالات پوچھتی ہے۔',
  'په دې پړاو کې د پروژې د ټیم مسؤول باید پرېکړه وکړي چې ایا پروژه دې د شته سرچینو سره مخ ته ولاړه شي که نه. تحلیل اوسني سیسټم ته هم ګوري چې څه او څنګه خپله دنده ترسره کوي. د تحلیل پر مهال د پروژې ټیم لاندې پوښتنې کوي.')
t.group('list', [('Can the proposed software system be developed with the available resources and budget?', 'کیا مجوزہ سافٹ ویئر سسٹم دستیاب وسائل اور بجٹ کے ساتھ تیار کیا جا سکتا ہے؟', 'ایا وړاندیز شوی سافټویري سیسټم د شته سرچینو او بودیجې سره جوړېدای شي؟'),
                 ('Will this system significantly improve the organization?', 'کیا یہ نظام تنظیم کو نمایاں طور پر بہتر بنائے گا؟', 'ایا دا سیسټم سازمان په ډېره اندازه ښه کوي؟'),
                 ('Does the existing system even need to be replaced?', 'کیا موجودہ نظام کو بدلنے کی ضرورت بھی ہے؟', 'ایا اوسني سیسټم بدلولو ته اصلاً اړتیا شته؟')])
H('Activities of the analysis phase', 'تجزیے کے مرحلے کی سرگرمیاں', 'د تحلیل پړاو فعالیتونه')
t.group('list', [('Gather information to learn problem domain', 'مسئلے کے دائرے کو سمجھنے کے لیے معلومات جمع کرنا', 'د ستونزې د ساحې د پېژندو لپاره معلومات راټولول'),
                 ('Define system requirements.', 'نظام کی ضروریات متعین کرنا۔', 'د سیسټم اړتیاوې ټاکل.'), ('Prioritize requirements.', 'ضروریات کی ترجیح طے کرنا۔', 'اړتیاوو ته لومړیتوب ورکول.'),
                 ('Build prototypes for feasibility and discovery of requirements.', 'قابلِ عمل ہونے اور ضروریات کی دریافت کے لیے نمونے (پروٹوٹائپس) بنانا۔', 'د عملي کېدو او د اړتیاوو د موندلو لپاره لومړني نمونې (prototypes) جوړول.'),
                 ('Generate and evaluate alternative solutions for the problem in hand.', 'درپیش مسئلے کے متبادل حل تیار کرنا اور ان کا جائزہ لینا۔', 'د مخې ستونزې لپاره بدیل حلونه جوړول او ارزول.'),
                 ('Review recommendations with top level management to decide about the project.', 'منصوبے کے بارے میں فیصلے کے لیے اعلیٰ انتظامیہ کے ساتھ سفارشات کا جائزہ لینا۔', 'د پروژې په اړه د پرېکړې لپاره له لوړ پوړي مدیریت سره د سپارښتنو بیاکتنه.')])
H('d. Requirement engineering', 'd. ریکوائرمنٹ انجینئرنگ', 'd. د اړتیاوو انجنیري')
P('Requirements Engineering (RE) is a set of activities used to identify and communicate the purpose of a software system, and the contexts in which it will be used. Requirement engineering consists of the following steps.',
  'ریکوائرمنٹس انجینئرنگ (RE) سرگرمیوں کا ایک مجموعہ ہے جو سافٹ ویئر سسٹم کے مقصد اور ان سیاق و سباق کی نشاندہی اور ابلاغ کے لیے استعمال ہوتا ہے جن میں اسے استعمال کیا جائے گا۔ ریکوائرمنٹ انجینئرنگ درج ذیل مراحل پر مشتمل ہے۔',
  'د اړتیاوو انجنیري (RE) د فعالیتونو یوه ټولګه ده چې د سافټویري سیسټم د موخې او هغو شرایطو د پېژندو او خبرولو لپاره کارول کېږي چې پکې به وکارول شي. د اړتیاوو انجنیري لاندې ګامونه لري.')
t.group('list', [('Requirement gathering', 'ضروریات کی جمع آوری', 'د اړتیاوو راټولول'), ('Requirement validation', 'ضروریات کی توثیق', 'د اړتیاوو تایید'), ('Requirements management', 'ضروریات کا انتظام', 'د اړتیاوو اداره')])
H('Requirement gathering', 'ضروریات کی جمع آوری', 'د اړتیاوو راټولول')
P('Requirement gathering is usually the first part of any software product. In this phase, meetings with the customers or prospective customers are arranged; the market requirements and features that are in demand are analyzed. It is also to find out if there is a real need in the market for the software product that is proposed to be developed.',
  'ضروریات کی جمع آوری عموماً کسی بھی سافٹ ویئر پروڈکٹ کا پہلا حصہ ہوتی ہے۔ اس مرحلے میں گاہکوں یا ممکنہ گاہکوں کے ساتھ ملاقاتیں کی جاتی ہیں؛ مارکیٹ کی ضروریات اور طلب میں موجود خصوصیات کا تجزیہ کیا جاتا ہے۔ یہ بھی معلوم کیا جاتا ہے کہ کیا مجوزہ سافٹ ویئر پروڈکٹ کی مارکیٹ میں واقعی ضرورت ہے۔',
  'د اړتیاوو راټولول عموماً د هر سافټویري محصول لومړۍ برخه وي. په دې پړاو کې له پېرودونکو یا احتمالي پېرودونکو سره غونډې ترتیبېږي؛ د بازار اړتیاوې او هغه ځانګړنې چې غوښتنه یې شته، تحلیلېږي. دا هم معلومېږي چې ایا په بازار کې د جوړېدو لپاره وړاندیز شوي سافټویري محصول ته رښتینې اړتیا شته.')
P('These requirements are of two types:', 'یہ ضروریات دو قسم کی ہوتی ہیں:', 'دا اړتیاوې دوه ډوله دي:')
t.group('list', [('Functional requirements', 'فعالیاتی ضروریات', 'دندیزې اړتیاوې'), ('Non-Functional Requirements', 'غیر فعالیاتی ضروریات', 'نادندیزې اړتیاوې')])
P('Functional requirements: Functional requirement are those requirements of a software system which describe a function of a software system or its component. It includes calculations, technical details, data manipulation and processing and other specific functionality that define what a system is supposed to accomplish. Examples of functional requirements are:',
  'فعالیاتی ضروریات: فعالیاتی ضروریات سافٹ ویئر سسٹم کی وہ ضروریات ہیں جو سافٹ ویئر سسٹم یا اس کے کسی جز کے فعل کو بیان کرتی ہیں۔ اس میں حسابات، تکنیکی تفصیلات، ڈیٹا میں ردوبدل اور پراسیسنگ اور دیگر مخصوص افعال شامل ہیں جو یہ متعین کرتے ہیں کہ نظام کو کیا انجام دینا ہے۔ فعالیاتی ضروریات کی مثالیں یہ ہیں:',
  'دندیزې اړتیاوې: دندیزې اړتیاوې د سافټویري سیسټم هغه اړتیاوې دي چې د سافټویري سیسټم یا د هغه د یوې برخې دنده بیانوي. پکې محاسبې، تخنیکي جزییات، د ډېټا بدلون او پروسس او نور ځانګړي فعالیتونه شامل دي چې ټاکي سیسټم باید څه ترسره کړي. د دندیزو اړتیاوو بېلګې دا دي:')
for hen, hur, hps, items in [
    ('a) Interface requirements', 'a) انٹرفیس کی ضروریات', 'a) د منځګړي اړتیاوې', [('Field accepts numeric data entry.', 'فیلڈ عددی ڈیٹا کا اندراج قبول کرتی ہے۔', 'ساحه شمېریزه ډېټا مني.'), ('Field only accepts dates before the current date.', 'فیلڈ صرف موجودہ تاریخ سے پہلے کی تاریخیں قبول کرتی ہے۔', 'ساحه یوازې له اوسنۍ نېټې مخکې نېټې مني.'), ('Screen can print on-screen data to the printer.', 'اسکرین پر موجود ڈیٹا پرنٹر پر پرنٹ کیا جا سکتا ہے۔', 'پرده کولی شي پر پرده ښودل شوې ډېټا پرنټر ته چاپ کړي.')]),
    ('b) Business requirements', 'b) کاروباری ضروریات', 'b) سوداګریزې اړتیاوې', [('Data must be entered before a request can be approved.', 'درخواست کی منظوری سے پہلے ڈیٹا کا اندراج لازمی ہے۔', 'مخکې له دې چې غوښتنه تصویب شي، باید ډېټا ولیکل شي.')]),
    ('c) Regulatory/Compliance requirements', 'c) ضابطہ جاتی/تعمیلی ضروریات', 'c) مقرراتي/پیروي اړتیاوې', [('The database will have a functional audit trail.', 'ڈیٹا بیس میں فعال آڈٹ ٹریل ہوگا۔', 'ډېټابېس به فعاله د پلټنې لړۍ ولري.'), ('The system will limit access to authorized users.', 'نظام رسائی کو مجاز صارفین تک محدود کرے گا۔', 'سیسټم به لاسرسی واکمنو کاروونکو ته محدودوي.'), ('The spreadsheet can secure data with electronic signatures.', 'اسپریڈ شیٹ الیکٹرانک دستخط سے ڈیٹا محفوظ کر سکتی ہے۔', 'سپرېډشیټ کولی شي ډېټا په برېښنايي لاسلیکونو خوندي کړي.')]),
    ('d) Security requirements', 'd) سلامتی کی ضروریات', 'd) امنیتي اړتیاوې', [('Member of the Data Entry group can enter requests but not approve or delete requests.', 'ڈیٹا انٹری گروپ کا رکن درخواستیں درج کر سکتا ہے لیکن انھیں منظور یا حذف نہیں کر سکتا۔', 'د ډېټا ننوتو د ډلې غړی غوښتنې لیکلی شي خو تصویبولی یا ړنګولی یې نه شي.')])]:
    H(hen, hur, hps)
    t.group('lines', items)
rec = BOOK.record(t, 'cs12-u2-text-4', 'Unit 2 text (4)', 'یونٹ 2 — متن (۴)', '۲ څپرکی — متن (۴)', 25, [38, 39])
rec['sourceNote'] = 'The security-requirements list continues on p.40 (PDF26).'
issues = [{'id': 'cs12-pdf025', 'unit': 2, 'printedPage': 39,
           'description': 'p.39 prints “Functional requirement are those requirements” and “functionality that define”; p.38 “Analysis is also looking at”. Retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(25, [(2, rec)], issues=issues)
