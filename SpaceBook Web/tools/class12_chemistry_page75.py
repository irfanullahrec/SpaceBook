"""PDF75 printed142–143: polycyclic aromatics, physical properties and MO structure of benzene, resonance."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow75');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'naphthalene':('نیفتھلین','نفتالین'),'anthracene':('اینتھراسین','انتراسین'),'phenanthrene':('فینانتھرین','فینانترین'),'kekule structures':('کیکولے ساختیں','د کیکولې جوړښتونه'),
   'resonance hybrid':('ریزونینس ہائبرڈ','ریزونانس هایبرېډ'),'cyclohexa-1,3,5-triene':('سائیکلوہیکسا-1،3،5-ٹرائی این','سایکلوهېکسا-1،3،5-ټرای ین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
R=30;H=R*math.sqrt(3)  # flat-top-free: pointy-top hexagons; fused horizontally share a vertical edge
def poly(lang):
 s=F.start(170)
 for x in (95,95+H):s+=F.ring(x,80,R,kek=False,circle=True)
 s+=t(95+H/2,150,lb(lang,'naphthalene'),14)
 for k in range(3):s+=F.ring(330+k*H,80,R,kek=False,circle=True)
 s+=t(330+H,150,lb(lang,'anthracene'),14)
 # phenanthrene: two fused + one angular
 x0=620;s+=F.ring(x0,95,R,kek=False,circle=True)+F.ring(x0+H,95,R,kek=False,circle=True)+F.ring(x0+1.5*H,95-1.5*R,R,kek=False,circle=True)
 s+=t(x0+H/2,160,lb(lang,'phenanthrene'),14)
 return s+'</svg>'
def sigma(lang):
 s=F.start(250,520);cx,cy=260,125
 P=[(cx+70*math.cos(math.radians(60*i+30)),cy+70*math.sin(math.radians(60*i+30))) for i in range(6)]
 def lobe(x1,y1,x2,y2,ry=13,c='#8e24aa'):
  mx,my=(x1+x2)/2,(y1+y2)/2;ang=math.degrees(math.atan2(y2-y1,x2-x1));rx=math.hypot(x2-x1,y2-y1)/2
  return f'<ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="{rx:.1f}" ry="{ry}" fill="{c}" opacity=".72" transform="rotate({ang:.1f} {mx:.1f} {my:.1f})"/>'
 for i in range(6):
  (x1,y1),(x2,y2)=P[i],P[(i+1)%6];s+=lobe(x1,y1,x2,y2)
  x,y=P[i];hx,hy=cx+(x-cx)*1.65,cy+(y-cy)*1.65;s+=lobe(x,y,hx,hy,11)
  s+=f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="12" fill="#b3e5fc"/>'+t(hx,hy+5,'H',13,'#1a237e')
 for x,y in P:s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="#263238"/>'+t(x,y+5,'C',12,'#fff')
 return s+'</svg>'
def pi(lang):
 s=F.start(220);cx,cy=160,110
 pts=[(cx+60*math.cos(math.radians(60*i)),cy+40*math.sin(math.radians(60*i))) for i in range(6)]
 s+='<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'
 for x,y in pts:
  s+=f'<ellipse cx="{x:.1f}" cy="{y-20:.1f}" rx="9" ry="18" fill="#e91e63"/><ellipse cx="{x:.1f}" cy="{y+20:.1f}" rx="9" ry="18" fill="#1e88e5"/>'
  dx,dy=(x-cx)/60,(y-cy)/40;s+=line(x,y,x+dx*30,y+dy*22)+t(x+dx*40,y+dy*30+5,'H',13)
 cx2=430;s+=f'<ellipse cx="{cx2}" cy="88" rx="95" ry="30" fill="#ec407a"/><ellipse cx="{cx2}" cy="88" rx="45" ry="12" fill="white"/>'
 s+=f'<ellipse cx="{cx2}" cy="140" rx="95" ry="30" fill="#29b6f6"/><ellipse cx="{cx2}" cy="140" rx="45" ry="12" fill="white"/>'
 for x,y in ((360,60),(500,60),(360,175),(500,175)):s+=t(x,y,'H',13)
 s+=line(305,114,335,114)+t(296,119,'H',13)+line(525,114,555,114)+t(565,119,'H',13)
 s+=F.ring(700,110,45,circle=True)+line(700,65,739,87,1,'#555')+t(730,48,'1.397Å',13)+t(790,112,'120°',13)+t(740,190,'120°',13)+t(700,205,'H',13)
 return s+'</svg>'
def triene(lang):
 s=F.start(150,300)+F.ring(150,70,45,subs=None)
 for i,n in enumerate('612345'):
  a=math.radians(60*i);s+=t(150+28*math.sin(a),70-28*math.cos(a)+4,n,11,'#555')
 s+=t(185,22,'a',15)+t(205,80,'b',15)+t(150,140,lb(lang,'cyclohexa-1,3,5-triene'),13)
 return s+'</svg>'
def kekule(lang):
 s=F.start(160)+F.ring(240,70,42)
 s+=F.line(300,70,380,70,2,'#222','marker-end="url(#arrow75)"')+F.line(380,70,300,70,2,'#222','marker-end="url(#arrow75)"')
 pts=[(440+42*math.sin(math.radians(60*i)),70-42*math.cos(math.radians(60*i))) for i in range(6)]
 s+='<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'
 for i in (1,3,5):
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.78;s+=F.line(440+(x1-440)*k,70+(y1-70)*k,440+(x2-440)*k,70+(y2-70)*k)
 s+=t(530,78,'≡',26)+F.ring(620,70,42,kek=False,circle=True)
 s+=t(340,140,lb(lang,'kekule structures'),14)+t(620,140,lb(lang,'resonance hybrid'),14)
 return s+'</svg>'

add('Polycyclic aromatic hydrocarbons also have special names.','کثیر حلقوی ارومیٹک ہائیڈروکاربنوں کے بھی خاص نام ہیں۔','څو کړیز اروماتیک هایدروکاربنونه هم ځانګړي نومونه لري.')
visual('chem12-p75-polycyclic',poly)
add('16.8.2 Physical Properties of Benzene','16.8.2 بینزین کی طبعی خصوصیات','16.8.2 د بنزین فزیکي ځانګړنې','heading')
add('Benzene is a colourless liquid at room temperature and atmospheric pressure. It has peculiar smell and burning taste. The density of benzene is 0.88 g/mL. Benzene melts at 6°C and boils at 80°C. Benzene is more symmetrical than similar aliphatic compounds, so it packs better into crystals and has high melting point than corresponding aliphatic hydrocarbons. For example, benzene melts at 6°C, while hexane melts at –95°C. It is highly inflammable. Benzene is insoluble in water but soluble in ether, carbon tetrachloride etc.',
 'بینزین کمرے کے درجہ حرارت اور کرۂ ہوائی دباؤ پر بے رنگ مائع ہے۔ اس کی مخصوص بو اور جلانے والا ذائقہ ہوتا ہے۔ بینزین کی کثافت 0.88 g/mL ہے۔ بینزین 6°C پر پگھلتی اور 80°C پر ابلتی ہے۔ بینزین ملتے جلتے ایلیفیٹک مرکبات سے زیادہ متشاکل ہے، اس لیے یہ قلموں میں بہتر طور پر ترتیب پاتی ہے اور متعلقہ ایلیفیٹک ہائیڈروکاربنوں سے زیادہ نقطۂ پگھلاؤ رکھتی ہے۔ مثلاً بینزین 6°C پر پگھلتی ہے جبکہ ہیکسین –95°C پر پگھلتی ہے۔ یہ انتہائی آتش گیر ہے۔ بینزین پانی میں حل نہیں ہوتی مگر ایتھر، کاربن ٹیٹرا کلورائیڈ وغیرہ میں حل ہو جاتی ہے۔',
 'بنزین د کوټې په تودوخه او اتموسفېري فشار کې بې رنګه مایع ده. ځانګړی بوی او سوځوونکی خوند لري. د بنزین کثافت 0.88 g/mL دی. بنزین په 6°C کې ویلې کېږي او په 80°C کې ایشېږي. بنزین له ورته الیفاتیکو مرکباتو ډېر متناظر دی، نو په کرسټلونو کې ښه ځای پر ځای کېږي او له اړوندو الیفاتیکو هایدروکاربنونو لوړ د ویلې کېدو ټکی لري. د بېلګې په توګه، بنزین په 6°C کې ویلې کېږي، خو هېکسان په –95°C کې ویلې کېږي. ډېر اور اخیستونکی دی. بنزین په اوبو کې نه حلېږي خو په ایتر، کاربن ټیټراکلوراید او نورو کې حلېږي.')
add('16.8.3 Structure: Molecular Orbital Aspects','16.8.3 ساخت: سالماتی آربیٹل پہلو','16.8.3 جوړښت: مالیکولي اوربیټال اړخونه','heading')
add('The structure of benzene can best be described in terms of molecular orbital hybridization model. Each carbon atom of the ring is linked to others by sp²–hybrid orbitals and with s orbitals of the six hydrogen atoms, forming six C–C and six C–H sigma bonds respectively (Figure 16.11). Since, the sigma bond results from the overlap of planar sp²-hybrid orbitals, all carbon and hydrogen atoms in benzene lie in the same plane and all the bond angles are 120°.',
 'بینزین کی ساخت کو سالماتی آربیٹل ہائبرڈائزیشن ماڈل کے لحاظ سے بہترین طور پر بیان کیا جا سکتا ہے۔ حلقے کا ہر کاربن ایٹم sp²–ہائبرڈ آربیٹلوں کے ذریعے دوسرے کاربنوں سے اور چھ ہائیڈروجن ایٹموں کے s آربیٹلوں سے جڑ کر بالترتیب چھ C–C اور چھ C–H سگما بند بناتا ہے (شکل 16.11)۔ چونکہ سگما بند مستوی sp²-ہائبرڈ آربیٹلوں کے تداخل سے بنتا ہے، اس لیے بینزین میں تمام کاربن اور ہائیڈروجن ایٹم ایک ہی مستوی میں ہوتے ہیں اور تمام بند زاویے 120° ہوتے ہیں۔',
 'د بنزین جوړښت د مالیکولي اوربیټال هایبرېډیزېشن ماډل له مخې په ښه ډول بیانېدای شي. د کړۍ هر کاربني اټوم د sp²–هایبرېډ اوربیټالونو په واسطه له نورو سره او د شپږو هایدروجني اټومونو له s اوربیټالونو سره نښلي او په ترتیب سره شپږ C–C او شپږ C–H سیګما تړونونه جوړوي (شکل 16.11). څرنګه چې سیګما تړون د سطحي sp²-هایبرېډ اوربیټالونو له تداخل جوړېږي، د بنزین ټول کاربني او هایدروجني اټومونه په یوه سطحه کې پراته دي او ټولې تړون زاویې 120° دي.')
visual('chem12-figure16-11',sigma)
add('Figure 16.11 Orbital hybriziation model of benzene and formation of sigma bonds.','شکل 16.11 بینزین کا آربیٹل ہائبرڈائزیشن ماڈل اور سگما بندوں کی تشکیل۔','شکل 16.11 د بنزین د اوربیټال هایبرېډیزېشن ماډل او د سیګما تړونونو جوړېدل.')
add('Each carbon atom also possesses a half-filled unhybridized p orbital, which are perpendicular to the plane of sigma bonds. The side-wise overlap of these p orbitals produces delocalized pi molecular orbitals containing six electrons, which are associated with all six carbon atoms. It is this extensive pi electron delocalization which is responsible for the greater stability of benzene. The electron cloud of these delocalized pi electron lies half below and half above the ring (Figure 16.12). The carbon-carbon and carbon-hydrogen bond lengths are 139 pm (1.39 Å) and 108 pm (1.08 Å) respectively.',
 'ہر کاربن ایٹم کے پاس ایک نیم پُر غیر ہائبرڈ p آربیٹل بھی ہوتا ہے، جو سگما بندوں کے مستوی پر عمود ہوتے ہیں۔ ان p آربیٹلوں کا پہلو کے رخ تداخل چھ الیکٹرانوں پر مشتمل غیر مقامی پائی سالماتی آربیٹل بناتا ہے، جو تمام چھ کاربن ایٹموں سے وابستہ ہوتے ہیں۔ یہی وسیع پائی الیکٹرانی غیر مقامیت بینزین کی زیادہ پائیداری کی ذمہ دار ہے۔ ان غیر مقامی پائی الیکٹرانوں کا بادل آدھا حلقے کے نیچے اور آدھا اوپر ہوتا ہے (شکل 16.12)۔ کاربن–کاربن اور کاربن–ہائیڈروجن بندوں کی لمبائیاں بالترتیب 139 pm (1.39 Å) اور 108 pm (1.08 Å) ہیں۔',
 'هر کاربني اټوم یو نیم ډک نا هایبرېډ شوی p اوربیټال هم لري، چې د سیګما تړونونو پر سطحه عمود دي. د دې p اوربیټالونو اړخیز تداخل شپږ الکترونه لرونکي غیر ځایي پای مالیکولي اوربیټالونه جوړوي، چې له ټولو شپږو کاربني اټومونو سره تړاو لري. همدا پراخه پای الکتروني غیر ځایي کېدنه د بنزین د ډېر ثبات لامل ده. د دې غیر ځایي پای الکترونونو ورېځ نیمه د کړۍ لاندې او نیمه پورته پرته ده (شکل 16.12). د کاربن–کاربن او کاربن–هایدروجن تړونونو اوږدوالي په ترتیب سره 139 pm (1.39 Å) او 108 pm (1.08 Å) دي.')
visual('chem12-figure16-12',pi)
add('Figure 16.12 Unhybridized p-p orbitals overlap to form delocalized pi bonds.','شکل 16.12 غیر ہائبرڈ p-p آربیٹلوں کا تداخل غیر مقامی پائی بند بناتا ہے۔','شکل 16.12 د نا هایبرېډ شویو p-p اوربیټالونو تداخل غیر ځایي پای تړونونه جوړوي.')
add('16.8.4 Resonance, Resonance Energy and Stabilization','16.8.4 ریزونینس، ریزونینس توانائی اور پائیداری','16.8.4 ریزونانس، د ریزونانس انرژي او ثبات','heading')
add('Resonance','ریزونینس','ریزونانس','heading')
add('Some molecules (or ions) are not adequately represented by a single Lewis structure. Two or more valence-bond structures are drawn for such molecules, differing only in the placement of Pi electrons. These different structures are called resonance structures or resonance forms or canonical form because they are not different molecules, just different ways of drawing the same molecule. The actual molecule is said to be a resonance hybrid of its resonating forms.',
 'بعض سالمات (یا آئن) کسی ایک لیوس ساخت سے مناسب طور پر ظاہر نہیں ہوتے۔ ایسے سالمات کے لیے دو یا زیادہ ویلنس بانڈ ساختیں بنائی جاتی ہیں، جو صرف پائی الیکٹرانوں کی جگہ میں مختلف ہوتی ہیں۔ ان مختلف ساختوں کو ریزونینس ساختیں یا ریزونینس صورتیں یا کینونیکل صورت کہتے ہیں کیونکہ یہ مختلف سالمات نہیں بلکہ ایک ہی سالمے کو بنانے کے مختلف طریقے ہیں۔ اصل سالمے کو اس کی ریزونیٹنگ صورتوں کا ریزونینس ہائبرڈ کہا جاتا ہے۔',
 'ځینې مالیکولونه (یا ایونونه) په یوه لیوس جوړښت په بشپړ ډول نه ښودل کېږي. د داسې مالیکولونو لپاره دوه یا ډېر ویلنس باند جوړښتونه رسمېږي، چې یوازې د پای الکترونونو په ځای کې توپیر لري. دې بېلابېلو جوړښتونو ته ریزونانس جوړښتونه یا ریزونانس بڼې یا کینونیکل بڼه وايي ځکه چې بېل مالیکولونه نه دي، بلکې د یوه مالیکول د رسمولو بېلې لارې دي. اصلي مالیکول د خپلو ریزونانسي بڼو ریزونانس هایبرېډ بلل کېږي.')
add('For example, the structure (which is cyclohexa-1,3,5-triene) is used to represent benzene. It is not the real structure of benzene because if this is the real structure of benzene, it is expected that benzene should add three molecules of Br₂ (in absence of light), but in actual practice it does not do so. Benzene undergoes electrophilic substitution reaction rather than addition. The bond length of bonds “a” and “b” should be 154 pm and 134 pm respectively. However, all carbon-carbon bonds in benzene are equal and having bond lengths of 139 pm.',
 'مثلاً بینزین کو ظاہر کرنے کے لیے یہ ساخت (جو سائیکلوہیکسا-1،3،5-ٹرائی این ہے) استعمال ہوتی ہے۔ یہ بینزین کی اصل ساخت نہیں، کیونکہ اگر یہ بینزین کی اصل ساخت ہوتی تو توقع ہوتی کہ بینزین Br₂ کے تین سالمات (روشنی کی غیر موجودگی میں) شامل کرے، مگر عملاً ایسا نہیں ہوتا۔ بینزین اضافے کے بجائے الیکٹروفائلی تبادلے کا تعامل کرتی ہے۔ بندوں ”a“ اور ”b“ کی لمبائی بالترتیب 154 pm اور 134 pm ہونی چاہیے۔ تاہم بینزین میں تمام کاربن–کاربن بند برابر ہیں اور ان کی لمبائی 139 pm ہے۔',
 'د بېلګې په توګه، د بنزین د ښودلو لپاره دا جوړښت (چې سایکلوهېکسا-1،3،5-ټرای ین دی) کارېږي. دا د بنزین اصلي جوړښت نه دی، ځکه که دا د بنزین اصلي جوړښت وای، تمه کېده چې بنزین د Br₂ درې مالیکولونه (د رڼا په نشتوالي کې) ورزیات کړي، خو په عمل کې داسې نه کوي. بنزین د اضافې پر ځای الکتروفایلي بدلون تعامل کوي. د ”a“ او ”b“ تړونونو اوږدوالی باید په ترتیب سره 154 pm او 134 pm وای. خو په بنزین کې ټول کاربن–کاربن تړونونه سره برابر دي او اوږدوالی یې 139 pm دی.')
visual('chem12-p75-cyclohexatriene',triene)
add('Thus, the above structure is not the actual structure of benzene. In such case we write more than one structure to represent the actual structure of a molecule i.e. benzene. This representation of a real structure as a weighted average of two or more contributing structures is called resonance. The following resonance structures, commonly called Kekule structures, are used to represent benzene.',
 'لہٰذا اوپر والی ساخت بینزین کی اصل ساخت نہیں۔ ایسی صورت میں ہم کسی سالمے یعنی بینزین کی اصل ساخت ظاہر کرنے کے لیے ایک سے زیادہ ساختیں لکھتے ہیں۔ کسی حقیقی ساخت کو دو یا زیادہ شراکتی ساختوں کے وزنی اوسط کے طور پر ظاہر کرنا ریزونینس کہلاتا ہے۔ بینزین کو ظاہر کرنے کے لیے درج ذیل ریزونینس ساختیں استعمال ہوتی ہیں، جنہیں عام طور پر کیکولے ساختیں کہتے ہیں۔',
 'نو پورته جوړښت د بنزین اصلي جوړښت نه دی. په داسې حالت کې موږ د یوه مالیکول یعنې بنزین د اصلي جوړښت د ښودلو لپاره له یوه ډېر جوړښتونه لیکو. د یوه رښتیني جوړښت ښودل د دوو یا ډېرو ونډه لرونکو جوړښتونو د وزني اوسط په توګه ریزونانس بلل کېږي. د بنزین د ښودلو لپاره لاندې ریزونانس جوړښتونه کارېږي چې عموماً د کیکولې جوړښتونه بلل کېږي.')
visual('chem12-p75-kekule',kekule)

record=section('16.22','Polycyclic aromatics, benzene properties, MO structure and resonance','کثیر حلقوی ارومیٹکس، بینزین کی خصوصیات، سالماتی آربیٹل ساخت اور ریزونینس','څو کړیز اروماتیکونه، د بنزین ځانګړنې، مالیکولي اوربیټال جوړښت او ریزونانس',paras,layout,blocks,'142–143')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':75,'printedPages':[142,143]}]
record['sourceContinuesOnPdfPage']=76
issues=[{'id':'chem12-p142-hybriziation-typo','printedPage':142,'description':'Figure 16.11 caption printed "hybriziation"; italic definition sentence of resonance retained as plain text.'}]
carry=[{'from':'16.22','to':'16.23','startsAt':'It should be noted that the concept of resonance'}]
if __name__=='__main__':save(75,[record],carry=carry,issues=issues,chapter_number=16)
