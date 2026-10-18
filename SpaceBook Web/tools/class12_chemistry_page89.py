"""PDF89 printed170–171: carbocation classes and stability, SN1 mechanism."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow89');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Increasing carbocation stability':('کاربوکیٹائن کی بڑھتی پائیداری','د کاربوکاټیون زیاتېدونکی ثبات'),'methyl':('میتھائل','میتایل'),'cation':('کیٹائن','کاټیون'),'ethyl':('ایتھائل','ایتیل'),
   'isopropyl':('آئسوپروپائل','ایزوپروپیل'),'tert-butyl':('ٹرشری بیوٹائل','ټرشري بیوټیل'),'(primary)':('(ابتدائی)','(لومړنی)'),'(secondary)':('(ثانوی)','(دویمی)'),'(tertiary)':('(ثالثی)','(درېیمی)'),
   'substitution':('تبادلہ','بدلون'),'nucleophilic':('نیوکلیوفائلی','نیوکلیوفایلي'),'unimolecular':('یک سالمی','یو مالیکولي'),'tert-butyl bromide':('ٹرشری بیوٹائل برومائیڈ','ټرشري بیوټیل برومایډ'),
   'slow step':('سست مرحلہ','ورو پړاو'),'carbocation':('کاربوکیٹائن','کاربوکاټیون'),'(trigonal planar)':('(تکونی مستوی)','(درې ګوټی سطحي)'),'Nucleophile':('نیوکلیوفائل','نیوکلیوفایل'),
   'fast':('تیز','چټک'),'OR':('یا','یا'),'tert-butyl alcohol':('ٹرشری بیوٹائل الکوحل','ټرشري بیوټیل الکول')}
def lb(lang,v):return v if lang=='en' or not v else N[v][0 if lang=='ur' else 1]
def cplus(x,y,top,left,right,bot):
 return t(x,y-38,top,15)+line(x,y-32,x,y-16)+t(x-40,y+5,left,15)+line(x-22,y,x-10,y)+t(x,y+5,'C⁺',16)+line(x+10,y,x+22,y)+t(x+40,y+5,right,15)+line(x,y+10,x,y+26)+t(x,y+44,bot,15)
def stability(lang):
 s=F.start(220)+'<polygon points="60,20 720,20 720,10 760,32 720,54 720,44 60,44" fill="white" stroke="#222"/>'+t(400,38,lb(lang,'Increasing carbocation stability'),15)
 for k,(top,left,right,bot,a,b) in enumerate((('H','H','H','H','methyl','cation'),('H','H₃C','H','H','ethyl','cation'),('CH₃','H₃C','H','H','isopropyl','cation'),('CH₃','H₃C','CH₃','CH₃','tert-butyl','cation'))):
  x=110+k*190;s+=cplus(x,115,top,left,right,bot)+t(x,182,lb(lang,a),13)+t(x,198,lb(lang,b),13)+t(x,214,lb(lang,('','(primary)','(secondary)','(tertiary)')[k]),12,'#777')
  if k<3:s+=t(x+95,120,'<',20)
 return s+'</svg>'
def badge(lang):
 s=F.start(110,420)+'<rect x="10" y="10" width="400" height="92" rx="6" fill="white" stroke="#222"/>'
 s+=t(170,40,'S',18)+t(200,48,'N',18)+t(230,40,'1',18)+t(70,80,lb(lang,'substitution'),12)+t(200,98,lb(lang,'nucleophilic'),12)+t(330,80,lb(lang,'unimolecular'),12)
 s+=line(170,46,110,70,1,'#222','stroke-dasharray="2 3"')+line(200,54,200,86,1,'#222','stroke-dasharray="2 3"')+line(230,46,300,70,1,'#222','stroke-dasharray="2 3"')
 return s+'</svg>'
def tert(x,y,right,lab=None):
 return t(x-20,y-34,'H₃C',14)+line(x-8,y-26,x,y-12)+t(x-42,y+5,'H₃C',14)+line(x-24,y,x-10,y,1.5,'#222','stroke-dasharray="2 2"')+t(x,y+5,'C',16)+line(x,y+10,x-6,y+26,3)+t(x-14,y+42,'H₃C',14)+line(x+10,y,x+26,y)+t(x+26+len(right)*5,y+5,right,14)
def step1(lang):
 s=F.start(140)+tert(150,60,'Br')+t(150,125,lb(lang,'tert-butyl bromide'),12)+F.eq(280,400,55)+t(340,40,lb(lang,'slow step'),12)
 s+=t(520,30,'CH₃',14)+line(520,36,520,48)+t(520,64,'C⁺',16)+line(510,70,492,84)+t(480,96,'H₃C',14)+line(530,70,548,84)+t(562,96,'CH₃',14)+t(620,64,'+ Br⁻',16)
 s+=t(520,118,lb(lang,'carbocation'),12)+t(520,134,lb(lang,'(trigonal planar)'),12)
 return s+'</svg>'
def step2(lang):
 s=F.start(300)
 s+=t(110,40,'H₃C',14)+line(118,46,128,58)+t(135,72,'C⁺ — CH₃',15)+t(110,104,'H₃C',14)+line(118,96,128,82)+t(240,72,'+ H₂O',15)
 s+=t(110,140,lb(lang,'carbocation'),12)+t(110,156,lb(lang,'(trigonal planar)'),12)+t(250,140,lb(lang,'Nucleophile'),12)
 s+=F.arrow(300,380,66,lb(lang,'fast'))+t(490,72,'(CH₃)₃C — O⁺H₂',15)+t(610,72,lb(lang,'OR'),13)+t(720,72,'H₂O⁺ — C(CH₃)₃',15)
 s+=line(800,90,800,230)+F.line(800,230,730,230,2,'#222','marker-end="url(#arrow89)"')+t(820,165,'−H⁺',13)
 s+=t(420,236,'(CH₃)₃C — OH',16)+t(525,236,lb(lang,'OR'),13)+t(620,236,'HO — C(CH₃)₃',16)+t(550,270,lb(lang,'tert-butyl alcohol'),13)
 return s+'</svg>'

add('Carbocations are classified as primary, secondary, or tertiary according to the number of carbons (alkyl groups) that are directly attached to the positively charged carbon. Primary alkyl halides produce primary carbocations while secondary and tertiary alkyl halides yield secondary and tertiary carbocations respectively.',
 'کاربوکیٹائنز کی درجہ بندی ابتدائی، ثانوی یا ثالثی کے طور پر مثبت چارج والے کاربن سے براہِ راست جڑے کاربنوں (الکائل گروپوں) کی تعداد کے مطابق کی جاتی ہے۔ ابتدائی الکائل ہیلائیڈز ابتدائی کاربوکیٹائنز بناتے ہیں جبکہ ثانوی اور ثالثی الکائل ہیلائیڈز بالترتیب ثانوی اور ثالثی کاربوکیٹائنز دیتے ہیں۔',
 'کاربوکاټیونونه د هغو کاربنونو (الکایل ګروپونو) د شمېر له مخې چې له مثبت چارج لرونکي کاربن سره مستقیم تړلي دي، په لومړني، دویمي یا درېیمي ډلبندي کېږي. لومړني الکایل هالایډونه لومړني کاربوکاټیونونه جوړوي، خو دویمي او درېیمي الکایل هالایډونه په ترتیب سره دویمي او درېیمي کاربوکاټیونونه ورکوي.')
add('Alkyl groups directly attached to the positively charged carbon stabilize a carbocation, through its electron donating effect. Thus tertiary carbocations are more stable than secondary and secondary are more stable than primary ones. This stabilization comes from the stabilization of the positive charge of the carbocation by the electron donating alkyl groups directly attached. (Figure 17.3)',
 'مثبت چارج والے کاربن سے براہِ راست جڑے الکائل گروپ اپنے الیکٹران دینے والے اثر کے ذریعے کاربوکیٹائن کو پائیدار بناتے ہیں۔ اس طرح ثالثی کاربوکیٹائنز ثانوی سے اور ثانوی ابتدائی سے زیادہ پائیدار ہیں۔ یہ پائیداری براہِ راست جڑے الیکٹران دینے والے الکائل گروپوں کے ذریعے کاربوکیٹائن کے مثبت چارج کے استحکام سے آتی ہے۔ (شکل 17.3)',
 'له مثبت چارج لرونکي کاربن سره مستقیم تړلي الکایل ګروپونه د خپل الکترون ورکوونکي اغېز له لارې کاربوکاټیون ثابتوي. نو درېیمي کاربوکاټیونونه له دویمیو او دویمي له لومړنیو ډېر ثابت دي. دا ثبات د مستقیم تړلو الکترون ورکوونکو الکایل ګروپونو په واسطه د کاربوکاټیون د مثبت چارج له ثابتولو راځي. (شکل 17.3)')
visual('chem12-figure17-3',stability)
add('Figure 17.3 Realtive stability order of different types of carbocations.','شکل 17.3 مختلف اقسام کے کاربوکیٹائنز کی اضافی پائیداری کی ترتیب۔','شکل 17.3 د بېلابېلو ډولونو کاربوکاټیونونو د نسبي ثبات ترتیب.')
add('Mechanisms of Nucleophilic Substitution reactions','نیوکلیوفائلی تبادلے کے تعاملات کے طریق کار','د نیوکلیوفایلي بدلون تعاملونو میکانیزمونه','heading')
add('Alkyl halides can undergo nucleophilic substitution by two different types of mechanisms. The type of mechanism depends upon the nature of alkyl halides.','الکائل ہیلائیڈز دو مختلف طریق کار سے نیوکلیوفائلی تبادلہ کر سکتے ہیں۔ طریق کار کی قسم الکائل ہیلائیڈز کی نوعیت پر منحصر ہے۔','الکایل هالایډونه په دوو بېلو میکانیزمونو نیوکلیوفایلي بدلون کولی شي. د میکانیزم ډول د الکایل هالایډونو پر طبیعت پورې اړه لري.')
add('17.1.6.3 SN1 Mechanism','17.1.6.3 SN1 طریق کار','17.1.6.3 د SN1 میکانیزم','heading')
visual('chem12-p89-sn1-badge',badge)
add('SN1 stands for Substitution, Nucleophilic, unimolecular. It is a two-step mechanism. First step is slow (rate determining or rate limiting step) and involves the formation of intermediate carbocation by dissociation of alkyl halide or substrate. The term unimolecular means there is only one molecule involved in transition state of the rate-determing step. The second step is fast and involves the attack of nucleophile on planar carbocation and formation of product. SN1 mechanism is generally followed by tertiary alkyl halides. As it involves the formation of carbocation, it is favored by highly ionizing polar solvents (having O–H, N–H bond). For example the hydrolysis of tert-butyl bromide follow SN1 mechanism as shown below.',
 'SN1 کا مطلب ہے تبادلہ، نیوکلیوفائلی، یک سالمی۔ یہ دو مرحلوں والا طریق کار ہے۔ پہلا مرحلہ سست (شرح متعین کرنے والا یا شرح محدود کرنے والا مرحلہ) ہے اور اس میں الکائل ہیلائیڈ یا سبسٹریٹ کے انحلال سے درمیانی کاربوکیٹائن بنتا ہے۔ اصطلاح یک سالمی کا مطلب ہے کہ شرح متعین کرنے والے مرحلے کی عبوری حالت میں صرف ایک سالمہ شامل ہے۔ دوسرا مرحلہ تیز ہے اور اس میں مستوی کاربوکیٹائن پر نیوکلیوفائل کا حملہ اور پیداوار کی تشکیل ہوتی ہے۔ SN1 طریق کار عموماً ثالثی الکائل ہیلائیڈز اپناتے ہیں۔ چونکہ اس میں کاربوکیٹائن بنتا ہے، اس لیے زیادہ آئنائز کرنے والے قطبی محللات (O–H، N–H بند والے) اس کے حق میں ہیں۔ مثلاً ٹرشری بیوٹائل برومائیڈ کی ہائیڈرولائسز SN1 طریق کار سے ہوتی ہے، جیسا کہ نیچے دکھایا گیا ہے۔',
 'SN1 معنا یې بدلون، نیوکلیوفایلي، یو مالیکولي ده. دا دوه پړاوه میکانیزم دی. لومړی پړاو ورو دی (د سرعت ټاکونکی یا محدودوونکی پړاو) او د الکایل هالایډ یا سبسټرېټ د تجزیې له لارې منځنی کاربوکاټیون جوړوي. د یو مالیکولي اصطلاح معنا دا ده چې د سرعت ټاکونکي پړاو په انتقالي حالت کې یوازې یو مالیکول ښکېل دی. دویم پړاو چټک دی او پر سطحي کاربوکاټیون د نیوکلیوفایل برید او د محصول جوړېدل پکې شامل دي. د SN1 میکانیزم معمولاً درېیمي الکایل هالایډونه تعقیبوي. څرنګه چې کاربوکاټیون پکې جوړېږي، ډېر ایونایزوونکي قطبي محللونه (O–H، N–H تړون لرونکي) یې ملاتړ کوي. د بېلګې په توګه د ټرشري بیوټیل برومایډ هایدرولیز د SN1 میکانیزم تعقیبوي، لکه څنګه چې لاندې ښودل شوی.')
add('Step–1: The substrate undergoes ionization and yield a carbocation. The bromine atom completely detaches from the substrate as bromide ion.','مرحلہ–1: سبسٹریٹ آئنائز ہو کر کاربوکیٹائن دیتا ہے۔ برومین ایٹم برومائیڈ آئن کے طور پر سبسٹریٹ سے مکمل طور پر الگ ہو جاتا ہے۔','پړاو–1: سبسټرېټ ایونایز کېږي او کاربوکاټیون ورکوي. د برومین اټوم د برومایډ ایون په توګه له سبسټرېټ څخه بشپړ جلا کېږي.')
visual('chem12-p89-sn1-step1',step1)
add('Step–2: In second step, the entering nucleophile attacks the planar carbocation on either face, to produce the end product.','مرحلہ–2: دوسرے مرحلے میں داخل ہونے والا نیوکلیوفائل مستوی کاربوکیٹائن پر کسی بھی جانب سے حملہ کر کے آخری پیداوار بناتا ہے۔','پړاو–2: په دویم پړاو کې ننوتونکی نیوکلیوفایل پر سطحي کاربوکاټیون له هرې خوا برید کوي او وروستی محصول جوړوي.')
visual('chem12-p89-sn1-step2',step2)
add('The kinetic studies have shown that reactions proceeding through SN1 mechanism follow the first order kinetics. The rate of reaction depends only upon the concentration of substrate. The rate equation for above reaction is; rate = k [(CH₃)₃CBr]',
 'حرکیاتی مطالعات سے ظاہر ہوا ہے کہ SN1 طریق کار سے ہونے والے تعاملات پہلے درجے کی حرکیات پر چلتے ہیں۔ تعامل کی شرح صرف سبسٹریٹ کے ارتکاز پر منحصر ہے۔ اوپر کے تعامل کی شرح کی مساوات ہے؛ rate = k [(CH₃)₃CBr]',
 'حرکي مطالعاتو ښودلې چې د SN1 میکانیزم له لارې تعاملونه د لومړۍ درجې حرکیات تعقیبوي. د تعامل سرعت یوازې د سبسټرېټ پر غلظت پورې اړه لري. د پورته تعامل د سرعت معادله دا ده؛ rate = k [(CH₃)₃CBr]')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Two transition states are formed in SN1 mechanism. One in first step during formation of intermediate, the other in second step during formation of product from intermediate.','SN1 طریق کار میں دو عبوری حالتیں بنتی ہیں۔ ایک پہلے مرحلے میں درمیانی کی تشکیل کے دوران، دوسری دوسرے مرحلے میں درمیانی سے پیداوار بنتے وقت۔','په SN1 میکانیزم کې دوه انتقالي حالتونه جوړېږي. یو په لومړي پړاو کې د منځني د جوړېدو پر مهال، بل په دویم پړاو کې له منځني څخه د محصول د جوړېدو پر مهال.')
add('The intermediate carbocation is planar, the nucleophile attack from either side. If a nucleophile attacks the carbocation from the side of the leaving group, the product molecule shows retention of configuration. Attack from the side opposite to leaving group, gives a product molecule showing inversion of configuration. If the reactant is chiral, mixture of two enantiomers (Section 16.6.5) are produced, called racemic mixture and this process is called racemization. Racemization is simply a combination of retention and inversion. However in SN1, the product is rarely completely racemic and there is often more inversion than retention of configuration. This is also called partial racemization.',
 'درمیانی کاربوکیٹائن مستوی ہوتا ہے، اس لیے نیوکلیوفائل کسی بھی جانب سے حملہ کرتا ہے۔ اگر نیوکلیوفائل کاربوکیٹائن پر خارج ہونے والے گروپ کی جانب سے حملہ کرے تو پیداواری سالمہ ترتیب کی برقراری ظاہر کرتا ہے۔ خارج ہونے والے گروپ کی مخالف جانب سے حملہ ترتیب کی الٹ والا پیداواری سالمہ دیتا ہے۔ اگر متعامل کائرل ہو تو دو اینینشیومرز (حصہ 16.6.5) کا آمیزہ بنتا ہے، جسے ریسیمک آمیزہ کہتے ہیں اور اس عمل کو ریسیمائزیشن کہتے ہیں۔ ریسیمائزیشن دراصل برقراری اور الٹ کا مجموعہ ہے۔ تاہم SN1 میں پیداوار شاذ و نادر ہی مکمل ریسیمک ہوتی ہے اور اکثر ترتیب کی برقراری سے زیادہ الٹ ہوتا ہے۔ اسے جزوی ریسیمائزیشن بھی کہتے ہیں۔',
 'منځنی کاربوکاټیون سطحي دی، نو نیوکلیوفایل له هرې خوا برید کوي. که نیوکلیوفایل د وتونکي ګروپ له خوا پر کاربوکاټیون برید وکړي، د محصول مالیکول د ترتیب ساتنه ښيي. د وتونکي ګروپ له مخالفې خوا برید داسې محصول ورکوي چې د ترتیب اوښتون ښيي. که تعامل کوونکی کایرل وي، د دوو اینانټیومرونو (برخه 16.6.5) ګډوله جوړېږي چې ریسیمیک ګډوله بلل کېږي او دې بهیر ته ریسیمایزېشن وايي. ریسیمایزېشن یوازې د ساتنې او اوښتون ترکیب دی. خو په SN1 کې محصول ډېر لږ بشپړ ریسیمیک وي او ډېری د ترتیب له ساتنې ډېر اوښتون وي. دې ته نیمګړی ریسیمایزېشن هم وايي.')
record=section('17.5','Carbocation stability and SN1 mechanism','کاربوکیٹائن کی پائیداری اور SN1 طریق کار','د کاربوکاټیون ثبات او د SN1 میکانیزم',paras,layout,blocks,'170–171')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':89,'printedPages':[170,171]}]
record['sourceContinuesOnPdfPage']=90
issues=[{'id':'chem12-p171-sentence-continues','printedPage':171,'description':'Last sentence of printed 171 completes on printed 172 ("and there is often more inversion… partial racemization."); kept whole here. Printed "Realtive" and "rate-determing" retained.'}]
carry=[{'from':'17.5','to':'17.6','startsAt':'17.1.6.4 S2 Mechanism'}]
if __name__=='__main__':save(89,[record],carry=carry,issues=issues,chapter_number=17)
