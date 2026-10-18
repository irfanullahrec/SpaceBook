from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u03',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u03'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
# scan 31 = printed 27
s=page(31,'u03','27','Social life; anti-narcotics awareness campaign','معاشرتی زندگی؛ منشیات کے خلاف آگاہی مہم','ټولنیز ژوند؛ د نشه‌یي توکو پر ضد د پوهاوي کمپاین','drugs-1')
F=Flow(s)
P(s,[('معاشرتی زندگی: بچوں کو معاشرتی سرگرمیوں میں شامل رکھا جائے۔ انہیں مختلف کام سکھائے جائیں۔ بچے مل جل کر کام کرنے میں خوشی محسوس کرتے ہیں۔ شادی بیاہ، غم وغیرہ مختلف تقاریب میں انھیں مختلف کام تفویض کیے جائیں تو بچوں میں خود اعتمادی بڑھتی ہے۔ ان میں احساسِ ذمہ داری پیدا ہوتی ہے اور لگن سے کام کرتے ہیں۔ غلطی کی صورت میں بے عزتی اور ڈانٹ ڈپٹ سے اجتناب کیا جائے تاکہ بچے کی عزتِ نفس مجروح نہ ہو اور وہ منفی سرگرمیوں کی طرف راغب نہ ہو۔','Social life: children should be kept involved in social activities. They should be taught various tasks. Children feel happy working together. If they are assigned various tasks at weddings, bereavements and other occasions, self-confidence grows in children. A sense of responsibility arises in them and they work with devotion. In case of a mistake, humiliation and scolding should be avoided so that the child’s self-respect is not hurt and he is not drawn towards negative activities.','ټولنیز ژوند: ماشومان په ټولنیزو فعالیتونو کې ښکېل ساتل شي. هغوی ته بېلابېل کارونه ورزده کړل شي. ماشومان په ګډه کار کولو کې خوښي احساسوي. په واده، غم او نورو بېلابېلو غونډو کې که هغوی ته بېلابېل کارونه وسپارل شي نو په ماشومانو کې ځان باور زیاتېږي. په هغوی کې د مسؤولیت احساس پیدا کېږي او په لیوالتیا کار کوي. په غلطۍ کې بې‌عزتي او غندنې ډډه وشي ترڅو د ماشوم عزت نفس ټپي نه شي او هغه منفي فعالیتونو لوري ته مایل نه شي.',dict(listGroup='ap')),
('منشیات کے خلاف آگاہی مہم: سکول میں کم از کم مہینے میں ایک دن منشیات کے خلاف آگاہی مہم کے طور پر منانی چاہیے اور اس دن کسی ڈاکٹر کو بلا کر منشیات خصوصاً شراب نوشی کے مضر اثرات پر بحث کرنی چاہیے۔','Awareness campaign against narcotics: in school at least one day a month should be observed as an awareness campaign against narcotics, and on that day a doctor should be called to discuss the harmful effects of narcotics, especially alcohol drinking.','د نشه‌یي توکو پر ضد د پوهاوي کمپاین: په ښوونځي کې لږ تر لږه په میاشت کې یوه ورځ د نشه‌یي توکو پر ضد د پوهاوي کمپاین په توګه ولمانځل شي او په هغه ورځ کوم ډاکټر راوغوښتل شي او د نشه‌یي توکو په ځانګړې توګه د شرابو څکلو د زیان‌رسوونکو اغېزو په اړه بحث وشي.',dict(listGroup='ap',sourceGap=dict(note='A collage poster (a ribbon with “STAY DRUG FREE — JUST SAY NO TO DRUGS”, syringes, pills and a cannabis leaf) is redrawn only as a text ribbon.')))])
F.fg(0)
F.done()
fig=svg(360,200,'Awareness ribbon with the text STAY DRUG FREE and JUST SAY NO TO DRUGS',
 '<path d="M180 40 C120 40 110 100 160 130 L120 190 L160 190 L190 140 L220 190 L260 190 L210 120 C250 90 240 40 180 40 Z" fill="#e53935" stroke="#7f0000" stroke-width="3"/>'+T(180,78,'STAY DRUG FREE',13,'middle',700,'#fff')+T(180,150,'JUST SAY NO TO DRUGS',11,'middle',700,'#111'))
s['figures']=[dict(id='hpe11-s031-fig1',svg=fig,caption='Awareness ribbon: STAY DRUG FREE — JUST SAY NO TO DRUGS',captionUrdu='آگاہی ربن: منشیات سے پاک رہیں — منشیات کو نہ کہیں',captionPashto='د پوهاوي ربن: له نشه‌یي توکو پاک اوسئ — نشه‌یي توکو ته نه ووایئ',labels=[lab('STAY DRUG FREE','منشیات سے پاک رہیں','له نشه‌یي توکو پاک اوسئ'),lab('JUST SAY NO TO DRUGS','منشیات کو نہ کہیں','نشه‌یي توکو ته نه ووایئ')],sourceGap=dict(note='Simplified coded redrawing of the poster ribbon; the original also shows drug paraphernalia in a collage.'))]
s['sourceNote']='Printed page 27: social life and the anti-narcotics awareness campaign, with the poster picture; the English slogan is printed on the ribbon.'+NOTE
s['vocabulary']={}
save(s)
# scan 32 = printed 28
s=page(32,'u03','28','Exercise questions: Chapter 3','مشقی سوالات: باب 3','تمرین پوښتنې: دریم څپرکی','ex3')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جوابات منتخب کر کے لکھیں۔','1. Select the suitable answers and write them.','۱. مناسب ځوابونه وټاکئ او ولیکئ.')
Q(s,'i۔ اسلام میں ہر قسم کا نشہ ________ ہے۔','i. In Islam every kind of intoxicant is ________.','i. په اسلام کې هر ډول نشه ________ ده.')
for t in [('(الف) حلال','(a) lawful','(الف) حلال'),('(ب) حرام','(b) forbidden','(ب) حرام'),('(ج) جائز','(c) permissible','(ج) جایز'),('(د) نقصان دہ','(d) harmful','(د) زیان‌رسوونکی')]: O(s,*t)
Q(s,'ii۔ بچوں کو معاشرتی سرگرمیوں میں شامل کرنے سے ان میں ________ پیدا ہوتی ہے۔','ii. By involving children in social activities, ________ arises in them.','ii. ماشومان په ټولنیزو فعالیتونو کې ښکېلولو سره په هغوی کې ________ پیدا کېږي.')
for t in [('(الف) لالچ','(a) greed','(الف) لالچ'),('(ب) خود اعتمادی','(b) self-confidence','(ب) ځان باور'),('(ج) تھکاوٹ','(c) fatigue','(ج) ستړیا'),('(د) منفی سوچ','(d) negative thinking','(د) منفي فکر')]: O(s,*t)
Q(s,'iii۔ شراب ________ ہائیڈروجن اور آکسیجن کا مرکب ہے۔','iii. Alcohol is a compound of ________, hydrogen and oxygen.','iii. شراب ________، هایډروجن او اکسیجن مرکب دی.')
for t in [('(الف) نائیٹروجن','(a) nitrogen','(الف) نایتروجن'),('(ب) کاربن','(b) carbon','(ب) کاربن'),('(ج) آکسیجن','(c) oxygen','(ج) اکسیجن'),('(د) امونیا','(d) ammonia','(د) امونیا')]: O(s,*t)
Q(s,'iv۔ شراب سے ________ کی حرکت تیز ہو جاتی ہے۔','iv. By alcohol the movement of the ________ becomes faster.','iv. په شرابو سره د ________ حرکت ګړندی کېږي.')
for t in [('(الف) پھیپھڑوں','(a) lungs','(الف) سږو'),('(ب) خون','(b) blood','(ب) وینې'),('(ج) دل','(c) heart','(ج) زړه'),('(د) دماغ','(d) brain','(د) دماغو')]: O(s,*t)
Q(s,'v۔ شراب کے عادی افراد کے بچوں میں ________ کا مرض عموماً پایا جاتا ہے۔','v. In the children of habitual drinkers the disease of ________ is generally found.','v. د شرابو د عادي کسانو په ماشومانو کې د ________ ناروغي عموماً موندل کېږي.')
for t in [('(الف) ذہنی دباؤ','(a) mental stress','(الف) ذهني فشار'),('(ب) لنگڑاپن','(b) lameness','(ب) ګوډوالی'),('(ج) مرگی','(c) epilepsy','(ج) مرغۍ'),('(د) بینائی','(d) eyesight','(د) لیدل')]: O(s,*t)
H(s,'2۔ درج ذیل سوالات کے مختصر جواب لکھیں۔','2. Write short answers to the following questions.','۲. د لاندې پوښتنو لنډ ځوابونه ولیکئ.')
Q(s,'i۔ شراب نوشی کی طرف راغب کرنے والے عوامل بیان کریں۔','i. State the factors that incline people towards alcohol drinking.','i. هغه عوامل بیان کړئ چې شرابو څکلو لوري ته راکاږي.')
Q(s,'ii۔ شراب نوشی سے کس طرح نجات حاصل کی جا سکتی ہے؟','ii. How can deliverance from alcohol drinking be achieved?','ii. له شرابو څکلو نجات څنګه ترلاسه کېدای شي؟')
Q(s,'iii۔ شراب نوشی کس طرح صحت و کردار پر اثر انداز ہوتی ہے؟','iii. How does alcohol drinking affect health and character?','iii. شراب څکل په روغتیا او کردار څنګه اغېز کوي؟')
F.done()
s['sourceNote']='Printed page 28: exercise questions of Chapter 3 — five multiple-choice items (options الف–د) and three short-answer questions.'+NOTE
s['vocabulary']={}
save(s)
# scan 33 = printed 29
s=page(33,'u04','29','Chapter 4: Emergency Situations — opener','باب نمبر 4: ہنگامی صورتِ حال — آغاز','څلورم څپرکی: بېړني حالتونه — پیل','ch4-open')
F=Flow(s)
add(s,'bn','Chapter 4','باب نمبر 4','څلورم څپرکی')
H(s,'ہنگامی صورتِ حال','Emergency Situations','بېړني حالتونه')
P(s,[('اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After studying this chapter the students will be able to:','د دې څپرکي له لوستلو وروسته به زده‌کوونکي دې وړ شي چې هغوی:'),
('ہنگامی صورتِ حال کی نشاندہی کر سکیں۔','identify an emergency situation.','بېړني حالت وپېژني.',dict(listGroup='o4')),
('بم دھماکے کی صورت میں عام لوگوں کے لیے حفاظتی اقدامات کی نشاندہی کر سکیں۔','identify protective measures for ordinary people in case of a bomb blast.','د بم چاودنې په صورت کې د عامو خلکو لپاره ساتنیز اقدامات وښیي.',dict(listGroup='o4')),
('بم دھماکے کے بعد حفاظتی اقدامات کر سکیں۔','take protective measures after a bomb blast.','د بم چاودنې وروسته ساتنیز اقدامات وکړي.',dict(listGroup='o4')),
('کسی ہنگامی صورتِ حال میں ابتدائی طبی امداد کی مہارتوں کا مظاہرہ کر سکیں۔','demonstrate the skills of first aid in an emergency situation.','په کوم بېړني حالت کې د لومړنۍ طبي مرستې د مهارتونو ښودنه وکړي.',dict(listGroup='o4')),
('سکولوں میں غنڈہ گردی کو کم یا ختم کرنے کے لیے اصول وضع کر سکیں اور سماجی معیار بتا سکیں۔','frame principles for reducing or ending bullying in schools and state social standards.','په ښوونځیو کې د غونډه‌ګرۍ (بلینګ) کمولو یا ختمولو لپاره اصول جوړ کړي او ټولنیز معیارونه وښيي.',dict(listGroup='o4',sourceGap=dict(note='A photograph of a wrecked bus at the scene of a blast is not reproduced.')))])
F.done()
s['sourceNote']='Printed page 29: Chapter 4 opener with five learning outcomes. The chapter number “4” in the heading band is faint in the scan.'+NOTE
s['vocabulary']={}
save(s)
# scan 34 = printed 30
s=page(34,'u04','30','Emergency situations; bomb blast: measures (i–iii)','ہنگامی صورتِ حال؛ بم دھماکہ: اقدامات (i–iii)','بېړني حالتونه؛ د بم چاودنه: اقدامات (i–iii)','emergency-1')
F=Flow(s)
H(s,'ہنگامی صورتِ حال','Emergency Situations','بېړني حالتونه')
P(s,[('ایسے حالات جو اچانک اور غیر یقینی طور پر پیدا ہوں جو لوگوں کے جانی و مالی نقصان کا باعث بنے اور جن پر قابو پانے کے لیے فوری اقدامات کی ضرورت ہو، ہنگامی حالات کہتے ہیں۔ مثلاً آگ کا لگنا، سیلاب آنا، بم دھماکہ، زلزلہ وغیرہ۔','Situations which arise suddenly and unexpectedly, which cause loss of life and property of people and for controlling which immediate measures are needed, are called emergency situations. For example the outbreak of fire, coming of flood, bomb blast, earthquake, etc.','داسې حالات چې ناڅاپي او غیر یقیني ډول پیدا شي چې د خلکو د ځان او مال د زیان لامل شي او د هغو په کنټرول کې سمدستي اقدامات ته اړتیا وي، بېړني حالات بلل کېږي. لکه د اور لګېدل، سېلاب راتګ، د بم چاودنه، زلزله او نور.'),
('بم دھماکہ (Bomb Blast): 11 ستمبر 2001 کو امریکہ میں ورلڈ ٹریڈ سینٹر پر حملے کے بعد انسانی تاریخ میں تبدیلی رونما ہوئی۔ امریکہ کے افغانستان پر حملے اور دہشت گردی کے خلاف جنگ نے پاکستان کو بہت متاثر کیا۔ بم دھماکے اور خود کش حملے آئے دن کا معمول بن گئے لہٰذا بم دھماکے کی صورت میں عوام الناس کے لیے حفاظتی تدابیر کے بارے میں آگاہی بہت ضروری ہے۔','Bomb blast (Bomb Blast): after the attack on the World Trade Center in America on 11 September 2001 a change took place in human history. America’s attack on Afghanistan and the war against terrorism affected Pakistan greatly. Bomb blasts and suicide attacks have become the routine of every day; therefore in case of a bomb blast awareness among the general public about protective measures is very necessary.','د بم چاودنه (Bomb Blast): د ۲۰۰۱ کال د سپتمبر په ۱۱ په امریکا کې د نړیوال سوداګرۍ مرکز پر برید وروسته په انساني تاریخ کې بدلون راغی. د امریکا پر افغانستان برید او د ترهګرۍ پر ضد جګړې پاکستان ډېر اغېزمن کړ. د بم چاودنې او ځانمرګي بریدونه ورځنی معمول شو نو د بم چاودنې په صورت کې د عامو خلکو لپاره د ساتنیزو تدبیرونو په اړه پوهاوی ډېر اړین دی.',GAP('A photograph of the World Trade Center attack is not reproduced.'))])
H(s,'بم دھماکے کی صورت میں مندرجہ ذیل نکات پر عمل کرنا چاہیے:','In the Case of a Bomb Blast the Following Points Should Be Acted Upon:','د بم چاودنې په صورت کې په لاندې ټکو عمل کول پکار دي:')
P(s,[('i۔ پُر سکون رہنے کی کوشش کریں اور اپنی مدد آپ کریں۔','i. Try to stay calm and help yourself.','i. ارامه پاتې کېدو هڅه وکړئ او خپله مرسته وکړئ.',dict(listGroup='bb')),
('ii۔ اگر ارد گرد چیزیں گرنا شروع ہو جائیں تو کسی محفوظ جگہ جلد از جلد پہنچنے کی کوشش کریں۔ عمارت کے اندر میز یا ڈیسک کے نیچے گھس جائیں۔','ii. If things begin to fall around you, try to reach a safe place as quickly as possible. Inside a building get under a table or desk.','ii. که شاوخوا شیان لوېدو ته پیل وکړي نو په کوم خوندي ځای ژر تر ژره رسېدو هڅه وکړئ. د ودانۍ دننه د میز یا ډیسک لاندې ننوځئ.',dict(listGroup='bb')),
('iii۔ شیشے کی بنی اشیاء مثلاً آئینہ، کھڑکی اور کیبنٹ سے دور رہیں تاکہ وہ ٹوٹ کر آپ کو زخمی نہ کرے۔','iii. Stay away from things made of glass such as mirrors, windows and cabinets so that they do not break and injure you.','iii. د شیشې له جوړو شویو شیانو لکه ایینې، کړکۍ او کېبینټ نه لرې اوسئ ترڅو دا ماتېدو سره تاسو ټپي نه کړي.',dict(listGroup='bb'))])
F.done()
s['sourceNote']='Printed page 30: definition of emergency situations, bomb blast background, and measures i–iii during a blast.'+NOTE
s['vocabulary']={}
save(s)
# scan 35 = printed 31
s=page(35,'u04','31','Bomb blast measures (iv–x); precautions under rubble (start)','بم دھماکہ: اقدامات (iv–x)؛ ملبے کے نیچے احتیاطی تدابیر','د بم چاودنه: اقدامات (iv–x)؛ د ملبې لاندې احتیاطي تدبیرونه','emergency-2')
F=Flow(s)
P(s,[('iv۔ پولیس یا ریسکیو (Rescue) کی جانب سے دی گئی ہدایات پر عمل کریں اگر عمارت کو خالی کرنے کی ہدایت دی ہوں تو فوری عمل کریں۔','iv. Act on the instructions given by the police or rescue (Rescue); if instructions have been given to vacate the building, act immediately.','iv. د پولیسو یا ریسکیو (Rescue) له لوري ورکړل شویو لارښوونو عمل وکړئ که د ودانۍ د تشولو لارښوونه ورکړل شوې وي نو سمدستي عمل وکړئ.',dict(listGroup='bb')),
('v۔ زخمی اور معذور افراد کا خیال رکھیں اور انھیں بھی عمارت سے باہر لے جانے میں مدد کریں۔','v. Take care of injured and disabled persons and help in taking them out of the building too.','v. ټپیان او معذور کسان وساتئ او هغوی هم له ودانۍ بهر وړلو کې مرسته وکړئ.',dict(listGroup='bb')),
('vi۔ زیادہ زخمی افراد کو اس وقت تک جگہ سے نہ ہلائیں جب تک کوئی فوری خطرہ مثلاً عمارت کے انہدام یا آگ لگنے کا خطرہ نہ ہو۔','vi. Do not move seriously injured persons from the place unless there is an immediate danger, for example of the building collapsing or catching fire.','vi. ډېر ټپیان له ځایه مه خوځوئ تر هغه چې کومه سمدستي خطره لکه د ودانۍ د ړنګېدو یا د اور لګېدو خطره نه وي.',dict(listGroup='bb')),
('vii۔ گیس لائن یا باورچی خانے سے دور رہیں کیونکہ گیس کی لیکیج اور آگ لگنے کی خطرات زیادہ ہوتے ہیں۔','vii. Stay away from the gas line or kitchen, because the risks of gas leakage and fire are greater.','vii. له ګاز لاین یا پخلنځي لرې اوسئ ځکه چې د ګاز د لیک او اور لګېدو خطرونه زیات وي.',dict(listGroup='bb')),
('viii۔ لفٹ (Elevator) کا استعمال نہ کریں۔','viii. Do not use the lift (Elevator).','viii. لفټ (Elevator) مه کاروئ.',dict(listGroup='bb')),
('ix۔ سیدھا لیٹ جائیں کیونکہ خود کش حملے کی صورت میں بم میں موجود بال بیرنگ زمین سے اوپر 2 تا 6 فٹ تک کار گر ثابت ہوتے ہیں اور انسانی دھڑ اور سر کو زخمی کر سکتے ہیں۔','ix. Lie down flat, because in the case of a suicide attack the ball bearings in the bomb prove effective from 2 to 6 feet above the ground and can injure the human trunk and head.','ix. سیده ویده شئ ځکه چې د ځانمرګي برید په صورت کې په بم کې موجود بال بیرنګ له ځمکې پورته ۲ تر ۶ فوټو پورې اغېزناک ثابتېږي او د انسان تنه او سر ټپي کولای شي.',dict(listGroup='bb')),
('x۔ اپنا منہ کھلا رکھیں اور تھوڑے تھوڑے وقفے کے بعد سانس لیں۔ یاد رکھیں بم دھماکہ کی صورت میں بم میں موجود تیز دھار اشیاء یا حرارت سے اتنا نقصان نہیں ہوتا جتنا کہ ہوا کے زیادہ پریشر سے ہوتا ہے۔ دھماکے کی لہریں بہت تیزی کے ساتھ حرکت میں آتی ہیں اور ہوا سے بھرے انسانی اعضاء مثلاً پھیپھڑے اور گردوں کو متاثر کرتے ہیں۔ خود کش حملے کی صورت میں اموات کی زیادہ وجہ پھیپھڑوں میں اندرونی طور پر خون کا بہنا ہے۔ صرف 6 فی صد افراد حرارت یا بال بیرنگ سے جان بحق ہوتے ہیں۔','x. Keep your mouth open and breathe after short intervals. Remember that in a bomb blast the damage is not so much from sharp objects in the bomb or heat as from the greater pressure of air. Blast waves move with great speed and affect air-filled human organs such as the lungs and kidneys. In a suicide attack the main cause of deaths is internal bleeding in the lungs. Only 6 per cent of people die from heat or ball bearings.','x. خپله خوله خلاصه وساتئ او لږ لږ وقفې وروسته ساه واخلئ. یاد ولرئ د بم چاودنې په صورت کې په بم کې موجود تېره څنډه لرونکي شیانو یا تودوخې سره دومره زیان نه کېږي څومره چې د هوا له ډېر فشار سره کېږي. د چاودنې څپې ډېر تېزۍ سره حرکت ته راځي او له هوا ډک انساني غړي لکه سږي او پښتورګي اغېزمنوي. د ځانمرګي برید په صورت کې د مړینو ډېر لامل په سږو کې داخلي ډول د وینې بهېدل دي. یوازې ۶ سلنه کسان له تودوخې یا بال بیرنګ نه ځان بایلي.',dict(listGroup='bb'))])
H(s,'ملبے کے نیچے احتیاطی تدابیر:','Precautionary Measures Under Rubble:','د ملبې لاندې احتیاطي تدبیرونه:')
P(s,[('i۔ اپنا منہ رومال یا کسی کپڑے سے ڈھانپ لیں۔','i. Cover your mouth with a handkerchief or some cloth.','i. خپله خوله دسمال یا کوم ټوکر سره پټه کړئ.',dict(listGroup='rb')),
('ii۔ کسی پائپ یا دیوار کے ساتھ دستک کے انداز میں ہاتھ ماریں تاکہ ریسکیو ٹیم آپ کی موجودگی کے بارے میں آگاہ ہو۔','ii. Strike with your hand in a knocking manner on some pipe or wall so that the rescue team may know of your presence.','ii. په کوم پایپ یا دېوال کې د ټکور په انداز لاس ووهئ ترڅو ریسکیو ټیم ستاسو د شتون په اړه خبر شي.',dict(listGroup='rb')),
('iii۔ چیخنے چلانے سے گریز کریں اس طرح کرنے سے گرد و غبار آپ کے پھیپھڑوں میں جا کر دم گھٹنے کا سبب بن سکتا ہے۔','iii. Avoid screaming and shouting; by doing so dust may enter your lungs and become a cause of suffocation.','iii. چیغو وهلو ډډه وکړئ داسې کولو سره دوړې ستاسو سږو ته تللو سره د ساه ټنګېدو لامل کېدای شي.',dict(listGroup='rb',sourceGap=dict(note='The list continues on the next page (printed page 32).')))])
F.done()
s['sourceNote']='Printed page 31: bomb-blast measures iv–x and the heading with the first three precautions under rubble.'+NOTE
s['vocabulary']={}
save(s)
