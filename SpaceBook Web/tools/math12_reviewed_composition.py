"""Printed pages 29–30, checked against JPGs and full PDF page 19."""
from math12_reviewed_unit1 import heading, paragraph, command, page

PAGES = [
    page('019_page_1.jpg', 29, [
        heading('2.2.2 Composition of two given functions'),
        heading('Example 4'), paragraph(r'Let \(f(x)=4x+1\) and \(g(x)=2x^2+5x\). Find each of the following: (a) g(f(x)) (b) f(g(x))'),
        heading('Solution'), paragraph('a. Using the given functions to obtain:'),
        paragraph(r'\(g(f(x))=g(4x+1)=2(4x+1)^2+5(4x+1)=2(16x^2+8x+1)+20x+5\)'),
        paragraph(r'\(=32x^2+16x+2+20x+5=32x^2+36x+7\)'),
        paragraph('b. Using the given functions to obtain:'),
        paragraph(r'\(f(g(x))=f(2x^2+5x)=4(2x^2+5x)+1=8x^2+20x+1\).'),
        paragraph('This example shows that f(g(x)) is not usually equal to g(f(x)).'),
        heading('Example 5'), paragraph('Air pollution is a problem for many metropolitan areas. Suppose that carbon monoxide is measured as a function of the number of people according to the following information:'),
        {'type':'dataTable', 'headers':['Number of People','Daily Carbon Monoxide Level (in parts per million)'], 'rows':[['100,000','1.41'],['200,000','1.83'],['300,000','2.43'],['400,000','3.05'],['500,000','3.72']]},
        paragraph(r'Further studies show that a refined formula for the average daily level of carbon monoxide in the air is \(L(p)=0.7\sqrt{p^2+3}\)'),
        paragraph(r'Further assume that the population of a given metropolitan area is growing according to the formula \(p(t)=1+0.02t^3\), where t is the time from now (in years) and p is the population (in hundred thousands). Based on these assumptions, what level of air pollution should be expected in 4 years?'),
        heading('Solution'), paragraph('The level of pollution at time t is given by the composite function:'),
        command(None, r'\(L(p(t))=L(1+0.02t^3)=0.7\sqrt{(1+0.02t^3)^2+3}\), ∵ \(p(t)=1+0.02t^3\)', 'i'),
        paragraph('The air pollution expected in 4 years is obtained by putting t = 4 in equation (i):'),
        paragraph(r'\(L(p(t))=L(1+0.02t^3)=0.7\sqrt{[1+0.02(4)^3]^2+3}\simeq2.0\) ppm'),
        heading('2.3 Inverse of composition of functions'),
        paragraph('“Let y = f(x) be a function of x. This function takes a dependent variable y in response of independent variable x. The function that takes x as dependent variable in response of y as the independent is then called the inverse function of f(x)”.'),
        command(None, r'The inverse function is denoted by \(x=f^{-1}(y)\)', 'i'),
        paragraph(r'The symbol \(f^{-1}(y)\) means the inverse of f and does not mean \(\frac{1}{f}\).'),
        heading('Note'), paragraph('If f(x) is not one-to-one, then f(x) does not have an inverse function.'),
        paragraph(r'For example, if \(y=f(x)\) is one-to-one function, then the inverse of \(y=f(x)\) is the function \(x=f^{-1}(y)\) formed by interchanging the independent and dependent variables x and y for \(y=f(x)\). Thus, if \((a,b)\) is a point on the graph of \(f(x)\), then \((b,a)\) will be a point on the graph of the inverse of \(f(x)\). The domain and range of \(y=f(x)\) are also valid for its inverse function \(x=f^{-1}(y)\).'),
        {'type':'clarification','text':'As sets, the domain of an inverse function equals the range of the original function, and its range equals the original domain. The inverse notation x = f⁻¹(y) uses the original output y as the inverse input.'}
    ]),
    page('019_page_2.jpg', 30, [
        heading('2.3.1 Inverse of the composition of two given functions'),
        heading('Example 6'), paragraph('Find the inverse function of f(t) = 3t − 8.'),
        heading('Solution'), paragraph('The function f(t) takes an output 3t − 8 in response of input t. The inverse function must take an output t in response of input 3t − 8:'),
        command(None, r'\(f^{-1}(3t-8)=t\)', 'i'),
        paragraph(r'If \(z=3t-8\) say, then \(t=\frac{z+8}{3}\). Use these values in equation (i) to obtain: \(f^{-1}(z)=\frac{z+8}{3}\)'),
        paragraph(r'Put t as its argument instead of z to obtain the inverse function of \(f(t)=3t-8\): \(f^{-1}(t)=\frac{t+8}{3}\)'),
        heading('Example 7'), paragraph(r'Let \(f(x)=2x+3\) and \(g(x)=3x\) and \(h(x)=f(g(x))\). Write expressions for the following functions (a) h(x) (b) f⁻¹(x) (c) g⁻¹(x) (d) h⁻¹(x)'),
        heading('Solution'), paragraph('a. In response of f(x) and g(x), the function h(x) is:'),
        paragraph(r'\(h(x)=f(g(x))=f(3x)=2(3x)+3=6x+3\), ∵ g(x) = 3x'),
        paragraph('b. In response of f(x), the inverse of f(x) is:'),
        paragraph(r'\(x=f^{-1}(2x+3)\); \(x=f^{-1}(z)\), \(z=2x+3\Rightarrow x=\frac{z-3}{2}\)'),
        paragraph(r'\(\frac{z-3}{2}=f^{-1}(z)\); \(\frac{x-3}{2}=f^{-1}(x)\), insert x instead of z'),
        paragraph('c. In response of g(x), the inverse of g(x) is:'),
        paragraph(r'\(x=g^{-1}(3x)\); \(x=g^{-1}(z)\), \(z=3x\Rightarrow x=\frac{z}{3}\)'),
        paragraph(r'\(\frac{z}{3}=g^{-1}(z)\); \(\frac{x}{3}=g^{-1}(x)\), insert x instead of z'),
        paragraph('d. In response of h(x), the inverse of h(x) is:'),
        paragraph(r'\(x=h^{-1}(6x+3)\); \(x=h^{-1}(z)\), \(z=6x+3\Rightarrow x=\frac{z-3}{6}\)'),
        paragraph(r'\(\frac{z-3}{6}=h^{-1}(z)\); \(\frac{x-3}{6}=h^{-1}(x)\), insert x instead of z'),
        heading('Facts about Calculus'),
        paragraph('Calculus was discovered as a tool of problem solving. Before the development of calculus, there were a wide range of issues that could not be addressed using the simple mathematics that was available .e.g. people did not know how to measure the speed of different objects when it was changing ever time. Another effective method was desired to calculate the area under the curve. Algebra, geometry, trigonometry and statistics were well understood, but they could not provide necessary tools to address these important issues. Some of the mathematicians of history give the credit to the ancient Greeks for discovering the calculus. But most of the scholars and mathematicians recognize Gottfried Wilhelm von Leibniz and sir, Isaac Newton developed its modern concepts in 17ᵗʰ century. According to the university of Laws Leibniz and Newton held different concept, while Leibniz introduced that the variables of x and y composing “sequences of infinitely close values”. But Newton viewed them as variables that change with time. Leibniz considered calculus as a mathematical science for analysis but Newton took it being geometrical science.')
    ])
]
for source in PAGES:
    source['visualStatus'] = 'All formulas and the carbon-monoxide data table rendered digitally; no instructional image'
    source['alternateVerification'] = {'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':19,'side':'left' if source['page']==29 else 'right','reason':'Full spread restores clipped JPG text and confirms exponents and radical scope.'}
