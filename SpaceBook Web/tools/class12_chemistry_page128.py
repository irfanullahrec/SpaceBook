"""PDF128 printed248–249: Unit 19 exercise end and Project; Unit 20 opener with learning outcomes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow128');t=F.t;line=F.line
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows,kind='lines'):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':kind,'indices':list(range(s0,len(P)))})
 def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
 return P,L,B,add,lines,visual
def v5(lang):return F.start(90)+t(30,30,'v.',15)+chain(F,0,70,['H','—','C','—','C','=','CH','—','C','—','H'],15,None,{2:'=O',4:'CH₃',8:'=O'},center=300)+'</svg>'
N={'acid chloride':('ایسڈ کلورائیڈ','اسید کلوراید'),'carboxylate':('کاربوکسیلیٹ','کاربوکسیلېټ'),'nitrile':('نائٹرائل','نایټرایل'),'acid anhydride':('ایسڈ این ہائیڈرائیڈ','اسید انهایدراید'),'ester':('ایسٹر','ایسټر'),'amide':('امائیڈ','اماید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def hub(lang):
 s=F.start(260)+t(425,130,'R—C(=O)—ÖH',16)
 for (x,y,f,n) in ((150,60,'R—C(=O)—Cl:','acid chloride'),(700,40,'R—C(=O)—O:⁻','carboxylate'),(740,130,'R—C≡N:','nitrile'),(160,210,'R—C(=O)—O—C(=O)—R','acid anhydride'),(425,230,'R—C(=O)—O—R','ester'),(700,215,'R—C(=O)—NH₂','amide')):
  s+=t(x,y,f,14)+t(x,y+18,lb(lang,n),12)+F.line(425 if x==425 else (480 if x>425 else 370),140 if y<130 else 150,x+(-60 if x>425 else 60) if x!=425 else 425,y-14 if y>130 else y+4,2,'#222','marker-end="url(#arrow128)"')
 return s+'</svg>'
P,L,B,add,lines,visual=builder()
visual('chem12-p128-name-v',v5)
lines([('(d) Draw the structural formulae for the following organic compounds;','(d) درج ذیل نامیاتی مرکبات کے ساختی فارمولے بنائیں؛','(d) د لاندې عضوي مرکباتو جوړښتي فورمولونه رسم کړئ؛'),
 ('i. 2,4–dimethylpent–2–enal   ii. 2,2–dimethylbutanal','i. 2،4–ڈائی میتھائل پینٹ–2–اینل   ii. 2،2–ڈائی میتھائل بیوٹانل','i. 2،4–ډای میتایل پېنټ–2–ینال   ii. 2،2–ډای میتایل بیوټانال'),
 ('iii. 3,3–dimethylhex–4–en–2–one   iv. 4–methylhex–5–en–3–one','iii. 3،3–ڈائی میتھائل ہیکس–4–این–2–اون   iv. 4–میتھائل ہیکس–5–این–3–اون','iii. 3،3–ډای میتایل هېکس–4–ین–2–ون   iv. 4–میتایل هېکس–5–ین–3–ون'),
 ('v. pent–4–yn–2–one','v. پینٹ–4–ائن–2–اون','v. پېنټ–4–این–2–ون')])
add('Project','منصوبہ','پروژه','heading')
add('Identify aldehydes and ketones in the laboratory tests.','تجربہ گاہی ٹیسٹوں میں الڈیہائیڈز اور کیٹونز کی شناخت کریں۔','په لابراتواري ازموینو کې الدیهایډونه او کیټونونه وپېژنئ.','heading')
add('Add 50 mL of 0.1 M AgNO₃ to the beaker and add NH₄OH to this. A brown precipitate will form. Continue adding NH₄OH until the solution becomes clear. To this, add 25 mL of 0.8 M KOH. Again, add NH₄OH until solution becomes clear. To perform demonstration, add 5 mL of glucose solution to a flask (or test tube) and to this add 25 mL of Tollen’s reagent. Stopper the flask and swirl the solution so that the whole of the inner surface of the flask is wetted. The solution will turn yellow and brown then become cloudy and dark before silver begins to form on the inside of the flask. This should take a couple of minutes. When a satisfactory mirror has formed, rinse the flask and analyse the silver mirror.',
 'بیکر میں 0.1 M AgNO₃ کے 50 mL ڈالیں اور اس میں NH₄OH ملائیں۔ بھورا رسوب بنے گا۔ محلول صاف ہونے تک NH₄OH ملاتے رہیں۔ اس میں 0.8 M KOH کے 25 mL ڈالیں۔ پھر محلول صاف ہونے تک NH₄OH ملائیں۔ مظاہرے کے لیے ایک فلاسک (یا ٹیسٹ ٹیوب) میں گلوکوز محلول کے 5 mL ڈالیں اور اس میں ٹولن عامل کے 25 mL ملائیں۔ فلاسک پر ڈاٹ لگا کر محلول کو گھمائیں تاکہ فلاسک کی پوری اندرونی سطح گیلی ہو جائے۔ فلاسک کے اندر چاندی بننا شروع ہونے سے پہلے محلول پیلا اور بھورا ہو کر پھر دھندلا اور گہرا ہو جائے گا۔ اس میں چند منٹ لگیں گے۔ جب تسلی بخش آئینہ بن جائے تو فلاسک کو کھنگال کر چاندی کے آئینے کا تجزیہ کریں۔',
 'په بیکر کې د 0.1 M AgNO₃ 50 mL واچوئ او NH₄OH ورزیات کړئ. نسواري رسوب به جوړ شي. تر هغه NH₄OH ورزیاتوئ چې محلول روڼ شي. بیا د 0.8 M KOH 25 mL ورزیات کړئ. بیا تر هغه NH₄OH ورزیات کړئ چې محلول روڼ شي. د ښودنې لپاره په یوه فلاسک (یا ټیسټ ټیوب) کې د ګلوکوز محلول 5 mL واچوئ او د ټولن عامل 25 mL ورزیات کړئ. فلاسک بند کړئ او محلول وګرځوئ څو د فلاسک ټوله داخلي سطحه لانده شي. محلول به ژېړ او نسواري، بیا خړ او تیاره شي مخکې له دې چې د فلاسک دننه سپین زر جوړ شي. دا به څو دقیقې ونیسي. کله چې د قناعت وړ هینداره جوړه شوه، فلاسک ومینځئ او د سپینو زرو هینداره وڅېړئ.')
r13=section('19.13','Unit 19 exercise end and Project','یونٹ 19 مشق کا اختتام اور منصوبہ','د 19 واحد تمرین پای او پروژه',P,L,B,'248')
r13['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':128,'printedPages':[248]}];r13['insertBefore']='19.exercise.solved'
P,L,B,add,lines,visual=builder()
add('Unit 20 — Carbonyl Compounds 2: Carboxylic Acids and Functional Derivatives','یونٹ 20 — کاربونل مرکبات 2: کاربوکسیلک ایسڈز اور فعلی مشتقات','20 واحد — کاربونیل مرکبات 2: کاربوکسیلیک اسیدونه او فعال مشتقات','heading')
tb={'id':'chem12-unit20-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['7','1','6']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['7','1','6']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['7','1','6']]}]}
B.append(tb);L.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
lines([('Describe preparation of carboxylic acids by carbonation of Grignard’s Reagent, hydrolysis of nitriles, oxidation of primary alcohols, oxidation of aldehydes and oxidation of alkyl benzene. (Applying)','گرینیارڈ عامل کی کاربونیشن، نائٹرائلز کی ہائیڈرولائسز، ابتدائی الکوحلز کی تکسید، الڈیہائیڈز کی تکسید اور الکائل بینزین کی تکسید سے کاربوکسیلک ایسڈز کی تیاری بیان کریں۔ (اطلاق)','د ګرینیارډ عامل د کاربونېشن، د نایټرایلونو د هایدرولیز، د لومړنیو الکولونو د اکسیډېشن، د الدیهایډونو د اکسیډېشن او د الکایل بنزین د اکسیډېشن په واسطه د کاربوکسیلیک اسیدونو چمتو کول بیان کړي. (تطبیق)'),
 ('Discuss reactivity of carboxylic acids. (Applying)','کاربوکسیلک ایسڈز کی تعامل پذیری پر بحث کریں۔ (اطلاق)','د کاربوکسیلیک اسیدونو پر تعامل وړتیا بحث وکړي. (تطبیق)'),
 ('Describe the chemistry of carboxylic acids by conversion to carboxylic acid derivatives i.e. acyl halides, acid anhydrides, esters, amides and reactions involving inter conversion of these. (Analyzing)','کاربوکسیلک ایسڈز کی کیمیا ان کے مشتقات، یعنی ایسائل ہیلائیڈز، ایسڈ این ہائیڈرائیڈز، ایسٹرز، امائیڈز میں تبدیلی اور ان کی باہمی تبدیلی کے تعاملات کے ذریعے بیان کریں۔ (تجزیہ)','د کاربوکسیلیک اسیدونو کیمیا د هغوی مشتقاتو، یعنې اسایل هالایډونو، اسید انهایدرایډونو، ایسټرونو، امایډونو ته د بدلون او د دوی د متقابل بدلون د تعاملونو له لارې بیان کړي. (شننه)'),
 ('Describe reactions of carboxylic acid derivatives. (Applying)','کاربوکسیلک ایسڈ مشتقات کے تعاملات بیان کریں۔ (اطلاق)','د کاربوکسیلیک اسید د مشتقاتو تعاملونه بیان کړي. (تطبیق)'),
 ('Describe isomerism in carboxylic acids. (Understanding)','کاربوکسیلک ایسڈز میں آئسومرزم بیان کریں۔ (سمجھنا)','په کاربوکسیلیک اسیدونو کې ایزومېریزم بیان کړي. (پوهېدل)')],'list')
visual('chem12-p128-derivatives-hub',hub)
r20=section('chem12-u20-opening','Unit 20 opener and learning outcomes','یونٹ 20 کا آغاز اور تعلیمی نتائج','د 20 واحد پیل او د زده کړې پایلې',P,L,B,'249')
r20['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':128,'printedPages':[249]}];r20['sourceChapterNumber']=20;r20['insertBefore']='20.1'
r20['sourceCoverIllustrationReview']='Cover ball-and-stick molecules decorative; carboxylic-acid derivative hub on printed 249 reconstructed as coded SVG.'
trim=[{'id':'20.1','sourceChapterNumber':20,'startsAt':'Introduction\nNOT FOR SALE'}]
if __name__=='__main__':save(128,[r13,r20],trim=trim,chapter_number=19)
