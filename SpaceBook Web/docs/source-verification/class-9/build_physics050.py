from physics_page_tools import *

p=[
pair('slope of speed time graph will give magnitude of acceleration which can be written as','رفتار وقت گراف کی ڈھال تعجیل کی مقدار دے گی جسے یوں لکھ سکتے ہیں۔','چټکتیا او وخت ګراف میلان به د تعجیل اندازه ورکړي، چې داسې لیکل کېدای شي.'),
pair('Figure 2.11 Speed Time Graph Slope','شکل 2.11 رفتار وقت گراف کی ڈھال','شکل 2.11 د چټکتیا او وخت ګراف میلان'),
pair('Since acceleration is change in velocity with respect to time. Therefore change in speed with respect to time will only give magnitude of acceleration.','چونکہ تعجیل وقت کے لحاظ سے سمتی رفتار میں تبدیلی ہے۔ اس لیے وقت کے لحاظ سے رفتار کی تبدیلی صرف تعجیل کی مقدار دے گی۔','ځکه تعجیل د وخت په نسبت په سرعت کې بدلون دی. نو د وخت په نسبت د چټکتیا بدلون به یوازې د تعجیل اندازه ورکړي.'),
pair('B) Area under speed time graphs represent the distance traveled:','B) رفتار وقت گرافوں کے نیچے کا رقبہ طے کردہ فاصلہ ظاہر کرتا ہے:','B) د چټکتیا او وخت ګرافونو لاندې مساحت وهل شوی واټن ښيي:'),
pair('When we speak of the area under a graph, we are not talking about the literal number of square centimeters of paper but the quantities under discussion. From equation 2.1 the speed is defined as','گراف کے نیچے رقبے کی بات سے ہماری مراد کاغذ کے مربع سینٹی میٹروں کی لفظی تعداد نہیں، بلکہ زیرِ بحث مقداریں ہیں۔ مساوات 2.1 میں رفتار یوں بیان ہوئی ہے۔','کله چې د ګراف لاندې مساحت یادوو، د کاغذ د مربع سانتي مترو لفظي شمېر نه، بلکې تر بحث لاندې کمیتونه مو مطلب دي. د 2.1 معادلې له مخې چټکتیا داسې تعریف شوې ده.'),
pair('Figure 2.12 Speed Time Graph Area','شکل 2.12 رفتار وقت گراف کا رقبہ','شکل 2.12 د چټکتیا او وخت ګراف مساحت'),
pair('The above equation can be written as','اوپر کی مساوات یوں لکھی جا سکتی ہے۔','پورتنۍ معادله داسې لیکل کېدای شي.'),
pair('This quantity in speed-time graph is represented as area under the curve. For example if we want to calculate the area of rectangular shaded region for the speed time graph of an object in motion as shown in figure 2.12. The area ‘A’ of rectangle mathematically is length ‘l’ into width ‘w’.','رفتار وقت گراف میں یہ مقدار منحنی کے نیچے رقبے سے ظاہر ہوتی ہے۔ مثلاً اگر شکل 2.12 میں متحرک شے کے رفتار وقت گراف کے مستطیل سایہ دار حصے کا رقبہ معلوم کرنا ہو۔ مستطیل کا رقبہ ‘A’ ریاضیاتی طور پر لمبائی ‘l’ ضرب چوڑائی ‘w’ ہے۔','د چټکتیا او وخت په ګراف کې دا کمیت د منحني لاندې مساحت په توګه ښودل کېږي. د بېلګې په توګه، که د شکل 2.12 له مخې د یوه خوځېدونکي شي د چټکتیا او وخت ګراف د مستطیل سیوري شوې برخې مساحت محاسبه کول وغواړو. د مستطیل مساحت ‘A’ په ریاضي کې اوږدوالی ‘l’ ضرب پلنوالی ‘w’ دی.'),
pair('putting values from graph','گراف کی قدریں رکھنے سے','له ګراف څخه د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو')]

def chart(shade=False):
 g='<rect x="9" y="10" width="335" height="306" fill="#fff"/>'
 for x in range(9,345,15):g+=f'<path d="M{x} 10V316" stroke="#bba8b3" stroke-width=".8"/>'
 for y in range(10,317,15):g+=f'<path d="M9 {y}H344" stroke="#bba8b3" stroke-width=".8"/>'
 if shade:g+='<rect x="83" y="102" width="132" height="120" fill="#e1dea7" fill-opacity=".55"/>'
 g+='<path d="M83 50V252M83 222H277" stroke="#222" stroke-width="2"/><path d="M83 50l-6 12h12Z M277 222l-12 -6v12Z" fill="#29315c"/><path d="M83 102H215V222" fill="none" stroke="#111" stroke-dasharray="4 4" stroke-width="3"/>'
 g+=f'<path d="M83 {102 if shade else 222}L215 102" stroke="#284751" stroke-width="5"/>'
 g+='<path d="M43 102V222M37 102h12M37 222h12M83 269H215M83 261v16M215 261v16" stroke="#29315c" stroke-width="2"/>'
 g+=text('speed',85,33,'middle',20)+text('v (ms⁻¹)',86,53,'middle',20)+text('time',290,203,'middle',19)+text('t (s)',291,224,'middle',19)+text('Δv',31,166,'middle',19)+text('Δt',149,293,'middle',19)+text('0',72,243,'middle',18)
 for i in range(1,6):
  xx=83+i*33
  g+=f'<path d="M{xx} 216v12" stroke="#9d2b34" stroke-width="3"/>'+text(str(i),xx,249,'middle',18)
  yy=222-i*30
  g+=f'<path d="M77 {yy}h12" stroke="#29315c" stroke-width="3"/>'+text(str(i*2),66,yy+7,'middle',18)
 return g

charts=[]
for n,sh in [(211,False),(212,True)]:
 b=chart(sh)
 c=block(f'physics9-speed-time-figure{n}',b,w=353,h=327,ratio=.49,label='Figure2.11 speed-time line from0s0ms-1 to4s8ms-1' if not sh else 'Figure2.12 shaded rectangle under constant8ms-1 line from0 to4 seconds; source delta-v vertical bracket retained',ur=b.replace('speed','رفتار').replace('>time<','>وقت<'),ps=b.replace('speed','چټکتیا').replace('>time<','>وخت<'),kind='graph')
 c['graphData']=dict(xAxis=dict(quantity='time',unit='s',ticks=[0,1,2,3,4,5]),yAxis=dict(quantity='speed',unit='ms⁻¹',ticks=[0,2,4,6,8,10]),points=[[0,8 if sh else 0],[4,8]],shadedArea=[[0,0],[0,8],[4,8],[4,0]] if sh else None,sourceDeltaVBracket=8,sourceDeltaTBracket=4)
 charts.append(c)
f=block('physics9-speed-time-acceleration-slope',text('slope =',5,65)+frac('Δv','Δt',125,45)+text('=',190,65)+frac(sub('v⃗','f')+' − '+sub('v','i'),sub('t','f')+' − '+sub('t','i'),231,130),w=410,ratio=.43,ur=(text('ڈھال =',5,65)+frac('Δv','Δt',125,45)+text('=',190,65)+frac(sub('v⃗','f')+' − '+sub('v','i'),sub('t','f')+' − '+sub('t','i'),231,130)),ps=(text('میلان =',5,65)+frac('Δv','Δt',125,45)+text('=',190,65)+frac(sub('v⃗','f')+' − '+sub('v','i'),sub('t','f')+' − '+sub('t','i'),231,130)))
b=text('Magnitude of acceleration |a| =',5,65)+frac('8 ms⁻¹ − 0 ms⁻¹','4 s − 0 s',455,200)+text('=',675,65)+frac('8 ms⁻¹','4 s',715,110)+text('= 2 ms⁻²',845,65)
mag=block('physics9-acceleration-magnitude-graph',b,w=1005,ratio=.98,ur=b.replace('Magnitude of acceleration','تعجیل کی مقدار'),ps=b.replace('Magnitude of acceleration','د تعجیل اندازه'))
b=text('speed =',5,65)+frac('distance','elapsed time',120,165)+text('or',323,65)+text('v =',390,65)+frac('Δs','Δt',466,45)
speed=block('physics9-graph-area-speed-formula',b,w=550,ratio=.55,ur=b.replace('speed','رفتار').replace('distance','فاصلہ').replace('elapsed time','گزرا وقت').replace('>or<','>یا<'),ps=b.replace('speed','چټکتیا').replace('distance','واټن').replace('elapsed time','تېر شوی وخت').replace('>or<','>یا<'))
b=text('distance = speed × elapsed time',5,37)+text('or',18,87)+text('Δs = v × Δt',80,87)+number('2.11',390,61)
dist=block('physics9-distance-equation211',b,w=500,h=120,ratio=.55,label='Equation2.11 distance equals speed times elapsed time; delta s equals v times delta t',ur=b.replace('distance','فاصلہ').replace('speed','رفتار').replace('elapsed time','گزرا وقت').replace('>or<','>یا<'),ps=b.replace('distance','واټن').replace('speed','چټکتیا').replace('elapsed time','تېر شوی وخت').replace('>or<','>یا<'))
b=text('Area = length × width',5,42)+text('or  A = l × w',355,42)+text('or  A = Δt × Δv = Δv × Δt',590,42)
area=block('physics9-graph-rectangle-area-formula',b,w=1015,h=80,ratio=.98,ur=b.replace('Area','رقبہ').replace('length','لمبائی').replace('width','چوڑائی').replace('or','یا'),ps=b.replace('Area','مساحت').replace('length','اوږدوالی').replace('width','پلنوالی').replace('or','یا'))
b=text('A = (8 − 0) ms⁻¹ × (4 − 0) s',5,65)+text('or  A =',495,65)+frac('8 m','s',610,70)+text('× 4 s',700,65)
val=block('physics9-graph-rectangle-area-values',b,w=810,ratio=.81,ur=b.replace('or','یا'),ps=b.replace('or','یا'))
answer=block('physics9-graph-rectangle-area-answer',text('A = 32 m',8,43),w=180,h=75,ratio=.21)
s=section('2.4.2','2.4.2 SPEED - TIME GRAPH','2.4.2 رفتار وقت گراف','2.4.2 د چټکتیا او وخت ګراف',p,[f,*charts,mag,speed,dist,area,val,answer],[para(0),visual(f),para(1,'heading'),visual(charts[0]),para(2),visual(mag),para(3,'heading'),para(4),visual(speed),para(5,'heading'),visual(charts[1]),para(6),visual(dist),para(7),visual(area),para(8),visual(val),para(9),visual(answer)])
s['continuesPreviousParagraph']=True
save(50,'Speed-time slope Figure2.11 / rectangle area Figure2.12 / equation2.11',[s],'Fresh visible PDF inspection. Source continuation joined to page49 paragraph. Preserved slope/change-in-speed explanation and all fractions. Native graph2.11 matches0–5s/0–10ms⁻¹ axes and(4,8) endpoint; graph2.12 preserves constant8ms⁻¹ rectangular shading through4s and printed Δv bracket. Reconstructed speed/distance equation2.11, complete area derivation and32m result with explicit source translations and scaled coded labels.')
