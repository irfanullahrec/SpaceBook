"""PDF78 printed148–149: nitronium formation, sulphonation, halogenation, Friedel-Crafts alkylation (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow78');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'nitronium ion':('نائٹرونیم آئن','نایټرونیم ایون'),'(Electrophile)':('(الیکٹروفائل)','(الکتروفایل)'),'benzene':('بینزین','بنزین'),'benzenesulphonic acid':('بینزین سلفونک ایسڈ','بنزین سلفونیک اسید'),
   'fuming H₂SO₄':('دھواں دار H₂SO₄','لوګی لرونکی H₂SO₄'),'toluene':('ٹولوئین','تولوین'),'o-methylbenzenesulphonic acid (43%)':('o-میتھائل بینزین سلفونک ایسڈ (43%)','o-میتایل بنزین سلفونیک اسید (43%)'),
   'm-methylbenzenesulphonic acid (4%)':('m-میتھائل بینزین سلفونک ایسڈ (4%)','m-میتایل بنزین سلفونیک اسید (4%)'),'p-methylbenzenesulphonic acid (53%)':('p-میتھائل بینزین سلفونک ایسڈ (53%)','p-میتایل بنزین سلفونیک اسید (53%)'),
   'sulphur trioxide':('سلفر ٹرائی آکسائیڈ','سلفر ټرای اکساید'),'chlorobenzene':('کلورو بینزین','کلوروبنزین'),'o-chlorotoluene (43%)':('o-کلورو ٹولوئین (43%)','o-کلوروتولوین (43%)'),
   'm-chlorotolene(2%)':('m-کلورو ٹولوئین (2%)','m-کلوروتولوین (2%)'),'p-chlorotoluene (55%)':('p-کلورو ٹولوئین (55%)','p-کلوروتولوین (55%)'),'chloronium ion':('کلورونیم آئن','کلورونیم ایون'),
   'methyl':('میتھائل','میتایل'),'chloride':('کلورائیڈ','کلوراید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def ring(cx,cy,r=28,subs=None):return F.ring(cx,cy,r,subs=subs)
def eqn(lang,left,right,labels,h=75):
 s=F.start(h)+t(220,35,left,18)+F.arrow(340,440,29)+t(600,35,right,18)
 for i,l in enumerate(labels):s+=t(560,55+i*16,lb(lang,l),13)
 return s+'</svg>'
def simple(lang,reag,cond_a,cond_b,sub,prod,extra,left_extra=None):
 s=F.start(125)+ring(160,62)+t(160,117,lb(lang,'benzene'),13)+t(250,69,reag,18)
 s+=F.arrow(300,420,62,cond_a,cond_b)+ring(500,62,28,{1:sub})+t(500,117,lb(lang,prod),13)+t(630,69,extra,18)
 return s+'</svg>'
def wrap(v,n=24):
 if len(v)<=n or ' ' not in v:return [v]
 m=len(v)//2;sp=min((i for i,c in enumerate(v) if c==' '),key=lambda i:abs(i-m));return [v[:sp],v[sp+1:]]
def isomers(lang,reag,names,sub):
 s=F.start(210)+ring(70,95,28,{0:'CH₃'})+t(70,150,lb(lang,'toluene'),13)
 s+=line(115,95,215,95,2,'#222','marker-end="url(#arrow78)"')+t(165,85,reag[0],13)
 for i,r in enumerate(reag[1:]):s+=t(165,112+16*i,r,13)
 for k,(v,name) in enumerate(zip((1,2,3),names)):
  x=300+k*200;y0=172 if v==3 else 150
  for j,part in enumerate(wrap(lb(lang,name))):s+=t(x,y0+15*j,part,12)
  s+=ring(x,85,28,{0:'CH₃',v:sub})
  if k<2:s+=t(x+100,90,'+',20)
 return s+'</svg>'
def tidbit(lang):
 s=F.start(110)
 s+=t(90,60,':Cl̈—C̈l:',18)+F.arrow(150,175,54)+t(230,60,'AlCl₃',18)
 s+=F.eq(275,330,55)+t(450,60,'Cl⁺—Cl—Al⁻Cl₃',18)+F.eq(560,615,55)+t(720,60,'Cl⁺  +  AlCl₄⁻',18)
 return s+'</svg>'

visual('chem12-p78-nitronium',lambda l:eqn(l,'HNO₃ + 2H₂SO₄','NO₂⁺ + 2HSO₄⁻ + H₃O⁺',['nitronium ion','(Electrophile)']))
add('16.8.5.2.3 Sulphonation','16.8.5.2.3 سلفونیشن','16.8.5.2.3 سلفونېشن','heading')
add('Benzene reacts with concentrated sulfuric acid at 120°C or fuming sulfuric acid at room temperature, to give benzenesulphonic acid. Fuming sulphuric acid is concentrated sulphuric acid in which sulphur trioxide has been dissolved.',
 'بینزین 120°C پر مرتکز سلفیورک ایسڈ یا کمرے کے درجہ حرارت پر دھواں دار سلفیورک ایسڈ سے تعامل کر کے بینزین سلفونک ایسڈ دیتی ہے۔ دھواں دار سلفیورک ایسڈ وہ مرتکز سلفیورک ایسڈ ہے جس میں سلفر ٹرائی آکسائیڈ حل کی گئی ہو۔',
 'بنزین په 120°C کې له غلیظ سلفوریک اسید یا د کوټې په تودوخه کې له لوګی لرونکي سلفوریک اسید سره تعامل کوي او بنزین سلفونیک اسید ورکوي. لوګی لرونکی سلفوریک اسید هغه غلیظ سلفوریک اسید دی چې پکې سلفر ټرای اکساید حل شوی وي.')
visual('chem12-p78-sulphonation-1',lambda l:simple(l,'+ H₂SO₄','120°C','','SO₃H','benzenesulphonic acid','+ H₂O'))
visual('chem12-p78-sulphonation-2',lambda l:simple(l,'+ SO₃',lb(l,'fuming H₂SO₄'),'25°C','SO₃H','benzenesulphonic acid',''))
add('Sulphonation of toluene also yield a mixture of isomeric o–, m– and p–methylbenzenesuphonic acid, in different percentages. The ortho and para products again predominate, while meta product is obtained in small amount.',
 'ٹولوئین کی سلفونیشن سے بھی ہم ترکیب o–، m– اور p–میتھائل بینزین سلفونک ایسڈ کا آمیزہ مختلف فیصد میں حاصل ہوتا ہے۔ اورتھو اور پیرا پیداواریں پھر غالب ہوتی ہیں، جبکہ میٹا پیداوار کم مقدار میں حاصل ہوتی ہے۔',
 'د تولوین سلفونېشن هم د ایزومري o–، m– او p–میتایل بنزین سلفونیک اسید ګډوله په بېلابېلو سلنو ورکوي. اورتو او پارا محصولات بیا غالب دي، خو میټا محصول په لږه اندازه ترلاسه کېږي.')
visual('chem12-p78-toluene-sulphonation',lambda l:isomers(l,[lb(l,'fuming H₂SO₄')],['o-methylbenzenesulphonic acid (43%)','m-methylbenzenesulphonic acid (4%)','p-methylbenzenesulphonic acid (53%)'],'SO₃H'))
add('The electrophile is sulphur trioxide in this reaction. The electrophile sulphur trioxide attacks on benzene ring and forms the products via arenium ion intermediate.',
 'اس تعامل میں الیکٹروفائل سلفر ٹرائی آکسائیڈ ہے۔ الیکٹروفائل سلفر ٹرائی آکسائیڈ بینزین حلقے پر حملہ کرتا ہے اور ایرینیم آئن درمیانی کے ذریعے پیداواریں بناتا ہے۔',
 'په دې تعامل کې الکتروفایل سلفر ټرای اکساید دی. الکتروفایل سلفر ټرای اکساید د بنزین پر کړۍ برید کوي او د ارینیم ایون د منځني له لارې محصولات جوړوي.')
visual('chem12-p78-so3',lambda l:eqn(l,'2H₂SO₄','SO₃ + HSO₄⁻ + H₃O⁺',['sulphur trioxide','(Electrophile)']))
add('16.8.5.2.4 Halogenation','16.8.5.2.4 ہیلوجینیشن','16.8.5.2.4 هالوجینېشن','heading')
add('Benzene reacts with molecular halogen at room temperature, in the presence of Lewis acid catalyst to form halobenzene. For example reaction of chlorine with benzene in the presence ferric chloride is given below.',
 'بینزین کمرے کے درجہ حرارت پر لیوس ایسڈ عمل انگیز کی موجودگی میں سالماتی ہیلوجن سے تعامل کر کے ہیلو بینزین بناتی ہے۔ مثلاً فیرک کلورائیڈ کی موجودگی میں کلورین کا بینزین سے تعامل نیچے دیا گیا ہے۔',
 'بنزین د کوټې په تودوخه کې د لیوس اسید کتلست په شتون کې له مالیکولي هالوجن سره تعامل کوي او هالوبنزین جوړوي. د بېلګې په توګه د فېریک کلوراید په شتون کې له بنزین سره د کلورین تعامل لاندې ورکړل شوی.')
visual('chem12-p78-chlorination',lambda l:simple(l,'+ Cl₂','FeCl₃','25°C','Cl','chlorobenzene','+ HCl'))
add('Chlorination of toluene in presence of FeCl₃ results in a mixture of isomeric o-, m- and p–chlorotoluenes, in different percentages. The ortho and para products predominate, while meta product is obtained in small amount.',
 'FeCl₃ کی موجودگی میں ٹولوئین کی کلورینیشن سے ہم ترکیب o-، m- اور p–کلورو ٹولوئینز کا آمیزہ مختلف فیصد میں حاصل ہوتا ہے۔ اورتھو اور پیرا پیداواریں غالب ہوتی ہیں، جبکہ میٹا پیداوار کم مقدار میں حاصل ہوتی ہے۔',
 'د FeCl₃ په شتون کې د تولوین کلورینېشن د ایزومري o-، m- او p–کلوروتولوینونو ګډوله په بېلابېلو سلنو ورکوي. اورتو او پارا محصولات غالب دي، خو میټا محصول په لږه اندازه ترلاسه کېږي.')
visual('chem12-p78-chlorotoluenes',lambda l:isomers(l,['Cl₂','FeCl₃','−HCl'],['o-chlorotoluene (43%)','m-chlorotolene(2%)','p-chlorotoluene (55%)'],'Cl'))
add('The electrophile is chloronium ions formed by reaction with ferric chloride and chlorine molecules. The electrophile chloronium ion attacks on benzene ring and form products via arenium ion intermediate.',
 'الیکٹروفائل کلورونیم آئن ہیں جو فیرک کلورائیڈ اور کلورین سالمات کے تعامل سے بنتے ہیں۔ الیکٹروفائل کلورونیم آئن بینزین حلقے پر حملہ کرتا ہے اور ایرینیم آئن درمیانی کے ذریعے پیداواریں بناتا ہے۔',
 'الکتروفایل کلورونیم ایونونه دي چې د فېریک کلوراید او کلورین مالیکولونو له تعامل جوړېږي. الکتروفایل کلورونیم ایون د بنزین پر کړۍ برید کوي او د ارینیم ایون د منځني له لارې محصولات جوړوي.')
visual('chem12-p78-chloronium',lambda l:eqn(l,'Cl₂ + FeCl₃','Cl⁺ + FeCl₄⁻',['chloronium ion','(Electrophile)']))
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Chlorine reacts with AlCl₃ to form a complex, which reacts as if it were Cl⁺.','کلورین AlCl₃ سے تعامل کر کے ایک کمپلیکس بناتی ہے، جو ایسے تعامل کرتا ہے جیسے یہ Cl⁺ ہو۔','کلورین له AlCl₃ سره تعامل کوي او یو کمپلېکس جوړوي، چې داسې تعامل کوي لکه Cl⁺ چې وي.')
visual('chem12-p78-alcl3-tidbit',tidbit)
add('16.8.5.2.5 Friedel-Crafts Alkylation','16.8.5.2.5 فریڈل-کرافٹس الکائلیشن','16.8.5.2.5 فریډل-کرافټس الکایلېشن','heading')
add('Benzene reacts with alkyl halides in the presence of Lewis acid catalyst to form alkyl benzenes. For example, reaction of benzene with methyl chloride in the presence of aluminum chloride yields toluene.',
 'بینزین لیوس ایسڈ عمل انگیز کی موجودگی میں الکائل ہیلائیڈز سے تعامل کر کے الکائل بینزینز بناتی ہے۔ مثلاً ایلومینیم کلورائیڈ کی موجودگی میں بینزین کا میتھائل کلورائیڈ سے تعامل ٹولوئین دیتا ہے۔',
 'بنزین د لیوس اسید کتلست په شتون کې له الکایل هالایډونو سره تعامل کوي او الکایل بنزینونه جوړوي. د بېلګې په توګه د المونیم کلوراید په شتون کې له میتایل کلوراید سره د بنزین تعامل تولوین ورکوي.')
def fc(lang):
 s=F.start(140)+ring(160,62)+t(160,117,lb(lang,'benzene'),13)+t(260,69,'+ CH₃Cl',18)+t(260,93,lb(lang,'methyl'),13)+t(260,109,lb(lang,'chloride'),13)
 s+=F.arrow(320,420,62,'AlCl₃')+ring(500,62,28,{1:'CH₃'})+t(500,117,lb(lang,'toluene'),13)+t(620,69,'+ HCl',18)
 return s+'</svg>'
visual('chem12-p78-friedel-crafts-methyl',fc)
add('Substituting methyl groups into toluene, via Friedel-Craft’s alkylation results in formation of three isomeric xylenes. Mainly the o- and p-xylene are formed.',
 'فریڈل-کرافٹ کی الکائلیشن کے ذریعے ٹولوئین میں میتھائل گروپ داخل کرنے سے تین ہم ترکیب زائلینز بنتی ہیں۔ زیادہ تر o- اور p-زائلین بنتی ہیں۔',
 'د فریډل-کرافټ د الکایلېشن له لارې تولوین ته د میتایل ګروپونو ورننوتل درې ایزومري زایلینونه جوړوي. ډېری o- او p-زایلین جوړېږي.')

record=section('16.25','Sulphonation, halogenation and Friedel-Crafts alkylation','سلفونیشن، ہیلوجینیشن اور فریڈل-کرافٹس الکائلیشن','سلفونېشن، هالوجینېشن او فریډل-کرافټس الکایلېشن',paras,layout,blocks,'148–149')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':78,'printedPages':[148,149]}]
record['sourceContinuesOnPdfPage']=79
issues=[{'id':'chem12-p148-printed-spellings','printedPage':148,'description':'Printed "methylbenzenesuphonic" and "m-chlorotolene" retained; Tidbit Lewis-dot scheme rendered as condensed equilibrium Cl₂ + AlCl₃ ⇌ Cl⁺—Cl—Al⁻Cl₃ ⇌ Cl⁺ + AlCl₄⁻.'}]
carry=[{'from':'16.25','to':'16.26','startsAt':'149\nCH,\nCH,\nCH,\nCH,Cl'}]
if __name__=='__main__':save(78,[record],carry=carry,issues=issues,chapter_number=16)
