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
    def done(s_): s_.s['flow']=s_.f
CH='chem11-acids-bases-salts'
def mk(n,title,ur,ps,sid): return page(n,CH,title,ur,ps,sid)
def Q(s,key,en,ur,ps): add(s,key,en,ur,ps,role='question')

# ---------- 269 ----------
s=mk(269,'Key Points (Unit 8)','اہم نکات (یونٹ 8)','مهم ټکي (۸ یونټ)','key-points-1')
head(s,'kp','KEY POINTS','اہم نکات','مهم ټکي')
KP=[(f'Brontsed acid is a species (molecule or ion) which donates or tends to don{SO} a proton.',f'برونسٹڈ تیزاب ایک نوع (سالمہ یا آئن) ہے جو پروٹان عطا کرتی ہے یا عطا کرنے کا رجحان رکھتی ہے {SO}۔',f'برونسټډ اسید یو ډول (مالیکول یا آیون) دی چې پروټون ورکوي یا ورکولو تمایل لري {SO}.'),
(f'Brontsed base is a species (molecule or ion) which accepts or tends to acc{SO} a proton.',f'برونسٹڈ اساس ایک نوع (سالمہ یا آئن) ہے جو پروٹان قبول کرتی ہے یا قبول کرنے کا رجحان رکھتی ہے {SO}۔',f'برونسټډ القلي یو ډول (مالیکول یا آیون) دی چې پروټون منل کوي یا منلو تمایل لري {SO}.'),
(f'Stronger Brontsed acids are those that lose their protons more easily t{SO} other acids.',f'مضبوط برونسٹڈ تیزاب وہ ہیں جو اپنے پروٹان دوسرے تیزابوں کے مقابلے میں زیادہ آسانی سے کھو دیتے ہیں {SO}۔',f'قوي برونسټډ اسیدونه هغه دي چې خپل پروټونونه د نورو اسیدونو په پرتله په اسانۍ له لاسه ورکوي {SO}.'),
(f'Stronger Brontsed bases are those that hold on to protons more stron{SO} than other bases.',f'مضبوط برونسٹڈ اساس وہ ہیں جو پروٹان کو دوسرے اساسوں کے مقابلے میں زیادہ مضبوطی سے تھامے رکھتے ہیں {SO}۔',f'قوي برونسټډ القلي هغه دي چې پروټونونه د نورو القليو په پرتله ډېر پياوړي ټینګ ساتي {SO}.'),
(f'A species formed from an acid by the loss of a proton is called the conjug{SO} base of that acid and a specie formed from a base by gaining a proton{SO} called the conjugate acid of that base.',f'کسی تیزاب سے پروٹان کے نکلنے سے بننے والی نوع اس تیزاب کا مزدوج {SO} اساس کہلاتی ہے اور کسی اساس میں پروٹان کے شامل ہونے سے بننے والی نوع {SO} اس اساس کا مزدوج تیزاب کہلاتی ہے۔',f'هغه ډول چې له یو اسید څخه د پروټون د له لاسه ورکولو سره جوړېږي د هغه اسید مزدوج {SO} القلي بلل کېږي او هغه ډول چې له یو القلي سره د پروټون په ترلاسه کولو سره جوړېږي {SO} د هغه القلي مزدوج اسید بلل کېږي.'),
('A strong acid is one that ionizes completely in aqueous solution.','مضبوط تیزاب وہ ہے جو آبی محلول میں مکمل طور پر آئنائز ہو جائے۔','قوي اسید هغه دی چې په اوبیز محلول کې په بشپړ ډول آیونایز شي.'),
('A weak acid is one that ionizes only to a limited extent in water.','کمزور تیزاب وہ ہے جو پانی میں صرف محدود حد تک آئنائز ہوتا ہے۔','ضعیف اسید هغه دی چې په اوبو کې یوازې محدودې اندازې ته آیونایز کېږي.'),
(f'Acid-base reaction involves the transfer of a proton from an acid to a base{SO} weak acid has a strong conjugate base while a weak base has always a stro{SO} conjugate acid.',f'تیزاب اساس تعامل میں پروٹان کی منتقلی تیزاب سے اساس کی طرف ہوتی ہے {SO} کمزور تیزاب کا مزدوج اساس مضبوط ہوتا ہے جبکہ کمزور اساس کا مزدوج تیزاب ہمیشہ مضبوط {SO} ہوتا ہے۔',f'د اسید-القلي په تعامل کې د پروټون لېږد له اسید څخه القلي ته رامنځته کېږي {SO} ضعیف اسید قوي مزدوج القلي لري پداسې حال کې چې ضعیف القلي تل قوي {SO} مزدوج اسید لري.'),
(f'Ionic product of water, K_w is a constant quantity equal to 1 × 10⁻¹⁴ at 25°C{SO}',f'پانی کا آئنی حاصل ضرب K_w ایک مستقل مقدار ہے جو 25°C پر 1 × 10⁻¹⁴ کے برابر ہے {SO}',f'د اوبو آیوني حاصل ضرب K_w یو ثابت مقدار دی چې په 25°C کې له 1 × 10⁻¹⁴ سره مساوي دی {SO}'),
(f'When a base completely dissociates in water to yield aqueous OH⁻ ions, th{SO} solution is referred as alkaline.',f'جب کوئی اساس پانی میں مکمل طور پر تفکیک ہو کر آبی OH⁻ آئن دے تو {SO} محلول القلی کہلاتا ہے۔',f'کله چې یو القلي په اوبو کې په بشپړ ډول تجزیه شي او اوبیز OH⁻ آیونونه ورکړي نو {SO} محلول القلي بلل کېږي.'),
('Strong bases are all strong electrolytes that ionize completely in water.','مضبوط اساس سب مضبوط برق پاش ہیں جو پانی میں مکمل طور پر آئنائز ہوتے ہیں۔','قوي القلي ټول قوي الکترولایټونه دي چې په اوبو کې په بشپړ ډول آیونایز کېږي.'),
('A weak base is one that ionizes only to a limited extent in water.','کمزور اساس وہ ہے جو پانی میں صرف محدود حد تک آئنائز ہوتا ہے۔','ضعیف القلي هغه دی چې په اوبو کې یوازې محدودې اندازې ته آیونایز کېږي.'),
(f'In the self-ionization of water, two water molecules produce a hydronium io{SO} and a hydroxide ion by transfer of a proton. This is called the autoionizat{SO} of water.',f'پانی کی خود آئنائزیشن میں دو پانی کے سالمے پروٹان کی منتقلی سے ایک ہائیڈرونیم {SO} آئن اور ایک ہائیڈرو آکسائیڈ آئن پیدا کرتے ہیں۔ اسے پانی کی ازخود آئنائزیشن {SO} کہتے ہیں۔',f'د اوبو په ځان آیونایزیشن کې دوه د اوبو مالیکولونه د پروټون د لېږد په واسطه یو هایدرونیم {SO} آیون او یو هایدروکسایډ آیون جوړوي. دې ته د اوبو اتو آیونایزیشن {SO} ویل کېږي.'),
('Water is an amphoteric substance: it behaves both as an acid and a base','پانی ایک ایمفوٹیرک مادہ ہے: یہ تیزاب اور اساس دونوں کی طرح برتاؤ کرتا ہے','اوبه یو امفوټریک مواد دي: دا د اسید او القلي دواړو په څېر چلند کوي'),
(f'pH is the negative logarithm of the H⁺ or H₃O⁺ concentration in moles pe{SO} dm³, smaller the value of pH, greater is the acidity.',f'pH H⁺ یا H₃O⁺ کے ارتکاز کا منفی لوگارتھم ہے، مول فی {SO} dm³ میں؛ pH کی قیمت جتنی چھوٹی ہو تیزابیت اتنی ہی زیادہ ہوتی ہے۔',f'pH د H⁺ یا H₃O⁺ د غلظت منفي لوګاریتم دی، په مولونو په {SO} هر dm³ کې؛ د pH ارزښت څومره کوچنی وي اسیدیت به هماغومره ډېر وي.'),
(f'The pOH is defined as the negative logarithm of the OH⁻ concentration{SO} moles per dm³.',f'pOH کی تعریف OH⁻ کے ارتکاز کے منفی لوگارتھم کے طور پر کی جاتی ہے {SO} مول فی dm³۔',f'pOH د OH⁻ د غلظت د منفي لوګاریتم په توګه تعریفېږي {SO} په مولونو په هر dm³ کې.'),
(f'K_a, the acid ionization constant, is the equilibrium constant for the ionizat{SO} of an acid.',f'K_a، تیزابی آئنائزیشن مستقلہ، کسی تیزاب کی آئنائزیشن کا توازنی مستقلہ ہے {SO}۔',f'K_a، د اسید د آیونایزیشن ثابت، د یو اسید د آیونایزیشن د تعادل ثابت دی {SO}.')]
for i,(e,u,p) in enumerate(KP,1): add(s,f'k{i}',e,u,p)
s['equations']=[eqn(269,'k9e',r'K_w=[\mathrm{H^+}][\mathrm{OH^-}]=1\times10^{-14}','K_w = [H⁺][OH⁻] = 1 × 10⁻¹⁴'),eqn(269,'hx',r'\mathrm{HX_{(aq)}\rightleftharpoons H^+_{(aq)}+X^-_{(aq)}}','HX(aq) ⇌ H⁺(aq) + X⁻(aq)')]
s['flow']=[dict(type='paragraphs',ids=ids(s,0,17)),dict(type='equation',index=1)]
s['sourceNote']='Printed folio 264. The right edge is clipped by the page curl on most bullets; clipped endings are marked [scan obscured] and not inferred. "Brontsed" is a printed misspelling of Bronsted (retained). The K_w bullet and the final K_a bullet continue with their equations (K_w line printed inside the bullet; HX ⇌ H⁺ + X⁻ at the foot, the K_a expression continues on the next page). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; "Brontsed" misspelling retained; K_a expression continues on the next page.')
s['vocabulary']={'amphoteric':{'ur':'ایمفوٹیرک','ps':'امفوټریک'},'autoionization':{'ur':'خود آئنائزیشن','ps':'ځان آیونایزیشن'}}
# the Kw equation is shown within bullet 9; keep eq index 0 reserved in the equation list
s['flow']=[dict(type='paragraphs',ids=ids(s,0,10)),dict(type='equation',index=0),dict(type='paragraphs',ids=ids(s,10,18)),dict(type='equation',index=1)]
save(s)

# ---------- 270 ----------
s=mk(270,'Key Points (continued)','اہم نکات (جاری)','مهم ټکي (دوام)','key-points-2')
F=Flow(s)
KP=[('A strong acid has a very large K_a value.','مضبوط تیزاب کی K_a کی قیمت بہت بڑی ہوتی ہے۔','قوي اسید ډېر لوی K_a ارزښت لري.'),
('pK_a is the negative logarithm of K_a. So greater the value of pK_a, lower is the strength of an acid.','pK_a، K_a کا منفی لوگارتھم ہے۔ لہٰذا pK_a کی قیمت جتنی زیادہ ہو تیزاب کی قوت اتنی ہی کم ہوتی ہے۔','pK_a د K_a منفي لوګاریتم دی. نو د pK_a ارزښت څومره ډېر وي د اسید قوت به هماغومره کم وي.'),
('Base-ionization constant, K_b, is the dissociation constant of a base and pK_b is the negative logarithm of K_b. If a substance has greater value of dissociation constant K_b, and smaller pK_b value then it will be strong base.','اساسی آئنائزیشن مستقلہ K_b کسی اساس کا تفکیک مستقلہ ہے اور pK_b، K_b کا منفی لوگارتھم ہے۔ اگر کسی مادے کے تفکیک مستقلہ K_b کی قیمت زیادہ اور pK_b کی قیمت کم ہو تو وہ مضبوط اساس ہوگا۔','د القلي د آیونایزیشن ثابت K_b د یو القلي د تجزیې ثابت دی او pK_b د K_b منفي لوګاریتم دی. که یو مواد د تجزیې د ثابت K_b ډېر ارزښت او کوچنی pK_b ارزښت ولري نو دا به قوي القلي وي.'),
('K_b, the base ionization constant, is the equilibrium constant for the ionization of base.','K_b، اساسی آئنائزیشن مستقلہ، اساس کی آئنائزیشن کا توازنی مستقلہ ہے۔','K_b، د القلي د آیونایزیشن ثابت، د القلي د آیونایزیشن د تعادل ثابت دی.'),
('A Lewis acid is a species that can accept an electron pair from another species.','لیوس تیزاب وہ نوع ہے جو کسی دوسری نوع سے الیکٹران جوڑا قبول کر سکے۔','لیویس اسید هغه ډول دی چې له بل ډول څخه د الکترون جوړه منل کولای شي.'),
('A Lewis base is a species that can donate an electron pair to another species.','لیوس اساس وہ نوع ہے جو کسی دوسری نوع کو الیکٹران جوڑا عطا کر سکے۔','لیویس القلي هغه ډول دی چې بل ډول ته د الکترون جوړه ورکولای شي.'),
('Lewis acid – base reaction involves the exchange of a proton from an acid to a base. A weak acid has a strong conjugate base while a weak base has always a strong conjugate acid.','لیوس تیزاب اساس تعامل میں تیزاب سے اساس کو پروٹان کا تبادلہ شامل ہوتا ہے۔ کمزور تیزاب کا مزدوج اساس مضبوط ہوتا ہے جبکہ کمزور اساس کا مزدوج تیزاب ہمیشہ مضبوط ہوتا ہے۔','د لیویس اسید-القلي په تعامل کې له اسید څخه القلي ته د پروټون تبادله شامله ده. ضعیف اسید قوي مزدوج القلي لري پداسې حال کې چې ضعیف القلي تل قوي مزدوج اسید لري.'),
('A solution, which resists a change in pH when a small amount of a strong acid or a strong base is added to it, is called a buffer solution.','وہ محلول جو مضبوط تیزاب یا مضبوط اساس کی تھوڑی مقدار شامل کرنے پر pH کی تبدیلی کی مزاحمت کرتا ہے بفر محلول کہلاتا ہے۔','هغه محلول چې د قوي اسید یا قوي القلي د لږ مقدار د اضافه کولو په وخت د pH د بدلون مقاومت کوي د بفر محلول بلل کېږي.'),
('Acid buffer contains a weak acid and its salt with a strong base.','تیزابی بفر میں ایک کمزور تیزاب اور مضبوط اساس کے ساتھ اس کا نمک ہوتا ہے۔','اسیدي بفر یو ضعیف اسید او د قوي القلي سره د هغه مالګه لري.'),
('Basic buffer contains a weak base and its salt with a strong acid.','اساسی بفر میں ایک کمزور اساس اور مضبوط تیزاب کے ساتھ اس کا نمک ہوتا ہے۔','القلي بفر یو ضعیف القلي او د قوي اسید سره د هغه مالګه لري.'),
('Buffer action is the resistance offered by a buffer solution to change in pH on the addition of small amount of an acid or base.','بفر عمل وہ مزاحمت ہے جو بفر محلول تیزاب یا اساس کی تھوڑی مقدار کے اضافے پر pH کی تبدیلی کے خلاف پیش کرتا ہے۔','د بفر عمل هغه مقاومت دی چې د بفر محلول د اسید یا القلي د لږ مقدار د اضافه کولو په وخت د pH د بدلون په وړاندې وړاندې کوي.'),
('Hydrolysis is the reaction of an anion or cation of a salt with water accompanied by cleavage of H–O–H bond.','ہائیڈرولائسس نمک کے اینائن یا کیٹائن کا پانی کے ساتھ تعامل ہے جس کے ساتھ H–O–H بندھن ٹوٹتا ہے۔','هایدرولیز د مالګې د انیاین یا کیټاین تعامل له اوبو سره دی چې د H–O–H بند د ماتېدو سره مل وي.')]
for i,(e,u,p) in enumerate(KP,1): add(s,f'k{i}',e,u,p)
F.e('ka',r'K_a=\frac{[\mathrm{H^+}][\mathrm{X^-}]}{[\mathrm{HX}]}','K_a = [H⁺][X⁻] / [HX]')
F.p('k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12')
F.done()
s['sourceNote']='Printed folio 265. The top equation K_a = [H⁺][X⁻]/[HX] completes the last bullet of the previous page. The left edge is clipped by the page curl (the first words of most bullets are cut) but the sentences are legible. Item 7 is printed as "Lewis acid – base reaction involves the exchange of a proton from an acid to a base…" (retained). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='First words of many left-hand lines are cut by the page curl.')
s['vocabulary']={}
save(s)

# ---------- 271 ----------
s=mk(271,'Unit 8 Exercise · Choose the correct option (1–12)','یونٹ 8 مشق · درست جواب منتخب کریں (1–12)','د 8 یونټ تمرین · سم انتخاب وټاکئ (1–12)','exercise-mcq-1')
head(s,'ex','EXERCISE','مشق','تمرین')
head(s,'ch','Choose the correct option.','درست جواب منتخب کریں۔','سم انتخاب وټاکئ.')
Qs=[('Which one is the example of buffer','بفر کی مثال کون سی ہے','د بفر بېلګه کومه ده',[('HCl/ NaCl','HCl/ NaCl (ہائیڈروکلورک ایسڈ/سوڈیم کلورائیڈ)','HCl/ NaCl (هایدروکلوریک اسید/سوډیم کلوراید)'),('NaOH/ H₂CO₃','NaOH/ H₂CO₃ (سوڈیم ہائیڈرو آکسائیڈ/کاربونک ایسڈ)','NaOH/ H₂CO₃ (سوډیم هایدروکسایډ/کاربونیک اسید)'),('NH₄OH/NH₄Cl',None,None),('NaOH/ NaCl','NaOH/ NaCl (سوڈیم ہائیڈرو آکسائیڈ/سوڈیم کلورائیڈ)','NaOH/ NaCl (سوډیم هایدروکسایډ/سوډیم کلوراید)')]),
('Conjugate acid – base pair differs by','مزدوج تیزاب اساس جوڑا کس سے مختلف ہوتا ہے','مزدوج اسید-القلي جوړه په کوم توپیر لري',[('A proton','ایک پروٹان','یو پروټون'),('A proton pair','ایک پروٹان جوڑا','یوه پروټون جوړه'),('An electron','ایک الیکٹران','یو الکترون'),('An electron pair','ایک الیکٹران جوڑا','یوه الکترون جوړه')]),
(f'1 M solution of Ca(OH)₂ is mixed with 1M solution of HCl. The produc{SO} solution is','1 M Ca(OH)₂ محلول کو 1M HCl محلول کے ساتھ ملایا جاتا ہے۔ حاصل محلول ہے','1 M Ca(OH)₂ محلول له 1M HCl محلول سره ګډېږي. پایله محلول دی',[('Acidic','تیزابی','اسیدي'),('Basic','اساسی','القلي'),('Neutral','معتدل','خنثی'),('Amphoteric','ایمفوٹیرک','امفوټریک')]),
('Cl⁻ is the conjugate base of','Cl⁻ کس کا مزدوج اساس ہے','Cl⁻ د کوم مزدوج القلي دی',[('AlCl₃','AlCl₃ (ایلومینیم کلورائیڈ)','AlCl₃ (المونیم کلوراید)'),('NaCl','NaCl (سوڈیم کلورائیڈ)','NaCl (سوډیم کلوراید)'),('HCl',None,None),('KCl',None,None)]),
('pH of an aqueous solution is 9. Its pOH is','ایک آبی محلول کا pH 9 ہے۔ اس کا pOH ہے','د یو اوبیز محلول pH 9 دی. د هغه pOH دی',[('11',None,None),('9',None,None),('7',None,None),('5',None,None)]),
('Salt of a weak base and strong acid has a pH, approximately','کمزور اساس اور مضبوط تیزاب کے نمک کا pH تقریباً ہوتا ہے','د ضعیف القلي او قوي اسید د مالګې pH نږدې دی',[('8',None,None),('6',None,None),('7',None,None),('9',None,None)]),
('The unit of K_w is,','K_w کی اکائی ہے،','د K_w واحد دی،',[('Mole dm⁻³','مول dm⁻³','مول dm⁻³'),('Mole⁻² dm⁻⁶','مول⁻² dm⁻⁶','مول⁻² dm⁻⁶'),('Mole² dm⁻⁶','مول² dm⁻⁶','مول² dm⁻⁶'),('Mole² dm⁻³','مول² dm⁻³','مول² dm⁻³')]),
('Very large K_a value means that the substance is a','K_a کی بہت بڑی قیمت کا مطلب ہے کہ مادہ ہے','ډېر لوی K_a ارزښت معنا لري چې مواد دی',[('Strong acid','مضبوط تیزاب','قوي اسید'),('Weak acid','کمزور تیزاب','ضعیف اسید'),('Weak base','کمزور اساس','ضعیف القلي'),('Strong base','مضبوط اساس','قوي القلي')]),
('In following halogen acids which one is the strongest acid','درج ذیل ہیلوجن تیزابوں میں سے کون سا سب سے مضبوط تیزاب ہے','په لاندې هلوجن اسیدونو کې کوم یو تر ټولو قوي اسید دی',[('HF',None,None),('HCl',None,None),('HBr',None,None),('HI',None,None)]),
('Which one of following solution have zero pH','درج ذیل میں سے کس محلول کا pH صفر ہے','له لاندې محلولونو څخه کوم یو pH صفر لري',[('1M HCl',None,None),('0.5M H₂SO₄',None,None),('0.1M HNO₃',None,None),('1M CH₃COOH','1M CH₃COOH (ایسیٹک ایسڈ)','1M CH₃COOH (اسیټیک اسید)')]),
('Which one is not true for acids','تیزابوں کے لیے کون سی بات درست نہیں ہے','د اسیدونو لپاره کومه خبره سمه نه ده',[('Liberate H⁺','H⁺ خارج کرنا','H⁺ خوشې کول'),('Accepts electrons','الیکٹران قبول کرنا','الکترونونه منل'),('Have high pH','بلند pH ہونا','لوړ pH لرل'),('Turn blue litmus red','نیلے لٹمس کو سرخ کرنا','نیلی لیټمس سور کول')]),
('10⁻³ moles of HNO₃ is dissolved /dm³. Its pH is','10⁻³ مول HNO₃ فی dm³ میں حل کیا گیا ہے۔ اس کا pH ہے','10⁻³ مول HNO₃ په هر dm³ کې حل شوی. د هغه pH دی',[('−3',None,None),('5',None,None),('3',None,None),('1',None,None)])]
for n,(q,u,p,o) in enumerate(Qs,1): mcq(s,n,q,u,p,o,271)
s['flow']=[dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 266. The scan is slightly skewed and the right edge is clipped at the end of question 3 ("The produc…" [scan obscured]). In question 4 the printed first option is labelled "c." (a source misprint; it is the first option here). Option labels in questions 7 are printed as "Mole.dm⁻³", "Mole⁻².dm⁻⁶", "Mole².dm⁻⁶", "Mole².dm⁻³". A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Question 4 first option is mislabelled "c." on the source; question 3 text is cut at the right edge.')
s['vocabulary']={'conjugate':{'ur':'مزدوج','ps':'مزدوج'}}
save(s)

# ---------- 272 ----------
s=mk(272,'Unit 8 Exercise (continued) · Short, Numerical and Descriptive Questions','یونٹ 8 مشق (جاری) · مختصر، عددی اور تفصیلی سوالات','د 8 یونټ تمرین (دوام) · لنډې، عددي او تشریحي پوښتنې','exercise-questions')
Qs=[('A solution with a pK_a value of 9, suggest that it is a','وہ محلول جس کی pK_a کی قیمت 9 ہے ظاہر کرتا ہے کہ یہ ہے','هغه محلول چې د pK_a ارزښت یې 9 دی وړاندیز کوي چې دا دی',[('Strong acid','مضبوط تیزاب','قوي اسید'),('Weak acid','کمزور تیزاب','ضعیف اسید'),('Weak base','کمزور اساس','ضعیف القلي'),('Strong base','مضبوط اساس','قوي القلي')]),
('Cl⁻ is a / an','Cl⁻ ہے','Cl⁻ دی',[('Acid','تیزاب','اسید'),('base','اساس','القلي'),('Amphoteric','ایمفوٹیرک','امفوټریک'),('None','کوئی نہیں','هېڅ یو نه')]),
('An acidic buffer solution can be prepared by mixing','ایک تیزابی بفر محلول ملانے سے تیار کیا جا سکتا ہے','یو اسیدي بفر محلول د ګډولو په واسطه جوړېدای شي',[('Weak acid and its salt with strong base','کمزور تیزاب اور مضبوط اساس کے ساتھ اس کا نمک','ضعیف اسید او د قوي القلي سره د هغه مالګه'),('Strong acid and its salt with weak base','مضبوط تیزاب اور کمزور اساس کے ساتھ اس کا نمک','قوي اسید او د ضعیف القلي سره د هغه مالګه'),('Weak base and its salt with strong acid','کمزور اساس اور مضبوط تیزاب کے ساتھ اس کا نمک','ضعیف القلي او د قوي اسید سره د هغه مالګه'),('Strong base and its salt with weak acid','مضبوط اساس اور کمزور تیزاب کے ساتھ اس کا نمک','قوي القلي او د ضعیف اسید سره د هغه مالګه')])]
for n,(q,u,p,o) in enumerate(Qs,13): mcq(s,n,q,u,p,o,272)
head(s,'sq','Short Questions','مختصر سوالات','لنډې پوښتنې')
SQ=[('What information would you use to support the view that water can act either as a weak acid or as a weak base?','آپ کون سی معلومات استعمال کریں گے جو اس نظریے کی تائید کریں کہ پانی کمزور تیزاب یا کمزور اساس دونوں کی طرح کام کر سکتا ہے؟','تاسو به کومه معلومات وکاروئ چې د دې نظر ملاتړ وکړي چې اوبه د ضعیف اسید یا ضعیف القلي په توګه عمل کولای شي؟'),
('Explain that why the sum of pK_a and pK_b is always equal to 14.','وضاحت کریں کہ pK_a اور pK_b کا مجموعہ ہمیشہ 14 کے برابر کیوں ہوتا ہے۔','تشریح کړئ چې د pK_a او pK_b مجموعه تل له 14 سره ولې مساوي وي.'),
('Explain why the conjugate base of a strong acid is a weak base and the conjugate acid of a strong base is a weak acid.','وضاحت کریں کہ مضبوط تیزاب کا مزدوج اساس کمزور اساس اور مضبوط اساس کا مزدوج تیزاب کمزور تیزاب کیوں ہوتا ہے۔','تشریح کړئ چې د قوي اسید مزدوج القلي ولې ضعیف القلي او د قوي القلي مزدوج اسید ولې ضعیف اسید وي.'),
('Justify your answer with equations that CH₃COONa gives a basic solution while NH₄Cl an acidic solution in water.','معادلات کے ساتھ اپنے جواب کی توجیہ کریں کہ CH₃COONa پانی میں اساسی محلول دیتا ہے جبکہ NH₄Cl تیزابی محلول۔','خپل ځواب په معادلو سره توجیه کړئ چې CH₃COONa په اوبو کې القلي محلول ورکوي پداسې حال کې چې NH₄Cl اسیدي محلول.'),
('Why do you call AlCl₃ and BF₃ as Lewis acids, Cl⁻ and NH₃ as Lewis bases?','آپ AlCl₃ اور BF₃ کو لیوس تیزاب اور Cl⁻ اور NH₃ کو لیوس اساس کیوں کہتے ہیں؟','تاسو AlCl₃ او BF₃ ولې لیویس اسیدونه او Cl⁻ او NH₃ ولې لیویس القلي بولئ؟')]
for i,(e,u,p) in enumerate(SQ,1): Q(s,f's{i}',f'{i}. {e}',f'{i}۔ {u}',f'{i}. {p}')
head(s,'nq','Numerical Questions','عددی سوالات','عددي پوښتنې')
NQ=[('What is the pH of 0.0001M Ca(OH)₂ solution. (Ans. pH = 10.3)','0.0001M Ca(OH)₂ محلول کا pH کیا ہے۔ (جواب: pH = 10.3)','د 0.0001M Ca(OH)₂ محلول pH څومره دی. (ځواب: pH = 10.3)'),
(f'What is [H⁺] and [OH⁻] ions concentration of solution, which has a pH of 4.87? (Ans. [H⁺] = 1.35 × 10⁻⁵, [OH⁻] = 7.41 × 10⁻{SO})',f'اس محلول میں [H⁺] اور [OH⁻] آئنوں کا ارتکاز کیا ہے جس کا pH 4.87 ہے؟ (جواب: [H⁺] = 1.35 × 10⁻⁵، [OH⁻] = 7.41 × 10⁻{SO})',f'د هغه محلول د [H⁺] او [OH⁻] آیونونو غلظت څومره دی چې pH یې 4.87 دی؟ (ځواب: [H⁺] = 1.35 × 10⁻⁵، [OH⁻] = 7.41 × 10⁻{SO})'),
('What is the pH of a 1.0 × 10⁻⁴ M KOH solution? (Ans. pH = 10)','1.0 × 10⁻⁴ M KOH محلول کا pH کیا ہے؟ (جواب: pH = 10)','د 1.0 × 10⁻⁴ M KOH محلول pH څومره دی؟ (ځواب: pH = 10)'),
('What is the pH of a solution if the [H₃O⁺] is 6.7×10⁻⁴M. (Ans. pH = 3.17)','اگر [H₃O⁺] 6.7×10⁻⁴M ہو تو محلول کا pH کیا ہے۔ (جواب: pH = 3.17)','که [H₃O⁺] 6.7×10⁻⁴M وي نو د محلول pH څومره دی. (ځواب: pH = 3.17)'),
('What is the pH of a solution for which [OH⁻] is 0.15M. (Ans. pH = 13.2)','اس محلول کا pH کیا ہے جس کے لیے [OH⁻] 0.15M ہے۔ (جواب: pH = 13.2)','د هغه محلول pH څومره دی چې [OH⁻] یې 0.15M وي. (ځواب: pH = 13.2)')]
for i,(e,u,p) in enumerate(NQ,1): Q(s,f'n{i}',f'{i}. {e}',f'{i}۔ {u}',f'{i}. {p}')
head(s,'dq','Descriptive Questions','تفصیلی سوالات','تشریحي پوښتنې')
Q(s,'d1a','1. (a) What is Bronsted–Lowery acids and bases? Explain it with suitable examples.','1۔ (الف) برونسٹڈ لوری تیزاب اور اساس کیا ہیں؟ مناسب مثالوں کے ساتھ وضاحت کریں۔','1. (الف) برونسټډ-لوري اسیدونه او القلي څه دي؟ په مناسبو بېلګو سره یې تشریح کړئ.')
Q(s,'d1b','(b) Write equations and indicate the conjugate acid – base pairs for the following; (i) Acetic acid and water, (ii) Ammonia and hydrochloric acid','(ب) درج ذیل کے لیے مساواتیں لکھیں اور مزدوج تیزاب اساس جوڑے ظاہر کریں؛ (i) ایسیٹک ایسڈ اور پانی، (ii) امونیا اور ہائیڈروکلورک ایسڈ','(ب) د لاندې لپاره معادلې ولیکئ او مزدوج اسید-القلي جوړې وښیئ؛ (i) اسیټیک اسید او اوبه، (ii) امونیا او هایدروکلوریک اسید')
Q(s,'d1c','(c) Justify that NH₃ is a base according to Lewis concept.','(ج) لیوس تصور کے مطابق ثابت کریں کہ NH₃ اساس ہے۔','(ج) د لیویس مفکورې له مخې ثابته کړئ چې NH₃ القلي دی.')
Q(s,'d2a','2. (a) Define buffer solution. What is buffer action and show with equations how a buffer system works?','2۔ (الف) بفر محلول کی تعریف کریں۔ بفر عمل کیا ہے اور مساواتوں کے ساتھ دکھائیں کہ بفر نظام کیسے کام کرتا ہے؟','2. (الف) بفر محلول تعریف کړئ. د بفر عمل څه دی او په معادلو سره وښیئ چې د بفر سیسټم څنګه کار کوي؟')
Q(s,'d2b','(b) What are the applications of buffers solutions?','(ب) بفر محلولوں کے اطلاقات کیا ہیں؟','(ب) د بفر محلولونو کارونې څه دي؟')
Q(s,'d2c','(c) Justify that buffer solution resists changes in pH, when a small amount of','(ج) ثابت کریں کہ بفر محلول pH کی تبدیلی کی مزاحمت کرتا ہے، جب تھوڑی مقدار','(ج) ثابته کړئ چې بفر محلول د pH د بدلون مقاومت کوي، کله چې لږ مقدار')
s['flow']=[dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 267. The left edge is clipped by the page curl (question numbers and the first letters of several lines are cut; the numbering shown for 13–15, the short, numerical and descriptive questions is read from order). The exponent of [OH⁻] in the answer to numerical question 2 is too small/blurred to read and is marked [scan obscured]. The last question (2c) is cut at the bottom of the page and continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Left-edge numbering partly cut; [OH⁻] answer exponent in numerical question 2 unreadable; question 2(c) continues on the next page.')
s['vocabulary']={}
save(s)
