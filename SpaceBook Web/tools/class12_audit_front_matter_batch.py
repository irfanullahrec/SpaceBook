"""Record the fresh visual pass over PDF1–5 without trusting old completion claims."""
import json
from class12_source_review import OUT
from class12_fidelity_repair import stage_reference
corrections=json.loads((OUT/'physics-corrections.json').read_text(encoding='utf-8'))
by_id={item['id']:item for item in corrections}
def ref(identity):return by_id[identity]
p1={'id':'phys12-front-cover','paragraphs':['For Grade XII','Free From Government','NOT FOR SALE','Khyber Pakhtunkhwa Textbook Board Peshawar']}
stage_reference(1,p1,'Rendered original PDF1 at150dpi and visually inspected the full cover. Exact title “A Textbook of Physics”, Grade XII, free-from-government and NOT FOR SALE wording, publisher and emblem match the coded front-cover record. Cover collage is decorative; no lesson raster reused.')
progress=json.loads((OUT/'progress.json').read_text(encoding='utf-8'))
entry=next(page for page in progress['pages'] if page['pdfPage']==2)
entry.update(status='excluded',recordIds=[],evidence='Rendered and visually inspected the complete original PDF2. It is solely a third-party website and app advertisement, including download links and subject list; excluded from textbook lessons.')
repair=progress['fidelityRepair']
if 2 not in repair['completedPages']:repair['completedPages'].append(2)
(OUT/'progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
stage_reference(3,ref('phys12-front-quotation'),'Rendered and inspected the complete original PDF3 spread. Exact Urdu quotation and attribution, English anti-corruption slogan, Grade-XII title and publisher are present in the active paired records in the same reading order. Decorative floral borders/emblem excluded.')
stage_reference(4,ref('phys12-front-publication'),'Rendered and inspected the complete original PDF4 spread. Publisher rights/NOC/curriculum, all legible credits and preface text/paragraph boundaries compared with active paired records. Two very faint reviewer names remain explicitly unreadable and are recorded as unresolved; no names guessed.',[
 'Two reviewer names on printed page2 remain too faint to read in both locally available scans. Explicit unreadable markers retained instead of guessed names.'
],[ref('phys12-front-preface')])
contents={'id':'phys12-front-contents','paragraphs':['Units — Pages','11 Electrostatics — 1','12 Current electricity — 52','13 Electromagnetism — 88','14 Electromagnetic induction — 126','15 Alternating current — 156','16 Physics of solids — 202','17 Electronics — 230','18 Dawn of the modern physics — 254','19 Atomic Spectra — 297','20 Nuclear physics — 333','Glossary — 383']}
stage_reference(5,contents,'Rendered and inspected the complete original PDF5 spread. All12 table-of-contents entries and printed starting pages match the semantic table. The facing printed page1 heading, question and all nine Coulomb/electrostatics outcomes match active source-aligned paragraphs; the existing copier image is decorative context, not instructional apparatus.',[],[ref('phys12-front-outcomes1')])
print('Fresh source review staged for PDF1–5; PDF2 excluded; PDF4 name locations retained unresolved.')
