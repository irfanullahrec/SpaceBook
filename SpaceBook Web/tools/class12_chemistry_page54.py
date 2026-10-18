"""PDF54, printed100–101; full learning outcomes and hydrocarbon introduction."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
import math

paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
outcomes=[
('Describe the chemistry of alkenes by the following reactions of ethene i.e. hydrogenation, hydrohalogenation, hydration, halogenation, halohydration, epoxidation, ozonolysis and polymerization. (Understanding)','ایتھین کے درج ذیل تعاملات یعنی ہائیڈروجینیشن، ہائیڈروہیلوجینیشن، ہائیڈریشن، ہیلوجینیشن، ہیلوہائیڈریشن، ایپو آکسیڈیشن، اوزونولائسز اور پولیمرائزیشن سے الکینز کی کیمیا بیان کریں۔ (سمجھنا)','د ایتین د لاندې تعاملونو یعنې هایدروجنېشن، هایدروهالوجنېشن، هایدرېشن، هالوجنېشن، هالوهایدرېشن، ایپوکسیدېشن، اوزونولیز او پولیمریزېشن له لارې د الکینونو کیمیا بیان کړي. (پوهېدل)'),
('Explain the concept of conjugation in alkenes, having alternate double bonds. (Understanding)','باری باری دوہرے بند رکھنے والے الکینز میں کنجوگیشن کا تصور واضح کریں۔ (سمجھنا)','په هغو الکینونو کې چې نوبتي دوه ګوني تړونونه لري، د کنجوګېشن مفهوم روښانه کړي. (پوهېدل)'),
('Explain the shape of benzene molecule (Molecular Orbital Aspect). (Understanding)','بینزین کے سالمے کی شکل واضح کریں (سالماتی مدار کا پہلو)۔ (سمجھنا)','د بینزین د مالیکول شکل روښانه کړي (د مالیکولي اوربیټل له پلوه). (پوهېدل)'),
('Define resonance, resonance energy and relative stability. (Understanding)','ریزونینس، ریزونینس توانائی اور نسبتی استحکام کی تعریف کریں۔ (سمجھنا)','ریزونانس، د ریزونانس انرژي او نسبي ثبات تعریف کړي. (پوهېدل)'),
('Compare the reactivity of benzene with alkanes and alkenes. (Applying)','بینزین کی تعامل پذیری کا الکینز (یک بند) اور الکینز (دوہرے بند) سے موازنہ کریں۔ (اطلاق)','د بینزین تعامل وړتیا له الکانونو او الکینونو سره پرتله کړي. (تطبیق)'),
('Describe. what is meant by term delocalized electrons in the context of benzene ring. (Understanding)','بینزین حلقے کے تناظر میں غیر مقامی الیکٹرانوں کی اصطلاح سے کیا مراد ہے، بیان کریں۔ (سمجھنا)','د بینزین د کړۍ په تړاو د غیر موضعي الکترونونو د اصطلاح معنا بیان کړي. (پوهېدل)'),
('Describe addition reactions of benzene and methyl benzene. (Applying)','بینزین اور میتھائل بینزین کے اضافی تعاملات بیان کریں۔ (اطلاق)','د بینزین او میتایل بینزین د زیاتونې تعاملونه بیان کړي. (تطبیق)'),
('Describe the mechanism of electrophilic substitution in benzene. (Understanding)','بینزین میں الیکٹروفیلک تبادلے کا طریق کار بیان کریں۔ (سمجھنا)','په بینزین کې د الکتروفیلي تعویض میکانیزم بیان کړي. (پوهېدل)'),
('Discuss the chemistry of benzene and toluene by nitration, sulphonation, halogenations, Friedel-Craft’s alkylation and acylation. (Applying)','نائٹریشن، سلفونیشن، ہیلوجینیشن، فریڈل–کرافٹس الکائلیشن اور ایسیلیشن سے بینزین اور ٹولیون کی کیمیا پر بحث کریں۔ (اطلاق)','د نایټرېشن، سلفونېشن، هالوجنېشن، فریډل–کرافټس الکایلېشن او اسیلیشن له لارې د بینزین او ټولوین پر کیمیا بحث وکړي. (تطبیق)'),
('Apply the knowledge of positions of substituents in the electrophilic substitution of benzene. (Applying)','بینزین کے الیکٹروفیلک تبادلے میں متبادل گروہوں کے مقامات کے علم کا اطلاق کریں۔ (اطلاق)','د بینزین په الکتروفیلي تعویض کې د ځایناستو د موقعیتونو پوهه وکاروي. (تطبیق)'),
('Use the IUPAC naming system of alkynes. (Applying)','الکائنز کے لیے IUPAC نام گذاری کا نظام استعمال کریں۔ (اطلاق)','د الکاینونو د نومولو IUPAC سیستم وکاروي. (تطبیق)'),
('Compare the reactivity of alkynes with alkanes, alkenes and arenes. (Analyzing)','الکائنز کی تعامل پذیری کا الکینز (یک بند)، الکینز (دوہرے بند) اور ارینز سے موازنہ کریں۔ (تجزیہ)','د الکاینونو تعامل وړتیا له الکانونو، الکینونو او ارینونو سره پرتله کړي. (شننه)'),
('Discuss the shape of alkynes in terms of sigma and pi carbon-carbon bonds. (Applying)','سگما اور پائی کاربن–کاربن بندوں کے لحاظ سے الکائنز کی شکل پر بحث کریں۔ (اطلاق)','د سیګما او پای کاربن–کاربن تړونونو له مخې د الکاینونو پر شکل بحث وکړي. (تطبیق)'),
('Describe the preparation of alkynes, using elimination reactions. (Applying)','حذفی تعاملات سے الکائنز کی تیاری بیان کریں۔ (اطلاق)','د حذف تعاملونو په کارولو د الکاینونو چمتو کول بیان کړي. (تطبیق)'),
('Describe acidity of alkynes. (Understanding)','الکائنز کی تیزابی خاصیت بیان کریں۔ (سمجھنا)','د الکاینونو اسیدي خاصیت بیان کړي. (پوهېدل)'),
('Discuss the chemistry of alkynes by hydrogenation, hydrohalogenation, hydration, bromination, ozonolysis and reaction with metals. (Understanding)','ہائیڈروجینیشن، ہائیڈروہیلوجینیشن، ہائیڈریشن، برومینیشن، اوزونولائسز اور دھاتوں سے تعامل کے ذریعے الکائنز کی کیمیا پر بحث کریں۔ (سمجھنا)','د هایدروجنېشن، هایدروهالوجنېشن، هایدرېشن، برومینېشن، اوزونولیز او له فلزونو سره د تعامل له لارې د الکاینونو پر کیمیا بحث وکړي. (پوهېدل)'),
('Describe and differentiate between substitution and addition reactions. (Understanding)','تبادلے اور اضافے کے تعاملات بیان کریں اور ان میں فرق کریں۔ (سمجھنا)','د تعویض او زیاتونې تعاملونه بیان او توپیر یې وکړي. (پوهېدل)'),
('Explain isomerism in alkanes, alkenes, alkynes and substituted benzene. (Understanding)','الکینز (یک بند)، الکینز (دوہرے بند)، الکائنز اور متبادل گروہ والے بینزین میں آئسومرزم واضح کریں۔ (سمجھنا)','په الکانونو، الکینونو، الکاینونو او ځایناستي لرونکي بینزین کې ایزومېریزم روښانه کړي. (پوهېدل)')]
for row in outcomes:add(*row,'list')

def opening_diagrams(lang):
 bond={'en':'σ bond','ur':'σ بند','ps':'σ تړون'}[lang]
 s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 350" role="img" aria-label="Orbital overlap and mirror-related chiral centres"><rect width="720" height="350" fill="white"/>']
 def t(x,y,v,size=20):s.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#17202a">{escape(v)}</text>')
 def line(x,y,a,b,w=2):s.append(f'<path d="M{x},{y} L{a},{b}" stroke="#333" stroke-width="{w}" fill="none"/>')
 # The source shows a pair of overlapping p lobes above and below the axis.
 for x in [92,157]:
  s.append(f'<ellipse cx="{x}" cy="48" rx="23" ry="29" transform="rotate(20 {x} 48)" fill="#e72d73" fill-opacity=".75"/><ellipse cx="{x}" cy="103" rx="23" ry="29" transform="rotate(20 {x} 103)" fill="#e72d73" fill-opacity=".75"/>')
 s.append('<path d="M94 28 Q125 15 157 28 L157 68 Q125 82 94 68Z M94 82 Q125 72 157 82 L157 126 Q125 144 94 126Z" fill="#e72d73" fill-opacity=".45"/>')
 line(48,78,201,78);t(37,85,'H');t(211,85,'H');t(93,85,'C');t(157,85,'C');t(250,85,'=')
 for x,rx in [(321,39),(467,76),(614,39)]:s.append(f'<ellipse cx="{x}" cy="78" rx="{rx}" ry="26" fill="none" stroke="#222" stroke-width="2"/>');t(x,84,bond,17)
 for x,v in [(270,'H'),(378,'C'),(556,'C'),(665,'H')]:t(x,84,v)
 line(360,169,360,330,3)
 for center,mirror in [(242,1),(474,-1)]:
  items=[(center,191,'1','#81d5b9',7),(center-70*mirror,274,'2','#54d7ea',10),(center+30*mirror,309,'3','#f56ca9',12),(center+47*mirror,274,'4','#fae38b',4)]
  for x,y,label,color,width in items:
   line(center,251,x,y,width);s.append(f'<ellipse cx="{x}" cy="{y}" rx="18" ry="21" fill="{color}"/>');t(x,y+7,label)
  s.append(f'<circle cx="{center}" cy="251" r="24" fill="#333"/>');s.append(f'<text x="{center}" y="258" text-anchor="middle" font-size="21" fill="white">C*</text>')
 s.append('</svg>');return ''.join(s)
visual('chem12-p54-outcome-models',opening_diagrams)
add('Introduction','تعارف','سریزه','heading')
add('Hydrocarbons are the organic compounds which contain carbon and hydrogen only. For example methane (CH₄), ethylene (C₂H₄), acetylene (C₂H₂) benzene (C₆H₆) etc. These compounds are thought to serve as basis for all other organic compounds. That is, all other organic compounds are considered as the derivatives of hydrocarbons where one or more hydrogen atoms have been replaced by another atom or group of atoms.','ہائیڈروکاربن وہ نامیاتی مرکبات ہیں جن میں صرف کاربن اور ہائیڈروجن ہوتے ہیں۔ مثلاً میتھین (CH₄)، ایتھیلین (C₂H₄)، ایسیٹیلین (C₂H₂)، بینزین (C₆H₆) وغیرہ۔ ان مرکبات کو باقی تمام نامیاتی مرکبات کی بنیاد سمجھا جاتا ہے۔ یعنی باقی تمام نامیاتی مرکبات ہائیڈروکاربنوں کے مشتقات سمجھے جاتے ہیں، جن میں ایک یا زیادہ ہائیڈروجن ایٹموں کی جگہ کوئی دوسرا ایٹم یا ایٹموں کا گروہ آ گیا ہو۔','هایدروکاربنونه هغه عضوي مرکبات دي چې یوازې کاربن او هایدروجن لري. لکه میتان (CH₄)، ایتیلین (C₂H₄)، اسیتیلین (C₂H₂)، بینزین (C₆H₆) او نور. دا مرکبات د نورو ټولو عضوي مرکباتو بنسټ ګڼل کېږي. یعنې نور ټول عضوي مرکبات د هایدروکاربنونو مشتقات ګڼل کېږي چې یو یا څو هایدروجني اټومونه یې په بل اټوم یا د اټومونو په ډله بدل شوي وي.')
add('Petroleum, natural gas and coal are the main natural sources of hydrocarbons. These sources are frequently found in underground deposits. The significance of hydrocarbons can be realized by their uses in daily life and in industries and power generation as fuel and as raw materials for synthesis of many other organic compounds.','پٹرولیم، قدرتی گیس اور کوئلہ ہائیڈروکاربنوں کے بنیادی قدرتی ماخذ ہیں۔ یہ ماخذ اکثر زیر زمین ذخائر میں ملتے ہیں۔ روزمرہ زندگی، صنعتوں اور بجلی کی پیداوار میں ایندھن کے طور پر، اور بہت سے دوسرے نامیاتی مرکبات کی تیاری میں خام مال کے طور پر ان کے استعمال سے ہائیڈروکاربنوں کی اہمیت سمجھی جا سکتی ہے۔','پټرولیم، طبیعي ګاز او سکاره د هایدروکاربنونو مهمې طبیعي سرچینې دي. دا سرچینې ډېر ځله په ځمکلاندې زېرمو کې موندل کېږي. د هایدروکاربنونو اهمیت په ورځني ژوند، صنعتونو او د برېښنا په تولید کې د سون په توګه، او د ډېرو نورو عضوي مرکباتو د جوړولو لپاره د خامو موادو په توګه د دوی له کارونې څرګندېږي.')
add('16.1 Types of Hydrocarbons','16.1 ہائیڈروکاربنوں کی اقسام','16.1 د هایدروکاربنونو ډولونه','heading')
add('Hydrocarbons are divided into two major categories i.e. Aliphatic hydrocarbons and Aromatic hydrocarbons. This classification dates from the nineteenth century, when organic chemistry was almost exclusively devoted to the study of materials from natural sources and these terms were coined that reflected a substance’s origin.','ہائیڈروکاربن دو بڑی قسموں یعنی ایلیفیٹک ہائیڈروکاربن اور ارومیٹک ہائیڈروکاربن میں تقسیم ہیں۔ یہ درجہ بندی انیسویں صدی سے چلی آ رہی ہے، جب نامیاتی کیمیا تقریباً صرف قدرتی ماخذوں سے ملنے والے مادوں کے مطالعے کے لیے وقف تھی، اور یہ اصطلاحات وضع کی گئیں جو مادے کے ماخذ کی عکاسی کرتی تھیں۔','هایدروکاربنونه په دوو لویو ډلو، یعنې الیفاتیک هایدروکاربنونو او اروماتیک هایدروکاربنونو، وېشل کېږي. دا ډلبندي له نولسمې پېړۍ راهیسې ده، کله چې عضوي کیمیا نږدې یوازې د طبیعي سرچینو د موادو مطالعې ته ځانګړې وه او دا اصطلاحات جوړ شول چې د مادې سرچینه یې څرګندوله.')
add('1. Aliphatic Hydrocarbons','1. ایلیفیٹک ہائیڈروکاربن','1. الیفاتیک هایدروکاربنونه','heading')
add('The word aliphatic was derived from the Greek word aleiphar (fat), as these compounds were mostly derived from fats and oils. Aliphatic hydrocarbons are further classified into saturated and unsaturated hydrocarbons. In saturated hydrocarbons, the carbon atoms are joined to each other only by single bond. They include alkanes and cycloalkanes. Unsaturated hydrocarbons must contain a carbon-carbon multiple bond. They include, alkenes having carbon-carbon double bond and alkynes having carbon-carbon triple bond. These aliphatic hydrocarbons may be cyclic and open chain (acyclic). Examples of some aliphatic hydrocarbons are given below.','ایلیفیٹک لفظ یونانی لفظ aleiphar (چربی) سے نکلا ہے، کیونکہ یہ مرکبات زیادہ تر چربیوں اور تیلوں سے حاصل کیے جاتے تھے۔ ایلیفیٹک ہائیڈروکاربن مزید سیر شدہ اور غیر سیر شدہ ہائیڈروکاربنوں میں تقسیم ہوتے ہیں۔ سیر شدہ ہائیڈروکاربنوں میں کاربن ایٹم صرف یک بند سے ایک دوسرے کے ساتھ جڑے ہوتے ہیں۔ ان میں الکینز اور سائیکلوالکینز شامل ہیں۔ غیر سیر شدہ ہائیڈروکاربنوں میں کاربن–کاربن کثیر بند لازماً ہوتا ہے۔ ان میں کاربن–کاربن دوہرا بند رکھنے والے الکینز اور کاربن–کاربن تہرا بند رکھنے والے الکائنز شامل ہیں۔ یہ ایلیفیٹک ہائیڈروکاربن حلقوی یا کھلی زنجیر والے (غیر حلقوی) ہو سکتے ہیں۔ بعض ایلیفیٹک ہائیڈروکاربنوں کی مثالیں ذیل میں ہیں۔','الیفاتیک کلمه له یوناني aleiphar (وازده) څخه اخیستل شوې، ځکه دا مرکبات تر ډېره له وازدو او غوړیو ترلاسه کېدل. الیفاتیک هایدروکاربنونه بیا په مشبوع او غیر مشبوع هایدروکاربنونو وېشل کېږي. په مشبوع هایدروکاربنونو کې کاربني اټومونه یوازې په یو ګوني تړون یو له بل سره نښتي وي. الکانونه او سایکلوالکانونه پکې شامل دي. غیر مشبوع هایدروکاربنونه باید کاربن–کاربن څوګونی تړون ولري. په دوی کې د کاربن–کاربن دوه ګونی تړون لرونکي الکینونه او د کاربن–کاربن درې ګونی تړون لرونکي الکاینونه شامل دي. دا الیفاتیک هایدروکاربنونه کړیز او د پرانیستې ځنځیر (غیر کړیز) کېدای شي. لاندې د ځینو الیفاتیک هایدروکاربنونو بېلګې ورکړل شوې دي.')

def structures(lang,unsaturated=False):
 names={'en':['ethane','propane','cyclobutane','ethene','propene','cyclobutene','cyclohexene'],'ur':['ایتھین','پروپین','سائیکلوبیوٹین','ایتھین (دوہرا بند)','پروپین (دوہرا بند)','سائیکلوبیوٹین (دوہرا بند)','سائیکلوہیکسین'],'ps':['ایتان','پروپان','سایکلوبیوټان','ایتین','پروپین','سایکلوبیوټین','سایکلوهیکسین']}[lang]
 s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 210" role="img" aria-label="Hydrocarbon structural formulae"><rect width="850" height="210" fill="white"/>']
 def t(x,y,v,sz=22):s.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{sz}" fill="#111">{escape(v)}</text>')
 def ring(cx,cy,n,labels,double=None):
  if n==4:pts=[(cx-37,cy-32),(cx+37,cy-32),(cx+37,cy+32),(cx-37,cy+32)]
  else:pts=[(cx+54*math.cos(-math.pi/2+i*math.pi/3),cy+54*math.sin(-math.pi/2+i*math.pi/3)) for i in range(6)]
  for i,((x,y),(a,b)) in enumerate(zip(pts,pts[1:]+pts[:1])):
   dx=a-x;dy=b-y;L=math.hypot(dx,dy);ux=dx/L;uy=dy/L
   for off in ([-3,3] if i==double else [0]):s.append(f'<path d="M{x+ux*20-uy*off},{y+uy*14+ux*off} L{a-ux*20-uy*off},{b-uy*14+ux*off}" stroke="#222" stroke-width="2"/>')
  for (x,y),v in zip(pts,labels):t(x,y+6,v,19)
 if not unsaturated:
  t(125,110,'CH₃—CH₃');t(125,175,names[0],18);t(380,110,'CH₃—CH₂—CH₃');t(380,175,names[1],18);ring(680,88,4,['CH₂']*4);t(680,175,names[2],18)
 else:
  t(95,110,'CH₂=CH₂');t(95,185,names[3],17);t(305,110,'H₃C—CH=CH₂');t(305,185,names[4],17);ring(510,88,4,['CH₂','CH₂','CH','CH'],2);t(510,185,names[5],16);ring(738,88,6,['CH₂','CH','CH','CH₂','CH₂','CH₂'],1);t(738,185,names[6],17)
 return ''.join(s)+'</svg>'
add('Alkanes and Cycloalkanes','الکینز اور سائیکلوالکینز','الکانونه او سایکلوالکانونه','heading');visual('chem12-p54-alkanes',lambda l:structures(l))
add('Alkenes and Cycloalkenes','الکینز (دوہرے بند) اور سائیکلوالکینز','الکینونه او سایکلوالکینونه','heading');visual('chem12-p54-alkenes',lambda l:structures(l,True))
record=section('16.1','Learning outcomes, introduction and hydrocarbon types','تعلیمی نتائج، تعارف اور ہائیڈروکاربنوں کی اقسام','د زده کړې پایلې، سریزه او د هایدروکاربنونو ډولونه',paras,layout,blocks,'100–101')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':54,'printedPages':[100,101]}]
if __name__=='__main__':save(54,[record],trim=[{'id':'16.2','startsAt':'Alkynes and Cycloalkynes'}],chapter_number=16)
