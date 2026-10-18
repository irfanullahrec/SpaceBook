import json
from class12_source_review import DATA,OUT,upsert
from class12_physics_page015 import patches
text=DATA.read_text(encoding='utf-8')
start=text.index('PHYS_12_DATA[0].sections.unshift(...')+len('PHYS_12_DATA[0].sections.unshift(...')
sections,_=json.JSONDecoder().raw_decode(text[start:])
target=next(s for s in sections if s['id']=='phys12-front-gauss20')
block=next(b for b in target['sourceBlocks'] if b['id']=='patches')
old=block['svg']
block.update(svg=patches('en'),svgUrdu=patches('ur'),svgPashto=patches('ps'))
target['content']=target['content'].replace(old,block['svg'])
record=next(r for r in json.loads((OUT/'physics-corrections.json').read_text(encoding='utf-8')) if r['id']==target['id'])
upsert([record],[target])
