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
    def done(s_): s_.s['flow']=s_.f
TC='chem11-thermochemistry'
def mk(n,title,ur,ps,sid): return page(n,TC,title,ur,ps,sid)
def tx(x,y,t,size=11,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'
def arrow(x1,y1,x2,y2,col='#111'):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{col}" stroke-width="2" fill="none"/><circle cx="{x2}" cy="{y2}" r="3.5" fill="{col}"/>'
def Q(s,key,en,ur,ps): add(s,key,en,ur,ps,role='question')

# ---------- 353 ----------
s=mk(353,'Figure 11.5 Two ways of changing A to B · Single and two step process · Heat of Formation','شکل 11.5 A سے B میں تبدیلی کے دو طریقے · یک مرحلہ اور دو مرحلہ عمل · تشکیل کی حرارت','شکل 11.5 له A څخه B ته د بدلون دوه لارې · یو مرحله او دوه مرحله پروسه · د جوړېدو تودوخه','fig115-hess')
F=Flow(s)
fg=(arrow(150,60,370,60)+arrow(150,60,110,120)+arrow(110,120,230,120)+arrow(230,120,370,60)
 +tx(70,45,'Initial',11,'end')+tx(70,60,'State',11,'end')+tx(140,60,'A',14,'end',700)+tx(385,60,'B',14,'start',700)+tx(420,45,'Final',11,'start')+tx(420,60,'State',11,'start')
 +tx(260,50,'+Q',12,'middle',700)+tx(100,95,'+q₁',12,'end',700)+tx(100,128,'C',14,'end',700)+tx(240,132,'D',14,'start',700)+tx(170,138,'+q₂',12,'middle',700)+tx(330,100,'+q₃',12,'start',700)
 +tx(240,175,'Fig. 11.5 Two ways of changing A to B.',12,'middle',700,'#a02040'))
s['figures']=[dict(id='chem11-p353-fig115',svg=svg(480,190,'Hess law diagram: direct path from A to B with heat +Q and indirect path A to C to D to B with heats q1, q2 and q3',fg),caption='Fig. 11.5 Two ways of changing A to B.',captionUrdu='شکل 11.5 A کو B میں تبدیل کرنے کے دو طریقے۔',captionPashto='شکل 11.5 A ته B ته د بدلون دوه لارې.',labels=[lab('Initial State','ابتدائی حالت','لومړنی حالت'),lab('Final State','آخری حالت','وروستی حالت'),lab('+Q','+Q','+Q')],sourceGap=dict(note='Diagram redrawn as a schematic; points A, B, C, D and the heats +Q, +q₁, +q₂, +q₃ follow the print.'))]
add(s,'a1',f'Following example of formation of Na₂CO₃ with the reaction of NaOH and CO₂ illustrates the Hess\'s law{SO}','Na₂CO₃ کی تشکیل کی درج ذیل مثال NaOH اور CO₂ کے تعامل سے ہیس کے قانون کی وضاحت کرتی ہے {SO}','د Na₂CO₃ د جوړېدو لاندې بېلګه د NaOH او CO₂ د تعامل سره د هېس قانون روښانه کوي {SO}'.replace('{SO}',SO))
add(s,'h1','Single step process','ایک مرحلہ عمل','یو مرحله پروسه',kind='heading')
add(s,'h2','Two step process','دو مرحلہ عمل','دوه مرحله پروسه',kind='heading')
add(s,'a2',"According to Hess's Law ΔH = ΔH₁ + ΔH₂",'ہیس کے قانون کے مطابق ΔH = ΔH₁ + ΔH₂','د هېس د قانون له مخې ΔH = ΔH₁ + ΔH₂')
add(s,'a3','Putting the values','قیمتیں رکھنے پر','ارزښتونه ایښودلو سره')
add(s,'a4',f"By applying the Hess's law the heat of all those reactions can be calculated, which cannot be measured directly. Some of its applications are as follows.{SO}",f'ہیس کے قانون کے اطلاق سے ان تمام تعاملات کی حرارت معلوم کی جا سکتی ہے جو براہِ راست ناپی نہیں جا سکتیں۔ اس کے کچھ اطلاقات درج ذیل ہیں {SO}۔',f'د هېس د قانون په تطبیق سره د ټولو هغو تعاملاتو تودوخه محاسبه کېدای شي چې مستقیماً نشي اندازه کېدای. د هغه ځینې کارونې په لاندې ډول دي {SO}.')
add(s,'h3','Heat of Formation','تشکیل کی حرارت','د جوړېدو تودوخه',kind='heading')
add(s,'a5',f'Carbon monoxide, for example, is prepared by reacting carbon with oxygen, but along with carbon monoxide, carbon dioxide is also formed. So to determine the heat of reaction for CO formation, an indirect method is used as follows.{SO}',f'مثال کے طور پر کاربن مونو آکسائیڈ کاربن کے آکسیجن کے ساتھ تعامل سے تیار کی جاتی ہے، لیکن کاربن مونو آکسائیڈ کے ساتھ کاربن ڈائی آکسائیڈ بھی بنتی ہے۔ اس لیے CO کی تشکیل کے لیے تعامل کی حرارت معلوم کرنے کے لیے ایک بالواسطہ طریقہ اس طرح استعمال کیا جاتا ہے {SO}۔',f'د بېلګې په توګه کاربن مونو اکسایډ د کاربن د اکسیجن سره د تعامل په واسطه جوړېږي، خو د کاربن مونو اکسایډ سره سره کاربن ډای اکسایډ هم جوړېږي. نو د CO د جوړېدو لپاره د تعامل د تودوخې د ټاکلو لپاره یوه غیر مستقیمه طریقه په لاندې ډول کارول کېږي {SO}.')
F.fg(0)
F.p('a1','h1')
F.e('s1',r'2\mathrm{NaOH_{(aq)}+CO_{2(g)}\longrightarrow Na_2CO_{3(aq)}+H_2O_{(l)}}\qquad\Delta H=-89.08\ \mathrm{kJ}','2NaOH(aq) + CO₂(g) → Na₂CO₃(aq) + H₂O(l)   ΔH = −89.08 kJ')
F.p('h2')
F.e('t1',r'\mathrm{NaOH_{(aq)}+CO_{2(g)}\longrightarrow NaHCO_{3(aq)}}\qquad\Delta H_1=-48.06\ \mathrm{kJ}','NaOH(aq) + CO₂(g) → NaHCO₃(aq)   ΔH₁ = −48.06 kJ')
F.e('t2',r'\mathrm{NaHCO_3+NaOH_{(aq)}\longrightarrow Na_2CO_{3(aq)}+H_2O_{(l)}}\qquad\Delta H_2=-41.02\ \mathrm{kJ}','NaHCO₃ + NaOH(aq) → Na₂CO₃(aq) + H₂O(l)   ΔH₂ = −41.02 kJ')
F.p('a2','a3')
F.e('v1',r'\Delta H=-48.06-41.02','ΔH = −48.06 − 41.02')
F.e('v2',r'\Delta H=-89.08\ \mathrm{kJ}','ΔH = −89.08 kJ')
F.p('a4','h3','a5')
F.done()
s['sourceNote']='Printed folio 348. The arrows "→" in the printed reactions appear as garbled characters on the scan and are read as →. The right edge is clipped on the prose lines (Na₂CO₃ example, applications and Heat of Formation); clipped endings are marked [scan obscured] and not inferred. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Arrow glyphs garbled on the scan; right-edge clipping on prose lines.')
s['vocabulary']={'heat of formation':{'ur':'تشکیل کی حرارت','ps':'د جوړېدو تودوخه'}}
save(s)

# ---------- 354 ----------
s=mk(354,'Heat of formation of CO · Lattice energy · 11.9 Born Haber Cycle','CO کی تشکیل کی حرارت · جالی توانائی · 11.9 بورن ہیبر چکر','د CO د جوړېدو تودوخه · د جالۍ انرژي · 11.9 بورن-هابر دوره','born-haber')
F=Flow(s)
add(s,'a1','Subtracting equation (ii) from (i) and similarly subtracting ΔH₂ from ΔH₁ We get','مساوات (ii) کو (i) سے منفی کرنے پر اور اسی طرح ΔH₂ کو ΔH₁ سے منفی کرنے پر ہمیں ملتا ہے','معادله (ii) له (i) څخه منفي کولو سره او همدارنګه ΔH₂ له ΔH₁ څخه منفي کولو سره موږ ترلاسه کوو')
add(s,'a2','The lattice energy can be calculated from the available thermodynamic data by a cyclic process known as Born-Haber Cycle, which is based on Hess\'s law.','جالی توانائی دستیاب تھرموڈائنامک ڈیٹا سے ایک چکری عمل کے ذریعے حساب کی جا سکتی ہے جسے بورن ہیبر چکر کہتے ہیں، جو ہیس کے قانون پر مبنی ہے۔','د جالۍ انرژي د شته ترموډینامیکي معلوماتو څخه د یوې دوراني پروسې په واسطه محاسبه کېدای شي چې بورن-هابر دوره بلل کېږي، چې د هېس په قانون ولاړه ده.')
add(s,'h','11.9 Born Haber Cycle','11.9 بورن ہیبر چکر','11.9 بورن-هابر دوره',kind='heading')
add(s,'b1','The Born-Haber Cycle is based on the principle that the sum of energy changes which occur in a closed cycle, from the same initial and final states, is zero. This principle involves the law of conservation of energy in accordance with the first law of thermodynamics.','بورن ہیبر چکر اس اصول پر مبنی ہے کہ ایک بند چکر میں، ایک ہی ابتدائی اور آخری حالتوں سے، ہونے والی توانائی کی تبدیلیوں کا مجموعہ صفر ہوتا ہے۔ اس اصول میں تھرموڈائنامکس کے پہلے قانون کے مطابق توانائی کی بقا کا قانون شامل ہے۔','د بورن-هابر دوره پدې اصل ولاړه ده چې په یوه تړلې دوره کې، له یو شان لومړني او وروستي حالتونو څخه، د پېښېدونکو انرژۍ بدلونونو مجموعه صفر ده. دا اصل د ترموډینامیکس د لومړي قانون سره سم د انرژۍ د ساتنې قانون شاملوي.')
add(s,'b2',f'The Born Haber cycle may be considered for NaCl as an example. The standard heat of formation ΔH°f of NaCl is the amount of heat given out when one mole of NaCl is formed from its elements, solid Na and gaseous chlorine. Lattice energy cannot be measured directly, but it can be determined indirectly. We measure ΔH°f for NaCl as follows:','بورن ہیبر چکر کو NaCl کی مثال کے طور پر لیا جا سکتا ہے۔ NaCl کی تشکیل کی معیاری حرارت ΔH°f وہ حرارت کی مقدار ہے جو اس وقت خارج ہوتی ہے جب NaCl کا ایک مول اس کے عناصر، ٹھوس Na اور گیسی کلورین، سے بنے۔ جالی توانائی براہِ راست نہیں ناپی جا سکتی لیکن اسے بالواسطہ متعین کیا جا سکتا ہے۔ ہم NaCl کے لیے ΔH°f اس طرح ناپتے ہیں:','د بورن-هابر دوره د NaCl د بېلګې په توګه ګڼل کېدای شي. د NaCl د جوړېدو معیاري تودوخه ΔH°f د تودوخې هغه مقدار دی چې کله د NaCl یو مول له خپلو عناصرو، جامد Na او ګازي کلورین څخه جوړ شي خوشې کېږي. د جالۍ انرژي مستقیماً نشي اندازه کېدای خو په غیر مستقیم ډول ټاکل کېدای شي. موږ د NaCl لپاره ΔH°f په لاندې ډول اندازه کوو:')
add(s,'d0','Direct','براہِ راست','مستقیم',kind='heading')
add(s,'d1','Stepwise','مرحلہ وار','ګام په ګام',kind='heading')
add(s,'d2','Similarly Cl is formed in the following two steps:','اسی طرح Cl درج ذیل دو مراحل میں بنتا ہے:','همدارنګه Cl په لاندې دوو مرحلو کې جوړېږي:')
F.e('c0',r'\mathrm{C_{(s)}+\tfrac{1}{2}O_{2(g)}\longrightarrow CO_{(g)}}\qquad\Delta H^{\circ}=?','C(s) + ½O₂(g) → CO(g)   ΔH° = ?')
F.e('c1',r'\text{i)}\ \mathrm{C_{(s)}+O_{2(g)}\longrightarrow CO_{2(g)}}\qquad\Delta H^{\circ}_1=-393.5\ \mathrm{kJ\,mol^{-1}}','i) C(s) + O₂(g) → CO₂(g)   ΔH°₁ = −393.5 kJ mol⁻¹')
F.e('c2',r'\text{ii)}\ \mathrm{CO_{(g)}+\tfrac{1}{2}O_{2(g)}\longrightarrow CO_{2(g)}}\qquad\Delta H^{\circ}_2=-285.7\ \mathrm{kJ\,mol^{-1}}','ii) CO(g) + ½O₂(g) → CO₂(g)   ΔH°₂ = −285.7 kJ mol⁻¹')
F.p('a1')
F.e('c3',r'\mathrm{C_{(s)}+\tfrac{1}{2}O_{2(g)}\longrightarrow CO_{(g)}}\qquad\Delta H^{\circ}=-108.88\ \mathrm{kJ\,mol^{-1}}','C(s) + ½O₂(g) → CO(g)   ΔH° = −108.88 kJ mol⁻¹')
F.p('a2','h','b1','b2','d0')
F.e('n0',r'\mathrm{Na_{(s)}+\tfrac{1}{2}Cl_{2(g)}\rightarrow NaCl_{(s)}}\qquad\Delta H^{\circ}_f=-411\ \mathrm{kJ\,mol}','Na(s) + ½Cl₂(g) → NaCl(s)   ΔH°f = −411 kJ mol')
F.p('d1')
F.e('n1',r'\text{i)}\ \mathrm{Na_{(s)}\rightarrow Na_{(g)}}\qquad\Delta H^{\circ}_{Sub}=109\ \mathrm{kJ\,mol^{-1}}','i) Na(s) → Na(g)   ΔH°Sub = 109 kJ mol⁻¹')
F.e('n2',r'\text{ii)}\ \mathrm{Na_{(g)}\rightarrow Na^+_{(g)}+e^-}\qquad\Delta H^{\circ}_{IE}=496\ \mathrm{kJ\,mol^{-1}}','ii) Na(g) → Na⁺(g) + e⁻   ΔH°IE = 496 kJ mol⁻¹')
F.p('d2')
F.e('n3',r'\text{iii)}\ \mathrm{Cl_{2(g)}\rightarrow2Cl_{(g)}}\qquad\Delta H^{\circ}_{Diss}=242\ \mathrm{kJ\,mol^{-1}}','iii) Cl₂(g) → 2Cl(g)   ΔH°Diss = 242 kJ mol⁻¹')
F.e('n4',r'\text{iv)}\ \mathrm{Cl_{(g)}+e^-\rightarrow Cl^-_{(g)}}\qquad\Delta H^{\circ}_{EA}=-348\ \mathrm{kJ\,mol^{-1}}','iv) Cl(g) + e⁻ → Cl⁻(g)   ΔH°EA = −348 kJ mol⁻¹')
F.e('n5',r'\text{v)}\ \mathrm{Na^+_{(g)}+Cl^-_{(g)}\rightarrow NaCl_{(s)}}\qquad\Delta H^{\circ}_{Lat}=U=?','v) Na⁺(g) + Cl⁻(g) → NaCl(s)   ΔH°Lat = U = ?')
F.done()
s['sourceNote']='Printed folio 349. The arrows in the printed reactions appear as garbled characters (¾¾®) on the scan and are read as →. Printed unit "kJ mol" (without −1) on the Direct line and "kJ/mol" forms are as printed. The text "Substracting" is a printed misspelling (retained in meaning, shown as "Subtracting"). The pink italic definitions are partly faint. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Arrow glyphs garbled on the scan; "Substracting" misspelling normalized in the paraphrase; units printed as "kJ mol" on the Direct line.')
s['vocabulary']={'lattice energy':{'ur':'جالی توانائی','ps':'د جالۍ انرژي'},'born haber cycle':{'ur':'بورن ہیبر چکر','ps':'بورن-هابر دوره'}}
save(s)

# ---------- 355 ----------
s=mk(355,'Born Haber Cycle summary diagram · Example 11.5 Lattice energy of KBr','بورن ہیبر چکر کا خلاصہ خاکہ · مثال 11.5 KBr کی جالی توانائی','د بورن-هابر دورې لنډیز انځور · بېلګه 11.5 د KBr د جالۍ انرژي','born-haber-diagram-ex115')
F=Flow(s)
def bh(top,l_dh,l_sub,l_ie,l_ea,l_lat,x1='ClBr'):
    return None
d1=('<path d="M30 40 H350" stroke="#222" stroke-width="2"/><path d="M345 35 L355 40 L345 45" fill="#222"/><path d="M30 40 V170 H270" stroke="#222" stroke-width="2" fill="none"/><path d="M80 40 V105 H200" stroke="#222" stroke-width="2" fill="none"/><path d="M200 105 H260" stroke="#222" stroke-width="2"/><path d="M330 175 V50" stroke="#222" stroke-width="2"/><path d="M325 55 L330 45 L335 55" fill="#222"/><path d="M270 170 H330 V120 H275" stroke="#222" stroke-width="2" fill="none"/>'
 +tx(20,35,'Na(s) + ½Cl₂(g)',11,'start')+tx(360,45,'NaCl(s)',11,'start')+tx(190,32,'ΔH°f',11)+tx(150,100,'½ΔH°Diss',10)+tx(210,118,'Cl(g)',10,'end')+tx(240,100,'ΔH°EA',10)+tx(290,115,'Cl⁻(g)',10,'start')+tx(130,160,'ΔH°Sub',10)+tx(200,165,'Na(g)',10,'end')+tx(235,155,'ΔH°IE',10)+tx(290,170,'Na⁺(g)',10,'start')+tx(335,110,'ΔH°Lat = ?',10,'start'))
d2=('<path d="M30 40 H350" stroke="#222" stroke-width="2"/><path d="M345 35 L355 40 L345 45" fill="#222"/><path d="M30 40 V170 H270" stroke="#222" stroke-width="2" fill="none"/><path d="M80 40 V105 H200" stroke="#222" stroke-width="2" fill="none"/><path d="M330 175 V50" stroke="#222" stroke-width="2"/><path d="M325 55 L330 45 L335 55" fill="#222"/><path d="M270 170 H330 V120 H275" stroke="#222" stroke-width="2" fill="none"/>'
 +tx(20,35,'K(s) + ½Br₂(g)',11,'start')+tx(360,45,'KBr(s)',11,'start')+tx(190,32,'ΔH°f = −405.8 kJ',11)+tx(130,100,'½ΔH°Diss = 192.5/2',10)+tx(220,118,'Br(g)',10,'end')+tx(245,100,'ΔH°EA = −334.7 kJ/mol',9)+tx(290,115,'Br⁻(g)',10,'start')+tx(140,160,'ΔH Sub = 88 kJ/mol',10)+tx(210,165,'K(g)',10,'end')+tx(245,155,'ΔH°IE = 414 kJ/mol',9)+tx(290,170,'K⁺(g)',10,'start')+tx(335,110,'ΔH°Lat = −669 kJ',10,'start'))
s['figures']=[dict(id='chem11-p355-nacl',svg=svg(420,205,'Born-Haber cycle for NaCl: formation, sublimation, ionization, dissociation, electron affinity and lattice energy steps',d1),caption='Born-Haber cycle for NaCl',captionUrdu='NaCl کے لیے بورن ہیبر چکر',captionPashto='د NaCl لپاره بورن-هابر دوره',labels=[lab('ΔH°f','ΔH°f','ΔH°f'),lab('ΔH°Lat = ?','ΔH°Lat = ؟','ΔH°Lat = ؟')],sourceGap=dict(note='Cycle diagram redrawn as a schematic from the print; right-hand label ΔH°Lat = ? is slightly clipped.')),
 dict(id='chem11-p355-kbr',svg=svg(420,205,'Born-Haber cycle for KBr with the values from Example 11.5',d2),caption='Born-Haber cycle for KBr (Example 11.5)',captionUrdu='KBr کے لیے بورن ہیبر چکر (مثال 11.5)',captionPashto='د KBr لپاره بورن-هابر دوره (بېلګه 11.5)',labels=[lab('ΔH°f = −405.8 kJ','ΔH°f = −405.8 kJ','ΔH°f = −405.8 kJ'),lab('ΔH°Lat = −669 kJ','ΔH°Lat = −669 kJ','ΔH°Lat = −669 kJ')],sourceGap=dict(note='Cycle diagram redrawn as a schematic from the print; the lower-right part of the figure is clipped by the page edge.'))]
add(s,'a1',f'The various energies involved in Born Haber Cycle for NaCl can be summarized as follows','NaCl کے لیے بورن ہیبر چکر میں شامل مختلف توانائیوں کو اس طرح خلاصہ کیا جا سکتا ہے','د NaCl لپاره په بورن-هابر دوره کې شاملې بېلابېلې انرژۍ په لاندې ډول لنډېدای شي')
add(s,'a2',f'According to Hess\'s law the sum of all the five steps lead to the heat of formation of NaCl(s).','ہیس کے قانون کے مطابق تمام پانچ مراحل کا مجموعہ NaCl(s) کی تشکیل کی حرارت تک پہنچاتا ہے۔','د هېس د قانون له مخې د ټولو پنځو ګامونو مجموعه د NaCl(s) د جوړېدو تودوخې ته رسوي.')
add(s,'e','Example 11.5','مثال 11.5','بېلګه 11.5',kind='heading')
add(s,'q','Calculate the lattice energy of KBr. The heat of sublimation of potassium is 88 kJ/mole, the heat of dissociation of bromine gas is 192.5 kJ/mole. The ionization energy of K is 414 is kJ/mole, the electron affinity of Br is −334.7 kJ/mole and the heat of formation of KBr is −405.8 kJ/mole.','KBr کی جالی توانائی معلوم کریں۔ پوٹاشیم کی تصعید کی حرارت 88 kJ/mole ہے، برومین گیس کی تفکیک کی حرارت 192.5 kJ/mole ہے۔ K کی آئنائزیشن توانائی 414 kJ/mole ہے، Br کی الیکٹران رغبت −334.7 kJ/mole ہے اور KBr کی تشکیل کی حرارت −405.8 kJ/mole ہے۔','د KBr د جالۍ انرژي محاسبه کړئ. د پوتاشیم د تصعید تودوخه 88 kJ/mole ده، د برومین ګاز د تجزیې تودوخه 192.5 kJ/mole ده. د K د آیونایزیشن انرژي 414 kJ/mole ده، د Br د الکترون تمایل −334.7 kJ/mole دی او د KBr د جوړېدو تودوخه −405.8 kJ/mole ده.')
F.p('a1')
F.fg(0)
F.p('a2')
F.e('s1',r'\Delta H^{\circ}_f=\Delta H^{\circ}_{Sub}+\Delta H^{\circ}_{IE}+\tfrac12\Delta H^{\circ}_{Diss}+\Delta H^{\circ}_{EA}+\Delta H^{\circ}_{Lat}','ΔH°f = ΔH°Sub + ΔH°IE + ½ΔH°Diss + ΔH°EA + ΔH°Lat')
F.e('s2',r'\Delta H^{\circ}_{Lat}=\Delta H^{\circ}_f-\Delta H^{\circ}_{Sub}-\Delta H^{\circ}_{IE}-\tfrac12\Delta H^{\circ}_{Diss}-\Delta H^{\circ}_{EA}','ΔH°Lat = ΔH°f − ΔH°Sub − ΔH°IE − ½ΔH°Diss − ΔH°EA')
F.e('s3',r'=-411\ \mathrm{kJ/mol}-109\ \mathrm{kJ/mol}-496\ \mathrm{kJ/mol}-121\ \mathrm{kJ/mol}-(-348\ \mathrm{kJ/mol})','= −411 kJ/mol − 109 kJ/mol − 496 kJ/mol − 121 kJ/mol − (−348 kJ/mol)')
F.e('s4',r'\Delta H^{\circ}_{Lat}\ \text{of NaCl}_{(s)}=-789\ \mathrm{kJ/mol}','ΔH°Lat of NaCl(s) = −789 kJ/mol')
F.p('e','q')
F.fg(1)
F.done()
s['sourceNote']='Printed folio 350. The right edge is clipped by the page curl on the first line, the "According to Hess\'s law" line, the Example 11.5 question and the right end of both cycle diagrams. The printed lattice-energy arithmetic for NaCl shows "−121 kJ/mol" for ½ΔH°Diss and "−411 − 109 − 496 − 121 − (−348)" as written; the stated result is −789 kJ/mol as printed (the arithmetic gives −789). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; both Born-Haber diagrams redrawn as schematics.')
s['vocabulary']={'lattice energy':{'ur':'جالی توانائی','ps':'د جالۍ انرژي'}}
save(s)

# ---------- 356 ----------
s=mk(356,'Example 11.5 solution · Self-Assessment','مثال 11.5 کا حل · خود جائزہ','د بېلګې 11.5 حل · ځان ارزونه','solution115')
F=Flow(s)
add(s,'sa','Self-Assessment','خود جائزہ','ځان ارزونه',kind='heading')
Q(s,'sa1','1. Define calorimetry and how to measure enthalpy change with the help of calorimeter.','1۔ کیلوری میٹری کی تعریف کریں اور کیلوری میٹر کی مدد سے انتھالپی تبدیلی کیسے ناپی جاتی ہے۔','1. کیلوري میټري تعریف کړئ او د کیلوري میټر په مرسته د انتالپي بدلون څنګه اندازه کېږي.')
Q(s,'sa2',"2. State the Hess's law.",'2۔ ہیس کا قانون بیان کریں۔','2. د هېس قانون بیان کړئ.')
Q(s,'sa3','3. On which principle Born Harber cycle is based?','3۔ بورن ہیبر چکر کس اصول پر مبنی ہے؟','3. بورن-هابر دوره په کوم اصل ولاړه ده؟')
F.e('e1',r'\Delta H^{\circ}_f=\Delta H^{\circ}_{Sub}+\Delta H^{\circ}_{IE}+\tfrac12\Delta H^{\circ}_{Diss}+\Delta H^{\circ}_{EA}+\Delta H^{\circ}_{Lat}','ΔH°f = ΔH°Sub + ΔH°IE + ½ΔH°Diss + ΔH°EA + ΔH°Lat')
F.e('e2',r'\Delta H^{\circ}_{Lat}=\Delta H^{\circ}_f-\Delta H^{\circ}_{Sub}-\Delta H^{\circ}_{IE}-\tfrac12\Delta H^{\circ}_{Diss}-\Delta H^{\circ}_{EA}','ΔH°Lat = ΔH°f − ΔH°Sub − ΔH°IE − ½ΔH°Diss − ΔH°EA')
F.e('e3',r'=-405.8-88-414-\tfrac12\,192.5-(-334.7)','= −405.8 − 88 − 414 − ½ 192.5 − (−334.7)')
F.e('e4',r'\Delta H^{\circ}_{Lat}=-669.3\ \mathrm{kJ/mol}','ΔH°Lat = −669.3 kJ/mol')
F.p('sa','sa1','sa2','sa3')
F.done()
s['sourceNote']='Printed folio 351 (the folio number is not visible). The scan is slightly skewed; "Harber" in the third Self-Assessment question is a printed misspelling (retained as "Harber" in the English line). The printed result is −669.3 kJ/mol. The lower two thirds of the page are blank. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='"Harber" is printed in the third question; page is mostly blank below.')
s['vocabulary']={}
save(s)
