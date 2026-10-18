"""Helpers that write coded SVG graphs / tables for Class 11 Mathematics page transcriptions."""
import math
OUT=r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-11\math\pages'
COLS=['#2563eb','#dc2626','#16a34a','#9333ea']
def graph(w,h,xr,yr,curves,pts=(),title='',step=1,ystep=None,labels=(),n=70):
    xmin,xmax=xr;ymin,ymax=yr
    def X(x):return 20+(x-xmin)/(xmax-xmin)*(w-40)
    def Y(y):return h-20-(y-ymin)/(ymax-ymin)*(h-40)
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title>']
    ax=Y(0) if ymin<=0<=ymax else h-20
    ay=X(0) if xmin<=0<=xmax else 20
    s.append(f'<path d="M20 {ax:.1f}H{w-12}M{ay:.1f} {h-12}V12" stroke="#334155" stroke-width="1.6" fill="none"/>')
    s.append(f'<path d="M{w-12} {ax:.1f}l-8-4v8Z M{ay:.1f} 12l-4 8h8Z" fill="#334155"/>')
    ys=ystep or step
    xt=math.ceil(xmin/step)*step
    while xt<=xmax+1e-9:
        if abs(xt)>1e-9:s.append(f'<path d="M{X(xt):.1f} {ax-3:.1f}v6" stroke="#334155" stroke-width="1"/><text x="{X(xt):.1f}" y="{ax+15:.1f}" font-size="9" text-anchor="middle" fill="#334155" font-family="sans-serif">{xt:g}</text>')
        xt+=step
    yt=math.ceil(ymin/ys)*ys
    while yt<=ymax+1e-9:
        if abs(yt)>1e-9:s.append(f'<path d="M{ay-3:.1f} {Y(yt):.1f}h6" stroke="#334155" stroke-width="1"/><text x="{ay-6:.1f}" y="{Y(yt)+3:.1f}" font-size="9" text-anchor="end" fill="#334155" font-family="sans-serif">{yt:g}</text>')
        yt+=ys
    s.append(f'<text x="{w-16}" y="{ax-6:.1f}" font-size="12" font-style="italic" fill="#0f172a">x</text><text x="{ay+7:.1f}" y="22" font-size="12" font-style="italic" fill="#0f172a">y</text>')
    for fn,col,x0,x1 in curves:
        d=[];prev=False
        for i in range(n+1):
            x=x0+(x1-x0)*i/n
            try:y=fn(x)
            except Exception:y=None
            ok=y is not None and ymin-1e-6<=y<=ymax+1e-6
            if ok:d.append(f'{"L" if prev else "M"}{X(x):.1f} {Y(y):.1f}')
            prev=ok
        s.append(f'<path d="{" ".join(d)}" fill="none" stroke="{col}" stroke-width="2.2"/>')
    for x,y,lab,dx,dy in pts:
        s.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3" fill="#dc2626"/><text x="{X(x)+dx:.1f}" y="{Y(y)+dy:.1f}" font-size="10" font-family="sans-serif" fill="#0f172a">{lab}</text>')
    for t,x,y,col in labels:
        s.append(f'<text x="{x}" y="{y}" font-size="12" font-family="sans-serif" fill="{col}">{t}</text>')
    s.append('</svg>')
    return ''.join(s)
def svgblock(en,ur,ps,svg):return f'svg {en} || {ur} || {ps}\n{svg}\nendsvg\n'
def tbl(cap,rows):
    out=f'table {cap}\n'+'th | '+' | '.join(rows[0])+'\n'
    for r in rows[1:]:out+='tr | '+' | '.join(r)+'\n'
    return out+'endtable\n'
def pt(x,y,dx=6,dy=-4):return (x,y,f'({x:g},{y:g})',dx,dy)

def _clip(poly,a,b,c,op):
    """clip polygon by half-plane a*x+b*y (op) c, op in ('<=','>=')"""
    sgn=1 if op=='<=' else -1
    def val(p):return sgn*(a*p[0]+b*p[1]-c)
    out=[]
    for i in range(len(poly)):
        p,q=poly[i],poly[(i+1)%len(poly)]
        vp,vq=val(p),val(q)
        if vp<=1e-9:out.append(p)
        if (vp<-1e-9 and vq>1e-9) or (vp>1e-9 and vq<-1e-9):
            t=vp/(vp-vq);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out
def region(w,h,xr,yr,ineqs,lines,pts=(),title='',step=1,ystep=None,fill='#7dd3fc',labels=(),dashed=()):
    """ineqs: list of (a,b,c,op) whose intersection is shaded; lines: list of (a,b,c) boundaries to draw; pts: (x,y,label,dx,dy)"""
    xmin,xmax=xr;ymin,ymax=yr
    def X(x):return 20+(x-xmin)/(xmax-xmin)*(w-40)
    def Y(y):return h-20-(y-ymin)/(ymax-ymin)*(h-40)
    poly=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)]
    for a,b,c,op in ineqs:poly=_clip(poly,a,b,c,op) if poly else poly
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title>']
    if poly:s.append('<polygon points="'+' '.join(f'{X(a):.1f},{Y(b):.1f}' for a,b in poly)+f'" fill="{fill}" opacity="0.6"/>')
    ax=Y(0) if ymin<=0<=ymax else h-20
    ay=X(0) if xmin<=0<=xmax else 20
    s.append(f'<path d="M20 {ax:.1f}H{w-12}M{ay:.1f} {h-12}V12" stroke="#334155" stroke-width="1.5" fill="none"/><path d="M{w-12} {ax:.1f}l-8-4v8Z M{ay:.1f} 12l-4 8h8Z" fill="#334155"/>')
    t=math.ceil(xmin/step)*step
    while t<=xmax+1e-9:
        if abs(t)>1e-9:s.append(f'<path d="M{X(t):.1f} {ax-3:.1f}v6" stroke="#334155" stroke-width="1"/><text x="{X(t):.1f}" y="{ax+14:.1f}" font-size="9" text-anchor="middle" fill="#334155" font-family="sans-serif">{t:g}</text>')
        t+=step
    ys=ystep or step
    t=math.ceil(ymin/ys)*ys
    while t<=ymax+1e-9:
        if abs(t)>1e-9:s.append(f'<path d="M{ay-3:.1f} {Y(t):.1f}h6" stroke="#334155" stroke-width="1"/><text x="{ay-5:.1f}" y="{Y(t)+3:.1f}" font-size="9" text-anchor="end" fill="#334155" font-family="sans-serif">{t:g}</text>')
        t+=ys
    for i,(a,b,c) in enumerate(lines):
        # endpoints of the line within the viewport
        cand=[]
        if abs(b)>1e-12:
            for x in (xmin,xmax):
                y=(c-a*x)/b
                if ymin-1e-9<=y<=ymax+1e-9:cand.append((x,y))
        if abs(a)>1e-12:
            for y in (ymin,ymax):
                x=(c-b*y)/a
                if xmin-1e-9<=x<=xmax+1e-9:cand.append((x,y))
        cand=sorted(set((round(p[0],6),round(p[1],6)) for p in cand))
        if len(cand)>=2:
            p,q=cand[0],cand[-1]
            s.append(f'<path d="M{X(p[0]):.1f} {Y(p[1]):.1f}L{X(q[0]):.1f} {Y(q[1]):.1f}" stroke="#0f172a" stroke-width="1.9" fill="none"{" stroke-dasharray=\"6 5\"" if i in dashed else ""}/>')
    for x,y,lab,dx,dy in pts:
        s.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3" fill="#dc2626"/><text x="{X(x)+dx:.1f}" y="{Y(y)+dy:.1f}" font-size="10" font-family="sans-serif" fill="#0f172a">{lab}</text>')
    for tx,x,y,col in labels:
        s.append(f'<text x="{x}" y="{y}" font-size="11" font-family="sans-serif" fill="{col}">{tx}</text>')
    s.append(f'<text x="{ay+5:.1f}" y="{ax+12:.1f}" font-size="10" font-family="sans-serif" fill="#0f172a">O</text></svg>')
    return ''.join(s)
