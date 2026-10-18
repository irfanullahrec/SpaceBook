"""PDF147 printed288–289: effect of pH (Figure 21.4), enzyme inhibition — irreversible, reversible (competitive Figure 21.5, non-competitive Figure 21.6)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow147');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Optimum pH':('موزوں ترین pH','غوره pH'),'Increasing enzyme activity':('خامرے کی بڑھتی سرگرمی','د انزایم زیاتېدونکی فعالیت'),'enzyme':('خامرہ','انزایم'),'substrate':('سبسٹریٹ','سبسټرېټ'),'inhibitor':('روکنے والا','مخنیوونکی'),
   'enzyme-inhibitor':('خامرہ–روکنے والا','انزایم–مخنیوونکی'),'complex':('کمپلیکس','کمپلېکس'),'NO REACTION':('کوئی تعامل نہیں','هېڅ تعامل نشته'),'inhibitor binds to':('روکنے والا جڑتا ہے','مخنیوونکی نښلي'),
   'the active site':('فعال مقام سے','له فعال ځای سره'),'the allosteric site':('ایلوسٹیرک مقام سے','له الوسټېریک ځای سره'),'Directly blocks':('براہِ راست روکتا ہے','مستقیم بندوي'),'Changes the shape':('شکل بدل دیتا ہے','بڼه بدلوي'),'of the active site':('فعال مقام کی','د فعال ځای')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def phgraph(lang):
 X=lambda p:200+(p-4)*60;Y=lambda r:300-r*2.3
 s=F.start(370)
 for p in range(4,12):s+=line(X(p),Y(0),X(p),Y(100),0.6,'#bbb')
 for r in range(0,101,12):s+=line(X(4),Y(r),X(11.5),Y(r),0.6,'#bbb')
 s+=line(X(4),Y(0),X(11.5),Y(0),2)+line(X(4),Y(0),X(4),Y(105),2)
 for p in range(4,12):s+=t(X(p),Y(0)+20,str(p),12)
 pts=[f'{X(p/20):.1f},{Y(max(0,100*(1-((p/20-8)/(3.3 if p/20<8 else 3))**2))):.1f}' for p in range(94,221)]
 s+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="#1976d2" stroke-width="2.5"/>'+line(X(8),Y(0),X(8),Y(108),1.5,'#222','stroke-dasharray="3 4"')
 s+=f'<rect x="{X(8)-60}" y="6" width="120" height="24" fill="#fce4ec" stroke="#c2185b"/>'+t(X(8),23,lb(lang,'Optimum pH'),12)
 s+=f'<text x="{X(4)-30}" y="{Y(50)}" transform="rotate(-90 {X(4)-30} {Y(50)})" text-anchor="middle" font-family="Arial" font-size="13" fill="#ad1457">{lb(lang,"Increasing enzyme activity")}</text>'+t(X(8),Y(0)+45,'pH',13,'#ad1457')
 return s+'</svg>'
def pac(x,y,c='#a1887f',notch='tri'):
 """Enzyme as a disc with a wedge-shaped active site."""
 return f'<path d="M{x} {y} L{x+30} {y-14} A32 32 0 1 0 {x+30} {y+14} Z" fill="{c}" stroke="#555" transform="translate(-6 0)"/>'
def inhib(lang,allo=False):
 s=F.start(200)+pac(80,90)+t(80,150,lb(lang,'enzyme'),12)+t(140,96,'+',20)
 s+='<path d="M190 70 a16 16 0 1 1 20 0 l-10 36 z" fill="#fdd835" stroke="#9e9d24"/>'+t(200,150,lb(lang,'substrate'),12)+t(250,96,'+',20)
 s+=('<circle cx="300" cy="90" r="16" fill="#1e88e5"/>' if allo else '<path d="M286 70 l28 0 l0 18 l-14 22 l-14 -22 z" fill="#2e7d32"/>')+t(300,150,lb(lang,'inhibitor'),12)
 s+=F.arrow(350,420,90)+pac(500,95)
 s+=('<circle cx="476" cy="120" r="14" fill="#1e88e5"/><path d="M495 30 a14 14 0 1 1 18 0 l-9 30 z" fill="#c0ca33"/>' if allo else '<path d="M512 80 l26 0 l0 16 l-13 18 l-13 -18 z" fill="#2e7d32"/><path d="M470 20 a14 14 0 1 1 18 0 l-9 30 z" fill="#c0ca33"/>')
 s+=t(500,150,lb(lang,'enzyme-inhibitor'),12)+t(500,166,lb(lang,'complex'),12)+F.arrow(570,640,90)
 s+='<circle cx="700" cy="90" r="28" fill="#fff" stroke="#c62828" stroke-width="5"/>'+line(680,110,720,70,4,'#c62828')+t(700,86,'NO',10,'#c62828')+t(700,100,'REACTION',8,'#c62828')
 s+=t(720,30,lb(lang,'inhibitor binds to'),11)+t(720,44,lb(lang,'the allosteric site' if allo else 'the active site'),11)
 s+=t(700,146,lb(lang,'Changes the shape' if allo else 'Directly blocks'),11,'#555')+t(700,160,lb(lang,'of the active site' if allo else 'the active site'),11,'#555')
 return s+'</svg>'

add('2. pH','2. pH','2. pH','heading')
add('Enzyme activity is also effected by pH. Some enzymes work best in alkaline pH while others in acidic pH. As the pH is decreased or increased, the nature of the various acid and amino groups on the side chains is altered, which results in change in the overall shape and structure of the enzyme.','خامرے کی سرگرمی pH سے بھی متاثر ہوتی ہے۔ بعض خامرے اساسی pH میں بہترین کام کرتے ہیں جبکہ دوسرے تیزابی pH میں۔ pH کم یا زیادہ ہونے پر ضمنی زنجیروں پر موجود مختلف تیزابی اور امائنو گروپوں کی نوعیت بدل جاتی ہے، جس کے نتیجے میں خامرے کی مجموعی شکل اور ساخت بدل جاتی ہے۔','د انزایم فعالیت د pH په واسطه هم اغېزمنېږي. ځینې انزایمونه په قلوي pH کې ښه کار کوي او نور په اسیدي pH کې. کله چې pH کم یا زیات شي، پر څنګیزو ځنځیرونو د بېلابېلو اسیدي او امینو ګروپونو طبیعت بدلېږي، چې پایله یې د انزایم په ټوله بڼه او جوړښت کې بدلون دی.')
add('Each enzyme has a pH at which it shows the maximum activity. This pH is called optimum pH. For example, the optimum pH of pepsin is around 2.0 while that of trypsin varies from 8 – 9 pH. The pH below which the enzyme loses its activity and at which the enzymes shows the lowest activity is called minimum pH. Most of the enzymes have optimum activities in the range 5–9 pH. Pepsin is an exception to this rules.','ہر خامرے کا ایک pH ہوتا ہے جس پر وہ زیادہ سے زیادہ سرگرمی دکھاتا ہے۔ اس pH کو موزوں ترین pH کہتے ہیں۔ مثلاً پیپسن کا موزوں ترین pH تقریباً 2.0 ہے جبکہ ٹرپسن کا 8 – 9 pH کے درمیان ہے۔ وہ pH جس سے نیچے خامرہ اپنی سرگرمی کھو دیتا ہے اور جس پر خامرہ سب سے کم سرگرمی دکھاتا ہے، کم سے کم pH کہلاتا ہے۔ زیادہ تر خامروں کی موزوں ترین سرگرمیاں 5–9 pH کی حد میں ہیں۔ پیپسن اس اصول سے مستثنیٰ ہے۔','هر انزایم یو pH لري چې پکې اعظمي فعالیت ښيي. دې pH ته غوره pH وايي. د بېلګې په توګه د پېپسین غوره pH نږدې 2.0 دی، په داسې حال کې چې د ټرپسین له 8 – 9 pH پورې دی. هغه pH چې له هغه ښکته انزایم خپل فعالیت له لاسه ورکوي او پکې تر ټولو لږ فعالیت ښيي، لږترلږه pH بلل کېږي. ډېری انزایمونه د 5–9 pH په پوله کې غوره فعالیت لري. پېپسین له دې قاعدې استثنا دی.')
add('Plotting a graph between enzyme activity and pH, we get a curve as shown in the Figure 21.4.','خامرے کی سرگرمی اور pH کے درمیان گراف بنانے پر شکل 21.4 جیسا خم حاصل ہوتا ہے۔','د انزایم د فعالیت او pH ترمنځ د ګراف په رسمولو، هغه منحني لاسته راځي چې په شکل 21.4 کې ښودل شوې.')
visual('chem12-figure21-4',phgraph)
add('Figure 21.4 Effect of pH on enzyme.','شکل 21.4 خامرے پر pH کا اثر۔','شکل 21.4 پر انزایم د pH اغېز.')
add('Enzyme Inhibition','خامروں کی روک تھام','د انزایم مخنیوی','heading')
add('The process by which the activity of an enzyme is decreased or inhibited by the addition of certain substances to the reaction is called enzyme inhibition. The different substance, which inhibit the activity of enzymes, are known as inhibitors. Poisons and drugs are examples of enzyme inhibitors. According to the similarity between the inhibitor and the substrate, enzyme inhibition is classified into:','وہ عمل جس میں تعامل میں بعض مادے شامل کرنے سے خامرے کی سرگرمی کم یا روک دی جاتی ہے، خامروں کی روک تھام کہلاتا ہے۔ وہ مختلف مادے جو خامروں کی سرگرمی روکتے ہیں، روکنے والے (انہیبیٹرز) کہلاتے ہیں۔ زہر اور ادویات خامروں کو روکنے والوں کی مثالیں ہیں۔ روکنے والے اور سبسٹریٹ کی مشابہت کے مطابق خامروں کی روک تھام کی درجہ بندی یہ ہے:','هغه عملیه چې پکې تعامل ته د ځینو موادو په زیاتولو د انزایم فعالیت کمېږي یا مخنیوی یې کېږي، د انزایم مخنیوی بلل کېږي. هغه بېلابېل مواد چې د انزایمونو د فعالیت مخه نیسي، مخنیوونکي بلل کېږي. زهر او درمل د انزایم د مخنیوونکو بېلګې دي. د مخنیوونکي او سبسټرېټ ترمنځ د ورته والي له مخې د انزایم مخنیوی داسې ډلبندي کېږي:')
add('i. Irreversible Inhibition','i. ناقابلِ واپسی روک تھام','i. نه بېرته ګرځېدونکی مخنیوی','heading')
add('When the inhibitor reacts and form a strong covalent bond with the active site of the enzyme then it termed as irreversible inhibition. The inhibitors forms a stable and irreversible complex with the enzyme. This complex cannot be broken down by physical or chemical methods to restore the active form of the enzyme.','جب روکنے والا خامرے کے فعال مقام سے تعامل کر کے مضبوط شریک گرفتی بند بناتا ہے تو اسے ناقابلِ واپسی روک تھام کہتے ہیں۔ روکنے والے خامرے کے ساتھ پائیدار اور ناقابلِ واپسی کمپلیکس بناتے ہیں۔ اس کمپلیکس کو خامرے کی فعال صورت بحال کرنے کے لیے طبعی یا کیمیائی طریقوں سے توڑا نہیں جا سکتا۔','کله چې مخنیوونکی د انزایم له فعال ځای سره تعامل وکړي او قوي کوولانټ تړون جوړ کړي، نو دې ته نه بېرته ګرځېدونکی مخنیوی وايي. مخنیوونکي له انزایم سره ثابت او نه بېرته ګرځېدونکی کمپلېکس جوړوي. دا کمپلېکس د انزایم د فعالې بڼې د بېرته راګرځولو لپاره په فزیکي یا کیمیاوي طریقو نه شي ماتېدای.')
add('ii. Reversible Inhibition','ii. قابلِ واپسی روک تھام','ii. بېرته ګرځېدونکی مخنیوی','heading')
add('It is a temporary type of inhibition. In this inhibition the inhibitor binds non-covalently (weak interaction) with enzyme. If inhibitor is removed, the action of enzyme is fully restored. The activity of enzyme is fully restored on removing the inhibitor by dialysis. It is sub-divided into,','یہ عارضی قسم کی روک تھام ہے۔ اس میں روکنے والا خامرے سے غیر شریک گرفتی (کمزور تعامل) طور پر جڑتا ہے۔ روکنے والے کو ہٹانے پر خامرے کا عمل مکمل بحال ہو جاتا ہے۔ ڈائیلائسز سے روکنے والے کو ہٹانے پر خامرے کی سرگرمی مکمل بحال ہو جاتی ہے۔ اس کی ذیلی تقسیم یہ ہے،','دا یو لنډمهاله ډول مخنیوی دی. په دې مخنیوي کې مخنیوونکی له انزایم سره غیر کوولانټ (کمزوری تعامل) نښلي. که مخنیوونکی لرې شي، د انزایم عمل بشپړ بېرته راګرځي. د ډیالیسس په واسطه د مخنیوونکي په لرې کولو د انزایم فعالیت بشپړ بېرته راګرځي. دا په لاندې ډول وېشل کېږي،')
add('(a). Competitive Inhibition','(a). مسابقتی روک تھام','(a). سیالي لرونکی مخنیوی','heading')
lines([('A competitive inhibitor has structural similarities to the normal substrate for the enzyme.','مسابقتی روکنے والا خامرے کے عام سبسٹریٹ سے ساختی مشابہت رکھتا ہے۔','سیالي لرونکی مخنیوونکی د انزایم له عادي سبسټرېټ سره جوړښتي ورته والی لري.'),
 ('Competitive inhibitors compete with the substrate for the active site of the enzyme and form an enzyme inhibitor complex.','مسابقتی روکنے والے خامرے کے فعال مقام کے لیے سبسٹریٹ سے مقابلہ کرتے ہیں اور خامرہ–روکنے والا کمپلیکس بناتے ہیں۔','سیالي لرونکي مخنیوونکي د انزایم د فعال ځای لپاره له سبسټرېټ سره سیالي کوي او د انزایم–مخنیوونکي کمپلېکس جوړوي.'),
 ('The inhibitor binds to the same active sites of enzymes to which the actual substrate binds. By this way, the active sites of the enzyme are blocked and then the substrate is unable to bind to the enzyme.','روکنے والا خامرے کے انہی فعال مقامات سے جڑتا ہے جن سے اصل سبسٹریٹ جڑتا ہے۔ اس طرح خامرے کے فعال مقامات بند ہو جاتے ہیں اور سبسٹریٹ خامرے سے نہیں جڑ پاتا۔','مخنیوونکی د انزایم له همغو فعالو ځایونو سره نښلي چې اصلي سبسټرېټ ورسره نښلي. په دې توګه د انزایم فعال ځایونه بندېږي او بیا سبسټرېټ له انزایم سره نه شي نښلېدای.')])
visual('chem12-figure21-5',lambda l:inhib(l,False))
add('Figure 21.5 Competitive inhibition.','شکل 21.5 مسابقتی روک تھام۔','شکل 21.5 سیالي لرونکی مخنیوی.')
add('(b). Non-Competitive Inhibition','(b). غیر مسابقتی روک تھام','(b). بې سیالۍ مخنیوی','heading')
lines([('The inhibitor has no structural resemblance with the substrate of the enzyme.','روکنے والے کی خامرے کے سبسٹریٹ سے کوئی ساختی مشابہت نہیں ہوتی۔','مخنیوونکی د انزایم له سبسټرېټ سره هېڅ جوړښتي ورته والی نه لري.'),
 ('They do not compete with the substrate for the active sites of the enzyme.','یہ خامرے کے فعال مقامات کے لیے سبسٹریٹ سے مقابلہ نہیں کرتے۔','دوی د انزایم د فعالو ځایونو لپاره له سبسټرېټ سره سیالي نه کوي.'),
 ('The inhibitor does not bind to the active sites of enzyme.','روکنے والا خامرے کے فعال مقامات سے نہیں جڑتا۔','مخنیوونکی د انزایم له فعالو ځایونو سره نه نښلي.'),
 ('Inhibitor binds to the site other than active sites of the enzyme, to form enzyme – substrate inhibitor complex.','روکنے والا خامرے کے فعال مقامات کے علاوہ کسی دوسرے مقام سے جڑ کر خامرہ – سبسٹریٹ روکنے والا کمپلیکس بناتا ہے۔','مخنیوونکی د انزایم له فعالو ځایونو پرته له بل ځای سره نښلي او د انزایم – سبسټرېټ مخنیوونکي کمپلېکس جوړوي.')])
visual('chem12-figure21-6',lambda l:inhib(l,True))
add('Figure 21.6 Non-Competitive inhibition.','شکل 21.6 غیر مسابقتی روک تھام۔','شکل 21.6 بې سیالۍ مخنیوی.')
record=section('21.9','Effect of pH and enzyme inhibition','pH کا اثر اور خامروں کی روک تھام','د pH اغېز او د انزایم مخنیوی',paras,layout,blocks,'288–289')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':147,'printedPages':[288,289]}]
record['sourceContinuesOnPdfPage']=148
record['sourceIllustrationReview']='Figures 21.5–21.6 pictorial enzyme/substrate/inhibitor artwork re-drawn as labelled schematic SVG.'
carry=[{'from':'21.9','to':'21.10','startsAt':'Uncompetitive Inhibition'}]
if __name__=='__main__':save(147,[record],carry=carry,chapter_number=21)
