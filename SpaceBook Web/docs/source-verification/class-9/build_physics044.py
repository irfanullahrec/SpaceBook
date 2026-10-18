from physics_page_tools import *

p=[
pair('instantaneous velocity is the velocity for very short time interval t (very small such that limit approaching to zero)’. Mathematically','لحظاتی سمتی رفتار بہت مختصر وقفۂ وقت t کی سمتی رفتار ہے (اتنا چھوٹا کہ حد صفر کے قریب ہو)۔ ریاضیاتی طور پر','لحظه يي سرعت د ډېر لنډ وخت واټن t سرعت دی (دومره ډېر کوچنی چې حد یې صفر ته نږدې کېږي)». په ریاضي کې'),
pair('Figure 2.7 Velocity','شکل 2.7 سمتی رفتار','شکل 2.7 سرعت'),
pair('The average velocity does not convey detailed information about the motion during the corresponding time interval Δt.. Suppose a car moves on a curved track, through points A, B, C, D and E as shown in the figure. (a) The average velocity is defined over the entire journey, (b) the measure of velocity in shorter interval of time is different both in magnitude and direction at different points. (c) The instantaneous velocity will be tangent to the curved path of the motion of car.','اوسط سمتی رفتار متعلقہ وقفۂ وقت Δt کے دوران حرکت کی تفصیلی معلومات نہیں دیتی۔ فرض کریں گاڑی شکل کے مطابق منحنی راستے پر A، B، C، D اور E نقاط سے گزرتی ہے۔ (a) اوسط سمتی رفتار پورے سفر کے لیے بیان ہوتی ہے۔ (b) مختصر وقفۂ وقت میں سمتی رفتار کی مقدار اور سمت مختلف نقاط پر مختلف ہوتی ہیں۔ (c) لحظاتی سمتی رفتار گاڑی کی حرکت کے منحنی راستے پر مماس ہوگی۔','منځنی سرعت د اړوند وخت واټن Δt په اوږدو کې د حرکت تفصیلي معلومات نه ورکوي. فرض کړئ یو موټر د شکل له مخې پر منحني لاره د A، B، C، D او E ټکو څخه تېرېږي. (a) منځنی سرعت د ټول سفر لپاره تعریفېږي. (b) د لنډ وخت واټن سرعت په بېلابېلو ټکو کې هم په اندازه او هم په لوري کې توپیر لري. (c) لحظه يي سرعت به د موټر د حرکت پر منحني لاره مماس وي.'),
pair('The velocity which magnitude and direction does not change with time is called uniform velocity.','هغه سمتی رفتار جس کی مقدار اور سمت وقت کے ساتھ نہ بدلیں، یکساں سمتی رفتار کہلاتی ہے۔','هغه سرعت چې اندازه او لوری یې له وخت سره نه بدلېږي، یوشان سرعت بلل کېږي.'),
pair('Example 2.2 STRAIGHT ROAD','مثال 2.2 سیدھی سڑک','بېلګه 2.2 مستقیم سړک'),
pair('A straight track is 1200 m in length. A runner begins at the starting line, runs due east for the full length of the track, turns around and runs halfway back. The time for this run is five minutes. What is her (a) average velocity, and (b) average speed?','سیدھے راستے کی لمبائی 1200 m ہے۔ ایک دوڑنے والی ابتدائی لکیر سے شروع کر کے راستے کی پوری لمبائی مشرق کی طرف دوڑتی ہے، مڑتی ہے اور آدھا راستہ واپس دوڑتی ہے۔ اس دوڑ کا وقت پانچ منٹ ہے۔ اس کی (a) اوسط سمتی رفتار اور (b) اوسط رفتار کیا ہیں؟','د مستقیمې لارې اوږدوالی 1200 m دی. یوه منډه وهونکې د پیل له کرښې شروع کوي، د لارې په ټوله اوږدوالي ختیځ ته منډه وهي، بېرته تاوېږي او نیمه لاره بېرته راځي. د دې منډې وخت پنځه دقیقې دی. د هغې (a) منځنی سرعت او (b) منځنۍ چټکتیا څومره دي؟'),
pair('GIVEN:','دیے گئے:','ورکړل شوي:'),
pair('Distance covered s = 1200 m + 600 m = 1800 m','طے کردہ فاصلہ s = 1200 m + 600 m = 1800 m','وهل شوی واټن s = 1200 m + 600 m = 1800 m'),
pair('Displacement Δs = 1200 m - 600 m = 600 m','نقل مکانی Δs = 1200 m - 600 m = 600 m','بېځایه کېدل Δs = 1200 m - 600 m = 600 m'),
pair('time Δt = 5 min = (5 × 60 s) = 300 s','وقت Δt = 5 min = (5 × 60 s) = 300 s','وخت Δt = 5 min = (5 × 60 s) = 300 s'),
pair('REQUIRED:','مطلوب:','غوښتل شوي:'),
pair('(a) average speed ⟨v⟩ = ?','(a) اوسط رفتار ⟨v⟩ = ؟','(a) منځنۍ چټکتیا ⟨v⟩ = ؟'),
pair('(b) average velocity ⟨v⃗⟩ = ?','(b) اوسط سمتی رفتار ⟨v⃗⟩ = ؟','(b) منځنی سرعت ⟨v⃗⟩ = ؟')]
p[3]['urdu']=p[3]['urdu'].replace('هغه ','')
v=block('physics9-instantaneous-velocity-equation26',text(sub('v⃗','inst')+' =',5,63)+text('Lim',125,63)+text('Δt→0',147,91,'middle',16)+frac('s⃗','t',200,40)+number('2.6',355),w=440,ratio=.46,label='Printed equation 2.6 instantaneous velocity: limit as delta t approaches zero of vector s divided by t')
body=''
for i in range(3):
 x=i*290
 body+=f'<g transform="translate({x},0)"><text x="115" y="23">({chr(97+i)})</text><path d="M30 220Q30 155 53 142Q135 133 208 143Q255 131 247 51" fill="none" stroke="#47785f" stroke-width="4" stroke-dasharray="3 7"/>'
 points=[(30,220,'A'),(53,142,'B'),(208,143,'C'),(247,108,'D'),(247,51,'E')]
 for xx,yy,name in points:
  body+=f'<circle cx="{xx}" cy="{yy}" r="6" fill="#bb3343" stroke="#542a36"/>'+text(name,xx-21,yy-12,size=21)
 if i==0:
  body+='<path d="M30 220L247 51" stroke="#332945" stroke-width="3"/><path d="M247 51l-5 16l-10 -12Z" fill="#332945"/>'
  body+=text('&lt; v⃗ &gt; =',82,243)+frac('s⃗','t',188,35,y=233)
 elif i==1:
  body+='<path d="M30 220L53 142L208 143L247 108L247 51" fill="none" stroke="#332945" stroke-width="3"/><path d="M53 142l2 16l-13 -3Z M208 143l-16 -7v14Z M247 108l-6 16l-10 -11Z M247 51l-7 16h14Z" fill="#332945"/>'
  body+=text('v⃗ =',98,243)+frac('Δs⃗','Δt',165,45,y=233)
 else:
  body+='<path d="M7 171L86 119M186 154L233 125" fill="none" stroke="#332945" stroke-width="3"/><path d="M86 119l-8 16l-8 -12Z M233 125l-8 15l-7 -13Z" fill="#332945"/>'
  body+=text('v⃗ = Lim',85,244)+text('Δt→0',164,269,'middle',14)+frac('Δs⃗','Δt',220,42,y=233)
 body+='</g>'
f=block('physics9-velocity-figure27',body,w=880,h=295,ratio=.97,label='Figure 2.7 three dotted curved paths through A B C D E: whole-journey displacement, segment velocities and tangent instantaneous velocities',kind='vector')
prev=json.loads((OUT/'physics-page-043.json').read_text(encoding='utf-8'))['sections'][1]['paras'][-1]
full={k:prev[k]+' '+p[0][k] for k in ['text','urdu','pashto']}
definition=full['text'][full['text'].index('‘The'):]
s=section('2.3.4','2.3.4 VELOCITY','2.3.4 سمتی رفتار','2.3.4 سرعت',p,[v,f],[para(0),visual(v),para(1,'heading'),visual(f),para(2,'quotation'),para(3,'quotation'),para(4,'heading'),para(5),dict(type='parallelPhrases',columns=[[6,7,8,9],[10,11,12]])])
s['continuesPreviousParagraph']=True
num=dict(num='2.2',name='STRAIGHT ROAD',statement=p[5]['text'],given='\n'.join(q['text'] for q in p[7:10]),required=p[11]['text']+'\n'+p[12]['text'],formula='',solution='',answer='',sourcePendingContinuation=True,sourcePdfPage=44,sourcePrintedPage=39,pairedParagraphs=p[5:13])
save(44,'Instantaneous/uniform velocity / Figure 2.7 / Example 2.2 beginning',[s],'Fresh rendered source inspection. Preserved instantaneous definition continued from page43, printed s-vector/t equation2.6, source caption and complete three-panel Figure2.7: green dotted path points, directed diagonal/segments/tangents and three vector equations. Corrected Example2.2 to original runner question and data; preserved opposite a/b order in REQUIRED instead of silently changing it. Pending source solution left empty until its next consecutive page. All prose explicitly paired and book-size native diagram.',definitions=[dict(term='Instantaneous Velocity',definition=definition,urdu=full['urdu'],pashto=full['pashto'],sourcePdfPages=[43,44],sourcePrintedPages=[38,39]),dict(term='Uniform Velocity',definition=p[3]['text'],urdu=p[3]['urdu'],pashto=p[3]['pashto'],sourcePdfPage=44,sourcePrintedPage=39)],numericals=[num])
