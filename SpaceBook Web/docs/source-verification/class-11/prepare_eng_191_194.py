from enghelp import *
c=cell
U='u20'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
RC='eng11-u20-rc'; WEX='eng11-u20-writing'
# ---------- scan 191 (printed 182) ----------
s=page(191,U,'182','Glossary (end) · Reading Comprehension','فرہنگ (اختتام) · مطالعے کا فہم','لغتنامه (پای) · د لوست پوهه','glossary-rc')
F=Flow(s)
G=[('outfit','a set of clothes worn together, especially for a particular occasion or purpose','کپڑوں کا مجموعہ جو ایک ساتھ پہنا جائے، خاص طور پر کسی خاص موقع یا مقصد کے لیے','د جامو یو سیټ چې یو ځای اغوستل کېږي، په ځانګړې توګه د ځانګړي مناسبت یا موخې لپاره','لباس','د جامو سیټ'),
('overdressing','to dress too warmly, too showily, or too formally for the occasion.','موقع کے لیے بہت گرم، بہت بھڑکیلے یا بہت رسمی لباس پہننا۔','د مناسبت لپاره ډېرې ګرمې، ډېرې ښکارندویه یا ډېرې رسمي جامې اغوستل.','حد سے زیادہ بن ٹھن کر آنا','ډېره سینګار کول'),
('put on spot','if you put someone on the spot, you cause them embarrassment or difficulty by forcing them at that moment to answer a difficult question or make an important decision','اگر آپ کسی کو مشکل میں ڈال دیں تو آپ اسے اسی لمحے کوئی مشکل سوال حل کرنے یا اہم فیصلہ کرنے پر مجبور کر کے شرمندگی یا دشواری میں ڈالتے ہیں','که تاسو یو څوک په ستونزه کې واچوئ نو تاسو هغه په هماغه شېبه د یوې ستونزمنې پوښتنې ځواب یا مهم پرېکړې ته اړ کولو سره شرم یا ستونزې ته اړ کوئ','مشکل میں ڈالنا','په ستونزه کې اچول'),
('simulation','imitation of a situation or process','کسی صورتِ حال یا عمل کی نقل','د یو حالت یا بهیر نقل','نقل','نقل'),
('sparkle','shine brightly with flashes of light','روشنی کی چمک کے ساتھ تیز چمکنا','د رڼا د ځلا سره په تېزۍ ځلېدل','چمکنا','ځلېدل')]
s['tables']=[table('Glossary (continued)','فرہنگ (جاری)','لغتنامه (دوام)',[c('Word','لفظ','کلمه'),c('Meaning','معنی','معنا')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
F.tb(0)
for w,m,mu,mp,uw,pw in G: V[w]=dict(ur=uw,ps=pw)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.',RC,'exercise')
RQ=[('What is job interview?','جاب انٹرویو کیا ہے؟','د دندې مرکه څه ده؟'),
('Describe some types of job interviews and their purposes.','جاب انٹرویو کی کچھ اقسام اور ان کے مقاصد بیان کریں۔','د دندې د مرکو ځینې ډولونه او د هغو موخې بیان کړئ.'),
('How should one dress for job interviews?','جاب انٹرویو کے لیے کسی کو کیسا لباس پہننا چاہیے؟','د دندې مرکو لپاره باید یو څوک څنګه جامې واغوندي؟'),
('What is the impact of dressing on interview?','انٹرویو پر لباس کا کیا اثر ہوتا ہے؟','پر مرکه د جامو اغېز څه دی؟'),
('How can a person keep nerves calm during interviews?','انٹرویو کے دوران کوئی شخص اپنے اعصاب کو کیسے پرسکون رکھ سکتا ہے؟','یو کس د مرکو پر مهال خپل اعصاب څنګه آرام ساتلی شي؟'),
('What is the importance of first five minutes in job interview? How should the opening of the interview be planned ?','جاب انٹرویو میں پہلے پانچ منٹ کی کیا اہمیت ہے؟ انٹرویو کے آغاز کی منصوبہ بندی کیسے کی جانی چاہیے؟','د دندې په مرکه کې د لومړیو پنځو دقیقو اهمیت څه دی؟ د مرکې پیل څنګه پلان شي؟'),
('What is the role of self confidence in job interview and how can it be boosted?','جاب انٹرویو میں خود اعتمادی کا کیا کردار ہے اور اسے کیسے بڑھایا جا سکتا ہے؟','د دندې په مرکه کې د ځان‌باور رول څه دی او دا څنګه زیاتېدای شي؟'),
('What type of text is used in the lesson ‘How To Take Job Interview’? Illustrate it with examples from the text.','سبق ‘جاب انٹرویو کیسے دیں’ میں کس قسم کا متن استعمال ہوا ہے؟ متن سے مثالوں کے ذریعے اس کی وضاحت کریں۔','په درس ‘د دندې مرکه څنګه ورکړو’ کې کوم ډول متن کارول شوی؟ د متن له بېلګو سره یې روښانه کړئ.'),
('What is the central idea of the lesson ‘How To Take Job Interview ’?','سبق ‘جاب انٹرویو کیسے دیں’ کا مرکزی خیال کیا ہے؟','د درس ‘د دندې مرکه څنګه ورکړو’ مرکزي مفکوره څه ده؟'),
('What is mock interview? How can it be helpful for preparation of job interviews?','نقلی (mock) انٹرویو کیا ہے؟ یہ جاب انٹرویو کی تیاری کے لیے کیسے مددگار ہو سکتا ہے؟','مصنوعي (mock) مرکه څه ده؟ دا د دندې د مرکو د چمتو کولو لپاره څنګه ګټوره کېدای شي؟')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',RC,'exercise')
F.done()
s['sourceNote']='Printed page 182. The page continues the glossary table from the previous page (5 rows; the first row is cut at the top edge) and then has a pink "Reading Comprehension" banner with ten questions. The right edge of the scan clips a few line ends (e.g. "Interview\'?", "it"). The Urdu and Pashto columns of the glossary are added by us. Border lines, a pink corner flag and the "Whatsapp" strip are excluded. The page number 182 is printed in a diamond at the foot.'
s['vocabulary']=V
save(s)
# ---------- scan 192 (printed 183) ----------
s=page(192,U,'183','Writing Suggestions: comprehending job advertisements (A)','لکھنے کی تجاویز: ملازمت کے اشتہارات کو سمجھنا (الف)','د لیکلو وړاندیزونه: د دندې اعلانونو پوهېدل (الف)','writing-job-ad-a')
F=Flow(s)
H(s,'wh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
H(s,'cj','Comprehending Job Advertisements','ملازمت کے اشتہارات کو سمجھنا','د دندې اعلانونو پوهېدل',tab='writing')
H(s,'ja','Job Advertisements (A)','ملازمت کے اشتہارات (الف)','د دندې اعلانونه (الف)',tab='writing')
H(s,'ti','TEACHING ASSISTANT.','ٹیچنگ اسسٹنٹ۔','د ښوونکي مرستیال.',tab='writing')
for k,a,b,d in [('p1','Required from: November 2002 - Term time only, four mornings weekly','درکار از: نومبر 2002 - صرف سمسٹر کے دوران، ہفتے میں چار صبحیں','اړتیا له: نومبر ۲۰۰۲ - یوازې د سمستر پر مهال، په اونۍ کې څلور سهارونه'),
('p2','We are looking for a caring and enthusiastic teaching assistant to work in a Y3 classroom to work alongside children who require extra support. Experience of working with children is essential. You will be part of a friendly and committed staff team and we shall offer opportunities to help you develop professionally.','ہم ایک ہمدرد اور پرجوش ٹیچنگ اسسٹنٹ کی تلاش میں ہیں جو Y3 کلاس روم میں ان بچوں کے ساتھ کام کرے جنہیں اضافی مدد کی ضرورت ہو۔ بچوں کے ساتھ کام کرنے کا تجربہ ضروری ہے۔ آپ ایک دوستانہ اور پرعزم عملے کی ٹیم کا حصہ ہوں گے اور ہم آپ کو پیشہ ورانہ طور پر ترقی کرنے میں مدد کے مواقع فراہم کریں گے۔','موږ یو مهربان او په ولوله ډک د ښوونکي مرستیال لټوو چې په Y3 ټولګي کې له هغو ماشومانو سره کار وکړي چې اضافي مرستې ته اړتیا لري. له ماشومانو سره د کار تجربه اړینه ده. تاسو به د یوې دوستانه او ژمنې کارکوونکو ډلې برخه یاست او موږ به تاسو ته د مسلکي وده کولو لپاره فرصتونه برابر کړو.'),
('p3','Please telephone Ms. Maria, School Secretary for further details. Visits are welcomed. Letters of applicant and CV with the details of 2 references should be sent to Ms. Laila, Head teacher by October 14.','مزید تفصیلات کے لیے براہِ کرم اسکول سیکرٹری محترمہ ماریہ کو فون کریں۔ دورے کا خیر مقدم ہے۔ درخواست کے خطوط اور 2 حوالوں کی تفصیلات کے ساتھ CV ہیڈ ٹیچر محترمہ لیلیٰ کو 14 اکتوبر تک بھیجے جائیں۔','د نورو تفصیلاتو لپاره مهرباني وکړئ د ښوونځي منشي میرمن ماریا ته زنګ ووهئ. لیدنې ته ښه راغلاست. د غوښتونکي لیکونه او د ۲ حوالو د جزئیاتو سره CV باید د مشرې ښوونکې میرمن لیلا ته تر ۱۴ اکتوبر پورې ولېږل شي.'),
('pr','Principal','پرنسپل','پرنسپل'),
('sc','St. Michael’s Junior School','سینٹ مائیکلز جونیئر اسکول','سینټ مایکلز جونیر ښوونځی'),
('ad','Circular Road, Peshawar.','سرکلر روڈ، پشاور۔','سرکلر روډ، پېښور.')]:
    add(s,k,a,b,d,tab='writing')
F.done()
s['sourceNote']='Printed page 183. Pink banner "Writing Suggestions", the sub-heading "Comprehending Job Advertisements", the heading "Job Advertisements (A)" and a framed pink advertisement for a Teaching Assistant at St. Michael’s Junior School, Circular Road, Peshawar (the text of a fictional/specimen advertisement printed in the textbook; the printed text reads "Letters of applicant" and "Ms. Maria," with a comma attached to "Ms. Maria,"; kept as printed). Border lines, a pink corner flag, the watermark and coloured binding strips at the foot are excluded. The page number 183 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 193 (printed 184) ----------
s=page(193,U,'184','Writing Suggestions: job advertisements (B)','لکھنے کی تجاویز: ملازمت کے اشتہارات (ب)','د لیکلو وړاندیزونه: د دندې اعلانونه (ب)','writing-job-ad-b')
F=Flow(s)
H(s,'jb','Job Advertisements (B)','ملازمت کے اشتہارات (ب)','د دندې اعلانونه (ب)',tab='writing')
H(s,'ti','CONTRACTS MANAGER','کنٹریکٹس مینیجر','د قراردادونو مدیر',tab='writing')
for k,a,b,d in [('p1','KP Builders has been providing a quality service for over 25 years, specializing in refurbishment and major alterations for Local Authorities & Housing Associations in the Capital Territory, Islamabad.','کے پی بلڈرز 25 سال سے زائد عرصے سے معیاری خدمات فراہم کر رہا ہے، اور دارالحکومت اسلام آباد میں مقامی حکام اور ہاؤسنگ ایسوسی ایشنز کے لیے تزئین و آرائش اور بڑی تبدیلیوں میں مہارت رکھتا ہے۔','کې پي بلډرز له ۲۵ کلونو ډېر وخت راهیسې د کیفیت لرونکې خدمتونه برابروي او په پلازمېنه اسلام‌آباد کې د سیمه‌ییزو چارواکو او کورجوړونې ټولنو لپاره په نوي کولو او لویو بدلونونو کې تخصص لري.'),
('p2','Our continued success is due to the commitment of our dedicated team of professionals. We are looking for an experienced Contracts Manager, able to demonstrate the drive necessary to lead a team of Surveyors, Site Managers and Trades, reporting to the Contracts Director.','ہماری مسلسل کامیابی ہمارے مخلص پیشہ ور افراد کی ٹیم کی لگن کی وجہ سے ہے۔ ہم ایک تجربہ کار کنٹریکٹس مینیجر کی تلاش میں ہیں، جو سروے کرنے والوں، سائٹ مینیجرز اور ہنر مندوں کی ٹیم کی قیادت کے لیے ضروری جذبہ دکھا سکے اور کنٹریکٹس ڈائریکٹر کو رپورٹ کرے۔','زموږ دوامداره بریا زموږ د ځانګړو مسلکي کسانو د ډلې د ژمنې له امله ده. موږ یو تجربه لرونکی د قراردادونو مدیر لټوو، چې د سروې کوونکو، ساحې مدیرانو او مسلکیانو د ډلې د مشرۍ لپاره اړین هڅه وښيي او د قراردادونو رئیس ته راپور ورکړي.'),
('p3','You will be responsible for controlling all projects using the company’s management control process and our fully computerized ICT system.','آپ کمپنی کے انتظامی کنٹرول کے عمل اور ہمارے مکمل کمپیوٹرائزڈ ICT نظام کو استعمال کرتے ہوئے تمام منصوبوں کو کنٹرول کرنے کے ذمہ دار ہوں گے۔','تاسو به د شرکت د مدیریتي کنټرول بهیر او زموږ بشپړ کمپیوټري ICT سیستم په کارولو سره د ټولو پروژو د کنټرول مسؤل یاست.'),
('p4','This is a great opportunity for an individual with a proven track record of delivering projects on time & within budget whilst able to maintain our mission statement of ‘Building Quality on Time’.','یہ ایک ایسے فرد کے لیے بہترین موقع ہے جس کا وقت پر اور بجٹ کے اندر منصوبے مکمل کرنے کا ثابت شدہ ریکارڈ ہو اور جو ہمارے مشن اسٹیٹمنٹ ‘وقت پر معیار کی تعمیر’ کو برقرار رکھ سکے۔','دا د هغه کس لپاره یوه ستره فرصت ده چې د پروژو په وخت او په بودجه کې د بشپړولو ثابت شوی ریکارډ لري او د خپل ماموریت بیان ‘په وخت کې د کیفیت جوړول’ ساتلای شي.'),
('p5','If you feel this is the challenge for you, please apply in writing with a full CV to:','اگر آپ محسوس کرتے ہیں کہ یہ آپ کے لیے چیلنج ہے تو براہِ کرم مکمل CV کے ساتھ تحریری درخواست دیں:','که تاسو احساسوئ چې دا ستاسو لپاره ننګونه ده نو مهرباني وکړئ د بشپړ CV سره په لیکلې بڼه غوښتنه وکړئ:'),
('a1','Mr. Ibrar Khan','جناب ابرار خان','ښاغلی ابرار خان'),('a2','KP Builders,','کے پی بلڈرز،','کې پي بلډرز،'),('a3','Blue Area, Islamabad','بلیو ایریا، اسلام آباد','بلیو ایریا، اسلام‌آباد')]:
    add(s,k,a,b,d,tab='writing')
F.done()
s['sourceNote']='Printed page 184. The heading "Job Advertisements (B)" and a framed pink advertisement for a Contracts Manager at KP Builders, Blue Area, Islamabad (the text of a specimen advertisement printed in the textbook; the title "CONTRACTS MANAGER" is underlined in print). Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded. The page number 184 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 194 (printed 185) ----------
s=page(194,U,'185','Comprehension questions · Specimen advertisement','فہم کے سوالات · نمونہ اشتہار','د پوهې پوښتنې · نمونه اعلان','comprehension-ad')
F=Flow(s)
H(s,'ch','Comprehension Questions','فہم کے سوالات','د پوهې پوښتنې',tab='writing')
Qn(s,'q1','1. Read through the advertisement labelled (A) again and make a list of all the words and expressions used to describe:','1. اشتہار (الف) کو دوبارہ پڑھیں اور ان تمام الفاظ اور اظہارات کی فہرست بنائیں جو بیان کرنے کے لیے استعمال ہوئے ہیں:','۱. اعلان (الف) بیا ولولئ او د ټولو هغو کلمو او بیانونو لیست جوړ کړئ چې د بیانولو لپاره کارول شوي:',WEX,'writing')
Qn(s,'q1a','a) The job requirements','الف) ملازمت کے تقاضے','الف) د دندې اړتیاوې',WEX,'writing')
Qn(s,'q1b','b) The benefits offered by the job.','ب) ملازمت کی طرف سے پیش کردہ فوائد۔','ب) د دندې لخوا وړاندې شوې ګټې.',WEX,'writing')
Qn(s,'q2','2. Look at the job advertisement labelled (B) and answer the questions.','2. اشتہار (ب) کو دیکھیں اور سوالات کے جواب دیں۔','۲. اعلان (ب) وګورئ او پوښتنو ته ځواب ورکړئ.',WEX,'writing')
for l,a,b,d in [('a','Who placed the job advertisement in the newspaper?','ملازمت کا اشتہار اخبار میں کس نے دیا؟','د دندې اعلان په ورځپاڼه کې چا وکېښود؟'),('b','What job is being offered and which sector?','کون سی ملازمت پیش کی جا رہی ہے اور کس شعبے میں؟','کومه دنده وړاندې کېږي او په کومه برخه کې؟'),('c','What is required for the job?','ملازمت کے لیے کیا درکار ہے؟','د دندې لپاره څه اړین دي؟'),('d','Where will the successful candidate work?','کامیاب امیدوار کہاں کام کرے گا؟','بریالی نوماند به چېرته کار کوي؟')]:
    Qn(s,f'q2{l}',f'{l}. {a}',f'{l}. {b}',f'{l}. {d}',WEX,'writing')
H(s,'ad','Garrison Academy Kharian Cantt (Army Public School & College System) — TEACHING STAFF REQUIRED','گیریژن اکیڈمی کھاریاں چھاؤنی (آرمی پبلک اسکول اینڈ کالج سسٹم) — تدریسی عملہ درکار ہے','ګیریزن اکاډمي خاریان چاونۍ (د اردو عامه ښوونځي او کالج سیسټم) — د ښوونې کارکوونکي په کار دي',tab='writing')
add(s,'ai','Following qualified and committed teaching staff is required for the under mentioned positions:-','درج ذیل اہل اور پرعزم تدریسی عملہ مندرجہ ذیل عہدوں کے لیے درکار ہے:-','لاندې وړ او ژمن د ښوونې کارکوونکي لاندې یاد شوو ځایونو لپاره په کار دي:-',tab='writing')
s['tables']=[table('Teaching staff required','درکار تدریسی عملہ','د ښوونې کارکوونکي په کار دي',[c('Ser','نمبر شمار','لړ'),c('Name of Post','عہدے کا نام','د ځای نوم'),c('Qualification / Experience','تعلیمی قابلیت / تجربہ','وړتیا / تجربه')],[
[c('01','01','۰۱'),c('Arabic MA (Arabic) or equal (Male/ Female)','عربی ایم اے (عربی) یا مساوی (مرد/خاتون)','عربي ایم اے (عربي) یا برابر (نارینه/ښځینه)'),c('Master in Arabic with minimum three years experience','عربی میں ماسٹر کم از کم تین سال کے تجربے کے ساتھ','په عربي کې ماسټر لږ تر لږه درې کلن تجربې سره')],
[c('02','02','۰۲'),c('Career Counselor/School Counselor','کیریئر کونسلر/اسکول کونسلر','د مسلک مشاور/د ښوونځي مشاور'),c('MIT from reputed institution','معتبر ادارے سے MIT','له معتبر ادارې څخه MIT')],
[c('03','03','۰۳'),c('English','انگریزی','انګلیسي'),c('MA English','ایم اے انگریزی','ایم اے انګلیسي')],
[c('04','04','۰۴'),c('Urdu','اردو','اردو'),c('MA Urdu','ایم اے اردو','ایم اے اردو')],
[c('05','05','۰۵'),c('Maths','ریاضی','ریاضي'),c('MSc Maths','ایم ایس سی ریاضی','ایم ایس سي ریاضي')],
[c('06','06','۰۶'),c('Physics','طبیعیات','فزیک'),c('MSc Phy','ایم ایس سی فزکس','ایم ایس سي فزیک')],
[c('07','07','۰۷'),c('Chemistry','کیمیا','کیمیا'),c('MSc Chem','ایم ایس سی کیمسٹری','ایم ایس سي کیمیا')]],tab='writing')]
F.tb(0)
for k,a,b,d in [('b1','Attractive salary package commensurate with experience and qualifications. Pay package has been recently revised. Candidates having experience of minimum three years of teaching in well reputed English medium institutions will be given preference.','تجربے اور قابلیت کے مطابق پرکشش تنخواہ کا پیکیج۔ تنخواہ کا پیکیج حال ہی میں نظرِ ثانی شدہ ہے۔ معروف انگلش میڈیم اداروں میں کم از کم تین سال تدریس کا تجربہ رکھنے والے امیدواروں کو ترجیح دی جائے گی۔','د تجربې او وړتیا سره سم زړه‌پورې د معاش کڅوړه. د معاش کڅوړه په دې وروستیو کې بیا کتل شوې ده. هغه نوماندان چې په ښه پېژندل شویو انګلیسي منځنیو بنسټونو کې لږ تر لږه درې کلن د تدریس تجربه لري ترجیح به ورکړل شي.'),
('b2','Keeping in view experience and qualification, special grade may be offered to the deserving candidates.','تجربے اور قابلیت کو مدنظر رکھتے ہوئے مستحق امیدواروں کو خصوصی گریڈ پیش کیا جا سکتا ہے۔','د تجربې او وړتیا په پام کې نیولو سره وړ نوماندانو ته ځانګړی ګرېډ وړاندې کېدای شي.'),
('b3','Atmosphere and working conditions of GAK are excellent. Additional benefits/ perks and privileges including medical treatment, membership of club, loan and board & lodging facilities are also provided. Intensive training for teachers is conducted free of cost under APSACS.','جی اے کے کا ماحول اور کام کی شرائط بہترین ہیں۔ طبی علاج، کلب کی رکنیت، قرض اور قیام و طعام کی سہولتوں سمیت اضافی فوائد/مراعات اور اعزازات بھی فراہم کیے جاتے ہیں۔ APSACS کے تحت اساتذہ کے لیے مفت گہری تربیت کرائی جاتی ہے۔','د GAK چاپېریال او د کار شرایط ډېر ښه دي. اضافي ګټې/امتیازات او مراعات په ګډون د طبي درملنې، د کلب غړیتوب، پور او استوګنې او خوړو اسانتیاوې هم برابرېږي. د APSACS لاندې ښوونکو ته په وړیا ډول ژوره روزنه ورکول کېږي.'),
('b4','Semi-furnished single accommodation is offered in a safe and pollution free environment.','محفوظ اور آلودگی سے پاک ماحول میں نیم فرنشڈ سنگل رہائش پیش کی جاتی ہے۔','په خوندي او له ککړتیا پاک چاپېریال کې نیمه سمبال یوازېنی استوګنځی وړاندې کېږي.'),
('b5','Complete CVs with photographs and a copy of CNIC to be forwarded to Principal Garrison Academy Kharian Cantt within 10 days of publication of the advertisement.','مکمل CV تصاویر اور CNIC کی کاپی کے ساتھ اشتہار کی اشاعت کے 10 دن کے اندر پرنسپل گیریژن اکیڈمی کھاریاں چھاؤنی کو بھیجے جائیں۔','بشپړ CV د انځورونو او د CNIC د کاپي سره د اعلان د خپرېدو په ۱۰ ورځو کې د ګیریزن اکاډمي خاریان چاونۍ مشر ته ولېږل شي.'),
('pp','Principal (Prof Arjasab Khan Zafar) — Tel: 053-9240263, 053-59-36325','پرنسپل (پروفیسر ارجسب خان ظفر) — فون: 053-9240263، 053-59-36325','پرنسپل (پروفیسور ارجسب خان ظفر) — تلیفون: 053-9240263, 053-59-36325'),
('sm','(A sample of an original job advertisement from a National Daily)','(ایک قومی روزنامے سے اصل ملازمت کے اشتہار کا نمونہ)','(د یوې ملي ورځپاڼې څخه د اصلي دندې د اعلان نمونه)')]:
    add(s,k,a,b,d,tab='writing')
F.done()
s['sourceNote']='Printed page 185. "Comprehension Questions" with questions 1 and 2 (sub-parts a–b and a–d), followed by a framed, small-print advertisement ("A sample of an original job advertisement from a National Daily") for teaching staff at Garrison Academy Kharian Cantt (Army Public School & College System): a 7-row table (Ser / Name of Post / Qualification-Experience), five bullets and the principal\'s name and telephone numbers, reproduced as printed in the textbook. The small print is read at reduced resolution; a few characters in the bullets are indistinct and are read from context. The Urdu and Pashto texts are translations by us. A binding strip and the "Whatsapp" strip are excluded. Border lines and pink corner flags are excluded. The page number 185 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
