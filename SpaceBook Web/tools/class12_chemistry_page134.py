"""PDF134 printed262–263: amides, reduction, decarboxylation, reactions of acyl halides and anhydrides."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl,chain,tetra
F=Fig('arrow134');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k);T=lambda *a,**k:tetra(F,*a,**k)
def ch(y,toks,up,center,size=15):return chain(F,0,y,toks,size,None,up,center=center)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'ammonium carboxylate':('امونیم کاربوکسیلیٹ','امونیم کاربوکسیلېټ'),'amide':('امائیڈ','امایډ'),'heat':('حرارت','تودوخه'),'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),
   'ammonium acetate':('امونیم ایسیٹیٹ','امونیم اسیټېټ'),'acetamide':('ایسیٹامائیڈ','اسیټامایډ'),'acetyl chloride':('ایسیٹائل کلورائیڈ','اسیټیل کلوراید'),'ethyl acetate':('ایتھائل ایسیٹیٹ','ایتیل اسیټېټ'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),
   'acetic anhydride':('ایسیٹک این ہائیڈرائیڈ','اسیټیک انهایدراید'),'1° -alcohol':('1° -الکوحل','1° -الکول'),'1. LiAlH₄, ether':('1. LiAlH₄، ایتھر','1. LiAlH₄، ایتر'),'sodium carboxylate':('سوڈیم کاربوکسیلیٹ','سوډیم کاربوکسیلېټ'),'alkane':('الکین','الکان'),
   'sodium acetate':('سوڈیم ایسیٹیٹ','سوډیم اسیټېټ'),'methane':('میتھین','میتان'),'sodium propionate':('سوڈیم پروپیونیٹ','سوډیم پروپیونېټ'),'ethane':('ایتھین','ایتان'),'anhydride':('این ہائیڈرائیڈ','انهایدراید'),'carboxylic acids':('کاربوکسلک ایسڈز','کاربوکسیلیک اسیدونه')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def amide1(lang):
 s=F.start(210)
 for i,(g,n1,n2,n3) in enumerate((('R','carboxylic acid','ammonium carboxylate','amide'),('CH₃','acetic acid','ammonium acetate','acetamide'))):
  y=60+110*i;s+=C(90,y,g,'OH')+t(90,y+24,lb(lang,n1),12)+t(200,y,'+  NH₃',16)+F.arrow(240,300,y-6)+C(390,y,g,'O⁻NH₄⁺')+t(390,y+24,lb(lang,n2),12)+F.arrow(490,570,y-6,lb(lang,'heat'))+C(660,y,g,'NH₂')+t(660,y+24,lb(lang,n3),12)+t(780,y,'+  H₂O',16)
 return s+'</svg>'
def ammonol(lang):
 s=F.start(320)
 s+=C(150,60,'CH₃','Cl')+t(150,84,lb(lang,'acetyl chloride'),12)+t(270,60,'+  NH₃',16)+F.arrow(310,400,54)+C(500,60,'CH₃','NH₂')+t(500,84,lb(lang,'acetamide'),12)+t(650,60,'+  HCl',16)
 s+=C(150,170,'CH₃','OC₂H₅')+t(150,194,lb(lang,'ethyl acetate'),12)+t(290,170,'+  NH₃',16)+F.arrow(330,400,164)+C(500,170,'CH₃','NH₂')+t(500,194,lb(lang,'acetamide'),12)+t(690,170,'+  C₂H₅OH',16)+t(700,194,lb(lang,'ethyl alcohol'),12)
 s+=ch(280,['CH₃','—','C','—','O','—','C','—','CH₃'],{2:'=O',6:'=O'},140)+t(140,304,lb(lang,'acetic anhydride'),12)+t(290,280,'+  NH₃',16)+F.arrow(330,400,274)+C(500,280,'CH₃','NH₂')+t(500,304,lb(lang,'acetamide'),12)+t(600,280,'+',16)+C(700,280,'CH₃','OH')+t(700,304,lb(lang,'acetic acid'),12)
 return s+'</svg>'
def red(lang):
 s=F.start(130)+C(230,60,'R','OH')+t(230,84,lb(lang,'carboxylic acid'),12)+F.arrow(330,460,54,lb(lang,'1. LiAlH₄, ether'),'2. H₂O')+T(570,60,'OH','R','H','H')+t(570,120,lb(lang,'1° -alcohol'),12)
 return s+'</svg>'
def decarb(lang):
 s=F.start(320)
 for i,(g,n1,p,n2) in enumerate((('R','sodium carboxylate','R—H','alkane'),('CH₃','sodium acetate','CH₄','methane'),('C₂H₅','sodium propionate','C₂H₆','ethane'))):
  y=60+110*i;s+=C(170,y,g,'O⁻Na⁺')+t(170,y+24,lb(lang,n1),12)+t(320,y,'+  NaOH',16)+F.arrow(380,480,y-6,'CaO','Δ')+t(540,y,p,16)+t(540,y+24,lb(lang,n2),12)+t(660,y,'+  Na₂CO₃',16)
 return s+'</svg>'
def anhyd(lang):
 s=F.start(110)+ch(60,['R','—','C','—','O','—','C','—',"R′"],{2:'=O',6:'=O'},150)+t(150,86,lb(lang,'anhydride'),12)+t(310,60,'+  H—OH',16)+F.arrow(360,440,54)
 s+=C(530,60,'R','OH')+t(620,60,'+',16)+C(710,60,"R′",'OH')+t(620,86,lb(lang,'carboxylic acids'),12)
 return s+'</svg>'

add('20.7.1.4 Conversion to Amides','20.7.1.4 امائیڈز میں تبدیلی','20.7.1.4 په امایډونو بدلول','heading')
add('Amides are the least reactive of the derivatives of carboxylic acid derivatives. These are obtained by replacing –OH of the acid with –N₂ group.','امائیڈز کاربوکسلک ایسڈ مشتقات میں سب سے کم تعامل پذیر ہیں۔ یہ ایسڈ کے –OH کو –N₂ گروپ سے بدل کر حاصل کیے جاتے ہیں۔','امایډونه د کاربوکسیلیک اسید په مشتقاتو کې تر ټولو لږ تعامل کوونکي دي. دا د اسید د –OH په –N₂ ګروپ بدلولو ترلاسه کېږي.')
add('Amides can be prepared by the reaction of ammonia with carboxylic acid to form first ammonium salts which on heating produce acid amides, upon dehydration.','امائیڈز امونیا کے کاربوکسلک ایسڈ سے تعامل کے ذریعے تیار کیے جا سکتے ہیں جس سے پہلے امونیم نمکیات بنتے ہیں جو گرم کرنے پر پانی کے اخراج سے ایسڈ امائیڈز دیتے ہیں۔','امایډونه له کاربوکسیلیک اسید سره د امونیا د تعامل په واسطه چمتو کېدای شي چې لومړی امونیم مالګې جوړوي او بیا د تودولو پر مهال د اوبو په ایستلو اسید امایډونه ورکوي.')
visual('chem12-p134-amides-from-acids',amide1)
add('Amides can also be prepared by the reaction of ammonia with acid chlorides, esters or anhydrides (ammonolysis).','امائیڈز امونیا کے ایسڈ کلورائیڈز، ایسٹرز یا این ہائیڈرائیڈز سے تعامل (امونولائسز) کے ذریعے بھی تیار کیے جا سکتے ہیں۔','امایډونه له اسید کلوراېډونو، ایسټرونو یا انهایدرایډونو سره د امونیا د تعامل (امونولایسس) په واسطه هم چمتو کېدای شي.')
visual('chem12-p134-ammonolysis',ammonol)
add('20.7.2 Reduction to Alcohols','20.7.2 الکوحلز تک تخفیف','20.7.2 الکولونو ته ارجاع','heading')
add('Carboxylic acids can be reduced to the corresponding primary alcohol using lithium aluminum hydride in ether (Section 18.1.5.6).','ایتھر میں لیتھیم ایلومینیم ہائیڈرائیڈ استعمال کر کے کاربوکسلک ایسڈز کی متعلقہ ابتدائی الکوحل تک تخفیف کی جا سکتی ہے (حصہ 18.1.5.6)۔','کاربوکسیلیک اسیدونه په ایتر کې د لیتیم المونیم هایدراید په کارولو اړوند لومړني الکول ته ارجاع کېدای شي (برخه 18.1.5.6).')
visual('chem12-p134-lialh4-reduction',red)
add('20.7.3 Decarboxylation Reactions','20.7.3 ڈی کاربوکسیلیشن تعاملات','20.7.3 د ډی کاربوکسیلېشن تعاملونه','heading')
add('The removal of carbon dioxide from a carboxylic acid is known as decarboxylation. Decarboxylation of carboxylic acid takes place when its sodium salt is heated with soda lime (dry mixture of caustic soda, NaOH and quick lime, CaO) to form alkanes. The resulting alkane contains one carbon less than parent carboxylic acid.','کاربوکسلک ایسڈ سے کاربن ڈائی آکسائیڈ کے اخراج کو ڈی کاربوکسیلیشن کہتے ہیں۔ کاربوکسلک ایسڈ کی ڈی کاربوکسیلیشن اس وقت ہوتی ہے جب اس کے سوڈیم نمک کو سوڈا لائم (کاسٹک سوڈا NaOH اور بجھے بغیر چونے CaO کا خشک آمیزہ) کے ساتھ گرم کیا جائے، جس سے الکینز بنتے ہیں۔ حاصل ہونے والے الکین میں اصل کاربوکسلک ایسڈ سے ایک کاربن کم ہوتا ہے۔','له کاربوکسیلیک اسید څخه د کاربن ډای اکساید لرې کولو ته ډی کاربوکسیلېشن وايي. د کاربوکسیلیک اسید ډی کاربوکسیلېشن هغه وخت کېږي چې د هغه سوډیم مالګه له سوډا لایم (د کاسټیک سوډا NaOH او ژوندي چونې CaO وچه ګډوله) سره توده شي، او الکانونه جوړوي. حاصل شوی الکان د اصلي کاربوکسیلیک اسید په پرتله یو کاربن کم لري.')
visual('chem12-p134-decarboxylation',decarb)
add('20.7.4 Reactions of Carboxylic Acid Derivatives','20.7.4 کاربوکسلک ایسڈ مشتقات کے تعاملات','20.7.4 د کاربوکسیلیک اسید د مشتقاتو تعاملونه','heading')
add('20.7.4.1 Reactions of Acyl Halides','20.7.4.1 ایسائل ہیلائیڈز کے تعاملات','20.7.4.1 د اسایل هالایډونو تعاملونه','heading')
add('Acid halides are the most reactive of all derivatives of carboxylic acid.','ایسڈ ہیلائیڈز کاربوکسلک ایسڈ کے تمام مشتقات میں سب سے زیادہ تعامل پذیر ہیں۔','اسید هالایډونه د کاربوکسیلیک اسید په ټولو مشتقاتو کې تر ټولو ډېر تعامل کوونکي دي.')
add('(i) Friedel–Crafts Acylation Reaction','(i) فریڈل–کرافٹس ایسائلیشن تعامل','(i) د فریډل–کرافټس اسایلېشن تعامل','heading')
add('Acid halides react with benzene in the presence of Lewis acid to form aromatic ketones. (Section 16.8.5.2.6).','ایسڈ ہیلائیڈز لیوس ایسڈ کی موجودگی میں بینزین سے تعامل کر کے ارومیٹک کیٹونز بناتے ہیں۔ (حصہ 16.8.5.2.6)۔','اسید هالایډونه د لیوس اسید په شتون کې له بنزین سره تعامل کوي او اروماتیک کیټونونه جوړوي. (برخه 16.8.5.2.6).')
add('20.7.4.2 Reactions of Acid Anhydrides','20.7.4.2 ایسڈ این ہائیڈرائیڈز کے تعاملات','20.7.4.2 د اسید انهایدرایډونو تعاملونه','heading')
add('Acid Anhydrides are more reactive than esters but less reactive than acid halides, toward nucleophiles.','ایسڈ این ہائیڈرائیڈز نیوکلیوفائلز کی طرف ایسٹرز سے زیادہ لیکن ایسڈ ہیلائیڈز سے کم تعامل پذیر ہیں۔','اسید انهایدرایډونه د نیوکلیوفایلونو په وړاندې له ایسټرونو ډېر خو له اسید هالایډونو لږ تعامل کوونکي دي.')
add('(i) Hydrolysis','(i) ہائیڈرولائسز','(i) هایدرولایسس','heading')
add('On hydrolysis, anhydrides form corresponding carboxylic acids. The hydrolysis of anhydrides can occurs in the presence of acid or base catalyst, though uncatalyzed hydrolysis can also occurs readily.','ہائیڈرولائسز پر این ہائیڈرائیڈز متعلقہ کاربوکسلک ایسڈز بناتے ہیں۔ این ہائیڈرائیڈز کی ہائیڈرولائسز تیزابی یا اساسی عمل انگیز کی موجودگی میں ہو سکتی ہے، اگرچہ عمل انگیز کے بغیر ہائیڈرولائسز بھی آسانی سے ہو جاتی ہے۔','د هایدرولایسس پر مهال انهایدرایډونه اړوند کاربوکسیلیک اسیدونه جوړوي. د انهایدرایډونو هایدرولایسس د اسیدي یا قلوي کتلست په شتون کې کېدای شي، که څه هم بې کتلسته هایدرولایسس هم په اسانۍ کېږي.')
visual('chem12-p134-anhydride-hydrolysis',anhyd)
record=section('20.7','Amides, reduction, decarboxylation and reactions of acyl halides and anhydrides','امائیڈز، تخفیف، ڈی کاربوکسیلیشن اور ایسائل ہیلائیڈز و این ہائیڈرائیڈز کے تعاملات','امایډونه، ارجاع، ډی کاربوکسیلېشن او د اسایل هالایډونو او انهایدرایډونو تعاملونه',paras,layout,blocks,'262–263')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':134,'printedPages':[262,263]}]
record['sourceContinuesOnPdfPage']=135
issues=[{'id':'chem12-p262-amide-group-printing','printedPage':262,'description':'Text reads "replacing –OH of the acid with –N₂ group" (intended –NH₂); retained as printed.'}]
trim=[{'id':'20.8','startsAt':'20.7.4.3 Reactions of Esters'}]
if __name__=='__main__':save(134,[record],trim=trim,issues=issues,chapter_number=20)
