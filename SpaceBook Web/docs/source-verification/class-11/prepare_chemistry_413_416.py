from chemlib import *
c=cell
GL='chem11-glossary-index'
def pg(n,title,ur,ps,sid): return page(n,GL,title,ur,ps,sid)
def index_page(s,groups):
    s['paras']=[]; s['tables']=[]; s['flow']=[]
    add(s,'h','Index','اشاریہ','لړلیک',kind='heading')
    s['flow'].append(dict(type='paragraphs',ids=[f"chem11-p{s['source']['pdfPage']}-h"]))
    for letter,rows in groups:
        s['tables'].append(table(letter,letter,letter,[c('Term','اصطلاح','اصطلاح'),c('Page','صفحہ','پاڼه')],[[c(t,u,p),c(str(n))] for t,u,p,n in rows]))
        s['flow'].append(dict(type='table',index=len(s['tables'])-1))
    s['vocabulary']={'index':dict(ur='اشاریہ',ps='لړلیک')}

# ---------- 413 ----------
s=pg(413,'Index: R – Y','اشاریہ: R – Y','لړلیک: R – Y','index-r-y')
G=[
('R',[('Resonance','گمک (ریزونینس)','ریزونانس',79),('Rate law','شرحی قانون','د کچې قانون',273),("Raoult's law",'راؤلٹ کا قانون','د راولټ قانون',310),('Reduction','تخفیف','ریډکشن',359),('Reducing agent','تخفیفی ایجنٹ','ریډیوسینګ اجنټ',361)]),
('S',[('Solubility','حلالیت','منحلېدنه',302),('Spectrum','طیف','سپېکټرم',42),('s-orbital','s-مدار','s-اوربیټل',59),('Sigma bond','سگما بانڈ','سیګما بانډ',81),('Surface tension','سطحی تناؤ','سطحي کشش',164),('Salt hydrolysis','نمک کی آبکافت','د مالګې هایدرولیز',261),('Symmetry','تشاکل','تناسب (سمیټري)',185),('Solvation','محلل کاری (سالویشن)','سالویشن',321),('Standard hydrogen electrode SHE','معیاری ہائیڈروجن الیکٹروڈ SHE','معیاري هایدروجن الکترود SHE',368)]),
('T',[('Transition temperature','تبدیلی کا درجہ حرارت','د بدلون تودوخه',190),('Theoretical yield','نظریاتی پیداوار','نظري حاصل',18),('Thermodynamics','حرکیاتِ حرارت','ترموډینامیک',333),('Types of chemical equilibrium','کیمیائی توازن کی اقسام','د کیمیاوي انډول ډولونه',212)]),
('U',[('Unit cell','اکائی خلیہ','واحد حجره',193)]),
('V',[('VSEPR Theory','VSEPR نظریہ','VSEPR تیوري',72),('VBT','VBT','VBT',80),('Van der waals equation','وین ڈر والز مساوات','د وان در والز معادله',128),('Vapour pressure','بخاراتی دباؤ','د بخار فشار',161),('Viscosity','چپچپاہٹ','چسپناکي',165),('Voltaic cell','وولٹائی خلیہ','وولټایک حجره',375)]),
('X',[('X-rays','ایکس شعاعیں','ایکس وړانګې',49)]),
('Y',[('Yield','پیداوار','حاصل',18)])]
index_page(s,G)
s['sourceNote']='Printed folio 408 (Index, third page; the folio is cropped off). Two columns: left column R, S, T, right column U, V, X, Y (there is no letter band for W). Printed spellings retained: "Van der waals equation". The page numbers are printed at the right of each entry. The scan is skewed with a ghost of the next page showing at the lower left; a CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; ghosting ignored.')
save(s)

# ---------- 414 ----------
s=pg(414,'MCQs Answer Keys','کثیر انتخابی سوالات کی جوابی کلید','د څو انتخابي پوښتنو د ځوابونو کلیدونه','mcq-answer-keys')
add(s,'h','MCQs Answer Keys','کثیر انتخابی سوالات کی جوابی کلید','د څو انتخابي پوښتنو د ځوابونو کلیدونه',kind='heading')
K=[('1.','d d a b c c d c b c d c - - -'),('2.','b a a d a b b b a c b b a c b'),('3.','a b b b b b c d a b b b b c c'),('4.','d d d a a b c c d c a c c a a'),('5.','a c c a d d d c c a c a d - -'),('6.','b c a b c c a c b d d a c b -'),('7.','b d b c d d b c b c a b'),('8.','c a b c d b c a d a c c b b a'),('9.','b a b d c a d b b d b d c'),('10.','a a c d b c b b d b b b d'),('11.','a b a c b c d b d d a d d a'),('12.','b c b d b a d a d a b a b')]
rows=[]
for u,a in K:
    v=a.split(); v=v+['']*(15-len(v))
    rows.append([c(u)]+[c(x) for x in v])
s['tables']=[table('MCQs Answer Keys','کثیر انتخابی سوالات کی جوابی کلید','د څو انتخابي پوښتنو د ځوابونو کلیدونه',[c('Unit','یونٹ','واحد')]+[c(str(i)) for i in range(1,16)],rows)]
s['flow']=[dict(type='paragraphs',ids=['chem11-p414-h']),dict(type='table',index=0)]
s['vocabulary']={'answer keys':dict(ur='جوابی کلید',ps='د ځوابونو کلیدونه')}
s['sourceNote']='Printed folio is not legible (cropped). The table is transcribed exactly as printed: rows are Units 1–12 and columns are question numbers 1–15; "-" marks printed dashes (Unit 1 questions 13–15, Unit 5 questions 14–15, Unit 6 question 15) and blank cells were left blank (the unit has fewer questions). The scan is skewed and the CamScanner watermark crosses several cells (Unit 4 and Unit 5 around question 9–12; Unit 6 around question 7–9); letters in these cells are read from the visible strokes. Compare with the Unit exercises installed on the earlier pages. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; watermark crosses several cells.')
save(s)

# ---------- 415 ----------
s=pg(415,'References','حوالہ جات','مآخذونه','references')
add(s,'h','References','حوالہ جات','مآخذونه',kind='heading')
RF=[
('Fundamental Concepts in Physical Chemistry, By Berendra Nathalcur','طبعی کیمیا کے بنیادی تصورات، از Berendra Nathalcur','د فزیکي کیمیا بنسټیز مفاهیم، د Berendra Nathalcur لخوا'),
('Essential of Physical Chemistry, By Arun Bahl, B.S. Bahl and G.D. Tuli','طبعی کیمیا کے لوازمات، از Arun Bahl, B.S. Bahl اور G.D. Tuli','د فزیکي کیمیا اړتیاوې، د Arun Bahl, B.S. Bahl او G.D. Tuli لخوا'),
('Atomic Physics (Modern Physics) By Dr. S.N. Ghoshal','ایٹمی طبعیات (جدید طبعیات)، از ڈاکٹر S.N. Ghoshal','اتومي فزیک (عصري فزیک)، د ډاکټر S.N. Ghoshal لخوا'),
('Physical Chemistry, By Gordon M. Barrow','طبعی کیمیا، از Gordon M. Barrow','فزیکي کیمیا، د Gordon M. Barrow لخوا'),
('Advanced Chemistry I (Cambridge Edition), By Phillips S.C. Mathews.','ایڈوانسڈ کیمسٹری I (کیمبرج ایڈیشن)، از Phillips S.C. Mathews۔','پرمختللې کیمیا I (کیمبرج چاپ)، د Phillips S.C. Mathews لخوا.'),
('Physical Chemistry, By Ghulam Nabi, B,A, Khokar and M.N. Akhtar','طبعی کیمیا، از Ghulam Nabi, B,A, Khokar اور M.N. Akhtar','فزیکي کیمیا، د Ghulam Nabi, B,A, Khokar او M.N. Akhtar لخوا'),
('Principles of physical chemistry, By Haq Nawaz Bhatti and Kazim Hussain','طبعی کیمیا کے اصول، از Haq Nawaz Bhatti اور Kazim Hussain','د فزیکي کیمیا اصول، د Haq Nawaz Bhatti او Kazim Hussain لخوا'),
('Introductory College Chemistry, By Floyed, J. Quick','تمہیدی کالج کیمیا، از Floyed, J. Quick','پېژندنیزه کالج کیمیا، د Floyed, J. Quick لخوا'),
('The Chemistry, the Central Science, 14th Edition, By Theodore L. Brown, H. Eugene LeMay','کیمیا، مرکزی سائنس، چودھواں ایڈیشن، از Theodore L. Brown, H. Eugene LeMay','کیمیا، مرکزي ساینس، څوارلسم چاپ، د Theodore L. Brown, H. Eugene LeMay لخوا'),
('Chemistry by Raymond Chang 8th Ed. 2005, Mc Graw Hill, Higher Education, New York, NY 10020','کیمیا از Raymond Chang، آٹھواں ایڈیشن 2005، Mc Graw Hill, Higher Education, New York, NY 10020','کیمیا د Raymond Chang لخوا، اتم چاپ 2005، Mc Graw Hill, Higher Education, New York, NY 10020'),
('Chemistry, reactions structure and properties, 2nd Edition, By Dillard, Clyde R, Goldberg and David E.','کیمیا، تعاملات، ساخت اور خصوصیات، دوسرا ایڈیشن، از Dillard, Clyde R, Goldberg اور David E.','کیمیا، تعاملات، جوړښت او ځانګړتیاوې، دویم چاپ، د Dillard, Clyde R, Goldberg او David E. لخوا'),
('The Elements of Physical Chemistry by P.W. Atkins 3rd edition, Oxford University Press, USA. 1995.','طبعی کیمیا کے عناصر از P.W. Atkins، تیسرا ایڈیشن، Oxford University Press, USA، 1995۔','د فزیکي کیمیا عناصر د P.W. Atkins لخوا، دریم چاپ، Oxford University Press, USA، 1995.'),
('General Chemistry, Principles and Structure By James E Brady and Gerard E Humiston John Wiley and Sons, New York','عمومی کیمیا، اصول اور ساخت، از James E Brady اور Gerard E Humiston، John Wiley and Sons, New York','عمومي کیمیا، اصول او جوړښت، د James E Brady او Gerard E Humiston لخوا، John Wiley and Sons, New York')]
for i,(a,b,c_) in enumerate(RF,1): add(s,f'r{i}',a,b,c_)
s['flow']=[dict(type='paragraphs',ids=[p['id'] for p in s['paras']])]
s['vocabulary']={'references':dict(ur='حوالہ جات',ps='مآخذونه')}
s['sourceNote']='Printed folio is cropped. Thirteen bulleted entries, printed spellings and punctuation retained: "Berendra Nathalcur", "Floyed, J. Quick", "Khokar", "B,A,". The ordinal suffixes (14th, 8th, 2nd, 3rd) are printed as superscripts. The scan is skewed with strong curl at the right edge; a CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan.')
s['vocabulary']['references']=dict(ur='حوالہ جات',ps='مآخذونه')
save(s)

# ---------- 416 ----------
s=pg(416,'Authors','مصنفین','لیکوالان','authors')
add(s,'h','Authors','مصنفین','لیکوالان',kind='heading')
AU=[
('a1','Dr. Khurshid Ali','ڈاکٹر خورشید علی','ډاکټر خورشید علي',None),
('a1t','He is M.Sc and M. Phil from Quaid-e-Azam University, Islamabad and Ph. D from Middle East Technical University Ankara, Turkey. He has attended many workshops and training sessions on teaching and book writing and also delivered lectures as resource person in such sessions. He has produced 23 master, 7 M. Phil and 6 Ph.D research students. He has about 55 publications in journals of international repute.','انہوں نے قائداعظم یونیورسٹی اسلام آباد سے ایم ایس سی اور ایم فل اور مڈل ایسٹ ٹیکنیکل یونیورسٹی انقرہ، ترکی سے پی ایچ ڈی کی ہے۔ انہوں نے تدریس اور کتاب نویسی پر کئی ورکشاپوں اور تربیتی نشستوں میں شرکت کی ہے اور ایسی نشستوں میں وسائلی شخص کے طور پر لیکچر بھی دیے ہیں۔ انہوں نے 23 ماسٹر، 7 ایم فل اور 6 پی ایچ ڈی تحقیقی طلبہ تیار کیے ہیں۔ ان کی بین الاقوامی شہرت کے جرائد میں تقریباً 55 اشاعتیں ہیں۔','هغه د قائداعظم پوهنتون اسلام اباد څخه M.Sc او M. Phil او د Middle East Technical University انقره، ترکیه څخه Ph. D لري. هغه په تدریس او د کتاب لیکلو په اړه ډېرو ورکشاپونو او روزنیزو غونډو کې برخه اخیستې او په داسې غونډو کې د سرچینې شخص په توګه یې لیکچرونه هم ورکړي. هغه 23 ماسټر، 7 M. Phil او 6 Ph.D څېړونکي زده کوونکي روزلي دي. د هغه د نړیوالې شهرت لرونکو مجلو کې نږدې 55 خپرونې شته.'),
('a2','Dr. Muhammad Ibrahim','ڈاکٹر محمد ابراہیم','ډاکټر محمد ابراهیم',None),
('a2t','Dr. Muhammad Ibrahim is working in the Department of Elementary and Secondary Education as senior subject specialist in chemistry, since 2003. He has obtained his Master degree in chemistry from University of Peshawar. He got his Ph.D degree in education from Sarhad University of Science & Information Technology, Peshawar. He has attended a number of seminars and workshops on curriculum and textbook development. He is author of several articles, which have been published in national and international journals.','ڈاکٹر محمد ابراہیم 2003 سے ابتدائی و ثانوی تعلیم کے محکمے میں کیمیا کے سینئر مضمون ماہر کے طور پر کام کر رہے ہیں۔ انہوں نے پشاور یونیورسٹی سے کیمیا میں ماسٹر کی ڈگری حاصل کی۔ انہوں نے سرحد یونیورسٹی آف سائنس اینڈ انفارمیشن ٹیکنالوجی، پشاور سے تعلیم میں پی ایچ ڈی کی ڈگری حاصل کی۔ انہوں نے نصاب اور درسی کتب کی تیاری پر متعدد سیمیناروں اور ورکشاپوں میں شرکت کی ہے۔ وہ کئی مضامین کے مصنف ہیں جو قومی اور بین الاقوامی جرائد میں شائع ہو چکے ہیں۔','ډاکټر محمد ابراهیم له 2003 راهیسې د لومړني او ثانوي زدکړو په څانګه کې د کیمیا د لوړ مضمون متخصص په توګه کار کوي. هغه د پېښور پوهنتون څخه په کیمیا کې د ماسټرۍ درجه ترلاسه کړې. هغه د سرحد د ساینس او معلوماتي ټکنالوجۍ پوهنتون، پېښور څخه په تعلیم کې د Ph.D درجه ترلاسه کړه. هغه په نصاب او درسي کتابونو د جوړولو په اړه ډېرو سیمینارونو او ورکشاپونو کې برخه اخیستې. هغه د ډېرو مقالو لیکوال دی چې په ملي او نړیوالو مجلو کې خپرې شوې.'),
('a3','Prof. Dr. Nasim Mustafa','پروفیسر ڈاکٹر نسیم مصطفیٰ','پروفیسر ډاکټر نسیم مصطفی',None),
('a3t','Prof. Dr. Nasim Mustafa did her Ph. D. from N.C.E in Physical Chemistry from University of Peshawar. She is teaching in Jinnah College Peshawar as professor of chemistry. She is the author of several books. She has attended numerous seminars and workshops related to books development and research. She has about 30 research publications.','پروفیسر ڈاکٹر نسیم مصطفیٰ نے پشاور یونیورسٹی سے این سی ای میں طبعی کیمیا میں پی ایچ ڈی کی ہے۔ وہ جناح کالج پشاور میں کیمیا کی پروفیسر کے طور پر پڑھا رہی ہیں۔ وہ کئی کتابوں کی مصنفہ ہیں۔ انہوں نے کتابوں کی تیاری اور تحقیق سے متعلق متعدد سیمیناروں اور ورکشاپوں میں شرکت کی ہے۔ ان کی تقریباً 30 تحقیقی اشاعتیں ہیں۔','پروفیسر ډاکټر نسیم مصطفی د پېښور پوهنتون څخه په فزیکي کیمیا کې د N.C.E Ph. D. ترلاسه کړې. هغه په جناح کالج پېښور کې د کیمیا د پروفیسرې په توګه تدریس کوي. هغه د ډېرو کتابونو لیکوالې ده. هغې د کتابونو د جوړولو او څېړنې پورې تړلو ډېرو سیمینارونو او ورکشاپونو کې برخه اخیستې. د هغې نږدې 30 څېړنیزې خپرونې شته.'),
('a4','Mushtaq -Ur-Rehman','مشتاق الرحمٰن','مشتاق الرحمن',None),
('a4t','He did his M. Phil in Chemistry from N.C.E in Physical Chemistry from University of Peshawar. He has attended numerous seminars and workshops relating to education and development of Textbooks. Currently he is working as Assistant professor in chemistry at Govt College Shabqader Charsadda.','انہوں نے پشاور یونیورسٹی سے این سی ای میں طبعی کیمیا میں ایم فل کیا ہے۔ انہوں نے تعلیم اور درسی کتب کی تیاری سے متعلق متعدد سیمیناروں اور ورکشاپوں میں شرکت کی ہے۔ فی الحال وہ گورنمنٹ کالج شبقدر چارسدہ میں کیمیا کے اسسٹنٹ پروفیسر کے طور پر کام کر رہے ہیں۔','هغه د پېښور پوهنتون څخه په فزیکي کیمیا کې د N.C.E په کیمیا کې M. Phil کړی. هغه په زدکړو او د درسي کتابونو په جوړولو پورې تړلو ډېرو سیمینارونو او ورکشاپونو کې برخه اخیستې. اوس مهال هغه د دولتي کالج شبقدر چارسدې کې د کیمیا د مرستیال پروفیسر په توګه کار کوي.')]
for row_ in AU:
    k,a,b,c_=row_[:4]
    add(s,k,a,b,c_,kind='heading' if not k.endswith('t') else None) if not k.endswith('t') else add(s,k,a,b,c_)
s['flow']=[dict(type='paragraphs',ids=[p['id'] for p in s['paras']])]
s['vocabulary']={'authors':dict(ur='مصنفین',ps='لیکوالان')}
s['sourceNote']='Printed folio is cropped. The page lists four authors with short biographies; printed spellings retained, including "Mushtaq -Ur-Rehman" with a space before the hyphen. The scan is skewed with strong curl at the lower-left; the first words of the lines of the lower biographies are clipped by the curl but legible. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; lower-left curl.')
save(s)
