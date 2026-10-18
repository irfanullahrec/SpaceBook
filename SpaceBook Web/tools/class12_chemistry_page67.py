"""PDF67 printed126–127: structural isomerism and stereoisomerism."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=21):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="#17212b">{escape(v)}</text>'
def line(x,y,a,b,w=2):return f'<path d="M{x} {y}L{a} {b}" stroke="#222" stroke-width="{w}" fill="none"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
def start(h):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 {h}" role="img"><rect width="850" height="{h}" fill="white"/>'
names={
'propan-1-ol':('پروپان-1-اول','پروپان-1-ول'),'(n-propyl alcohol)':('(n-پروپائل الکوحل)','(n-پروپیل الکول)'),
'propan-2-ol':('پروپان-2-اول','پروپان-2-ول'),'(isopropyl alcohol)':('(آئسوپروپائل الکوحل)','(ایزوپروپیل الکول)'),
'but-1-ene':('بیوٹ-1-این','بیوټ-1-ین'),'but-2-ene':('بیوٹ-2-این','بیوټ-2-ین'),
'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'dimethyl ether':('ڈائی میتھائل ایتھر','ډای میتایل ایتر'),
'propionaldehyde':('پروپیون الڈیہائیڈ','پروپیون الدیهاید'),'acetone':('ایسیٹون','اسیتون'),
'diethyl ether':('ڈائی ایتھائل ایتھر','ډای ایتیل ایتر'),'methyl n-propyl ether':('میتھائل n-پروپائل ایتھر','میتایل n-پروپیل ایتر'),
'propanone':('پروپانون','پروپانون'),'(keto form)':('(کیٹو صورت)','(کیټو بڼه)'),
'propen-2-ol':('پروپین-2-اول','پروپین-2-ول'),'(enol form)':('(اینول صورت)','(اینول بڼه)'),
'cis-but-2-ene':('سس-بیوٹ-2-این','سیس-بیوټ-2-ین'),'trans-but-2-ene':('ٹرانس-بیوٹ-2-این','ټرانس-بیوټ-2-ین'),
'cis-1,2-dimethylcyclopropane':('سس-1،2-ڈائی میتھائل سائیکلوپروپین','سیس-1،2-ډای میتایل سایکلوپروپان'),
'trans-1,2-dimethylcyclopropane':('ٹرانس-1،2-ڈائی میتھائل سائیکلوپروپین','ټرانس-1،2-ډای میتایل سایکلوپروپان')}
def label(lang,v):return v if lang=='en' else names[v][0 if lang=='ur' else 1]
def pairs(lang,kind):
 h=240 if kind=='position' else 115;s=start(h)
 if kind=='position':
  s+=t(220,42,'CH₃—CH₂—CH₂—OH')+t(635,28,'CH₃—CH—CH₃')+line(635,34,635,56)+t(635,76,'OH')
  for x,n,b in [(220,'propan-1-ol','(n-propyl alcohol)'),(635,'propan-2-ol','(isopropyl alcohol)')]:s+=t(x,112,label(lang,n),18)+t(x,138,label(lang,b),17)
  s+=t(220,190,'CH₃—CH₂—CH=CH₂')+t(220,222,label(lang,'but-1-ene'),18)+t(635,190,'CH₃—CH=CH—CH₃')+t(635,222,label(lang,'but-2-ene'),18)
 else:
  rows={'functional':[('CH₃—CH₂—OH','ethyl alcohol'),('CH₃—O—CH₃','dimethyl ether')],'carbonyl':[('CH₃—CH₂—CHO','propionaldehyde'),('CH₃—CO—CH₃','acetone')],'metamer':[('CH₃—CH₂—O—CH₂—CH₃','diethyl ether'),('CH₃—O—CH₂—CH₂—CH₃','methyl n-propyl ether')]}[kind]
  for x,(formula,name) in zip([220,635],rows):s+=t(x,42,formula)+t(x,88,label(lang,name),18)
 return s+'</svg>'
visual('chem12-p67-position-isomers',lambda l:pairs(l,'position'))
add('16.6.1.3 Functional group Isomerism','16.6.1.3 فعلی گروپ آئسومرزم','16.6.1.3 د فعالي ګروپ ایزومېریزم','heading')
add('Functional group isomerism involves in compounds having the same formula but different functional groups. For example, ethyl alcohol and dimethyl ether are functional group isomers.','فعلی گروپ آئسومرزم ان مرکبات میں ہوتا ہے جن کا فارمولا یکساں مگر فعلی گروپ مختلف ہوں۔ مثلاً ایتھائل الکوحل اور ڈائی میتھائل ایتھر فعلی گروپ آئسومر ہیں۔','د فعالي ګروپ ایزومېریزم په هغو مرکباتو کې وي چې یو شان فورمول خو بېلابېل فعالي ګروپونه لري. د بېلګې په توګه، ایتیل الکول او ډای میتایل ایتر د فعالي ګروپ ایزومرونه دي.')
visual('chem12-p67-functional-isomers',lambda l:pairs(l,'functional'))
add('Similarly, Propionaldehyde and acetone are also functional group isomers.','اسی طرح پروپیون الڈیہائیڈ اور ایسیٹون بھی فعلی گروپ آئسومر ہیں۔','همدارنګه پروپیون الدیهاید او اسیتون هم د فعالي ګروپ ایزومرونه دي.')
visual('chem12-p67-carbonyl-isomers',lambda l:pairs(l,'carbonyl'))
add('16.6.1.4 Metamerism','16.6.1.4 میٹامرزم','16.6.1.4 مېټامېریزم','heading')
add('This type of isomerism is exhibited due to the unequal distribution of carbon atoms (or alkyl groups) on either side of the functional group. Isomers belong to the same homologous series. For example, diethyl ether and methyl n-propyl ether are metamers.','اس قسم کا آئسومرزم فعلی گروپ کے دونوں جانب کاربن ایٹموں (یا الکائل گروپوں) کی غیر مساوی تقسیم کے باعث ظاہر ہوتا ہے۔ آئسومر ایک ہی ہم سلسلہ خاندان سے تعلق رکھتے ہیں۔ مثلاً ڈائی ایتھائل ایتھر اور میتھائل n-پروپائل ایتھر میٹامر ہیں۔','دا ډول ایزومېریزم د فعالي ګروپ پر دواړو خواوو د کاربني اټومونو (یا الکایل ګروپونو) د نابرابر وېش له امله څرګندېږي. ایزومرونه په یوه همولوګ لړۍ پورې اړه لري. د بېلګې په توګه، ډای ایتیل ایتر او میتایل n-پروپیل ایتر مېټامرونه دي.')
visual('chem12-p67-metamers',lambda l:pairs(l,'metamer'))
add('16.6.1.5 Tautomerism','16.6.1.5 ٹاٹومرزم','16.6.1.5 ټاوټومېریزم','heading')
add('Tautomers are constitutional isomers that differ from each other by position of a proton (and may also a pi bond). It is a special type of functional group isomerism, in which the isomers are in dynamic equilibrium with each other. Tautomerization is the process of inter-conversion of tautomers, and an equilibrium process, which means that the equilibrium will establish with specific concentrations of tautomers of a compound. One of the important example of tautomerism is keto-enol tautomerism. The keto and enol tautomers of acetone are given below.','ٹاٹومر ایسے ساختی آئسومر ہیں جو پروٹون (اور ممکنہ طور پر پائی بند) کے مقام میں ایک دوسرے سے مختلف ہوں۔ یہ فعلی گروپ آئسومرزم کی خاص قسم ہے جس میں آئسومر ایک دوسرے کے ساتھ حرکی توازن میں ہوتے ہیں۔ ٹاٹومرائزیشن ٹاٹومروں کے باہمی تبدیل ہونے کا عمل اور ایک توازنی عمل ہے، یعنی مرکب کے ٹاٹومروں کی مخصوص ارتکازوں کے ساتھ توازن قائم ہوتا ہے۔ ٹاٹومرزم کی ایک اہم مثال کیٹو–اینول ٹاٹومرزم ہے۔ ایسیٹون کے کیٹو اور اینول ٹاٹومر ذیل میں ہیں۔','ټاوټومرونه جوړښتي ایزومرونه دي چې د پروټون (او ښايي د پای تړون) په موقعیت کې یو له بله توپیر لري. دا د فعالي ګروپ ایزومېریزم ځانګړی ډول دی چې ایزومرونه پکې یو له بل سره په متحرک تعادل کې وي. ټاوټومرایزېشن د ټاوټومرونو د خپلمنځي بدلون بهیر او یو تعادلي بهیر دی؛ یعنې تعادل به د یوه مرکب د ټاوټومرونو په ځانګړو غلظتونو کې ټینګ شي. د ټاوټومېریزم یوه مهمه بېلګه کیټو–اینول ټاوټومېریزم دی. د اسیتون کیټو او اینول ټاوټومرونه لاندې ورکړل شوي دي.')
def tautomer(lang):
 s=start(190)+t(220,87,'H—CH₂—C—CH₃')+line(254,67,254,39)+line(260,67,260,39)+t(257,30,'O')
 s+=line(385,77,463,77)+line(463,85,385,85)+'<path d="M455 71L463 77H455 M393 91L385 85H393" fill="none" stroke="#b42e50" stroke-width="2"/>'
 s+=t(650,87,'CH₂=C—CH₃')+line(650,67,650,39)+t(650,30,'OH')
 for x,n,f in [(230,'propanone','(keto form)'),(650,'propen-2-ol','(enol form)')]:s+=t(x,133,label(lang,n),18)+t(x,163,label(lang,f),18)
 return s+'</svg>'
visual('chem12-p67-tautomers',tautomer)
add('The result of this keto-enol tautomerization, is the migration of a proton from one location to another, accompanied by a change in location of the pi bond.','اس کیٹو–اینول ٹاٹومرائزیشن کا نتیجہ پروٹون کی ایک مقام سے دوسرے مقام پر منتقلی ہے، جس کے ساتھ پائی بند کا مقام بھی بدلتا ہے۔','د دې کیټو–اینول ټاوټومرایزېشن پایله د پروټون له یوه ځایه بل ځای ته لېږدېدل دي، چې ورسره د پای تړون موقعیت هم بدلېږي.')
add('16.6.2 Stereoisomerism','16.6.2 اسٹیریوآئسومرزم','16.6.2 سټیریوایزومېریزم','heading')
add('When isomerism is caused by different arrangement of atoms or groups in space, the phenomenon is called stereoisomerism. Thus, the stereoisomers have the same molecular formula and connectivity of atoms, but differ in the arrangement of atoms or groups in space. In other words, the isomers that have the same constitution but differ in the spatial arrangement of their atoms are called stereoisomers. Some stereoisomers which are inter-convertible by rotation of single bond are called conformational isomers. But the stereoisomers which are not inter-convertible without breaking and making of some bonds, are called configurational isomers. Conformational isomerism is beyond the scope of this book, so we will discuss only the configurational isomerism in stereoisomers, which is of two types i.e. geometric and optical isomerism.','جب آئسومرزم خلا میں ایٹموں یا گروپوں کی مختلف ترتیب کے باعث ہو تو اس مظہر کو اسٹیریوآئسومرزم کہتے ہیں۔ یوں اسٹیریوآئسومروں کا سالماتی فارمولا اور ایٹموں کا باہمی اتصال یکساں ہوتا ہے، مگر خلا میں ایٹموں یا گروپوں کی ترتیب مختلف ہوتی ہے۔ دوسرے لفظوں میں، یکساں ساخت رکھنے مگر ایٹموں کی فضائی ترتیب میں مختلف آئسومر اسٹیریوآئسومر کہلاتے ہیں۔ یک بند کے گرد گردش سے ایک دوسرے میں تبدیل ہونے والے بعض اسٹیریوآئسومر کنفارمیشنل آئسومر کہلاتے ہیں۔ لیکن وہ اسٹیریوآئسومر جو بعض بند توڑے اور بنائے بغیر باہم تبدیل نہیں ہوتے، کنفگوریشنل آئسومر کہلاتے ہیں۔ کنفارمیشنل آئسومرزم اس کتاب کے دائرے سے باہر ہے، لہٰذا ہم صرف کنفگوریشنل آئسومرزم پر بحث کریں گے، جس کی دو قسمیں یعنی ہندسی اور نوری آئسومرزم ہیں۔','کله چې ایزومېریزم په فضا کې د اټومونو یا ګروپونو د بېلابېل ترتیب له امله وي، دې پدیدې ته سټیریوایزومېریزم ویل کېږي. نو سټیریوایزومرونه یو شان مالیکولي فورمول او د اټومونو نښلون لري، خو په فضا کې د اټومونو یا ګروپونو په ترتیب کې توپیر لري. په بل عبارت، هغه ایزومرونه چې یو شان جوړښت لري خو د اټومونو په فضايي ترتیب کې توپیر لري، سټیریوایزومرونه بلل کېږي. ځینې سټیریوایزومرونه چې د یو ګوني تړون په څرخېدو یو پر بل بدلېږي، کنفورمېشنل ایزومرونه بلل کېږي. خو هغه سټیریوایزومرونه چې د ځینو تړونونو له ماتولو او جوړولو پرته یو پر بل نه بدلېږي، کنفیګورېشنل ایزومرونه بلل کېږي. کنفورمېشنل ایزومېریزم د دې کتاب له چوکاټه بهر دی، نو یوازې کنفیګورېشنل ایزومېریزم څېړو، چې دوه ډوله دی: هندسي او نوري ایزومېریزم.')
add('16.6.2.1 Geometrical Isomerism','16.6.2.1 ہندسی آئسومرزم','16.6.2.1 هندسي ایزومېریزم','heading')
add('Geometric isomers have different arrangement of atoms or groups when the rotation is restricted in a molecule. For example, but-2-ene have two stereoisomeric forms, cis-but-2-ene and trans-but-2-ene, as shown below.','جب سالمے میں گردش محدود ہو تو ہندسی آئسومروں میں ایٹموں یا گروپوں کی ترتیب مختلف ہوتی ہے۔ مثلاً بیوٹ-2-این کی دو اسٹیریوآئسومری صورتیں، سس-بیوٹ-2-این اور ٹرانس-بیوٹ-2-این ہیں، جیسا کہ ذیل میں دکھایا گیا ہے۔','کله چې په مالیکول کې څرخېدل محدود وي، هندسي ایزومرونه د اټومونو یا ګروپونو بېلابېل ترتیب لري. د بېلګې په توګه، بیوټ-2-ین دوه سټیریوایزومري بڼې لري: سیس-بیوټ-2-ین او ټرانس-بیوټ-2-ین، لکه لاندې چې ښودل شوي.')
def geometric(lang,cyclic=False):
 s=start(230)
 for x,trans in [(240,False),(650,True)]:
  if cyclic:
   left=(x-65,108);right=(x+65,108);bottom=(x,160)
   s+=line(*left,*right)+line(*left,*bottom,5)+line(*bottom,*right,5)
   ends=[(left[0],left[1],x-90,60,'CH₃'),(left[0],left[1],x-90,150,'H'),(right[0],right[1],x+90,60,'H' if trans else 'CH₃'),(right[0],right[1],x+90,150,'CH₃' if trans else 'H')]
  else:
   s+=t(x-30,110,'C')+t(x+30,110,'C')+line(x-17,102,x+17,102)+line(x-17,108,x+17,108)
   ends=[(x-37,95,x-65,52,'CH₃'),(x-37,113,x-65,156,'H'),(x+37,95,x+65,52,'H' if trans else 'CH₃'),(x+37,113,x+65,156,'CH₃' if trans else 'H')]
  for a,b,c,d,v in ends:
   sign=1 if d>b else -1;s+=line(a,b,c,d-sign*15)+t(c,d+6,v,20)
  name=('trans-' if trans else 'cis-')+('1,2-dimethylcyclopropane' if cyclic else 'but-2-ene');s+=t(x,211,label(lang,name),16 if cyclic else 18)
 return s+'</svg>'
visual('chem12-p67-cis-trans-butene',lambda l:geometric(l))
add('The isomers in which the two methyl groups are on the same side of the double bond is called the cis (a Latin word meaning “on this side”) isomer, while trans (a Latin word meaning “across”) isomer has got them on the opposite sides of the double bond. Consequently this type of isomerism is also called cis-trans isomerism. Due to restricted rotation of carbon-carbon double bond, the cis and trans isomers are not inter-convertible without breaking of pi bond. These are two different compounds and have different properties.','جس آئسومر میں دونوں میتھائل گروپ دوہرے بند کی ایک ہی جانب ہوں، وہ سس (لاطینی لفظ، بمعنی “اس جانب”) آئسومر کہلاتا ہے، جبکہ ٹرانس (لاطینی لفظ، بمعنی “آرپار”) آئسومر میں وہ دوہرے بند کی مخالف جانب ہوتے ہیں۔ چنانچہ اس قسم کو سس–ٹرانس آئسومرزم بھی کہتے ہیں۔ کاربن–کاربن دوہرے بند کے گرد محدود گردش کے باعث سس اور ٹرانس آئسومر پائی بند توڑے بغیر باہم تبدیل نہیں ہوتے۔ یہ دو مختلف مرکبات ہیں اور مختلف خصوصیات رکھتے ہیں۔','هغه ایزومر چې دواړه میتایل ګروپونه یې د دوه ګوني تړون پر یوه خوا وي، سیس (لاتیني کلمه، معنا یې “پر دې خوا”) ایزومر بلل کېږي، خو په ټرانس (لاتیني کلمه، معنا یې “بلې غاړې ته”) ایزومر کې دا ګروپونه د دوه ګوني تړون پر مخالفو خواوو وي. له همدې امله دا ډول ایزومېریزم سیس–ټرانس ایزومېریزم هم بلل کېږي. د کاربن–کاربن د دوه ګوني تړون د محدود څرخېدو له امله سیس او ټرانس ایزومرونه د پای تړون له ماتولو پرته یو پر بل نه بدلېږي. دا دوه بېلابېل مرکبات دي او بېلابېلې ځانګړنې لري.')
add('Geometric isomerism in alkenes is possible only when each double bonded carbon atom is attached to two different atoms or groups, thus propene does not have geometric isomers. Geometric isomerism is also possible in substituted cycloalkanes. For example 1,2-dimethylcyclopropane also has two geometric isomers.','الکینز میں ہندسی آئسومرزم صرف تب ممکن ہے جب دوہرے بند کا ہر کاربن ایٹم دو مختلف ایٹموں یا گروپوں سے جڑا ہو، اس لیے پروپین کے ہندسی آئسومر نہیں ہوتے۔ متبادل گروہوں والے سائیکلوالکینز میں بھی ہندسی آئسومرزم ممکن ہے۔ مثلاً 1،2-ڈائی میتھائل سائیکلوپروپین کے بھی دو ہندسی آئسومر ہیں۔','په الکینونو کې هندسي ایزومېریزم یوازې هغه مهال ممکن دی چې د دوه ګوني تړون هر کاربني اټوم له دوو بېلابېلو اټومونو یا ګروپونو سره تړلی وي؛ نو پروپین هندسي ایزومرونه نه لري. په ځایناستو لرونکو سایکلوالکانونو کې هم هندسي ایزومېریزم ممکن دی. د بېلګې په توګه، 1،2-ډای میتایل سایکلوپروپان هم دوه هندسي ایزومرونه لري.')
visual('chem12-p67-cis-trans-cyclopropane',lambda l:geometric(l,True))
record=section('16.14','Functional isomers, tautomerism and geometrical isomerism','فعلی آئسومر، ٹاٹومرزم اور ہندسی آئسومرزم','فعالي ایزومرونه، ټاوټومېریزم او هندسي ایزومېریزم',paras,layout,blocks,'126–127')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':67,'printedPages':[126,127]}]
if __name__=='__main__':save(67,[record],carry=[{'from':'16.14','to':'16.15','startsAt':'16.6.2.2 Optical Isomerism'}],chapter_number=16)
