import json
import math
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[6]
page.update(id='cls9-physics-page-007',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s.update(heading='1.1 INTRODUCTION TO PHYSICS',headingUrdu='1.1 طبیعیات کا تعارف',headingPashto='1.1 د فزیک پېژندنه')
s['paras'][7]['text']=s['paras'][7]['text'].replace('Physicists investigate','Physics investigate')
page['sourceClarifications']=[{'printedText':'Physics investigate the motions of electrons and rockets','note':'Source prints Physics as the subject of investigate. Retained as printed; intended meaning appears to refer to physicists. This note is editorial.'}]
telescope='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 280" role="img" aria-labelledby="physics9-telescope-title"><title id="physics9-telescope-title">Gemini North observatory with a smaller dome behind it</title><rect width="420" height="280" fill="#34384c"/><path d="M0 225L100 211L185 221L290 209L420 230V280H0Z" fill="#8b6752"/><path d="M185 208V124Q185 36 282 35Q375 36 375 124V208Z" fill="#cc896a" stroke="#563a39" stroke-width="3"/><path d="M185 124H375M196 97H364M211 70H349M233 47H328M204 124V169M226 124V169M248 124V169M270 124V169M292 124V169M314 124V169M336 124V169M357 124V169" fill="none" stroke="#623f3c" stroke-width="4"/><path d="M225 173H330V209H225Z" fill="#704e40"/><path d="M246 177H272V208H246Z" fill="#272b32"/><path d="M294 176H318V195H294Z" fill="#333745"/><path d="M69 218V175Q69 133 103 133Q139 133 139 175V219Z" fill="#937568" stroke="#4b3d40" stroke-width="3"/><path d="M98 135V177H112V137" fill="#3b3440"/><path d="M156 122L181 118V220H156Z" fill="#73604f"/></svg>'
galaxy=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 240" role="img" aria-labelledby="physics9-galaxy-title"><title id="physics9-galaxy-title">Milky Way spiral galaxy viewed at an angle</title><rect width="420" height="240" fill="#10152b"/><ellipse cx="210" cy="125" rx="152" ry="48" fill="#3e4485" opacity=".65"/>']
for arm in range(4):
    points=[]
    for i in range(100):
        radius=12+i*1.3
        angle=i*.042+arm*math.pi/2
        points.append(f'{210+math.cos(angle)*radius:.1f},{125+math.sin(angle)*radius*.28:.1f}')
    galaxy.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="#9c93cc" stroke-width="8" opacity=".5"/>')
for i in range(115):
    angle=i*2.399963
    radius=20+(i%31)*4
    x=210+math.cos(angle)*radius
    y=125+math.sin(angle)*radius*.29
    galaxy.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{1+(i%3)*.4}" fill="#f2d4cd" opacity=".8"/>')
galaxy.append('<ellipse cx="210" cy="125" rx="46" ry="15" fill="#f5d4ae"/><ellipse cx="210" cy="125" rx="22" ry="8" fill="#fff1ce"/></svg>')
caption=s['paras'][4]
caption['text']=caption['text'].removeprefix('TELESCOPE: ')
caption['urdu']=caption['urdu'].removeprefix('دوربین: ')
caption['pashto']=caption['pashto'].removeprefix('دوربین: ')
caption=s['paras'][9]
caption['text']=caption['text'].removeprefix('MILKY WAY GALAXY: ')
caption['urdu']=caption['urdu'].removeprefix('کہکشاں ملکی وے: ')
caption['pashto']=caption['pashto'].removeprefix('د شیدو لار کهکشان: ')
s['paras'] += [dict(text='TELESCOPE',urdu='دوربین',pashto='دوربین'),dict(text='MILKY WAY GALAXY',urdu='کہکشاں ملکی وے',pashto='د شیدو لار کهکشان')]
s['blocks']=[dict(type='illustration',id='physics9-telescope-002',svg=telescope,captionIndex=4,sourcePdfPage=7,printedPage=2),dict(type='illustration',id='physics9-galaxy-002',svg=''.join(galaxy),captionIndex=9,sourcePdfPage=7,printedPage=2)]
s['sourceLayout']=[dict(type='paragraph',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='heading',indices=[2]),dict(type='paragraph',indices=[3]),dict(type='visual',blockId='physics9-telescope-002'),dict(type='heading',indices=[11]),dict(type='paragraph',indices=[4]),dict(type='paragraph',indices=[5]),dict(type='paragraph',indices=[6]),dict(type='paragraph',indices=[7]),dict(type='paragraph',indices=[8]),dict(type='visual',blockId='physics9-galaxy-002'),dict(type='heading',indices=[12]),dict(type='paragraph',indices=[9]),dict(type='paragraph',indices=[10])]
page['comparison']='Fresh visual review of every source paragraph, definition, captions and heading. Retained source cloths and Physics investigate wording; separated caption labels from prose; added native SVG of the two observatory domes and tilted spiral galaxy, retaining relationships without source raster. Explicit layout keeps source paragraph and caption boundaries with paired translations.'
(OUT/'physics-page-007.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
