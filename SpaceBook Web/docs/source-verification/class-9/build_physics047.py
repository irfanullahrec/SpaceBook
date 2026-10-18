from physics_page_tools import *

p=[
pair('Example 2.3 ACCELERATION OF CAR','مثال 2.3 گاڑی کی تعجیل','بېلګه 2.3 د موټر تعجیل'),
pair('You observe that your car accelerate from rest to 140 km/h in just 17.6 seconds on straight road towards east. What is the acceleration of your car.','آپ دیکھتے ہیں کہ مشرق کی طرف سیدھی سڑک پر آپ کی گاڑی سکون سے صرف 17.6 سیکنڈ میں 140 km/h تک تیز ہوتی ہے۔ آپ کی گاڑی کی تعجیل کیا ہے۔','تاسو ګورئ چې ستاسو موټر ختیځ ته پر مستقیم سړک له سکون څخه یوازې په 17.6 ثانیو کې 140 km/h ته ګړندی کېږي. ستاسو د موټر تعجیل څومره دی.'),
pair('SOLUTION','حل','حل'),
pair('GIVEN:','دیے گئے:','ورکړل شوي:'),
pair('initial velocity vᵢ = 0 km/h East = 0 m/s East','ابتدائی سمتی رفتار vᵢ = 0 km/h مشرق = 0 m/s مشرق','لومړنی سرعت vᵢ = 0 km/h ختیځ = 0 m/s ختیځ'),
pair('final velocity v𝒇 = 140 km/h East = 38.88 m/s East','آخری سمتی رفتار v𝒇 = 140 km/h مشرق = 38.88 m/s مشرق','وروستی سرعت v𝒇 = 140 km/h ختیځ = 38.88 m/s ختیځ'),
pair('time elapsed Δt = 17.6 s','گزرا ہوا وقت Δt = 17.6 s','تېر شوی وخت Δt = 17.6 s'),
pair('REQUIRED:','مطلوب:','غوښتل شوي:'),
pair('acceleration a = ?','تعجیل a = ؟','تعجیل a = ؟'),
pair('Conversion from km/h to m/s','km/h سے m/s میں تبدیلی','له km/h څخه m/s ته اړول'),
pair('From the definition of acceleration, equation 2.7 gives','تعجیل کی تعریف سے مساوات 2.7 دیتی ہے۔','د تعجیل له تعریفه، 2.7 معادله ورکوي'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('or','یا','یا'),
pair('therefore','لہٰذا','نو'),
pair('Answer','جواب','ځواب'),
pair('EXTENSION EXERCISE 2.2','توسیعی مشق 2.2','پراختیايي تمرین 2.2'),
pair('In this example, when the driver apply breaks in what direction will the resulting acceleration points?','اس مثال میں جب ڈرائیور بریک لگائے تو پیدا ہونے والی تعجیل کس سمت میں ہوگی؟','په دې بېلګه کې، کله چې چلوونکی بریک ووهي، رامنځته کېدونکی تعجیل به په کوم لوري وي؟'),
pair('Assignment 2.3 CAR’S ACCELERATION','اسائنمنٹ 2.3 گاڑی کی تعجیل','دنده 2.3 د موټر تعجیل'),
pair('If in the same experiment you take the readings of the speedometer of the car as 20 km/h in the 4ᵗʰ second and 32 km/h in the 9ᵗʰ second. What is the acceleration of your car in this interval?','اگر اسی تجربے میں آپ گاڑی کے اسپیڈومیٹر سے چوتھے سیکنڈ میں 20 km/h اور نویں سیکنڈ میں 32 km/h کی قرأت لیں، تو اس وقفے میں آپ کی گاڑی کی تعجیل کیا ہے؟','که په همدې تجربه کې د موټر د چټکتیا سنج لوستنې په څلورمه ثانیه کې 20 km/h او په نهمه ثانیه کې 32 km/h واخلئ، په دې واټن کې ستاسو د موټر تعجیل څومره دی؟'),
pair('INTERESTING INFORMATION CONTINENTAL DRIFT','دلچسپ معلومات براعظمی سرکاؤ','په زړه پورې معلومات د لویو وچو خوځېدنه'),
pair('Continental Drift is the movement of the Earth’s continents relative to each other, thus appearing to ‘drift’ across the ocean bed. The continental plates (therefore continents) move across the surface of the Earth at the geologically slow rate of 1-10 cm/year or 1-10 m/century. This is about the same speed that fingernails and hair grow.','براعظمی سرکاؤ زمین کے براعظموں کی ایک دوسرے کے مقابل حرکت ہے، جس سے وہ سمندر کی تہہ پر ’’سرکتے‘‘ دکھائی دیتے ہیں۔ براعظمی پلیٹیں (اور اس طرح براعظم) سطحِ زمین پر ارضیاتی لحاظ سے سست شرح، 1-10 cm/year یا 1-10 m/century سے حرکت کرتی ہیں۔ یہ تقریباً ناخنوں اور بالوں کے بڑھنے کی رفتار ہے۔','د لویو وچو خوځېدنه د ځمکې د لویو وچو یو د بل په نسبت حرکت دی، نو داسې ښکاري چې د سمندر پر تل «خوځېږي». د لویو وچو تختې (او له همدې امله لویې وچې) د ځمکې پر سطحه د جیولوژۍ له مخې په ورو کچه، 1-10 cm/year یا 1-10 m/century خوځېږي. دا نږدې د نوکانو او ویښتو د ودې چټکتیا ده.')]

conv=block('physics9-example23-kmh-conversion',text('140 km/h =',5,63)+frac('140×10³ m','60×60 s',170,160)+text('=',345,63)+frac('140,000','3600 s',383,130)+text('= 38.9 m/s',530,63),w=705,ratio=.67,label='140 kilometres per hour conversion with two fractions equals38.9 metres per second')
car='<path d="M20 82Q32 48 81 45L132 47L160 65L189 72L202 93L196 114H16L10 97Z" fill="#f1eeee" stroke="#303339" stroke-width="3"/><path d="M47 66L78 49H126L150 65Z" fill="#373442" stroke="#343b43" stroke-width="2"/><path d="M116 49v64M47 72h123M19 82h48" stroke="#6e6266" fill="none"/><circle cx="49" cy="110" r="22" fill="#27272d" stroke="#908d96" stroke-width="3"/><circle cx="49" cy="110" r="13" fill="#757982"/><circle cx="167" cy="110" r="22" fill="#27272d" stroke="#908d96" stroke-width="3"/><circle cx="167" cy="110" r="13" fill="#757982"/>'
photo=block('physics9-example23-car-photo','<rect width="250" height="170" fill="#554959"/><path d="M0 10Q80 40 140 15L250 37V116L0 63Z" fill="#72626d"/><path d="M0 84L250 151v19H0Z" fill="#939197"/><g transform="translate(9,42) scale(.98,.8)">'+car.replace('#f1eeee','#9b99a6')+'</g>',w=250,h=170,ratio=.27,label='Car travelling to the right on a sloped perspective road, as pictured in Example2.3',kind='illustration')
diagram='<g transform="translate(5,10)">'+car+'</g><path d="M229 98H505" stroke="#111" stroke-width="4"/><path d="M505 98l-18 -10v20Z" fill="#111"/>'+text('a⃗',354,84,size=28)+'<path d="M583 75v55M562 101h43" stroke="#a82e32" stroke-width="3"/><path d="M583 75l-5 9h10Z M583 130l-5 -9h10Z M562 101l9 -5v10Z M605 101l-9 -5v10Z" fill="#a82e32"/>'+text('N',583,65,'middle',18)+text('S',583,155,'middle',18)+text('W',549,108,'middle',18)+text('E',621,108,'middle',18)
d=block('physics9-example23-acceleration-car',diagram,w=640,h=175,ratio=.88,label='Car pointing east, eastward acceleration vector and NEWS geographic axes',kind='vector')
form=text('a⃗ =',5,63)+frac('Δv⃗','Δt',85,50)+text('or',165,63)+text('a⃗ =',220,63)+frac(sub('v⃗','f')+' − '+sub('v⃗','i'),'Δt',299,125)
f=block('physics9-example23-acceleration-formula',form,w=470,ratio=.49,ur=form.replace('>or<','>یا<'),ps=form.replace('>or<','>یا<'))
values=text('a⃗ =',5,63)+frac('(38.9 − 0) m/s','17.6 s',90,210)+text('East',319,63)
val=block('physics9-example23-values',values,w=400,ratio=.42,ur=values.replace('East','مشرق'),ps=values.replace('East','ختیځ'))
values=text('a⃗ =',5,63)+frac('38.9 m/s','17.6 s',90,125)+text('East',230,63)
short=block('physics9-example23-reducedvalues',values,w=320,ratio=.34,ur=values.replace('East','مشرق'),ps=values.replace('East','ختیځ'))
ans=text('a⃗ = 2.2 m/s² East',8,45)
a=block('physics9-example23-answer',ans,w=340,h=75,ratio=.37,label='Printed acceleration answer:2.2 metres per second squared East',ur=ans.replace('East','مشرق'),ps=ans.replace('East','ختیځ'))
layout=[para(0,'heading'),para(1),para(2,'heading'),dict(type='parallelPhrases',columns=[[3,4,5,6],[7,8]]),para(9,'heading'),visual(conv),visual(photo),visual(d),para(10),visual(f),para(11),visual(val),para(12),visual(short),para(13),visual(a),para(14),para(15,'heading'),para(16),para(17,'heading'),para(18),para(19,'heading'),para(20,'quotation')]
num=dict(num='2.3',name='ACCELERATION OF CAR',statement=p[1]['text'],given='\n'.join(q['text'] for q in p[4:7]),required=p[8]['text'],formula='<div style="max-width:300px">'+f['svg']+'</div>',solution='<div style="max-width:300px">'+conv['svg']+val['svg']+short['svg']+'</div>',answer='a⃗ = 2.2 m/s² East',answerSource='textbook',sourcePdfPage=47,sourcePrintedPage=42,pairedParagraphs=p[1:17])
save(47,'Example 2.3 acceleration of car / extension / Assignment2.3 / continental drift',[section('2.3.5','2.3.5 ACCELERATION:','2.3.5 تعجیل:','2.3.5 تعجیل:',p,[conv,photo,d,f,val,short,a],layout)],'Fresh visible source inspection. Replaced unrelated legacy braking Example2.3 with original140km/h/17.6s eastward-car problem,38.88m/s GIVEN and38.9m/s calculation precision preserved. All conversion and acceleration fractions restored plus original2.2m/s²East answer. Two native car visuals at original ratios, NEWS axis, acceleration arrow, original breaks spelling/question,20/32kmh assignment and full continental-drift note retained with explicit translations. No extension or assignment solution added.',numericals=[num],activities=[dict(num='Assignment 2.3',name='CAR’S ACCELERATION',procedure=p[18]['text'],urdu=p[18]['urdu'],pashto=p[18]['pashto'],sourcePdfPage=47,sourcePrintedPage=42)])
