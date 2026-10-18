import json
from class12_source_review import DATA,OUT,upsert
from class12_physics_page020 import figure
text=DATA.read_text(encoding='utf-8');prefix='PHYS_12_DATA[0].sections.unshift(...'
sections,_=json.JSONDecoder().raw_decode(text[text.index(prefix)+len(prefix):])
target=next(s for s in sections if s['id']=='phys12-front-point30')
target['content']=target['content'].replace(target['diagramSvg'],figure('en'))
target.update(diagramSvg=figure('en'),diagramSvgUrdu=figure('ur'),diagramSvgPashto=figure('ps'))
record=next(r for r in json.loads((OUT/'physics-corrections.json').read_text(encoding='utf-8')) if r['id']==target['id'])
upsert([record],[target])
