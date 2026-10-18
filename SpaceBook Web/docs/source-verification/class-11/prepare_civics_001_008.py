from civicshelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded.'
def toc(s,rows,note):
    hd=[c('Chapter','نمبر شمار','د څپرکي شمېره'),c('Contents','مضامین','مضامین'),c('Page','صفحہ نمبر','د پاڼې شمېره')]
    body=[[c(ch,ch_u,ch_p),c(en,ur,ps),c(str(pg))] for ch,ch_u,ch_p,ur,en,ps,pg in rows]
    return table('Table of contents','فہرستِ مضامین','د مضامینو فهرست',hd,body,sourceGap=dict(note=note))
def R(ch,ur,en,ps,pg): return (('Ch. '+ch if ch else ''),('باب '+ch if ch else ''),('څپرکی '+ch if ch else ''),ur,en,ps,pg)
# scan 1 = 001_page_1
s=page(1,'front-matter','','Title page','عنوانی صفحہ','د سرلیک پاڼه','title')
F=Flow(s)
H(s,'شہریت','Civics (Shehriyat)','ښارواله (شهریت)')
P(s,'برائے گیارھویں جماعت','For the eleventh class','د یوولسم ټولګي لپاره')
P(s,'پروفیسر بختیار','Professor Bakhtiyar','پروفېسر بختیار')
P(s,'Published by: Leading Books Publisher','Published by: Leading Books Publisher','Published by: Leading Books Publisher')
P(s,'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','Khyber Pakhtunkhwa Textbook Board, Peshawar','د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
F.done()
s['sourceNote']='Title page of the book: title, class, author, publisher and board name. Handwritten signatures, dates and names scribbled on the page are not reproduced; the publisher’s and board logos are not reproduced.'+NOTE
s['vocabulary']={}
save(s)
# scan 2 = 001_page_2
s=page(2,'front-matter','','Two sayings of the Prophet ﷺ on bribery and unlawful wealth','رشوت اور حرام مال کے بارے میں دو احادیث','د رشوت او حرام مال په اړه دوه حدیثونه','sayings')
F=Flow(s)
P(s,'رشوت دینے اور لینے والے پر اللہ تعالیٰ کی لعنت ہے۔ (ابنِ ماجہ)','Allah’s curse is upon the one who gives and the one who takes a bribe. (Ibn Majah)','په رشوت ورکوونکي او اخیستونکي د الله تعالی لعنت دی. (ابن ماجه)',boxed=True)
P(s,'حرام مال سے اللہ تعالیٰ صدقہ قبول نہیں کرتا۔ (احمد)','Allah does not accept charity from unlawful wealth. (Ahmad)','الله تعالی له حرام مال نه صدقه نه قبلوي. (احمد)',boxed=True)
F.done()
s['sourceNote']='Page with two boxed sayings in decorative frames (Ibn Majah; Ahmad); the benediction after the Prophet’s name is not printed. Handwritten marks on the page are not reproduced.'+NOTE
s['vocabulary']={}
save(s)
# scan 3 = 002_page_1 : contents, chapters 1-2
s=page(3,'front-matter','','Table of contents (1): Chapter 1 and the start of Chapter 2','فہرستِ مضامین (1): باب 1 اور باب 2 کا آغاز','د مضامینو فهرست (۱): ۱ څپرکی او د ۲ څپرکي پیل','toc1')
F=Flow(s)
H(s,'فہرستِ مضامین','Table of contents','د مضامینو فهرست')
F.tb(0)
F.done()
rows=[R('1','سیاسی نظام','Political System','سیاسي نظام',1),R('','کمیونٹی','Community','ټولنه',2),R('','ریاست','The State','دولت',3),R('','اسلامی ریاست کا تصور','The concept of the Islamic State','د اسلامي دولت تصور',4),R('','ریاست اور حکومت میں فرق','Difference between state and government','د دولت او حکومت ترمنځ توپیر',8),R('','حکومت کی ضرورت','The need for government','د حکومت اړتیا',13),R('','آئین','The Constitution','اساسي قانون',14),R('','اچھے آئین کی خصوصیات','Characteristics of a good constitution','د ښه اساسي قانون ځانګړتیاوې',15),R('','پاکستان کے 1973ء کے دستور کی خصوصیات','Features of the 1973 Constitution of Pakistan','د پاکستان د ۱۹۷۳ز دستور ځانګړتیاوې',17),R('','پاکستان کے 1973ء کے دستور میں ترامیم کا خلاصہ','Summary of the amendments to the 1973 Constitution of Pakistan','د پاکستان د ۱۹۷۳ز دستور د ترمیمونو لنډیز',24),R('','پاکستان کے 1973ء کے دستور میں ترامیم کی وجہ سے ابھرنے والے مسائل','Problems arising from the amendments to the 1973 Constitution of Pakistan','د ۱۹۷۳ز دستور د ترمیمونو له امله راپورته شوې ستونزې',26),R('','تحریری اور غیر تحریری دستور','Written and unwritten constitutions','لیکلی او نالیکلی دستور',27),R('','سیاسی نظام','The political system','سیاسي نظام',28),R('','سیاسی نظام کی خصوصیات','Characteristics of a political system','د سیاسي نظام ځانګړتیاوې',28),R('','فیصلہ ساز سیاسی ادارے اور سرگرمیاں','Decision-making political institutions and activities','پرېکړه کوونکي سیاسي ادارې او فعالیتونه',30),R('2','حکومت کی اقسام','Types of Government','د حکومت ډولونه',36),R('','بادشاہت','Monarchy','پاچاهي',37),R('','جمہوریت، خصوصیات و اصول','Democracy: characteristics and principles','جمهوریت، ځانګړتیاوې او اصول',40)]
s['tables']=[toc(s,rows,'Printed as a three-column table (Number, Contents, Page). The chapter label appears only on the first row of each chapter. The rows “Political system” and “Characteristics of a political system” both show page 28 as printed.')]
s['sourceNote']='Contents page 1 of 5 (scan order): Chapter 1 (all entries) and the first three rows of Chapter 2, with printed page numbers 1–40. The contents pages were photographed out of reading order; this page comes first.'+NOTE
s['vocabulary']={}
save(s)
# scan 4 = 002_page_2 : publisher details
s=page(4,'front-matter','','Copyright, approval and editorial credits','حقوق، منظوری اور ادارتی تفصیل','د حقوقو، منظورۍ او مسؤلیت تفصیل','credits')
F=Flow(s)
P(s,'جملہ حقوق بجنّگ لیڈنگ بکس پبلیشرز محفوظ ہیں۔','All rights reserved by Leading Books Publishers.','ټول حقوق د لیډنګ بکس پبلیشرز لپاره خوندي دي.',boxed=True)
P(s,'منظور کردہ: نظامتِ نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد','Approved by: Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','منظور شوی: د خیبر پښتونخوا د نصاب او د ښوونکو زده کړې رياست، ایبټ اباد')
P(s,'بمطابق: قومی نصاب 2006','According to: National Curriculum 2006','د ۲۰۰۶ز ملي نصاب سره سم')
P(s,'مراسلہ نمبر 8536-38/SS-II مورخہ 09-10-2012','Letter No. 8536-38/SS-II dated 09-10-2012','مراسله شمېره 8536-38/SS-II نېټه ۰۹-۱۰-۲۰۱۲')
P(s,'مصنف: پروفیسر بختیار','Author: Professor Bakhtiyar','لیکوال: پروفېسر بختیار')
P(s,'نگران نظرِ ثانی کمیٹی: سید بشیر حسین شاہ، ناظم، نظامتِ نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد','Supervisor of the review committee: Syed Bashir Hussain Shah, Director, Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','د بیاکتنې کمېټې څارونکی: سید بشیر حسین شاه، رئیس، د خیبر پښتونخوا د نصاب او ښوونکو زده کړې رياست، ایبټ اباد')
P(s,'نظرِ ثانی: عطاء اللہ خان (ڈائریکٹر)، ڈائریکٹریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن خیبر پختونخوا، ایبٹ آباد؛ خالد شاہ، پرنسپل گورنمنٹ ہائی سکول کاکا صاحب، نوشہرہ؛ طاہر اقبال، اسسٹنٹ پروفیسر گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد؛ ولی خان، ڈپٹی ڈائریکٹر (پی اینڈ ڈی) ایلیمنٹری اینڈ سیکنڈری ایجوکیشن پشاور؛ فضل الرحمٰن، ماہر مضمون، ڈائریکٹریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن خیبر پختونخوا، ایبٹ آباد','Review: Ataullah Khan (Director), Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad; Khalid Shah, Principal, Government High School Kaka Sahib, Nowshera; Tahir Iqbal, Assistant Professor, Government Postgraduate College No. 1, Abbottabad; Wali Khan, Deputy Director (P&D), Elementary and Secondary Education, Peshawar; Fazl-ur-Rahman, Subject Specialist, Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','بیاکتنه: عطاء الله خان (رئیس)، د خیبر پښتونخوا د نصاب او ښوونکو زده کړې رياست، ایبټ اباد؛ خالد شاه، پرنسپل حکومتي عالي ښوونځی کاکا صاحب، نوښار؛ طاهر اقبال، اسیستنټ پروفېسر حکومتي پوسټ ګریجویټ کالج نمبر ۱، ایبټ اباد؛ ولي خان، مرستیال رئیس (پی اینډ ډي) لومړنۍ او ثانوي زده کړې پېښور؛ فضل الرحمن، د مضمون متخصص، د خیبر پښتونخوا د نصاب او ښوونکو زده کړې رياست، ایبټ اباد')
P(s,'ایڈیٹر: غلام زاہد جان، ماہر مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Editor: Ghulam Zahid Jan, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar','مدیر: غلام زاهد جان، د مضمون متخصص، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
P(s,'طباعت زیرِ نگرانی: ڈاکٹر حسین آفریدی (چیئرمین)، سعید الرحمٰن (ممبر ای اینڈ پی)، خیبر پختونخوا ٹیکسٹ بک بورڈ','Printed under the supervision of: Dr Hussain Afridi (Chairman), Saeed-ur-Rahman (Member, E&P), Khyber Pakhtunkhwa Textbook Board','چاپ د څارنې لاندې: ډاکټر حسین افریدي (رئیس)، سعید الرحمن (غړی ای اینډ پي)، د خیبر پښتونخوا د درسي کتابونو بورډ')
P(s,'تعلیمی سال: 2019-20','Academic year: 2019-20','تعلیمي کال: ۲۰۱۹-۲۰')
P(s,'ویب سائٹ: www.kptbb.gov.pk','Website: www.kptbb.gov.pk','ویب پاڼه: www.kptbb.gov.pk')
P(s,'ای میل: memberbb@yahoo.com','Email: memberbb@yahoo.com','ای میل: memberbb@yahoo.com')
P(s,'فون نمبر: 091-9217159-60','Phone: 091-9217159-60','تلیفون: 091-9217159-60')
F.done()
s['sourceNote']='Copyright, approval, review and printing credits page; the first line (“جملہ حقوق …”) is boxed. Some words in the first line and in names are hard to read in the scan (e.g. the publisher’s name “بجنّگ” read as printed; “کاکا صاحب” in a school name), and are given as read.'+NOTE
s['vocabulary']={}
save(s)
# scan 5 = 003_page_1 : contents, chapters 4(end)-6(start)
s=page(5,'front-matter','','Table of contents (3): end of Chapter 4, Chapter 5 and the start of Chapter 6','فہرستِ مضامین (3): باب 4 کا اختتام، باب 5 اور باب 6 کا آغاز','د مضامینو فهرست (۳): د ۴ څپرکي پای، ۵ څپرکی او د ۶ څپرکي پیل','toc3')
F=Flow(s)
H(s,'فہرستِ مضامین','Table of contents','د مضامینو فهرست')
F.tb(0)
F.done()
rows=[R('','اور سیاست پر اثرات','and its effects on politics','او په سیاست باندې اغېزې',83),R('','پاکستان کا ملائشیا، چین اور سری لنکا سے آزاد تجارت کے معاہدات اور پاکستان پر سیاسی اثرات','Pakistan’s free-trade agreements with Malaysia, China and Sri Lanka and their political effects on Pakistan','د پاکستان له مالیزیا، چین او سري لنکا سره د آزادې سوداګرۍ تړونونه او په پاکستان سیاسي اغېزې',85),R('','پاکستان کا ایران، چین اور بھارت سے سیاسی تعلقات','Pakistan’s political relations with Iran, China and India','د پاکستان له ایران، چین او هند سره سیاسي اړیکې',88),R('5','تضاد اور تضاد کا حل','Conflict and Conflict Resolution','ټکر او د ټکر حل',99),R('','تضاد اور تضاد میں شدت','Conflict and escalation of conflict','ټکر او د ټکر شدت',100),R('','تضاد میں حصہ داروں کے مفادات اور حالت','Interests and position of the parties in a conflict','په ټکر کې د ونډه وال د ګټو او حالت',102),R('','تضاد کی پھیلاؤ کے وجوہات کا تجزیہ (ذاتی، مقامی، قومی اور بین الاقوامی)','Analysis of the causes of the spread of conflict (personal, local, national and international)','د ټکر د خپرېدو د لاملونو تحلیل (شخصي، سیمه ایز، ملي او نړیوال)',106),R('','تضاد کا حل: اتفاقِ رائے، مل کر کام کرنا، سودے بازی','Resolving conflict: consensus, working together, bargaining','د ټکر حل: اتفاق، یو ځای کار، سودا',106),R('','پاکستان میں قومی سطح پر اہم تضادات کی نشاندہی اور وجوہات','Identifying the main national conflicts in Pakistan and their causes','په پاکستان کې په ملي کچه د مهمو ټکرونو پېژندنه او لاملونه',108),R('','تشدد کے ذریعے اختلافات حل کرنے کے نتائج','Consequences of resolving disputes through violence','په تاوتریخوالي سره د اختلافونو د حل پایلې',111),R('','قومی سطح پر تضاد کے حل میں حکومتی اقدامات','Government measures in resolving conflict at the national level','په ملي کچه د ټکر په حل کې حکومتي اقدامات',112),R('','مل کر کام کرنے، سودا بازی اور اتفاقِ رائے سے پاکستان میں قومی تضادات کے حل کے لیے حکمتِ عملی','Strategy for resolving national conflicts in Pakistan through working together, bargaining and consensus','د یو ځای کار، سودا او اتفاق له لارې په پاکستان کې د ملي ټکرونو د حل ستراتیژي',115),R('6','علمی مہارتیں','Practical Skills','علمي مهارتونه',121),R('','تفتیش یا انکوائری کے مراحل','Stages of investigation or inquiry','د تفتیش یا پوښتنې پړاوونه',123),R('','مقامی یا ملکی کمیونٹی میں اہم مسائل کی نشاندہی','Identifying important problems in the local or national community','په سیمه ایزه یا ملي ټولنه کې د مهمو ستونزو پېژندنه',124),R('','تنقیدی سوچ (تعصب)','Critical thinking (bias)','انتقادي فکر (تعصب)',126),R('','پروپیگنڈہ (تعریف)','Propaganda (definition)','پروپېګنډا (تعریف)',127)]
s['tables']=[toc(s,rows,'Printed as a three-column table. The first row continues an entry begun on the previous page (the entry on the ECO and Pakistan’s economy at page 80 in the previous contents page).')]
s['sourceNote']='Contents page 3 of 5 (scan order): the end of Chapter 4’s list, all of Chapter 5, and the first rows of Chapter 6, with printed page numbers 83–127. Right edge slightly cut.'+NOTE
s['vocabulary']={}
save(s)
# scan 6 = 003_page_2 : contents, chapters 2(end)-4(start)
s=page(6,'front-matter','','Table of contents (2): end of Chapter 2, Chapter 3 and the start of Chapter 4','فہرستِ مضامین (2): باب 2 کا اختتام، باب 3 اور باب 4 کا آغاز','د مضامینو فهرست (۲): د ۲ څپرکي پای، ۳ څپرکی او د ۴ څپرکي پیل','toc2')
F=Flow(s)
H(s,'فہرستِ مضامین','Table of contents','د مضامینو فهرست')
F.tb(0)
F.done()
rows=[R('','آمریت','Dictatorship','استبداد',44),R('','آمریت کی خصوصیات','Characteristics of dictatorship','د استبداد ځانګړتیاوې',45),R('','اسلامی حکومت اور اس کی خصوصیات','The Islamic government and its characteristics','اسلامي حکومت او ځانګړتیاوې یې',49),R('','مختلف طرزِ ہائے حکومت کی بنیادیں (نظریہ، ثقافت، تاریخ، اقدار وغیرہ)','Foundations of the different forms of government (ideology, culture, history, values, etc.)','د مختلفو حکومتي ډولونو بنسټونه (نظریه، کلتور، تاریخ، ارزښتونه او نور)',52),R('3','حقوق','Rights','حقوق',57),R('','انسانی حقوق کی تاریخ','History of human rights','د انساني حقونو تاریخ',58),R('','حقوق کے اقسام','Types of rights','د حقونو ډولونه',59),R('','اسلام میں انسانی حقوق کی تاریخ','History of human rights in Islam','په اسلام کې د انساني حقونو تاریخ',63),R('','اسلام میں بنیادی انسانی حقوق','Basic human rights in Islam','په اسلام کې بنسټیز انساني حقونه',64),R('','اقوامِ متحدہ کے حقوق کا عالمی منشور اور موازنہ','The United Nations Universal Declaration of Human Rights and a comparison','د ملګرو ملتونو د حقونو نړیوال منشور او پرتله',68),R('','اعلامیہ اور کنونشن میں فرق','Difference between a declaration and a convention','د اعلامیې او کنوانسیون ترمنځ توپیر',73),R('','انسانی حقوق کی ناقابلِ تقسیم، باہمی انحصار اور تعلق خصوصیات','The indivisible, interdependent and interrelated character of human rights','د انساني حقونو د نه ویشلو، متقابل انحصار او اړیکې ځانګړتیاوې',74),R('4','سیاسی اقتصادیات','Political Economics','سیاسي اقتصادیات',78),R('','سیاسی اقتصادیات','Political economics','سیاسي اقتصادیات',79),R('','بین الاقوامی تجارت، دو طرفہ تجارت اور کثیر الاطرافی تجارت','International trade, bilateral trade and multilateral trade','نړیواله سوداګري، دوه اړخیزه سوداګري او څو اړخیزه سوداګري',79),R('','پاکستان کی اقتصادیات اور سیاست پر سارک کے اثرات','Effects of SAARC on Pakistan’s economy and politics','په پاکستان اقتصاد او سیاست د سارک اغېزې',80),R('','اقتصادی تعاون تنظیم (ای سی او ECO) کی پاکستان کی اقتصادیات','The Economic Cooperation Organisation (ECO) and Pakistan’s economy','د اقتصادي همکارۍ سازمان (ای سي او) او د پاکستان اقتصاد',80)]
s['tables']=[toc(s,rows,'Printed as a three-column table. The last block (Chapter 4) has one fewer page number than lines; the numbers 79, 79, 80 are aligned approximately with “سیاسی اقتصادیات”, “بین الاقوامی تجارت …” and the ECO line, and the SAARC line is assigned 80 here (uncertain). The next contents page begins with “83 اور سیاست پر اثرات”.')]
s['sourceNote']='Contents page 2 of 5 (scan order): end of Chapter 2’s list, all of Chapter 3 and the start of Chapter 4, with printed page numbers 44–80. Edge of the page slightly shadowed.'+NOTE
s['vocabulary']={}
save(s)
# scan 7 = 004_page_1 : contents, chapter 8
s=page(7,'front-matter','','Table of contents (5): Chapter 8','فہرستِ مضامین (5): باب 8','د مضامینو فهرست (۵): ۸ څپرکی','toc5')
F=Flow(s)
H(s,'فہرستِ مضامین','Table of contents','د مضامینو فهرست')
F.tb(0)
F.done()
rows=[R('8','انسانی اقدار کا فروغ','Promotion of Human Values','د انساني ارزښتونو وده',167),R('','انسانی اقدار','Human values','انساني ارزښتونه',168),R('','مساوات، داد رسی اور عدم مساوات','Equality, justice and inequality','مساوات، عدالت او نابرابري',169),R('','پاکستانی معاشرہ میں عدم مساوات کے اقسام','Types of inequality in Pakistani society','په پاکستاني ټولنه کې د نابرابرۍ ډولونه',170),R('','پاکستانی معاشرہ میں عدم مساوات کی وجوہات','Causes of inequality in Pakistani society','په پاکستاني ټولنه کې د نابرابرۍ لاملونه',172),R('','پاکستانی معاشرہ میں عدم مساوات کے اثرات','Effects of inequality in Pakistani society','په پاکستاني ټولنه کې د نابرابرۍ اغېزې',175),R('','اُن گروہوں کی نشاندہی جن کو مقامی اور قومی سطح پر امتیازات کا سامنا ہے','Identifying the groups that face discrimination at the local and national level','د هغو ډلو پېژندنه چې په سیمه ایزه او ملي کچه تبعیض سره مخامخ دي',179),R('','معاشرہ میں عدل کے فروغ کے طریقے','Ways of promoting justice in society','په ټولنه کې د عدل د ودې لارې',180),R('','ناانصافی (امتیاز، تفریق اور سٹیریوٹائپ کے تعاریف)','Injustice (definitions of discrimination, differentiation and stereotype)','بې انصافي (د تبعیض، تفریق او سټېریوټایپ تعریفونه)',183),R('','تعصب اور سٹیریوٹائپ کے امتیازات میں تبدیل کرنے والے طریقے','Ways in which prejudice and stereotypes turn into discrimination','هغه لارې چې تعصب او سټېریوټایپ په تبعیض بدلوي',185),R('','پاکستانی معاشرہ میں ناانصافیوں کی نشاندہی','Identifying injustices in Pakistani society','په پاکستاني ټولنه کې د بې انصافیو پېژندنه',187),R('','انصاف کے لوازمات','Requirements of justice','د انصاف اړتیاوې',191),R('','ایسی سرگرمیوں کی تجاویز جو مقامی، ملکی اور عالمی سطح پر انصاف کا سبب بن جائیں','Suggested activities that could bring about justice at the local, national and global level','د هغو فعالیتونو وړاندیزونه چې په سیمه ایزه، ملي او نړیواله کچه د انصاف سبب شي',194)]
s['tables']=[toc(s,rows,'Printed as a three-column table; the chapter label “باب 8” is printed once.')]
s['sourceNote']='Contents page 5 of 5 (scan order): Chapter 8 (printed pages 167–194). The contents list ends with this chapter; the book’s last entry is page 194.'+NOTE
s['vocabulary']={}
save(s)
# scan 8 = 004_page_2 : contents, chapters 6(end)-7
s=page(8,'front-matter','','Table of contents (4): end of Chapter 6 and Chapter 7','فہرستِ مضامین (4): باب 6 کا اختتام اور باب 7','د مضامینو فهرست (۴): د ۶ څپرکي پای او ۷ څپرکی','toc4')
F=Flow(s)
H(s,'فہرستِ مضامین','Table of contents','د مضامینو فهرست')
F.tb(0)
F.done()
rows=[R('','پروپیگنڈہ کے مختلف طریقے','Different methods of propaganda','د پروپېګنډا بېلابېلې لارې',128),R('','معلومات جمع کرنے کے طریقے','Methods of collecting information','د معلوماتو راټولولو لارې',132),R('','مقامی یا صوبائی پالیسی تبدیل کرنے کے لیے تجاویز تاکہ مسئلہ یا واقعہ صحیح انداز میں حل ہو','Suggestions for changing local or provincial policy so that a problem or event is resolved properly','د سیمه ایزې یا ولایتي پالیسۍ د بدلولو وړاندیزونه ترڅو ستونزه یا پېښه په سمه توګه حل شي',135),R('','تفتیش سے حاصل کردہ معلومات کی زبانی یا پاور پوائنٹ کے ذریعے پیشکش','Presenting the information obtained from the inquiry orally or through PowerPoint','له تفتیش نه د ترلاسه شویو معلوماتو شفاهي یا د پاور پوینټ له لارې وړاندې کول',136),R('7','ذرائع ابلاغ اور سول سوسائٹی','Media and Civil Society','د خبرولو وسایل او مدني ټولنه',142),R('','ذرائع ابلاغ: تعریف','The media: definition','د خبرولو وسایل: تعریف',143),R('','آزاد میڈیا کی ضرورت اور اہمیت','The need for and importance of a free media','د آزاد رسنیو اړتیا او اهمیت',143),R('','پاکستان میں جمہوریت کی ترقی اور مضبوطی میں میڈیا کا کردار','The role of the media in the growth and strengthening of democracy in Pakistan','په پاکستان کې د جمهوریت په وده او پیاوړتیا کې د رسنیو رول',144),R('','میڈیا پر نظر رکھنے کے لیے حکومتی قوانین','Government laws for keeping watch over the media','د رسنیو د څارنې لپاره حکومتي قوانین',147),R('','سول سوسائٹی','Civil society','مدني ټولنه',151),R('','جمہوری معاشرہ میں سول سوسائٹی کے فرائض','The duties of civil society in a democratic society','په دیموکراتیکه ټولنه کې د مدني ټولنې دندې',152),R('','غیر سرکاری تنظیموں کی تعریف','Definition of non-governmental organisations','د غیر دولتي سازمانونو تعریف',153),R('','پاکستان میں غیر سرکاری تنظیموں کو درپیش مشکلات','Difficulties faced by NGOs in Pakistan','په پاکستان کې غیر دولتي سازمانونو ته مخامخ ستونزې',154),R('','پاکستان میں سماجی و اقتصادی ترقی میں غیر سرکاری تنظیموں کا کردار','The role of NGOs in social and economic development in Pakistan','په پاکستان کې په ټولنیزه او اقتصادي پرمختګ کې د غیر دولتي سازمانونو رول',156),R('','غیر سرکاری تنظیم اور مفاداتی گروہ میں فرق','Difference between an NGO and an interest group','د غیر دولتي سازمان او ګټو ډلې ترمنځ توپیر',156),R('','شہریوں کی فلاح اور جمہوریت کے لیے سول سوسائٹی تنظیموں، مفاداتی گروہوں اور غیر سیاسی تنظیموں کا کردار','The role of civil society organisations, interest groups and non-political organisations in the welfare of citizens and for democracy','د اتباعو د هوساینې او جمهوریت لپاره د مدني ټولنې سازمانونو، د ګټو ډلو او غیر سیاسي سازمانونو رول',158),R('','رضاکاری کی تعریف','Definition of voluntarism','د داوطلبۍ تعریف',161),R('','پاکستانی معاشرہ میں رضاکاری کی اہمیت','The importance of voluntarism in Pakistani society','په پاکستاني ټولنه کې د داوطلبۍ اهمیت',162)]
s['tables']=[toc(s,rows,'Printed as a three-column table; the chapter label “باب 7” is printed once. The page is shadowed along the left edge.')]
s['sourceNote']='Contents page 4 of 5 (scan order): end of Chapter 6’s list and all of Chapter 7, with printed page numbers 128–162.'+NOTE
s['vocabulary']={}
save(s)
