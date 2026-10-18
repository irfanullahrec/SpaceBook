"""Computer Science XII PDF31 (spread): printed pp.50–51 — analyst list (end); d. programmer; e. software tester; f. customer."""
from class12_cs_common import BOOK, Builder

t = Builder()
P = t.p
H = t.h
t.group('list', [('Whenever a development process is conducted, the system analyst is responsible for designing components and providing that information to the developer.', 'جب بھی تیاری کا عمل کیا جائے، سسٹم اینالسٹ اجزاء کو ڈیزائن کرنے اور وہ معلومات ڈویلپر کو فراہم کرنے کا ذمہ دار ہوتا ہے۔', 'هر کله چې د جوړولو بهیر ترسره شي، د سیسټم شنونکی د برخو د ډیزاین او جوړوونکي ته د هغو معلوماتو د برابرولو مسؤول وي.')])
H('d. Programmer', 'd. پروگرامر', 'd. پروګرام جوړوونکی')
P('A programmer is a technical person that writes computer programs in computer programming languages to develop software. A programmer writes, tests, debugs, and maintains the detailed instructions that are executed by the computer to perform their functions. Other names for programmer are coder and developer.',
  'پروگرامر ایک تکنیکی شخص ہے جو سافٹ ویئر تیار کرنے کے لیے کمپیوٹر پروگرامنگ زبانوں میں کمپیوٹر پروگرام لکھتا ہے۔ پروگرامر وہ تفصیلی ہدایات لکھتا، جانچتا، ان کی خرابیاں دور کرتا اور انھیں برقرار رکھتا ہے جنھیں کمپیوٹر اپنے افعال انجام دینے کے لیے چلاتا ہے۔ پروگرامر کے دوسرے نام کوڈر اور ڈویلپر ہیں۔',
  'پروګرام جوړوونکی یو تخنیکي کس دی چې د سافټویر د جوړولو لپاره په کمپیوټري پروګرامي ژبو کمپیوټري پروګرامونه لیکي. پروګرام جوړوونکی هغه مفصلې لارښوونې لیکي، ازمویي، تېروتنې یې لرې کوي او ساتي یې چې کمپیوټر یې د خپلو دندو د ترسره کولو لپاره اجرا کوي. د پروګرام جوړوونکي نور نومونه کوډر او جوړوونکی (developer) دي.')
P('The roles of a programmer are:', 'پروگرامر کے کردار یہ ہیں:', 'د پروګرام جوړوونکي رولونه دا دي:')
t.group('list', [
 ('Writing, testing, and maintaining the instructions of computer programs.', 'کمپیوٹر پروگراموں کی ہدایات لکھنا، جانچنا اور برقرار رکھنا۔', 'د کمپیوټري پروګرامونو لارښوونې لیکل، ازمویل او ساتل.'),
 ('Updating, repairing, modifying and expanding existing programs', 'موجودہ پروگراموں کو تازہ کرنا، مرمت کرنا، ترمیم کرنا اور وسعت دینا', 'د شته پروګرامونو تازه کول، ترمیمول، بدلول او پراخول'),
 ('Testing the code by running to ensure its correctness', 'کوڈ کو چلا کر اس کی درستی یقینی بنانے کے لیے جانچنا', 'کوډ د چلولو له لارې ازمویل څو یې سموالی ډاډمن شي'),
 ('Developing new methods and approaches to computer programming', 'کمپیوٹر پروگرامنگ کے نئے طریقے اور انداز تیار کرنا', 'د کمپیوټري پروګرام‌سازۍ نوې طریقې او لارې جوړول'),
 ('Consultancy with outside parties in relation to the construction of computer programming methods and the programs themselves.', 'کمپیوٹر پروگرامنگ کے طریقوں اور خود پروگراموں کی تعمیر کے سلسلے میں بیرونی فریقوں سے مشاورت۔', 'د کمپیوټري پروګرام‌سازۍ د طریقو او پخپله د پروګرامونو د جوړولو په اړه له بهرنیو اړخونو سره مشوره.'),
 ('Supervision of the information systems (in some cases).', 'معلوماتی نظاموں کی نگرانی (بعض صورتوں میں)۔', 'د معلوماتي سیسټمونو څارنه (په ځینو حالاتو کې).'),
 ('Maintenance of computer databases is another type of specific duty which à computer programmer may find himself/herself responsible.', 'کمپیوٹر ڈیٹا بیسز کی دیکھ بھال ایک اور مخصوص فریضہ ہے جس کا ذمہ دار کمپیوٹر پروگرامر خود کو پا سکتا ہے۔', 'د کمپیوټري ډېټابېسونو ساتنه بله ځانګړې دنده ده چې کمپیوټري پروګرام جوړوونکی کېدای شي ځان یې مسؤول ومومي.'),
 ('Preparing graphs, tables and analytical data displays which show the progress of a computer program.', 'گراف، جدولیں اور تجزیاتی ڈیٹا کی نمائشیں تیار کرنا جو کمپیوٹر پروگرام کی پیش رفت ظاہر کریں۔', 'ګرافونه، جدولونه او تحلیلي ډېټا ښودنې چمتو کول چې د کمپیوټري پروګرام پرمختګ ښيي.')])
H('e. Software Tester', 'e. سافٹ ویئر ٹیسٹر', 'e. د سافټویر ازموونکی')
P('A software tester is a computer programmer having specialty in testing the computer programs using different testing techniques. Software tester is responsible for understanding requirements, creating test scenarios, test scripts, preparing test data, executing test scripts and reporting defects and reporting results to test lead.',
  'سافٹ ویئر ٹیسٹر ایک کمپیوٹر پروگرامر ہے جو مختلف جانچ کی تکنیکوں کے ذریعے کمپیوٹر پروگراموں کی جانچ میں مہارت رکھتا ہے۔ سافٹ ویئر ٹیسٹر ضروریات کو سمجھنے، ٹیسٹ منظرنامے اور ٹیسٹ اسکرپٹس بنانے، ٹیسٹ ڈیٹا تیار کرنے، ٹیسٹ اسکرپٹس چلانے اور خامیوں اور نتائج کی رپورٹ ٹیسٹ لیڈ کو دینے کا ذمہ دار ہے۔',
  'د سافټویر ازموونکی یو کمپیوټري پروګرام جوړوونکی دی چې د بېلابېلو ازموینیزو تخنیکونو په کارولو د کمپیوټري پروګرامونو په ازموینه کې ځانګړی مهارت لري. د سافټویر ازموونکی د اړتیاوو د پوهېدو، د ازموینې سناریوګانو او سکریپټونو د جوړولو، د ازموینې ډېټا د چمتو کولو، د سکریپټونو د اجرا او د نیمګړتیاوو او پایلو د ازموینې مشر ته راپور ورکولو مسؤول دی.')
P('The roles of a software tester are:', 'سافٹ ویئر ٹیسٹر کے کردار یہ ہیں:', 'د سافټویر ازموونکي رولونه دا دي:')
t.group('list', [
 ('Create test scenarios, test conditions and expected results and test cases.', 'ٹیسٹ منظرنامے، ٹیسٹ شرائط، متوقع نتائج اور ٹیسٹ کیسز بنانا۔', 'د ازموینې سناریوګانې، شرایط، متوقع پایلې او د ازموینې قضیې جوړول.'),
 ('Run and maintain automated test scripts.', 'خودکار ٹیسٹ اسکرپٹس چلانا اور برقرار رکھنا۔', 'اتوماتیک ازموینیز سکریپټونه چلول او ساتل.'),
 ('Create required test data and maintain common test data sheet of the project.', 'مطلوبہ ٹیسٹ ڈیٹا بنانا اور منصوبے کی مشترکہ ٹیسٹ ڈیٹا شیٹ برقرار رکھنا۔', 'اړینه ازموینیزه ډېټا جوړول او د پروژې ګډه ازموینیزه ډېټا پاڼه ساتل.'),
 ('Create test deliverables as per testing standards followed by the company or project.', 'کمپنی یا منصوبے کے جانچ کے معیار کے مطابق ٹیسٹ کے نتائج (deliverables) تیار کرنا۔', 'د شرکت یا پروژې د ازموینې د معیارونو سره سم د ازموینې وړاندې کېدونکي توکي جوړول.'),
 ('Execute test scripts and document test results.', 'ٹیسٹ اسکرپٹس چلانا اور ٹیسٹ کے نتائج کی دستاویز بندی کرنا۔', 'د ازموینې سکریپټونه اجرا کول او پایلې ثبتول.'),
 ('Inform testing team leader on any issues that could potentially impact quality, schedule or budget of the project.', 'جانچ ٹیم کے سربراہ کو ایسے کسی بھی مسئلے سے آگاہ کرنا جو منصوبے کے معیار، نظام الاوقات یا بجٹ کو متاثر کر سکے۔', 'د ازموینې د ټیم مشر هره هغه ستونزه خبرول چې کېدای شي د پروژې پر کیفیت، مهالوېش یا بودیجه اغېز وکړي.')])
H('f. Customer', 'f. گاہک', 'f. پېرودونکی')
P('A Customer is an individual or an organization that is a current or potential buyer or user of the software product. Customers usually purchase software from software manufacturer companies (software houses), users groups and individuals. Customers are also called clients but the only difference between the two is that the customers purchase the software products and the clients purchase services. Customers are the real evaluators of a software product by using it and identifying its merits and demerits.',
  'گاہک وہ فرد یا تنظیم ہے جو سافٹ ویئر پروڈکٹ کا موجودہ یا ممکنہ خریدار یا صارف ہو۔ گاہک عموماً سافٹ ویئر بنانے والی کمپنیوں (سافٹ ویئر ہاؤسز)، صارفین کے گروپوں اور افراد سے سافٹ ویئر خریدتے ہیں۔ گاہکوں کو کلائنٹس بھی کہا جاتا ہے لیکن دونوں میں صرف یہ فرق ہے کہ گاہک سافٹ ویئر پروڈکٹس خریدتے ہیں اور کلائنٹس خدمات خریدتے ہیں۔ گاہک سافٹ ویئر پروڈکٹ کو استعمال کر کے اور اس کی خوبیاں اور خامیاں پہچان کر اس کے حقیقی جائزہ کار ہوتے ہیں۔',
  'پېرودونکی هغه کس یا سازمان دی چې د سافټویري محصول اوسنی یا احتمالي پېرودونکی یا کاروونکی وي. پېرودونکي عموماً له سافټویر جوړوونکو شرکتونو (سافټویر هاوسونو)، د کاروونکو له ډلو او کسانو سافټویر اخلي. پېرودونکو ته پېرېدونکي (clients) هم ویل کېږي، خو د دواړو یوازینی توپیر دا دی چې پېرودونکي سافټویري محصولات اخلي او پېرېدونکي خدمتونه اخلي. پېرودونکي د سافټویري محصول په کارولو او د ښېګڼو او نیمګړتیاوو په پېژندو سره یې رښتیني ارزوونکي دي.')
rec = BOOK.record(t, 'cs12-u2-text-10', 'Unit 2 text (10)', 'یونٹ 2 — متن (۱۰)', '۲ څپرکی — متن (۱۰)', 31, [50, 51])
rec['sourceNote'] = 'The first item continues the analyst list from p.49. The rest of p.51 is blank in print.'
issues = [{'id': 'cs12-pdf031', 'unit': 2, 'printedPage': 50,
           'description': 'p.50 prints “which à computer programmer may find himself/herself responsible” (stray accented “à” for “a”) and “a technical person that writes”; retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(31, [(2, rec)], issues=issues)
