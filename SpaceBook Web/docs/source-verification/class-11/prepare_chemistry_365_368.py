from chemlib import *
c=cell
def eqn(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
EC='chem11-electrochemistry'
def mk(n,title,ur,ps,sid): return page(n,EC,title,ur,ps,sid)
class Flow:
    def __init__(s_,s): s_.s=s; s_.s['equations']=[]; s_.f=[]
    def p(s_,*keys):
        s_.f.append(dict(type='paragraphs',ids=[f"chem11-p{s_.s['source']['pdfPage']}-{k}" for k in keys]))
    def e(s_,key,latex,text):
        s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def done(s_): s_.s['flow']=s_.f

# ---------- 365 ----------
s=mk(365,'Oxidation number rules (continued) · Example 12.1 · 12.1.3 Recognizing oxidation and reduction reactions','تکسیدی عدد کے قواعد (جاری) · مثال 12.1 · 12.1.3 تکسیدی اور تخفیفی تعاملات کی شناخت','د اکسیډیشن شمېرې قواعد (دوام) · بېلګه 12.1 · 12.1.3 د اکسیډیشن او ریډکشن تعاملاتو پېژندل','oxidation-rules-ex121')
F=Flow(s)
R=[(f'ii. The oxidation number of hydrogen in its compounds is +1 but in metal hydrides it is −1, e.g. NaH and MgH₂.','ii. ہائیڈروجن کا اپنے مرکبات میں تکسیدی عدد +1 ہے لیکن دھاتی ہائیڈرائیڈز میں یہ −1 ہے، مثلاً NaH اور MgH₂۔','ii. د هایدروجن په خپلو مرکباتو کې د اکسیډیشن شمېره +1 ده خو په فلزي هایدرایډونو کې −1 ده، لکه NaH او MgH₂.'),
('iii. The oxidation number of oxygen in the compounds is −2 but in peroxides it is −1 and in OF₂ is +2.','iii. آکسیجن کا مرکبات میں تکسیدی عدد −2 ہے لیکن پرآکسائیڈز میں یہ −1 اور OF₂ میں +2 ہے۔','iii. د اکسیجن په مرکباتو کې د اکسیډیشن شمېره −2 ده خو په پیرکسایډونو کې −1 او په OF₂ کې +2 ده.'),
('iv. The oxidation numbers of the elements of groups I, II and III in the compounds are +1, +2 and +3 respectively.','iv. مرکبات میں گروپ I، II اور III کے عناصر کے تکسیدی اعداد بالترتیب +1، +2 اور +3 ہیں۔','iv. په مرکباتو کې د I، II او III ګروپونو د عناصرو د اکسیډیشن شمېرې په ترتیب سره +1، +2 او +3 دي.'),
('v. The oxidation number of the halogens of group VII in the binary compounds is −1.','v. بائنری مرکبات میں گروپ VII کے ہیلوجنوں کا تکسیدی عدد −1 ہے۔','v. په دوګونو مرکباتو کې د VII ګروپ د هلوجنونو د اکسیډیشن شمېره −1 ده.'),
('vi. The algebraic sum of the oxidation numbers of all the atoms in a molecule is zero.','vi. سالمے میں تمام ایٹموں کے تکسیدی اعداد کا الجبری مجموعہ صفر ہوتا ہے۔','vi. په مالیکول کې د ټولو اتومونو د اکسیډیشن شمېرو الجبري مجموعه صفر ده.'),
('vii. The algebraic sum of the oxidation numbers of all the atoms in an ion is equal to the charge on the ion.','vii. آئن میں تمام ایٹموں کے تکسیدی اعداد کا الجبری مجموعہ آئن پر چارج کے برابر ہوتا ہے۔','vii. په آیون کې د ټولو اتومونو د اکسیډیشن شمېرو الجبري مجموعه په آیون د چارج سره مساوي ده.')]
for i,(e,u,p) in enumerate(R,1): add(s,f'r{i}',e,u,p)
add(s,'e1','Example 12.1:','مثال 12.1:','بېلګه 12.1:',kind='heading')
add(s,'q1','Calculate the oxidation number of Cr in K₂Cr₂O₇.','K₂Cr₂O₇ میں Cr کا تکسیدی عدد معلوم کریں۔','په K₂Cr₂O₇ کې د Cr د اکسیډیشن شمېره محاسبه کړئ.')
add(s,'q2','Oxidation Number of K = +1   Oxidation Number of O = −2','K کا تکسیدی عدد = +1   O کا تکسیدی عدد = −2','د K د اکسیډیشن شمېره = +1   د O د اکسیډیشن شمېره = −2')
add(s,'q3','Oxidation Number of Cr = X','Cr کا تکسیدی عدد = X','د Cr د اکسیډیشن شمېره = X')
add(s,'q4','Putting these values in the formula K₂Cr₂O₇','ان قیمتوں کو فارمولا K₂Cr₂O₇ میں رکھنے پر','دا ارزښتونه په فورمول K₂Cr₂O₇ کې ایښودلو سره')
add(s,'p1h','Practice Problem: 12.1','مشقی مسئلہ: 12.1','د تمرین ستونزه: 12.1',kind='heading')
add(s,'p1','Calculate the oxidation number of S in H₂SO₄.','H₂SO₄ میں S کا تکسیدی عدد معلوم کریں۔','په H₂SO₄ کې د S د اکسیډیشن شمېره محاسبه کړئ.')
add(s,'h3','12.1.3 Recognizing oxidation and reduction reactions','12.1.3 تکسیدی اور تخفیفی تعاملات کی شناخت','12.1.3 د اکسیډیشن او ریډکشن تعاملاتو پېژندل',kind='heading')
add(s,'a1',f'Oxidation reduction reactions are reactions in which electrons are lost by an atom or ion in one reactant and gained by an atom or ion in another reactant. In order to tell whether a redox reaction has occurred or not, we need a way to keep track of electrons and assign oxidation numbers to the atoms or ions involved in a chemical reaction.{SO}',f'تکسید و تخفیف کے تعاملات وہ تعاملات ہیں جن میں ایک تعامل کنندہ کے ایٹم یا آئن سے الیکٹران کھوئے جاتے ہیں اور دوسرے تعامل کنندہ کے ایٹم یا آئن کے ذریعے حاصل کیے جاتے ہیں۔ یہ بتانے کے لیے کہ ریڈاکس تعامل ہوا ہے یا نہیں ہمیں الیکٹرانوں کا حساب رکھنے کا ایک طریقہ چاہیے اور کیمیائی تعامل میں شامل ایٹموں یا آئنوں کو تکسیدی اعداد تفویض کرنے ہوں گے {SO}۔',f'د اکسیډیشن ریډکشن تعاملات هغه تعاملات دي چې په هغو کې الکترونونه په یو متعامل کې د اتوم یا آیون په واسطه له لاسه ورکول کېږي او په بل متعامل کې د اتوم یا آیون په واسطه ترلاسه کېږي. د دې ویلو لپاره چې ریډاکس تعامل رامنځته شوی که نه موږ د الکترونونو د حساب ساتلو لار ته اړتیا لرو او په کيمياوي تعامل کې شاملو اتومونو یا آیونونو ته د اکسیډیشن شمېرې ټاکل کېږي {SO}.')
add(s,'a2',f'In any redox reaction, you can recognize the species oxidized or reduced by noting the change in their oxidation number. A species with an increase in oxidation number is said to be oxidized and the one with decrease in oxidation number is said to be reduced as clear from the following example. In organic reactions, the concept of addition or removal of oxygen or hydrogen can also be helpful in such case.{SO}',f'کسی بھی ریڈاکس تعامل میں آپ تکسیدی عدد میں تبدیلی کو نوٹ کر کے تکسید یا تخفیف پانے والی انواع کو پہچان سکتے ہیں۔ جس نوع کے تکسیدی عدد میں اضافہ ہو اسے تکسید شدہ اور جس کے تکسیدی عدد میں کمی ہو اسے تخفیف شدہ کہا جاتا ہے جیسا کہ درج ذیل مثال سے واضح ہے۔ نامیاتی تعاملات میں آکسیجن یا ہائیڈروجن کے اضافے یا ہٹانے کا تصور بھی ایسی صورت میں مفید ہو سکتا ہے {SO}۔',f'په هر ریډاکس تعامل کې تاسو کولای شئ د اکسیډیشن شمېرې بدلون یادښت کولو سره اکسیډیز یا ریډیوس شوي ډولونه وپېژنئ. هغه ډول چې د اکسیډیشن شمېره یې زیاتېږي اکسیډیز او هغه چې کمېږي ریډیوس ویل کېږي لکه څنګه چې له لاندې بېلګې څخه څرګنده ده. په عضوي تعاملاتو کې د اکسیجن یا هایدروجن د اضافه کولو یا لرې کولو مفکوره هم په داسې حالت کې ګټوره کېدای شي {SO}.')
add(s,'e2','Example 12.2:','مثال 12.2:','بېلګه 12.2:',kind='heading')
add(s,'q5',f'Determine which element is oxidized and which one is reduced in the following reactions.{SO}',f'تعین کریں کہ درج ذیل تعاملات میں کون سا عنصر تکسید شدہ اور کون سا تخفیف شدہ ہے {SO}۔',f'وټاکئ چې په لاندې تعاملاتو کې کوم عنصر اکسیډیز شوی او کوم ریډیوس شوی {SO}.')
F.p('r1','r2','r3','r4','r5','r6','e1','q1','q2','q3','q4')
F.e('c1',r'2(+1)+2X+7(-2)=0','2(+1) + 2X + 7(−2) = 0')
F.e('c2','2+2X-14=0','2 + 2X − 14 = 0')
F.e('c3','2X=12','2X = 12')
F.e('c4','X=6','X = 6')
F.p('p1h','p1','h3','a1','a2','e2','q5')
F.done()
s['sourceNote']='Printed folio 360. The right edge is clipped by the page curl on rules ii–vii and the 12.1.3 paragraphs (word endings cut); the sentences are legible and read in full; clipped fragments are marked [scan obscured]. Rule i is on the previous page. Example 12.2 continues on the next page. The footer is partly cut. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; Example 12.2 continues on the next page.')
s['vocabulary']={'oxidized':{'ur':'تکسید شدہ','ps':'اکسیډیز شوی'},'reduced':{'ur':'تخفیف شدہ','ps':'ریډیوس شوی'}}
save(s)

# ---------- 366 ----------
s=mk(366,'Example 12.2 solution · Oxidizing and Reducing Agent · 12.1.4 Balancing Redox Equations by Oxidation Number Method','مثال 12.2 کا حل · تکسیدی اور تخفیفی ایجنٹ · 12.1.4 تکسیدی عدد کے طریقے سے ریڈاکس مساواتوں کو متوازن کرنا','د بېلګې 12.2 حل · اکسیډېزنګ او ریډیوسینګ اجنټ · 12.1.4 د اکسیډیشن شمېرې په طریقه د ریډاکس معادلو انډولول','agents-balancing')
F=Flow(s)
add(s,'a0','following reactions.','درج ذیل تعاملات۔','لاندې تعاملات.')
add(s,'sol','Solution:','حل:','حل:',kind='heading')
add(s,'a1','a. Zn is oxidized (oxidation number: 0 → +2); H⁺ is reduced (Oxidation number +1 → 0).','الف۔ Zn تکسید شدہ ہے (تکسیدی عدد: 0 → +2)؛ H⁺ تخفیف شدہ ہے (تکسیدی عدد +1 → 0)۔','الف. Zn اکسیډیز شوی دی (د اکسیډیشن شمېره: 0 → +2)؛ H⁺ ریډیوس شوی دی (د اکسیډیشن شمېره +1 → 0).')
add(s,'a2','b. Al is oxidized (oxidation number: 0 → +3); Cu²⁺ is reduced (+2 → 0). Thus when oxidation occurs, an element loses electrons and its oxidation number increases (become more positive). When reduction occurs, an element gains electrons and its oxidation number decreases or is reduced (becomes more negative).','ب۔ Al تکسید شدہ ہے (تکسیدی عدد: 0 → +3)؛ Cu²⁺ تخفیف شدہ ہے (+2 → 0)۔ اس طرح جب تکسید ہوتا ہے تو عنصر الیکٹران کھوتا ہے اور اس کا تکسیدی عدد بڑھتا ہے (زیادہ مثبت ہو جاتا ہے)۔ جب تخفیف ہوتی ہے تو عنصر الیکٹران حاصل کرتا ہے اور اس کا تکسیدی عدد کم ہوتا ہے (زیادہ منفی ہو جاتا ہے)۔','ب. Al اکسیډیز شوی دی (د اکسیډیشن شمېره: 0 → +3)؛ Cu²⁺ ریډیوس شوی دی (+2 → 0). په دې توګه کله چې اکسیډیشن پېښېږي نو عنصر الکترونونه له لاسه ورکوي او د هغه د اکسیډیشن شمېره زیاتېږي (ډېره مثبته کېږي). کله چې ریډکشن پېښېږي نو عنصر الکترونونه ترلاسه کوي او د هغه د اکسیډیشن شمېره کمېږي (ډېره منفي کېږي).')
add(s,'h1','(i) Oxidizing Agent','(i) تکسیدی ایجنٹ (آکسیڈائزنگ ایجنٹ)','(i) اکسیډېزنګ اجنټ',kind='heading')
add(s,'b1','The substance which oxidizes other substances and itself gets reduced during this process is called oxidizing agent. The oxidation number of oxidizing agent is decreased in the reaction e.g. the oxidation number of Cl₂ in above reaction is decreased from 0 to −1, therefore, Cl₂ is an oxidizing agent.','وہ مادہ جو دوسرے مادوں کو تکسید کرتا ہے اور اس عمل کے دوران خود تخفیف پاتا ہے تکسیدی ایجنٹ کہلاتا ہے۔ تعامل میں تکسیدی ایجنٹ کا تکسیدی عدد کم ہوتا ہے مثلاً مندرجہ بالا تعامل میں Cl₂ کا تکسیدی عدد 0 سے −1 تک کم ہوا ہے، اس لیے Cl₂ ایک تکسیدی ایجنٹ ہے۔','هغه مواد چې نور مواد اکسیډیز کوي او پخپله پدې پروسه کې ریډیوس کېږي اکسیډېزنګ اجنټ بلل کېږي. په تعامل کې د اکسیډېزنګ اجنټ د اکسیډیشن شمېره کمېږي لکه په پورتني تعامل کې د Cl₂ د اکسیډیشن شمېره له 0 څخه −1 ته کمه شوې، نو Cl₂ یو اکسیډېزنګ اجنټ دی.')
add(s,'h2','(ii) Reducing Agent','(ii) تخفیفی ایجنٹ (ریڈیوسنگ ایجنٹ)','(ii) ریډیوسینګ اجنټ',kind='heading')
add(s,'b2','The substance which reduces other substances and itself gets oxidized during this process is called reducing agent. The oxidation number of the reducing agent is increased e.g. the oxidation number of Na in above reaction is increased from 0 to +1 so it is a reducing agent.','وہ مادہ جو دوسرے مادوں کو تخفیف کرتا ہے اور اس عمل کے دوران خود تکسید پاتا ہے تخفیفی ایجنٹ کہلاتا ہے۔ تخفیفی ایجنٹ کا تکسیدی عدد بڑھتا ہے مثلاً مندرجہ بالا تعامل میں Na کا تکسیدی عدد 0 سے +1 تک بڑھا ہے اس لیے یہ تخفیفی ایجنٹ ہے۔','هغه مواد چې نور مواد ریډیوس کوي او پخپله پدې پروسه کې اکسیډیز کېږي ریډیوسینګ اجنټ بلل کېږي. د ریډیوسینګ اجنټ د اکسیډیشن شمېره زیاتېږي لکه په پورتني تعامل کې د Na د اکسیډیشن شمېره له 0 څخه +1 ته زیاته شوې نو دا یو ریډیوسینګ اجنټ دی.')
add(s,'h3','Balancing Oxidation Reduction Equations','تکسید و تخفیف کی مساواتوں کو متوازن کرنا','د اکسیډیشن ریډکشن معادلو انډولول',kind='heading')
add(s,'c1','A large variety of chemical reactions involve oxidation and reduction processes which are expressed in the form of chemical equations. There are two systematic ways for balancing these equations.','کیمیائی تعاملات کی ایک بڑی قسم تکسید اور تخفیف کے عملوں پر مشتمل ہوتی ہے جو کیمیائی مساواتوں کی صورت میں ظاہر کیے جاتے ہیں۔ ان مساواتوں کو متوازن کرنے کے دو منظم طریقے ہیں۔','د کيمياوي تعاملاتو یو لوی شمېر د اکسیډیشن او ریډکشن پروسې شاملوي چې د کيمياوي معادلو په بڼه ښودل کېږي. د دې معادلو د انډولولو دوه منظمې لارې شته.')
add(s,'h4','12.1.4 Balancing Redox Equations by Oxidation Number Method','12.1.4 تکسیدی عدد کے طریقے سے ریڈاکس مساواتوں کو متوازن کرنا','12.1.4 د اکسیډیشن شمېرې په طریقه د ریډاکس معادلو انډولول',kind='heading')
add(s,'c2','Oxidation and reduction are simultaneous processes; collectively called redox process. If one substance in a reaction is oxidized, it loses electrons and acts as reducing agent, then the other substance, simultaneously, is reduced, gains electrons and acts as oxidizing agent. The number of electron gained and lost must be equal. This principle builds the basis of balancing the redox equation. The following steps are involved in balancing equations by oxidation number method.','تکسید اور تخفیف بیک وقت ہونے والے عمل ہیں؛ جنہیں مجموعی طور پر ریڈاکس عمل کہتے ہیں۔ اگر کسی تعامل میں ایک مادہ تکسید پاتا ہے تو وہ الیکٹران کھوتا ہے اور تخفیفی ایجنٹ کے طور پر کام کرتا ہے، پھر دوسرا مادہ بیک وقت تخفیف پاتا ہے، الیکٹران حاصل کرتا ہے اور تکسیدی ایجنٹ کے طور پر کام کرتا ہے۔ حاصل اور کھوئے گئے الیکٹرانوں کی تعداد برابر ہونی چاہیے۔ یہ اصول ریڈاکس مساوات کو متوازن کرنے کی بنیاد ہے۔ تکسیدی عدد کے طریقے سے مساواتوں کو متوازن کرنے میں درج ذیل مراحل شامل ہیں۔','اکسیډیشن او ریډکشن یو مهال پېښېدونکې پروسې دي؛ چې ګډ ډول ریډاکس پروسه بلل کېږي. که په یوه تعامل کې یو مواد اکسیډیز شي نو الکترونونه له لاسه ورکوي او د ریډیوسینګ اجنټ په توګه عمل کوي، بیا بل مواد په یو مهال ریډیوس کېږي، الکترونونه ترلاسه کوي او د اکسیډېزنګ اجنټ په توګه عمل کوي. د ترلاسه شویو او له لاسه ورکړل شویو الکترونونو شمېر باید مساوي وي. دا اصل د ریډاکس معادلې د انډولولو بنسټ جوړوي. د اکسیډیشن شمېرې په طریقه د معادلو په انډولولو کې لاندې ګامونه شامل دي.')
add(s,'s1','i. Write down the skeleton of the unbalanced redox equation.','i. غیر متوازن ریڈاکس مساوات کا ڈھانچہ لکھیں۔','i. د نه انډول شوې ریډاکس معادلې سکلیټ ولیکئ.')
add(s,'s2','ii. Write the oxidation numbers over the symbol of the elements whose oxidation numbers change during the reaction.','ii. ان عناصر کی علامتوں کے اوپر تکسیدی اعداد لکھیں جن کے تکسیدی اعداد تعامل کے دوران بدلتے ہیں۔','ii. د هغو عناصرو د سمبولونو پر سر د اکسیډیشن شمېرې ولیکئ چې د اکسیډیشن شمېرې یې د تعامل پر مهال بدلېږي.')
F.p('a0','sol','a1')
F.p('a2','h1','b1','h2','b2','h3','c1','h4','c2','s1','s2')
F.done()
# reaction lines a) b) as equations inserted after a0
s['equations']=[eqn(366,'ra',r'\text{a)}\ \mathrm{Zn+2H^+\rightarrow Zn^{2+}+H_2}','a) Zn + 2H⁺ → Zn²⁺ + H₂'),eqn(366,'rb',r'\text{b)}\ 2\mathrm{Al+3Cu^{2+}\rightarrow2Al^{3+}+3Cu}','b) 2Al + 3Cu²⁺ → 2Al³⁺ + 3Cu')]
s['flow']=[dict(type='paragraphs',ids=['chem11-p366-a0']),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[f'chem11-p366-{k}' for k in ('sol','a1','a2','h1','b1','h2','b2','h3','c1','h4','c2','s1','s2')])]
s['sourceNote']='Printed folio 361. The sentence at the top completes Example 12.2 from the previous page. The text under (i) and (ii) refers to "the above reaction" (with Cl₂ and Na) which is not printed on this page; retained as printed. The left edge is slightly clipped. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Oxidizing/reducing agent text refers to a reaction (Cl₂, Na) not shown on this page.')
s['vocabulary']={'oxidizing agent':{'ur':'تکسیدی ایجنٹ','ps':'اکسیډېزنګ اجنټ'},'reducing agent':{'ur':'تخفیفی ایجنٹ','ps':'ریډیوسینګ اجنټ'}}
save(s)

# ---------- 367 ----------
s=mk(367,'Steps iii–vi · Example 12.3 Balancing Zn + HNO₃','مراحل iii–vi · مثال 12.3 Zn + HNO₃ کو متوازن کرنا','ګامونه iii–vi · بېلګه 12.3 د Zn + HNO₃ انډولول','steps-example123')
F=Flow(s)
add(s,'s3','iii. Identify the oxidizing and reducing agents, which undergo change in their oxidation number.','iii. تکسیدی اور تخفیفی ایجنٹوں کی شناخت کریں جن کے تکسیدی عدد میں تبدیلی ہوتی ہے۔','iii. اکسیډېزنګ او ریډیوسینګ اجنټونه وپېژنئ چې د اکسیډیشن شمېره یې بدلېږي.')
add(s,'s4','iv. Indicate the change in oxidation number by means of arrows which show the number of electrons gained or lost.','iv. تکسیدی عدد میں تبدیلی تیروں کے ذریعے ظاہر کریں جو حاصل یا کھوئے گئے الیکٹرانوں کی تعداد دکھاتے ہیں۔','iv. د اکسیډیشن شمېرې بدلون د غشو په واسطه وښیئ چې د ترلاسه یا له لاسه ورکړل شویو الکترونونو شمېر ښيي.')
add(s,'s5','v. Multiply the formula of the oxidizing and the reducing agents by a number such that the number of electrons lost during oxidation becomes equal to the gain of electrons during reduction.','v. تکسیدی اور تخفیفی ایجنٹوں کے فارمولے کو ایک ایسے عدد سے ضرب دیں کہ تکسید کے دوران کھوئے گئے الیکٹرانوں کی تعداد تخفیف کے دوران حاصل کیے گئے الیکٹرانوں کے برابر ہو جائے۔','v. د اکسیډېزنګ او ریډیوسینګ اجنټونو فورمول په یوې شمېرې کې ضرب کړئ چې د اکسیډیشن پر مهال له لاسه ورکړل شویو الکترونونو شمېر د ریډکشن پر مهال له ترلاسه شویو الکترونونو سره مساوي شي.')
add(s,'s6','vi. Balance the rest of the equation by simple inspection.','vi. باقی مساوات کو سادہ معائنے سے متوازن کریں۔','vi. د معادلې پاتې برخه په ساده کتنې انډول کړئ.')
add(s,'e','Example 12.3','مثال 12.3','بېلګه 12.3',kind='heading')
add(s,'q','Let us balance the following equation by oxidation number method, by using the above mentioned steps.','آئیے مندرجہ بالا مراحل استعمال کر کے درج ذیل مساوات کو تکسیدی عدد کے طریقے سے متوازن کریں۔','راځئ لاندې معادله د اکسیډیشن شمېرې په طریقه، د پورتنیو ګامونو په کارولو سره انډول کړو.')
add(s,'i','(i) Zn + HNO₃ → Zn(NO₃)₂ + NO + H₂O','(i) Zn + HNO₃ → Zn(NO₃)₂ + NO + H₂O','(i) Zn + HNO₃ → Zn(NO₃)₂ + NO + H₂O')
add(s,'ii','(ii) Oxidation number of Zn is 0, oxidation number of Zn in Zn(NO₃)₂ is +2. Oxidation numbers of Zn increases from 0 to +2, so it is oxidized and is a reducing agent. Oxidation number of N decreases from +5 in HNO₃ to +2 in NO so it is reduced and acts as an oxidizing agent.','(ii) Zn کا تکسیدی عدد 0 ہے، Zn(NO₃)₂ میں Zn کا تکسیدی عدد +2 ہے۔ Zn کا تکسیدی عدد 0 سے +2 تک بڑھتا ہے اس لیے یہ تکسید شدہ اور تخفیفی ایجنٹ ہے۔ N کا تکسیدی عدد HNO₃ میں +5 سے NO میں +2 تک کم ہوتا ہے اس لیے یہ تخفیف شدہ ہے اور تکسیدی ایجنٹ کے طور پر کام کرتا ہے۔','(ii) د Zn د اکسیډیشن شمېره 0 ده، په Zn(NO₃)₂ کې د Zn د اکسیډیشن شمېره +2 ده. د Zn د اکسیډیشن شمېره له 0 څخه +2 ته زیاتېږي نو دا اکسیډیز شوی او ریډیوسینګ اجنټ دی. د N د اکسیډیشن شمېره په HNO₃ کې له +5 څخه په NO کې +2 ته کمېږي نو دا ریډیوس شوی او د اکسیډېزنګ اجنټ په توګه عمل کوي.')
add(s,'iii','(iii) Write the oxidation numbers over the symbols of the elements oxidized and reduced.','(iii) تکسید اور تخفیف پانے والے عناصر کی علامتوں کے اوپر تکسیدی اعداد لکھیں۔','(iii) د اکسیډیز او ریډیوس شویو عناصرو د سمبولونو پر سر د اکسیډیشن شمېرې ولیکئ.')
add(s,'iv','(iv) Indicate the change in oxidation numbers by means of arrows.','(iv) تکسیدی اعداد میں تبدیلی تیروں کے ذریعے ظاہر کریں۔','(iv) د اکسیډیشن شمېرو بدلون د غشو په واسطه وښیئ.')
add(s,'hence','Hence, the species reduced and oxidized can be written as follows:','لہٰذا تخفیف اور تکسید پانے والی انواع کو اس طرح لکھا جا سکتا ہے:','نو ریډیوس او اکسیډیز شوي ډولونه داسې لیکل کېدای شي:')
add(s,'v','(v) Multiply equation (a) by 3 and (b) by 2, so that the number of electrons gained becomes equal to the number of electrons lost. By this way we get coefficients of different species appeared in equation given in part (i) above which takes the following form','(v) مساوات (a) کو 3 سے اور (b) کو 2 سے ضرب دیں تاکہ حاصل کیے گئے الیکٹرانوں کی تعداد کھوئے گئے الیکٹرانوں کی تعداد کے برابر ہو جائے۔ اس طرح ہمیں اوپر حصہ (i) میں دی گئی مساوات میں آنے والی مختلف انواع کے عددی سر ملتے ہیں جو درج ذیل شکل اختیار کرتی ہے','(v) معادله (a) په 3 او (b) په 2 کې ضرب کړئ، ترڅو د ترلاسه شویو الکترونونو شمېر له لاسه ورکړل شویو الکترونونو شمېر سره مساوي شي. په دې توګه موږ په پورتنۍ برخه (i) کې ورکړل شوې معادله کې د راتلونکو بېلابېلو ډولونو ضریبونه ترلاسه کوو چې لاندې بڼه اخلي')
add(s,'vi',f'(vi) Add six more NO₃⁻ in the form of HNO₃ to the reactant\'s side, to balance 6NO₃⁻ of Zn(NO₃)₂ in the products side. Also balance H and O atom by inspection.',f'(vi) حاصلات کی طرف Zn(NO₃)₂ کے 6NO₃⁻ کو متوازن کرنے کے لیے تعامل کنندگان کی طرف HNO₃ کی شکل میں چھ مزید NO₃⁻ شامل کریں۔ H اور O ایٹموں کو بھی معائنے سے متوازن کریں۔',f'(vi) د محصولاتو په اړخ کې د Zn(NO₃)₂ د 6NO₃⁻ د انډولولو لپاره د متعاملینو په اړخ کې د HNO₃ په بڼه شپږ نور NO₃⁻ اضافه کړئ. د H او O اتومونه هم په کتنې انډول کړئ.')
F.p('s3','s4','s5','s6','e','q','i','ii','iii')
F.e('o1',r'\mathrm{Zn+HN^{+5}O_3\longrightarrow Zn^{+2}(NO_3)_2+N^{+2}O+H_2O}','Zn + HN⁺⁵O₃ → Zn⁺²(NO₃)₂ + N⁺²O + H₂O')
F.p('iv')
F.e('o2',r'\mathrm{Zn+HNO_3\longrightarrow Zn(NO_3)_2+NO+H_2O}\quad(\text{Reduced; Oxidized})','Zn + HNO₃ → Zn(NO₃)₂ + NO + H₂O   (N reduced; Zn oxidized)')
F.p('hence')
F.e('a',r'\text{a)}\ \mathrm{Zn^0\longrightarrow Zn^{2+}+2e^-}\quad\text{(Zn oxidized)}','a) Zn⁰ → Zn²⁺ + 2e⁻   (Zn oxidized)')
F.e('b',r'\text{b)}\ \mathrm{HN^{+5}O_3+3e^-\longrightarrow N^{2+}O}\quad\text{(N reduced)}','b) HN⁺⁵O₃ + 3e⁻ → N²⁺O   (N reduced)')
F.p('v')
F.e('v1',r'3\mathrm{Zn}+2\mathrm{HNO_3}\longrightarrow3\mathrm{Zn(NO_3)_2}+2\mathrm{NO}+\mathrm{O_2}','3Zn + 2HNO₃ → 3Zn(NO₃)₂ + 2NO + O₂')
F.p('vi')
F.e('v2',r'3\mathrm{Zn}+2\mathrm{HNO_3}+6\mathrm{HNO_3}\longrightarrow3\mathrm{Zn(NO_3)_2}+2\mathrm{NO}+4\mathrm{H_2O}','3Zn + 2HNO₃ + 6HNO₃ → 3Zn(NO₃)₂ + 2NO + 4H₂O')
F.done()
s['sourceNote']='Printed folio 362. The right edge is clipped on a few lines ("…change in their [oxidation number]", "…which show", "…becomes", "…is +2") but the sentences are legible and read in full. The skewed equations in steps (iii) and (iv) (oxidation numbers written above symbols; arrows labelled "Reduced" and "Oxidized") are recorded as equations. In step (v) the printed equation ends "+ O₂" as printed (it is corrected in the next step). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Slight right-edge clipping; step (v) equation printed with "+ O₂" and retained.')
s['vocabulary']={}
save(s)

# ---------- 368 ----------
s=mk(368,'Final balanced equation · 12.1.5 Balancing Redox Equations by the Half Reaction Method · Example 12.4','حتمی متوازن مساوات · 12.1.5 نیم تعامل کے طریقے سے ریڈاکس مساواتوں کو متوازن کرنا · مثال 12.4','وروستۍ انډول شوې معادله · 12.1.5 د نیمایي تعامل په طریقه د ریډاکس معادلو انډولول · بېلګه 12.4','half-reaction-method')
F=Flow(s)
add(s,'a0','Now the final balanced equation is:','اب حتمی متوازن مساوات یہ ہے:','اوس وروستۍ انډول شوې معادله دا ده:')
add(s,'h','12.1.5. Balancing the Redox Equations by the Half Reaction Method','12.1.5 نیم تعامل کے طریقے سے ریڈاکس مساواتوں کو متوازن کرنا','12.1.5 د نیمایي تعامل په طریقه د ریډاکس معادلو انډولول',kind='heading')
add(s,'a1','This method of balancing is also called the ion electron method. No oxidation numbers are assigned in this method. It applies to redox reactions taking place in aqueous medium. The following steps are used for balancing redox equation by this method.','توازن کا یہ طریقہ آئن الیکٹران طریقہ بھی کہلاتا ہے۔ اس طریقے میں تکسیدی اعداد تفویض نہیں کیے جاتے۔ یہ آبی واسطے میں ہونے والے ریڈاکس تعاملات پر لاگو ہوتا ہے۔ اس طریقے سے ریڈاکس مساوات کو متوازن کرنے کے لیے درج ذیل مراحل استعمال کیے جاتے ہیں۔','دا د انډولولو طریقه د آیون الکترون طریقه هم بلل کېږي. پدې طریقه کې د اکسیډیشن شمېرې نه ټاکل کېږي. دا په اوبیز منځګړي کې پېښېدونکو ریډاکس تعاملاتو باندې تطبیقېږي. د دې طریقې په واسطه د ریډاکس معادلې د انډولولو لپاره لاندې ګامونه کارول کېږي.')
S=[('i. Split the equation into two half reactions, one for oxidation and the other for reduction showing only the oxidizing and reducing agents.','i. مساوات کو دو نیم تعاملات میں تقسیم کریں، ایک تکسید کے لیے اور دوسرا تخفیف کے لیے جس میں صرف تکسیدی اور تخفیفی ایجنٹ دکھائے جائیں۔','i. معادله په دوو نیمایي تعاملاتو ویشئ، یو د اکسیډیشن لپاره او بل د ریډکشن لپاره چې یوازې اکسیډېزنګ او ریډیوسینګ اجنټونه ښيي.'),
('ii. Balance number of atoms on both sides of the two half reactions independently. In neutral medium H₂O and H⁺ can be added on either side.','ii. دونوں نیم تعاملات کے دونوں اطراف ایٹموں کی تعداد کو الگ الگ متوازن کریں۔ معتدل واسطے میں H₂O اور H⁺ کسی بھی طرف شامل کیے جا سکتے ہیں۔','ii. د دواړو نیمایي تعاملاتو په دواړو اړخونو کې د اتومونو شمېر په جلا جلا ډول انډول کړئ. په خنثی منځګړي کې H₂O او H⁺ په هر اړخ کې اضافه کېدای شي.'),
('iii. In acidic medium the H⁺ ion may be used for greater number of oxygen and H₂O can be added to the other side.','iii. تیزابی واسطے میں H⁺ آئن آکسیجن کی زیادہ تعداد کے لیے استعمال کیا جا سکتا ہے اور H₂O دوسری طرف شامل کیا جا سکتا ہے۔','iii. په اسیدي منځګړي کې H⁺ آیون د اکسیجن د ډېر شمېر لپاره کارېدای شي او H₂O بل اړخ ته اضافه کېدای شي.'),
('iv. Balance the charge by adding electrons (e⁻) to the side deficient in negative charge.','iv. منفی چارج کی کمی والی طرف الیکٹران (e⁻) شامل کر کے چارج کو متوازن کریں۔','iv. چارج د منفي چارج په کمښت لرونکي اړخ ته د الکترونونو (e⁻) په اضافه کولو سره انډول کړئ.'),
('v. Multiply each half reaction by a number chosen so that the total number of electrons lost by the reducing agent equals the number of the electrons gained by the oxidizing agent.','v. ہر نیم تعامل کو ایک ایسے عدد سے ضرب دیں جو اس طرح چنا گیا ہو کہ تخفیفی ایجنٹ کے کھوئے ہوئے الیکٹرانوں کی کل تعداد تکسیدی ایجنٹ کے حاصل کیے ہوئے الیکٹرانوں کی تعداد کے برابر ہو۔','v. هر نیمایي تعامل په یوې شمېرې کې ضرب کړئ چې داسې غوره شوې وي چې د ریډیوسینګ اجنټ لخوا له لاسه ورکړل شویو الکترونونو ټول شمېر د اکسیډېزنګ اجنټ لخوا ترلاسه شویو الکترونونو له شمېر سره مساوي شي.'),
('vi. Add the two half reactions resulting from the multiplications. Cancel anything appearing to both sides in the net equation.','vi. ضرب کے نتیجے میں حاصل ہونے والے دونوں نیم تعاملات کو جمع کریں۔ خالص مساوات میں دونوں طرف ظاہر ہونے والی ہر چیز کاٹ دیں۔','vi. د ضرب په پایله کې ترلاسه شوي دواړه نیمایي تعاملات یوځای کړئ. په خالصه معادله کې په دواړو اړخونو ښکارېدونکې هره شی لغوه کړئ.'),
('vii. Check the final equation by counting the number of atoms and the net charge on either side.','vii. حتمی مساوات کو دونوں طرف ایٹموں کی تعداد اور خالص چارج گن کر جانچیں۔','vii. وروستۍ معادله د هر اړخ د اتومونو شمېر او خالص چارج په شمېرلو سره وڅېړئ.')]
for i,(e,u,p) in enumerate(S,1): add(s,f's{i}',e,u,p)
add(s,'e','Example 12.4','مثال 12.4','بېلګه 12.4',kind='heading')
add(s,'q','Balance the following equation of the reaction taking place in acidic medium by ion electron method.','اسیدی واسطے میں ہونے والے تعامل کی درج ذیل مساوات کو آئن الیکٹران طریقے سے متوازن کریں۔','د لاندې تعامل معادله چې په اسیدي منځګړي کې پېښېږي د آیون الکترون په طریقه انډول کړئ.')
add(s,'i1','i) Split the reaction into two half reactions, one for oxidation and the other for reduction.','i) تعامل کو دو نیم تعاملات میں تقسیم کریں، ایک تکسید کے لیے اور دوسرا تخفیف کے لیے۔','i) تعامل په دوو نیمایي تعاملاتو ویشئ، یو د اکسیډیشن لپاره او بل د ریډکشن لپاره.')
add(s,'ii1','ii) Balance the number of O-atoms on each half reaction by adding H⁺ (oxygen excess side) and H₂O to other side. Also multiply I⁻ by 2 in Equation (a)','ii) ہر نیم تعامل پر O ایٹموں کی تعداد H⁺ (آکسیجن کی زیادتی والی طرف) اور دوسری طرف H₂O شامل کر کے متوازن کریں۔ مساوات (a) میں I⁻ کو بھی 2 سے ضرب دیں','ii) په هر نیمایي تعامل کې د O اتومونو شمېر د H⁺ (د اکسیجن د زیاتوالي اړخ) او بل اړخ ته H₂O په اضافه کولو سره انډول کړئ. په معادله (a) کې I⁻ هم په 2 کې ضرب کړئ')
add(s,'iii1','iii) Balance the charges on both sides of each half reaction by adding electrons to either side.','iii) ہر نیم تعامل کے دونوں اطراف چارج کو کسی بھی طرف الیکٹران شامل کر کے متوازن کریں۔','iii) د هر نیمایي تعامل په دواړو اړخونو کې چارجونه په هر اړخ ته د الکترونونو په اضافه کولو سره انډول کړئ.')
F.p('a0')
F.e('f',r'3\mathrm{Zn}+8\mathrm{HNO_3}\longrightarrow3\mathrm{Zn(NO_3)_2}+2\mathrm{NO}+4\mathrm{H_2O}','3Zn + 8HNO₃ → 3Zn(NO₃)₂ + 2NO + 4H₂O')
F.p('h','a1','s1','s2','s3','s4','s5','s6','s7','e','q')
F.e('r',r'\mathrm{I^-+NO_2\longrightarrow I_2+NO}','I⁻ + NO₂ → I₂ + NO')
F.p('i1')
F.e('a',r'\text{a)}\ \mathrm{I^-\longrightarrow I_2}\quad\text{(increase in oxidation number shows oxidation)}','a) I⁻ → I₂   (increase in oxidation number shows oxidation)')
F.e('b',r'\text{b)}\ \mathrm{NO_2\longrightarrow NO}\quad\text{(decrease in oxidation number of N shows reduction)}','b) NO₂ → NO   (decrease in oxidation number of N shows reduction)')
F.p('ii1')
F.e('c',r'\text{a)}\ 2\mathrm{I^-\longrightarrow I_2}','a) 2I⁻ → I₂')
F.e('d',r'\text{b)}\ \mathrm{NO_2+2H^+\longrightarrow NO+H_2O}','b) NO₂ + 2H⁺ → NO + H₂O')
F.p('iii1')
F.done()
s['sourceNote']='Printed folio 363 (the folio number is partly cut). The scan is skewed; the right edge is slightly clipped on the step list. A CamScanner watermark crosses the page. Example 12.4 continues on the next page.'
s['sourceGap']=dict(note='Skewed scan; Example 12.4 continues on the next page.')
s['vocabulary']={'half reaction':{'ur':'نیم تعامل','ps':'نیمایی تعامل'},'ion electron method':{'ur':'آئن الیکٹران طریقہ','ps':'د آیون الکترون طریقه'}}
save(s)
