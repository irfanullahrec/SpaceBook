"""Manual transcription from reviewed JPG pages, not Word OCR.

JPG edge clipping on printed page 3 was resolved against full PDF page 6,
left-hand page. The split PDF repeats the cropped JPG and cannot resolve it.
"""

def heading(text):
    return {"type": "heading", "text": text}

def paragraph(text):
    return {"type": "paragraph", "text": text}

def command(text, result=None, number=None):
    return {"type": "command", "text": text, "result": result, "number": number}

def figure(name, caption, alt):
    return {"type": "figure", "src": "assets/math12/" + name + ".jpg", "caption": caption, "alt": alt}

def page(file, number, blocks, defects=None):
    return {"file": file, "page": number, "title": "INTRODUCTION TO SYMBOLIC PACKAGE, MAPLE", "paragraphs": [], "blocks": blocks, "sourceDefects": defects or [], "visualStatus": "software screenshots preserved as cropped figures; equations rendered digitally"}

PAGES = [
    page("005_page_2.jpg", 2, [
        heading("A. Getting started with Maple"),
        paragraph("The maple software runs on different systems and platforms. It depends on the platform and system. It is convenient to use if you have windows based operating system (installed maple software package 14, 18 or any latest package)."),
        paragraph("When a maple session is started, the maple prompt command (>) is displayed like |>.") ,
        figure("figure-1-1", "Figure 1.1 Maple start menu", "Maple start screen with task icons and the palettes sidebar"),
        paragraph("This prompt-character will show at the upper left of the worksheet indicates that maple is waiting to receive input in the form of maple statement."),
        paragraph('When you are finished with the maple session, you will leave the program by selecting "Exit" under the file menu (upper left of the maple tools bar) as shown in Figure 1.2.'),
        figure("figure-1-2", "Figure 1.2", "Maple File menu with Exit selected, beside a worksheet containing a plotted parabola"),
        heading("1.1.2 Recognition of basic MAPLE commands"),
        paragraph("A MAPLE command is a statement of calculation followed by a semicolon or a colon. Following are some commands followed by the displayed results.")
    ]),
    page("006_page_1.jpg", 3, [
        paragraph('Enter the commands on your worksheet and verify the given results. When you get to "Save the file", select "Save" under the "File" menu or use CTRL-S to save your working. For example,'),
        command("7 + 17;", "24", 1), command(r"12^2 + 15*2 - 3;", "171", 2), command("12 + 4*(6 + 1 - 10);", "0", 3),
        heading("Remember"),
        paragraph("If you do not include a semicolon or colon at the end of a command, MAPLE will interpret the next command line as a continuation of the previous command."),
        paragraph("The symbol +, -, *, / and ^ (or **) denote addition, subtraction, multiplication, division and exponential (4^2 = 4**2 = 4² = 16)."),
        paragraph("When a string of operations are specified in a command, MAPLE first does exponentiations then multiplication and divisions, then additions and subtractions. To change the order, we use parentheses."),
        heading("i. Save command:"),
        paragraph("To save a variable in our current MAPLE session to a file, type the following at the command prompt."),
        command('Save variablename, "Filename.m";'),
        paragraph("Replace the variable name with your variable name and replace the file name with your file name, but keep .m extension."),
        paragraph("The Save command saves the variable as a MAPLE assignment statement. If the value of your variable depends on other variables, you must save them as well."),
        paragraph("You can save more than one variable by giving all variable names to the save command."),
        command('Save variablename1, variablename2, variablename3, "filename.m";'),
        heading("ii. Editing commands:"),
        paragraph("If you make a mistake in a command or want to change a command, you can go back and edit the command."),
        heading("iii. Exact arithmetic and floating-point (evalf) commands:"),
        paragraph("MAPLE calculates fractions (exact arithmetic) unless you specify that you want decimals (floating-point arithmetic) with the evalf function."),
        paragraph('("evalf" stands for "evaluate using floating-point arithmetic").'),
        command(r"\(\frac{27}{29}+\frac{14}{29}-\frac{4}{29};\)", r"\(\frac{37}{29}\)", 4),
        command(r"\(evalf(\frac{27}{29}+\frac{14}{29}-\frac{4}{29},4);\)", "1.276", 5),
        paragraph("The argument 4 in the evalf command specifies the number of significant figures you want in the result. If you omit this command, you will get ten significant figures:"),
        command(r"\(evalf(\frac{27}{29}+\frac{14}{29}-\frac{4}{29});\)", "1.275862069", 6)
    ]),
    page("006_page_2.jpg", 4, [
        heading("iv. Maple internal memory clearing command:"),
        paragraph("To clear the internal memory during a maple session. We use 'restart' command or click the restart icon on the tool bar of the worksheet. e.g."),
        command("restart"),
        paragraph("when you enter this command, the maple session returns to its startup state. All the values reset to their initial values."),
        heading("v. Enlistment of variables:"),
        paragraph("Use the colon-equal symbol (:=) to define variables that is, to assign values to them. Once you have defined a variable, simply typing its name will show its value, and using the name in a formula will cause the value to be substituted. For example,"),
        command("A := 25; B := 145;", "A := 25\nB := 145", 7),
        paragraph("If you want to string commands together on the same line, then:"),
        command("A := 5; B := 10; C := 12;", "A := 5\nB := 10\nC := 12", 8),
        command("2*A + 4*B + 5*C;", "110", 9),
        command(r"\(\frac{4\cdot A}{B};\)", "2", 10),
        heading("1.1.3 Use of MAPLE as a calculator"),
        paragraph('You click-start, then select-program <Maple 18 <click-"Maple Calculator" to obtain:'),
        heading("(a) Maplesoft (TM) Graphing Calculator Overview"),
        paragraph("This graphical scientific calculator is available for use as part of your Maple(TM) installation or via a Web Server running MapleNet(TM). This calculator use Maple for calculations."),
        heading("On toolbar,"),
        {"type": "list", "items": [
            'use the "setting tab" to control the basic computation settings for the calculator.',
            'use the "Math tab" to select the functions to apply, from basic functions to linear algebra to statistics.',
            'use the "Graph tab" to control how graphs are displayed and what they display.',
            'use the "Data tab" to control the data used to produce a graph or the data to be tabulated directly.',
            'use the "Variable tab" to control the variables you have assigned and their values.',
            'To involve the graphical calculator, use your mouse to press the "Math tab" and select functions to apply. This will build your expression in the input area, which is just below the session history area on the left side of the calculator. When you are ready to evaluate your expression, press ENTER key on your keyboard. Alternatively, you can press the "Graph button", to graph the expression, or the "data button", to tabulate values for the expression.'
        ]},
        heading("Example 1"),
        paragraph(r"Differentiate \(f(x)=x^2+4x+4\) with respect to x at a point x = 2. The steps required for obtaining the graphing-calculator result are:"),
        heading("Solution"),
        paragraph("Click-Math tab < Click-Calculus < Click-Differentiate to obtain:")
    ]),
    page("007_page_1.jpg", 5, [
        command("Diff()"),
        paragraph(r'Cursor “1” requires A: the expression \(x^2+4x+4\), X: the differentiation of \(f(x)\) with respect to x and P: the differentiation of \(f(x)\) at a point x=2.'),
        command("Diff(A,X,P)"), command(r"Diff(\(x^2+4x+4\),x,2)"), paragraph("Click-ENTER"), command("", "8"),
        heading("Example 2"),
        paragraph(r"Integrate \(x^2+4x+4\), with respect to x over the interval [0,1]. The graphing – calculator result is as under:"),
        heading("Solution"), command("Int(1)"),
        paragraph(r'Cursor “1” requires A: the function \(x^2+4x+4\), X: the integration of \(f(x)\) with respect to x, P: the lower limit x = 0 and Q: the upper limit x = 1 of the integral.'),
        command("Int(A,X,P,Q)"), command(r"Int(\(x^2+4x+4\),x,0,1)", "6.333333"),
        heading("(b) Unit calculator"), paragraph("To use maple as a calculator simply type in your worksheet command prompt e.g."),
        command("? Assistant calculator"),
        figure("figure-1-3", "Figure 1.3", "Maplesoft Units Calculator with input and output unit selectors"),
        paragraph("Then you will see the unit calculator as shown in the Figure 1.3."),
        heading("1.1.4 Online MAPLE help"),
        paragraph("You can get help with MAPLE syntax by using the HELP menu, as described previously. If you have a question about a particular command, you can quickly get help by typing a question mark followed by the name (no semicolon). For example,"),
        command("? Addition"),
        paragraph('will open a window containing information about what the “addition” does and how to use it as shown in Figure 1.4. Click on the little “Cross” box at the upper left of the window to close down the little window.')
    ]),
    page("007_page_2.jpg", 6, [
        figure("figure-1-4", "Figure 1.4", "Maple help window describing arithmetic operators"),
        heading("1.2 Polynomials"),
        paragraph("We are familiar about polynomials since our previous grades. The factorization of a polynomial, expansion of an expression can be solved through direct MAPLE commands and context menus."),
        heading("1.2.1 Use of MAPLE commands for factoring a polynomial"),
        heading("(a) Commands"), command(r"factor(\(x^2+7\cdot x+12\));", r"\((x+4)(x+3)\)", 1),
        heading("(b) Context menu result"),
        paragraph("You can use Maple’s context menus to perform a wide variety of mathematical and other operations. Enter the polynomial and place your cursor at the end of the polynomial or expressions and right-click. The command will show you full information about factorization on line by typing. Then choose the factor option from the open window as shown in Figure 1.5. The context menu offers several operation to choose from according to the expression that you are using. The above result through context menu is as under:"),
        command(r"\(x^2+7\cdot x+12\)"), command(r"\(x^2+7\cdot x+12\));", r"\((x+4)(x+3)\)", 2),
        paragraph('The result is obtained through right-click on the last end of the expression by selecting “Factor” on the context menus. As shown in Figure 1.5.')
    ])
]
PAGES.extend([
    page('008_page_1.jpg', 7, [
        figure('figure-1-5', 'Figure 1.5', 'Maple context menu with the Factor operation selected'),
        heading('1.2.2 Use of MAPLE commands for expanding an expression'), heading('(a) Command'),
        paragraph('Use MAPLE command “expand” before parenthesis to expand the given expression.'),
        command(r'expand(\((x^2+2)\cdot(x^3+4\cdot x-3)\));', r'\(x^5+6x^3-3x^2+8x-6\)', 3),
        heading('(b) Context menu result'),
        paragraph('Enter the given expression and place your cursor on the last end of the expression and right click. Then choose expand option from the opened window as shown in the Figure 1.6.'),
        command(r'\((x^2+2)\cdot(x^3+4\cdot x-3)\)'),
        command('expand((x^2+2)*(x^3+4*x-3));', r'\(x^5+6x^3-3x^2+8x-6\)', 4),
        figure('figure-1-6', 'Figure 1.6', 'Maple context menu with Expand and its Apply Immediately submenu selected')
    ]),
    page('008_page_2.jpg', 8, [
        heading('1.2.3 Use of MAPLE commands for simplifying an expression'), heading('(a) Command'),
        command(r'\(simplify((25)^{\frac{1}{2}}+\frac{9}{6}-\frac{2}{3});\)', r'\(\frac{35}{6}\)', 5),
        heading('(b) Context menu result'),
        paragraph('Enter the given expression and place your cursor on the last end of the expression and right click. Then choose “simplify” from the opened window as shown in the Figure 1.7.'),
        command(r'\((25)^{\frac{1}{2}}+\frac{9}{6}-\frac{2}{3}\)'),
        command('simplify(25^(1/2)+9*(1/6)-2/3);', r'\(\frac{35}{6}\)', 6),
        figure('figure-1-7', 'Figure 1.7', 'Maple Simplify submenu showing the Simplify operation selected'),
        heading('1.2.4 Use of MAPLE commands for simplifying a rational expression'), heading('(a) Command'),
        command(r'\(simplify(\frac{t^2-9}{t^2+7\cdot t+12});\)', r'\(\frac{t-3}{t+4}\)', 7)
    ]),
    page('009_page_1.jpg', 9, [
        heading('(b) Context menu result'),
        paragraph('Enter the given expression and place your cursor on the last end of the expression and right click. Then select “simplify” option as shown in the Figure 1.8.'),
        command(r'\(\frac{t^2-9}{t^2+7\cdot t+12}\)'),
        command('simplify((t^2-9)/(t^2+7*t+12));', r'\(\frac{t-3}{t+4}\)', 8),
        figure('figure-1-8', 'Figure 1.8', 'Maple context menu Simplify operation for a rational expression'),
        heading('1.2.5 Use of MAPLE commands for substituting on expression'), heading('(a) Command'),
        command(r'subs(\(t=20,t^2-2\cdot t+5\));', '365', 9),
        heading('(b) Context menu result'),
        paragraph('Enter the given expression and place your cursor on last end of the expression and right click. Then select “evaluate at a point” option as shown in the Figure 1.9 and Figure 1.10 respectively.'),
        command(r'\(t^2-2\cdot t+5\)'), command('eval(t^2-2*t+5,t=20);', '365', 10)
    ]),
    page('009_page_2.jpg', 10, [
        figure('figure-1-9', 'Figure 1.9', 'Maple context menu with Evaluate at a Point selected'),
        figure('figure-1-10', 'Figure 1.10', 'Maple Evaluate at a Point dialog specifying t = 20'),
        heading('1.3 Graphics'), heading('1.3.1 Plot a two dimensional graph'),
        paragraph('To plot any two dimensional graph in MAPLE we use “plot” command in the command prompt.')
    ])
])
PAGES[1]['alternateVerification'] = {'pdf': 'Math Book for 12 class KPTBB.pdf', 'pdfPage': 6, 'side': 'left', 'reason': 'Full spread restores the text clipped at the JPG right edge.'}

# The original full PDF supplies sharper, uncropped versions of the same figures.
FIGURE_PDF_CROPS = [
    (5, 'figure-1-1', (892, 248, 1440, 502)),
    (5, 'figure-1-2', (841, 610, 1457, 918)),
    (7, 'figure-1-3', (102, 496, 668, 794)),
    (7, 'figure-1-4', (810, 107, 1450, 457)),
    (8, 'figure-1-5', (73, 106, 719, 392)),
    (8, 'figure-1-6', (124, 703, 748, 990)),
    (8, 'figure-1-7', (830, 455, 1474, 781)),
    (9, 'figure-1-8', (56, 333, 709, 718)),
    (9, 'figure-1-9', (822, 118, 1469, 454)),
    (9, 'figure-1-10', (810, 472, 1466, 886))
]
