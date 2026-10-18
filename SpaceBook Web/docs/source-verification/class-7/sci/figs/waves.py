import math, json
def sine(x0,y0,lam,amp,n,step=2):
    pts=[]
    for i in range(int(lam*n/step)+1):
        x=i*step; pts.append('%.1f,%.1f'%(x0+x,y0-amp*math.sin(2*math.pi*x/lam)))
    return 'M'+' L'.join(pts)
def defs(): return '<defs><marker id="wa" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z"/></marker><marker id="wb" markerWidth="8" markerHeight="8" refX="1" refY="4" orient="auto"><path d="M8 0 L0 4 L8 8z"/></marker></defs>'
d={}
# Fig 9.6 crest/trough, 3 waves
o=['<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Transverse wave with crest, trough and one wavelength marked">',defs()]
o.append('<path d="%s Z" fill="#38bdf8"/>'%sine(40,100,120,55,0.5))
o.append('<path d="M100,100 L'+' L'.join('%.1f,%.1f'%(40+x,100-55*math.sin(2*math.pi*x/120)) for x in range(60,121,2))+' Z" fill="#f472b6"/>')
o.append('<path d="%s" fill="none" stroke="#000" stroke-width="2.5"/>'%sine(40,100,120,55,3))
o.append('<line x1="20" y1="100" x2="420" y2="100" stroke="#000" stroke-dasharray="8 6"/><text x="425" y="96">(Mean</text><text x="425" y="111">position)</text>')
o.append('<text x="75" y="30">Crest</text><text x="135" y="185">Trough</text>')
o.append('<path d="M40 170 H160" stroke="#000" marker-end="url(#wa)" marker-start="url(#wb)"/><text x="80" y="195">Wave (λ)</text>')
o.append('</svg>'); d['Wave96']=''.join(o)
# Fig 9.9 wavelength and amplitude
o=['<svg viewBox="0 0 520 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Wavelength and amplitude of a transverse wave">',defs()]
o.append('<path d="%s" fill="none" stroke="#000" stroke-width="2.5"/>'%sine(40,110,160,60,2.5))
o.append('<line x1="20" y1="110" x2="460" y2="110" stroke="#000" stroke-dasharray="10 8"/>')
o.append('<path d="M80 30 H240" stroke="#1d4ed8" stroke-width="1.5" marker-end="url(#wa)" marker-start="url(#wb)"/><text x="120" y="22" fill="#1d4ed8" font-weight="bold">WAVELENGTH (crest to crest)</text>')
o.append('<path d="M160 195 H320" stroke="#1d4ed8" stroke-width="1.5" marker-end="url(#wa)" marker-start="url(#wb)"/><text x="170" y="190" fill="#1d4ed8" font-weight="bold">WAVELENGTH (trough to trough)</text>')
o.append('<path d="M80 110 V52" stroke="#be185d" stroke-width="1.5" marker-end="url(#wa)"/><text x="88" y="80" fill="#be185d" font-weight="bold">AMPLITUDE</text>')
o.append('<path d="M320 110 V168" stroke="#be185d" stroke-width="1.5" marker-end="url(#wa)"/><text x="328" y="150" fill="#be185d" font-weight="bold">AMPLITUDE</text>')
o.append('<text x="68" y="45">Crest</text><text x="150" y="182">Trough</text></svg>'); d['Wave99']=''.join(o)
# Longitudinal spring
def spring(segs,w=480,y=60):
    o=[]; x=20
    for dense,n in segs:
        gap=4 if dense else 11
        for i in range(n): o.append('<ellipse cx="%.1f" cy="%d" rx="%.1f" ry="16" fill="none" stroke="#111" stroke-width="2.2"/>'%(x,y,gap*0.9)); x+=gap
    return ''.join(o),x
segs=[(1,14),(0,8),(1,14),(0,8),(1,14),(0,8),(1,14)]
s,xe=spring(segs)
o=['<svg viewBox="0 0 %d 130" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Longitudinal wave in a spring: compressions and rarefactions">'%(int(xe)+20),s]
x=20; labs=[]
for dense,n in segs:
    gap=4 if dense else 11; mid=x+gap*n/2; labs.append('<text x="%.0f" y="%d" text-anchor="middle" fill="%s">%s</text>'%(mid,105 if dense else 30,'#be185d' if dense else '#1d4ed8','COMPRESSION' if dense else 'RAREFACTION')); x+=gap*n
o+=labs; o.append('</svg>'); d['Spring98']=''.join(o)
json.dump(d,open('waves.json','w',encoding='utf-8')); print('ok')
def pair(label,rows):
    h=len(rows)*70+10
    o=['<svg viewBox="0 0 470 %d" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="%s">'%(h,label)]
    for i,(lam,amp,col,txt) in enumerate(rows):
        y=40+i*70; o.append('<line x1="10" y1="%d" x2="330" y2="%d" stroke="#94a3b8" stroke-dasharray="4 4"/>'%(y,y))
        o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.5"/>'%(sine(10,y,lam,amp,320/lam),col)); o.append('<text x="340" y="%d" font-weight="bold">%s</text>'%(y+4,txt))
    o.append('</svg>'); return ''.join(o)
d['Freq910']=pair('High and low frequency waves',[(40,25,'#1e293b','High frequency'),(110,25,'#1e293b','Low frequency')])
d['Amp911a']=pair('Waves of different amplitude, same frequency',[(40,28,'#dc2626','Greater amplitude'),(40,12,'#2563eb','Smaller amplitude')])
d['Freq911b']=pair('Waves of different frequencies',[(110,25,'#1e293b','Lower frequency'),(35,25,'#dc2626','Higher frequency')])
d['Pitch915']=pair('Pitch and frequency of waves',[(80,25,'#be185d','a. higher pitch'),(200,25,'#1d4ed8','b. lower pitch')])
d['Loud']=pair('Loud and soft sound',[(60,30,'#dc2626','Loud (large amplitude)'),(60,10,'#2563eb','Soft (small amplitude)')])
json.dump(d,open('waves.json','w',encoding='utf-8')); print('ok2')
o=['<svg viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Displacement-time graph: amplitude 5 cm, time period 4 s, 3.5 waves in 14 s">']
X0,Y0,sx,sy=50,120,30,16
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#000"/><line x1="%d" y1="20" x2="%d" y2="220" stroke="#000"/>'%(X0,Y0,X0+14*sx+30,Y0,X0,X0))
for t in range(0,15,2): o.append('<text x="%d" y="%d" text-anchor="middle">%d</text><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#000"/>'%(X0+t*sx,Y0+14,t,X0+t*sx,Y0-3,X0+t*sx,Y0+3))
o.append('<text x="%d" y="%d">5 cm</text><text x="%d" y="%d">−5 cm</text>'%(X0-40,Y0-5*sy+4,X0-46,Y0+5*sy+4))
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#94a3b8" stroke-dasharray="3 3"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#94a3b8" stroke-dasharray="3 3"/>'%(X0,Y0-5*sy,X0+14*sx,Y0-5*sy,X0,Y0+5*sy,X0+14*sx,Y0+5*sy))
pts=' L'.join('%.1f,%.1f'%(X0+t/10*sx,Y0-5*sy*math.sin(2*math.pi*(t/10)/4)) for t in range(0,141))
o.append('<path d="M%s" fill="none" stroke="#1e293b" stroke-width="2.2"/>'%pts)
o.append('<text x="%d" y="%d">Time (seconds)</text><text x="14" y="130" transform="rotate(-90 14 130)">Displacement (cm)</text></svg>'%(X0+14*sx-40,Y0+30))
d['DispTime']=''.join(o)
json.dump(d,open('waves.json','w',encoding='utf-8')); print('ok3')
