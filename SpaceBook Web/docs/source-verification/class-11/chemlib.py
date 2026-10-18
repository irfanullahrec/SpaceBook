import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SO='[scan obscured]'
def page(n,chapter,title,ur,ps,sid):
    return dict(chapter=chapter,id=f'chem11-p{n}-{sid}',title=title,headingUrdu=ur,headingPashto=ps,sourceLanguage='en',source=dict(pdfPage=n,printedPage=n-5),auditStatus='corrected; verification pending',paras=[],flow=[],vocabulary={})
def add(s,key,en,ur,ps,**meta):
    s['paras'].append(dict(id=f"chem11-p{s['source']['pdfPage']}-{key}",en=en,ur=ur,ps=ps,**meta))
def head(s,key,en,ur,ps): add(s,key,en,ur,ps,kind='heading')
def cell(en,ur=None,ps=None): return dict(en=en,ur=ur or en,ps=ps or en)
def table(caption,cu,cp,headers,rows): return dict(caption=caption,captionUrdu=cu,captionPashto=cp,headers=headers,rows=rows)
def eq(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
def ids(s,a=0,b=None): return [p['id'] for p in s['paras'][a:b]]
def save(s):
    (ROOT/f"chemistry-page-{s['source']['pdfPage']}.json").write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
def lab(en,ur=None,ps=None): return dict(en=en,ur=ur or en,ps=ps or en)
def fig(n,key,svg,cap,cu,cp,labels): return dict(id=f'chem11-p{n}-{key}',svg=svg,caption=cap,captionUrdu=cu,captionPashto=cp,labels=labels)
def svg(w,h,aria,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{aria}" style="width:100%;max-width:{w}px;height:auto;background:#fff">{body}</svg>'
def T(x,y,t,size=14,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'
def mcq(s,n,q,qu,qp,opts,pg,**m):
    eid=f'chem11-p{pg}-mcq-{n}'
    add(s,f'mcq-{n}',f'{n}. {q}',f'{n}۔ {qu}',f'{n}. {qp}',role='question',exerciseId=eid,**m)
    for i,(e,u,p) in enumerate(opts):
        L='abcd'[i]
        add(s,f'mcq-{n}{L}',f'{L}. {e}',f'{L}۔ {u or e}',f'{L}. {p or e}',role='option',exerciseId=eid)
def cube(x,y,w=110,extra=''):
    d=w*0.35
    return (f'<g fill="none" stroke="#222" stroke-width="2"><rect x="{x}" y="{y+d}" width="{w}" height="{w}"/><rect x="{x+d}" y="{y}" width="{w}" height="{w}"/>'
            f'<path d="M{x} {y+d} L{x+d} {y} M{x+w} {y+d} L{x+w+d} {y} M{x} {y+d+w} L{x+d} {y+w} M{x+w} {y+d+w} L{x+w+d} {y+w}"/></g>'+extra)
