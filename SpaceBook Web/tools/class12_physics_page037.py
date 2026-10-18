"""Sequential source correction for PDF page 37 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"

def pair(en, ur, ps): return (en, ur, ps)

def svg(body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" role="img" '
            f'aria-label="{escape(label, quote=True)}" style="width:100%;max-width:520px;height:auto">'
            f'<rect width="100%" height="100%" fill="#fff"/>{body}</svg>')

RHEOSTAT = [
    pair('i) RHEOSTATS', 'i) ریوسٹیٹ', 'i) ریوستات'),
    pair('To use the variable resistor as a current control device one of the two fixed terminals say A and the sliding terminal C are inserted in the circuit as shown in figure 12.5. In this way the resistance of the wire between A and the sliding contact C is used. If the sliding contact is shifted away from the terminal A the length and hence the resistance included in the circuit increases. If the sliding contact is moved towards A, the resistance decreases. Adjusting the resistance in the circuit controls the current in a circuit.',
         'متغیر مزاحم کو برقی رو کے کنٹرول کے آلے کے طور پر استعمال کرنے کے لیے دو مستقل سروں میں سے ایک، مثلاً A، اور سرکتا ہوا سرا C شکل 12.5 کے مطابق سرکٹ میں لگائے جاتے ہیں۔ اس طرح تار کا وہ حصہ استعمال ہوتا ہے جو A اور سرکتے ہوئے رابطے C کے درمیان ہے۔ اگر سرکتے رابطے کو سرے A سے دور کیا جائے تو شامل تار کی لمبائی اور اس کے ساتھ مزاحمت بڑھ جاتی ہے۔ اگر سرکتے رابطے کو A کی طرف لے جائیں تو مزاحمت کم ہو جاتی ہے۔ سرکٹ میں مزاحمت کو ایڈجسٹ کرنے سے برقی رو قابو میں رہتی ہے۔',
         'د متغیر مقاومت د برېښنايي جریان د کنټرول لپاره، له دوو ثابتو ترمینلونو څخه یو، لکه A، او خوځنده ترمینل C د 12.5 شکل په څېر په مدار کې نښلول کېږي. په دې توګه د A او خوځنده تماس C ترمنځ د سیم مقاومت کارول کېږي. که خوځنده تماس له A څخه لرې شي، په مدار کې د سیم اوږدوالی او ورسره مقاومت زیاتېږي. که تماس د A پر لور وخوځول شي، مقاومت کمېږي. په مدار کې د مقاومت تنظیمول برېښنايي جریان کنټرولوي.'),
]

POTENTIAL = [
    pair('ii) POTENTIAL DIVIDER', 'ii) پوٹینشل ڈیوائیڈر', 'ii) پوتنشیالي وېشونکی'),
    pair('A potential divider provides a convenient way of getting a variable potential difference from a fixed potential difference. With the help of the battery, a potential difference V is applied across the ends A and B of the resistor (figure 12.6). Let R be the resistance of wire AB. The current I passing through it is',
         'پوٹینشل ڈیوائیڈر، مستقل پوٹینشل فرق سے متغیر پوٹینشل فرق حاصل کرنے کا آسان طریقہ فراہم کرتا ہے۔ بیٹری کی مدد سے مزاحم کے سروں A اور B کے درمیان پوٹینشل فرق V لگایا جاتا ہے (شکل 12.6)۔ فرض کریں کہ تار AB کی مزاحمت R ہے۔ اس میں سے گزرنے والی برقی رو I یہ ہے:',
         'پوتنشیالي وېشونکی له ثابت پوتنشیالي توپیر څخه د متغیر پوتنشیالي توپیر د ترلاسه کولو اسانه لاره برابروي. د بیټرۍ په مرسته د مقاومت د A او B پایونو ترمنځ د V پوتنشیالي توپیر لګېږي (12.6 شکل). فرض کړئ چې د AB سیم مقاومت R دی. له هغه څخه تېرېدونکی جریان I داسې دی:'),
    pair(r'\(I=\frac{V}{R}\)', r'\(I=\frac{V}{R}\)', r'\(I=\frac{V}{R}\)'),
    pair('If R_BC is the resistance of the portion of the wire BC and the current passing through BC is I. The PD between the points B and C is given by',
         'اگر تار کے حصے BC کی مزاحمت R_BC ہو اور اس حصے سے گزرنے والی برقی رو I ہو تو نقاط B اور C کے درمیان پوٹینشل فرق یہ ہے:',
         'که د BC سیم د برخې مقاومت R_BC وي او له BC څخه تېرېدونکی جریان I وي، د B او C نقطو ترمنځ پوتنشیالي توپیر داسې دی:'),
    pair(r'\(V_{BC}=IR_{BC}\)', r'\(V_{BC}=IR_{BC}\)', r'\(V_{BC}=IR_{BC}\)'),
    pair(r'\(\Rightarrow V_{BC}=\frac{V}{R}R_{BC}=\frac{R_{BC}}{R}V\)', r'\(\Rightarrow V_{BC}=\frac{V}{R}R_{BC}=\frac{R_{BC}}{R}V\)', r'\(\Rightarrow V_{BC}=\frac{V}{R}R_{BC}=\frac{R_{BC}}{R}V\)'),
    pair('Depending on the position of the sliding contact C, the value of the fraction R_BC/R can be varied from 0 to 1. When the contact C, moving towards B, the length and hence the resistance R_BC of the portion of the wire decreases. Thus V_BC decreases. On the other hand if the sliding contact C is moved towards the end A, the length and the resistance R_BC of the wire increases and hence voltage V_BC increases.',
         'سرکتے رابطے C کی جگہ کے مطابق کسر R_BC/R کی قدر 0 سے 1 تک بدلی جا سکتی ہے۔ جب رابطہ C، B کی طرف حرکت کرتا ہے تو تار کے حصے کی لمبائی اور اس لیے مزاحمت R_BC کم ہوتی ہے۔ چنانچہ V_BC کم ہو جاتا ہے۔ دوسری طرف اگر سرکتے رابطے C کو سرے A کی طرف لے جائیں تو تار کی لمبائی اور مزاحمت R_BC بڑھ جاتی ہے، لہٰذا وولٹیج V_BC بڑھ جاتا ہے۔',
         'د خوځنده تماس C د موقعیت له مخې د R_BC/R کسر ارزښت له 0 څخه تر 1 پورې بدلېدای شي. کله چې تماس C د B پر لور ځي، د سیم د برخې اوږدوالی او ورسره مقاومت R_BC کمېږي؛ نو V_BC هم کمېږي. برعکس، که تماس C د A پای ته وخوځول شي، د سیم اوږدوالی او مقاومت R_BC زیاتېږي او له همدې امله ولتاژ V_BC زیاتېږي.'),
]

THERMISTOR = [
    pair('12.6 THERMISTOR', '12.6 تھرمسٹر', '12.6 ترمېسټر'),
    pair('Thermistor is temperature sensing device or resistance thermometer whose prime function is to exhibit change in electrical resistance when subjected to a corresponding change in body temperature. It is made of metallic oxides, pressed into a bead, disk, or cylindrical shape and then encapsulated with an impermeable material such as epoxy or glass. The two main types of the thermistors are NTC (Negative Temperature Coefficient) and PTC (Positive Temperature Coefficient).',
         'تھرمسٹر درجۂ حرارت محسوس کرنے والا آلہ یا مزاحمتی تھرمامیٹر ہے۔ اس کا بنیادی کام جسمانی درجۂ حرارت میں تبدیلی کے ساتھ برقی مزاحمت میں تبدیلی ظاہر کرنا ہے۔ یہ دھاتی آکسائیڈز سے بنتا ہے جنہیں دبا کر موتی، قرص یا استوانی شکل دی جاتی ہے، پھر ایپوکسی یا شیشے جیسے ناقابلِ نفوذ مادے میں بند کیا جاتا ہے۔ تھرمسٹروں کی دو بنیادی اقسام NTC (منفی درجۂ حرارت ضریب) اور PTC (مثبت درجۂ حرارت ضریب) ہیں۔',
         'ترمېسټر د تودوخې د حس کولو وسیله یا مقاومتي ترمامیتر دی چې اساسي دنده یې د جسم د تودوخې له بدلون سره سم په برېښنايي مقاومت کې بدلون ښودل دي. دا له فلزي اکسایډونو جوړېږي؛ اکسایډونه د دانې، ډیسک یا استوانې بڼه نیسي او بیا د ایپوکسي یا ښیښې په څېر نه‌نفوذېدونکي موادو کې پوښل کېږي. د ترمېسټر دوه اساسي ډولونه NTC (د تودوخې منفي ضریب) او PTC (د تودوخې مثبت ضریب) دي.'),
    pair('NEGATIVE TEMPERATURE COEFFICIENT (NTC) THERMISTOR:', 'منفی درجۂ حرارت ضریب (NTC) تھرمسٹر:', 'د تودوخې د منفي ضریب (NTC) ترمېسټر:'),
    pair('These types of thermistor are most commonly used. The resistance of an NTC thermistor decreases with increasing temperature. Conversely, its resistance increases with decreasing temperature. A small changes in temperature can cause significant changes in their electrical resistance. This makes them ideal for accurate temperature measurement and control. Some appliances, such as washing machines, clothes dryers, refrigerators and freezers, as well as small appliances like hair dryers, ovens, toasters, thermostats, air conditioners and fire alarms also have NTCs for temperature control. Figure 12.7 shows some Types of thermistor.',
         'یہ تھرمسٹر سب سے زیادہ استعمال ہوتے ہیں۔ NTC تھرمسٹر کی مزاحمت درجۂ حرارت بڑھنے پر کم ہوتی ہے۔ اس کے برعکس درجۂ حرارت کم ہونے پر مزاحمت بڑھتی ہے۔ درجۂ حرارت میں معمولی تبدیلی بھی ان کی برقی مزاحمت میں نمایاں تبدیلی پیدا کر سکتی ہے۔ اسی لیے یہ درجۂ حرارت کی درست پیمائش اور کنٹرول کے لیے موزوں ہیں۔ بعض آلات، مثلاً واشنگ مشینیں، کپڑے سکھانے والی مشینیں، ریفریجریٹر اور فریزر، نیز ہیئر ڈرائر، اوون، ٹوسٹر، تھرموسٹیٹ، ایئر کنڈیشنر اور فائر الارم، درجۂ حرارت کے کنٹرول کے لیے NTC رکھتے ہیں۔ شکل 12.7 میں تھرمسٹر کی چند اقسام دکھائی گئی ہیں۔',
         'دا ډول ترمېسټرونه تر ټولو ډېر کارول کېږي. د NTC ترمېسټر مقاومت د تودوخې په لوړېدو کمېږي او د تودوخې په کمېدو زیاتېږي. د تودوخې لږ بدلون هم د دوی په برېښنايي مقاومت کې د پام وړ بدلون راوستلای شي؛ له همدې امله د تودوخې د کره اندازه کولو او کنټرول لپاره مناسب دي. ځینې وسایل لکه د کالو مینځلو ماشینونه، د کالو وچوونکي، یخچالونه او فریزرونه، او همدارنګه د وېښتانو وچوونکي، تنورونه، ټوسټرونه، ترموسټاټونه، ایرکنډېشنرونه او د اور خبرتیا وسایل د تودوخې د کنټرول لپاره NTC لري. 12.7 شکل د ترمېسټر ځینې ډولونه ښيي.'),
]

def make(identity, title, printed, pairs, layout, headings, pages, visual=None):
    record = {'id': identity, 'title': title, 'kind': 'lesson', 'pdfPage': 37,
              'printedPage': printed, 'sourcePdf': SOURCE, 'paragraphs': [p[0] for p in pairs]}
    item = section(record, pairs, layout, headings)
    item['kind'] = 'lesson'
    item['sourceReferences'] = [{'pdfPage': 37, 'printedPage': p, 'sourcePdf': SOURCE} for p in pages]
    if visual:
        item.update(visual)
        item['content'] += visual['diagramSvg']
    return record, item

def rheostat_svg(lang):
    L = {'en':('Battery','lamp','FIGURE 12.5'), 'ur':('بیٹری','بلب','شکل 12.5'), 'ps':('بیټرۍ','څراغ','12.5 شکل')}[lang]
    body = ('<path d="M40 110H105M105 110l12-18 18 36 18-36 18 36 18-36 18 36 18-18H285M355 110H475V165H40V110" fill="none" stroke="#334155" stroke-width="3"/>'
      '<path d="M105 110V72M105 72H205" stroke="#334155" stroke-width="3"/><path d="M187 62l18 10-18 10" fill="#334155"/>'
      '<circle cx="105" cy="110" r="5" fill="#2563eb"/><circle cx="285" cy="110" r="5" fill="#2563eb"/><circle cx="205" cy="72" r="5" fill="#2563eb"/>'
      '<path d="M245 96l10 14-10 14 10 14" fill="none" stroke="#f59e0b" stroke-width="3"/><circle cx="245" cy="110" r="22" fill="none" stroke="#334155" stroke-width="2"/>'
      '<text x="96" y="135" font-size="16">A</text><text x="278" y="135" font-size="16">B</text><text x="195" y="60" font-size="16">C</text>'
      f'<text x="52" y="154" font-size="14">{escape(L[0])}</text><text x="215" y="160" font-size="14">{escape(L[1])}</text><text x="350" y="32" font-size="16">{escape(L[2])}</text>')
    return svg(body, L[2])

def divider_svg(lang):
    L = {'en':('Potential divider','slider C','VBC','FIGURE 12.6'), 'ur':('پوٹینشل ڈیوائیڈر','سرکتا رابطہ C','VBC','شکل 12.6'), 'ps':('پوتنشیالي وېشونکی','خوځنده تماس C','VBC','12.6 شکل')}[lang]
    body = ('<path d="M130 90H410M130 90V150H410V90" fill="none" stroke="#334155" stroke-width="3"/>'
      '<path d="M185 90l12-14 20 28 20-28 20 28 20-28 20 28 20-28 20 28 20-14" fill="none" stroke="#2563eb" stroke-width="3"/>'
      '<path d="M295 90V48M280 48H310" stroke="#f59e0b" stroke-width="4"/><circle cx="295" cy="90" r="6" fill="#f59e0b"/>'
      '<path d="M130 90V150M410 90V150" stroke="#334155" stroke-width="3"/><path d="M85 104V138M76 138H94M80 145H90" stroke="#334155" stroke-width="3"/>'
      '<text x="116" y="79" font-size="16">A</text><text x="404" y="79" font-size="16">B</text><text x="283" y="39" font-size="16">C</text>'
      f'<text x="150" y="182" font-size="15">V</text><text x="322" y="182" font-size="15">{escape(L[2])}</text><text x="310" y="30" font-size="15">{escape(L[1])}</text><text x="332" y="208" font-size="15">{escape(L[0])}</text><text x="350" y="25" font-size="15">{escape(L[3])}</text>')
    return svg(body, L[3])

def thermistor_svg(lang):
    L = {'en':('US & Japan','Europe','(a) Thermistor Symbol','(b) Types of thermistor','FIGURE 12.7'),
         'ur':('امریکہ اور جاپان','یورپ','(الف) تھرمسٹر کی علامت','(ب) تھرمسٹر کی اقسام','شکل 12.7'),
         'ps':('امریکا او جاپان','اروپا','(الف) د ترمېسټر نښه','(ب) د ترمېسټر ډولونه','12.7 شکل')}[lang]
    body = ('<path d="M35 92H90M130 92H180M90 75L130 109M180 75L220 109" stroke="#334155" stroke-width="3"/>'
      '<rect x="90" y="76" width="40" height="32" fill="#e0f2fe" stroke="#334155" stroke-width="2"/><path d="M180 76h40v32h-40z" fill="#e0f2fe" stroke="#334155" stroke-width="2"/>'
      '<text x="40" y="60" font-size="13">NTC</text><text x="190" y="60" font-size="13">PTC</text>'
      '<circle cx="305" cy="78" r="10" fill="#f59e0b" stroke="#334155"/><ellipse cx="360" cy="80" rx="24" ry="13" fill="#bae6fd" stroke="#334155"/><rect x="405" y="68" width="48" height="24" rx="7" fill="#cbd5e1" stroke="#334155"/><rect x="465" y="68" width="28" height="24" rx="5" fill="#fecaca" stroke="#334155"/>'
      f'<text x="72" y="132" font-size="13">{escape(L[0])}</text><text x="183" y="132" font-size="13">{escape(L[1])}</text><text x="48" y="176" font-size="13">{escape(L[2])}</text><text x="300" y="176" font-size="13">{escape(L[3])}</text><text x="380" y="30" font-size="15">{escape(L[4])}</text>')
    return svg(body, L[4])

if __name__ == '__main__':
    r = make('phys12-unit12-rheostats64', 'i) Rheostats — variable resistance and current control', 64, RHEOSTAT,
      [{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'}],
      ('i) ریوسٹیٹ — متغیر مزاحمت اور برقی رو کا کنٹرول','i) ریوستات — متغیر مقاومت او د برېښنايي جریان کنټرول'), [64],
      {'diagramSvg':rheostat_svg('en'),'diagramSvgUrdu':rheostat_svg('ur'),'diagramSvgPashto':rheostat_svg('ps')})
    d = make('phys12-unit12-potential-divider64-65', 'ii) Potential divider', 64, POTENTIAL,
      [{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},
       {'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'equation','indices':[5]},
       {'type':'visual'},{'type':'paragraph','indices':[6]}],
      ('ii) پوٹینشل ڈیوائیڈر','ii) پوتنشیالي وېشونکی'), [64,65],
      {'diagramSvg':divider_svg('en'),'diagramSvgUrdu':divider_svg('ur'),'diagramSvgPashto':divider_svg('ps')})
    t = make('phys12-unit12-thermistor-ntc65', '12.6 Thermistor — NTC type', 65, THERMISTOR,
      [{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'heading','indices':[2]},
       {'type':'paragraph','indices':[3]},{'type':'visual'}],
      ('12.6 تھرمسٹر — NTC قسم','12.6 ترمېسټر — NTC ډول'), [65],
      {'diagramSvg':thermistor_svg('en'),'diagramSvgUrdu':thermistor_svg('ur'),'diagramSvgPashto':thermistor_svg('ps')})
    records=[r[0],d[0],t[0]]; sections=[r[1],d[1],t[1]]
    upsert(records, sections, chapter_index=1)
    sync_companions(chapter_index=1,
      definitions=[{'term':'Rheostat','definition':RHEOSTAT[1][0],'definitionUrdu':RHEOSTAT[1][1],'definitionPashto':RHEOSTAT[1][2],
        'sourceReferences':[{'pdfPage':37,'printedPage':64,'sourcePdf':SOURCE}]},
       {'term':'Potential divider','definition':POTENTIAL[1][0]+' '+POTENTIAL[2][0]+' '+POTENTIAL[3][0]+' '+POTENTIAL[4][0]+' '+POTENTIAL[5][0],
        'definitionUrdu':POTENTIAL[1][1]+' '+POTENTIAL[2][1]+' '+POTENTIAL[3][1]+' '+POTENTIAL[4][1]+' '+POTENTIAL[5][1],
        'definitionPashto':POTENTIAL[1][2]+' '+POTENTIAL[2][2]+' '+POTENTIAL[3][2]+' '+POTENTIAL[4][2]+' '+POTENTIAL[5][2],
        'sourceReferences':[{'pdfPage':37,'printedPage':64,'sourcePdf':SOURCE}]},
       {'term':'Thermistor','definition':THERMISTOR[1][0],'definitionUrdu':THERMISTOR[1][1],'definitionPashto':THERMISTOR[1][2],
        'sourceReferences':[{'pdfPage':37,'printedPage':65,'sourcePdf':SOURCE}]}],
      retire_sections=['12.4'],
      trim_sections=[{'id':'12.5','startsAt':'POSITIVE TEMPERATURE COEFFICIENT (PTC) THERMISTOR:','title':'12.6 PTC thermistor — continuation pending source review'}])
    checkpoint(37,'corrected_verified',[x['id'] for x in records],
      'Rendered and visually inspected PDF page 37 at source resolution, printed pages 64–65. Compared the complete rheostat and potential-divider text, equations and figures 12.5–12.6, potential-divider continuation, thermistor and NTC descriptions, and figure 12.7. Rebuilt all three instructional visuals as translated inline SVG, paired each source paragraph with Urdu and Pashto, synchronized reusable definitions, retired covered legacy section 12.4 and trimmed covered text from 12.5 at the first unreviewed PTC heading. OCR was used only to locate text; the rendered page was authoritative.')
