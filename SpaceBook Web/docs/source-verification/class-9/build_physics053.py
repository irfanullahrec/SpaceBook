from physics_page_tools import *

p=[
pair('(iii) In the last 5 seconds','(iii) آخری 5 سیکنڈ میں','(iii) په وروستیو 5 ثانیو کې'),
pair('In the first 10 s the cars acceleration is 2.5 m/s², from 10 s to 40 s it is 0 m/s², while in the last 5 s it is -5 m/s², the negative gradient indicates that the car is slowing down.','پہلے 10 s میں گاڑی کی تعجیل 2.5 m/s² ہے، 10 s سے 40 s تک 0 m/s² اور آخری 5 s میں -5 m/s² ہے۔ منفی ڈھال ظاہر کرتی ہے کہ گاڑی آہستہ ہو رہی ہے۔','په لومړیو 10 s کې د موټر تعجیل 2.5 m/s² دی، له 10 s څخه تر 40 s پورې 0 m/s² او په وروستیو 5 s کې -5 m/s² دی. منفي میلان ښيي چې موټر ورو کېږي.'),
pair('Answer','جواب','ځواب'),
pair('b. Now the total distance covered is equal to the area under the speed-time graph.','b. اوس کل طے کردہ فاصلہ رفتار وقت گراف کے نیچے رقبے کے برابر ہے۔','b. اوس ټول وهل شوی واټن د چټکتیا او وخت ګراف لاندې مساحت سره برابر دی.'),
pair('or','یا','یا'),
pair('Answer','جواب','ځواب'),
pair('total distance covered by car is ‘937.5 m','گاڑی کا کل طے کردہ فاصلہ ‘937.5 m ہے۔','د موټر ټول وهل شوی واټن ‘937.5 m دی.'),
pair('c. Now the average speed can be calculated when distance s is divided by total time t.','c. اب فاصلہ s کو کل وقت t سے تقسیم کر کے اوسط رفتار معلوم کی جا سکتی ہے۔','c. اوس منځنۍ چټکتیا هغه وخت محاسبه کېدای شي چې واټن s پر ټول وخت t ووېشل شي.'),
pair('therefore','لہٰذا','نو'),
pair('Answer','جواب','ځواب'),
pair('The average speed of the car is 20.8 m/s','گاڑی کی اوسط رفتار 20.8 m/s ہے۔','د موټر منځنۍ چټکتیا 20.8 m/s ده.'),
pair('Assignment 2.4 GRAPHICAL ANALYSIS OF CYCLIST','اسائنمنٹ 2.4 سائیکل سوار کا گرافی تجزیہ','دنده 2.4 د بایسکل چلوونکي ګرافیکي تحلیل'),
pair('A cyclist increases his speed from ZERO to 8ms⁻¹ in 10 s. Then he moves with uniform speed for the next 20 seconds and then its speed decreases uniformly to ZERO in the next 20 seconds. The graph is plotted for the journey, use this graph to calculate the total distance covered.','سائیکل سوار اپنی رفتار صفر سے 10 s میں 8ms⁻¹ تک بڑھاتا ہے۔ پھر اگلے 20 سیکنڈ یکساں رفتار سے چلتا ہے، اور اس کے بعد اگلے 20 سیکنڈ میں رفتار یکساں طور پر صفر تک کم ہوتی ہے۔ سفر کا گراف بنایا گیا ہے؛ اس سے کل طے کردہ فاصلہ معلوم کریں۔','یو بایسکل چلوونکی خپله چټکتیا په 10 s کې له صفر څخه 8ms⁻¹ ته زیاتوي. بیا راتلونکې 20 ثانیې په یوشان چټکتیا ځي او وروسته یې چټکتیا په راتلونکو 20 ثانیو کې په یوشان ډول صفر ته کمېږي. د سفر ګراف رسم شوی؛ له دې ګرافه ټول وهل شوی واټن محاسبه کړئ.'),
pair('Editorial source-review note: The constant-speed calculation prints 40 s − 30 s, although the preceding text specifies the interval from 10 s to 40 s. The printed calculation is retained.','ادارتی ماخذ جائزے کا نوٹ: مستقل رفتار کی گنتی میں 40 s − 30 s چھپا ہے، حالانکہ اس سے پہلے متن میں وقفہ 10 s سے 40 s بیان ہوا ہے۔ چھپی گنتی برقرار رکھی گئی ہے۔','د سرچینې د کتنې سمونیز یادښت: د ثابتې چټکتیا په محاسبه کې 40 s − 30 s چاپ شوي، خو مخکینی متن له 10 s څخه تر 40 s پورې واټن یادوي. چاپ شوې محاسبه ساتل شوې ده.')]

def acceleration(n,d,reduced,ans,i):
 b=text('Magnitude of acceleration  a =',5,65)+frac(n,d,455,240)+text('=',711,65)+frac(reduced,'10 s' if i==2 else '5 s',753,140)+text('= '+ans,910,65)
 return block(f'physics9-example24-acceleration-{i}',b,w=1090,ratio=.98,ur=b.replace('Magnitude of acceleration','تعجیل کی مقدار'),ps=b.replace('Magnitude of acceleration','د تعجیل اندازه'))
a2=acceleration('25 m s⁻¹ − 25 m s⁻¹','40 s − 30 s','0 m s⁻¹','0 m s⁻²',2)
a3=acceleration('0 m s⁻¹ − 25 m s⁻¹','45 s − 40 s','−25 m s⁻¹','−5 m s⁻²',3)
b=text('Total distance',110,29,'middle')+text('covered',110,64,'middle')+text('=',230,45)+text('Area of triangle',371,29,'middle')+text('Δ OAE',371,64,'middle')+text('+',507,45)+text('Area of',658,29,'middle')+text('rectangle ABDE',658,64,'middle')+text('+',797,45)+text('Area of triangle',960,29,'middle')+text('Δ CDB',960,64,'middle')
sumarea=block('physics9-example24-distance-area-components',b,w=1110,h=95,ratio=.98,ur=b.replace('Total distance','کل فاصلہ').replace('covered','طے کردہ').replace('Area of triangle','مثلث کا رقبہ').replace('Area of','رقبہ').replace('rectangle ABDE','مستطیل ABDE'),ps=b.replace('Total distance','ټول واټن').replace('covered','وهل شوی').replace('Area of triangle','د مثلث مساحت').replace('Area of','مساحت').replace('rectangle ABDE','مستطیل ABDE'))
b=text('S = {',5,65)+frac('1','2',92,30)+text('× (25 ms⁻¹ × 10 s)} + {25 ms⁻¹ × 30 s} + {',138,65)+frac('1','2',810,30)+text('× (25 ms⁻¹ × 5 s)}',861,65)
areas=block('physics9-example24-distance-area-values',b,w=1210,ratio=.98)
sumans=block('physics9-example24-distance-answer',text('S = 125 m + 750 m + 62.5 m = 937.5 m',5,45),w=650,h=80,ratio=.78)
b=text('&lt; v &gt; =',5,65)+frac('Total distance','Total time',140,205)+text('or',384,65)+text('&lt; v &gt; =',450,65)+frac('937.5 m','45 s',585,120)
avg=block('physics9-example24-average-speed-values',b,w=760,ratio=.78,ur=b.replace('Total distance','کل فاصلہ').replace('Total time','کل وقت').replace('>or<','>یا<'),ps=b.replace('Total distance','ټول واټن').replace('Total time','ټول وخت').replace('>or<','>یا<'))
ans=block('physics9-example24-average-speed-answer',text('&lt; v &gt; = 20.8 m/s',5,45),w=330,h=80,ratio=.4)

g='<rect x="6" y="7" width="328" height="316" fill="#fff"/>'
for x in range(6,335,15):g+=f'<path d="M{x} 7V323" stroke="#976d7f" stroke-width=".8"/>'
for y in range(7,324,15):g+=f'<path d="M6 {y}H334" stroke="#976d7f" stroke-width=".8"/>'
g+='<polygon points="85,246 115,126 115,246" fill="#76aacb" fill-opacity=".7"/><rect x="115" y="126" width="60" height="120" fill="#eadc6f" fill-opacity=".7"/><polygon points="175,126 235,246 175,246" fill="#76aacb" fill-opacity=".7"/><path d="M85 80V269M85 246H275" stroke="#a13139" stroke-width="3"/><path d="M85 80l-6 12h12Z M275 246l-12 -6v12Z" fill="#a13139"/><path d="M85 246L115 126H175L235 246" stroke="#235fa4" stroke-width="5" fill="none"/><path d="M45 126V246M39 126h12M39 246h12M85 293H235M85 285v16M235 285v16" stroke="#293552" stroke-width="2"/>'
g+=text('speed',83,55,'middle',20)+text('v (ms⁻¹)',84,78,'middle',20)+text('time',302,223,'middle',19)+text('t (s)',302,245,'middle',19)+text('Δv',29,188,'middle',19)+text('Δt',160,317,'middle',19)+text('O',70,267,'middle',18)+text('A',115,114,'middle',18)+text('B',175,114,'middle',18)+text('E',121,235,'middle',18)+text('D',181,235,'middle',18)+text('C',242,235,'middle',18)
for i in range(1,6):
 xx=85+i*30
 g+=f'<path d="M{xx} 240v12" stroke="#a13139" stroke-width="3"/>'+text(str(i*10),xx,273,'middle',18)
for i in range(1,5):
 yy=246-i*30
 g+=f'<path d="M79 {yy}h12" stroke="#293552" stroke-width="3"/>'+text(str(i*2),67,yy+7,'middle',18)
graph=block('physics9-assignment24-cyclist-graph',g,w=343,h=332,ratio=.39,label='Assignment2.4 cyclist speed-time graph O(0,0),A(10,8),B(30,8),C(50,0),E(10,0),D(30,0); blue triangles and yellow rectangle',ur=g.replace('speed','رفتار').replace('>time<','>وقت<'),ps=g.replace('speed','چټکتیا').replace('>time<','>وخت<'),kind='graph')
graph['graphData']=dict(xAxis=dict(quantity='time',unit='s',ticks=[0,10,20,30,40,50]),yAxis=dict(quantity='speed',unit='ms⁻¹',ticks=[0,2,4,6,8]),points=dict(O=[0,0],A=[10,8],B=[30,8],C=[50,0],E=[10,0],D=[30,0]),shadedRegions=[['O','A','E'],['E','A','B','D'],['D','B','C']])
prev=OUT/'physics-page-052.json';page=json.loads(prev.read_text(encoding='utf-8'));num=page['numericals'][0]
num.update(solution=num['solution']+'<div style="max-width:490px">'+a2['svg']+a3['svg']+sumarea['svg']+areas['svg']+sumans['svg']+avg['svg']+ans['svg']+'</div>',answer=p[1]['text']+'\n'+'Total distance = 937.5 m.\n'+p[10]['text'],answerSource='textbook',sourcePendingContinuation=False,sourcePdfPages=[52,53],sourcePrintedPages=[47,48],pairedParagraphs=num['pairedParagraphs']+p[:11],editorialNote=p[13]['text'])
prev.write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
layout=[visual(a2),para(0),visual(a3),para(1,'quotation'),para(2),para(3),visual(sumarea),visual(areas),para(4),visual(sumans),para(5),para(6),para(7),visual(avg),para(8),visual(ans),para(9),para(10),para(11,'heading'),dict(type='visualParagraph',blockId=graph['id'],indices=[12],visualFirst=False),para(13,'quotation')]
save(53,'Example2.4 completed calculation / Assignment2.4 cyclist graph',[section('2.4.2','2.4.2 SPEED - TIME GRAPH','2.4.2 رفتار وقت گراف','2.4.2 د چټکتیا او وخت ګراف',p,[a2,a3,sumarea,areas,sumans,avg,ans,graph],layout)],'Fresh full-page and3x detail crop inspection. Verified negative25 numerator in final acceleration; restored0/-5ms⁻² stages, original40s−30s denominator retained with separate source note. Complete region decomposition and all half-fraction steps,937.5m distance,45s average-speed fraction/20.8m/s answer preserved. Original lone quote before937.5m retained. Native cyclist graph uses10/30/50second stages and8ms⁻¹ with labelled/shaded regions, at.39 book ratio. Complete aligned translations; no assignment answer invented.',numericals=[num],activities=[dict(num='Assignment 2.4',name='GRAPHICAL ANALYSIS OF CYCLIST',procedure=p[12]['text'],urdu=p[12]['urdu'],pashto=p[12]['pashto'],sourcePdfPage=53,sourcePrintedPage=48)])
