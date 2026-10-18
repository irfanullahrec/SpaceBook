"""Sequential source correction for PDF page 33 of Class 12 Physics."""
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"


def make_svg(body, width, height, labels):
    aria = escape(labels[0], quote=True)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'role="img" aria-label="{aria}" style="width:100%;max-width:{width}px;height:auto">'
            f'<rect width="100%" height="100%" fill="#fff"/>{body}</svg>')


def eeg_figure(lang):
    labels = {
        'en': ('Electroencephalogram (EEG)', 'Electrodes', 'Recording device', 'Brain-wave traces'),
        'ur': ('الیکٹرواینسیفلوگرام (EEG)', 'الیکٹروڈ', 'ریکارڈنگ آلہ', 'دماغی لہریں'),
        'ps': ('الکټروانسفالوګرام (EEG)', 'الکترودونه', 'د ثبتولو آله', 'د دماغ څپې'),
    }[lang]
    body = (
        '<path d="M82 125c0-44 28-75 70-75 40 0 63 30 63 69 0 18-8 31-20 40l-4 35h-69l-5-29c-22-9-35-20-35-40z" '
        'fill="#f1c7a8" stroke="#334155" stroke-width="3"/>'
        '<path d="M106 93c13-25 46-31 71-18" fill="none" stroke="#7c3f2c" stroke-width="5"/>'
        '<path d="M180 130h25m-12-12v24" stroke="#334155" stroke-width="3"/>'
        '<path d="M150 83L255 60M176 98L255 90M178 120L255 120" fill="none" stroke="#475569" stroke-width="2"/>'
        '<circle cx="150" cy="83" r="5" fill="#dc2626"/><circle cx="176" cy="98" r="5" fill="#dc2626"/><circle cx="178" cy="120" r="5" fill="#dc2626"/>'
        '<rect x="255" y="40" width="230" height="175" rx="10" fill="#eff6ff" stroke="#334155" stroke-width="3"/>'
        '<rect x="275" y="58" width="190" height="105" fill="#fff" stroke="#94a3b8"/>'
        '<path d="M280 79h18l7-11 9 24 8-13h23l8-9 8 19 9-10h25l8-7 8 18 8-11h19M280 108h26l8-8 8 18 8-11h22l8-12 8 23 8-10h24l8-6 8 17 8-11h19M280 139h18l8-8 8 17 8-9h26l8-13 8 21 8-9h22l8-7 8 16 8-8h19" '
        'fill="none" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="20" y="25" font-size="16">{escape(labels[0])}</text>'
        f'<text x="90" y="218" font-size="14">{escape(labels[1])}</text>'
        f'<text x="270" y="190" font-size="14">{escape(labels[2])}</text>'
        f'<text x="360" y="238" font-size="14" text-anchor="middle">{escape(labels[3])}</text>'
    )
    return make_svg(body, 510, 255, labels)


def ohm_portrait(lang):
    labels = {
        'en': ('Georg Simon Ohm, 1787–1854', 'Georg Simon Ohm (1787–1854)'),
        'ur': ('جارج سائمن اوم، 1787–1854', 'جارج سائمن اوم (1787–1854)'),
        'ps': ('ګیورګ سایمن اوم، 1787–1854', 'ګیورګ سایمن اوم (1787–1854)'),
    }[lang]
    body = (
        '<ellipse cx="110" cy="88" rx="50" ry="58" fill="#f1c7a8" stroke="#334155" stroke-width="3"/>'
        '<path d="M61 76c-7-42 17-67 51-67 32 0 53 20 52 57l-10-20-15 9-17-13-25 12-20-6-9 20z" fill="#334155"/>'
        '<path d="M91 88h7m26 0h7M103 112q9 6 18 0M82 139q28 17 56 0l31 64H52z" fill="#475569" stroke="#334155" stroke-width="3"/>'
        f'<text x="110" y="227" text-anchor="middle" font-size="15">{escape(labels[1])}</text>'
    )
    return make_svg(body, 220, 245, labels)


def ohm_graphs(lang):
    labels = {
        'en': ('Current–voltage graphs (Figure 12.3)', 'Metals', 'Filament bulb', 'Thermistor', 'Semiconductor diode', 'Current I', 'Voltage V', 'V-I graph'),
        'ur': ('رو اور وولٹیج کے گراف (شکل 12.3)', 'دھاتیں', 'فلامنٹ بلب', 'تھرمیسٹر', 'سیمی کنڈکٹر ڈائیوڈ', 'رو I', 'وولٹیج V', 'V-I گراف'),
        'ps': ('د جریان او ولتاژ ګرافونه (شکل 12.3)', 'فلزونه', 'د فلامنټ بلب', 'ترمیسټر', 'نیمه‌هادي ډایوډ', 'جریان I', 'ولتاژ V', 'V-I ګراف'),
    }[lang]
    charts = []
    curves = ('M0 112L112 18', 'M0 112C30 45 62 24 112 17', 'M0 112C35 108 72 80 112 18', 'M0 112C75 112 88 106 94 90C101 69 103 37 112 18')
    for i, curve in enumerate(curves):
        x = 35 + (i % 2) * 285
        y = 63 + (i // 2) * 220
        extra_label = f'<text x="80" y="40" font-size="13">{escape(labels[7])}</text>' if i == 2 else ''
        charts.append(
            f'<g transform="translate({x} {y})"><path d="M0 120H180M25 145V0" fill="none" stroke="#334155" stroke-width="2"/>'
            f'<path d="{curve}" transform="translate(25 8)" fill="none" stroke="#1d4ed8" stroke-width="3"/>'
            f'<text x="8" y="14" font-size="12">{escape(labels[5])}</text><text x="150" y="143" font-size="12">{escape(labels[6])}</text>'
            f'{extra_label}'
            f'<text x="102" y="170" font-size="15" text-anchor="middle">({chr(97+i)}) {escape(labels[1+i])}</text></g>'
        )
    body = f'<text x="310" y="28" text-anchor="middle" font-size="18">{escape(labels[0])}</text>' + ''.join(charts)
    return make_svg(body, 600, 500, labels)


def pair(en, ur, ps):
    return (en, ur, ps)


EEG = [
    pair('FOR YOUR INFORMATION — Electroencephalogram', 'آپ کی معلومات کے لیے — الیکٹرواینسیفلوگرام', 'ستاسو د معلوماتو لپاره — الکټروانسفالوګرام'),
    pair('An electroencephalogram (EEG) is a test that uses metal discs (called electrodes) to evaluate the electrical activity in the brain. The brain constantly generates minute electrical currents even during sleep and in deep coma. The electrodes with thin wires are attached to your scalp which detects tiny electrical charges that result from the activity of your brain cells.', 'الیکٹرواینسیفلوگرام (EEG) ایک ایسا ٹیسٹ ہے جس میں دھاتی ڈسکیں (جنہیں الیکٹروڈ کہتے ہیں) دماغ کی برقی سرگرمی جانچنے کے لیے استعمال ہوتی ہیں۔ دماغ نیند اور گہری بے ہوشی کے دوران بھی مسلسل نہایت معمولی برقی روئیں پیدا کرتا ہے۔ باریک تاروں والے الیکٹروڈ آپ کی کھوپڑی کی جلد پر لگائے جاتے ہیں، جو دماغی خلیوں کی سرگرمی سے پیدا ہونے والے ننھے برقی بار محسوس کرتے ہیں۔', 'الکټروانسفالوګرام (EEG) هغه ازموینه ده چې د دماغ برېښنايي فعالیت د ارزونې لپاره فلزي ډیسکونه (چې الکترودونه بلل کېږي) کاروي. دماغ د خوب او ژورې بې‌هوښۍ پر مهال هم په دوامداره توګه ډېرې کوچنۍ برېښنايي کرنټونه تولیدوي. نري سیم لرونکي الکترودونه د سر پر پوستکي نښلول کېږي؛ دا د دماغي حجرو د فعالیت له امله پیدا شوي واړه برېښنايي چارجونه کشفوي.'),
    pair('The computer records your brains electrical activity on the screen or on a paper as wavy line. These lines allow neurologists to quickly assess whether there are abnormal patterns. An EEG is one of the main diagnostic tests for epilepsy, Brain tumors, Stroke etc.', 'کمپیوٹر دماغ کی برقی سرگرمی کو اسکرین یا کاغذ پر لہردار لکیر کی صورت میں ریکارڈ کرتا ہے۔ یہ لہریں اعصابی ماہرین کو جلد جانچنے دیتی ہیں کہ آیا کوئی غیر معمولی نمونہ موجود ہے۔ EEG مرگی، دماغی رسولیوں، فالج وغیرہ کے لیے اہم تشخیصی ٹیسٹوں میں سے ایک ہے۔', 'کمپیوټر د دماغ برېښنايي فعالیت پر پرده یا پر کاغذ د څپې په څېر کرښه ثبتوي. دا کرښې عصبي متخصصانو ته اجازه ورکوي چې ژر وارزوي ایا غیرعادي بڼې شته. EEG د مرۍ، دماغي تومورونو، سکتې او نورو لپاره له مهمو تشخیصي ازموینو څخه یوه ده.'),
]

OHM = [
    pair('12.2 OHM’S LAW', '12.2 اوم کا قانون', '12.2 د اوم قانون'),
    pair('This law was presented by German scientist George Simon Ohm in (1826). It relates the three fundamental electrical quantities: voltage (V), the current (I) and resistance (R). If a voltage V is applied across a conductor and current (I) flows through it then according to ohm law', 'یہ قانون جرمن سائنس دان جارج سائمن اوم نے (1826) میں پیش کیا۔ یہ تین بنیادی برقی مقداروں: وولٹیج (V)، رو (I) اور مزاحمت (R) کے درمیان تعلق بیان کرتا ہے۔ اگر کسی موصل کے سروں پر وولٹیج V لگائی جائے اور اس میں رو (I) گزرے تو اوم کے قانون کے مطابق', 'دا قانون جرمني ساینسپوه ګیورګ سایمن اوم په (1826) کال کې وړاندې کړ. دا د برېښنا درې بنسټیزې کچې سره تړي: ولتاژ (V)، جریان (I) او مقاومت (R). که د یوه هادي پر پایونو ولتاژ V ولګول شي او جریان (I) ترې تېر شي، نو د اوم د قانون له مخې'),
    pair('The magnitude of the current in a conductor is proportional to the applied voltage as long as the temperature of the conductor is kept constant.', 'موصل میں رو کی مقدار لگائی گئی وولٹیج کے متناسب ہوتی ہے، بشرطیکہ موصل کا درجۂ حرارت مستقل رکھا جائے۔', 'په هادي کې د جریان اندازه له لګېدلي ولتاژ سره متناسب ده، تر هغه چې د هادي تودوخه ثابته وساتل شي.'),
    pair('Georg Simon OHM (1787-1854)', 'جارج سائمن اوم (1787–1854)', 'ګیورګ سایمن اوم (1787–1854)'),
    pair('Georg Simon Ohm was a German physicist and mathematician. He defines the fundamental relationship between voltage, current, and resistance.', 'جارج سائمن اوم یو جرمن طبیعیات دان اور ریاضی دان تھے۔ وہ وولٹیج، رو اور مزاحمت کے درمیان بنیادی تعلق کی تعریف کرتے ہیں۔', 'ګیورګ سایمن اوم جرمنی فزیکپوه او ریاضي‌پوه و. هغه د ولتاژ، جریان او مقاومت ترمنځ بنسټیزه اړیکه تعریفوي.'),
    pair('Mathematically', 'ریاضیاتی طور پر', 'په ریاضيکي بڼه'),
    pair(r'\(I\propto V\) or \(I=\frac{V}{R}\)', r'\(I\propto V\) یا \(I=\frac{V}{R}\)', r'\(I\propto V\) یا \(I=\frac{V}{R}\)'),
    pair(r'or \(V=IR\) ...(12.2)', r'یا \(V=IR\) ...(12.2)', r'یا \(V=IR\) ...(12.2)'),
    pair('Where R is constant, which is known as the resistance of the conducting material. Resistance depends upon the nature, dimension and physical state of the conductor. For a conductor that obeys Ohm’s law, a graph of current I as a function of voltage V is a straight line passing through the origin Figure (12.3(a).', 'جہاں R مستقل ہے اور اسے موصل مادے کی مزاحمت کہتے ہیں۔ مزاحمت موصل کی نوعیت، ابعاد اور طبعی حالت پر منحصر ہوتی ہے۔ اوم کے قانون کی پابندی کرنے والے موصل کے لیے رو I کا وولٹیج V کے تابع گراف مبدأ سے گزرنے والی سیدھی لکیر ہے، شکل (12.3(a).', 'دلته R ثابته ده او د هادي د مقاومت په نوم یادېږي. مقاومت د هادي په طبیعت، ابعادو او فزیکي حالت پورې اړه لري. د اوم د قانون منونکي هادي لپاره د جریان I د ولتاژ V په وړاندې ګراف یوه نېغه کرښه ده چې له مبدأ تېرېږي، شکل (12.3(a).'),
    pair(r'The slope of the line is \(\tan\theta=\frac{I}{V}=\frac{1}{R}\).', r'اس لکیر کا ڈھلوان \(\tan\theta=\frac{I}{V}=\frac{1}{R}\) ہے۔', r'د کرښې مېلان \(\tan\theta=\frac{I}{V}=\frac{1}{R}\) دی.'),
    pair('As R is constant the slope is constant for ohmic conductors. The Ohm’s law is not valid for all conducting material. Those materials for which the slope of I verses V graph is not constant are called non-Ohmic materials. For examples Fig 12.3 (b, c & d) illustrates the non-Ohmic characteristics of the filament of an electric bulb, a thermistor and of a semiconductor diode respectively. The I-V graph for non-Ohmic materials is non linear (curved).', 'چونکہ R مستقل ہے، اس لیے اومی موصلوں کے لیے ڈھلوان مستقل ہوتی ہے۔ اوم کا قانون ہر موصل مادے پر لاگو نہیں ہوتا۔ جن مادوں کے I بمقابلہ V گراف کی ڈھلوان مستقل نہ ہو انہیں غیر اومی مادے کہتے ہیں۔ مثال کے طور پر شکل 12.3 (b، c اور d) بالترتیب برقی بلب کے فلامنٹ، تھرمیسٹر اور سیمی کنڈکٹر ڈائیوڈ کی غیر اومی خصوصیات دکھاتی ہے۔ غیر اومی مادوں کا I-V گراف غیر خطی (خم دار) ہوتا ہے۔', 'ځکه چې R ثابته ده، د اومي هاديانو لپاره مېلان هم ثابت وي. د اوم قانون پر ټولو جریان لېږدوونکو موادو نه پلي کېږي. هغه مواد چې د I پر وړاندې د V ګراف مېلان یې ثابت نه وي، غیر اومي مواد بلل کېږي. د بېلګې په توګه، 12.3 شکل (b، c او d) په ترتیب سره د برېښنايي څراغ فلامنټ، ترمیسټر او نیمه‌هادي ډایوډ غیر اومي ځانګړنې ښيي. د غیر اومي موادو I-V ګراف غیرخطي (کږلېچن) وي.'),
]


def create(identity, title, printed, pairs, layout, titles, visuals=None, printed_pages=None):
    record = {'id': identity, 'title': title, 'kind': 'lesson', 'pdfPage': 33,
              'printedPage': printed, 'sourcePdf': SOURCE, 'paragraphs': [p[0] for p in pairs]}
    item = section(record, pairs, layout, titles)
    item['kind'] = 'lesson'
    if printed_pages:
        item['sourceReferences'] = [{'pdfPage': 33, 'printedPage': page, 'sourcePdf': SOURCE} for page in printed_pages]
    if visuals:
        item.update(visuals)
        item['diagramSvg'] = visuals.get('diagramSvg', '')
        item['diagramSvgUrdu'] = visuals.get('diagramSvgUrdu', '')
        item['diagramSvgPashto'] = visuals.get('diagramSvgPashto', '')
        item['content'] += item['diagramSvg']
    return record, item


if __name__ == '__main__':
    eeg = create('phys12-unit12-eeg56', 'For your information — Electroencephalogram', 56, EEG,
                 [{'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
                  {'type': 'paragraph', 'indices': [2]}, {'type': 'visual'}],
                 ('آپ کی معلومات کے لیے — الیکٹرواینسیفلوگرام', 'ستاسو د معلوماتو لپاره — الکټروانسفالوګرام'),
                 {'diagramSvg': eeg_figure('en'), 'diagramSvgUrdu': eeg_figure('ur'), 'diagramSvgPashto': eeg_figure('ps')})
    ohm_layout = [
        {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
        {'type': 'paragraph', 'indices': [2]}, {'type': 'heading', 'indices': [3]},
        {'type': 'visual'}, {'type': 'paragraph', 'indices': [4]}, {'type': 'heading', 'indices': [5]},
        {'type': 'equation', 'indices': [6]}, {'type': 'equation', 'indices': [7]},
        {'type': 'paragraph', 'indices': [8]}, {'type': 'equation', 'indices': [9]},
        {'type': 'paragraph', 'indices': [10]}, {'type': 'visual'},
    ]
    ohm_visuals = {
        'diagramSvg': ohm_portrait('en') + ohm_graphs('en'),
        'diagramSvgUrdu': ohm_portrait('ur') + ohm_graphs('ur'),
        'diagramSvgPashto': ohm_portrait('ps') + ohm_graphs('ps'),
    }
    law = create('phys12-unit12-ohms-law56-57', '12.2 Ohm’s law', 56, OHM, ohm_layout,
                 ('12.2 اوم کا قانون', '12.2 د اوم قانون'), ohm_visuals, [56, 57])
    upsert([eeg[0], law[0]], [eeg[1], law[1]], chapter_index=1)
    sync_companions(chapter_index=1, formulas=[
        {'id': 'phys12-unit12-eq-12.2', 'name': 'Ohm’s law', 'number': '12.2',
         'formula': OHM[7][0] + ' ' + OHM[8][0], 'latex': r'V=IR',
         'sourceReferences': [{'pdfPage': 33, 'printedPage': 57, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-ohmic-slope', 'name': 'Slope of an ohmic conductor’s I–V graph',
         'formula': OHM[9][0], 'latex': r'\tan\theta=\frac{I}{V}=\frac{1}{R}',
         'sourceReferences': [{'pdfPage': 33, 'printedPage': 57, 'sourcePdf': SOURCE}]},
    ], definitions=[
        {'term': 'Ohm’s law', 'definition': OHM[1][0] + ' ' + OHM[2][0],
         'definitionUrdu': OHM[1][1] + ' ' + OHM[2][1], 'definitionPashto': OHM[1][2] + ' ' + OHM[2][2],
         'sourceReferences': [{'pdfPage': 33, 'printedPage': 56, 'sourcePdf': SOURCE}]},
    ], trim_sections=[{'id': '12.2', 'startsAt': 'EXAMPLE 12.2', 'title': 'Ohm’s law — source review through PDF page 33'}])
    checkpoint(33, 'corrected_verified', [eeg[0]['id'], law[0]['id']],
               'Rendered the complete spread and inspected both printed pages 56–57. Compared the EEG panel and prose; Ohm’s-law introduction, bio panel, equations 12.2, slope relation, non-ohmic explanation and Figure 12.3 against the scan. Rebuilt EEG equipment/traces, schematic Ohm portrait and all four I–V plots as language-labeled inline SVG. Paired every source paragraph with Urdu and Pashto. Preserved the source wording and its printed Figure-reference punctuation. Legacy topic is trimmed at Example 12.2, the next unreviewed source block.',
               printed_pages=[56, 57], chapter_number=12)
