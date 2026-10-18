"""Computer Science XII PDF24 (spread): printed pp.36–37 — Fig 2.1 (coded); a. planning phase; b. feasibility (technical, economic, operational)."""
from class12_cs_common import BOOK, Builder
from class12_cs_figs import fig_2_1

t = Builder()
P = t.p
H = t.h
en, ur, ps, ratio = fig_2_1()
t.visual('cs12-fig-2-1', en, ur, ps, ratio)
H('a. Planning phase', 'a. منصوبہ بندی کا مرحلہ', 'a. د پلان جوړونې پړاو')
P('Planning phase is the first phase of System Development Life Cycle. During this phase, the group that is responsible for creating the software system must first determine what the system needs to do for the organization. Often, the planning phase tries to find answers for the questions such as:',
  'منصوبہ بندی کا مرحلہ سسٹم ڈویلپمنٹ لائف سائیکل کا پہلا مرحلہ ہے۔ اس مرحلے میں سافٹ ویئر سسٹم بنانے کے ذمہ دار گروپ کو پہلے یہ طے کرنا ہوتا ہے کہ نظام کو تنظیم کے لیے کیا کرنا ہے۔ اکثر منصوبہ بندی کا مرحلہ درج ذیل جیسے سوالات کے جواب تلاش کرتا ہے:',
  'د پلان جوړونې پړاو د سیسټم د پراختیا د ژوند دورې لومړی پړاو دی. په دې پړاو کې هغه ډله چې د سافټویري سیسټم د جوړولو مسؤوله ده، باید لومړی وټاکي چې سیسټم د سازمان لپاره څه کول پکار دي. ډېری وخت د پلان جوړونې پړاو د لاندې پوښتنو ځوابونه لټوي:')
t.group('list', [('What do we need this system for?', 'ہمیں یہ نظام کس لیے چاہیے؟', 'موږ دې سیسټم ته د څه لپاره اړتیا لرو؟'),
                 ('What the new software system will do for the organization?', 'نیا سافٹ ویئر سسٹم تنظیم کے لیے کیا کرے گا؟', 'نوی سافټویري سیسټم به د سازمان لپاره څه کوي؟'),
                 ('How this new software system will be developed?', 'یہ نیا سافٹ ویئر سسٹم کیسے تیار کیا جائے گا؟', 'دا نوی سافټویري سیسټم به څنګه جوړېږي؟')])
P('In this initial phase of SDLC, all the resources, both human and technology resources are put together and a project plan is devised by the project manager.',
  'SDLC کے اس ابتدائی مرحلے میں تمام وسائل، انسانی اور تکنیکی دونوں، اکٹھے کیے جاتے ہیں اور پروجیکٹ مینیجر منصوبے کا خاکہ تیار کرتا ہے۔',
  'د SDLC په دې لومړني پړاو کې ټولې سرچینې، بشري او تکنالوژیکي دواړه، راټولېږي او د پروژې مدیر د پروژې پلان جوړوي.')
H('Activities of the planning phase', 'منصوبہ بندی کے مرحلے کی سرگرمیاں', 'د پلان جوړونې پړاو فعالیتونه')
t.group('list', [('Define business problem or opportunity', 'کاروباری مسئلہ یا موقع متعین کرنا', 'سوداګریزه ستونزه یا فرصت ټاکل'),
                 ('Define Project Scope and Constraints', 'منصوبے کا دائرہ کار اور پابندیاں متعین کرنا', 'د پروژې ساحه او محدودیتونه ټاکل'),
                 ('Produce detailed project schedule (time) and cost', 'منصوبے کا تفصیلی نظام الاوقات (وقت) اور لاگت تیار کرنا', 'د پروژې مفصل مهالوېش (وخت) او لګښت جوړول'),
                 ('Define project benefits', 'منصوبے کے فوائد متعین کرنا', 'د پروژې ګټې ټاکل'),
                 ('Write a report to management', 'انتظامیہ کے لیے رپورٹ لکھنا', 'مدیریت ته راپور لیکل')])
H('b. Feasibility', 'b. فیزیبلٹی', 'b. د عملي کېدو وړتیا')
P('Analysis and evaluation of a proposed project or system, to determine, whether it is technically, economically and operationally feasible within the estimated cost and time is called feasibility study. Feasibility study is one of the important steps in SDLC. It is divided into:',
  'کسی مجوزہ منصوبے یا نظام کا تجزیہ اور جائزہ، یہ طے کرنے کے لیے کہ آیا وہ تخمینی لاگت اور وقت کے اندر تکنیکی، معاشی اور عملی طور پر قابلِ عمل ہے، فیزیبلٹی اسٹڈی کہلاتا ہے۔ فیزیبلٹی اسٹڈی SDLC کے اہم مراحل میں سے ایک ہے۔ اسے درج ذیل میں تقسیم کیا جاتا ہے:',
  'د یوې وړاندیز شوې پروژې یا سیسټم تحلیل او ارزونه، د دې ټاکلو لپاره چې ایا په اټکل شوي لګښت او وخت کې تخنیکي، اقتصادي او عملیاتي پلوه د عملي کېدو وړ ده که نه، د عملي کېدو وړتیا څېړنه بلل کېږي. دا څېړنه د SDLC له مهمو ګامونو څخه یو دی. په لاندې برخو وېشل کېږي:')
H('i. Technical feasibility', 'i. تکنیکی فیزیبلٹی', 'i. تخنیکي وړتیا')
P('It refers to the technical resources needed for the development of the proposed software system.', 'اس سے مراد مجوزہ سافٹ ویئر سسٹم کی تیاری کے لیے درکار تکنیکی وسائل ہیں۔', 'دا د وړاندیز شوي سافټویري سیسټم د جوړولو لپاره اړینو تخنیکي سرچینو ته اشاره ده.')
H('ii. Economic feasibility', 'ii. معاشی فیزیبلٹی', 'ii. اقتصادي وړتیا')
P('This refers to the cost of the project. Here, it tries to determine; total cost of ownership (TCO), tangible benefits and intangible benefits.', 'اس سے مراد منصوبے کی لاگت ہے۔ یہاں یہ طے کرنے کی کوشش کی جاتی ہے: ملکیت کی کل لاگت (TCO)، ٹھوس فوائد اور غیر ٹھوس فوائد۔', 'دا د پروژې لګښت ته اشاره ده. دلته هڅه کېږي چې وټاکل شي: د ملکیت ټول لګښت (TCO)، محسوسې ګټې او نامحسوسې ګټې.')
H('iii. Operational feasibility', 'iii. عملی فیزیبلٹی', 'iii. عملیاتي وړتیا')
P('In this type of feasibility it is determined that whether the proposed system will be used effectively after it has been developed. It means whether the organization has much experienced personals to operate the system or not?',
  'فیزیبلٹی کی اس قسم میں یہ طے کیا جاتا ہے کہ آیا مجوزہ نظام تیار ہونے کے بعد مؤثر طریقے سے استعمال ہوگا یا نہیں۔ اس کا مطلب ہے کہ آیا تنظیم کے پاس نظام چلانے کے لیے کافی تجربہ کار عملہ ہے یا نہیں؟',
  'په دې ډول وړتیا کې ټاکل کېږي چې ایا وړاندیز شوی سیسټم به له جوړېدو وروسته په اغېزمن ډول وکارول شي. مطلب یې دا دی چې ایا سازمان د سیسټم د چلولو لپاره کافي تجربه‌لرونکي کارکوونکي لري که نه؟')
rec = BOOK.record(t, 'cs12-u2-text-3', 'Unit 2 text (3)', 'یونٹ 2 — متن (۳)', '۲ څپرکی — متن (۳)', 24, [36, 37])
rec['sourceNote'] = 'Figure 2.1 is reproduced as a coded cascade diagram (“Requirement Engineering” shortened in the English box label).'
issues = [{'id': 'cs12-pdf024', 'unit': 2, 'printedPage': 37,
           'description': 'p.37 prints “experienced personals” (for “personnel”) and “determine; total cost”; retained as printed. Owner pen marks in the left margin of p.36 excluded.'}]

if __name__ == '__main__':
    BOOK.save(24, [(2, rec)], issues=issues)
