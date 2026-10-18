"""Printed page 31. Graph scales checked against full PDF page 20;
answer intervals cross-checked against printed answer page 326 (PDF 167).
"""
from math12_reviewed_unit1 import heading, paragraph, figure, page

def graph(label, **definition):
    return {'type':'diagram','id':'math12-ex21-q1-'+label,'caption':'('+label+')','diagram':{'type':'source-function-graph','title':'('+label+')', **definition}}

GRAPHS = [
    graph('a',xMin=-10,xMax=10,yMin=-95,yMax=5,xTicks=[-10,-5,0,5,10],yTicks=[-90,-80,-70,-60,-50,-40,-30,-20,-10],yGridStep=5,polynomial=[5,0,-1]),
    graph('b',xMin=-10,xMax=10,yMin=-1000,yMax=1000,xTicks=[-10,-5,0,5,10],yTicks=[-1000,-500,500,1000],yGridStep=100,polynomial=[0,0,0,1]),
    graph('c',xMin=-10,xMax=10,yMin=-4.5,yMax=4.5,xTicks=[-10,-5,0,5,10],yTicks=[-4,-3,-2,-1,1,2,3,4],yGridStep=.5,reciprocalShift=2,asymptote=-2),
    graph('d',xMin=-10,xMax=10,yMin=0,yMax=20,xTicks=[-10,-5,0,5,10],yTicks=[5,10,15,20],polynomial=[7,2]),
    graph('e',xMin=-10,xMax=10,yMin=0,yMax=20,xTicks=[-10,-5,0,5,10],yTicks=[5,10,15,20],polynomial=[0,0,1]),
    graph('f',xMin=-10,xMax=10,yMin=-20,yMax=20,xTicks=[-10,-5,0,5,10],yTicks=[-20,-10,10,20],yGridStep=5,absolute={'a':1,'b':0})
]
QUESTIONS = [
    'Read the graphs and write the function, domain and range of f.',
    'Draw the graphs of the following functions.\n(a) 2|x − 3|\n(b) 4|x − 3| + 3\n(c) 5|3x + 7| − 2\n(d) 2|4x + 3| + 1',
    r'Find the composite functions f(g(x)) and g(f(x)) of the following functions:'+'\n'+r'(a) \(f(x)=x^2+1, g(x)=2x\)'+'\n'+r'(b) \(f(x)=\sin x, g(x)=1-x^2\)'+'\n'+r'(c) \(f(x)=\frac{x-1}{x+1}, g(x)=\frac{x+1}{1-x}\)'+'\n'+r'(d) \(f(x)=\sin x, g(x)=2x+3\)',
    r'Determine the inverse function of f(g(x)) and g(f(x)) for the following functions:'+'\n'+r'(a) \(f(x)=x+5, g(x)=x-4\)'+'\n'+r'(b) \(f(x)=2x+7, g(x)=2x\)'+'\n'+r'(c) \(f(x)=2(x-4), g(x)=\frac{x+5}{2}\)'+'\n'+r'(d) \(f(x)=\frac{x+4}{2}, g(x)=2x-4\)',
    'Observe the following graphs and identify their domain and range.'
]
PROJECT = [figure('ex21-project-landscape','Project (i)','Landscape profile with a coordinate grid; peak near y = 4 and a valley touching y = 0'),figure('ex21-project-car','Project (ii)','Car profile with a coordinate grid; topmost marked point is near x = 8, y = 3')]
PAGES = [page('020_page_1.jpg',31,[heading('Exercise 2.1'),heading('1.'),paragraph(QUESTIONS[0]),*GRAPHS,heading('2.'),paragraph(QUESTIONS[1]),heading('3.'),paragraph(QUESTIONS[2]),heading('4.'),paragraph(QUESTIONS[3]),heading('Project'),paragraph(QUESTIONS[4]),*PROJECT])]
PAGES[0]['visualStatus']='Six exercise graphs recreated as SVG from standard function families matching the source scales; two photographic project diagrams retained as isolated source crops'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':20,'side':'left','reason':'Sharper spread confirms graph scales, signs and all rational-function denominators.'}
PAGES[0]['sourceNotes']=['No algebraic formulas are printed beside Question 1 graphs; formula identification in the learning solution is an inference from the standard curve families and plotted scales.','Printed answer page 326 gives the first range as (−∞, 5), although the parabola reaches its maximum; the distinction is labelled in the learning solution.']
FIGURE_PDF_CROPS = [(20,'ex21-project-landscape',(119,850,376,995)),(20,'ex21-project-car',(388,850,755,995))]

STEPS = [
    [
        'Identify the standard curve families from the shapes and scales. Matching formulas inferred from the graphs are (a) 5 − x², (b) x³, (c) 1/(x + 2), (d) 2x + 7, (e) x², (f) |x|. The book does not print these formulas beside the graphs.',
        '(a) The downward parabola reaches a maximum of 5 and continues in both horizontal directions. Domain: ℝ; range: (−∞, 5].',
        '(b) The cubic continues through all x-values and takes all real y-values. Domain: ℝ; range: ℝ.',
        '(c) The vertical asymptote excludes x = −2, and the curve never reaches y = 0. Domain: ℝ ∖ {−2}; range: ℝ ∖ {0}.',
        '(d) The nonconstant straight line has domain ℝ and range ℝ.',
        '(e) The upward parabola and (f) the absolute-value graph each have domain ℝ and range [0, ∞).'
    ],
    [
        '(a) For 2|x − 3|, set x − 3 = 0. The vertex is (3, 0); branch slopes are −2 and 2. Plot (0, 6), (3, 0), (6, 6).',
        '(b) For 4|x − 3| + 3, the vertex is (3, 3); branch slopes are −4 and 4. Plot (0, 15), (3, 3), (6, 15).',
        '(c) For 5|3x + 7| − 2, solve 3x + 7 = 0. The vertex is (−7/3, −2); branch slopes are −15 and 15. Plot (−3, 8), (−7/3, −2), (−2, 3).',
        '(d) For 2|4x + 3| + 1, solve 4x + 3 = 0. The vertex is (−3/4, 1); branch slopes are −8 and 8. Plot (−1, 3), (−3/4, 1), (0, 7).',
        'All four functions are defined for every real x and open upward. Their ranges start at the vertex y-values: (a) [0, ∞), (b) [3, ∞), (c) [−2, ∞), (d) [1, ∞).'
    ],
    [
        '(a) f(g(x)) = (2x)² + 1 = 4x² + 1; g(f(x)) = 2(x² + 1) = 2x² + 2. Both domains are ℝ.',
        '(b) f(g(x)) = sin(1 − x²); g(f(x)) = 1 − sin²x = cos²x. Both domains are ℝ.',
        r'(c) \(f(g(x))=\frac{\frac{x+1}{1-x}-1}{\frac{x+1}{1-x}+1}=\frac{2x/(1-x)}{2/(1-x)}=x\). The inner g requires x ≠ 1; g(x) never equals −1. Domain: ℝ ∖ {1}.',
        r'(c) \(g(f(x))=\frac{\frac{x-1}{x+1}+1}{1-\frac{x-1}{x+1}}=\frac{2x/(x+1)}{2/(x+1)}=x\). The inner f requires x ≠ −1; f(x) never equals 1. Domain: ℝ ∖ {−1}.',
        '(d) f(g(x)) = sin(2x + 3); g(f(x)) = 2 sin x + 3. Both domains are ℝ. Simplifying the rational compositions to x does not restore their excluded inputs.'
    ],
    [
        '(a) f(g(x)) = (x − 4) + 5 = x + 1, and g(f(x)) = (x + 5) − 4 = x + 1. Solve y = x + 1 to get the inverse x − 1 for each.',
        '(b) f(g(x)) = 2(2x) + 7 = 4x + 7. Solve y = 4x + 7: inverse (x − 7)/4. For g(f(x)) = 2(2x + 7) = 4x + 14, the inverse is (x − 14)/4.',
        '(c) f(g(x)) = 2((x + 5)/2 − 4) = x − 3, so its inverse is x + 3. For g(f(x)) = (2(x − 4) + 5)/2 = x − 3/2, the inverse is x + 3/2.',
        '(d) f(g(x)) = ((2x − 4) + 4)/2 = x, and g(f(x)) = 2((x + 4)/2) − 4 = x. Both inverses are the identity function x.'
    ],
    ['Read the horizontal extent of each highlighted profile for its domain; read its lowest and highest y-values for its range.', 'The landscape profile reaches the horizontal axis at the valley and has a highest visible level near y = 4. Its visible range is approximately [0, 4].', 'The car’s upper outline reaches a marked high point near (8, 3). The intended upper profile has visible range approximately [0, 3].', 'The photograph crops do not mark both horizontal endpoints unambiguously. Use the visible coordinate grid to estimate the shown domains; exact endpoint values remain unverified. Do not infer an infinite domain from the cropped pictures.']
]
ANSWERS = ['(a) ℝ, (−∞, 5]; (b) ℝ, ℝ; (c) ℝ ∖ {−2}, ℝ ∖ {0}; (d) ℝ, ℝ; (e)–(f) ℝ, [0, ∞).','All domains: ℝ. Ranges: (a) [0, ∞); (b) [3, ∞); (c) [−2, ∞); (d) [1, ∞).','See the compositions and their domains above.','Inverses, in the order (f ∘ g)⁻¹, (g ∘ f)⁻¹: (a) x − 1, x − 1; (b) (x − 7)/4, (x − 14)/4; (c) x + 3, x + 3/2; (d) x, x.','Visible ranges approximately [0, 4] and [0, 3]; exact project domains still require clearer endpoint evidence.']
