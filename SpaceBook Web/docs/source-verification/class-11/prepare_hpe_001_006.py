from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); the watermark "awaz e inqilab.com" and the "NOT FOR SALE" footer strip are excluded. Photographs are not reproduced.'
# scan 1 cover
s=page(1,'front-matter','','Front cover','سرورق','پوښ','cover')
F=Flow(s)
H(s,'صحت و جسمانی تعلیم','Health and Physical Education','روغتیا او فزیکي زده‌کړه')
P(s,[('برائے گیارھویں جماعت','For Eleventh Class','د یولسم ټولګي لپاره'),
('FREE FROM GOVERMENT — NOT FOR SALE','FREE FROM GOVERMENT — NOT FOR SALE (spelling as printed)','FREE FROM GOVERMENT — NOT FOR SALE (لکه څنګه چې چاپ شوی)',GAP('Printed misspelling “GOVERMENT” kept; the cover photographs of sports (tennis, badminton, basketball, swimming, running, football) are not reproduced.')),
('خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Khyber Pakhtunkhwa Textbook Board, Peshawar','خیبر پښتونخوا ټیکسټ بک بورډ، پېښور')])
F.done()
s['sourceNote']='Front cover: title, class, board name and the "free from government / not for sale" line.'+NOTE
s['vocabulary']={}
save(s)
# scan 2 title page (i)
s=page(2,'front-matter','i','Title page','عنوانی صفحہ','سرلیک پاڼه','title')
F=Flow(s)
H(s,'صحت و جسمانی تعلیم','Health and Physical Education','روغتیا او فزیکي زده‌کړه')
P(s,[('برائے گیارھویں جماعت','For Eleventh Class','د یولسم ټولګي لپاره'),
('خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Khyber Pakhtunkhwa Textbook Board, Peshawar','خیبر پښتونخوا ټیکسټ بک بورډ، پېښور',GAP('The board’s emblem (Khyber Pakhtunkhwa Textbook Board) is not reproduced.'))])
F.done()
s['sourceNote']='Printed page (i): title page with the board emblem.'+NOTE
s['vocabulary']={}
save(s)
# scan 3 imprint (ii)
s=page(3,'front-matter','ii','Imprint, approval and credits','حقوق، منظوری اور اعترافات','حقونه، منظوري او منندوی','imprint')
F=Flow(s)
P(s,[('جملہ حقوق بحق یونیورسٹی بک پبلشرز، پشاور محفوظ ہیں۔','All rights are reserved by University Book Publishers, Peshawar.','ټول حقونه د یونیورسټي بک پبلشرز، پېښور سره خوندي دي.'),
('منظور کردہ: نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا، ایبٹ آباد','Approved by: Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','منظور شوی: د نصاب او د ښوونکو زده‌کړې رګنۍ، خیبر پښتونخوا، ابټ اباد'),
('مراسلہ نمبر: 6343-46/F.03/Vol-I/HPE-XI(UBP) مورخہ: 28-11-2018','Letter No.: 6343-46/F.03/Vol-I/HPE-XI(UBP), dated 28-11-2018','مراسله نمبر: 6343-46/F.03/Vol-I/HPE-XI(UBP) نېټه: 28-11-2018')])
H(s,'مصنفین','Authors','لیکوالان')
P(s,[('ملک آصف، سابقہ چیئرمین ہیلتھ اینڈ فیزیکل ایجوکیشن ڈیپارٹمنٹ، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد','Malik Asif, former Chairman, Health and Physical Education Department, Government Post Graduate College No. 1, Abbottabad','ملک آصف، پخوانی رییس، د روغتیا او فزیکي زده‌کړې څانګه، دولتي پوسټ ګریجویټ کالج نمبر ۱، ابټ اباد',dict(listGroup='au')),
('رشید اللہ، لیکچرر، گورنمنٹ کالج شیروان، ایبٹ آباد','Rashidullah, Lecturer, Government College Sherwan, Abbottabad','رشیدالله، لیکچرر، دولتي کالج شېروان، ابټ اباد',dict(listGroup='au')),
('سمیع اللہ مروت، (DPE) گورنمنٹ ہائیر سیکنڈری سکول نواں شہر، ایبٹ آباد','Samiullah Marwat, (DPE) Government Higher Secondary School Nawan Shehr, Abbottabad','سمیع الله مروت، (DPE) دولتي لوړ ثانوي ښوونځی نوی ښار، ابټ اباد',dict(listGroup='au')),
('عارف علی شاہ، چیئرمین ہیلتھ اینڈ فیزیکل ایجوکیشن ڈیپارٹمنٹ، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد','Arif Ali Shah, Chairman, Health and Physical Education Department, Government Post Graduate College No. 1, Abbottabad','عارف علي شاه، رییس، د روغتیا او فزیکي زده‌کړې څانګه، دولتي پوسټ ګریجویټ کالج نمبر ۱، ابټ اباد',dict(listGroup='au'))])
P(s,[('زیرِ سرپرستی: گوہر علی خان، ناظم نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا، ایبٹ آباد','Under the patronage of: Gohar Ali Khan, Director, Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','تر سرپرستۍ لاندې: ګوهر علي خان، رییس، د نصاب او د ښوونکو زده‌کړې رګنۍ، خیبر پښتونخوا، ابټ اباد'),
('فوکل پرسن: ذوالفقار خان، ایڈیشنل ڈائریکٹر (نصاب و نظرثانی کتب) نظامت نصاب و تعلیم اساتذہ ایبٹ آباد خیبر پختونخوا','Focal person: Zulfiqar Khan, Additional Director (Curriculum and Book Review), Directorate of Curriculum and Teacher Education, Abbottabad, Khyber Pakhtunkhwa','فوکل پرسن: ذوالفقار خان، اضافي رییس (نصاب او د کتابونو بیاکتنه)، د نصاب او د ښوونکو زده‌کړې رګنۍ، ابټ اباد، خیبر پښتونخوا')])
H(s,'نظرِ ثانی','Reviewers','بیاکتونکي')
P(s,[('نگہت سیما کاکاخیل، SIPE، گورنمنٹ گرلز ہائیر سیکنڈری سکول، کالو خان صوابی','Nighat Seema Kakakhel, SIPE, Government Girls Higher Secondary School, Kalu Khan, Swabi','نګهت سیما کاکاخېل، SIPE، دولتي نجونو لوړ ثانوي ښوونځی، کالو خان صوابۍ',dict(listGroup='rv')),
('محمد ندیم، لیکچرر HPE، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد','Muhammad Nadeem, Lecturer HPE, Government Post Graduate College No. 1, Abbottabad','محمد ندیم، لیکچرر HPE، دولتي پوسټ ګریجویټ کالج نمبر ۱، ابټ اباد',dict(listGroup='rv')),
('محمد صابر، SIPE، گورنمنٹ ہائی سکول ہرنو، ایبٹ آباد','Muhammad Sabir, SIPE, Government High School Harno, Abbottabad','محمد صابر، SIPE، دولتي عالي ښوونځی هرنو، ابټ اباد',dict(listGroup='rv')),
('سمیع اللہ، ڈیسک آفیسر، نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا، ایبٹ آباد','Samiullah, Desk Officer, Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','سمیع الله، ډیسک افسر، د نصاب او د ښوونکو زده‌کړې رګنۍ، خیبر پښتونخوا، ابټ اباد',dict(listGroup='rv')),
('محمد الیاس، ماہر مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Muhammad Ilyas, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar','محمد الیاس، د مضمون ماهر، خیبر پښتونخوا ټیکسټ بک بورډ، پېښور',dict(listGroup='rv'))])
P(s,[('ایڈیٹر: محمد الیاس، ماہر مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Editor: Muhammad Ilyas, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar','مدیر: محمد الیاس، د مضمون ماهر، خیبر پښتونخوا ټیکسټ بک بورډ، پېښور'),
('طباعت زیرِ نگرانی: رشید خان پائندہ خیل (چیئرمین)؛ سعید الرحمٰن، ممبر (ای اینڈ ڈی)','Printing under supervision of: Rashid Khan Pindakhel (Chairman); Saeed-ur-Rahman, Member (E&D)','چاپ تر څارنې لاندې: رشید خان پاینده‌خېل (رییس)؛ سعید الرحمن، غړی (E&D)'),
('خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — تعلیمی سال: 22-2021','Khyber Pakhtunkhwa Textbook Board, Peshawar — academic year 2021-22','خیبر پښتونخوا ټیکسټ بک بورډ، پېښور — تعلیمي کال: 2021-22'),
('ویب سائٹ: www.kptbb.gov.pk — ای میل: membertbb@yahoo.com — فون نمبر: 091-9217159-60','Website: www.kptbb.gov.pk — Email: membertbb@yahoo.com — Phone: 091-9217159-60','ویب پاڼه: www.kptbb.gov.pk — بریښنالیک: membertbb@yahoo.com — تلیفون: 091-9217159-60')])
F.done()
s['sourceNote']='Printed page (ii): rights, approval, authors, reviewers, editor, printing and contact details. The “DPE” and “SIPE” abbreviations are printed in Latin letters; the scan reads “نمبر ایبٹ آباد” for “نمبر 1” in two author lines (number 1 restored from the reviewers line).'+NOTE
s['vocabulary']={}
save(s)
# scan 4 contents (iii)
s=page(4,'front-matter','iii','Table of contents','فہرستِ مضامین','د مضامینو فهرست','contents')
F=Flow(s)
H(s,'فہرستِ مضامین','Table of Contents','د مضامینو فهرست')
P(s,[('باب نمبر — عنوانات — صفحہ نمبر','Chapter number — Titles — Page number','د څپرکي شمېره — سرلیکونه — د پاڼې شمېره'),
('1۔ غیر متعدی امراض — صفحہ 1','1. Non-Communicable Diseases — page 1','۱. غیر ساري ناروغۍ — پاڼه ۱',dict(listGroup='toc')),
('2۔ نظامِ تنفس اور ورزش — صفحہ 15','2. Respiratory System and Exercise — page 15','۲. تنفسي نظام او تمرین — پاڼه ۱۵',dict(listGroup='toc')),
('3۔ منشیات — صفحہ 21','3. Narcotics — page 21','۳. نشه‌یي توکي — پاڼه ۲۱',dict(listGroup='toc')),
('4۔ ہنگامی صورتِ حال — صفحہ 29','4. Emergency Situations — page 29','۴. بېړني حالتونه — پاڼه ۲۹',dict(listGroup='toc')),
('5۔ کھیلوں کے لیے بائیو میکینکس — صفحہ 38','5. Biomechanics for Sports — page 38','۵. د لوبو لپاره بایومیکانیکس — پاڼه ۳۸',dict(listGroup='toc')),
('6۔ فٹنس پلان — صفحہ 54','6. Fitness Plan — page 54','۶. د فټنس پلان — پاڼه ۵۴',dict(listGroup='toc')),
('7۔ کھیلوں کے قوانین اور مہارتیں — صفحہ 60','7. Rules and Skills of Sports — page 60','۷. د لوبو قوانین او مهارتونه — پاڼه ۶۰',dict(listGroup='toc',sourceGap=dict(note='A photograph of sports equipment at the foot of the page is not reproduced.')))])
F.done()
s['sourceNote']='Printed page (iii): table of contents with chapter numbers, titles and starting pages (Chapter 1 starts at printed page 1, i.e. the introduction page).'+NOTE
s['vocabulary']={}
save(s)
# scan 5 intro (printed 1)
s=page(5,'u00','1','Physical Education: Introduction','جسمانی تعلیم: تعارف','فزیکي زده‌کړه: پېژندنه','intro')
F=Flow(s)
H(s,'جسمانی تعلیم — تعارف','Physical Education — Introduction','فزیکي زده‌کړه — پېژندنه')
P(s,[('قدیم زمانے میں جسمانی سرگرمیاں مخصوص مقاصد کے لیے کی جاتی تھیں۔ شروع شروع میں انسان اپنی بقاء، حصولِ رزق اور پُر خطر ماحول سے بچاؤ کے لیے جسمانی قوت کو سب سے اہم سمجھتا تھا اور اس مقصد کے لیے وہ مختلف قسم کی جسمانی سرگرمیاں کرتا تھا۔ اب خوراک حاصل کرنے میں زیادہ دشواری پیش نہیں آتی، وحشی جانوروں کے خطرات بھی کم ہوتے ہیں۔ جنگیں بھی خود کار ہتھیاروں سے لڑی جاتی ہیں۔ معاشرے نے شہریت کے سلسلے میں بین الاقوامی قوانین وضع کر لیے ہیں۔','In ancient times physical activities were performed for specific purposes. In the beginning man considered physical strength most important for his survival, obtaining food and protection from a dangerous environment, and for this purpose he performed various kinds of physical activities. Now there is not much difficulty in obtaining food, and the dangers from wild animals are also fewer. Wars too are fought with automatic weapons. Society has framed international laws concerning citizenship.','په زړو زمانو کې فزیکي فعالیتونه د ځانګړو موخو لپاره کېدل. په پیل کې انسان د خپلې ژوندیتوب، د روزۍ ترلاسه کولو او له خطرناک چاپېریال نه د ژغورنې لپاره فزیکي ځواک تر ټولو مهم ګڼلو او دې موخې لپاره یې بېلابېل ډوله فزیکي فعالیتونه کول. اوس د خوړو په ترلاسه کولو کې ډېره ستونزه نه راځي، د وحشي څارویو خطرونه هم کم دي. جګړې هم په خپلکاره وسلو کېږي. ټولنې د اتباعو په اړه نړیوال قوانین جوړ کړي دي.'),
('دورِ جدید میں جسمانی تعلیم کی اہمیت اور بڑھ گئی ہے۔ انسانوں کا کام خود کار مشینی آلات نے لے لیا ہے۔ سنیما، ٹیلی ویژن، موٹر کار کی سواری، کمپیوٹر اور مختلف قسم کی جدید آسائشوں نے آج کے انسان کو جسمانی سرگرمیوں سے دور کر دیا ہے۔ جس کی وجہ سے جرائم، ذہنی دباؤ اور مختلف بیماریاں انسانوں پر حاوی ہو رہی ہیں۔ جسمانی تعلیم بیک وقت سائنس بھی ہے اور فن بھی۔ حرکت کے قوانین، جسمانی اعضا کے فعل اور ان کے ردِ عمل کے اثرات جسمانی تعلیم کو سائنس کا درجہ دیتے ہیں اور کھیل، جمناسٹک اور حرکات کا ماہرانہ عمل اسے فن کا درجہ دیتے ہیں۔ ضرورت اس بات کی ہے کہ طلبہ کو جسمانی سرگرمیوں میں مہارت، اعضاء اور پٹھوں کی صحت مندانہ افعال، بیماریوں سے بچاؤ، درست قامت اور تفریحی سرگرمیوں کی اہمیت ذہن نشین کرائی جائے۔','In the modern age the importance of physical education has increased further. Automatic mechanical devices have taken over the work of human beings. Cinema, television, travel by motor car, the computer and various kinds of modern comforts have drawn today’s man away from physical activity, because of which crime, mental stress and various diseases are overpowering human beings. Physical education is at once a science and an art. The laws of motion, the functions of bodily organs and the effects of their reactions give physical education the status of science, and the skilled practice of sports, gymnastics and movements gives it the status of art. What is needed is that students be made to understand the importance of skill in physical activities, healthy functions of organs and muscles, prevention of diseases, correct posture and recreational activities.','په نوې دوره کې د فزیکي زده‌کړې اهمیت نور هم زیات شوی. د انسانانو کار خپلکاره ماشیني وسایلو اخیستی. سینما، ټلویزیون، موټر سورلي، کمپیوټر او بېلابېلو نویو آرامیو نن ورځ انسان له فزیکي فعالیتونو لرې کړی، چې له امله یې جرمونه، ذهني فشار او بېلابېل ناروغۍ پر انسانانو غالبېږي. فزیکي زده‌کړه په یو وخت کې ساینس هم ده او هنر هم. د حرکت قوانین، د بدن د غړو فعلونه او د هغو د عکس العمل اغېز فزیکي زده‌کړې ته د ساینس درجه ورکوي او د لوبو، جمناسټیک او حرکاتو ماهرانه عمل ورته د هنر درجه ورکوي. اړتیا دا ده چې زده‌کوونکو ته په فزیکي فعالیتونو کې مهارت، د غړو او عضلاتو د سالمو فعلونو، له ناروغیو د ژغورنې، سم قد او تفریحي فعالیتونو اهمیت ذهن‌نشین کړای شي.'),
('مختلف سکالرز نے جسمانی تعلیم کی تعریف کچھ یوں کی ہے۔','Various scholars have defined physical education as follows.','بېلابېلو سکالرانو فزیکي زده‌کړه داسې تعریف کړې ده.'),
('چارلس بچر (Charle Bucher) کے مطابق: “جسمانی تعلیم مکمل تعلیمی عمل کا جزوِ کامل ہے اور یہ وہ میدان ہے جس کا دائرہ کار وہ خاص جسمانی سرگرمیاں ہیں جو اس مقصد کے لیے منتخب کی گئی ہیں اور جو جسمانی، ذہنی، جذباتی اور سماجی طور پر صحت مند شہری بنانے میں مدد و معاون ثابت ہوں۔”','According to Charles Bucher (“Charle Bucher” as printed): “Physical education is an integral part of the total educational process, and it is the field whose scope is those particular physical activities chosen for this purpose which prove helpful in making healthy citizens physically, mentally, emotionally and socially.”','د چارلس بچر (Charle Bucher) په وینا: “فزیکي زده‌کړه د بشپړ تعلیمي بهیر بشپړ جز دی او دا هغه میدان دی چې د کار دایره یې هغه ځانګړي فزیکي فعالیتونه دي چې د دې موخې لپاره ټاکل شوي او چې فزیکي، ذهني، احساساتي او ټولنیز ډول روغ اتباع جوړولو کې مرسته‌کوونکي ثابت شي.”',dict(listGroup='df')),
('اسی طرح جان ڈیوی (John Dewey) کے مطابق: “جسمانی تعلیم ایسی منتخب سرگرمیوں پر عمل کرنا ہے جن سے انسانی طرزِ عمل کے بنانے، بالیدگی اور ذہنی نشوونما کے تقاضے پورے ہوتے ہیں۔”','In the same way, according to John Dewey: “Physical education is acting on such selected activities by which the requirements of forming human conduct, growth and mental development are fulfilled.”','همداسې د جان ډیوي (John Dewey) په وینا: “فزیکي زده‌کړه پر داسې ټاکل شویو فعالیتونو عمل کول دي چې د انساني چلند جوړولو، وده او ذهني نشوونما غوښتنې پرې پوره کېږي.”',dict(listGroup='df')),
('نکسن کوزن (Nikson Koszen) کے مطابق: “تعلیمِ جسمانی عام تعلیم کا وہ حصہ ہے جو بچوں کو سرگرم جسمانی مشاغل کے ذریعے دی جاتی ہے۔ اس کا تعلق جسمانی سرگرمیوں اور ان سے متعلقہ نتائج اور اثرات سے ہے جو افراد پر واقع ہوتے ہیں۔”','According to Nikson Koszen: “Physical education is that part of general education which is given to children through active physical pursuits. It relates to physical activities and the related results and effects that fall on individuals.”','د نکسن کوزن (Nikson Koszen) په وینا: “فزیکي زده‌کړه د عامې زده‌کړې هغه برخه ده چې ماشومانو ته د فعالو فزیکي مشغولیتونو په مټ ورکول کېږي. د هغې اړیکه له فزیکي فعالیتونو او هغو اړوندو پایلو او اغېزو سره ده چې پر افرادو واقع کېږي.”',dict(listGroup='df'))])
F.done()
s['sourceNote']='Printed page 1: introduction to physical education with three scholars’ definitions. The names are printed as “Charle Bucher”, “John Dewey”, “Nikson Koszen” (spellings kept; the opening “جسمانی تعلیم — تعارف” is the page title).'+NOTE
s['vocabulary']={}
save(s)
# scan 6 chapter 1 opener (printed 2)
s=page(6,'u01','2','Chapter 1: Non-Communicable Diseases — opener','باب نمبر 1: غیر متعدی امراض — آغاز','لومړی څپرکی: غیر ساري ناروغۍ — پیل','ch1-open')
F=Flow(s)
add(s,'bn','Chapter 1','باب نمبر 1','لومړی څپرکی')
H(s,'غیر متعدی امراض (Non Communicable Diseases)','Non-Communicable Diseases','غیر ساري ناروغۍ (Non Communicable Diseases)')
P(s,[('(i) آسٹیوپوروسس (Osteoporosis)','(i) Osteoporosis','(i) اسټیوپوروسیس (Osteoporosis)',dict(listGroup='tp')),
('(ii) دل کے امراض (Heart Diseases)','(ii) Heart Diseases','(ii) د زړه ناروغۍ (Heart Diseases)',dict(listGroup='tp')),
('(iii) ذیابطیس (Diabetes)','(iii) Diabetes','(iii) شکر ناروغي (Diabetes)',dict(listGroup='tp')),
('اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After studying this chapter the students will be able to:','د دې څپرکي له لوستلو وروسته به زده‌کوونکي دې وړ شي چې هغوی:'),
('آسٹیوپوروسس کی علامات اور وجوہات بیان کر سکیں۔','describe the symptoms and causes of osteoporosis.','د اسټیوپوروسیس نښې او لاملونه بیان کړای شي.',dict(listGroup='slo')),
('دل کی بیماریوں کی علامات اور وجوہات بیان کر سکیں۔','describe the symptoms and causes of heart diseases.','د زړه د ناروغیو نښې او لاملونه بیان کړای شي.',dict(listGroup='slo')),
('ذیابطیس کے مریض پر غذائی پابندیاں بیان کر سکیں۔','describe the dietary restrictions on a diabetic patient.','د شکر ناروغ لپاره غذايي بندیزونه بیان کړای شي.',dict(listGroup='slo')),
('ذیابطیس کے مریض کے لیے خوراک کا پلان بنا سکیں۔','make a diet plan for a diabetic patient.','د شکر ناروغ لپاره د خوړو پلان جوړ کړای شي.',dict(listGroup='slo',sourceGap=dict(note='Two photographs at the foot (a man holding his chest with an X-ray of the heart, and X-ray images of knee bones) are not reproduced.')))])
F.done()
s['sourceNote']='Printed page 2: Chapter 1 opener with the three topics and four student learning outcomes.'+NOTE
s['vocabulary']={}
save(s)
