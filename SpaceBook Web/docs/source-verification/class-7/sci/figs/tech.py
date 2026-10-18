import json, math
def pie(title,parts,cx=110,cy=120,r=80):
    o=['<svg viewBox="0 0 330 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="%s">'%title,'<text x="10" y="18" font-weight="bold">%s</text>'%title]
    a=-math.pi/2
    for i,(lab,val,col) in enumerate(parts):
        b=a+2*math.pi*val/100; large=1 if val>50 else 0
        o.append('<path d="M%d %d L%.1f %.1f A%d %d 0 %d 1 %.1f %.1f Z" fill="%s" stroke="#fff" stroke-width="2"/>'%(cx,cy,cx+r*math.cos(a),cy+r*math.sin(a),r,r,large,cx+r*math.cos(b),cy+r*math.sin(b),col))
        o.append('<rect x="215" y="%d" width="14" height="14" fill="%s"/><text x="235" y="%d">%s %g%%</text>'%(60+i*24,col,72+i*24,lab,val)); a=b
    o.append('</svg>'); return ''.join(o)
d={'EarthPie':pie('Surface of the Earth',[('Water',70,'#2563eb'),('Land',30,'#d6a77a')]),
   'WaterPie':pie('World water distribution',[('Salt water',98,'#0ea5e9'),('Fresh water',2,'#1e3a8a')]),
   'FreshPie':pie('Fresh water (2%)',[('Ice',87,'#bae6fd'),('Groundwater',12,'#0369a1'),('Rivers and lakes',1,'#16a34a')])}
json.dump(d,open('tech.json','w',encoding='utf-8')); print('ok')
