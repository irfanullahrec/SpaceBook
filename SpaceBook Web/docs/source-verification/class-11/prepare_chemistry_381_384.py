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
    def fg(s_,i): s_.f.append(dict(type='figure',index=i))
    def done(s_): s_.s['flow']=s_.f

# ---------- 381 ----------
s=mk(381,'Voltaic cell (continued) · Daniell Cell · Figure 12.7','وولٹائی خلیہ (جاری) · ڈینیل خلیہ · شکل 12.7','وولټایک حجره (دوام) · ډینیل حجره · شکل 12.7','daniell-cell')
F=Flow(s)
add(s,'a1',f'takes place. At one electrode electrons enter resulting in reduction reaction while at the other they leave the solution and oxidation takes place. A typical example of the voltaic cell is that of a Daniell cell.','ہوتا ہے۔ ایک الیکٹروڈ پر الیکٹران داخل ہوتے ہیں جس سے تخفیفی تعامل ہوتا ہے جبکہ دوسرے پر وہ محلول چھوڑتے ہیں اور تکسید ہوتی ہے۔ وولٹائی خلیے کی ایک عام مثال ڈینیل خلیہ ہے۔','پېښېږي. په یوه الکترود کې الکترونونه ننوځي چې د ریډکشن تعامل لامل کېږي پداسې حال کې چې په بل کې دوی محلول پرېږدي او اکسیډیشن پېښېږي. د وولټایک حجرې یوه عادي بېلګه د ډینیل حجره ده.')
add(s,'h','Daniell Cell:','ڈینیل خلیہ:','ډینیل حجره:',kind='heading')
add(s,'b1','As you have studied in your ninth grade, this cell has a Zn electrode dipped into 1M ZnSO₄ solution and a Cu electrode immersed in a 1M solution of Cu²⁺ ions. These two half cells are externally connected through a metallic wire while internally they are connected by a salt bridge. The salt bridge contains an aqueous KCl solution in a gel and allows electric connectivity between the two compartments i.e. anode and cathode compartments.','جیسا کہ آپ نے نویں جماعت میں پڑھا ہے، اس خلیے میں Zn الیکٹروڈ 1M ZnSO₄ محلول میں ڈوبا ہوتا ہے اور Cu الیکٹروڈ Cu²⁺ آئنوں کے 1M محلول میں ڈوبا ہوتا ہے۔ یہ دونوں نیم خلیے بیرونی طور پر دھاتی تار سے جڑے ہوتے ہیں جبکہ اندرونی طور پر نمکی پل سے جڑے ہوتے ہیں۔ نمکی پل میں جیل میں KCl کا آبی محلول ہوتا ہے اور دونوں خانوں یعنی اینوڈ اور کیتھوڈ خانوں کے درمیان برقی رابطہ ممکن بناتا ہے۔','لکه څنګه چې تاسو په نهمه ټولګي کې لوستي، په دې حجره کې د Zn الکترود په 1M ZnSO₄ محلول کې ډوب وي او د Cu الکترود د Cu²⁺ آیونونو په 1M محلول کې ډوب وي. دا دوه نیمې حجرې په بهرني ډول د فلزي تار په واسطه وصل دي پداسې حال کې چې په داخلي ډول د مالګینې پله په واسطه وصل دي. مالګینه پله په جیل کې د KCl اوبیز محلول لري او د دوو برخو یعنې انوډ او کیتوډ برخو ترمنځ برېښنایي اړیکه ممکنه کوي.')
add(s,'b2',f'Zn tends to lose electrons more readily than Cu giving its electrons to the electrode at the anode and get oxidized. Electrons flow from the Zn electrode to the Cu electrode through external circuit. The Cu²⁺ ions, surrounding the cathode, pick up the electrons and get deposited as neutral metal at the copper cathode where reduction of Cu²⁺ takes place. The following half reactions occur at the electrodes.','Zn میں Cu کی نسبت الیکٹران زیادہ آسانی سے کھونے کا رجحان ہے، وہ اپنے الیکٹران اینوڈ پر الیکٹروڈ کو دیتا ہے اور تکسید ہو جاتا ہے۔ الیکٹران بیرونی سرکٹ سے Zn الیکٹروڈ سے Cu الیکٹروڈ کی طرف بہتے ہیں۔ کیتھوڈ کے گرد موجود Cu²⁺ آئن ان الیکٹرانوں کو لے لیتے ہیں اور تانبے کے کیتھوڈ پر معتدل دھات کے طور پر جمع ہو جاتے ہیں جہاں Cu²⁺ کی تخفیف ہوتی ہے۔ الیکٹروڈز پر درج ذیل نیم تعاملات ہوتے ہیں۔','Zn د Cu په پرتله الکترونونه ډېر په اسانۍ له لاسه ورکوي، خپل الکترونونه په انوډ کې الکترود ته ورکوي او اکسیډیز کېږي. الکترونونه د بهرني سرکټ له لارې له Zn الکترود څخه Cu الکترود ته بهېږي. د کیتوډ شاوخوا Cu²⁺ آیونونه الکترونونه اخلي او د مسو په کیتوډ کې د خنثی فلز په توګه ترسب کېږي چېرته چې د Cu²⁺ ریډکشن پېښېږي. لاندې نیمایي تعاملات په الکترودونو کې پېښېږي.')
add(s,'an','At anode','اینوڈ پر','په انوډ کې')
add(s,'ca','At cathode','کیتھوڈ پر','په کیتوډ کې')
add(s,'nr','Net reaction','خالص تعامل','خالص تعامل')
add(s,'b3','The cell is represented as follows,','خلیہ اس طرح ظاہر کیا جاتا ہے،','حجره په لاندې ډول ښودل کېږي،')
d=('<rect x="10" y="10" width="330" height="240" fill="#f2f2f2" stroke="#555"/><path d="M80 60 V40 H255 V60" fill="none" stroke="#222" stroke-width="1.5"/><circle cx="168" cy="40" r="9" fill="#fff" stroke="#222"/>'+tx(168,44,'V',10,'middle',700)+
 '<path d="M45 150 V200 H125 V150" fill="#c490d0" fill-opacity=".7"/><path d="M215 140 V200 H300 V140" fill="#e0a860" fill-opacity=".8"/><path d="M35 100 V205 Q35 220 50 220 H135 Q150 220 150 205 V150 M205 140 V205 Q205 220 220 220 H305 Q320 220 320 205 V100" fill="none" stroke="#333" stroke-width="2"/>'
 '<rect x="75" y="62" width="10" height="130" fill="#445" stroke="#222"/><rect x="250" y="62" width="10" height="130" fill="#6a3a2a" stroke="#222"/><path d="M110 170 V105 H215 V170" fill="none" stroke="#bbb" stroke-width="12"/><path d="M110 170 V105 H215 V170" fill="none" stroke="#444" stroke-width="2"/>'
 +tx(40,60,'negative',9,'start')+tx(40,70,'anode',9,'start')+tx(262,60,'positive',9,'start')+tx(262,70,'cathode',9,'start')+tx(168,26,'voltmeter',9)+tx(168,98,'salt bridge',9)+tx(25,95,'zinc',9,'start')+tx(262,95,'copper',9,'start')+tx(80,238,'zinc sulphate solution',9)+tx(250,238,'copper sulphate solution',9)+tx(175,272,'Fig: 12.7 Daniell Cell',12,'middle',700,'#a02040'))
s['figures']=[dict(id='chem11-p381-fig127',svg=svg(350,285,'Daniell cell: zinc anode in zinc sulphate solution and copper cathode in copper sulphate solution connected by a salt bridge and a voltmeter',d),caption='Fig: 12.7 Daniell Cell',captionUrdu='شکل 12.7 ڈینیل خلیہ',captionPashto='شکل 12.7 ډینیل حجره',labels=[lab('voltmeter','وولٹ میٹر','وولټ میټر'),lab('negative anode','منفی اینوڈ','منفي انوډ'),lab('positive cathode','مثبت کیتھوڈ','مثبت کیتوډ'),lab('salt bridge','نمکی پل','مالګینه پله'),lab('zinc','زنک','زنک'),lab('copper','تانبا','مس'),lab('zinc sulphate solution','زنک سلفیٹ محلول','د زنک سلفیټ محلول'),lab('copper sulphate solution','کاپر سلفیٹ محلول','د مسو سلفیټ محلول')],sourceGap=dict(note='Photo-style Daniell cell illustration redrawn as a schematic; colours and geometry simplified.'))]
F.p('a1','h','b1'); F.fg(0); F.p('b2','an')
F.e('r1',r'\mathrm{Zn\longrightarrow Zn^{2+}+2e^-}\qquad E^\circ_{Ox}=+0.76\,\mathrm{V}','Zn → Zn²⁺ + 2e⁻   E°Ox = +0.76 V')
F.p('ca')
F.e('r2',r'\mathrm{Cu^{2+}+2e^-\longrightarrow Cu}\qquad E^\circ_{Red}=+0.34\,\mathrm{V}','Cu²⁺ + 2e⁻ → Cu   E°Red = +0.34 V')
F.p('nr')
F.e('r3',r'\mathrm{Zn+Cu^{2+}\longrightarrow Zn^{2+}+Cu}\qquad E^\circ_{cell}=1.10\,\mathrm{V}','Zn + Cu²⁺ → Zn²⁺ + Cu   E°cell = 1.10 V')
F.p('b3')
F.e('r4',r'\mathrm{Zn_{(s)}/Zn^{2+}_{(aq)}(1M)\,//\,Cu^{2+}_{(aq)}(1M)/Cu_{(s)}}','Zn(s)/Zn²⁺(aq)(1M) // Cu²⁺(aq)(1M)/Cu(s)')
F.done()
s['sourceNote']='Printed folio 376. The scan is skewed with right-edge curl; the right ends of the first paragraphs are clipped slightly. A pen-drawn oval around "Daniell Cell:" and around the cell notation is not text. The Fig. 12.7 labels are small and partly blurred; they were read as best possible. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; figure labels blurred; figure redrawn as schematic.')
s['vocabulary']={'daniell cell':{'ur':'ڈینیل خلیہ','ps':'ډینیل حجره'},'salt bridge':{'ur':'نمکی پل','ps':'مالګینه پله'}}
save(s)

# ---------- 382 ----------
s=mk(382,"Tidbit: Some Electrical Terms · Faraday's Laws of Electrolysis","معلومات: کچھ برقی اصطلاحات · فیراڈے کے قوانینِ برق پاشی",'معلومات: ځینې برېښنایي اصطلاحات · د فاراډې د الکترولیز قوانین','faraday-laws')
F=Flow(s)
add(s,'t0','Tidbit','معلومات','معلومات',kind='heading')
add(s,'t1','Some Electrical Terms','کچھ برقی اصطلاحات','ځینې برېښنایي اصطلاحات',kind='heading')
add(s,'t2','A Coulomb is the SI unit for quantity of electricity, it is defined as the quantity of electric charge carried by a current of on ampere flowing through a wire for one second. 1 Coulomb =1 ampere x1 sec or 1C=1Ax1s.','کولمب برقی مقدار کی SI اکائی ہے، اسے اس برقی چارج کی مقدار کے طور پر بیان کیا جاتا ہے جو ایک ایمپیئر کی رو ایک سیکنڈ تک تار میں بہنے سے لے جاتی ہے۔ 1 کولمب = 1 ایمپیئر × 1 سیکنڈ یا 1C = 1A × 1s۔','کولمب د برېښنا د مقدار SI واحد دی، دا د هغه برېښنایي چارج د مقدار په توګه تعریفېږي چې د یو امپیر جریان د یوې ثانیې لپاره په تار کې بهېدو سره وړل کېږي. 1 کولمب = 1 امپیر × 1 ثانیه یا 1C = 1A × 1s.')
add(s,'t3','Ampere: It is basic SI unit used for measuring the rate of electron flow or electric current in an electric conductor. One ampere of current represents one coulomb of electric charge (carried by 6.24x10¹⁸ electrons) moving through a specific point in one second. 1 Ampere= 1Coulomb/second.','ایمپیئر: یہ بنیادی SI اکائی ہے جو برقی موصل میں الیکٹرانوں کے بہاؤ کی شرح یا برقی رو ناپنے کے لیے استعمال ہوتی ہے۔ ایک ایمپیئر کی رو ایک کولمب برقی چارج (جسے 6.24×10¹⁸ الیکٹران لے جاتے ہیں) کی ایک خاص نقطے سے ایک سیکنڈ میں گزرنے کو ظاہر کرتی ہے۔ 1 ایمپیئر = 1 کولمب/سیکنڈ۔','امپیر: دا بنسټیز SI واحد دی چې په برېښنایي هادي کې د الکترون د بهېدو کچې یا برېښنایي جریان د اندازه کولو لپاره کارول کېږي. د یو امپیر جریان د یو کولمب برېښنایي چارج (چې 6.24×10¹⁸ الکترونونه یې وړي) په یوه ثانیه کې د یوې ځانګړې نقطې له لارې تېرېدل ښيي. 1 امپیر = 1 کولمب/ثانیه.')
add(s,'t4','Volt: It is the measure of how strongly an electric current is sent around an electric circuit. It is unit of electric potential or electromotive force. A potential of one volt appears across a resistance of one ohm when a current of one ampere flows through that resistance.','وولٹ: یہ اس بات کی پیمائش ہے کہ برقی رو کو برقی سرکٹ میں کتنی قوت سے بھیجا جاتا ہے۔ یہ برقی پوٹینشل یا برقی محرک قوت کی اکائی ہے۔ ایک وولٹ کا پوٹینشل ایک اوہم کی مزاحمت پر اس وقت ظاہر ہوتا ہے جب ایک ایمپیئر کی رو اس مزاحمت میں سے گزرتی ہے۔','وولټ: دا د دې اندازه ده چې برېښنایي جریان په برېښنایي سرکټ کې څومره قوت سره لېږل کېږي. دا د برېښنایي پوټنشیل یا برېښنایي محرکه قوې واحد دی. د یو وولټ پوټنشیل د یو اوهم په مقاومت کې هغه وخت څرګندېږي کله چې د یو امپیر جریان د دې مقاومت له لارې تېرېږي.')
add(s,'h1',"Faraday's Laws of Electrolysis",'فیراڈے کے قوانینِ برق پاشی','د فاراډې د الکترولیز قوانین',kind='heading')
add(s,'a1','Michael Faraday (1813) gave a relationship between the quantity of electricity passed and the amount of substances deposited at the electrode.','مائیکل فیراڈے (1813) نے گزاری گئی بجلی کی مقدار اور الیکٹروڈ پر جمع ہونے والے مادوں کی مقدار کے درمیان تعلق دیا۔','مایکل فاراډې (1813) د تېر شوي برېښنا د مقدار او په الکترود کې د ترسب شویو موادو د مقدار ترمنځ اړیکه ورکړه.')
add(s,'h2',"Faraday's First Law:",'فیراڈے کا پہلا قانون:','د فاراډې لومړی قانون:',kind='heading')
add(s,'a2','The amount of any substance (W) deposited or liberated at an electrode is directly proportional to the quantity of electricity (Q) passed.','کسی بھی مادے کی مقدار (W) جو الیکٹروڈ پر جمع یا خارج ہو، گزاری گئی بجلی کی مقدار (Q) کے براہِ راست متناسب ہوتی ہے۔','د هر ماده مقدار (W) چې په الکترود کې ترسب یا خوشې کېږي د تېر شوي برېښنا له مقدار (Q) سره مستقیماً متناسب وي.')
add(s,'or','Or','یا','یا')
add(s,'a3','Where, W is the mass in gram, Q is amount of charge in Coulombs and Z is the proportionality constant. Z is called the electrochemical equivalent. When Q=1C then Eq.(12.3) becomes','جہاں W گرام میں کمیت ہے، Q کولمب میں چارج کی مقدار ہے اور Z تناسبی مستقلہ ہے۔ Z کو برق کیمیائی مساوی کہتے ہیں۔ جب Q=1C ہو تو مساوات (12.3) بن جاتی ہے','چېرته W په ګرامو کې کتله ده، Q په کولمبو کې د چارج مقدار دی او Z تناسبي ثابت دی. Z ته الکتروکيمياوي معادل ویل کېږي. کله چې Q=1C وي نو معادله (12.3) کېږي')
add(s,'a4','Here with the help of Eq. (12.4) we can now define the electrochemical equivalent as the mass of substance liberated when one Coulomb electricity is passed through the electrolyte solution.','یہاں مساوات (12.4) کی مدد سے ہم اب برق کیمیائی مساوی کی تعریف اس مادے کی کمیت کے طور پر کر سکتے ہیں جو برق پاش محلول میں سے ایک کولمب بجلی گزارنے پر خارج ہو۔','دلته د معادلې (12.4) په مرسته موږ اوس کولای شو الکتروکيمياوي معادل د هغه ماده د کتلې په توګه تعریف کړو چې کله د الکترولایټ محلول له لارې یو کولمب برېښنا تېره شي خوشې کېږي.')
add(s,'a5','Moreover, amount of charge, Q = I t where, I is current in amperes and t is time in seconds. Thus, we can also write Eq. (12.3) as','مزید یہ کہ چارج کی مقدار Q = I t ہے جہاں I ایمپیئر میں رو اور t سیکنڈ میں وقت ہے۔ اس طرح ہم مساوات (12.3) کو یوں بھی لکھ سکتے ہیں','سربیره پر دې، د چارج مقدار Q = I t دی چېرته I په امپیرو کې جریان او t په ثانیو کې وخت دی. په دې توګه موږ کولای شو معادله (12.3) داسې هم ولیکو')
add(s,'h3',"Faraday's Second Law",'فیراڈے کا دوسرا قانون','د فاراډې دوهم قانون',kind='heading')
add(s,'b1',f"It states that, 'if the same amount of electricity is passed through the solutions of different electrolytes, the amounts of different substances deposited are in the ratio of their chemical equivalents. Or the masses of different substances liberated for the same quantity of electric charge during the{SO}","یہ بیان کرتا ہے کہ 'اگر بجلی کی یکساں مقدار مختلف برق پاشوں کے محلولوں میں سے گزاری جائے تو جمع ہونے والے مختلف مادوں کی مقداریں ان کے کیمیائی مساویوں کی نسبت میں ہوتی ہیں۔ یا برقی چارج کی یکساں مقدار کے لیے خارج ہونے والے مختلف مادوں کی کمیتیں برق پاشی کے دوران {SO}","دا وايي چې 'که د برېښنا یو شان مقدار د بېلابېلو الکترولایټونو د محلولونو له لارې تېر شي نو د ترسب شویو بېلابېلو موادو مقدارونه د هغو د کیمیاوي معادلونو په تناسب وي. یا د برېښنایي چارج د یو شان مقدار لپاره د الکترولیز پر مهال د خوشې شویو بېلابېلو موادو کتلې {SO}")
F.p('t0','t1','t2','t3','t4','h1','a1','h2','a2')
F.e('r1',r'W\propto Q\qquad(12.3)','W ∝ Q   (12.3)')
F.p('or')
F.e('r2',r'W=ZQ','W = ZQ')
F.p('a3')
F.e('r3',r'W=Z\qquad(12.4)','W = Z   (12.4)')
F.p('a4','a5')
F.e('r4',r'W=ZIt\qquad(12.5)','W = ZIt   (12.5)')
F.p('h3','b1')
F.done()
s['sourceNote']='Printed folio 377. A handwritten "V=IR" beside the Volt definition is ignored. The printed text reads "a current of on ampere" (retained). The word "electrochemical equivalent" is in pink italic. Eq. (12.3) is printed "W ∝ Q" followed by "Or W=ZQ" at the same number (12.3). The page is skewed, with right-edge curl; the last sentence continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; sentence continues next page.')
s['vocabulary']={'coulomb':{'ur':'کولمب','ps':'کولمب'},'ampere':{'ur':'ایمپیئر','ps':'امپیر'},'volt':{'ur':'وولٹ','ps':'وولټ'},'electrochemical equivalent':{'ur':'برق کیمیائی مساوی','ps':'الکتروکيمياوي معادل'}}
save(s)

# ---------- 383 ----------
s=mk(383,"Faraday's Second Law (continued) · Equation 12.6 · Example 12.7",'فیراڈے کا دوسرا قانون (جاری) · مساوات 12.6 · مثال 12.7','د فاراډې دوهم قانون (دوام) · معادله 12.6 · بېلګه 12.7','faraday-second')
F=Flow(s)
add(s,'a1',f'electrolysis are proportional to their equivalent masses. Suppose a certain amount of current passing through the dil. CuSO₄ and dil. AgNO₃ solutions for the same interval of time, then, we will find that the ratio of the masses of liberated silver and copper is 107.88/31.54 because equivalent mass of silver is 107.88 and that of copper is 31.548.',f'ان کے مساوی کمیتوں کے متناسب ہوتی ہیں۔ فرض کریں کہ ہلکے CuSO₄ اور ہلکے AgNO₃ محلولوں میں سے ایک ہی وقت کے وقفے کے لیے ایک خاص مقدار کی رو گزاری جائے، تو ہم دیکھیں گے کہ خارج ہونے والی چاندی اور تانبے کی کمیتوں کی نسبت 107.88/31.54 ہے کیونکہ چاندی کی مساوی کمیت 107.88 اور تانبے کی 31.548 ہے۔','د هغو له معادلو کتلو سره متناسب دي. فرض کړئ چې د جریان یو ټاکلی مقدار د رقیق CuSO₄ او رقیق AgNO₃ محلولونو له لارې د یو شان وخت وقفې لپاره تېر شي، نو موږ به ومومو چې د خوشې شویو سپینو زرو او مسو د کتلو نسبت 107.88/31.54 دی ځکه چې د سپینو زرو معادله کتله 107.88 او د مسو 31.548 ده.')
add(s,'a2','Thus','اس طرح','په دې توګه')
add(s,'a3','Also from the Faraday\'s first law','نیز فیراڈے کے پہلے قانون سے','همداراز د فاراډې له لومړي قانون څخه')
add(s,'a5','Combining above two equations we get W ∝ I t e','مندرجہ بالا دونوں مساواتوں کو ملانے سے ہمیں W ∝ I t e ملتا ہے','پورتنۍ دواړې معادلې یوځای کولو سره موږ W ∝ I t e ترلاسه کوو')
add(s,'a6','Introducing the proportionality constant 1/F, we get.','تناسبی مستقلہ 1/F متعارف کرانے پر ہمیں ملتا ہے۔','د تناسبي ثابت 1/F په معرفي کولو سره موږ ترلاسه کوو.')
add(s,'b1',f'Where "F" is called Faraday\'s constant which is equal to 9650[scan obscured] Coulomb/mol.',f'جہاں "F" کو فیراڈے مستقلہ کہتے ہیں جو 9650[scan obscured] کولمب/مول کے برابر ہے۔',f'چېرته "F" ته د فاراډې ثابت ویل کېږي چې 9650[scan obscured] کولمب/مول سره مساوي دی.')
add(s,'b2',f'Faraday\'s second law can also be derived mathematically from equation (12.6). It can be concluded from this equation that for a fixed amount of electricity passed for a fixed time the term It/F assumes a fixed value and under this condition W∝e which, as the law states that the amount of substance, W liberated, is directly proportional to the equivalent mass \'e\'.',f'فیراڈے کا دوسرا قانون مساوات (12.6) سے ریاضیاتی طور پر بھی اخذ کیا جا سکتا ہے۔ اس مساوات سے یہ نتیجہ نکالا جا سکتا ہے کہ ایک مقررہ وقت کے لیے گزاری گئی بجلی کی مقررہ مقدار کے لیے It/F کی قیمت مقررہ ہوتی ہے اور اس شرط کے تحت W∝e ہوتا ہے، جیسا کہ قانون بیان کرتا ہے کہ خارج ہونے والے مادے کی مقدار W مساوی کمیت \'e\' کے براہِ راست متناسب ہے۔',f'د فاراډې دوهم قانون د معادلې (12.6) څخه په ریاضیاتي ډول هم استخراج کېدای شي. له دې معادلې څخه دا پایله اخیستل کېدای شي چې د ټاکلي وخت لپاره د تېر شوي برېښنا د ټاکلي مقدار لپاره It/F یو ټاکلی ارزښت غوره کوي او پدې شرط W∝e کېږي، لکه څنګه چې قانون وايي چې د خوشې شوي ماده مقدار W د معادلې کتلې \'e\' سره مستقیماً متناسب دی.')
add(s,'x7','Example 12.7','مثال 12.7','بېلګه 12.7',kind='heading')
add(s,'x7q','A certain amount of current is passed through AgNO₃ solution for three hours. The net amount of Ag deposited was found to be 60.8 g. Calculate the current when gram equivalents (e) of Ag is 107.8.','AgNO₃ محلول میں سے تین گھنٹے تک ایک خاص مقدار کی رو گزاری گئی۔ جمع ہونے والی Ag کی خالص مقدار 60.8 g پائی گئی۔ رو کا حساب لگائیں جب Ag کے گرام مساوی (e) 107.8 ہیں۔','د AgNO₃ محلول له لارې د جریان یو ټاکلی مقدار درې ساعته تېر شو. د ترسب شوي Ag خالص مقدار 60.8 g وموندل شو. جریان محاسبه کړئ کله چې د Ag ګرام معادل (e) 107.8 وي.',role='question')
add(s,'sol','Solution','حل','حل',kind='heading')
add(s,'s1','Time (t)=3 hours = 3 x 60 x 60 s','وقت (t) = 3 گھنٹے = 3 × 60 × 60 s','وخت (t) = 3 ساعته = 3 × 60 × 60 s')
add(s,'s2','W (amount of Ag)= 60.8g','W (Ag کی مقدار) = 60.8g','W (د Ag مقدار) = 60.8g')
add(s,'s3','Gram equivalent mass of Ag (e)=107.8g,  F=96500 C mol⁻¹','Ag کی گرام مساوی کمیت (e) = 107.8g،  F = 96500 C mol⁻¹','د Ag ګرام معادله کتله (e) = 107.8g،  F = 96500 C mol⁻¹')
F.p('a1','a2')
F.e('r1',r'W\propto \text{Equivalent mass }(e)','W ∝ Equivalent mass (e)')
F.p('a3')
F.e('r2',r'W\propto Q\qquad\text{or}\qquad W\propto It','W ∝ Q   or   W ∝ It')
F.p('a5','a6')
F.e('r3',r'W=\frac{1}{F}Ite\qquad(12.6)','W = (1/F) Ite   (12.6)')
F.p('b1','b2','x7','x7q','sol','s1','s2','s3')
F.e('r4',r'W=\frac{1}{F}Ite','W = (1/F) Ite')
F.e('r5',r'I=\frac{WF}{te}','I = WF/te')
F.e('r6',r'I=\frac{60.8\,\mathrm{g}\times 96500\,\mathrm{C/mol}}{3\times60\times60\,\mathrm{s}\times107.8\,\mathrm{g/mol}}=5.04\,\mathrm{A}','I = (60.8 g × 96500 C/mol) / (3 × 60 × 60 s × 107.8 g/mol) = 5.04 A')
F.done()
s['sourceNote']='Printed folio 378. The scan is skewed with strong right-edge curl: line ends in the first paragraphs ("Suppose a certain…", "solutions for…", "masses of…", "silver is…") and in b1/b2 ("equal to 9650[…]", "from equation", "electricity", "under this", "substance W") are clipped. Printed values retained: "107.88/31.54" and "31.548" differ in the source; Eq. numbering as printed. A "Not For Sale" watermark stamp and a CamScanner watermark cross the page.'
s['sourceGap']=dict(note='Skewed scan; right-edge curl clipping; printed numeric inconsistency 31.54/31.548 retained.')
s['vocabulary']={"faraday's constant":{'ur':'فیراڈے مستقلہ','ps':'د فاراډې ثابت'}}
save(s)

# ---------- 384 ----------
s=mk(384,'12.3.4 Batteries · Primary Batteries · Dry Cell · Figure 12.8','12.3.4 بیٹریاں · ابتدائی بیٹریاں · خشک خلیہ · شکل 12.8','12.3.4 بیټرۍ · لومړنۍ بیټرۍ · وچه حجره · شکل 12.8','batteries-dry-cell')
F=Flow(s)
add(s,'h','12.3.4 Batteries','12.3.4 بیٹریاں','12.3.4 بیټرۍ',kind='heading')
add(s,'a1','There are four major types of batteries.','بیٹریوں کی چار بڑی اقسام ہیں۔','د بیټریو څلور لوی ډولونه شته.')
add(s,'t1','1 Primary batteries:','1 ابتدائی بیٹریاں:','1 لومړنۍ بیټرۍ:',kind='heading')
add(s,'a2','These batteries are not reversible and once discharged cannot be recharged, e.g. dry cell.','یہ بیٹریاں الٹ پذیر نہیں ہوتیں اور ایک بار خالی ہونے کے بعد دوبارہ چارج نہیں کی جا سکتیں، مثلاً خشک خلیہ۔','دا بیټرۍ بیرته راګرځېدونکې نه دي او یو ځل خالي کېدو وروسته بیا چارج نشي کېدای، لکه وچه حجره.')
add(s,'t2','2 Secondary batteries:','2 ثانوی بیٹریاں:','2 دوهمي بیټرۍ:',kind='heading')
add(s,'a3','They are reversible and can be recharged, e.g. Lead storage battery.','یہ الٹ پذیر ہوتی ہیں اور دوبارہ چارج کی جا سکتی ہیں، مثلاً سیسہ ذخیرہ بیٹری۔','دا بیرته راګرځېدونکې دي او بیا چارج کېدای شي، لکه د سرب ذخیره کوونکې بیټرۍ.')
add(s,'t3','3 Solar batteries:','3 شمسی بیٹریاں:','3 لمریزې بیټرۍ:',kind='heading')
add(s,'a4','They are photoelectrical cells and generate energy.','یہ فوٹو الیکٹرک خلیے ہیں اور توانائی پیدا کرتی ہیں۔','دا فوتو برېښنایي حجرې دي او انرژي تولیدوي.')
add(s,'t4','4 Fuel batteries:','4 ایندھن بیٹریاں:','4 سونګ بیټرۍ:',kind='heading')
add(s,'a5','They are the super batteries and have high charge density.','یہ سپر بیٹریاں ہیں اور ان میں چارج کی کثافت زیادہ ہوتی ہے۔','دا سوپر بیټرۍ دي او لوړ چارج کثافت لري.')
add(s,'p1','(i) Primary Batteries','(i) ابتدائی بیٹریاں','(i) لومړنۍ بیټرۍ',kind='heading')
add(s,'p2','Dry Cell','خشک خلیہ','وچه حجره',kind='heading')
add(s,'b1',f'As you have studied in your previous class, the container of the cell is made of Zn, which acts as an anode. The container is lined with a porous paper, which separates anode from inside material. A graphite rod in the centre of the cell acts as cathode. Electrolyte is a moist mixture of NH₄Cl, MnO₂, ZnCl₂ and powdered carbon. The dry cell is sealed to prevent the evaporation of moisture. When the dry cell delivers current, Zn oxidizes to Zn²⁺ ions and leaves electrons on the Zn container. The electrons move through outer circuit to the graphite cathode, where NH₄⁺ ions pick up the electrons and release NH₃ at the cathode. NH₃ produced at the cathode reacts with Zn²⁺ ions to form a complex ion. The redox reactions taking place at the two electrodes are as follows.','جیسا کہ آپ نے پچھلی جماعت میں پڑھا ہے، خلیے کا برتن Zn کا بنا ہوتا ہے جو اینوڈ کا کام کرتا ہے۔ برتن پر مسام دار کاغذ کی تہہ لگی ہوتی ہے جو اینوڈ کو اندرونی مواد سے الگ کرتی ہے۔ خلیے کے مرکز میں گریفائٹ کی سلاخ کیتھوڈ کا کام کرتی ہے۔ برق پاش NH₄Cl، MnO₂، ZnCl₂ اور پسے ہوئے کاربن کا نم مرکب ہے۔ خشک خلیے کو نمی کے بخارات بننے سے روکنے کے لیے بند کیا جاتا ہے۔ جب خشک خلیہ رو دیتا ہے تو Zn تکسید ہو کر Zn²⁺ آئن بنتا ہے اور Zn کے برتن پر الیکٹران چھوڑ دیتا ہے۔ الیکٹران بیرونی سرکٹ سے گریفائٹ کیتھوڈ تک جاتے ہیں جہاں NH₄⁺ آئن الیکٹران لے کر کیتھوڈ پر NH₃ خارج کرتے ہیں۔ کیتھوڈ پر پیدا ہونے والی NH₃ Zn²⁺ آئنوں سے تعامل کر کے ایک پیچیدہ آئن بناتی ہے۔ دونوں الیکٹروڈز پر ہونے والے ریڈاکس تعاملات درج ذیل ہیں۔','لکه څنګه چې تاسو په تېر ټولګي کې لوستي، د حجرې ظرف د Zn جوړ دی چې د انوډ په توګه عمل کوي. ظرف د سوري لرونکي کاغذ طبقه لري چې انوډ له داخلي موادو جلا کوي. د حجرې په مرکز کې د ګرافایټ ډنډه د کیتوډ په توګه عمل کوي. الکترولایټ د NH₄Cl، MnO₂، ZnCl₂ او پوډر شوي کاربن لنده مخلوط دی. وچه حجره د رطوبت د تبخیر د مخنیوي لپاره تړل کېږي. کله چې وچه حجره جریان ورکوي نو Zn اکسیډیز کېږي چې Zn²⁺ آیونونه جوړوي او د Zn په ظرف کې الکترونونه پرېږدي. الکترونونه د بهرني سرکټ له لارې ګرافایټ کیتوډ ته ځي چېرته چې NH₄⁺ آیونونه الکترونونه اخلي او په کیتوډ کې NH₃ خوشې کوي. په کیتوډ کې جوړ شوی NH₃ له Zn²⁺ آیونونو سره تعامل کوي چې پیچلی آیون جوړوي. په دواړو الکترودونو کې پېښېدونکي ریډاکس تعاملات په لاندې ډول دي.')
add(s,'an','At anode (Oxidation)','اینوڈ پر (تکسید)','په انوډ کې (اکسیډیشن)')
add(s,'ca','At cathode (Reduction)','کیتھوڈ پر (تخفیف)','په کیتوډ کې (ریډکشن)')
add(s,'nr','Net reaction','خالص تعامل','خالص تعامل')
add(s,'b2','This is irreversible because Zn and NH₄⁺ are consumed during the process of working and cannot be reversed back to their initial states by the application of the external electrical potential.','یہ ناقابلِ واپسی ہے کیونکہ Zn اور NH₄⁺ کام کرنے کے عمل کے دوران صرف ہو جاتے ہیں اور بیرونی برقی پوٹینشل لگانے سے اپنی ابتدائی حالت میں واپس نہیں لائے جا سکتے۔','دا بیرته نه راګرځېدونکی دی ځکه چې Zn او NH₄⁺ د کار کولو د بهیر پر مهال مصرفېږي او د بهرني برېښنایي پوټنشیل په کارولو سره خپلو لومړنیو حالتونو ته نشي بیرته راګرځېدای.')
d=('<ellipse cx="85" cy="25" rx="60" ry="14" fill="#c8302a" stroke="#333"/><path d="M25 25 V190 Q85 215 145 190 V25" fill="#3a8ab8" stroke="#333" stroke-width="2"/><path d="M40 35 V180 Q85 200 130 180 V35 Q85 50 40 35" fill="#e8d030" stroke="#555"/><rect x="72" y="5" width="20" height="170" fill="#222"/>'
 +tx(160,70,'Anode',10,'start',700)+tx(160,82,'(Zinc Inner Case)',10,'start')+tx(160,115,'Cathode',10,'start',700)+tx(160,127,'(Graphite Rod)',10,'start')+tx(160,160,'Electrolytic paste of',10,'start')+tx(160,172,'MnO₂ of NH₄Cl',10,'start')+tx(160,184,'and Carbon',10,'start')+tx(130,228,'Fig. 12.8: The Dry Cell',12,'middle',700,'#a02040'))
s['figures']=[dict(id='chem11-p384-fig128',svg=svg(290,240,'Cutaway of a dry cell showing the zinc inner case as anode, the central graphite rod as cathode and the electrolytic paste',d),caption='Fig. 12.8: The Dry Cell',captionUrdu='شکل 12.8: خشک خلیہ',captionPashto='شکل 12.8: وچه حجره',labels=[lab('Anode (Zinc Inner Case)','اینوڈ (زنک کا اندرونی خول)','انوډ (د زنک داخلي قاب)'),lab('Cathode (Graphite Rod)','کیتھوڈ (گریفائٹ سلاخ)','کیتوډ (ګرافایټ ډنډه)'),lab('Electrolytic paste of MnO₂ of NH₄Cl and Carbon','MnO₂، NH₄Cl اور کاربن کا برق پاش پیسٹ','د MnO₂، NH₄Cl او کاربن الکترولایټیک پیسټ')],sourceGap=dict(note='Photo-style dry-cell cutaway redrawn as a schematic; layers simplified. The printed label reads "MnO₂ of NH₄Cl" and is kept as printed.'))]
F.p('h','a1','t1','a2','t2','a3','t3','a4','t4','a5','p1','p2','b1'); F.fg(0)
F.p('an')
F.e('r1',r'\mathrm{Zn\longrightarrow Zn^{2+}+2e^-}','Zn → Zn²⁺ + 2e⁻')
F.p('ca')
F.e('r2',r'2\mathrm{MnO_2+2NH_4^++2e^-\longrightarrow Mn_2O_3+2NH_3+H_2O}','2MnO₂ + 2NH₄⁺ + 2e⁻ → Mn₂O₃ + 2NH₃ + H₂O')
F.p('nr')
F.e('r3',r'\mathrm{Zn+2MnO_2+2NH_4^+\longrightarrow Zn^{2+}+Mn_2O_3+2NH_3+H_2O}','Zn + 2MnO₂ + 2NH₄⁺ → Zn²⁺ + Mn₂O₃ + 2NH₃ + H₂O')
F.p('b2')
F.done()
s['sourceNote']='Printed folio 379. The scan is skewed with left-edge curl; the lines in the lower-left of the b1 paragraph are clipped at their starts ("to form a complex ion…") but read from context. Printed notation kept ("NH⁺₄", "MnO₂ of NH₄Cl" in the figure label). Fig. 12.8 is redrawn as a schematic. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; left-edge clipping; figure redrawn.')
s['vocabulary']={'dry cell':{'ur':'خشک خلیہ','ps':'وچه حجره'},'primary battery':{'ur':'ابتدائی بیٹری','ps':'لومړنۍ بیټرۍ'},'secondary battery':{'ur':'ثانوی بیٹری','ps':'دوهمي بیټرۍ'}}
save(s)
