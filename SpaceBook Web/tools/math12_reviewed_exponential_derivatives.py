"""Printed 91–92, manually verified JPG and full PDF spread 50."""
from math12_reviewed_unit1 import heading,paragraph,page,command
def eq(s):return command(None,'\\('+s+'\\)')
def note(s):return {'type':'clarification','text':s}
PAGES=[page('050_page_1.jpg',91,[
 heading('3.6.1 Derivative of eˣ and aˣ from first principle'),heading('i. Derivative of eˣ'),paragraph(r'If \(y=e^x\), then the derivative by first principle rule is:'),
 eq(r'\frac{dy}{dx}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x},\quad y=f(x)=e^x'),
 eq(r'=\lim_{\Delta x\to0}\frac{e^{x+\Delta x}-e^x}{\Delta x}=\lim_{\Delta x\to0}\frac{e^xe^{\Delta x}-e^x}{\Delta x}'),
 eq(r'=\lim_{\Delta x\to0}\frac{e^x(e^{\Delta x}-1)}{\Delta x}=\lim_{\Delta x\to0}e^x\lim_{\Delta x\to0}\frac{e^{\Delta x}-1}{\Delta x}=e^x(1)=e^x,\quad\lim_{\Delta x\to0}\frac{e^{\Delta x}-1}{\Delta x}=1'),
 heading('ii. Derivative of aˣ'),paragraph(r'If \(y=a^x\), then the derivative by first principle rule is:'),
 eq(r'\frac{dy}{dx}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x},\quad y=f(x)=a^x'),
 eq(r'=\lim_{\Delta x\to0}\frac{a^{x+\Delta x}-a^x}{\Delta x}=\lim_{\Delta x\to0}\frac{a^xa^{\Delta x}-a^x}{\Delta x}'),
 eq(r'=\lim_{\Delta x\to0}\frac{a^x(a^{\Delta x}-1)}{\Delta x}=\lim_{\Delta x\to0}a^x\lim_{\Delta x\to0}\frac{a^{\Delta x}-1}{\Delta x}=a^x\log_ea'),
 eq(r'\lim_{\Delta x\to0}\frac{a^{\Delta x}-1}{\Delta x}=\log_ea=\ln a'),
 heading('3.6.2 Derivative of ln x and logₐ x from first principle'),heading('i. Derivative of ln x'),paragraph('If y = ln x, then the derivative by first principle rule is:'),
 eq(r'\frac{dy}{dx}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x},\quad y=f(x)=\ln x'),
 eq(r'=\lim_{\Delta x\to0}\frac{\ln(x+\Delta x)-\ln x}{\Delta x}=\lim_{\Delta x\to0}\frac1{\Delta x}\ln(\frac{x+\Delta x}x)'),paragraph('Logarithmic — rule'),
 eq(r'=\lim_{\Delta x\to0}\frac{x}x\frac1{\Delta x}\ln(1+\frac{\Delta x}x)'),paragraph('multiply and divide out by x'),
 eq(r'=\lim_{\Delta x\to0}\frac1x\frac{x}{\Delta x}\ln(1+\frac{\Delta x}x)=\lim_{\Delta x\to0}\frac1x\ln(1+\frac{\Delta x}x)^{\frac{x}{\Delta x}}=\frac1x\ln e=\frac1x'),
 eq(r'\lim_{\Delta x\to0}(1+\frac{\Delta x}x)^{\frac{x}{\Delta x}}=e'),
 heading('ii. Derivative of logₐ x'),paragraph('If y = logₐ x, then the derivative by first principle rule is:'),
 eq(r'\frac{dy}{dx}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x},\quad y=f(x)=\log_ax'),
 eq(r'=\lim_{\Delta x\to0}\frac{\log_a(x+\Delta x)-\log_ax}{\Delta x}=\lim_{\Delta x\to0}\frac1{\Delta x}\log_a(\frac{x+\Delta x}x)=\lim_{\Delta x\to0}\frac1{\Delta x}\log_a(1+\frac{\Delta x}x)'),
 eq(r'=\lim_{\Delta x\to0}\frac{x}x\frac1{\Delta x}\log_a(1+\frac{\Delta x}x)'),paragraph('multiply and divide out by x'),
 eq(r'=\frac1x\lim_{\Delta x\to0}\frac{x}{\Delta x}\log_a(1+\frac{\Delta x}x)=\frac1x\lim_{\Delta x\to0}\log_a(1+\frac{\Delta x}x)^{\frac{x}{\Delta x}}=\frac1x\log_ae'),
 eq(r'\lim_{\Delta x\to0}(1+\frac{\Delta x}x)^{\frac{x}{\Delta x}}=e'),
 note('For real exponentials, a > 0; a = 1 yields the constant function and zero derivative. For logarithms require x > 0 and a > 0, a ≠ 1. Also logₐe = 1/ln a. The logarithm limit is evaluated for fixed positive x and sufficiently small Δx, so x + Δx remains positive. These proofs use the standard exponential limit and logarithm continuity; they do not derive those prerequisites here.')
]),page('050_page_2.jpg',92,[
 heading('These exponential and logarithmic formulas are listed in the box:'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(e^x)=e^x\)',r'ii. \(\frac{d}{dx}(a^x)=a^x\log_ea\)',r'iii. \(\frac{d}{dx}(\ln x)=\frac1x\)',r'iv. \(\frac{d}{dx}(\log_ax)=\frac1x\log_ae\)']},
 paragraph('The chain rule can be used to derive the generalization of the power rule and the rules for differentiating the exponential and logarithmic functions, as summarized in the box:'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(e^u)=e^u\frac{du}{dx}\)',r'ii. \(\frac{d}{dx}(a^u)=a^u\log_ea\frac{du}{dx}\)',r'iii. \(\frac{d}{dx}(\ln u)=\frac1u\frac{du}{dx}\)',r'iv. \(\frac{d}{dx}(\log_au)=\frac1u\log_ae\frac{du}{dx}\)']},
 heading('19'),paragraph(r'Differentiate the following functions: (a) \(f(x)=7^{4-3x^5}\); (b) \(f(x)=\log_{10}\sqrt{x^2-7x}+x^3\); (c) \(f(x)=\ln(e^{mx}+e^{-mx})\); (d) \(f(x)=\frac{e^{2x}}{\ln x}\).'),heading('Solution'),
 paragraph(r'a. If the given function is \(f(x)=7^{4-3x^5}\), then the derivative of the given function w.r.t. x is:'),
 eq(r'\frac{dy}{dx}=\frac{d}{dx}[7^{4-3x^5}]'),paragraph('Let'),eq(r'u=4-3x^5\quad\Rightarrow\quad\frac{du}{dx}=-15x^4'),paragraph('Now,'),eq(r'y=7^u\quad\Rightarrow\quad\frac{dy}{du}=\frac{d}{du}(7^u)=7^u\log_e7'),paragraph('By using chain rule'),eq(r'\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}=7^u\log_e7(-15x^4)=-15x^4\,7^{4-3x^5}\log_e7'),
 paragraph(r'b. If the given function is \(f(x)=\log_{10}\sqrt{x^2-7x}+x^3\), then the derivative of the given function w.r.t. x is:'),
 eq(r'\frac{df}{dx}=\frac{d}{dx}[\log_{10}\sqrt{x^2-7x}]+\frac{d}{dx}(x^3)=\frac1u\log_{10}e\frac{du}{dx}+3x^2,\quad u=\sqrt{x^2-7x}'),
 eq(r'=\frac1{2(x^2-7x)}\log_{10}e\frac{d}{dx}(x^2-7x)+3x^2=\frac{2x-7}{2(x^2-7x)}\log_{10}e+3x^2'),
 paragraph(r'c. If the given function is \(f(x)=\ln(e^{mx}+e^{-mx})\), then the derivative of the given function w.r.t. x is:'),
 eq(r'\frac{df}{dx}=\frac{d}{dx}[\ln(e^{mx}+e^{-mx})]=\frac{d}{du}(\ln u)\frac{d}{dx}(e^{mx}+e^{-mx}),\quad u=e^{mx}+e^{-mx}'),
 eq(r'=\frac1{\ln u}(me^{mx}-me^{-mx})=\frac1{\ln(e^{mx}+e^{-mx})}m(e^{mx}-e^{-mx})=\frac{m(e^{mx}-e^{-mx})}{\ln(e^{mx}+e^{-mx})}'),
 note(r'The printed part (c) differentiates ln u as 1/ln u, conflicting with the correct rule 1/u in the box above. For real constant m, the correct derivative is \(\frac{m(e^{mx}-e^{-mx})}{e^{mx}+e^{-mx}}\). The sum of exponentials is positive for every real x.'),
 paragraph(r'd. If the given function is \(f(x)=\frac{e^{2x}}{\ln x}\), then the derivative of the given function w.r.t. x is:'),
 eq(r'\frac{df}{dx}=\frac{\frac{d}{dx}[e^{2x}]\ln x-e^{2x}\frac{d}{dx}[\ln x]}{(\ln x)^2}=\frac{e^{2x}\frac{d}{dx}(2x)\ln x-\frac{e^{2x}}x}{(\ln x)^2}'),
 eq(r'=\frac{2e^{2x}\ln x-\frac1xe^{2x}}{(\ln x)^2}=\frac{2xe^{2x}\ln x-e^{2x}}{x(\ln x)^2}=\frac{e^{2x}(2x\ln x-1)}{x(\ln x)^2}'),
 note('Part (a) is defined for every real x. Part (b) requires x² − 7x > 0, so x < 0 or x > 7. Part (d) requires x > 0 and x ≠ 1; the logarithm in its denominator must be nonzero.')
])]
PAGES.append(page('051_page_1.jpg',93,[
 heading('3.6.3 Use of logarithmic differentiation to algebraic expressions involving product, quotient and power'),paragraph('Logarithmic differentiation is a procedure in which logarithms are used to trade the task of differentiating products and quotients for that of differentiating sums and differences. It is especially valuable as a means for handling complicated product or quotient functions and power functions where variables appear in both the base and the exponent.'),
 heading('Example 20'),paragraph(r'Differentiate the following functions: (a) \(y=\ln\left[\frac{x(x^2-3)^2}{\sqrt{x^2-4}}\right]\); (b) \(y=x^{\sin x}\).'),heading('Solution'),
 paragraph(r'a. \(y=\ln\left[\frac{x(x^2-3)^2}{\sqrt{x^2-4}}\right]\). If the given function after simplification is:'),
 eq(r'y=\ln\left[\frac{x(x^2-3)^2}{(x^2-4)^{1/2}}\right]=\ln[x(x^2-3)^2]-\ln[(x^2-4)^{1/2}]'),paragraph('logarithms rules'),
 eq(r'=\ln x+\ln(x^2-3)^2-\ln(x^2-4)^{1/2}=\ln x+2\ln(x^2-3)-\frac12\ln(x^2-4)'),paragraph('The derivative of y w.r.t. x is:'),
 eq(r'\frac{dy}{dx}=\frac{d}{dx}\left[\ln x+2\ln(x^2-3)-\frac12\ln(x^2-4)\right]=\frac{d}{dx}[\ln x]+2\frac{d}{dx}[\ln(x^2-3)]-\frac12\frac{d}{dx}[\ln(x^2-4)]'),
 eq(r'=\frac1x+2\frac1{x^2-3}(2x)-\frac12\frac1{x^2-4}(2x)=\frac{4x^4-20x^2+12}{x(x^2-3)(x^2-4)}=\frac{4(x^4-5x^2+3)}{x(x^2-3)(x+2)(x-2)}'),
 paragraph(r'b. \(y=x^{\sin x}\). Taking ln of both sides:'),eq(r'\ln y=\ln(x^{\sin x}),\quad\ln y=\sin x\ln x'),paragraph('Then on differentiation w.r.t. x it becomes:'),
 eq(r'\frac{d}{dx}(\ln y)=\frac{d}{dx}(\sin x\ln x)'),eq(r'\frac1y\frac{dy}{dx}=\sin x\frac{d}{dx}(\ln x)+\ln x\frac{d}{dx}(\sin x)'),eq(r'\frac1y\frac{dy}{dx}=\frac{\sin x}x+\ln x\cos x'),
 eq(r'\frac{dy}{dx}=y\left[\frac{\sin x}x+\ln x\cos x\right]=x^{\sin x}\left[\frac{\sin x}x+\ln x\cos x\right]'),
 note('For part (a), the denominator requires |x| > 2 and the logarithm argument must be positive. Since (x² − 3)² and the denominator are positive there, its sign is the sign of x, giving the original real domain x > 2. All separated logarithms are valid on that domain. For part (b), use x > 0 to define the differentiable real power x^(sin x) = exp(sin x ln x).'),
 heading('3.7 Differentiation of Hyperbolic and Inverse Hyperbolic Functions'),paragraph('The concept of hyperbolic functions is completely discussed in Unit-2. The differentiation of hyperbolic functions can be found as follows:')
]))
for p in PAGES:
 p['title']='DIFFERENTIATION';p['visualStatus']='Complete exponential/logarithmic first-principles proofs, formula boxes and Example 19 mathematics rendered digitally'
 p['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':(p['page']+9)//2,'side':'left' if p['page']%2 else 'right','reason':'Checks log bases, source exponents, radical extent, logarithmic differentiation and incorrect printed 1/ln u derivative in Example 19(c).'}
EXAMPLES=[{'id':'we-3-source-19','num':'19','title':'Example 19','problem':r'Differentiate (a) \(7^{4-3x^5}\); (b) \(\log_{10}\sqrt{x^2-7x}+x^3\); (c) \(\ln(e^{mx}+e^{-mx})\); (d) \(e^{2x}/\ln x\).','given':'m is a real constant. Check the domains of logarithms before differentiating.','method':'Chain, sum and quotient rules with d(ln u)/dx = u′/u.','steps':[r'(a) Set u = 4 − 3x⁵, so u′ = −15x⁴. The derivative of 7ᵘ is 7ᵘ ln7 times u′. Thus f′ = −15x⁴7^(4 − 3x⁵)ln7 for every real x.',r'(b) Let q = x² − 7x. The logarithm of √q requires q > 0, giving x < 0 or x > 7. Since log₁₀√q = (ln q)/(2ln10), its derivative is q′/(2q ln10).',r'Add the cubic derivative: f′ = (2x − 7)/[2(x² − 7x)ln10] + 3x², on that original domain.',r'(c) Set u = e^(mx) + e^(−mx), with u′ = m e^(mx) − m e^(−mx). The sum u is positive for all real x.',r'The logarithm chain rule gives f′ = u′/u = m[e^(mx) − e^(−mx)]/[e^(mx) + e^(−mx)]. The printed denominator ln u is incorrect. At m = 0 the function is ln2 and its derivative is zero.',r'(d) Set N = e^(2x) and D = ln x. Then N′ = 2e^(2x) and D′ = 1/x. Require x > 0 and x ≠ 1.',r'Quotient rule gives f′ = [2e^(2x)ln x − e^(2x)/x]/(ln x)² = e^(2x)(2x ln x − 1)/[x(ln x)²].',r'Check part (c) independently as ln(2cosh(mx)); differentiation yields m tanh(mx), identical to the exponential ratio. No sign or branch restriction is needed for real m and x.'],'answer':r'(a) −15x⁴7^(4 − 3x⁵)ln7. (b) (2x − 7)/[2(x² − 7x)ln10] + 3x². (c) m[e^(mx) − e^(−mx)]/[e^(mx) + e^(−mx)]. (d) e^(2x)(2x ln x − 1)/[x(ln x)²], with the domains stated above.','sourceClarification':'The source differentiates ln u as 1/ln u in part (c); the correct derivative is 1/u, already printed in its formula box.','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':92,'jpg':'050_page_2.jpg','verification':'complete question and source solution visually compared with JPG and full PDF'}]}]
EXAMPLES.append({'id':'we-3-source-20','num':'20','title':'Example 20','problem':r'Differentiate (a) \(y=\ln\left[\frac{x(x^2-3)^2}{\sqrt{x^2-4}}\right]\); (b) \(y=x^{\sin x}\).','given':'A logarithm of a quotient and a positive-base variable power.','method':'Expand valid logarithms and differentiate; use logarithmic differentiation for the variable power.','steps':[r'(a) Require x² − 4 > 0. The denominator and squared factor are positive, so the logarithm argument has the sign of x. The real domain is x > 2.',r'On this domain, y = ln x + 2ln(x² − 3) − (1/2)ln(x² − 4). Every logarithm argument is positive.',r'Differentiate term by term: y′ = 1/x + 4x/(x² − 3) − x/(x² − 4).',r'The common denominator x(x² − 3)(x² − 4) gives numerator (x² − 3)(x² − 4) + 4x²(x² − 4) − x²(x² − 3) = 4x⁴ − 20x² + 12.',r'Hence y′ = 4(x⁴ − 5x² + 3)/[x(x² − 3)(x² − 4)], for x > 2. Factoring x² − 4 gives the equivalent source denominator x(x² − 3)(x + 2)(x − 2).',r'(b) For x > 0, define y = exp(sin x ln x), so y > 0 and ln y = sin x ln x.',r'Differentiate: y′/y = cos x ln x + sin x/x. Multiply by y to obtain y′ = x^(sin x)[cos x ln x + sin x/x].',r'Independent check: differentiating exp(sin x ln x) directly with the chain rule yields the same result. Negative-base variable real powers do not provide the open real domain assumed by this logarithmic method.'],'answer':r'(a) \(\frac{4(x^4-5x^2+3)}{x(x^2-3)(x^2-4)}\), x > 2. (b) \(x^{\sin x}[\cos x\ln x+\frac{\sin x}x]\), x > 0.','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':93,'jpg':'051_page_1.jpg','verification':'complete question and source solution visually compared with JPG and full PDF'}]})
