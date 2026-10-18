"""Chemistry source cover, credits and contents with aligned target languages."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save

def make(identity,title,urt,pst,paras,page,blocks=None,layout=None):
    s=section(identity,title,urt,pst,paras,layout or [{'type':'paragraph','indices':[i]} for i in range(len(paras))],blocks or [],None)
    s['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':page,'printedPage':None}]
    s['insertBefore']='13.1';s['kind']='book_front_matter'
    return s

cover=make('chem12-cover','Textbook cover','کتاب کا سرورق','د کتاب پوښ',[
    pair('A Textbook of Chemistry','کیمیا کی نصابی کتاب','د کیمیا درسي کتاب'),
    pair('For Grade XII','بارہویں جماعت کے لیے','د دولسم ټولګي لپاره'),
    pair('Free From Government','حکومت کی طرف سے مفت','د حکومت له خوا وړیا'),
    pair('NOT FOR SALE','فروخت کے لیے نہیں','د پلور لپاره نه دی'),
    pair('Khyber Pakhtunkhwa Textbook Board Peshawar','خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
],1)

credits=make('chem12-credits','Publication and title page','اشاعتی معلومات اور صفحۂ عنوان','د خپرونې معلومات او د سرلیک پاڼه',[
 pair('All rights reserved with the Leading Books Publishers, Peshawar.','جملہ حقوق لیڈنگ بکس پبلشرز، پشاور کے پاس محفوظ ہیں۔','ټول حقوق له لیډنګ بکس خپرندویانو، پېښور، سره خوندي دي.'),
 pair('Approved by: Directorate of Curriculum and Teachers Education Khyber Pakhtunkhwa, Abbottabad, according to the National Curriculum 2006.','منظور شدہ: ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچرز ایجوکیشن خیبر پختونخوا، ایبٹ آباد، قومی نصاب 2006 کے مطابق۔','منظور شوی: د خیبر پښتونخوا د نصاب او ښوونکو د روزنې ریاست، ایبټ آباد، د 2006 ملي نصاب له مخې.'),
 pair('NOC No. 2666-68/G-04/CTR/Chm-XII_LBP     Dated: 06/05/2021','این او سی نمبر: 2666-68/G-04/CTR/Chm-XII_LBP     تاریخ: 06/05/2021','د NOC شمېره: 2666-68/G-04/CTR/Chm-XII_LBP     نېټه: 06/05/2021'),
 pair('Authors: Prof. Dr. Khurshid Ali; Zaid Ullah; Muhammad Amin; Dr. Muhammad Ibrahim; Mushtaq-ur-Rehman.','مصنفین: پروفیسر ڈاکٹر خورشید علی؛ زید اللہ؛ محمد امین؛ ڈاکٹر محمد ابراہیم؛ مشتاق الرحمٰن۔','لیکوالان: پروفیسور ډاکټر خورشید علي؛ زید الله؛ محمد امین؛ ډاکټر محمد ابراهیم؛ مشتاق الرحمن.'),
 pair('Review Supervision: Gohar Ali Khan, Director, Curriculum and Teachers Education Khyber Pakhtunkhwa, Abbottabad.','نظرثانی کی نگرانی: گوہر علی خان، ڈائریکٹر، کریکولم اینڈ ٹیچرز ایجوکیشن خیبر پختونخوا، ایبٹ آباد۔','د بیاکتنې څارنه: ګوهر علي خان، د خیبر پښتونخوا د نصاب او ښوونکو د روزنې رئیس، ایبټ آباد.'),
 pair('Focal Person: Zulfiqar Khan, Additional Director, Curriculum and Textbook Review, Directorate of Curriculum and Teachers Education, Khyber Pakhtunkhwa, Abbottabad.','فوکل پرسن: ذوالفقار خان، ایڈیشنل ڈائریکٹر، کریکولم اینڈ ٹیکسٹ بک ریویو، ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچرز ایجوکیشن، خیبر پختونخوا، ایبٹ آباد۔','اړیکې مسؤول: ذوالفقار خان، د نصاب او درسي کتابونو د بیاکتنې اضافي رئیس، د خیبر پښتونخوا د نصاب او ښوونکو د روزنې ریاست، ایبټ آباد.'),
 pair('Re-reviewers:','دوبارہ نظرثانی کرنے والے:','بیا بیاکتونکي:'),
 pair('Dr. Muhammad Shakeel, Associate Professor, Govt: Degree College Lahor, Swabi.','ڈاکٹر محمد شکیل، ایسوسی ایٹ پروفیسر، گورنمنٹ ڈگری کالج لاہور، صوابی۔','ډاکټر محمد شکیل، اسوسیټ پروفیسور، حکومتي ډګري کالج، لاهور، صوابۍ.'),
 pair('Umer Farooq, Principal, GHS Pabbi, Nowshera.','عمر فاروق، پرنسپل، جی ایچ ایس پبی، نوشہرہ۔','عمر فاروق، مدیر، GHS پبي، نوښار.'),
 pair('Ashfaq Ahmad, Subject Specialist, GHSS Behali, Mansehra.','اشفاق احمد، مضمون کے ماہر، جی ایچ ایس ایس بہالی، مانسہرہ۔','اشفاق احمد، د مضمون متخصص، GHSS بهالي، مانسهره.'),
 pair('Salmana Zaman Khan, Subject Specialist (Science), Khyber Pakhtunkhwa Textbook Board, Peshawar.','سلمانہ زمان خان، مضمون کے ماہر (سائنس)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔','سلمانه زمان خان، د مضمون متخصص (ساینس)، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.'),
 pair('Dr. Gul Nazir Khan, Desk Officer, DCTE, Abbottabad.','ڈاکٹر گل نذیر خان، ڈیسک آفیسر، ڈی سی ٹی ای، ایبٹ آباد۔','ډاکټر ګل نذیر خان، د مېز مسؤول، DCTE، ایبټ آباد.'),
 pair('Editor: Salmana Zaman Khan, Subject Specialist (Science), Khyber Pakhtunkhwa Textbook Board, Peshawar.','مدیر: سلمانہ زمان خان، مضمون کے ماہر (سائنس)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔','سموونکی: سلمانه زمان خان، د مضمون متخصص (ساینس)، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.'),
 pair('Printing Supervision: Arshad Khan Afridi Chairman; Abdul Wali Khan Member (E & P); Khyber Pakhtunkhwa Textbook Board, Peshawar.','طباعت کی نگرانی: ارشد خان آفریدی، چیئرمین؛ عبدالولی خان، ممبر (E & P)؛ خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔','د چاپ څارنه: ارشد خان اپریدی، مشر؛ عبدالولي خان، غړی (E & P)؛ د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.'),
 pair('Academic Year: 2022-23','تعلیمی سال: 2022-23','تعلیمي کال: 2022-23'),
 pair('Website: www.kptbb.gov.pk','ویب سائٹ: www.kptbb.gov.pk','وېبپاڼه: www.kptbb.gov.pk'),
 pair('Email: membertbb@yahoo.com','ای میل: membertbb@yahoo.com','برېښنالیک: membertbb@yahoo.com'),
 pair('Telephone: 091-9217714-15','ٹیلی فون: 091-9217714-15','ټیلیفون: 091-9217714-15'),
 pair('A Textbook of Chemistry','کیمیا کی نصابی کتاب','د کیمیا درسي کتاب'),
 pair('For Grade XII','بارہویں جماعت کے لیے','د دولسم ټولګي لپاره'),
 pair('Khyber Pakhtunkhwa Textbook Board Peshawar','خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور','د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
],3)

titles=['s and p-Block Elements','d and f - Block Elements: Transition Elements','Organic Compounds','Hydrocarbons','Alkyl Halides and Amines','Alcohols, Phenols and Ethers','Carbonyl Compounds 1: Aldehydes and Ketones','Carbonyl Compounds 2: Carboxylic Acids and Functional Derivatives','Biochemistry','Industrial chemistry','Environmental Chemistry','Analytical Chemistry','Answers','Glossary']
ur=['s اور p بلاک کے عناصر','d اور f بلاک کے عناصر: عبوری عناصر','نامیاتی مرکبات','ہائیڈروکاربن','الکائل ہیلائیڈز اور امائنز','الکوحل، فینول اور ایتھر','کاربونائل مرکبات 1: ایلڈیہائیڈز اور کیٹونز','کاربونائل مرکبات 2: کاربوکسلک ایسڈز اور فعلی مشتقات','حیاتی کیمیا','صنعتی کیمیا','ماحولیاتی کیمیا','تجزیاتی کیمیا','جوابات','فرہنگ']
ps=['د s او p بلاک عناصر','د d او f بلاک عناصر: انتقالي عناصر','عضوي مرکبات','هایدروکاربنونه','الکایل هالایډونه او امینونه','الکولونه، فینولونه او اېترونه','کاربونیل مرکبات 1: الدیهایډونه او کېټونونه','کاربونیل مرکبات 2: کاربوکسیلیک اسیدونه او وظیفوي مشتقات','حیاتي کیمیا','صنعتي کیمیا','چاپېریالي کیمیا','تجزیوي کیمیا','ځوابونه','وییزه']
pages=['1','46','81','99','162','194','225','249','272','309','335','358','384','386']
numbers=[str(n) for n in range(13,25)]+['','']
table={'id':'chem12-contents-table','headers':['S/No','Topic','Page/No'],'rows':[[n,t,p] for n,t,p in zip(numbers,titles,pages)],
       'translations':[{'language':'اردو','headers':['نمبر','موضوع','صفحہ نمبر'],'rows':[[n,t,p] for n,t,p in zip(numbers,ur,pages)]},
                       {'language':'پښتو','headers':['شمېره','موضوع','د پاڼې شمېره'],'rows':[[n,t,p] for n,t,p in zip(numbers,ps,pages)]}]}
contents=make('chem12-contents','Contents','فہرست','منځپانګه',[pair('Contents','فہرست','منځپانګه')],4,[table],[{'type':'heading','indices':[0]},{'type':'sourceDataTable','tableId':table['id']}])
if __name__=='__main__':
    save(1,[cover]);save(3,[credits]);save(4,[contents])
