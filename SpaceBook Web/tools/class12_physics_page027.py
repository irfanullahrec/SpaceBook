from class12_source_review import upsert, section, checkpoint, sync_companions
from class12_physics_page013 import SOURCE, svg

DISCHARGE = [
 ('The capacitor will discharge itself through resistance R.', 'کیپیسٹر مزاحمت R کے ذریعے خود ڈسچارج ہوگا۔', 'کپاسیټر به د R مقاومت له لارې ډسچارج شي.'),
 (r'\(t=RC\quad q=q_0(0.368)\)',)*3,
 ('The time constant of an RC circuit is also the time during which the charge on the capacitor falls from its maximum value to 36.8%. The corresponding graph in Figure 11.30 shows that discharging begins at t=0 when q=q₀, and decreases gradually.', 'RC سرکٹ کا وقت کا مستقل وہ دورانیہ بھی ہے جس میں کیپیسٹر کا بار اپنی زیادہ سے زیادہ قدر سے گھٹ کر 36.8% رہ جاتا ہے۔ شکل 11.30 کا متعلقہ گراف دکھاتا ہے کہ ڈسچارج t=0 پر q=q₀ سے شروع ہوتا ہے اور بتدریج کم ہوتا جاتا ہے۔', 'د RC مدار د وخت ثابت هغه موده هم ده چې په ترڅ کې یې د کپاسیټر چارج له اعظمي کچې 36.8٪ ته راټیټېږي. د شکل 11.30 اړوند ګراف ښيي چې ډسچارج په t=0 کې له q=q₀ څخه پیلېږي او ورو ورو کمېږي.'),
 ('The charging and discharging of a capacitor has many applications. Capacitor discharge ignition (CDI) is a type of automotive electronic ignition system widely used in motorcycles, lawn mowers, chain saws, small engines, turbine-powered aircraft, and some cars. It can enhance the capability of a power supply and make the spark much stronger.', 'کیپیسٹر کو چارج اور ڈسچارج کرنے کے کئی استعمال ہیں۔ کیپیسٹر ڈسچارج اگنیشن (CDI) گاڑیوں کے برقی اگنیشن نظام کی ایک قسم ہے، جو موٹر سائیکلوں، لان کاٹنے والی مشینوں، چین سا، چھوٹے انجنوں، ٹربائن والے ہوائی جہازوں اور بعض کاروں میں عام ہے۔ یہ بجلی کے منبع کی صلاحیت بڑھا کر چنگاری کو زیادہ طاقتور بنا سکتا ہے۔', 'د کپاسیټر چارج او ډسچارج ډېرې کارونې لري. د کپاسیټر ډسچارج اېګنیشن (CDI) د موټرو د برېښنايي اېګنیشن یو ډول سیستم دی چې په موټرسایکلونو، د چمن پرېکوونکو ماشینونو، چین‌ساؤونو، کوچنیو انجنونو، توربین لرونکو الوتکو او ځینو موټرو کې کارېږي. دا د برېښنا سرچینې وړتیا لوړوي او سپرک پیاوړی کوي.'),
 ('TIP', 'اشارہ', 'اشاره'),
 ('Electronic flashguns for cameras have to be left for a short period of time between flashes. There is a capacitor inside that stores energy; it needs to be charged up again by the battery in the flashgun.', 'کیمرے کے الیکٹرانک فلیش کو چمکوں کے درمیان تھوڑا وقت دینا پڑتا ہے۔ اس کے اندر توانائی ذخیرہ کرنے والا کیپیسٹر ہوتا ہے، جسے فلیش کی بیٹری دوبارہ چارج کرتی ہے۔', 'د کمرې برېښنايي فلشونه باید د دوو ځلاوو ترمنځ لږ وخت پرېښودل شي. دننه یې د انرژۍ زېرمه کولو کپاسیټر وي، چې د فلش بېټرۍ یې بیا چارجوي.'),
]

KEYS = [
 ('Coulomb’s Law: the magnitude of the force between two point charges is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them.', 'د کولمب قانون: د دوو نقطوي بارونو ترمنځ د قوې مقدار د بارونو د مقدارونو له حاصل ضرب سره مستقیم او د واټن له مربع سره معکوس تناسب لري۔', 'د کولمب قانون: د دوو نقطوي چارجونو ترمنځ د قوې اندازه د چارجونو د مقدارونو له حاصل ضرب سره مستقیم او د واټن له مربع سره معکوس تناسب لري.'),
 ('Electric potential at any point: the work done in bringing a unit positive charge from infinity to that point without producing any acceleration.', 'کسی نقطے پر برقی پوٹینشل: اکائی مثبت بار کو لامحدود فاصلے سے اس نقطے تک لانے میں کیا گیا کام، بشرطیکہ کوئی تعجیل پیدا نہ ہو۔', 'په یوه نقطه کې برېښنايي پوتنشیال: د واحد مثبت چارج له لامحدود واټن څخه تر هغې نقطې د راوړلو کار، پرته له دې چې تعجیل رامنځته شي.'),
 ('Electric field: the region around a charge in which an electric test charge would experience an electric force.', 'برقی میدان: بار کے گرد وہ خطہ جہاں برقی آزمائشی بار برقی قوت محسوس کرے۔', 'برېښنايي میدان: د چارج شاوخوا هغه سیمه چې ازمېښتي برېښنايي چارج پکې برېښنايي قوه احساس کړي.'),
 (r'The electric flux \(\Phi\): the number of lines of force that pass through an area placed in the electric field. \(\Phi=E\cdot A=EA\cos\theta\). When area A is normal to the electric field E, the flux is maximum. When area A is parallel to E, the flux is minimum.', r'برقی فلوکس \(\Phi\): برقی میدان میں رکھی سطح سے گزرنے والی قوت کی لکیروں کی تعداد۔ \(\Phi=E\cdot A=EA\cos\theta\)۔ جب سطح A، میدان E پر عمود ہو تو فلوکس زیادہ سے زیادہ اور جب متوازی ہو تو کم سے کم ہوتا ہے۔', r'برېښنايي فلوکس \(\Phi\): په برېښنايي میدان کې د یوې سطحې له لارې د قوې د تېرېدونکو کرښو شمېر. \(\Phi=E\cdot A=EA\cos\theta\). کله چې A سطحه پر E میدان عموده وي، فلوکس اعظمي وي؛ او چې موازي وي، فلوکس لږ تر لږه وي.'),
 (r'Gauss’s law: the electric flux through any closed surface is \(\frac{1}{\epsilon_0}\) times the total charge enclosed by it.', r'گاؤس کا قانون: کسی بھی بند سطح سے گزرنے والا برقی فلوکس، اس کے اندر کے کل بار کا \(\frac{1}{\epsilon_0}\) گنا ہوتا ہے۔', r'د ګاوس قانون: له هرې تړلې سطحې څخه برېښنايي فلوکس د هغې دننه د ټول چارج \(\frac{1}{\epsilon_0}\) چنده وي.'),
 ('Capacitor: a device which is used for storing electric charges.', 'کیپیسٹر: برقی بار ذخیرہ کرنے کا آلہ۔', 'کپاسیټر: د برېښنايي چارجونو د زېرمه کولو وسیله.'),
 (r'Electron volt (eV): the unit of energy related to the joule by \(1\,\mathrm{eV}=1.602\times10^{-19}\,\mathrm J\).', r'الیکٹران وولٹ (eV): توانائی کی اکائی، جس کا جول سے تعلق \(1\,\mathrm{eV}=1.602\times10^{-19}\,\mathrm J\) ہے۔', r'الکترون ولټ (eV): د انرژۍ واحد چې له جول سره یې اړیکه \(1\,\mathrm{eV}=1.602\times10^{-19}\,\mathrm J\) ده.'),
 ('Dipole: a system of two charges of equal magnitude but opposite sign separated by distance d.', 'ثنائیہ: برابر مقدار مگر مخالف علامت کے دو باروں کا نظام، جن کے درمیان فاصلہ d ہو۔', 'ډایپول: د دوو برابر مقدار خو مخالفې نښې لرونکو چارجونو سیستم چې د d واټن په اندازه بېل وي.'),
]

def circuit(lang):
    caption = {'en':'Figure 11.29 — discharging a capacitor','ur':'شکل 11.29 — کیپیسٹر کا ڈسچارج ہونا','ps':'شکل 11.29 — د کپاسیټر ډسچارج'}[lang]
    body = '<path d="M85 55H320V265H85V55" fill="none" stroke="#cbd5e1" stroke-width="4"/><circle cx="110" cy="55" r="5" fill="#111827" stroke="#fff" stroke-width="3"/><circle cx="135" cy="55" r="5" fill="#111827" stroke="#fff" stroke-width="3"/><path d="M110 55L132 45" stroke="#f8fafc" stroke-width="4"/>'
    body += '<path d="M320 105V130M320 130L302 140V172L320 182V212M300 142H340M300 170H340" fill="none" stroke="#f8fafc" stroke-width="4"/><text x="349" y="165">R</text><text x="349" y="210">C</text><text x="116" y="35">K</text>'
    body += '<path d="M85 100V160M73 160H97M77 171H93" stroke="#f8fafc" stroke-width="4"/><text x="38" y="145">−q</text><text x="38" y="190">+q</text><path d="M85 110V145M265 265H215" stroke="#38bdf8" stroke-width="3" marker-end="url(#a)"/><text x="68" y="105">i</text><text x="235" y="251">i</text>'
    return '<figure>'+svg(body,410,300,'Open-loop capacitor discharging through resistance R, with switch K and decreasing current')+'<figcaption>'+caption+'</figcaption></figure>'

def decay_graph(lang):
    caption = {'en':'Figure 11.30 — discharging a capacitor','ur':'شکل 11.30 — کیپیسٹر کا ڈسچارج گراف','ps':'شکل 11.30 — د کپاسیټر د ډسچارج ګراف'}[lang]
    body = '<path d="M70 245V35M70 245H405" stroke="#f8fafc" stroke-width="3" marker-end="url(#a)"/><path d="M72 53C126 157 194 205 382 230" fill="none" stroke="#38bdf8" stroke-width="4"/><path d="M71 169H165V244M71 169H165" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6 5"/><text x="40" y="53">q</text><text x="414" y="250">t</text><text x="80" y="47">q₀</text><text x="78" y="162">0.368q₀</text><text x="154" y="270">RC</text><text x="212" y="300">Discharging of a capacitor</text>'
    return '<figure>'+svg(body,450,315,'Capacitor charge q decays from q0 toward zero; 0.368 q0 occurs at time RC')+'<figcaption>'+caption+'</figcaption></figure>'

def cdi_schematic(lang):
    caption = {'en':'Figure 11.31 — electronic ignition CDI (schematic)','ur':'شکل 11.31 — برقی اگنیشن CDI (خاکہ)','ps':'شکل 11.31 — برېښنايي اېګنیشن CDI (انځوریزه بڼه)'}[lang]
    body = '<rect x="25" y="75" width="92" height="70" rx="8" fill="#334155" stroke="#cbd5e1" stroke-width="3"/><text x="41" y="105">CDI</text><text x="36" y="126">capacitor</text><path d="M117 110H170M220 110H278M278 110V170" stroke="#38bdf8" stroke-width="4" fill="none"/>'
    body += '<path d="M170 78C145 78 145 142 170 142C195 142 195 78 220 78M170 78C195 78 195 142 220 142" fill="none" stroke="#fbbf24" stroke-width="4"/><text x="173" y="165">coil</text>'
    body += '<path d="M278 170L262 196L282 196L267 225L307 184L286 184L302 170Z" fill="#f8fafc"/><text x="245" y="255">spark plug</text><path d="M50 75V48H95V75M50 145V185H100" stroke="#94a3b8" stroke-width="3" fill="none"/><text x="48" y="40">battery</text>'
    return '<figure>'+svg(body,365,285,'Schematic CDI ignition path: battery, capacitor discharge unit, ignition coil, and spark plug')+'<figcaption>'+caption+'</figcaption></figure>'

def discharge_figures(lang):
    return circuit(lang)+decay_graph(lang)+cdi_schematic(lang)

if __name__ == '__main__':
    records, sections = [], []
    specs = [
      ('phys12-front-discharge44','Capacitor discharging and CDI ignition',44,DISCHARGE,
       ('کیپیسٹر کا ڈسچارج اور CDI اگنیشن','د کپاسیټر ډسچارج او CDI اېګنیشن'),
       [{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'visual'},{'type':'heading','indices':[4]},{'type':'paragraph','indices':[5]}],discharge_figures),
      ('phys12-front-keypoints45','KEY POINTS — Unit 11 Electrostatics',45,KEYS,
       ('اہم نکات — یونٹ 11 برق ساکنات','مهم ټکي — ۱۱م څپرکی، الکتروسټاتیک'),
       [{'type':'paragraph','indices':[i]} for i in range(8)],None),
    ]
    for identity,title,printed,pairs,headings,layout,visual in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':27,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        item=section(record,pairs,layout,headings)
        item['kind']='lesson'
        if visual:
            item.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'))
            item['content']+=visual('en')
        records.append(record);sections.append(item)
    upsert(records,sections)
    sync_companions(formulas=[
      {'id':'phys12-eq-rc-discharge-368','name':'Capacitor charge after one discharge time constant','formula':DISCHARGE[1][0],'latex':r't=RC,\ q=0.368q_0','sourceReferences':[{'pdfPage':27,'printedPage':44}]}
    ],definitions=[
      {'term':'Coulomb’s law','definition':KEYS[0][0].split(': ',1)[1],'definitionUrdu':KEYS[0][1].split(': ',1)[1],'definitionPashto':KEYS[0][2].split(': ',1)[1],'sourceReferences':[{'pdfPage':27,'printedPage':45}]},
      {'term':'Electric field','definition':KEYS[2][0].split(': ',1)[1],'definitionUrdu':KEYS[2][1].split(': ',1)[1],'definitionPashto':KEYS[2][2].split(': ',1)[1],'sourceReferences':[{'pdfPage':27,'printedPage':45}]},
    ])
    checkpoint(27,'corrected_verified',[r['id'] for r in records],
      'Original spread rendered at 2.5x and inspected. Discharge behavior at t=RC, 36.8% residual charge, CDI applications and camera-flash tip compared; native discharge circuit, exponential decay graph and CDI schematic replace the source photo/graphs. All eight printed Unit 11 key-point definitions transcribed with aligned translations; inline flux, Gauss-law and eV equations checked.',printed_pages=[44,45])
