"""Printed page 41, visually checked with JPG and full PDF physical page 25 left."""
from math12_reviewed_unit1 import heading, paragraph, command, page
from math12_reviewed_modulus import piecewise

COMPOUND={'type':'source-function-graph','title':'Compound function: 3 − x; x + 2; 1','xMin':-7,'xMax':9,'yMin':-3,'yMax':10,'xTicks':[-6,-4,-2,0,2,4,6],'yTicks':[2,4,6,8],'linearSegments':[[-6,9,-2,5],[-2,0,2,4],[2,1,8,1]],'openPoints':[[-2,5],[2,4]],'closedPoints':[[-2,0],[2,1]],'rays':[[-2,5,-6,9],[2,1,8,1]]}
ELLIPSE={'type':'source-function-graph','title':'x = 3 cos t, y = 2 sin t, 0 ≤ t ≤ 2π','xMin':-4,'xMax':4,'yMin':-3,'yMax':3,'xTicks':[-3,-2,-1,0,1,2,3],'yTicks':[-2,-1,1,2],'ellipse':{'a':3,'b':2}}
PAGES=[page('025_page_1.jpg',41,[
    heading('Example 21'),paragraph(r'Sketch the graph of the parametric function \((x(t),y(t))=(3\cos(t),2\sin(t))\) for \(0\leq t\leq2\pi\).'),heading('Solution'),
    paragraph('To sketch the graph of the parametric equation, Let’s make a table to get the idea of the shape and direction of the graph.'),
    {'type':'dataTable','headers':['t','0',r'\(\frac{\pi}{4}\)',r'\(\frac{\pi}{2}\)',r'\(\frac{3\pi}{4}\)',r'\(\pi\)',r'\(\frac{5\pi}{4}\)',r'\(\frac{3\pi}{2}\)',r'\(\frac{7\pi}{4}\)',r'\(2\pi\)'],'rows':[['x(t)','3','2.12','0','−2.12','−3','−2.12','0','2.12','3'],['y(t)','0','1.41','2','1.41','0','−1.41','−2','−1.41','0']]},
    paragraph('Now, convert the standard form by eliminating the parameter. e.g.'),
    command(None,r'\(x=3\cos(t)\Rightarrow x^2=9\cos^2(t)\)','i'),command(None,r'\(y=2\sin(t)\Rightarrow y^2=4\sin^2(t)\)','ii'),
    paragraph(r'From (i) and (ii). \(\frac{x^2}{9}+\frac{y^2}{4}=\cos^2(t)+\sin^2(t)=1\)'),
    paragraph(r'So, the formula of ellipse is \(\frac{x^2}{9}+\frac{y^2}{4}=1\) where a = 3, b = 2.'),
    paragraph('This is an ellipse, which will be discussed in detail in unit-9.'),
    heading('(d) Graphical display of discontinuous functions of the type'),
    piecewise('y =',[['x','when 0 ≤ x < 1'],['x − 1','when 1 ≤ x ≤ 2']]),
    heading('Example 22'),paragraph('Graph the compound function:'),
    piecewise('f(x) =',[['3 − x','if x < −2'],['x + 2','if −2 ≤ x < 2'],['1','if x ≥ 2']]),heading('Solution'),
    paragraph('a. Use the function f(x) = 3 − x for x < −2 to obtain a set of points:'),
    {'type':'dataTable','headers':['x','−3','−2'],'rows':[['f(x)','6','5']]},
    paragraph('b. Use the function f(x) = x + 2 for −2 ≤ x < 2 to obtain a set of points:'),
    {'type':'dataTable','headers':['x','−2','2'],'rows':[['f(x)','0','4']]},
    paragraph('c. Use the function f(x) = 1 for x ≥ 2 to obtain a set of points:'),
    {'type':'dataTable','headers':['x','2','4'],'rows':[['f(x)','1','1']]},
    {'type':'clarification','text':'The first two source tables include their excluded boundary values as plotting guides. At x = −2, use an open endpoint at (−2, 5) and a closed endpoint at (−2, 0). At x = 2, use an open endpoint at (2, 4) and a closed endpoint at (2, 1). The function takes only the closed endpoint value at each boundary.'},
    paragraph('Use these tabular points to obtain the graph of a compound function in Figure 2.20.'),
    {'type':'diagram','id':'math12-source-figure-2-20','caption':'Figure 2.20','diagram':COMPOUND},
    heading('Do You Know?'),paragraph('A function that defined by more than one equation is called compound function.')
])]
PAGES[0]['visualStatus']='Parametric table, four coordinate equations, two piecewise definitions and three plotting tables rendered digitally; Figure 2.20 reconstructed with its open and closed endpoints'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':25,'side':'left','reason':'Confirms endpoint inclusion, all nine parameter values and the clipped compound-function note.'}
