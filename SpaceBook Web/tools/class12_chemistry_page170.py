"""PDF170 printed334–335: Unit 22 Q3 3–5 and Project; Unit 23 Environmental Chemistry opener and learning outcomes."""
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
lines([('3. (a). What are adhesives? Classify the adhesives on the basis of origin and reactiveness.','3. (a). چپکنے والے مادے کیا ہیں؟ ماخذ اور تعامل پذیری کی بنیاد پر چپکنے والے مادوں کی درجہ بندی کریں۔','3. (a). سرېښونه څه دي؟ د سرچینې او تعامل وړتیا پر بنسټ سرېښونه ډلبندي کړئ.'),
 ('(b). Discuss the importance of adhesive in our daily life.','(b). ہماری روزمرہ زندگی میں چپکنے والے مادوں کی اہمیت پر بحث کریں۔','(b). زموږ په ورځني ژوند کې د سرېښونو اهمیت وڅېړئ.'),
 ('4. (a). Write down the raw materials in Pakistan for various chemical and petrochemical industries.','4. (a). مختلف کیمیائی اور پیٹرو کیمیکل صنعتوں کے لیے پاکستان میں خام مال لکھیں۔','4. (a). د بېلابېلو کیمیاوي او پټرو کیمیکل صنعتونو لپاره په پاکستان کې خام مواد ولیکئ.'),
 ('(b). Discuss the Safety Considerations in Process Industries in detail.','(b). عمل کی صنعتوں میں حفاظتی امور پر تفصیل سے بحث کریں۔','(b). د پروسس په صنعتونو کې د خوندیتوب ملاحظات په تفصیل وڅېړئ.'),
 ('5. (a). Explain the fractional distillation of petroleum.','5. (a). پیٹرولیم کی جزوی کشید کی وضاحت کریں۔','5. (a). د پټرولیم جزوي تقطیر تشریح کړئ.'),
 ('(b). Discuss in detail the importance of the chemical industries in the economy of Pakistan.','(b). پاکستان کی معیشت میں کیمیائی صنعتوں کی اہمیت پر تفصیل سے بحث کریں۔','(b). د پاکستان په اقتصاد کې د کیمیاوي صنعتونو اهمیت په تفصیل وڅېړئ.')])
add('Project','پروجیکٹ','پروژه','heading')
add('Use the library or internet to research the petrochemicals. Write a newspaper article about petrochemicals. Make sure that the following questions are answered in the article.','پیٹرو کیمیکلز پر تحقیق کے لیے لائبریری یا انٹرنیٹ استعمال کریں۔ پیٹرو کیمیکلز کے بارے میں اخباری مضمون لکھیں۔ یقینی بنائیں کہ مضمون میں درج ذیل سوالات کے جواب دیے گئے ہوں۔','د پټرو کیمیکلونو د څېړنې لپاره کتابتون یا انټرنیټ وکاروئ. د پټرو کیمیکلونو په اړه د ورځپاڼې مقاله ولیکئ. ډاډ ترلاسه کړئ چې په مقاله کې د لاندې پوښتنو ځوابونه ورکړل شوي.')
lines([('1. What are the origin of petroleum?','1. پیٹرولیم کا ماخذ کیا ہے؟','1. د پټرولیم سرچینه څه ده؟'),('2. How petroleum is refined? Also, give a touch to the different fractions.','2. پیٹرولیم کیسے صاف کیا جاتا ہے؟ مختلف اجزا کا بھی ذکر کریں۔','2. پټرولیم څنګه تصفیه کېږي؟ بېلابېلو برخو ته هم اشاره وکړئ.'),
 ('3. How petrochemicals are produced?','3. پیٹرو کیمیکلز کیسے تیار ہوتے ہیں؟','3. پټرو کیمیکلونه څنګه تولیدېږي؟'),('4. Write down the names of some famous petrochemicals.','4. چند مشہور پیٹرو کیمیکلز کے نام لکھیں۔','4. د ځینو مشهورو پټرو کیمیکلونو نومونه ولیکئ.'),
 ('5. What are the functions of petrochemicals?','5. پیٹرو کیمیکلز کے افعال کیا ہیں؟','5. د پټرو کیمیکلونو دندې څه دي؟'),('6. Why the petrochemicals are so much important in our life?','6. پیٹرو کیمیکلز ہماری زندگی میں اتنے اہم کیوں ہیں؟','6. پټرو کیمیکلونه زموږ په ژوند کې دومره مهم ولې دي؟')])
r14=section('22.14','Unit 22 exercise: detailed questions 3–5 and Project','یونٹ 22 مشق: تفصیلی سوالات 3–5 اور پروجیکٹ','د 22 واحد تمرین: مفصلې پوښتنې 3–5 او پروژه',P,L,[],'334')
r14['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':170,'printedPages':[334]}]
P,L,B,add,lines=builder()
add('Unit 23 — Environmental Chemistry','یونٹ 23 — ماحولیاتی کیمیا','23 واحد — چاپېریالي کیمیا','heading')
tb={'id':'chem12-unit23-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['9','1','6']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['9','1','6']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['9','1','6']]}]}
B.append(tb);L.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
lines([('Recognize various chemical reactions, occurring in the atmosphere. (Understanding)','فضا میں ہونے والے مختلف کیمیائی تعاملات کو پہچانیں۔ (سمجھنا)','په اتموسفیر کې د پېښېدونکو بېلابېلو کیمیاوي تعاملونو پېژندنه. (پوهېدل)'),
 ('Recognize that the release of COₓ, SOₓ, NOₓ, VOCs are associated with the combustion of hydrocarbon-based fuels. (Applying)','پہچانیں کہ COₓ، SOₓ، NOₓ اور VOCs کا اخراج ہائیڈروکاربن پر مبنی ایندھنوں کے جلنے سے وابستہ ہے۔ (اطلاق)','وپېژني چې د COₓ، SOₓ، NOₓ او VOCs خوشې کېدل د هایدروکاربن پر بنسټ سونګ توکو له سوځېدو سره تړلي دي. (تطبیق)'),
 ('Outline problems associated with release of pollutants, including acid rain and the formation by free radical reactions of hazardous inorganic and organic compounds e.g PAN. (Analyzing)','آلودگیوں کے اخراج سے وابستہ مسائل کا خاکہ پیش کریں، بشمول تیزابی بارش اور آزاد ریڈیکل تعاملات سے خطرناک غیر نامیاتی اور نامیاتی مرکبات مثلاً PAN کا بننا۔ (تجزیہ)','د ککړوونکو له خوشې کېدو سره تړلې ستونزې په لنډ ډول وړاندې کړي، په ګډون د تېزابي بارانونو او د ازادو رادیکالونو د تعاملونو په واسطه د خطرناکو غیر عضوي او عضوي مرکباتو لکه PAN جوړېدل. (تحلیل)'),
 ('Describe causes and impacts of urban smog. (Analyzing)','شہری سموگ کی وجوہات اور اثرات بیان کریں۔ (تجزیہ)','د ښاري سموګ لاملونه او اغېزې بیان کړي. (تحلیل)'),
 ('Explain greenhouse effect and global warming as resulting in climate change. (Analyzing)','گرین ہاؤس اثر اور عالمی حدت کی وضاحت کریں جس کا نتیجہ موسمیاتی تبدیلی ہے۔ (تجزیہ)','د شنه خونې اغېز او نړیواله تودوخه چې د اقلیم د بدلون پایله لري تشریح کړي. (تحلیل)'),
 ('Explain the build-up and recognize the adverse effects of ozone in the troposphere. (Applying)','ٹروپوسفیئر میں اوزون کے جمع ہونے کی وضاحت کریں اور اس کے مضر اثرات کو پہچانیں۔ (اطلاق)','په ټروپوسفیر کې د اوزون راټولېدل تشریح کړي او ناوړه اغېزې یې وپېژني. (تطبیق)'),
 ('Describe the role of CFCs in destroying ozone in the stratosphere. (Applying)','سٹریٹوسفیئر میں اوزون کو تباہ کرنے میں CFCs کا کردار بیان کریں۔ (اطلاق)','په سټراټوسفیر کې د اوزون په ویجاړولو کې د CFCs رول بیان کړي. (تطبیق)'),
 ('Describe the role of ozone in the stratosphere in reducing the intensity of harmful UV radiation reaching the Earth. (Understanding)','زمین تک پہنچنے والی نقصان دہ UV شعاعوں کی شدت کم کرنے میں سٹریٹوسفیئر میں اوزون کا کردار بیان کریں۔ (سمجھنا)','ځمکې ته د رسېدونکو زیانمنو UV وړانګو د شدت په کمولو کې په سټراټوسفیر کې د اوزون رول بیان کړي. (پوهېدل)'),
 ('List possible alternatives to the use of CFCs. (Applying)','CFCs کے استعمال کے ممکنہ متبادلات کی فہرست بنائیں۔ (اطلاق)','د CFCs د کارونې ممکنه بدیلونه لیست کړي. (تطبیق)'),
 ('Recognize and describe various water pollutants. (Applying)','پانی کی مختلف آلودگیوں کو پہچانیں اور بیان کریں۔ (اطلاق)','د اوبو بېلابېل ککړوونکي وپېژني او بیان یې کړي. (تطبیق)'),
 ('Explain the various parameters of water analysis. (Applying)','پانی کے تجزیے کے مختلف پیمانوں کی وضاحت کریں۔ (اطلاق)','د اوبو د تحلیل بېلابېل پارامترونه تشریح کړي. (تطبیق)')],'list')
r23=section('chem12-u23-opening','Unit 23 opener and learning outcomes','یونٹ 23 کا آغاز اور تعلیمی نتائج','د 23 واحد پیل او د زده کړې پایلې',P,L,B,'335')
r23['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':170,'printedPages':[335]}];r23['sourceChapterNumber']=23;r23['insertBefore']='23.1'
r23['sourceCoverIllustrationReview']='Cover laboratory/plant photograph and greenhouse-effect artwork are decorative; not reproduced.'
trim=[{'id':'23.1','sourceChapterNumber':23,'startsAt':'Introduction\nNOT FOR SA'}]
if __name__=='__main__':save(170,[r14,r23],trim=trim,chapter_number=22)
