"""Computer Science XII PDF30 (spread): printed pp.48–49 — a. management; b. project manager; c. system analyst."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
H('a. Management', 'a. انتظامیہ', 'a. مدیریت')
P('Organizing, coordinating and controlling the activities of a software development by the managers and executives in accordance with certain standard procedures is called management. A strong management has the ability to satisfy the customers and acquirers of the software system. Also, a proposed project or a product will only meet its objectives if managed properly, otherwise, will result in failure.',
  'مینیجرز اور منتظمین کا کچھ معیاری طریقۂ کار کے مطابق سافٹ ویئر کی تیاری کی سرگرمیوں کو منظم کرنا، ہم آہنگ کرنا اور کنٹرول کرنا انتظامیہ (مینجمنٹ) کہلاتا ہے۔ مضبوط انتظامیہ سافٹ ویئر سسٹم کے گاہکوں اور حاصل کنندگان کو مطمئن کرنے کی صلاحیت رکھتی ہے۔ نیز کوئی مجوزہ منصوبہ یا پروڈکٹ اسی وقت اپنے مقاصد پورے کرے گا جب اس کا انتظام درست ہو، ورنہ ناکامی ہوگی۔',
  'د مدیرانو او اجرايي چارواکو له خوا د ځینو معیاري کړنلارو سره سم د سافټویر د جوړولو د فعالیتونو تنظیمول، همغږي کول او کنټرولول مدیریت بلل کېږي. پیاوړی مدیریت د سافټویري سیسټم پېرودونکي او ترلاسه کوونکي خوښول وړتیا لري. همداراز یوه وړاندیز شوې پروژه یا محصول یوازې هغه وخت خپلې موخې پوره کوي چې په سم ډول اداره شي، که نه پایله به یې ناکامي وي.')
P('The role of good Management is to:', 'اچھی انتظامیہ کا کردار یہ ہے:', 'د ښه مدیریت رول دا دی:')
t.group('list', [
 ('Provide consistency of success of the software with regard to Time, Cost, and Quality objectives.', 'وقت، لاگت اور معیار کے مقاصد کے لحاظ سے سافٹ ویئر کی کامیابی میں تسلسل فراہم کرنا۔', 'د وخت، لګښت او کیفیت د موخو په اړه د سافټویر د بریا دوام برابرول.'),
 ('Ensure that customer expectations are met.', 'یقینی بنانا کہ گاہک کی توقعات پوری ہوں۔', 'ډاډمنول چې د پېرودونکي تمې پوره شوې.'),
 ('Collect historical information and data for future use.', 'مستقبل کے استعمال کے لیے تاریخی معلومات اور ڈیٹا جمع کرنا۔', 'د راتلونکي کارونې لپاره تاریخي معلومات او ډېټا راټولول.'),
 ('Provide a method of thought for ensuring all requirements are addressed through a comprehensive work definition process.', 'ایک ایسا طریقۂ فکر فراہم کرنا جس سے جامع کام کی تعریف کے عمل کے ذریعے تمام ضروریات کا احاطہ یقینی ہو۔', 'د فکر داسې لاره برابرول چې د کار د جامع تعریف د بهیر له لارې ټولې اړتیاوې ډاډمنې شي.'),
 ('Reduce risks associated with the project.', 'منصوبے سے وابستہ خطرات کم کرنا۔', 'له پروژې سره تړلي خطرونه کمول.'),
 ('Minimize scope creep by providing a process for managing changes.', 'تبدیلیوں کے انتظام کا عمل فراہم کر کے دائرۂ کار کے بے قابو پھیلاؤ کو کم کرنا۔', 'د بدلونونو د ادارې بهیر برابرولو سره د ساحې ناکنټرول پراختیا کمول.')])
H('b. Project Manager', 'b. پروجیکٹ مینیجر', 'b. د پروژې مدیر')
P('A project manager is a professional in the field of project management responsible for planning, execution, and closing of any project. Apart from management skills, a software project manager will typically have an extensive background in software development. He is also expected to be familiar with the whole software development life cycle process. The specific responsibilities of the project manager vary depending on the company size, the company maturity, and the company culture.',
  'پروجیکٹ مینیجر پروجیکٹ مینجمنٹ کے شعبے کا ماہر ہوتا ہے جو کسی بھی منصوبے کی منصوبہ بندی، نفاذ اور اختتام کا ذمہ دار ہوتا ہے۔ انتظامی مہارتوں کے علاوہ سافٹ ویئر پروجیکٹ مینیجر عموماً سافٹ ویئر کی تیاری کا وسیع پس منظر رکھتا ہے۔ اس سے یہ بھی توقع کی جاتی ہے کہ وہ سافٹ ویئر ڈویلپمنٹ لائف سائیکل کے پورے عمل سے واقف ہو۔ پروجیکٹ مینیجر کی مخصوص ذمہ داریاں کمپنی کے حجم، پختگی اور ثقافت کے لحاظ سے مختلف ہوتی ہیں۔',
  'د پروژې مدیر د پروژې د مدیریت په برخه کې مسلکي کس دی چې د هرې پروژې د پلان جوړونې، اجرا او پای ته رسولو مسؤول وي. د مدیریتي مهارتونو سربېره د سافټویري پروژې مدیر عموماً د سافټویر په جوړولو کې پراخه سابقه لري. له هغه دا هم تمه کېږي چې د سافټویر د پراختیا د ژوند دورې له ټول بهیر سره اشنا وي. د پروژې د مدیر ځانګړي مسؤولیتونه د شرکت د اندازې، پخوالي او کلتور له مخې توپیر لري.')
P('The role of project manager is to manage:', 'پروجیکٹ مینیجر کا کردار ان کا انتظام کرنا ہے:', 'د پروژې د مدیر رول د لاندې اداره ده:')
t.group('list', [('Project plan', 'منصوبے کا خاکہ', 'د پروژې پلان'), ('Project stakeholders', 'منصوبے کے اسٹیک ہولڈرز', 'د پروژې ښکېل اړخونه'), ('Project team', 'پروجیکٹ ٹیم', 'د پروژې ټیم'),
                 ('Project risk', 'منصوبے کا خطرہ', 'د پروژې خطر'), ('Project schedule', 'منصوبے کا نظام الاوقات', 'د پروژې مهالوېش'), ('Project budget', 'منصوبے کا بجٹ', 'د پروژې بودیجه'),
                 ('Project conflicts', 'منصوبے کے تنازعات', 'د پروژې شخړې')])
H('c. System Analyst', 'c. سسٹم اینالسٹ', 'c. د سیسټم شنونکی')
P('A systems analyst is a professional in the field of software development that studies the problems, plans solutions for them, recommends software systems, and coordinates development to meet business or other requirements. System analyst has expertise in a variety of programming languages, operating systems, and computer hardware platforms. Because they often write user requests into technical specifications, the systems analyst is the contact person between vendor and information technology professionals. Analyst may be responsible for developing cost analysis, design considerations, and implementation time.',
  'سسٹمز اینالسٹ سافٹ ویئر کی تیاری کے شعبے کا وہ ماہر ہے جو مسائل کا مطالعہ کرتا ہے، ان کے حل کی منصوبہ بندی کرتا ہے، سافٹ ویئر سسٹمز تجویز کرتا ہے اور کاروباری یا دیگر ضروریات پوری کرنے کے لیے تیاری کو ہم آہنگ کرتا ہے۔ سسٹم اینالسٹ مختلف پروگرامنگ زبانوں، آپریٹنگ سسٹمز اور کمپیوٹر ہارڈویئر پلیٹ فارمز میں مہارت رکھتا ہے۔ چونکہ وہ اکثر صارفین کی درخواستوں کو تکنیکی تفصیلات میں لکھتے ہیں، اس لیے سسٹمز اینالسٹ فروخت کنندہ اور انفارمیشن ٹیکنالوجی کے ماہرین کے درمیان رابطے کا ذریعہ ہوتا ہے۔ اینالسٹ لاگت کے تجزیے، ڈیزائن کے پہلوؤں اور نفاذ کے وقت کی تیاری کا ذمہ دار ہو سکتا ہے۔',
  'د سیسټمونو شنونکی د سافټویر د جوړولو په برخه کې هغه مسلکي کس دی چې ستونزې څېړي، د هغو لپاره حلونه پلانوي، سافټویري سیسټمونه وړاندیزوي او د سوداګریزو یا نورو اړتیاوو د پوره کولو لپاره جوړونه همغږي کوي. د سیسټم شنونکی په بېلابېلو پروګرامي ژبو، عملیاتي سیسټمونو او کمپیوټري هارډویري پلیټفارمونو کې مهارت لري. څرنګه چې دوی ډېری وخت د کاروونکو غوښتنې په تخنیکي مشخصاتو اړوي، نو د سیسټمونو شنونکی د پلورونکي او معلوماتي ټکنالوژۍ د مسلکي کسانو ترمنځ د اړیکې کس وي. شنونکی کېدای شي د لګښت د تحلیل، د ډیزاین د ملاحظاتو او د پلي کولو د وخت د جوړولو مسؤول وي.')
P('The role of system analyst is to:', 'سسٹم اینالسٹ کا کردار یہ ہے:', 'د سیسټم د شنونکي رول دا دی:')
t.group('list', [
 ('Plan a system flow from the ground up.', 'بنیاد سے نظام کے بہاؤ کی منصوبہ بندی کرنا۔', 'له بنسټه د سیسټم د بهیر پلانول.'),
 ('Interact with customers to learn and document requirements that are then used to produce business requirements documents.', 'گاہکوں سے رابطہ کر کے ضروریات معلوم کرنا اور دستاویز بند کرنا جنھیں بعد میں کاروباری ضروریات کی دستاویزات تیار کرنے کے لیے استعمال کیا جاتا ہے۔', 'له پېرودونکو سره تعامل، څو اړتیاوې زده او ثبت کړي چې بیا د سوداګریزو اړتیاوو د اسنادو د جوړولو لپاره کارول کېږي.'),
 ('Write technical requirements from a critical phase.', 'ایک نازک مرحلے سے تکنیکی ضروریات لکھنا۔', 'له یوه حساس پړاو تخنیکي اړتیاوې لیکل.'),
 ('Interact with designers to understand software limitations.', 'سافٹ ویئر کی حدود سمجھنے کے لیے ڈیزائنرز سے رابطہ کرنا۔', 'د سافټویر د محدودیتونو د پوهېدو لپاره له ډیزاینرانو سره تعامل.'),
 ('Help programmers during system development, e.g. provide use cases, flowcharts or even database design.', 'نظام کی تیاری کے دوران پروگرامرز کی مدد کرنا، مثلاً یوز کیسز، فلو چارٹس یا ڈیٹا بیس ڈیزائن فراہم کرنا۔', 'د سیسټم د جوړولو پر مهال له پروګرام جوړوونکو سره مرسته، لکه د کارونې پېښې، فلوچارټونه یا حتی د ډېټابېس ډیزاین برابرول.'),
 ('Manage system testing.', 'نظام کی جانچ کا انتظام کرنا۔', 'د سیسټم ازموینې اداره کول.'),
 ('Document requirements and contribute to user manuals.', 'ضروریات کی دستاویز بندی کرنا اور صارف کی ہدایت ناموں میں حصہ ڈالنا۔', 'اړتیاوې ثبتول او د کاروونکي لارښوونو کې برخه اخیستل.')])
rec = BOOK.record(t, 'cs12-u2-text-9', 'Unit 2 text (9)', 'یونٹ 2 — متن (۹)', '۲ څپرکی — متن (۹)', 30, [48, 49])
issues = [{'id': 'cs12-pdf030', 'unit': 2, 'printedPage': 49,
           'description': 'p.49 prints “a professional … that studies” and “Write technical requirements from a critical phase”; retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(30, [(2, rec)], issues=issues)
