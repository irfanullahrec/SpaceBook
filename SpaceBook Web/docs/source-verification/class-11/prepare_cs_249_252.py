from cshelp import *
c=cell
U='u7'
def H(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,kind='heading',**m)
NOTE=' Diagrams are redrawn as simplified coded SVG with the printed labels. Watermark, border lines, page-edge shadows and handwriting are excluded.'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
def schema(cols,keys,extra=''):
    # cols: list of names; keys: indexes underlined
    x=10;b='';w=[max(60,len(n)*8+16) for n in cols]
    for i,n in enumerate(cols):
        fill='#c9a6a6' if i in keys else '#8fb4e0'
        b+=f'<rect x="{x}" y="10" width="{w[i]}" height="30" fill="{fill}" stroke="#111"/>'+T(x+w[i]/2,30,n,11,'middle',700)
        if i in keys: b+=f'<line x1="{x+8}" y1="33" x2="{x+w[i]-8}" y2="33" stroke="#111"/>'
        x+=w[i]
    return svg(x+20,60+len(extra)*0,'Table structure: '+', '.join(cols),b+extra)
hd=[c('Proj_no','پراجیکٹ نمبر','د پروژې شمېره'),c('Proj_name','پراجیکٹ نام','د پروژې نوم'),c('Emp_no','ملازم نمبر','د کارکوونکي شمېره'),c('Emp_name','ملازم نام','د کارکوونکي نوم'),c('Job_class','ملازمت کی قسم','د دندې ډول'),c('Charge_per_hour','فی گھنٹہ چارج','په ساعت چارج'),c('Hours','گھنٹے','ساعتونه')]
def r(p,pn,pnu,pnp,e,n,nu,npp,j,ju,jp,ch,h): return [c(p),c(pn,pnu,pnp),c(e),c(n,nu,npp),c(j,ju,jp),c(ch),c(h)]
# ---------- scan 249 (printed 240) ----------
s=page(249,U,'240','Employee Table (Figure 7.23); 2nd Normal Form; Figure 7.24','ایمپلائی ٹیبل (شکل ۷.۲۳)؛ سیکنڈ نارمل فارم؛ شکل ۷.۲۴','د کارکوونکي جدول (انځور ۷.۲۳)؛ دویمه نورمال بڼه؛ انځور ۷.۲۴','p240')
F=Flow(s)
H(s,'h1','Employee Table','ایمپلائی ٹیبل','د کارکوونکي جدول')
rows=[r('15','Evergreen','ایور گرین','ایورګرین','103','Jameel Khan','جمیل خان','جمیل خان','Elect. Engineer','الیکٹریکل انجینئر','برېښنايي انجینیر','1000','23'),
 r('15','Evergreen','ایور گرین','ایورګرین','101','Faisal Naeem','فیصل نعیم','فیصل نعیم','DB Designer','ڈی بی ڈیزائنر','ډېټابېس ډیزاینر','900','19'),
 r('15','Evergreen','ایور گرین','ایورګرین','105','Bilal Ahmad','بلال احمد','بلال احمد','DB Designer','ڈی بی ڈیزائنر','ډېټابېس ډیزاینر','900','35'),
 r('18','MIS','ایم آئی ایس','MIS','114','Zubair Ahmad','زبیر احمد','زبیر احمد','Programmer','پروگرامر','پروګرامر','750','12.6'),
 r('18','MIS','ایم آئی ایس','MIS','118','M. Waseem','ایم۔ وسیم','م. وسیم','System Analyst','سسٹم اینالسٹ','سیسټم تحلیلګر','800','45.3'),
 r('18','MIS','ایم آئی ایس','MIS','104','Shaukat Ali','شوکت علی','شوکت علي','App Designer','ایپ ڈیزائنر','اپ ډیزاینر','600','32.4')]
s['tables']=[table('Figure 7.23 Employee Table','شکل ۷.۲۳ ایمپلائی ٹیبل','انځور ۷.۲۳ د کارکوونکي جدول',hd,rows)]
F.tb(0)
add(s,'a','Attribute Proj_no is not an adequate key and does not uniquely identifies all the records. To maintain a proper primary key, the new key must be composed of a combination of Proj_no and Emp_no.','ایٹریبیوٹ پراجیکٹ_نمبر مناسب کی نہیں ہے اور تمام ریکارڈز کو منفرد طور پر شناخت نہیں کرتا۔ مناسب پرائمری کی برقرار رکھنے کے لیے نئی کی پراجیکٹ_نمبر اور ملازم_نمبر کے امتزاج پر مشتمل ہونی چاہیے۔','خاصیت Proj_no یوه کافي کیلي نه ده او ټول ثبتونه په ځانګړي ډول نه پېژني. د سمې لومړنۍ کیلي د ساتلو لپاره نوې کیلي باید د Proj_no او Emp_no له ګډون جوړه وي.')
H(s,'h2','2nd Normal Form','سیکنڈ نارمل فارم','دویمه نورمال بڼه')
add(s,'b','A relation will be in 2nd NF if it is in the first normal form and all non key attributes must be fully functional dependent on the whole primary key (No partial dependencies). Consider the table 7.24','ریلیشن ۲ این ایف میں ہو گا اگر وہ پہلے نارمل فارم میں ہو اور تمام غیر کی ایٹریبیوٹس پوری پرائمری کی پر مکمل فعلی طور پر منحصر ہوں (کوئی جزوی انحصار نہیں)۔ ٹیبل ۷.۲۴ پر غور کریں','اړیکه به په 2nd NF کې وي که چېرې په لومړۍ نورمال بڼه کې وي او ټول غیر-کیلي خاصیتونه باید په ټوله لومړنۍ کیلي بشپړ دندیز ډول تړلي وي (هېڅ جزوي تکیه نه). ۷.۲۴ جدول ته پام وکړئ')
H(s,'h3','Employee Table','ایمپلائی ٹیبل','د کارکوونکي جدول')
fig=schema(['Proj_no','Proj_name','Emp_no','Emp_name','Job_class','Charge_per_hour','Hours'],[0,2])
fig=fig.replace('height="60"','height="115"').replace('viewBox="0 0 ','viewBox="0 0 ',1)
extra='<polyline points="50,45 50,70 120,70 120,45" fill="none" stroke="#223a8a" stroke-width="1.5"/>'+T(10,95,'Partial dependency',10,'start',700)+'<polyline points="215,45 215,70 440,70 440,45" fill="none" stroke="#223a8a" stroke-width="1.5"/>'+T(300,95,'Partial dependency',10,'start',700)
s['figures']=[dict(svg=schema(['Proj_no','Proj_name','Emp_no','Emp_name','Job_class','Charge_per_hour','Hours'],[0,2],extra).replace('height="60"','height="110"').replace('viewBox="0 0 %d 60"'%0,''),id='cs11-s249-fig1',caption='Figure 7.24',captionUrdu='شکل ۷.۲۴',captionPashto='انځور ۷.۲۴',labels=[lab('Partial dependency','جزوی انحصار','جزوي تکیه')])]
F.fg(0)
F.done()
fin(s,'Printed page 240: Figure 7.23 Employee Table (the same table as Figure 7.22 with the project number and name repeated in every row, six rows), the paragraph on the key, “2nd Normal Form” and Figure 7.24 Employee Table (the seven column names with arrows and the labels “Partial dependency” twice; redrawn as coded SVG). The printed “does not uniquely identifies” is kept.')
# ---------- scan 250 (printed 241) ----------
s=page(250,U,'241','Partial dependencies; Figures 7.25–7.27; 3rd Normal Form; Figure 7.28','جزوی انحصار؛ شکلیں ۷.۲۵ تا ۷.۲۷؛ تھرڈ نارمل فارم؛ شکل ۷.۲۸','جزوي تکیه؛ انځورونه ۷.۲۵ تر ۷.۲۷؛ دریمه نورمال بڼه؛ انځور ۷.۲۸','p241')
F=Flow(s)
add(s,'a','Attribute Proj_name is dependent on Proj_no, while Emp_name, Job_class and Charge_per_hour are dependent on Emp_no. Dependencies based on only part of a composite primary key are called partial dependencies.','ایٹریبیوٹ پراجیکٹ_نام پراجیکٹ_نمبر پر منحصر ہے جبکہ ملازم_نام، جاب_کلاس اور چارج_فی_آور ملازم_نمبر پر منحصر ہیں۔ مرکب پرائمری کی کے صرف ایک حصے پر مبنی انحصار جزوی انحصار کہلاتے ہیں۔','خاصیت Proj_name په Proj_no پورې تړلی دی، پداسې حال کې چې Emp_name، Job_class او Charge_per_hour په Emp_no پورې تړلي دي. هغه تکیه چې یوازې د ترکیبي لومړنۍ کیلي په یوې برخې ولاړې وي جزوي تکیه بلل کېږي.')
H(s,'h1','Project Table','پراجیکٹ ٹیبل','د پروژې جدول')
H(s,'h2','Employee Table','ایمپلائی ٹیبل','د کارکوونکي جدول')
H(s,'h3','Hours Table','آورز ٹیبل','د ساعتونو جدول')
s['figures']=[dict(svg=schema(['Proj_no','Proj_name'],[0]),id='cs11-s250-fig1',caption='Figure 7.25 Project Table',captionUrdu='شکل ۷.۲۵ پراجیکٹ ٹیبل',captionPashto='انځور ۷.۲۵ د پروژې جدول',labels=[]),
 dict(svg=schema(['Emp_no','Emp_name','Job_class','Charge_per_hour'],[0]),id='cs11-s250-fig2',caption='Figure 7.26 Employee Table',captionUrdu='شکل ۷.۲۶ ایمپلائی ٹیبل',captionPashto='انځور ۷.۲۶ د کارکوونکي جدول',labels=[]),
 dict(svg=schema(['Proj_no','Emp_no','Hours'],[0,1]),id='cs11-s250-fig3',caption='Figure 7.27 Hours Table',captionUrdu='شکل ۷.۲۷ آورز ٹیبل',captionPashto='انځور ۷.۲۷ د ساعتونو جدول',labels=[]),
 dict(svg=schema(['Emp_no','Emp_name','Job_class','Charge_per_hour'],[0],'<polyline points="205,45 205,75 290,75 290,45" fill="none" stroke="#223a8a" stroke-width="1.5"/>'+T(300,70,'Transitive dependency',10,'start',700)).replace('height="60"','height="95"'),id='cs11-s250-fig4',caption='Figure 7.28 Employee Table',captionUrdu='شکل ۷.۲۸ ایمپلائی ٹیبل',captionPashto='انځور ۷.۲۸ د کارکوونکي جدول',labels=[lab('Transitive dependency','ترسیلی انحصار','انتقالي تکیه')])]
F.fg(0)
F.fg(1)
F.fg(2)
add(s,'b','Because the number of hours spent on each project by each employee is dependent on both Proj_no and Emp_no, we place these hours in the Hours table hours as in Figure 7.27.','چونکہ ہر ملازم کے ہر پراجیکٹ پر گزارے گئے گھنٹوں کی تعداد پراجیکٹ_نمبر اور ملازم_نمبر دونوں پر منحصر ہے، ہم ان گھنٹوں کو آورز ٹیبل میں رکھتے ہیں جیسا کہ شکل ۷.۲۷ میں ہے۔','ځکه چې د هر کارکوونکي لخوا په هره پروژه تېر شوي ساعتونو شمېر په Proj_no او Emp_no دواړو پورې تړلی دی، موږ دا ساعتونه د ساعتونو جدول کې ږدو لکه څنګه چې ۷.۲۷ انځور کې دي.')
H(s,'h4','3rd Normal Form','تھرڈ نارمل فارم','دریمه نورمال بڼه')
add(s,'c','The relation should be in the 1st and 2nd normal forms and all transitive dependencies must be removed. A transitive dependency is a dependency of one non-key attribute on another non-key attribute. Consider Table in Figure 7.28.','ریلیشن پہلے اور دوسرے نارمل فارمز میں ہونا چاہیے اور تمام ترسیلی انحصار ہٹائے جانے چاہئیں۔ ترسیلی انحصار ایک غیر کی ایٹریبیوٹ کا دوسرے غیر کی ایٹریبیوٹ پر انحصار ہے۔ شکل ۷.۲۸ کے ٹیبل پر غور کریں۔','اړیکه باید په لومړۍ او دویمه نورمال بڼه کې وي او ټولې انتقالي تکیې باید لېرې شي. انتقالي تکیه د یوه غیر-کیلي خاصیت په بل غیر-کیلي خاصیت تکیه ده. په ۷.۲۸ انځور کې جدول ته پام وکړئ.')
H(s,'h5','Employee Table','ایمپلائی ٹیبل','د کارکوونکي جدول')
F.fg(3)
F.done()
fin(s,'Printed page 241: the paragraph on partial dependencies, the Project Table (Figure 7.25: Proj_no, Proj_name), the Employee Table (Figure 7.26: Emp_no, Emp_name, Job_class, Charge_per_hour), the Hours Table (Figure 7.27: Proj_no, Emp_no, Hours), “3rd Normal Form” and the Employee Table with an arrow labelled “Transitive dependency” (Figure 7.28); the table structures are redrawn as coded SVG with the key columns underlined as printed.')
# ---------- scan 251 (printed 242) ----------
s=page(251,U,'242','3rd Normal Form (end); Figures 7.29 and 7.30','تھرڈ نارمل فارم (اختتام)؛ شکلیں ۷.۲۹ اور ۷.۳۰','دریمه نورمال بڼه (پای)؛ انځورونه ۷.۲۹ او ۷.۳۰','p242')
F=Flow(s)
add(s,'a','Both Job_class and Charge_per_hour are nonprime attributes and the later one is dependent on the former. So by removing transitive dependency the following new tables will be created.','جاب_کلاس اور چارج_فی_آور دونوں غیر بنیادی ایٹریبیوٹس ہیں اور بعد والا پہلے والے پر منحصر ہے۔ اس لیے ترسیلی انحصار ہٹانے سے درج ذیل نئے ٹیبلز بنیں گے۔','Job_class او Charge_per_hour دواړه غیر لومړني خاصیتونه دي او وروستی په مخکني پورې تړلی دی. نو د انتقالي تکیې په لېرې کولو سره به لاندې نوي جدولونه جوړ شي.')
H(s,'h1','Employee Table','ایمپلائی ٹیبل','د کارکوونکي جدول')
H(s,'h2','Job Table','جاب ٹیبل','د دندې جدول')
s['figures']=[dict(svg=schema(['Emp_no','Emp_name','Job_class'],[0]),id='cs11-s251-fig1',caption='Figure 7.29 Employee Table',captionUrdu='شکل ۷.۲۹ ایمپلائی ٹیبل',captionPashto='انځور ۷.۲۹ د کارکوونکي جدول',labels=[]),
 dict(svg=schema(['Job_class','Chg_per_hour'],[0]),id='cs11-s251-fig2',caption='Figure 7.30 Job Table',captionUrdu='شکل ۷.۳۰ جاب ٹیبل',captionPashto='انځور ۷.۳۰ د دندې جدول',labels=[])]
F.fg(0)
F.fg(1)
F.done()
fin(s,'Printed page 242: the closing paragraph of 3rd Normal Form, the Employee Table (Figure 7.29: Emp_no, Emp_name, Job_class) and the Job Table (Figure 7.30: Job_class, Chg_per_hour), both redrawn as coded SVG with the key columns underlined as printed. The rest of the page is blank. “Chg_per_hour” is printed in the Job Table.')
# ---------- scan 252 (printed 243) ----------
s=page(252,U,'243','Summary of Unit 7 (1)','یونٹ ۷ کا خلاصہ (۱)','د ۷ واحد لنډیز (۱)','p243')
F=Flow(s)
H(s,'h','SUMMARY','خلاصہ','لنډیز')
L(s,[('b1','Data is a collection of facts, figures, numbers or ideas that can be organized and processed.','ڈیٹا حقائق، اعداد و شمار، نمبروں یا خیالات کا مجموعہ ہے جسے منظم اور پراسیس کیا جا سکتا ہے۔','ډېټا د حقایقو، شمېرو، عددونو یا مفکورو ټولګه ده چې منظم او پروسس کېدای شي.'),('b2','When facts, figures or numbers (data) are processed and converted into meaningful form that can be used for decision making or any other useful activity, it is called Information.','جب حقائق، اعداد و شمار یا نمبرز (ڈیٹا) کو پراسیس کر کے بامعنی شکل میں تبدیل کیا جائے جو فیصلہ سازی یا کسی اور مفید سرگرمی کے لیے استعمال ہو سکے تو اسے معلومات کہتے ہیں۔','کله چې حقایق، شمېرې یا عددونه (ډېټا) پروسس شي او مانادار بڼې ته بدل شي چې د پرېکړې کولو یا کوم بل ګټور فعالیت لپاره کارېدای شي، نو دې ته معلومات ویل کېږي.'),('b3','File Management system also known as Conventional file system or simply file system is a method of storing and organizing collection of data in the form of files on the secondary storage devices.','فائل مینجمنٹ سسٹم، جسے روایتی فائل سسٹم یا محض فائل سسٹم بھی کہتے ہیں، ثانوی ذخیرہ آلات پر فائلوں کی شکل میں ڈیٹا کے مجموعے کو ذخیرہ اور منظم کرنے کا ایک طریقہ ہے۔','د فایل مدیریت سیسټم، چې دودیز فایل سیسټم یا یوازې فایل سیسټم هم ورته ویل کېږي، په ثانوي ذخیره وسایلو کې د فایلونو په بڼه د ډېټا د ټولګې د ساتلو او منظمولو یوه طریقه ده.'),('b4','Database is a shared collection of logically related data (and a description of this data i.e. metadata), designed to meet the information needs of multiple users in an organization.','ڈیٹا بیس منطقی طور پر متعلقہ ڈیٹا (اور اس ڈیٹا کی تفصیل یعنی میٹا ڈیٹا) کا مشترکہ مجموعہ ہے جو کسی ادارے میں متعدد صارفین کی معلوماتی ضروریات پوری کرنے کے لیے بنایا گیا ہو۔','ډېټابېس د منطقي اړوندې ډېټا (او د دې ډېټا تشریح یعنې میټا ډېټا) ګډه ټولګه ده، چې په یوه اداره کې د ډیرو کاروونکو د معلوماتي اړتیاوو د پوره کولو لپاره ډیزاین شوې ده.'),('b5','A database management system (DBMS) is a set of programs that allow users to create a database, edit and update data in database files, store and retrieve data from those database files.','ڈیٹا بیس مینجمنٹ سسٹم (ڈی بی ایم ایس) پروگراموں کا ایک مجموعہ ہے جو صارفین کو ڈیٹا بیس بنانے، ڈیٹا بیس فائلوں میں ڈیٹا میں ترمیم اور اپ ڈیٹ کرنے اور ان فائلوں سے ڈیٹا محفوظ اور حاصل کرنے کی اجازت دیتا ہے۔','د ډېټابېس مدیریت سیسټم (DBMS) د پروګرامونو یوه ټولګه ده چې کاروونکو ته اجازه ورکوي ډېټابېس جوړ کړي، په ډېټابېس فایلونو کې ډېټا سمه او تازه کړي، له هغو ډېټابېس فایلونو نه ډېټا ذخیره او ترلاسه کړي.'),('b6','A database model is a set of rules or specifications which state that how data can be stored, organized and manipulated in a database system.','ڈیٹا بیس ماڈل قواعد یا وضاحتوں کا مجموعہ ہے جو بیان کرتا ہے کہ ڈیٹا بیس سسٹم میں ڈیٹا کو کیسے ذخیرہ، منظم اور اس میں ترمیم کی جا سکتی ہے۔','د ډېټابېس ماډل د قواعدو یا مشخصاتو یوه ټولګه ده چې بیانوي چې په ډېټابېس سیسټم کې ډېټا څنګه ذخیره، منظم او کار ترې اخیستل کېدای شي.'),('b7','Hierarchal Database Model is a type of model in which data is organized into a tree-like structure.','ہائیرارکل ڈیٹا بیس ماڈل ایسا ماڈل ہے جس میں ڈیٹا درخت نما ساخت میں منظم ہوتا ہے۔','درجه بندي ډېټابېس ماډل یو ډول ماډل دی چې په هغه کې ډېټا د ونې غوندې جوړښت کې منظمه کېږي.'),('b8','A network database is similar to a hierarchical database except that each child can have more than one parent record.','نیٹ ورک ڈیٹا بیس ہائیرارکیکل ڈیٹا بیس سے مشابہ ہے سوائے اس کے کہ ہر بچے کے ایک سے زیادہ والدین ریکارڈ ہو سکتے ہیں۔','شبکه ډېټابېس د درجه بندي ډېټابېس غوندې ده پرته له دې چې هر ماشوم کېدای شي له یوه څخه ډیر د مور ثبتونه ولري.'),('b9','Relational Database Model uses a collection of tables to represent both data and the relationship among those data. Each table has multiple columns and each column has a unique name.','ریلیشنل ڈیٹا بیس ماڈل ڈیٹا اور ان ڈیٹا کے درمیان تعلق دونوں کو ظاہر کرنے کے لیے ٹیبلز کا مجموعہ استعمال کرتا ہے۔ ہر ٹیبل کے متعدد کالم ہوتے ہیں اور ہر کالم کا منفرد نام ہوتا ہے۔','اړونده ډېټابېس ماډل د جدولونو ټولګه کاروي ترڅو ډېټا او د دغو ډېټا ترمنځ اړیکه دواړه وښیي. هر جدول څو ستونونه لري او هر ستون ځانګړی نوم لري.'),('b10','Object-Oriented database Model is a database model in which information is represented in the form of objects as used in object-oriented programming.','آبجیکٹ اورینٹڈ ڈیٹا بیس ماڈل ایسا ڈیٹا بیس ماڈل ہے جس میں معلومات آبجیکٹس کی شکل میں ظاہر ہوتی ہیں جیسا کہ آبجیکٹ اورینٹڈ پروگرامنگ میں استعمال ہوتا ہے۔','څیز پر بنسټ ډېټابېس ماډل یو ډېټابېس ماډل دی چې په هغه کې معلومات د څیزونو په بڼه ښودل کېږي لکه څنګه چې په څیز پر بنسټ پروګرامنګ کې کارول کېږي.'),('b11','Object relational database model add new object storage capabilities to the relational systems at the core of modern information systems.','آبجیکٹ ریلیشنل ڈیٹا بیس ماڈل جدید معلوماتی نظاموں کے مرکز میں موجود ریلیشنل سسٹمز میں نئی آبجیکٹ ذخیرہ صلاحیتیں شامل کرتا ہے۔','څیز اړونده ډېټابېس ماډل د مدرنو معلوماتي سیسټمونو په مرکز کې اړوندو سیسټمونو ته نوې څیز ذخیرې وړتیاوې زیاتوي.'),('b12','SQL (Structured Query Language) is the standard language for relational database systems.','ایس کیو ایل (سٹرکچرڈ کوئری لینگویج) ریلیشنل ڈیٹا بیس سسٹمز کے لیے معیاری زبان ہے۔','SQL (جوړښت لرونکې پوښتنې ژبه) د اړوندو ډېټابېس سیسټمونو لپاره معیاري ژبه ده.')],'sum')
F.done()
fin(s,'Printed page 243: the heading “SUMMARY” of Unit 7 and twelve bulleted points (the summary continues on the next page). The page has a pink border and the printed word “Hierarchal” is kept.')
