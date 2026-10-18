from physics_page_tools import *

p=[
pair('object which covers a distance of 100 m in 10 s, the slope of distance time graph will give speed as equation 2.10 can be written as','کوئی شے 10 s میں 100 m فاصلہ طے کرتی ہے؛ فاصلہ وقت گراف کی ڈھال رفتار دے گی اور مساوات 2.10 یوں لکھی جا سکتی ہے۔','شی په 10 s کې 100 m واټن وهي؛ د واټن او وخت ګراف میلان به چټکتیا ورکړي او 2.10 معادله داسې لیکل کېدای شي.'),
pair('from equation 2.1 it is definition of speed, therefore','مساوات 2.1 کے مطابق یہ رفتار کی تعریف ہے، لہٰذا','د 2.1 معادلې له مخې دا د چټکتیا تعریف دی، نو'),
pair('QUIZ DISTANCE- TIME GRAPH','کوئز فاصلہ وقت گراف','کوېز د واټن او وخت ګراف'),
pair('Which of these graphs has higher speed?','ان میں کس گراف کی رفتار زیادہ ہے؟','له دې ګرافونو کوم یو لوړه چټکتیا لري؟'),
pair('Which of these graphs show increasing speed?','ان میں کون سا گراف بڑھتی ہوئی رفتار دکھاتا ہے؟','له دې ګرافونو کوم یو زیاتېدونکې چټکتیا ښيي؟'),
pair('Figure 2.10 Graphical Interpretation','شکل 2.10 گراف کی تشریح','شکل 2.10 د ګراف تفسیر'),
pair('ZERO SPEED','صفر رفتار','صفر چټکتیا'),
pair('Time is passing and no change in distance is seen. It means the body is at rest. Since there is no slope so the speed is zero.','وقت گزر رہا ہے مگر فاصلے میں کوئی تبدیلی دکھائی نہیں دیتی۔ اس کا مطلب جسم ساکن ہے۔ ڈھال نہیں، اس لیے رفتار صفر ہے۔','وخت تېرېږي او په واټن کې هېڅ بدلون نه لیدل کېږي. دا مانا لري چې جسم په سکون کې دی. میلان نشته، نو چټکتیا صفر ده.'),
pair('UNIFORM SPEED','یکساں رفتار','یوشان چټکتیا'),
pair('The distance is increasing linearly with time. The slope is constant therefore object is moving with uniform speed.','فاصلہ وقت کے ساتھ خطی طور پر بڑھ رہا ہے۔ ڈھال مستقل ہے، اس لیے شے یکساں رفتار سے حرکت کر رہی ہے۔','واټن له وخت سره په خطي ډول زیاتېږي. میلان ثابت دی، نو شی په یوشان چټکتیا حرکت کوي.'),
pair('VARIABLE SPEED','متغیر رفتار','بدلېدونکې چټکتیا'),
pair('The distance is changing non-linearly with time (spiking down). The slope is changing therefore object is moving with variable speed.','فاصلہ وقت کے ساتھ غیر خطی طور پر بدل رہا ہے (نیچے کو جھکتا ہوا)۔ ڈھال بدل رہی ہے، اس لیے شے متغیر رفتار سے حرکت کر رہی ہے۔','واټن له وخت سره په غیر خطي ډول بدلېږي (ښکته راکږېږي). میلان بدلېږي، نو شی په بدلېدونکې چټکتیا حرکت کوي.')]
f=block('physics9-distance-time-slope',text('slope =',5,65)+frac('Δs','Δt',125,45)+text('=',188,65)+frac(sub('s','f')+' − '+sub('s','i'),sub('t','f')+' − '+sub('t','i'),230,130),w=405,ratio=.41,ur=(text('ڈھال =',5,65)+frac('Δs','Δt',125,45)+text('=',188,65)+frac(sub('s','f')+' − '+sub('s','i'),sub('t','f')+' − '+sub('t','i'),230,130)),ps=(text('میلان =',5,65)+frac('Δs','Δt',125,45)+text('=',188,65)+frac(sub('s','f')+' − '+sub('s','i'),sub('t','f')+' − '+sub('t','i'),230,130)))
b=text('speed v =',5,65)+frac('100 m − 0 m','10 s − 0 s',160,180)+text('=',360,65)+frac('100 m','10 s',397,95)+text('= 10 ms⁻¹',515,65)
c=block('physics9-distance-time-speed-calculation',b,w=675,ratio=.66,label='Distance-time slope:100 metres minus0 over10 seconds minus0 equals10 metres per second',ur=b.replace('speed','رفتار'),ps=b.replace('speed','چټکتیا'))
quiz=''
for i in range(2):
 quiz+=f'<g transform="translate({i*235},0)"><rect x="10" y="10" width="210" height="190" fill="#fff" stroke="#7c838a"/><rect x="150" y="10" width="49" height="29" fill="#fff" stroke="#333"/><path d="M41 57V183M27 172H202" stroke="#111" stroke-width="2"/>'+text('S (m)',47,51,'middle',20)+text('t (s)',202,193,'middle',20)+text('0',30,194,'middle',18)
 if i==0:quiz+='<path d="M41 172L165 140M41 172L139 106M41 172L70 96" stroke="#a0352e" stroke-width="3" fill="none"/>'+text('A',174,145,size=20)+text('B',145,105,size=20)+text('C',71,88,size=20)
 else:quiz+='<path d="M41 172C149 180 167 139 186 91M41 172C38 104 67 73 174 72" stroke="#a0352e" stroke-width="3" fill="none"/>'+text('A',189,112,size=20)+text('B',151,61,size=20)
 quiz+='</g>'
qz=block('physics9-distance-time-quiz',quiz,w=475,h=210,ratio=.54,label='Distance-time quiz: three straight slopes A shallow B middle C steep; second graph A concave-up B concave-down; blank answer boxes',kind='graph')
qz['graphData']=dict(left=['A shallow straight','B medium straight','C steep straight'],right=['A increasing slope','B decreasing slope'],axes=['S (m)','t (s)'])
graphs=''
for i in range(3):
 g='<rect x="4" y="9" width="222" height="202" fill="#fff"/>'
 for x in range(4,227,14):g+=f'<path d="M{x} 9V211" stroke="#cebdc7" stroke-width=".7"/>'
 for y in range(9,212,14):g+=f'<path d="M4 {y}H226" stroke="#cebdc7" stroke-width=".7"/>'
 g+='<path d="M40 41V190M20 179H180" stroke="#111" stroke-width="2"/>'+text('S (m)',44,29,'middle',20)+text('t (s)',203,187,'middle',20)+text('0',28,207,'middle',18)
 path=['M40 68H178','M40 179L178 64','M40 179C61 68 140 47 177 51'][i]
 g+=f'<path d="{path}" stroke="#2f784f" stroke-width="3" fill="none"/>'
 graphs+=f'<g transform="translate({i*235},0)">{g}</g>'
fig=block('physics9-distance-time-interpretation-figure210',graphs,w=710,h=220,ratio=.98,label='Figure2.10: zero-speed horizontal distance line; uniform-speed straight rising line; variable-speed rising concave-down curve',kind='graph')
fig['graphData']=dict(panels=['constant positive distance','linearly increasing distance from origin','nonlinear increasing distance with decreasing slope'],axes=['S (m)','t (s)'])
s=section('2.4.1','2.4.1 DISTANCE-TIME GRAPH','2.4.1 فاصلہ وقت گراف','2.4.1 د واټن او وخت ګراف',p,[f,c,qz,fig],[para(0),visual(f),para(1),visual(c),para(2,'heading'),visual(qz),dict(type='parallelPhrases',columns=[[3],[4]]),para(5,'heading'),visual(fig),dict(type='parallelPhrases',columns=[[6,7],[8,9],[10,11]])])
s['continuesPreviousParagraph']=True
r=[
pair('The graph plotted between speed (v) and time (t) is called speed-time graph. In this graphical analysis the speed is plotted along vertical axis (y-axis) and time along horizontal axis (x-axis). Speed time graph is useful for two purposes.','رفتار (v) اور وقت (t) کے درمیان بنایا گیا گراف رفتار وقت گراف کہلاتا ہے۔ اس تجزیے میں رفتار عمودی محور (y محور) اور وقت افقی محور (x محور) پر دکھاتے ہیں۔ رفتار وقت گراف دو مقاصد کے لیے مفید ہے۔','د چټکتیا (v) او وخت (t) ترمنځ رسم شوی ګراف د چټکتیا او وخت ګراف بلل کېږي. په دې ګرافیکي تحلیل کې چټکتیا پر عمودي محور (y محور) او وخت پر افقي محور (x محور) رسمېږي. د چټکتیا او وخت ګراف د دوو موخو لپاره ګټور دی.'),
pair('A. Slope or gradient of the graph gives magnitude of acceleration','A. گراف کی ڈھال تعجیل کی مقدار دیتی ہے۔','A. د ګراف میلان د تعجیل اندازه ورکوي.'),
pair('B. Area under the graph gives distance traveled.','B. گراف کے نیچے کا رقبہ طے کردہ فاصلہ دیتا ہے۔','B. د ګراف لاندې مساحت وهل شوی واټن ورکوي.'),
pair('A. The slope of speed time curve gives magnitude of acceleration.','A. رفتار وقت منحنی کی ڈھال تعجیل کی مقدار دیتی ہے۔','A. د چټکتیا او وخت منحني میلان د تعجیل اندازه ورکوي.'),
pair('Consider the motion of the object which speeds up from 0 m/s to 8 m/s in 4s, the','اس شے کی حرکت پر غور کریں جس کی رفتار 4s میں 0 m/s سے 8 m/s ہو جاتی ہے، اس','د هغه شي حرکت ته پام وکړئ چې چټکتیا یې په 4s کې له 0 m/s څخه 8 m/s ته زیاتېږي، د')]
save(49,'Distance-time slope calculation / quizzes / Figure2.10 / speed-time introduction',[s,section('2.4.2','2.4.2 SPEED - TIME GRAPH','2.4.2 رفتار وقت گراف','2.4.2 د چټکتیا او وخت ګراف',r,[],[para(0),dict(type='numberedList',indices=[1,2]),para(3,'heading'),para(4)])],'Fresh visible source inspection. Joined source paragraph continuation from page48 without duplicate displayed paragraph. Restored two fraction calculations, two native quiz graphs with original blank answer boxes, Figure2.10 three grid plots with constant/linear/concave-down geometry and three aligned caption columns. Original spiking down wording retained. Speed-time introduction, two uses and final acceleration example fragment preserved, explicitly translated. No quiz answers invented.')
