"""Source PDF35, printed62–63; figure and typography review pending."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,body):
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 460" role="img"><g font-family="Arial" font-size="18" fill="#222">'+body+'</g></svg>'
 blocks.append({'id':identity,'svg':svg,'svgUrdu':svg,'svgPashto':svg});layout.append({'type':'visual','blockId':identity})
body=''
for x,y,m,labels,charge,formula in [(170,110,'Fe',['H₂O']*6,'3+','[Fe(H₂O)₆]³⁺'),(520,110,'Al',['F']*6,'3−','[AlF₆]³⁻'),(170,330,'Co',['NH₃']*6,'2+','[Co(NH₃)₆]²⁺'),(520,330,'Cu',['H₂O','NH₃','NH₃','H₂O','NH₃','NH₃'],'2+','[Cu(NH₃)₄(H₂O)₂]²⁺')]:
 body+=f'<text x="{x-10}" y="{y+6}">{m}</text>'
 for i,(dx,dy) in enumerate([(0,-72),(70,-32),(70,35),(0,75),(-70,35),(-70,-32)]):
  body+=f'<text x="{x+dx-15}" y="{y+dy}">{labels[i]}</text><path d="M{x+dx*.72} {y+dy*.72}L{x+dx*.23} {y+dy*.23}" stroke="#222" stroke-width="2"'+(' stroke-dasharray="3 3"' if i in [1,5] else '')+'/>'
  # Arrowhead points from donor ligand towards the central metal.
  import math
  a=math.atan2(-dy,-dx);tx=x+dx*.23;ty=y+dy*.23
  body+=f'<path d="M{tx} {ty}L{tx-9*math.cos(a-.45)} {ty-9*math.sin(a-.45)}L{tx-9*math.cos(a+.45)} {ty-9*math.sin(a+.45)}Z"/>'
 body+=f'<path d="M{x-100} {y-90}h-10v180h10M{x+105} {y-90}h10v180h-10" fill="none" stroke="#222"/><text x="{x+118}" y="{y-80}">{charge}</text><text x="{x-90}" y="{y+117}">{formula}</text>'
visual('chem12-figure14-6',body)
add('Figure 14.6 Geometrical shapes of complexes.','شکل 14.6 کمپلیکسوں کی ہندسی شکلیں۔','شکل 14.6 د کمپلېکسونو هندسي شکلونه.')
add('14.2.4 Colour of Complexes','14.2.4 کمپلیکسوں کا رنگ','14.2.4 د کمپلېکسونو رنګ','heading')
add('Most of the compounds of the transition metals are coloured in solid or solution state. In transition elements, the d orbitals are responsible for the development of colour in the transition compound. When these orbitals form bonds with the ligands, they splits up, e.g. in octahedral complexes they divide into two energy levels, one set has higher energy than the other. The electrons residing in low energy d-orbital absorb a part of the visible light and jump to higher energy d-orbital. This process is called d – d transition.',
 'عبوری دھاتوں کے بیشتر مرکبات ٹھوس یا محلول حالت میں رنگین ہیں۔ عبوری عناصر میں d آربیٹل مرکب کا رنگ پیدا کرتے ہیں۔ جب یہ آربیٹل لیگنڈز سے بند بناتے ہیں تو تقسیم ہوتے ہیں؛ مثلاً آکٹاہیڈرل کمپلیکسوں میں دو توانائی سطحوں میں تقسیم ہوتے ہیں، ایک مجموعے کی توانائی دوسرے سے زیادہ ہے۔ کم توانائی d آربیٹل کے الیکٹران مرئی روشنی کا کچھ حصہ جذب کرکے زیادہ توانائی d آربیٹل میں چھلانگ لگاتے ہیں۔ یہ عمل d–d منتقلی ہے۔',
 'د انتقالي فلزونو ډېری مرکبات په جامد یا محلول حالت کې رنګین دي. په انتقالي عناصرو کې d اوربیټالونه د مرکب رنګ رامنځته کوي. چې دا اوربیټالونه له لېګنډونو سره تړونونه جوړ کړي، وېشل کېږي؛ لکه په اوکتاهېډرل کمپلېکسونو کې په دوو انرژي سطحو وېشل کېږي، د یوه ټولګي انرژي تر بل زیاته وي. د ټیټې انرژۍ d اوربیټال الکترونونه د لیدو وړ رڼا یوه برخه جذبوي او د لوړې انرژۍ d اوربیټال ته ټوپ کوي. دې بهیر ته d–d انتقال وایي.')
add('When light is allowed to fall on a substance, it absorbs from it the light of a particular colour whose wavelength is in the visible region (4000 – 7000Å) and reflects or transmits back the remaining light which is the colour complementary to that of the absorbed light. The colour of the transmitted light is different from the colour of the absorbed light and is known as the complementary colour of the absorbed light. The colour of the transition metal complex is the colour of this transmitted light.',
 'روشنی کسی مادے پر پڑے تو وہ ایک خاص رنگ کی روشنی جذب کرتا ہے جس کی طول موج مرئی علاقے (4000–7000Å) میں ہے، اور باقی روشنی منعکس یا منتقل کرتا ہے، جس کا رنگ جذب شدہ روشنی کا تکمیلی رنگ ہے۔ منتقل روشنی کا رنگ جذب شدہ روشنی سے مختلف ہے اور اس کا تکمیلی رنگ کہلاتا ہے۔ عبوری دھاتی کمپلیکس کا رنگ اسی منتقل روشنی کا رنگ ہے۔',
 'چې رڼا پر یوه ماده ولګېږي، ماده د ځانګړي رنګ رڼا جذبوي چې د څپې اوږدوالی یې د لیدو وړ سیمه (4000–7000Å) کې وي، او پاتې رڼا منعکسوي یا لېږدوي، چې رنګ یې د جذب شوې رڼا متمم رنګ دی. د لېږدېدلې رڼا رنګ له جذب شوې رڼا توپیر لري او د هغې متمم رنګ بلل کېږي. د انتقالي فلزي کمپلېکس رنګ د همدې لېږدېدلې رڼا رنګ دی.')
add('Tidbit — Complementary Colours','مختصر معلومات — تکمیلی رنگ','لنډ معلومات — متمم رنګونه','heading')
add('Colours directly opposite each other on the colour wheel are said to be complementary colours. Blue and yellow are complementary colours; red and cyan are complementary; and so are green and magenta. Copper (II) sulphate solution is pale blue (cyan) because it absorbs light in the red region of the spectrum. Thus, cyan is the complementary colour of red.',
 'رنگوں کے دائرے میں بالکل آمنے سامنے رنگ تکمیلی رنگ ہیں۔ نیلا اور پیلا، سرخ اور سیان، اور سبز اور میجنٹا تکمیلی ہیں۔ کاپر(II) سلفیٹ کا محلول ہلکا نیلا (سیان) ہے کیونکہ وہ طیف کے سرخ علاقے کی روشنی جذب کرتا ہے۔ یوں سیان سرخ کا تکمیلی رنگ ہے۔',
 'د رنګونو په دایره کې یو بل ته مخامخ رنګونه متمم رنګونه دي. نیلي او ژېړ، سور او سیان، او شین او مېجنټا متمم دي. د مسو(II) سلفېټ محلول سپک نیلي (سیان) دی ځکه د طیف په سره سیمه کې رڼا جذبوي. نو سیان د سره متمم رنګ دی.')
body=''
import math
for i,(label,color) in enumerate([('Magenta','#df1687'),('Blue','#6030a2'),('Cyan','#19bdce'),('Green','#35993b'),('Yellow','#ffe800'),('Red','#e33232')]):
 a=-math.pi/2+i*math.pi/3;b=a+math.pi/3
 x1,y1=360+120*math.cos(a),220+120*math.sin(a);x2,y2=360+120*math.cos(b),220+120*math.sin(b)
 body+=f'<path d="M360 220L{x1} {y1}A120 120 0 0 1 {x2} {y2}Z" fill="{color}" stroke="white" stroke-width="3"/><text x="{360+170*math.cos((a+b)/2)-25}" y="{220+170*math.sin((a+b)/2)}">{label}</text>'
visual('chem12-p62-complementary-wheel',body)
for field,words in [('svgUrdu',['میجنٹا','نیلا','سیان','سبز','پیلا','سرخ']),('svgPashto',['مېجنټا','نیلي','سیان','شین','ژېړ','سور'])]:
 for label,word in zip(['Magenta','Blue','Cyan','Green','Yellow','Red'],words):
  blocks[-1][field]=blocks[-1][field].replace('>'+label+'</text>','>'+word+'</text>')
add('If the complex absorbs all colours except orange, the complex appears orange. The complex will also appear orange if it absorbs only light of the colour blue. In a complementary manner, if the complex ion absorbed only orange, it would appear blue. Blue and orange are referred to as complementary colours. In [Ti(H₂O)₆]³⁺, yellow and green lights are absorbed, while most of the blue and red lights are transmitted, therefore the solution of [Ti(H₂O)₆]³⁺ ions looks purple in colour.',
 'کمپلیکس نارنجی کے سوا تمام رنگ جذب کرے تو نارنجی دکھائی دیتا ہے۔ صرف نیلی روشنی جذب کرے تو بھی نارنجی ہے۔ تکمیلی طور پر صرف نارنجی جذب کرنے والا کمپلیکس آئن نیلا دکھائی دیتا ہے۔ نیلا اور نارنجی تکمیلی رنگ ہیں۔ [Ti(H₂O)₆]³⁺ میں پیلی اور سبز روشنی جذب جبکہ بیشتر نیلی اور سرخ روشنی منتقل ہوتی ہے، اس لیے ان آئنوں کا محلول جامنی ہے۔',
 'که کمپلېکس له نارنجي پرته ټول رنګونه جذب کړي، نارنجي ښکاري. که یوازې نیلي رڼا جذب کړي، هم نارنجي ښکاري. په متمم ډول که کمپلېکس ایون یوازې نارنجي جذب کړي، نیلي ښکاري. نیلي او نارنجي متمم رنګونه دي. په [Ti(H₂O)₆]³⁺ کې ژېړه او شنه رڼا جذبېږي، خو ډېره نیلي او سره رڼا لېږدېږي، نو د دغو ایونونو محلول ارغواني ښکاري.')
def wave(x,y,w,c):
 # printed light rays are drawn as small sine-like waves ending in an arrowhead
 d=f'M{x} {y}'+''.join(f'q{5} {-6} {10} 0t10 0' for _ in range(int(w//20)))
 e=x+int(w//20)*20
 return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2"/><path d="M{e} {y-5}L{e+9} {y}L{e} {y+5}Z" fill="{c}"/>'
B,R='#27587d','#b5543c'
f7='<text x="50" y="300">Incoming λ</text><text x="300" y="300">Absorbed λ</text><text x="560" y="300">Transmitted λ</text>'
f7+=''.join(wave(30,y,100,c) for y,c in [(110,B),(132,B),(154,B),(176,R),(198,R),(220,R)])
f7+=wave(290,190,100,B)+wave(290,212,100,R)
f7+=''.join(wave(590,y,80,c) for y,c in [(110,B),(132,B),(196,R),(218,R)])
f7+='<rect x="160" y="110" width="70" height="35" fill="none" stroke="#222"/><path d="M195 110V145" stroke="#222"/><text x="240" y="135">eg</text>'
f7+='<rect x="150" y="200" width="105" height="35" fill="none" stroke="#222"/><path d="M185 200V235M220 200V235" stroke="#222"/><text x="160" y="224">↑</text><text x="262" y="230">t2g</text>'
f7+='<text x="345" y="60" font-size="14">e⁻ jumps to</text><text x="345" y="78" font-size="14">higher level</text><path d="M395 84L430 108" stroke="#222"/>'
f7+='<rect x="420" y="110" width="70" height="35" fill="#f3d6dc" stroke="#222"/><path d="M455 110V145" stroke="#222"/><text x="430" y="135">↑</text><text x="500" y="135">eg</text>'
f7+='<rect x="400" y="240" width="105" height="35" fill="none" stroke="#222"/><path d="M435 240V275M470 240V275" stroke="#222"/><text x="512" y="270">t2g</text>'
visual('chem12-figure14-7',f7)
for field,words in [('svgUrdu',['آنے والی λ','جذب شدہ λ','منتقل λ']),('svgPashto',['راروانه λ','جذب شوې λ','لېږدېدلې λ'])]:
 for label,word in zip(['Incoming λ','Absorbed λ','Transmitted λ'],words):
  blocks[-1][field]=blocks[-1][field].replace('>'+label+'</text>','>'+word+'</text>')
add('e⁻ jumps to higher level','e⁻ زیادہ توانائی سطح میں چھلانگ لگاتا ہے','e⁻ لوړې انرژي سطحې ته ټوپ کوي')
add('Figure 14.7: Absorbance and transmittance of light in [Ti(H₂O)₆]³⁺ and splitting of d-orbital.','شکل 14.7: [Ti(H₂O)₆]³⁺ میں روشنی کا جذب اور انتقال اور d آربیٹل کی تقسیم۔','شکل 14.7: په [Ti(H₂O)₆]³⁺ کې د رڼا جذب او لېږد او د d اوربیټال وېش.')
add('The ions which have completely filled or empty d–orbitals are colourless e.g. complexes of Cu⁺(3d¹⁰), Zn²⁺(3d¹⁰) and Sc³⁺(3d⁰), Ti⁴⁺(3d⁰) are colourless.',
 'مکمل بھرے یا خالی d آربیٹل والے آئن بے رنگ ہیں، مثلاً Cu⁺(3d¹⁰)، Zn²⁺(3d¹⁰)، Sc³⁺(3d⁰) اور Ti⁴⁺(3d⁰) کے کمپلیکس بے رنگ ہیں۔',
 'په بشپړ ډول ډک یا تش d اوربیټالونه لرونکي ایونونه بې رنګه دي، لکه د Cu⁺(3d¹⁰)، Zn²⁺(3d¹⁰)، Sc³⁺(3d⁰) او Ti⁴⁺(3d⁰) کمپلېکسونه بې رنګه دي.')
add('Table 14.8 Colours and outer Electronic Configurations of Transition Metal Ions','جدول 14.8 عبوری دھاتی آئنوں کے رنگ اور بیرونی الیکٹرانی ترتیبیں','جدول 14.8 د انتقالي فلزي ایونونو رنګونه او بهرني الکتروني ترتیبونه')
rows=[['Sc³⁺','3d⁰','Colourless'],['Ti³⁺','3d¹','Purple'],['Ti⁴⁺','3d⁰','Colourless'],['V³⁺','3d²','Green'],['Cr³⁺','3d³','Violet'],['Mn²⁺','3d⁵','Light pink'],['Mn³⁺','3d⁴','Violet'],['Fe²⁺','3d⁶','Light yellow'],['Fe³⁺','3d⁵','Yellow']]
colors={'Colourless':('بے رنگ','بې رنګه'),'Purple':('جامنی','ارغواني'),'Green':('سبز','شین'),'Violet':('بنفشی','بنفشي'),'Light pink':('ہلکا گلابی','سپک ګلابي'),'Light yellow':('ہلکا پیلا','سپک ژېړ'),'Yellow':('پیلا','ژېړ')}
blocks.append({'id':'chem12-table14-8-first','headers':['Ion','Outer configuration','Colour'],'rows':rows,'translations':[{'language':lang,'headers':headers,'rows':[[r[0],r[1],colors[r[2]][n]] for r in rows]} for n,lang,headers in [(0,'اردو',['آئن','بیرونی ترتیب','رنگ']),(1,'پښتو',['ایون','بهرنی ترتیب','رنګ'])]]});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
record=section('14.10','Octahedral shapes and colour of complexes','آکٹاہیڈرل شکلیں اور کمپلیکسوں کا رنگ','اوکتاهېډرل شکلونه او د کمپلېکسونو رنګ',paras,layout,blocks,'62–63');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':35,'printedPages':[62,63]}];record['sourceContinuesOnPdfPage']=36
if __name__=='__main__':save(35,[record],trim=[{'id':'14.11','startsAt':'Co\n3d7'}],issues=[{'id':'chem12-p62-cobalt-charge','printedPage':62,'description':'Figure14.6 prints cobalt hexaammine as 2+. Retained; scientific review pending.'},{'id':'chem12-p62-complementary-colors','printedPage':62,'description':'Tidbit blue/yellow complement versus page63 blue/orange assertion retained as printed.'}],chapter_number=14)
