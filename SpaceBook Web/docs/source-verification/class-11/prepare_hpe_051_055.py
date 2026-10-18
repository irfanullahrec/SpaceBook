from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u05',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u05'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
def L(items,g):
    return [(a,b,c,dict(listGroup=g)) for a,b,c in items]
# scan 51 = printed 49
s=page(51,'u05','49','Gymnastics: exercises of body parts; group exercises','جمناسٹک: جسم کے مختلف حصوں کی ورزشیں؛ گروہی ورزشیں','جمناسټیک: د بدن د بېلابېلو برخو تمرینونه؛ ډله‌ییز تمرینونه','gym-3')
F=Flow(s)
H(s,'3۔ جسم کے مختلف حصوں کی ورزشیں اور سرگرمیاں:','3. Exercises and Activities of Various Parts of the Body:','۳. د بدن د بېلابېلو برخو تمرینونه او فعالیتونه:')
H(s,'ورزشیں (Exercises)','Exercises','تمرینونه (Exercises)')
P(s,[('جسم کے مختلف جوڑوں کی ورزشیں: اچھلنا، کودنا، اچھل کر پاؤں سامنے لانا، رسی کودنا، گیند کودنا۔','Exercises of the various joints of the body: bouncing, jumping, bouncing and bringing the feet forward, skipping rope, jumping the ball.','د بدن د بېلابېلو جوړو تمرینونه: پورته ټوپ، ټوپ وهل، ټوپ وهلو سره پښې مخې ته راوړل، رسۍ ټوپ، توپ ټوپ.',dict(listGroup='bp')),
('ٹانگوں کی ورزشیں: گھٹنوں کے بل جھکنا، اٹھنا، اکڑوں بیٹھ کر آگے پیچھے کودنا۔ پنجوں پر کھڑے ہونا۔','Exercises of the legs: bending on the knees, rising, sitting in a squatting position and jumping forward and backward. Standing on the toes.','د پښو تمرینونه: په زنګنونو کږېدل، پاڅېدل، په ګونډو ناست کېدو سره مخکې شاته ټوپ وهل. په ګوتو ولاړ کېدل.',dict(listGroup='bp')),
('دھڑ کے بالائی حصے کی ورزشیں: دھڑ اٹھانا اور گردن کو پیچھے کی طرف دبانا۔ پہلو کو گرانا اور جھکانا، دبانا، موڑنا۔','Exercises of the upper part of the trunk: raising the trunk and pressing the neck backward. Letting the side fall and bending, pressing, twisting.','د تنې د پورتنۍ برخې تمرینونه: تنه پورته کول او غاړه شاته لوري ته ټېل وهل. څنګ غورځول او کږول، ټېل وهل، اړول.',dict(listGroup='bp'))])
H(s,'سرگرمیاں (Activities)','Activities','فعالیتونه (Activities)')
P(s,[('مندرجہ بالا ورزشیں مختلف گیموں اور اتھلیٹکس ایونٹ میں بہتر کارکردگی کا باعث بن سکتے ہیں۔ مثلاً گولہ پھینکنا، ڈسکس تھرو اور نیزہ وغیرہ۔','The above exercises can become a cause of better performance in various games and athletic events, for example shot put, discus throw and javelin, etc.','پورتني تمرینونه په بېلابېلو لوبو او اتلیټکس ایونټ کې د ښې کارکردګي لامل کېدای شي. لکه ګولې غورځول، ډیسکس تهرو او نېزه او نور.')])
H(s,'4۔ گروہی ورزشیں اور سرگرمیاں (Group Exercises and Activities)','4. Group Exercises and Activities','۴. ډله‌ییز تمرینونه او فعالیتونه (Group Exercises and Activities)')
P(s,[('گروہی سرگرمیاں اور حرکات انسان میں خود اعتمادی، ہم آہنگی، تیز رفتاری، توانائی اور جرات جیسی خوبیاں پیدا کرتی ہیں۔ گروہی سرگرمیوں کی وجہ سے ٹیم ورک (Team work) اور تعاون جیسے جذبات پیدا ہوتے ہیں۔','Group activities and movements create in man such qualities as self-confidence, coordination, speed, energy and courage. Because of group activities feelings such as team work (Team work) and cooperation arise.','ډله‌ییز فعالیتونه او حرکتونه په انسان کې ځان باور، همغږي، ګړندیتوب، ځواک او زړورتیا غوندې ښېګڼې پیدا کوي. د ډله‌ییزو فعالیتونو له امله ټیم ورک (Team work) او همکارۍ غوندې احساسات پیدا کېږي.')])
F.done()
s['sourceNote']='Printed page 49: exercises of body parts (joints, legs, upper trunk) and activities; the heading and text of group exercises. The lower half of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 52 = printed 50
s=page(52,'u05','50','Athletics: track events; kinds of start (bunch, medium)','اتھلیٹکس: دوڑ کے مقابلے؛ آغاز کے طریقے (بلٹ، میڈیم)','اتلیټکس: د منډې سیالۍ؛ د پیل طریقې (بلټ، منځنی)','athletics-1')
F=Flow(s)
H(s,'اتھلیٹکس (Athletics)','Athletics','اتلیټکس (Athletics)')
H(s,'دوڑ کے مقابلے (Track Events)','Track Events','د منډې سیالۍ (Track Events)')
P(s,[('ٹریک ایونٹس میں ذاتی کارکردگی اور مہارتوں کو بڑھانے کے لیے بائیو مکینیکل اصولوں کے مطابق جسمانی حرکات پر کنٹرول کا مظاہرہ ہوتا ہے۔','In track events, for increasing personal performance and skills, control over physical movements according to biomechanical principles is demonstrated.','په ټریک ایونټونو کې د شخصي کارکردګۍ او مهارتونو زیاتولو لپاره د بایومیکانیکي اصولو سره سم پر بدني حرکتونو د کنټرول ښودنه کېږي.')])
H(s,'دوڑ کا آغاز (Start)','Start of the Race (Start)','د منډې پیل (Start)')
P(s,[('تیز دوڑ میں اتھلیٹ مندرجہ ذیل تین طریقوں سے سٹارٹ لے سکتے ہیں۔','In a sprint the athlete can take a start by the following three methods.','په ګړندۍ منډه کې اتلیټ په لاندې دریو طریقو پیل ترلاسه کولای شي.')]+L([('1۔ بلٹ سٹارٹ (Bunch or Bullet start)','1. Bullet start (Bunch or Bullet start)','۱. بلټ سټارټ (Bunch or Bullet start)'),('2۔ میڈیم سٹارٹ (Medium start)','2. Medium start (Medium start)','۲. منځنی سټارټ (Medium start)'),('3۔ الانگیٹیڈ سٹارٹ (Elongated start)','3. Elongated start (Elongated start)','۳. اوږد سټارټ (Elongated start)')],'st'))
H(s,'1۔ بلٹ سٹارٹ (Bunch or Bullet start)','1. Bullet Start (Bunch or Bullet start)','۱. بلټ سټارټ (Bunch or Bullet start)')
P(s,[('یہ سٹارٹ عام طور پر چھوٹے قد کے کھلاڑی لیتے ہیں۔ اس سٹارٹ میں اگلا پاؤں سٹارٹنگ لائن سے پیچھے ہوتا ہے اور پچھلے پاؤں کا گھٹنا اگلے پاؤں کے پنجے کے برابر رکھا جاتا ہے۔','This start is generally taken by short-statured players. In this start the front foot is behind the starting line and the knee of the back foot is kept level with the toe of the front foot.','دا پیل عموماً کوچنی قد لرونکي لوبغاړي اخلي. پدې پیل کې مخکینۍ پښه د پیل له کرښې شاته وي او د شاتنۍ پښې زنګنه د مخکینۍ پښې د ګوتو برابره ساتل کېږي.')])
H(s,'2۔ میڈیم سٹارٹ (Medium start)','2. Medium Start (Medium start)','۲. منځنی سټارټ (Medium start)')
P(s,[('یہ سٹارٹ عموماً در میانے قد کے کھلاڑی لیتے ہیں۔ اس سٹارٹ میں اگلا پاؤں سٹارٹنگ لائن سے پیچھے ہوتا ہے اور پچھلی ٹانگ کا گھٹنا اگلے پاؤں کے محراب کے برابر رکھا جاتا ہے۔','This start is generally taken by medium-statured players. In this start the front foot is behind the starting line and the knee of the back leg is kept level with the arch of the front foot.','دا پیل عموماً منځني قد لرونکي لوبغاړي اخلي. پدې پیل کې مخکینۍ پښه د پیل له کرښې شاته وي او د شاتنۍ پښې زنګنه د مخکینۍ پښې د محراب برابره ساتل کېږي.')])
F.done()
s['sourceNote']='Printed page 50: athletics — track events, three kinds of start (list), and the first two explained (bunch/bullet, medium).'+NOTE
s['vocabulary']={}
save(s)
# scan 53 = printed 51 (photo)
s=page(53,'u05','51','Elongated start; stages of a sprint (1–3)','الانگیٹیڈ سٹارٹ؛ تیز دوڑ کے مراحل (1–3)','اوږد سټارټ؛ د ګړندۍ منډې پړاوونه (۱–۳)','athletics-2')
F=Flow(s)
H(s,'3۔ الانگیٹیڈ سٹارٹ (Elongated start)','3. Elongated Start (Elongated start)','۳. اوږد سټارټ (Elongated start)')
P(s,[('یہ سٹارٹ عام طور پر لمبے قد کے اتھلیٹ لیتے ہیں۔ اس سٹارٹ میں اگلا پاؤں سٹارٹنگ پاؤں سے پیچھے ہوتا ہے اور پچھلے پاؤں کا گھٹنا اگلے پاؤں کے ایڑی کے برابر رکھا جاتا ہے۔','This start is generally taken by tall athletes. In this start the front foot is behind the starting foot and the knee of the back foot is kept level with the heel of the front foot.','دا پیل عموماً اوږد قد لرونکي اتلیټان اخلي. پدې پیل کې مخکینۍ پښه د پیل له پښې شاته وي او د شاتنۍ پښې زنګنه د مخکینۍ پښې د پوندې برابره ساتل کېږي.',GAP('The scan reads “سٹارٹنگ پاؤں سے” where “سٹارٹنگ لائن سے” (starting line) is probably meant; kept as printed.')),
('تیز دوڑ میں اتھلیٹ آغاز سے اختتام تک مندرجہ ذیل مراحل طے کرتا ہے۔','In a sprint the athlete goes through the following stages from beginning to end.','په ګړندۍ منډه کې اتلیټ له پیل نه تر پایه لاندې پړاوونه تېروي.')]+L([('1۔ آن یور مارکس (On your marks)','1. On your marks (On your marks)','۱. آن یور مارکس (On your marks)'),('2۔ سیٹ (Sit)','2. Sit (“Sit” as printed; the usual command is “Set”)','۲. سیټ (Sit)'),('3۔ فائر (Fire)','3. Fire (Fire)','۳. فایر (Fire)'),('4۔ ڈرائیو آف (Drive off)','4. Drive off (Drive off)','۴. ډرایو آف (Drive off)'),('5۔ بتدریج تیز ہونا (Acceleration)','5. Gradually speeding up (Acceleration)','۵. په تدریج ګړندی کېدل (Acceleration)'),('6۔ اختتام (Finish)','6. Finish (Finish)','۶. پای (Finish)')],'sg'))
H(s,'1۔ آن یور مارکس (On your marks)','1. On Your Marks (On your marks)','۱. آن یور مارکس (On your marks)')
P(s,[('اتھلیٹ دوڑ شروع ہونے سے پہلے اسمبلی لائن پر کھڑے ہوتے ہیں۔ سٹارٹر کی پکار پر “آن یور مارکس” پر اتھلیٹ سٹارٹنگ لائن پر آ کر دوڑ کے لیے پوزیشن لیتے ہیں۔','Before the race begins the athletes stand on the assembly line. At the starter’s call “On your marks” the athletes come to the starting line and take position for the race.','اتلیټان د منډې له پیل نه مخکې په اسمبلۍ کرښه ودرېږي. د سټارټر په غږ “آن یور مارکس” په اتلیټان د پیل کرښې ته راتلو سره د منډې لپاره موقعیت اخلي.',GAP('A photograph of sprinters in the starting blocks is not reproduced.'))])
H(s,'2۔ سیٹ (Sit)','2. Set (Sit)','۲. سیټ (Sit)')
P(s,[('آن یور مارکس کے بعد سٹارٹر سیٹ پکارتا ہے جس پر اتھلیٹ زمین سے لگا اپنا گھٹنا اٹھا لیتا ہے۔','After “On your marks” the starter calls “Set” (Sit as printed), on which the athlete lifts his knee which was touching the ground.','له آن یور مارکس وروسته سټارټر سیټ غږ کوي چې پر هغه اتلیټ له ځمکې سره نښتې خپله زنګنه پورته کوي.')])
H(s,'3۔ فائر (Fire)','3. Fire (Fire)','۳. فایر (Fire)')
P(s,[('سیٹ کے تقریباً ایک دو سیکنڈ بعد پستول سے فائر کیا جاتا ہے۔','About one or two seconds after “Set” a shot is fired from the pistol.','د سیټ نه نږدې یو دوه ثانیې وروسته په پستول فایر کېږي.')])
F.done()
s['sourceNote']='Printed page 51: the elongated start, the six stages of a sprint, and the first three stages explained; a starting-block photograph is left out. The scan prints the call as “سیٹ (Sit)”.'+NOTE
s['vocabulary']={}
save(s)
# scan 54 = printed 52 (photo)
s=page(54,'u05','52','Sprint stages 4–6 (drive off, acceleration, finish)','تیز دوڑ کے مراحل 4–6','د ګړندۍ منډې پړاوونه ۴–۶','athletics-3')
F=Flow(s)
H(s,'4۔ ڈرائیو آف (Drive off)','4. Drive Off (Drive off)','۴. ډرایو آف (Drive off)')
P(s,[('فائر کے ساتھ ہی اتھلیٹ دوڑ کا آغاز کرتے ہیں۔','With the fire the athletes begin the race.','د فایر سره سم اتلیټان د منډې پیل کوي.')])
H(s,'5۔ بتدریج تیز ہونا (Acceleration)','5. Gradually Speeding Up (Acceleration)','۵. په تدریج ګړندی کېدل (Acceleration)')
P(s,[('اتھلیٹ کا اپنی رفتار میں بتدریج اضافہ کرتے ہوئے آگے بڑھنا۔','The athlete moving forward while gradually increasing his speed.','اتلیټ خپل ګړندیتوب کې په تدریج زیاتوالي سره مخکې تلل.')])
H(s,'6۔ اختتام (Finish)','6. Finish (Finish)','۶. پای (Finish)')
P(s,[('جس اتھلیٹ کا دھڑ سوا اختتامی لکیر کو پہلے عبور کرے، وہ فاتح ہوگا۔','The athlete whose trunk crosses the finishing line first will be the winner.','هغه اتلیټ چې تنه یې د پای کرښه لومړی تېره کړي، هغه به ګټونکی وي.',GAP('The scan reads “دھڑ سوا اختتامی لکیر” (apparently “دھڑ اختتامی لکیر”); the word “سوا” seems a printing slip and is not translated. A photograph of the finish of an Olympic race is not reproduced.'))])
F.done()
s['sourceNote']='Printed page 52: sprint stages 4–6 and a finish-line photograph (omitted). The page number “52” sits near the right edge of the footer strip; the lower part of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 55 = printed 53
s=page(55,'u05','53','Exercise questions: Chapter 5','مشقی سوالات: باب 5','تمرین پوښتنې: پنځم څپرکی','ex5')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جواب منتخب کر کے لکھیں۔','1. Select the suitable answer and write it.','۱. مناسب ځواب وټاکئ او ولیکئ.')
Q(s,'i۔ بیڈ منٹن کی مہارتوں میں سب سے مشکل ________ کی مہارت ہے۔','i. Among the skills of badminton the most difficult is the skill of ________.','i. د بیډمنټن په مهارتونو کې تر ټولو ستونزمنه د ________ مهارت دی.')
for t in [('ا۔ سمیش','a. smash','ا. سمېش'),('ب۔ سروس','b. service','ب. سروس'),('ج۔ الٹے ہاتھ کی ریکٹ سے ضرب','c. a stroke with the racket in the back hand','ج. په کیڼ لاس د ریکټ ګوزار'),('د۔ سیدھے ہاتھ کی ریکٹ سے ضرب','d. a stroke with the racket in the right hand','د. په ښي لاس د ریکټ ګوزار')]: O(s,*t)
Q(s,'ii۔ والی بال میں پاس بنانے والے کو ________ کہتے ہیں۔','ii. In volleyball the one who makes the pass is called the ________.','ii. په والیبال کې پاس جوړوونکي ته ________ وايي.')
for t in [('ا۔ سمیشر','a. smasher','ا. سمېشر'),('ب۔ بوسٹر','b. booster','ب. بوسټر'),('ج۔ سروس مین','c. service man','ج. سروس مین'),('د۔ سنٹر مین','d. centre man','د. سنټر مین')]: O(s,*t)
Q(s,'iii۔ والی بال میں سمیشنگ کے دوران ________ برقرار رکھا جائے۔','iii. In volleyball during smashing ________ should be maintained.','iii. په والیبال کې د سمېشنګ په موده کې ________ وساتل شي.')
for t in [('ا۔ توازن','a. balance','ا. توازن'),('ب۔ جذبات','b. feelings','ب. احساسات'),('ج۔ حوصلہ','c. courage','ج. حوصله'),('د۔ حرکت','d. movement','د. حرکت')]: O(s,*t)
Q(s,'iv۔ جمناسٹک میں ________ قائم رکھنا بہت ضروری ہے۔','iv. In gymnastics it is very necessary to maintain ________.','iv. په جمناسټیک کې ________ ساتل ډېر اړین دي.')
for t in [('ا۔ حرکت','a. movement','ا. حرکت'),('ب۔ توازن','b. balance','ب. توازن'),('ج۔ رفتار','c. speed','ج. ګړندیتوب'),('د۔ طاقت','d. strength','د. ځواک')]: O(s,*t)
Q(s,'v۔ تیز دوڑ میں بلٹ سٹارٹ عموماً ________ کے لیے موزوں ہوتا ہے۔','v. In a sprint the bullet start is generally suitable for ________.','v. په ګړندۍ منډه کې بلټ سټارټ عموماً د ________ لپاره مناسب وي.')
for t in [('ا۔ مرد اتھلیٹ','a. male athletes','ا. نارینه اتلیټ'),('ب۔ عورت اتھلیٹ','b. female athletes','ب. ښځینه اتلیټ'),('ج۔ لمبے قد والے اتھلیٹ','c. tall athletes','ج. اوږد قد لرونکي اتلیټان'),('د۔ چھوٹے قد والے اتھلیٹ','d. short-statured athletes','د. کوچني قد لرونکي اتلیټان')]: O(s,*t)
H(s,'2۔ درج ذیل سوالات کے جوابات لکھیں۔','2. Write answers to the following questions.','۲. د لاندې پوښتنو ځوابونه ولیکئ.')
Q(s,'i۔ والی بال کی مہارتوں میں بائیو مکینیکل اصول کس طرح استعمال ہوتے ہیں؟','i. How are biomechanical principles used in the skills of volleyball?','i. د والیبال په مهارتونو کې بایومیکانیکي اصول څنګه کارول کېږي؟')
Q(s,'ii۔ جمناسٹک اور اتھلیٹکس میں بائیو مکینیکل اصولوں کا استعمال لکھیں۔','ii. Write the use of biomechanical principles in gymnastics and athletics.','ii. په جمناسټیک او اتلیټکس کې د بایومیکانیکي اصولو کارول ولیکئ.')
F.done()
s['sourceNote']='Printed page 53: exercise questions of Chapter 5 — five multiple-choice items (options ا–د) and two descriptive questions. The page number “53” is partly cut off at the foot.'+NOTE
s['vocabulary']={}
save(s)
