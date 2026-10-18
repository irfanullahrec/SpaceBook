from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='g02',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 174 = printed 167
s=page(174,'g02','167','Exercise (Mashq) on the ghazal of Mir Dard','مشق: غزلِ درد پر سوالات','تمرین: د درد د غزل پوښتنې','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ خالی جگہ مناسب لفظ کے انتخاب سے پُر کریں۔','1. Fill in the blank with the suitable word chosen from the brackets.','۱. تش ځای د مناسب کلمې په غوره کولو ډک کړئ.')
for t in [('الف) قتلِ عاشق کسی ............ سے کچھ دور نہ تھا (معشوق، محبوب، دشمن)','(a) The killing of a lover was not far from any ............ (mashooq, mehboob, dushman)','(الف) د عاشق وژل له کوم ............ نه څه لرې نه و (معشوق، محبوب، دښمن)'),
('ب) رات مجلس میں ترے ............ کے شعلے کے حضور (آگ، حسن، نار)','(b) Last night in the assembly, in the presence of the flame of your ............ (fire, beauty, flame)','(ب) د تیرې شپې په مجلس کې ستا د ............ د شعلې په حضور (اور، حسن، لمبه)'),
('ج) واں پہ پہنچا کہ ............ کا بھی مقدور نہ تھا (انسان، آدمی، فرشتے)','(c) He reached where even ............ had no power (insaan, aadmi, farishta)','(ج) هلته ورسېد چې ............ هم وس نه و (انسان، آدم، فرښته)'),
('د) مُحتسِب آج تو ............ میں تیرے ہاتھوں (تھانے، جیل خانے، مے خانے)','(d) Muhtasib, today in the ............ because of you (police station, prison, tavern)','(د) محتسبه نن په ............ کې ستا په لاس (تهانه، زندان، میخانه)'),
('ہ) دردؔ کے ملنے سے اے ............ بُرا کیوں مانا (یار، دوست، دشمن)','(e) Friend ............! Why did you take offence at meeting Dard? (yaar, dost, dushman)','(ه) د درد له ملاقات نه ای ............ بد ولې ګڼې (یار، ملګری، دښمن)')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-1')
Q(s,'2۔ ردیف کسے کہتے ہیں؟ دردؔ کی غزل کی ردیف کی نشان دہی کریں۔','2. What is radif? Point out the radif of Dard’s ghazal.','۲. ردیف ته څه وايي؟ د درد د غزل ردیف په نښه کړئ.')
Q(s,'3۔ دور، دستور، مذکور وغیرہ اس غزل کے قافیے ہیں۔ ایسے پانچ ہم قافیہ الفاظ لکھیں جو اس غزل میں موجود نہ ہوں۔','3. Door, dastoor, mazkoor etc. are the rhymes of this ghazal. Write five such rhyming words which are not present in this ghazal.','۳. دور، دستور، مذکور او نور د دې غزل قافیې دي. داسې پنځه هم قافیه الفاظ ولیکئ چې پدې غزل کې موجود نه وي.')
Q(s,'4۔ کنایہ قریب اور کنایہ بعید میں، مثالوں کی مدد سے فرق واضح کریں۔','4. Make clear the difference between near kinaya and far kinaya with the help of examples.','۴. د نژدې کنایې او لرې کنایې ترمنځ توپیر د بېلګو په مرسته څرګند کړئ.')
Q(s,'5۔ اس غزل کے قوافی لکھیں۔','5. Write the rhymes of this ghazal.','۵. د دې غزل قافیې ولیکئ.')
Q(s,'6۔ درج ذیل کی تعریف کریں اور دو دو مثالیں لکھیں۔ مراعاۃ النظیر، حسنِ تعلیل، لف و نشر، تلمیح، تضمین۔','6. Define the following and write two examples each: muraat-un-nazeer, husn-e-ta’leel, laff-o-nashr, talmeeh, tazmeen.','۶. د لاندې تعریف وکړئ او دوه دوه بېلګې ولیکئ. مراعاة النظیر، حسن تعلیل، لف او نشر، تلمیح، تضمین.')
Q(s,'7۔ آپ کو اس غزل میں دردؔ کا کون سا شعر پسند ہے اور کیوں؟','7. Which couplet of Dard in this ghazal do you like and why?','۷. تاسو ته پدې غزل کې د درد کوم شعر خوښ دی او ولې؟')
F.done()
s['sourceNote']='Printed page 167 (scan 174): “Mashq” title and questions 1–7 (question 1 has five fill-in items, each with a bracketed choice of three words printed at the left in blue; question 6 lists figures in blue). The right-hand choices in question 1(c) read “انسان، آدمی، فرشتے”.'+NOTE
s['vocabulary']={}
save(s)
# scan 175 = printed 168
s=page(175,'g03','168','Sheikh Ghulam Hamdani Mushafi (poet profile)','شیخ غلام ہمدانی مصحفی (شاعر کا تعارف)','شیخ غلام همداني مصحفي (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'شیخ غلام ہمدانی مصحفی','Sheikh Ghulam Hamdani Mushafi','شیخ غلام همداني مصحفي')
P(s,'پیدایش: ۱۷۵۱ء — وفات: ۱۸۴۴ء','Born: 1751 — Died: 1844','زېږېدنه: ۱۷۵۱ز — وفات: ۱۸۴۴ز')
P(s,'مصحفیؔ کی غزل دبستانِ دِلّی اور دبستانِ لکھنؤ کے دل آویز امتزاج کے ساتھ سامنے آتی ہے۔ اُن کی غزل میں ایک طرف دبستانِ دِلّی کا سوز و گداز ہے، تو دوسری جانب دبستانِ لکھنؤ کی پیکر تراشی کا رجحان بھی نظر آتا ہے۔','Mushafi’s ghazal comes forward with an attractive blend of the Delhi school and the Lucknow school. In his ghazal there is on one side the burning and melting quality of the Delhi school, and on the other the tendency to image-making of the Lucknow school is also seen.','د مصحفي غزل د دهلي دبستان او د لکهنو دبستان د زړه راکښونکي ګډوالي سره مخې ته راځي. د هغه په غزل کې یو لور د دهلي دبستان سوز او ګداز دی نو بل لور د لکهنو دبستان د پیکر ټراشلو رجحان هم ښکاري.')
P(s,'مصحفیؔ کا اُسلوب نہایت سلیس، بے حد سادہ اور تخلیقی نفاست کا حامل ہے۔ اُن کے لہجے میں ایک دھیما پن اور ٹھہراؤ ہے جو اُن کی غزل میں ایک طلسماتی فضا پیدا کرتا ہے۔ مصحفیؔ کو غزل پر ایک استادانہ کمال حاصل ہے۔ وہ پامال موضوعات کو بھی نئے انداز سے برتتے ہوئے اِن میں کوئی نہ کوئی جدّت کا پہلو پیدا کرتے ہیں۔ ان کے کئی ایک اشعار کو ضرب المثل کی حیثیّت حاصل ہے۔','Mushafi’s style is extremely fluent, very simple and bears creative refinement. In his tone there is a mildness and steadiness which creates a magical atmosphere in his ghazal. Mushafi has masterly perfection in the ghazal. Even in trodden themes, handling them in a new manner, he creates some aspect of novelty. Several of his couplets have the status of proverbs.','د مصحفي سټایل ډېر روان، ډېر ساده او تخلیقي نفاست لري. د هغه په لهجه کې یو ټیټ والی او ټینګ والی دی چې د هغه په غزل کې یوه طلسماتي فضا پیدا کوي. مصحفي ته په غزل کې استادانه کمال ترلاسه دی. هغه د پایمال شویو موضوعاتو ته هم په نوي انداز کارولو سره پکې کوم نه کوم نوښت پیدا کوي. د هغه ډېر شعرونه ضرب المثل حیثیت لري.')
P(s,'مولانا محمد حسین آزادؔ نے «آبِ حیات» میں لکھا ہے کہ «یہ اُصولِ فن سے بال برابر بھی سرکتے نہ تھے۔ کلام پر قدرتِ کامل پائی تھی۔ الفاظ کو پس و پیش اور مضمون کو کم و بیش کر کے اس در و بست سے شعر میں کھپاتے تھے کہ جو حقِ استادی کا ہے ادا ہو جاتا تھا»۔','Maulana Muhammad Husain Azad wrote in “Aab-e-Hayat” that “He did not budge a hair’s breadth from the principles of art. He had complete mastery over language. By rearranging words and increasing or decreasing the theme, he fitted them into the verse with such arrangement that the due of mastership was paid.”','مولانا محمد حسین آزاد په «آب حیات» کې لیکلي دي چې «دا د فن له اصولو نه د ویښتو په اندازه هم نه تښتېدل. په کلام یې بشپړ قدرت درلود. الفاظو ته وړاندې وروسته او مضمون ته لږ ډېر کولو سره یې په شعر کې داسې ځای کول چې د استادۍ حق ادا کېده».')
P(s,'مصحفیؔ کی غزلیات میں روانی اور جوانی پائی جاتی ہے۔ وہ صحتِ زبان کا بھی بہت خیال رکھتے تھے۔ ان کے اشعار میں ترنّم پایا جاتا ہے اور یہ کیفیّت موزوں اصوات کی تکرار سے پیدا ہوتی ہے۔','In Mushafi’s ghazals fluency and youthfulness are found. He also took great care of the correctness of language. In his verses melody is found and this quality arises from the repetition of suitable sounds.','د مصحفي په غزلونو کې روانۍ او ځوانۍ موندل کېږي. هغه د ژبې د صحت ډېر خیال هم ساتلو. د هغه په شعرونو کې ترنم موندل کېږي او دا کیفیت د موزونو غږونو له تکرار نه پیدا کېږي.')
F.done()
s['sourceNote']='Printed page 168 (scan 175): ornamental title “شیخ غلام ہمدانی مصحفی”, portrait (not reproduced), birth/death boxes (1751 and 1844), and the biography (the list of works is not on this page).'+NOTE
s['vocabulary']={}
save(s)
# scan 176 = printed 169
s=page(176,'g03','169','Ghazal (Mushafi): “Nagah chaman mein jab woh gul-andam aa gaya”','غزل (مصحفی): «ناگہ چمن میں جب وہ گل اندام آ گیا»','غزل (مصحفي): «ناڅاپه په ګلزار کې کله چې هغه ګل اندام راغی»','poem1')
F=Flow(s)
H(s,'غزل','Ghazal','غزل')
for r in [
('ناگہ چمن میں جب وہ گل اندام آ گیا','گل کو شکستِ رنگ کا پیغام آ گیا','When suddenly that rose-bodied one came into the garden,','the message of the defeat of colour came to the rose.','کله چې ناڅاپه په ګلزار کې هغه ګل اندام راغی','ګل ته د رنګ د ماتې پیغام راغی'),
('اٹھا جو صبحِ خواب سے وہ مست پُر خمار','خورشید گف کے بیچ لیے جام آ گیا','When that intoxicated, languorous one rose from sleep in the morning,','the sun came holding a goblet in his palm.','کله چې هغه مست پر خماره د سهار له خوب راپاڅېد','لمر په لاس کې جام نیولی راغی'),
('افسوس ہے کہ ہم تو رہے مستِ خوابِ صبح','اور آفتابِ عمر لبِ بام آ گیا','Alas that we remained drunk with the morning sleep,','and the sun of life came to the edge of the roof.','افسوس دی چې موږ د سهار په خوب مست پاتې شو','او د عمر لمر د بام په څنډه راغی'),
('ہے جائے رحم حال پہ یاں اُس اسیر کے','جو گرتے ہی ہوا سے تہِ دام آ گیا','There is cause for pity here for the state of that prisoner','who, falling from the air, at once came under the net.','دلته د هغه بندي په حال د رحم ځای دی','چې له هوا د لوېدو سره سم د جال لاندې راغی'),
('سمجھو خدا کے واسطے پیارے بُرا نہیں','دو دن، اگر کسی کے کوئی کام آ گیا','Understand, for God’s sake, dear, it is not bad','if for a couple of days one has been of use to someone.','پوه شئ د خدای لپاره ګرانه بد نه دی','دوه ورځې که چا ته څوک په کار راغی'),
('کر قطع کب گیا ترے کوچے سے مصحفیؔ؟','گر صبح کو گیا، وہیں پھر شام آ گیا','Did Mushafi ever give up your lane?','if he went in the morning, by evening he was back there.','ایا مصحفي ستا له کوڅې نه کله لاړ؟','که سهار لاړ نو هلته بیا ماښام راغی')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 169 (scan 176): title “غزل”, running head “شیخ غلام ہمدانی مصحفی”, and the ghazal “ناگہ چمن میں جب وہ گل اندام آ گیا” (five couplets in two-line form plus the closing couplet with the pen-name “مصحفی” centred).'+NOTE
s['vocabulary']={}
save(s)
