"""Printed pages 27–28, visually checked against JPGs and full PDF page 18."""
from math12_reviewed_unit1 import heading, paragraph, page

def graph(number, title, definition):
    return {'type':'diagram', 'id':f'math12-source-figure-2-{number}', 'caption':f'Figure 2.{number}', 'diagram':{'type':'source-function-graph', 'title':title, **definition}}

def piecewise(label, rows):
    return {'type':'piecewise', 'label':label, 'rows':rows}

def table(rows, caption=None):
    return {'type':'table', 'rows':rows, 'caption':caption}

SOURCE_CURVE = {'xMin':-7,'xMax':5,'yMin':-2,'yMax':6,'xTicks':[-5,0,5],'yTicks':[5], 'trace': [[[-6,0],[-4.5,5.3],[-2.5,5.3],[0,0]],[[0,0],[.8,.1],[1.8,1.1],[2,3]]], 'endpoints':[[-6,0],[2,3]]}

PAGES = [
    page('018_page_1.jpg', 27, [
        graph(2, 'Domain and range example', SOURCE_CURVE),
        graph(3, 'Domain and range example', {**SOURCE_CURVE, 'domainRange':True}),
        heading('Remember'), paragraph('If the graph continuous beyond the given portion of the graph the domain and range can be greater than the given values.'),
        heading('2.1.2 Graph of modulus function (i.e. y = |x|) and its domain and range'),
        paragraph('“A function that contains an algebraic expression with in the absolute value symbols is called an absolute value function.”'),
        paragraph('In our previous classes we have studied that the absolute value of a number is its distance from 0 on the number line.'),
        paragraph('The parent absolute value function can be written as f(x) = |x| which is defined as'),
        piecewise('f(x) =', [['x','if x ≥ 0'],['−x','if x < 0']]),
        paragraph('To graph the above absolute value functions simply choose some values of x and get the values of y then draw them accordingly.'),
        table([['x',-4,-3,-2,-1,0,1,2,3,4,'Domain values'],['y',4,3,2,1,0,1,2,3,4,'Range values']]),
        paragraph('Now, plot the points'),
        paragraph('In general, domain of f(x) = |x| is (−∞, ∞) and range is [0, ∞) but the graph is v-shaped graph. Figure 2.4 shows the graph of f(x) = |x|.'),
        graph(4, 'f(x) = |x|', {'xMin':-10,'xMax':10,'yMin':0,'yMax':10,'xTicks':[-10,-5,0,5,10],'yTicks':[2,4,6,8,10],'absolute':{'a':1,'b':0}}),
        heading('Remember'),
        paragraph('In any absolute value function for vertical translation of f(x) = |x| you can use the function g(x) = f(x) + h'),
        paragraph('(i) When h > 0 the graph of f(x) translate ‘h’ unit up to get g(x).'),
        paragraph('(ii) When h < 0 the graph f(x) translate ‘h’ units down to get g(x).'),
        paragraph('This is called vertical translation. For horizontal translation of f(x) = |x| you can use the function g(x) = f(x − k)'),
        paragraph('(i) When k > 0 the graph of f(x) will translate ‘k’ units to the right to get g(x).'),
        paragraph('(ii) When k < 0 the graph of f(x) will translate ‘k’ units to the right to get g(x).'),
        paragraph('This is called horizontal translation.'),
        {'type':'clarification','text':'For g(x) = f(x − k), a negative k moves the graph left by |k| units. The printed reminder repeats “right”; its wording above is retained.'},
        heading('Example 2'), paragraph('Graph the following absolute value functions and identify its domain and range: f(x) = |3x − 4|'),
        heading('Solution'), paragraph('From the definition of absolute value function, the given function is'),
        piecewise('f(x) =', [['3x + 4','if 3x + 4 ≥ 0'],['−(3x + 4)','if 3x + 4 < 0']]),
        graph(5, 'f(x) = |3x + 4|', {'xMin':-10,'xMax':10,'yMin':0,'yMax':35,'xTicks':[-10,-5,0,5,10],'yTicks':[5,10,15,20,25,30],'absolute':{'a':3,'b':4}}),
        paragraph(r'The inequality \(3x+4\ge0\) is satisfied whenever \(x\ge-\frac{4}{3}\), and \(3x+4<0\)')
    ]),
    page('018_page_2.jpg', 28, [
        {**paragraph(r'is satisfied whenever \(x<-\frac{4}{3}\). If \(x=-\frac{4}{3}\), \(y=0\), so the graph will consist of two lines that meet at \(\left(-\frac{4}{3},0\right)\). Use the tabular form to obtain the graph of a function:'), 'continuesPreviousParagraph':True},
        table([['x',r'\(-\frac{4}{3}\)',0],['y',0,4]], 'f(x) = 3x + 4, 3x + 4 ≥ 0'),
        table([['x',r'\(-\frac{4}{3}\)',-3],['y',0,5]], 'f(x) = −(3x + 4), 3x + 4 < 0'),
        paragraph('This function has a domain set (−∞, ∞) and range set is [0, ∞).'),
        {'type':'clarification','text':'Example 2 asks for |3x − 4|, while the printed solution, tables and Figure 2.5 use |3x + 4|. The requested function has vertex (4/3, 0); the printed solution has vertex (−4/3, 0). Both have domain ℝ and range [0, ∞). The source solution above is preserved.'},
        heading('2.2 Composition of Functions'),
        paragraph('Composition of function can be described as a progression of “getting” and “dropping” “off”. A function gets ‘x’ does something for it and drops it off. Then another function goes along and gets the drop off, does something for it, and drop it off once more. This pattern may proceed more than a few functions. Suppose a composition as a progression of car rides. ‘x’ boy is picked up by the first car function transported to a required location and dropped off. Then another car function come and pick up the x boy at this new location transports x boy to another location and drops x boy off.'),
        heading('2.2.1 Recognition of composite functions'),
        paragraph(r'Consider the function \(h(x)\) whose rule is \(h(x)=\sqrt{x^3}\). To compute \(h(4)\), you first need to find \(x^3=4^3=64\) and then take the square root to obtain \(\sqrt{x^3}=\sqrt{64}=8\). So the rule of \(h(x)\) may be rephrased as:'),
        {'type':'command','text':None,'result':'h(x) = f(g(x))','number':'i'},
        paragraph(r'Here \(g(x)=x^3\), and \(f(x)=\sqrt{x^3}\). We may think of the functions \(f(x)\) and \(g(x)\) as being “composed” to create the function \(h\).'),
        paragraph('In other words, when the output from one function is used as the input to another function, we form what is known as a composite function.'),
        paragraph('“If f(x) and g(x) are the two functions, then, a composite function or composition of g and f is the function whose values are given by g(f(x)) for all x in the domain of f(x) such that f(x) is in the domain of g(x).”'),
        {'type':'clarification','text':'To produce h(x) = √(x³) from g(x) = x³, the outer function must be f(x) = √x. The printed f(x) = √(x³) would instead produce √(x⁹). The original formula above is retained.'},
        heading('Example 3'), paragraph(r'Let \(f(x)=2x-1\) and \(g(x)=\sqrt{3x+5}\). Find each of the following: (a) g(f(4)) (b) f(g(4)) (c) f(g(−2))'),
        heading('Solution'),
        paragraph(r'a. The function \(f(x)\) for \(x=4\) is used to obtain \(f(4)=2(4)-1=7\). Use \(f(4)\) to obtain: \(g(f(4))=g(7)=\sqrt{3(7)+5}=\sqrt{26}\)'),
        paragraph(r'b. The function \(g(x)\) for \(x=4\) is used to obtain \(g(4)=\sqrt{3(4)+5}=\sqrt{17}\). Use g(4) to obtain: \(f(g(4))=f(\sqrt{17})=2\sqrt{17}-1\)'),
        paragraph('c. f(g(−2)) does not exist, since −2 is not in the domain of g.')
    ])
]
PAGES[0]['visualStatus'] = 'Figures 2.2–2.3 traced digitally from the source curve; Figures 2.4–2.5 recreated from their printed equations and scales; tables and piecewise definitions rendered digitally'
PAGES[1]['visualStatus'] = 'Value tables and all formulas rendered digitally'
for source in PAGES:
    source['alternateVerification'] = {'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':18,'side':'left' if source['page']==27 else 'right','reason':'Full spread restores clipped JPG text and confirms graph scales and source inconsistencies.'}
