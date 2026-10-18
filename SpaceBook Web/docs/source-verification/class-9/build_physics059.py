from physics_page_tools import *

p=[
pair('Figure “a” shows the well-known phenomenon of a rock falling faster than a sheet of paper. The effect of air resistance is responsible for the slower fall of the paper. When air is removed from the tube, as in Figure “b”, the rock and the paper have exactly the same acceleration due to gravity. In the absence of air, the rock and the paper both fall freely.','شکل “a” معروف مظہر دکھاتی ہے کہ پتھر کاغذ کی چادر سے تیز گرتا ہے۔ کاغذ کے آہستہ گرنے کی وجہ ہوا کی مزاحمت ہے۔ شکل “b” کی طرح نلی سے ہوا نکال دی جائے تو پتھر اور کاغذ کی ثقلی تعجیل بالکل یکساں ہوتی ہے۔ ہوا نہ ہونے پر دونوں آزادانہ گرتے ہیں۔','شکل “a” هغه پېژندل شوې پدیده ښيي چې ډبره د کاغذ تر پاڼې ګړندۍ لوېږي. د هوا د مقاومت اغېز د کاغذ د ورو لوېدو لامل دی. کله چې د شکل “b” په څېر له نل څخه هوا وایستل شي، ډبره او کاغذ د جاذبې له امله بالکل یو شان تعجیل لري. د هوا په نشتوالي کې دواړه ازاد لوېږي.'),
pair('Since the acceleration is constant in free-fall, the equations of kinematics can be used. In these equations we replace acceleration ‘a’ with acceleration due to gravity ‘g’ and distance ‘s’ with height ‘h’.','آزاد سقوط میں تعجیل مستقل ہوتی ہے، اس لیے حرکیات کی مساوات استعمال کی جا سکتی ہیں۔ ان میں تعجیل ‘a’ کو ثقلی تعجیل ‘g’ اور فاصلہ ‘s’ کو بلندی ‘h’ سے بدلتے ہیں۔','په ازاد سقوط کې تعجیل ثابت دی، نو د کینماتیک معادلې کارول کېدای شي. په دې معادلو کې تعجیل ‘a’ د جاذبې په تعجیل ‘g’ او واټن ‘s’ په لوړوالي ‘h’ بدلوو.'),
pair('When an object moves with the gravity acceleration due to gravity is taken as positive (+g) and when an object moves against gravity, acceleration due to gravity is taken negative (-g).','جب شے کشش ثقل کے ساتھ حرکت کرے تو ثقلی تعجیل مثبت (+g) لیتے ہیں، اور جب کشش ثقل کے خلاف حرکت کرے تو ثقلی تعجیل منفی (-g) لیتے ہیں۔','کله چې یو شی له جاذبې سره حرکت کوي، د جاذبې تعجیل مثبت (+g) ګڼل کېږي، او کله چې د جاذبې پر خلاف حرکت کوي، د جاذبې تعجیل منفي (-g) ګڼل کېږي.'),
pair('LAB WORK','لیبارٹری کا کام','لابراتواري کار'),
pair('Find the value of “g” by free fall method.','آزاد سقوط کے طریقے سے “g” کی قدر معلوم کریں۔','د ازاد سقوط په طریقه د “g” ارزښت ومومئ.'),
pair('Example 2.7 HEIGHT OF BRIDGE FROM WATER SURFACE','مثال 2.7 پانی کی سطح سے پل کی بلندی','بېلګه 2.7 د اوبو له سطحې د پله لوړوالی'),
pair('A stone is dropped from the Attock Bridge. The stone reaches the water in 3.2 s. Find the a. height of the bridge from water and b. velocity of the stone when it strikes the water.','اٹک پل سے پتھر گرایا جاتا ہے، جو 3.2 s میں پانی تک پہنچتا ہے۔ a. پانی سے پل کی بلندی اور b. پانی سے ٹکراتے وقت پتھر کی سمتی رفتار معلوم کریں۔','له اټک پله څخه یوه ډبره غورځول کېږي. ډبره په 3.2 s کې اوبو ته رسېږي. a. له اوبو څخه د پله لوړوالی او b. له اوبو سره د لګېدو پر مهال د ډبرې سرعت ومومئ.'),
pair('SOLUTION','حل','حل'),
pair('GIVEN:','دیے گئے:','ورکړل شوي:'),
pair('Time t = 3.2 s','وقت t = 3.2 s','وخت t = 3.2 s'),
pair('Initial velocity vᵢ = 0 ms⁻¹','ابتدائی سمتی رفتار vᵢ = 0 ms⁻¹','لومړنی سرعت vᵢ = 0 ms⁻¹'),
pair('Acceleration due to gravity g = 9.8 ms⁻²','ثقلی تعجیل g = 9.8 ms⁻²','د جاذبې تعجیل g = 9.8 ms⁻²'),
pair('REQUIRED:','مطلوب:','غوښتل شوي:'),
pair('a. Height h = ?','a. بلندی h = ؟','a. لوړوالی h = ؟'),
pair('b. Final velocity v𝒇 = ?','b. آخری سمتی رفتار v𝒇 = ؟','b. وروستی سرعت v𝒇 = ؟'),
pair('a. By second equation of motion','a. حرکت کی دوسری مساوات سے','a. د حرکت د دویمې معادلې له مخې'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('Rounding off to correct significant figures','درست بامعنی ہندسوں تک قریب ترین قدر لینے سے','د سمو بامعنی شمېرو لپاره په ګردولو'),
pair('Answer','جواب','ځواب')]

f1=block('physics9-free-fall-equation215',text(sub('v','f')+' = '+sub('v','i')+' + gt',5,43)+number('2.15',385,15),w=475,h=80,ratio=.49,label='Equation2.15 final velocity equals initial velocity plus g times t')
f2=block('physics9-free-fall-equation216',text('h = '+sub('v','i')+'t +',5,65)+frac('1','2',185,30)+text('gt²',242,65)+number('2.16',395),w=490,ratio=.51,label='Equation2.16 height equals initial velocity times time plus one half g times time squared')
f3=block('physics9-free-fall-equation217',text('2gh = '+sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),5,43)+number('2.17',430,15),w=515,h=80,ratio=.53,label='Equation2.17 twice g times height equals final velocity squared minus initial velocity squared')
formula=block('physics9-example27-height-formula',text('h = '+sub('v','i')+'t +',5,65)+frac('1','2',185,30)+text('gt²',242,65),w=340,ratio=.36)
values=block('physics9-example27-height-values',text('h = 0 ms⁻¹ × 3.2 s +',5,65)+frac('1','2',310,30)+text('× 9.8 ms⁻² × (3.2)²',366,65),w=715,ratio=.76)
height=block('physics9-example27-height-unrounded',text('h = 50.176 m',5,43),w=245,h=75,ratio=.27)
ans=block('physics9-example27-height-answer',text('h = 50 m',5,43),w=170,h=75,ratio=.19)
num=dict(num='2.7',name='HEIGHT OF BRIDGE FROM WATER SURFACE',statement=p[6]['text'],given='\n'.join(q['text'] for q in p[9:12]),required=p[13]['text']+'\n'+p[14]['text'],formula='<div style="max-width:220px">'+formula['svg']+'</div>',solution='<div style="max-width:430px">'+values['svg']+height['svg']+'</div>',answer='a. h = 50 m',answerSource='textbook',sourcePendingContinuation=True,sourcePdfPage=59,sourcePrintedPage=54,pairedParagraphs=p[6:20])
layout=[para(0),para(1),visual(f1),visual(f2),visual(f3),para(2),para(3,'heading'),para(4,'quotation'),para(5,'heading'),para(6),para(7,'heading'),dict(type='parallelPhrases',columns=[[8,9,10,11],[12,13,14]]),para(15),visual(formula),para(16),visual(values),para(17),visual(height),para(18),visual(ans),para(19)]
save(59,'Free-fall equations2.15–2.17 / lab work / bridge Example2.7 beginning',[section('2.6','2.5 MOTION DUE TO GRAVITY:','2.5 کشش ثقل سے حرکت:','2.5 د جاذبې له امله حرکت:',p,[f1,f2,f3,formula,values,height,ans],layout)],'Fresh visible source inspection. Complete tube explanation, constant-gravity substitution paragraph and original +/-g convention restored with native numbered equations2.15–2.17. Free-fall lab instruction and original Attock Bridge3.2s problem/given/required/height solution preserved, including50.176m then50m source rounding. Complete paragraph translations aligned; final velocity subpart explicitly pending consecutive next page.',numericals=[num],activities=[dict(num='source-lab-free-fall',name='LAB WORK',procedure=p[4]['text'],urdu=p[4]['urdu'],pashto=p[4]['pashto'],sourcePdfPage=59,sourcePrintedPage=54)])
