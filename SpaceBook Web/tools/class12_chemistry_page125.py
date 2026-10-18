"""PDF125 printed242–243: Tollen's and Fehling's/Benedict's tests, oxidation of ketones, Society Technology and Science (sugar ring forms)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl
import math
F=Fig('arrow125');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'aldehyde':('الڈیہائیڈ','الدیهاید'),'ammonium':('امونیم','امونیم'),'carboxylate':('کاربوکسیلیٹ','کاربوکسیلېټ'),'silver':('چاندی','سپین زر'),'carboxylate ion':('کاربوکسیلیٹ آئن','کاربوکسیلېټ ایون'),
   'cuprous oxide':('کیوپرس آکسائیڈ','کیوپرس اکساید'),'(red ppt)':('(سرخ رسوب)','(سور رسوب)'),'acetone':('ایسیٹون','اسیتون'),'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),
   'Open form':('کھلی صورت','خلاصه بڼه'),'Closed form':('بند صورت','تړلې بڼه'),'D-Fructose':('D-فرکٹوز','D-فرکټوز'),'A furanose ring':('فیورانوز حلقہ','فورانوز کړۍ'),'A pyranose ring':('پائرانوز حلقہ','پیرانوز کړۍ'),'D-Glucose':('D-گلوکوز','D-ګلوکوز')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def eqs(lang):
 s=F.start(170)+t(160,40,'RCHO + 2[Ag(NH₃)₂]OH',15)+t(90,62,lb(lang,'aldehyde'),12)+F.arrow(300,380,34)+t(570,40,'RCOO⁻NH₄⁺ + 3NH₃ + H₂O + 2Ag↓',15)+t(480,62,lb(lang,'ammonium'),12)+t(480,78,lb(lang,'carboxylate'),12)+t(730,62,lb(lang,'silver'),12)
 s+=t(160,125,'RCHO + 2Cu²⁺ + 5OH⁻',15)+t(90,147,lb(lang,'aldehyde'),12)+F.arrow(300,380,119)+t(540,125,'RCOO⁻ + Cu₂O↓ + 3H₂O',15)+t(460,147,lb(lang,'carboxylate ion'),12)+t(580,147,lb(lang,'cuprous oxide'),12)+t(580,163,lb(lang,'(red ppt)'),12)
 return s+'</svg>'
def ketone(lang):return F.start(100)+C(160,60,'CH₃','CH₃')+t(270,60,'+ 4[O]',15)+t(160,84,lb(lang,'acetone'),12)+F.arrow(320,430,54,'K₂Cr₂O₇','H₂SO₄')+C(560,60,'CH₃','OH')+t(700,60,'+ CO₂ + H₂O',15)+t(560,84,lb(lang,'acetic acid'),12)+'</svg>'
def fischer(x,y,rows,top):
 s=t(x,y-6,top,13)+line(x,y,x,y+18*len(rows))
 for i,(l,r,num) in enumerate(rows):
  yy=y+18*(i+1);s+=t(x-26,yy+4,l,12)+line(x-14,yy,x+14,yy)+t(x+26,yy+4,r,12)+t(x-8,yy-4,num,9,'#555')
 return s
def hexring(cx,cy,w=70,h=30,open_=False):
 pts=[(cx-w,cy),(cx-w/2,cy-h),(cx+w/2,cy-h),(cx+w,cy),(cx+w/2,cy+h),(cx-w/2,cy+h)]
 if open_:
  q=[pts[2],pts[3],pts[4],pts[5],pts[0],pts[1]]
  return '<polyline points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in q)+'" fill="none" stroke="#222" stroke-width="2"/>',pts
 return '<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)+'" fill="none" stroke="#222" stroke-width="2"/>',pts
def glucose(lang):
 s=F.start(220)+fischer(90,40,[('H','OH','2'),('HO','H','3'),('H','OH','4'),('H','OH','5')],'H—C=O')+t(90,40+18*5+16,'CH₂OH',12)+t(170,110,'=',20)
 r,p=hexring(330,110,open_=True);s+=r+t(p[2][0]+20,p[2][1]-6,'O═C—H',12)+t(330,70,'HOCH₂',12)+t(330,190,lb(lang,'Open form'),12)
 s+=F.eq(440,500,110)+t(470,96,'[H⁺]',11)
 r,p=hexring(640,110);s+=r+t(p[2][0],p[2][1]-8,'O',13)+t(p[3][0]+16,p[3][1]+4,'OH',12)+t(p[0][0]-18,p[0][1]+4,'HO',12)+t(640,64,'HOCH₂',12)+t(640,190,lb(lang,'Closed form'),12)
 return s+'</svg>'
def fructose(lang,kind):
 s=F.start(220)+fischer(90,40,[('','O','2'),('HO','H','3'),('H','OH','4'),('H','OH','5')],'¹CH₂OH')+t(90,40+18*5+16,'CH₂OH',12)+t(90,200,lb(lang,'D-Fructose'),12)+t(170,110,'=',20)
 if kind=='furanose':
  r=[(300,110),(340,80),(400,90),(420,130),(360,150)];s+='<polyline points="'+' '.join(f'{a},{b}' for a,b in r)+'" fill="none" stroke="#222" stroke-width="2"/>'+t(430,76,'O',13)+t(460,92,'CH₂OH',12)+t(320,62,'HOCH₂',12)+F.eq(500,560,110)+t(530,96,'[H⁺]',11)
  p=[(620,110),(670,80),(720,110),(705,150),(635,150)];s+='<polygon points="'+' '.join(f'{a},{b}' for a,b in p)+'" fill="none" stroke="#222" stroke-width="2"/>'+t(670,74,'O',13)+t(745,106,'OH',12)+t(745,150,'CH₂OH',12)+t(600,80,'HOCH₂',12)+t(670,200,lb(lang,'A furanose ring'),12)
 else:
  r,p=hexring(330,110,open_=True);s+=r+t(330,72,'H',12)+t(p[3][0]+30,p[3][1]+4,'C(=O)CH₂OH',11)+F.eq(470,530,110)+t(500,96,'[H⁺]',11)
  r,p=hexring(660,110);s+=r+t(p[2][0],p[2][1]-8,'O',13)+t(p[3][0]+16,p[3][1]-6,'OH',12)+t(p[3][0]+30,p[3][1]+16,'CH₂OH',12)+t(p[0][0]-18,p[0][1]+4,'HO',12)+t(660,200,lb(lang,'A pyranose ring'),12)
 return s+'</svg>'

visual('chem12-p125-tollens-fehling',eqs)
add('ii. Fehling’s solution test','ii. فہلنگ محلول ٹیسٹ','ii. د فهلینګ محلول ازموینه','heading')
add('Fehling’s solution is alkaline solution of cupric ions complexed with tartarate ion. When Fehling solution is added to an aldehyde and gently heated, the aldehyde is oxidized to corresponding carboxylate and the cupric ion present in Fehling’s solution is reduced to cuprous oxide (Cu₂O), which forms red precipitate. The formation of red precipitate indicates the presence of aldehyde because ketones do not give this test.',
 'فہلنگ محلول ٹارٹریٹ آئن کے ساتھ کمپلیکس شدہ کیوپرک آئنوں کا القلی محلول ہے۔ جب فہلنگ محلول کو الڈیہائیڈ میں ملا کر ہلکا گرم کیا جائے تو الڈیہائیڈ متعلقہ کاربوکسیلیٹ میں تکسید ہو جاتا ہے اور فہلنگ محلول میں موجود کیوپرک آئن کی تخفیف کیوپرس آکسائیڈ (Cu₂O) میں ہوتی ہے، جو سرخ رسوب بناتا ہے۔ سرخ رسوب کا بننا الڈیہائیڈ کی موجودگی ظاہر کرتا ہے کیونکہ کیٹونز یہ ٹیسٹ نہیں دیتے۔',
 'د فهلینګ محلول له ټارټرېټ ایون سره کمپلېکس شویو کیوپریک ایونونو القلي محلول دی. کله چې د فهلینګ محلول الدیهاید ته ورزیات او ورو تود شي، الدیهاید اړوند کاربوکسیلېټ ته اکسیډایز کېږي او په فهلینګ محلول کې شته کیوپریک ایون کیوپرس اکساید (Cu₂O) ته ارجاع کېږي، چې سور رسوب جوړوي. د سور رسوب جوړېدل د الدیهاید شتون ښيي ځکه کیټونونه دا ازموینه نه ورکوي.')
add('This test is widely used for the estimation of glucose in blood and urine.','یہ ٹیسٹ خون اور پیشاب میں گلوکوز کی مقدار معلوم کرنے کے لیے وسیع پیمانے پر استعمال ہوتا ہے۔','دا ازموینه په وینه او ادرار کې د ګلوکوز د اندازه کولو لپاره په پراخه کچه کارېږي.')
add('iii. Benedict’s solution test','iii. بینیڈکٹ محلول ٹیسٹ','iii. د بېنېډکټ محلول ازموینه','heading')
add('Benedict’s solution is an alkaline solution of cupric ions complexed with citrate ion. It react in the same way as Fehling’s solution.','بینیڈکٹ محلول سٹریٹ آئن کے ساتھ کمپلیکس شدہ کیوپرک آئنوں کا القلی محلول ہے۔ یہ فہلنگ محلول کی طرح تعامل کرتا ہے۔','د بېنېډکټ محلول له سیټرېټ ایون سره کمپلېکس شویو کیوپریک ایونونو القلي محلول دی. د فهلینګ محلول په څېر تعامل کوي.')
add('b. Oxidations of Ketones','b. کیٹونز کی تکسید','b. د کیټونونو اکسیډېشن','heading')
add('In aldehydes, oxidation involve hydrogen that is attached to carbonyl carbon but in case of ketones no such hydrogen exists. Ketones having α-hydrogen can be oxidized by breaking of carbon-carbon sigma bond, using strong oxidizing agents like acidified dichromate or permanganate.','الڈیہائیڈز میں تکسید میں وہ ہائیڈروجن شامل ہوتا ہے جو کاربونل کاربن سے جڑا ہو، لیکن کیٹونز میں ایسا کوئی ہائیڈروجن نہیں ہوتا۔ α-ہائیڈروجن رکھنے والے کیٹونز کی تکسید تیزابی ڈائی کرومیٹ یا پرمینگنیٹ جیسے طاقتور تکسیدی عاملوں سے کاربن–کاربن سگما بند توڑ کر کی جا سکتی ہے۔','په الدیهایډونو کې اکسیډېشن هغه هایدروجن رانغاړي چې له کاربونیل کاربن سره تړلی دی، خو په کیټونونو کې داسې هایدروجن نشته. د α-هایدروجن لرونکي کیټونونه د قوي اکسیډایز کوونکو عاملونو لکه اسیدي ډای کرومېټ یا پرمنګنېټ په کارولو د کاربن–کاربن سیګما تړون په ماتولو اکسیډایز کېدای شي.')
visual('chem12-p125-ketone-oxidation',ketone)
add('Society, Technology And Science','معاشرہ، ٹیکنالوجی اور سائنس','ټولنه، ټکنالوژي او ساینس','heading')
add('Carbohydrates are an important class of naturally occurring substances found in both plant and animal matter. Carbohydrates containing an aldehydic carbonyl are simply called as aldoses, while those containing ketonic carbonyl are known as ketoses. For example, glucose is a six-carbon aldehyde sugar, whereas fructose, the sugar that occurs widely in fruit, is a six-carbon ketone sugar. Glucose, having both alcohol and aldehyde functional groups and having a reasonably long and flexible backbone, and can react with itself to form a six-member ring structure, called pyranose ring, which is actually a hemiacetal as shown below. Indeed, only a small percentage of the glucose molecules are in the open-chain form in aqueous solution.',
 'کاربوہائیڈریٹس قدرتی طور پر پائے جانے والے مادوں کی ایک اہم جماعت ہیں جو پودوں اور جانوروں دونوں میں ملتے ہیں۔ الڈیہائیڈی کاربونل والے کاربوہائیڈریٹس کو سادہ طور پر الڈوزز کہتے ہیں، جبکہ کیٹونی کاربونل والے کیٹوزز کہلاتے ہیں۔ مثلاً گلوکوز چھ کاربن والی الڈیہائیڈ شکر ہے، جبکہ فرکٹوز، جو پھلوں میں وسیع پیمانے پر پائی جاتی ہے، چھ کاربن والی کیٹون شکر ہے۔ گلوکوز میں الکوحل اور الڈیہائیڈ دونوں فعلی گروپ ہیں اور اس کا ڈھانچہ کافی لمبا اور لچکدار ہے، اس لیے یہ خود سے تعامل کر کے چھ رکنی حلقہ ساخت بنا سکتا ہے جسے پائرانوز حلقہ کہتے ہیں، جو دراصل ہیمی ایسیٹل ہے جیسا کہ نیچے دکھایا گیا ہے۔ درحقیقت آبی محلول میں گلوکوز کے سالمات کا صرف ایک چھوٹا فیصد کھلی زنجیر کی صورت میں ہوتا ہے۔',
 'کاربوهایدریټونه په طبیعي ډول موندل کېدونکو موادو یو مهم ټولګی دی چې په نباتي او حیواني موادو دواړو کې موندل کېږي. هغه کاربوهایدریټونه چې الدیهایدي کاربونیل لري په ساده ډول الډوزونه بلل کېږي، او هغه چې کیټوني کاربونیل لري کیټوزونه بلل کېږي. د بېلګې په توګه ګلوکوز شپږ کاربنه الدیهایدي شکره ده، په داسې حال کې چې فرکټوز، چې په مېوو کې په پراخه کچه موندل کېږي، شپږ کاربنه کیټوني شکره ده. ګلوکوز د الکول او الدیهاید دواړه فعال ګروپونه لري او نسبتاً اوږد او انعطاف منونکی ډډ لري، نو کولی شي له ځان سره تعامل وکړي او شپږ غړیز کړیز جوړښت جوړ کړي چې پیرانوز کړۍ بلل کېږي، چې په حقیقت کې هیمي اسیټال دی لکه څنګه چې لاندې ښودل شوی. په حقیقت کې په اوبلن محلول کې د ګلوکوز د مالیکولونو یوازې لږه سلنه د خلاص ځنځیر په بڼه وي.')
visual('chem12-p125-glucose-ring',glucose)
add('Fructose can also cyclize to form a five-member ring structure, called furanose ring, which is also a hemiacetal. The five-member rings formed when the –OH group on C-5 reacts with the carbonyl group on C-2.','فرکٹوز بھی حلقہ بنا کر پانچ رکنی حلقہ ساخت بنا سکتا ہے جسے فیورانوز حلقہ کہتے ہیں، جو بھی ہیمی ایسیٹل ہے۔ پانچ رکنی حلقے اس وقت بنتے ہیں جب C-5 پر –OH گروپ C-2 کے کاربونل گروپ سے تعامل کرتا ہے۔','فرکټوز هم کړیز کېدای شي او پنځه غړیز کړیز جوړښت جوړوي چې فورانوز کړۍ بلل کېږي، چې دا هم هیمي اسیټال دی. پنځه غړیزې کړۍ هغه وخت جوړېږي چې پر C-5 د –OH ګروپ د C-2 له کاربونیل ګروپ سره تعامل وکړي.')
visual('chem12-p125-fructose-furanose',lambda l:fructose(l,'furanose'))
add('D-Fructose can also cyclize to give pyranose forms that result from the reaction involving the hydroxyl group at C-6.','D-فرکٹوز C-6 کے ہائیڈروآکسل گروپ پر مشتمل تعامل سے پائرانوز صورتیں بھی بنا سکتا ہے۔','D-فرکټوز هم کړیز کېدای شي او پیرانوز بڼې ورکوي چې د C-6 د هایدروکسیل ګروپ له تعامل څخه پایله کېږي.')
visual('chem12-p125-fructose-pyranose',lambda l:fructose(l,'pyranose'))
record=section('19.9','Fehling’s and Benedict’s tests, oxidation of ketones, sugar ring forms','فہلنگ اور بینیڈکٹ ٹیسٹ، کیٹونز کی تکسید، شکر کی حلقہ صورتیں','د فهلینګ او بېنېډکټ ازموینې، د کیټونونو اکسیډېشن، د شکرو کړیزې بڼې',paras,layout,blocks,'242–243')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':125,'printedPages':[242,243]}]
record['sourceContinuesOnPdfPage']=126
issues=[{'id':'chem12-p243-sugar-figures','printedPage':243,'description':'Glucose/fructose Fischer and Haworth ring figures reconstructed as simplified coded schematics (ring skeletons with principal OH/CH₂OH labels); full stereo-detail of every substituent not reproduced. Printed "tartarate" retained.'}]
trim=[{'id':'19.10','startsAt':'Key Points'}]
if __name__=='__main__':save(125,[record],trim=trim,issues=issues,chapter_number=19)
