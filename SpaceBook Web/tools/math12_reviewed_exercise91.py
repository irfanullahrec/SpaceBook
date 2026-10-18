"""Printed 251–252: all ten exercise groups, three figures and summary."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import note
from math12_native_geometry import geometry,path
QUESTIONS=[
 'In each case, sketch the parabola, indicate vertex, focus, latus-rectum endpoints and axis: (a) x²=2y; (b) y²=−3(x+1); (c) (y−3)²=x.',
 'Determine the equation of each graphed parabola: (a) V(2,−1), F(2,1), plotted (−2,1),(6,1), printed directrix x=2; (b) V(0,0), printed directrix x=−2, plotted (6,12),(6,−12).',
 'Write the equation from: (a) F(0,3), directrix y=−3; (b) F(4,0), directrix x=−4; (c) V(0,0), x-axis symmetry, through (3,6); (d) V(0,0), y-axis symmetry, through (−12,−3); (e) vertical symmetry, through (−3,4), V(5,1); (f) horizontal symmetry, through (7,9), V(3,−7).',
 'Find the equation of the set of all points with distances from (4,3) that equal their distances from (−2,1).',
 'Find an equation for a parabola with focal chord length 6, focus (4,−2) and directrix parallel to the y-axis.',
 'Find intersections of line and parabola: (a) y²+3x=−8, x−y+2=0; (b) x²=2y, x−y−2=0.',
 'Find c so (a) x−y+c=0 touches y²=9x; (b) x−y+c=0 touches x²=(2/3)y.',
 'Find tangent and normal: (a) at (3,6) to y²=12x; (b) at (1/2,−1/3) to x²=−3y/4.',
 'Find a tangent (a) to y²=x making an angle 135° with the x-axis; (b) to x²=y making an angle 60° with the x-axis.',
 'Find the equation of the parabolic portion of the archway shown: top of arch is 3 ft below x-axis, parabolic rise is 6 ft, vertical portion below is 18 ft; opening width 12 ft and side widths 3 ft each.'
]
STEPS=[
 ['Use (x−h)²=4p(y−k) for a vertical axis and (y−k)²=4p(x−h) for a horizontal axis.','(a) h=k=0, 4p=2, p=1/2: upward; V(0,0), F(0,1/2), directrix y=−1/2, axis x=0. Latus endpoints (±1,1/2), length 2.','(b) h=−1,k=0,4p=−3,p=−3/4: left; V(−1,0), F(−7/4,0), directrix x=−1/4, axis y=0.','Its latus endpoints are (−7/4,±3/2), length 3.','(c) h=0,k=3,4p=1,p=1/4: right; V(0,3), F(1/4,3), directrix x=−1/4, axis y=3.','Its latus endpoints are (1/4,5/2),(1/4,7/2), length 1. Sketch each smooth symmetric curve through the vertex and these endpoints.'],
 ['(a) The printed vertex (2,−1) and focus (2,1) give a vertical axis, p=2.','Therefore (x−2)²=8(y+1). Both plotted (−2,1),(6,1) satisfy 16=8·2.','The corresponding directrix must be y=−3. The source line x=2 passes through the vertex and focus, so it is the axis, not a valid directrix.','(b) Vertex (0,0) and directrix x=−2 give p=2, focus (2,0) and y²=8x.','However (6,±12) do not satisfy this equation: 144≠48. At x=6 the correct y values are ±4√3.','If instead the vertex and plotted (6,±12) are retained, 144=4p·6 gives p=6, equation y²=24x and directrix x=−6. The printed labels cannot all hold simultaneously.'],
 ['(a) Vertex midway between F(0,3) and y=−3 is (0,0), p=3: x²=12y.','(b) Vertex midway between F(4,0) and x=−4 is (0,0), p=4: y²=16x.','(c) Horizontal axis: y²=4px. At (3,6), 36=12p, giving p=3 and y²=12x.','(d) Vertical axis: x²=4py. At (−12,−3), 144=−12p gives p=−12 and x²=−48y.','(e) Write (x−5)²=4p(y−1). At (−3,4), 64=12p, giving p=16/3 and (x−5)²=(64/3)(y−1).','(f) Write (y+7)²=4p(x−3). At (7,9), 256=16p, giving p=16 and (y+7)²=64(x−3).','Substitute each stated point and check the focus/directrix midpoint in (a),(b); all six conditions hold.'],
 ['For a variable point (x,y), equate distances to the two fixed points.','Both distances are nonnegative, so square without changing the locus: (x−4)²+(y−3)²=(x+2)²+(y−1)².','Expand and cancel x²+y²: −8x−6y+25=4x−2y+5.','Thus −12x−4y+20=0, or 3x+y−5=0.','The fixed-point midpoint (1,2) lies on this line; the connecting vector is (6,2), whose slope is 1/3, while the locus slope is −3.','Hence the locus is their perpendicular bisector, a line. A parabola would require one fixed point and a fixed directrix line.'],
 ['Interpret “focal chord” here as latus rectum, as the exercise wording in this unit does.','The length is 4|p|=6, so p=±3/2. The directrix is vertical, giving a horizontal axis.','The focus equals (h+p,k)=(4,−2), hence k=−2 and h=4−p.','If p=3/2, h=5/2: (y+2)²=6(x−5/2), directrix x=1, opening right.','If p=−3/2, h=11/2: (y+2)²=−6(x−11/2), directrix x=7, opening left.','Both have focus (4,−2) and latus endpoints (4,1),(4,−5), length 6. No opening direction was specified, so both are valid. An arbitrary focal chord length alone would not determine |p|.'],
 ['(a) x−y+2=0 gives x=y−2.','Substitute in y²+3x=−8: y²+3y−6=−8, hence y²+3y+2=(y+1)(y+2)=0.','Thus y=−1 gives x=−3 and y=−2 gives x=−4. Both points satisfy both original equations.','(b) x−y−2=0 gives y=x−2.','Substitute in x²=2y: x²−2x+4=0, with discriminant 4−16=−12.','There are no real intersections. The complex solutions are x=1±i√3, y=−1±i√3.'],
 ['Both lines have slope m=1 because y=x+c.','(a) y²=9x has p=9/4. The slope-form tangent condition is c=p/m=9/4.','Tangent: y=x+9/4. Its contact is (p/m²,2p/m)=(9/4,9/2).','(b) x²=(2/3)y has p=1/6. The condition is c=−pm²=−1/6.','Tangent: y=x−1/6. Its contact is (2pm,pm²)=(1/3,1/6).','Substituting each line in its parabola produces a repeated quadratic root at the stated contact.'],
 ['(a) Check 6²=12·3; p=3. The tangent point form gives 6y=6(x+3), or x−y+3=0.','The tangent slope is 2p/y₁=1, so normal slope is −1. Through (3,6): y−6=−(x−3), or x+y−9=0.','(b) Check (1/2)²=−3(−1/3)/4=1/4; 4p=−3/4, p=−3/16.','Use xx₁=2p(y+y₁): x/2=−3(y−1/3)/8, giving 4x+3y−1=0.','The tangent slope is x₁/(2p)=−4/3, so normal slope is 3/4.','Use y+1/3=(3/4)(x−1/2), giving 18x−24y−17=0. Both lines contain the contact, with slope product −1.'],
 ['(a) The inclination 135° gives m=tan135°=−1.','Compare y²=x with y²=4px: p=1/4.','Use y=mx+p/m to obtain y=−x−1/4, contact (1/4,−1/2).','(b) Inclination 60° gives m=√3.','Compare x²=y with x²=4py: p=1/4. Use y=mx−pm² to obtain y=√3x−3/4.','The contact is (2pm,pm²)=(√3/2,3/4), and differentiation gives its slope 2x=√3.'],
 ['Use the displayed axes, with the y-axis along the centre of the arch and x-axis at the top of the outer wall.','The parabolic vertex is V=(0,−3). The parabolic portion drops 6 ft to the spring points, so these have y=−9.','The opening is 12 ft wide, so the spring points are (−6,−9),(6,−9).','Write x²=4p(y+3). At (6,−9), 36=4p(−6), giving p=−3/2.','Thus x²=−6(y+3), or y=−3−x²/6, for −6≤x≤6.','At x=±6 the height is −9 and at x=0 it is −3. The remaining 18-ft straight portions and 3-ft side widths describe the wall, without altering this parabolic portion.']
]
ANSWERS=['(a) V(0,0), F(0,1/2), endpoints (±1,1/2); (b) V(−1,0), F(−7/4,0), endpoints (−7/4,±3/2); (c) V(0,3), F(1/4,3), endpoints (1/4,3±1/2).','(a) (x−2)²=8(y+1); printed directrix inconsistent. (b) y²=8x from directrix, or y²=24x from plotted points; source inconsistent.','(a) x²=12y; (b) y²=16x; (c) y²=12x; (d) x²=−48y; (e) (x−5)²=(64/3)(y−1); (f) (y+7)²=64(x−3).','3x+y−5=0, a perpendicular-bisector line.','(y+2)²=6(x−5/2) or (y+2)²=−6(x−11/2).','(a) (−3,−1),(−4,−2); (b) no real intersections.','(a) c=9/4; (b) c=−1/6.','(a) tangent x−y+3=0, normal x+y−9=0; (b) tangent 4x+3y−1=0, normal 18x−24y−17=0.','(a) y=−x−1/4; (b) y=√3x−3/4.','x²=−6(y+3), −6≤x≤6.']

def question_graph(n):
 if n==1:
  def pt(x,y):return(180+28*x,220-35*y)
  coords=[(x,(x-2)**2/8-1) for x in [i/20 for i in range(-60,141)]]
  paths=[path([pt(x,y) for x,y in coords]),path([pt(-5,0),pt(8,0)]),path([pt(0,-2.5),pt(0,5)]),path([pt(2,-2.5),pt(2,5)],stroke='#dc2626')]
  labels=[(225,170,'F(2,1)'),(170,283,'V(2,−1)'),(238,67,'Printed x=2'),(60,193,'(−2,1)'),(335,190,'(6,1)'),(410,228,'x'),(176,35,'y')];dots=[(2,1),(2,-1),(-2,1),(6,1)]
 else:
  def pt(x,y):return(165+21*x,185-8*y)
  coords=[(y*y/24,y) for y in range(-16,17)]
  paths=[path([pt(x,y) for x,y in coords]),path([pt(-6,0),pt(13,0)]),path([pt(0,-20),pt(0,20)]),path([pt(-2,-20),pt(-2,20)],stroke='#dc2626',dash=True),path([pt(6,-12),pt(6,12)],dash=True)]
  labels=[(118,40,'Printed x=−2'),(297,82,'(6,12)'),(297,303,'(6,−12)'),(298,209,'(6,0)'),(168,181,'V(0,0)'),(442,190,'x'),(165,19,'y')];dots=[(0,0),(6,12),(6,-12),(6,0)]
 return geometry('Exercise 9.1 Q2('+('a' if n==1 else 'b')+')','Source graph and original conflicting labels for Exercise 9.1 Question 2',paths,labels,points=[{'x':pt(x,y)[0],'y':pt(x,y)[1]} for x,y in dots],size=(480,360))
def arch():
 def pt(x,y):return(240+18*x,50-11*y)
 curve=[pt(x,-3-x*x/6) for x in [i/20 for i in range(-120,121)]]
 polygon=[pt(-9,0),pt(9,0),pt(9,-27),pt(6,-27),pt(6,-9)]+list(reversed(curve))+[pt(-6,-27),pt(-9,-27),pt(-9,0)]
 paths=[path(polygon,fill='#bbf7d0'),path([pt(-10,0),pt(11,0)]),path([pt(0,2),pt(0,-5)]),path([pt(10,0),pt(10,-27)])]
 labels=[(240,25,'y'),(445,52,'x'),(425,74,'3 ft'),(425,118,'6 ft'),(425,248,'18 ft'),(183,383,'12 ft'),(70,383,'3 ft'),(365,383,'3 ft')]
 for y in [0,-3,-9,-27]:paths.append(path([pt(9.6,y),pt(10.4,y)]))
 return geometry('Exercise 9.1 Q10','Source archway: 3-foot top offset, 6-foot parabolic rise, 18-foot legs, 12-foot opening and 3-foot side walls',paths,labels,size=(510,410))
SUMMARY={'type':'dataTable','headers':['Element','y²=4ax','y²=−4ax','x²=4ay','x²=−4ay'],'rows':[['Focus','(a,0)','(−a,0)','(0,a)','(0,−a)'],['Directrix','x=−a','x=a','y=−a','y=a'],['Vertex','(0,0)','(0,0)','(0,0)','(0,0)'],['Axis','y=0','y=0','x=0','x=0'],['Latus Rectum','x=a','x=−a','y=a','y=−a'],['Graph','opens right','opens left','opens up','opens down']]}
def summary_graphs():
 out=[]
 for i in range(4):
  def pt(x,y):return(180+48*x,170-48*y)
  vertical=i>=2;sign=1 if i%2==0 else -1
  coords=[(t,sign*t*t/4) if vertical else (sign*t*t/4,t) for t in [j/20 for j in range(-55,56)]]
  direct=[(-2.6,-sign),(2.6,-sign)] if vertical else [(-sign,-2.6),(-sign,2.6)];focus=(0,sign) if vertical else (sign,0)
  out.append(geometry('Summary graph '+str(i+1),'Standard parabola — '+['right','left','up','down'][i]+' opening, focus and directrix', [path([pt(x,y) for x,y in coords]),path([pt(-3,0),pt(3,0)]),path([pt(0,-3),pt(0,3)]),path([pt(x,y) for x,y in direct])],[(180,191,'O'),(pt(*focus)[0]+5,pt(*focus)[1]-8,'F'),(326,180,'x'),(180,22,'y')],points=[{'x':pt(*focus)[0],'y':pt(*focus)[1]}],size=(370,340)))
 return out
PAGES=[page('130_page_1.jpg',251,[heading('Exercise 9.1')]+[paragraph(str(i+1)+'. '+q) for i,q in enumerate(QUESTIONS[:8])]+[question_graph(1),question_graph(2),note('Question 2(a) labels x=2 as directrix although it passes through the vertex and focus; vertex/focus/curve instead require y=−3. Question 2(b) directrix x=−2 and plotted (6,±12) are inconsistent. Their alternative equations are kept separate. Question 4 specifies two fixed points and therefore has a straight-line locus, not a parabola. Question 5 does not specify opening direction and uses focal chord to mean latus rectum.')]),page('130_page_2.jpg',252,[paragraph('9. '+QUESTIONS[8]),paragraph('10. '+QUESTIONS[9]),arch(),heading('Summary of Standard Parabola'),SUMMARY]+summary_graphs()+[note('The table uses a>0; its latus-rectum entries are the lines containing those chords, not their lengths. Each length is 4a, and the chords have endpoints (±a,±2a) for the horizontal forms or (±2a,±a) for the vertical forms with the sign chosen for the focus coordinate.')])]
for v in PAGES:v.update(title='CONICS-II',visualStatus='All ten source question groups, two conflicting-label graphs, exact archway and four summary graphs',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':130,'side':'left' if v['page']==251 else 'right','reason':'All subparts, fractions and dimensional segments visually reviewed'})

# Learning sketches requested in Question 1, drawn from its exact equations.
def answer_graphs():
 out=[]
 for n,(h,k,p,vertical) in enumerate([(0,0,.5,True),(-1,0,-.75,False),(0,3,.25,False)],1):
  def pt(x,y):return(210+48*(x-h),180-48*(y-k))
  curve=[(h+t,k+t*t/(4*p)) if vertical else (h+t*t/(4*p),k+t) for t in [i/30 for i in range(-60,61)]]
  focus=(h,k+p) if vertical else (h+p,k)
  ends=[(h-2*abs(p),k+p),(h+2*abs(p),k+p)] if vertical else [(h+p,k-2*abs(p)),(h+p,k+2*abs(p))]
  direct=[(h-3,k-p),(h+3,k-p)] if vertical else [(h-p,k-3),(h-p,k+3)]
  paths=[path([pt(x,y) for x,y in curve]),path([pt(h-3,k),pt(h+3,k)]),path([pt(h,k-3),pt(h,k+3)]),path([pt(x,y) for x,y in direct],dash=True),path([pt(x,y) for x,y in ends])]
  labels=[(218,203,f'V({h:g},{k:g})'),(40,28,QUESTIONS[0].split(': ')[1].split('; ')[n-1])]
  for x,y in [focus]+ends:xx,yy=pt(x,y);labels.append((xx+7,yy-9,f'({x:g},{y:g})'))
  out.append(geometry('Question 1 learning sketch '+str(n),'Exact learning sketch for Exercise 9.1 Question 1('+chr(96+n)+')',paths,labels,points=[{'x':pt(x,y)[0],'y':pt(x,y)[1]} for x,y in [(h,k),focus]+ends],size=(440,395)))
 return out
