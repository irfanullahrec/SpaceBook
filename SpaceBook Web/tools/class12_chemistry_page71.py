"""PDF71 printed134–135: alkyne preparation, reactivity and acidity of terminal alkynes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def t(x,y,v,size=20,color='#17212b'):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(v)}</text>'
def line(x,y,a,b,w=2,c='#222',extra=''):return f'<path d="M{x} {y}L{a} {b}" stroke="{c}" stroke-width="{w}" fill="none" {extra}/>'
def start(h,w=850):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><defs><marker id="arrow71" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8z" fill="#222"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
L={'1,2-dibromoethane':('1،2-ڈائی برومو ایتھین','1،2-ډای بروموایتان'),'bromoethene':('برومو ایتھین (دوہرا بند)','بروموایتین'),'(vinyl bromide)':('(وائنائل برومائیڈ)','(وینایل برومایډ)'),
   'ethyne':('ایتھائن','ایتاین'),'alcohol':('الکوحل','الکول'),'1,1,2,2-tetrabromoethane':('1،1،2،2-ٹیٹرا برومو ایتھین','1،1،2،2-ټیټرا بروموایتان'),'acetylene':('ایسیٹیلین','اسیتیلین'),
   'overlap of p orbitals':('p آربیٹلوں کا تداخل','د p اوربیټالونو تداخل'),'cylinder of electron density':('الیکٹرانی کثافت کا سلنڈر','د الکتروني کثافت استوانه'),
   'propyne':('پروپائن','پروپاین'),'terminal alkyne':('ٹرمینل الکائن','ټرمینل الکاین'),'sodium acetylide':('سوڈیم ایسیٹیلائیڈ','سوډیم اسیتیلاید'),
   '1–alkyne':('1–الکائن','1–الکاین'),'sodium alkynide':('سوڈیم الکائنائیڈ','سوډیم الکاینایډ')}
def lb(lang,v):return v if lang=='en' else L[v][0 if lang=='ur' else 1]
def arrow(x1,x2,y,a='',b=''):return line(x1,y,x2,y,2,'#222','marker-end="url(#arrow71)"')+(t((x1+x2)/2,y-9,a,14) if a else '')+(t((x1+x2)/2,y+19,b,14) if b else '')

def dihalide(lang):
 s=start(250)
 s+=t(95,48,'H₂C — CH₂',20)+line(70,55,70,72)+line(122,55,122,72)+t(70,90,'Br',17)+t(122,90,'Br',17)+t(95,115,lb(lang,'1,2-dibromoethane'),14)
 s+=t(215,48,'+ KOH',20)+arrow(265,355,42,lb(lang,'alcohol'),'80°C')
 s+=t(430,48,'HC = CH₂',20)+line(405,55,405,72)+t(405,90,'Br',17)+t(430,112,lb(lang,'bromoethene'),14)+t(430,130,lb(lang,'(vinyl bromide)'),14)+t(640,48,'+ KBr + H₂O',20)
 s+=t(95,180,'HC = CH₂',20)+line(70,187,70,204)+t(70,222,'Br',17)+t(95,244,lb(lang,'bromoethene'),14)
 s+=t(215,180,'+ NaNH₂',20)+arrow(275,375,174,'liq. NH₃','−33°C')+t(450,180,'HC ≡ CH',20)+t(450,204,lb(lang,'ethyne'),14)+t(650,180,'+ NaBr + NH₃',20)
 return s+'</svg>'
def tetra(lang):
 s=start(150)+t(115,30,'Br',17)+t(144,30,'Br',17)+t(150,72,'H — C — C — H  + 2Zn',20)+line(115,38,115,56)+line(144,38,144,56)+line(115,80,115,98)+line(144,80,144,98)+t(115,118,'Br',17)+t(144,118,'Br',17)
 s+=t(150,142,lb(lang,'1,1,2,2-tetrabromoethane'),14)+arrow(330,430,66,lb(lang,'alcohol'))+t(620,72,'H — C ≡ C — H  +  2ZnBr₂',20)+t(580,96,lb(lang,'acetylene'),14)
 return s+'</svg>'
def cloud(lang):
 s=start(150)
 s+=t(40,74,'H',20)+line(55,68,120,68)+line(230,68,290,68)+t(305,74,'H',20)
 for cx in (140,210):s+=f'<ellipse cx="{cx}" cy="42" rx="22" ry="26" fill="#ec407a" opacity=".8"/><ellipse cx="{cx}" cy="94" rx="22" ry="26" fill="#ec407a" opacity=".8"/><ellipse cx="{cx}" cy="68" rx="28" ry="14" fill="#f8bbd0" opacity=".9"/>'
 s+=line(120,68,230,68,3)+t(345,74,'=',24)
 s+='<rect x="490" y="25" width="190" height="86" rx="10" fill="#fff176" opacity=".8"/>'
 s+='<ellipse cx="420" cy="68" rx="45" ry="22" fill="none" stroke="#222"/><ellipse cx="585" cy="68" rx="85" ry="24" fill="none" stroke="#222"/><ellipse cx="740" cy="68" rx="45" ry="22" fill="none" stroke="#222"/>'
 s+=t(410,74,'Hσ bond',14)+t(475,76,'C',18)+t(585,74,'σ bond',15,'#c62828')+t(695,76,'C',18)+t(745,74,'σ bondH',14)
 s+=t(175,140,lb(lang,'overlap of p orbitals'),14)+t(585,140,lb(lang,'cylinder of electron density'),14)
 return s+'</svg>'
def terminal(lang):
 s=start(75)+t(150,30,'H — C ≡ C — H',20)+t(150,55,lb(lang,'acetylene'),14)+t(420,30,'CH₃ — C ≡ C — H',20)+t(420,55,lb(lang,'propyne'),14)+t(690,30,'R — C ≡ C — H',20)+t(690,55,lb(lang,'terminal alkyne'),14)
 return s+'</svg>'
def acetylide(lang):
 s=start(150)
 s+=t(170,40,'H — C ≡ C — H + NaNH₂',20)+t(110,64,lb(lang,'acetylene'),14)+arrow(330,420,34,'liq.NH₃')+t(600,40,'H — C ≡ C⁻Na⁺ + NH₃',20)+t(580,64,lb(lang,'sodium acetylide'),14)
 s+=t(170,115,'R — C ≡ C — H + NaNH₂',20)+t(110,139,lb(lang,'1–alkyne'),14)+arrow(330,420,109,'liq.NH₃')+t(600,115,'R — C ≡ C⁻Na⁺ + NH₃',20)+t(580,139,lb(lang,'sodium alkynide'),14)
 return s+'</svg>'
def polar(lang):
 return start(75)+t(422,20,'δ−',13)+t(490,20,'δ+',13)+t(425,42,'R — C ≡ C — H',20)+t(425,66,lb(lang,'terminal alkyne'),14)+'</svg>'

visual('chem12-p71-dihalide-elimination',dihalide)
add('16.7.5.2 Dehalogenation of Tetrahalides','16.7.5.2 ٹیٹرا ہیلائیڈز کی ڈی ہیلوجینیشن','16.7.5.2 د ټیټرا هالایډونو ډی هالوجینېشن','heading')
add('When tetrahalides having two halogen atoms on each of the two adjacent carbons, are heated with zinc dust in alcohol, alkynes are formed.',
 'جب ایسے ٹیٹرا ہیلائیڈز کو، جن کے دو ملحقہ کاربنوں میں سے ہر ایک پر دو ہیلوجن ایٹم ہوں، الکوحل میں زنک کے سفوف کے ساتھ گرم کیا جائے تو الکائنز بنتے ہیں۔',
 'کله چې هغه ټیټرا هالایډونه چې په دوو ګاونډیو کاربنونو کې پر هر یوه دوه هالوجني اټومونه لري، په الکول کې د جستو له دوړو سره تود شي، الکاینونه جوړېږي.')
visual('chem12-p71-tetrahalide',tetra)
add('16.7.6 Reactivity of Alkynes','16.7.6 الکائنز کی تعامل پذیری','16.7.6 د الکاینونو تعامل وړتیا','heading')
add('Alkynes are unsaturated hydrocarbons like alkenes. Thus they resemble alkenes in most of their reactions. For example, alkyne add hydrogen, halogens and halogen acids much like the addition of these reagents to alkenes. However, unlike alkenes which add one molecules of these reagents, alkynes add two molecules in a step-wise manner. Characteristic reaction of alkyne are also electrophilic addition reactions.',
 'الکائنز، الکینز (دوہرے بند والے) کی طرح غیر سیر شدہ ہائیڈروکاربن ہیں۔ اس لیے اپنے اکثر تعاملات میں یہ الکینز سے مشابہ ہیں۔ مثلاً الکائن ہائیڈروجن، ہیلوجنز اور ہیلوجن تیزاب اسی طرح شامل کرتے ہیں جیسے یہ عامل الکینز میں شامل ہوتے ہیں۔ تاہم الکینز کے برعکس، جو ان عاملوں کا ایک سالمہ شامل کرتے ہیں، الکائنز مرحلہ وار دو سالمات شامل کرتے ہیں۔ الکائن کے خصوصی تعاملات بھی الیکٹروفائلی اضافی تعاملات ہیں۔',
 'الکاینونه د الکینونو په څېر نامشبوع هایدروکاربنونه دي. نو په خپلو ډېرو تعاملونو کې الکینونو ته ورته دي. د بېلګې په توګه، الکاین هایدروجن، هالوجنونه او هالوجني اسیدونه په هماغه ډول ورزیاتوي لکه دا عاملونه چې الکینونو ته ورزیاتېږي. خو د الکینونو برعکس، چې د دې عاملونو یو مالیکول ورزیاتوي، الکاینونه په پړاو پړاو دوه مالیکولونه ورزیاتوي. د الکاین ځانګړي تعاملونه هم الکتروفایلي اضافي تعاملونه دي.')
add('It is to be noted that a carbon–carbon triple bond of alkynes, in general, is less reactive than a carbon–carbon double bond of alkenes, towards electrophilic reagents. This is due to the following reasons.',
 'یہ قابلِ ذکر ہے کہ الکائنز کا کاربن–کاربن تہرا بند عموماً الیکٹروفائلی عاملوں کے لیے الکینز کے کاربن–کاربن دوہرے بند سے کم تعامل پذیر ہوتا ہے۔ اس کی وجوہ درج ذیل ہیں۔',
 'د یادونې وړ ده چې د الکاینونو کاربن–کاربن درې ګونی تړون عموماً د الکتروفایلي عاملونو په وړاندې د الکینونو له کاربن–کاربن دوه ګوني تړون لږ تعامل کوونکی دی. دا د لاندې دلیلونو له امله ده.')
add('i. The triple bonded carbon atoms in alkynes are sp-hybridized while double bonded c-atoms in alkenes are sp²-hybridized. Greater the s character of an orbital, the more highly the electrons in that orbital are held by the nucleus. Thus, pi electrons in alkynes (50% s-character) are more strongly held by the carbon atom than in case of alkenes (33.33% s-character) and are less easily available for reactions with electrophile. This makes alkynes, less reactive than alkenes in electrophilic reactions.',
 'i. الکائنز میں تہرے بند والے کاربن ایٹم sp-ہائبرڈ ہوتے ہیں جبکہ الکینز میں دوہرے بند والے کاربن ایٹم sp²-ہائبرڈ ہوتے ہیں۔ کسی آربیٹل کا s کردار جتنا زیادہ ہو، اس آربیٹل کے الیکٹران مرکزے سے اتنی ہی مضبوطی سے بندھے ہوتے ہیں۔ چنانچہ الکائنز (50% s-کردار) میں پائی الیکٹران الکینز (33.33% s-کردار) کی نسبت کاربن ایٹم سے زیادہ مضبوطی سے بندھے ہوتے ہیں اور الیکٹروفائل سے تعامل کے لیے کم آسانی سے دستیاب ہوتے ہیں۔ اس وجہ سے الیکٹروفائلی تعاملات میں الکائنز، الکینز سے کم تعامل پذیر ہیں۔',
 'i. په الکاینونو کې درې ګوني تړلي کاربني اټومونه sp-هایبرېډ دي، په داسې حال کې چې په الکینونو کې دوه ګوني تړلي کاربني اټومونه sp²-هایبرېډ دي. د یوه اوربیټال s ځانګړنه چې څومره ډېره وي، د هغه اوربیټال الکترونونه هومره په کلکه د هستې له خوا نیول کېږي. نو په الکاینونو (50% s-ځانګړنه) کې پای الکترونونه د الکینونو (33.33% s-ځانګړنه) په پرتله د کاربني اټوم له خوا ډېر کلک نیول کېږي او له الکتروفایل سره د تعامل لپاره لږ په اسانۍ شته وي. دا الکاینونه په الکتروفایلي تعاملونو کې له الکینونو لږ تعامل کوونکي کوي.','list')
add('ii. In alkynes, there are two pi bonds, the four lobes of which merge to form a single electron cloud. This cloud is cylindrically symmetrical about the inter-nuclear axis and occupies large volume (Figure 16.10). Thus, the pi electron–density per unit volume becomes low. Due to decrease in the electron density, pi electrons are not easily available to an electrophile and hence less reactive towards electrophilic addition reactions.',
 'ii. الکائنز میں دو پائی بند ہوتے ہیں، جن کے چار حصے مل کر ایک ہی الیکٹرانی بادل بناتے ہیں۔ یہ بادل بین المرکزی محور کے گرد اسطوانی طور پر متشاکل ہوتا ہے اور بڑا حجم گھیرتا ہے (شکل 16.10)۔ اس لیے فی اکائی حجم پائی الیکٹرانی کثافت کم ہو جاتی ہے۔ الیکٹرانی کثافت میں کمی کی وجہ سے پائی الیکٹران الیکٹروفائل کو آسانی سے دستیاب نہیں ہوتے اور اس لیے الیکٹروفائلی اضافی تعاملات کے لیے کم تعامل پذیر ہوتے ہیں۔',
 'ii. په الکاینونو کې دوه پای تړونونه وي، چې څلور برخې یې سره یو ځای کېږي او یو واحد الکتروني ورېځ جوړوي. دا ورېځ د هستو ترمنځ محور شاوخوا استوانه یي متناظره ده او لوی حجم نیسي (شکل 16.10). نو په هر واحد حجم کې د پای الکتروني کثافت ټیټ کېږي. د الکتروني کثافت د کمښت له امله پای الکترونونه الکتروفایل ته په اسانۍ نه رسېږي او له همدې امله د الکتروفایلي اضافي تعاملونو په وړاندې لږ تعامل کوونکي دي.','list')
visual('chem12-figure16-10',cloud)
add('Figure 16.10 Formation of cylidrical pi electronic cloud of triple bond.','شکل 16.10 تہرے بند کے اسطوانی پائی الیکٹرانی بادل کی تشکیل۔','شکل 16.10 د درې ګوني تړون د استوانه یي پای الکتروني ورېځې جوړېدل.')
add('16.7.7 Acidity of Terminal Alkynes','16.7.7 ٹرمینل الکائنز کی تیزابیت','16.7.7 د ټرمینل الکاینونو تېزابیت','heading')
add('Alkynes in which the triple bond is at the end of the chain, are referred to as terminal or 1-alkynes. Some examples and general formula of terminal alkynes are given below.',
 'وہ الکائنز جن میں تہرا بند زنجیر کے سرے پر ہو، ٹرمینل یا 1-الکائنز کہلاتے ہیں۔ ٹرمینل الکائنز کی چند مثالیں اور عمومی فارمولا درج ذیل ہیں۔',
 'هغه الکاینونه چې درې ګونی تړون یې د ځنځیر په پای کې وي، ټرمینل یا 1-الکاینونه بلل کېږي. د ټرمینل الکاینونو ځینې بېلګې او عمومي فورمول لاندې ورکړل شوي.')
visual('chem12-p71-terminal-alkynes',terminal)
add('Terminal alkynes and acetylene are slightly acidic in nature. They readily donate proton to a strong base. Thus if acetylene or a terminal alkyne is treated with a solution of sodium amide (NaNH₂) in liquid ammonia, sodium acetylide or generally sodium alkynide is obtained.',
 'ٹرمینل الکائنز اور ایسیٹیلین فطرتاً ہلکے تیزابی ہیں۔ یہ طاقتور اساس کو آسانی سے پروٹان دیتے ہیں۔ چنانچہ اگر ایسیٹیلین یا کسی ٹرمینل الکائن کو مائع امونیا میں سوڈیم امائیڈ (NaNH₂) کے محلول سے عمل کرایا جائے تو سوڈیم ایسیٹیلائیڈ یا عمومی طور پر سوڈیم الکائنائیڈ حاصل ہوتا ہے۔',
 'ټرمینل الکاینونه او اسیتیلین په طبیعت کې لږ تېزابي دي. دوی قوي قلوي ته په اسانۍ پروټون ورکوي. نو که اسیتیلین یا یو ټرمینل الکاین په مایع امونیا کې د سوډیم اماید (NaNH₂) له محلول سره تعامل وکړي، سوډیم اسیتیلاید یا په عمومي ډول سوډیم الکاینایډ ترلاسه کېږي.')
visual('chem12-p71-acetylide',acetylide)
add('Acetylene and other terminal alkynes are more acidic than alkanes and alkenes, as clear from pKa values given in Table 16.5. The acidity of an acetylenic hydrogen is due to sp-hybridization of triple bonded carbon atom. A sp-hybrid orbital has 50% s character in it and renders the carbon atom more electronegative than sp² and sp³-hybridized carbons. As a result, the sp-hybridized carbon atoms of a terminal alkyne pulls the electrons more strongly making the attached hydrogen atom slightly acidic.',
 'ایسیٹیلین اور دوسرے ٹرمینل الکائنز، الکینز (اکیلے اور دوہرے بند والے) سے زیادہ تیزابی ہیں، جیسا کہ جدول 16.5 میں دیے گئے pKa اقدار سے واضح ہے۔ ایسیٹیلینک ہائیڈروجن کی تیزابیت تہرے بند والے کاربن ایٹم کی sp-ہائبرڈائزیشن کی وجہ سے ہے۔ sp-ہائبرڈ آربیٹل میں 50% s کردار ہوتا ہے اور یہ کاربن ایٹم کو sp² اور sp³-ہائبرڈ کاربنوں سے زیادہ برقی منفی بنا دیتا ہے۔ نتیجتاً ٹرمینل الکائن کے sp-ہائبرڈ کاربن ایٹم الیکٹرانوں کو زیادہ زور سے کھینچتے ہیں جس سے جڑا ہوا ہائیڈروجن ایٹم ہلکا تیزابی ہو جاتا ہے۔',
 'اسیتیلین او نور ټرمینل الکاینونه له الکانونو او الکینونو ډېر تېزابي دي، لکه څنګه چې په جدول 16.5 کې د ورکړل شویو pKa ارزښتونو څخه څرګندېږي. د اسیتیلیني هایدروجن تېزابیت د درې ګوني تړلي کاربني اټوم د sp-هایبرېډیزېشن له امله دی. sp-هایبرېډ اوربیټال 50% s ځانګړنه لري او کاربني اټوم له sp² او sp³-هایبرېډ کاربنونو ډېر الکترونېګاتیف کوي. په پایله کې د ټرمینل الکاین sp-هایبرېډ کاربني اټومونه الکترونونه ډېر په زور راکاږي او تړلی هایدروجني اټوم لږ تېزابي کوي.')
visual('chem12-p71-terminal-polarity',polar)

record=section('16.18','Alkyne preparation, reactivity and acidity of terminal alkynes','الکائنز کی تیاری، تعامل پذیری اور ٹرمینل الکائنز کی تیزابیت','د الکاینونو چمتو کول، تعامل وړتیا او د ټرمینل الکاینونو تېزابیت',paras,layout,blocks,'134–135')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':71,'printedPages':[134,135]}]
record['sourceContinuesOnPdfPage']=72
issues=[{'id':'chem12-p135-cylidrical-typo','printedPage':135,'description':'Figure 16.10 caption printed "cylidrical"; retained in English.'}]
carry=[{'from':'16.18','to':'16.19','startsAt':'Table 16.5 pKa values of Ethane'}]
if __name__=='__main__':save(71,[record],carry=carry,issues=issues,chapter_number=16)
