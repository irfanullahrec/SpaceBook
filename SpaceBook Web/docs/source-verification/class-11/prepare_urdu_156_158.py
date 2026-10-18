from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n10',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
def V1(s,u1,e1,p1): add(s,f'v{len(s["paras"])+1}',e1,u1,p1,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 156 = printed 149
s=page(156,'n10','149','Exercise (Mashq) on Purana Coat','مشق: «پرانا کوٹ» پر سوالات','تمرین: «زوړ کوټ» پوښتنې','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ شاعر نے پرانے کوٹ کی خامیوں کو کیسے خوبیاں بنا کر پیش کیا ہے۔','1. How has the poet presented the defects of the old coat as virtues?','۱. شاعر د زوړ کوټ نیمګړتیاوې څنګه ښېګڼې جوړې کړې او وړاندې کړې دي؟')
Q(s,'2۔ تشبیہ اور استعارے سے کیا مراد ہے؟ اس نظم میں شاعر نے پرانے کوٹ کے لیے کیا کیا تشبیہات اور استعارات استعمال کیے ہیں؟','2. What is meant by simile and metaphor? What similes and metaphors has the poet used in this poem for the old coat?','۲. د تشبیه او استعارې نه څه مراد دی؟ پدې نظم کې شاعر د زوړ کوټ لپاره کومې کومې تشبیهات او استعارې کارولي دي؟')
Q(s,'3۔ مصرعے مکمل کریں۔','3. Complete the lines.','۳. مصرعې بشپړې کړئ.')
for t in [('الف) کسی مرے ہوئے گورے کی ____________','(a) “Kisi mare hue gore ki ____________”','(الف) د کوم مړ شوي ګوري ____________'),
('ب) پہن چکے ہیں اسے ____________','(b) “Pehen chuke hain use ____________”','(ب) اغوستې یې ده ____________'),
('ج) میاں بزرگوں کا سایہ ____________','(c) “Mian buzurgon ka saya ____________”','(ج) ورورګلو د بزرګانو سیوری ____________'),
('د) نئی طرح کی یہ صنعت ہے ____________','(d) “Nai tarah ki ye sanat hai ____________”','(د) نوې ډول دا صنعت دی ____________'),
('ہ) گذشتہ صدیوں کی تاریخ کا ____________','(e) “Guzishta sadiyon ki tareekh ka ____________”','(ه) د تېرو پېړیو د تاریخ ____________')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-3')
Q(s,'4۔ نظم «پرانا کوٹ» کا مرکزی خیال لکھیں۔','4. Write the central idea of the poem “Purana Coat”.','۴. د «زوړ کوټ» نظم مرکزي خیال ولیکئ.')
Q(s,'5۔ قافیہ ہم آواز الفاظ کو کہتے ہیں، جیسے کوٹ اور نوٹ، دکان اور نکتہ داں۔ اس نظم میں اور کون کون سے قافیے استعمال ہوئے ہیں؟','5. Qafiya is the name for rhyming words, like “coat” and “note”, “dukan” and “nukta-dan”. Which other rhymes have been used in this poem?','۵. قافیه همغږو الفاظو ته وايي لکه کوټ او نوټ، دکان او نکته دان. پدې نظم کې نورې کومې قافیې کارول شوي دي؟')
Q(s,'6۔ کسی شاعر کے ایک مصرعے پر دوسرا مصرع لگا کر نیا شعر کہنا «صنعتِ تضمین» کہلاتا ہے۔ مثلاً: «بنا ہے کوٹ یہ نیلامی کی دکان کے لیے / صلائے عام ہے یارانِ نکتہ داں کے لیے»۔ ایسے تین اشعار تحریر کریں جن میں صنعتِ تضمین کا استعمال ہو۔','6. To compose a new verse by adding another line to a line of some poet is called “sanat-e-tazmeen”. For example: “This coat was made for the auction shop; / it is a general invitation for friends who know subtleties.” Write three couplets in which the figure tazmeen is used.','۶. د کوم شاعر پر یوه مصرعه بله مصرعه ورزیاتولو سره نوی شعر ویل «صنعت تضمین» بلل کېږي. مثلاً: «دا کوټ د نیلام د دوکان لپاره جوړ شوی / د نکته پوهو ملګرو لپاره عام بلنه ده». داسې درې شعرونه ولیکئ چې په هغو کې صنعت تضمین کارول شوی وي.')
F.done()
s['sourceNote']='Printed page 149 (scan 156): “Mashq” title and questions 1–6 (question 3 has five half-lines with blank rules for completion; question 6 quotes the couplet on the page).'+NOTE
s['vocabulary']={}
save(s)
# scan 157 = printed 150
s=page(157,'n11','150','Syed Zameer Jafri (poet profile)','سیّد ضمیر جعفری (شاعر کا تعارف)','سید ضمیر جعفري (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'سیّد ضمیر جعفری','Syed Zameer Jafri','سید ضمیر جعفري')
P(s,'پیدایش: یکم جنوری ۱۹۱۶ء — وفات: ۱۲؍ مئی ۱۹۹۹ء','Born: 1 January 1916 — Died: 12 May 1999','زېږېدنه: ۱ جنوري ۱۹۱۶ز — وفات: ۱۲ مۍ ۱۹۹۹ز')
P(s,'اصل نام سیّد ضمیر حسین ہے۔ ضلع جہلم کے ایک گاؤں چک عبدالخالق میں پیدا ہوئے۔ ابتدائی تعلیم گاؤں کے اسکول میں حاصل کی۔ ثانوی تعلیم گورنمنٹ ہائی اسکول جہلم سے پائی۔ گورنمنٹ کالج کیمبل پور (اٹک) سے ایف اے کیا اور بی اے کی ڈگری اسلامیہ کالج لاہور سے حاصل کی۔','His real name is Syed Zameer Hussain. He was born in a village, Chak Abdul Khaliq, in district Jhelum. He received his early education in the village school. He got secondary education at Government High School Jhelum. He did his FA from Government College Campbellpur (Attock) and obtained the BA degree from Islamia College Lahore.','اصلي نوم یې سید ضمیر حسین دی. د جهلم د ولسوالۍ په یوه کلي چک عبدالخالق کې زېږېدلی دی. لومړنۍ زده‌کړه یې د کلي په ښوونځي کې وکړه. ثانوي زده‌کړه یې د ګورنمنټ هاى ښوونځي جهلم نه ترلاسه کړه. د ګورنمنټ کالج کیمبل پور (اټک) نه یې ایف اے وکړ او د بي اے ډګري یې له اسلامیه کالج لاهور نه ترلاسه کړه.')
P(s,'تعلیم مکمل کرنے کے بعد صحافت کے کوچے میں قدم رکھا اور مولانا چراغ حسن حسرتؔ کے اخبار «شیرازہ» میں بطور معاون مدیر کام کرتے رہے۔ بعد میں ایک فوجی اخبار کے عملۂ ادارت میں شامل ہو گئے۔ وہاں سے فوج میں کمیشن حاصل کیا۔ میجر کی حیثیّت سے ملازمت سے سبک دوش ہوئے۔ بعد ازاں مختلف سرکاری عہدوں پر فائز رہے۔','After completing his education he entered the lane of journalism and worked as assistant editor in the newspaper “Shiraza” of Maulana Chiragh Hasan Hasrat. Later he joined the editorial staff of an army newspaper. From there he obtained a commission in the army. He retired from service as a Major. Afterwards he held various government posts.','د زده‌کړې له بشپړولو وروسته یې د ژورنالیزم کوڅې ته قدم کېښود او د مولانا چراغ حسن حسرت په ورځپاڼه «شیرازه» کې د مرستیال مدیر په توګه کار کاوه. وروسته د یوې پوځي ورځپاڼې د مدیریت عملې کې شامل شو. له هغه ځایه یې په پوځ کې کمېشن ترلاسه کړ. د میجر په حیثیت له دندې سبکدوش شو. وروسته په بېلابېلو دولتي دندو پاتې شو.')
P(s,'سیّد ضمیر جعفری نے مزاحیہ شاعری میں زندگی کی ناہم واریوں کو آشکار کرنے اور تاثر کی شدّت سے اصلاحی مقاصد حاصل کرنے کی کوشش کی ہے۔ اُن کے ہاں زندگی کو اعتنا کی نظر سے دیکھنے اور اس کی حالت بدلنے کا انداز نمایاں ہے۔ اُن کے منتخب کردہ موضوعات پھول کی طرح کِھلتے اور بے ساختہ مسکراہٹ کو جنم دیتے ہیں۔','In humorous poetry Syed Zameer Jafri has tried to expose the disparities of life and to achieve reformative aims through the intensity of impression. In him the manner of looking at life with consideration and of changing its condition is prominent. The subjects he chose open like flowers and give birth to spontaneous smiles.','سید ضمیر جعفري په مزاحیه شاعرۍ کې د ژوند ناهموارۍ څرګندولو او د تاثر د شدت له لارې اصلاحي موخو ترلاسه کولو هڅه کړې ده. د هغه سره ژوند ته په پام کتل او د هغه حالت بدلولو انداز څرګند دی. د هغه ټاکل شوي موضوعات د ګل په څېر خلاصېږي او بې ساخته موسکا پیدا کوي.')
P(s,'تصانیف: قریۂ جاں، مافی الضمیر، مسدّسِ بدحالی، گنڈر شیر خاں، کتابی چہرے، من میلہ وغیرہ۔','Works: Qarya-e-Jaan, Maafi-uz-Zameer, Musaddas-e-Badhali, Gundar Sher Khan (title as read), Kitabi Chehre, Man Mela, etc.','تصنیفات: قریه جان، مافي الضمیر، مسدس بدحالي، ګنډر شیر خان (سرلیک لکه څنګه چې لوستل شوی)، کتابي څېرې، من میله او نور.')
F.done()
s['sourceNote']='Printed page 150 (scan 157): ornamental title “سیّد ضمیر جعفری”, portrait (not reproduced), birth/death boxes (1 January 1916 and 12 May 1999), biography and list of works (one title is read approximately).'+NOTE
s['vocabulary']={}
save(s)
# scan 158 = printed 151
s=page(158,'n11','151','Yeh Sarkain (Syed Zameer Jafri)','یہ سڑکیں (سیّد ضمیر جعفری)','دا سړکونه (سید ضمیر جعفري)','poem1')
F=Flow(s)
H(s,'یہ سڑکیں','Yeh Sarkain (These Roads)','دا سړکونه')
for r in [
('زمیں پر آدمی کی اوّلیں ایجاد یہ سڑکیں','پرانے وقت کے بغداد کی اولاد یہ سڑکیں','These roads, the first invention of man on earth,','these roads, the offspring of the Baghdad of old times,','پر ځمکه د انسان لومړنی اختراع دا سړکونه','د زړې زمانې د بغداد اولاد دا سړکونه'),
('ہمارے شہر کی مادر پدر آزاد یہ سڑکیں','مرمّت کی حدوں سے زائد المیعاد یہ سڑکیں','these roads of our city, wholly free (of any parent),','these roads, beyond the limits of repair, expired in date,','زموږ د ښار پخپله خوښه پرېښودل شوي دا سړکونه','د ترمیم له حده زیات نېټه تېر شوي دا سړکونه')]:
    V(s,*r)
V1(s,'بظاہر صید، لیکن اصل میں صیّاد یہ سڑکیں','seemingly the prey, but in reality these roads are the hunters.','په ظاهر کې ښکار، خو په اصل کې ښکارچي دا سړکونه')
for r in [
('دمِ بارانِ رحمت گرد کا گرداب ہو جانا','گڑھوں کا پھیل کر تالاب در تالاب ہو جانا','At the moment of the rain of mercy the dust becoming a whirlpool,','pits spreading and becoming pond upon pond,','د رحمت د باران په شېبه د دوړو ګردباد کېدل','د ګټو غځېدل او حوض په حوض کېدل'),
('پھر کر نالیوں کا «رستم و سہراب» ہو جانا','محلّے کے گلی کوچوں کا زہرہ آب ہو جانا','the drains going round and becoming “Rustam and Sohrab”,','the lanes and streets of the quarter turning to gall-water —','بیا ګرځېدلو نالیو د «رستم او سهراب» کېدل','د سیمې د کوڅو زهره اوبه کېدل')]:
    V(s,*r)
V1(s,'مہینوں تک برنگِ ہر چہ بادا باد یہ سڑکیں','for months these roads remain in the colour of “come what may”.','میاشتې پورې په رنګ د هر څه چې کېږي دا سړکونه')
for r in [
('بہر گامے سڑک کھا جانے والی کھائیاں دیکھو','چھتے راستوں کی ٹوٹتی انگڑائیاں دیکھو','See at every step the chasms that swallow the road,','see the breaking yawns of the hive-like paths;','په هر ګام د سړک خوړونکي کندې وګورئ','د غوټې لارو ماتېدونکې انګړیدنې وګورئ'),
('کھڑی اونچائیوں کے پیٹ میں گہرائیاں دیکھو','گڑھوں کی جا بجا بہزادیاں، چغتائیاں دیکھو','see the depths in the belly of the standing heights,','see here and there the “Behzads” and “Chughtais” of the pits —','د ولاړو لوړو په ګېډه کې ژورتیاوې وګورئ','د ګټو ځای په ځای بهزادۍ، چغتایۍ وګورئ')]:
    V(s,*r)
V1(s,'نقوشِ مانی و چغتائی، و بہزاد یہ سڑکیں','these roads are the designs of Mani, Chughtai and Behzad.','د مانۍ، چغتایي او بهزاد نقشونه دا سړکونه')
for r in [
('ہم اِن سے حلم و صبر و شکر کا پیغام لیتے ہیں','کہ جب چلتے ہیں کم از کم خدا کا نام لیتے ہیں','From these we take the message of forbearance, patience and gratitude,','for when we walk at least we take the name of God.','موږ له دغو نه د حلم، صبر او شکر پیغام اخلو','چې کله ځو لږ تر لږه د خدای نوم اخلو'),
('یہ کام آئیں نہ آئیں ہم انھی سے کام لیتے ہیں','«گلوں سے خار بہتر ہیں، جو دامن تھام لیتے ہیں»','Whether they are of use or not, we make use of these very ones;','“Thorns are better than roses, for they hold the skirt.”','دا په کار راشي که نه موږ همدا کاروو','«له ګلانو نه خاره ښه دي چې لمن نیسي»')]:
    V(s,*r)
V1(s,'ہم ان سے مطمئن ہیں اور ہم سے شاد یہ سڑکیں','we are content with them and these roads are glad with us.','موږ ترې مطمئن یو او دا سړکونه له موږ خوشاله دي')
F.done()
s['sourceNote']='Printed page 151 (scan 158): title “یہ سڑکیں” in an ornamental frame, running head “سیّد ضمیر جعفری”, and four stanzas of the poem (each two rows of right and left half-lines and a centred closing line). “پھر کر نالیوں” and “چغتائیاں” are read as printed; “زہرہ آب ہو جانا” is the idiom for becoming terrified.'+NOTE
s['vocabulary']={}
save(s)
