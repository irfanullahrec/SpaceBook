# -*- coding: utf-8 -*-
"""
SpaceBook - Units 8, 9, 10, 11 Data Builder for Class 8 Mathematics
"""

def get_unit_8():
    return {
        "number": 8,
        "id": "unit-8",
        "title": "Simultaneous Linear Equations",
        "titleUrdu": "ہمزاد لکیری مساواتیں",
        "type": "chapter",
        "pageRange": "pp. 163–207",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 8 develops methods for solving systems of simultaneous linear equations in two variables. It details the Elimination Method (by equating coefficients), the Substitution Method, and Graphical solution representations. It thoroughly explores linear inequalities in one variable (solving algebraically and plotting on the real number line, including flipping inequality symbols when multiplying/dividing by negatives), accompanied by practical word problems.",
        "urduSummary": "یونٹ 8 دو متغیرات پر مشتمل ہمزاد لکیری مساواتوں (Simultaneous Linear Equations) کے نظام کو حل کرنے کے طریقوں کی وضاحت کرتا ہے۔ اس میں طریقہ اخراج (Elimination Method)، طریقہ استبدال (Substitution Method)، اور ترسیمی طریقہ (Graphical Method) شامل ہیں۔ علاوہ ازیں، یک متغیری لکیری غیر مساواتوں (Inequalities) کے حل، عددی خط پر ان کی نمائندگی، اور حقیقی زندگی کے روزمرہ سوالات حل کیے گئے ہیں۔",
        "sections": [
            {
                "id": "8.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Solve simultaneous linear equations using Elimination and Substitution methods.\n• Solve linear inequalities in one variable and plot solution sets on a number line.\n• Formulate and solve real-life word problems using simultaneous linear equations.",
                "theory": "Core Competencies:\n1. Solve a₁x + b₁y = c₁ and a₂x + b₂y = c₂ simultaneously.\n2. Inequality rule: Multiplying or dividing both sides of an inequality by a negative number reverses the direction of the inequality sign (< becomes >, > becomes <).\n3. Translate verbal statements into linear equations and interpret solutions.",
                "paras": [
                    "Solve systems of simultaneous linear equations by algebraic methods.",
                    "Solve and graph linear inequalities on the real number line.",
                    "Formulate mathematical models from word problems and find unique solutions."
                ]
            },
            {
                "id": "8.1-simultaneous-methods",
                "title": "8.1 Methods of Solving Simultaneous Equations",
                "heading": "Methods of Solving Simultaneous Equations",
                "headingUrdu": "ہمزاد مساواتوں کو حل کرنے کے طریقے",
                "text": "1. Elimination Method: Multiply equations by constants so that coefficients of one variable become equal, then add or subtract to eliminate that variable.\n2. Substitution Method: Express one variable in terms of the other from one equation and substitute into the other equation.\n3. Graphical Method: Graph both straight lines; the coordinates (x, y) of the point of intersection represent the common solution.",
                "theory": "Algorithm for Elimination:\n1. Choose variable to eliminate (e.g. y).\n2. Multiply Eq(1) and Eq(2) so that coefficients of y are numerically equal.\n3. If coefficients have opposite signs, ADD equations. If same sign, SUBTRACT.\n4. Solve the resulting single-variable equation for x, then substitute x back to find y.",
                "paras": [
                    "Elimination equates coefficients to isolate a single variable.",
                    "Substitution expresses one variable in terms of the other.",
                    "The point of intersection of two linear graphs gives the simultaneous solution."
                ]
            },
            {
                "id": "8.2-linear-inequalities",
                "title": "8.2 Linear Inequalities in One Variable",
                "heading": "Linear Inequalities in One Variable",
                "headingUrdu": "یک متغیری لکیری غیر مساواتیں",
                "text": "An inequality contains symbols <, >, ≤, or ≥.\nKey Rule: When you multiply or divide both sides of an inequality by a negative number, the inequality sign MUST reverse direction.\nExample: -2x < 6 → x > 6 / (-2) → x > -3.",
                "theory": "Inequality Properties:\n• If a < b then a + c < b + c\n• If a < b and c > 0 then ac < bc\n• If a < b and c < 0 then ac > bc (reversal)\nOn a number line, strict inequality (< or >) uses an open circle ○; non-strict (≤ or ≥) uses a solid closed dot ●.",
                "paras": [
                    "Inequalities describe ranges of numerical values.",
                    "Multiplying or dividing by a negative number reverses the inequality direction.",
                    "Solutions are depicted graphically on a continuous number line."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-8-1",
                "title": "Example 1: Elimination Method",
                "problem": "Solve simultaneously:\n2x + 3y = 13  ...(1)\n3x - y = 3     ...(2)",
                "solution": "Multiply Eq(2) by 3:\n9x - 3y = 9   ...(3)\nAdd Eq(1) and Eq(3):\n(2x + 3y) + (9x - 3y) = 13 + 9\n11x = 22 → x = 2.\nSubstitute x = 2 into Eq(2):\n3(2) - y = 3 → 6 - y = 3 → y = 3.\nSolution set = {(2, 3)}."
            },
            {
                "id": "we-8-8-2",
                "title": "Example 2: Solving an Inequality",
                "problem": "Solve and graph on number line: 3(x - 2) ≤ 5x + 4.",
                "solution": "3x - 6 ≤ 5x + 4\n3x - 5x ≤ 4 + 6\n-2x ≤ 10\nDivide by -2 (reverse sign):\nx ≥ 10 / (-2)\nx ≥ -5.\nSolution: All real numbers x such that x ≥ -5 (solid dot on -5 extending rightwards)."
            }
        ],
        "exercises": [
            {
                "exercise": "8.3",
                "title": "Exercise 8.3: Elimination Method",
                "answerKeyText": "Exercise 8.3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Solve by elimination:\n(a) x + y = 7, x - y = 3\n(b) 2x + y = 10, x + 2y = 8",
                        "solution": "(a) Adding: 2x = 10 → x = 5. Then y = 7 - 5 = 2. Solution: (5, 2).\n(b) Multiply second by 2: 2x + 4y = 16. Subtract first: 3y = 6 → y = 2. Then x = 8 - 2(2) = 4. Solution: (4, 2)."
                    }
                ]
            },
            {
                "exercise": "8.5",
                "title": "Exercise 8.5: Substitution Method",
                "answerKeyText": "Exercise 8.5 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Solve by substitution: y = 2x - 1 and 3x + y = 9.",
                        "solution": "Substitute y = 2x - 1 into 3x + y = 9:\n3x + (2x - 1) = 9\n5x - 1 = 9 → 5x = 10 → x = 2.\nThen y = 2(2) - 1 = 3. Solution: (2, 3)."
                    }
                ]
            },
            {
                "exercise": "8.7",
                "title": "Exercise 8.7: Linear Inequalities",
                "answerKeyText": "Exercise 8.7 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Solve the inequalities:\n(a) 2x + 5 < 11\n(b) 4 - 3x ≥ 16\n(c) 5x - 2 > 3x + 6",
                        "solution": "(a) 2x < 6 → x < 3\n(b) -3x ≥ 12 → x ≤ -4 (sign reverses)\n(c) 2x > 8 → x > 4"
                    }
                ]
            },
            {
                "exercise": "8.8",
                "title": "Exercise 8.8: Word Problems",
                "answerKeyText": "Exercise 8.8 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "The sum of two numbers is 45 and their difference is 15. Find the numbers.",
                        "solution": "Let the numbers be x and y.\nx + y = 45\nx - y = 15\nAdding equations: 2x = 60 → x = 30.\nSubtracting equations: 2y = 30 → y = 15.\nThe numbers are 30 and 15."
                    }
                ]
            },
            {
                "exercise": "Review 8",
                "title": "Review Exercise 8",
                "answerKeyText": "Review Exercise 8 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "If 3 pens and 2 books cost Rs 190, while 2 pens and 4 books cost Rs 260, find the cost of each item.",
                        "solution": "Let pen = p, book = b.\n3p + 2b = 190 ...(1)\n2p + 4b = 260 → p + 2b = 130 ...(2)\nSubtract (2) from (1): 2p = 60 → p = Rs 30 (cost of 1 pen).\nFrom (2): 30 + 2b = 130 → 2b = 100 → b = Rs 50 (cost of 1 book)."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Linear System",
                "formula": "a_1 x + b_1 y = c_1, \\quad a_2 x + b_2 y = c_2",
                "note": "Standard 2-variable linear system."
            },
            {
                "name": "Inequality Reversal",
                "formula": "a < b \\implies -a > -b",
                "note": "Multiplying/dividing by negative reverses inequality."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "If -4x < 12, then x is:", "options": ["A) x < -3", "B) x > -3", "C) x > 3", "D) x < 3"], "answer": "B) x > -3", "explanation": "Dividing by -4 reverses inequality sign: x > -3."},
                {"q": "The solution of x + y = 10 and x - y = 2 is:", "options": ["A) (5, 5)", "B) (6, 4)", "C) (7, 3)", "D) (8, 2)"], "answer": "B) (6, 4)", "explanation": "6 + 4 = 10 and 6 - 4 = 2."},
                {"q": "The graph of a linear equation in two variables is always a:", "options": ["A) Circle", "B) Parabola", "C) Straight line", "D) Triangle"], "answer": "C) Straight line", "explanation": "Linear equations produce straight lines."}
            ],
            "shortQuestions": [
                {"q": "Why does the inequality sign reverse when multiplying by a negative number?", "answer": "Because multiplying by a negative number reflects positions across zero on the number line, reversing their order (e.g., 2 < 5, but -2 > -5)."},
                {"q": "What is the condition for two linear equations to have a unique solution?", "answer": "The lines must intersect at a single point, which requires that their slopes are unequal (a1/a2 ≠ b1/b2)."}
            ],
            "longQuestions": [
                {"q": "The perimeter of a rectangle is 60 cm. The length is 6 cm more than twice the width. Find the dimensions of the rectangle.", "answer": "Let length = L and width = W.\n1. Perimeter = 2(L + W) = 60 → L + W = 30 ...(1)\n2. Condition: L = 2W + 6 ...(2)\nSubstitute (2) into (1):\n(2W + 6) + W = 30\n3W + 6 = 30 → 3W = 24 → W = 8 cm.\nThen L = 2(8) + 6 = 16 + 6 = 22 cm.\nLength = 22 cm, Width = 8 cm."}
            ]
        }
    }


def get_unit_9():
    return {
        "number": 9,
        "id": "unit-9",
        "title": "Surface, Area and Volume",
        "titleUrdu": "سطحی رقبہ اور حجم",
        "type": "chapter",
        "pageRange": "pp. 208–237",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 9 provides rigorous geometrical formulas and calculations for three-dimensional solid figures. It details circles (circumference C = 2πr, area A = πr²), cylinders (curved surface area = 2πrh, total surface area = 2πr(h+r), volume = πr²h), right circular cones (slant height l = √(r²+h²), curved surface area = πrl, total surface area = πr(l+r), volume = 1/3 πr²h), and spheres (surface area = 4πr², volume = 4/3 πr³).",
        "urduSummary": "یونٹ 9 سہ جہتی (3D) اشکال کے سطحی رقبے اور حجم کے فارمولوں اور ان کے عملی اطلاق کی وضاحت کرتا ہے۔ اس میں دائرہ (محیط C = 2πr، رقبہ A = πr²)، سلنڈر (خمدار سطحی رقبہ = 2πrh، کل سطحی رقبہ = 2πr(h+r)، حجم = πr²h)، مخروط (Cone) کا مائل ارتفاع l = √(r²+h²)، سطحی رقبہ اور حجم = 1/3 πr²h، اور کُرہ (Sphere) کا سطحی رقبہ = 4πr² اور حجم = 4/3 πr³ تفصیلاً شامل ہیں۔",
        "sections": [
            {
                "id": "9.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Calculate the circumference and area of a circle.\n• Find the surface area and volume of a cylinder.\n• Find the surface area and volume of a right circular cone.\n• Find the surface area and volume of a sphere and hemisphere.",
                "theory": "Core Competencies:\n1. Cylinder formulas: Curved Area = 2πrh, Total Area = 2πr(r + h), Volume = πr²h.\n2. Cone formulas: Slant height l = √(r² + h²), Curved Area = πrl, Total Area = πr(r + l), Volume = 1/3 πr²h.\n3. Sphere formulas: Surface Area = 4πr², Volume = 4/3 πr³.",
                "paras": [
                    "Calculate perimeter and area of circular regions.",
                    "Determine surface areas and capacities of cylindrical storage tanks.",
                    "Apply conic geometry formulas to cones and funnels.",
                    "Compute spherical surface areas and planetary or ballistic volumes."
                ]
            },
            {
                "id": "9.1-cylinder",
                "title": "9.1 Cylinder: Surface Area and Volume",
                "heading": "Cylinder: Surface Area and Volume",
                "headingUrdu": "سلنڈر: سطحی رقبہ اور حجم",
                "text": "A cylinder consists of two parallel congruent circular bases and a curved surface.\n• Curved Surface Area = 2πrh\n• Base Area (2 circular ends) = 2πr²\n• Total Surface Area = 2πrh + 2πr² = 2πr(h + r)\n• Volume = Base Area × Height = πr²h\n(Using π ≈ 22/7 or 3.1416).",
                "theory": "Cylinder Calculations:\nRadius r, height h.\nUnits: Surface area in cm² or m²; Volume in cm³ or m³ (1 m³ = 1000 litres).",
                "paras": [
                    "Curved area equals the circumference of the base multiplied by height.",
                    "Total surface area includes top and bottom circular bases.",
                    "Volume measures internal storage capacity."
                ]
            },
            {
                "id": "9.2-cone-sphere",
                "title": "9.2 Cone and Sphere: Surface Area & Volume",
                "heading": "Cone and Sphere: Surface Area & Volume",
                "headingUrdu": "مخروط اور کُرہ: رقبہ اور حجم",
                "text": "• Cone: Slant height l = √(r² + h²)\n  Curved Surface Area = πrl\n  Total Surface Area = πr(l + r)\n  Volume = 1/3 πr²h (exactly one-third of cylinder with same base and height).\n• Sphere: All points equidistant from center (radius r).\n  Surface Area = 4πr²\n  Volume = 4/3 πr³\n• Hemisphere: Half of a sphere.\n  Curved Area = 2πr², Total Area = 3πr², Volume = 2/3 πr³.",
                "theory": "Cone & Sphere Summary:\nCone volume is 1/3 the volume of a cylinder with identical base and height.\nSphere surface area equals 4 times the area of its great circle (4πr²).",
                "paras": [
                    "A cone's slant height relates to its radius and altitude by Pythagoras' theorem.",
                    "The volume of a cone is 1/3 πr²h.",
                    "A sphere's entire exterior surface is 4πr² and its volume is 4/3 πr³."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-9-1",
                "title": "Example 1: Volume and Area of Cylinder",
                "problem": "Find the total surface area and volume of a cylinder having radius 7 cm and height 10 cm (take π = 22/7).",
                "solution": "1. Total Surface Area = 2πr(h + r)\n= 2 × (22/7) × 7 × (10 + 7) = 44 × 17 = 748 cm².\n2. Volume = πr²h\n= (22/7) × 7² × 10 = (22/7) × 49 × 10 = 22 × 7 × 10 = 1540 cm³."
            },
            {
                "id": "we-8-9-2",
                "title": "Example 2: Volume and Area of Sphere",
                "problem": "A metal ball has radius 21 cm. Find its surface area and volume.",
                "solution": "1. Surface Area = 4πr² = 4 × (22/7) × 21² = 4 × (22/7) × 441 = 4 × 22 × 63 = 5544 cm².\n2. Volume = (4/3) πr³ = (4/3) × (22/7) × 21³ = (4/3) × (22/7) × 9261 = 4 × 22 × 441 = 38,808 cm³."
            }
        ],
        "exercises": [
            {
                "exercise": "9.1",
                "title": "Exercise 9.1: Circle & Cylinder",
                "answerKeyText": "Exercise 9.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the circumference and area of a circle with radius 14 cm.",
                        "solution": "C = 2πr = 2 × (22/7) × 14 = 88 cm.\nArea = πr² = (22/7) × 14² = (22/7) × 196 = 616 cm²."
                    },
                    {
                        "qNo": "2",
                        "question": "A cylindrical tank has radius 3.5 m and height 12 m. Find its volume.",
                        "solution": "V = πr²h = (22/7) × (3.5)² × 12 = (22/7) × 12.25 × 12 = 462 m³."
                    }
                ]
            },
            {
                "exercise": "9.3",
                "title": "Exercise 9.3: Cone",
                "answerKeyText": "Exercise 9.3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "The radius of the base of a cone is 6 cm and height is 8 cm. Find its slant height, curved surface area, and volume.",
                        "solution": "Slant height l = √(r² + h²) = √(6² + 8²) = √(36 + 64) = √100 = 10 cm.\nCurved Area = πrl = (22/7) × 6 × 10 = 1320 / 7 = 188.57 cm².\nVolume = (1/3) πr²h = (1/3) × (22/7) × 36 × 8 = (12 × 8 × 22) / 7 = 2112 / 7 = 301.71 cm³."
                    }
                ]
            },
            {
                "exercise": "9.5",
                "title": "Exercise 9.5: Sphere",
                "answerKeyText": "Exercise 9.5 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the surface area and volume of a sphere of radius 7 cm.",
                        "solution": "Surface Area = 4πr² = 4 × (22/7) × 49 = 4 × 22 × 7 = 616 cm².\nVolume = (4/3) πr³ = (4/3) × (22/7) × 343 = (4 × 22 × 49) / 3 = 4312 / 3 = 1437.33 cm³."
                    }
                ]
            },
            {
                "exercise": "Review 9",
                "title": "Review Exercise 9",
                "answerKeyText": "Review Exercise 9 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "How many litres of water can a cylindrical drum of radius 0.7 m and height 2 m hold? (1 m³ = 1000 litres)",
                        "solution": "Volume = πr²h = (22/7) × (0.7)² × 2 = (22/7) × 0.49 × 2 = 3.08 m³.\nCapacity = 3.08 × 1000 = 3,080 litres."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Cylinder Volume & Area",
                "formula": "V = \\pi r^2 h, \\quad A_{\\text{total}} = 2\\pi r(h + r)",
                "note": "Complete cylindrical solids."
            },
            {
                "name": "Cone & Sphere Volumes",
                "formula": "V_{\\text{cone}} = \\frac{1}{3} \\pi r^2 h, \\quad V_{\\text{sphere}} = \\frac{4}{3} \\pi r^3",
                "note": "Standard 3D solid capacities."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "The formula for the total surface area of a cylinder is:", "options": ["A) 2πrh", "B) 2πr(h + r)", "C) πr²h", "D) 4πr²"], "answer": "B) 2πr(h + r)", "explanation": "Curved area + 2 circular bases = 2πrh + 2πr² = 2πr(h + r)."},
                {"q": "If the radius of a sphere is doubled, its surface area becomes:", "options": ["A) 2 times", "B) 4 times", "C) 8 times", "D) 16 times"], "answer": "B) 4 times", "explanation": "A ∝ r², so (2r)² = 4r²."},
                {"q": "The volume of a cone is what fraction of the volume of a cylinder with identical radius and height?", "options": ["A) 1/2", "B) 1/3", "C) 1/4", "D) 2/3"], "answer": "B) 1/3", "explanation": "V_cone = (1/3)πr²h."}
            ],
            "shortQuestions": [
                {"q": "Define the slant height of a cone and state its formula in terms of radius and height.", "answer": "The slant height (l) is the distance from the apex of the cone to any point on the circumference of its circular base along its surface. By Pythagoras' theorem: l = √(r² + h²)."},
                {"q": "Write the formula for the curved surface area and volume of a hemisphere.", "answer": "Curved surface area = 2πr²; Volume = (2/3)πr³."}
            ],
            "longQuestions": [
                {"q": "A solid metal cone has base radius 6 cm and height 12 cm. It is melted and recast into a sphere of radius R. Assuming no loss of metal, find the radius R of the sphere.", "answer": "1. Volume of cone = (1/3) π r² h = (1/3) × π × 6² × 12 = (1/3) × π × 36 × 12 = 144π cm³.\n2. Volume of sphere = (4/3) π R³.\n3. Equating volumes:\n(4/3) π R³ = 144π\n(4/3) R³ = 144\nR³ = (144 × 3) / 4 = 36 × 3 = 108\nR = ∛108 ≈ 4.76 cm."}
            ]
        }
    }


def get_unit_10():
    return {
        "number": 10,
        "id": "unit-10",
        "title": "Geometry",
        "titleUrdu": "جیومیٹری",
        "type": "chapter",
        "pageRange": "pp. 238–274",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 10 covers demonstrative and practical geometry. It introduces deductive proofs based on axioms and postulates, proves Pythagoras' Theorem (c² = a² + b²) and its converse, demonstrates triangle congruence (SSS, SAS, ASA, RHS) and similarity criteria, classifies quadrilaterals (parallelograms, rectangles, rhombuses, trapeziums), and provides step-by-step constructions for geometric figures and circle tangents.",
        "urduSummary": "یونٹ 10 نظریاتی اور عملی جیومیٹری پر محیط ہے۔ اس میں مسلمات اور دعووں پر مبنی استخراجی ثبوت، مسئلہ فیثاغورث (c² = a² + b²) اور اس کا عکس، مثلثوں کی مطابقت (SSS, SAS, ASA, RHS) اور مشابہت کے اصول، چوکوروں (متوازی الاضلاع، مستطیل، معین، ذوزنقہ) کے خصائص، اور پرکار و فٹ رولر سے مثلثوں اور دائرے کے مماس کھینچنے کی عملی مشقیں شامل ہیں۔",
        "sections": [
            {
                "id": "10.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Understand axioms, postulates, and theorems in demonstrative geometry.\n• State and prove Pythagoras' Theorem and apply its converse.\n• Identify congruent and similar triangles using congruence criteria.\n• Construct triangles, quadrilaterals, and tangents to circles.",
                "theory": "Core Competencies:\n1. Pythagoras Theorem: In right ΔABC with ∠C = 90°, c² = a² + b².\n2. Converse: If c² = a² + b², the triangle is right-angled opposite to hypotenuse c.\n3. Congruence Criteria: SSS, SAS, ASA, RHS.\n4. Practical construction of tangents from an external point to a circle.",
                "paras": [
                    "Formulate deductive proofs using axioms and geometric theorems.",
                    "Verify and apply Pythagoras' Theorem in 2D Euclidean geometry.",
                    "Determine congruence and geometric similarity in polygons.",
                    "Execute accurate geometric constructions using compass and straightedge."
                ]
            },
            {
                "id": "10.1-pythagoras",
                "title": "10.1 Pythagoras' Theorem and its Converse",
                "heading": "Pythagoras' Theorem and its Converse",
                "headingUrdu": "مسئلہ فیثاغورث اور اس کا عکس",
                "text": "• Theorem: In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides:\n(Hypotenuse)² = (Base)² + (Perpendicular)²  →  c² = a² + b².\n• Converse: If the square of the longest side of a triangle is equal to the sum of the squares of the other two sides, the angle opposite the longest side is a right angle (90°).\n• Pythagorean Triples: Sets of three positive integers (a, b, c) satisfying a² + b² = c² (e.g., 3-4-5, 5-12-13, 7-24-25, 8-15-17).",
                "theory": "Proof Concept:\nIn right ΔABC with altitude dropped to the hypotenuse, two similar sub-triangles are formed, establishing geometric proportionality that yields c² = a² + b².",
                "paras": [
                    "Pythagoras' Theorem applies strictly to right-angled triangles.",
                    "The hypotenuse is the side opposite the 90° right angle and is the longest side.",
                    "The converse enables determining whether a triangle is right-angled from side lengths alone."
                ]
            },
            {
                "id": "10.2-congruence-quadrilaterals",
                "title": "10.2 Congruency, Similarity, & Quadrilaterals",
                "heading": "Congruency, Similarity, & Quadrilaterals",
                "headingUrdu": "مطابقت، مشابہت اور چوکوریں",
                "text": "• Congruent Triangles (≅): Exact same shape and size. Criteria:\n  1. SSS (Side-Side-Side)\n  2. SAS (Side-Angle-Side)\n  3. ASA (Angle-Side-Angle)\n  4. RHS (Right angle-Hypotenuse-Side)\n• Similar Triangles (~): Same shape, corresponding angles equal, corresponding sides proportional.\n• Quadrilaterals:\n  - Parallelogram: Opposite sides and angles equal; diagonals bisect each other.\n  - Rectangle: Parallelogram with all angles 90°; diagonals equal.\n  - Rhombus: Parallelogram with all 4 sides equal; diagonals perpendicular bisectors.\n  - Trapezium: Quadrilateral with one pair of parallel sides.",
                "theory": "Properties Summary:\nSum of interior angles of a quadrilateral = 360°.\nDiagonals of a rhombus intersect at 90°.",
                "paras": [
                    "Congruent triangles coincide completely in all angles and sides.",
                    "Similar figures maintain identical angular proportions with scaled sides.",
                    "Quadrilaterals are classified by parallelism, side lengths, and diagonal intersections."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-10-1",
                "title": "Example 1: Applying Pythagoras' Theorem",
                "problem": "In a right triangle, base = 8 cm and perpendicular = 6 cm. Find the hypotenuse.",
                "solution": "By Pythagoras' theorem:\nc² = a² + b²\nc² = 6² + 8² = 36 + 64 = 100\nc = √100 = 10 cm."
            },
            {
                "id": "we-8-10-2",
                "title": "Example 2: Verifying Right-Angled Triangle",
                "problem": "Determine whether a triangle with sides 9 cm, 12 cm, and 15 cm is right-angled.",
                "solution": "Longest side c = 15 cm. c² = 15² = 225.\nSum of squares of other sides: a² + b² = 9² + 12² = 81 + 144 = 225.\nSince c² = a² + b² (225 = 225), by the converse of Pythagoras' Theorem, the triangle is right-angled."
            }
        ],
        "exercises": [
            {
                "exercise": "10.1",
                "title": "Exercise 10.1: Pythagoras Applications",
                "answerKeyText": "Exercise 10.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the unknown side x in a right triangle where:\n(a) a = 5 cm, b = 12 cm, c = x\n(b) a = x, b = 24 cm, c = 25 cm",
                        "solution": "(a) x² = 5² + 12² = 25 + 144 = 169 → x = √169 = 13 cm.\n(b) x² + 24² = 25² → x² + 576 = 625 → x² = 49 → x = 7 cm."
                    }
                ]
            },
            {
                "exercise": "10.3",
                "title": "Exercise 10.3: Congruence",
                "answerKeyText": "Exercise 10.3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "State the congruence criterion that proves ΔABC ≅ ΔPQR if AB = PQ, BC = QR, and AC = PR.",
                        "solution": "SSS (Side-Side-Side) Congruence Criterion."
                    }
                ]
            },
            {
                "exercise": "10.9",
                "title": "Exercise 10.9: Quadrilateral Angles",
                "answerKeyText": "Exercise 10.9 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "In a parallelogram ABCD, ∠A = 70°. Find the remaining angles ∠B, ∠C, and ∠D.",
                        "solution": "In a parallelogram:\n• Opposite angles are equal: ∠C = ∠A = 70°.\n• Adjacent angles are supplementary: ∠A + ∠B = 180° → ∠B = 180° - 70° = 110°.\n• Opposite to ∠B: ∠D = ∠B = 110°.\nAngles are: ∠A = 70°, ∠B = 110°, ∠C = 70°, ∠D = 110°."
                    }
                ]
            },
            {
                "exercise": "Review 10",
                "title": "Review Exercise 10",
                "answerKeyText": "Review Exercise 10 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "A ladder 15 m long reaches a window 12 m above the ground. How far is the foot of the ladder from the wall?",
                        "solution": "Ladder = hypotenuse c = 15 m. Window height = perpendicular b = 12 m. Distance = base a.\na² = c² - b² = 15² - 12² = 225 - 144 = 81.\na = √81 = 9 meters."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Pythagoras' Theorem",
                "formula": "c^2 = a^2 + b^2",
                "note": "For any right-angled triangle where c is the hypotenuse."
            },
            {
                "name": "Quadrilateral Angle Sum",
                "formula": "\\sum \\angle_{\\text{interior}} = 360^\\circ",
                "note": "Sum of interior angles of any simple quadrilateral."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "In a right-angled triangle, the side opposite the 90° angle is called:", "options": ["A) Base", "B) Perpendicular", "C) Hypotenuse", "D) Altitude"], "answer": "C) Hypotenuse", "explanation": "The hypotenuse is opposite the right angle."},
                {"q": "Which of the following is a Pythagorean triple?", "options": ["A) (2, 3, 5)", "B) (3, 4, 5)", "C) (4, 5, 6)", "D) (5, 6, 7)"], "answer": "B) (3, 4, 5)", "explanation": "3² + 4² = 9 + 16 = 25 = 5²."},
                {"q": "The diagonals of a rhombus intersect each other at:", "options": ["A) 45°", "B) 60°", "C) 90°", "D) 180°"], "answer": "C) 90°", "explanation": "Rhombus diagonals are perpendicular bisectors."}
            ],
            "shortQuestions": [
                {"q": "State the RHS Congruence Criterion for triangles.", "answer": "If the hypotenuse and one side of a right-angled triangle are equal to the hypotenuse and corresponding side of another right-angled triangle, the two triangles are congruent (RHS: Right angle-Hypotenuse-Side)."},
                {"q": "What is the sum of adjacent angles in a parallelogram?", "answer": "Adjacent angles in a parallelogram are supplementary; their sum is 180°."}
            ],
            "longQuestions": [
                {"q": "Prove that the sum of all four interior angles of a quadrilateral is 360°.", "answer": "1. Let ABCD be a quadrilateral.\n2. Draw diagonal AC dividing ABCD into two triangles: ΔABC and ΔADC.\n3. In ΔABC: ∠1 + ∠2 + ∠B = 180° (angle sum of a triangle).\n4. In ΔADC: ∠3 + ∠4 + ∠D = 180°.\n5. Adding both equations:\n(∠1 + ∠3) + ∠B + (∠2 + ∠4) + ∠D = 180° + 180°\n∠A + ∠B + ∠C + ∠D = 360°.\nHence proved."}
            ]
        }
    }


def get_unit_11():
    return {
        "number": 11,
        "id": "unit-11",
        "title": "Data Management and Probability",
        "titleUrdu": "ڈیٹا مینجمنٹ اور امکانات (پروببلٹی)",
        "type": "chapter",
        "pageRange": "pp. 275–307",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 11 teaches data management and basic probability theory. It constructs frequency distributions for grouped data (class limits, boundaries, midpoint x, and width), renders graphical charts (histograms, frequency polygons, and pie charts), and computes measures of central tendency (Mean x̄ = Σfx/Σf, Median, and Mode). It develops probability concepts: sample space S, simple and compound events, independent events, and contrasts experimental probability with theoretical probability P(E) = n(E)/n(S).",
        "urduSummary": "یونٹ 11 شماریات (ڈیٹا مینجمنٹ) اور امکانیات (Probability) کا جامع احاطہ کرتا ہے۔ اس میں گروہی مواد کی فریکوئنسی تقسیم (کلاس حدود، کلاس باؤنڈریز، مڈ پوائنٹ، کلاس وقفہ)، گرافیکل نمائندگی (ہسٹوگرام، کثیر الاضلاع گراف، پائی چارٹ)، اور مرکزی رجحان کے پیمانے (حسابی اوسط x̄ = Σfx/Σf، وادیہ اور مد) شامل ہیں۔ علاوہ ازیں، سیمپل سپیس، واقعات، نظریاتی اور تجرباتی امکان P(E) = n(E)/n(S) کے سوالات تفصیلاً حل کیے گئے ہیں۔",
        "sections": [
            {
                "id": "11.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Construct grouped frequency distributions.\n• Draw histograms, frequency polygons, and pie charts.\n• Calculate Mean, Median, and Mode for grouped and ungrouped data.\n• Determine theoretical and experimental probability of events.",
                "theory": "Core Competencies:\n1. Frequency distribution components: Class Limits, Class Boundaries, Mid-point x = (Lower + Upper)/2, Frequency f.\n2. Mean: x̄ = Σfx / Σf.\n3. Probability: P(E) = Number of favorable outcomes n(E) / Total outcomes in sample space n(S). 0 ≤ P(E) ≤ 1.",
                "paras": [
                    "Organize raw empirical data into grouped frequency tables.",
                    "Construct histograms and pie charts with precise angular scales.",
                    "Calculate measures of central tendency for data sets.",
                    "Compute event probabilities and compare theoretical vs experimental odds."
                ]
            },
            {
                "id": "11.1-data-representation",
                "title": "11.1 Frequency Distribution and Histograms",
                "heading": "Frequency Distribution & Histograms",
                "headingUrdu": "فریکوئنسی تقسیم اور ہسٹوگرام",
                "text": "• Class Interval: A range of data values.\n• Class Boundaries: True limits of the class interval (subtract 0.5 from lower limit, add 0.5 to upper limit).\n• Mid-point (Class Mark): x = (Lower Limit + Upper Limit) / 2.\n• Histogram: A graph consisting of adjacent rectangles where width represents class boundaries and height represents frequency.",
                "theory": "Data Presentation Rules:\n• Frequency polygon is constructed by connecting mid-points of tops of histogram rectangles.\n• Pie Chart: Angular representation where each sector angle = (Component value / Total value) × 360°.",
                "paras": [
                    "Class boundaries eliminate gaps between intervals for continuous charting.",
                    "Histograms use adjacent bars without gaps between consecutive classes.",
                    "Pie charts distribute proportional angles totaling 360 degrees."
                ]
            },
            {
                "id": "11.2-central-tendency",
                "title": "11.2 Measures of Central Tendency",
                "heading": "Measures of Central Tendency",
                "headingUrdu": "مرکزی رجحان کے پیمانے",
                "text": "1. Mean (Arithmetic Average):\n   • Ungrouped: x̄ = Σx / n\n   • Grouped: x̄ = Σfx / Σf\n2. Median: The middle value when data is arranged in ascending order.\n3. Mode: The most frequently occurring value in the dataset (a dataset can be unimodal, bimodal, or have no mode).",
                "theory": "Formulas Summary:\nMean represents the balanced center of all data.\nMedian divides the ordered dataset into two equal halves.\nMode detects peak frequency density.",
                "paras": [
                    "The arithmetic mean combines all numerical observations divided by count.",
                    "The median represents the central element of an ordered dataset.",
                    "The mode indicates the most common observation."
                ]
            },
            {
                "id": "11.3-probability",
                "title": "11.3 Concept of Probability",
                "heading": "Concept of Probability",
                "headingUrdu": "امکانات (Probability) کا تصور",
                "text": "• Experiment: An operation that can produce certain well-defined outcomes.\n• Sample Space (S): The set of all possible outcomes (e.g. for a fair die, S = {1, 2, 3, 4, 5, 6}, n(S) = 6).\n• Event (E): Any subset of the sample space.\n• Theoretical Probability: P(E) = n(E) / n(S).\n• Certain Event: P = 1. Impossible Event: P = 0.\n• Independent Events: The occurrence of one event does not affect the occurrence of the other: P(A ∩ B) = P(A) × P(B).",
                "theory": "Probability Properties:\n1. 0 ≤ P(E) ≤ 1 for any event E.\n2. P(E') = 1 - P(E) (complementary event).\n3. Experimental probability is based on actual trials: (Number of times event occurred) / (Total number of trials performed). As trials increase, experimental probability converges to theoretical probability.",
                "paras": [
                    "Probability quantifies the likelihood of occurrence between 0 and 1.",
                    "A sample space encompasses all possible elementary outcomes.",
                    "Independent events do not influence each other's likelihood.",
                    "Experimental frequency approaches theoretical probability over many trials."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-11-1",
                "title": "Example 1: Calculating Grouped Mean",
                "problem": "Calculate the mean from the frequency table:\nClass: 10-20 (f=3), 20-30 (f=7), 30-40 (f=6), 40-50 (f=4).",
                "solution": "1. Find midpoints (x):\n• 10-20: x = 15, fx = 3 × 15 = 45\n• 20-30: x = 25, fx = 7 × 25 = 175\n• 30-40: x = 35, fx = 6 × 35 = 210\n• 40-50: x = 45, fx = 4 × 45 = 180\n2. Sums:\nΣf = 3 + 7 + 6 + 4 = 20\nΣfx = 45 + 175 + 210 + 180 = 610\n3. Mean x̄ = Σfx / Σf = 610 / 20 = 30.5."
            },
            {
                "id": "we-8-11-2",
                "title": "Example 2: Calculating Event Probability",
                "problem": "A fair die is rolled. Find the probability of getting: (a) an even number (b) a number greater than 4.",
                "solution": "Sample space S = {1, 2, 3, 4, 5, 6}, n(S) = 6.\n(a) Event A (even number) = {2, 4, 6}, n(A) = 3.\nP(A) = n(A) / n(S) = 3 / 6 = 1/2 (or 0.5).\n(b) Event B (number > 4) = {5, 6}, n(B) = 2.\nP(B) = n(B) / n(S) = 2 / 6 = 1/3 (or approx 0.33)."
            }
        ],
        "exercises": [
            {
                "exercise": "11.1",
                "title": "Exercise 11.1: Frequency Distribution",
                "answerKeyText": "Exercise 11.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "For the class interval 25 - 34, find:\n(a) Lower class limit and upper class limit\n(b) Class boundaries\n(c) Class midpoint\n(d) Class width",
                        "solution": "(a) Lower limit = 25, Upper limit = 34.\n(b) Class boundaries = 24.5 - 34.5.\n(c) Midpoint x = (25 + 34) / 2 = 59 / 2 = 29.5.\n(d) Class width = 34.5 - 24.5 = 10."
                    }
                ]
            },
            {
                "exercise": "11.2",
                "title": "Exercise 11.2: Mean and Central Tendency",
                "answerKeyText": "Exercise 11.2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the Mean, Median, and Mode of: 12, 15, 18, 12, 20, 14, 21.",
                        "solution": "1. Mean = (12 + 15 + 18 + 12 + 20 + 14 + 21) / 7 = 112 / 7 = 16.\n2. Ordered list: 12, 12, 14, 15, 18, 20, 21. Middle value (4th term) = 15. Median = 15.\n3. Mode: 12 occurs most frequently (twice). Mode = 12."
                    }
                ]
            },
            {
                "exercise": "11.4",
                "title": "Exercise 11.4: Probability",
                "answerKeyText": "Exercise 11.4 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "A bag contains 5 red balls, 3 green balls, and 2 blue balls. A ball is drawn at random. Find the probability that the ball is:\n(a) Red\n(b) Green\n(c) Not blue",
                        "solution": "Total balls n(S) = 5 + 3 + 2 = 10.\n(a) P(Red) = 5 / 10 = 1/2.\n(b) P(Green) = 3 / 10.\n(c) Not blue = Red + Green = 5 + 3 = 8 balls. P(Not blue) = 8 / 10 = 4/5."
                    },
                    {
                        "qNo": "2",
                        "question": "In a box there are 4 blue beads, 6 red beads, and 2 yellow beads. Sara picked a bead, recorded it, and put it back. She then picked a second bead. Tell if the events are independent and calculate the probability that the 1st is blue and 2nd is yellow.",
                        "solution": "1. The events are INDEPENDENT because the first bead is replaced before drawing the second, leaving the sample space unchanged.\n2. Total beads = 4 + 6 + 2 = 12.\n• P(1st is blue) = 4 / 12 = 1/3.\n• P(2nd is yellow) = 2 / 12 = 1/6.\n• P(Blue and Yellow) = (1/3) × (1/6) = 1/18."
                    }
                ]
            },
            {
                "exercise": "Review 11",
                "title": "Review Exercise 11",
                "answerKeyText": "Review Exercise 11 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "A coin is tossed 50 times. Heads appeared 28 times and Tails appeared 22 times. Find the experimental probability of getting (a) Head (b) Tail, and compare with theoretical probability.",
                        "solution": "(a) Experimental P(Head) = 28 / 50 = 0.56. Theoretical P(Head) = 1/2 = 0.50.\n(b) Experimental P(Tail) = 22 / 50 = 0.44. Theoretical P(Tail) = 1/2 = 0.50.\nThe experimental probabilities deviate slightly from 0.50 due to finite sample size variation."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Grouped Mean",
                "formula": "\\bar{x} = \\frac{\\sum f x}{\\sum f}",
                "note": "Arithmetic mean for grouped frequency data."
            },
            {
                "name": "Probability of an Event",
                "formula": "P(E) = \\frac{n(E)}{n(S)}, \\quad 0 \\le P(E) \\le 1",
                "note": "Ratio of favorable outcomes to total sample space."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "The probability of an impossible event is:", "options": ["A) 1", "B) 0.5", "C) 0", "D) -1"], "answer": "C) 0", "explanation": "Impossible events cannot happen."},
                {"q": "If P(E) = 0.35, then P(not E) is:", "options": ["A) 0.35", "B) 0.65", "C) 1.35", "D) 0"], "answer": "B) 0.65", "explanation": "P(E') = 1 - 0.35 = 0.65."},
                {"q": "The angle of a sector in a pie chart representing 25% of the total is:", "options": ["A) 25°", "B) 50°", "C) 90°", "D) 100°"], "answer": "C) 90°", "explanation": "25% of 360° = 0.25 × 360° = 90°."}
            ],
            "shortQuestions": [
                {"q": "What is the difference between class limits and class boundaries?", "answer": "Class limits are the stated endpoints of a class interval (e.g. 10 - 19), which often have gaps between consecutive classes. Class boundaries are continuous limits (e.g. 9.5 - 19.5) formed by eliminating gaps so the upper boundary of one class matches the lower boundary of the next."},
                {"q": "State the multiplication rule for two independent events A and B.", "answer": "For independent events A and B: P(A ∩ B) = P(A) × P(B)."}
            ],
            "longQuestions": [
                {"q": "A survey of 120 students recorded their favorite sport: Football (40), Cricket (50), Badminton (20), Basketball (10). Calculate the sector angles and describe how to construct a pie chart.", "answer": "Total students = 120. Total angle = 360°.\nAngle per student = 360° / 120 = 3°.\n• Football: 40 × 3° = 120°\n• Cricket: 50 × 3° = 150°\n• Badminton: 20 × 3° = 60°\n• Basketball: 10 × 3° = 30°\nCheck sum: 120° + 150° + 60° + 30° = 360°.\nConstruction: Draw a circle with a compass, draw a baseline radius, and measure consecutive sector angles using a protractor."}
            ]
        }
    }

print("Units 8, 9, 10, 11 defined successfully.")
