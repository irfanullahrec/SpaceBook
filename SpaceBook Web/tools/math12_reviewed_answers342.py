"""Printed answer 342: all five conic diagrams reconstructed natively."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_answers333 import groups
from math12_native_geometry import geometry,path

def parabola(label):
 if label=='a':
  def pt(x,y):return(250+100*x,240-110*y)
  curve=[pt(x,x*x/2) for x in [i/100 for i in range(-155,156)]]
  paths=[path(curve),path([pt(-1.7,0),pt(1.7,0)]),path([pt(0,-.7),pt(0,1.5)]),path([pt(-1,.5),pt(1,.5)]),path([pt(-1.7,-.5),pt(1.7,-.5)],stroke='#c9a227')]
  labels=[(55,174,'A(−1,1/2)'),(352,174,'B(1,1/2)'),(260,160,'F(0,1/2)'),(255,262,'V(0,0)'),(240,64,'x=0'),(410,312,'y=1/2'),(430,250,'x')]
  dots=[pt(0,0),pt(0,.5),pt(-1,.5),pt(1,.5)]
 elif label=='b':
  def pt(x,y):return(390+110*x,180-70*y)
  curve=[pt(-1-y*y/3,y) for y in [i/100 for i in range(-195,196)]]
  paths=[path(curve),path([pt(-3.3,0),pt(.5,0)]),path([pt(0,-2),pt(0,2)]),path([pt(-1.75,-1.5),pt(-1.75,1.5)]),path([pt(-.25,-2),pt(-.25,2)],stroke='#c9a227')]
  labels=[(135,60,'A(−7/4,+3/2)'),(130,307,'B(−7/4,−3/2)'),(85,164,'F(−7/4,0)'),(280,162,'V(−1,0)'),(395,33,'y'),(450,192,'x')]
  dots=[pt(-1,0),pt(-1.75,0),pt(-1.75,-1.5),pt(-1.75,1.5)]
 else:
  def pt(x,y):return(165+160*x,375-85*y)
  curve=[pt((y-3)**2,y) for y in [i/100 for i in range(180,421)]]
  paths=[path(curve),path([pt(-.4,0),pt(1.8,0)]),path([pt(0,0),pt(0,4.3)]),path([pt(-.35,3),pt(1.7,3)]),path([pt(.25,2.5),pt(.25,3.5)]),path([pt(-.25,0),pt(-.25,4.3)],stroke='#c9a227')]
  labels=[(30,119,'V(0,3)'),(208,62,'B(1/4,7/2)'),(210,180,'A(1/4,5/2)'),(214,111,'F(1/4,3)'),(430,123,'y=3'),(157,12,'y')]
  dots=[pt(0,3),pt(.25,3),pt(.25,2.5),pt(.25,3.5)]
 return geometry('Printed answer 9.1, Q1 ('+label+')','Source parabola key ('+label+')',paths,labels,dots,size=(500,400))

EX91=[heading('1. (b)'),paragraph('Vertex (−1,0), focus (−7/4,0), ends of latus rectum A(−7/4,+3/2), B(−7/4,−3/2), axis of symmetry: y = 0.'),heading('1. (c)'),paragraph('Vertex (0,3), focus (1/4,3), ends of latus rectum A(1/4,5/2), B(1/4,7/2), axis of symmetry: y = 3.'),*[parabola(label) for label in 'abc'],note('Source-figure note: graph (a) labels its lower directrix y=1/2, despite placing it below the x-axis. The correct directrix is y=−1/2; the printed label is preserved on the native source diagram.'),*groups([
 (2,[('a',r'(x-2)^2=8(y+1)'),('b',r'y^2=24x')]),
 (3,[('a',r'x^2=12y'),('b',r'y^2=16x'),('c',r'y^2=12x'),('d',r'x^2=-48y'),('e',r'(x-5)^2=\frac{64}{3}(y-1)'),('f',r'(y+7)^2=64(x-3)')]),
 (4,[('',r'3x+y+5=0')]),
 (5,[('',r'(y+2)^2=6(x-\frac52)')]),
 (7,[('a',r'c=\frac94'),('b',r'c=-\frac16')]),
 (8,[('a',r'\text{tangent: }x-y+3=0\quad\text{normal: }x+y-9=0'),('b',r'\text{tangent: }4x+3y-1=0\quad\text{normal: }8x+9y-1=0')]),
 (9,[('a',r'4x+4y+1=0'),('b',r'y=\sqrt3x+\frac1{4\sqrt3}')]),
 (10,[('',r'x^2=-12(y+3)')])])]
i=next(i for i,b in enumerate(EX91) if b.get('text')=='7.')
EX91[i:i]=[heading('6.'),paragraph('(a) P₁(1,3) and P₂(4,6).'),paragraph('(b) x = 1 ± √3i which is imaginary so the line does not intersect the parabola.')]
EX91.extend([note('SpaceBook clarification: 2(b) uses the plotted points rather than the conflicting directrix. Question 4 requires 3x+y−5=0. Question 5 permits two opening directions. The printed intersections in 6(a), normal in 8(b), tangent in 9(b) and arch coefficient in 10 disagree with the source givens; their checked solutions remain separately available. The arch is x²=−6(y+3) on −6≤x≤6.')])

def ellipse(label,a,b,points):
 return {'type':'diagram','caption':'Printed answer 9.2, Q1 ('+label+')','diagram':{'type':'source-function-graph','title':'Source ellipse key ('+label+')','equalAspect':True,'xMin':-max(a,b)-1,'xMax':max(a,b)+1,'yMin':-max(a,b)-1,'yMax':max(a,b)+1,'xTicks':[-a,0,a],'yTicks':[-b,0,b],'ellipse':{'a':a,'b':b},'points':points}}
EX92=[heading('Exercise 9.2'),heading('1. (a)'),ellipse('a',3,2,[[-3,0,'V′(−3,0)'],[3,0,'V(3,0)'],[0,2,'B(0,2)'],[0,-2,'B′(0,−2)'],[-5**.5,0,'F′(−√5,0)'],[5**.5,0,'F(√5,0)']]),paragraph('Centre C(0,0); Foci F(±√5,0); End points of major axis A(±3,0); End points of minor axis B(0,±2).'),heading('1. (b)'),ellipse('b',4,5,[[0,5,'A₁(0,5)'],[0,-5,'A₂(0,−5)'],[-4,0,'B₁(−4,0)'],[4,0,'B₂(4,0)'],[0,3,'F(0,3)'],[0,-3,'F′(0,−3)']]),paragraph('Centre C(0,0); Foci F(0,±3); End points of major axis A(0,±5); End points of minor axis B(±4,0).')]
PAGES=[page('175_page_2.jpg',342,[heading('Answers'),*EX91,*EX92])]
PAGES[0].update(title='Answers — Parabolas and ellipse opening',visualStatus='Three parabola and two ellipse diagrams reconstructed as labelled native SVG; all printed results and source errors kept separate from learning solutions',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':175,'side':'right'})
