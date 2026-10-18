"""PDF84 printed160–161: Unit 16 exercise continuation (Q3 3c–5, structure drawing) and Project."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow84');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows):
 start=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':'lines','indices':list(range(start,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
def hexa(cx,cy,r,dbl=(),circle=False,subs=None):
 s=F.ring(cx,cy,r,kek=False,circle=circle,subs=subs)
 pts=[(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
 for i in dbl:
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.76;s+=line(cx+(x1-cx)*k,cy+(y1-cy)*k,cx+(x2-cx)*k,cy+(y2-cy)*k)
 return s
def structures(lang):
 s=F.start(560)
 s+=t(30,40,'(i)',16)+t(200,30,'CH₂—CH₃',17)+line(170,36,170,52)+t(200,72,'CH₃—CH—CH₂—CH₃',17)
 s+=t(450,40,'(ii)',16)+t(640,30,'CH₃—CH—CH₃',17)+line(640,36,640,52)+t(640,72,'CH₃—CH₂—CH₂—CH—CH₂—CH₂—CH₂—CH₃',16)
 s+=t(30,130,'(iii)',16)+t(200,130,'CH₃—CH₂—C—CH₂—CH₂—CH₃',17)+line(154,138,154,156)+line(160,138,160,156)+t(157,174,'CH₂',17)
 s+=t(450,130,'(iv)',16)+t(620,130,'(CH₃CH₂)₂C = CHCH₃',17)
 s+=t(30,230,'(v)',16)+t(220,230,'(CH₃)₃C—C≡C—CH(CH₃)CH₂CH₃',17)
 s+=t(450,230,'(vi)',16)+hexa(560,225,30)
 sq=[(600,210),(630,210),(630,240),(600,240)];s+=line(590,225,600,225)+'<polygon points="'+' '.join(f'{x},{y}' for x,y in sq)+'" fill="none" stroke="#222" stroke-width="2"/>'
 s+=t(30,330,'(vii)',16)+hexa(160,350,30,(0,2,4),subs={0:'NO₂',1:'Cl',2:'NO₂',3:'Br'})
 s+=t(450,330,'(viii)',16)+hexa(620,350,30,(0,2,4),subs={1:'CH₃',2:'OH',5:'HO'})
 s+=t(30,470,'(ix)',16)+hexa(160,490,32,subs={5:'H₃C',1:'C₂H₅',3:'CH₃'})
 s+=t(450,470,'(x)',16)
 H=30*math.sqrt(3)
 for k in range(3):s+=hexa(560+k*H,490,30,(0,2,4) if k==0 else ((1,3,5) if k==1 else (0,2,4)))
 return s+'</svg>'

lines([
 ('(c) Starting from an alkene how would you prepare the following compounds? (i) Vicinal dihalide (ii) Alcohol (iii) Aldehydes and ketones (iv) Epoxide','(c) کسی الکین (دوہرے بند والے) سے شروع کر کے آپ درج ذیل مرکبات کیسے تیار کریں گے؟ (i) وسینل ڈائی ہیلائیڈ (ii) الکوحل (iii) الڈیہائیڈز اور کیٹونز (iv) ایپو آکسائیڈ','(c) له یوه الکین څخه په پیل لاندې مرکبات څنګه جوړوئ؟ (i) وېسینل ډای هالایډ (ii) الکول (iii) الدیهایډونه او کیټونونه (iv) ایپوکساید'),
 ('4. (a) Describe the structure of benzene on the basis of MOT.','4. (a) MOT کی بنیاد پر بینزین کی ساخت بیان کریں۔','4. (a) د MOT پر بنسټ د بنزین جوړښت بیان کړئ.'),
 ('(b) Describe mechanism of electrophilic substitution reaction in benzene.','(b) بینزین میں الیکٹروفائلی تبادلے کے تعامل کا طریق کار بیان کریں۔','(b) په بنزین کې د الکتروفایلي بدلون تعامل میکانیزم بیان کړئ.'),
 ('(c) How would you prepare the following compounds from benzene? (i) Acetophenone (ii) Toluene (iii) Nitrobenzene (iv) Benzenesulphonic acid (v) Chlorobenzene (vi) Cyclohexane','(c) بینزین سے آپ درج ذیل مرکبات کیسے تیار کریں گے؟ (i) ایسیٹو فینون (ii) ٹولوئین (iii) نائٹرو بینزین (iv) بینزین سلفونک ایسڈ (v) کلورو بینزین (vi) سائیکلوہیکسین','(c) له بنزین څخه لاندې مرکبات څنګه جوړوئ؟ (i) اسیټوفینون (ii) تولوین (iii) نایټروبنزین (iv) بنزین سلفونیک اسید (v) کلوروبنزین (vi) سایکلوهېکسان'),
 ('5. (a) Explain the directing and activitating effect in mono substituted benzene derivatives.','5. (a) یک متبادل بینزین مشتقات میں سمت دینے اور فعال کرنے کا اثر واضح کریں۔','5. (a) په یو بدیلي بنزیني مشتقاتو کې د لارښوونې او فعالولو اغېز روښانه کړئ.'),
 ('(b) Write the systematic names for the following organic compounds.','(b) درج ذیل نامیاتی مرکبات کے نظامی نام لکھیں۔','(b) د لاندې عضوي مرکباتو سیستماتیک نومونه ولیکئ.')])
visual('chem12-p84-naming-structures',structures)
add('(a) Draw the structural formula of the following organic compounds.','(a) درج ذیل نامیاتی مرکبات کے ساختی فارمولے بنائیں۔','(a) د لاندې عضوي مرکباتو جوړښتي فورمولونه رسم کړئ.','heading')
lines([
 ('i. 3–ethyl–4–methyloctane   ii. 4–isopropyldecane','i. 3–ایتھائل–4–میتھائل اوکٹین   ii. 4–آئسوپروپائل ڈیکین','i. 3–ایتیل–4–میتایل اوکټان   ii. 4–ایزوپروپیل ډیکان'),
 ('iii. sec-butylcycloheptane   iv. 2,3–dimethyl–4–propylnonane','iii. sec-بیوٹائل سائیکلوہیپٹین   iv. 2،3–ڈائی میتھائل–4–پروپائل نونین','iii. sec-بیوټیل سایکلوهېپټان   iv. 2،3–ډای میتایل–4–پروپیل نونان'),
 ('iv. 2,4,4–trimethylhex–2–ene   v. cis–hex–3–ene','iv. 2،4،4–ٹرائی میتھائل ہیکس–2–این   v. cis–ہیکس–3–این','iv. 2،4،4–ټرای میتایل هېکس–2–ین   v. cis–هېکس–3–ین'),
 ('vi. phenanthrene   vii. hex-2-yne','vi. فینانتھرین   vii. ہیکس-2-ائن','vi. فینانترین   vii. هېکس-2-این'),
 ('viii. 1,2–dimethyl–4–propylbenzene   ix. cyclopropylbenzene','viii. 1،2–ڈائی میتھائل–4–پروپائل بینزین   ix. سائیکلوپروپائل بینزین','viii. 1،2–ډای میتایل–4–پروپیل بنزین   ix. سایکلوپروپیل بنزین')])
add('Project','منصوبہ','پروژه','heading')
add('Set up one small test tube in a test tube rack in the hood. Add 10 mg of a solid or 10 mL of a liquid organic compound containing carbon-carbon double bond. Add 1-3mL of distilled water (if compound is water soluble) or carbon tetrachloride (if compound is water insoluble), shake the mixtures for 2 minutes. Add bromine water reagent (5mL of bromine dissolved in 100 mL of water) for water soluble compound, or bromine in CCl₄ (5mL of bromine dissolved in 100mL of CCl₄) for water insoluble compound, drop by drop. Do not add an excess of the bromine reagent. The bromine reagent is brown or yellow-brown in color. Observe the dissipation of the brownish color of bromine.',
 'ہُڈ میں ٹیسٹ ٹیوب ریک میں ایک چھوٹی ٹیسٹ ٹیوب رکھیں۔ کاربن–کاربن دوہرا بند رکھنے والے ٹھوس نامیاتی مرکب کے 10 mg یا مائع کے 10 mL ڈالیں۔ 1-3mL کشید شدہ پانی (اگر مرکب پانی میں حل پذیر ہو) یا کاربن ٹیٹرا کلورائیڈ (اگر مرکب پانی میں ناحل پذیر ہو) شامل کریں اور آمیزوں کو 2 منٹ ہلائیں۔ پانی میں حل پذیر مرکب کے لیے برومین واٹر عامل (100 mL پانی میں 5mL برومین) یا پانی میں ناحل پذیر مرکب کے لیے CCl₄ میں برومین (100mL CCl₄ میں 5mL برومین) قطرہ قطرہ شامل کریں۔ برومین عامل زیادہ مقدار میں شامل نہ کریں۔ برومین عامل بھورے یا زرد بھورے رنگ کا ہوتا ہے۔ برومین کے بھورے رنگ کے غائب ہونے کا مشاہدہ کریں۔',
 'په هوډ کې د ازموینې د ټیوبونو په رف کې یو کوچنی ټیسټ ټیوب کېږدئ. د کاربن–کاربن دوه ګوني تړون لرونکي جامد عضوي مرکب 10 mg یا د مایع 10 mL ورزیات کړئ. 1-3mL مقطرې اوبه (که مرکب په اوبو کې حلېدونکی وي) یا کاربن ټیټراکلوراید (که مرکب په اوبو کې نه حلېږي) ورزیاتې کړئ او ګډولې 2 دقیقې وښوروئ. د اوبو کې د حلېدونکي مرکب لپاره د برومین اوبو عامل (په 100 mL اوبو کې 5mL برومین) یا د نه حلېدونکي مرکب لپاره په CCl₄ کې برومین (په 100mL CCl₄ کې 5mL برومین) څاڅکی څاڅکی ورزیات کړئ. د برومین عامل ډېر مه ورزیاتوئ. د برومین عامل نسواري یا ژېړ نسواري رنګ لري. د برومین د نسواري رنګ له منځه تلل وګورئ.')
record=section('16.31','Unit 16 exercise continued and Project','یونٹ 16 مشق کا تسلسل اور منصوبہ','د 16 واحد تمرین دوام او پروژه',paras,layout,blocks,'160–161')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':84,'printedPages':[160,161]}]
record['sourceChapterNumber']=16;record['insertBefore']='16.exercise.solved'
issues=[{'id':'chem12-p160-printed-numbering','printedPage':160,'description':'Printed "activitating", duplicate item number "iv." in the structure-drawing list and unnumbered "(a)" question on printed 161 retained as printed; Q5(b) structures (i)–(x) reconstructed as coded SVG.'}]
if __name__=='__main__':save(84,[record],issues=issues,chapter_number=16)
