from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n08',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 147 = printed 140
s=page(147,'n08','140','Naseehat-e-Akhlaqi (Akbar Allahabadi)','نصیحتِ اخلاقی (اکبر الٰہ آبادی)','اخلاقي نصیحت (اکبر الله اباد)','poem1')
F=Flow(s)
H(s,'نصیحتِ اخلاقی','Naseehat-e-Akhlaqi (Moral Advice)','اخلاقي نصیحت')
for r in [
('بیٹے کو لوگ کہتے ہیں، آنکھوں کا نور ہے','ہے زندگی کا لطف۔ تو دل کا سرور ہے','People call the son the light of the eyes;','he is the pleasure of life, the delight of the heart.','زوی ته خلک وايي د سترګو رڼا ده','د ژوند خوند دی. د زړه سرور دی'),
('گھر میں اسی کے دم سے ہے ہر سمت روشنی','نازاں ہے اس پہ باپ، تو ماں کو غرور ہے','In the home, by his breath there is light on every side;','the father is proud of him and the mother takes pride.','په کور کې د هغه په ساه هر لور رڼا ده','پلار پرې ویاړي، مور ورته ویاړ لري'),
('خوش قسمتی کی اس کو نشانی سمجھتے ہیں','کہتے ہیں یہ خدا کے کرم کا ظہور ہے','They regard him as the sign of good fortune;','they say this is the manifestation of God’s mercy.','هغه د نېکمرغۍ نښه ګڼي','وايي دا د خدای د کرم ظهور دی'),
('اکبرؔ بھی اس خیال سے کرتا ہے اتفاق','اس کا بھی ہے یہ قول، کہ ایسا ضرور ہے','Akbar too agrees with this idea;','this is his saying too: that it is certainly so.','اکبر هم له دې خیال سره موافق دی','دا د هغه هم خبره ده چې داسې ضرور دی'),
('البتہ شرط یہ ہے، کہ بیٹا ہو ہونہار','مائل ہے نیکیوں پہ، برائی سے دور ہے','The condition, however, is that the son be promising,','inclined to good deeds and far from evil.','البته شرط دا ده چې زوی هونهار وي','په نېکیو مایل وي، له بدۍ لرې وي'),
('سنتا ہے دل لگا کے بزرگوں کی پند کو','وقتِ کلام لب پہ جناب و حضور ہے','He listens attentively to the advice of elders;','at the time of speaking “sir” and “your honour” are on his lips.','د لویانو نصیحت په زړه اورېږي','د خبرو پر مهال پر شونډو یې جناب او حضور وي'),
('برتاؤ اس کا صدق و محبّت سے ہے بھرا','اس میں نہ ہے فریب نہ ہے مکر و زور ہے','His conduct is full of truth and love;','in it there is neither deceit nor craft and force.','د هغه چلند له رښتینولۍ او مینې ډک دی','پدې کې نه درغلي ده نه مکر او زور'),
('افکارِ والدین میں ہے دل سے وہ شریک','ہمدرد ہے معین ہے اہلِ شعور ہے','He shares from the heart in the parents’ anxieties;','he is sympathetic, a helper, a man of understanding.','د والدینو په فکرونو کې له زړه ګډون لري','هم درد دی، مرستندوی دی، د شعور خاوند دی'),
('راضی ہے اس پہ باپ کی جو کچھ ہو مصلحت','صابر ہے با ادب ہے عقیل و غیور ہے','He is content with whatever the father’s considered policy may be;','he is patient, courteous, intelligent and self-respecting.','پدې راضي دی چې د پلار څه مصلحت وي','صابر دی، با ادبه دی، هوښیار او غیرتي دی'),
('رکھتا ہے خاندان کی عزّت کا وہ خیال','نیکوں کا دوست صحبتِ بد سے نفور ہے','He keeps in mind the honour of the family;','he is a friend of the good and averse to bad company.','د کورنۍ د عزت خیال ساتي','د نېکانو ملګری دی، له بد ملګرتیا نه کرکه لري'),
('کسبِ کمال کی ہے شب و روز اس کو دھن','علم و ہنر کے شوق کا دل میں وفور ہے','Night and day he is intent on acquiring perfection;','his heart is full of eagerness for knowledge and skill.','د کمال د ترلاسه کولو شپه او ورځ ورته لېوالتیا ده','د علم او هنر د شوق په زړه کې ډېروالی دی'),
('لیکن جو ان صفات کا مطلق نہیں پتا','اور پھر بھی ہے خوشی تو خوشی کا قصور ہے','But he who has no trace of these qualities at all','and is still happy — then the fault is that of happiness.','خو هغه چې د دغو صفتونو هېڅ پته نه لري','او بیا هم خوشاله دی نو د خوښۍ ګناه ده')]:
    V(s,*r)
P(s,'(کلیاتِ اکبر حصّہ اوّل)','(Kulliyat-e-Akbar, part one)','(کلیات اکبر لومړۍ برخه)')
F.done()
s['sourceNote']='Printed page 140 (scan 147): title “نصیحتِ اخلاقی” in an ornamental frame, running head “اکبر الٰہ آبادی”, a poem of twelve couplets printed in two columns (each right-hand half-line is paired with the left-hand one in the same row), and the source line “(کلیاتِ اکبر حصہ اوّل)”.'+NOTE
s['vocabulary']={}
save(s)
# scan 148 = printed 141
s=page(148,'n08','141','Exercise (Mashq) on Naseehat-e-Akhlaqi; teachers’ instruction','مشق: «نصیحتِ اخلاقی» پر سوالات؛ ہدایت برائے اساتذہ','تمرین: «اخلاقي نصیحت» پوښتنې؛ د ښوونکو لارښوونه','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ اس نظم میں اکبر الٰہ آبادی نے ہونہار بیٹے کی کیا خصوصیات بتائی ہیں؟','1. What characteristics of a promising son has Akbar Allahabadi stated in this poem?','۱. پدې نظم کې اکبر الله اباد د هونهار زوی کومې ځانګړتیاوې بیان کړي دي؟')
Q(s,'2۔ نظم «نصیحتِ اخلاقی» کا خلاصہ لکھیں۔','2. Write a summary of the poem “Naseehat-e-Akhlaqi”.','۲. د «اخلاقي نصیحت» نظم لنډیز ولیکئ.')
Q(s,'3۔ درج ذیل الفاظ و محاورات کے معنی لکھیں اور جملوں میں استعمال کریں۔ نازاں، ظہور، مکر و زور، کسبِ کمال، اہلِ شعور۔','3. Write the meanings of the following words and idioms and use them in sentences: nazaan, zuhoor, makr-o-zor, kasb-e-kamal, ahl-e-shaoor.','۳. د لاندې الفاظو او محاورو معنا ولیکئ او په جملو کې یې وکاروئ. نازان، ظهور، مکر او زور، کسب کمال، اهل شعور.')
Q(s,'4۔ اس نظم کا مرکزی خیال تحریر کریں۔','4. Write the central idea of this poem.','۴. د دې نظم مرکزي خیال ولیکئ.')
Q(s,'5۔ اس نظم کے قوافی لکھیں۔','5. Write the rhymes of this poem.','۵. د دې نظم قافیې ولیکئ.')
H(s,'ہدایت برائے اساتذہ:','Instruction for teachers:','د ښوونکو لپاره لارښوونه:')
P(s,'طلبہ کو طنز و مزاح کی تعریف بتائیں نیز دونوں کے فرق اور اہمیت سے روشناس کریں۔','Tell the students the definition of satire and humour and also acquaint them with the difference and importance of the two.','زده‌کوونکو ته د طنز او مزاح تعریف ووایئ او همدارنګه د دواړو له توپیر او اهمیت نه یې خبر کړئ.',boxed=True)
F.done()
s['sourceNote']='Printed page 141 (scan 148): “Mashq” title, questions 1–5 (question 3 lists words in blue) and the boxed teachers’ instruction; the middle of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 149 = printed 142
s=page(149,'n09','142','Hafeez Jalandhari (poet profile)','حفیظ جالندھری (شاعر کا تعارف)','حفیظ جالندهري (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'حفیظ جالندھری','Hafeez Jalandhari','حفیظ جالندهري')
P(s,'پیدایش: ۱۹۰۰ء — وفات: ۱۹۸۲ء','Born: 1900 — Died: 1982','زېږېدنه: ۱۹۰۰ز — وفات: ۱۹۸۲ز')
P(s,'محمد حفیظ نام اور حفیظ ہی تخلص تھا۔ جالندھر میں پیدا ہوئے۔ والد کا نام حافظ شمس الدّین تھا۔ اُن کے اُستاد اُنھیں ابوالاثر حفیظ کہتے تھے اور وہ اسی نام سے مشہور ہوئے۔ ان کی ابتدائی تعلیم جالندھر ہی میں ہوئی۔ وہ خاندانی حالات اور گھریلو ذمّے داریوں کی وجہ سے اپنی تعلیم مکمل نہ کر سکے۔ وہ بائیس سال کی عمر میں جالندھر سے لاہور آئے۔ یہاں کی ادبی فضا میں ان کے ادبی جوہر خوب کھلے اور جلد ہی وہ اپنے دور کے ممتاز شعرا میں شمار ہونے لگے۔','His name was Muhammad Hafeez and “Hafeez” was his pen-name. He was born in Jalandhar. His father’s name was Hafiz Shamsuddin. His teacher used to call him Abul Asar Hafeez, and he became famous by that very name. His early education was in Jalandhar itself. Because of family circumstances and domestic responsibilities he could not complete his education. At the age of twenty-two he came to Lahore from Jalandhar. In the literary atmosphere here his literary gems opened out well, and soon he came to be counted among the distinguished poets of his age.','نوم یې محمد حفیظ او تخلص یې حفیظ و. په جالندهر کې زېږېدلی دی. د پلار نوم حافظ شمس الدین و. د هغه استاد هغه ته ابوالاثر حفیظ ویل او هغه په همدې نوم مشهور شو. د هغه لومړنۍ زده‌کړه په جالندهر کې وشوه. هغه د کورنیو حالاتو او کورنیو مسؤلیتونو له امله خپله زده‌کړه بشپړه نشوه کړای. هغه د دوه ویشت کلنۍ په عمر له جالندهر نه لاهور ته راغی. دلته د ادبي فضا په منځ کې د هغه ادبي جوهر ښه څرګند شو او ژر په خپل دور د ممتازو شاعرانو په ډله کې شمېرل شو.')
P(s,'اُنھوں نے پاکستان کا قومی ترانہ اور اسلام کی منظوم تاریخ «شاہنامۂ اسلام» کے عنوان سے رقم کی۔ ان دونوں تخلیقات نے انھیں زندۂ جاوید بنا دیا۔','He wrote the national anthem of Pakistan and the versified history of Islam under the title “Shahnama-e-Islam”. These two creations made him immortal.','هغه د پاکستان ملي ترانه او د اسلام منظوم تاریخ د «شاهنامه اسلام» په نوم ولیکل. دغو دواړو تخلیقاتو هغه تل پاتې کړ.')
P(s,'حفیظؔ بنیادی طور پر گیت نگار ہیں۔ اُن کے گیت جذبات اور لطافت سے بھرپور ہیں۔ وہ عام طور پر چھوٹی اور مترنّم بحریں استعمال کرتے ہیں۔ اُن کی شاعری کی خصوصیّت غنائیت اور شگفتگی ہے۔ اُن کی شاعری میں ہندی الفاظ کا بے تکلفانہ انداز، ان کے کلام میں مٹھاس پیدا کر دیتا ہے۔ انھوں نے نظموں میں قابلِ قدر تجربے بھی کیے۔ سادگی دل کشی، موسیقیّت، تغزّل، منظر کشی، ندرتِ تشبیہات، مقصدیّت اور متنوّع بحروں کا استعمال ان کے کلام کی نمایاں خصوصیات ہیں۔','Hafeez is basically a lyricist. His songs are full of emotion and delicacy. He generally uses short and melodious metres. The characteristic of his poetry is lyricism and freshness. In his poetry the informal way of using Hindi words creates sweetness in his verse. In his nazms he also made valuable experiments. Simplicity, charm, musicality, lyric quality, scene-painting, novelty of similes, purposefulness and the use of varied metres are the prominent characteristics of his poetry.','حفیظ بنسټیز ډول سندرغاړی دی. د هغه سندرې په جذباتو او نرمۍ ډکې دي. هغه عموماً لنډې او مترنمې بحرونه کاروي. د هغه د شاعرۍ ځانګړتیا غنایت او شګوفتګي ده. د هغه په شاعرۍ کې د هندي الفاظو بې تکلفه انداز د هغه په کلام کې خوږوالی پیدا کوي. هغه په نظمونو کې د قدر وړ تجربې هم وکړې. سادګي زړه کښونه، موسیقیت، تغزل، منظر ښودل، د تشبیهاتو نوښت، مقصدیت او بېلابېلو بحرونو کارول د هغه د کلام څرګندې ځانګړتیاوې دي.')
P(s,'تصانیف: سوز و ساز، تلخابۂ شیریں، تصویرِ کشمیر، بہار کے پھول، نغمہ زار، حفیظ کے گیت، حفیظ کی نظمیں اور چیونٹی نامہ۔','Works: Soz-o-Saaz, Talkhaba-e-Shireen, Tasweer-e-Kashmir, Bahar ke Phool, Naghma Zaar, Hafeez ke Geet, Hafeez ki Nazmein and Cheeonti Nama.','تصنیفات: سوز او ساز، تلخابه شیرین، تصویر کشمیر، د بهار ګلونه، نغمه زار، د حفیظ سندرې، د حفیظ نظمونه او چیونټي نامه.')
F.done()
s['sourceNote']='Printed page 142 (scan 149): ornamental title “حفیظ جالندھری”, portrait (not reproduced), birth/death boxes (1900 and 1982), biography and list of works (the dates are read from the scan).'+NOTE
s['vocabulary']={}
save(s)
