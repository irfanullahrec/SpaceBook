from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n09',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. The poem is printed in two columns of half-lines (right and left); each row is stored as one two-line item, right-hand half-line first.'
# scan 150 = printed 143
s=page(150,'n09','143','Jalwa-e-Sehar (Hafeez Jalandhari), part 1','جلوۂ سحر (حفیظ جالندھری) (حصہ اوّل)','د سهار جلوه (حفیظ جالندهري) (لومړۍ برخه)','poem1')
F=Flow(s)
H(s,'جلوۂ سحر','Jalwa-e-Sehar (The Splendour of Dawn)','د سهار جلوه')
for r in [
('چلا ستارۂ سحر','سنا کے صبح کی خبر','The star of dawn has set out,','announcing the news of morning.','د سهار ستوری روان شو','د سهار خبر اورولو سره'),
('زمیں پہ نور چھا گیا','فلک پہ رنگ آ گیا','Light spread over the earth;','colour came upon the sky.','پر ځمکه رڼا خپره شوه','پر اسمان رنګ راغی'),
('تمام زادگانِ شب','چمک چمک کے سو گئے','All the children of the night','twinkled and twinkled and went to sleep;','د شپې ټول زامن','ځلېدلو ځلېدلو سره ویده شول'),
('شرارِ آسمانِ شب','دمک دمک کے سو گئے','the sparks of the night sky','glowed and glowed and went to sleep.','د شپې اسمان څلانده','ځلېدلو ځلېدلو سره ویده شول'),
('ستارے زرد ہو چکے','چراغ سرد ہو چکے','The stars have turned pale;','the lamps have turned cold.','ستوري ژیړ شوي دي','څراغونه سړه شوي دي'),
('وہ ٹمٹما کے رہ گئے','یہ جھلملا کے رہ گئے','Those flickered and were left;','these glimmered and were left.','هغوی ټمټمېدو سره پاتې شول','دغوی ځلېدو سره پاتې شول'),
('چلا ستارۂ سحر','سنا کے صبح کی خبر','The star of dawn has set out,','announcing the news of morning.','د سهار ستوری روان شو','د سهار خبر اورولو سره')]:
    V(s,*r)
for r in [
('یکایک ایک نور کا','غبارِ شرق سے اٹھا','Suddenly a cloud of light','rose from the dust-cloud of the east;','ناڅاپه د یوې رڼا','د ختیځ له غبار پورته شوه'),
('وہ رفتہ رفتہ بڑھ چلا','اور آسماں پہ چھا گیا','it gradually advanced','and spread over the sky.','هغه ورو ورو مخکې ولاړ','او پر اسمان خپره شوه'),
('حسینۂ نمود نے','نقاب اٹھا دیا','The beauty of appearance','lifted her veil;','د ښکاره کېدو ښکلې','پرده پورته کړه'),
('فسوں گرِ شہود نے','طلسمِ شب مٹا دیا','the enchanter of the witnessed world','erased the spell of the night.','د مشاهدې افسونګر','د شپې طلسم له منځه یووړ'),
('یکایک ایک تازگی','یکایک ایک روشنی','Suddenly a freshness','suddenly a light','ناڅاپه یو تازګي','ناڅاپه یوه رڼا'),
('نگاہِ جاں میں آ گئی','حیات میں سما گئی','came into the eye of the soul;','merged into life.','د ساه په سترګو کې راغله','په ژوند کې ننوته'),
('یکایک ایک نور کا','غبارِ شرق سے اٹھا','Suddenly a cloud of light','rose from the dust-cloud of the east.','ناڅاپه د یوې رڼا','د ختیځ له غبار پورته شوه')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 143 (scan 150): title “جلوۂ سحر” (very faint in the scan), running head “حفیظ جالندھری”, and the first two stanzas of the poem, each printed as seven rows with a refrain repeated at the start and end. The scan is slightly out of focus.'+NOTE
s['vocabulary']={}
save(s)
# scan 151 = printed 144
s=page(151,'n09','144','Jalwa-e-Sehar, part 2','جلوۂ سحر (حصہ دوم)','د سهار جلوه (دویمه برخه)','poem2')
F=Flow(s)
for r in [
('عبادتوں کے در کھلے','سعادتوں کے در کھلے','The doors of worship have opened;','the doors of blessing have opened.','د عبادتونو دروازې خلاصې شوې','د سعادتونو دروازې خلاصې شوې'),
('درِ قبول وا ہوا','دعا کا وقت آ گیا','The door of acceptance is open;','the time of prayer has come.','د قبولېدو دروازه خلاصه شوه','د دعا وخت راغی'),
('اذان کی صدا اٹھی','جگا ……… کو','The call to prayer has risen,','waking … (the rest of this line is illegible in the scan).','د اذان غږ پورته شو','ویښ کړی ……… (د دې کرښې پاتې برخه په سکین کې ناپېژندل ده)'),
('چلی ہے اٹھ کے بندگی','لیے ہوئے نیاز کو','Worship has set out, having risen,','carrying its supplication.','بندګي پاڅېدو سره روانه شوې','خپل نیاز له ځان سره اخیستو سره'),
('صنم کدہ بھی کھل گیا','اٹھا ہے شور سنکھ کا','The idol-house too has opened;','the din of the conch has risen.','د بتخانې دروازه هم خلاصه شوه','د شنګ شور پورته شوی'),
('چلو نمازیو! چلو','اٹھو پجاریو! اٹھو','Come, worshippers, come!','Rise, priests, rise!','ځئ لمونځ کوونکو! ځئ','پاڅېږئ پوجاریانو! پاڅېږئ'),
('عبادتوں کے در کھلے','سعادتوں کے در کھلے','The doors of worship have opened;','the doors of blessing have opened.','د عبادتونو دروازې خلاصې شوې','د سعادتونو دروازې خلاصې شوې')]:
    V(s,*r)
for r in [
('کسان اٹھ کھڑے ہوئے','مویشیوں کو لے چلے','The farmers have stood up','and are leading their cattle out.','بزګران پاڅېدلي دي','او خپل څاروي یې وړي'),
('کہیں مزے میں آ گئے','تو کوئی تان اڑا گئے','If somewhere they got into the mood,','then some raised a tune.','که چېرته په مزه کې راغلل','نو کوم تان یې پورته کړ'),
('یہ سرد شبنمی ہوا','یہ صحت آفریں سماں','This cool dewy breeze,','this health-giving atmosphere,','دا سړه شبنمي باد','دا روغتیا ورکوونکی فضا'),
('یہ فرشِ سبز گھاس کا','یہ دل فریب آسماں','this green carpet of grass,','this heart-alluring sky —','دا د واښو شین فرش','دا زړه راکښونکی اسمان'),
('بسے ہوئے ہیں پریت میں','ہیں محو ان کے گیت میں','they dwell in love,','they are absorbed in their songs.','په مینه کې مېشت دي','د هغوی په سندرو کې ډوب دي'),
('کہاں ہیں شہر کے مکیں','وہ بے نصیب اُٹھے نہیں','Where are the dwellers of the city?','Those unlucky ones have not risen.','چېرته دي د ښار اوسېدونکي','هغه بې نصیبه نه دي پاڅېدلي'),
('کسان اٹھ کھڑے ہوئے','مویشیوں کو لے چلے','The farmers have stood up','and are leading their cattle out.','بزګران پاڅېدلي دي','او خپل څاروي یې وړي')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 144 (scan 151): two stanzas of the poem as in the previous page (refrain at start and end of each); the second half-line of the third row of the first stanza is only partly legible (“جگا … … کو”). Row 5 of the second stanza reads “بسے ہوئے پریت میں / ہیں محو ان کے گیت میں” in print.'+NOTE
s['vocabulary']={}
save(s)
# scan 152 = printed 145
s=page(152,'n09','145','Jalwa-e-Sehar, end; Exercise (Mashq)','جلوۂ سحر (اختتام)؛ مشق','د سهار جلوه (پای)؛ تمرین','poem3')
F=Flow(s)
for r in [
('اٹھی حسینۂ سحر','پہن کے سر پہ تاجِ زر','The beauty of dawn has risen,','wearing a crown of gold on her head.','د سهار ښکلې پاڅېده','په سر یې د زرو تاج اغوستی'),
('لباسِ نور زیبِ بر','چڑھی فرازِ کوہ پر','Clothed in a garment of light,','she climbed on the summit of the mountain.','د رڼا جامې یې په تن ښکلې','پر غره سر ته وختله'),
('وہ خندۂ نگاہ سے','پہاڑ طور بن گئے','By the laughter of her glance','the mountains became Mount Tur;','د هغې د سترګو له خندا','غرونه طور شول'),
('وہ عکسِ جلوہ گاہ سے','…………… بن گئے','by the reflection of her place of manifestation','… … became … (the second half-line is hidden by a fold in the scan).','د هغې د جلوه ځای له انعکاس','…………… شول (دویمه نیمه مصرع په سکین کې د تاو له امله پټه ده)'),
('نوائے جُوئبار اُٹھی','صدائے آبشار اُٹھی','The song of the stream rose,','the sound of the waterfall rose;','د ویالې نوا پورته شوه','د اوبو غورځېدو غږ پورته شو'),
('ہواؤں کے رباب اُٹھے','خوش آمدید کے لیے','the lutes of the winds rose','to welcome her.','د بادونو رباب پورته شول','د ښه راغلاست لپاره'),
('اٹھی حسینۂ سحر','پہن کے سر پہ تاجِ زر','The beauty of dawn has risen,','wearing a crown of gold on her head.','د سهار ښکلې پاڅېده','په سر یې د زرو تاج اغوستی')]:
    V(s,*r)
P(s,'(سرمایۂ اُردو، انتخاب از حافظ محمود شیرانی)','(Sarmaya-e-Urdu, selection by Hafiz Mahmood Sherani)','(سرمایه اردو، د حافظ محمود شیراني انتخاب)')
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ «جلوۂ سحر» میں پیش کیا گیا صبح کا منظر اپنے الفاظ میں بیان کریں۔','1. Describe in your own words the scene of morning presented in “Jalwa-e-Sehar”.','۱. په «د سهار جلوه» کې وړاندې شوی د سهار منظر په خپلو الفاظو بیان کړئ.')
Q(s,'2۔ اس نظم میں صبح کا منظر بڑی خوب صورتی سے بیان کیا گیا ہے۔ آپ شام کے منظر کو اپنے الفاظ میں بیان کریں۔','2. In this poem the scene of morning has been described very beautifully. Describe the scene of evening in your own words.','۲. پدې نظم کې د سهار منظر په ډېر ښکلا بیان شوی دی. تاسو د ماښام منظر په خپلو الفاظو بیان کړئ.')
Q(s,'3۔ آخری بند میں شاعر نے صبح کو «حسینۂ سحر» کے ایک کردار کی صورت میں پیش کرتے ہوئے اس کے استقبال کو کن لفظوں میں بیان کیا ہے؟','3. In the last band, presenting the morning as a character, “Haseena-e-Sehar”, in what words has the poet described her welcome?','۳. په وروستۍ بند کې شاعر سهار د «حسینۀ سحر» د یو کردار په بڼه وړاندې کولو سره د هغې هرکلی په کومو الفاظو بیان کړی دی؟')
Q(s,'4۔ جملے بنائیں۔ یکایک، سعادت، صحت آفریں، جلوہ گاہ، جوئبار، آبشار۔','4. Make sentences: yakayak, saadat, sehat-afreen, jalwa-gah, joobaar, aabshaar.','۴. جملې جوړې کړئ. یکایک، سعادت، صحت آفرین، جلوه ګاه، جوی بار، آبشار.')
Q(s,'5۔ کنایہ کی تعریف کریں اور مثالوں کی مدد سے وضاحت کریں۔','5. Define kinaya (indirect reference) and explain with the help of examples.','۵. د کنایې تعریف وکړئ او د بېلګو په مرسته یې تشریح کړئ.')
F.done()
s['sourceNote']='Printed page 145 (scan 152): the last stanza of the poem (fourth row’s left half-line hidden by a fold of the page), source line “(سرمایۂ اُردو، انتخاب از حافظ محمود شیرانی)”, the “Mashq” title and questions 1–5 (question 4 lists words in blue).'+NOTE
s['vocabulary']={}
save(s)
