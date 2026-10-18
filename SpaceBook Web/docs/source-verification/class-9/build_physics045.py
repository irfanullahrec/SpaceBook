from physics_page_tools import *

p=[
pair('From the definition of average velocity, equation 2.5 we have','اوسط سمتی رفتار کی تعریف، مساوات 2.5 سے ہمارے پاس ہے۔','د منځني سرعت له تعریف، 2.5 معادلې څخه لرو'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('Answer','جواب','ځواب'),
pair('From the definition of average speed, equation 2.3 we have','اوسط رفتار کی تعریف، مساوات 2.3 سے ہمارے پاس ہے۔','د منځنۍ چټکتیا له تعریف، 2.3 معادلې څخه لرو'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('Answer','جواب','ځواب'),
pair('Her average velocity is 2 m/s East, while her average speed is 6 m/s.','اس کی اوسط سمتی رفتار مشرق کی طرف 2 m/s ہے، جبکہ اوسط رفتار 6 m/s ہے۔','د هغې منځنی سرعت ختیځ ته 2 m/s دی، خو منځنۍ چټکتیا یې 6 m/s ده.'),
pair('Assignment 2.2 AVERAGE VELOCITY OF COMPLETE LAP','اسائنمنٹ 2.2 مکمل چکر کی اوسط سمتی رفتار','دنده 2.2 د بشپړ چکر منځنی سرعت'),
pair('A runner makes one lap around a 270 m circular track in 30 s. What is his (a) average speed and (b) average velocity?','ایک دوڑنے والا 270 m کے دائرہ نما راستے کا ایک چکر 30 s میں مکمل کرتا ہے۔ اس کی (a) اوسط رفتار اور (b) اوسط سمتی رفتار کیا ہیں؟','یو منډه وهونکی د 270 m دایروي لارې یو چکر په 30 s کې وهي. د هغه (a) منځنۍ چټکتیا او (b) منځنی سرعت څومره دي؟'),
pair('Editorial source-review note: The reference to equation 2.3 in this average-speed solution is retained as printed; the average-speed equation is numbered 2.2 on printed page 36.','ادارتی ماخذ جائزے کا نوٹ: اوسط رفتار کے اس حل میں مساوات 2.3 کا حوالہ اصل کے مطابق رکھا گیا ہے؛ اوسط رفتار کی مساوات مطبوعہ صفحہ 36 پر 2.2 ہے۔','د سرچینې د کتنې سمونیز یادښت: د منځنۍ چټکتیا په دې حل کې د 2.3 معادلې حواله د چاپ له مخې ساتل شوې؛ د منځنۍ چټکتیا معادله په چاپي مخ 36 کې 2.2 شمېرل شوې ده.')]

road='<path d="M24 69H552Q566 69 566 82Q566 95 552 95H288" fill="none" stroke="#285e77" stroke-width="3"/><path d="M24 111H288" stroke="#222" stroke-width="3"/><path d="M288 111l-17 -9v18Z" fill="#222"/><path d="M24 136H552" stroke="#222" stroke-width="2"/>'
for i in range(13):
 x=24+44*i
 road+=f'<path d="M{x} 136v13" stroke="#222" stroke-width="2"/>'+text(str(i*100),x,175,'middle',18)
runner='<circle cx="0" cy="-50" r="5" fill="#357d9c"/><path d="M0 -44l-6 18l9 10l-9 22M-6 -26l-13 5l-10 18M-3 -38l12 9l10 -7M-7 -36l-10 7l-6 -4" stroke="#357d9c" stroke-width="5" fill="none"/>'
for xx,flip in [(68,1),(266,1),(464,-1)]:road+=f'<g transform="translate({xx},69) scale({flip},1)">{runner}</g>'
road+=text('distance',305,60,size=21)+text('displacement',112,104,size=21)+text('meters',288,205,'middle',22)
road+='<path d="M613 51v63M590 83h46" stroke="#a72e28" stroke-width="3"/><path d="M613 51l-5 9h10Z M613 114l-5 -9h10Z M590 83l9 -5v10Z M636 83l-9 -5v10Z" fill="#a72e28"/>'+text('N',613,40,'middle',18)+text('S',613,139,'middle',18)+text('W',578,90,'middle',18)+text('E',651,90,'middle',18)
r=block('physics9-runner-example22-road',road,w=665,h=220,ratio=.95,label='Example 2.2: 0 to1200 metre scale, outbound and halfway-return distance path, eastward displacement arrow to600 metres, three runner positions and NEWS coordinate cross',ur=road.replace('>distance<','>فاصلہ<').replace('>displacement<','>نقل مکانی<').replace('>meters<','>میٹر<'),ps=road.replace('>distance<','>واټن<').replace('>displacement<','>بېځایه کېدل<').replace('>meters<','>متر<'),kind='vector')
v=block('physics9-example22-velocity',text('&lt; v⃗ &gt; =',5,64)+frac('s⃗','t',135,40),w=210,ratio=.23)
vc=block('physics9-example22-velocity-values',text('&lt; v⃗ &gt; =',5,64)+frac('600 m (East)','300 s',135,165),w=350,ratio=.36,ur=text('&lt; v⃗ &gt; =',5,64)+frac('600 m (مشرق)','300 s',135,165),ps=text('&lt; v⃗ &gt; =',5,64)+frac('600 m (ختیځ)','300 s',135,165))
va=block('physics9-example22-velocity-answer',text('&lt; v⃗ &gt; = 2 m/s East',5,45),w=390,h=75,ratio=.43,ur=text('&lt; v⃗ &gt; = 2 m/s مشرق',5,45),ps=text('&lt; v⃗ &gt; = 2 m/s ختیځ',5,45))
s=block('physics9-example22-speed',text('&lt; v &gt; =',5,64)+frac('s','t',135,40),w=210,ratio=.23)
sc=block('physics9-example22-speed-values',text('&lt; v &gt; =',5,64)+frac('1800 m','300 s',135,115),w=295,ratio=.31)
sa=block('physics9-example22-speed-answer',text('&lt; v &gt; = 6 m/s',5,45),w=320,h=75,ratio=.35)

q=[
pair('‘The measure of change in velocity Δv with the passage of time ‘Δt’ is called acceleration. (or) Time rate of change of velocity is called acceleration a⃗’. Mathematically','وقت ‘Δt’ گزرنے کے ساتھ سمتی رفتار میں تبدیلی Δv کی پیمائش تعجیل کہلاتی ہے۔ (یا) سمتی رفتار کی تبدیلی کی زمانی شرح تعجیل a⃗ کہلاتی ہے۔ ریاضیاتی طور پر','د وخت ‘Δt’ په تېرېدو په سرعت کې د بدلون Δv اندازه تعجیل بلل کېږي. (یا) د سرعت د بدلون زماني کچه تعجیل a⃗ بلل کېږي. په ریاضي کې'),
pair('Acceleration is also a vector quantity having same direction as change in velocity. SI Unit of acceleration is meter per second squared (m/s²). Acceleration is a measure of how rapidly the velocity is changing.','تعجیل بھی سمتی مقدار ہے اور اس کی سمت سمتی رفتار میں تبدیلی کی سمت جیسی ہوتی ہے۔ تعجیل کی SI اکائی میٹر فی سیکنڈ مربع (m/s²) ہے۔ تعجیل بتاتی ہے کہ سمتی رفتار کتنی تیزی سے بدل رہی ہے۔','تعجیل هم ویکټوري کمیت دی او د سرعت د بدلون په څېر لوری لري. د تعجیل SI واحد متر پر ثانیه مربع (m/s²) دی. تعجیل دا اندازه کوي چې سرعت څومره په چټکۍ بدلېږي.'),
pair('A) Average Acceleration:','A) اوسط تعجیل:','A) منځنی تعجیل:'),
pair('‘Average acceleration ⟨a⃗⟩ is the net change in velocity Δv⃗ divided by the total time t’.','اوسط تعجیل ⟨a⃗⟩ سمتی رفتار کی خالص تبدیلی Δv⃗ کو کل وقت t سے تقسیم کرنے پر ملتی ہے۔','منځنی تعجیل ⟨a⃗⟩ په سرعت کې خالص بدلون Δv⃗ پر ټول وخت t وېشل دي.')]
eq=text('acceleration =',5,65)+frac('change in velocity','elapsed time',215,250)+text('or',490,65)+text('a⃗ =',540,65)+frac('Δv⃗','Δt',620,55)+text('or',705,65)+text('a⃗ =',765,65)+frac(sub('v⃗','f')+' − '+sub('v⃗','i'),sub('t','f')+' − '+sub('t','i'),840,130)+number('2.7',1090)
a=block('physics9-acceleration-equation27',eq,w=1175,ratio=.98,label='Equation 2.7 acceleration equals change in velocity over elapsed time, delta v-vector over delta t, final minus initial velocities over final minus initial times',ur=eq.replace('acceleration','تعجیل').replace('change in velocity','سمتی رفتار میں تبدیلی').replace('elapsed time','گزرا وقت').replace('>or<','>یا<'),ps=eq.replace('acceleration','تعجیل').replace('change in velocity','د سرعت بدلون').replace('elapsed time','تېر شوی وخت').replace('>or<','>یا<'))
eq=text('&lt; a⃗ &gt; =',5,65)+frac('Total change in velocity','Total time',145,310)+text('or',500,65)+text('=&lt; a⃗ &gt; =',560,65)+frac('Δv⃗','t',740,45)+number('2.8',900)
aa=block('physics9-average-acceleration-equation28',eq,w=985,ratio=.96,label='Printed equation 2.8 average acceleration: total change in velocity over total time, with printed leading equals after or',ur=eq.replace('Total change in velocity','سمتی رفتار کی کل تبدیلی').replace('Total time','کل وقت').replace('>or<','>یا<'),ps=eq.replace('Total change in velocity','د سرعت ټول بدلون').replace('Total time','ټول وخت').replace('>or<','>یا<'))
previous=OUT/'physics-page-044.json'
page=json.loads(previous.read_text(encoding='utf-8'))
num=page['numericals'][0]
num.update(formula='<div style="max-width:230px">'+v['svg']+s['svg']+'</div>',solution='<div style="max-width:260px">'+vc['svg']+sc['svg']+'</div>',answer=p[8]['text'],answerSource='textbook',sourcePendingContinuation=False,sourcePdfPages=[44,45],sourcePrintedPages=[39,40],pairedParagraphs=num['pairedParagraphs']+p[:9],editorialNote=p[11]['text'])
previous.write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
layout=[visual(r),para(0),visual(v),para(1),visual(vc),para(2),visual(va),para(3),para(4),visual(s),para(5),visual(sc),para(6),visual(sa),para(7),para(8),para(9,'heading'),para(10),para(11,'quotation')]
save(45,'Example 2.2 solution / Assignment 2.2 / acceleration and average acceleration',[section('2.3.4','2.3.4 VELOCITY','2.3.4 سمتی رفتار','2.3.4 سرعت',p,[r,v,vc,va,s,sc,sa],layout),section('2.3.5','2.3.5 ACCELERATION:','2.3.5 تعجیل:','2.3.5 تعجیل:',q,[a,aa],[para(0,'quotation'),visual(a),para(1),para(2,'heading'),para(3,'quotation'),visual(aa)])],'Fresh visible PDF page inspection. Coded scaled0–1200m road, three runner figures, outbound/return distance path and600m eastward displacement. Restored Example2.2 vector and scalar fractions/answers, assignment question and printed equation2.3 reference with separate note. Corrected acceleration definition, units, direction prose, average definition and both complete numbered equations2.7–2.8; source leading equals retained. All word labels and original paragraphs aligned to explicit translations.',numericals=[num],activities=[dict(num='Assignment 2.2',name='AVERAGE VELOCITY OF COMPLETE LAP',procedure=p[10]['text'],urdu=p[10]['urdu'],pashto=p[10]['pashto'],sourcePdfPage=45,sourcePrintedPage=40)],definitions=[dict(term='Acceleration',definition=q[0]['text'],urdu=q[0]['urdu'],pashto=q[0]['pashto'],sourcePdfPage=45,sourcePrintedPage=40),dict(term='Average Acceleration',definition=q[3]['text'],urdu=q[3]['urdu'],pashto=q[3]['pashto'],sourcePdfPage=45,sourcePrintedPage=40)])
