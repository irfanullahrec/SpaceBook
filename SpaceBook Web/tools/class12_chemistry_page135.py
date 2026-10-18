"""PDF135 printed264–265: reactions of esters, amides and nitriles; 20.7.5 summary introduction."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl
F=Fig('arrow135');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'ester':('ایسٹر','ایسټر'),'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'alcohol':('الکوحل','الکول'),'sodium carboxylate':('سوڈیم کاربوکسیلیٹ','سوډیم کاربوکسیلېټ'),'amide':('امائیڈ','امایډ'),'heat':('حرارت','تودوخه'),
   'primary amide':('ابتدائی امائیڈ','لومړنی امایډ'),'primary amine':('ابتدائی امائن','لومړنی امین'),'grignard reagent':('گرینیارڈ عامل','ګرینیارډ عامل'),'nitrile':('نائٹرائل','نایټرایل'),'imine salt':('امائن نمک','ایمین مالګه'),
   'ketone':('کیٹون','کیټون'),'(workup)':('(ورک اپ)','(ورک اپ)'),'methanenitrile':('میتھین نائٹرائل','میتان نایټرایل'),'acetone':('ایسیٹون','اسیتون'),'1. LiAlH₄/ether':('1. LiAlH₄/ایتھر','1. LiAlH₄/ایتر')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def esterhyd(lang):
 s=F.start(210)
 s+=C(110,60,"R′",'OR')+t(110,84,lb(lang,'ester'),12)+t(250,60,'+  H—OH',16)+F.eq(300,400,54)+t(350,42,'H⁺',12)+C(500,60,"R′",'OH')+t(500,84,lb(lang,'carboxylic acid'),12)+t(660,60,'+  R—OH',16)+t(680,84,lb(lang,'alcohol'),12)
 s+=C(110,170,"R′",'OR')+t(110,194,lb(lang,'ester'),12)+t(250,170,'+  NaOH',16)+F.arrow(300,400,164,'H₂O')+C(500,170,"R′",'O⁻Na⁺')+t(500,194,lb(lang,'sodium carboxylate'),12)+t(680,170,'+  R—OH',16)+t(700,194,lb(lang,'alcohol'),12)
 return s+'</svg>'
def amidehyd(lang):
 s=F.start(100)+C(110,55,'R','NH₂')+t(110,79,lb(lang,'amide'),12)+t(250,55,'+  H—OH',16)+F.arrow(310,430,49,'H⁺ or ⁻OH',lb(lang,'heat'))+C(530,55,'R','OH')+t(530,79,lb(lang,'carboxylic acid'),12)+t(680,55,'+  NH₃',16)
 return s+'</svg>'
def amidered(lang):
 s=F.start(100)+C(230,55,'R','NH₂')+t(230,79,lb(lang,'primary amide'),12)+F.arrow(330,460,49,lb(lang,'1. LiAlH₄/ether'),'2. H₂O')+t(580,55,'R—CH₂—NH₂',16)+t(580,79,lb(lang,'primary amine'),12)
 return s+'</svg>'
def grig(lang):
 s=F.start(210)+t(90,70,'R—MgX  +',16)+t(90,94,lb(lang,'grignard reagent'),12)+t(220,70,"R′—C≡N",16)+t(220,94,lb(lang,'nitrile'),12)+f'<path d="M80 50 Q160 10 230 52" fill="none" stroke="#222" marker-end="url(#arrow135)"/>'+F.arrow(280,360,64)
 s+=t(440,30,'N⁻MgX⁺',14)+line(437,38,437,54)+line(443,38,443,54)+t(440,70,"R—C—R′",16)+t(440,94,lb(lang,'imine salt'),12)+F.arrow(510,610,64,'H₃O⁺',lb(lang,'(workup)'))+C(700,70,'R',"R′")+t(700,94,lb(lang,'ketone'),12)
 s+=t(250,180,'CH₃—C≡N',16)+t(250,204,lb(lang,'methanenitrile'),12)+F.arrow(330,460,174,'1. CH₃MgBr','2. H₃O⁺')+C(560,180,'CH₃','CH₃')+t(560,204,lb(lang,'acetone'),12)
 return s.replace('viewBox="0 0 850 210"','viewBox="0 0 850 215"')+'</svg>'

add('20.7.4.3 Reactions of Esters','20.7.4.3 ایسٹرز کے تعاملات','20.7.4.3 د ایسټرونو تعاملونه','heading')
add('Following are some of the important reactions of esters.','ایسٹرز کے چند اہم تعاملات درج ذیل ہیں۔','لاندې د ایسټرونو ځینې مهم تعاملونه دي.')
add('(i) Hydrolysis','(i) ہائیڈرولائسز','(i) هایدرولایسس','heading')
add('Esters are commonly hydrolyzed to carboxylic acid and alcohol, on heating with water very slowly. However the hydrolysis of ester can be catalyzed by an acid or base.','ایسٹرز عموماً پانی کے ساتھ گرم کرنے پر بہت آہستہ کاربوکسلک ایسڈ اور الکوحل میں ہائیڈرولائز ہوتے ہیں۔ تاہم ایسٹر کی ہائیڈرولائسز تیزاب یا اساس سے عمل انگیز کی جا سکتی ہے۔','ایسټرونه معمولاً له اوبو سره د تودولو پر مهال ډېر ورو کاربوکسیلیک اسید او الکول ته هایدرولایز کېږي. خو د ایسټر هایدرولایسس د اسید یا قلوي په واسطه کتلست کېدای شي.')
add('The acid-catalyzed hydrolysis is reversible, and is the reverse of acid-catalyzed esterification (Section 18.1.7.4 and 20.7.1.3).','تیزاب سے عمل انگیز ہائیڈرولائسز معکوس ہے، اور تیزاب سے عمل انگیز ایسٹریفکیشن کا الٹ ہے (حصے 18.1.7.4 اور 20.7.1.3)۔','اسیدي کتلستي هایدرولایسس بېرته ګرځېدونکی دی او د اسیدي کتلستي ایسټریفیکېشن برعکس دی (برخې 18.1.7.4 او 20.7.1.3).')
add('The alkaline hydrolysis will yield a salt of carboxylic acid and alcohol. This reaction is also called saponification reaction, because such type of reaction is used for preparation of soap from fats.','اساسی ہائیڈرولائسز سے کاربوکسلک ایسڈ کا نمک اور الکوحل حاصل ہوں گے۔ اس تعامل کو سیپونیفکیشن تعامل بھی کہتے ہیں، کیونکہ اس قسم کا تعامل چکنائیوں سے صابن کی تیاری کے لیے استعمال ہوتا ہے۔','قلوي هایدرولایسس د کاربوکسیلیک اسید مالګه او الکول ورکوي. دې تعامل ته د صابون جوړونې تعامل هم وايي، ځکه دا ډول تعامل له غوړیو څخه د صابون د جوړولو لپاره کارېږي.')
visual('chem12-p135-ester-hydrolysis',esterhyd)
add('(ii) Reduction of Esters','(ii) ایسٹرز کی تخفیف','(ii) د ایسټرونو ارجاع','heading')
add('Ester can be reduced to alcohols in the presence of strong reducing agent such as lithium aluminum hydride in ether (Section 18.1.5.6).','ایسٹر کی ایتھر میں لیتھیم ایلومینیم ہائیڈرائیڈ جیسے طاقتور تخفیفی عامل کی موجودگی میں الکوحلز تک تخفیف کی جا سکتی ہے (حصہ 18.1.5.6)۔','ایسټر په ایتر کې د لیتیم المونیم هایدراید په څېر د قوي ارجاع کوونکي عامل په شتون کې الکولونو ته ارجاع کېدای شي (برخه 18.1.5.6).')
add('(iii) Reaction of Ester with Grignard Reagent','(iii) گرینیارڈ عامل کے ساتھ ایسٹر کا تعامل','(iii) له ګرینیارډ عامل سره د ایسټر تعامل','heading')
add('Esters react with two equivalents of Grignard reagent to give an alcohol (Section 17.2.3.2).','ایسٹرز گرینیارڈ عامل کے دو مساویوں سے تعامل کر کے الکوحل دیتے ہیں (حصہ 17.2.3.2)۔','ایسټرونه د ګرینیارډ عامل له دوو معادلو سره تعامل کوي او الکول ورکوي (برخه 17.2.3.2).')
add('20.7.4.4 Reactions of Amides','20.7.4.4 امائیڈز کے تعاملات','20.7.4.4 د امایډونو تعاملونه','heading')
add('Amides are the least reactive of the common carboxylic acid derivatives. Like other acid derivatives, amides can also reacts with nucleophiles like water.','امائیڈز عام کاربوکسلک ایسڈ مشتقات میں سب سے کم تعامل پذیر ہیں۔ دوسرے ایسڈ مشتقات کی طرح امائیڈز بھی پانی جیسے نیوکلیوفائلز سے تعامل کر سکتے ہیں۔','امایډونه د عامو کاربوکسیلیک اسید مشتقاتو په منځ کې تر ټولو لږ تعامل کوونکي دي. د نورو اسید مشتقاتو په څېر، امایډونه هم د اوبو په څېر نیوکلیوفایلونو سره تعامل کولی شي.')
add('(i) Hydrolysis','(i) ہائیڈرولائسز','(i) هایدرولایسس','heading')
add('Amides on hydrolysis form the corresponding carboxylic acids and ammonia. The reaction is very slow and requires the use of strong acid or base as catalyst. Both are irreversible and in case of base catalyst, salt of carboxylic acid is obtained.','امائیڈز ہائیڈرولائسز پر متعلقہ کاربوکسلک ایسڈز اور امونیا بناتے ہیں۔ یہ تعامل بہت آہستہ ہے اور اس کے لیے طاقتور تیزاب یا اساس بطور عمل انگیز درکار ہے۔ دونوں غیر معکوس ہیں اور اساسی عمل انگیز کی صورت میں کاربوکسلک ایسڈ کا نمک حاصل ہوتا ہے۔','امایډونه د هایدرولایسس پر مهال اړوند کاربوکسیلیک اسیدونه او امونیا جوړوي. دا تعامل ډېر ورو دی او د کتلست په توګه قوي اسید یا قلوي ته اړتیا لري. دواړه بېرته نه ګرځېدونکي دي او د قلوي کتلست په حالت کې د کاربوکسیلیک اسید مالګه ترلاسه کېږي.')
visual('chem12-p135-amide-hydrolysis',amidehyd)
add('(ii) Reduction','(ii) تخفیف','(ii) ارجاع','heading')
add('Amides can be reduced to primary amines in presence of lithium aluminium hydride (Section 17.3.5.2.3).','لیتھیم ایلومینیم ہائیڈرائیڈ کی موجودگی میں امائیڈز کی ابتدائی امائنز تک تخفیف کی جا سکتی ہے (حصہ 17.3.5.2.3)۔','امایډونه د لیتیم المونیم هایدراید په شتون کې لومړنیو امینونو ته ارجاع کېدای شي (برخه 17.3.5.2.3).')
visual('chem12-p135-amide-reduction',amidered)
add('20.7.4.5 Reactions of Nitriles','20.7.4.5 نائٹرائلز کے تعاملات','20.7.4.5 د نایټرایلونو تعاملونه','heading')
add('Alkyl nitriles or simply nitriles are also considered as derivatives of carboxylic acids. The following are some of the important reactions of nitriles.','الکائل نائٹرائلز یا صرف نائٹرائلز کو بھی کاربوکسلک ایسڈز کے مشتقات سمجھا جاتا ہے۔ نائٹرائلز کے چند اہم تعاملات درج ذیل ہیں۔','الکایل نایټرایلونه یا یوازې نایټرایلونه هم د کاربوکسیلیک اسیدونو مشتقات ګڼل کېږي. لاندې د نایټرایلونو ځینې مهم تعاملونه دي.')
add('(i) Hydrolysis','(i) ہائیڈرولائسز','(i) هایدرولایسس','heading')
add('Hydrolysis of nitriles with aqueous acid or base yields a carboxylic acid. In the presence of base catalyst, the final product is actually salt of carboxylic acid (Section 20.5.2).','آبی تیزاب یا اساس سے نائٹرائلز کی ہائیڈرولائسز کاربوکسلک ایسڈ دیتی ہے۔ اساسی عمل انگیز کی موجودگی میں آخری پیداوار دراصل کاربوکسلک ایسڈ کا نمک ہوتی ہے (حصہ 20.5.2)۔','د اوبلن اسید یا قلوي په واسطه د نایټرایلونو هایدرولایسس کاربوکسیلیک اسید ورکوي. د قلوي کتلست په شتون کې وروستی محصول په حقیقت کې د کاربوکسیلیک اسید مالګه وي (برخه 20.5.2).')
add('(ii) Reduction','(ii) تخفیف','(ii) ارجاع','heading')
add('Nitriles yield primary amines when reduced with catalytic method, or using lithium aluminium hydride in ether (Section 17.3.5.2.1).','نائٹرائلز کی عمل انگیز طریقے سے یا ایتھر میں لیتھیم ایلومینیم ہائیڈرائیڈ سے تخفیف کرنے پر ابتدائی امائنز حاصل ہوتے ہیں (حصہ 17.3.5.2.1)۔','نایټرایلونه د کتلستي طریقې یا په ایتر کې د لیتیم المونیم هایدراید په واسطه د ارجاع پر مهال لومړني امینونه ورکوي (برخه 17.3.5.2.1).')
add('(iii) Reaction with Grignard Reagent','(iii) گرینیارڈ عامل کے ساتھ تعامل','(iii) له ګرینیارډ عامل سره تعامل','heading')
add('Nitriles on reaction with Grignard reagent produce ketones. The strongly nucleophilic Grignard reagent add to carbon-nitrogen triple bond in a similar fashion to that seen in aldehydes and ketones. The reaction proceeds via an imine salt intermediate, which is further hydrolysed to give ketones.','نائٹرائلز گرینیارڈ عامل سے تعامل پر کیٹونز بناتے ہیں۔ طاقتور نیوکلیوفائلی گرینیارڈ عامل کاربن–نائٹروجن تہرے بند پر اسی طرح اضافہ کرتا ہے جیسا کہ الڈیہائیڈز اور کیٹونز میں دیکھا گیا۔ تعامل امائن نمک درمیانی کے ذریعے آگے بڑھتا ہے، جس کی مزید ہائیڈرولائسز سے کیٹونز حاصل ہوتے ہیں۔','نایټرایلونه له ګرینیارډ عامل سره په تعامل کیټونونه جوړوي. قوي نیوکلیوفایلي ګرینیارډ عامل د کاربن–نایټروجن پر درې ګوني تړون په همغه ډول اضافه کېږي لکه په الدیهایډونو او کیټونونو کې چې ولیدل شول. تعامل د ایمین مالګې منځني له لارې مخ ته ځي، چې نور هایدرولایز کېږي او کیټونونه ورکوي.')
visual('chem12-p135-nitrile-grignard',grig)
add('20.7.5 Summary of the Reactions that Interconvert Carboxylic Acid Derivatives','20.7.5 کاربوکسلک ایسڈ مشتقات کو باہم تبدیل کرنے والے تعاملات کا خلاصہ','20.7.5 د کاربوکسیلیک اسید مشتقات یو په بل بدلوونکو تعاملونو لنډیز','heading')
add('A summary of the reactions of different derivatives of carboxylic acids with certain nucleophiles, have been listed in Table 20.5.','کاربوکسلک ایسڈز کے مختلف مشتقات کے بعض نیوکلیوفائلز سے تعاملات کا خلاصہ جدول 20.5 میں دیا گیا ہے۔','له ځینو نیوکلیوفایلونو سره د کاربوکسیلیک اسیدونو د بېلابېلو مشتقاتو د تعاملونو لنډیز په جدول 20.5 کې ورکړل شوی.')
add('The different acids derivatives are listed at the left of the chart in order of decreasing reactivities towards nucleophiles. The common nucleophiles are listed across the top. In case of hydrolysis, corresponding acid is obtained, we either start with an acyl …','مختلف ایسڈ مشتقات چارٹ کے بائیں جانب نیوکلیوفائلز کی طرف گھٹتی ہوئی تعامل پذیری کی ترتیب سے درج ہیں۔ عام نیوکلیوفائلز اوپر کی جانب درج ہیں۔ ہائیڈرولائسز کی صورت میں متعلقہ ایسڈ حاصل ہوتا ہے، خواہ ہم ایسائل …','بېلابېل اسید مشتقات د چارټ په کیڼ اړخ کې د نیوکلیوفایلونو په وړاندې د کمېدونکي تعامل وړتیا په ترتیب لیکل شوي. عام نیوکلیوفایلونه په سر کې لیکل شوي. د هایدرولایسس په حالت کې اړوند اسید ترلاسه کېږي، که موږ له اسایل …')
record=section('20.8','Reactions of esters, amides and nitriles','ایسٹرز، امائیڈز اور نائٹرائلز کے تعاملات','د ایسټرونو، امایډونو او نایټرایلونو تعاملونه',paras,layout,blocks,'264–265')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':135,'printedPages':[264,265]}]
record['sourceContinuesOnPdfPage']=136
issues=[{'id':'chem12-p265-methanenitrile-printing','printedPage':265,'description':'CH₃—C≡N is labelled "methanenitrile" (IUPAC: ethanenitrile); retained as printed.'}]
trim=[{'id':'20.9','startsAt':'halides, acid anhydride, ester, amide or nitrile'}]
if __name__=='__main__':save(135,[record],trim=trim,issues=issues,chapter_number=20)
