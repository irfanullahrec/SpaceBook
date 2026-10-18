from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='g01',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='g01'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'urdu11-{u}-q',tab='exercise')
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Ghazal couplets: the two printed hemistichs are stored as two lines (right-hand hemistich first in rows printed in two columns).'
# scan 168 = printed 161
s=page(168,'g01','161','Ghazal (Mir Taqi Mir): “Faqeerana aaye sada kar chale”','غزل (میر تقی میر): «فقیرانہ آئے صدا کر چلے»','غزل (میر تقي میر): «فقیرانه راغلو غږ کولو سره ولاړو»','poem1')
F=Flow(s)
H(s,'غزل','Ghazal','غزل')
for r in [
('فقیرانہ آئے صدا کر چلے','میاں! خوش رہو ہم دُعا کر چلے','We came as faqirs and, calling out, we depart;','“Friends! Stay happy; we depart praying for you.”','فقیرانه راغلو غږ کولو سره ولاړو','ورورګلو! خوشاله اوسئ موږ دعا کولو سره ځو'),
('وہ کیا چیز ہے آہ! جس کے لیے','ہر اِک چیز سے دل اُٹھا کر چلے','What is that thing, alas, for which','we depart having turned our heart from everything?','هغه څه شی دی افسوس چې د هغه لپاره','له هر شي نه زړه پورته کړو او ولاړو'),
('کوئی نا اُمیدانہ کرتے نگاہ','سو تم ہم سے منہ بھی چھپا کر چلے','Someone casting a hopeless glance —','so you too depart hiding your face from us.','کوم نا امیده نظر کولو سره','نو تاسو هم له موږ نه مخ پټولو سره ځئ'),
('دکھائی دیے یوں کہ بے خود کیا','ہمیں آپ سے بھی جدا کر چلے','You appeared in such a way as to make us beside ourselves;','you depart having separated us even from ourselves.','داسې مو ښکاره شوئ چې بې خوده مو کړو','موږ مو له خپل ځان نه هم جلا کړو او ولاړو'),
('جبیں سجدہ کرتے ہی کرتے گئی','حقِ بندگی ہم ادا کر چلے','The forehead went on prostrating and prostrating;','we depart having fulfilled the right of servitude.','تندی سجده کولو سجده کولو تلل','د بندګۍ حق مو ادا کړ او ولاړو'),
('پرستش کی یاں تک کہ اے بت تجھے','نظر میں سبھوں کی خدا کر چلے','O idol, we worshipped you so much that','we depart having made you God in everyone’s sight.','ای بته موږ دومره ستاسو پرستش وکړه چې','د ټولو په نظر کې مو خدای کړو او ولاړو')]:
    V(s,*r)
V(s,'کہیں کیا، جو پوچھے کوئی ہم سے میرؔ','جہاں میں تم آئے تھے، کیا کر چلے','What shall we say if someone asks us, Mir,','“You came into the world; what did you do and depart?”','څه ووایو که څوک له موږ نه وپوښتي میر','«په نړۍ کې راغلئ، څه مو وکړل او ولاړئ»')
P(s,'(انتخابِ کلامِ میرؔ)','(Selection from the verse of Mir)','(د میر د کلام انتخاب)')
F.done()
s['sourceNote']='Printed page 161 (scan 168): title “غزل” in an ornamental frame, running head “میر تقی میر”, the ghazal “فقیرانہ آئے صدا کر چلے” (six couplets in two columns plus the closing couplet with the pen-name “میر” centred) and source line “(انتخابِ کلامِ میرؔ)”.'+NOTE
s['vocabulary']={}
save(s)
# scan 169 = printed 162
s=page(169,'g01','162','Ghazal (Mir Taqi Mir): “Peeri mein kya jawani ke mausam ko roiye”','غزل (میر تقی میر): «پیری میں کیا جوانی کے موسم کو رویئے»','غزل (میر تقي میر): «په زوړ والي کې د ځوانۍ پر موسم څه ژاړو»','poem2')
F=Flow(s)
H(s,'غزل','Ghazal','غزل')
for r in [
('پیری میں کیا جوانی کے موسم کو رویئے','اب صبح ہونے آئی ہے، اک دم تو سویئے','In old age, why weep for the season of youth?','Now morning is about to dawn; let us sleep at least a moment.','په زوړ والي کې د ځوانۍ پر موسم څه ژاړو','اوس سهار کېږي، یو دم خو ویده شو'),
('اخلاصِ دل سے چاہیے سجدہ نماز میں','بے فائدہ ہے ورنہ جو یوں وقت کھویئے','Prostration in prayer should be with sincerity of heart;','otherwise it is useless if you waste time thus.','د زړه له اخلاصه باید په لمانځه کې سجده وي','که نه بې ګټې ده چې داسې وخت ضایع کړئ'),
('کس طور آنسوؤں میں نہاتے ہیں غم گُساں','اس آبِ گرم میں تو نہ انگلی ڈبویئے','How do the sorrow-sharers bathe in tears?','you should not dip even a finger in that hot water.','څنګه په اوښکو کې غم خوړونکي ځان مینځي','په دې ګرمو اوبو کې خو ګوته هم مه ډوبوئ'),
('اب جان جسمِ خاک سے تنگ آ گئی بہت','کب تک اس ایک ٹوکری مٹی کو دھویئے','Now the soul has become very tired of the body of dust;','how long should one wash this one basket of clay?','اوس ساه له خاورینې جسم نه ډېره تنګه شوې','تر کومه به دا یوه ټوکرۍ خټه مینځو'),
('آلودہ اُس گلی کی جو ہوں خاک سے تو میرؔ','آبِ حیات سے بھی نہ وے پاؤں دھویئے','If you are soiled by the dust of that lane, Mir,','do not wash those feet even with the water of life.','که د هغې کوڅې په خاوره آلوده یې میر','د ژوند په اوبو هم هغه پښې مه مینځئ')]:
    V(s,*r)
P(s,'(انتخابِ کلامِ میرؔ، ڈاکٹر مولوی عبد الحق)','(Selection from the verse of Mir, Dr Maulvi Abdul Haq)','(د میر د کلام انتخاب، ډاکټر مولوي عبدالحق)')
F.done()
s['sourceNote']='Printed page 162 (scan 169): title “غزل” (faint) and a second ghazal of Mir (five couplets, each two lines), source line “(انتخابِ کلامِ میرؔ، ڈاکٹر مولوی عبد الحق)”. The last couplet reads “نہ وے” as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 170 = printed 163
s=page(170,'g01','163','Exercise (Mashq) on the ghazals of Mir: question 1 (multiple choice)','مشق: غزلیاتِ میر پر سوالات: سوال 1 (کثیر انتخابی)','تمرین: د میر غزلونو پوښتنې: ۱ پوښتنه (څو انتخابي)','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ دُرست الفاظ کا انتخاب کریں۔','1. Choose the correct words.','۱. سم الفاظ غوره کړئ.')
def M(txt,en,ps,opts):
    add(s,f'q{len(s["paras"])+1}',en,txt,ps,role='question',exerciseId='urdu11-g01-q',tab='exercise')
    for a,e,(u,en2,p2) in zip(['الف','ب','ج','د'],['a','b','c','d'],opts):
        add(s,f'o{len(s["paras"])+1}',f'({e}) {en2}',f'{a}) {u}',f'{a}) {p2}',role='option',exerciseId='urdu11-g01-q',tab='exercise')
M('(الف) ہر شعر میں ............ مصرعے ہوتے ہیں۔','(a) In every couplet there are ............ lines.','(الف) په هر شعر کې ............ مصرعې وي.',[('دو','two','دوه'),('چار','four','څلور'),('تین','three','درې'),('پانچ','five','پنځه')])
M('(ب) غزل کے پہلے شعر کو ............ کہتے ہیں۔','(b) The first couplet of a ghazal is called ............','(ب) د غزل لومړي شعر ته ............ وايي.',[('ردیف','radif','ردیف'),('بیت الغزل','bait-ul-ghazal','بیت الغزل'),('مقطع','maqta','مقطع'),('مطلع','matla','مطلع')])
M('(ج) غزل کے ............ میں شاعر اپنا تخلص استعمال کرتا ہے۔','(c) In the ............ of a ghazal the poet uses his pen-name.','(ج) د غزل په ............ کې شاعر خپل تخلص کاروي.',[('مطلع','matla','مطلع'),('مقطع','maqta','مقطع'),('درمیان','middle','منځ'),('آغاز','beginning','پیل')])
M('(د) میرؔ کو ............ کہا گیا۔','(d) Mir was called ............','(د) میر ته ............ ویل شوي.',[('خدائے سخن','Khuda-e-Sukhan','خدای سخن'),('بابائے اُردو','Baba-e-Urdu','بابای اردو'),('بلبلِ ہند','Bulbul-e-Hind','بلبل هند'),('اُردو غزل کا باوا آدم','the Adam of the Urdu ghazal','د اردو غزل بابا آدم')])
M('(ہ) غزل کے تمام اشعار کا ............ مفہوم ہوتا ہے۔','(e) All the couplets of a ghazal have ............ meaning.','(ه) د غزل ټولو شعرونو ............ مفهوم وي.',[('الگ الگ','separate','جلا جلا'),('ایک','one','یو'),('متضاد','opposite','متضاد'),('مبارک','blessed','مبارک')])
M('(و) میرؔ کی غزل کا بنیادی موضوع ............ ہے۔','(f) The basic subject of Mir’s ghazal is ............','(و) د میر د غزل بنسټیز موضوع ............ ده.',[('غم','grief','غم'),('شک','doubt','شک'),('خوشی','joy','خوښي'),('حُسن','beauty','حسن')])
F.done()
s['sourceNote']='Printed page 163 (scan 170): “Mashq” title and question 1 with six multiple-choice items (الف–و), each with four options printed with blue bullets. The remaining questions follow on the next page.'+NOTE
s['vocabulary']={}
save(s)
