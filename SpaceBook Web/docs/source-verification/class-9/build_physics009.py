import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[8]
page.update(id='cls9-physics-page-009',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
for start in [0,3,6,9,12,15]:
    english=s['paras'][start+2]['text']
    for offset,language in enumerate(['ar','ur','en']):
        s['paras'][start+offset].update(sourceLanguage=language,english=english)
for para in s['paras'][18:]:
    para.update(sourceLanguage='en',english=para['text'])
s['paras'].append(dict(text='YAQUB KINDI',urdu='یعقوب کندی',pashto='یعقوب کندي',sourceLanguage='en',english='YAQUB KINDI'))
portrait='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 285" role="img" aria-labelledby="physics9-kindi-title"><title id="physics9-kindi-title">Yaqub Kindi, shown wearing a turban and robe in a profile portrait</title><rect width="220" height="285" fill="#edf1f4"/><path d="M36 282L62 229L99 201L150 179L207 238L217 285Z" fill="#526477" stroke="#243849" stroke-width="2"/><path d="M82 201L59 161L69 118L104 80L156 84L178 137L147 180L136 214Z" fill="#d0d6dc" stroke="#334155" stroke-width="2"/><path d="M73 126L59 148L70 153L61 162L73 168L91 167L94 180L120 187L139 166L144 130L117 129L108 160L99 154L89 143Z" fill="#293d4f"/><path d="M71 123L94 122L103 127" fill="none" stroke="#1e293b" stroke-width="4"/><path d="M75 133L94 133" stroke="#334155" stroke-width="3"/><path d="M68 112Q46 89 75 68L159 60Q186 65 187 93L172 125L144 100L89 100Z" fill="#cbd5e1" stroke="#4f6272" stroke-width="3"/><path d="M61 83Q111 58 176 85M63 95Q111 72 174 98M74 67L163 95M72 77L165 107M92 56L166 76" fill="none" stroke="#6b7d90" stroke-width="4"/><path d="M89 60L98 22L106 11L113 20L105 60" fill="#74889b"/><path d="M61 239L153 187L174 198L77 266M84 275L171 210M126 279L192 227" fill="none" stroke="#d4dce4" stroke-width="9"/><path d="M148 222L174 275M160 216L192 273M172 212L207 266" fill="none" stroke="#34495c" stroke-width="3"/></svg>'
s['blocks'].append(dict(type='illustration',id='physics9-kindi-004',svg=portrait,sourcePdfPage=9,printedPage=4))
s['sourceLayout']=[dict(type='quotation',indices=[0,1,2]),dict(type='quotation',indices=[3,4,5]),dict(type='quotation',indices=[6,7,8]),dict(type='parallelPhrases',columns=[[9,10,11],[12,13,14],[15,16,17]]),dict(type='heading',indices=[18]),dict(type='paragraph',indices=[19]),dict(type='heading',indices=[20]),dict(type='paragraph',indices=[21]),dict(type='visual',blockId='physics9-kindi-004'),dict(type='heading',indices=[22])]
page['comparison']='Fresh 2x visual review of all three Arabic verses, source Urdu/English translations, surah references, three short phrases in columns, contribution heading, biography and portrait caption. Explicit source-language records preserve Arabic/Urdu as originals rather than English. Quotation boxes and three-column phrase structure restored; native portrait preserves visible turban/profile/robe. Printed Busra and dates retained.'
(OUT/'physics-page-009.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
