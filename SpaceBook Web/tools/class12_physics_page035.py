"""Sequential source correction for PDF page 35 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
VOCAB = json.loads((ROOT / 'docs/source-verification/class-12/physics-vocabulary-cache-unit12.json').read_text(encoding='utf-8'))['terms']


def v(key, lang):
    return VOCAB[key][lang]


def pair(en, ur, ps):
    return (en, ur, ps)


def svg(body, label, width=510, height=210):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
            f'aria-label="{escape(label, quote=True)}" style="width:100%;max-width:{width}px;height:auto">'
            f'<rect width="100%" height="100%" fill="#fff"/>{body}</svg>')


def material_wire(lang):
    labels = {
        'en': ('Cross-section area of a material', '1 m', '1 m²', 'FIGURE 12.4'),
        'ur': ('مادے کا رقبۂ مقطع', '1 میٹر', '1 مربع میٹر', 'شکل 12.4'),
        'ps': ('د مادې د مقطع مساحت', '1 متر', '1 مربع متر', 'شکل 12.4'),
    }[lang]
    body = (
        '<path d="M92 65H385V137H92Z" fill="#dbeafe" stroke="#334155" stroke-width="3"/>'
        '<ellipse cx="92" cy="101" rx="20" ry="36" fill="#7dd3fc" stroke="#334155" stroke-width="3"/>'
        '<ellipse cx="385" cy="101" rx="20" ry="36" fill="#bfdbfe" stroke="#334155" stroke-width="3"/>'
        '<path d="M92 164H385M92 158V171M385 158V171" stroke="#334155" stroke-width="2"/>'
        f'<text x="238" y="190" text-anchor="middle" font-size="16">{escape(labels[1])}</text>'
        f'<text x="85" y="54" text-anchor="middle" font-size="15">{escape(labels[2])}</text>'
        f'<text x="391" y="54" text-anchor="middle" font-size="15">{escape(labels[2])}</text>'
        f'<text x="250" y="30" text-anchor="middle" font-size="17">{escape(labels[0])}</text>'
        f'<text x="14" y="30" font-size="13">{escape(labels[3])}</text>'
    )
    return svg(body, labels[3] + ': ' + labels[0], 480, 210)


RESISTIVITY = [
    pair(r'\(R=\rho\frac{L}{A}\) ...(12.3)', r'\(R=\rho\frac{L}{A}\) ...(12.3)', r'\(R=\rho\frac{L}{A}\) ...(12.3)'),
    pair("Where ρ (Greek LETTER 'Rho') is a constant and is known as resistivity or specific resistance of the material.", 'جہاں ρ (یونانی حرف رو) ایک مستقل ہے اور اسے مادے کی مزاحمت النوعی یا مخصوص مزاحمت کہتے ہیں۔', 'دلته ρ (د یوناني الفبا د رو توری) یو ثابت دی او د مادې مخصوص مقاومت یا resistivity بلل کېږي.'),
    pair('The specific resistance of a material is the resistance offered by 1m length of wire of a material having an area of cross-section of 1m². A wire of 1 metre length is shown in figure 12.4. The unit of resistivity is ohm-meter (Ω.m). The resistivity of a substance varies over a wide range. To give an idea to the reader, the following table may be referred.', 'کسی مادے کی مخصوص مزاحمت وہ مزاحمت ہے جو اس مادے کی 1m لمبی تار، جس کا رقبۂ مقطع 1m² ہو، پیش کرتی ہے۔ شکل 12.4 میں 1 میٹر لمبی تار دکھائی گئی ہے۔ مزاحمت النوعی کی اکائی اوم میٹر (Ω.m) ہے۔ کسی مادے کی مزاحمت النوعی کی حد بہت وسیع ہوتی ہے۔ اس کا اندازہ دینے کے لیے درج ذیل جدول دیکھا جا سکتا ہے۔', 'د یوې مادې مخصوص مقاومت هغه مقاومت دی چې د هماغې مادې د 1m اوږد سیم له خوا وړاندې کېږي، که د مقطع مساحت یې 1m² وي. په 12.4 شکل کې د 1 متر اوږد سیم ښودنه شوې. د مخصوص مقاومت واحد اوم متر (Ω.m) دی. د یوې مادې مخصوص مقاومت پراخه کچه لري. د لوستونکي د پوهولو لپاره لاندې جدول کتلای شي.'),
]

TABLE_AND_CONDUCTANCE = [
    pair('The resistivity of metals and alloys is very small. Therefore, these materials are good conductors of electric current. On the other hand, resistivity of insulators is extremely large. As a result, these materials hardly conduct any current. There is also an intermediate class of material known as semiconductors. The resistivity of these substances lies between conductors and insulators.', 'دھاتوں اور مرکبات کی مزاحمت النوعی بہت کم ہوتی ہے۔ اس لیے یہ مادے برقی رو کے اچھے موصل ہیں۔ دوسری طرف، عایقوں کی مزاحمت النوعی بہت زیادہ ہوتی ہے، اس لیے یہ مادے بمشکل کوئی رو گزارتے ہیں۔ مادوں کی ایک درمیانی جماعت بھی ہے جسے سیمی کنڈکٹر کہتے ہیں۔ ان مادوں کی مزاحمت النوعی موصلوں اور عایقوں کے درمیان ہوتی ہے۔', 'د فلزونو او الیاژونو مخصوص مقاومت ډېر لږ وي. له همدې امله دا مواد د برېښنايي جریان ښه هاديان دي. برعکس، د عایقونو مخصوص مقاومت خورا لوړ وي، نو دا مواد نږدې هېڅ جریان نه لېږدوي. د موادو یوه منځنۍ ډله هم شته چې نیمه‌هادیان بلل کېږي. د دغو موادو مخصوص مقاومت د هاديانو او عایقونو ترمنځ وي.'),
    pair("The resistivity’s of some metals.", 'د ځینو دھاتوں کی مزاحمت النوعی۔', 'د ځینو فلزونو مخصوص مقاومت.'),
    pair('Metals — Resistivity (μΩm)', 'دھاتیں — مزاحمت (μΩm)', 'فلزونه — مخصوص مقاومت (μΩm)'),
    pair('Copper (hard drawn) — 0.0178', 'تانبا (سخت کھینچی ہوئی تار) — 0.0178', 'مس (سخت کش شوی سیم) — 0.0178'),
    pair('Aluminium — 0.0285', 'ایلومینیم — 0.0285', 'المونیم — 0.0285'),
    pair('Tin — 0.114', 'ٹن — 0.114', 'قلعي — 0.114'),
    pair('Silver — 0.0163', 'چاندی — 0.0163', 'سپین زر — 0.0163'),
    pair('Brass — 0.06-0.09', 'پیتل — 0.06-0.09', 'برنج — 0.06-0.09'),
    pair('Iron — 0.1', 'لوہا — 0.1', 'اوسپنه — 0.1'),
    pair('Lead — 0.219', 'سیسہ — 0.219', 'سرب — 0.219'),
    pair('CONDUCTANCE', v('conductance', 'ur'), v('conductance', 'ps')),
    pair('The reciprocal of resistance of a conductor is called conductance (G). If a conductor has resistance R, then its conductance G is given by', 'موصل کی مزاحمت کے معکوس کو موصلت (G) کہتے ہیں۔ اگر موصل کی مزاحمت R ہو تو اس کی موصلت G یہ ہے:', 'د هادي د مقاومت معکوس ته هاديتوب (G) ویل کېږي. که د هادي مقاومت R وي، نو هاديتوب G یې داسې دی:'),
    pair(r'\(G=\frac1R\) ...(12.4)', r'\(G=\frac1R\) ...(12.4)', r'\(G=\frac1R\) ...(12.4)'),
    pair('The SI unit of conductance is mho (i.e. ohm spelled back ward) these days, it is a usual practice to use Siemen as the unit of conductance. It is denoted by symbol S.', 'موصلت کی SI اکائی mho (یعنی ohm کو الٹا لکھنے سے بنا لفظ) ہے۔ آج کل موصلت کی اکائی کے طور پر Siemen استعمال کرنے کا رواج ہے۔ اسے علامت S سے ظاہر کرتے ہیں۔', 'د هاديتوب د SI واحد mho دی (یعنې د ohm توری سرچپه لیکل شوی). اوس د هاديتوب د واحد په توګه د Siemen کارول معمول دي. د S په نښه ښودل کېږي.'),
    pair('CONDUCTIVITY', v('conductivity', 'ur'), v('conductivity', 'ps')),
    pair('The reciprocal of resistivity of a conductor is called its conductivity. It is denoted by the symbol σ. If a conductor has resistivity ρ, then its conductivity is given by', 'موصل کی مزاحمت النوعی کے معکوس کو اس کی برقی چالکتا کہتے ہیں۔ اسے علامت σ سے ظاہر کرتے ہیں۔ اگر موصل کی مزاحمت النوعی ρ ہو تو اس کی چالکتا یہ ہے:', 'د هادي د مخصوص مقاومت معکوس یې برېښنايي لېږدوړتیا بلل کېږي. په σ نښه ښودل کېږي. که د هادي مخصوص مقاومت ρ وي، نو لېږدوړتیا یې داسې ده:'),
    pair(r'\(\sigma=\frac1\rho=\frac{L}{RA}\) ...(12.5)', r'\(\sigma=\frac1\rho=\frac{L}{RA}\) ...(12.5)', r'\(\sigma=\frac1\rho=\frac{L}{RA}\) ...(12.5)'),
    pair('The unit of conductivity is mho m⁻¹ or siemen meter⁻¹ (S.m⁻¹).', 'چالکتا کی اکائی mho m⁻¹ یا siemen meter⁻¹ (S.m⁻¹) ہے۔', 'د لېږدوړتیا واحد mho m⁻¹ یا siemen meter⁻¹ (S.m⁻¹) دی.'),
]

TEMPERATURE = [
    pair('12.4 EFFECT OF TEMPERATURE ON RESISTANCE', '12.4 درجۂ حرارت کا مزاحمت پر اثر', '12.4 د تودوخې اغېز پر مقاومت'),
    pair('The resistance of a material changes with the change in temperature. The effect of temperature upon resistance varies according to the type of material.', 'درجۂ حرارت بدلنے سے مادے کی مزاحمت بدلتی ہے۔ مزاحمت پر درجۂ حرارت کا اثر مادے کی قسم کے مطابق مختلف ہوتا ہے۔', 'د تودوخې په بدلېدو سره د مادې مقاومت بدلېږي. پر مقاومت د تودوخې اغېز د مادې له ډول سره سم توپیر لري.'),
    pair('i) Thus resistance of a conductor (e.g. copper, aluminum) increases with the increase of temperature. The change in resistance is fairly regular for normal range of temperatures.', 'i) چنانچہ موصل (مثلاً تانبا، ایلومینیم) کی مزاحمت درجۂ حرارت بڑھنے سے بڑھتی ہے۔ معمول کی درجۂ حرارت کی حدود میں مزاحمت کی تبدیلی کافی باقاعدہ ہوتی ہے۔', 'i) د هادي (لکه مس او المونیم) مقاومت د تودوخې په لوړېدو سره زیاتېږي. د تودوخې په عادي کچه کې د مقاومت بدلون تر ډېره منظم وي.'),
    pair('ii) The resistance of electrolytes, insulators (e.g. glass, mica, rubber etc.) and semiconductors (e.g. germanium, silicon etc.) decreases with the increase in temperature.', 'ii) الیکٹرولائٹس، عایقوں (مثلاً شیشہ، ابرق، ربڑ وغیرہ) اور سیمی کنڈکٹروں (مثلاً جرمانیئم، سلیکان وغیرہ) کی مزاحمت درجۂ حرارت بڑھنے سے کم ہوتی ہے۔', 'ii) د الکترولایتونو، عایقونو (لکه ښیښه، مایکا، ربړ او نور) او نیمه‌هاديانو (لکه جرمانیم، سیلیکون او نور) مقاومت د تودوخې په لوړېدو سره کمېږي.'),
    pair('12.4.1 TEMPERATURE CO-EFFICIENT OF RESISTANCE/RESISTIVITY', '12.4.1 د مزاحمت/مزاحمت النوعی د درجۂ حرارت ضریب', '12.4.1 د مقاومت/مخصوص مقاومت د تودوخې ضریب'),
    pair('Consider a conductor having resistance R₀ at 0°C and R_T at T °C. It has been found that in the normal range of temperatures, the increase in resistance (R_T − R₀) is', 'ایسا موصل لیں جس کی 0°C پر مزاحمت R₀ اور T°C پر R_T ہو۔ معلوم ہوا ہے کہ درجۂ حرارت کی معمول کی حدود میں مزاحمت (R_T − R₀) میں اضافہ', 'یو هادي په پام کې ونیسئ چې په 0°C کې مقاومت R₀ او په T°C کې R_T وي. موندل شوې چې د تودوخې په عادي کچه کې د مقاومت زیاتوالی (R_T − R₀)'),
    pair(r'i) Directly proportional to the initial resistance i.e. \(R_T-R_0\propto R_0\)', r'i) ابتدائی مزاحمت کے براہِ راست متناسب ہے، یعنی \(R_T-R_0\propto R_0\)', r'i) له لومړني مقاومت سره نېغ په نېغه متناسب دی، یعنې \(R_T-R_0\propto R_0\)'),
    pair(r'ii) Directly proportional to the rise in temperature i.e. \(R_T-R_0\propto T\)', r'ii) درجۂ حرارت میں اضافے کے براہِ راست متناسب ہے، یعنی \(R_T-R_0\propto T\)', r'ii) د تودوخې له لوړېدو سره نېغ په نېغه متناسب دی، یعنې \(R_T-R_0\propto T\)'),
    pair('Combining the above two relations, we get', 'مندرجہ بالا دونوں تعلقات کو ملانے سے ملتا ہے:', 'د پورته دوو اړیکو له یوځای کولو څخه ترلاسه کوو:'),
    pair(r'\(R_T-R_0\propto R_0T\)', r'\(R_T-R_0\propto R_0T\)', r'\(R_T-R_0\propto R_0T\)'),
    pair(r'\(R_T-R_0=\alpha R_0T\) ...(12.6)', r'\(R_T-R_0=\alpha R_0T\) ...(12.6)', r'\(R_T-R_0=\alpha R_0T\) ...(12.6)'),
]


def make_record(identity, title, printed, pairs, layout, titles, printed_pages, visual=None):
    record = {'id': identity, 'title': title, 'kind': 'lesson', 'pdfPage': 35,
              'printedPage': printed, 'sourcePdf': SOURCE, 'paragraphs': [p[0] for p in pairs]}
    item = section(record, pairs, layout, titles)
    item['kind'] = 'lesson'
    item['sourceReferences'] = [{'pdfPage': 35, 'printedPage': page, 'sourcePdf': SOURCE} for page in printed_pages]
    if visual:
        item.update(visual)
        item['content'] += visual['diagramSvg']
    return record, item


if __name__ == '__main__':
    resistivity = make_record('phys12-unit12-resistivity60', 'Resistivity and specific resistance', 60,
        RESISTIVITY, [{'type': 'equation', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
                      {'type': 'paragraph', 'indices': [2]}, {'type': 'visual'}],
        ('مزاحمت النوعی اور مخصوص مزاحمت', 'مخصوص مقاومت او resistivity'), [60],
        {'diagramSvg': material_wire('en'), 'diagramSvgUrdu': material_wire('ur'), 'diagramSvgPashto': material_wire('ps')})
    table_rows = [[], [], ['Metals', 'Resistivity (μΩm)'], ['Copper (hard drawn)', '0.0178'], ['Aluminium', '0.0285'],
                  ['Tin', '0.114'], ['Silver', '0.0163'], ['Brass', '0.06-0.09'], ['Iron', '0.1'], ['Lead', '0.219'],
                  [], [], [], [], [], [], [], []]
    table_layout = [
        {'type': 'paragraph', 'indices': [0]}, {'type': 'heading', 'indices': [1]},
        {'type': 'table', 'indices': list(range(2, 10))}, {'type': 'heading', 'indices': [10]},
        {'type': 'paragraph', 'indices': [11]}, {'type': 'equation', 'indices': [12]},
        {'type': 'paragraph', 'indices': [13]}, {'type': 'heading', 'indices': [14]},
        {'type': 'paragraph', 'indices': [15]}, {'type': 'equation', 'indices': [16]},
        {'type': 'paragraph', 'indices': [17]},
    ]
    table_section = make_record('phys12-unit12-metal-resistivity-table-conductance60-61',
        'Table 12.1 — Resistivity, conductance and conductivity', 60, TABLE_AND_CONDUCTANCE, table_layout,
        ('جدول 12.1 — دھاتوں کی مزاحمت النوعی، موصلت اور چالکتا', '12.1 جدول — د فلزونو مخصوص مقاومت، هاديتوب او لېږدوړتیا'), [60, 61])
    table_section[1]['sourceTableRows'] = table_rows
    table_section[1]['sourceTables'] = [{'caption': TABLE_AND_CONDUCTANCE[1][0], 'headers': table_rows[2], 'rows': table_rows[3:10]}]
    header_html = '<thead><tr>'+''.join('<th scope="col">'+escape(cell)+'</th>' for cell in table_rows[2])+'</tr></thead>'
    body_html = '<tbody>'+''.join('<tr>'+''.join('<td>'+escape(cell)+'</td>' for cell in row)+'</tr>' for row in table_rows[3:10])+'</tbody>'
    tail_html = ''.join('<p>'+escape(TABLE_AND_CONDUCTANCE[i][0])+'</p>' for i in range(10, 18))
    table_section[1]['content'] = '<p>'+escape(TABLE_AND_CONDUCTANCE[0][0])+'</p><table><caption>'+escape(TABLE_AND_CONDUCTANCE[1][0])+'</caption>'+header_html+body_html+'</table>'+tail_html
    temperature_layout = [
        {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
        {'type': 'orderedList', 'indices': [2, 3]}, {'type': 'heading', 'indices': [4]},
        {'type': 'paragraph', 'indices': [5]}, {'type': 'orderedList', 'indices': [6, 7]},
        {'type': 'paragraph', 'indices': [8]}, {'type': 'equation', 'indices': [9]},
        {'type': 'equation', 'indices': [10]},
    ]
    temperature = make_record('phys12-unit12-temperature-resistance-coefficient61',
        '12.4 Effect of temperature on resistance', 61, TEMPERATURE, temperature_layout,
        ('12.4 درجۂ حرارت کا مزاحمت پر اثر', '12.4 د تودوخې اغېز پر مقاومت'), [61])
    records = [resistivity[0], table_section[0], temperature[0]]
    sections = [resistivity[1], table_section[1], temperature[1]]
    upsert(records, sections, chapter_index=1)
    example122 = {'id': 'textbook-example-12-2', 'num': '12.2', 'title': 'Example 12.2', 'problem': r'The high voltage in a TV receiver is 17 kV. The maximum allowable current is 150μA. What is the least permissible value of load resistance?',
        'given': [r'V=17\,\mathrm{kV},\ I=150\,\mu\mathrm A'], 'required': [r'Load resistance R=?'],
        'steps': [r'V=17\,\mathrm{kV}=17\times10^3\,\mathrm V', r'I=150\,\mu\mathrm A=150\times10^{-6}\,\mathrm A', r'R=\frac VI=\frac{17\times10^3}{150\times10^{-6}}=113.3\times10^6\,\Omega'],
        'answer': r'113.3\times10^6\,\Omega', 'solutionOrigin': 'textbook',
        'sourceReferences': [{'pdfPage': 34, 'printedPage': 58, 'sourcePdf': SOURCE}]}
    sync_companions(chapter_index=1, formulas=[
        {'id': 'phys12-unit12-eq-12.3', 'name': 'Resistance of a uniform conductor', 'number': '12.3',
         'formula': RESISTIVITY[0][0], 'latex': r'R=\rho\frac LA', 'sourceReferences': [{'pdfPage': 35, 'printedPage': 60, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-eq-12.4', 'name': 'Conductance', 'number': '12.4', 'formula': TABLE_AND_CONDUCTANCE[12][0],
         'latex': r'G=\frac1R', 'sourceReferences': [{'pdfPage': 35, 'printedPage': 60, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-eq-12.5', 'name': 'Conductivity', 'number': '12.5', 'formula': TABLE_AND_CONDUCTANCE[16][0],
         'latex': r'\sigma=\frac1\rho=\frac{L}{RA}', 'sourceReferences': [{'pdfPage': 35, 'printedPage': 61, 'sourcePdf': SOURCE}]},
        {'id': 'phys12-unit12-eq-12.6', 'name': 'Temperature dependence of resistance', 'number': '12.6',
         'formula': TEMPERATURE[10][0], 'latex': r'R_T-R_0=\alpha R_0T', 'sourceReferences': [{'pdfPage': 35, 'printedPage': 61, 'sourcePdf': SOURCE}]},
    ], definitions=[
        {'term': 'Resistivity', 'definition': RESISTIVITY[1][0]+' '+RESISTIVITY[2][0],
         'definitionUrdu': RESISTIVITY[1][1]+' '+RESISTIVITY[2][1], 'definitionPashto': RESISTIVITY[1][2]+' '+RESISTIVITY[2][2],
         'sourceReferences': [{'pdfPage': 35, 'printedPage': 60, 'sourcePdf': SOURCE}]},
        {'term': 'Conductance', 'definition': TABLE_AND_CONDUCTANCE[11][0]+' '+TABLE_AND_CONDUCTANCE[12][0],
         'definitionUrdu': TABLE_AND_CONDUCTANCE[11][1]+' '+TABLE_AND_CONDUCTANCE[12][1], 'definitionPashto': TABLE_AND_CONDUCTANCE[11][2]+' '+TABLE_AND_CONDUCTANCE[12][2],
         'sourceReferences': [{'pdfPage': 35, 'printedPage': 60, 'sourcePdf': SOURCE}]},
        {'term': 'Conductivity', 'definition': TABLE_AND_CONDUCTANCE[15][0]+' '+TABLE_AND_CONDUCTANCE[16][0],
         'definitionUrdu': TABLE_AND_CONDUCTANCE[15][1]+' '+TABLE_AND_CONDUCTANCE[16][1], 'definitionPashto': TABLE_AND_CONDUCTANCE[15][2]+' '+TABLE_AND_CONDUCTANCE[16][2],
         'sourceReferences': [{'pdfPage': 35, 'printedPage': 61, 'sourcePdf': SOURCE}]},
    ], worked_examples=[example122], trim_sections=[{
        'id': '12.3', 'startsAt': 'PHYSICS-XII\nUNIT 12 CURRENT ELECTRICITY\nNOT FOR SALE\n62\nWhere is the constant and is called temperature co-efficient of resistance.',
        'title': 'Temperature coefficient — continuation begins on PDF page 36'}])
    checkpoint(35, 'corrected_verified', [record['id'] for record in records],
        'Rendered PDF page 35 and inspected printed pages 60–61. Compared Eq. 12.3, resistivity definition and units, Figure 12.4, the full metal-resistivity table, conductance and conductivity definitions/equations, and the full printed temperature effect plus derivation through Eq. 12.6. Rebuilt the wire illustration as SVG and the source table as a translated semantic HTML table. Reused the Unit 12 vocabulary cache and kept the legacy continuation beginning on printed page 62 pending page 36.',
        printed_pages=[60, 61], chapter_number=12)
