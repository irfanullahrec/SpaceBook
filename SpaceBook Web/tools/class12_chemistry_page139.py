"""PDF139 printed272–273: Unit 21 Biochemistry opener, learning outcomes, introduction, Figure 21.1, start of 21.1 Carbohydrates."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow139');t=F.t;line=F.line
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows,kind='lines'):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':kind,'indices':list(range(s0,len(P)))})
 def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
 return P,L,B,add,lines,visual
N={'BIOCHEMICAL':('حیاتی کیمیائی','ژوندکیمیاوي'),'SUBSTANCES':('مادے','مواد'),'BIOINORGANIC':('حیاتی غیر نامیاتی','ژوندي غیر عضوي'),'BIOORGANIC':('حیاتی نامیاتی','ژوندي عضوي'),
   'Substances that do':('وہ مادے جن میں','هغه مواد چې'),'not contain carbon':('کاربن نہیں ہوتا','کاربن نه لري'),'Substances that':('وہ مادے جن میں','هغه مواد چې'),'contain carbon':('کاربن ہوتا ہے','کاربن لري'),
   'Water (about 70%)':('پانی (تقریباً 70%)','اوبه (نږدې 70%)'),'Inorganic salts (about 5%)':('غیر نامیاتی نمکیات (تقریباً 5%)','غیر عضوي مالګې (نږدې 5%)'),'Proteins (about 15%)':('پروٹینز (تقریباً 15%)','پروټینونه (نږدې 15%)'),
   'Lipids (about 7%)':('لپڈز (تقریباً 7%)','لیپیډونه (نږدې 7%)'),'Carbohydrates (about 2%)':('کاربوہائیڈریٹس (تقریباً 2%)','کاربوهایدرېټونه (نږدې 2%)'),'Nucleic acids (about 1%)':('نیوکلک ایسڈز (تقریباً 1%)','نیوکلیک اسیدونه (نږدې 1%)')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def box(x,y,w,h,a,b=None,fill='#e8f5e9'):
 s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#2e7d32" stroke-width="1.5"/>'
 return s+(t(x+w/2,y+h/2-3,a,12)+t(x+w/2,y+h/2+13,b,12) if b else t(x+w/2,y+h/2+5,a,12))
def fig(lang):
 s=F.start(300)+box(20,120,150,50,lb(lang,'BIOCHEMICAL'),lb(lang,'SUBSTANCES'),'#fce4ec')
 s+=box(250,20,170,42,lb(lang,'BIOINORGANIC'),lb(lang,'SUBSTANCES'))+box(250,62,170,42,lb(lang,'Substances that do'),lb(lang,'not contain carbon'),'#fff')
 s+=box(250,160,170,42,lb(lang,'BIOORGANIC'),lb(lang,'SUBSTANCES'))+box(250,202,170,42,lb(lang,'Substances that'),lb(lang,'contain carbon'),'#fff')
 s+=line(170,145,210,145)+line(210,62,210,202)+line(210,62,250,62)+line(210,202,250,202)
 right=[('Water (about 70%)',20),('Inorganic salts (about 5%)',70),('Proteins (about 15%)',130),('Lipids (about 7%)',180),('Carbohydrates (about 2%)',230),('Nucleic acids (about 1%)',280)]
 s+=line(420,41,460,41)+line(460,30,460,80)+line(420,181,460,181)+line(460,130,460,280)
 for v,y in right:s+=line(460,y+10 if y<100 else y,500,y+10 if y<100 else y)+box(500,(y-8 if y<100 else y-18),220,32,lb(lang,v))
 return s.replace('viewBox="0 0 850 300"','viewBox="0 0 850 310"')+'</svg>'

P,L,B,add,lines,visual=builder()
add('Unit 21 — Biochemistry','یونٹ 21 — حیاتی کیمیا','21 واحد — ژوندکیمیا','heading')
tb={'id':'chem12-unit21-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['6','1','6']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['6','1','6']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['6','1','6']]}]}
B.append(tb);L.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
lines([('Explain the basis of classification and structure-function relationship of carbohydrates. (Understanding)','کاربوہائیڈریٹس کی درجہ بندی کی بنیاد اور ساخت–فعل کے تعلق کی وضاحت کریں۔ (سمجھنا)','د کاربوهایدرېټونو د ډلبندۍ اساس او د جوړښت–دندې اړیکه تشریح کړي. (پوهېدل)'),
 ('Explain the role of various Carbohydrates in health and diseases. (Understanding)','صحت اور بیماریوں میں مختلف کاربوہائیڈریٹس کے کردار کی وضاحت کریں۔ (سمجھنا)','په روغتیا او ناروغیو کې د بېلابېلو کاربوهایدرېټونو رول تشریح کړي. (پوهېدل)'),
 ('Identify the nutritional importance and their role as energy storage. (Applying)','ان کی غذائی اہمیت اور توانائی ذخیرہ کرنے میں ان کے کردار کی شناخت کریں۔ (اطلاق)','د هغوی غذايي اهمیت او د انرژۍ د زېرمه کولو رول وپېژني. (تطبیق)'),
 ('Explain the basis of classification and structure-function relationship of proteins. (Understanding)','پروٹینز کی درجہ بندی کی بنیاد اور ساخت–فعل کے تعلق کی وضاحت کریں۔ (سمجھنا)','د پروټینونو د ډلبندۍ اساس او د جوړښت–دندې اړیکه تشریح کړي. (پوهېدل)'),
 ('Describe the role of various proteins in maintaining body functions and their nutritional importance. (Applying)','جسمانی افعال برقرار رکھنے میں مختلف پروٹینز کے کردار اور ان کی غذائی اہمیت بیان کریں۔ (اطلاق)','د بدن د دندو په ساتلو کې د بېلابېلو پروټینونو رول او د هغوی غذايي اهمیت بیان کړي. (تطبیق)'),
 ('Describe the role of enzymes as biocatalyst and relate this role to various functions such as digestion of food. (Applying)','حیاتی عمل انگیز کے طور پر خامروں کا کردار بیان کریں اور اس کردار کو خوراک کے ہضم جیسے مختلف افعال سے منسلک کریں۔ (اطلاق)','د ژوندي کتلست په توګه د انزایمونو رول بیان کړي او دا رول د خوړو د هضم په څېر له بېلابېلو دندو سره وتړي. (تطبیق)'),
 ('Identify factors that affect enzymes activity such as effect of temperature and pH. (Understanding)','خامروں کی سرگرمی پر اثر انداز ہونے والے عوامل جیسے درجہ حرارت اور pH کے اثر کی شناخت کریں۔ (سمجھنا)','هغه عوامل وپېژني چې د انزایمونو پر فعالیت اغېز کوي، لکه د تودوخې او pH اغېز. (پوهېدل)'),
 ('Explain the role of inhibitors of enzyme catalysed reactions. (Understanding)','خامروں سے عمل انگیز تعاملات کے روکنے والوں کے کردار کی وضاحت کریں۔ (سمجھنا)','د انزایمي کتلستي تعاملونو د مخنیوونکو رول تشریح کړي. (پوهېدل)'),
 ('Describe the basis of classification and structure-function relationship of lipids. (Applying)','لپڈز کی درجہ بندی کی بنیاد اور ساخت–فعل کا تعلق بیان کریں۔ (اطلاق)','د لیپیډونو د ډلبندۍ اساس او د جوړښت–دندې اړیکه بیان کړي. (تطبیق)'),
 ('Identify the nutritional and Biological importance of lipids. (Applying)','لپڈز کی غذائی اور حیاتیاتی اہمیت کی شناخت کریں۔ (اطلاق)','د لیپیډونو غذايي او بیولوژیکي اهمیت وپېژني. (تطبیق)'),
 ('Identify the structural components of DNA and RNA. (Applying)','DNA اور RNA کے ساختی اجزا کی شناخت کریں۔ (اطلاق)','د DNA او RNA جوړښتي برخې وپېژني. (تطبیق)'),
 ('Recognize the structural differences between DNA polymer (double strand) and RNA (Single strand). (Understanding)','DNA پولیمر (دوہری لڑی) اور RNA (اکہری لڑی) کے ساختی فرق کو پہچانیں۔ (سمجھنا)','د DNA پولیمر (دوه تاري) او RNA (یو تاري) ترمنځ جوړښتي توپیرونه وپېژني. (پوهېدل)'),
 ('Relate DNA sequences to its function as storage of genetic information. (Applying)','DNA ترتیبوں کو جینیاتی معلومات کے ذخیرے کے طور پر اس کے فعل سے منسلک کریں۔ (اطلاق)','د DNA ترتیبونه د جنیټیکي معلوماتو د زېرمې په توګه له دندې سره وتړي. (تطبیق)'),
 ('Relate RNA sequence (transcript) to its role in transfer of information to protein (Translation). (Applying)','RNA ترتیب (ٹرانسکرپٹ) کو پروٹین تک معلومات کی منتقلی (ٹرانسلیشن) میں اس کے کردار سے منسلک کریں۔ (اطلاق)','د RNA ترتیب (ټرانسکرېپټ) پروټین ته د معلوماتو په لېږد (ټرانسلېشن) کې له رول سره وتړي. (تطبیق)'),
 ('Identify the sources of minerals such as iron, calcium, phosphorous and zinc. (Applying)','لوہے، کیلشیم، فاسفورس اور زنک جیسی معدنیات کے ذرائع کی شناخت کریں۔ (اطلاق)','د اوسپنې، کلسیم، فاسفورس او جستو په څېر د منرالونو سرچینې وپېژني. (تطبیق)'),
 ('Describe the role of iron, calcium, phosphorous and zinc in nutrition. (Applying)','غذائیت میں لوہے، کیلشیم، فاسفورس اور زنک کا کردار بیان کریں۔ (اطلاق)','په تغذیه کې د اوسپنې، کلسیم، فاسفورس او جستو رول بیان کړي. (تطبیق)')],'list')
r0=section('chem12-u21-opening','Unit 21 opener and learning outcomes','یونٹ 21 کا آغاز اور تعلیمی نتائج','د 21 واحد پیل او د زده کړې پایلې',P,L,B,'272')
r0['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':139,'printedPages':[272]}];r0['insertBefore']='21.1'
r0['sourceCoverIllustrationReview']='Cover DNA double-helix photograph is decorative; not reproduced.'

P,L,B,add,lines,visual=builder()
add('Introduction','تعارف','پېژندنه','heading')
add('Biochemistry is the study of the chemical substances found in living organisms and the chemical interactions of these substances with one another. Living organisms consist primarily of the elements carbon, hydrogen, oxygen and nitrogen. Many other elements such as sulphur and phosphorus are essential to life but they do not comprise a large portion of living organism.','حیاتی کیمیا جانداروں میں پائے جانے والے کیمیائی مادوں اور ان مادوں کے ایک دوسرے سے کیمیائی تعاملات کا مطالعہ ہے۔ جاندار بنیادی طور پر کاربن، ہائیڈروجن، آکسیجن اور نائٹروجن عناصر پر مشتمل ہوتے ہیں۔ سلفر اور فاسفورس جیسے بہت سے دوسرے عناصر زندگی کے لیے ضروری ہیں لیکن یہ جاندار کا بڑا حصہ نہیں بناتے۔','ژوندکیمیا په ژوندیو موجوداتو کې د موندل شویو کیمیاوي موادو او له یو بل سره د دغو موادو د کیمیاوي تعاملونو مطالعه ده. ژوندي موجودات په اصل کې له کاربن، هایدروجن، اکسیجن او نایټروجن عناصرو جوړ دي. ډېر نور عناصر لکه سلفر او فاسفورس د ژوند لپاره اړین دي خو د ژوندي موجود لویه برخه نه جوړوي.')
add('Elements combine to form the molecules that make up living cells. The substances that are associated with life are called biochemical substances. Biochemical substances are divided into two groups: Figure 21.1 gives an approximate mass composition for the human body in terms of types of biochemical substances present.','عناصر مل کر وہ سالمات بناتے ہیں جن سے زندہ خلیے بنتے ہیں۔ زندگی سے وابستہ مادوں کو حیاتی کیمیائی مادے کہتے ہیں۔ حیاتی کیمیائی مادے دو گروہوں میں تقسیم ہیں: شکل 21.1 موجود حیاتی کیمیائی مادوں کی اقسام کے لحاظ سے انسانی جسم کی تقریبی کمیتی ترکیب دکھاتی ہے۔','عناصر یو ځای کېږي او هغه مالیکولونه جوړوي چې ژوندي حجرې ترې جوړېږي. هغه مواد چې له ژوند سره تړلي دي ژوندکیمیاوي مواد بلل کېږي. ژوندکیمیاوي مواد په دوو ډلو وېشل کېږي: شکل 21.1 د شته ژوندکیمیاوي موادو د ډولونو له مخې د انسان د بدن نږدې کتلوي ترکیب ښيي.')
visual('chem12-figure21-1',fig)
add('Figure 21.1 Classification of biochemical substances.','شکل 21.1 حیاتی کیمیائی مادوں کی درجہ بندی۔','شکل 21.1 د ژوندکیمیاوي موادو ډلبندي.')
add('In grade–X, you have learnt the basics of biochemistry. In this unit, you will study in detail the concepts of biochemistry, biomolecules their structure and nutritional importance.','جماعت دہم میں آپ حیاتی کیمیا کی بنیادی باتیں سیکھ چکے ہیں۔ اس یونٹ میں آپ حیاتی کیمیا کے تصورات، حیاتی سالمات، ان کی ساخت اور غذائی اہمیت کا تفصیل سے مطالعہ کریں گے۔','په لسم ټولګي کې تاسو د ژوندکیمیا بنسټونه زده کړي. په دې واحد کې به تاسو د ژوندکیمیا مفاهیم، ژوندي مالیکولونه، د هغوی جوړښت او غذايي اهمیت په تفصیل سره ولولئ.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Bioorganic molecules make up only about one-fourth of body mass. The bioinorganic substance (water) constitutes over two-third of the mass of the human body, and another 4%–5% of body mass comes from inorganic salts.','حیاتی نامیاتی سالمات جسم کی کمیت کا صرف تقریباً ایک چوتھائی بناتے ہیں۔ حیاتی غیر نامیاتی مادہ (پانی) انسانی جسم کی کمیت کا دو تہائی سے زیادہ ہے، اور جسم کی کمیت کا مزید 4%–5% غیر نامیاتی نمکیات سے آتا ہے۔','ژوندي عضوي مالیکولونه د بدن د کتلې یوازې نږدې یو پر څلورمه برخه جوړوي. ژوندی غیر عضوي ماده (اوبه) د انسان د بدن د کتلې له دوه پر دریمې ډېره برخه جوړوي، او د بدن د کتلې نور 4%–5% له غیر عضوي مالګو راځي.')
add('21.1 Carbohydrates','21.1 کاربوہائیڈریٹس','21.1 کاربوهایدرېټونه','heading')
add('Carbohydrates form an important class of naturally occurring organic compounds. They are widely distributed in plants and animals. Plants are the major sources of carbohydrates. Carbohydrates include glucose (grape sugar), fructose (honey, fruits), starch (potatoes), cellulose (wood) and glycogen (liver) etc. The word carbohydrate arose because molecular formulae of these compounds can be expressed as hydrates of carbon. Glucose, for example, has the molecular formula C₆H₁₂O₆ can be written as C₆(H₂O)₆. But, however, there are some compounds which are …',
 'کاربوہائیڈریٹس قدرتی طور پر پائے جانے والے نامیاتی مرکبات کی ایک اہم جماعت ہیں۔ یہ پودوں اور جانوروں میں وسیع پیمانے پر پائے جاتے ہیں۔ پودے کاربوہائیڈریٹس کے بڑے ذرائع ہیں۔ کاربوہائیڈریٹس میں گلوکوز (انگوری شکر)، فرکٹوز (شہد، پھل)، نشاستہ (آلو)، سیلولوز (لکڑی) اور گلائیکوجن (جگر) وغیرہ شامل ہیں۔ لفظ کاربوہائیڈریٹ اس لیے بنا کہ ان مرکبات کے سالماتی فارمولے کاربن کے ہائیڈریٹس کے طور پر لکھے جا سکتے ہیں۔ مثلاً گلوکوز کا سالماتی فارمولا C₆H₁₂O₆ ہے جو C₆(H₂O)₆ لکھا جا سکتا ہے۔ لیکن بہرحال کچھ مرکبات ایسے ہیں جو …',
 'کاربوهایدرېټونه په طبیعي ډول موندل کېدونکو عضوي مرکباتو یوه مهمه ډله ده. په بوټو او ژویو کې په پراخه کچه خپاره دي. بوټي د کاربوهایدرېټونو لویې سرچینې دي. کاربوهایدرېټونه ګلوکوز (د انګورو بوره)، فرکټوز (شات، مېوې)، نشایسته (کچالو)، سلولوز (لرګی) او ګلایکوجن (ځیګر) او نور لري. د کاربوهایدرېټ کلمه ځکه رامنځته شوه چې د دغو مرکباتو مالیکولي فورمولونه د کاربن د هایدرېټونو په توګه ښودل کېدای شي. د بېلګې په توګه ګلوکوز مالیکولي فورمول C₆H₁₂O₆ لري چې C₆(H₂O)₆ لیکل کېدای شي. خو بیا هم ځینې مرکبات شته چې …')
r1=section('21.1','Introduction and carbohydrates','تعارف اور کاربوہائیڈریٹس','پېژندنه او کاربوهایدرېټونه',P,L,B,'273')
r1['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':139,'printedPages':[273]}]
r1['sourceContinuesOnPdfPage']=140
carry=[{'from':'21.1','to':'21.2','startsAt':'having molecular formula'}]
if __name__=='__main__':save(139,[r0,r1],carry=carry,chapter_number=21)
