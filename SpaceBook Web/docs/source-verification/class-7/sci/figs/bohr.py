import math, json
def bohr(name,p,n,shells,size=200):
    c=size//2; out=['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" role="img" aria-label="%s atom: %d protons, %d neutrons, electrons %s">'%(size+120,size,name,p,n,",".join(map(str,shells)))]
    out.append('<circle cx="%d" cy="%d" r="22" fill="#38bdf8" stroke="#0369a1"/>'%(c,c))
    out.append('<text x="%d" y="%d" text-anchor="middle" font-size="11" font-weight="bold">%dp</text><text x="%d" y="%d" text-anchor="middle" font-size="11" font-weight="bold">%dn</text>'%(c,c-2,p,c,c+11,n))
    for i,e in enumerate(shells):
        r=36+i*22
        out.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#a16207" stroke-width="2"/>'%(c,c,r))
        for k in range(e):
            a=2*math.pi*k/e - math.pi/2
            out.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="#f472b6" stroke="#9d174d"/>'%(c+r*math.cos(a),c+r*math.sin(a)))
    lab=" ".join("KLM"[i] for i in range(len(shells)))
    out.append('<text x="%d" y="40" font-size="13" font-weight="bold">%s</text>'%(size+5,name))
    for i,e in enumerate(shells):
        out.append('<text x="%d" y="%d" font-size="11">Shell %d: %d</text>'%(size+5,62+i*16,i+1,e))
    out.append('<text x="%d" y="%d" font-size="11">%s</text><text x="%d" y="%d" font-size="11" font-weight="bold">%s</text>'%(size+5,62+len(shells)*16+8,lab,size+5,62+len(shells)*16+22,", ".join(map(str,shells))))
    out.append('</svg>'); return ''.join(out)
d={k:bohr(*v) for k,v in {'H':('Hydrogen',1,0,[1]),'Li':('Lithium',3,4,[2,1]),'B':('Boron',5,6,[2,3]),'O':('Oxygen',8,8,[2,6]),'Cl':('Chlorine',17,18,[2,8,7]),'N':('Nitrogen',7,7,[2,5]),'Na':('Sodium',11,12,[2,8,1])}.items()}
json.dump(d,open('bohr.json','w',encoding='utf-8'))
print('ok')
