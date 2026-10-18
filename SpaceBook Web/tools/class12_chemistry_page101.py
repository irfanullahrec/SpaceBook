"""PDF101 printed194–195: Unit 18 opener, learning outcomes, introduction, alcohols and their classes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow101');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Alcohols':('الکوحلز','الکولونه'),'Phenols':('فینولز','فینولونه'),'Ethers':('ایتھرز','ایترونه'),'hydroxyl group':('ہائیڈروآکسل گروپ','هایدروکسیل ګروپ'),'(functional group)':('(فعلی گروپ)','(فعال ګروپ)'),
   'aliphatic carbon':('ایلیفیٹک کاربن','الیفاتیک کاربن'),'methyl alcohols':('میتھائل الکوحلز','میتایل الکولونه'),'primary (1°) alcohols':('ابتدائی (1°) الکوحلز','لومړني (1°) الکولونه'),
   'secondary (2°) alcohols':('ثانوی (2°) الکوحلز','دویمي (2°) الکولونه'),'tertiary (3°) alcohols':('ثالثی (3°) الکوحلز','درېیمي (3°) الکولونه')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def families(lang):
 s=F.start(90)
 for x,(f,n) in zip((180,420,660),(('R – OH','Alcohols'),('Ar – OH','Phenols'),('Ar/R – Ö – R/Ar','Ethers'))):s+=t(x,40,f,18)+t(x,64,lb(lang,n),13)
 return s+'</svg>'
def group(lang):
 s=F.start(110)+t(330,60,'—C—',18)+line(330,30,330,46)+line(330,70,330,86)+'<rect x="352" y="40" width="60" height="30" fill="none" stroke="#222" stroke-dasharray="3 3"/>'+t(382,61,'OH',17)
 s+=t(480,52,lb(lang,'hydroxyl group'),13,'#1565c0')+t(480,68,lb(lang,'(functional group)'),13,'#1565c0')+f'<path d="M330 90 Q350 104 400 98" fill="none" stroke="#222" stroke-dasharray="2 3"/>'+t(470,102,lb(lang,'aliphatic carbon'),13,'#1565c0')
 return s+'</svg>'
def classes(lang):
 s=F.start(150)
 for x,(top,left,bot,name) in zip((110,320,540,750),(('H','H','H','methyl alcohols'),('H','R','H','primary (1°) alcohols'),('R','R','H','secondary (2°) alcohols'),('R','R','R','tertiary (3°) alcohols'))):
  s+=t(x,30,top,16)+line(x,36,x,52)+t(x-36,72,left+' —',16)+t(x,72,'C',17)+t(x+32,72,'— OH',16)+line(x,80,x,96)+t(x,114,bot,16)+t(x,140,lb(lang,name),12)
 return s+'</svg>'

add('Unit 18 — Alcohols, Phenols and Ethers','یونٹ 18 — الکوحلز، فینولز اور ایتھرز','18 واحد — الکولونه، فینولونه او ایترونه','heading')
tb={'id':'chem12-unit18-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['9','1','8']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['9','1','8']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['9','1','8']]}]}
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
out=[('Explain nomenclature, structure and acidity of alcohols as exemplified by ethanol. (Understanding)','ایتھانول کی مثال سے الکوحلز کی نام گذاری، ساخت اور تیزابیت واضح کریں۔ (سمجھنا)','د ایتانول په بېلګه د الکولونو نومول، جوړښت او تېزابیت روښانه کړي. (پوهېدل)'),
 ('Describe the preparation of alcohols by reduction of aldehydes, ketones, carboxylic acids and esters. (Applying)','الڈیہائیڈز، کیٹونز، کاربوکسیلک ایسڈز اور ایسٹرز کی تخفیف سے الکوحلز کی تیاری بیان کریں۔ (اطلاق)','د الدیهایډونو، کیټونونو، کاربوکسیلیک اسیدونو او ایسټرونو د ارجاع په واسطه د الکولونو چمتو کول بیان کړي. (تطبیق)'),
 ('Explain reactivity of alcohols. (Understanding)','الکوحلز کی تعامل پذیری واضح کریں۔ (سمجھنا)','د الکولونو تعامل وړتیا روښانه کړي. (پوهېدل)'),
 ('Describe the chemistry of alcohols by preparation of ethers and esters, oxidative cleavage of 1,2–diols. (Applying)','ایتھرز اور ایسٹرز کی تیاری اور 1،2–ڈائی اولز کی تکسیدی شکست کے ذریعے الکوحلز کی کیمیا بیان کریں۔ (اطلاق)','د ایترونو او ایسټرونو د جوړولو او د 1،2–ډای اولونو د اکسیډیټیف ماتولو له لارې د الکولونو کیمیا بیان کړي. (تطبیق)'),
 ('Discuss thiols (RSH). (Understanding)','تھائیولز (RSH) پر بحث کریں۔ (سمجھنا)','پر تیولونو (RSH) بحث وکړي. (پوهېدل)'),
 ('Explain the nomenclature, structure and acidity of phenols. (Applying)','فینولز کی نام گذاری، ساخت اور تیزابیت واضح کریں۔ (اطلاق)','د فینولونو نومول، جوړښت او تېزابیت روښانه کړي. (تطبیق)'),
 ('Describe the preparation of phenol from benzene sulphonic acid, chlorobenzene, acidic oxidation of cumene and hydrolysis of diazonium salts. (Applying)','بینزین سلفونک ایسڈ، کلورو بینزین، کیومین کی تیزابی تکسید اور ڈائی ایزونیم نمکیات کی ہائیڈرولائسز سے فینول کی تیاری بیان کریں۔ (اطلاق)','له بنزین سلفونیک اسید، کلوروبنزین، د کیومین له اسیدي اکسیډېشن او د ډای ازونیم مالګو له هایدرولیز څخه د فینول چمتو کول بیان کړي. (تطبیق)'),
 ('Discuss the reactivity of phenol and their chemistry by electrophilic aromatic substitution, reaction with sodium metal and oxidation. (Applying)','الیکٹروفائلی ارومیٹک تبادلے، سوڈیم دھات سے تعامل اور تکسید کے ذریعے فینول کی تعامل پذیری اور کیمیا پر بحث کریں۔ (اطلاق)','د الکتروفایلي اروماتیک بدلون، له سوډیم فلز سره تعامل او اکسیډېشن له لارې د فینول پر تعامل وړتیا او کیمیا بحث وکړي. (تطبیق)'),
 ('Differentiate between alcohol and phenol. (Understanding)','الکوحل اور فینول میں فرق کریں۔ (سمجھنا)','د الکول او فینول توپیر وکړي. (پوهېدل)'),
 ('Describe isomerism in alcohols and phenols. (Understanding)','الکوحلز اور فینولز میں آئسومرزم بیان کریں۔ (سمجھنا)','په الکولونو او فینولونو کې ایزومېریزم بیان کړي. (پوهېدل)'),
 ('Identify ethers from their formula. (Understanding)','ایتھرز کو ان کے فارمولے سے شناخت کریں۔ (سمجھنا)','ایترونه د خپل فورمول له مخې وپېژني. (پوهېدل)')]
s0=len(paras)
for r in out:paras.append(pair(*r))
layout.append({'type':'list','indices':list(range(s0,len(paras)))})
add('Introduction','تعارف','پېژندنه','heading')
add('Alcohols, phenols and ethers are derivatives of water. In alcohol and phenol one hydrogen of water has been replaced by an alkyl group and aryl group respectively. Whereas in ether both hydrogen atom have been replaced by two alkyl (or aryl) groups.',
 'الکوحلز، فینولز اور ایتھرز پانی کے مشتقات ہیں۔ الکوحل اور فینول میں پانی کا ایک ہائیڈروجن بالترتیب الکائل گروپ اور ایرائل گروپ سے بدلا گیا ہے۔ جبکہ ایتھر میں دونوں ہائیڈروجن ایٹم دو الکائل (یا ایرائل) گروپوں سے بدلے گئے ہیں۔',
 'الکولونه، فینولونه او ایترونه د اوبو مشتقات دي. په الکول او فینول کې د اوبو یو هایدروجن په ترتیب سره په الکایل ګروپ او اریل ګروپ بدل شوی. په داسې حال کې چې په ایتر کې دواړه هایدروجني اټومونه په دوو الکایل (یا اریل) ګروپونو بدل شوي.')
visual('chem12-p101-families',families)
add('18.1 Alcohols','18.1 الکوحلز','18.1 الکولونه','heading')
add('Alcohols are organic compounds, in which a hydroxyl group (–OH) is attached to an aliphatic carbon atom. Hydroxyl group is the functional group of alcohols. The general formula of alcohols (containing one –OH group) is R–OH or CₙH₂ₙ₊₁OH e.g. methyl alcohol (CH₃OH), ethyl alcohol (C₂H₅OH) etc.',
 'الکوحلز وہ نامیاتی مرکبات ہیں جن میں ہائیڈروآکسل گروپ (–OH) ایک ایلیفیٹک کاربن ایٹم سے جڑا ہوتا ہے۔ ہائیڈروآکسل گروپ الکوحلز کا فعلی گروپ ہے۔ الکوحلز (ایک –OH گروپ والے) کا عمومی فارمولا R–OH یا CₙH₂ₙ₊₁OH ہے، مثلاً میتھائل الکوحل (CH₃OH)، ایتھائل الکوحل (C₂H₅OH) وغیرہ۔',
 'الکولونه هغه عضوي مرکبات دي چې پکې هایدروکسیل ګروپ (–OH) له یوه الیفاتیک کاربني اټوم سره تړلی وي. هایدروکسیل ګروپ د الکولونو فعال ګروپ دی. د الکولونو (یو –OH ګروپ لرونکو) عمومي فورمول R–OH یا CₙH₂ₙ₊₁OH دی، لکه میتایل الکول (CH₃OH)، ایتیل الکول (C₂H₅OH) او نور.')
visual('chem12-p101-hydroxyl',group)
add('Alcohols may be monohydric or polyhydric, depending upon the number of –OH groups in a molecule. Monohydric alcohol contain one –OH group, while polyhydric alcohols contain more than one –OH group. Polyhydric alcohols may further be classified into dihydric alcohols (or diols), trihydric alcohols (or triol), etc. containing two and three hydroxyl groups respectively. Dihydric alcohols (diols) are also called glycols because of their sweet taste. (Greek glycys means ‘sweet’) (Examples are given in nomenclature).',
 'سالمے میں –OH گروپوں کی تعداد کے لحاظ سے الکوحلز مونو ہائیڈرک یا پولی ہائیڈرک ہو سکتے ہیں۔ مونو ہائیڈرک الکوحل میں ایک –OH گروپ ہوتا ہے، جبکہ پولی ہائیڈرک الکوحلز میں ایک سے زیادہ –OH گروپ ہوتے ہیں۔ پولی ہائیڈرک الکوحلز کو مزید ڈائی ہائیڈرک الکوحلز (یا ڈائی اولز)، ٹرائی ہائیڈرک الکوحلز (یا ٹرائی اول) وغیرہ میں تقسیم کیا جا سکتا ہے جن میں بالترتیب دو اور تین ہائیڈروآکسل گروپ ہوتے ہیں۔ ڈائی ہائیڈرک الکوحلز (ڈائی اولز) کو میٹھے ذائقے کی وجہ سے گلائیکولز بھی کہتے ہیں۔ (یونانی glycys کا مطلب ’میٹھا‘ ہے) (مثالیں نام گذاری میں دی گئی ہیں)۔',
 'په مالیکول کې د –OH ګروپونو د شمېر له مخې الکولونه کېدای شي مونوهایدریک یا پولي هایدریک وي. مونوهایدریک الکول یو –OH ګروپ لري، خو پولي هایدریک الکولونه له یوه ډېر –OH ګروپونه لري. پولي هایدریک الکولونه نور هم په ډای هایدریک الکولونو (یا ډای اولونو)، ټرای هایدریک الکولونو (یا ټرای اول) او نورو وېشل کېدای شي چې په ترتیب سره دوه او درې هایدروکسیل ګروپونه لري. ډای هایدریک الکولونو (ډای اولونو) ته د خوږ خوند له امله ګلایکولونه هم وايي. (یوناني glycys د ’خوږ‘ معنا لري) (بېلګې په نومولو کې ورکړل شوې).')
add('Monohydric alcohols may be primary, secondary or tertiary. When the hydroxyl group is attached to the primary carbon atom, it is classified as primary alcohol but when the hydroxyl group is attached to the secondary or tertiary carbon atom, the alcohol is accordingly classified as secondary or tertiary alcohol.',
 'مونو ہائیڈرک الکوحلز ابتدائی، ثانوی یا ثالثی ہو سکتے ہیں۔ جب ہائیڈروآکسل گروپ ابتدائی کاربن ایٹم سے جڑا ہو تو اسے ابتدائی الکوحل کہتے ہیں، لیکن جب ہائیڈروآکسل گروپ ثانوی یا ثالثی کاربن ایٹم سے جڑا ہو تو الکوحل کو اسی مناسبت سے ثانوی یا ثالثی الکوحل کہا جاتا ہے۔',
 'مونوهایدریک الکولونه کېدای شي لومړني، دویمي یا درېیمي وي. کله چې هایدروکسیل ګروپ له لومړني کاربني اټوم سره تړلی وي، لومړنی الکول ګڼل کېږي، خو کله چې هایدروکسیل ګروپ له دویمي یا درېیمي کاربني اټوم سره تړلی وي، الکول په همدې ډول دویمی یا درېیمی الکول ګڼل کېږي.')
visual('chem12-p101-alcohol-classes',classes)
add('18.1.1 Nomenclature','18.1.1 نام گذاری','18.1.1 نومول','heading')
add('Alcohols are named by common and IUPAC systems.','الکوحلز کے نام عام اور IUPAC نظاموں سے رکھے جاتے ہیں۔','الکولونه د عام او IUPAC سیستمونو په واسطه نومول کېږي.')
record=section('18.1','Unit 18 opener and introduction to alcohols','یونٹ 18 کا آغاز اور الکوحلز کا تعارف','د 18 واحد پیل او د الکولونو پېژندنه',paras,layout,blocks,'194–195')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':101,'printedPages':[194,195]}]
record['sourceContinuesOnPdfPage']=102
record['sourceCoverIllustrationReview']='Cover ball-and-stick and electrostatic-potential renderings are decorative; not reconstructed.'
carry=[{'from':'18.1','to':'18.2','startsAt':'a. Common System\nNOT FOR SALE'}]
if __name__=='__main__':save(101,[record],carry=carry,chapter_number=18)
