"""Printed page 35, checked against JPG and full PDF physical page 22, left."""
from math12_reviewed_unit1 import heading, paragraph, command, page

PAGES = [page('022_page_1.jpg',35,[
    heading('a. Common Logarithms'),
    paragraph(r'Common Logarithms are logarithms with base 10: \(y=\log_{10}x\) means \(10^y=x\)'),
    paragraph('“Log x”, which is read “the logarithm of x”, is the answer to the question “to what exponent must 10 be raised to produce x?”'),
    heading('Example 9'), paragraph(r'Evaluate the following logarithmic functions: (a). log 10000 (b). log .01 (c). \(\log\sqrt{10}=\frac{1}{2}\)'),
    heading('Solution'),
    paragraph(r'This is equal to: \(\log10000=\log10^4=4\log10=4\)'),
    paragraph(r'This is equal to: \(\log .01=\log\frac{1}{100}=\log(10)^{-2}=-2\log10=-2\)'),
    paragraph(r'c. This is equal to: \(\log\sqrt{10}=\log(10)^{\frac{1}{2}}=\frac{1}{2}\log10=\frac{1}{2}\)'),
    heading('Do You Know?'), paragraph('The common logarithm is also called Briggsian logarithms and the natural logarithm is also called Napierian logarithms.'),
    heading('b. Natural Logarithms'),
    paragraph(r'Natural Logarithms are logarithms with base e: \(y=\ln x\) means \(e^y=x\)'),
    paragraph('“ln x”, which is read “the el-en of x”, is the answer to the question “to what exponent must e be raised to produce x?”'),
    paragraph(r'\(y=\log_b x\) means \(b^y=x\)'),
    paragraph('“y = log_b x”, which is read “y is the logarithm of x to the base b”, is the answer to the question “to what power must b be raised to produce x?”'),
    heading('Logarithmic Notation'),
    paragraph(r'Common logarithmic: \(\log x=\log_{10}x\). Natural logarithmic: \(\ln x=\log_e x\)'),
    heading('Logarithmic–Exponential Relationships'),
    {'type':'dataTable','headers':['Logarithmic notation','Equivalent exponential notation'],'rows':[[r'\(\log x=y\)',r'\(x=10^y\)'],[r'\(\ln x=y\)',r'\(x=e^y\)']]},
    heading('Properties of Logarithms'),
    paragraph('If b, M and N are positive real numbers b ≠ 1, and p and x are also any positive real numbers, then:'),
    {'type':'list','items':[
        r'i. \(\log_b1=0\)', r'ii. \(\log_b b=1\)', r'iii. \(\log_b b^x=x\)', r'iv. \(b^{\log_b x}=x\), x > 0',
        r'v. \(\log_b MN=\log_b M+\log_b N\)',r'vi. \(\log_b\frac{M}{N}=\log_b M-\log_b N\)',
        r'vii. \(\log_b M^p=p\log_b M\)',r'viii. \(\log_b M=\log_b N\), M = N'
    ]},
    heading('Example 10'), paragraph(r'Find x to four decimal places for the following indicated exponential functions: (a). \(10^x=2\) (b). \(e^x=3\)'),
    heading('Solution'),
    paragraph(r'a. \(10^x=2\); \(\log10^x=\log2\), log of both sides; \(x\log10=\log2\), ∵ log 10 = 1; x = 0.3010'),
    paragraph(r'b. \(e^x=3\); \(\ln e^x=\ln3\), ln of both sides; \(x\ln e=\ln3\), ∵ ln e = 1; x = 1.0986'),
    heading('Example 11'), paragraph('Two people with the covid-19 positive visited the campus of Peshawar University. The number of days T that it took for the corona virus to infect n people is given by'),
    command(None,r'\(T(n)=-1.43\ln\left(\frac{10,000-n}{4998n}\right)\)'),
    paragraph('How many days will it take for the virus to infect a. 500 people? b. 5000 people?')
])]
PAGES[0]['visualStatus']='All logarithmic rules, relationships and numerical examples rendered digitally; no instructional image'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':22,'side':'left','reason':'Full spread confirms logarithm bases, fractional exponents, property labels and Example 11 denominator 4998n.'}
PAGES[0]['sourceNotes']=['Part (c) of Example 9 prints its result in the question itself; retained in the source transcription.','Example 11 question is on this page and its solution continues on printed page 36; both have been visually reviewed together.']
