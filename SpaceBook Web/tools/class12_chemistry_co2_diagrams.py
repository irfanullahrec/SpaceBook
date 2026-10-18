"""Source Figures13.4–13.7 as scalable code, without scanned image embeds."""
import html
def figure(number,lang):
    labels={'en':['Hybridization','Gives a linear 180° arrangement','Unhybridized p orbital','Second unhybridized p orbital','sigma bond (1 pair of electrons)','pi bond (1 pair of electrons)'],
            'ur':['ہائبرڈائزیشن','خطی 180° ترتیب بنتی ہے','غیر ہائبرڈ p آربیٹل','دوسرا غیر ہائبرڈ p آربیٹل','سگما بند (الیکٹرونوں کا 1 جوڑا)','پائی بند (الیکٹرونوں کا 1 جوڑا)'],
            'ps':['هایبرډایزېشن','خطي 180° ترتیب جوړوي','ناهایبرډ p اوربیټل','دویم ناهایبرډ p اوربیټل','سیګما تړون (د الکترونونو 1 جوړه)','پای تړون (د الکترونونو 1 جوړه)']}[lang]
    s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 340" role="img" aria-label="Figure 13.'+str(number)+'"><rect width="720" height="340" fill="white"/>']
    def text(x,y,t,size=15):s.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#111">{html.escape(t)}</text>')
    def line(x,y,x2,y2,dashed=False):s.append(f'<path d="M{x} {y}L{x2} {y2}" fill="none" stroke="#374151"'+(' stroke-dasharray="5 4"' if dashed else '')+'/>')
    def ellipse(x,y,rx,ry,color,rotation=0):s.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{color}" fill-opacity=".75" stroke="#475569" transform="rotate({rotation} {x} {y})"/>')
    def sp(x,y):
        ellipse(x-34,y,33,15,'#fbbf24');ellipse(x+34,y,33,15,'#fbbf24');text(x,y+5,'C');text(x-44,y+35,'sp');text(x+44,y+35,'sp')
    def oxygen(x,y,inward):
        ellipse(x+inward*34,y,33,15,'#84cc16');ellipse(x-inward*24,y-40,30,15,'#84cc16',55*inward);ellipse(x-inward*24,y+40,30,15,'#84cc16',-55*inward);text(x,y+5,'O');text(x+inward*34,y-20,'sp²');text(x-inward*31,y-65,'sp²');text(x-inward*31,y+74,'sp²')
    def p(x,y,offset=0):
        ellipse(x,y-40,17,37,'#a78bfa',offset);ellipse(x,y+40,17,37,'#a78bfa',offset)
    if number==4:
        # Separate s and p, two hybrid orbitals, then their linear arrangement.
        ellipse(45,155,13,13,'#c4b5fd');line(45,180,45,115);line(20,155,74,155);text(45,202,'s')
        ellipse(113,155,28,12,'#f472b6');line(113,180,113,115);line(80,155,145,155);text(113,202,'p')
        line(156,155,240,155);text(201,131,labels[0],13);text(231,162,'→')
        for x in [290,385]:
            ellipse(x,155,28,12,'#fbbf24');line(x,180,x,115);line(x-32,155,x+32,155);text(x,202,'sp')
        line(425,155,542,155);text(485,125,labels[1],12);text(532,161,'→')
        sp(625,155);text(625,245,'180°');text(653,97,'z');text(675,144,'x');text(661,118,'y')
    elif number==5:
        oxygen(230,163,1);sp(360,163);oxygen(490,163,-1)
    elif number==6:
        sp(205,170);p(205,170);ellipse(172,147,29,12,'#f472b6',35);ellipse(238,193,29,12,'#f472b6',35)
        text(190,40,labels[2]);text(200,286,labels[3]);line(205,50,205,90);line(180,263,175,220)
        oxygen(530,170,1);p(530,170);text(558,77,'p')
    else:
        oxygen(130,173,1);sp(260,173);oxygen(390,173,-1)
        for x in [130,260,390]:
            p(x,173);ellipse(x-23,190,24,15,'#7dd3fc',-30);ellipse(x+23,156,24,15,'#7dd3fc',-30)
        for a,b in [(130,260),(260,390)]:
            for dy in [-51,-43,43,51]:line(a,173+dy,b,173+dy,True)
        text(135,29,labels[4],13);line(150,38,175,173);text(340,52,labels[5],13);line(340,63,320,125)
        text(180,301,labels[5],13);line(180,285,180,222);text(260,326,'(a)')
        text(586,180,'O═C═O',25)
        for x,sign in [(527,-1),(645,1)]:
            for dx,dy in [(0,-15),(5*sign,-8),(5*sign,5),(0,12)]:
                s.append(f'<circle cx="{x+dx}" cy="{173+dy}" r="2" fill="#111"/>')
        text(586,326,'(b)')
    s.append('</svg>');return ''.join(s)
def block(number):return {'id':f'chem12-figure-13-{number}','svg':figure(number,'en'),'svgUrdu':figure(number,'ur'),'svgPashto':figure(number,'ps')}
