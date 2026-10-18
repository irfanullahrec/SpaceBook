"""Printed answer page 326, visually checked on full PDF physical 167."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import note
from math12_native_geometry import geometry,path

def modulus_graph(label,a,b,c,bounds,xticks,yticks):
 xmin,xmax,ymin,ymax=bounds
 def pt(x,y):return(55+400*(x-xmin)/(xmax-xmin),280-240*(y-ymin)/(ymax-ymin))
 paths=[path([pt(xmin,0),pt(xmax,0)]),path([pt(0,ymin),pt(0,ymax)])]
 labels=[(465,pt(0,0)[1],'x'),(pt(0,0)[0],25,'y')]
 for x in xticks:
  px,py=pt(x,0);paths.append(path([(px,py-3),(px,py+3)]));labels.append((px,py+17,str(x)))
 for y in yticks:
  px,py=pt(0,y);paths.append(path([(px-3,py),(px+3,py)]));labels.append((px-22,py,str(y)))
 segment=[]
 for i in range(801):
  x=xmin+(xmax-xmin)*i/800;y=abs(a*x+b)+c
  if ymin<=y<=ymax:segment.append(pt(x,y))
  elif segment:paths.append(path(segment,stroke='#175fa3'));segment=[]
 if segment:paths.append(path(segment,stroke='#175fa3'))
 return geometry('Printed answer 2.1, Q2 ('+label+')','Answer-key modulus graph ('+label+')',paths,labels)

BLOCKS=[heading('Answers'),heading('Unit 2'),heading('Exercise 2.1'),heading('1.'),
 paragraph('(a) Domain: (−∞, ∞) or −∞ < x < ∞; Range: (−∞, 5).'),
 paragraph('(b) Domain: (−∞, ∞) or −∞ < x < ∞; Range: (−∞, ∞).'),
 paragraph('(c) Domain: (−∞, −2) ∪ (−2, ∞); Range: (−∞, 0) ∪ (0, ∞).'),
 paragraph('(d) Domain: (−∞, ∞) or −∞ < x < ∞; Range: (−∞, ∞).'),
 paragraph('(e) Domain: (−∞, ∞) or −∞ < x < ∞; Range: [0, ∞).'),
 paragraph('(f) Domain: (−∞, ∞) or −∞ < x < ∞; Range: [0, ∞).'),heading('2.'),
 modulus_graph('a',2,-6,0,(0,6,0,7),range(7),range(1,7)),
 modulus_graph('b',4,-12,3,(0,6,0,16),range(7),range(4,16,2)),
 modulus_graph('c',15,35,-2,(-10,6,-5,125),range(-10,7,2),range(20,121,20)),
 modulus_graph('d',8,6,1,(-10,10,0,85),range(-10,11,2),range(10,81,10)),
 note('SpaceBook clarification: the printed range in 1(a) excludes the attained maximum 5. The learning solution uses (−∞, 5]. These native graphs reproduce the functions and source axis scales; slight margins expose the vertices without clipping them.')]
PAGES=[page('167_page_2.jpg',326,BLOCKS)]
PAGES[0].update(title='Answers — Unit 2, Exercise 2.1',visualStatus='Four printed modulus graphs reconstructed as native labelled SVG; source ranges retained digitally',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':167,'side':'right'},sourceNotes=['Printed range (−∞, 5) retained with separate correction.'])
