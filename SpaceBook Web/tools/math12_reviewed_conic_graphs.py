"""Printed page 40: JPG and full PDF physical page 24 right."""
from math12_reviewed_unit1 import heading, paragraph, command, page

GRID={'type':'source-function-graph','xMin':-5,'xMax':5,'yMin':-3.75,'yMax':3.75,'xTicks':[-4,-3,-2,-1,0,1,2,3,4],'yTicks':[-3,-2,-1,1,2,3]}
CIRCLE={**GRID,'title':'x² + y² = 9','ellipse':{'a':3,'b':3}}
ELLIPSE={**GRID,'title':'x²/16 + y²/9 = 1','ellipse':{'a':4,'b':3}}
PARABOLA={'type':'source-function-graph','title':'x = 3t², y = 4t + 3','xMin':-5,'xMax':22,'yMin':-10,'yMax':12,'xTicks':[-5,0,5,10,15,20],'yTicks':[-5,5,10],'sidewaysParabola':{'coefficient':3/16,'center':3},'points':[[0,3,'(0,3)']]}
PAGES=[page('024_page_2.jpg',40,[
    heading(r'(b) Graphical display of implicit defined function such as \(x^2+y^2=a^2\) and \(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\) and distinguish between graph of a function and of an equation'),
    heading('Example 18'),paragraph(r'Sketch the graph of \(x^2+y^2=9\).'),heading('Solution'),
    paragraph(r'This equation \(x^2+y^2=9\) is an equation of circle having radius 3 with centred at origin (0, 0).'),
    paragraph(r'Rewrite the equation \(x^2+y^2=9\) as'),command(None,r'\((x-0)^2+(y-0)^2=3^2\)'),
    paragraph(r'The standard form of equation of circle is \((x-h)^2+(y-k)^2=r^2\)'),
    paragraph('With centre (h, k) = (0, 0) and radius r = 3'),paragraph('So, this is a circle of radius 3 centred at origin (0, 0).'),paragraph(r'Figure 2.17 is showing the graph of \(x^2+y^2=9\).'),
    {'type':'diagram','id':'math12-source-figure-2-17','caption':'Figure 2.17','diagram':CIRCLE},
    heading('Example 19'),paragraph(r'Sketch the graph of \(\frac{x^2}{16}+\frac{y^2}{9}=1\).'),heading('Solution'),
    paragraph(r'The equation \(\frac{x^2}{16}+\frac{y^2}{9}=1\) is an equation of ellipse.'),
    paragraph(r'Compare it with the standard equation \(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\) ∴ \(c^2=a^2-b^2\)'),
    paragraph(r'where, \(h=0, k=0, a=\sqrt{16}=4, b=\sqrt{9}=3\) and \(c=\sqrt{16-9}=\sqrt{7}\)'),
    paragraph('So,'),{'type':'list','items':[r'Center: \((h,k)=(0,0)\)',r'Foci: \((h\pm c,k)=(\pm\sqrt{7},0)\)',r'Vertices: \((h\pm a,k)=(\pm3,0)\)',r'Co-vertices: \((h,k\pm b)=(0,\pm4)\)']},
    {'type':'clarification','text':'The source interchanges the numerical semi-axis lengths in its vertices and co-vertices. For a = 4 and b = 3, the vertices are (±4, 0) and the co-vertices are (0, ±3). The printed coordinates are retained above; the equation determines the digital graph.'},
    paragraph('Graph the center, vertices, foci and axes on the graph paper as shown in Figure 2.18.'),
    {'type':'diagram','id':'math12-source-figure-2-18','caption':'Figure 2.18','diagram':ELLIPSE},
    heading('Note'),paragraph('The students will learn more about conic in unit 8 and 9.'),
    heading(r'(c) Graphical display of parametric equation functions such as \(x=at^2, y=2at;\ x=a\sec \theta, y=b\tan \theta\)'),
    heading('Example 20'),paragraph(r'Sketch the graph of the parametric function \((x(t),y(t))=(3t^2,4t+3)\).'),heading('Solution'),
    paragraph('To sketch the graph of the parametric equation, Let’s make a table to get the idea of the shape and direction of the graph.'),
    {'type':'dataTable','headers':['t','−6','−5','−4','−3','−2','−1','0','1','2','3','4','5','6'],'rows':[['x(t)','108','75','48','27','12','3','0','3','12','27','48','75','108'],['y(t)','−21','−17','−13','−9','−5','−1','3','7','11','15','19','23','27']]},
    command(None,r'\(y=4t+3\Rightarrow t=\frac{y-3}{4}\)','i'),command(None,r'\(x=3t^2\)','ii'),
    command(None,r'\(x=3\left(\frac{y-3}{4}\right)^2\)'),
    command(None,r'\(x=\frac{3}{16}(y^2-6y+9)\Rightarrow x=\frac{3}{8}(y^2-6y+9)\)'),
    {'type':'clarification','text':'The final printed implication changes 3/16 to 3/8 without justification. Eliminating t gives x = (3/16)(y − 3)². The digital curve and learning solution use the given parametric equations; the printed algebra is retained above.'},
    paragraph('This is a right opening parabola, its graph is shown in Figure 2.19.'),
    {'type':'diagram','id':'math12-source-figure-2-19','caption':'Figure 2.19','diagram':PARABOLA}
])]
PAGES[0]['visualStatus']='All equations, coordinate lists and the thirteen-column parameter table rendered digitally; Figures 2.17–2.19 reconstructed as SVG from the given equations'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':24,'side':'right','reason':'Confirms source ellipse-coordinate errors, all table values and the printed coefficient mismatch.'}
