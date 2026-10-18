"""Sequential source correction for PDF page 36 of Class 12 Physics."""
import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
VOCAB = json.loads((ROOT / 'docs/source-verification/class-12/physics-vocabulary-cache-unit12.json').read_text(encoding='utf-8'))['terms']


def v(key, lang):
    return VOCAB[key][lang]


def pair(en, ur, ps):
    return (en, ur, ps)


COEFFICIENT = [
    pair('Where α is the constant and is called temperature co-efficient of resistance. Its value depends upon the nature of material and temperature.', 'جہاں α مستقل ہے اور اسے مزاحمت کا درجۂ حرارت کا ضریب کہتے ہیں۔ اس کی قدر مادے کی نوعیت اور درجۂ حرارت پر منحصر ہے۔', 'دلته α ثابت دی او د مقاومت د تودوخې ضریب بلل کېږي. ارزښت یې د مادې په طبیعت او تودوخې پورې اړه لري.'),
    pair('Rearranging equation (12.6) we get:', 'مساوات (12.6) کو دوبارہ ترتیب دینے سے ملتا ہے:', 'د (12.6) معادلې له بیا تنظیمولو څخه ترلاسه کوو:'),
    pair(r'\(R_T=R_0(1+\alpha T)\) ...(12.7)', r'\(R_T=R_0(1+\alpha T)\) ...(12.7)', r'\(R_T=R_0(1+\alpha T)\) ...(12.7)'),
    pair('From equation (12.6) we get:', 'مساوات (12.6) سے ملتا ہے:', 'له (12.6) معادلې څخه ترلاسه کوو:'),
    pair(r'\(\alpha=\frac{R_T-R_0}{R_0T}\) ...(12.8)', r'\(\alpha=\frac{R_T-R_0}{R_0T}\) ...(12.8)', r'\(\alpha=\frac{R_T-R_0}{R_0T}\) ...(12.8)'),
    pair('Temperature co-efficient of resistance α may be defined as increase in resistance per ohm original resistance per degree rise in temperature.', 'مزاحمت کے درجۂ حرارت کے ضریب α کی تعریف یہ ہے: درجۂ حرارت میں فی درجے اضافے پر اصل مزاحمت کے فی اوم میں مزاحمت کا اضافہ۔', 'د مقاومت د تودوخې ضریب α داسې تعریفېدای شي: د تودوخې د هرې درجې لوړېدو پر مهال د اصلي مقاومت په هر اوم کې د مقاومت زیاتوالی.'),
    pair('The unit of α as derived from the definition is K⁻¹. Since the resistance of metals increases with the rise in temperature, they have positive temperature co-efficient of resistance, while co-efficient α is negative for semiconductor because they show decrease in resistance as the temperature raises. The resistivity or specific resistance of most materials increases linearly with increasing temperature. The equation (12.8) also apply to ρ. At temperature T the resistivity ρ_T of a material is given by', 'د تعریف له مخې د α اکائی K⁻¹ ہے۔ چونکہ دھاتوں کی مزاحمت درجۂ حرارت بڑھنے سے بڑھتی ہے، اس لیے ان کا ضریبِ مزاحمت مثبت ہوتا ہے، جبکہ سیمی کنڈکٹر کے لیے ضریب α منفی ہے کیونکہ درجۂ حرارت بڑھنے پر ان کی مزاحمت کم ہوتی ہے۔ زیادہ تر مادوں کی مزاحمت النوعی درجۂ حرارت بڑھنے سے خطی طور پر بڑھتی ہے۔ مساوات (12.8) کا اطلاق ρ پر بھی ہوتا ہے۔ درجۂ حرارت T پر کسی مادے کی مزاحمت النوعی ρ_T یہ ہے:', 'د تعریف له مخې د α واحد K⁻¹ دی. څرنګه چې د فلزونو مقاومت د تودوخې په لوړېدو زیاتېږي، نو د مقاومت د تودوخې ضریب یې مثبت وي؛ خو د نیمه‌هادي لپاره ضریب α منفي وي، ځکه د تودوخې په لوړېدو یې مقاومت کمېږي. د ډېرو موادو مخصوص مقاومت د تودوخې په زیاتېدو سره په خطي ډول لوړېږي. (12.8) معادله پر ρ هم پلي کېږي. په T تودوخه کې د مادې مخصوص مقاومت ρ_T داسې دی:'),
    pair(r'\(\rho_T=\rho_0(1+\alpha T)\) ...(12.9)', r'\(\rho_T=\rho_0(1+\alpha T)\) ...(12.9)', r'\(\rho_T=\rho_0(1+\alpha T)\) ...(12.9)'),
    pair(r'\(\alpha=\frac{\rho_T-\rho_0}{\rho_0T}\) ...(12.10)', r'\(\alpha=\frac{\rho_T-\rho_0}{\rho_0T}\) ...(12.10)', r'\(\alpha=\frac{\rho_T-\rho_0}{\rho_0T}\) ...(12.10)'),
]

EXAMPLE123 = [
    pair('EXAMPLE 12.3', 'مثال 12.3', 'بېلګه 12.3'),
    pair('A transmission line made of copper has a resistance of 100 Ω at 0°C. Calculate the change in resistance between summer and winter, knowing that temperature varies from +35°C to -30°C. Assume the temperature co-efficient of copper to be 0.00427/°C at 0°C.', 'تانبے کی بنی ایک ترسیلی لائن کی مزاحمت 0°C پر 100 Ω ہے۔ گرمیوں اور سردیوں کے درمیان مزاحمت میں تبدیلی معلوم کریں، جبکہ درجۂ حرارت +35°C سے -30°C تک بدلتا ہے۔ فرض کریں کہ 0°C پر تانبے کا درجۂ حرارت کا ضریب 0.00427/°C ہے۔', 'د مسو د لېږد کرښه په 0°C کې 100 Ω مقاومت لري. د اوړي او ژمي ترمنځ د مقاومت بدلون محاسبه کړئ، په دې پوهېدو سره چې تودوخه له +35°C څخه -30°C ته بدلېږي. فرض کړئ چې په 0°C کې د مسو د تودوخې ضریب 0.00427/°C دی.'),
    pair('GIVEN', 'معلوم ہے', 'ورکړل شوي'),
    pair(r'Temperature \(T_1=+35°C\), temperature \(T_2=-30°C\), resistance \(R_0=100\,\Omega\), temperature co-efficient of copper \(\alpha=0.00427/°C\)', r'درجۂ حرارت \(T_1=+35°C\)، درجۂ حرارت \(T_2=-30°C\)، مزاحمت \(R_0=100\,\Omega\)، تانبے کا درجۂ حرارت کا ضریب \(\alpha=0.00427/°C\)', r'تودوخه \(T_1=+35°C\)، تودوخه \(T_2=-30°C\)، مقاومت \(R_0=100\,\Omega\)، د مسو د تودوخې ضریب \(\alpha=0.00427/°C\)'),
    pair('REQUIRED', 'مطلوب', 'غوښتل شوي'),
    pair(r'Change in resistance \(R=?\)', r'مزاحمت میں تبدیلی \(R=?\)', r'د مقاومت بدلون \(R=?\)'),
    pair('SOLUTION', 'حل', 'حل'),
    pair(r'\(R_T=R_0(1+\alpha T)\)', r'\(R_T=R_0(1+\alpha T)\)', r'\(R_T=R_0(1+\alpha T)\)'),
    pair(r'\(\Rightarrow R_{-30}=100(1+0.00427(-30))\)', r'\(\Rightarrow R_{-30}=100(1+0.00427(-30))\)', r'\(\Rightarrow R_{-30}=100(1+0.00427(-30))\)'),
    pair(r'\(\Rightarrow R_{-30}=87.2\,\Omega\)', r'\(\Rightarrow R_{-30}=87.2\,\Omega\)', r'\(\Rightarrow R_{-30}=87.2\,\Omega\)'),
    pair(r'similarly \(R_{+35}=100[1+0.00427(35)]\)', r'اسی طرح \(R_{+35}=100[1+0.00427(35)]\)', r'همدارنګه \(R_{+35}=100[1+0.00427(35)]\)'),
    pair(r'\(R_{+35}=115\,\Omega\)', r'\(R_{+35}=115\,\Omega\)', r'\(R_{+35}=115\,\Omega\)'),
    pair(r'Change in resistance \(=115-87.2=27.8\,\Omega\)', r'مزاحمت میں تبدیلی \(=115-87.2=27.8\,\Omega\)', r'د مقاومت بدلون \(=115-87.2=27.8\,\Omega\)'),
]

EXAMPLE124 = [
    pair('EXAMPLE 12.4', 'مثال 12.4', 'بېلګه 12.4'),
    pair('Calculate the resistance of copper conductor having a length of 2 km and a cross-section of 22 mm². Assume the resistivity is 18 × 10⁻⁹ Ω.m.', '2 km لمبے اور 22 mm² رقبۂ مقطع والے تانبے کے موصل کی مزاحمت معلوم کریں۔ فرض کریں کہ مزاحمت النوعی 18 × 10⁻⁹ Ω.m ہے۔', 'د مسو د هغه هادي مقاومت محاسبه کړئ چې اوږدوالی یې 2 km او د مقطع مساحت یې 22 mm² دی. فرض کړئ چې مخصوص مقاومت 18 × 10⁻⁹ Ω.m دی.'),
    pair('GIVEN', 'معلوم ہے', 'ورکړل شوي'),
    pair(r'Length \(L=2\,\mathrm{km}=2000\,\mathrm m\); cross-section \(A=22\,\mathrm{mm}^2=22\times10^{-6}\,\mathrm m^2\); resistivity \(\rho=18\times10^{-9}\,\Omega.\mathrm m\)', r'لمبائی \(L=2\,\mathrm{km}=2000\,\mathrm m\)؛ رقبۂ مقطع \(A=22\,\mathrm{mm}^2=22\times10^{-6}\,\mathrm m^2\)؛ مزاحمت النوعی \(\rho=18\times10^{-9}\,\Omega.\mathrm m\)', r'اوږدوالی \(L=2\,\mathrm{km}=2000\,\mathrm m\)؛ د مقطع مساحت \(A=22\,\mathrm{mm}^2=22\times10^{-6}\,\mathrm m^2\)؛ مخصوص مقاومت \(\rho=18\times10^{-9}\,\Omega.\mathrm m\)'),
    pair('REQUIRED', 'مطلوب', 'غوښتل شوي'),
    pair(r'Resistance of copper \(R=?\)', r'تانبے کی مزاحمت \(R=?\)', r'د مسو مقاومت \(R=?\)'),
    pair('SOLUTION', 'حل', 'حل'),
    pair('The resistance of copper wire of length L, cross-sectional area A and resistivity ρ is given by', 'L لمبائی، A رقبۂ مقطع اور ρ مزاحمت النوعی والی تانبے کی تار کی مزاحمت یہ ہے:', 'د مسو د هغه سیم مقاومت چې اوږدوالی یې L، د مقطع مساحت یې A او مخصوص مقاومت یې ρ وي، داسې دی:'),
    pair(r'\(R=\frac{\rho L}{A}\)', r'\(R=\frac{\rho L}{A}\)', r'\(R=\frac{\rho L}{A}\)'),
    pair('Thus resistance of copper conductor is', 'چنانچہ تانبے کے موصل کی مزاحمت یہ ہے:', 'نو د مسو د هادي مقاومت داسې دی:'),
    pair(r'\(R=18\times10^{-9}\times\frac{2000}{22\times10^{-6}}\)', r'\(R=18\times10^{-9}\times\frac{2000}{22\times10^{-6}}\)', r'\(R=18\times10^{-9}\times\frac{2000}{22\times10^{-6}}\)'),
    pair(r'\(R=1.64\,\Omega\)', r'\(R=1.64\,\Omega\)', r'\(R=1.64\,\Omega\)'),
]

ASSIGNMENT = [
    pair('ASSIGNMENT 12.1', 'اسائنمنٹ 12.1', 'دنده 12.1'),
    pair(r'(a) Calculate the resistance per unit length of a 22 nichrome wire of radius 0.321mm. (b) If a potential difference of 10V is maintained across 1m length of nichrome wire, what is the current in the wire? \(\rho_{\mathrm{nichromes}}=1.5\times10^{-6}\,\Omega.\mathrm m\). answer(4.6 Ω/m, 2.2 A)', r'(a) 0.321mm رداس والی 22 نائیکروم تار کی فی اکائی لمبائی مزاحمت معلوم کریں۔ (b) اگر نائیکروم تار کی 1m لمبائی کے سروں پر 10V فرقِ پوٹینشل برقرار رکھا جائے تو تار میں رو کتنی ہوگی؟ \(\rho_{\mathrm{nichromes}}=1.5\times10^{-6}\,\Omega.\mathrm m\)۔ جواب(4.6 Ω/m, 2.2 A)', r'(a) د 0.321mm شعاع لرونکي د 22 نایکروم سیم د هر واحد اوږدوالي مقاومت محاسبه کړئ. (b) که د نایکروم سیم د 1m اوږدوالي پر سرونو 10V پوتنشیالي توپیر وساتل شي، په سیم کې جریان څو دی؟ \(\rho_{\mathrm{nichromes}}=1.5\times10^{-6}\,\Omega.\mathrm m\). ځواب(4.6 Ω/m, 2.2 A)'),
]

WIRE_WOUND = [
    pair('12.5 WIRE-WOUND VARIABLE RESISTORS', '12.5 تار لپٹے متغیر مزاحم', '12.5 په سیم تاو شوي متغیر مقاومتونه'),
    pair('High stability and high accuracy resistors are always wire-wound. It is then enclosed in an insulating cover.', 'زیادہ استحکام اور زیادہ درستی والے مزاحم ہمیشہ تار لپیٹ کر بنائے جاتے ہیں۔ پھر انہیں ایک عایق غلاف میں بند کیا جاتا ہے۔', 'لوړ ثبات او لوړه کره‌والی لرونکي مقاومتونه تل د سیم په تاوولو جوړېږي. بیا په عایق پوښ کې بندېږي.'),
    pair('Generally, nickel chromium is used because of its very small temperature co-efficient of resistance. Wire wound resistors can safely operate at higher temperatures than carbon type resistors. Wire wound variable resistor can be used in two ways.', 'عموماً نکل کرومیم استعمال کیا جاتا ہے کیونکہ اس کا مزاحمت کا درجۂ حرارت کا ضریب بہت کم ہوتا ہے۔ تار لپٹے مزاحم کاربن قسم کے مزاحموں سے زیادہ درجۂ حرارت پر محفوظ طور پر کام کر سکتے ہیں۔ تار لپٹا متغیر مزاحم دو طریقوں سے استعمال کیا جا سکتا ہے۔', 'عموماً نکل کرومیم کارول کېږي، ځکه د مقاومت د تودوخې ضریب یې ډېر لږ دی. په سیم تاو شوي مقاومتونه د کاربن ډوله مقاومتونو په پرتله په لوړو تودوخې کې په خوندي ډول کار کوي. په سیم تاو شوی متغیر مقاومت په دوو لارو کارېدای شي.'),
    pair('i) Rheostats     ii) Potential divider', 'i) ریوسٹیٹ     ii) پوٹینشل ڈیوائیڈر', 'i) ریوستات     ii) پوتنشیالي وېشونکی'),
]


def make_record(identity, title, printed, pairs, layout, headings, printed_pages):
    record = {'id': identity, 'title': title, 'kind': 'lesson', 'pdfPage': 36,
              'printedPage': printed, 'sourcePdf': SOURCE, 'paragraphs': [p[0] for p in pairs]}
    item = section(record, pairs, layout, headings)
    item['kind'] = 'lesson'
    item['sourceReferences'] = [{'pdfPage': 36, 'printedPage': page, 'sourcePdf': SOURCE} for page in printed_pages]
    return record, item


if __name__ == '__main__':
    coefficient_layout = [
        {'type': 'paragraph', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
        {'type': 'equation', 'indices': [2]}, {'type': 'paragraph', 'indices': [3]},
        {'type': 'equation', 'indices': [4]}, {'type': 'paragraph', 'indices': [5]},
        {'type': 'paragraph', 'indices': [6]}, {'type': 'equation', 'indices': [7]},
        {'type': 'equation', 'indices': [8]},
    ]
    coefficient = make_record('phys12-unit12-coefficient-resistivity62', 'Temperature coefficient of resistance and resistivity — continuation', 62,
        COEFFICIENT, coefficient_layout, ('د مزاحمت او مزاحمت النوعی د تودوخې ضریب — دوام', 'مزاحمت او مخصوص مقاومت — دوام'), [62])
    ex123_layout = [
        {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
        {'type': 'heading', 'indices': [2]}, {'type': 'paragraph', 'indices': [3]},
        {'type': 'heading', 'indices': [4]}, {'type': 'paragraph', 'indices': [5]},
        {'type': 'heading', 'indices': [6]}, {'type': 'equation', 'indices': [7]},
        {'type': 'equation', 'indices': [8]}, {'type': 'equation', 'indices': [9]},
        {'type': 'equation', 'indices': [10]}, {'type': 'equation', 'indices': [11]},
        {'type': 'equation', 'indices': [12]},
    ]
    ex123 = make_record('phys12-unit12-example12362', 'Example 12.3 — change in copper resistance', 62,
        EXAMPLE123, ex123_layout, ('مثال 12.3 — تانبے کی مزاحمت میں تبدیلی', 'بېلګه 12.3 — د مسو په مقاومت کې بدلون'), [62])
    ex124_layout = [
        {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
        {'type': 'heading', 'indices': [2]}, {'type': 'paragraph', 'indices': [3]},
        {'type': 'heading', 'indices': [4]}, {'type': 'paragraph', 'indices': [5]},
        {'type': 'heading', 'indices': [6]}, {'type': 'paragraph', 'indices': [7]},
        {'type': 'equation', 'indices': [8]}, {'type': 'paragraph', 'indices': [9]},
        {'type': 'equation', 'indices': [10]}, {'type': 'equation', 'indices': [11]},
    ]
    ex124 = make_record('phys12-unit12-example12463', 'Example 12.4 — resistance of a copper conductor', 63,
        EXAMPLE124, ex124_layout, ('مثال 12.4 — تانبے کے موصل کی مزاحمت', 'بېلګه 12.4 — د مسو د هادي مقاومت'), [63])
    assignment_layout = [{'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]}]
    assignment = make_record('phys12-unit12-assignment12163', 'Assignment 12.1 — nichrome wire', 63,
        ASSIGNMENT, assignment_layout, ('اسائنمنٹ 12.1 — نائیکروم تار', 'دنده 12.1 — نایکروم سیم'), [63])
    wire_layout = [
        {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
        {'type': 'paragraph', 'indices': [2]}, {'type': 'paragraph', 'indices': [3]},
    ]
    wire = make_record('phys12-unit12-wirewound-resistors63', '12.5 Wire-wound variable resistors — introduction', 63,
        WIRE_WOUND, wire_layout, ('12.5 تار لپٹے متغیر مزاحم — تعارف', '12.5 په سیم تاو شوي متغیر مقاومتونه — سریزه'), [63])

    records = [coefficient[0], ex123[0], ex124[0], assignment[0], wire[0]]
    sections = [coefficient[1], ex123[1], ex124[1], assignment[1], wire[1]]
    upsert(records, sections, chapter_index=1)
    worked = [
        {'id': 'textbook-example-12-3', 'num': '12.3', 'title': 'Example 12.3', 'problem': EXAMPLE123[1][0],
         'given': [EXAMPLE123[3][0]], 'required': [EXAMPLE123[5][0]],
         'steps': [EXAMPLE123[i][0] for i in range(7, 13)], 'answer': r'27.8\,\Omega',
         'solutionOrigin': 'textbook', 'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
        {'id': 'textbook-example-12-4', 'num': '12.4', 'title': 'Example 12.4', 'problem': EXAMPLE124[1][0],
         'given': [EXAMPLE124[3][0]], 'required': [EXAMPLE124[5][0]],
         'steps': [EXAMPLE124[i][0] for i in (7, 8, 9, 10, 11)], 'answer': r'1.64\,\Omega',
         'solutionOrigin': 'textbook', 'sourceReferences': [{'pdfPage': 36, 'printedPage': 63, 'sourcePdf': SOURCE}]},
    ]
    assignment_card = {'id': 'assignment-12-1', 'title': 'Assignment 12.1', 'problems': [
        {'id': 'assignment-12-1-q1', 'question': ASSIGNMENT[1][0],
         'questionUrdu': ASSIGNMENT[1][1], 'questionPashto': ASSIGNMENT[1][2],
         'answer': '4.6 Ω/m, 2.2 A', 'solutionOrigin': 'textbook answer',
         'sourceReferences': [{'pdfPage': 36, 'printedPage': 63, 'sourcePdf': SOURCE}]}
    ]}
    sync_companions(chapter_index=1, formulas=[
        {'id': 'phys12-unit12-eq-12.7', 'name': 'Resistance at temperature T', 'number': '12.7',
         'formula': COEFFICIENT[2][0], 'latex': r'R_T=R_0(1+\alpha T)', 'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-eq-12.8', 'name': 'Temperature coefficient of resistance', 'number': '12.8',
         'formula': COEFFICIENT[4][0], 'latex': r'\alpha=\frac{R_T-R_0}{R_0T}', 'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-eq-12.9', 'name': 'Resistivity at temperature T', 'number': '12.9',
         'formula': COEFFICIENT[7][0], 'latex': r'\rho_T=\rho_0(1+\alpha T)', 'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-eq-12.10', 'name': 'Temperature coefficient of resistivity', 'number': '12.10',
         'formula': COEFFICIENT[8][0], 'latex': r'\alpha=\frac{\rho_T-\rho_0}{\rho_0T}', 'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
    ], definitions=[
        {'term': 'Temperature coefficient of resistance', 'definition': COEFFICIENT[5][0],
         'definitionUrdu': COEFFICIENT[5][1], 'definitionPashto': COEFFICIENT[5][2],
         'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
        {'term': 'Temperature coefficient of resistivity',
         'definition': COEFFICIENT[6][0] + ' ' + COEFFICIENT[7][0] + ' ' + COEFFICIENT[8][0],
         'definitionUrdu': COEFFICIENT[6][1] + ' ' + COEFFICIENT[7][1] + ' ' + COEFFICIENT[8][1],
         'definitionPashto': COEFFICIENT[6][2] + ' ' + COEFFICIENT[7][2] + ' ' + COEFFICIENT[8][2],
         'sourceReferences': [{'pdfPage': 36, 'printedPage': 62, 'sourcePdf': SOURCE}]},
    ], worked_examples=worked, exercises=[assignment_card], retire_sections=['12.3'],
       trim_sections=[{'id': '12.4', 'startsAt': 'i) RHEOSTATS\nNOT FORSALE\n64',
                       'title': '12.5 Rheostats — continuation pending source review'}])
    checkpoint(36, 'corrected_verified', [record['id'] for record in records],
        'Rendered PDF page 36 and inspected printed pages 62–63. Compared all coefficient prose and Eqs. 12.7–12.10, complete Example 12.3 solution, Example 12.4 data/substitution/result, Assignment 12.1 wording and printed answers, and the wire-wound resistor introduction. Added aligned Urdu/Pashto text, textbook worked-example cards and the source-answer exercise card. Reused cached Unit 12 vocabulary and retired covered legacy pages 60–62 while retaining the unreviewed printed-page-64 rheostat continuation.',
        printed_pages=[62, 63], chapter_number=12)
