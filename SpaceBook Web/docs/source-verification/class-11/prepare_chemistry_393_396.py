from chemlib import *
EC='chem11-electrochemistry'
def eqn(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
class Flow:
    def __init__(s_,s): s_.s=s; s_.s['equations']=[]; s_.f=[]; s_.k=0
    def rest(s_):
        ids_=[p['id'] for p in s_.s['paras'][s_.k:]]; s_.k=len(s_.s['paras'])
        if ids_: s_.f.append(dict(type='paragraphs',ids=ids_))
    def e(s_,key,latex,text):
        s_.rest(); s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def done(s_): s_.rest(); s_.s['flow']=s_.f

# ---------- 393 ----------
s=page(393,EC,'EXERCISE · Choose the correct option (1–10)','مشق · درست جواب منتخب کریں (۱–۱۰)','تمرین · سم انتخاب وټاکئ (۱–۱۰)','exercise-mcq-1')
head(s,'ex','EXERCISE','مشق','تمرین'); head(s,'choose','Choose the correct option.','درست جواب منتخب کریں۔','سم انتخاب وټاکئ.')
mcq(s,1,'Weak electrolyte in solution is','محلول میں کمزور برق پاش ہے','په محلول کې کمزوری الکترولایټ دی',[('completely ionized','مکمل طور پر آئنائز','بشپړ آیونایز شوی'),('slightly ionized','معمولی آئنائز','لږ آیونایز شوی'),('never ionized','کبھی آئنائز نہیں','هېڅکله آیونایز نه شوی'),('destroyed','تباہ شدہ','ویجاړ شوی')],393)
mcq(s,2,'Which one of the following is a strong electrolyte in solution?','محلول میں درج ذیل میں سے کون سا مضبوط برق پاش ہے؟','په محلول کې له لاندې څخه کوم قوي الکترولایټ دی؟',[('Ammonium hydroxide','امونیم ہائیڈرو آکسائیڈ','امونیم هایدروکسایډ'),('Carbonic acid','کاربونک ایسڈ','کاربونیک اسید'),('Potassium iodide','پوٹاشیم آیوڈائیڈ','پوتاشیم آیوډایډ'),('Acetic acid','ایسٹک ایسڈ','اسیټیک اسید')],393)
mcq(s,3,'In electrolytic cell the cathode has a charge','برق پاشی خلیے میں کیتھوڈ پر چارج ہوتا ہے','په الکترولایټیک حجره کې کیتوډ چارج لري',[('Positive','مثبت','مثبت'),('Negative','منفی','منفي'),('Neutral','معتدل','خنثی'),('Zero','صفر','صفر')],393)
mcq(s,4,'The oxidation number of Cl in HClO₃ is','HClO₃ میں Cl کا تکسیدی عدد ہے','په HClO₃ کې د Cl د اکسیډیشن شمېره ده',[('-1',None,None),('+1',None,None),('+3',None,None),('+5',None,None)],393)
mcq(s,5,'The oxidation number of magnesium in MgCO₃ is','MgCO₃ میں میگنیشیم کا تکسیدی عدد ہے','په MgCO₃ کې د مګنیزیم د اکسیډیشن شمېره ده',[('+3',None,None),('+2',None,None),('+1',None,None),('-1',None,None)],393)
mcq(s,6,'Which one of the following is a reduction reaction','درج ذیل میں سے کون سا تخفیفی تعامل ہے','له لاندې څخه کوم ریډکشن تعامل دی',[('Br₂ → 2Br⁻','Br₂ → 2Br⁻','Br₂ → 2Br⁻'),('Fe²⁺ → Fe³⁺','Fe²⁺ → Fe³⁺','Fe²⁺ → Fe³⁺'),('Zn → Zn²⁺','Zn → Zn²⁺','Zn → Zn²⁺'),('Sn²⁺ → Sn⁴⁺','Sn²⁺ → Sn⁴⁺','Sn²⁺ → Sn⁴⁺')],393)
mcq(s,7,'A cell in which a non-spontaneous redox reaction is carried out by passing an electric current is a/an','وہ خلیہ جس میں برقی رو گزار کر غیر ازخود ریڈاکس تعامل کیا جاتا ہے','هغه حجره چې په هغې کې د برېښنایي جریان په تېرولو سره غیرځانګړی ریډاکس تعامل ترسره کېږي',[('Galvanic cell','گیلوانی خلیہ','ګلوانیک حجره'),('Voltaic cell','وولٹائی خلیہ','وولټایک حجره'),('Daniell cell','ڈینیل خلیہ','ډینیل حجره'),('Electrolytic cell','برق پاشی خلیہ','الکترولایټیک حجره')],393)
mcq(s,8,'Zinc rod acts as anode in the Daniell cell but acts as cathode when coupled with aluminum electrode, this is because the standard reduction potential of','زنک کی سلاخ ڈینیل خلیے میں اینوڈ کا کام کرتی ہے لیکن المونیم الیکٹروڈ کے ساتھ جوڑنے پر کیتھوڈ کا کام کرتی ہے، اس کی وجہ یہ ہے کہ معیاری تخفیفی پوٹینشل','د زنک ډنډه په ډینیل حجره کې د انوډ په توګه عمل کوي خو کله چې له المونیم الکترود سره وصل شي د کیتوډ په توګه عمل کوي، دا ځکه چې معیاري ریډکشن پوټنشیل',[('Zn>Al',None,None),('Zn < Al',None,None),('Zn=Al',None,None),('Zn=0',None,None)],393)
mcq(s,9,'Electrolysis is a process in which the cations and anions liberated from electrolyte are','برق پاشی ایک عمل ہے جس میں برق پاش سے خارج ہونے والے کیٹائن اور اینائن ہوتے ہیں','الکترولیز یو بهیر دی چې په هغه کې له الکترولایټ څخه خوشې شوي کیټاینونه او انیاینونه',[('hydrated','ہائیڈریٹڈ','هایدریټ شوي'),('hydrolyzed','آبکافت شدہ','هایدرولایز شوي'),('charged','چارج شدہ','چارج شوي'),('discharged','ڈسچارج شدہ','ډیسچارج شوي')],393)
mcq(s,10,'A cell which produces electric current by a redox reaction is called a/an','وہ خلیہ جو ریڈاکس تعامل سے برقی رو پیدا کرے کہلاتا ہے','هغه حجره چې د ریډاکس تعامل په واسطه برېښنایي جریان تولیدوي بلل کېږي',[('Voltaic cell','وولٹائی خلیہ','وولټایک حجره'),('Electrolytic cell','برق پاشی خلیہ','الکترولایټیک حجره'),('Half-cell','نیم خلیہ','نیمه حجره'),('Standard cell','معیاری خلیہ','معیاري حجره')],393)
F=Flow(s); F.done()
s['sourceNote']='Printed folio 388. No printed answers on the page. The scan is skewed and the layout is two columns of options; options are separate records. The Question 4 option "-1" is printed "-I" and Question 5 option "-1" is printed "-I" (the digit is read as 1). Question 7 prints "a/an" and Question 8 prints "aluminum"; as printed. The question stems 8 and 9 continue across the right edge and are read from the visible text. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; right-edge curl.')
s['vocabulary']={'electrolyte':{'ur':'برق پاش','ps':'الکترولایټ'},'oxidation number':{'ur':'تکسیدی عدد','ps':'د اکسیډیشن شمېره'}}
save(s)

# ---------- 394 ----------
s=page(394,EC,'EXERCISE · Choose the correct option (11–13) · Short Questions · Numerical (1)','مشق · درست جواب (۱۱–۱۳) · مختصر سوالات · عددی (۱)','تمرین · سم انتخاب (۱۱–۱۳) · لنډې پوښتنې · عددي (۱)','exercise-short-numerical')
mcq(s,11,'The lead storage battery is a/an','سیسہ ذخیرہ بیٹری ہے','د سرب ذخیره کوونکې بیټرۍ ده',[('Daniell cell','ڈینیل خلیہ','ډینیل حجره'),('Voltaic cell','وولٹائی خلیہ','وولټایک حجره'),('Dry cell','خشک خلیہ','وچه حجره'),('Electrolytic cell','برق پاشی خلیہ','الکترولایټیک حجره')],394)
mcq(s,12,'The electrode potential of the standard hydrogen electrode is chosen as','معیاری ہائیڈروجن الیکٹروڈ کا الیکٹروڈ پوٹینشل چنا گیا ہے','د معیاري هایدروجن الکترود الکترود پوټنشیل ټاکل شوی',[('0 V',None,None),('1V',None,None),('-1 V',None,None),('2V',None,None)],394)
mcq(s,13,'A cathode has the reduction potential','کیتھوڈ کا تخفیفی پوٹینشل ہوتا ہے','کیتوډ ریډکشن پوټنشیل لري',[('Less than the anode','اینوڈ سے کم','له انوډ څخه لږ'),('More than the anode','اینوڈ سے زیادہ','له انوډ څخه ډېر'),('same as that of anode.','اینوڈ کے برابر','د انوډ سره یو شان'),('zero','صفر','صفر')],394)
add(s,'short','Short Questions','مختصر سوالات','لنډې پوښتنې',kind='heading')
SQ=[('What is the oxidation number of N in N₂O, NO₂, N₂O₃, HNO₃, and NH₄⁺.','N₂O، NO₂، N₂O₃، HNO₃ اور NH₄⁺ میں N کا تکسیدی عدد کیا ہے۔','په N₂O، NO₂، N₂O₃، HNO₃ او NH₄⁺ کې د N د اکسیډیشن شمېره څومره ده.'),
('Na⁺ is an oxidizing but Na is a reducing agent, why?','Na⁺ تکسیدی ہے لیکن Na تخفیفی ایجنٹ ہے، کیوں؟','Na⁺ اکسیډېزنګ دی خو Na ریډیوسینګ اجنټ دی، ولې؟'),
('The lead storage battery is rechargeable. Why?','سیسہ ذخیرہ بیٹری دوبارہ چارج ہو سکتی ہے۔ کیوں؟','د سرب ذخیره کوونکې بیټرۍ بیا چارج کېدونکې ده. ولې؟'),
('Why a solution of sugar is non-conductor but that of table salt is a good conductor of electricity?','چینی کا محلول غیر موصل کیوں ہے جبکہ کھانے کے نمک کا محلول بجلی کا اچھا موصل ہے؟','د بوره محلول غیرهادي ولې دی پداسې حال کې چې د خوړو مالګې محلول د برېښنا ښه هادي دی؟'),
('NaCl is non-conductor in the solid state but is a good conductor in molten form. Why?','NaCl ٹھوس حالت میں غیر موصل ہے لیکن پگھلی حالت میں اچھا موصل ہے۔ کیوں؟','NaCl په جامد حالت کې غیرهادي دی خو په ویلې شوې بڼه کې ښه هادي دی. ولې؟'),
('During electrolysis of fused NaCl, sodium metal is collected at cathode and not at anode, why?','پگھلے ہوئے NaCl کی برق پاشی کے دوران سوڈیم دھات کیتھوڈ پر جمع ہوتی ہے نہ کہ اینوڈ پر، کیوں؟','د ویلې شوي NaCl د الکترولیز پر مهال سوډیم فلز په کیتوډ کې راټولېږي نه په انوډ کې، ولې؟'),
('SHE acts as anode with Cu electrode but acts as cathode when connected to Zn electrode.','SHE، Cu الیکٹروڈ کے ساتھ اینوڈ کا کام کرتا ہے لیکن Zn الیکٹروڈ سے جوڑنے پر کیتھوڈ کا کام کرتا ہے۔','SHE له Cu الکترود سره د انوډ په توګه عمل کوي خو کله چې له Zn الکترود سره وصل شي د کیتوډ په توګه عمل کوي.'),
('In electroplating, the article to be plated is made cathode, why?','برق ملمع کاری میں جس چیز پر ملمع کرنا ہو اسے کیتھوڈ بنایا جاتا ہے، کیوں؟','په برېښنایي پوښښ کې هغه شی چې پوښل کېږي کیتوډ جوړېږي، ولې؟')]
for i,(a,b,c) in enumerate(SQ,1):
    add(s,f'sq-{i}',f'{i}. {a}',f'{i}۔ {b}',f'{i}. {c}',role='question',exerciseId=f'chem11-p394-short-{i}')
add(s,'num','Numerical','عددی','عددي',kind='heading')
add(s,'n1','1. Balance the following equation by Oxidation Number method','1۔ تکسیدی عدد کے طریقے سے درج ذیل مساوات کو متوازن کریں','1. لاندې معادله د اکسیډیشن شمېرې په طریقه انډول کړئ',role='question',exerciseId='chem11-p394-numerical-1')
F=Flow(s)
F.e('i',r'\text{i.}\ \mathrm{KMnO_4+H_2S+H_2SO_4\longrightarrow KHSO_4+MnSO_4+S+H_2O}','i. KMnO₄ + H₂S + H₂SO₄ → KHSO₄ + MnSO₄ + S + H₂O')
F.e('ii',r'\text{ii.}\ \mathrm{Fe+V_2O_3\longrightarrow Fe_2O_3+VO}','ii. Fe + V₂O₃ → Fe₂O₃ + VO')
F.e('iii',r'\text{iii.}\ \mathrm{MnO_2+4HCl\longrightarrow MnCl_2+Cl_2+H_2O}','iii. MnO₂ + 4HCl → MnCl₂ + Cl₂ + H₂O')
F.e('iv',r'\text{iv.}\ \mathrm{Mg+HCl\longrightarrow MgCl_2+H_2}','iv. Mg + HCl → MgCl₂ + H₂')
F.e('v',r'\text{v.}\ \mathrm{Cu+H_2SO_4\longrightarrow CuSO_4+SO_2+H_2O}','v. Cu + H₂SO₄ → CuSO₄ + SO₂ + H₂O')
F.e('vi',r'\text{vi.}\ \mathrm{KMnO_4+KNO_2+H_2SO_4\longrightarrow MnSO_4+KNO_3+K_2SO_4+H_2O}','vi. KMnO₄ + KNO₂ + H₂SO₄ → MnSO₄ + KNO₃ + K₂SO₄ + H₂O')
F.done()
s['sourceNote']='Printed folio 389. No printed answers on the page. The scan is skewed. In Short Question 1 the printed formulas are "N₂O, NO₂, N₂O₃, HNO₃, and NH₄⁺" (the final punctuation is a full stop). Question 7 of the Short Questions is printed as a statement ending in a full stop, not a question; retained as printed. Equations are listed under Numerical 1 as items i–vi. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan.')
s['vocabulary']={}
# flow: place equations after n1 (short/num paragraphs precede them)
s['flow']=[dict(type='paragraphs',ids=[p['id'] for p in s['paras']])]+[dict(type='equation',index=i) for i in range(len(s['equations']))]
save(s)

# ---------- 395 ----------
s=page(395,EC,'EXERCISE · Numerical (2, 3) · Descriptive Questions','مشق · عددی (۲، ۳) · تفصیلی سوالات','تمرین · عددي (۲، ۳) · تشریحي پوښتنې','exercise-numerical-descriptive')
add(s,'n2','2. Balance the following redox equations by the half reaction method','2۔ درج ذیل ریڈاکس مساواتوں کو نیم تعامل کے طریقے سے متوازن کریں','2. لاندې ریډاکس معادلې د نیمایي تعامل په طریقه انډول کړئ',role='question',exerciseId='chem11-p395-numerical-2')
add(s,'n3','3. Given the following cells at 25°C.','3۔ 25°C پر درج ذیل خلیے دیے گئے ہیں۔','3. په 25°C کې لاندې حجرې ورکړل شوي.',role='question',exerciseId='chem11-p395-numerical-3')
add(s,'n3a','(a) Write the cell reactions','(الف) خلوی تعاملات لکھیں','(الف) د حجرې تعاملات ولیکئ',role='question',exerciseId='chem11-p395-numerical-3a')
add(s,'n3b','(b) Calculate the cell voltage','(ب) خلوی وولٹیج کا حساب لگائیں','(ب) د حجرې وولټیج محاسبه کړئ',role='question',exerciseId='chem11-p395-numerical-3b')
add(s,'dh','Descriptive Questions','تفصیلی سوالات','تشریحي پوښتنې',kind='heading')
DQ=[('d1a','1. (a) Define the term electrolysis. State and explain Faraday\'s laws of electrolysis.','1۔ (الف) برق پاشی کی اصطلاح کی تعریف کریں۔ فیراڈے کے قوانینِ برق پاشی بیان کریں اور ان کی وضاحت کریں۔','1. (الف) د الکترولیز اصطلاح تعریف کړئ. د فاراډې د الکترولیز قوانین بیان او تشریح کړئ.'),
('d1b','(b) A certain amount of current is passed through CuSO₄ solution for fifty minutes. The net amount of Cu deposited was found to be 25g. Calculate the current when Z=1 and At. Mass of Cu is 63.5g.','(ب) CuSO₄ محلول میں سے پچاس منٹ تک ایک خاص مقدار کی رو گزاری گئی۔ جمع ہونے والے Cu کی خالص مقدار 25g پائی گئی۔ رو کا حساب لگائیں جب Z=1 ہے اور Cu کی ایٹمی کمیت 63.5g ہے۔','(ب) د CuSO₄ محلول له لارې د جریان یو ټاکلی مقدار پنځوس دقیقې تېر شو. د ترسب شوي Cu خالص مقدار 25g وموندل شو. جریان محاسبه کړئ کله چې Z=1 او د Cu اټومي کتله 63.5g ده.'),
('d2','2. What is an electrode potential? How it can be measured?','2۔ الیکٹروڈ پوٹینشل کیا ہے؟ اسے کیسے ناپا جا سکتا ہے؟','2. د الکترود پوټنشیل څه دی؟ دا څنګه اندازه کېدای شي؟'),
('d3','3. What is the difference between the following? Give examples.','3۔ درج ذیل میں کیا فرق ہے؟ مثالیں دیں۔','3. د لاندې ترمنځ څه توپیر دی؟ بېلګې ورکړئ.'),
('d3i','i) Reversible and irreversible cells','i) الٹ پذیر اور ناقابلِ واپسی خلیے','i) بیرته راګرځېدونکې او بیرته نه راګرځېدونکې حجرې'),
('d3ii','ii) Electrolytic and voltaic cell','ii) برق پاشی اور وولٹائی خلیہ','ii) الکترولایټیک او وولټایک حجره'),
('d4i','4. i) Explain the term oxidation and reduction with example.','4۔ i) مثال کے ساتھ تکسید اور تخفیف کی اصطلاحات کی وضاحت کریں۔','4. i) په بېلګې سره د اکسیډیشن او ریډکشن اصطلاحات تشریح کړئ.'),
('d4ii','ii) What is oxidation state? Give the oxidation number of Mn in KMnO₄, MnO₂ and Mn₂O₇.','ii) تکسیدی حالت کیا ہے؟ KMnO₄، MnO₂ اور Mn₂O₇ میں Mn کا تکسیدی عدد بتائیں۔','ii) د اکسیډیشن حالت څه دی؟ په KMnO₄، MnO₂ او Mn₂O₇ کې د Mn د اکسیډیشن شمېره ورکړئ.'),
('d5','5. What is an electrolytic cell? Explain Daniell cell in detail.','5۔ برق پاشی خلیہ کیا ہے؟ ڈینیل خلیے کی تفصیل سے وضاحت کریں۔','5. الکترولایټیک حجره څه ده؟ د ډینیل حجره په تفصیل سره تشریح کړئ.'),
('d5a','a) Calculate the electrical energy obtained from a Daniell cell.','الف) ڈینیل خلیے سے حاصل ہونے والی برقی توانائی کا حساب لگائیں۔','الف) له ډینیل حجرې څخه ترلاسه شوې برېښنایي انرژي محاسبه کړئ.'),
('d5b','b) What are the half-cell reaction? Give the half-cell reactions of the Nelson\'s cell for the production of NaOH.','ب) نیم خلوی تعامل کیا ہیں؟ NaOH کی تیاری کے لیے نیلسن خلیے کے نیم خلوی تعاملات بتائیں۔','ب) نیمه حجروي تعامل څه دي؟ د NaOH د جوړولو لپاره د نیلسن حجرې نیمه حجروي تعاملات ورکړئ.')]
for k,a,b,c in DQ: add(s,k,a,b,c,role='question',exerciseId=f'chem11-p395-desc-{k}')
F=Flow(s)
F.rest_ids=None
# order: n2, equations (half reaction items), n3.., table of cells as equations, descriptive
s['equations']=[]
def E(key,latex,text): s['equations'].append(eqn(395,key,latex,text))
E('h1',r'\text{i.}\ \mathrm{Sn^{2+}+Fe^{3+}\longrightarrow Sn^{4+}+Fe^{2+}}\quad\text{(Acidic medium)}','i. Sn²⁺ + Fe³⁺ → Sn⁴⁺ + Fe²⁺   (Acidic medium)')
E('h2',r'\text{ii.}\ \mathrm{Zn+Cr_2O_7^{2-}+H^+\longrightarrow Zn^{2+}+Cr^{3+}+H_2O}\quad\text{(Acidic medium)}','ii. Zn + Cr₂O₇²⁻ + H⁺ → Zn²⁺ + Cr³⁺ + H₂O   (Acidic medium)')
E('h3',r'\text{iii.}\ \mathrm{H_2O_2+MnO_4^-+H^+\longrightarrow Mn^{2+}+O_2+H_2O}\quad\text{(Acidic medium)}','iii. H₂O₂ + MnO₄⁻ + H⁺ → Mn²⁺ + O₂ + H₂O   (Acidic medium)')
E('h4',r'\text{iv.}\ \mathrm{Sn^{2+}+I_2\longrightarrow Sn^{4+}+I^-}\quad\text{(Neutral)}','iv. Sn²⁺ + I₂ → Sn⁴⁺ + I⁻   (Neutral)')
E('c1',r'\text{i. 1)}\ \mathrm{Mg^{2+}/Mg}\qquad E^\circ_{Red}=-2.38\,\mathrm{V}','i. 1) Mg²⁺/Mg   E°Red = −2.38 V')
E('c2',r'\text{2)}\ \mathrm{Cu^{2+}/Cu}\qquad E^\circ_{Red}=+0.34\,\mathrm{V}','2) Cu²⁺/Cu   E°Red = +0.34 V')
E('c3',r'\text{ii. 1)}\ \mathrm{2H^+/H_2}\qquad E^\circ_{Red}=0.00\,\mathrm{V}','ii. 1) 2H⁺/H₂   E°Red = 0.00 V')
E('c4',r'\text{2)}\ \mathrm{Ag^+/Ag}\qquad E^\circ_{Red}=+0.80\,\mathrm{V}','2) Ag⁺/Ag   E°Red = +0.80 V')
pid=lambda k:f'chem11-p395-{k}'
s['flow']=[dict(type='paragraphs',ids=[pid('n2')])]+[dict(type='equation',index=i) for i in range(4)]+[dict(type='paragraphs',ids=[pid('n3'),pid('n3a'),pid('n3b')])]+[dict(type='equation',index=i) for i in range(4,8)]+[dict(type='paragraphs',ids=[pid(k) for k in ['dh']+[d[0] for d in DQ]])]
s['sourceNote']='Printed folio 390. No printed answers on the page. The scan is skewed with right-edge curl; the right ends of Descriptive Question 4(ii) and 5 are partly clipped ("MnO₂", "Nelson\'s") but legible. The medium labels "(Acidic medium)", "(Acidic medium)", "(Acidic medium)", "(Neutral)" are printed at the right of items i–iv. In Descriptive Question 1(b) the printed "At. Mass" is retained. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; right-edge curl.')
s['vocabulary']={}
save(s)

# ---------- 396 ----------
s=page(396,EC,'EXERCISE · Descriptive Questions (6, 7) · Project','مشق · تفصیلی سوالات (۶، ۷) · منصوبہ','تمرین · تشریحي پوښتنې (۶، ۷) · پروژه','exercise-descriptive-project')
add(s,'d6','6. What are electrochemical cells? Explain it in detail.','6۔ برق کیمیائی خلیے کیا ہیں؟ اس کی تفصیل سے وضاحت کریں۔','6. الکتروکيمياوي حجرې څه دي؟ دا په تفصیل سره تشریح کړئ.',role='question',exerciseId='chem11-p396-desc-6')
add(s,'d7','7. Write down the types of batteries. Explain fuel cells?','7۔ بیٹریوں کی اقسام لکھیں۔ ایندھن خلیوں کی وضاحت کریں؟','7. د بیټریو ډولونه ولیکئ. د سونګ حجرې تشریح کړئ؟',role='question',exerciseId='chem11-p396-desc-7')
add(s,'ph','Project','منصوبہ','پروژه',kind='heading')
add(s,'p1','Take two lead pencils and sharp them from both the ends in order to expose the inner carbon cores. Take a beaker filled with 100 mL water acidified with sulphuric acid. Fix the two pencils in the beaker in vertical position about 2cm from each other. Connect the pencil cores with electrical wires with the terminals of a 9 volt battery, one pencil with the positive pole and other with the negative pole of the battery. When the battery is switched on you will see bubbles coming from the lower ends of the pencil cores. What do you think about the nature of the bubbles? Which reactions are carried out at the pencil ends? Identify the anode and the cathode?','دو سیسہ پنسلیں لیں اور اندرونی کاربن مغز ظاہر کرنے کے لیے انہیں دونوں سروں سے تراشیں۔ سلفیورک ایسڈ سے تیزابی بنائے گئے 100 mL پانی سے بھرا ایک بیکر لیں۔ دونوں پنسلوں کو بیکر میں تقریباً 2cm کے فاصلے پر عمودی حالت میں لگائیں۔ پنسل کے مغزوں کو برقی تاروں کے ذریعے 9 وولٹ بیٹری کے سروں سے جوڑیں، ایک پنسل کو بیٹری کے مثبت قطب سے اور دوسری کو منفی قطب سے۔ جب بیٹری چالو کی جاتی ہے تو آپ کو پنسل کے مغزوں کے نچلے سروں سے بلبلے نکلتے نظر آئیں گے۔ بلبلوں کی نوعیت کے بارے میں آپ کیا سوچتے ہیں؟ پنسل کے سروں پر کون سے تعاملات ہوتے ہیں؟ اینوڈ اور کیتھوڈ کی نشاندہی کریں؟','دوه سرب پنسلونه واخلئ او د دننه کاربن مغزونو د ښکاره کولو لپاره یې له دواړو سرونو تیره کړئ. د سلفیوریک اسید سره تیزابي شوې 100 mL اوبو ډک بیکر واخلئ. دواړه پنسلونه په بیکر کې نږدې 2cm واټن سره په عمودي حالت کې ټینګ کړئ. د پنسل مغزونه د برېښنایي تارونو په واسطه د 9 وولټ بیټرۍ له سرونو سره وصل کړئ، یوه پنسل د بیټرۍ له مثبت قطب سره او بله له منفي قطب سره. کله چې بیټرۍ چالان شي نو تاسو به د پنسل مغزونو له ښکتنیو سرونو څخه ګومبیزې راوتل وګورئ. د ګومبیزو د طبیعت په اړه تاسو څه فکر کوئ؟ د پنسل په سرونو کې کوم تعاملات ترسره کېږي؟ انوډ او کیتوډ وپیژنئ؟')
F=Flow(s); F.done()
s['sourceNote']='Printed folio 391 (the folio is not legible on the scan). The page has two questions and the Project and is otherwise blank below; the lower part of the page is cropped. The scan is skewed with strong right-edge curl and a CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; bottom cropped.')
s['vocabulary']={}
save(s)
