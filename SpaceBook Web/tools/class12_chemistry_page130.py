"""PDF130 printed252–253: IUPAC names of acids; nomenclature of acid halides, amides, esters, anhydrides, nitriles."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain,carbonyl
import math
F=Fig('arrow130');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
 return P,L,B,add,visual
U={'methanoic acid':'میتھانوئک ایسڈ','ethanoic acid':'ایتھانوئک ایسڈ','propanoic acid':'پروپانوئک ایسڈ','3-methylbutanoic acid':'3-میتھائل بیوٹانوئک ایسڈ','2-bromo-3-methylbutanoic acid':'2-برومو-3-میتھائل بیوٹانوئک ایسڈ',
 'ethanedioic acid':'ایتھین ڈائی اوئک ایسڈ','(oxalic acid)':'(آکزیلک ایسڈ)','propanedioic acid':'پروپین ڈائی اوئک ایسڈ','(malonic acid)':'(میلونک ایسڈ)','butanedioic acid':'بیوٹین ڈائی اوئک ایسڈ','(succinic acid)':'(سکسینک ایسڈ)',
 'propenoic acid':'پروپینوئک ایسڈ','2-butynoic acid (but-2-ynoic acid)':'2-بیوٹائنوئک ایسڈ (بیوٹ-2-ائنوئک ایسڈ)','cyclohexanecarboxylic acid':'سائیکلوہیکسین کاربوکسلک ایسڈ','cyclopentanecarboxylic acid':'سائیکلوپینٹین کاربوکسلک ایسڈ',
 'Common name:':'عام نام:','IUPAC name:':'IUPAC نام:'}
Pz={'methanoic acid':'میتانویک اسید','ethanoic acid':'ایتانویک اسید','propanoic acid':'پروپانویک اسید','3-methylbutanoic acid':'3-میتایل بیوټانویک اسید','2-bromo-3-methylbutanoic acid':'2-برومو-3-میتایل بیوټانویک اسید',
 'ethanedioic acid':'ایتان ډای اویک اسید','(oxalic acid)':'(اکسالیک اسید)','propanedioic acid':'پروپان ډای اویک اسید','(malonic acid)':'(مالونیک اسید)','butanedioic acid':'بیوټان ډای اویک اسید','(succinic acid)':'(سوکسینیک اسید)',
 'propenoic acid':'پروپینویک اسید','2-butynoic acid (but-2-ynoic acid)':'2-بیوټاینویک اسید (بیوټ-2-اینویک اسید)','cyclohexanecarboxylic acid':'سایکلوهېکسان کاربوکسیلیک اسید','cyclopentanecarboxylic acid':'سایکلوپېنټان کاربوکسیلیک اسید',
 'Common name:':'عام نوم:','IUPAC name:':'IUPAC نوم:'}
def lb(lang,v):return v if lang=='en' else (U if lang=='ur' else Pz).get(v,v)
def iupac(lang):
 s=F.start(400)
 for x,(l,n) in zip((150,420,690),(('H','methanoic acid'),('CH₃','ethanoic acid'),('CH₃—CH₂','propanoic acid'))):s+=C(x,60,l,'OH')+t(x,84,lb(lang,n),12)
 s+=chain(F,0,160,['CH₃','—','CH','—','CH₂','—','C','—','OH'],15,{0:'4',2:'3',4:'2',6:'1'},{2:'CH₃',6:'=O'},center=220)+t(220,184,lb(lang,'3-methylbutanoic acid'),12)
 s+=chain(F,0,160,['CH₃','—','CH','—','CH','—','C','—','OH'],15,{0:'4',2:'3',4:'2',6:'1'},{2:'CH₃',4:'Br',6:'=O'},center=620)+t(620,184,lb(lang,'2-bromo-3-methylbutanoic acid'),12)
 s+=chain(F,0,270,['HO','—','C','—','C','—','OH'],15,None,{2:'=O',4:'=O'},center=130)+t(130,294,lb(lang,'ethanedioic acid'),12)+t(130,310,lb(lang,'(oxalic acid)'),12)
 s+=chain(F,0,270,['HO','—','C','—','CH₂','—','C','—','OH'],15,None,{2:'=O',6:'=O'},center=390)+t(390,294,lb(lang,'propanedioic acid'),12)+t(390,310,lb(lang,'(malonic acid)'),12)
 s+=chain(F,0,270,['HO','—','C','—','CH₂','—','CH₂','—','C','—','OH'],14,None,{2:'=O',8:'=O'},center=680)+t(680,294,lb(lang,'butanedioic acid'),12)+t(680,310,lb(lang,'(succinic acid)'),12)
 s+=chain(F,0,370,['CH₂','=','CH','—','COOH'],15,{0:'3',2:'2',4:'1'},center=220)+t(220,394,lb(lang,'propenoic acid'),12)
 s+=chain(F,0,370,['CH₃','—','C','≡','C','—','COOH'],15,{0:'4',2:'3',4:'2',6:'1'},center=620)+t(620,394,lb(lang,'2-butynoic acid (but-2-ynoic acid)'),12)
 return s.replace('viewBox="0 0 850 400"','viewBox="0 0 850 405"')+'</svg>'
def cyclic(lang):
 s=F.start(160)+F.ring(260,80,34,kek=False,subs={1:'COOH'})+t(260,145,lb(lang,'cyclohexanecarboxylic acid'),12)
 pts=[(600+32*math.cos(math.radians(-90+72*i)),85+32*math.sin(math.radians(-90+72*i))) for i in range(5)]
 s+='<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'+line(pts[1][0],pts[1][1],pts[1][0]+18,pts[1][1]-10)+t(pts[1][0]+46,pts[1][1]-8,'COOH',14)+t(600,145,lb(lang,'cyclopentanecarboxylic acid'),12)
 return s+'</svg>'
def table(lang,rows,h=125):
 s=F.start(h)+t(70,86,lb(lang,'Common name:'),12)+t(70,104,lb(lang,'IUPAC name:'),12)
 for x,(struct,cn,iu) in zip((260,480,700),rows):
  s+=struct(x)+t(x,86,cn,12)+t(x,104,iu,12)
 return s+'</svg>'
P,L,B,add,visual=builder()
add('(b) IUPAC Nomenclature','(b) IUPAC نام گذاری','(b) IUPAC نومول','heading')
add('Aliphatic monocarboxylic acids are named as alkanoic acids. These are obtained by replacing the ending ‘–e’ of the corresponding alkane with the suffix ‘–oic acid’ e.g.','ایلیفیٹک مونو کاربوکسلک ایسڈز کے نام الکانوئک ایسڈز کے طور پر رکھے جاتے ہیں۔ یہ متعلقہ الکین (اکیلے بند والے) کے اختتامیہ ’–e‘ کو لاحقہ ’–oic acid‘ سے بدل کر حاصل کیے جاتے ہیں، مثلاً','الیفاتیک مونو کاربوکسیلیک اسیدونه د الکانویک اسیدونو په توګه نومول کېږي. دا د اړوند الکان پای ’–e‘ په ’–oic acid‘ وروستاړي بدلولو ترلاسه کېږي، لکه')
visual('chem12-p130-iupac-acids',iupac)
add('In case of branched acids, the chain is numbered starting from the carboxyl carbon atom and substituents are located in the usual way. Carboxylic acids containing two carboxyl groups are named as alkanedioic acid; their trivial names are also given in parenthesis. Similarly, the unsaturated carboxylic acids are named as alkenoic acid, alkynoic acid (examples shown above).',
 'شاخ دار ایسڈز کی صورت میں زنجیر کو کاربوکسل کاربن ایٹم سے نمبر دیا جاتا ہے اور متبادلات کا مقام معمول کے مطابق بتایا جاتا ہے۔ دو کاربوکسل گروپ رکھنے والے کاربوکسلک ایسڈز کے نام الکین ڈائی اوئک ایسڈ کے طور پر رکھے جاتے ہیں؛ ان کے روایتی نام بھی قوسین میں دیے گئے ہیں۔ اسی طرح غیر سیر شدہ کاربوکسلک ایسڈز کے نام الکینوئک ایسڈ، الکائنوئک ایسڈ رکھے جاتے ہیں (مثالیں اوپر دکھائی گئی ہیں)۔',
 'د څانګه لرونکو اسیدونو په حالت کې ځنځیر له کاربوکسیل کاربني اټوم څخه شمېرل کېږي او بدیلونه په معمول ډول ښودل کېږي. هغه کاربوکسیلیک اسیدونه چې دوه کاربوکسیل ګروپونه لري، د الکان ډای اویک اسید په توګه نومول کېږي؛ دودیز نومونه یې هم په قوسونو کې ورکړل شوي. همدارنګه نامشبوع کاربوکسیلیک اسیدونه د الکینویک اسید، الکاینویک اسید په توګه نومول کېږي (بېلګې پورته ښودل شوې).')
add('If carboxyl group is attached to a cyclic ring, it is named by adding suffix –carboxylic acid to name of cycloalkane.','اگر کاربوکسل گروپ کسی حلقے سے جڑا ہو تو سائیکلوالکین کے نام کے ساتھ لاحقہ –carboxylic acid لگا کر نام رکھا جاتا ہے۔','که کاربوکسیل ګروپ له کړۍ سره تړلی وي، د سایکلوالکان له نوم سره د –carboxylic acid وروستاړي په زیاتولو نومول کېږي.')
visual('chem12-p130-cyclic-acids',cyclic)
add('Nomenclature of acid halides','ایسڈ ہیلائیڈز کی نام گذاری','د اسید هالایډونو نومول','heading')
add('The names of acid halides are derived from the names of corresponding carboxylic acids. The ending –ic of the name of acid is replaced by –yl, and the word acid is replaced by halide, in both common and IUPAC systems.','ایسڈ ہیلائیڈز کے نام متعلقہ کاربوکسلک ایسڈز کے ناموں سے اخذ کیے جاتے ہیں۔ عام اور IUPAC دونوں نظاموں میں ایسڈ کے نام کا اختتامیہ –ic، –yl سے اور لفظ acid، halide سے بدل دیا جاتا ہے۔','د اسید هالایډونو نومونه د اړوندو کاربوکسیلیک اسیدونو له نومونو اخیستل کېږي. په عام او IUPAC دواړو سیستمونو کې د اسید د نوم پای –ic په –yl او د acid کلمه په halide بدلېږي.')
visual('chem12-p130-acid-halides',lambda l:table(l,[(lambda x:C(x,58,'H','Cl'),'formyl chloride','methanoyl chloride'),(lambda x:C(x,58,'CH₃','Cl'),'acetyl chloride','ethanoyl chloride'),(lambda x:C(x,58,'CH₃—CH₂','Cl'),'propionyl chloride','propanoyl chloride')]))
r2=section('20.2','IUPAC names of carboxylic acids and acid halides','کاربوکسلک ایسڈز اور ایسڈ ہیلائیڈز کے IUPAC نام','د کاربوکسیلیک اسیدونو او اسید هالایډونو IUPAC نومونه',P,L,B,'252')
r2['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':130,'printedPages':[252]}]
P,L,B,add,visual=builder()
add('Nomenclature of amides','امائیڈز کی نام گذاری','د امایډونو نومول','heading')
add('Names of amides are also derived from carboxylic acids. The ending –ic acid of common names and –oic acid from IUPAC name is replaced by –amide.','امائیڈز کے نام بھی کاربوکسلک ایسڈز سے اخذ ہوتے ہیں۔ عام ناموں کا اختتامیہ –ic acid اور IUPAC نام کا –oic acid، –amide سے بدل دیا جاتا ہے۔','د امایډونو نومونه هم له کاربوکسیلیک اسیدونو اخیستل کېږي. د عامو نومونو پای –ic acid او د IUPAC نوم –oic acid په –amide بدلېږي.')
visual('chem12-p130-amides',lambda l:table(l,[(lambda x:C(x,58,'H','NH₂'),'formamide','methanamide'),(lambda x:C(x,58,'CH₃','NH₂'),'acetamide','ethanamide'),(lambda x:C(x,58,'CH₃—CH₂','NH₂'),'propionamide','propanamide')]))
add('Nomenclature of esters','ایسٹرز کی نام گذاری','د ایسټرونو نومول','heading')
add('The names of esters consist of two words. The first word is derived from the alkyl group of the alcohol (alkyl group attached to oxygen), and the second word from the carboxylate group of the carboxylic acid, with the ending –ic acid is replaced by –ate in both common and IUPAC systems.','ایسٹرز کے نام دو الفاظ پر مشتمل ہوتے ہیں۔ پہلا لفظ الکوحل کے الکائل گروپ (آکسیجن سے جڑا الکائل گروپ) سے اور دوسرا لفظ کاربوکسلک ایسڈ کے کاربوکسیلیٹ گروپ سے اخذ ہوتا ہے، اور عام اور IUPAC دونوں نظاموں میں اختتامیہ –ic acid، –ate سے بدل دیا جاتا ہے۔','د ایسټرونو نومونه له دوو کلمو جوړ دي. لومړۍ کلمه د الکول له الکایل ګروپ (له اکسیجن سره تړلی الکایل ګروپ) او دویمه کلمه د کاربوکسیلیک اسید له کاربوکسیلېټ ګروپ اخیستل کېږي، او په عام او IUPAC دواړو سیستمونو کې پای –ic acid په –ate بدلېږي.')
def esters(lang):
 s=F.start(125)+t(60,86,lb(lang,'Common name:'),11)+t(60,104,lb(lang,'IUPAC name:'),11)
 for x,(l,r,cn,iu) in zip((200,390,570,750),(('H','OCH₃','methyl formate','methyl methanoate'),('CH₃','OCH₃','methyl acetate','methyl ethanoate'),('CH₃','OC₂H₅','ethyl acetate','ethyl ethanoate'),('CH₃—CH₂','OCH₃','methyl propionate','methyl propanoate'))):s+=C(x,58,l,r,size=14)+t(x,86,cn,11)+t(x,104,iu,11)
 return s+'</svg>'
visual('chem12-p130-esters',esters)
add('Nomenclature of acid anhydrides','ایسڈ این ہائیڈرائیڈز کی نام گذاری','د اسید انهایدرایډونو نومول','heading')
add('Anhydrides are named by replacing the word ‘acid’ of the parent acid by anhydride. For mixed anhydrides, the parent name of each acid is written in alphabetic order, followed by word anhydride.','این ہائیڈرائیڈز کے نام بنیادی ایسڈ کے لفظ ’acid‘ کو anhydride سے بدل کر رکھے جاتے ہیں۔ مخلوط این ہائیڈرائیڈز کے لیے ہر ایسڈ کا بنیادی نام حروفِ تہجی کی ترتیب سے لکھا جاتا ہے اور اس کے بعد لفظ anhydride آتا ہے۔','انهایدرایډونه د اصلي اسید د ’acid‘ کلمې په anhydride بدلولو نومول کېږي. د ګډو انهایدرایډونو لپاره د هر اسید اصلي نوم د الفبا په ترتیب لیکل کېږي او ورپسې د anhydride کلمه راځي.')
def anh(lang):
 s=F.start(125)+t(70,86,lb(lang,'Common name:'),12)+t(70,104,lb(lang,'IUPAC name:'),12)
 s+=chain(F,0,58,['CH₃','—','C','—','O','—','C','—','CH₃'],14,None,{2:'=O',6:'=O'},center=330)+t(330,86,'acetic anhydride',12)+t(330,104,'ethanoic anhydride',12)
 s+=chain(F,0,58,['CH₃','—','CH₂','—','C','—','O','—','C','—','CH₃'],14,None,{4:'=O',8:'=O'},center=640)+t(640,86,'acetic propionic anhydride',12)+t(640,104,'ethanoic propanoic anhydride',12)
 return s+'</svg>'
visual('chem12-p130-anhydrides',anh)
add('Nomenclature of nitriles','نائٹرائلز کی نام گذاری','د نایټرایلونو نومول','heading')
add('Nitriles contain the cyano (–C ≡ N) group. Although nitriles lack the carbonyl group of carboxylic acids, they are classified as acid derivatives because they hydrolyze to give carboxylic acids and can be synthesized by dehydration of amides.','نائٹرائلز میں سائنو (–C ≡ N) گروپ ہوتا ہے۔ اگرچہ نائٹرائلز میں کاربوکسلک ایسڈز کا کاربونل گروپ نہیں ہوتا، پھر بھی انہیں ایسڈ مشتقات میں شمار کیا جاتا ہے کیونکہ یہ ہائیڈرولائز ہو کر کاربوکسلک ایسڈز دیتے ہیں اور امائیڈز کی آب ربائی سے تیار کیے جا سکتے ہیں۔','نایټرایلونه سیانو (–C ≡ N) ګروپ لري. که څه هم نایټرایلونه د کاربوکسیلیک اسیدونو کاربونیل ګروپ نه لري، د اسید مشتقاتو په توګه ګڼل کېږي ځکه هایدرولیز کېږي او کاربوکسیلیک اسیدونه ورکوي او د امایډونو د اوبو ایستلو په واسطه جوړېدای شي.')
add('Common names of nitriles are derived from the corresponding carboxylic acids. Begin with the common name of the acid, and replace the suffix -ic acid with the suffix -onitrile. They can also be named as alkyl cyanides in common system, written in parenthesis. The IUPAC name is constructed from the alkane name, with the suffix -nitrile added.','نائٹرائلز کے عام نام متعلقہ کاربوکسلک ایسڈز سے اخذ کیے جاتے ہیں۔ ایسڈ کے عام نام سے شروع کریں اور لاحقہ -ic acid کو لاحقہ -onitrile سے بدل دیں۔ عام نظام میں انہیں الکائل سائنائیڈز کے طور پر بھی نام دیا جا سکتا ہے، جو قوسین میں لکھے گئے ہیں۔ IUPAC نام الکین (اکیلے بند والے) کے نام کے ساتھ لاحقہ -nitrile لگا کر بنایا جاتا ہے۔','د نایټرایلونو عام نومونه له اړوندو کاربوکسیلیک اسیدونو اخیستل کېږي. د اسید له عام نوم څخه پیل وکړئ او -ic acid وروستاړی په -onitrile بدل کړئ. په عام سیستم کې د الکایل سیانایډونو په توګه هم نومول کېدای شي چې په قوسونو کې لیکل شوي. IUPAC نوم د الکان له نوم سره د -nitrile وروستاړي په زیاتولو جوړېږي.')
def nitr(lang):
 s=F.start(130)+t(70,60,lb(lang,'Common name:'),12)+t(70,104,lb(lang,'IUPAC name:'),12)
 for x,(f,cn,cy,iu) in zip((280,500,720),(('CH₃—C≡N','acetonitrile','(methyl cyanide)','ethanenitrile'),('CH₃—CH₂—C≡N','propiononitrile','(ethyl cyanide)','propanenitrile'),('CH₃—CH₂—CH₂—C≡N','butyronitrile','(n-propyl cyanide)','butanenitrile'))):s+=t(x,35,f,15)+t(x,60,cn,12)+t(x,78,cy,12)+t(x,104,iu,12)
 return s+'</svg>'
visual('chem12-p130-nitriles',nitr)
r3=section('20.3','Nomenclature of amides, esters, anhydrides and nitriles','امائیڈز، ایسٹرز، این ہائیڈرائیڈز اور نائٹرائلز کی نام گذاری','د امایډونو، ایسټرونو، انهایدرایډونو او نایټرایلونو نومول',P,L,B,'253')
r3['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':130,'printedPages':[253]}]
r3['sourceContinuesOnPdfPage']=131
issues=[{'id':'chem12-p252-iupac-text','printedPage':252,'description':'Compound names in the halide/amide/ester/anhydride/nitrile tables are kept in English in all three languages (they are systematic chemical names); prose is translated.'}]
carry=[{'from':'20.3','to':'20.4','startsAt':'The carboxylate ion exists as a resonance'}]
if __name__=='__main__':save(130,[r2,r3],carry=carry,issues=issues,chapter_number=20)
