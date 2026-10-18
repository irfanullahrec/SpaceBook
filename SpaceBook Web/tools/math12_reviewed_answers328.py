"""Printed answer page 328: five logarithmic graphs and directed line."""
import math
from math12_reviewed_unit1 import heading,page
from math12_reviewed_higher_derivatives import note
from math12_native_geometry import geometry,path

def logarithmic_graph(label,title,a,shift,c,coords):
 def pt(x,y):return(65+15*(x+5),285-16*(y+5))
 paths=[];labels=[(250,22,title)]
 for x in range(-5,26):paths.append(path([pt(x,-5),pt(x,15)],stroke='#e0e5eb'))
 for y in range(-5,16):paths.append(path([pt(-5,y),pt(25,y)],stroke='#e0e5eb'))
 paths.extend([path([pt(-5,0),pt(25,0)]),path([pt(0,-5),pt(0,15)])])
 segment=[]
 for i in range(2401):
  x=-5+30*i/2400
  if x+shift<=0:continue
  y=a*math.log(x+shift)+c
  if -5<=y<=15:segment.append(pt(x,y))
 if segment:paths.append(path(segment,stroke='#9b273d'))
 points=[]
 for x,y,text in coords:
  px,py=pt(x,y);points.append((px,py));labels.append((px+8,py-10,text))
 for x in [-5,0,5,10,15,20,25]:labels.append((pt(x,0)[0],pt(x,0)[1]+18,str(x)))
 for y in [-5,5,10]:labels.append((pt(0,y)[0]-24,pt(0,y)[1],str(y)))
 return geometry('Printed answer 2.2, Q4 ('+label+')',title,paths,labels,points,size=(550,365))

GRAPHS=[
 logarithmic_graph('a','y = ln(x)',1,0,0,[(1,0,'(1,0)'),(6,1.8,'(6,1.8)'),(12,2.5,'(12,2.5)'),(18,2.9,'(18,2.9)')]),
 logarithmic_graph('b','u = −ln(x)',-1,0,0,[(1,0,'(1,0)'),(6,-1.8,'(6,−1.8)'),(12,-2.5,'(12,−2.5)'),(18,-2.9,'(18,−2.9)')]),
 logarithmic_graph('c','y = 2ln(x + 2)',2,2,0,[(1,2.2,'(1,2.2)'),(6,4.2,'(6,4.2)'),(12,5.3,'(12,5.3)'),(18,6.4,'(18,6.4)')]),
 logarithmic_graph('d','y = 4ln(x − 3)',4,-3,0,[(4,0,'(4,0)'),(6,4.4,'(6,4.4)'),(12,8.8,'(12,8.8)'),(18,10.8,'(10,10.8)')]),
 logarithmic_graph('e','y = 4ln(x) − 2',4,0,-2,[(1,-2,'(1,−2)'),(6,5.2,'(6,5.2)'),(12,8,'(12,8)'),(18,9.6,'(18,9.6)')])]

def directed_line():
 def pt(x,y):return(240+25*x,195-25*y)
 paths=[path([pt(-6,0),pt(6,0)]),path([pt(0,-6),pt(0,6)]),path([pt(0,6),pt(6,-6)])]
 for x in range(-6,7):paths.append(path([pt(x,-6),pt(x,6)],stroke='#e0e5eb'))
 for y in range(-6,7):paths.append(path([pt(-6,y),pt(6,y)],stroke='#e0e5eb'))
 # Source direction arrow follows decreasing x and increasing y.
 paths.extend([path([pt(0,0),pt(2,2)]),path([pt(0,0),pt(2,3)]),path([pt(2,2),pt(1.6,1.9)]),path([pt(2,2),pt(1.9,1.6)])])
 return geometry('Printed answer 2.2, Q5 (a)','Directed line y = 6 − 2x',paths,[(240,30,'y'),(400,195,'x'),(225,214,'0')],size=(500,380))
BLOCKS=[heading('Answers'),heading('4.'),*GRAPHS,note('SpaceBook clarification: all coordinate labels are retained from the key. In (c), 2ln(20)≈5.9915, so (18,6.4) is inconsistent with the function. In (d), the last plotted point is near x=18 but is labelled (10,10.8); 4ln(15)≈10.8322 whereas 4ln(7)≈7.7836. The native curve follows the stated formula, and the source’s conflicting labels remain visible. Graph margins and label spacing are expanded for readability.'),heading('5. (a)'),directed_line()]
PAGES=[page('168_page_2.jpg',328,BLOCKS)]
PAGES[0].update(title='Answers — Exercise 2.2, Q4 and Q5(a)',visualStatus='Five logarithmic graphs and directed straight line reconstructed as labelled native SVG; inconsistent source point labels retained separately from function values',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':168,'side':'right'})
