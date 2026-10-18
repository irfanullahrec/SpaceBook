"""PDF133 printed260–261: reactivity (resonance, acidity), 20.7 reactions — acyl halides, anhydrides, esters."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl,chain
F=Fig('arrow133');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
def ch(y,toks,up,center,size=15):return chain(F,0,y,toks,size,None,up,center=center)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'thionyl chloride':('تھایونائل کلورائیڈ','تایونیل کلوراید'),'acid chloride':('ایسڈ کلورائیڈ','اسید کلوراید'),'phosphorous':('فاسفورس','فاسفورس'),'pentachloride':('پینٹا کلورائیڈ','پنټا کلوراید'),
   'carboxylic acids':('کاربوکسلک ایسڈز','کاربوکسیلیک اسیدونه'),'anhydride':('این ہائیڈرائیڈ','انهایدراید'),'acetic acids':('ایسیٹک ایسڈز','اسیټیک اسیدونه'),'acetic anhydride':('ایسیٹک این ہائیڈرائیڈ','اسیټیک انهایدراید'),
   'alcohol':('الکوحل','الکول'),'ester':('ایسٹر','ایسټر'),'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'ethyl acetate':('ایتھائل ایسیٹیٹ','ایتیل اسیټېټ'),'acetyl chloride':('ایسیٹائل کلورائیڈ','اسیټیل کلوراید'),'pyridine':('پیریڈین','پیریډین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def res(lang):
 s=F.start(100)+C(250,60,'H','ÖH')+t(380,60,'⟷',20)+t(500,60,'H—C',16)+line(518,50,540,32)+t(552,28,'Ö:⁻',15)+line(518,62,540,80)+line(524,58,546,76)+t(556,92,'ȮH⁺',15)
 return s+'</svg>'
def halides(lang):
 s=F.start(220)
 s+=C(110,60,'R','OH')+t(110,84,lb(lang,'carboxylic acid'),12)+t(230,60,'+  SOCl₂',16)+t(240,84,lb(lang,'thionyl chloride'),12)+F.arrow(300,400,54)+C(490,60,'R','Cl')+t(490,84,lb(lang,'acid chloride'),12)+t(660,60,'+  SO₂  +  HCl',16)
 s+=C(110,170,'R','OH')+t(110,194,lb(lang,'carboxylic acid'),12)+t(230,170,'+  PCl₅',16)+t(240,194,lb(lang,'phosphorous'),12)+t(240,210,lb(lang,'pentachloride'),12)+F.arrow(300,400,164)+C(490,170,'R','Cl')+t(490,194,lb(lang,'acid chloride'),12)+t(670,170,'+  POCl₃  +  HCl',16)
 return s+'</svg>'
def anhyd(lang):
 s=F.start(210)
 s+=ch(60,['R','—','C','—','OH','  +  ','HO','—','C','—','R'],{2:'=O',8:'=O'},200)+t(200,86,lb(lang,'carboxylic acids'),12)+F.arrow(410,490,54,'P₂O₅','−H₂O')+ch(60,['R','—','C','—','O','—','C','—','R'],{2:'=O',6:'=O'},660)+t(660,86,lb(lang,'anhydride'),12)
 s+=ch(170,['CH₃','—','C','—','OH','  +  ','HO','—','C','—','CH₃'],{2:'=O',8:'=O'},200)+t(200,196,lb(lang,'acetic acids'),12)+F.arrow(410,490,164,'P₂O₅','−H₂O')+ch(170,['CH₃','—','C','—','O','—','C','—','CH₃'],{2:'=O',6:'=O'},660)+t(660,196,lb(lang,'acetic anhydride'),12)
 return s+'</svg>'
def ester(lang):
 s=F.start(210)
 s+=C(110,60,"R′",'OH')+t(110,84,lb(lang,'carboxylic acid'),12)+t(250,60,'+  H—O—R',16)+t(270,84,lb(lang,'alcohol'),12)+F.eq(350,440,54)+t(395,42,'H⁺',12)+C(540,60,"R′",'OR')+t(540,84,lb(lang,'ester'),12)+t(680,60,'+  H₂O',16)
 s+=C(110,170,'CH₃','OH')+t(110,194,lb(lang,'acetic acid'),12)+t(270,170,'+  H—O—C₂H₅',16)+t(280,194,lb(lang,'ethyl alcohol'),12)+F.eq(380,460,164)+t(420,152,'H⁺',12)+C(570,170,'CH₃','OC₂H₅')+t(570,194,lb(lang,'ethyl acetate'),12)+t(720,170,'+  H₂O',16)
 return s+'</svg>'
def alcoholysis(lang):
 s=F.start(210)
 s+=C(100,60,'CH₃','Cl')+t(100,84,lb(lang,'acetyl chloride'),12)+t(260,60,'+  C₂H₅—O—H',16)+t(270,84,lb(lang,'ethyl alcohol'),12)+F.arrow(370,460,54,lb(lang,'pyridine'))+C(560,60,'CH₃','OC₂H₅')+t(560,84,lb(lang,'ethyl acetate'),12)+t(710,60,'+  HCl',16)
 s+=ch(170,['CH₃','—','C','—','O','—','C','—','CH₃'],{2:'=O',6:'=O'},130)+t(130,196,lb(lang,'acetic anhydride'),12)+t(330,170,'+ C₂H₅—O—H',15)+t(330,196,lb(lang,'ethyl alcohol'),12)+F.arrow(420,480,164)+C(560,170,'CH₃','OC₂H₅')+t(560,196,lb(lang,'ethyl acetate'),12)+t(660,170,'+',15)+C(750,170,'CH₃','OH',)+t(750,196,lb(lang,'acetic acid'),12)
 return s+'</svg>'

add('The carboxyl group is also less susceptible to nucleophilic attack than aldehydes and ketones, because the carbon atom of the carboxyl group is less electrophilic, due to delocalization of one of lone-pair of hydroxyl group with carbonyl (Section 20.2).','کاربوکسل گروپ الڈیہائیڈز اور کیٹونز کے مقابلے میں نیوکلیوفائلی حملے کا کم نشانہ بنتا ہے، کیونکہ ہائیڈروآکسل گروپ کے ایک تنہا جوڑے کی کاربونل کے ساتھ غیر مقامیت کی وجہ سے کاربوکسل گروپ کا کاربن ایٹم کم الیکٹروفائلی ہوتا ہے (حصہ 20.2)۔','کاربوکسیل ګروپ د الدیهایډونو او کیټونونو په پرتله نیوکلیوفایلي برید ته لږ چمتو دی، ځکه د هایدروکسیل ګروپ د یوې یوازینۍ جوړې له کاربونیل سره د غیر ځایي کېدو له امله د کاربوکسیل ګروپ کاربني اټوم لږ الکتروفایلي دی (برخه 20.2).')
visual('chem12-p133-carboxyl-resonance',res)
add('Similarly the carbonyl group withdraws electrons from hydroxyl, making the O–H bond more polar and it becomes easier for the hydrogen atom to ionize than O–H bond of alcohols. Hence, carboxylic acids are more acidic than alcohols.','اسی طرح کاربونل گروپ ہائیڈروآکسل سے الیکٹران کھینچتا ہے جس سے O–H بند زیادہ قطبی ہو جاتا ہے اور الکوحلز کے O–H بند کے مقابلے میں ہائیڈروجن ایٹم کا آئنائز ہونا آسان ہو جاتا ہے۔ لہٰذا کاربوکسلک ایسڈز الکوحلز سے زیادہ تیزابی ہیں۔','همدارنګه کاربونیل ګروپ له هایدروکسیل څخه الکترونونه راکاږي، چې O–H تړون ډېر قطبي کوي او د الکولونو د O–H تړون په پرتله د هایدروجني اټوم ایونایز کېدل اسانه کېږي. نو کاربوکسیلیک اسیدونه له الکولونو ډېر تېزابي دي.')
add('20.7 Reactions of Carboxylic Acids','20.7 کاربوکسلک ایسڈز کے تعاملات','20.7 د کاربوکسیلیک اسیدونو تعاملونه','heading')
add('Following are some of the reactions of carboxylic acids that involve the conversion of the carboxylic acids to their derivatives as well as synthesis of some other compounds.','کاربوکسلک ایسڈز کے چند تعاملات درج ذیل ہیں جن میں کاربوکسلک ایسڈز کی ان کے مشتقات میں تبدیلی اور بعض دوسرے مرکبات کی تالیف شامل ہے۔','لاندې د کاربوکسیلیک اسیدونو ځینې تعاملونه دي چې د کاربوکسیلیک اسیدونو په مشتقاتو بدلېدل او د ځینو نورو مرکباتو جوړول پکې شامل دي.')
add('20.7.1 Conversion to Carboxylic Acid Derivatives','20.7.1 کاربوکسلک ایسڈ مشتقات میں تبدیلی','20.7.1 د کاربوکسیلیک اسید په مشتقاتو بدلول','heading')
add('20.7.1.1 Conversion to Acyl Halides','20.7.1.1 ایسائل ہیلائیڈز میں تبدیلی','20.7.1.1 په اسایل هالایډونو بدلول','heading')
add('Acyl halides or acid halides are the most reactive of carboxylic acid derivatives and they can be used for preparation of other functional derivatives of carboxylic acid. Acyl chlorides are more common and less expensive than bromides and iodides. They are usually prepared by replacing the –OH of carboxyl with –Cl, using thionyl chloride or phosphorous pentachloride.','ایسائل ہیلائیڈز یا ایسڈ ہیلائیڈز کاربوکسلک ایسڈ مشتقات میں سب سے زیادہ تعامل پذیر ہیں اور انہیں کاربوکسلک ایسڈ کے دوسرے فعلی مشتقات کی تیاری کے لیے استعمال کیا جا سکتا ہے۔ ایسائل کلورائیڈز برومائیڈز اور آیوڈائیڈز سے زیادہ عام اور سستے ہیں۔ انہیں عموماً تھایونائل کلورائیڈ یا فاسفورس پینٹا کلورائیڈ کے ذریعے کاربوکسل کے –OH کو –Cl سے بدل کر تیار کیا جاتا ہے۔','اسایل هالایډونه یا اسید هالایډونه د کاربوکسیلیک اسید په مشتقاتو کې تر ټولو ډېر تعامل کوونکي دي او د کاربوکسیلیک اسید د نورو فعالو مشتقاتو د چمتو کولو لپاره کارېدای شي. اسایل کلوراېډونه له بروماېډونو او ایوډاېډونو ډېر عام او ارزانه دي. معمولاً د تایونیل کلوراید یا فاسفورس پنټا کلوراید په کارولو سره د کاربوکسیل –OH په –Cl بدلولو چمتو کېږي.')
visual('chem12-p133-acyl-halides',halides)
add('20.7.1.2 Conversion to Acid Anhydrides','20.7.1.2 ایسڈ این ہائیڈرائیڈز میں تبدیلی','20.7.1.2 په اسید انهایدرایډونو بدلول','heading')
add('Acid anhydrides are derived from acids by removing water from two carboxylic acid molecules. As the name indicates, these are anhydrous carboxylic acids. They are actually diacyl oxides. The dehydration of water from carboxylic acid to form anhydride, can be accomplished by using dehydration agents like phosphorous pentaoxide.','ایسڈ این ہائیڈرائیڈز دو کاربوکسلک ایسڈ سالمات سے پانی نکال کر ایسڈز سے اخذ کیے جاتے ہیں۔ جیسا کہ نام سے ظاہر ہے، یہ بے آب کاربوکسلک ایسڈز ہیں۔ یہ دراصل ڈائی ایسائل آکسائیڈز ہیں۔ این ہائیڈرائیڈ بنانے کے لیے کاربوکسلک ایسڈ سے پانی کا اخراج فاسفورس پینٹا آکسائیڈ جیسے پانی کش عاملوں سے کیا جا سکتا ہے۔','اسید انهایدرایډونه له دوو کاربوکسیلیک اسید مالیکولونو څخه د اوبو په لرې کولو له اسیدونو اخیستل کېږي. لکه څنګه چې نوم یې ښيي، دا بې اوبو کاربوکسیلیک اسیدونه دي. په حقیقت کې ډای اسایل اکسایډونه دي. د انهایدراید د جوړولو لپاره له کاربوکسیلیک اسید څخه د اوبو لرې کول د فاسفورس پنټا اکساید په څېر اوبه ایستونکو عاملونو په کارولو ترسره کېدای شي.')
visual('chem12-p133-anhydrides',anhyd)
add('20.7.1.3 Conversion to Esters','20.7.1.3 ایسٹرز میں تبدیلی','20.7.1.3 په ایسټرونو بدلول','heading')
add('Esters are a class of organic compounds that are derived from acids by replacing the hydroxyl group (–OH) by an alkoxy group (–OR). They are obtained by elimination of water molecule from an acid and an alcohol.','ایسٹرز نامیاتی مرکبات کی ایک جماعت ہیں جو ایسڈز سے ہائیڈروآکسل گروپ (–OH) کو الکوآکسی گروپ (–OR) سے بدل کر اخذ کیے جاتے ہیں۔ یہ ایسڈ اور الکوحل سے پانی کے سالمے کے اخراج سے حاصل ہوتے ہیں۔','ایسټرونه د عضوي مرکباتو یوه ډله ده چې له اسیدونو څخه د هایدروکسیل ګروپ (–OH) په الکوکسي ګروپ (–OR) بدلولو اخیستل کېږي. دا له اسید او الکول څخه د اوبو د مالیکول په ایستلو ترلاسه کېږي.')
add('When a carboxylic acid and an alcohol are heated in the presence of an acid catalyst, an equilibrium is established with the formation of ester and water. This reaction is reversible and called esterification (Section 18.1.7.4). The position of equilibrium can be made more favorable in the right, by using either the alcohol or the carboxylic acid in excess, or removing water from the reaction mixture.','جب کاربوکسلک ایسڈ اور الکوحل کو تیزابی عمل انگیز کی موجودگی میں گرم کیا جاتا ہے تو ایسٹر اور پانی بننے کے ساتھ توازن قائم ہو جاتا ہے۔ یہ تعامل معکوس ہے اور ایسٹریفکیشن کہلاتا ہے (حصہ 18.1.7.4)۔ الکوحل یا کاربوکسلک ایسڈ کو زیادہ مقدار میں استعمال کر کے، یا تعاملی آمیزے سے پانی نکال کر توازن کا مقام دائیں جانب زیادہ موافق بنایا جا سکتا ہے۔','کله چې کاربوکسیلیک اسید او الکول د اسیدي کتلست په شتون کې تود شي، د ایسټر او اوبو په جوړېدو سره توازن رامنځته کېږي. دا تعامل بېرته ګرځېدونکی دی او ایسټریفیکېشن بلل کېږي (برخه 18.1.7.4). د الکول یا کاربوکسیلیک اسید په زیاته اندازه کارولو، یا د تعامل له ګډولې څخه د اوبو په لرې کولو د توازن موقعیت ښي لوري ته ډېر مناسب کېدای شي.')
visual('chem12-p133-esterification',ester)
add('Ethyl acetate is an important ester which can be prepared by this method by the reaction of acetic acid with ethanol.','ایتھائل ایسیٹیٹ ایک اہم ایسٹر ہے جو اس طریقے سے ایسیٹک ایسڈ اور ایتھانول کے تعامل سے تیار کیا جا سکتا ہے۔','ایتیل اسیټېټ یو مهم ایسټر دی چې په دې طریقه د اسیټیک اسید او ایتانول د تعامل په واسطه چمتو کېدای شي.')
add('Esters can also be prepared by the reaction of an alcohol with acid halide or acid anhydride (alcoholysis of acid halide or anhydride). In case of conversion of acid halide to ester, pyridine base is used to consume the HCl formed in reaction.','ایسٹرز الکوحل کے ایسڈ ہیلائیڈ یا ایسڈ این ہائیڈرائیڈ سے تعامل (ایسڈ ہیلائیڈ یا این ہائیڈرائیڈ کی الکوحلائسز) سے بھی تیار کیے جا سکتے ہیں۔ ایسڈ ہیلائیڈ کو ایسٹر میں بدلنے کی صورت میں تعامل میں بننے والے HCl کو جذب کرنے کے لیے پیریڈین اساس استعمال کی جاتی ہے۔','ایسټرونه د الکول له اسید هالاید یا اسید انهایدراید سره د تعامل (د اسید هالاید یا انهایدراید الکولایسس) په واسطه هم چمتو کېدای شي. د اسید هالاید په ایسټر بدلولو کې په تعامل کې جوړ شوي HCl د جذبولو لپاره پیریډین قلوي کارېږي.')
visual('chem12-p133-alcoholysis',alcoholysis)
record=section('20.6','Reactivity of carboxyl group; acyl halides, anhydrides and esters','کاربوکسل گروپ کی تعامل پذیری؛ ایسائل ہیلائیڈز، این ہائیڈرائیڈز اور ایسٹرز','د کاربوکسیل ګروپ تعامل وړتیا؛ اسایل هالایډونه، انهایدرایډونه او ایسټرونه',paras,layout,blocks,'260–261')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':133,'printedPages':[260,261]}]
record['sourceContinuesOnPdfPage']=134
trim=[{'id':'20.7','startsAt':'20.7.1.4 Conversion to Amides'}]
if __name__=='__main__':save(133,[record],trim=trim,chapter_number=20)
