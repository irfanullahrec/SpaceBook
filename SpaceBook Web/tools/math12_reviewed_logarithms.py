"""Printed page 34, compared with JPG and full PDF physical page 21, right."""
from math12_reviewed_unit1 import heading, paragraph, command, page

PAGES = [page('021_page_2.jpg',34,[
    paragraph('Interestingly, the value of expression (i) is never close to 1, but seems to be approaching a number close to 2.7183. In fact, as x increases without bound, the value of expression (i) approaches an irrational number that we call e. The irrational number e to twelve decimal places is:'),
    paragraph('e = 2.718 281 828 459'),
    heading('Example 8'), paragraph('Cholera, an intestinal disease, is caused by a cholera bacterium that multiplies exponentially by cell division as given approximately by'),
    command(None,r'\(N=N_0e^{1.386t}\)'),
    paragraph('with N is the number of bacteria present after t hours and N₀ is the number of bacteria present at the start (t = 0). If we start with 25 bacteria, how many bacteria (to the nearest unit) will be present in (a) 1 hour? (b) 3 hours? (c) 4 hours? (d) Interpret'),
    heading('Solution'), paragraph('Use the amount of initial bacteria N₀ = 25 in the given equation to obtain:'),
    command(None,r'\(N=25e^{1.386t}\), N₀ = 25','i'),
    paragraph('a. The bacteria at a time t = 1 hour is obtained by putting t = 1 in equation (i):'),
    paragraph(r'\(N=25e^{1.386(1)}=99.97\) bacteria'),
    paragraph('b. The bacteria at a time t = 3 hours is obtained by putting t = 3 in equation (i):'),
    paragraph(r'\(N=25e^{1.386(3)}=1599\) bacteria'),
    paragraph('c. The bacteria at a time t = 4 hours is obtained by putting t = 4 in equation (i):'),
    paragraph(r'\(N=25e^{1.386(4)}=6392\) bacteria'),
    paragraph('d. Thus, we conclude that the population of bacteria is growing when time t increases.'),
    {'type':'diagram','id':'math12-source-figure-2-6','caption':'Figure 2.6','diagram':{'type':'source-function-graph','title':r'\(f(x)=25e^{1.386x}\)','xMin':0,'xMax':5,'yMin':0,'yMax':10000,'xTicks':[0,1,2,3,4,5],'yTicks':[2000,4000,6000,8000,10000],'yGridStep':1000,'exponential':{'initial':25,'rate':1.386},'xLabel':'Time hours','yLabel':'N'}},
    {'type':'clarification','text':'The question asks for the nearest unit. The printed one-hour result 99.97 rounds to 100 bacteria. With the printed rate 1.386, the three-hour and four-hour values round to 1599 and 6392 respectively.'},
    heading('v. Logarithmic Functions'),
    paragraph('Logarithms are an alternative way of writing expressions which involve powers or indices. They are used extensively in the study of sound. The decimals used in defining the intensity of sound, is based on a logarithmic scale.'),
    paragraph('Until the development of computers and calculators, logarithms were the only effective tool for large scale numerical computations. They are no longer needed for this, but it still plays a crucial role in many applications.'),
    paragraph(r'For illustration, if we start with the exponential function y = f(x) defined by \(y=2^x\) then the interchange of the variables is giving the inverse of \(y=2^x\):'),
    paragraph(r'\(x=2^y\)'),
    paragraph('We call this inverse exponential function, the logarithmic function with base 2, and write this as:'),
    command(None,r'\(y=\log_2 x\) if and only if \(x=2^y\)','i'),
    paragraph(r'“The inverse of an exponential function is called a logarithmic function. For b > 0 and b ≠ 1, the logarithmic function is: \(y=\log_b x\), which is equivalent to \(x=b^y\).”'),
    paragraph('The log to the base b of x is the exponent to which b must be raised to obtain x. The domain of the logarithmic function is the set of all positive real numbers, which is also the range of the corresponding exponential function. Obviously, the range of the logarithmic function is the set of all real numbers, which is also the domain of the corresponding exponential function.'),
    paragraph('Typical graphs of an exponential function and its inverse, a logarithmic are shown in the Figure 2.7.'),
    {'type':'diagram','id':'math12-source-figure-2-7','caption':'Figure 2.7','diagram':{'type':'source-exponential-log-pair','title':'Exponential and logarithmic inverse functions','base':2}},
    {'type':'clarification','text':'Figure 2.7 labels the general base b > 1 without giving a numerical value. This digital illustration uses b = 2 from the preceding explanation and shows the inverse curves reflected across y = x. The source labels remain general.'}
])]
PAGES[0]['visualStatus']='Figure 2.6 recreated from printed equation and scale; Figure 2.7 digitally illustrated using representative base 2 because the source specifies only b > 1'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':21,'side':'right','reason':'Sharper spread confirms exponent 1.386t, printed numerical results and logarithmic inverse notation.'}
PAGES[0]['sourceNotes']=['The one-hour result is not rounded to the nearest unit in the printed solution; preserve it and label the learning correction.','Figure 2.7 specifies a general base b > 1, not a numerical base; digital base choice is explicitly disclosed.']
