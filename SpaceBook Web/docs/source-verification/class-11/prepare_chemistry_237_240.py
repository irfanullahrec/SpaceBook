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
def mk(n,ch,title,ur,ps,sid): return page(n,ch,title,ur,ps,sid)
EQ='chem11-equilibrium'
def R(F,key,left,right,tl,tr,arrow=r'\rightleftharpoons',t='⇌'):
    F.e(key,left+arrow+right,f'{tl} {t} {tr}')
def Q(s,key,en,ur,ps): add(s,key,en,ur,ps,role='question')
AB=r'\mathrm{A+B}'
# ---------- 237 ----------
s=mk(237,EQ,'Unit 7 Exercise (continued) · Short Questions · Numerical Questions','یونٹ 7 مشق (جاری) · مختصر سوالات · عددی سوالات','د 7 یونټ تمرین (دوام) · لنډې پوښتنې · عددي پوښتنې','exercise-short-numerical')
F=Flow(s)
mcq(s,10,'How much reaction is complete when K_c = 1 for the system A+B ⇌ C+D','جب نظام A+B ⇌ C+D کے لیے K_c = 1 ہو تو تعامل کتنا مکمل ہوتا ہے','کله چې د A+B ⇌ C+D سیسټم لپاره K_c = 1 وي نو تعامل څومره بشپړ وي',[('10%',None,None),('25%',None,None),('50%',None,None),('100%',None,None)],237)
mcq(s,11,'HCl when added to H₂S solution','HCl کو H₂S کے محلول میں ڈالنے پر','HCl کله چې د H₂S محلول ته اضافه شي',[('suppresses the ionization of H₂S','H₂S کی آئنائزیشن کو دباتا ہے','د H₂S آیونایزیشن ځپي'),('enhances the ionization','آئنائزیشن بڑھاتا ہے','آیونایزیشن زیاتوي'),('solution becomes coloured','محلول رنگین ہو جاتا ہے','محلول رنګین کېږي'),('does not affect','کوئی اثر نہیں ڈالتا','اغېز نه کوي')],237)
mcq(s,12,'The value of K_p is greater than K_c when the difference of the moles of the products and reactants is','K_p کی قیمت K_c سے زیادہ ہوتی ہے جب حاصلات اور تعامل کنندگان کے مولوں کا فرق ہو','د K_p ارزښت د K_c څخه ډېر وي کله چې د محصولاتو او متعاملینو د مولونو توپیر وي',[('zero','صفر','صفر'),('positive','مثبت','مثبت'),('negative','منفی','منفي'),('one','ایک','یو')],237)
head(s,'sh','Write answers for the given short questions.','دیے گئے مختصر سوالات کے جوابات لکھیں۔','د ورکړل شویو لنډو پوښتنو ځوابونه ولیکئ.')
Q(s,'s1','1. The change in temperature changes the equilibrium position of the reaction N₂(g) + O₂(g) ⇌ 2NO(g) but change in pressure does not, why?','1۔ درجہ حرارت کی تبدیلی تعامل N₂(g) + O₂(g) ⇌ 2NO(g) کے توازن کا مقام بدلتی ہے لیکن دباؤ کی تبدیلی نہیں بدلتی، کیوں؟','1. د تودوخې بدلون د N₂(g) + O₂(g) ⇌ 2NO(g) تعامل د تعادل موقعیت بدلوي خو د فشار بدلون نه بدلوي، ولې؟')
Q(s,'s2','2. Give the units of K_p for the following reversible reactions.','2۔ درج ذیل الٹنے والے تعاملات کے لیے K_p کی اکائیاں دیں۔','2. د لاندې بېرته کېدونکو تعاملاتو لپاره د K_p واحدونه ورکړئ.')
Q(s,'s3',f'3. Why does the value of K_c fall with the rise in temperature for the synthesis of SO₃?','3۔ SO₃ کی تالیف کے لیے درجہ حرارت بڑھنے سے K_c کی قیمت کیوں گھٹ جاتی ہے؟','3. د SO₃ د ترکیب لپاره د تودوخې په لوړېدو سره د K_c ارزښت ولې کمېږي؟')
Q(s,'s4',f'4. There is a dynamic rather than static equilibrium present between liquid{SO} and vapour at constant temperature; explain.',f'4۔ مستقل درجہ حرارت پر مائع {SO} اور بخارات کے درمیان ساکن کے بجائے حرکی توازن موجود ہوتا ہے؛ وضاحت کریں۔',f'4. په ثابته تودوخه کې د مایع {SO} او بخار ترمنځ د ساکن په ځای دیناميکي تعادل شتون لري؛ تشریح کړئ.')
Q(s,'s5',f'5. The change in concentration of reactants does not change the value of{SO} equilibrium constant permanently, elaborate.',f'5۔ تعامل کنندگان کے ارتکاز کی تبدیلی توازنی مستقلہ {SO} کی قیمت کو مستقل طور پر نہیں بدلتی، وضاحت کریں۔',f'5. د متعاملینو د غلظت بدلون د تعادل ثابت {SO} ارزښت په دایمي ډول نه بدلوي، تفصیل ورکړئ.')
Q(s,'s6','6. Discuss the equilibrium of a sparingly soluble salt.','6۔ کم حل پذیر نمک کے توازن پر بحث کریں۔','6. د یوې لږ حل کېدونکې مالګې د تعادل په اړه بحث وکړئ.')
Q(s,'s7',f'7. Common ion effect operates best in the purification of certain substances{SO}, explain.',f'7۔ مشترک آئن اثر بعض مادوں کی تطہیر میں بہترین کام کرتا ہے {SO}، وضاحت کریں۔',f'7. ګډ آیون اغېز د ځینو موادو په پاکولو کې غوره کار کوي {SO}، تشریح کړئ.')
Q(s,'s8','8. The ionization of calcium oxalate is suppressed by adding CaCl₂ to it, why?','8۔ کیلشیم آکسالیٹ کی آئنائزیشن CaCl₂ شامل کرنے سے دب جاتی ہے، کیوں؟','8. د کلسیم اوکزالیټ آیونایزیشن د CaCl₂ په اضافه کولو سره ځپل کېږي، ولې؟')
Q(s,'s9',f'9. The solubility of a sparingly soluble substance is calculated from the{SO} solubility product data, explain.',f'9۔ کم حل پذیر مادے کی حلالیت حلالیت حاصل ضرب کے اعداد و شمار سے معلوم کی جاتی ہے {SO}، وضاحت کریں۔',f'9. د یوې لږ حل کېدونکې مادې حلالیت د حلالیت حاصل ضرب له معلوماتو څخه محاسبه کېږي {SO}، تشریح کړئ.')
head(s,'nq','Numerical Questions','عددی سوالات','عددي پوښتنې')
Q(s,'n1',f'1. Calculate K_c for the synthesis of ammonia at 500°C. K_p = 1.44 × 10⁻⁵. (Ans: 5.8 × 10⁻{SO})',f'1۔ 500°C پر امونیا کی تالیف کے لیے K_c معلوم کریں۔ K_p = 1.44 × 10⁻⁵۔ (جواب: 5.8 × 10⁻{SO})',f'1. په 500°C کې د امونیا د ترکیب لپاره K_c محاسبه کړئ. K_p = 1.44 × 10⁻⁵. (ځواب: 5.8 × 10⁻{SO})')
F.p('ex','ch') if False else None
F.p('mcq-10','mcq-10a','mcq-10b','mcq-10c','mcq-10d')
F.p('mcq-11','mcq-11a','mcq-11b','mcq-11c','mcq-11d','mcq-12','mcq-12a','mcq-12b','mcq-12c','mcq-12d','sh','s1')
F.e('s1r',r'\mathrm{N_{2(g)}+O_{2(g)}\rightleftharpoons 2NO_{(g)}}','N₂(g) + O₂(g) ⇌ 2NO(g)')
F.p('s2')
F.e('s2a',r'\text{a)}\ \mathrm{PCl_{5(g)}\rightleftharpoons PCl_{3(g)}+Cl_{2(g)}}','a) PCl₅(g) ⇌ PCl₃(g) + Cl₂(g)')
F.e('s2b',r'\text{b)}\ \mathrm{N_{2(g)}+3H_{2(g)}\rightleftharpoons 2NH_{3(g)}}','b) N₂(g) + 3H₂(g) ⇌ 2NH₃(g)')
F.e('s2c',r'\text{c)}\ \mathrm{H_{2(g)}+CO_{2(g)}\rightleftharpoons CO_{(g)}+H_2O_{(g)}}','c) H₂(g) + CO₂(g) ⇌ CO(g) + H₂O(g)')
F.e('s2d',r'\text{d)}\ 4\mathrm{NH_{3(g)}}+5\mathrm{O_{2(g)}}\rightleftharpoons 4\mathrm{NO_{(g)}}+6\mathrm{H_2O_{(g)}}','d) 4NH₃(g) + 5O₂(g) ⇌ 4NO(g) + 6H₂O(g)')
F.p('s3')
F.e('s3r',r'2\mathrm{SO_{2(g)}+O_{2(g)}\rightleftharpoons 2SO_{3(g)}}\qquad\Delta H=-94.58\ \mathrm{kJ\,mol^{-1}}','2SO₂(g) + O₂(g) ⇌ 2SO₃(g)    ΔH = −94.58 kJ mol⁻¹')
F.p('s4','s5','s6','s7','s8','s9','nq','n1')
F.done()
s['sourceNote']='Printed folio 232. The right edge is clipped on several lines (questions 4, 5, 7, 9 and the answer to numerical question 1); clipped endings are marked [scan obscured] and not inferred. The printed answer to numerical question 1 ("Ans: 5.8 × 10⁻…") is cut after the exponent sign. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Answer exponent for numerical question 1 is cut off at the right edge.')
s['vocabulary']={'sparingly soluble':{'ur':'کم حل پذیر','ps':'لږ حل کېدونکی'},'common ion effect':{'ur':'مشترک آئن اثر','ps':'ګډ آیون اغېز'}}
save(s)

# ---------- 238 ----------
s=mk(238,EQ,'Unit 7 Exercise (continued) · Numerical Questions 2–6 · Descriptive Questions 1–5','یونٹ 7 مشق (جاری) · عددی سوالات 2–6 · تفصیلی سوالات 1–5','د 7 یونټ تمرین (دوام) · عددي پوښتنې 2–6 · تشریحي پوښتنې 1–5','exercise-numerical-descriptive')
F=Flow(s)
N=[('2. The solubility of CaF₂ in water at 25°C is found to be 2.05 × 10⁻⁴M. What is the K_sp at this temperature? (Ans: 3.446 × 10⁻¹¹)','2۔ 25°C پر پانی میں CaF₂ کی حلالیت 2.05 × 10⁻⁴M پائی گئی۔ اس درجہ حرارت پر K_sp کیا ہے؟ (جواب: 3.446 × 10⁻¹¹)','2. په 25°C کې په اوبو کې د CaF₂ حلالیت 2.05 × 10⁻⁴M وموندل شو. په دې تودوخه کې K_sp څومره دی؟ (ځواب: 3.446 × 10⁻¹¹)'),
('3. The solubility product of AgCl is 1.8 × 10⁻¹⁰. Calculate the molar solubility of the salt. (Ans: 1.34 × 10⁻⁵ M)','3۔ AgCl کا حلالیت حاصل ضرب 1.8 × 10⁻¹⁰ ہے۔ نمک کی مولر حلالیت معلوم کریں۔ (جواب: 1.34 × 10⁻⁵ M)','3. د AgCl د حلالیت حاصل ضرب 1.8 × 10⁻¹⁰ دی. د مالګې مولر حلالیت محاسبه کړئ. (ځواب: 1.34 × 10⁻⁵ M)'),
('4. A mixture of 0.5 moles of H₂ and I₂ each was placed in a one litre flask at 400°C. Calculate the concentration of H₂, I₂ and HI at equilibrium. The K_c for the reaction is 54.3. (Ans: [H₂] = [I₂] = 0.107M, [HI] = 0.786M)','4۔ 0.5 مول H₂ اور I₂ کا آمیزہ 400°C پر ایک لیٹر کے فلاسک میں رکھا گیا۔ توازن پر H₂، I₂ اور HI کا ارتکاز معلوم کریں۔ تعامل کا K_c 54.3 ہے۔ (جواب: [H₂] = [I₂] = 0.107M، [HI] = 0.786M)','4. د H₂ او I₂ هر یوه 0.5 مول مخلوط په 400°C کې په یو لیتر فلاسک کې کېښودل شو. په تعادل کې د H₂، I₂ او HI غلظت محاسبه کړئ. د تعامل K_c 54.3 دی. (ځواب: [H₂] = [I₂] = 0.107M، [HI] = 0.786M)'),
('5. The equilibrium mixture contains 1 mole of PCl₅, 0.3 mole of PCl₃ and 0.08 mole of Cl₂ in a 10 L flask. Calculate K_c. (Ans: K_c = 2.40 × 10⁻³)','5۔ توازنی آمیزے میں 10 L کے فلاسک میں 1 مول PCl₅، 0.3 مول PCl₃ اور 0.08 مول Cl₂ ہے۔ K_c معلوم کریں۔ (جواب: K_c = 2.40 × 10⁻³)','5. د تعادل مخلوط په 10 L فلاسک کې 1 مول PCl₅، 0.3 مول PCl₃ او 0.08 مول Cl₂ لري. K_c محاسبه کړئ. (ځواب: K_c = 2.40 × 10⁻³)'),
('6. The equilibrium concentration of N₂ and O₂ is 0.25M each while its K_c is 0.1 at 2000°C. Calculate the equilibrium concentration of NO according to the following reaction. (Ans: [NO] = 0.079M)','6۔ N₂ اور O₂ کا توازنی ارتکاز ہر ایک 0.25M ہے جبکہ 2000°C پر اس کا K_c 0.1 ہے۔ درج ذیل تعامل کے مطابق NO کا توازنی ارتکاز معلوم کریں۔ (جواب: [NO] = 0.079M)','6. د N₂ او O₂ د تعادل غلظت هر یو 0.25M دی پداسې حال کې چې په 2000°C کې یې K_c 0.1 دی. د لاندې تعامل له مخې د NO د تعادل غلظت محاسبه کړئ. (ځواب: [NO] = 0.079M)')]
for i,(e,u,p) in enumerate(N,2): Q(s,f'n{i}',e,u,p)
head(s,'dq','Descriptive Questions','تفصیلی سوالات','تشریحي پوښتنې')
Q(s,'d1','1. Write down K_c for the following reversible reactions.','1۔ درج ذیل الٹنے والے تعاملات کے لیے K_c لکھیں۔','1. د لاندې بېرته کېدونکو تعاملاتو لپاره K_c ولیکئ.')
Q(s,'d2','2. Predict the effect of increasing pressure on the following gaseous equilibria.','2۔ درج ذیل گیسی توازنوں پر دباؤ بڑھانے کے اثر کی پیش گوئی کریں۔','2. په لاندې ګازي تعادلونو باندې د فشار د زیاتوالي د اغېز وړاندوینه وکړئ.')
Q(s,'d3','3. Derive the relationship between K_p and K_c.','3۔ K_p اور K_c کے درمیان تعلق اخذ کریں۔','3. د K_p او K_c ترمنځ اړیکه استنباط کړئ.')
Q(s,'d4','4. What is the solubility product? Derive the solubility product expression for slightly soluble AgBr, CaCO₃, Al(OH)₃ and PbCrO₄.','4۔ حلالیت حاصل ضرب کیا ہے؟ قدرے حل پذیر AgBr، CaCO₃، Al(OH)₃ اور PbCrO₄ کے لیے حلالیت حاصل ضرب کا اظہار اخذ کریں۔','4. د حلالیت حاصل ضرب څه دی؟ د لږ حل کېدونکو AgBr، CaCO₃، Al(OH)₃ او PbCrO₄ لپاره د حلالیت حاصل ضرب بیان استنباط کړئ.')
Q(s,'d5','5. Explain the following.','5۔ درج ذیل کی وضاحت کریں۔','5. لاندې تشریح کړئ.')
Q(s,'d5a','(a) State the Law of Mass Action and derive the equilibrium constant expression for the given equation.','(الف) قانونِ کمیتِ عمل بیان کریں اور دی گئی مساوات کے لیے توازنی مستقلہ کا اظہار اخذ کریں۔','(الف) د کتلې د عمل قانون بیان کړئ او د ورکړل شوې معادلې لپاره د تعادل ثابت بیان استنباط کړئ.')
for i in range(2,7):
    pass
F.p('n2','n3','n4','n5','n6')
F.e('n6r',r'\mathrm{N_{2(g)}+O_{2(g)}\rightleftharpoons 2NO_{(g)}}','N₂(g) + O₂(g) ⇌ 2NO(g)')
F.p('dq','d1')
F.e('d1i',r'\text{i.}\ \mathrm{PCl_{5(g)}\rightleftharpoons PCl_{3(g)}+Cl_{2(g)}}','i. PCl₅(g) ⇌ PCl₃(g) + Cl₂(g)')
F.e('d1ii',r'\text{ii.}\ 2\mathrm{HI_{(g)}\rightleftharpoons H_{2(g)}+I_{2(g)}}','ii. 2HI(g) ⇌ H₂(g) + I₂(g)')
F.e('d1iii',r'\text{iii.}\ \mathrm{H_{2(g)}+CO_{2(g)}\rightleftharpoons CO_{(g)}+H_2O_{(g)}}','iii. H₂(g) + CO₂(g) ⇌ CO(g) + H₂O(g)')
F.e('d1iv',r'\text{iv.}\ 2\mathrm{N_2O_{5(g)}\rightleftharpoons 4NO_{2(g)}+O_{2(g)}}','iv. 2N₂O₅(g) ⇌ 4NO₂(g) + O₂(g)')
F.p('d2')
F.e('d2i',r'\text{i.}\ \mathrm{N_{2(g)}+O_{2(g)}\rightleftharpoons 2NO_{(g)}}','i. N₂(g) + O₂(g) ⇌ 2NO(g)')
F.e('d2ii',r'\text{ii.}\ \mathrm{PCl_{5(g)}\rightleftharpoons PCl_{3(g)}+Cl_{2(g)}}','ii. PCl₅(g) ⇌ PCl₃(g) + Cl₂(g)')
F.e('d2iii',r'\text{iii.}\ 2\mathrm{NO_{2(g)}\rightleftharpoons N_2O_{4(g)}}','iii. 2NO₂(g) ⇌ N₂O₄(g)')
F.e('d2iv',r'\text{iv.}\ 2\mathrm{SO_{2(g)}+O_{2(g)}\rightleftharpoons 2SO_{3(g)}}','iv. 2SO₂(g) + O₂(g) ⇌ 2SO₃(g)')
F.p('d3','d4','d5','d5a')
F.e('d5r',r'\mathrm{A+B\rightleftharpoons C+D}','A + B ⇌ C + D')
F.done()
s['sourceNote']='Printed folio 233. Question numbers on the left edge are slightly faint but legible. The answers printed in brackets after the numerical questions are transcribed as printed. Part 5(b) continues on the next page. A CamScanner watermark crosses the page.'
s['vocabulary']={'molar solubility':{'ur':'مولر حلالیت','ps':'مولر حلالیت'}}
save(s)

# ---------- 239 ----------
s=mk(239,EQ,'Unit 7 Exercise (continued) · Descriptive Questions 5–8 · Project','یونٹ 7 مشق (جاری) · تفصیلی سوالات 5–8 · منصوبہ','د 7 یونټ تمرین (دوام) · تشریحي پوښتنې 5–8 · پروژه','exercise-project')
F=Flow(s)
Q(s,'q1',f'(b) Given the equilibrium concentrations of N₂, O₂ and NO as 0.05M, 0.05M, and 5.5 × 10⁻⁴M respectively. Calculate K_c for the decomposition of NO at 1500°C for the reaction. (Ans: 8.26 × 10{SO})',f'(ب) N₂، O₂ اور NO کے توازنی ارتکاز بالترتیب 0.05M، 0.05M اور 5.5 × 10⁻⁴M دیے گئے ہیں۔ تعامل کے لیے 1500°C پر NO کی تحلیل کا K_c معلوم کریں۔ (جواب: 8.26 × 10{SO})',f'(ب) د N₂، O₂ او NO د تعادل غلظتونه په ترتیب سره 0.05M، 0.05M او 5.5 × 10⁻⁴M ورکړل شوي. د تعامل لپاره په 1500°C کې د NO د تجزیې K_c محاسبه کړئ. (ځواب: 8.26 × 10{SO})')
Q(s,'q2','ii. Find the value of equilibrium constant K_c for following reaction. The equilibrium concentrations are [SO₂] = 0.90M, [O₂] = 0.35M and [SO₃] = 1.1M. (Ans: 4.3)','ii. درج ذیل تعامل کے لیے توازنی مستقلہ K_c کی قیمت معلوم کریں۔ توازنی ارتکاز [SO₂] = 0.90M، [O₂] = 0.35M اور [SO₃] = 1.1M ہیں۔ (جواب: 4.3)','ii. د لاندې تعامل لپاره د تعادل ثابت K_c ارزښت ومومئ. د تعادل غلظتونه [SO₂] = 0.90M، [O₂] = 0.35M او [SO₃] = 1.1M دي. (ځواب: 4.3)')
Q(s,'q3',"ii. (a) State Le-Chatelier's principle and discuss its application to ammonia system.",'ii. (الف) لی شیٹیلیئر کا اصول بیان کریں اور امونیا کے نظام پر اس کے اطلاق پر بحث کریں۔','ii. (الف) د لی-شاټیلیر اصل بیان کړئ او د امونیا په سیسټم باندې د هغه د کارونې په اړه بحث وکړئ.')
Q(s,'q4','(b) What is the effect of raising temperature on each of the following equilibria.','(ب) درج ذیل توازنوں میں سے ہر ایک پر درجہ حرارت بڑھانے کا کیا اثر ہے۔','(ب) د لاندې تعادلونو له هر یوه باندې د تودوخې د لوړولو اغېز څه دی.')
Q(s,'q5',f'iv. (a) With the help of chemical equilibrium constant expression, how will you predict the direction and the extent of a chemical reaction?','iv. (الف) کیمیائی توازنی مستقلہ کے اظہار کی مدد سے آپ کیمیائی تعامل کی سمت اور حد کی پیش گوئی کیسے کریں گے؟','iv. (الف) د کيمياوي تعادل د ثابت د بیان په مرسته به تاسو د کيمياوي تعامل لوری او اندازه څنګه وړاندوینه کوئ؟')
Q(s,'q6',f'(b) The equilibrium constant for the reaction, 2O₃ ⇌ 3O₂ is 1.0 × 10{SO} at 25°C. Predict the extent of the formation of O₂ at room temperature.',f'(ب) تعامل 2O₃ ⇌ 3O₂ کا توازنی مستقلہ 25°C پر 1.0 × 10{SO} ہے۔ کمرے کے درجہ حرارت پر O₂ کی تشکیل کی حد کی پیش گوئی کریں۔',f'(ب) د 2O₃ ⇌ 3O₂ تعامل د تعادل ثابت په 25°C کې 1.0 × 10{SO} دی. د خونې په تودوخه کې د O₂ د جوړېدو اندازه وړاندوینه کړئ.')
head(s,'pj','Project','منصوبہ','پروژه')
add(s,'pj1','Take two test tubes, add about 10 cm³ solution of potassium chromate (K₂CrO₄) in both of them. Note the colour of the solution. Place one test tube in test tube stand for colour comparison purpose and add dil.HCl solution to the second test tube till the colour changes from yellow to orange. Now add a few cm³ solution of dil. NaOH. You will observe that the yellow colour appears again. Compare the colour with that of the first test tube solution.','دو ٹیسٹ ٹیوبیں لیں، دونوں میں تقریباً 10 cm³ پوٹاشیم کرومیٹ (K₂CrO₄) کا محلول ڈالیں۔ محلول کا رنگ نوٹ کریں۔ ایک ٹیسٹ ٹیوب کو رنگ کے موازنے کے لیے ٹیسٹ ٹیوب اسٹینڈ میں رکھیں اور دوسری ٹیسٹ ٹیوب میں ہلکا HCl کا محلول اس وقت تک ڈالیں جب تک رنگ پیلے سے نارنجی نہ ہو جائے۔ اب ہلکے NaOH کے چند cm³ محلول ڈالیں۔ آپ دیکھیں گے کہ پیلا رنگ دوبارہ ظاہر ہوتا ہے۔ رنگ کا موازنہ پہلی ٹیسٹ ٹیوب کے محلول کے رنگ سے کریں۔','دوه ټیسټ ټیوبونه واخلئ، په دواړو کې نږدې 10 cm³ د پوتاشیم کرومیټ (K₂CrO₄) محلول واچوئ. د محلول رنګ یادښت کړئ. یو ټیسټ ټیوب د رنګ د پرتلې لپاره د ټیسټ ټیوب په سټینډ کې کېږدئ او په دویم ټیسټ ټیوب کې رقیق HCl محلول تر هغه اضافه کړئ چې رنګ له ژیړ څخه نارنجي ته بدل شي. اوس د رقیق NaOH ځینې cm³ محلول اضافه کړئ. تاسو به وګورئ چې ژیړ رنګ بیا ښکاره کېږي. رنګ د لومړي ټیسټ ټیوب د محلول له رنګ سره پرتله کړئ.')
add(s,'pj2','The reaction that is taking place due to the addition of acid is the following','تیزاب کے اضافے سے جو تعامل ہو رہا ہے وہ درج ذیل ہے','هغه تعامل چې د اسید د اضافه کولو له امله پېښېږي دا دی')
add(s,'pj3','Questions:','سوالات:','پوښتنې:')
add(s,'pj4','i. Which principle is governing this reaction to bring it from left to right and back?','i. اس تعامل کو بائیں سے دائیں اور واپس لانے میں کون سا اصول کارفرما ہے؟','i. کوم اصل دا تعامل له چپ څخه ښي ته او بیرته راوړلو کې حاکم دی؟')
add(s,'pj5','ii. Why the reaction go back from right to left by the addition of base?','ii. القلی کے اضافے سے تعامل دائیں سے بائیں واپس کیوں جاتا ہے؟','ii. ولې تعامل د القلي په اضافه کولو سره له ښي څخه چپ ته بېرته ځي؟')
F.p('q1','q2')
F.e('q2r',r'2\mathrm{SO_{2(g)}+O_{2(g)}\rightleftharpoons 2SO_{3(g)}}','2SO₂(g) + O₂(g) ⇌ 2SO₃(g)')
F.p('q3','q4')
F.e('t1',r'\text{i.}\ \mathrm{N_{2(g)}+3H_{2(g)}\rightleftharpoons 2NH_{3(g)}}\qquad\Delta H=-\text{ve}','i. N₂(g) + 3H₂(g) ⇌ 2NH₃(g)    ΔH = −ve')
F.e('t2',r'\text{ii.}\ 2\mathrm{NO_{(g)}+O_{2(g)}\rightleftharpoons 2NO_{2(g)}}\qquad\Delta H=-\text{ve}','ii. 2NO(g) + O₂(g) ⇌ 2NO₂(g)    ΔH = −ve')
F.e('t3',r'\text{iii.}\ 2\mathrm{SO_{2(g)}+O_{2(g)}\rightleftharpoons 2SO_{3(g)}}\qquad\Delta H=-\text{ve}','iii. 2SO₂(g) + O₂(g) ⇌ 2SO₃(g)    ΔH = −ve')
F.e('t4',r'\text{iv.}\ \mathrm{N_{2(g)}+O_{2(g)}\rightleftharpoons 2NO_{(g)}}\qquad\Delta H=+\text{ve}','iv. N₂(g) + O₂(g) ⇌ 2NO(g)    ΔH = +ve')
F.p('q5','q6','pj','pj1','pj2')
F.e('cr',r'2\mathrm{CrO_4^{2-}}_{(aq)}+2\mathrm{H^+}_{(aq)}\rightleftharpoons\mathrm{Cr_2O_7^{2-}}_{(aq)}+\mathrm{H_2O}\quad(\text{Yellow}\rightarrow\text{Orange})','2CrO₄²⁻(aq) + 2H⁺(aq) ⇌ Cr₂O₇²⁻(aq) + H₂O   (Yellow ⇌ Orange)')
F.p('pj3','pj4','pj5')
F.done()
s['sourceNote']='Printed folio 234. The right edge is clipped on several lines; clipped endings are marked [scan obscured] and not inferred (the exponent of the Ans. in 5(b) and of K_c in 5(iv)(b)). Numbering is as printed: the question list shows "ii." twice (the second is read as the item after "ii. Find the value…") and the question numbers on the left are faint. The reaction for 5(b) is not printed on the page. The colour labels "Yellow" and "Orange" appear under the chromate and dichromate species in the Project equation. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Printed numbering repeats "ii." for consecutive items; exponents in two answers/values are cut off at the right edge.')
s['vocabulary']={'potassium chromate':{'ur':'پوٹاشیم کرومیٹ','ps':'پوتاشیم کرومیټ'}}
save(s)

# ---------- 240 ----------
s=mk(240,'chem11-acids-bases-salts','Unit 8 · Acids, Bases and Salts · Student learning outcomes','یونٹ 8 · تیزاب، اساس اور نمکیات · طلبہ کے تعلیمی نتائج','یونټ 8 · اسیدونه، القلي او مالګې · د زده کوونکو د زده کړې پایلې','unit8-outcomes')
add(s,'u','Unit-08','یونٹ-08','یونټ-08',kind='heading')
add(s,'t','Acids, Bases and Salts','تیزاب، اساس اور نمکیات','اسیدونه، القلي او مالګې',kind='heading')
add(s,'lead','After reading this unit, the students will be able to:','اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ:','د دې یونټ له لوستلو وروسته به زده کوونکي دې وړ شي چې:')
O=[('Define Bronsted and Lowery concepts for acids and bases. (Remembering)','تیزابوں اور اساسوں کے لیے برونسٹڈ اور لوری کے تصورات کی تعریف کریں۔ (یاد رکھنا)','د اسیدونو او القليو لپاره د برونسټډ او لوري مفکورې تعریف کړئ. (په یاد ساتل)'),
('Define salts, conjugate acids and conjugate bases. (Remembering)','نمکیات، مزدوج تیزاب اور مزدوج اساس کی تعریف کریں۔ (یاد رکھنا)','مالګې، مزدوج اسیدونه او مزدوج القلي تعریف کړئ. (په یاد ساتل)'),
('Identify conjugate acid-base pairs of Bronsted-Lowery acid and base. (Analyzing)','برونسٹڈ لوری تیزاب اور اساس کے مزدوج تیزاب اساس جوڑوں کی شناخت کریں۔ (تجزیہ)','د برونسټډ-لوري اسید او القلي مزدوج اسید-القلي جوړې وپېژنئ. (تحلیل)'),
('Explain ionization constant of water and calculate pH and pOH in aqueous medium using given K_w values. (Applying)','پانی کے آئنائزیشن مستقلہ کی وضاحت کریں اور دی گئی K_w قیمتیں استعمال کر کے آبی واسطے میں pH اور pOH معلوم کریں۔ (اطلاق)','د اوبو د آیونایزیشن ثابت تشریح کړئ او د ورکړل شویو K_w ارزښتونو په کارولو سره په اوبیز منځګړي کې pH او pOH محاسبه کړئ. (کارول)'),
('Use the extent of ionization and the acid dissociation constant, K_a, to distinguish between strong and weak acids. (Applying)','آئنائزیشن کی حد اور تیزابی تفکیک مستقلہ K_a استعمال کر کے مضبوط اور کمزور تیزابوں میں فرق کریں۔ (اطلاق)','د آیونایزیشن اندازه او د اسیدي تجزیې ثابت K_a وکاروئ ترڅو قوي او ضعیف اسیدونه توپیر کړئ. (کارول)'),
('Use the extent of ionization and the base dissociation constant, K_b, to distinguish between strong and weak bases. (Applying)','آئنائزیشن کی حد اور اساسی تفکیک مستقلہ K_b استعمال کر کے مضبوط اور کمزور اساسوں میں فرق کریں۔ (اطلاق)','د آیونایزیشن اندازه او د القلي د تجزیې ثابت K_b وکاروئ ترڅو قوي او ضعیف القلي توپیر کړئ. (کارول)'),
('Define a buffer and show with equations how a buffer system works. (Applying)','بفر کی تعریف کریں اور مساواتوں کے ساتھ دکھائیں کہ بفر نظام کیسے کام کرتا ہے۔ (اطلاق)','بفر تعریف کړئ او په معادلو سره وښیئ چې د بفر سیسټم څنګه کار کوي. (کارول)'),
('Make a buffered solution and explain how such a solution maintains a constant pH, even with the addition of small amounts of strong acid or strong base. (Understanding)','بفر محلول بنائیں اور وضاحت کریں کہ ایسا محلول مضبوط تیزاب یا مضبوط اساس کی تھوڑی مقدار شامل کرنے پر بھی مستقل pH کیسے برقرار رکھتا ہے۔ (سمجھنا)','بفر شوی محلول جوړ کړئ او تشریح کړئ چې داسې محلول د قوي اسید یا قوي القلي د لږو مقدارونو په اضافه کولو سره هم ثابت pH څنګه ساتي. (پوهېدل)'),
('Use the concept of hydrolysis to explain why aqueous solutions of some salts are acidic or basic. (Applying)','آبپاشیدگی (ہائیڈرولائسس) کا تصور استعمال کر کے وضاحت کریں کہ کچھ نمکیات کے آبی محلول تیزابی یا اساسی کیوں ہوتے ہیں۔ (اطلاق)','د هایدرولیز مفکوره وکاروئ ترڅو تشریح کړئ چې د ځینو مالګو اوبیز محلولونه ولې اسیدي یا القلي دي. (کارول)'),
('Use concept of hydrolysis to explain why the solution of a salt is not necessarily neutral. (Understanding)','ہائیڈرولائسس کا تصور استعمال کر کے وضاحت کریں کہ نمک کا محلول ضروری نہیں کہ معتدل ہو۔ (سمجھنا)','د هایدرولیز مفکوره وکاروئ ترڅو تشریح کړئ چې د مالګې محلول ولې اړینه نه ده چې خنثی وي. (پوهېدل)'),
('Define and explain leveling effect. (Understanding)','برابری کے اثر (لیولنگ ایفیکٹ) کی تعریف کریں اور وضاحت کریں۔ (سمجھنا)','د برابرولو اغېز (لیولینګ ایفیکټ) تعریف او تشریح کړئ. (پوهېدل)')]
for i,(e,u,p) in enumerate(O,1): add(s,f'o{i}',e,u,p)
head(s,'tw','Teaching Periods · Assessment · Weightage %','تدریسی پیریڈز · تشخیص · وزن %','د تدریس دورې · ارزونه · وزن %')
add(s,'tp','Teaching periods: 08','تدریسی پیریڈز: 08','د تدریس دورې: 08')
add(s,'as','Assessment: 01','تشخیص: 01','ارزونه: 01')
add(s,'wt','Weightage %: 06','وزن %: 06','وزن %: 06')
fig1=('<path d="M60 60 h20 l30 100 h-80 z" fill="#d03040" stroke="#822"/><path d="M60 60 h20 v-20 h-20 z" fill="#fff" stroke="#822"/>'
 '<path d="M170 60 h20 l30 100 h-80 z" fill="#4a6ad8" stroke="#238"/><path d="M170 60 h20 v-20 h-20 z" fill="#fff" stroke="#238"/>'
 '<rect x="270" y="50" width="70" height="110" rx="10" fill="#f4f4f4" stroke="#777"/><rect x="278" y="40" width="54" height="14" fill="#555"/><ellipse cx="305" cy="105" rx="30" ry="16" fill="#f0d878" stroke="#a80"/>'
 +T(305,110,'Salts',12,'middle',700)+T(75,150,'ACID',13,'middle',700,'#fff')+T(190,150,'BASE',13,'middle',700,'#fff'))
s['figures']=[fig(240,'cover',svg(400,190,'Cartoon of an acid flask, a base flask and a jar of salts',fig1),'Unit 8 cover: ACID, BASE and Salts','یونٹ 8 کا سرورق: تیزاب، اساس اور نمکیات','د 8 یونټ پوښ: اسید، القلي او مالګې',[lab('ACID','تیزاب','اسید'),lab('BASE','اساس','القلي'),lab('Salts','نمکیات','مالګې')])]
s['figures'][0]['sourceGap']=dict(note='Cover cartoon (two flasks and a salt jar) redrawn as a simple schematic; the original illustration is not reproduced.')
s['flow']=[dict(type='paragraphs',ids=ids(s,0,3)),dict(type='paragraphs',ids=ids(s,3,14)),dict(type='paragraphs',ids=ids(s,14)),dict(type='figure',index=0)]
s['sourceNote']='Printed folio 235. Unit opener. Text is legible. The side panel gives Teaching 08, Assessment 01, Weightage % 06 as printed. The cover illustration (ACID flask, BASE flask, jar labelled Salts) is redrawn as a schematic. A CamScanner watermark crosses the page.'
s['vocabulary']={'conjugate acid':{'ur':'مزدوج تیزاب','ps':'مزدوج اسید'},'conjugate base':{'ur':'مزدوج اساس','ps':'مزدوج القلي'},'buffer':{'ur':'بفر','ps':'بفر'},'hydrolysis':{'ur':'ہائیڈرولائسس','ps':'هایدرولیز'},'leveling effect':{'ur':'برابری کا اثر','ps':'د برابرولو اغېز'}}
save(s)
