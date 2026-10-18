"""PDF105 printed202–203: reduction of aldehydes/ketones/acids/esters, hydride donors, reactivity of alcohols, reaction with HX."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,_w
F=Fig('arrow105');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'higher aldehyde':('بڑا الڈیہائیڈ','لوړ الدیهاید'),'1°- alcohol':('1°- الکوحل','1°- الکول'),'ketone':('کیٹون','کیټون'),'2°- alcohol':('2°- الکوحل','2°- الکول'),'carboxylic acid':('کاربوکسیلک ایسڈ','کاربوکسیلیک اسید'),
   'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'carboxylic ester':('کاربوکسیلک ایسٹر','کاربوکسیلیک ایسټر'),'alcohol':('الکوحل','الکول'),'methyl acetate':('میتھائل ایسیٹیٹ','میتایل اسیټېټ'),
   'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),'sodium borohydride':('سوڈیم بوروہائیڈرائیڈ','سوډیم بوروهایدراید'),'lithium aluminum hydride':('لیتھیم ایلومینیم ہائیڈرائیڈ','لیتیم المونیم هایدراید'),
   'lone pairs':('تنہا جوڑے','یوازینۍ جوړې'),'polar bonds':('قطبی بند','قطبي تړونونه'),'halogen acid':('ہیلوجن تیزاب','هالوجني اسید'),'alkyl halide':('الکائل ہیلائیڈ','الکایل هالایډ')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def lay(x,y,l,r,size=16):
 toks=[l,'—','C','—',r];tot=sum(_w(k) for k in toks);cx=x-tot/2;out='';cc=0
 for k in toks:
  w=_w(k);out+=t(cx+w/2,y,k,size)
  if k=='C':cc=cx+w/2
  cx+=w
 return out,cc
def carbonyl(x,y,l,r):o,c=lay(x,y,l,r);return o+t(c,y-36,'O',14)+line(c-3,y-30,c-3,y-15)+line(c+3,y-30,c+3,y-15)
def tetra(x,y,top,l,r,bot):o,c=lay(x,y,l,r);return o+t(c,y-36,top,14)+line(c,y-30,c,y-15)+line(c,y+7,c,y+22)+t(c,y+38,bot,14)
def rows(lang,items,h=None):
 s=F.start(h or 130*len(items)+10)
 for i,(l,r,extra,ln,pl,pr,prod,pn,extra2) in enumerate(items):
  y=60+130*i;s+=carbonyl(170,y,l,r)+(t(260,y,extra,16) if extra else '')+t(170,y+26,lb(lang,ln),12)+F.arrow(300,440,y-6,'1. LiAlH₄, ether','2. H₂O')
  s+=tetra(560,y,'OH',pl,pr,'H')+t(560,y+60,lb(lang,pn),12)+(t(720,y,extra2,16) if extra2 else '')
 return s+'</svg>'
def hydrides(lang):
 s=F.start(140)
 for x,(m,ion,name,f) in zip((250,600),(('B','Na⁺','sodium borohydride','(NaBH₄)'),('Al','Li⁺','lithium aluminum hydride','(LiAlH₄)'))):
  s+=t(x,30,'H',15)+line(x,36,x,48)+t(x,66,'H — '+m+'⁻ — H',16)+line(x,74,x,86)+t(x,102,'H',15)+t(x+70,30,ion,14)+t(x,122,lb(lang,name),12)+t(x,138,f,12)
 return s+'</svg>'
def polar(lang):
 s=F.start(140)+line(250,80,300,80)+line(285,62,300,80)+line(285,98,300,80)+t(312,86,'C',18)+line(326,80,380,80,3)+t(394,86,'O',18)+t(312,58,'δ⁺',12)+t(394,58,'δ⁻',12)
 s+=t(394,46,'••',14)+t(420,70,':',16)+line(404,90,430,112,3)+t(438,126,'H',16)+t(458,112,'δ⁺',12)
 s+=t(560,50,lb(lang,'lone pairs'),13,'#1565c0')+t(560,120,lb(lang,'polar bonds'),13,'#1565c0')+f'<path d="M520 50 Q470 30 410 40" fill="none" stroke="#1565c0" stroke-dasharray="3 3"/><path d="M520 118 Q440 100 360 90" fill="none" stroke="#1565c0" stroke-dasharray="3 3"/>'
 return s+'</svg>'
def hx(lang):return F.start(80)+t(220,35,'R – OH  +  H–X',17)+t(180,58,lb(lang,'alcohol'),12)+t(270,58,lb(lang,'halogen acid'),12)+F.arrow(330,430,29)+t(560,35,'R–X  +  H₂O',17)+t(540,58,lb(lang,'alkyl halide'),12)+'</svg>'

visual('chem12-p105-carbonyl-reduction',lambda l:rows(l,[('R','H','','higher aldehyde','R','H','','1°- alcohol',''),('R','R','+ H₂','ketone','R','R','','2°- alcohol','')]))
add('18.1.5.6 Reduction of Carboxylic Acids and Esters','18.1.5.6 کاربوکسیلک ایسڈز اور ایسٹرز کی تخفیف','18.1.5.6 د کاربوکسیلیک اسیدونو او ایسټرونو ارجاع','heading')
add('Carboxylic acids are exceedingly difficult to reduce. A very powerful reducing agent such as lithium aluminium hydride is required to convert a carboxylic acid to a primary alcohol. Sodium borohydride is not a potent hydride donor as lithium aluminium hydride and does not reduce carboxylic acids.',
 'کاربوکسیلک ایسڈز کی تخفیف بہت مشکل ہے۔ کاربوکسیلک ایسڈ کو ابتدائی الکوحل میں بدلنے کے لیے لیتھیم ایلومینیم ہائیڈرائیڈ جیسا بہت طاقتور تخفیفی عامل درکار ہے۔ سوڈیم بوروہائیڈرائیڈ لیتھیم ایلومینیم ہائیڈرائیڈ جتنا طاقتور ہائیڈرائیڈ دینے والا نہیں اور کاربوکسیلک ایسڈز کی تخفیف نہیں کرتا۔',
 'د کاربوکسیلیک اسیدونو ارجاع ډېره ستونزمنه ده. د کاربوکسیلیک اسید د لومړني الکول ته د بدلولو لپاره ډېر قوي ارجاع کوونکی عامل لکه لیتیم المونیم هایدراید اړین دی. سوډیم بوروهایدراید د لیتیم المونیم هایدراید په څېر قوي هایدراید ورکوونکی نه دی او کاربوکسیلیک اسیدونه نه ارجاع کوي.')
visual('chem12-p105-acid-reduction',lambda l:rows(l,[('R','OH','','carboxylic acid','R','H','','1°- alcohol',''),('CH₃','OH','','acetic acid','CH₃','H','','ethyl alcohol','')]))
add('Esters can also be reduced by lithium aluminium hydride. Two alcohols are formed from each ester molecule. The acyl group of the ester is cleaved, giving a primary alcohol.','ایسٹرز کی تخفیف بھی لیتھیم ایلومینیم ہائیڈرائیڈ سے کی جا سکتی ہے۔ ہر ایسٹر سالمے سے دو الکوحل بنتے ہیں۔ ایسٹر کا ایسائل گروپ ٹوٹ کر ابتدائی الکوحل دیتا ہے۔','ایسټرونه هم د لیتیم المونیم هایدراید په واسطه ارجاع کېدای شي. له هر ایسټر مالیکول څخه دوه الکولونه جوړېږي. د ایسټر اسایل ګروپ ماتېږي او لومړنی الکول ورکوي.')
visual('chem12-p105-ester-reduction',lambda l:rows(l,[('R',"OR′",'','carboxylic ester','R','H','','1°- alcohol',"+ R′—OH"),('CH₃','OCH₃','','methyl acetate','CH₃','H','','ethyl alcohol','+ CH₃—OH')]))
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Lithium aluminium hydride and sodium borohydride are hydride (H⁻) donors. Lithium aluminium hydride is much stronger reducing agent than sodium borohydride.','لیتھیم ایلومینیم ہائیڈرائیڈ اور سوڈیم بوروہائیڈرائیڈ ہائیڈرائیڈ (H⁻) دینے والے ہیں۔ لیتھیم ایلومینیم ہائیڈرائیڈ سوڈیم بوروہائیڈرائیڈ سے کہیں زیادہ طاقتور تخفیفی عامل ہے۔','لیتیم المونیم هایدراید او سوډیم بوروهایدراید د هایدراید (H⁻) ورکوونکي دي. لیتیم المونیم هایدراید له سوډیم بوروهایدراید ډېر قوي ارجاع کوونکی عامل دی.')
visual('chem12-p105-hydrides',hydrides)
add('18.1.6 Reactivity','18.1.6 تعامل پذیری','18.1.6 تعامل وړتیا','heading')
add('The functional group of the alcohols is the hydroxyl group, which is the reactive site. This group has two reactive covalent bonds, the C–O bond and the O–H bond. The electronegativity of oxygen is substantially greater than that of carbon and hydrogen. Consequently, the covalent bonds of this functional group are polarized so that oxygen is electron rich and both carbon and hydrogen are electrophilic. The oxygen atom of alcohols has two unshared pairs of electrons and hence is an electron rich centre.',
 'الکوحلز کا فعلی گروپ ہائیڈروآکسل گروپ ہے، جو تعامل کا مقام ہے۔ اس گروپ میں دو تعامل پذیر شریک گرفتی بند ہیں، C–O بند اور O–H بند۔ آکسیجن کی برقی منفیت کاربن اور ہائیڈروجن سے کافی زیادہ ہے۔ نتیجتاً اس فعلی گروپ کے شریک گرفتی بند اس طرح قطبی ہوتے ہیں کہ آکسیجن الیکٹرانوں سے بھرپور اور کاربن اور ہائیڈروجن دونوں الیکٹروفائلی ہوتے ہیں۔ الکوحلز کے آکسیجن ایٹم پر الیکٹرانوں کے دو غیر مشترک جوڑے ہوتے ہیں اور اس لیے یہ الیکٹرانوں سے بھرپور مرکز ہے۔',
 'د الکولونو فعال ګروپ هایدروکسیل ګروپ دی، چې د تعامل ځای دی. دا ګروپ دوه تعامل کوونکي کوولانسي تړونونه لري، د C–O تړون او د O–H تړون. د اکسیجن الکترونېګاتیویټي د کاربن او هایدروجن په پرتله ډېره لوړه ده. په پایله کې د دې فعال ګروپ کوولانسي تړونونه داسې قطبي کېږي چې اکسیجن له الکترونونو ډک او کاربن او هایدروجن دواړه الکتروفایلي وي. د الکولونو اکسیجني اټوم د الکترونونو دوه نه شریکې جوړې لري او له همدې امله له الکترونونو ډک مرکز دی.')
visual('chem12-p105-polar-bonds',polar)
add('Alcohols are reactive compounds. They readily react with polar or ionic reagents. Generally, the reactions of alcohol involve the fission of either the O–H bond or the C–O bond. The common reactions of alcohols are substitution, elimination and oxidation reactions.','الکوحلز تعامل پذیر مرکبات ہیں۔ یہ قطبی یا آئنی عاملوں سے آسانی سے تعامل کرتے ہیں۔ عموماً الکوحل کے تعاملات میں یا تو O–H بند یا C–O بند ٹوٹتا ہے۔ الکوحلز کے عام تعاملات تبادلہ، اخراج اور تکسید کے تعاملات ہیں۔','الکولونه تعامل کوونکي مرکبات دي. له قطبي یا ایوني عاملونو سره په اسانۍ تعامل کوي. عموماً د الکول په تعاملونو کې یا د O–H تړون یا د C–O تړون ماتېږي. د الکولونو عام تعاملونه بدلون، ایستنه او اکسیډېشن تعاملونه دي.')
add('18.1.7 Reactions of Alcohols','18.1.7 الکوحلز کے تعاملات','18.1.7 د الکولونو تعاملونه','heading')
add('18.1.7.1 Reaction with Halogen acids (HX) to give Alkyl halides','18.1.7.1 ہیلوجن تیزابوں (HX) سے تعامل کر کے الکائل ہیلائیڈز بنانا','18.1.7.1 له هالوجني اسیدونو (HX) سره تعامل او د الکایل هالایډونو جوړول','heading')
add('Alcohols react with halogen acids to form alkyl halides by replacement of hydroxyl group with halogen atom (Section 17.1.4.1).','الکوحلز ہیلوجن تیزابوں سے تعامل کر کے ہائیڈروآکسل گروپ کو ہیلوجن ایٹم سے بدل کر الکائل ہیلائیڈز بناتے ہیں (حصہ 17.1.4.1)۔','الکولونه له هالوجني اسیدونو سره تعامل کوي او د هایدروکسیل ګروپ په هالوجني اټوم بدلولو سره الکایل هالایډونه جوړوي (برخه 17.1.4.1).')
visual('chem12-p105-hx',hx)
add('Reactivity of halogen acid increases with acid strength. In case hydrogen chloride, anhydrous zinc chloride is used as catalyst while treating alcohol to produce alkyl chlorides.','ہیلوجن تیزاب کی تعامل پذیری تیزاب کی طاقت کے ساتھ بڑھتی ہے۔ ہائیڈروجن کلورائیڈ کی صورت میں الکوحل سے الکائل کلورائیڈز بنانے کے لیے بے آب زنک کلورائیڈ بطور عمل انگیز استعمال ہوتا ہے۔','د هالوجني اسید تعامل وړتیا د اسید له قوت سره زیاتېږي. د هایدروجن کلوراید په حالت کې د الکول څخه د الکایل کلورایډونو د جوړولو پر مهال بې اوبو جست کلوراید د کتلست په توګه کارېږي.')
record=section('18.5','Reduction routes to alcohols, reactivity and reaction with HX','الکوحلز تک تخفیف کے طریقے، تعامل پذیری اور HX سے تعامل','الکولونو ته د ارجاع لارې، تعامل وړتیا او له HX سره تعامل',paras,layout,blocks,'202–203')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':105,'printedPages':[202,203]}]
record['sourceContinuesOnPdfPage']=106
issues=[{'id':'chem12-p202-ketone-h2','printedPage':202,'description':'Ketone reduction with LiAlH₄ is printed with "+ H₂" on the reactant side; retained as printed.'}]
trim=[{'id':'18.6','startsAt':'HBr and HI require no catalyst'}]
if __name__=='__main__':save(105,[record],trim=trim,issues=issues,chapter_number=18)
