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
    def tb(s_,i): s_.f.append(dict(type='table',index=i))
    def done(s_): s_.s['flow']=s_.f
CH='chem11-acids-bases-salts'
def mk(n,title,ur,ps,sid): return page(n,CH,title,ur,ps,sid)

# ---------- 257 ----------
s=mk(257,'8.4.4 Leveling Effect','8.4.4 برابری کا اثر (لیولنگ ایفیکٹ)','8.4.4 د برابرولو اغېز (لیولینګ ایفیکټ)','leveling-effect')
F=Flow(s)
head(s,'h','8.4.4 Leveling Effect','8.4.4 برابری کا اثر','8.4.4 د برابرولو اغېز')
add(s,'a1',f'Strong acids, such as HCl, HBr, and HI, all show nearly same strength{SO} water. The water molecule is such a strong base compared to the conjuga{SO} bases Cl⁻, Br⁻, and I⁻ that ionization of these strong acids is essentially complete{SO} aqueous solutions. The phenomenon by which the strength of different{SO} acids having close values of pK_a is levelled (equalized) by a definite solven{SO} called leveling effect. The acid strength depends upon the solvent chosen.',
 f'مضبوط تیزاب، جیسے HCl، HBr اور HI، سب تقریباً ایک جیسی قوت دکھاتے ہیں {SO} پانی میں۔ پانی کا سالمہ مزدوج {SO} اساسوں Cl⁻، Br⁻ اور I⁻ کے مقابلے میں اتنا مضبوط اساس ہے کہ ان مضبوط تیزابوں کی آئنائزیشن بنیادی طور پر مکمل ہوتی ہے {SO} آبی محلولوں میں۔ وہ مظہر جس کے ذریعے مختلف {SO} تیزابوں کی قوت، جن کی pK_a کی قیمتیں قریب ہوں، کسی مخصوص محلل کے ذریعے برابر کر دی جاتی ہے {SO} برابری کا اثر کہلاتا ہے۔ تیزاب کی قوت منتخب محلل پر منحصر ہوتی ہے۔',
 f'قوي اسیدونه، لکه HCl، HBr او HI، ټول نږدې یو شان قوت ښيي {SO} په اوبو کې. د اوبو مالیکول د مزدوج {SO} القليو Cl⁻، Br⁻ او I⁻ په پرتله دومره قوي القلي دی چې د دې قوي اسیدونو آیونایزیشن په اصل کې بشپړ دی {SO} په اوبیزو محلولونو کې. هغه پدیده چې په هغې کې د بېلابېلو {SO} اسیدونو قوت، چې د pK_a نژدې ارزښتونه لري، د یو ټاکلي محلل په واسطه برابرېږي {SO} د برابرولو اغېز بلل کېږي. د اسید قوت د ټاکل شوي محلل پورې اړه لري.')
add(s,'a2',f'They appear to have nearly equal strengths because their strengths ar{SO} due to that of hydronium ion (H₃O⁺). All the acids, which are complete{SO} dissociated in aqueous solution, are expressed by H₃O⁺ ion. It is not possible to{SO} find the order of increasing strengths of these acids because they are complete{SO} ionized.',
 f'یہ تقریباً برابر قوت رکھتے نظر آتے ہیں کیونکہ ان کی قوتیں {SO} ہائیڈرونیم آئن (H₃O⁺) کی وجہ سے ہیں۔ تمام تیزاب جو آبی محلول میں مکمل طور پر {SO} تفکیک ہوتے ہیں H₃O⁺ آئن کے ذریعے ظاہر کیے جاتے ہیں۔ ان تیزابوں کی بڑھتی قوت کی ترتیب معلوم کرنا ممکن نہیں {SO} کیونکہ وہ مکمل طور پر {SO} آئنائز ہوتے ہیں۔',
 f'دوی داسې ښکاري چې نږدې مساوي قوت لري ځکه چې د هغوی قوتونه {SO} د هایدرونیم آیون (H₃O⁺) له امله دي. ټول اسیدونه چې په اوبیز محلول کې په بشپړ ډول {SO} تجزیه کېږي د H₃O⁺ آیون په واسطه ښودل کېږي. د دې اسیدونو د زیاتېدونکي قوت ترتیب موندل ممکن نه دي {SO} ځکه چې دوی په بشپړ ډول {SO} آیونایز دي.')
add(s,'a3',f'In solvents less basic than water, you will be able to find that HCl, HBr and{SO} HI differs clearly in their tendency to give up a proton to the solvent. For{SO} example, when dissolved in ethanol (a weaker base than water), the extent of{SO} ionization increases in the order HCl < HBr < HI, and so HI is demonstrated to be{SO} the strongest of these acids.',
 f'پانی سے کم اساسی محللوں میں آپ یہ معلوم کر سکیں گے کہ HCl، HBr اور {SO} HI محلل کو پروٹان دینے کے رجحان میں واضح طور پر مختلف ہیں۔ مثال کے طور پر {SO} جب ایتھانول (پانی سے کمزور اساس) میں حل کیے جائیں تو آئنائزیشن کی حد {SO} HCl < HBr < HI کی ترتیب میں بڑھتی ہے، اور اس طرح HI ان تیزابوں میں {SO} سب سے مضبوط ثابت ہوتا ہے۔',
 f'په هغو محللونو کې چې له اوبو څخه لږ القلي دي، تاسو به وکولای شئ پوه شئ چې HCl، HBr او {SO} HI د محلل ته د پروټون ورکولو په تمایل کې په روښانه ډول توپیر لري. د بېلګې په توګه {SO} کله چې په ایتانول (د اوبو څخه ضعیف القلي) کې حل شي نو د آیونایزیشن اندازه {SO} د HCl < HBr < HI په ترتیب زیاتېږي، او دا ډول HI تر دې اسیدونو {SO} تر ټولو قوي ثابتېږي.')
add(s,'a4',f'The same effect is noticed in the case of solutions of bases. Water also{SO} exerts a leveling effect on the strengths of strong bases. For example, the oxide{SO} ion, O²⁻, and the amide ion, NH₂⁻ are such strong bases that they react{SO} completely with water. When Na₂O and NaNH₂ are dissolved in water, they give{SO} following reactions.',
 f'یہی اثر اساسوں کے محلولوں کی صورت میں بھی دیکھا جاتا ہے۔ پانی بھی {SO} مضبوط اساسوں کی قوتوں پر برابری کا اثر ڈالتا ہے۔ مثال کے طور پر آکسائیڈ {SO} آئن O²⁻ اور امائیڈ آئن NH₂⁻ اتنے مضبوط اساس ہیں کہ وہ پانی کے ساتھ {SO} مکمل طور پر تعامل کرتے ہیں۔ جب Na₂O اور NaNH₂ پانی میں حل کیے جاتے ہیں تو وہ درج {SO} ذیل تعاملات دیتے ہیں۔',
 f'همدا اغېز د القليو د محلولونو په حالت کې هم لیدل کېږي. اوبه هم {SO} د قوي القليو په قوتونو برابرولو اغېز لري. د بېلګې په توګه اکسایډ {SO} آیون O²⁻ او امایډ آیون NH₂⁻ دومره قوي القلي دي چې دوی له اوبو سره {SO} په بشپړ ډول تعامل کوي. کله چې Na₂O او NaNH₂ په اوبو کې حل شي نو دوی لاندې {SO} تعاملات ورکوي.')
add(s,'a5',f'The reaction goes to competition and thus, O²⁻ and NH₂⁻ appear to have{SO} the same basic strength in water; they both give a 100% yield of hydroxide ions{SO} The basic strength of O²⁻ and NH₂⁻ is leveled to the strength of OH⁻ ions and they{SO} behave as equally strong bases in aqueous solution.',
 f'تعامل تکمیل تک جاتا ہے اور اس لیے O²⁻ اور NH₂⁻ پانی میں ایک جیسی اساسی قوت {SO} رکھتے نظر آتے ہیں؛ دونوں ہائیڈرو آکسائیڈ آئنوں کی 100% پیداوار دیتے ہیں {SO}۔ O²⁻ اور NH₂⁻ کی اساسی قوت OH⁻ آئنوں کی قوت کے برابر ہو جاتی ہے اور وہ {SO} آبی محلول میں برابر مضبوط اساسوں کی طرح برتاؤ کرتے ہیں۔',
 f'تعامل بشپړېدو ته ځي او نو O²⁻ او NH₂⁻ په اوبو کې یو شان القلي قوت {SO} لرونکي ښکاري؛ دواړه د هایدروکسایډ آیونونو 100% حاصل ورکوي {SO}. د O²⁻ او NH₂⁻ القلي قوت د OH⁻ آیونونو قوت ته برابرېږي او دوی {SO} په اوبیز محلول کې د مساوي قوي القليو په څېر چلند کوي.')
add(s,'a6',f'The approximate values of pK_a of some of the acids are given in table 8.{SO}',f'کچھ تیزابوں کی pK_a کی تقریبی قیمتیں جدول 8.{SO} میں دی گئی ہیں۔',f'د ځینو اسیدونو د pK_a نږدې ارزښتونه په 8.{SO} جدول کې ورکړل شوي دي.')
F.p('h','a1','a2','a3','a4')
F.e('r1',r'\mathrm{O^{2-}_{(aq)}+H_2O_{(l)}\longrightarrow OH^-_{(aq)}+OH^-_{(aq)}}','O²⁻(aq) + H₂O(l) → OH⁻(aq) + OH⁻(aq)')
F.e('r2',r'\mathrm{NH^{-}_{2(aq)}+H_2O_{(l)}\longrightarrow NH_{3(aq)}+OH^-_{(aq)}}','NH₂⁻(aq) + H₂O(l) → NH₃(aq) + OH⁻(aq)')
F.p('a5','a6')
F.done()
s['sourceNote']='Printed folio 252. The right edge is clipped by the page curl on nearly every line; clipped endings are marked [scan obscured] and not inferred. A handwritten insertion ("or acetic acid") between lines on this copy is not part of the printed book. The pink italic definition of the leveling effect is partly cut at the right. The table number in the last line is cut. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping throughout; table number in the last line is cut.')
s['vocabulary']={'leveling effect':{'ur':'برابری کا اثر','ps':'د برابرولو اغېز'}}
save(s)

# ---------- 258 ----------
s=mk(258,'Table 8.6 pKa Values · 8.4.5 Base Ionization Constant Kb and pKb','جدول 8.6 pKa کی قیمتیں · 8.4.5 اساسی آئنائزیشن مستقلہ Kb اور pKb','جدول 8.6 د pKa ارزښتونه · 8.4.5 د القلي د آیونایزیشن ثابت Kb او pKb','table86-kb')
F=Flow(s)
rows=[('HClO₄','−10','(COOH)₂','1.3'),('HI','−10','H₂SO₃','1.8'),('HBr','−9','CH₃COOH','4.7'),('HCl','−7','H₂CO₃','6.4'),('H₂SO₄','−3','H₂S','7.0'),('HNO₃','−3','NH₄⁺','9.3'),('HClO₃','−3','HCN','9.4')]
s['tables']=[table('Table 8.6 pKa Values (Approximately) of Some Acids In Water','جدول 8.6 پانی میں کچھ تیزابوں کی pKa کی (تقریبی) قیمتیں','جدول 8.6 په اوبو کې د ځینو اسیدونو د pKa (نږدې) ارزښتونه',[c('Acids','تیزاب','اسیدونه'),c('pKa'),c('Acids','تیزاب','اسیدونه'),c('pKa')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in rows])]
s['tables'][0]['sourceGap']=dict(note='The printed table has two side-by-side blocks (Acids/pKa). Handwritten corrections and circles on this copy (e.g. "−2", "−3" beside H₂SO₄ and HNO₃) are not part of the printed book and are ignored.')
head(s,'h845','8.4.5 Base Ionization Constant, K_b and pK_b','8.4.5 اساسی آئنائزیشن مستقلہ K_b اور pK_b','8.4.5 د القلي د آیونایزیشن ثابت K_b او pK_b')
add(s,'a1','The ionization of weak bases is treated in the same way as the ionization of weak acids.','کمزور اساسوں کی آئنائزیشن کو اسی طرح لیا جاتا ہے جیسے کمزور تیزابوں کی آئنائزیشن۔','د ضعیفو القليو آیونایزیشن په همدې ډول ګڼل کېږي لکه د ضعیفو اسیدونو آیونایزیشن.')
add(s,'a2','Consider a weak Bronsted base, A⁻. Its ionization in water is represented','ایک کمزور برونسٹڈ اساس A⁻ پر غور کریں۔ پانی میں اس کی آئنائزیشن اس طرح ظاہر کی جاتی ہے','یو ضعیف برونسټډ القلي A⁻ ته پام وکړئ. په اوبو کې د هغه آیونایزیشن په لاندې ډول ښودل کېږي')
add(s,'a3','The equilibrium expression for this ionization is','اس آئنائزیشن کے لیے توازنی اظہار یہ ہے','د دې آیونایزیشن لپاره د تعادل بیان دا دی')
add(s,'a4','Where for base is, K_c.[H₂O] = K_b, so you can write the above equation as,','جہاں اساس کے لیے K_c.[H₂O] = K_b ہے، اس لیے آپ مندرجہ بالا مساوات کو اس طرح لکھ سکتے ہیں،','چېرته چې د القلي لپاره K_c.[H₂O] = K_b دی، نو تاسو کولای شئ پورتنۍ معادله داسې ولیکئ،')
add(s,'a5','Where K_b, the base ionization or dissociation constant. It is the equilibrium constant for the ionization of base. At a given temperature, the strength of the Bronsted base, A⁻ is measured quantitatively by the magnitude of K_b. The larger the value of K_b, the stronger will be the base, that is, the greater the concentration of OH⁻ ions at equilibrium due to its ionization. A negative logarithm of K_b is pK_b. Keep in mind, however, that only weak bases have K_b values associated with them.','جہاں K_b اساسی آئنائزیشن یا تفکیک مستقلہ ہے۔ یہ اساس کی آئنائزیشن کا توازنی مستقلہ ہے۔ ایک دیے گئے درجہ حرارت پر برونسٹڈ اساس A⁻ کی قوت K_b کی مقدار سے مقداری طور پر ناپی جاتی ہے۔ K_b کی قیمت جتنی بڑی ہوگی اساس اتنا ہی مضبوط ہوگا، یعنی اس کی آئنائزیشن کی وجہ سے توازن پر OH⁻ آئنوں کا ارتکاز اتنا ہی زیادہ ہوگا۔ K_b کا منفی لوگارتھم pK_b ہے۔ تاہم یاد رکھیں کہ صرف کمزور اساسوں کے ساتھ K_b کی قیمتیں وابستہ ہوتی ہیں۔','چېرته چې K_b د القلي د آیونایزیشن یا تجزیې ثابت دی. دا د القلي د آیونایزیشن د تعادل ثابت دی. په یوه ورکړل شوې تودوخه کې د برونسټډ القلي A⁻ قوت د K_b د اندازې په واسطه کمیتي ډول اندازه کېږي. د K_b ارزښت څومره لوی وي القلي به هماغومره قوي وي، یعنې د هغه د آیونایزیشن له امله په تعادل کې د OH⁻ آیونونو غلظت به هماغومره ډېر وي. د K_b منفي لوګاریتم pK_b دی. خو په یاد ولرئ چې یوازې ضعیف القلي د K_b ارزښتونه لري.')
F.tb(0)
F.p('h845','a1','a2')
F.e('ion',r'\mathrm{A^-_{(aq)}+H_2O_{(l)}\rightleftharpoons HA_{(aq)}+OH^-_{(aq)}}','A⁻(aq) + H₂O(l) ⇌ HA(aq) + OH⁻(aq)')
F.p('a3')
F.e('e812',r'K_c=\frac{[\mathrm{HA}][\mathrm{OH^-}]}{[\mathrm{H_2O}][\mathrm{A^-}]}\qquad(8.12)','K_c = [HA][OH⁻] / [H₂O][A⁻]   (8.12)')
F.e('e812b',r'K_c[\mathrm{H_2O}]=\frac{[\mathrm{HA}][\mathrm{OH^-}]}{[\mathrm{A^-}]}','K_c [H₂O] = [HA][OH⁻] / [A⁻]')
F.p('a4')
F.e('e813',r'K_b=\frac{[\mathrm{HA}][\mathrm{OH^-}]}{[\mathrm{A^-}]}\qquad(8.13)','K_b = [HA][OH⁻] / [A⁻]   (8.13)')
F.p('a5')
F.e('e814',r'\mathrm{p}K_b=-\log K_b\qquad(8.14)','pK_b = −log K_b   (8.14)')
F.done()
s['sourceNote']='Printed folio 253. The left edge is slightly clipped on the paragraph beginning "Where K_b…" (first letters of lines cut) but the sentences are legible. Equation number (8.14) is printed here for pK_b and again for K_a×K_b = K_w on the next page (a source numbering duplication, retained). Handwritten circles on this copy are ignored. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Equation number 8.14 is printed twice in the source (pKb here; Ka×Kb=Kw next page).')
s['vocabulary']={'bronsted base':{'ur':'برونسٹڈ اساس','ps':'برونسټډ القلي'}}
save(s)

# ---------- 259 ----------
s=mk(259,'Table 8.7 Ionization Constants of Some Weak Bases · 8.4.6 Relationship of Ka and Kb','جدول 8.7 کچھ کمزور اساسوں کے آئنائزیشن مستقلے · 8.4.6 Ka اور Kb کا باہمی تعلق','جدول 8.7 د ځینو ضعیفو القليو د آیونایزیشن ثابتونه · 8.4.6 د Ka او Kb اړیکه','table87-ka-kb')
F=Flow(s)
rows=[('Ammonia','امونیا','امونیا','NH₃','1.8 × 10⁻⁵'),('Aniline','اینیلین','انیلین','C₆H₅NH₂','4.2 × 10⁻¹⁰'),('Dimethylamine','ڈائی میتھائل امین','ډای میتایل امین','(CH₃)₂NH','5.1 × 10⁻⁴'),('Ethylamine','ایتھائل امین','ایتایل امین','C₂H₅NH₂','4.7 × 10⁻⁴'),('Hydrazine','ہائیڈرازین','هایدرازین','N₂H₄','1.7 × 10⁻⁶'),('Hydroxylamine','ہائیڈروکسل امین','هایدروکسیل امین','NH₂OH','1.1 × 10⁻⁸'),('Methylamine','میتھائل امین','میتایل امین','CH₃NH₂','4.4 × 10⁻⁴'),('Pyridine','پائرڈین','پیریډین','C₅H₅N','1.4 × 10⁻⁹'),('Urea','یوریا','یوریا','NH₂CONH₂','1.5 × 10⁻¹⁴')]
s['tables']=[table('Table 8.7 Ionization Constants of Some Weak Bases at 25°C','جدول 8.7 کچھ کمزور اساسوں کے آئنائزیشن مستقلے 25°C پر','جدول 8.7 د ځینو ضعیفو القليو د آیونایزیشن ثابتونه په 25°C کې',[c('Substance','مادہ','مواد'),c('Formula','فارمولا','فورمول'),c('Kb','Kb','Kb')],[[c(a,b,d),c(f),c(k)] for a,b,d,f,k in rows])]
s['tables'][0]['sourceGap']=dict(note='Handwritten digits beside the K_b column on this copy are not part of the printed book and are ignored.')
head(s,'h846','8.4.6 Relationship of K_a and K_b','8.4.6 K_a اور K_b کا باہمی تعلق','8.4.6 د K_a او K_b اړیکه')
add(s,'a1',f'According to Bronsted – Lowery concept when a weak acid or a weak base is dissolved in water, a conjugate acid-base pair is produced. An important relationship between the acid ionization constant, K_a and the ionization constant of its conjugate base, K_b, can be derived as follows, using the general equation of an acid as an example is,',f'برونسٹڈ لوری تصور کے مطابق جب کوئی کمزور تیزاب یا کمزور اساس پانی میں حل کیا جاتا ہے تو ایک مزدوج تیزاب اساس جوڑا پیدا ہوتا ہے۔ تیزابی آئنائزیشن مستقلہ K_a اور اس کے مزدوج اساس کے آئنائزیشن مستقلہ K_b کے درمیان ایک اہم تعلق درج ذیل طریقے سے اخذ کیا جا سکتا ہے، ایک تیزاب کی عمومی مساوات کو مثال کے طور پر لیتے ہوئے،',f'د برونسټډ-لوري د مفکورې له مخې کله چې یو ضعیف اسید یا ضعیف القلي په اوبو کې حل شي نو یوه مزدوج اسید-القلي جوړه جوړېږي. د اسید د آیونایزیشن ثابت K_a او د هغه د مزدوج القلي د آیونایزیشن ثابت K_b ترمنځ یوه مهمه اړیکه په لاندې ډول استنباط کېدای شي، د یو اسید عمومي معادله د بېلګې په توګه اخیستلو سره،')
add(s,'a2','You have an equation for K_a, given in equation (8.10) previously,','آپ کے پاس K_a کی ایک مساوات ہے جو پہلے مساوات (8.10) میں دی گئی ہے،','تاسو د K_a لپاره یوه معادله لرئ چې مخکې په معادله (8.10) کې ورکړل شوې،')
add(s,'a3','The general equation of base as an example is,','اساس کی عمومی مساوات بطور مثال یہ ہے،','د القلي عمومي معادله د بېلګې په توګه دا ده،')
add(s,'a4','You have an equation (8.13) for K_b,','آپ کے پاس K_b کے لیے مساوات (8.13) ہے،','تاسو د K_b لپاره معادله (8.13) لرئ،')
add(s,'a5','Multiplying the expression of K_a with that of K_b','K_a کے اظہار کو K_b کے اظہار سے ضرب دینے پر','د K_a بیان د K_b له بیان سره ضرب کولو سره')
add(s,'a6','On simplification you get,','سادہ کرنے پر آپ کو ملتا ہے،','ساده کولو سره تاسو ترلاسه کوئ،')
add(s,'a7','As you know that, [H⁺][OH⁻] = K_w','جیسا کہ آپ جانتے ہیں، [H⁺][OH⁻] = K_w','لکه څنګه چې تاسو پوهېږئ، [H⁺][OH⁻] = K_w')
add(s,'a8','You can write, the above equation (8.14), as','آپ مندرجہ بالا مساوات (8.14) کو اس طرح لکھ سکتے ہیں','تاسو کولای شئ پورتنۍ معادله (8.14) داسې ولیکئ')
F.tb(0)
F.p('h846','a1')
F.e('ha',r'\mathrm{HA_{(aq)}+H_2O_{(l)}\rightleftharpoons H_3O^+_{(aq)}+A^-_{(aq)}}','HA(aq) + H₂O(l) ⇌ H₃O⁺(aq) + A⁻(aq)')
F.p('a2')
F.e('e810',r'K_a=\frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]}\qquad(8.10)','K_a = [H₃O⁺][A⁻] / [HA]   (8.10)')
F.p('a3')
F.e('base',r'\mathrm{A^-_{(aq)}+H_2O_{(l)}\rightleftharpoons HA_{(aq)}+OH^-_{(aq)}}','A⁻(aq) + H₂O(l) ⇌ HA(aq) + OH⁻(aq)')
F.p('a4')
F.e('e813',r'K_b=\frac{[\mathrm{HA}][\mathrm{OH^-}]}{[\mathrm{A^-}]}\qquad(8.13)','K_b = [HA][OH⁻] / [A⁻]   (8.13)')
F.p('a5')
F.e('mult',r'K_a\times K_b=\frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]}\times\frac{[\mathrm{HA}][\mathrm{OH^-}]}{[\mathrm{A^-}]}','K_a × K_b = [H₃O⁺][A⁻] / [HA] × [HA][OH⁻] / [A⁻]')
F.p('a6')
F.e('s1',r'K_a\times K_b=[\mathrm{H_3O^+}]\times[\mathrm{OH^-}]=[\mathrm{H^+}][\mathrm{OH^-}]','K_a × K_b = [H₃O⁺] × [OH⁻] = [H⁺][OH⁻]')
F.e('s2',r'K_a\times K_b=[\mathrm{H^+}][\mathrm{OH^-}]','K_a × K_b = [H⁺][OH⁻]')
F.p('a7')
F.e('s3',r'K_a\times K_b=K_w\qquad(8.14)\qquad(K_w=1.0\times10^{-14})','K_a × K_b = K_w   (8.14)   (K_w = 1.0 × 10⁻¹⁴)')
F.p('a8')
F.e('s4',r'K_a=\frac{K_w}{K_b}','K_a = K_w / K_b')
F.done()
s['sourceNote']='Printed folio 254. The right edge is slightly clipped on a few lines (e.g. "…or a weak base", "…ionization constant", "…general equation of…"); the sentences are legible. Handwritten digits beside Table 8.7 on this copy are not part of the printed book. A CamScanner watermark crosses the page.'
s['vocabulary']={}
save(s)

# ---------- 260 ----------
s=mk(260,'Ka and Kb conclusion · pKa + pKb = 14 · Example 8.4 · 8.5 Lewis Definitions of Acids and Bases','Ka اور Kb کا نتیجہ · pKa + pKb = 14 · مثال 8.4 · 8.5 تیزابوں اور اساسوں کی لیوس تعریفیں','د Ka او Kb پایله · pKa + pKb = 14 · بېلګه 8.4 · 8.5 د اسیدونو او القليو د لیویس تعریفونه','pka-pkb-lewis')
F=Flow(s)
add(s,'a1','This enables you to draw an important conclusion: The stronger the acid (the larger K_a), the weaker its conjugate base (the smaller K_b), and vice versa. As K_w being constant, so, you can write as,','یہ آپ کو ایک اہم نتیجہ اخذ کرنے کے قابل بناتا ہے: تیزاب جتنا مضبوط (K_a جتنا بڑا) ہوگا، اس کا مزدوج اساس اتنا ہی کمزور (K_b اتنا ہی چھوٹا) ہوگا، اور اس کے برعکس۔ چونکہ K_w مستقل ہے اس لیے آپ لکھ سکتے ہیں،','دا تاسو ته وړتیا درکوي چې یوه مهمه پایله ترلاسه کړئ: اسید څومره قوي (K_a څومره لوی) وي، د هغه مزدوج القلي به هماغومره ضعیف (K_b هماغومره کوچنی) وي، او برعکس. ځکه چې K_w ثابت دی نو تاسو کولای شئ ولیکئ،')
add(s,'a2','Using the equation K_a × K_b = K_w','مساوات K_a × K_b = K_w استعمال کرتے ہوئے','د معادلې K_a × K_b = K_w په کارولو سره')
add(s,'a3','Taking negative logarithm (– log) of the equation (8.14),','مساوات (8.14) کا منفی لوگارتھم (– log) لینے پر،','د معادلې (8.14) منفي لوګاریتم (– log) اخیستلو سره،')
add(s,'a4','So you can write,','لہٰذا آپ لکھ سکتے ہیں،','نو تاسو لیکلای شئ،')
add(s,'a5','Knowing the pK_a value of an acid, you can find the pK_b of its conjugate base and vice versa.','کسی تیزاب کی pK_a کی قیمت جان کر آپ اس کے مزدوج اساس کی pK_b معلوم کر سکتے ہیں اور اس کے برعکس۔','د یو اسید د pK_a ارزښت په پوهېدو سره تاسو کولای شئ د هغه د مزدوج القلي pK_b ومومئ او برعکس.')
head(s,'e4','Example 8.4','مثال 8.4','بېلګه 8.4')
add(s,'q','Acetic acid (CH₃COOH) has a pK_a value of 4.7 at 25°C. What is the pK_b value of its cojuagte base, CH₃COO⁻?','25°C پر ایسیٹک ایسڈ (CH₃COOH) کی pK_a کی قیمت 4.7 ہے۔ اس کے مزدوج اساس CH₃COO⁻ کی pK_b کی قیمت کیا ہے؟','په 25°C کې د اسیټیک اسید (CH₃COOH) pK_a ارزښت 4.7 دی. د هغه د مزدوج القلي CH₃COO⁻ pK_b ارزښت څومره دی؟')
head(s,'sol','Solution','حل','حل')
add(s,'b1','The value of pK_a = 4.7','pK_a کی قیمت = 4.7','د pK_a ارزښت = 4.7')
add(s,'b2','Value of pK_b = ?','pK_b کی قیمت = ؟','د pK_b ارزښت = ؟')
add(s,'b3','As','چونکہ','لکه څنګه چې')
add(s,'b4','or','یا','یا')
add(s,'b5','or','یا','یا')
head(s,'h85','8.5 Lewis Definitions of Acids and Bases','8.5 تیزابوں اور اساسوں کی لیوس تعریفیں','8.5 د اسیدونو او القليو د لیویس تعریفونه')
add(s,'c1','A more general and broader concept of acids and bases was introduced by Gilbert N. Lewis. According to this concept, a Lewis acid is any specie (molecule or ion) that can form a covalent bond by accepting an electron pair from another species; a Lewis base is a specie that can form a covalent bond by donating an electron pair to any other specie.','تیزابوں اور اساسوں کا ایک زیادہ عمومی اور وسیع تصور گلبرٹ این لیوس نے پیش کیا۔ اس تصور کے مطابق لیوس تیزاب کوئی بھی نوع (سالمہ یا آئن) ہے جو کسی دوسری نوع سے الیکٹران جوڑا قبول کر کے ہم ذرّی بندھن بنا سکے؛ لیوس اساس وہ نوع ہے جو کسی دوسری نوع کو الیکٹران جوڑا عطا کر کے ہم ذرّی بندھن بنا سکے۔','د اسیدونو او القليو یوه ډېره عمومي او پراخه مفکوره ګیلبرټ ان لیویس وړاندې کړه. د دې مفکورې له مخې لیویس اسید هر هغه ډول (مالیکول یا آیون) دی چې له بل ډول څخه د الکترون جوړه منلو سره کوولنټ بند جوړ کړي؛ لیویس القلي هغه ډول دی چې د بل ډول ته د الکترون جوړې ورکولو سره کوولنټ بند جوړ کړي.')
head(s,'lh','The Lewis acid','لیوس تیزاب','لیویس اسید')
add(s,'c2','Those compounds which are electron deficient or which have less than eight electrons (octet) in valence shell behave as Lewis acids, e.g.','وہ مرکبات جو الیکٹران کی کمی رکھتے ہیں یا جن کے گرفتی خول میں آٹھ سے کم الیکٹران (اوکٹیٹ) ہوں لیوس تیزاب کی طرح برتاؤ کرتے ہیں، مثلاً','هغه مرکبات چې الکترون کمښت لري یا چې په والانس شیل کې له اتو څخه لږ الکترونونه (اوکټیټ) لري د لیویس اسید په څېر چلند کوي، لکه')
F.p('a1')
F.e('prop',r'K_a\propto\frac{1}{K_b}','K_a ∝ 1 / K_b')
F.p('a2')
F.e('e814',r'K_a\times K_b=K_w\qquad(8.14)','K_a × K_b = K_w   (8.14)')
F.p('a3')
F.e('logs',r'(-\log K_a)+(-\log K_b)=-\log K_w','(− log K_a) + (− log K_b) = − log K_w')
F.p('a4')
F.e('e815',r'\mathrm{p}K_a+\mathrm{p}K_b=14\qquad(8.15)','pK_a + pK_b = 14   (8.15)')
F.e('pkb',r'\mathrm{p}K_a=14-\mathrm{p}K_b','pK_a = 14 − pK_b')
F.p('a5','e4','q','sol','b1','b2','b3')
F.e('x1',r'\mathrm{p}K_a+\mathrm{p}K_b=14','pK_a + pK_b = 14')
F.p('b4')
F.e('x2',r'\mathrm{p}K_b=14-\mathrm{p}K_a','pK_b = 14 − pK_a')
F.p('b5')
F.e('x3',r'\mathrm{p}K_b=14-4.7','pK_b = 14 − 4.7')
F.e('x4',r'\mathrm{p}K_b=9.3','pK_b = 9.3')
F.p('h85','c1','lh','c2')
F.done()
s['sourceNote']='Printed folio 255. The left edge is clipped by the page curl (the first letters of lines such as "the larger K_a)", "K_w being constant", "(molecule or ion)", "from another species;", "donating an electron pair" and "electrons (octet)" are cut) but the sentences are legible. "cojuagte" in Example 8.4 is a printed misspelling. The Lewis acid example continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='First letters of several left-hand lines are cut; "cojuagte" is a printed misspelling; the "e.g." example continues on the next page.')
s['vocabulary']={'lewis acid':{'ur':'لیوس تیزاب','ps':'لیویس اسید'},'lewis base':{'ur':'لیوس اساس','ps':'لیویس القلي'},'octet':{'ur':'اوکٹیٹ','ps':'اوکټیټ'}}
save(s)
