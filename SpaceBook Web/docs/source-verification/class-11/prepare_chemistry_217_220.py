from chemlib import *
c=cell
def eqn(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
class Flow:
    def __init__(s_,s): s_.s=s; s_.s['equations']=[]; s_.f=[]; s_.n=0
    def p(s_,*keys):
        s_.f.append(dict(type='paragraphs',ids=[f"chem11-p{s_.s['source']['pdfPage']}-{k}" for k in keys]))
    def e(s_,key,latex,text):
        s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def done(s_): s_.s['flow']=s_.f

# ---------- 217 ----------
s=page(217,'chem11-equilibrium','Necessary conditions of equilibrium · Types of chemical equilibrium · 7.1.2 The law of Mass Action','توازن کی ضروری شرائط · کیمیائی توازن کی اقسام · 7.1.2 قانونِ کمیتِ عمل','د تعادل اړین شرایط · د کيمياوي تعادل ډولونه · 7.1.2 د کتلې د عمل قانون','conditions-mass-action')
F=Flow(s)
add(s,'n0','The necessary conditions of equilibrium are as follows:','توازن کی ضروری شرائط درج ذیل ہیں:','د تعادل اړین شرایط په لاندې ډول دي:')
add(s,'n1',f'1) The equilibrium state can only be reached if the reaction is taking place in{SO} closed vessel wherein substances can neither leave nor enter.',f'1) توازنی حالت صرف اسی صورت میں حاصل ہو سکتی ہے جب تعامل ایک {SO} بند برتن میں ہو رہا ہو جس میں مادے نہ باہر جا سکیں نہ اندر آ سکیں۔',f'1) د تعادل حالت یوازې هغه وخت ترلاسه کېدای شي چې تعامل په یوه {SO} تړلي لوښي کې ترسره شي چې مواد نه ور وتلای شي او نه ور داخلېدای شي.')
add(s,'n2',f'2) Catalyst helps to attain equilibrium earlier but it does not change the positio{SO} of equilibrium.',f'2) اتپریرک توازن جلد حاصل کرنے میں مدد دیتا ہے لیکن توازن کے مقام {SO} کو تبدیل نہیں کرتا۔',f'2) کتلیست د تعادل ژر ترلاسه کولو کې مرسته کوي خو د تعادل موقعیت {SO} نه بدلوي.')
add(s,'n3',f'3) The state of equilibrium is maintained only as long as the reaction condition{SO} such as temperature and pressure etc. do not change.',f'3) توازن کی حالت صرف اسی وقت تک برقرار رہتی ہے جب تک تعامل کے حالات {SO} مثلاً درجہ حرارت اور دباؤ وغیرہ تبدیل نہ ہوں۔',f'3) د تعادل حالت یوازې تر هغه وخته پورې پاتې کېږي چې د تعامل شرایط {SO} لکه تودوخه او فشار او نور ونه بدلېږي.')
add(s,'n4',f'Once the equilibrium composition has been attained no further change{SO} the quantities of the components will occur as long as the system remains un{SO} disturbed, although microscopically, (at molecular level) reactants are converted{SO} products and product molecules are reacting to give the reactants back; both the{SO} forward and reverse reactions taking place at the same rate. Thus, there is n{SO} observable change in the concentration of both reactants and products, this is calle{SO} dynamic equilibrium. An equilibrium state can be recognized by the constancy of{SO} concentration, pressure in the case of gaseous reactants or products, density and colour, etc. of the reaction mixture.',
 f'ایک بار توازنی ترکیب حاصل ہو جانے کے بعد کوئی مزید تبدیلی {SO} اجزاء کی مقداروں میں اس وقت تک نہیں ہوگی جب تک نظام غیر {SO} مضطرب رہتا ہے، اگرچہ خوردبینی طور پر (سالماتی سطح پر) تعامل کنندگان {SO} حاصلات میں تبدیل ہوتے ہیں اور حاصلات کے سالمے تعامل کر کے تعامل کنندگان واپس دیتے ہیں؛ سیدھا اور الٹا دونوں {SO} تعاملات ایک ہی شرح سے ہوتے رہتے ہیں۔ یوں تعامل کنندگان اور حاصلات دونوں کے ارتکاز میں کوئی {SO} قابلِ مشاہدہ تبدیلی نہیں ہوتی، اسے {SO} حرکی توازن کہتے ہیں۔ توازنی حالت کو ارتکاز کی مستقل مزاجی، گیسی تعامل کنندگان یا حاصلات کی صورت میں دباؤ، {SO} کثافت اور رنگ وغیرہ سے پہچانا جا سکتا ہے۔',
 f'کله چې د تعادل جوړښت ترلاسه شي نور بدلون {SO} د اجزاوو په مقدارونو کې به تر هغه پېښ نشي چې سیسټم نه {SO} ګډوډېږي، که څه هم مایکروسکوپي ډول (په مالیکولي کچه) متعاملین {SO} په محصولاتو بدلېږي او د محصول مالیکولونه تعامل کوي چې متعاملین بېرته ورکړي؛ مخکښ او بېرته دواړه {SO} تعاملات په یوې چټکتیا سره پېښېږي. په دې توګه د متعاملینو او محصولاتو دواړو په غلظت کې هېڅ {SO} د لیدلو وړ بدلون نشته، دې ته {SO} دیناميکي تعادل ویل کېږي. د تعادل حالت د غلظت ثابتوالي، د ګازي متعاملینو یا محصولاتو په حالت کې فشار، {SO} کثافت او رنګ او نورو په واسطه پېژندل کېدای شي.')
add(s,'rc-h','Reading Check','مطالعہ کی جانچ','د لوستلو ازموینه',kind='heading')
add(s,'rc1','Define chemical equilibrium.','کیمیائی توازن کی تعریف کریں۔','کيمياوي تعادل تعریف کړئ.',role='question')
head(s,'th','Types of chemical equilibrium','کیمیائی توازن کی اقسام','د کيمياوي تعادل ډولونه')
add(s,'t0','There are two types of chemical equilibrium:','کیمیائی توازن کی دو اقسام ہیں:','د کيمياوي تعادل دوه ډولونه دي:')
add(s,'t1',f'i) Homogeneous Equilibrium: In homogeneous equilibrium all th{SO} components of reaction occur only in one phase. For example, a system{SO} containing only gases or totally miscible liquids e.g.',f'i) ہم جنس توازن: ہم جنس توازن میں تعامل کے تمام {SO} اجزاء صرف ایک فیز میں ہوتے ہیں۔ مثلاً ایک نظام {SO} جس میں صرف گیسیں یا مکمل طور پر قابلِ امتزاج مائعات ہوں، جیسے،',f'i) همجنس تعادل: په همجنس تعادل کې د تعامل ټول {SO} اجزا یوازې په یوه فیز کې وي. د بېلګې په توګه یو سیسټم {SO} چې یوازې ګازونه یا په بشپړ ډول ګډېدونکي مایعات ولري، لکه،')
add(s,'t2',f'ii) Heterogeneous Equilibrium: In heterogeneous equilibrium the reactio{SO} components occur in two or more phases. For example;',f'ii) غیر ہم جنس توازن: غیر ہم جنس توازن میں تعامل {SO} کے اجزاء دو یا زیادہ فیزوں میں ہوتے ہیں۔ مثلاً؛',f'ii) ناهمجنس تعادل: په ناهمجنس تعادل کې د تعامل {SO} اجزا په دوو یا ډېرو فیزونو کې وي. د بېلګې په توګه؛')
head(s,'h712','7.1.2. The law of Mass Action and expression for Equilibrium Constant','7.1.2 قانونِ کمیتِ عمل اور توازنی مستقلہ کا اظہار','7.1.2 د کتلې د عمل قانون او د تعادل ثابت بیان')
add(s,'m1',f'This law was first enunciated by C.M. Guldberg and P. Waage in 1864 tha{SO} helps us to find the relations between the concentrations of reactants and{SO} products at equilibrium in a chemical reaction. It states that "{SO} substance reacts is proportional to its active mass and the rate of{SO} reaction is proportional to the product of the active masses of the{SO} substances". By the term active mass (or activity) we mean the molar{SO} concentration, or number of moles dm⁻³ in a dilute solution. Consider a general{SO} reaction;',
 f'یہ قانون سب سے پہلے سی ایم گلڈبرگ اور پی وائج نے 1864 میں پیش کیا {SO} جو ہمیں کیمیائی تعامل میں توازن پر تعامل کنندگان اور {SO} حاصلات کے ارتکازوں کے درمیان تعلقات معلوم کرنے میں مدد دیتا ہے۔ یہ کہتا ہے کہ "{SO} مادہ جس شرح سے تعامل کرتا ہے وہ اس کی فعال کمیت کے متناسب ہے اور {SO} تعامل کی شرح تعامل کرنے والے مادوں کی فعال کمیتوں کے حاصل ضرب کے متناسب ہے {SO} مادے"۔ فعال کمیت (یا فعالیت) سے ہماری مراد ایک ہلکے محلول میں مولر ارتکاز، یا مولوں کی تعداد dm⁻³ ہے {SO}۔ ایک عمومی {SO} تعامل پر غور کریں؛',
 f'دا قانون لومړی ځل د سي ايم ګولډبرګ او پي واګ په 1864 کې وړاندې کړ {SO} چې موږ سره د کيمياوي تعامل په تعادل کې د متعاملینو او {SO} محصولاتو د غلظتونو ترمنځ اړیکې موندلو کې مرسته کوي. دا وايي چې "{SO} مواد چې په کومې چټکتیا سره تعامل کوي هغه د هغه د فعال کتلې سره متناسب دی او د {SO} تعامل چټکتیا د تعامل کوونکو موادو د فعالو کتلو د حاصل ضرب سره متناسب ده {SO} مواد". د فعالې کتلې (یا فعالیت) له اصطلاح څخه زموږ مطلب په یوه رقیق محلول کې مولر غلظت، یا د مولونو شمېر dm⁻³ دی {SO}. یو عمومي {SO} تعامل ته پام وکړئ؛')
F.p('n0','n1','n2','n3','n4','rc-h','rc1','th','t0','t1')
F.e('hom1',r'\mathrm{N_{2(g)}+O_{2(g)}\rightleftharpoons 2NO_{(g)}}','N₂(g) + O₂(g) ⇌ 2NO(g)')
F.e('hom2',r'\mathrm{CH_3COOH_{(l)}+C_2H_5OH_{(l)}\rightleftharpoons CH_3COOC_2H_{5(l)}+H_2O_{(l)}}','CH₃COOH(l) + C₂H₅OH(l) ⇌ CH₃COOC₂H₅(l) + H₂O(l)')
F.p('t2')
F.e('het',r'\mathrm{CaCO_{3(s)}\rightleftharpoons CaO_{(s)}+CO_{2(g)}}','CaCO₃(s) ⇌ CaO(s) + CO₂(g)')
F.p('h712','m1')
F.done()
s['sourceNote']='Printed folio 212. The right edge is clipped by the page curl on almost every line; clipped endings are marked [scan obscured] and not inferred. The pink italic statement of the law of mass action is faint and its opening and middle words are unreadable, so those fragments are marked [scan obscured]. The Reading Check box is partly cut at the edge. Heading letters of "Types of chemical equilibrium", "Homogeneous Equilibrium", "Heterogeneous Equilibrium" are partly blurred. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping throughout; faint pink italic text in the law-of-mass-action statement is unreadable in places.')
s['vocabulary']={'homogeneous equilibrium':{'ur':'ہم جنس توازن','ps':'همجنس تعادل'},'heterogeneous equilibrium':{'ur':'غیر ہم جنس توازن','ps':'ناهمجنس تعادل'},'active mass':{'ur':'فعال کمیت','ps':'فعاله کتله'},'law of mass action':{'ur':'قانونِ کمیتِ عمل','ps':'د کتلې د عمل قانون'},'catalyst':{'ur':'اتپریرک','ps':'کتلیست'}}
save(s)

# ---------- 218 ----------
s=page(218,'chem11-equilibrium','Equilibrium constant Kc · Equations 7.1 and 7.2','توازنی مستقلہ Kc · مساوات 7.1 اور 7.2','د تعادل ثابت Kc · معادلې 7.1 او 7.2','kc-expression')
F=Flow(s)
F.e('ab',r'\mathrm{A+B}\underset{k_r}{\overset{k_f}{\rightleftharpoons}}\mathrm{C+D}','A + B ⇌ C + D (k_f forward, k_r reverse)')
add(s,'a1','Where A and B are the reactants while C and D are the products. The equilibrium concentrations in mol dm⁻³ of A, B, C and D are represented in square brackets like [A], [B], [C], and [D], respectively. According to the law of mass action the rate of forward reaction is proportional to the product of molar concentrations of A and B.','جہاں A اور B تعامل کنندگان ہیں جبکہ C اور D حاصلات ہیں۔ A، B، C اور D کے توازنی ارتکاز mol dm⁻³ میں بالترتیب چوکور قوسین [A]، [B]، [C] اور [D] میں ظاہر کیے جاتے ہیں۔ قانونِ کمیتِ عمل کے مطابق سیدھے تعامل کی شرح A اور B کے مولر ارتکازوں کے حاصل ضرب کے متناسب ہے۔','چېرته چې A او B متعاملین دي پداسې حال کې چې C او D محصولات دي. د A، B، C او D د تعادل غلظتونه په mol dm⁻³ کې په ترتیب سره په څلور کنجي قوسونو لکه [A]، [B]، [C] او [D] کې ښودل کېږي. د کتلې د عمل د قانون له مخې د مخکښ تعامل چټکتیا د A او B د مولر غلظتونو د حاصل ضرب سره متناسب ده.')
F.p('a1')
F.e('f1',r'\text{Rate of forward reaction}\propto[\mathrm{A}][\mathrm{B}]','Rate of forward reaction ∝ [A][B]')
F.e('f2',r'\text{Rate of forward reaction}=k_f[\mathrm{A}][\mathrm{B}]','Rate of forward reaction = k_f [A][B]')
add(s,'a2','k_f is the proportionality constant known as rate constant for the forward reaction. Since C and D are the reactants for the backward reaction so the rate of reverse reaction is given by','k_f تناسب کا مستقلہ ہے جسے سیدھے تعامل کا شرحی مستقلہ کہا جاتا ہے۔ چونکہ C اور D الٹے تعامل کے لیے تعامل کنندگان ہیں اس لیے الٹے تعامل کی شرح اس طرح دی جاتی ہے','k_f د تناسب ثابت دی چې د مخکښ تعامل د چټکتیا ثابت په نوم یادېږي. ځکه چې C او D د شاتګ تعامل لپاره متعاملین دي نو د بېرته تعامل چټکتیا په دې ډول ورکول کېږي')
F.p('a2')
F.e('r1',r'\text{Rate of reverse reaction}\propto[\mathrm{C}][\mathrm{D}]','Rate of reverse reaction ∝ [C][D]')
F.e('r2',r'\text{Rate of reverse reaction}=k_r[\mathrm{C}][\mathrm{D}]','Rate of reverse reaction = k_r [C][D]')
add(s,'a3','Where, k_r is the rate constant for the backward (or reverse) reaction.','جہاں k_r الٹے (یا واپسی) تعامل کا شرحی مستقلہ ہے۔','چېرته چې k_r د شاتګ (یا بېرته) تعامل د چټکتیا ثابت دی.')
add(s,'a4','At equilibrium,','توازن پر،','په تعادل کې،')
F.p('a3','a4')
F.e('eq0',r'\text{The rate of forward reaction}=\text{The rate of reverse reaction}','The rate of forward reaction = The rate of reverse reaction')
add(s,'a5','Therefore,','اس لیے،','نو،')
F.p('a5')
F.e('eq1',r'k_f[\mathrm{A}][\mathrm{B}]=k_r[\mathrm{C}][\mathrm{D}]','k_f [A][B] = k_r [C][D]')
add(s,'a6','On rearranging the above relation we get,','مندرجہ بالا تعلق کو دوبارہ ترتیب دینے پر ہمیں ملتا ہے،','پورتنۍ اړیکه بیا ترتیبولو سره موږ ترلاسه کوو،')
F.p('a6')
F.e('e71',r'\frac{[\mathrm{C}][\mathrm{D}]}{[\mathrm{A}][\mathrm{B}]}=\frac{k_f}{k_r}=K_c\qquad(7.1)','[C][D] / [A][B] = k_f / k_r = K_c   (7.1)')
add(s,'a7','Where, K_c is the ratio of the rate constants (k_f/k_r). It is known as equilibrium constant of the reaction. K_c of the form as given in Eq.7.1 is defined as the ratio of the product of the molar concentration of the products to that of the reactants.','جہاں K_c شرحی مستقلوں کی نسبت (k_f/k_r) ہے۔ یہ تعامل کا توازنی مستقلہ کہلاتا ہے۔ مساوات 7.1 میں دی گئی شکل کا K_c اس طرح بیان کیا جاتا ہے کہ حاصلات کے مولر ارتکازوں کے حاصل ضرب کی تعامل کنندگان کے مولر ارتکازوں کے حاصل ضرب سے نسبت۔','چېرته چې K_c د چټکتیا ثابتونو نسبت (k_f/k_r) دی. دا د تعامل د تعادل ثابت په نوم یادېږي. د K_c هغه بڼه چې په 7.1 معادله کې ورکړل شوې داسې تعریفېږي چې د محصولاتو د مولر غلظتونو د حاصل ضرب نسبت د متعاملینو د مولر غلظتونو د حاصل ضرب سره.')
add(s,'a8','For a more general reaction of the following type','درج ذیل قسم کے زیادہ عمومی تعامل کے لیے','د لاندې ډول د ډېر عمومي تعامل لپاره')
F.p('a7','a8')
F.e('gen',r'a\mathrm{A}+b\mathrm{B}\rightleftharpoons c\mathrm{C}+d\mathrm{D}','aA + bB ⇌ cC + dD')
add(s,'a9','Where a, b, c, and d represents the number of moles of the species taking part in the chemical reaction. They are called the coefficient of the species (reactants or products) present in the balanced chemical equation. According to the law of mass action, the equilibrium constant expression is;','جہاں a، b، c اور d کیمیائی تعامل میں حصہ لینے والی انواع کے مولوں کی تعداد ظاہر کرتے ہیں۔ انہیں متوازن کیمیائی مساوات میں موجود انواع (تعامل کنندگان یا حاصلات) کے عددی سر (کوایفیشنٹ) کہا جاتا ہے۔ قانونِ کمیتِ عمل کے مطابق توازنی مستقلہ کا اظہار یہ ہے؛','چېرته چې a، b، c او d په کيمياوي تعامل کې برخه اخیستونکو ډولونو د مولونو شمېر ښيي. دوی ته په متوازن کيمياوي معادله کې د شته ډولونو (متعاملین یا محصولات) ضریبونه ویل کېږي. د کتلې د عمل د قانون له مخې د تعادل ثابت بیان دا دی؛')
F.p('a9')
F.e('e72',r'K_c=\frac{[\mathrm{C}]^c[\mathrm{D}]^d}{[\mathrm{A}]^a[\mathrm{B}]^b}\qquad(7.2)','K_c = [C]^c [D]^d / [A]^a [B]^b   (7.2)')
add(s,'a10','Eq. (7.2) is a general form of the mathematical representation of the equilibrium constant which can more appropriately be defined as the ratio of the','مساوات (7.2) توازنی مستقلہ کی ریاضیاتی نمائندگی کی عمومی شکل ہے جسے زیادہ مناسب طور پر اس طرح بیان کیا جا سکتا ہے کہ نسبت','معادله (7.2) د تعادل ثابت د ریاضیاتي استازیتوب عمومي بڼه ده چې ډېر مناسب ډول داسې تعریفېدای شي چې نسبت')
F.p('a10')
F.done()
s['sourceNote']='Printed folio 213. The text is legible. Subscripts on the rate constants (k_f, k_r) are tiny on the scan; they are read as forward and reverse. The sentence at the foot of the page continues on the next page. The pink italic definitions are partly faint but readable. A CamScanner watermark crosses the page.'
s['vocabulary']={'rate constant':{'ur':'شرحی مستقلہ','ps':'د چټکتیا ثابت'},'equilibrium constant':{'ur':'توازنی مستقلہ','ps':'د تعادل ثابت'},'coefficient':{'ur':'عددی سر (کوایفیشنٹ)','ps':'ضریب'}}
save(s)

# ---------- 219 ----------
s=page(219,'chem11-equilibrium','Kc continued · Kp, Kx, Kn · Self-Assessment','Kc جاری · Kp، Kx، Kn · خود جائزہ','Kc دوام · Kp، Kx، Kn · ځان ارزونه','kp-kx-kn')
F=Flow(s)
add(s,'b1',f'product of the molar concentrations of the products to that of the reactants{SO} raised to the power equal to the coefficients of the respective species that occ{SO} in the balanced chemical equation. Thus, in the light of the above discussion the{SO} law of mass action can more appropriately be defined as the rate of any chemical{SO} reaction is proportional to product of the active masses (or activity) of the{SO} reactants, with each reactant raised to a power equal to the coefficients of the{SO} reactants that occurs in the (balanced) chemical equation at a given temperature{SO}. The value of K_c is independent of the initial concentrations of the reactants and{SO} products but changes only with change in temperature. Remember that the{SO} concentrations of reactants and the products appearing in equilibrium constant{SO} expression (Eq.7.2) are the equilibrium concentrations.',
 f'حاصلات کے مولر ارتکازوں کے حاصل ضرب کی نسبت تعامل کنندگان کے ارتکازوں سے {SO} متعلقہ انواع کے عددی سروں کے برابر قوت تک بڑھا کر جو متوازن کیمیائی مساوات میں آتے ہیں {SO}۔ اس طرح مندرجہ بالا بحث کی روشنی میں {SO} قانونِ کمیتِ عمل کو زیادہ مناسب طور پر یوں بیان کیا جا سکتا ہے کہ کسی بھی کیمیائی تعامل کی شرح {SO} تعامل کنندگان کی فعال کمیتوں (یا فعالیت) کے حاصل ضرب کے متناسب ہے، ہر تعامل کنندہ کو اس کے {SO} متوازن کیمیائی مساوات میں آنے والے عددی سر کے برابر قوت تک بڑھا کر، ایک دیے گئے درجہ حرارت پر {SO}۔ K_c کی قیمت تعامل کنندگان اور {SO} حاصلات کے ابتدائی ارتکازوں سے آزاد ہے لیکن صرف درجہ حرارت کی تبدیلی سے بدلتی ہے۔ یاد رکھیں کہ {SO} توازنی مستقلہ کے اظہار (مساوات 7.2) میں آنے والے تعامل کنندگان اور حاصلات کے ارتکاز توازنی ارتکاز ہیں {SO}۔',
 f'د محصولاتو د مولر غلظتونو د حاصل ضرب نسبت د متعاملینو سره {SO} د اړوندو ډولونو د ضریبونو په اندازې توان ته پورته شوي چې په متوازن کيمياوي معادله کې راځي {SO}. په دې توګه د پورتنۍ بحث په رڼا کې {SO} د کتلې د عمل قانون ډېر مناسب ډول داسې تعریفېدای شي چې د هر کيمياوي تعامل چټکتیا {SO} د متعاملینو د فعالو کتلو (یا فعالیت) د حاصل ضرب سره متناسبه ده، هر متعامل د خپل {SO} ضریب په اندازې توان ته پورته شوی چې په متوازن کيمياوي معادله کې راځي، په یوه ورکړل شوې تودوخه کې {SO}. د K_c ارزښت د متعاملینو او {SO} محصولاتو له لومړنیو غلظتونو څخه خپلواک دی خو یوازې د تودوخې په بدلون سره بدلېږي. په یاد ولرئ چې {SO} د تعادل ثابت په بیان (معادله 7.2) کې راتلونکي د متعاملینو او محصولاتو غلظتونه د تعادل غلظتونه دي {SO}.')
add(s,'b2',f'For a gaseous equilibrium, it is some times more convenient to expres{SO} the concentration of gases in terms of their partial pressures at any give{SO} temperature. Let P_A, P_B, P_C, and P_D are the partial pressures of the gaseous species{SO} then the equilibrium constant K_p may be expressed as;',f'گیسی توازن کے لیے، کبھی کبھی گیسوں کے ارتکاز کو ان کے جزوی دباؤ کے لحاظ سے {SO} ظاہر کرنا زیادہ آسان ہوتا ہے کسی دیے گئے {SO} درجہ حرارت پر۔ فرض کریں P_A، P_B، P_C اور P_D گیسی انواع کے جزوی دباؤ ہیں {SO} تو توازنی مستقلہ K_p اس طرح ظاہر کیا جا سکتا ہے؛',f'د ګازي تعادل لپاره، ځینې وخت د ګازونو غلظت د هغوی د جزوي فشارونو په اړه {SO} ښودل ډېر اسانه وي په هر ورکړل شوې {SO} تودوخه کې. فرض کړئ P_A، P_B، P_C او P_D د ګازي ډولونو جزوي فشارونه دي {SO} نو د تعادل ثابت K_p داسې ښودل کېدای شي؛')
add(s,'b3',f'If the concentrations are expressed in terms of mole fractions, then the{SO} equilibrium constant K_x can be represented as;',f'اگر ارتکاز کو مول اجزاء (مول جزو) کے لحاظ سے ظاہر کیا جائے تو {SO} توازنی مستقلہ K_x اس طرح ظاہر کیا جا سکتا ہے؛',f'که غلظتونه د مول برخو په اړه وښودل شي نو {SO} د تعادل ثابت K_x داسې ښودل کېدای شي؛')
add(s,'b4',f'Similarly, in terms of number of moles, the equilibrium constant K_n is written as{SO}',f'اسی طرح، مولوں کی تعداد کے لحاظ سے توازنی مستقلہ K_n اس طرح لکھا جاتا ہے {SO}',f'همدارنګه، د مولونو د شمېر په اړه د تعادل ثابت K_n داسې لیکل کېږي {SO}')
add(s,'b5',f'Here it should be mentioned that how to recognize that equilibrium has{SO} been reached. For this purpose the concentration of any of the reactant or{SO} product species is monitored, at different time intervals, by analysing them using{SO} any suitable physical or chemical method of analysis. When the concentration of{SO} the chosen species becomes constant, after the elapsed interval, it is an indication of{SO} the fact that the equilibrium state has been reached.',f'یہاں یہ بتانا ضروری ہے کہ کیسے پہچانا جائے کہ توازن حاصل ہو گیا ہے {SO}۔ اس مقصد کے لیے تعامل کنندگان یا {SO} حاصلات میں سے کسی ایک نوع کے ارتکاز کی مختلف وقفوں پر نگرانی کی جاتی ہے، انہیں کسی بھی {SO} مناسب طبعی یا کیمیائی تجزیاتی طریقے سے جانچ کر۔ جب منتخب نوع کا ارتکاز {SO} گزرے ہوئے وقفے کے بعد مستقل ہو جاتا ہے تو یہ اس بات کی علامت ہے {SO} کہ توازنی حالت حاصل ہو گئی ہے۔',f'دلته باید یادونه وشي چې څنګه وپېژندل شي چې تعادل ترلاسه شوی {SO}. د دې موخې لپاره د متعاملینو یا {SO} محصولاتو د هر یوه ډول غلظت په بېلابېلو وختي وقفو کې څارل کېږي، د هغوی په هر مناسب فزیکي یا کيمياوي تحلیلي طریقه سره {SO}. کله چې د ټاکل شوي ډول غلظت {SO} د تېر شوي وقفې وروسته ثابت شي نو دا د دې نښه ده چې {SO} د تعادل حالت ترلاسه شوی.')
head(s,'sa','Self-Assessment','خود جائزہ','ځان ارزونه')
add(s,'sa1','Define forward and backward reactions with examples.','سیدھے اور الٹے تعاملات کی مثالوں کے ساتھ تعریف کریں۔','مخکښ او شاتګ تعاملات په بېلګو سره تعریف کړئ.',role='question')
add(s,'sa2','Expalin law of mass action with an example.','قانونِ کمیتِ عمل کی ایک مثال کے ساتھ وضاحت کریں۔','د کتلې د عمل قانون په یوې بېلګې سره تشریح کړئ.',role='question')
add(s,'sa3','Differentiate between homogeneous and heterogeneous equilibrium.','ہم جنس اور غیر ہم جنس توازن میں فرق کریں۔','د همجنس او ناهمجنس تعادل ترمنځ توپیر وکړئ.',role='question')
F.p('b1','b2')
F.e('e73',r'K_p=\frac{(P_C)^c}{(P_A)^a}\times\frac{(P_D)^d}{(P_B)^b}\qquad(7.3)','K_p = (P_C)^c / (P_A)^a × (P_D)^d / (P_B)^b   (7.3)')
F.p('b3')
F.e('kx',r'K_x=\frac{(X_C)^c(X_D)^d}{(X_A)^a(X_B)^b}','K_x = (X_C)^c (X_D)^d / (X_A)^a (X_B)^b')
F.p('b4')
F.e('kn',r'K_n=\frac{(n_C)^c(n_D)^d}{(n_A)^a(n_B)^b}','K_n = (n_C)^c (n_D)^d / (n_A)^a (n_B)^b')
F.p('b5','sa','sa1','sa2','sa3')
F.done()
s['sourceNote']='Printed folio 214. This page continues the sentence from the previous page. The right edge is clipped by the page curl on most lines; clipped endings are marked [scan obscured] and not inferred. "Expalin" in the second Self-Assessment item is a misprint on the source ("Explain") and is retained as printed in the English line. Subscripts in K_x/K_n numerators and denominators are small but legible. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping throughout; the first line is partly cut in the italic definition.')
s['vocabulary']={'partial pressure':{'ur':'جزوی دباؤ','ps':'جزوي فشار'},'mole fraction':{'ur':'مول جزو','ps':'مول برخه'}}
save(s)

# ---------- 220 ----------
s=page(220,'chem11-equilibrium','Example 7.1 · Practice Problem 7.1 · 7.1.3 Relationship between Kc, Kp, Kx, Kn','مثال 7.1 · مشقی مسئلہ 7.1 · 7.1.3 Kc، Kp، Kx، Kn کا باہمی تعلق','بېلګه 7.1 · د تمرین ستونزه 7.1 · 7.1.3 د Kc، Kp، Kx، Kn تر منځ اړیکه','example-71')
F=Flow(s)
head(s,'ex','Example 7.1','مثال 7.1','بېلګه 7.1')
add(s,'e1','An equilibrium mixture is found to contain 7g of N₂, 0.3g of H₂ and 1.53g of NH₃ per dm³ at 300°C. Find K_c for the reaction.','ایک توازنی آمیزے میں 300°C پر فی dm³ 7g N₂، 0.3g H₂ اور 1.53g NH₃ پائے گئے۔ تعامل کے لیے K_c معلوم کریں۔','یو د تعادل مخلوط کې په 300°C کې په هر dm³ کې 7g N₂، 0.3g H₂ او 1.53g NH₃ وموندل شول. د تعامل لپاره K_c ومومئ.')
head(s,'sol','Solution','حل','حل')
add(s,'pp-h','Practice Problem 7.1','مشقی مسئلہ 7.1','د تمرین ستونزه 7.1',kind='heading')
add(s,'pp1','Nitrogen and hydrogen are placed in an empty 5.00 dm³ container at 500°C. When equilibrium is established, 3.01 mol of N₂, 2.10 mol of H₂, and 0.565 mol of NH₃ are present. Find the K_c for the following reaction at 500°C.','نائٹروجن اور ہائیڈروجن کو 500°C پر ایک خالی 5.00 dm³ کے برتن میں رکھا جاتا ہے۔ جب توازن قائم ہو جاتا ہے تو 3.01 mol N₂، 2.10 mol H₂ اور 0.565 mol NH₃ موجود ہوتے ہیں۔ 500°C پر درج ذیل تعامل کے لیے K_c معلوم کریں۔','نایتروجن او هایدروجن په 500°C کې په یوه تش 5.00 dm³ لوښي کې ایښودل کېږي. کله چې تعادل رامنځته شي، 3.01 mol N₂، 2.10 mol H₂ او 0.565 mol NH₃ شتون لري. په 500°C کې د لاندې تعامل لپاره K_c ومومئ.')
head(s,'h713','7.1.3. Relationship between Equilibrium Constants (K_c, K_p, K_x, K_n)','7.1.3 توازنی مستقلوں (K_c، K_p، K_x، K_n) کے درمیان تعلق','7.1.3 د تعادل ثابتونو (K_c، K_p، K_x، K_n) ترمنځ اړیکه')
head(s,'ih','i) Relation between K_p and K_c','i) K_p اور K_c کے درمیان تعلق','i) د K_p او K_c ترمنځ اړیکه')
add(s,'g1','Consider a general reaction','ایک عمومی تعامل پر غور کریں','یو عمومي تعامل ته پام وکړئ')
add(s,'g2','For an ideal gaseous system, the equilibrium constant expression is written as,','ایک مثالی گیسی نظام کے لیے توازنی مستقلہ کا اظہار اس طرح لکھا جاتا ہے،','د یو ایډیال ګازي سیسټم لپاره د تعادل ثابت بیان داسې لیکل کېږي،')
add(s,'g3','Where P represents the partial pressure of the individual gas components present in the equilibrium state.','جہاں P توازنی حالت میں موجود انفرادی گیسی اجزاء کا جزوی دباؤ ظاہر کرتا ہے۔','چېرته چې P د تعادل په حالت کې د شته انفرادي ګازي اجزاوو جزوي فشار ښيي.')
add(s,'g4',"For 'n' number of moles the ideal gas equation is given as;","'n' مولوں کی تعداد کے لیے مثالی گیس کی مساوات اس طرح دی جاتی ہے؛","د 'n' مولونو د شمېر لپاره د ایډیال ګاز معادله داسې ورکول کېږي؛")
rx=r'\mathrm{N_{2(g)}+3H_{2(g)}\rightleftharpoons 2NH_{3(g)}}'
rxt='N₂(g) + 3H₂(g) ⇌ 2NH₃(g)'
F.p('ex','e1')
F.e('rx',rx,rxt)
F.p('sol')
F.e('n2',r'[\mathrm{N_2}]=\text{mol dm}^{-3}\text{ of N}_2=\frac{7\ \mathrm{g}}{28\ \mathrm{g\,mol^{-1}}}=0.25\ \mathrm{mol}','[N₂] = mol dm⁻³ of N₂ = 7 g / 28 g mol⁻¹ = 0.25 mol')
F.e('h2',r'[\mathrm{H_2}]=0.15\ \mathrm{mol}=\frac{0.3\ \mathrm{g}}{2\ \mathrm{g\,mol^{-1}}}=0.15\ \mathrm{mol}','[H₂] = 0.15 mol = 0.3 g / 2 g mol⁻¹ = 0.15 mol')
F.e('nh3',r'[\mathrm{NH_3}]=\frac{1.53\ \mathrm{g}}{17\ \mathrm{g\,mol^{-1}}}=0.09\ \mathrm{mol}','[NH₃] = 1.53 g / 17 g mol⁻¹ = 0.09 mol')
F.e('kc',r'K_c=\frac{[\mathrm{NH_3}]^2}{[\mathrm{N_2}][\mathrm{H_2}]^3}','K_c = [NH₃]² / [N₂][H₂]³')
F.e('kcv',r'K_c=\frac{[0.09]^2}{[0.25][0.15]^3}=\frac{9.6\ (\mathrm{dm^3})^2}{\mathrm{mol}^2}\ \text{or}\ 9.6\ \mathrm{M^{-2}}','K_c = [0.09]² / ([0.25][0.15]³) = 9.6 (dm³)² / mol² or 9.6 M⁻²')
F.p('pp-h','pp1')
F.e('pprx',rx,rxt)
F.p('h713','ih','g1')
F.e('gen',r'a\mathrm{A}+b\mathrm{B}\rightleftharpoons c\mathrm{C}+d\mathrm{D}','aA + bB ⇌ cC + dD')
F.p('g2')
F.e('kp',r'K_p=\frac{(P_C)^c}{(P_A)^a}\times\frac{(P_D)^d}{(P_B)^b}','K_p = (P_C)^c / (P_A)^a × (P_D)^d / (P_B)^b')
F.p('g3','g4')
F.e('pv',r'PV=nRT','PV = nRT')
F.e('pnv',r'P=(n/V)RT','P = (n/V)RT')
F.done()
s['sourceNote']='Printed folio 215. The printed Kc line shows 9.6 (dm³)²/mol² or 9.6 M⁻² and the value is confirmed by the arithmetic (0.09²/(0.25×0.15³)). The Practice Problem has no answer printed. The lower area of the page and the footer are partly shadowed. A CamScanner watermark crosses the page.'
s['vocabulary']={'ideal gas':{'ur':'مثالی گیس','ps':'ایډیال ګاز'},'partial pressure':{'ur':'جزوی دباؤ','ps':'جزوي فشار'}}
save(s)
