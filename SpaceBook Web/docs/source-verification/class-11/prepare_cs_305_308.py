from cshelp import *
c=cell
EX='cs11-u8-q'
def H(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,kind='heading',**m)
def Q(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,role='question',exerciseId=EX,tab='exercise',**m)
def QI(s,k,en,ur,ps,g): add(s,k,en,ur,ps,role='question',exerciseId=EX,tab='exercise',listGroup=g)
def O(s,k,en,ur,ps,g): add(s,k,en,ur,ps,role='option',exerciseId=EX,tab='exercise',listGroup=g)
NOTE=' Watermark, border lines, page-edge shadows and handwriting are excluded.'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
def M(s,idx,roman,q,qu,qp,opts):
    g=f'm{idx}'
    QI(s,f'm{idx}',f'{roman}. '+q,f'{roman}۔ '+qu,f'{roman}. '+qp,g)
    for j,(l,e,u,p) in enumerate(opts): O(s,f'm{idx}o{j}',f'{l}. '+e,f'{l}۔ '+u,f'{l}. '+p,g)
def at(cap,cu,cp,romans,letters):
    return table(cap,cu,cp,[c(r) for r in romans],[[c(l) for l in letters]])
R10=['i','ii','iii','iv','v','vi','vii','viii','ix','x']
R5=['xi','xii','xiii','xiv','xv']
R8=['i','ii','iii','iv','v','vi','vii','viii']
# ---------- scan 305 (printed 296) ----------
s=page(305,'u8','296','Exercise: Q1 multiple-choice (i–viii)','مشق: سوال ۱ (درست جواب) i تا viii','تمرین: ۱ پوښتنه (سم ځواب) i تر viii','p296')
F=Flow(s)
H(s,'h','EXERCISE','مشق','تمرین')
Q(s,'q1','Q1. Select the best choice for the following MCQs.','سوال ۱: درج ذیل کثیر انتخابی سوالات کے لیے بہترین جواب منتخب کریں۔','۱ پوښتنه: د لاندې څو انتخابي پوښتنو لپاره غوره انتخاب وټاکئ.')
M(s,1,'i','Which of the following is used to store data in a database?','درج ذیل میں سے کون سا ڈیٹا بیس میں ڈیٹا محفوظ کرنے کے لیے استعمال ہوتا ہے؟','لاندې له کوم یو په ډېټابېس کې د ډېټا د ساتلو لپاره کارول کېږي؟',[('A','Table','ٹیبل','جدول'),('B','Form','فارم','فورم'),('C','Query','کوئری','پوښتنه'),('D','Report','رپورٹ','راپور')])
M(s,2,'ii','____________ is a window that displays data for viewing, entering and editing information.','____________ ایک ونڈو ہے جو معلومات دیکھنے، درج کرنے اور ترمیم کرنے کے لیے ڈیٹا دکھاتی ہے۔','____________ یوه کړکۍ ده چې د معلوماتو د لیدلو، دخلولو او سمولو لپاره ډېټا ښيي.',[('A','Table','ٹیبل','جدول'),('B','Form','فارم','فورم'),('C','Query','کوئری','پوښتنه'),('D','Report','رپورٹ','راپور')])
M(s,3,'iii','Which of the following is logical data type?','درج ذیل میں سے کون سا منطقی ڈیٹا ٹائپ ہے؟','لاندې له کوم یو منطقي د ډېټا ډول دی؟',[('A','Text','ٹیکسٹ','متن'),('B','Memo','میمو','یادښت'),('C','Autonumber','آٹو نمبر','اتومات شمېره'),('D','Yes/No','ہاں/نہیں','هو/نه')])
M(s,4,'iv','____________ is an open source application program.','____________ اوپن سورس ایپلیکیشن پروگرام ہے۔','____________ یو پرانیستی سرچینه اپلېکېشن پروګرام دی.',[('A','MS Access','ایم ایس ایکسیس','MS Access (ایم ایس اېکسېس)'),('B','OpenOffice Base','اوپن آفس بیس','اوپن آفس بیس (OpenOffice Base)'),('C','SQL Server','ایس کیو ایل سرور','SQL خدمتګار'),('D','MS Word','ایم ایس ورڈ','MS Word (ایم ایس ورډ)')])
M(s,5,'v','What is the maximum size of text field data type?','ٹیکسٹ فیلڈ ڈیٹا ٹائپ کا زیادہ سے زیادہ سائز کیا ہے؟','د متن ساحې د ډېټا ډول اعظمي کچه څومره ده؟',[('A','253','۲۵۳','۲۵۳'),('B','254','۲۵۴','۲۵۴'),('C','255','۲۵۵','۲۵۵'),('D','256','۲۵۶','۲۵۶')])
M(s,6,'vi','____________ Key is a unique key field in a table.','____________ کی ٹیبل میں ایک منفرد کی فیلڈ ہے۔','____________ کیلي په جدول کې یوه ځانګړې کیلي ساحه ده.',[('A','Secondary','سیکنڈری','دویمي'),('B','Foreign','فارن','بهرنۍ'),('C','Composite','کمپوزٹ','ترکیبي'),('D','Primary','پرائمری','لومړنۍ')])
M(s,7,'vii','Which key is used to create one-to-many relationship between tables?','ٹیبلز کے درمیان ایک سے کئی تعلق بنانے کے لیے کون سی کی استعمال ہوتی ہے؟','د جدولونو ترمنځ د یو-ته-ډیر اړیکې د جوړولو لپاره کومه کیلي کارول کېږي؟',[('A','Secondary','سیکنڈری','دویمي'),('B','Foreign','فارن','بهرنۍ'),('C','Composite','کمپوزٹ','ترکیبي'),('D','Primary','پرائمری','لومړنۍ')])
M(s,8,'viii','____________ is used to display data in an organized manner so that users can print it.','____________ ڈیٹا کو منظم انداز میں دکھانے کے لیے استعمال ہوتا ہے تاکہ صارفین اسے پرنٹ کر سکیں۔','____________ د ډېټا په منظم ډول د ښودلو لپاره کارول کېږي ترڅو کاروونکي یې چاپ کړي.',[('A','Table','ٹیبل','جدول'),('B','Form','فارم','فورم'),('C','Query','کوئری','پوښتنه'),('D','Report','رپورٹ','راپور')])
F.done()
fin(s,'Printed page 296: the banner “EXERCISE” and Q1 with the multiple-choice questions i–viii of Unit 8. The options are printed in two columns, and the printed order of the options within the columns is A, C, B, D reading down; they are given in the order A, B, C, D. The first page of the Exercise starts the exercise of Unit 8.')
# ---------- scan 306 (printed 297) ----------
s=page(306,'u8','297','Exercise: Q2 short questions; Q3 detailed questions','مشق: سوال ۲ مختصر سوالات؛ سوال ۳ تفصیلی سوالات','تمرین: ۲ پوښتنه لنډې پوښتنې؛ ۳ پوښتنه تفصیلي پوښتنې','p297')
F=Flow(s)
Q(s,'q2','Q2. Give short answers of the following questions.','سوال ۲: درج ذیل سوالات کے مختصر جوابات دیں۔','۲ پوښتنه: د لاندې پوښتنو لنډ ځوابونه ورکړئ.')
for r,e,u,p in [('i','Name different types of database management systems.','ڈیٹا بیس مینجمنٹ سسٹمز کی مختلف اقسام کے نام بتائیں۔','د ډېټابېس مدیریت سیسټمونو د مختلفو ډولونو نومونه ووایئ.'),('ii','What is OpenOffice Base?','اوپن آفس بیس کیا ہے؟','اوپن آفس بیس څه دی؟'),('iii','How forms are useful in database?','ڈیٹا بیس میں فارمز کیسے مفید ہیں؟','فورمونه په ډېټابېس کې څنګه ګټور دي؟'),('iv','Name common Access database objects.','ایکسیس ڈیٹا بیس کے عام آبجیکٹس کے نام بتائیں۔','د Access ډېټابېس عام څیزونو نومونه ووایئ.'),('v','How primary key is assigned in a table?','ٹیبل میں پرائمری کی کیسے تفویض کی جاتی ہے؟','په جدول کې لومړنۍ کیلي څنګه ټاکل کېږي؟'),('vi','What is a report?','رپورٹ کیا ہے؟','راپور څه دی؟'),('vii','How relationship can be edited in Access.','ایکسیس میں تعلق میں ترمیم کیسے کی جا سکتی ہے۔','په Access کې اړیکه څنګه سمېدای شي.'),('viii','Name different navigation buttons in a form.','فارم میں مختلف نیویگیشن بٹنوں کے نام بتائیں۔','په فورم کې د لارښوونې مختلفې تڼۍ نومونه ووایئ.')]:
    QI(s,f's{r}',f'{r}. '+e,f'{r}۔ '+u,f'{r}. '+p,'q2')
Q(s,'q3','Q3. Give detailed answers of the following questions.','سوال ۳: درج ذیل سوالات کے تفصیلی جوابات دیں۔','۳ پوښتنه: د لاندې پوښتنو تفصیلي ځوابونه ورکړئ.')
QI(s,'t1','i. Explain the following database objects.','i۔ درج ذیل ڈیٹا بیس آبجیکٹس کی وضاحت کریں۔','i. لاندې د ډېټابېس څیزونه تشریح کړئ.','q3')
for r,e,u,p in [('a','Tables','ٹیبلز','جدولونه'),('b','Forms','فارمز','فورمونه'),('c','Queries','کوئریز','پوښتنې'),('d','Reports','رپورٹس','راپورونه')]:
    QI(s,f't1{r}',f'{r}) {e}',f'{r}) {u}',f'{r}) {p}','q3')
for r,e,u,p in [('ii','Explain different data types used in Access.','ایکسیس میں استعمال ہونے والی مختلف ڈیٹا ٹائپس کی وضاحت کریں۔','په Access کې کارېدونکي مختلف د ډېټا ډولونه تشریح کړئ.'),('iii','Describe two ways of creating a table in Access.','ایکسیس میں ٹیبل بنانے کے دو طریقے بیان کریں۔','په Access کې د جدول د جوړولو دوه لارې بیان کړئ.'),('iv','Explain the process of creating forms in Access.','ایکسیس میں فارمز بنانے کے عمل کی وضاحت کریں۔','په Access کې د فورمونو د جوړولو پروسه تشریح کړئ.'),('v','Write the steps for creating relationships between tables.','ٹیبلز کے درمیان تعلقات بنانے کے اقدامات لکھیں۔','د جدولونو ترمنځ د اړیکو د جوړولو ګامونه ولیکئ.'),('vi','Explain different types of queries used in Access.','ایکسیس میں استعمال ہونے والی کوئریز کی مختلف اقسام کی وضاحت کریں۔','په Access کې کارېدونکې د پوښتنو مختلف ډولونه تشریح کړئ.'),('vii','How can one-to-many relationship can be created between two tables? Give example.','دو ٹیبلز کے درمیان ایک سے کئی تعلق کیسے بنایا جا سکتا ہے؟ مثال دیں۔','د دوو جدولونو ترمنځ د یو-ته-ډیر اړیکه څنګه جوړېدای شي؟ بېلګه ورکړئ.'),('viii','What is a query? How query is created using wizard option in Access 2007?','کوئری کیا ہے؟ ایکسیس ۲۰۰۷ میں ویزرڈ آپشن استعمال کر کے کوئری کیسے بنائی جاتی ہے؟','پوښتنه څه ده؟ په Access 2007 کې د مرستندوي اختیار په کارولو پوښتنه څنګه جوړېږي؟')]:
    QI(s,f't{r}',f'{r}. '+e,f'{r}۔ '+u,f'{r}. '+p,'q3')
F.done()
fin(s,'Printed page 297: Q2 with eight short questions and Q3 with eight detailed questions of Unit 8 (question i has four sub-items a–d printed in two columns). The rest of the page is blank. Unit 8 ends here. The printed spelling “How can one-to-many relationship can be created” is kept.')
# ---------- scan 307 (printed 298) ----------
s=page(307,'back-matter','298','Answers to MCQs: Units 1–4','کثیر انتخابی سوالات کے جوابات: یونٹ ۱ تا ۴','د څو انتخابي پوښتنو ځوابونه: ۱ تر ۴ واحدونه','p298')
F=Flow(s)
H(s,'h','ANSWERS TO MCQs','کثیر انتخابی سوالات کے جوابات','د څو انتخابي پوښتنو ځوابونه')
H(s,'h1','Unit 1 OVERVIEW OF COMPUTER SYSTEM','یونٹ ۱ کمپیوٹر سسٹم کا جائزہ','۱ واحد د کمپیوټر سیسټم کتنه')
s['tables']=[at('Unit 1: Q.1 Multiple Choice Questions (i–x)','یونٹ ۱: سوال ۱ کثیر انتخابی سوالات (i تا x)','۱ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'BCCCDBAADC'),
 at('Unit 1: Q.1 Multiple Choice Questions (xi–xv)','یونٹ ۱: سوال ۱ کثیر انتخابی سوالات (xi تا xv)','۱ واحد: ۱ پوښتنه څو انتخابي پوښتنې (xi تر xv)',R5,'BBCAD')]
F.tb(0); F.tb(1)
H(s,'h2','Unit 2 COMPUTER MEMORY','یونٹ ۲ کمپیوٹر میموری','۲ واحد د کمپیوټر حافظه')
s['tables'].append(at('Unit 2: Q.1 Multiple Choice Questions (i–x)','یونٹ ۲: سوال ۱ کثیر انتخابی سوالات (i تا x)','۲ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'BCCADACBBC'))
F.tb(2)
H(s,'h3','Unit 3 CENTRAL PROCESSING UNIT','یونٹ ۳ مرکزی پراسیسنگ یونٹ','۳ واحد مرکزي پروسس واحد')
s['tables']+=[at('Unit 3: Q.1 Multiple Choice Questions (i–x)','یونٹ ۳: سوال ۱ کثیر انتخابی سوالات (i تا x)','۳ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'ABCBCAACAB'),at('Unit 3: Q.1 Multiple Choice Questions (xi–xv)','یونٹ ۳: سوال ۱ کثیر انتخابی سوالات (xi تا xv)','۳ واحد: ۱ پوښتنه څو انتخابي پوښتنې (xi تر xv)',R5,'BBAAD')]
F.tb(3); F.tb(4)
H(s,'h4','Unit 4 INSIDE SYSTEM UNIT','یونٹ ۴ سسٹم یونٹ کے اندر','۴ واحد د سیسټم واحد دننه')
s['tables'].append(at('Unit 4: Q.1 Multiple Choice Questions (i–x)','یونٹ ۴: سوال ۱ کثیر انتخابی سوالات (i تا x)','۴ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'BDDADCBACC'))
F.tb(5)
F.done()
fin(s,'Printed page 298: the heading “ANSWERS TO MCQs” and the answer tables of Unit 1 (i–x and xi–xv), Unit 2 (i–x), Unit 3 (i–x and xi–xv) and Unit 4 (i–x); each answer is a single letter A–D under the question number. The left edge of the scan is dark and the answer letters are read from a slightly slanted print; answers marked with a stray dot (for example “A`” and “C.”) are read as the letter.')
# ---------- scan 308 (printed 299) ----------
s=page(308,'back-matter','299','Answers to MCQs: Units 5–8','کثیر انتخابی سوالات کے جوابات: یونٹ ۵ تا ۸','د څو انتخابي پوښتنو ځوابونه: ۵ تر ۸ واحدونه','p299')
F=Flow(s)
H(s,'h1','Unit 5 NETWORK COMMUNICATION AND PROTOCOLS','یونٹ ۵ نیٹ ورک کمیونیکیشن اور پروٹوکولز','۵ واحد د شبکې اړیکې او پروتوکولونه')
s['tables']=[at('Unit 5: Q.1 Multiple Choice Questions (i–x)','یونٹ ۵: سوال ۱ کثیر انتخابی سوالات (i تا x)','۵ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'BCADBCDBAC'),at('Unit 5: Q.1 Multiple Choice Questions (xi–xv)','یونٹ ۵: سوال ۱ کثیر انتخابی سوالات (xi تا xv)','۵ واحد: ۱ پوښتنه څو انتخابي پوښتنې (xi تر xv)',R5,'DDCDC')]
F.tb(0); F.tb(1)
H(s,'h2','Unit 6 WIRELESS COMMUNICATIONS','یونٹ ۶ وائرلیس کمیونیکیشنز','۶ واحد بې سیمې اړیکې')
s['tables'].append(at('Unit 6: Q.1 Multiple Choice Questions (i–x)','یونٹ ۶: سوال ۱ کثیر انتخابی سوالات (i تا x)','۶ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'ABBADDCBAD'))
F.tb(2)
H(s,'h3','Unit 7 DATABASE FUNDAMENTALS','یونٹ ۷ ڈیٹا بیس کے بنیادی اصول','۷ واحد د ډېټابېس بنسټیز اصول')
s['tables'].append(at('Unit 7: Q.1 Multiple Choice Questions (i–x)','یونٹ ۷: سوال ۱ کثیر انتخابی سوالات (i تا x)','۷ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر x)',R10,'ACACCABCCB'))
F.tb(3)
H(s,'h4','Unit 8 DATABASE DEVELOPMENT','یونٹ ۸ ڈیٹا بیس ڈیولپمنٹ','۸ واحد د ډېټابېس جوړونه')
s['tables'].append(at('Unit 8: Q.1 Multiple Choice Questions (i–viii)','یونٹ ۸: سوال ۱ کثیر انتخابی سوالات (i تا viii)','۸ واحد: ۱ پوښتنه څو انتخابي پوښتنې (i تر viii)',R8,'ABDBCDDD'))
F.tb(4)
F.done()
fin(s,'Printed page 299: the answer tables of Unit 5 (i–x and xi–xv), Unit 6 (i–x), Unit 7 (i–x) and Unit 8 (i–viii); each answer is a single letter A–D under the question number. The running head reads “Answers”. A stray dot after the first answer of Unit 8 is read as the letter.')
