import json
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent
SOURCE = r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf'

def pair(t, u, p):
    return dict(text=t, urdu=u, pashto=p)

def svg(body, w=750, h=110, label='Textbook equation'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, quote=True)}"><g font-family="sans-serif" font-size="25" fill="currentColor">{body}</g></svg>'

def text(t, x, y, anchor=None, size=None):
    attrs = (f' text-anchor="{anchor}"' if anchor else '') + (f' font-size="{size}"' if size else '')
    return f'<text x="{x}" y="{y}"{attrs}>{t}</text>'

def sub(t, s):
    return f'{t}<tspan baseline-shift="sub" font-size="17">{s}</tspan>'

def sup(t, s):
    return f'{t}<tspan baseline-shift="super" font-size="17">{s}</tspan>'

def frac(n, d, x, w, y=54):
    return text(n, x+w/2, y-20, 'middle') + text(d, x+w/2, y+38, 'middle') + f'<path d="M{x} {y}h{w}" stroke="currentColor" stroke-width="2"/>'

def number(n, x=640, y=38):
    return f'<path d="M{x-65} {y+20}h65" stroke="currentColor" stroke-width="2"/><rect x="{x}" y="{y}" width="63" height="40" rx="4" fill="#3e899d"/>'+text(n, x+31.5,y+28,'middle')

def block(i, body, w=750, h=110, ratio=.9, label='Textbook equation', ur=None, ps=None, kind='formula'):
    s=svg(body,w,h,label)
    return dict(type=kind,id=i,svg=s,svgUrdu=svg(ur if ur is not None else body,w,h,label),svgPashto=svg(ps if ps is not None else body,w,h,label),sourceWidthRatio=ratio)

def section(code, heading, ur, ps, paras, blocks, layout):
    return dict(code=code,heading=heading,headingUrdu=ur,headingPashto=ps,paras=paras,blocks=blocks,sourceLayout=layout)

def para(i, kind='paragraph'):
    return dict(type=kind,indices=[i])

def visual(b):
    return dict(type='visual',blockId=b['id'])

def save(n, title, sections, comparison, **extra):
    page=dict(id=f'cls9-physics-page-{n:03}',pdfPage=n,printedPage=n-5,status='corrected-fresh-review',chapterNumber=2,chapter='Unit 2: Kinematics',title=title,sourcePdf=SOURCE,sections=sections,comparison=comparison,**extra)
    (OUT/f'physics-page-{n:03}.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return page
