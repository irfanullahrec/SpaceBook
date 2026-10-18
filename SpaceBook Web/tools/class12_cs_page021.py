"""Computer Science XII PDF21 (spread): p.30 Unit 1 exercise Q3 ix–x, Q4–Q9 (unit 1 complete); p.31 Unit 2 opener — learning outcomes."""
from class12_cs_common import BOOK, Builder

e = Builder()
e.group('lines', [
 ('ix. A process is said to be in ready state if it is waiting for some external event which has not yet been occurred.', 'ix. پراسیس اس وقت تیار حالت میں کہلاتا ہے جب وہ کسی ایسے بیرونی واقعے کا انتظار کر رہا ہو جو ابھی پیش نہیں آیا۔', 'ix. یوه پروسه هغه وخت په چمتو حالت کې ګڼل کېږي چې د کومې بهرنۍ پېښې انتظار باسي چې لا نه ده پېښه شوې.'),
 ('x. Batch processing systems does not support interactivity.', 'x. بیچ پراسیسنگ سسٹم تعامل کی معاونت نہیں کرتے۔', 'x. ډله‌ییز پروسس سیسټمونه د تعامل ملاتړ نه کوي.')])
e.p('Q.4 What is an Operating system? Explain different types of operating systems.', 'سوال 4: آپریٹنگ سسٹم کیا ہے؟ آپریٹنگ سسٹمز کی مختلف اقسام کی وضاحت کریں۔', 'پوښتنه ۴: عملیاتي سیسټم څه دی؟ د عملیاتي سیسټمونو بېلابېل ډولونه تشریح کړئ.')
e.p('Q.5 Differentiate between the following:', 'سوال 5: درج ذیل میں فرق کریں:', 'پوښتنه ۵: د لاندې ترمنځ توپیر وکړئ:')
e.group('lines', [('a) Single-user and Multi-users operating systems', 'a) سنگل یوزر اور ملٹی یوزر آپریٹنگ سسٹم', 'a) یو-کاروونکی او ډېر-کاروونکي عملیاتي سیسټمونه'),
                  ('b) Thread and Process', 'b) تھریڈ اور پراسیس', 'b) تار او پروسه'), ('c) Multiprogramming and Multiprocessing', 'c) ملٹی پروگرامنگ اور ملٹی پروسیسنگ', 'c) څو-پروګرامي او څو-پروسسي کار')])
e.p('Q.6 Define distributed operating system and describe its advantages and disadvantages.', 'سوال 6: ڈسٹری بیوٹڈ آپریٹنگ سسٹم کی تعریف کریں اور اس کے فوائد اور نقصانات بیان کریں۔', 'پوښتنه ۶: وېشل شوی عملیاتي سیسټم تعریف کړئ او ګټې او زیانونه یې بیان کړئ.')
e.p('Q.7 Write short notes on the following.', 'سوال 7: درج ذیل پر مختصر نوٹ لکھیں۔', 'پوښتنه ۷: په لاندې موضوعاتو لنډ یادښتونه ولیکئ.')
e.group('lines', [('a) Different states of a process', 'a) پراسیس کی مختلف حالتیں', 'a) د پروسې بېلابېل حالتونه'), ('b) DOS', 'b) DOS', 'b) DOS'),
                  ('c) Real time processing systems', 'c) ریئل ٹائم پراسیسنگ سسٹمز', 'c) سمدستي پروسس سیسټمونه'), ('d) Embedded operating systems', 'd) ایمبیڈڈ آپریٹنگ سسٹمز', 'd) ننښتي عملیاتي سیسټمونه')])
e.p('Q.8 Describe functions of an operating system.', 'سوال 8: آپریٹنگ سسٹم کے افعال بیان کریں۔', 'پوښتنه ۸: د عملیاتي سیسټم دندې بیان کړئ.')
e.p('Q.9 Compare DOS, Windows and UNIX operating systems.', 'سوال 9: DOS، Windows اور UNIX آپریٹنگ سسٹمز کا موازنہ کریں۔', 'پوښتنه ۹: د DOS، Windows او UNIX عملیاتي سیسټمونو پرتله وکړئ.')
ex = BOOK.record(e, 'cs12-u1-exercise-3', 'Unit 1 exercise (3)', 'یونٹ 1: مشق (۳)', '۱ څپرکی: تمرین (۳)', 21, [30])

t = Builder()
t.p('Unit 2', 'یونٹ 2', '۲ څپرکی')
t.h('SYSTEM DEVELOPMENT LIFE CYCLE', 'سسٹم ڈویلپمنٹ لائف سائیکل', 'د سیسټم د پراختیا د ژوند دوره')
t.h('After the completion of Unit-2, Students will be able to:', 'یونٹ 2 مکمل کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د ۲ څپرکي له بشپړولو وروسته به زده‌کوونکي وکولی شي چې:')
L = lambda rows: t.group('list', rows)
L([('Define a system.', 'سسٹم کی تعریف کر سکیں۔', 'سیسټم تعریف کړي.'),
   ('Explain System Development Life Cycle and its importance.', 'سسٹم ڈویلپمنٹ لائف سائیکل اور اس کی اہمیت کی وضاحت کر سکیں۔', 'د سیسټم د پراختیا د ژوند دوره او اهمیت یې تشریح کړي.'),
   ('Describe objectives of SDLC.', 'ایس ڈی ایل سی کے مقاصد بیان کر سکیں۔', 'د SDLC موخې بیان کړي.'),
   ('Describe stakeholder of SDLC and their roles.', 'ایس ڈی ایل سی کے اسٹیک ہولڈرز اور ان کے کردار بیان کر سکیں۔', 'د SDLC ښکېل اړخونه او رولونه یې بیان کړي.'),
   ('Explain the following phases of SDLC:', 'ایس ڈی ایل سی کے درج ذیل مراحل کی وضاحت کر سکیں:', 'د SDLC لاندې پړاوونه تشریح کړي:')])
L([('Planning', 'منصوبہ بندی', 'پلان جوړونه'), ('Feasibility', 'قابلِ عمل ہونا (فیزیبلٹی)', 'د عملي کېدو وړتیا'), ('Analysis', 'تجزیہ', 'تحلیل'), ('Requirement engineering', 'ریکوائرمنٹ انجینئرنگ', 'د اړتیاوو انجنیري'),
   ('Requirement gathering — Functional requirements; Non-functional requirements', 'ضروریات کی جمع آوری — فعالیاتی ضروریات؛ غیر فعالیاتی ضروریات', 'د اړتیاوو راټولول — دندیزې اړتیاوې؛ نادندیزې اړتیاوې'),
   ('Requirement validation', 'ضروریات کی توثیق', 'د اړتیاوو تایید'), ('Requirement management', 'ضروریات کا انتظام', 'د اړتیاوو اداره'),
   ('Design (algorithm, flowchart and pseudo code)', 'ڈیزائن (الگورتھم، فلو چارٹ اور سوڈو کوڈ)', 'ډیزاین (الګوریتم، د بهیر چارټ او شبه کوډ)'), ('Coding', 'کوڈنگ', 'کوډ لیکنه'),
   ('Testing/verification', 'جانچ/تصدیق', 'ازموینه/تایید'), ('Deployment/implementation', 'تعیناتی/نفاذ', 'ځای پر ځای کول/پلي کول'), ('Maintenance/support', 'دیکھ بھال/معاونت', 'ساتنه/ملاتړ')])
L([('Explain the role of the following in:', 'درج ذیل کے کردار کی وضاحت کر سکیں:', 'د لاندې رول تشریح کړي:')])
L([('Management', 'انتظامیہ', 'مدیریت'), ('Project manager', 'پروجیکٹ مینیجر', 'د پروژې مدیر'), ('System analyst', 'سسٹم اینالسٹ', 'د سیسټم شنونکی'),
   ('Programmer', 'پروگرامر', 'پروګرام جوړوونکی'), ('Software tester', 'سافٹ ویئر ٹیسٹر', 'د سافټویر ازموونکی'), ('Customer', 'گاہک', 'پېرودونکی')])
UT = ('System Development Life Cycle', 'سسٹم ڈویلپمنٹ لائف سائیکل', 'د سیسټم د پراختیا د ژوند دوره')
rec = BOOK.record(t, 'cs12-u2-outcomes', 'Unit 2: learning outcomes', 'یونٹ 2: حاصلاتِ تعلم', '۲ څپرکی: د زده‌کړې پایلې', 21, [31], unit_title=UT)
rec['sourceNote'] = 'Nested bullet levels of the printed outcomes box are flattened.'
issues = [{'id': 'cs12-pdf021', 'unit': 1, 'printedPage': 30, 'description': 'Q3(ix) prints “has not yet been occurred”, Q3(x) “systems does not”. Retained as printed. Owner tick marks excluded.'}]

if __name__ == '__main__':
    BOOK.save(21, [(1, ex), (2, rec)], issues=issues, complete_units=[1])
