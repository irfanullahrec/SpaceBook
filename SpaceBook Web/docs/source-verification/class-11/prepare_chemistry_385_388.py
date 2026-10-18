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

# ---------- 385 ----------
s=mk(385,'Secondary Batteries · The Lead Storage Battery · Figure 12.9','ثانوی بیٹریاں · سیسہ ذخیرہ بیٹری · شکل 12.9','دوهمي بیټرۍ · د سرب ذخیره کوونکې بیټرۍ · شکل 12.9','lead-storage-battery')
F=Flow(s)
add(s,'h1','(ii) Secondary Batteries','(ii) ثانوی بیٹریاں','(ii) دوهمي بیټرۍ',kind='heading')
add(s,'h2','The Lead Storage Battery','سیسہ ذخیرہ بیٹری','د سرب ذخیره کوونکې بیټرۍ',kind='heading')
add(s,'a1',f'The lead storage battery commonly used in automobiles and generators. It is a combination of six voltaic cells of the same kind, arranged in series with the anode of one cell connected to the cathode of the other. The anodes are Pb plates while the cathodes are made of lead dioxide (PbO₂). Both the anode and cathode are immersed in an aqueous solution of sulfuric acid, which acts as the electrolyte (Fig.12.9). When the anodes and cathodes are connected, the current flows and the following reactions take place.','سیسہ ذخیرہ بیٹری عام طور پر گاڑیوں اور جنریٹروں میں استعمال ہوتی ہے۔ یہ ایک ہی قسم کے چھ وولٹائی خلیوں کا مجموعہ ہے جو سلسلہ وار ترتیب میں ہوتے ہیں اور ایک خلیے کا اینوڈ دوسرے کے کیتھوڈ سے جڑا ہوتا ہے۔ اینوڈ Pb کی پلیٹیں ہیں جبکہ کیتھوڈ لیڈ ڈائی آکسائیڈ (PbO₂) کے بنے ہوتے ہیں۔ اینوڈ اور کیتھوڈ دونوں سلفیورک ایسڈ کے آبی محلول میں ڈوبے ہوتے ہیں جو برق پاش کا کام کرتا ہے (شکل 12.9)۔ جب اینوڈز اور کیتھوڈز کو جوڑا جاتا ہے تو رو بہتی ہے اور درج ذیل تعاملات ہوتے ہیں۔','د سرب ذخیره کوونکې بیټرۍ په عادي ډول په موټرو او جنریټرونو کې کارول کېږي. دا د یو ډول شپږ وولټایک حجرو ترکیب دی چې په لړ کې ترتیب شوي او د یوې حجرې انوډ د بلې له کیتوډ سره وصل وي. انوډونه د Pb پلیټونه دي پداسې حال کې چې کیتوډونه د سرب ډای اکسایډ (PbO₂) څخه جوړ دي. انوډ او کیتوډ دواړه د سلفیوریک اسید په اوبیز محلول کې ډوب وي چې د الکترولایټ په توګه عمل کوي (12.9 شکل). کله چې انوډونه او کیتوډونه وصل شي نو جریان بهېږي او لاندې تعاملات پېښېږي.')
add(s,'an','At Anode','اینوڈ پر','په انوډ کې')
add(s,'ca','At Cathode','کیتھوڈ پر','په کیتوډ کې')
add(s,'nr','Net Reaction','خالص تعامل','خالص تعامل')
add(s,'a2','When the cell works insoluble PbSO₄ goes on depositing on both the electrodes, H₂SO₄ is consumed and water is formed.','جب خلیہ کام کرتا ہے تو ناحل پذیر PbSO₄ دونوں الیکٹروڈز پر جمع ہوتا رہتا ہے، H₂SO₄ صرف ہوتا ہے اور پانی بنتا ہے۔','کله چې حجره کار کوي نو نه منحلېدونکی PbSO₄ په دواړو الکترودونو کې ترسبېږي، H₂SO₄ مصرفېږي او اوبه جوړېږي.')
add(s,'b1',f'It is a reversible battery. If, during recharging, the current from an external source is allowed to flow in the opposite direction all the above chemical changes are reversed and converts lead sulphate back to lead and lead dioxide on the respective electrodes. During recharging the negative electrode is connected to the negative terminal of the direct current (DC) source and positive electrode to the positive terminal of DC source. The reactions are;','یہ ایک الٹ پذیر بیٹری ہے۔ اگر دوبارہ چارج کرنے کے دوران بیرونی ذریعے سے رو کو مخالف سمت میں بہنے دیا جائے تو مندرجہ بالا تمام کیمیائی تبدیلیاں الٹ جاتی ہیں اور لیڈ سلفیٹ متعلقہ الیکٹروڈز پر واپس سیسہ اور لیڈ ڈائی آکسائیڈ میں تبدیل ہو جاتا ہے۔ دوبارہ چارج کرنے کے دوران منفی الیکٹروڈ ڈائریکٹ کرنٹ (DC) ذریعے کے منفی سرے سے اور مثبت الیکٹروڈ DC ذریعے کے مثبت سرے سے جڑا ہوتا ہے۔ تعاملات یہ ہیں؛','دا یوه بیرته راګرځېدونکې بیټرۍ ده. که د بیا چارج کولو پر مهال د بهرنۍ سرچینې جریان ته اجازه ورکړل شي چې مخالف لوري ته وبهېږي نو پورتني ټول کیمیاوي بدلونونه سمکې کېږي او سرب سلفیټ په اړوندو الکترودونو کې بیرته سرب او سرب ډای اکسایډ ته بدلوي. د بیا چارج کولو پر مهال منفي الکترود د مستقیم جریان (DC) سرچینې له منفي سرې سره او مثبت الکترود د DC سرچینې له مثبتې سرې سره وصل وي. تعاملات دا دي؛')
add(s,'neg','At negative electrode:','منفی الیکٹروڈ پر:','په منفي الکترود کې:')
add(s,'pos','At positive electrode:','مثبت الیکٹروڈ پر:','په مثبت الکترود کې:')
add(s,'nr2','Net reaction:','خالص تعامل:','خالص تعامل:')
add(s,'b2',f'Thus, Pb, PbO₂ and H₂SO₄ are reformed and the battery is again ready for{SO}',f'اس طرح Pb، PbO₂ اور H₂SO₄ دوبارہ بن جاتے ہیں اور بیٹری دوبارہ تیار ہو جاتی ہے {SO}',f'په دې توګه Pb، PbO₂ او H₂SO₄ بیا جوړېږي او بیټرۍ بیا چمتو کېږي {SO}')
d=('<rect x="10" y="40" width="240" height="140" fill="none"/><path d="M12 150 V190 H245 V150" fill="none" stroke="#222" stroke-width="2.5"/><path d="M70 190 V160 M160 190 V160" stroke="#222" stroke-width="2"/><rect x="14" y="140" width="231" height="50" fill="#bfdcf0" fill-opacity=".6"/>'
 '<rect x="22" y="55" width="9" height="130" fill="#e8943a" stroke="#555"/><rect x="62" y="55" width="9" height="130" fill="#2a8ec0" stroke="#555"/><rect x="95" y="62" width="9" height="125" fill="#999" stroke="#555"/><rect x="132" y="55" width="9" height="130" fill="#2a8ec0" stroke="#555"/><rect x="165" y="62" width="9" height="125" fill="#999" stroke="#555"/><rect x="215" y="55" width="9" height="130" fill="#2a8ec0" stroke="#555"/>'
 '<path d="M26 50 V30 H100 V55 M66 50 V40 H132 M140 40 V55 M220 50 V40 H170 V60" fill="none" stroke="#222" stroke-width="1.5"/><circle cx="125" cy="22" r="9" fill="#fff" stroke="#222"/>'+tx(125,26,'V',10,'middle',700)+tx(125,10,'Voltmeter',10)+tx(36,52,'Pb',10,'start')+tx(228,75,'PbO₂',10,'start')
 +'<path d="M300 85 L315 70 H390 V150 L375 170 H300 Z" fill="#2a8ec0" stroke="#223" stroke-width="2"/><path d="M315 70 L375 70 L390 85" fill="none" stroke="#223"/><rect x="300" y="85" width="75" height="85" fill="#3a6a9a" stroke="#223"/>'+''.join(f'<rect x="{x}" y="88" width="5" height="80" fill="#222"/>' for x in (305,320,335,350,365))+tx(295,72,'lead anode',10,'end')+tx(395,150,'PbO₂',10,'start')+tx(395,162,'Cathode',10,'start')+tx(215,215,'Fig: 12.9 Lead Storage Battery (internal and external)',12,'middle',700,'#a02040'))
s['figures']=[dict(id='chem11-p385-fig129',svg=svg(470,230,'Lead storage battery shown internally as cells in series with lead anodes and lead dioxide cathodes in sulfuric acid and externally as a battery case',d),caption='Fig: 12.9 Lead Storage Battery (internal and external)',captionUrdu='شکل 12.9 سیسہ ذخیرہ بیٹری (اندرونی اور بیرونی)',captionPashto='شکل 12.9 د سرب ذخیره کوونکې بیټرۍ (داخلي او بهرنۍ)',labels=[lab('Voltmeter','وولٹ میٹر','وولټ میټر'),lab('Pb','Pb','Pb'),lab('PbO₂','PbO₂','PbO₂'),lab('lead anode','سیسہ اینوڈ','د سرب انوډ'),lab('PbO₂ Cathode','PbO₂ کیتھوڈ','PbO₂ کیتوډ')],sourceGap=dict(note='Cell-series diagram and battery case illustration redrawn as a schematic; plate count and arrangement are simplified.'))]
F.p('h1','h2','a1','an')
F.e('r1',r'\mathrm{Pb(s)+H_2SO_4(aq)\longrightarrow PbSO_4(s)+2H^++2e^-}','Pb(s) + H₂SO₄(aq) → PbSO₄(s) + 2H⁺ + 2e⁻')
F.p('ca')
F.e('r2',r'\mathrm{PbO_2(s)+H_2SO_4(aq)+2H^++2e^-\longrightarrow PbSO_4(s)+2H_2O(l)}','PbO₂(s) + H₂SO₄(aq) + 2H⁺ + 2e⁻ → PbSO₄(s) + 2H₂O(l)')
F.p('nr')
F.e('r3',r'\mathrm{Pb(s)+PbO_2(s)+2H_2SO_4\longrightarrow 2PbSO_4(s)+2H_2O(l)}','Pb(s) + PbO₂(s) + 2H₂SO₄ → 2PbSO₄(s) + 2H₂O(l)')
F.p('a2'); F.fg(0); F.p('b1','neg')
F.e('r4',r'\mathrm{PbSO_{4(s)}+2e^-\longrightarrow Pb_{(s)}+SO_4^{2-}}\quad\text{(Reduction)}','PbSO₄(s) + 2e⁻ → Pb(s) + SO₄²⁻   (Reduction)')
F.p('pos')
F.e('r5',r'\mathrm{PbSO_{4(s)}+2H_2O\longrightarrow PbO_{2(s)}+4H^++SO_4^{2-}+2e^-}\quad\text{(Oxidation)}','PbSO₄(s) + 2H₂O → PbO₂(s) + 4H⁺ + SO₄²⁻ + 2e⁻   (Oxidation)')
F.p('nr2')
F.e('r6',r'2\mathrm{PbSO_{4(s)}+2H_2O\longrightarrow Pb_{(s)}+PbO_{2(s)}+2SO_4^{2-}+4H^+}','2PbSO₄(s) + 2H₂O → Pb(s) + PbO₂(s) + 2SO₄²⁻ + 4H⁺')
F.p('b2')
F.done()
s['sourceNote']='Printed folio 380. The scan is skewed with right-edge curl; right ends of the paragraph lines are partly clipped but readable, and the last line ends "ready for" and continues on the next page. The printed text has "PbO₂)." with the closing bracket as ")." Equations are shown as printed (the positive-electrode line shows 2H₂O on the left and an unbalanced charge; not corrected). The words "At negative electrode:" and "At positive electrode:" label the recharging reactions. Fig. 12.9 is redrawn as a schematic. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; right-edge curl; figure redrawn; sentence continues next page.')
s['vocabulary']={'lead storage battery':{'ur':'سیسہ ذخیرہ بیٹری','ps':'د سرب ذخیره کوونکې بیټرۍ'},'recharging':{'ur':'دوبارہ چارج کرنا','ps':'بیا چارج کول'}}
save(s)

# ---------- 386 ----------
s=mk(386,'Fuel Cells','ایندھن خلیے','د سونګ حجرې','fuel-cells')
F=Flow(s)
add(s,'a0','generating useful electricity.','مفید بجلی پیدا کرنے کے لیے۔','ګټوره برېښنا تولیدولو لپاره.')
add(s,'h','(iii) Fuel Cells','(iii) ایندھن خلیے','(iii) د سونګ حجرې',kind='heading')
add(s,'c1',f'A fuel cell is a primary cell of special type which converts chemical energy of fuel directly to electrical energy. The chemicals that produce electricity are constantly replaced as soon as they are consumed. Fuel cells differ from common batteries such that in these, electricity is produced from chemical fuels fed to them as needed, so that their operating life is unlimited. One of the most important fuel cell is the hydrogen/oxygen fuel cell. In this cell the negative terminal (anode) is porous graphite coated with nickel and the positive terminal (cathode) is porous graphite coated with nickel and nickel oxide. The nickel and nickel oxide act as catalyst on the surface of the terminal. Nickel can be replaced by platinum.','ایندھن خلیہ ایک خاص قسم کا ابتدائی خلیہ ہے جو ایندھن کی کیمیائی توانائی کو براہِ راست برقی توانائی میں تبدیل کرتا ہے۔ جو کیمیائی مادے بجلی پیدا کرتے ہیں وہ صرف ہوتے ہی مسلسل بدل دیے جاتے ہیں۔ ایندھن خلیے عام بیٹریوں سے اس طرح مختلف ہیں کہ ان میں ضرورت کے مطابق دیے گئے کیمیائی ایندھن سے بجلی پیدا ہوتی ہے، اس لیے ان کی کام کرنے کی عمر لامحدود ہوتی ہے۔ سب سے اہم ایندھن خلیوں میں سے ایک ہائیڈروجن/آکسیجن ایندھن خلیہ ہے۔ اس خلیے میں منفی سرا (اینوڈ) نکل چڑھا ہوا مسام دار گریفائٹ ہے اور مثبت سرا (کیتھوڈ) نکل اور نکل آکسائیڈ چڑھا ہوا مسام دار گریفائٹ ہے۔ نکل اور نکل آکسائیڈ سرے کی سطح پر اتپریرک کا کام کرتے ہیں۔ نکل کو پلاٹینم سے بدلا جا سکتا ہے۔','د سونګ حجره یو ځانګړی ډول لومړنۍ حجره ده چې د سونګ کیمیاوي انرژي مستقیماً په برېښنایي انرژي بدلوي. هغه کیمیاوي مواد چې برېښنا تولیدوي هماغه وخت چې مصرف شي په دوامداره توګه بدلېږي. د سونګ حجرې له عادي بیټریو څخه دې ډول توپیر لري چې په دوی کې برېښنا د اړتیا سره سم ورکړل شویو کیمیاوي سونګونو څخه تولیدېږي، نو د دوی د کار کولو عمر بې حده وي. یو له ډېرو مهمو سونګ حجرو څخه د هایدروجن/اکسیجن سونګ حجره ده. په دې حجره کې منفي سر (انوډ) د نکل پوښل شوی سوري لرونکی ګرافایټ دی او مثبت سر (کیتوډ) د نکل او نکل اکسایډ پوښل شوی سوري لرونکی ګرافایټ دی. نکل او نکل اکسایډ د سر په سطحه د کتالیست په توګه عمل کوي. نکل په پلاټینم بدلېدای شي.')
add(s,'c2','Hydrogen is passed into the negative compartment of the cell and oxygen into the positive compartment. Under pressure the gases diffuse through the porous graphite terminals into the warm potassium hydroxide solution located between the terminals. At the anode, hydrogen reacts with hydroxide ions from the warm KOH(aq) and electrons are released. Thus, the reaction','ہائیڈروجن کو خلیے کے منفی خانے میں اور آکسیجن کو مثبت خانے میں داخل کیا جاتا ہے۔ دباؤ کے تحت گیسیں مسام دار گریفائٹ سروں سے گزر کر سروں کے درمیان موجود گرم پوٹاشیم ہائیڈرو آکسائیڈ محلول میں پھیلتی ہیں۔ اینوڈ پر ہائیڈروجن گرم KOH(aq) سے ہائیڈرو آکسائیڈ آئنوں کے ساتھ تعامل کرتی ہے اور الیکٹران خارج ہوتے ہیں۔ اس طرح، تعامل','هایدروجن د حجرې منفي برخې ته او اکسیجن مثبتې برخې ته ننوېستل کېږي. په فشار لاندې ګازونه د سوري لرونکو ګرافایټ سرونو له لارې د سرونو ترمنځ ګرم پوتاشیم هایدروکسایډ محلول ته خپرېږي. په انوډ کې هایدروجن د ګرم KOH(aq) له هایدروکسایډ آیونونو سره تعامل کوي او الکترونونه خوشې کېږي. په دې توګه، تعامل')
add(s,'an','At anode','اینوڈ پر','په انوډ کې')
add(s,'or','Or','یا','یا')
add(s,'c3','At cathode oxygen and water take electron to form hydroxide ions.','کیتھوڈ پر آکسیجن اور پانی الیکٹران لے کر ہائیڈرو آکسائیڈ آئن بناتے ہیں۔','په کیتوډ کې اکسیجن او اوبه الکترونونه اخلي ترڅو هایدروکسایډ آیونونه جوړ کړي.')
add(s,'ca','At cathode','کیتھوڈ پر','په کیتوډ کې')
add(s,'c4','Adding above two equations we get the overall reaction as follows:','مندرجہ بالا دونوں مساواتوں کو جمع کرنے سے ہمیں مجموعی تعامل اس طرح ملتا ہے:','پورتنۍ دواړې معادلې یوځای کولو سره موږ ټولیز تعامل په لاندې ډول ترلاسه کوو:')
add(s,'ov','Overall reaction','مجموعی تعامل','ټولیز تعامل')
add(s,'c5','Fuel cells based on hydrogen and oxygen has a significant future as a power source for electric automobiles and in space vehicles. The cell is shown in Fig. 12.10. Electrodes are hollow tubes made of porous compressed carbon impregnated with platinum or nickel (increased surface area acts as a catalyst). The electrolyte is KOH. Hydrogen is oxidized at the anode giving electrons to the outer circuit while the electrons are accepted at the cathode where reduction occurs and in this way current flows. The cell products can be regenerated externally into fuel for returning to the cell.','ہائیڈروجن اور آکسیجن پر مبنی ایندھن خلیوں کا برقی گاڑیوں اور خلائی گاڑیوں میں بجلی کے ذریعے کے طور پر اہم مستقبل ہے۔ خلیہ شکل 12.10 میں دکھایا گیا ہے۔ الیکٹروڈز مسام دار دبے ہوئے کاربن کی بنی کھوکھلی نلیاں ہیں جن میں پلاٹینم یا نکل بھرا ہوتا ہے (بڑھا ہوا سطحی رقبہ اتپریرک کا کام کرتا ہے)۔ برق پاش KOH ہے۔ اینوڈ پر ہائیڈروجن تکسید ہو کر بیرونی سرکٹ کو الیکٹران دیتی ہے جبکہ کیتھوڈ پر جہاں تخفیف ہوتی ہے الیکٹران قبول کیے جاتے ہیں اور اس طرح رو بہتی ہے۔ خلیے کی مصنوعات کو بیرونی طور پر دوبارہ ایندھن میں تبدیل کر کے خلیے میں واپس بھیجا جا سکتا ہے۔','د هایدروجن او اکسیجن پر بنسټ د سونګ حجرې د برېښنایي موټرو او فضايي موټرو کې د برېښنا د سرچینې په توګه مهم راتلونکی لري. حجره په 12.10 شکل کې ښودل شوې. الکترودونه د سوري لرونکي فشرده کاربن جوړ شوې کوڅې نلونه دي چې په پلاټینم یا نکل مشبوع شوي (زیاته سطحي ساحه د کتالیست په توګه عمل کوي). الکترولایټ KOH دی. هایدروجن په انوډ کې اکسیډیز کېږي او بهرني سرکټ ته الکترونونه ورکوي پداسې حال کې چې الکترونونه په کیتوډ کې چېرته چې ریډکشن پېښېږي منل کېږي او په دې توګه جریان بهېږي. د حجرې محصولات په بهرني ډول بیرته سونګ ته بدلېدای شي ترڅو حجرې ته بیرته ولېږل شي.')
F.p('a0','h','c1','c2','an')
F.e('r1',r'2\mathrm{H_{2(g)}+4OH^-_{(aq)}\longrightarrow 4H_2O_{(l)}+4e^-}\quad\text{(Oxidation)}','2H₂(g) + 4OH⁻(aq) → 4H₂O(l) + 4e⁻   (Oxidation)')
F.p('or')
F.e('r2',r'2\mathrm{H_2\longrightarrow 4H^++4e^-}','2H₂ → 4H⁺ + 4e⁻')
F.p('c3','ca')
F.e('r3',r'\mathrm{O_{2(g)}+2H_2O_{(l)}+4e^-\longrightarrow 4OH^-_{(aq)}}\quad\text{(Reduction)}','O₂(g) + 2H₂O(l) + 4e⁻ → 4OH⁻(aq)   (Reduction)')
F.p('c4','ov')
F.e('r4',r'2\mathrm{H_{2(g)}+O_{2(g)}\longrightarrow 2H_2O_{(l)}}','2H₂(g) + O₂(g) → 2H₂O(l)')
F.p('c5')
F.done()
s['sourceNote']='Printed folio 381. The scan is skewed; the left edge is clipped at the first words of the c1 paragraph lines ("of fuel directly…", "constantly replaced…", "batteries such that…", "them as needed…", "important fuel cell…", "terminal (anode)…", "(cathode)…", "nickel oxide…", "by platinum") and the text is arranged from legible fragments and context; the c5 left clipping similarly ("Fig.", "impregnated", "The electrolyte", "outer circuit", "occurs", "externally"). The second anode equation is printed "2H₂ → 4H⁺ + 4e⁻" with the 2H label partly obscured. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan; left-edge clipping on first paragraph lines.')
s['vocabulary']={'fuel cell':{'ur':'ایندھن خلیہ','ps':'د سونګ حجره'},'catalyst':{'ur':'اتپریرک','ps':'کتالیست'}}
save(s)
