"""Computer Science XII PDF23 (spread): printed pp.34–35 — objectives (end); 2.1.4 stakeholders; role of stakeholders; 2.1.5 SDLC phases list."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
t.group('list', [
 ('One of the major objectives of SDLC is to establish an appropriate level of management authority to direct, coordinate, control, review, and approve the software development project.', 'SDLC کے بڑے مقاصد میں سے ایک سافٹ ویئر کی تیاری کے منصوبے کی رہنمائی، ہم آہنگی، کنٹرول، جائزہ اور منظوری کے لیے انتظامی اختیار کی مناسب سطح قائم کرنا ہے۔', 'د SDLC له لویو موخو څخه یوه د سافټویر د جوړولو د پروژې د لارښوونې، همغږۍ، کنټرول، بیاکتنې او تصویب لپاره د مدیریتي واک مناسبه کچه ټینګول دي.'),
 ('SDLC should ensure the project management accountability.', 'SDLC کو پروجیکٹ مینجمنٹ کی جواب دہی یقینی بنانی چاہیے۔', 'SDLC باید د پروژې د مدیریت حساب‌ورکونه ډاډمنه کړي.'),
 ('Proper documentation of all the requirements needed for the development of the new software system.', 'نئے سافٹ ویئر سسٹم کی تیاری کے لیے درکار تمام ضروریات کی مناسب دستاویز بندی۔', 'د نوي سافټویري سیسټم د جوړولو لپاره د ټولو اړینو اړتیاوو سم اسناد کول.'),
 ('Ensuring that projects are developed within the current and planned information technology infrastructure.', 'یہ یقینی بنانا کہ منصوبے موجودہ اور منصوبہ بند انفارمیشن ٹیکنالوجی ڈھانچے کے اندر تیار ہوں۔', 'ډاډمنول چې پروژې د اوسنۍ او پلان شوې معلوماتي ټکنالوژۍ د زیربنا دننه جوړېږي.'),
 ('SDLC should identify the potential project risks in advance so that proper planning should be done.', 'SDLC کو منصوبے کے ممکنہ خطرات کی پیشگی نشاندہی کرنی چاہیے تاکہ مناسب منصوبہ بندی کی جا سکے۔', 'SDLC باید د پروژې احتمالي خطرونه مخکې وپېژني څو سم پلان جوړ شي.')])
H('2.1.4 Stakeholders of SDLC', '2.1.4 ایس ڈی ایل سی کے اسٹیک ہولڈرز', '۲.۱.۴ د SDLC ښکېل اړخونه')
P('Those entities which are either within the organization or outside of the organization that sponsor a project, or have an interest or have the intention to get it after its successful completion, or may have a positive or negative influence in the project completion are called stakeholders. Project stakeholders include the customers, the user group, the project manager, the development team and the testers. All those who have some interest in the project can be considered as stakeholders of that project. The individuals as well as the organizations that are actively involved in the project, or whose interests may be affected as a result of project execution or project completion are the part of stakeholders. It is the duty of the project management team to identify the stakeholders, determine their requirements, expectations and manage their influence in relation to the requirements to ensure a successful project.',
  'وہ ادارے جو تنظیم کے اندر یا باہر ہوں، جو کسی منصوبے کی سرپرستی کریں، یا اس میں دلچسپی رکھیں یا اس کی کامیاب تکمیل کے بعد اسے حاصل کرنے کا ارادہ رکھیں، یا منصوبے کی تکمیل پر مثبت یا منفی اثر رکھتے ہوں، اسٹیک ہولڈرز کہلاتے ہیں۔ منصوبے کے اسٹیک ہولڈرز میں گاہک، صارفین کا گروپ، پروجیکٹ مینیجر، ڈویلپمنٹ ٹیم اور ٹیسٹرز شامل ہیں۔ وہ سب جو منصوبے میں کچھ دلچسپی رکھتے ہوں، اس منصوبے کے اسٹیک ہولڈرز سمجھے جا سکتے ہیں۔ وہ افراد اور تنظیمیں جو منصوبے میں فعال طور پر شامل ہوں، یا جن کے مفادات منصوبے کے نفاذ یا تکمیل کے نتیجے میں متاثر ہو سکتے ہوں، اسٹیک ہولڈرز کا حصہ ہیں۔ پروجیکٹ مینجمنٹ ٹیم کا فرض ہے کہ اسٹیک ہولڈرز کی نشاندہی کرے، ان کی ضروریات اور توقعات متعین کرے اور کامیاب منصوبے کو یقینی بنانے کے لیے ضروریات کے حوالے سے ان کے اثر کا انتظام کرے۔',
  'هغه اړخونه چې یا د سازمان دننه وي یا ترې بهر، چې د یوې پروژې ملاتړ کوي، یا پکې لېوالتیا لري یا د بریالي بشپړېدو وروسته یې د ترلاسه کولو اراده لري، یا د پروژې په بشپړېدو مثبت یا منفي اغېز لري، ښکېل اړخونه (stakeholders) بلل کېږي. د پروژې ښکېل اړخونه پېرودونکي، د کاروونکو ډله، د پروژې مدیر، جوړوونکی ټیم او ازموونکي رانغاړي. ټول هغه کسان چې په پروژه کې یو څه لېوالتیا لري، د هغې پروژې ښکېل اړخونه ګڼل کېدای شي. هغه کسان او سازمانونه چې په پروژه کې فعال ښکېل وي، یا ګټې یې د پروژې د اجرا یا بشپړېدو په پایله کې اغېزمنېدای شي، د ښکېلو اړخونو برخه دي. د پروژې د مدیریت ټیم دنده ده چې ښکېل اړخونه وپېژني، اړتیاوې او تمې یې وټاکي او د بریالۍ پروژې د ډاډمنولو لپاره د اړتیاوو په اړه د هغوی اغېز اداره کړي.')
H('Role of stakeholders', 'اسٹیک ہولڈرز کا کردار', 'د ښکېلو اړخونو رول')
P('The basic roles of the stakeholders are:', 'اسٹیک ہولڈرز کے بنیادی کردار یہ ہیں:', 'د ښکېلو اړخونو بنسټیز رولونه دا دي:')
t.group('list', [
 ('For the development of a software system, resources such as time, money, equipment etc. are needed which should be provided to the project team by the stakeholders.', 'سافٹ ویئر سسٹم کی تیاری کے لیے وقت، رقم، آلات وغیرہ جیسے وسائل درکار ہوتے ہیں جو اسٹیک ہولڈرز کو پروجیکٹ ٹیم کو فراہم کرنے چاہییں۔', 'د سافټویري سیسټم د جوړولو لپاره سرچینې لکه وخت، پیسې، وسایل او نور اړین وي چې باید ښکېل اړخونه یې د پروژې ټیم ته برابر کړي.'),
 ('Stakeholders educate the developers about their business.', 'اسٹیک ہولڈرز ڈویلپرز کو اپنے کاروبار کے بارے میں آگاہ کرتے ہیں۔', 'ښکېل اړخونه جوړوونکي له خپلې سوداګرۍ خبروي.'),
 ('They spend more time to provide information and clarify requirements to the analysts and developers.', 'وہ تجزیہ کاروں اور ڈویلپرز کو معلومات فراہم کرنے اور ضروریات واضح کرنے میں زیادہ وقت صرف کرتے ہیں۔', 'دوی شنونکو او جوړوونکو ته د معلوماتو برابرولو او د اړتیاوو روښانه کولو لپاره ډېر وخت لګوي.'),
 ('The stakeholders should be specific and precise about the requirements.', 'اسٹیک ہولڈرز کو ضروریات کے بارے میں مخصوص اور درست ہونا چاہیے۔', 'ښکېل اړخونه باید د اړتیاوو په اړه ځانګړي او دقیق وي.'),
 ('Make timely decisions.', 'بروقت فیصلے کرنا۔', 'په وخت پرېکړې کول.'),
 ('Respect a developer’s assessment of cost and feasibility.', 'لاگت اور قابلِ عمل ہونے کے بارے میں ڈویلپر کے اندازے کا احترام کرنا۔', 'د لګښت او عملي کېدو په اړه د جوړوونکي ارزونې ته درناوی.'),
 ('Set requirement priorities.', 'ضروریات کی ترجیحات مقرر کرنا۔', 'د اړتیاوو لومړیتوبونه ټاکل.'),
 ('Review and provide timely feedback.', 'جائزہ لینا اور بروقت رائے دینا۔', 'بیاکتنه او په وخت غبرګون ورکول.'),
 ('Promptly communicate changes to requirements.', 'ضروریات میں تبدیلیوں سے فوراً آگاہ کرنا۔', 'په اړتیاوو کې بدلونونه سمدستي خبرول.')])
H('2.1.5 System development life cycle phases', '2.1.5 سسٹم ڈویلپمنٹ لائف سائیکل کے مراحل', '۲.۱.۵ د سیسټم د پراختیا د ژوند دورې پړاوونه')
P('The most commonly used phases of SDLC are given below.', 'SDLC کے سب سے زیادہ استعمال ہونے والے مراحل ذیل میں دیے گئے ہیں۔', 'د SDLC تر ټولو ډېر کارېدونکي پړاوونه لاندې ورکړل شوي.')
t.group('list', [('Planning', 'منصوبہ بندی', 'پلان جوړونه'), ('Feasibility Study', 'فیزیبلٹی اسٹڈی', 'د عملي کېدو وړتیا څېړنه'), ('Analysis', 'تجزیہ', 'تحلیل'),
                 ('Requirement Engineering', 'ریکوائرمنٹ انجینئرنگ', 'د اړتیاوو انجنیري'), ('Design', 'ڈیزائن', 'ډیزاین'), ('Coding', 'کوڈنگ', 'کوډ لیکنه'),
                 ('Testing / Verification', 'جانچ / تصدیق', 'ازموینه / تایید'), ('Deployment / Implementation', 'تعیناتی / نفاذ', 'ځای پر ځای کول / پلي کول'), ('Maintenance / Support', 'دیکھ بھال / معاونت', 'ساتنه / ملاتړ')])
P('These phases are diagrammatically shown in Figure 2.1.', 'یہ مراحل شکل 2.1 میں تصویری طور پر دکھائے گئے ہیں۔', 'دا پړاوونه په ۲.۱ شکل کې په انځوري ډول ښودل شوي.')
rec = BOOK.record(t, 'cs12-u2-text-2', 'Unit 2 text (2)', 'یونٹ 2 — متن (۲)', '۲ څپرکی — متن (۲)', 23, [34, 35])
rec['sourceNote'] = 'The first list continues the objectives from p.33.'
issues = [{'id': 'cs12-pdf023', 'unit': 2, 'printedPage': 34,
           'description': 'Heavy owner handwriting (names in the left margin of p.34, pen curves on p.35) excluded. p.34 “should be done” lacks a final full stop in print.'}]

if __name__ == '__main__':
    BOOK.save(23, [(2, rec)], issues=issues)
