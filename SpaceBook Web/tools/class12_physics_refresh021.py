import json
from class12_source_review import DATA,OUT,upsert,sync_companions
from class12_physics_page021 import EXAMPLE
text=DATA.read_text(encoding='utf-8');prefix='PHYS_12_DATA[0].sections.unshift(...'
sections,_=json.JSONDecoder().raw_decode(text[text.index(prefix)+len(prefix):])
target=next(s for s in sections if s['id']=='phys12-front-example116')
target['paras'][11]['originalText']=EXAMPLE[11][0]
record=next(r for r in json.loads((OUT/'physics-corrections.json').read_text(encoding='utf-8')) if r['id']==target['id'])
record['paragraphs'][11]=EXAMPLE[11][0]
upsert([record],[target])
companion=json.loads((OUT/'physics-companions.json').read_text(encoding='utf-8'))
example=next(e for e in companion['workedExamples'] if e['id']=='textbook-example-6')
example['answer']=EXAMPLE[11][0];example['steps'][-1]=EXAMPLE[11][0]
sync_companions(worked_examples=[example])
