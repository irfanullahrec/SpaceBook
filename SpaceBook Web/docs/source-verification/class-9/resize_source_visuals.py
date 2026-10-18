import json,os
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
ratios={'cls9-physics-dashboard-001':.34,'physics9-telescope-002':.35,'physics9-galaxy-002':.35,'physics9-pet-003':.35,'physics9-hologram-003':.35,'physics9-kindi-004':.27,'physics9-car-007':.95,'physics9-cockpit-008':.35,'physics9-viruses-009':.36,'physics9-earthmoon-010':.35,'physics9-housefly-012':.35,'physics9-mosquito':.39,'physics9-tuberculosis':.37,'physics9-calliper-source':.89,'physics9-calliper-figure11':.9}
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
 app=ROOT/'js/app.js';text=app.read_text(encoding='utf-8')
 old="      return lang === 'en' ? (visual?.svg || '') : (lang === 'ur' ? visual?.svgUrdu || '' : visual?.svgPashto || '');"
 new="""      const markup = lang === 'en' ? (visual?.svg || '') : (lang === 'ur' ? visual?.svgUrdu || '' : visual?.svgPashto || '');
      if (!visual?.sourceWidthRatio) return markup;
      const width = Math.max(1, Math.min(100, visual.sourceWidthRatio * 100));
      return `<div class="class9-source-object" style="width:${width}%;max-width:100%;margin:.5rem auto;">${markup.replace(/<svg\\b/, '<svg style="display:block;width:100%;height:auto;max-width:100%;"')}</div>`;"""
 if old not in text:raise ValueError('Renderer changed; inspect before editing')
 app.write_text(text.replace(old,new,1),encoding='utf-8')
 data=ROOT/'js/data_phys.js';text=data.read_text(encoding='utf-8');marker=text.index('// Agent 1 sequential Class 9 Physics source review\n');start=text.index('const pages = ',marker)+len('const pages = ');pages,length=json.JSONDecoder().raw_decode(text[start:])
 for page in pages:
  file=OUT/f"physics-page-{page['pdfPage']:03}.json"
  if not file.exists():continue
  reviewed=json.loads(file.read_text(encoding='utf-8'))
  for s in reviewed.get('sections',[]):
   for b in s.get('blocks',[]):
    if b.get('svg'):
     b['sourceWidthRatio']=ratios.get(b.get('id'),.25 if 'portrait' in b.get('id','') else .8)
     b['sourceSizing']='Width relative to the printed textbook content column; retain SVG aspect ratio.'
  file.write_text(json.dumps(reviewed,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  page.clear();page.update(reviewed)
 data.write_text(text[:start]+json.dumps(pages,ensure_ascii=False,indent=2)+text[start+length:],encoding='utf-8')
finally:
 os.close(fd);lock.unlink()
print('Reviewed Class 9 Physics visuals constrained to source-column proportions.')
