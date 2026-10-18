"""Printed 343: original shifted-ellipse inconsistencies and hyperbolas."""
import math
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_answers333 import groups
from math12_native_geometry import geometry,path

def ellipse_c():
 def pt(x,y):return(210+42*x,310-42*y)
 paths=[path([pt(1+4*math.cos(i*math.pi/90),2+3*math.sin(i*math.pi/90)) for i in range(181)]),path([pt(-4,0),pt(6,0)]),path([pt(0,-1.4),pt(0,6)]),path([pt(-3,2),pt(5,2)])]
 labels=[(20,219,'V′(−3,2)'),(420,219,'V(5,2)'),(208,87,'B(0,5)'),(208,371,'B′(0,−1)'),(100,198,'C(−1,2)'),(222,201,'C(0,0)'),(100,275,'F′(1−√7,2)'),(292,275,'F(1+√7,2)')]
 return geometry('Printed answer 9.2, Q1 (c)','Source shifted ellipse with conflicting labels',paths,labels,size=(530,400))

def hyperbola(label,a,b,vertical=False,h=0,k=0,point_labels=(),asym_labels=(),caption=None):
 scale=25 if vertical else 38
 def pt(x,y):return(250+scale*(x-h),250-scale*(y-k))
 paths=[path([pt(h-5,k),pt(h+5,k)]),path([pt(h,k-8),pt(h,k+8)])]
 for sign in [-1,1]:
  curve=[]
  for i in range(201):
   t=-1+2*i/200
   x=h+(b*math.sinh(t) if vertical else sign*a*math.cosh(t))
   y=k+(sign*a*math.cosh(t) if vertical else b*math.sinh(t))
   px,py=pt(x,y)
   if 15<=px<=485 and 15<=py<=485:curve.append((px,py))
  paths.append(path(curve))
  slope=a/b if vertical else b/a
  paths.append(path([pt(h-4,k-sign*4*slope),pt(h+4,k+sign*4*slope)]))
 labels=[(255,274,'C('+str(h)+','+str(k)+')')];dots=[]
 for x,y,text in point_labels:
  px,py=pt(x,y);dots.append((px,py))
  offset=(50 if text.startswith('F') else 22) if vertical else (45 if text.startswith('F') else -20)
  label_y=py-offset if vertical and y>k else py+offset
  labels.append((max(5,px-55),label_y,text))
 labels.extend(asym_labels)
 return geometry(caption or 'Printed answer 9.3, Q1 ('+label+')','Source hyperbola key ('+label+')',paths,labels,dots,size=(530,510))

EX92=[heading('1. (c)'),ellipse_c(),paragraph('Centre: The center is C(h,k) = C(−1,2).'),paragraph('Foci: F₁(−1+√7,−1,2), F₂(−1−√7,−1,2).'),paragraph('End points of major axis A(5,2), A′(−3,2).'),paragraph('End Points of minor axis B(1,5), B′(1,−1).'),note('SpaceBook clarification: the key’s ellipse drawing, center, foci and endpoint labels conflict. Its foci text even has three coordinate entries. The exercise equation instead gives center (−1,2), major endpoints (−5,2),(3,2), minor endpoints (−1,5),(−1,−1), and foci (−1±√7,2). All printed labels and triples above are preserved.'),*groups([
 (2,[('a',r'\frac{x^2}{36}+\frac{y^2}{9}=1'),('b',r'\frac{(x-6)^2}{49}+\frac{(y+2)^2}{16}=1'),('c',r'\frac{(x-2)^2}{9}+\frac{y^2}{25}=1')]),
 (3,[('a',r'\frac{(x+3)^2}{4}+\frac{(y-2)^2}{1}=1'),('b',r'\frac{(x-8)^2}{16}+\frac{(y-2)^2}{4}=1'),('c',r'\frac{(x-23/16)^2}{(73/16)^2}+\frac{(y-3)^2}{3^5}=1'),('d',r'\frac{x^2}{4}+\frac{(y-5)^2}{9}=1')]),
 (4,[('a',r'e=\frac35'),('b',r'\frac{x^2}{25}+\frac{y^2}{16}=1'),('c',r'e=\frac{\sqrt3}{2}')]),
 (5,[('a',r'c=\pm\sqrt5'),('b',r'c=\pm4'),('c',r'c=\pm6')]),
 (6,[('a',r'\text{tangent: }\frac{x}{4}+\frac{2y}{9}=1\quad\text{normal: }8x-9y+10=0'),('b',r'\text{tangent: }6x+21y-14=0\quad\text{normal: }7x-2y-9=0'),('c',r'\text{tangent: }x+4y-4=0\quad\text{normal: }4x-y-3=0')]),
 (7,[('a',r'8x-9y+30=0'),('',r'6x+21y-144=0')])]),note('SpaceBook clarification: all three exercise contacts in Question 6 are off their stated ellipses, so no tangent/normal at those points exists. The key nevertheless prints the lines above. Other denominator and graph-label discrepancies remain distinct from the checked exercise solutions.')]
EX93=[heading('Exercise 9.3'),heading('1. (a)'),hyperbola('a',2,3,point_labels=[(-2,0,'V₁(−2,0)'),(2,0,'V₂(2,0)'),(-math.sqrt(13),0,'F₁(−√13,0)'),(math.sqrt(13),0,'F₂(√13,0)')],asym_labels=[(320,68,'y=(3/2)x'),(330,440,'y=−(3/2)x')]),paragraph('Centre C(0,0); Vertices V₁(−2,0), V₂(2,0); Foci F₁(−√13,0), F₂(√13,0); Equation of asymptotes y = ±(3/2)x.'),heading('1. (b)'),hyperbola('b',5,2,vertical=True,point_labels=[(0,5,'V₂(0,5)'),(0,-5,'V₁(0,−5)'),(0,math.sqrt(29),'F₂(0,√29)'),(0,-math.sqrt(29),'F₁(0,−√29)')],asym_labels=[(345,87,'y=(5/2)x'),(330,425,'y=−(5/2)x')]),paragraph('Centre C(0,0); Vertices V₁(0,5), V₂(0,−5); Foci F₁(0,√29), F₂(0,−√29); Equation of asymptotes y = ±(5/2)x.'),note('Source-label note: in part (b), the printed diagram’s V₁/V₂ and F₁/F₂ names are reversed relative to the text below it. Both versions are retained; the coordinates themselves identify the same two vertices and foci.')]
PAGES=[page('176_page_1.jpg',343,[heading('Answers'),*EX92,*EX93])]
PAGES[0].update(title='Answers — Ellipse continuation and hyperbola opening',visualStatus='Shifted ellipse and two hyperbolas reconstructed with original labels; all source formulas and conflicting coordinates preserved',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':176,'side':'left'})
