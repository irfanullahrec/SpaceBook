from enghelp import *
c=cell
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def Op(s,key,en,ur,ps,ex,tab='grammar',**m): add(s,key,en,ur,ps,role='option',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
OPT={'quality':('adjective of quality','صفتِ کیفیت (adjective of quality)','د کیفیت صفت (adjective of quality)'),
'quantity':('adjective of quantity','صفتِ مقدار (adjective of quantity)','د مقدار صفت (adjective of quantity)'),
'number':('adjective of number','صفتِ عدد (adjective of number)','د شمېر صفت (adjective of number)'),
'numeral':('numeral adjective','عددی صفت (numeral adjective)','عددي صفت (numeral adjective)'),
'distributive':('distributive adjective','تقسیمی صفت (distributive adjective)','تقسیمي صفت (distributive adjective)'),
'demonstrative':('demonstrative adjective','اشاراتی صفت (demonstrative adjective)','اشاره‌ییزه صفت (demonstrative adjective)')}
def opts(s,prefix,kinds,ex):
    for k in kinds:
        e,u,p=OPT[k]; Op(s,f'{prefix}{k[0:4]}',e,u,p,ex)
VEX='eng11-u14-vocab'; GEX='eng11-u14-grammar'
# ---------- scan 143 (printed 134) ----------
s=page(143,'u14','134','Vocabulary exercise (end) · Grammar: adjectives (A, 1–4)','ذخیرۂ الفاظ کی مشق (اختتام) · قواعد: صفات (الف، 1–4)','د لغت تمرین (پای) · ګرامر: صفتونه (الف، ۱–۴)','vocab-adjectives-1')
F=Flow(s)
VQ=[('Your uncle was so happy about his new model car that he had finished but his wife turned round and really ______ saying it was just a toy for kids.','آپ کے چچا اپنی نئی ماڈل کار سے اتنے خوش تھے کہ وہ بس ختم کر چکے تھے لیکن ان کی بیوی مڑی اور واقعی ______ یہ کہتے ہوئے کہ یہ تو بچوں کا کھلونا ہے۔','ستاسو تره د خپل نوي ماډل موټر په اړه دومره خوشاله و چې هغه پای ته رسولی و خو د هغه ښځې وګرځېده او رښتیا ______ ویل یې چې دا یوازې د ماشومانو لوبو ده.'),
('It was only five miles to the next hostel but we ______ of it due to the weight of the packs and took nearly three hours to get there.','اگلے ہاسٹل تک صرف پانچ میل تھے لیکن ہم نے تھیلوں کے وزن کی وجہ سے ______ اور وہاں پہنچنے میں تقریباً تین گھنٹے لگ گئے۔','بل هاسټل ته یوازې پنځه میله وو خو موږ د بارونو د وزن له امله ______ او هلته ورسېدو تقریباً درې ساعته ونیول.'),
('I never knew about the chance of a new job at all. I only ______ from Sania who had overheard the managers talking at lunch in the staff canteen.','مجھے نئی نوکری کے موقع کے بارے میں بالکل پتا نہیں تھا۔ میں نے صرف ثانیہ سے ______ جس نے اسٹاف کینٹین میں لنچ پر مینیجرز کو بات کرتے سن لیا تھا۔','ما د نوې دندې د فرصت په اړه هېڅ نه پوهېدم. ما یوازې له ثانیې ______ چې په کارمندانو کنټین کې په غرمه کې یې د مدیرانو خبرې اورېدلې وې.'),
('Samia always ______ a real dreamer who finds it difficult to accept the mundane in life. She is a typical teenager!','سامیہ ہمیشہ ______ ایک حقیقی خواب دیکھنے والی جسے زندگی کی عام باتیں قبول کرنا مشکل لگتا ہے۔ وہ ایک عام نوجوان لڑکی ہے!','سمیعه تل ______ یوه رښتینې خوبګره چې د ژوند عام شیان منل ورته ستونزمن دي. هغه یوه عادي ځوانه نجلۍ ده!')]
for i,(a,b,d) in enumerate(VQ,9): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',VEX,'vocabulary')
H(s,'gr','Grammar','قواعد','ګرامر',tab='grammar')
H(s,'gt','Adjectives and Adjective Phrases and Clauses','صفات اور صفتی فقرے اور جملے','صفتونه او صفتي عبارتونه او جملې',tab='grammar')
Qn(s,'ga','A. Identify the adjectives in the following sentences and state their kind.','الف. درج ذیل جملوں میں صفات کی شناخت کریں اور ان کی قسم بتائیں۔','الف. په لاندې جملو کې صفتونه وپېژنئ او د هغو ډول ووایئ.',GEX,'grammar')
AQ=[('Karachi is a big city. Here big is an ______','کراچی ایک بڑا شہر ہے۔ یہاں big ایک ______ ہے','کراچي یو لوی ښار دی. دلته big یو ______ دی',['quality','quantity','number']),
('She ate some rice. Here some is an ______','اس نے کچھ چاول کھائے۔ یہاں some ایک ______ ہے','هغې یو څه وريجې وخوړلې. دلته some یو ______ دی',['quality','quantity','number']),
('The foolish crow opened his mouth to sing. Here foolish is an ______','بے وقوف کوے نے گانے کے لیے منہ کھولا۔ یہاں foolish ایک ______ ہے','نادانه کارغه د سندرې ویلو لپاره خپله خوله خلاصه کړه. دلته foolish یو ______ دی',['quality','quantity','number']),
('He has little patience. Here little is an ______','اس میں صبر کم ہے۔ یہاں little ایک ______ ہے','هغه لږ صبر لري. دلته little یو ______ دی',['quality'])]
for i,(a,b,d,ks) in enumerate(AQ,1):
    Qn(s,f'a{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
    for k in ks: Op(s,f'a{i}{k[:4]}',OPT[k][0],OPT[k][1],OPT[k][2],GEX)
F.done()
s['sourceNote']='Printed page 134. The page begins with items 9–12 of the vocabulary exercise, followed by "Grammar", the heading "Adjectives and Adjective Phrases and Clauses" and Part A items 1–4, each with a printed dotted blank and three bullet options (adjective of quality / quantity / number); item 4 continues on the next page. The printed text of item 9 breaks across lines after "finished"; kept as printed. The upper-left corner is cut off at the page edge. Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 134 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 144 (printed 135) ----------
s=page(144,'u14','135','Grammar: adjectives (A, 4–10)','قواعد: صفات (الف، 4–10)','ګرامر: صفتونه (الف، ۴–۱۰)','adjectives-2')
F=Flow(s)
Op(s,'a4quan','adjective of quantity','صفتِ مقدار (adjective of quantity)','د مقدار صفت (adjective of quantity)',GEX,sourceGap=dict(note='Continues item 4 of the previous page ("He has little patience. Here little is an ___ — adjective of quality / quantity / number").'))
Op(s,'a4numb','adjective of number','صفتِ عدد (adjective of number)','د شمېر صفت (adjective of number)',GEX)
AQ=[(5,'He has lost all of his wealth. Here all is an ______','اس نے اپنی ساری دولت کھو دی۔ یہاں all ایک ______ ہے','هغه خپله ټوله شتمني له لاسه ورکړه. دلته all یو ______ دی',['quality','quantity','number']),
(6,'We did not receive sufficient rain this year. Here sufficient is an ______','اس سال ہمیں کافی بارش نہیں ہوئی۔ یہاں sufficient ایک ______ ہے','پدې کال موږ کافي باران ونه موند. دلته sufficient یو ______ دی',['quality','quantity','number']),
(7,'Each hand has five fingers. Here five is an ______','ہر ہاتھ میں پانچ انگلیاں ہیں۔ یہاں five ایک ______ ہے','هر لاس پنځه ګوتې لري. دلته five یو ______ دی',['quality','quantity','number']),
(8,'There are several mistakes in your composition. Here several is an ______','آپ کی تحریر میں کئی غلطیاں ہیں۔ یہاں several ایک ______ ہے','ستاسو په لیکنه کې څو غلطۍ شته. دلته several یو ______ دی',['quality','quantity','number']),
(9,'January is the first month of the year. Here the first is an ______','جنوری سال کا پہلا مہینہ ہے۔ یہاں the first ایک ______ ہے','جنوري د کال لومړۍ میاشت ده. دلته the first یو ______ دی',['quality','quantity','number']),
(10,'Our country expects every citizen to do their duty. Here every is a ______','ہمارا ملک ہر شہری سے توقع کرتا ہے کہ وہ اپنا فرض ادا کرے۔ یہاں every ایک ______ ہے','زموږ هېواد له هر اوسېدونکي تمه لري چې خپله دنده ترسره کړي. دلته every یو ______ دی',['numeral'])]
for n,a,b,d,ks in AQ:
    Qn(s,f'a{n}',f'{n}. {a}',f'{n}. {b}',f'{n}. {d}',GEX,'grammar')
    for k in ks: Op(s,f'a{n}{k[:4]}',OPT[k][0],OPT[k][1],OPT[k][2],GEX)
F.done()
s['sourceNote']='Printed page 135. The first two options complete item 4 of the previous page. Items 5–9 each have three bullet options (quality / quantity / number); item 10 begins with "numeral adjective" and its options (numeral / distributive / demonstrative) continue on the next page. The left edge of the scan is partly covered by the page shadow. Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 135 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 145 (printed 136) ----------
s=page(145,'u14','136','Grammar: adjectives (A end, B) · Teacher\'s Guideline','قواعد: صفات (الف کا اختتام، ب) · استاد کی رہنمائی','ګرامر: صفتونه (الف پای، ب) · د ښوونکي لارښوونه','adjectives-3')
F=Flow(s)
for k in ['distributive','demonstrative']: Op(s,f'a10{k[:4]}',OPT[k][0],OPT[k][1],OPT[k][2],GEX,sourceGap=dict(note='Continues item 10 of the previous page ("Our country expects every citizen to do their duty. Here every is a ___ — numeral / distributive / demonstrative adjective").') if k=='distributive' else {})
AQ=[(11,'Neither accusation is true. Here neither is a ______','دونوں الزامات میں سے کوئی سچ نہیں۔ یہاں neither ایک ______ ہے','هیڅ یو تور هم رښتیا نه دی. دلته neither یو ______ دی'),
(12,'Those apples are ripe. Here those is a ______','وہ سیب پکے ہوئے ہیں۔ یہاں those ایک ______ ہے','هغه مڼې پخې دي. دلته those یو ______ دی')]
for n,a,b,d in AQ:
    Qn(s,f'a{n}',f'{n}. {a}',f'{n}. {b}',f'{n}. {d}',GEX,'grammar')
    for k in ['numeral','distributive','demonstrative']: Op(s,f'a{n}{k[:4]}',OPT[k][0],OPT[k][1],OPT[k][2],GEX)
Qn(s,'gb','B. Determine which form of the adjective best completes each of the following sentences.','ب. فیصلہ کریں کہ صفت کی کون سی شکل درج ذیل جملوں میں سے ہر ایک کو بہترین طور پر مکمل کرتی ہے۔','ب. پرېکړه وکړئ چې د صفت کومه بڼه لاندې هره جمله په غوره ډول بشپړوي.',GEX,'grammar')
GB=[('Her (most high, highest) score at bowling was 200.','بولنگ میں اس کا (most high, highest) اسکور 200 تھا۔','په بولینګ کې د هغې (most high, highest) سکور ۲۰۰ و.'),
('It goes without saying that Nasir’s hand was (larger, more large) than mine.','یہ کہے بغیر ظاہر ہے کہ ناصر کا ہاتھ میرے ہاتھ سے (larger, more large) تھا۔','ویل ضروري نه دي چې د ناصر لاس زما له لاس (larger, more large) و.'),
('Maheen was (more good, better) than Abrar at solving riddles.','ماہین پہیلیاں حل کرنے میں ابرار سے (more good, better) تھی۔','ماهین په معما حلولو کې له ابرار (more good, better) وه.'),
('This test tube of water is definitely (clearer, clearest) than the other.','پانی کی یہ ٹیسٹ ٹیوب دوسری سے یقیناً (clearer, clearest) ہے۔','دا د اوبو آزموینه ټیوب له بل څخه یقیناً (clearer, clearest) دی.'),
('Tomorrow’s weather should be (coolest, cooler) than today’s.','کل کا موسم آج کے موسم سے (coolest, cooler) ہونا چاہیے۔','د سبا هوا باید له نن څخه (coolest, cooler) وي.'),
('Compared to Nadia’s cats, mine is hardly the (slimmest, slimmer).','نادیہ کی بلیوں کے مقابلے میں میری بلی شاید ہی (slimmest, slimmer) ہو۔','د نادیې له پیشوګانو سره پرتله، زما یوه په سختۍ (slimmest, slimmer) ده.')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the use of adjectives and degrees of adjectives.','طلبہ کو صفات اور صفات کے درجات کے استعمال کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د صفتونو او د صفتونو د درجو کارول تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 136. The first two options complete item 10 of the previous page; then items 11 and 12 (options: numeral / distributive / demonstrative adjective), Part B (six items with the choices in parentheses) and the pink "Teacher\'s Guideline" banner (partly smudged). Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 136 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 146 (printed 137) ----------
s=page(146,'u15','137','Unit 15: University Days · Learning outcomes','یونٹ 15: یونیورسٹی کے دن · سیکھنے کے نتائج','واحد 15: د پوهنتون ورځې · د زده کړې پایلې','unit15-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 15','یونٹ 15','واحد 15')
H(s,'title','University Days','یونیورسٹی کے دن','د پوهنتون ورځې')
add(s,'au','James Thurber','جیمز تھربر','جیمز ترېبر')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('analyze passages in the text to identify the theme/ general subject, key idea/ central thought (a statement about the general subject), and supporting details.','متن کے اقتباسات کا تجزیہ کر کے موضوع/عمومی مضمون، کلیدی خیال/مرکزی فکر (عمومی موضوع کے بارے میں ایک بیان) اور معاون تفصیلات کی نشاندہی کریں۔','د متن برخې تحلیل کړي ترڅو موضوع/عمومي مضمون، کلیدي مفکوره/مرکزي فکر (د عمومي موضوع په اړه یو بیان) او ملاتړي جزئیات وپېژني.'),
('recognize that the theme of a text is carried in a thesis statement.','پہچانیں کہ متن کا موضوع ایک مرکزی دعوے (تھیسس اسٹیٹمنٹ) میں ہوتا ہے۔','وپېژني چې د متن موضوع په مرکزي ادعا (تیسس) کې وي.'),
('apply critical thinking to interact with text, use intensive reading strategies (while-reading) to:','متن سے تعامل کے لیے تنقیدی سوچ کو بروئے کار لائیں، گہرے مطالعے کی حکمتِ عملیاں (پڑھتے وقت) استعمال کریں تاکہ:','له متن سره د اړیکې لپاره انتقادي فکر پلي کړي، د ژورې لوست ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو:'),
('• scan to answer short questions.','• مختصر سوالات کے جواب کے لیے سرسری نظر ڈالیں (اسکین کریں)۔','• د لنډو پوښتنو د ځواب لپاره سکین وکړي.'),
('• make simple inferences using context of the text and prior knowledge.','• متن کے سیاق اور پیشگی علم سے سادہ نتائج اخذ کریں۔','• د متن د شرایطو او مخکني پوهې په کارولو ساده پایلې واخلي.'),
('• distinguish between what is clearly stated and what is implied.','• جو واضح طور پر بیان کیا گیا ہے اور جو ضمنی ہے ان میں فرق کریں۔','• د هغه څه چې په روښانه ډول بیان شوي او هغه چې ضمني دي ترمنځ توپیر وکړي.'),
('• comprehend/interpret text by applying critical thinking.','• تنقیدی سوچ کو بروئے کار لا کر متن کو سمجھیں/اس کی تشریح کریں۔','• د انتقادي فکر په پلي کولو سره متن وپوهېږي/تفسیر یې کړي.'),
('analyze an essay to identify the general subject, main idea (a statement about the general subject), key ideas, supporting details.','مضمون کا تجزیہ کر کے عمومی موضوع، مرکزی خیال (عمومی موضوع کے بارے میں ایک بیان)، کلیدی خیالات اور معاون تفصیلات کی نشاندہی کریں۔','یوه مقاله تحلیل کړي ترڅو عمومي موضوع، اصلي مفکوره (د عمومي موضوع په اړه یو بیان)، کلیدي مفکورې او ملاتړي جزئیات وپېژني.'),
('analyze paragraphs to identify sentences that support the main idea through facts, analogies, anecdotes and quotations.','پیراگرافوں کا تجزیہ کر کے ایسے جملوں کی نشاندہی کریں جو حقائق، تمثیلوں، حکایات اور اقتباسات کے ذریعے مرکزی خیال کی تائید کرتے ہیں۔','پاراګرافونه تحلیل کړي ترڅو هغه جملې وپېژني چې په حقایقو، تمثیلونو، حکایتونو او نقل‌قولونو اصلي مفکوره ملاتړ کوي.'),
('write an extended narrative incident:','ایک طویل بیانیہ واقعہ لکھیں:','یو اوږد بیانیه پېښه ولیکي:'),
('• include action, spoken words, observations, thoughts, and feelings.','• عمل، بولے گئے الفاظ، مشاہدات، خیالات اور احساسات شامل کریں۔','• عمل، ویل شوي الفاظ، مشاهدې، فکرونه او احساسات شامل کړي.'),
('• use concrete sensory details to describe and support impressions of people, places, things or experiences.','• لوگوں، جگہوں، چیزوں یا تجربات کے تاثرات کی وضاحت اور تائید کے لیے ٹھوس حسی تفصیلات استعمال کریں۔','• د خلکو، ځایونو، شیانو یا تجربو د تاثراتو د تشریح او ملاتړ لپاره کانکریټ حسي جزئیات وکاروي.'),
('• give a proper beginning, middle and end to the narrative.','• بیانیے کو مناسب آغاز، درمیان اور اختتام دیں۔','• بیانیې ته مناسب پیل، منځ او پای ورکړي.'),
('• express and show gratitude, apology, anger and impatience in oral communication.','• زبانی گفتگو میں شکرگزاری، معذرت، غصہ اور بے صبری کا اظہار کریں اور دکھائیں۔','• په شفاهي اړیکه کې مننه، بخښنه، غوسه او بې‌صبري څرګنده کړي او وښيي.'),
('use appropriate vocabulary and correct spelling in their own writing.','اپنی تحریر میں موزوں ذخیرۂ الفاظ اور درست املا استعمال کریں۔','په خپله لیکنه کې مناسب لغت او سمه املا وکاروي.'),
('follow order of adjectives in sentences.','جملوں میں صفات کی ترتیب کی پیروی کریں۔','په جملو کې د صفتونو د ترتیب پیروي وکړي.'),
('Identify and use adjective phrases and clauses','صفتی فقروں اور جملوں کی شناخت کریں اور استعمال کریں','صفتي عبارتونه او جملې وپېژني او وکاروي')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 137: Unit 15 opening page with the unit number, the title banner "University Days", the author tag "James Thurber" and the learning outcomes with nested bullets (printed bullets "•" shown in the text of sub-items). The last line is printed without a final full stop. Border lines, pink corner flags, the watermark and the phone-number strip are excluded. The page number 137 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
