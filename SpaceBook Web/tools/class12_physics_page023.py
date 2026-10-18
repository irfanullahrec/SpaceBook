from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
DERIVATION=[
 ('Where, V = V1 - V2 is the potential difference and d is the separation between the plates. The strength of the electric field also depends on the number of charges on the plates. The charge density is the total charge per unit area of the plate, i.e.,','جہاں V = V1 - V2 فرقِ برق ہے اور d پلیٹوں کے درمیان فاصلہ ہے۔ برقی میدان کی شدت پلیٹوں پر باروں کی تعداد پر بھی منحصر ہے۔ بار کی کثافت پلیٹ کے فی اکائی رقبہ کل بار ہے، یعنی،','دلته V = V1 - V2 د پوتانشیل توپیر او d د تختو ترمنځ واټن دی. د برېښنايي میدان شدت پر تختو د چارجونو په شمېر هم اړه لري. د چارج کثافت د تختې د هر واحد مساحت ټول چارج دی، یعنې،'),
 (r'\(\sigma=\frac QA\)',)*3,
 ('By using Gauss’s law the electric field intensity E between the plates is','د گاؤس کا قانون استعمال کرنے سے پلیٹوں کے درمیان برقی میدان کی شدت E یہ ہے','د ګاوس د قانون په کارولو سره د تختو ترمنځ د برېښنايي میدان شدت E دا دی'),
 (r'\(E=\frac{\sigma}{\varepsilon_o}=\frac Q{\varepsilon_o A}\) (B)',)*3,
 ('From Eq (A) & (B) we have','مساوات (A) اور (B) سے ہمارے پاس ہے','له معادلو (A) او (B) څخه لرو'),
 (r'\(E=\frac Vd=\frac Q{\varepsilon_o A}\)',)*3,
 (r'Or \(Q=\frac{\varepsilon_o AV}d\) ...(11.30)',r'یا \(Q=\frac{\varepsilon_o AV}d\) ...(11.30)',r'یا \(Q=\frac{\varepsilon_o AV}d\) ...(11.30)'),
 (r'By using \(C_{vac}=\frac QV\), Eq(11.30) becomes',r'\(C_{vac}=\frac QV\) استعمال کرنے سے مساوات (11.30) بن جاتی ہے',r'د \(C_{vac}=\frac QV\) په کارولو سره معادله (11.30) داسې کېږي'),
 (r'\(C_{vac}=\frac QV=\frac{\varepsilon_o A}d\) ...(11.31)',)*3,
 ('When a dielectric is inserted between the plates of a capacitor, then it is seen that the charge storing capacity of a capacitor is enhanced by the dielectric which permits it to store εr times more charge for the same potential difference','جب کیپیسٹر کی پلیٹوں کے درمیان ڈائی الیکٹرک داخل کیا جائے تو اس کی بار ذخیرہ کرنے کی صلاحیت بڑھ جاتی ہے، جس سے وہ اسی فرقِ برق پر εr گنا زیادہ بار ذخیرہ کر سکتا ہے','کله چې د کپاسیټر د تختو ترمنځ ډای الکټریک کېښودل شي، د کپاسیټر د چارج زېرمه کولو وړتیا ورسره زیاتېږي او د هماغه پوتانشیل توپیر لپاره εr برابره زیاته اندازه چارج زېرمه کولای شي'),
]
DIELECTRIC=[
 ('difference. In case of a parallel plate capacitor completely filled with a dielectric the capacitance is','فرقِ برق۔ ڈائی الیکٹرک سے مکمل بھرے متوازی پلیٹوں کے کیپیسٹر کی گنجائش یہ ہے','د پوتانشیل توپیر. د ډای الکټریک څخه په بشپړه توګه ډک د موازي تختو کپاسیټر ظرفیت دا دی'),
 (r'\(C_{med}=\frac{\varepsilon_o\varepsilon_r A}d\) ...(11.32)',)*3,
 ('Eq11.32: shows the dependence of capacitance upon the area of the plates, the separation between the plates and the medium between them.','مساوات 11.32 دکھاتی ہے کہ گنجائش پلیٹوں کے رقبے، ان کے درمیان فاصلے اور ان کے درمیان واسطے پر منحصر ہے۔','معادله 11.32 ښيي چې ظرفیت د تختو پر مساحت، د تختو ترمنځ واټن او د هغوی ترمنځ منځني چاپېریال پورې اړه لري.'),
 ('From Eq(11.31) and Eq(11.32) we have','مساوات (11.31) اور (11.32) سے ہمارے پاس ہے','له معادلو (11.31) او (11.32) څخه لرو'),
 (r'\(\varepsilon_r=\frac{C_{med}}{C_{vac}}\) ...(11.33)',)*3,
 ('This relation provides us with the definition of relative permittivity or dielectric constant or specific inductive capacity.','یہ تعلق اضافی برقی نفوذ پذیری، ڈائی الیکٹرک مستقل یا مخصوص القائی گنجائش کی تعریف دیتا ہے۔','دا اړیکه د نسبي برېښنايي نفوذپذیرۍ، ډای الکټریک ثابت یا د ځانګړي القايي ظرفیت تعریف راکوي.'),
 ('The ratio of the capacitance of a capacitor with a given material filling the space between the plates to the capacitance of the same capacitor when the space is evacuated is the relative permittivity εr of the material.','پلیٹوں کے درمیان جگہ کو کسی مادے سے بھرنے پر کیپیسٹر کی گنجائش اور وہی جگہ خالی کرنے پر اسی کیپیسٹر کی گنجائش کا تناسب اس مادے کی نسبتی برقی نفوذ پذیری εr ہے۔','د یوه ټاکلي مادي منځني چاپېریال سره د کپاسیټر ظرفیت او د هماغه کپاسیټر د ظرفیت نسبت چې منځنۍ تشه یې خالي وي، د هغه مادې نسبي برېښنايي نفوذپذیري εr ده.'),
]
COMBINATIONS=[
 ('We know that the capacitors can be connected either in series or in parallel. We want to find out an equivalent capacitor that has the same capacitance as that of the combination of capacitors','ہم جانتے ہیں کہ کیپیسٹر سلسلہ وار یا متوازی طور پر جوڑے جا سکتے ہیں۔ ہم ایسا مساوی کیپیسٹر معلوم کرنا چاہتے ہیں جس کی گنجائش، کیپیسٹروں کے مجموعے کی گنجائش کے برابر ہو۔','پوهېږو چې کپاسیټرونه په لړۍ یا موازي ډول نښلول کېدای شي. غواړو یو معادل کپاسیټر ومومو چې ظرفیت یې د کپاسیټرونو د ترکیب له ظرفیت سره برابر وي.'),
 ('SERIES COMBINATION OF CAPACITORS','کیپیسٹروں کا سلسلہ وار اتصال','د کپاسیټرونو لړۍ‌يي نښلون'),
 ('When the capacitors are connected plate to plate i.e. the right plate of one capacitor is connected to the left plate of the next capacitor so on as shown in Fig:11.24 then it called series','جب کیپیسٹر پلیٹ سے پلیٹ جوڑے جائیں، یعنی ایک کیپیسٹر کی دائیں پلیٹ اگلے کی بائیں پلیٹ سے جوڑی جائے، جیسا کہ شکل 11.24 میں ہے، تو اسے سلسلہ وار اتصال کہتے ہیں۔','کله چې کپاسیټرونه تخته پر تخته ونښلول شي، یعنې د یوه کپاسیټر ښۍ تخته د بل راتلونکي کپاسیټر له کیڼې تختې سره ونښلول شي، لکه په شکل 11.24 کې، نو دا لړۍ‌يي نښلون بلل کېږي.'),
]
NERVE=[
 ('FOR YOUR INFORMATION','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره'),
 ('An axon membrane acts as a capacitor. Axon of a resting human nerve cell has a potential difference of 65mV. Current enters the axon (or dendrite) through ion channels (e.g. Na+ channels) in a region of membrane, depolarizing that region. The intracellular positive charge is attracted to adjacent negatively charged regions of membrane.','ایکسن کی جھلی کیپیسٹر کی طرح عمل کرتی ہے۔ سکون کی حالت میں انسانی عصبی خلیے کے ایکسن میں 65mV کا فرقِ برق ہوتا ہے۔ آئن چینلز (مثلاً Na+ چینلز) کے ذریعے رو جھلی کے ایک حصے میں ایکسن (یا ڈینڈرائٹ) میں داخل ہوتی ہے اور اس حصے کو ڈی پولرائز کرتی ہے۔ خلیے کے اندر مثبت بار جھلی کے متصل منفی بار والے حصوں کی طرف کھنچتا ہے۔','د اکسون غشا د کپاسیټر په توګه عمل کوي. د ارام په حالت کې د انسان د عصبي حجرې په اکسون کې د پوتانشیل توپیر 65mV وي. جریان د ایون کانالونو (لکه Na+ کانالونو) له لارې د غشا یوې سیمې ته اکسون (یا ډینډرایټ) ته ننوځي او هغه سیمه ډی‌پولرایز کوي. د حجرې دننه مثبت چارج د غشا نږدې منفي چارج لرونکو سیمو ته جذبېږي.'),
]

def circuit(lang):
    body='<path d="M90 50H280V240H90Z" fill="none" stroke="#334155" stroke-width="3"/><rect x="112" y="45" width="24" height="100" fill="#fef3c7" stroke="#334155"/><rect x="190" y="45" width="24" height="100" fill="#fef3c7" stroke="#334155"/>'
    for y in range(60,144,18):body+=f'<text x="117" y="{y}">+</text><text x="195" y="{y}">−</text>'
    body+='<path d="M159 220V260M179 232V248" stroke="#334155" stroke-width="3"/><text x="149" y="215">+</text><text x="178" y="215">−</text><text x="106" y="41">A</text><text x="218" y="41">B</text>'
    cap={'en':'FIGURE 11.23: Plates of a capacitor separated by a distance d','ur':'شکل 11.23: فاصلے d سے جدا کیپیسٹر کی پلیٹیں','ps':'شکل 11.23: د d واټن په اندازه بېلې د کپاسیټر تختې'}[lang]
    return '<figure>'+svg(body,370,280,'Parallel capacitor plates A and B, battery connections, separation d')+'<figcaption>'+cap+'</figcaption></figure>'

def neuron(lang):
    body='<path d="M150 118C185 73 235 80 260 120 290 80 340 79 365 110 394 111 409 140 392 160 409 185 390 211 364 204 345 232 302 223 285 194 259 224 217 218 210 184 178 196 149 168 150 118Z" fill="#67c5d2" stroke="#334155" stroke-width="3"/><circle cx="278" cy="148" r="22" fill="#8b1c3a"/>'
    for path in ['M153 122L100 90 72 48','M154 132L87 131 48 116','M165 163L106 194 76 229','M183 98L156 55 151 29','M356 157C410 162 447 154 478 147','M400 149L454 113 478 89','M412 158L463 182 480 210']:
        body+=f'<path d="{path}" fill="none" stroke="#8b1c3a" stroke-width="7" stroke-linecap="round"/>'
    for x in [450,510,570]:
        body+=f'<rect x="{x}" y="137" width="49" height="21" rx="10" fill="#cbd5e1" stroke="#334155"/><path d="M{x+10} 137V158M{x+38} 137V158" stroke="#334155"/>'
    body+='<path d="M482 145C509 88 527 90 555 145M524 154C540 194 558 195 579 157" fill="none" stroke="#334155" stroke-width="3"/><text x="72" y="34">Neuron</text><text x="420" y="81">Axon</text><text x="510" y="127">Myelin</text>'
    return '<figure>'+svg(body,610,260,'Schematic neuron cell with branching dendrites, axon and myelin sheath sections')+'<figcaption>Neuron / Axon / Myelin — schematic</figcaption></figure>'

if __name__=='__main__':
    specs=[('phys12-front-parallel-capacitance36','11.10.2 PARALLEL PLATE CAPACITOR — derivation',36,DERIVATION,('11.10.2 متوازی پلیٹوں کا کیپیسٹر — اخذ','11.10.2 د موازي تختو کپاسیټر — استنتاج'),circuit,[{'type':'paragraph' if i in [0,2,4,9] else 'equation','indices':[i]} for i in range(10)]+[{'type':'visual'}]),('phys12-front-dielectric37','Dielectric-filled capacitor and relative permittivity',37,DIELECTRIC,('ڈائی الیکٹرک بھرا کیپیسٹر اور نسبتی برقی نفوذ پذیری','ډای الکټریک ډک کپاسیټر او نسبي برېښنايي نفوذپذیري'),None,[{'type':'paragraph' if i in [0,2,3,5,6] else 'equation','indices':[i]} for i in range(len(DIELECTRIC))]),('phys12-front-combinations37','11.10.3 COMBINATIONS OF CAPACITORS',37,COMBINATIONS,('11.10.3 کیپیسٹروں کا اتصال','11.10.3 د کپاسیټرونو نښلون'),None,[{'type':'paragraph','indices':[0]},{'type':'heading','indices':[1]},{'type':'paragraph','indices':[2]}]),('phys12-front-neuron37','FOR YOUR INFORMATION — Axon membrane',37,NERVE,('آپ کی معلومات کے لیے — ایکسن کی جھلی','ستاسو د معلوماتو لپاره — د اکسون غشا'),neuron,[{'type':'heading','indices':[0]},{'type':'visual'},{'type':'paragraph','indices':[1]}])]
    records=[];sections=[]
    for identity,title,page,pairs,titles,visual,layout in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':23,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        if visual:
            revised.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));revised['content']+=visual('en')
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(retire_sections=['11.13'],trim_sections=[{'id':'11.14','startsAt':'Figure:11.24','title':'Capacitors in series (source review starts at PDF page 24)','clearSciNote':True}],formulas=[{'id':'phys12-eq-11.30','name':'Parallel-plate capacitor charge','number':'11.30','formula':r'\(Q=\frac{\varepsilon_o AV}d\)','latex':r'Q=\frac{\varepsilon_o AV}d','sourceReferences':[{'pdfPage':23,'printedPage':36}]},{'id':'phys12-eq-11.31','name':'Vacuum parallel-plate capacitance','number':'11.31','formula':r'\(C_{vac}=\frac QV=\frac{\varepsilon_o A}d\)','latex':r'C_{vac}=\frac QV=\frac{\varepsilon_o A}d','sourceReferences':[{'pdfPage':23,'printedPage':36}]},{'id':'phys12-eq-11.32','name':'Dielectric capacitor','number':'11.32','formula':DIELECTRIC[1][0],'latex':r'C_{med}=\frac{\varepsilon_o\varepsilon_r A}d','sourceReferences':[{'pdfPage':23,'printedPage':37}]},{'id':'phys12-eq-11.33','name':'Relative permittivity','number':'11.33','formula':DIELECTRIC[4][0],'latex':r'\varepsilon_r=\frac{C_{med}}{C_{vac}}','sourceReferences':[{'pdfPage':23,'printedPage':37}]}],definitions=[{'term':'Relative permittivity','def':DIELECTRIC[5][0],'sourceReferences':[{'pdfPage':23,'printedPage':37}]}])
    checkpoint(23,'corrected_verified',[r['id'] for r in records],'Original spread inspected at2.5x. Full Eq11.30–11.33 derivations, dielectric and relative permittivity definitions, capacitor series introduction, and axon capacitor information box transcribed with aligned Urdu/Pashto. Figures11.23 and coded neuron schematic replace source visuals. Existing parallel-capacitance continuation trimmed at printed page36 start; covered legacy section11.13 retired and11.14 trimmed to PDF24.',printed_pages=[36,37])
