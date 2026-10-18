"""Reusable coded SVG chart builders for Class 11 Statistics pages."""
from statlib import svg,T
def _axes(W,H,L,R,Tp,B,ymin,ymax,yticks,grid=False,title=None,sub=None):
    pw,ph=W-L-R,H-Tp-B
    Y=lambda v:Tp+ph*(1-(v-ymin)/(ymax-ymin))
    o=''
    if title:o+=T(L+pw/2,18,title,13,'middle',600)
    if sub:o+=T(L+pw/2,34,sub,11)
    for t in yticks:
        if grid:o+=f'<line x1="{L}" y1="{Y(t):.1f}" x2="{L+pw}" y2="{Y(t):.1f}" stroke="#bbb"/>'
        o+=T(L-6,Y(t)+4,str(t),11,'end')+f'<line x1="{L-3}" y1="{Y(t):.1f}" x2="{L}" y2="{Y(t):.1f}" stroke="#333"/>'
    o+=f'<line x1="{L}" y1="{Tp}" x2="{L}" y2="{Tp+ph}" stroke="#333" stroke-width="1.5"/><line x1="{L}" y1="{Tp+ph}" x2="{L+pw}" y2="{Tp+ph}" stroke="#333" stroke-width="1.5"/>'
    return o,Y,pw,ph
def line_chart(title,sub,xs,ys,ymax,yticks,aria,W=560,H=320,xlabel='',ylabel='',color='#1c7ab8',grid=True):
    L,R,Tp,B=60,20,52,40
    o,Y,pw,ph=_axes(W,H,L,R,Tp,B,0,ymax,yticks,grid,title,sub)
    n=len(xs);X=lambda i:L+pw*(i+.5)/n
    for i in range(n+1):
        o+=f'<line x1="{L+pw*i/n:.1f}" y1="{Tp}" x2="{L+pw*i/n:.1f}" y2="{Tp+ph}" stroke="#bbb"/>' if grid else ''
    o+='<polyline fill="none" stroke="'+color+'" stroke-width="2.5" points="'+' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(ys))+'"/>'
    for i,v in enumerate(ys): o+=f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="{color}"/>'+T(X(i),Tp+ph+16,str(xs[i]),11)
    if xlabel:o+=T(L+pw/2,H-6,xlabel,12)
    if ylabel:o+=f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">{ylabel}</text>'
    return svg(W,H,aria,o)
def stems(title,xs,ys,ymax,yticks,aria,W=560,H=320,xlabel='',ylabel='',scale=None):
    L,R,Tp,B=70,30,52,48
    o,Y,pw,ph=_axes(W,H,L,R,Tp,B,0,ymax,yticks,False,title)
    n=len(xs);X=lambda i:L+pw*(i+.5)/n
    for i,v in enumerate(ys):
        o+=f'<line x1="{X(i):.1f}" y1="{Y(v):.1f}" x2="{X(i):.1f}" y2="{Y(0):.1f}" stroke="#111" stroke-width="1.5"/><circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="4.5" fill="#111"/>'+T(X(i),Tp+ph+16,str(xs[i]),11)
    if xlabel:o+=T(L+pw/2,H-6,xlabel,12)
    if ylabel:o+=f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">{ylabel}</text>'
    if scale:
        for k,t in enumerate(scale): o+=T(W-20,70+k*16,t,11,'end')
    return svg(W,H,aria,o)
def histogram(title,edges,heights,ymax,yticks,aria,W=560,H=320,xlabel='',ylabel='',scale=None,edge_labels=True):
    L,R,Tp,B=70,30,52,52
    o,Y,pw,ph=_axes(W,H,L,R,Tp,B,0,ymax,yticks,False,title)
    lo,hi=edges[0],edges[-1];X=lambda v:L+pw*0.04+(pw*0.92)*(v-lo)/(hi-lo)
    for i,h in enumerate(heights):
        o+=f'<rect x="{X(edges[i]):.1f}" y="{Y(h):.1f}" width="{X(edges[i+1])-X(edges[i]):.1f}" height="{Y(0)-Y(h):.1f}" fill="#e3f0fa" stroke="#1c4f7a" stroke-width="1.5"/>'
    if edge_labels:
        for e in edges: o+=f'<text transform="translate({X(e):.1f} {Tp+ph+14}) rotate(90)" font-size="10" font-family="Arial">{e}</text>'
    if xlabel:o+=T(L+pw/2,H-4,xlabel,12)
    if ylabel:o+=f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">{ylabel}</text>'
    if scale:
        for k,t in enumerate(scale): o+=T(W-20,70+k*16,t,11,'end')
    return svg(W,H,aria,o)

def xy(title,xlabels,ys,ymax,yticks,aria,W=560,H=320,xlabel='',ylabel='',smooth=False,marker='x',scale=None,color='#1c7ab8'):
    """Points sit at equally spaced x positions labelled by xlabels."""
    L,R,Tp,B=70,30,52,48
    o,Y,pw,ph=_axes(W,H,L,R,Tp,B,0,ymax,yticks,False,title)
    n=len(xlabels);X=lambda i:L+pw*0.06+pw*0.88*i/(n-1)
    pts=[(X(i),Y(v)) for i,v in enumerate(ys)]
    if smooth:
        d=f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
        for i in range(1,len(pts)):
            x0,y0=pts[i-1];x1,y1=pts[i];cx=(x0+x1)/2
            d+=f' C{cx:.1f},{y0:.1f} {cx:.1f},{y1:.1f} {x1:.1f},{y1:.1f}'
        o+=f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>'
    else:
        o+=f'<polyline fill="none" stroke="{color}" stroke-width="2" points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'"/>'
    for i,(x,y) in enumerate(pts):
        o+=(f'<path d="M{x-4:.1f},{y-4:.1f} L{x+4:.1f},{y+4:.1f} M{x-4:.1f},{y+4:.1f} L{x+4:.1f},{y-4:.1f}" stroke="{color}" stroke-width="1.6"/>' if marker=='x' else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{color}"/>')
        o+=T(x,Tp+ph+16,str(xlabels[i]),11)
    if xlabel:o+=T(L+pw/2,H-6,xlabel,12)
    if ylabel:o+=f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">{ylabel}</text>'
    if scale:
        for k,t in enumerate(scale): o+=T(W-20,70+k*16,t,11,'end')
    return svg(W,H,aria,o)
def step_chart(title,xs,cfs,ymax,yticks,aria,W=560,H=320,xlabel='',ylabel='',scale=None):
    """Step function: cumulative frequency cfs[i] holds from xs[i] to xs[i+1]; last value ends with a drop to zero."""
    L,R,Tp,B=70,30,52,48
    o,Y,pw,ph=_axes(W,H,L,R,Tp,B,0,ymax,yticks,False,title)
    n=len(xs);X=lambda i:L+pw*0.06+pw*0.88*i/n
    d=f'M{X(0):.1f},{Y(0):.1f}'
    for i,v in enumerate(cfs):
        d+=f' L{X(i):.1f},{Y(v):.1f} L{X(i+1):.1f},{Y(v):.1f}'
    d+=f' L{X(n):.1f},{Y(0):.1f}'
    o+=f'<path d="{d}" fill="none" stroke="#111" stroke-width="2.2"/>'
    for i,x in enumerate(xs): o+=T(X(i),Tp+ph+16,str(x),11)
    if xlabel:o+=T(L+pw/2,H-6,xlabel,12)
    if ylabel:o+=f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">{ylabel}</text>'
    if scale:
        for k,t in enumerate(scale): o+=T(W-20,70+k*16,t,11,'end')
    return svg(W,H,aria,o)
