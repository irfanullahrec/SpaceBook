from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
s=s.replace('M211 61V102M112 223V159','M211 61V121M112 223V159')
needle='  const wave20=['
addition=r'''  rope20.geometry.markedSegment=Array.from({length:15},(_,i)=>{
    const t=.3+i*.35/14,u=1-t;
    return [u*u*u*503+3*u*u*t*521+3*u*t*t*522+t*t*t*541,u*u*u*150+3*u*u*t*150+3*u*t*t*68+t*t*t*68];
  });
  rope20.svg=rope20.svg.replace('M513 119Q517 89 522 80',rope20.geometry.markedSegment.map(([x,y],i)=>`${i?'L':'M'}${x} ${y}`).join(' '));
'''
if 'rope20.geometry.markedSegment=' not in s:s=s.replace(needle,addition+needle)
p.write_text(s,encoding='utf-8')
