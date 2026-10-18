import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions
from physics_agent2_translations import TRANSLATIONS, TITLES
from physics_agent2_page009 import prepare
from physics_agent2_layout import LAYOUT
prepare()

if __name__ == '__main__':
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    records = [r for r in old if r['pdfPage']==9]
    sections = []
    for record in records:
        identity = record['id']
        pairs = list(TRANSLATIONS[identity])
        layout = LAYOUT[identity]
        if identity == 'phys12-front-field8':
            record['paragraphs'][7] = r'If five charges are placed such that, as shown in figure, then the resultant force exerted by charges \(q_2\), \(q_3\), \(q_4\), and \(q_5\) on charges \(q_1\) is'
            record['paragraphs'][8] = r'\(F_1=F_{12}+F_{13}+F_{14}+F_{15}\)'
            pairs[8] = (record['paragraphs'][8], record['paragraphs'][8])
            record['paragraphs'].append('TIP')
            pairs.append(('اشارہ', 'اشاره'))
            layout = layout[:3]+[{'type':'heading','indices':[9]}, {'type':'visual'},
                                {'type':'paragraph','indices':[7]}, {'type':'equation','indices':[8]}]+layout[3:6]
        if identity == 'phys12-front-field9':
            record['paragraphs'][3] = record['paragraphs'][3].replace(', so', ' so')
        if identity == 'phys12-front-example112-start':
            pairs[2] = (pairs[2][0].replace('فاصلہ', 'نصف قطر'), pairs[2][1].replace('واټن', 'شعاع'))
        revised = section(record, [(p,*pair) for p,pair in zip(record['paragraphs'],pairs)], layout, TITLES[identity])
        revised['kind'] = 'lesson'
        if record.get('diagramHtml'):
            svg = record['diagramHtml']
            revised['diagramSvg'] = svg
            revised['diagramSvgUrdu'] = svg.replace('Figure 11.3: Electric field intensity due to a point charge.', 'شکل 11.3: نقطہ بار کی وجہ سے برقی میدان کی شدت۔')
            revised['diagramSvgPashto'] = svg.replace('Figure 11.3: Electric field intensity due to a point charge.', 'شکل 11.3: د نقطوي چارج له امله د برېښنايي میدان شدت.')
            revised['content'] += svg
        sections.append(revised)
    upsert(records, sections)
    entries = [
      ('phys12-eq-field-definition', r'\vec E=\frac{\vec F}{q_0}',8,'Electric field intensity'),
      ('phys12-eq-11.9',r'\vec F=q_0\vec E',8,'Force on a test charge'),
      ('phys12-eq-11.10',r'\vec E=k\frac{q}{r^2}\hat r',9,'Point-charge field'),
      ('phys12-tip-superposition',r'F_1=F_{12}+F_{13}+F_{14}+F_{15}',8,'Force superposition'),
    ]
    sync_companions(formulas=[{'id':ident,'name':name,'formula':r'\('+latex+r'\)','latex':latex,
                              'note':'Textbook source equation','sourceReferences':[{'pdfPage':9,'printedPage':page}]} for ident,latex,page,name in entries])
    checkpoint(9, 'corrected_verified', [r['id'] for r in records],
               'Complete spread rendered at 3x and compared with paragraphs, definition, SI units, vector force/intensity derivation, Eq 11.9/11.10 and beginning of Example 11.2. Existing five-charge SVG checked for signs, all four force directions and labels; radial field SVG checked for outward spokes, positive source/test charge and force arrow. TIP heading and source plural charges restored, source scalar F1 summation retained without invented vector marks. Diagram captions translated and available in all panels. Radius translated as radius rather than distance. Equation cards synchronized; example continuation remains on PDF page 10.', printed_pages=[8,9])
