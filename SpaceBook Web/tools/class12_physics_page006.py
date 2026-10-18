import json
from class12_source_review import ROOT, upsert, section, checkpoint
from physics_agent2_translations import TRANSLATIONS, TITLES

PORTRAIT = '''<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 250" role="img" aria-label="Coulomb in a pale wig, dark coat and gold epaulette" style="max-width:210px;width:100%;height:auto"><rect width="210" height="250" fill="#474337"/><path d="M18 249Q20 190 79 169L141 165Q188 178 202 250" fill="#292b28"/><path d="M62 161L90 189 105 238 139 185 143 158" fill="#e8e3ce"/><path d="M72 34Q103 7 145 42L167 93Q177 128 150 157L128 176Q85 170 68 144L51 95Z" fill="#d5b397"/><path d="M69 102Q45 135 34 104Q17 88 34 66Q22 39 55 35Q66 5 100 16Q132 3 154 34L161 77Q139 65 137 39Q104 55 74 39Q55 67 69 102Z" fill="#e5dfc4"/><path d="M58 87Q29 99 41 131Q57 143 67 128L78 138 70 112Z" fill="#ded5b9"/><path d="M76 93Q94 82 106 92M125 89Q140 80 151 91" fill="none" stroke="#786457" stroke-width="3"/><ellipse cx="98" cy="98" rx="4" ry="3" fill="#302e29"/><ellipse cx="142" cy="96" rx="4" ry="3" fill="#302e29"/><path d="M128 102L137 120 120 125M106 144Q125 150 142 139" fill="none" stroke="#99735d" stroke-width="2"/><path d="M26 192L60 177 80 198 38 211Z" fill="#ad8946"/><path d="M33 209L37 230M43 206L47 227M54 203L57 225M64 201L68 221" stroke="#c9a354" stroke-width="7"/><path d="M86 184L128 181 116 196 138 209 123 220 137 231 109 239Z" fill="#f1ebdb"/></svg></figure>'''

if __name__ == '__main__':
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    outcomes = next(item for item in old if item['id'] == 'phys12-front-outcomes2')
    intro = next(item for item in old if item['id'] == 'phys12-front-coulomb-introduction')
    out_section = section(outcomes, [(p, *pair) for p, pair in zip(outcomes['paragraphs'], TRANSLATIONS[outcomes['id']])],
                          [{'type': 'list', 'indices': list(range(21))}, {'type': 'paragraph', 'indices': [21]}], TITLES[outcomes['id']])
    out_section['kind'] = 'learning_outcomes'
    # Separate source paragraphs; the prior layout merged the capacitance paragraph.
    intro['paragraphs'][6] = "Charles-Augustin de Coulom was an eminent Frenc physicist who formulated th law known Coulomb's law"
    intro['paragraphs'].append('(1736-1805).')
    intro['paragraphs'].append('[Editorial note: the source scan clips the endings of Coulom, Frenc and th; the missing letters have not been silently supplied.]')
    intro.pop('figures', None)
    diagram = intro['diagramHtml']
    diagram = diagram.replace('F₂₁', 'F⃗₂₁').replace('F₁₂', 'F⃗₁₂')
    diagram = diagram.replace('<line x1="100" y1="70"', '<text x="12" y="74">(a)</text><line x1="100" y1="70"', 1)
    diagram = diagram.replace('<line x1="100" y1="180"', '<text x="12" y="184">(b)</text><line x1="100" y1="180"', 1)
    diagram = diagram.replace('Figure 11.1 (a), (b): Coulomb force between similar charges.', 'FIGURE 11.1 — Coulomb force between similar charges')
    diagram = diagram.replace('Figure 11.2: Coulomb force between opposite charges.', 'FIGURE 11.2 — Coulomb force between opposite charges.')
    diagram += PORTRAIT
    intro['diagramHtml'] = diagram
    intro['sourceDefects'] = ['Biography right-edge clipping: Coulom / Frenc / th. Printed fragments retained; original JPG and split copy contain the same clipping.']
    pairs = [(p, *pair) for p, pair in zip(intro['paragraphs'][:6], TRANSLATIONS[intro['id']][:6])]
    pairs += [
        (intro['paragraphs'][6], 'شارل آگستان دے کولوم ایک ممتاز فرانسیسی طبیعیات دان تھے جنہوں نے کولوم کا قانون وضع کیا۔', 'شارل اګوستن دي کولم یو نامتو فرانسوي فزیکپوه و چې د کولم په نوم پېژندل شوی قانون یې جوړ کړ.'),
        ('(1736-1805).', '(1736-1805)۔', '(1736-1805).'),
        (intro['paragraphs'][8], '[ادارتی نوٹ: اصل اسکین میں Coulom، Frenc اور th کے آخری حروف کٹے ہوئے ہیں؛ گم شدہ حروف خاموشی سے شامل نہیں کیے گئے۔]', '[د سمونوال یادونه: په اصلي سکین کې د Coulom، Frenc او th وروستي توري پرې شوي؛ ورک توري په پټه نه دي ورزیات شوي.]'),
    ]
    layout = [{'type': 'paragraph', 'indices': [i]} for i in range(3)]
    layout += [{'type': 'heading', 'indices': [3]}, {'type': 'paragraph', 'indices': [4]},
               {'type': 'paragraph', 'indices': [5]}, {'type': 'visual'},
               {'type': 'paragraph', 'indices': [7]}, {'type': 'paragraph', 'indices': [6]},
               {'type': 'paragraph', 'indices': [8]}]
    revised = section(intro, pairs, layout, TITLES[intro['id']])
    revised['kind'] = 'lesson'
    revised['paras'][8]['isEditorial'] = True
    revised['paras'][8]['originalText'] = None
    revised['diagramSvg'] = diagram
    revised['diagramSvgUrdu'] = diagram.replace('FIGURE 11.1 — Coulomb force between similar charges', 'شکل 11.1 — ہم نوع باروں کے درمیان کولوم کی قوت').replace('FIGURE 11.2 — Coulomb force between opposite charges.', 'شکل 11.2 — مخالف باروں کے درمیان کولوم کی قوت۔')
    revised['diagramSvgPashto'] = diagram.replace('FIGURE 11.1 — Coulomb force between similar charges', 'شکل 11.1 — د یو ډول چارجونو ترمنځ د کولم قوه').replace('FIGURE 11.2 — Coulomb force between opposite charges.', 'شکل 11.2 — د مخالفو چارجونو ترمنځ د کولم قوه.')
    revised['content'] += diagram
    upsert([outcomes, intro], [out_section, revised])
    checkpoint(6, 'corrected_unresolved', [outcomes['id'], intro['id']],
               'Full spread inspected at 3x, biography crop at 6x and original JPG/split checked. Twenty-one outcomes, introduction, three opening paragraphs, law statement and q=ne compared. Corrected merged paragraph boundary, vector-force and panel labels. Removed Coulomb raster portrait, replaced with native SVG illustration. Figure captions paired in Urdu and Pashto visual fields. Clipped biography endings preserved as printed and separately disclosed.',
               issues=['Printed page 3 Coulomb biography clips Coulom / Frenc / th. Local complete PDF, JPG and split source show same loss; exact missing source letters unresolved.'], printed_pages=[2,3])
