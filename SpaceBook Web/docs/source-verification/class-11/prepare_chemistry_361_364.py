from chemlib import *
c=cell
def eqn(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
EC='chem11-electrochemistry'
def mk(n,title,ur,ps,sid): return page(n,EC,title,ur,ps,sid)
def tx(x,y,t,size=11,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'
class Flow:
    def __init__(s_,s): s_.s=s; s_.s['equations']=[]; s_.f=[]
    def p(s_,*keys):
        s_.f.append(dict(type='paragraphs',ids=[f"chem11-p{s_.s['source']['pdfPage']}-{k}" for k in keys]))
    def e(s_,key,latex,text):
        s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def done(s_): s_.s['flow']=s_.f

# ---------- 361 ----------
s=mk(361,'Unit 12 · Electrochemistry · Student learning outcomes','یونٹ 12 · برقی کیمیا · طلبہ کے تعلیمی نتائج','یونټ 12 · الکتروکیمیا · د زده کوونکو د زده کړې پایلې','unit12-outcomes')
add(s,'u','Unit-12','یونٹ-12','یونټ-12',kind='heading')
add(s,'t','Electrochemistry','برقی کیمیا','الکتروکیمیا',kind='heading')
add(s,'lead','After reading this unit, the students will be able to:','اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ:','د دې یونټ له لوستلو وروسته به زده کوونکي دې وړ شي چې:')
O=[('Give the characteristics of a Redox reaction. (Understanding)','ریڈاکس تعامل کی خصوصیات بیان کریں۔ (سمجھنا)','د ریډاکس تعامل ځانګړنې ورکړئ. (پوهېدل)'),
('Determine the oxidation number of an atom of any element in a pure substance. (Applying)','کسی خالص مادے میں کسی بھی عنصر کے ایٹم کا تکسیدی عدد متعین کریں۔ (اطلاق)','په یو خالص مواد کې د هر عنصر د اتوم د اکسیډیشن شمېره وټاکئ. (کارول)'),
('Define oxidation and reduction in terms of a change in oxidation number. (Applying)','تکسیدی عدد میں تبدیلی کے لحاظ سے تکسید اور تخفیف کی تعریف کریں۔ (اطلاق)','د اکسیډیشن شمېرې د بدلون په اړه اکسیډیشن او ریډکشن تعریف کړئ. (کارول)'),
('Use the oxidation-number change method to identify atoms being oxidized or reduced in redox reactions. (Applying)','ریڈاکس تعاملات میں تکسید یا تخفیف پانے والے ایٹموں کی شناخت کے لیے تکسیدی عدد کی تبدیلی کا طریقہ استعمال کریں۔ (اطلاق)','په ریډاکس تعاملاتو کې د اکسیډیز یا ریډیوس کېدونکو اتومونو د پېژندلو لپاره د اکسیډیشن شمېرې د بدلون طریقه وکاروئ. (کارول)'),
('Use the oxidation-number change method to balance redox equations. (Applying)','ریڈاکس مساواتوں کو متوازن کرنے کے لیے تکسیدی عدد کی تبدیلی کا طریقہ استعمال کریں۔ (اطلاق)','د ریډاکس معادلو د انډولولو لپاره د اکسیډیشن شمېرې د بدلون طریقه وکاروئ. (کارول)'),
('Balance redox reactions that take place in acid solutions. Break a redox reaction into oxidation and reduction half reactions. (Applying)','تیزابی محلولوں میں ہونے والے ریڈاکس تعاملات کو متوازن کریں۔ ریڈاکس تعامل کو تکسیدی اور تخفیفی نیم تعاملات میں تقسیم کریں۔ (اطلاق)','هغه ریډاکس تعاملات انډول کړئ چې په اسیدي محلولونو کې پېښېږي. یو ریډاکس تعامل په اکسیډیشن او ریډکشن نیمایي تعاملاتو ویشئ. (کارول)'),
('Use the half reaction method to balance an unbalanced a redox equation. (Applying)','غیر متوازن ریڈاکس مساوات کو متوازن کرنے کے لیے نیم تعامل کا طریقہ استعمال کریں۔ (اطلاق)','د نیمایي تعامل طریقه وکاروئ ترڅو یوه نه انډول شوې ریډاکس معادله انډول کړئ. (کارول)'),
('Define cathode, anode, electrode potential and S.H.E. (Standard Hydrogen Electrode). (Remembering)','کیتھوڈ، اینوڈ، الیکٹروڈ پوٹینشل اور S.H.E. (معیاری ہائیڈروجن الیکٹروڈ) کی تعریف کریں۔ (یاد رکھنا)','کیتوډ، انوډ، د الکترود پوټنشیل او S.H.E. (معیاري هایدروجن الکترود) تعریف کړئ. (په یاد ساتل)'),
('Identify the substance oxidized and the substance reduced in a dry cell. (Applying)','خشک سیل میں تکسید پانے والے مادے اور تخفیف پانے والے مادے کی شناخت کریں۔ (اطلاق)','په یو وچ سیل کې اکسیډیز شوی مواد او ریډیوس شوی مواد وپېژنئ. (کارول)'),
('Use the activity series of metals to predict the products of single replacement reactions. (Applying)','فلزات کی سرگرمی سلسلہ استعمال کر کے واحد تبدیلی کے تعاملات کے حاصلات کی پیش گوئی کریں۔ (اطلاق)','د فلزاتو د فعالیت لړۍ وکاروئ ترڅو د یو ځای کېدونکي بدلون تعاملاتو محصولات وړاندوینه کړئ. (کارول)'),
('Define cell potential and describe how it is determined. (Understanding)','سیل پوٹینشل کی تعریف کریں اور بیان کریں کہ یہ کیسے متعین ہوتا ہے۔ (سمجھنا)','د حجرې پوټنشیل تعریف کړئ او بیان کړئ چې دا څنګه ټاکل کېږي. (پوهېدل)'),
('Describe the reaction that occurs when a lead storage battery is recharged. (Applying)','وہ تعامل بیان کریں جو لیڈ سٹوریج بیٹری کو ری چارج کرتے وقت ہوتا ہے۔ (اطلاق)','هغه تعامل بیان کړئ چې کله د سرب ذخیره کوونکې بیټرۍ بیا چارج کېږي پېښېږي. (کارول)'),
('Explain how a fuel cell produces electrical energy. (Applying)','وضاحت کریں کہ ایندھن سیل برقی توانائی کیسے پیدا کرتا ہے۔ (اطلاق)','تشریح کړئ چې د سونګ حجره څنګه برېښنایي انرژي جوړوي. (کارول)'),
('Define the standard electrode potential of an electrode. (Remembering)','کسی الیکٹروڈ کے معیاری الیکٹروڈ پوٹینشل کی تعریف کریں۔ (یاد رکھنا)','د یو الکترود معیاري الکترود پوټنشیل تعریف کړئ. (په یاد ساتل)'),
('Distinguish between electrical terms such as coulomb, ampere and volt. (Understanding)','برقی اصطلاحات جیسے کولمب، ایمپیئر اور وولٹ میں فرق کریں۔ (سمجھنا)','د برېښنایي اصطلاحاتو لکه کولمب، امپیر او وولټ ترمنځ توپیر وکړئ. (پوهېدل)'),
("State and explain Faraday's laws. (Understanding)",'فیراڈے کے قوانین بیان کریں اور ان کی وضاحت کریں۔ (سمجھنا)','د فاراډې قوانین بیان او تشریح کړئ. (پوهېدل)'),
('Describe how dry cell supplies electricity. (Understanding)','بیان کریں کہ خشک سیل بجلی کیسے فراہم کرتا ہے۔ (سمجھنا)','بیان کړئ چې وچ سیل څنګه برېښنا برابروي. (پوهېدل)'),
('Explain how a lead storage battery produces electricity. (Understanding)','وضاحت کریں کہ لیڈ سٹوریج بیٹری بجلی کیسے پیدا کرتی ہے۔ (سمجھنا)','تشریح کړئ چې د سرب ذخیره کوونکې بیټرۍ څنګه برېښنا جوړوي. (پوهېدل)'),
('Define corrosion and describe simple methods like electroplating and galvanizing for its prevention. (Applying)','سنکنی (کروژن) کی تعریف کریں اور اس کی روک تھام کے سادہ طریقے جیسے برقی ملمع کاری اور جستی کاری بیان کریں۔ (اطلاق)','زنګ (کوروژن) تعریف کړئ او د هغې د مخنیوي ساده طریقې لکه الکتروپلیټینګ او ګالوانایزینګ بیان کړئ. (کارول)')]
for i,(e,u,p) in enumerate(O,1): add(s,f'o{i}',e,u,p)
head(s,'tw','Teaching Periods · Assessment · Weightage %','تدریسی پیریڈز · تشخیص · وزن %','د تدریس دورې · ارزونه · وزن %')
add(s,'tp','Teaching periods: 10','تدریسی پیریڈز: 10','د تدریس دورې: 10')
add(s,'as','Assessment: 01','تشخیص: 01','ارزونه: 01')
add(s,'wt','Weightage %: 08','وزن %: 08','وزن %: 08')
u=('<path d="M110 40 V90 Q110 140 160 140 Q210 140 210 90 V40" fill="none" stroke="#9ec8e8" stroke-width="12"/><rect x="95" y="20" width="30" height="45" fill="#c8a060" stroke="#6a4a20"/><rect x="195" y="20" width="30" height="45" fill="#c8a060" stroke="#6a4a20"/><path d="M125 30 C150 0 190 0 195 30" stroke="#e8a040" stroke-width="2" fill="none"/>')
s['figures']=[dict(id='chem11-p361-cover',svg=svg(320,160,'U-tube electrolytic cell with two electrodes connected by a wire',u),caption='Unit 12 cover: a U-tube with two electrodes',captionUrdu='یونٹ 12 کا سرورق: دو الیکٹروڈز والی U نلی',captionPashto='د 12 یونټ پوښ: دوه الکترودونو لرونکی U نل',labels=[lab('Electrodes','الیکٹروڈز','الکترودونه')],sourceGap=dict(note='Cover photograph (U-tube with electrodes) redrawn as a simple schematic.'))]
s['flow']=[dict(type='paragraphs',ids=ids(s,0,3)),dict(type='paragraphs',ids=ids(s,3,12)),dict(type='paragraphs',ids=ids(s,12)),dict(type='figure',index=0)]
s['sourceNote']='Printed folio 356. Unit opener. The right edge is clipped by the page curl on several outcome lines ("…in a pure substance", "…change in oxidation number", "…oxidized or reduced", "…balance redox", "…redox equation", "…Standard Hydrogen Electrode") but the sentences are legible and read in full; the outcome list continues on the next page. Side panel: Teaching 10, Assessment 01, Weightage % 08. Cover photograph redrawn as a schematic. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Slight right-edge clipping; list continues on the next page; cover photograph redrawn.')
s['vocabulary']={'electrochemistry':{'ur':'برقی کیمیا','ps':'الکتروکیمیا'},'redox reaction':{'ur':'ریڈاکس تعامل','ps':'ریډاکس تعامل'},'oxidation number':{'ur':'تکسیدی عدد','ps':'د اکسیډیشن شمېره'},'cathode':{'ur':'کیتھوڈ','ps':'کیتوډ'},'anode':{'ur':'اینوڈ','ps':'انوډ'}}
save(s)

# ---------- 362 ----------
s=mk(362,'Learning outcomes (continued) · Introduction · Conductors','تعلیمی نتائج (جاری) · تعارف · موصل','د زده کړې پایلې (دوام) · پېژندنه · تېرونکي','unit12-intro')
OO=O[9:]
for i,(e,u,p) in enumerate(OO,1): add(s,f'o{i}',e,u,p)
head(s,'h','Introduction','تعارف','پېژندنه')
add(s,'i1',f'Electrochemistry is the branch of chemistry which deals with the chemical changes that take place in the matter by passage of electric current and conversion of chemical energy into electrical energy and vice versa. The passage of electricity through the solutions of acids, bases and salts is accompanied by a chemical change. Such substances which allow electric current to pass through them in solution form or in molten form are called electrolytes.{SO}',f'برقی کیمیا کیمیا کی وہ شاخ ہے جو برقی رو کے گزرنے سے مادے میں ہونے والی کیمیائی تبدیلیوں اور کیمیائی توانائی کی برقی توانائی میں اور اس کے برعکس تبدیلی سے بحث کرتی ہے۔ تیزابوں، اساسوں اور نمکوں کے محلولوں میں سے بجلی کا گزرنا کیمیائی تبدیلی کے ساتھ ہوتا ہے۔ ایسے مادے جو محلول کی شکل میں یا پگھلی ہوئی شکل میں اپنے اندر سے برقی رو گزرنے دیں برق پاش کہلاتے ہیں {SO}۔',f'الکتروکیمیا د کیمیا هغه څانګه ده چې د برېښنايي جریان د تېرېدو په واسطه په مادې کې د پېښېدونکو کيمياوي بدلونونو او د کيمياوي انرژۍ برېښنایي انرژۍ ته او برعکس د بدلون سره بحث کوي. د اسیدونو، القليو او مالګو له محلولونو څخه د برېښنا تېرېدل د کيمياوي بدلون سره مل وي. داسې مواد چې په محلول بڼه یا په ویلې شوې بڼه کې برېښنايي جریان له ځانه تېرېدو ته پرېږدي الکترولایټونه بلل کېږي {SO}.')
add(s,'i2',f'In this unit, you will refresh your knowledge about certain basic terminologies used in the field of electrochemistry.{SO}',f'اس یونٹ میں آپ برقی کیمیا کے شعبے میں استعمال ہونے والی کچھ بنیادی اصطلاحات کے بارے میں اپنے علم کو تازہ کریں گے {SO}۔',f'پدې یونټ کې به تاسو د الکتروکیمیا په برخه کې کارېدونکو ځینو بنسټیزو اصطلاحاتو په اړه خپله پوهه تازه کړئ {SO}.')
head(s,'c0','Conductors','موصل (کنڈکٹرز)','تېرونکي')
add(s,'c1',f'Substances which allow the flow of electric current through them are known as conductors. The flow of current in metallic conductors, e.g. Cu, Ag etc. is due to the movement of electrons in the metal without any chemical change, while passage of electricity through the solutions of acids, bases and salts is accompanied by a chemical change.{SO}',f'وہ مادے جو اپنے اندر سے برقی رو کے بہاؤ کی اجازت دیں موصل کہلاتے ہیں۔ دھاتی موصلوں مثلاً Cu، Ag وغیرہ میں رو کا بہاؤ دھات میں الیکٹرانوں کی حرکت کی وجہ سے ہوتا ہے بغیر کسی کیمیائی تبدیلی کے، جبکہ تیزابوں، اساسوں اور نمکوں کے محلولوں میں سے بجلی کا گزرنا کیمیائی تبدیلی کے ساتھ ہوتا ہے {SO}۔',f'هغه مواد چې له ځانه د برېښنايي جریان بهېدو ته اجازه ورکوي تېرونکي بلل کېږي. په فلزي تېرونکو لکه Cu، Ag او نورو کې د جریان بهېدل په فلز کې د الکترونونو د حرکت له امله وي پرته له کوم کيمياوي بدلون، پداسې حال کې چې د اسیدونو، القليو او مالګو له محلولونو څخه د برېښنا تېرېدل د کيمياوي بدلون سره مل وي {SO}.')
s['flow']=[dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 357. The right edge is slightly clipped on the bottom of the page and the footer is cut; text is legible. The page repeats the remaining outcomes (continued from the previous page), then the Introduction box and the Conductors paragraph begin; the Conductors paragraph is cut at the page foot by the footer band. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Bottom edge of the page and footer clipped.')
s['vocabulary']={'electrolytes':{'ur':'برق پاش','ps':'الکترولایټونه'},'conductors':{'ur':'موصل','ps':'تېرونکي'}}
save(s)

# ---------- 363 ----------
s=mk(363,'Electrolytes · Strong and Weak Electrolytes · Electrolysis · Science, Technology and Society: Application of Redox Reactions and Electrolysis','برق پاش · مضبوط اور کمزور برق پاش · برق پاشیدگی · سائنس، ٹیکنالوجی اور معاشرہ: ریڈاکس تعاملات اور برق پاشیدگی کے اطلاقات','الکترولایټونه · قوي او ضعیف الکترولایټونه · الکترولیز · ساینس، ټیکنالوجي او ټولنه: د ریډاکس تعاملاتو او الکترولیز کارونې','electrolytes-sts')
head(s,'h1','Electrolytes','برق پاش','الکترولایټونه')
add(s,'a1',f'The substance which in solution or in molten state conducts electricity is called an electrolyte. Electrolytes may be strong or weak depending upon the extent of ionization.{SO}',f'وہ مادہ جو محلول میں یا پگھلی ہوئی حالت میں بجلی گزارے برق پاش کہلاتا ہے۔ برق پاش آئنائزیشن کی حد کے مطابق مضبوط یا کمزور ہو سکتے ہیں {SO}۔',f'هغه مواد چې په محلول یا ویلې شوې حالت کې برېښنا تېروي الکترولایټ بلل کېږي. الکترولایټونه د آیونایزیشن د اندازې په پام کې نیولو سره قوي یا ضعیف کېدای شي {SO}.')
head(s,'h2','Strong Electrolytes','مضبوط برق پاش','قوي الکترولایټونه')
add(s,'a2',f'The substance which is completely converted into its ions in the solution or in the molten state is called a strong electrolyte e.g. NaCl, NaOH and H₂SO₄.','وہ مادہ جو محلول میں یا پگھلی ہوئی حالت میں مکمل طور پر اپنے آئنوں میں تبدیل ہو جائے مضبوط برق پاش کہلاتا ہے مثلاً NaCl، NaOH اور H₂SO₄۔','هغه مواد چې په محلول یا ویلې شوې حالت کې په بشپړ ډول په خپلو آیونونو بدل شي قوي الکترولایټ بلل کېږي لکه NaCl، NaOH او H₂SO₄.')
head(s,'h3','Weak Electrolytes','کمزور برق پاش','ضعیف الکترولایټونه')
add(s,'a3','The substance which is partially dissociated into its ions is called a weak electrolyte e. g. NH₄OH and H₂CO₃.','وہ مادہ جو جزوی طور پر اپنے آئنوں میں تفکیک ہو کمزور برق پاش کہلاتا ہے مثلاً NH₄OH اور H₂CO₃۔','هغه مواد چې په جزوي ډول په خپلو آیونونو تجزیه شي ضعیف الکترولایټ بلل کېږي لکه NH₄OH او H₂CO₃.')
head(s,'h4','Electrolytic Conduction or Electrolysis','برق پاشی ایصال یا برق پاشیدگی (الیکٹرولیسس)','الکترولایټیک تېرونه یا الکترولیز')
add(s,'a4',f'Electrolysis is a phenomenon in which chemical change takes place at the surface of electrodes due to the passage of the electric current. On passing the current through an electrolytic solution, ions migrate to the opposite electrodes where the gain and loss of electrons take place which bring about the chemical change.{SO}',f'برق پاشیدگی ایسا مظہر ہے جس میں برقی رو کے گزرنے کی وجہ سے الیکٹروڈز کی سطح پر کیمیائی تبدیلی واقع ہوتی ہے۔ برق پاشی محلول میں سے رو گزارنے پر آئن مخالف الیکٹروڈز کی طرف ہجرت کرتے ہیں جہاں الیکٹرانوں کا حصول اور کھونا ہوتا ہے جو کیمیائی تبدیلی لاتا ہے {SO}۔',f'الکترولیز یوه پدیده ده چې په هغې کې د برېښنايي جریان د تېرېدو له امله د الکترودونو په سطحه کيمياوي بدلون پېښېږي. د الکترولایټیک محلول له لارې د جریان تېرولو پر مهال آیونونه مخالفو الکترودونو ته مهاجرت کوي چېرته چې د الکترونونو ترلاسه کول او له لاسه ورکول پېښېږي چې کيمياوي بدلون رامنځته کوي {SO}.')
head(s,'sts','Science, Technology and Society','سائنس، ٹیکنالوجی اور معاشرہ','ساینس، ټیکنالوجي او ټولنه')
add(s,'b0','Application of Redox Reactions and Electrolysis','ریڈاکس تعاملات اور برق پاشیدگی کے اطلاقات','د ریډاکس تعاملاتو او الکترولیز کارونې',kind='heading')
add(s,'b1','Some important applications of electrolysis on industrial scale are as follows:','صنعتی پیمانے پر برق پاشیدگی کے کچھ اہم اطلاقات درج ذیل ہیں:','په صنعتي کچه د الکترولیز ځینې مهمې کارونې په لاندې ډول دي:')
L=[(f'1) Batteries use oxidation and reduction reactions to produce direct current (DC).','1) بیٹریاں سیدھی رو (DC) پیدا کرنے کے لیے تکسید اور تخفیف کے تعاملات استعمال کرتی ہیں۔','1) بیټرۍ د مستقیم جریان (DC) د جوړولو لپاره د اکسیډیشن او ریډکشن تعاملات کاروي.'),
('2) Inside the rocket propellant, a redox reaction takes place.','2) راکٹ کے پروپیلنٹ کے اندر ریڈاکس تعامل ہوتا ہے۔','2) د راکټ د پروپیلنټ دننه ریډاکس تعامل پېښېږي.'),
(f'3) Many metals are separated from their ores with the help of redox reactions.{SO}',f'3) بہت سی دھاتیں ریڈاکس تعاملات کی مدد سے اپنی کچ دھات سے الگ کی جاتی ہیں {SO}۔',f'3) ډېر فلزات د ریډاکس تعاملاتو په مرسته له خپلو کانونو څخه جلا کېږي {SO}.'),
('4) Production of hydrogen gas by electrolysis of water.','4) پانی کی برق پاشیدگی سے ہائیڈروجن گیس کی پیداوار۔','4) د اوبو د الکترولیز په واسطه د هایدروجن ګاز تولید.'),
('5) Manufacture of heavy water, D₂O.','5) بھاری پانی D₂O کی تیاری۔','5) د درنو اوبو D₂O جوړول.'),
(f'6) The metals, like Na, K, Mg, Al etc. are obtained by electrolysis of fused electrolytes containing these metals.{SO}',f'6) Na، K، Mg، Al وغیرہ جیسی دھاتیں ان دھاتوں پر مشتمل پگھلے ہوئے برق پاشوں کی برق پاشیدگی سے حاصل کی جاتی ہیں {SO}۔',f'6) فلزات لکه Na، K، Mg، Al او نور د دې فلزاتو لرونکو ویلې شویو الکترولایټونو د الکترولیز په واسطه ترلاسه کېږي {SO}.'),
(f'7) Compounds, like NaOH, KOH, Na₂CO₃, KClO₃, KMnO₄ etc. are synthesized by electrolysis.{SO}',f'7) NaOH، KOH، Na₂CO₃، KClO₃، KMnO₄ وغیرہ جیسے مرکبات برق پاشیدگی سے تالیف کیے جاتے ہیں {SO}۔',f'7) مرکبات لکه NaOH، KOH، Na₂CO₃، KClO₃، KMnO₄ او نور د الکترولیز په واسطه ترکیبېږي {SO}.'),
(f'8) Electroplating is the process of coating an object made of inferior metal with a superior metal by electrolysis.{SO}',f'8) برقی ملمع کاری کسی کمتر دھات کی بنی شے پر برق پاشیدگی کے ذریعے اعلیٰ دھات کی تہہ چڑھانے کا عمل ہے {SO}۔',f'8) الکتروپلیټینګ د کمتر فلز څخه جوړ شوي شي په ځان د الکترولیز په واسطه د غوره فلز د پوښ کولو پروسه ده {SO}.'),
(f'9) Purification of metal by electrolysis is known as electroplating. In this method pure metal is deposited at cathode from a solution containing metal ions, e.g. Ag, Cu etc., where anode is a piece of impure metal.{SO}',f'9) برق پاشیدگی سے دھات کی تطہیر برقی ملمع کاری کے نام سے جانی جاتی ہے۔ اس طریقے میں خالص دھات دھاتی آئنوں پر مشتمل محلول سے کیتھوڈ پر جمع ہوتی ہے، مثلاً Ag، Cu وغیرہ، جہاں اینوڈ ناخالص دھات کا ٹکڑا ہوتا ہے {SO}۔',f'9) د الکترولیز په واسطه د فلز پاکول د الکتروپلیټینګ په نوم پېژندل کېږي. پدې طریقه کې خالص فلز د فلزي آیونونو لرونکي محلول څخه په کیتوډ کې ترسب کېږي، لکه Ag، Cu او نور، چېرته چې انوډ د ناپاک فلز ټوټه وي {SO}.')]
for i,(e,u,p) in enumerate(L,1): add(s,f'l{i}',e,u,p)
s['flow']=[dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 358. The right edge is clipped by the page curl on the Electrolytes paragraphs and on the STS list; clipped endings are marked [scan obscured] and not inferred. Item 9 is headed "Purification of metal … is known as electroplating" as printed (a source misstatement for electro-refining) and is retained. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; printed item 9 equates metal purification with "electroplating" and is retained as printed.')
s['vocabulary']={'electrolysis':{'ur':'برق پاشیدگی','ps':'الکترولیز'},'electroplating':{'ur':'برقی ملمع کاری','ps':'الکتروپلیټینګ'},'strong electrolyte':{'ur':'مضبوط برق پاش','ps':'قوي الکترولایټ'},'weak electrolyte':{'ur':'کمزور برق پاش','ps':'ضعیف الکترولایټ'}}
save(s)

# ---------- 364 ----------
s=mk(364,'12.1 Oxidation-Reduction Concepts · 12.1.1 Oxidation and Reduction · 12.1.2 Oxidation State','12.1 تکسید و تخفیف کے تصورات · 12.1.1 تکسید اور تخفیف · 12.1.2 تکسیدی حالت','12.1 د اکسیډیشن-ریډکشن مفکورې · 12.1.1 اکسیډیشن او ریډکشن · 12.1.2 د اکسیډیشن حالت','oxidation-reduction')
F=Flow(s)
head(s,'h1','12.1 Oxidation-Reduction Concepts','12.1 تکسید و تخفیف کے تصورات','12.1 د اکسیډیشن-ریډکشن مفکورې')
head(s,'h2','12.1.1 Oxidation and Reduction','12.1.1 تکسید اور تخفیف','12.1.1 اکسیډیشن او ریډکشن')
add(s,'a0','Oxidation and reduction can be defined in different ways.','تکسید اور تخفیف کی مختلف طریقوں سے تعریف کی جا سکتی ہے۔','اکسیډیشن او ریډکشن په بېلابېلو لارو تعریفېدای شي.')
add(s,'a1','A. The Classical Concept','الف۔ کلاسیکی تصور','الف. کلاسیکي مفکوره',kind='heading')
add(s,'a2','According to this concept, oxidation and reduction are defined as','اس تصور کے مطابق تکسید اور تخفیف کی تعریف اس طرح کی جاتی ہے','د دې مفکورې له مخې اکسیډیشن او ریډکشن داسې تعریفېږي')
add(s,'a3','i. The addition of oxygen is oxidation while the removal of oxygen is reduction. e.g. SO₂ is oxidized to SO₃ by gaining O while CO₂ is reduced to C by removal of O.','i. آکسیجن کا اضافہ تکسید ہے جبکہ آکسیجن کا ہٹانا تخفیف ہے۔ مثلاً SO₂ آکسیجن حاصل کر کے SO₃ میں تکسید ہوتی ہے جبکہ CO₂ آکسیجن ہٹانے سے C میں تخفیف ہوتی ہے۔','i. د اکسیجن اضافه کول اکسیډیشن دی پداسې حال کې چې د اکسیجن لرې کول ریډکشن دی. لکه SO₂ د O په ترلاسه کولو سره SO₃ ته اکسیډیز کېږي پداسې حال کې چې CO₂ د O په لرې کولو سره C ته ریډیوس کېږي.')
add(s,'a4','ii. The removal of H₂ is oxidation while its addition leads to reduction reaction. e.g. NH₃ is oxidized to N₂ while Cl₂ is reduced to HCl.','ii. H₂ کا ہٹانا تکسید ہے جبکہ اس کا اضافہ تخفیف کے تعامل کا باعث بنتا ہے۔ مثلاً NH₃، N₂ میں تکسید ہوتی ہے جبکہ Cl₂، HCl میں تخفیف ہوتی ہے۔','ii. د H₂ لرې کول اکسیډیشن دی پداسې حال کې چې د هغه اضافه کول د ریډکشن تعامل لامل کېږي. لکه NH₃ ته N₂ ته اکسیډیز کېږي پداسې حال کې چې Cl₂ ته HCl ته ریډیوس کېږي.')
add(s,'b0','B. Electron Transfer Concept','ب۔ الیکٹران منتقلی کا تصور','ب. د الکترون د لېږد مفکوره',kind='heading')
add(s,'b1','This concept is about the transfer of electrons from one element to another. The concept is explained below.','یہ تصور ایک عنصر سے دوسرے عنصر کو الیکٹرانوں کی منتقلی کے بارے میں ہے۔ تصور کی وضاحت نیچے کی گئی ہے۔','دا مفکوره له یو عنصر څخه بل ته د الکترونونو د لېږد په اړه ده. مفکوره لاندې تشریح شوې.')
add(s,'b2','The atom which loses electrons is said to be oxidized and this process is called oxidation. The atom which gains electrons is reduced and the phenomenon is called the reduction. In terms of oxidation number an increase in oxidation number is oxidation and decrease in oxidation number is reduction. For example','وہ ایٹم جو الیکٹران کھوتا ہے تکسید شدہ کہلاتا ہے اور اس عمل کو تکسید کہتے ہیں۔ وہ ایٹم جو الیکٹران حاصل کرتا ہے تخفیف شدہ ہوتا ہے اور اس مظہر کو تخفیف کہتے ہیں۔ تکسیدی عدد کے لحاظ سے تکسیدی عدد میں اضافہ تکسید اور تکسیدی عدد میں کمی تخفیف ہے۔ مثلاً','هغه اتوم چې الکترونونه له لاسه ورکوي اکسیډیز شوی ویل کېږي او دې پروسې ته اکسیډیشن ویل کېږي. هغه اتوم چې الکترونونه ترلاسه کوي ریډیوس کېږي او پدیدې ته ریډکشن ویل کېږي. د اکسیډیشن شمېرې په اړه د اکسیډیشن شمېرې زیاتوالی اکسیډیشن او د اکسیډیشن شمېرې کمښت ریډکشن دی. د بېلګې په توګه')
add(s,'b3','(Electron loss and increase in oxidation number; oxidation)','(الیکٹران کا کھونا اور تکسیدی عدد میں اضافہ؛ تکسید)','(د الکترون له لاسه ورکول او د اکسیډیشن شمېرې زیاتوالی؛ اکسیډیشن)')
add(s,'b4','(Addition of electron and decrease in oxidation number; reduction)','(الیکٹران کا اضافہ اور تکسیدی عدد میں کمی؛ تخفیف)','(د الکترون اضافه کول او د اکسیډیشن شمېرې کمښت؛ ریډکشن)')
add(s,'b5','(Net reaction)','(خالص تعامل)','(خالص تعامل)')
add(s,'c0','12.1.2 Oxidation State or Oxidation Number','12.1.2 تکسیدی حالت یا تکسیدی عدد','12.1.2 د اکسیډیشن حالت یا د اکسیډیشن شمېره',kind='heading')
add(s,'c1',f'The oxidation state is the apparent charge, positive or negative, which an atom would have in a molecule or ion. It is different from the valency because valency is only a number while oxidation state indicates the positive or negative charge of the atom. The oxidation state of an atom is described by its oxidation number which is assigned according to the following rules.{SO}',f'تکسیدی حالت ظاہری چارج ہے، مثبت یا منفی، جو ایک ایٹم کسی سالمے یا آئن میں رکھتا ہوگا۔ یہ گرفتی سے مختلف ہے کیونکہ گرفتی صرف ایک عدد ہے جبکہ تکسیدی حالت ایٹم کے مثبت یا منفی چارج کو ظاہر کرتی ہے۔ ایٹم کی تکسیدی حالت اس کے تکسیدی عدد سے بیان کی جاتی ہے جو درج ذیل قواعد کے مطابق تفویض کیا جاتا ہے {SO}۔',f'د اکسیډیشن حالت ښکاره چارج دی، مثبت یا منفي، چې یو اتوم به په یو مالیکول یا آیون کې ولري. دا له والنسي څخه توپیر لري ځکه چې والنسي یوازې یوه شمېره ده پداسې حال کې چې د اکسیډیشن حالت د اتوم مثبت یا منفي چارج ښيي. د اتوم د اکسیډیشن حالت د هغه د اکسیډیشن شمېرې په واسطه بیانېږي چې د لاندې قواعدو له مخې ټاکل کېږي {SO}.')
add(s,'r0','Rules for assigning the Oxidation number','تکسیدی عدد تفویض کرنے کے قواعد','د اکسیډیشن شمېرې د ټاکلو قواعد',kind='heading')
add(s,'r1',f'1. The oxidation number of a free element is zero, e.g. oxidation number of H₂, O₂ and Mn is zero.{SO}',f'1۔ آزاد عنصر کا تکسیدی عدد صفر ہوتا ہے، مثلاً H₂، O₂ اور Mn کا تکسیدی عدد صفر ہے {SO}۔',f'1. د یو آزاد عنصر د اکسیډیشن شمېره صفر ده، لکه د H₂، O₂ او Mn د اکسیډیشن شمېره صفر ده {SO}.')
F.p('h1','h2','a0','a1','a2','a3')
F.e('x1',r'2\mathrm{SO_2+O_2\longrightarrow 2SO_3}\qquad\text{(oxidation)}','2SO₂ + O₂ → 2SO₃   (oxidation)')
F.e('x2',r'\mathrm{CO_2\longrightarrow C+O_2}\qquad\text{(reduction)}','CO₂ → C + O₂   (reduction)')
F.p('a4')
F.e('y1',r'2\mathrm{NH_3\longrightarrow N_2+3H_2}\ \text{(oxidation)}','2NH₃ → N₂ + 3H₂ (oxidation)')
F.e('y2',r'\mathrm{H_2+Cl_2\longrightarrow 2HCl}\ \text{(reduction)}','H₂ + Cl₂ → 2HCl (reduction)')
F.p('b0','b1','b2')
F.e('z1',r'\mathrm{Al_{(s)}\longrightarrow Al^{3+}_{(aq)}+3e^-}\quad\text{(Electron loss and increase in oxidation number; oxidation)}','Al(s) → Al³⁺(aq) + 3e⁻   (Electron loss and increase in oxidation number; oxidation)')
F.e('z2',r'\mathrm{Cu^{2+}_{(aq)}+2e^-\longrightarrow Cu_{(s)}}\quad\text{(Addition of electron and decrease in oxidation number; reduction)}','Cu²⁺(aq) + 2e⁻ → Cu(s)   (Addition of electron and decrease in oxidation number; reduction)')
F.e('z3',r'2\mathrm{Al_{(s)}+3Cu^{2+}_{(aq)}\longrightarrow 2Al^{3+}_{(aq)}+3Cu_{(s)}}\quad\text{(Net reaction)}','2Al(s) + 3Cu²⁺(aq) → 2Al³⁺(aq) + 3Cu(s)   (Net reaction)')
F.p('c0','c1','r0','r1')
F.done()
s['paras']=[p for p in s['paras'] if not p['id'].endswith(('-b3','-b4','-b5'))]
s['sourceNote']='Printed folio 359. The page is skewed and the folio is partly cut. The right-hand annotations of the three electron-transfer lines are folded into the equations. The oxidation-state paragraph starts under a skewed "12.1.2" heading; the right edge is slightly clipped. The rules for the oxidation number begin at the foot (rule 1) and continue on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; rules for oxidation number continue on the next page.')
s['vocabulary']={'oxidation':{'ur':'تکسید','ps':'اکسیډیشن'},'reduction':{'ur':'تخفیف','ps':'ریډکشن'},'oxidation state':{'ur':'تکسیدی حالت','ps':'د اکسیډیشن حالت'},'valency':{'ur':'گرفتی','ps':'والنسي'}}
save(s)
