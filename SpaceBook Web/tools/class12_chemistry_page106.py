"""PDF106 printed204–205: Lucas test, PX₃/SOCl₂, dehydration, Fischer esterification, oxidation of primary alcohols."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,_w
F=Fig('arrow106');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'alcohol':('الکوحل','الکول'),'alkyl chloride':('الکائل کلورائیڈ','الکایل کلوراید'),'alkyl halide':('الکائل ہیلائیڈ','الکایل هالایډ'),'thionyl chloride':('تھائیونائل کلورائیڈ','تیونیل کلوراید'),
   'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'ethene':('ایتھین (دوہرا بند)','ایتین'),'carboxylic acid':('کاربوکسیلک ایسڈ','کاربوکسیلیک اسید'),'ester':('ایسٹر','ایسټر'),'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),
   'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),'methyl acetate':('میتھائل ایسیٹیٹ','میتایل اسیټېټ'),'1° -alcohol':('1° -الکوحل','1° -الکول'),'aldehyde':('الڈیہائیڈ','الدیهاید'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'pyridine':('پیریڈین','پیریډین')}
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
def simple(lang,rows):
 s=F.start(75*len(rows)+10)
 for i,(l,ln,a,b,r,rn) in enumerate(rows):
  y=40+75*i;s+=t(200,y,l,17)+t(200,y+22,'   '.join(lb(lang,x) for x in ln),12)+F.arrow(330,440,y-6,lb(lang,a) if a in N else a,b)+t(580,y,r,17)+t(580,y+22,lb(lang,rn),12)
 return s+'</svg>'
def dehyd(lang):
 s=F.start(140)+t(200,30,'H    OH',15)+line(185,36,185,52)+line(215,36,215,52)+t(200,70,'H—C—C—H',17)+line(185,78,185,94)+line(215,78,215,94)+t(200,110,'H    H',15)+t(200,132,lb(lang,'ethyl alcohol'),12)
 s+=F.arrow(320,440,64,'Conc H₂SO₄','170°C')+t(520,34,'H',15)+t(600,34,'H',15)+line(526,40,544,56)+line(594,40,576,56)+t(560,70,'C = C',17)+line(544,78,526,94)+line(576,78,594,94)+t(520,110,'H',15)+t(600,110,'H',15)+t(560,132,lb(lang,'ethene'),12)+t(680,70,'+ H₂O',17)
 return s+'</svg>'
def ester(lang):
 s=F.start(220)+t(110,80,'R—O—H  +',16)+t(90,104,lb(lang,'alcohol'),12)+carbonyl(250,80,"R′",'OH')+t(250,104,lb(lang,'carboxylic acid'),12)+F.eq(350,440,74)+t(395,60,'H⁺',13)+carbonyl(550,80,"R′",'OR')+t(550,104,lb(lang,'ester'),12)+t(670,80,'+ H₂O',16)
 s+=t(110,180,'CH₃—O—H  +',16)+t(90,204,lb(lang,'methyl alcohol'),12)+carbonyl(260,180,'CH₃','OH')+t(260,204,lb(lang,'acetic acid'),12)+F.eq(350,440,174)+t(395,160,'H⁺',13)+carbonyl(560,180,'CH₃','OCH₃')+t(560,204,lb(lang,'methyl acetate'),12)+t(690,180,'+ H₂O',16)
 return s+'</svg>'
def oxid(lang):
 s=F.start(260)
 for i,(l,n1,n2,n3) in enumerate((('R','1° -alcohol','aldehyde','carboxylic acid'),('CH₃','ethyl alcohol','acetaldehyde','acetic acid'))):
  y=70+125*i;s+=tetra(140,y,'OH',l,'H','H')+t(140,y+60,lb(lang,n1),12)+F.arrow(250,350,y-6,'[O]','−H₂O')+carbonyl(450,y,l,'H')+t(450,y+26,lb(lang,n2),12)+F.arrow(530,620,y-6,'[O]')+carbonyl(710,y,l,'OH')+t(710,y+26,lb(lang,n3),12)
 return s+'</svg>'

add('HBr and HI require no catalyst. The mixture of concentrated hydrochloric acid and anhydrous zinc chloride (conc. HCl + ZnCl₂), is called Lucas Reagnt. Tertiary alcohols are more reactive while primary alcohols are least reactive.','HBr اور HI کو عمل انگیز کی ضرورت نہیں۔ مرتکز ہائیڈروکلورک ایسڈ اور بے آب زنک کلورائیڈ کا آمیزہ (مرتکز HCl + ZnCl₂) لوکاس عامل کہلاتا ہے۔ ثالثی الکوحلز زیادہ جبکہ ابتدائی الکوحلز سب سے کم تعامل پذیر ہیں۔','HBr او HI کتلست ته اړتیا نه لري. د غلیظ هایدروکلوریک اسید او بې اوبو جست کلوراید ګډوله (غلیظ HCl + ZnCl₂) د لوکاس عامل بلل کېږي. درېیمي الکولونه ډېر او لومړني الکولونه تر ټولو لږ تعامل کوونکي دي.')
add('Lucas Test: This test is used to distinguish between primary, secondary and tertiary alcohols. Alcohols react with Lucas reagent to form corresponding chlorides, which are insoluble and form cloudiness in the test tube.','لوکاس ٹیسٹ: یہ ٹیسٹ ابتدائی، ثانوی اور ثالثی الکوحلز میں امتیاز کے لیے استعمال ہوتا ہے۔ الکوحلز لوکاس عامل سے تعامل کر کے متعلقہ کلورائیڈز بناتے ہیں، جو ناحل پذیر ہوتے ہیں اور ٹیسٹ ٹیوب میں دھندلاہٹ پیدا کرتے ہیں۔','د لوکاس ازموینه: دا ازموینه د لومړنیو، دویمیو او درېیمیو الکولونو د توپیر لپاره کارېږي. الکولونه له لوکاس عامل سره تعامل کوي او اړوند کلورایډونه جوړوي، چې نه حلېدونکي دي او په ټیسټ ټیوب کې خړوالی رامنځته کوي.')
visual('chem12-p106-lucas',lambda l:simple(l,[('R – OH  +  HCl',['alcohol'],'ZnCl₂','','R – Cl  +  H₂O','alkyl chloride')]))
add('The time taken, for cloudiness to appear corresponds to the reactivity of alcohol and therefore distinguishes primary, secondary and tertiary alcohols. Tertiary alcohol react with Lucas reagent immediately, a secondary alcohol react after some time, whereas primary and methyl alcohol do not react at room temperature.','دھندلاہٹ ظاہر ہونے میں لگنے والا وقت الکوحل کی تعامل پذیری کے مطابق ہوتا ہے اور اس طرح ابتدائی، ثانوی اور ثالثی الکوحلز میں امتیاز کرتا ہے۔ ثالثی الکوحل لوکاس عامل سے فوراً، ثانوی الکوحل کچھ دیر بعد تعامل کرتا ہے، جبکہ ابتدائی اور میتھائل الکوحل کمرے کے درجہ حرارت پر تعامل نہیں کرتے۔','د خړوالي د څرګندېدو لپاره نیول شوی وخت د الکول د تعامل وړتیا سره سمون لري او په دې توګه لومړني، دویمي او درېیمي الکولونه بېلوي. درېیمی الکول له لوکاس عامل سره سمدستي، دویمی الکول یو څه وروسته تعامل کوي، خو لومړنی او میتایل الکول د کوټې په تودوخه کې تعامل نه کوي.')
add('18.1.7.2 Reaction with Phosphorous trihalides (PX₃) and Thionyl chloride (SOCl₂) to give alkyl halides','18.1.7.2 فاسفورس ٹرائی ہیلائیڈز (PX₃) اور تھائیونائل کلورائیڈ (SOCl₂) سے تعامل کر کے الکائل ہیلائیڈز بنانا','18.1.7.2 له فاسفورس ټرای هالایډونو (PX₃) او تیونیل کلوراید (SOCl₂) سره تعامل او د الکایل هالایډونو جوړول','heading')
add('Alcohols when treated with phosphorous trihalides (PX₃), yield corresponding alkyl halides.','فاسفورس ٹرائی ہیلائیڈز (PX₃) سے عمل کرانے پر الکوحلز متعلقہ الکائل ہیلائیڈز دیتے ہیں۔','الکولونه چې له فاسفورس ټرای هالایډونو (PX₃) سره تعامل وکړي، اړوند الکایل هالایډونه ورکوي.')
visual('chem12-p106-px3',lambda l:simple(l,[('3R – OH  +  PX₃',['alcohol'],'','','3R – X  +  H₃PO₃','alkyl halide')]))
add('Alcohols react with thionyl chloride (SOCl₂) in the presence of pyridine to yield the corresponding alkyl chlorides (Section 17.1.4.2).','الکوحلز پیریڈین کی موجودگی میں تھائیونائل کلورائیڈ (SOCl₂) سے تعامل کر کے متعلقہ الکائل کلورائیڈز دیتے ہیں (حصہ 17.1.4.2)۔','الکولونه د پیریډین په شتون کې له تیونیل کلوراید (SOCl₂) سره تعامل کوي او اړوند الکایل کلورایډونه ورکوي (برخه 17.1.4.2).')
visual('chem12-p106-socl2',lambda l:simple(l,[('R – OH  +  SOCl₂',['alcohol','thionyl chloride'],'pyridine','−HCl','R – Cl  +  SO₂','alkyl halide')]))
add('18.1.7.3 Acid catalysed Dehydration','18.1.7.3 تیزابی عمل انگیز آب ربائی','18.1.7.3 اسیدي کتلستي اوبه ایستنه','heading')
add('Alcohols, when treated with concentrated sulphuric acid at 170°C, undergo dehydration to form alkenes (Section 16.5.5.1).','الکوحلز کو 170°C پر مرتکز سلفیورک ایسڈ سے عمل کرانے پر ان کی آب ربائی ہو کر الکینز (دوہرے بند والے) بنتے ہیں (حصہ 16.5.5.1)۔','الکولونه چې په 170°C کې له غلیظ سلفوریک اسید سره تعامل وکړي، اوبه یې ایستل کېږي او الکینونه جوړوي (برخه 16.5.5.1).')
visual('chem12-p106-dehydration',dehyd)
add('The order of rate of dehydration of different alcohols is; tertiary alcohols > secondary alcohols > primary alcohols.','مختلف الکوحلز کی آب ربائی کی شرح کی ترتیب یہ ہے؛ ثالثی الکوحلز > ثانوی الکوحلز > ابتدائی الکوحلز۔','د بېلابېلو الکولونو د اوبو ایستلو د سرعت ترتیب دا دی؛ درېیمي الکولونه > دویمي الکولونه > لومړني الکولونه.')
add('18.1.7.4 Preparation of Esters','18.1.7.4 ایسٹرز کی تیاری','18.1.7.4 د ایسټرونو جوړول','heading')
add('Alcohols react with carboxylic acids in the presence of concentrated sulphuric acid catalyst to form esters. This method is commonly used for preparation of esters and also called Fischer Esterification. It is a type of condensation reaction.','الکوحلز مرتکز سلفیورک ایسڈ عمل انگیز کی موجودگی میں کاربوکسیلک ایسڈز سے تعامل کر کے ایسٹرز بناتے ہیں۔ یہ طریقہ عام طور پر ایسٹرز کی تیاری کے لیے استعمال ہوتا ہے اور اسے فشر ایسٹریفیکیشن بھی کہتے ہیں۔ یہ تکثیفی تعامل کی ایک قسم ہے۔','الکولونه د غلیظ سلفوریک اسید کتلست په شتون کې له کاربوکسیلیک اسیدونو سره تعامل کوي او ایسټرونه جوړوي. دا طریقه عموماً د ایسټرونو د جوړولو لپاره کارېږي او د فیشر ایسټریفیکېشن په نوم هم یادېږي. دا د تراکم تعامل یو ډول دی.')
visual('chem12-p106-esterification',ester)
add('Fischer esterification is reversible, and the position of equilibrium lies slightly to the side of products when the reactants are simple alcohols and carboxylic acids. When the Fischer esterification is used for preparative purposes, the position of equilibrium can be made more favorable by using either the alcohol or the carboxylic acid in excess, or removing water from the reaction mixture. For steric reasons, the order of alcohol reactivity in the Fischer esterification is; methyl alcohol > primary alcohol > secondary alcohol > tertiary alcohol.',
 'فشر ایسٹریفیکیشن رجعی ہے، اور جب متعاملات سادہ الکوحلز اور کاربوکسیلک ایسڈز ہوں تو توازن کا مقام قدرے پیداواروں کی طرف ہوتا ہے۔ جب فشر ایسٹریفیکیشن تیاری کے مقاصد کے لیے استعمال ہو تو الکوحل یا کاربوکسیلک ایسڈ کی زیادتی استعمال کر کے یا تعاملی آمیزے سے پانی نکال کر توازن کا مقام زیادہ سازگار بنایا جا سکتا ہے۔ فضائی وجوہ سے فشر ایسٹریفیکیشن میں الکوحل کی تعامل پذیری کی ترتیب یہ ہے؛ میتھائل الکوحل > ابتدائی الکوحل > ثانوی الکوحل > ثالثی الکوحل۔',
 'د فیشر ایسټریفیکېشن بېرته ګرځېدونکی دی، او کله چې تعامل کوونکي ساده الکولونه او کاربوکسیلیک اسیدونه وي، د توازن ځای یو څه د محصولاتو خوا ته وي. کله چې د فیشر ایسټریفیکېشن د جوړونې موخو لپاره وکارول شي، د الکول یا کاربوکسیلیک اسید د زیاتې اندازې په کارولو یا له تعاملي ګډولې څخه د اوبو په ایستلو د توازن ځای ډېر مناسب کېدای شي. د فضايي دلیلونو له امله په فیشر ایسټریفیکېشن کې د الکول د تعامل وړتیا ترتیب دا دی؛ میتایل الکول > لومړنی الکول > دویمی الکول > درېیمی الکول.')
add('18.1.7.5 Oxidation','18.1.7.5 تکسید','18.1.7.5 اکسیډېشن','heading')
add('Oxidation of an alcohol yields a carbonyl compound. Whether the resulting carbonyl compound is an aldehyde, a ketone, or a carboxylic acid depends on the alcohol and on the oxidizing agent.','الکوحل کی تکسید سے کاربونل مرکب بنتا ہے۔ حاصل ہونے والا کاربونل مرکب الڈیہائیڈ، کیٹون یا کاربوکسیلک ایسڈ ہو گا، اس کا انحصار الکوحل اور تکسیدی عامل پر ہے۔','د الکول اکسیډېشن کاربونیل مرکب ورکوي. دا چې جوړ شوی کاربونیل مرکب الدیهاید، کیټون یا کاربوکسیلیک اسید وي، په الکول او اکسیډایز کوونکي عامل پورې اړه لري.')
add('Primary alcohols may be oxidized either to an aldehyde or to a carboxylic acid. Vigorous oxidation with solutions of strong oxidizing agents like, acidified chromate (CrO₄²⁻), dichromate (Cr₂O₇²⁻) or permanganate (MnO₄⁻) solution leads to the formation of a carboxylic acid, through aldehyde intermediate.','ابتدائی الکوحلز کی تکسید یا تو الڈیہائیڈ یا کاربوکسیلک ایسڈ تک ہو سکتی ہے۔ تیزابی کرومیٹ (CrO₄²⁻)، ڈائی کرومیٹ (Cr₂O₇²⁻) یا پرمینگنیٹ (MnO₄⁻) جیسے طاقتور تکسیدی عاملوں کے محلولوں سے شدید تکسید الڈیہائیڈ درمیانی کے ذریعے کاربوکسیلک ایسڈ بناتی ہے۔','لومړني الکولونه کېدای شي یا الدیهاید ته یا کاربوکسیلیک اسید ته اکسیډایز شي. د قوي اکسیډایز کوونکو عاملونو لکه اسیدي کرومېټ (CrO₄²⁻)، ډای کرومېټ (Cr₂O₇²⁻) یا پرمنګنېټ (MnO₄⁻) محلولونو سره شدید اکسیډېشن د الدیهاید منځني له لارې کاربوکسیلیک اسید جوړوي.')
visual('chem12-p106-primary-oxidation',oxid)
record=section('18.6','Lucas test, halogenation, dehydration, esterification and oxidation of 1° alcohols','لوکاس ٹیسٹ، ہیلوجینیشن، آب ربائی، ایسٹریفیکیشن اور ابتدائی الکوحلز کی تکسید','د لوکاس ازموینه، هالوجینېشن، اوبه ایستنه، ایسټریفیکېشن او د لومړنیو الکولونو اکسیډېشن',paras,layout,blocks,'204–205')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':106,'printedPages':[204,205]}]
record['sourceContinuesOnPdfPage']=107
issues=[{'id':'chem12-p204-lucas-spelling','printedPage':204,'description':'Printed "Lucas Reagnt" retained.'}]
if __name__=='__main__':save(106,[record],issues=issues,chapter_number=18)
