"""Printed key diagrams 329–330, checked against PDF physical 169."""
import math
from math12_reviewed_unit1 import heading,page
from math12_reviewed_higher_derivatives import note
from math12_reviewed_exercise22_remaining import graph,log_graph

def source_graph(q,label,title,**settings):
 b=graph(q,label,title,**settings)
 b['id']='math12-answer-'+str(q)+'-'+label
 b['caption']='Printed answer 2.2, Q'+str(q)+' ('+label+')'
 return b

ELLIPSE=source_graph(5,'b','Answer-key parametric ellipse: clockwise',equalAspect=True,xMin=-6,xMax=6,yMin=-6,yMax=6,xTicks=[-4,0,4],yTicks=[-3,3],ellipse={'a':4,'b':3,'clockwise':True},points=[[-4,0,'(−4,0)'],[4,0,'(4,0)'],[0,3,'(0,3)'],[0,-3,'(0,−3)'],[0,0,'(0,0)']])
EXP=[]
for label,title,initial,rate,bounds in [('a','Answer-key 6(a): e⁻²ˣ',1,-2,(-3,7)),('b','Answer-key 6(b): (2/3)e³ˣ',2/3,3,(-5,3)),('c','Answer-key 6(c): 4ˣ',1,math.log(4),(-5,3)),('d','Answer-key 6(d): 4⁻ˣ',1,-math.log(4),(-3,5))]:
 EXP.append(source_graph(6,label,title,xMin=bounds[0],xMax=bounds[1],yMin=-1,yMax=7,xTicks=list(range(bounds[0],bounds[1]+1)),yTicks=[2,4,6],exponential={'initial':initial,'rate':rate},points=[[0,initial,'']]))
LOG_E=log_graph(6,'e','Answer-key 6(e): log₂(x + 5)',shift=-5,base=2,xmin=-5.5,xmax=3,ymin=-1,ymax=4.5)
LOG_E['caption']='Printed answer 2.2, Q6 (e)'
LOG_F=log_graph(6,'f','Answer-key 6(f): single shifted branch',shift=2.5,xmin=-1,xmax=7,ymin=-4,ymax=3,inputFactor=2)
LOG_F['caption']='Printed answer 2.2, Q6 (f)'
LOG_G=log_graph(6,'g','Answer-key 6(g): two symmetric branches',base=2,xmin=-3,xmax=3,ymin=-4,ymax=3,power=2)
LOG_G['caption']='Printed answer 2.2, Q6 (g)'
CONICS=[]
for label,a,b in [('a',2,2),('b',4,4),('c',5,3),('d',6,math.sqrt(6))]:
 CONICS.append(source_graph(7,label,'Answer-key closed curve ('+label+')',equalAspect=True,xMin=-max(a,b)-1,xMax=max(a,b)+1,yMin=-max(a,b)-1,yMax=max(a,b)+1,xTicks=[-a,0,a],yTicks=[-b,b],ellipse={'a':a,'b':b},closedPoints=[[-a,0],[a,0],[0,-b],[0,b]]))
BLOCKS329=[heading('Answers'),heading('5. (b)'),ELLIPSE,heading('6. (a)–(e)'),*EXP,LOG_E]
BLOCKS330=[heading('Answers'),heading('6. (f)–(g)'),LOG_F,LOG_G,note('SpaceBook clarification: the source labels its single shifted logarithmic branch (f) and its two symmetric branches (g), opposite to the exercise’s function order. Their printed labels are preserved here. The learning graphs follow the question order. Equations used for reconstruction are identified from the exercise and curve families; these answer-key drawings print no formulas beside the curves.'),heading('7. (a)–(d)'),*CONICS,note('SpaceBook reconstruction note: the source provides closed curves and axis marks rather than new equations. Native curves use the matching exercise equations; the source’s sketch spacing is schematic. In (d), the exact vertical semiaxis is √6, not a new integer inferred from the sketch.')]
PAGES=[page('169_page_1.jpg',329,BLOCKS329),page('169_page_2.jpg',330,BLOCKS330)]
for p in PAGES:p.update(title='Answers — Exercise 2.2 graph continuation',visualStatus='Native graph reconstructions preserve printed part labels; curve equations traced to exercise with inference disclosed',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':169,'side':'left' if p['page']==329 else 'right'})
