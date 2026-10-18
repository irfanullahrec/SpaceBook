"""PDF157 printed308–309: Unit 21 exercise Q3 3–6 and Project; Unit 22 Industrial Chemistry opener and learning outcomes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows,kind='lines'):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':kind,'indices':list(range(s0,len(P)))})
 return P,L,B,add,lines
P,L,B,add,lines=builder()
lines([('3. (a). What are lipids? Explain the basis of classification of lipids.','3. (a). لپڈز کیا ہیں؟ لپڈز کی درجہ بندی کی بنیاد کی وضاحت کریں۔','3. (a). لیپیډونه څه دي؟ د لیپیډونو د ډلبندۍ اساس تشریح کړئ.'),
 ('(b). Discuss in detail the structure and nutritional and biological importance of lipids.','(b). لپڈز کی ساخت اور غذائی و حیاتیاتی اہمیت پر تفصیل سے بحث کریں۔','(b). د لیپیډونو جوړښت او غذايي او بیولوژیکي اهمیت په تفصیل سره وڅېړئ.'),
 ('4. (a). Explain the role of inhibitors of enzyme catalysed reactions.','4. (a). خامروں سے عمل انگیز تعاملات کے روکنے والوں کے کردار کی وضاحت کریں۔','4. (a). د انزایمي کتلستي تعاملونو د مخنیوونکو رول تشریح کړئ.'),
 ('(b). Identify the different structural components of DNA and RNA.','(b). DNA اور RNA کے مختلف ساختی اجزا کی شناخت کریں۔','(b). د DNA او RNA بېلابېلې جوړښتي برخې وپېژنئ.'),
 ('5. (a). Assess the role of enzyme as biocatalyst and relate this role to various functions such as digestion of food.','5. (a). حیاتی عمل انگیز کے طور پر خامرے کے کردار کا جائزہ لیں اور اس کردار کو خوراک کے ہضم جیسے مختلف افعال سے منسلک کریں۔','5. (a). د ژوندي کتلست په توګه د انزایم رول وارزوئ او دا رول د خوړو د هضم په څېر له بېلابېلو دندو سره وتړئ.'),
 ('(b). Evaluate the factors that affect enzyme activity such as effect of temperature and pH.','(b). خامرے کی سرگرمی پر اثر انداز ہونے والے عوامل جیسے درجہ حرارت اور pH کے اثر کا جائزہ لیں۔','(b). هغه عوامل وارزوئ چې د انزایم پر فعالیت اغېز کوي لکه د تودوخې او pH اغېز.'),
 ('6. (a). Why zinc is important for human being?','6. (a). زنک انسان کے لیے کیوں اہم ہے؟','6. (a). جست د انسان لپاره ولې مهم دی؟'),
 ('(b). State the medical problems that may relate to calcium and phosphorus.','(b). کیلشیم اور فاسفورس سے متعلق ہو سکنے والے طبی مسائل بیان کریں۔','(b). هغه طبي ستونزې بیان کړئ چې کېدای شي له کلسیم او فاسفورس سره تړاو ولري.')])
add('Project','پروجیکٹ','پروژه','heading')
add('Take 250cm³ milk in a beaker. Gently warm the milk (not boil), add small amount of lemon juice or vinegar (acetic acid) in it and observe it. Report your observation by answering the following questions.','ایک بیکر میں 250cm³ دودھ لیں۔ دودھ کو ہلکا گرم کریں (ابالیں نہیں)، اس میں لیموں کا رس یا سرکہ (ایسیٹک ایسڈ) تھوڑی مقدار میں ڈالیں اور مشاہدہ کریں۔ درج ذیل سوالات کے جوابات دے کر اپنا مشاہدہ بیان کریں۔','په یوه بیکر کې 250cm³ شیدې واخلئ. شیدې ورو تودې کړئ (مه یې ایشوئ)، لږ مقدار د لیمو اوبه یا سرکه (اسیټیک اسید) ورګډې کړئ او وګورئ. د لاندې پوښتنو په ځوابولو خپله کتنه راپور کړئ.')
lines([('1. What happen to the state of the milk?','1. دودھ کی حالت کو کیا ہوتا ہے؟','1. د شیدو حالت ته څه کېږي؟'),('2. Is there any chemical change occur in it?','2. کیا اس میں کوئی کیمیائی تبدیلی ہوتی ہے؟','2. ایا پکې کوم کیمیاوي بدلون راځي؟'),
 ('3. Does the change in pH affect the milk?','3. کیا pH کی تبدیلی دودھ پر اثر کرتی ہے؟','3. ایا د pH بدلون پر شیدو اغېز کوي؟'),('4. Name the product obtained during the process.','4. عمل کے دوران حاصل ہونے والی پیداوار کا نام بتائیں۔','4. د عملیې پر مهال د ترلاسه شوي محصول نوم واخلئ.'),
 ('5. Is this product has any nutritional importance?','5. کیا اس پیداوار کی کوئی غذائی اہمیت ہے؟','5. ایا دا محصول کوم غذايي اهمیت لري؟'),('6. Name some products in which it is used.','6. چند ایسی مصنوعات کے نام بتائیں جن میں یہ استعمال ہوتی ہے۔','6. ځینې هغه محصولات ونوموئ چې پکې کارېږي.')])
r21=section('21.21','Unit 21 exercise: detailed questions 3–6 and Project','یونٹ 21 مشق: تفصیلی سوالات 3–6 اور پروجیکٹ','د 21 واحد تمرین: مفصلې پوښتنې 3–6 او پروژه',P,L,[],'308')
r21['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':157,'printedPages':[308]}]
P,L,B,add,lines=builder()
add('Unit 22 — Industrial chemistry','یونٹ 22 — صنعتی کیمیا','22 واحد — صنعتي کیمیا','heading')
tb={'id':'chem12-unit22-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['8','1','6']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['8','1','6']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['8','1','6']]}]}
B.append(tb);L.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
lines([('Discuss the importance of the chemical industries in the economy of Pakistan. (Analysing)','پاکستان کی معیشت میں کیمیائی صنعتوں کی اہمیت پر بحث کریں۔ (تجزیہ)','د پاکستان په اقتصاد کې د کیمیاوي صنعتونو پر اهمیت بحث وکړي. (تحلیل)'),
 ('Describe the raw materials available in Pakistan for various chemical industries. (Applying)','مختلف کیمیائی صنعتوں کے لیے پاکستان میں دستیاب خام مال بیان کریں۔ (اطلاق)','د بېلابېلو کیمیاوي صنعتونو لپاره په پاکستان کې شته خام مواد بیان کړي. (تطبیق)'),
 ('Describe the chemical processes of addition and condensation polymerization. (Understanding)','اضافی اور تکثیفی پولیمرائزیشن کے کیمیائی عمل بیان کریں۔ (سمجھنا)','د اضافي او تکثیفي پولیمرایزېشن کیمیاوي عملیې بیان کړي. (پوهېدل)'),
 ('Interpret difference between petrochemical and chemicals derived from them. (Understanding)','پیٹرو کیمیکل اور ان سے ماخوذ کیمیکلز میں فرق کی تشریح کریں۔ (سمجھنا)','د پټرو کیمیکل او له هغو څخه د اخیستل شویو کیمیکلونو ترمنځ توپیر تفسیر کړي. (پوهېدل)'),
 ('Describe the fractional distillation and refining of Petroleum (Understanding)','پیٹرولیم کی جزوی کشید اور صفائی بیان کریں (سمجھنا)','د پټرولیم جزوي تقطیر او تصفیه بیان کړي (پوهېدل)'),
 ('List the various raw materials for Petrochemical industry. (Analysing)','پیٹرو کیمیکل صنعت کے مختلف خام مال کی فہرست بنائیں۔ (تجزیہ)','د پټرو کیمیکل صنعت لپاره بېلابېل خام مواد لیست کړي. (تحلیل)'),
 ('Identify the important fractions. (Analysing)','اہم اجزا (فریکشنز) کی شناخت کریں۔ (تجزیہ)','مهمې برخې (فرکشنونه) وپېژني. (تحلیل)'),
 ('Describe the basic building block processes in Petrochemical technology. (Understanding)','پیٹرو کیمیکل ٹیکنالوجی میں بنیادی تعمیری عمل بیان کریں۔ (سمجھنا)','په پټرو کیمیکل ټکنالوژي کې بنسټیزې جوړونکې عملیې بیان کړي. (پوهېدل)'),
 ('Describe the Petrochemical process technology. (Understanding)','پیٹرو کیمیکل عمل کی ٹیکنالوجی بیان کریں۔ (سمجھنا)','د پټرو کیمیکل عملیې ټکنالوژي بیان کړي. (پوهېدل)'),
 ('List some major petrochemicals. (Applying)','چند بڑے پیٹرو کیمیکلز کی فہرست بنائیں۔ (اطلاق)','ځینې لوی پټرو کیمیکلونه لیست کړي. (تطبیق)'),
 ('Discuss types and applications of hair dyes. (Applying)','بالوں کے رنگوں کی اقسام اور استعمالات پر بحث کریں۔ (اطلاق)','د وېښتو د رنګونو ډولونه او کارونې وڅېړي. (تطبیق)'),
 ('Describe the formation and uses of PVC and Nylon. (Applying)','PVC اور نائیلون کی تشکیل اور استعمالات بیان کریں۔ (اطلاق)','د PVC او نایلون جوړښت او کارونې بیان کړي. (تطبیق)'),
 ('Describe preparation and applications of various cosmetics like nail varnish, nail polish remover and lipsticks. (Understanding)','نیل وارنش، نیل پالش ریموور اور لپ اسٹک جیسی مختلف کاسمیٹکس کی تیاری اور استعمالات بیان کریں۔ (سمجھنا)','د بېلابېلو سینګار توکو لکه د نوکانو وارنیش، د نوکانو پالش لرې کوونکي او لپسټکونو چمتو کول او کارونې بیان کړي. (پوهېدل)'),
 ('Describe types and applications of synthetic adhesives. (Understanding)','مصنوعی چپکنے والے مادوں کی اقسام اور استعمالات بیان کریں۔ (سمجھنا)','د مصنوعي سرېښونو ډولونه او کارونې بیان کړي. (پوهېدل)')],'list')
r22=section('chem12-u22-opening','Unit 22 opener and learning outcomes','یونٹ 22 کا آغاز اور تعلیمی نتائج','د 22 واحد پیل او د زده کړې پایلې',P,L,B,'309')
r22['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':157,'printedPages':[309]}];r22['sourceChapterNumber']=22;r22['insertBefore']='22.1'
r22['sourceCoverIllustrationReview']='Cover laboratory-glassware and refinery photographs are decorative; not reproduced.'
trim=[{'id':'22.1','sourceChapterNumber':22,'startsAt':'Introduction\nNOT FOR SALE'}]
if __name__=='__main__':save(157,[r21,r22],trim=trim,chapter_number=21)
