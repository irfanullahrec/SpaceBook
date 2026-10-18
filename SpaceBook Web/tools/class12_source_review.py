"""Precise Class 12 Physics upserts and immediate fresh-audit checkpoints."""
from pathlib import Path
import html
import json
import os
import time
from contextlib import contextmanager

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/source-verification/class-12'
DATA = ROOT / 'js/phys_12_data.js'

def write_data(text):
    """Replace the shared data file atomically so a transient write cannot truncate it."""
    temporary = DATA.with_name(DATA.name + '.tmp')
    temporary.write_text(text, encoding='utf-8')
    last_error = None
    for _ in range(10):
        try:
            os.replace(temporary, DATA)
            return
        except OSError as exc:
            last_error = exc
            try:
                DATA.write_text(text, encoding='utf-8')
                temporary.unlink(missing_ok=True)
                return
            except OSError as direct_exc:
                last_error = direct_exc
                time.sleep(0.25)
    raise last_error

@contextmanager
def shared_class_data_lock():
    """Hold the common short lock while rereading and patching shared physics data."""
    lock = ROOT / 'tmp/class-content-shared.lock'
    lock.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.write(descriptor, f'class12-physics pid={os.getpid()}\n'.encode('ascii'))
        os.close(descriptor)
        descriptor = None
        yield
    finally:
        if descriptor is not None:
            os.close(descriptor)
        lock.unlink(missing_ok=True)

def replace_json(text, prefix, update):
    start = text.index(prefix) + len(prefix)
    value, length = json.JSONDecoder().raw_decode(text[start:])
    update(value)
    return text[:start] + json.dumps(value, ensure_ascii=False, indent=2) + text[start+length:]

def upsert(records, sections, chapter_index=0):
    if chapter_index:
        unit_number=11+chapter_index
        records_path=OUT/f'physics-corrections-unit{unit_number}.json'
        sections_path=OUT/f'physics-sections-unit{unit_number}.json'
        saved_records=json.loads(records_path.read_text(encoding='utf-8')) if records_path.exists() else []
        saved_sections=json.loads(sections_path.read_text(encoding='utf-8')) if sections_path.exists() else []
        for collection,entries in ((saved_records,records),(saved_sections,sections)):
            for entry in entries:
                index=next((i for i,item in enumerate(collection) if item['id']==entry['id']),None)
                if index is None: collection.append(entry)
                else: collection[index]=entry
        marker=f'// BEGIN CLASS12 UNIT{unit_number} SOURCE REVIEW UPSERTS'
        end_marker=f'// END CLASS12 UNIT{unit_number} SOURCE REVIEW UPSERTS'
        index=f'PHYS_12_DATA[{chapter_index}]'
        block=(f'{marker}\n{index}.reviewedSourcePages = '+json.dumps(saved_records,ensure_ascii=False,indent=2)+';\n'
               +f'{index}.sections.unshift(...'+json.dumps(saved_sections,ensure_ascii=False,indent=2)+');\n'
               +f'{index}.topics = {index}.sections.map(section => ({{...{index}.topics.find(topic => topic.id === section.id), ...section}}));\n{end_marker}\n')
        text=DATA.read_text(encoding='utf-8')
        if marker in text:
            start=text.index(marker);end=text.index(end_marker,start)+len(end_marker)
            text=text[:start]+block.rstrip()+text[end:]
        else:
            anchor='PHYS_12_DATA[0].reviewedSourcePages = '
            position=text.find(anchor)
            if position<0: raise ValueError('Cannot locate Unit 11 source review insertion point')
            text=text[:position]+block+'\n'+text[position:]
        write_data(text)
        records_path.write_text(json.dumps(saved_records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        sections_path.write_text(json.dumps(saved_sections,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return
    text = DATA.read_text(encoding='utf-8')
    def update_records(items):
        for entry in records:
            index = next((i for i, item in enumerate(items) if item['id'] == entry['id']), None)
            if index is None:
                items.append(entry)
            else:
                items[index] = entry
    def update_sections(items):
        for entry in sections:
            index = next((i for i, item in enumerate(items) if item['id'] == entry['id']), None)
            if index is None:
                items.append(entry)
            else:
                items[index] = entry
    text = replace_json(text, f'PHYS_12_DATA[{chapter_index}].reviewedSourcePages = ', update_records)
    text = replace_json(text, f'PHYS_12_DATA[{chapter_index}].sections.unshift(...', update_sections)
    write_data(text)
    cache = OUT / 'physics-corrections.json'
    saved = json.loads(cache.read_text(encoding='utf-8')) if cache.exists() else []
    update_records(saved)
    cache.write_text(json.dumps(saved, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def checkpoint(page, status, record_ids, evidence, issues=None, printed_pages=None, chapter_number=11):
    path = OUT / 'progress.json'
    progress = json.loads(path.read_text(encoding='utf-8'))
    assert page == progress['nextPage'], (page, progress['nextPage'])
    entry = {'pdfPage': page, 'printedPages': printed_pages or [], 'status': status,
             'recordIds': record_ids, 'evidence': evidence, 'chapterNumber':chapter_number}
    progress['pages'].append(entry)
    progress['nextPage'] = page + 1
    progress['lastInspectedPage'] = page
    if status in ('verified_unchanged', 'corrected_verified'):
        progress['lastFullyVerifiedPage'] = page
    for issue in issues or []:
        progress['unresolvedItems'].append({'pdfPage': page, 'issue': issue})
    path.write_text(json.dumps(progress, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    refresh_progress()

def refresh_progress():
    path=OUT/'progress.json'
    progress=json.loads(path.read_text(encoding='utf-8'))
    verified=progress.get('lastFullyVerifiedPage',0)
    chapter=progress['pages'][-1].get('chapterNumber',11) if progress.get('pages') else 11
    if chapter >= 12:
        unit_name={12:'Current Electricity',13:'Electromagnetism'}.get(chapter,'Physics')
        section_name=('Steady current' if chapter==12 and verified <= 31 else unit_name)
        progress['currentChapter']=f'Unit {chapter}: {unit_name} — {section_name}'
    elif verified >= 30:
        progress['currentChapter']='Unit 11: Electrostatics — Exercise numerical questions'
    elif verified >= 29:
        progress['currentChapter']='Unit 11: Electrostatics — Exercise conceptual and comprehensive questions'
    elif verified >= 27:
        progress['currentChapter']='Unit 11: Electrostatics — RC discharge, applications and key points'
    elif verified >= 25:
        progress['currentChapter']='Unit 11: Electrostatics — capacitor energy and RC charging'
    elif verified >= 22:
        progress['currentChapter']='Unit 11: Electrostatics — capacitors, dielectrics and polarization'
    elif verified >= 18:
        progress['currentChapter']='Unit 11: Electrostatics — electric potential and work'
    elif verified >= 14:
        progress['currentChapter']='Unit 11: Electrostatics — Gauss’s law and applications'
    else:
        progress['currentChapter']='Unit 11: Electrostatics — Coulomb’s law and electric field'
    progress['nextAction']=f"Render Physics complete PDF page {progress['nextPage']} locally and inspect in sequence; compare active trimmed continuation and all relevant views. Source defects on PDF pages 4, 6 and 8 remain open. Finish Physics through PDF201, resolve split/edition relationships, then remaining non-Mathematics subjects in assignment order."
    path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    inventory_path=OUT/'inventory.json'
    inventory=json.loads(inventory_path.read_text(encoding='utf-8'))
    subject=next(s for s in inventory['subjects'] if s['subject']=='Physics')
    primary=next(p for p in subject['pdfs'] if p['sourcePath']==progress['sourcePdf'])
    primary.update(reviewStatus='in_progress_incomplete',nextPage=progress['nextPage'],lastInspectedPage=progress['lastInspectedPage'],lastFullyVerifiedPage=progress['lastFullyVerifiedPage'],verifiedUnchangedPages=[p['pdfPage'] for p in progress['pages'] if p['status']=='verified_unchanged'],correctedPages=[p['pdfPage'] for p in progress['pages'] if p['status'].startswith('corrected')],excludedPages=[p['pdfPage'] for p in progress['pages'] if p['status']=='excluded'],unresolvedPages=[p['pdfPage'] for p in progress['pages'] if p['status']=='corrected_unresolved'])
    inventory_path.write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def sync_companions(formulas=None, definitions=None, worked_examples=None, exercises=None, retire_sections=None, trim_sections=None, retire_exercises=None, retire_worked_examples=None, retire_formulas=None, replace_definitions=False, update_section_metadata=None, chapter_index=0):
    """Update audited summary cards by stable ID or precise legacy formula."""
    unit_number=11+chapter_index
    path = OUT / ('physics-companions.json' if chapter_index==0 else f'physics-companions-unit{unit_number}.json')
    data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'formulas': [], 'definitions': []}
    data.setdefault('workedExamples', [])
    data.setdefault('exercises', [])
    data.setdefault('retireSections', [])
    data.setdefault('trimSections', [])
    data.setdefault('updateSectionMetadata', [])
    data.setdefault('retireExercises', [])
    data.setdefault('retireWorkedExamples', [])
    data.setdefault('retireFormulas', [])
    if replace_definitions:
        data['replaceDefinitions'] = True
        data['definitions'] = []
    for identity in retire_sections or []:
        if identity not in data['retireSections']:
            data['retireSections'].append(identity)
    for identity in retire_exercises or []:
        if identity not in data['retireExercises']:
            data['retireExercises'].append(identity)
    for identity in retire_worked_examples or []:
        if identity not in data['retireWorkedExamples']:
            data['retireWorkedExamples'].append(identity)
    for identity in retire_formulas or []:
        if identity not in data['retireFormulas']:
            data['retireFormulas'].append(identity)
    for change in trim_sections or []:
        existing = next((i for i,item in enumerate(data['trimSections']) if item['id']==change['id']),None)
        if existing is None:
            data['trimSections'].append(change)
        else:
            data['trimSections'][existing]=change
    for change in update_section_metadata or []:
        existing=next((i for i,item in enumerate(data['updateSectionMetadata']) if item['id']==change['id']),None)
        if existing is None:data['updateSectionMetadata'].append(change)
        else:data['updateSectionMetadata'][existing]=change
    for kind, entries in [('formulas', formulas), ('definitions', definitions), ('workedExamples', worked_examples), ('exercises', exercises)]:
        for entry in entries or []:
            key = 'term' if kind == 'definitions' else 'id'
            index = next((i for i, item in enumerate(data[kind]) if item[key] == entry[key]), None)
            if index is None:
                data[kind].append(entry)
            else:
                data[kind][index] = entry
    marker = '// BEGIN CLASS12 FRESH AUDIT COMPANION UPSERTS' if chapter_index==0 else f'// BEGIN CLASS12 UNIT{unit_number} FRESH AUDIT COMPANION UPSERTS'
    end_marker=f'// END CLASS12 UNIT{unit_number} FRESH AUDIT COMPANION UPSERTS'
    suffix=''
    source=DATA.read_text(encoding='utf-8')
    if chapter_index==0:
        text=source.split(marker)[0].rstrip()+'\n\n'+marker+'\n'
    elif marker in source:
        start=source.index(marker);end=source.index(end_marker,start)+len(end_marker)
        text=source[:start].rstrip()+'\n\n'+marker+'\n';suffix=source[end:]
    else:
        anchor='// BEGIN CLASS12 FRESH AUDIT COMPANION UPSERTS'
        position=source.index(anchor)
        text=source[:position].rstrip()+'\n\n'+marker+'\n';suffix=source[position:]
    text += '{ const audit = '+json.dumps(data, ensure_ascii=False, indent=2)+';\n'
    block = '''if (audit.replaceDefinitions) PHYS_12_DATA[0].definitions = [...(audit.definitions || [])];
    for (const entry of audit.formulas) {
      const items = PHYS_12_DATA[0].formulas;
      const index = items.findIndex(item => item.id === entry.id || (entry.legacyFormula && item.formula === entry.legacyFormula));
      const {legacyFormula, ...correction} = entry;
      if (index >= 0) items[index] = {...items[index], ...correction}; else items.push(correction);
    }
    PHYS_12_DATA[0].formulas = PHYS_12_DATA[0].formulas.filter(entry =>
      !(audit.retireFormulas || []).includes(entry.id) && !(audit.retireFormulas || []).includes(entry.name));
    for (const entry of audit.definitions) {
      const items = PHYS_12_DATA[0].definitions;
      const index = items.findIndex(item => item.term === entry.term);
      if (index >= 0) items[index] = {...items[index], ...entry}; else items.push(entry);
    }
    for (const kind of ['workedExamples', 'exercises']) for (const entry of audit[kind] || []) {
      const items = PHYS_12_DATA[0][kind];
      const index = items.findIndex(item => item.id === entry.id);
      if (index >= 0) items[index] = {...items[index], ...entry}; else items.push(entry);
    }
    PHYS_12_DATA[0].exercises = PHYS_12_DATA[0].exercises.filter(entry =>
      !(audit.retireExercises || []).includes(entry.id) && !(audit.retireExercises || []).includes(entry.exercise) && !(audit.retireExercises || []).includes(entry.title));
    PHYS_12_DATA[0].workedExamples = PHYS_12_DATA[0].workedExamples.filter(entry => !(audit.retireWorkedExamples || []).includes(entry.id));
    PHYS_12_DATA[0].sections = PHYS_12_DATA[0].sections.filter(section => !(audit.retireSections || []).includes(section.id));
    for (const change of audit.updateSectionMetadata || []) {
      const section=PHYS_12_DATA[0].sections.find(section=>section.id===change.id);
      if(section)Object.assign(section,change.values);
    }
    for (const change of audit.trimSections || []) {
      const section = PHYS_12_DATA[0].sections.find(section => section.id === change.id);
      if (!section) continue;
      if (change.startsAt) {
        const start = section.theory.indexOf(change.startsAt);
        if (start < 0) throw new Error('Missing Physics12 continuation: '+change.id);
        section.theory = section.theory.slice(start);
      }
      if (change.endsBefore) {
        const end = section.theory.indexOf(change.endsBefore);
        if (end < 0) throw new Error('Missing Physics12 end boundary: '+change.id);
        section.theory = section.theory.slice(0,end).trimEnd();
      }
      section.content = section.theory.replace(/\\n/g, '<br>');
      if (change.title) section.title = change.title;
      if (change.clearSciNote) section.sciNote = '';
    }
    PHYS_12_DATA[0].topics = PHYS_12_DATA[0].sections.map(section => ({...PHYS_12_DATA[0].topics.find(topic => topic.id === section.id), ...section}));
}\n'''
    block=block.replace('PHYS_12_DATA[0]',f'PHYS_12_DATA[{chapter_index}]')
    text += block
    if chapter_index:
        text+=end_marker+'\n'+suffix
    write_data(text)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def section(record, pairs, layout, titles, source_language='en'):
    paragraphs = [{'text': text, 'english': text, 'urdu': urdu, 'pashto': pashto,
                   'originalText': original, 'originalLanguage': source_language}
                  for original, (text, urdu, pashto) in zip(record['paragraphs'], pairs)]
    assert len(paragraphs) == len(record['paragraphs'])
    return {'id': record['id'], 'title': record['title'], 'kind': 'book_front_matter',
            'content': ''.join('<p>'+html.escape(p['text'])+'</p>' for p in paragraphs),
            'theory': '\n'.join(p['text'] for p in paragraphs), 'paras': paragraphs,
            'urdu': '\n\n'.join(p['urdu'] for p in paragraphs),
            'pashto': '\n\n'.join(p['pashto'] for p in paragraphs),
            'sourceLanguage': source_language, 'headingUrdu': titles[0], 'headingPashto': titles[1],
            'diagramSvg': '', 'translationStatus': 'authored_aligned_paragraphs',
            'sourceLayout': layout, 'sourceReferences': [{'pdfPage': record['pdfPage'],
            'printedPage': record['printedPage'], 'sourcePdf': record['sourcePdf']}]}
