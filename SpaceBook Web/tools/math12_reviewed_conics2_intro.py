"""Printed 241–242, complete Conics II objectives and source introduction."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_conics_intro import ellipse
from math12_native_geometry import geometry,path
OBJECTIVES=[('9.1 Parabola',[
 'Define a parabola and its elements (i.e. focus, directrix, eccentricity, vertex, axis, focal chord and latus rectum).',
 'General form of an equation of a parabola.',
 'Standard equations of parabola, sketch their graphs and find their elements.',
 'Find the equation of a parabola with the following given elements: focus and vertex; focus and directrix; vertex and directrix.',
 'Recognize tangent and normal to a parabola.',
 'Find the condition when a line is tangent to a parabola at a point and hence write the equation of a tangent line in slope form.',
 'Find the equation of a tangent and a normal to a parabola at a point.',
 'Solve suspension and reflection problems related to parabola.']),('9.2 Ellipse',[
 'Define ellips and its elements (i.e. centre, foci, vertices, covertices, directories, major and minor axes, eccentricity, focal chord and latus rectum).',
 'Explain that circle is a special case of an ellipse.',
 'Derive the standard form of equation of an ellipse and identify its elements.',
 'Find the equation of an ellipse with the following given elements: major and minor axes; two points; foci, vertices or lengths of a latus rectum; foci, minor axes or length of a latus rectum.',
 'Convert a given equation to the standard form of equation of an ellipse, find its elements and draw the graph.',
 'Recognize tangent and normal to an ellipse.',
 'Find points of intersection of an ellipse with a line including the condition of tangency.',
 'Find the equation of a tangent in slope form.',
 'Find the equation of a tangent and a normal to an ellipse at a point.']),('9.3 Hyperbola',[
 'Define hyperbola and its elements (i.e. centre, vertices, foci, directrices, transverse and conjugate axes, eccentricity, focal chord and latus rectum).',
 'Derive the standard form of equation of a hyperbola and identify its elements.',
 'Find the equation of a hyperbola with the following given elements: transverse and conjugate axes with centre at origin; two points; eccentricity, latera recta and transverse axes; focus, eccentricity and centre; focus, centre and directrix.',
 'Convert a given equation to the standard form of equation of a hyperbola, find its elements and sketch the graph.',
 'Recognize tangent and normal to a hyperbola.',
 'Find points of intersection of a hyperbola with a line including the condition of tangency; the equation of tangent in slope form.',
 'Find the equation of a tangent and a normal to a hyperbola at a point.']),('9.4 Translation and rotation of axes',[
 'Define translation and rotation of axes and demonstrate through examples.',
 'Find the equations of transformation for translation of axes and rotation of axes.',
 'Find the transformed equation by using translation or rotation of axes.',
 'Find new origin and new axes referred to old origin and old axes.',
 'Find the angle through which the axes be rotated about the origin so that the product term xy is removed form the transformed equation.'])]
INTRO=[heading('Introduction'),paragraph('In our previous unit of this book we have learnt that a conic section (or simply a conic) is a curve obtained as the intersection of the surface of a cone with a plane. In this unit we will study in details about the three types of conic sections that are parabola, hyperbola and the ellipse. The circle is a type of ellipse and same time considered to be the fourth type of conic section. We have already discussed in details about tangent and normal in previous section.')]
def projectile():
 curve=[(65+320*t,275-4*210*t*(1-t)) for t in [i/100 for i in range(101)]]
 t=.16;x,y=65+320*t,275-4*210*t*(1-t)
 paths=[path(curve),path(ellipse(x,y,12,12),fill='white'),path([(x-5,y-4),(x+3,y-6),(x+7,y+1),(x+1,y+6),(x-6,y+2),(x-5,y-4)],fill='#334155')]
 return geometry('Figure 9.1(a)','Figure 9.1(a) — source soccer-ball trajectory illustrated by a parabolic arc',paths,[],size=(450,320))
def equal_distances():
 # y = −x²/4 in mathematical units, scale 50, focus (0,−1), directrix y = 1.
 paths=[path([(240+u,105+u*u/200) for u in range(-145,146,3)]),path([(70,55),(420,55)]),path([(320,137),(240,155)],stroke='#be123c'),path([(320,137),(320,55)],stroke='#be123c'),path([(310,55),(310,65),(320,65)])]
 return geometry('Figure 9.1(b)','Figure 9.1(b) — parabola point equidistant from focus and directrix',paths,[(149,45,'directrix'),(214,176,'focus'),(325,142,'P'),(178,109,'parabola'),(324,101,'equal'),(268,202,'distances')],points=[{'x':240,'y':155},{'x':320,'y':137}],size=(460,330))
def parabola_elements():
 # y² = 4px, p = 40 display units; graph includes both latus-rectum endpoints.
 paths=[path([(205+y*y/160,185-y) for y in range(-130,131,2)]),path([(165,40),(165,315)]),path([(130,185),(445,185)],dash=True),path([(245,105),(245,265)])]
 for y in [28,55,80,108]:
  p=(205+y*y/160,185-y);paths.extend([path([(165,p[1]),p]),path([(245,185),p])])
 return geometry('Figure 9.2','Figure 9.2 — focus F(p,0), directrix x = −p, vertex and perpendicular focal chord AB (latus rectum)',paths,[(99,132,'Directrix'),(131,153,'x = −p'),(194,211,'V'),(243,209,'F(p,0)'),(252,97,'B'),(249,285,'A'),(288,244,'focus'),(127,206,'P′')],points=[{'x':245,'y':185},{'x':205,'y':185}],size=(480,340))
PAGES=[page('125_page_1.jpg',241,[]),page('125_page_2.jpg',242,INTRO+[
 heading('9.1 Parabola'),paragraph('When you kick a soccer ball (or shoot an arrow, fire a missile or throw a stone) it arcs up into the air and comes down again ...'),projectile(),paragraph('A parabola is a curve where any point is at an equal distance from: a fixed point (the focus), and a fixed straight line (the directrix). Get a piece of paper, draw a straight line on it, then make a big dot for the focus (not on the line!). Now play around with some measurements until you have another dot that is exactly the same distance from the focus and the straight line. Keep going until you have lots of little dots, then join the little dots and you will have a parabola!'),equal_distances(),paragraph('In our study of quadratic functions, the graph of the general form of the quadratic equation'),eq(r'y=ax^2+bx+c','i'),paragraph('(with a ≠ 0) is a parabola that opens upward if a > 0 and downward if a < 0.'),heading('Remember'),paragraph('The graph of a quadratic equation is always parabola. But all parabolas can not be represented by quadratic equation, because all parabolas are not graphs of the functions.'),note('The statement about a quadratic graph refers to y = ax²+bx+c with a ≠ 0. Every parabola does have a quadratic equation in two Cartesian variables; for example y² = 4px opens sideways and is not a single-valued function y of x. The projectile illustration assumes constant downward gravity, a flat reference frame and negligible air resistance, so it is a model rather than a claim about every real flight.'),heading('(i) Parabola and its elements (i.e. focus, directrix, eccentricity, vertex, axis, focal chord and latus rectum)'),paragraph('The parabola is the set of all points P in the plane such that the distance from a fixed point F (focus) and the distance from a fixed straight line (directrix) to a point are equidistant. The line through the focus perpendicular to the directrix is called the principal axis of the parabola, and the point where the axis intersects the parabola is called the vertex. The line segment AB that passes through the focus perpendicular to the axis and with endpoints on the parabola is called the focal chord or its latus rectum. These terminologies are shown in the Figure 9.2.'),parabola_elements(),note('Distance to the directrix means perpendicular point-to-line distance. The focus must be off that line for a nondegenerate parabola. A focal chord is any chord through the focus; the latus rectum is specifically the one perpendicular to the axis. Figure 9.2 depicts that special focal chord, with the vertex halfway between focus and directrix.')])]
PAGES[0]['objectives']=OBJECTIVES
for p in PAGES:
 p.update(title='CONICS-II',visualStatus='Complete source objectives/introduction and three native parabola figures with exact equal-distance geometry',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':125,'side':'left' if p['page']==241 else 'right','reason':'All objective elements, quadratic-function qualification and focus/directrix labels visually checked'})
