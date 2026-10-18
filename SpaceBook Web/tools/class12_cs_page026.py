"""Computer Science XII PDF26 (spread): printed pp.40–41 — security requirements (end); non-functional requirements; requirements validation; requirements management; e. design phase."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
t.group('lines', [('Members of the Managers group can enter or approve a request, but not delete requests.', 'مینیجرز گروپ کے اراکین درخواست درج یا منظور کر سکتے ہیں لیکن درخواستیں حذف نہیں کر سکتے۔', 'د مدیرانو د ډلې غړي غوښتنه لیکلی یا تصویبولی شي، خو غوښتنې نه شي ړنګولی.'),
                  ('Members of the Administrators group cannot enter or approve requests, but can delete requests.', 'ایڈمنسٹریٹرز گروپ کے اراکین درخواستیں درج یا منظور نہیں کر سکتے لیکن حذف کر سکتے ہیں۔', 'د مدیرانو (Administrators) د ډلې غړي غوښتنې نه شي لیکلی یا تصویبولی، خو ړنګولی یې شي.')])
P('Non-functional requirements: Non-functional requirements are those requirements which specify criteria for the judgment of the operations of a system. It describes that how well the system performs its duties. Nonfunctional requirements are often called qualities of a system. These requirements depend upon the nature of the software.',
  'غیر فعالیاتی ضروریات: غیر فعالیاتی ضروریات وہ ضروریات ہیں جو نظام کے کاموں کو پرکھنے کے معیار متعین کرتی ہیں۔ یہ بیان کرتی ہیں کہ نظام اپنے فرائض کتنی اچھی طرح انجام دیتا ہے۔ غیر فعالیاتی ضروریات کو اکثر نظام کی خوبیاں کہا جاتا ہے۔ یہ ضروریات سافٹ ویئر کی نوعیت پر منحصر ہوتی ہیں۔',
  'نادندیزې اړتیاوې: نادندیزې اړتیاوې هغه اړتیاوې دي چې د سیسټم د چارو د ارزونې معیارونه ټاکي. دا بیانوي چې سیسټم خپلې دندې څومره ښه ترسره کوي. نادندیزو اړتیاوو ته ډېری وخت د سیسټم ځانګړنې (qualities) ویل کېږي. دا اړتیاوې د سافټویر په ډول پورې اړه لري.')
P('Different types of non-functional requirement are:', 'غیر فعالیاتی ضروریات کی مختلف اقسام یہ ہیں:', 'د نادندیزو اړتیاوو بېلابېل ډولونه دا دي:')
t.group('lines', [(e, u, p) for e, u, p in [
    ('Accessibility Requirements', 'رسائی کی ضروریات', 'د لاسرسي اړتیاوې'), ('Accuracy Requirements', 'درستی کی ضروریات', 'د دقت اړتیاوې'), ('Backup and Recovery Requirements', 'بیک اپ اور بحالی کی ضروریات', 'د بېک‌اپ او بیا راګرځولو اړتیاوې'),
    ('Memory Capacity Requirements', 'میموری کی گنجائش کی ضروریات', 'د حافظې د ظرفیت اړتیاوې'), ('Compatibility Requirements', 'مطابقت کی ضروریات', 'د همغږۍ اړتیاوې'), ('Error-Handling Requirements', 'خرابی سے نمٹنے کی ضروریات', 'د تېروتنو د سمبالښت اړتیاوې'),
    ('Maintainability Requirements', 'دیکھ بھال کی ضروریات', 'د ساتنې وړتیا اړتیاوې'), ('Performance Requirements', 'کارکردگی کی ضروریات', 'د کارکردګۍ اړتیاوې'), ('Security Requirements', 'سلامتی کی ضروریات', 'امنیتي اړتیاوې')]])
H('Requirements validation', 'ضروریات کی توثیق', 'د اړتیاوو تایید')
P('Requirement validation is concerned with examining the requirements to certify that they meet the intentions of the stakeholders, and to ensure that they define the right system, the essence of the agreement and understandings between developer and acquirer about what to build, in a manner that ensures a common understanding across the project team and among the stakeholders. The validation differs from verification in the sense that verification occurs after requirements have been accepted.',
  'ضروریات کی توثیق کا تعلق ضروریات کی جانچ سے ہے تاکہ تصدیق ہو سکے کہ وہ اسٹیک ہولڈرز کے ارادوں کو پورا کرتی ہیں، اور یہ یقینی بنایا جا سکے کہ وہ درست نظام کو متعین کرتی ہیں — یعنی ڈویلپر اور حاصل کنندہ کے درمیان اس بات کے بارے میں معاہدے اور مفاہمت کا خلاصہ کہ کیا بنانا ہے — اس طرح کہ پروجیکٹ ٹیم اور اسٹیک ہولڈرز کے درمیان مشترکہ سمجھ یقینی ہو۔ توثیق تصدیق سے اس لحاظ سے مختلف ہے کہ تصدیق ضروریات قبول ہونے کے بعد ہوتی ہے۔',
  'د اړتیاوو تایید د اړتیاوو له ارزونې سره تړاو لري، څو تصدیق شي چې د ښکېلو اړخونو نیتونه پوره کوي، او ډاډ ترلاسه شي چې سم سیسټم ټاکي — یعنې د جوړوونکي او ترلاسه کوونکي ترمنځ د دې په اړه د تړون او پوهاوي لنډیز چې څه باید جوړ شي — په داسې ډول چې د پروژې په ټیم او ښکېلو اړخونو کې ګډ پوهاوی ډاډمن کړي. تایید (validation) له تصدیق (verification) سره په دې توپیر لري چې تصدیق د اړتیاوو له منلو وروسته کېږي.')
P('In requirements validation, the requirements elicited are reviewed to check that requirements are complete, correct, unambiguous, consistent, prioritized, modifiable, and traceable.',
  'ضروریات کی توثیق میں حاصل شدہ ضروریات کا جائزہ لیا جاتا ہے تاکہ جانچا جا سکے کہ ضروریات مکمل، درست، غیر مبہم، ہم آہنگ، ترجیح یافتہ، قابلِ ترمیم اور قابلِ سراغ ہیں۔',
  'د اړتیاوو په تایید کې راایستل شوې اړتیاوې بیاکتل کېږي، څو وکتل شي چې اړتیاوې بشپړې، سمې، بې‌ابهامه، همغږې، لومړیتوب ورکړل شوې، د بدلون وړ او د تعقیب وړ دي.')
H('Requirements management', 'ضروریات کا انتظام', 'د اړتیاوو اداره')
P('Requirements management is performed to ensure that the software continues to meet the expectations of the acquirer and users. The requirements document should always accurately reflect those expectations, as changes occur, in order to communicate to the development team.',
  'ضروریات کا انتظام اس لیے کیا جاتا ہے کہ یقینی بنایا جا سکے کہ سافٹ ویئر حاصل کنندہ اور صارفین کی توقعات پر پورا اترتا رہے۔ ضروریات کی دستاویز کو تبدیلیاں ہونے پر ہمیشہ ان توقعات کی درست عکاسی کرنی چاہیے تاکہ ڈویلپمنٹ ٹیم کو آگاہ کیا جا سکے۔',
  'د اړتیاوو اداره د دې لپاره کېږي چې ډاډ ترلاسه شي سافټویر د ترلاسه کوونکي او کاروونکو تمې پوره کوي. د اړتیاوو سند باید تل، کله چې بدلونونه راشي، هغه تمې په دقیق ډول منعکس کړي، څو جوړوونکي ټیم ته ورسول شي.')
P('Requirements management, therefore, needs to gather new requirements that arise from changing expectations, new regulations, or other sources of change. It needs to analyze the impact of those changes on the project. The conflicts that arise among the acquirer and the user needs to be addressed and changes should be negotiated and validated before such requirements are added to the baseline.',
  'لہٰذا ضروریات کے انتظام میں بدلتی توقعات، نئے ضوابط یا تبدیلی کے دیگر ذرائع سے پیدا ہونے والی نئی ضروریات جمع کرنا ضروری ہے۔ منصوبے پر ان تبدیلیوں کے اثر کا تجزیہ کرنا ضروری ہے۔ حاصل کنندہ اور صارف کے درمیان پیدا ہونے والے تنازعات کو حل کرنا اور ایسی ضروریات کو بنیادی خاکے (baseline) میں شامل کرنے سے پہلے تبدیلیوں پر گفت و شنید اور ان کی توثیق ضروری ہے۔',
  'نو د اړتیاوو اداره باید هغه نوې اړتیاوې راټولې کړي چې له بدلېدونکو تمو، نویو مقرراتو یا د بدلون له نورو سرچینو راولاړېږي. باید پر پروژه د دې بدلونونو اغېز تحلیل کړي. د ترلاسه کوونکي او کاروونکي ترمنځ راپورته شوې شخړې باید حل شي او بدلونونه باید مخکې له دې چې داسې اړتیاوې اساس‌کرښې (baseline) ته ورزیاتې شي، خبرې او تایید شي.')
H('e. Design phase', 'e. ڈیزائن کا مرحلہ', 'e. د ډیزاین پړاو')
P('During this phase, the system is designed to satisfy the functional requirements identified in the previous phase. Since problems in the design phase can be very expensive to solve in later stages of the software development, therefore, a variety of elements are considered in the design to minimize the risk. These include:',
  'اس مرحلے میں نظام کو پچھلے مرحلے میں نشان زد فعالیاتی ضروریات کو پورا کرنے کے لیے ڈیزائن کیا جاتا ہے۔ چونکہ ڈیزائن کے مرحلے کے مسائل کو سافٹ ویئر کی تیاری کے بعد کے مراحل میں حل کرنا بہت مہنگا ہو سکتا ہے، اس لیے خطرے کو کم سے کم کرنے کے لیے ڈیزائن میں مختلف عناصر کو مدِنظر رکھا جاتا ہے۔ ان میں شامل ہیں:',
  'په دې پړاو کې سیسټم داسې ډیزاینېږي چې په تېر پړاو کې پېژندل شوې دندیزې اړتیاوې پوره کړي. څرنګه چې د ډیزاین د پړاو ستونزې د سافټویر د جوړولو په وروستیو پړاوونو کې حلول ډېر ګران کېدای شي، نو د خطر د کمولو لپاره په ډیزاین کې بېلابېل عناصر په پام کې نیول کېږي. په دې کې شامل دي:')
t.group('list', [('Identifying potential risks and defining mitigating design features.', 'ممکنہ خطرات کی نشاندہی اور ان میں کمی لانے والی ڈیزائن خصوصیات کا تعین۔', 'د احتمالي خطرونو پېژندل او د کموونکو ډیزاین ځانګړنو ټاکل.'),
                 ('Performing a security risk assessment.', 'سلامتی کے خطرے کا جائزہ لینا۔', 'د امنیتي خطر ارزونه ترسره کول.'),
                 ('Developing a conversion plan to migrate current data to the new system.', 'موجودہ ڈیٹا کو نئے نظام میں منتقل کرنے کے لیے تبدیلی کا منصوبہ تیار کرنا۔', 'نوي سیسټم ته د اوسنۍ ډېټا د لېږد لپاره د بدلون پلان جوړول.'),
                 ('Determining the operating environment.', 'آپریٹنگ ماحول کا تعین۔', 'د کار چاپېریال ټاکل.')])
rec = BOOK.record(t, 'cs12-u2-text-5', 'Unit 2 text (5)', 'یونٹ 2 — متن (۵)', '۲ څپرکی — متن (۵)', 26, [40, 41])
rec['sourceNote'] = 'The first two lines continue the security requirements from p.39. The design-phase list continues on p.42 (PDF27).'
issues = [{'id': 'cs12-pdf026', 'unit': 2, 'printedPage': 40,
           'description': 'p.40 prints “It describes that how well”; p.41 prints the heading as “Re quirements management” (stray space) and “conflicts that arise among the acquirer and the user needs”. Retained/normalised. Owner bracket lines around the list on p.40 excluded.'}]

if __name__ == '__main__':
    BOOK.save(26, [(2, rec)], issues=issues)
