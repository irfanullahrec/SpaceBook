"""PDF98 printed188–189: Society, Technology and Science (chlorophyll and hemoglobin); Key Points of Unit 17."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow98');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Chlorophyll':('کلوروفل','کلوروفیل'),'Hemoglobin':('ہیموگلوبن','هیموګلوبین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def porphyrin(cx,cy,metal,labels):
 """labels: per pyrrole k (angles 135,45,-45,-135) → (vertical-side label, horizontal-side label)."""
 s='';rings=[]
 for k,ang in enumerate((135,45,-45,-135)):
  a=math.radians(ang);pcx,pcy=cx+66*math.cos(a),cy-66*math.sin(a);inward=ang+180
  pts=[(pcx+24*math.cos(math.radians(inward+72*j)),pcy-24*math.sin(math.radians(inward+72*j))) for j in range(5)]
  rings.append(pts);s+='<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'
  b1,b2=pts[2],pts[3];vert,hor=(b1,b2) if abs(b1[0]-pcx)<abs(b2[0]-pcx) else (b2,b1)
  for (bx,by),lab in ((vert,labels[k][0]),(hor,labels[k][1])):
   dx,dy=bx-pcx,by-pcy;d=math.hypot(dx,dy);ex,ey=bx+dx/d*16,by+dy/d*16;s+=line(bx,by,ex,ey,1.5)
   s+=t(ex+dx/d*(10+3.5*len(lab)) ,ey+dy/d*12+5,lab,12)
 for k in range(4):
  A,B=rings[k],rings[(k+1)%4];ca=min((A[1],A[4]),key=lambda p:math.hypot(p[0]-B[0][0],p[1]-B[0][1]));cb=min((B[1],B[4]),key=lambda p:math.hypot(p[0]-A[0][0],p[1]-A[0][1]))
  mx,my=(ca[0]+cb[0])/2,(ca[1]+cb[1])/2;dx,dy=mx-cx,my-cy;d=math.hypot(dx,dy);mx,my=mx+dx/d*12,my+dy/d*12
  s+=line(ca[0],ca[1],mx,my)+line(mx,my,cb[0],cb[1])
 for pts in rings:
  nx,ny=pts[0];s+=f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="8" fill="white"/>'+t(nx,ny+5,'N',13)+line(nx+(cx-nx)*.25,ny+(cy-ny)*.25,cx+(nx-cx)*.4,cy+(ny-cy)*.4,1.5,'#222','stroke-dasharray="3 3"')
 return s+f'<circle cx="{cx}" cy="{cy}" r="13" fill="white"/>'+t(cx,cy+6,metal,15)
def pigments(lang):
 s=F.start(330)+t(200,24,lb(lang,'Chlorophyll'),15)+t(640,24,lb(lang,'Hemoglobin'),15)+line(420,30,420,320,6,'#999')
 s+=porphyrin(200,170,'Mg',[('CHO','H₃C'),('CH₃','CH₂CH₃'),('ring E','CH₃'),('CH₂CH₂CO₂CH₃','H₃C')])
 s+=porphyrin(640,170,'Fe',[('CH=CH₂','H₃C'),('CH₃','CH=CH₂'),('CH₂CH₂COOH','CH₃'),('CH₂CH₂COOH','H₃C')])
 return s+'</svg>'

add('Society, Technology And Science','معاشرہ، ٹیکنالوجی اور سائنس','ټولنه، ټکنالوژي او ساینس','heading')
add('Chlorophyll is the substance which makes plants green. The chlorophyll molecule has the unique capacity to convert the energy of the sun into chemical energy (through photosynthesis), which the plant uses to make carbohydrates from carbon dioxide and water. Hemoglobin is the substance in human blood which carries oxygen from the lungs to the other tissues and cells of the body.',
 'کلوروفل وہ مادہ ہے جو پودوں کو سبز بناتا ہے۔ کلوروفل کے سالمے میں سورج کی توانائی کو (ضیائی تالیف کے ذریعے) کیمیائی توانائی میں بدلنے کی منفرد صلاحیت ہے، جسے پودا کاربن ڈائی آکسائیڈ اور پانی سے کاربوہائیڈریٹس بنانے میں استعمال کرتا ہے۔ ہیموگلوبن انسانی خون میں وہ مادہ ہے جو پھیپھڑوں سے آکسیجن جسم کے دوسرے بافتوں اور خلیوں تک لے جاتا ہے۔',
 'کلوروفیل هغه ماده ده چې نباتات شنه کوي. د کلوروفیل مالیکول ځانګړې وړتیا لري چې د لمر انرژي (د فوتوسنتیز له لارې) په کیمیاوي انرژۍ بدله کړي، چې نبات یې له کاربن ډای اکساید او اوبو څخه د کاربوهایدریټونو د جوړولو لپاره کاروي. هیموګلوبین د انسان په وینه کې هغه ماده ده چې له سږو څخه اکسیجن د بدن نورو نسجونو او حجرو ته وړي.')
add('Hemoglobin and Chlorophyll have similar structures composed of four elements; carbon, hydrogen, oxygen and nitrogen. The main difference is that hemoglobin is built around iron (Fe), whereas chlorophyll is built around magnesium (Mg). The primary function for hemoglobin is to transport oxygen from the lungs to other parts of the body.',
 'ہیموگلوبن اور کلوروفل کی ساختیں ملتی جلتی ہیں جو چار عناصر یعنی کاربن، ہائیڈروجن، آکسیجن اور نائٹروجن پر مشتمل ہیں۔ بنیادی فرق یہ ہے کہ ہیموگلوبن لوہے (Fe) کے گرد بنا ہے جبکہ کلوروفل میگنیشیم (Mg) کے گرد بنا ہے۔ ہیموگلوبن کا بنیادی کام پھیپھڑوں سے آکسیجن جسم کے دوسرے حصوں تک پہنچانا ہے۔',
 'هیموګلوبین او کلوروفیل ورته جوړښتونه لري چې له څلورو عناصرو یعنې کاربن، هایدروجن، اکسیجن او نایتروجن څخه جوړ دي. اصلي توپیر دا دی چې هیموګلوبین د اوسپنې (Fe) شاوخوا جوړ دی، په داسې حال کې چې کلوروفیل د مګنیزیم (Mg) شاوخوا جوړ دی. د هیموګلوبین اصلي دنده له سږو څخه د بدن نورو برخو ته د اکسیجن لېږدول دي.')
visual('chem12-p98-chlorophyll-hemoglobin',pigments)
add('In sickle cell anemia, the abnormal hemoglobin (Hemoglobin-S) sticks together when it gives up its oxygen to the tissues. These clumps cause red blood cells to become stiff and shaped like a sickle.',
 'سکل سیل انیمیا میں غیر معمولی ہیموگلوبن (ہیموگلوبن-S) بافتوں کو آکسیجن دینے پر آپس میں چپک جاتا ہے۔ یہ گچھے سرخ خونی خلیوں کو سخت اور درانتی جیسا بنا دیتے ہیں۔',
 'د سکل سېل انیمیا په ناروغۍ کې غیر نورمال هیموګلوبین (هیموګلوبین-S) کله چې نسجونو ته خپل اکسیجن ورکوي، یو له بل سره نښلي. دا ټوټې سرې کرویات سخت او د لور په څېر کوي.')
add('Chlorophyll helps do the job of hemoglobin when ingested. Promote the health of circulation, cleanse the body, increase the number of red blood cells and therefore increase oxygen throughout the body, in other words, Chlorophyll helps build hemoglobin. This is exactly what our sickle cell babies and others need, to build hemoglobin.',
 'کھائے جانے پر کلوروفل ہیموگلوبن کا کام کرنے میں مدد دیتا ہے۔ یہ دورانِ خون کی صحت کو فروغ دیتا ہے، جسم کو صاف کرتا ہے، سرخ خونی خلیوں کی تعداد بڑھاتا ہے اور یوں پورے جسم میں آکسیجن بڑھاتا ہے؛ دوسرے الفاظ میں کلوروفل ہیموگلوبن بنانے میں مدد دیتا ہے۔ ہمارے سکل سیل والے بچوں اور دوسروں کو ہیموگلوبن بنانے کے لیے بالکل یہی چاہیے۔',
 'کله چې وخوړل شي، کلوروفیل د هیموګلوبین په دنده کې مرسته کوي. د وینې د جریان روغتیا ښه کوي، بدن پاکوي، د سرو کروياتو شمېر زیاتوي او په دې توګه په ټول بدن کې اکسیجن زیاتوي؛ په بله وینا، کلوروفیل د هیموګلوبین په جوړولو کې مرسته کوي. زموږ سکل سېل لرونکي ماشومان او نور د هیموګلوبین د جوړولو لپاره همدې ته اړتیا لري.')
add('Key Points','اہم نکات','مهم ټکي','heading')
pts=[('General formula of alkyl halide is R–X.','الکائل ہیلائیڈ کا عمومی فارمولا R–X ہے۔','د الکایل هالایډ عمومي فورمول R–X دی.'),
 ('The molecule which undergoes substitution reaction is called ‘substrate’.','جو سالمہ تبادلے کا تعامل کرے اسے ’سبسٹریٹ‘ کہتے ہیں۔','هغه مالیکول چې د بدلون تعامل کوي ’سبسټرېټ‘ بلل کېږي.'),
 ('The group or species which leaves the substrate is called “leaving group”.','جو گروپ یا نوع سبسٹریٹ کو چھوڑے اسے ”خارج ہونے والا گروپ“ کہتے ہیں۔','هغه ګروپ یا ډول چې سبسټرېټ پرېږدي ”وتونکی ګروپ“ بلل کېږي.'),
 ('SN1 mechanism is defined as that nucleophilic substitution reaction in which only one molecule is involved in rate determing or slow step.','SN1 طریق کار وہ نیوکلیوفائلی تبادلے کا تعامل ہے جس کے شرح متعین کرنے والے یا سست مرحلے میں صرف ایک سالمہ شامل ہو۔','د SN1 میکانیزم هغه نیوکلیوفایلي بدلون تعامل دی چې د سرعت ټاکونکي یا ورو پړاو کې یې یوازې یو مالیکول ښکېل وي.'),
 ('Those nucleophilic substitution reactions in which two species are involved in the rate determing or slow step are called SN2 reactions.','وہ نیوکلیوفائلی تبادلے کے تعاملات جن کے شرح متعین کرنے والے یا سست مرحلے میں دو انواع شامل ہوں، SN2 تعاملات کہلاتے ہیں۔','هغه نیوکلیوفایلي بدلون تعاملونه چې د سرعت ټاکونکي یا ورو پړاو کې یې دوه ډولونه ښکېل وي، SN2 تعاملونه بلل کېږي.'),
 ('The primary alkyl halides undergo SN2 mechanism while tertiary alkyl halides undergo SN1 mechanism.','ابتدائی الکائل ہیلائیڈز SN2 طریق کار جبکہ ثالثی الکائل ہیلائیڈز SN1 طریق کار اپناتے ہیں۔','لومړني الکایل هالایډونه د SN2 میکانیزم او درېیمي الکایل هالایډونه د SN1 میکانیزم تعقیبوي.'),
 ('In polar solvent secondary alkyl halides follow SN1-mechanism while in non-polar solvents follow SN2-mechanism.','قطبی محلل میں ثانوی الکائل ہیلائیڈز SN1-طریق کار جبکہ غیر قطبی محللات میں SN2-طریق کار اپناتے ہیں۔','په قطبي محلل کې دویمي الکایل هالایډونه د SN1-میکانیزم او په غیر قطبي محللونو کې د SN2-میکانیزم تعقیبوي.'),
 ('During elimination reaction two strong sigma bonds are broken and a new weaker pi bond is formed.','اخراجی تعامل کے دوران دو مضبوط سگما بند ٹوٹتے ہیں اور ایک نیا کمزور پائی بند بنتا ہے۔','د ایستلو تعامل پر مهال دوه قوي سیګما تړونونه ماتېږي او یو نوی کمزوری پای تړون جوړېږي.'),
 ('E1 stands for unimolecular elimination while E2 stands for bimolecular elimination reaction.','E1 کا مطلب یک سالمی اخراج جبکہ E2 کا مطلب دو سالمی اخراجی تعامل ہے۔','E1 د یو مالیکولي ایستنې او E2 د دوه مالیکولي ایستلو تعامل لپاره دی.'),
 ('Those organic compounds which contain at least one carbon—metal bond in their structure are known as organometallic compounds.','وہ نامیاتی مرکبات جن کی ساخت میں کم از کم ایک کاربن—دھات بند ہو، آرگینو میٹلک مرکبات کہلاتے ہیں۔','هغه عضوي مرکبات چې په جوړښت کې یې لږ تر لږه یو کاربن—فلز تړون وي، عضوي فلزي مرکبات بلل کېږي.'),
 ('Amines are derivatives of NH₃ in which one or more hydrogen atom have been replaced by one or more similar or different alkyl group.','امائنز NH₃ کے وہ مشتقات ہیں جن میں ایک یا زیادہ ہائیڈروجن ایٹم ایک یا زیادہ یکساں یا مختلف الکائل گروپوں سے بدل دیے گئے ہوں۔','امینونه د NH₃ هغه مشتقات دي چې پکې یو یا ډېر هایدروجني اټومونه په یوه یا ډېرو ورته یا بېلو الکایل ګروپونو بدل شوي وي.'),
 ('Due to presence of lone pair of electrons on nitrogen atoms (R–NH₂) amines are basic in nature.','نائٹروجن ایٹموں (R–NH₂) پر الیکٹرانوں کے تنہا جوڑے کی موجودگی کی وجہ سے امائنز فطرتاً اساسی ہیں۔','پر نایتروجني اټومونو (R–NH₂) د الکترونونو د یوازینۍ جوړې د شتون له امله امینونه په طبیعت کې قلوي دي.')]
s0=len(paras)
for r in pts:paras.append(pair(*r))
layout.append({'type':'list','indices':list(range(s0,len(paras)))})
record=section('17.14','Society, Technology and Science; Key Points','معاشرہ، ٹیکنالوجی اور سائنس؛ اہم نکات','ټولنه، ټکنالوژي او ساینس؛ مهم ټکي',paras,layout,blocks,'188–189')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':98,'printedPages':[188,189]}]
record['sourceContinuesOnPdfPage']=99
issues=[{'id':'chem12-p188-porphyrins','printedPage':188,'description':'Chlorophyll and hemoglobin skeletal formulas reconstructed as simplified coded porphyrin rings with metal centre and principal substituent labels; Key Point printed "substrate" definition and "rate determing" retained.'}]
trim=[{'id':'17.15','startsAt':'Exercise\nQI. Choose'}]
if __name__=='__main__':save(98,[record],trim=trim,issues=issues,chapter_number=17)
