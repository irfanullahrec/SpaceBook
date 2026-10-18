"""Code-native PDF20 instructional figures, with translated labels."""
import html
def orbitals(lang,excited=False):
    labels={'en':['Ground state (C)','Excited state (C*)','Promotion'], 'ur':['بنیادی حالت (C)','برانگیختہ حالت (C*)','ترقی'], 'ps':['بنسټیز حالت (C)','پارېدلی حالت (C*)','لوړول']}[lang]
    parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 250" role="img" aria-label="Carbon orbital electron promotion"><rect width="520" height="250" fill="white"/>']
    def text(x,y,t,size=16):parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#111">{html.escape(t)}</text>')
    def row(y,occupancy):
        for i,(name,electrons) in enumerate(zip(['2s','2pₓ','2pᵧ','2p_z'],occupancy)):
            x=200+i*65;parts.append(f'<rect x="{x}" y="{y}" width="40" height="40" fill="none" stroke="#111"/>');text(x+20,y+63,name)
            for j,direction in enumerate(electrons):
                ax=x+14+j*13;end=y+8 if direction=='up' else y+32;start=y+32 if direction=='up' else y+8
                parts.append(f'<path d="M{ax} {start}V{end}m-4 {4 if direction=="up" else -4}l4 {-4 if direction=="up" else 4}l4 {4 if direction=="up" else -4}" fill="none" stroke="#be123c" stroke-width="2"/>')
    row(45,[['up','down'],['up'],['up'],[]]);text(98,72,labels[1] if excited else labels[0],14)
    if excited:
        text(323,23,labels[2]);parts.append('<path d="M220 40 Q285 -10 415 40m-8 -2l8 2l-4 -7" fill="none" stroke="#111"/>')
        parts.append('<path d="M285 109V142m-4 -6l4 6l4 -6" fill="none" stroke="#be123c"/>')
        row(150,[['up'],['up'],['up'],['up']])
    parts.append('</svg>');return ''.join(parts)
def tetrachloride(lang):
    lab={'en':['Bond Distance,','Bond angle,'], 'ur':['بند کا فاصلہ،','بند کا زاویہ،'], 'ps':['د تړون واټن،','د تړون زاویه،']}[lang]
    parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320" role="img" aria-label="Figure 13.3 Structure of CCl4"><defs><radialGradient id="cl20"><stop offset="0" stop-color="#dcfce7"/><stop offset="1" stop-color="#4d8573"/></radialGradient><radialGradient id="c20"><stop offset="0" stop-color="#e5d5df"/><stop offset="1" stop-color="#62515d"/></radialGradient></defs><rect width="600" height="320" fill="white"/>']
    def text(x,y,t):parts.append(f'<text x="{x}" y="{y}" font-size="16" text-anchor="middle" fill="#111">{html.escape(t)}</text>')
    # Ball-and-stick and space-filling depictions preserve the two source models.
    for cx,cy,scale,solid in [(170,145,1,False),(445,151,1.08,True)]:
        ends=[(cx,cy-77),(cx-76,cy+40),(cx+50,cy+3),(cx+35,cy+81)]
        if not solid:
            for x,y in ends:parts.append(f'<path d="M{cx} {cy}L{x} {y}" stroke="#333" stroke-width="9"/><path d="M{cx} {cy}L{x} {y}" stroke="#ddd" stroke-width="4"/>')
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{27 if solid else 20}" fill="#9a8793" stroke="#444"/>')
        for x,y in ends:parts.append(f'<circle cx="{x}" cy="{y}" r="{43 if solid else 25}" fill="#86b69e" stroke="#334155"/>')
        text(cx-32,cy-12,'C');text(cx-40,cy-90,'Cl')
    parts.append('<path d="M161 172Q135 212 104 190" fill="none" stroke="#111"/>')
    text(250,78,lab[0]);text(250,101,'1.78 A°');text(127,267,lab[1]);text(127,290,'109.5°')
    parts.append('</svg>');return ''.join(parts)
def block(identity,kind):
    make=(lambda lang:orbitals(lang,kind=='excited')) if kind!='ccl4' else tetrachloride
    return {'id':identity,'svg':make('en'),'svgUrdu':make('ur'),'svgPashto':make('ps')}
