"""Sequential source correction for PDF page 38 of Class 12 Physics."""
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def svg(body,label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:520px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>')

PTC=[
 pair('POSITIVE TEMPERATURE COEFFICIENT (PTC) THERMISTOR:', 'مثبت درجۂ حرارت ضریب (PTC) تھرمسٹر:', 'د تودوخې د مثبت ضریب (PTC) ترمېسټر:'),
 pair('PTC thermistor is generally used for fuse purpose. The resistance of PTC thermistor increases with increase in temperature and when temperature decreases, its resistance decreases. One of the properties of PTC thermistors is that when an excessively large current flows, they generate heat by themselves and become highly resistive. With this property, they are used as overcurrent protection devices. They are used as timing devices in televisions. They are also used as heater in automotive industry to provide additional heat inside cabin with diesel engine or to heat diesel in cold climatic conditions before engine injection.',
      'PTC تھرمسٹر عموماً فیوز کے طور پر استعمال ہوتا ہے۔ درجۂ حرارت بڑھنے پر PTC تھرمسٹر کی مزاحمت بڑھتی ہے اور درجۂ حرارت کم ہونے پر مزاحمت کم ہوتی ہے۔ PTC تھرمسٹروں کی ایک خاصیت یہ ہے کہ جب بہت زیادہ برقی رو گزرتی ہے تو وہ خود حرارت پیدا کرتے ہیں اور ان کی مزاحمت بہت زیادہ ہو جاتی ہے۔ اس خاصیت کے باعث انہیں زائد برقی رو سے تحفظ کے آلات کے طور پر استعمال کیا جاتا ہے۔ ٹیلی وژن میں انہیں ٹائمنگ آلات کے طور پر بھی استعمال کیا جاتا ہے۔ آٹوموٹیو صنعت میں انہیں ڈیزل انجن والی گاڑی کے کیبن میں اضافی حرارت دینے یا سرد موسم میں انجن میں انجیکشن سے پہلے ڈیزل گرم کرنے کے لیے بھی ہیٹر کے طور پر استعمال کیا جاتا ہے۔',
      'PTC ترمېسټر عموماً د فیوز په توګه کارول کېږي. د تودوخې په لوړېدو د PTC ترمېسټر مقاومت زیاتېږي او د تودوخې په کمېدو مقاومت یې کمېږي. د PTC ترمېسټرونو یوه ځانګړنه دا ده چې د ډېر لوی جریان په تېرېدو خپله تودوخه تولیدوي او ډېر لوړ مقاومت پیدا کوي. له همدې ځانګړنې سره د اضافي جریان د ساتنې د وسیلو په توګه کارول کېږي. په ټلوېزیونونو کې د وخت ټاکلو د وسیلو په توګه هم کارول کېږي. د موټرو په صنعت کې د ډیزلي انجن د موټر د کابین د اضافي تودوخې یا په سړه هوا کې انجن ته له تزریق مخکې د ډیزلو د تودولو لپاره د هیټر په توګه هم کارول کېږي.'),
]
EMF=[
 pair('12.7 ELECTROMOTIVE FORCE', '12.7 برقی محرکہ قوت', '12.7 برېښنايي محرکه قوه'),
 pair('An external energy source is required by most electrical circuits to move charge through the circuit. The circuit therefore must include a device that maintains a potential difference between two points in the circuit, just as a circulating fluid requires as analogous device (pump).',
      'زیادہ تر برقی سرکٹس میں چارج کو سرکٹ میں حرکت دینے کے لیے بیرونی توانائی کا ذریعہ درکار ہوتا ہے۔ اس لیے سرکٹ میں ایسا آلہ ہونا چاہیے جو سرکٹ کے دو نقاط کے درمیان پوٹینشل فرق برقرار رکھے، بالکل اسی طرح جیسے گردش کرتے سیال کے لیے مماثل آلہ (پمپ) درکار ہوتا ہے۔',
      'په ډېرو برېښنايي مدارونو کې د مدار له لارې د چارج د خوځولو لپاره د بهرنۍ انرژۍ سرچینې ته اړتیا وي. نو مدار باید داسې وسیله ولري چې د مدار د دوو نقطو ترمنځ پوتنشیالي توپیر وساتي، لکه څنګه چې ګرځېدونکی مایع ورته وسیلې (پمپ) ته اړتیا لري.'),
 pair('Such a device which converts non-electrical energy into electrical energy is called a source of electromotive force (emf).',
      'هغه آله چې غیر برقی توانائی کو برقی توانائی میں تبدیل کرتی ہے، برقی محرکہ قوت (emf) کا منبع کہلاتی ہے۔',
      'هغه وسیله چې غیربرېښنايي انرژي په برېښنايي انرژۍ بدلوي، د برېښنايي محرکې قوې (emf) سرچینه بلل کېږي.'),
 pair('This reminds us a pump, which can cause water to move from a place of low gravitational potential to a place of high potential. Figure (12.8) shows the e.m.f. source ε, connected to a resistor R. It maintains its upper terminal at a high potential and its lower terminal at a low potential, as indicated by the + and - signs. In the external circuit positive charge carriers would be driven in the direction shown by the arrows marked I.',
      'یہ ہمیں پمپ کی یاد دلاتا ہے، جو پانی کو کم ثقلی پوٹینشل سے زیادہ پوٹینشل کی جگہ تک لے جا سکتا ہے۔ شکل (12.8) میں برقی محرکہ قوت ε کا منبع مزاحم R سے منسلک دکھایا گیا ہے۔ یہ اپنا اوپری سرا بلند پوٹینشل اور نچلا سرا کم پوٹینشل پر رکھتا ہے، جیسا کہ + اور − کی علامتیں بتاتی ہیں۔ بیرونی سرکٹ میں مثبت بار بردار I سے نشان زد تیروں کی سمت میں چلیں گے۔',
      'دا د پمپ یاد راکوي، چې اوبه له ټیټ جاذبوي پوتنشیال څخه لوړ پوتنشیال ته رسولای شي. (12.8 شکل) د ε برېښنايي محرکې قوې سرچینه له R مقاومت سره نښلول شوې ښيي. د + او − نښو له مخې، سرچینه خپل پورتنی ترمینل په لوړ او ښکته ترمینل په ټیټ پوتنشیال ساتي. په بهرني مدار کې مثبت چارج لرونکي د I په غشو ښودل شوي لوري ته خوځېږي.'),
]
SOURCES=[
 pair('SOURCES OF e.m.f.', 'برقی محرکہ قوت کے ذرائع', 'د برېښنايي محرکې قوې سرچینې'),
 pair('The work done by emf on charge carriers in its interior must be derived from a source of energy. There are many sources of e.m.f. A few examples are',
      'منبع کے اندر بار برداروں پر برقی محرکہ قوت کا کیا گیا کام کسی توانائی کے ذریعے سے حاصل ہونا چاہیے۔ برقی محرکہ قوت کے بہت سے ذرائع ہیں۔ چند مثالیں یہ ہیں:',
      'د سرچینې دننه پر چارج لرونکو د محرکې قوې ترسره شوی کار باید د انرژۍ له یوې سرچینې څخه وي. د برېښنايي محرکې قوې ډېرې سرچینې شته. څو بېلګې یې دا دي:'),
 pair('1. Batteries or cells convert chemical energy into electrical energy.', '1. بیٹریاں یا سیل کیمیائی توانائی کو برقی توانائی میں تبدیل کرتے ہیں۔', '1. بیټرۍ یا حجرې کیمیاوي انرژي په برېښنايي انرژۍ بدلوي.'),
 pair('2. Electrical generators convert mechanical energy into electrical energy.', '2. برقی جنریٹر میکانی توانائی کو برقی توانائی میں تبدیل کرتے ہیں۔', '2. برېښنايي جنراتورونه میخانیکي انرژي په برېښنايي انرژۍ بدلوي.'),
 pair('3. Thermocouples convert heat energy into electrical energy.', '3. تھرموکپل حرارتی توانائی کو برقی توانائی میں تبدیل کرتے ہیں۔', '3. ترموکوپلونه حرارتي انرژي په برېښنايي انرژۍ بدلوي.'),
 pair('4. Radiant (a solar cell) converts sunlight directly into electrical energy.', '4. تابکاری توانائی (سولر سیل) سورج کی روشنی کو براہِ راست برقی توانائی میں تبدیل کرتی ہے۔', '4. وړانګیزه انرژي (لمریزه حجره) د لمر رڼا نېغ په نېغه په برېښنايي انرژۍ بدلوي.'),
]
DEFINITION=[
 pair('We define e.m.f. E of a source equal to the work done in carrying 1 coulomb of charge through the source.',
      'کسی منبع کی برقی محرکہ قوت E کو اس کام کے برابر تعریف کرتے ہیں جو منبع میں سے 1 کولمب چارج لے جانے میں کیا جائے۔',
      'د یوې سرچینې برېښنايي محرکه قوه E د هغه کار سره برابره تعریفوو چې د سرچینې له لارې د 1 کولمب چارج په لېږدولو کې ترسره کېږي.'),
 pair('Suppose q coulombs require an amount of work W joule to be transported through the source then ε in volts is given by',
      'فرض کریں کہ منبع میں سے q کولمب چارج منتقل کرنے کے لیے W جول کام درکار ہو، تو وولٹ میں ε یہ ہے:',
      'فرض کړئ چې د q کولمب چارج د سرچینې له لارې د لېږدولو لپاره W جول کار ته اړتیا وي؛ نو په ولټ کې ε داسې ده:'),
 pair(r'\(\epsilon=\frac{W}{q}\) ...(12.11)',r'\(\epsilon=\frac{W}{q}\) ...(12.11)',r'\(\epsilon=\frac{W}{q}\) ...(12.11)'),
 pair('The potential at the ends of a terminal of a battery when circuit is open is also called e.m.f. The unit of e.m.f. is the joule/coulomb, which is the volt (abbreviation V): 1 volt = 1 joule/coulomb.',
      'جب سرکٹ کھلا ہو تو بیٹری کے ٹرمینل کے سروں پر پوٹینشل کو بھی برقی محرکہ قوت کہتے ہیں۔ برقی محرکہ قوت کی اکائی جول/کولمب ہے، جو وولٹ (اختصار V) ہے: 1 وولٹ = 1 جول/کولمب۔',
      'کله چې مدار پرانیستی وي، د بیټرۍ د ترمینلونو د پایونو پوتنشیال ته هم برېښنايي محرکه قوه ویل کېږي. د محرکې قوې واحد جول/کولمب دی چې ولټ (لنډیز V) دی: 1 ولټ = 1 جول/کولمب.'),
]
INTERNAL=[
 pair('12.8 INTERNAL RESISTANCE OF A SUPPLY', '12.8 منبع کی اندرونی مزاحمت', '12.8 د برېښنايي سرچینې دننی مقاومت'),
 pair('All supplies (e.g. a cell) must have some internal resistance, however small. When the cell is delivering no current i.e. no load, the potential difference across terminals will be equal to e.m.f. (ε) of cell. When some load resistance ‘R’ is connected across the terminals of the cell, the current I starts flowing in the circuit Figure (12.9). This current causes a voltage drop across internal resistance r of the cell so that terminal voltage V available will be less than ε. The relationship between ε and V can be easily established.',
      'تمام برقی ذرائع (مثلاً سیل) میں کچھ نہ کچھ اندرونی مزاحمت ہوتی ہے، خواہ بہت کم ہو۔ جب سیل کوئی برقی رو نہیں دے رہا ہو، یعنی لوڈ نہ ہو، تو ٹرمینلز کے درمیان پوٹینشل فرق سیل کی برقی محرکہ قوت (ε) کے برابر ہوتا ہے۔ جب سیل کے ٹرمینلز کے پار کوئی لوڈ مزاحمت R جوڑی جائے تو سرکٹ میں برقی رو I بہنے لگتی ہے (شکل 12.9)۔ یہ برقی رو سیل کی اندرونی مزاحمت r پر وولٹیج ڈراپ پیدا کرتی ہے، اس لیے دستیاب ٹرمینل وولٹیج V، ε سے کم ہو گا۔ ε اور V کے درمیان تعلق آسانی سے قائم کیا جا سکتا ہے۔',
      'ټولې برېښنايي سرچینې (لکه حجره) یو څه دننی مقاومت لري، که څه هم ډېر لږ وي. کله چې حجره جریان نه ورکوي، یعنې بار نه وي، د ترمینلونو ترمنځ پوتنشیالي توپیر د حجرې له برېښنايي محرکې قوې (ε) سره برابر وي. کله چې د حجرې د ترمینلونو ترمنځ د R بار مقاومت ونښلول شي، په مدار کې I جریان پیلېږي (12.9 شکل). دا جریان د حجرې پر r دنني مقاومت د ولتاژ لوېدنه رامنځته کوي، نو شته ترمینلي ولتاژ V له ε څخه کم وي. د ε او V ترمنځ اړیکه په اسانۍ موندل کېدای شي.'),
]
FYI=[
 pair('Just as a water fountain requires a pump, an electric circuit requires a source of electromotive force to sustain a steady current. In an electronic circuit there must be a device somewhere in the loop that acts like the water pump in a water fountain. In this device a charge travels uphill’s from lower to higher potential energy even though the electrostatic force is trying to push it from higher to lower potential energy. The direction of current in such a device is from lower to higher potential, just the opposite of what happens in an ordinary conductor. The influence that makes current flow from lower to higher potential is called electromotive force.',
      'جس طرح پانی کے فوارے کو پمپ درکار ہوتا ہے، اسی طرح مسلسل برقی رو برقرار رکھنے کے لیے برقی سرکٹ کو برقی محرکہ قوت کے منبع کی ضرورت ہوتی ہے۔ برقی سرکٹ کے حلقے میں کہیں ایسا آلہ ہونا چاہیے جو فوارے کے پمپ جیسا کام کرے۔ اس آلے میں چارج کم پوٹینشل توانائی سے زیادہ پوٹینشل توانائی کی طرف اوپر جاتا ہے، اگرچہ برقی ساکن قوت اسے زیادہ سے کم پوٹینشل توانائی کی طرف دھکیلنے کی کوشش کرتی ہے۔ ایسے آلے میں برقی رو کی سمت کم سے زیادہ پوٹینشل کی طرف ہوتی ہے، جو عام موصل میں ہونے والی سمت کے بالکل الٹ ہے۔ جو اثر برقی رو کو کم سے زیادہ پوٹینشل کی طرف بہاتا ہے اسے برقی محرکہ قوت کہتے ہیں۔',
      'لکه څنګه چې د اوبو چوترې ته پمپ پکار دی، برېښنايي مدار هم د ثابت جریان د ساتلو لپاره د برېښنايي محرکې قوې سرچینې ته اړتیا لري. په برېښنايي مدار کې باید په کړۍ کې داسې وسیله وي چې د اوبو د چوترې د پمپ په څېر کار وکړي. په دې وسیله کې چارج له ټیټې پوتنشیالي انرژۍ څخه لوړې ته پورته ځي، که څه هم الکتروستاتیکه قوه یې له لوړې څخه ټیټې پوتنشیالي انرژۍ ته ټېل وهي. په داسې وسیله کې د جریان لوری له ټیټ پوتنشیال څخه لوړ ته وي، چې په عادي هادي کې د جریان د لوري برعکس دی. هغه اغېز چې جریان له ټیټ څخه لوړ پوتنشیال ته بهوي، برېښنايي محرکه قوه بلل کېږي.'),
]

def make(identity,title,printed,pairs,layout,titles,pages,visual=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':38,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[{'pdfPage':38,'printedPage':n,'sourcePdf':SOURCE} for n in pages]
 if visual:s.update(visual);s['content']+=visual['diagramSvg']
 return r,s

def emf_svg(lang):
 L={'en':('emf source','resistor','positive charge flow I','FIGURE 12.8'), 'ur':('برقی محرکہ قوت کا منبع','مزاحم','مثبت بار کا بہاؤ I','شکل 12.8'), 'ps':('د محرکې قوې سرچینه','مقاومت','د مثبت چارج جریان I','12.8 شکل')}[lang]
 b=('<path d="M70 70H175M205 70H430V160H70V70" fill="none" stroke="#334155" stroke-width="3"/><path d="M160 48V92M176 58V82" stroke="#2563eb" stroke-width="4"/><path d="M176 70H205" stroke="#334155" stroke-width="3"/><path d="M285 58l12 12-12 12 12 12" fill="none" stroke="#f59e0b" stroke-width="3"/><circle cx="290" cy="70" r="22" fill="none" stroke="#334155" stroke-width="2"/><path d="M230 155H360" stroke="#16a34a" stroke-width="2"/><path d="M350 149l12 6-12 6" fill="#16a34a"/><text x="144" y="42" font-size="15">−</text><text x="174" y="42" font-size="15">+</text><text x="148" y="112" font-size="15">ε</text><text x="280" y="117" font-size="15">R</text>')
 b+=f'<text x="35" y="193" font-size="13">{escape(L[0])}</text><text x="365" y="142" font-size="13">{escape(L[1])}</text><text x="225" y="185" font-size="13">{escape(L[2])}</text><text x="345" y="28" font-size="15">{escape(L[3])}</text>'
 return svg(b,L[3])
def pump_svg(lang):
 L={'en':('water fountain','pump','low potential','high potential','FYI'), 'ur':('پانی کا فوارہ','پمپ','کم پوٹینشل','زیادہ پوٹینشل','معلومات'), 'ps':('د اوبو چوتره','پمپ','ټیټ پوتنشیال','لوړ پوتنشیال','پوه شئ')}[lang]
 b=('<path d="M70 165H440M125 165V130Q125 105 150 105H190Q210 105 210 130V165M145 105V78H190V105" fill="#bae6fd" stroke="#334155" stroke-width="3"/><path d="M167 77C145 55 180 42 167 25M190 77C215 56 180 43 195 25" fill="none" stroke="#0ea5e9" stroke-width="3"/><path d="M270 160V72H370V160" fill="none" stroke="#334155" stroke-width="3"/><path d="M292 128V91M322 128V91M352 128V91" stroke="#2563eb" stroke-width="4"/><path d="M286 96l6-10 6 10M316 96l6-10 6 10M346 96l6-10 6 10" fill="#2563eb"/>')
 b+=f'<text x="92" y="197" font-size="13">{escape(L[0])}</text><text x="138" y="72" font-size="13">{escape(L[1])}</text><text x="260" y="57" font-size="13">{escape(L[2])}</text><text x="360" y="57" font-size="13">{escape(L[3])}</text><text x="25" y="28" font-size="14">{escape(L[4])}</text>'
 return svg(b,L[4])

if __name__=='__main__':
 p=make('phys12-unit12-ptc66','PTC thermistor',66,PTC,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]}],('PTC تھرمسٹر','PTC ترمېسټر'),[66])
 e=make('phys12-unit12-emf-source66','12.7 Electromotive force and source',66,EMF,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'visual'}],('12.7 برقی محرکہ قوت اور منبع','12.7 برېښنايي محرکه قوه او سرچینه'),[66],{'diagramSvg':emf_svg('en'),'diagramSvgUrdu':emf_svg('ur'),'diagramSvgPashto':emf_svg('ps')})
 sr_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'list','indices':[2,3,4,5]}]
 sr=make('phys12-unit12-emf-sources66','Sources of electromotive force',66,SOURCES,sr_layout,('برقی محرکہ قوت کے ذرائع','د برېښنايي محرکې قوې سرچینې'),[66])
 d=make('phys12-unit12-emf-definition67','Definition and unit of electromotive force',67,DEFINITION,[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]}],('برقی محرکہ قوت کی تعریف اور اکائی','د برېښنايي محرکې قوې تعریف او واحد'),[67])
 i=make('phys12-unit12-internal-resistance-intro67','12.8 Internal resistance — introduction',67,INTERNAL,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'}],('12.8 اندرونی مزاحمت — تعارف','12.8 دننی مقاومت — سریزه'),[67],{'diagramSvg':pump_svg('en'),'diagramSvgUrdu':pump_svg('ur'),'diagramSvgPashto':pump_svg('ps')})
 f=make('phys12-unit12-emf-fyi67','FYI — electromotive force analogy',67,FYI,[{'type':'paragraph','indices':[0]}],('معلومات — برقی محرکہ قوت کی مثال','پوه شئ — د برېښنايي محرکې قوې بېلګه'),[67])
 records=[x[0] for x in (p,e,sr,d,i,f)];sections=[x[1] for x in (p,e,sr,d,i,f)]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,retire_sections=['12.5'],
  formulas=[{'id':'phys12-unit12-eq-12.11','name':'Electromotive force','number':'12.11','formula':DEFINITION[2][0],'latex':r'\epsilon=\frac{W}{q}','sourceReferences':[{'pdfPage':38,'printedPage':67,'sourcePdf':SOURCE}]}],
  definitions=[{'term':'Electromotive force','definition':DEFINITION[0][0]+' '+DEFINITION[1][0]+' '+DEFINITION[2][0]+' '+DEFINITION[3][0],
    'definitionUrdu':DEFINITION[0][1]+' '+DEFINITION[1][1]+' '+DEFINITION[2][1]+' '+DEFINITION[3][1],
    'definitionPashto':DEFINITION[0][2]+' '+DEFINITION[1][2]+' '+DEFINITION[2][2]+' '+DEFINITION[3][2],
    'sourceReferences':[{'pdfPage':38,'printedPage':67,'sourcePdf':SOURCE}]}])
 checkpoint(38,'corrected_verified',[x['id'] for x in records],
  'Rendered and visually inspected PDF page 38 at source resolution, printed pages 66–67. Compared PTC thermistor text, the e.m.f. introduction and Figure 12.8, all four listed e.m.f. sources, the definition and Eq. 12.11, unit statement, internal-resistance introduction and complete FYI panel. Rebuilt the source and pump analogy visuals as translated inline SVG; preserved the four numbered source examples and aligned Urdu/Pashto paragraph records. Synced Eq. 12.11 and the e.m.f. definition; retired legacy 12.5 after confirming page 65–67 coverage.', printed_pages=[66,67],chapter_number=12)
