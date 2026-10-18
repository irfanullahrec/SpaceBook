from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
def L(items,g):
    return [(a,b,c,dict(listGroup=g)) for a,b,c in items]
def track(w,h,lanes,aria,labels):
    body=''
    for i in range(lanes):
        o=i*14
        body+=f'<rect x="{40+o}" y="{30+o}" width="{w-80-2*o}" height="{h-60-2*o}" rx="{70-o//2}" fill="none" stroke="#1565c0" stroke-width="2"/>'
    return svg(w,h,aria,body+labels)
# scan 66 = printed 64 (figure)
s=page(66,'u07','64','200-metre race: stagger of lanes; rules (1–2)','200 میٹر دوڑ: گلیوں کا فاصلہ؛ قوانین (1–2)','۲۰۰ متره منډه: د لینونو واټن؛ قوانین (۱–۲)','race200-1')
F=Flow(s)
H(s,'200 میٹر دوڑ کے قوانین اور مہارتیں','Rules and Skills of the 200-Metre Race','د ۲۰۰ مترو منډې قوانین او مهارتونه')
P(s,[('200 میٹر دوڑ کا سٹارٹ ٹریک کے نصف حصہ سے ہوتا ہے تمام کھلاڑیوں کو یکساں فاصلہ طے کرنے کے لیے زینے دیے جاتے ہیں۔','The start of the 200-metre race is from half of the track; stagger is given to all the players so that they cover an equal distance.','د ۲۰۰ مترو منډې پیل د ټریک له نیمایي برخې وي ټولو لوبغاړو ته د یو شان واټن وهلو لپاره ستګر (زینې) ورکول کېږي.',GAP('The scan reads “زینے” (steps), which refers to the lane stagger; kept as printed.'))]+L([('پہلی گلی: 0 میٹر','First lane: 0 metres','لومړی لین: ۰ متره'),('دوسری گلی (پہلا زینہ): 3.25 میٹر','Second lane (first stagger): 3.25 metres','دویم لین (لومړی زینه): ۳.۲۵ متره'),('تیسری سے آخری گلی تک: 3.83 میٹر','Third to the last lane: 3.83 metres','دریم لین تر وروستي پورې: ۳.۸۳ متره')],'sg'))
F.fg(0)
H(s,'قوانین:','Rules:','قوانین:')
P(s,[]+L([('1۔ کھلاڑیوں کو گلیاں قرعہ اندازی کے ذریعے دی جائیں گی۔','1. Lanes will be given to the players by draw.','۱. لوبغاړو ته لینونه په قرعه ورکول کېږي.'),('2۔ ہر کھلاڑی کو چست نمبر دیا جائے گا۔','2. Every player will be given a bib number.','۲. هر لوبغاړي ته چست نمبر ورکول کېږي.')],'ru'))
F.done()
fig=track(520,300,4,'Oval running track with four lanes; starting line for 200 metres at the top and a finishing line at the right, with the lane stagger labels 0 m, 3.25 m, 3.83 m and 3.83 m',
  T(250,22,'Starting Line 200m',13,'middle',700)+'<line x1="250" y1="30" x2="250" y2="86" stroke="#c62828" stroke-width="3"/>'+T(222,48,'3.83m',11)+T(222,64,'3.83m',11)+T(222,80,'3.25m',11)+T(222,96,'0m',11)+
  '<line x1="410" y1="160" x2="410" y2="268" stroke="#c62828" stroke-width="3"/>'+T(410,284,'Finishing Line',13,'middle',700))
s['figures']=[dict(id='hpe11-s066-fig1',svg=fig,caption='200-metre track: lane stagger (0 m, 3.25 m, 3.83 m, 3.83 m), starting line and finishing line',captionUrdu='200 میٹر ٹریک: گلیوں کا زینہ، سٹارٹنگ لائن اور فنشنگ لائن',captionPashto='د ۲۰۰ مترو ټریک: د لینونو زینه، د پیل کرښه او د پای کرښه',labels=[lab('Starting Line 200m','سٹارٹنگ لائن 200 میٹر','د ۲۰۰ مترو د پیل کرښه'),lab('Finishing Line','فنشنگ لائن','د پای کرښه')],sourceGap=dict(note='Simplified coded redrawing of the red-lined track diagram (printed in English labels); the printed diagram also shows a bow-tie of straight lines in the infield and a rectangular frame.'))]
s['sourceNote']='Printed page 64: the 200-metre race (stagger distances), the track diagram, and rules 1–2.'+NOTE
s['vocabulary']={}
save(s)
# scan 67 = printed 65
s=page(67,'u07','65','200-metre rules (3–11) and fouls','200 میٹر کے قوانین (3–11) اور فاؤلز','د ۲۰۰ مترو قوانین (۳–۱۱) او فاولونه','race200-2')
F=Flow(s)
P(s,[]+L([('3۔ ہر کھلاڑی اپنی گلی میں دوڑ مکمل کرے گا۔','3. Every player will complete the race in his own lane.','۳. هر لوبغاړی په خپل لین کې منډه بشپړوي.'),('4۔ اگر کھلاڑیوں کی تعداد 8 سے زیادہ ہو تو ہیٹس کرائی جائیں گی۔','4. If the number of players is more than 8, heats will be held.','۴. که د لوبغاړو شمېر له ۸ زیات وي نو هیټس به وشي.'),('5۔ کھلاڑیوں کے ہاتھ سٹارٹ کے وقت سٹارٹنگ لائن سے پیچھے ہوں گے۔','5. The players’ hands will be behind the starting line at the time of the start.','۵. د لوبغاړو لاسونه د پیل په وخت د پیل کرښې شاته وي.'),('6۔ کوئی کھلاڑی ٹریک سے باہر چلا جائے تو دوبارہ شامل نہیں ہو سکتا۔','6. If a player goes out of the track he cannot rejoin.','۶. که کوم لوبغاړی له ټریک نه بهر لاړ شي نو بېرته نشي شاملېدای.'),('7۔ کھلاڑی کوئی ایسی چیز استعمال نہیں کر سکتا جس سے دوڑ میں مدد ملتی ہو۔','7. A player cannot use anything by which he would get help in the race.','۷. لوبغاړی کومه داسې شی نشي کارولای چې له هغه په منډه کې مرسته ترلاسه شي.'),('8۔ جو کھلاڑی ہیٹ میں کامیاب ہوگا وہی فائنل میں حصہ لے گا۔','8. The player who succeeds in the heat will take part in the final.','۸. هغه لوبغاړی چې په هیټ کې بریالی شي همدا به په پای لوبه کې برخه اخلي.'),('9۔ غلط سٹارٹ کی صورت میں وارننگ یا مقابلہ سے اخراج ہوگا۔','9. In case of a false start there will be a warning or expulsion from the competition.','۹. د غلط پیل په صورت کې به خبرداری یا له سیالۍ شړل وي.'),('10۔ گلی کی چوڑائی 1.22 میٹر ہوگی۔','10. The width of a lane will be 1.22 metres.','۱۰. د لین پلنوالی به ۱.۲۲ متره وي.'),('11۔ سٹینڈرڈ ٹریک پر 8 گلیاں ہوتی ہیں۔','11. A standard track has 8 lanes.','۱۱. په معیاري ټریک ۸ لینونه وي.')],'ru'))
H(s,'فاؤلز:','Fouls:','فاولونه:')
P(s,[]+L([('1۔ سٹارٹ کے وقت لائن سے ہاتھوں کا آگے ہونا۔','1. The hands being ahead of the line at the time of the start.','۱. د پیل په وخت د کرښې نه د لاسونو مخکې کېدل.'),('2۔ اپنی گلی میں دوڑ مکمل نہ کرنا۔','2. Not completing the race in one’s own lane.','۲. په خپل لین کې منډه بشپړه نه کول.'),('3۔ کسی دوسرے کھلاڑی کے لیے رکاوٹ پیدا کرنا۔','3. Creating an obstruction for another player.','۳. د بل لوبغاړي لپاره خنډ پیدا کول.'),('4۔ چیسٹ نمبر کے بغیر دوڑنا۔','4. Running without a chest number.','۴. پرته له چیسټ نمبر منډې وهل.'),('5۔ اپنی ہیٹ کے بغیر بھاگنا۔','5. Running without one’s own heat.','۵. پرته له خپل هیټ منډې وهل.'),('6۔ فائر سے پہلے بھاگنا۔','6. Running before the fire.','۶. له فایر نه مخکې منډې وهل.'),('7۔ کسی کھلاڑی یا عہدیدار سے ناشائستہ رویہ اختیار کرنا۔','7. Adopting improper behaviour towards a player or official.','۷. له کوم لوبغاړي یا عهدېدار سره ناوړه چلند کول.')],'fl'))
F.done()
s['sourceNote']='Printed page 65: rules 3–11 of the 200-metre race and a list of seven fouls; the lower part of the page is blank. The page number “65” sits in a hexagon near the left of the footer.'+NOTE
s['vocabulary']={}
save(s)
# scan 68 = printed 66
s=page(68,'u07','66','Skills of the 200-metre race','200 میٹر دوڑ کی مہارتیں','د ۲۰۰ مترو منډې مهارتونه','race200-3')
F=Flow(s)
H(s,'200 میٹر دوڑ کی مہارتیں','Skills of the 200-Metre Race','د ۲۰۰ مترو منډې مهارتونه')
H(s,'1۔ آن یور مارکس:','1. On Your Marks:','۱. آن یور مارکس:')
P(s,[('کھلاڑی سٹارٹنگ لائن پر کروچ پوزیشن میں بیٹھے گا۔ دونوں پاؤں زمین پر ہوں گے۔ ہاتھ لائن سے پیچھے ہوں گے جسم حالت سکون میں ہوگا۔ انگوٹھے اندر کی طرف اور انگلیاں باہر کی طرف ہوں گی۔','The player will sit on the starting line in the crouch position. Both feet will be on the ground. The hands will be behind the line and the body will be in a state of rest. The thumbs will be towards the inside and the fingers towards the outside.','لوبغاړی به د پیل پر کرښه د کروچ په حالت کې کېني. دواړه پښې به په ځمکه وي. لاسونه به د کرښې شاته وي بدن به د سکون په حالت کې وي. ګوتې به دننه لوري ته او نورې ګوتې به بهر لوري ته وي.')])
H(s,'2۔ سیٹ:','2. Set:','۲. سیټ:')
P(s,[('جو نہی سیٹ کا اعلان ہوں کھلاڑی جسم کو اوپر اٹھائے گا اور چھاتی کو لائن سے آگے نکالے گا۔','As soon as “Set” is announced, the player will raise his body and push his chest forward of the line.','همدا چې د سیټ اعلان وشي لوبغاړی به بدن پورته کوي او سینه به له کرښې مخکې وباسي.')])
H(s,'3۔ وسل / فائر:','3. Whistle / Fire:','۳. وسل / فایر:')
P(s,[('جب فائر کی آواز آئے کھلاڑی کا جسم جھکا ہو گا پہلے 100 میٹر تک رفتار میں اضافہ کی کوشش کرنی چاہیے اور جسم کو آہستہ آہستہ سیدھا کیا جائے۔','When the sound of the fire comes, the player’s body will be bent; up to the first 100 metres an effort should be made to increase speed and the body should be gradually straightened.','کله چې د فایر غږ راشي د لوبغاړي بدن به کږ وي لومړنیو ۱۰۰ مترو پورې په ګړندیتوب کې د زیاتوالي هڅه باید وشي او بدن ورو ورو سیده کړای شي.'),
('آخری 100 میٹر میں بازوؤں اور ٹانگوں کی بھرپور طاقت کا استعمال کیا جائے اور رفتار برقرار رکھی جائے۔ اختتام پر پہنچتے ہی چھاتی کو آگے کی طرف بڑھایا جائے اور اختتامی لکیر کو عبور کیا جائے۔','In the last 100 metres the full strength of the arms and legs should be used and the speed should be maintained. On reaching the end the chest should be pushed forward and the finishing line crossed.','په وروستیو ۱۰۰ مترو کې د لاسونو او پښو بشپړ ځواک وکارول شي او ګړندیتوب وساتل شي. پای ته رسېدو سره سم سینه مخکې لوري ته وغځول شي او د پای کرښه تېره شي.')])
F.done()
s['sourceNote']='Printed page 66: skills of the 200-metre race (on your marks, set, fire/whistle and finish); the lower half of the page is blank. The footer strip is cropped in the scan.'+NOTE
s['vocabulary']={}
save(s)
# scan 69 = printed 67 (figure)
s=page(69,'u07','67','The 800-metre race and its track','800 میٹر دوڑ اور اس کا ٹریک','۸۰۰ متره منډه او د هغې ټریک','race800-1')
F=Flow(s)
H(s,'800 میٹر دوڑ','800-Metre Race','۸۰۰ متره منډه')
P(s,[('800 میٹر دوڑ کو درمیانے فاصلے کی دوڑ بھی کہتے ہیں۔ یہ دوڑ بھی 400 میٹر کی سٹینڈرڈ ٹریک میں دوڑی جاتی ہے۔ اس دوڑ کے لیے 400 میٹر کے زینے دیے جاتے ہیں۔ تمام کھلاڑیوں کو گلیاں قرعہ اندازی سے دی جاتی ہیں۔ 800 میٹر دوڑ کی سٹارٹ اور اختتام ایک ہی جگہ پر ہوتا ہے۔','The 800-metre race is also called a middle-distance race. This race too is run on a standard track of 400 metres. For this race the staggers of 400 metres are given. Lanes are given to all players by draw. The start and the end of the 800-metre race are at the same place.','۸۰۰ متره منډه ته منځنی واټن منډه هم وايي. دا منډه هم د ۴۰۰ مترو په معیاري ټریک وهل کېږي. د دې منډې لپاره د ۴۰۰ مترو زینې ورکول کېږي. ټولو لوبغاړو ته لینونه په قرعه ورکول کېږي. د ۸۰۰ مترو منډې پیل او پای په یوه ځای کې وي.',GAP('The printed “زینے” (stagger) is kept; it refers to the lane stagger for the first bend.')),
('800 میٹر کے دوڑ کے لیے ٹریک:','Track for the 800-metre race:','د ۸۰۰ مترو منډې لپاره ټریک:')])
F.fg(0)
P(s,[('800 میٹر دوڑ کے لیے ٹریک','Track for the 800-metre race','د ۸۰۰ مترو منډې لپاره ټریک')])
F.done()
fig=track(520,320,5,'Oval track with five lanes for the 800-metre race; the start and finishing line at the lower right and the stagger labels 0 m, 7.04 m and 7.67 m on the left',
  T(200,20,'800m Starting and Finishing Line',12,'middle',700)+'<line x1="410" y1="244" x2="410" y2="300" stroke="#c62828" stroke-width="3"/>'+T(410,314,'800 m Start and Finishing Line',11,'middle',700)+T(70,150,'7.67m',10)+T(96,150,'7.67m',10)+T(120,150,'7.67m',10)+T(142,150,'7.67m',10)+T(166,150,'7.04m',10)+T(210,160,'0m',10))
s['figures']=[dict(id='hpe11-s069-fig1',svg=fig,caption='Track for the 800-metre race (start and finishing line; stagger 0 m, 7.04 m, 7.67 m)',captionUrdu='800 میٹر دوڑ کے لیے ٹریک (سٹارٹ اور فنشنگ لائن؛ زینے 0، 7.04، 7.67 میٹر)',captionPashto='د ۸۰۰ مترو منډې لپاره ټریک (د پیل او پای کرښه؛ زینې ۰، ۷.۰۴، ۷.۶۷ متره)',labels=[lab('800m Starting and Finishing Line','800 میٹر سٹارٹ اور فنشنگ لائن','د ۸۰۰ مترو د پیل او پای کرښه')],sourceGap=dict(note='Simplified coded oval track; the original red-line drawing shows nine lanes and stagger labels 0 m, 7.04 m and four of 7.67 m.'))]
s['sourceNote']='Printed page 67: introduction of the 800-metre race and the track diagram (labels printed in English); the caption under the diagram repeats “800 میٹر دوڑ کے لیے ٹریک”.'+NOTE
s['vocabulary']={}
save(s)
# scan 70 = printed 68
s=page(70,'u07','68','Rules and fouls of the 800-metre race','800 میٹر دوڑ کے قوانین اور فاؤلز','د ۸۰۰ مترو منډې قوانین او فاولونه','race800-2')
F=Flow(s)
H(s,'800 میٹر دوڑ کے قوانین:','Rules of the 800-Metre Race:','د ۸۰۰ مترو منډې قوانین:')
P(s,[]+L([('1۔ دوڑ میں گلیاں قرعہ اندازی کے ذریعے دی جاتی ہے۔','1. In the race lanes are given by draw.','۱. په منډه کې لینونه په قرعه ورکول کېږي.'),('2۔ دوڑ میں اگر کھلاڑیوں کی تعداد 8 سے زیادہ ہوں تو ہیٹ کروائی جائیگی اور اس میں 8 بہترین کھلاڑیوں کا انتخاب کر کے فائنل کرایا جائے گا۔','2. In the race, if the number of players is more than 8, a heat will be held and from it the 8 best players will be selected and the final held.','۲. په منډه کې که د لوبغاړو شمېر له ۸ زیات وي نو هیټ به وشي او په هغې کې د ۸ غوره لوبغاړو ټاکلو سره پای لوبه کېږي.'),('3۔ اگر کھلاڑیوں کی تعداد 8 یا 8 سے کم ہو تو دوڑ فائنل ہوگی۔','3. If the number of players is 8 or fewer than 8, the race will be the final.','۳. که د لوبغاړو شمېر ۸ یا له ۸ کم وي نو منډه پای لوبه وي.'),('4۔ ہر کھلاڑی کو دو نمبر دیے جائیں گے ایک پشت پر اور دوسرا چھاتی پر لگائے گا۔','4. Every player will be given two numbers; he will put one on the back and the other on the chest.','۴. هر لوبغاړي ته دوه نمبرونه ورکول کېږي یو به په شا او بل به په سینه لګوي.'),('5۔ اگر کوئی کھلاڑی اپنی مرضی سے دوڑ چھوڑے تو اسے دوبارہ شامل نہیں کیا جائے گا۔','5. If any player leaves the race of his own will he will not be included again.','۵. که کوم لوبغاړی په خپله خوښه منډه پرېږدي نو بېرته به شامل نشي.'),('6۔ کھلاڑی اپنے لیے دوڑنے کے راستے پر کوئی نشان معاونت کے لیے نہیں رکھ سکتا۔','6. A player cannot put any mark for his own help on the path of running.','۶. لوبغاړی د خپل ځان لپاره د منډو په لار کومه نښه د مرستې لپاره نشي ایښودلای.'),('7۔ کھلاڑی ایسی چیز استعمال نہیں کر سکتا جو دوڑ میں مدد دے سکے۔','7. A player cannot use anything which can help in the race.','۷. لوبغاړی داسې شی نشي کارولای چې په منډه کې مرسته وکړي.'),('8۔ کھلاڑی ننگے پاؤں یا جوتوں کے ساتھ دوڑنے کا حق رکھتا ہے۔','8. A player has the right to run barefoot or with shoes.','۸. لوبغاړی په لوڅو پښو یا بوټونو سره منډو حق لري.'),('9۔ دوڑ دو چکروں میں مکمل ہوگا۔','9. The race will be completed in two laps.','۹. منډه په دوو ګردشونو کې بشپړېږي.')],'ru'))
H(s,'800 میٹر دوڑ کے فاؤلز:','Fouls of the 800-Metre Race:','د ۸۰۰ مترو منډې فاولونه:')
P(s,[]+L([('1۔ چسٹ نمبر کے بغیر دوڑ میں حصہ لینا۔','1. Taking part in the race without a chest number.','۱. پرته له چسټ نمبر په منډه کې برخه اخیستل.'),('2۔ کسی دوسرے کھلاڑی کے دوڑ میں رکاوٹ ڈالنا۔','2. Creating an obstruction in another player’s race.','۲. د بل لوبغاړي په منډه کې خنډ اچول.'),('3۔ کسی دوسرے کھلاڑی کو دھکادے کر گرا دینا۔','3. Pushing another player and making him fall.','۳. بل لوبغاړی په ټېل وهلو سره راغورځول.'),('4۔ فائر کرنے سے پہلے بھاگنا۔','4. Running before the fire.','۴. له فایر کولو نه مخکې منډې وهل.'),('5۔ دوڑ کو مکمل نہ کرنا۔','5. Not completing the race.','۵. منډه بشپړه نه کول.'),('6۔ کوئی ایسی چیز استعمال کرنا جو دوڑ میں مدد دے سکے۔','6. Using anything which can help in the race.','۶. کومه داسې شی کارول چې په منډه کې مرسته وکړي.')],'fl'))
F.done()
s['sourceNote']='Printed page 68: rules 1–9 and six fouls of the 800-metre race. The page number “68” and the footer strip are cropped at the foot of the scan.'+NOTE
s['vocabulary']={}
save(s)
