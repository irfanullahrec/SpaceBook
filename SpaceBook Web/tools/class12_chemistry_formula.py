"""Shared helpers for typeset formula rows (fractions) in Chemistry XII coded SVGs."""
def frac(F,x,y,n,d,size=14):
    w=max(len(n),len(d))*size*0.52
    return F.t(x,y-8,n,size)+F.line(x-w/2,y,x+w/2,y,1.2)+F.t(x,y+18,d,size)
def formula_rows(F,rows,h=60,x0=230):
    """rows: list of (lhs, parts); part = ('t', text, '') or ('f', numerator, denominator). Returns svg string."""
    s=F.start(h*len(rows)+10)
    for i,(lhs,parts) in enumerate(rows):
        y=34+h*i;x=x0;s+=F.t(x-50,y+5,lhs,15)
        for kind,a,b in parts:
            if kind=='t':
                w=len(a)*8+10;s+=F.t(x+w/2,y+5,a,14);x+=w
            else:
                w=max(len(a),len(b))*7.3+20;s+=frac(F,x+w/2,y,a,b);x+=w
    return s+'</svg>'
