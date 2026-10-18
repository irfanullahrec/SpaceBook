"""Code-only diagrams for vector exercises, with no textbook image embeds."""
import math
from html import escape

def arrow(a,b,color='#027da8',label='',offset=(0,-8)):
    x,y=a;u,v=b;angle=math.atan2(v-y,u-x);s=7
    points=[(u,v),(u-s*math.cos(angle-.45),v-s*math.sin(angle-.45)),(u-s*math.cos(angle+.45),v-s*math.sin(angle+.45))]
    out=f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="{color}" stroke-width="2.3"/><polygon points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in points)+f'" fill="{color}"/>'
    if label:out+=f'<text x="{(x+u)/2+offset[0]}" y="{(y+v)/2+offset[1]}" fill="{color}">{escape(label)}</text>'
    return out
def wrap(body,title,w=320,h=260):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title><g font-family="Arial,sans-serif" font-size="15" fill="#172b4d">{body}</g></svg>'
def polygon(points,labels):
    out='<polygon points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#334155" stroke-width="2"/>'
    for (x,y),label in zip(points,labels):
        dx=(x-160)/15;dy=(y-125)/14
        out+=f'<text x="{x+dx-5:.1f}" y="{y+dy+5:.1f}">{label}</text>'
    return out
def source_figures():
    p=[(105,208),(215,208),(270,113),(215,18),(105,18),(50,113)]
    h1=wrap(polygon(p,'ABCDEF')+arrow(p[0],p[1],label='a',offset=(0,20))+arrow(p[1],p[2],label='b',offset=(12,0))+arrow(p[2],p[3],label='c',offset=(12,0)),'Exercise 3.1, question 1: regular hexagon ABCDEF')
    grid=''.join(f'<path d="M{x} 15V215 M20 {x-5}H220" stroke="#cbd5e1" stroke-width="1"/>' for x in range(20,221,20))
    h2=wrap(grid+arrow((40,135),(100,55),label='a')+arrow((180,155),(160,95),label='b',offset=(13,0)),'Exercise 3.1, question 2: vectors a and b on a square grid',245,235)
    h6=wrap(polygon([(40,215),(230,35),(275,210)],['O','P','R'])+arrow((40,215),(230,35),label='p',offset=(-10,-8))+arrow((40,215),(275,210),label='r',offset=(0,20))+'<circle cx="252.5" cy="122.5" r="3" fill="#027da8"/><text x="263" y="127">M</text>','Exercise 3.1, question 6: triangle OPR, M the midpoint of PR')
    p7=[(160,18),(65,73),(65,183),(160,238),(255,183),(255,73)]
    h7=wrap(polygon(p7,'ABCDEF')+'<circle cx="160" cy="128" r="3" fill="#b91c1c"/><text x="168" y="133">O</text>','Exercise 3.1, question 7: regular hexagon ABCDEF with centre O',320,275)
    return {1:h1,2:h2,6:h6,7:h7}
def construction():
    body=''
    for index,(na,nb,label) in enumerate([(1,2,'a + 2b'),(2,-1,'2a − b'),(3,-2,'3a − 2b')]):
        # Uniform scale within each panel, translated head-to-tail copies.
        vectors=[((3,4),'a')]*na+[((-1 if nb>0 else 1,3 if nb>0 else -3),'b' if nb>0 else '−b')]*abs(nb)
        points=[(0,0)]
        for (x,y),_ in vectors:points.append((points[-1][0]+x,points[-1][1]+y))
        ox=index*250+30;oy=230;scale=16
        cv=lambda p:(ox+p[0]*scale,oy-p[1]*scale)
        body+=f'<text x="{ox}" y="24">({["i","ii","iii"][index]}) {label}</text>'
        for j,(_,name) in enumerate(vectors):
            body+=arrow(cv(points[j]),cv(points[j+1]),'#64748b',name,(0,-9))
        body+=arrow(cv(points[0]),cv(points[-1]),'#dc2626')
        body+=f'<circle cx="{ox}" cy="{oy}" r="3" fill="#172b4d"/><text x="{ox-13}" y="{oy+17}">O</text>'
    return wrap(body,'Head-to-tail constructions; red arrows are the three required resultant vectors',760,265)
