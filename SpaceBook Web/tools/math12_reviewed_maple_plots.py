"""Printed page 42, compared against JPG and full PDF page 25 right."""
from math12_reviewed_unit1 import heading, paragraph, command, page

PARABOLA={'type':'source-function-graph','title':'y = −(x + 2)²','equalAspect':True,'xMin':-4,'xMax':0,'yMin':-4,'yMax':0,'xTicks':[-4,-3,-2,-1,0],'yTicks':[-4,-3,-2,-1],'polynomial':[-4,-4,-1]}
CIRCLE={'type':'source-function-graph','title':'Parametric circle','equalAspect':True,'xMin':-1.5,'xMax':1.5,'yMin':-1.5,'yMax':1.5,'xTicks':[-1.5,-.5,.5,1.5],'yTicks':[-1.5,-.5,.5,1.5],'xGridStep':.1,'yGridStep':.1,'ellipse':{'a':1,'b':1}}
def diagram(number,graph):
    return {'type':'diagram','id':f'math12-source-figure-2-{number}','caption':f'Figure 2.{number}','diagram':graph}

PAGES=[page('025_page_2.jpg',42,[
    heading('2.5.2 MAPLE graphic commands for two-dimensional plot of'),
    {'type':'list','items':['an expression (or a function)','a parameterized form of a function','implicit function by restricting domain and range']},
    paragraph('Look at the following example, the procedure to use the maple graphic commands is illustrated.'),
    heading('Example 23'),paragraph('Use maple commands to draw the graphs of the given function.'),
    {'type':'list','items':[r'(a). Function \(f(x)=-(x+2)^2\), with domain [0, −4].',r'(b). Parametric function \((x(t),y(t))=\cos(t).\sin(t)\) for t = −3.5 to 3.5, x from −1.5 to 1.5 and y from −1.5 to 1.5.',r'(c). An implicit function \(x^2-y^2=1\), x from −5 to 5 and y from −5 to 5.']},
    heading('Solution'),paragraph('The command below will show you full detail of plotting expressions/ functions on line by typing:'),command('?plots'),
    heading('a. Command'),command('plot(−(x + 2)^2, x = 0..−4);'),diagram(21,PARABOLA),
    heading('Context Menu'),command('−(x + 2)^2',r'\(-(x+2)^2\)',1),command('plot(−(x + 2)^2, x = 0..−4)'),diagram(22,PARABOLA),
    {'type':'clarification','text':'The source prints the reversed interval [0, −4] and x = 0..−4, while its graph spans −4 ≤ x ≤ 0. The printed syntax is retained. The digital graph follows the displayed parabola on [−4, 0].'},
    heading('b. Command'),command('plot([cos(t), sin(t), t = −3.5..3.5], −1.5..1.5, −1.5..1.5);'),diagram(23,CIRCLE),
    heading('Context Menu'),command('sin(t), cos(t)','sin(t), cos(t)',1),command('plot([sin(t), cos(t), t = −3.5..3.5])'),diagram(24,CIRCLE),
    {'type':'clarification','text':'The source uses cos(t), sin(t) in the command and sin(t), cos(t) in the context menu. Both trace the same unit circle, but they start at different points and travel in opposite directions as t increases. The interval [−3.5, 3.5] exceeds one full turn.'},
    paragraph('This graph is obtained through right-click on the last end of the expression by selecting "Plots < Plot Builder < 2D Parametric Plot" on the context menu.')
])]
PAGES[0]['visualStatus']='Commands and numbered outputs rendered digitally; Figures 2.21–2.24 reconstructed as SVG with equal coordinate scales from their plotted expressions'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':25,'side':'right','reason':'Confirms clipped headings, reversed range, command/context-menu coordinate order and plot-menu wording.'}
PAGES[0]['sourceNotes']=['Example 23 continues on printed page 43; its complete source text and learning solution are verified across pages 42–43.']
