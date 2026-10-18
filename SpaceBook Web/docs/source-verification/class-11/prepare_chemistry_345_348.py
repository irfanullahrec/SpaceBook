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
TC='chem11-thermochemistry'
def mk(n,title,ur,ps,sid): return page(n,TC,title,ur,ps,sid)

# ---------- 345 ----------
s=mk(345,'Enthalpy H = E + PV · ΔH = qp · Example 11.2','انتھالپی H = E + PV · ΔH = qp · مثال 11.2','انتالپي H = E + PV · ΔH = qp · بېلګه 11.2','enthalpy-example112')
F=Flow(s)
add(s,'a1',f'pressure, thus, the equation takes the form, considering the sign convention, as ΔE=q−PΔV. On rearranging this equation we get','دباؤ، اس طرح مساوات علامتی روایت کو مدنظر رکھتے ہوئے ΔE=q−PΔV کی شکل اختیار کرتی ہے۔ اس مساوات کو دوبارہ ترتیب دینے پر ہمیں ملتا ہے','فشار، په دې توګه معادله د نښو کنوانسیون په پام کې نیولو سره ΔE=q−PΔV بڼه اخلي. دا معادله بیا ترتیبولو سره موږ ترلاسه کوو')
add(s,'a2','Here q_p stands for heat supplied at constant pressure condition. Now we introduce a new thermodynamic function of a system called enthalpy (H), or heat content of the system which is defined by the equation','یہاں q_p مستقل دباؤ کی حالت میں فراہم کی گئی حرارت کو ظاہر کرتا ہے۔ اب ہم نظام کا ایک نیا تھرموڈائنامک تفاعل متعارف کراتے ہیں جسے انتھالپی (H) یا نظام کا حرارتی مواد کہتے ہیں جو مساوات سے متعین ہوتا ہے','دلته q_p په ثابت فشار حالت کې رسول شوې تودوخه ښيي. اوس موږ د یو سیسټم نوې ترموډینامیکي تابع معرفي کوو چې انتالپي (H) یا د سیسټم تودوخیز مواد بلل کېږي چې د معادلې په واسطه ټاکل کېږي')
add(s,'a3','Thus, the total heat content of a system, \'H\', at constant pressure is equal to the internal energy plus PV work','اس طرح مستقل دباؤ پر نظام کا کل حرارتی مواد \'H\' اندرونی توانائی جمع PV کام کے برابر ہوتا ہے','په دې توګه په ثابت فشار کې د یو سیسټم ټول تودوخیز مواد \'H\' له داخلي انرژۍ جمع PV کار سره مساوي دی')
add(s,'a4',"Change in enthalpy, 'ΔH' at constant pressure is given by",'مستقل دباؤ پر انتھالپی میں تبدیلی \'ΔH\' اس طرح دی جاتی ہے','په ثابت فشار کې د انتالپي بدلون \'ΔH\' په لاندې ډول ورکول کېږي')
add(s,'a5','Comparing Eq.(11.4a) and (11.7) we can easily demonstrate that','مساوات (11.4a) اور (11.7) کا موازنہ کر کے ہم آسانی سے ثابت کر سکتے ہیں کہ','د (11.4a) او (11.7) معادلو په پرتله کولو سره موږ په اسانۍ ښودلای شو چې')
add(s,'a6','Thus, from Eq. (11.8) heat supplied at constant pressure is equal to change in enthalpy.','اس طرح مساوات (11.8) سے مستقل دباؤ پر فراہم کی گئی حرارت انتھالپی میں تبدیلی کے برابر ہے۔','په دې توګه له معادلې (11.8) څخه په ثابت فشار کې رسول شوې تودوخه د انتالپي له بدلون سره مساوي ده.')
add(s,'a7','Thus, we have proved that heat supplied at constant volume, q_v=ΔE and heat supplied at constant pressure, q_p=ΔH','اس طرح ہم نے ثابت کر دیا کہ مستقل حجم پر فراہم کی گئی حرارت q_v=ΔE اور مستقل دباؤ پر فراہم کی گئی حرارت q_p=ΔH ہے','په دې توګه موږ ثابته کړه چې په ثابت حجم کې رسول شوې تودوخه q_v=ΔE او په ثابت فشار کې رسول شوې تودوخه q_p=ΔH ده')
add(s,'a8',f'Hence, heat evolved or absorbed at constant pressure during a process or a reaction is equal to change in the enthalpy of the system. Since, ΔH is the heat of the reaction, it can be calculated theoretically and measured experimentally. Its units are expressed in energy units, i.e. kJ or Joules.{SO}',f'لہٰذا کسی عمل یا تعامل کے دوران مستقل دباؤ پر خارج یا جذب ہونے والی حرارت نظام کی انتھالپی میں تبدیلی کے برابر ہوتی ہے۔ چونکہ ΔH تعامل کی حرارت ہے اس لیے اسے نظری طور پر حساب کیا اور تجرباتی طور پر ناپا جا سکتا ہے۔ اس کی اکائیاں توانائی کی اکائیوں میں ظاہر کی جاتی ہیں یعنی kJ یا جول {SO}۔',f'نو په ثابت فشار کې د یوې پروسې یا تعامل پر مهال خوشې یا جذب شوې تودوخه د سیسټم د انتالپي له بدلون سره مساوي ده. ځکه چې ΔH د تعامل تودوخه ده نو دا په نظري ډول محاسبه او په تجربوي ډول اندازه کېدای شي. واحدونه یې د انرژۍ په واحدونو کې ښودل کېږي یعنې kJ یا جول {SO}.')
add(s,'a9','From the above discussion it is concluded that.','مندرجہ بالا بحث سے یہ نتیجہ اخذ ہوتا ہے کہ۔','له پورتنۍ بحث څخه دا پایله اخیستل کېږي چې.')
add(s,'c1','1. Since E, P, and V are state functions so according to Eq. (11.6), enthalpy is also a state function.','1۔ چونکہ E، P اور V حالت کے تفاعل ہیں اس لیے مساوات (11.6) کے مطابق انتھالپی بھی حالت کا تفاعل ہے۔','1. ځکه چې E، P او V د حالت تابع دي نو د معادلې (11.6) له مخې انتالپي هم د حالت تابع ده.')
add(s,'c2','2. ΔH is positive when the heat is absorbed and it is negative when the heat is released by the system.','2۔ ΔH مثبت ہوتا ہے جب حرارت جذب ہو اور منفی ہوتا ہے جب نظام سے حرارت خارج ہو۔','2. ΔH مثبت وي کله چې تودوخه جذب شي او منفي وي کله چې تودوخه د سیسټم لخوا خوشې شي.')
add(s,'c3','3. Processes involving solids and liquids have their ΔH = ΔE, since the change in volume (ΔV) is very small and closed to zero hence the term PΔV in Eq. (11.7) can be neglected.','3۔ ٹھوس اور مائعات پر مشتمل عملوں کا ΔH = ΔE ہوتا ہے، کیونکہ حجم میں تبدیلی (ΔV) بہت چھوٹی اور صفر کے قریب ہوتی ہے اس لیے مساوات (11.7) میں PΔV کا جزو نظر انداز کیا جا سکتا ہے۔','3. هغه پروسې چې جامدات او مایعات شاملوي ΔH = ΔE لري، ځکه چې د حجم بدلون (ΔV) ډېر کوچنی او صفر ته نژدې دی نو په معادله (11.7) کې د PΔV اصطلاح له پامه غورځول کېدای شي.')
add(s,'e','Example 11.2:','مثال 11.2:','بېلګه 11.2:',kind='heading')
add(s,'q','When 1 mole of ice melts at 0°C and constant pressure of 1 atmosphere, 6025 J of heat is absorbed by the system. The molar volumes of ice and water are 0.020 and 0.018 dm³, respectively. Calculate ΔH and ΔE.','جب 1 مول برف 0°C اور 1 ماحول کے مستقل دباؤ پر پگھلتی ہے تو نظام 6025 J حرارت جذب کرتا ہے۔ برف اور پانی کے مولر حجم بالترتیب 0.020 اور 0.018 dm³ ہیں۔ ΔH اور ΔE معلوم کریں۔','کله چې 1 مول یخ په 0°C او د 1 اتموسفیر ثابت فشار کې ویلې شي نو سیسټم 6025 J تودوخه جذبوي. د یخ او اوبو مولر حجمونه په ترتیب سره 0.020 او 0.018 dm³ دي. ΔH او ΔE محاسبه کړئ.')
F.p('a1')
F.e('e114a',r'q_p=\Delta E+P\Delta V\qquad(11.4a)','q_p = ΔE + PΔV   (11.4a)')
F.p('a2')
F.e('e116',r'H=E+PV\qquad(11.6)','H = E + PV   (11.6)')
F.p('a3','a4')
F.e('e117',r'\Delta H=\Delta E+P\Delta V\qquad(11.7)','ΔH = ΔE + PΔV   (11.7)')
F.p('a5')
F.e('e118',r'q_p=\Delta H\qquad(11.8)','q_p = ΔH   (11.8)')
F.p('a6','a7','a8','a9','c1','c2','c3','e','q')
F.done()
s['sourceNote']='Printed folio 340. The scan is skewed and the right edge is slightly clipped on the lower paragraphs; the sentences are legible. The first line completes the sentence from the previous page. The solution to Example 11.2 is on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='First line completes the previous sentence; right edge slightly clipped.')
s['vocabulary']={'enthalpy':{'ur':'انتھالپی','ps':'انتالپي'}}
save(s)

# ---------- 346 ----------
s=mk(346,'Solution of Example 11.2 · Standard Enthalpy Change ΔH°','مثال 11.2 کا حل · معیاری انتھالپی تبدیلی ΔH°','د بېلګې 11.2 حل · معیاري د انتالپي بدلون ΔH°','solution112-standard')
F=Flow(s)
add(s,'s','Solution:','حل:','حل:',kind='heading')
add(s,'a2','Since 1dm³·atm = 101.25 J','چونکہ 1dm³·atm = 101.25 J','ځکه چې 1dm³·atm = 101.25 J')
add(s,'a3','So','لہٰذا','نو')
add(s,'b1','b. ΔH = ΔE + PΔV','ب۔ ΔH = ΔE + PΔV','ب. ΔH = ΔE + PΔV')
add(s,'h','Standard Enthalpy Change, ΔH°','معیاری انتھالپی تبدیلی ΔH°','معیاري د انتالپي بدلون ΔH°',kind='heading')
add(s,'c1',f'The change in enthalpy measured at room temperature (298K) and one atmospheric pressure when the reactant and products are in their standard (natural) states is called the standard enthalpy change.',f'کمرے کے درجہ حرارت (298K) اور ایک ماحولیاتی دباؤ پر ناپی گئی انتھالپی میں تبدیلی جب تعامل کنندگان اور حاصلات اپنی معیاری (قدرتی) حالتوں میں ہوں معیاری انتھالپی تبدیلی کہلاتی ہے {SO}۔',f'د خونې په تودوخه (298K) او یو اتموسفیري فشار کې اندازه شوی د انتالپي بدلون کله چې متعاملین او محصولات په خپلو معیاري (طبیعي) حالتونو کې وي معیاري د انتالپي بدلون بلل کېږي {SO}.')
add(s,'c2',f'It should be mentioned that there is no way to measure absolute value of enthalpy of a substance; only values relative to an arbitrary reference can be determined. Furthermore, it is important to state the conditions under which a reaction is performed. Thus, arbitrary reference point is the set of conditions of temperature and pressure, for thermochemical measurements, are 298 K (25°C) and one atmosphere respectively. Any enthalpy change measured under these conditions is described as a standard enthalpy change and given the symbol ΔH° or ΔH°₂₉₈. This implies that all the substances involved in the reaction are in their normal and natural state at 298K and 1 atmosphere. This state is called the standard state. Thus, ΔH°₂₉₈ for reaction corresponds to gaseous hydrogen, oxygen and liquid water (not steam) which are their most stable and normal state or standard states.{SO}',f'یہ بتانا ضروری ہے کہ کسی مادے کی انتھالپی کی مطلق قیمت ناپنے کا کوئی طریقہ نہیں؛ صرف کسی من مانے حوالے کی نسبت سے قیمتیں متعین کی جا سکتی ہیں۔ مزید یہ کہ ان حالات کا بیان کرنا اہم ہے جن میں تعامل کیا جاتا ہے۔ اس طرح من مانا حوالہ نقطہ درجہ حرارت اور دباؤ کے حالات کا مجموعہ ہے، حرارتی کیمیائی پیمائشوں کے لیے یہ بالترتیب 298 K (25°C) اور ایک ماحولیاتی دباؤ ہیں۔ ان حالات میں ناپی گئی کوئی بھی انتھالپی تبدیلی معیاری انتھالپی تبدیلی کہلاتی ہے اور اسے علامت ΔH° یا ΔH°₂₉₈ دی جاتی ہے۔ اس کا مطلب ہے کہ تعامل میں شامل تمام مادے 298K اور 1 ماحولیاتی دباؤ پر اپنی عام اور قدرتی حالت میں ہیں۔ اس حالت کو معیاری حالت کہتے ہیں۔ اس طرح تعامل کے لیے ΔH°₂₉₈ گیسی ہائیڈروجن، آکسیجن اور مائع پانی (بھاپ نہیں) سے مطابقت رکھتی ہے جو ان کی سب سے مستحکم اور عام حالت یا معیاری حالتیں ہیں {SO}۔',f'دا باید یاده شي چې د یوې مادې د انتالپي مطلق ارزښت د اندازه کولو هېڅ لاره نشته؛ یوازې د یو خپلسري حوالې په پرتله ارزښتونه ټاکل کېدای شي. سربیره پر دې دا مهم دي چې هغه شرایط بیان شي چې په هغو کې تعامل ترسره کېږي. په دې توګه خپلسري حوالې ټکی د تودوخې او فشار د شرایطو ټولګه ده، د ترموکيمياوي اندازو لپاره دا په ترتیب سره 298 K (25°C) او یو اتموسفیر دي. په دې شرایطو کې اندازه شوی هر د انتالپي بدلون معیاري د انتالپي بدلون بلل کېږي او ΔH° یا ΔH°₂₉₈ نښه ورکول کېږي. دا معنا لري چې په تعامل کې ټول شامل مواد په 298K او 1 اتموسفیر کې په خپل عادي او طبیعي حالت کې دي. دې حالت ته معیاري حالت ویل کېږي. په دې توګه د تعامل لپاره ΔH°₂₉₈ له ګازي هایدروجن، اکسیجن او مایع اوبو (نه بخار) سره سمون لري چې د هغوی تر ټولو ټینګ او عادي حالت یا معیاري حالتونه دي {SO}.')
F.p('s')
F.e('x1',r'\Delta H=q_p=6025\ \mathrm{J}','ΔH = q_p = 6025 J')
F.e('x2','P=1\ \mathrm{atm}','P = 1 atm')
F.e('x3',r'P\Delta V=P\times(V_2-V_1)','PΔV = P × (V₂ − V₁)')
F.e('x4',r'=1\ \mathrm{atm}\times(0.018\ \mathrm{dm^3}-0.020\ \mathrm{dm^3})','= 1 atm × (0.018 dm³ − 0.020 dm³)')
F.e('x5',r'P\Delta V=-0.002\ \mathrm{dm^3\,atm}','PΔV = −0.002 dm³ atm')
F.p('a2','a3')
F.e('x6',r'P\Delta V=-0.002\ \mathrm{dm^3\,atm}\times101.25\ \mathrm{J\,dm^{-3}\,atm^{-1}}=-0.2025\ \mathrm{J}','PΔV = −0.002 dm³ atm × 101.25 J dm⁻³ atm⁻¹ = −0.2025 J')
F.p('b1')
F.e('y1',r'\Delta E=\Delta H-P\Delta V','ΔE = ΔH − PΔV')
F.e('y2',r'=6025\ \mathrm{J}-(-0.2025\ \mathrm{J})','= 6025 J − (−0.2025 J)')
F.e('y3',r'\Delta E=6025.20\ \mathrm{J}','ΔE = 6025.20 J')
F.p('h','c1','c2')
F.e('z',r'2\mathrm{H_{2(g)}+O_{2(g)}\rightarrow2H_2O_{(l)}}','2H₂(g) + O₂(g) → 2H₂O(l)')
F.done()
s['sourceNote']='Printed folio 341. The left edge is clipped by the page curl (first letters of the paragraph lines are cut) and the Solution/Since/So labels are partly cut. The printed conversion line reads "1 dm³ = atm = 101.25 J" (the "·" is missing; read as 1 dm³·atm = 101.25 J). The standard-enthalpy heading carries a leading marker (i) that is cut. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Left-edge letters cut; "1dm³=atm" printed for 1 dm³·atm.')
s['vocabulary']={'standard state':{'ur':'معیاری حالت','ps':'معیاري حالت'}}
save(s)

# ---------- 347 ----------
s=mk(347,'(ii) Standard Enthalpy of Formation · Table 11.2 · (iii) Standard Enthalpy of Reaction','(ii) تشکیل کی معیاری انتھالپی · جدول 11.2 · (iii) تعامل کی معیاری انتھالپی','(ii) د جوړېدو معیاري انتالپي · جدول 11.2 · (iii) د تعامل معیاري انتالپي','table112')
F=Flow(s)
add(s,'h2','(ii) The standard enthalpy of formation (ΔH°f)','(ii) تشکیل کی معیاری انتھالپی (ΔH°f)','(ii) د جوړېدو معیاري انتالپي (ΔH°f)',kind='heading')
add(s,'a1',f'It is defined as the heat change that results when 1 mole of a compound is formed from its elements where all the reactants and products are at their standard state i.e. 298K and 1 atm. pressure. The standard enthalpy of formation of all the elements in their most stable form is arbitrarily taken as zero. For example molecular oxygen (O₂) is more stable than its allotropic form ozone (O₃) at 1 atm and 25°C. A list of standard enthalpies of formation for some elements and compounds is given in Table 11.2. These values are helpful to calculate standard enthalpies of reactions (ΔH°reaction).{SO}',f'اس کی تعریف اس حرارتی تبدیلی کے طور پر کی جاتی ہے جو اس وقت ہوتی ہے جب کسی مرکب کا 1 مول اس کے عناصر سے بنے جہاں تمام تعامل کنندگان اور حاصلات اپنی معیاری حالت یعنی 298K اور 1 atm دباؤ پر ہوں۔ تمام عناصر کی ان کی سب سے مستحکم شکل میں تشکیل کی معیاری انتھالپی من مانی طور پر صفر لی جاتی ہے۔ مثلاً سالماتی آکسیجن (O₂) 1 atm اور 25°C پر اپنی دوسرے روپ اوزون (O₃) سے زیادہ مستحکم ہے۔ کچھ عناصر اور مرکبات کے لیے تشکیل کی معیاری انتھالپیوں کی فہرست جدول 11.2 میں دی گئی ہے۔ یہ قیمتیں تعاملات کی معیاری انتھالپیاں (ΔH°reaction) معلوم کرنے میں مددگار ہیں {SO}۔',f'دا د هغې تودوخې بدلون په توګه تعریفېږي چې کله د یو مرکب 1 مول له خپلو عناصرو څخه جوړ شي چېرته چې ټول متعاملین او محصولات په خپل معیاري حالت یعنې 298K او 1 atm فشار کې وي. د ټولو عناصرو د جوړېدو معیاري انتالپي چې په خپل تر ټولو ټینګه بڼه کې وي په خپلسري ډول صفر ګڼل کېږي. د بېلګې په توګه مالیکولي اکسیجن (O₂) د 1 atm او 25°C کې د خپلې المورفي بڼې اوزون (O₃) څخه ډېر ټینګ دی. د ځینو عناصرو او مرکباتو لپاره د جوړېدو د معیاري انتالپیو لیست په 11.2 جدول کې ورکړل شوی. دا ارزښتونه د تعاملاتو د معیاري انتالپیو (ΔH°reaction) د محاسبې لپاره ګټور دي {SO}.')
add(s,'a2',f'The standard heat of formation of CO₂ is −393.51 kJ mol⁻¹ and that of SO₂ is −296.83 kJ mol⁻¹ as shown below.{SO}',f'CO₂ کی تشکیل کی معیاری حرارت −393.51 kJ mol⁻¹ اور SO₂ کی −296.83 kJ mol⁻¹ ہے جیسا کہ نیچے دکھایا گیا ہے {SO}۔',f'د CO₂ د جوړېدو معیاري تودوخه −393.51 kJ mol⁻¹ او د SO₂ −296.83 kJ mol⁻¹ ده لکه څنګه چې لاندې ښودل شوي {SO}.')
rows=[('All elements in their standard states','0.00','CaC₂(s)','−62.5'),('C(s) (graphite)','0.00','CS₂(l)','+89.7'),('C(s) (diamond)','+1.90','HCl(g)','−92.31'),('P(s) (white)','0.00','NaCl(s)','−411.00'),('P(s) (red)','−17.60','HBr(g)','−36.40'),('H₂O(l)','−285.84','HI(g)','+26.48'),('SO₂(g)','−296.83','NH₃(g)','−46.11'),('CO(g)','−110.53','H₂S(g)','−20.63'),('CO₂(g)','−393.51','CH₄(g)','−74.81'),('Fe₂O₃(s)','−824.2','C₂H₂(g)','+226.73'),('Fe₃O₄(s)','−1118.4','H₂SO₄(l)','−813.99'),('CaO(s)','−635.5','HNO₃(l)','−174.10')]
s['tables']=[table('Table 11.2: Standard Enthalpies of Formation at 298 K','جدول 11.2: 298 K پر تشکیل کی معیاری انتھالپیاں','جدول 11.2: په 298 K کې د جوړېدو معیاري انتالپۍ',[c('Substance','مادہ','مواد'),c('ΔH°f'),c('Substance','مادہ','مواد'),c('ΔH°f')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in rows])]
s['tables'][0]['sourceGap']=dict(note='The table caption is clipped at the right ("…at 298 K"). Units (kJ mol⁻¹) are not printed in the header. CH₄(g) is printed as −74.81 on the scan (as printed). Row alignment follows the printed order.')
add(s,'h3','(iii) Standard Enthalpy of Reaction (ΔH°Reaction)','(iii) تعامل کی معیاری انتھالپی (ΔH°Reaction)','(iii) د تعامل معیاري انتالپي (ΔH°Reaction)',kind='heading')
add(s,'b1',f'The standard enthalpy of reaction, (ΔH°r), is the change in enthalpy for a given reaction calculated from the standard enthalpies of formation for all reactants and products. It can be calculated from the difference between the total enthalpies of formation of products and reactants as follows{SO}',f'تعامل کی معیاری انتھالپی (ΔH°r) کسی دیے گئے تعامل کی انتھالپی میں وہ تبدیلی ہے جو تمام تعامل کنندگان اور حاصلات کی تشکیل کی معیاری انتھالپیوں سے حساب کی جاتی ہے۔ اسے حاصلات اور تعامل کنندگان کی تشکیل کی کل انتھالپیوں کے فرق سے اس طرح حساب کیا جا سکتا ہے {SO}',f'د تعامل معیاري انتالپي (ΔH°r) د یو ورکړل شوي تعامل لپاره د انتالپي هغه بدلون دی چې د ټولو متعاملینو او محصولاتو د جوړېدو له معیاري انتالپیو څخه محاسبه کېږي. دا د محصولاتو او متعاملینو د جوړېدو د ټولو انتالپیو د توپیر څخه په لاندې ډول محاسبه کېدای شي {SO}')
F.p('h2','a1','a2')
F.e('r1',r'\mathrm{C_{(s)}+O_{2(g)}\rightarrow CO_{2(g)}}\qquad\Delta H^{\circ}_f=-393.51\ \mathrm{kJ\,mol^{-1}}','C(s) + O₂(g) → CO₂(g)   ΔH°f = −393.51 kJ mol⁻¹')
F.e('r2',r'\mathrm{S_{(s)}+O_{2(g)}\rightarrow SO_{2(g)}}\qquad\Delta H^{\circ}_f=-296.83\ \mathrm{kJ\,mol^{-1}}','S(s) + O₂(g) → SO₂(g)   ΔH°f = −296.83 kJ mol⁻¹')
F.tb(0)
F.p('h3','b1')
F.done()
s['sourceNote']='Printed folio 342 (the folio number is not visible). The right edge is clipped by the page curl on the prose (word endings cut) and on the table title; clipped endings are marked [scan obscured] and not inferred. The formula for the standard enthalpy of reaction continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; table title clipped; formula continues on the next page.')
s['vocabulary']={'enthalpy of formation':{'ur':'تشکیل کی انتھالپی','ps':'د جوړېدو انتالپي'}}
save(s)

# ---------- 348 ----------
s=mk(348,'ΔH°r formula · (iv) Standard Enthalpy of Combustion · Example 11.3 · Tidbit: Food energy','ΔH°r کا فارمولا · (iv) احتراق کی معیاری انتھالپی · مثال 11.3 · معلومات: خوراک کی توانائی','د ΔH°r فورمول · (iv) د سوځېدو معیاري انتالپي · بېلګه 11.3 · ځانګړې یادونه: د خوړو انرژي','combustion-example113')
F=Flow(s)
add(s,'a1','For example,','مثال کے طور پر،','د بېلګې په توګه،')
add(s,'h','(iv) Standard Enthalpy of Combustion (ΔH°c)','(iv) احتراق کی معیاری انتھالپی (ΔH°c)','(iv) د سوځېدو معیاري انتالپي (ΔH°c)',kind='heading')
add(s,'b1',f'It is the amount of heat produced when one mole of a compound in its standard state, is completely burnt in excess of air or oxygen at 298K and 1atm. pressure. All the substances involved are in their standard states and the reaction is carried out under standard conditions, i.e. 298 K (25°C) and one atmospheric pressure. For example, the enthalpy of combustion of CH₄ is −890 kJ mol⁻¹.','یہ حرارت کی وہ مقدار ہے جو اس وقت پیدا ہوتی ہے جب کسی مرکب کا ایک مول اپنی معیاری حالت میں 298K اور 1atm دباؤ پر ہوا یا آکسیجن کی زیادتی میں مکمل طور پر جلایا جائے۔ تمام شامل مادے اپنی معیاری حالتوں میں ہوتے ہیں اور تعامل معیاری حالات یعنی 298 K (25°C) اور ایک ماحولیاتی دباؤ پر کیا جاتا ہے۔ مثلاً CH₄ کی احتراق کی انتھالپی −890 kJ mol⁻¹ ہے۔','دا د تودوخې هغه مقدار دی چې کله د یو مرکب یو مول په خپل معیاري حالت کې په 298K او 1atm فشار کې د هوا یا اکسیجن په زیاتوالي کې په بشپړ ډول وسوځول شي جوړېږي. ټول شامل مواد په خپلو معیاري حالتونو کې دي او تعامل په معیاري شرایطو یعنې 298 K (25°C) او یو اتموسفیري فشار کې ترسره کېږي. د بېلګې په توګه د CH₄ د سوځېدو انتالپي −890 kJ mol⁻¹ ده.')
add(s,'e','Example 11.3','مثال 11.3','بېلګه 11.3',kind='heading')
add(s,'q','The heats of formation of CH₄(g), CO₂(g) and H₂O(g) are: −74.85kJ mol⁻¹, −393.50kJ mol⁻¹ and −285.81kJ mol⁻¹, respectively. Calculate the heat of combustion of the following reaction.','CH₄(g)، CO₂(g) اور H₂O(g) کی تشکیل کی حرارتیں بالترتیب −74.85kJ mol⁻¹، −393.50kJ mol⁻¹ اور −285.81kJ mol⁻¹ ہیں۔ درج ذیل تعامل کی احتراق کی حرارت معلوم کریں۔','د CH₄(g)، CO₂(g) او H₂O(g) د جوړېدو تودوخې په ترتیب سره −74.85kJ mol⁻¹، −393.50kJ mol⁻¹ او −285.81kJ mol⁻¹ دي. د لاندې تعامل د سوځېدو تودوخه محاسبه کړئ.')
add(s,'s','Solution:','حل:','حل:',kind='heading')
add(s,'t-h','Tidbit','معلومات','ځانګړې یادونه',kind='heading')
add(s,'t1','The potential energy stored in food stuff is experimentally determined by combustion analysis. Calculate your daily intake of food calories, the method of calculation is given in an example given below.','خوراک کی اشیاء میں ذخیرہ شدہ مخفی توانائی تجرباتی طور پر احتراقی تجزیے سے متعین کی جاتی ہے۔ اپنی روزانہ خوراک کی کیلوریز کا حساب لگائیں، حساب کا طریقہ نیچے دی گئی مثال میں دیا گیا ہے۔','په خوراکي توکو کې زېرمه شوې پوټنشیل انرژي په تجربوي ډول د سوځېدو تحلیل په واسطه ټاکل کېږي. خپل د ورځې د خوړو کالورۍ محاسبه کړئ، د محاسبې طریقه لاندې ورکړل شوې بېلګه کې ورکړل شوې.')
add(s,'t2','To calculate energy available from food, multiply the number of grams of carbohydrate, protein, and fat by 4, 4, and 9, respectively. Then add the result together.','خوراک سے دستیاب توانائی کا حساب لگانے کے لیے کاربوہائیڈریٹ، پروٹین اور چکنائی کے گراموں کی تعداد کو بالترتیب 4، 4 اور 9 سے ضرب دیں۔ پھر نتائج کو جمع کر لیں۔','د خوړو څخه د شته انرژۍ د محاسبې لپاره د کاربوهایډریټ، پروټین او غوړو د ګرامو شمېر په ترتیب سره په 4، 4 او 9 کې ضرب کړئ. بیا پایلې یوځای کړئ.')
add(s,'t3','Example: One slice of bread with a tablespoon of peanut butter on it contains 16 g carbohydrate, 7 g protein, and 9 g fat. Calculate total energy consumed in this intake.','مثال: ایک بریڈ کے سلائس پر ایک چمچ مونگ پھلی کا مکھن لگا ہو تو اس میں 16 g کاربوہائیڈریٹ، 7 g پروٹین اور 9 g چکنائی ہوتی ہے۔ اس خوراک میں استعمال شدہ کل توانائی معلوم کریں۔','بېلګه: د ډوډۍ یوه ټوټه چې په هغې د مونګپلۍ د مکھن یو چمچ وي 16 g کاربوهایډریټ، 7 g پروټین او 9 g غوړي لري. په دې خوراک کې مصرف شوې ټوله انرژي محاسبه کړئ.')
add(s,'t4','Solution:','حل:','حل:')
add(s,'t5','16 g carbohydrate × 4 kcal/g = 64 kcal','16 g کاربوہائیڈریٹ × 4 kcal/g = 64 kcal','16 g کاربوهایډریټ × 4 kcal/g = 64 kcal')
add(s,'t6','7 g protein × 4 kcl/g = 28 kcal','7 g پروٹین × 4 kcl/g = 28 kcal','7 g پروټین × 4 kcl/g = 28 kcal')
add(s,'t7','9 g fat × 9kcal/g = 81 kcal','9 g چکنائی × 9kcal/g = 81 kcal','9 g غوړي × 9kcal/g = 81 kcal')
add(s,'t8','Total = 173 kcal','کل = 173 kcal','ټول = 173 kcal')
F.e('f0',r'\Delta H^{\circ}_r=\sum\Delta H^{\circ}_{(products)}-\sum\Delta H^{\circ}_{(Reactants)}','ΔH°r = ΣΔH°(products) − ΣΔH°(Reactants)')
F.p('a1')
F.e('f1',r'2\mathrm{H_{2(g)}+O_{2(g)}\rightarrow2H_2O_{(l)}}\qquad\Delta H^{\circ}_{(Reaction)}=-572\ \mathrm{kJ\,mol^{-1}}','2H₂(g) + O₂(g) → 2H₂O(l)   ΔH°(Reaction) = −572 kJ mol⁻¹')
F.p('h','b1')
F.e('f2',r'\mathrm{CH_{4(g)}+2O_{2(g)}\longrightarrow CO_{2(g)}+2H_2O_{(g)}}\qquad\Delta H_c=-890\ \mathrm{kJ/mol}','CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)   ΔH_c = −890 kJ/mol')
F.p('e','q')
F.e('f3',r'\mathrm{CH_{4(g)}+2O_{2(g)}\longrightarrow CO_{2(g)}+2H_2O_{(g)}}\qquad\Delta H^{\circ}_c=?','CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)   ΔH°c = ?')
F.p('s')
F.e('g1',r'\text{Heat of the reaction}=\Delta H^{\circ}_r=\sum[\Delta H^{\circ}_{f\,products}]-\sum[\Delta H^{\circ}_{f\,reactants}]','Heat of the reaction = ΔH°r = Σ[ΔH°f products] − Σ[ΔH°f reactants]')
F.e('g2',r'\Delta H^{\circ}_c=[\Delta H^{\circ}_{fCO_2}+2\Delta H^{\circ}_{fH_2O}]-[\Delta H^{\circ}_{fCH_4}+2\Delta H^{\circ}_{fO_2}]','ΔH°c = [ΔH°fCO₂ + 2ΔH°fH₂O] − [ΔH°fCH₄ + 2ΔH°fO₂]')
F.e('g3',r'\Delta H^{\circ}_c=[-393.50+2(-285.81)]-[-74.85+2\times0]\ \mathrm{kJ\,mol^{-1}}','ΔH°c = [−393.50 + 2(−285.81)] − [−74.85 + 2×0] kJ mol⁻¹')
F.e('g4',r'\Delta H_c=[-965.12+74.85]\ \mathrm{kJ\,mol^{-1}}=-890.27\ \mathrm{kJ\,mol^{-1}}','ΔH_c = [−965.12 + 74.85] kJ mol⁻¹ = −890.27 kJ mol⁻¹')
F.p('t-h','t1','t2','t3','t4','t5','t6','t7','t8')
F.done()
s['sourceNote']='Printed folio 343. The formula at the top completes the sentence from the previous page ("…as follows"). The left edge is slightly clipped (first letters of several lines, and the heading marker "(iv)") but the text is legible. In the Tidbit, "kcl/g" for protein is printed as such (a source misprint for kcal/g) and retained; the Tidbit has a star mark that is not text. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Left-edge letters cut; "kcl/g" printed for kcal/g and retained.')
s['vocabulary']={'enthalpy of combustion':{'ur':'احتراق کی انتھالپی','ps':'د سوځېدو انتالپي'}}
save(s)
