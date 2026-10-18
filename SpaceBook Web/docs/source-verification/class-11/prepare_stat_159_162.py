from stathelp import *
c=cell
U='index-numbers'
E43='stat11-ex-4-3'; E44='stat11-ex-4-4'; E45='stat11-ex-4-5'; E46='stat11-ex-4-6'
# ---------- scan 159 (printed 151) ----------
s=page(159,U,'151','Link relative and chain indices · Example 4.3','کڑی اضافت اور زنجیری اشاریے · مثال 4.3','پیوندي نسبت او زنځیري شاخصونه · بېلګه 4.3','index-chain-1')
Flow(s)
add(s,'c1','According to this method price of current period is divided by price of the preceding period and this ratio is multiplied by 100. That is','اس طریقے کے مطابق موجودہ مدت کی قیمت کو پچھلی مدت کی قیمت سے تقسیم کیا جاتا ہے اور اس تناسب کو 100 سے ضرب دیا جاتا ہے۔ یعنی','د دې طریقې له مخې د اوسنۍ دورې بیه د تېرې دورې پر بیه ویشل کېږي او دا نسبت په 100 ضرب کېږي. یعنې',sourceGap=dict(note='Continues the chain base method paragraph from the previous page.'))
add(s,'c2','Similarly link relative for quantity is','اسی طرح مقدار کے لیے کڑی اضافت ہے','همدارنګه د مقدار لپاره پیوندي نسبت دی')
head(s,'ex43','Example: 4.3','مثال: 4.3','بېلګه: 4.3',exampleId=E43)
add(s,'q43','Consider the following price data of a single commodity. Find link relatives and then chain indices.','ایک ہی جنس کے درج ذیل قیمتی اعداد و شمار پر غور کریں۔ کڑی اضافتیں اور پھر زنجیری اشاریے معلوم کریں۔','د یوه واحد توکي لاندې د بیو معلومات په پام کې ونیسئ. پیوندي نسبتونه او بیا زنځیري شاخصونه ومومئ.',role='question',exampleId=E43)
head(s,'sol43','Solution:','حل:','حل:',exampleId=E43)
add(s,'n1','Note that the chain indices are the same as the prices relatives with 1964 as base.','نوٹ کریں کہ زنجیری اشاریے 1964 کو بنیاد لے کر قیمتی اضافتوں کے برابر ہیں۔','پام وکړئ چې زنځیري شاخصونه د 1964 د بنسټ په نیولو سره د بیې له نسبتونو سره مساوي دي.',role='solution',exampleId=E43)
add(s,'n2','Calculation of unweighted price index numbers (composite are more variable case)','غیر وزنی قیمتی اشاریہ اعداد کا حساب (مرکب یا ایک سے زیادہ متغیر کی صورت)','د نه‌وزني بیو شاخص شمېرو محاسبه (مرکب یا له یو څخه ډېر متغیر حالت)',sourceGap=dict(note='The printed phrase "composite are more variable case" is kept as printed.'))
yr=[1964+i for i in range(10)]; pr=[20,18,23,24,25,27,28,30,32,33]
lk=['20/20 × 100 = 100','18/20 × 100 = 90','23/18 × 100 = 127.8','24/23 × 100 = 104.3','104.2','108','103.7','107.1','106.6','103.1']
ch=['100','100 × 90/100 = 90','90 × 127.8/100 = 115','115 × 104.3/100 = 120','125','135','140','150','160','165']
s['tables']=[table('Example 4.3: years and prices','مثال 4.3: سال اور قیمتیں','بېلګه 4.3: کلونه او بیې',[c('Years:','سال:','کلونه:')]+[c(str(v)) for v in yr],[[c('Price:','قیمت:','بیه:')]+[c(str(v)) for v in pr]],exampleId=E43),
 table('Example 4.3 solution: link relatives and chain indices','مثال 4.3 کا حل: کڑی اضافتیں اور زنجیری اشاریے','د بېلګې 4.3 حل: پیوندي نسبتونه او زنځیري شاخصونه',[c('Year','سال','کال'),c('Price','قیمت','بیه'),c('P0n = (pn/pn−1) × 100'),c('Chain indices','زنجیری اشاریے','زنځیري شاخصونه')],[[c(str(yr[i])),c(str(pr[i])),c(lk[i]),c(ch[i])] for i in range(10)],exampleId=E43)]
s['equations']+=[eqn(159,'lr',r'\text{Link relative}=\dfrac{\text{Current period price}}{\text{Preceding period price}}\times 100','Link relative = (Current period price / Preceding period price) × 100'),
 eqn(159,'p0n',r'P_{0n}=\dfrac{p_n}{p_{n-1}}\times 100','P0n = (pn / pn−1) × 100'),
 eqn(159,'q0n',r'Q_{0n}=\dfrac{q_n}{q_{n-1}}\times 100','Q0n = (qn / qn−1) × 100')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(159,k) for k in ks])
s['flow']=[P('c1'),dict(type='equation',index=0),dict(type='equation',index=1),P('c2'),dict(type='equation',index=2),P('ex43','q43'),dict(type='table',index=0),P('sol43'),dict(type='table',index=1),P('n1','n2')]
s['sourceNote']='Printed page 151. In the solution table the first rows show the full working (fraction × 100 = value; chain index as product / 100) and later rows only the values. Header graphics and watermark excluded.'
s['vocabulary']={'chain indices':dict(ur='زنجیری اشاریے',ps='زنځیري شاخصونه')}
save(s)
# ---------- scan 160 (printed 152) ----------
s=page(160,U,'152','Unweighted composite index numbers · (i) Simple aggregative method · Example 4.4','غیر وزنی مرکب اشاریہ اعداد · (i) سادہ مجموعی طریقہ · مثال 4.4','نه‌وزني مرکب شاخص شمېرې · (i) ساده مجموعي طریقه · بېلګه 4.4','index-aggregative-1')
Flow(s)
add(s,'t1','The following two unweighted index number formulas are used for composite index numbers:','مرکب اشاریہ اعداد کے لیے درج ذیل دو غیر وزنی اشاریہ عدد فارمولے استعمال ہوتے ہیں:','د مرکبو شاخص شمېرو لپاره لاندې دوه نه‌وزني شاخص شمېرې فورمولونه کارول کېږي:')
add(s,'h1','(i) Simple aggregative price index numbers method','(i) سادہ مجموعی قیمتی اشاریہ اعداد کا طریقہ','(i) ساده مجموعي د بیو شاخص شمېرو طریقه')
add(s,'t2','This method shows the percentage change in the aggregate price of a number of commodities at different periods. According to this method, sum of the prices of commodities in a given year is expressed as percentage of the total of the prices of commodities in the base year. Symbolically, it can be written as','یہ طریقہ مختلف مدتوں میں متعدد اجناس کی مجموعی قیمت میں فیصد تبدیلی ظاہر کرتا ہے۔ اس طریقے کے مطابق کسی دیے گئے سال میں اجناس کی قیمتوں کا مجموعہ بنیادی سال میں اجناس کی قیمتوں کے کل کے فیصد کے طور پر ظاہر کیا جاتا ہے۔ علامتی طور پر اسے یوں لکھا جا سکتا ہے','دا طریقه په بېلابېلو دورو کې د څو توکو د مجموعي بیې سلنه بدلون ښيي. د دې طریقې له مخې په یوه ورکړل شوي کال کې د توکو د بیو مجموعه د بنسټیز کال د توکو د بیو د ټول په سلنه ښودل کېږي. په علامتي ډول دا داسې لیکل کېدای شي')
add(s,'t3','Similarly, simple aggregative quantity index number formula is','اسی طرح سادہ مجموعی مقداری اشاریہ عدد کا فارمولا ہے','همدارنګه د ساده مجموعي مقدار شاخص شمېرې فورمول دی')
head(s,'ex44','Example: 4.4','مثال: 4.4','بېلګه: 4.4',exampleId=E44)
add(s,'q44','Compute a simple aggregative price index number for the year 1968 based on 1967 from the following data.','درج ذیل اعداد و شمار سے 1967 کی بنیاد پر سال 1968 کے لیے سادہ مجموعی قیمتی اشاریہ عدد حساب کریں۔','له لاندې معلوماتو څخه د 1967 پر بنسټ د 1968 کال لپاره ساده مجموعي د بیې شاخص شمېره محاسبه کړئ.',role='question',exampleId=E44)
head(s,'sol44','Solution:','حل:','حل:',exampleId=E44)
rows=[('Milk','Seer','0.75','0.85'),('Rice','Maund','35','32'),('Salt','Maund','10','11'),('Oil','Gallon','1.25','1.35'),('Cloth','Yard','2.25','2.60'),('Wheat','Ton','351','335'),('Sugar','Seer','1.25','1.40')]
s['tables']=[table('Example 4.4: commodities and prices','مثال 4.4: اجناس اور قیمتیں','بېلګه 4.4: توکي او بیې',[c('Commodities','اجناس','توکي'),c('Unit','اکائی','واحد'),c('Price (in Rs) 1967','قیمت (روپوں میں) 1967','بیه (په روپیو) 1967'),c('Price (in Rs) 1968','قیمت (روپوں میں) 1968','بیه (په روپیو) 1968')],[[c(v) for v in r] for r in rows],exampleId=E44),
 table('Example 4.4 solution table','مثال 4.4 کا حل: جدول','د بېلګې 4.4 د حل جدول',[c('Commodities','اجناس','توکي'),c('Unit','اکائی','واحد'),c('1967 (p0)'),c('1968 (pn)')],[[c(r[0]),c('Tan' if r[0]=='Wheat' else r[1]),c(r[2]),c(r[3])] for r in rows]+[[c('Total','میزان','ټولیز'),c('–'),c('Σp0 = 401.50'),c('Σpn = 384.20')]],exampleId=E44)]
s['equations']+=[eqn(160,'e1',r'P_{0n}=\dfrac{\sum p_n}{\sum p_0}\times 100','P0n = (Σpn / Σp0) × 100'),
 eqn(160,'e2',r'Q_{0n}=\dfrac{\sum q_n}{\sum q_0}\times 100','Q0n = (Σqn / Σq0) × 100')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(160,k) for k in ks])
s['flow']=[P('t1','h1','t2'),dict(type='equation',index=0),P('t3'),dict(type='equation',index=1),P('ex44','q44'),dict(type='table',index=0),P('sol44'),dict(type='table',index=1)]
s['sourceNote']='Printed page 152. In the solution table the unit of wheat is printed "Tan" (the question table has "Ton"); kept as printed. The two-level header "Price (in Rs) / 1967 / 1968" is flattened. Handwritten notes near the first formula are ignored. Header graphics and watermark excluded.'
s['vocabulary']={'aggregative':dict(ur='مجموعی',ps='مجموعي')}
save(s)
# ---------- scan 161 (printed 153) ----------
s=page(161,U,'153','Example 4.4 (end) · Merits and demerits · (ii) Simple average of relatives · Example 4.5','مثال 4.4 (اختتام) · خوبیاں اور خامیاں · (ii) اضافتوں کا سادہ اوسط · مثال 4.5','بېلګه 4.4 (پای) · ګټې او زیانونه · (ii) د نسبتونو ساده اوسط · بېلګه 4.5','index-aggregative-2')
Flow(s)
add(s,'t1','The simple aggregative price index number is given by','سادہ مجموعی قیمتی اشاریہ عدد یوں دیا جاتا ہے','ساده مجموعي د بیې شاخص شمېره داسې ورکول کېږي',role='solution',exampleId=E44)
add(s,'t2','which is less than 100 by amount 4.3. It means that the prices have decreased in 1968 as compared to 1967 by 4.3 %.','جو 100 سے 4.3 کی مقدار سے کم ہے۔ اس کا مطلب ہے کہ 1968 میں قیمتیں 1967 کے مقابلے میں 4.3 فیصد کم ہوئی ہیں۔','چې له 100 څخه په 4.3 اندازه کمه ده. پدې معنا چې په 1968 کې بیې د 1967 په پرتله په 4.3 سلنه کمې شوې دي.',role='solution',exampleId=E44)
add(s,'t3','Merits and demerits of simple aggregative method','سادہ مجموعی طریقے کی خوبیاں اور خامیاں','د ساده مجموعي طریقې ګټې او زیانونه')
add(s,'mh','Merits','خوبیاں','ګټې')
L(s,[('m1','(i) This method is simple to understand.','(i) یہ طریقہ سمجھنے میں آسان ہے۔','(i) دا طریقه د پوهېدو لپاره ساده ده.'),('m2','(ii) It is easy to calculate.','(ii) اس کا حساب آسان ہے۔','(ii) محاسبه یې اسانه ده.')],'aggr-merits')
add(s,'dh','Demerits','خامیاں','زیانونه')
L(s,[('d1','(i) It does not consider the relative importance of various commodities involved in the index numbers e.g. it gives equal importance milk and shaving cream.','(i) یہ اشاریہ اعداد میں شامل مختلف اجناس کی اضافی اہمیت کو مدنظر نہیں رکھتا مثلاً یہ دودھ اور شیونگ کریم کو برابر اہمیت دیتا ہے۔','(i) دا په شاخص شمېرو کې شامل بېلابېلو توکو نسبي اهمیت په پام کې نه نیسي لکه دا شېدو او د ږیرې کریم ته مساوي اهمیت ورکوي.'),('d2','(ii) The unit of prices of different commodities e.g. metre, dozen, kg etc. affects the value of index number very much. That is why this method is seldom used in practice.','(ii) مختلف اجناس کی قیمتوں کی اکائی مثلاً میٹر، درجن، کلوگرام وغیرہ اشاریہ عدد کی قدر کو بہت متاثر کرتی ہے۔ اسی لیے یہ طریقہ عملی طور پر شاذ و نادر استعمال ہوتا ہے۔','(ii) د بېلابېلو توکو د بیو واحد لکه متر، درجن، کیلوګرام او نور د شاخص شمېرې ارزښت ډېر اغېزمن کوي. همدا لامل دی چې دا طریقه په عمل کې په ندرت کارول کېږي.')],'aggr-demerits')
add(s,'h2','(ii) Simple average of relatives price index number method','(ii) اضافتوں کے سادہ اوسط کا قیمتی اشاریہ عدد کا طریقہ','(ii) د نسبتونو د ساده اوسط د بیې شاخص شمېرې طریقه')
add(s,'t4','According to this method index numbers are obtained by taking average (mean, median, G.M) of the price relatives or link relatives of the given commodities.','اس طریقے کے مطابق اشاریہ اعداد دی گئی اجناس کی قیمتی اضافتوں یا کڑی اضافتوں کا اوسط (اوسط، وسطانیہ، ہندسی اوسط) لے کر حاصل کیے جاتے ہیں۔','د دې طریقې له مخې شاخص شمېرې د ورکړل شویو توکو د بیې نسبتونو یا پیوندي نسبتونو اوسط (اوسط، میانه، هندسي اوسط) اخیستلو سره ترلاسه کېږي.')
head(s,'ex45','Example: 4.5','مثال: 4.5','بېلګه: 4.5',exampleId=E45)
add(s,'q45','Find index number for the year 2011, 2012, and 2013 from the following data by taking 2010 as base and use mean and median as averages of the price relatives.','درج ذیل اعداد و شمار سے 2010 کو بنیاد لے کر سال 2011، 2012 اور 2013 کے لیے اشاریہ عدد معلوم کریں اور قیمتی اضافتوں کے اوسط کے طور پر اوسط اور وسطانیہ استعمال کریں۔','له لاندې معلوماتو څخه د 2010 د بنسټ په نیولو سره د 2011، 2012 او 2013 کلونو لپاره شاخص شمېره ومومئ او د بیې د نسبتونو د اوسط په توګه اوسط او میانه وکاروئ.',role='question',exampleId=E45)
s['tables']=[table('Example 4.5: prices of sugar, tea, soap and tobacco','مثال 4.5: چینی، چائے، صابن اور تمباکو کی قیمتیں','بېلګه 4.5: د بورې، چای، صابون او تنباکو بیې',[c('Year','سال','کال'),c('Sugar (Rs)','چینی (روپے)','بوره (روپۍ)'),c('Tea (Rs)','چائے (روپے)','چای (روپۍ)'),c('Soap (Rs)','صابن (روپے)','صابون (روپۍ)'),c('Tobacco (Rs)','تمباکو (روپے)','تنباکو (روپۍ)')],[[c(v) for v in r] for r in [('2010','1.20','2.80','1.50','3.50'),('2011','1.40','3.00','1.75','4.20'),('2012','1.50','3.25','2.00','4.50'),('2013','1.60','3.40','2.25','4.47')]],exampleId=E45)]
s['equations']+=[eqn(161,'a',r'P_{0n}=\dfrac{\sum p_n}{\sum p_0}\times 100','P0n = (Σpn / Σp0) × 100',exampleId=E44),
 eqn(161,'b',r'=\dfrac{384.20}{401.50}\times 100=95.7','= (384.20 / 401.50) × 100 = 95.7',exampleId=E44)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(161,k) for k in ks])
s['flow']=[P('t1'),dict(type='equation',index=0),dict(type='equation',index=1),P('t2','t3','mh','m1','m2','dh','d1','d2','h2','t4','ex45','q45'),dict(type='table',index=0)]
s['sourceNote']='Printed page 153. The two-level header "Price (Rs) / Sugar / Tea / Soap / Tobacco" is flattened. Printed spellings kept: "shaving cream". Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 162 (printed 154) ----------
s=page(162,U,'154','Example 4.5: solution · Example 4.6: chain indices (start)','مثال 4.5: حل · مثال 4.6: زنجیری اشاریے (آغاز)','بېلګه 4.5: حل · بېلګه 4.6: زنځیري شاخصونه (پیل)','index-relatives-1')
Flow(s)
head(s,'sol45','Solution:','حل:','حل:',exampleId=E45)
add(s,'a1','First we compute price relatives P0n = (pn/p0) × 100 for each commodity and then index numbers by using A.M and median as follows;','پہلے ہم ہر جنس کے لیے قیمتی اضافتیں P0n = (pn/p0) × 100 حساب کرتے ہیں اور پھر حسابی اوسط اور وسطانیہ استعمال کر کے اشاریہ اعداد درج ذیل طور پر حساب کرتے ہیں؛','لومړی موږ د هر توکي لپاره د بیې نسبتونه P0n = (pn/p0) × 100 محاسبه کوو او بیا د A.M او میانې په کارولو سره شاخص شمېرې داسې محاسبه کوو؛',role='solution',exampleId=E45)
head(s,'ex46','Example: 4.6','مثال: 4.6','بېلګه: 4.6',exampleId=E46)
add(s,'q46','Find chain indices for the following data by using A.M of the relatives.','درج ذیل اعداد و شمار سے اضافتوں کے حسابی اوسط کے ذریعے زنجیری اشاریے معلوم کریں۔','له لاندې معلوماتو څخه د نسبتونو د حسابي اوسط په واسطه زنځیري شاخصونه ومومئ.',role='question',exampleId=E46)
head(s,'sol46','Solution:','حل:','حل:',exampleId=E46)
add(s,'a2','First we compute link relatives P0n = (pn/pn−1) × 100 for each commodity and','پہلے ہم ہر جنس کے لیے کڑی اضافتیں P0n = (pn/pn−1) × 100 حساب کرتے ہیں اور','لومړی موږ د هر توکي لپاره پیوندي نسبتونه P0n = (pn/pn−1) × 100 محاسبه کوو او',role='solution',exampleId=E46,sourceGap=dict(note='The sentence continues on the next page ("then chain indices …").'))
s['tables']=[table('Example 4.5 solution: price relatives and index numbers','مثال 4.5 کا حل: قیمتی اضافتیں اور اشاریہ اعداد','د بېلګې 4.5 حل: د بیې نسبتونه او شاخص شمېرې',[c('Year','سال','کال'),c('Sugar','چینی','بوره'),c('Tea','چائے','چای'),c('Soap','صابن','صابون'),c('Tobacco','تمباکو','تنباکو'),c('By mean','اوسط سے','په اوسط'),c('By median','وسطانیہ سے','په میانه')],[[c(v) for v in r] for r in [('2010','1.20/1.20 × 100 = 100','100','100','100','100','100'),('2011','1.40/1.20 × 100 = 116.7','107.1','116.7','120','115.1','116.7'),('2012','125','116.1','133.3','128.6','125.8','126.6'),('2013','133.3','121.4','150','127.7','133.03','130.5')]],exampleId=E45),
 table('Example 4.6: prices of sugar, tea and coffee','مثال 4.6: چینی، چائے اور کافی کی قیمتیں','بېلګه 4.6: د بورې، چای او کافي بیې',[c('Year','سال','کال'),c('Sugar (Rs)','چینی (روپے)','بوره (روپۍ)'),c('Tea (Rs)','چائے (روپے)','چای (روپۍ)'),c('Coffee (Rs)','کافی (روپے)','کافي (روپۍ)')],[[c(v) for v in r] for r in [('1940','2.8','10.5','2.7'),('1941','3.4','10.8','3.2'),('1942','3.6','10.6','3.5'),('1943','4','11.4','3.8'),('1944','4.2','11.5','4')]],exampleId=E46)]
build(s,162,['sol45','a1','T:0','ex46','q46','T:1','sol46','a2'],[])
s['sourceNote']='Printed page 154. The two-level headers "Price relatives / Index numbers" and "Commodity (Prices in Rs.)" are flattened; the first cells of the 2010 and 2011 rows show the full fraction working. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
