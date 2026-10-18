from physics_page_tools import *

p=[
pair('b. By First equation of motion','b. حرکت کی پہلی مساوات سے','b. د حرکت د لومړۍ معادلې له مخې'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('Rounding off to correct significant figures','درست بامعنی ہندسوں تک قریب ترین قدر لینے سے','د سمو بامعنی شمېرو لپاره په ګردولو'),
pair('Answer','جواب','ځواب'),
pair('Assignment 2.7 CRICKET BALL','اسائنمنٹ 2.7 کرکٹ کی گیند','دنده 2.7 د کرکټ توپ'),
pair('In a cricket match ball go straight up with a velocity of 40 m/s. Calculate','کرکٹ میچ میں گیند 40 m/s سمتی رفتار سے سیدھی اوپر جاتی ہے۔ معلوم کریں','د کرکټ په یوه لوبه کې توپ په 40 m/s سرعت نېغ پورته ځي. محاسبه کړئ'),
pair('a) maximum height ball will reach','a) گیند کی زیادہ سے زیادہ پہنچنے کی بلندی','a) تر ټولو زیات لوړوالی چې توپ ورته رسېږي'),
pair('b) time to reach that height.','b) اس بلندی تک پہنچنے کا وقت۔','b) هغه لوړوالي ته د رسېدو وخت.')]
v=block('physics9-example27-velocity-formula',text(sub('v','f')+' = '+sub('v','i')+' + gt',5,43),w=285,h=75,ratio=.31)
c=block('physics9-example27-velocity-values',text(sub('v','f')+' = 0 ms⁻¹ + 9.8 ms⁻² × 3.2 s',5,43),w=565,h=80,ratio=.62)
unrounded=block('physics9-example27-velocity-unrounded',text(sub('v','f')+' = 31.36 ms⁻¹',5,43),w=305,h=75,ratio=.34)
ans=block('physics9-example27-velocity-answer',text(sub('v','f')+' = 31 ms⁻¹',5,43),w=255,h=75,ratio=.28)
prev=OUT/'physics-page-059.json';page=json.loads(prev.read_text(encoding='utf-8'));num=page['numericals'][0]
num.update(formula=num['formula']+'<div style="max-width:190px">'+v['svg']+'</div>',solution=num['solution']+'<div style="max-width:360px">'+c['svg']+unrounded['svg']+'</div>',answer='a. h = 50 m; b. v𝒇 = 31 ms⁻¹',answerSource='textbook',sourcePendingContinuation=False,sourcePdfPages=[59,60],sourcePrintedPages=[54,55],pairedParagraphs=num['pairedParagraphs']+p[:5])
prev.write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

q=[
pair('Mechanics: The branch of Physics, which deals with the motion of bodies.','میکانکس: طبیعیات کی وہ شاخ جو جسموں کی حرکت سے متعلق ہے۔','میکانیک: د فزیک هغه څانګه چې د جسمونو له حرکت سره سروکار لري.'),
pair('Kinematics: The branch of physics, which deals with discussion of motion of object without reference to the forces causing the motion.','حرکیات: طبیعیات کی وہ شاخ جو حرکت پیدا کرنے والی قوتوں کا حوالہ دیے بغیر شے کی حرکت پر بحث کرتی ہے۔','کینماتیک: د فزیک هغه څانګه چې د حرکت رامنځته کوونکو قواؤ له یادونې پرته د شي د حرکت په اړه بحث کوي.'),
pair('Dynamics: It is the study of motion of bodies under the action of a force.','ڈائنامکس: قوت کے عمل کے تحت جسموں کی حرکت کا مطالعہ ہے۔','ډینامیک: د قوې تر اغېز لاندې د جسمونو د حرکت مطالعه ده.'),
pair('Rest: A body is said to be at rest if it does not change its position with respect to an observer.','سکون: جسم ساکن کہلاتا ہے اگر مبصر کے لحاظ سے اس کا مقام نہ بدلے۔','سکون: یو جسم په سکون کې بلل کېږي که د کتونکي په نسبت خپل موقعیت نه بدلوي.'),
pair('Motion: A body is said to be in motion if it changes its position with respect to an observer.','حرکت: جسم متحرک کہلاتا ہے اگر مبصر کے لحاظ سے اس کا مقام بدلے۔','حرکت: یو جسم په حرکت کې بلل کېږي که د کتونکي په نسبت خپل موقعیت بدلوي.'),
pair('Types of Motion: There are three main types of motion','حرکت کی اقسام: حرکت کی تین بنیادی اقسام ہیں۔','د حرکت ډولونه: د حرکت درې اصلي ډولونه شته'),
pair('a) Translatory Motion','a) انتقالی حرکت','a) انتقالی حرکت'),
pair('b) Rotatory Motion','b) دورانی حرکت','b) دوراني حرکت'),
pair('c) Vibratory Motion','c) ارتعاشی حرکت','c) اهتزازي حرکت'),
pair('Scalars: Physical quantities completely specified by its magnitude, that is, a proper unit and a number are called scalars.','عددی مقداریں: وہ طبیعی مقداریں جو اپنی مقدار، یعنی مناسب اکائی اور عدد، سے مکمل بیان ہوں، عددی مقداریں کہلاتی ہیں۔','سکالرونه: هغه فزیکي کمیتونه چې په خپلې اندازې، یعنې مناسب واحد او شمېر، بشپړ مشخص شي، سکالرونه بلل کېږي.'),
pair('Vectors: Physical quantities completely specified by magnitude, as well as direction are called vectors.','سمتی مقداریں: وہ طبیعی مقداریں جو مقدار اور سمت دونوں سے مکمل بیان ہوں، سمتی مقداریں کہلاتی ہیں۔','ویکټورونه: هغه فزیکي کمیتونه چې په اندازې او همدارنګه لوري بشپړ مشخص شي، ویکټورونه بلل کېږي.'),
pair('Position: The distance and direction of a body from a fixed point shows its position.','مقام: مقرر نقطے سے جسم کا فاصلہ اور سمت اس کا مقام ظاہر کرتے ہیں۔','موقعیت: له یوه ثابت ټکي څخه د جسم واټن او لوری د هغه موقعیت ښيي.'),
pair('Displacement: The shortest distance from the initial and final position of a body is called displacement.','نقل مکانی: جسم کے ابتدائی اور آخری مقام کے درمیان مختصر ترین فاصلہ نقل مکانی کہلاتا ہے۔','بېځایه کېدل: د جسم د لومړني او وروستي موقعیت ترمنځ تر ټولو لنډ واټن بېځایه کېدل بلل کېږي.'),
pair('Speed: time rate of change of distance is called speed it is a scalar quantity.','رفتار: فاصلے کی تبدیلی کی زمانی شرح رفتار کہلاتی ہے؛ یہ عددی مقدار ہے۔','چټکتیا: د واټن د بدلون زماني کچه چټکتیا بلل کېږي؛ دا سکالر کمیت دی.'),
pair('Velocity: The time rate of change of displacement is called velocity it is a vector quantity.','سمتی رفتار: نقل مکانی کی تبدیلی کی زمانی شرح سمتی رفتار کہلاتی ہے؛ یہ سمتی مقدار ہے۔','سرعت: د بېځایه کېدو د بدلون زماني کچه سرعت بلل کېږي؛ دا ویکټوري کمیت دی.'),
pair('Acceleration: The time rate of change of velocity is called acceleration.','تعجیل: سمتی رفتار کی تبدیلی کی زمانی شرح تعجیل کہلاتی ہے۔','تعجیل: د سرعت د بدلون زماني کچه تعجیل بلل کېږي.'),
pair('Equations of Motion: The inter-relationship of velocity, uniform acceleration, time interval and displacement of an object are expressed by the following equations:','حرکت کی مساوات: شے کی سمتی رفتار، یکساں تعجیل، وقفۂ وقت اور نقل مکانی کے باہمی تعلق کو درج ذیل مساوات سے ظاہر کرتے ہیں:','د حرکت معادلې: د شي د سرعت، یوشان تعجیل، د وخت واټن او بېځایه کېدو متقابلې اړیکې په لاندې معادلو ښودل کېږي:')]
eq=block('physics9-key-points-motion-equations',text('a. '+sub('v','f')+' = '+sub('v','i')+' + at',5,65)+text('b. s = '+sub('v','i')+'t +',358,65)+frac('1','2',570,30)+text('at²',625,65)+text('c. 2as = '+sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),745,65),w=1080,ratio=.98,label='Source key points a,b,c: all three equations of motion with subscripts, half fraction and squares')
links=[dict(name='First Equation of Motion',blockIds=['physics9-first-motion-equation212']),dict(name='Second Equation of Motion',blockIds=['physics9-second-motion-equation213']),dict(name='Third Equation of Motion',blockIds=['physics9-third-motion-equation214']),dict(name='Average Speed',blockIds=['physics9-average-speed-equation22']),dict(name='Acceleration',blockIds=['physics9-acceleration-equation27']),dict(name='Free Fall Equations',blockIds=['physics9-free-fall-equation215','physics9-free-fall-equation216','physics9-free-fall-equation217'])]
layout=[para(i) for i in range(6)]+[dict(type='parallelPhrases',columns=[[6],[7],[8]])]+[para(i) for i in range(9,17)]+[visual(eq)]
save(60,'Example2.7 completed velocity / Assignment2.7 / original Unit2 key points',[section('2.6','2.5 MOTION DUE TO GRAVITY:','2.5 کشش ثقل سے حرکت:','2.5 د جاذبې له امله حرکت:',p,[v,c,unrounded,ans],[para(0),visual(v),para(1),visual(c),para(2),visual(unrounded),para(3),visual(ans),para(4),para(5,'heading'),para(6),dict(type='parallelPhrases',columns=[[7],[8]])]),section('source-u2-key-points','KEY POINTS','اہم نکات','مهم ټکي',q,[eq],layout)],'Fresh visible source inspection. Restored bridge final-velocity calculation31.36ms⁻¹ and printed31ms⁻¹ rounding; Assignment2.7 original cricket-ball question/subparts retained without answers. All original Unit2 key points preserved as distinct paired records with three motion types in columns and coded three-equation row. Corrected source definitions/grammar retained and aligned to translations. Added source formula links to synchronize existing summary/formula cards from reviewed native equations.',numericals=[num],activities=[dict(num='Assignment 2.7',name='CRICKET BALL',procedure=' '.join(q['text'] for q in p[6:9]),urdu=' '.join(q['urdu'] for q in p[6:9]),pashto=' '.join(q['pashto'] for q in p[6:9]),sourcePdfPage=60,sourcePrintedPage=55)],formulaSourceLinks=links)
