from statlib import *
c=cell
FM='front-matter'
# ---------- scan 1: front cover ----------
s=page(1,FM,None,'Front cover','سرورق','مخپاڼه','cover',layout='cover')
add(s,'t','Statistics','شماریات','احصایه',kind='heading')
add(s,'sub','A Textbook for','ایک درسی کتاب برائے','یو درسي کتاب د',)
add(s,'g','Grade XI','جماعت یازدہم','یوولسم ټولګی')
add(s,'stamp','FREE FORM GOVERNMENT NOT FOR SALE','حکومت کی طرف سے مفت، فروخت کے لیے نہیں','د حکومت لخوا وړیا، د پلور لپاره نه دی')
add(s,'pub','Khyber Pakhtunkhwa Textbook Board Peshawar','خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','د خیبر پښتونخوا درسي کتابونو بورډ پېښور')
F=Flow(s);F.done()
s['sourceNote']='Front cover. The diagonal red stamp prints "FREE FORM GOVERNMENT NOT FOR SALE" ("FORM" as printed). Excluded as decorative or noninstructional: the cover montage (people building a bar chart, arrow chart, globe, pen), the board emblem, and the website watermark "awaz e inqilab.com" applied to every scan.'
s['vocabulary']={}
save(s)
# ---------- scan 4: Quran verse and hadith (Urdu source) ----------
s=page(4,FM,None,'Quranic verse and Hadith (source in Urdu)','قرآنی آیت اور حدیث','قرآني آیت او حدیث','verses',layout='cover')
add(s,'v1','مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تا کہ تم پر رحم کیا جائے۔','مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تا کہ تم پر رحم کیا جائے۔','مومنان خو یو له بل سره وروڼه دي. نو خپل دوه وروڼو ترمنځ سوله وکړئ او له الله څخه ویره ولرئ ترڅو په تاسو رحم وشي.')
add(s,'v1r','(سورۃ الحجرات: ۱۰)','(سورۃ الحجرات: ۱۰)','(سورة الحجرات: ۱۰)')
add(s,'v2','ایک مسلمان کی جان، مال اور عزت دوسرے مسلمان پر حرام ہے۔','ایک مسلمان کی جان، مال اور عزت دوسرے مسلمان پر حرام ہے۔','د یو مسلمان ژوند، مال او عزت پر بل مسلمان حرام دی.')
F=Flow(s);F.done()
s['sourceNote']='Source text is Urdu (original kept in the original slot; the Urdu field repeats the original). English meaning for reference: "The believers are but brothers, so make settlement between your brothers and fear Allah so that you may receive mercy" (Surah Al-Hujurat 49:10); "The life, property and honour of a Muslim are forbidden to another Muslim." The ornamental flower borders are decorative and excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 5: title page ----------
s=page(5,FM,'i','Title page','عنوان کا صفحہ','د سرلیک پاڼه','title',layout='cover')
add(s,'t','Statistics','شماریات','احصایه',kind='heading')
add(s,'sub','A Textbook for','ایک درسی کتاب برائے','یو درسي کتاب د')
add(s,'g','GRADE XI','جماعت یازدہم','یوولسم ټولګی')
add(s,'pub','KHYBER PAKHTUNKHWA TEXTBOOK BOARD PESHAWAR','خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','د خیبر پښتونخوا درسي کتابونو بورډ پېښور')
add(s,'nfs','NOT FOR SALE','فروخت کے لیے نہیں','د پلور لپاره نه دی')
F=Flow(s);F.done()
s['sourceNote']='Printed folio (i). Excluded as decorative: the bar-chart graphic, the hand-and-pen illustration, the board emblem, and the website watermark.'
s['vocabulary']={}
save(s)
# ---------- scan 6: credits ----------
s=page(6,FM,'ii','Publication details and contributors','اشاعتی تفصیلات اور معاونین','د خپرونې جزئیات او ونډه‌وال','credits',layout='credits')
R=[
('rights','All rights reserved with Leading Books Publishers, (Pvt.) Ltd. Peshawar','جملہ حقوق لیڈنگ بکس پبلشرز (پرائیویٹ) لمیٹڈ پشاور کے پاس محفوظ ہیں','ټول حقوق د لیډنګ بوکس پبلشرز (خصوصي) لمیټډ پېښور سره خوندي دي',None),
('h1','Approved by:','منظوری دینے والا ادارہ:','منظوري ورکوونکی:','heading'),
('appr','Directorate of Curriculum & Teacher Education, Abbottabad according to the National Curriculum 2009.','ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن، ایبٹ آباد، قومی نصاب 2009 کے مطابق۔','د نصاب او ښوونکو د روزنې ریاست، اېبټ‌آباد، د 2009 ملي نصاب سره سم.',None),
('noc','NOC No. 9516-18/F.03/Vol-1/Statistics –XI dated 14-12-2017','این او سی نمبر 9516-18/F.03/Vol-1/Statistics –XI مورخہ 14-12-2017','د NOC شمېره 9516-18/F.03/Vol-1/Statistics –XI نېټه 14-12-2017',None),
('h2','Author:','مصنف:','لیکوال:','heading'),
('au','Prof. Jamal Shah, Principal Government Degree College, Zaida Swabi','پروفیسر جمال شاہ، پرنسپل گورنمنٹ ڈگری کالج زیدہ صوابی','پروفیسر جمال شاه، پرنسپال دولتي ډګري کالج زېده صوابۍ',None),
('h3','Review Supervision:','نگرانیِ نظرثانی:','د بیاکتنې څارنه:','heading'),
('rs','Gohar Ali Khan, Director DCTE, Abbottabad.','گوہر علی خان، ڈائریکٹر ڈی سی ٹی ای، ایبٹ آباد۔','ګوهر علي خان، د DCTE رئیس، اېبټ‌آباد.',None),
('h4','Focal person:','فوکل پرسن:','فوکل شخص:','heading'),
('fp','Zulfiqar Khan, Additional Director (Curriculum Wing and Textbook Review), DCTE, Khyber Pakhtunkhwa Abbottabad','ذوالفقار خان، ایڈیشنل ڈائریکٹر (کریکولم ونگ اینڈ ٹیکسٹ بک ریویو)، ڈی سی ٹی ای، خیبر پختونخوا ایبٹ آباد','ذوالفقار خان، اضافي رئیس (د نصاب څانګه او د درسي کتاب بیاکتنه)، DCTE، خیبر پښتونخوا اېبټ‌آباد',None),
('h5','Reviewers:','نظرثانی کنندگان:','بیاکتونکي:','heading'),
('r1','Mr. Zia Shahid, Principal, GHS NO. 3 Abbottabad','جناب ضیاء شاہد، پرنسپل، جی ایچ ایس نمبر 3 ایبٹ آباد','ښاغلی ضیاء شاهد، پرنسپال، GHS نمبر 3 اېبټ‌آباد','rev'),
('r2','Mr. Majid Khan, Assist. Prof. GPGC No.1 , Abbottabad','جناب ماجد خان، اسسٹنٹ پروفیسر، جی پی جی سی نمبر 1، ایبٹ آباد','ښاغلی ماجد خان، مرستیال پروفیسر، GPGC نمبر 1، اېبټ‌آباد','rev'),
('r3','Mr. Iftikhar Hussain, SS, GHSS Nawanshehr, Abbottabad','جناب افتخار حسین، ایس ایس، جی ایچ ایس ایس نوانشہر، ایبٹ آباد','ښاغلی افتخار حسین، SS، GHSS نوانشهر، اېبټ‌آباد','rev'),
('r4','Mr. Abrar Ahmad, SS, DCTE, Abbottabad','جناب ابرار احمد، ایس ایس، ڈی سی ٹی ای، ایبٹ آباد','ښاغلی ابرار احمد، SS، DCTE، اېبټ‌آباد','rev'),
('r5','Dr. Muhammad Shah, Ex-SS, KP Textbook Board, peshawar','ڈاکٹر محمد شاہ، سابق ایس ایس، کے پی ٹیکسٹ بک بورڈ، پشاور','ډاکټر محمد شاه، پخوانی SS، KP د درسي کتابونو بورډ، پېښور','rev'),
('h6','Editor:','مدیر:','سمونګر:','heading'),
('ed','Shakeel Iqbal, SS, KP Textbook Board, Peshawar','شکیل اقبال، ایس ایس، کے پی ٹیکسٹ بک بورڈ، پشاور','شکیل اقبال، SS، KP د درسي کتابونو بورډ، پېښور',None),
('h7','Printing Supervision:','نگرانیِ طباعت:','د چاپ څارنه:','heading'),
('p1','Rasheed Khan PaindaKhel, Chairman','رشید خان پائندہ خیل، چیئرمین','رشید خان پاینده خېل، رئیس','pr'),
('p2','Saeedur Rehman, Member(E&P), KP Textbook Board, Peshawar','سعیدالرحمن، ممبر (ای اینڈ پی)، کے پی ٹیکسٹ بک بورڈ، پشاور','سعیدالرحمن، غړی (E&P)، KP د درسي کتابونو بورډ، پېښور','pr'),
('yr','Academic Year 2021-22','تعلیمی سال 2021-22','تعلیمي کال 2021-22',None),
('web','Website: www.kptbb.gov.pk','ویب سائٹ: www.kptbb.gov.pk','ویب پاڼه: www.kptbb.gov.pk',None),
('em','Email: membertbb@yahoo.com','ای میل: membertbb@yahoo.com','بریښنالیک: membertbb@yahoo.com',None),
('ph','Phone: 091-9217159-60','فون: 091-9217159-60','ټیلیفون: 091-9217159-60',None)]
for k,a,b,c_,t in R:
    if t=='heading': head(s,k,a,b,c_)
    elif t: add(s,k,a,b,c_,listGroup=t)
    else: add(s,k,a,b,c_)
F=Flow(s);F.done()
s['sourceNote']='Printed folio (ii). Printed spellings retained ("peshawar", "GPGC No.1 ,", "PaindaKhel"). The blue header graphics and the website watermark are excluded as noninstructional.'
s['vocabulary']={}
save(s)
# ---------- scan 7: preface ----------
s=page(7,FM,'iii','Preface','پیش لفظ','سريزه','preface',layout='preface')
head(s,'h','PREFACE','پیش لفظ','سريزه')
PF=[
('a','This book is a beginning for the beginners of statistics. For those who know statistics, there is sufficient literature but for new entry in the subject there was a need for an easy book especially in the province of Khyber PakhtunKhwa.','یہ کتاب شماریات کے ابتدائی طلبہ کے لیے ایک آغاز ہے۔ جو لوگ شماریات جانتے ہیں ان کے لیے کافی لٹریچر موجود ہے لیکن اس مضمون میں نئے آنے والوں کے لیے خاص طور پر صوبہ خیبر پختونخوا میں ایک آسان کتاب کی ضرورت تھی۔','دا کتاب د احصایې د پیل کوونکو لپاره یو پیل دی. د هغو کسانو لپاره چې احصایه پېژني کافي ادبیات شته خو په دې مضمون کې د نوي راتلونکو لپاره په ځانګړې توګه په خیبر پښتونخوا ولایت کې یوه اسانه کتاب ته اړتیا وه.'),
('b','This is a text book written strictly according to the National curriculum for statistics grades XI - XII 2009 Government of Pakistan.','یہ ایک درسی کتاب ہے جو حکومتِ پاکستان کے شماریات جماعت یازدہم – دوازدہم 2009 کے قومی نصاب کے عین مطابق لکھی گئی ہے۔','دا یو درسي کتاب دی چې د پاکستان حکومت د احصایې د XI - XII ټولګیو د 2009 ملي نصاب سره په کلکه سم لیکل شوی دی.'),
('c','It gives me great pleasure and satisfaction in presenting the connectivity and simplicity of the book before the intermediate Part-I readers.','مجھے انٹرمیڈیٹ حصہ اول کے قارئین کے سامنے کتاب کی ربط و تسلسل اور سادگی پیش کرتے ہوئے بڑی خوشی اور اطمینان ہو رہا ہے۔','ما ته د انټرمیډیټ لومړي برخې لوستونکو مخې ته د کتاب پیوستون او سادګي وړاندې کولو سره ډېره خوښي او رضایت راکوي.'),
('d','I hope this book will be attractive and fruitful for those who have chosen the subject statistics for the first time including teachers and my dearest students all over the country.','مجھے امید ہے کہ یہ کتاب ان لوگوں کے لیے پرکشش اور مفید ہو گی جنہوں نے پہلی بار شماریات کا مضمون چنا ہے، جن میں اساتذہ اور ملک بھر کے میرے عزیز ترین طلبہ شامل ہیں۔','زه هیله لرم چې دا کتاب به د هغو کسانو لپاره په زړه پورې او ګټور وي چې د لومړي ځل لپاره یې د احصایې مضمون غوره کړی، په شمول د ښوونکو او په ټول هېواد کې زما د ګرانو زده کوونکو.'),
('e','I am thankful to Almighty ALLAH who has given me the thinking capabilities and strength to convert my ideas to the pages.','میں اللہ تعالیٰ کا شکر گزار ہوں جس نے مجھے سوچنے کی صلاحیتیں اور اپنے خیالات کو صفحات پر منتقل کرنے کی طاقت عطا کی۔','زه د الله تعالی منندوی یم چې ما ته یې د فکر کولو وړتیا او د خپلو افکارو پاڼو ته د اړولو ځواک راکړ.'),
('f','May ALLAH reward my student Farooq Ahmad (Lecturer in Statistics), friend Izaz Ali (Professor of Mathematics), the editor and my sons whose, trust, motivation and help made it possible.','اللہ میرے شاگرد فاروق احمد (لیکچرر شماریات)، دوست اعزاز علی (پروفیسر ریاضی)، مدیر اور میرے بیٹوں کو اجر دے جن کے اعتماد، حوصلہ افزائی اور مدد نے اسے ممکن بنایا۔','الله دې زما شاګرد فاروق احمد (د احصایې لیکچرر)، ملګري اعزاز علي (د ریاضي پروفیسر)، سمونګر او زما زامنو ته اجر ورکړي چې باور، هڅونې او مرستې یې دا ممکنه کړه.'),
('g','I pray to ALLAH for making this sincere presentation understandable for everyone.','میں اللہ سے دعا کرتا ہوں کہ وہ اس مخلصانہ پیشکش کو سب کے لیے قابلِ فہم بنا دے۔','زه له الله څخه دعا کوم چې دا مخلصانه وړاندې کول د ټولو لپاره د پوهېدو وړ کړي.'),
('h2','Suggestions for correction and improvement of the book will be highly appreciated.','کتاب کی اصلاح اور بہتری کے لیے تجاویز کی نہایت قدر کی جائے گی۔','د کتاب د سمون او ښه والي لپاره وړاندیزونه به ډېر ستایل کېږي.'),
('sig1','Prof: Jamal Shah','پروفیسر: جمال شاہ','پروفیسر: جمال شاه'),
('sig2','Principal','پرنسپل','پرنسپال'),
('sig3','Government Degree College Zaida Swabi','گورنمنٹ ڈگری کالج زیدہ صوابی','دولتي ډګري کالج زېده صوابۍ')]
for k,a,b,c_ in PF: add(s,k,a,b,c_)
F=Flow(s);F.done()
s['sourceNote']='Printed folio (iii). Printed spellings retained ("PakhtunKhwa", "whose, trust,"). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 8: contents ----------
s=page(8,FM,'iv','Contents','فہرستِ مضامین','د منځپانګې لړلیک','contents',layout='tableOfContents')
head(s,'h','CONTENTS','فہرستِ مضامین','د منځپانګې لړلیک')
TOC=[('1','Collection and Presentation of Data','اعداد و شمار کا اکٹھا کرنا اور پیشکش','د معلوماتو راټولول او وړاندې کول','01'),
('2','Measures of Central Tendency (MCT)','مرکزی رجحان کے پیمانے (MCT)','د مرکزي تمایل اندازې (MCT)','54'),
('3','Measures of Dispersion, Skewness and Kurtosis','انتشار، کجی اور نوکیلاپن کے پیمانے','د خپراوي، کوړوالي او تېزوالي اندازې','90'),
('4','Index Numbers','اشاریہ اعداد','شاخصي شمېرې','145'),
('5','Simple Linear Regression and Correlation','سادہ خطی تانتجہ (ریگریشن) اور ہم رشتگی','ساده خطي ریګرېشن او اړیکه','173'),
('6','Time Series','وقتی سلسلہ','د وخت لړۍ','195'),
('7','Vital Statistics','حیاتی شماریات','حیاتي احصایې','215'),
('8','Interpolation','درمیان یابی','منځګړیتوب (انټرپولېشن)','239'),
('9','Linear Programming','خطی پروگرامنگ','خطي پروګرامېنګ','251'),
('10','Answers','جوابات','ځوابونه','285'),
('11','Glossary','فرہنگ','وییپانګه','291'),
('12','Index','اشاریہ','لړلیک','297')]
s['tables']=[table('Contents','فہرستِ مضامین','د منځپانګې لړلیک',[c('Sr.#','نمبر شمار','ګڼه'),c('Unit','یونٹ','واحد'),c('Pg.#','صفحہ','مخ')],[[c(a),c(b,u,p),c(g)] for a,b,u,p,g in TOC])]
F=Flow(s);F.tb(0);s['flow']=[dict(type='paragraphs',ids=['stat11-s008-h']),dict(type='table',index=0)]
s['sourceNote']='Printed folio (iv). Page numbers as printed ("01" for Unit 1). Header graphics and watermark excluded.'
s['vocabulary']={'contents':dict(ur='فہرستِ مضامین',ps='د منځپانګې لړلیک')}
save(s)
