import math, json
def atom(cx,cy,sym,shells,r0=20,dr=14,er=3.5,col='#2563eb'):
    o=['<circle cx="%d" cy="%d" r="%d" fill="#fbcfe8" stroke="#be185d"/>'%(cx,cy,r0-6),'<text x="%d" y="%d" text-anchor="middle" font-size="11" font-weight="bold">%s</text>'%(cx,cy+4,sym)]
    for i,e in enumerate(shells):
        r=r0+4+i*dr; o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>'%(cx,cy,r))
        for k in range(e):
            a=2*math.pi*k/max(e,1)-math.pi/2; o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'%(cx+r*math.cos(a),cy+r*math.sin(a),er,col))
    return ''.join(o)
def pair(sym,p,n,s1,s2,lab1,lab2,net1,net2):
    o=['<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="%s atom and ion">'%sym]
    o.append(atom(90,95,sym,s1)); o.append(atom(380,95,sym,s2))
    def txt(x,lab,e,net):
        return '<text x="%d" y="50" font-weight="bold">%s</text><text x="%d" y="78">%d protons</text><text x="%d" y="96">%d electrons</text><line x1="%d" y1="102" x2="%d" y2="102" stroke="#000"/><text x="%d" y="118">%s net charge</text>'%(x,lab,x,p,x,e,x,x+95,x,net)
    o.append(txt(170,lab1,sum(s1),net1)); o.append(txt(460,lab2,sum(s2),net2))
    o.append('<path d="M270 95 H300" stroke="#000" stroke-width="2" marker-end="url(#ah)"/><defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z"/></marker></defs>')
    o.append('</svg>'); return ''.join(o)
d={'NaIon':pair('Na',11,12,[2,8,1],[2,8],'Na atom','Na⁺ (positive ion)','0','+1'),
   'ClIon':pair('Cl',17,18,[2,8,7],[2,8,8],'Cl atom','Cl⁻ (negative ion)','0','−1')}
names=['hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen','oxygen','fluorine','neon','sodium','magnesium','aluminium','silicon','phosphorus','sulphur','chlorine','argon']
neut=[0,2,4,5,6,6,7,8,10,10,12,12,14,14,16,16,18,22]
def conf(z):
    s=[];
    for cap in (2,8,8):
        t=min(cap,z); s.append(t); z-=t
        if z==0: break
    return s
g=['<svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="9" role="img" aria-label="Electronic arrangement of the first eighteen elements">']
pos={}
for z in range(1,19):
    if z==1: c,r=0,0
    elif z==2: c,r=7,0
    else: c=(z-3)%8; r=1+(z-3)//8
    x=c*80; y=r*86
    g.append('<rect x="%d" y="%d" width="78" height="84" fill="#fff" stroke="#1e3a8a"/><text x="%d" y="%d">%d</text>'%(x+1,y+1,x+4,y+11,z))
    g.append(atom(x+40,y+40,'%dp'%z,conf(z),r0=12,dr=8,er=2.2).replace('font-size="11"','font-size="7"'))
    g.append('<text x="%d" y="%d" text-anchor="middle">%s (%dn)</text>'%(x+40,y+80,names[z-1],neut[z-1]))
g.append('</svg>'); d['Grid18']=''.join(g)
json.dump(d,open('ions.json','w',encoding='utf-8')); print('ok')
def single(sym,p,shells,lab,charge):
    o=['<svg viewBox="0 0 180 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="%s">'%lab]
    if shells: o.append(atom(90,75,sym,shells))
    else: o.append('<circle cx="90" cy="75" r="14" fill="#fbcfe8" stroke="#be185d"/><text x="90" y="79" text-anchor="middle" font-size="11" font-weight="bold">%s</text>'%sym)
    o.append('<text x="90" y="150" text-anchor="middle" font-weight="bold">%s (%s)</text><text x="90" y="165" text-anchor="middle" font-size="10">%d protons, %d electrons</text></svg>'%(lab,charge,p,sum(shells)))
    return ''.join(o)
d['Hion']=single('H',1,[],'Hydrogen ion','H⁺')
d['Liion']=single('Li',3,[2],'Lithium ion','Li⁺')
d['Oion']=single('O',8,[2,8],'Oxygen ion','O²⁻')
json.dump(d,open('ions.json','w',encoding='utf-8')); print('ok2')
o=['<svg viewBox="0 0 440 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Electronic arrangement of magnesium and oxygen">',atom(110,80,'Mg',[2,8,2],r0=18,dr=14),atom(330,80,'O',[2,6],r0=18,dr=16,col='#be123c'),'<text x="110" y="165" text-anchor="middle">Mg (2, 8, 2)</text><text x="330" y="165" text-anchor="middle">O (2, 6)</text></svg>']
d['MgO']=''.join(o)
st={'H':('#bae6fd','#0284c7',11),'C':('#525252','#171717',17),'O':('#a3a3a3','#404040',17),'N':('#38bdf8','#0369a1',17)}
mols=[('H2O',[('H',-20,8),('O',0,0),('H',20,8)]),('CO',[('C',-15,0),('O',15,0)]),('O2',[('O',-15,0),('O',15,0)]),('NH3',[('H',-24,6),('N',0,-6),('H',0,14),('H',24,6)]),('NO',[('N',-15,0),('O',15,0)]),('NO2',[('O',-28,0),('N',0,0),('O',28,0)]),('CO2',[('O',-30,0),('C',0,0),('O',30,0)]),('H2',[('H',-10,0),('H',10,0)])]
g=['<svg viewBox="0 0 420 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Molecule chart: atoms of hydrogen, carbon, oxygen and nitrogen">']
for i,(s,(f,sk,r)) in enumerate(st.items()):
    x=50+i*105; g.append('<circle cx="%d" cy="22" r="%d" fill="%s" stroke="%s"/><text x="%d" y="55" text-anchor="middle">%s</text>'%(x,r,f,sk,x,{'H':'Hydrogen-H','C':'Carbon-C','O':'Oxygen-O','N':'Nitrogen-N'}[s]))
for k,(name,atoms) in enumerate(mols):
    col=k%2; row=k//2; x=col*210; y=65+row*66
    g.append('<rect x="%d" y="%d" width="208" height="64" fill="#fff" stroke="#000"/><text x="%d" y="%d">%d)</text>'%(x+1,y,x+6,y+15,k+1))
    for s,dx,dy in atoms:
        f,sk,r=st[s]; g.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s"/>'%(x+105+dx,y+30+dy,r-3,f,sk))
g.append('</svg>'); d['MolChart']=''.join(g)
json.dump(d,open('ions.json','w',encoding='utf-8')); print('ok3')
