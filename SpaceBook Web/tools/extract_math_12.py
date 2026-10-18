"""Extract the real Class 12 Mathematics outline and build the SpaceBook data file.

The DOCX transcription is the source for prose and headings. Equation-heavy
paragraphs are intentionally omitted from theory until checked against scans;
the printed book page ranges are retained for scan cross-reference.
"""

from pathlib import Path
from docx import Document
import html
import json
import re

ROOT = Path(r"D:\SpaceBook\Books\12th\12th Maths")
OUT = Path(r"D:\SpaceBook\SpaceBook Web\js\math_12_data.js")
PARTS = sorted((ROOT / "Word").glob("001_page_1_and_356_more_part_*.docx"))
UNITS = [
    (1, "Introduction to Symbolic Package, Maple", 1, 24),
    (2, "Functions and Limits", 25, 62),
    (3, "Differentiation", 63, 100),
    (4, "Higher Order Derivatives and Applications", 101, 129),
    (5, "Differentiation of Vector Functions", 130, 141),
    (6, "Integration", 142, 177),
    (7, "Plane Analytic Geometry: Straight Line", 178, 212),
    (8, "Conics I", 213, 240),
    (9, "Conics II", 241, 285),
    (10, "Differential Equations", 286, 299),
    (11, "Partial Differentiation", 300, 308),
    (12, "Introduction to Numerical Methods", 309, 325),
]
LESSON_TITLES = {
    1: ["Introduction", "Polynomials", "Graphics", "Matrices"],
    2: ["Functions", "Composite Functions", "Inverse Functions", "Transcendental Functions", "Graphs of Functions", "Limits of Sequences", "Limits of Functions", "Continuous and Discontinuous Functions"],
    3: ["Derivative of a Function", "Theorems on Differentiation", "Applications of Differentiation Theorems", "Chain Rule", "Differentiation of Trigonometric and Inverse Trigonometric Functions", "Differentiation of Exponential and Logarithmic Functions", "Differentiation of Hyperbolic and Inverse Hyperbolic Functions"],
    4: ["Higher Order Derivatives", "Maclaurin's and Taylor's Expansions", "Applications of Derivatives", "Maxima and Minima"],
    5: ["Scalar and Vector Functions", "Limit and Continuity", "Differentiation of Vector Functions", "Vector Differentiation"],
    6: ["Antiderivatives", "Integration by Substitution", "Integration of Rational Functions", "Integration by Parts", "Integration Using Partial Fractions", "Definite Integrals"],
    7: ["Division of a Line Segment", "Slope of a Straight Line", "Equation of a Straight Line Parallel to the Coordinate Axes", "Standard Forms of the Equation of a Straight Line", "Distance of a Point from a Line", "Angle Between Lines", "Concurrency of Straight Lines", "Area of a Triangular Region", "Homogeneous Equations"],
    8: ["Conics and Members of Its Family", "Circle", "Tangents and Normal", "Properties of a Circle"],
    9: ["Parabola", "Ellipse", "Hyperbola", "Translation and Rotation of Axes"],
    10: ["Ordinary Differential Equations", "Formation of Differential Equations", "Solution of Differential Equations", "Orthogonal Trajectories"],
    11: ["Differentiation of Functions of Two Variables", "Euler's Theorem"],
    12: ["Numerical Solution of Non-linear Equations", "Numerical Quadrature"],
}
HEADING = re.compile(r"^\s*(\d{1,2})\.(\d{1,2})(?:\.(\d{1,2}))?\s*[.]?\s*(.*?)\s*$")
UNIT_MARK = re.compile(r"^\s*UNIT\s*[- ]?\s*(\d{1,2})\b", re.I)
EXAMPLE_MARK = re.compile(r"^\s*(?:Worked\s+)?Example(?:\s+(\d+(?:\.\d+)?))?\b\s*(.*)$", re.I)
EXERCISE_MARK = re.compile(r"^\s*(Review\s+Exercise|Exercise)(?:\s+([\d.]+))?\s*$", re.I)
JUNK = re.compile(r"^(?:NOT FOR SALE|UNIT\s*[- ]?\d+|\d{1,3}|[A-Z]\.?)$", re.I)


def clean(text):
    text = html.unescape(text or "")
    return re.sub(r"\s+", " ", text).strip()


def load_paragraphs():
    all_paras = []
    for path in PARTS:
        doc = Document(path)
        all_paras.extend((path.name, clean(p.text)) for p in doc.paragraphs if clean(p.text))
    return all_paras


def likely_prose(text):
    if len(text) < 45 or JUNK.fullmatch(text):
        return False
    if re.match(r"^(?:Figure|Example|Exercise|Review Exercise|Remember|History)\b", text, re.I):
        return False
    # A paragraph dominated by notation should be transcribed from its JPG.
    if sum(ch in "=√∫±≤≥<>^_{}[]" for ch in text) >= max(3, len(text) // 18):
        return False
    return bool(re.search(r"[A-Za-z]{3,}", text))


def chapter_one_text(text):
    """Keep all legible Unit 1 text, including formula and Maple command lines."""
    if len(text) < 3 or JUNK.fullmatch(text):
        return False
    if re.fullmatch(r"[\W\d_]+|[A-Za-z]{1,2}", text):
        return False
    if re.match(r"^(?:Figure\s+\d+\.\d+|INTRODUCTION TO SYMBOLIC PACKAGE|UNIT\s*[- ]?1)\b", text, re.I):
        return False
    return True


def unit1_slo_bank():
    rows = [
        ("Which three parts make up Maple software?", "User interface|Kernel|Library|All of these", 3, "Maple consists of the user interface, kernel, and library."),
        ("What does the Maple user interface handle?", "Input, output display, and worksheet control|Only file storage|Only graph colors|Only matrix determinants", 0, "The interface handles mathematical input, command input, output display, and worksheet control."),
        ("What is the Maple kernel described as?", "Compiled C code|A graph palette|A worksheet file|A matrix type", 0, "The kernel is a small collection of compiled C code that performs the core calculations."),
        ("What is found in the Maple library?", "Mathematical routines and packages|Only operating-system files|Only fonts|Only worksheet prompts", 0, "The library contains routines for algebra, statistics, calculus, graphics, and other topics."),
        ("Which symbols can terminate a Maple calculation command?", "Semicolon or colon|Comma only|Period only|Parentheses only", 0, "A Maple calculation statement is followed by a semicolon or a colon."),
        ("What happens when a command has no semicolon or colon?", "The next input continues the command|The worksheet closes|The value becomes zero|The command is saved automatically", 0, "Without a terminator, Maple treats the next command line as a continuation."),
        ("Which operator assigns a value to a Maple variable?", "=|:=|==|->", 1, "Maple uses the colon-equal assignment operator :=."),
        ("Which operation is performed first in Maple precedence?", "Addition|Division|Exponentiation|Subtraction", 2, "Exponentiation is performed before multiplication and division, then addition and subtraction."),
        ("Which command requests a floating-point evaluation?", "factor|evalf|subs|restart", 1, "evalf evaluates an expression using floating-point arithmetic."),
        ("What does exact arithmetic preserve?", "Fraction values exactly|Only rounded decimals|Only graph points|Only variable names", 0, "Maple keeps rational results exact unless a floating-point evaluation is requested."),
        ("Which command clears Maple's stored session values?", "expand|restart|factor|plot", 1, "The restart command returns Maple to its startup state and resets assigned values."),
        ("What file extension is named for the Save command in the book?", ".m|.jpg|.html|.csv", 0, "The book instructs the reader to retain the .m extension when saving a variable file."),
        ("Factor x^{2}+7x+12.", "(x+3)(x+4)|(x+6)(x+2)|(x-3)(x-4)|x(x+7)+12", 0, "The numbers 3 and 4 multiply to 12 and add to 7, so the factorization is (x+3)(x+4)."),
        ("Expand (x+2)(x+3).", "x^{2}+5x+6|x^{2}+6x+5|x^{2}+x+6|x^{2}+6", 0, "Multiply the terms: x²+3x+2x+6=x²+5x+6."),
        ("Evaluate 25^{1/2}+9/6-2/3 exactly.", "35/6|5|6|7/6", 0, "25^(1/2)=5, and 5+3/2-2/3=30/6+9/6-4/6=35/6."),
        ("Simplify (x^{2}-9)/(x^{2}+7x+12).", "(x-3)/(x+4), x≠-3,-4|(x+3)/(x+4), x≠-3,-4|(x-3)/(x+3)|1", 0, "Factor numerator and denominator: (x−3)(x+3)/[(x+3)(x+4)]. Cancel x+3, retaining x≠−3,−4."),
        ("For t=20, evaluate t^{2}-2t+5.", "365|345|405|3650", 0, "Substitute 20: 20²−2(20)+5=400−40+5=365."),
        ("Which Maple command plots a two-dimensional function?", "plot|factor|subs|inverse", 0, "The book uses the plot command for two-dimensional graphs."),
        ("In plot(f(x), x=a..b), what does a..b specify?", "The x-domain|The line color|The y-axis label|The graph title", 0, "The interval a..b specifies the domain over which the function is plotted."),
        ("Which syntax represents a parametric plot in Maple?", "[x(t),y(t),t=a..b]|x+y=t|matrix(x,y)|factor(x,y)", 0, "A parametric plot supplies the x and y functions and the parameter interval."),
        ("If x=cos(t) and y=sin(t), what equation does the curve satisfy?", "x^{2}+y^{2}=1|x+y=1|xy=1|x^{2}-y^{2}=1", 0, "Using cos²(t)+sin²(t)=1 gives x²+y²=1, the unit circle."),
        ("For y=sec(x), where are the vertical asymptotes?", "x=π/2+kπ|x=kπ|x=0 only|y=0", 0, "sec(x)=1/cos(x), so vertical asymptotes occur where cos(x)=0: x=π/2+kπ."),
        ("What is the default value of the adaptive plotting option?", "true|false|0|200", 0, "Adaptive plotting is true by default."),
        ("Which options control the initial sampling of a plotted function?", "sample and numpoints|caption and title|font and color|legend and labels", 0, "The text explains that sample and numpoints control the interval sampling."),
        ("Which is a valid axes option?", "boxed|triangle|matrix|fraction", 0, "The axes option can be boxed, framed, none, or normal."),
        ("What does the annotation option add to a plot?", "Descriptive text attached to a curve or point|A matrix inverse|A new domain|A decimal approximation", 0, "Annotation adds descriptive text to a two-dimensional curve or point plot."),
        ("What is the default setting for gridlines?", "false|true|800|π", 0, "The book states that gridlines are false by default."),
        ("What are default axis labels when variables are available?", "The names of the variables|The function's roots|The title text|The legend entries", 0, "By default, labels are the names of variables in the plotted function."),
        ("When is a legend useful?", "When plotting multiple curves|When clearing memory|When simplifying a fraction|When defining one variable", 0, "A legend can list an entry for each curve in a multiple-curve plot."),
        ("Which is one of the listed plot styles?", "point line|inverse|restart|colon-equal", 0, "The listed styles include line, point, point line, polygon, and polygon outline."),
        ("What is the default minimum number of plotted points?", "200|20|10|800", 0, "The numpoints option specifies the minimum number; its default is 200."),
        ("What range is allowed for plot transparency?", "[0,1]|[1,10]|(-∞,0)|[0,100]", 0, "Transparency is a floating-point value from 0 to 1, inclusive."),
        ("A matrix with 3 rows and 2 columns has what order?", "3×2|2×3|5×1|6×6", 0, "Matrix order is rows by columns, so the order is 3×2."),
        ("What is the result of [[1,2],[3,4]] + [[4,3],[2,1]]?", "[[5,5],[5,5]]|[[4,6],[6,4]]|[[5,6],[5,4]]|[[4,5],[6,5]]", 0, "Add corresponding entries: 1+4=5, 2+3=5, 3+2=5, and 4+1=5."),
        ("Find det([[1,2],[3,4]]).", "-2|2|10|-10", 0, "For a 2×2 matrix, the determinant is ad−bc=1·4−2·3=−2."),
    ]
    mcqs = []
    for i, (q, choices, correct, exp) in enumerate(rows, 1):
        item = {"q": q, "options": choices.split("|"), "correct": correct, "exp": exp}
        if i == 18:
            item["diagram"] = {"type":"quadratic-graph", "a":1, "b":0, "c":-4, "xMin":-4, "xMax":4, "yMin":-5, "yMax":12, "xLabel":"x", "yLabel":"y", "title":"Graph of y=x²−4"}
        elif i == 21:
            item["diagram"] = {"type":"unit-circle", "title":"Unit circle: x=cos(t), y=sin(t)"}
        elif i == 22:
            item["diagram"] = {"type":"secant-graph", "title":"Graph of y=sec(x)"}
        mcqs.append(item)

    long_data = [
        ("Explain the three parts of Maple software and the role of each.", "The user interface handles mathematical input, commands, output display, and worksheet control. The kernel is the compiled core that performs calculations and supplies arithmetic and memory facilities. The library contains routines and packages for areas such as linear algebra, statistics, calculus, and graphics."),
        ("Explain Maple command endings, assignment, precedence, and exact arithmetic.", "A calculation command ends with a semicolon or colon. Without either, the next line continues the same command. Use := to assign a value. Maple evaluates powers first, then multiplication and division, then addition and subtraction; parentheses change the order. Maple preserves exact fractions unless evalf is requested."),
        ("Factor x²+7x+12 and expand (x+2)(x+3), showing the main steps.", "For the factorization, find two numbers with product 12 and sum 7: 3 and 4. Thus x²+7x+12=(x+3)(x+4). For expansion, (x+2)(x+3)=x²+3x+2x+6=x²+5x+6."),
        ("Simplify (x²−9)/(x²+7x+12) and state the excluded values.", "Factor both parts: (x²−9)/(x²+7x+12)=[(x−3)(x+3)]/[(x+3)(x+4)]. Cancel x+3 to obtain (x−3)/(x+4). The original denominator is zero at x=−3 and x=−4, so both values remain excluded."),
        ("Use substitution to evaluate t²−2t+5 at t=20.", "Replace each t with 20: 20²−2(20)+5=400−40+5=365."),
        ("Sketch the graph of y=x²−4. Identify its intercepts and vertex.", "The graph is an upward-opening parabola. Set y=0: x²−4=0, so (x−2)(x+2)=0 and the x-intercepts are (−2,0) and (2,0). At x=0, y=−4, so the vertex is (0,−4).", {"type":"quadratic-graph","a":1,"b":0,"c":-4,"xMin":-4,"xMax":4,"yMin":-5,"yMax":12,"xLabel":"x","yLabel":"y","title":"Graph of y=x²−4","points":[{"x":-2,"y":0,"label":"(−2,0)"},{"x":2,"y":0,"label":"(2,0)"}]}),
        ("For y=x²+2 on −3≤x≤3, state the domain and range and describe the graph.", "The domain is [−3,3]. The parabola opens upward and has vertex (0,2), its minimum value. At x=−3 and x=3, y=11. Therefore the range is [2,11].", {"type":"quadratic-graph","a":1,"b":0,"c":2,"xMin":-3,"xMax":3,"yMin":0,"yMax":11,"xLabel":"x","yLabel":"y","title":"y=x²+2 on [−3,3]"}),
        ("Describe the parametric curve x=cos(t), y=sin(t), where −4≤t≤4.", "Squaring and adding gives x²+y²=cos²(t)+sin²(t)=1. The curve lies on the unit circle centered at the origin. The parameter interval covers more than one full revolution, so the circle is traced more than once.", {"type":"unit-circle","title":"Parametric unit circle"}),
        ("Describe the graph of y=sec(x) on −2π≤x≤2π.", "Since sec(x)=1/cos(x), the graph is undefined where cos(x)=0. In this interval the vertical asymptotes occur at x=−3π/2, −π/2, π/2, and 3π/2. The graph is even and has period 2π.", {"type":"secant-graph","title":"Graph of y=sec(x)"}),
        ("Explain adaptive, sample, and numpoints options for plotting.", "The interval is sampled at points controlled by sample and numpoints. Adaptive plotting subdivides intervals when needed to represent the function more accurately; it is true by default and may be disabled or limited by an integer. Sample supplies initial sample values. Numpoints gives the minimum number of points and defaults to 200."),
        ("Describe the axes, axis, axis-coordinates, and coords plotting options.", "Axes selects boxed, framed, none, or normal axes. Axis can set axis information globally or for a specified direction, including colors, ticks, grid lines, and logarithmic scales. Axis-coordinates chooses Cartesian or polar display; Cartesian is the default. Polar plots use axis-coordinates=polar together with coords=polar."),
        ("Explain how labels, legends, titles, and styles improve a plot.", "Labels name the axes and default to the variables in the function. Label directions control horizontal or vertical orientation. A legend provides entries for multiple curves and its style controls font and location. A title adds a heading and can use titlefont. Styles include line, point, point line, polygon, and polygon outline."),
        ("Describe the matrix palette procedure and matrix order.", "A matrix order is stated as rows×columns. In the palette, select matrix, choose the required row and column counts, choose the data type, and insert the matrix. Press ENTER to place the selected matrix into the worksheet."),
        ("For A=[[1,2],[3,4]], find Aᵀ and det(A). Then state how the inverse is obtained in Maple.", "Transpose by interchanging rows and columns: Aᵀ=[[1,3],[2,4]]. The determinant is 1·4−2·3=−2. Since the determinant is non-zero, A is invertible. In Maple, use the inverse command or choose Standard Operations, then inverse, from the context menu."),
    ]
    lqs = []
    for q, sol, *extra in long_data:
        item = {"q": q, "sol": sol, "marks": 8, "rubric": "Award marks for the correct method, mathematical working, and final result."}
        if extra: item["diagram"] = extra[0]
        lqs.append(item)

    short_data = [
        ("What are the three components of Maple?", "The user interface, kernel, and library."),
        ("What does the Maple kernel do?", "It supplies the compiled core and facilities needed to perform Maple calculations."),
        ("Which operator assigns a value to a variable?", "The colon-equal operator, :=."),
        ("What is the command terminator in Maple?", "A semicolon or a colon."),
        ("What is the purpose of evalf?", "It evaluates an expression using floating-point arithmetic."),
        ("Evaluate 3²+2×4.", "3²+2×4=9+8=17."),
        ("Factor x²−5x+6.", "x²−5x+6=(x−2)(x−3)."),
        ("Expand (x−1)(x+4).", "(x−1)(x+4)=x²+3x−4."),
        ("Simplify (x²−4)/(x−2), stating the restriction.", "(x²−4)/(x−2)=[(x−2)(x+2)]/(x−2)=x+2, with x≠2."),
        ("Find 2u²+u−1 when u=3.", "2(3²)+3−1=18+3−1=20."),
        ("Which command plots a two-dimensional graph?", "The plot command."),
        ("What does the domain of a plotted function describe?", "The allowed input values, usually the x-values over which the graph is drawn."),
        ("What is the vertex and minimum of y=x²−1?", "The vertex is (0,−1), and the minimum value is −1.", {"type":"quadratic-graph","a":1,"b":0,"c":-1,"xMin":-3,"xMax":3,"yMin":-2,"yMax":9,"xLabel":"x","yLabel":"y","title":"Graph of y=x²−1"}),
        ("What curve is represented by x=cos(t), y=sin(t)?", "The unit circle x²+y²=1.", {"type":"unit-circle","title":"x=cos(t), y=sin(t)"}),
        ("Where does sec(x) have a vertical asymptote?", "Where cos(x)=0, namely x=π/2+kπ for integer k.", {"type":"secant-graph","title":"Vertical asymptotes of sec(x)"}),
        ("What is the default value of adaptive plotting?", "True."),
        ("What is the default numpoints value stated in the book?", "200 points."),
        ("State the order of a matrix with 2 rows and 3 columns.", "Its order is 2×3."),
        ("Find the determinant of [[2,1],[5,3]].", "2·3−1·5=1."),
        ("What does transposing a matrix do?", "It changes rows into columns and columns into rows."),
    ]
    sqs = []
    for q, sol, *extra in short_data:
        item = {"q": q, "sol": sol, "marks": 3}
        if extra: item["diagram"] = extra[0]
        sqs.append(item)
    return {"mcqs": mcqs, "shortQuestions": sqs, "longQuestions": lqs}


def build(paragraphs):
    chapters = []
    for number, title, page_start, page_end in UNITS:
        found = {}
        unit_now = None
        unit_markers = [(i, int(match.group(1))) for i, (_, text) in enumerate(paragraphs)
                        if (match := UNIT_MARK.match(text)) and 1 <= int(match.group(1)) <= 12]
        unit_starts = [i for i, unit_no in unit_markers if unit_no == number]
        unit_start = unit_starts[0] if unit_starts else 0
        unit_end = next((i for i, unit_no in unit_markers if i > unit_start and unit_no != number), len(paragraphs))
        for i, (_, text) in enumerate(paragraphs[unit_start:unit_end], start=unit_start):
            unit_marker = UNIT_MARK.match(text)
            if unit_marker and 1 <= int(unit_marker.group(1)) <= 12:
                unit_now = int(unit_marker.group(1))
            match = HEADING.match(text)
            if not match or int(match.group(1)) != number or (unit_now not in (None, number)):
                continue
            heading_title = clean(match.group(4))
            if not heading_title:
                heading_title = next((clean(paragraphs[j][1]) for j in range(i + 1, min(i + 4, len(paragraphs)))
                                      if re.search(r"[A-Za-z]{3}", paragraphs[j][1])
                                      and not JUNK.fullmatch(paragraphs[j][1])
                                      and not HEADING.match(paragraphs[j][1])
                                      and not EXERCISE_MARK.match(paragraphs[j][1])
                                      and not EXAMPLE_MARK.match(paragraphs[j][1])), "")
            if number == 1 and not match.group(3):
                lesson_number = int(match.group(2))
                if not 1 <= lesson_number <= len(LESSON_TITLES[1]):
                    continue
                expected = LESSON_TITLES[1][lesson_number - 1].lower()
                if expected not in heading_title.lower():
                    continue
            if not re.search(r"[A-Za-z]{3}", heading_title) or len(heading_title) > 180:
                continue
            sid = f"{number}.{int(match.group(2))}" + (f".{int(match.group(3))}" if match.group(3) else "")
            # Keep the clean, numbered lesson heading, not OCR fragments.
            found.setdefault(sid, (i, f"{sid} {heading_title}"))

        ordered = sorted(found.items(), key=lambda item: item[1][0])
        extracted_sections = []
        for idx, (sid, (start, section_title)) in enumerate(ordered):
            next_start = ordered[idx + 1][1][0] if idx + 1 < len(ordered) else unit_end
            prose = []
            for _, para in paragraphs[start + 1:next_start]:
                include = chapter_one_text(para) if number == 1 else likely_prose(para)
                if include and para not in prose:
                    prose.append(para)
                if number != 1 and sum(map(len, prose)) >= 1800:
                    break
            extracted_sections.append((sid, "\n\n".join(prose)))

        # The app's Lesson tab is organized by the printed top-level lesson
        # numbers. Nested numbered headings are folded into their lesson body.
        sections = []
        for lesson_num, lesson_title in enumerate(LESSON_TITLES[number], 1):
            sid = f"{number}.{lesson_num}"
            body_parts, seen_parts = [], set()
            for source_id, text in extracted_sections:
                if not (source_id == sid or source_id.startswith(sid + ".")):
                    continue
                for part in text.split("\n\n"):
                    key = part.strip().casefold()
                    if key and key not in seen_parts:
                        seen_parts.add(key)
                        body_parts.append(part)
            body = "\n\n".join(body_parts)
            sections.append({
                "id": f"sec-{number}-{lesson_num}", "title": f"{sid} {lesson_title}",
                "theory": body, "rules": [], "keyPoints": [],
            })

        if number == 1:
            # Pages 1–4 were transcribed from the page scans and replace the
            # damaged DOCX OCR for the opening lesson. Numbered worked examples
            # remain in the separate Examples tab.
            sections[0]["theory"] = """By the end of this unit, the students will be able to:

1.1 Introduction
• Recognize the MAPLE environment.
• Recognize basic MAPLE commands.
• Use MAPLE as a calculator.
• Use online MAPLE help.

1.2 Polynomials
• Use MAPLE commands for factoring a polynomial, expanding an expression, simplifying a rational expression, simplifying an expression, and substituting into an expression.

1.3 Graphics
• Plot a two-dimensional graph and demonstrate the domain and range of a plot.
• Sketch parametric equations and know plotting options.

1.4 Matrices
• Recognize matrix and vector entry arrangement.
• Apply matrix operations.
• Compute the inverse and transpose of a matrix.

1.1 Introduction
In the modern age of science and technology, technical computation has become the heart of problem solving in engineering and mathematics. To help us, MAPLE offers a vast repository of mathematical algorithms, covering a wide range of applications. It is a symbolic and numeric computing tool as well as a multi-paradigm programming language conceived at the University of Waterloo in 1980. From the first day, it has continued to be benchmark software for mathematical and symbolic computation. The Maple user interface allows us to harness all the computational power by using context-sensitive menus, an interactive assistant, and task templates. In this unit, we will learn how to use the basic commands that will lead us into the creative, dynamic, and captivating world of MAPLE explorations.

1.1.1 Recognition of MAPLE Environment
Maple software consists of three different parts.

User interface
It handles the input of mathematical expressions and different commands. The user interface also handles the display of output and the control of the MAPLE worksheet environment.

Kernel
It is a small collection of compiled C code. The entire kernel is loaded when a MAPLE session is started. It contains the essential facilities required to run MAPLE and perform basic mathematical operations. The components of the kernel include the MAPLE programming-language interpreter, arithmetic and memory-management facilities, and fundamental functions. Its small size ensures that the MAPLE system is portable, compact, and efficient.

Library
It contains most of the MAPLE routines, including functions related to linear algebra, statistics, calculus, graphics, and other topics. This library also consists of individual routines and different packages of routines. All the library routines are implemented in the high-level MAPLE programming language and can be viewed and modified. Hence, it is useful to learn the MAPLE programming language so that we can modify existing code to produce the required routines.

A. Getting started with Maple
The Maple software runs on different systems and platforms. It depends on the platform and system. It is convenient to use if you have a Windows-based operating system (installed Maple software package 14, 18, or any latest package).

When a Maple session is started, the Maple prompt command (>) is displayed.

Figure 1.1 Maple start menu

This prompt character appears at the upper left of the worksheet and indicates that Maple is waiting to receive input in the form of a Maple statement. When you have finished with the Maple session, leave the program by selecting “Exit” under the “File” menu, as shown in Figure 1.2.

Figure 1.2 File menu and worksheet

1.1.2 Recognition of basic MAPLE commands
A MAPLE command is a statement of calculation followed by a semicolon or a colon. The following sections introduce commands and their displayed results.

Enter commands on your worksheet and verify the given results. To save your worksheet, select “Save” under the “File” menu or use Ctrl+S.

Remember
If you do not include a semicolon or colon at the end of a command, MAPLE interprets the next command line as a continuation of the previous command. The symbols +, −, *, /, and ^ denote addition, subtraction, multiplication, division, and exponentiation, respectively. When a string of operations is specified in a command, MAPLE performs exponentiation first, then multiplication and division, and then addition and subtraction. To change the order, use parentheses.

Save command
To save a variable in a file, type the Save command at the command prompt. Replace the variable name and file name with your own, but keep the .m extension. The Save command saves the variable as a MAPLE assignment statement. If the value of a variable depends on other variables, save those variables as well. You can save more than one variable by giving all the variable names in the Save command.

Editing commands
If you make a mistake in a command or want to change it, you can go back and edit the command.

Exact arithmetic and floating-point (evalf) commands
MAPLE calculates fractions using exact arithmetic unless you specify that you want decimals (floating-point arithmetic) with the evalf command. “evalf” stands for “evaluate using floating-point arithmetic.” The argument in the evalf command specifies the number of significant figures in the result. If you omit it, MAPLE returns its default number of significant figures.

Maple internal memory clearing command
To clear the internal memory during a Maple session, use the restart command or click the restart icon on the toolbar. When you enter this command, the Maple session returns to its startup state and all values are reset to their initial values.

Enlistment of variables
Use the colon-equal symbol (:=) to define variables and assign values to them. Once you have defined a variable, type its name to display its value. Using the variable name in a formula substitutes the assigned value.

1.1.3 Use of MAPLE as a calculator
You can obtain the MapleSoft(TM) Graphing Calculator Overview by selecting Start, then Programs, then Maple 18, and then Maple Calculator.

This graphical scientific calculator is available as part of your Maple(TM) installation or via a web server running MapleNet(TM). The calculator is used for Maple calculations.

On the toolbar:
• Use the Settings tab to control the basic computation settings for the calculator.
• Use the Math tab to select functions, from basic functions to linear algebra to statistics.
• Use the Graph tab to control how graphs are displayed and what they display.
• Use the Data tab to control the data used to produce a graph or data tabulated directly.
• Use the Variable tab to control the variables you have assigned and their values.

To use the graphical calculator, press the Math tab and select the functions to apply. This builds your expression in the input area, which is adjacent to the session history area on the left side of the calculator. When you are ready to evaluate the expression, press ENTER on your keyboard. Alternatively, press the Graph button to graph the expression, or the Data button to tabulate values for the expression.

1.1.4 Online MAPLE help
You can get help with MAPLE syntax by using the HELP menu, as described previously. If you have a question about a particular command, you can quickly get help by typing a question mark followed by the name of the command (without a semicolon).

This opens a window containing information about what the command does and how to use it. Click the small “Cross” box at the upper left of the window to close it."""

            sections[1]["theory"] = """1.2 Polynomials
We are familiar with polynomials from our previous grades. The factorization of a polynomial and the expansion of an expression can be performed through direct MAPLE commands and context menus.

1.2.1 Use of MAPLE commands for factoring a polynomial
Commands

Context menu result
You can use Maple’s context menus to perform a wide variety of mathematical and other operations. Enter the polynomial, place your cursor at the end of the expression, and right-click. The command window provides information about the factorization. Choose the Factor option from the open window, as shown in Figure 1.5. The context menu offers several operations to choose from according to the expression you are using.

1.2.2 Use of MAPLE commands for expanding an expression
Command
Use the MAPLE command “expand” before the parentheses to expand the given expression.

Context menu result
Enter the given expression, place your cursor at the end of it, and right-click. Then choose the expand option from the open window, as shown in Figure 1.6.

1.2.3 Use of MAPLE commands for simplifying an expression
Command
Use the simplify command to simplify an expression.

Context menu result
Enter the given expression, place your cursor at the end of it, and right-click. Then choose “simplify” from the open window, as shown in Figure 1.7.

1.2.4 Use of MAPLE commands for simplifying a rational expression
Command
Use the simplify command to simplify a rational expression.

Context menu result
Enter the given expression, place your cursor at the end of it, and right-click. Then select the “simplify” option, as shown in Figure 1.8.

1.2.5 Use of MAPLE commands for substituting an expression
Command
Use the subs command to substitute a value into an expression.

Context menu result
Enter the given expression, place your cursor at the end of it, and right-click. Then select the “evaluate at a point” option, as shown in Figures 1.9 and 1.10."""

            sections[2]["theory"] = """1.3 Graphics

1.3.1 Plot a two-dimensional graph
To plot any two-dimensional graph in MAPLE, use the “plot” command at the command prompt.

1.3.2 Domain and range of a plot
To plot a two-dimensional graph with a specified domain and range, use the “plot” command at the command prompt.

1.3.3 Sketch parametric equations
To sketch parametric equations in MAPLE, use the “plot” command. The graph is plotted over the specified parameter interval and viewing ranges.

1.3.4 Know plotting options
The plotting options listed below can provide commands that create two-dimensional plots. These options can be used with the “plot” command and are generally available to all MAPLE commands that generate two-dimensional plots. The help page for a particular MAPLE command provides more detail about the options it accepts. Options must be added at the end of the given sequence. You can explore the options in the “plot” command interactively by using the Interactive Plot Builder.

Adaptive
adaptive = true, false, or a non-negative integer
When plotting a function over an interval, the interval is sampled at a number of points controlled by “sample” and “numpoints”. Adaptive plotting subdivides intervals, where necessary, to obtain a better representation of the function. This subsampling can be turned off by setting “adaptive” to false. By default it is true, and intervals are subdivided at most six times to improve the plot. Setting this option to a non-negative integer controls the maximum number of subdivisions.

Annotation
The annotation option adds descriptive text to a two-dimensional curve or point plot. A point plot is a collection of points treated as a single plot element. Mathematical text appears when the pointer hovers over the associated curve or point.

Axes
Specifies the type of axes: boxed, framed, none, or normal.

Axes font
Specifies the font for labels on the axes’ tick marks. It is specified in the same manner as the font option and overrides values specified for font.

Axis
The axis and axis[dir] options provide information about one or more axes for plotting commands such as “plot” and “plot3d”. This information can include axis color, tick-mark and grid-line locations, and logarithmic scales. With axis = t, the information is applied to all axes. With axis[dir] = t, it is applied only to the specified direction: x-axis, y-axis, or z-axis, or a sequence of two directions. Multiple axis[dir] options with different values can be used for different axes. Two-dimensional plotting commands do not accept the axis[3] option. The axis information is given by t, which may contain one or more sub-options.

Axis coordinates
Normally, a coordinate system is used to display the axes. Cartesian axes are displayed by default. If the coordinate system is polar, radial and angular axes are generated. This option is used together with the coords = polar option.

Background
The background option sets a single background image or color for a plot. Its value can be an image file name, a string, a name, a datatype = float, an Array used with the Image Tools package, or a color. If size is omitted, the dimensions of the plot can be determined by the image. If size is provided, the image is displayed with the dimensions of the plot. A color may be given as a color-tools object or a color string. A string is first interpreted as a file name; if the file does not exist, it is assumed to be a color.

Caption
The caption value can be an arbitrary expression or a list consisting of the caption followed by the font option. By default, there is no caption.

Caption font
Defines the font for the plot caption in the same manner as the font option. It overrides values specified for font.

Color
Specifies the color of the curves to be plotted.

Color scheme
Applies a color scheme to a surface or set of points.

Coordinate view
This option is used when the axis-coordinates option has the value polar. It specifies the radial range to display and the angular range to display.

Coords
The value is one of the choices listed on the coords help page. Cartesian axes are displayed by default. To generate polar plots, use the axis-coordinates = polar option together with the coords = polar option.

Discont
Allows detection of discontinuities.

Filled
If the filled option is true, the area between the curve and the x-axis is shown in a solid color. Its value can also be a list containing sub-options such as color, style, or transparency. These options apply to the filled area, not the original curve. This option does not work with non-Cartesian coordinate systems.

Filled regions
If the filledregions option is true, regions defined by curves are filled with different colors. This option is available only for the “contourplot”, “implicitplot”, and “listcontplot” commands. It does not work with non-Cartesian coordinate systems.

Font
Defines the font for the plot title, caption, axis tick-mark labels, and axis labels when no font has been specified for the axes, caption, label, or title options. The value is a list of the form [family, style, size]. The family may be Times, Courier, Helvetica, or Symbol, or any font supported by the system, such as Times New Roman or Calibri in Windows. The first letter of the family name must be capitalized. The style may be roman, bold, italic, bold italic, oblique, bold oblique, or omitted. The Symbol family does not accept a style option. The final value is the point size.

Gridline
By default, grid lines are drawn when gridlines = true or gridlines is provided. The default is gridlines = false. If the axis option is also provided and contains a gridlines sub-option, that option overrides this one.

Labels
Specifies labels for the axes. By default, the labels are the names of the variables in the original function to be plotted; if these are unavailable, no labels are used.

Label directions
Specifies the direction in which labels are printed along the axes. The x- and y-axis labels can be horizontal or vertical. The default direction is horizontal.

Label font
Specifies the font for labels on the plot axes in the same manner as the font option. It overrides values specified for font.

Legend
If the plot command is used to plot multiple curves, the legend value can be a list containing a legend entry for each curve.

Legend style
The value is a list of one or more sub-options. The legendstyle option includes font and location. The location sub-option allows the legend to be placed at the top, bottom, right, or left.

Line style
Controls the line style of curves. The available styles are solid, dot, dash, dash dot, long dash, space dash, or space dot. The default is solid. The value can also be an integer from 1 to 7, with each integer representing a line style as shown in the book.

Number of points
Specifies the minimum number of points to be generated. The default is 200.

Resolution
Sets the horizontal display resolution of the device in pixels. The default resolution is 800. The value determines when the adaptive plotting scheme terminates.

Sample
A list of numerical values used for the initial sampling of the function. Normally, the function is sampled at additional points. To restrict sampling to only the listed values, include the adaptive = false option.

Scaling
Controls the scaling of the graph. By default, the plot is scaled to fit the plot window. The constrained value causes all axes to use the same scale.

Size
Specifies the size of the plot window. It can be set by specifying the number of pixels, a proportion of worksheet width, or a ratio such as a square, the golden ratio, or a custom ratio.

Smart view
Determines an appropriate view of the plot data. The plot command generates data based on the range provided or on a default range if none is provided. With smartview = true, a view is computed that tries to present the important regions of the data. To show all computed data, use smartview = false. The default is true. This option is available for the plot command and applies only to curves, not points, polygons, or text.

Style
The plot style can be line, point, point line, polygon, or polygon outline. The names in parentheses are aliases for the option values. The line, polygon, and polygon-outline styles draw curves by interpolating between sample points. The point style plots only the points. The default, polygon outline, draws polygons filled with an outline. Polygon style shows polygons without an outline, while line style draws polygon outlines only. Point line combines point and line styles.

Symbol
Specifies the symbol used for points. Choices include asterisk, box, circle, cross, diagonal cross, diamond, point, solid box, solid circle, or solid diamond.

Symbol size
Specifies the size of a plotting symbol as a natural number. This does not affect the point symbol. The default symbol size is 10.

Thickness
Specifies the thickness of lines in the plot. The value must be a non-negative number. A value of 0 produces the thinnest line. The default is 1.

Tick marks
The values m and n specify tick-mark placement on the x- and y-axes, respectively. They can be an integer specifying the number of tick marks, a list of locations, a list of equations of the form location = label, a name, or a spacing structure.

Title
A title can be given to the plot. Its value can be an arbitrary expression or a list consisting of the title followed by the font option. By default, a plot has no title.

Title font
Specified in the same manner as the font option. It overrides values specified for font.

Transparency
Specifies the transparency of the plot surface. The value must be a floating-point number in the range [0, 1]. A value of 0 means “not transparent”; a value of 1 means “fully transparent.”

Use units
When set to true, this option indicates that units are part of the function and should be included in axis labels. Its value can also be a list of units.

View
Specifies the minimum and maximum coordinates of the curve to be displayed. By default, it is determined by the smartview option. If smartview = false is given, all plot data is displayed. If smartview = true, or the option is omitted, the data is analyzed to determine a reasonable view that shows its significant features.

Remember
If the same option is provided more than once with different values, the final value specified is generally the one used. All the above options are available for the Standard Worksheet interface."""

            sections[3]["theory"] = """1.4 Matrices
The command displays full information about matrices when you type ?matrices at the command line.

1.4.1 Recognition of matrix and vector entry arrangement
Using palettes
Use the cursor button to select the matrix palette. Click “matrix”, choose the required number of rows and columns, and click the data type to select the entries. Finally, click “insert matrix” and press ENTER to obtain the required matrix.

1.4.2 Applying matrix operations
Matrix addition
Matrix multiplication
Using palettes
To obtain the result, right-click the last matrix, then click “simplify” or press ENTER.

1.4.3 Inverse and transpose of a matrix
Inverse of a matrix
Using palettes
To obtain the result through the context menu, right-click the last matrix, select “Standard Operations”, and then click “inverse” to obtain the inverse of a matrix.

Transpose of a matrix
To obtain the result through the context menu, right-click the last matrix, select “Standard Operations”, and then click “transpose” to obtain the transpose of a matrix.

Determinant of a matrix
To obtain the result through the context menu, right-click the last matrix, select “Standard Operations”, and then click “determinant” to obtain its determinant."""

        examples, exercises = [], []
        active_unit = None
        unit_lines = []
        for _, para in paragraphs:
            um = UNIT_MARK.match(para)
            if um and 1 <= int(um.group(1)) <= 12:
                active_unit = int(um.group(1))
            if active_unit == number:
                unit_lines.append(para)
        # Keep real numbered example headings and source excerpts. The source
        # transcription is not promoted to a worked solution when notation is garbled.
        example_matches = []
        for pos, para in enumerate(unit_lines):
            em = EXAMPLE_MARK.match(para)
            if em:
                label = em.group(1) or str(len(example_matches) + 1)
                example_matches.append((pos, label, clean(em.group(2))))
        for idx, (pos, label, title_tail) in enumerate(example_matches):
            stop = example_matches[idx + 1][0] if idx + 1 < len(example_matches) else min(len(unit_lines), pos + 12)
            source = [line for line in unit_lines[pos + 1:stop] if likely_prose(line)]
            examples.append({
                "id": f"we-{number}-{idx + 1}", "num": label,
                "title": f"Example {label}",
                "problem": title_tail or (source[0] if source else ""),
                "given": "", "method": "", "steps": source[1:], "answer": "",
                "diagram": None,
            })

        if number == 1:
            # These six numbered examples have been checked directly against
            # the corresponding printed pages (pp. 4–14), including the Maple
            # command results and the graphs shown in the scans.
            examples = [
                {"id":"we-1-1","num":"1","title":"Example 1",
                 "problem":"Differentiate \\(f(x)=x^{2}+4x+4\\) with respect to \\(x\\) at the point \\(x=2\\).",
                 "given":"f(x)=x^{2}+4x+4, x=2","method":"Maple differentiation at a point",
                 "steps":["Set A=x^{2}+4x+4, X=x, and P=2.","Enter Diff(A,X,P).","Substitute the values: Diff(x^{2}+4x+4,x,2)=8."],
                 "answer":"8","diagram":None},
                {"id":"we-1-2","num":"2","title":"Example 2",
                 "problem":"Integrate \\(x^{2}+4x+4\\) with respect to \\(x\\) over the interval \\([0,1]\\).",
                 "given":"f(x)=x^{2}+4x+4, lower limit 0, upper limit 1","method":"Maple definite integration",
                 "steps":["Set A=x^{2}+4x+4, X=x, P=0, and Q=1.","Enter Int(A,X,P,Q).","\\int_{0}^{1}(x^{2}+4x+4)\\,dx=[\\frac{x^{3}}{3}+2x^{2}+4x]_{0}^{1}=\\frac{19}{3}\\approx6.333333."],
                 "answer":"6.333333","diagram":None},
                {"id":"we-1-3","num":"3","title":"Example 3",
                 "problem":"Plot the graph of \\(y=x^{2}+3x+8\\).","given":"y=x^{2}+3x+8","method":"Plot the quadratic function in Maple",
                 "steps":["Enter plot(x^{2}+3x+8).","The graph is an upward-opening parabola with vertex \\((-\\frac{3}{2},\\frac{23}{4})\\)."],
                 "answer":"The graph is the parabola \\(y=x^{2}+3x+8\\).","diagram":{"type":"quadratic-graph","a":1,"b":3,"c":8,"xMin":-10,"xMax":10,"yMin":0,"yMax":130,"xLabel":"x","yLabel":"y","title":"Graph of y=x²+3x+8"}},
                {"id":"we-1-4","num":"4","title":"Example 4",
                 "problem":"Plot the graph of \\(y=x^{2}+2\\) for \\(-3\\leq x\\leq3\\).","given":"y=x^{2}+2, -3≤x≤3","method":"Plot the function over the specified domain",
                 "steps":["Enter plot(x^{2}+2,x=-3..3).","The vertex is (0,2), and the graph is symmetric about the y-axis."],
                 "answer":"The graph is the portion of \\(y=x^{2}+2\\) on \\([-3,3]\\), with range \\([2,11]\\).","diagram":{"type":"quadratic-graph","a":1,"b":0,"c":2,"xMin":-3,"xMax":3,"yMin":0,"yMax":11,"xLabel":"x","yLabel":"y","title":"Graph of y=x²+2 on [-3,3]"}},
                {"id":"we-1-5","num":"5","title":"Example 5",
                 "problem":"Sketch the graph of the parametric equations x = cos(t) and y = sin(t), where −4 ≤ t ≤ 4, with −2 ≤ x,y ≤ 2.","given":"x = cos(t), y = sin(t), −4 ≤ t ≤ 4","method":"Plot the parametric curve",
                 "steps":["Use the parameter t in the interval [-4,4].","Since x²+y²=cos²(t)+sin²(t)=1, the curve is the unit circle."],
                 "answer":"A unit circle centered at the origin.","diagram":{"type":"unit-circle","title":"Parametric curve x=cos(t), y=sin(t)"}},
                {"id":"we-1-6","num":"6","title":"Example 6",
                 "problem":"Plot the graph of sec(x) for −2π ≤ x ≤ 2π, and give it the title “Graph of Secant Function”.","given":"y = sec(x), −2π ≤ x ≤ 2π","method":"Plot the secant function with the stated Maple options",
                 "steps":["Set the graph title to “Graph of Secant Function” and use Times New Roman, 20 pt.","The printed example also uses framed axes, point style, asterisk symbols of size 20, and tick marks spaced by π."],
                 "answer":"The graph has vertical asymptotes where cos(x)=0.","diagram":{"type":"secant-graph","title":"Graph of Secant Function"}},
            ]

        # Actual exercise headings are included even when the Word source does
        # not preserve enough equation/answer material to create a trustworthy solution.
        exercise_matches = []
        for pos, para in enumerate(unit_lines):
            xm = EXERCISE_MARK.match(para)
            if xm:
                label = clean(xm.group(2))
                if not label and pos + 1 < len(unit_lines) and re.fullmatch(r"\d+(?:\.\d+)*", unit_lines[pos + 1]):
                    label = unit_lines[pos + 1]
                name = ("Review Exercise" if xm.group(1).lower().startswith("review") else "Exercise")
                exercise_matches.append((pos, f"{name} {label}".strip()))
        for idx, (pos, label) in enumerate(exercise_matches):
            if any(ex["title"] == label for ex in exercises):
                continue
            exercises.append({"id": f"ex-{number}-{len(exercises) + 1}",
                              "exercise": label, "title": label, "description": "",
                              "problems": [], "pageStart": page_start, "pageEnd": page_end})

        chapters.append({
            "id": f"unit-{number}", "number": number, "title": title,
            "titleUrdu": "", "pageRange": f"Printed pages {page_start}–{page_end}",
            "pageStart": page_start, "pageEnd": page_end,
            "sections": sections,
            "workedExamples": examples, "exercises": exercises,
            "slos": unit1_slo_bank() if number == 1 else {"mcqs": [], "shortQuestions": [], "longQuestions": []},
            "formulaSheet": [],
        })
    return chapters


def main():
    if not PARTS:
        raise SystemExit(f"No Word source files found in {ROOT / 'Word'}")
    paragraphs = load_paragraphs()
    chapters = build(paragraphs)
    if "--outline" in __import__("sys").argv:
        print(json.dumps([{
            "number": chapter["number"],
            "title": chapter["title"],
            "lessons": [section["title"] for section in chapter["sections"]],
        } for chapter in chapters], ensure_ascii=False, indent=2))
        return
    js = "// Class 12 Mathematics — source-derived KPTBB unit and lesson data.\n"
    js += "const MATH_12_DATA = " + json.dumps(chapters, ensure_ascii=False, indent=2) + ";\n"
    js += "if (typeof DATA !== 'undefined' && DATA) { DATA.math12Units = MATH_12_DATA; }\n"
    js += "if (typeof window !== 'undefined') { window.MATH_12_DATA = MATH_12_DATA; }"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(js, encoding="utf-8")
    print(f"Wrote {len(chapters)} units to {OUT}")


if __name__ == "__main__":
    main()
