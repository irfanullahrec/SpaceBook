from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u07',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u07'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
def L(items,g):
    return [(a,b,c,dict(listGroup=g)) for a,b,c in items]
def MC(s,q,opts):
    Q(s,*q)
    for o in opts: O(s,*o)
def hand(x,y,w,rot=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="12" rx="6" fill="#bdbdbd" stroke="#333"/>'
# scan 76 = printed 74 (figure)
s=page(76,'u07','74','Baton exchange: visual and non-visual methods; correct and wrong ways','بیٹن کی تبدیلی: بصری اور غیر بصری طریقہ؛ درست اور غلط طریقے','د بیټن بدلول: لیدنیز او غیر لیدنیز طریقه؛ سمې او غلطې طریقې','relay-5')
F=Flow(s)
H(s,'i۔ بصری طریقہ:','i. Visual Method:','i. لیدنیز طریقه:')
P(s,[('یہ طریقہ 4 × 100 میٹر یا اس سے زیادہ فاصلہ کی ڈاک دوڑ میں استعمال کیا جاتا ہے چونکہ اس دوڑ میں کھلاڑی کی رفتار یکساں نہیں رہتی۔ اس لیے کھلاڑی کے قریب پہنچنے پر اس کا ساتھی اندازہ کرنے کے لیے پیچھے دیکھتے ہوئے دوڑ کا آغاز کرتا ہے اور اسی دوران اپنے ساتھی سے بیٹن وصول کرتا ہے۔','This method is used in a relay race of 4 × 100 metres or a longer distance, because in this race the player’s speed does not remain uniform. Therefore when the player comes near, his fellow player, looking back to judge, begins to run and during this receives the baton from his fellow player.','دا طریقه د ۴ × ۱۰۰ متره یا له هغې زیات واټن په ریلې منډه کې کارول کېږي ځکه چې په دې منډه کې د لوبغاړي ګړندیتوب یو شان نه پاتې کېږي. له همدې امله د لوبغاړي سره نږدې رسېدو په اټکل کولو لپاره د هغه ملګری شاته کتو سره د منډې پیل کوي او په همدې موده کې له خپل ملګري بیټن ترلاسه کوي.')])
H(s,'ii۔ غیر بصری طریقہ:','ii. Non-visual Method:','ii. غیر لیدنیز طریقه:')
P(s,[('یہ طریقہ ایسی دوڑ میں استعمال کیا جاتا ہے جن میں بیٹن دینے والے کی رفتار بہت تیز ہوتی ہے اور وصول کرنے والا کھلاڑی بغیر دیکھے بیٹن تبدیل کرتا ہے۔ بیٹن تبدیلی کا طریقہ چھوٹے فاصلے کی تیز ترین دوڑوں میں استعمال ہوتا ہے۔ بیٹن وصول کرنے والا اپنے ساتھی کے پہنچنے سے پہلے اپنی پوری رفتار سے دوڑ نا شروع کرتا ہے اور بیٹن کی تبدیلی بغیر دیکھے تقریباً پوری رفتار میں مکمل ہوتی ہے۔ یہ طریقہ عام طور سے 4 × 100 اور 4 × 400 میٹر دوڑ کے لیے موزوں تصور کیا جاتا ہے۔','This method is used in races in which the speed of the one giving the baton is very high and the player receiving changes the baton without looking. The method of baton exchange is used in the fastest races of short distances. The one receiving the baton begins to run at his full speed before his fellow player arrives, and the exchange of the baton is completed, without looking, almost at full speed. This method is generally considered suitable for the 4 × 100 and 4 × 400-metre races.','دا طریقه په داسې منډه کې کارول کېږي چې په هغو کې د بیټن ورکوونکي ګړندیتوب ډېر ګړندی وي او ترلاسه کوونکی لوبغاړی پرته له کتو بیټن بدلوي. د بیټن د بدلون طریقه د لنډ واټن په ګړندیو منډو کې کارول کېږي. بیټن ترلاسه کوونکی د خپل ملګري له رسېدو نه مخکې په خپل بشپړ ګړندیتوب منډې پیل کوي او د بیټن بدلون پرته له کتو نژدې په بشپړ ګړندیتوب کې بشپړېږي. دا طریقه عموماً د ۴ × ۱۰۰ او ۴ × ۴۰۰ مترو منډې لپاره مناسبه ګڼل کېږي.')])
F.fg(0)
F.done()
fig=svg(520,250,'Two panels with three numbered hand-and-baton drawings each: on the left a cross mark with the wrong way of exchanging the baton, on the right a tick mark with the correct way; below, three views of a hand gripping the baton',
  '<circle cx="130" cy="30" r="20" fill="#333"/><path d="M122 30 l16 0 M130 22 l0 16" stroke="#fff" stroke-width="3" transform="rotate(45 130 30)"/>'+T(130,76,'Wrong way',12)+
  '<circle cx="390" cy="30" r="20" fill="#333"/><path d="M380 32 l8 8 l14 -16" stroke="#fff" stroke-width="3" fill="none"/>'+T(390,76,'Correct way',12)+
  '<g>'+''.join(f'<rect x="{x}" y="110" width="110" height="14" rx="7" fill="#bdbdbd" stroke="#333"/><circle cx="{x+30}" cy="150" r="22" fill="#e0c3a8" stroke="#6d4c41"/>'+T(x+55,210,str(n),16,'middle',700) for n,x in [(1,40),(2,200),(3,360)])+'</g>')
s['figures']=[dict(id='hpe11-s076-fig1',svg=fig,caption='Baton exchange: wrong way (cross) and correct way (tick); three grips (1–3)',captionUrdu='بیٹن تبدیل کرنے کا غلط اور درست طریقہ؛ تین گرفتیں (1–3)',captionPashto='د بیټن بدلولو غلطه او سمه طریقه؛ درې نیونې (۱–۳)',labels=[lab('Wrong way','غلط طریقہ','غلطه طریقه'),lab('Correct way','درست طریقہ','سمه طریقه')],sourceGap=dict(note='Simplified coded schematic of the photographic hand drawings (cross and tick marks with three numbered grips); the photographs are not reproduced.'))]
s['sourceNote']='Printed page 74: visual and non-visual methods of baton exchange and the illustration of the correct and wrong ways with three numbered grips.'+NOTE
s['vocabulary']={}
save(s)
# scan 77 = printed 75 (figure)
s=page(77,'u07','75','Three ways of holding the baton; visual and non-visual exchange; finish','بیٹن پکڑنے کے تین طریقے؛ بصری اور غیر بصری تبدیلی؛ اختتام','د بیټن نیولو درې طریقې؛ لیدنیز او غیر لیدنیز بدلون؛ پای','relay-6')
F=Flow(s)
P(s,[]+L([('1۔ پہلے طریقے میں بیٹن کو چھوٹی انگلی اور ساتھ والی انگلی میں پکڑا جاتا ہے۔ شہادت والی انگلی انگوٹھا اور رنگ فنگر کو لائن کے پیچھے رکھا جاتا ہے۔','1. In the first method the baton is held between the little finger and the adjoining finger. The index finger, thumb and ring finger are kept behind the line.','۱. په لومړۍ طریقه کې بیټن په وړې ګوتې او ورسره ګوتې کې نیول کېږي. د شهادت ګوته، غټه ګوته او د ګوتو ګوته (رنګ فنګر) د کرښې شاته ساتل کېږي.'),('2۔ دوسرے طریقے میں بیٹن کو درمیان والی انگلیوں میں پکڑا جاتا ہے۔ چھوٹی انگلی اور شہادت والی انگلی اور انگوٹھا لائن کے پیچھے ہوتے ہیں۔','2. In the second method the baton is held between the middle fingers. The little finger, the index finger and the thumb are behind the line.','۲. په دویمه طریقه کې بیټن په منځنیو ګوتو کې نیول کېږي. وړه ګوته، د شهادت ګوته او غټه ګوته د کرښې شاته وي.'),('3۔ تیسرے طریقے میں رنگ فنگر میں بیٹن کو پکڑا جاتا ہے۔ باقی کی تینوں انگلیاں اور انگوٹھا لائن کے پیچھے رکھا جاتا ہے۔','3. In the third method the baton is held with the ring finger. The remaining three fingers and the thumb are kept behind the line.','۳. په دریمه طریقه کې بیټن په رنګ فنګر کې نیول کېږي. پاتې درې ګوتې او غټه ګوته د کرښې شاته ساتل کېږي.')],'gp'))
F.fg(0)
H(s,'اختتام','Finish','پای')
F.fg(1)
F.done()
def two(y,l1,l2):
    return (f'<circle cx="120" cy="{y}" r="14" fill="#333"/><path d="M120 {y+14} q-6 40 8 70 M120 {y+30} l60 -16 M120 {y+84} l-20 40 M128 {y+84} l22 30" stroke="#333" stroke-width="5" fill="none"/>'
            f'<circle cx="300" cy="{y+10}" r="14" fill="#333"/><path d="M300 {y+24} q-6 40 8 70 M300 {y+40} l-60 -26 M300 {y+94} l-20 36 M308 {y+94} l22 28" stroke="#333" stroke-width="5" fill="none"/>'
            f'<rect x="168" y="{y+6}" width="40" height="8" fill="#5d4037"/>')
fig1=svg(520,220,'Two runners passing a baton: left, the non-visual method (receiving runner holds the hand back without looking) and right, the visual method (runners face each other)',
  two(20,'','')+T(260,210,'Baton exchange (visual / non-visual)',12,'middle',700))
fig2=svg(360,200,'A runner crossing a finishing line on a track with lane numbers 1 to 7',
  ''.join(f'<rect x="60" y="{100+i*12}" width="260" height="11" fill="#e0e0e0" stroke="#999"/>'+T(240,{100+i*12+9},str(i+1),9) if False else '' for i in range(7))+
  '<rect x="60" y="110" width="260" height="80" fill="#cfd8dc" stroke="#78909c"/>'+''.join(f'<line x1="60" y1="{110+i*11}" x2="320" y2="{110+i*11}" stroke="#78909c"/>'+T(280,{110+i*11-2},str(i),9) for i in range(1,8))+
  '<line x1="250" y1="104" x2="250" y2="196" stroke="#c62828" stroke-width="3" stroke-dasharray="5 3"/><circle cx="180" cy="40" r="14" fill="#333"/><path d="M180 54 q-6 36 10 60 M180 70 l36 -10 M180 70 l-30 10 M190 114 l-24 38 M190 114 l24 30" stroke="#333" stroke-width="6" fill="none"/>')
s['figures']=[dict(id='hpe11-s077-fig1',svg=fig1,caption='Baton exchange: non-visual method (right) and visual method (left)',captionUrdu='بیٹن تبدیلی کا غیر بصری طریقہ (دائیں) اور بصری طریقہ (بائیں)',captionPashto='د بیټن بدلون غیر لیدنیز طریقه (ښي) او لیدنیز طریقه (کیڼ)',labels=[],sourceGap=dict(note='Simplified coded stick-figure schematic of the two pairs of runners; the original has two line drawings.')),
 dict(id='hpe11-s077-fig2',svg=fig2,caption='Finish: a runner crossing the finishing line',captionUrdu='اختتام: کھلاڑی اختتامی لکیر عبور کرتے ہوئے',captionPashto='پای: لوبغاړی د پای کرښه تېروي',labels=[lab('Finish','اختتام','پای')],sourceGap=dict(note='Simplified coded redrawing of the grey photo-like illustration of a runner at the line.'))]
s['sourceNote']='Printed page 75: the three ways of holding the baton, the visual/non-visual drawings and the “finish” illustration. The left drawing is labelled “بیٹن تبدیلی کا بصری طریقہ” and the right “بیٹن تبدیلی کا غیر بصری طریقہ”.'+NOTE
s['vocabulary']={}
save(s)
# scan 78 = printed 76
s=page(78,'u07','76','Exercise questions: Chapter 7 (1–9)','مشقی سوالات: باب 7 (1–9)','تمرین پوښتنې: اووم څپرکی (۱–۹)','ex7a')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جواب منتخب کر کے لکھیں۔','1. Select the suitable answer and write it.','۱. مناسب ځواب وټاکئ او ولیکئ.')
MC(s,('i۔ دنیا کی تیز ترین دوڑ ________ ہے۔','i. The fastest race in the world is the ________.','i. د نړۍ تر ټولو ګړندۍ منډه ________ ده.'),[('(الف) 200 میٹر','(a) 200 metres','(الف) ۲۰۰ متره'),('(ب) 400 میٹر','(b) 400 metres','(ب) ۴۰۰ متره'),('(ج) 100 میٹر','(c) 100 metres','(ج) ۱۰۰ متره'),('(د) 1600 میٹر','(d) 1600 metres','(د) ۱۶۰۰ متره')])
MC(s,('ii۔ تمام قسم کی دوڑ میں اگر کھلاڑیوں کی تعداد ________ سے زیادہ ہو تو ہیٹس کرائی جاتی ہے۔','ii. In all kinds of races, if the number of players is more than ________, heats are held.','ii. په ټولو ډولونو منډو کې که د لوبغاړو شمېر له ________ زیات وي نو هیټس کېږي.'),[('(الف) 4','(a) 4','(الف) ۴'),('(ب) 6','(b) 6','(ب) ۶'),('(ج) 8','(c) 8','(ج) ۸'),('(د) 10','(d) 10','(د) ۱۰')])
MC(s,('iii۔ دوڑ میں اختتامی لکیر کو ________ سے چھونا لازمی ہے۔','iii. In a race it is necessary to touch the finishing line with the ________.','iii. په منډه کې د پای کرښه په ________ لمس کول لازمي دي.'),[('(الف) ٹارسو','(a) torso (“Tarsso” as printed)','(الف) ټارسو'),('(ب) پاؤں','(b) foot','(ب) پښه'),('(ج) ہاتھ','(c) hand','(ج) لاس'),('(د) سر','(d) head','(د) سر')])
MC(s,('iv۔ دوڑ میں سٹارٹنگ کے وقت کھلاڑی کے ہاتھ سٹارٹنگ لائن سے ________ ہوں گے۔','iv. In the race at the time of starting the player’s hands will be ________ the starting line.','iv. په منډه کې د پیل په وخت د لوبغاړي لاسونه د پیل له کرښې ________ وي.'),[('(الف) آگے','(a) ahead of','(الف) مخکې'),('(ب) پیچھے','(b) behind','(ب) شاته'),('(ج) دائیں','(c) right of','(ج) ښي'),('(د) بائیں','(d) left of','(د) کیڼ')])
MC(s,('v۔ 200 میٹر دوڑ میں گلی کا درمیانی فاصلہ ________ میٹر ہوتا ہے۔','v. In the 200-metre race the lane width is ________ metres.','v. په ۲۰۰ مترو منډه کې د لین منځنی واټن ________ متره وي.'),[('(الف) 2','(a) 2','(الف) ۲'),('(ب) 2.12','(b) 2.12','(ب) ۲.۱۲'),('(ج) 1.22','(c) 1.22','(ج) ۱.۲۲'),('(د) 1.42','(d) 1.42','(د) ۱.۴۲')])
MC(s,('vi۔ 200 میٹر دوڑ میں دوسری گلی کا زینہ ________ میٹر ہوتا ہے۔','vi. In the 200-metre race the stagger of the second lane is ________ metres.','vi. په ۲۰۰ مترو منډه کې د دویم لین زینه ________ متره وي.'),[('(الف) 3.15','(a) 3.15','(الف) ۳.۱۵'),('(ب) 3.25','(b) 3.25','(ب) ۳.۲۵'),('(ج) 3.45','(c) 3.45','(ج) ۳.۴۵'),('(د) 3.55','(d) 3.55','(د) ۳.۵۵')])
MC(s,('vii۔ سٹینڈرڈ ٹریک پر گلیوں کی تعداد ________ ہوتی ہے۔','vii. On a standard track the number of lanes is ________.','vii. په معیاري ټریک د لینونو شمېر ________ وي.'),[('(الف) 6','(a) 6','(الف) ۶'),('(ب) 7','(b) 7','(ب) ۷'),('(ج) 8','(c) 8','(ج) ۸'),('(د) 10','(d) 10','(د) ۱۰')])
MC(s,('viii۔ گلیوں کا انتخاب ________ کے ذریعے کیا جاتا ہے۔','viii. The choice of lanes is made by ________.','viii. د لینونو ټاکنه د ________ په مټ کېږي.'),[('(الف) مرضی','(a) choice','(الف) خوښه'),('(ب) انتظامیہ','(b) the administration','(ب) اداره'),('(ج) ٹاس','(c) toss','(ج) ټاس'),('(د) قرعہ اندازی','(d) draw','(د) قرعه')])
MC(s,('ix۔ 800 میٹر دوڑ میں معیاری ٹریک کا کل فاصلہ ________ میٹر ہوتا ہے۔','ix. In the 800-metre race the total distance of the standard track is ________ metres.','ix. په ۸۰۰ مترو منډه کې د معیاري ټریک ټول واټن ________ متره وي.'),[('(الف) 200','(a) 200','(الف) ۲۰۰'),('(ب) 400','(b) 400','(ب) ۴۰۰'),('(ج) 600','(c) 600','(ج) ۶۰۰'),('(د) 800','(d) 800','(د) ۸۰۰')])
F.done()
s['sourceNote']='Printed page 76: Chapter 7 exercise questions, multiple-choice items i–ix (continued on the next page).'+NOTE
s['vocabulary']={}
save(s)
# scan 79 = printed 77
s=page(79,'u07','77','Exercise questions: Chapter 7 (10–13) and descriptive questions','مشقی سوالات: باب 7 (10–13) اور تفصیلی سوالات','تمرین پوښتنې: اووم څپرکی (۱۰–۱۳) او تشریحي پوښتنې','ex7b')
F=Flow(s)
MC(s,('x۔ 800 میٹر دوڑ کے لیے زینے ________ میٹر کے دیں گے۔','x. For the 800-metre race the staggers will be given of ________ metres.','x. د ۸۰۰ مترو منډې لپاره زینې د ________ مترو ورکوو.'),[('(الف) 400','(a) 400','(الف) ۴۰۰'),('(ب) 600','(b) 600','(ب) ۶۰۰'),('(ج) 800','(c) 800','(ج) ۸۰۰'),('(د) کوئی نہیں','(d) none','(د) هېڅ نه')])
MC(s,('xi۔ 4 x 100 میٹر ڈاک دوڑ میں بیٹن تبدیلی کا علاقہ ________ میٹر ہوتا ہے۔','xi. In the 4 x 100-metre relay race the baton exchange zone is ________ metres.','xi. په ۴ x ۱۰۰ مترو ریلې منډه کې د بیټن د بدلون سیمه ________ متره وي.'),[('(الف) 10 میٹر','(a) 10 metres','(الف) ۱۰ متره'),('(ب) 20 میٹر','(b) 20 metres','(ب) ۲۰ متره'),('(ج) 30 میٹر','(c) 30 metres','(ج) ۳۰ متره'),('(د) 40 میٹر','(d) 40 metres','(د) ۴۰ متره')])
MC(s,('xii۔ بیٹن کا وزن ________ گرام ہوتا ہے۔','xii. The weight of the baton is ________ grams.','xii. د بیټن وزن ________ ګرامه وي.'),[('(الف) 15','(a) 15','(الف) ۱۵'),('(ب) 30','(b) 30','(ب) ۳۰'),('(ج) 50','(c) 50','(ج) ۵۰'),('(د) 60','(d) 60','(د) ۶۰')])
MC(s,('xiii۔ بیٹن کی لمبائی ________ سینٹی میٹر ہوتی ہے۔','xiii. The length of the baton is ________ centimetres.','xiii. د بیټن اوږدوالی ________ سانتي متره وي.'),[('(الف) 26 تا 30','(a) 26 to 30','(الف) ۲۶ تر ۳۰'),('(ب) 28 تا 30','(b) 28 to 30','(ب) ۲۸ تر ۳۰'),('(ج) 30 تا 32','(c) 30 to 32','(ج) ۳۰ تر ۳۲'),('(د) 32 تا 34','(d) 32 to 34','(د) ۳۲ تر ۳۴')])
H(s,'2۔ درج ذیل سوالوں کے جواب لکھیں۔','2. Write answers to the following questions.','۲. د لاندې پوښتنو ځوابونه ولیکئ.')
for ur,en,ps in [('i۔ 100 میٹر دوڑ کے قوانین و فاؤلز درج کریں۔','i. List the rules and fouls of the 100-metre race.','i. د ۱۰۰ مترو منډې قوانین او فاولونه ولیکئ.'),('ii۔ 100 میٹر دوڑ کی مہارتیں تفصیل سے لکھیں۔','ii. Write in detail the skills of the 100-metre race.','ii. د ۱۰۰ مترو منډې مهارتونه په تفصیل ولیکئ.'),('iii۔ 200 میٹر دوڑ کے قوانین درج کریں۔','iii. List the rules of the 200-metre race.','iii. د ۲۰۰ مترو منډې قوانین ولیکئ.'),('iv۔ 200 میٹر میں زینوں کی پیمائش لکھیں نیز فاؤلز درج کریں۔','iv. Write the measurement of staggers in the 200 metres and also list the fouls.','iv. په ۲۰۰ مترو کې د زینو اندازه ولیکئ همداراز فاولونه ولیکئ.'),('v۔ 800 میٹر دوڑ کے قوانین تحریر کریں۔','v. Write the rules of the 800-metre race.','v. د ۸۰۰ مترو منډې قوانین ولیکئ.'),('vi۔ 800 میٹر کے فاؤلز بیان کریں۔','vi. State the fouls of the 800 metres.','vi. د ۸۰۰ مترو فاولونه بیان کړئ.'),('vii۔ 4 x 100 میٹر دوڑ کے قوانین لکھیں۔','vii. Write the rules of the 4 x 100-metre race.','vii. د ۴ x ۱۰۰ مترو منډې قوانین ولیکئ.'),('viii۔ 4 x 100 میٹر دوڑ میں بیٹن تبدیل کرنے کے طریقے بیان کریں۔','viii. State the methods of changing the baton in the 4 x 100-metre race.','viii. په ۴ x ۱۰۰ مترو منډه کې د بیټن بدلولو طریقې بیان کړئ.')]: Q(s,ur,en,ps)
F.done()
s['sourceNote']='Printed page 77: Chapter 7 exercise questions, multiple-choice items x–xiii, and eight descriptive questions; the lower part of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 80 = printed 78 (figure)
s=page(80,'u07','78','Field events: shot put — circle, weights and stop board','فیلڈ ایونٹس: شاٹ پٹ — دائرہ، وزن اور سٹاپ بورڈ','فیلډ ایونټونه: شاټ پټ — دایره، وزن او سټاپ بورډ','shotput-1')
F=Flow(s)
H(s,'فیلڈ ایونٹس','Field Events','فیلډ ایونټونه')
H(s,'شاٹ پٹ (Shot-put)','Shot Put (Shot-put)','شاټ پټ (Shot-put)')
H(s,'شاٹ پٹ کے قوانین اور مہارتیں:','Rules and Skills of Shot Put:','د شاټ پټ قوانین او مهارتونه:')
P(s,[('دائرہ: گولہ ایک دائرہ کے اندر سے پھینکا جائے گا جسے شاٹ پٹ کا سیکٹر کہتے ہیں۔','Circle: the shot will be thrown from within a circle, whose sector is called the shot-put sector.','دایره: ګولۍ د یوې دایرې له دننه غورځول کېږي چې د شاټ پټ سکتور ورته وايي.'),
('دائرہ کا اندرونی قطر 2.135 میٹر اور دائرے کا نصف حصہ ظاہر کرنے کے لیے دائرے کے باہر دونوں طرف 5 سینٹی میٹر موٹی اور 75 سینٹی میٹر لمبی لائن کھینچی جاتی ہے۔','The inner diameter of the circle is 2.135 metres, and to show the half of the circle a line 5 centimetres thick and 75 centimetres long is drawn outside the circle on both sides.','د دایرې داخلي قطر ۲.۱۳۵ متره دی او د دایرې د نیمایي برخې د ښودلو لپاره د دایرې بهر په دواړو خواوو ۵ سانتي متره ضخامت او ۷۵ سانتي متره اوږده کرښه کاږل کېږي.')]+L([('سیکٹر کا زاویہ: 34.92° ہوگا۔','Angle of the sector: it will be 34.92°.','د سکتور زاویه: ۳۴.۹۲° وي.'),('مردوں کے لیے گولہ کا وزن: 7.265 کلو گرام','Weight of the shot for men: 7.265 kilograms','د نارینه وو لپاره د ګولۍ وزن: ۷.۲۶۵ کیلوګرامه'),('مردوں کے لیے قطر: 110 سے 130 ملی میٹر','Diameter for men: 110 to 130 millimetres','د نارینه وو لپاره قطر: ۱۱۰ نه تر ۱۳۰ ملي متره'),('عورتوں کے لیے وزن: 4 کلو گرام','Weight for women: 4 kilograms','د ښځو لپاره وزن: ۴ کیلوګرامه'),('عورتوں کے لیے قطر: 95 سے 100 ملی میٹر','Diameter for women: 95 to 100 millimetres','د ښځو لپاره قطر: ۹۵ نه تر ۱۰۰ ملي متره')],'sp')+[('سٹاپ بورڈ:','Stop board:','سټاپ بورډ:')]+L([('لمبائی 4 فٹ (1.22 میٹر)','Length 4 feet (1.22 metres)','اوږدوالی ۴ فوټه (۱.۲۲ متره)'),('چوڑائی 11.2 سینٹی میٹر','Width 11.2 centimetres','پلنوالی ۱۱.۲ سانتي متره'),('اونچائی 10.2 سینٹی میٹر','Height 10.2 centimetres','لوړوالی ۱۰.۲ سانتي متره')],'sb'))
F.fg(0)
F.done()
fig=svg(360,300,'A shot-putter standing in the throwing circle on a pink surface, holding the shot at the neck with the other arm raised, and an upward arrow at the waist',
  '<rect x="0" y="180" width="360" height="120" fill="#f48fb1"/><ellipse cx="170" cy="250" rx="120" ry="34" fill="none" stroke="#fff" stroke-width="3"/>'+
  '<circle cx="190" cy="40" r="18" fill="#6d4c41"/><path d="M190 58 l-6 70 M190 66 l50 -20 M190 70 l-44 24" stroke="#c62828" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M184 128 l-30 90 M184 128 l30 86" stroke="#222" stroke-width="12" stroke-linecap="round"/><circle cx="244" cy="44" r="8" fill="#455a64"/><polygon points="190,140 178,166 202,166" fill="#e53935"/>')
s['figures']=[dict(id='hpe11-s080-fig1',svg=fig,caption='Shot-putter in the throwing circle',captionUrdu='دائرے میں گولہ پھینکنے والا کھلاڑی',captionPashto='په دایره کې ګولۍ غورځوونکی لوبغاړی',labels=[],sourceGap=dict(note='Simplified coded stick-style redrawing; the original is a coloured illustration.'))]
s['sourceNote']='Printed page 78: heading of the field events and shot put; the circle, sector angle, weights and diameters for men and women, and the stop board (length, width, height). The heading band is faint and partly overprinted in the scan.'+NOTE
s['vocabulary']={}
save(s)
