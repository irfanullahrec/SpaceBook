"""PDF85 printed162–163: Unit 17 opener, learning outcomes, introduction to alkyl halides, common names."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow85');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'methyl halide':('میتھائل ہیلائیڈ','میتایل هالایډ'),'primary (1°) alkyl halide':('ابتدائی (1°) الکائل ہیلائیڈ','لومړنی (1°) الکایل هالایډ'),'secondary (2°) alkyl halide':('ثانوی (2°) الکائل ہیلائیڈ','دویمی (2°) الکایل هالایډ'),
   'tertiary (3°) alkyl halide':('ثالثی (3°) الکائل ہیلائیڈ','درېیمی (3°) الکایل هالایډ'),'methyl chloride':('میتھائل کلورائیڈ','میتایل کلوراید'),'ethyl chloride':('ایتھائل کلورائیڈ','ایتیل کلوراید'),'n-propyl chloride':('n-پروپائل کلورائیڈ','n-پروپیل کلوراید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def cover(lang):
 s=F.start(170,520)
 s+='<path d="M120 30 C100 30 92 70 110 92 L120 104 L130 92 C148 70 140 30 120 30z" fill="#f9a825" stroke="#333"/>'+t(112,70,'••',14)+'<rect x="20" y="62" width="44" height="26" fill="white" stroke="#333"/>'+t(42,82,'sp³',16)+line(64,80,108,100,1.5)
 s+=t(120,122,'N',20)+line(126,118,160,112,2,'#222','stroke-dasharray="3 3"')+t(175,112,'R³',15)+line(114,128,95,150)+t(88,165,'R¹',15)+line(126,128,140,150,4)+t(150,165,'R²',15)
 s+=f'<circle cx="380" cy="34" r="18" fill="#c0ca33" stroke="#333"/>'+t(380,40,'Cl',15)+'<path d="M376 52 L384 52 L382 92 L378 92z" fill="#cddc39"/>'
 for x,y in ((330,118),(430,118),(380,160)):s+=line(380,104,x,y,3,'#999')+f'<circle cx="{x}" cy="{y}" r="11" fill="white" stroke="#333"/>'+t(x,y+5,'H',13)
 s+=f'<circle cx="380" cy="104" r="16" fill="#eeeeee" stroke="#333"/>'+t(380,110,'C',15)
 return s+'</svg>'
def classes(lang):
 s=F.start(160)
 for x,(top,left,bot,name) in zip((110,320,540,750),(('H','H','H','methyl halide'),('H','R','H','primary (1°) alkyl halide'),('R','R','H','secondary (2°) alkyl halide'),('R','R','R','tertiary (3°) alkyl halide'))):
  s+=t(x,30,top,17)+line(x,36,x,54)+t(x-38,76,left+' —',17)+t(x,76,'C',18)+t(x+30,76,'— X',17)+line(x,84,x,102)+t(x,122,bot,17)+t(x,150,lb(lang,name),12)
 return s+'</svg>'
def common(lang):
 s=F.start(80)
 for x,(f,n) in zip((160,425,690),(('CH₃—Cl','methyl chloride'),('CH₃—CH₂—Cl','ethyl chloride'),('CH₃—CH₂—CH₂—Cl','n-propyl chloride'))):s+=t(x,35,f,18)+t(x,60,lb(lang,n),13)
 return s+'</svg>'

add('Unit 17 — Alkyl Halides and Amines','یونٹ 17 — الکائل ہیلائیڈز اور امائنز','17 واحد — الکایل هالایډونه او امینونه','heading')
tb={'id':'chem12-unit17-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['11','1','8']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['11','1','8']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['11','1','8']]}]}
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:','heading')
out=[('Name alkyl halides using IUPAC system. (Applying)','IUPAC نظام سے الکائل ہیلائیڈز کے نام رکھیں۔ (اطلاق)','د IUPAC سیستم په کارولو الکایل هالایډونه ونوموي. (تطبیق)'),
 ('Discuss the structure and reactivity of RX. (Applying)','RX کی ساخت اور تعامل پذیری پر بحث کریں۔ (اطلاق)','د RX پر جوړښت او تعامل وړتیا بحث وکړي. (تطبیق)'),
 ('Describe the preparation of RX by the reaction of alcohols with HX, SOCl₂ and PX₃ and by radical halogenations of alkanes. (Applying)','الکوحلز کے HX، SOCl₂ اور PX₃ سے تعامل اور الکینز (اکیلے بند والے) کی ریڈیکل ہیلوجینیشن سے RX کی تیاری بیان کریں۔ (اطلاق)','د الکولونو له HX، SOCl₂ او PX₃ سره د تعامل او د الکانونو د رادیکالي هالوجینېشن په واسطه د RX چمتو کول بیان کړي. (تطبیق)'),
 ('Describe the mechanism and types of nucleophilic substitution reactions. (Understanding)','نیوکلیوفائلی تبادلے کے تعاملات کا طریق کار اور اقسام بیان کریں۔ (سمجھنا)','د نیوکلیوفایلي بدلون تعاملونو میکانیزم او ډولونه بیان کړي. (پوهېدل)'),
 ('Describe the mechanism and types of elimination reactions. (Understanding)','اخراجی تعاملات کا طریق کار اور اقسام بیان کریں۔ (سمجھنا)','د ایستلو تعاملونو میکانیزم او ډولونه بیان کړي. (پوهېدل)'),
 ('Describe the preparation and reactivity of Grignard’s reagent. (Applying)','گرینیارڈ عامل کی تیاری اور تعامل پذیری بیان کریں۔ (اطلاق)','د ګرینیارډ عامل چمتو کول او تعامل وړتیا بیان کړي. (تطبیق)'),
 ('Discuss chemistry of Grignard’s reagents by the addition of aldehydes, ketones, esters and carbon dioxide. (Understanding)','الڈیہائیڈز، کیٹونز، ایسٹرز اور کاربن ڈائی آکسائیڈ کے اضافے سے گرینیارڈ عاملوں کی کیمیا پر بحث کریں۔ (سمجھنا)','د الدیهایډونو، کیټونونو، ایسټرونو او کاربن ډای اکساید د زیاتولو له لارې د ګرینیارډ عاملونو پر کیمیا بحث وکړي. (پوهېدل)'),
 ('Discuss nomenclature, structure and basicity of amines. (Applying).','امائنز کی نام گذاری، ساخت اور اساسیت پر بحث کریں۔ (اطلاق)','د امینونو پر نومولو، جوړښت او قلویت بحث وکړي. (تطبیق)'),
 ('Describe the preparation of amines by alkylation of ammonia with RX and reduction of nitriles, nitro and amide functional groups. (Applying).','RX سے امونیا کی الکائلیشن اور نائٹرائلز، نائٹرو اور امائیڈ فعلی گروپوں کی تخفیف سے امائنز کی تیاری بیان کریں۔ (اطلاق)','له RX سره د امونیا د الکایلېشن او د نایټرایلونو، نایټرو او اماید فعالو ګروپونو د ارجاع په واسطه د امینونو چمتو کول بیان کړي. (تطبیق)'),
 ('Discuss the reactivity of amines. (Applying)','امائنز کی تعامل پذیری پر بحث کریں۔ (اطلاق)','د امینونو پر تعامل وړتیا بحث وکړي. (تطبیق)'),
 ('Describe the chemistry of amines by alkylation of amines with RX, reactions with aldehydes, ketones, preparation of amides and diazonium salts. (Applying).','RX سے امائنز کی الکائلیشن، الڈیہائیڈز اور کیٹونز سے تعاملات، امائیڈز اور ڈائی ایزونیم نمکیات کی تیاری کے ذریعے امائنز کی کیمیا بیان کریں۔ (اطلاق)','له RX سره د امینونو د الکایلېشن، له الدیهایډونو او کیټونونو سره د تعاملونو، د امایډونو او ډای ازونیم مالګو د جوړولو له لارې د امینونو کیمیا بیان کړي. (تطبیق)'),
 ('Describe isomerism of alkyl halides and amines. (Understanding)','الکائل ہیلائیڈز اور امائنز کا آئسومرزم بیان کریں۔ (سمجھنا)','د الکایل هالایډونو او امینونو ایزومېریزم بیان کړي. (پوهېدل)')]
s0=len(paras)
for r in out:paras.append(pair(*r))
layout.append({'type':'list','indices':list(range(s0,len(paras)))})
visual('chem12-p85-cover-models',cover)
add('Introduction','تعارف','پېژندنه','heading')
add('17.1 Alkyl Halides','17.1 الکائل ہیلائیڈز','17.1 الکایل هالایډونه','heading')
add('Halogen derivatives of alkanes are called haloalkanes. Haloalkanes are formed by replacing one or more hydrogen atoms from alkanes by halogens. They are also called organohalogen compounds. Haloalkanes may be monohaloalkanes, dihaloalkanes, trihaloalkanes etc., depending upon the number of halogen atoms present in the molecule.',
 'الکینز (اکیلے بند والے) کے ہیلوجن مشتقات ہیلو الکینز کہلاتے ہیں۔ ہیلو الکینز الکینز کے ایک یا زیادہ ہائیڈروجن ایٹموں کو ہیلوجنز سے بدلنے سے بنتے ہیں۔ انہیں آرگینو ہیلوجن مرکبات بھی کہتے ہیں۔ سالمے میں موجود ہیلوجن ایٹموں کی تعداد کے لحاظ سے ہیلو الکینز مونو ہیلو الکینز، ڈائی ہیلو الکینز، ٹرائی ہیلو الکینز وغیرہ ہو سکتے ہیں۔',
 'د الکانونو هالوجني مشتقات هالوالکانونه بلل کېږي. هالوالکانونه د الکانونو د یوه یا ډېرو هایدروجني اټومونو په هالوجنونو د بدلولو په واسطه جوړېږي. دوی ته عضوي هالوجني مرکبات هم وايي. په مالیکول کې د شته هالوجني اټومونو د شمېر پر بنسټ هالوالکانونه کېدای شي مونوهالوالکانونه، ډای هالوالکانونه، ټرای هالوالکانونه او نور وي.')
add('Monohaloalkanes are usually called alkyl halides. The functional group of alkyl halides is halogen. They are represented by R–X, where R- is an alkyl group represented by CₙH₂ₙ₊₁ and –X is halogen which is the functional group. The general formula of alkyl halides is CₙH₂ₙ₊₁X, where n represents the number of carbon atoms.',
 'مونو ہیلو الکینز کو عموماً الکائل ہیلائیڈز کہا جاتا ہے۔ الکائل ہیلائیڈز کا فعلی گروپ ہیلوجن ہے۔ انہیں R–X سے ظاہر کیا جاتا ہے، جہاں R- الکائل گروپ ہے جسے CₙH₂ₙ₊₁ سے ظاہر کیا جاتا ہے اور –X ہیلوجن ہے جو فعلی گروپ ہے۔ الکائل ہیلائیڈز کا عمومی فارمولا CₙH₂ₙ₊₁X ہے، جہاں n کاربن ایٹموں کی تعداد ہے۔',
 'مونوهالوالکانونه معمولاً الکایل هالایډونه بلل کېږي. د الکایل هالایډونو فعال ګروپ هالوجن دی. دوی په R–X ښودل کېږي، چې R- الکایل ګروپ دی او په CₙH₂ₙ₊₁ ښودل کېږي او –X هالوجن دی چې فعال ګروپ دی. د الکایل هالایډونو عمومي فورمول CₙH₂ₙ₊₁X دی، چې n د کاربني اټومونو شمېر ښيي.')
add('Alkyl halides are classified according to the nature of the carbon atom bonded to the halogen. If the halogen-bearing carbon is bonded to one carbon atom, it is primary (1°) and the alkyl halide is a primary alkyl halide. If two carbon atoms are bonded to the halogen-bearing carbon, it is secondary (2°) and the compound is a secondary alkyl halide. A tertiary alkyl halide (3°) has three other carbon atoms bonded to the halogen–bearing carbon atom. If the halogen-bearing carbon atom is a methyl group (bonded to no other carbon atoms), the compound is a methyl halide.',
 'الکائل ہیلائیڈز کی درجہ بندی ہیلوجن سے جڑے کاربن ایٹم کی نوعیت کے لحاظ سے کی جاتی ہے۔ اگر ہیلوجن والا کاربن ایک کاربن ایٹم سے جڑا ہو تو وہ ابتدائی (1°) ہے اور الکائل ہیلائیڈ ابتدائی الکائل ہیلائیڈ ہے۔ اگر ہیلوجن والے کاربن سے دو کاربن ایٹم جڑے ہوں تو وہ ثانوی (2°) ہے اور مرکب ثانوی الکائل ہیلائیڈ ہے۔ ثالثی الکائل ہیلائیڈ (3°) میں ہیلوجن والے کاربن ایٹم سے تین دوسرے کاربن ایٹم جڑے ہوتے ہیں۔ اگر ہیلوجن والا کاربن ایٹم میتھائل گروپ ہو (کسی دوسرے کاربن ایٹم سے نہ جڑا ہو) تو مرکب میتھائل ہیلائیڈ ہے۔',
 'الکایل هالایډونه له هالوجن سره د تړلي کاربني اټوم د طبیعت پر بنسټ ډلبندي کېږي. که هالوجن لرونکی کاربن له یوه کاربني اټوم سره تړلی وي، لومړنی (1°) دی او الکایل هالایډ لومړنی الکایل هالایډ دی. که له هالوجن لرونکي کاربن سره دوه کاربني اټومونه تړلي وي، دویمی (2°) دی او مرکب دویمی الکایل هالایډ دی. درېیمی الکایل هالایډ (3°) له هالوجن لرونکي کاربني اټوم سره درې نور کاربني اټومونه لري. که هالوجن لرونکی کاربني اټوم میتایل ګروپ وي (له بل کاربني اټوم سره نه وي تړلی)، مرکب میتایل هالایډ دی.')
visual('chem12-p85-halide-classes',classes)
add('17.1.1 Nomenclature','17.1.1 نام گذاری','17.1.1 نومول','heading')
add('There are two ways of naming alkyl halides. The common (trivial) system and systematic (IUPAC) nomenclature.','الکائل ہیلائیڈز کے نام رکھنے کے دو طریقے ہیں: عام (روایتی) نظام اور نظامی (IUPAC) نام گذاری۔','د الکایل هالایډونو د نومولو دوه لارې دي: عام (دودیز) سیستم او سیستماتیک (IUPAC) نومول.')
add('(a) Common system','(a) عام نظام','(a) عام سیستم','heading')
add('Common or “trivial” names are constructed by naming the alkyl group followed by the term halide. This is the origin of the term alkyl halide. Common names are useful only for simple alkyl halides, such as the following:',
 'عام یا ”روایتی“ نام الکائل گروپ کا نام لے کر اس کے بعد لفظ ہیلائیڈ لگا کر بنائے جاتے ہیں۔ اصطلاح الکائل ہیلائیڈ کی اصل یہی ہے۔ عام نام صرف سادہ الکائل ہیلائیڈز کے لیے مفید ہیں، جیسے درج ذیل:',
 'عام یا ”دودیز“ نومونه د الکایل ګروپ په نومولو او ورپسې د هالایډ کلمې په راوړلو جوړېږي. د الکایل هالایډ اصطلاح اصل همدا دی. عام نومونه یوازې د ساده الکایل هالایډونو لپاره ګټور دي، لکه لاندې:')
visual('chem12-p85-common-names',common)

record=section('17.1','Unit 17 opener, introduction to alkyl halides and common names','یونٹ 17 کا آغاز، الکائل ہیلائیڈز کا تعارف اور عام نام','د 17 واحد پیل، د الکایل هالایډونو پېژندنه او عام نومونه',paras,layout,blocks,'162–163')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':85,'printedPages':[162,163]}]
record['sourceContinuesOnPdfPage']=86
record['sourceCoverIllustrationReview']='Cover ball-and-stick chain is decorative; instructional sp³ amine and tetrahedral CH₃Cl models on printed 162 reconstructed as coded SVG.'
carry=[{'from':'17.1','to':'17.2','startsAt':'H,C-C-CI\nH,C-C-Cl'}]
if __name__=='__main__':save(85,[record],carry=carry,chapter_number=17)
