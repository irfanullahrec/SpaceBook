"""Persist independently inspected Physics pages in the existing subject data."""
from pathlib import Path
import json
import html

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'js/phys_12_data.js'
PROGRESS = ROOT / 'docs/source-verification/physics-agent2-sequential.json'
RECORDS = ROOT / 'docs/source-verification/physics-agent2-pages.json'
MARKER = '// BEGIN PHYSICS AGENT 2 SEQUENTIAL SOURCE PASS'

def save_page(number, records, note=None, repair=False):
    progress = json.loads(PROGRESS.read_text(encoding='utf-8'))
    if not repair:
        assert number == len(progress['completedPages']) + 1
    pages = json.loads(RECORDS.read_text(encoding='utf-8')) if RECORDS.exists() else []
    for record in records:
        record['pdfPage'] = number
        record['sourcePdf'] = progress['sourcePdf']
        pages.append(record)
    text = DATA.read_text(encoding='utf-8').split(MARKER)[0].rstrip()
    addition = '\n\n'+MARKER+'\nPHYS_12_DATA[0].reviewedSourcePages = '+json.dumps(pages,ensure_ascii=False,indent=2)+';\n'
    addition += "PHYS_12_DATA[0].bookFrontMatter = PHYS_12_DATA[0].reviewedSourcePages.filter(page => page.kind !== 'learning_outcomes' && page.kind !== 'lesson');\n"
    addition += "PHYS_12_DATA[0].sections = PHYS_12_DATA[0].sections.filter(section => !section.id.startsWith('phys12-front-'));\n"
    sections=[]
    from physics_agent2_translations import TRANSLATIONS, TITLES
    from physics_agent2_layout import LAYOUT
    if any(record.get('pdfPage',0) >= 8 for record in pages):
        from physics_agent2_page008 import prepare
        prepare()
    if any(record.get('pdfPage',0) >= 9 for record in pages):
        from physics_agent2_page009 import prepare
        prepare()
    if any(record.get('pdfPage',0) >= 10 for record in pages):
        from physics_agent2_page010 import prepare
        prepare()
        addition += "{ const continuation = PHYS_12_DATA[0].sections.find(section => section.id === '11.4'); if (continuation) { const start = continuation.theory.indexOf('Selenium is'); if (start >= 0) { continuation.theory = continuation.theory.slice(start); continuation.content = continuation.theory.replace(/\\n/g, '<br>'); continuation.title = 'Photocopiers (continued; awaiting source review)'; } } }\n"
    if any(record.get('pdfPage',0) >= 11 for record in pages):
        from physics_agent2_page011 import prepare
        prepare()
        addition += "PHYS_12_DATA[0].sections = PHYS_12_DATA[0].sections.filter(section => section.id !== '11.4');\n"
        addition += "{ const continuation = PHYS_12_DATA[0].sections.find(section => section.id === '11.5'); if (continuation) { const start = continuation.theory.indexOf('EXAMPLE 11.3'); if (start >= 0) { continuation.theory = continuation.theory.slice(start); continuation.content = continuation.theory.replace(/\\n/g, '<br>'); continuation.title = 'Example 11.3 and electric flux (awaiting source review)'; } } }\n"
    if any(record.get('printedPage') == 9 for record in pages):
        addition += "PHYS_12_DATA[0].sections = PHYS_12_DATA[0].sections.filter(section => section.id !== '11.3');\n"
        addition += "{ const continuation = PHYS_12_DATA[0].sections.find(section => section.id === '11.4'); if (continuation) { const start = continuation.theory.indexOf('REQUIRED'); if (start >= 0) { continuation.theory = continuation.theory.slice(start); continuation.content = continuation.theory.replace(/\\n/g, '<br>'); continuation.title = 'Example 11.2 (continued; awaiting source review)'; } } }\n"
    for record in pages:
        body = ''.join('<p>'+html.escape(p)+'</p>' for p in record.get('paragraphs',[]))
        for figure in record.get('figures', []):
            body += '<figure><img src="'+html.escape(figure['src'],quote=True)+'" alt="'+html.escape(figure['alt'],quote=True)+'" style="max-width:100%;height:auto"><figcaption>'+html.escape(figure['caption'])+'</figcaption></figure>'
        if record.get('rows'):
            body += '<table><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(cell))+'</td>' for cell in row)+'</tr>' for row in record['rows'])+'</tbody></table>'
        body += record.get('diagramHtml','')
        translated = TRANSLATIONS.get(record['id'], [])
        paragraphs = record.get('paragraphs', [])
        if record.get('rows'):
            paragraphs = [' — '.join(str(cell) for cell in row) for row in record['rows']]
        assert len(translated) == len(paragraphs), f"Missing aligned translations: {record['id']}"
        paras = [{'text':text,'urdu':pair[0],'pashto':pair[1]} for text,pair in zip(paragraphs,translated)]
        ur_title, ps_title = TITLES[record['id']]
        visual_html = body[body.find('<figure>'):] if '<figure>' in body else ''
        if record.get('rows'):
            visual_html = body[body.find('<table>'):]
        if record.get('diagramHtml') and not visual_html:
            visual_html = record['diagramHtml']
        sections.append({'id':record['id'],'title':record['title'],'content':body,
                         'theory':'\n'.join(record.get('paragraphs',[])),
                         'paras':paras,'urdu':'\n\n'.join(pair[0] for pair in translated),
                         'pashto':'\n\n'.join(pair[1] for pair in translated),
                         'headingUrdu':ur_title,'headingPashto':ps_title,
                         'diagramSvg':visual_html,'translationStatus':'authored_aligned_paragraphs',
                         'sourceLayout':LAYOUT[record['id']],
                         'sourceTableRows':record.get('rows',[]),
                         'sourceReferences':[{'pdfPage':record['pdfPage'],'printedPage':record['printedPage'],'sourcePdf':record['sourcePdf']}],
                         'kind':record.get('kind','book_front_matter')})
    addition+='PHYS_12_DATA[0].sections.unshift(...'+json.dumps(sections,ensure_ascii=False,indent=2)+');\n'
    if any(record.get('printedPage') == 1 for record in pages):
        addition += "{ const intro = PHYS_12_DATA[0].sections.find(section => section.id === '11.1'); if (intro) { const start = intro.theory.indexOf('In this unit two fundamental'); if (start >= 0) { intro.theory = intro.theory.slice(start); intro.content = intro.theory.replace(/\\n/g, '<br>'); } } }\n"
    if any(record.get('printedPage') == 3 for record in pages):
        addition += "{ const intro = PHYS_12_DATA[0].sections.find(section => section.id === '11.1'); if (intro) { const start = intro.theory.indexOf('The magnitude of the force F'); if (start >= 0) { intro.theory = intro.theory.slice(start); intro.content = intro.theory.replace(/\\n/g, '<br>'); intro.title = '11.1 Coulomb’s law (continued)'; } } }\n"
    if any(record.get('printedPage') == 5 for record in pages):
        addition += "PHYS_12_DATA[0].sections = PHYS_12_DATA[0].sections.filter(section => section.id !== '11.1');\n"
        addition += "{ const continuation = PHYS_12_DATA[0].sections.find(section => section.id === '11.2'); if (continuation) { const start = continuation.theory.indexOf('Obviously'); if (start >= 0) { continuation.theory = continuation.theory.slice(start); continuation.content = continuation.theory.replace(/\\n/g, '<br>'); continuation.title = 'Coulomb’s law in material media (continued)'; } } }\n"
    if any(record.get('printedPage') == 7 for record in pages):
        addition += "PHYS_12_DATA[0].sections = PHYS_12_DATA[0].sections.filter(section => section.id !== '11.2');\n"
        addition += "{ const continuation = PHYS_12_DATA[0].sections.find(section => section.id === '11.3'); if (continuation) { const start = continuation.theory.indexOf('11.2 ELECTRIC FIELD AND ITS INTENSITY'); if (start >= 0) { continuation.theory = continuation.theory.slice(start); continuation.content = continuation.theory.replace(/\\n/g, '<br>'); continuation.title = '11.2 Electric field and its intensity (continuation awaiting source review)'; } } }\n"
    for record in pages:
        for example in record.get('workedExamples', []):
            addition += "{ const items = PHYS_12_DATA[0].workedExamples; const entry = "+json.dumps(example,ensure_ascii=False)+"; const index = items.findIndex(item => item.id === entry.id); if (index >= 0) items[index] = entry; else items.push(entry); }\n"
        for exercise in record.get('exercises', []):
            addition += "{ const items = PHYS_12_DATA[0].exercises; const entry = "+json.dumps(exercise,ensure_ascii=False)+"; const index = items.findIndex(item => item.id === entry.id); if (index >= 0) items[index] = entry; else items.push(entry); }\n"
        for definition in record.get('definitions', []):
            entry={'term':definition['term'],'def':definition['text'],'sourceReferences':[{'pdfPage':record['pdfPage'],'printedPage':record['printedPage']}]}
            addition += "{ const items = PHYS_12_DATA[0].definitions; const entry = "+json.dumps(entry,ensure_ascii=False)+"; const index = items.findIndex(item => item.term === entry.term); if (index >= 0) items[index] = entry; else items.push(entry); }\n"
    addition += "PHYS_12_DATA[0].topics = PHYS_12_DATA[0].sections.map(section => ({...PHYS_12_DATA[0].topics.find(topic => topic.id === section.id), ...section}));\n"
    DATA.write_text(text+addition,encoding='utf-8')
    RECORDS.write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if repair:
        progress['correctionPass'] = {'status':'saved','scope':f"PDF pages 1–{progress['lastFullyImplementedPdfPage']}",'fixes':['Explicit plain paragraph input for interactive reading','Aligned authored Urdu and Pashto translations','Topic/section data synchronized','Visual figures separated from translatable prose']}
        PROGRESS.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return
    progress['completedPages'].append({'pdfPage':number,'printedPages':[r['printedPage'] for r in records],'recordIds':[r['id'] for r in records],'note':note})
    progress.update(status='in_progress',currentPdfPage=number,lastFullyImplementedPdfPage=number,
                    nextPage=number+1,printedTextbookPageReference=[r['printedPage'] for r in records],
                    requiredVerification='Visual source PDF inspection and direct comparison with coded project data; browser checks waived by user',verificationBlocker=None)
    for record in records:
        for issue in record.get('sourceDefects', []):
            progress['unresolvedExtractionIssues'].append({'pdfPage':number,'recordId':record['id'],'issue':issue})
    PROGRESS.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__ == '__main__':
    save_page(1,[{'id':'phys12-front-cover','printedPage':None,'title':'A Textbook of Physics',
                 'paragraphs':['For Grade XII','Free From Government','NOT FOR SALE','Khyber Pakhtunkhwa Textbook Board Peshawar'],
                 'kind':'cover','visuals':'Decorative cover collage: magnet, magnetic field, compass and accelerator; no instructional exercise.'}])
    save_page(2,[], 'Distributor advertisement; no textbook educational content. Inspected and excluded from lessons.')
