"""Printed 277–278: all nine hyperbola exercise groups and summary."""
import math
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import note
from math12_native_geometry import geometry,path
QUESTIONS=[
 'Sketch each hyperbola; identify center, vertices, foci and asymptotes: (a) x²/4−y²/9=1; (b) y²/25−x²/4=1; (c) (x−2)²/9−(y−3)²/16=1; (d) (y+1)²/16−(x+3)²/25=1.',
 'Determine the equation of the “graphed ellipse” [source wording]: (a) V(−4,0),(4,0), asymptote y=x/2; (b) V(0,5),(0,−5), asymptote y=5x/4; (c) V(1,3),(7,3), asymptote y=x/2+1; (d) F(−5,3),(−5,−7), V(−5,3),(−5,−5).',
 'Write the hyperbola equation from: (a) foci (0,3),(0,−3), one vertex (0,−2); (b) vertices (5,0),(−5,0), one focus (−7,0); (c) transverse axis is x-axis, asymptotes y=3x,y=−3x; (d) foci (5,0),(−5,0), eccentricity 5/3; (e) vertices (3,−1),(−1,−1), asymptotes y=(9/4)x−13/4 and y=−(9/4)x+5/4.',
 'Find the locus of a moving point whose difference of distances is (a) 8 from points (−5,0),(5,0); (b) 10 from points (0,−13),(0,13).',
 'Write the hyperbola equation (a) with vertices (2,−2),(−4,−2), passing through (5,1); (b) with vertices (−3,1),(−3,3), passing through (0,4).',
 'Sketch each rectangular hyperbola and identify vertices, foci and asymptotes: (a) (x+1)²−(y−2)²=1; (b) (x−3)²/4−(y+1)²/4=1.',
 'Find intersections of line and hyperbola: (a) xy=4,y=x−3; (b) y²−x²/4=1,x+4y−4=0.',
 'Find c so (a) y=x+c touches x²/16−y²/4=1; (b) y=−x+c touches x²/16−y²/9=1.',
 'Find tangent and normal (a) at (−√13,9/2) to x²/4−y²/9=1; (b) at (16/3,5) to x²/9−y²/16=1.'
]
STEPS=[
 ['For each form identify the positive-square axis, center (h,k), positive lengths a,b and c=√(a²+b²).','(a) C(0,0), horizontal a=2,b=3,c=√13; vertices (±2,0), foci (±√13,0), asymptotes y=±3x/2.','(b) C(0,0), vertical a=5,b=2,c=√29; vertices (0,±5), foci (0,±√29), asymptotes y=±5x/2.','(c) C(2,3), horizontal a=3,b=4,c=5; vertices (−1,3),(5,3), foci (−3,3),(7,3), asymptotes y−3=±4(x−2)/3.','(d) C(−3,−1), vertical a=4,b=5,c=√41; vertices (−3,3),(−3,−5), foci (−3,−1±√41), asymptotes y+1=±4(x+3)/5.','Draw each construction rectangle, extend its diagonals, then sketch branches through the vertices approaching those asymptotes. The native learning graphs show these exact elements.'],
 ['The four figures are hyperbolas; the word ellipse in the printed question is a heading error.','(a) C=(0,0),a=4, asymptote slope b/a=1/2 gives b=2: x²/16−y²/4=1.','(b) C=(0,0),a=5, vertical slope a/b=5/4 gives b=4: y²/25−x²/16=1.','(c) Vertex midpoint is (4,3),a=3, horizontal slope b/a=1/2 gives b=3/2. Thus (x−4)²/9−(y−3)²/(9/4)=1. Its positive asymptote is y=x/2+1 as printed.','(d) The source upper focus and upper vertex are both (−5,3), impossible for a nondegenerate hyperbola because c>a. The focal midpoint is (−5,−2), while the printed vertex midpoint is (−5,−1), another contradiction.','If the focus pair and lower vertex (−5,−5) are retained, a=3,c=5,b²=16; the equation would be (y+2)²/9−(x+5)²/16=1, with corrected upper vertex (−5,1). This is a conditional repair, not a literal solution of all conflicting labels.'],
 ['(a) The foci give C=(0,0),c=3, vertical axis. Given vertex gives a=2, so b²=9−4=5 and y²/4−x²/5=1.','(b) C=(0,0),a=5,c=7, horizontal axis. Then b²=49−25=24: x²/25−y²/24=1.','(c) The asymptotes meet at (0,0), fixing center; b/a=3 fixes only a ratio, not the scale.','Thus the whole family x²/a²−y²/(9a²)=1 with a>0 satisfies the data. No unique equation can be found without a vertex, focus, point or length.','(d) C=(0,0),c=5,e=5/3 gives a=c/e=3; b²=25−9=16, so x²/9−y²/16=1.','(e) Vertex midpoint C=(1,−1), horizontal a=2, slope b/a=9/4 gives b=9/2. Both printed asymptotes pass through C.','Therefore (x−1)²/4−(y+1)²/(81/4)=1. Check the endpoints and diagonal slopes to verify the equation.'],
 ['For a hyperbola interpret the stated difference as the magnitude |d₁−d₂|=2a.','(a) Center (0,0), foci along x, c=5 and 2a=8 gives a=4.','Then b²=c²−a²=25−16=9, hence x²/16−y²/9=1.','(b) Center (0,0), foci along y, c=13 and 2a=10 gives a=5.','Then b²=169−25=144, hence y²/25−x²/144=1.','If a signed difference in the listed order was intended, retain only the corresponding branch; the absolute difference gives both branches, as a hyperbola conventionally does.'],
 ['(a) Vertex midpoint C=(−1,−2), horizontal a=3. Write (x+1)²/9−(y+2)²/b²=1.','Substitute (5,1): 36/9−9/b²=1, so b²=3.','Therefore (x+1)²/9−(y+2)²/3=1; the given point yields 4−3=1.','(b) Vertex midpoint C=(−3,2), vertical a=1. Write (y−2)²−(x+3)²/b²=1.','Substitute (0,4): 4−9/b²=1, so b²=3.','Therefore (y−2)²−(x+3)²/3=1; both source vertices and the given point satisfy it.'],
 ['A rectangular hyperbola has a=b, so its asymptotes are perpendicular lines of slopes ±1.','(a) C=(−1,2),a=b=1,c=√2: vertices (−2,2),(0,2), foci (−1±√2,2).','Asymptotes y−2=±(x+1); draw the centered square with side midpoints at the vertices and conjugate-axis endpoints.','(b) C=(3,−1),a=b=2,c=2√2: vertices (1,−1),(5,−1), foci (3±2√2,−1).','Asymptotes y+1=±(x−3); draw the corresponding construction square and branches.','Both curves are horizontal. Their vertex coordinates satisfy their equations, and each pair of asymptote slopes has product −1.'],
 ['(a) Substitute y=x−3 into xy=4: x(x−3)=4.','Thus x²−3x−4=(x−4)(x+1)=0, giving x=4 or −1.','The intersections are (4,1),(−1,−4), and both have xy=4 and y=x−3.','(b) The line gives y=1−x/4. Substitute: (1−x/4)²−x²/4=1.','Simplify to −x/2−3x²/16=0, or x(3x+8)=0.','Thus x=0 or −8/3, with y=1 or 5/3. The intersections (0,1),(−8/3,5/3) satisfy both original equations.'],
 ['For a finite-slope tangent use c²=A m²−B when x²/A−y²/B=1, with strictly positive radicand.','(a) m=1,A=16,B=4 gives c²=12, hence c=±2√3.','The tangents are y=x±2√3.','(b) m=−1,A=16,B=9 gives c²=7, hence c=±√7.','The tangents are y=−x±√7.','Both radicands are positive, so neither slope is an asymptote and each sign gives a real finite contact.'],
 ['(a) Verify the contact: 13/4−(81/4)/9=13/4−9/4=1.','Use xx₁/4−yy₁/9=1 to obtain −√13x/4−y/2=1, or √13x+2y+4=0.','The tangent slope is −√13/2; normal slope is 2/√13. Through (−√13,9/2), the normal is y−9/2=(2/√13)(x+√13).','Equivalently 4x−2√13y+13√13=0; substitute the contact and check the perpendicular slopes.','(b) At the printed (16/3,5), the curve value is 256/81 − 25/16 = 2071/1296 ≠ 1.','The stated point is off this hyperbola, so a tangent or normal at that point of the curve is undefined. A point-form substitution would give a polar line, not a tangent; no replacement coordinate is silently assumed.']
]
ANSWERS=['(a) C(0,0), V(±2,0), F(±√13,0), y=±3x/2; (b) C(0,0), V(0,±5), F(0,±√29), y=±5x/2; (c) C(2,3), V(−1,3),(5,3), F(−3,3),(7,3); (d) C(−3,−1), V(−3,3),(−3,−5), F(−3,−1±√41).','(a) x²/16−y²/4=1; (b) y²/25−x²/16=1; (c) (x−4)²/9−(y−3)²/(9/4)=1; (d) conflicting source labels; conditional repair (y+2)²/9−(x+5)²/16=1.','(a) y²/4−x²/5=1; (b) x²/25−y²/24=1; (c) family x²/a²−y²/(9a²)=1,a>0; (d) x²/9−y²/16=1; (e) (x−1)²/4−(y+1)²/(81/4)=1.','(a) x²/16−y²/9=1; (b) y²/25−x²/144=1 (absolute difference).','(a) (x+1)²/9−(y+2)²/3=1; (b) (y−2)²−(x+3)²/3=1.','(a) V(−2,2),(0,2), F(−1±√2,2), y−2=±(x+1); (b) V(1,−1),(5,−1), F(3±2√2,−1), y+1=±(x−3).','(a) (4,1),(−1,−4); (b) (0,1),(−8/3,5/3).','(a) c=±2√3; (b) c=±√7.','(a) tangent √13x+2y+4=0, normal 4x−2√13y+13√13=0; (b) off-curve source point: no at-point tangent/normal.']
def curve(h,k,a,b,vertical,title,source=False,conflict=False):
 s= min(30,92/max(a,b));c=math.sqrt(a*a+b*b)
 def pt(x,y):return(260+s*(x-h),200-s*(y-k))
 paths=[path([(20,pt(h,0)[1]),(560,pt(h,0)[1])]),path([(pt(0,k)[0],20),(pt(0,k)[0],410)])]
 for sign in [-1,1]:
  vals=[]
  for i in range(-95,96,2):t=i/100;x=sign*a*math.cosh(t);y=b*math.sinh(t);vals.append(pt(h+y,k+x) if vertical else pt(h+x,k+y))
  paths.append(path(vals))
 m=a/b if vertical else b/a;span=min(200/s,170/(s*m))
 for sign in [-1,1]:paths.append(path([pt(h-span,k-sign*m*span),pt(h+span,k+sign*m*span)],dash=True))
 labels=[(266,224,f'C({h:g},{k:g})')];dots=[(h,k)]
 for value,letter in [(a,'V'),(c,'F')]:
  if source and not conflict and letter=='F':continue
  for sign in [-1,1]:
   x,y=(h,k+sign*value) if vertical else (h+sign*value,k);dots.append((x,y));xx,yy=pt(x,y)
   if conflict:
    label=('F(−5,3)' if sign>0 else 'F(−5,−7)') if letter=='F' else ('Printed V(−5,3)' if sign>0 else 'V(−5,−5)')
   else:label=f'{letter}({x:.4g},{y:.4g})'
   labels.append((max(4,xx-60),yy-10 if y>k else yy+23,label))
 if source:labels.append((305,50,['y=x/2','y=5x/4','y=x/2+1','Conflicting upper label'][int(title[-1])-1]))
 return geometry(title,title+' — '+('original source labels' if source else 'exact learning graph')+' with asymptotes',paths,labels,points=[{'x':pt(x,y)[0],'y':pt(x,y)[1]} for x,y in dots],size=(580,430))
def source_graphs():return [curve(0,0,4,2,False,'Exercise 9.3 Q2 source graph 1',True),curve(0,0,5,4,True,'Exercise 9.3 Q2 source graph 2',True),curve(4,3,3,1.5,False,'Exercise 9.3 Q2 source graph 3',True),curve(-5,-2,3,4,True,'Exercise 9.3 Q2 source graph 4',True,True)]
def learning_graphs(q):
 vals=[(0,0,2,3,False),(0,0,5,2,True),(2,3,3,4,False),(-3,-1,4,5,True)] if q==1 else [(-1,2,1,1,False),(3,-1,2,2,False)]
 return [curve(*v,'Exercise 9.3 Q'+str(q)+' learning graph '+str(i+1)) for i,v in enumerate(vals)]
SUMMARY={'type':'dataTable','headers':['Element','x²/a²−y²/b²=1','y²/a²−x²/b²=1'],'rows':[['Relation','c²=a²+b²','c²=a²+b²'],['Focus','(±c,0)','(0,±c)'],['Directrices','x=±c/e²','y=±c/e²'],['Major axis','y=0','x=0'],['Vertices','(±a,0)','(0,±a)'],['Covertices','(0,±b)','(±b,0)'],['Centre','(0,0)','(0,0)'],['Eccentricity','e=c/a>1','e=c/a>1']]}
PAGES=[page('143_page_1.jpg',277,[heading('Exercise 9.3')]+[paragraph(str(i+1)+'. '+q) for i,q in enumerate(QUESTIONS[:6])]+source_graphs()+[note('The word ellipse in Q2 refers to its hyperbola figures. Q2(d) has an upper vertex sharing its focus coordinates and inconsistent vertex/focal midpoints; no nondegenerate hyperbola satisfies all printed labels. Its native source-associated diagram retains these labels and identifies the conditional geometry in the worked solution. Q3(c) gives only a center and asymptote ratio, so it determines a family rather than a unique hyperbola.')]),page('143_page_2.jpg',278,[paragraph(str(i+7)+'. '+q) for i,q in enumerate(QUESTIONS[6:])]+[heading('Summary of standard Hyperbolas'),SUMMARY,curve(0,0,2,1,False,'Summary horizontal hyperbola'),curve(0,0,2,1,True,'Summary vertical hyperbola'),note('For a,b>0, c=√(a²+b²)>a and e=c/a>1. Directrices are at ±a²/c along the transverse direction. “Major axis” here means transverse axis; “covertices” are conjugate-axis construction endpoints and do not belong to the hyperbola. Q9(b)’s printed contact is off its curve and has no at-point tangent or normal.')])]
for v in PAGES:v.update(title='CONICS-II',visualStatus='All nine source groups, four question graphs and complete summary with two native orientation diagrams',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':143,'side':'left' if v['page']==277 else 'right','reason':'Every source graph label, radical and fractional coefficient checked visually'})
