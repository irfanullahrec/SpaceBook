from physics_page_tools import *

p=[
pair('ACTIVITY SPEED- TIME GRAPH','سرگرمی رفتار وقت گراف','فعالیت د چټکتیا او وخت ګراف'),
pair('What does the slope of these graphs tells about magnitude of acceleration?','ان گرافوں کی ڈھال تعجیل کی مقدار کے بارے میں کیا بتاتی ہے؟','د دې ګرافونو میلان د تعجیل د اندازې په اړه څه وايي؟'),
pair('Example 2.4 GRAPHICAL ANALYSIS OF CAR’S SPEED','مثال 2.4 گاڑی کی رفتار کا گرافی تجزیہ','بېلګه 2.4 د موټر د چټکتیا ګرافیکي تحلیل'),
pair('A car increases its speed from ZERO to a 25 ms⁻¹ in 10 s. Then it moves with uniform speed for the next 30 seconds and then the driver apply brakes and the speed of the car decreases uniformly to ZERO in the next 5 seconds. The graph is plotted for the journey, use this graph to calculate:','گاڑی اپنی رفتار صفر سے 10 s میں 25 ms⁻¹ تک بڑھاتی ہے۔ پھر اگلے 30 سیکنڈ یکساں رفتار سے چلتی ہے، اور ڈرائیور بریک لگاتا ہے تو اگلے 5 سیکنڈ میں رفتار یکساں طور پر صفر تک کم ہوتی ہے۔ سفر کا گراف بنایا گیا ہے؛ اس سے معلوم کریں:','یو موټر خپله چټکتیا په 10 s کې له صفر څخه 25 ms⁻¹ ته زیاتوي. بیا راتلونکې 30 ثانیې په یوشان چټکتیا ځي او وروسته چلوونکی بریک وهي، نو د موټر چټکتیا په راتلونکو 5 ثانیو کې په یوشان ډول صفر ته کمېږي. د سفر ګراف رسم شوی؛ له دې ګرافه محاسبه کړئ:'),
pair('a. magnitude of acceleration (i) in first 10 s. (ii) from 10 s to 40 s and (iii) in last 5 seconds.','a. تعجیل کی مقدار (i) پہلے 10 s میں، (ii) 10 s سے 40 s تک، اور (iii) آخری 5 سیکنڈ میں۔','a. د تعجیل اندازه (i) په لومړیو 10 s کې، (ii) له 10 s څخه تر 40 s پورې، او (iii) په وروستیو 5 ثانیو کې.'),
pair('b. total distance covered','b. کل طے کردہ فاصلہ','b. ټول وهل شوی واټن'),
pair('and c. average speed of the car for whole journey.','اور c. پورے سفر کے لیے گاڑی کی اوسط رفتار۔','او c. د ټول سفر لپاره د موټر منځنۍ چټکتیا.'),
pair('SOLUTION','حل','حل'),
pair('a. The slope of the graph will give magnitude of acceleration','a. گراف کی ڈھال تعجیل کی مقدار دے گی۔','a. د ګراف میلان به د تعجیل اندازه ورکړي.'),
pair('(i) For the first 10 seconds, OA line represents the slope','(i) پہلے 10 سیکنڈ کے لیے لکیر OA ڈھال ظاہر کرتی ہے۔','(i) د لومړیو 10 ثانیو لپاره OA کرښه میلان ښيي.'),
pair('(ii) From 10 s to 40 s, the slope is represented by line AB','(ii) 10 s سے 40 s تک ڈھال لکیر AB سے ظاہر ہوتی ہے۔','(ii) له 10 s څخه تر 40 s پورې میلان د AB کرښې په واسطه ښودل کېږي.')]

source=json.loads((OUT/'physics-page-049.json').read_text(encoding='utf-8'))
act=json.loads(json.dumps(next(b for b in source['sections'][0]['blocks'] if b['id']=='physics9-distance-time-interpretation-figure210')))
act['id']='physics9-speed-time-activity-graphs';act['sourceWidthRatio']=.98
for field in ['svg','svgUrdu','svgPashto']:
 s=act[field].replace('viewBox="0 0 710 220"','viewBox="0 0 710 280"').replace('S (m)','v (m/s)').replace('stroke="#2f784f"','stroke="#286583"').replace('Figure2.10: zero-speed horizontal distance line; uniform-speed straight rising line; variable-speed rising concave-down curve','Speed-time activity: three graphs constant, linear increase and concave-down increase with blank answer boxes')
 boxes=''.join(f'<rect x="{5+i*235}" y="228" width="220" height="42" fill="#fff" stroke="#42627c" stroke-width="2"/>' for i in range(3))
 act[field]=s.replace('</g></svg>',boxes+'</g></svg>')
act['graphData']=dict(panels=['constant positive speed','linearly increasing speed from origin','increasing speed with decreasing slope'],axes=['v (m/s)','t (s)'],blankAnswerBoxes=3)
g='<rect x="6" y="7" width="328" height="316" fill="#fff"/>'
for x in range(6,335,15):g+=f'<path d="M{x} 7V323" stroke="#976d7f" stroke-width=".8"/>'
for y in range(7,324,15):g+=f'<path d="M6 {y}H334" stroke="#976d7f" stroke-width=".8"/>'
g+='<polygon points="85,246 115,96 115,246" fill="#7ba1c0" fill-opacity=".65"/><rect x="115" y="96" width="90" height="150" fill="#e7dfa2" fill-opacity=".6"/><polygon points="205,96 220,246 205,246" fill="#7ba1c0" fill-opacity=".65"/><path d="M85 58V271M85 246H275" stroke="#a13139" stroke-width="3"/><path d="M85 58l-6 12h12Z M275 246l-12 -6v12Z" fill="#a13139"/><path d="M85 246L115 96H205L220 246" stroke="#28778d" stroke-width="5" fill="none"/><path d="M45 96V246M39 96h12M39 246h12M85 293H220M85 285v16M220 285v16" stroke="#293552" stroke-width="2"/>'
g+=text('speed',83,32,'middle',20)+text('v (ms⁻¹)',84,53,'middle',20)+text('time',302,223,'middle',19)+text('t (s)',302,245,'middle',19)+text('Δv',29,175,'middle',19)+text('Δt',153,317,'middle',19)+text('O',70,267,'middle',18)+text('A',115,85,'middle',18)+text('B',205,85,'middle',18)+text('E',122,235,'middle',18)+text('D',197,235,'middle',18)+text('C',230,235,'middle',18)
for i in range(1,6):
 xx=85+i*30;yy=246-i*30
 g+=f'<path d="M{xx} 240v12" stroke="#a13139" stroke-width="3"/>'+text(str(i*10),xx,273,'middle',18)
 g+=f'<path d="M79 {yy}h12" stroke="#293552" stroke-width="3"/>'+text(str(i*5),67,yy+7,'middle',18)
graph=block('physics9-example24-car-speed-graph',g,w=343,h=332,ratio=.47,label='Example2.4 speed-time graph O(0,0),A(10,25),B(40,25),C(45,0),E(10,0),D(40,0); blue triangle sides and yellow rectangle; time0–50s, speed0–25ms-1',ur=g.replace('speed','رفتار').replace('>time<','>وقت<'),ps=g.replace('speed','چټکتیا').replace('>time<','>وخت<'),kind='graph')
graph['graphData']=dict(xAxis=dict(quantity='time',unit='s',ticks=[0,10,20,30,40,50]),yAxis=dict(quantity='speed',unit='ms⁻¹',ticks=[0,5,10,15,20,25]),points=dict(O=[0,0],A=[10,25],B=[40,25],C=[45,0],E=[10,0],D=[40,0]),shadedRegions=[['O','A','E'],['E','A','B','D'],['D','B','C']])
b=text('slope =',5,65)+frac('Δv','Δt',125,45)+text('=',190,65)+frac(sub('v','f')+' − '+sub('v','i'),sub('t','f')+' − '+sub('t','i'),233,130)+text('= magnitude of acceleration',382,65)
f=block('physics9-example24-slope-formula',b,w=835,ratio=.91,ur=b.replace('slope','ڈھال').replace('magnitude of acceleration','تعجیل کی مقدار'),ps=b.replace('slope','میلان').replace('magnitude of acceleration','د تعجیل اندازه'))
b=text('Magnitude of acceleration  a =',5,65)+frac('25 m s⁻¹ − 0 m s⁻¹','10 s − 0 s',455,220)+text('=',690,65)+frac('25 m s⁻¹','10 s',730,125)+text('= 2.5 m s⁻²',870,65)
a=block('physics9-example24-oa-acceleration',b,w=1050,ratio=.98,ur=b.replace('Magnitude of acceleration','تعجیل کی مقدار'),ps=b.replace('Magnitude of acceleration','د تعجیل اندازه'))
num=dict(num='2.4',name='GRAPHICAL ANALYSIS OF CAR’S SPEED',statement=' '.join(q['text'] for q in p[3:7]),given='Textbook speed-time graph: O(0,0), A(10,25), B(40,25), C(45,0); time in s, speed in ms⁻¹.',required=' '.join(q['text'] for q in p[4:7]),formula='<div style="max-width:490px">'+f['svg']+'</div>',solution='<div style="max-width:490px">'+a['svg']+'</div>',answer='',sourcePendingContinuation=True,sourcePdfPage=52,sourcePrintedPage=47,pairedParagraphs=p[3:11],diagramSvg='<div style="max-width:245px">'+graph['svg']+'</div>')
save(52,'Speed-time activity / Example2.4 graphical car-speed analysis beginning',[section('2.4.2','2.4.2 SPEED - TIME GRAPH','2.4.2 رفتار وقت گراف','2.4.2 د چټکتیا او وخت ګراف',p,[act,graph,f,a],[para(0,'heading'),para(1),visual(act),para(2,'heading'),para(3),dict(type='numberedList',indices=[4,5,6]),visual(graph),para(7,'heading'),para(8),visual(f),para(9),visual(a),para(10)])],'Fresh visible source inspection. Restored activity question and three native grid plots with unfilled answer rectangles. Corrected Example2.4 to actual car speed graph and a/b/c subquestions. Native graph faithfully uses10/40/45second stages,25ms⁻¹ plateau,OABCDE labels and three shaded regions, with structured reusable point data. Preserved original extra a wording. First acceleration fraction/2.5ms⁻² result restored; remaining solution explicitly pending consecutive page. All captions/word labels/prose translated.',numericals=[num],activities=[dict(num='source-speed-time-slope-activity',name='SPEED- TIME GRAPH',procedure=p[1]['text'],urdu=p[1]['urdu'],pashto=p[1]['pashto'],sourcePdfPage=52,sourcePrintedPage=47)])
