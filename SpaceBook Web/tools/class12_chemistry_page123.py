"""PDF123 printed238–239: Wolf–Kishner (acetone), reduction with hydrides, carbon nucleophiles (Grignard, HCN), nitrogen nucleophiles."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl,tetra
F=Fig('arrow123');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k);T=lambda *a,**k:tetra(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'acetone':('ایسیٹون','اسیتون'),'hydrazine':('ہائیڈرازین','هایدرازین'),'acetone hydrazone':('ایسیٹون ہائیڈرازون','د اسیتون هایدرازون'),'propane':('پروپین (اکیلا بند)','پروپان'),'aldehyde/ketone':('الڈیہائیڈ/کیٹون','الدیهاید/کیټون'),
   'alcohol':('الکوحل','الکول'),'hydrogen cyanide':('ہائیڈروجن سائنائیڈ','هایدروجن سیانایډ'),'cyanohydrin':('سائنو ہائیڈرن','سیانوهایډرین'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),
   '2-hydroxypropanenitrile':('2-ہائیڈروآکسی پروپین نائٹرائل','2-هایدروکسي پروپان نایټرایل'),'(acetaldehdye cyanohydrin)':('(ایسیٹ الڈیہائیڈ سائنو ہائیڈرن)','(د اسیټالدیهاید سیانوهایډرین)'),
   '2-hydroxy-2-methylpropanenitrile':('2-ہائیڈروآکسی-2-میتھائل پروپین نائٹرائل','2-هایدروکسي-2-میتایل پروپان نایټرایل'),'(acetone cyanohydrin)':('(ایسیٹون سائنو ہائیڈرن)','(د اسیتون سیانوهایډرین)'),
   'ammonia or':('امونیا یا','امونیا یا'),'ammonia derivative':('امونیا مشتق','د امونیا مشتق'),'imine or derivative':('امین یا مشتق','ایمین یا مشتق'),'(Condensation product)':('(تکثیفی پیداوار)','(د تراکم محصول)'),
   'oxonium ion':('آکسونیم آئن','اکسونیم ایون'),'addition product':('اضافی پیداوار','اضافي محصول'),'condensation':('تکثیفی','د تراکم'),'product':('پیداوار','محصول')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def wk(lang):
 s=F.start(110)+C(110,70,'CH₃','CH₃')+t(110,92,lb(lang,'acetone'),12)+t(240,70,'+ NH₂—NH₂',15)+t(250,92,lb(lang,'hydrazine'),12)+F.arrow(310,370,64,'','−H₂O')
 s+=t(440,32,'N—NH₂',14)+line(437,38,437,54)+line(443,38,443,54)+t(440,70,'CH₃—C—CH₃',15)+t(440,92,lb(lang,'acetone hydrazone'),12)+F.arrow(500,610,64,'KOH, 200°C','−N₂')+t(700,70,'CH₃—CH₂—CH₃',15)+t(700,92,lb(lang,'propane'),12)
 return s+'</svg>'
def hyd(lang):
 s=F.start(250)+C(160,60)+t(160,84,lb(lang,'aldehyde/ketone'),12)+F.arrow(300,500,54,'1. LiAlH₄ or NaBH₄, ether','2. H₂O')+T(620,60,'OH','','','H')+t(620,118,lb(lang,'alcohol'),12)
 s+=C(160,180)+t(230,180,'+ H₂',15)+t(160,204,lb(lang,'aldehyde/ketone'),12)+F.arrow(300,500,174,'Ni or Pt or Pd')+T(620,180,'OH','','','H')+t(620,238,lb(lang,'alcohol'),12)
 return s.replace('viewBox="0 0 850 250"','viewBox="0 0 850 250"')+'</svg>'
def hcn(lang,items):
 s=F.start(140*len(items)+10)
 for i,(l,r,n,pr,p1,p2) in enumerate(items):
  y=60+140*i;s+=C(140,y,l,r)+t(140,y+24,lb(lang,n),12)+t(300,y,'+  H—CN',15)+t(310,y+24,lb(lang,'hydrogen cyanide'),12)+F.arrow(380,480,y-6,'KCN')
  s+=T(600,y,'OH',l,pr,'CN')+(t(600,y+58,lb(lang,p1),12)+(t(600,y+74,lb(lang,p2),12) if p2 else ''))
 return s+'</svg>'
def nitro(lang):
 s=F.start(130)+C(140,70)+t(140,94,lb(lang,'aldehyde/ketone'),12)+t(240,70,'+',16)+t(330,34,'H',14)+line(330,40,330,56)+t(330,70,'H—N—X',15)+t(330,92,lb(lang,'ammonia or'),12)+t(330,108,lb(lang,'ammonia derivative'),12)
 s+=F.eq(410,490,64)+t(450,50,'H⁺',12)+t(570,32,'N—X',14)+line(567,38,567,54)+line(573,38,573,54)+t(570,70,'—C—',15)+t(670,70,'+ H₂O',15)+t(570,92,lb(lang,'imine or derivative'),12)+t(570,108,lb(lang,'(Condensation product)'),12)
 return s+'</svg>'
def mech(lang):
 s=F.start(140)+C(70,70)+t(70,94,lb(lang,'aldehyde/ketone'),11)+F.eq(115,165,64)+t(140,52,'H⁺',11)
 s+=t(210,32,'O⁺—H',13)+line(207,38,207,54)+line(213,38,213,54)+t(210,70,'—C—',14)+t(210,94,lb(lang,'oxonium ion'),11)+F.eq(265,325,64)+t(295,52,'N̈H₂X',11)+t(295,86,'−H⁺',11)
 s+=T(390,70,'OH','','','NHX',14)+t(390,128,lb(lang,'addition product'),11)+F.eq(445,505,64)+t(475,52,'H⁺',11)+T(570,70,'O⁺H₂','','','XN—H',14)+F.eq(630,690,64)+t(660,86,'−H⁺',11)
 s+=t(750,32,'N—X',13)+line(747,38,747,54)+line(753,38,753,54)+t(750,70,'—C—',14)+t(805,70,'+ H₂O',13)+t(750,94,lb(lang,'condensation'),11)+t(750,108,lb(lang,'product'),11)
 return s+'</svg>'

visual('chem12-p123-wk-acetone',wk)
add('19.6.3.2 Using Hydrides to give Alcohols','19.6.3.2 ہائیڈرائیڈز سے الکوحلز بنانا','19.6.3.2 د هایدرایډونو په واسطه الکولونه ورکول','heading')
add('Aldehydes and ketones are reduced to alcohols, by using catalytic method or metal hydrides (Section 18.1.5.5). Formaldehyde produces methyl alcohol, higher aldehydes give primary alcohols while ketones yield secondary alcohols.','الڈیہائیڈز اور کیٹونز کی عمل انگیز طریقے یا دھاتی ہائیڈرائیڈز سے الکوحلز تک تخفیف کی جاتی ہے (حصہ 18.1.5.5)۔ فارم الڈیہائیڈ میتھائل الکوحل، بڑے الڈیہائیڈز ابتدائی الکوحلز جبکہ کیٹونز ثانوی الکوحلز دیتے ہیں۔','الدیهایډونه او کیټونونه د کتلستي طریقې یا فلزي هایدرایډونو په کارولو الکولونو ته ارجاع کېږي (برخه 18.1.5.5). فورمالدیهاید میتایل الکول، لوړ الدیهایډونه لومړني الکولونه او کیټونونه دویمي الکولونه ورکوي.')
visual('chem12-p123-hydrides',hyd)
add('19.6.3.3 Using Carbon Nucleophiles','19.6.3.3 کاربن نیوکلیوفائلز کا استعمال','19.6.3.3 د کاربن نیوکلیوفایلونو کارول','heading')
add('Carbon nucleophiles, such as Grignard reagent and hydrogen cyanide, can also convert the carbonyl group into hydroxyl group.','کاربن نیوکلیوفائلز، جیسے گرینیارڈ عامل اور ہائیڈروجن سائنائیڈ، بھی کاربونل گروپ کو ہائیڈروآکسل گروپ میں بدل سکتے ہیں۔','د کاربن نیوکلیوفایلونه لکه ګرینیارډ عامل او هایدروجن سیانایډ هم کاربونیل ګروپ په هایدروکسیل ګروپ بدلولی شي.')
add('(a) Using Grignard Reagent','(a) گرینیارڈ عامل کا استعمال','(a) د ګرینیارډ عامل کارول','heading')
add('Grignard reagents act as carbon nucleophiles toward carbonyl compounds. The R- group of the Grignard reagent adds irreversibly to the carbonyl carbon, forming a new carbon-carbon bond in the intermediate alkoxide (addition product). The alkoxide upon acid workup gives alcohol (Section 17.2.3.1).','گرینیارڈ عاملین کاربونل مرکبات کے لیے کاربن نیوکلیوفائل کا کام کرتے ہیں۔ گرینیارڈ عامل کا R- گروپ ناقابلِ واپسی طور پر کاربونل کاربن میں شامل ہوتا ہے اور درمیانی الکوآکسائیڈ (اضافی پیداوار) میں نیا کاربن–کاربن بند بناتا ہے۔ الکوآکسائیڈ تیزابی ورک اپ پر الکوحل دیتا ہے (حصہ 17.2.3.1)۔','ګرینیارډ عاملونه د کاربونیل مرکباتو په وړاندې د کاربن نیوکلیوفایل په توګه عمل کوي. د ګرینیارډ عامل R- ګروپ په نه بېرته ګرځېدونکي ډول کاربونیل کاربن ته ورزیاتېږي او په منځني الکوکساید (اضافي محصول) کې نوی کاربن–کاربن تړون جوړوي. الکوکساید د اسیدي ورک اپ پر مهال الکول ورکوي (برخه 17.2.3.1).')
add('(b) Using Hydrogen Cyanide (HCN)','(b) ہائیڈروجن سائنائیڈ (HCN) کا استعمال','(b) د هایدروجن سیانایډ (HCN) کارول','heading')
add('The carbon in hydrogen cyanide also acts as carbon nucleophile and undergoes nucleophillic addition to aldehydes and ketones in the presence of a cyanide base to yield cyanohydrins.','ہائیڈروجن سائنائیڈ کا کاربن بھی کاربن نیوکلیوفائل کا کام کرتا ہے اور سائنائیڈ اساس کی موجودگی میں الڈیہائیڈز اور کیٹونز میں نیوکلیوفائلی اضافہ کر کے سائنو ہائیڈرنز دیتا ہے۔','په هایدروجن سیانایډ کې کاربن هم د کاربن نیوکلیوفایل په توګه عمل کوي او د سیانایډ قلوي په شتون کې الدیهایډونو او کیټونونو ته نیوکلیوفایلي اضافه کوي او سیانوهایډرینونه ورکوي.')
visual('chem12-p123-hcn-general',lambda l:hcn(l,[('','','aldehyde/ketone','','cyanohydrin',None)]))
add('Some examples of cyanohydrins formation are given below.','سائنو ہائیڈرنز بننے کی چند مثالیں درج ذیل ہیں۔','د سیانوهایډرینونو د جوړېدو ځینې بېلګې لاندې ورکړل شوې.')
visual('chem12-p123-hcn-examples',lambda l:hcn(l,[('CH₃','H','acetaldehyde','H','2-hydroxypropanenitrile','(acetaldehdye cyanohydrin)'),('CH₃','CH₃','acetone','CH₃','2-hydroxy-2-methylpropanenitrile','(acetone cyanohydrin)')]))
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Cyanohydrins are compounds with a hydroxyl (–OH) and cyano (–CN) groups attached to the same carbon.','سائنو ہائیڈرنز وہ مرکبات ہیں جن میں ہائیڈروآکسل (–OH) اور سائنو (–CN) گروپ ایک ہی کاربن سے جڑے ہوں۔','سیانوهایډرینونه هغه مرکبات دي چې پکې هایدروکسیل (–OH) او سیانو (–CN) ګروپونه له یوه کاربن سره تړلي وي.','list')
add('Ammonia and ammonia derivatives act as nucleophiles toward the carbonyl carbon atoms because of presence of unshared electron pair on nitrogen atom in these compounds.','امونیا اور امونیا کے مشتقات کاربونل کاربن ایٹموں کے لیے نیوکلیوفائل کا کام کرتے ہیں کیونکہ ان مرکبات میں نائٹروجن ایٹم پر غیر مشترک الیکٹرانی جوڑا ہوتا ہے۔','امونیا او د امونیا مشتقات د کاربونیل کاربني اټومونو په وړاندې د نیوکلیوفایلونو په توګه عمل کوي ځکه په دې مرکباتو کې پر نایتروجني اټوم نه شریکه الکتروني جوړه شته.','list')
add('19.6.3.4 Using Nitrogen Nucleophiles','19.6.3.4 نائٹروجن نیوکلیوفائلز کا استعمال','19.6.3.4 د نایتروجن نیوکلیوفایلونو کارول','heading')
add('Ammonia and ammonia derivatives such as primary amines (R–NH₂), hydroxyl amine (NH₂–OH), hydrazine (NH₂–NH₂) and phenyl hydrazine (NH₂–NH–C₆H₅) add to carbonyl group of aldehyde and ketone in the presence of acid catalyst to form an unstable addition product. The stabilization of addition product is achieved by dehydration, to form a condensation product which are imine or imine derivatives.',
 'امونیا اور امونیا کے مشتقات جیسے ابتدائی امائنز (R–NH₂)، ہائیڈروآکسل امائن (NH₂–OH)، ہائیڈرازین (NH₂–NH₂) اور فینائل ہائیڈرازین (NH₂–NH–C₆H₅) تیزابی عمل انگیز کی موجودگی میں الڈیہائیڈ اور کیٹون کے کاربونل گروپ میں شامل ہو کر ایک ناپائیدار اضافی پیداوار بناتے ہیں۔ اضافی پیداوار کی پائیداری آب ربائی سے حاصل ہوتی ہے، جس سے تکثیفی پیداوار یعنی امین یا امین مشتقات بنتے ہیں۔',
 'امونیا او د امونیا مشتقات لکه لومړني امینونه (R–NH₂)، هایدروکسیل امین (NH₂–OH)، هایدرازین (NH₂–NH₂) او فینیل هایدرازین (NH₂–NH–C₆H₅) د اسیدي کتلست په شتون کې د الدیهاید او کیټون کاربونیل ګروپ ته ورزیاتېږي او یو بې ثباته اضافي محصول جوړوي. د اضافي محصول ثبات د اوبو ایستلو په واسطه ترلاسه کېږي، چې د تراکم محصول یعنې ایمین یا د ایمین مشتقات جوړوي.')
visual('chem12-p123-nitrogen',nitro)
add('The reaction is catalyzed by an acid. The mechanism is similar to general acid-catalysed mechanism discussed in Section 19.6.1.','یہ تعامل تیزاب سے عمل انگیز ہوتا ہے۔ اس کا طریق کار حصہ 19.6.1 میں بیان کردہ عمومی تیزابی عمل انگیز طریق کار جیسا ہے۔','دا تعامل د اسید په واسطه کتلست کېږي. میکانیزم یې په 19.6.1 برخه کې بیان شوي عمومي اسیدي کتلستي میکانیزم ته ورته دی.')
visual('chem12-p123-nitrogen-mechanism',mech)
add('Reactions of ammonia and ammonia derivatives are given below.','امونیا اور امونیا کے مشتقات کے تعاملات درج ذیل ہیں۔','د امونیا او د امونیا د مشتقاتو تعاملونه لاندې ورکړل شوي.')
record=section('19.7','Reduction with hydrides; carbon and nitrogen nucleophiles','ہائیڈرائیڈز سے تخفیف؛ کاربن اور نائٹروجن نیوکلیوفائلز','د هایدرایډونو په واسطه ارجاع؛ د کاربن او نایتروجن نیوکلیوفایلونه',paras,layout,blocks,'238–239')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':123,'printedPages':[238,239]}]
record['sourceContinuesOnPdfPage']=124
if __name__=='__main__':save(123,[record],chapter_number=19)
