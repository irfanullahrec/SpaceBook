"""PDF93 printed178–179: Grignard reactions with aldehydes/ketones, esters and carbon dioxide."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,_w
F=Fig('arrow93');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'formaldehyde':('فارم الڈیہائیڈ','فورمالدیهاید'),'higher aldehyde':('بڑا الڈیہائیڈ','لوړ الدیهاید'),'ketone':('کیٹون','کیټون'),'addition product':('اضافی پیداوار','اضافي محصول'),
   '1°-alcohol':('1°-الکوحل','1°-الکول'),'2°-alcohol':('2°-الکوحل','2°-الکول'),'3°-alcohol':('3°-الکوحل','3°-الکول'),'(workup)':('(ورک اپ)','(ورک اپ)'),'ethyl formate':('ایتھائل فارمیٹ','ایتیل فورمېټ'),
   'aldehyde':('الڈیہائیڈ','الدیهاید'),'ethyl propanoate':('ایتھائل پروپانوئیٹ','ایتیل پروپانویټ'),'carbon dioxide':('کاربن ڈائی آکسائیڈ','کاربن ډای اکساید'),'carboxylic acid':('کاربوکسیلک ایسڈ','کاربوکسیلیک اسید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def _lay(x,y,left,right):
 toks=[left,'—','C','—',right];tot=sum(_w(k) for k in toks);cx=x-tot/2;out='';cc=0
 for k in toks:
  w=_w(k);out+=t(cx+w/2,y,k,17)
  if k=='C':cc=cx+w/2
  cx+=w
 return out,cc
def carbonyl(x,y,left,right):
 o,c=_lay(x,y,left,right);return o+t(c,y-38,'O',15)+line(c-3,y-32,c-3,y-16)+line(c+3,y-32,c+3,y-16)
def tetra(x,y,top,left,right,bot):
 o,c=_lay(x,y,left,right);return o+t(c,y-38,top,15)+line(c,y-32,c,y-16)+line(c,y+8,c,y+24)+t(c,y+42,bot,15)
def aldket(lang):
 s=F.start(420)
 for i,(l,r,name,b,alc) in enumerate((('H','H','formaldehyde','H','1°-alcohol'),('R','H','higher aldehyde','R','2°-alcohol'),('R','R','ketone','R','3°-alcohol'))):
  y=60+130*i;s+=t(80,y,'R—MgX  +',16)+carbonyl(190,y,l,r)+t(190,y+26,lb(lang,name),12)+F.arrow(260,310,y-6)
  s+=tetra(400,y,'O⁻Mg⁺X',l,r,'R')+t(400,y+62,lb(lang,'addition product'),12)+F.arrow(480,580,y-6,'H₃O⁺',lb(lang,'(workup)'))+tetra(680,y,'OH',l,r,'R')+t(680,y+62,lb(lang,alc),12)
 return s+'</svg>'
def formate(lang):
 s=F.start(290)+t(70,70,'R—MgX  +',16)+carbonyl(200,70,'H','OC₂H₅')+t(200,96,lb(lang,'ethyl formate'),12)+F.arrow(285,320,64)
 s+=tetra(420,70,'O⁻Mg⁺X','H','OC₂H₅','R')+t(420,132,lb(lang,'addition product'),12)+F.arrow(520,640,64,'−C₂H₅OMgX')+carbonyl(730,70,'R','H')+t(730,96,lb(lang,'aldehyde'),12)
 s+=line(800,110,800,220)+F.line(800,220,600,220,2,'#222','marker-end="url(#arrow93)"')+t(700,210,'1. RMgX',13)+t(700,240,'2. H₃O⁺',13)+t(700,256,lb(lang,'(workup)'),12)
 s+=tetra(470,226,'OH','R','H','R')+t(470,288,lb(lang,'2°-alcohol'),12)
 return s+'</svg>'
def higher(lang):
 s=F.start(290)+t(70,70,'R—MgX  +',16)+carbonyl(205,70,'C₂H₅','OC₂H₅')+t(205,96,lb(lang,'ethyl propanoate'),12)+F.arrow(300,330,64)
 s+=tetra(440,70,'O⁻Mg⁺X','C₂H₅','OC₂H₅','R')+t(440,132,lb(lang,'addition product'),12)+F.arrow(545,650,64,'−C₂H₅OMgX')+carbonyl(740,70,'C₂H₅','R')+t(740,96,lb(lang,'ketone'),12)
 s+=line(810,110,810,220)+F.line(810,220,610,220,2,'#222','marker-end="url(#arrow93)"')+t(710,210,'1. RMgX',13)+t(710,240,'2. H₃O⁺',13)+t(710,256,lb(lang,'(workup)'),12)
 s+=tetra(470,226,'OH','C₂H₅','R','R')+t(470,288,lb(lang,'3°-alcohol'),12)
 return s+'</svg>'
def co2(lang):
 s=F.start(140)+t(80,70,'R—MgX  +',16)+t(190,30,'O',15)+line(187,36,187,52)+line(193,36,193,52)+t(190,70,'C',17)+line(187,78,187,94)+line(193,78,193,94)+t(190,112,'O',15)+t(190,132,lb(lang,'carbon dioxide'),12)
 s+=F.arrow(240,320,64)+carbonyl(420,70,'R','O⁻Mg⁺X')+t(420,96,lb(lang,'addition product'),12)+F.arrow(520,620,64,'H₃O⁺',lb(lang,'(workup)'))+carbonyl(720,70,'R','OH')+t(720,96,lb(lang,'carboxylic acid'),12)
 return s+'</svg>'

add('17.2.3.1 Reactions with Aldehydes and Ketones','17.2.3.1 الڈیہائیڈز اور کیٹونز سے تعاملات','17.2.3.1 له الدیهایډونو او کیټونونو سره تعاملونه','heading')
add('Grignard reagents react with aldehydes and ketones to yield addition products. Addition product upon workup with water or dilute acid solution yield alcohols. Formaldehyde produce primary alcohol, higher aldehydes produce secondary, while ketones produce tertiary alcohols on treatment with Grignard reagents.',
 'گرینیارڈ عاملین الڈیہائیڈز اور کیٹونز سے تعامل کر کے اضافی پیداواریں دیتے ہیں۔ اضافی پیداوار پانی یا ہلکے تیزابی محلول سے ورک اپ پر الکوحلز دیتی ہے۔ گرینیارڈ عاملین سے عمل کرانے پر فارم الڈیہائیڈ ابتدائی الکوحل، بڑے الڈیہائیڈز ثانوی جبکہ کیٹونز ثالثی الکوحلز دیتے ہیں۔',
 'ګرینیارډ عاملونه له الدیهایډونو او کیټونونو سره تعامل کوي او اضافي محصولات ورکوي. اضافي محصول له اوبو یا رقیق اسیدي محلول سره د ورک اپ پر مهال الکولونه ورکوي. له ګرینیارډ عاملونو سره د تعامل پر مهال فورمالدیهاید لومړنی الکول، لوړ الدیهایډونه دویمي او کیټونونه درېیمي الکولونه ورکوي.')
visual('chem12-p93-grignard-carbonyls',aldket)
add('Self-assessmnet','خود جانچ','ځان ارزونه','heading')
add('Write the reaction of methylmagnesium bromide with acetaldehyde and acetone, followed by acid workup. Also write the names of products.','میتھائل میگنیشیم برومائیڈ کا ایسیٹ الڈیہائیڈ اور ایسیٹون سے تعامل اور اس کے بعد تیزابی ورک اپ لکھیں۔ پیداواروں کے نام بھی لکھیں۔','له اسیټالدیهاید او اسیتون سره د میتایل مګنیزیم برومایډ تعامل او ورپسې اسیدي ورک اپ ولیکئ. د محصولاتو نومونه هم ولیکئ.')
add('17.2.3.2 Reactions with Esters','17.2.3.2 ایسٹرز سے تعاملات','17.2.3.2 له ایسټرونو سره تعاملونه','heading')
add('Grignard reagents react with esters to yield carbonyl compounds (aldehydes and ketones). These carbonyl compounds react with more of the Grignard reagent in the same reaction mixture and yield alcohols as the final products (Section 17.2.3.1).','گرینیارڈ عاملین ایسٹرز سے تعامل کر کے کاربونل مرکبات (الڈیہائیڈز اور کیٹونز) دیتے ہیں۔ یہ کاربونل مرکبات اسی تعاملی آمیزے میں مزید گرینیارڈ عامل سے تعامل کر کے آخری پیداوار کے طور پر الکوحلز دیتے ہیں (حصہ 17.2.3.1)۔','ګرینیارډ عاملونه له ایسټرونو سره تعامل کوي او کاربونیل مرکبات (الدیهایډونه او کیټونونه) ورکوي. دا کاربونیل مرکبات په همدې تعاملي ګډوله کې له نور ګرینیارډ عامل سره تعامل کوي او د وروستي محصول په توګه الکولونه ورکوي (برخه 17.2.3.1).')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('The second step, a “workup” with acid solution, occurs after our key Grignard reaction, and the remaining Grignard reagent is also destroyed by acid. Only water can also be used for workup.','دوسرا مرحلہ، یعنی تیزابی محلول سے ”ورک اپ“، ہمارے بنیادی گرینیارڈ تعامل کے بعد ہوتا ہے، اور باقی ماندہ گرینیارڈ عامل بھی تیزاب سے ختم ہو جاتا ہے۔ ورک اپ کے لیے صرف پانی بھی استعمال ہو سکتا ہے۔','دویم پړاو، یعنې له اسیدي محلول سره ”ورک اپ“، زموږ له اصلي ګرینیارډ تعامل وروسته ترسره کېږي، او پاتې ګرینیارډ عامل هم د اسید په واسطه له منځه ځي. د ورک اپ لپاره یوازې اوبه هم کارېدای شي.')
add('a. Reaction with esters of formic acid','a. فارمک ایسڈ کے ایسٹرز سے تعامل','a. د فورمیک اسید له ایسټرونو سره تعامل','heading')
add('Ester of formic acid is also called formate ester e.g. methyl formate, ethyl formate etc. Grignard reagent react with ethyl formate (or any other formate ester), yielding an addition product. Addition product undergoes elimination and forms an aldehyde. This aldehyde further reacts with another molecule of the Grignard reagent to yield a secondary alcohol as final product.',
 'فارمک ایسڈ کے ایسٹر کو فارمیٹ ایسٹر بھی کہتے ہیں، مثلاً میتھائل فارمیٹ، ایتھائل فارمیٹ وغیرہ۔ گرینیارڈ عامل ایتھائل فارمیٹ (یا کسی دوسرے فارمیٹ ایسٹر) سے تعامل کر کے اضافی پیداوار دیتا ہے۔ اضافی پیداوار اخراج سے گزر کر الڈیہائیڈ بناتی ہے۔ یہ الڈیہائیڈ گرینیارڈ عامل کے ایک اور سالمے سے مزید تعامل کر کے آخری پیداوار کے طور پر ثانوی الکوحل دیتا ہے۔',
 'د فورمیک اسید ایسټر ته فورمېټ ایسټر هم وايي، لکه میتایل فورمېټ، ایتیل فورمېټ او نور. ګرینیارډ عامل له ایتیل فورمېټ (یا بل فورمېټ ایسټر) سره تعامل کوي او اضافي محصول ورکوي. اضافي محصول ایستنه کوي او الدیهاید جوړوي. دا الدیهاید د ګرینیارډ عامل له بل مالیکول سره نور تعامل کوي او د وروستي محصول په توګه دویمی الکول ورکوي.')
visual('chem12-p93-formate',formate)
add('b. Reaction with esters of higher carboxylic acids','b. بڑے کاربوکسیلک ایسڈز کے ایسٹرز سے تعامل','b. د لوړو کاربوکسیلیک اسیدونو له ایسټرونو سره تعامل','heading')
add('Ester of higher carboxylic acids yield tertiary alcohol as final product. For example, ethyl propanoate reacts in the same way as ethyl formate but the end product of this reaction is a tertiary alcohol, through intermediate ketone.','بڑے کاربوکسیلک ایسڈز کے ایسٹر آخری پیداوار کے طور پر ثالثی الکوحل دیتے ہیں۔ مثلاً ایتھائل پروپانوئیٹ ایتھائل فارمیٹ کی طرح تعامل کرتا ہے لیکن اس تعامل کی آخری پیداوار درمیانی کیٹون کے ذریعے ثالثی الکوحل ہوتی ہے۔','د لوړو کاربوکسیلیک اسیدونو ایسټرونه د وروستي محصول په توګه درېیمی الکول ورکوي. د بېلګې په توګه ایتیل پروپانویټ د ایتیل فورمېټ په څېر تعامل کوي خو د دې تعامل وروستی محصول د منځني کیټون له لارې درېیمی الکول دی.')
visual('chem12-p93-higher-ester',higher)
add('17.2.3.3 Reaction with carbon dioxide','17.2.3.3 کاربن ڈائی آکسائیڈ سے تعامل','17.2.3.3 له کاربن ډای اکساید سره تعامل','heading')
add('Grignard reagents react with carbon dioxide forming an addition product. Addition product upon acid workup yields carboxylic acids.','گرینیارڈ عاملین کاربن ڈائی آکسائیڈ سے تعامل کر کے اضافی پیداوار بناتے ہیں۔ اضافی پیداوار تیزابی ورک اپ پر کاربوکسیلک ایسڈز دیتی ہے۔','ګرینیارډ عاملونه له کاربن ډای اکساید سره تعامل کوي او اضافي محصول جوړوي. اضافي محصول د اسیدي ورک اپ پر مهال کاربوکسیلیک اسیدونه ورکوي.')
visual('chem12-p93-co2',co2)
add('For example methylmagnesium bromide upon addition to carbon dioxide followed by acid workup results acetic acid.','مثلاً میتھائل میگنیشیم برومائیڈ کاربن ڈائی آکسائیڈ میں اضافے اور اس کے بعد تیزابی ورک اپ سے ایسیٹک ایسڈ دیتا ہے۔','د بېلګې په توګه میتایل مګنیزیم برومایډ کاربن ډای اکساید ته د زیاتېدو او ورپسې اسیدي ورک اپ په پایله کې اسیټیک اسید ورکوي.')
record=section('17.9','Grignard reactions with carbonyls, esters and carbon dioxide','گرینیارڈ عاملین کے کاربونلز، ایسٹرز اور کاربن ڈائی آکسائیڈ سے تعاملات','د ګرینیارډ عاملونو تعاملونه له کاربونیلونو، ایسټرونو او کاربن ډای اکساید سره',paras,layout,blocks,'178–179')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':93,'printedPages':[178,179]}]
record['sourceContinuesOnPdfPage']=94
carry=[{'from':'17.9','to':'17.10','startsAt':'CH,-MgBr+\nmethylmagnesium bromide'}]
if __name__=='__main__':save(93,[record],carry=carry,chapter_number=17)
