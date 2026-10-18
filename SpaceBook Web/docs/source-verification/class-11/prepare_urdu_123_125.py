from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n01',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Poem couplets: the two printed lines are stored with a line break.'
# scan 123 = printed 116
s=page(123,'n01','116','Exercise (Mashq) on Hamd; box on Nazm','مشق: «حمد» پر سوالات؛ نظم','تمرین: «حمد» پوښتنې؛ نظم','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ «یہ سب آیاتِ الٰہی ہیں، ذرا غور سے دیکھ»۔ حمد کے اشعار کے پس منظر میں اس مصرعے کی وضاحت کریں۔','1. “All these are the signs of God; look carefully.” In the background of the couplets of the Hamd, explain this line.','۱. «دا ټول د الله آیتونه دي، لږ په غور وګوره». د حمد د شعرونو په شاليد دغه مصرع تشریح کړئ.')
Q(s,'2۔ اس حمد میں اللہ تعالیٰ کی جن صفات کا ذکر کیا گیا ہے، اُنھیں اپنے الفاظ میں لکھیں۔','2. Write in your own words the attributes of Allah the Exalted mentioned in this Hamd.','۲. پدې حمد کې د الله تعالیٰ د کومو صفتونو یادونه شوې ده هغه په خپلو الفاظو ولیکئ.')
Q(s,'3۔ حمد کی تعریف کریں۔ اس حمد کے علاوہ کوئی سے تین حمدیہ اشعار تحریر کریں۔','3. Define Hamd. Besides this Hamd, write any three couplets of Hamd.','۳. د حمد تعریف وکړئ. له دې حمد نه سر بېره کوم درې حمدیه شعرونه ولیکئ.')
Q(s,'4۔ قواعد کے حوالے سے جملے دُرست کریں۔','4. Correct the sentences with regard to grammar.','۴. د قواعدو په اړه جملې سمې کړئ.')
for t in [('• یا کھانا کھاؤ یا چائے پیو۔','• Either eat food or drink tea.','• یا ډوډۍ وخورئ یا چای وڅښئ.'),
('• اے لوگو! میری بات سنو۔','• O people! Listen to what I say.','• ای خلکو! زما خبره واورئ.'),
('• وہ ہنستا ہوا بولا۔','• He spoke laughing.','• هغه خندا کولو سره وویل.'),
('• جب میں لاہور پہنچ جاؤں گا تمھیں خط لکھوں گا۔','• When I reach Lahore I shall write you a letter.','• کله چې زه لاهور ته ورسېږم تاسو ته به خط ولیکم.'),
('• میں نے در حقیقت میں اُسے تمام صورتِ حال بتا دی۔','• I in reality told him the whole situation.','• ما په حقیقت کې هغه ته ټوله حالت وویل.')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-4')
Q(s,'5۔ اس حمد کے قوافی لکھیں۔','5. Write the rhymes (qawafi) of this Hamd.','۵. د دې حمد قافیې ولیکئ.')
Q(s,'6۔ حمد کا خلاصہ اپنے الفاظ میں لکھیں۔','6. Write the summary of the Hamd in your own words.','۶. د حمد لنډیز په خپلو الفاظو ولیکئ.')
H(s,'نظم:','Nazm:','نظم:')
P(s,'۱۔ نظم کے لفظی معنی ہیں «پرونا» جیسے موتی لڑی میں پروئے جاتے ہیں۔ ادب کی رُو سے اشعار کے مجموعے کو نظم کہتے ہیں۔','1. The literal meaning of “nazm” is “to string”, as pearls are strung in a thread. In literature a collection of verses is called nazm.','۱. د نظم لفظي معنا «پرول» ده لکه څنګه چې مرواریدونه په لړۍ کې پېل کېږي. د ادب له مخې د شعرونو ټولګې ته نظم وايي.',boxed=True)
P(s,'۲۔ «کسی ایک خیال یا موضوع کے تحت لکھے گئے اشعار کو نظم کہتے ہیں»۔','2. “Verses written under a single idea or subject are called nazm.”','۲. «د کوم یو خیال یا موضوع لاندې لیکل شوي شعرونو ته نظم وايي».',boxed=True)
H(s,'پابند نظم:','Pabandi nazm (metrical poem):','پابند نظم:')
P(s,'اس نظم میں وزن اور بحر کے ساتھ ساتھ قافیہ اور بسا اوقات ردیف کی پابندی بھی ضروری ہوتی ہے۔','In this nazm, along with metre and bahr, the observance of rhyme and often radif too is necessary.','پدې نظم کې د وزن او بحر سره سره د قافیې او ډېر وختونه د ردیف پابندي هم ضروري وي.',boxed=True)
F.done()
s['sourceNote']='Printed page 116 (scan 123): “Mashq” title, questions 1–6 (question 4 has five bulleted sentences in blue to be corrected) and the blue box on “نظم” and “پابند نظم”. The printed 5th bullet reads “میں نے در حقیقت میں اُسے…” as given.'+NOTE
s['vocabulary']={}
save(s)
# scan 124 = printed 117
s=page(124,'n02','117','Mohsin Kakorvi (poet profile)','محسن کاکوروی (شاعر کا تعارف)','محسن کاکوروي (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'محسن کاکوروی','Mohsin Kakorvi','محسن کاکوروي')
P(s,'پیدایش: ۱۸۲۶ء — وفات: ۱۹۰۵ء','Born: 1826 — Died: 1905','زېږېدنه: ۱۸۲۶ز — وفات: ۱۹۰۵ز')
P(s,'نام محمد محسنؔ اور محسنؔ ہی اُن کا تخلص تھا۔ لکھنؤ کے ایک قصبے کاکوری میں پیدا ہوئے۔ علومِ متداولہ کے حصول کے بعد انگریزی تعلیم حاصل کی اور عدالتی کاموں میں مشغول ہو گئے۔ بعد ازاں وکالت کا امتحان پاس کیا اور آگرے میں پریکٹس کرتے رہے۔','His name was Muhammad Mohsin and “Mohsin” was his pen-name. He was born in Kakori, a town near Lucknow. After acquiring the current sciences he received an English education and became engaged in court work. Later he passed the law examination and kept practising in Agra.','نوم یې محمد محسن او محسن یې تخلص و. د لکهنو په یوه ښارګوټي کاکوري کې زېږېدلی دی. د متداولو علومو له ترلاسه کولو وروسته یې انګلیسي زده‌کړه وکړه او په عدالتي کارونو بوخت شو. وروسته یې د وکالت امتحان تېر کړ او په اګره کې یې وکالت کاوه.')
P(s,'روایت ہے کہ محسنؔ نو سال کے تھے کہ اُنھیں خواب میں حضرت محمد رسول اللہ خاتم النبیین (ﷺ) کی زیارت نصیب ہوئی، جس پر اظہارِ مسرّت کے طور پر اُنھوں نے ایک فارسی نظم لکھی۔ محسن کاکوروی کا زیادہ تر کلام حمدیہ اور نعتیہ ہے۔ ان کی وجۂ شہرت بھی ان کا نعتیہ کلام ہے۔','It is related that when Mohsin was nine years old he was blessed in a dream with the vision of Hazrat Muhammad, Messenger of Allah, Seal of the Prophets (peace be upon him), on which, as an expression of joy, he wrote a Persian poem. Most of Mohsin Kakorvi’s poetry is hamd and naat. The reason for his fame too is his naat poetry.','روایت ده چې محسن نهه کلن و چې په خوب کې یې د حضرت محمد رسول الله خاتم النبیین (ﷺ) زیارت نصیب شو چې پر هغې یې د خوښۍ د څرګندولو په توګه یو فارسي نظم ولیکه. د محسن کاکوروي ډېر کلام حمدیه او نعتیه دی. د هغه د شهرت لامل هم د هغه نعتیه کلام دی.')
P(s,'محسنؔ کی شاعری مجموعی طور پر زبان دانی کا ایک عمدہ نمونہ ہے جس میں عربی فارسی کے علاوہ ہندی الفاظ بھی استعمال کیے گئے ہیں۔ اُن کی نعتوں میں صداقت اور خلوص موجود ہے۔ اُن کا اُسلوب شگفتہ اور رواں دواں ہے۔ دبستانِ لکھنؤ سے تعلق کی وجہ سے اُن کے ہاں شوکتِ الفاظ پائی جاتی ہے۔ اُن کی زبان کوثر و تسنیم میں دُھلی ہوئی ہے۔ بندشیں چُست اور نادر و حسین تشبیہات اور استعارات نے اُن کے کلام کو چار چاند لگا دیے ہیں۔ اِن کے ہاں الفاظ کا چناؤ اور مضمون کی بلندی ہمیشہ ہم آہنگ نظر آتی ہے اور یہ چیز ان کی قادر الکلامی کی دلیل ہے۔ نعتوں کے علاوہ ان کے مجموعۂ کلّیات میں صحابۂ کرام (رضوان اللہ تعالیٰ علیہم اجمعین) کے مناقب بھی موجود ہیں اور بعض دیگر اصناف پر بھی اشعار ملتے ہیں جن میں تاریخ گوئی بھی ملتی ہے۔','Mohsin’s poetry as a whole is an excellent example of command of language in which, besides Arabic and Persian, Hindi words too have been used. In his naats sincerity and devotion are present. His style is lively and flowing. Because of his connection with the Lucknow school, grandeur of words is found in him. His language is washed in Kausar and Tasneem. Tight constructions and rare and beautiful similes and metaphors have added great lustre to his poetry. In him the choice of words and the loftiness of theme always appear in harmony, and this is proof of his mastery of speech. Besides naats, in his collected works there are also eulogies of the Companions (may Allah the Exalted be pleased with them all), and verses on some other genres too are found, among which chronogram-writing is also found.','د محسن شاعري په ټوله کې د ژبې پوهې یو ښه نمونه ده چې په هغې کې له عربي فارسي نه پرته هندي الفاظ هم کارول شوي دي. د هغه په نعتونو کې صداقت او اخلاص موجود دی. د هغه سټایل ژوندی او روان دی. د لکهنو له دبستان سره د تړاو له امله د هغه سره د الفاظو شوکت موندل کېږي. د هغه ژبه په کوثر او تسنیم کې مینځل شوې ده. چستې بندېشونه او نادر او ښکلې تشبیهات او استعارې د هغه کلام ته څلور سپوږمۍ ور ورکړې دي. د هغه سره د الفاظو انتخاب او د مضمون لوړتیا تل همغږي ښکاري او دا شی د هغه د قادر الکلامۍ دلیل دی. د نعتونو سر بېره د هغه په کلیاتو ټولګه کې د صحابه کرامو (رضوان الله تعالیٰ علیهم اجمعین) مناقب هم موجود دي او د ځینو نورو ډولونو شعرونه هم موندل کېږي چې په هغو کې تاریخ ګویي هم موندل کېږي.')
P(s,'مجموعۂ کلام: کلیاتِ نعتِ محسن','Poetry collection: Kulliyat-e-Naat-e-Mohsin','د شعري ټولګه: کلیات نعت محسن')
F.done()
s['sourceNote']='Printed page 117 (scan 124): ornamental title “محسن کاکوروی”, birth/death boxes (1826 and 1905), biography and the collection name; no portrait on this page.'+NOTE
s['vocabulary']={}
save(s)
# scan 125 = printed 118
s=page(125,'n02','118','Naat (Mohsin Kakorvi), part 1','نعت (محسن کاکوروی) (حصہ اوّل)','نعت (محسن کاکوروي) (لومړۍ برخه)','poem1')
F=Flow(s)
H(s,'نعت','Naat','نعت')
V(s,'سب سے اعلیٰ تری سرکار ہے، سب سے افضل','میرے ایمانِ مفصّل کا یہی ہے مُجمل','Your court is the highest of all, the most excellent of all;','this is the summary of my detailed faith.','تر ټولو لوړ ستا دربار دی، تر ټولو افضل','زما د مفصل ایمان لنډیز همدا دی')
V(s,'گلِ خوش رنگ رسولِ مدنی و عربی','زیبِ دامانِ ابد، طُرّۂ دستارِ اَزَل','The fair-coloured flower, the Messenger of Madina and Arabia,','the ornament of the skirt of eternity, the crest of the turban of pre-eternity.','ښکلی رنګین ګل، د مدیني او عربي رسول','د ابد د لمنې ښکلا، د ازل د دستار تاج')
V(s,'اَوجِ رِفعت کا قمر، نخلِ دو عالم کا ثمر','بحرِ وحدت کا گُہر، چشمۂ کثرت کا کنول','The moon of the zenith of loftiness, the fruit of the tree of the two worlds,','the pearl of the ocean of oneness, the lotus of the spring of multiplicity.','د لوړو لوړې سپوږمۍ، د دواړو نړیو د ونې میوه','د وحدت د بحر مروارید، د کثرت د چینې کنول')
V(s,'ہے تمنّا کہ رہے نعت سے تیرے خالی','نہ مرا شعر، نہ قطعہ، نہ قصیدہ، نہ غزل','My wish is that, empty of your naat, may remain','neither my verse, nor my quatrain, nor my qasida, nor my ghazal.','هیله ده چې ستا له نعت نه خالي پاتې شي','نه زما شعر، نه قطعه، نه قصیده، نه غزل')
V(s,'ہو مرا ریشۂ اُمّید، وہ نخلِ سر سبز','جس کی ہر شاخ میں ہوں پھول، ہر اک پھول میں پھل','May the root of my hope be that green tree','on each branch of which there are flowers, and in each flower a fruit.','زما د هیلې ریښه دې هغه شنه ونه وي','چې په هره څانګه کې یې ګلونه وي، په هر ګل کې میوه')
V(s,'رُخِ انور کا ترے دھیان رہے بعدِ فنا','میرے ہم راہ چلے راہِ عدم میں مشعل','May the thought of your radiant face remain after death;','may it walk with me as a torch on the road to non-being.','د ستا د رڼا مخ فکر دې له فنا وروسته وي','زما سره دې د عدم په لاره کې مشعل روان وي')
V(s,'صفِ محشر میں ترے ساتھ ہو تیرا مدّاح','ہاتھ میں ہو یہی مستانہ قصیدہ، یہ غزل','In the rows of the Resurrection may your praiser be with you,','with this ecstatic qasida, this ghazal, in his hand.','د محشر په صف کې ستا سره دې ستا ثنا خوان وي','په لاس کې دې همدا مستانه قصیده، دا غزل وي')
F.done()
s['sourceNote']='Printed page 118 (scan 125): title “نعت” in an ornamental frame, running head “محسن کاکوروی”, seven couplets, and the foot note “(قصیدہ «مدحِ خیر المرسلین ﷺ» سے انتخاب)” (selection from the qasida “Madh-e-Khair-ul-Mursaleen”).'+NOTE
s['vocabulary']={}
save(s)
