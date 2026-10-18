"""Answer page 327; original inverse labels and signs retained."""
import math
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import note
from math12_native_geometry import geometry,path

def exponential_graph(label,title,rate,bounds,coordinates):
 xmin,xmax,ymin,ymax=bounds
 def pt(x,y):return(55+400*(x-xmin)/(xmax-xmin),280-240*(y-ymin)/(ymax-ymin))
 paths=[];labels=[(270,20,title)]
 for x in range(int(xmin),int(xmax)+1,10 if xmax==100 else 1):
  paths.append(path([pt(x,ymin),pt(x,ymax)],stroke='#dce3eb'))
 for y in range(int(ymin),int(ymax)+1,25 if ymax==150 else 1):
  paths.append(path([pt(xmin,y),pt(xmax,y)],stroke='#dce3eb'))
 paths.extend([path([pt(xmin,0),pt(xmax,0)]),path([pt(0,ymin),pt(0,ymax)])])
 curve=[]
 for i in range(1601):
  x=xmin+(xmax-xmin)*i/1600;y=math.exp(rate*x)
  if ymin<=y<=ymax:curve.append(pt(x,y))
  elif curve:paths.append(path(curve,stroke='#9b273d'));curve=[]
 if curve:paths.append(path(curve,stroke='#9b273d'))
 for j,(x,y,text) in enumerate(coordinates):
  px,py=pt(x,y);paths.append(path([(px-2,py),(px+2,py)],stroke='#111827'))
  # Source labels crowded near the axis; offsets preserve every coordinate legibly.
  lx=70+(j%3)*132;ly=325+(j//3)*24
  paths.append(path([(px,py),(lx,ly-10)],stroke='#b8c2cd'));labels.append((lx,ly,text))
 for x in [xmin,0,xmax]:labels.append((*pt(x,0),str(x)))
 for y in [ymin,ymax]:labels.append((pt(0,y)[0]-24,pt(0,y)[1],str(y)))
 return geometry('Printed answer 2.2, Q3 ('+label+')',title,paths,labels,size=(500,395))

EX21=[heading('3.'),paragraph('(a) f[g(x)] = 4x² + 1, g[f(x)] = 2x² + 2.'),paragraph('(b) f[g(x)] = sin(1 − x²), g[f(x)] = 1 − sin²x = cos²x.'),paragraph('(c) f[g(x)] = x, g[f(x)] = x.'),paragraph('(d) f[g(x)] = Sin(2x + 3), g[f(x)] = 2Sinx + 3.'),heading('4.'),paragraph('(a) h⁻¹(x) = f⁻¹(g(x)) = x − 1; k⁻¹(x) = g⁻¹f(x) = x − 1.'),paragraph('(b) h⁻¹(x) = f⁻¹(g(x)) = (x − 7)/4; k⁻¹(x) = g⁻¹(f(x)) = (x − 14)/4.'),paragraph('(c) h⁻¹(x) = f⁻¹[g(x)] = x + 3; k⁻¹(x) = g⁻¹[f(x)] = (2x − 3)/2.'),paragraph('(d) h⁻¹(x) = f⁻¹[g(x)] = x self-inverse; k⁻¹(x) = g⁻¹[f(x)] = x self-inverse.'),note('SpaceBook clarification: the key’s composition labels omit the inverse on the inner function. The inverse of f∘g is g⁻¹∘f⁻¹. In 4(c), the second numerical result also has the wrong sign: the checked inverse is (2x + 3)/2. The cancelled identities in 3(c) retain the original excluded inputs, as explained in the learning solution.')]
EX22=[heading('Exercise 2.2'),heading('1.'),paragraph('(a) Trigonometric; (b) Algebraic; (c) Inverse trigonometric; (d) Logarithmic; (e) Implicit; (f) Hyperbolic; (g) Explicit.'),heading('2.'),paragraph('(a) 1 in gram 100; (b) 0.7089 in gram 70.9g; (c) 0.5025 in gram 50.3g; (d) 0.11648 in gram 11.6g.'),paragraph('(e) The amount of radium in the box decreases with the passage of time.'),heading('3.'),
 exponential_graph('a','h(x) = 2ˣ',math.log(2),(-10,10,-5,12),[(0,1,'(0,1)'),(-1,.5,'(−1,0.5)'),(-2,.25,'(−2,0.25)'),(-3,.125,'(−3,0.125)'),(-4,.063,'(−4,0.063)'),(-5,.031,'(−5,0.031)')]),
 exponential_graph('b','m(x) = 3⁻ˣ',-math.log(3),(-10,10,-5,12),[(0,1,'(0,1)'),(1,.33,'(1,0.33)'),(2,.11,'(2,0.11)'),(3,.037,'(3,0.037)')]),
 exponential_graph('c','N = eᵗ',1,(-100,100,-25,175),[(0,1,'(0,1)'),(1,2.7,'(1,2.7)'),(2,7.4,'(2,7.4)'),(3,20.09,'(3,20.09)'),(4,54.6,'(4,54.6)'),(5,148.4,'(5,148.4)')]),
 exponential_graph('d','N = e⁻ᵗ',-1,(-10,10,-5,12),[(0,1,'(0,1)'),(1,.37,'(1,0.37)'),(2,.14,'(2,0.14)'),(3,.05,'(3,0.05)'),(4,.02,'(4,0.02)'),(5,.007,'(5,0.007)')])]
PAGES=[page('168_page_1.jpg',327,[heading('Answers'),*EX21,*EX22])]
PAGES[0].update(title='Answers — Exercises 2.1 and 2.2',visualStatus='Four exponential graphs reconstructed with source coordinate labels and separate leader lines for readability',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':168,'side':'left'},sourceNotes=['Inverse composition notation and Q4(c) numerical sign retained exactly with separate clarification.'])
