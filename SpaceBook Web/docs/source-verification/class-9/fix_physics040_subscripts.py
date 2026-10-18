import json
from pathlib import Path
OUT=Path(__file__).resolve().parent;file=OUT/'physics-page-040.json';page=json.loads(file.read_text(encoding='utf-8'))
for s in page['sections']:
 for b in s['blocks']:
  for field in ['svg','svgUrdu','svgPashto']:
   if field not in b:continue
   for a,v in [('s𝒇','s<tspan baseline-shift="sub" font-size="17">f</tspan>'),('sᵢ','s<tspan baseline-shift="sub" font-size="17">i</tspan>'),('t𝒇','t<tspan baseline-shift="sub" font-size="17">f</tspan>'),('tᵢ','t<tspan baseline-shift="sub" font-size="17">i</tspan>')]:b[field]=b[field].replace(a,v)
file.write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
