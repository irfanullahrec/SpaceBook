from chemlib import *
c=cell
def eqn(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
class Flow:
    def __init__(s_,s): s_.s=s; s_.s['equations']=[]; s_.f=[]
    def p(s_,*keys):
        s_.f.append(dict(type='paragraphs',ids=[f"chem11-p{s_.s['source']['pdfPage']}-{k}" for k in keys]))
    def e(s_,key,latex,text):
        s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def fg(s_,i): s_.f.append(dict(type='figure',index=i))
    def tb(s_,i): s_.f.append(dict(type='table',index=i))
    def done(s_): s_.s['flow']=s_.f
TC='chem11-thermochemistry'
def mk(n,title,ur,ps,sid): return page(n,TC,title,ur,ps,sid)
def tx(x,y,t,size=11,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'

# ---------- 341 ----------
s=mk(341,'ΔE = E₂ − E₁ · Consequences of internal energy increase · 11.4 First Law of Thermodynamics','ΔE = E₂ − E₁ · اندرونی توانائی میں اضافے کے نتائج · 11.4 تھرموڈائنامکس کا پہلا قانون','ΔE = E₂ − E₁ · د داخلي انرژۍ د زیاتوالي پایلې · 11.4 د ترموډینامیکس لومړی قانون','first-law')
F=Flow(s)
add(s,'a1',f'Internal energy of a system cannot be determined, however, change in{SO} internal energy, denoted by ΔE, can be measured and calculated.',f'کسی نظام کی اندرونی توانائی متعین نہیں کی جا سکتی، تاہم اندرونی توانائی میں تبدیلی جسے ΔE سے ظاہر کیا جاتا ہے ناپی اور حساب کی جا سکتی ہے {SO}۔',f'د یو سیسټم داخلي انرژي نشي ټاکل کېدای، خو په داخلي انرژۍ کې بدلون چې په ΔE ښودل کېږي اندازه او محاسبه کېدای شي {SO}.')
add(s,'a2',f'An increase in internal energy of a chemical system has three possible consequences.{SO}',f'کیمیائی نظام کی اندرونی توانائی میں اضافے کے تین ممکنہ نتائج ہیں {SO}۔',f'د یو کيمياوي سیسټم په داخلي انرژۍ کې زیاتوالی درې ممکنې پایلې لري {SO}.')
add(s,'c1',f'i. Increase in internal energy of a system can increase the temperature of the system by increasing the kinetic energy of the molecules.',f'i. نظام کی اندرونی توانائی میں اضافہ سالموں کی حرکی توانائی بڑھا کر نظام کا درجہ حرارت بڑھا سکتا ہے {SO}۔',f'i. د یو سیسټم په داخلي انرژۍ کې زیاتوالی د مالیکولونو د حرکي انرژۍ په زیاتولو سره د سیسټم تودوخه لوړولای شي {SO}.')
add(s,'c2',f'ii. Increase in internal energy of a system can result in phase change of system, e.g., melting or evaporation may occur.',f'ii. نظام کی اندرونی توانائی میں اضافہ نظام کی فیز تبدیلی کا باعث بن سکتا ہے، مثلاً پگھلنا یا بخارات بننا واقع ہو سکتا ہے {SO}۔',f'ii. د یو سیسټم په داخلي انرژۍ کې زیاتوالی د سیسټم د فیز بدلون لامل کېدای شي، د بېلګې په توګه ویلې کېدل یا بخارېدل پېښېدای شي {SO}.')
add(s,'c3',f'iii. Increase in internal energy can result in a chemical reaction if energy supplied is sufficient to break the bonds.',f'iii. اندرونی توانائی میں اضافہ کیمیائی تعامل کا باعث بن سکتا ہے اگر فراہم کی گئی توانائی بندھن توڑنے کے لیے کافی ہو {SO}۔',f'iii. په داخلي انرژۍ کې زیاتوالی کيمياوي تعامل لامل کېدای شي که ورکړل شوې انرژي د بندونو د ماتولو لپاره کافي وي {SO}.')
add(s,'h','11.4 First Law of Thermodynamics','11.4 تھرموڈائنامکس کا پہلا قانون','11.4 د ترموډینامیکس لومړی قانون',kind='heading')
add(s,'b1',f'It was Josiah Willard Gibbs who in 1873 on the basis of experimental work stated the First Law of Thermodynamics. The first law of thermodynamics is, in fact, the law of conservation of energy. According to Gibbs the first law states that energy can neither be created nor destroyed although it may be transferred or changed from one form to another. It can also be stated that "the total energy of the system and its surroundings is conserved". For example, an electric bulb converts electric energy into light energy. The potential energy of a falling ball is converted into kinetic energy.{SO}',f'یہ جوسائیہ ولارڈ گبز تھا جس نے 1873 میں تجرباتی کام کی بنیاد پر تھرموڈائنامکس کا پہلا قانون بیان کیا۔ تھرموڈائنامکس کا پہلا قانون درحقیقت توانائی کی بقا کا قانون ہے۔ گبز کے مطابق پہلا قانون کہتا ہے کہ توانائی نہ پیدا کی جا سکتی ہے نہ فنا، اگرچہ یہ ایک شکل سے دوسری شکل میں منتقل یا تبدیل ہو سکتی ہے۔ یہ بھی کہا جا سکتا ہے کہ "نظام اور اس کے ماحول کی کل توانائی محفوظ رہتی ہے"۔ مثلاً برقی بلب برقی توانائی کو روشنی کی توانائی میں بدلتا ہے۔ گرتی ہوئی گیند کی مخفی توانائی حرکی توانائی میں تبدیل ہو جاتی ہے {SO}۔',f'دا جوسیا ولارډ ګبز و چې په 1873 کې د تجربوي کار پر بنسټ یې د ترموډینامیکس لومړی قانون بیان کړ. د ترموډینامیکس لومړی قانون په حقیقت کې د انرژۍ د ساتنې قانون دی. د ګبز له مخې لومړی قانون وايي چې انرژي نه جوړېدای شي او نه له منځه تلای شي که څه هم له یوې بڼې بلې بڼې ته لېږدول یا بدلېدای شي. دا هم ویل کېدای شي چې "د سیسټم او د هغه د شاوخوا ټوله انرژي ساتل کېږي". د بېلګې په توګه یو برېښنایي بلب برېښنایي انرژي په رڼا انرژۍ بدلوي. د غورځېدونکي بال پوټنشیل انرژي په حرکي انرژۍ بدلېږي {SO}.')
add(s,'b2',f'Energy is exchanged between the system and surroundings in the form of heat and work. A system may lose energy to the surroundings in the form of heat but, at the same time, the same amount of energy is absorbed by the surroundings. Hence, the amount of energy lost by the system is equal to the amount of energy gained by the surroundings.{SO}',f'نظام اور ماحول کے درمیان توانائی حرارت اور کام کی صورت میں مبادلہ ہوتی ہے۔ ایک نظام حرارت کی شکل میں ماحول کو توانائی کھو سکتا ہے لیکن اسی وقت اتنی ہی توانائی ماحول جذب کر لیتا ہے۔ لہٰذا نظام کی کھوئی ہوئی توانائی کی مقدار ماحول کی حاصل کی ہوئی توانائی کی مقدار کے برابر ہوتی ہے {SO}۔',f'د سیسټم او شاوخوا ترمنځ انرژي د تودوخې او کار په بڼه تبادله کېږي. یو سیسټم کولای شي د تودوخې په بڼه شاوخوا ته انرژي له لاسه ورکړي خو په ورته وخت کې همدومره انرژي شاوخوا جذبوي. نو د سیسټم له لاسه ورکړل شوې انرژۍ مقدار د شاوخوا د ترلاسه شوې انرژۍ له مقدار سره مساوي دی {SO}.')
add(s,'b3',f'A way of expressing the first law of thermodynamics is that, any change in internal energy (ΔE) of a system is given by the sum of the heat (q) that flows across its boundaries and the work (w) done on the system by the surroundings.{SO}',f'تھرموڈائنامکس کے پہلے قانون کو بیان کرنے کا ایک طریقہ یہ ہے کہ نظام کی اندرونی توانائی (ΔE) میں کوئی بھی تبدیلی اس حرارت (q) جو اس کی حدود کے آر پار بہتی ہے اور ماحول کی طرف سے نظام پر کیے گئے کام (w) کے مجموعے سے دی جاتی ہے {SO}۔',f'د ترموډینامیکس د لومړي قانون د بیانولو یوه لاره دا ده چې د سیسټم په داخلي انرژۍ (ΔE) کې هر بدلون د هغې تودوخې (q) چې د هغه د پولو له لارې بهېږي او د شاوخوا لخوا په سیسټم باندې ترسره شوي کار (w) د مجموعې په واسطه ورکول کېږي {SO}.')
fig=('<path d="M60 40 C140 10 230 10 300 40" stroke="#3a8ac8" stroke-width="2" fill="none"/><path d="M294 34 L302 42 L290 44" fill="#3a8ac8"/>'
 '<path d="M300 110 C230 140 140 140 70 105" stroke="#3a8ac8" stroke-width="2" fill="none"/><path d="M76 98 L68 105 L80 108" fill="#3a8ac8"/>'
 +tx(180,10,'ΔE = E₂ − E₁',11)+tx(45,55,'E₁',11)+tx(320,55,'E₂',11)+tx(30,105,'State 1',11,'middle',700)+tx(330,105,'State 2',11,'middle',700))
s['figures']=[fig_ if False else dict(id='chem11-p341-state',svg=svg(370,150,'Two arrows between State 1 with energy E1 and State 2 with energy E2 showing delta E equals E2 minus E1',fig),caption='Change in internal energy between State 1 and State 2: ΔE = E₂ − E₁',captionUrdu='حالت 1 اور حالت 2 کے درمیان اندرونی توانائی میں تبدیلی: ΔE = E₂ − E₁',captionPashto='د 1 حالت او 2 حالت ترمنځ د داخلي انرژۍ بدلون: ΔE = E₂ − E₁',labels=[lab('State 1','حالت 1','1 حالت'),lab('State 2','حالت 2','2 حالت')],sourceGap=dict(note='Two-path diagram redrawn as a schematic.'))]
F.p('a1')
F.fg(0)
F.p('a2','c1','c2','c3','h','b1','b2','b3')
F.done()
s['sourceNote']='Printed folio 336. The right edge is clipped by the page curl on the text lines and on the pink italic statement of the first law; clipped endings are marked [scan obscured] and not inferred. The last sentence continues with Eq. (11.1) on the next page. The path diagram (ΔE = E₂ − E₁ between State 1 and State 2) is redrawn as a schematic. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; diagram redrawn; sentence continues on the next page.')
s['vocabulary']={'first law of thermodynamics':{'ur':'تھرموڈائنامکس کا پہلا قانون','ps':'د ترموډینامیکس لومړی قانون'}}
save(s)

# ---------- 342 ----------
s=mk(342,'Equation 11.1 · Table 11.1 Sign convention · Figure 11.2 · Tidbit','مساوات 11.1 · جدول 11.1 علامتی روایت · شکل 11.2 · معلومات','معادله 11.1 · جدول 11.1 د نښو کنوانسیون · شکل 11.2 · ځانګړې یادونه','sign-convention')
F=Flow(s)
add(s,'a1',f"Eq.11.1 says that the change in the internal energy of a system is the sum of the heat exchanged 'q' between the system and the surrounding and the work done 'w' on (or by) the system. The sign convention for 'q' and 'w' are as follows.",f"مساوات 11.1 کہتی ہے کہ نظام کی اندرونی توانائی میں تبدیلی نظام اور ماحول کے درمیان مبادلہ شدہ حرارت 'q' اور نظام پر (یا نظام کے ذریعے) کیے گئے کام 'w' کا مجموعہ ہے۔ 'q' اور 'w' کی علامتی روایت درج ذیل ہے۔",f"معادله 11.1 وايي چې د سیسټم په داخلي انرژۍ کې بدلون د سیسټم او شاوخوا ترمنځ تبادله شوې تودوخې 'q' او په سیسټم باندې (یا د سیسټم په واسطه) ترسره شوي کار 'w' مجموعه ده. د 'q' او 'w' د نښو کنوانسیون په لاندې ډول دی.")
add(s,'a2','The first law of thermodynamics states that the change in internal energy for the system (ΔE) is equal to the amount of heat provided to the system (q) minus the amount of work done by the system (w).','تھرموڈائنامکس کا پہلا قانون کہتا ہے کہ نظام کی اندرونی توانائی میں تبدیلی (ΔE) نظام کو فراہم کی گئی حرارت (q) منفی نظام کے ذریعے کیے گئے کام (w) کی مقدار کے برابر ہوتی ہے۔','د ترموډینامیکس لومړی قانون وايي چې د سیسټم لپاره په داخلي انرژۍ کې بدلون (ΔE) سیسټم ته ورکړل شوې تودوخې (q) منفي د سیسټم په واسطه ترسره شوي کار (w) له مقدار سره مساوي دی.')
add(s,'a3','In some books you can find this equation as','کچھ کتابوں میں آپ یہ مساوات اس طرح پا سکتے ہیں','په ځینو کتابونو کې تاسو دا معادله داسې موندلای شئ')
add(s,'t-h','Tidbit','معلومات','ځانګړې یادونه',kind='heading')
add(s,'t1','Work has opposite signs in physics and chemistry. Work done by system is represented as negative (−w) in chemistry and as positive (+w) in physics.','کام کی علامتیں طبیعیات اور کیمیا میں مخالف ہیں۔ نظام کے ذریعے کیا گیا کام کیمیا میں منفی (−w) اور طبیعیات میں مثبت (+w) ظاہر کیا جاتا ہے۔','کار په فزیک او کیمیا کې مخالفې نښې لري. د سیسټم په واسطه ترسره شوی کار په کیمیا کې منفي (−w) او په فزیک کې مثبت (+w) ښودل کېږي.')
add(s,'sa','Energy Inputs and Outputs','توانائی کی آمد و رفت (اِن پٹس اور آؤٹ پٹس)','د انرژۍ ننوتل او وتل',kind='heading')
rows=[('Work done by the system on the surrounding','نظام کی طرف سے ماحول پر کیا گیا کام','د سیسټم لخوا په شاوخوا ترسره شوی کار','w (negative)','w (منفی)','w (منفي)'),('Work done on the system by the surrounding','ماحول کی طرف سے نظام پر کیا گیا کام','د شاوخوا لخوا په سیسټم ترسره شوی کار','w (positive)','w (مثبت)','w (مثبت)'),('Heat absorbed by the system from the surroundings','نظام کی طرف سے ماحول سے جذب کی گئی حرارت','د سیسټم لخوا له شاوخوا څخه جذب شوې تودوخه','q (positive)','q (مثبت)','q (مثبت)'),('Heat absorbed by the surroundings from the system','ماحول کی طرف سے نظام سے جذب کی گئی حرارت','د شاوخوا لخوا له سیسټم څخه جذب شوې تودوخه','q (negative)','q (منفی)','q (منفي)')]
s['tables']=[table('Table 11.1: Sign Convention for Work and Heat','جدول 11.1: کام اور حرارت کے لیے علامتی روایت','جدول 11.1: د کار او تودوخې لپاره د نښو کنوانسیون',[c('Process','عمل','پروسه'),c('Sign','علامت','نښه')],[[c(a,b,d),c(e,f,g)] for a,b,d,e,f,g in rows])]
box=('<rect x="140" y="70" width="140" height="70" rx="12" fill="#6ab4e0" stroke="#2a6ab8"/>'+tx(210,95,'E',14,'middle',700)+tx(210,112,'(Internal energy',9)+tx(210,124,'contained in system)',9)
 +'<path d="M20 100 H138" stroke="#6ab4e0" stroke-width="22"/><path d="M130 88 L150 105 L130 122 Z" fill="#6ab4e0"/>'+tx(60,104,'+q',14,'middle',700)+tx(60,135,'Heat added',10)+tx(60,147,'to system',10)
 +'<path d="M282 100 H400" stroke="#6ab4e0" stroke-width="22"/><path d="M392 88 L414 105 L392 122 Z" fill="#6ab4e0"/>'+tx(340,104,'−q',14,'middle',700)+tx(345,135,'Heat given off',10)+tx(345,147,'by system',10)
 +'<path d="M210 5 V65" stroke="#6ab4e0" stroke-width="22"/><path d="M198 58 L210 75 L222 58 Z" fill="#6ab4e0"/>'+tx(185,35,'+W',12,'middle',700)+tx(265,25,'work done',10,'start')+tx(265,38,'by system',10,'start')
 +'<path d="M210 145 V210" stroke="#6ab4e0" stroke-width="22"/><path d="M198 205 L210 225 L222 205 Z" fill="#6ab4e0"/>'+tx(185,180,'−W',12,'middle',700)+tx(265,190,'work done',10,'start')+tx(265,203,'by system',10,'start')
 +tx(210,248,'Fig. 11.2 Sign convention for work and heat',12,'middle',700,'#a02040'))
s['figures']=[dict(id='chem11-p342-fig112',svg=svg(430,260,'Energy inputs and outputs of a system E: heat in plus q, heat out minus q, work labelled plus W and minus W',box),caption='Fig. 11.2 Sign convention for work and heat',captionUrdu='شکل 11.2 کام اور حرارت کے لیے علامتی روایت',captionPashto='شکل 11.2 د کار او تودوخې لپاره د نښو کنوانسیون',labels=[lab('Heat added to system','نظام میں حرارت کا اضافہ','سیسټم ته د تودوخې اضافه کول'),lab('Heat given off by system','نظام سے حرارت کا اخراج','د سیسټم لخوا د تودوخې خوشې کول'),lab('work done by system','نظام کے ذریعے کیا گیا کام','د سیسټم په واسطه ترسره شوی کار')],sourceGap=dict(note='Diagram redrawn as a schematic. The two work arrows are both labelled "work done by system" with signs +W (top) and −W (bottom) as printed.'))]
F.p('a1')
F.e('e111',r'\Delta E=q+w\qquad(11.1)','ΔE = q + w   (11.1)')
F.tb(0)
F.fg(0)
F.p('a2')
F.e('i',r'\Delta E=q-w\qquad(\mathrm{i})','ΔE = q − w   (i)')
F.p('a3')
F.e('ii',r'\Delta E=q+w\qquad(\mathrm{ii})','ΔE = q + w   (ii)')
F.p('t-h','t1')
F.done()
# order fix: 'sa' paragraph is unused as flow label; drop it
s['paras']=[p for p in s['paras'] if not p['id'].endswith('-sa')]
s['sourceNote']='Printed folio 337. The left edge is clipped by the page curl on the paragraph at the foot (first letters of lines cut) but the text is legible. The first line of Fig. 11.2 reads "work done by system" at both arrows (the top arrow is labelled +W and the bottom arrow −W); retained as printed. The diagram and the table are redrawn/recorded here. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='First letters of left-hand lines cut; both work arrows in Fig. 11.2 are labelled "work done by system" in print.')
s['vocabulary']={}
save(s)

# ---------- 343 ----------
s=mk(343,'Pressure-Volume Work · Tidbit: Units of Work · Equation 11.2 · Figure 11.3','دباؤ-حجم کام · معلومات: کام کی اکائیاں · مساوات 11.2 · شکل 11.3','د فشار-حجم کار · ځانګړې یادونه: د کار واحدونه · معادله 11.2 · شکل 11.3','pv-work')
F=Flow(s)
add(s,'a1','The difference between the two equations is that in the first one \'w\' is work done by the system, whereas, in the second one, it is the work done on the system.','دونوں مساواتوں میں فرق یہ ہے کہ پہلی میں \'w\' نظام کے ذریعے کیا گیا کام ہے جبکہ دوسری میں یہ نظام پر کیا گیا کام ہے۔','د دواړو معادلو ترمنځ توپیر دا دی چې په لومړۍ کې \'w\' د سیسټم په واسطه ترسره شوی کار دی، پداسې حال کې چې په دویمه کې دا په سیسټم باندې ترسره شوی کار دی.')
add(s,'h','Pressure-Volume Work','دباؤ-حجم کام','د فشار-حجم کار',kind='heading')
add(s,'b1','The only type of work in thermodynamics is the work of expansion or pressure-volume (PV) work. This is the work done when a system expands against an opposing pressure.','تھرموڈائنامکس میں کام کی واحد قسم پھیلاؤ کا کام یا دباؤ-حجم (PV) کام ہے۔ یہ وہ کام ہے جو اس وقت ہوتا ہے جب نظام مخالف دباؤ کے خلاف پھیلتا ہے۔','په ترموډینامیکس کې د کار یوازینی ډول د پراخېدو کار یا د فشار-حجم (PV) کار دی. دا هغه کار دی چې هغه مهال ترسره کېږي کله چې سیسټم د مخالف فشار په وړاندې پراخېږي.')
add(s,'b2','Consider a gas contained in a cylinder of cross sectional area, A, fitted with a weightless and frictionless piston. The pressure on the piston is P. Since, pressure is force per unit area so P can be written as.','ایک گیس پر غور کریں جو رقبۂ عمودی A والے سلنڈر میں بند ہے جس میں بے وزن اور بے رگڑ پسٹن لگا ہے۔ پسٹن پر دباؤ P ہے۔ چونکہ دباؤ فی اکائی رقبہ قوت ہے اس لیے P کو اس طرح لکھا جا سکتا ہے۔','یو ګاز ته پام وکړئ چې په یو سلنډر کې چې مقطعي ساحه یې A ده او بې وزنه او بې رګړه پسټن لري بند دی. په پسټن فشار P دی. ځکه چې فشار په هر واحد ساحه ځواک دی نو P داسې لیکل کېدای شي.')
add(s,'b3','We know that, work = force × distance','ہم جانتے ہیں کہ کام = قوت × فاصلہ','موږ پوهېږو چې کار = ځواک × واټن')
add(s,'b4','If the piston moves through a distance Δl during expansion, the work done will be,','اگر پھیلاؤ کے دوران پسٹن فاصلہ Δl طے کرے تو کیا گیا کام ہوگا،','که پسټن د پراخېدو پر مهال واټن Δl وهي نو ترسره شوی کار به وي،')
add(s,'b5','Since,','چونکہ،','ځکه چې،')
add(s,'b6','Thus,','لہٰذا،','نو،')
add(s,'t-h','Tidbit','معلومات','ځانګړې یادونه',kind='heading')
add(s,'t0','Units of Work','کام کی اکائیاں','د کار واحدونه',kind='heading')
add(s,'t1','In physics work is product of force and displacement. SI unit of work is Joule (J), which is defined as the work done by a force of one Newton through a displacement of one meter i.e. Newton meter (Nm). One Nm is equal to one Joule which is SI recommended unit of work.','طبیعیات میں کام قوت اور ہٹاؤ کا حاصل ضرب ہے۔ کام کی SI اکائی جول (J) ہے جس کی تعریف ایک نیوٹن کی قوت کے ذریعے ایک میٹر کے ہٹاؤ پر کیے گئے کام کے طور پر کی جاتی ہے یعنی نیوٹن میٹر (Nm)۔ ایک Nm ایک جول کے برابر ہے جو کام کی SI تجویز کردہ اکائی ہے۔','په فزیک کې کار د ځواک او بې ځایه کېدو حاصل ضرب دی. د کار SI واحد جول (J) دی چې د یو نیوټن د ځواک په واسطه د یو متر د بې ځایه کېدو پر مهال د ترسره شوي کار په توګه تعریفېږي یعنې نیوټن متر (Nm). یو Nm له یو جول سره مساوي دی چې د کار SI سپارښتل شوی واحد دی.')
add(s,'t2','Thermal energy is the energy possessed within an object or system due to movement of the particles within the object or the system. Amount of thermal energy in an object is measured in Joules (J).','حرارتی توانائی وہ توانائی ہے جو کسی شے یا نظام کے اندر شے یا نظام کے ذرات کی حرکت کی وجہ سے ہوتی ہے۔ کسی شے میں حرارتی توانائی کی مقدار جول (J) میں ناپی جاتی ہے۔','تودوخیزه انرژي هغه انرژي ده چې په یوه شي یا سیسټم کې د شي یا سیسټم د ذراتو د حرکت له امله وي. په یوه شي کې د تودوخیزې انرژۍ مقدار په جولو (J) کې اندازه کېږي.')
cyl=lambda x,l,fill:(f'<rect x="{x}" y="60" width="130" height="150" fill="#f0f4f8" stroke="#667"/><rect x="{x}" y="{l}" width="130" height="{210-l}" fill="{fill}" opacity=".7"/><rect x="{x+60}" y="25" width="10" height="{l-25}" fill="#aaa"/><rect x="{x+10}" y="{l-8}" width="110" height="10" fill="#888"/>')
pv=(cyl(30,120,'#c078c0')+cyl(210,95,'#c078c0')+tx(95,22,'P<tspan font-size="8" dy="3">ext</tspan>',11)+tx(275,22,'P<tspan font-size="8" dy="3">ext</tspan>',11)+tx(18,170,'l₁',11)+tx(198,155,'l₂',11)+tx(95,230,'V₁',12,'middle',700)+tx(275,230,'V₂',12,'middle',700)
 +'<rect x="380" y="100" width="70" height="40" rx="8" fill="#c078c0" opacity=".8"/>'+tx(415,92,'A',11)+tx(360,60,'Δl',11)+'<path d="M350 70 V100" stroke="#666"/>'+tx(430,170,'ΔV = AΔl',11,'middle',700)+tx(430,195,'volume change',11)+tx(240,258,'Fig. 11.3 Pressure-volume work',12,'middle',700,'#a02040'))
s['figures']=[dict(id='chem11-p343-fig113',svg=svg(480,270,'Gas in a cylinder with a piston expanding from volume V1 to V2 against external pressure, with the volume change shown as a disc of area A and thickness delta l',pv),caption='Fig. 11.3 Pressure-volume work',captionUrdu='شکل 11.3 دباؤ-حجم کام',captionPashto='شکل 11.3 د فشار-حجم کار',labels=[lab('P ext','P ext (بیرونی دباؤ)','P ext (بهرنی فشار)'),lab('V₁','V₁','V₁'),lab('V₂','V₂','V₂'),lab('volume change','حجم میں تبدیلی','د حجم بدلون')],sourceGap=dict(note='Illustration redrawn as a schematic (two cylinders with pistons and a disc showing ΔV = AΔl); the 3-D rendering is not reproduced.'))]
F.p('a1','h','b1','b2')
F.e('p1',r'P=\frac{F}{A}\qquad\text{or}\qquad F=P\times A','P = F/A   or   F = P × A')
F.p('b3','b4')
F.e('w1',r'w=P\times A\times\Delta l','w = P × A × Δl')
F.p('b5')
F.e('w2',r'A\times\Delta l=\Delta V','A × Δl = ΔV')
F.p('b6')
F.e('e112',r'w=P\Delta V\qquad(11.2)','w = PΔV   (11.2)')
F.fg(0)
F.p('t-h','t0','t1','t2')
F.done()
s['sourceNote']='Printed folio 338. The right edge of the Tidbit box is clipped by the page curl (word endings cut: "…work is", "…force and", "…displacement", "…of one", "…Newton meter", etc.); the sentences are completed from the visible parts and are standard definitions; any clipped endings are not otherwise altered. The bottom edge of the figure caption is partly hidden by the footer. The figure is redrawn as a schematic. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Tidbit box right edge clipped (endings completed from context); figure redrawn.')
s['vocabulary']={'pressure-volume work':{'ur':'دباؤ-حجم کام','ps':'د فشار-حجم کار'},'thermal energy':{'ur':'حرارتی توانائی','ps':'تودوخیزه انرژي'}}
save(s)

# ---------- 344 ----------
s=mk(344,'Equations 11.3–11.5 · Example 11.1 · Self-Assessment · 11.5 Standard State and Standard Enthalpy changes','مساواتیں 11.3–11.5 · مثال 11.1 · خود جائزہ · 11.5 معیاری حالت اور معیاری انتھالپی تبدیلیاں','معادلې 11.3–11.5 · بېلګه 11.1 · ځان ارزونه · 11.5 معیاري حالت او معیاري انتالپي بدلونونه','example111-standard-enthalpy')
F=Flow(s)
add(s,'a1','This is called pressure-volume work and is positive when it is done on the system. Here, ΔV is change in volume in the case of expansion or contraction. In the light of Equation 11.2 Equation 11.1 becomes','اسے دباؤ-حجم کام کہتے ہیں اور یہ مثبت ہوتا ہے جب یہ نظام پر کیا جائے۔ یہاں ΔV پھیلاؤ یا سکڑاؤ کی صورت میں حجم میں تبدیلی ہے۔ مساوات 11.2 کی روشنی میں مساوات 11.1 بن جاتی ہے','دې ته د فشار-حجم کار ویل کېږي او مثبت وي کله چې په سیسټم باندې ترسره شي. دلته ΔV د پراخېدو یا ټوکېدو په حالت کې د حجم بدلون دی. د 11.2 معادلې په رڼا کې 11.1 معادله کېږي')
add(s,'a2','Whereas, work is negative (−PΔV), when it is done by the system.','جبکہ کام منفی (−PΔV) ہوتا ہے جب یہ نظام کے ذریعے کیا جائے۔','پداسې حال کې چې کار منفي (−PΔV) وي کله چې د سیسټم په واسطه ترسره شي.')
add(s,'a3','If the volume of the system is kept constant then ΔV=0 and hence, PΔV=0, so Eq.11.3, at constant volume becomes','اگر نظام کا حجم مستقل رکھا جائے تو ΔV=0 اور لہٰذا PΔV=0 ہوتا ہے، اس لیے مستقل حجم پر مساوات 11.3 بن جاتی ہے','که د سیسټم حجم ثابت وساتل شي نو ΔV=0 او نو PΔV=0 وي، نو په ثابت حجم کې معادله 11.3 کېږي')
add(s,'a4','Hence, heat absorbed at constant volume is utilized to increase the internal energy only and no work is done.','لہٰذا مستقل حجم پر جذب کی گئی حرارت صرف اندرونی توانائی بڑھانے میں استعمال ہوتی ہے اور کوئی کام نہیں ہوتا۔','نو په ثابت حجم کې جذب شوې تودوخه یوازې د داخلي انرژۍ د زیاتولو لپاره کارول کېږي او هېڅ کار نه ترسره کېږي.')
add(s,'a5','Units of work and heat in SI system are,','SI نظام میں کام اور حرارت کی اکائیاں ہیں،','په SI سیسټم کې د کار او تودوخې واحدونه دي،')
add(s,'e','Example 11.1','مثال 11.1','بېلګه 11.1',kind='heading')
add(s,'q','Calculate the work done when 1 mole of an ideal gas expands from 15 dm³ to 20 dm³ against a constant external pressure of 2 atmospheres.','وہ کام معلوم کریں جب 1 مول مثالی گیس 15 dm³ سے 20 dm³ تک 2 ماحول کے مستقل بیرونی دباؤ کے خلاف پھیلے۔','هغه کار محاسبه کړئ کله چې د ایډیال ګاز 1 مول له 15 dm³ څخه 20 dm³ ته د 2 اتموسفیرو د ثابت بهرني فشار په وړاندې پراخ شي.')
add(s,'s','Solution:','حل:','حل:',kind='heading')
add(s,'s1','Since','چونکہ','ځکه چې')
add(s,'sa','Self-Assessment','خود جائزہ','ځان ارزونه',kind='heading')
add(s,'sa1','What are the consequences of an increase in internal energy of a chemical system.','کیمیائی نظام کی اندرونی توانائی میں اضافے کے نتائج کیا ہیں۔','د یو کيمياوي سیسټم په داخلي انرژۍ کې د زیاتوالي پایلې څه دي.',role='question')
add(s,'sa2','Define first law of thermodynamics.','تھرموڈائنامکس کے پہلے قانون کی تعریف کریں۔','د ترموډینامیکس لومړی قانون تعریف کړئ.',role='question')
add(s,'h','11.5 Standard State and Standard Enthalpy changes','11.5 معیاری حالت اور معیاری انتھالپی تبدیلیاں','11.5 معیاري حالت او معیاري انتالپي بدلونونه',kind='heading')
add(s,'b1','First law of thermodynamics can be applied to processes carried out under different conditions. There are two main conditions under which the processes can occur, i.e., at constant volume and at constant pressure which is the most common way of carrying out chemical reactions. Eq.(11.3) shows the first law of thermodynamics. It has also been shown that processes at constant volume follow the equation ΔE=q_v.','تھرموڈائنامکس کے پہلے قانون کا اطلاق مختلف حالات میں کیے جانے والے عملوں پر کیا جا سکتا ہے۔ دو بنیادی حالات ہیں جن میں عمل ہو سکتے ہیں، یعنی مستقل حجم پر اور مستقل دباؤ پر جو کیمیائی تعاملات کرنے کا سب سے عام طریقہ ہے۔ مساوات (11.3) تھرموڈائنامکس کا پہلا قانون ظاہر کرتی ہے۔ یہ بھی دکھایا گیا ہے کہ مستقل حجم پر عمل مساوات ΔE=q_v کی پیروی کرتے ہیں۔','د ترموډینامیکس لومړی قانون په بېلابېلو شرایطو کې ترسره شویو پروسو باندې تطبیقېدای شي. دوه اصلي شرایط شته چې په هغو کې پروسې پېښېدای شي، یعنې په ثابت حجم کې او په ثابت فشار کې چې د کيمياوي تعاملاتو د ترسره کولو تر ټولو عام ډول دی. معادله (11.3) د ترموډینامیکس لومړی قانون ښيي. دا هم ښودل شوي چې په ثابت حجم کې پروسې د ΔE=q_v معادله تعقیبوي.')
add(s,'b2','Now let us establish equation for most commonly occurring processes which take place at constant pressure. Starting from first law equation','اب آئیے ان عملوں کے لیے مساوات قائم کریں جو سب سے زیادہ عام طور پر مستقل دباؤ پر ہوتے ہیں۔ پہلے قانون کی مساوات سے آغاز کرتے ہوئے','اوس راځئ د هغو پروسو لپاره معادله رامنځته کړو چې تر ټولو ډېر په ثابت فشار کې پېښېږي. د لومړي قانون له معادلې پیل کولو سره')
add(s,'b3',f"When we supply heat 'q' to a gas it expands to keep its pressure constant which results in performing work on the surrounding against external{SO}",f"جب ہم گیس کو حرارت 'q' فراہم کرتے ہیں تو وہ اپنا دباؤ مستقل رکھنے کے لیے پھیلتی ہے جس کے نتیجے میں بیرونی {SO} کے خلاف ماحول پر کام ہوتا ہے",f"کله چې موږ ګاز ته تودوخه 'q' ورکوو نو دا خپل فشار ثابت ساتلو لپاره پراخېږي چې په پایله کې د بهرني {SO} په وړاندې په شاوخوا کار ترسره کېږي")
F.p('a1')
F.e('e113',r'\Delta E=q+P\Delta V\qquad(11.3)','ΔE = q + PΔV   (11.3)')
F.p('a2')
F.e('e114',r'q=\Delta E-P\,\Delta V\qquad(11.4)','q = ΔE − P ΔV   (11.4)')
F.p('a3')
F.e('e115',r'\Delta E=q_v\qquad(11.5)','ΔE = q_v   (11.5)')
F.p('a4','a5')
F.e('u',r'\mathrm{Nm^{-2}\times m^3=Nm\ or\ Joules\ (J)}','Nm⁻² × m³ = Nm or Joules (J)')
F.p('e','q','s')
F.e('x1',r'P=2\ \mathrm{atm}','P = 2 atm')
F.e('x2',r'\Delta V=V_2-V_1=20\ \mathrm{dm^3}-15\ \mathrm{dm^3}=5\ \mathrm{dm^3}','ΔV = V₂ − V₁ = 20 dm³ − 15 dm³ = 5 dm³')
F.p('s1')
F.e('x3',r'w=P\Delta V','w = PΔV')
F.e('x4',r'w=2\ \mathrm{atm}\times5\ \mathrm{dm^3}=10\ \mathrm{atm\,dm^3}','w = 2 atm × 5 dm³ = 10 atm dm³')
F.p('sa','sa1','sa2','h','b1','b2')
F.e('x5',r'\Delta E=q+P\Delta V\qquad(11.3)','ΔE = q + PΔV   (11.3)')
F.p('b3')
F.done()
s['sourceNote']='Printed folio 339. The scan is skewed; the right edge is clipped at the foot ("…against external [pressure]") and the sentence continues on the next page. The Example solution ends at w = 10 atm dm³ as printed (no conversion to joules). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; last sentence is cut at the right edge and continues on the next page.')
s['vocabulary']={}
save(s)
