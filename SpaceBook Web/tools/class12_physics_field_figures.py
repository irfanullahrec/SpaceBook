"""Native reusable field-line geometry for source Figures 11.4–11.7."""
from math import cos, sin, pi, hypot, atan2

def arrow(x,y,dx,dy,color='#a52b36',size=7):
    length=hypot(dx,dy)
    ux,uy=dx/length,dy/length
    bx,by=x-size*ux,y-size*uy
    return f'<path d="M{x} {y}L{bx-3*uy} {by+3*ux}L{bx+3*uy} {by-3*ux}Z" fill="{color}"/>'

CAPTIONS = {
 '11.4': ('Two equal and opposite charges', 'برابر مقدار کے دو مخالف بار', 'د مساوي مقدار دوه مخالف چارجونه'),
 '11.5': ('Two equal and positive charges placed at certain distance', 'ایک خاص فاصلے پر رکھے گئے برابر مقدار کے دو مثبت بار', 'په ټاکلي واټن کې ایښودل شوي د مساوي مقدار دوه مثبت چارجونه'),
 '11.6': ('Uniform electric field between charged plates.', 'بار دار تختیوں کے درمیان یکساں برقی میدان۔', 'د چارج لرونکو تختو ترمنځ یوشان برېښنايي میدان.'),
 '11.7': ('Electric lines of force on the surface of metal plate', 'دھاتی تختی کی سطح پر برقی خطوطِ قوت', 'د فلزي تختې پر سطحه د برېښنايي قوې کرښې'),
}

def shell(number, body, language='en'):
    suffix = number.replace('.', '-')+'-'+language
    caption = CAPTIONS[number][{'en':0,'ur':1,'ps':2}[language]]
    return f'''<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 400" role="img" aria-labelledby="phys12-figure-{suffix}-title" style="max-width:500px;width:100%;height:auto"><title id="phys12-figure-{suffix}-title">{caption}</title><defs><marker id="phys12-arrow-{suffix}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#a52b36"/></marker></defs>{body.replace('FIELDARROW', 'phys12-arrow-'+suffix)}</svg><figcaption>{'FIGURE' if language=='en' else 'شکل'} {number} — {caption}</figcaption></figure>'''

def charge(x,y,sign,r=20):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{"#f9a8d4" if sign=="+" else "#67e8f9"}" stroke="#64748b"/><text x="{x-7}" y="{y+7}" font-size="25">{sign}</text>'

def dipole():
    body = ''
    for sign in (-1,1):
        for height in (28,48,75,105,140,172):
            y = 190+sign*height
            start = 190+sign*17
            body += f'<path d="M160 {start} C180 {y} 209 {y} 240 {y} S303 {y} 320 {start}" fill="none" stroke="#7f1d1d" stroke-width="2" marker-mid="url(#FIELDARROW)"/>'
            body += arrow(240,y,1,0)
    for y in (183,190,197):
        body += f'<path d="M173 {y}H240 307" fill="none" stroke="#7f1d1d" stroke-width="2" marker-mid="url(#FIELDARROW)"/>'
        body += arrow(240,y,1,0)
    for sign in (-1,1):
        for angle in (15,35,55,75):
            radians = angle*pi/180
            sy = 190+sign*20*sin(radians)
            ey = 190+sign*170*sin(radians)
            body += f'<path d="M{150-20*cos(radians)} {sy}Q{90-40*cos(radians)} {ey} {max(8,150-180*cos(radians))} {ey}" fill="none" stroke="#7f1d1d" stroke-width="2" marker-end="url(#FIELDARROW)"/>'
            body += f'<path d="M{min(472,330+180*cos(radians))} {ey}Q{390+40*cos(radians)} {ey} {330+20*cos(radians)} {sy}" fill="none" stroke="#7f1d1d" stroke-width="2" marker-end="url(#FIELDARROW)"/>'
            body += arrow(max(8,150-180*cos(radians)),ey,-1,sign*.6)
            body += arrow(330+20*cos(radians),sy,-1,-sign*.6)
    return body+charge(150,190,'+')+charge(330,190,'−')

def like_charges():
    body = ''
    for x, direction in [(140,-1),(340,1)]:
        for angle in (-pi/2,-3*pi/4,pi,3*pi/4,pi/2):
            dx = direction*abs(cos(angle))
            dy = sin(angle)
            body += f'<path d="M{x+23*dx} {190+23*dy}Q{x+75*dx} {190+85*dy} {x+127*dx} {190+175*dy}" fill="none" stroke="#a52b36" stroke-width="2" marker-end="url(#FIELDARROW)"/>'
            body += arrow(x+127*dx,190+175*dy,52*dx,90*dy)
        for ysign in (-1,1):
            for bend in (35,65,85):
                endx = x-direction*bend
                body += f'<path d="M{x-direction*16} {190+ysign*12}C{endx} {190+ysign*35} {endx} {190+ysign*92} {endx} {190+ysign*175}" fill="none" stroke="#a52b36" stroke-width="2" marker-end="url(#FIELDARROW)"/>'
                body += arrow(endx,190+ysign*175,0,ysign)
    body += charge(140,190,'+')+charge(340,190,'+')
    for x,y,label,ex,ey in [(198.875,113.5,'C',207.7,77.5),(281.125,113.5,'D',272.3,77.5),(281.125,266.5,'B',272.3,302.5),(411.5,283.25,'A',435.5,321.5)]:
        body += f'<circle cx="{x}" cy="{y}" r="3" fill="#65a30d"/><text x="{x+7}" y="{y-5}">{label}</text><line x1="{x}" y1="{y}" x2="{ex}" y2="{ey}" stroke="#0d9488" stroke-width="2" marker-end="url(#FIELDARROW)"/><text x="{ex+6}" y="{ey}">E⃗</text>'
        body += arrow(ex,ey,ex-x,ey-y,'#0d9488')
    body += '<line x1="405" y1="289" x2="439" y2="343" stroke="#334155" stroke-width="2" marker-end="url(#FIELDARROW)"/><text x="439" y="357">F⃗</text>'+arrow(439,343,34,54,'#334155')
    return body

def plates():
    body = '<rect x="75" y="80" width="330" height="17" fill="#f8fafc" stroke="#334155"/><rect x="75" y="285" width="330" height="17" fill="#f8fafc" stroke="#334155"/>'
    for x in range(95,395,20):
        body += f'<text x="{x}" y="94">+</text><text x="{x}" y="299">−</text><path d="M{x} 98V195 284" stroke="#a52b36" stroke-width="1.5" fill="none" marker-mid="url(#FIELDARROW)"/>'
        body += arrow(x,195,0,1)
    for offset in (15,40):
        body += f'<path d="M80 98C{80-offset} 124 {80-offset} 163 {80-offset} 190 S{80-offset} 256 80 285" fill="none" stroke="#a52b36" marker-mid="url(#FIELDARROW)"/>'
        body += f'<path d="M400 98C{400+offset} 124 {400+offset} 163 {400+offset} 190 S{400+offset} 256 400 285" fill="none" stroke="#a52b36" marker-mid="url(#FIELDARROW)"/>'
        body += arrow(80-offset,190,0,1)+arrow(400+offset,190,0,1)
    return body

def conductor():
    body = '<rect x="360" y="45" width="15" height="310" fill="#d5a469" stroke="#a16207"/>'
    for y in range(65,345,35):
        body += f'<text x="363" y="{y}">−</text>'
    for radius in (40,58,78,101,126):
        body += f'<circle cx="195" cy="200" r="{radius}" stroke="#94a3b8" fill="none"/>'
    for target in (60,100,145,200,255,300,340):
        angle=atan2(target-200,165)
        body += f'<path d="M{195+25*cos(angle)} {200+25*sin(angle)}C{245 if target==200 else 225} {target} 305 {target} 359 {target}" fill="none" stroke="#a52b36" stroke-width="1.4" marker-end="url(#FIELDARROW)"/>'+arrow(350,target,1,0)
    for angle in (pi/2,3*pi/4,pi,5*pi/4,3*pi/2):
        body += f'<line x1="{195+27*cos(angle)}" y1="{200+27*sin(angle)}" x2="{195+150*cos(angle)}" y2="{200+150*sin(angle)}" stroke="#a52b36" marker-end="url(#FIELDARROW)"/>'
        body += arrow(195+140*cos(angle),200+140*sin(angle),cos(angle),sin(angle))
    body += '<circle cx="195" cy="200" r="25" fill="#d1d5db" stroke="#64748b"/>'
    for angle in [i*pi/4 for i in range(8)]:
        body += f'<text x="{190+21*cos(angle)}" y="{205+21*sin(angle)}" font-size="14">+</text>'
    return body+'<text x="285" y="351">E</text>'

def source_blocks():
    return [{'id':'phys12-field-figure-'+number, 'svg':shell(number,body()),
             'svgUrdu':shell(number,body(),'ur'), 'svgPashto':shell(number,body(),'ps')}
            for number,body in [('11.4',dipole),('11.5',like_charges),('11.6',plates),('11.7',conductor)]]
