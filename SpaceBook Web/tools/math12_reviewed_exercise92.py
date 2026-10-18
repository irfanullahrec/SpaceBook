"""Printed 264: all seven exercise groups and their three source graphs."""
import math
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import note
from math12_native_geometry import geometry,path
QUESTIONS=[
 'Sketch each ellipse; indicate center, foci and major/minor-axis endpoints: (a) x²/9+y²/4=1; (b) x²/16+y²/25=1; (c) (x+1)²/16+(y−2)²/9=1.',
 'Determine the equation of each graphed ellipse: (a) C(0,0), endpoints (0,3),(6,0); (b) C(6,−2), endpoints (6,2),(6,−6),(13,−2), left endpoint labelled (−1,2); (c) C(2,0), endpoints (−1,0),(5,0),(2,5),(2,−5).',
 'Write the ellipse equation from: (a) C(−3,2), a=2,b=1, horizontal major axis; (b) vertices (4,2),(12,2), b=2; (c) a focus (−2,3), a vertex (6,3), minor-axis length 6; (d) vertices (0,8),(0,2), c=√5.',
 'Using e=c/a, determine (a) eccentricity of x²/25+y²/16=1; (b) the ellipse with vertices (−5,0),(5,0) and eccentricity 3/5; (c) eccentricity if a=4,b=2.',
 'Find c so (a) x−y+c=0 touches x²/4+y²/9=1; (b) 2x−y+c=0 touches x²/3+y²/4=1; (c) x−y+c=0 touches x²/25+y²/11=1.',
 'Find tangent and normal: (a) at (1,2) to x²/4+y²/9=1; (b) at (3,6) to x²/7+y²/4=1; (c) at (1,1) to x²/4+y²=1.',
 'Find tangents (a) to x²/4+y²/9=1 perpendicular to 9x+8y−36=0; (b) to x²/7+y²/4=1 parallel to 6x+21y−14=0.'
]
STEPS=[
 ['(a) Center (0,0), horizontal major axis, a=3,b=2,c=√(9−4)=√5.','Vertices (±3,0), minor endpoints (0,±2), foci (±√5,0); plot these and draw a smooth symmetric ellipse.','(b) Center (0,0), vertical major axis, a=5,b=4,c=√(25−16)=3.','Vertices (0,±5), minor endpoints (±4,0), foci (0,±3).','(c) Center (−1,2), horizontal major axis, a=4,b=3,c=√7.','Vertices (−5,2),(3,2), minor endpoints (−1,−1),(−1,5), foci (−1±√7,2). The native sketches plot the four extrema and exact foci for all three curves.'],
 ['(a) The center is (0,0), horizontal semiaxis 6 and vertical semiaxis 3, so x²/36+y²/9=1.','(b) Top (6,2) and bottom (6,−6) have midpoint (6,−2) and vertical semiaxis 4.','Right (13,−2) is 7 units from center, hence the left endpoint is (−1,−2), not the printed (−1,2).','Thus (x−6)²/49+(y+2)²/16=1. The source label (−1,2) does not satisfy this ellipse and conflicts with the drawn horizontal diameter.','(c) Left/right endpoints (−1,0),(5,0) give C=(2,0), horizontal semiaxis 3; vertical endpoints (2,±5) give semiaxis 5.','Therefore (x−2)²/9+y²/25=1; substitute all four stated endpoints to check it.'],
 ['(a) Use horizontal form with h=−3,k=2,a=2,b=1: (x+3)²/4+(y−2)²=1.','(b) Vertex midpoint is (8,2); a=4,b=2, so (x−8)²/16+(y−2)²/4=1.','(c) The focus and vertex share y=3, so the major axis is horizontal; b=6/2=3. Their separation is 8.','For a nondegenerate ellipse c<a and a−c≤b=3, so the separation 8 must be a+c, rather than a−c. Solve a+c=8 and (a−c)(a+c)=b²=9.','Thus a−c=9/8, a=73/16,c=55/16. The center lies left of the given right vertex: h=6−73/16=23/16,k=3.','The equation is (x−23/16)²/(73/16)²+(y−3)²/9=1. It has focus h−c=−2 and right vertex h+a=6, checking both source elements.','(d) Vertex midpoint is (0,5), vertical major axis and a=3. Given c=√5 gives b²=9−5=4, so x²/4+(y−5)²/9=1.'],
 ['(a) a=5,b=4, so c=√(25−16)=3 and e=3/5.','(b) Vertices (±5,0) give center (0,0), a=5 and horizontal major axis.','With e=3/5, c=ea=3 and b²=a²−c²=25−9=16.','Therefore x²/25+y²/16=1.','(c) a=4,b=2 gives c=√(16−4)=2√3, hence e=c/a=√3/2.','Each eccentricity lies between 0 and 1, as required for a noncircular ellipse.'],
 ['Rewrite each line as y=mx+c; use c=±√(A m²+B) when the ellipse is x²/A+y²/B=1.','(a) m=1,A=4,B=9 gives c=±√13, tangents y=x±√13.','(b) m=2,A=3,B=4 gives c=±√16=±4, tangents y=2x±4.','(c) m=1,A=25,B=11 gives c=±√36=±6, tangents y=x±6.','For each substitution the resulting quadratic has discriminant zero, so each line has one repeated contact.','The two signs describe the two parallel supporting tangents, not two contacts on the same line.'],
 ['Before applying a tangent or normal formula at a point, check that the point lies on the curve.','(a) At (1,2), x²/4+y²/9=1/4+4/9=25/36≠1. This point is inside the ellipse.','Thus no tangent or normal at (1,2) exists; also no real tangent through this interior point exists.','(b) At (3,6), x²/7+y²/4=9/7+9=72/7≠1, so the point is exterior and no tangent or normal at that point of this ellipse is defined.','(c) At (1,1), x²/4+y²=1/4+1=5/4≠1, also exterior; again no at-point tangent or normal is defined.','For an exterior point one could ask a different question about two tangents through it, but the source explicitly asks tangent/normal at the stated point. Applying the point-form tangent without a membership check would give a polar line, not the requested tangent.'],
 ['(a) The given line has slope −9/8; perpendicular tangents have slope m=8/9.','Use y=mx±√(4m²+9) to obtain y=(8/9)x±√985/9.','Equivalently 9y−8x=±√985. The slope product (8/9)(−9/8)=−1.','(b) The given line has slope −6/21=−2/7; parallel tangents have the same slope.','Use y=mx±√(7m²+4) with m=−2/7: intercepts ±√(32/7)=±4√14/7.','Thus 7y+2x=±4√14. Both lines have the requested parallel slope and satisfy the zero-discriminant tangent condition.']
]
ANSWERS=['(a) C(0,0), F(±√5,0), V(±3,0), minor ends (0,±2); (b) C(0,0), F(0,±3), V(0,±5), minor ends (±4,0); (c) C(−1,2), F(−1±√7,2), V(−5,2),(3,2), minor ends (−1,−1),(−1,5).','(a) x²/36+y²/9=1; (b) (x−6)²/49+(y+2)²/16=1 with corrected left label (−1,−2); (c) (x−2)²/9+y²/25=1.','(a) (x+3)²/4+(y−2)²=1; (b) (x−8)²/16+(y−2)²/4=1; (c) (x−23/16)²/(73/16)²+(y−3)²/9=1; (d) x²/4+(y−5)²/9=1.','(a) e=3/5; (b) x²/25+y²/16=1; (c) e=√3/2.','(a) c=±√13; (b) c=±4; (c) c=±6.','All three printed points are off their ellipses; no tangent or normal at those points is defined.','(a) 9y−8x=±√985; (b) 7y+2x=±4√14.']
def diagram(i,learning=False):
 h,k,ax,ay=([ (0,0,3,2),(0,0,4,5),(-1,2,4,3)] if learning else [(0,0,6,3),(6,-2,7,4),(2,0,3,5)])[i]
 s=min(24,135/max(ax,ay));ox=240-h*s;oy=190+k*s
 def pt(x,y):return(ox+s*x,oy-s*y)
 paths=[path([pt(h+ax*math.cos(t*math.pi/90),k+ay*math.sin(t*math.pi/90)) for t in range(181)]),path([(20,oy),(465,oy)]),path([(ox,30),(ox,355)])]
 endpoints=[(h-ax,k),(h+ax,k),(h,k-ay),(h,k+ay)];dots=[(h,k)]+endpoints;labels=[(246,213,f'C({h:g},{k:g})'),(467,oy+7,'x'),(ox,24,'y')]
 for x,y in endpoints:
  xx,yy=pt(x,y);label=f'({x:g},{y:g})'
  if not learning and i==1 and x==h-ax:label='Printed (−1,2)'
  labels.append((max(3,xx-35),yy+23 if y<=k else yy-9,label))
 if learning:
  c=math.sqrt(abs(ax*ax-ay*ay));foci=[(h-c,k),(h+c,k)] if ax>ay else [(h,k-c),(h,k+c)]
  for x,y in foci:xx,yy=pt(x,y);dots.append((x,y));labels.append((xx+5,yy-7,'F'))
 else:
  for x,y in endpoints:paths.append(path([pt(h,k),pt(x,y)]))
 return geometry('Exercise 9.2 Q'+('1 learning sketch' if learning else '2 source graph')+' ('+chr(97+i)+')','Exact '+('learning ellipse with foci' if learning else 'source ellipse with original labels')+' for Exercise 9.2 '+str(i+1),paths,labels,points=[{'x':pt(x,y)[0],'y':pt(x,y)[1]} for x,y in dots],size=(510,400))
PAGES=[page('136_page_2.jpg',264,[heading('Exercise 9.2')]+[paragraph(str(i+1)+'. '+q) for i,q in enumerate(QUESTIONS)]+[diagram(i) for i in range(3)]+[note('Question 2(b) draws the left endpoint on the horizontal line y=−2 but labels it (−1,2). The displayed source label is retained and the inconsistency is explained in its solution. All three contact points in Question 6 are off the corresponding ellipses, so the requested at-point tangent/normal equations are undefined; no invented contact coordinates replace them.')])]
PAGES[0].update(title='CONICS-II',visualStatus='All seven groups and three original-label ellipse graphs natively reconstructed',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':136,'side':'right','reason':'Every denominator, point coordinate and source graph label visually checked'})
