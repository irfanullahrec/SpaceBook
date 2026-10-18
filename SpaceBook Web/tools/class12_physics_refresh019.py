import json
from class12_source_review import DATA,OUT,upsert
from class12_physics_page019 import equipotential
text=DATA.read_text(encoding='utf-8')
start=text.index('PHYS_12_DATA[0].sections.unshift(...')+len('PHYS_12_DATA[0].sections.unshift(...')
sections,_=json.JSONDecoder().raw_decode(text[start:])
target=next(s for s in sections if s['id']=='phys12-front-equipotential28')
target['content']=target['content'].replace(target['diagramSvg'],equipotential('en'))
target.update(diagramSvg=equipotential('en'),diagramSvgUrdu=equipotential('ur'),diagramSvgPashto=equipotential('ps'))
record=next(r for r in json.loads((OUT/'physics-corrections.json').read_text(encoding='utf-8')) if r['id']==target['id'])
upsert([record],[target])
