from enghelp import *
c=cell
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
# ---------- scan 63 (printed 54) ----------
U='u05'
s=page(63,U,'54','Reading Comprehension · Writing Suggestions · Oral Communication · Vocabulary and Grammar (start)','مطالعے کا فہم · لکھنے کی تجاویز · زبانی رابطہ · ذخیرۂ الفاظ اور قواعد (آغاز)','د لوست پوهه · د لیکلو وړاندیزونه · شفاهي اړیکه · لغت او ګرامر (پیل)','rc-exercises-1')
F=Flow(s)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions','درج ذیل سوالات کے جواب دیں','لاندې پوښتنو ته ځواب ورکړئ','eng11-u05-rc','exercise')
RQ=[('Analyze the text of ‘It’s Country For Me’ and give one example of fact and opinion each.','‘یہ میرے لیے ملک ہے’ کے متن کا تجزیہ کریں اور حقیقت اور رائے کی ایک ایک مثال دیں۔','د ‘دا زما لپاره هېواد دی’ متن تحلیل کړئ او د حقیقت او نظر هر یو یوه بېلګه ورکړئ.'),
('How coherence and cohesion is achieved in the essay ‘It’s Country For Me’. Illustrate with examples from the text.','مضمون ‘یہ میرے لیے ملک ہے’ میں ربط اور ہم آہنگی کیسے حاصل کی گئی ہے۔ متن سے مثالوں کے ساتھ واضح کریں۔','په مقاله ‘دا زما لپاره هېواد دی’ کې اړیکه او همغږي څنګه ترلاسه شوې ده. له متن څخه د مثالونو سره روښانه یې کړئ.'),
('Explain the significance of the title, ‘It’s Country For Me’ and its connection to the theme of the lesson.','سرخی ‘یہ میرے لیے ملک ہے’ کی اہمیت اور سبق کے مرکزی خیال سے اس کے تعلق کی وضاحت کریں۔','د سرلیک ‘دا زما لپاره هېواد دی’ اهمیت او د درس له مرکزي مفکورې سره د هغه اړیکه تشریح کړئ.'),
('Describe Joel’s treatment of ‘Lamby’, the orphaned lamb and Jessica the small dog; what does this show?','یتیم میمنے ‘لیمبی’ اور چھوٹی کتیا جیسیکا کے ساتھ جوئل کے سلوک کو بیان کریں؛ یہ کیا ظاہر کرتا ہے؟','د یتیم وري ‘لیمبي’ او کوچنۍ سپۍ جېسیکا سره د جوئل چلند بیان کړئ؛ دا څه ښيي؟'),
('Compare and contrast your daily routine with that of Joel’s. How would you rate the motivational level of your doing work with that of Joel’s?','اپنے روزمرہ معمول کا جوئل کے معمول سے موازنہ اور تضاد کریں۔ آپ اپنے کام کرنے کی ترغیب کی سطح کا جوئل کی سطح سے کیسے موازنہ کریں گے؟','خپل ورځنی معمول د جوئل له معمول سره پرتله کړئ او توپیر یې ښودل. تاسو به د خپل کار کولو د هڅونې کچه د جوئل له کچې سره څنګه پرتله کړئ؟'),
('What skills one is required to learn if he wants to be a full-fledged farmer?','اگر کوئی پورا کاشتکار بننا چاہتا ہو تو اسے کون سی مہارتیں سیکھنی ہوں گی؟','که څوک یو بشپړ بزګر کېدل غواړي نو کومې مهارتونه باید زده کړي؟'),
('In what way does Joel play the role of an adult?','جوئل کس طرح بالغ کا کردار ادا کرتا ہے؟','جوئل څنګه د یو بالغ رول لوبوي؟')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u05-rc','exercise')
H(s,'wsh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
add(s,'ws','Summarize the lesson ‘Its Country for Me’ in your own words.','سبق ‘یہ میرے لیے ملک ہے’ کا اپنے الفاظ میں خلاصہ لکھیں۔','د درس ‘دا زما لپاره هېواد دی’ لنډیز په خپلو کلمو ولیکئ.',tab='writing',role='question',exerciseId='eng11-u05-writing')
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'ot','Divide the class into groups of five students. Every student of the group should give oral recount, imaginary or factual, of his/her adventures on a trip to hilly or rural areas.','جماعت کو پانچ پانچ طلبہ کے گروہوں میں تقسیم کریں۔ گروہ کا ہر طالب علم پہاڑی یا دیہی علاقوں کے سفر پر اپنی مہمات کا زبانی بیان، خیالی یا حقیقی، دے۔','ټولګی په پنځو پنځو زده کوونکو ډلو وویشئ. د ډلې هر زده کوونکی دې د غرنیو یا کلیوالو سیمو په سفر کې د خپلو ماجراګانو شفاهي بیان، خیالي یا واقعي، ورکړي.',tab='language')
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'vi','Search the following words related to space science and astronomy in authentic source and then write the correct word in front of its meaning below.','خلائی سائنس اور فلکیات سے متعلق درج ذیل الفاظ مستند ذرائع میں تلاش کریں اور پھر نیچے ان کے معنی کے سامنے درست لفظ لکھیں۔','د فضايي ساینس او ستورپوهنې پورې اړوندې لاندې کلمې په معتبرو سرچینو کې ولټوئ او بیا د هغو د معنا مخې ته سمه کلمه ولیکئ.','eng11-u05-vocab','vocabulary')
add(s,'vw','orbit, dock, launch, countdown, lift-off, manned, splashdown, gravity','orbit، dock، launch، countdown، lift-off، manned، splashdown، gravity','orbit، dock، launch، countdown، lift-off، manned، splashdown، gravity',tab='vocabulary',sourceGap=dict(note='The eight words are printed on pink strips in two rows of four.'))
VQ=[('1. the beginning of a space flight ____________','1. خلائی پرواز کا آغاز ____________','1. د فضايي الوتنې پیل ____________'),('2. attach self to another space vehicle ____________','2. خود کو دوسری خلائی گاڑی سے جوڑنا ____________','2. ځان له بلې فضايي موټر سره نښلول ____________'),('3. counting to zero before launch ____________','3. لانچ سے پہلے صفر تک گنتی ____________','3. د لانچ دمخه تر صفر پورې شمېرنه ____________'),('4. going around a planet ____________','4. کسی سیارے کے گرد چکر لگانا ____________','4. د یوې سیارې شاوخوا ګرځېدل ____________')]
for i,(a,b,d) in enumerate(VQ,1): Qn(s,f'v{i}',a,b,d,'eng11-u05-vocab','vocabulary',**({'sourceGap':dict(note='Items 5–8 continue on the next page.')} if i==4 else {}))
F.done()
s['sourceNote']='Printed page 54. The right edge of the photograph clips the ends of lines in questions 1, 2, 3, 4, 5, 6 and in the vocabulary instruction (for example "fa[ct]", "Country F[or]", "i[ts]", "Jessic[a]", "woul[d]", "full-fledge[d]"); the words are read from context. "Not For Sale" is printed at the lower right beside the page number 54 (in a diamond). Border lines, pink corner flags and the watermark are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 64 (printed 55) ----------
s=page(64,U,'55','Vocabulary (end) · Grammar: articles · Teacher\'s Guideline','ذخیرۂ الفاظ (اختتام) · قواعد: حروفِ تعریف (آرٹیکلز) · استاد کی رہنمائی','لغت (پای) · ګرامر: مقالې · د ښوونکي لارښوونه','vocab-grammar-2')
F=Flow(s)
VQ=[('5. the force that all celestial bodies have ____________','5. وہ قوت جو تمام اجرامِ فلکی میں ہوتی ہے ____________','5. هغه ځواک چې ټول اسماني اجسام یې لري ____________'),('6. when the space vehicle leaves the surface ____________','6. جب خلائی گاڑی سطح چھوڑتی ہے ____________','6. کله چې فضايي موټر سطحه پرېږدي ____________'),('7. using astronauts, not computers or animals ____________','7. کمپیوٹر یا جانوروں کے بجائے خلا باز استعمال کرنا ____________','7. د کمپیوټرونو یا ځناورو پر ځای فضانوردان کارول ____________'),('8. landing in the sea ____________','8. سمندر میں اترنا ____________','8. په سمندر کې ښکته کېدل ____________')]
for i,(a,b,d) in enumerate(VQ,5): Qn(s,f'v{i}',a,b,d,'eng11-u05-vocab','vocabulary',**({'sourceGap':dict(note='Items 5–8 complete the vocabulary exercise of the previous page.')} if i==5 else {}))
H(s,'gr','GRAMMAR','قواعد','ګرامر',tab='grammar')
Qn(s,'ga','A. Fill in the article a, an or the where necessary. Choose X where no article is used.','الف. جہاں ضروری ہو حرفِ تعریف a، an یا the سے پُر کریں۔ جہاں کوئی آرٹیکل استعمال نہیں ہوتا وہاں X منتخب کریں۔','a. چېرته چې اړتیا وي مقاله a، an یا the ډکه کړئ. چېرته چې هېڅ مقاله نه کارېږي X وټاکئ.','eng11-u05-grammar','grammar')
GA=[('1. I like ____________ blue T-shirt over there better than ____________ red one.','1. مجھے وہاں والی ____________ نیلی ٹی شرٹ اس ____________ سرخ سے زیادہ پسند ہے۔','1. زه هغه ____________ شین ټي شرټ د هغه ____________ سور څخه ډېر خوښوم.'),('2. Their car does 150 miles ____________ hour.','2. ان کی گاڑی ____________ گھنٹے میں 150 میل چلتی ہے۔','2. د هغوی موټر ____________ ساعت کې 150 میله ځي.'),('3. Where’s ____________ USB drive I lent you last week?','3. وہ ____________ یو ایس بی ڈرائیو کہاں ہے جو میں نے پچھلے ہفتے آپ کو ادھار دی تھی؟','3. هغه ____________ USB ډرایو چېرته دی چې ما تېره اونۍ تاسو ته پور درکړی و؟'),('4. Do you still live in ____________ Bristol?','4. کیا آپ اب بھی ____________ برسٹل میں رہتے ہیں؟','4. ایا تاسو لا هم په ____________ بریسټل کې اوسېږئ؟'),('5. Is your mother working in ____________ old office building?','5. کیا آپ کی ماں ____________ پرانی دفتر کی عمارت میں کام کر رہی ہیں؟','5. ایا ستاسو مور په ____________ زړه دفتر ودانۍ کې کار کوي؟'),('6. Afsha’s father works as ____________ electrician.','6. افشاں کے والد ____________ الیکٹریشن کے طور پر کام کرتے ہیں۔','6. د افشا پلار د ____________ برېښنا‌کار په توګه کار کوي.'),('7. The tomatoes are Rs. 30 ____________ kilo.','7. ٹماٹر 30 روپے ____________ کلو ہیں۔','7. روميان 30 روپۍ ____________ کیلو دي.'),('8. What do you usually have for ____________ breakfast?','8. آپ عموماً ____________ ناشتے میں کیا کھاتے ہیں؟','8. تاسو معمولاً په ____________ سهارنۍ کې څه خورئ؟'),('9. Hashir has ____________ terrible headache.','9. ہاشر کو ____________ شدید سر درد ہے۔','9. هاشر ____________ سخت سردرد لري.'),('10. After this tour you have ____________ whole afternoon free to explore the city.','10. اس دورے کے بعد آپ کے پاس شہر کی سیر کے لیے ____________ پوری دوپہر خالی ہے۔','10. د دې سفر وروسته تاسو د ښار د سیل لپاره ____________ ټوله غرمه خالي لرئ.')]
for i,(a,b,d) in enumerate(GA,1): Qn(s,f'g{i}',a,b,d,'eng11-u05-grammar','grammar')
Qn(s,'gb','B. Fill in the blanks with the definite article the, if needed. Put an X if not needed.','ب. اگر ضرورت ہو تو خالی جگہوں کو definite article the سے پُر کریں۔ اگر ضرورت نہ ہو تو X لگائیں۔','b. که اړتیا وي تشې د ټاکلې مقالې the سره ډکې کړئ. که اړتیا نه وي X کېږدئ.','eng11-u05-grammar','grammar')
GB=[('1. My grandmother likes ____________ flowers very much.','1. میری دادی کو ____________ پھول بہت پسند ہیں۔','1. زما انا ____________ ګلان ډېر خوښوي.'),('2. I love ____________ flowers in your garden.','2. مجھے آپ کے باغ کے ____________ پھول بہت پسند ہیں۔','2. زه ستاسو په باغ کې ____________ ګلان ډېر خوښوم.'),('3. See you on ____________ Wednesday.','3. ____________ بدھ کو ملتے ہیں۔','3. ____________ چهارشنبه ګورو.'),('4. Zohaib goes to work by ____________ bus.','4. ذوہیب ____________ بس سے کام پر جاتا ہے۔','4. ذوهیب ____________ بس سره کار ته ځي.'),('5. Don’t be late for ____________ school.','5. ____________ اسکول کے لیے دیر نہ کریں۔','5. ____________ ښوونځي ته ناوخته مه کېږئ.'),('6. Listen! Kashaf is playing ____________ trumpet.','6. سنو! کشف ____________ ٹرمپیٹ بجا رہی ہے۔','6. واورئ! کشف ____________ ټرمپیټ غږوي.'),('7. We often see our cousins over ____________ Eid.','7. ہم اکثر ____________ عید پر اپنے کزنز کو دیکھتے ہیں۔','7. موږ ډېر ځله ____________ اختر پر خپل تره‌زامنو سره سره لیدو.'),('8. She has never been to ____________ Nathiagali before.','8. وہ پہلے کبھی ____________ نتھیاگلی نہیں گئی۔','8. هغه مخکې هېڅکله ____________ نتهیاګلي ته نه ده تللې.'),('9. What about going to Karachi in ____________ February?','9. ____________ فروری میں کراچی جانے کے بارے میں کیا خیال ہے؟','9. په ____________ فبرورۍ کې کراچۍ ته تلو په اړه څه فکر دی؟')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',a,b,d,'eng11-u05-grammar','grammar')
H(s,'tg','Teacher\'s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the use of articles.','طلبہ کو آرٹیکلز کے استعمال کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د مقالو کارول تشریح کړئ او بیا تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 55. Items 5–8 complete the vocabulary exercise of the previous page. In exercises A and B the instructions show the articles "a", "an", "the" in bold italic. A pink "Teacher\'s Guideline" banner ends the page. The page number 55 is printed in a diamond at the foot. Border lines, pink corner flags and the watermark are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 65 (printed 56) ----------
U='u06'
s=page(65,U,'56','Unit 6: Mother to Son · Learning outcomes','یونٹ 6: ماں کا بیٹے کے نام · سیکھنے کے نتائج','واحد 6: مور له زوی ته · د زده کړې پایلې','unit6-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 6','یونٹ 6','واحد 6')
H(s,'title','Mother to Son','ماں کا بیٹے کے نام','مور له زوی ته')
add(s,'au','Langston Hughes','لینگسٹن ہیوز','لانګسټن هیوز')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('use critical thinking to respond orally and in writing to the text (post-reading) to:','متن کا (پڑھنے کے بعد) زبانی اور تحریری جواب دینے کے لیے تنقیدی سوچ استعمال کریں تاکہ:','متن ته (له لوستلو وروسته) په شفاهي او لیکلي ډول د ځواب ورکولو لپاره انتقادي فکر وکاروي ترڅو:'),
('– give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read.','– پڑھے گئے متن کے نقطہ ہائے نظر / خیالات اور مسائل سے متعلق ذاتی رائے دیں اور اپنے موقف کا جواز پیش کریں۔','– د لوستل شوي متن د لیدلورو / نظرونو او مسایلو اړوند شخصي نظر ورکړي او خپل دریځ توجیه کړي.'),
('– relate what is read to his or her own feelings and experiences.','– جو پڑھا گیا اسے اپنے احساسات اور تجربات سے جوڑیں۔','– هغه څه چې لوستل شوي د خپلو احساساتو او تجربو سره وتړي.'),
('– scan to answer short questions.','– مختصر سوالات کے جواب دینے کے لیے سرسری نظر ڈالیں۔','– لنډو پوښتنو ځوابولو لپاره ګړندی کتنه وکړي.'),
('read a given poem and give orally and in writing:','دی گئی نظم پڑھیں اور زبانی اور تحریری طور پر پیش کریں:','ورکړل شوې نظم ولولئ او په شفاهي او لیکلي ډول وړاندې کړئ:'),
('– theme and its development.','– مرکزی خیال اور اس کی نشوونما۔','– مرکزي مفکوره او د هغې وده.'),
('– personal response with justification.','– جواز کے ساتھ ذاتی ردِعمل۔','– په توجیه سره شخصي غبرګون.'),
('recognize literary techniques such as personification and alliteration.','ادبی تکنیکوں جیسے تجسیم (شخصیت بخشی) اور حرفی تکرار (تجنیسِ صوتی) کو پہچانیں۔','ادبي تخنیکونه لکه شخصي کول او د غږ تکرار وپېژني.'),
('analyse how a writer/ poet uses language to:','تجزیہ کریں کہ ایک مصنف / شاعر زبان کو کیسے استعمال کرتا ہے تاکہ:','تحلیل کړي چې یو لیکوال / شاعر ژبه څنګه کاروي ترڅو:'),
('– appeal to the senses through use of figurative language including similes, metaphors and imagery','– تشبیہات، استعارات اور پیکر تراشی سمیت مجازی زبان کے استعمال سے حواس کو متاثر کریں','– د مجازي ژبې په کارولو سره حواسو ته اپیل وکړي په شمول د تشبیهاتو، استعارو او انځورګرۍ'),
('– set tone.','– لہجہ / فضا قائم کریں۔','– لهجه / فضا جوړه کړي.'),
('develop focus for own writing by identifying audience and purpose.','سامعین اور مقصد کی نشاندہی کر کے اپنی تحریر کے لیے توجہ پیدا کریں۔','د لیدونکو او موخې په پېژندلو سره د خپلې لیکنې لپاره تمرکز رامنځته کړي.'),
('demonstrate heightened awareness of conventions and dynamics of group discussion and interaction to:','گروہی بحث اور تعامل کے اصولوں اور حرکیات سے بلند آگاہی کا مظاہرہ کریں تاکہ:','د ډله‌ییزې بحث او اړیکې د دودونو او حرکیاتو لوړ پوهاوی وښيي ترڅو:'),
('– present and explain ones point of view clearly','– اپنے نقطۂ نظر کو واضح طور پر پیش اور بیان کریں','– خپل لیدلوری په روښانه ډول وړاندې او تشریح کړي'),
('– support or modified one’s opinion with reasons','– دلائل کے ساتھ اپنی رائے کی تائید کریں یا اسے تبدیل کریں','– خپل نظر په دلایلو سره ملاتړ یا بدل کړي'),
('– acknowledge other’s contribution','– دوسروں کی شراکت کو تسلیم کریں','– د نورو ونډه ومني'),
('– share information and ideas','– معلومات اور خیالات کا اشتراک کریں','– معلومات او نظرونه شریک کړي'),
('– clarify, rephrase, explain, expand and restate information and ideas.','– معلومات اور خیالات کی وضاحت کریں، دوبارہ بیان کریں، تشریح کریں، وسعت دیں اور دہرائیں۔','– معلومات او نظرونه روښانه کړي، بیا ووايي، تشریح کړي، پراخ کړي او بیا تکرار کړي.'),
('illustrate the use and all functions of modal verbs.','معاون افعال (موڈل ورب) کے استعمال اور تمام افعال کی مثال دیں۔','د موډل فعلونو کارول او ټولې دندې وښيي.'),
('use various reference sources to refine vocabulary for interpersonal academic workplace situation including figurative, idiomatic and technical vocabulary.','باہمی، تعلیمی اور کام کی جگہ کی صورتحال کے لیے مجازی، محاوراتی اور فنی ذخیرۂ الفاظ سمیت ذخیرۂ الفاظ کو نکھارنے کے لیے مختلف حوالہ جاتی ذرائع استعمال کریں۔','د شخصي، تعلیمي او د کار ځای حالت لپاره لغت ښه کولو لپاره بېلابېلې حوالې سرچینې وکاروي په شمول د مجازي، محاوراتي او تخنیکي لغت.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 56: Unit 6 opening page with the unit number, the title banner "Mother to Son", the author tag "Langston Hughes" (the right edge of the photograph clips the last letters of the tag and of some outcome lines) and the list of learning outcomes. The page number 56 is printed in a diamond at the foot. Border lines, pink corner flags and the watermark are excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 66 (printed 57) ----------
s=page(66,U,'57','Mother to Son (poem)','ماں کا بیٹے کے نام (نظم)','مور له زوی ته (نظم)','poem')
F=Flow(s)
add(s,'h','Mother to Son','ماں کا بیٹے کے نام','مور له زوی ته',kind='heading')
add(s,'s1','Well, son, I’ll tell you:\nLife for me ain’t been no crystal stair.\nIt’s had tacks in it,\nAnd splinters,\nAnd boards torn up,\nAnd places with no carpet on the floor—\nBare.\nBut all the time\nI’se been a-climbin’ on,\nAnd reachin’ landin’s,\nAnd turnin’ corners,\nAnd sometimes goin’ in the dark\nWhere there ain’t been no light.\nSo boy, don’t you turn back.\nDon’t you set down on the steps\n’Cause you finds it’s kinder hard.\nDon’t you fall now—\nFor I’se still goin’, honey,\nI’se still climbin’,\nAnd life for me ain’t been no crystal stair.','ٹھیک ہے، بیٹے، میں تمہیں بتاتی ہوں:\nمیرے لیے زندگی بلّور کی سیڑھی نہیں رہی۔\nاس میں کیلیں رہی ہیں،\nاور کرچیاں،\nاور اکھڑے ہوئے تختے،\nاور ایسی جگہیں جہاں فرش پر قالین نہیں—\nننگا۔\nلیکن ہر وقت\nمیں چڑھتی ہی رہی ہوں،\nاور پڑاؤ تک پہنچتی رہی ہوں،\nاور موڑ مڑتی رہی ہوں،\nاور کبھی کبھی اندھیرے میں جاتی رہی ہوں\nجہاں کوئی روشنی نہیں رہی۔\nتو بیٹے، پیچھے مت مڑنا۔\nسیڑھیوں پر مت بیٹھ جانا\nکیونکہ تمہیں یہ کچھ سخت لگتا ہے۔\nاب گِر مت جانا—\nکیونکہ میں اب بھی جا رہی ہوں، پیارے،\nمیں اب بھی چڑھ رہی ہوں،\nاور میرے لیے زندگی بلّور کی سیڑھی نہیں رہی۔','ښه، زویه، زه به تا ته ووایم:\nزما لپاره ژوند د کرستالو زینه نه دی وی.\nپه هغې کې میخونه وو،\nاو ټوټې،\nاو پورته شوي تختې،\nاو داسې ځایونه چې پر فرش قالین نه و—\nبرېښ.\nخو تل\nزه پورته خېژېدلې،\nاو پړاوونو ته رسېدلې،\nاو کونجونه ګرځېدلې،\nاو کله ناکله په تیارو کې تللې\nچېرته چې هېڅ رڼا نه وه.\nنو هلکه، شاته مه ګرځه.\nپر زینو مه کېنه\nځکه چې ته یې یو څه سخت مومې.\nاوس مه غورځېږه—\nځکه چې زه لا هم ځم، ګرانه،\nزه لا هم خېژم،\nاو زما لپاره ژوند د کرستالو زینه نه دی وی.',listType='poem')
add(s,'at','Langston Hughes','لینگسٹن ہیوز','لانګسټن هیوز')
add(s,'n','A black-and-white photograph of a dark figure and light vertical bands (a staircase or railing) fills the lower part of the page; it is not reproduced.','نچلے حصے میں سیاہ و سفید تصویر ہے جس میں ایک تاریک شکل اور روشن عمودی پٹیاں (سیڑھی یا جنگلا) دکھائی دیتی ہیں؛ یہ تصویر نقل نہیں کی گئی۔','په ښکتنۍ برخه کې توروسپین انځور دی چې تیاره شکل او روښانه عمودي پټۍ (زینه یا کتاره) ښيي؛ دا انځور نه دی رانقل شوی.')
F.done()
s['sourceNote']='Printed page 57: the poem "Mother to Son" (20 lines) by Langston Hughes (1922; public domain), in the dialect printed ("ain’t", "I’se", "a-climbin’", "goin’"). The author name is printed below the poem in bold red. A black-and-white photograph fills the foot of the page. The page number 57 is printed in a diamond at the foot. Border lines, pink corner flags and the watermark are excluded; a partial footer at the bottom edge is excluded.'
s['vocabulary']={}
save(s)
