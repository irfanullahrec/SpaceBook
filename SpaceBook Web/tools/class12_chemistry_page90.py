"""PDF90 printed172–173: SN2 mechanism, Table 17.2, 1,2-elimination overview, E1 (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow90');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'substitution':('تبادلہ','بدلون'),'nucleophilic':('نیوکلیوفائلی','نیوکلیوفایلي'),'biomolecular':('دو سالمی','دوه مالیکولي'),'elimination':('اخراج','ایستنه'),'unimolecular':('یک سالمی','یو مالیکولي'),
   'methyl iodide':('میتھائل آئیوڈائیڈ','میتایل ایوډایډ'),'transition state':('عبوری حالت','انتقالي حالت'),'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),'Base':('اساس','قلوي'),'Alkene':('الکین','الکین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def badge(lang,a,b,c,words):
 s=F.start(110,420)+'<rect x="10" y="10" width="400" height="92" rx="6" fill="white" stroke="#222"/>'
 s+=t(170,40,a,18)+(t(200,48,b,18) if b else '')+t(230,40,c,18)
 xs=(70,200,330) if len(words)==3 else (90,330)
 for x,w in zip(xs,words):s+=t(x,90 if x!=200 else 98,lb(lang,w),12)
 s+=line(170,46,xs[0]+40,74,1,'#222','stroke-dasharray="2 3"')+line(230,46,xs[-1]-30,74,1,'#222','stroke-dasharray="2 3"')+(line(200,54,200,84,1,'#222','stroke-dasharray="2 3"') if b else '')
 return s+'</svg>'
def sn2(lang):
 s=F.start(170)
 s+=t(40,92,'HŌ⁻ +',17)+f'<path d="M30 74 Q60 50 100 78" fill="none" stroke="#222" stroke-width="1.5" marker-end="url(#arrow90)"/>'
 s+=t(120,52,'H',15)+line(126,58,140,76)+t(105,92,'H',15)+line(115,88,138,84,1.5,'#222','stroke-dasharray="2 2"')+t(150,92,'C',17)+line(160,86,190,86)+t(205,92,'Br',16)+line(146,100,140,120,3)+t(138,138,'H',15)
 s+=F.arrow(225,275,86)
 s+='<path d="M290 30 L282 30 L282 140 L290 140 M470 30 L478 30 L478 140 L470 140" fill="none" stroke="#222" stroke-width="2"/>'+t(484,26,'‡',14)
 s+=t(320,92,'HO',15)+line(338,86,365,86,1.5,'#222','stroke-dasharray="3 3"')+t(378,92,'C',17)+line(390,86,420,86,1.5,'#222','stroke-dasharray="3 3"')+t(440,92,'Br',15)
 s+=t(378,40,'H',15)+line(378,46,378,74)+line(372,98,356,122)+t(350,138,'H',15)+line(384,98,402,122,3)+t(408,138,'H',15)+t(380,160,lb(lang,'transition state'),12)
 s+=F.arrow(500,550,86)+t(590,92,'HO — C',17)+t(616,48,'H',15)+line(616,54,616,74)+t(650,92,'H',15)+line(626,88,644,88,1.5,'#222','stroke-dasharray="2 2"')+line(618,100,620,118,3)+t(620,136,'H',15)+t(740,92,'+ Br⁻',17)
 s+=t(150,160,lb(lang,'methyl iodide'),12)+t(610,160,lb(lang,'methyl alcohol'),12)
 return s+'</svg>'
def elim(lang):
 s=F.start(130)+t(70,40,'X',16)+t(130,40,'H',16)+t(92,52,'α',12)+t(112,52,'β',12)+line(76,46,88,62)+line(124,46,114,62)+t(100,76,'—C—C—',17)+line(88,84,82,100)+line(114,84,120,100)
 s+=t(250,58,'⊖',14)+t(290,70,': '+lb(lang,'Base'),14)+F.arrow(240,330,78)
 s+=t(400,44,'H',15)+t(460,44,'H',15)+line(406,50,418,62)+line(454,50,442,62)+t(430,78,'C = C',17)+line(418,86,406,98)+line(442,86,454,98)+t(400,114,'H',15)+t(460,114,'H',15)+t(430,128,lb(lang,'Alkene'),12)
 s+=t(620,78,'H — '+lb(lang,'Base'),16)+t(700,78,'+',17)+t(750,78,':Ẍ:⁻',17)
 return s+'</svg>'

add('17.1.6.4 SN2 Mechanism','17.1.6.4 SN2 طریق کار','17.1.6.4 د SN2 میکانیزم','heading')
visual('chem12-p90-sn2-badge',lambda l:badge(l,'S','N','2',['substitution','nucleophilic','biomolecular']))
add('The abbreviation SN2 stands for Substitution, Nucleophilic, bimolecular. It is a single step concerted mechanism, with bonds breaking and forming at the same time. The entering nucleophile attacks the electrophilic carbon atom of the substrate before the leaving group departs. The middle structure is a transition state, rather than an intermediate. The term bimolecular means that the transition state of the rate-limiting step (the only step in this reaction) involves the collision of two molecules (or ions).',
 'مخفف SN2 کا مطلب ہے تبادلہ، نیوکلیوفائلی، دو سالمی۔ یہ ایک مرحلے کا ہم وقت طریق کار ہے، جس میں بند ایک ہی وقت میں ٹوٹتے اور بنتے ہیں۔ داخل ہونے والا نیوکلیوفائل خارج ہونے والے گروپ کے جانے سے پہلے سبسٹریٹ کے الیکٹروفائلی کاربن ایٹم پر حملہ کرتا ہے۔ درمیانی ساخت عبوری حالت ہے، درمیانی مرکب نہیں۔ اصطلاح دو سالمی کا مطلب ہے کہ شرح محدود کرنے والے مرحلے (اس تعامل کا واحد مرحلہ) کی عبوری حالت میں دو سالمات (یا آئنوں) کا تصادم شامل ہے۔',
 'د SN2 لنډیز معنا بدلون، نیوکلیوفایلي، دوه مالیکولي ده. دا یو پړاوه هممهاله میکانیزم دی، چې پکې تړونونه په یو وخت ماتېږي او جوړېږي. ننوتونکی نیوکلیوفایل د وتونکي ګروپ له وتلو مخکې د سبسټرېټ پر الکتروفایلي کاربني اټوم برید کوي. منځنی جوړښت انتقالي حالت دی، نه منځنی مرکب. د دوه مالیکولي اصطلاح معنا دا ده چې د سرعت محدودوونکي پړاو (په دې تعامل کې یوازینی پړاو) انتقالي حالت د دوو مالیکولونو (یا ایونونو) ټکر رانغاړي.')
add('This mechanism is generally followed by primary alkyl halides and methyl halides. For example, the reaction of hydroxide ion with methyl bromide to form methyl alcohol follow SN2 mechanism, shown below.','یہ طریق کار عموماً ابتدائی الکائل ہیلائیڈز اور میتھائل ہیلائیڈز اپناتے ہیں۔ مثلاً میتھائل برومائیڈ سے ہائیڈروآکسائیڈ آئن کا تعامل جس سے میتھائل الکوحل بنتا ہے، SN2 طریق کار پر چلتا ہے، جیسا کہ نیچے دکھایا گیا ہے۔','دا میکانیزم معمولاً لومړني الکایل هالایډونه او میتایل هالایډونه تعقیبوي. د بېلګې په توګه له میتایل برومایډ سره د هایدروکساید ایون تعامل چې میتایل الکول جوړوي، د SN2 میکانیزم تعقیبوي، لکه څنګه چې لاندې ښودل شوی.')
visual('chem12-p90-sn2-scheme',sn2)
add('It is clear from the above one-step mechanism, that entering nucleophile can attack only from the back side because the front side is blocked by the halogen atom. In the transition state, carbon–bromine bond begins to break as the carbon–oxygen bond begins to form. In other words, the extent of bond formation on one side is equal to the extent of bond breaking on the other side.',
 'اوپر کے ایک مرحلے والے طریق کار سے واضح ہے کہ داخل ہونے والا نیوکلیوفائل صرف پچھلی جانب سے حملہ کر سکتا ہے کیونکہ اگلی جانب ہیلوجن ایٹم سے بند ہے۔ عبوری حالت میں کاربن–برومین بند ٹوٹنا شروع ہوتا ہے جبکہ کاربن–آکسیجن بند بننا شروع ہوتا ہے۔ دوسرے الفاظ میں ایک جانب بند بننے کی حد دوسری جانب بند ٹوٹنے کی حد کے برابر ہوتی ہے۔',
 'له پورته یو پړاوه میکانیزم څرګندېږي چې ننوتونکی نیوکلیوفایل یوازې له شا خوا برید کولی شي ځکه مخکینۍ خوا د هالوجني اټوم په واسطه بنده ده. په انتقالي حالت کې د کاربن–برومین تړون په ماتېدو پیل کوي کله چې د کاربن–اکسیجن تړون په جوړېدو پیل کوي. په بله وینا، په یوه خوا د تړون د جوړېدو کچه په بله خوا د تړون د ماتېدو له کچې سره برابره ده.')
add('This one-step mechanism is supported by kinetic information. The rate is found to double when the concentration of either reactant (nucleophile and substrate) is to be doubled. The reaction is, therefore, first order in each of the reactants and second order overall. The rate equation has the following form: rate = k [CH₃Br][⁻OH]',
 'اس ایک مرحلے والے طریق کار کی تائید حرکیاتی معلومات سے ہوتی ہے۔ کسی بھی متعامل (نیوکلیوفائل اور سبسٹریٹ) کا ارتکاز دوگنا کرنے پر شرح دوگنی ہو جاتی ہے۔ اس لیے تعامل ہر متعامل کے لحاظ سے پہلے درجے کا اور مجموعی طور پر دوسرے درجے کا ہے۔ شرح کی مساوات یہ ہے: rate = k [CH₃Br][⁻OH]',
 'دا یو پړاوه میکانیزم د حرکي معلوماتو په واسطه تاییدېږي. کله چې د هر تعامل کوونکي (نیوکلیوفایل او سبسټرېټ) غلظت دوه چنده شي، سرعت دوه چنده کېږي. نو تعامل د هر تعامل کوونکي له مخې لومړۍ درجه او په ټولیز ډول دویمه درجه دی. د سرعت معادله داسې ده: rate = k [CH₃Br][⁻OH]')
add('Back-side attack of nucleophile literally turns the tetrahedron of the carbon atom inside out. In the product, the nucleophile assumes a stereochemical position in space, opposite to the position of the leaving group originally occupied. This is called inversion of configuration at the carbon atom, shown in above reaction. SN2 mechanism is generally favored by polar aprotic solvents.',
 'نیوکلیوفائل کا پچھلی جانب سے حملہ حقیقتاً کاربن ایٹم کے چہار سطحی کو اندر سے باہر الٹ دیتا ہے۔ پیداوار میں نیوکلیوفائل فضا میں ایسی اسٹیریو کیمیائی جگہ لیتا ہے جو خارج ہونے والے گروپ کی اصل جگہ کے مخالف ہو۔ اسے کاربن ایٹم پر ترتیب کا الٹ کہتے ہیں، جیسا کہ اوپر کے تعامل میں دکھایا گیا ہے۔ SN2 طریق کار کو عموماً قطبی اپروٹک محللات سازگار ہیں۔',
 'د نیوکلیوفایل له شا خوا برید په حقیقت کې د کاربني اټوم څلورمخی دننه بهر اړوي. په محصول کې نیوکلیوفایل په فضا کې داسې سټیریوکیمیاوي ځای نیسي چې د وتونکي ګروپ د اصلي ځای مخالف وي. دې ته پر کاربني اټوم د ترتیب اوښتون وايي، لکه څنګه چې په پورته تعامل کې ښودل شوی. د SN2 میکانیزم معمولاً قطبي اپروټیک محللونه ملاتړ کوي.')
add('The type of mechanism followed by the secondary alkyl halides is governed by the nature of the solvent. If polar protic solvent is present, they follow SN1 mechanism, while in polar aprotic solvents, SN2 mechanism is followed.','ثانوی الکائل ہیلائیڈز کون سا طریق کار اپناتے ہیں، اس کا فیصلہ محلل کی نوعیت کرتی ہے۔ قطبی پروٹک محلل کی موجودگی میں یہ SN1 طریق کار اپناتے ہیں، جبکہ قطبی اپروٹک محللات میں SN2 طریق کار ہوتا ہے۔','د دویمي الکایل هالایډونو د میکانیزم ډول د محلل طبیعت ټاکي. که قطبي پروټیک محلل شته وي، د SN1 میکانیزم تعقیبوي، خو په قطبي اپروټیک محللونو کې د SN2 میکانیزم تعقیبېږي.')
tb={'id':'chem12-table17-2','headers':['Factors and characteristics','SN1','SN2'],
 'rows':[['Promoting factors — Nucleophile','Weak Nucleophile','Strong Nucleophile'],['Promoting factors — Substrate','3° > 2°','CH₃X > 1° > 2°'],['Promoting factors — Solvent','Polar protic','Polar aprotic'],['Characteristics — Kinetics','First Order','Second Order'],['Characteristics — Stereochemistry','Inversion and retention','Inversion']],
 'translations':[{'language':'اردو','headers':['عوامل اور خصوصیات','SN1','SN2'],'rows':[['سازگار عوامل — نیوکلیوفائل','کمزور نیوکلیوفائل','طاقتور نیوکلیوفائل'],['سازگار عوامل — سبسٹریٹ','3° > 2°','CH₃X > 1° > 2°'],['سازگار عوامل — محلل','قطبی پروٹک','قطبی اپروٹک'],['خصوصیات — حرکیات','پہلا درجہ','دوسرا درجہ'],['خصوصیات — اسٹیریو کیمیا','الٹ اور برقراری','الٹ']]},
                 {'language':'پښتو','headers':['عوامل او ځانګړنې','SN1','SN2'],'rows':[['ملاتړي عوامل — نیوکلیوفایل','کمزوری نیوکلیوفایل','قوي نیوکلیوفایل'],['ملاتړي عوامل — سبسټرېټ','3° > 2°','CH₃X > 1° > 2°'],['ملاتړي عوامل — محلل','قطبي پروټیک','قطبي اپروټیک'],['ځانګړنې — حرکیات','لومړۍ درجه','دویمه درجه'],['ځانګړنې — سټیریوکیمیا','اوښتون او ساتنه','اوښتون']]}]}
add('Table 17.2 Summary of Nucleophilic Substitution in Alkyl Halides','جدول 17.2 الکائل ہیلائیڈز میں نیوکلیوفائلی تبادلے کا خلاصہ','جدول 17.2 په الکایل هالایډونو کې د نیوکلیوفایلي بدلون لنډیز')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('17.1.7 1,2-Elimination Reactions','17.1.7 1،2-اخراجی تعاملات','17.1.7 1،2-ایستلو تعاملونه','heading')
add('17.1.7.1 Overview','17.1.7.1 جائزہ','17.1.7.1 کتنه','heading')
add('We have already discussed that alkyl halides undergo substitution as well as elimination reactions in (Section 17.1.5). When treated with a strong base, an alkyl halide can undergo a type of elimination process, called 1,2-elimination, also known as β-elimination, in which a proton is removed from the β position, the halide is ejected as a leaving group from the α position and a double bond is formed between the α and β positions:',
 'ہم (حصہ 17.1.5) میں بیان کر چکے ہیں کہ الکائل ہیلائیڈز تبادلے کے ساتھ ساتھ اخراج کے تعاملات بھی کرتے ہیں۔ طاقتور اساس سے عمل کرانے پر الکائل ہیلائیڈ ایک قسم کا اخراجی عمل کر سکتا ہے جسے 1،2-اخراج یا β-اخراج کہتے ہیں، جس میں β مقام سے پروٹان ہٹایا جاتا ہے، ہیلائیڈ α مقام سے خارج ہونے والے گروپ کے طور پر نکلتا ہے اور α اور β مقامات کے درمیان دوہرا بند بنتا ہے:',
 'موږ مخکې په (برخه 17.1.5) کې بحث کړی چې الکایل هالایډونه بدلون او ایستلو دواړه تعاملونه کوي. کله چې له قوي قلوي سره تعامل وکړي، الکایل هالایډ د ایستلو یو ډول بهیر کولی شي چې 1،2-ایستنه یا β-ایستنه بلل کېږي، چې پکې له β موقعیت څخه پروټون لرې کېږي، هالایډ د وتونکي ګروپ په توګه له α موقعیت ایستل کېږي او د α او β موقعیتونو ترمنځ دوه ګونی تړون جوړېږي:')
visual('chem12-p90-beta-elimination',elim)
add('Alkyl halides undergo elimination reactions by two different types of mechanisms.','الکائل ہیلائیڈز دو مختلف طریق کار سے اخراجی تعاملات کرتے ہیں۔','الکایل هالایډونه په دوو بېلو میکانیزمونو د ایستلو تعاملونه کوي.')
add('17.1.7.2 E1 Mechanism','17.1.7.2 E1 طریق کار','17.1.7.2 د E1 میکانیزم','heading')
visual('chem12-p90-e1-badge',lambda l:badge(l,'E','','1',['elimination','unimolecular']))
add('The abbreviation E1 stands for Elimination, unimolecular. The mechanism is called unimolecular because the rate-limiting transition state involves a single molecule rather than a collision between two molecules. The slow step of an E1 reaction is the same as in the SN1 reaction: unimolecular ionization to form a carbocation.',
 'مخفف E1 کا مطلب ہے اخراج، یک سالمی۔ اس طریق کار کو یک سالمی اس لیے کہتے ہیں کہ شرح محدود کرنے والی عبوری حالت میں دو سالمات کے تصادم کے بجائے ایک ہی سالمہ شامل ہوتا ہے۔ E1 تعامل کا سست مرحلہ وہی ہے جو SN1 تعامل میں ہے: کاربوکیٹائن بنانے کے لیے یک سالمی آئنائزیشن۔',
 'د E1 لنډیز معنا ایستنه، یو مالیکولي ده. دې میکانیزم ته یو مالیکولي ځکه وايي چې د سرعت محدودوونکی انتقالي حالت د دوو مالیکولونو د ټکر پر ځای یوازې یو مالیکول رانغاړي. د E1 تعامل ورو پړاو د SN1 تعامل په څېر دی: د کاربوکاټیون د جوړولو لپاره یو مالیکولي ایونایزېشن.')
record=section('17.6','SN2 mechanism, Table 17.2 and 1,2-elimination','SN2 طریق کار، جدول 17.2 اور 1،2-اخراج','د SN2 میکانیزم، جدول 17.2 او 1،2-ایستنه',paras,layout,blocks,'172–173')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':90,'printedPages':[172,173]}]
record['sourceContinuesOnPdfPage']=91
issues=[{'id':'chem12-p172-methyl-iodide-label','printedPage':172,'description':'SN2 scheme substrate CH₃Br is labelled "methyl iodide" and badges read "biomolecular"; retained as printed. Last E1 sentence completed from printed 174.'}]
carry=[{'from':'17.6','to':'17.7','startsAt':'In a fast second step'}]
if __name__=='__main__':save(90,[record],carry=carry,issues=issues,chapter_number=17)
