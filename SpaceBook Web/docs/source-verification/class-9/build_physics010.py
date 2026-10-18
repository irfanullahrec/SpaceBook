import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[9]
page.update(id='cls9-physics-page-010',status='corrected-fresh-review',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
s=page['sections'][0]
s['paras'][6]['text']=s['paras'][6]['text'].replace('Dr. Ishfaq','Dr.Ishfaq')+'"'
def portrait(identity,name,style):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 270" role="img" aria-labelledby="{identity}-title"><title id="{identity}-title">{name} — coded reconstruction of the source portrait</title><rect width="220" height="270" fill="#e2e8f0"/>'
    if style=='haitham':
        svg+='<path d="M39 260L59 205L106 180L157 204L181 263Z" fill="#26364b"/><ellipse cx="109" cy="134" rx="46" ry="67" fill="#c8b9a7"/><path d="M65 139L71 177L90 220L133 213L156 172L150 135L126 157L99 157Z" fill="#26354a"/><path d="M78 123Q89 111 100 123M117 120Q132 111 142 120M99 143L102 153L114 152" fill="none" stroke="#29354a" stroke-width="3"/><path d="M63 115Q42 61 84 47Q146 25 166 79L158 112L137 100L113 70L92 105Z" fill="#d9d3cd" stroke="#38485a" stroke-width="3"/><path d="M52 76L144 39M54 91L155 55M60 105L163 73M72 49L158 91M86 43L157 104" stroke="#64748b" stroke-width="4"/>'
    elif style=='beruni':
        svg+='<path d="M29 267L57 210L139 191L195 220L214 270Z" fill="#2a3241"/><path d="M62 108L78 76L138 73L153 111L173 130L157 139L163 153L145 166L133 202L97 193L77 156Z" fill="#bdab9c" stroke="#3b3940" stroke-width="2"/><path d="M88 150L111 146L128 157L157 143L147 184L131 216L96 202Z" fill="#3c3a43"/><path d="M115 116L139 114M121 124L136 123M141 145L155 145" stroke="#242c3c" stroke-width="3"/><path d="M62 138Q40 100 60 65L109 37L150 59L167 95L140 89L110 69L79 116L71 162L55 231L38 234Z" fill="#e2d9d7" stroke="#554d58" stroke-width="3"/><path d="M52 96L126 46M56 108L139 58M71 121L150 77M60 157L46 228" stroke="#998995" stroke-width="4"/>'
    else:
        svg+='<path d="M21 270L34 218L80 190L140 190L190 215L211 270Z" fill="#465371"/><path d="M80 194L110 218L140 190L157 270H64Z" fill="#f8fafc"/><path d="M105 213L117 212L124 230L113 267L99 232Z" fill="#26344f"/><path d="M74 127L71 158L88 188L113 203L139 184L152 155L147 119Z" fill="#cf9b97" stroke="#814f5e" stroke-width="2"/>'
        if style=='ishfaq':
            svg+='<path d="M70 134L66 104Q69 68 94 59Q133 51 148 83L157 127L145 121L140 86L91 86L80 125Z" fill="#f0e9e7"/><path d="M76 136H103V154H81ZM115 136H143V154H118Z" fill="#b0a9b2" fill-opacity=".4" stroke="#1f2937" stroke-width="3"/><path d="M103 141H115M111 150L106 163L117 164M97 178H123" stroke="#624751" stroke-width="2" fill="none"/>'
        else:
            svg+='<path d="M70 135L60 107Q57 67 96 57Q132 39 156 75L158 115L147 135L143 95L122 81L90 91L80 126Z" fill="#242736"/><path d="M82 135L99 131M119 131L140 134M110 142L104 158L118 160M91 174Q113 162 134 174L127 183L99 184Z" fill="#252637" stroke="#513843" stroke-width="2"/>'
    return svg+'</svg>'
labels=[('IBNAL HAITHAM','ابن الہیثم','ابن الهيثم','haitham'),('AL BERUNI','البیرونی','البیروني','beruni'),('Ishfaq Ahmad','اشفاق احمد','اشفاق احمد','ishfaq'),('Abdul Qadeer Khan','عبدالقدیر خان','عبدالقدیر خان','qadeer')]
s['blocks']=[]
for i,(name,urdu,pashto,style) in enumerate(labels):
    s['paras'].append(dict(text=name,urdu=urdu,pashto=pashto))
    s['blocks'].append(dict(type='illustration',id=f'physics9-portrait-{style}-005',svg=portrait(f'physics9-portrait-{style}-005',name,style),sourcePdfPage=10,printedPage=5))
s['sourceLayout']=[dict(type='heading',indices=[0]),dict(type='paragraph',indices=[1]),dict(type='visual',blockId='physics9-portrait-haitham-005'),dict(type='heading',indices=[9]),dict(type='heading',indices=[2]),dict(type='paragraph',indices=[3]),dict(type='visual',blockId='physics9-portrait-beruni-005'),dict(type='heading',indices=[10]),dict(type='heading',indices=[4]),dict(type='heading',indices=[5]),dict(type='paragraph',indices=[6]),dict(type='visual',blockId='physics9-portrait-ishfaq-005'),dict(type='heading',indices=[11]),dict(type='heading',indices=[7]),dict(type='paragraph',indices=[8]),dict(type='visual',blockId='physics9-portrait-qadeer-005'),dict(type='heading',indices=[12])]
page['comparison']='Fresh visual review of four biographies, headings, dates, book/institution/award names, and portrait labels. Preserved source afghan, Busra, geography; and orphan closing quote after kind. Reconstructed four distinct native portraits: turban/beard/front pose, side-facing headwrap/beard, white hair/glasses/suit, and dark hair/moustache/suit. Captions have paired translations and illustrations occur once in reading order.'
(OUT/'physics-page-010.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
