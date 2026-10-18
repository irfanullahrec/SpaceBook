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
def mk(n,title,ur,ps,sid): return page(n,'chem11-equilibrium',title,ur,ps,sid)

# ---------- 233 ----------
s=mk(233,'7.5 Common Ion effect · Example 7.7 Dissociation of Weak Acid · Example 7.8 Dissociation of Weak Base','7.5 مشترک آئن اثر · مثال 7.7 کمزور تیزاب کی تفکیک · مثال 7.8 کمزور اساس کی تفکیک','7.5 ګډ آیون اغېز · بېلګه 7.7 د ضعیف اسید تجزیه · بېلګه 7.8 د ضعیف القلي تجزیه','common-ion-effect')
F=Flow(s)
head(s,'h75','7.5 Common Ion effect','7.5 مشترک آئن اثر','7.5 ګډ آیون اغېز')
add(s,'a1',f'It is a phenomenon in which the extent of dissociation (or solubility){SO} any weak electrolyte is suppressed by the presence of small amount of a stro{SO} electrolyte having a common ion with the weak electrolyte. In other words, {SO} shift of equilibrium towards left side, caused by the addition of an electro{SO} having an ion in common with the dissolved electrolyte is called common i{SO} effect.',f'یہ ایک مظہر ہے جس میں کسی کمزور برق پاش کی تفکیک (یا حلالیت) کی حد {SO} کسی مضبوط برق پاش کی تھوڑی مقدار کی موجودگی سے دب جاتی ہے جس کا کمزور برق پاش کے ساتھ ایک مشترک آئن ہو۔ دوسرے لفظوں میں، {SO} توازن کا بائیں طرف منتقل ہونا، جو کسی ایسے برق پاش کے اضافے سے ہو {SO} جس کا حل شدہ برق پاش کے ساتھ ایک مشترک آئن ہو، مشترک آئن اثر کہلاتا ہے {SO} اثر۔',f'دا یو پدیده ده چې په هغه کې د یو ضعیف الکترولایټ د تجزیې (یا حلالیت) اندازه {SO} د یو قوي الکترولایټ د لږ مقدار په شتون سره ځپل کېږي چې د ضعیف الکترولایټ سره یو ګډ آیون ولري. په بل عبارت، {SO} د تعادل چپ لوري ته بدلون، چې د یو الکترولایټ په اضافه کولو سره رامنځته شي {SO} چې د منحل شوي الکترولایټ سره یو ګډ آیون ولري، د ګډ آیون اغېز بلل کېږي {SO} اغېز.')
add(s,'a2','Consider the following examples for explanation of common ion effect.','مشترک آئن اثر کی وضاحت کے لیے درج ذیل مثالوں پر غور کریں۔','د ګډ آیون د اغېز د تشریح لپاره لاندې بېلګو ته پام وکړئ.')
head(s,'e7','Example 7.7 Dissociation of Weak Acid','مثال 7.7 کمزور تیزاب کی تفکیک','بېلګه 7.7 د ضعیف اسید تجزیه')
add(s,'b1',f'Ionization of weak electrolyte, acetic acid (CH₃COOH), is suppressed b{SO} adding strong electrolyte such as sodium acetate (CH₃COONa), containin{SO} common ion that is acetate ion (CH₃COO⁻). Acetic acid in water dissociates an{SO} an equilibrium exists as follows.',f'کمزور برق پاش، ایسیٹک ایسڈ (CH₃COOH) کی آئنائزیشن مضبوط برق پاش جیسے سوڈیم ایسیٹیٹ (CH₃COONa) شامل کرنے سے دب جاتی ہے {SO} جس میں مشترک آئن یعنی ایسیٹیٹ آئن (CH₃COO⁻) ہوتا ہے {SO}۔ پانی میں ایسیٹک ایسڈ تفکیک ہوتا ہے اور {SO} ایک توازن اس طرح قائم ہوتا ہے۔',f'د ضعیف الکترولایټ، اسیټیک اسید (CH₃COOH) آیونایزیشن د قوي الکترولایټ لکه سوډیم اسیټیټ (CH₃COONa) په اضافه کولو سره ځپل کېږي {SO} چې ګډ آیون یعنې اسیټیټ آیون (CH₃COO⁻) لري {SO}. په اوبو کې اسیټیک اسید تجزیه کېږي او {SO} یو تعادل په لاندې ډول رامنځته کېږي.')
add(s,'b2','The acid dissociation constant, K_a, for this dissociation is written as;','اس تفکیک کے لیے تیزابی تفکیک مستقلہ K_a اس طرح لکھا جاتا ہے؛','د دې تجزیې لپاره د اسیدي تجزیې ثابت K_a داسې لیکل کېږي؛')
add(s,'b3',f'When a small amount of strong electrolyte, like sodium acetat{SO} (CH₃COONa), is added to the aqueous solution of CH₃COOH, it gets dissociate{SO} as follows.',f'جب مضبوط برق پاش، جیسے سوڈیم ایسیٹیٹ {SO} (CH₃COONa) کی تھوڑی مقدار CH₃COOH کے آبی محلول میں ڈالی جاتی ہے تو وہ تفکیک ہو جاتا ہے {SO} اس طرح۔',f'کله چې د قوي الکترولایټ، لکه سوډیم اسیټیټ {SO} (CH₃COONa) لږ مقدار د CH₃COOH اوبیز محلول ته اضافه شي نو دا تجزیه کېږي {SO} په لاندې ډول.')
add(s,'b4',f"Here acetate ions (CH₃COO⁻) are common in CH₃COOH and CH₃COON{SO}. According to Le-Chatelier's principle equilibrium, (i), shifts towards left to kee{SO} the value of K_a constant, thus the concentration of CH₃COOH molecules i{SO} increased. In this way ionization of CH₃COOH is suppressed by addin{SO} CH₃COONa.",f'یہاں ایسیٹیٹ آئن (CH₃COO⁻) CH₃COOH اور CH₃COON {SO} میں مشترک ہیں۔ لی شیٹیلیئر کے اصول کے مطابق توازن (i) بائیں طرف منتقل ہوتا ہے تاکہ {SO} K_a کی قیمت مستقل رہے، اس طرح CH₃COOH کے سالموں کا ارتکاز {SO} بڑھ جاتا ہے۔ اس طرح CH₃COOH کی آئنائزیشن {SO} CH₃COONa شامل کرنے سے دب جاتی ہے۔',f'دلته اسیټیټ آیونونه (CH₃COO⁻) په CH₃COOH او CH₃COON {SO} کې ګډ دي. د لی-شاټیلیر د اصل له مخې تعادل (i) چپ لوري ته ځي ترڅو {SO} د K_a ارزښت ثابت وساتي، په دې توګه د CH₃COOH د مالیکولونو غلظت {SO} زیاتېږي. په دې توګه د CH₃COOH آیونایزیشن د {SO} CH₃COONa په اضافه کولو سره ځپل کېږي.')
head(s,'e8','Example 7.8 Dissociation of Weak Base','مثال 7.8 کمزور اساس کی تفکیک','بېلګه 7.8 د ضعیف القلي تجزیه')
add(s,'c1',f'Ionization of weak electrolyte such as ammonium hydroxide (NH₄OH) i{SO} suppressed by adding strong electrolyte, i.e. ammonium chloride (NH₄Cl{SO} containing common ammonium ions (NH₄⁺). NH₄OH dissociates in water a{SO} follows,',f'کمزور برق پاش جیسے امونیم ہائیڈرو آکسائیڈ (NH₄OH) کی آئنائزیشن {SO} مضبوط برق پاش یعنی امونیم کلورائیڈ (NH₄Cl) شامل کرنے سے دب جاتی ہے {SO} جس میں مشترک امونیم آئن (NH₄⁺) ہوتے ہیں۔ NH₄OH پانی میں اس طرح تفکیک ہوتا ہے {SO} جیسا کہ درج ذیل ہے،',f'د ضعیف الکترولایټ لکه امونیم هایدروکسایډ (NH₄OH) آیونایزیشن {SO} د قوي الکترولایټ یعنې امونیم کلوراید (NH₄Cl) په اضافه کولو سره ځپل کېږي {SO} چې ګډ امونیم آیونونه (NH₄⁺) لري. NH₄OH په اوبو کې {SO} په لاندې ډول تجزیه کېږي،')
F.p('h75','a1','a2','e7','b1')
F.e('i',r'\mathrm{CH_3COOH_{(aq)}\rightleftharpoons CH_3COO^-_{(aq)}+H^+_{(aq)}}\qquad\text{(i)}','CH₃COOH(aq) ⇌ CH₃COO⁻(aq) + H⁺(aq)    (i)')
F.p('b2')
F.e('ka',r'K_a=\frac{[\mathrm{CH_3COO^-}][\mathrm{H^+}]}{[\mathrm{CH_3COOH}]}','K_a = [CH₃COO⁻][H⁺] / [CH₃COOH]')
F.p('b3')
F.e('na',r'\mathrm{CH_3COONa_{(s)}\xrightarrow{H_2O}CH_3COO^-_{(aq)}+Na^+_{(aq)}}','CH₃COONa(s) → (H₂O) CH₃COO⁻(aq) + Na⁺(aq)')
F.p('b4','e8','c1')
F.e('nh4oh',r'\mathrm{NH_4OH_{(aq)}\rightleftharpoons NH^+_{4(aq)}+OH^-_{(aq)}}','NH₄OH(aq) ⇌ NH₄⁺(aq) + OH⁻(aq)')
F.done()
s['sourceNote']='Printed folio 228. The right edge is clipped by the page curl on nearly every prose line; clipped endings are marked [scan obscured] and not inferred. The pink italic definition of the common ion effect is partly cut at the right. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping on nearly every prose line.')
s['vocabulary']={'common ion effect':{'ur':'مشترک آئن اثر','ps':'ګډ آیون اغېز'},'weak electrolyte':{'ur':'کمزور برق پاش','ps':'ضعیف الکترولایټ'},'ionization':{'ur':'آئنائزیشن','ps':'آیونایزیشن'}}
save(s)

# ---------- 234 ----------
s=mk(234,'Base dissociation constant Kb · Example 7.9 · Reading Check','اساسی تفکیک مستقلہ Kb · مثال 7.9 · مطالعہ کی جانچ','د القلي تجزیې ثابت Kb · بېلګه 7.9 · د لوستلو ازموینه','kb-example-79')
F=Flow(s)
add(s,'a1','The equilibrium constant i.e. base dissociation constant, K_b, is written as','توازنی مستقلہ یعنی اساسی تفکیک مستقلہ K_b اس طرح لکھا جاتا ہے','د تعادل ثابت یعنې د القلي د تجزیې ثابت K_b داسې لیکل کېږي')
add(s,'a2','If a small amount of strong electrolyte like ammonium chloride (NH₄Cl) is added to the aqueous solution of NH₄OH, it gets dissociated as follows','اگر مضبوط برق پاش جیسے امونیم کلورائیڈ (NH₄Cl) کی تھوڑی مقدار NH₄OH کے آبی محلول میں ڈالی جائے تو وہ اس طرح تفکیک ہو جاتا ہے','که د قوي الکترولایټ لکه امونیم کلوراید (NH₄Cl) لږ مقدار د NH₄OH اوبیز محلول ته اضافه شي نو دا په لاندې ډول تجزیه کېږي')
add(s,'a3',"Here ammonium ions are common in NH₄OH and NH₄Cl and addition of NH₄Cl increases the concentration of NH₄⁺ ions. Thus according to Le-Chatelier's principle, equilibrium of NH₄OH shifts towards left to keep the value of K_b constant, the concentration of NH₄OH molecules is increased. In this way ionization of NH₄OH is suppressed by adding NH₄Cl.",'یہاں امونیم آئن NH₄OH اور NH₄Cl میں مشترک ہیں اور NH₄Cl کے اضافے سے NH₄⁺ آئنوں کا ارتکاز بڑھ جاتا ہے۔ لہٰذا لی شیٹیلیئر کے اصول کے مطابق NH₄OH کا توازن بائیں طرف منتقل ہوتا ہے تاکہ K_b کی قیمت مستقل رہے، NH₄OH کے سالموں کا ارتکاز بڑھ جاتا ہے۔ اس طرح NH₄OH کی آئنائزیشن NH₄Cl شامل کرنے سے دب جاتی ہے۔','دلته امونیم آیونونه په NH₄OH او NH₄Cl کې ګډ دي او د NH₄Cl اضافه کول د NH₄⁺ آیونونو غلظت زیاتوي. نو د لی-شاټیلیر د اصل له مخې د NH₄OH تعادل چپ لوري ته ځي ترڅو د K_b ارزښت ثابت وساتي، د NH₄OH د مالیکولونو غلظت زیاتېږي. په دې توګه د NH₄OH آیونایزیشن د NH₄Cl په اضافه کولو سره ځپل کېږي.')
head(s,'e9','Example 7.9','مثال 7.9','بېلګه 7.9')
add(s,'b1','Purification of NaCl is carried out by passing HCl gas through a saturated solution of NaCl.','NaCl کی تطہیر سیر شدہ NaCl محلول میں HCl گیس گزار کر کی جاتی ہے۔','د NaCl پاکول د NaCl د ګټ شوي محلول له لارې د HCl ګاز په تېرولو سره ترسره کېږي.')
add(s,'b2','Cl⁻¹ is a common ion due to which equilibrium shifts to the backward direction whereby NaCl precipitates.','Cl⁻¹ ایک مشترک آئن ہے جس کی وجہ سے توازن الٹی سمت میں منتقل ہوتا ہے اور NaCl ترسیب ہو جاتا ہے۔','Cl⁻¹ یو ګډ آیون دی چې له امله یې تعادل شاتګ لوري ته ځي او NaCl رسوب کېږي.')
add(s,'rc-h','Reading Check','مطالعہ کی جانچ','د لوستلو ازموینه',kind='heading')
add(s,'rc1','Define common ion effect.','مشترک آئن اثر کی تعریف کریں۔','د ګډ آیون اغېز تعریف کړئ.',role='question')
add(s,'rc2','Explain the solubility product of a substance with an example.','کسی مادے کے حلالیت حاصل ضرب کی ایک مثال کے ساتھ وضاحت کریں۔','د یوې مادې د حلالیت حاصل ضرب په یوې بېلګې سره تشریح کړئ.',role='question')
F.p('a1')
F.e('kb',r'K_b=\frac{[\mathrm{NH_4^+}][\mathrm{OH^-}]}{[\mathrm{NH_4OH}]}','K_b = [NH₄⁺][OH⁻] / [NH₄OH]')
F.p('a2')
F.e('nh4cl',r'\mathrm{NH_4Cl_{(s)}\xrightarrow{H_2O}NH^+_{4(aq)}+Cl^-_{(aq)}}','NH₄Cl(s) → (H₂O) NH₄⁺(aq) + Cl⁻(aq)')
F.p('a3','e9','b1')
F.e('nacl',r'\mathrm{NaCl_{(s)}\rightleftharpoons Na^+_{(aq)}+Cl^-_{(aq)}}','NaCl(s) ⇌ Na⁺(aq) + Cl⁻(aq)')
F.e('hcl',r'\mathrm{HCl_{(g)}\xrightarrow{H_2O}H^+_{(aq)}+Cl^-_{(aq)}}','HCl(g) → (H₂O) H⁺(aq) + Cl⁻(aq)')
F.p('b2','rc-h','rc1','rc2')
F.done()
s['sourceNote']='Printed folio 229. The text is legible; the right margin is slightly shadowed. The lower third of the page is blank apart from the Reading Check box, whose heading is partly faint. A CamScanner watermark crosses the page.'
s['vocabulary']={'base dissociation constant':{'ur':'اساسی تفکیک مستقلہ','ps':'د القلي د تجزیې ثابت'}}
save(s)

# ---------- 235 ----------
s=mk(235,'Key Points','اہم نکات','مهم ټکي','key-points')
head(s,'kp','KEY POINTS','اہم نکات','مهم ټکي')
KP=[(f'In a chemical reaction when the rate of forward reaction becomes equal to th{SO} rate of backward reaction, the reaction is in the state of dynamic equilibrium.',f'کسی کیمیائی تعامل میں جب سیدھے تعامل کی شرح {SO} الٹے تعامل کی شرح کے برابر ہو جاتی ہے تو تعامل حرکی توازن کی حالت میں ہوتا ہے۔',f'په یو کيمياوي تعامل کې کله چې د مخکښ تعامل چټکتیا {SO} د شاتګ تعامل له چټکتیا سره مساوي شي نو تعامل د دیناميکي تعادل په حالت کې وي.'),
(f'According to the Law of Mass Action, the rate at which a substance reacts is{SO} directly proportional to its active mass and the rate of reaction is directly{SO} proportional to the product of active masses of the reacting substances.',f'قانونِ کمیتِ عمل کے مطابق، کسی مادے کے تعامل کرنے کی شرح {SO} اس کی فعال کمیت کے براہِ راست متناسب ہوتی ہے اور تعامل کی شرح تعامل کرنے والے مادوں کی فعال کمیتوں کے حاصل ضرب کے براہِ راست {SO} متناسب ہوتی ہے۔',f'د کتلې د عمل د قانون له مخې، د یوې مادې د تعامل چټکتیا {SO} د هغې د فعالې کتلې سره مستقیماً متناسبه ده او د تعامل چټکتیا د تعامل کوونکو موادو د فعالو کتلو د حاصل ضرب سره مستقیماً {SO} متناسبه ده.'),
(f'Equilibrium constant of the reaction, K_c, is defined as the ratio of the product of{SO} the molar concentrations of the products to that of the reactants.',f'تعامل کا توازنی مستقلہ K_c اس طرح بیان کیا جاتا ہے کہ حاصلات کے مولر ارتکازوں کے حاصل ضرب کی {SO} تعامل کنندگان کے مولر ارتکازوں سے نسبت۔',f'د تعامل د تعادل ثابت K_c داسې تعریفېږي چې د محصولاتو د مولر غلظتونو د حاصل ضرب نسبت {SO} د متعاملینو د مولر غلظتونو سره.'),
(f'A large value of equilibrium constant, K_c, indicates that the reaction is almos{SO} complete. If the value of K_c is very small, then the reaction proceeds a little in the{SO} forward direction rather the reverse reaction is favoured.',f'توازنی مستقلہ K_c کی بڑی قیمت ظاہر کرتی ہے کہ تعامل تقریباً {SO} مکمل ہے۔ اگر K_c کی قیمت بہت چھوٹی ہو تو تعامل سیدھی سمت میں تھوڑا آگے بڑھتا ہے {SO} بلکہ الٹے تعامل کو ترجیح ملتی ہے۔',f'د تعادل د ثابت K_c لوی ارزښت ښيي چې تعامل نږدې {SO} بشپړ دی. که د K_c ارزښت ډېر کوچنی وي نو تعامل په مخکښ لوري کې لږ مخکې ځي {SO} بلکې بېرته تعامل غوره کېږي.'),
(f'Le-Chatelier\'s Principle states that "if a stress is applied to a system at{SO} equilibrium, the equilibrium will shift in the forward or backward direction to{SO} reduce the effect of stress".',f'لی شیٹیلیئر کا اصول کہتا ہے کہ "اگر توازن میں موجود نظام پر تناؤ ڈالا جائے {SO} تو توازن تناؤ کا اثر کم کرنے کے لیے سیدھی یا الٹی سمت میں منتقل ہو جائے گا {SO}"۔',f'د لی-شاټیلیر اصل وايي چې "که په تعادل کې په یو سیسټم فشار (تنش) وکارول شي {SO} نو تعادل به د فشار د اغېز د کمولو لپاره مخکښ یا شاتګ لوري ته لاړ شي {SO}".'),
(f'The catalyst has no effect on the equilibrium composition of a reaction{SO} However, it increases the rate of the reaction by lowering its energy of activation{SO}',f'اتپریرک کا تعامل کی توازنی ترکیب پر کوئی اثر نہیں ہوتا {SO}۔ تاہم یہ تعامل کی توانائی دہلیز کو کم کر کے تعامل کی شرح بڑھاتا ہے {SO}',f'کتلیست د تعامل د تعادل جوړښت باندې هېڅ اغېز نه لري {SO}. خو دا د تعامل د فعالولو انرژي په کمولو سره د تعامل چټکتیا زیاتوي {SO}'),
(f'If a soluble salt (say A⁺C⁻) is added to another less soluble salt (A⁺B⁻) containing{SO} common ion A⁺, the dissociation of A⁺B⁻ is suppressed. It is called common ion{SO} effect.',f'اگر کوئی حل پذیر نمک (مثلاً A⁺C⁻) کسی دوسرے کم حل پذیر نمک (A⁺B⁻) میں ڈالا جائے جس میں {SO} مشترک آئن A⁺ ہو تو A⁺B⁻ کی تفکیک دب جاتی ہے۔ اسے مشترک آئن {SO} اثر کہتے ہیں۔',f'که یو حل کېدونکې مالګه (لکه A⁺C⁻) بلې لږ حل کېدونکې مالګې (A⁺B⁻) ته اضافه شي چې {SO} ګډ آیون A⁺ لري نو د A⁺B⁻ تجزیه ځپل کېږي. دې ته ګډ آیون {SO} اغېز ویل کېږي.')]
for i,(e,u,p) in enumerate(KP,1): add(s,f'k{i}',e,u,p)
s['flow']=[dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 230 (page number not visible on the scan). The right edge is clipped by the page curl; clipped endings are marked [scan obscured] and not inferred. The key points list has seven bullets as printed. The lower part of the page is blank. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; page number not visible.')
s['vocabulary']={'dynamic equilibrium':{'ur':'حرکی توازن','ps':'دیناميکي تعادل'},'energy of activation':{'ur':'توانائی دہلیز','ps':'د فعالولو انرژي'}}
save(s)

# ---------- 236 ----------
s=mk(236,'Unit 7 Exercise · Choose the correct answer (1–9)','یونٹ 7 مشق · درست جواب منتخب کریں (1–9)','د 7 یونټ تمرین · سم ځواب وټاکئ (1–9)','exercise-mcq-1')
head(s,'ex','EXERCISE','مشق','تمرین')
head(s,'ch','Choose the correct answer.','درست جواب منتخب کریں۔','سم ځواب وټاکئ.')
Q=[('In which of the following values of K_c, the reaction goes to completion in the forward direction:','K_c کی درج ذیل قیمتوں میں سے کس پر تعامل سیدھی سمت میں تکمیل تک پہنچتا ہے:','د K_c له لاندې ارزښتونو څخه په کوم کې تعامل په مخکښ لوري کې بشپړېدو ته رسېږي:',[('10²',None,None),('10³⁰',None,None),('10⁻³⁰',None,None),('1',None,None)]),
('An appreciable amount of the product and reactants is present in a reaction if its equilibrium constant value is:','کسی تعامل میں حاصلات اور تعامل کنندگان کی قابلِ ذکر مقدار اس وقت موجود ہوتی ہے جب اس کے توازنی مستقلہ کی قیمت ہو:','په یو تعامل کې د محصول او متعاملینو د پام وړ مقدار هغه مهال شتون لري چې د تعادل د ثابت ارزښت وي:',[('Negative and large','منفی اور بڑی','منفي او لوی'),('Negative and small','منفی اور چھوٹی','منفي او کوچنی'),('Zero','صفر','صفر'),('Neither large nor small','نہ بڑی نہ چھوٹی','نه لوی نه کوچنی')]),
('Consider N₂(g) + 3H₂(g) ⇌ 2NH₃(g)   ΔH = 92.46 kJ/mol. The optimum temperature for the production of ammonia is:','N₂(g) + 3H₂(g) ⇌ 2NH₃(g)   ΔH = 92.46 kJ/mol پر غور کریں۔ امونیا کی پیداوار کے لیے موزوں ترین درجہ حرارت ہے:','N₂(g) + 3H₂(g) ⇌ 2NH₃(g)   ΔH = 92.46 kJ/mol ته پام وکړئ. د امونیا د تولید لپاره غوره تودوخه ده:',[('5000 °C',None,None),('450 °C',None,None),('0 °C',None,None),('Constant temperature','مستقل درجہ حرارت','ثابته تودوخه')]),
('In the production of SO₃ from SO₂ and oxygen. The yield of SO₃ is increased by','SO₂ اور آکسیجن سے SO₃ کی پیداوار میں SO₃ کی مقدار بڑھتی ہے','د SO₂ او اکسیجن څخه د SO₃ په تولید کې د SO₃ حاصل زیاتېږي',[('increasing temperature','درجہ حرارت بڑھانے سے','د تودوخې په لوړولو سره'),('adding a catalyst','اتپریرک شامل کرنے سے','د کتلیست په اضافه کولو سره'),('adding more SO₂','مزید SO₂ شامل کرنے سے','د نور SO₂ په اضافه کولو سره'),('removing O₂','O₂ ہٹانے سے','د O₂ په لرې کولو سره')]),
("Le-Chatelier's principle applies to",'لی شیٹیلیئر کا اصول لاگو ہوتا ہے','د لی-شاټیلیر اصل تطبیقېږي په',[('mechanical system','میکانی نظام','میخانیکي سیسټم'),('physical system','طبعی نظام','فزیکي سیسټم'),('chemical system','کیمیائی نظام','کيمياوي سیسټم'),('both b and c','b اور c دونوں','b او c دواړه')]),
('The unit of K_c for the system PCl₅ ⇌ PCl₃ + Cl₂ is','نظام PCl₅ ⇌ PCl₃ + Cl₂ کے لیے K_c کی اکائی ہے','د PCl₅ ⇌ PCl₃ + Cl₂ سیسټم لپاره د K_c واحد دی',[('mol²/dm⁶',None,None),('dm³/mol',None,None),('mol/dm⁶',None,None),('mol/dm³',None,None)]),
('Forward reaction goes virtually to completion when K_c is','سیدھا تعامل عملاً تکمیل تک پہنچتا ہے جب K_c ہو','مخکښ تعامل عملاً بشپړېدو ته رسېږي کله چې K_c وي',[('positive and small','مثبت اور چھوٹی','مثبت او کوچنی'),('positive and large','مثبت اور بڑی','مثبت او لوی'),('negative and large','منفی اور بڑی','منفي او لوی'),('unity','اکائی (1)','واحد (1)')]),
('Endothermic reactions are favoured in the forward direction by','گرم گیر تعاملات کو سیدھی سمت میں ترجیح ملتی ہے','تودوخه جذبوونکي تعاملات په مخکښ لوري کې غوره کېږي د',[('cooling','ٹھنڈا کرنے سے','یخولو سره'),('freezing','جمانے سے','کلکولو/یخ کولو سره'),('heating','گرم کرنے سے','تودولو سره'),('adding a catalyst','اتپریرک شامل کرنے سے','د کتلیست په اضافه کولو سره')]),
('Molecules of chlorine decompose to a very small extent into atomic chlorine i.e. Cl₂ ⇌ 2Cl; this is because K_c of this reaction is','کلورین کے سالمے بہت کم حد تک جوہری کلورین میں تحلیل ہوتے ہیں یعنی Cl₂ ⇌ 2Cl؛ اس کی وجہ یہ ہے کہ اس تعامل کا K_c ہے','د کلورین مالیکولونه ډېر لږ اندازې ته په اټومي کلورین تجزیه کېږي یعنې Cl₂ ⇌ 2Cl؛ دا ځکه چې د دې تعامل K_c دی',[('very large','بہت بڑا','ډېر لوی'),('very small','بہت چھوٹا','ډېر کوچنی'),('zero','صفر','صفر'),('1',None,None)])]
for n,(q,u,p,o) in enumerate(Q,1): mcq(s,n,q,u,p,o,236)
s['flow']=[dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 231. The scan is skewed; all questions and options are legible. Question 3 prints ΔH = 92.46 kJ/mol (positive) as given. The page has no clipped words. A CamScanner watermark crosses the page.'
s['vocabulary']={'optimum temperature':{'ur':'موزوں ترین درجہ حرارت','ps':'غوره تودوخه'},'endothermic':{'ur':'گرم گیر','ps':'تودوخه جذبوونکی'}}
save(s)
