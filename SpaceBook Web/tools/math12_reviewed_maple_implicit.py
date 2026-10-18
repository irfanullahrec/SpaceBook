"""Printed page 43, checked against JPG and full PDF page 26 left."""
from math12_reviewed_unit1 import heading, paragraph, command, page

HYPERBOLA={'type':'source-function-graph','title':'x² − y² = 1','equalAspect':True,'xMin':-5,'xMax':5,'yMin':-5,'yMax':5,'xTicks':[-4,-2,0,2,4],'yTicks':[-4,-2,2,4],'hyperbola':True,'diagonalAsymptotes':True}
CONTEXT_HYPERBOLA={**HYPERBOLA,'xMin':-10,'xMax':10,'yMin':-10,'yMax':10,'xTicks':[-10,-5,0,5,10],'yTicks':[-5,5,10]}
FRAME={'type':'source-function-graph','title':'y = x² − b, printed initial frame b = −5','xMin':-10,'xMax':10,'yMin':-10,'yMax':110,'xTicks':[-10,-5,0,5,10],'yTicks':[20,40,60,80,100],'yGridStep':10,'polynomial':[5,0,1]}
def diagram(n,graph):
    return {'type':'diagram','id':f'math12-source-figure-2-{n}','caption':f'Figure 2.{n}','diagram':graph}

PAGES=[page('026_page_1.jpg',43,[
    heading('c. Command'),command('plots[implicitplot](x^2 − y^2 = 1, x = −5..5, y = −5..5);'),diagram(25,HYPERBOLA),
    heading('Context Menu'),command('x^2 − y^2 = 1',r'\(x^2-y^2=1\)',1),command('smartplot[x,y](x^2 − y^2 = 1)'),diagram(26,CONTEXT_HYPERBOLA),
    paragraph('This graph is obtained through right-click on the last end of the expression by selecting "Plots < 2D-Implicit Plot < x, y" on the context menu.'),
    heading('2.5.3 MAPLE package plots for plotting different types of functions'),
    paragraph('Look at the following example the procedure of plotting the functions using maple package is illustrated.'),heading('Example 24'),paragraph('Use MAPLE commands to draw the following functions.'),heading('Solution'),
    paragraph(r'(a). \(f(x)=x^2-b\), x from −1 to 10 and y from −5 to 5.'),
    paragraph(r'(b). \((x(t),y(t))=\cos(tx)\sin(ty)\), t from −1 to 2, x from −π to π, y from −π to π.'),
    paragraph('The command below will show you full detail of plotting packages on line by typing'),command('?plots[animate]'),
    heading('a. Command'),command('plots[animate](plot, [x^2 − b, x = −10..10], b = −5..5);'),command(None,'b = −5.'),diagram(27,FRAME),
    heading('Context Menu'),command('x^2 − b',r'\(x^2-b\)',1),command('plots[animate](\'plot\', [x^2 − b, x = −10..10, labels = [x, ""]], b = −5..5)'),command(None,'b = −5.'),diagram(28,FRAME),
    {'type':'clarification','text':'The source describes x from −1 to 10 and y from −5 to 5, but its command uses x from −10 to 10 and animates b from −5 to 5. Both versions are retained. These digital figures show the printed initial animation frame b = −5, so y = x² + 5; they do not claim to show the complete animation.'},
    paragraph('This graph is obtained through right-click on the last end of the expression by selecting "Plots < Plot Builder < Animation (choose 2D-Implicit Plot)" on the context menu.')
])]
PAGES[0]['visualStatus']='All Maple commands and outputs rendered digitally; Figures 2.25–2.28 reconstructed as SVG, with the animation frame b = −5 explicitly identified'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':26,'side':'left','reason':'Restores menu wording and confirms the hyperbola, animation ranges, labels and initial frame.'}
PAGES[0]['sourceNotes']=['Example 23 is verified across pages 42–43. Example 24 continues on page 44; its full source text and learning solution are verified across pages 43–44.']
