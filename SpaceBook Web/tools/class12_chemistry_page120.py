"""PDF120 printed232–233: preparation of aldehydes/ketones — ozonolysis, hydration of alkynes, oxidation of alcohols, Friedel–Crafts acylation."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl,tetra
F=Fig('arrow120');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k);T=lambda *a,**k:tetra(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'trans-but-2-ene':('trans-بیوٹ-2-این','trans-بیوټ-2-ین'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'acetaldehdye':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'2-methylbut-2-ene':('2-میتھائل بیوٹ-2-این','2-میتایل بیوټ-2-ین'),
   'acetone':('ایسیٹون','اسیتون'),'ethyne':('ایتھائن','ایتاین'),'Vinyl alcohol':('وائنائل الکوحل','وینایل الکول'),'propyne':('پروپائن','پروپاین'),'propen-2-ol':('پروپین-2-اول','پروپین-2-ول'),
   '1° -alcohol':('1° -الکوحل','1° -الکول'),'aldehyde':('الڈیہائیڈ','الدیهاید'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'2° -alcohol':('2° -الکوحل','2° -الکول'),'ketone':('کیٹون','کیټون'),
   'isopropyl alcohol':('آئسوپروپائل الکوحل','ایزوپروپیل الکول'),'benzene':('بینزین','بنزین'),'acetyl chloride':('ایسیٹائل کلورائیڈ','اسیټیل کلوراید'),'acetophenone':('ایسیٹو فینون','اسیټوفینون')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def alkene(x,y,a,b,c,d):return t(x-40,y-22,a,14)+line(x-30,y-16,x-14,y-4)+t(x-40,y+30,b,14)+line(x-30,y+22,x-14,y+8)+t(x,y+5,'C=C',16)+line(x+14,y-4,x+30,y-16)+t(x+40,y-22,c,14)+line(x+14,y+8,x+30,y+22)+t(x+44,y+30,d,14)
def ozon(lang):
 s=F.start(265)
 for i,(sub,n,p1,n1,p2,n2) in enumerate(((('CH₃','H','H','CH₃'),'trans-but-2-ene',('CH₃','H'),'acetaldehyde',('CH₃','H'),'acetaldehdye'),(('CH₃','CH₃','H','CH₃'),'2-methylbut-2-ene',('CH₃','CH₃'),'acetone',('CH₃','H'),'acetaldehyde'))):
  y=70+120*i;s+=alkene(110,y,*sub)+t(110,y+52,lb(lang,n),12)+line(180,y,330,y,2,'#222','marker-end="url(#arrow120)"')+t(255,y-10,'1. O₃',12)+t(255,y+16,'2. Zn/H₂O, 100°C',12)
  s+=C(430,y+6,*p1)+t(430,y+30,lb(lang,n1),12)+t(520,y+6,'+',16)+C(610,y+6,*p2)+t(610,y+30,lb(lang,n2),12)+t(720,y+6,'+ ZnO',16)
 return s+'</svg>'
def hydr(lang):
 s=F.start(180)
 s+=t(110,60,'H—C≡C—H + H—OH',15)+t(150,40,'δ+ δ−',11)+t(60,82,lb(lang,'ethyne'),12)+F.arrow(220,330,54,'H₂SO₄, HgSO₄','100°C')+t(400,30,'OH',13)+line(408,36,408,46)+t(400,60,'CH₂ = CH',15)+t(400,82,lb(lang,'Vinyl alcohol'),12)
 s+=F.eq(470,540,54)+C(640,60,'CH₃','H')+t(640,82,lb(lang,'acetaldehyde'),12)
 s+=t(120,150,'CH₃—C≡C—CH₃ + H—OH',15)+t(176,130,'δ+ δ−',11)+t(70,172,lb(lang,'propyne'),12)+F.arrow(240,340,144,'H₂SO₄, HgSO₄','100°C')+t(430,120,'OH',13)+line(438,126,438,136)+t(420,150,'CH₂ = C — CH₃',15)+t(420,172,lb(lang,'propen-2-ol'),12)
 s+=F.eq(500,560,144)+C(660,150,'CH₃','CH₃')+t(660,172,lb(lang,'acetone'),12)
 return s+'</svg>'
def ox(lang,items):
 s=F.start(130*len(items)+10)
 for i,(l,r,bot,n1,pl,pr,n2,cond) in enumerate(items):
  y=60+130*i;s+=T(140,y,'OH',l,r,bot)+t(240,y,'+ [O]',16)+t(140,y+60,lb(lang,n1),12)+F.arrow(300,440,y-6,cond,'−H₂O')+C(580,y,pl,pr)+t(580,y+26,lb(lang,n2),12)
 return s+'</svg>'
def fc(lang):
 s=F.start(140)+F.ring(120,80,28)+t(120,135,lb(lang,'benzene'),12)+t(185,86,'+',16)+C(270,86,'CH₃','Cl')+t(270,110,lb(lang,'acetyl chloride'),12)+F.arrow(360,450,80,'AlCl₃')
 s+=F.ring(530,80,28)+line(554,66,574,56)+t(580,50,'C',15)+line(577,42,577,26)+line(583,42,583,26)+t(580,20,'O',14)+line(590,54,610,62)+t(630,68,'CH₃',14)+t(560,135,lb(lang,'acetophenone'),12)+t(710,86,'+ HCl',16)
 return s+'</svg>'

add('19.4.1 Ozonolysis of Alkenes','19.4.1 الکینز کی اوزونولائسز','19.4.1 د الکینونو اوزونولایسس','heading')
add('Ozone reacts vigorously with alkenes to form an unstable intermediate compound called ozonide. The ozonide is reduced directly to aldehydes and ketones by zinc and water, to produce aldehyde and/or ketones. The reaction is called ozonolysis. Symmetrical alkene produces single product while asymmetric alkene yield a mixture of aldehydes/ketones (Section 16.5.7.7). For example, ozonolysis of symmetric but-2-ene (both cis and trans) gives only acetaldehyde, while asymmetric 2-methylbut-2-ene yields a mixture of acetaldehyde and acetone.',
 'اوزون الکینز (دوہرے بند والے) سے زور دار تعامل کر کے ایک ناپائیدار درمیانی مرکب بناتی ہے جسے اوزونائیڈ کہتے ہیں۔ اوزونائیڈ کی زنک اور پانی سے براہِ راست الڈیہائیڈز اور کیٹونز میں تخفیف ہو جاتی ہے۔ اس تعامل کو اوزونولائسز کہتے ہیں۔ متشاکل الکین ایک ہی پیداوار جبکہ غیر متشاکل الکین الڈیہائیڈز/کیٹونز کا آمیزہ دیتا ہے (حصہ 16.5.7.7)۔ مثلاً متشاکل بیوٹ-2-این (cis اور trans دونوں) کی اوزونولائسز صرف ایسیٹ الڈیہائیڈ دیتی ہے، جبکہ غیر متشاکل 2-میتھائل بیوٹ-2-این ایسیٹ الڈیہائیڈ اور ایسیٹون کا آمیزہ دیتا ہے۔',
 'اوزون له الکینونو سره په زوره تعامل کوي او یو بې ثباته منځنی مرکب جوړوي چې اوزونایډ بلل کېږي. اوزونایډ د جستو او اوبو په واسطه مستقیم الدیهایډونو او کیټونونو ته ارجاع کېږي. دې تعامل ته اوزونولایسس وايي. متناظر الکین یو محصول او نامتناظر الکین د الدیهایډونو/کیټونونو ګډوله ورکوي (برخه 16.5.7.7). د بېلګې په توګه د متناظر بیوټ-2-ین (cis او trans دواړه) اوزونولایسس یوازې اسیټالدیهاید ورکوي، خو نامتناظر 2-میتایل بیوټ-2-ین د اسیټالدیهاید او اسیتون ګډوله ورکوي.')
visual('chem12-p120-ozonolysis',ozon)
add('19.4.2 Hydration of Alkynes','19.4.2 الکائنز کی ہائیڈریشن','19.4.2 د الکاینونو هایدرېشن','heading')
add('Alkynes undergo acid-catalyzed addition of water across the triple bond in the presence of mercuric sulphate and sulfuric acid as a catalyst to produce carbonyl compounds. Acetaldehyde is produced in case of acetylene, while ketones are produced from higher alkynes (Section 16.7.8.4).','الکائنز مرکیورک سلفیٹ اور سلفیورک ایسڈ کی بطور عمل انگیز موجودگی میں تہرے بند پر پانی کا تیزاب سے عمل انگیز اضافہ کر کے کاربونل مرکبات بناتے ہیں۔ ایسیٹیلین کی صورت میں ایسیٹ الڈیہائیڈ بنتا ہے، جبکہ بڑے الکائنز سے کیٹونز بنتے ہیں (حصہ 16.7.8.4)۔','الکاینونه د کتلست په توګه د مرکیوریک سلفېټ او سلفوریک اسید په شتون کې پر درې ګوني تړون د اوبو اسیدي کتلستي اضافه کوي او کاربونیل مرکبات جوړوي. د اسیتیلین په حالت کې اسیټالدیهاید جوړېږي، خو له لوړو الکاینونو کیټونونه جوړېږي (برخه 16.7.8.4).')
visual('chem12-p120-hydration',hydr)
add('19.4.3 Oxidation of Alcohols','19.4.3 الکوحلز کی تکسید','19.4.3 د الکولونو اکسیډېشن','heading')
add('Oxidation of a primary alcohol with strong oxidizing agents like, acidified chromate (CrO₄²⁻), dichromate (Cr₂O₇²⁻) or permanganate (MnO₄⁻) solution leads to the formation of a carboxylic acid as final product, through aldehydes intermediate. However, good yield of aldehydes can be obtained using oxidizing agents such as pyridinium chlorochromate (PCC), a complex of chromium trioxide with pyridine and HCl, without over (excessive) oxidation (Section 18.1.7.5).',
 'تیزابی کرومیٹ (CrO₄²⁻)، ڈائی کرومیٹ (Cr₂O₇²⁻) یا پرمینگنیٹ (MnO₄⁻) محلول جیسے طاقتور تکسیدی عاملوں سے ابتدائی الکوحل کی تکسید الڈیہائیڈ درمیانی کے ذریعے آخری پیداوار کے طور پر کاربوکسیلک ایسڈ دیتی ہے۔ تاہم پیریڈینیم کلوروکرومیٹ (PCC)، جو پیریڈین اور HCl کے ساتھ کرومیم ٹرائی آکسائیڈ کا کمپلیکس ہے، جیسے تکسیدی عاملوں سے زیادہ تکسید کے بغیر الڈیہائیڈز کی اچھی مقدار حاصل کی جا سکتی ہے (حصہ 18.1.7.5)۔',
 'د قوي اکسیډایز کوونکو عاملونو لکه اسیدي کرومېټ (CrO₄²⁻)، ډای کرومېټ (Cr₂O₇²⁻) یا پرمنګنېټ (MnO₄⁻) محلول په واسطه د لومړني الکول اکسیډېشن د الدیهاید منځني له لارې د وروستي محصول په توګه کاربوکسیلیک اسید ورکوي. خو د پیریډینیم کلوروکرومېټ (PCC)، چې له پیریډین او HCl سره د کرومیم ټرای اکساید کمپلېکس دی، په څېر اکسیډایز کوونکو عاملونو سره له ډېر اکسیډېشن پرته د الدیهایډونو ښه حاصل ترلاسه کېدای شي (برخه 18.1.7.5).')
visual('chem12-p120-pcc',lambda l:ox(l,[('R','H','H','1° -alcohol','R','H','aldehyde','PCC,CH₂Cl₂'),('CH₃','H','H','ethyl alcohol','CH₃','H','acetaldehyde','PCC,CH₂Cl₂')]))
add('Secondary alcohols are oxidized to ketones by the same reagents that oxidize primary alcohols.','ثانوی الکوحلز کی کیٹونز تک تکسید انہی عاملوں سے ہوتی ہے جو ابتدائی الکوحلز کی تکسید کرتے ہیں۔','دویمي الکولونه د همغو عاملونو په واسطه کیټونونو ته اکسیډایز کېږي چې لومړني الکولونه اکسیډایز کوي.')
visual('chem12-p120-secondary',lambda l:ox(l,[('R','H','R','2° -alcohol','R','R','ketone',''),('CH₃','H','CH₃','isopropyl alcohol','CH₃','CH₃','acetone','')]))
add('19.4.4 Friedel-Crafts Acylation of Aromatics','19.4.4 ارومیٹکس کی فریڈل-کرافٹس ایسائلیشن','19.4.4 د اروماتیکونو فریډل-کرافټس اسایلېشن','heading')
add('Benzene reacts with acid halides (or anhydrides) in the presence of a Lewis acid catalyst to give aromatic ketones. For example, benzene react with acetyl chloride in the presence of aluminum chloride catalyst to form acetophenone (Section 16.8.5.2.6).','بینزین لیوس ایسڈ عمل انگیز کی موجودگی میں ایسڈ ہیلائیڈز (یا این ہائیڈرائیڈز) سے تعامل کر کے ارومیٹک کیٹونز دیتی ہے۔ مثلاً بینزین ایلومینیم کلورائیڈ عمل انگیز کی موجودگی میں ایسیٹائل کلورائیڈ سے تعامل کر کے ایسیٹو فینون بناتی ہے (حصہ 16.8.5.2.6)۔','بنزین د لیوس اسید کتلست په شتون کې له اسید هالایډونو (یا انهایدرایډونو) سره تعامل کوي او اروماتیک کیټونونه ورکوي. د بېلګې په توګه بنزین د المونیم کلوراید کتلست په شتون کې له اسیټیل کلوراید سره تعامل کوي او اسیټوفینون جوړوي (برخه 16.8.5.2.6).')
visual('chem12-p120-acylation',fc)
record=section('19.4','Preparation of aldehydes and ketones','الڈیہائیڈز اور کیٹونز کی تیاری','د الدیهایډونو او کیټونونو چمتو کول',paras,layout,blocks,'232–233')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':120,'printedPages':[232,233]}]
record['sourceContinuesOnPdfPage']=121
issues=[{'id':'chem12-p232-propyne-printing','printedPage':232,'description':'Second hydration example is labelled "propyne" but drawn as CH₃—C≡C—CH₃ (but-2-yne) and gives propen-2-ol/acetone; retained as printed. Label "acetaldehdye" retained.'}]
carry=[{'from':'19.4','to':'19.5','startsAt':'19.5 Reactivity of Carbonyl Group'}]
if __name__=='__main__':save(120,[record],carry=carry,issues=issues,chapter_number=19)
