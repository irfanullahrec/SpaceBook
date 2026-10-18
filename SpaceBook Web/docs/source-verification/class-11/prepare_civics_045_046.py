from civicshelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,ur,en,ps,g,**m): add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g,**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting and ornamental borders excluded. Printed page = scan − 9. Words at the cut edge of the photographed page are restored from context and the Word text.'
# scan 45 = 023_page_2 : printed 36
s=page(45,'c02','36','Chapter 2: Kinds of Government — learning objectives','باب 2: حکومت کی اقسام — تدریسی مقاصد','۲ څپرکی: د حکومت ډولونه — د تدریس موخې','ch2')
F=Flow(s)
P(s,'باب 2','Chapter 2','۲ څپرکی')
H(s,'حکومت کی اقسام (Kinds of Government)','Kinds of Government','د حکومت ډولونه (Kinds of Government)')
P(s,'تدریسی مقاصد:','Learning objectives:','د تدریس موخې:',kind='heading')
P(s,'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:','After studying this chapter students will be able to:','د دې څپرکي له لوستلو وروسته به زده کوونکي دې ته وړ شي چې:')
for u,e,p in [
 ('۱۔ دنیا میں مروجہ طرزہائے حکومت یعنی بادشاہت، جمہوریت، اسلامی طرزِ حکومت اور آمریت کی شناخت کر سکیں۔','1. identify the forms of government current in the world, that is, monarchy, democracy, Islamic government and dictatorship.','۱. په نړۍ کې رواج حکومتي ډولونه یعنې پاچاهي، جمهوریت، اسلامي حکومت او استبداد وپېژني.'),
 ('۲۔ حکومت کی ساخت کی مختلف بنیادوں یعنی نظریہ، ثقافت، تاریخ اور اقدار کی وضاحت کر سکیں۔','2. explain the different bases of the structure of government, that is, ideology, culture, history and values.','۲. د حکومت د جوړښت بېلابېل بنسټونه یعنې نظریه، کلتور، تاریخ او ارزښتونه روښانه کړي.'),
 ('۳۔ ہر طرزِ حکومت کی نمایاں خصوصیات کی تشریح کر سکیں۔','3. describe the main characteristics of each form of government.','۳. د هر حکومتي ډول مهمې ځانګړتیاوې تشریح کړي.'),
 ('۴۔ ایسے تین ممالک کی نشاندہی کر سکیں جہاں مختلف طرز کی حکومتیں قائم ہیں۔','4. identify three countries where different kinds of government are established.','۴. داسې درې هېوادونه وپېژني چېرته چې بېلابېل ډوله حکومتونه شته.'),
 ('۵۔ یہ تشریح کر سکیں کہ ہر طرزِ حکومت کی بناوٹ کیسے ہوتی ہے یعنی ہر حکومت کے کلیدی اداروں کی تشریح۔','5. explain how each form of government is structured, that is, describe the key institutions of each government.','۵. تشریح کړي چې د هر حکومتي ډول جوړښت څنګه وي یعنې د هر حکومت د کلیدي ادارو تشریح.'),
 ('۶۔ اس بات کی وضاحت کر سکیں کہ ہر طرزِ حکومت میں ادارے کیسے عوام کی خدمت کرنے میں مصروفِ عمل ہوتے ہیں۔','6. explain how, in each form of government, institutions are engaged in serving the people.','۶. روښانه کړي چې په هر حکومتي ډول کې ادارې څنګه د خلکو په خدمت بوختې وي.'),
 ('۷۔ اس بات کا جائزہ لے سکیں کہ مختلف طرزہائے حکومت میں شہریوں کا کیا کردار ہوتا ہے۔','7. review what role citizens have in the different forms of government.','۷. وڅېړي چې په بېلابېلو حکومتي ډولونو کې د اتباعو رول څه وي.')]:
    I(s,u,e,p,'objectives')
F.done()
s['sourceNote']='Printed page 36 (scan 45): chapter opener with the chapter badge “باب 2”, title “حکومت کی اقسام (Kinds of Government)” and seven learning objectives. The left edge is cut and the left part of some lines is restored from the Word text.'+NOTE
s['vocabulary']={}
save(s)
# scan 46 = 023_page_1 : printed 37
s=page(46,'c02','37','Kinds of government; monarchy: definition','حکومت کی اقسام؛ بادشاہت کی تعریف','د حکومت ډولونه؛ د پاچاهۍ تعریف','kinds')
F=Flow(s)
H(s,'حکومت کی اقسام','Kinds of government','د حکومت ډولونه')
P(s,'دنیا بھر میں مختلف قسم کی حکومتیں پائی جاتی ہیں۔ مثلاً بادشاہت، جمہوریت، پارلیمانی نظام، صدارتی نظام اور آمریت وغیرہ۔ عام طور پر ہر ملک میں وہاں کے عوام کی نفسیات اور مزاج کے مطابق طرزِ حکومت اپنائی جاتی ہے۔ مثال کے طور پر برطانیہ میں آئینی بادشاہت ہے جو وہاں کے عوام کی روایت پسندی کی آئینہ دار ہے۔ بھارت اور پاکستان میں پارلیمانی جمہوریت ہے جبکہ امریکہ میں صدارتی جمہوریت قائم ہے۔ بعض اوقات ملک کی خراب سیاسی صورتِ حال کی وجہ سے مسلح افواج آمریت قائم کرتی ہیں۔','Different kinds of governments are found all over the world, for example monarchy, democracy, parliamentary system, presidential system and dictatorship. Generally in every country the form of government is adopted according to the psychology and temperament of its people. For example, Britain has a constitutional monarchy, which reflects the traditionalism of the people there. India and Pakistan have parliamentary democracy while America has presidential democracy. Sometimes, because of a country’s bad political situation, the armed forces establish dictatorship.','په نړۍ کې بېلابېل ډوله حکومتونه موندل کېږي، د بېلګې په توګه پاچاهي، جمهوریت، پارلماني نظام، ولسمشرۍ نظام او استبداد او نور. معمولاً په هر هېواد کې د هغه ځای د خلکو د نفسیاتو او مزاج سره سم حکومتي طرز خپلېږي. د بېلګې په توګه په برتانیه کې اساسي پاچاهي ده چې د هغه ځای د خلکو د دود پالنې ښکارندوی ده. په هند او پاکستان کې پارلماني جمهوریت دی پداسې حال کې چې په امریکا کې ولسمشریز جمهوریت دی. کله ناکله د هېواد د بد سیاسي حالت له امله وسله وال ځواکونه استبداد جوړوي.')
H(s,'بادشاہت (Monarchy)','Monarchy','پاچاهي (Monarchy)')
H(s,'بادشاہت کی تعریف (Definition)','Definition of monarchy','د پاچاهۍ تعریف (Definition)')
P(s,'لفظ بادشاہت کے لیے انگریزی زبان میں لفظ “Monarchy” استعمال کیا جاتا ہے جو دو یونانی الفاظ Mono اور Archo سے اخذ کیا گیا ہے جن کے بالترتیب معنی ہیں ایک اور حاکم۔ لہٰذا اس کا مطلب ہے ایک حاکم۔ مختلف مفکرین نے بادشاہت کی تعریف یوں کی ہے:','For the word “badshahat” the English word “Monarchy” is used, which is derived from two Greek words, “Mono” and “Archo”, meaning respectively one and ruler. Therefore its meaning is one ruler. Different thinkers have defined monarchy in this way:','د پاچاهۍ د ټکي لپاره په انګرېزي ژبه کې «Monarchy» ټکی کارول کېږي چې له دوو یوناني ټکو Mono او Archo اخیستل شوی دی چې په ترتیب سره معنا یې یو او حاکم ده. نو مطلب یې یو حاکم دی. بېلابېلو مفکرینو د پاچاهۍ تعریف داسې کړی دی:')
I(s,'۱۔ چیمبرز کے مطابق: «یہ حکومت کا وہ نظام ہے جس میں ایک بادشاہ، ملکہ یا دوسرا شاہی فرد ملک کا سرکاری حاکم ہوتا ہے بے شک اُس کے اختیارات بہت کم یا برائے نام کیوں نہ ہوں۔»','1. According to Chambers: “It is that system of government in which a king, queen or another royal person is the official ruler of the country, even though his powers may be very few or only nominal.”','۱. د چیمبرز له مخې: «دا د حکومت هغه نظام دی چې په کې یو پاچا، ملکه یا بل شاهي کس د هېواد رسمي حاکم وي که څه هم د هغه اختیارات ډېر لږ یا نومي وي.»','mdef')
I(s,'۲۔ انکارٹا کے مطابق: «وہ سیاسی نظام جس میں ایک بادشاہ یا اُس کے خاندان کا کوئی اور فرد حکومت کرے۔» اس طرزِ حکومت میں سارے ریاستی اختیارات بادشاہ کے پاس ہوتے ہیں اور حکومت کے تمام انتظامی، عدالتی اور قانون سازی کے فرائض وہ خود ہی سرانجام دیتا ہے یا اُس کی زیرِ نگرانی ادا کیے جاتے ہیں۔','2. According to Encarta: “The political system in which a king or another member of his family rules.” In this form of government all the powers of the state are with the king and he himself performs all the administrative, judicial and legislative duties of the government or they are performed under his supervision.','۲. د انکارټا له مخې: «هغه سیاسي نظام چې په کې یو پاچا یا د هغه د کورنۍ بل کس حکومت کوي.» په دې حکومتي طرز کې د دولت ټول اختیارات د پاچا سره وي او د حکومت ټولې اداري، قضایي او قانوني دندې هغه پخپله ترسره کوي یا د هغه تر څارنې لاندې ترسره کېږي.','mdef')
F.done()
s['sourceNote']='Printed page 37 (scan 46): the heading “حکومت کی اقسام” (with pen notes written above it, ignored), a paragraph, the blue banner “بادشاہت (Monarchy)”, the heading “بادشاہت کی تعریف (Defintion)” (the printed English caption is misspelt) and two definitions. The right edge of the photograph is cut.'+NOTE
s['vocabulary']={}
save(s)
