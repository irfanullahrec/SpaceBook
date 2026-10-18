"""Printed page 53, visually checked against JPG and full PDF physical page 31 left."""
from math12_reviewed_unit1 import paragraph, command, page

PAGES=[page('031_page_1.jpg',53,[
    paragraph('Taking limit y → 0, when x → 0:'),
    command(None,r'\(\lim_{x\to0}\frac{a^x-1}{x}=\lim_{y\to0}\frac{y}{\frac{\log(1+y)}{\log a}}=\lim_{y\to0}\frac{1}{\frac{1}{y}\log(1+y)\left(\frac{1}{\log a}\right)}=\lim_{y\to0}\frac{\log a}{\log(1+y)^{\frac{1}{y}}}\)'),
    command(None,r'\(=\log a\frac{1}{\log\lim_{y\to0}(1+y)^{\frac{1}{y}}}=\log a\frac{1}{\log e}=\log_e a=\ln a\)'),
    paragraph('By replacing ‘a’ with ‘e’ the following result can be deduced.'),command(None,r'\(\lim_{x\to0}\frac{e^x-1}{x}=\ln e=1\)'),
    {'type':'clarification','text':r'Here \(\log(1+y)^{1/y}\) means the logarithm of \((1+y)^{1/y}\), as follows from the preceding log power rule. All logs in the change-of-base calculation use the same fixed base. Since \((1+y)^{1/y}\to e\) and log is continuous at e, the result is log a / log e = ln a. The case a = 1 was handled separately on page 52.'},
    command('c. Prove that',r'\(\lim_{x\to0}\frac{\sqrt{x+a}-\sqrt{a}}{x}=\frac{1}{2\sqrt{a}}\)'),command('Proof: We have to show that:',r'\(\lim_{x\to0}\frac{\sqrt{x+a}-\sqrt{a}}{x}=\frac{1}{2\sqrt{a}}\)'),
    command('Take L.H.S.',r'\(\lim_{x\to0}f(x)=\lim_{x\to0}\frac{\sqrt{x+a}-\sqrt{a}}{x}=\frac{\sqrt{0+a}-\sqrt{a}}{0}=\frac{0}{0}\text{ which is undefined.}\)'),paragraph('Now, rationalize the function f(x),'),
    command(None,r'\(f(x)=\left(\frac{\sqrt{x+a}-\sqrt{a}}{x}\right)\left(\frac{\sqrt{x+a}+\sqrt{a}}{\sqrt{x+a}+\sqrt{a}}\right)\)'),command(None,r'\(=\frac{x+a-a}{x(\sqrt{x+a}+\sqrt{a})}=\frac{x}{x(\sqrt{x+a}+\sqrt{a})}\)'),
    command(None,r'\(\Rightarrow\quad\lim_{x\to0}f(x)=\lim_{x\to0}\frac{1}{\sqrt{x+a}+\sqrt{a}}\)'),command(None,r'\(=\frac{1}{\sqrt{0+a}+\sqrt{a}}=\frac{1}{2\sqrt{a}}=\text{R.H.S.}\)'),
    {'type':'clarification','text':'The stated finite real limit requires a > 0. Rationalization cancels x only for x ≠ 0, which is sufficient for the limit. At a = 0, the real-domain right-hand quotient is √x/x = 1/√x and tends to +∞, so there is no finite limit. For a < 0, √a is not real. The substitution 0/0 is indeterminate; the displayed rationalization evaluates the limit without assigning a value to 0/0.'},
    command('d. Prove that',r'\(\lim_{x\to0}\frac{(1+x)^n-1}{x}=n\)'),paragraph(r'Proof: If we put \((1+x)^n-1=z\); then: \((1+x)^n-1=z\)'),command(None,r'\(\Rightarrow\quad(1+x)^n=(1+z)\)'),paragraph('Taking log of both sides to obtain:'),command(None,r'\(\log(1+x)^n=\log(1+z)\)'),command(None,r'\(n\log(1+x)=\log(1+z)\)'),paragraph('Use these expressions in the left-hand side of the limit to obtain the right-hand side:'),
    command(None,r'\(\frac{(1+x)^n-1}{x}=\frac{z}{x}=\frac{z}{x}\frac{\log(1+z)}{\log(1+z)}=\frac{z}{\log(1+z)}\frac{n\log(1+x)}{x}=\frac{1}{\log(1+z)^{\frac{1}{z}}}\,n\log(1+x)^{\frac{1}{x}}\)'),paragraph('Taking limit z → 0, when x → 0:'),command(None,r'\(\lim_{x\to0}\frac{(1+x)^n-1}{x}=\lim_{z\to0}\frac{1}{\log(1+z)^{\frac{1}{z}}}\lim_{x\to0}n\log(1+x)^{\frac{1}{x}}=\frac{1}{\log e}\,n\log e=n\)'),
    {'type':'clarification','text':'For any fixed real n, work near 0 with 1 + x > 0. If n ≠ 0 and x ≠ 0, then z ≠ 0 and log(1 + z) ≠ 0, so the displayed divisions are valid. As x tends to 0, z tends to 0, and both logarithms of the displayed power expressions tend to log e. If n = 0, the numerator is identically zero and the quotient is 0 for x ≠ 0, so its limit is 0 directly.'}
])]
for block in PAGES[0]['blocks']:
    if block['type']=='command': block['prompt']=False
PAGES[0]['visualStatus']='All logarithmic, rationalization and power-limit proof steps rendered as digital mathematics; no source illustration on this page'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':31,'side':'left','reason':'Restores clipped log change-of-base expressions, square-root denominators and the complete power-limit proof.'}
PAGES[0]['sourceNotes']=['Completes the logarithmic substitution proof begun on page 52. The next page introduces the sandwich theorem and the sine limit.']
