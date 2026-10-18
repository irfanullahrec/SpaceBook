"""PDF110 printed212–213: preparation of phenols (sulphonate fusion, Dow, cumene, diazonium), reactivity, EAS intro."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow110');t=F.t;line=F.line;ring=F.ring
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'benzene':('بینزین','بنزین'),'benzenesulfonic':('بینزین سلفونک','بنزین سلفونیک'),'acid':('ایسڈ','اسید'),'sodium':('سوڈیم','سوډیم'),'benzenesulfonate':('بینزین سلفونیٹ','بنزین سلفونېټ'),'phenoxide':('فینو آکسائیڈ','فینوکساید'),
   'sodium phenoxide':('سوڈیم فینو آکسائیڈ','سوډیم فینوکساید'),'phenol':('فینول','فینول'),'chlorobenzene':('کلورو بینزین','کلوروبنزین'),'cumene':('کیومین','کیومین'),'cumene hydroperoxide':('کیومین ہائیڈروپرآکسائیڈ','کیومین هایدروپراکساید'),
   'acetone':('ایسیٹون','اسیتون'),'nitrobenzene':('نائٹرو بینزین','نایټروبنزین'),'aniline':('اینیلین','انیلین'),'benzene diazomium chloride':('بینزین ڈائی ایزونیم کلورائیڈ','بنزین ډای ازونیم کلوراید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def lab(x,y,lang,*ws):return ''.join(t(x,y+15*i,lb(lang,w),12) for i,w in enumerate(ws))
def sulph(lang):
 s=F.start(140)+ring(60,70,24)+lab(60,118,lang,'benzene')+F.arrow(95,175,70,'Fuming','H₂SO₄',12)
 s+=ring(230,70,24,subs={0:'SO₃H'})+lab(230,118,lang,'benzenesulfonic','acid')+F.arrow(270,350,70,'NaOH','−H₂O',12)
 s+=ring(410,70,24,subs={0:'SO₃Na'})+lab(410,118,lang,'sodium','benzenesulfonate')+line(450,70,560,70,2,'#222','marker-end="url(#arrow110)"')+t(505,58,'2NaOH',12)+t(505,86,'350°C',12)+t(505,100,'−Na₂SO₃',12)+t(505,114,'−H₂O',12)
 s+=ring(620,70,24,subs={0:'ONa'})+lab(620,118,lang,'sodium','phenoxide')
 return s+'</svg>'
def acidify(lang):return F.start(130)+ring(200,70,24,subs={0:'O⁻Na⁺'})+lab(200,118,lang,'sodium phenoxide')+t(290,76,'+ HCl',16)+F.arrow(340,430,70,'H₂O')+ring(500,70,24,subs={0:'OH'})+lab(500,118,lang,'phenol')+t(610,76,'+ NaCl',16)+'</svg>'
def dow(lang):
 s=F.start(140)+ring(60,75,24)+lab(60,122,lang,'benzene')+F.arrow(95,175,75,'Cl₂/FeCl₃','−HCl',12)+ring(225,75,24,subs={0:'Cl'})+lab(225,122,lang,'chlorobenzene')
 s+=line(265,75,410,75,2,'#222','marker-end="url(#arrow110)"')+t(338,63,'aq. NaOH (10%)',12)+t(338,91,'350°C,150 atm',12)+t(338,105,'−NaCl',12)
 s+=ring(460,75,24,subs={0:'O⁻Na⁺'})+lab(460,122,lang,'sodium phenoxide')+F.arrow(500,600,75,'HCl/H₂O','−NaCl',12)+ring(650,75,24,subs={0:'OH'})+lab(650,122,lang,'phenol')
 return s+'</svg>'
def cumene(lang):
 s=F.start(280)+ring(60,90,24)+lab(60,135,lang,'benzene')+F.arrow(95,225,90,'CH₃—CH=CH₂','H₂SO₄, 250°C',12)
 s+=ring(290,90,24,subs={0:'CH(CH₃)₂'})+lab(290,135,lang,'cumene')+F.arrow(335,420,90,'O₂','−2H₂O',12)
 s+=ring(490,90,24)+line(490,66,490,54)+t(490,46,'CH₃—C—CH₃',14)+line(490,32,490,22)+t(490,16,'OOH',13)+lab(490,135,lang,'cumene hydroperoxide')
 s+=line(560,90,640,90)+line(640,90,640,230)+F.line(640,230,470,230,2,'#222','marker-end="url(#arrow110)"')+t(680,160,'H₂SO₄/H₂O',12)+t(680,176,'70°C',12)
 s+=t(160,200,'O',14)+line(157,206,157,220)+line(163,206,163,220)+t(160,240,'CH₃—C—CH₃  +',15)+lab(150,262,lang,'acetone')+ring(380,232,24,subs={0:'OH'})+lab(380,276,lang,'phenol')
 return s.replace('viewBox="0 0 850 280"','viewBox="0 0 850 290"')+'</svg>'
def diazo(lang):
 s=F.start(290)+ring(80,90,24)+lab(80,135,lang,'benzene')+F.arrow(120,230,90,'HNO₃','H₂SO₄ / −H₂O',12)+ring(290,90,24,subs={0:'NO₂'})+lab(290,135,lang,'nitrobenzene')
 s+=F.arrow(330,440,90,'Sn/HCl','−2H₂O',12)+ring(500,90,24,subs={0:'NH₂'})+lab(500,135,lang,'aniline')
 s+=line(545,90,640,90)+line(640,90,640,230)+F.line(640,230,570,230,2,'#222','marker-end="url(#arrow110)"')+t(700,150,'NaNO₂/HCl',12)+t(700,166,'0°C',12)+t(700,182,'−NaCl / −H₂O',12)
 s+=ring(500,235,24,subs={0:'N₂⁺Cl⁻'})+lab(500,280,lang,'benzene diazomium chloride')+F.line(455,235,330,235,2,'#222','marker-end="url(#arrow110)"')+t(392,223,'H₂O, 100°C',12)+t(392,251,'−HCl / −N₂',12)
 s+=ring(270,235,24,subs={0:'OH'})+lab(270,280,lang,'phenol')
 return s.replace('viewBox="0 0 850 290"','viewBox="0 0 850 295"')+'</svg>'

visual('chem12-p110-sulphonate-fusion',sulph)
add('The resultant sodium phenoxide is then treated with dilute HCl to form phenol.','حاصل ہونے والے سوڈیم فینو آکسائیڈ کو پھر ہلکے HCl سے عمل کرا کر فینول بنایا جاتا ہے۔','ترلاسه شوی سوډیم فینوکساید بیا له رقیق HCl سره تعامل ورکول کېږي څو فینول جوړ شي.')
visual('chem12-p110-acidify',acidify)
add('The process can also be used in laboratory, but due to vigorous conditions required for this process, limits its applications.','یہ عمل تجربہ گاہ میں بھی استعمال ہو سکتا ہے، لیکن اس کے لیے درکار سخت شرائط اس کے استعمال کو محدود کرتی ہیں۔','دا بهیر په لابراتوار کې هم کارېدای شي، خو د دې بهیر لپاره اړین سخت شرایط یې کارونه محدودوي.')
add('18.2.5.2 From Chlorobenzene (Dow Process)','18.2.5.2 کلورو بینزین سے (ڈاؤ عمل)','18.2.5.2 له کلوروبنزین څخه (ډاو بهیر)','heading')
add('In this method, chlorobenzene is hydrolysed with aqueous sodium hydroxide at high temperature and pressure. This process was developed by Dow Chemical Company of USA in 1928. The resultant sodium phenoxide is then treated with dilute HCl to form phenol.','اس طریقے میں کلورو بینزین کی زیادہ درجہ حرارت اور دباؤ پر آبی سوڈیم ہائیڈروآکسائیڈ سے ہائیڈرولائسز کی جاتی ہے۔ یہ عمل امریکہ کی ڈاؤ کیمیکل کمپنی نے 1928 میں تیار کیا۔ حاصل ہونے والے سوڈیم فینو آکسائیڈ کو پھر ہلکے HCl سے عمل کرا کر فینول بنایا جاتا ہے۔','په دې طریقه کې کلوروبنزین په لوړه تودوخه او فشار کې له اوبلن سوډیم هایدروکساید سره هایدرولیز کېږي. دا بهیر د امریکا د ډاو کیمیکل شرکت له خوا په 1928 کې جوړ شو. ترلاسه شوی سوډیم فینوکساید بیا له رقیق HCl سره تعامل ورکول کېږي څو فینول جوړ شي.')
visual('chem12-p110-dow',dow)
add('18.2.5.3 From Acidic oxidation of Cumene','18.2.5.3 کیومین کی تیزابی تکسید سے','18.2.5.3 د کیومین له اسیدي اکسیډېشن څخه','heading')
add('This method involves air oxidation of cumene (isopropyl benzene) to cumene hydroperoxide, which on treatment with dilute hydrochloric acid forms phenol along with acetone. The cumene is prepared by alkylation of benzene (Section 16.8.5.2.5).','اس طریقے میں کیومین (آئسوپروپائل بینزین) کی ہوا سے تکسید کر کے کیومین ہائیڈروپرآکسائیڈ بنایا جاتا ہے، جو ہلکے ہائیڈروکلورک ایسڈ سے عمل پر ایسیٹون کے ساتھ فینول بناتا ہے۔ کیومین بینزین کی الکائلیشن سے تیار کیا جاتا ہے (حصہ 16.8.5.2.5)۔','په دې طریقه کې د کیومین (ایزوپروپیل بنزین) هوایي اکسیډېشن کیومین هایدروپراکساید ته کېږي، چې له رقیق هایدروکلوریک اسید سره د تعامل پر مهال له اسیتون سره فینول جوړوي. کیومین د بنزین د الکایلېشن په واسطه جوړېږي (برخه 16.8.5.2.5).')
visual('chem12-p110-cumene',cumene)
add('18.2.5.4 Hydrolysis of Diazonium Salts','18.2.5.4 ڈائی ایزونیم نمکیات کی ہائیڈرولائسز','18.2.5.4 د ډای ازونیم مالګو هایدرولیز','heading')
add('This is a simple laboratory method in which a solution of benzenediazonium chloride is warmed on a water bath at 100°C. Benzenediazonium chloride is prepared by diazotization of aniline (Section 17.6.7.5).','یہ ایک سادہ تجربہ گاہی طریقہ ہے جس میں بینزین ڈائی ایزونیم کلورائیڈ کے محلول کو 100°C پر پانی کے حمام پر گرم کیا جاتا ہے۔ بینزین ڈائی ایزونیم کلورائیڈ اینیلین کی ڈائی ایزوٹائزیشن سے تیار کیا جاتا ہے (حصہ 17.6.7.5)۔','دا یوه ساده لابراتواري طریقه ده چې پکې د بنزین ډای ازونیم کلوراید محلول په 100°C کې د اوبو پر حمام تودېږي. بنزین ډای ازونیم کلوراید د انیلین د ډای ازوټایزېشن په واسطه جوړېږي (برخه 17.6.7.5).')
visual('chem12-p110-diazonium',diazo)
add('18.2.6 Reactivity of Phenol','18.2.6 فینول کی تعامل پذیری','18.2.6 د فینول تعامل وړتیا','heading')
add('Generally phenols exhibit two types of reactions i.e. reactions of hydroxyl group and reactions of aromatic ring.','عموماً فینولز دو قسم کے تعاملات ظاہر کرتے ہیں، یعنی ہائیڈروآکسل گروپ کے تعاملات اور ارومیٹک حلقے کے تعاملات۔','عموماً فینولونه دوه ډوله تعاملونه ښيي، یعنې د هایدروکسیل ګروپ تعاملونه او د اروماتیکې کړۍ تعاملونه.')
add('In the first type of reactions, usually involve the breaking of O–H bond in formation of salts, ethers, esters etc. In these reactions phenol somewhat resemble to alcohols. In the second type of reactions, the benzene ring of phenol undergoes electrophilic substitution reactions which are characteristic of most of the aromatic compounds e.g. nitration, sulphonation, halogenation, Friedel–Crafts alkylation and acylation etc.',
 'پہلی قسم کے تعاملات میں عموماً نمکیات، ایتھرز، ایسٹرز وغیرہ بنتے وقت O–H بند ٹوٹتا ہے۔ ان تعاملات میں فینول کچھ حد تک الکوحلز سے مشابہ ہے۔ دوسری قسم کے تعاملات میں فینول کا بینزین حلقہ الیکٹروفائلی تبادلے کے تعاملات کرتا ہے جو زیادہ تر ارومیٹک مرکبات کی خصوصیت ہیں، مثلاً نائٹریشن، سلفونیشن، ہیلوجینیشن، فریڈل–کرافٹس الکائلیشن اور ایسائلیشن وغیرہ۔',
 'په لومړي ډول تعاملونو کې معمولاً د مالګو، ایترونو، ایسټرونو او نورو د جوړېدو پر مهال د O–H تړون ماتېږي. په دې تعاملونو کې فینول یو څه الکولونو ته ورته دی. په دویم ډول تعاملونو کې د فینول بنزیني کړۍ الکتروفایلي بدلون تعاملونه کوي چې د ډېرو اروماتیکو مرکباتو ځانګړنه ده، لکه نایټرېشن، سلفونېشن، هالوجینېشن، فریډل–کرافټس الکایلېشن او اسایلېشن او نور.')
add('The presence of hydroxyl group on the benzene ring in phenol increases electron density of the ring at ortho and para positions by giving its electron pair to the ring and hence increases the reactivity of the ring relative to benzene itself, for electrophillic substitution reactions (Section 16.8.5.2.7).',
 'فینول میں بینزین حلقے پر ہائیڈروآکسل گروپ کی موجودگی حلقے کو اپنا الیکٹرانی جوڑا دے کر اورتھو اور پیرا مقامات پر حلقے کی الیکٹرانی کثافت بڑھا دیتی ہے اور اس طرح الیکٹروفائلی تبادلے کے تعاملات کے لیے خود بینزین کے مقابلے میں حلقے کی تعامل پذیری بڑھاتی ہے (حصہ 16.8.5.2.7)۔',
 'په فینول کې پر بنزیني کړۍ د هایدروکسیل ګروپ شتون کړۍ ته د خپلې الکتروني جوړې په ورکولو سره په اورتو او پارا موقعیتونو کې د کړۍ الکتروني کثافت زیاتوي او په دې توګه د الکتروفایلي بدلون تعاملونو لپاره د پخپله بنزین په پرتله د کړۍ تعامل وړتیا زیاتوي (برخه 16.8.5.2.7).')
add('18.2.7 Reactions of Phenols','18.2.7 فینولز کے تعاملات','18.2.7 د فینولونو تعاملونه','heading')
add('18.2.7.1 Electrophilic Aromatic Substitutions','18.2.7.1 الیکٹروفائلی ارومیٹک تبادلے','18.2.7.1 الکتروفایلي اروماتیک بدلونونه','heading')
add('In these reactions an electrophile is introduced into the aromatic ring and the hydroxyl group remains intact. Some electrophilic substitution reactions are given below.','ان تعاملات میں الیکٹروفائل ارومیٹک حلقے میں داخل ہوتا ہے اور ہائیڈروآکسل گروپ برقرار رہتا ہے۔ چند الیکٹروفائلی تبادلے کے تعاملات درج ذیل ہیں۔','په دې تعاملونو کې الکتروفایل اروماتیکې کړۍ ته ورننوځي او هایدروکسیل ګروپ پر خپل ځای پاتې کېږي. ځینې الکتروفایلي بدلون تعاملونه لاندې ورکړل شوي.')
add('1. Nitration','1. نائٹریشن','1. نایټرېشن','heading')
add('Phenol reacts with dilute nitric acid to form, mainly o– and p–nitrophenol (Section 16.8.5.2.7).','فینول ہلکے نائٹرک ایسڈ سے تعامل کر کے زیادہ تر o– اور p–نائٹرو فینول بناتا ہے (حصہ 16.8.5.2.7)۔','فینول له رقیق نایټریک اسید سره تعامل کوي او ډېری o– او p–نایټروفینول جوړوي (برخه 16.8.5.2.7).')
record=section('18.10','Preparation of phenols, reactivity and electrophilic substitution','فینولز کی تیاری، تعامل پذیری اور الیکٹروفائلی تبادلہ','د فینولونو چمتو کول، تعامل وړتیا او الکتروفایلي بدلون',paras,layout,blocks,'212–213')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':110,'printedPages':[212,213]}]
record['sourceContinuesOnPdfPage']=111
issues=[{'id':'chem12-p212-printing','printedPage':212,'description':'Printed "diazomium", "electrophillic" and "(Section 17.6.7.5)" (Unit 17 section is 17.3.7.5) retained; NaOH step to sodium benzenesulfonate shown as printed.'}]
trim=[{'id':'18.11','startsAt':'H2O, 100°C'},{'id':'18.12','startsAt':'213\nNOT FOR SALE'}]
if __name__=='__main__':save(110,[record],trim=trim,issues=issues,chapter_number=18)
