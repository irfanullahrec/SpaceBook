"""PDF183 printed360–361: combustion analysis apparatus (Figure 24.1), %C/%H/%O formulae, empirical and molecular formula, Example 24.1 (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow183');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
K=lambda lang,*v:v[{'en':0,'ur':1,'ps':2}[lang]]
def frac(x,y,n,d,size=14):
 w=max(len(n),len(d))*size*0.52;return t(x,y-8,n,size)+line(x-w/2,y,x+w/2,y,1.2)+t(x,y+18,d,size)
def formula_rows(rows,h=60):
 """rows: list of (lhs, [(kind, a, b)...]) kinds: 't' text, 'f' fraction."""
 def f(lang):
  s=F.start(h*len(rows)+10)
  for i,(lhs,parts) in enumerate(rows):
   y=34+h*i;x=230;s+=t(x-50,y+5,lhs,15)
   for kind,a,b in parts:
    if kind=='t':w=len(a)*8+10;s+=t(x+w/2,y+5,a,14);x+=w
    else:w=max(len(a),len(b))*7.3+20;s+=frac(x+w/2,y,a,b);x+=w
  return s+'</svg>'
 return f
def app(lang):
 s=F.start(220)+'<rect x="150" y="60" width="200" height="90" rx="14" fill="#546e7a"/><rect x="170" y="80" width="200" height="50" rx="20" fill="#ef9a9a" stroke="#555"/>'
 s+='<rect x="400" y="80" width="130" height="50" rx="22" fill="#c5e1a5" stroke="#555"/><rect x="560" y="80" width="130" height="50" rx="22" fill="#b39ddb" stroke="#555"/>'+line(370,105,400,105,4,'#90a4ae')+line(530,105,560,105,4,'#90a4ae')+F.arrow(60,150,105)+F.arrow(690,770,105)
 s+=t(60,94,'O₂',13)+t(230,40,K(lang,'Furnace','بھٹی','بټۍ'),12)+t(240,180,K(lang,'Sample','نمونہ','نمونه'),12)+t(470,40,'CO₂, H₂O, O₂',12)+t(470,56,K(lang,'and other gases','اور دوسری گیسیں','او نور ګازونه'),12)
 s+=t(465,156,K(lang,'H₂O absorber','H₂O جاذب','H₂O جذبوونکی'),12)+t(465,172,K(lang,'such as Mg(ClO₄)₂','مثلاً Mg(ClO₄)₂','لکه Mg(ClO₄)₂'),12)+t(625,156,K(lang,'CO₂ absorber','CO₂ جاذب','CO₂ جذبوونکی'),12)+t(625,172,K(lang,'such as NaOH','مثلاً NaOH','لکه NaOH'),12)
 s+=t(790,90,'O₂',12)+t(800,124,K(lang,'and other gases','اور دوسری گیسیں','او نور ګازونه'),11)
 return s+'</svg>'

add('… furnace and trapped in a pair of absorbers. Water is absorbed in a sample of magnesium perchlorate (Mg(ClO₄)₂ of known mass, and carbon dioxide is absorbed by aqueous solution of sodium or potassium hydroxide. The increase in masses of both absorbers is the masses of water and carbon dioxide produced respectively, during combustion.','… بھٹی سے باہر بہا کر جاذبوں کے ایک جوڑے میں قید کر لیے جاتے ہیں۔ پانی معلوم کمیت والے میگنیشیم پرکلوریٹ Mg(ClO₄)₂ کے نمونے میں جذب ہوتا ہے، اور کاربن ڈائی آکسائیڈ سوڈیم یا پوٹاشیم ہائیڈروآکسائیڈ کے آبی محلول میں جذب ہوتی ہے۔ دونوں جاذبوں کی کمیت میں اضافہ بالترتیب احتراق کے دوران بننے والے پانی اور کاربن ڈائی آکسائیڈ کی کمیت ہے۔','… له بټۍ بهر وړل کېږي او د جذبوونکو په یوه جوړه کې ساتل کېږي. اوبه د معلومې کتلې د مګنیزیم پرکلورېټ Mg(ClO₄)₂ په نمونه کې جذبېږي، او کاربن ډای اکساید د سوډیم یا پوتاشیم هایدروکساید په اوبلن محلول کې جذبېږي. د دواړو جذبوونکو په کتلو کې زیاتوالی په ترتیب سره د سوځېدو پر مهال د تولید شویو اوبو او کاربن ډای اکساید کتلې دي.')
visual('chem12-figure24-1',app)
add('Figure 24.1 Procedure of combustion analysis.','شکل 24.1 احتراقی تجزیے کا طریقۂ کار۔','شکل 24.1 د سوځېدنې تحلیل کړنلاره.')
add('Percentage of C and H in organic compound are calculated by the following formulae.','نامیاتی مرکب میں C اور H کا فیصد درج ذیل فارمولوں سے نکالا جاتا ہے۔','په عضوي مرکب کې د C او H سلنه د لاندې فورمولونو په واسطه محاسبه کېږي.')
visual('chem12-p183-percent-formulae',lambda l:formula_rows([('%C =',[('f',K(l,'mass of CO₂ produced','پیدا شدہ CO₂ کی کمیت','د تولید شوي CO₂ کتله'),K(l,'mass of organic compound','نامیاتی مرکب کی کمیت','د عضوي مرکب کتله')),('t','×',''),('f','12.011','44.010'),('t','× 100','')]),
 ('%H =',[('f',K(l,'mass of H₂O produced','پیدا شدہ H₂O کی کمیت','د تولید شوو H₂O کتله'),K(l,'mass of organic compound','نامیاتی مرکب کی کمیت','د عضوي مرکب کتله')),('t','×',''),('f','2.0158','18.0153'),('t','× 100','')])],70)(l))
add('Percentage of oxygen is calculated as; %O = 100 – (%C + %H)','آکسیجن کا فیصد یوں نکالا جاتا ہے؛ %O = 100 – (%C + %H)','د اکسیجن سلنه داسې محاسبه کېږي؛ %O = 100 – (%C + %H)')
add('Calculation of Empirical Formula','تجرباتی فارمولے کا حساب','د تجربي فورمول محاسبه','heading')
add('Empirical formula is the formula that gives the simplest whole number ratio of the atoms of elements present in the compound. In order to find the empirical formula of a compound, the following steps should be followed.','تجرباتی فارمولا وہ فارمولا ہے جو مرکب میں موجود عناصر کے ایٹموں کا سادہ ترین مکمل عددی تناسب دیتا ہے۔ کسی مرکب کا تجرباتی فارمولا معلوم کرنے کے لیے درج ذیل مراحل اپنائے جائیں۔','تجربي فورمول هغه فورمول دی چې په مرکب کې د شتو عناصرو د اټومونو تر ټولو ساده بشپړه عددي نسبت ورکوي. د یوه مرکب د تجربي فورمول د موندلو لپاره باید لاندې ګامونه تعقیب شي.')
lines([('Number of moles of carbon, hydrogen and oxygen is calculated by the following formulae.','کاربن، ہائیڈروجن اور آکسیجن کے مولز کی تعداد درج ذیل فارمولوں سے نکالی جاتی ہے۔','د کاربن، هایدروجن او اکسیجن د مولونو شمېر د لاندې فورمولونو په واسطه محاسبه کېږي.')])
visual('chem12-p183-moles',lambda l:formula_rows([(K(l,'moles of C =','C کے مولز =','د C مولونه ='),[('f','%C','12.011')]),(K(l,'moles of H =','H کے مولز =','د H مولونه ='),[('f','%H','1.0079')]),(K(l,'moles of O =','O کے مولز =','د O مولونه ='),[('f','%O','15.9994')])],56)(l))
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('If we have 100 grams compound then percentage of C, H and O should be taken as their grams present in 100 grams compound. Now moles = Mass (in g) / Molar Mass','اگر ہمارے پاس 100 گرام مرکب ہو تو C، H اور O کے فیصد کو 100 گرام مرکب میں ان کے گرام سمجھا جائے۔ اب مولز = کمیت (گرام میں) / مولر کمیت','که موږ 100 ګرامه مرکب ولرو، نو د C، H او O سلنه باید په 100 ګرامه مرکب کې د هغوی ګرامونه وګڼل شي. اوس مولونه = کتله (په ګرام) / مولر کتله')
lines([('The simplest ratio between the numbers of moles is found out by dividing the number of moles of each element by the smallest number of moles.','مولز کی تعداد کے درمیان سادہ ترین تناسب ہر عنصر کے مولز کی تعداد کو مولز کی سب سے چھوٹی تعداد سے تقسیم کر کے معلوم کیا جاتا ہے۔','د مولونو د شمېر ترمنځ تر ټولو ساده نسبت د هر عنصر د مولونو شمېر د مولونو پر تر ټولو کوچني شمېر وېشلو موندل کېږي.'),
 ('If the ratio is not in whole numbers then number of moles of each element is multiplied by a suitable small number to get the whole number ratio.','اگر تناسب مکمل اعداد میں نہ ہو تو ہر عنصر کے مولز کی تعداد کو کسی مناسب چھوٹے عدد سے ضرب دے کر مکمل عددی تناسب حاصل کیا جاتا ہے۔','که نسبت په بشپړو عددونو کې نه وي، نو د هر عنصر د مولونو شمېر په یوه مناسب کوچني عدد ضربېږي څو بشپړ عددي نسبت ترلاسه شي.'),
 ('Finally the symbol of each element is written and their number of moles are written as subscripts. This gives the empirical formula of a compound.','آخر میں ہر عنصر کی علامت لکھی جاتی ہے اور ان کے مولز کی تعداد ذیلی اعداد کے طور پر لکھی جاتی ہے۔ اس سے مرکب کا تجرباتی فارمولا ملتا ہے۔','په پای کې د هر عنصر سمبول لیکل کېږي او د هغوی د مولونو شمېر د لاندیني عددونو په توګه لیکل کېږي. دا د مرکب تجربي فورمول ورکوي.')])
add('Calculation of Molecular Formula','سالماتی فارمولے کا حساب','د مالیکولي فورمول محاسبه','heading')
add('Molecular formula shows the actual number of atoms of each kind of element in a compound. Molecular formula is either same to empirical formula or integral multiple of the empirical formula.','سالماتی فارمولا مرکب میں ہر قسم کے عنصر کے ایٹموں کی اصل تعداد ظاہر کرتا ہے۔ سالماتی فارمولا یا تو تجرباتی فارمولے جیسا ہوتا ہے یا اس کا مکمل عددی مضرب۔','مالیکولي فورمول په مرکب کې د هر ډول عنصر د اټومونو اصلي شمېر ښيي. مالیکولي فورمول یا له تجربي فورمول سره یو شان وي یا د هغه بشپړ عددي مضرب.')
visual('chem12-p183-n',lambda l:formula_rows([(K(l,'molecular formula =','سالماتی فارمولا =','مالیکولي فورمول ='),[('t',K(l,'n × empirical formula','n × تجرباتی فارمولا','n × تجربي فورمول'),'')]),(K(l,'where  n =','جہاں  n =','چېرته چې  n ='),[('f',K(l,'molecular mass','سالماتی کمیت','مالیکولي کتله'),K(l,'empirical formula mass','تجرباتی فارمولا کمیت','د تجربي فورمول کتله'))])],60)(l))
add('The molecular mass can be obtained from mass spectrometric experiment (Section 24.2.2.4) or with the help of colligative properties of solution.','سالماتی کمیت ماس سپیکٹرومیٹری تجربے (حصہ 24.2.2.4) سے یا محلول کی اجتماعی خصوصیات کی مدد سے حاصل کی جا سکتی ہے۔','مالیکولي کتله د ماس سپکټرومیټري له تجربې (برخه 24.2.2.4) یا د محلول د ټولیزو ځانګړنو په مرسته ترلاسه کېدای شي.')
add('Example 24.1: Trioxane (1,3,5-trioxane) is a cyclic trimer of formaldehyde, a precursor for the production of polyoxymethylene plastics. 17.471 g of trioxane upon complete combustion produces 10.477 g of water and 25.612 g of carbon dioxide. The molecular mass of trioxane determined by mass spectrometry, is 90.079 a.m.u. Calculate the empirical and molecular formulae of trioxane.','مثال 24.1: ٹرائی آکسین (1،3،5-ٹرائی آکسین) فارم الڈیہائیڈ کا حلقوی ٹرائمر ہے جو پولی آکسی میتھیلین پلاسٹک کی تیاری کا ابتدائی مادہ ہے۔ 17.471 g ٹرائی آکسین مکمل احتراق پر 10.477 g پانی اور 25.612 g کاربن ڈائی آکسائیڈ دیتا ہے۔ ماس سپیکٹرومیٹری سے متعین ٹرائی آکسین کی سالماتی کمیت 90.079 a.m.u ہے۔ ٹرائی آکسین کا تجرباتی اور سالماتی فارمولا نکالیں۔','بېلګه 24.1: ټرای اکسان (1،3،5-ټرای اکسان) د فورمالدیهاید حلقوي ټرایمر دی چې د پولي اکسي میتیلین پلاستیکونو د تولید مخکنی ماده ده. 17.471 g ټرای اکسان د بشپړ سوځېدو پر مهال 10.477 g اوبه او 25.612 g کاربن ډای اکساید تولیدوي. د ماس سپکټرومیټري په واسطه ټاکل شوې د ټرای اکسان مالیکولي کتله 90.079 a.m.u ده. د ټرای اکسان تجربي او مالیکولي فورمولونه محاسبه کړئ.')
add('Solution:','حل:','حل:','heading')
visual('chem12-p183-example-solution',lambda l:formula_rows([('%C =',[('f','25.612g','17.471g'),('t','×',''),('f','12.011','44.010'),('t','× 100 = 40.008%','')]),('%H =',[('f','10.477g','17.471g'),('t','×',''),('f','2.0158','18.0153'),('t','× 100 = 6.71%','')]),('%O =',[('t','100 – (40.008 + 6.71) = 53.282%','')]),
 (K(l,'moles of C =','C کے مولز =','د C مولونه ='),[('f','40.008','12.011'),('t','= 3.33','')]),(K(l,'moles of H =','H کے مولز =','د H مولونه ='),[('f','6.71','1.0079'),('t','= 6.66','')])],62)(l))
record=section('24.2','Combustion analysis calculations and empirical/molecular formula','احتراقی تجزیے کے حسابات اور تجرباتی/سالماتی فارمولا','د سوځېدنې تحلیل محاسبې او تجربي/مالیکولي فورمول',paras,layout,blocks,'360–361')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':183,'printedPages':[360,361]}]
record['sourceContinuesOnPdfPage']=184
record['sourceIllustrationReview']='Figure 24.1 combustion-train photograph re-drawn as labelled schematic SVG; placeholder legacy SVG dropped.'
carry=[{'from':'24.2','to':'24.3','startsAt':'53.282\nmoles of O'}]
if __name__=='__main__':save(183,[record],carry=carry,chapter_number=24)
