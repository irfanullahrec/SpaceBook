from stathelp import *
c=cell
U='vital-statistics'
E72='stat11-ex-7-2'; E73='stat11-ex-7-3'; E74='stat11-ex-7-4'
# ---------- scan 231 (printed 221) ----------
s=page(231,U,'221','Specific death rate (formulas) · age-, sex-, age-sex-specific · (3) Infant · (4) Neonatal · (5) Still birth rates','مخصوص شرحِ اموات (فارمولے) · عمر، جنس اور عمر و جنس کے لحاظ سے · (3) شیرخوار · (4) نوزائیدہ · (5) مردہ پیدائش کی شرحیں','ځانګړې د مړینې کچه (فورمولونه) · د عمر، جنس او عمر-جنس له مخې · (3) ماشوم · (4) نوی زېږېدلی · (5) مړه زېږون کچې','vs-rates-2')
Flow(s)
add(s,'h1','(i) Age-specific death rate','(i) عمر کے لحاظ سے مخصوص شرحِ اموات','(i) د عمر له مخې ځانګړې د مړینې کچه')
add(s,'t1','When the death rates are computed for the population consisting of the specified age group, it is called age specific death rate (Age-S.D.R).','جب شرحیں اموات کسی مخصوص عمر کے گروہ پر مشتمل آبادی کے لیے حساب کی جائیں تو اسے عمر کے لحاظ سے مخصوص شرحِ اموات (Age-S.D.R) کہتے ہیں۔','کله چې د مړینې کچې د ځانګړې عمري ډلې لرونکي نفوس لپاره محاسبه شي نو دې ته د عمر له مخې ځانګړې د مړینې کچه (Age-S.D.R) ویل کېږي.')
add(s,'h2','(ii) Sex-specific death rate','(ii) جنس کے لحاظ سے مخصوص شرحِ اموات','(ii) د جنس له مخې ځانګړې د مړینې کچه')
add(s,'t2','When the death rates are computed for the population consisting of the specified gender i.e. male or female, it is called sex-specific death rate','جب شرحیں اموات کسی مخصوص جنس یعنی مرد یا عورت پر مشتمل آبادی کے لیے حساب کی جائیں تو اسے جنس کے لحاظ سے مخصوص شرحِ اموات کہتے ہیں','کله چې د مړینې کچې د ځانګړي جنس یعنې نارینه یا ښځینه لرونکي نفوس لپاره محاسبه شي نو دې ته د جنس له مخې ځانګړې د مړینې کچه ویل کېږي')
add(s,'h3','(iii) Age-sex- specific death rate','(iii) عمر و جنس کے لحاظ سے مخصوص شرحِ اموات','(iii) د عمر-جنس له مخې ځانګړې د مړینې کچه')
add(s,'t3','When age-specific death rates are computed separately for male and females, they are called age-sex- specific death rates.','جب عمر کے لحاظ سے مخصوص شرحیں اموات مردوں اور عورتوں کے لیے الگ الگ حساب کی جائیں تو انہیں عمر و جنس کے لحاظ سے مخصوص شرحیں اموات کہتے ہیں۔','کله چې د عمر له مخې ځانګړې د مړینې کچې د نارینه او ښځو لپاره جلا محاسبه شي نو دوی ته د عمر-جنس له مخې ځانګړې د مړینې کچې ویل کېږي.')
add(s,'h4','(3) Infant mortality rate','(3) شیرخوار اموات کی شرح','(3) د ماشومانو د مړینې کچه')
add(s,'t4','When the children deaths are under one year of age, then the Age-SDR is known as infant mortality rate.','جب بچوں کی اموات ایک سال سے کم عمر میں ہوں تو Age-SDR کو شیرخوار اموات کی شرح کہا جاتا ہے۔','کله چې د ماشومانو مړینې د یو کال څخه کم عمر کې وي نو Age-SDR د ماشومانو د مړینې کچه بلل کېږي.')
add(s,'w','where','جہاں','چېرته')
add(s,'w1','D = Number of deaths below one year of age during a given year.','D = ایک دیے گئے سال کے دوران ایک سال سے کم عمر میں اموات کی تعداد۔','D = په یو ورکړل شوي کال کې د یو کال څخه کم عمر کې د مړینو شمېر.')
add(s,'w2','B = Number of live birth during the same year.','B = اسی سال کے دوران زندہ پیدائشوں کی تعداد۔','B = په همدې کال کې د ژوندیو زېږونونو شمېر.')
add(s,'h5','(4) Neonatal mortality rate','(4) نوزائیدہ اموات کی شرح','(4) د نوي زېږېدلو د مړینې کچه')
add(s,'t5','When the children deaths are under one month then Age-S.D.R is called neo-natal mortality rate.','جب بچوں کی اموات ایک مہینے سے کم عمر میں ہوں تو Age-S.D.R کو نوزائیدہ اموات کی شرح کہا جاتا ہے۔','کله چې د ماشومانو مړینې د یوې میاشتې څخه کم عمر کې وي نو Age-S.D.R د نوي زېږېدلو د مړینې کچه بلل کېږي.')
add(s,'h6','(5) Still birth rate','(5) مردہ پیدائش کی شرح','(5) د مړه زېږون کچه')
add(s,'t6','When the children birth “are dead babies” then Age-S.D.R is known as still birth rate.','جب بچوں کی پیدائش “مردہ بچے” ہوں تو Age-S.D.R کو مردہ پیدائش کی شرح کہا جاتا ہے۔','کله چې د ماشومانو زېږون “مړه ماشومان” وي نو Age-S.D.R د مړه زېږون کچه بلل کېږي.')
s['equations']+=[eqn(231,'sdr',r'\text{S.D.R}=\dfrac{\text{Number of deaths in the specified section of a population in a given year}}{\text{Total population of the specified section in the same year}}\times 1000','S.D.R = (Number of deaths in the specified section of a population in a given year / Total population of the specified section in the same year) × 1000'),
 eqn(231,'asdr',r'\text{Age-S.D.R}=\dfrac{\text{The number of deaths in a specified age group}}{\text{Total midyear of the same specified age group in the same year}}','Age-S.D.R = (The number of deaths in a specified age group) / (Total midyear of the same specified age group in the same year)   [the factor × 1000 is not printed here]'),
 eqn(231,'imr',r'\text{I.M.R}=\dfrac{D}{B}\times 1000','I.M.R = (D/B) × 1000')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(231,k) for k in ks])
s['flow']=[dict(type='equation',index=0),P('h1','t1'),dict(type='equation',index=1),P('h2','t2','h3','t3','h4','t4'),dict(type='equation',index=2),P('w','w1','w2','h5','t5','h6','t6')]
s['sourceNote']='Printed page 221. The first formula (S.D.R) belongs to the item "(2) Specific death rate" begun on the previous page. Printed spellings kept: "neo-natal", "midyear". Header graphics and watermark excluded.'
s['vocabulary']={'infant mortality rate':dict(ur='شیرخوار اموات کی شرح',ps='د ماشومانو د مړینې کچه')}
save(s)
# ---------- scan 232 (printed 222) ----------
s=page(232,U,'222','(6) Maternal death rate · Example 7.2: crude death rate · Example 7.3 (question)','(6) زچگی کے دوران اموات کی شرح · مثال 7.2: خام شرحِ اموات · مثال 7.3 (سوال)','(6) د مور د مړینې کچه · بېلګه 7.2: خام د مړینې کچه · بېلګه 7.3 (پوښتنه)','vs-rates-3')
Flow(s)
add(s,'h6','(6) Maternal death rate','(6) زچگی کے دوران اموات کی شرح','(6) د مور د مړینې کچه')
add(s,'t6','The death rate among the women of child bearing age due to child birth during a given year in a region is known as maternal death rate.','کسی علاقے میں ایک دیے گئے سال کے دوران بچے کی پیدائش کی وجہ سے بچے پیدا کرنے کی عمر کی عورتوں میں شرحِ اموات کو زچگی کے دوران اموات کی شرح کہا جاتا ہے۔','په یوه سیمه کې په یو ورکړل شوي کال کې د ماشوم زېږولو له امله د ماشوم زېږولو عمر ښځو کې د مړینې کچه د مور د مړینې کچه بلل کېږي.')
head(s,'ex72','Example: 7.2','مثال: 7.2','بېلګه: 7.2',exampleId=E72)
add(s,'q72','Calculate crude death rate from the data given below.','نیچے دیے گئے اعداد و شمار سے خام شرحِ اموات حساب کریں۔','له لاندې ورکړل شویو معلوماتو څخه خام د مړینې کچه محاسبه کړئ.',role='question',exampleId=E72)
head(s,'sol72','Solution:','حل:','حل:',exampleId=E72)
head(s,'ex73','Example: 7.3','مثال: 7.3','بېلګه: 7.3',exampleId=E73)
add(s,'q73','Compute crude death rates, age-specific death rates for district A and B using the data given below:','نیچے دیے گئے اعداد و شمار کے ذریعے ضلع A اور B کے لیے خام شرحیں اموات اور عمر کے لحاظ سے مخصوص شرحیں اموات حساب کریں:','د لاندې ورکړل شویو معلوماتو په کارولو سره د A او B ولسوالیو لپاره خام د مړینې کچې او د عمر له مخې ځانګړې د مړینې کچې محاسبه کړئ:',role='question',exampleId=E73,sourceGap=dict(note='The solution of Example 7.3 is on the next page.'))
a=['Below 5','5 – 15','15 – 60','Above 60']; pop=[10000,15000,120000,5000]; de=[150,40,75,510]
s['tables']=[table('Example 7.2: age, population and deaths','مثال 7.2: عمر، آبادی اور اموات','بېلګه 7.2: عمر، نفوس او مړینې',[c('Age (years)','عمر (سال)','عمر (کلونه)'),c('Population','آبادی','نفوس'),c('No. of deaths','اموات کی تعداد','د مړینو شمېر')],[[c(a[i]),c(str(pop[i])),c(str(de[i]))] for i in range(4)],exampleId=E72),
 table('Example 7.2 solution table','مثال 7.2 کا حل: جدول','د بېلګې 7.2 د حل جدول',[c('Age (years)','عمر (سال)','عمر (کلونه)'),c('Population','آبادی','نفوس'),c('No. of deaths','اموات کی تعداد','د مړینو شمېر')],[[c(a[i]),c(str(pop[i])),c(str(de[i]))] for i in range(4)]+[[c('Total','میزان','ټولیز'),c('1,50,000'),c('775')]],exampleId=E72),
 table('Example 7.3: districts A and B','مثال 7.3: اضلاع A اور B','بېلګه 7.3: ولسوالۍ A او B',[c('Age-group (years)','عمر کا گروہ (سال)','عمري ډله (کلونه)'),c('District-A: Deaths','ضلع-A: اموات','ولسوالۍ-A: مړینې'),c('District-A: Population','ضلع-A: آبادی','ولسوالۍ-A: نفوس'),c('District-B: Deaths','ضلع-B: اموات','ولسوالۍ-B: مړینې'),c('District-B: Population','ضلع-B: آبادی','ولسوالۍ-B: نفوس')],[[c(v) for v in r] for r in [('0 - 14','2','500','1','400'),('15 - 29','8','2000','1','300'),('30 - 44','12','2000','5','1000'),('45 - 59','10','1000','18','2000'),('60 - 74','20','500','70','2000'),('75 and above','15','100','50','400')]],exampleId=E73)]
s['equations']+=[eqn(232,'cdr',r'\text{C.D.R}=\dfrac{\text{Total number of registered deaths in the year}}{\text{Total midyear population during the given year}}\times 1000=\dfrac{775}{150000}\times 1000=5.17\ \text{per }1000','C.D.R = (Total number of registered deaths in the year / Total midyear population during the given year) × 1000 = 775/150000 × 1000 = 5.17 per 1000',exampleId=E72)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(232,k) for k in ks])
s['flow']=[P('h6','t6','ex72','q72'),dict(type='table',index=0),P('sol72'),dict(type='table',index=1),dict(type='equation',index=0),P('ex73','q73'),dict(type='table',index=2)]
s['sourceNote']='Printed page 222. A handwritten note "deaths etc." at the top margin is ignored. The first question table of Example 7.2 and the solution table are both printed; in the question table the two-level header "District-A / District-B" in Example 7.3 is flattened. Printed total kept: "1,50,000". Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 233 (printed 223) ----------
s=page(233,U,'223','Example 7.3: solution · (7) Standardized death rate · (i) Direct method','مثال 7.3: حل · (7) معیاری شرحِ اموات · (i) براہِ راست طریقہ','بېلګه 7.3: حل · (7) معیاري د مړینې کچه · (i) مستقیمه طریقه','vs-rates-4')
Flow(s)
head(s,'sol73','Solution:','حل:','حل:',exampleId=E73)
add(s,'h7','(7) Standardized death rate','(7) معیاری شرحِ اموات','(7) معیاري د مړینې کچه')
add(s,'t7','All the death rates are affected by many socio-economic factors such as climate, income, educational level, occupation, age, sex etc. Aged people die comparatively at a higher rate than young people. Bad climate is injurious to health etc. To eliminate the effects of these factors, the corrected or adjusted or standardized death rates are computed to compare the death rates of two region or communities. The standardized death rates are computed either by','تمام شرحیں اموات بہت سے سماجی و معاشی عوامل جیسے آب و ہوا، آمدنی، تعلیمی سطح، پیشہ، عمر، جنس وغیرہ سے متاثر ہوتی ہیں۔ بوڑھے لوگ نسبتاً نوجوانوں سے زیادہ شرح پر مرتے ہیں۔ خراب آب و ہوا صحت کے لیے نقصان دہ ہے وغیرہ۔ ان عوامل کے اثرات کو ختم کرنے کے لیے دو علاقوں یا برادریوں کی شرحیں اموات کا موازنہ کرنے کے لیے درست شدہ یا ایڈجسٹ شدہ یا معیاری شرحیں اموات حساب کی جاتی ہیں۔ معیاری شرحیں اموات یا تو حساب کی جاتی ہیں','ټولې د مړینې کچې د ډېرو ټولنیزو-اقتصادي عواملو لکه اقلیم، عاید، تعلیمي کچه، مسلک، عمر، جنس او نورو لخوا اغېزمنې کېږي. زاړه خلک نسبتاً له ځوانانو څخه په لوړه کچه مري. بد اقلیم روغتیا ته زیانمن دی او نور. د دې عواملو د اغېزو د لرې کولو لپاره د دوو سیمو یا ټولنو د مړینې د کچو د پرتلې لپاره سم شوې یا تعدیل شوې یا معیاري د مړینې کچې محاسبه کېږي. معیاري د مړینې کچې یا محاسبه کېږي',sourceGap=dict(note='The word "by" at the end introduces items (i) Direct method and (ii) Indirect method.'))
add(s,'h8','(i) Direct method','(i) براہِ راست طریقہ','(i) مستقیمه طریقه')
add(s,'w','where','جہاں','چېرته')
add(s,'w1','d_i = number of deaths in the given population in the ith age-group.','d_i = دی گئی آبادی میں i ویں عمر کے گروہ میں اموات کی تعداد۔','d_i = په ورکړل شوي نفوس کې د i‌م عمري ډلې کې د مړینو شمېر.')
add(s,'w2','p_i = given population in the ith age-group.','p_i = i ویں عمر کے گروہ میں دی گئی آبادی۔','p_i = د i‌م عمري ډلې کې ورکړل شوی نفوس.')
add(s,'w3','P_i = standard population in the ith age group.','P_i = i ویں عمر کے گروہ میں معیاری آبادی۔','P_i = د i‌م عمري ډلې کې معیاري نفوس.')
rows=[('0 - 4','2','500','4','1','400','2.5'),('15 - 29','8','2000','4','1','300','3.3'),('30 - 44','12','2000','6','5','1000','5'),('45 - 59','10','1000','10','18','2000','9'),('60 - 74','20','500','40','70','2000','35'),('75 & above','15','100','150','50','400','125')]
s['tables']=[table('Example 7.3 solution table: age-specific death rates','مثال 7.3 کا حل: عمر کے لحاظ سے مخصوص شرحیں اموات','د بېلګې 7.3 حل: د عمر له مخې ځانګړې د مړینې کچې',[c('Age group (years)','عمر کا گروہ (سال)','عمري ډله (کلونه)'),c('District-A: Deaths (D)','ضلع-A: اموات (D)','ولسوالۍ-A: مړینې (D)'),c('District-A: Population (P)','ضلع-A: آبادی (P)','ولسوالۍ-A: نفوس (P)'),c('District-A: Age-S.D.R','ضلع-A: Age-S.D.R','ولسوالۍ-A: Age-S.D.R'),c('District-B: Deaths (D)','ضلع-B: اموات (D)','ولسوالۍ-B: مړینې (D)'),c('District-B: Population (P)','ضلع-B: آبادی (P)','ولسوالۍ-B: نفوس (P)'),c('District-B: Age-S.D.R','ضلع-B: Age-S.D.R','ولسوالۍ-B: Age-S.D.R')],[[c(r[0]),c(r[1]),c(r[2]),c(('2/500 × 1000 = ' if r[0]=='0 - 4' else '')+r[3]),c(r[4]),c(r[5]),c(('1/400 × 1000 = ' if r[0]=='0 - 4' else '')+r[6])] for r in rows]+[[c('Total','میزان','ټولیز'),c('67'),c('6100'),c('11'),c('145'),c('6100'),c('23.8')]],exampleId=E73)]
s['equations']+=[eqn(233,'ca',r'\text{C.D.R for district A}=\dfrac{67}{6100}\times 1000=11\ \text{per thousand}','C.D.R for district A = 67/6100 × 1000 = 11 per thousand',exampleId=E73),
 eqn(233,'cb',r'\text{C.D.R for district B}=\dfrac{145}{6100}\times 1000=23.8\ \text{per thousand}','C.D.R for district B = 145/6100 × 1000 = 23.8 per thousand',exampleId=E73),
 eqn(233,'std',r'S_T.D.R=\dfrac{\sum\left(\dfrac{d_i}{p_i}\right)P_i}{\sum P_i}\times 1000','S_T.D.R = Σ(d_i/p_i)P_i / ΣP_i × 1000')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(233,k) for k in ks])
s['flow']=[P('sol73'),dict(type='table',index=0),dict(type='equation',index=0),dict(type='equation',index=1),P('h7','t7','h8'),dict(type='equation',index=2),P('w','w1','w2','w3')]
s['sourceNote']='Printed page 223. The two-level header "District-A / District-B with Deaths, Population and Age-S.D.R" is flattened. In the first data row of the solution the Age-S.D.R cells show the full working (2/500 × 1000 = 4 and 1/400 × 1000 = 2.5). Header graphics and watermark excluded.'
s['vocabulary']={'standardized death rate':dict(ur='معیاری شرحِ اموات',ps='معیاري د مړینې کچه')}
save(s)
# ---------- scan 234 (printed 224) ----------
s=page(234,U,'224','(ii) Indirect method · Example 7.4: crude and standardized death rate (start)','(ii) بالواسطہ طریقہ · مثال 7.4: خام اور معیاری شرحِ اموات (آغاز)','(ii) غیر مستقیمه طریقه · بېلګه 7.4: خام او معیاري د مړینې کچه (پیل)','vs-rates-5')
Flow(s)
add(s,'h1','(ii) Indirect method','(ii) بالواسطہ طریقہ','(ii) غیر مستقیمه طریقه')
add(s,'w','where D_i = number of deaths in the standard population in the ith age group.','جہاں D_i = معیاری آبادی میں i ویں عمر کے گروہ میں اموات کی تعداد۔','چېرته چې D_i = په معیاري نفوس کې د i‌م عمري ډلې کې د مړینو شمېر.')
head(s,'ex74','Example: 7.4','مثال: 7.4','بېلګه: 7.4',exampleId=E74)
add(s,'q74','Compute crude death rate and standardized death rate of the local population from the data given below and compare it with the crude death rate of the standard population.','نیچے دیے گئے اعداد و شمار سے مقامی آبادی کی خام شرحِ اموات اور معیاری شرحِ اموات حساب کریں اور اس کا معیاری آبادی کی خام شرحِ اموات سے موازنہ کریں۔','له لاندې ورکړل شویو معلوماتو څخه د سیمه‌ییز نفوس خام د مړینې کچه او معیاري د مړینې کچه محاسبه کړئ او د معیاري نفوس له خام د مړینې کچې سره یې پرتله کړئ.',role='question',exampleId=E74)
head(s,'sol74','Solution:','حل:','حل:',exampleId=E74)
add(s,'a1','Now standardized death rate for local population by direct method is','اب مقامی آبادی کے لیے براہِ راست طریقے سے معیاری شرحِ اموات ہے','اوس د سیمه‌ییز نفوس لپاره په مستقیمه طریقه معیاري د مړینې کچه ده',role='solution',exampleId=E74,sourceGap=dict(note='The working continues on the next page.'))
s['tables']=[table('Example 7.4: local and standard population','مثال 7.4: مقامی اور معیاری آبادی','بېلګه 7.4: سیمه‌ییز او معیاري نفوس',[c('Age (years)','عمر (سال)','عمر (کلونه)'),c('Local population: Population','مقامی آبادی: آبادی','سیمه‌ییز نفوس: نفوس'),c('Local population: Deaths','مقامی آبادی: اموات','سیمه‌ییز نفوس: مړینې'),c('Standard population: Population','معیاری آبادی: آبادی','معیاري نفوس: نفوس'),c('Standard population: Deaths','معیاری آبادی: اموات','معیاري نفوس: مړینې')],[[c(v) for v in r] for r in [('0 - 10','400','16','600','18'),('10 - 20','1500','6','1000','5'),('20 - 60','2400','24','3000','24'),('60 - 100','700','21','400','20'),('Total','5000','67','5000','67')]],exampleId=E74)]
s['equations']+=[eqn(234,'ind',r'S_T.D.R=\dfrac{\sum d_i}{\sum\left(\dfrac{D_i}{P_i}\right)p_i}\times\text{C.D.R of standard population}','S_T.D.R = Σd_i / Σ(D_i/P_i)p_i × C.D.R of standard population'),
 eqn(234,'cdr',r'\text{C.D.R}=\dfrac{D}{P}\times 1000','C.D.R = (D/P) × 1000',exampleId=E74),
 eqn(234,'cl',r'\text{C.D.R for local population}=\dfrac{67}{5000}\times 1000=13.4','C.D.R for local population = 67/5000 × 1000 = 13.4',exampleId=E74),
 eqn(234,'cs',r'\text{C.D.R for standard population}=\dfrac{67}{5000}\times 1000=13.4','C.D.R for standard population = 67/5000 × 1000 = 13.4',exampleId=E74),
 eqn(234,'dir',r'S_T.D.R=\dfrac{\sum\left(\dfrac{d_i}{p_i}\right)P_i}{\sum P_i}\times 1000','S_T.D.R = Σ(d_i/p_i)P_i / ΣP_i × 1000',exampleId=E74)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(234,k) for k in ks])
s['flow']=[P('h1'),dict(type='equation',index=0),P('w','ex74','q74'),dict(type='table',index=0),P('sol74'),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),P('a1'),dict(type='equation',index=4)]
s['sourceNote']='Printed page 224. The two-level header "Local population / Standard population with Population and Deaths" is flattened. The printed C.D.R values are both 13.4. A dark mark at the top-left corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
