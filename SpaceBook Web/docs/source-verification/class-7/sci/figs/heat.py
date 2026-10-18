import json, math
d={}
# mixing graph
X0,Y0,W,H=50,200,330,170
hot=' L'.join('%.1f,%.1f'%(X0+t*3.3, Y0-H*(0.5+0.45*math.exp(-t/15))) for t in range(0,101))
cold=' L'.join('%.1f,%.1f'%(X0+t*3.3, Y0-H*(0.5-0.45*math.exp(-t/15))) for t in range(0,101))
d['Mix107']=('<svg viewBox="0 0 420 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Temperature-time graph: hot coffee cools and cold milk warms to the same mixing temperature">'
 '<path d="M%d 20 V%d H%d" fill="none" stroke="#000" stroke-width="2"/>'%(X0,Y0,X0+W+20)+
 '<path d="M%s" fill="none" stroke="#be123c" stroke-width="2.5"/><path d="M%s" fill="none" stroke="#0f766e" stroke-width="2.5"/>'%(hot,cold)+
 '<text x="80" y="40" fill="#be123c">hot coffee</text><text x="80" y="185" fill="#0f766e">cold milk</text><text x="300" y="95">mixing temperature</text>'
 '<text x="200" y="225">time</text><text x="18" y="140" transform="rotate(-90 18 140)">temperature</text></svg>')
def grid(x0,y0,gap,col):
    return ''.join('<circle cx="%d" cy="%d" r="7" fill="%s"/>'%(x0+i*gap,y0+j*gap,col) for i in range(6) for j in range(6))
d['Exp108']=('<svg viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Thermal expansion of solids: particles move further apart on heating">'
 +grid(20,40,18,'#1d4ed8')+grid(230,20,28,'#2563eb')+
 '<path d="M150 90 H200" stroke="#0284c7" stroke-width="3"/><path d="M196 84 L206 90 L196 96z" fill="#0284c7"/>'
 '<text x="20" y="175" font-weight="bold">Particles before heat</text><text x="20" y="190">• vibrate a little</text><text x="20" y="204">• atoms in fixed positions</text>'
 '<text x="230" y="190" font-weight="bold">Particles after heat</text><text x="230" y="204">• more vibration, more space</text><text x="230" y="218">• still vibrate about fixed positions</text></svg>')
json.dump(d,open('heat.json','w',encoding='utf-8')); print('ok')
