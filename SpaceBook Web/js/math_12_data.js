// Class 12 Mathematics — source-derived KPTBB unit and lesson data.
const MATH_12_DATA = [
  {
    "id": "unit-1",
    "number": 1,
    "title": "Introduction to Symbolic Package, Maple",
    "titleUrdu": "",
    "pageRange": "Printed pages 1–24",
    "pageStart": 1,
    "pageEnd": 24,
    "sections": [
      {
        "id": "sec-1-1",
        "title": "1.1 Introduction",
        "theory": "By the end of this unit, the students will be able to:\n\n1.1 Introduction\n• Recognize the MAPLE environment.\n• Recognize basic MAPLE commands.\n• Use MAPLE as a calculator.\n• Use online MAPLE help.\n\n1.2 Polynomials\n• Use MAPLE commands for factoring a polynomial, expanding an expression, simplifying a rational expression, simplifying an expression, and substituting into an expression.\n\n1.3 Graphics\n• Plot a two-dimensional graph and demonstrate the domain and range of a plot.\n• Sketch parametric equations and know plotting options.\n\n1.4 Matrices\n• Recognize matrix and vector entry arrangement.\n• Apply matrix operations.\n• Compute the inverse and transpose of a matrix.\n\n1.1 Introduction\nIn the modern age of science and technology, technical computation has become the heart of problem solving in engineering and mathematics. To help us, MAPLE offers a vast repository of mathematical algorithms, covering a wide range of applications. It is a symbolic and numeric computing tool as well as a multi-paradigm programming language conceived at the University of Waterloo in 1980. From the first day, it has continued to be benchmark software for mathematical and symbolic computation. The Maple user interface allows us to harness all the computational power by using context-sensitive menus, an interactive assistant, and task templates. In this unit, we will learn how to use the basic commands that will lead us into the creative, dynamic, and captivating world of MAPLE explorations.\n\n1.1.1 Recognition of MAPLE Environment\nMaple software consists of three different parts.\n\nUser interface\nIt handles the input of mathematical expressions and different commands. The user interface also handles the display of output and the control of the MAPLE worksheet environment.\n\nKernel\nIt is a small collection of compiled C code. The entire kernel is loaded when a MAPLE session is started. It contains the essential facilities required to run MAPLE and perform basic mathematical operations. The components of the kernel include the MAPLE programming-language interpreter, arithmetic and memory-management facilities, and fundamental functions. Its small size ensures that the MAPLE system is portable, compact, and efficient.\n\nLibrary\nIt contains most of the MAPLE routines, including functions related to linear algebra, statistics, calculus, graphics, and other topics. This library also consists of individual routines and different packages of routines. All the library routines are implemented in the high-level MAPLE programming language and can be viewed and modified. Hence, it is useful to learn the MAPLE programming language so that we can modify existing code to produce the required routines.\n\nA. Getting started with Maple\nThe Maple software runs on different systems and platforms. It depends on the platform and system. It is convenient to use if you have a Windows-based operating system (installed Maple software package 14, 18, or any latest package).\n\nWhen a Maple session is started, the Maple prompt command (>) is displayed.\n\nFigure 1.1 Maple start menu\n\nThis prompt character appears at the upper left of the worksheet and indicates that Maple is waiting to receive input in the form of a Maple statement. When you have finished with the Maple session, leave the program by selecting “Exit” under the “File” menu, as shown in Figure 1.2.\n\nFigure 1.2 File menu and worksheet\n\n1.1.2 Recognition of basic MAPLE commands\nA MAPLE command is a statement of calculation followed by a semicolon or a colon. The following sections introduce commands and their displayed results.\n\nEnter commands on your worksheet and verify the given results. To save your worksheet, select “Save” under the “File” menu or use Ctrl+S.\n\nRemember\nIf you do not include a semicolon or colon at the end of a command, MAPLE interprets the next command line as a continuation of the previous command. The symbols +, −, *, /, and ^ denote addition, subtraction, multiplication, division, and exponentiation, respectively. When a string of operations is specified in a command, MAPLE performs exponentiation first, then multiplication and division, and then addition and subtraction. To change the order, use parentheses.\n\nSave command\nTo save a variable in a file, type the Save command at the command prompt. Replace the variable name and file name with your own, but keep the .m extension. The Save command saves the variable as a MAPLE assignment statement. If the value of a variable depends on other variables, save those variables as well. You can save more than one variable by giving all the variable names in the Save command.\n\nEditing commands\nIf you make a mistake in a command or want to change it, you can go back and edit the command.\n\nExact arithmetic and floating-point (evalf) commands\nMAPLE calculates fractions using exact arithmetic unless you specify that you want decimals (floating-point arithmetic) with the evalf command. “evalf” stands for “evaluate using floating-point arithmetic.” The argument in the evalf command specifies the number of significant figures in the result. If you omit it, MAPLE returns its default number of significant figures.\n\nMaple internal memory clearing command\nTo clear the internal memory during a Maple session, use the restart command or click the restart icon on the toolbar. When you enter this command, the Maple session returns to its startup state and all values are reset to their initial values.\n\nEnlistment of variables\nUse the colon-equal symbol (:=) to define variables and assign values to them. Once you have defined a variable, type its name to display its value. Using the variable name in a formula substitutes the assigned value.\n\n1.1.3 Use of MAPLE as a calculator\nYou can obtain the MapleSoft(TM) Graphing Calculator Overview by selecting Start, then Programs, then Maple 18, and then Maple Calculator.\n\nThis graphical scientific calculator is available as part of your Maple(TM) installation or via a web server running MapleNet(TM). The calculator is used for Maple calculations.\n\nOn the toolbar:\n• Use the Settings tab to control the basic computation settings for the calculator.\n• Use the Math tab to select functions, from basic functions to linear algebra to statistics.\n• Use the Graph tab to control how graphs are displayed and what they display.\n• Use the Data tab to control the data used to produce a graph or data tabulated directly.\n• Use the Variable tab to control the variables you have assigned and their values.\n\nTo use the graphical calculator, press the Math tab and select the functions to apply. This builds your expression in the input area, which is adjacent to the session history area on the left side of the calculator. When you are ready to evaluate the expression, press ENTER on your keyboard. Alternatively, press the Graph button to graph the expression, or the Data button to tabulate values for the expression.\n\n1.1.4 Online MAPLE help\nYou can get help with MAPLE syntax by using the HELP menu, as described previously. If you have a question about a particular command, you can quickly get help by typing a question mark followed by the name of the command (without a semicolon).\n\nThis opens a window containing information about what the command does and how to use it. Click the small “Cross” box at the upper left of the window to close it.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-1-2",
        "title": "1.2 Polynomials",
        "theory": "1.2 Polynomials\nWe are familiar with polynomials from our previous grades. The factorization of a polynomial and the expansion of an expression can be performed through direct MAPLE commands and context menus.\n\n1.2.1 Use of MAPLE commands for factoring a polynomial\nCommands\n\nContext menu result\nYou can use Maple’s context menus to perform a wide variety of mathematical and other operations. Enter the polynomial, place your cursor at the end of the expression, and right-click. The command window provides information about the factorization. Choose the Factor option from the open window, as shown in Figure 1.5. The context menu offers several operations to choose from according to the expression you are using.\n\n1.2.2 Use of MAPLE commands for expanding an expression\nCommand\nUse the MAPLE command “expand” before the parentheses to expand the given expression.\n\nContext menu result\nEnter the given expression, place your cursor at the end of it, and right-click. Then choose the expand option from the open window, as shown in Figure 1.6.\n\n1.2.3 Use of MAPLE commands for simplifying an expression\nCommand\nUse the simplify command to simplify an expression.\n\nContext menu result\nEnter the given expression, place your cursor at the end of it, and right-click. Then choose “simplify” from the open window, as shown in Figure 1.7.\n\n1.2.4 Use of MAPLE commands for simplifying a rational expression\nCommand\nUse the simplify command to simplify a rational expression.\n\nContext menu result\nEnter the given expression, place your cursor at the end of it, and right-click. Then select the “simplify” option, as shown in Figure 1.8.\n\n1.2.5 Use of MAPLE commands for substituting an expression\nCommand\nUse the subs command to substitute a value into an expression.\n\nContext menu result\nEnter the given expression, place your cursor at the end of it, and right-click. Then select the “evaluate at a point” option, as shown in Figures 1.9 and 1.10.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-1-3",
        "title": "1.3 Graphics",
        "theory": "1.3 Graphics\n\n1.3.1 Plot a two-dimensional graph\nTo plot any two-dimensional graph in MAPLE, use the “plot” command at the command prompt.\n\n1.3.2 Domain and range of a plot\nTo plot a two-dimensional graph with a specified domain and range, use the “plot” command at the command prompt.\n\n1.3.3 Sketch parametric equations\nTo sketch parametric equations in MAPLE, use the “plot” command. The graph is plotted over the specified parameter interval and viewing ranges.\n\n1.3.4 Know plotting options\nThe plotting options listed below can provide commands that create two-dimensional plots. These options can be used with the “plot” command and are generally available to all MAPLE commands that generate two-dimensional plots. The help page for a particular MAPLE command provides more detail about the options it accepts. Options must be added at the end of the given sequence. You can explore the options in the “plot” command interactively by using the Interactive Plot Builder.\n\nAdaptive\nadaptive = true, false, or a non-negative integer\nWhen plotting a function over an interval, the interval is sampled at a number of points controlled by “sample” and “numpoints”. Adaptive plotting subdivides intervals, where necessary, to obtain a better representation of the function. This subsampling can be turned off by setting “adaptive” to false. By default it is true, and intervals are subdivided at most six times to improve the plot. Setting this option to a non-negative integer controls the maximum number of subdivisions.\n\nAnnotation\nThe annotation option adds descriptive text to a two-dimensional curve or point plot. A point plot is a collection of points treated as a single plot element. Mathematical text appears when the pointer hovers over the associated curve or point.\n\nAxes\nSpecifies the type of axes: boxed, framed, none, or normal.\n\nAxes font\nSpecifies the font for labels on the axes’ tick marks. It is specified in the same manner as the font option and overrides values specified for font.\n\nAxis\nThe axis and axis[dir] options provide information about one or more axes for plotting commands such as “plot” and “plot3d”. This information can include axis color, tick-mark and grid-line locations, and logarithmic scales. With axis = t, the information is applied to all axes. With axis[dir] = t, it is applied only to the specified direction: x-axis, y-axis, or z-axis, or a sequence of two directions. Multiple axis[dir] options with different values can be used for different axes. Two-dimensional plotting commands do not accept the axis[3] option. The axis information is given by t, which may contain one or more sub-options.\n\nAxis coordinates\nNormally, a coordinate system is used to display the axes. Cartesian axes are displayed by default. If the coordinate system is polar, radial and angular axes are generated. This option is used together with the coords = polar option.\n\nBackground\nThe background option sets a single background image or color for a plot. Its value can be an image file name, a string, a name, a datatype = float, an Array used with the Image Tools package, or a color. If size is omitted, the dimensions of the plot can be determined by the image. If size is provided, the image is displayed with the dimensions of the plot. A color may be given as a color-tools object or a color string. A string is first interpreted as a file name; if the file does not exist, it is assumed to be a color.\n\nCaption\nThe caption value can be an arbitrary expression or a list consisting of the caption followed by the font option. By default, there is no caption.\n\nCaption font\nDefines the font for the plot caption in the same manner as the font option. It overrides values specified for font.\n\nColor\nSpecifies the color of the curves to be plotted.\n\nColor scheme\nApplies a color scheme to a surface or set of points.\n\nCoordinate view\nThis option is used when the axis-coordinates option has the value polar. It specifies the radial range to display and the angular range to display.\n\nCoords\nThe value is one of the choices listed on the coords help page. Cartesian axes are displayed by default. To generate polar plots, use the axis-coordinates = polar option together with the coords = polar option.\n\nDiscont\nAllows detection of discontinuities.\n\nFilled\nIf the filled option is true, the area between the curve and the x-axis is shown in a solid color. Its value can also be a list containing sub-options such as color, style, or transparency. These options apply to the filled area, not the original curve. This option does not work with non-Cartesian coordinate systems.\n\nFilled regions\nIf the filledregions option is true, regions defined by curves are filled with different colors. This option is available only for the “contourplot”, “implicitplot”, and “listcontplot” commands. It does not work with non-Cartesian coordinate systems.\n\nFont\nDefines the font for the plot title, caption, axis tick-mark labels, and axis labels when no font has been specified for the axes, caption, label, or title options. The value is a list of the form [family, style, size]. The family may be Times, Courier, Helvetica, or Symbol, or any font supported by the system, such as Times New Roman or Calibri in Windows. The first letter of the family name must be capitalized. The style may be roman, bold, italic, bold italic, oblique, bold oblique, or omitted. The Symbol family does not accept a style option. The final value is the point size.\n\nGridline\nBy default, grid lines are drawn when gridlines = true or gridlines is provided. The default is gridlines = false. If the axis option is also provided and contains a gridlines sub-option, that option overrides this one.\n\nLabels\nSpecifies labels for the axes. By default, the labels are the names of the variables in the original function to be plotted; if these are unavailable, no labels are used.\n\nLabel directions\nSpecifies the direction in which labels are printed along the axes. The x- and y-axis labels can be horizontal or vertical. The default direction is horizontal.\n\nLabel font\nSpecifies the font for labels on the plot axes in the same manner as the font option. It overrides values specified for font.\n\nLegend\nIf the plot command is used to plot multiple curves, the legend value can be a list containing a legend entry for each curve.\n\nLegend style\nThe value is a list of one or more sub-options. The legendstyle option includes font and location. The location sub-option allows the legend to be placed at the top, bottom, right, or left.\n\nLine style\nControls the line style of curves. The available styles are solid, dot, dash, dash dot, long dash, space dash, or space dot. The default is solid. The value can also be an integer from 1 to 7, with each integer representing a line style as shown in the book.\n\nNumber of points\nSpecifies the minimum number of points to be generated. The default is 200.\n\nResolution\nSets the horizontal display resolution of the device in pixels. The default resolution is 800. The value determines when the adaptive plotting scheme terminates.\n\nSample\nA list of numerical values used for the initial sampling of the function. Normally, the function is sampled at additional points. To restrict sampling to only the listed values, include the adaptive = false option.\n\nScaling\nControls the scaling of the graph. By default, the plot is scaled to fit the plot window. The constrained value causes all axes to use the same scale.\n\nSize\nSpecifies the size of the plot window. It can be set by specifying the number of pixels, a proportion of worksheet width, or a ratio such as a square, the golden ratio, or a custom ratio.\n\nSmart view\nDetermines an appropriate view of the plot data. The plot command generates data based on the range provided or on a default range if none is provided. With smartview = true, a view is computed that tries to present the important regions of the data. To show all computed data, use smartview = false. The default is true. This option is available for the plot command and applies only to curves, not points, polygons, or text.\n\nStyle\nThe plot style can be line, point, point line, polygon, or polygon outline. The names in parentheses are aliases for the option values. The line, polygon, and polygon-outline styles draw curves by interpolating between sample points. The point style plots only the points. The default, polygon outline, draws polygons filled with an outline. Polygon style shows polygons without an outline, while line style draws polygon outlines only. Point line combines point and line styles.\n\nSymbol\nSpecifies the symbol used for points. Choices include asterisk, box, circle, cross, diagonal cross, diamond, point, solid box, solid circle, or solid diamond.\n\nSymbol size\nSpecifies the size of a plotting symbol as a natural number. This does not affect the point symbol. The default symbol size is 10.\n\nThickness\nSpecifies the thickness of lines in the plot. The value must be a non-negative number. A value of 0 produces the thinnest line. The default is 1.\n\nTick marks\nThe values m and n specify tick-mark placement on the x- and y-axes, respectively. They can be an integer specifying the number of tick marks, a list of locations, a list of equations of the form location = label, a name, or a spacing structure.\n\nTitle\nA title can be given to the plot. Its value can be an arbitrary expression or a list consisting of the title followed by the font option. By default, a plot has no title.\n\nTitle font\nSpecified in the same manner as the font option. It overrides values specified for font.\n\nTransparency\nSpecifies the transparency of the plot surface. The value must be a floating-point number in the range [0, 1]. A value of 0 means “not transparent”; a value of 1 means “fully transparent.”\n\nUse units\nWhen set to true, this option indicates that units are part of the function and should be included in axis labels. Its value can also be a list of units.\n\nView\nSpecifies the minimum and maximum coordinates of the curve to be displayed. By default, it is determined by the smartview option. If smartview = false is given, all plot data is displayed. If smartview = true, or the option is omitted, the data is analyzed to determine a reasonable view that shows its significant features.\n\nRemember\nIf the same option is provided more than once with different values, the final value specified is generally the one used. All the above options are available for the Standard Worksheet interface.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-1-4",
        "title": "1.4 Matrices",
        "theory": "1.4 Matrices\nThe command displays full information about matrices when you type ?matrices at the command line.\n\n1.4.1 Recognition of matrix and vector entry arrangement\nUsing palettes\nUse the cursor button to select the matrix palette. Click “matrix”, choose the required number of rows and columns, and click the data type to select the entries. Finally, click “insert matrix” and press ENTER to obtain the required matrix.\n\n1.4.2 Applying matrix operations\nMatrix addition\nMatrix multiplication\nUsing palettes\nTo obtain the result, right-click the last matrix, then click “simplify” or press ENTER.\n\n1.4.3 Inverse and transpose of a matrix\nInverse of a matrix\nUsing palettes\nTo obtain the result through the context menu, right-click the last matrix, select “Standard Operations”, and then click “inverse” to obtain the inverse of a matrix.\n\nTranspose of a matrix\nTo obtain the result through the context menu, right-click the last matrix, select “Standard Operations”, and then click “transpose” to obtain the transpose of a matrix.\n\nDeterminant of a matrix\nTo obtain the result through the context menu, right-click the last matrix, select “Standard Operations”, and then click “determinant” to obtain its determinant.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-1-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Differentiate \\(f(x)=x^{2}+4x+4\\) with respect to \\(x\\) at the point \\(x=2\\).",
        "given": "f(x)=x^{2}+4x+4, x=2",
        "method": "Maple differentiation at a point",
        "steps": [
          "Set A=x^{2}+4x+4, X=x, and P=2.",
          "Enter Diff(A,X,P).",
          "Substitute the values: Diff(x^{2}+4x+4,x,2)=8."
        ],
        "answer": "8",
        "diagram": null
      },
      {
        "id": "we-1-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Integrate \\(x^{2}+4x+4\\) with respect to \\(x\\) over the interval \\([0,1]\\).",
        "given": "f(x)=x^{2}+4x+4, lower limit 0, upper limit 1",
        "method": "Maple definite integration",
        "steps": [
          "Set A=x^{2}+4x+4, X=x, P=0, and Q=1.",
          "Enter Int(A,X,P,Q).",
          "\\int_{0}^{1}(x^{2}+4x+4)\\,dx=[\\frac{x^{3}}{3}+2x^{2}+4x]_{0}^{1}=\\frac{19}{3}\\approx6.333333."
        ],
        "answer": "6.333333",
        "diagram": null
      },
      {
        "id": "we-1-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Plot the graph of \\(y=x^{2}+3x+8\\).",
        "given": "y=x^{2}+3x+8",
        "method": "Plot the quadratic function in Maple",
        "steps": [
          "Enter plot(x^{2}+3x+8).",
          "The graph is an upward-opening parabola with vertex \\((-\\frac{3}{2},\\frac{23}{4})\\)."
        ],
        "answer": "The graph is the parabola \\(y=x^{2}+3x+8\\).",
        "diagram": {
          "type": "quadratic-graph",
          "a": 1,
          "b": 3,
          "c": 8,
          "xMin": -10,
          "xMax": 10,
          "yMin": 0,
          "yMax": 130,
          "xLabel": "x",
          "yLabel": "y",
          "title": "Graph of y=x²+3x+8"
        }
      },
      {
        "id": "we-1-4",
        "num": "4",
        "title": "Example 4",
        "problem": "Plot the graph of \\(y=x^{2}+2\\) for \\(-3\\leq x\\leq3\\).",
        "given": "y=x^{2}+2, -3≤x≤3",
        "method": "Plot the function over the specified domain",
        "steps": [
          "Enter plot(x^{2}+2,x=-3..3).",
          "The vertex is (0,2), and the graph is symmetric about the y-axis."
        ],
        "answer": "The graph is the portion of \\(y=x^{2}+2\\) on \\([-3,3]\\), with range \\([2,11]\\).",
        "diagram": {
          "type": "quadratic-graph",
          "a": 1,
          "b": 0,
          "c": 2,
          "xMin": -3,
          "xMax": 3,
          "yMin": 0,
          "yMax": 11,
          "xLabel": "x",
          "yLabel": "y",
          "title": "Graph of y=x²+2 on [-3,3]"
        }
      },
      {
        "id": "we-1-5",
        "num": "5",
        "title": "Example 5",
        "problem": "Sketch the graph of the parametric equations x = cos(t) and y = sin(t), where −4 ≤ t ≤ 4, with −2 ≤ x,y ≤ 2.",
        "given": "x = cos(t), y = sin(t), −4 ≤ t ≤ 4",
        "method": "Plot the parametric curve",
        "steps": [
          "Use the parameter t in the interval [-4,4].",
          "Since x²+y²=cos²(t)+sin²(t)=1, the curve is the unit circle."
        ],
        "answer": "A unit circle centered at the origin.",
        "diagram": {
          "type": "unit-circle",
          "title": "Parametric curve x=cos(t), y=sin(t)"
        }
      },
      {
        "id": "we-1-6",
        "num": "6",
        "title": "Example 6",
        "problem": "Plot the graph of sec(x) for −2π ≤ x ≤ 2π, and give it the title “Graph of Secant Function”.",
        "given": "y = sec(x), −2π ≤ x ≤ 2π",
        "method": "Plot the secant function with the stated Maple options",
        "steps": [
          "Set the graph title to “Graph of Secant Function” and use Times New Roman, 20 pt.",
          "The printed example also uses framed axes, point style, asterisk symbols of size 20, and tick marks spaced by π."
        ],
        "answer": "The graph has vertical asymptotes where cos(x)=0.",
        "diagram": {
          "type": "secant-graph",
          "title": "Graph of Secant Function"
        }
      }
    ],
    "exercises": [],
    "slos": {
      "mcqs": [
        {
          "q": "Which three parts make up Maple software?",
          "options": [
            "User interface",
            "Kernel",
            "Library",
            "All of these"
          ],
          "correct": 3,
          "exp": "Maple consists of the user interface, kernel, and library."
        },
        {
          "q": "What does the Maple user interface handle?",
          "options": [
            "Input, output display, and worksheet control",
            "Only file storage",
            "Only graph colors",
            "Only matrix determinants"
          ],
          "correct": 0,
          "exp": "The interface handles mathematical input, command input, output display, and worksheet control."
        },
        {
          "q": "What is the Maple kernel described as?",
          "options": [
            "Compiled C code",
            "A graph palette",
            "A worksheet file",
            "A matrix type"
          ],
          "correct": 0,
          "exp": "The kernel is a small collection of compiled C code that performs the core calculations."
        },
        {
          "q": "What is found in the Maple library?",
          "options": [
            "Mathematical routines and packages",
            "Only operating-system files",
            "Only fonts",
            "Only worksheet prompts"
          ],
          "correct": 0,
          "exp": "The library contains routines for algebra, statistics, calculus, graphics, and other topics."
        },
        {
          "q": "Which symbols can terminate a Maple calculation command?",
          "options": [
            "Semicolon or colon",
            "Comma only",
            "Period only",
            "Parentheses only"
          ],
          "correct": 0,
          "exp": "A Maple calculation statement is followed by a semicolon or a colon."
        },
        {
          "q": "What happens when a command has no semicolon or colon?",
          "options": [
            "The next input continues the command",
            "The worksheet closes",
            "The value becomes zero",
            "The command is saved automatically"
          ],
          "correct": 0,
          "exp": "Without a terminator, Maple treats the next command line as a continuation."
        },
        {
          "q": "Which operator assigns a value to a Maple variable?",
          "options": [
            "=",
            ":=",
            "==",
            "->"
          ],
          "correct": 1,
          "exp": "Maple uses the colon-equal assignment operator :=."
        },
        {
          "q": "Which operation is performed first in Maple precedence?",
          "options": [
            "Addition",
            "Division",
            "Exponentiation",
            "Subtraction"
          ],
          "correct": 2,
          "exp": "Exponentiation is performed before multiplication and division, then addition and subtraction."
        },
        {
          "q": "Which command requests a floating-point evaluation?",
          "options": [
            "factor",
            "evalf",
            "subs",
            "restart"
          ],
          "correct": 1,
          "exp": "evalf evaluates an expression using floating-point arithmetic."
        },
        {
          "q": "What does exact arithmetic preserve?",
          "options": [
            "Fraction values exactly",
            "Only rounded decimals",
            "Only graph points",
            "Only variable names"
          ],
          "correct": 0,
          "exp": "Maple keeps rational results exact unless a floating-point evaluation is requested."
        },
        {
          "q": "Which command clears Maple's stored session values?",
          "options": [
            "expand",
            "restart",
            "factor",
            "plot"
          ],
          "correct": 1,
          "exp": "The restart command returns Maple to its startup state and resets assigned values."
        },
        {
          "q": "What file extension is named for the Save command in the book?",
          "options": [
            ".m",
            ".jpg",
            ".html",
            ".csv"
          ],
          "correct": 0,
          "exp": "The book instructs the reader to retain the .m extension when saving a variable file."
        },
        {
          "q": "Factor x^{2}+7x+12.",
          "options": [
            "(x+3)(x+4)",
            "(x+6)(x+2)",
            "(x-3)(x-4)",
            "x(x+7)+12"
          ],
          "correct": 0,
          "exp": "The numbers 3 and 4 multiply to 12 and add to 7, so the factorization is (x+3)(x+4)."
        },
        {
          "q": "Expand (x+2)(x+3).",
          "options": [
            "x^{2}+5x+6",
            "x^{2}+6x+5",
            "x^{2}+x+6",
            "x^{2}+6"
          ],
          "correct": 0,
          "exp": "Multiply the terms: x²+3x+2x+6=x²+5x+6."
        },
        {
          "q": "Evaluate 25^{1/2}+9/6-2/3 exactly.",
          "options": [
            "35/6",
            "5",
            "6",
            "7/6"
          ],
          "correct": 0,
          "exp": "25^(1/2)=5, and 5+3/2-2/3=30/6+9/6-4/6=35/6."
        },
        {
          "q": "Simplify (x^{2}-9)/(x^{2}+7x+12).",
          "options": [
            "(x-3)/(x+4), x≠-3,-4",
            "(x+3)/(x+4), x≠-3,-4",
            "(x-3)/(x+3)",
            "1"
          ],
          "correct": 0,
          "exp": "Factor numerator and denominator: (x−3)(x+3)/[(x+3)(x+4)]. Cancel x+3, retaining x≠−3,−4."
        },
        {
          "q": "For t=20, evaluate t^{2}-2t+5.",
          "options": [
            "365",
            "345",
            "405",
            "3650"
          ],
          "correct": 0,
          "exp": "Substitute 20: 20²−2(20)+5=400−40+5=365."
        },
        {
          "q": "Which Maple command plots a two-dimensional function?",
          "options": [
            "plot",
            "factor",
            "subs",
            "inverse"
          ],
          "correct": 0,
          "exp": "The book uses the plot command for two-dimensional graphs.",
          "diagram": {
            "type": "quadratic-graph",
            "a": 1,
            "b": 0,
            "c": -4,
            "xMin": -4,
            "xMax": 4,
            "yMin": -5,
            "yMax": 12,
            "xLabel": "x",
            "yLabel": "y",
            "title": "Graph of y=x²−4"
          }
        },
        {
          "q": "In plot(f(x), x=a..b), what does a..b specify?",
          "options": [
            "The x-domain",
            "The line color",
            "The y-axis label",
            "The graph title"
          ],
          "correct": 0,
          "exp": "The interval a..b specifies the domain over which the function is plotted."
        },
        {
          "q": "Which syntax represents a parametric plot in Maple?",
          "options": [
            "[x(t),y(t),t=a..b]",
            "x+y=t",
            "matrix(x,y)",
            "factor(x,y)"
          ],
          "correct": 0,
          "exp": "A parametric plot supplies the x and y functions and the parameter interval."
        },
        {
          "q": "If x=cos(t) and y=sin(t), what equation does the curve satisfy?",
          "options": [
            "x^{2}+y^{2}=1",
            "x+y=1",
            "xy=1",
            "x^{2}-y^{2}=1"
          ],
          "correct": 0,
          "exp": "Using cos²(t)+sin²(t)=1 gives x²+y²=1, the unit circle.",
          "diagram": {
            "type": "unit-circle",
            "title": "Unit circle: x=cos(t), y=sin(t)"
          }
        },
        {
          "q": "For y=sec(x), where are the vertical asymptotes?",
          "options": [
            "x=π/2+kπ",
            "x=kπ",
            "x=0 only",
            "y=0"
          ],
          "correct": 0,
          "exp": "sec(x)=1/cos(x), so vertical asymptotes occur where cos(x)=0: x=π/2+kπ.",
          "diagram": {
            "type": "secant-graph",
            "title": "Graph of y=sec(x)"
          }
        },
        {
          "q": "What is the default value of the adaptive plotting option?",
          "options": [
            "true",
            "false",
            "0",
            "200"
          ],
          "correct": 0,
          "exp": "Adaptive plotting is true by default."
        },
        {
          "q": "Which options control the initial sampling of a plotted function?",
          "options": [
            "sample and numpoints",
            "caption and title",
            "font and color",
            "legend and labels"
          ],
          "correct": 0,
          "exp": "The text explains that sample and numpoints control the interval sampling."
        },
        {
          "q": "Which is a valid axes option?",
          "options": [
            "boxed",
            "triangle",
            "matrix",
            "fraction"
          ],
          "correct": 0,
          "exp": "The axes option can be boxed, framed, none, or normal."
        },
        {
          "q": "What does the annotation option add to a plot?",
          "options": [
            "Descriptive text attached to a curve or point",
            "A matrix inverse",
            "A new domain",
            "A decimal approximation"
          ],
          "correct": 0,
          "exp": "Annotation adds descriptive text to a two-dimensional curve or point plot."
        },
        {
          "q": "What is the default setting for gridlines?",
          "options": [
            "false",
            "true",
            "800",
            "π"
          ],
          "correct": 0,
          "exp": "The book states that gridlines are false by default."
        },
        {
          "q": "What are default axis labels when variables are available?",
          "options": [
            "The names of the variables",
            "The function's roots",
            "The title text",
            "The legend entries"
          ],
          "correct": 0,
          "exp": "By default, labels are the names of variables in the plotted function."
        },
        {
          "q": "When is a legend useful?",
          "options": [
            "When plotting multiple curves",
            "When clearing memory",
            "When simplifying a fraction",
            "When defining one variable"
          ],
          "correct": 0,
          "exp": "A legend can list an entry for each curve in a multiple-curve plot."
        },
        {
          "q": "Which is one of the listed plot styles?",
          "options": [
            "point line",
            "inverse",
            "restart",
            "colon-equal"
          ],
          "correct": 0,
          "exp": "The listed styles include line, point, point line, polygon, and polygon outline."
        },
        {
          "q": "What is the default minimum number of plotted points?",
          "options": [
            "200",
            "20",
            "10",
            "800"
          ],
          "correct": 0,
          "exp": "The numpoints option specifies the minimum number; its default is 200."
        },
        {
          "q": "What range is allowed for plot transparency?",
          "options": [
            "[0,1]",
            "[1,10]",
            "(-∞,0)",
            "[0,100]"
          ],
          "correct": 0,
          "exp": "Transparency is a floating-point value from 0 to 1, inclusive."
        },
        {
          "q": "A matrix with 3 rows and 2 columns has what order?",
          "options": [
            "3×2",
            "2×3",
            "5×1",
            "6×6"
          ],
          "correct": 0,
          "exp": "Matrix order is rows by columns, so the order is 3×2."
        },
        {
          "q": "What is the result of [[1,2],[3,4]] + [[4,3],[2,1]]?",
          "options": [
            "[[5,5],[5,5]]",
            "[[4,6],[6,4]]",
            "[[5,6],[5,4]]",
            "[[4,5],[6,5]]"
          ],
          "correct": 0,
          "exp": "Add corresponding entries: 1+4=5, 2+3=5, 3+2=5, and 4+1=5."
        },
        {
          "q": "Find det([[1,2],[3,4]]).",
          "options": [
            "-2",
            "2",
            "10",
            "-10"
          ],
          "correct": 0,
          "exp": "For a 2×2 matrix, the determinant is ad−bc=1·4−2·3=−2."
        }
      ],
      "shortQuestions": [
        {
          "q": "What are the three components of Maple?",
          "sol": "The user interface, kernel, and library.",
          "marks": 3
        },
        {
          "q": "What does the Maple kernel do?",
          "sol": "It supplies the compiled core and facilities needed to perform Maple calculations.",
          "marks": 3
        },
        {
          "q": "Which operator assigns a value to a variable?",
          "sol": "The colon-equal operator, :=.",
          "marks": 3
        },
        {
          "q": "What is the command terminator in Maple?",
          "sol": "A semicolon or a colon.",
          "marks": 3
        },
        {
          "q": "What is the purpose of evalf?",
          "sol": "It evaluates an expression using floating-point arithmetic.",
          "marks": 3
        },
        {
          "q": "Evaluate 3²+2×4.",
          "sol": "3²+2×4=9+8=17.",
          "marks": 3
        },
        {
          "q": "Factor x²−5x+6.",
          "sol": "x²−5x+6=(x−2)(x−3).",
          "marks": 3
        },
        {
          "q": "Expand (x−1)(x+4).",
          "sol": "(x−1)(x+4)=x²+3x−4.",
          "marks": 3
        },
        {
          "q": "Simplify (x²−4)/(x−2), stating the restriction.",
          "sol": "(x²−4)/(x−2)=[(x−2)(x+2)]/(x−2)=x+2, with x≠2.",
          "marks": 3
        },
        {
          "q": "Find 2u²+u−1 when u=3.",
          "sol": "2(3²)+3−1=18+3−1=20.",
          "marks": 3
        },
        {
          "q": "Which command plots a two-dimensional graph?",
          "sol": "The plot command.",
          "marks": 3
        },
        {
          "q": "What does the domain of a plotted function describe?",
          "sol": "The allowed input values, usually the x-values over which the graph is drawn.",
          "marks": 3
        },
        {
          "q": "What is the vertex and minimum of y=x²−1?",
          "sol": "The vertex is (0,−1), and the minimum value is −1.",
          "marks": 3,
          "diagram": {
            "type": "quadratic-graph",
            "a": 1,
            "b": 0,
            "c": -1,
            "xMin": -3,
            "xMax": 3,
            "yMin": -2,
            "yMax": 9,
            "xLabel": "x",
            "yLabel": "y",
            "title": "Graph of y=x²−1"
          }
        },
        {
          "q": "What curve is represented by x=cos(t), y=sin(t)?",
          "sol": "The unit circle x²+y²=1.",
          "marks": 3,
          "diagram": {
            "type": "unit-circle",
            "title": "x=cos(t), y=sin(t)"
          }
        },
        {
          "q": "Where does sec(x) have a vertical asymptote?",
          "sol": "Where cos(x)=0, namely x=π/2+kπ for integer k.",
          "marks": 3,
          "diagram": {
            "type": "secant-graph",
            "title": "Vertical asymptotes of sec(x)"
          }
        },
        {
          "q": "What is the default value of adaptive plotting?",
          "sol": "True.",
          "marks": 3
        },
        {
          "q": "What is the default numpoints value stated in the book?",
          "sol": "200 points.",
          "marks": 3
        },
        {
          "q": "State the order of a matrix with 2 rows and 3 columns.",
          "sol": "Its order is 2×3.",
          "marks": 3
        },
        {
          "q": "Find the determinant of [[2,1],[5,3]].",
          "sol": "2·3−1·5=1.",
          "marks": 3
        },
        {
          "q": "What does transposing a matrix do?",
          "sol": "It changes rows into columns and columns into rows.",
          "marks": 3
        }
      ],
      "longQuestions": [
        {
          "q": "Explain the three parts of Maple software and the role of each.",
          "sol": "The user interface handles mathematical input, commands, output display, and worksheet control. The kernel is the compiled core that performs calculations and supplies arithmetic and memory facilities. The library contains routines and packages for areas such as linear algebra, statistics, calculus, and graphics.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Explain Maple command endings, assignment, precedence, and exact arithmetic.",
          "sol": "A calculation command ends with a semicolon or colon. Without either, the next line continues the same command. Use := to assign a value. Maple evaluates powers first, then multiplication and division, then addition and subtraction; parentheses change the order. Maple preserves exact fractions unless evalf is requested.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Factor x²+7x+12 and expand (x+2)(x+3), showing the main steps.",
          "sol": "For the factorization, find two numbers with product 12 and sum 7: 3 and 4. Thus x²+7x+12=(x+3)(x+4). For expansion, (x+2)(x+3)=x²+3x+2x+6=x²+5x+6.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Simplify (x²−9)/(x²+7x+12) and state the excluded values.",
          "sol": "Factor both parts: (x²−9)/(x²+7x+12)=[(x−3)(x+3)]/[(x+3)(x+4)]. Cancel x+3 to obtain (x−3)/(x+4). The original denominator is zero at x=−3 and x=−4, so both values remain excluded.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Use substitution to evaluate t²−2t+5 at t=20.",
          "sol": "Replace each t with 20: 20²−2(20)+5=400−40+5=365.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Sketch the graph of y=x²−4. Identify its intercepts and vertex.",
          "sol": "The graph is an upward-opening parabola. Set y=0: x²−4=0, so (x−2)(x+2)=0 and the x-intercepts are (−2,0) and (2,0). At x=0, y=−4, so the vertex is (0,−4).",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result.",
          "diagram": {
            "type": "quadratic-graph",
            "a": 1,
            "b": 0,
            "c": -4,
            "xMin": -4,
            "xMax": 4,
            "yMin": -5,
            "yMax": 12,
            "xLabel": "x",
            "yLabel": "y",
            "title": "Graph of y=x²−4",
            "points": [
              {
                "x": -2,
                "y": 0,
                "label": "(−2,0)"
              },
              {
                "x": 2,
                "y": 0,
                "label": "(2,0)"
              }
            ]
          }
        },
        {
          "q": "For y=x²+2 on −3≤x≤3, state the domain and range and describe the graph.",
          "sol": "The domain is [−3,3]. The parabola opens upward and has vertex (0,2), its minimum value. At x=−3 and x=3, y=11. Therefore the range is [2,11].",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result.",
          "diagram": {
            "type": "quadratic-graph",
            "a": 1,
            "b": 0,
            "c": 2,
            "xMin": -3,
            "xMax": 3,
            "yMin": 0,
            "yMax": 11,
            "xLabel": "x",
            "yLabel": "y",
            "title": "y=x²+2 on [−3,3]"
          }
        },
        {
          "q": "Describe the parametric curve x=cos(t), y=sin(t), where −4≤t≤4.",
          "sol": "Squaring and adding gives x²+y²=cos²(t)+sin²(t)=1. The curve lies on the unit circle centered at the origin. The parameter interval covers more than one full revolution, so the circle is traced more than once.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result.",
          "diagram": {
            "type": "unit-circle",
            "title": "Parametric unit circle"
          }
        },
        {
          "q": "Describe the graph of y=sec(x) on −2π≤x≤2π.",
          "sol": "Since sec(x)=1/cos(x), the graph is undefined where cos(x)=0. In this interval the vertical asymptotes occur at x=−3π/2, −π/2, π/2, and 3π/2. The graph is even and has period 2π.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result.",
          "diagram": {
            "type": "secant-graph",
            "title": "Graph of y=sec(x)"
          }
        },
        {
          "q": "Explain adaptive, sample, and numpoints options for plotting.",
          "sol": "The interval is sampled at points controlled by sample and numpoints. Adaptive plotting subdivides intervals when needed to represent the function more accurately; it is true by default and may be disabled or limited by an integer. Sample supplies initial sample values. Numpoints gives the minimum number of points and defaults to 200.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Describe the axes, axis, axis-coordinates, and coords plotting options.",
          "sol": "Axes selects boxed, framed, none, or normal axes. Axis can set axis information globally or for a specified direction, including colors, ticks, grid lines, and logarithmic scales. Axis-coordinates chooses Cartesian or polar display; Cartesian is the default. Polar plots use axis-coordinates=polar together with coords=polar.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Explain how labels, legends, titles, and styles improve a plot.",
          "sol": "Labels name the axes and default to the variables in the function. Label directions control horizontal or vertical orientation. A legend provides entries for multiple curves and its style controls font and location. A title adds a heading and can use titlefont. Styles include line, point, point line, polygon, and polygon outline.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "Describe the matrix palette procedure and matrix order.",
          "sol": "A matrix order is stated as rows×columns. In the palette, select matrix, choose the required row and column counts, choose the data type, and insert the matrix. Press ENTER to place the selected matrix into the worksheet.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        },
        {
          "q": "For A=[[1,2],[3,4]], find Aᵀ and det(A). Then state how the inverse is obtained in Maple.",
          "sol": "Transpose by interchanging rows and columns: Aᵀ=[[1,3],[2,4]]. The determinant is 1·4−2·3=−2. Since the determinant is non-zero, A is invertible. In Maple, use the inverse command or choose Standard Operations, then inverse, from the context menu.",
          "marks": 8,
          "rubric": "Award marks for the correct method, mathematical working, and final result."
        }
      ]
    },
    "formulaSheet": []
  },
  {
    "id": "unit-2",
    "number": 2,
    "title": "Functions and Limits",
    "titleUrdu": "",
    "pageRange": "Printed pages 25–62",
    "pageStart": 25,
    "pageEnd": 62,
    "sections": [
      {
        "id": "sec-2-1",
        "title": "2.1 Functions",
        "theory": "The three animals Zurain owns before he started his collection.\n\nFunction are constantly encountered in mathematics and are essential for formulating physical relationships in science and technology. In our routine life function is very useful e.g. Zurain like all kind of animals. He started collecting them recently and already owns 3 animals. He plans on buying every month accordingly, of each type of animals.\n\nLet 'x' be the number of months have past since Zurain started collecting animals. Let y be the number of animals Zurain owns. How can we write a function in terms of x and y?\n\nTo write the function, at very beginning, when x=0, Zurain has not bought any new animal, he owns 3 animals so, y=3 animals \"After the first month, when x = 1, Zurain owns 3 animals, plus the 1 animal he just bought. He now owns y=3+1 animals\n\nSimilarly, after the second month, when x = 2, Zurain owns 3 animals, plus the 2 new animals he bought after he started animals. He now y=3+2 animals\n\nTherefore for x animals the function will be y=3+x where, 'x'is independent variable and 'y' is dependent variable.\n\nIn mathematics, the word function is used in much the same way, but more restrictively. It is defined as:\n\nPeter Dirichlet was German Mathematician who made valuable contributions in the study of mathematics such as number theory.mechanics and analysis.\n\nHe was the first person who gave the modern definition of function in 1837.\n\n\"Ifa variable \"y\"depends on a variable 'x'in such a way that each value of 'x'determines exactly\n\none value of \"y\"then we call it y'is a function of xeg_y= ƒ(1)\n\nThe domain and range can be identified by the graph.\n\nBecause domain refers to the set of all input values, so, \"all the values shown on the x-axis. The range refers to the set of all output values. Which are shown on the y-axis. Consider the graph given in -10- Figure 2.1.\n\nIts domain is (-0,-2)-(-2,∞) and range is (-0,0)(0,∞)\n\n\"A function that contains an algebraic expression with in the absolute value symbols is called\n\nIn our previous classes we have studied that the absolute value of\n\na number is its distance from 0 on the number line.\n\nThe parent absolute value function can be written as f(x)=x which is\n\nTo graph the above absolute value functions simply choose some values of x and get the values of y then draw them accordingly.\n\nIn general, domain of f(x)=xlis (,) and range is [0,∞) but the graph is v-shaped grap Figure 2.4 shows the graph of f(x)=x).\n\nIn any absolute value function for vertical translation of f(x)=x you can use the function g(x)=(x)+* () When >0 the graph of f(x) translate \" unit up to get g(x).\n\nWhen the graph (x) translate \"A\" units down to get g(x).\n\nThis is called vertical translation. For horizontal translation of f(x) = xl you can use the function g(x)= f(x-4)\n\nWhen > the graph of (r) will translate \"k\" units to the right to get g(x).\n\nWhen the graph of(r) will translate \" units to the left to get g(x). This is called horizontal translation.\n\nSolution From the definition of absolute value function, the given function is\n\nThe inequality 3x+420 is satisfied whenever x2-, and 3x + 4 <0\n\n0, so the graph will consist of two lines that meet at\n\nUse the tabular form to obtain the graph of a function:\n\nThis function has a domain set (,) and range set is [0,∞).\n\nComposition of function can be described as a progression of \"getting\" and \"dropping\" \"off\"\". function gets \"x\" does something for it and drops it off. Then another function goes along and gets the drop off, does something for it, and drop it off once more. This pattern may proceed more than a few functions. Suppose a composition as a progression of car rides. \"x\" boy is picked up by the first car function transported to a required location and dropped off. Then another car function come and pick up the x boy at this new location transports x boy to another location and drops x boy off.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-2",
        "title": "2.2 Composite Functions",
        "theory": "Consider the function (x) whose rule is h(x)=√.To compute h(4), you first need to find x=4'-64 and then take the square root to obtain√√√64-8.So the rule of h(x) may be rephrased\n\nHere g(x)=x andƒ(x)=√. We may think of the functions f(x) and g(x) as being \"composed\" to create the function .\n\nIn other words, when the output from one function is used as the input to another function, we form what is known as a composite function.\n\n\"Iff(x) and g(x) are the two functions, then, a composite function or composition ofg and fis the function whose values are given by g(f(x)) for all x in the domain of fix) such that fix) is in the domain of g(x).\"\n\nc. (g(-2)) does not exist, since -2 is not in the domain of g.\n\nSolution a. Using the given functions to obtain:\n\nThis example shows that (g(x)) is not usually equal to g (f(x)).",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-3",
        "title": "2.3 Inverse Functions",
        "theory": "If the graph continuous beyond the given portion of the graph the domain and range can be greater than the given valu\n\nSolution The function () takes an output 3-8 in response of input r. The inverse function must take an outputt in response of input 3-8:\n\nUse these values in equation (i) to obtain: (2)==+8\n\nPut t as its argument instead of z to obtain the inverse function of f(r)-31-8: (1)='+\n\nCrumple 7 Let/(x)=2x+3 and g(x) = 3x and h(x) = f(g(x))- Write expressions for the following functions\n\na. In response of f(x) and g(x), the function A(x) b. In response of f(x), the inverse of f(x) is:\n\nc. In response of g(x), the inverse of g(x) is:\n\nCalculus was discovered as a tool of problem solving. Before the development of calculus, there were a wide range of issues that could not be addressed using the simple mathematics that was available .e.g. people did not know how to measure the speed of different objects when it was changing ever time. Another effective method was desired to calculate the area under the curve. Algebra, geometry, trigonometry and statistics were well understood, but they could not provide necessary tools to address these important issues. Some of the mathematicians of history give the credit to the ancient Greeks for discovering the calculus. But most of the scholars and mathematicians recognize Gottfried Wilhelm von Leibniz and sir, Isaac Newton developed its modern concepts in 17 century. According to the university of Laws Leibniz and Newton held different concept, while Leibniz introduced that the variables of x and y composing \"sequences of infinitely close values\". But Newton viewed them as variables that change with time. Leibniz considered calculus as a mathematical science for analysis but Newton took it being geometrical science.\n\nRead the graphs and write the function, domain and range of ƒ\n\nFind the composite functions (g(x)) and g (f(x)) of the following functions: a._f(x)=x2+l, g(x)=2x",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-4",
        "title": "2.4 Transcendental Functions",
        "theory": "\"Functions that are not algebraic are called transcendental functions.\n\nThe functions, such as all trigonometric functions, hyperbolic functions, exponential functions and logarithmic functions are called transcendental functions.\n\nA polynomial P(x) is a function of the form f(x) = P(x)=a, x+u...\n\nwith a is a nonnegative integer and a,,a,,a,,a,,a, are constants. If a, 40, then, the integer n is called the degree of the polynomial.\n\nThe constant a, is called the leading coefficient and the constant a, is called the constant term of the polynomial function. In particular, the polynomial (1) is going to be a\n\n2.4.1 Recognition of algebraic, trigonometric, inverse trigonometric, exponential, logarithmic, hyperbolic (and their identities), explicit and implicit functions, and parametric representation of functions\n\nA function f(x) is called an algebraic function if it can be constructed using algebraic operations (such as adding, subtracting, multiplying, dividing or taking roots) starting with polynomials. Any rational function is an algebraic function e.g.\n\n“Trigonometric function are the functions that describe the relationship between the sides and angles of a right triangle\".\n\nAny trigonometric function include one or more of the following 6 trigonometric ratios.\n\nThese function has completely discussed in grade (XI) Mathematics,\n\n\"Inverse trigonometric function are simply defined as the inverse functions of the basic trigonometric function.\n\nThese functions are used to get the angle with any of the trigonometric ratios. Inverse trigonometric functions are also known as \"Arc functions\" particularly these are 6 functions such as:\n\n(iv). Arc cosecant(x) = esc\"'(x) where x2lorxs-1 (v). Are secant(x) = sec(x) where x21orxs-1 (vi). Arc cotangent(x) = cot '(x) where x R\n\nInverse trigonometric functions are also termed as, cyclometric functions, arcus functions and anti trigonometric functions.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-5",
        "title": "2.5 Graphs of Functions",
        "theory": "MAPLE graphic commands for two-dimensional plot of\n\nimplicit function by restricting domain and range\n\nLook at the following example, the procedure to use the maple graphic commands is illustrated. Example 23 Use maple commands to draw the graphs of the given function.\n\n(b). Parametric function (x(t), y(t)) = cos().sin() for r=-3.5 to 3.5, x from -1.5 to 1.5 and y\n\ne). An implicit function x-x from -5 to 5 and y from -5 to 5.\n\nSolution The command below will show you full detail of plotting expressions/functions on line by typing: >?plots\n\nThis graph is obtained through right-click on the last end of the expression by selecting \"Plots< Plot Builder <2D Parametric Plot\" on the context menu.\n\nThis graph is obtained through right-click on the last end of the expression by selecting Plots <2D-Implicit Plot <x, y\" on the context menu.\n\nMAPLE package plots for plotting different types of functions\n\nLook at the following example the procedure of plotting the functions using maple package illustrated.\n\nSolution (a). f(x)=x-b,x from -1 to 10 and y from -5 to 5.\n\n(b). (x(t), y(t)) = cos(x) sin(ty)), from -1 to 2, x from - to л, from - toл The command below will show you full detail of plotting packages on line by typing\n\nThis graph is obtained through right-click on the last end of the expression by selecting \"Plots < Plot Bu <Animation (choose 2D-Implicit Plot)\" on the context menu.\n\nThis graph is obtained through right-click on the last end of the expression by selecting \"Plots Plot Builder < Animation (choose 3D-Implicit Plot + Parameter)\" on the context menu.\n\nRecognize and write the type for each of the following functions:\n\nA sealed bar contains radium. The number of grams present at time t is given by Q(r)=100043/ where is measured in years. Find the amount of radium in the bor at the following times:\n\nUsing a calculator and point-by-point to plot the following exponential functions: a. h(x)=(2\");[-5,0] b. m(x)=(3): [0,3] c. N=':[0,5] d=e\":[0,5] Using a calculator and point-by-point to plot the following logarithmic functions: a. y Inx\n\nSketch the following parametric curves: a. (x(t), y(t))=(3-1,2),t is real number. Sketch the graph of:\n\nUse maple commands to plot the graphs of the functions given in Q.1.\n\nThe algebraic problems considered in earlier sections dealt with static situations:\n\nCalculus, on the other hand, deals with dynamic situations:\n\nHow fast is a rocket going at any instant after lift-off?\n\nThe techniques of calculus will allow us to answer many questions like these that deal with rates of change.\n\nThe key idea underlying the development of calculus is the concept of limit. So we begin by studying limits after explaining the location of intervals on the real number line.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-6",
        "title": "2.6 Limits of Sequences",
        "theory": "Identify through graph the domain and range of a function.\n\nDraw the graph of modulus function (ie. y=x) and identify its domain and range.\n\nii. Find the composition of two given functions.\n\nDescribe the inverse of composition of two given functions.\n\nRecognize algebraic, trigonometric, inverse trigonometric, exponential, logarithmic, hyperbolic (and their identities), explicit and implicit functions, and parametric representation of functions.\n\nthe explicitly defined functions like y=/(x), where ƒ'(x) = e', a', log, x, log, x.\n\nthe implicitly defined functions such as x2+-and-land distinguish between graph of a\n\nxa y=b tan 8. the parametric equations of functions such as x-ar, y=2ar, x = a sec 0,\n\nUse MAPLE graphic commands for two-dimensional plot of\n\nUse MAPLE package plots for plotting different types of functions.\n\nIdentify a real number by a point on the number line.\n\n⚫ closed interval, half open and half closed intervals, on the number line.\n\nThe various types of numbers used in this book can be illustrated with a diagram called a number line. Each real number corresponds to exactly one point on the line and vice-versa. A number line with\n\nox tends to zero (x0)ox tends to a (x→ a) ox tends to infinity (x)\n\nThe answer to the phrase x tends to \"0\" is easy to see that the value of a function y = f(x) = x2-4\n\ngets closer and closer to a single real number \"2\"on both left and right sides of \"2\", when x is a number very close to \"0\" on both left and right sides of \"0\". In this situation, we are in position to say that x approaches to \"0\" or x tends to \"0\" and is denoted by x-0, when f(x) tends to a single number \"say\n\nThe answer to the phrase x tends to \"a\" (a is any real number) is easy to see that the value of a function\n\ngets closer and closer to a single real number \"24\"on both left and right sides of \"2\", when x is a number very close to \"a\" on both left and right sides of \"a\". In this situation, we say that x approaches to \"a\" or x tends to \"a\" and is denoted by x→a, when f(x) tends to a single number \"say £= 2a\". iii. x tends to infinity (x→→ ∞)\n\nThe answer to the phrase x tends to \"infinity\" is easy to see that the function f(x) =\n\ngets smaller and smaller, when x approaches \"infinity\" from either side of a number say 3, situation, we say that the function f(x) gets closer and closer to a single number \"say L = 3\" when from either side.\n\nThe number is the limit of the sequence (S.) if\n\nIf such an L exist, we say & converges, or convergent.\n\nIf 'L' does not exist, (S.) diverges or divergent. There are two notations which we use to show\n\nThese notations are abbreviated as lim S.-L or S→ L\n\n= be a sequence. To get the first few terms of this sequence we need to plug of n into the general form of the sequence. We will get the sequence terms considering integer.\n\nSimilarly, we can get more terms by using this process and write the above sequence in the\n\nIn the above sequence we treated it as a function that can only have integers plugged into them. This is an important idea which allows us to do many things with sequences that we can not compute by using other methods, To graph the sequence (5) we plot the points (n, S,) as a ranges\n\ngraph representing first 25 terms of the given sequence. From the graph we noticed that the terms of the sequence get closer and closer to zero, but not exactly equal to zero. We zero is limiting value of the sequence and it can be written as\n\n26 Represent the sequence on one dimensional space whose nth term is s1 =- Solution The sequence (s) in terms of function notation is s(n)=3. whose domain is the set of non-negative integers. The functional values of (n) develop\n\nThe one dimensional view on a real number line is shown in figure\n\nIf lima, Land limb, M, then the limit exist are the following:\n\n27 Find the limit of each of these convergent/divergent sequences.\n\nSome of the sample points near a = infinity are:\n\nIn the above expression the numerator tends to 1 asn, but the denominator appro to 0. So, the quotient increases without bound. Hence, the sequence is divergent.\n\nThe sequence does not approaches to any specific number. So it is divergent sequence by oscil The nth term is always either 1 or-1. It is 1 when n is even and -1 when n is odd.\n\n\"Let f (x) be a function defined on an open interval X Containing x = c(the value (c) needs to be defined)\n\nThe specific number L is called the limit of function f(x) as x → e if and only if, for every there exist 6-0 such that\n\nThis definition is also known as the couchy definition for limit. Usually limit of a function is written as lim f(x)= L and read as \"Lim off(x) as x→ c\n\nThis is neither desirable nor practicable to find the limit of a function by numerical approach. Ye be able to evaluate a limit in some mechanical way.\n\nTheorems on limits of sum, difference, product and quotient of function. demonstrate through examples\n\nLet f(x) and g(x) be two functions, for which lim f(x)= L and lim g(x) = M\n\nThe limit of the sum of two functions is equal to the sum of their limits lim[/(x)+g(x)] = lim /(x) + lim g(x) = L+M\n\nIL The limit of the difference of two functions is equal to the difference of their limits\n\nBy applying lim on both sides of equation (iii).\n\nBy multiplying equation (i) and equation (ii).\n\nThe limit of the quotient of the functions is equal to the quotient of their limits provided the limit of the denominator is non-zero\n\nBy using equation (i) and equation (ii). f(x)x-",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-7",
        "title": "2.7 Limits of Functions",
        "theory": "v. Find the limit of a sequence whose nth term is given.\n\nState the theorems on limits of sum, difference, product and quotient of functions and demonstrate through examples.\n\nEvaluate the limits of functions of the following types:\n\nEvaluate limits of different algebraic, exponential and trigonometric functions. Use MAPLE command limit to evaluate limit of a function.\n\nRecognize left hand and right hand limits and demonstrate through examples. Define continuity of a function at a point and in an interval.\n\nProof: In this situation, we need to divide out the numerator by denominator to obtain:\n\nBeing a polynomial, the function to the right of the above expression (i) is continuous for all values and as such its limit, when x→ a must equal to its value at x=a. Thus, the limit of the expressic when tends to a is:\n\nProof: When xa, the limit of a function is of the form\n\nwe need to rationalize the given function to obtain the required limit:\n\nProof: The base \"e\" is an irrational number (like #), it cannot be represented exactly by a decimal fraction. However, e can be approximated as closely as we like by evaluating the eu\n\nfor sufficiently large x. What happens to the value of the expression as x increases without bor results are summarized in the following table:\n\nis never close to 1, but seems to be approaching a number approaches an irrational\n\nclose to 2.7183. In fact, as increases without bound, the value of expression number that we call e. The irrational number e to twelve decimal places is:\n\nProof: If we put y=, then y→, when x->0, and the left-hand side of the limit thus gives the\n\nProof: If we put a'-1=y, then x is obtained by taking log of both sides:\n\nBy replacing 'a' with 'e' the following result can be deduced.\n\nProof: If we put (1+x)\" -1 = 2; then: (1+x)* − 1 = z\n\n→ · (1+x)\" = (l+z) Taking log of both sides to obtain:\n\nUse these expressions in the left-hand side of the limit to obtain the right-hand side:\n\nThe sandwich theorem: This is a theorem that is used in calculus to evaluate a limit of a function. It particularly useful to evaluate limits where other techniques might be unnecessarily complicated. To define sandwich theorem.\n\n\"Let f'(x), g(x) and à (x) be functions such that f(x)g(x)Sh(x) for all in some open interval containing \"2\", except possibly at itself. If lim f(x) = L and im (x)= then lim g(x)=L\n\n(b). lim (1−cosx), when lim sin x=0 and lim cos.x=1.\n\nThe procedure of using MAPLE command \"limit\" is illustrated in the following example.\n\nSolution This will show you all commands about the limits. a. Command\n\nUsing Palettes: Use cursor button to select limit palette. Click- the required limit palette and replace a by 2. Click (a+b) (for sum rule of a function), then press \"Enter\" key to obtain the required limit:\n\nIf the command for the required lim of a function is not known to ye then, easily on line, call the commu by typing:\n\nUsing Palettes: Use cursor button to select limit palette. Click-the required limit, and replace a b Click-(a*b) (for product rule of a function), then \"Enter\" key to obtain the required limit:\n\nUsing Palettes: Use cursor button to select limit palette. Click-the required limit and replace\n\n(the quotient rule of a function), then \"Enter\" key to obtain the required limit:\n\nUse algebra and the rules of limits to evaluate the following limits:\n\nFind the limit of the convergent of the following sequences:\n\nWeekly sales (in rupees) at big store r weeks after the end of an advertising campaign are given by: S(x)=5000+ 3600\n\nFind the sale for the indicated weeks limits:\n\nUse MAPLE command \"limit\" to evaluate the limit of all parts of Q.1. Use algebraic techniques to evaluate the following.\n\nWhat type of function are represented by the curves drawn on each image?\n\nBefore discussion about continuous and discontinuous function we will revise the concept o limit of a function, which we have done in previous Section 2.6.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-2-8",
        "title": "2.8 Continuous and Discontinuous Functions",
        "theory": "Test continuity and discontinuity of a function at a point and in an interval.\n\nUse MAPLE command iscont to test continuity of a function at a point and in a given interval.\n\nThe concept of function and its limit is fundamental idea to us, in the study of mathematics that distinguishes calculus from algebra and trigonometry. In this unit, we will revise the concept of function from unit-8 of grade-XI mathematics and then develop the concept of limit which is the fundamental building block on which all the calculus concepts are based.\n\nIt is a value the function approaches as the x-values approach the limit from one side only i.e. th left side limit and the right side limit.\n\nA given function f(x) has a left hand limit if f(x) can be made as close to the number. *L* we please for all values of x<ce.g.\n\nA function f(x) has a right hand limit if f(x) can be made as to the number \"L\" as we ples\n\n\"In general, the function has a limit as x approaches e if both the left hand and right hand limit c exist and are el.\n\nSince lim f(x) lim f(x) Therefore, lim (r) does not exist.\n\nHere, we observed that sometimes lim f(x) = f(x) and sometime it does not and also some f(c) is not defined whereas lim f(x) = f(x) exist.\n\nA function is said to be a continuous function at a point if two sided limit at that point exi equal to the function's value e.g. Consider a function f(x), it is continuous at the point x=c if.\n\nIf any one of the above condition does not satisfied then the function is not continuous.\n\nNow, look at the following graph of function.\n\nA function is said to be a discontinuous function at a point 'e' if one of the three conditions of continuity does not satisfy.\n\nIt can be seen that the side limits consider with the value of the function with the point.\n\n\"A function is said to be a continuous function in dn interval when the function fined at every point in that interval and no jumps or breaks invol\n\nIf some functions f(x) satisfies these criteria from xa to x and we say that f(x) is continuous on the interval [a,b]. 2.8.3\n\nf(x) is continuous over the closed interval [a, b] if it is continuous on the (a, b) interval.\n\nTest of continuity and discontinuity of a function at a point and in an interval\n\nSolution In order to check the continuity of the function f(x) at x=-2. We will have to check the function for all three conditions as we have done in Example 37.\n\nHence, ƒ(-2) is not defined. We know that if any of the three conditions of continuity does not satisfy, the function will discontinuous.\n\nTherefore, f(x) is discontinuous function at x=-\n\nHowever, if we try to find the limit of (x), we conclude that f(x) is continuous on all the values other than --2.\n\nThis implies that f(x) is continuous at all the values of x other than -2.\n\nThe graph of p(x) is shown in the Figure 2.34 From the graph of the function, the left, right limits\n\nFrom the graph of the function, the limit and the value of the function are equal:\n\nSometimes functions nood to be defined in pieces, because they have a split domain. These function more than one formula to define the function, and therefore these types of functions are called continuous functions.\n\nLook at the lowing example The procedure of using the maple command for continuity of a function is illustrated in this example. Prample 40 Use maple command \"iscount\" to check the continuity of function\n\n(a). Internal from 0 to 1. (b). Closed interval [0, 1]. (c). Open interval (0, 1).\n\nCreate at least five functions randomly then use MAPLE command \"iscont\" to check their on interval (0,1)\n\nUse properties of continuous function to test the continuity and discontinuity of the following functions:\n\nUse the graph of the function g(x) to answer the following questions:\n\na. Is g(x) continuous on the open interval (-1, 2)?\n\nb. Is g(x) continuous from the right at x=-1?\n\nd. Is g(r) continuous on the closed interval [-1, 2]?\n\nUse the graph of the function f(x) to answer the following questions:\n\nIs f(x) continuous on the open interval (0, 3)?\n\nd. Is g(r) continuous on the closed interval [0,3]?\n\nGraph and locate all points of discontinuity of the following piecewise functions:\n\nPersonal computer salesperson receives a base salary of $1,000 per month and a commission of 5% of all sales over $10,000 during the month. If the monthly sales are $20,000 or more, the salesperson is given an additional $500 bonus. Let E(s) represents the person's earnings during the month as a function of the monthly sales. a. Graph E(s) for 0 S$30,000\n\nUse MAPLE command \"iscont\" to test the continuity of f(x)=\n\nIfy is expressed in term of x as y-f(x) then y is called:\n\nA function = f(x) is a rule that assigns for each value of the independent variable x a unique value of the dependent variable y\n\nA function that defined by more than one equation is called a compound function.\n\nThe graph of a function f(x) consists of all points whose coordinates (x, y) satisfy a function y= f(x), for all x in the domain of f(x).\n\nLet y = f(x) be a function of x. This function takes an dependent variable y in response of independent variable x. The function that takes x as dependent variable in response of y as the independent is then called the inverse function of(x) and is denoted by: x=",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-2-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Find the domain and range of the function whose graph is shown in the Figure 2.2. Solution Here the horizontal extent is -6 to 2. So, the domain of the function is re[-6,2] vertical extent of the grah is 0 to 4. So the range of the function is ye [0,4]. Shown in the Figure 2.3",
        "given": "",
        "method": "",
        "steps": [
          "2.1.2 Graph of modulus function (i.e. y=x) and its domain and range",
          "\"A function that contains an algebraic expression with in the absolute value symbols is called",
          "In our previous classes we have studied that the absolute value of",
          "a number is its distance from 0 on the number line.",
          "The parent absolute value function can be written as f(x)=x which is",
          "To graph the above absolute value functions simply choose some values of x and get the values of y then draw them accordingly.",
          "In general, domain of f(x)=xlis (,) and range is [0,∞) but the graph is v-shaped grap Figure 2.4 shows the graph of f(x)=x).",
          "In any absolute value function for vertical translation of f(x)=x you can use the function g(x)=(x)+* () When >0 the graph of f(x) translate \" unit up to get g(x).",
          "When the graph (x) translate \"A\" units down to get g(x).",
          "This is called vertical translation. For horizontal translation of f(x) = xl you can use the function g(x)= f(x-4)",
          "When > the graph of (r) will translate \"k\" units to the right to get g(x).",
          "When the graph of(r) will translate \" units to the left to get g(x). This is called horizontal translation."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Graph the following absolute value functions and identify its domain and range: f(x)= |3x-4|",
        "given": "",
        "method": "",
        "steps": [
          "The inequality 3x+420 is satisfied whenever x2-, and 3x + 4 <0",
          "0, so the graph will consist of two lines that meet at",
          "Use the tabular form to obtain the graph of a function:",
          "This function has a domain set (,) and range set is [0,∞).",
          "Composition of function can be described as a progression of \"getting\" and \"dropping\" \"off\"\". function gets \"x\" does something for it and drops it off. Then another function goes along and gets the drop off, does something for it, and drop it off once more. This pattern may proceed more than a few functions. Suppose a composition as a progression of car rides. \"x\" boy is picked up by the first car function transported to a required location and dropped off. Then another car function come and pick up the x boy at this new location transports x boy to another location and drops x boy off.",
          "Consider the function (x) whose rule is h(x)=√.To compute h(4), you first need to find x=4'-64 and then take the square root to obtain√√√64-8.So the rule of h(x) may be rephrased",
          "Here g(x)=x andƒ(x)=√. We may think of the functions f(x) and g(x) as being \"composed\" to create the function .",
          "In other words, when the output from one function is used as the input to another function, we form what is known as a composite function.",
          "\"Iff(x) and g(x) are the two functions, then, a composite function or composition ofg and fis the function whose values are given by g(f(x)) for all x in the domain of fix) such that fix) is in the domain of g(x).\""
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Let /(x)=2x-1 and g(x)=√3x+5. Find each of the following:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-4",
        "num": "4",
        "title": "Example 4",
        "problem": "Let f(x)=4x+1 and g(x)=2x2+5x. Find each of the following:",
        "given": "",
        "method": "",
        "steps": [
          "This example shows that (g(x)) is not usually equal to g (f(x))."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-5",
        "num": "5",
        "title": "Example 5",
        "problem": "Air pollution is a problem for many metropolitan areas. Suppose that carbon monoxide is measured as a function of the number of people according to the following information:",
        "given": "",
        "method": "",
        "steps": [
          "Further assume that the population of a given metropolitan area is growing according to the formula p(r)=1+0.02r,where t is the time from now (in years) and p is the population (in hundred thousands). Based on these assumptions, what level of air pollution should be expected in 4 years? Solution The level of pollution at time t is given by the composite function:",
          "The air pollution expected in 4 years is obtained by putting = 4 in equation L(p(t)) = L(1+0.02r\")=0.71+0.02(4)+3-2.0 ppm",
          "\"Let y= f(x) be a function of x. This function takes a dependent variable y in response of independen variable x. The function that takes x as dependent variable in response of y as the independent is then called the inverse function off(x)\".",
          "The symbol \"() means the inverse of ƒ and does not mean",
          "If f(x) is not one-to-on then f(x) does not have an inverse function.",
          "For example, if y=f(x) is one-to-one function, then the inverse of y= f(x) is the function x = f(y) formed by interchanging the independent and dependent variables x and y for y = f(x). Thus, if (a, b) is a point on the graph of f(x), then (b, a) will be a point on the graph of the inverse of f(x). The domain and range of y = f(x) are also valid for its inverse function x = \"(y)",
          "2.3.1 Inverse of the composition of two given functions Cumple 6 Find the inverse function of f()-31-8.",
          "Solution The function () takes an output 3-8 in response of input r. The inverse function must take an outputt in response of input 3-8:",
          "Use these values in equation (i) to obtain: (2)==+8",
          "Put t as its argument instead of z to obtain the inverse function of f(r)-31-8: (1)='+",
          "Crumple 7 Let/(x)=2x+3 and g(x) = 3x and h(x) = f(g(x))- Write expressions for the following functions",
          "a. In response of f(x) and g(x), the function A(x) b. In response of f(x), the inverse of f(x) is:",
          "c. In response of g(x), the inverse of g(x) is:",
          "Calculus was discovered as a tool of problem solving. Before the development of calculus, there were a wide range of issues that could not be addressed using the simple mathematics that was available .e.g. people did not know how to measure the speed of different objects when it was changing ever time. Another effective method was desired to calculate the area under the curve. Algebra, geometry, trigonometry and statistics were well understood, but they could not provide necessary tools to address these important issues. Some of the mathematicians of history give the credit to the ancient Greeks for discovering the calculus. But most of the scholars and mathematicians recognize Gottfried Wilhelm von Leibniz and sir, Isaac Newton developed its modern concepts in 17 century. According to the university of Laws Leibniz and Newton held different concept, while Leibniz introduced that the variables of x and y composing \"sequences of infinitely close values\". But Newton viewed them as variables that change with time. Leibniz considered calculus as a mathematical science for analysis but Newton took it being geometrical science.",
          "Read the graphs and write the function, domain and range of ƒ",
          "Find the composite functions (g(x)) and g (f(x)) of the following functions: a._f(x)=x2+l, g(x)=2x",
          "Determine the inverse function of (g(x)) and g (f(x)) for the following functions:",
          "Observe the following graphs and identify their domain and range.",
          "\"Functions that are not algebraic are called transcendental functions.",
          "The functions, such as all trigonometric functions, hyperbolic functions, exponential functions and logarithmic functions are called transcendental functions.",
          "A polynomial P(x) is a function of the form f(x) = P(x)=a, x+u...",
          "with a is a nonnegative integer and a,,a,,a,,a,,a, are constants. If a, 40, then, the integer n is called the degree of the polynomial.",
          "The constant a, is called the leading coefficient and the constant a, is called the constant term of the polynomial function. In particular, the polynomial (1) is going to be a",
          "2.4.1 Recognition of algebraic, trigonometric, inverse trigonometric, exponential, logarithmic, hyperbolic (and their identities), explicit and implicit functions, and parametric representation of functions",
          "A function f(x) is called an algebraic function if it can be constructed using algebraic operations (such as adding, subtracting, multiplying, dividing or taking roots) starting with polynomials. Any rational function is an algebraic function e.g.",
          "“Trigonometric function are the functions that describe the relationship between the sides and angles of a right triangle\".",
          "Any trigonometric function include one or more of the following 6 trigonometric ratios.",
          "These function has completely discussed in grade (XI) Mathematics,",
          "\"Inverse trigonometric function are simply defined as the inverse functions of the basic trigonometric function.",
          "These functions are used to get the angle with any of the trigonometric ratios. Inverse trigonometric functions are also known as \"Arc functions\" particularly these are 6 functions such as:",
          "(iv). Arc cosecant(x) = esc\"'(x) where x2lorxs-1 (v). Are secant(x) = sec(x) where x21orxs-1 (vi). Arc cotangent(x) = cot '(x) where x R",
          "Inverse trigonometric functions are also termed as, cyclometric functions, arcus functions and anti trigonometric functions.",
          "Inverse trigonometric functions are widely used in the field of physics, engineering, geometry and navigations.",
          "The exponential function has widespread application in many areas of science and engineering. Areas which utilize the exponential function include expansion of materials, laws of cooling, radioactive decay and the discharge of a capacitor.",
          "bis a positive constant, defines an exponential of the set of all real numbers,",
          "We require the base to be positive and to avoid imaginary numbers such as (-2)=√√-2=i√2. We conclude b=1 as a base, since f(x)=1-1 is a constant function.",
          "If a and b are positive real numbers, a#1 and #1, then,",
          "Of all possible bases b, it can use for the exponential function yb, which ones are the most useful? If you look at the keys on a scientific calculator, you will likely see 10\" and e\". It is clear why base 10 would be important, because our number system is a base 10 system. But what is e, and why is it included as a base? It turns out that base e is used more frequently than all other bases combined. The reason for this is that certain formulas and the results of certain processes found in calculus and more advanced mathematics take on their simplest form if this base is used. This is why you will see e used extensively in expressions and formulas that model real-world phenomena. In fact, its use is so prevalent that you will often hear people refer to ye as the exponential function. The base e is an irrational number (like) it cannot be represented exactly by any finite decimal fraction. However, e can be approximated as closely as we like by evaluating the expression",
          "for sufficiently large x. What happens to the value of expression (i) as x increases without bound? The results are summarized in the following table:",
          "Interestingly, the value of expression (i) is never close to 1, but seems to be approaching a number close to 2.7183. In fact, as x increases without bound, the value of expression approaches an irrational number that we call e. The irrational number e to twelve decimal places is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-6",
        "num": "8",
        "title": "Example 8",
        "problem": "Cholera, an intestinal disease, is caused by a cholera bacterium that multiplies exponentially by cell division as given approximately by",
        "given": "",
        "method": "",
        "steps": [
          "(a) 1 hour? 3 hours? Solution Use the amount of initial bacteria No=25 in the",
          "The bacteria at a time = 1 hour is obtained by putting",
          "The bacteria at a time - 3 hours is obtained by putting M",
          "The bacteria at a time r-4 hours is obtained by putting 1-4 in equation (1):",
          "Thus, we conclude that the population of bacteria is growing when timer increases.",
          "Logarithms are an alternative way of writing expressions which involve powers or indices. They are used extensively in the study of sound. The decimals used in defining the intensity of sound, is based on a logarithmic scale.",
          "Until the development of computers and calculators, logarithms were the only effective tool for large scale numerical computations. They are no longer needed for this, but it still plays a crucial role in many applications.",
          "For illustration, if we start with the exponential function y = f(x) defined by y=2\" then the interchange of the variables is giving the inverse of y=2\":",
          "We call this inverse exponential function, the logarithmic function with base 2, and write this as: y=log, if and only if x=2'",
          "\"The inverse of an exponential tancom relied a logarithmic function. For b>0 and bal. the logarithmic function is: y log which is equivalent to x=",
          "The log to the base of x is the exponent to which b must be raised to obtain r. The domain of the logarithmic function is the set of all positive real numbers, which is also the range of the corresponding exponential function. Obviously, the range of the logarithmic function is the set of all real numbers, which is also the domain of the corresponding exponential function.",
          "Typical graphs of an exponential function and its inverse, a logarithmic are shown in the Figure 2 NOT FOR SALE",
          "Common Logarithms are logarithms with base 10: y=log, means 10\" = x",
          "\"Log x\", which is read \"the logarithm of x\", is the answer to the question\" to what exponent must 10 be raised to produce x ?"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-7",
        "num": "9",
        "title": "Example 9",
        "problem": "Evaluate the following logarithmic functions:",
        "given": "",
        "method": "",
        "steps": [
          "Natural Logarithms are logarithms with base e: - In x means e'= x",
          "\"In x\", which is read \"the el-en of x\", is the answer to the question\" to what exponent must e be raised to produce \"?",
          "'y log, x\", which is read \"y is the logarithm of x to the base b\", is the answer to the question\" to what power must b be raised to produce x?",
          "If b, M and N are positive real numbers bel, and p and x are also any positive real numbers, then: i. log, 1-0 ii. log,b=1 iii. log, b'=x"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-8",
        "num": "10",
        "title": "Example 10",
        "problem": "Find x to four decimal places for the following indicated exponential functions:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-9",
        "num": "11",
        "title": "Example 11",
        "problem": "Two people with the covid-19 positive visited the campus of Peshawar University. The",
        "given": "",
        "method": "",
        "steps": [
          "How many days will it take for the virus to infecta. 500 people? b. 5000 people?",
          "Solution The number of days 7 that will take for the flu virus to infect n people is given by",
          "The number of days that will take for the virus to infect 500 people, is obtained by putting = equation (i):",
          "10,000-500 4998(500) -1.43 (-5.57275)=7.96903-8 days",
          "In physics, it is shown that a heavy, flexible cable (for example a power line) that is suspended between two points at the same height assumes the shape of a curve called a catenary, with an equation",
          "This is one of several important applications that involve combinations of exponential functions. In certain ways, the functions we shall study are analogous to be trigonometric functions, and they have essentially the same relationship to the hyperbola that the trigonometric functions have to the circle. For this reason, these functions are called hyperbolic functions. Three basic functions are the hyperbolic sine (denoted \"sinhx\" and pronounced \"cinch\"), the hyperbolic cosine (coshr; pronounced \"kosh\") and the hyperbolic tangent (tanhx; pronounced \"tansh\"). They are listed as under:",
          "The name \"hyperbolic functions\" comes from the fact that the functions sinht and cosht play the same role in the parametric representation of the hyperbolic x-y-1, as the trigonometric functions sint and cost, do in the parametric representation of the circle x2 + y2 = 1.",
          "Eliminating the parameter't from the parametric equations x=cost, y sint",
          "to obtain the equation of the circle: x+y=cost+sint=1",
          "are the parametric equations of the hyperbola. Squaring these equations and subtracting the second from the first to obtain the equation of hyperbola: x-y=cosh' t-sinh t=1",
          "If y is equated to an expression involving only x terms, then we say that y is expressed explicitly",
          "Sometimes we have an equation connecting x and y but it is impossible to write it in the form of y=√(x):",
          "In these cases we say that y is expressed implicitly in terms of x.",
          "The following curves are modeled through implicit functions:",
          "It is sometimes useful to define the variables x and y in the ordered pair (x, y), so that they are each functions of some other variable, say r",
          "The domain of these functions/(f) and g (1) is some interval D. The variable r is called a parameter and x=ƒ(r) and y=g() are called the parametric equations.",
          "\"If (t) and g(t) are continuous functions of parameter t on an interval D, then the equations",
          "are called the parametric equations for the plane curve generated by the set of ordered pairs in the plane:",
          "12 Sketch the graph of the parametric functions (x(t), y(t))=(3-1,21) for all r.",
          "Solution The graph is the collection of all points (x, y) with",
          "the Figure 7.0 developed a straight line parallel to the direction vector u = (-1,2) and passing through the point p (3,0).",
          "In our previous classes we have learnt that graphical representations refers to the use of intuitive charts to clearly visualize and simplify the given data sets. The data is ingested into the graphical representation of software and then represented by the different symbols. Like, curves, bars and slices on the chart.",
          "(a) Graphical display of explicit defined functions like",
          "Solution Use a scientific calculator to create the table of points. Plot",
          "these points and then join them to obtain the graphs of smooth curves in the Figure 2.10. The domain set is (-),while the range set is (0,0).",
          "ii. Graphically representation of / L Example 14 Sketch the graph of y=2\".",
          "Solution To hand sketch graphs of equations such as y = 2′′ or j = 2, simply make a tables by assigning integers to x, plot the resulting points, and then join these points with a smooth curve as shown in Figure 2.11,",
          "It is useful to compare the graphs y=2 and y=2\" by plotting both on the same set of coordinate ares as shown in Figures 2.12. The graph of f(x)=b', b>1 shown in Figure 2.13 looks very much like the graph of y=2\", and the graph of (x)=6, 0<b<l in Figure 2.13 looks very much like the graph of y=2\"",
          "The graphs in Figures 2.12 and Figures 2.13 suggest the following important general properties of exponential functions that are summarized in the box below:",
          "1. All graphs will pass through the point (0,1).",
          "2. All graphs are continuous curves, with no holes or jumps. 3. If b>1, then b' increases as x increases.",
          "Graphically representation of log.x and log.x"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-10",
        "num": "15",
        "title": "Example 15",
        "problem": "Sketch the graph of y=log.",
        "given": "",
        "method": "",
        "steps": [
          "The graphs of y=2' and y=log,x are shown in the Figure 2.14."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-11",
        "num": "16",
        "title": "Example 16",
        "problem": "Sketch the graph of y=log,(x-2).",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-12",
        "num": "17",
        "title": "Example 17",
        "problem": "Sketch the graph of y= Inx",
        "given": "",
        "method": "",
        "steps": [
          "Any ordered pair of numbers on the graph of the exponential function will be on the graph of logarithmic function if we interchange the order of the components.",
          "If we fold the paper along the dashed line y = x, u two graphs match exactly.",
          "The line y=x is a line of symmetry for the tw graphs.",
          "(b) Graphical display of implicit defined function such as x2+y=a2 and",
          "and distinguish between graph of a function and of an equation"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-13",
        "num": "18",
        "title": "Example 18",
        "problem": "Sketch the graph of x2+ y2=9.",
        "given": "",
        "method": "",
        "steps": [
          "The standard form of equation of circle is (x-h)2+(y-k)2 = r2",
          "So, this is a circle of radius 3 centred at origin (0, 0)."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-14",
        "num": "19",
        "title": "Example 19",
        "problem": "Sketch the graph of",
        "given": "",
        "method": "",
        "steps": [
          "The students will learn more about conic in unit 8 and 9.",
          "(c) Graphical display of parametric equation functions such as x=ar, y=2at;"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-15",
        "num": "20",
        "title": "Example 20",
        "problem": "Sketch the graph of the parametric function (x(t), y(t)) = (3r2. 4t + 3).",
        "given": "",
        "method": "",
        "steps": [
          "This is a right opening parabola, its graph is shown in Figure 2.19."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-16",
        "num": "21",
        "title": "Example 21",
        "problem": "Sketch the graph of the parametric function (x(t), y(t))=(3.cos (t), 2.sin (t)) for 0≤1527 Solution To sketch the graph of the parametric equation. Let's make a table to get the idea of the shape and direction of the graph..",
        "given": "",
        "method": "",
        "steps": [
          "This is an ellipse, which will be discussed in detail in unit-9.",
          "(d) Graphical display of discontinuous functions of the type"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-17",
        "num": "22",
        "title": "Example 22",
        "problem": "Graph the compound function:",
        "given": "",
        "method": "",
        "steps": [
          "b. Use the function f(x)=x+2 for -2sx<2 to obtain a set of points:",
          "e. Use the function f(x)= 1 for x 2 2 to obtain a set of points:",
          "Use these tabular points to obtain the graph of a compound function in Figure 2.20.",
          "MAPLE graphic commands for two-dimensional plot of",
          "implicit function by restricting domain and range",
          "Look at the following example, the procedure to use the maple graphic commands is illustrated. Example 23 Use maple commands to draw the graphs of the given function.",
          "(b). Parametric function (x(t), y(t)) = cos().sin() for r=-3.5 to 3.5, x from -1.5 to 1.5 and y",
          "e). An implicit function x-x from -5 to 5 and y from -5 to 5.",
          "Solution The command below will show you full detail of plotting expressions/functions on line by typing: >?plots",
          "This graph is obtained through right-click on the last end of the expression by selecting \"Plots< Plot Builder <2D Parametric Plot\" on the context menu.",
          "This graph is obtained through right-click on the last end of the expression by selecting Plots <2D-Implicit Plot <x, y\" on the context menu.",
          "MAPLE package plots for plotting different types of functions",
          "Look at the following example the procedure of plotting the functions using maple package illustrated."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-18",
        "num": "24",
        "title": "Example 24",
        "problem": "Use MAPLE commands to draw the following functions.",
        "given": "",
        "method": "",
        "steps": [
          "(b). (x(t), y(t)) = cos(x) sin(ty)), from -1 to 2, x from - to л, from - toл The command below will show you full detail of plotting packages on line by typing",
          "This graph is obtained through right-click on the last end of the expression by selecting \"Plots < Plot Bu <Animation (choose 2D-Implicit Plot)\" on the context menu.",
          "This graph is obtained through right-click on the last end of the expression by selecting \"Plots Plot Builder < Animation (choose 3D-Implicit Plot + Parameter)\" on the context menu.",
          "Recognize and write the type for each of the following functions:",
          "A sealed bar contains radium. The number of grams present at time t is given by Q(r)=100043/ where is measured in years. Find the amount of radium in the bor at the following times:",
          "Using a calculator and point-by-point to plot the following exponential functions: a. h(x)=(2\");[-5,0] b. m(x)=(3): [0,3] c. N=':[0,5] d=e\":[0,5] Using a calculator and point-by-point to plot the following logarithmic functions: a. y Inx",
          "Sketch the following parametric curves: a. (x(t), y(t))=(3-1,2),t is real number. Sketch the graph of:",
          "Use maple commands to plot the graphs of the functions given in Q.1.",
          "The algebraic problems considered in earlier sections dealt with static situations:",
          "Calculus, on the other hand, deals with dynamic situations:",
          "How fast is a rocket going at any instant after lift-off?",
          "The techniques of calculus will allow us to answer many questions like these that deal with rates of change.",
          "The key idea underlying the development of calculus is the concept of limit. So we begin by studying limits after explaining the location of intervals on the real number line.",
          "2.6.1 Identification of a real number by a point on the number line",
          "The various types of numbers used in this book can be illustrated with a diagram called a number line. Each real number corresponds to exactly one point on the line and vice-versa. A number line with",
          "2.31: several sample numbers located on it is shown in Figure",
          "2.6.1 Representation of open interval, closed interval, half open and half",
          "\"A set that consists of all the real numbers between two points is called an interval.",
          "A special notation will be used to indicate an interval on the real number line.",
          "For example, the interval including all numbers x, where--2 < x <3 is written as (-2, 3). Th parentheses indicate that the number-2-and 3 are not included.",
          "If-2 and 3 are to be included in the interval, square brackets are used, as in [-2, 3]. The chart below shows several typical intervals, where a <b:",
          "Both a and b are included- a is included, b is not. b is included, a is not.",
          "Interval notation is also used to describe sets such as the set of all numbers x, with x2-2. Th interval is written[-2,00)."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-19",
        "num": "24",
        "title": "Example 24",
        "problem": "Represent the following intervals on number line.",
        "given": "",
        "method": "",
        "steps": [
          "The symbol, read \"infinity\" does not represent a number. It simply indicates that all numbe greater than -2 are in the interval. Similarly, the notation (-2) indicates the set of all",
          "The graph of the interval [-2, 1] is as under."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-20",
        "num": "25",
        "title": "Example 25",
        "problem": "Use number line to indicate the interval notation:",
        "given": "",
        "method": "",
        "steps": [
          "ox tends to zero (x0)ox tends to a (x→ a) ox tends to infinity (x)",
          "The answer to the phrase x tends to \"0\" is easy to see that the value of a function y = f(x) = x2-4",
          "gets closer and closer to a single real number \"2\"on both left and right sides of \"2\", when x is a number very close to \"0\" on both left and right sides of \"0\". In this situation, we are in position to say that x approaches to \"0\" or x tends to \"0\" and is denoted by x-0, when f(x) tends to a single number \"say",
          "The answer to the phrase x tends to \"a\" (a is any real number) is easy to see that the value of a function",
          "gets closer and closer to a single real number \"24\"on both left and right sides of \"2\", when x is a number very close to \"a\" on both left and right sides of \"a\". In this situation, we say that x approaches to \"a\" or x tends to \"a\" and is denoted by x→a, when f(x) tends to a single number \"say £= 2a\". iii. x tends to infinity (x→→ ∞)",
          "The answer to the phrase x tends to \"infinity\" is easy to see that the function f(x) =",
          "gets smaller and smaller, when x approaches \"infinity\" from either side of a number say 3, situation, we say that the function f(x) gets closer and closer to a single number \"say L = 3\" when from either side.",
          "The number is the limit of the sequence (S.) if",
          "If such an L exist, we say & converges, or convergent.",
          "If 'L' does not exist, (S.) diverges or divergent. There are two notations which we use to show",
          "These notations are abbreviated as lim S.-L or S→ L",
          "2.6.5 Limit of a sequence whose no term is given",
          "= be a sequence. To get the first few terms of this sequence we need to plug of n into the general form of the sequence. We will get the sequence terms considering integer.",
          "Similarly, we can get more terms by using this process and write the above sequence in the",
          "In the above sequence we treated it as a function that can only have integers plugged into them. This is an important idea which allows us to do many things with sequences that we can not compute by using other methods, To graph the sequence (5) we plot the points (n, S,) as a ranges",
          "graph representing first 25 terms of the given sequence. From the graph we noticed that the terms of the sequence get closer and closer to zero, but not exactly equal to zero. We zero is limiting value of the sequence and it can be written as",
          "26 Represent the sequence on one dimensional space whose nth term is s1 =- Solution The sequence (s) in terms of function notation is s(n)=3. whose domain is the set of non-negative integers. The functional values of (n) develop",
          "The one dimensional view on a real number line is shown in figure",
          "If lima, Land limb, M, then the limit exist are the following:",
          "27 Find the limit of each of these convergent/divergent sequences.",
          "Some of the sample points near a = infinity are:",
          "In the above expression the numerator tends to 1 asn, but the denominator appro to 0. So, the quotient increases without bound. Hence, the sequence is divergent.",
          "The sequence does not approaches to any specific number. So it is divergent sequence by oscil The nth term is always either 1 or-1. It is 1 when n is even and -1 when n is odd.",
          "\"Let f (x) be a function defined on an open interval X Containing x = c(the value (c) needs to be defined)",
          "The specific number L is called the limit of function f(x) as x → e if and only if, for every there exist 6-0 such that",
          "This definition is also known as the couchy definition for limit. Usually limit of a function is written as lim f(x)= L and read as \"Lim off(x) as x→ c",
          "This is neither desirable nor practicable to find the limit of a function by numerical approach. Ye be able to evaluate a limit in some mechanical way.",
          "Theorems on limits of sum, difference, product and quotient of function. demonstrate through examples",
          "Let f(x) and g(x) be two functions, for which lim f(x)= L and lim g(x) = M",
          "The limit of the sum of two functions is equal to the sum of their limits lim[/(x)+g(x)] = lim /(x) + lim g(x) = L+M"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-21",
        "num": "28",
        "title": "Example 28",
        "problem": "If f(x) = x2+2x+3 and g(x)=x-4 then calculate lim[ƒ(x)+g(x)]",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-22",
        "num": "29",
        "title": "Example 29",
        "problem": "If f(x)=x-7 and g(x)=x+3x+2 then calculate lim[ƒ(x) − g(x)]",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-23",
        "num": "30",
        "title": "Example 30",
        "problem": "If f(x)=x+5 and g(x)=2x-4 then calculate lim[/(x)g(x)] Solution Since,",
        "given": "",
        "method": "",
        "steps": [
          "By applying lim on both sides of equation (iii).",
          "The limit of the quotient of the functions is equal to the quotient of their limits provided the limit of the denominator is non-zero"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-24",
        "num": "31",
        "title": "Example 31",
        "problem": "If f(x)=x-4 and g(x)=x+3 then calculate lim",
        "given": "",
        "method": "",
        "steps": [
          "By applying lim on both sides of equation (iii).",
          "2.7.1 Llimits of the functions of the following types",
          "Proof: In this situation, we need to divide out the numerator by denominator to obtain:",
          "Being a polynomial, the function to the right of the above expression (i) is continuous for all values and as such its limit, when x→ a must equal to its value at x=a. Thus, the limit of the expressic when tends to a is:",
          "Proof: When xa, the limit of a function is of the form",
          "we need to rationalize the given function to obtain the required limit:",
          "Proof: The base \"e\" is an irrational number (like #), it cannot be represented exactly by a decimal fraction. However, e can be approximated as closely as we like by evaluating the eu",
          "for sufficiently large x. What happens to the value of the expression as x increases without bor results are summarized in the following table:",
          "is never close to 1, but seems to be approaching a number approaches an irrational",
          "close to 2.7183. In fact, as increases without bound, the value of expression number that we call e. The irrational number e to twelve decimal places is:",
          "Proof: If we put y=, then y→, when x->0, and the left-hand side of the limit thus gives the",
          "Proof: If we put a'-1=y, then x is obtained by taking log of both sides:",
          "By replacing 'a' with 'e' the following result can be deduced.",
          "Proof: If we put (1+x)\" -1 = 2; then: (1+x)* − 1 = z",
          "→ · (1+x)\" = (l+z) Taking log of both sides to obtain:",
          "Use these expressions in the left-hand side of the limit to obtain the right-hand side:",
          "The sandwich theorem: This is a theorem that is used in calculus to evaluate a limit of a function. It particularly useful to evaluate limits where other techniques might be unnecessarily complicated. To define sandwich theorem.",
          "\"Let f'(x), g(x) and à (x) be functions such that f(x)g(x)Sh(x) for all in some open interval containing \"2\", except possibly at itself. If lim f(x) = L and im (x)= then lim g(x)=L",
          "e. Prove that lim=1 if angle'x is measured in radian.",
          "Proof: Take a positive acute central angle of a circle with radius",
          "In term of x, the areas are expressed as produce 20 to S so, that",
          "Area of AORO < Area of sector ORO < Area of A SRO,",
          "As sin x is positive, so, dividing by sinx we get",
          "Since is sandwiched between 1 and a quantity approaches 1 itself.",
          "Therefore, by the sandwich theorem, it must also approach I ie., lim",
          "2.7.2 Limits of different algebraic, exponential and trigonometric functions The idea of limits in the above situations is illustrated in the following examples:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-25",
        "num": "32",
        "title": "Example 32",
        "problem": "Evaluate lim",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-26",
        "num": "33",
        "title": "Example 33",
        "problem": "Evaluate lim x-3x-2).",
        "given": "",
        "method": "",
        "steps": [
          "2.7.3 MAPLE Command to evaluate limit of a function",
          "The procedure of using MAPLE command \"limit\" is illustrated in the following example.",
          "Solution This will show you all commands about the limits. a. Command",
          "Using Palettes: Use cursor button to select limit palette. Click- the required limit palette and replace a by 2. Click (a+b) (for sum rule of a function), then press \"Enter\" key to obtain the required limit:",
          "If the command for the required lim of a function is not known to ye then, easily on line, call the commu by typing:",
          "Using Palettes: Use cursor button to select limit palette. Click-the required limit, and replace a b Click-(a*b) (for product rule of a function), then \"Enter\" key to obtain the required limit:",
          "Using Palettes: Use cursor button to select limit palette. Click-the required limit and replace",
          "(the quotient rule of a function), then \"Enter\" key to obtain the required limit:",
          "Use algebra and the rules of limits to evaluate the following limits:",
          "Find the limit of the convergent of the following sequences:",
          "Weekly sales (in rupees) at big store r weeks after the end of an advertising campaign are given by: S(x)=5000+ 3600",
          "Find the sale for the indicated weeks limits:",
          "Use MAPLE command \"limit\" to evaluate the limit of all parts of Q.1. Use algebraic techniques to evaluate the following.",
          "What type of function are represented by the curves drawn on each image?",
          "Before discussion about continuous and discontinuous function we will revise the concept o limit of a function, which we have done in previous Section 2.6.",
          "It is a value the function approaches as the x-values approach the limit from one side only i.e. th left side limit and the right side limit.",
          "A given function f(x) has a left hand limit if f(x) can be made as close to the number. *L* we please for all values of x<ce.g.",
          "A function f(x) has a right hand limit if f(x) can be made as to the number \"L\" as we ples",
          "\"In general, the function has a limit as x approaches e if both the left hand and right hand limit c exist and are el."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-27",
        "num": "36",
        "title": "Example 36",
        "problem": "Determine whether lim f(x) and lim f(x) exist, if",
        "given": "",
        "method": "",
        "steps": [
          "Here, we observed that sometimes lim f(x) = f(x) and sometime it does not and also some f(c) is not defined whereas lim f(x) = f(x) exist.",
          "2.8.2 Continuity of a function at a point and in an interval",
          "A function is said to be a continuous function at a point if two sided limit at that point exi equal to the function's value e.g. Consider a function f(x), it is continuous at the point x=c if.",
          "If any one of the above condition does not satisfied then the function is not continuous."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-28",
        "num": "37",
        "title": "Example 37",
        "problem": "Discuss the continuity of f(x)=x-2x-3x+5 at x=1",
        "given": "",
        "method": "",
        "steps": [
          "A function is said to be a discontinuous function at a point 'e' if one of the three conditions of continuity does not satisfy.",
          "It can be seen that the side limits consider with the value of the function with the point.",
          "\"A function is said to be a continuous function in dn interval when the function fined at every point in that interval and no jumps or breaks invol",
          "If some functions f(x) satisfies these criteria from xa to x and we say that f(x) is continuous on the interval [a,b]. 2.8.3",
          "f(x) is continuous over the closed interval [a, b] if it is continuous on the (a, b) interval.",
          "Test of continuity and discontinuity of a function at a point and in an interval"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-29",
        "num": "38",
        "title": "Example 38",
        "problem": "Discuss the continuity of f(x)=-",
        "given": "",
        "method": "",
        "steps": [
          "Hence, ƒ(-2) is not defined. We know that if any of the three conditions of continuity does not satisfy, the function will discontinuous.",
          "Therefore, f(x) is discontinuous function at x=-",
          "However, if we try to find the limit of (x), we conclude that f(x) is continuous on all the values other than --2.",
          "This implies that f(x) is continuous at all the values of x other than -2."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-2-30",
        "num": "39",
        "title": "Example 39",
        "problem": "First-class postage in 1995 was 30.32 for the first ounce and $0.23 for each additional ounce up to 11 ounces. If p(x) is the amount of postage for a letter weighing in x ounces, then we write:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-2-1",
        "exercise": "Exercise 2.1",
        "title": "Exercise 2.1",
        "description": "",
        "problems": [
          {
            "id": "ex-2-1-q1",
            "qNo": "1",
            "question": "Read each of the six graphs in the book and state its function, domain, and range.",
            "solution": "From the plotted curves and the answer section: (a) domain ℝ; range (−∞, 5]. (b) domain ℝ; range ℝ. (c) domain ℝ\\{−2}; range ℝ\\{0}. (d) domain ℝ; range ℝ. (e) domain ℝ; range [0, ∞). (f) domain ℝ; range [0, ∞). For each graph, the function is identified by its plotted curve: (a) downward-opening parabola, (b) increasing straight line, (c) reciprocal-type hyperbola with asymptotes x = −2 and y = 0, (d) straight line, and (e)–(f) upward/nonnegative curves. The scan does not print an algebraic formula for these six plotted functions.",
            "diagram": null
          },
          {
            "id": "ex-2-1-q2",
            "qNo": "2",
            "question": "Sketch each graph and give its domain and range: (a) y = 2|x − 3|, (b) y = 4|x − 3| + 3, (c) y = 5|3x + 7| − 2, (d) y = 2|4x + 3| + 1.",
            "solution": "Each absolute-value graph is V-shaped and has domain ℝ. (a) The vertex is (3, 0), so the range is [0, ∞). (b) The vertex is (3, 3), so the range is [3, ∞). (c) Since 3x + 7 = 0 at x = −7/3, the vertex is (−7/3, −2), so the range is [−2, ∞). (d) Since 4x + 3 = 0 at x = −3/4, the vertex is (−3/4, 1), so the range is [1, ∞). The positive coefficients outside the absolute values make all four graphs open upward.",
            "diagram": {
              "type": "absolute-value-set",
              "title": "Exercise 2.1, Question 2",
              "functions": [
                {
                  "a": 2,
                  "b": 1,
                  "c": -3,
                  "d": 0,
                  "label": "(a)"
                },
                {
                  "a": 4,
                  "b": 1,
                  "c": -3,
                  "d": 3,
                  "label": "(b)"
                },
                {
                  "a": 5,
                  "b": 3,
                  "c": 7,
                  "d": -2,
                  "label": "(c)"
                },
                {
                  "a": 2,
                  "b": 4,
                  "c": 3,
                  "d": 1,
                  "label": "(d)"
                }
              ]
            }
          },
          {
            "id": "ex-2-1-q3",
            "qNo": "3",
            "question": "Find f(g(x)) and g(f(x)): (a) f(x) = x² + 1, g(x) = 2x; (b) f(x) = sin x, g(x) = 1 − x²; (c) f(x) = (x − 1)/(x + 1), g(x) = (x + 1)/(1 − x); (d) f(x) = sin x, g(x) = 2x + 3.",
            "solution": "(a) f(g(x)) = (2x)² + 1 = 4x² + 1; g(f(x)) = 2(x² + 1) = 2x² + 2.\n(b) f(g(x)) = sin(1 − x²); g(f(x)) = 1 − sin²x = cos²x.\n(c) f(g(x)) = x and g(f(x)) = x, where the expressions are defined.\n(d) f(g(x)) = sin(2x + 3); g(f(x)) = 2 sin x + 3.",
            "diagram": null
          },
          {
            "id": "ex-2-1-q4",
            "qNo": "4",
            "question": "For each pair, find f(g(x)) and g(f(x)), then determine the inverse of each composite: (a) f(x) = x + 5, g(x) = x − 4; (b) f(x) = 2x + 7, g(x) = 2x; (c) f(x) = 2(x − 4), g(x) = (x + 5)/2; (d) f(x) = (x + 4)/2, g(x) = 2x − 4.",
            "solution": "(a) Both composites are x + 1. Set y = x + 1 and solve for x: the inverse is y − 1, so each inverse is x − 1.\n(b) f(g(x)) = 4x + 7, whose inverse is (x − 7)/4. g(f(x)) = 4x + 14, whose inverse is (x − 14)/4.\n(c) f(g(x)) = x − 3, whose inverse is x + 3. g(f(x)) = x − 3/2, whose inverse is x + 3/2.\n(d) Both composites simplify to x, so each is self-inverse and its inverse is x.",
            "diagram": null
          },
          {
            "id": "ex-2-1-q5",
            "qNo": "Project",
            "question": "Observe the two printed graphs and identify the domain and range of each.",
            "solution": "For each picture, trace the graph from its leftmost to rightmost plotted x-coordinate to obtain the domain, then from its lowest to highest y-coordinate to obtain the range. The exact endpoints must be read from the printed graphs on page 31.",
            "diagram": null
          }
        ],
        "pageStart": 25,
        "pageEnd": 62
      },
      {
        "id": "ex-2-2",
        "exercise": "Exercise 2.2",
        "title": "Exercise 2.2",
        "description": "",
        "problems": [
          {
            "id": "ex-2-2-q1",
            "qNo": "1",
            "question": "Classify: (a) y=sin²x+x; (b) y=7x⁴+3x²−4x+5; (c) y=arctan x−7; (d) y=log₂16+7log₂x; (e) x²+y²=36; (f) y=(e^{3x}+e^{−3x})/(e^{3x}−e^{−3x}); (g) y=√(x−8).",
            "solution": "(a) Trigonometric; (b) polynomial; (c) inverse trigonometric; (d) logarithmic; (e) implicit relation (a circle); (f) hyperbolic; (g) radical/algebraic. These classifications follow from the defining form of each expression.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q2",
            "qNo": "2",
            "question": "A sealed container has radium amount Q(t) = 100e^{−0.00043t} grams, where t is measured in years. Find Q(0), Q(800), Q(1600), and Q(5000), and describe the result.",
            "solution": "Substitute each time into Q(t). Q(0)=100e^0=100 g. Q(800)=100e^{−0.344}≈70.9 g. Q(1600)=100e^{−0.688}≈50.2 g. Q(5000)=100e^{−2.15}≈11.6 g. The amount decreases as time passes because the exponent is a negative multiple of t.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q3",
            "qNo": "3",
            "question": "Use point-by-point plotting for (a) h(x)=2^x, −5≤x≤0; (b) m(x)=3^{−x}, 0≤x≤3; (c) N=e^x, 0≤x≤5; (d) N=e^{−x}, 0≤x≤5.",
            "solution": "Evaluate each function at the endpoints and intermediate integer x-values, then plot the ordered pairs. (a) 2^x increases from 1/32 to 1. (b) 3^{−x} decreases from 1 to 1/27. (c) e^x increases from 1 to e^5. (d) e^{−x} decreases from 1 to e^{−5}. All four curves remain positive and have horizontal asymptote y=0.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q4",
            "qNo": "4",
            "question": "Use point-by-point plotting for the logarithmic functions shown in Exercise 2.2, Question 4 (a–f).",
            "solution": "The six functions are logarithmic transformations. Their vertical asymptotes and domains are: (a) y=ln x: x=0, domain (0,∞); (b) u=−ln x: x=0, domain (0,∞); (c) y=2ln(x+2): x=−2, domain (−2,∞); (d) y=4ln(x−3): x=3, domain (3,∞); (e) y=4ln x−2: x=0, domain (0,∞); (f) y=4ln(x−2): x=2, domain (2,∞). Plot by evaluating valid x-values on each side of the asymptote, never at the asymptote.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q5",
            "qNo": "5",
            "question": "Sketch the parametric curves: (a) x=3−t², y=2t, t∈ℝ; (b) x=4cos t, y=−3sin t.",
            "solution": "(a) Eliminate t: t=y/2, so x=3−y²/4. This is a left-opening parabola with vertex (3,0). (b) Divide x=4cos t by 4 and y=−3sin t by −3; adding the squares gives x²/16+y²/9=1, an ellipse centered at the origin with horizontal semiaxis 4 and vertical semiaxis 3.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q6",
            "qNo": "6",
            "question": "Sketch the graphs: (a) e^{−2x}; (b) (2/3)e^{2x}; (c) 4^x; (d) 4^{−x}; (e) log₂(x+5); (f) log₂(x²); (g) log₂(2x−5).",
            "solution": "Each exponential has domain ℝ and horizontal asymptote y=0. (a),(d) decrease; (b),(c) increase. For the logarithms, identify the positive argument: (e) domain x>−5 and vertical asymptote x=−5; (f) domain x≠0 with vertical asymptote x=0 on both sides; (g) domain x>5/2 and vertical asymptote x=5/2. Use the standard logarithm graph and apply the stated shifts/scales.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q7",
            "qNo": "7",
            "question": "Sketch: (a) x²+y²=4; (b) x²+y²=16; (c) x²/25+y²/9=1; (d) x²/36+y²/9=−1.",
            "solution": "(a) Circle centered at (0,0), radius 2. (b) Circle centered at (0,0), radius 4. (c) Ellipse centered at the origin with semiaxes 5 (horizontal) and 3 (vertical); vertices are (±5,0), co-vertices (0,±3). (d) There are no real points because a sum of nonnegative terms cannot equal −1; its real graph is empty.",
            "diagram": null
          },
          {
            "id": "ex-2-2-q8",
            "qNo": "8",
            "question": "Use Maple commands to plot the graphs of the functions in Question 1.",
            "solution": "For each expression, enter the function in Maple and use plot(function, x=a..b) with a suitable interval. For implicit relations such as x²+y²=36, use an implicit plot with both x and y ranges. The plot is checked by comparing its shape and domain with the classifications in Question 1.",
            "diagram": null
          }
        ],
        "pageStart": 25,
        "pageEnd": 62
      },
      {
        "id": "ex-2-3",
        "exercise": "Exercise 2.3",
        "title": "Exercise 2.3",
        "description": "",
        "problems": [
          {
            "id": "ex-2-3-q1",
            "qNo": "1",
            "question": "Evaluate: (a) lim_{x→4}(3/x+1/(x−5)); (b) lim_{x→1}((x²+3x+2)/(x²+x+2))²; (c) lim_{x→1}(√x−1)/(x−1); (d) lim_{x→1}(1/x−1)/(x−1); (e) lim_{x→0}(1−sin x)/cos²x; (f) lim_{x→0}tan x/x; (g) lim_{x→0}(sec x−1)/(x sec x); (h) lim_{x→0}sin²(7x)/(7x).",
            "solution": "(a) 3/4+1/(−1)=−1/4. (b) ((1+3+2)/(1+1+2))²=(6/4)²=9/4. (c) Rationalize: 1/(√x+1)→1/2. (d) (1−x)/(x(x−1))=−1/x→−1. (e) Direct substitution gives 1. (f) The standard limit is 1. (g) Since (sec x−1)/(x sec x)=(1−cos x)/x→0. (h) sin²(7x)/(7x)→0.",
            "diagram": null
          },
          {
            "id": "ex-2-3-q2",
            "qNo": "2",
            "question": "Use algebra and limit laws: (a) lim_{x→4}−6/(x−4)²; (b) lim_{x→0}([1/(x+3)]−1/3)/x; (c) lim_{x→5}(√x−√5)/(x−5).",
            "solution": "(a) The denominator approaches 0 through positive values, so the expression tends to −∞. (b) Combine the numerator: [1/(x+3)−1/3]/x = [−x/(3(x+3))]/x = −1/[3(x+3)]→−1/9. (c) Rationalize to 1/(√x+√5)→1/(2√5).",
            "diagram": null
          },
          {
            "id": "ex-2-3-q3",
            "qNo": "3",
            "question": "Find the limits of the sequences: (a) {5n/(n+7)}; (b) {(4−7n)/(8+n)}; (c) {(-1)^n/n²}.",
            "solution": "Divide numerator and denominator by n in the first two: (a) 5/(1+7/n)→5; (b) (4/n−7)/(8/n+1)→−7. For (c), |(−1)^n/n²|=1/n²→0, so the sequence tends to 0.",
            "diagram": null
          },
          {
            "id": "ex-2-3-q4",
            "qNo": "4",
            "question": "Weekly sales are S(x)=5000+3600/(x+2) rupees, x weeks after an advertising campaign. Find (a) S(5), (b) lim_{x→5}S(x), and (c) lim_{x→∞}S(x).",
            "solution": "(a) S(5)=5000+3600/7=5514.2857… rupees. (b) S is continuous at 5, so the limit is S(5)=5514.2857… rupees. (c) As x→∞, 3600/(x+2)→0, hence the limit is 5000 rupees.",
            "diagram": null
          },
          {
            "id": "ex-2-3-q5",
            "qNo": "5",
            "question": "Use Maple’s limit command to evaluate every limit from Question 1.",
            "solution": "Enter each expression using the syntax limit(expression, x=a), replacing x and a with the variable and limiting value shown in Question 1. The outputs are (a) −1/4, (b) 9/4, (c) 1/2, (d) −1, (e) 1, (f) 1, (g) 0, and (h) 0.",
            "diagram": null
          },
          {
            "id": "ex-2-3-q6",
            "qNo": "6",
            "question": "Evaluate the limits in parts (a–g) using algebraic techniques and standard limits.",
            "solution": "(a) Rationalize the difference of square roots before letting h→0. (b) Factor the difference of powers and cancel the common factor before substitution. (c) Use 1−cos u=2sin²(u/2), giving p²/q². (d) Rewrite tan θ−sin θ=sin θ(1−cos θ); dividing by sin³θ gives (1−cos θ)/sin²θ→1/2. (e) (1−1/n)^n→e^{−1}. (f) Apply (1+u)^{1/u}→e after matching the exponent. (g) Compare the base with a constant less than 1; the limit is 0.",
            "diagram": null
          },
          {
            "id": "ex-2-3-project",
            "qNo": "Project",
            "question": "Identify the types of functions represented by the two curves shown in the book.",
            "solution": "Identify each curve from its shape and defining equation printed beside it: the first is a real-world plotted curve; the second is the displayed algebraic function. Read the curve’s equation and classify it by its functional form.",
            "diagram": null
          }
        ],
        "pageStart": 25,
        "pageEnd": 62
      },
      {
        "id": "ex-2-4",
        "exercise": "Exercise 2.4",
        "title": "Exercise 2.4",
        "description": "",
        "problems": [
          {
            "id": "ex-2-4-q1",
            "qNo": "1",
            "question": "Use continuity properties to test: (a) f(x)=2x−3; (b) h(x)=2/(x−5); (c) g(x)=(x−5)/((x−3)(x+2)).",
            "solution": "(a) A polynomial is continuous for every real x. (b) A rational function is continuous wherever its denominator is nonzero, so h is continuous on (−∞,5) and (5,∞), and discontinuous at x=5. (c) The denominator is zero at x=3 and x=−2; g is continuous on each interval that excludes these points and discontinuous at both.",
            "diagram": null
          },
          {
            "id": "ex-2-4-q2",
            "qNo": "2",
            "question": "Show that f(x)=sin x/x for x≠0 and f(0)=1 is continuous at x=0.",
            "solution": "By definition, continuity at 0 requires lim_{x→0} f(x)=f(0). The standard trigonometric limit gives lim_{x→0}(sin x)/x=1, and f(0)=1. Therefore the limit equals the function value, so f is continuous at 0.",
            "diagram": null
          },
          {
            "id": "ex-2-4-q3",
            "qNo": "3",
            "question": "Use the graph of g(x) to answer the continuity and one-sided continuity questions at x=−1 and x=2 in parts (a–d).",
            "solution": "Read the plotted point and the approaching curve at each marked x-value. The answer key states: g is continuous on (−1,2); it is continuous from the right at x=−1; it is continuous from the left at x=2; and it is continuous on [−1,2]. Check the endpoint equalities using the one-sided limits shown by the graph.",
            "diagram": null
          },
          {
            "id": "ex-2-4-q4",
            "qNo": "4",
            "question": "Use the graph of f(x) to answer the continuity and one-sided continuity questions on [0,3].",
            "solution": "From the graph and answer key: f is continuous on (0,3), continuous from the right at x=0, continuous from the left at x=3, and continuous on the closed interval [0,3]. Continuity on the closed interval uses the right-hand limit at the left endpoint and the left-hand limit at the right endpoint.",
            "diagram": null
          },
          {
            "id": "ex-2-4-q5",
            "qNo": "5",
            "question": "Graph each piecewise function and locate all points of discontinuity: (a) f(x)=1+x for x<1; 5−x for x≥1. (b) f(x)=−x for x<0; 1 for x=0; x for x>0.",
            "solution": "(a) At x=1, the left-hand limit is 2, while f(1)=4; therefore there is a jump discontinuity at x=1. Each branch is linear and continuous elsewhere. (b) Both one-sided limits at 0 equal 0, but f(0)=1; hence there is a removable discontinuity at x=0. Elsewhere each branch is continuous.",
            "diagram": null
          },
          {
            "id": "ex-2-4-q6",
            "qNo": "6",
            "question": "A salesperson earns a $1,000 monthly base salary and 5% commission on sales over $10,000; at sales of $20,000 or more an additional $500 bonus is paid. Define E(s), graph it, and answer the limit/value and continuity questions in parts (a–d).",
            "solution": "A piecewise model is E(s)=1000 for 0≤s≤10000; E(s)=1000+0.05(s−10000) for 10000<s<20000; E(s)=1500+0.05(s−10000) for s≥20000. At s=10000, E=1000 and both adjoining values approach 1000, so it is continuous there. At s=20000, the value jumps from the left-hand limit 1500 to E(20000)=2000; the two-sided limit does not exist, so it is discontinuous there. The graph consists of the base segment, a rising commission segment, then an upward $500 jump followed by the same slope.",
            "diagram": null
          },
          {
            "id": "ex-2-4-q7",
            "qNo": "7",
            "question": "Use Maple’s iscont command to test whether f(x)=(x²+1)/(x²+2.7) is continuous on [−5,5].",
            "solution": "The denominator x²+2.7 is positive for every real x, so the rational function has no singularity on [−5,5] and is continuous throughout that interval. Maple’s iscont command therefore returns true.",
            "diagram": null
          }
        ],
        "pageStart": 25,
        "pageEnd": 62
      },
      {
        "id": "ex-2-5",
        "exercise": "Review Exercise",
        "title": "Review Exercise",
        "description": "",
        "problems": [
          {
            "id": "ex-2-review-q1",
            "qNo": "i",
            "question": "In y=(x²+4x−3)/(x+3), identify the independent variable.",
            "solution": "The input variable is x; y depends on x. Answer: x.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q2",
            "qNo": "ii",
            "question": "For f(x)=(3x²−2)/(3x+9), find f(−3).",
            "solution": "At x=−3 the denominator 3x+9 is 0, while the numerator is nonzero. Thus f(−3) is undefined.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q3",
            "qNo": "iii",
            "question": "Find the domain of f(x)=(3x²−2)/(3x+9).",
            "solution": "A rational function is undefined when its denominator is zero: 3x+9=0 gives x=−3. Domain: ℝ\\{−3}.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q4",
            "qNo": "iv",
            "question": "Find the domain of f(x)=(3x−2)/(3x²+9).",
            "solution": "Since 3x²+9=3(x²+3)>0 for all real x, there is no excluded real input. Domain: ℝ.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q5",
            "qNo": "v",
            "question": "If f(x)=2x+3, find f^{−1}(5).",
            "solution": "Set y=2x+3 and solve for x: x=(y−3)/2. Thus f^{−1}(y)=(y−3)/2, and f^{−1}(5)=(5−3)/2=1.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q6",
            "qNo": "vi",
            "question": "A function written as y=f(x) is called what kind of function?",
            "solution": "The dependent variable y is explicitly given in terms of x. It is an explicit function.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q7",
            "qNo": "vii",
            "question": "If f(x)=3x²+2x−1 and g(x)=x+1, find f(g(x)).",
            "solution": "f(g(x))=3(x+1)²+2(x+1)−1=3x²+6x+3+2x+2−1=3x²+8x+4.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q8",
            "qNo": "viii",
            "question": "Choose the listed approximation for e.",
            "solution": "e=2.7182818…; to two decimal places, e≈2.72. The closest listed option is 2.71.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q9",
            "qNo": "ix",
            "question": "If 5^x=7, express x using natural logarithms.",
            "solution": "Take ln of both sides: x ln 5=ln 7, so x=ln 7/ln 5.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q10",
            "qNo": "x",
            "question": "Write coth x in exponential form.",
            "solution": "Using cosh x=(e^x+e^{−x})/2 and sinh x=(e^x−e^{−x})/2, coth x=cosh x/sinh x=(e^x+e^{−x})/(e^x−e^{−x}).",
            "diagram": null
          },
          {
            "id": "ex-2-review-q11",
            "qNo": "xi",
            "question": "Simplify ln(m²)−ln(n²).",
            "solution": "By the quotient law of logarithms, ln(m²)−ln(n²)=ln(m²/n²), for m,n≠0.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q12",
            "qNo": "xii",
            "question": "For f(x)=2/(x²−9), find its discontinuity points.",
            "solution": "The denominator factors as (x−3)(x+3) and vanishes at x=3 and x=−3. These are the discontinuity points.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q13",
            "qNo": "xiii",
            "question": "Evaluate lim_{θ→0} sin(7θ)/(7θ).",
            "solution": "Let u=7θ. As θ→0, u→0, and sin u/u→1. The limit is 1.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q14",
            "qNo": "xiv",
            "question": "If f(θ)=θ sec θ, find f(0).",
            "solution": "f(0)=0·sec 0=0·1=0.",
            "diagram": null
          },
          {
            "id": "ex-2-review-q15",
            "qNo": "xv",
            "question": "Find the inverse of f(x)=(e^x−e^{−x})/(e^x+e^{−x}).",
            "solution": "Let y=(e^x−e^{−x})/(e^x+e^{−x})=tanh x. Then x=artanh y=(1/2)ln((1+y)/(1−y)), for −1<y<1. Therefore f^{−1}(x)=(1/2)ln((1+x)/(1−x)).",
            "diagram": null
          }
        ],
        "pageStart": 25,
        "pageEnd": 62
      },
      {
        "id": "ex-2-6",
        "exercise": "Review Exercise 2",
        "title": "Review Exercise 2",
        "description": "",
        "problems": [],
        "pageStart": 25,
        "pageEnd": 62
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-3",
    "number": 3,
    "title": "Differentiation",
    "titleUrdu": "",
    "pageRange": "Printed pages 63–100",
    "pageStart": 63,
    "pageEnd": 100,
    "sections": [
      {
        "id": "sec-3-1",
        "title": "3.1 Derivative of a Function",
        "theory": "In the sense of a tangent line the concept of derivative is very old in the study of mathematics. This is familiar to Greek geometers. But the modern development of a calculus credited to Isaac Newton and G.W Leibniz. Who provided the independent and unique approaches to the derivatives and differentiation.\n\nTo understand the origin of the concept of variables, some real-life situations in which one numerical quantity depends on, corresponds to, or determines another are considered. For example,\n\nThe amount of income tax (output/dependent variable) you pay on the amount of your income (input/independent variable). The way in which the income determines the tax is given by the tax law (rule).\n\n2. A person in business wants to know how profit (output/dependent variable) changes with respect\n\nA person in medicine wants to know how a patient's reaction to a drug (output/dependent variable) changes with respect to dose (input/independent variable).\n\nIn each case, the change in dependent variable requires the definite change in independent variable through a definite rule which is called a function.\n\nindependent variable is incremented (or decremented)\n\nA familiar situation related to change in dependent with respect to change in independent is that a driver makes the run of 120, mile trip from Peshawar to Islamabad, in 2 hours. The table shows how far the driver has traveled from Peshawar at various times:\n\nIf ƒ is the function whose rule is (r) = distance from Peshawar at time r, then, the table shows that (1.0) 54,/(1.5)-88 and (2.0)=120 miles. So the distance traveled from time =1.5 tot 2.0 is (2)-(1.5)=120-88-32, the change in dependent variable (change in distance) in response of incremented independent variable r, while the distance traveled from time r=1.5 to -1.0 is (1.5)-(1.0)=88-54-35, the change in dependent variable (change in distance) in response of decremented independent variabler.\n\nThe idea of average rate of change is something we encounter every day. For example, it accelerates from 0 to 96 km/h in 8.0 s, then we say that it accelerates at an average rate of 12 km spaceship climbs from 0 to 10,000 m in 2.5 s, then we say that the ship climbs at an average velo 4000 m/s. If com grows a total of 28 inches in 2 weeks, then it grows an average of 2 inches per da\n\nIn these examples, the indicated average rate of change is obtained by dividing the change in the dependent variable by the change in the independent variable.\n\nLet us examine the process of finding the average rate of change of a function f(x). If we select any value of x and increase it by an amount Ax, then a new value of the independent variable is x+Ax. As x changes from x to x‚†Âxy will change to a corresponding amount of y+Ay. The ordered pairs P(x, y) and Q(x+Ax, y+Ay) developed must satisfy the function y = f(x). This is shown in the Figure 3.1 If the function value at a point P (x,y) is y=f(x) then, the function value at a point Q is y+Ay=f(x+Ax) (ii) The difference of equations (i) and (ii) gives the change in y; (y+Ay)-y=f(x+Ax)-f(x) = Ay= f(x+&x)−ƒ(x) The change in x is Ax=x+Ax-I\n\nThe instantaneous rate of change of a function f(x) at a point P is the derivative of a fune f(x) at that point P, f'(x) = lim (x+Ax)-f(x)\n\nThis is called first principle rule of derivative of a function f(x) with respect to x. If y=√(x) is a function, then its derivative or differential coefficient is denoted by\n\na number in the domain of y = f (x) such that y' = f(x) is defined, then the function f is said differentiable at x. The process that produces the function from the function f is called differentiat 3 Determine the derivative of a function f(x)=x2-6x+5 by first principle rule at a\n\nSolution The derivative of a given function by first principle rule (i) is:\n\nThe result f'(x)=2x-6 represents the slope of the tangent line at any point P (x, y) curve f(x) = x2-6x+5. Thus, the slope of the tangent line at a particular point, say P (4,-3) on curve is: f'(x)=2x-6\n\nthe slope of the secant line (the average rate of change) is called the approximate rate of change. ⚫the slope of the tangent line (the instantaneous rate of change) is called the exact rate of change.\n\nIf(x) is any function, then the derivative by first principle rule is\n\nThe process used for finding the derivative of a function in and the result 2 is the differential coefficient of a function f(x)= x2-6x+5 at a particular point P(4, 3).\n\nSymbol(x) is used to indicate the derivative of f (x) with respect to x. Sometimes other symbols are used to indicate the derivative. Each of the symbols in the following box indicates the derivative of the dependent variable y with respect to the independent variable x\n\n(x): read \" prime of 3\" (derivative of/(r) with respect to x)\n\n\"The tangent line to the graph of a function y = f(x) at the point ill. f: read \"/prime\" (the derivative (x, f(x)) is the line through this point having slope\n\nprovided this limit exists. If this limit does not exist, then there is\n\nIf f(x)=x\", is any integer, then, by first principle rule, the derivative of f(x)=x\" w.rt. x is: f'(x) = lim f(x+Ax)-f(x)\n\ny' + Ay = (ax + b)\" + (\")(ax + by \" (a^x)+(\")(ax+b)\" (adx)2 + (\"\")(ax+b)\" (a_^x)\" + + (a.Ax)\" (ii)\n\nlim {a (\")(ax + b) \" + (\")(ax + b)\" (@Ax)\" + (\") (ax + b)^(ada)\".\n\n(ax+b)\"\" + lim (\") (ax + b)\" (ax)\" + lim (\")(ax+6)3\n\nBy applying limit all terms tends to zero except first term so,\n\nThis is generalized power rule of differentiation.\n\nFind the average rate of change of the following functions over the indicated intervals:\n\nUse definition for the rate of change to find out the average rate of change over the specified interval for the following functions:\n\nA ball is thrown straight up. Its height after t seconds is given by the formula =-16r+80r. Use definition for the rate of change to determine the average velocity for the specified intervals: a. From 1-2 to 1-2.1. The rate of change of price is called inflation. The price p in rupees after years is p(r)=3r+r+1. Use definition for the rate of change to determine the average rate of change of inflation from z=3 to 1-5 years. What the rate of change means? Explain.\n\nA farmer plants x acres of sugar beets. The profit generated is f(x)=-1800x-9x. Determine the average rate of change of the profit, when the planted area is in between 20 acres and x = 50 acres. What the rate of change means? Explain.\n\nUse first principle rule to determine the derivative of the following functions:\n\nUse function ƒ'(x)=-7x+6 to do the following:\n\na. Find the derivative of a function at point P(5,-4).\n\nb. Find the tangent line on the curve y=x-7x+6 at point P(5, 4).\n\nc. View the slope of the tangent line on the curve at P(6, 0)?\n\nUse definition of derivative to determine the slope of the tangent line to the curve at a given point and then find out the tangent line equation on that curve at the same point, for the following curves:\n\nThere is always an odometer and a speedometer in an automobile. These two things work in tandem and allow the driver to determine the speed of his/her vehicle and the distance he/she has traveled.\n\nElectronic versions of these two gauges simply use derivatives to transform the data sent to the electronic motherboard from the tyres to miles per hour (MPH) and distance (KM).",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-3-2",
        "title": "3.2 Theorems on Differentiation",
        "theory": "Theorem-1: The derivative of a constant is zero\n\nProof: Iff(x) = c, where e is any constant, then, by first principle rule, the derivative of a constant function\n\nThis calculation develops the rule that the derivative of a constant function is zero.\n\nIf ƒ (x) = c, where e is any constant, then: f'(x)=0\n\n5 Differentiate the following constant functions:\n\nution The graphs of the functions are horizontal lines parallel to x-axis, since all function are constant. The derivative in each case is therefore going to be zero.\n\nTheorem-2: The derivative of any constant multiple of a function is equal to the product of that const and the derivative of the function.\n\nIf f(x)=c.g(x), where e is any constant, then by the first principle rule, the derivative\n\nThis calculation develops the rule that the derivative of a constant multiple function is product of the constant function and the derivati of a function f(x).\n\nIn general: If g(x)=x\" and f(x)=cg(x), c is any constant, then: f(x) = cg′(x) = cme\"\" Example 6 Differentiate the following functions:\n\nIf ƒ (x)=4x2, then, the derivative of a give function is: If f(x)=0.555x\", then, the derivative of a given function is:\n\nTheorem-3: The derivative of a sum (or difference) of two functions is equal to the sum (or difference) of their derivatives.\n\nProof: To determine the derivative of a polynomial, such as the derivative of the sum or difference of two or more functions, we need to develop a rule that could be used in the determination of a derivative like f(x)=3x2+2x+3. In this situation, if h(x) = f(x)+g(x), then, our task is to determine '(x) by first principle rule of differentiation:\n\nBy subtraction equation (1) from equation (1)\n\nNow, apply lim on both sides of equation (iv)\n\nWe can say that the derivative of a sum of two functions is the sum of the derivatives of two functions. The difference of two functions/(x)-g(x) can be written as",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-3-3",
        "title": "3.3 Applications of Differentiation Theorems",
        "theory": "- Constant multiple of x\" Product of functions\n\nSum (or difference) of functions Quotient of two functions\n\n(d). As more wheat is produced; what happens to the marginal cost?\n\nIf C(x)=5000+20x+10√x, then the marginal cost is the derivative of C (x) with respect to x:\n\nThe marginal cost at x=9 units is obtained by inserting x-9 in C′(x):\n\nThe marginal cost at x = 16 units is obtained by inserting x16 in C'(x):\n\nThe marginal cost at x=25 units is obtained by inserting x =25 in C′(x):\n\nIn business and economics the rates of change of such variables as cost, revenue and profit are most important. Economists use the word marginal to refer to rates of change. For example, the marginal cost refers to the rate of change of cost. Since the derivative of a function gives the rate of change of the function, a marginal cost (or revenue of profit) function is found by taking the derivative of the cost (or revenue of profit) function. The marginal cost at some level of production is the cost to produce the (x+1)st item (ie., one more item).\n\nFind the derivative of the following functions w.r.t involved independent variable:\n\nof the following function in terms of parameter t\n\nAt a certain factor, the total cost of manufacturing 4 units during the daily production run isC(q)=0.2g2+q+900 dollars. From experience, it has been determined that approximately q(t)='+100r units are manufactured during the first thours of a production run. Compute the rate at which the total manufacturing cost is changing with respect to time one hour after production begins.\n\nUse implicit differentiation to perform for the following functions:\n\nArrange the following functions explicitly and implicitly to perform\n\nDetermine the slope of the tangent line to the curve 3x2-7y+14y=27 at the point P(-3,0).\n\nSuppose two motor boats leave from the same point at the same time. If one boat travels north at 15 miles per hour and the other boat travels east at 20 miles per hour. How fast will the distance between them be changing after 2 hours?",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-3-4",
        "title": "3.4 Chain Rule",
        "theory": "\"The chain rule is a rule which we use to differentiate the composite functions\". We have learnt about composition of functions in unit-2 that a function is a composite functions of the two similar functions f(x) and g(x) if it is written as (g(x)]. In other words it is a function of a function. For example sin(x) is a composite functions because of we consider f(x)= sin(x) and g(x) = x2 then / [g(x)] = sin(x). Generally, we write chain rule as;\n\nProof: For our convenience, we set Let u= g(x) the equation (i) will be\n\nNow, subtracting equation (i) from equation (iii)\n\nSubstitute the value of g(x+Ax) from equation (vi) to equation (v)\n\nMultiply and divide the right side of equation\n\nIf y = f(x)=(4x-3)-u\" with u=4x-3, then, the first derivative w.r.t. x by chain rule is:\n\npatrol. At the outbreak of a flu epidemic, 30 work hours are used daily in parking patrol, but during the epidemic that number is decreasing at the rate of 6 work hours per day. How fast is revenue from parking fines decreasing during the epidemic?\n\nWe need to find the change in revenue with respect to time t. The chain rule is used to\n\nThis tells us that the revenue is being lost at the rate of approximately $94 per day.\n\nIf y = f(x) is any differential function of x, then it admits an inverse function x = g(y). Suppose y is changed by a small amount Ay. This will cause x to change by an amount Ax, The increment. Ar in x corresponds to the increment Ay in y is determined from\n\nLeibniz was the first person who mentioned the composite of the square root function and the function on 1676. The common notation of the chain rule is also due Leibniz.\n\nThe derivative of y = (4x-3)' is 12(4x-3). This result agrees to result\n\nIn words, ifƒ(x) is equal to an expression in x raised to a power of n, then f(x) is equal to the product of times the expression to the n-1 power times the derivative of the expression with respect to the variable. The statement is known as the general power rule.\n\nIf y = f(x)=(11x-7) then, the first derivative of a given function is:\n\nIf two differential functions x-f() and yg (1) of parameter t. If th(x) is an inverse function of x= f(t). then y=g[h(x)] is a function of x.\n\nWhether y is expressed explicitly or implicitly in terms of x, we can still differentiate to find If y is expressed explicitly in terms of x, then dy will also be expressed\n\nexplicitly in terms of x. Ify is expressed implicitly in terms of x, then of x and y.\n\ndy Fortunately, there is a simple technique based on the chain rule that allows us to find without first solving the equation for y explicitly. This technique is known as implicit differentiation. It consists differentiation of the both sides of the equation with respect to x and then solving the resultant equation\n\n14 Differentiate the implicit equation xy+2y=3x+2y.\n\nThe implicit equation is The implicit differentiation of\n\nis obtained by differentiating both sides w.r.L. x.\n\nThe slope of a tangent line to the given curve is that can be found by taking the\n\nAt a point P(5, 4), the slope of the tangent line is:\n\nNote that the expression is undefined at j=2. This makes sense, when you see that the tangent vertical there.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-3-5",
        "title": "3.5 Differentiation of Trigonometric and Inverse Trigonometric Functions",
        "theory": "To understand this section we need to know about trigonometric function. For differentiating all trigonometric functions we use the basic rule of differentiation that we have already learnt e.g. We will use product, quotient and chain rules to differentiation functions that are the combination of the trigonometric function.\n\nDerivative of sin. If y=sinx then the derivative of y = sinx is\n\nDerivative of cos: Ify-cos x, then the derivative of y-cos x is\n\nSubtracting equation from equation y+Ay-y=cos(x+x)=cos(x) Ay = cos(x+Ax)-cos(x)\n\nAy=-2sin(x+4x+x) sin(x+4x-x) Ay=-2sin(x+4x).sin(47)\n\nDerivative of tan x Ify tanx, then the derivative of\n\nSubtracting equation from equation 3+Ay− y = tan(x+Ax) = tan(x)\n\nThe traffic police officers uses radar guns to take the advantage of the easy use of derivatives. When a radar gun is pointed and fired at a car on the motorway. The gun is able to determine the time and distance at which the radar was able to hit a certain section of the car with the use of derivative it is able to calculate the speed at which the car was going and also report the distance that the car was from the radar gun.\n\nsin(x+Ax).cos(x)=sin(x).cos(x+Ax) Ax.cos(x).cos(x+Ax)\n\nDerivative of secx Ify secx, then the derivative of y = sec(x) is\n\nNow, divide equation (iii) by the Ax Ay cot(x+Ax)-cot(x)\n\nNow, apply lim on both sides of equation (iv).\n\nThe chain rule can be used to derive the generalization of the power. rule and the rules for differentiating the trigonometric functions, as summarized in the box:\n\nIf the given function is p()=(1+r)sinz, then the product rule of differentiation w.r.t. r is used to\n\nthen the quotient rule of differentiation w.r.t. x is used to\n\n17 Differentiate the following trigonometric functions:\n\n4. If the given function is f(x)= secx tanx, then the product rule of differentiation w.r.t. x is used to obtain:\n\n(3.x + 2 tan x). —-—-— (x2 + tan x) - (x2 + tan x)=(3x+2 tan x)\n\nDifferentiation of inverse trigonometric functions\n\nDerivative of sin x: If ysin\" x, then x = sin y.\n\nTake its reciprocal to obtain the derivative of y w.r.t. X:\n\nHere, the sign of the radical is the same as that of cosy. By definition of sinx:\n\nDerivative of cos 'x: If y=cosx, then.x=cosy.\n\nTake its reciprocal to obtai.. the derivative of y w.rt. I\n\nHere, the sign of the radical is the same as that of sin y. By definition of cos1x\n\nAlso, if y lies between 0 and л, then, sin y is necessarily positive. Hence\n\nDerivative of tan 'x: If y=tanx, then x = tan y The differentiation of x = tany w.r.t. y is: d\n\nTake its reciprocal to obtain the derivative of y w.EL. x.\n\n1 dx secy 1+tany 1+x Derivative of see 'x: If\n\nTake its reciprocal to obtain the derivative of y w.r.t. x\n\nWe take + sign before the radical sign to obtain: (sec\" x)\n\nDerivative of cosec\" If y=cosecx, then.x=cosecy.\n\nTake its reciprocal to obtain the derivative of y w.EL X\n\nWe take + sign before the radical sign to obtain: (cosecx)=\n\nDerivative of cot'x: If y=cotx, then x = coty.\n\nTake its reciprocal to obtain the derivative of y w.rl x\n\nThese inverse trigonometric formulas are listed in the box:\n\nThe chain rule can be used to derive the generalization of the power rule and the rules for difcrentiating the inverse trigonometric functions, as summarized in the box:\n\nUse of first principle rules to differentiate the following functions..\n\nDifferentiate the following trigonometric functions by using any suitable rule.\n\nUse any suitable rule of differentiation to perform",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-3-6",
        "title": "3.6 Differentiation of Exponential and Logarithmic Functions",
        "theory": "Suppose profits on the sale of swimming suits in a departmental store are given approximately by\n\nwhere P(t) is profit (in hundreds of dollars) for a week of sales t weeks after January first.\n\na. What is the rate of change of profit t weeks after the first of the year?\n\nb. What is the rate of change of profit 8 weeks after the first of the year? 26weeks after the first\n\nof the year? 50 weeks after the first of the year?\n\nA normal seated adult breathes in and exhales about 0.8 liter of air every 4 seconds. The volume of air P(/) in the lungs t seconds after exhaling is given approximately by (t)=0.45-0.35cos,05:58.\n\na. What is the rate of flow of airt seconds afterexhaling?\n\nb. What is the rate of flow of air 3 seconds after exhaling? 4 seconds after exhaling? 5 seconds\n\nDifferentiation of Exponential and Logarithmic Functions\n\nThe goal of this section is to develop the differential calculus of logarithmic and exponential functions. We shall begin by deriving differentiation formulas for In x and e'. The derived formulas will be applied to a number of differentiation problems and applications.\n\nDerivative of e': If y=e, then the derivative of y=e\" by first principle rule is:\n\nDerivative of a': If y=a\", then the derivative of y=a\" by first principle rule is:\n\nDerivative of Inx: Ify- Inx, then the derivative of y= Inx by first principle rule is:\n\nDerivative of log..: If y=logx, then the derivative of y= log,x by first principle rule is:\n\nThese exponential and logarithmic formulas are listed in the box:\n\nThe chain rule can be used to derive the generalization of the power rule and the rules for differentiating the exponential and logarithmic functions, as summarized in the box:\n\nIf the given function is f(x)=74-), then the derivative of the given function w.r.t. x is\n\nIf the given function is f(x)=log√(x-7x)+x', then the derivative of a given function w.r.t. x is:\n\nIf the given function is f(x)= In(e\"\"+e), then the derivative of a given function w.r.t. x is:\n\nIf the given function is f(x) = then the derivative of a given function w.r.t. x is:\n\nLogarithmic differentiation is a procedure in which logarithmis are used to trade the task of differentiating products and quotients for that of differentiating sums and differences. It is especially valuable as a means for handling complicated product or quotient functions and power functions where variables appear in both the base and the exponent.\n\nIf the given function after simplification is\n\n- Inx + In(x-3)2 - In(x2-4) = ln x+2 In(x-3)-In(x-4),\n\nthen on differentiation w.r.L. x. It becomes;",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-3-7",
        "title": "3.7 Differentiation of Hyperbolic and Inverse Hyperbolic Functions",
        "theory": "The concept of hyperbolic functions is completely discussed in Unit-2. The differentiation of\n\nhyperbolic functions can be found as follows:\n\nDerivative of sinkx: If y=sin kx, then on differentiation w.t.t. x, it bec\n\nDerivative of cosky: If y= cos krete, then on differentiation w r.t. x, it b\n\nthen on differentiation w.r...x throute. sin kr\n\nThe chain rule can be used to derive the generalization of the power rule and the rules for dentisung the hyperbolic functions, as summarized in the box:\n\nIf the given function is y = cos h(2x-1), then the derivative of y w.r.t. x is:\n\nDerivative of sinh 'x: Ify sinh'x, then x = sinh y, the differentiation of x= sin hy w.rty is\n\ncoshy Take its reciprocal to obtain the derivative of y w.r.t. x.\n\nHere, the sign of the radical is the same as that of cos hy which we know is always positive.\n\nthen the differentiation of x=cosh yw.r.ty is:\n\nTake its reciprocal to obtain the derivative of yw.r.tx\n\nthen the differentiation of x=tan by w.r.t. y is:\n\nTake its reciprocal to obtain the derivative of yw.r.t. I\n\nDerivative of sech'x: If y=sechx, then x=sechy.\n\nTake its reciprocal to obtain the derivative of y w.r.tx\n\nHere, the sign of the radical is the same as that of tanhy but we know that sech 'x is always\n\npositive, so that tanky is always positive. Hence, (sech ̄x)=\n\nDerivative of cosech': Ifycosech 'x, then x cosechy.\n\nThe differentiation of x = cosechy w.r.t. y is: --cosechy cothy\n\nTake its reciprocal to obtain the derivative of y w.r.t. x.\n\nHere, the sign of the radical is the same as that of cothy which. Here cothy is positive or negative according as x is positive or negative.\n\nDerivative of cot': If y=coth 'x, then.x=cothy.\n\nTake its reciprocal to obtain the derivative of y w.rix\n\nThis result is obtained through right-click on the last end of the expression by selecting\" Differentiate <x\n\nUse the rule of first principle to find the derivative of the following functions:\n\nby using any suitable rule of differentiation.\n\nA research group (used hospital records) developed the approximate mathematical model related to systolic blood pressure and age is: p(x)=40+25 In(x+1), 0≤x≤65\n\nwhere p (x) is the pressure measured in millimeters of mercury and x is age in years. What is the rate of change of pressure at the end of 10 years? at the end of 30 years? at the end of 60 years? A single cholera bacterium divides every 0.5 hour to produce two complete cholera bacteria. If we start with a colony of 5,000 bacteria, then after hours there will be a A(r)=50002\" bacteria. Find (r), A(1) and (5). Interpret the results.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-3-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Determine the average rate of change of y per unit increases from 1 to 3.",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-2",
        "num": "2",
        "title": "Example 2",
        "problem": "2 The height h of a certain brand of corn with respect to t days (21) afte germinates is h(t)=√r-1.\"",
        "given": "",
        "method": "",
        "steps": [
          "(b). Find the average growth rate between days",
          "The average growth rate through definition (v) is:",
          "The average growth rate (i) is used for t 4 and Ar=5 to obtain the average growth between days 4 and 9:",
          "5 5 Thus, the average rate of change of the height of the com",
          "with respect to time (between days 4 and 9) is (1 unit",
          "change in height for each 5 units change in time). The graph is shown in Figure 3.2. The average rate of change is of course helpful in understanding the instantaneous rate of change.",
          "Derivative of a function as an instantaneous rate of change of a variable with respect to another variable",
          "In the previous sub-section, we discussed the average rate of change, and learned that the average rate of change is the slope of the secant line joining two points on the curve = f(x). More commonly, we are asked to determine the exact or instantaneous rate of change at a particular time. For example, for an aeroplane, what is the instanta: ous rate of change of the distance that occurs at a specific time?\" is can be dealt by the slope of a tangent line into a curve y(x) at a specific point?",
          "To illustrate his idea, let us examine the graph of a function +5y=x at a particular point P (0.5, 0.25) with different secant lines",
          "PQ, PQ, that developed from the secant line PQ:",
          "The tabular form contains coordinates for the points P. Q, the change Ar inx, the change Ay in y",
          "the slope of the secant lines PQ,PQPQ... Notice that the slope of the secant line PQ is 2.5",
          "(A-375-2.5). If we take values of Q closer to P (ie, to Q, Q...), then, Ax gets smaller, and",
          "The tabular form clearly shows that, as approaches P.Axapproaches 0, and the slope of the secant line approaches the slope of the tangent line at a particular point P(0.5, 0.25) which is 1.",
          "Geometrically, the slope of the tangent line to a curve at a particular point P is the instantaneous",
          "and (or exact) rate of change at that particular point.",
          "This terminology develops the idea that the slope of the secant line becomes a better approximation for the slope of the tangent line to the curve at a particular point P. From our discussion on limit, it follows that the exact/actual slope of the tangent line to a curve y=ƒ{x} at a particular point P corresponds to the instantaneous rate",
          "slope of the secant of change at that point. That is,",
          "Aydy slope of the tangent line at a particular",
          "The statement lim is read \"the limit as delta x approaches zero of delta y divided by deltax",
          "If the limit exists, then the result is the slope of tangent line or the instantaneous rate of change of y wi respect to x which we call the derivative of function.",
          "Different mathematicians used different notations to write derivative.",
          "3.1.5 Derivative or differential coefficient of a function",
          "The instantaneous rate of change of a function f(x) at a point P is the derivative of a fune f(x) at that point P, f'(x) = lim (x+Ax)-f(x)",
          "This is called first principle rule of derivative of a function f(x) with respect to x. If y=√(x) is a function, then its derivative or differential coefficient is denoted by",
          "a number in the domain of y = f (x) such that y' = f(x) is defined, then the function f is said differentiable at x. The process that produces the function from the function f is called differentiat 3 Determine the derivative of a function f(x)=x2-6x+5 by first principle rule at a",
          "Solution The derivative of a given function by first principle rule (i) is:",
          "The result f'(x)=2x-6 represents the slope of the tangent line at any point P (x, y) curve f(x) = x2-6x+5. Thus, the slope of the tangent line at a particular point, say P (4,-3) on curve is: f'(x)=2x-6",
          "the slope of the secant line (the average rate of change) is called the approximate rate of change. ⚫the slope of the tangent line (the instantaneous rate of change) is called the exact rate of change.",
          "If(x) is any function, then the derivative by first principle rule is",
          "The process used for finding the derivative of a function in and the result 2 is the differential coefficient of a function f(x)= x2-6x+5 at a particular point P(4, 3).",
          "Symbol(x) is used to indicate the derivative of f (x) with respect to x. Sometimes other symbols are used to indicate the derivative. Each of the symbols in the following box indicates the derivative of the dependent variable y with respect to the independent variable x",
          "(x): read \" prime of 3\" (derivative of/(r) with respect to x)",
          "\"The tangent line to the graph of a function y = f(x) at the point ill. f: read \"/prime\" (the derivative (x, f(x)) is the line through this point having slope",
          "provided this limit exists. If this limit does not exist, then there is",
          "D. y: read D sub x, 3o (the derivative of y with respect to x)",
          "y: read \"prime\" (the derivative of y with respect to r)",
          "The slope of the tangent line is the instantaneous rate of change, gives \"the exact rate of change in the phenomena.",
          "(a). Find the derivative of a function at a point P (3,9).",
          "(b). Find the tangent line on a given curve y=x at a point P(3,9).",
          "(c). View the slope of the tangent line on a curve y=x at a point P (3,9) graphically.",
          "Solution 4. By first principle rule, the derivative of a given function is:",
          "Result (i) is used to obtain the slope of the tangent",
          "y = y1 = ƒ ̃(x)(x − x,), Point from of the line",
          "The graphical view of the slope of the tangent line is represented in Figure 3",
          "3.1.6 Differentiate of y=x\" from first principles rule",
          "If f(x)=x\", is any integer, then, by first principle rule, the derivative of f(x)=x\" w.rt. x is: f'(x) = lim f(x+Ax)-f(x)",
          "3.1.7 Differentiation of y = (ax+b)\" from first principle",
          "y' + Ay = (ax + b)\" + (\")(ax + by \" (a^x)+(\")(ax+b)\" (adx)2 + (\"\")(ax+b)\" (a_^x)\" + + (a.Ax)\" (ii)",
          "lim {a (\")(ax + b) \" + (\")(ax + b)\" (@Ax)\" + (\") (ax + b)^(ada)\".",
          "(ax+b)\"\" + lim (\") (ax + b)\" (ax)\" + lim (\")(ax+6)3",
          "By applying limit all terms tends to zero except first term so,",
          "This is generalized power rule of differentiation.",
          "Find the average rate of change of the following functions over the indicated intervals:",
          "Use definition for the rate of change to find out the average rate of change over the specified interval for the following functions:",
          "A ball is thrown straight up. Its height after t seconds is given by the formula =-16r+80r. Use definition for the rate of change to determine the average velocity for the specified intervals: a. From 1-2 to 1-2.1. The rate of change of price is called inflation. The price p in rupees after years is p(r)=3r+r+1. Use definition for the rate of change to determine the average rate of change of inflation from z=3 to 1-5 years. What the rate of change means? Explain.",
          "A farmer plants x acres of sugar beets. The profit generated is f(x)=-1800x-9x. Determine the average rate of change of the profit, when the planted area is in between 20 acres and x = 50 acres. What the rate of change means? Explain.",
          "Use first principle rule to determine the derivative of the following functions:",
          "Use function ƒ'(x)=-7x+6 to do the following:",
          "a. Find the derivative of a function at point P(5,-4).",
          "b. Find the tangent line on the curve y=x-7x+6 at point P(5, 4).",
          "c. View the slope of the tangent line on the curve at P(6, 0)?",
          "Use definition of derivative to determine the slope of the tangent line to the curve at a given point and then find out the tangent line equation on that curve at the same point, for the following curves:",
          "There is always an odometer and a speedometer in an automobile. These two things work in tandem and allow the driver to determine the speed of his/her vehicle and the distance he/she has traveled.",
          "Electronic versions of these two gauges simply use derivatives to transform the data sent to the electronic motherboard from the tyres to miles per hour (MPH) and distance (KM).",
          "In previous section, the derivative of a function f(x) is defined:",
          "We learned that the derivative is found by applying the first principle rule. Now, after doing the exercise for the previous section, you may be wondering whether there is a shorter way of finding the derivative. In this and the next several sections, the discussion on the theorem that provides easier ways of finding derivatives.",
          "Theorem-1: The derivative of a constant is zero",
          "Proof: Iff(x) = c, where e is any constant, then, by first principle rule, the derivative of a constant function",
          "This calculation develops the rule that the derivative of a constant function is zero.",
          "If ƒ (x) = c, where e is any constant, then: f'(x)=0",
          "5 Differentiate the following constant functions:",
          "ution The graphs of the functions are horizontal lines parallel to x-axis, since all function are constant. The derivative in each case is therefore going to be zero.",
          "Theorem-2: The derivative of any constant multiple of a function is equal to the product of that const and the derivative of the function.",
          "If f(x)=c.g(x), where e is any constant, then by the first principle rule, the derivative",
          "This calculation develops the rule that the derivative of a constant multiple function is product of the constant function and the derivati of a function f(x).",
          "In general: If g(x)=x\" and f(x)=cg(x), c is any constant, then: f(x) = cg′(x) = cme\"\" Example 6 Differentiate the following functions:",
          "If ƒ (x)=4x2, then, the derivative of a give function is: If f(x)=0.555x\", then, the derivative of a given function is:",
          "Theorem-3: The derivative of a sum (or difference) of two functions is equal to the sum (or difference) of their derivatives.",
          "Proof: To determine the derivative of a polynomial, such as the derivative of the sum or difference of two or more functions, we need to develop a rule that could be used in the determination of a derivative like f(x)=3x2+2x+3. In this situation, if h(x) = f(x)+g(x), then, our task is to determine '(x) by first principle rule of differentiation:",
          "By subtraction equation (1) from equation (1)",
          "Now, apply lim on both sides of equation (iv)",
          "We can say that the derivative of a sum of two functions is the sum of the derivatives of two functions. The difference of two functions/(x)-g(x) can be written as",
          "the sum of f(x)-g(x)=f(x)+-g(x)]. Thus, the derivative of the difference of two functions is the difference of their derivatives.",
          "In general: If u = f(x) and vg (x), then, the sum rule can be restated using the notations:",
          "This rule generalizes to the sum and difference of any given number of functions."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-3",
        "num": "7",
        "title": "Example 7",
        "problem": "If f(x)=3x+4x and g(x)=7x-2 the differentiate f(x)+g(x) and f(x)= g(x)",
        "given": "",
        "method": "",
        "steps": [
          "Proof: If (x)=√(x)g(x), and f(x) and g(x) are differentiable functions of x, then by first principle rule,",
          "Theorem-3: The derivative of a sum (or difference) of two functions is equal to the sum (or difference) of their derivatives.",
          "Proof: To determine the derivative of a polynomial, such as the derivative of the sum or difference of two or more functions, we need to develop a rule that could be used in the determination of a derivative like f(x)=3x2+2x+3. In this situation, if h(x) = f(x)+g(x), then, our task is to determine '(x) by first principle rule of differentiation:",
          "By subtraction equation (1) from equation (1)",
          "Now, apply lim on both sides of equation (iv)",
          "We can say that the derivative of a sum of two functions is the sum of the derivatives of two functions. The difference of two functions/(x)-g(x) can be written as",
          "the sum of f(x)-g(x)=f(x)+-g(x)]. Thus, the derivative of the difference of two functions is the difference of their derivatives.",
          "In general: If u = f(x) and vg (x), then, the sum rule can be restated using the notations:",
          "This rule generalizes to the sum and difference of any given number of functions."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-4",
        "num": "7",
        "title": "Example 7",
        "problem": "If f(x)=3x+4x and g(x)=7x-2 the differentiate f(x)+g(x) and f(x)= g(x)",
        "given": "",
        "method": "",
        "steps": [
          "Proof: If (x)=√(x)g(x), and f(x) and g(x) are differentiable functions of x, then by first principle rule,",
          "with f(x) and vg (x), then the quotient rule can be restated"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-5",
        "num": "8",
        "title": "Example 8",
        "problem": "Differentiate the following functions:",
        "given": "",
        "method": "",
        "steps": [
          "Few simple examples of applications of differentiation are given in this section.",
          "- Constant multiple of x\" Product of functions",
          "Sum (or difference) of functions Quotient of two functions"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-6",
        "num": "9",
        "title": "Example 9",
        "problem": "The cost in (million) dollars to produce x units of wheat is given by",
        "given": "",
        "method": "",
        "steps": [
          "If C(x)=5000+20x+10√x, then the marginal cost is the derivative of C (x) with respect to x:",
          "The marginal cost at x=9 units is obtained by inserting x-9 in C′(x):",
          "The marginal cost at x = 16 units is obtained by inserting x16 in C'(x):",
          "The marginal cost at x=25 units is obtained by inserting x =25 in C′(x):",
          "In business and economics the rates of change of such variables as cost, revenue and profit are most important. Economists use the word marginal to refer to rates of change. For example, the marginal cost refers to the rate of change of cost. Since the derivative of a function gives the rate of change of the function, a marginal cost (or revenue of profit) function is found by taking the derivative of the cost (or revenue of profit) function. The marginal cost at some level of production is the cost to produce the (x+1)st item (ie., one more item).",
          "\"The chain rule is a rule which we use to differentiate the composite functions\". We have learnt about composition of functions in unit-2 that a function is a composite functions of the two similar functions f(x) and g(x) if it is written as (g(x)]. In other words it is a function of a function. For example sin(x) is a composite functions because of we consider f(x)= sin(x) and g(x) = x2 then / [g(x)] = sin(x). Generally, we write chain rule as;",
          "Proof: For our convenience, we set Let u= g(x) the equation (i) will be",
          "Now, subtracting equation (i) from equation (iii)",
          "Substitute the value of g(x+Ax) from equation (vi) to equation (v)",
          "Multiply and divide the right side of equation"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-7",
        "num": "10",
        "title": "Example 10",
        "problem": "Differentiate the following functions w.r.LX.",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-8",
        "num": "11",
        "title": "Example 11",
        "problem": "The revenue realized by a small city from the collection of fines from parking tickets is given by R(x) 8000 where x is the number of work hours each day that can be devoted to parking.",
        "given": "",
        "method": "",
        "steps": [
          "We need to find the change in revenue with respect to time t. The chain rule is used to",
          "This tells us that the revenue is being lost at the rate of approximately $94 per day.",
          "If y = f(x) is any differential function of x, then it admits an inverse function x = g(y). Suppose y is changed by a small amount Ay. This will cause x to change by an amount Ax, The increment. Ar in x corresponds to the increment Ay in y is determined from",
          "Leibniz was the first person who mentioned the composite of the square root function and the function on 1676. The common notation of the chain rule is also due Leibniz.",
          "The derivative of y = (4x-3)' is 12(4x-3). This result agrees to result",
          "In words, ifƒ(x) is equal to an expression in x raised to a power of n, then f(x) is equal to the product of times the expression to the n-1 power times the derivative of the expression with respect to the variable. The statement is known as the general power rule.",
          "If y = f(x)=(11x-7) then, the first derivative of a given function is:",
          "If two differential functions x-f() and yg (1) of parameter t. If th(x) is an inverse function of x= f(t). then y=g[h(x)] is a function of x.",
          "Whether y is expressed explicitly or implicitly in terms of x, we can still differentiate to find If y is expressed explicitly in terms of x, then dy will also be expressed",
          "explicitly in terms of x. Ify is expressed implicitly in terms of x, then of x and y.",
          "dy Fortunately, there is a simple technique based on the chain rule that allows us to find without first solving the equation for y explicitly. This technique is known as implicit differentiation. It consists differentiation of the both sides of the equation with respect to x and then solving the resultant equation",
          "14 Differentiate the implicit equation xy+2y=3x+2y.",
          "The implicit equation is The implicit differentiation of",
          "is obtained by differentiating both sides w.r.L. x."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-9",
        "num": "15",
        "title": "Example 15",
        "problem": "Find the slope of a tangent line to the circle x+y=5x+4y at a particular point P(5,4).",
        "given": "",
        "method": "",
        "steps": [
          "At a point P(5, 4), the slope of the tangent line is:",
          "Note that the expression is undefined at j=2. This makes sense, when you see that the tangent vertical there.",
          "Find the derivative of the following functions w.r.t involved independent variable:",
          "of the following function in terms of parameter t",
          "At a certain factor, the total cost of manufacturing 4 units during the daily production run isC(q)=0.2g2+q+900 dollars. From experience, it has been determined that approximately q(t)='+100r units are manufactured during the first thours of a production run. Compute the rate at which the total manufacturing cost is changing with respect to time one hour after production begins.",
          "Use implicit differentiation to perform for the following functions:",
          "Arrange the following functions explicitly and implicitly to perform",
          "Determine the slope of the tangent line to the curve 3x2-7y+14y=27 at the point P(-3,0).",
          "Suppose two motor boats leave from the same point at the same time. If one boat travels north at 15 miles per hour and the other boat travels east at 20 miles per hour. How fast will the distance between them be changing after 2 hours?",
          "3.5 Differentiation of Trigonometric and inverse Trigonometric Functions",
          "To understand this section we need to know about trigonometric function. For differentiating all trigonometric functions we use the basic rule of differentiation that we have already learnt e.g. We will use product, quotient and chain rules to differentiation functions that are the combination of the trigonometric function.",
          "3.5.1 Differentiation of trigonometric functions (sinx, cosx, tanx, cosecx, secr",
          "Derivative of sin. If y=sinx then the derivative of y = sinx is",
          "Derivative of cos: Ify-cos x, then the derivative of y-cos x is",
          "Subtracting equation from equation y+Ay-y=cos(x+x)=cos(x) Ay = cos(x+Ax)-cos(x)",
          "Ay=-2sin(x+4x+x) sin(x+4x-x) Ay=-2sin(x+4x).sin(47)",
          "Derivative of tan x Ify tanx, then the derivative of",
          "Subtracting equation from equation 3+Ay− y = tan(x+Ax) = tan(x)",
          "The traffic police officers uses radar guns to take the advantage of the easy use of derivatives. When a radar gun is pointed and fired at a car on the motorway. The gun is able to determine the time and distance at which the radar was able to hit a certain section of the car with the use of derivative it is able to calculate the speed at which the car was going and also report the distance that the car was from the radar gun.",
          "sin(x+Ax).cos(x)=sin(x).cos(x+Ax) Ax.cos(x).cos(x+Ax)",
          "Derivative of secx Ify secx, then the derivative of y = sec(x) is",
          "Now, divide equation (iii) by the Ax Ay cot(x+Ax)-cot(x)",
          "Now, apply lim on both sides of equation (iv).",
          "The chain rule can be used to derive the generalization of the power. rule and the rules for differentiating the trigonometric functions, as summarized in the box:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-10",
        "num": "16",
        "title": "Example 16",
        "problem": "Differentiate the following trigonometric functions:",
        "given": "",
        "method": "",
        "steps": [
          "then the quotient rule of differentiation w.r.t. x is used to",
          "17 Differentiate the following trigonometric functions:",
          "4. If the given function is f(x)= secx tanx, then the product rule of differentiation w.r.t. x is used to obtain:",
          "then the quotient rule of differentiation w.r.t. x is used to",
          "(3.x + 2 tan x). —-—-— (x2 + tan x) - (x2 + tan x)=(3x+2 tan x)",
          "Differentiation of inverse trigonometric functions",
          "Derivative of sin x: If ysin\" x, then x = sin y.",
          "Take its reciprocal to obtain the derivative of y w.r.t. X:",
          "Here, the sign of the radical is the same as that of cosy. By definition of sinx:",
          "Derivative of cos 'x: If y=cosx, then.x=cosy.",
          "Take its reciprocal to obtai.. the derivative of y w.rt. I",
          "Here, the sign of the radical is the same as that of sin y. By definition of cos1x",
          "Also, if y lies between 0 and л, then, sin y is necessarily positive. Hence",
          "Derivative of tan 'x: If y=tanx, then x = tan y The differentiation of x = tany w.r.t. y is: d",
          "Take its reciprocal to obtain the derivative of y w.EL. x.",
          "1 dx secy 1+tany 1+x Derivative of see 'x: If",
          "Take its reciprocal to obtain the derivative of y w.r.t. x",
          "We take + sign before the radical sign to obtain: (sec\" x)",
          "Derivative of cosec\" If y=cosecx, then.x=cosecy.",
          "Take its reciprocal to obtain the derivative of y w.EL X",
          "We take + sign before the radical sign to obtain: (cosecx)=",
          "Derivative of cot'x: If y=cotx, then x = coty.",
          "Take its reciprocal to obtain the derivative of y w.rl x",
          "These inverse trigonometric formulas are listed in the box:",
          "The chain rule can be used to derive the generalization of the power rule and the rules for difcrentiating the inverse trigonometric functions, as summarized in the box:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-11",
        "num": "18",
        "title": "Example 18",
        "problem": "Differentiate the following inverse trigonometric functions:",
        "given": "",
        "method": "",
        "steps": [
          "Differentiate the following trigonometric functions by using any suitable rule.",
          "Use any suitable rule of differentiation to perform",
          "Suppose profits on the sale of swimming suits in a departmental store are given approximately by",
          "where P(t) is profit (in hundreds of dollars) for a week of sales t weeks after January first.",
          "a. What is the rate of change of profit t weeks after the first of the year?",
          "b. What is the rate of change of profit 8 weeks after the first of the year? 26weeks after the first",
          "of the year? 50 weeks after the first of the year?",
          "A normal seated adult breathes in and exhales about 0.8 liter of air every 4 seconds. The volume of air P(/) in the lungs t seconds after exhaling is given approximately by (t)=0.45-0.35cos,05:58.",
          "a. What is the rate of flow of airt seconds afterexhaling?",
          "b. What is the rate of flow of air 3 seconds after exhaling? 4 seconds after exhaling? 5 seconds",
          "Differentiation of Exponential and Logarithmic Functions",
          "The goal of this section is to develop the differential calculus of logarithmic and exponential functions. We shall begin by deriving differentiation formulas for In x and e'. The derived formulas will be applied to a number of differentiation problems and applications.",
          "Derivative of e': If y=e, then the derivative of y=e\" by first principle rule is:",
          "Derivative of a': If y=a\", then the derivative of y=a\" by first principle rule is:",
          "3.6.2 Derivative of Inx and log.x from first principle",
          "Derivative of Inx: Ify- Inx, then the derivative of y= Inx by first principle rule is:",
          "Derivative of log..: If y=logx, then the derivative of y= log,x by first principle rule is:",
          "These exponential and logarithmic formulas are listed in the box:",
          "The chain rule can be used to derive the generalization of the power rule and the rules for differentiating the exponential and logarithmic functions, as summarized in the box:",
          "If the given function is f(x)=74-), then the derivative of the given function w.r.t. x is",
          "If the given function is f(x)=log√(x-7x)+x', then the derivative of a given function w.r.t. x is:",
          "If the given function is f(x)= In(e\"\"+e), then the derivative of a given function w.r.t. x is:",
          "If the given function is f(x) = then the derivative of a given function w.r.t. x is:",
          "3.6.3 Use of logarithmic differentiation to algebraic expressions involving product,",
          "Logarithmic differentiation is a procedure in which logarithmis are used to trade the task of differentiating products and quotients for that of differentiating sums and differences. It is especially valuable as a means for handling complicated product or quotient functions and power functions where variables appear in both the base and the exponent."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-12",
        "num": "20",
        "title": "Example 20",
        "problem": "Differentiate the following functions",
        "given": "",
        "method": "",
        "steps": [
          "- Inx + In(x-3)2 - In(x2-4) = ln x+2 In(x-3)-In(x-4),",
          "then on differentiation w.r.L. x. It becomes;",
          "3.7 Differentiation of Hyperbolic and Inverse Hyperbolic Functions",
          "The concept of hyperbolic functions is completely discussed in Unit-2. The differentiation of",
          "hyperbolic functions can be found as follows:",
          "Derivative of sinkx: If y=sin kx, then on differentiation w.t.t. x, it bec",
          "Derivative of cosky: If y= cos krete, then on differentiation w r.t. x, it b",
          "then on differentiation w.r...x throute. sin kr",
          "The chain rule can be used to derive the generalization of the power rule and the rules for dentisung the hyperbolic functions, as summarized in the box:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-3-13",
        "num": "21",
        "title": "Example 21",
        "problem": "Differentiate the following functions: (a). y=cosh(2x-1) (b). y=sech",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-3-1",
        "exercise": "Exercise 3.1",
        "title": "Exercise 3.1",
        "description": "",
        "problems": [
          {
            "id": "ex-3-1-q1",
            "qNo": "1",
            "question": "Find the average rate of change: (a) y=x²+4, x=2 to 3; (b) y=x²+1/x, x=−2 to −3; (c) s=2t²−5t+7, t=1 to 3; (d) h=√(2t+4), t=8 to 8.5.",
            "solution": "Use [f(b)−f(a)]/(b−a). (a) (13−8)/(3−2)=5. (b) f(−2)=7/2 and f(−3)=26/3, so [(26/3)−(7/2)]/(−1)=−31/6. (c) [10−4]/2=3. (d) [√21−√20]/0.5=2(√21−2√5).",
            "diagram": null
          },
          {
            "id": "ex-3-1-q2",
            "qNo": "2",
            "question": "Use the definition of rate of change: (a) s=2t−3, t=2 to 5; (b) y=x²−6x+8, x=3 to 3.1; (c) A=πr², r=2 to 2.1; (d) h=√(t−9), t=9 to 16.",
            "solution": "The average rate is the change in the dependent variable divided by the change in the independent variable. (a) 2. (b) [f(3.1)−f(3)]/0.1=[−0.99−(−1)]/0.1=0.1. (c) π(2.1²−2²)/0.1=4.1π. (d) (√7−0)/(16−9)=1/√7.",
            "diagram": null
          },
          {
            "id": "ex-3-1-q3",
            "qNo": "3",
            "question": "A ball’s height is h(t)=−16t²+80t feet. Find its average velocity from t=2 to 2.1 and from t=2 to 2.01.",
            "solution": "h(2)=96. h(2.1)=97.44, so the first average velocity is (97.44−96)/0.1=14.4 ft/s. h(2.01)=96.1584, so the second is (96.1584−96)/0.01=15.84 ft/s.",
            "diagram": null
          },
          {
            "id": "ex-3-1-q4",
            "qNo": "4",
            "question": "Inflation is modeled by p(t)=3t²+t+1. Find the average rate of change of price from t=3 to t=5 and explain its meaning.",
            "solution": "p(5)=81 and p(3)=31. The average rate is (81−31)/(5−3)=25 rupees per year. Over those two years, the modeled price increased by an average of 25 rupees each year.",
            "diagram": null
          },
          {
            "id": "ex-3-1-q5",
            "qNo": "5",
            "question": "Profit is f(x)=1800x−9x². Find the average rate of change when planted area changes from 20 to 50 acres and explain.",
            "solution": "f(50)=67,500 and f(20)=32,400. Thus [f(50)−f(20)]/(50−20)=35,100/30=1,170. The profit increases by an average of 1,170 currency units per additional acre over this interval.",
            "diagram": null
          },
          {
            "id": "ex-3-1-q6",
            "qNo": "6",
            "question": "Use the first-principle rule to differentiate: (a) 3x; (b) √(5x+6); (c) x²+1; (d) 12−x²; (e) 16x²−7x; (f) 7/x.",
            "solution": "Apply f'(x)=lim_{h→0}[f(x+h)−f(x)]/h and simplify. (a) 3. (b) 5/[2√(5x+6)]. (c) 2x. (d) −2x. (e) 32x−7. (f) −7/x².",
            "diagram": null
          },
          {
            "id": "ex-3-1-q7",
            "qNo": "7",
            "question": "For f(x)=x²−7x+6: (a) find the derivative at P(5,−4); (b) find the tangent line at P(5,−4); (c) find the tangent slope at P(6,0).",
            "solution": "f'(x)=2x−7. (a) f'(5)=3. (b) Point-slope form gives y+4=3(x−5), hence y=3x−19. (c) f'(6)=5.",
            "diagram": {
              "type": "tangent-line",
              "a": 1,
              "b": -7,
              "c": 6,
              "x0": 5,
              "xMin": 0,
              "xMax": 8,
              "title": "Curve and tangent at P(5, −4)"
            }
          },
          {
            "id": "ex-3-1-q8",
            "qNo": "8",
            "question": "Use the derivative definition to find each tangent slope and tangent line: (a) f=x²+7x at x=3; (b) f=6x²−11x−10 at x=1; (c) f=3x²−6x−10 at x=0; (d) f=2x³+3x−4 at x=1.",
            "solution": "Differentiate using first principles, then use y−f(a)=f'(a)(x−a). (a) f'(x)=2x+7; at x=3 the point is (3,30), slope 13, line y=13x−9. (b) f'=12x−11; point (1,−15), slope 1, line y=x−16. (c) f'=6x−6; point (0,−10), slope −6, line y=−6x−10. (d) f'=6x²+3; point (1,1), slope 9, line y=9x−8.",
            "diagram": null
          }
        ],
        "pageStart": 63,
        "pageEnd": 100
      },
      {
        "id": "ex-3-2",
        "exercise": "Exercise 3.3",
        "title": "Exercise 3.3",
        "description": "",
        "problems": [
          {
            "id": "ex-3-3-q1",
            "qNo": "1",
            "question": "Differentiate: (a) w=4(x³−4x+2)^5; (b) y=(4x−x²)^11/5; (c) u=∛(1−3r²); (d) s=1/(3t+1)^7.",
            "solution": "Apply the chain rule. (a) dw/dx=20(x³−4x+2)^4(3x²−4). (b) dy/dx=(11/5)(4x−x²)^10(4−2x). (c) du/dr=−2r/(1−3r²)^{2/3}. (d) Writing s=(3t+1)^{−7}, ds/dt=−21/(3t+1)^8.",
            "diagram": null
          },
          {
            "id": "ex-3-3-q2",
            "qNo": "2",
            "question": "Find f'(x): (a) f=(2x−5)^3(5x−7); (b) f=(x+2)^2/(x−1); (c) f=[(2x−5)/(x−4)]^4; (d) f=x√(2x²+11).",
            "solution": "(a) Product and chain rules give f'=(2x−5)^2(40x−67). (b) Quotient rule gives f'=(x+2)(x−4)/(x−1)^2. (c) Chain and quotient rules give f'=−12(2x−5)^3/(x−4)^5. (d) Product rule gives f'=√(2x²+11)+2x²/√(2x²+11)=(4x²+11)/√(2x²+11).",
            "diagram": null
          },
          {
            "id": "ex-3-3-q3",
            "qNo": "3",
            "question": "Find dy/dx for each parametric curve: (a) x=1+t², y=t³+2t²+1; (b) x=3at²+2, y=6t⁴+9; (c) x=a(1−t²)/(1+t²), y=2bt/(1+t²); (d) x=3at/(1+t³), y=3at²/(1+t³).",
            "solution": "Use dy/dx=(dy/dt)/(dx/dt). (a) (3t²+4t)/(2t)=(3t+4)/2. (b) 24t³/(6at)=4t²/a. (c) [2b(1−t²)/(1+t²)²]/[−4at/(1+t²)²]=−b(1−t²)/(2at). (d) [3at(2−t³)/(1+t³)²]/[3a(1−2t³)/(1+t³)²]=t(2−t³)/(1−2t³).",
            "diagram": null
          }
        ],
        "pageStart": 63,
        "pageEnd": 100
      },
      {
        "id": "ex-3-3",
        "exercise": "Exercise 3.4",
        "title": "Exercise 3.4",
        "description": "",
        "problems": [
          {
            "id": "ex-3-4-q1",
            "qNo": "1",
            "question": "Using first principles, differentiate: (a) sin(2x); (b) cot(3x); (c) cos(3x)+tan(3x); (d) cot²x; (e) tan√x; (f) sin²x.",
            "solution": "Apply f'(x)=lim_{h→0}[f(x+h)−f(x)]/h and the standard trigonometric limits. (a) 2cos(2x). (b) −3csc²(3x). (c) −3sin(3x)+3sec²(3x). (d) −2cot x csc²x. (e) sec²(√x)/(2√x). (f) 2sin x cos x.",
            "diagram": null
          },
          {
            "id": "ex-3-4-q2",
            "qNo": "2",
            "question": "Differentiate: (a) x²cot(3x); (b) y=(sin2x+cot3x)²; (c) y=4cosec(2x); (d) y=2tan((x+3)²); (e) y=√(tan x)/cos√x; (f) y=(1+tan2x)/cosec3x.",
            "solution": "Use product, quotient, and chain rules. (a) 2x cot(3x)−3x²csc²(3x). (b) 2(sin2x+cot3x)(2cos2x−3csc²3x). (c) −8csc(2x)cot(2x). (d) 4(x+3)sec²((x+3)²). For (e), write y=√(tan x)sec√x; then y'=sec²x·sec√x/[2√(tan x)]+√(tan x)sec√x tan√x/(2√x). (f) Rewrite y=(1+tan2x)sin3x; y'=2sec²(2x)sin3x+3(1+tan2x)cos3x.",
            "diagram": null
          },
          {
            "id": "ex-3-4-q3",
            "qNo": "3",
            "question": "Differentiate: (a) cos^{−1}(x/a); (b) tan^{−1}(x/p); (c) cot^{−1}(a/x); (d) cosec^{−1}√(1+x²); (e) cosec^{−1}(t+3); (f) x tan^{−1}((x+1)/(x−1)).",
            "solution": "(a) −1/√(a²−x²). (b) p/(p²+x²). (c) a/(a²+x²). (d) −1/(1+x²) for x>0; use the absolute-value form at x<0. (e) −1/(|t+3|√((t+3)²−1)). (f) By the product and chain rules, tan^{−1}((x+1)/(x−1))−2x/((x−1)²+(x+1)²).",
            "diagram": null
          },
          {
            "id": "ex-3-4-q4",
            "qNo": "4",
            "question": "Profit is P(t)=5−5cos(πt/10) hundred dollars, where t is weeks after January 1. Find the rate of change at t=8, 26, and 50 weeks.",
            "solution": "P'(t)=(π/2)sin(πt/10), in hundreds of dollars per week. Thus P'(8)=(π/2)sin(4π/5)≈0.9233; P'(26)=(π/2)sin(13π/5)≈1.4939; P'(50)=(π/2)sin(5π)=0.",
            "diagram": null
          },
          {
            "id": "ex-3-4-q5",
            "qNo": "5",
            "question": "The air volume is V(t)=0.45−0.35cos(πt/2) litres for 0≤t≤8 seconds. Find the rate of flow at t=3, 4, and 5 seconds.",
            "solution": "Differentiate: V'(t)=0.175π sin(πt/2) litres per second. Therefore V'(3)=−0.175π≈−0.5498 L/s, V'(4)=0, and V'(5)=0.175π≈0.5498 L/s.",
            "diagram": null
          }
        ],
        "pageStart": 63,
        "pageEnd": 100
      },
      {
        "id": "ex-3-4",
        "exercise": "Exercise 3.5",
        "title": "Exercise 3.5",
        "description": "",
        "problems": [],
        "pageStart": 63,
        "pageEnd": 100
      },
      {
        "id": "ex-3-5",
        "exercise": "Exercise 3.2",
        "title": "Exercise 3.2",
        "description": "",
        "problems": [],
        "pageStart": 63,
        "pageEnd": 100
      },
      {
        "id": "ex-3-6",
        "exercise": "Exercise",
        "title": "Exercise",
        "description": "",
        "problems": [],
        "pageStart": 63,
        "pageEnd": 100
      },
      {
        "id": "ex-3-7",
        "exercise": "Review Exercise 3",
        "title": "Review Exercise 3",
        "description": "",
        "problems": [],
        "pageStart": 63,
        "pageEnd": 100
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-4",
    "number": 4,
    "title": "Higher Order Derivatives and Applications",
    "titleUrdu": "",
    "pageRange": "Printed pages 101–129",
    "pageStart": 101,
    "pageEnd": 129,
    "sections": [
      {
        "id": "sec-4-1",
        "title": "4.1 Higher Order Derivatives",
        "theory": "The successive derivatives of some functions are gathered to obtain the general form of nth derivatives in the following cases:\n\nIf f(x)=(ax+b)\", m is positive integer, then the successive derivatives of the given function developed a general term for the nth derivative of a function:\n\nIf f(x) = ln(ax+b), then the successive derivatives developed a general term for the nth derivative of a function:\n\nIf f(x)=a\", then the successive derivatives developed a general term for the nth derivative:\n\nIf a=e, then the nth derivative of f(x)=e\" is obtained by inserting a➡e:\n\nIf f(x)=sin(ax+b), then the successive derivatives developed a general term for the nth\n\nIf f(x)= cos(ax+b), then the successive derivatives developed a general term for the n-th\n\nIf f(x)=(6x+4) with a = 6, b=4 and 9, then the 5 derivative of the given function is\n\nwith a 4 and 6-3, then the 5 derivative of the given function is obtained by\n\nIf f(x) = ln(4x+7) with a 4 and 6-7, then the 5 derivative of the given function is obtained by inserting n = 5 in equation:\n\nIf f(x)=6′′ with a 6 and m 4, then the 5 derivative of the given function is obtained by inserting » = 5 in equation:\n\nIf ƒ '(x) = e** with m=4, then the 5 derivative of the given function is obtained by inserting a = 5 in\n\nIf f(x)=sin(5x+7) with a 5 and b = 7 then the 5th derivative of the given function is obtained\n\nThe first implicit derivative of (i) w.r.t. x is:\n\nThe second implicit derivative of first implicit derivative (ii) w.rt. x is:\n\nThe first implicit derivative of (i) w.r.t..x is:\n\nThe second implicit derivative of first implicit derivative (ii)\n\nEquation (1) can be written simplified form for 1 order\n\nThe first derivative of the parametric functions x = x() and y=y(f) w.r.t. x is:\n\nThe second derivative of the parametric functions is obtained by taking the derivative of\n\nThe quotient rule of differentiation is used to simplify the right hand side of equation (ii):\n\nUse (ii) in (iii) to obtain the general term for second derivative of parametric functions x (1) and\n\nIn light of result (iv), the first and second derivatives of the parametric functions\n\nThe procedure to use of MAPLE command diff is illustrated in the following example.\n\nFor second derivative, after command, press the \"Enter\" key two times to obtain the second derivative of a given function above result.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-4-2",
        "title": "4.2 Maclaurin's and Taylor's Expansions",
        "theory": "Often the value of a function and the values of its derivatives are known at a particular point and from this information it is desired to obtain values of the function around that particular point. The Taylor polynomials and Taylor series allow us to make such estimates.\n\nIf f(x) and its a derivatives at x=x, are (x). \"(x)/(x). then the nth order Taylor polynomial p(x) may be written as:\n\nThis polynomial provides an approximation to f(x). The polynomial and its n derivatives are very much matched with the values off(x) and its first a derivatives evaluated at x=x\n\nand its derivatives evaluated at x=0 are known by (0)=1,\n\n0)=1. Use fourth order Taylor polynomial about x=0 to estimate\n\nSolution) The fourth order Taylor polynomial p,(x) is obtained by terminating the Taylor polynomial (i) after fourth order derivative term:\n\nThe Taylor polynomial (iii) is used to obtain approximation of a function y=√(x)=e* at x=0.2:\n\nNotice that the Taylor polynomial approximation equals the actual function value\n\nTaylor's Series: The Taylor polynomials have been used to estimate the values of y=(x) at various x values, It is reasonable to ask:\n\n4. How accurate Taylor polynomials generated by y=(x) atr, to approximate y=f(x) at values of other\n\nHIGHER ORDER DERIVATIVES AND APPLICATIONS If more and more terms are used in the Taylor polynomial, then this will produce a better and better\n\nTo answer these questions, we introduce the Taylor series. As more and more terms are included in the\n\nTaylor polynomial, we obtain an infinite series, known as a Taylor series:\n\nFor some Taylor series, the value of the series equals the value of the function for every value of x. That is, the Taylor series approximations of e, sin and cos.xequal the values of e. sin x and cosx for every value of However, some functions have a Taylor series which equals the function only for a limited range of x values. For example, the value of a function f(x)=- which equals its Taylor series only when −1<x<1.\n\nA special case of a Taylor series occurs, when the function = f(x) is known only at the origin x=0. This special condition imposed on Taylor series, develops the Maclaurin's series:",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-4-3",
        "title": "4.3 Applications of Derivatives",
        "theory": "P(xo-y, Jis (y-3)= mix −x). ii. The normal equation at a point\n\nIf my is the slope of the first curve and my is the slope of the second curve, then the angle of intersection in between these two curves at a point of intersection is the angle in between their tangents at that point. This angle takes the notation:\n\nSolution The required angle of intersection in between the given two curves is: tan\n\nFor point of intersection, solve the system of nonlinear equations for the unknowns x and y.\n\nUsing first equation of the nonlinear system (ii) in second equation to obtain:\n\nThe set of x values is used in first equation of the nonlinear system (ii) to obtain a set of y value Put x=0 to obtain y=x-2x+1=1\n\nPut x=2 to obtain y=x-2x+1-8-4+1-5 This process developed a set of points of intersection: (0,1), (−1,2), (2,5).\n\nThe slope of the first curve at a point (2, 5) is: -3x-2=>\n\nThe slope of the second curve at a point (2,5) is: -2x=\n\nThe slopes m, and m, are used in (i) to obtain the angle of intersection in between the given two curves.\n\nPoint on a curve where the tangent is parallel to the given line\n\nLook at the following example the procedure to find the point on a curve where tangent is parallel t the given line is illustrated in this example.\n\nFind all the points on the curve y=2x+4x2 where tangent line is parallel to the lim\n\nIn each case, find the equation of the tangent line to the curve at the indicated value of x a j=√/x+1, x=3\n\nIn each case, find the equation of normal to the curve at the indicated value of x: a. y=xeʻ. x-l\n\na. Find an equation of the tangent line to the curvex+y=13 at (-2, 3).\n\nFind an equation of the tangent line to the curve sin(x-3)=xy at (0,m).\n\ne. Find an equation of the normal line to the curve x+2yyat (1,-1).\n\nd. Find an equation of the normal line to the curve x-2=-3x-1 at (1, 2). a. Show that the first four terms in the Taylor series expansion of f(x)-tan x\n\nFind the critical values of the given functions in the following problems and show where the function is increasing and where it is decreasing.\n\nFind the critical values of the following functions:\n\nDetermine whether the given function has a relative maximum, a relative minimum, or neither\n\ngiven critical values for the following problems:\n\nFind all critical points of the functions in the following problems, and determine where the gra\n\nthe function is rising, falling, concave up, or concave down. Sketch the graph.\n\nFind all relative extrema of the following functions:\n\nSuppose f(x) is a differential function with derivative f(x)=(x-1)(x-2)(x-4)(x+5) Find all critical values of f(x) and determine whether each corresponds to a relative maximum relative minimum, or neither.\n\nSuppose f(x) is a differential function with derivative f(x)=!\n\nFind all critical values of (x) and determine whether each corresponds to a relative maximi a relative minimum, or neither.\n\nA company has found through experience that increasing its advertising also increases up to a point. The company believes that the mathematical model connecting profit in hundre of dollars P(x) and expenditures on advertising in thousands of dollars x P(x)=80+108x-r', 0≤x≤10\n\na. Find the expenditure on advertising that leads to maximum profit.\n\nThe total profit P(x) (in thousands of dollars) from the sale of x hundred thousands of automobil tires is approximated by P(x)=-1+9x+120x-400, 3≤x≤15\n\nFind the number of hundred thousands of tires that must be sold to maximize profit. Find the maximum profit.\n\nThe percent of concentration of a drug in the bloodstream x hours after the drug is admini:\n\nOn what time intervals is the concentration of the drug increasing?\n\nFind the time at which the concentration is a maximum.\n\nA diesel generator burns fuel at the rate of G(x)=-",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-4-4",
        "title": "4.4 Maxima and Minima",
        "theory": "Always the maximum and minimum values of a function can be read from its graphical view. For a quadratic function (whose graph is parabola), the maximum or minimum values can be determined without graphing by finding the vertex algebraically. For functions whose graphs are not known, other techniques are needed. In this unit, we shall see how to use derivatives to determine the maximum and minimum values of a function as well as the intervals where the function is increasing or decreasing. 4.4.1 Increasing and decreasing functions\n\nSuppose an ecologist has determined the size of a population of a certain species as a function () of time t (months). If it turns out that the population is increasing until the end of the first year and decreasing thereafter. It is reasonable to expect the population to be maximized at time 1-12 and for the population curve to have a high point\n\nIf the graph of a function (r), such as this population curve, is rising throughout the interval 0 << 12, then we say that (r) is strictly increasing on that interval. Similarly, the graph of the function in Figure 4.3 is strictly decreasing on the interval 12 <1<20 These terms are defined more formally in the Figure 4.4.\n\nThe function f(x) is strictly increasing on an interval (a, b), if\n\nf(x) < f(x), whenever xx, for x, and x, on (a, b). The function () is strictly decreasing on an interval (a, b), if f(x) > f(x), whenever x < x, for x, and 1,on (a, b).\n\nThe function f(x)=x is a parabola passing through the origin. Take any two points x, and in the interval (a, b) for which: f(x)=√(x)=x − x' = (1, − 1)(x + 1)\n\nIf x,,x,€ (0,∞) with condition x,>x,, then the function f(x) is increasing in the interval (0,0):\n\nf(x)>f(x), both (x-x)and (x+x)ane+ve, when x2 > Xj\n\nIfx,,, (0,0) with condition x,>x,, then the function f(x) is decreasing in the interval (-0,0)-\n\n(c) is increasing on (a, b) if (c) is decreasing on (a, b) if\n\nx, x, then there exist a point c between x, and x, such that\n\nIf a function is continuous on ja, hj Trenciable on (a, b) then there\n\nSimilarly, the proof of part (ii) can be done which is left as an exercise for the reader.\n\nSolution For graphical view, the given function through completing square\n\nis compared with the general equation of parabola f(x)=a[x-h)+k to obtain a parabola with vertex (-1,-4) that opens upward (a =lis positive). The graph of a parabola through the points (-4.5) and (2,5) is shown in the Figure 4.5.\n\nThe derivative of a given function with respect to x is the\n\nIf the slope of parabola is f(x) > 0 (positive), then it gives\n\nThis shows that the given function (r) is increasing in the interval\n\nIf the slope of parabola is \"(x) <0 (negative), then it gives\n\nThis shows that the given function f(x) is decreasing in the interval (-0,−1).\n\nIf the slope of parabola is '(x)=0(zero), then it gives\n\nThis shows that the given function f(x) is neither increasing nor decreasing at a vertex (-1,-4). 4.4.3 Examination of a given function for extreme values\n\nTypically the extrema of a continuous function occur either at endpoints of the interval or at points where the graph has a \"peak\" or a \"valley\" (points where the graph is higher or lower than all nearby points). For example, the function (r) in Figure 4.6 has \"peaks\" at B and D and \"valleys\" at C and E. Peaks and valleys are what we call the relative extrema.\n\nThe exact location of a relative maximum or minimum rather than a graphic's approximation can normally be found by using derivatives. The concept developed is as under:\n\nLet f(x) be a function as a roller coaster track with a roller coaster car moving from left to right along the graph in the Figure 4.6. As the car moves up towards a peak, its floor tilts upward. At the\n\nThe first derivative of a function can be used to determine whether the function is increa decreasing on a given interval. We shall use this information to develop a procedure called th derivative test for classifying a given point as a relative maximum, a relative minimum, or neither\n\nThe steps involved in first-derivative test for relative extrema are the following:\n\n1. Find all critical values of f(x). That is, find all numbers e such that f(c) is defined and\n\nThe point (c. (c)) is a relative maximum if ƒ\"'(x)>0 (rising) for all x in an open interval ( the left of c, and (x) <0 (falling) for all x in an open interval (c. b) to the right of c The point (c. /(c)) is a relative minimum if (x) <0 (falling) for all x in an en interval( the left of c, and \"(x)>0 (rising) for all in an open interval (c, b) to the right of c The point (c, (c)) is not an extremum if the derivative f(x) has the same sign in open in (a, c) and (c, b) on both sides of c.\n\nIn light of first-derivative test, the function f(x)=x-3x2-9x+1 (example 2-4) has the values-1 and 3. The function f(x) is increasing when <-1 and x > 3 and decreasing when −1 The first derivative test tells us that there is a relative maximum of 6 at x=-1 and a relative minim -26 at x=3.\n\nSolution The first derivative of f(x)=2x+3x2-12x-5 is: -\n\nvalues -3,0 and 2. Many other choices of the test values are\n\nalso possible, but we try to select numbers that will make the computations easy. This is shown\n\nThe test values -3 and 0 are used for the critical value x-2 to obtain:\n\nThe value of the derivative is positive (rising) to the left of -2 and negative (falling) to the right of -2. Thus, x=-2 leads a relative maximum point\n\nThe test values 0 and 2 are used for the critical value x=1 to obtain:\n\nThe value of the derivative is negative (falling) to the left of 1 and positive (rising) to the right of 6. Thus, x = 1 leads a relative minimum point. ƒ(1)=2(1)+3(1)-12(1)-5=-12 Thus, the arrow pattern in the figure suggests that the graph of f(x) has a relative maximum at (-2, 15) and a relative minimum at (1,–12). The Second Derative Rule: It is often possible to classify a critical point P(c, ƒ (c)) on the graph of f(x) by examining the sign of \"(c). Specifically, if (c)=0 and (c)>0, then there is a horizontal tangent line at P and the graph of (x) is concave up in the neighborhood of P. This means that the graph of f(x) is cupped upward from the horizontal tangent at P and to expect P to be a relative minimum, as shown in Figure 4.11.\n\ntraveling x miles per hour on a straight level road. If fuel costs $2 per gallon, find the speed that produce the minimum total cost for a 1000 mile trip. Find the maximum total cost. Solution The total cost of the trip in dollars is the product of the (number of gallons per mile) (the nu of miles) (the cost per gallon) that develops the rule: C(x)=\n\nThe independent variable x represents speed, only positive values of make sense here. Thus domain of C(x) is the open interval (0,0) and there are no endpoints to check.\n\nThe first and second derivatives of C(x) are the following: C(x)=\n\nPut C(x)=0 to obtain the critical values: The only critical number in the domain is x=28.3. The second derivative test at a critical value x\n\nThe second derivative test shows that the critical value = 28.3 leads to a minimum value. The minim\n\ntotal cost is found by inserting x 28.3 in the cost function: C(28.3) 8000+10(28.3) Example 30 The supporting cable of a pipeline suspension system forms a parabolic are between supports, which is described by the equation y=0.03125 -1.25x. The distances are measured in mele The origin of the axis system is at the point where the cable attaches to the left support tower. Where point is on the and how far is it below the attachment point?\"\n\nSolution For the low point of the cable, we need to find the first and second derivatives of the given function:\n\nSince the second derivative is positive for all values of x, the critical value x = 20 will produce the minimum value on the curve.\n\nThe low point on the cable occurs 20.0 m to the right of the left to original function to obtain the distance from the low point of the point:\n\nTherefore, the low point of the cable is 20.0 m to the nigh\n\nThe procedure to the use of MAPLE command maximize ( compl te maximum (minimum) value of a function is illustrated in the following example,\n\nThis result is obtained through right click on the last end of the expression by selecting \"Optimization < maximize local\"on the context menu.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-4-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Find the second derivative of the following functions:",
        "given": "",
        "method": "",
        "steps": [
          "The second derivative of y = (0) can be written with any of the following notations:",
          "The third derivative can be written in a similar way. For derivative #24, the derivative holds the notation f(x), n = 4,5,......",
          ",then the first and second derivatives of the given",
          "function through quotient rule are the following:",
          "In the previous unit, we saw that the first derivative of a function represents the rate of change of the function. The second derivative, then, represents the rate of change of the first derivative. If a function describes the position of moving object at time t, then the first derivative gives the velocity of the object. That is, if y=3() describes the position of the object at time t, then v(t)=() gives the velocity at a time t.",
          "The rate of change of velocity is called acceleration. Since the second derivative gives the rate of change of the first derivative, the acceleration is the derivative of the velocity. Thus, if a(t) represents the acceleration at time t, then"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-2",
        "num": "2",
        "title": "Example 2",
        "problem": "An object is moving along a straight line with its position s(t) (in feet) at time t (in seconds):",
        "given": "",
        "method": "",
        "steps": [
          "The velocity at any time t is the first derivative of s(t) w.r.t. r. v=",
          "The acceleration at any time t is the first derivative of (f) w.rt. a=",
          "The object will stop at seconds, since we want time 120.",
          "4.1.1 Higher order derivatives of algebraic, trigonometric, exponential and logarithmic",
          "The successive derivatives of some functions are gathered to obtain the general form of nth derivatives in the following cases:",
          "If f(x)=(ax+b)\", m is positive integer, then the successive derivatives of the given function developed a general term for the nth derivative of a function:",
          "If f(x) = ln(ax+b), then the successive derivatives developed a general term for the nth derivative of a function:",
          "If f(x)=a\", then the successive derivatives developed a general term for the nth derivative:",
          "If a=e, then the nth derivative of f(x)=e\" is obtained by inserting a➡e:",
          "If f(x)=sin(ax+b), then the successive derivatives developed a general term for the nth",
          "If f(x)= cos(ax+b), then the successive derivatives developed a general term for the n-th"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Find the 5th derivatives of the following functions:",
        "given": "",
        "method": "",
        "steps": [
          "with a 4 and 6-3, then the 5 derivative of the given function is obtained by",
          "If f(x) = ln(4x+7) with a 4 and 6-7, then the 5 derivative of the given function is obtained by inserting n = 5 in equation:",
          "If f(x)=6′′ with a 6 and m 4, then the 5 derivative of the given function is obtained by inserting » = 5 in equation:",
          "If ƒ '(x) = e** with m=4, then the 5 derivative of the given function is obtained by inserting a = 5 in",
          "If f(x)=sin(5x+7) with a 5 and b = 7 then the 5th derivative of the given function is obtained",
          "4.1.2 Second derivative of implicit, inverse trigonometric and parametric functions"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-4",
        "num": "4",
        "title": "Example 4",
        "problem": "The first implicit derivative of (i) w.r.t. x is:",
        "given": "",
        "method": "",
        "steps": [
          "The second implicit derivative of first implicit derivative (ii) w.rt. x is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-5",
        "num": "5",
        "title": "Example 5",
        "problem": "Find the second derivative of cosy+y=20.",
        "given": "",
        "method": "",
        "steps": [
          "The second implicit derivative of first implicit derivative (ii)",
          "Equation (1) can be written simplified form for 1 order"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-6",
        "num": "6",
        "title": "Example 6",
        "problem": "Find the second derivative when the parametric functions are:",
        "given": "",
        "method": "",
        "steps": [
          "The second derivative of the parametric functions is obtained by taking the derivative of",
          "The quotient rule of differentiation is used to simplify the right hand side of equation (ii):",
          "Use (ii) in (iii) to obtain the general term for second derivative of parametric functions x (1) and",
          "In light of result (iv), the first and second derivatives of the parametric functions",
          "4.1.3 MAPLE command diff repeatedly to find higher order derivative of",
          "The procedure to use of MAPLE command diff is illustrated in the following example."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-7",
        "num": "7",
        "title": "Example 7",
        "problem": "Differentiate",
        "given": "",
        "method": "",
        "steps": [
          "Often the value of a function and the values of its derivatives are known at a particular point and from this information it is desired to obtain values of the function around that particular point. The Taylor polynomials and Taylor series allow us to make such estimates.",
          "4.2.1 Maclaurin's and Taylor's theorems. Using these theorems to expand sinx, ens",
          "If f(x) and its a derivatives at x=x, are (x). \"(x)/(x). then the nth order Taylor polynomial p(x) may be written as:",
          "This polynomial provides an approximation to f(x). The polynomial and its n derivatives are very much matched with the values off(x) and its first a derivatives evaluated at x=x"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-8",
        "num": "8",
        "title": "Example 8",
        "problem": "The function = f(x)",
        "given": "",
        "method": "",
        "steps": [
          "0)=1. Use fourth order Taylor polynomial about x=0 to estimate",
          "Solution) The fourth order Taylor polynomial p,(x) is obtained by terminating the Taylor polynomial (i) after fourth order derivative term:",
          "The Taylor polynomial (iii) is used to obtain approximation of a function y=√(x)=e* at x=0.2:",
          "Notice that the Taylor polynomial approximation equals the actual function value",
          "Taylor's Series: The Taylor polynomials have been used to estimate the values of y=(x) at various x values, It is reasonable to ask:",
          "4. How accurate Taylor polynomials generated by y=(x) atr, to approximate y=f(x) at values of other",
          "HIGHER ORDER DERIVATIVES AND APPLICATIONS If more and more terms are used in the Taylor polynomial, then this will produce a better and better",
          "To answer these questions, we introduce the Taylor series. As more and more terms are included in the",
          "Taylor polynomial, we obtain an infinite series, known as a Taylor series:",
          "For some Taylor series, the value of the series equals the value of the function for every value of x. That is, the Taylor series approximations of e, sin and cos.xequal the values of e. sin x and cosx for every value of However, some functions have a Taylor series which equals the function only for a limited range of x values. For example, the value of a function f(x)=- which equals its Taylor series only when −1<x<1.",
          "A special case of a Taylor series occurs, when the function = f(x) is known only at the origin x=0. This special condition imposed on Taylor series, develops the Maclaurin's series:",
          "The Taylor and Maclaurin's series of y= f(x) about a particular point x, are of course:",
          "If we use x-x,=, then equations (ii) and (iii) take the popular notation for the Taylor and Maclaurin's series of order n",
          "The graphical view of a function y= f(x) atxx, is shown",
          "The popular notation for the Taylor & Maclaurin's series of order a are:",
          "If a function y= f(x) is known at a particular point x 0, then the Taylor series (iv) at forward or backward point x=x,+ of a function = f(x) are:",
          "Now, look at the following examples the procedure to the use of Taylor and Maclaurin's Theorem is illustrated in these examples.",
          "Eample 9 Use Taylor's series to approximate the value of a function f(x)='at a point.x1 = 2.",
          "Solution The function and its derivatives at x=2",
          "D. Maclaurin's theorem for the functions of the typeƒ (x) = u"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-9",
        "num": "10",
        "title": "Example 10",
        "problem": "Use Maclaurin's series to approximate the value of a function f(x)= a'at a point x,",
        "given": "",
        "method": "",
        "steps": [
          "are used in Maclaurin series (iii) to obtain the Maclaurin series approximation of a' at a point.x, =0:",
          "Maclaurin's theorem for the functions of the type"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-10",
        "num": "11",
        "title": "Example 11",
        "problem": "Use Maclaurin's series to approximate the value of a function f(x)=e at a point x,=0.",
        "given": "",
        "method": "",
        "steps": [
          "are used in Maclaurin series (iii) to obtain the Maclaurin's series approximation of e' at a point x,",
          "Maclaurin's theorem for the function of the type fi.x)= sin(z) Example 12 Use Maclaurin's series to approximate the value of a function f(x) sin (x) at a point x=0.",
          "are used in Maclaurin series (iii) to obtain the Maclaurin series approximation of sin x at a point x,= 0):",
          "Mach therefore function of the type/(x)=cos(x)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-11",
        "num": "13",
        "title": "Example 13",
        "problem": "Use Maclaurin's series to approximate the value of a function f(x)= cos x at a point x=0",
        "given": "",
        "method": "",
        "steps": [
          "are used in Maclaurin series (ii) to obtain the Maclaurin series approximation of a function costat point.x=0: cosx=/(0)+x/\" (0) + ƒ* (0) /* (0) +--",
          "inclurin's theorem for the function of the type f(x)=tan(x)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-12",
        "num": "14",
        "title": "Example 14",
        "problem": "Use Maclaurin's series to approximate the value of a function f(x)= tanx at a point x,",
        "given": "",
        "method": "",
        "steps": [
          "are used in Maclaurin's (iii) to obtain the Maclaurin's series approximation of a function tanx at a point",
          "Macherin's thebrem fir the funciton of the type fod",
          "15 Use Maclaurin's series to approximate the value of a function f(x)=log,(1+x) at a point",
          "Solution The function and its derivatives atx, = 0",
          "are used in Maclaurin's series (i) to obtain the Maclaurin's series approximation of a function",
          "Maclaurin's theorem for the function of the type xd=h/1+x}"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-13",
        "num": "16",
        "title": "Example 16",
        "problem": "Use Maclaurin's series to approximate the value of a function f(x)= In(1+x) at a point",
        "given": "",
        "method": "",
        "steps": [
          "are used in Maclaurin's series (ii) to obtain the Maclaurin's series approximation of In(1+x) at a",
          "Use Taylor's theorem to compute the series of the following functions at x=3",
          "422 MAPLE command \"Taylor\" to find Taylor's expansion for a given function",
          "The use of MAPLE command \"Taylor is illustrated in the following example."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-14",
        "num": "17",
        "title": "Example 17",
        "problem": "Use Maple command taylor for the function",
        "given": "",
        "method": "",
        "steps": [
          "by Taylor's series expansion to first 5 terms.",
          "This result is obtained through right click on the last end of the expression by selecting \"Series <x\" on",
          "The normal line (ii) on the given curve at a particular point P(2, 4) is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-15",
        "num": "19",
        "title": "Example 19",
        "problem": "Find the equations of the tangent and normal lines on the curve -9- at a point, whos y crosses the x-axis.",
        "given": "",
        "method": "",
        "steps": [
          "Put y-0 in y=9- to obtain a set of points: 0=y=9-xx2-9⇒x=±3⇒(3,0), (-3.0) If the given curve is y=9-x, then, the slope of the tangent line is the first derivative of the given curve at a particular point P(13,0):",
          "The tangent lines (i) on the given curve at the particular points are:",
          "The normal lines (ii) on the given curve at the particular points are:",
          "4.3.3 Angle of intersection of the two curves",
          "P(xo-y, Jis (y-3)= mix −x). ii. The normal equation at a point",
          "If my is the slope of the first curve and my is the slope of the second curve, then the angle of intersection in between these two curves at a point of intersection is the angle in between their tangents at that point. This angle takes the notation:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-16",
        "num": "20",
        "title": "Example 20",
        "problem": "Find the angle of intersection in between the curves y=x-2x+1 and y=x+1 at the point of intersection (2,5).",
        "given": "",
        "method": "",
        "steps": [
          "For point of intersection, solve the system of nonlinear equations for the unknowns x and y.",
          "Using first equation of the nonlinear system (ii) in second equation to obtain:",
          "The set of x values is used in first equation of the nonlinear system (ii) to obtain a set of y value Put x=0 to obtain y=x-2x+1=1",
          "Put x=2 to obtain y=x-2x+1-8-4+1-5 This process developed a set of points of intersection: (0,1), (−1,2), (2,5).",
          "The slope of the first curve at a point (2, 5) is: -3x-2=>",
          "The slope of the second curve at a point (2,5) is: -2x=",
          "The slopes m, and m, are used in (i) to obtain the angle of intersection in between the given two curves.",
          "Point on a curve where the tangent is parallel to the given line",
          "Look at the following example the procedure to find the point on a curve where tangent is parallel t the given line is illustrated in this example.",
          "Find all the points on the curve y=2x+4x2 where tangent line is parallel to the lim",
          "In each case, find the equation of the tangent line to the curve at the indicated value of x a j=√/x+1, x=3",
          "In each case, find the equation of normal to the curve at the indicated value of x: a. y=xeʻ. x-l",
          "a. Find an equation of the tangent line to the curvex+y=13 at (-2, 3).",
          "Find an equation of the tangent line to the curve sin(x-3)=xy at (0,m).",
          "e. Find an equation of the normal line to the curve x+2yyat (1,-1).",
          "d. Find an equation of the normal line to the curve x-2=-3x-1 at (1, 2). a. Show that the first four terms in the Taylor series expansion of f(x)-tan x",
          "b. Show that the first four terms in the Taylor series expansion of f(x)=√x",
          "Show that the first four terms in the Taylor series expansion of",
          "Find the Maclaurin series expansion for the following functions:",
          "a. Use the Maclaurin series for e\" to show that the sum of the infinite series 1++++...",
          "b. Use part (a) to find out the value of e that must be accurate to 4 decimal places. Find the angle of intersection between the following curves:",
          "Find the points on the curve y=5x-4x where tangent line is parallel to the line y=5x-3.",
          "B.Taylor was a British mathematician who is known by his invention of Taylor's theorem and the Taylor's series. In 1708 he obtained the solution of the problem of the \"centre of oscillation\" and published on 1714. Calculus of finite differences add to the branch of higher mathematics in 1715 with the name \"Methodus Incrementorum Directa et Inversa\". This word contain the well known layrange realized its importance and termed it as the main foundation of differential calculus.",
          "Always the maximum and minimum values of a function can be read from its graphical view. For a quadratic function (whose graph is parabola), the maximum or minimum values can be determined without graphing by finding the vertex algebraically. For functions whose graphs are not known, other techniques are needed. In this unit, we shall see how to use derivatives to determine the maximum and minimum values of a function as well as the intervals where the function is increasing or decreasing. 4.4.1 Increasing and decreasing functions",
          "Suppose an ecologist has determined the size of a population of a certain species as a function () of time t (months). If it turns out that the population is increasing until the end of the first year and decreasing thereafter. It is reasonable to expect the population to be maximized at time 1-12 and for the population curve to have a high point",
          "If the graph of a function (r), such as this population curve, is rising throughout the interval 0 << 12, then we say that (r) is strictly increasing on that interval. Similarly, the graph of the function in Figure 4.3 is strictly decreasing on the interval 12 <1<20 These terms are defined more formally in the Figure 4.4.",
          "The function f(x) is strictly increasing on an interval (a, b), if",
          "f(x) < f(x), whenever xx, for x, and x, on (a, b). The function () is strictly decreasing on an interval (a, b), if f(x) > f(x), whenever x < x, for x, and 1,on (a, b)."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-17",
        "num": "22",
        "title": "Example 22",
        "problem": "Find the intervals at which the function f(x)=x is increasing or decreasing.",
        "given": "",
        "method": "",
        "steps": [
          "If x,,x,€ (0,∞) with condition x,>x,, then the function f(x) is increasing in the interval (0,0):",
          "f(x)>f(x), both (x-x)and (x+x)ane+ve, when x2 > Xj",
          "Ifx,,, (0,0) with condition x,>x,, then the function f(x) is decreasing in the interval (-0,0)-",
          "ƒ(xg)<ƒ(x,), (x,−x,) is +ve while (x,+x,) is – ve, when x2 > X,",
          "4.4.2 Prove that if f(x) is a differentiable function on the open interval (a, b) then",
          "(c) is increasing on (a, b) if (c) is decreasing on (a, b) if",
          "x, x, then there exist a point c between x, and x, such that",
          "If a function is continuous on ja, hj Trenciable on (a, b) then there",
          "Similarly, the proof of part (ii) can be done which is left as an exercise for the reader."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-18",
        "num": "23",
        "title": "Example 23",
        "problem": "Determine the values of x at which the function f(x)=x+2x-3 is increasing or decreasing. Also find the point at which the given function is neither increasing nor decreasing.",
        "given": "",
        "method": "",
        "steps": [
          "is compared with the general equation of parabola f(x)=a[x-h)+k to obtain a parabola with vertex (-1,-4) that opens upward (a =lis positive). The graph of a parabola through the points (-4.5) and (2,5) is shown in the Figure 4.5.",
          "The derivative of a given function with respect to x is the",
          "If the slope of parabola is f(x) > 0 (positive), then it gives",
          "This shows that the given function (r) is increasing in the interval",
          "If the slope of parabola is \"(x) <0 (negative), then it gives",
          "This shows that the given function f(x) is decreasing in the interval (-0,−1).",
          "If the slope of parabola is '(x)=0(zero), then it gives",
          "This shows that the given function f(x) is neither increasing nor decreasing at a vertex (-1,-4). 4.4.3 Examination of a given function for extreme values",
          "Typically the extrema of a continuous function occur either at endpoints of the interval or at points where the graph has a \"peak\" or a \"valley\" (points where the graph is higher or lower than all nearby points). For example, the function (r) in Figure 4.6 has \"peaks\" at B and D and \"valleys\" at C and E. Peaks and valleys are what we call the relative extrema.",
          "The exact location of a relative maximum or minimum rather than a graphic's approximation can normally be found by using derivatives. The concept developed is as under:",
          "Let f(x) be a function as a roller coaster track with a roller coaster car moving from left to right along the graph in the Figure 4.6. As the car moves up towards a peak, its floor tilts upward. At the",
          "instant the car reaches the peak, its floor is level, but then it begins to tilt downward as the car down toward a valley. At any point along the graph, the floor of the car (a straight-line segment figure) represents the tangent line to the graph at that point. Using this analogy, we see that as the car through the peaks and valleys at A, B, C, the tangent line is horizontal and has slope 0. At peak D and E, however, a real roller coaster car would have trouble. It would fly off the track at peak D and be un make the 90' change of direction at valley E. There is no tangent line at D or E, because of the sharp con Thus, the points where a peak or a valley occurs have this property: the tangent line is horiz and has slope ( there or no tangent line is defined there. The slope of the tangent line to the function f(x) at a point P(x, f(x)) is the value of the derivative/\"(x)-",
          "A. Relative Maximum and Relative Minimum: The function f(x) is said to have a rela maximum at a number e if(c)2/(x) for all x in an open interval containing c. Also, f(x said to have a relative minimum at a number d if (d)/(x) for all x in an open inte containing d. In general, the relative maxima and relative minima are called relative extrema. B. Critical Values and Critical Point: Suppose f(x) is defined at a number e and either ƒ\"(c) or f'(c) does not exist. Then the number e is called a critical value of f(x) and the p P(c. /(c)) on the graph of f(x) is called a critical point.",
          "Note that if (c) is not defined, then c cannot be a critical value. If there is a relative maxim at c, then the functional value (c) at that point is the maximum value. Similarly, if there is a rela minimum at e, then the functional value (c) at that point is the minimum value."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-19",
        "num": "24",
        "title": "Example 24",
        "problem": "Find the critical values for the following functions:",
        "given": "",
        "method": "",
        "steps": [
          "√(x) = 12x2 - 10x-8 is defined for all values of x. Set /(x)=0 to obtain the critical values:",
          "The first derivative of the given function is: (x)=(x-4)",
          "The derivative is not defined at x=2, also the original function f(x) is not defined",
          "at x=2. Sox-2 is not a critical value. Set (x)=0 to obtain the other critical values:",
          "The first derivative of the given function is: f'(x)=6x-3x2",
          "The derivative is not defined at x= 0, but the original function f(x) at x = 0 is f(0)=12(0)-2(0)-0 defined. So x = 0 is a critical value. For other critical values, set",
          "The derivative of a given function is: f(x)=3x-12x",
          "The derivative fails to exist when = 0, but the original function (x) is defined when x=0. So x=0 is a critical value of f(x).",
          "Ifx 0, then ƒ(x) is going to be 0 only, when the numerator 4x-4=0 is zero for x=1. So.x-1 is also the critical value of f(x). Thus, the critical values of f(x) are 0 and 1.",
          "The derivative fails to exist when x = 0, but the original function f(x) is defined when x = 0. So x-0 is a critical value of f(x). Ifx 0, then f(x) is going to be 0 only when the numerator 4-4x=0 is zero for x = 1.Sox = 1 is the critical value of f(x). Thus, the critical values of f(x) are 0 and 1. Theorem 4.1: If a continuous function (x) has a relative extremum at e, then e must be a critical value of f(x)."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-20",
        "num": "25",
        "title": "Example 25",
        "problem": "The function f(x) is defined by f(x)=x-3x-9x+1. Determine the intervals at which the function f(x) is strictly increasing or decreasing",
        "given": "",
        "method": "",
        "steps": [
          "Thus, the function f(x) increases in the intervals for x < -1 and x>3, but decreases in the"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-21",
        "num": "26",
        "title": "Example 26",
        "problem": "Draw the function f(x)-x-3x-9x+1 and its derivative (x)=3x-6x-9. Use these graphs to tell about the following questions:",
        "given": "",
        "method": "",
        "steps": [
          "(b). When the graph of f(x) is decreasing, what does that mean in",
          "These graphs develop the idea that the critical values of",
          "f(x) are always intercepts for the graph of '(x)=3x2-6x-9:",
          "■ If(x) is positive, then f(x) is increasing. If(x) is negative, then f(x) is decreasing.",
          "4.4.4 State the second derivatives rule to find the extreme values of a function at a p",
          "The first derivative of a function can be used to determine whether the function is increa decreasing on a given interval. We shall use this information to develop a procedure called th derivative test for classifying a given point as a relative maximum, a relative minimum, or neither",
          "The steps involved in first-derivative test for relative extrema are the following:",
          "1. Find all critical values of f(x). That is, find all numbers e such that f(c) is defined and",
          "The point (c. (c)) is a relative maximum if ƒ\"'(x)>0 (rising) for all x in an open interval ( the left of c, and (x) <0 (falling) for all x in an open interval (c. b) to the right of c The point (c. /(c)) is a relative minimum if (x) <0 (falling) for all x in an en interval( the left of c, and \"(x)>0 (rising) for all in an open interval (c, b) to the right of c The point (c, (c)) is not an extremum if the derivative f(x) has the same sign in open in (a, c) and (c, b) on both sides of c.",
          "In light of first-derivative test, the function f(x)=x-3x2-9x+1 (example 2-4) has the values-1 and 3. The function f(x) is increasing when <-1 and x > 3 and decreasing when −1 The first derivative test tells us that there is a relative maximum of 6 at x=-1 and a relative minim -26 at x=3."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-22",
        "num": "27",
        "title": "Example 27",
        "problem": "Examine the function f(x)=2x+3x-12x-5 for the relative extrema using first-den",
        "given": "",
        "method": "",
        "steps": [
          "values -3,0 and 2. Many other choices of the test values are",
          "also possible, but we try to select numbers that will make the computations easy. This is shown",
          "The test values -3 and 0 are used for the critical value x-2 to obtain:",
          "The value of the derivative is positive (rising) to the left of -2 and negative (falling) to the right of -2. Thus, x=-2 leads a relative maximum point",
          "The test values 0 and 2 are used for the critical value x=1 to obtain:",
          "The value of the derivative is negative (falling) to the left of 1 and positive (rising) to the right of 6. Thus, x = 1 leads a relative minimum point. ƒ(1)=2(1)+3(1)-12(1)-5=-12 Thus, the arrow pattern in the figure suggests that the graph of f(x) has a relative maximum at (-2, 15) and a relative minimum at (1,–12). The Second Derative Rule: It is often possible to classify a critical point P(c, ƒ (c)) on the graph of f(x) by examining the sign of \"(c). Specifically, if (c)=0 and (c)>0, then there is a horizontal tangent line at P and the graph of (x) is concave up in the neighborhood of P. This means that the graph of f(x) is cupped upward from the horizontal tangent at P and to expect P to be a relative minimum, as shown in Figure 4.11.",
          "Similarly, we expect P to be a relative maximum, if/\"(c)=0 and (c) <0, because the graph is cupped down beneath the critical point P, as shown in Figure 4.12.",
          "The point Pc, f(c)) is said to be a relative maximum, if the slope (c) of the tangent line from left to right along a curve through P, is decreasing from positive to zero to negative and the second derivative (c) is negative.",
          "The point P(c, (c)) is said to be relative minimum, if the slope/\"(e) of the tangent line from left to right along a curve through P. is increasing from negative to zero to positive and the second- derivative\"(c) is positive. These observations lead to the second-derivative test for relative extreme.",
          "The Second Derivative Rule for Relative Extrema: Let /(x) be a function such that (c) and the second derivative exists on an open interval (a, b) containing c.",
          "1. Ifƒ\"(c)> 0, then there is a relative minimum atxe and the graph of f(x) is concave up in the neighborhood of P(<./{c}}",
          "2. If(c)<0, then there is a relative maximum at x=e and the graph of (x) is concave down in the neighborhood of Pcf{c}}",
          "3. If (c)= 0, then the second derivative test fails and gives no information."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-23",
        "num": "28",
        "title": "Example 28",
        "problem": "Use the second-derivative test to determine whether each critical value of the fu f(x)=3x-5x+2 corresponds to a relative maximum, a relative minimum, or neither. Solution The first and second derivatives of f(x) are the following:",
        "given": "",
        "method": "",
        "steps": [
          "4.4.6 Solve real-life problems related to extreme values"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-4-24",
        "num": "29",
        "title": "Example 29",
        "problem": "A truck burns fuel at the rate of G(x)=",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-4-1",
        "exercise": "Exercise 4.2",
        "title": "Exercise 4.2",
        "description": "",
        "problems": [
          {
            "id": "ex-4-2-q1",
            "qNo": "1",
            "question": "Find the tangent line at the stated x-value: (a) y=√(x+1), x=3; (b) y=sin(2x+π), x=0; (c) y=x²e^x, x=1; (d) y=x/(x²+1), x=1.",
            "solution": "Use y−f(a)=f'(a)(x−a). (a) f(3)=2 and f'(3)=1/4, so y−2=(x−3)/4. (b) f(0)=0 and f'(0)=2cosπ=−2, so y=−2x. (c) f(1)=e and f'(x)=e^x(x²+2x), hence f'(1)=3e; tangent: y−e=3e(x−1). (d) f(1)=1/2 and f'(x)=(1−x²)/(x²+1)², so f'(1)=0; tangent y=1/2.",
            "diagram": null
          },
          {
            "id": "ex-4-2-q2",
            "qNo": "2",
            "question": "Find the normal line at the stated x-value: (a) y=xe^x, x=1; (b) y=(2x+1)^4, x=0; (c) y=cos(x−π), x=π/2.",
            "solution": "The normal slope is the negative reciprocal of the tangent slope. (a) f(1)=e, f'(1)=2e, so the normal slope is −1/(2e): y−e=−(x−1)/(2e). (b) f(0)=1, f'(0)=8, so y−1=−x/8. (c) f(π/2)=0 and f'(x)=−sin(x−π), giving f'(π/2)=1; the normal slope is −1, so y=−(x−π/2).",
            "diagram": null
          },
          {
            "id": "ex-4-2-q3",
            "qNo": "3",
            "question": "Find the indicated tangent or normal equations: (a) tangent to x²+y²=13 at (−2,3); (b) tangent to sin(x−y)=xy at (0,π); (c) normal to x²+2xy=y³ at (1,−1).",
            "solution": "(a) Implicit differentiation gives 2x+2y y'=0, so y'=−x/y. At (−2,3), slope=2/3, hence y−3=(2/3)(x+2). (b) Differentiate: cos(x−y)(1−y')=y+xy'. At (0,π), cos(−π)=−1, so −1+y'=π; hence y'=π+1 and the tangent is y−π=(π+1)x. (c) Differentiate 2x+2(y+xy')=3y²y'; solving at (1,−1) gives y'=0, so the tangent is horizontal and the normal is x=1.",
            "diagram": null
          },
          {
            "id": "ex-4-2-q4",
            "qNo": "4",
            "question": "Write the first four nonzero Taylor terms: (a) cos x about x=π/4; (b) √x about x=4; (c) x+e^x about x=1.",
            "solution": "Use f(a)+f'(a)(x−a)+f''(a)(x−a)²/2!+f'''(a)(x−a)³/3!. (a) cos(π/4)−sin(π/4)(x−π/4)−cos(π/4)(x−π/4)²/2!+sin(π/4)(x−π/4)³/3! = (√2/2)[1−(x−π/4)−(x−π/4)²/2+(x−π/4)³/6]. (b) 2+(x−4)/4−(x−4)²/64+(x−4)³/512. (c) 1+e + (1+e)(x−1)+e(x−1)²/2!+e(x−1)³/3! + …; the constant term is f(1)=1+e.",
            "diagram": null
          },
          {
            "id": "ex-4-2-q5",
            "qNo": "5",
            "question": "Find the Maclaurin expansions: (a) 1/(1+x); (b) sin²x; (c) cosh x; (d) ln(1−4x).",
            "solution": "Use standard power series. (a) 1−x+x²−x³+x⁴−… for |x|<1. (b) (1−cos 2x)/2=x²−x⁴/3+2x⁶/45−…. (c) 1+x²/2!+x⁴/4!+x⁶/6!+…. (d) −∑_{n=1}∞(4x)^n/n=−4x−8x²−(64/3)x³−64x⁴−… for |x|<1/4.",
            "diagram": null
          },
          {
            "id": "ex-4-2-q6",
            "qNo": "6",
            "question": "Use the series for e^x to show e=1+1+1/2!+1/3!+… and approximate e to four decimal places.",
            "solution": "The Maclaurin series e^x=∑_{n=0}∞x^n/n!. Setting x=1 gives e=∑_{n=0}∞1/n!. Summing terms through n=9 gives 2.7182815…, and the remaining positive tail is less than 0.000003, so e≈2.7183 to four decimal places.",
            "diagram": null
          },
          {
            "id": "ex-4-2-q7",
            "qNo": "7",
            "question": "Find the intersection angle of the curve pairs shown in the printed exercise.",
            "solution": "At an intersection, find both tangent slopes by implicit differentiation. If the slopes are m₁ and m₂, the angle θ between the curves satisfies tan θ=|(m₂−m₁)/(1+m₁m₂)|. Substitute the intersection coordinates for each pair and take the acute angle. The scan’s second pair equation is not legible enough here to state a verified numerical angle.",
            "diagram": null
          },
          {
            "id": "ex-4-2-q8",
            "qNo": "8",
            "question": "Find the point(s) on y=5x³−4x² where the tangent is parallel to y=5x−3.",
            "solution": "The given line has slope 5. Differentiate the curve: y'=15x²−8x. Set 15x²−8x=5, so 15x²−8x−5=0. Thus x=(4±√91)/15. Substitute each x into y=5x³−4x² to obtain the corresponding points.",
            "diagram": null
          }
        ],
        "pageStart": 101,
        "pageEnd": 129
      },
      {
        "id": "ex-4-2",
        "exercise": "Exercise 4.3",
        "title": "Exercise 4.3",
        "description": "",
        "problems": [
          {
            "id": "ex-4-3-q1",
            "qNo": "1",
            "question": "Find critical values and intervals of increase/decrease: (a) f(x)=x³+3x²+1; (b) f(x)=x⁴+35x²−125x−9.375.",
            "solution": "(a) f'=3x²+6x=3x(x+2). Critical numbers: −2,0. The derivative is positive on (−∞,−2) and (0,∞), negative on (−2,0); hence f increases on the first and third intervals and decreases on the middle interval. (b) f'=4x³+70x−125. Since f''=12x²+70>0, f' is strictly increasing and has one real zero, approximately x≈1.566. Thus f decreases before this critical number and increases after it.",
            "diagram": null
          },
          {
            "id": "ex-4-3-q2",
            "qNo": "2",
            "question": "Find the critical values: (a) f(x)=2x³−3x²−72x+15; (b) f(x)=x³/3−x²−15x+6.",
            "solution": "(a) f'=6x²−6x−72=6(x−4)(x+3); critical numbers are x=−3 and x=4. (b) f'=x²−2x−15=(x−5)(x+3); critical numbers are x=−3 and x=5.",
            "diagram": null
          },
          {
            "id": "ex-4-3-q9",
            "qNo": "9",
            "question": "The concentration model is K(x)=4x/(3x²+27), for x>0 hours. Find where it increases/decreases and when its maximum occurs.",
            "solution": "K'(x)=4(27−3x²)/(3x²+27)²=12(9−x²)/(3x²+27)². For x>0 the denominator is positive; K'>0 on (0,3), K'<0 on (3,∞). Therefore the concentration reaches its maximum at x=3 hours, with K(3)=12/54=2/9.",
            "diagram": null
          },
          {
            "id": "ex-4-3-q10",
            "qNo": "10",
            "question": "A generator uses fuel at G(x)=1/48(300/x+2x) gallons per hour after x kilowatt-hours. Fuel costs $2.25 per gallon. Find x that minimizes fuel cost for 32 operating hours and the minimum cost.",
            "solution": "Total fuel cost is C(x)=32·2.25·G(x)=450/x+3x, x>0. Then C'(x)=−450/x²+3. Set C'=0: x²=150, so x=√150≈12.247 (positive domain). Since C''(x)=900/x³>0, this is a minimum. C_min=450/√150+3√150=6√150≈$73.48.",
            "diagram": null
          }
        ],
        "pageStart": 101,
        "pageEnd": 129
      },
      {
        "id": "ex-4-3",
        "exercise": "Review Exercise 4",
        "title": "Review Exercise 4",
        "description": "",
        "problems": [],
        "pageStart": 101,
        "pageEnd": 129
      },
      {
        "id": "ex-4-4",
        "exercise": "Exercise 4.1",
        "title": "Exercise 4.1",
        "description": "",
        "problems": [
          {
            "id": "ex-4-1-q1",
            "qNo": "1",
            "question": "Find the second derivative: (a) y=x³−4x²+5x+2; (b) y=x²+3x−1; (c) y=sin x; (d) y=e^x.",
            "solution": "Differentiate twice. (a) y'=3x²−8x+5, y''=6x−8. (b) y'=2x+3, y''=2. (c) y'=cos x, y''=−sin x. (d) y'=e^x, y''=e^x.",
            "diagram": null
          },
          {
            "id": "ex-4-1-q2",
            "qNo": "2",
            "question": "Find d²y/dx² for the parametric curve x=1+t², y=t³+2t²+1.",
            "solution": "dx/dt=2t, dy/dt=3t²+4t, so dy/dx=(3t+4)/2. Then d²y/dx²=[d/dt((3t+4)/2)]/(dx/dt)=3/(4t).",
            "diagram": null
          },
          {
            "id": "ex-4-1-q3",
            "qNo": "3",
            "question": "Find y'' for: (a) y=tan^{−1}x; (b) y=ln(x²+1).",
            "solution": "(a) y'=1/(1+x²), hence y''=−2x/(1+x²)². (b) y'=2x/(x²+1), hence y''=2(1−x²)/(x²+1)².",
            "diagram": null
          },
          {
            "id": "ex-4-1-q4",
            "qNo": "4",
            "question": "Show that y=1/x satisfies xy'+y=0, then verify the relation by differentiation.",
            "solution": "For y=x^{−1}, y'=−x^{−2}. Therefore xy'+y=x(−x^{−2})+x^{−1}=−x^{−1}+x^{−1}=0, for x≠0.",
            "diagram": null
          }
        ],
        "pageStart": 101,
        "pageEnd": 129
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-5",
    "number": 5,
    "title": "Differentiation of Vector Functions",
    "titleUrdu": "",
    "pageRange": "Printed pages 130–141",
    "pageStart": 130,
    "pageEnd": 141,
    "sections": [
      {
        "id": "sec-5-1",
        "title": "5.1 Scalar and Vector Functions",
        "theory": "ii. Explain domain and range of a vector function.\n\nDefine limit of a vector function and employ the usual technique for algebra of limits of scalar function to demonstrate the following properties of limits of a vector function.\n\nThe limit of the sum (difference) of two vector functions is the sum (difference) of their limits.\n\nThe limit of the dot product of two vector functions is the dot product of their limits.\n\nThe limit of the cross product of two vector functions is the cross product of their limits.\n\nThe limit of the product of a scalar function and a vector function is the product of their limits.\n\nDefine continuity of a vector function and demonstrate through examples.\n\nDefine derivative of a vector function of a single variable and elaborate the result:\n\n¡£/00 = {{0/+J90] +600, where in 600, 50) are differentiable functions of a scalar variable t, then\n\nProve the following formulae of differentiation:\n\nwhere a is a constant vector function, fand g are vector functions, and is a scalar function of r. Apply vector differentiation to calculate velocity and acceleration of a position vector in = x[n]/+3{/}}=={0}A\n\nIn the same way that we studied numerical calculus after we learned numerical arithmetic. We can now study vectors calculus. Since we already studied vector arithmetic in unit-3 of grade-xi Mathematics. Quite simply, we might have a vector quantity that varies with respect to another variable, either a scalar or a vector. In this unit we shall study the vector functions and the applications of the differential calculus. We shall extend the basic concepts of calculus in a simple and natural way. The study of vector calculus makes the more useful in the geometrical, physical and engineering applications.\n\nThe relationship of calculus and vector methods forms what is called vector calculus. The key to use vector calculus is the concept of a vector function.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-5-2",
        "title": "5.2 Limit and Continuity",
        "theory": "For the most part, vector limits behave like scalar limits. The proper definition of the limit of a vector function is given below.\n\nLimit of a vector function and properties of limits of a vectors function\n\n\"Let a vector function F(r) be defined for all values of t in some neighbourhood about a point to except possibly at itself and let Z be a constant vector called limit vector. The function F(r)is said to approach the limit vector Z as \" approaches \"if for any given real number >0 such that\n\nF(-4e whenever 02-28 symbolically, it is written as lim F(t) = Z\n\nNow look at the following useful properties of vector valued functions.\n\nThe limit of the sum (difference of two vector functions is the sum (difference) of their limits. If lim F(r)-Z and lim G(t)= M, where Land M are constant vector functions then:\n\nThe limit of the dot product of two vector functions is the dot product of their limits.\n\nIf lim F(t)=Z and lim G(t)=M, where Z and M are constant vector functions then:\n\nThe limit of the cross product of two vector functions is the cross product of their limits. If lim F(1) = Z and limG(r)=M, where Zand M are constant vector functions then:\n\nThe limit of the product of a scalar function and a vector function is the product of their limi If lim F(1) = Z and lim/)ere is a constant vector and is a scalar constant then\n\n3 Find lim(), when the vector function is F()=(-3)+7+ sin ark.\n\nA vector function Fir) as he continuous at 1-1, if\n\n, is in the domain of a veter function F(r) lim F(r) = F()\n\nA continuous vector value fun is also continuous at every poin its domain.\n\nhops, 4 For what values oft is the sector function F()-(sint,(1-1)) continuous?\n\nSolution The components of a vector function are: ()=sinf, 0)=(-1), TeR\n\nThe function () is continuous for all t; (f) is continuous where-1-0-(1). This, F continuous, when t is a real number other than 1.\n\nPimple 5 For what values of t is F(r)=(sinz, (1-1), In r) continuous?\n\nSolution The components of a vector function are:\n\nThe function (/) is continuous for all t; (r) is continuous where 1-0 (that is, where 1). / is continuous for? >0. Thus, F (f) is continuous function whenever t is any positive number other that That is 10, 11.\n\nJ. Willard Gibbs was an American scientist. He made his great contributions in the field of mathematics, physics and chemistry. He was the first American who obtained his doctorate degree in engineering after spending three years in Europe, he joined Yale university as professor of mathematical physics from 1871 to his death. He earned international reputation while working in relative isolation. A great scientist Albert Einstein praised him as \"the greatest mind in American history\". Together with Oliver Heaviside (Britain and American national) Gibbs developed vector analysis to express the new laws of electromagnetism.\n\nfor these values of t at which the limit exists, we can also use the Leibniz notation\n\nF(), and [F] The following theorem establishes a convenient method for computing the den\n\nTheorem-1: The vector function F()=(()«ƒ£0.ƒ‚0)= ƒ}{0}i+ƒ;(1)j+ƒ(1)k is different a point i=1, whenever the component functions f().f(t),f,(t) of F(r) are all differential point t=1: i.c. F(1)=(©£«£©)= £î+£;}+f@k",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-5-3",
        "title": "5.3 Differentiation of Vector Functions",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-5-4",
        "title": "5.4 Vector Differentiation",
        "theory": "Several rules for computing derivatives of vector functions are\n\nlisted below, which can be proved by applying rules for limits of vector A vector Falso written functions to appropriate theorems for scalar derivatives.\n\nWhere, a is a constant vector function, ƒ and g are vector functions and is a scalar function off.\n\nProof: i. Let a be a constant vector function then (a)(a,i+a,j+a, k) == ai + 2 a) + — ak\n\n(Q(e + Ar) fƒ (e + de) − q(e + di)f(t)] + Lim\n\n1 ƒ2 = (-r2¿')Ì—(→†)}+(-5) are used in the RHS to obtain\n\n= (3 — 2te' — 1aè' )Î + (3r2 )}+(e' -21) which is identical to the L.H.S. Thus, the L.H.S = R.H.S.\n\nIn the calculus of single variable the velocity is defined as the derivative of the position funct\n\nFor vector calculus we use the same definition.\n\nLet 7(0) = x(i + 2007+z(1) be a differential vector valued function representing the position ves of a particle at time \"/\" then the velocity vector is the derivative of position vector.\n\nIn the calculus of single variable, we defined the acceleration of a particle as the second derivative of the position vector. There is no change for the vector calculus.\n\n\"Let F=7(1)=x+y]+zbe a twice differentiable vector valued function, representing the position vector of a particle at time \"r. Then the acceleration vector is the second derivative of the position vector F(r)\n\nSolution Since, F(1) = (3x2 + 5)î— (4c” + 2e − 1)] + sin(z)ë\n\nIn the calculus of single variable the speed was the absolute value of the velocity. In the vector calculus the magnitude of velocity vector.\n\nLet (1) be a differentiable vector valued function representation of the position of a particle in time \"7\" the speed 's\" of\n\nthe particle is the magnitude of the velocity vector. Speed-S()-y-Pr\n\nSolution If the particle's position at a time t is, then F(1) = costi+sint}+k then, the\n\nThe velocity at a timer = 2 is (2)=-sin(2)i+cos(2)+3(4)-0.917-0.427+12k, use rad The acceleration at a time t-2 is a(2)=-cos(2)7-sin(2)+6(2) 0.427-0.917+12k The speed is [=√(sint)2+ (cost)+ (3r2)2= √1+9 At a time -2,\n\nFind the vector derivative of the following vector functions:\n\nFind the second order derivatives of the following vector valued functions.\n\nDifferentiate the following scalar functions:\n\nFind the particle's velocity, acceleration, speed and direction of motion for the indicated val when the position vector of a particle's in space at time t is (r:\n\nIf F(r)is a differentiable vector functions of t such that F(t) 0, then show that",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-5-1",
        "num": "2",
        "title": "Example 2",
        "problem": "Find the domain for the following vector functions:",
        "given": "",
        "method": "",
        "steps": [
          "The function (r) = sint is defined for all t; (f)-(1-1) is defined for all values of t except =1; (r) = It is defined for r>0. Thus, the domain of a function F(r)is 0, r1. The range in each case is of course a vector quantity.",
          "It follows from the definition of vector operations that vector functions can be added, subtracted, multiplied by a scalar function, and multiplied together e.g.",
          "If F and G are vector functions of the real variable t, and h() is any scalar function, then F+G, F-Gand FxGare vector functions, and F-G is a scalar function.",
          "For the most part, vector limits behave like scalar limits. The proper definition of the limit of a vector function is given below.",
          "Limit of a vector function and properties of limits of a vectors function",
          "\"Let a vector function F(r) be defined for all values of t in some neighbourhood about a point to except possibly at itself and let Z be a constant vector called limit vector. The function F(r)is said to approach the limit vector Z as \" approaches \"if for any given real number >0 such that",
          "F(-4e whenever 02-28 symbolically, it is written as lim F(t) = Z",
          "Now look at the following useful properties of vector valued functions.",
          "The limit of the sum (difference of two vector functions is the sum (difference) of their limits. If lim F(r)-Z and lim G(t)= M, where Land M are constant vector functions then:",
          "The limit of the dot product of two vector functions is the dot product of their limits.",
          "If lim F(t)=Z and lim G(t)=M, where Z and M are constant vector functions then:",
          "The limit of the cross product of two vector functions is the cross product of their limits. If lim F(1) = Z and limG(r)=M, where Zand M are constant vector functions then:",
          "The limit of the product of a scalar function and a vector function is the product of their limi If lim F(1) = Z and lim/)ere is a constant vector and is a scalar constant then",
          "3 Find lim(), when the vector function is F()=(-3)+7+ sin ark.",
          "A vector function Fir) as he continuous at 1-1, if",
          ", is in the domain of a veter function F(r) lim F(r) = F()",
          "A continuous vector value fun is also continuous at every poin its domain.",
          "hops, 4 For what values oft is the sector function F()-(sint,(1-1)) continuous?",
          "Solution The components of a vector function are: ()=sinf, 0)=(-1), TeR",
          "The function () is continuous for all t; (f) is continuous where-1-0-(1). This, F continuous, when t is a real number other than 1.",
          "Pimple 5 For what values of t is F(r)=(sinz, (1-1), In r) continuous?",
          "Solution The components of a vector function are:",
          "The function (/) is continuous for all t; (r) is continuous where 1-0 (that is, where 1). / is continuous for? >0. Thus, F (f) is continuous function whenever t is any positive number other that That is 10, 11.",
          "J. Willard Gibbs was an American scientist. He made his great contributions in the field of mathematics, physics and chemistry. He was the first American who obtained his doctorate degree in engineering after spending three years in Europe, he joined Yale university as professor of mathematical physics from 1871 to his death. He earned international reputation while working in relative isolation. A great scientist Albert Einstein praised him as \"the greatest mind in American history\". Together with Oliver Heaviside (Britain and American national) Gibbs developed vector analysis to express the new laws of electromagnetism.",
          "for these values of t at which the limit exists, we can also use the Leibniz notation",
          "F(), and [F] The following theorem establishes a convenient method for computing the den",
          "Theorem-1: The vector function F()=(()«ƒ£0.ƒ‚0)= ƒ}{0}i+ƒ;(1)j+ƒ(1)k is different a point i=1, whenever the component functions f().f(t),f,(t) of F(r) are all differential point t=1: i.c. F(1)=(©£«£©)= £î+£;}+f@k",
          "Proof: If a vector function F(r) is differentiable, then their component functions ()() exist, then the scalar derivatives ()() and (0) by first-principle rule",
          "In the Leibniz notation, the derivative of F(r)is denoted by:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-2",
        "num": "6",
        "title": "Example 6",
        "problem": "For what values of t is G(t)=1+ (cost)}+(-5) differentiable?",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-3",
        "num": "7",
        "title": "Example 7",
        "problem": "Find the derivative of the vector function F(t)=1+ sint }+(r2+5t)k.",
        "given": "",
        "method": "",
        "steps": [
          "Several rules for computing derivatives of vector functions are",
          "listed below, which can be proved by applying rules for limits of vector A vector Falso written functions to appropriate theorems for scalar derivatives.",
          "Where, a is a constant vector function, ƒ and g are vector functions and is a scalar function off.",
          "Proof: i. Let a be a constant vector function then (a)(a,i+a,j+a, k) == ai + 2 a) + — ak",
          "(Q(e + Ar) fƒ (e + de) − q(e + di)f(t)] + Lim"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-4",
        "num": "8",
        "title": "Example 8",
        "problem": "Let F()=1+1+1k and G(t)=1+j+3k are the vector functions. Verify the",
        "given": "",
        "method": "",
        "steps": [
          "= (3 — 2te' — 1aè' )Î + (3r2 )}+(e' -21) which is identical to the L.H.S. Thus, the L.H.S = R.H.S."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-5",
        "num": "9",
        "title": "Example 9",
        "problem": "IF(0)=1+de+rk and G(1)=31i+ej-2rk are the two vector functions and any scalar function, then evaluate the following derivatives: (a) (2F+r1G)",
        "given": "",
        "method": "",
        "steps": [
          "In the calculus of single variable the velocity is defined as the derivative of the position funct",
          "For vector calculus we use the same definition.",
          "Let 7(0) = x(i + 2007+z(1) be a differential vector valued function representing the position ves of a particle at time \"/\" then the velocity vector is the derivative of position vector."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-6",
        "num": "10",
        "title": "Example 10",
        "problem": "Find the velocity of the particle whose position vector is 7-7)=5+4j — co{r}",
        "given": "",
        "method": "",
        "steps": [
          "\"Let F=7(1)=x+y]+zbe a twice differentiable vector valued function, representing the position vector of a particle at time \"r. Then the acceleration vector is the second derivative of the position vector F(r)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-7",
        "num": "11",
        "title": "Example 11",
        "problem": "Find the acceleration of the particle whose position vector is",
        "given": "",
        "method": "",
        "steps": [
          "In the calculus of single variable the speed was the absolute value of the velocity. In the vector calculus the magnitude of velocity vector.",
          "Let (1) be a differentiable vector valued function representation of the position of a particle in time \"7\" the speed 's\" of",
          "the particle is the magnitude of the velocity vector. Speed-S()-y-Pr"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-8",
        "num": "12",
        "title": "Example 12",
        "problem": "Fin the speed of particle whose position vector is F(r)=3+47-sinin after 30 seconds. Solution Since, 7(1)-31+4)+sin(r) = P()=(F)=(317+4)-sin(r)4)",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-5-9",
        "num": "13",
        "title": "Example 13",
        "problem": "A particle's position at time' r' is determined by the vector (r) = cos(r)i+sin(1)] +13k . Find the particle's velocity, speed, direction and acceleration at a time = 2. Interpret the particle's motion:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-5-1",
        "exercise": "Exercise 5.2",
        "title": "Exercise 5.2",
        "description": "",
        "problems": [
          {
            "id": "ex-5-2-q1",
            "qNo": "1",
            "question": "Find the vector derivative: (a) F(t)=t i+t² j+(t³+t)k; (b) F(s)=(sin s+s²)i+(2s²−s)j+3k; (c) F(θ)=cosθ[i+tanθ j+3k].",
            "solution": "Differentiate components. (a) F'(t)=i+2t j+3t²k. (b) F'(s)=(cos s+2s)i+(4s−1)j. (c) Expand components: cosθ i+sinθ j+3cosθ k, hence F'(θ)=−sinθ i+cosθ j−3sinθ k.",
            "diagram": null
          },
          {
            "id": "ex-5-2-q2",
            "qNo": "2",
            "question": "Find the second vector derivatives: (a) F(t)=t²i+3t³j−8t²k; (b) F(s)=(3+s²)i−(s+1)²j+3s⁴k; (c) F(x)=ln x i−x²k; (d) F(θ)=sin²θ i−cos²θ j.",
            "solution": "Differentiate twice componentwise. (a) F''(t)=2i+18t j−16k. (b) F''(s)=2i−2j+36s²k. (c) F''(x)=−x^{−2}i−2k. (d) F'(θ)=sin(2θ)i+sin(2θ)j; F''(θ)=2cos(2θ)i+2cos(2θ)j.",
            "diagram": null
          },
          {
            "id": "ex-5-2-q3",
            "qNo": "3",
            "question": "Differentiate the scalar functions: (a) f(x)=[x i+(x+1)j]·[2x i−3x²j]; (b) g(x)=sin x i−2x j+cos x k.",
            "solution": "(a) The dot product is 2x²−3x²(x+1)=−3x³−x²+2x, so f'(x)=−9x²−2x+2. (b) Differentiate components: g'(x)=cos x i−2j−sin x k.",
            "diagram": null
          },
          {
            "id": "ex-5-2-q4",
            "qNo": "4",
            "question": "For each position vector r(t), find velocity, acceleration, speed, and direction of motion at the stated time: (a) r(t)=t i+t²j+2t k at t=1; (b) r(t)=cos t i+sin t j+3t k at t=π/4; (c) r(t)=e^t i+e^{−t}j+e^{2t}k at t=ln2.",
            "solution": "Use v=r', a=r'', speed=|v|, direction v/|v|. (a) v(1)=i+2j+2k; a=2j; speed=3; direction=(i+2j+2k)/3. (b) v=−sin t i+cos t j+3k, a=−cos t i−sin t j; at π/4 speed=√10 and direction=(−i+j+3√2 k)/(2√5). (c) At t=ln2, v=2i+1/2 j+4k; a=2i+1/4 j+8k; speed=√(81/4)=9/2; direction=(4/9)i+(1/9)j+(8/9)k.",
            "diagram": null
          },
          {
            "id": "ex-5-2-q5",
            "qNo": "5",
            "question": "If F(t) is differentiable and F(t)≠0, show d|F|/dt = [F·F']/|F|.",
            "solution": "Since |F|=(F·F)^{1/2}, differentiate by the chain rule: d|F|/dt=(1/2)(F·F)^{−1/2}·d(F·F)/dt. By the product rule for dot products, d(F·F)/dt=F'·F+F·F'=2F·F'. Therefore d|F|/dt=(F·F')/|F|.",
            "diagram": null
          }
        ],
        "pageStart": 130,
        "pageEnd": 141
      },
      {
        "id": "ex-5-2",
        "exercise": "Review Exercise 5",
        "title": "Review Exercise 5",
        "description": "",
        "problems": [],
        "pageStart": 130,
        "pageEnd": 141
      },
      {
        "id": "ex-5-3",
        "exercise": "Exercise 5.1",
        "title": "Exercise 5.1",
        "description": "",
        "problems": [],
        "pageStart": 130,
        "pageEnd": 141
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-6",
    "number": 6,
    "title": "Integration",
    "titleUrdu": "",
    "pageRange": "Printed pages 142–177",
    "pageStart": 142,
    "pageEnd": 177,
    "sections": [
      {
        "id": "sec-6-1",
        "title": "6.1 Antiderivatives",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-6-2",
        "title": "6.2 Integration by Substitution",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-6-3",
        "title": "6.3 Integration of Rational Functions",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-6-4",
        "title": "6.4 Integration by Parts",
        "theory": "Use definite integral to find out the area between the curve f(x) and the x-axis over the i interval [a, b]:\n\nSetup definite integrals in problems a to d that represent the indicated shaded areas:\n\nAn oil tanker is leaking oil at a rate given in barrels per hour by\n\nWhere t is the time in hours after the tanker hits a hidden rock (when /= 0). a. Find the total number of barrels that the ship will leak on the first day. b. Find the total number of barrels that the ship will leak on the second day. c. What is happening over the long run to the amount of oil leaked per day? Use MAPLE command \"in\" to evaluate\n\nThe process of finding antiderivative is called.\n\nF(x) is an antiderivative of f(x) if F(x) = f(x).\n\nIf F(x) = f(x), then [f(x)dx = F(x)+C, for any real number C. It is called indefinite in If f(x) and g(x) are integral functions w.r.t. x, then the integral of the product of f(x) an\n\nIf f(x) is continuous on the interval [a, b] and [a, b] is divided into n equal subintervalu right-hand points are x,,,,, then the definite integral of f(x) from x-a tox-bis\n\nThe definite integral of the product of two functions and vw.r.tx is:\n\nIf f(x) is continuous and f(x)20on the closed interval [a, b], then the area under a curve on [a, b] is given by the definite integral of f(x) on [a, b]:\n\nIf a function f(x) is continuous on the closed interval [a, b], then\n\nWhere F(x) is any function such that F(x)= f(x) for all x in",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-6-5",
        "title": "6.5 Integration Using Partial Fractions",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-6-6",
        "title": "6.6 Definite Integrals",
        "theory": "(a). Indefinite integral of a function f(x)=x+x+x+x+1 w.rt variable.x.\n\nDefinite integral of a function f(x)=w.r.t variable x.\n\nUsing Palettes: Use cursor button to select integral palette. Click-integral palette, insert the function required, then press \"ENTER\" key to obtain the integral of a given function:\n\nThe relationship between derivative and integrals as an inverse operation was noticed first time by Isaac barrow (1630-1677) in the 17° century. He was a teacher of Sir Isaac Newton. Newton and Leibniz are known as key inventor of calculus. They made the use of calculus as conjuctor, that is as a mathematical statement which is suspected to be true. But has not proven yet. The fundamental theorem of integral calculus was not officially proven in all its glory until Berhard Riemann (1826-1866) demonstrated it in the 19 century. During this 200-years a lot of mathematic like real analysis had invented before Riemann could prove that derivatives and integrals are inverse.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-6-1",
        "num": "20",
        "title": "Example 20",
        "problem": "Find the area between the x-axis and the curve (x)=-2x from x=-1 to x=3.",
        "given": "",
        "method": "",
        "steps": [
          "The sketch of the region is shown in the Figure 6.8.",
          "6.6.6 MAPLE command \"in\" to evaluate definite and indefinite integrals The use of maple common \"in\" is illustrated in the following example."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-2",
        "num": "21",
        "title": "Example 21",
        "problem": "Use MAPLE command \"int\" to solve.",
        "given": "",
        "method": "",
        "steps": [
          "Definite integral of a function f(x)=w.r.t variable x.",
          "Using Palettes: Use cursor button to select integral palette. Click-integral palette, insert the function required, then press \"ENTER\" key to obtain the integral of a given function:",
          "The relationship between derivative and integrals as an inverse operation was noticed first time by Isaac barrow (1630-1677) in the 17° century. He was a teacher of Sir Isaac Newton. Newton and Leibniz are known as key inventor of calculus. They made the use of calculus as conjuctor, that is as a mathematical statement which is suspected to be true. But has not proven yet. The fundamental theorem of integral calculus was not officially proven in all its glory until Berhard Riemann (1826-1866) demonstrated it in the 19 century. During this 200-years a lot of mathematic like real analysis had invented before Riemann could prove that derivatives and integrals are inverse.",
          "Use definite integral to find out the area between the curve f(x) and the x-axis over the i interval [a, b]:",
          "Setup definite integrals in problems a to d that represent the indicated shaded areas:",
          "An oil tanker is leaking oil at a rate given in barrels per hour by",
          "Where t is the time in hours after the tanker hits a hidden rock (when /= 0). a. Find the total number of barrels that the ship will leak on the first day. b. Find the total number of barrels that the ship will leak on the second day. c. What is happening over the long run to the amount of oil leaked per day? Use MAPLE command \"in\" to evaluate",
          "The process of finding antiderivative is called.",
          "F(x) is an antiderivative of f(x) if F(x) = f(x).",
          "If F(x) = f(x), then [f(x)dx = F(x)+C, for any real number C. It is called indefinite in If f(x) and g(x) are integral functions w.r.t. x, then the integral of the product of f(x) an",
          "If f(x) is continuous on the interval [a, b] and [a, b] is divided into n equal subintervalu right-hand points are x,,,,, then the definite integral of f(x) from x-a tox-bis",
          "The definite integral of the product of two functions and vw.r.tx is:",
          "If f(x) is continuous and f(x)20on the closed interval [a, b], then the area under a curve on [a, b] is given by the definite integral of f(x) on [a, b]:",
          "If a function f(x) is continuous on the closed interval [a, b], then",
          "Where F(x) is any function such that F(x)= f(x) for all x in",
          "Now, use trigonometric substitutions in equation (ii)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-3",
        "num": "9",
        "title": "Example 9",
        "problem": "Evaluate the integral f",
        "given": "",
        "method": "",
        "steps": [
          "In previous sections, we have learnt some of the basic techniques of integration to sol problems like xdx and [sinxdx. But, how do we evaluate an integral whose integrand is the",
          "of two functions such as fxsin xdx, fxe'dx, fx ln xdx",
          "To solve integral of the type like that, we have a technique called integration by parts.",
          "For this technique, recall the differentiation of the product of two functions f(x) and g(x) w.r.t.x.",
          "The integral of (i) with respect to x is giving",
          "The equation that can be transformed into more convenient form by substituting -(x) an v=g(x), du= f'(x)dx and dv=g'(x)dx: Judy-v-fvdu",
          "This is the standard form of the integration by parts formula."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-4",
        "num": "10",
        "title": "Example 10",
        "problem": "Evaluate the integral fxe'dx.",
        "given": "",
        "method": "",
        "steps": [
          "6.4.2 Applying method of integration by parts to evaluate integrals of the following",
          "In this problem, we choose =√a- -xand 1 to integrate the integrand of (i):",
          "6.4.3 Evaluation of integrals using integration by parts Example 11 Evaluate the integral fx In xdx."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-5",
        "num": "12",
        "title": "Example 12",
        "problem": "Evaluate the integral le'sin x dx.",
        "given": "",
        "method": "",
        "steps": [
          "It appears that we have not made any progress since we cannot evaluate the new integral. However, the form of the new integral prompts us to apply the technique a second time and see what happens.",
          "Again, the integral of the integral part of equation (ii) with substitution and",
          "Here's very helpful mnemonic for an order of priority for which factor the derivative must be passed to.",
          "Evaluate the following indefinite integrals by method of substitution:",
          "Use suitable substitutions and tables to evaluate the following indefinite integrals:",
          "Evaluate the following by using integration by parts.",
          "Archimedes was a Greek mathematician, physicist and astronomer. He was known as leading scientist in classical antiquity. His mathematical work is to modem in technique hat it is barely distinguishable from that of 17 century mathematicians. It was all done without the benefits of algebra or a convenient number system. He also developed general method for finding the areas and volumes. He used the method to find areas banded by parabolas and spirals and to find volume of cylinders, paraboloids and segments of spheres. Archimedes also gave a procedure to find approximating values of it and banded its value",
          "He also invented a method to find the square roots and proposed another method based on the Greek",
          "myriad for representing numbers as large as one followed by 80 million billion zeros. Archimedes was most proud of his discovery of a method for finding the volume of a sphere. He showed that the",
          "volume of a sphere is the volume of the cylinder. The method of mechanical theorems, which was the part of",
          "palimpsest found in the Constantinople in 1906. In that treatise Archimedes explain how he made some of his discoveries that are participating in the main idea of the integral calculus.",
          "process may be Partial fraction decomposition has great value as a tool for integration. This thought of as the \"reverse\" of adding fractional algebraic expressions, and it allows us to break rational expressions into simpler terms. Partial fraction decomposition is an algebraic procedure for expressing a reduced rational function as a sum of fractional parts. For example, the rational",
          "can be decomposed into partial fractions only if P(x) and D(x) have no common factors and if the degree of P(x) is less than the degree of D(x). If the degree of P(x) is greater than or equal to the degree of Dix). then use division to obtain a polynomial plus a proper fraction. For example, the rational function after",
          "8x-1 is our proper fraction (this is the part which requires decomposition into partial fractions).",
          "In algebra, the theory of equations tells us that any polynomial P(x) with real coefficients can be expressed as a product of linear and irreducible quadratic powers, some of which may be repeated. This fact can be used to justify the following general procedure for obtaining the partial fraction decomposition of a rational function.",
          "Let f(x)=(x) where P(x) and D(x) have no common factors and D(x) = 0.",
          "The steps involved in decomposing the rational function are the following:",
          "If the degree of P(x) is greater than or equal to the degree of D(x), use long division to express",
          "as the sum of a polynomial and a fraction () in which the degree of the remainder",
          "D(x) polynomial R(x) is less than the degree of the denominator polynomial D(x). Factorize the denominator D(x) into the product of linear and irreducible quadratic powers.",
          "as a cascading sum of partial fractions of the form",
          "P(x) D(x) Verify that the number of constants used is identical to the degree of the denominator."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-6",
        "num": "13",
        "title": "Example 13",
        "problem": "Evaluate the following integrals:",
        "given": "",
        "method": "",
        "steps": [
          "The denominator factors are the two distinct linear factors, so we can set the rational functio",
          "equal to the sum of the two partial fractions",
          "To determine the constants 4, and 4, we multiply both sides of the equation (i) by (x-2) (x + 1) to obtain:",
          "Set x-2-0-x-2 in equation (ii) to obtain: 8(2)-1=4,(2+1)+4(2-2) 15-34, 4, 5 Set x+1=0=> x=-1 in equation (ii) to obtain :",
          "Use these constants values in equation (i) to obtain:",
          "Use this decomposition instead of rational expression in the given integral to obtain:",
          "The integrand is a proper fraction, so we start by factoring the denominator",
          "The denominator factors are the three repeated linear factors, so we can set the rational function",
          "x2-6x+3 equal to the sum of the three partial fractions",
          "To determine the constants A, A, and A,, we multiply both sides of the equation (i) by (x-2)'to",
          "For constants A4, equate the coefficients of x and x on each side of equation (ii) to obtain:",
          "Solving this system of equations for the unknowns 4 and 4, to obtain A, 1 and A, Use these constants values in equation (ii) to obtain:",
          "Use this decomposition instead of rational expression in the given integral to obtain:",
          "The intergand is a proper fraction and the denominator factors are the two repeated quadratic factors, so we can set the rational function equal to the sum of the two partial fractions:",
          "To determine the constants values, the similar procedure is used to obtain = 0,4 = 2,8,3,B=1.",
          "With these substitutions, the equation (i) becomes:",
          "Now the readers are in position, how to find the complete solution of the question.",
          "Evaluate the indefinite integrals after decomposing the following rational functions into partial",
          "The rate at which the body eliminates a drug (in milliliters per hour) is given by",
          "where I is the number of hours since the drug was administered. If R(0) = 0 is the current drug elimination, how much of the drug is eliminated during the first hour after it was administered?",
          "The rate of change of the voting population of a city with respect to time (in years) is estimated",
          "where N(t) is in thousands. If N(0) is the current voting population, then how much will this An oil tanker aground on a reef is losing oil and producing an oil slick that is radiating outward",
          "where r is the radius (in feet) of the circular slick after t minutes. Find the radius of the slick after",
          "\"A definite Integral is an integral that contains start and end value, say a and b, where interval [a, b] are limits or boundaries\".",
          "Look at the following figures, Figure 6.1 is showing the indefinite integral while the Figure 6.2 is showing definite integral.",
          "Definite integrals can be calculated in a same way as we have learnt in previous section for calculation of indefinite integral, but there is slight difference, to find definite integral simply calculate indefinite integral at point a and at point b, then subtract the result."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-7",
        "num": "14",
        "title": "Example 14",
        "problem": "Evaluate r'de",
        "given": "",
        "method": "",
        "steps": [
          "To calculate the approximate area of any mountain we use integration.",
          "This limiting process is what we mean when we say the area is the definite integral of f(x) = x2 from x = 0 to x=2. It is written symbolically as",
          "We read symbol as \"the area A equals the integral from x=0 to x=2 of the function f(x) = x2.\" The number 0 is called the lower limit of integration, the number 2 is called the upper limit of integration, the function f(x)=x is called the integrand and the dr tells us that we are integrating the function f(x)=x with respect to the variable x.",
          "If f(x) is continuous on the interval [a, b] and [a, b] is divided into n equal subintervals whose right-hand points are ...... then the definite integral of f(x) from xato x=b is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-8",
        "num": "15",
        "title": "Example 15",
        "problem": "Find the actual area of the region bounded by the curve f(x)=x and the x-axis in the",
        "given": "",
        "method": "",
        "steps": [
          "In previous section, we learned that we can determine the area of a region with a defin integral. However, with the tools available to us at this time, evaluating a definite integral using summation process is rather tedious and time consuming. To provide us with a more efficient method evaluating the definite integral, we now consider a very important theorem in calculus, \"fundamental theorem of integral calculus\". This explanation will show that the definite integral be applied in a general manner and not only to the concept of area.",
          "To help provide a better understanding of the meaning of the fundamental theorem of integ calculus, let us begin with area of a region using definite integral",
          "To develop the theorem, we need to introduce a new function called the area function () function indicates the area of the region under the graph of the function from x=ɑ to x=b in the Figure",
          "The area function A(x) is the area from a to x that must be continuous and non-negative on the interval [a, b].",
          "If we increase x by Ar, then the area (x) under the curve will increase by an amount that we call Adin Figure 6.4. We can see that AA is slightly bigger than the area of the inscribed rectangle and slightly smaller than the area of the circumscribed rectangle. In Figure 6.5, the smaller rectangle is inscribed (within the curve) and the large rectangle is circumscribed.",
          "For the area of the inscribed rectangle, we take the minimum value of f(x) within the closed interval [x,x+Ar]. We call this minimum value (m).",
          "For the area of the circumscribed rectangle, we take the maximum value within the closed interval [xx+Ar]. We refer to this value as (M). Hence the minimum area is",
          "Algebraically, we can write f(m)AxSAAs f(M)Ax",
          "If we take the limit as Ar-0, then (m) and (M) approach the same point on the curve and",
          "(x). To determine a real value of (x), we must solve equation (iv)",
          "The last equation (v) tells us that if it is possible to find an antiderivative of f(x), then we can",
          "evaluate the definite integral f(x)de. This is nicely condensed in the fundamental theorem.",
          "Statement: If a function (x) is continuous on the closed interval [a,b], then the definite integral of a function f(x) in the interval [a,b] is:",
          "Proof: Here F(x) is any function such that F(x)= f(x) for all x in [a, b].",
          "It is important to recognize that the fundamental theorem of integral calculus describes a means for evaluating a definite integral. It does not provide us with a technique for finding the antiderivative. To find the antiderivative of a definite integral, we use the same techniques we used to find the antiderivative of the indefinite integral. But what happens to the constant C? This constant C drops out as illustrated below:",
          "In computations involving integrals, it is often helpful to use the seven basic properties related",
          "fundamental theorem of calculus that are listed below:",
          "Proof: By the definition of the definite integral",
          "Let F(x) = f(x), [a, b] be an interval then by the fundamental theorem of integral calculus.",
          "Hence, by (i) and (ii) f(x)dx = f(dy (proved)",
          "Proof: By using the definition of definite integrate",
          "-- Lim (x)--- f(x)de Hence, Ĵf(x)dx = -Ïƒ(x)dx",
          "By using the fundamental theorem of integral calculus.",
          "Use definition of the definite integral to show",
          "Proof: If (x) is integral on interval [-a, a] w.r.t 'x', then for a number 0 in the interval [-a, a], the definite integral of f(x) from a to a is 2 times the definite integral of f(x) from 0 to a:",
          "Extend techniques of integration using properties to calculate definite integral"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-9",
        "num": "16",
        "title": "Example 16",
        "problem": "Evaluate the following definite integrals:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-10",
        "num": "17",
        "title": "Example 17",
        "problem": "Evaluate the following definite integrals: (a).",
        "given": "",
        "method": "",
        "steps": [
          "Substitute all these in the given integral to obtain:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-11",
        "num": "18",
        "title": "Example 18",
        "problem": "Evaluate the following definite integrals: (a). [xe'dx",
        "given": "",
        "method": "",
        "steps": [
          "The integration by parts rule with substitution = e̱\" and",
          "6.6.4 Definite integral as the area under the curve",
          "f(x) is continuous and f(x)20on the closed interval [a, b], then the area under a curve (c) on the interval [a, b] is given by the definite integral of f(x) on [a, b]:",
          "The steps involved in finding the area between a curve and he x-axis are the following:",
          "The definite integral f(x)dx presents the sum of the signed",
          "areas between the graph of y = f(x) and the x-axis from xato x=b, where the area above the x-axis (peak) are counted positively and the reas below the x-axis (valley) are counted negatively. This is shown in the Figure 6.6-",
          "If f(x) is a continuous function over the interval [a, b], then the area between y = f(x) and the x-axis from x = a to x = b can be found using definite integrals as follows:",
          "If f(x) is positive for some values of x and negative for others on an interval (as in Figure 6.6), then, the area between the graph of and the x-axis can be found by (dividing the interval into subintervals over which f (x) is always positive or always negative) taking the sum of the areas of subregions over each subinterval:",
          "In Figure 6.6, A represents the area between y = f(x) and the x-axis from x = a to x = c, and B represents the area between y = f(x) and the x-axis from x = c to x = b. Both A and B are positive quantities. Since f(x)20on the interval [c, b], the area is",
          "6.6.5 Application of definite integral as the area under a curve"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-12",
        "num": "19",
        "title": "Example 19",
        "problem": "Find the area between the x-axis and the curve f(x)=x-4 from x=0 to x=4.",
        "given": "",
        "method": "",
        "steps": [
          "The sketch of the region is shown in the Figure 6.7.",
          "is not the correct area. This definite integral does not represent the area over the entire interval [0,4], but"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-13",
        "num": "20",
        "title": "Example 20",
        "problem": "Find the area between the x-axis and the curve",
        "given": "",
        "method": "",
        "steps": [
          "The sketch of the region is shown in the Figure 6.8.",
          "6.6.6 MAPLE command \"in\" to evaluate definite and indefinite integrals",
          "The use of maple common \"in\" is illustrated in the following example."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-6-14",
        "num": "21",
        "title": "Example 21",
        "problem": "Use MAPLE command \"int\" to solve.",
        "given": "",
        "method": "",
        "steps": [
          "Definite integral of a function f(x)=x w.r.t variable x.",
          "Using Palettes: Use cursor button to select integral palette. Click-integral palette, insert the function required, then press \"ENTER\" key to obtain the integral of a given function:"
        ],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-6-1",
        "exercise": "Exercise 6.4",
        "title": "Exercise 6.4",
        "description": "",
        "problems": [],
        "pageStart": 142,
        "pageEnd": 177
      },
      {
        "id": "ex-6-2",
        "exercise": "Review Exercise 6",
        "title": "Review Exercise 6",
        "description": "",
        "problems": [],
        "pageStart": 142,
        "pageEnd": 177
      },
      {
        "id": "ex-6-3",
        "exercise": "Exercise 6.2",
        "title": "Exercise 6.2",
        "description": "",
        "problems": [
          {
            "id": "ex-6-2-q1",
            "qNo": "1",
            "question": "Evaluate by substitution: (a) ∫sin⁴x cos x dx; (b) ∫√(sin²x) cos x dx; (c) ∫sin x ln(cos x)/cos x dx; (d) ∫e^x sin(e^x) dx; (e) ∫cot√x/√x dx; (f) ∫(sin x−cos x)/(sin x+cos x) dx.",
            "solution": "(a) Let u=sin x: u⁵/5+C. (b) Let u=sin x: ∫|u|du; on intervals where sin x≥0 this is (sin²x)/2+C. (c) Let u=cos x; du=−sin x dx, giving −∫ln u/u du=−(1/2)(ln(cos x))²+C. (d) Let u=e^x: −cos(e^x)+C. (e) Let u=√x; dx=2u du, giving 2∫cot u du=2ln|sin√x|+C. (f) Let u=sin x+cos x; du=(cos x−sin x)dx, so the integral is −ln|sin x+cos x|+C.",
            "diagram": null
          },
          {
            "id": "ex-6-2-q2",
            "qNo": "2",
            "question": "Evaluate using suitable substitutions: (a) ∫dx/(x²+16); (b) ∫sin x/(cos²x+1) dx; (c) ∫dx/√(e^{2x}−4); (d) ∫(2x+5)/(x²+4x+5) dx; (e) ∫(2+x)/√(4−2x−x²) dx.",
            "solution": "(a) (1/4)tan^{−1}(x/4)+C. (b) Let u=cos x: −tan^{−1}u+C. (c) Put u=e^x; then ∫du/[u√(u²−4)]=(1/2)sec^{−1}(e^x/2)+C, on e^x>2. (d) Write numerator as (2x+4)+1; result ln(x²+4x+5)+(1/√1)tan^{−1}(x+2)+C. (e) Complete square: 4−2x−x²=5−(x+1)² and numerator=(x+1)+1; result −√(5−(x+1)²)+sin^{−1}((x+1)/√5)+C.",
            "diagram": null
          },
          {
            "id": "ex-6-2-q3",
            "qNo": "3",
            "question": "Evaluate by integration by parts: (a) ∫x²e^x dx; (b) ∫x cos x dx; (c) ∫e^x sin x dx.",
            "solution": "(a) Repeated integration by parts gives e^x(x²−2x+2)+C. (b) x sin x+cos x+C. (c) Let I=∫e^x sin x dx; integrating by parts twice gives I=e^x sin x−e^x cos x−I, hence I=(e^x/2)(sin x−cos x)+C.",
            "diagram": null
          }
        ],
        "pageStart": 142,
        "pageEnd": 177
      },
      {
        "id": "ex-6-4",
        "exercise": "Exercise 6.3",
        "title": "Exercise 6.3",
        "description": "",
        "problems": [],
        "pageStart": 142,
        "pageEnd": 177
      },
      {
        "id": "ex-6-5",
        "exercise": "Exercise 6.1",
        "title": "Exercise 6.1",
        "description": "",
        "problems": [],
        "pageStart": 142,
        "pageEnd": 177
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-7",
    "number": 7,
    "title": "Plane Analytic Geometry: Straight Line",
    "titleUrdu": "",
    "pageRange": "Printed pages 178–212",
    "pageStart": 178,
    "pageEnd": 212,
    "sections": [
      {
        "id": "sec-7-1",
        "title": "7.1 Division of a Line Segment",
        "theory": "We are familiar with the set of real numbers as well as with several of its subsets, natural numbers and real numbers. The real numbers can easily be visualized by using dimensional coordinate system call real number line.\n\nCalculation of distance between two given points The study of plane analytic geometry is greatly facilitated by the use of vectors. The distance between any given points can be calculated by using the distance formula.\n\nIf P(x,y) and Q(x,y) are two points in the x-plane and is the angle in between the positive directions of the x and y axes, then, PQ is the directed line segment associated to initial point P(x.) and terminal point\n\nThe components of the directed line segment PQ are: OP+PQ=OQ\n\nSquaring both side of the directed line segment PQ to obtain\n\n= (x; − x; )2 + (y; − }; )2 + 2(x, −x, )(y2 − y1) cos\n\nPythagoras Theorem: If P(x,) Q(x,y) are the two points xy-plane, then the distance d betw given two points P(x,y) Q(x) is obtained by applyi theorem of Pythagoras to triangle (PQ)2 = (PR)2+(QR)\n\nThis is the distance from point P(x,y) to point Q,(x,,,) in the Cartesian coordinate plane.\n\nIf the line segment PQ is horizontal, then the distance from the point P(x,.,) to point Q(x.) is obtained by inserting y = y, in result (1): d=PQ| = √(x, − x,)2\n\nIf the line segment PQ is vertical, then the distance from point P(x.) to point Q(x,y) is obtained by inserting x1 = x, in result (1); d=[PQ=√(x-3)2\n\nSolution P(x)= (3,-2), Q(5,35)=(-1,-5) is used to obtain the distance d in between the two points P and Q:\n\nCo-ordinates of a point that divides the line segment in given ratio (Internally and externally)\n\nTake P(x,y) and Q(x,y) are the initial and terminal points of a line segment PQ and R(x, y) is a point that divides PQ in the ratio m, my. If, and rare the position vectors of P, Q and R. then x=(x+3)=x+3). 5=(3112)=x+y;), r=(x,y)=x+yƒ\n\nEquating x and y components to obtain the coordinates of R(x,y)\n\nthat divides the line segment PQ in the ratiom, m.\n\nIf R is the midpoint of the line segment PQ, then, mm, and the coordinates of the midpoint R of the\n\nThe coordinates of the point that divides the line segment PQ joining two points P(x,y,) and Q(x,y)\n\nexternally in the ratio m, :m, (m, or m, is negative) are:\n\nIf R(x, y) is a point that divides the line segment PQ in the ratio 5:7, then the coordinates-of R(x, y) is obtained through result (B):\n\nIf R(x, y) is a point that divides the segment PQ in the ratio 3:-2, then the coordinates of R(x, y) is obtained through result (B):\n\nThe medians and angle bisectors of a triangle are concurrent\n\nProof: If A(x,,,), B(x)) and C(,,,) are the vertices of a triangle ABC and P, Q and R are the midpoints of the sides AB, BC and CA, then the coordinates of the midpoint Q through\n\nIf G(x, y) is the centroid (in centre) of the triangle ABC, then, the coordinates of the point G that divides the median AQ in the ratiom, :m, = 2:1 are:\n\nSimilarly, the coordinates of the point G(x, y) that divides the medians BR and CP each in the\n\nTherefore, the point G(x, y) lies on each median and consequently the medians of the triangle ABC are\n\nProof: If ABC is a triangle with vertices A(x.), B(,) and C(,), whose lengths are\n\nABC BC-a and C4-6, then, the position vectors of A, B and C are respectively:\n\nConsider AD, BE and CF are the internal bisectors of the angles A, B\n\nand C that meet at centroid G. This is shown in Figure 7.5.\n\nIf AD is the internal bisector of angle A, then:\n\nThis means that D divides BC internally in the ratio c:b and the position vector of D is therefore: cr+br2\n\nIf BG is the internal bisector of the angle B, then,\n\nThe coordinates of the centroid G(x, y) is obtained from equation (iii) by equating the x and y\n\nSimilarly, the internal bisector of the angle C also passes through the point G(x, y). Thus, the angle bisectors of a triangle ABC are concurrent and G(x, y) is the point of concurrency.\n\npool. How can he find the largest circular pool that can be built there?\n\nSolution The largest possible circular pool would have the same size as the largest circle that can be inscribed in the triangular backyard. The largest circle that can be inscribed in a triangle is incircle. This can be determined by finding the point of concurrency of the angle bisectors of each corner of the backyard and then making a circle with this point as center and the shortest distance from this point to the boundary as radius.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-2",
        "title": "7.2 Slope of a Straight Line",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-3",
        "title": "7.3 Equation of a Straight Line Parallel to the Coordinate Axes",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-4",
        "title": "7.4 Standard Forms of the Equation of a Straight Line",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-5",
        "title": "7.5 Distance of a Point from a Line",
        "theory": "Recall distance formula to calculate distance between two points given in Cartesian plane.\n\nFind coordinates of a point that divides the line segment in given ratio (internally and externally).\n\nShow that the medians and angle bisectors of a triangle are concurrent.\n\nDerive the formula to find the slope of a line passing through two points.\n\nFind the condition that two straight lines with given slopes may be\n\nEquation of a straight line parallel to Co-ordinate axes\n\nFind the equation of a straight line parallel to\n\nDefine intercepts of a straight line. Derive equation of a straight line in\n\nShow that a linear equation in two variables represents a straight line.\n\nReduce the general form of the equation of a straight line to the other standard forms.\n\nRecognize a point with respect to position of a line.\n\nFind the perpendicular distance from a point to the given straight lines.\n\nFind the angle between two coplanar intersecting straight lines.\n\nFind the equation of family of lines passing through the point of intersection of two given lines. Calculate angles of the triangle when the slopes of the sides are given. Concurrency of straight lines",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-6",
        "title": "7.6 Angle Between Lines",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-7",
        "title": "7.7 Concurrency of Straight Lines",
        "theory": "Find the condition of concurrency of three straight lines.\n\nFind the equation of median, altitude and right bisector of a triangle. Show that\n\nthree medians, three altitudes, of a triangle are concurrent.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-8",
        "title": "7.8 Area of a Triangular Region",
        "theory": "",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-7-9",
        "title": "7.9 Homogeneous Equations",
        "theory": "Recognize homogeneous linear and quadratic equations in two variables.\n\nFind area of a triangular region whose vertices are given.\n\nInvestigate that the 2 degree homogeneous equation in two variables and y represents a pair of straight lines through the origin and find acute angle between them.\n\nWe are familiar about Cartesian coordinate system, we have learnt about it in our previous classes. This Cartesian coordinate system may be helpful to know the slope formula, Pythagoras theorem and distance formula. In this lesson we will learn in details and write the equations involving arbitrary points. Most of the geometric ideas can be expressed using algebraic equations. Analytic geometry is defined as:\n\n\"The study of relationship between geometry and algebra is called analytic geometry\".\n\nFor example to calculate the slope/gradient between two given points, the numerator difference in the y-coordinates some times called it \"Rise\" and the denominator is the diff\n\nbetween x-coordinates, some time called it “run” e-g.\n\nAnalytic Geometry was independent and simultaneous invention of Pierre De Fermat and Rene Descane fundamental idea of Analytic Geometry and the representation of curved lines by algebraic equations n\n\ntwo variables say, x and y was given in seventeenth century by them.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-7-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Find the distance between the two points P(3,-2) and Q(−1, −5).",
        "given": "",
        "method": "",
        "steps": [
          "Co-ordinates of a point that divides the line segment in given ratio (Internally and externally)",
          "Take P(x,y) and Q(x,y) are the initial and terminal points of a line segment PQ and R(x, y) is a point that divides PQ in the ratio m, my. If, and rare the position vectors of P, Q and R. then x=(x+3)=x+3). 5=(3112)=x+y;), r=(x,y)=x+yƒ",
          "Equating x and y components to obtain the coordinates of R(x,y)",
          "that divides the line segment PQ in the ratiom, m.",
          "If R is the midpoint of the line segment PQ, then, mm, and the coordinates of the midpoint R of the",
          "The coordinates of the point that divides the line segment PQ joining two points P(x,y,) and Q(x,y)",
          "externally in the ratio m, :m, (m, or m, is negative) are:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Find the coordinates of the point which divides the line segment PQ joining the two points (a). P(1, 2) and Q(3, 4) in the ratio 5:7. (b). P(3, 4) and Q(-6, 2) in the ratio 3: -2.",
        "given": "",
        "method": "",
        "steps": [
          "If R(x, y) is a point that divides the segment PQ in the ratio 3:-2, then the coordinates of R(x, y) is obtained through result (B):",
          "The medians and angle bisectors of a triangle are concurrent",
          "Proof: If A(x,,,), B(x)) and C(,,,) are the vertices of a triangle ABC and P, Q and R are the midpoints of the sides AB, BC and CA, then the coordinates of the midpoint Q through",
          "If G(x, y) is the centroid (in centre) of the triangle ABC, then, the coordinates of the point G that divides the median AQ in the ratiom, :m, = 2:1 are:",
          "Similarly, the coordinates of the point G(x, y) that divides the medians BR and CP each in the",
          "Therefore, the point G(x, y) lies on each median and consequently the medians of the triangle ABC are"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Find the centroid of the triangle ABC, whose vertices are A(3,-5), B(-7, 4) and C(10,-2). Solution Let A(3,-5), B(-7, 4) and C(10, -2) are the vertices of the triangle ABC, If G(x, y) is the centroid of the triangle ABC then, the coordinates of the point G(x, y) are:",
        "given": "",
        "method": "",
        "steps": [
          "ABC BC-a and C4-6, then, the position vectors of A, B and C are respectively:",
          "Consider AD, BE and CF are the internal bisectors of the angles A, B",
          "and C that meet at centroid G. This is shown in Figure 7.5.",
          "If AD is the internal bisector of angle A, then:",
          "This means that D divides BC internally in the ratio c:b and the position vector of D is therefore: cr+br2",
          "If BG is the internal bisector of the angle B, then,",
          "The coordinates of the centroid G(x, y) is obtained from equation (iii) by equating the x and y",
          "Similarly, the internal bisector of the angle C also passes through the point G(x, y). Thus, the angle bisectors of a triangle ABC are concurrent and G(x, y) is the point of concurrency."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-4",
        "num": "4",
        "title": "Example 4",
        "problem": "Muhammad Ayaan has a triangular piece of backyard where he wants to build a swimming",
        "given": "",
        "method": "",
        "steps": [
          "Solution The largest possible circular pool would have the same size as the largest circle that can be inscribed in the triangular backyard. The largest circle that can be inscribed in a triangle is incircle. This can be determined by finding the point of concurrency of the angle bisectors of each corner of the backyard and then making a circle with this point as center and the shortest distance from this point to the boundary as radius."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-5",
        "num": "5",
        "title": "Example 5",
        "problem": "Find the length JO.",
        "given": "",
        "method": "",
        "steps": [
          "We have the measures of two sides of the right triangle AHOL, so it is possible to find the length of the third side. Use the Pythagorean Theorem to find the length HO. = √(LO)2 - (HL)2 = √13-12-√169-144-√25=5 Since JOHO, the length JO also equals 5 units.",
          "The three points are A (-1,3), B (2,1) and C (5,-1). Show that |AB|+|BC-AC- In each case, find the midpoint of the line segment PQ joining the two points P(x,y) and Q(94);",
          "In each case, find the coordinates of the point R(x,y) which divides the line segment PQ joining",
          "a. P(1,2), Q(3,4) in the ratio 5:7. b. P(3,4), Q(-6,2) in the ratio 3:-2.",
          "In each case, in what ratio is the line segment PQ (joining the two points P(x,y) and",
          "Find the centroid of the triangle ABC, whose vertices are the following:",
          "automatically give the symmetric form of a line L after simplification:",
          "14 Find the equation of a straight line with inclination 45° and passing through the",
          "Solution Here we have inclination a=45° and point (x,,,)=(2,√2). The equation of line",
          "Substitute the above values in the formula to get the equation of a straight line.",
          "The normal form of a line is the equation of a line in terms of the length of the perpendicular on it from the origin and that perpendicular makes an angle with the x-axis.",
          "If a line L intersects the x-axis and y-axis at points A and B, then OA and OB are the x and y-intercepts of the line L. Draw ON perpendicular to line L that provides the perpendicular distance p from the origin on the line L which is denoted by ON= p. If ON makes an angle with the positive direction of the x-axis, then the r and intercepts of the line L are respectively:",
          "IfOA and OB are the x and y-intercepts of a line L, then through result (x), the equation of a",
          "line L in terms of perpendicular distance p and angle is:",
          "The normal form of a line is also referred to perpendicular form of a line.",
          "15 Find the corresponding equation of a line, if the length of the perpendicular distance from",
          "the origin on a line is 3 units that makes an angle of 120o.",
          "Solution Result is used for the assumptions p=3, 6=120 to obtain the required equation of a line",
          "difference in the y-coordinates some times called it \"Rise\" and the denominator is the difference For example to calculate the slope/gradient between two given points, the numerator is the",
          "between x-coordinates, some time called it \"run\" e.g.",
          "Analytic Geometry was independent and simultaneous invention of Pierre De Fermat and Rene Descartes. The fundamental idea of Analytic Geometry and the representation of curved lines by algebraic equations relating two variables say, x and y was given in seventeenth century by them.",
          "We are familiar with the set of real numbers as well as with several of its subsets, including natural numbers and real numbers. The real numbers can easily be visualized by using a one dimensional coordinate system call real number line.",
          "7.1.1 Calculation of distance between two given points The study of plane analytic geometry is greatly",
          "facilitated by the use of vectors. The distance between any two given points can be calculated by using the distance formula.",
          "ay-plane and 0 is the angle in between the positive directions of the x and y axes, then, PQ is the directed line segment associated to initial point P(.) and terminal point Q(X12).",
          "The components of the directed line segment PQ are: OP+PQ=OQ",
          "Squaring both side of the directed line segment PQ to obtain",
          "➡ (x; − x, )2 + (y'; − y', )2 + 2(x-x)(); 1) cos",
          "Pythagoras Theorem: If P(5.3) Q.) are the two points in the xy-plane, then the distance between the given two points P(x,y) and Q(x) is obtained by applying the theorem of Pythagoras to triangle PQR: (PQ)\" = (PR)2+(QR)\"",
          "This is the distance from point P(x) to point Q(x.) in the Cartesian coordinate plane.",
          "The distance from the origin 0(0,0) to point P(x,y) is obtained by inserting x,=,=0 in result (1): d=|OP|= √x2+y?",
          "If the line segment PD is horizontal, then the distance from the point P(x,y) to point Q(x,y) is obtained by inserting y;=y, in result (1): d=PQ|= √(x−x,)2",
          "If the line segment PQ is vertical, then the distance from point P(x) to point Q(x) is obtained by inserting x = x, in result (1): d=[PQ)=√(s—35)a"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-6",
        "num": "1",
        "title": "Example 1",
        "problem": "Find the distance between the two points P(3,-2) and Q(−1, −5).",
        "given": "",
        "method": "",
        "steps": [
          "Co-ordinates of a point that divides the line segment in given ratio (Internally and externally)",
          "Take P(x,.,) and Q(x) are the initial and terminal points of a line segment PQ and R(x, y) is a point that divides PQ in the ratio mm. If, and are the position vectors of P. Q and R, then x-(x,y1)=x,i+y1j, (2,2)=x+y), r(x,y)=x+yj",
          "(x, y) = m2 (x1. Y1) +m, (x2+ Y2), components form",
          "Equating x and y components to obtain the coordinates of R(x,y)",
          "that divides the line segment PQ in the ratio m, :m..",
          "If R is the midpoint of the line segment PQ, then, mm, and the coordinates of the midpoint R. of the",
          "The coordinates of the point that divides the line segment PQ joining two points P(x,,};) and Q(x,y,)",
          "externally in the ratio m, :m, (m, or m, is negative) are: (x,y)=",
          "2 Find the coordinates of the point which divides the line segment PQ joining the two points (a). P(1, 2) and Q(3, 4) in the ratio 5:7. (b). P(3, 4) and Q(-6, 2) in the ratio 3: -2",
          "If R(x, y) is a point that divides the line segment PQ in the ratio 5:7, then the coordinates of R(x, y) is obtained through result (B):",
          "If R(x, y) is a point that divides the segment PQ in the ratio 3:-2, then the coordinates of R(x,y) is obtained through result (B):",
          "The medians and angle bisectors of a triangle are concurrent",
          "Proof: If A(x,y), B(x.) and C(x,.,) are the vertices of a triangle ABC and P, Q and R are the midpoints of the sides AB, BC and CA, then the coordinates of the midpoint Q through",
          "If G(x, y) is the centroid (in centre) of the triangle ABC, then, the coordinates of the point G that divides the median AQ in the ratio m, :m, -2:1 are:",
          "Similarly, the coordinates of the point G(x, y) that divides the medians BR and CP each in t",
          "Therefore, the point G(x, y) lies on each median and consequently the medians of the triangle ABC are"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-7",
        "num": "3",
        "title": "Example 3",
        "problem": "Find the centroid of the triangle ABC, whose vertices are A(3,-5), B(−7, 4) and C(10, −2). Solution Let A(3,-5), B(-7, 4) and C(10, -2) are the vertices of the triangle ABC, If G(x, y) is the centroid of the triangle ABC then, the coordinates of the point G(x, y) are:",
        "given": "",
        "method": "",
        "steps": [
          "Consider AD, BE and CF are the internal bisectors of the angles, B",
          "and C that meet at centroid G. This is shown in Figure 7.5.",
          "If AD is the internal bisector of angle A, then:",
          "This means that D divides BC internally in the ratio cb and the position vector of D is therefore: cr+ br",
          "If BG is the internal bisector of the angle 8, then,",
          "The coordinates of the centroid G(x, y) is obtained from equation (iii) by equating the x and",
          "Similarly, the internal bisector of the angle C also passes through the point G(x, y). Thus, the angle bisectors of a triangle ABC are concurrent and G(x, y) is the point of concurrency."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-8",
        "num": "4",
        "title": "Example 4",
        "problem": "Muhammad Ayaan has a triangular piece of backyard where he wants to build a swimmin pool. How can he find the largest circular pool that can be built there?",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-9",
        "num": "5",
        "title": "Example 5",
        "problem": "Find the length JO.",
        "given": "",
        "method": "",
        "steps": [
          "We have the measures of two sides of the right triangle AHOL, so it is possible to find the length of the third side. Use the Pythagorean Theorem to find the length HO.",
          "The three points are A (-1,3), B (2,1) and C (5,-1). Show that |AB|+| BC|=|AC|-",
          "In each case, find the midpoint of the line segment PQ joining the two points P(x,,,) and Q(x): a. P(10,20), Q(-12,-8)",
          "In each case, find the coordinates of the point R(x,y) which divides the line segment PQ joining",
          "1. P(1,2), (3,4) in the ratio 5:7. b. P(3,4), Q(-6,2) in the ratio 3:-2.",
          "In each case, in what ratio is the line segment PQ (joining the two points P(x,.) Q(x,,',) divided by the point R(x, y):",
          "Find the centroid of the triangle ABC, whose vertices are the following:",
          "The slope of a line is a measure of the when \"steepness\" of the line, and whether it rises, or falls when moving from left to right. The line from A to B rises up, while the line from C to D goes down are depicted in the Figure 7.6. 7.2.1 Slope of a line",
          "The graph of a line can be drawn knowing only one point on the line if the \"steepness\" of the line is known, too.",
          "(vertically) to return to the line, then the slope of the line is the \"steepness\" defined as the ratio of the vertical rise to the horizontal run: slope-rise, the run is always a movement to the right",
          "7.2.2 Formula to find the slope of a line passing through two points",
          "Mathematically, if any two points on a line are",
          "available, then their join makes a constant angle with a fixed direction and the angle so formed is independent of the choice of the two points on the line. This is a precise way of saying that any line has a constant slope. It is customary to measure the angle which a line makes with the positive direction of the x-axis. The quantity tan is defined to be the slope of the line and is denoted by m. The slope of a line is also referred to gradient of the line.",
          "For illustration, if A(x,y) and B(x,.), where x, x, are any two points, then their join develops a",
          "with the x-axis. Draw AM, and BN parallel to y-axis and AL",
          "The slope of a line L through the two points A(,) and B(x,y), is therefore:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-10",
        "num": "6",
        "title": "Example 6",
        "problem": "Find the slope m of the line L through the points",
        "given": "",
        "method": "",
        "steps": [
          "The given two points E(2,4) and F(4,6) form a line L, whose mure where m is a slope. slope is:",
          "The given two points M(3,1) and N(-1,3) is form a line L. whose slope is:",
          "7.2.3 Condition for two straight lines with given slopes are",
          "If L, and L, are the two lines having slopes m, and m,, then the lines L, and L, are parallel if they make the same angle with the x-axis, that means they have the same slope. Conversely, if two lines L, and L, have the same slope, then they will make the same angle",
          "with the x-axis and the lines L, and L, are therefore parallel for which:",
          "It is important to note that the lines parallel to x-axis have zero slopes whereas the lines parallel to y-axis have the slope so.",
          "If L, and L, are the two perpendicular lines make the angles and ẞ with the x-axis, then the slopes of the lines L,",
          "Ly are respectively m = tanc and m,tanß. From the Figure 7.9, it is clear tha",
          "The given lines L, and L, are found perpendicular, since the product of their slopes equals -1:",
          "7.3 Equation of a Straight Line Parallel to Co-ordi",
          "7.3.1 Equation of a straight line parallel to",
          "o y-axis and at distance 'a' from it. o x-axis and at a distance 'b' from it.",
          "Let PQ be a straight line parallel to y-axis at a distance \"a\" units from it see Figure 7.10. This is very clear, that all the points on the line PQ",
          "have the same ordinate say 'b'. Therefore, PQ can be considered as the",
          "locus of a point at a distance \"a\" from y-axis and all points on the PQ",
          "a therefore, the equation of straight line is parallel to y-axis at a distance",
          "If a = 0, then the straight line coincides with the y-axis and its equation becomes x = 0). If PQ is parallel and to the left of y-axis at a distance \"a\", then its equation is x=-b."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-11",
        "num": "7",
        "title": "Example 7",
        "problem": "Find the equation of straight line parallel to y-axis at a distance 5 units on the right side of J-axis.",
        "given": "",
        "method": "",
        "steps": [
          "Let PQ be a straight line parallel to x-axis at a distance \"b\" units from it see Figure 7.11. This is every clear that all the points on the same ordinate say, \"b\". Therefore, PQ can be considered as the locus of a point at a distance 'b' from .x- axir and all points on the PQ satisfy the condition y = b. Therefore, the equation of a straight line is parallel to x-axis at a distance b from it if e.g.",
          "i. Ifb-0, then the straight line coincides with the x-axis and its equation becomes y = 0. If PQ is parallel and below the x-axis at a distance \"b\", then its equation is y=-b.",
          "7.4 Standard Form of Equation of a Straight Line",
          "Because of their simplicity, linear equation (line) is used in many applications to describe relationships between two variables. We shall see some of these applications in this unit. First, we need to develop some standard forms that are related to linear equations.",
          "\"If a straight line AB intersects x-axis at C and y-axis at D, then OC is called the x-intercept of AB on the x-axis and OD is called the y-intercept of AB on the y-axis."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-12",
        "num": "8",
        "title": "Example 8",
        "problem": "Find the x and y intercepts of a line 2x+4y+6-0.",
        "given": "",
        "method": "",
        "steps": [
          "The y-intercept of a line is obtained by putting x-0 in a line:",
          "The general criteria are that a line in two dimensional space can be determined by specifying its slope and just one point.",
          "Let L be the line see Figure 7.13 develops the y-intercept e on",
          "the y-axis. The line L also makes an angle with the positive direction of the x-axis that develops a slope = tanë.",
          "Let P(x,y) be any point on the line L. Draw PM parallel to y-axis and CN parallel to x-axis that give",
          "In APCN, the angle is PNC=90° and the slope of the line L",
          "is giving the slope-intercept form of the line L:",
          "If the straight line L passes through the origin (0, 0), then e=0 and the equation of line becomes y",
          "mx. In y = mx + c, m denotes the slope and e denotes the y-intercept of the line L on the an of y."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-13",
        "num": "9",
        "title": "Example 9",
        "problem": "Determine the slopes of the following lines: (a). x-y=5 (b). 2x+3y=6",
        "given": "",
        "method": "",
        "steps": [
          "Thus, the slope of the line is the coefficient of x-term which is m"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-14",
        "num": "10",
        "title": "Example 10",
        "problem": "Find an equation of the line with slope 4, when the y-intercept is 6.",
        "given": "",
        "method": "",
        "steps": [
          "If L is a line see Figure 7.14 passing through the point A(x,y) and P(x, y) is any point on a line L, then the slope of the",
          "line L is giving the point-slope form of a line L:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-15",
        "num": "11",
        "title": "Example 11",
        "problem": "Find an equation of a line with slope 4 and passes through the point (2,4).",
        "given": "",
        "method": "",
        "steps": [
          "If L is a line see Figure 7.15 passing through the two points A(x,,,) and B(x,y), then the slope of the line Lis:",
          "If the equation of a line L through the A(x,y) with slope mis",
          "then the equation of a line L through the two points A(x) and B(x,y) is the equation of the two-point form of a line L:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-16",
        "num": "12",
        "title": "Example 12",
        "problem": "Find an equation of a line that passes through the two points P(-1,-2) and Q(-5,0). Solution Result (v) is used for the assumptions P(x,y) = P(-1,-2), Q(x, y) = Q(-5,0) to obtain the required two-point form of a line:",
        "given": "",
        "method": "",
        "steps": [
          "Let P(x,y) be any point on the line L. Draw PM parallel to y-aris and PN parallel to x-axis. From the Figure 7.16, the comparison of similar triangles ABNP and APMA is giving the equation of double- intercept form of a line L:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-17",
        "num": "13",
        "title": "Example 13",
        "problem": "Find the equation of a line whose x and y intercepts are (3,0) and (0,4) respectively. Solution Result (vi) is used for the assumptions a-3, 6-4 to obtain the required line:",
        "given": "",
        "method": "",
        "steps": [
          "r to vary with any positive or negative values, then P will take any position on the line L. Conversely, if P is given to be any point on the line L, then the unique value of r can be found which in fact is the distance of P from A. Thus, it follows that serves as a parameter of point P.",
          "To find the coordinates of a point P in terms of the parameter, let us draw AL and PM parallel to y-axis and AN parallel to x-axis, that with the following assumptions",
          "dvelops the parametric equations of a line L through the point A(x) at an angle 0:",
          "The parametric equations (viii) automatically give the symmetric form of a line L after simplification:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-18",
        "num": "14",
        "title": "Example 14",
        "problem": "Find the equation of a straight line with inclination 45° and passing through the pot (2,√2).",
        "given": "",
        "method": "",
        "steps": [
          "Substitute the above values in the formula to get the equation of a straight line.",
          "The normal form of a line is the equation of a line in terms of the length of the perpendicular on it from the origin and that perpendicular makes an angle with the x-axis.",
          "If a line L intersects the x-axis and y-axis at points A and B, then OA and OB are the x and y-intercepts of the line L. Draw ON perpendicular to line L that provides the perpendicular distance p from the origin on the line L which is denoted by ON= p. If ON makes an angle with the positive direction of the x-axis, then the x and y- intercepts of the line L are respectively:",
          "If OA and OB are the x and y-intercepts of a line L, then through result (x), the equation of a normal",
          "line L in terms of perpendicular distance p and angle is:",
          "The normal form of a line is also referred to perpendicular form of a line."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-19",
        "num": "15",
        "title": "Example 15",
        "problem": "Find the corresponding equation of a line, if the length of the perpendicular distance from",
        "given": "",
        "method": "",
        "steps": [
          "Solution Result (x) is used for the assumptions p=3, 0=120 to obtain the required equation of a lit",
          "A linear equation in two variables is a straight line",
          "A first degree polynomial p(x)=4x+q, is rearranged to obtain an equation of the form",
          "is then called the general equation of the straight line. Here a, b and c are Remember constants while x and y are variables.",
          "Consider, If P(x3), Q.,) and R(x,,y,) are the three points on the locus polynomial p(x) is represented by the straight line",
          "The three lines from equation (ii) to equation (iv) develops a homogeneous system of three linear",
          "The homogeneous system of linear equations (v) defines a nontrivial solution only if the determinant of a coefficient matrix A of the system (v) is zero:",
          "X(5—35)−34(5-1)+(x);−1,31⁄2)=0 Equation (vi) is rearranged to obtain:",
          "Multiply both sides of equation (vii) by to obtain the area of the triangle formed by P. Q and R. that",
          "Since the three points P, Q and R. lying on the locus (1) are collinear. Hence, the locus (i) represents a straight line.",
          "General form of a straight line is reducible to other standard forms Any standard form of a line can also be determined from the general form of a line (i).",
          "To reduce the general form (i) to the slope intercept form of a line, we need to involve the following steps",
          "To reduce the general form (i) to the double-intercept form, we need to involve the following ste",
          "To reduce the general form (i) to the normal form, we need to involve the following steps: From the Figure 7.18(b), the angles along the positive directions of the x and y-axis are following:",
          "The values of cose and sine are used in the trigonometric identity cos\"0+ sin 0-1 to obtain p",
          "This p is the perpendicular distance from the origin to the line +2=1 (ie, nx+my-mn=",
          "course, the perpendicular distance from the origin to the line ax+by+c=0 must be:",
          "For converting the general form (i) to normal form, divide the line ax+by+c=0 by",
          "obtain the conversion of the general form (1) in the normal form:",
          "Find the equation of lines that are represented on the coordinate planes:",
          "In each case, find the slope, if it is defined:",
          "What are the x- and y-intercepts for each of the following lines? a. y=2x+6",
          "In each case, show that the pair of lines are parallel or perpendicular or neither. a. x-2y-6=0, 2x+y-5=0",
          "In each case, find the equation of a line that passes through the pair of points:",
          "(0,0) and A(2,6) b. E(1,0) and F(2,5) c. 1(1,1) and J(3,3)",
          "In each case, find the equation of a line that passes through the point A(x,y) having slope m:",
          "In each case, find the equation of a line that exists the y-intercept e and slope m:",
          "How can you calculate the midpoint between your home and school/college? Calculate this distance and write the procedure.",
          "In Euclidean geometry, the distance from a point to a line is the shortest distance from a given point to any point on an infinite straight line. It is the perpendicular distance of the point to the line, the length of the line segment which joins the point to nearest point on the line.",
          "7.5.1 Position of a point with respect to a line",
          "To show that the point P(x,.,) is on one side or on the other side of the straight line ax+by+c=0 according as the expression ax, +by+c<0 or ax,+by+c>0, the procedure developed is as under:",
          "Let AB be the straight line ax + by + c = 0 and P(x,y) is a point above the line AB Figure 7.18 and P(x,y) is also a point below the line AB Figure 7.19. From P draw perpendicular PM on the x-axis that cuts the line AB at a point Q whose coordinates are Q(x,,J1⁄2)- If Q(x,y) lies on the line AB, then it give:",
          "Hence P lies on one side or on the other side of the line ax+by+c=0 accom"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-20",
        "num": "16",
        "title": "Example 16",
        "problem": "Determine whether the point P(10,-6) lies above or below the line 9x+10y-3=0.5",
        "given": "",
        "method": "",
        "steps": [
          "The given line 9x+10y-3-0 is compared to the line ar+by+c=0 to obtain the coeff",
          "The given point P(10,-6) is substituted in the given line to obtain:",
          "Thus, the point P(10,-6) lies above the given line 9x+10y-3=0",
          "ii. The given point P(10,-6) and the origin 0(0,0) are substituted in the given line to obtain:",
          "Hence, the point P(10,-6) and the origin O(0,0) lie on the opposite side of the given line 9x+10y-3=0. 7.5.2 Perpendicular distance from a point to the given straight line",
          "and = (a,b) is a nonzero vector perpendicular to the line (i) at a point Q(x,y), then the distance D is the scalar projection",
          "of a vector QP (associated to any point (P(x,y)) onto :",
          "the perpendicular distance from a line ar+by+c=0 to a point P(x,y)-"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-21",
        "num": "17",
        "title": "Example 17",
        "problem": "Find the perpendicular distance from a line 7x+3y-9-0 to a point P(2,3).",
        "given": "",
        "method": "",
        "steps": [
          "If the two lines are available, then the angle between these two lines can found as follows:",
          "7.6.1 The angle between two coplanar intersecting straight lines",
          "The unit vectors are the vectors lie in the same directions of the given lines. The unit vectors along",
          "the line AB and CD are respectively u= (cose,,sin0,) and",
          "The angle of intersection between the lines AB and CD is the angle of intersection in between their unit vector u and y that can be found by taking the dot product in between the unit vectors a and 1:",
          "The standard form of the angle is obtained if",
          "is positive, then result (1) gives the acute angle between the lines AB and CD.",
          "is negative, then result (1) gives the obtuse angle between the lines AB and CD.",
          "If one of the given lines is parallel to the y-axis, then the angle is not possible to obtain by formula:",
          "Because 90° is the angle made by that line with the positive x-axis and tan 90°, In such a case, the angle between the lines will be calculated by drawing the figure.",
          "The lines are parallel, if the cross product in between the unit vector and v is zero:",
          "The lines are perpendicular, if the dot product in between the unit vector and v is zero:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-22",
        "num": "18",
        "title": "Example 18",
        "problem": "Find the angle from the line 7x+3y-9-0 to the line 5x-2y+2=0.",
        "given": "",
        "method": "",
        "steps": [
          "If is the angle from first line to line second, then",
          "The equation of family of lines passing through the point of intersection of two given lines",
          "and P(x,y) is their point of intersection. The given lines L, and L are used to obtain a first degree equation of a straight line in x and y: (qx+by+c)+ λ(ax+by+c)=0, 2, is constant",
          "The coordinates of a point P will reduce each line in (iii) to zero, since, by hypothesis, P is the point of intersection, i.e., it lies on each line. Therefore P satisfies (iii) and represents the family of lines through the point of intersection of L,=0 and L2 =0."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-23",
        "num": "19",
        "title": "Example 19",
        "problem": "Develop the family of lines through the point of intersection of the lines 2x-3y+4=0) and 2x+y-1-0. Find the line from the family of lines which is",
        "given": "",
        "method": "",
        "steps": [
          "The family of lines (iv) is parallel to the line with slope m",
          "The value of¿=-3 is used in (iv) to obtain the particular line from the family of lines (iv): (2x-3y+4)-3(2x+y=1)=0",
          "The slope of the given line 4x+3y-1-0 ism,--. The family of lines (iv) is perpendicular to",
          "the line 4x+3y=1=0, if and only if the product of their slopes equals -i:",
          "The value of 2-is used in (iv) to obtain the particular line from the family of lines:",
          "7.63 The angels of the triangle when the slopes of the sides are given",
          "IfA(x,, },), B(x,, }', ) and C(x,y) are the vertices of a triangle ABC and the slopes of the sides AB, BC and CA of the triangle ABC are respectively:",
          "If0,, 0,and, are the angles in between their sides AB to AC, BC to",
          "BA and CB to CA respectively, then the angles can be found through results tan 0) =",
          "The angles from the sides AB to AC, BC to BA, and CA to CB of a triangle ABC are respectively: tan0,--m"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-24",
        "num": "20",
        "title": "Example 20",
        "problem": "Find the angles of the triangle ABC, whose vertices are A(-2,-3), B(4,-1) and C(2,3).",
        "given": "",
        "method": "",
        "steps": [
          "Result (v) to obtain the angle 0, from the sides AB to AC use:",
          "Result (v) to obtain the angle 0, from the sides BC to BA use:",
          "Result (v) to obtain the angle 0, from the sides CA to CB use: tan0,",
          "Show that the point P(x,y) lies above or below the line ax+by+c=0. Also show that the po P(x,y) and the origin lie on the same side or on the opposite side of the line ax+by+c=0 a. P(4,-5), 4x-3y-17=0",
          "In each case, show that the points P(x,y) and Q(3) are on the same side or on the opposi side of the line ax+by+c=0:",
          "In each case, find the perpendicular distance from the line ax+by+c=0 to a point a. P(3, 4), 4x-3y+6=0",
          "b. P(5,8), 3x-2y+7=0 c. P(3,-1), 5x+12y-16-0 from the line L, to line L,, if the slopes of the lines L, and L",
          "In each case, find the angle from the line L, to the line L.:",
          "In each case, find the angle from the line L, to the line L",
          "In each case, find the angles of the triangle ABC whose vertices are the following: a. A(1,2), B(4,2) and C(-2,3)",
          "Find the equation of the straight line from the family of straight lines through the point of",
          "a. 2x-3y+4=0,3x+4y-5-0 and is perpendicular to the line 6x-7y-18=0. b. 3x-4y+1=0, 5x+y-1-0 and cuts off equal intercepts from the ares.",
          "Pierre de Fermat was French lawyer and a mathematician. He was credited for the early development of calculus. In particular he was recognized because of his discovery of an original method of finding the greatest and smallest ordinates of curved lines which are very important for the differential calculus. He also made some contribution to number theory, but a magnificent contribution to analytical geometry, optics and probability. He became famous in the community of mathematics because of Fermat's principle for light propagation and his Fermat's last theorem in the field of number theory. Fermat's work in analytical geometry was circulated in manuscript form in 1636. He also developed a method for determining maxima, minima and tangents to various curves that was equivalent to differentiate calculus.",
          "Before to touch the concurrency of straight lines, we need to develop the concept of intersection of lines. Logically, the solution of the system of lines exists only, if the lines intersect.",
          "For illustration, the two lines.x+y= 1 and x-y=0 is forming the system of two linear equations",
          "reduced in an echelon form through row operations",
          "The second equation is giving y-which is used in",
          "equation to obtain x-2. The solution set (x)-(4) of",
          "system of two linear equations is unique (one solution set). This",
          "It is important to note that the system of two lines",
          "x+y=1 and x-y=0 is giving a unique solution set, since the lines are intersecting at just a single point.",
          "x + y = 1 and x+y=0 is not giving a solution set, since the lines are not intersecting, because the line are parallel.",
          "x + y = 1 and 2x + 2y = 2 is giving an Infinite set of solutions, since the lines are intersecting more than one points, because the lines make a sense of coincident lines.",
          "unique solution is the unique point of intersection at which the given two lines intersect.",
          "7.7.1 Condition of concurrency of three straight lines",
          "The condition of concurrency of three straight lines is the point of intersection at which the three straight lines intersect. For illustration, if the given three lines are",
          "then, the three lines develop a homogeneous system of three linear equations",
          "In homogeneous system of three linear equations lines (ii), the homogeneous coordinates are used:",
          "Concurrency means that the three lines must intersect at a point G(x,y), say, that can be found by solving the system of linear equations (1) The system (ii) has a nontrivial solution if the determinant of the coefficient matrix of the system (ii) is zero:",
          "This is the condition of concurrency of three lines.",
          "For required point of concurrency follow the steps given below:",
          "Choose any two lines from the given three system of linear equations (1).",
          "Develop the system of these two linear equations.",
          "of the system of two linear equations and reduce it in an echelon form",
          "Substitute the developed point of intersection in the remaining third line. If the point of intersection satisfies the remaining third line, then that point of intersection should be taken as the point of concurrency of the given thre"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-25",
        "num": "21",
        "title": "Example 21",
        "problem": "Show that the three lines x+4y+3=0, 5x-4-5-0 and 2x+2y+1=0 are concurrent. the lines are concurrent, then find out the point of concurrency.",
        "given": "",
        "method": "",
        "steps": [
          "The given three lines are concurrent. For the point of concurrency G(x,y), choose the first two lines",
          "that develops the system of two linear equations, whose augmented matrix A/b is reduced in",
          "to obtain the reduced system of linear equations:",
          "The second equation is giving y--which is used in first equation to obtain x",
          "line with substitution of the point of intersection (x,y)-(-) is going to be zero:",
          "Thus, the given three lines are concurrent at a point G.-).",
          "7.7.2 Equation of median, altitude and right bisector of a triangle",
          "A median is a line segment from an interior angle of a triangle to the mid point of the opposi side. Look at the following example, the procedure to find the equation of median of triangle i"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-26",
        "num": "22",
        "title": "Example 22",
        "problem": "Find the equation of the median of a triangle having vertices are 4(8, -5), B(6,5) and C(-6,9).",
        "given": "",
        "method": "",
        "steps": [
          "Then its co-ordinates are given as (816-515) - (7.0)",
          "Since, the median CC passes through points C and C, using the two-point form of the equation of a straight line, the equation of median CC' can be found as",
          "If is the midpoint of side BC of AABC then its coordinates are given as",
          "Since, the median A passes through the point and respectively. By using the two point form of the equation of a straight line, the equation of median",
          "If 8' is the midpoint of side AC of ABC then its coordinated are given as",
          "Since, the median 88' passes through the point B and B' respectively. By using the two point form of the equation of a straight line, the equation of median 88' can be found as",
          "Altitude of a triangle is a perpendicular drawn from the vertex of the triangle to the opposite side. This is also known as the height of the triangle. Mostly it is used to find the area of the triangle. Look at the following example the procedure to find the equation of altitude is illustrated in example 22. Example 23 Find the equation of altitude of triangle ABC having vertices are 4(-7, 4), B(9, 6) and C[7, -10).",
          "The altitude CC' is perpendicular to side 48, so, the slope of",
          "Since the altitude CC' passes through the point C(7,-10), by using point slope form of the equation of a line, the equation of CC' is",
          "Which is the equation of the altitude from C to 48.",
          "The altitude AA' is perpendicular to side BC, so, the slope of AA'",
          "Since, the altitude passes through the point (-7,4), by using the point slope form of the equation of",
          "Which is the equation of the altitude from A to BC",
          "1. The altitude BB' is perpendicular to side AC. So,",
          "=1, since, the altituded passes through the point B(9,6). By using t (-1)",
          "pint slope form of the equation of a line, the equation of BB' is y-6=1(x--x--3-0. Which the equation of the altitude from B to AC.",
          "The bisector of a triangle is a line perpendicular to the side and passing through its midpoint. T three perpendicular bisectors of the sides of a triangle meet in a single point. The procedure to find th equation of a bisector is illustrate in the following example."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-27",
        "num": "24",
        "title": "Example 24",
        "problem": "Find the equation of the right bisector of a triangle having pints are 4(-7, 4), B(10, 8).",
        "given": "",
        "method": "",
        "steps": [
          "Fore bisector of 4(-7, 4) and B(10, 8) put the values in equation (i)",
          "For bisector of B(10, 8) and C(6, -12), put the values in equation (1)",
          "For bisector of 4(-7, 4) and C(6,-12) put the values in equation (i)",
          "Show that, three right bisectors, three medians and three altitudes of a",
          "Three right bisectors of a triangle are concurrent",
          "To show the concurrency of the right bisectors of a triangle, the procedure developed is as under:",
          "Let ABC be a triangle, whose vertices are A(1,3),B(.) and C(x,y,), D, E, F are the midpoints of the sides BC, CA, AB of a triangle ABC whose coordinates are respectively:",
          "If the slope of the side BC and the slope of the right bisector DG of the side BC are respectively:",
          "then, the equation of the right bisector DG of side BC is obtained by point-slope form of a line:",
          "Similarly, the equations of the right bisectors EG (of side CA), FG (of side 18) is respectively.",
          "The right bisectors DG, EG and FG is concurrent, if the determinant of the coefficient matrix of the related system of equations of the right bisectors DG, EG and FG equals zero:",
          "The operation of addition of rows R+R+R, to row R is used to obtain:",
          "The value of the determinant is zero. Hence, the right bisectors DG, EG and FG of a triangle ABC are"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-28",
        "num": "2",
        "title": "Example 2",
        "problem": "Let ABC be a triangle with vertices 4(0,0), B(8,6) and C(12,0). Show that the right bisectors",
        "given": "",
        "method": "",
        "steps": [
          "Solution The vertices A(5.3)=4(0,0), B(5.3) B(8,6) and C(x,.,)= C(12,0) of the triangle ABC are used in the determinant (1) to obtain:",
          "The determinant (ii) equals zero. Hence, the right bisectors DG, EG and FG the triangle ABC",
          "Let ABC be a triangle, whose vertices are A(x,y),B(x) and",
          "C(x,,,). The altitudes of the triangle ABC are AD, BE and CF.",
          "If the slope of the side BC and the slope of the altitude AD are",
          "then, the equation of the altitude AD is obtained by point-slope form of a line:",
          "Similarly, the equations of the altitudes BE and CF are respectively:",
          "The altitudes AD, BE and CF are concurrent, if the determinant of the coefficient matrix A oft related system of equations of the altitudes AD, BE and CF equals zero:",
          "The operation of addition of rows R+R+R, to row R, is used to obtain:",
          "The value of the determinant is zero. Therefore, the altitudes AD, BE and CF of a tringk",
          "ABC will also make concurrency at a point say, G(x,y).",
          "The conclusion drawn from the above results is that the three medians AD, BE and CF of",
          "Exquiple 26 Let ABC be a triangle with vertices (0,0), 83,6) and C12,0). Show in the altitudes. BE and CF of the triangle ABC are concurrent.",
          "Solution The vertices (x,y)=4(0,0), (5.3)=(86) and C) (20) of the triangle ABC are used in the determinant (i to oftenc",
          "The determinant (iii) equals zero. Hence, the ahaudes AD, BE and CF of the tringle Cure concurrentt-",
          "Let ABC be a triangle whose vertices are P(x).P(+)",
          "and (.). Project PA.PB and PC on the xaze that",
          "The area of the trianguler region P3, is the sum of the areas of the trapezia PACP.PCBP and PASite trapezium PABP",
          "It is important to note that the area A of the triangular region PR equals ze wiem dietvertisonsofili triangular region are collinear points."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-29",
        "num": "27",
        "title": "Example 27",
        "problem": "Find the area of the triangular regla. PPP, whose varies are R{[(4-5)) R[65-69) and! P(3.1).",
        "given": "",
        "method": "",
        "steps": [
          "= [4(-6-13+5(5-3) + (5 + 189)||- |-28-10-13-punis",
          "In general, any line equation in two variables that passes through the origin is called homogeneous equation.",
          "Homogeneous linear and quadratic equation in two variables",
          "is called a nonhomogeneous emeton et lice For c= 0, the nonhomogeneous equation (1) gives the homogeneous equation of the form that passes through the origin definitely. This also defines a homogeneous equation of degree 1, since the ar+by=0 indices of x and y in every term of (ii) is the same, the degree being 1. For example, the equation of line +",
          "(ii) y=0 is homogeneous line, since it defines a homogeneous equation of degree 1.",
          "Homargenmons quadratic equation in two variables",
          "\"An equation of the form ax+2y+by2=0, 0, where a, b, care constants",
          "is called a homogene sus quadratic equation of second degree in variables x and y\" Since the sum of the indices of x and y in every term are the same number \"2\". For example,",
          "are homogeneous quadratic equations of the second degree in x and y. On the other hand, the equation of the form 3xy2-4x+5y=0 is not a homogeneous equation, since the sum of the indices of x and y are not the same in each and every term.",
          "7.9.2 Second degree homogeneous equations represents a pair of straight lines",
          "Stundurd form of second degree becogenevas equation",
          "Ifqx+hy+c=0anda,x+by+c=0 are the two straight lines, then the simple product of the given two nonhomogeneous lines defines a joint equation of a line:",
          "The join: ¿quation of the homogeneous straight lines is obtained from (1) by putting e1 =,=0:",
          "The product of homogeneous lines (ii) is giving the standard form of the second degree homogeneous equation:",
          "Any point P(x, y) that satisfies first line a,x+by=0 or second line a,x+b,y=0 will also",
          "satisfies the joint homogeneous equation of (ii).",
          "The product of (iv) to constant quantity is giving the",
          "joint equation of the two first degree homogeneous equations in x and y",
          "real and coincident, if h2-ab=0. imaginary, if k2 -ab < 0.",
          "The lines (v) and (vi) are therefore first degree equations in x and y."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-7-30",
        "num": "28",
        "title": "Example 28",
        "problem": "Find two first degree straight lines in x and y when the second degree homogeneous equation is 5.x2+3x-8=0.",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-7-1",
        "exercise": "Exercise 7.1",
        "title": "Exercise 7.1",
        "description": "",
        "problems": [
          {
            "id": "ex-7-1-q1",
            "qNo": "1",
            "question": "For A(−1,3), B(2,1), and C(5,−1), show that |AB|+|BC|=|AC|.",
            "solution": "Using the distance formula: |AB|=√((2+1)²+(1−3)²)=√13; |BC|=√((5−2)²+(−1−1)²)=√13; |AC|=√((5+1)²+(−1−3)²)=√52=2√13. Therefore |AB|+|BC|=2√13=|AC|.",
            "diagram": null
          },
          {
            "id": "ex-7-1-q2",
            "qNo": "2",
            "question": "Find the midpoint of each segment: (a) P(10,20), Q(−12,−8); (b) P(a,−b), Q(−a,b); (c) P(1/2,−1/4), Q(3/4,4/7).",
            "solution": "Apply M=((x₁+x₂)/2,(y₁+y₂)/2). (a) M=(−1,6). (b) M=(0,0). (c) M=(5/8,9/56).",
            "diagram": null
          },
          {
            "id": "ex-7-1-q3",
            "qNo": "3",
            "question": "Find R(x,y) dividing PQ in the stated ratios: (a) P(1,2), Q(3,4), ratio 5:7; (b) P(3,4), Q(−6,2), ratio 3:−2; (c) P(−6,7), Q(5,−4), ratio 2/7:1.",
            "solution": "Use the section formula R=((n x₁+m x₂)/(m+n),(n y₁+m y₂)/(m+n)) for ratio m:n. (a) R=(11/6,17/6). (b) With signed ratio 3:−2, R=(−24,−2). (c) Rewrite 2/7:1 as 2:7; R=(−32/9,41/9).",
            "diagram": null
          },
          {
            "id": "ex-7-1-q4",
            "qNo": "4",
            "question": "Determine the ratio in which R divides PQ for the two coordinate sets shown in the textbook.",
            "solution": "For each set, use the x-coordinate section equation x_R=(n x_P+m x_Q)/(m+n) to solve for m:n, then verify the result with the y-coordinate. The second coordinate of the second printed R point is not legible in the scan, so that ratio cannot be stated reliably from the available page image.",
            "diagram": null
          },
          {
            "id": "ex-7-1-q5",
            "qNo": "5",
            "question": "Find each triangle’s centroid: (a) A(4,−2), B(−2,4), C(5,5); (b) A(3,5), B(4,6), C(3,−1); (c) A(1,1), B(−2,−2), C(4,5).",
            "solution": "The centroid is the coordinate-wise mean of the vertices. (a) G=(7/3,7/3). (b) G=(10/3,10/3). (c) G=(1,4/3).",
            "diagram": null
          }
        ],
        "pageStart": 178,
        "pageEnd": 212
      },
      {
        "id": "ex-7-2",
        "exercise": "Exercise 7.2",
        "title": "Exercise 7.2",
        "description": "",
        "problems": [
          {
            "id": "ex-7-2-q1",
            "qNo": "1",
            "question": "Find the distance between P(3,−2) and Q(−1,−5).",
            "solution": "d=√[(-1−3)²+(−5+2)²]=√(16+9)=5.",
            "diagram": null
          },
          {
            "id": "ex-7-2-q2",
            "qNo": "2",
            "question": "Find the point dividing the segment from P(2,−3) to Q(8,9) internally in the ratio 1:2.",
            "solution": "Section formula: R=((2x_P+x_Q)/3,(2y_P+y_Q)/3)=((4+8)/3,(-6+9)/3)=(4,1).",
            "diagram": null
          },
          {
            "id": "ex-7-2-q3",
            "qNo": "3",
            "question": "Find the midpoint of P(−4,6) and Q(8,−2).",
            "solution": "M=((−4+8)/2,(6−2)/2)=(2,2).",
            "diagram": null
          },
          {
            "id": "ex-7-2-q4",
            "qNo": "4",
            "question": "Find the centroid of the triangle with vertices (1,2), (4,−1), and (−2,5).",
            "solution": "G=((1+4−2)/3,(2−1+5)/3)=(1,2).",
            "diagram": null
          },
          {
            "id": "ex-7-2-q5",
            "qNo": "5",
            "question": "Find the equation of the line through (2,3) and (−1,−3).",
            "solution": "Slope m=(−3−3)/(−1−2)=2. Point-slope form gives y−3=2(x−2), so y=2x−1.",
            "diagram": null
          },
          {
            "id": "ex-7-2-q6",
            "qNo": "6",
            "question": "Find the slope of the line through (−2,5) and (4,−1), and state whether it is parallel or perpendicular to a line of slope 1.",
            "solution": "m=(−1−5)/(4+2)=−1. Since the product of slopes −1·1=−1, the lines are perpendicular.",
            "diagram": null
          },
          {
            "id": "ex-7-2-q7",
            "qNo": "7",
            "question": "Find the distance of (3,−2) from the line 4x−3y+5=0.",
            "solution": "d=|4(3)−3(−2)+5|/√(4²+(−3)²)=23/5.",
            "diagram": null
          },
          {
            "id": "ex-7-2-q8",
            "qNo": "8",
            "question": "Find the angle between two lines with slopes 2 and −1/3.",
            "solution": "tan θ=|(m₂−m₁)/(1+m₁m₂)|=|(-1/3−2)/(1−2/3)|=7. Therefore θ=tan^{−1}(7)≈81.87°.",
            "diagram": null
          },
          {
            "id": "ex-7-2-q9",
            "qNo": "9",
            "question": "Find the area of the triangle with vertices (0,0), (4,0), and (1,3).",
            "solution": "Using base 4 and height 3, area=(1/2)(4)(3)=6 square units.",
            "diagram": null
          }
        ],
        "pageStart": 178,
        "pageEnd": 212
      },
      {
        "id": "ex-7-3",
        "exercise": "Exercise",
        "title": "Exercise",
        "description": "",
        "problems": [],
        "pageStart": 178,
        "pageEnd": 212
      },
      {
        "id": "ex-7-4",
        "exercise": "Review Exercise 7",
        "title": "Review Exercise 7",
        "description": "",
        "problems": [],
        "pageStart": 178,
        "pageEnd": 212
      },
      {
        "id": "ex-7-5",
        "exercise": "Exercise 7.3",
        "title": "Exercise 7.3",
        "description": "",
        "problems": [],
        "pageStart": 178,
        "pageEnd": 212
      },
      {
        "id": "ex-7-6",
        "exercise": "Exercise 7.4",
        "title": "Exercise 7.4",
        "description": "",
        "problems": [
          {
            "id": "ex-7-4-q1",
            "qNo": "1",
            "question": "Find the intersection of each pair: (a) 2x+4y−10=0 and 5x−3y+1=0; (b) 2x+y−8=0 and 3x+2y−2=0.",
            "solution": "(a) Solve x+2y=5 and 5x−3y=−1: x=1, y=2. (b) From 2x+y=8 and 3x+2y=2, solve to obtain x=14, y=−20.",
            "diagram": null
          },
          {
            "id": "ex-7-4-q4",
            "qNo": "4",
            "question": "Find triangle areas: (a) P(0,0), P(2,4), P(−2,2); (b) P(−1,−2), P(2,5), P(5,2).",
            "solution": "Use one-half the absolute determinant of two side vectors. (a) Area=|2·2−4(−2)|/2=6. (b) The determinant from A is 3·4−7·6=−30, so area=15 square units.",
            "diagram": null
          },
          {
            "id": "ex-7-4-q5",
            "qNo": "5",
            "question": "Find the areas bounded by the vertices: (a) A(−3,6), B(3,2), C(6,0); (b) A(−2,4), B(3,−6), C(1,−2). Determine whether the vertices are collinear.",
            "solution": "Use the determinant area formula. (a) The slopes AB and BC both equal −2/3, so area=0 and the points are collinear. (b) The determinant is zero as well, so the area is 0 and the points are collinear.",
            "diagram": null
          }
        ],
        "pageStart": 178,
        "pageEnd": 212
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-8",
    "number": 8,
    "title": "Conics I",
    "titleUrdu": "",
    "pageRange": "Printed pages 213–240",
    "pageStart": 213,
    "pageEnd": 240,
    "sections": [
      {
        "id": "sec-8-1",
        "title": "8.1 Conics and Members of Its Family",
        "theory": "In each case, find an equation of a circle, when the center and radius are the following:\n\nIn each case, determine the equation of a circle using the given information:\n\nc. C(6-6), circumference passes through the origin.\n\nd. C(-9,-6), circumference passes through the point (-20,8).\n\nIn each case, find the center C(-g-f) and radius =√g+f-e of the following: a. x2+y2-8x-6y+9=0\n\nIn each case, find an equation of a circle which passes through the three points:\n\nIn each case, find an equation of a circle which\n\na. contains the point (2,6),(6,4) and has its center on the line 3x+2y-1-0.\n\nb. contains the point (4,1),(6,5) and has its center on the line 4x+y-16=0.\n\nFind an equation of a circle which passes through the points\n\na. (0,0),(0,3) and the line 4x-5y=0 is tangent to it at (0,0).\n\nb. (0,-1),(3,0) and the line 3x+y=9 is tangent to it at (3,0). Find an equation of a circle that is concentric to circle\n\na. 2x+2y2+16x-7y=0 and is tangent to the y-axis.\n\nb. x2+y2-8x+4=0 and is tangent to the line x+2y+6=0.\n\nc. x2+y2+6x-10y+33=0 and is touching the x-axis.\n\nFind equation of circle which passes through origin and whose intercepts are on the co",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-8-2",
        "title": "8.2 Circle",
        "theory": "A circle is a shape that has a continuous and constant curve. Though it is always curving; it has an algebraic expression that describes its nature.\n\n\"The set of all points in the plane in such a way distances from a fixed point in that plane (called the center) is equal to a fixed distance (called the radius) of the circle. Derivation of Circle Equation: This definition helps us in developing a standard form of the equation of a circle.\n\nLet C (h, k) be a fixed point at the center of the circle and r is the radius of the circle and P(x, y) is any one of the collection of points on the circumference of the circle that gives the distance from the fixed point C(h, k) which is called the radius of a circle. The position vectors of P and C relative to origin are respectively. OP (x,y), OC=(h,k)\n\nFrom the Figure 8.2, the distance from the center C to point P is the fixed distance equals the radius of the circle:\n\nThe standard form of a circle with radius r and center (A, A) is:\n\nIf the center of the circle is at the origin (h, k)=(0,0), then the circle equation (ii) becomes:\n\nDetermine the equation of a circle with center at (-2,1) and radius =)\n\nSolution The standard form of the equation of a circle is (x-)+(−k)2 = r2\n\nWhere (h, k) are the coordinates of the centre and is the radius.\n\nsubstitute these values into the standard equation.\n\nThe arrangement of the general equation of the second degree in x and y that may represent a circle through the following procedure:\n\nThe general equation of the second degree in variables x and y is:\n\nDivide out both sides of equation (i) by a to obtain:\n\nThe rearranged equation (ii) of the general equation of the second degree (i) in x and y gives the general equation of a circle if and only if\n\nx2+2gx+g2 −g2 + y2+2f y+f-f+c=0 Adding and subtracting gandƒa in equation (ii) (x+8)2+(y+ƒ)2 = g2 + f2-c\n\nThe locus of a point (x, y) which moves in such a way that its distance from a fixed point (-g.-) is constant and equals √g2+f-c. This of course represents a circle.\n\nFor general equation of circle x + y2+2x+2y+c=0\n\nCenter and Radius: The coordinates of the center are (-g,-) and the radius is r = √(-8)2+(-ƒ)2-c.\n\nIndependent Constant: The general equation contains three independent constants gf and e. They\n\ncan be determined from the three independent conditions.\n\nIf g2+ƒ3-c>0, then, the circle is real and different from zero.\n\nIf g2 +ƒ3-c=0, then, the circle shrinks into a point (-g,-). It is called point circle.\n\nIf g2+ƒ3-c<0, then, the circle is imaginary or virtual.\n\nThe coefficients of x is equal to the coefficients of, and there is no term containing xy and the square of the radius r220.\n\nSolution The given circle equation is rearranged to obtain:\n\nThe circle equation (i) is compared to the general form of a an equation of circle to obtain the values of\n\nThe center and radius of the given circle are therefore:\n\nB. two points and having its centre on a given line\n\nC. two points and equation of tangent at one of these points is known D. two points and touching a given line\n\nA. Equation passing through three non-collinear points. Consider the general equation a circle is given by x2+y+2gx+2y+c=0\n\nIf the given circle is passing through three non-collinear points, say, A(5,3),B(x,,,) and C(,,,) then these points must satisfy the general equation of a circle. Now put the above three points in the given equation of a circle, Le.:\n\nSolution The required equation of a circle is x+y+2gx+2y+c=0\n\nwhich passes through the three points A(1,0), B(0,-6) and C(3,4), which gives a system of three lines equations in three unknowns g, and e\n\nThe system of three linear equation (11) in matrix form\n\nReduce this augmented matrix in an echelon form to obtain:\n\nThird equation of the system (ii) is giving c = SM\n\nwhich is used in second and first equations to\n\nare used in equation (ii) to obtain the required circle\n\nEquation of circle passing through two points and having its centre on a given line Consider the general equation a circle is given by\n\nIf the given circle is passing through two points, say A(x) and\n\nB(x), then these points must satisfy the general equation of a circle. Now put these two points in the given equation of a circle, Le.\n\nAlso, the given straight line ax+by+c=0 passes through the enter (-g.-f) of the circle.\n\nE 4 Find the equation of a circle which passes through the points A(3,1) and B(2,2) having its center on the line x+3=0.\n\nwhich passes through the two points A(3,1) and B(2,2) that gives a system of two linear equations\n\nIf the center (-g.-1) of the circle lies on the linex+y-3=0, then the line x+y-3=0 becomes: -g-/-3=0⇒ g+ƒ=-3\n\nThe combination of equations (ii) and (iii) is giving the system of three linear equations in three unknown gande",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-8-3",
        "title": "8.3 Tangents and Normal",
        "theory": "If a secant PQ of a circle is moved upward about one of its points of intersection P, then the second point of intersection Q is moving gradually along the curve that tends to coincide with P. The limiting position PT of PQ is then called the tangent to the circle at the point P.\n\nThe point of the circle at which a tangent meets the circle is called point of contact (Say P) of the tangent.\n\nThe normal at a contact point P to a circle (or conic) is the straight line PR perpendicular to the tangent PT to the circle (or conic) at that point P.\n\nwhich develops a system of two nonlinear equations:\n\nThe solution set {(x, y)) of the nonlinear system of equations (iii)exists only, if the curves of the system (iii) are intersecting. That set of points of intersection ((x, y)) is the solution set, can be found by solving the nonlinear system (iii) simultaneously.\n\nThe line (ii) is used in a circle (i) to obtain the quadratic equation in x\n\nThe equation (iv) being a quadratic equation in x, gives a set of two values, and x, of which will be used in a line (ii) to obtain a set of two y values ; and y-\n\nThe solution set ((x.),(5, 3)} of the system (iii) is of course a set of points of intersection\n\nThe points of intersection of the system (iii) are real, coincident or imaginary, according as the roots of the quadratic equation (iv) are real, coincident or imaginary or according as the discriminate of the quadratic equation (iv)\n\nSolution The equations of the line and circle are: 3x-4y+20=0\n\nThe line (i) is used in a circle ()to obtain the x-coordinates of the points of intersection:\n\nare used in the line() to obtain the y-coordinates:\n\nTo determine the position of a line with respect to the circle, we need to find its distance from centre of a circle and compare it with radius then:\n\ni. If distance is less than the radius, the line will intersect\n\nii. If the distance is equal to the radius, then the line will\n\niii. If the distance is greater than the radius, the line will\n\nLet AB be the straight line y=x+e that intersects the\n\ncircle x2+ya\" at points P and Q respectively.\n\nJoin OP and put it by OP-a, which is the radius of a\n\ngiven circle. Draw OM perpendicular on PQ. If OM is perpendicular to PQ, then, the perpet\n\ndistance OM from O(0,0) on a secant line mux-y+c=0 (line PQ) is: OM\n\nFrom the right-angled triangle OMP, it is known that:\n\nThe secant line PQ is 2 times of OM, and the length of the intercept PQ is therefore:\n\nCondition of Tangency: The line y=mx+c touches the circle x+y=a\", if the length of the in\n\nThe equation (ii) is the required condition at which the line y = mx + e touches the circle x+y=a. Example 8 Find the length of the chord joining the points P and Q on the line +1 which cuts\n\nthe circle x2+22. Show that if the line touches the circle, then a\n\nIf PQ is the chord of a circle x2+y=2, and PQ is 2 times of MP, then the length of the chord PQ through result (i) is:\n\nIf the given line touches the circle x+y=r, then, the length of the chord PQ is going to be zero:\n\nSolution The center of the given circle is C-g.-)=C(-2,1) and the line x-y+2=0 (line AB intersects the circle at points P and Q and M(x,y) is the middle point of the chord PQ. Join C and\n\nthat develops a line CM perpendicular to chord PQ.\n\nIf M lies on line AB, then, the line equation x-y+2=0 becomes:\n\nThe slopes of the lines (i) and CM are respectively:\n\nIf CM is perpendicular to AB, then the product of their slopes equals -1:\n\nThe equations (i) and (ii) are solved to obtain the coordinates of the middle point M:\n\nIf m is the slope of the tangent line to the circle x+ya (1)\n\nthen the equation of that tangent line is of the form\n\nHere is to be calculated from the fact that the line (ii) is tangent to the circle (i). The line (ii) used in circle (i) to obtain the quadratic equation in x:\n\nIf the line (i) touches the circle (1), then the quadratic equation (iii) has coincident roots ►\n\nwhich the discriminant of the quadratic equation (iii) equals zero:\n\nEquation (iv) is the condition of tangency. The value of c from equation (iv) is used in the line to obtain the required equation of the tangent:\n\nThe equation of any tangent to the circle x+y=a in the slope form is: y=mx±√1+m2 (vi) The line y=mx+should touch the circle x+y=a\" under condition: e=tal+m (vii) The interpretation of result (v) is that the line x+my+=0 should touch the circle + a under condition: a2(+m2)-n2=0⇒n=±a√l2 + m2\n\nThe interpretation of result (v) that the line x2+y+2gx+2y+c=0 under condition:\n\nLet y=mxta√1+m2 be a tangent to a circle (1) at a point (x, y), if the circle equation (i) is identical to xx+yya, then the coefficients of like terms of y=mx±a√1+m xx;+y};=a2 ⇒yy=-xx,+ are compared to obtain the point of contact:\n\nSolution The slope of the line x+y+c=0 ism-1. The value of c at which the line x+y+c=0 will touch the given circle x2+y=64 is: e=ta/1+m2, result (vii)\n\nThe required tangent line that should touch the given circle is:\n\nThe point of contact through result (x) is: (.)-\n\nIf 4(x) is a point lying on the circle (i), then the circle (i) becomes:\n\nIf r, and r, are the position vectors of A and the center C(-g.-) of the circle relative to origin x=(x,y)=xi+y1j. 5=(-8.-f)--gi-fi then, from the Figure 8.11:\n\nLet P(x, y) be any point on the tangent line AT, whose\n\nThe equation of tangent to the circle (i) is obtained if AP is perpendicular to CA for which the dot product in between the vectors AP and AC equals zero:\n\nThe tangent equation to the circle x+y=a\" at a point (x,.,) through result (iii) is:\n\nIf C(— g. – f) is the center of the circle and A(x) is a contact point, then the slope\n\nthe required normal line develops the normal line CA at 4(x,y):\n\nThe normal equation to the circle x+y=a at a point A(x,y) through result (v) is:\n\nResult ((vi)is used to obtain the normal equation to the given circle:\n\nSolution Result ((iii) is used to obtain the tangent line to the given circle:\n\nResult (v) is used to obtain the normal line to the given circle: x(y; +/)− y(x+8)+(x−)=0\n\nThe procedure for finding the length of the tangent drawn from\n\nthe external point P(x,y) to the circle x2+y+2gx+2y+c=0is\n\nLet P(x,y,) be the given external point and PT be one of the two tangents drawn from point P to the circle\n\nJoin CP and CT. C(-g. f) is the center of the circle (i) and\n\nFrom the right-angled triangle PTC, the length of the tangent PT drawn from point P to the given circle is:\n\nThe length of the tangent drawn from the point P(x,.,) to the circle x+y= q2 PT-√x+x-a2\n\nThe lengths of the two tangents drawn from the point P(x,y) on the given circle are equal. Example 13 Find the length of the tangent drawn from the point P(3,4) on the circles\n\na. If PT is the tangent drawn from the point P(3,4) on the\n\ngiven circle, then, the length of the tangent PT on the given circle through result (iii) is:\n\nIf PT is the tangent drawn from the point P(3,4) on the given circle, then, the length of the tangent PT on the given circle through result (ii) is:\n\nIf y=mx+al+m is any tangent to the circle x+y=a\", then the tangent line that passes through the point (x,y) is y = mx,+a√1+m?\n\nTaking square on both sides of equation (i) (y-mx)=a\" (1+m2)\n\nthat gives the quadratic equation in m: m2(x-2)-2mx, y, +(3,7 −a\") = 0\n\nThis quadratic equation (ii) gives two values of m that two values of m represent the slopes of\n\nthe required two tangents on the given circle.\n\nThe tangents are real and different, real and coincident or imaginary or according discriminant of the quadratic equation (ii):\n\nor according as the point P(x3) lies outside, on, or inside the circle x2+ y2 =a2.\n\nIn general, two tangent can also be drawn from the point P(x.) to the circle x2+y2+2gx+2ƒy+c=0.\n\nSolution If y=mx+c=mx+al+m2 is any tangent to the circle x+y=16, then the number of tangents through result (ii)\n\nMentechmus was a Greek mathematician. He was teacher of Alexander the Great and a friend of Ploto. He was the first person who introduced the conic section and investigate ellipse, parabola and hyperbola. He also gave the solution to the problem of doubling the cube. He introduced parabola as - Lx where 'L' is a constant called the latus rectum\n\nnough he was not acute of the fact that any equation in two unknowns determines a curve. He deliberately derived these properties of conic section and other properties also. By using these information it has not possible to find a solution to the problem of the duplication of the cube by solving for the point at which two parabolas intersect. Menaechmus's work an conic section is known as primary work for conic section.\n\nIn each case, find the tangent and normal equations\n\na. at a point (1,2) to the circle x+y=5. b. at a point (-3,-2) to the circle x2+y=13. c. at a point (4,1) to the circle x2+-4x+2y-3=0.\n\na. at a point (cos 60°, sin 60°) to the circle 36(x+y)=13.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-8-4",
        "title": "8.4 Properties of a Circle",
        "theory": "There are some properties of a circle that are listed as under.\n\nand PQ be any chord of a circle, whose end points are P(x,;) and\n\nIf PQ is a chord of the circle, then P and Q are the points\n\nThe subtraction of these two circles equations gives the slope\n\nIf the center of the circle is C(-g-f) and the midpoint of the chord PQ is\n\nthen the slope of the perpendicular line CD is:\n\nFrom the Figure 8.14 the chord PQ and the line CD are perpendicular if and only if the product of their slopes equals -1:\n\nthe perpendicular bisector of any chord PQ of a circle passes through the center of the circle. This is our second property.\n\nthe line joining the two points of the circle that touches the center of the circle is called the diameter of the circle. This diameter acts as the perpendicular bisector to the chord PQ, if the\n\ndiameter of a circle bisects the chord PQ. This is our third property. The proof is similar to property first, but the graphical view is shown in the Figure 8.14.\n\nare the end points of the chord AB of the circle\n\n(a). the line from the center of the circle is perpendicular to AB, also bisects the cherd AB.\n\nthe line from the center of the circle to the midpoint of the chord AB is perpendicular to the chord\n\n(c). the perpendicular bisector CD of the chord AB pass though the center of the given circle.\n\nSolution The equation of the circle with center\n\nslopes the chord AB and the perpendicular line CD are respectively.\n\nThe chord AB and the line CD are perpendicular if and only if the product of their slopes equals –\n\nTherefore, CD is perpendicular bisector of the chord AB. This result is automatically valid fo parts b and c.\n\nIf the perpendicular distances form the center of a circle to its two chords are equal, then the chords are\n\nLet the circle equation with center C-g.-) is:\n\nIf AB and DE are the two chords of the circle(i), then the coordinates of the end points of the chord AB and DE are respectively:\n\nFrom the Figure 8.15, it is clear that the perpendicular distance d,= CP from the center C on the chord AB equals\n\nthe perpendicular distance d, =CQ from C on the chord\n\nDE, if and only if the chords AB and DE are with equal lengths: AB=DE\n\nThus, the chords AB and DE are equidistant from C on the circle (i) if and only if d1 =d;\n\nIn similar manner, the chords AB (join A to D) and BE (join B to E) are congruent chord the perpendicular distance d, = CR from C on the chord AD equals the perpendicular d, CS from\n\nSolution The circle equation with center C(0,0) is: x2+ y2=4\n\nIf AB and DE are the two chords of the circle (i), whose coordinates are respectively:\n\nFrom the Figure 8.16, it is clear that the chords AB and DE are with equal length:\n\nThus, the two chords AB and DE are equal. For equidistant, the procedure is as under:\n\nThe equations of the chords AB and DE (through two-\n\nThe perpendicular distance d, from C(0,0) on the chord AB is: d\n\nThe perpendicular distance d, from C(0,0) on the chord DE is: d\n\nThe perpendicular distance d, from C(0,0) on the chord AB is equal to the perpendicular\n\nThus, the chords AB and DE are equidistant from the center C(0,0) of the circle (i) 8.4.5 Measure of the central angle of a minor arc is double the measure of the\n\nangle subtended by the corresponding major are\n\nand the minor are BC subtended the angle from the center of the circle is BOC.\n\nThe are BC is the minor are of the circle (i), whose coordinates are B(--) and C(-3).\n\nare which is two times the angle subtended by the major are: BOC=2<BAC\n\nIf P(x,y) is any point on the semicircle and BA is fixed as the diameter of the circle() on the x-axis, whose coordinates are A (a, 0) and B (-a, 0), then the point P(x, y) lies on the circle (i) that changes the circle equation to:+y?!\n\nJoin PA and PB that develops a right angle ZAPB. The angle ZAPB is a right angle, if AP and PB are perpendicular to each other, for which the slopes of AP and PB are respectively:\n\nThus, PA and PB are perpendicular and the angle ZAPB=90° is of course a right-angle. If ZAPB=90°, then P is a point lies on the semicircle, for which the Pythagorean rule PA+PBAB\n\nwhich is a circle, P may lie on the upper or the lower semicircle.\n\nStandard Form of a Circle: The standard form of a circle with radius r and center C(h, k) is: (x − h)2 + (p −k)2 = p\n\n→ General Form of a Circle: The general form of a circle with radius =√(-g)+(-c and\n\nThe coefficient of x is equal to the coefficient of y', and there is no term containing xy and the square of the radius is 20.\n\nIf g2+ƒ-e> 0, then the circle is real and different from zero.\n\nIf g2+f-c=0, then the circle shrinks to a point (-g.-). It is called a point circle.\n\nIfg+/- <0, then the circle is imaginary or virtual.\n\nThe condition at which the line y=mx+e should touch the circle x+y=ais: c=±a√1+m The equation of any tangent to the circle x+y=a'in the slope-form is: y=muxta√1+m The condition at which the line Er+my+n-0 should touch the circle x2+ y2='is:\n\nThe condition at which the line lx+my+0 should touch the circle. x+y+2gx+2y+c=0is: (c-f)+2fgim+(c-g\")m'-2n(gl+ fm)+n-0\n\nThe tangent equation to the circle x+y=a\" at a point A(5.3) is: x+3y=\n\nThe normal equation to the circle \"+y+2gx+2f+c=0 at a point A(x,,,,) is: x(;+S)−3{x+g)+(x,−6)=0\n\nThe normal equation to the circle x+y=a at a point A(x,y) is: x-3x=0\n\nThe length of the tangent drawn from the point P(x,y) to the circle x+y+2g+2f+c=0",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-8-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Determine the equation of a circle with center at (-2,1) and radius =)",
        "given": "",
        "method": "",
        "steps": [
          "Solution The standard form of the equation of a circle is (x-)+(−k)2 = r2",
          "Where (h, k) are the coordinates of the centre and is the radius.",
          "substitute these values into the standard equation.",
          "8.2.2 General form of an equation of a circle",
          "The arrangement of the general equation of the second degree in x and y that may represent a circle through the following procedure:",
          "The general equation of the second degree in variables x and y is:",
          "Divide out both sides of equation (i) by a to obtain:",
          "The rearranged equation (ii) of the general equation of the second degree (i) in x and y gives the general equation of a circle if and only if",
          "x2+2gx+g2 −g2 + y2+2f y+f-f+c=0 Adding and subtracting gandƒa in equation (ii) (x+8)2+(y+ƒ)2 = g2 + f2-c",
          "The locus of a point (x, y) which moves in such a way that its distance from a fixed point (-g.-) is constant and equals √g2+f-c. This of course represents a circle.",
          "For general equation of circle x + y2+2x+2y+c=0",
          "Center and Radius: The coordinates of the center are (-g,-) and the radius is r = √(-8)2+(-ƒ)2-c.",
          "Independent Constant: The general equation contains three independent constants gf and e. They",
          "can be determined from the three independent conditions.",
          "If g2+ƒ3-c>0, then, the circle is real and different from zero.",
          "If g2 +ƒ3-c=0, then, the circle shrinks into a point (-g,-). It is called point circle.",
          "If g2+ƒ3-c<0, then, the circle is imaginary or virtual.",
          "The coefficients of x is equal to the coefficients of, and there is no term containing xy and the square of the radius r220."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Find the center and radius of a circle 45x+45 y1-60y+36x+19=0.",
        "given": "",
        "method": "",
        "steps": [
          "The circle equation (i) is compared to the general form of a an equation of circle to obtain the values of",
          "The center and radius of the given circle are therefore:",
          "8.2.3 The equation of a circle passing through",
          "B. two points and having its centre on a given line",
          "C. two points and equation of tangent at one of these points is known D. two points and touching a given line",
          "A. Equation passing through three non-collinear points. Consider the general equation a circle is given by x2+y+2gx+2y+c=0",
          "If the given circle is passing through three non-collinear points, say, A(5,3),B(x,,,) and C(,,,) then these points must satisfy the general equation of a circle. Now put the above three points in the given equation of a circle, Le.:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Find the equation of a circle which passes through the three points A(1,0), B(0,–6) and C(3,4)",
        "given": "",
        "method": "",
        "steps": [
          "which passes through the three points A(1,0), B(0,-6) and C(3,4), which gives a system of three lines equations in three unknowns g, and e",
          "The system of three linear equation (11) in matrix form",
          "Reduce this augmented matrix in an echelon form to obtain:",
          "Third equation of the system (ii) is giving c = SM",
          "which is used in second and first equations to",
          "are used in equation (ii) to obtain the required circle",
          "Equation of circle passing through two points and having its centre on a given line Consider the general equation a circle is given by",
          "If the given circle is passing through two points, say A(x) and",
          "B(x), then these points must satisfy the general equation of a circle. Now put these two points in the given equation of a circle, Le.",
          "Also, the given straight line ax+by+c=0 passes through the enter (-g.-f) of the circle.",
          "E 4 Find the equation of a circle which passes through the points A(3,1) and B(2,2) having its center on the line x+3=0.",
          "Solution The required equation of a circle is x+y+2gx+2y+c=0",
          "which passes through the two points A(3,1) and B(2,2) that gives a system of two linear equations",
          "If the center (-g.-1) of the circle lies on the linex+y-3=0, then the line x+y-3=0 becomes: -g-/-3=0⇒ g+ƒ=-3",
          "The combination of equations (ii) and (iii) is giving the system of three linear equations in three unknown gande",
          "Reduce this augmented matrix in an echelon form to obtain the unknowns and c",
          "Third equation of the system (iv) is giving e-4 which is used in second and first equations t obtain the values off=-1 and g=-2.",
          "The values of g = -2, -1 and c = 4 are used in equation (i) to obtain the required circ equation: x+y-4x-2y+4-0",
          "The equation of a circle passing through two points and equation of tangent at one points is known",
          "Consider the general equation a circle is given by",
          "If the given circle is passing through two points, say A(x) and B(x), then these points must satisfy the general equation of a circle. Now put these two points in the given equation of a circle, Le.:",
          "touches the circle at one point, as shown in the given diagram,",
          "and it is clear from the diagram that the distance of a given point from the center (-g.) must be eq the radius of the circle."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-4",
        "num": "5",
        "title": "Example 5",
        "problem": "Find the equation of a circle which passes through the two points A(0,-1) and B(3,-3) and 3x-2y-2-0 is the tangent line on the circle at a point A(0,-1).",
        "given": "",
        "method": "",
        "steps": [
          "and the slope of the tangent line 3x-2y-2-0 is",
          "TCA is perpendicular to the tangent line 3x-2y-2-0, then the product of their slopes equals to (-1):",
          "The equations (i) and (ii) are solved to obtain the values of --2 and",
          "The equation of a circle passing through two points and touching a given line"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-5",
        "num": "6",
        "title": "Example 6",
        "problem": "Find the equation of a circle which passes through the two points (0,0) and 8(4,0) and is touching a line 3x+4y+4=0.",
        "given": "",
        "method": "",
        "steps": [
          "(0,0) and B(4,0) are the two points lie on equals the radius of the circle from the",
          "The radius of the required circle is r=|CA|-√4+ and the center is C(2, 4).",
          "For the values of k, the perpendicular distance from the center (2, k) on the line 3r +4y+ 4 = 0 equals the radius of the circle:",
          "The equations of the circles with the above centers and radii are the following:",
          "In each case, find an equation of a circle, when the center and radius are the following:",
          "In each case, determine the equation of a circle using the given information:",
          "c. C(6-6), circumference passes through the origin.",
          "d. C(-9,-6), circumference passes through the point (-20,8).",
          "In each case, find the center C(-g-f) and radius =√g+f-e of the following: a. x2+y2-8x-6y+9=0",
          "In each case, find an equation of a circle which passes through the three points:",
          "In each case, find an equation of a circle which",
          "a. contains the point (2,6),(6,4) and has its center on the line 3x+2y-1-0.",
          "b. contains the point (4,1),(6,5) and has its center on the line 4x+y-16=0.",
          "Find an equation of a circle which passes through the points",
          "a. (0,0),(0,3) and the line 4x-5y=0 is tangent to it at (0,0).",
          "b. (0,-1),(3,0) and the line 3x+y=9 is tangent to it at (3,0). Find an equation of a circle that is concentric to circle",
          "a. 2x+2y2+16x-7y=0 and is tangent to the y-axis.",
          "b. x2+y2-8x+4=0 and is tangent to the line x+2y+6=0.",
          "c. x2+y2+6x-10y+33=0 and is touching the x-axis.",
          "Find equation of circle which passes through origin and whose intercepts are on the co",
          "If a secant PQ of a circle is moved upward about one of its points of intersection P, then the second point of intersection Q is moving gradually along the curve that tends to coincide with P. The limiting position PT of PQ is then called the tangent to the circle at the point P.",
          "The point of the circle at which a tangent meets the circle is called point of contact (Say P) of the tangent.",
          "The normal at a contact point P to a circle (or conic) is the straight line PR perpendicular to the tangent PT to the circle (or conic) at that point P.",
          "8.3.1 The condition when a line intersect the circle",
          "which develops a system of two nonlinear equations:",
          "The solution set {(x, y)) of the nonlinear system of equations (iii)exists only, if the curves of the system (iii) are intersecting. That set of points of intersection ((x, y)) is the solution set, can be found by solving the nonlinear system (iii) simultaneously.",
          "The line (ii) is used in a circle (i) to obtain the quadratic equation in x",
          "The equation (iv) being a quadratic equation in x, gives a set of two values, and x, of which will be used in a line (ii) to obtain a set of two y values ; and y-",
          "The solution set ((x.),(5, 3)} of the system (iii) is of course a set of points of intersection",
          "The points of intersection of the system (iii) are real, coincident or imaginary, according as the roots of the quadratic equation (iv) are real, coincident or imaginary or according as the discriminate of the quadratic equation (iv)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-6",
        "num": "7",
        "title": "Example 7",
        "problem": "Find the points of intersection of the line 3x-4y+20=0 and the circle x2+y=25.",
        "given": "",
        "method": "",
        "steps": [
          "The line (i) is used in a circle ()to obtain the x-coordinates of the points of intersection:",
          "are used in the line() to obtain the y-coordinates:",
          "8.3.2 Condition when a line touches the circle +y=",
          "To determine the position of a line with respect to the circle, we need to find its distance from centre of a circle and compare it with radius then:",
          "i. If distance is less than the radius, the line will intersect",
          "ii. If the distance is equal to the radius, then the line will",
          "iii. If the distance is greater than the radius, the line will",
          "Let AB be the straight line y=x+e that intersects the",
          "circle x2+ya\" at points P and Q respectively.",
          "Join OP and put it by OP-a, which is the radius of a",
          "given circle. Draw OM perpendicular on PQ. If OM is perpendicular to PQ, then, the perpet",
          "distance OM from O(0,0) on a secant line mux-y+c=0 (line PQ) is: OM",
          "From the right-angled triangle OMP, it is known that:",
          "The secant line PQ is 2 times of OM, and the length of the intercept PQ is therefore:",
          "Condition of Tangency: The line y=mx+c touches the circle x+y=a\", if the length of the in",
          "The equation (ii) is the required condition at which the line y = mx + e touches the circle x+y=a. Example 8 Find the length of the chord joining the points P and Q on the line +1 which cuts",
          "the circle x2+22. Show that if the line touches the circle, then a",
          "If PQ is the chord of a circle x2+y=2, and PQ is 2 times of MP, then the length of the chord PQ through result (i) is:",
          "If the given line touches the circle x+y=r, then, the length of the chord PQ is going to be zero:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-7",
        "num": "9",
        "title": "Example 9",
        "problem": "Find the coordinates of the middle point of the chord which the circle x2+y+4x-2y-30 cuts off on the line x-y+2=0.",
        "given": "",
        "method": "",
        "steps": [
          "that develops a line CM perpendicular to chord PQ.",
          "If M lies on line AB, then, the line equation x-y+2=0 becomes:",
          "The slopes of the lines (i) and CM are respectively:",
          "If CM is perpendicular to AB, then the product of their slopes equals -1:",
          "The equations (i) and (ii) are solved to obtain the coordinates of the middle point M:",
          "Thus, the coordinates of the middle point is M",
          "8.3.3 The equation of a tangent to a circle in slope form",
          "If m is the slope of the tangent line to the circle x+ya (1)",
          "then the equation of that tangent line is of the form",
          "Here is to be calculated from the fact that the line (ii) is tangent to the circle (i). The line (ii) used in circle (i) to obtain the quadratic equation in x:",
          "If the line (i) touches the circle (1), then the quadratic equation (iii) has coincident roots ►",
          "which the discriminant of the quadratic equation (iii) equals zero:",
          "Equation (iv) is the condition of tangency. The value of c from equation (iv) is used in the line to obtain the required equation of the tangent:",
          "The equation of any tangent to the circle x+y=a in the slope form is: y=mx±√1+m2 (vi) The line y=mx+should touch the circle x+y=a\" under condition: e=tal+m (vii) The interpretation of result (v) is that the line x+my+=0 should touch the circle + a under condition: a2(+m2)-n2=0⇒n=±a√l2 + m2",
          "The interpretation of result (v) that the line x2+y+2gx+2y+c=0 under condition:",
          "Let y=mxta√1+m2 be a tangent to a circle (1) at a point (x, y), if the circle equation (i) is identical to xx+yya, then the coefficients of like terms of y=mx±a√1+m xx;+y};=a2 ⇒yy=-xx,+ are compared to obtain the point of contact:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-8",
        "num": "10",
        "title": "Example 10",
        "problem": "For what value of e, the line x+y+c=0 will touch the circle x+y=64? Use that value of c to find the tangent that should touch the given circle. Find also the contact point.",
        "given": "",
        "method": "",
        "steps": [
          "The required tangent line that should touch the given circle is:",
          "The point of contact through result (x) is: (.)-",
          "8.3.4 The equations of tangent and normal to a circle at a point",
          "If 4(x) is a point lying on the circle (i), then the circle (i) becomes:",
          "If r, and r, are the position vectors of A and the center C(-g.-) of the circle relative to origin x=(x,y)=xi+y1j. 5=(-8.-f)--gi-fi then, from the Figure 8.11:",
          "Let P(x, y) be any point on the tangent line AT, whose",
          "The equation of tangent to the circle (i) is obtained if AP is perpendicular to CA for which the dot product in between the vectors AP and AC equals zero:",
          "The tangent equation to the circle x+y=a\" at a point (x,.,) through result (iii) is:",
          "If C(— g. – f) is the center of the circle and A(x) is a contact point, then the slope",
          "the required normal line develops the normal line CA at 4(x,y):",
          "The normal equation to the circle x+y=a at a point A(x,y) through result (v) is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-9",
        "num": "11",
        "title": "Example 11",
        "problem": "Find the equations of the tangent and normal to the circle x+y=25 at a point (3, 4). Solution Result ((ix) is used to obtain the tangent equation to the given circle:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-10",
        "num": "12",
        "title": "Example 12",
        "problem": "Find the equations of the tangent and normal to the circle x2+-2x+4y+3=25 at a point (2,-3).",
        "given": "",
        "method": "",
        "steps": [
          "Result (v) is used to obtain the normal line to the given circle: x(y; +/)− y(x+8)+(x−)=0",
          "8.3.5 Length of a tangents to a circle from a given external point",
          "The procedure for finding the length of the tangent drawn from",
          "the external point P(x,y) to the circle x2+y+2gx+2y+c=0is",
          "Let P(x,y,) be the given external point and PT be one of the two tangents drawn from point P to the circle",
          "Join CP and CT. C(-g. f) is the center of the circle (i) and",
          "From the right-angled triangle PTC, the length of the tangent PT drawn from point P to the given circle is:",
          "The length of the tangent drawn from the point P(x,.,) to the circle x+y= q2 PT-√x+x-a2",
          "The lengths of the two tangents drawn from the point P(x,y) on the given circle are equal. Example 13 Find the length of the tangent drawn from the point P(3,4) on the circles",
          "a. If PT is the tangent drawn from the point P(3,4) on the",
          "given circle, then, the length of the tangent PT on the given circle through result (iii) is:",
          "If PT is the tangent drawn from the point P(3,4) on the given circle, then, the length of the tangent PT on the given circle through result (ii) is:",
          "8.3.6 Two tangents drawn to a circle from an external point are equal in length",
          "If y=mx+al+m is any tangent to the circle x+y=a\", then the tangent line that passes through the point (x,y) is y = mx,+a√1+m?",
          "Taking square on both sides of equation (i) (y-mx)=a\" (1+m2)",
          "that gives the quadratic equation in m: m2(x-2)-2mx, y, +(3,7 −a\") = 0",
          "This quadratic equation (ii) gives two values of m that two values of m represent the slopes of",
          "the required two tangents on the given circle.",
          "The tangents are real and different, real and coincident or imaginary or according discriminant of the quadratic equation (ii):",
          "or according as the point P(x3) lies outside, on, or inside the circle x2+ y2 =a2.",
          "In general, two tangent can also be drawn from the point P(x.) to the circle x2+y2+2gx+2ƒy+c=0."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-11",
        "num": "14",
        "title": "Example 14",
        "problem": "Find the equations of the tangents drawn from the point (6,4) to the circle x2+ y2=16.",
        "given": "",
        "method": "",
        "steps": [
          "Mentechmus was a Greek mathematician. He was teacher of Alexander the Great and a friend of Ploto. He was the first person who introduced the conic section and investigate ellipse, parabola and hyperbola. He also gave the solution to the problem of doubling the cube. He introduced parabola as - Lx where 'L' is a constant called the latus rectum",
          "nough he was not acute of the fact that any equation in two unknowns determines a curve. He deliberately derived these properties of conic section and other properties also. By using these information it has not possible to find a solution to the problem of the duplication of the cube by solving for the point at which two parabolas intersect. Menaechmus's work an conic section is known as primary work for conic section.",
          "In each case, find the tangent and normal equations",
          "a. at a point (1,2) to the circle x+y=5. b. at a point (-3,-2) to the circle x2+y=13. c. at a point (4,1) to the circle x2+-4x+2y-3=0.",
          "In each case, find the tangent and normal equations",
          "a. at a point (cos 60°, sin 60°) to the circle 36(x+y)=13.",
          "b. at a point (2cos 45°, 2sin 45°) to the circle x+y=4. c. at a point (cos 30°, sin 30°) to the circle x + y2=1",
          "the line 1x+my+n=0 touches the circle x2+y2=a2? b. the line x+y+n=0 touches the circle x2+y=97 c. the line 2x+2y+n=0 touches the circle x2+y=81? For what value of c",
          "a. the line y=mx+c touches the circle x + y2 = a?? b. the line y=-x+c touches the circle x + y2=9?",
          "Find the condition at which the line Ix+my+n=0 touches the circle x+y+2gx+2y+c=0. For what value of n",
          "a. the line 3x+4y+n=0 touches the circle x2+y-4x-63-12-07",
          "b. the line x-2y+n=0 touches the circle x+y2+3x+6y-5-0?",
          "c. the line 2x+y+n=0 touches the circle x+y2-2x-10y+21=0?",
          "If the tangent length from the point P to the circle xya\" is equal to the perpendicular distance from P to the line Ex+my+n=0, then find out the locus of P.",
          "If the length of the tangent line from the point P to the circle x+y=9 is equal to the perpendicular distance form P to the line 3x+4y+3=0.",
          "b. If the length of the tangent line from the point P to the circle + y2 = 25 is equal to perpendicular distance form P to the line 4x+3y+3=0.",
          "a. The length of the tangent from (.g) to the circle x+y=6 is twice the length of the",
          "tangent to the circle x+y+3x+3y=0. Prove that f+g+4f+4g+2=0.",
          "b. the length of the tangent from (.g) to the circle x2+y4 is 4 times the length of the",
          "tangent to the circle x2 + y2+2x+2y=0. Prove that 15f+15g+32f+32g+4=0.",
          "a. circle x2+ y2 = 4 which are parallel to the straight line x+2y+3=0.",
          "b. circle x2+ y2 = 25 which are parallel to the straight line 3x+4y+3=0.",
          "a. x=8 and y=7 touch the circle x+y2-6x-4y-12-0. Find also the contact points. b. x+y-1-0 and x-y+1-0 touch the circle x+y-4x-2y+3-0. Find also the contact points",
          "a. to the circle x2+y=2, which make an angle of 45° with the x-axis. b. to the circle 3x+3y=1, which make an angle of 30° with the x-axis. c. to the circle x2+ y2 = 4, which make an angle of 60° with the x-axis.",
          "There are some properties of a circle that are listed as under.",
          "8.4.1 Perpendicular from the center of a circle on a chord bisects the chord",
          "and PQ be any chord of a circle, whose end points are P(x,;) and",
          "If PQ is a chord of the circle, then P and Q are the points",
          "The subtraction of these two circles equations gives the slope",
          "If the center of the circle is C(-g-f) and the midpoint of the chord PQ is",
          "then the slope of the perpendicular line CD is:",
          "From the Figure 8.14 the chord PQ and the line CD are perpendicular if and only if the product of their slopes equals -1:",
          "the perpendicular bisector of any chord PQ of a circle passes through the center of the circle. This is our second property.",
          "the line joining the two points of the circle that touches the center of the circle is called the diameter of the circle. This diameter acts as the perpendicular bisector to the chord PQ, if the",
          "diameter of a circle bisects the chord PQ. This is our third property. The proof is similar to property first, but the graphical view is shown in the Figure 8.14."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-12",
        "num": "15",
        "title": "Example 15",
        "problem": "If A(-3,4) and B(1,5)",
        "given": "",
        "method": "",
        "steps": [
          "(a). the line from the center of the circle is perpendicular to AB, also bisects the cherd AB.",
          "the line from the center of the circle to the midpoint of the chord AB is perpendicular to the chord",
          "(c). the perpendicular bisector CD of the chord AB pass though the center of the given circle.",
          "Solution The equation of the circle with center",
          "slopes the chord AB and the perpendicular line CD are respectively.",
          "The chord AB and the line CD are perpendicular if and only if the product of their slopes equals –",
          "Therefore, CD is perpendicular bisector of the chord AB. This result is automatically valid fo parts b and c.",
          "8.4.4 Congruent chords of a circle are equidistant from its center and its converse",
          "If the perpendicular distances form the center of a circle to its two chords are equal, then the chords are",
          "Let the circle equation with center C-g.-) is:",
          "If AB and DE are the two chords of the circle(i), then the coordinates of the end points of the chord AB and DE are respectively:",
          "From the Figure 8.15, it is clear that the perpendicular distance d,= CP from the center C on the chord AB equals",
          "the perpendicular distance d, =CQ from C on the chord",
          "DE, if and only if the chords AB and DE are with equal lengths: AB=DE",
          "Thus, the chords AB and DE are equidistant from C on the circle (i) if and only if d1 =d;",
          "In similar manner, the chords AB (join A to D) and BE (join B to E) are congruent chord the perpendicular distance d, = CR from C on the chord AD equals the perpendicular d, CS from"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-13",
        "num": "16",
        "title": "Example 16",
        "problem": "Show that the chords AB and DE are equidistant from the center C(0,0) of the circle +=4. The coordinates of the end points of the two chords are A(0,2), B(-2,0), D(0,-2) and E(2,0).",
        "given": "",
        "method": "",
        "steps": [
          "If AB and DE are the two chords of the circle (i), whose coordinates are respectively:",
          "From the Figure 8.16, it is clear that the chords AB and DE are with equal length:",
          "Thus, the two chords AB and DE are equal. For equidistant, the procedure is as under:",
          "The equations of the chords AB and DE (through two-",
          "The perpendicular distance d, from C(0,0) on the chord AB is: d",
          "The perpendicular distance d, from C(0,0) on the chord DE is: d",
          "The perpendicular distance d, from C(0,0) on the chord AB is equal to the perpendicular",
          "Thus, the chords AB and DE are equidistant from the center C(0,0) of the circle (i) 8.4.5 Measure of the central angle of a minor arc is double the measure of the",
          "angle subtended by the corresponding major are",
          "and the minor are BC subtended the angle from the center of the circle is BOC.",
          "The are BC is the minor are of the circle (i), whose coordinates are B(--) and C(-3).",
          "are which is two times the angle subtended by the major are: BOC=2<BAC",
          "A(0, a) is a point on the major arc, then join AB and AC that develops the angle of the minor",
          "From the Figure 8.17, if ZBAC=@ and ZBOC = 28, then, result (ii) can be verified as follows:",
          "is proving result (iv) with result (iii). Thus ZBOC=2ZBAC"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-8-14",
        "num": "17",
        "title": "Example 17",
        "problem": "Show that the angle subtended by the minor are BC of the circle +7-9 is two times the angle subtended. in the major are. The coordinates of the minor arc are B(2,√5),C(2,-√5).",
        "given": "",
        "method": "",
        "steps": [
          "If A(-3,0) is a point on the major arc, then join AB and AC that develops the angle of the minor arc which is two times the angle subtended by the major arc: From the Figure 8.18, if/BAC-8 and",
          "BOC=26, then, result (v) can be verified as √5-0"
        ],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-8-1",
        "exercise": "Exercise 8.1",
        "title": "Exercise 8.1",
        "description": "",
        "problems": [],
        "pageStart": 213,
        "pageEnd": 240
      },
      {
        "id": "ex-8-2",
        "exercise": "Exercise 8.2",
        "title": "Exercise 8.2",
        "description": "",
        "problems": [
          {
            "id": "ex-8-2-q1",
            "qNo": "1",
            "question": "Find tangent and normal equations: (a) at (1,2) to x²+y²=5; (b) at (−3,−2) to x²+y²=13; (c) at (4,1) to x²+y²−4x+2y−3=0.",
            "solution": "For x²+y²=r², tangent at (x₁,y₁) is xx₁+yy₁=r²; the normal passes through the center and point. (a) Tangent x+2y=5; normal y=2x. (b) Tangent −3x−2y=13; normal 2x−3y=0. (c) Complete squares: (x−2)²+(y+1)²=8. At (4,1), radius vector from center (2,−1) is (2,2), so tangent slope −1: x+y=5; normal slope 1: y=x−3.",
            "diagram": null
          },
          {
            "id": "ex-8-2-q2",
            "qNo": "2",
            "question": "For the circle x²+y²=13, find tangent and normal equations at (6cos60°,6sin60°); also find the tangent at (2cos45°,2sin45°) to x²+y²=4.",
            "solution": "(a) The stated point has radius 6 and therefore is not on x²+y²=13; no tangent to this circle exists at that point as printed. (b) Point=(√2,√2), circle radius²=4. Tangent: √2x+√2y=4, or x+y=2√2. Normal: y=x.",
            "diagram": null
          },
          {
            "id": "ex-8-2-q3",
            "qNo": "3",
            "question": "Find n so the line x+y+n=0 is tangent to x²+y²=9.",
            "solution": "The distance from the center (0,0) to the line must equal radius 3: |n|/√2=3. Thus n=±3√2.",
            "diagram": null
          },
          {
            "id": "ex-8-2-q4",
            "qNo": "4",
            "question": "Find n so y=mx+c is tangent to x²+y²=a².",
            "solution": "The distance from the origin to mx−y+c=0 is |c|/√(m²+1). Set this equal to a; hence c=±a√(m²+1).",
            "diagram": null
          },
          {
            "id": "ex-8-2-q10",
            "qNo": "10",
            "question": "Find tangents to x²+y²=4 parallel to x+2y+3=0, and to x²+y²=25 parallel to 3x+4y+3=0.",
            "solution": "Parallel lines have the same x,y coefficients. For x²+y²=r², a tangent x+2y+c=0 has |c|=r√5. (a) c=±2√5. (b) A tangent 3x+4y+c=0 has |c|=5√(3²+4²)=25, so c=±25.",
            "diagram": null
          }
        ],
        "pageStart": 213,
        "pageEnd": 240
      },
      {
        "id": "ex-8-3",
        "exercise": "Exercise",
        "title": "Exercise",
        "description": "",
        "problems": [],
        "pageStart": 213,
        "pageEnd": 240
      },
      {
        "id": "ex-8-4",
        "exercise": "Review Exercise 8",
        "title": "Review Exercise 8",
        "description": "",
        "problems": [],
        "pageStart": 213,
        "pageEnd": 240
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-9",
    "number": 9,
    "title": "Conics II",
    "titleUrdu": "",
    "pageRange": "Printed pages 241–285",
    "pageStart": 241,
    "pageEnd": 285,
    "sections": [
      {
        "id": "sec-9-1",
        "title": "9.1 Parabola",
        "theory": "Define a parabola and its elements (i.e. focus, directrix, eccentricity, vertex, axis, focal chord and latus rectum). General form of an equation of a parabola.\n\nStandard equations of parabola, sketch their graphs and find their elements.\n\nFind the equation of a parabola with the following given elements:\n\nFind the condition when a line is tangent to a parabola at a point and hence write the equation of a tangent line in slope form.\n\nFind the equation of a tangent and a normal to a parabola at a point.\n\nSolve suspension and reflection problems related to parabola.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-9-2",
        "title": "9.2 Ellipse",
        "theory": "Define ellips and its elements (i.e. centre, foci, vertices, covertices, directories, major and minor eccentricity, focal chord and latus rectum).\n\nExplain that circle is a special case of an ellipse.\n\nDerive the standard form of equation of an ellipse and identify its elements.\n\n⚫ foci, vertices or lengths of a latus rectum,\n\nFind the equation of an ellipse with the following given elements.\n\nfoci, minor axes or length of a latus rectum.\n\nConvert a given equation to the standard form of equation of an ellipse, find its elements and draw the graph. Recognize tangent and normal to an ellipse.\n\nvii. Find points of intersection of an ellipse with a line including the condition of tangency.\n\nFind the equation of a tangent in slope form.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-9-3",
        "title": "9.3 Hyperbola",
        "theory": "Fine the equation of a tangent and a normal, to an ellipse at a point. Hyperbola",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-9-4",
        "title": "9.4 Translation and Rotation of Axes",
        "theory": "Define hyperbola and its elements (ie. centre, foci, vertices, directrices, transverse and conjugate axes, eccentricity, focal chord and latus rectum),\n\nDerive the standard form of equation of a hyperbola and identify its elements.\n\nFind the equation of a hyperbola with the following given elements:\n\ntransverse and conjugate axes with centre at origin, eccentricity, Latera recta and transverse axes,\n\nConvert a given equation to the standard form of equation of a hyperbola, find its elements and sketch the graph. Recognize tangent and normal to a hyperbola.\n\npoints of intersection of a hyperbola with a line including the condition of tangency,\n\nFind the equation of a tangent and a normal to a hyperbola at a point.\n\nDefine translation and rotation of axes and demonstrate through examples. Find the equations of transformation for\n\nFind the transformed equation by using translation or rotation of axes.\n\nFind new origin and new axes referred to old origin and old axes.\n\nFind the angle through which the axes be rotated about the origin so that the product term xy is removed\n\nIn our previous unit of this book we have learnt that a conic section (or simply a conic) is a curve obtained as the intersection of the surface of a cone with a plane. In this unit we will study in details about the three types of conic sections that are parabola, hyperbola and the ellipse. The circle is a type of ellipse and same time considered to be the fourth type of conic section. We have already discussed in details about tangent and normal in previous section.\n\nWhen you kick a soccer ball (or shoot an arrow, fire a missile or throw\n\na stone) it arcs up into the air and comes down again\n\nA parabola is a curve where any point is at an equal distance from:\n\net a piece of paper, draw a straight line on it, then make a big dot for the focus (not on the line!).",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-9-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Graph the parabola y2-8x=0 and indicate the vertex, focus, directrix and the focal chord.",
        "given": "",
        "method": "",
        "steps": [
          "and is compared with the standard form of the parabola (3) to obtain:",
          "Since p>0, the parabola opens to the right. The vertex is V(0,0), the focus is F(2,0), the directrix is the line x=-2 and the length of the focal chord is 4p=4(2) = 8. The line of symmetry is the positive x-axis. This is shown in the Figure 9.4."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Graph the parabola x+y=0and indicate the vertex, focus, directrix and the focal chord.",
        "given": "",
        "method": "",
        "steps": [
          "and is compared with the standard form of the parabola (5) to obtain :",
          "Since p< 0, the parabola opens downward. The vertex",
          "V(0,0), the focus is F(0,1), the directrix is the",
          "negative y-axis. This is shown in the Figure 9.5.",
          "(iv) The equation of a parabola with the given elements"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Find an equation of parabola with",
        "given": "",
        "method": "",
        "steps": [
          "and the line of symmetry is the positive x-axis. This is shown in the Figure 9.7.",
          "By inspection, the value of p is p -- that satisfies the",
          "directrix x- This gives the equation of parabola",
          "line of symmetry is the negative x-axis. This is shown in the Figure 9.8.",
          "(v) Recognition of tangent and normal to a parabola",
          "A line which is parallel to the axis of a parabola intersects the parabola in only one (finite) point; all other lines will cut the parabola in two real and distinct points, real and coincident points, or complex conjugate points. \"A line which meets a parabola in two coincident points is called a tangent.\" A tangent to any curve at a point P is the limiting position of a secant line, cutting the curve in two points P and Q as Q→ P.The normal can easily be shown in the subsection of this section.",
          "(vi) The condition at which a line is tangent to parabola at a point",
          "The line is tangent to parabola, when the line intersects the parabola in two real and coincident",
          "The solution set (x,y) of nonlinear system of equations (10) exists only, if the curves of the system",
          "(10) are intersecting. That set of points of intersection (x,y) (a solution set) can be found by solving the",
          "The line (9) is used in parabola (8) to obtain the quadratic equation in x",
          "The equation (11) being a quadratic equation in x, gives a set of two values.x, and x, of x, which will be used in a line (9) to obtain a set of two y values y, and y",
          "Thus, a solution set ((.)(.)) of the system (10) is of course a set of points of intersection of the system (10).",
          "The points of intersection of the system (10) are real, coincident or imaginary, according as the roots of the quadratic equation (11) are real, coincident or imaginary or according as the discriminant of the quadratic equation (11):",
          "Disc=4(mc-2p)-4m'c'>0, real and different Disc=4(mc-2p)\" - 4m22=0, real and coincident Disc-4(mc-2p)-4me<0, imaginary"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-4",
        "num": "4",
        "title": "Example 4",
        "problem": "For what condition the tangent line 4x-y-4-0 intersects the parabola.x\"=y?",
        "given": "",
        "method": "",
        "steps": [
          "The line (12) is used in parabola (13) to obtain the y-coordinates of the points of intersection:",
          "x2=4x-4 Put the value of y from equation (12)",
          "The x-coordinates are used in the line (12) to obtain the y-coordinates y=4,4",
          "Thus, the set of two points of intersection (2,4) and (2,4) are real and coincident and the tangent line 4x-3-4-0 is of course intersecting the parabola (13) at two coincident points (2,4) and (2,4).",
          "then the equation of that tangent line is of the form",
          "Here e is to be calculated from the fact that the line (15) is tangent to parabola (14). The line (15) is used in parabola (14) to obtain the quadratic equation in x:",
          "If the line (15) touches the parabola (14), then the quadratic equation (16) has coincident roots for which the discriminant of the quadratic equation (16) equals zero:",
          "The equation (17) represents the condition of tangency. The value of c from equation (17) is used",
          "in the line (15) to obtain the required equation of tangent",
          "⚫ the equation of any tangent to parabola y 4px in the slope-form is:",
          "the line y=mx+c should touch the parabola y=4px under condition:",
          "the condition of tangency in case of parabola x=4py and line y = mx + c is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-5",
        "num": "5",
        "title": "Example 5",
        "problem": "For what value of c, the line x-y+c=0 will touch the parabola x=8y? Use that value of to find the tangent line that should touch the given parabola.",
        "given": "",
        "method": "",
        "steps": [
          "Here m is the slope of the line x-y+c=0, which is m=1. The required tangent line that should touch the parabola through (20) is:",
          "(vii) The equation of a tangent and a normal to a parabola at a point",
          "Let the equation of the tangent line at a point p(x,y) to parabola y=4px be: J−y, − m,(x−x, )",
          "Herem, is the slope of the tangent line to parabola y=4px at a point p(x,y,) that can be found by",
          "The substitution of (22) in (21) is giving the equation of the tangent line at a point p(5.)\\) '",
          "the equation of the tangent line at a point p(x,y,) to parabola y=4py is:",
          "if the tangent line y=mx+] to parabola y2 = 4px is identical to yy, -2p(x+x,), then the",
          "and yy,=2p(x+x) are compared to obtain the contact",
          "point is p(4,3)-(22) in case of parabola y' - 4px.",
          "if the tangent line y muc-pm2 to parabola x=4py is identical to xx=2p(y+y), then the coefficients of like terms of y=x-pm and xx=2p(y+y) are compared to obtain the point of",
          "p(x,y)-(2pm, pm) in case of parabola x=4py. (26)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-6",
        "num": "6",
        "title": "Example 6",
        "problem": "Find the equation of tangent line at a point p(2,-4) to parabola y=8.x. Show that p(2,-4) is",
        "given": "",
        "method": "",
        "steps": [
          "Solution Result (23) is used to obtain the tangent line to the given parabola:",
          "The Equation of a normal line to parabola at a point",
          "The equation of the normal line at a point p(x,.,) to parabola y 4 pris:",
          "Here m, is the slope of the normal line to parabola y=4pr at a point p(x,y) that can be found by",
          "The substitution of (28) in (27) is giving the normal equation at a point p(x,,,) to parabola"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-7",
        "num": "7",
        "title": "Example 7",
        "problem": "Find the normal equation at a point p(2-4) to parabola y2=8.x. Solution Result (29) is used to obtain the normal line to the given parabola:",
        "given": "",
        "method": "",
        "steps": [
          "The parabola is more than just a geometric concept. It has many uses in the physical world that are listed under:",
          "1. Projectiles in the air, such as a ball, or a missile, or water sprayed from",
          "a hose, describe a parabolic path when acted on only by gravity. 2. Many arches of bridges or buildings are parabolic in shape. With this",
          "shape, the arch can support the structure above it.",
          "3. Rotating a parabola about its line of symmetry, creates a bowl type surface called a paraboloid of revolution. A paraboloid has an important reflection property. Any ray or wave that originates at the focus and strikes the surface of the paraboloid is reflected parallel to the line of symmetry. See Figure 9.9.",
          "This forms the basic design of the reflectors for automobile headlights, flashlights, searchlights, telescopes, etc. This is also an excellent collecting device and is the basic design of TV, radar, and radio antennas."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-8",
        "num": "8",
        "title": "Example 8",
        "problem": "The cables of a bridge form a parabolic arc. The low point of the cable is 10ft above the roadway midway between two towers. The distance between the towers is 400 ft. The cable is attached to the towers 50ft above the roadway. Determine the equation of the parabola that describes the path of the",
        "given": "",
        "method": "",
        "steps": [
          "The vertex V(0,10) and a point on the curve (x, y)=(200,50) are used in (30) to obtain p:",
          "(x − h)2 = 4p(y−k), translate h units on the x-axis, k units on the y-axis",
          "The substitution of V(h, k) = (0,10) and p=250 in equation (30) is giving the parabolic equation"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-9",
        "num": "9",
        "title": "Example 9",
        "problem": "A radar antenna is constructed so that a cross section along its axis is a parabola with the receiver at the focus. Find the focus if the antenna is 12 m across and its depth is 4 m. Find the equation of parabola that described the radar antenna. This is shown in the Figure 9.11.",
        "given": "",
        "method": "",
        "steps": [
          "Thus, the parabolic equation that describes the radar antenna",
          "In each case, sketch the parabola represented by the equation, indicate the vertex, the focus, the end points of the focal chord (latus rectum) and the axis of symmetry:",
          "In each case, determine the equation of graphed parabola:",
          "In each case, write the equation of parabola through the given information:",
          "c. Vertex at (0,0), x-axis is the line of symmetry, passes through (3,6). d. Vertex at (0,0), 3-axis is the line of symmetry, passes through (-12,-3). e. Line of symmetry is vertical, passes through (-3,4), vertex at P(5,1).",
          "f. Line of symmetry is horizontal, passes through (7,9), vertex at V(3,−7).",
          "Find the equation of the set of all points with distances from (4,3) that equal their distances (-2,1).",
          "Find an equation for a parabola whose focal chord has length 6, if it is known that the parabola has",
          "focus (4,-2) and its directrix is parallel to the y-axis.",
          "In each case, find the points of intersection in between the line and the parabola:",
          "a. the line x-y+c=0 will touch the parabola y2=9x?",
          "In each case, find the tangent equation and normal equation",
          "a. to parabola y=x, which makes an angle of 135° with the x-axis.",
          "b. to parabola y=y which makes an angle of 60° with the x-axis.",
          "Find the equation of the parabolic portion of the archway, if parabolic archway has the dimensions shown in the figure below:",
          "In shape and in format, the ellipse is different from the parabola. Although the parabola is open at one end, the ellipse is entirely closed. The parabola has one focus and one vertex, while the ellipse has two",
          "The second type of conic is called an ellipse, and is defined as follows.",
          "An ellipse is the set of all points in a plane, the sum of whose distances from two distinct fixed points (foci) is constant.",
          "Center- It is the point where major and minor axis intersects each other. The midpoint of the connecting two",
          "Focus - There are two focal points on the major axis which defines the ellipse. These are same distance to the both sides from the center.",
          "Major Axis - It is the lengthiest diameter of the ellipse. It has the end points on the widest part of the ellipse and passes through the center.",
          "Minor Axis - It is the shortest diameter of the ellipse. It is the perpendicular bisector of the major axis. It has the end points on the narrow part of the ellipse and passes through the center. Vertices - The four points where the major and minor axis touches the ellipse are the vertices. The end points of major axis are generally called Vertex and the end points of minor axis art generally called Co-vertex.",
          "Chord - It is a line segment that has both the end points on the ellipse. Major axis is also the chord which is the longest one in an ellipse.",
          "Eccentricity is the factor related to conic sections which shows how circular the conic section is. More eccentricity means less spherical and less eccentricity means more spherical. It is denoted by \"?\" The eccentricity of an ellipse is showed by the ratio of the distance between the two foci, to the size of",
          "where e Eccentricity, c= The distance from the center to any one of the foci and a= The sea The eccentricity of an ellipse is between 0 and 1 (0 <e <1). If the eccentricity is zero the foci ch with the center point and become a circle. If the eccentricity moves toward 1, the ellipse gets i",
          "Directrix is the line which is parallel to the minor axis of the ellipse and related to both the foci of the ellipse.",
          "It is the line parallel to directrix and passes through any of the focus of an ellipse. It is denoted by \"21\".",
          "In an ellipse, latus rectum is 26% (where a is one half of the major diameter and b is the half of the minor diameter).",
          "The half of latus rectum till its intersection point with the major axis is the semi latus rectum. It is denoted by \"/\".",
          "If P(x, y) is any point on the ellipse, then the distances from the two foci F(-.0) and F(c,0) to the point P(x, y) are the following:",
          "By definition of an ellipse, the general form of an ellipse is:",
          "The relative shape of an ellipse can be determined by its eccentricity e. The distance from the center of the ellipse to a foci is c and the distance from the center to a vertex is a. The eccentricityris given by the equation:",
          "The eccentricity of all ellipses are in a range between 0 and 1 (0 <e < 1). This is shown in the Figure 9.14.",
          "An ellipse with an eccentricity close to 1 is long and thin, and the foci are relatively far apart. If the eccentricity is small, close to 0, then the ellipse resembles a circle. It can be shown that the circle is a special case of the ellipse when e=0.",
          "(iii) Standard form of equation of an ellipse",
          "The standard form of the equation of an ellipse with center at the origin, length of the semimajor axis a, length of the semiminor axis band major axis along the x-axis shown in the Figure 9.15.",
          "If we replace the foci on the 3-axis, center at the origin, and pick any point P(x, y) on the plane, then we can develop the equation of the vertical ellipse given in the following definition. \"The standard form of the equation of an ellipse with center at the origin, length of the semimajor axis a length of the semimine raxis b and major axis along the y-axis is shown in the Figure 9.16.",
          "Graphing Ellipse: In order to sketch an ellipse, it is required to plot the center, the intercepts ±a on the major axis and ±b on the minor axis.",
          "First, rewrite the equation of the ellipse in the standard form, so that there is a \"1\" on the right and the numerator coefficients of the square terms are also 1. The center is at (0,0) and plot the intercepts on the x-axis and y-axis. For the x-intercepts, plot± the square root of the number a\"; for the plot the square root of the number 6, finally, and draw the ellipse using these intercepts. The longer as is called the major axis. If this larger axis is horizontal, then the ellipse is called horizontal, and if the",
          "major axis is vertical, the ellipse is then called vertical",
          "The orientation of the ellipse equation with center C(0,0), vertices/end points of the major axis and",
          "the end points of the semiminor axis are summarized in the box"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-10",
        "num": "10",
        "title": "Example 10",
        "problem": "Determine the vertices, end points of the minor axis and the coordinates of foci of the ellipse 9+4=36. Sketch the ellipse.",
        "given": "",
        "method": "",
        "steps": [
          "The equation (38-a) is related to the vertical standard form ellipse (37). The center of the ellipse is at the origin, but the vertices of the major axis are on the y-axis, since the larger numerical value is undery. Thus, 9 or a=3, and 4 orb-2 and -a-b-9-4-5 or cu±√5.",
          "The coordinates of the center, vertices/end points of the major axis, end points of the minor axis and the foci are the following:",
          "The ellipse is symmetrical with respect to the major axis, minor axis. The center, vertices, foci, and the points",
          "are labeled to obtain the graph of the given ellipse in Figure 9.17."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-11",
        "num": "11",
        "title": "Example 11",
        "problem": "Determine the vertices, end points of the minor axis and the coordinates of foci of the ellipse 2x+5y=10. Sketch the ellipse.",
        "given": "",
        "method": "",
        "steps": [
          "The ellipse (8-b) is related to the horizontal standaru form ellipse (36). The center of the ellipse is at the origin, but the vertices of the major axis are on the x-axis, since the large numerical value is under x. Thus, a-5 or a=√5 and b2=2 or b=√2 and e-a-b-5-2-3 or c=±√3.",
          "The coordinates of the center, vertices/end points of the major axis, end points of the minor axis and the foci are the following:",
          "(iv) Equation of an ellipse through its elements"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-12",
        "num": "12",
        "title": "Example 12",
        "problem": "Find an equation for the ellipse with foci F(-1,0) and F,(1,0) and vertices V(-2,0) and",
        "given": "",
        "method": "",
        "steps": [
          "The values of a and b are used in the horizontal standard form ellipse (36) to obtain",
          "The standard form of the equation of an ellipse with center at C(h, k), length of the seminaj is a and semiminor axis b, and major axis parallel the x-axis is:",
          "The standard form of the equation of an ellipse with center at C(h, k), length of the semimajor axis a and semiminor axis b, and major axis parallel to the y-axis is:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-13",
        "num": "13",
        "title": "Example 13",
        "problem": "Graph the ellipse whose equation is 4x+25y-8x+100y+4=0. Indicate the center, vertices, foci and the end points of the minor axis.",
        "given": "",
        "method": "",
        "steps": [
          "The given ellipse (42) with substitution X-x--x-1 and Y-y-k-y+2,-1,--2 gives the translated ellipse in the XY-plane:",
          "The center of the ellipse is at the origin. The major axis is horizontal and the vertices are on the x-axis. Thus, a = 5, 6-2 and c=±√21-14.58.",
          "The coordinates of the center, vertices/end points of the major axis, end points of the minor axis and the foci of the translated ellipse (43) are the following:",
          "vertices/end points of the major axis, the end points of the minor axis and foci of the given ellipse (42) are the following:",
          "The center of the given ellipse (42) is C(1,-2).",
          "The coordinates of the vertices V,(-5,0), V(5,0) of the translated ellipse are X = -5, Y = 0 (in",
          "case of V,) and X=-5, Y = 0 (in case of V,). Put X=-5 and Y-0 in (43) to obtain the coordinates of the vertex V, of the given ellipse (42) :",
          "The vertex V, of the given ellipse (42) is V,-4,-2) and the vertex V, of the given ellipse (42) is course V,(6,-2).",
          "• The coordinates of the foci F(-4.58,0), F(4.58,0) of the translated ellipse are X=-4.58, Y=00 case of F,) and X = 4.58, Y0 (in case of F). Put X-4.58 and Y-0 in (43) to obtain th coordinates of the focus F, of the given ellipse (42);",
          "The focus of the given ellipse (42) is F(-3.58,-2) and the focus F, of the given ellipse (42) is c course F,(5.58,-2).",
          "The graph of the ellipse is shown in the Figure 9.21.",
          "The orientation of the ellipse equation with center C(h, k) are summarized in the boxes:",
          "Vertices/End Points of Major Axis V1(h−a,k),V;h+a,k)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-14",
        "num": "14",
        "title": "Example 14",
        "problem": "Find the equation of the ellipse with vertices at (-1, 2) and (7, 2) and with 2 as the length of the semiminor axis.",
        "given": "",
        "method": "",
        "steps": [
          "(3,2) of the line segment V, V, is the center C(h, k) = C(3, 2). This is shown in the Figure 9.22.",
          "The distance from the center C(3, 2) to either vertex is 4 units. The semiminor axis has a length of b=2. From the Figure 9.22, we see that the major axis is parallel to the x-axis. The horizontal standard form of the ellipse (40) is used to obtain the required ellipse equation:",
          "(vi) Recognition of tangent and normal to an ellipse",
          "\"A line that interacts the ellipse at a point is known as tangent at the ellipse\" in the Figure 9.23, the line LM is tangent to the ellipse which is intersecting the ellipse at point \"P' as shown in Figure 9.23,",
          "Normal to an ellipse is a line perpendicular to the tangent to curve through the point of contact. Line QR is normal to the ellipse which is perpendicular to the tangent LM at point 'P', as shown in Figure 9,23,",
          "(vii) Point of Intersection of an ellipse and a line The given line and ellipse",
          "The angle between tangent to ellipse and normal is always a right angle.",
          "The solution set (x,y) of nonlinear system of equations (47) exists only, if the curves of the system (47) are intersecting. That set of points of intersection (x,y) (a solution set) can be found by solving the nonlinear system (47) simultaneously.",
          "The line (45) is used in ellipse (46) to obtain the quadratic equation in r",
          "The equation (48) being a quadratic equation in x, gives a set of two values x, and 1, of, which will be used in a line (45) to obtain a set of two values y, and y, of y",
          "Thus, a solution set ((.)(.)) of the system (47) is of course a set of points of intersection of the system (47).",
          "The points of intersection of the system (47) are real, coincident or imaginary, according as the roots of the quadratic equation (48) are real, coincident or imaginary, according as the discriminant of the quadratic equation (48)",
          "Disc=4a*m*c2-4(a'm2+b2)(a)(c2-b2)>0, real and different Disc=4a*m3c2-4(a'm2+b2)(a)(c2-b2)=0, real and coincident",
          "Disc=4a*m3c2-4(a3m2+b2)(a)(c2-b3)<0, imaginary"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-15",
        "num": "15",
        "title": "Example 15",
        "problem": "Find the points of intersection of the line 2r-y-2-0 and the ellipse 4x+9y=36.",
        "given": "",
        "method": "",
        "steps": [
          "The line (49) is used in an ellipse (50) to obtain ther-coordinates of the points of intersection:",
          "The x-coordinates are used in the line (49) to obtain the y-coordinates: x=0. giver=-2",
          "Thus, the set of two points of intersection (0,-2) and",
          "intersects the ellipse (50) at points (0,-2) and",
          "(viii) The equation of a tangent line in slope-form",
          "Ifm is the slope of the tangent line to ellipse 4+1",
          "then the equation of that tangent line is of the form y=mx+e Here is to be calculated from the fact that the line (52) is tangent to ellipse (51).",
          "The line (52) is used in an ellipse (51) to obtain the quadratic equation in x:",
          "If the line (52) touches the ellipse (51), then the quadratic equation (53) has coincident roots for which the discriminant of the quadratic equation (53) equals zero:",
          "a3m2c3 −(a*m2 +b2 ) (c3-b)=0, divide out by ŝa1 a'm'c'-a'm'c'+a'm'b'-b'c'+b=0",
          "The equation (54) is the condition of tangency. The value ofc from equation (54) is used in the line (2) to obtain the required equation of the tangent line: y=mx+c=m√a®m2+b2",
          "⚫ the equation of any tangent to ellipse+1 1 in the slope-form is:",
          "Condition of Tangency: The line y = mx + c should touch the ellipse +2-"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-16",
        "num": "16",
        "title": "Example 16",
        "problem": "For what value of c, the line 2r-+-0 will touch an ellipse",
        "given": "",
        "method": "",
        "steps": [
          "Solution The values of c at which the line 2r-y+c=0 will touch the given ellipse through result (57)",
          "The required tangent lines that should touch the ellipse through result (56) is:",
          "(ix) The equation of a tangent line to ellipse at a point",
          "The equation of a tangent line at a point P(x,y) to ellipse",
          "Herem, is the slope of the tangent line to ellipse",
          "The substitution of (59) in (58) is giving the equation of the tangent line at a point P(x,.,) to ellipse:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-17",
        "num": "17",
        "title": "Example 17",
        "problem": "Find the equation of the tangent at a point P(3.12) to ellipse 2-1.",
        "given": "",
        "method": "",
        "steps": [
          "(x) The equation of a normal line to ellipse at a point",
          "The equation of a normal at a point P(x,y) to ellipse",
          "the normal equation at a point P(x,y,) to ellipse:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-18",
        "num": "18",
        "title": "Example 18",
        "problem": "Find the normal equation at a point P",
        "given": "",
        "method": "",
        "steps": [
          "In each case, sketch the ellipse represented by the equation. Indicate the center, foci, endpoints of the major axis and end points of the minor axis:",
          "In each case, determine the equation of graphed ellipse:",
          "In each case, write the equation of ellipse through the given information: a. Center is at (-3, 2), a=2, b-1, major axis is horizontal.",
          "c. A focus is at (-2, 3), a vertex is at (6,3), length of minor axis is 6. d. Vertices are at (0,8) and (0,2), c = √5.",
          "The shape of an ellipse depends on the eccentricity of the ellipse e = . Determine",
          "b. the equation of the ellipse with vertices are at (-5,0), and (5,0) and the eccentricity is e-3.",
          "c. the eccentricity of the ellipse, if the length of the semimajor axis is a=4 and the length of the semiminor axis is b=2.",
          "a. the line x-y+c=0 will touch the ellipse +=1?",
          "In each case, find the tangent equation and normal equation",
          "a. to the ellipse += 1 which is perpendicular to the line 9x+8y-36=0.",
          "The ad of the sonic veten se sondemna defnen miler har of besligue it",
          "Hyperia and is center, flex scenery, heal cars, tratenerse and conjagane anen, eccentricity focal chart and lana rea",
          "why should we be concerned about the conjugate axis or the length ! Te significance of bis determined by solving the standard form of hyperbola for y:",
          "Let us examine the fraction (a is constant). If we substitute larger and larger values for x, then the",
          "becomes smaller and smaller. In fact, the fraction eventually gets very close to zero. Thus, for",
          "large values of x, the term 1-approaches 1. Therefore, for large values of x, the y values approaches the",
          "value +x, and the value of the hyperbola gets closer and closer to the lines:",
          "These lines are called the asymptotes of the hyperbola. As x takes on values that are gester distances from the center of the hyperbola, the values of y (of the hyperbola) become closer and closer to the asymptotes even though they never actually reach the corresponding p-values of the asymptotes. Since these lines are easy to graph, the asymptotes are valuable aids in sketching the hyperbola.",
          "If a straight line cuts a hyperbola in two points at an infinite distance from the origin and is itself at a finite distance from the origin is then called the asymptotes.",
          "The orientation of the hyperbola with center C(0,0), vertices and foci are summarized in the box:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-19",
        "num": "19",
        "title": "Example 19",
        "problem": "Sketch the hyperbola-1, with center at the origin and the transverse axis is at the",
        "given": "",
        "method": "",
        "steps": [
          "Solution The given hyperbola equation is in the standard form of the equation of a hyperbola transverse axis along the x-axis. This tells us that a=9,a=±3 and 62=16,b-14. The vertices of the hyperbola are V,(−3,0) and V,(3,0). The value of e for foci can be found by using the formula: c=a+b2=9+16=25,e=15",
          "The foci are therefore F(-5,0) and F,(5,0). The asymptotes",
          "For sketching the hyperbola, the end points of the conjugate axis (0,-4) and (0,4) are located, then draw the lines through the points (0,-4) and (0,4) parallel to the x-axis. Similarly, draw the lines through the end points of the transverse axis V(-3,0) and V,(3,0) parallel to j– axis to complete the rectangle. The resultant rectangle and the extended diagonals of the rectangle are the asymptotes of the hyperbola. The sketch of the hyperbola is shown in the Figure 9.28."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-20",
        "num": "20",
        "title": "Example 20",
        "problem": "Sketch the hyperbola 16y7-9,2 = 144, with center at the origin and the transverse axis is at the y-axis. Determine the vertices and foci of the hyperbola",
        "given": "",
        "method": "",
        "steps": [
          "If the transverse axis is along the y-axis, then select -9,a=13 and 6=16,b=14. The vertices of the hyperbola are V,(0,3) and V,(0,-3). The end points of the conjugate axis are (-4, 0) and (4, 0). The value of for foci",
          "The foci are therefore F,(0,5) and F,(0,-5). The asymptotes are the lines",
          "Sketch the rectangle formed by the points (0,±3) and (14,0) and then sketch the asymptotes using the diagonals of the rectangle. With the asymptotes, vertices and foci, it is easy to sketch the hyperbola, as",
          "(iv) Equation of hyperbola through its elements"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-21",
        "num": "21",
        "title": "Example 21",
        "problem": "Find the vertices, foci, eccentricity and the asymptotes of the hyperbola 16-9y=144.",
        "given": "",
        "method": "",
        "steps": [
          "The vertices, foci, eccentricity and asymptotes of the given hyperbolaise following:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-22",
        "num": "22",
        "title": "Example 22",
        "problem": "Find the equation of hyperbola, when one focus is at (0,6), center is at C(0,0) and the eccentricity is 3.",
        "given": "",
        "method": "",
        "steps": [
          "These values of a and c is used in the formula to obtain the value of b c2=a2+b2",
          "If any point (h, k) on the plane is selected as the center of the hyperbola and a major axis parallel to the x-axis or y-axis is selected, then with the geometrical definition, a new set of equations for hyperbola",
          "The standard form of the equation of a hyperbola with center at C(h, k), vertices at V1(h+a,k) and V1(h—a,k), foci at F(h-e,k) and F,(h+c,k) is:",
          "The standard form of the equation of a hyperbola with center at C(h, k), vertices at V,(h,k+a) and V1(k,k-a), foci at F(h,k+e)and(h,k-c) is:",
          "The orientation of the hyperbola equation with center C(A, A) are summarized in the box:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-23",
        "num": "23",
        "title": "Example 23",
        "problem": "Sketch the hyperbola",
        "given": "",
        "method": "",
        "steps": [
          "(vi) Recognition of tangent and normal to hyperbola",
          "A line which intersects a hyperbola in two coincident points is a tangent. For the hyperbola, there will be two tangents [real and distanct, coincident (with an asymptote), or complex] with a given slope. The formulation for tangents to hyperbola will be discussed in the succeeding sections.",
          "(vii) Point of intersection of hyperbola with a line including the condition of",
          "The solution set (x,y) of nonlinear system of equations (soexists only, if the curves of the system",
          "are intersecting. That set of points of intersection (x,y) (a solution set) can be found by solving the",
          "The line (78)is used in hyperbola (79to obtain the quadratic equation in x:",
          "being a quadratic equation in x, gives a set of two values x, and x, of x, which will to obtain a set of two values y, and y, of y The solution set {(x,y).(x,y)} of the system",
          "is of course a set of points of intersection of the system",
          "are real, coincident or imaginary, according as the roots are real, coincident or imaginary, or according as the discriminant of the",
          "Disc=4a\"m3c2+4(b2-am3)(a)(c2+b2)>0, real and different",
          "Disc=4am c2+4(b3-a'm2)(a2)(c2+b2)=0, real and coincident"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-24",
        "num": "24",
        "title": "Example 24",
        "problem": "Find the points of intersection of the line x-y-1-0 and the hyperbola 4x2-y= 4. Solution The equations of the line and hyperbola are",
        "given": "",
        "method": "",
        "steps": [
          "The x-coordinates are used in the line to obtain the y-coordinates:",
          "Thus, the set of two points of intersection (1,0) and",
          "x-y-1-0 intersects the hyperbola at points (1,0) and",
          "(viii) Equation of a tangent line in slope-form",
          "Ifm is the slope of the tangent line to hyperbola",
          "then the equation of that tangent line is of the form",
          "Here c is to be calculated from the fact that the line is tangent to hyperbola (541 The line is used in hyperbola to obtain the quadratic equation in x:",
          "which the discriminant of the quadratic equation 4a m'e2+4(b2-a'm')(a)(c'+b2)=0",
          "is going to be zero: , then the quadratic equation has coincident roots for",
          "a'm2c2 + (b2 − a'm2)(c2 + b2)=0, divide out by 4a2",
          "The equation, is the condition of tangency. The value of e from equation is used in the line to obtain the required equation of the tangent line:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-25",
        "num": "25",
        "title": "Example 25",
        "problem": "For what value of c, the line y=x+c will touch the hyperbola",
        "given": "",
        "method": "",
        "steps": [
          "is the slope of the line y=x+c. The required tangent lines that should touch the",
          "Equation of a tangent line to hyperbola at a point",
          "The equation of the tangent at a point P(x) to hyperbola",
          "Herem, is the slope of the tangent line to hyperbola",
          "The substitution of (92) in (91) is giving the equation of the tangent line at a point P(x) to"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-26",
        "num": "26",
        "title": "Example 26",
        "problem": "Find the equation of the tangent at a point P(5.1) to hyperbola--1",
        "given": "",
        "method": "",
        "steps": [
          "Equation of a normal line to hyperbola at a point",
          "The equation of the normal at a point P(x,y;) to hyperbola =1, 3-3-1,",
          "Here m, is the slope of the normal to hyperbola-1, at a point P(x, J;) that",
          "The substitution of (95) in (94) is giving the normal equation at a point PL) to hyperbola:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-27",
        "num": "27",
        "title": "Example 27",
        "problem": "Find the normal equation at a point P(5.1) to hyperbola--1",
        "given": "",
        "method": "",
        "steps": [
          "In each case, sketch the hyperbola represented by the equation. Indicate the center, vertices, foci a the equations of the asymptotes:",
          "In each case, determine the equation of graphed ellipse:",
          "In each case, write the equation of hyperbola through the given information:",
          "Foci are at (0,3) and (0,-3), one vertex is at (0,-2).",
          "Vertices are at (5,0) and (-5,0), one focus is at (-7,0).",
          "Transverse axis is the x-axis, asymptotes are the lines y= 3x and y=-3r. Foci are at (5,0) and (-5,0), eccentricity is 5/3.",
          "Vertices are at (3,-1) and (-1,-1), asymptotes are the lines y=(9/4)x−(13/4) and } = (-9/4) x + (5/4).",
          "Determine the path of a point that moves so that the difference of its distances from",
          "with vertices at (2,-2), (-4,-2) and that passes through the point with coordinates (5,1)- with vertices at (-3,1), (-3,3) and that passes through the point with coordinates (0,4). In each case, sketch the rectangular hyperbola and identify the vertices, the foci and the asymptotes:",
          "In each case, find the points of intersection in between the line and the hyperbola:",
          "In each case, find the tangent equation and normal equation",
          "If the coordinates of a point or the equation of a curve be given with reference to a system of axes, rectangular or oblique, then the coordinates of the same point or the equation of the same curve can be obtained with reference to another system of axes, rectangular or oblique. The process of so changing the coordinates of a point or the equation of a curve is called the transformation of coordinates.",
          "In general, we come across to define three types of change of axes that are the following:",
          "Translation of Axes: This will be used in changing the origin only and the new axes are parallel to",
          "Ratation of Axes: This will be used in changing the directions of the axes without changing the origin of the system.",
          "General Transformation: This will be used, when the change of the direction and the origin of the axes both come together.",
          "The relationship between the two sets of coordinate axes is called the translation of axes.",
          "The rotational relationship between the two sets of coordinate axes is called the rotation of axes.",
          "Equations of transformation for translation of axes If 0(0,0) is the old origin of the set of old rectangular coordinate axes ox and oy, then the coordinates of a point P with respect to the old axes are P(x, y).",
          "If O(h, k) is the new origin of the set of new rectangular coordinate axes OX and OY parallel to the old rectangular coordinate axes, then the coordinates of a point P with respect to the new axes are P(X, Y).",
          "If PM and ON are perpendicular to old coordinate axis where PM intersects the new coordinate axis OX at M,, then, the following assumptions",
          "develops a set of rectangular coordinate axes in terms of new coordinates X, Y by means of the relation:",
          "The set of equations (97) are the equations of transformation for translation of axes. By making this substitution in a given equation, a new equation of the same graph is obtained, referred now to the new",
          "(iii) Equations of transformation for rotation of axes",
          "If ox and oy is the set of old rectangular coordinate axes, then the set of new rectangular coordinate axes OX and OY is obtained by rotating the old rectangular coordinates through an angle 0,0<0<90'",
          "If the coordinates of a point P with respect to the old axes are P(x, y), then the coordinates of a point P with respect to the new axes are PCX, Y.)",
          "If PM and PN are perpendicular to Or and OX and NN, and NM, are perpendicular to Or and PM, then, the following assumptions",
          "ON, MN, ON, -M,N ONcos-NP sin 0=Xcos-Ysin J=MP",
          "MM, +M,P = N,N+M,P-ON sin0+ NP cos@Xsin+Y cos",
          "develops a set of rectangular coordinate axes in terms of new coordinates X, Y by means of the relation:",
          "Transformed equations through translation and rotation of axes"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-28",
        "num": "28",
        "title": "Example 28",
        "problem": "Translate to parallel axes through the point (1,-2) the conic 4x+25y-8x+100y+4=0. Solution Substitute x-X+h-X+1(-1) and y-Y+k-Y-2 (k-−2) in the given equation",
        "given": "",
        "method": "",
        "steps": [
          "The standard form of the given conic (ellipse) equation in xy-plane is obtained by backward substitution of X-x+1 and Y-y-2:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-29",
        "num": "29",
        "title": "Example 29",
        "problem": "Transform to axes inclined at an angle 45 to the original axes of the conic",
        "given": "",
        "method": "",
        "steps": [
          "in and new axes with respect to old origin and old axes",
          "This is actually the general transformation (third type) which requires both translation and rotation of axes. The procedure developed is as under:",
          "If O(0,0) is the old origin of the set of old rectangular coordinate axes ox and oy, then the origin of the set of rectangular coordinate axes OX and OY parallel to the old rectangular coordinate axes is O(h, k). Further, the set of new rectangular coordinate axes OX' and OY' is obtained by rotating the rectangular coordinates axes OX and OY through an angle 0,0 < 0 < 90° in anti-clockwise direction.",
          "If the rectangular coordinates of a point P with respect to old rectangular coordinate axes are P(xy), then the rectangular coordinates of a point P with respect to rectangular coordinates axes OX, OY and new rectangular coordinates axes OX',OY' are respectively P(X,Y) and P(X,Y).",
          "develops a set of rectangular coordinate axes in terms of new coordinates X'and 'by means of"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-30",
        "num": "30",
        "title": "Example 30",
        "problem": "Transform to new axes inclined at an angle 45° to the original axes of the conic x2+ y2-8x+4xy-1-0 through (2, 3).",
        "given": "",
        "method": "",
        "steps": [
          "(vi) Angle through which the axes be rotated about the origin so that the product",
          "term xy is removed from the transformed equation",
          "The substitution of the equations of transformation (95- x=Xcos-Ysin0, y=Xsin0+Ycos@",
          "ax2+2kxy+by2=a(Xcos-Ysine) +2hXcos-Ysin 0)(X sin+Y cos 0)+b(Xsine+Y cose)\" = (a cos10+2ksin@cose+bsin 0)x+(-2(-b)sincos+2h(cose-sine)) XY+(asin 0-2hsin cos0+bcos\" ey The expression ax2+2hxy+by will be of the formaX+bY\", if the coefficient of XY term on the right side of the above equation equals zero:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-9-31",
        "num": "31",
        "title": "Example 31",
        "problem": "At what angle the axes are rotated about the origin so that the transformed equation of the",
        "given": "",
        "method": "",
        "steps": [
          "Solution If the axes of the given conic are rotated through an angle 0, then the angle can be fou"
        ],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-9-1",
        "exercise": "Exercise 9.1",
        "title": "Exercise 9.1",
        "description": "",
        "problems": [],
        "pageStart": 241,
        "pageEnd": 285
      },
      {
        "id": "ex-9-2",
        "exercise": "Exercise 9.2",
        "title": "Exercise 9.2",
        "description": "",
        "problems": [],
        "pageStart": 241,
        "pageEnd": 285
      },
      {
        "id": "ex-9-3",
        "exercise": "Exercise 9.3",
        "title": "Exercise 9.3",
        "description": "",
        "problems": [],
        "pageStart": 241,
        "pageEnd": 285
      },
      {
        "id": "ex-9-4",
        "exercise": "Exercise 9.4",
        "title": "Exercise 9.4",
        "description": "",
        "problems": [],
        "pageStart": 241,
        "pageEnd": 285
      },
      {
        "id": "ex-9-5",
        "exercise": "Exercise",
        "title": "Exercise",
        "description": "",
        "problems": [],
        "pageStart": 241,
        "pageEnd": 285
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-10",
    "number": 10,
    "title": "Differential Equations",
    "titleUrdu": "",
    "pageRange": "Printed pages 286–299",
    "pageStart": 286,
    "pageEnd": 299,
    "sections": [
      {
        "id": "sec-10-1",
        "title": "10.1 Ordinary Differential Equations",
        "theory": "A differential equation is an equation that involves the derivatives of an unknown function (dependent variable) of one or more variables (independent variables).\n\n\"If the unknown function depends on only one variable, then the derivative is an ordinary derivative, and the equation is then called an ordinary differential equation.\n\nIf the unknown function depends on more than one variable, then the derivative is partial derivative, and the equation is then called partial differential equation.\n\nThe following differential equations are the examples of ordinary differential equations with their\n\nThe order of a differential equation is the order of the highest-order derivative occurring in the equation c.g.\n\n+(x2+2x)y=7 is second order differential equation.\n\nThe degree of a differential equation is the power of the highest-order derivative occurring in the equation.\n\ndy+(d)-84+2y= 8 is an equation having degree is 1.\n\nSolution Differential equation (a) is an ordinary differential equation of order 1 and degree 1, since the highest ordinary derivative is of order 1 and the exponent of the highest ordinary derivative is 1. Differential equation (b) is an ordinary differential equation of order 2 and degree 1, while Differential equation (c) is an ordinary differential equation of order 3 and degree 2.\n\nA solution of an equation in a single variable is a number which satisfies the equation. In similar fashion, solutions of the differential equations are functions, rather than numbers, which satisfy the differential equation. The variables which appear in equations are called \"unknowns.\" Exactly, the only dependent variable in differential equations is referred to as \"unknown.\"\n\nFor illustration, a solution of the differential equation=1is an expression of the unknown dependent variable y in terms of the independent variable x.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-10-2",
        "title": "10.2 Formation of Differential Equations",
        "theory": "In most of the physical situations, we can observe the process but can not worked out directly to the differential equation. As a result, we have a general solution at our disposal before we know the equation of which it is the solution. Let's begin with the step for forming with differential equation.\n\nDiscover the differential equation that describes a specified physical situation.\n\nFind either exactly or approximately, the appropriate solution of that equation.\n\nLook at the following examples for the concept of formation of a differential equation.\n\nSolution If S() is the unknown distance travel by you w.r.t. 'r' number of hours, then, the rate at which the distance travels is the first derivative of S(1) with respect to r: 5-30, the per hour speed\n\nIntegrating with respect to /to obtain S(n) [d-f30dt+c⇒ S(r) = 30t+c,\n\nthe distance travels by Ali with respect to \"7\" number of hours and the constant quantity e is the fixed distance in this situation.\n\nSolution If P(x) is the unknown animal population w.r.t. x number of years, then, the rate at which the animal population grows is the first derivative of P(x) W.EL X\n\nHere = 0.04 is the constant growth, W= 10,000, is the total size of animal population i habitat. Integrating with respect to x to obtain P(x),\n\nthe total population and c, the fixed population that depends on P-3000 when x = 0. This problem\n\nthe IVP problem with the initial condition P(0)=3000.\n\nFind the order and degree of each the following ordinary differential equations:\n\nIn each case, show that the indicated function is a solution of the differential equation: a. y=e'+e2,\n\nIn each case, use the initial condition and the general solution of the differential equation to determine a particular solution:\n\nSuppose a student carrying Corona Virus returns to an isolated college campus of 1000 students. If it is considered that the rate at which the virus spreads is proportional not only to the number 'x' of infected students but also to the number of students not infected. Find the number of infected students after 6 days. If it is further observed after 4 days = 50.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-10-3",
        "title": "10.3 Solution of Differential Equations",
        "theory": "If the solution of a first order differential equation is not possible by direct integration, then, the integral process (in case of difficulties) for obtaining the solution of a differential equation indicates the actual concept of a differential equation.\n\nWe examine techniques for solving first order differential equations. For this unit, recommended techniques for solving the differential equations are the separation of variables, reducible to separation form, homogeneous and equations reducible to homogeneous\n\nIf the solution of a differential equation is not possible by direct integration, then the integral technique called separation of variables will be used for solving the differential equation. Separation of variables is a technique commonly used to solve first order differential equations. It is so called because we try to rearrange the equation to be solved in such a way that all terms involving the dependent variable ( say) appear on one side of the equation, and all terms involving the independent variable (z. say) appear on the other side. It is not possible to rearrange all first order differential equations in this way so this technique is not always appropriate. Further, it is not always possible to perform the integration even if the variables are separable.\n\nIn general, a differential equation of the form\n\nthat by shifting x on one side and y on the other side g(y)dy=f(x)dx, SDE\n\nis giving a separable differential equation. The solution to separable differential equation (ii) car found by integrating left hand side w.r.t.y and right hand side w.r.t. X. Example 7 Find the general solution of the linear differential\n\nSolution The solution of the given differential equation is not possible by direct integration. The separable form of the given first order differential equation is obtained by shifting y on the left and x on\n\nis giving the general solution of the first order differential equation. This general solution represents a family of exponential functions as shown in the Figure 10.2.\n\nIf the solution of the differential equation is not possible by separable form, then the given differential equa can be reduced in separable form by substitution. This substitution changes the dependent variable formy\n\nDetermine the time necessary for the number of bacteria to be quadruple.\n\nSolution If N() is the unknown number of bacteria w.r.t time r hours, then, the rate at which bacterial grows, is represented by:\n\nReduce the differential equation to separable form\n\nthat on integration is giving the general solution of (i):\n\nThe initial condition N(0)= N, is used in equation (ii) to obtain c\n\nUse c in equation (ii) to obtain a particular solution:\n\nThe condition N(1)= is used in equation (iv) to obtain the value of k\n\nUse the value of in equation (iv) to obtain a particular solution (specific number of bacteria):\n\nThe condition N=4N, (when the bacterial have quadrupled) is used (vi) to obtain the time -\n\nat which the bacteria is four times of the original number of bacterial.\n\nOur experience with first order differential equations has taught us that such equations often have general solutions containing a single arbitrary constant. Each such solution defines a corresponding set of integral curves. A nonempty set of plane curves defined by a differential equation involving just one parameter (single arbitrary constant) is commonly called a one-parameter family of curves. Of special importance in certain applications are those one-parameter families of curves which are orthogonal trajectories of one another.\n\n\"The curves of a family F(x,y,c) are said to be orthogonal trajectories of curves of a family G(x,y,c,), if and only if each curve of either family is intersected by at least one curve of the other family and at every point of intersection of a curve of F with a curve of G, the two curves are perpendicular.\"",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-10-4",
        "title": "10.4 Orthogonal Trajectories",
        "theory": "Define ordinary differential equation (DE), order of a DE, degree of a DE, solution of a DE - general solution and particular solution.\n\nDemonstrate the concept of formation of a differential equation.\n\nSolve differential equations of first order and first degree of the form:\n\nSolve real life problems related to differential equations.\n\nFind orthogonal trajectories (rectangular coordinates) of the given family of curves.\n\nUse MAPLE graphic commands to view the graphs of given family of curves and its orthogonal trajectories.\n\nThe laws of the universe are written in the language of mathematics. Algebra is sufficient to solve many static problems, but the most interesting natural phenomena involve change and are describe only by equations that relates rates at which quantities change.\n\nSuppose the solution of problems concerning the motion of objects, the flow of charged particles, heat transport, etc often involves discussion of relations of the form\n\nIn the first equation, x might represent distance. For this case, is the rate of change of\n\ndy distance with respect to time t that is speed. In the second equation, a might be a charge and is the\n\nrate of flow of charge that is current. These are examples of different equations, so called because these are equations involving the derivatives of various quantities. Such equations arise out of situations in which change is occurring.\n\nIn engineering, differential equations are most commonly used to model dynamic systems. These are the systems which change with time. Examples include an electronic circuit with time-dependent currents and voltages, a chemical production line in which pressure, tank levels, flow rates, etc, vary with time.\n\nThere is a wide variety of differential equations which occur in engineering applications, and consequently there is a wide variety of solution techniques available.\n\nThe two families of curves F(x,y,c) and G(x,y,e) are perpendicular at a point of intersection, il and only if their tangents are perpendicular at the point of intersection. If their tangent lines, say, L, and L2, are perpendicular, then the product of their slopes equals -1:\n\nmm,-1, m, and m, are the slopes of the two tangent lines L, and L\n\nThis is called the differential equation of orthogonal trajectories. If one family of curves F given, then the other family of curves G can be found by solving the differential equation of orthogona\n\nThe differential equation of the orthogonal trajectories (i) with the slope of the given orthogonal trajectories (ii) is used to obtain the other family of curves G of orthogonal trajectories:\n\nThus, the family of curves G represents a family of homogeneous straight lines that pass through the origin. This is the result, we would expect, since the radii of a circle are the homogeneous lines y=Cx, C is any real number) perpendicular to the lines tangent to a circle.\n\nMAPLE graphic commands to view the graphs of given family of curves and its orthogonal trajectories\n\nThe general solution 3(x)=sqrt[-x+] of the above problem in example 12 is the first family of curves. This can also be written as += c. The orthogonal trajectories of a first family of curves is the second family of curves represented by y=Cx.\n\nThis equation can be viewed through command on line by typing MAPLE commands as,\n\nFind general solution of the following differential equations:\n\nReduce the following differential equations in separable form and then solve: a. y=(y+x)2\n\nSolve the following homogeneous differential equations:\n\nReduce the following differential equations in the standard form of homogeneous form and then solve:\n\nThe slope of a family of curves at a point P(x, y) is. Determine the equation of the curve that passes through the point P(4,-3).\n\nFind the solution curve of the differential equation x=3+x which passes through the point P(-1, 2).\n\nFind the real portion from the solution curves of the differential equation xe'dx+ydx=xdy which passes through the point P(1, 0).\n\nA particle moves along the x-axis so that its velocity at any point is equal to half its abscissa three times the time. At a time r=2,x=-4, determine the motion of a particle along the x-axis.\n\ndx dt The rate of consumption of oil (billions of barrels) is given by 1.2, Where 1=0)\n\ncorrespond to 1990. Find the total amount of oil used from 1990 to year 1995. At this rate, how much oil will be used in (t=8) years?\n\ndl 100r dt 2+1 The rate of infection of a disease (in people per month) is given by: Where is the time in months since the disease broke out. Find the total number of infected people over the first four months of the disease.\n\nDetermine the equations of the orthogonal trajectories of the following families of curves.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-10-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Determine the order and degree of the following ordinary differential equations:",
        "given": "",
        "method": "",
        "steps": [
          "A solution of an equation in a single variable is a number which satisfies the equation. In similar fashion, solutions of the differential equations are functions, rather than numbers, which satisfy the differential equation. The variables which appear in equations are called \"unknowns.\" Exactly, the only dependent variable in differential equations is referred to as \"unknown.\"",
          "For illustration, a solution of the differential equation=1is an expression of the unknown dependent variable y in terms of the independent variable x.",
          "\"A solution of an ordinary differential is any function y = f(x) or f(x, y) which when substituted in the differential equation, reduces the differential equation to an identity; that is, it satisfies the"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Show that y=x+A is a solution of the first order differential equation",
        "given": "",
        "method": "",
        "steps": [
          "This shows that y=x+ is a solution of the ordinary differential equation",
          "The solution of a differential equation when depends on a single arbitrary constant quantity, is called the general solution of the first order differential equation. If we give particular steps for value to a single arbitrary constant quantity, then the solution to obtain is called the particular solution. Graphically,",
          "The particular solution is also known as specific solution or exact solution or actual solution.",
          "the general solution of a first order deferential equation represents a family of curves for any choice of arbitrary constant quantity.",
          "The particular solution of a first order differential equation is a particular curve chosen from family of curves (general solution) for a particular value of a constant quantity."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Graphically, show that y=x+A is a",
        "given": "",
        "method": "",
        "steps": [
          "1. Find a particular solution, when x=0 and y = 1.",
          "Solution The general solution y=x+A of a first order differential equation=1, represents a family of",
          "parallel straight lines for different values of arbitrary constant quantities A = 0, 1, 2,...",
          "The particular value for the particular line that passes through a point P(0, 1) can be found from the general solution y=x+A by putting x=0,y=1:",
          "Use this particular value of A= 1 in general solution y=x+A to obtain a particular solution (line) y=x+1.",
          "If we are to determine the solutions of a differential equation subject to conditions on the unknown function and its derivatives specified for one value of the independent variable, the conditions are then called",
          "conditions and the related differential equation is called an initial value problem \"IVP\".",
          "Thus, the problem of example 3 is the initial value problem that leads the notation:"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-4",
        "num": "4",
        "title": "Example 4",
        "problem": "Determine a particular solution for the first order differential equation that satisfies the initial conditions=0, when 1 = 0.",
        "given": "",
        "method": "",
        "steps": [
          "for which the solution is the unknown function () that can be found by integrating directly the first order differential equation with respect to t",
          "The general solution (r)--32r+c at a point P(0, 0) is giving e=0. Use this c=0 in general solution to obtain the particular solutions()=-32",
          "In most of the physical situations, we can observe the process but can not worked out directly to the differential equation. As a result, we have a general solution at our disposal before we know the equation of which it is the solution. Let's begin with the step for forming with differential equation.",
          "Discover the differential equation that describes a specified physical situation.",
          "Find either exactly or approximately, the appropriate solution of that equation.",
          "Look at the following examples for the concept of formation of a differential equation."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-5",
        "num": "5",
        "title": "Example 5",
        "problem": "The rate at which the distance travels by Ali is 30 mph. Find the total distance travels by Ali at a time t hours.",
        "given": "",
        "method": "",
        "steps": [
          "Integrating with respect to /to obtain S(n) [d-f30dt+c⇒ S(r) = 30t+c,",
          "the distance travels by Ali with respect to \"7\" number of hours and the constant quantity e is the fixed distance in this situation."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-6",
        "num": "6",
        "title": "Example 6",
        "problem": "The rate at which the animal population is growing at a constant rate 4%. The habitat support no more than 10,000 animals. There are 3000 animals present now. Find an equation that gives the animal population y w.r.t. x number of years.",
        "given": "",
        "method": "",
        "steps": [
          "Here = 0.04 is the constant growth, W= 10,000, is the total size of animal population i habitat. Integrating with respect to x to obtain P(x),",
          "the total population and c, the fixed population that depends on P-3000 when x = 0. This problem",
          "the IVP problem with the initial condition P(0)=3000.",
          "Find the order and degree of each the following ordinary differential equations:",
          "In each case, show that the indicated function is a solution of the differential equation: a. y=e'+e2,",
          "In each case, use the initial condition and the general solution of the differential equation to determine a particular solution:",
          "Suppose a student carrying Corona Virus returns to an isolated college campus of 1000 students. If it is considered that the rate at which the virus spreads is proportional not only to the number 'x' of infected students but also to the number of students not infected. Find the number of infected students after 6 days. If it is further observed after 4 days = 50.",
          "Leibniz was the German Mathematician and philosopher. He introduced and published the concept of differential equation in (1684). In most of the documents indicated that he knew how to solve the differential equations in 1666.",
          "Sir Isaac Newton was an English Mathematician, Physicist and Astronomer. He never published his \"Method of fluxions\"",
          "Confried Wübelm Leibniz but it is claimed that he discovered it in 1665 to 1667. Which is",
          "If the solution of a first order differential equation is not possible by direct integration, then, the integral process (in case of difficulties) for obtaining the solution of a differential equation indicates the actual concept of a differential equation.",
          "10.3.1 Solution of first order and first degree differential equations",
          "We examine techniques for solving first order differential equations. For this unit, recommended techniques for solving the differential equations are the separation of variables, reducible to separation form, homogeneous and equations reducible to homogeneous",
          "If the solution of a differential equation is not possible by direct integration, then the integral technique called separation of variables will be used for solving the differential equation. Separation of variables is a technique commonly used to solve first order differential equations. It is so called because we try to rearrange the equation to be solved in such a way that all terms involving the dependent variable ( say) appear on one side of the equation, and all terms involving the independent variable (z. say) appear on the other side. It is not possible to rearrange all first order differential equations in this way so this technique is not always appropriate. Further, it is not always possible to perform the integration even if the variables are separable.",
          "In general, a differential equation of the form",
          "that by shifting x on one side and y on the other side g(y)dy=f(x)dx, SDE",
          "is giving a separable differential equation. The solution to separable differential equation (ii) car found by integrating left hand side w.r.t.y and right hand side w.r.t. X. Example 7 Find the general solution of the linear differential",
          "Solution The solution of the given differential equation is not possible by direct integration. The separable form of the given first order differential equation is obtained by shifting y on the left and x on",
          "is giving the general solution of the first order differential equation. This general solution represents a family of exponential functions as shown in the Figure 10.2.",
          "If the solution of the differential equation is not possible by separable form, then the given differential equa can be reduced in separable form by substitution. This substitution changes the dependent variable formy",
          "new variable, say, and keeps x as the independent variable."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-7",
        "num": "8",
        "title": "Example 8",
        "problem": "Find the general solution of the non-linear differential equation (x+y)\".",
        "given": "",
        "method": "",
        "steps": [
          "in the given differential equation to obtain separable differential",
          "Integrating equation (1) to obtain the general solution of ordinary differential equation (i).",
          "the general solution of the given ordinary differential equation that depends on a single arbitrary",
          "The homogeneous differential equations are related to homogeneous functions.",
          "\"A function f(x, y) is homogeneous function of degree n in variables x and y if and only if for all values of the variables x and y and for every positive value of 7, the identity is true.",
          "For illustration, the function f(x,y)=x+yis homogeneous function of degree 2, since the identity (1) is true:",
          "The identity (i) is not true for a function f(x,y)=x+y+1, since the function is not homogeneous.",
          "is called a homogenous differential equation, if it defines a homogenous function of degree zero.",
          "The homogeneous differential equation (ii) can be reduced to separable form by introducing a",
          "The substitution of (iii) in equation (ii) automatically converts the homogeneous differential equation in separable differential equation."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-8",
        "num": "8",
        "title": "Example 8",
        "problem": "Find the general solution of the homogeneous differential equation:",
        "given": "",
        "method": "",
        "steps": [
          "Solution The given differential equation defines a homogeneous function of degree zero, when the function on the right of the given differential equation defines a homogeneous function of degree zero:",
          "The given homogeneous differential equation is used for the assumptions",
          "to obtain a separable differential equation of the form:",
          "Integrating SDE (ii) to obtain the general solution of the SDE (ii):",
          "is used in equation (iii) to obtain the general solution of the given",
          "the homogeneous form by taking new variable x and y such that x=X+h and y=Y+k, where hand",
          "k are constants to be choosen as to make the given equation homogeneous.",
          "Now, by choosing & and such that a+b+c=0 and h÷bk+q= So, the differential equation becomes."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-9",
        "num": "10",
        "title": "Example 10",
        "problem": "Find the general solution of the differential equation x=x+y.",
        "given": "",
        "method": "",
        "steps": [
          "Divide out by x to obtain the standard form of homogeneous differential equation:",
          "Homogeneous differential equation (i) is used for the assumptions",
          "to obtain a separable differential equation of the form:",
          "Integrating the SDE (i) to obtain the general solution of the SDE (ii):",
          "that by back substitution is giving Ince ⇒y=xhe",
          "If the differential equation not homogeneous differential equation, then it might be a nonhomogeneous differential equation.",
          "the general solution of the given homogeneous differential equation that depends on a single arbitrary",
          "10.3.2 Solve real life problems related to differential equation"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-10",
        "num": "11",
        "title": "Example 11",
        "problem": "A certain bacteria grows at a rate that is proportional to the number present at a particular time. If the number of bacterial at a time = 0 is N, and at time = 1 hour, the number of bacteria is",
        "given": "",
        "method": "",
        "steps": [
          "Solution If N() is the unknown number of bacteria w.r.t time r hours, then, the rate at which bacterial grows, is represented by:",
          "Reduce the differential equation to separable form",
          "that on integration is giving the general solution of (i):",
          "The initial condition N(0)= N, is used in equation (ii) to obtain c",
          "Use c in equation (ii) to obtain a particular solution:",
          "The condition N(1)= is used in equation (iv) to obtain the value of k",
          "Use the value of in equation (iv) to obtain a particular solution (specific number of bacteria):",
          "The condition N=4N, (when the bacterial have quadrupled) is used (vi) to obtain the time -",
          "at which the bacteria is four times of the original number of bacterial.",
          "Our experience with first order differential equations has taught us that such equations often have general solutions containing a single arbitrary constant. Each such solution defines a corresponding set of integral curves. A nonempty set of plane curves defined by a differential equation involving just one parameter (single arbitrary constant) is commonly called a one-parameter family of curves. Of special importance in certain applications are those one-parameter families of curves which are orthogonal trajectories of one another.",
          "\"The curves of a family F(x,y,c) are said to be orthogonal trajectories of curves of a family G(x,y,c,), if and only if each curve of either family is intersected by at least one curve of the other family and at every point of intersection of a curve of F with a curve of G, the two curves are perpendicular.\"",
          "10.4.1 Orthogonal trajectories of the given family of curves",
          "The two families of curves F(x,y,c) and G(x,y,e) are perpendicular at a point of intersection, il and only if their tangents are perpendicular at the point of intersection. If their tangent lines, say, L, and L2, are perpendicular, then the product of their slopes equals -1:",
          "mm,-1, m, and m, are the slopes of the two tangent lines L, and L",
          "This is called the differential equation of orthogonal trajectories. If one family of curves F given, then the other family of curves G can be found by solving the differential equation of orthogona"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-10-11",
        "num": "12",
        "title": "Example 12",
        "problem": "Determine the orthogonal trajectories of the family of curves (circles)x+y=c. Solution To determine the orthogonal trajectories of the circles, we need to determine the slope (derivative) of the family of circles",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-10-1",
        "exercise": "Exercise 10.1",
        "title": "Exercise 10.1",
        "description": "",
        "problems": [
          {
            "id": "ex-10-1-q1",
            "qNo": "1",
            "question": "Find the order and degree of each ordinary differential equation in parts (a–d) on the textbook page.",
            "solution": "The order is the highest derivative present; the degree is its power after the equation is polynomial in derivatives. (a) First order, degree 1. (b) Second order, degree 1. (c) Third order, degree 1. (d) Second order, degree 1.",
            "diagram": null
          },
          {
            "id": "ex-10-1-q4",
            "qNo": "4",
            "question": "Solve the initial-value problems: (a) y'=cos x, y(0)=1; (b) y'=x², y(0)=1; (c) y'=1/x, y(2)=0; (d) y'=2xy², y(3)=−1.",
            "solution": "Integrate and use the initial condition. (a) y=sin x+C, and y(0)=1 gives y=sin x+1. (b) y=x³/3+C, so y=x³/3+1. (c) y=ln|x|+C; y(2)=0 gives y=ln(x/2) on x>0. (d) Separate: y^{−2}dy=2x dx, so −1/y=x²+C. The condition gives C=−8; therefore y=−1/(x²−8), on the interval containing x=3 where the solution is defined.",
            "diagram": null
          }
        ],
        "pageStart": 286,
        "pageEnd": 299
      },
      {
        "id": "ex-10-2",
        "exercise": "Exercise 10.2",
        "title": "Exercise 10.2",
        "description": "",
        "problems": [
          {
            "id": "ex-10-2-q1",
            "qNo": "1a",
            "question": "Find the general solution of (dy/dx)²=1−y².",
            "solution": "Separate variables: dy/√(1−y²)=±dx. Integrating gives sin^{−1}y=±x+C, equivalently y=sin(±x+C), on intervals where the separation is valid.",
            "diagram": null
          },
          {
            "id": "ex-10-2-q1b",
            "qNo": "1b",
            "question": "Find the general solution of e^x(dy/dx)+y=0.",
            "solution": "Rewrite y'/y=−e^{−x}. Integrate: ln|y|=e^{−x}+C. Thus y=C e^{e^{−x}}.",
            "diagram": null
          },
          {
            "id": "ex-10-2-q1c",
            "qNo": "1c",
            "question": "Solve √(1−x²)dy=√(1−y²)dx.",
            "solution": "Separate: dy/√(1−y²)=dx/√(1−x²). Integrating both sides gives sin^{−1}y=sin^{−1}x+C.",
            "diagram": null
          },
          {
            "id": "ex-10-2-q5",
            "qNo": "5",
            "question": "A curve has slope dy/dx=1/(1−x) and passes through (4,−3). Determine its equation.",
            "solution": "Integrate: y=−ln|1−x|+C. Substitute (4,−3): −3=−ln3+C, so C=−3+ln3. Since the curve passes through x=4>1, y=−3+ln(3/(x−1)).",
            "diagram": null
          },
          {
            "id": "ex-10-2-q9",
            "qNo": "9",
            "question": "Oil consumption is dW/dt=1.2e^{0.04t} billion barrels per year. Find the total used over eight years, t=0 to 8.",
            "solution": "Integrate the rate: W(8)−W(0)=∫₀⁸1.2e^{0.04t}dt=(1.2/0.04)(e^{0.32}−1)=30(e^{0.32}−1)≈11.32 billion barrels.",
            "diagram": null
          },
          {
            "id": "ex-10-2-q10",
            "qNo": "10",
            "question": "The infection rate is dI/dt=100t/(t²+1) people per month. Find the total number infected during the first four months.",
            "solution": "Integrate from 0 to 4: I(4)−I(0)=∫₀⁴ 100t/(t²+1)dt=50[ln(t²+1)]₀⁴=50ln17≈141.67 people. The total is about 142 people if rounded to a whole person.",
            "diagram": null
          }
        ],
        "pageStart": 286,
        "pageEnd": 299
      },
      {
        "id": "ex-10-3",
        "exercise": "Review Exercise 10",
        "title": "Review Exercise 10",
        "description": "",
        "problems": [],
        "pageStart": 286,
        "pageEnd": 299
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-11",
    "number": 11,
    "title": "Partial Differentiation",
    "titleUrdu": "",
    "pageRange": "Printed pages 300–308",
    "pageStart": 300,
    "pageEnd": 308,
    "sections": [
      {
        "id": "sec-11-1",
        "title": "11.1 Differentiation of Functions of Two Variables",
        "theory": "\"A function == f (x, y) is a function of two variables x and y. if for each given pair (x, y), we determine a single value of \"Where, x, y and are real variables.\n\nThe real numbers x and y are independent variables; z is the dependent variable. The set of all ordered pairs of real numbers (x, y) such that f(x, y) is a real number, is the domain off and the set of\n\nFor this function, we need to show the transformation of two independent variables (inputs) x and y' is just a single dependent variable z. In respect of any two real values of independent variables x and\n\nThe function = f(x,y)=√1-x+y is therefore declared a function of two independent variables x and y.\n\nThe domain of f(x, y) is the set of all ordered (x, y) for which\n\n1-x+y is defined. We must have 1-x+y20 or y2x-1, in order for the square root to be defined. In a function z = f(x, y)=√1-x+y, we see that f(x, y) must be nonnegative and the range off(x, y) is all 20\n\nTo give clear concept to partial derivative, the problem related to our real-life situations is considered as:\n\nSuppose, a small firm makes only two products, radios and audiocassette recorders. The profit of\n\n(1) the firm from these two products is given by: P(x, y)=40x-10x+5y-80, Where x is the number of units of radios sold and y is the number of units of recorders sold. How changes in x will (radios) or y (recorders) affects P (profit)?\n\nSuppose that sales of radios have been steady at 10 units; only the sales of recorders vary. The management would like to find the rate (marginal profit/ derivative of the profit function) at which the y number of recorders sold.\n\nIf x is fixed at 10 units, then this information reduces the profit two variables function to single variable function that can be found from equation (i) by putting x = 10:\n\nThe function P(10, y) shows the profit from the sales of y recorders, assuming that x is fixed at 10 units. The rate, at which the y number of recorders sold, is the ordinary derivative of P(10, y) with\n\nThis represents the per unit profit from y number of audiocassette recorders.\n\nThe notation of P(10,y) is usually stands for ordinary derivative, when the function is a single variable function. In our case, the profit function () is a function of two variables; its rate with respect to y should be a partial derivative. For partial derivative with respect to y derivative in equation (ii) is replaced by P(10,y) to obtain\n\naPP(10,y) = P-100+10y, prime notation \"/\" is not allowed.\n\nthe partial derivative f(x,y) with respect to x is the derivative of f(x,y) obtained by keeping\n\nf(x,y) with respect to y is the derivative off (xy) obtained by keeping\n\ny as a variable and x as a constant quantity.\n\n\"If == f(x,y) is a function of two variables, then the first partial derivatives of = f(x, y) with respect to x and y are the functions f, and f, respectively, defined by,\n\nThe function is z=xsin (3x+y). Find z, and z, at a point (.0).\n\nSolution The partial derivative of z (x, y) w.rt. x is:\n\n=2xsin(3x+y\")+x* cos(3x+y) (3x+y)=2.xsin(3x+y)+x\" cos(3x+y)(3+0) -2xsin(3x+y)+3x2 cos(3x+y)\n\nWhere x represents the temperature of the river water in degree Celsius before it reaches the power plant and y is the number of megawatts (in hundreds) of electricity being produced by the plant.\n\n4. The partial derivative of (i) w.r.t..x is the rate of change in 7 with respect to x. 7=2+y, y is constant\n\nThis rate with x-9 and y = 5 is [T] =2+y=2+5=7 the approximate change in temperature resulting from a one degree increase in input water, if the input electricity y remains constant at 500 b. The partial derivative of (i) w... y is the rate of change in T with respect to y: T, =5+x, x is constant This rate with x-9 and 3-5 is [T] =5+x-5+9-14 the approximate change in temperature resulting from a one megawatt increase in production of electricity if the input water temperature x\n\nlf ƒ'(x,y) = x2y + xy2 and t is any real number, then find out the following:\n\nThe function is f(x,y,z) = x*′ye2 +(x+y−2). Find the fuction value at the following points:\n\nThe production function z for the United States was once estimated as:\n\nWhere x stands for the amount of labor and y stands for the amount of capital. Find the marginal productivity of labor\n\nWhere. stands for the amount of labor and y stands for the amount of capital. Find the margina\n\nIf ƒ′(x,y) = x2y+xy2, then find f, and f, by using definition of partial derivatives.\n\nLeonhard Euler was a Swiss Mathematician, Physicist, Astronomer and Engineer. He made the important and influential contributions in many branches of Mathematics, such as calculus, graph theory, topology and analytic number theory. He also made significant contribution in mechanics, fluid dynamics, optics and music theory, He was the first person who introduced f(x) to denoted the function fapplied to the argument \"X\". In 1735 he introduced a theorem known by his name Euler theorem.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-11-2",
        "title": "11.2 Euler's Theorem",
        "theory": "Find partial derivatives of a function of two variables. Euler's Theoreni\n\nState and prove Euler's theorem on homogeneous functions.\n\nVerify Euler's theorem for homogeneous functions of different degrees (simple cases).\n\nUse MAPLE command diff to find partial derivatives.\n\nThe goal of this unit is to extend the methods of single variable differential calculus to functions of two variables. In many practical situations, the value of one quantity may depend on the values of two or more others. For example, the amount of water in a reservoir may depend on the amount of rainfall and on the amount of water consumed by local residents. The current in an electrical circuit may vary with the electromotive force, the capacitance, the resistance, and the impedance in the circuit. The flow of blood from an artery into a small capillary may depend on the diameter of the capillary and the pressure in both the artery and the capillary. The output of a factory may depend on the amount of capital invested in the plant and on the size of the labor force. We will analyze such situations using functions of several variables.\n\nIn many problems involving functions of several variables, the goal is to find the derivative of the function with respect to one of its variables when all the others are held constant. In this unit, we need to develop the concept and shall see how it can be used to find slopes and rates of change in case of two variables function.\n\n11.1. Differentiation of the function of two variables\n\nIn the real world, physical quantities often depend on two or more variables. For example, we might be concerned with the temperature on a metal plate at various points at time r. The locations of temperature on the plate are given as ordered pairs (x, y), so that the temperature T can be considered as a function of two location variables x and y, as well as a time variable r. The notation of a function of single variable, we might extend this as T(x,y,). We begin our study of function of two variables by examining this notation and a few other basic concepts.\n\n\"A function f(x, y) is said to be a homogeneous function of degree n if, for all values of & and some constant values of n, we have\n\na. f(x,y)=3x+4y is a homogeneous function of degree 1.\n\nb. f(x,y)=3x2+4y' is a homogeneous function of degree 2.\n\nhomogeneous of degree n if, for all values of A and some constant\n\nA homogeneous function can also define another way.\n\n\"A function (x, y) is said to be homogeneous function of degree n if it is expressed in the form\n\nSolution The function f(x,y)=2x+y is a homogeneous function of degree 2, if the identity (i) is\n\nThus, the given function is a homogeneous function of degree 2.\n\nStatement: If z=f(x, y) is continuously differentiable and defines a homogeneous function of\n\nProof: If z=xf, then, its partial derivatives with respect x and y are the following:\n\nThe addition of the products of (ii) by x and y (iii) by y to obtain the Euler's method of order n\n\nSolution The homogeneous function and its derivatives\n\nz= f(x,y) = ax2+2bxy+cy\", -2ax+2by, -2bx+2ey are used in Euler's result (iv) to confirm the degree of homogeneous function:\n\nThe Euler's procedure confirmed the second degree of homogeneous function.\n\na The function = (x, y) is not a homogeneous function, however, it can be reduced to homogeneous form by introducing a new variable ::\n\nThe given function is a homogeneous of degree 2. The Euler's theorem in thi\n\nThe partial derivatives ofz-tan u w... x and y\n\nare substituting in (i) to obtain the required result:\n\nLook at the following example he use of MAPLE command \"diff\" is illustrated in this examples. Example 8 Use MAPLE command \"diff\" to find the partial derivation of\n\n(a). ƒ(x,y) = x2+y2+3x+4x3y w.r.t, variables x and y.\n\n(b) f(x,y)=ysinx+xcosy+x w..., variables x and y. Solution\n\nUsing Palettes: Use cursor button to select expression in which you are interested. In this problem, the expression is partial derivative palette. Click-partial derivative palette, insert the given function, then press \"ENTER\" key to obtain the partial derivatives of a given function:\n\nVerify Euler's theorem for the following homogeneous functions:\n\nUse MAPLE command \"diff\" to find the partial derivation of\n\n(b). dependent variables (d). dependent constants\n\nvi. The functions of more than one independent variables are called:\n\nvii. If f(x,y,z) = √x2+y'-z, then ƒ(1, 0, 1) is:\n\nA function = (x, y) is a function of two variables x and y, if a unique of is obtained from each ordered pair of real numbers (x, y). The real numbers x and y are independent variables; is the dependent variable. The set of all ordered pairs of real numbers (x, y) such that f(x, y) is a real number, is the domain of fand the set of all values off(x, y) is the range.\n\n→ A polynomial function in x and y is the sum of functions of the form\n\nIf r=√(x,y) is a function of two variables, then the first partial derivatives of z = f(x, y) with respect to x and y are the functions /, and /, respectively, defined by,\n\nf(x,y)-lim f(x+Ax, y) = f(x,y), f,(x, y) = lim f(x,y+Ay)-f(x,y)\n\nA function f(x, y) is a homogeneous function of degree n in variables x and y, if for all values of the variables and for every positive value of, for which the identity is true:\n\nThe specialty of Euler's theorem is to verify the degree of a homogeneous function. The homogeneous function is a function f(x, y) not altered if the real numbers x and y of a function ==ƒ(x, y) are stretched or squeezed by any real scalar quantity)...",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-11-1",
        "num": "1",
        "title": "Example 1",
        "problem": "How to show that = f(x,y)=√1-x+y is a function of two independent variables.x and y? Find also the domain and range of a given function.",
        "given": "",
        "method": "",
        "steps": [
          "The function = f(x,y)=√1-x+y is therefore declared a function of two independent variables x and y.",
          "The domain of f(x, y) is the set of all ordered (x, y) for which",
          "1-x+y is defined. We must have 1-x+y20 or y2x-1, in order for the square root to be defined. In a function z = f(x, y)=√1-x+y, we see that f(x, y) must be nonnegative and the range off(x, y) is all 20",
          "To give clear concept to partial derivative, the problem related to our real-life situations is considered as:",
          "Suppose, a small firm makes only two products, radios and audiocassette recorders. The profit of",
          "(1) the firm from these two products is given by: P(x, y)=40x-10x+5y-80, Where x is the number of units of radios sold and y is the number of units of recorders sold. How changes in x will (radios) or y (recorders) affects P (profit)?",
          "Suppose that sales of radios have been steady at 10 units; only the sales of recorders vary. The management would like to find the rate (marginal profit/ derivative of the profit function) at which the y number of recorders sold.",
          "If x is fixed at 10 units, then this information reduces the profit two variables function to single variable function that can be found from equation (i) by putting x = 10:",
          "The function P(10, y) shows the profit from the sales of y recorders, assuming that x is fixed at 10 units. The rate, at which the y number of recorders sold, is the ordinary derivative of P(10, y) with",
          "This represents the per unit profit from y number of audiocassette recorders.",
          "The notation of P(10,y) is usually stands for ordinary derivative, when the function is a single variable function. In our case, the profit function () is a function of two variables; its rate with respect to y should be a partial derivative. For partial derivative with respect to y derivative in equation (ii) is replaced by P(10,y) to obtain",
          "aPP(10,y) = P-100+10y, prime notation \"/\" is not allowed.",
          "the partial derivative f(x,y) with respect to x is the derivative of f(x,y) obtained by keeping",
          "f(x,y) with respect to y is the derivative off (xy) obtained by keeping",
          "y as a variable and x as a constant quantity.",
          "11.1.3 Partial derivatives of a function of two variables",
          "\"If == f(x,y) is a function of two variables, then the first partial derivatives of = f(x, y) with respect to x and y are the functions f, and f, respectively, defined by,"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-11-2",
        "num": "2",
        "title": "Example 2",
        "problem": "If function is f(x,y)=xy+xy. Find partial derivatives, and f Solution The partial derivatives of f(x, y) w.r.t. x and y are the following:",
        "given": "",
        "method": "",
        "steps": [],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-11-3",
        "num": "3",
        "title": "Example 3",
        "problem": "The function is",
        "given": "",
        "method": "",
        "steps": [
          "=2xsin(3x+y\")+x* cos(3x+y) (3x+y)=2.xsin(3x+y)+x\" cos(3x+y)(3+0) -2xsin(3x+y)+3x2 cos(3x+y)"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-11-4",
        "num": "4",
        "title": "Example 4",
        "problem": "Suppose that the temperature of the water at the point on a river where a nuclear power plant discharges its hot waste water is approximated by T(x,y)=2x+5y+xy=40",
        "given": "",
        "method": "",
        "steps": [
          "4. The partial derivative of (i) w.r.t..x is the rate of change in 7 with respect to x. 7=2+y, y is constant",
          "This rate with x-9 and y = 5 is [T] =2+y=2+5=7 the approximate change in temperature resulting from a one degree increase in input water, if the input electricity y remains constant at 500 b. The partial derivative of (i) w... y is the rate of change in T with respect to y: T, =5+x, x is constant This rate with x-9 and 3-5 is [T] =5+x-5+9-14 the approximate change in temperature resulting from a one megawatt increase in production of electricity if the input water temperature x",
          "lf ƒ'(x,y) = x2y + xy2 and t is any real number, then find out the following:",
          "The function is f(x,y,z) = x*′ye2 +(x+y−2). Find the fuction value at the following points:",
          "The production function z for the United States was once estimated as:",
          "Where x stands for the amount of labor and y stands for the amount of capital. Find the marginal productivity of labor",
          "Where. stands for the amount of labor and y stands for the amount of capital. Find the margina",
          "If ƒ′(x,y) = x2y+xy2, then find f, and f, by using definition of partial derivatives.",
          "Leonhard Euler was a Swiss Mathematician, Physicist, Astronomer and Engineer. He made the important and influential contributions in many branches of Mathematics, such as calculus, graph theory, topology and analytic number theory. He also made significant contribution in mechanics, fluid dynamics, optics and music theory, He was the first person who introduced f(x) to denoted the function fapplied to the argument \"X\". In 1735 he introduced a theorem known by his name Euler theorem.",
          "The specialty of Euler's theorem is to verify the degree of a homogeneous function. The homogeneous function is a function = (x, y) not altered if the real numbers x and y of a function z=f(x,y) are stretched or squeezed by any real scalar quantity 7.",
          "\"A function f(x, y) is said to be a homogeneous function of degree n if, for all values of & and some constant values of n, we have",
          "a. f(x,y)=3x+4y is a homogeneous function of degree 1.",
          "b. f(x,y)=3x2+4y' is a homogeneous function of degree 2.",
          "homogeneous of degree n if, for all values of A and some constant",
          "A homogeneous function can also define another way.",
          "\"A function (x, y) is said to be homogeneous function of degree n if it is expressed in the form"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-11-5",
        "num": "5",
        "title": "Example 5",
        "problem": "Show that the function /(x,y)=2xy+y is a homogeneous function of degree 2.",
        "given": "",
        "method": "",
        "steps": [
          "Thus, the given function is a homogeneous function of degree 2.",
          "11.2.2 Verification of Euler's theorem for homogeneous functions of different",
          "Statement: If z=f(x, y) is continuously differentiable and defines a homogeneous function of",
          "Proof: If z=xf, then, its partial derivatives with respect x and y are the following:",
          "The addition of the products of (ii) by x and y (iii) by y to obtain the Euler's method of order n"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-11-6",
        "num": "6",
        "title": "Example 6",
        "problem": "Use Euler's theorem to verify that the function z= f(x,y) = ar2+2hxy+cy\" homogeneous function of degree 2.",
        "given": "",
        "method": "",
        "steps": [
          "z= f(x,y) = ax2+2bxy+cy\", -2ax+2by, -2bx+2ey are used in Euler's result (iv) to confirm the degree of homogeneous function:",
          "The Euler's procedure confirmed the second degree of homogeneous function."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-11-7",
        "num": "7",
        "title": "Example 7",
        "problem": "If u tan",
        "given": "",
        "method": "",
        "steps": [
          "The given function is a homogeneous of degree 2. The Euler's theorem in thi"
        ],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-11-1",
        "exercise": "Exercise 11.1",
        "title": "Exercise 11.1",
        "description": "",
        "problems": [
          {
            "id": "ex-11-1-q4",
            "qNo": "4",
            "question": "A production function is z=f(x,y)=x^{0.7}y^{0.3}, where x is labor and y is capital. Find the marginal productivity of labor and capital.",
            "solution": "Hold y constant when differentiating with respect to x: ∂z/∂x=0.7x^{−0.3}y^{0.3}. Hold x constant when differentiating with respect to y: ∂z/∂y=0.3x^{0.7}y^{−0.7}.",
            "diagram": null
          },
          {
            "id": "ex-11-1-q5",
            "qNo": "5",
            "question": "For the Canadian production function z=f(x,y)=x^{0.4}y^{0.6}, find marginal productivity of labor and capital.",
            "solution": "Treat the other input as a constant in each partial derivative: ∂z/∂x=0.4x^{−0.6}y^{0.6}; ∂z/∂y=0.6x^{0.4}y^{−0.4}.",
            "diagram": null
          },
          {
            "id": "ex-11-1-q6",
            "qNo": "6",
            "question": "For f(x,y)=x²y+xy², find f_x and f_y from the definition of partial derivatives.",
            "solution": "By definition, f_x=lim_{h→0}[f(x+h,y)−f(x,y)]/h. Expanding gives [(x+h)²y+(x+h)y²−x²y−xy²]/h=2xy+hy+y²; as h→0, f_x=2xy+y². Similarly, f_y=lim_{k→0}[f(x,y+k)−f(x,y)]/k=x²+2xy.",
            "diagram": null
          }
        ],
        "pageStart": 300,
        "pageEnd": 308
      },
      {
        "id": "ex-11-2",
        "exercise": "Exercise 11.2",
        "title": "Exercise 11.2",
        "description": "",
        "problems": [],
        "pageStart": 300,
        "pageEnd": 308
      },
      {
        "id": "ex-11-3",
        "exercise": "Review Exercise 11",
        "title": "Review Exercise 11",
        "description": "",
        "problems": [],
        "pageStart": 300,
        "pageEnd": 308
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  },
  {
    "id": "unit-12",
    "number": 12,
    "title": "Introduction to Numerical Methods",
    "titleUrdu": "",
    "pageRange": "Printed pages 309–325",
    "pageStart": 309,
    "pageEnd": 325,
    "sections": [
      {
        "id": "sec-12-1",
        "title": "12.1 Numerical Solution of Non-linear Equations",
        "theory": "Explain the basic principles of solving a non-linear equation in one variable.\n\nCalculate real roots of a non-linear equation in one variable by\n\nUse MAPLE command solve to find numerical solution of an equation and demonstrate through examples. Numerical quadrature\n\nto compute the approximate value of definite integrals without error terms.\n\nUse MAPLE command trapezold for trapezoidal rule and simpson for Simpson's rule and demonstrate through examples.\n\nScientists, economists, engineers, and other researchers study relationships between quantities. For example, an engineer may need to know how the illumination from a light source on an object is related to the distance between the object and the source; a biologist may wish to investigate how the population of a bacterial colony varies with time in the presence of a toxin; an economist may wish to determine the relationship between demand for a certain commodity and its market price. The mathematical study of such relationships involves the concept of non-linear equations. For example, the value of the assets of a certain company at time years is modeled by a non-linear equation f(t)=100,000-75,000e where t is measured in years. The standing rule for solving non-linear equations algebraic is quadratic formula. In this case, it is not valid to obtain the actual number of r (years) at which the asset function (r) is going to be zero. Now we are in position to obtain the approximate number of year's t that can be found by using some numerical procedures. In this unit, we will learn the numerical procedures recommended are the bracketing methods and iterative methods.\n\nNumerical analysis is the theory of constructive methods in mathematical analysis. Constructive methods in their turn mean a procedure that permits us to obtain the solution of a mathematical problem with an arbitrary precision in a finite number of steps that can be prepared rationally.\n\nNumerical analysis is both a Science and an Art. As a Science, it is concerned with the proces by which a mathematical problem can be solved arithmetically. As an Art, numerical analysis in concerned with choosing that procedure which is best suited to the solution of a particular problem.\n\nStudents learning numerical solution of non-linear equations should have the following objectives in view. First, he should obtain an intuitive and working understanding of some numerica methods for the basic problems of numerical analysis. Second, he should gain some appreciation of the concept of error and of the need to analyze and predict it. Third, he should develop some experience i the implementation of numerical method by using computer software.\n\n\"If ƒ (x) is any continuous function of a single variable x. then any number r for which { {r}\"\n\nis called a root of f(x) = 0. Also we say that is a zero of the junction f(x).\n\nIf f(x) is any algebraic function (non-linear equation), then the actual roots of f(x) can be found by direct rules, such as quadratic formula, common factors procedure and synthetic division.\n\nFor example, the quadratic equation x2+5x+6=0 has two actual (or exact) roots r=-2 and =-3obtained by common factors procedure/quadratic formula:\n\nOn the other hand, the actual roots of non-algebraic equation x+5x+6=0 are not possible by applying quadratic formula. The only way is to find out the approximate roots that can be found by using some numerical procedures. The numerical procedures are the bracketing methods and iterative methods.\n\nFor approximate roots of a non-linear equations, the numerical procedures Bisection method and regula-falsi method are the bracketing methods that depend on two initial approximations that must be in the shape of a closed interval [a, b].\n\nThe non-linear curve (1) has the function values f(a) and (b) in the interval [a, b] that must be opposite in signs for showing its continuity. Once the interval has been found, no matter how large, the iteration will be preceded until an approximate root is obtained. The fundamental principle in computer science is the iteration. As the name suggests, it means that a process of bisection or regula- falsi method is repeated until an answer is achieved.\n\nIf y f(x) is continuous function in the interval [a, b], then, it will cross the x-axis at point (r,0) whose x-coordinate x = r will keep as actual root that lies somewhere in the interval [4, b]. This is shown in the Figure 12.1.\n\nThe bisection method systematically moves the endpoints of the interval [a,b] closer and closer together till it reaches an interval of small width that brackets the root r. The decision step for this process of interval halving is to\n\nI. If the function values f(a) and (c) at xa and xe have opposite signs, then the approximate\n\nIf the function values f(c) and (b) at x=e and x-b have opposite signs, then the approximate root lies in interval [e, b] and discard a\n\nIf the function value at x=c is f(c)=0, then e is our approximate root to actual root r.\n\nIf either of cases 1 or 2 occurs, we have an interval half as wide as the original interval that contains the root, and we are \"squeezing down on it see Figure 12.1. To continue the process, relabel the new smaller interval and repeat the sequence of nested intervals and their midpoints.\n\nThe given interval[a,b] is the initial interval at which the function f(x) must be opposite in signs. At this stage, the initial interval brackets the actual root r whose midpoint is c = (a+b)\n\nMAPLE command \"fsolve\" to find numerical solution of an equation and demonstrate through examples\n\nThe use of MAPLE command \"solve\" to find the approximate solution of given function is illustrated in the following example.\n\n(a). Linear equation x-5x+6=0 with initial start x = 1.8.\n\n(b). Nonlinear equation x2-5x+6=0 with initial start x = 0.5.\n\nSolution The command below will show you full detail of the approximate root of linear and non- linear equations on line by typing without initial start:\n\nThe quadratic function f (x) is also a second degree polynomial. The numerical solution through polynomial is:\n\nhis result is obtained through right-click on the last end of the expression by selecting \"Solve Numerically Solve\" on the context menu.\n\nFind an interval asxsb at which (a) and (b) have opposite signs for the following\n\nCompute four iterates of the bisection method for the following functions with indicated\n\nCompute four iterates of the regula-falsi method for the following functions with indicated.\n\nWhat will happen if the bisection method is used with the function f(x)=x-2)\n\nFind iteratex, of Newton-Raphson iterative method for the following functions with initial start.x,\n\nUse Newton-Raphson iterative method to approximate the actual of the following non-linear equations with indicated interval:\n\nContinue the process until two consecutive iterates will agree to three decimal places. Use MAPLE command \"solve\" to solve 3x+4x-3-0 with initial start at x=0.5\n\nQusta Ibn Luqa was a Syrian mathematician, astronomer and philosopher. He contribute\n\nmany fields of science, medicine, astronomy. His translation on the difference between the spirit and the soul was one of the few works not attributed to Aristotle that was included in a list of books to be read or lectured on. He was the first person to write the double false position in 10 century. He justified the technique by a formal, Euclidean-style geometric proof, within the tradition of Muslim nathematics. Double false position was known as Hisab-al-Khata'ayn. It was used for centuries to solve practical problems such as commercial and recreational problems.",
        "rules": [],
        "keyPoints": []
      },
      {
        "id": "sec-12-2",
        "title": "12.2 Numerical Quadrature",
        "theory": "the integral Numerical integration is a primary tool used by engineers and scientists to obtain approximate solutions for definite integrals that cannot be solved analytically. For example,\n\nhas no actual solution. This means that there is no any integral formula that could be used directly to obtain the actual solution. The only way is to find out the approximate solution the: can be found by using some numerical procedures, such, as numerical integration.\n\nWe now approach the subject of numerical integration. The goal is to approximate the definite integral of f(x)\n\nover the interval [a, b] by evaluating f(x) at a finite number of equally spaced grid points:\n\nis called a numerical integration or quadrature formula.\n\nThe term E [f(x)] is called the truncation error for integration. The values quadrature nodes and {w, are called the weights.\n\nDepend on the given numerical procedure, the grid points (x,) are chosen in various ways. For trapezoidal rule and Simpson's rule, the grid points are chosen to be equally spaced. Before discussion of trapezoidal rule and Simpson's rule it must be familiar about approximation by rectangles and approximate area by rectangles.\n\nIf ƒ(x)=0 is a function over the interval [a, b], then the definite integral (ii) represents the actual area under the graph of f(x) on the interval [a, b]. This is shown in the Figure 12.4.\n\nFor approximate area, the function f(x) must be known at equally spaced grid points in the interval[a, b], each of width Ax=(b-a)/n:\n\nIn light of above equally spaced grid points, the actual area (ii) under a curve f(x) over the interval [a, b] is rearranged as under:\n\nConsider the initial subinterval[1,4]. Let x, denote the right endpoint of the initial subinterval, and the base of the rectangle is of course the initial subinterval and its height is f(x). The area of the rectangle in the initial subinterval is therefore f(x)Ax.\n\nIf f(x)dris the actual area in the initial subinterval, then the approximate area f(x)Axis of course the area of the rectangle lies in the initial subinterval [xx]. Thus, the sum of the areas of all rectangles is giving approximate area under the curve f(x) to actual area represented by definite integral (iv),\n\nThis approximation improves as the number of rectangles increases, and we can estimate the integral to any desired degree of accuracy by taking a large enough. However, because fairly large values of a are usually required to achieve reasonable accuracy, approximation by rectangic is rarely used in practice.",
        "rules": [],
        "keyPoints": []
      }
    ],
    "workedExamples": [
      {
        "id": "we-12-1",
        "num": "1",
        "title": "Example 1",
        "problem": "Perform two iterations of the bisection method to approximate the actual root of the non-linear equation f(x)=sinx-d (x is in radians) in the interval [0.5, 0.7].",
        "given": "",
        "method": "",
        "steps": [
          "The function values (a) and (b) are opposite in signs, so the actual root of f(x) lies in the interval [0.5, 0.7].",
          "i. The midpoint of the initial interval [a,b]is c,a,b,",
          "The function values f(a) and (c) are opposite in signs, so the approximation to the actual root of f(x) lies in the interval [0.5, 0.6] and discard b = 0.7. The initial interval is reset to obtain the first interval [a,b]=[0.5,0.6].",
          "The function values (b) and (c) are opposite in signs, so the approximation to actual root of f(x) lies in the interval [0.55,0.6] and discard a=0.5. The first interval is reset to obtain the second interval",
          "After second iteration of the bisection method, the midpoint =0.55 is declared approximate root to actual root. The approximation value of a function f(x)=sin.x-e\" at approximate root",
          "The next bracketing method is the method of regula-falsi method. It was developed because the bisection method converges at a fairly slow speed. As before, we assume that (a) and (b) have opposite signs. The bisection method always used the midpoint of the interval as the next iterate, but in regula-falsi method, the next iterate is anywhere in the interval [a, b] represented by the point of intersection (c, 0) of the straight line formed by the points (a,f(a)), and (b,f(b)) and the x-axis",
          "signs, then the root lies in the interval [a, c] and discard b.",
          "If the function values ƒ (c) and (b) at x=c and x = b",
          "If the function value at x=e is (c) = 0, then e is our approximate root. This is shown in the"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-12-2",
        "num": "2",
        "title": "Example 2",
        "problem": "Perform two iterations of the regula-falsi method to approximate the actual root r of the non-linear equation Remember - f(x)=sinx-e' (x is in radians) in the interval [0.5, 0.7].",
        "given": "",
        "method": "",
        "steps": [
          "Reset the given interval to obtain the initial equation f(x)-0 in the interval interval [a,b]=[0.5,0.7] and compute the function f(x)=sinx-e [a, b]. Proceed with the method",
          "only if f(x) is continuous and f(a) and (b) have opposite in",
          "The function values f(a) and (b) are opposite in signs, so the actual root r off(x) lies in the interval [0.5,0.7]. Equation (i) is used to obtain",
          "That provides the function value at c=0.592364:",
          "The function values (a) and (c) are opposite in signs, so the approximation to actual root of f(x) lies in the interval [0.5, 0.592364] and discard 4, -0.7. The initial interval is reset to obtain the first interval [4,,b]=[0.5,0.592364].",
          "that provides the function value at c=0.755: (0.755)=sin(0.755)-7-0.215 The function values at x=a=0.5, x=b=0.592364, c=0.755 are the following:",
          "The function values f(a) and (c) are opposite in signs, so the approximation to actual root of f(x) lies in the interval [0.5, 0.755] and discard b=0.592364. The first interval is reset to",
          "root F. The approximate value of a function f(x)=sinx-e\" at approximate root Fq=0.755 After second iteration of the regula-falsi, the point =0.755 is declared as approximation to actual",
          "Another numerical procedure is the Newton-Raphson method under the umbrella of iterative methods. The Newton-Raphson method is one-point iterative method which requires one previous approximation in contrast of bracketing methods which require two in computing the successive approximation.",
          "The Newton-Raphson method uses the slopes of the tangent lines to the graph of a function f(x)to approximate roots of the equation f(x) = 0.",
          "If ƒ(x) and ƒ'(x) are continuous near actual roots, then this extra information regarding the nature of f(x) can be used to develop a sequence of iterates {x} that will converge faster to actual root than either the bisection and regula-falsi methods.",
          "If is any actual root of an equation of the form f(x)=0, and x, is an initial approximation to the actual r, then the tangent line on a curve (x) at a point (.) crosses the x-axis at a point (x,.0). The point (1.0) is the point of intersection of the tangent line and the x-axis, and the x-coordinate of the point of intersection (1.0) is our first approximation to the actual root of an equation f(x)=0.This is shown in the Figure 12.3.",
          "The slope of the tangent line on a curve y = f(x) at a point (5.) is used to obtain the first",
          "Similarly, the slope of the tangent line on a curve y= f(x) at a point (x,,) is used to obtain the second",
          "This procedure of slope finding method is continued till it reaches the (i + 1)-th iterate:",
          "To find approximate root of an equation of the form f(x) = 0 with initial iterate x, the iteration method",
          "develops a sequence of successive iterates(x) that will converge faster to actual root r than either the bisection and"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-12-3",
        "num": "3",
        "title": "Example 3",
        "problem": "Use Newton-Raphson iterative method to approxime is actual root r 0.438447 of the non-linear equation f(x)=x-5x+2 with initial start x=0.4 that must be accurate to six decimal places.",
        "given": "",
        "method": "",
        "steps": [
          "The second iterate x, -0.438447 agrees to six decimal accuracy of actual root =0.438447.",
          "We achieved in just two iterates of the Newton-Raphson method the six decimal accuracy.",
          "MAPLE command \"fsolve\" to find numerical solution of an equation and demonstrate through examples",
          "The use of MAPLE command \"solve\" to find the approximate solution of given function is illustrated in the following example."
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-12-4",
        "num": "4",
        "title": "Example 4",
        "problem": "Use maple command \"solve\" to solve.",
        "given": "",
        "method": "",
        "steps": [
          "(b). Nonlinear equation x2-5x+6=0 with initial start x = 0.5.",
          "Solution The command below will show you full detail of the approximate root of linear and non- linear equations on line by typing without initial start:",
          "The quadratic function f (x) is also a second degree polynomial. The numerical solution through polynomial is:",
          "his result is obtained through right-click on the last end of the expression by selecting \"Solve Numerically Solve\" on the context menu.",
          "Find an interval asxsb at which (a) and (b) have opposite signs for the following",
          "Compute four iterates of the bisection method for the following functions with indicated",
          "Compute four iterates of the regula-falsi method for the following functions with indicated.",
          "What will happen if the bisection method is used with the function f(x)=x-2)",
          "Find iteratex, of Newton-Raphson iterative method for the following functions with initial start.x,",
          "Use Newton-Raphson iterative method to approximate the actual of the following non-linear equations with indicated interval:",
          "Continue the process until two consecutive iterates will agree to three decimal places. Use MAPLE command \"solve\" to solve 3x+4x-3-0 with initial start at x=0.5",
          "Qusta Ibn Luqa was a Syrian mathematician, astronomer and philosopher. He contribute",
          "many fields of science, medicine, astronomy. His translation on the difference between the spirit and the soul was one of the few works not attributed to Aristotle that was included in a list of books to be read or lectured on. He was the first person to write the double false position in 10 century. He justified the technique by a formal, Euclidean-style geometric proof, within the tradition of Muslim nathematics. Double false position was known as Hisab-al-Khata'ayn. It was used for centuries to solve practical problems such as commercial and recreational problems.",
          "the integral Numerical integration is a primary tool used by engineers and scientists to obtain approximate solutions for definite integrals that cannot be solved analytically. For example,",
          "has no actual solution. This means that there is no any integral formula that could be used directly to obtain the actual solution. The only way is to find out the approximate solution the: can be found by using some numerical procedures, such, as numerical integration.",
          "We now approach the subject of numerical integration. The goal is to approximate the definite integral of f(x)",
          "over the interval [a, b] by evaluating f(x) at a finite number of equally spaced grid points:",
          "is called a numerical integration or quadrature formula.",
          "The term E [f(x)] is called the truncation error for integration. The values quadrature nodes and {w, are called the weights.",
          "Depend on the given numerical procedure, the grid points (x,) are chosen in various ways. For trapezoidal rule and Simpson's rule, the grid points are chosen to be equally spaced. Before discussion of trapezoidal rule and Simpson's rule it must be familiar about approximation by rectangles and approximate area by rectangles.",
          "If ƒ(x)=0 is a function over the interval [a, b], then the definite integral (ii) represents the actual area under the graph of f(x) on the interval [a, b]. This is shown in the Figure 12.4.",
          "For approximate area, the function f(x) must be known at equally spaced grid points in the interval[a, b], each of width Ax=(b-a)/n:",
          "In light of above equally spaced grid points, the actual area (ii) under a curve f(x) over the interval [a, b] is rearranged as under:",
          "Consider the initial subinterval[1,4]. Let x, denote the right endpoint of the initial subinterval, and the base of the rectangle is of course the initial subinterval and its height is f(x). The area of the rectangle in the initial subinterval is therefore f(x)Ax.",
          "If f(x)dris the actual area in the initial subinterval, then the approximate area f(x)Axis of course the area of the rectangle lies in the initial subinterval [xx]. Thus, the sum of the areas of all rectangles is giving approximate area under the curve f(x) to actual area represented by definite integral (iv),",
          "This approximation improves as the number of rectangles increases, and we can estimate the integral to any desired degree of accuracy by taking a large enough. However, because fairly large values of a are usually required to achieve reasonable accuracy, approximation by rectangic is rarely used in practice.",
          "The accuracy of the approximation can be improved if trapezoids are used instead of rectangles. Figure 12.5 shows the area approximated by a trapezoids instead of n rectangles.",
          "If Ìƒ(x)dx is the actual area in the initial subinterval.",
          "approximate area [f(x)+(x)]Aris of course the",
          "area of the trapezoid lies in the initial subinterval [5.4]. Thus, the sum of the areas of all trapezoids is giving approximate",
          "area under the curve f(x) to actual area represented by definite integral (iv):",
          "In general, Iff(x) is continuous on [a, b], then the trapezoidal rule is"
        ],
        "answer": "",
        "diagram": null
      },
      {
        "id": "we-12-5",
        "num": "5",
        "title": "Example 5",
        "problem": "Approximate the definite integral I=xdx",
        "given": "",
        "method": "",
        "steps": [
          "The trapezoidal rule (vi) is used for Ax=0.75 and n = 4 to obtain:",
          "The function values foffaff at grid points x,,,,,,, are"
        ],
        "answer": "",
        "diagram": null
      }
    ],
    "exercises": [
      {
        "id": "ex-12-1",
        "exercise": "Exercise",
        "title": "Exercise",
        "description": "",
        "problems": [],
        "pageStart": 309,
        "pageEnd": 325
      },
      {
        "id": "ex-12-2",
        "exercise": "Review Exercise 12",
        "title": "Review Exercise 12",
        "description": "",
        "problems": [],
        "pageStart": 309,
        "pageEnd": 325
      },
      {
        "id": "ex-12-3",
        "exercise": "Exercise 12.1",
        "title": "Exercise 12.1",
        "description": "",
        "problems": [
          {
            "id": "ex-12-1-q1",
            "qNo": "1",
            "question": "Find an interval [a,b] on which f(a) and f(b) have opposite signs: (a) e^x−2−x; (b) cos x+1−x; (c) ln x−5+x; (d) x³−10x+23.",
            "solution": "Check endpoint values. (a) f(1)=e−3<0 and f(2)=e²−4>0, so [1,2] works. (b) f(0)=2>0 and f(2)=cos2−1<0, so [0,2] works. (c) f(3)=ln3−2<0 and f(4)=ln4−1>0, so [3,4] works. (d) f(−4)=−1<0 and f(−3)=26>0, so [−4,−3] works.",
            "diagram": null
          },
          {
            "id": "ex-12-1-q4",
            "qNo": "4",
            "question": "What happens if bisection is applied to f(x)=1/(x−2) on (a) [3,7] and (b) [1,7]?",
            "solution": "(a) f(3)>0 and f(7)>0, so the endpoint signs are not opposite and the bisection method cannot start. (b) The endpoint signs are opposite, but f is discontinuous at x=2 and has no zero. Bisection’s continuity requirement fails; repeated midpoints can approach the vertical asymptote rather than a root.",
            "diagram": null
          },
          {
            "id": "ex-12-1-q7",
            "qNo": "7",
            "question": "Use Maple’s fsolve command to solve 3x²+4x−3=0 with initial guess x₀=0.5.",
            "solution": "The quadratic formula gives x=(−2±√13)/3. The root near the initial guess 0.5 is x=(−2+√13)/3≈0.53518. Maple fsolve with x₀=0.5 converges to this root.",
            "diagram": null
          }
        ],
        "pageStart": 309,
        "pageEnd": 325
      },
      {
        "id": "ex-12-4",
        "exercise": "Exercise 12.2",
        "title": "Exercise 12.2",
        "description": "",
        "problems": [
          {
            "id": "ex-12-2-q1",
            "qNo": "1",
            "question": "Apply the trapezoidal rule with the stated n and compare with the exact integral: (a) ∫₁³ x² dx, n=4; (b) ∫₀²(x²/2+1)dx, n=4; (c) ∫₁³ dx/x, n=6; (d) ∫₀¹√(1+x²)dx, n=6.",
            "solution": "Use h=(b−a)/n and T=h[f(x₀)/2+f(x₁)+…+f(x_{n−1})+f(x_n)/2]. (a) T=8.75; exact=26/3≈8.6667. (b) T=3.375; exact=10/3≈3.3333. (c) T≈1.10675; exact=ln3≈1.09861. (d) T≈1.14943; exact=[x√(1+x²)+ln(x+√(1+x²))]₀¹/2≈1.14779.",
            "diagram": null
          },
          {
            "id": "ex-12-2-q2",
            "qNo": "2",
            "question": "Apply composite Simpson’s rule and compare with the exact integral: (a) ∫₂⁴x²dx, n=3; (b) ∫₂³(x²/3−1)dx, n=4; (c) ∫₁³dx/x, n=3; (d) ∫₀¹e^{2x}dx, n=4.",
            "solution": "Use Simpson’s 3/8 rule when n=3, and Simpson’s 1/3 rule when n=4. (a) S=56/3≈18.6667, exact for a quadratic. (b) S=10/9≈1.1111, exact for a quadratic. (c) S≈1.10476; exact=ln3≈1.09861. (d) S≈3.19561; exact=(e²−1)/2≈3.19453.",
            "diagram": null
          },
          {
            "id": "ex-12-2-q3",
            "qNo": "3",
            "question": "For y=√(1−x²), 0≤x≤1, use the trapezoidal rule with n=4 to approximate ∫₀¹√(1−x²)dx and compare with π/4 using π=3.1.",
            "solution": "With h=1/4, the ordinates at x=0,1/4,1/2,3/4,1 are 1, √15/4, √3/2, √7/4, 0. Thus T=(1/4)[1/2+√15/4+√3/2+√7/4]≈0.74893. The exact quarter-circle area using π=3.1 is π/4=0.775, so the trapezoidal estimate is about 0.02607 lower.",
            "diagram": {
              "type": "quarter-circle",
              "radius": 1,
              "rule": "trapezoidal",
              "n": 4,
              "title": "Quarter circle y=√(1−x²)"
            }
          },
          {
            "id": "ex-12-2-q4",
            "qNo": "4",
            "question": "Use Simpson’s rule with n=4 for the quarter-circle integral ∫₀¹√(1−x²)dx and compare with π/4 using π=3.1.",
            "solution": "Composite Simpson’s rule gives S=(h/3)[f₀+f₄+4(f₁+f₃)+2f₂], h=1/4. Substituting 1, √15/4, √3/2, √7/4, 0 gives S≈0.77090. The comparison value π/4=0.775, so the approximation is about 0.00410 lower.",
            "diagram": {
              "type": "quarter-circle",
              "radius": 1,
              "rule": "simpson",
              "n": 4,
              "title": "Quarter circle and Simpson estimate"
            }
          },
          {
            "id": "ex-12-2-q5",
            "qNo": "5",
            "question": "Use Maple commands to approximate the area over [0,2] by (a) the trapezoidal rule and (b) Simpson’s rule.",
            "solution": "Set the desired integrand f(x), interval [0,2], and number of subintervals n in Maple’s numerical-integration command, then request the trapezoidal and Simpson approximations. The printed question does not specify an integrand or n, so numerical values cannot be determined from this prompt alone.",
            "diagram": null
          }
        ],
        "pageStart": 309,
        "pageEnd": 325
      }
    ],
    "slos": {
      "mcqs": [],
      "shortQuestions": [],
      "longQuestions": []
    },
    "formulaSheet": []
  }
];
if (typeof DATA !== 'undefined' && DATA) { DATA.math12Units = MATH_12_DATA; }
if (typeof window !== 'undefined') { window.MATH_12_DATA = MATH_12_DATA; }