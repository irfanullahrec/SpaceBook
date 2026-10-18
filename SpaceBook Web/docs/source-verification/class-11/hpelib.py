"""Helpers for Class 11 Health and Physical Education page records (keyed by scan number n; printed page = n - offset)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SO='[scan obscured]'
def page(n,chapter,printed,title,ur,ps,sid,layout=None):
    d=dict(chapter='hpe11-'+chapter,id=f'hpe11-s{n:03}-{sid}',title=title,headingUrdu=ur,headingPashto=ps,sourceLanguage='ur',source=dict(pdfPage=n,printedPage=printed),auditStatus='corrected; verification pending',paras=[],flow=[],vocabulary={})
    if layout: d['layout']=layout
    return d
def add(s,key,en,ur,ps,**meta):
    s['paras'].append(dict(id=f"hpe11-s{s['source']['pdfPage']:03}-{key}",en=en,ur=ur,ps=ps,**meta))
def head(s,key,en,ur,ps,**m): add(s,key,en,ur,ps,kind='heading',**m)
def cell(en,ur=None,ps=None): return dict(en=en,ur=ur if ur is not None else en,ps=ps if ps is not None else en)
def table(caption,cu,cp,headers,rows,**m): return dict(caption=caption,captionUrdu=cu,captionPashto=cp,headers=headers,rows=rows,**m)
def eqn(n,key,latex,text,**m):
    return dict(id=f'hpe11-s{n:03}-{key}',latex=latex,accessible=text,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')},**m)
def lab(en,ur=None,ps=None): return dict(en=en,ur=ur or en,ps=ps or en)
def svg(w,h,aria,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{aria}" style="width:100%;max-width:{w}px;height:auto;background:#fff">{body}</svg>'
def T(x,y,t,size=14,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'
def save(s): (ROOT/f"hpe-page-{s['source']['pdfPage']}.json").write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
class Flow:
    def __init__(s_,s): s_.s=s; s_.s.setdefault('equations',[]); s_.f=[]; s_.k=0
    def rest(s_):
        ids_=[p['id'] for p in s_.s['paras'][s_.k:]]; s_.k=len(s_.s['paras'])
        if ids_: s_.f.append(dict(type='paragraphs',ids=ids_))
    def e(s_,key,latex,text,**m):
        s_.rest(); s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text,**m)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def fg(s_,i): s_.rest(); s_.f.append(dict(type='figure',index=i))
    def tb(s_,i): s_.rest(); s_.f.append(dict(type='table',index=i))
    def done(s_): s_.rest(); s_.s['flow']=s_.f
