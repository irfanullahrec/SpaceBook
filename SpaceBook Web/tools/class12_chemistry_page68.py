"""PDF68 printed128–129: optical isomerism, chiral centres, chirality and optical activity."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=20,color='#17212b',anchor='middle'):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
def line(x,y,a,b,w=2,c='#222',extra=''):return f'<path d="M{x} {y}L{a} {b}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
def start(h,w=850):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="arrow68" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#c0262d"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
L={'2-hydroxypropanoic acid':('2-ہائیڈروآکسی پروپانوئک ایسڈ','2-هایدروکسي پروپانویک اسید'),'(Lactic acid)':('(لیکٹک ایسڈ)','(لاکټیک اسید)'),
   'mirror':('آئینہ','هینداره'),'light source':('روشنی کا منبع','د رڼا سرچینه'),'waves vibrating in':('تمام سمتوں میں','په ټولو لورو کې'),
   'all directions':('ارتعاش کرتی لہریں','لړزېدونکې څپې'),'polarizing filter':('پولرائزنگ فلٹر','پولرایزوونکی فلټر'),
   'waves vibrating in a':('ایک ہی مستوی میں','په یوه سطحه کې'),'single plane':('ارتعاش کرتی لہریں','لړزېدونکې څپې'),
   'plane-polarized light':('مستوی پولرائزڈ روشنی','سطحي پولرایز شوې رڼا')}
def lb(lang,v):return v if lang=='en' else L[v][0 if lang=='ur' else 1]

def lactic(lang):
 s=start(150)+t(425,30,'OH')+line(425,36,425,56)+t(425,78,'CH₃ — C* — COOH',22)+line(425,86,425,104)+t(425,124,'H')
 return s+t(425,146,lb(lang,'2-hydroxypropanoic acid')+' '+lb(lang,'(Lactic acid)'),15)+'</svg>'

def mirror(lang):
 s=start(210)
 def tet(cx,flip):
  out=''
  pts=[(cx,45,'1','#4caf50'),(cx-62*flip,140,'2','#29b6f6'),(cx+12*flip,150,'3','#e91e63'),(cx+40*flip,118,'4','#fdd835')]
  for x,y,n,c in pts:out+=line(cx,100,x,y,6,'#555')
  out+=f'<circle cx="{cx}" cy="100" r="24" fill="#263238"/>'+t(cx,107,'C*',17,'white')
  for x,y,n,c in pts:out+=f'<circle cx="{x}" cy="{y}" r="15" fill="{c}" stroke="#333"/>'+t(x,y+6,n,15)
  return out
 s+=tet(120,1)+line(225,30,225,185,5,'#90a4ae')+t(225,22,lb(lang,'mirror'),14)+tet(330,-1)
 s+=line(640,25,640,195,2,'#555','stroke-dasharray="3 5"')+t(640,18,lb(lang,'mirror'),14)
 s+=t(555,62,'COOH',18)+line(555,68,555,88)+t(555,108,'H₃C — C ··· H',18)+line(555,116,555,134)+t(555,152,'OH',18)
 s+=t(725,62,'HOOC',18)+line(725,68,725,88)+t(725,108,'H ··· C — CH₃',18)+line(725,116,725,134)+t(725,152,'HO',18)
 return s+'</svg>'

def polar(lang):
 s=start(175)
 s+=f'<circle cx="80" cy="85" r="26" fill="#ef9a9a" stroke="#b71c1c"/>'+line(80,111,80,135,8,'#455a64')+line(50,140,110,140,6,'#455a64')
 s+=line(112,85,200,85,2,'#c0262d','marker-end="url(#arrow68)"')
 s+=f'<circle cx="235" cy="85" r="24" fill="#ffcdd2" stroke="#b71c1c"/>'
 for a,b,c,d in ((235,61,235,109),(211,85,259,85),(218,68,252,102),(218,102,252,68)):s+=line(a,b,c,d,2,'#b71c1c')
 s+=line(262,85,370,85,2,'#c0262d','marker-end="url(#arrow68)"')
 s+='<rect x="380" y="35" width="120" height="100" fill="#eceff1" stroke="#37474f"/>'
 for x in range(392,500,16):s+=line(x,42,x,128,4,'#37474f')
 s+=line(505,85,600,85,2,'#c0262d','marker-end="url(#arrow68)"')
 s+='<ellipse cx="625" cy="85" rx="12" ry="26" fill="#ef5350" stroke="#b71c1c"/>'+line(625,59,625,111,2,'#7f0000')
 s+=t(235,20,lb(lang,'waves vibrating in'),14,'#00838f')+t(235,38,lb(lang,'all directions'),14,'#00838f')
 s+=t(640,20,lb(lang,'waves vibrating in a'),14,'#00838f')+t(640,38,lb(lang,'single plane'),14,'#00838f')
 s+=t(80,165,lb(lang,'light source'),15)+t(440,165,lb(lang,'polarizing filter'),15)+t(660,165,lb(lang,'plane-polarized light'),15)
 return s+'</svg>'

add('16.6.2.2 Optical Isomerism','16.6.2.2 نوری آئسومرزم','16.6.2.2 نوري ایزومېریزم','heading')
add('Optical isomerism is a type of isomerism in which the isomers have different interaction towards plane polarized light. If a stereoisomer rotates plane of polarization in clockwise direction, it is called dextrorotatory isomer, and if it rotates the plane of polarization in counter-clockwise direction, it is levorotatory isomer.',
 'نوری آئسومرزم آئسومرزم کی وہ قسم ہے جس میں آئسومر مستوی پولرائزڈ روشنی کے ساتھ مختلف تعامل رکھتے ہیں۔ اگر کوئی اسٹیریو آئسومر پولرائزیشن کے مستوی کو گھڑی کی سمت میں گھمائے تو اسے ڈیکسٹرو روٹیٹری آئسومر کہتے ہیں، اور اگر وہ پولرائزیشن کے مستوی کو گھڑی کی مخالف سمت میں گھمائے تو وہ لیوو روٹیٹری آئسومر ہے۔',
 'نوري ایزومېریزم د ایزومېریزم هغه ډول دی چې پکې ایزومرونه د سطحي پولرایز شوې رڼا په وړاندې بېل تعامل لري. که یو سټیریوایزومر د پولرایزېشن سطحه د ساعت د ستنو په لور وګرځوي، ډیکسټروروټېټري ایزومر بلل کېږي، او که د پولرایزېشن سطحه د ساعت د ستنو خلاف لوري ته وګرځوي، لیووروټېټري ایزومر دی.')
add('Lactic acid (2–hydroxypropanoic acid) is an example of a compound which shows optical isomerism and has two optical isomers. The isomer which is dextrorotatory is called (+)–lactic acid, while the levorotatory isomers is called (–)–lactic acid (Section 16.6.5).',
 'لیکٹک ایسڈ (2–ہائیڈروآکسی پروپانوئک ایسڈ) ایسے مرکب کی مثال ہے جو نوری آئسومرزم ظاہر کرتا ہے اور اس کے دو نوری آئسومر ہیں۔ جو آئسومر ڈیکسٹرو روٹیٹری ہے اسے (+)–لیکٹک ایسڈ کہتے ہیں، جبکہ لیوو روٹیٹری آئسومر کو (–)–لیکٹک ایسڈ کہتے ہیں (حصہ 16.6.5)۔',
 'لاکټیک اسید (2–هایدروکسي پروپانویک اسید) د داسې مرکب بېلګه ده چې نوري ایزومېریزم ښيي او دوه نوري ایزومرونه لري. هغه ایزومر چې ډیکسټروروټېټري دی (+)–لاکټیک اسید بلل کېږي، او لیووروټېټري ایزومر (–)–لاکټیک اسید بلل کېږي (برخه 16.6.5).')
add('16.6.3 Chiral Centres','16.6.3 کائرل مراکز','16.6.3 کایرل مرکزونه','heading')
add('A chiral center is an atom that has four different atoms or groups bonded to it. A chiral atom may have one lone pair and three different atoms or groups attached. It is also called chirality center or stereogenic center. Interchange of two groups at stereogenic center (or stereocenter) in a molecule gives another stereoisomer.',
 'کائرل مرکز وہ ایٹم ہے جس سے چار مختلف ایٹم یا گروپ جڑے ہوں۔ کسی کائرل ایٹم کے ساتھ ایک تنہا جوڑا اور تین مختلف ایٹم یا گروپ بھی جڑے ہو سکتے ہیں۔ اسے کائرلٹی مرکز یا اسٹیریوجینک مرکز بھی کہتے ہیں۔ کسی سالمے میں اسٹیریوجینک مرکز (یا اسٹیریو سینٹر) پر دو گروپوں کا باہمی تبادلہ ایک دوسرا اسٹیریو آئسومر دیتا ہے۔',
 'کایرل مرکز هغه اټوم دی چې څلور بېل اټومونه یا ګروپونه ورسره تړلي وي. یو کایرل اټوم کېدای شي یوه یوازینۍ جوړه او درې بېل اټومونه یا ګروپونه ولري. دې ته د کایرالیټي مرکز یا سټیریوجینیک مرکز هم وايي. په یوه مالیکول کې په سټیریوجینیک مرکز (یا سټیریوسنټر) د دوو ګروپونو ځای بدلول بل سټیریوایزومر ورکوي.')
add('16.6.4 Carbon based Chiral Center - Chiral Carbon','16.6.4 کاربن پر مبنی کائرل مرکز - کائرل کاربن','16.6.4 پر کاربن ولاړ کایرل مرکز - کایرل کاربن','heading')
add('A tetrahedral carbon atom in a molecule that bears four different substituents is referred to as a chiral carbon atom, stereogenic carbon or asymmetric carbon atom, and is often designated by an asterisk (∗). For example, lactic acid has a chiral carbon which is bonded to four different groups (–H, –OH, –CH₃, –COOH).',
 'کسی سالمے میں چار مختلف متبادلات رکھنے والا چہار سطحی کاربن ایٹم کائرل کاربن ایٹم، اسٹیریوجینک کاربن یا غیر متناسب کاربن ایٹم کہلاتا ہے، اور اسے اکثر ستارے (∗) سے ظاہر کیا جاتا ہے۔ مثلاً لیکٹک ایسڈ میں ایک کائرل کاربن ہے جو چار مختلف گروپوں (–H، –OH، –CH₃، –COOH) سے جڑا ہے۔',
 'په یوه مالیکول کې هغه څلورمخی کاربني اټوم چې څلور بېل بدیلونه لري، کایرل کاربني اټوم، سټیریوجینیک کاربن یا نامتقارن کاربني اټوم بلل کېږي، او ډېر ځله په ستوري (∗) ښودل کېږي. د بېلګې په توګه، لاکټیک اسید یو کایرل کاربن لري چې له څلورو بېلو ګروپونو (–H، –OH، –CH₃، –COOH) سره تړلی دی.')
visual('chem12-p68-lactic-acid',lactic)
add('16.6.5 Chirality','16.6.5 کائرلٹی','16.6.5 کایرالیټي','heading')
add('A molecule is chiral if its two mirror-image forms are not superimposable in three dimensions. The mirror image of chiral molecules is actually another stereoisomer. The word “chiral” is derived from the Greek word cheir, meaning “hand,” and it is entirely appropriate to speak of the “handedness” of molecules. All chiral molecules are also dissymmetric (do not have any plane of symmetry). The opposite of chiral is achiral. A molecule that is superimposable on its mirror image is achiral. Achiral molecules must have a plane of symmetry. Lactic acid has a chiral carbon and is also a chiral molecule. The non-superimposable mirror images of lactic acid are shown in (Figure 16.6).',
 'کوئی سالمہ کائرل ہوتا ہے اگر اس کی دو آئینہ عکسی صورتیں تین ابعاد میں ایک دوسرے پر منطبق نہ ہوں۔ کائرل سالمات کا آئینہ عکس دراصل ایک دوسرا اسٹیریو آئسومر ہوتا ہے۔ لفظ ”کائرل“ یونانی لفظ cheir سے نکلا ہے، جس کا مطلب ”ہاتھ“ ہے، اور سالمات کی ”ہاتھ پن“ کی بات کرنا بالکل مناسب ہے۔ تمام کائرل سالمات غیر متشاکل بھی ہوتے ہیں (ان کا کوئی تشاکلی مستوی نہیں ہوتا)۔ کائرل کا الٹ اکائرل ہے۔ جو سالمہ اپنے آئینہ عکس پر منطبق ہو جائے وہ اکائرل ہے۔ اکائرل سالمات میں لازماً تشاکلی مستوی ہوتا ہے۔ لیکٹک ایسڈ میں ایک کائرل کاربن ہے اور یہ کائرل سالمہ بھی ہے۔ لیکٹک ایسڈ کے غیر منطبق آئینہ عکس (شکل 16.6) میں دکھائے گئے ہیں۔',
 'یو مالیکول کایرل دی که د هغه دوه هینداریزې بڼې په درې بُعدونو کې یو پر بل منطبق نه شي. د کایرل مالیکولونو هینداریز انځور په حقیقت کې بل سټیریوایزومر دی. د ”کایرل“ کلمه له یوناني کلمې cheir څخه اخیستل شوې، چې معنا یې ”لاس“ ده، او د مالیکولونو د ”لاسوالي“ خبره کول بشپړ مناسب دي. ټول کایرل مالیکولونه نامتناظر هم دي (د تناظر هېڅ سطحه نه لري). د کایرل ضد اکایرل دی. هغه مالیکول چې پر خپل هینداریز انځور منطبق شي اکایرل دی. اکایرل مالیکولونه باید د تناظر سطحه ولري. لاکټیک اسید یو کایرل کاربن لري او کایرل مالیکول هم دی. د لاکټیک اسید نامنطبق هینداریز انځورونه په (شکل 16.6) کې ښودل شوي.')
visual('chem12-figure16-6',mirror)
add('Figure 16.6 Non-superimposable mirror images of a generalized chiral molecule and lactic acid.','شکل 16.6 ایک عمومی کائرل سالمے اور لیکٹک ایسڈ کے غیر منطبق آئینہ عکس۔','شکل 16.6 د یوه عمومي کایرل مالیکول او لاکټیک اسید نامنطبق هینداریز انځورونه.')
add('These structures are not identical because they cannot be superimposed on each other. They are the mirror images of each other. Such non superimposable mirror images constitute optical isomers and are called enantiomers of each other.',
 'یہ ساختیں یکساں نہیں کیونکہ انہیں ایک دوسرے پر منطبق نہیں کیا جا سکتا۔ یہ ایک دوسرے کے آئینہ عکس ہیں۔ ایسے غیر منطبق آئینہ عکس نوری آئسومر بناتے ہیں اور ایک دوسرے کے اینینشیومر کہلاتے ہیں۔',
 'دا جوړښتونه سره ورته نه دي ځکه چې یو پر بل منطبق کېدای نه شي. دوی د یو بل هینداریز انځورونه دي. داسې نامنطبق هینداریز انځورونه نوري ایزومرونه جوړوي او د یو بل اینانټیومرونه بلل کېږي.')
add('16.6.6 Optical Activity','16.6.6 نوری فعالیت','16.6.6 نوري فعالیت','heading')
add('Ordinary light is composed of electromagnetic radiations vibrating in many different planes and is unpolarized. The oscillating waves are of different wave lengths (polychromatic) in all possible planes perpendicular to the direction of propagation. It becomes monochromatic (light of a single wave length) when it is passed through a monochromator but it still has waves in all the planes. When this unpolarized light passes through a polarizing filter, the randomly vibrating light waves are filtered so that most of the light passing through is vibrating in one direction, and is now plane-polarized light (Figure 16.7) also.',
 'عام روشنی بہت سے مختلف مستویوں میں ارتعاش کرنے والی برقی مقناطیسی شعاعوں پر مشتمل ہوتی ہے اور غیر پولرائزڈ ہوتی ہے۔ ارتعاش کرتی لہریں انتشار کی سمت کے عمودی تمام ممکنہ مستویوں میں مختلف طول موج (کثیر رنگی) کی ہوتی ہیں۔ مونوکرومیٹر سے گزارنے پر یہ یک رنگی (ایک ہی طول موج کی روشنی) بن جاتی ہے مگر اس میں پھر بھی تمام مستویوں میں لہریں ہوتی ہیں۔ جب یہ غیر پولرائزڈ روشنی پولرائزنگ فلٹر سے گزرتی ہے تو بے ترتیب ارتعاش کرتی لہریں اس طرح چھن جاتی ہیں کہ گزرنے والی زیادہ تر روشنی ایک سمت میں ارتعاش کرتی ہے، اور اب یہ مستوی پولرائزڈ روشنی ہے (شکل 16.7)۔',
 'عادي رڼا په ډېرو بېلابېلو سطحو کې د لړزېدونکو برقي مقناطیسي وړانګو څخه جوړه ده او نا پولرایز شوې ده. لړزېدونکې څپې د خپرېدو د لوري په عمودي ټولو ممکنو سطحو کې بېلابېل موج اوږدوالي (څو رنګه) لري. کله چې له مونوکروماتور څخه تېره شي یو رنګه (د یوه موج اوږدوالي رڼا) کېږي، خو بیا هم په ټولو سطحو کې څپې لري. کله چې دا نا پولرایز شوې رڼا له پولرایزوونکي فلټر څخه تېرېږي، په ګډوډ ډول لړزېدونکې څپې داسې چاڼ کېږي چې ډېره تېرېدونکې رڼا په یوه لوري لړزېږي، او اوس سطحي پولرایز شوې رڼا ده (شکل 16.7).')
visual('chem12-figure16-7',polar)
add('Figure 16.7 Polarization of light with polarizer.','شکل 16.7 پولرائزر کے ذریعے روشنی کی پولرائزیشن۔','شکل 16.7 د پولرایزر په واسطه د رڼا پولرایزېشن.')
add('Solutions of some organic compounds have the ability to rotate the plane of polarized light. These compounds are said to be optically active, and this property of a compound is called optical activity. Optical activity of a compound is measured by an instrument called polarimeter. An optically active compound can exist in two enantiomeric forms, which rotate the plane of polarized light in opposite directions. These enantiomers are therefore optical isomers. The isomer which rotates the plane of polarized light to the right (clockwise direction) is said to be dextrorotatory isomer or (+)-isomer and the isomer which rotates the plane of polarized light to the left (anticlockwise direction) is said to be levorotatory isomer or (–)-isomer (Figure 16.8).',
 'بعض نامیاتی مرکبات کے محلول پولرائزڈ روشنی کے مستوی کو گھمانے کی صلاحیت رکھتے ہیں۔ ایسے مرکبات نوری طور پر فعال کہلاتے ہیں، اور مرکب کی اس خاصیت کو نوری فعالیت کہتے ہیں۔ کسی مرکب کی نوری فعالیت پولری میٹر نامی آلے سے ناپی جاتی ہے۔ نوری طور پر فعال مرکب دو اینینشیومری صورتوں میں موجود ہو سکتا ہے، جو پولرائزڈ روشنی کے مستوی کو مخالف سمتوں میں گھماتی ہیں۔ اس لیے یہ اینینشیومر نوری آئسومر ہیں۔ جو آئسومر پولرائزڈ روشنی کے مستوی کو دائیں (گھڑی کی سمت) گھمائے وہ ڈیکسٹرو روٹیٹری آئسومر یا (+)-آئسومر کہلاتا ہے اور جو آئسومر پولرائزڈ روشنی کے مستوی کو بائیں (گھڑی کی مخالف سمت) گھمائے وہ لیوو روٹیٹری آئسومر یا (–)-آئسومر کہلاتا ہے (شکل 16.8)۔',
 'د ځینو عضوي مرکباتو محلولونه د پولرایز شوې رڼا د سطحې د ګرځولو وړتیا لري. دا مرکبات نوري فعال بلل کېږي، او د مرکب دې ځانګړنې ته نوري فعالیت وايي. د مرکب نوري فعالیت د پولاریمېټر په نوم وسیلې اندازه کېږي. یو نوري فعال مرکب په دوو اینانټیومري بڼو شتون لرلی شي، چې د پولرایز شوې رڼا سطحه مخالفو لورو ته ګرځوي. نو دا اینانټیومرونه نوري ایزومرونه دي. هغه ایزومر چې د پولرایز شوې رڼا سطحه ښي لوري (د ساعت د ستنو په لور) ته ګرځوي ډیکسټروروټېټري ایزومر یا (+)-ایزومر بلل کېږي او هغه ایزومر چې د پولرایز شوې رڼا سطحه کیڼ لوري (د ساعت د ستنو خلاف) ته ګرځوي لیووروټېټري ایزومر یا (–)-ایزومر بلل کېږي (شکل 16.8).')

record=section('16.15','Optical isomerism, chirality and optical activity','نوری آئسومرزم، کائرلٹی اور نوری فعالیت','نوري ایزومېریزم، کایرالیټي او نوري فعالیت',paras,layout,blocks,'128–129')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':68,'printedPages':[128,129]}]
record['sourceContinuesOnPdfPage']=69
issues=[{'id':'chem12-p129-sentence-continues','printedPage':129,'description':'Last sentence of printed 129 ends on printed 130 ("said to be levorotatory isomer or (–)-isomer (Figure 16.8)."); kept whole in this record, rest of printed 130 continues in 16.16.'}]
carry=[{'from':'16.15','to':'16.16','startsAt':'Polarimetry is a common method'}]
if __name__=='__main__':save(68,[record],carry=carry,issues=issues,chapter_number=16)
