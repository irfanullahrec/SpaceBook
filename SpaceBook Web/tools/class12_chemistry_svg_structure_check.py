"""Parse saved Chemistry source SVGs; this is structural validation, not fidelity proof."""
from class12_chemistry_opening import OUT
from datetime import datetime,timezone
import json,xml.etree.ElementTree as ET
count=0;pages=[]
for page in range(32,52):
 audit=json.loads((OUT/f'chemistry-pdf{page}-repair.json').read_text(encoding='utf-8'))
 for section in audit['sections']:
  for block in section['sourceBlocks']:
   for field in ['svg','svgUrdu','svgPashto']:
    if field not in block:continue
    root=ET.fromstring(block[field]);assert root.tag.endswith('svg')
    assert not any(node.tag.endswith('image') for node in root.iter()),'Raster image forbidden'
    count+=1
 pages.append(page)
report={'checkedUtc':datetime.now(timezone.utc).isoformat(),'pdfPages':pages,'parsedLanguageSvgs':count,'passed':['SVG XML valid','No embedded raster-image elements'],'scope':'Structural checks only. Does not verify source drawing fidelity or right-to-left typography.'}
(OUT/'chemistry-svg-structure-pages32-51.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(report)
