"""PDF108 printed208–209: thiol names and properties, phenols, nomenclature of phenols, structure of phenol."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
import math
F=Fig('arrow108');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'IUPAC System:':('IUPAC نظام:','IUPAC سیستم:'),'Common System:':('عام نظام:','عام سیستم:'),'methanethiol':('میتھین تھائیول','میتان تیول'),'methyl mercaptan':('میتھائل مرکیپٹین','میتایل مرکاپټان'),
   'ethanethiol':('ایتھین تھائیول','ایتان تیول'),'ethyl mercaptan':('ایتھائل مرکیپٹین','ایتیل مرکاپټان'),'propane-2-thiol':('پروپین-2-تھائیول','پروپان-2-تیول'),'isopropyl mercaptan':('آئسوپروپائل مرکیپٹین','ایزوپروپیل مرکاپټان'),
   'phenol':('فینول','فینول'),'2-chlorophenol':('2-کلورو فینول','2-کلوروفینول'),'2-iodo-5-methylphenol':('2-آئیوڈو-5-میتھائل فینول','2-ایوډو-5-میتایل فینول'),
   'benzene-1,2-diol':('بینزین-1،2-ڈائی اول','بنزین-1،2-ډای ول'),'(catechol)':('(کیٹیکول)','(کېټیکول)'),'benzene-1,3-diol':('بینزین-1،3-ڈائی اول','بنزین-1،3-ډای ول'),'(resorcinol)':('(ریسورسینول)','(ریسورسینول)'),
   'benzene-1,4-diol':('بینزین-1،4-ڈائی اول','بنزین-1،4-ډای ول'),'(hydroquinone)':('(ہائیڈروکوئنون)','(هایدروکینون)'),'2-hydroxybenzoic acid':('2-ہائیڈروآکسی بینزوئک ایسڈ','2-هایدروکسي بنزویک اسید'),'(salicylic acid)':('(سیلیسیلک ایسڈ)','(سالیسیلیک اسید)'),
   '3-hydroxyacetophenone':('3-ہائیڈروآکسی ایسیٹو فینون','3-هایدروکسي اسیټوفینون'),'4-hydroxybenzaldehyde':('4-ہائیڈروآکسی بینز الڈیہائیڈ','4-هایدروکسي بنزالدیهاید'),'methyl alcohol':('میتھائل الکوحل','میتایل الکول')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def thiols(lang):
 s=F.start(130)+t(80,60,lb(lang,'IUPAC System:'),13)+t(80,80,lb(lang,'Common System:'),13)
 for x,(f,a,b,up) in zip((280,480,690),(('CH₃—SH','methanethiol','methyl mercaptan',None),('CH₃—CH₂—SH','ethanethiol','ethyl mercaptan',None),('CH₃—CH—CH₃','propane-2-thiol','isopropyl mercaptan','SH'))):
  s+=t(x,40,f,16)+t(x,62,lb(lang,a),12)+t(x,80,lb(lang,b),12)
  if up:s+=t(x,8+6,up,13)+line(x,18,x,26)
 return s.replace('viewBox="0 0 850 130"','viewBox="0 -10 850 140"')+'</svg>'
def grid(lang,items,h=190):
 s=F.start(h);n=len(items)
 for k,(subs,nums,a,b) in enumerate(items):
  x=850*(k+.5)/n;s+=F.ring(x,80,30,subs=subs)
  for v,lab in nums.items():
   ang=math.radians(60*v);s+=t(x+19*math.sin(ang),80-19*math.cos(ang)+4,lab,10,'#555')
  y0=80+30+(62 if 3 in subs else 24);s+=t(x,y0,lb(lang,a),12)+(t(x,y0+15,lb(lang,b),12) if b else '')
 return s+'</svg>'
def struct(lang):
 s=F.start(170)+F.ring(260,90,34)+t(250,96,'120°',12,'#c62828')+line(294,90,330,90)+t(342,96,'O',16)+line(350,96,368,112)+t(378,124,'H',15)+t(340,140,'109°',13)+t(312,40,'136 pm',14)+t(260,160,lb(lang,'phenol'),12)
 s+=t(560,96,'CH₃ — O',16)+line(590,100,608,116)+t(616,128,'H',15)+t(590,144,'108.9°',13)+t(590,40,'142 pm',14)+t(590,160,lb(lang,'methyl alcohol'),12)
 return s+'</svg>'

visual('chem12-p108-thiol-names',thiols)
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Thiols have a marked tendency to bond to mercury and the word mercaptan comes from the Latin mercurium captans, which means “seizing mercury.”','تھائیولز میں پارے سے بند بنانے کا نمایاں رجحان ہے اور لفظ مرکیپٹین لاطینی mercurium captans سے نکلا ہے، جس کا مطلب ہے ”پارہ پکڑنے والا“۔','تیولونه له سیمابو سره د تړلو ښکاره میلان لري او د مرکاپټان کلمه له لاتیني mercurium captans څخه اخیستل شوې، چې معنا یې ”سیماب نیوونکی“ ده.')
add('Methanethiol is a gas, while higher members are colourless, volatile liquids at RTP. Lower members have strong repulsive odours. Ethanethiol is added to natural gas in minute amounts to make gas leakage detectable by smell. Thiols have lower boiling points than the corresponding alcohols, due to lack of hydrogen bonding. They are insoluble in water but soluble in ethanol, ether and other organic solvents.',
 'میتھین تھائیول گیس ہے جبکہ بڑے ارکان RTP پر بے رنگ، اڑنے والے مائع ہیں۔ کم کاربن والے ارکان کی بو بہت ناگوار ہوتی ہے۔ گیس کے رساؤ کو بو سے پہچاننے کے قابل بنانے کے لیے قدرتی گیس میں ایتھین تھائیول بہت معمولی مقدار میں ملایا جاتا ہے۔ ہائیڈروجن بندش نہ ہونے کی وجہ سے تھائیولز کے نقطۂ جوش متعلقہ الکوحلز سے کم ہیں۔ یہ پانی میں حل نہیں ہوتے مگر ایتھانول، ایتھر اور دوسرے نامیاتی محللات میں حل ہوتے ہیں۔',
 'میتان تیول ګاز دی، خو لوړ غړي په RTP کې بې رنګه، الوتونکي مایعات دي. ټیټ غړي ډېر کرکجن بوی لري. ایتان تیول طبیعي ګاز ته په ډېره لږه اندازه ورګډېږي څو د ګاز وتل په بوی وپېژندل شي. تیولونه د هایدروجني تړون د نشتوالي له امله له اړوندو الکولونو ټیټ د ایشېدو ټکي لري. په اوبو کې نه حلېږي خو په ایتانول، ایتر او نورو عضوي محللونو کې حلېږي.')
add('18.2 Phenols','18.2 فینولز','18.2 فینولونه','heading')
add('Phenols are organic compounds in which hydroxyl group is attached directly to an aromatic ring. The parent compound of this group is called phenol (C₆H₅OH). Just like alcohols, they may also be monohydric, dihydric or polyhydric, depending upon the number of –OH groups attached per molecule.',
 'فینولز وہ نامیاتی مرکبات ہیں جن میں ہائیڈروآکسل گروپ براہِ راست ارومیٹک حلقے سے جڑا ہو۔ اس گروہ کا بنیادی مرکب فینول (C₆H₅OH) کہلاتا ہے۔ الکوحلز کی طرح یہ بھی فی سالمہ جڑے –OH گروپوں کی تعداد کے لحاظ سے مونو ہائیڈرک، ڈائی ہائیڈرک یا پولی ہائیڈرک ہو سکتے ہیں۔',
 'فینولونه هغه عضوي مرکبات دي چې پکې هایدروکسیل ګروپ مستقیم له اروماتیکې کړۍ سره تړلی وي. د دې ډلې اصلي مرکب فینول (C₆H₅OH) بلل کېږي. د الکولونو په څېر دوی هم په هر مالیکول کې د تړلو –OH ګروپونو د شمېر له مخې مونوهایدریک، ډای هایدریک یا پولي هایدریک کېدای شي.')
add('18.2.1 Nomenclature','18.2.1 نام گذاری','18.2.1 نومول','heading')
add('The systematic name for phenol is benzenol. But like other aromatic compounds, the common names of phenol and substituted phenols are acceptable IUPAC names. The substituted phenols are usually named as derivatives of the parent phenol.','فینول کا نظامی نام بینزینول ہے۔ لیکن دوسرے ارومیٹک مرکبات کی طرح فینول اور متبادل فینولز کے عام نام قابلِ قبول IUPAC نام ہیں۔ متبادل فینولز کے نام عموماً بنیادی فینول کے مشتقات کے طور پر رکھے جاتے ہیں۔','د فینول سیستماتیک نوم بنزینول دی. خو د نورو اروماتیکو مرکباتو په څېر د فینول او بدیل لرونکو فینولونو عام نومونه د منلو وړ IUPAC نومونه دي. بدیل لرونکي فینولونه معمولاً د اصلي فینول د مشتقاتو په توګه نومول کېږي.')
visual('chem12-p108-phenol-names',lambda l:grid(l,[({0:'OH'},{},'phenol',None),({0:'OH',1:'Cl'},{0:'1',1:'2'},'2-chlorophenol',None),({0:'OH',1:'I',4:'H₃C'},{0:'1',1:'2',2:'3',3:'4',4:'5',5:'6'},'2-iodo-5-methylphenol',None)]))
add('The three isomeric dihydroxy derivatives of benzene may be named as 1,2–, 1,3– and 1,4–benzenediol, respectively, but each one is more familiarly known by the common name indicated in parentheses below the structures shown here. These common names are permissible IUPAC names. Similar trihydroxy derivatives are named as benzenetriol and so on.',
 'بینزین کے تین ہم ترکیب ڈائی ہائیڈروآکسی مشتقات کے نام بالترتیب 1،2–، 1،3– اور 1،4–بینزین ڈائی اول رکھے جا سکتے ہیں، لیکن ہر ایک زیادہ تر اس عام نام سے جانا جاتا ہے جو یہاں دکھائی گئی ساختوں کے نیچے قوسین میں دیا گیا ہے۔ یہ عام نام قابلِ اجازت IUPAC نام ہیں۔ اسی طرح ٹرائی ہائیڈروآکسی مشتقات کے نام بینزین ٹرائی اول وغیرہ رکھے جاتے ہیں۔',
 'د بنزین درې ایزومري ډای هایدروکسي مشتقات کېدای شي په ترتیب سره 1،2–، 1،3– او 1،4–بنزین ډای ول ونومول شي، خو هر یو ډېر د هغه عام نوم په واسطه پېژندل کېږي چې دلته د ښودل شویو جوړښتونو لاندې په قوسونو کې ورکړل شوی. دا عام نومونه د منلو وړ IUPAC نومونه دي. ورته ټرای هایدروکسي مشتقات بنزین ټرای ول او داسې نور نومول کېږي.')
visual('chem12-p108-benzenediols',lambda l:grid(l,[({0:'OH',1:'OH'},{0:'1',1:'2'},'benzene-1,2-diol','(catechol)'),({0:'OH',2:'OH'},{0:'1',1:'2',2:'3'},'benzene-1,3-diol','(resorcinol)'),({0:'OH',3:'OH'},{0:'1',1:'2',2:'3',3:'4'},'benzene-1,4-diol','(hydroquinone)')],235))
add('Carboxyl, acyl and other groups, that take precedence over the phenolic hydroxyl, should determine the base name. The hydroxyl is treated as a substituent in these cases.','کاربوکسل، ایسائل اور دوسرے گروپ جو فینولی ہائیڈروآکسل پر ترجیح رکھتے ہیں، بنیادی نام کا تعین کرتے ہیں۔ ایسی صورتوں میں ہائیڈروآکسل کو متبادل سمجھا جاتا ہے۔','کاربوکسیل، اسایل او نور ګروپونه چې پر فینولي هایدروکسیل لومړیتوب لري، اصلي نوم ټاکي. په دې حالتونو کې هایدروکسیل د بدیل په توګه ګڼل کېږي.')
visual('chem12-p108-hydroxy-derivatives',lambda l:grid(l,[({0:'COOH',1:'OH'},{0:'1',1:'2'},'2-hydroxybenzoic acid','(salicylic acid)'),({0:'COCH₃',2:'OH'},{0:'1',1:'2',2:'3'},'3-hydroxyacetophenone',None),({0:'CHO',3:'OH'},{0:'1',1:'2',2:'3',3:'4'},'4-hydroxybenzaldehyde',None)],235))
add('Some other examples of phenols are already discussed in (Section 16.8.1).','فینولز کی کچھ دوسری مثالیں پہلے ہی (حصہ 16.8.1) میں بیان ہو چکی ہیں۔','د فینولونو ځینې نورې بېلګې دمخه په (برخه 16.8.1) کې بیان شوې.')
add('18.2.2 Structure of Phenol','18.2.2 فینول کی ساخت','18.2.2 د فینول جوړښت','heading')
add('In phenol molecule, the hydroxyl group is attached to a benzene ring. The molecule is planar, with a C–O–H bond angle of 109°, almost the same as tetrahedral angle and not much different from the, C–O–H angle (108.9°) of methyl alcohol (Section 18.1.3).','فینول کے سالمے میں ہائیڈروآکسل گروپ بینزین حلقے سے جڑا ہوتا ہے۔ سالمہ مستوی ہے، جس کا C–O–H بند زاویہ 109° ہے، جو تقریباً چہار سطحی زاویے کے برابر ہے اور میتھائل الکوحل کے C–O–H زاویے (108.9°) سے زیادہ مختلف نہیں (حصہ 18.1.3)۔','د فینول په مالیکول کې هایدروکسیل ګروپ له بنزیني کړۍ سره تړلی دی. مالیکول سطحي دی، چې د C–O–H تړون زاویه یې 109° ده، نږدې د څلورمخي زاویې سره برابره او د میتایل الکول له C–O–H زاویې (108.9°) څخه ډېره توپیر نه لري (برخه 18.1.3).')
visual('chem12-figure18-2',struct)
add('Figure 18.2 Comparison of structure of phenol and methyl alcohol','شکل 18.2 فینول اور میتھائل الکوحل کی ساخت کا موازنہ','شکل 18.2 د فینول او میتایل الکول د جوړښت پرتله')
add('In phenol the six carbon atoms are sp²–hybridized forming a hexagonal ring with internal angles of 120°. In the bonds C–O and O–H, bond lengths are 136 pm and 96 pm respectively. Since the bonds formed by sp²–hybridized carbon, are shorter than those formed by sp³-hybridized carbon, therefore the C–O bond length is slightly less than the C–O bond length in methanol (142 pm). In resonance terms, the shorter carbon–oxygen bond distance in phenol is attributed to the partial double-bond character that results from conjugation of the unshared electron pair of oxygen with the aromatic ring.',
 'فینول میں چھ کاربن ایٹم sp²–ہائبرڈ ہوتے ہیں اور 120° کے اندرونی زاویوں والا مسدس حلقہ بناتے ہیں۔ C–O اور O–H بندوں کی لمبائیاں بالترتیب 136 pm اور 96 pm ہیں۔ چونکہ sp²–ہائبرڈ کاربن کے بنائے ہوئے بند sp³-ہائبرڈ کاربن کے بندوں سے چھوٹے ہوتے ہیں، اس لیے C–O بند کی لمبائی میتھانول کے C–O بند (142 pm) سے قدرے کم ہے۔ ریزونینس کے لحاظ سے فینول میں کاربن–آکسیجن بند کا کم فاصلہ اس جزوی دوہرے بند کی خصوصیت سے منسوب ہے جو آکسیجن کے غیر مشترک الیکٹرانی جوڑے کے ارومیٹک حلقے سے کنجوگیشن کے نتیجے میں پیدا ہوتی ہے۔',
 'په فینول کې شپږ کاربني اټومونه sp²–هایبرېډ دي او د 120° داخلي زاویو شپږ ګوټې کړۍ جوړوي. د C–O او O–H تړونونو اوږدوالي په ترتیب سره 136 pm او 96 pm دي. څرنګه چې د sp²–هایبرېډ کاربن په واسطه جوړ شوي تړونونه د sp³-هایبرېډ کاربن له تړونونو لنډ دي، د C–O تړون اوږدوالی په میتانول کې د C–O تړون (142 pm) څخه یو څه کم دی. د ریزونانس له مخې په فینول کې د کاربن–اکسیجن لنډ واټن هغې نیمګړې دوه ګونې تړون ځانګړنې ته منسوب دی چې د اروماتیکې کړۍ سره د اکسیجن د نه شریکې الکتروني جوړې له کانجوګېشن رامنځته کېږي.')
record=section('18.8','Thiols, phenols, nomenclature and structure of phenol','تھائیولز، فینولز، فینول کی نام گذاری اور ساخت','تیولونه، فینولونه، د فینول نومول او جوړښت',paras,layout,blocks,'208–209')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':108,'printedPages':[208,209]}]
record['sourceContinuesOnPdfPage']=109
issues=[{'id':'chem12-p209-sentence-end','printedPage':209,'description':'Last phenol-structure sentence completes on printed 210; kept whole here.'}]
trim=[{'id':'18.9','startsAt':'1120°'}]
if __name__=='__main__':save(108,[record],trim=trim,issues=issues,chapter_number=18)
