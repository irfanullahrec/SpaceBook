"""PDF116 printed224–225: Unit 18 exercise end and Project; Unit 19 opener with learning outcomes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow116');t=F.t;line=F.line;ring=F.ring
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':'lines','indices':list(range(s0,len(P)))})
 def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
 return P,L,B,add,lines,visual
def names(lang):
 s=F.start(330)
 s+=t(30,40,'i.',15)+chain(F,0,90,['H₃C','—','C','—','CH₂','—','CH₃'],15,None,{2:'OH'},{2:'CH₃'},center=150)
 s+=t(300,40,'ii.',15)+chain(F,0,90,['H₃C','—','C','—','CH','—','CH₂','—','CH₃'],15,None,{2:'OH',4:'OH'},{2:'CH₃'},center=440)
 s+=t(600,40,'iii.',15)+chain(F,0,90,['H₃C','—','C','—','CH₂','—','CH=CH₂'],15,None,{2:'OH'},{2:'CH₃'},center=730)
 s+=t(30,200,'iv.',15)+ring(150,240,30,subs={0:'OH',1:'Br',2:'F',3:'CH₃'})
 s+=t(330,200,'v.',15)+chain(F,0,250,['H₃C','—','CH','—','CH','—','CH₃'],15,None,{2:'OCH₃',4:'OCH₃'},center=470)
 return s+'</svg>'
P,L,B,add,lines,visual=builder()
lines([('3. Give detail description of structure and chemical properties of phenols.','3. فینولز کی ساخت اور کیمیائی خصوصیات کی تفصیلی وضاحت کریں۔','3. د فینولونو د جوړښت او کیمیاوي ځانګړنو مفصل تشریح ورکړئ.'),
 ('4. (a) Discuss the structure, synthesis and chemical reactions of alcohols.','4. (a) الکوحلز کی ساخت، تالیف اور کیمیائی تعاملات پر بحث کریں۔','4. (a) د الکولونو پر جوړښت، ترکیب او کیمیاوي تعاملونو بحث وکړئ.'),
 ('(b) How alcohols are slightly acidic?','(b) الکوحلز ہلکے تیزابی کیسے ہیں؟','(b) الکولونه څنګه لږ تېزابي دي؟'),
 ('5. (a) How alcohol can be prepared from Grignard reagents.','5. (a) گرینیارڈ عاملین سے الکوحل کیسے تیار کیا جا سکتا ہے۔','5. (a) له ګرینیارډ عاملونو الکول څنګه چمتو کېدای شي.'),
 ('(b) Mention the reaction for the formation of following compounds from an alcohol. (i) ethene (ii) ethlyacetate (iii) acetone (iv) formaldehyde','(b) الکوحل سے درج ذیل مرکبات بنانے کا تعامل بتائیں۔ (i) ایتھین (ii) ایتھائل ایسیٹیٹ (iii) ایسیٹون (iv) فارم الڈیہائیڈ','(b) له الکول څخه د لاندې مرکباتو د جوړولو تعامل وښیئ. (i) ایتین (ii) ایتیل اسیټېټ (iii) اسیتون (iv) فورمالدیهاید'),
 ('(c) Write the systematic names for the following organic compounds;','(c) درج ذیل نامیاتی مرکبات کے نظامی نام لکھیں؛','(c) د لاندې عضوي مرکباتو سیستماتیک نومونه ولیکئ؛')])
visual('chem12-p116-naming',names)
lines([('(d) Draw the structural formula of the following organic compounds;','(d) درج ذیل نامیاتی مرکبات کے ساختی فارمولے بنائیں؛','(d) د لاندې عضوي مرکباتو جوړښتي فورمولونه رسم کړئ؛'),
 ('i. pentan–2–ol','i. پینٹین–2–اول','i. پېنټان–2–ول'),('ii. 3,4–dimethylhexan–2–ol','ii. 3،4–ڈائی میتھائل ہیکسین–2–اول','ii. 3،4–ډای میتایل هېکسان–2–ول'),
 ('iii. 4–methylpent–3–en–2–ol','iii. 4–میتھائل پینٹ–3–این–2–اول','iii. 4–میتایل پېنټ–3–ین–2–ول'),('iv. 3,4–dimethyl–2–nitrophenol','iv. 3،4–ڈائی میتھائل–2–نائٹرو فینول','iv. 3،4–ډای میتایل–2–نایټروفینول'),
 ('v. 2,3–dimethoxy–4–methylpentane','v. 2،3–ڈائی میتھوآکسی–4–میتھائل پینٹین','v. 2،3–ډای میتوکسي–4–میتایل پېنټان')])
r17=section('18.17','Unit 18 exercise: detailed questions','یونٹ 18 مشق: تفصیلی سوالات','د 18 واحد تمرین: تفصیلي پوښتنې',P,L,B,'224')
r17['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':116,'printedPages':[224]}]
P,L,B,add,lines,visual=builder()
add('Project','منصوبہ','پروژه','heading')
add('Dissolve few drops or one small crystal of phenol in 10 mL of ethyl alcohol or methyl alcohol. Stir vigorously while adding bromine water, drop–wise. Rapid loss of reddish brown color of bromine water and formation of white precipitate of 2,4,6–tribromophenol suggests the presence of phenol (Section 18.2.7.1).',
 'فینول کے چند قطرے یا ایک چھوٹی قلم 10 mL ایتھائل الکوحل یا میتھائل الکوحل میں حل کریں۔ قطرہ قطرہ برومین واٹر ڈالتے ہوئے زور سے ہلائیں۔ برومین واٹر کے سرخی مائل بھورے رنگ کا تیزی سے ختم ہونا اور 2،4،6–ٹرائی برومو فینول کا سفید رسوب بننا فینول کی موجودگی ظاہر کرتا ہے (حصہ 18.2.7.1)۔',
 'د فینول څو څاڅکي یا یو کوچنی کرسټل په 10 mL ایتیل الکول یا میتایل الکول کې حل کړئ. د برومین اوبو په څاڅکي څاڅکي زیاتولو سره په زوره وښوروئ. د برومین اوبو د سرخي مایل نسواري رنګ چټک ورکېدل او د 2،4،6–ټرای بروموفینول د سپین رسوب جوړېدل د فینول شتون ښيي (برخه 18.2.7.1).')
r18=section('18.18','Unit 18 Project','یونٹ 18 منصوبہ','د 18 واحد پروژه',P,L,B,'224')
r18['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':116,'printedPages':[224]}]
P,L,B,add,lines,visual=builder()
add('Unit 19 — Carbonyl Compounds 1: Aldehydes and Ketones','یونٹ 19 — کاربونل مرکبات 1: الڈیہائیڈز اور کیٹونز','19 واحد — کاربونیل مرکبات 1: الدیهایډونه او کیټونونه','heading')
tb={'id':'chem12-unit19-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['14','1','4']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['14','1','4']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['14','1','4']]}]}
B.append(tb);L.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
out=[('Explain nomenclature and structure of Aldehydes and ketones. (Applying)','الڈیہائیڈز اور کیٹونز کی نام گذاری اور ساخت واضح کریں۔ (اطلاق)','د الدیهایډونو او کیټونونو نومول او جوړښت روښانه کړي. (تطبیق)'),
 ('Discuss the preparation of aldehydes and ketones by ozonolysis of alkenes, hydration of alkynes, oxidation of alcohol and Friedel Craft’s acylation of aromatics. (Applying)','الکینز کی اوزونولائسز، الکائنز کی ہائیڈریشن، الکوحل کی تکسید اور ارومیٹکس کی فریڈل کرافٹ ایسائلیشن سے الڈیہائیڈز اور کیٹونز کی تیاری پر بحث کریں۔ (اطلاق)','د الکینونو اوزونولایسس، د الکاینونو هایدرېشن، د الکول اکسیډېشن او د اروماتیکونو د فریډل کرافټ اسایلېشن په واسطه د الدیهایډونو او کیټونونو پر چمتو کولو بحث وکړي. (تطبیق)'),
 ('Describe the reactivity of aldehydes and ketones and their comparison. (Analyzing)','الڈیہائیڈز اور کیٹونز کی تعامل پذیری اور ان کا موازنہ بیان کریں۔ (تجزیہ)','د الدیهایډونو او کیټونونو تعامل وړتیا او پرتله یې بیان کړي. (شننه)'),
 ('Describe acid and base catalyzed nucleophillic addition reactions of aldehydes and ketones. (Applying)','الڈیہائیڈز اور کیٹونز کے تیزاب اور اساس سے عمل انگیز نیوکلیوفائلی اضافی تعاملات بیان کریں۔ (اطلاق)','د الدیهایډونو او کیټونونو اسیدي او قلوي کتلستي نیوکلیوفایلي اضافي تعاملونه بیان کړي. (تطبیق)'),
 ('Discuss the chemistry of aldehydes and ketones by their reduction to hydrocarbons, alcohols, by using carbon nucleophiles, nitrogen nucleophiles and oxygen nucleophiles. (Applying)','الڈیہائیڈز اور کیٹونز کی ہائیڈروکاربنز اور الکوحلز تک تخفیف، اور کاربن، نائٹروجن اور آکسیجن نیوکلیوفائلز کے استعمال سے ان کی کیمیا پر بحث کریں۔ (اطلاق)','د الدیهایډونو او کیټونونو کیمیا د هایدروکاربنونو او الکولونو ته د ارجاع، او د کاربن، نایتروجن او اکسیجن نیوکلیوفایلونو په کارولو بحث کړي. (تطبیق)'),
 ('Describe oxidation reactions of aldehydes and ketones. (Applying)','الڈیہائیڈز اور کیٹونز کے تکسیدی تعاملات بیان کریں۔ (اطلاق)','د الدیهایډونو او کیټونونو اکسیډېشن تعاملونه بیان کړي. (تطبیق)'),
 ('Describe isomerism in aldehydes and ketones. (Understanding)','الڈیہائیڈز اور کیٹونز میں آئسومرزم بیان کریں۔ (سمجھنا)','په الدیهایډونو او کیټونونو کې ایزومېریزم بیان کړي. (پوهېدل)')]
s0=len(P)
for r in out:P.append(pair(*r))
L.append({'type':'list','indices':list(range(s0,len(P)))})
def carbonylfig(lang):
 s=F.start(170)+'<ellipse cx="220" cy="40" rx="60" ry="18" fill="#5c6bc0" opacity=".7"/>'+t(220,47,'π',20,'white')+'<ellipse cx="220" cy="130" rx="60" ry="18" fill="#5c6bc0" opacity=".7"/>'
 s+=t(180,90,'C',18)+t(230,82,'sp²–sp²',14)+line(195,88,260,88)+t(230,108,'σ',16)+t(275,92,'O',18)+line(170,95,130,135,3)+t(110,120,'s–sp²',13)
 s+='<ellipse cx="330" cy="60" rx="18" ry="14" fill="#f48fb1"/><ellipse cx="330" cy="120" rx="18" ry="14" fill="#f48fb1"/>'
 s+='<ellipse cx="560" cy="60" rx="10" ry="24" fill="#81d4fa"/><ellipse cx="560" cy="120" rx="10" ry="24" fill="#81d4fa"/><ellipse cx="680" cy="60" rx="10" ry="24" fill="#29b6f6"/><ellipse cx="680" cy="120" rx="10" ry="24" fill="#29b6f6"/>'
 s+=t(560,96,'C',17)+line(570,90,668,90)+t(680,96,'O',17)+line(552,84,520,60)+t(510,56,"R′",14)+line(552,96,520,122)+t(510,130,'R',14)+t(620,30,'π bond',13)+t(620,150,'σ bond',13)+t(740,150,'P ORBITAL',12)
 return s+'</svg>'
visual('chem12-p116-carbonyl-orbitals',carbonylfig)
r19=section('chem12-u19-opening','Unit 19 opener and learning outcomes','یونٹ 19 کا آغاز اور تعلیمی نتائج','د 19 واحد پیل او د زده کړې پایلې',P,L,B,'225')
r19['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':116,'printedPages':[225]}]
r19['sourceChapterNumber']=19;r19['insertBefore']='19.1'
r19['sourceCoverIllustrationReview']='Cover ball-and-stick molecules decorative; carbonyl σ/π orbital figure on printed 225 reconstructed as coded SVG.'
issues=[{'id':'chem12-p224-printed','printedPage':224,'description':'Q5(b)(ii) printed "ethlyacetate" retained; Unit 18 exercise split as 18.17 (questions) and 18.18 (Project); legacy Unit 19 spill formerly in 18.18 replaced (Unit 19 opener now its own record in chapter 19).'}]
if __name__=='__main__':save(116,[r17,r18,r19],issues=issues,chapter_number=18)
