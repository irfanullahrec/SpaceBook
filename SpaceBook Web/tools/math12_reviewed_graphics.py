"""Printed pages 11–18, visually compared with JPGs and full PDF spreads 10–13."""
from math12_reviewed_unit1 import page, heading, paragraph, command, figure

def plot(number, title, definition):
    return {"type": "diagram", "id": f"math12-source-figure-1-{number}", "title": title, "caption": f"Figure 1.{number}", "diagram": {"title": f"Figure 1.{number}", **definition}}

def quadratic(number, a, b, c, restricted=False, colour='#111827'):
    return plot(number, f"Graph of x² + {b}x + {c}" if b else f"Graph of x² + {c}, −3 ≤ x ≤ 3", {
        "type": "quadratic-graph", "a": a, "b": b, "c": c,
        "xMin": -3 if restricted else -10, "xMax": 3 if restricted else 10,
        "yMin": 2 if restricted else 0, "yMax": 11 if restricted else 140,
        "axisY": 2 if restricted else 0,
        "xTicks": list(range(-3,4)) if restricted else [-10,-5,0,5,10],
        "yTicks": list(range(3,12)) if restricted else [20,40,60,80,100,120],
        "grid": False, "colour": colour, "yLabel": "", "xLabel": "x"
    })

PAGES = [
    page('010_page_1.jpg', 11, [
        heading('Example 3'), paragraph(r'Plot the graph of \(x^2+3x+8\).'), heading('Solution'),
        paragraph(r'The graph of \(x^2+3x+8\) is shown in the Figure 1.11 and 1.12 respectively.'),
        heading('(a) Command'), command(r'plot(\(x^2+3\cdot x+8\));'), quadratic(11,1,3,8),
        heading('(b) Context menu result'),
        paragraph('This result is obtained through right click on the last end of the expression by selection “plots< 2-D plot” on the context menu.'),
        command(r'\(x^2+3\cdot x+8\)'), command('smartplot(x^2+3*x+8);'), quadratic(12,1,3,8,colour='#075985'),
        heading('1.3.2 Domain and Range of a plot'),
        paragraph('To plot a two dimensional graph with domain and range. We use “plot” command in the command prompt.'),
        heading('Example 4'), paragraph(r'Plot the graph of \(x^2+2\) having domain −3 to 3.'), heading('Solution'),
        paragraph(r'The graph of \(x^2+2\) is shown in the Figure 1.13 and 1.14 respectively.'),
        heading('(a) Command'), command(r'plot(\(x^2+2\),x=-3..3);'), quadratic(13,1,0,2,True,colour='#075985'),
        heading('(b) Context menu result'),
        paragraph('Enter an expression or function, right click on it and select plots < plot builder < 2-D plot and enter the domain for the expression or function.'),
        command(r'\(x^2+2\),x=-3..3);'), command('plot(x^2+2,x=-3..3);'), quadratic(14,1,0,2,True,colour='#075985')
    ]),
    page('010_page_2.jpg', 12, [
        heading('1.3.3 Sketch parametric equation'),
        paragraph('To sketch the parametric equation in MAPLE. We use MAPLE “plot” as discussed in the following example.'),
        heading('Example 5'), paragraph(r'Sketch the graph of parametric equation \(x=\cos(t)\) and \(x=\sin(t)\).'),
        paragraph(r'Where \(-4\leq t\leq4\), x = −2 to 2 and y = −2 to 2'), heading('Solution'), heading('(a) Command'),
        command('plot([cos(t),sin(t),t=-4..4],-2..2,-2..2);'),
        plot(15, 'Parametric circle given by the printed cosine and sine coordinate pair', {"type":"unit-circle", "xMin":-2,"xMax":2,"yMin":-2,"yMax":2,"xTicks":[-2,-1,0,1,2],"yTicks":[-2,-1,1,2],"colour":"#075985"}),
        heading('(b) Context menu result'),
        paragraph('Enter an expression or function, right click on it and select plots < plot builder < 2-D parametric plot and domain for the parametric t.'),
        command('cos(t), sin(t)'), command('plot([cos(t),sin(t),t=-4..4]);'),
        figure('figure-1-16', 'Figure 1.16', 'Original partial-circle plot shown for the context-menu parametric example'),
        heading('1.3.4 Know plotting options'),
        paragraph('The plotting options listed below can provide the commands that create 2-D plots. These options can be used with the “plot” command and are generally available to all Maple commands that generate two dimensional plots. The help page of Maple for a particular command provides more detail about the plotting options that accepts.'),
        paragraph('Options must be added at the end of the given sequence.'),
        paragraph('We can use an interactive method of exploring the options in the “plot” command by using the Interactive Plot Builder.'),
        heading('Adaptive'), command('adaptive = n or true/false'),
        paragraph('When we are plotting a function over an interval. The interval is sampled at a number of points, controlled by “sample” and “numpoints”. Adaptive plotting, where necessary, subdivides these intervals to attempt to get a better representation of the function. This option is subsampling can be turned off by setting the “adaptive” option to false. By default, this option is true and intervals are subdivided at most six times in trying to improve the plot. By setting this option to a non-negative integer, we can control the maximum number of six times the subintervals are divided.'),
        heading('Annotation'), command('annotation = t'),
        paragraph('The annotation option allows us to add descriptive text to a 2-D curve or point plot. The term "point plot" in this context means a collection of points that are treated as a single plot element, such that')
    ]),
    page('011_page_1.jpg', 13, [
        {**paragraph('created by the “dataplot” command. The text which is included mathematical expressions, appears when the pointer hovers over the plot element to which it is associated. An annotation for a curve or a point, which appears whenever the pointer is placed over the element.'), "continuesPreviousParagraph": True},
        heading('Axes'), command('axes=f'), paragraph('Specifies the type of axes, one of: boxed, frame, none, or normal.'),
        heading('Axes font'), command('axesfont=l'),
        paragraph('Font for the labels on the tick marks of the axes, specified in the same manner as font. This option overrides values specified for the font.'),
        heading('Axis'), command('axis=t or axis[dir]=t'),
        paragraph('The axis and axis[dir] options allows us to provide information about one or more axes to plotting commands such as “plot” and “plot3d”. For example, the axis color, locations of tick marks and gridlines, and use of logarithmic scales.'),
        paragraph('With the axis = t option, the information provided in t is applied to all the axes. With the axis[dir] = t option, t is used for only the direction(s) specified in dir (direction), which can be the single value at (x-axis), (y-axis) or (z-axis), or a sequence of two of these values. Multiple axis[dir] options, with different values of dir, can be used to specify different information for different axes. The commands for 2-D plotting do not accept the axis[3] option.'),
        paragraph('The axis information is given by t. The list t may contain one or more of the sub options.'),
        heading('Axis coordinates'), command('axiscoordinates = t'),
        paragraph('Normally a coordinate system is used to display of the axes. The value t can be either cartesian of polar. Cartesian axes are displayed by default. If t is polar, then radial and angular axes are generated. This option is used together with the cords = polar option.'),
        heading('Note'), paragraph('This option is only available in the Standard interface. In the Classic interface, the coordinates are always Cartesian.'),
        heading('Background'), command('background = t'),
        paragraph('The value of t can be the name of an image file, as a string, a name, a datatype = float, Array as used with the Image Tools package, or a color. A plot can have a single background image or color.'),
        paragraph('If the size option is omitted then the dimensions of the plot can be determined by the dimensions of the image. If the size option is provided then the image is displayed with the dimensions of the plot.'),
        paragraph('A color may be given as a color tools [color] object or as a color string. If t is a string, then it is first interpreted as a filename. If the file t does not exist, it is then assumed to be a color.'),
        heading('Caption'), command('caption = c'),
        paragraph('The value c can be an arbitrary expression. It can also be a list consisting of the caption followed by the font option. The default is no caption.')
    ]),
    page('011_page_2.jpg', 14, [
        heading('Caption font'), command('captionfont = l'),
        paragraph('This option defines the font for the plot caption, specified in the same manner as font. This option over-rides values specified for font.'),
        heading('Color'), command('color = n or colour = n'), paragraph('This allows us to specify the color of the curves to be plotted.'),
        heading('Color scheme'), command('colorscheme = t or colourscheme = t'), paragraph('This allows us to apply a color scheme to a surface or set of points.'),
        heading('Coordinate view'), command('coordinateview = [r₁,...,r₂, a₁,...,a₂]'),
        paragraph('This option is used when the axes coordinates option has the value polar. When that is the case, then r₁,...,r₂, specifies the radial range that is to be displayed and a₁,...,a₂, specifies the angular range.'),
        heading('Cords'), command('cords = cname'),
        paragraph('The value cname is one of the choices listed on the coords help page. The cartesian axes are displayed by default. To generate polar axes with polar plots, we use axiscoordinates = polar option along with the coords = polar option.'),
        heading('Discount'), command('discount = t'), paragraph('This allows us for detection of discontinuities.'),
        heading('Filled'), command('filled = true/false or list'),
        paragraph('If the filled option is set to true, the area between the curve and the x-axis is given by a solid color. The value of the filled option can also be a list containing one or more sub options (color, style or transparency). These options are applied only to the filled area, and not to the original curve itself. This option does not work with non-cartesian coordinate systems.'),
        heading('Filled regions'), command('filledregions = true/false'),
        paragraph('If the filledregions option is set to true, the regions defined by the curves are filled with different colors. This option is valid only by using the following commands:'),
        paragraph('“contourplot”, “implicitplot” and “listcontplot”. This option does not work with non-Cartesian coordinate systems.'),
        heading('Font'), command('font = l'),
        paragraph('This option defines the font for the plot title, caption, axis tick mark labels, and axis labels if no values have been specified for these for font, captionfont, label font, or title font options. The value l is a list of the form [family, style, size].')
    ]),
    page('012_page_1.jpg', 15, [
        paragraph('The value of family can be one of Times, Courier, Helvetica, or Symbol. It can also be any font name supported by your system, for example, Times New Roman and Calibri in Windows. The first letter of the family name must be capitalized.'),
        paragraph('The value of style can be omitted or one of roman, bold, italic, bold italic, oblique, or bold oblique. The Symbol family does not accept a style option. The final value, size, is the point size to be used.'),
        heading('Gridline'), command('gridlines=true/false'),
        paragraph('When gridlines = true or gridlines is provided, default gridlines are drawn. The default is gridlines = false.If the axis option is also provided and contains a gridlines sub option, then that option over rides this gridlines option.'),
        heading('Labels'), command('labels = [x, y]'),
        paragraph('This option specifies labels for the axes. By default labels are the names of the variables in the original function to be plotted, if these are available otherwise, no labels will be used.'),
        heading('Label directions'), command('labeldirections = [x,y]'),
        paragraph('This option specifies the direction in which labels are printed along the axes. The values of x and y should be horizontal or vertical. The default direction of any labels is horizontal.'),
        heading('Label font'), command('labelfont = l'),
        paragraph('The font of the labels on the axes of the plot, specified in the same manner as font. This option overrides values specified for font.'),
        heading('Legend'), command('legend = s'),
        paragraph('If the plot command is being used to plot multiple curves, then s can be a list containing a legend entry for each curve.'),
        heading('Legend style'), command('legendstyle = s'),
        paragraph('Since the value s is a list consisting of one or more sub options. The sub options are available for the legendstyle option include font = f and location = loc. The location = loc sub option allows us top, bottom, right and left for loc.'),
        heading('Line style'), command('linestyle = t'),
        paragraph('It controls the line style of curves. The line style value t can be one of the following names: solid, dot, dash, dash dot, long dash, space dash, or space dot. The default value of t is solid. The value t can also be an integer from 1 to 7, where each integer represents a line style, as given in the order above.'),
        heading('Num points'), command('numpoints = n'), paragraph('Specifies the minimum number of points to be generated. The default number of points is 200.')
    ]),
    page('012_page_2.jpg', 16, [
        heading('Remember'), paragraph('Plot employs an adaptive plotting scheme which automatically does more work where the function values do not lie close to a straight line.'),
        heading('Resolution'), command('resolution = n'),
        paragraph('This sets the horizontal display resolution of the device in pixels. The default resolution is n=800.'),
        paragraph('The value of n is used to determine when the adaptive plotting scheme terminates.'),
        heading('Sample'), command('sample = [l]'),
        paragraph('A list of numerical values which is to be used for the initial sampling of the function. Normally, the function is sampled at additional points. To restrict sampling to only these values we include the adaptive = false option.'),
        heading('Scaling'), command('scaling = s'),
        paragraph('It controls scaling of the graph. The value of s is unconstrained by default, which means the plot is scaled to fit the plot window. The constrained value causes all axes to use the same scale.'),
        heading('Size'), command('size = [w, h]'),
        paragraph('We use this to specify the size of the plot window. We can set the size of the plot window by specifying the number of pixels, a proportion of worksheet width, or a ratio, such as a square, the golden ratio, or a custom ratio.'),
        heading('Smart view'), command('smartview = true/false'),
        paragraph('This is used to determine an appropriate view of the plot data. The plot command generates data based on the range provided by us or on a default range if this is not provided. When the smartview = true option is provided, a view that tries to present the important regions of the data is computed. To show all data computed, use the smartview = false option. The default setting of smartview is true. This option is available for the plot command and only applies to curves not points, polygons or text.'),
        heading('Style'), command('style=s'),
        paragraph('The plot style should be one of line, point, point line, polygon, or polygon outline. The names in parentheses are aliases for the option values. The styles line, polygon, and polygon outline all draw curves by interpolating between the sample points. The point style results in a plot of the points only. The default style, polygon outline, draws any polygons as filled with an outline. The polygon style shows the polygons with no outline, whereas line draws the polygons as outlines only. The point line style is a combination of the point and line styles.'),
        heading('Symbol'), command('symbol=s'),
        paragraph('Symbol for points in the plot, where the value s is one of asterisk, box, circle, cross, diagonalcross, diamond, point, solidbox, solidcircle, soliddiamond')
    ]),
    page('013_page_1.jpg', 17, [
        heading('Symbol size'), command('symbolsize = n'),
        paragraph('The size of a symbol used in plotting can be given by a natural number. This does not affect the symbol POINT. The symbolsize is 10 by default.'),
        heading('Thickness'), command('thickness = n'),
        paragraph('This option specifies the thickness of lines in the plot. The thickness = n must be a non-negative number. A value with 0 produces the thinnest line. By default the value is 1.'),
        heading('Tick marks'), command('Tickmarks = [m, n]'),
        paragraph('The values m and n specify the tick mark placement for the x-axis and y-axis respectively and can take an integer specifying the number of tick marks, a list of values specifying locations, a list of equations each having the form location = label, a name, or a spacing structure.'),
        heading('Title'), command('title=t'),
        paragraph('We can give a title to the plot. The value t can be an arbitrary expression. The value t can also be a list consisting of the title followed by the font option. There is no title by default for a plot.'),
        heading('Title font'), command('titlefont = l'), paragraph('It specified in the same manner as font. This option overrides values specified for font.'),
        heading('Transparency'), command('transparency = t'),
        paragraph('This option specifies the transparency of the plot surface. The transparency = t must evaluate to a floating-point number in the range [0, 1]. 0 means "not transparent" but 1 means "fully transparent."'),
        heading('Use units'), command('useunits = t'),
        paragraph('This option, with t set to true, indicates that units are part of the function and should be included in the axes labels. The value t can also be a list of units.'),
        heading('View'), command('view = [xmin...xmax, ymin...ymax]'),
        paragraph('View option indicates the minimum and maximum coordinates of the curve to be displayed on the screen. By default it is determined by the smartview option: if smartview = false is given, then all the plot data will be displayed; if smartview = true or the smartview option is not given, then the plot structure will be analyzed to determine a reasonable view of the data which allows you to see the significant features of the data.'),
        heading('Remember'), {"type":"list", "items":[
            'If the same option is provided more than once, with different values, then the final value specified is generally the one used.',
            'All above options are available for the Standard Worksheet interface.'
        ]}
    ]),
    page('013_page_2.jpg', 18, [
        heading('Example 6'), paragraph('Plot the graph of sec(x) and give the title as;'),
        command(r'title="Graph\n of Secant Function "'), command('titlefont = ["Times New Roman", 20]'), heading('Solution'),
        command(r'plot(sec(x), x=-2\pi..2\pi, title="Graph of Secant Function", titlefont=["Times New Roman",20]);'),
        plot(17, 'Graph of Secant Function', {"type":"secant-graph","yMin":-8,"yMax":8,"yTicks":[-8,-6,-4,-2,2,4,6,8],"colour":"#111827","asymptoteColour":"#9f1239","asymptoteDashed":False,"title":"Figure 1.17","plotTitle":'Graph of Secant Function"'}),
        paragraph('This example uses the following axes and graph properties:'),
        command(r'title="Graph\n of Secant Function"'), command('axes = framed'), command('style = point'), command('symbol = asterisk'), command('symbolsize = 20'), command('tickmarks = [spacing (Pi), default]')
    ])
]
for source in PAGES:
    source['visualStatus'] = 'Graphs recreated from equations and source scales; text rendered digitally'
PAGES[1]['visualStatus'] = 'Figure 1.15 digitally recreated; Figure 1.16 retained as a cropped original pending exact vector reconstruction'
PAGES[1]['sourceNotes'] = [
    'Example 5 prints x=cos(t) and x=sin(t); the intended second coordinate is y=sin(t). Original question preserved; explanation separately labelled.',
    'Figure 1.16 shows partial arcs rather than the full curve determined by the printed parameter interval; preserve the scan rather than invent endpoints.'
]
PAGES[5]['sourceNotes'] = ['The displayed syntax sample = [l] is preserved from the book. It is a list, not a nested matrix.']
PAGES[6]['alternateVerification'] = {'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':13,'side':'left','reason':'Full spread restores text at the cropped JPG right edge.'}
PAGES[7]['sourceNotes'] = ['The title option prints the literal escape sequence \\n. Preserve it without treating it as a newline in the transcription.']
FIGURE_PDF_CROPS = [(10, 'figure-1-16', (1237, 394, 1401, 544))]
