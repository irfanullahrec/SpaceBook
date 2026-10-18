"""Figure14.1 reproduces the source's printed labels, including legacy/errant symbols."""
import html
def diagram(lang):
    label={'en':['s-block','p-block','d-block','f-block'],'ur':['s بلاک','p بلاک','d بلاک','f بلاک'],'ps':['s بلاک','p بلاک','d بلاک','f بلاک']}[lang]
    s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 590" role="img" aria-label="Figure 14.1"><rect width="900" height="590" fill="white"/>'];w=45;h=49;x0=30;y0=65
    def text(x,y,value,size=16):s.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#111">{html.escape(str(value))}</text>')
    def cell(c,r,num,symbol,fill):
        x=x0+c*w;y=y0+r*h;s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#334155"/>')
        if num:text(x+w/2,y+15,num,13);text(x+w/2,y+32,symbol,17)
    def arrow(x1,x2,y,value):
        s.append(f'<path d="M{x1} {y}H{x2}m-6 -4l6 4l-6 4 M{x1+6} {y-4}l-6 4l6 4" fill="none" stroke="#111" stroke-width="1.6"/>')
        if value:
            mid=(x1+x2)/2;s.append(f'<rect x="{mid-14}" y="{y-10}" width="28" height="17" fill="#fef08a"/>');text(mid,y+3,value,13)
    for r,(n,a,b) in enumerate([(1,'H',''),(3,'Li','Be'),(11,'Na','Mg'),(19,'K','Ca'),(37,'Rb','Sr'),(55,'Cs','Ba'),(87,'Fr','Ra')]):
        cell(0,r,n,a,'#f8fafc')
        if r:cell(1,r,n+1,b,'#f8fafc')
        arrow(x0+3,x0+(2 if r else 1)*w-3,y0+r*h+41,f'{r+1}s')
    cell(17,0,2,'He','#fef9c3');arrow(x0+17*w+3,x0+18*w-3,y0+41,'1s')
    for r,n,syms in [(1,5,'B C N O F Ne'),(2,13,'Al Si P S Cl Ar'),(3,31,'Ga Ge As Se Br Kr'),(4,49,'In Sn Sb Te I Xe'),(5,81,'Tl Pb Bi Po At Rn'),(6,113,'Uut Fl')]:
        seq=syms.split()
        for i in range(6):cell(12+i,r,n+i if i<len(seq) else '',seq[i] if i<len(seq) else '', '#bbf7d0')
        if r<6:arrow(x0+12*w+3,x0+18*w-3,y0+r*h+41,f'{r+1}p')
    for r,nums,syms in [(3,list(range(21,31)),'Sc Ti V Cr Mn Fe Co Ni Cu Zn'),(4,list(range(39,49)),'Y Zr Nb Mo Tc Ru Rh Pd Ag Cd'),(5,[57]+list(range(72,81)),'La Hf Ta W Re Os Ir Pt Au Hg'),(6,[89]+list(range(104,113)),'Ac Rf Db Sg Bb Hs Mt Ds Rg Cn')]:
        for i,(n,sym) in enumerate(zip(nums,syms.split())):cell(2+i,r,n,sym,'#fed7aa')
        arrow(x0+2*w+3,x0+12*w-3,y0+r*h+41,f'{r}d')
    groups=['IA','IIA','IIIB','IVB','VB','VIB','VIIB','','VIIIB','','IB','IIB','IIIA','IVA','VA','VIA','VIIA','VIIIA']
    for c,g in enumerate(groups):
        y=y0-23 if c in [0,17] else y0+h-23 if c==1 or c>=12 else y0+3*h-23
        text(x0+c*w+w/2,y,c+1,13);text(x0+c*w+w/2,y+17,g,13)
    s.append(f'<path d="M{x0+7*w} {y0+3*h-3}v-6h{3*w}v6" fill="none" stroke="#111"/>')
    for j,(n,syms) in enumerate([(58,'Ce Pr Nd Pm Sm Eu Gd Td Dy Ho Er Tm Yb Lu'),(90,'Th Pa U Np Pu Am Cn Bk Cf Es Fm Md No Lr')]):
        for i,sym in enumerate(syms.split()):
            x=180+i*w;y=435+j*h;s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fbcfe8" stroke="#334155"/>');text(x+w/2,y+15,n+i,13);text(x+w/2,y+32,sym,17)
        arrow(183,807,435+j*h+41,f'{j+4}f')
    s.append('<path d="M142 378L175 435L175 533 M142 329L142 425L175 435" fill="none" stroke="#be123c" stroke-width="2"/>')
    for x,y,v in [(72,23,label[0]),(715,41,label[1]),(345,182,label[2]),(82,480,label[3])]:text(x,y,v,21)
    s.append('</svg>');return ''.join(s)
