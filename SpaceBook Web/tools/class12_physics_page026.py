from class12_source_review import upsert, section, checkpoint, sync_companions
from class12_physics_page013 import SOURCE, svg

ENERGY = [
    (r'\(\begin{aligned}U=\frac{QV}{2}=\frac{CV^2}{2}\ ...(11.38)\\U=\frac{Q^2}{2C}\end{aligned}\)',)*3,
    ('It is also possible to regard the energy as being stored in the electric field between the plates rather than the potential energy of the charges on the plates. Such a view point is useful when the Electric field between the plates is considered rather than the charges on the plates causing the field is to be considered. We know that', 'توانائی کو پلیٹوں پر موجود باروں کی برقی وضعی توانائی کے بجائے پلیٹوں کے درمیان برقی میدان میں ذخیرہ شدہ بھی سمجھا جا سکتا ہے۔ یہ نقطۂ نظر اس وقت مفید ہے جب میدان کو پیدا کرنے والے باروں کے بجائے پلیٹوں کے درمیان برقی میدان پر غور کیا جائے۔ ہم جانتے ہیں کہ', 'انرژي د تختو پر مخ د چارجونو د برېښنايي وضعي انرژۍ پر ځای د تختو ترمنځ په برېښنايي میدان کې زېرمه شوې هم ګڼل کېدای شي. دا لیدلوری هغه وخت ګټور دی چې د میدان د رامنځته کوونکو چارجونو پر ځای د تختو ترمنځ برېښنايي میدان وڅېړو. پوهېږو چې'),
    (r'\(V=Ed\quad\text{and}\quad C=\frac{A\epsilon_r\epsilon_0}{d}\)',)*3,
    ('Substituting these values in Eq. (11.38), we get', 'ان قدروں کو مساوات (11.38) میں رکھنے سے حاصل ہوتا ہے:', 'دا ارزښتونه په معادله (11.38) کې په ځای کولو سره ترلاسه کوو:'),
    (r'\(U=\frac12\times\frac{A\epsilon_r\epsilon_0}{d}\times(Ed)^2=\frac12\epsilon_r\epsilon_0E^2\times(Ad)\) ...(11.39)',)*3,
    ('The product (Ad) is volume between the plates. Let u denote the energy density, that is, the energy contained in a unit volume of the field. Then', 'حاصل ضرب Ad پلیٹوں کے درمیان حجم ہے۔ u کو توانائی کی کثافت، یعنی میدان کے اکائی حجم میں موجود توانائی، ظاہر کرنے دیں۔ تب', 'حاصل ضرب Ad د تختو ترمنځ حجم دی. u دې د انرژۍ کثافت وښيي، یعنې په واحد حجم کې د میدان انرژي. نو'),
    (r'\(u=\frac{U}{\text{Volume}}=\frac{U}{Ad}\)',)*3,
    (r'\(u=\frac12\epsilon_r\epsilon_0E^2\) ...(11.40)',)*3,
    ('11.13 CHARGING AND DISCHARGING OF A CAPACITOR THROUGH A RESISTOR', '11.13 مزاحمت کار کے ذریعے کیپیسٹر کو چارج اور ڈسچارج کرنا', '11.13 د مقاومت له لارې د کپاسیټر چارج او ډسچارج کول'),
    ('Consider a circuit having a capacitance C and a resistance R which are joined in series with a battery of voltage V through a key K, as shown in Figure 11.27.', 'ایسا سرکٹ دیکھیں جس میں گنجائش C اور مزاحمت R، کلید K کے ذریعے وولٹیج V کی بیٹری کے ساتھ سلسلہ وار جڑے ہیں، جیسا کہ شکل 11.27 میں ہے۔', 'هغه مدار په پام کې ونیسئ چې د C ظرفیت او R مقاومت پکې د K سویچ له لارې د V ولټاژ له بېټرۍ سره په لړۍ کې نښتي وي، لکه په شکل 11.27 کې.'),
    ('Let us assume that the capacitor C has no charge when the key K is open. These are the initial conditions of the circuit; when the key is closed, then t=0, i=0 and q=0.', 'فرض کریں کہ کلید K کھلی ہونے پر کیپیسٹر C پر کوئی بار نہیں۔ یہ سرکٹ کی ابتدائی حالتیں ہیں؛ کلید بند کرتے وقت t=0، i=0 اور q=0 ہوتا ہے۔', 'فرض کړئ چې د K سویچ د پرانیستې پر مهال پر C کپاسیټر هېڅ چارج نشته. دا د مدار لومړني شرایط دي؛ د سویچ د تړلو پر مهال t=0، i=0 او q=0 وي.'),
]

CHARGING = [
    ('When the key is pressed, the capacitor begins to store charge. If at any time during charging, I is the current through the circuit and Q is the charge on the capacitor, it can be shown that after time t, as charge builds up on the plates, it repels more charge than is arriving, and the current drops as the charge on the plates increases.', 'کلید دبانے پر کیپیسٹر بار ذخیرہ کرنا شروع کرتا ہے۔ چارجنگ کے دوران کسی لمحے سرکٹ میں رو I اور کیپیسٹر پر بار Q ہو، تو وقت t بعد پلیٹوں پر بار بڑھنے کے ساتھ وہ آنے والے مزید بار کو دفع کرتا ہے، اور پلیٹوں کا بار بڑھنے سے رو کم ہوتی جاتی ہے۔', 'د سویچ په ټینګولو سره کپاسیټر د چارج زېرمه کول پیلوي. د چارج کولو پر مهال په هر وخت کې که د مدار جریان I او پر کپاسیټر چارج Q وي، نو له t وخت وروسته د تختو پر چارج په زیاتېدو، هغه نور راتلونکی چارج دفع کوي او د تختو د چارج له زیاتېدو سره جریان کمېږي.'),
    ('The graph between time t and charge q is shown in Figure 11.28. At time t=0 charge q=0, and at a certain time t charge q reaches its maximum value q₀.', 'وقت t اور بار q کا گراف شکل 11.28 میں ہے۔ t=0 پر q=0 ہوتا ہے، اور ایک خاص وقت پر q اپنی زیادہ سے زیادہ قدر q₀ تک پہنچتا ہے۔', 'د وخت t او چارج q ترمنځ ګراف په شکل 11.28 کې ښودل شوی. په t=0 کې q=0 وي، او په یوه ټاکلي وخت کې q خپلې اعظمي کچې q₀ ته رسېږي.'),
    ('The graph also shows that the charge reaches its maximum value sooner when the time constant is small. As the capacitor charges up, the potential difference across its plates begins to increase with the actual time taken for the charge on the capacitor to reach 63% of its maximum possible fully charged value.', 'گراف یہ بھی دکھاتا ہے کہ وقت کا مستقل چھوٹا ہو تو بار جلد اپنی زیادہ سے زیادہ قدر تک پہنچتا ہے۔ کیپیسٹر چارج ہونے کے ساتھ پلیٹوں کے درمیان فرقِ پوٹینشل بڑھتا ہے۔ مکمل چارج کی زیادہ سے زیادہ قدر کے 63% تک پہنچنے میں لگنے والا اصل وقت اس سے وابستہ ہے۔', 'ګراف دا هم ښيي چې د وخت ثابت چې کوچنی وي، چارج ژر خپلې اعظمي کچې ته رسېږي. د کپاسیټر په چارج کېدو سره د تختو ترمنځ پوتنشیالي توپیر زیاتېږي. د بشپړ چارج د اعظمي کچې 63٪ ته د رسېدو واقعي وخت له دې سره تړاو لري.'),
    ('TIME CONSTANT', 'وقت کا مستقل', 'د وخت ثابت'),
    ('The time taken to charge a capacitor in a given circuit is determined by the time constant of the circuit.', 'کسی دیے گئے سرکٹ میں کیپیسٹر کو چارج ہونے میں لگنے والا وقت سرکٹ کے وقت کے مستقل سے متعین ہوتا ہے۔', 'په ورکړل شوي مدار کې د کپاسیټر د چارج کېدو موده د مدار د وخت ثابت ټاکي.'),
    ('The factor RC is called the time constant. The time constant is the duration of time for the capacitor in which 63.2% of its maximum value charge is deposited on the plates, as illustrated in the curve in Figure 11.28.', 'حاصل ضرب RC کو وقت کا مستقل کہتے ہیں۔ یہ وہ دورانیہ ہے جس میں کیپیسٹر کی زیادہ سے زیادہ بار کی 63.2% مقدار پلیٹوں پر جمع ہو جاتی ہے، جیسا کہ شکل 11.28 کے منحنی میں دکھایا گیا ہے۔', 'حاصل ضرب RC ته د وخت ثابت ویل کېږي. دا هغه موده ده چې په ترڅ کې یې د کپاسیټر د اعظمي چارج 63.2٪ پر تختو زېرمه کېږي، لکه د شکل 11.28 په منحني کې چې ښودل شوې ده.'),
    ('Maximum charge on capacitor = capacitance × e.m.f. of battery', 'کیپیسٹر پر زیادہ سے زیادہ بار = گنجائش × بیٹری کی برقی محرک قوت', 'پر کپاسیټر اعظمي چارج = ظرفیت × د بېټرۍ الکتروموتوري قوه'),
    ('Figure 11.29 shows a resistor-capacitor circuit called an RC circuit.', 'شکل 11.29 میں مزاحمت کار اور کیپیسٹر کا سرکٹ دکھایا گیا ہے، جسے RC سرکٹ کہتے ہیں۔', 'شکل 11.29 د مقاومت او کپاسیټر مدار ښيي چې RC مدار بلل کېږي.'),
    ('When the battery is removed and the key K is first closed, the capacitor starts to discharge as shown in Figure 11.30.', 'بیٹری ہٹانے کے بعد جب کلید K پہلی بار بند کی جاتی ہے، تو کیپیسٹر ڈسچارج ہونا شروع کرتا ہے، جیسا کہ شکل 11.30 میں ہے۔', 'کله چې بېټرۍ لرې شي او د K سویچ د لومړي ځل لپاره وتړل شي، کپاسیټر ډسچارج پیلوي، لکه په شکل 11.30 کې.'),
    ('In principle, a capacitor can never charge up fully, because the rate of charging decreases as the charge increases. In practice, after a finite time the charging current becomes too small to measure, and the capacitor is effectively fully charged.', 'اصولی طور پر کیپیسٹر کبھی مکمل چارج نہیں ہو سکتا، کیونکہ بار بڑھنے کے ساتھ چارج ہونے کی رفتار گھٹتی ہے۔ عملی طور پر ایک محدود وقت بعد چارجنگ رو اتنی کم ہو جاتی ہے کہ اسے ناپنا ممکن نہیں رہتا، اور کیپیسٹر کو مؤثر طور پر مکمل چارج سمجھا جاتا ہے۔', 'په اصل کې کپاسیټر هېڅکله بشپړ چارج کېدای نه شي، ځکه د چارج له زیاتېدو سره د چارجېدو کچه کمېږي. په عمل کې له یوې محدودې مودې وروسته د چارج جریان دومره لږ شي چې اندازه کول یې ناشوني وي، او کپاسیټر عملاً بشپړ چارج شوی ګڼل کېږي.'),
]

def circuit(lang):
    caption = {'en':'Figure 11.27 — charging circuit','ur':'شکل 11.27 — چارجنگ سرکٹ','ps':'شکل 11.27 — د چارج کولو مدار'}[lang]
    body = '<path d="M72 65H180M220 65H350V105M350 176V188M350 212V260H72V65" fill="none" stroke="#cbd5e1" stroke-width="4"/>'
    body += '<circle cx="185" cy="65" r="6" fill="#111827" stroke="#f8fafc" stroke-width="3"/><circle cx="216" cy="65" r="6" fill="#111827" stroke="#f8fafc" stroke-width="3"/><path d="M190 60L211 48" stroke="#f8fafc" stroke-width="4"/>'
    body += '<path d="M350 105L334 115L366 127L334 139L366 151L334 163L350 176M330 188H370M330 212H370" fill="none" stroke="#f8fafc" stroke-width="4"/>'
    body += '<path d="M72 115V155M59 155H85M63 166H81" stroke="#f8fafc" stroke-width="4"/>'
    body += '<path d="M119 65H159M303 260H263" stroke="#38bdf8" stroke-width="3" marker-end="url(#a)"/><text x="130" y="52">i</text><text x="273" y="248">i</text>'
    body += '<text x="183" y="38">K</text><text x="378" y="173">R</text><text x="378" y="219">C</text><text x="25" y="150">V</text>'
    return '<figure>' + svg(body, 420, 300, 'Series RC circuit with voltage source V, switch K, resistor R, capacitor C, and current arrows') + '<figcaption>'+caption+'</figcaption></figure>'

def charge_graph(lang):
    caption = {'en':'Figure 11.28 — capacitor charging curve','ur':'شکل 11.28 — کیپیسٹر کی چارجنگ کا منحنی','ps':'شکل 11.28 — د کپاسیټر د چارج منحني'}[lang]
    body = '<path d="M70 245V35M70 245H410" stroke="#f8fafc" stroke-width="3" marker-end="url(#a)"/>'
    body += '<path d="M71 245C120 103 190 65 390 62" fill="none" stroke="#38bdf8" stroke-width="4"/><path d="M71 62H390" stroke="#fbbf24" stroke-width="2" stroke-dasharray="7 6"/>'
    body += '<path d="M169 245V124M70 124H169" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 5"/>'
    body += '<text x="30" y="55">q</text><text x="415" y="250">t</text><text x="82" y="54">q₀</text><text x="79" y="117">0.632q₀</text><text x="156" y="270">RC</text><text x="240" y="300">Charging of a capacitor</text>'
    return '<figure>' + svg(body, 450, 315, 'Capacitor charge q rises toward maximum q0 over time; 0.632 q0 occurs at time RC') + '<figcaption>'+caption+'</figcaption></figure>'

def charging_figures(lang):
    return circuit(lang) + charge_graph(lang)

if __name__ == '__main__':
    specs = [
      ('phys12-front-energy-density42', 'ENERGY STORED IN AN ELECTRIC FIELD', 42, ENERGY,
       ('برقی میدان میں ذخیرہ توانائی', 'په برېښنايي میدان کې زېرمه شوې انرژي'),
       [{'type':'equation','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'equation','indices':[6]},{'type':'equation','indices':[7]},{'type':'heading','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'paragraph','indices':[10]}], None),
      ('phys12-front-rc-time-constant43', '11.13 CHARGING AND DISCHARGING OF A CAPACITOR THROUGH A RESISTOR', 43, CHARGING,
       ('11.13 مزاحمت کار کے ذریعے کیپیسٹر کو چارج اور ڈسچارج کرنا', '11.13 د مقاومت له لارې د کپاسیټر چارج او ډسچارج کول'),
       [{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'paragraph','indices':[9]}], charging_figures),
    ]
    records, sections = [], []
    for identity, title, printed, pairs, heading, layout, visual in specs:
        record = {'id':identity,'title':title,'kind':'lesson','pdfPage':26,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised = section(record, pairs, layout, heading)
        revised['kind'] = 'lesson'
        if visual:
            revised.update(diagramSvg=visual('en'), diagramSvgUrdu=visual('ur'), diagramSvgPashto=visual('ps'))
            revised['content'] += visual('en')
        records.append(record)
        sections.append(revised)
    upsert(records, sections)
    sync_companions(formulas=[
      {'id':'phys12-eq-11.38','name':'Capacitor stored energy','number':'11.38','formula':ENERGY[0][0],'latex':r'U=\frac{QV}{2}=\frac{CV^2}{2}=\frac{Q^2}{2C}','sourceReferences':[{'pdfPage':26,'printedPage':42}]},
      {'id':'phys12-eq-11.39','name':'Energy in electric field','number':'11.39','formula':ENERGY[4][0],'latex':r'U=\frac12\epsilon_r\epsilon_0E^2(Ad)','sourceReferences':[{'pdfPage':26,'printedPage':42}]},
      {'id':'phys12-eq-11.40','name':'Electric-field energy density','number':'11.40','formula':ENERGY[7][0],'latex':r'u=\frac12\epsilon_r\epsilon_0E^2','sourceReferences':[{'pdfPage':26,'printedPage':42}]},
    ], definitions=[
      {'term':'Time constant','definition':CHARGING[4][0]+' '+CHARGING[5][0],'definitionUrdu':CHARGING[4][1]+' '+CHARGING[5][1],'definitionPashto':CHARGING[4][2]+' '+CHARGING[5][2],'sourceReferences':[{'pdfPage':26,'printedPage':43}]}
    ], trim_sections=[
      {'id':'11.15','startsAt':'11.12 ENERGY STORED IN A CAPACITOR','title':'Energy stored in a capacitor (source review continues through PDF page 26)','clearSciNote':True}
    ])
    from pathlib import Path
    import json
    progress = json.loads((Path(__file__).resolve().parents[1] / 'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))
    if progress['nextPage'] == 26:
        checkpoint(26,'corrected_verified',[r['id'] for r in records],
          'Original spread rendered at 2.5x and inspected. Energy equations 11.38–11.40, derivation and energy-density definition transcribed; section 11.13 opening and initial conditions retained. Charging prose, time constant RC, 63.2% criterion, maximum charge and full-charge note compared. Figures 11.27 and 11.28 rebuilt as native SVG; no instructional raster retained.',printed_pages=[42,43])
    elif progress['lastFullyVerifiedPage'] < 26:
        raise RuntimeError('Unexpected checkpoint state; refusing to advance the review ledger')
