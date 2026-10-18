"""Unit 2 opening: JPG transcription checked against full PDF physical page 17."""
from math12_reviewed_unit1 import heading, paragraph, figure, page

PAGES = [
    {'file':'017_page_1.jpg', 'page':25, 'title':'FUNCTIONS AND LIMITS', 'paragraphs':[], 'objectives':[
        ['2.1 Function', ['Identify through graph the domain and range of a function.', r'Draw the graph of modulus function (i.e. \(y=|x|\)) and identify its domain and range.']],
        ['2.2 Composition of functions', ['Recognize the composition of functions.', 'Find the composition of two given functions.']],
        ['2.3 Inverse of composition of functions', ['Describe the inverse of composition of two given functions.']],
        ['Transcendental functions', ['Recognize algebraic, trigonometric, inverse trigonometric, exponential, logarithmic, hyperbolic (and their identities), explicit and implicit functions, and parametric representation of functions.']],
        ['Graphical representations', [
            'Display graphically:',
            r'the explicitly defined functions like \(y=f(x)\), where \(f(x)=e^x, a^x, \log_a x, \log_e x\).',
            r'the implicitly defined functions such as \(x^2+y^2=a^2\) and \(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\) and distinguish between graph of a function and of an equation.',
            r'the parametric equations of functions such as \(x=at^2, y=2at; x=a\sec\theta, y=b\tan\theta\).',
            'the discontinuous functions of the type y = x when 0 ≤ x ≤ 1; y = x − 1 when 1 ≤ x ≤ 2.',
            'Use MAPLE graphic commands for two-dimensional plot of: an expression (or a function), parameterized form of a function, implicit function by restricting domain and range.',
            'Use MAPLE package plots for plotting different types of functions.'
        ]],
        ['2.6 Limit of a function', ['Identify a real number by a point on the number line.', 'Define and represent: open interval, closed interval, half open and half closed intervals, on the number line.', r'Explain the meaning of phrase: x tends to zero \((x\to0)\), x tends to a \((x\to a)\), x tends to infinity \((x\to\infty)\).', 'Define limit of a sequence.', 'Find the limit of a sequence whose nth term is given.', 'Define limit of a function.', 'State the theorems on limits of sum, difference, product and quotient of functions and demonstrate through examples.']],
        ['2.7 Important limits', [
            'Evaluate the limits of functions of the following types:',
            r'\(\frac{x^n-a^n}{x-a}, \frac{x-a}{\sqrt{x}-\sqrt{a}}\) when \(x\to a\),',
            r'\(\left(1+\frac{1}{x}\right)^x\) when \(x\to\infty\),',
            r'\((1+x)^{\frac{1}{x}}, \frac{\sqrt{x+a}-\sqrt{a}}{x}, \frac{a^x-1}{x}, \frac{(1+x)^n-1}{x}, \frac{\sin x}{x}\) when \(x\to0\).',
            'Evaluate limits of different algebraic, exponential and trigonometric functions.', 'Use MAPLE command limit to evaluate limit of a function.'
        ]],
        ['2.8 Continuous and discontinuous functions', ['Recognize left hand and right hand limits and demonstrate through examples.', 'Define continuity of a function at a point and in an interval.', 'Test continuity and discontinuity of a function at a point and in an interval.', 'Use MAPLE command iscont to test continuity of a function at a point and in a given interval.']]
    ], 'visualStatus':'Objectives and mathematical notation rendered digitally; decorative unit banner omitted', 'sourceDefects':['Section numbers for two clipped objective headings remain unavailable in both source copies; missing numbers are not invented.'], 'sourceNotes':['The Transcendental functions heading is restored using printed page 32. The Graphical representations heading prefix is restored using printed page 37 and its visible plural suffix on this page. Missing section numbers remain unverified.']},
    page('017_page_2.jpg', 26, [
        heading('Introduction'),
        paragraph('The concept of function and its limit is fundamental idea to us, in the study of mathematics that distinguishes calculus from algebra and trigonometry. In this unit, we will revise the concept of function from unit-8 of grade-XI mathematics and then develop the concept of limit which is the fundamental building block on which all the calculus concepts are based.'),
        heading('2.1 Functions'),
        paragraph('Function are constantly encountered in mathematics and are essential for formulating physical relationships in science and technology. In our routine life function is very useful e.g. Zurain like all kind of animals. He started collecting them recently and already owns 3 animals. He plans on buying every month accordingly, of each type of animals.'),
        figure('unit2-animals', 'The three animals Zurain owns before he started his collection.', 'Three animals: a goat, a cow and a horse'),
        paragraph('Let ‘x’ be the number of months have past since Zurain started collecting animals. Let ‘y’ be the number of animals Zurain owns. How can we write a function in terms of x and y?'),
        paragraph('To write the function, at very beginning, when x = 0, Zurain has not bought any new animal, he owns 3 animals so, y = 3 animals'),
        paragraph('After the first month, when x = 1, Zurain owns 3 animals, plus the 1 animal he just bought. He now owns y = 3 + 1 animals'),
        paragraph('Similarly, after the second month, when x = 2, Zurain owns 3 animals, plus the 2 new animals he bought after he started animals. He now owns y = 3 + 2 animals'),
        paragraph('Therefore for x animals the function will be y = 3 + x where, ‘x’ is independent variable and ‘y’ is dependent variable.'),
        heading('History'), figure('unit2-dirichlet', 'Peter Gustav Lejeune Dirichlet (1805–1859)', 'Portrait of Peter Gustav Lejeune Dirichlet'),
        paragraph('Peter Dirichlet was a German Mathematician who made valuable contributions in the study of mathematics such as number theory, mechanics and analysis. He was the first person who gave the modern definition of function in 1837.'),
        paragraph('In mathematics, the word function is used in much the same way, but more restrictively. It is defined as:'),
        paragraph('“If a variable ‘y’ depends on a variable ‘x’ in such a way that each value of ‘x’ determines exactly one value of ‘y’ then we call it ‘y’ is a function of ‘x’: e.g. y = f(x).”'),
        heading('2.1.1 Domain and range of a function through graph'),
        paragraph('The domain and range can be identified by the graph. Because domain refers to the set of all input values, so, “all the values shown on the x-axis. The range refers to the set of all output values. Which are shown on the y-axis. Consider the graph given in Figure 2.1.'),
        {'type':'diagram', 'id':'math12-source-figure-2-1', 'caption':'Figure 2.1', 'diagram':{'type':'source-reciprocal-graph', 'title':r'\(f(x)=\frac{1}{x+2}\)'}},
        paragraph(r'This is a graph of the function \(f(x)=\frac{1}{x+2}\)'),
        paragraph(r'Its domain is \((-\infty,-2)\cup(-2,\infty)\) and range is \((-\infty,0)\cup(0,\infty)\)'),
        heading('Example 1'), paragraph('Find the domain and range of the function whose graph is shown in the Figure 2.2.'),
        heading('Solution'), paragraph('Here the horizontal extent is −6 to 2. So, the domain of the function is x ∈ [−6, 2] vertical extent of the graph is 0 to 4. So the range of the function is y ∈ [0, 4]. Shown in the Figure 2.3.')
    ])
]
PAGES[1]['visualStatus'] = 'Reciprocal graph recreated as SVG; animal and portrait illustrations cropped without surrounding text'
for source in PAGES:
    source['alternateVerification'] = {'pdf':'Math Book for 12 class KPTBB.pdf', 'pdfPage':17, 'side':'left' if source['page']==25 else 'right', 'reason':'Full spread used to confirm mathematical notation and clipped page edges.'}
FIGURE_PDF_CROPS = [(17,'unit2-animals',(1253,273,1477,332)), (17,'unit2-dirichlet',(1356,413,1449,504))]
