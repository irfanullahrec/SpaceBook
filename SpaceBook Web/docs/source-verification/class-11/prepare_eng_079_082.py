from enghelp import *
c=cell
U='u07'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
def layout_svg():
    W,Hh=560,520
    o='<rect x="150" y="20" width="400" height="470" fill="none" stroke="#bbb"/>'
    o+='<rect x="160" y="30" width="190" height="75" fill="none" stroke="#999"/>'
    o+='<rect x="160" y="120" width="190" height="24" fill="none" stroke="#999"/>'
    o+='<rect x="160" y="156" width="190" height="62" fill="none" stroke="#999"/>'
    o+=T(165,247,'Dear',13,'start')+'<line x1="195" y1="251" x2="300" y2="251" stroke="#111"/>'+T(303,247,',',13,'start')
    o+='<rect x="160" y="268" width="380" height="24" fill="none" stroke="#999"/>'
    o+='<rect x="160" y="304" width="380" height="110" fill="none" stroke="#999"/>'
    o+=T(165,436,'Yours',13,'start')+'<line x1="205" y1="440" x2="310" y2="440" stroke="#111"/>'+T(313,436,',',13,'start')
    o+='<rect x="160" y="450" width="190" height="22" fill="none" stroke="#999"/>'
    o+='<rect x="160" y="478" width="190" height="22" fill="none" stroke="#999"/>'
    o+=T(80,18,'Your address',11,'start')+T(380,18,'Date',11,'start')
    o+=T(5,140,'Name, job title, and',11,'start')+T(5,154,'address of the person',11,'start')+T(5,168,'you are writing to.',11,'start')
    o+=T(5,232,'Insert Sir/Madam or',11,'start')+T(5,246,'Surname/Name with',11,'start')+T(5,260,'title (Mr., Ms., Mrs.,',11,'start')+T(5,274,'Dr., etc.)',11,'start')
    o+=T(5,284,'Topic sentence —',11,'start')+T(5,298,'what is the letter',11,'start')+T(5,312,'about',11,'start')
    o+=T(5,356,'Main body of',13,'start')+T(5,372,'letter',13,'start')
    o+=T(5,420,'Yours sincerely if you',11,'start')+T(5,434,'know the recipient’s',11,'start')+T(5,448,'name; Yours',11,'start')+T(5,462,'faithfully if you do',11,'start')+T(5,476,'not.',11,'start')
    o+=T(5,492,'Signature',13,'start')+T(5,512,'Your name',11,'start')
    o=o.replace('<text x="5" y="232"','<text x="5" y="200"').replace('<text x="5" y="246"','<text x="5" y="214"').replace('<text x="5" y="260"','<text x="5" y="228"').replace('<text x="5" y="274"','<text x="5" y="242"')
    return svg(W,Hh,'Formal letter layout: your address and date at the top, the address of the recipient, the salutation Dear …, a topic sentence, the main body of the letter, the closing Yours …, the signature and your name',o)
# ---------- scan 79 (printed 70) ----------
s=page(79,U,'70','Glossary · Reading Comprehension','فرہنگ · مطالعے کا فہم','لغتنامه · د لوست پوهه','glossary-rc')
F=Flow(s)
H(s,'gh','Glossary','فرہنگ','لغتنامه',tab='glossary')
G=[('career','an occupation undertaken for a significant period of a person’s life and with opportunities for progress','کوئی پیشہ جو انسان کی زندگی کے ایک اہم عرصے کے لیے اختیار کیا جائے اور جس میں ترقی کے مواقع ہوں','یو مسلک چې د یو کس د ژوند د یوې مهمې مودې لپاره غوره کېږي او د پرمختګ فرصتونه لري','پیشہ','مسلک'),
('montessori','a system of education for young children that seeks to develop natural interests and activities rather than use formal teaching methods','چھوٹے بچوں کے لیے تعلیم کا ایک نظام جو رسمی تدریسی طریقے استعمال کرنے کے بجائے فطری دلچسپیوں اور سرگرمیوں کو فروغ دینے کی کوشش کرتا ہے','د کوچنیو ماشومانو لپاره د زده کړې یو سیستم چې د رسمي ښوونې طریقو پر ځای طبیعي ګټې او فعالیتونه ودې کولو هڅه کوي','مونٹیسری','مونټیسري'),
('motives','a reason for doing something','کسی کام کو کرنے کی وجہ','د یو کار د کولو دلیل','محرکات','انګېزې'),
('numeracy','the ability to understand and work with numbers','اعداد کو سمجھنے اور ان کے ساتھ کام کرنے کی صلاحیت','د شمېرو د پوهېدو او له هغو سره د کار کولو وړتیا','عددی صلاحیت','شمېرپوهه'),
('pediatric','relating to the branch of medicine dealing with children and their diseases','طب کی اس شاخ سے متعلق جو بچوں اور ان کی بیماریوں سے متعلق ہے','د طب هغې څانګې پورې اړوند چې له ماشومانو او د هغوی له ناروغیو سره سروکار لري','اطفال سے متعلق','د ماشومانو')	,
('pragmatic','dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations','معاملات کو سمجھداری اور حقیقت پسندی سے نمٹانا اس طرح کہ نظریاتی کے بجائے عملی غور و فکر پر مبنی ہو','له شیانو سره په هوښیارۍ او واقعیت‌پالنې معامله کول په داسې ډول چې په نظري پر ځای عملي ملاحظاتو والړ وي','عملی','عملي'),
('reflect','think deeply or carefully about','گہرائی یا احتیاط سے سوچنا','په ژوروالي یا احتیاط فکر کول','غور کرنا','فکر کول'),
('retrospection','the action of looking back on or reviewing past events or situations, especially those in one’s own life','ماضی کے واقعات یا حالات، خاص طور پر اپنی زندگی کے، کو پیچھے مڑ کر دیکھنے یا ان کا جائزہ لینے کا عمل','د تېرو پېښو یا حالاتو، په ځانګړې توګه د خپل ژوند، شاته کتل یا بیاکتنه','ماضی بینی','شاته کتنه')]
s['tables']=[table('Glossary','فرہنگ','لغتنامه',[c('WORDS','الفاظ','کلمې'),c('MEANING','معنی','معنا')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
for w,m,mu,mp,uw,pw in G: V[w]=dict(ur=uw,ps=pw)
H(s,'rc','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u07-rc','exercise')
RQ=[('What is the dominant theme of the letter?','خط کا غالب موضوع کیا ہے؟','د لیک غالب موضوع څه دی؟'),
("Why doesn’t the career expert mention any specific profession as career?",'کیریئر ماہر کسی مخصوص پیشے کو بطور کیریئر کیوں بیان نہیں کرتا؟','د مسلک پوه ولې کوم ځانګړی مسلک د مسلک په توګه نه یادوي؟'),
('Why is the decision of choice of career considered the toughest? Give examples from the text of the letter.','پیشے کے انتخاب کا فیصلہ سب سے مشکل کیوں سمجھا جاتا ہے؟ خط کے متن سے مثالیں دیں۔','د مسلک د غوراوي پرېکړه ولې تر ټولو ستونزمنه ګڼل کېږي؟ د لیک له متن څخه بېلګې ورکړئ.'),
('What is self-assessment? How far is it helpful in the choice of career?','خود جائزہ کیا ہے؟ یہ پیشے کے انتخاب میں کس حد تک مددگار ہے؟','ځان‌ارزونه څه ده؟ دا د مسلک په غوراوي کې تر کومې کچې ګټوره ده؟'),
('Summarize the text of the lesson and extract the main points of the process of career choice. Now transfer the salient points of the process of career choice into flow chart and critically analyze the process.','سبق کے متن کا خلاصہ کریں اور پیشے کے انتخاب کے عمل کے اہم نکات نکالیں۔ اب پیشے کے انتخاب کے عمل کے نمایاں نکات کو بہاؤ کے چارٹ میں منتقل کریں اور عمل کا تنقیدی تجزیہ کریں۔','د درس متن لنډ کړئ او د مسلک د غوراوي د پروسې مهم ټکي را وباسئ. اوس د مسلک د غوراوي د پروسې مهم ټکي په فلوچارټ کې ولیږدوئ او پروسه په انتقادي ډول تحلیل کړئ.'),
('Evaluate the steps of career choice and tell how effective or otherwise they are for your choice of career.','پیشے کے انتخاب کے مراحل کا جائزہ لیں اور بتائیں کہ آپ کے پیشے کے انتخاب کے لیے وہ کتنے مؤثر ہیں یا نہیں۔','د مسلک د غوراوي مرحلې ارزونه وکړئ او ووايئ چې ستاسو د مسلک د غوراوي لپاره دوی څومره اغېزمن دي یا نه.')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u07-rc','exercise')
build(s,79,['gh','T:0','rc','ans']+[f'q{i}' for i in range(1,7)],[])
s['vocabulary']=V
s['sourceNote']='Printed page 70. A pink "Glossary" banner, a two-column table (WORDS / MEANING) and a pink "Reading Comprehension" banner. The right edge of the photograph clips the last letters of the meaning column and of questions 2, 3, 5 and 6 (for example "perio[d] of", "seeks [to]", "form[al]", "children an[d]", "tha[t is]", "event[s] [or]", "of th[e]", "process o[f]", "otherwise[ ]"); the words are read from context. The page number 70 is printed in a diamond at the foot. Border lines, pink corner flags and the watermark are excluded. The Urdu and Pashto columns of the glossary are added by us.'
save(s)
# ---------- scan 80 (printed 71) ----------
V={}
s=page(80,U,'71','Writing Suggestions: Letter Writing (start)','لکھنے کی تجاویز: خط نویسی (آغاز)','د لیکلو وړاندیزونه: لیک‌لیکنه (پیل)','letter-writing-1')
F=Flow(s)
H(s,'wsh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
H(s,'lw','Letter Writing','خط نویسی','لیک‌لیکنه',tab='writing')
H(s,'wf','Writing a Formal Letter','رسمی خط لکھنا','رسمي لیک لیکل',tab='writing')
H(s,'rf','Rules for Writing Formal Letters in English','انگریزی میں رسمی خطوط لکھنے کے اصول','په انګلیسي کې د رسمي لیکونو د لیکلو قواعد',tab='writing')
P=[('t1','In English there are a number of conventions that should be used when writing a formal or business letter. Furthermore, try to write as simply and as clearly as possible, and not to make the letter longer than necessary. Remember not to use informal language like contractions.','انگریزی میں رسمی یا کاروباری خط لکھتے وقت استعمال کرنے کے لیے بہت سے اصول ہیں۔ مزید یہ کہ جتنا ممکن ہو سادہ اور واضح لکھنے کی کوشش کریں، اور خط کو ضرورت سے زیادہ لمبا نہ کریں۔ یاد رکھیں کہ غیر رسمی زبان جیسے اختصارات استعمال نہ کریں۔','په انګلیسي کې د رسمي یا سوداګریز لیک د لیکلو پر مهال د کارولو لپاره ډېر دودونه شته. سربېره پردې، هڅه وکړئ تر هغه حده چې ممکنه وي ساده او روښانه ولیکئ، او لیک له اړتیا ډېر اوږد مه کړئ. یاد ولرئ چې غیر رسمي ژبه لکه لنډیزونه مه کاروئ.'),
('ah','Addresses:','پتے:','پتې:',dict(kind='heading')),
('a1','1) Your Address','1) آپ کا پتہ','1) ستاسو پته',dict(kind='heading')),
('t2','The return address (your address) should be written in the top left corner of the letter (avoid putting commas or full stops at the end of lines).','واپسی کا پتہ (آپ کا پتہ) خط کے اوپر بائیں کونے میں لکھا جانا چاہیے (لائنوں کے آخر میں کوما یا فل اسٹاپ لگانے سے گریز کریں)۔','د بېرته راتلو پته (ستاسو پته) باید د لیک په پورتنۍ کیڼ کونج کې ولیکل شي (د کرښو په پای کې کوما یا نقطې اچولو څخه ډډه وکړئ).'),
('dh','Date:','تاریخ:','نېټه:',dict(kind='heading')),
('t3','Write this after your address. Write the month as a word — 10th April 2010.','یہ اپنے پتے کے بعد لکھیں۔ مہینے کو لفظ کے طور پر لکھیں — 10 اپریل 2010۔','دا د خپلې پتې وروسته ولیکئ. میاشت د کلمې په توګه ولیکئ — د 2010 کال د اپرېل 10.'),
('a2','2) The Address of the person you are writing to','2) اس شخص کا پتہ جسے آپ لکھ رہے ہیں','2) د هغه کس پته چې تاسو ورته لیکئ',dict(kind='heading')),
('t4','The address should be written on the left, starting below your address.','پتہ بائیں طرف لکھا جانا چاہیے، آپ کے پتے کے نیچے سے شروع کر کے۔','پته باید په کیڼ لور ولیکل شي، ستاسو د پتې لاندې پیل کوي.'),
('sh','Salutation or greeting:','سلام یا آداب:','سلام یا هرکلی:',dict(kind='heading')),
('s1','1) Dear Sir or Madam,','1) محترم جناب یا محترمہ،','1) ګرانه ښاغلیه یا مېرمنې،',dict(kind='heading')),
('t5','If you do not know the name of the person you are writing to, use this. It is always advisable to try to find out a name (a comma is needed).','اگر آپ اس شخص کا نام نہیں جانتے جسے آپ لکھ رہے ہیں تو یہ استعمال کریں۔ نام معلوم کرنے کی کوشش کرنا ہمیشہ مناسب ہے (کوما کی ضرورت ہے)۔','که تاسو د هغه کس نوم نه پېژنئ چې ورته لیکئ نو دا وکاروئ. تل مناسب ده چې نوم موندلو هڅه وکړئ (کوما ته اړتیا ده).'),
('s2','2) Dear Mr. Abrar,','2) محترم مسٹر ابرار،','2) ګرانه ښاغلی ابرار،',dict(kind='heading')),
('t6','If you know the name, use the title (Mr., Mrs., Miss/Ms., Dr, etc.) and the surname only. If you are writing to a woman and do not know if she uses Mrs. or Miss, you can use Ms, which is used for both married and single women. (Note the comma after Mr. Abrar).','اگر آپ نام جانتے ہیں تو لقب (مسٹر، مسز، مس/محترمہ، ڈاکٹر وغیرہ) اور صرف خاندانی نام استعمال کریں۔ اگر آپ کسی خاتون کو لکھ رہے ہیں اور نہیں جانتے کہ وہ مسز یا مس استعمال کرتی ہے تو آپ Ms استعمال کر سکتے ہیں جو شادی شدہ اور غیر شادی شدہ دونوں خواتین کے لیے استعمال ہوتا ہے۔ (مسٹر ابرار کے بعد کوما نوٹ کریں)۔','که تاسو نوم پېژنئ نو لقب (ښاغلی، مېرمن، مس/ام‌ایس، ډاکټر او نور) او یوازې کورنی نوم وکاروئ. که تاسو یوې ښځې ته لیکئ او نه پوهېږئ چې هغه مېرمن یا مس کاروي نو تاسو Ms کارولای شئ چې د واده شویو او نه واده شویو دواړو ښځو لپاره کارېږي. (د ښاغلي ابرار وروسته کوما ته پام وکړئ).')]
for k,a,b,d,*m in P: add(s,k,a,b,d,tab='writing',**(m[0] if m else {}))
F.done()
s['sourceNote']='Printed page 71. Pink banner "Writing Suggestions" and bold headings "Letter Writing", "Writing a Formal Letter", "Rules for Writing Formal Letters in English", "Addresses:", "Date:", "Salutation or greeting:". The page number 71 is printed in a diamond at the foot. Border lines, pink corner flags, the watermark and the glued page edge at the top are excluded; a partial footer at the bottom edge is excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 81 (printed 72) ----------
s=page(81,U,'72','Letter Writing: ending a letter, how to write a formal letter','خط نویسی: خط کا اختتام، رسمی خط کیسے لکھیں','لیک‌لیکنه: د لیک پای، رسمي لیک څنګه ولیکو','letter-writing-2')
F=Flow(s)
P=[('eh','Ending a letter:','خط کا اختتام:','د لیک پای:',dict(kind='heading')),
('e1','1) Yours faithfully,','1) آپ کا وفادار،','1) ستاسو وفادار،',dict(kind='heading')),
('te1','If you begin your letter with ‘Dear Sir/Madam,’ end the letter this way.','اگر آپ اپنے خط کا آغاز ‘Dear Sir/Madam,’ سے کرتے ہیں تو خط کا اختتام اسی طرح کریں۔','که تاسو خپل لیک په ‘Dear Sir/Madam,’ پیل کوئ نو لیک په همدې ډول پای ته ورسوئ.',dict(sourceGap=dict(note='The right edge of the photograph clips the end of the line ("end the letter [this]").'))),
('e2','2) Yours sincerely,','2) آپ کا مخلص،','2) ستاسو مخلص،',dict(kind='heading')),
('te2','If you begin your letter with ‘Dear Mr. Abrar’, end the letter this way.','اگر آپ اپنے خط کا آغاز ‘Dear Mr. Abrar’ سے کرتے ہیں تو خط کا اختتام اسی طرح کریں۔','که تاسو خپل لیک په ‘Dear Mr. Abrar’ پیل کوئ نو لیک په همدې ډول پای ته ورسوئ.'),
('e3','3) Your signature','3) آپ کے دستخط','3) ستاسو لاسلیک',dict(kind='heading')),
('te3','Sign your name, and then print it underneath the signature. If you think the person you are writing to might not know whether you are a man or a woman, put your title in brackets after your name.','اپنے نام پر دستخط کریں، اور پھر اسے دستخط کے نیچے چھاپیں (صاف لکھیں)۔ اگر آپ کو لگتا ہے کہ جس شخص کو آپ لکھ رہے ہیں وہ شاید نہ جانتا ہو کہ آپ مرد ہیں یا عورت تو اپنے نام کے بعد قوسین میں اپنا لقب لکھیں۔','خپل نوم لاسلیک کړئ، او بیا یې د لاسلیک لاندې چاپ کړئ (په ښکاره ولیکئ). که تاسو فکر کوئ هغه کس چې ورته لیکئ ښايي نه پوهېږي چې تاسو نارینه یاست که ښځه نو خپل لقب د خپل نوم وروسته په قوس کې ولیکئ.',dict(sourceGap=dict(note='The right edge of the photograph clips some words of the lines ("If y[ou]", "you ar[e]"); the words are read from context.'))),
('hh','How to Write a Formal Letter','رسمی خط کیسے لکھیں','رسمي لیک څنګه ولیکو',dict(kind='heading')),
('fh','First paragraph','پہلا پیراگراف','لومړی پراګراف',dict(kind='heading')),
('tf','The first paragraph should be short and should state the purpose of the letter — to make an enquiry, complaint, request something, etc.','پہلا پیراگراف مختصر ہونا چاہیے اور خط کا مقصد بیان کرنا چاہیے — انکوائری، شکایت یا کوئی درخواست کرنا وغیرہ۔','لومړی پراګراف باید لنډ وي او د لیک موخه بیان کړي — پوښتنه کول، شکایت یا یوه غوښتنه کول او نور.'),
('mh','Middle Paragraph(s)','درمیانی پیراگراف','منځني پراګراف(ونه)',dict(kind='heading')),
('tm','The paragraph or paragraphs in the middle of the letter should contain the relevant information behind the writing of the letter. Most letters in English are not very long, so keep the information to the essentials and concentrate on organizing it in a clear and logical manner rather than expanding too much.','خط کے درمیان کا پیراگراف یا پیراگراف خط لکھنے کے پیچھے متعلقہ معلومات پر مشتمل ہونے چاہییں۔ انگریزی میں زیادہ تر خطوط بہت لمبے نہیں ہوتے، اس لیے معلومات کو بنیادی باتوں تک محدود رکھیں اور بہت زیادہ پھیلانے کے بجائے اسے واضح اور منطقی انداز میں ترتیب دینے پر توجہ دیں۔','د لیک په منځ کې پراګراف یا پراګرافونه باید د لیک د لیکلو شا اړونده معلومات ولري. په انګلیسي کې ډېر لیکونه ډېر اوږده نه وي، نو معلومات اړینو ټکو ته محدود وساتئ او د ډېر پراخولو پر ځای پر روښانه او منطقي ډول ترتیبولو تمرکز وکړئ.',dict(sourceGap=dict(note='The right edge of the photograph clips the last letters of lines ("sho[uld]", "M[ost]", "to [the]", "man[ner]"); the words are read from context.'))),
('lh','Last Paragraph','آخری پیراگراف','وروستی پراګراف',dict(kind='heading')),
('tl','The last paragraph of a formal letter should state what action you expect the recipient to take — to refund, send you information, etc.','رسمی خط کا آخری پیراگراف بتانا چاہیے کہ آپ وصول کنندہ سے کیا کارروائی کی توقع کرتے ہیں — رقم واپس کرنا، آپ کو معلومات بھیجنا وغیرہ۔','د رسمي لیک وروستی پراګراف باید ووايي چې تاسو له ترلاسه کوونکي څخه کوم عمل تمه لرئ — پیسې بېرته ورکول، تاسو ته معلومات لیږل او نور.',dict(sourceGap=dict(note='The right edge of the photograph clips the last letters of lines ("action y[ou]").'))),
('xh','Example of a Formal Letter with layout','لے آؤٹ کے ساتھ رسمی خط کی مثال','د ترتیب سره د رسمي لیک بېلګه',dict(kind='heading')),
('tx','The example letter below shows you a general layout for a formal letter.','نیچے دیا گیا مثالی خط آپ کو رسمی خط کا عمومی ترتیب دکھاتا ہے۔','لاندې بېلګه‌یي لیک تاسو ته د رسمي لیک عمومي ترتیب ښيي.',dict(sourceGap=dict(note='The right edge of the photograph clips the end of the line ("a form[al]"); the layout figure follows on the next page.')))]
for k,a,b,d,*m in P: add(s,k,a,b,d,tab='writing',**(m[0] if m else {}))
F.done()
s['sourceNote']='Printed page 72. Bold headings "Ending a letter:", "How to Write a Formal Letter", "First paragraph", "Middle Paragraph(s)", "Last Paragraph", "Example of a Formal Letter with layout". The right edge of the photograph clips the last letters of many lines; the words are read from context. The page number 72 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 82 (printed 73) ----------
s=page(82,U,'73','Formal Letter Layout','رسمی خط کا لے آؤٹ','د رسمي لیک ترتیب','letter-layout')
F=Flow(s)
H(s,'h','Formal Letter Layout','رسمی خط کا لے آؤٹ','د رسمي لیک ترتیب',tab='writing')
add(s,'t','Use this letter layout when you write your letter.','جب آپ اپنا خط لکھیں تو یہ خط کا لے آؤٹ استعمال کریں۔','کله چې تاسو خپل لیک لیکئ نو دا د لیک ترتیب وکاروئ.',tab='writing')
s['figures']=[dict(id='eng11-s082-fig1',svg=layout_svg(),caption='Formal letter layout',captionUrdu='رسمی خط کا لے آؤٹ',captionPashto='د رسمي لیک ترتیب',labels=[lab('Your address','آپ کا پتہ','ستاسو پته'),lab('Date','تاریخ','نېټه'),lab('Name, job title, and address of the person you are writing to.','اس شخص کا نام، عہدہ اور پتہ جسے آپ لکھ رہے ہیں۔','د هغه کس نوم، دنده او پته چې تاسو ورته لیکئ.'),lab('Insert Sir/Madam or Surname/Name with title (Mr., Ms., Mrs., Dr., etc.)','Sir/Madam یا لقب کے ساتھ خاندانی نام/نام لکھیں (مسٹر، مس، مسز، ڈاکٹر وغیرہ)','Sir/Madam یا له لقب سره کورنی نوم/نوم ولیکئ (ښاغلی، مس، مېرمن، ډاکټر او نور)'),lab('Topic sentence — what is the letter about','موضوعی جملہ — خط کس بارے میں ہے','موضوعي جمله — لیک د څه په اړه دی'),lab('Main body of letter','خط کا بنیادی متن','د لیک اصلي متن'),lab('Yours sincerely if you know the recipient’s name; Yours faithfully if you do not.','اگر آپ وصول کنندہ کا نام جانتے ہیں تو Yours sincerely؛ نہیں جانتے تو Yours faithfully۔','که تاسو د ترلاسه کوونکي نوم پېژنئ نو Yours sincerely؛ که نه نو Yours faithfully.'),lab('Signature','دستخط','لاسلیک'),lab('Your name','آپ کا نام','ستاسو نوم')],sourceGap=dict(note='Redrawn as a coded schematic of the printed layout diagram; the printed annotations are in a decorative italic font and are read from the left margin.'))]
build(s,82,['h','t','F:0'],[])
s['sourceNote']='Printed page 73: a full-page diagram under the pink banner "Formal Letter Layout", with the italic line "Use this letter layout when you write your letter." The layout shows boxes for your address, the date, the recipient\'s name/job title/address, "Dear ____,", a topic sentence, the main body, "Yours ____,", the signature and your name, with italic annotations on the left. A shadow of the neighbouring page at the left and a glued page edge at the top are excluded. The page number 73 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded.'
s['vocabulary']={}
save(s)
