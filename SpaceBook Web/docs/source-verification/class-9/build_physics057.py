from physics_page_tools import *

p=[
pair('SOLUTION','حل','حل'),
pair('a. To find final velocity we can use the first equation of motion','a. آخری سمتی رفتار معلوم کرنے کے لیے حرکت کی پہلی مساوات استعمال کر سکتے ہیں۔','a. د وروستي سرعت موندلو لپاره د حرکت لومړۍ معادله کارولای شو.'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('Answer','جواب','ځواب'),
pair('b. For the distance covered, we will use second equation of motion','b. طے کردہ فاصلے کے لیے حرکت کی دوسری مساوات استعمال کریں گے۔','b. د وهل شوي واټن لپاره به د حرکت دویمه معادله وکاروو.'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('Answer','جواب','ځواب'),
pair('EXTENSION EXERCISE 2.3','توسیعی مشق 2.3','پراختیايي تمرین 2.3'),
pair('This problem is captioned speeding motorcyclist. Is 41.8 m/s safe speed for motorcycle ride? Also verify the distance covered in this problem by third equation of motion.','اس مسئلے کا عنوان تیز ہوتا موٹر سائیکل سوار ہے۔ کیا موٹر سائیکل سواری کے لیے 41.8 m/s محفوظ رفتار ہے؟ اس مسئلے کا طے کردہ فاصلہ حرکت کی تیسری مساوات سے بھی تصدیق کریں۔','د دې مسئلې سرلیک ګړندی کېدونکی موټرسایکل چلوونکی دی. ایا 41.8 m/s د موټرسایکل د سپرلۍ لپاره خوندي چټکتیا ده؟ همدارنګه د حرکت په درېیمه معادله د دې مسئلې وهل شوی واټن تایید کړئ.'),
pair('Assignment 2.5 CYCLIST MOTION','اسائنمنٹ 2.5 سائیکل سوار کی حرکت','دنده 2.5 د بایسکل چلوونکي حرکت'),
pair('A cyclist is moving with uniform acceleration of 1.2 m/s². How much time will it require to change his velocity from 6 m/s to 12 m/s?','سائیکل سوار 1.2 m/s² کی یکساں تعجیل سے حرکت کر رہا ہے۔ اس کی سمتی رفتار 6 m/s سے 12 m/s ہونے کے لیے کتنا وقت چاہیے؟','یو بایسکل چلوونکی په 1.2 m/s² یوشان تعجیل حرکت کوي. څومره وخت ته اړتیا ده چې د هغه سرعت له 6 m/s څخه 12 m/s ته بدل شي؟'),
pair('Example 2.6. COMMERCIAL AIRCRAFT RUNWAY LENGTH','مثال 2.6. تجارتی ہوائی جہاز کے رن وے کی لمبائی','بېلګه 2.6. د سوداګریزې الوتکې د ځغاست لیکې اوږدوالی'),
pair('A Boeing 777 aircraft takes off at 295 km/h after accelerating from rest at 2.80 m/s². What is the minimum runway length required?','بوئنگ 777 ہوائی جہاز سکون سے 2.80 m/s² تعجیل حاصل کرنے کے بعد 295 km/h پر پرواز کرتا ہے۔ رن وے کی کم از کم مطلوبہ لمبائی کیا ہے؟','یوه بوینګ 777 الوتکه له سکون څخه په 2.80 m/s² تعجیل وروسته په 295 km/h الوتنه پیلوي. د ځغاست لیکې لږ تر لږه اړین اوږدوالی څومره دی؟'),
pair('SOLUTION','حل','حل'),
pair('GIVEN:','دیے گئے:','ورکړل شوي:'),
pair('initial velocity vᵢ = 0 km/h = 0 m/s','ابتدائی سمتی رفتار vᵢ = 0 km/h = 0 m/s','لومړنی سرعت vᵢ = 0 km/h = 0 m/s'),
pair('final velocity v𝒇 = 295 km/h = 81.9 m/s','آخری سمتی رفتار v𝒇 = 295 km/h = 81.9 m/s','وروستی سرعت v𝒇 = 295 km/h = 81.9 m/s'),
pair('acceleration = 2.80 m/s²','تعجیل = 2.80 m/s²','تعجیل = 2.80 m/s²'),
pair('REQUIRED:','مطلوب:','غوښتل شوي:'),
pair('distance s = ?','فاصلہ s = ؟','واټن s = ؟'),
pair('Conversion from km/h to m/s','km/h سے m/s میں تبدیلی','له km/h څخه m/s ته اړول'),
pair('Time is not given so we will use the third equation of motion','وقت نہیں دیا گیا، اس لیے حرکت کی تیسری مساوات استعمال کریں گے۔','وخت نه دی ورکړل شوی، نو د حرکت درېیمه معادله به وکاروو.'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('or','یا','یا'),
pair('Answer','جواب','ځواب')]

v=block('physics9-example25-first-formula',text(sub('v','f')+' = '+sub('v','i')+' + at',5,43),w=285,h=75,ratio=.32)
vc=block('physics9-example25-velocity-values',text(sub('v','f')+' = 0 m/s + 1.9 m/s² × 22 s',5,43),w=530,h=80,ratio=.59)
va=block('physics9-example25-velocity-answer',text(sub('v','f')+' = 41.8 m/s',5,43),w=285,h=75,ratio=.32)
s=block('physics9-example25-second-formula',text('s = '+sub('v','i')+'t +',5,65)+frac('1','2',185,30)+text('at²',242,65),w=340,ratio=.37)
sc=block('physics9-example25-distance-values',text('s = 0 m/s × 22 s +',5,65)+frac('1','2',310,30)+text('× 1.9 m/s² × (22 s)²',366,65),w=715,ratio=.79)
sa=block('physics9-example25-distance-answer',text('s = 459.8 m',5,43),w=225,h=75,ratio=.25)
conversion=block('physics9-example26-kmh-conversion',text('295 km/h =',5,65)+frac('295×10³ m','60×60 s',170,155)+text('=',345,65)+frac('295,000','3600 s',385,120)+text('= 81.9 m/s',525,65),w=715,ratio=.88)
b=text('2as = '+sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),5,65)+text('or',295,65)+text('s =',355,65)+frac(sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),'2a',440,160)
f=block('physics9-example26-third-formula',b,w=650,ratio=.72,ur=b.replace('>or<','>یا<'),ps=b.replace('>or<','>یا<'))
values=block('physics9-example26-runway-values',text('s =',5,65)+frac('(81.9 ms⁻¹)² − (0 ms⁻¹)²','2 × 2.80 ms⁻²',80,330),w=455,ratio=.51)
b=text('s =',5,65)+frac('6707.61 m² / s²','5.6 m / s²',80,245)+'<path d="M292 38l23 -28M227 102l27 -35M262 103l29 -31" stroke="#333" stroke-width="2"/>'
reduced=block('physics9-example26-runway-reduced',b,w=375,ratio=.43,label='Runway fraction6707.61 square metres per second squared over5.6 metres per second squared with source unit cancellation marks')
ans=block('physics9-example26-runway-answer',text('s = 1197.7875 m',5,43),w=310,h=75,ratio=.35)
prev=OUT/'physics-page-056.json';page=json.loads(prev.read_text(encoding='utf-8'));num=page['numericals'][0]
num.update(formula='<div style="max-width:280px">'+v['svg']+s['svg']+'</div>',solution='<div style="max-width:400px">'+vc['svg']+sc['svg']+'</div>',answer='v𝒇 = 41.8 m/s; s = 459.8 m',answerSource='textbook',sourcePendingContinuation=False,sourcePdfPages=[56,57],sourcePrintedPages=[51,52],pairedParagraphs=num['pairedParagraphs']+p[:11])
prev.write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
num2=dict(num='2.6',name='COMMERCIAL AIRCRAFT RUNWAY LENGTH',statement=p[14]['text'],given='\n'.join(q['text'] for q in p[17:20]),required=p[21]['text'],formula='<div style="max-width:390px">'+f['svg']+'</div>',solution='<div style="max-width:440px">'+conversion['svg']+values['svg']+reduced['svg']+'</div>',answer='s = 1197.7875 m',answerSource='textbook',sourcePdfPage=57,sourcePrintedPage=52,pairedParagraphs=p[14:27])
layout=[para(0,'heading'),para(1),visual(v),para(2),visual(vc),para(3),visual(va),para(4),para(5),visual(s),para(6),visual(sc),para(7),visual(sa),para(8),para(9,'heading'),para(10),para(11,'heading'),para(12),para(13,'heading'),para(14),para(15,'heading'),dict(type='parallelPhrases',columns=[[16,17,18,19],[20,21]]),para(22,'heading'),visual(conversion),para(23),visual(f),para(24),visual(values),visual(reduced),para(25),visual(ans),para(26)]
save(57,'Example2.5 solution / extension / Assignment2.5 / full aircraft Example2.6',[section('2.5','2.5 EQUATIONS OF MOTION','2.5 حرکت کی مساوات','2.5 د حرکت معادلې',p,[v,vc,va,s,sc,sa,conversion,f,values,reduced,ans],layout)],'Fresh visible source inspection. Complete motorcyclist first/second-equation solutions41.8m/s and459.8m, extension safety question and1.2m/s² cyclist assignment restored. Original aircraft Example2.6 preserved with Boeing777,295km/h,2.80m/s²,81.9m/s conversion, third-equation fractions, unit-cancellation marks,6707.61/5.6 and1197.7875m printed answer. All source prose explicitly paired; numerical bank upserts actualsource Examples2.5/2.6 without adding assignment answers.',numericals=[num,num2],activities=[dict(num='Assignment 2.5',name='CYCLIST MOTION',procedure=p[12]['text'],urdu=p[12]['urdu'],pashto=p[12]['pashto'],sourcePdfPage=57,sourcePrintedPage=52)])
