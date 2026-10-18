import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions
from physics_agent2_translations import TRANSLATIONS, TITLES
from physics_agent2_page008 import prepare
from physics_agent2_layout import LAYOUT
prepare()

def diagram(identity, signs, distances):
    positions = [65, 65 + 450 * distances[0] / sum(distances), 515]
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 125" role="img" aria-label="Three collinear charges and their separations" style="width:100%;max-width:580px;height:auto"><defs><marker id="{identity}" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8Z" fill="#334155"/></marker></defs>'
    for index, (x, sign) in enumerate(zip(positions, signs)):
        svg += f'<circle cx="{x}" cy="70" r="18" fill="{"#f9a8d4" if sign == "+" else "#f8fafc"}" stroke="#334155"/><text x="{x-6}" y="76" font-size="20">{sign}</text><text x="{x-9}" y="35">q<tspan baseline-shift="sub" font-size="11">{index+1}</tspan></text>'
    for i, distance in enumerate(distances):
        x1, x2 = positions[i]+22, positions[i+1]-22
        svg += f'<line x1="{x1}" y1="70" x2="{x2}" y2="70" stroke="#334155" marker-start="url(#{identity})" marker-end="url(#{identity})"/><text x="{(x1+x2)/2-18}" y="55">{distance} cm</text>'
    return svg+'</svg>'

if __name__ == '__main__':
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    records = [r for r in old if r['pdfPage']==8]
    sections = []
    for record in records:
        identity = record['id']
        translations = list(TRANSLATIONS[identity])
        layout = LAYOUT[identity]
        if identity == 'phys12-front-table111':
            for row in record['rows']:
                row[1] = row[1].replace('–', '-')
            record['rows'][0][1] = 'εᵣ'
            record['rows'][-1][0] = 'Ammonia(liquid)'
            paragraphs = [' — '.join(row) for row in record['rows']]
            table_record = {**record, 'paragraphs': paragraphs}
            translations = [(ur.replace('–','-').replace('εr','εᵣ'), ps.replace('–','-').replace('εr','εᵣ')) for ur, ps in translations]
            revised = section(table_record, [(p,*pair) for p,pair in zip(paragraphs, translations)], layout, TITLES[identity])
            revised['sourceTableRows'] = record['rows']
            revised['content'] = '<table><thead><tr>'+''.join('<th scope="col">'+cell+'</th>' for cell in record['rows'][0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+cell+'</td>' for cell in row)+'</tr>' for row in record['rows'][1:])+'</tbody></table>'
            revised['kind'] = 'lesson'
            sections.append(revised)
            continue
        if identity == 'phys12-front-media6':
            record['paragraphs'][3] = record['paragraphs'][3].replace(r'\mathrm{vac}', r'\mathrm{vac}')
        if identity == 'phys12-front-example111':
            for i in (2,3,4):
                record['paragraphs'][i] = record['paragraphs'][i].replace(r'\(q_', r'\((q_').replace('=-', ')=-', 1).replace('=+', ')=+', 1)
                translations[i] = tuple(v.replace(r'\(q_', r'\((q_').replace('=-', ')=-', 1).replace('=+', ')=+', 1) for v in translations[i])
            for i in (6,7):
                subscript = '12' if i==6 else '23'
                record['paragraphs'][i] = record['paragraphs'][i].replace(': ', ' ').replace(r'\(r_{'+subscript+'}=', r'\((r_{'+subscript+'})=')
            record['paragraphs'][9] = record['paragraphs'][9].replace(r'\(q_2\): \(F_', r'\(q_2=F_')
            record['diagramHtml'] = diagram('phys12-reviewed-example111',['−','+','−'],[6,4])
        if identity == 'phys12-front-solution111':
            record['paragraphs'][0] = record['paragraphs'][0].replace(': ', '= ')
            record['paragraphs'][1] = record['paragraphs'][1].replace(r'\(F_{21}=', r'\(=')
            record['paragraphs'][2] = record['paragraphs'][2].replace(r'=125\,\mathrm N', '')
            record['paragraphs'][3] = record['paragraphs'][3].replace(':', '=')
            record['paragraphs'][7] = r'The net electrostatic force on charge \(q_2=F_2=F_{21}-F_{23}\)'
            record['paragraphs'][8] = r'\(=675\,\mathrm N-125\,\mathrm N=550\,\mathrm N\).'
            record['paragraphs'].append(r'\(=125\,\mathrm N\)')
            translations[0] = tuple(v.replace(': ', '= ') for v in translations[0])
            translations[1] = (record['paragraphs'][1], record['paragraphs'][1])
            translations[2] = (record['paragraphs'][2], record['paragraphs'][2])
            translations[7] = (r'بار \(q_2\) پر خالص برقی سکونی قوت \(q_2=F_2=F_{21}-F_{23}\)', r'پر چارج \(q_2\) خالصه ساکنه برېښنايي قوه \(q_2=F_2=F_{21}-F_{23}\)')
            translations[8] = (record['paragraphs'][8], record['paragraphs'][8])
            translations.append((record['paragraphs'][11],record['paragraphs'][11]))
            layout = layout[:3]+[{'type':'equation','indices':[11]}]+layout[3:]
            example = record['workedExamples'][0]
            example_record = next(r for r in records if r['id']=='phys12-front-example111')
            example['given'] = example_record['paragraphs'][2:8]
            example['required'] = example_record['paragraphs'][9:11]
            example['steps'] = [record['paragraphs'][i] for i in [0,1,2,11,3,4,5,6,7,8,9]]
            example['diagramSvg'] = diagram('phys12-reviewed-example111-card',['−','+','−'],[6,4])
            record['sourceDefects'] = ['First F23 substitution lacks distance square; printed F21−F23 labels oppose the numerical subtraction. Printed statements retained, clarification explicitly editorial.']
        if identity == 'phys12-front-assignment111':
            record['paragraphs'][0] = r'Three charges \(+q_1=5\,\mu\mathrm C\), \(+q_2=10\,\mu\mathrm C\) and \(q_3\) are placed as shown in th figure. What is the electrostatic charge on \(q_3\) if the net electrostati force on charges \(q_2\) is zero.'
            record['paragraphs'][1] = r'\((20\times10^{-6}\,\mathrm C)\)'
            translations[1] = (record['paragraphs'][1],record['paragraphs'][1])
            record['paragraphs'].append('[Editorial note: th and electrostati are clipped at the right edge of the source scan; missing letters remain unresolved.]')
            translations.append(('[ادارتی نوٹ: اصل اسکین کے دائیں کنارے پر th اور electrostati کے آخری حروف کٹے ہوئے ہیں؛ گم شدہ حروف ابھی واضح نہیں۔]', '[د سمونوال یادونه: د اصلي سکین په ښي څنډه کې د th او electrostati وروستي توري پرې شوي؛ ورک توري لا نه دي معلوم.]'))
            layout = layout+[{'type':'paragraph','indices':[2]}]
            record['diagramHtml'] = diagram('phys12-reviewed-assignment111',['+','+','+'],[2,4])
            question = record['exercises'][0]['problems'][0]
            question['question'] = record['paragraphs'][0]
            question['solution'] = ''
            question['answerOrigin'] = 'textbook'
            question['sourceClarifications'] = [record['paragraphs'][2]]
            question['diagramSvg'] = diagram('phys12-reviewed-assignment111-card',['+','+','+'],[2,4])
            record['sourceDefects'] = [record['paragraphs'][2]]
        revised = section(record, [(p,*pair) for p,pair in zip(record['paragraphs'],translations)], layout, TITLES[identity])
        revised['kind'] = 'lesson'
        if record.get('diagramHtml'):
            revised['diagramSvg'] = record['diagramHtml']
            revised['diagramSvgUrdu'] = record['diagramHtml']
            revised['diagramSvgPashto'] = record['diagramHtml']
            revised['content'] += record['diagramHtml']
        if identity == 'phys12-front-solution111':
            revised['paras'][10]['isEditorial'] = True
            revised['paras'][10]['originalText'] = None
        if identity == 'phys12-front-assignment111':
            revised['paras'][2]['isEditorial'] = True
            revised['paras'][2]['originalText'] = None
        sections.append(revised)
    upsert(records, sections)
    worked = next(r for r in records if r['id']=='phys12-front-solution111')['workedExamples']
    exercises = next(r for r in records if r['id']=='phys12-front-assignment111')['exercises']
    sync_companions(formulas=[{'id':'phys12-eq-'+f['number'],'number':f['number'],'name':'Equation '+f['number'],
                              'formula':r'\('+f['latex']+r'\)','latex':f['latex'],'note':'Textbook source equation',
                              'sourceReferences':[{'pdfPage':8,'printedPage':6}]} for f in records[0]['formulas']],
                    worked_examples=worked, exercises=exercises)
    checkpoint(8, 'corrected_unresolved', [r['id'] for r in records],
               'Full spread inspected at 3x; equations and assignment at 5x/4x. Table rows, values, printed Germinium/Paraffine spellings, ranges and epsilon subscript compared. Corrected source punctuation and parentheses; kept all solution substitution steps, isolated 125 N line, restored printed net-force equality and retained textbook inconsistencies with editorial clarification. Native diagrams rebuilt with 6:4 and 2:4 distance proportions. Same corrections upserted into worked-example and exercise cards; source answer kept, no invented solution. Assignment right-edge clipped fragments retained and disclosed.',
               issues=['Assignment 11.1, printed page 7: right edge clips th and electrostati. Exact missing letters unresolved; source fragments retained.'], printed_pages=[6,7])
