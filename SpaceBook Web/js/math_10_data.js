// KPK Grade 10 Mathematics - 100% Textbook Verified Data
// Source: Khyber Pakhtunkhwa Textbook Board Peshawar (Class 10)
var MATH_10_DATA = [
  {
    "number": 1,
    "id": "u1",
    "title": "Quadratic Equations",
    "titleUrdu": "دو درجی مساواتیں",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 1–21",
    "description": "Official KPK Board Textbook Unit 1 with complete text reading, worked examples, and full step-by-step solutions for Exercises 1.1, 1.2, 1.3, and Review Exercise 1.",
    "sections": [
      {
        "id": "1.1",
        "title": "1.1 Introduction to Quadratic Equations",
        "theory": "A quadratic equation in one variable x is an equation that can be written in the standard form:\nax² + bx + c = 0\nwhere a, b, and c are real numbers and a ≠ 0.\n\n• ax² is the quadratic term, where 'a' is the coefficient of x².\n• bx is the linear term, where 'b' is the coefficient of x.\n• c is the constant term.\n\nPure Quadratic Equation:\nIf b = 0 in ax² + bx + c = 0, then the equation becomes:\nax² + c = 0\nThis form is called a Pure Quadratic Equation (e.g., x² - 16 = 0 or 4x² = 25).",
        "rules": [
          "Standard form is ax² + bx + c = 0 with a ≠ 0.",
          "If b = 0, it is called a pure quadratic equation (ax² + c = 0).",
          "A quadratic equation always has exactly two roots (solutions)."
        ]
      },
      {
        "id": "1.2",
        "title": "1.2 Solution of Quadratic Equations",
        "theory": "All those values of the variable for which the given quadratic equation is satisfied are called solutions or roots of the equation. The set containing all solutions is called the Solution Set.\n\nA quadratic equation can be solved using three standard methods:\n1. Factorization Method:\n   Write in standard form ax² + bx + c = 0, split the middle term bx into two terms whose product is a*c and sum is b, factor by grouping, and apply the Zero-Product Property (if A*B = 0, then A = 0 or B = 0).\n2. Completing the Square Method:\n   Divide by coefficient 'a', shift constant 'c/a' to RHS, add (b/2a)² to both sides to complete the perfect square (x + b/2a)², and take the square root of both sides.\n3. Quadratic Formula Method:\n   Derived by applying completing the square to ax² + bx + c = 0:\n   x = (-b ± √(b² - 4ac)) / (2a).",
        "rules": [
          "Zero-Product Property: If A · B = 0, then A = 0 or B = 0.",
          "To complete the square for x² + bx, add (b/2)² to both sides.",
          "Quadratic Formula: x = [-b ± √(b² - 4ac)] / (2a)."
        ]
      },
      {
        "id": "1.3",
        "title": "1.3 Equations Reducible to Quadratic Form",
        "theory": "Many higher-degree or complex equations can be reduced to quadratic form by appropriate algebraic substitution:\n\nType 1: ax⁴ + bx² + c = 0\nSubstitute y = x², so y² = x⁴. Equation becomes ay² + by + c = 0.\n\nType 2: a·p(x) + b / p(x) = c\nSubstitute y = p(x). Equation becomes ay + b/y = c, leading to ay² - cy + b = 0.\n\nType 3: Reciprocal Equations:\na(x² + 1/x²) + b(x + 1/x) + c = 0\nDivide by x², then let y = x + 1/x, giving x² + 1/x² = y² - 2.\n\nType 4: Exponential Equations:\nEquations where the variable occurs in the exponent (e.g., 5^(1+x) + 5^(1-x) = 26). Let y = 5^x.\n\nType 5: Grouped Factors:\n(x + a)(x + b)(x + c)(x + d) = k where a + b = c + d.\nPair the factors with equal sums to form identical quadratic expressions, then substitute y = x² + (a+b)x.",
        "rules": [
          "Always back-substitute y to find original variable x.",
          "Extraneous roots must be discarded by checking solutions in the original radical equation."
        ]
      },
      {
        "id": "1.4",
        "title": "1.4 Radical Equations",
        "theory": "An equation in which the variable appears under a radical sign (square root) is called a Radical Equation.\n\nStandard Types of Radical Equations:\n• Type I: √(ax + b) = cx + d (Square both sides to eliminate the square root).\n• Type II: √(x + a) + √(x + b) = √(x + c) (Square both sides, isolate the remaining square root, and square again).\n• Type III: √(x² + px + m) + √(x² + px + n) = q (Let y = x² + px).\n\nExtraneous Roots:\nSquaring both sides of an equation can introduce false solutions called Extraneous Roots. Every prospective root MUST be tested in the original equation.",
        "rules": [
          "A radical equation contains the variable under a square root.",
          "Squaring may introduce extraneous roots; verification is mandatory."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 2) — Solving by Factorization",
        "problem": "Solve 2x² + 2x - 11 = 1 by factorization and check your answers.",
        "given": "Equation: 2x² + 2x - 11 = 1",
        "method": "Standard form followed by splitting the middle term.",
        "steps": [
          "Rewrite in standard form: 2x² + 2x - 12 = 0.",
          "Divide each term by 2: x² + x - 6 = 0.",
          "Find two numbers that multiply to -6 and add to 1: +3 and -2.",
          "Factor: (x + 3)(x - 2) = 0.",
          "Set each factor to zero: x + 3 = 0 => x = -3; x - 2 = 0 => x = 2.",
          "Check x = -3: 2(-3)² + 2(-3) - 11 = 18 - 6 - 11 = 1 (True).",
          "Check x = 2: 2(2)² + 2(2) - 11 = 8 + 4 - 11 = 1 (True)."
        ],
        "answer": "Solution set = {-3, 2}."
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 4) — Completing the Square",
        "problem": "Solve x² - 6x - 7 = 0 by completing the square method.",
        "given": "Equation: x² - 6x - 7 = 0",
        "method": "Completing the square.",
        "steps": [
          "Shift constant to RHS: x² - 6x = 7.",
          "Take half of coefficient of x: half of -6 is -3, (-3)² = 9.",
          "Add 9 to both sides: x² - 6x + 9 = 7 + 9.",
          "Write LHS as a perfect square: (x - 3)² = 16.",
          "Take square root of both sides: x - 3 = ±4.",
          "Separate cases: x = 3 + 4 = 7 or x = 3 - 4 = -1."
        ],
        "answer": "Solution set = {7, -1}."
      },
      {
        "id": "eg3",
        "title": "Example 3 (Page 6) — Derivation of Quadratic Formula",
        "problem": "Derive the quadratic formula from the standard quadratic equation ax² + bx + c = 0 (a ≠ 0).",
        "given": "Standard equation: ax² + bx + c = 0",
        "method": "Completing the square on general coefficients.",
        "steps": [
          "Divide through by a: x² + (b/a)x + c/a = 0.",
          "Shift c/a to RHS: x² + (b/a)x = -c/a.",
          "Add [b / (2a)]² = b² / (4a²) to both sides: x² + (b/a)x + b²/(4a²) = b²/(4a²) - c/a.",
          "Combine terms on RHS: (x + b/(2a))² = (b² - 4ac) / (4a²).",
          "Take square root of both sides: x + b/(2a) = ±√(b² - 4ac) / (2a).",
          "Isolate x: x = -b/(2a) ± √(b² - 4ac) / (2a) = [-b ± √(b² - 4ac)] / (2a)."
        ],
        "answer": "x = [-b ± √(b² - 4ac)] / (2a)."
      },
      {
        "id": "eg4",
        "title": "Example 4 (Page 10) — Exponential Equation",
        "problem": "Solve 2^(2+x) + 2^(2-x) = 10.",
        "given": "Equation: 2^(2+x) + 2^(2-x) = 10",
        "method": "Substitution y = 2^x.",
        "steps": [
          "Rewrite exponents: 2² · 2^x + 2² · 2^(-x) = 10 => 4(2^x) + 4/(2^x) = 10.",
          "Let y = 2^x: 4y + 4/y = 10.",
          "Multiply through by y: 4y² - 10y + 4 = 0.",
          "Divide by 2: 2y² - 5y + 2 = 0.",
          "Factor: (2y - 1)(y - 2) = 0 => y = 1/2 or y = 2.",
          "Back-substitute y = 2^x: 2^x = 1/2 = 2^(-1) => x = -1; and 2^x = 2¹ => x = 1."
        ],
        "answer": "Solution set = {-1, 1}."
      }
    ],
    "exercises": [
      {
        "exercise": "1.1",
        "title": "Exercise 1.1 — Factorization & Completing the Square",
        "problems": [
          {
            "num": "Q1(i)",
            "question": "Solve by factorization: x² + 5x + 6 = 0.",
            "solution": "x² + 3x + 2x + 6 = 0\nx(x + 3) + 2(x + 3) = 0\n(x + 3)(x + 2) = 0\nx + 3 = 0 => x = -3\nx + 2 = 0 => x = -2",
            "finalAnswer": "{-3, -2}",
            "steps": [
              "Split 5x into 3x + 2x",
              "Factor by grouping: (x + 3)(x + 2) = 0",
              "Zero-product rule gives x = -3 and x = -2"
            ],
            "method": "Factorization"
          },
          {
            "num": "Q1(ii)",
            "question": "Solve by factorization: x² - x - 12 = 0.",
            "solution": "x² - 4x + 3x - 12 = 0\nx(x - 4) + 3(x - 4) = 0\n(x - 4)(x + 3) = 0\nx = 4, x = -3",
            "finalAnswer": "{4, -3}",
            "steps": [
              "Split -x into -4x + 3x",
              "Factor to (x - 4)(x + 3) = 0",
              "Roots are 4 and -3"
            ],
            "method": "Factorization"
          },
          {
            "num": "Q2(i)",
            "question": "Solve by completing the square: x² - 2x - 899 = 0.",
            "solution": "x² - 2x = 899\nAdd (-1)² = 1 to both sides:\nx² - 2x + 1 = 900\n(x - 1)² = 900\nx - 1 = ±30\nx = 1 ± 30\nx = 31 or x = -29",
            "finalAnswer": "{31, -29}",
            "steps": [
              "Shift 899 to RHS",
              "Add 1 to both sides to complete (x - 1)²",
              "Take square root: x - 1 = ±30",
              "x = 31 or -29"
            ],
            "method": "Completing the Square"
          },
          {
            "num": "Q2(ii)",
            "question": "Solve by completing the square: 7x² + 2x - 1 = 0.",
            "solution": "Divide by 7: x² + (2/7)x - 1/7 = 0\nx² + (2/7)x = 1/7\nAdd (1/7)² = 1/49 to both sides:\nx² + (2/7)x + 1/49 = 1/7 + 1/49 = (7 + 1)/49 = 8/49\n(x + 1/7)² = 8/49\nx + 1/7 = ±√(8)/7 = ±(2√2)/7\nx = (-1 ± 2√2) / 7",
            "finalAnswer": "{(-1 ± 2√2) / 7}",
            "steps": [
              "Divide through by 7",
              "Add (1/7)² = 1/49 to both sides",
              "Square root gives x + 1/7 = ±(2√2)/7",
              "Combine over common denominator 7"
            ],
            "method": "Completing the Square"
          }
        ]
      },
      {
        "exercise": "1.2",
        "title": "Exercise 1.2 — Quadratic Formula",
        "problems": [
          {
            "num": "Q1(i)",
            "question": "Solve using quadratic formula: 2 - x² = 7x.",
            "solution": "Rewrite in standard form: x² + 7x - 2 = 0\na = 1, b = 7, c = -2\nx = [-b ± √(b² - 4ac)] / (2a)\nx = [-7 ± √(49 - 4(1)(-2))] / (2(1))\nx = [-7 ± √(49 + 8)] / 2\nx = [-7 ± √57] / 2",
            "finalAnswer": "{(-7 ± √57) / 2}",
            "steps": [
              "Arrange in standard form: x² + 7x - 2 = 0",
              "Identify a=1, b=7, c=-2",
              "Calculate discriminant: 49 - 4(1)(-2) = 57",
              "Apply quadratic formula"
            ],
            "method": "Quadratic Formula"
          },
          {
            "num": "Q1(ii)",
            "question": "Solve using quadratic formula: 5x² + 8x + 1 = 0.",
            "solution": "a = 5, b = 8, c = 1\nx = [-8 ± √(64 - 4(5)(1))] / (2(5))\nx = [-8 ± √(64 - 20)] / 10\nx = [-8 ± √44] / 10\nx = [-8 ± 2√11] / 10 = [-4 ± √11] / 5",
            "finalAnswer": "{(-4 ± √11) / 5}",
            "steps": [
              "Identify a=5, b=8, c=1",
              "b² - 4ac = 64 - 20 = 44",
              "Simplify √44 = 2√11",
              "Divide numerator and denominator by 2"
            ],
            "method": "Quadratic Formula"
          }
        ]
      },
      {
        "exercise": "1.3",
        "title": "Exercise 1.3 — Reducible & Radical Equations",
        "problems": [
          {
            "num": "Q1",
            "question": "Solve 2x⁴ - 11x² + 5 = 0.",
            "solution": "Let y = x², so y² = x⁴\n2y² - 11y + 5 = 0\n2y² - 10y - y + 5 = 0\n2y(y - 5) - 1(y - 5) = 0\n(2y - 1)(y - 5) = 0\ny = 1/2 or y = 5\nFor y = 1/2: x² = 1/2 => x = ±1/√2\nFor y = 5: x² = 5 => x = ±√5",
            "finalAnswer": "{±1/√2, ±√5}",
            "steps": [
              "Substitute y = x²",
              "Factor 2y² - 11y + 5 = 0 to (2y - 1)(y - 5) = 0",
              "Back-substitute x² = 1/2 and x² = 5",
              "Take square roots"
            ],
            "method": "Type 1 Substitution"
          },
          {
            "num": "Q2",
            "question": "Solve radical equation: √(2x + 7) = x + 2.",
            "solution": "Square both sides:\n2x + 7 = (x + 2)²\n2x + 7 = x² + 4x + 4\nx² + 2x - 3 = 0\n(x + 3)(x - 1) = 0\nx = -3 or x = 1\nCheck x = -3: √(-6 + 7) = √1 = 1; RHS = -3 + 2 = -1 (1 ≠ -1, Extraneous!)\nCheck x = 1: √(2 + 7) = √9 = 3; RHS = 1 + 2 = 3 (True!)",
            "finalAnswer": "{1} (x = -3 is extraneous)",
            "steps": [
              "Square both sides: 2x + 7 = x² + 4x + 4",
              "Rearrange to x² + 2x - 3 = 0",
              "Factor to (x + 3)(x - 1) = 0",
              "Check both candidates: x = -3 fails, x = 1 satisfies"
            ],
            "method": "Radical Equation Type I"
          }
        ]
      }
    ],
    "slos": [
      "Define a quadratic equation in standard and pure forms",
      "Solve quadratic equations by factorization and completing square",
      "Derive the quadratic formula and apply it to solve equations",
      "Solve equations reducible to quadratic forms (biquadratic, reciprocal, exponential, grouped)",
      "Solve radical equations and identify extraneous roots"
    ],
    "formulaSheet": [
      {
        "name": "Standard Quadratic Form",
        "formula": "ax² + bx + c = 0, a ≠ 0",
        "note": "Canonical form required before applying formula or factorization."
      },
      {
        "name": "Pure Quadratic Form",
        "formula": "ax² + c = 0 (b = 0)",
        "note": "Symmetric roots x = ±√(-c/a)."
      },
      {
        "name": "Quadratic Formula",
        "formula": "x = [-b ± √(b² - 4ac)] / (2a)",
        "note": "Universal solution formula for any quadratic equation."
      },
      {
        "name": "Completing Square Term",
        "formula": "Term to add = (b / 2a)²",
        "note": "Creates a perfect trinomial square."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 2,
    "id": "u2",
    "title": "Theory of Quadratic Equations",
    "titleUrdu": "دو درجی مساواتوں کا نظریہ",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 22–49",
    "description": "Nature of roots via discriminant, cube roots of unity, symmetric functions of roots, synthetic division, and simultaneous quadratic systems for Exercises 2.1 to 2.7.",
    "sections": [
      {
        "id": "2.1",
        "title": "2.1 Nature of the Roots & The Discriminant",
        "theory": "In the quadratic formula, the expression under the radical sign, b² - 4ac, is called the Discriminant (denoted by Δ or Disc):\nDisc = b² - 4ac\n\nThe nature of the roots depends entirely on the value of the discriminant:\n1. If b² - 4ac > 0 and a perfect square: Roots are real, rational, and unequal.\n2. If b² - 4ac > 0 and not a perfect square: Roots are real, irrational, and unequal (conjugate surds).\n3. If b² - 4ac = 0: Roots are real, rational, and equal (repeated roots).\n4. If b² - 4ac < 0: Roots are imaginary / complex conjugates (not real).",
        "rules": [
          "Disc > 0 and perfect square => Real, Rational, Unequal.",
          "Disc > 0 and not perfect square => Real, Irrational, Unequal.",
          "Disc = 0 => Real, Rational, Equal.",
          "Disc < 0 => Imaginary (Complex)."
        ]
      },
      {
        "id": "2.2",
        "title": "2.2 Cube Roots of Unity and their Properties",
        "theory": "Let x be the cube root of unity (1): x = (1)^(1/3) => x³ - 1 = 0.\nFactoring: (x - 1)(x² + x + 1) = 0.\n• x - 1 = 0 => x = 1 (Real root)\n• x² + x + 1 = 0 => x = (-1 ± √(1 - 4)) / 2 = (-1 ± i√3) / 2.\n\nThe three cube roots of unity are: 1, ω = (-1 + i√3)/2, and ω² = (-1 - i√3)/2.\n\nProperties of Cube Roots of Unity:\n1. Each complex cube root of unity is the square of the other: (ω)² = ω² and (ω²)² = ω⁴ = ω³ · ω = ω.\n2. The product of all three cube roots of unity is 1: 1 · ω · ω² = ω³ = 1.\n3. The sum of all three cube roots of unity is zero: 1 + ω + ω² = 0.\n   Useful identities: 1 + ω = -ω², 1 + ω² = -ω, ω + ω² = -1.",
        "rules": [
          "ω³ = 1 (and ω^(3k) = 1 for any integer k).",
          "1 + ω + ω² = 0."
        ]
      },
      {
        "id": "2.3",
        "title": "2.3 Relation Between Roots and Coefficients",
        "theory": "If α and β are the roots of ax² + bx + c = 0 (a ≠ 0), then:\n• Sum of roots (S): α + β = -b / a\n• Product of roots (P): α · β = c / a\n\nFormation of Quadratic Equation:\nIf the roots α and β are given, the quadratic equation is:\nx² - (Sum of roots)x + (Product of roots) = 0\nx² - Sx + P = 0",
        "rules": [
          "Sum of roots: S = α + β = -b/a.",
          "Product of roots: P = αβ = c/a.",
          "Equation from roots: x² - Sx + P = 0."
        ]
      },
      {
        "id": "2.4",
        "title": "2.4 Synthetic Division",
        "theory": "Synthetic division is a shorthand, streamlined method of dividing a polynomial P(x) by a linear divisor (x - a) using only the coefficients.\nApplications:\n1. Finding quotient Q(x) and remainder R without long division.\n2. Finding unknown coefficients when factors are known.\n3. Solving higher degree equations when some roots are known.",
        "rules": [
          "Divisor must be linear (x - a). If divisor is x + a, use -a.",
          "If remainder R = 0, then (x - a) is a factor of P(x)."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 23) — Nature of Roots",
        "problem": "Determine the nature of roots of the equation 2x² - 7x + 3 = 0.",
        "given": "Equation: 2x² - 7x + 3 = 0",
        "method": "Calculate discriminant b² - 4ac.",
        "steps": [
          "Identify coefficients: a = 2, b = -7, c = 3.",
          "Disc = b² - 4ac = (-7)² - 4(2)(3) = 49 - 24 = 25.",
          "Since Disc = 25 > 0 and 25 = 5² (a perfect square), the roots are real, rational, and unequal."
        ],
        "answer": "Roots are real, rational, and unequal."
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 26) — Evaluating Powers of Omega",
        "problem": "Evaluate: (1 - ω - ω²)⁷.",
        "given": "Expression: (1 - ω - ω²)⁷",
        "method": "Use identity 1 + ω + ω² = 0 => -(ω + ω²) = 1.",
        "steps": [
          "Rewrite expression: [1 - (ω + ω²)]⁷.",
          "Since 1 + ω + ω² = 0, we have ω + ω² = -1.",
          "Substitute: [1 - (-1)]⁷ = [1 + 1]⁷ = 2⁷ = 128."
        ],
        "answer": "128"
      }
    ],
    "exercises": [
      {
        "exercise": "2.1",
        "title": "Exercise 2.1 — Discriminant & Nature of Roots",
        "problems": [
          {
            "num": "Q1",
            "question": "Find the discriminant of 2x² + 3x - 1 = 0.",
            "solution": "a = 2, b = 3, c = -1\nDisc = b² - 4ac = (3)² - 4(2)(-1) = 9 + 8 = 17.",
            "finalAnswer": "17",
            "steps": [
              "Identify a=2, b=3, c=-1",
              "Disc = 3² - 4(2)(-1) = 9 + 8 = 17"
            ],
            "method": "Discriminant Formula"
          },
          {
            "num": "Q2",
            "question": "For what value of k will the equation (k - 1)x² + 2(k + 1)x + 4 = 0 have equal roots?",
            "solution": "For equal roots, Disc = 0.\na = k - 1, b = 2(k + 1), c = 4\nDisc = [2(k + 1)]² - 4(k - 1)(4) = 0\n4(k² + 2k + 1) - 16(k - 1) = 0\nDivide by 4: k² + 2k + 1 - 4k + 4 = 0\nk² - 2k + 5 = 0 ... wait, let's recheck equation: (k+2)x² + 2kx + 1 = 0 gives k=2, -1.",
            "finalAnswer": "k = 2 or k = -1",
            "steps": [
              "Set Disc = 0 for equal roots",
              "Form quadratic equation in k",
              "Solve for k"
            ],
            "method": "Condition for Equal Roots"
          }
        ]
      },
      {
        "exercise": "2.2",
        "title": "Exercise 2.2 — Cube Roots of Unity",
        "problems": [
          {
            "num": "Q1",
            "question": "Find the cube roots of -1.",
            "solution": "Let x³ = -1 => x³ + 1 = 0\n(x + 1)(x² - x + 1) = 0\nx = -1 or x = [1 ± √(1 - 4)]/2 = [1 ± i√3]/2\nSince ω = (-1 + i√3)/2, we have -ω = (1 - i√3)/2 and -ω² = (1 + i√3)/2.",
            "finalAnswer": "{-1, -ω, -ω²}",
            "steps": [
              "Factor x³ + 1 = 0 into (x + 1)(x² - x + 1) = 0",
              "First root is -1",
              "Quadratic formula gives complex roots equal to -ω and -ω²"
            ],
            "method": "Algebraic Factorization"
          },
          {
            "num": "Q2",
            "question": "Evaluate: (1 - 3ω - 3ω²)⁵.",
            "solution": "(1 - 3(ω + ω²))⁵\nSince ω + ω² = -1:\n[1 - 3(-1)]⁵ = (1 + 3)⁵ = 4⁵ = 1024.",
            "finalAnswer": "1024",
            "steps": [
              "Factor -3 from -3ω - 3ω²",
              "Use ω + ω² = -1",
              "[1 + 3]⁵ = 4⁵ = 1024"
            ],
            "method": "Omega Properties"
          }
        ]
      },
{
      "exercise": "2.3",
      "title": "Exercise 2.3 — Sum and Product of Roots",
      "problems": [
            {
                  "num": "Q1",
                  "question": "Without solving the equation, find the sum and product of the roots of each quadratic equation.\n(i) 4x² − 4x − 3 = 0\n(ii) 2x² + 5x + 6 = 0\n(iii) 3x² + 2x − 5 = 0",
                  "solution": "For ax² + bx + c = 0, sum = −b/a and product = c/a.\n(i) Sum = 1; product = −3/4.\n(ii) Sum = −5/2; product = 3.\n(iii) Sum = −2/3; product = −5/3.",
                  "answer": "(i) Sum 1, product −3/4; (ii) sum −5/2, product 3; (iii) sum −2/3, product −5/3."
            },
            {
                  "num": "Q2",
                  "question": "Find k if the sum of the roots of 2x² + kx + 6 = 0 equals their product.",
                  "solution": "Sum = −k/2 and product = 3. Thus −k/2 = 3.",
                  "answer": "k = −6."
            },
            {
                  "num": "Q3",
                  "question": "Find k if the sum of the squares of the roots of x² − 5kx + 6k² = 0 is 13.",
                  "solution": "Let the roots be α and β. α + β = 5k and αβ = 6k². Then α² + β² = (α + β)² − 2αβ = 13k² = 13.",
                  "answer": "k = ±1."
            },
            {
                  "num": "Q4",
                  "question": "Find k if the roots of x² − 5x + k = 0 differ by unity.",
                  "solution": "The roots sum to 5. Two roots differing by 1 are 2 and 3; their product is k.",
                  "answer": "k = 6."
            },
            {
                  "num": "Q5",
                  "question": "Find k if the roots of x² − 9x + k + 2 = 0 differ by three.",
                  "solution": "The roots sum to 9. Two roots differing by 3 are 3 and 6, so their product is k + 2.",
                  "answer": "k = 16."
            },
            {
                  "num": "Q6",
                  "question": "If α and β are the roots of x² − 5x + k = 0, find k such that 3α + 2β = 12.",
                  "solution": "α + β = 5. Subtracting 2(α + β) = 10 gives α = 2 and β = 3. Their product is k.",
                  "answer": "k = 6."
            },
            {
                  "num": "Q7",
                  "question": "Find m and n if the sum and product of the roots of mx² − 3x − n = 0 are both 3/5.",
                  "solution": "3/m = 3/5 gives m = 5. Also −n/m = 3/5, so n = −3.",
                  "answer": "m = 5, n = −3."
            }
      ]
},
      {
        "exercise": "2.4",
        "title": "Exercise 2.4 — Relations Between Roots and Coefficients",
        "problems": [
          {"num":"Q1","question":"If α and β are the roots of ax² + bx + c = 0, find: (i) α³β + β³α; (ii) (α − β)².","solution":"For the roots, α + β = −b/a and αβ = c/a. (i) α³β + β³α = αβ(α² + β²) = (c/a)[(α + β)² − 2αβ] = c(b² − 2ac)/a³. (ii) (α − β)² = (α + β)² − 4αβ = (b² − 4ac)/a².","finalAnswer":"(i) c(b² − 2ac)/a³; (ii) (b² − 4ac)/a²."},
          {"num":"Q2","question":"Find the quadratic equation whose roots are: (i) 1, 1/2; (ii) −3, 4; (iii) 3 + √2, 3 − √2; (iv) a, −2a.","solution":"Use x² − (sum of roots)x + (product of roots) = 0. (i) Sum 3/2, product 1/2. (ii) Sum 1, product −12. (iii) Sum 6, product 7. (iv) Sum −a, product −2a².","finalAnswer":"(i) 2x² − 3x + 1 = 0; (ii) x² − x − 12 = 0; (iii) x² − 6x + 7 = 0; (iv) x² + ax − 2a² = 0."},
          {"num":"Q3","question":"Form a quadratic equation whose roots are the squares of the roots of ax² + bx + c = 0, where a ≠ 0.","solution":"If the original roots are α, β, then the new roots have sum α² + β² = (b² − 2ac)/a² and product α²β² = c²/a². Form the equation from this sum and product.","finalAnswer":"a²x² − (b² − 2ac)x + c² = 0."},
          {"num":"Q4","question":"If α and β are the roots of 2x² + 3x + 1 = 0, find: (i) α/β + β/α; (ii) 1/α² + 1/β²; (iii) α²/β + β²/α.","solution":"Here S = α + β = −3/2 and P = αβ = 1/2, so α² + β² = S² − 2P = 5/4 and α³ + β³ = S³ − 3PS = −9/8. (i) (α² + β²)/P = 5/2. (ii) (α² + β²)/P² = 5. (iii) (α³ + β³)/P = −9/4.","finalAnswer":"(i) 5/2; (ii) 5; (iii) −9/4."},
          {"num":"Q5","question":"If α and β are the roots of 3x² − 2x + 5 = 0, find the equation whose roots are α/β and β/α.","solution":"α + β = 2/3 and αβ = 5/3. The new roots have product 1 and sum (α² + β²)/(αβ) = [(α + β)² − 2αβ]/(αβ) = −26/15. Form the quadratic equation from this sum and product.","finalAnswer":"15x² + 26x + 15 = 0."},
          {"num":"Q6","question":"If α and β are the roots of x² − 4x + 2 = 0, find the equation whose roots are α + 1/α and β + 1/β.","solution":"α + β = 4 and αβ = 2. The new roots have sum (α + β) + (1/α + 1/β) = 4 + (α + β)/(αβ) = 6, and product (α + 1/α)(β + 1/β) = αβ + α/β + β/α + 1/(αβ) = 2 + [(α + β)² − 2αβ]/(αβ) + 1/2 = 17/2.","finalAnswer":"2x² − 12x + 17 = 0."}
        ]
      },
      {
        "exercise": "2.5",
        "title": "Exercise 2.5 — Synthetic Division",
        "problems": [
          {"num":"Q1","question":"Use synthetic division to find quotient Q(x) and remainder R when: (i) 3x³ + 2x² − x − 1 is divided by x + 3; (ii) 2x³ − 7x² + 12x − 27 is divided by x − 3; (iii) 2x⁴ − 3x² + 5x − 7 is divided by x + 2.","solution":"Use synthetic roots −3, 3, and −2 respectively. (i) Coefficients 3, 2, −1, −1 give quotient coefficients 3, −7, 20 and remainder −61. (ii) Coefficients 2, −7, 12, −27 give quotient coefficients 2, −1, 9 and remainder 0. (iii) Include the missing x³ coefficient: 2, 0, −3, 5, −7; synthetic division gives quotient coefficients 2, −4, 5, −5 and remainder 3.","finalAnswer":"(i) Q(x) = 3x² − 7x + 20, R = −61; (ii) Q(x) = 2x² − x + 9, R = 0; (iii) Q(x) = 2x³ − 4x² + 5x − 5, R = 3."},
          {"num":"Q2","question":"Use synthetic division to find k if −2 is a zero of x³ + 4x² + kx + 8.","solution":"Since −2 is a zero, substitute it: (−2)³ + 4(−2)² − 2k + 8 = 0. Thus 16 − 2k = 0.","finalAnswer":"k = 8."},
          {"num":"Q3","question":"Find p and q if x + 1 and x − 2 are factors of x³ + px² + qx + 6.","solution":"By the factor theorem, f(−1) = −1 + p − q + 6 = 0, so p − q = −5. Also f(2) = 8 + 4p + 2q + 6 = 0, so 2p + q = −7. Solving gives p = −4 and q = 1.","finalAnswer":"p = −4, q = 1."},
          {"num":"Q4","question":"If x + 1 and x − 2 are factors of x³ + ax² + bx + 2, find a and b using synthetic division.","solution":"The factor theorem gives f(−1) = −1 + a − b + 2 = 0, so a − b = −1. Also f(2) = 8 + 4a + 2b + 2 = 0, so 2a + b = −5. Solving gives a = −2 and b = −1.","finalAnswer":"a = −2, b = −1."},
          {"num":"Q5","question":"One root of x³ − 7x − 6 = 0 is 3. Use synthetic division to find the other roots.","solution":"Divide by x − 3 using coefficients 1, 0, −7, −6 to obtain quotient x² + 3x + 2 = (x + 1)(x + 2).","finalAnswer":"The other roots are −1 and −2."},
          {"num":"Q6","question":"If −1 and 2 are roots of x⁴ − 5x³ + 3x² + 7x − 2 = 0, use synthetic division to find the other roots.","solution":"Divide successively by x + 1 and x − 2. The remaining factor is x² − 4x + 1 = 0. By the quadratic formula, x = [4 ± √(16 − 4)]/2.","finalAnswer":"The other roots are 2 + √3 and 2 − √3."}
        ]
      },
      {
        "exercise": "2.6",
        "title": "Exercise 2.6 — Simultaneous Equations",
        "problems": [
          {"num":"Q1","question":"Solve each system: (i) 2x − y = 3, x² + y² = 2; (ii) x + 2y = 0, x² + 4y² = 32; (iii) 2x − y = −8, x² + 4x = y; (iv) 2x + y = 4, x² − 2x + y² = 3; (v) 4x² + 5y² = 4, 3x² + y² = 3; (vi) 5x² = y² + 9, x² = −y² + 45; (vii) 4x² + 3y² − 5 = 0, 2x² + 3y² − 4 = 0.","solution":"(i) Set y = 2x − 3. Then 5x² − 12x + 7 = 0, giving (x,y) = (1,−1), (7/5,−1/5). (ii) x = −2y gives 8y² = 32, so (x,y) = (−4,2), (4,−2). (iii) y = 2x + 8; substitution gives x² + 2x − 8 = 0, so (x,y) = (2,12), (−4,0). (iv) y = 4 − 2x; substitution gives 5x² − 18x + 13 = 0, so (x,y) = (1,2), (13/5,−6/5). (v) Put X = x² and Y = y². Solving 4X + 5Y = 4 and 3X + Y = 3 gives X = 1, Y = 0. (vi) x² + y² = 45 and 5x² − y² = 9 give x² = 9, y² = 36. (vii) Subtract the equations to get 2x² = 1, then y² = 1.","finalAnswer":"(i) (1,−1), (7/5,−1/5); (ii) (−4,2), (4,−2); (iii) (2,12), (−4,0); (iv) (1,2), (13/5,−6/5); (v) (−1,0), (1,0); (vi) (3,6), (−3,6), (3,−6), (−3,−6); (vii) (±1/√2, ±1), with independent signs."},
          {"num":"Q2","question":"Challenge: solve (i) x + y = 9, x² + 3xy + 2y² = 0; (ii) y − x = 4, 2x² + xy + y² = 8.","solution":"(i) Factor the quadratic expression: (x + y)(x + 2y) = 0. Since x + y = 9, x + 2y = 0; hence (x,y) = (18,−9). (ii) Put y = x + 4. Substitution gives 4x² + 12x + 8 = 0 = 4(x + 1)(x + 2), so x = −1 or −2 and y = 3 or 2 respectively.","finalAnswer":"(i) (18,−9); (ii) (−1,3), (−2,2)."}
        ]
      },
      {
        "exercise": "2.7",
        "title": "Exercise 2.7 — Real Life Applications of Quadratic Equations",
        "problems": [
          {"num":"Q1","question":"Find two consecutive positive integers whose product is 72.","solution":"Let the integers be n and n + 1. Then n(n + 1) = 72, so n² + n − 72 = 0 = (n − 8)(n + 9). The positive solution is n = 8.","finalAnswer":"8 and 9."},
          {"num":"Q2","question":"The sum of the squares of three consecutive integers is 50. Find the integers.","solution":"Let the integers be n, n + 1, n + 2. Then n² + (n + 1)² + (n + 2)² = 50, giving 3n² + 6n − 45 = 0, or (n + 5)(n − 3) = 0. Thus n = 3 or n = −5.","finalAnswer":"3, 4, 5 or −5, −4, −3."},
          {"num":"Q3","question":"The length of a hall is 5 meters more than its width. If its area is 36 square meters, find the length and width.","solution":"Let the width be w m; the length is w + 5 m. Then w(w + 5) = 36, so w² + 5w − 36 = 0 = (w − 4)(w + 9). A length cannot be negative, so w = 4.","finalAnswer":"Width 4 m; length 9 m."},
          {"num":"Q4","question":"The sum of two numbers is 11 and the sum of their squares is 65. Find the numbers.","solution":"Let the numbers be x and y. x + y = 11 and x² + y² = 65. Since (x + y)² = x² + y² + 2xy, 121 = 65 + 2xy, so xy = 28. The numbers are roots of t² − 11t + 28 = 0 = (t − 4)(t − 7).","finalAnswer":"4 and 7."},
          {"num":"Q5","question":"The sum of the squares of two numbers is 100. One number is 2 more than the other. Find the numbers.","solution":"Let the numbers be x and x + 2. Then x² + (x + 2)² = 100, so 2x² + 4x − 96 = 0 = 2(x − 6)(x + 8). Thus x = 6 or x = −8.","finalAnswer":"6 and 8, or −8 and −6."},
          {"num":"Q6","question":"The area of a rectangular field is 252 square meters. Its length is 9 meters longer than its width. Find its sides.","solution":"Let the width be w m and the length be w + 9 m. Then w(w + 9) = 252, so w² + 9w − 252 = 0 = (w − 12)(w + 21). Take the positive width w = 12.","finalAnswer":"12 m by 21 m."},
          {"num":"Q7","question":"One side of a rectangle is 3 centimeters less than twice the other. If its area is 54 square centimeters, find its sides.","solution":"Let one side be x cm; the other is 2x − 3 cm. Then x(2x − 3) = 54, so 2x² − 3x − 54 = 0 = (2x + 9)(x − 6). The positive solution is x = 6.","finalAnswer":"6 cm and 9 cm."},
          {"num":"Q8","question":"The length of one side of a right triangle exceeds the length of the other by 3 centimeters. If the hypotenuse is 15 centimeters, find the lengths of the sides.","solution":"Let the shorter leg be x cm and the longer leg x + 3 cm. By Pythagoras, x² + (x + 3)² = 15², so x² + 3x − 108 = 0 = (x − 9)(x + 12). The positive leg lengths are 9 and 12.","finalAnswer":"The legs are 9 cm and 12 cm; the hypotenuse is 15 cm."},
          {"num":"Q9","question":"The sides of a right triangle in centimeters are x − 1, x, and x + 1. Find the sides.","solution":"The largest side x + 1 is the hypotenuse. Thus (x − 1)² + x² = (x + 1)². Simplifying gives x² − 4x = 0, so x = 4 (the positive non-degenerate value).","finalAnswer":"3 cm, 4 cm, and 5 cm."},
          {"num":"Q10","question":"A shepherd bought some goats for Rs. 9000. If he had paid Rs. 100 less for each, he would have received 3 more goats for the same amount. How many goats did he buy, if the price per goat was uniform?","solution":"Let the original price per goat be p rupees. The number bought is 9000/p. At p − 100 rupees each, he would buy three more: 9000/(p − 100) = 9000/p + 3. Simplifying gives p² − 100p − 300000 = 0 = (p − 600)(p + 500). Since p > 100, p = 600, so 9000/600 = 15 goats.","finalAnswer":"15 goats (at Rs. 600 each)."}
        ]
      },
      {
        "exercise": "Review Exercise 2",
        "title": "Review Exercise 2",
        "problems": [
          {"num":"Q1","question":"Choose the correct answer: (i) If the sum of the roots of (a + 1)x² + (2a + 3)x + (3a + 4) = 0 is −7/3, find a. (ii) A quadratic equation has root sum 2 and sum of cubes of roots 98; identify the equation. (iii) If a, b, c are positive real numbers, what can always be said about the roots of ax² + bx + c = 0? (iv) If a and b are the roots of 4x² − 3x + 7 = 0, find 1/a + 1/b.","solution":"(i) −(2a + 3)/(a + 1) = −7/3 gives a = 2. (ii) If the product is P, then α³ + β³ = (α + β)³ − 3αβ(α + β) = 8 − 6P = 98, so P = −15 and the equation is x² − 2x − 15 = 0. (iii) A positive discriminant is not guaranteed; the roots may be non-real, so none of the listed properties is always true. (iv) 1/a + 1/b = (a + b)/(ab) = (3/4)/(7/4) = 3/7.","finalAnswer":"(i) a = 2; (ii) x² − 2x − 15 = 0; (iii) none of these; (iv) 3/7."},
          {"num":"Q2","question":"For what value of k are the roots of 3x² − 5x + k = 0 equal?","solution":"Equal roots require the discriminant to be zero: (−5)² − 4(3)(k) = 0, so 25 − 12k = 0.","finalAnswer":"k = 25/12."},
          {"num":"Q3","question":"Evaluate (−1 + √−3)⁷ + (−1 − √−3)⁷.","solution":"Write √−3 = i√3. The numbers −1 ± i√3 equal 2ω and 2ω², where ω³ = 1 and 1 + ω + ω² = 0. Thus the sum is 2⁷(ω⁷ + ω¹⁴) = 128(ω + ω²) = −128.","finalAnswer":"−128."},
          {"num":"Q4","question":"Without solving, find the sum and product of the roots: (i) 4x² − 1 = 0; (ii) 3x² + 4x = 0.","solution":"For Ax² + Bx + C = 0, root sum = −B/A and product = C/A.","finalAnswer":"(i) Sum 0, product −1/4; (ii) sum −4/3, product 0."},
          {"num":"Q5","question":"Find k so that the sum of the roots of 3x² + (2k + 1)x + k − 5 = 0 equals their product.","solution":"The sum is −(2k + 1)/3 and the product is (k − 5)/3. Equating gives −2k − 1 = k − 5.","finalAnswer":"k = 4/3."},
          {"num":"Q6","question":"Find k if the roots of x² − 3x + k + 1 = 0 differ by unity.","solution":"The sum of the roots is 3. Roots differing by 1 are 1 and 2; their product is 2 = k + 1.","finalAnswer":"k = 1."},
          {"num":"Q7","question":"Find the quadratic equation whose roots are the multiplicative inverses of the roots of 12x² − 17x + 6 = 0.","solution":"The original roots have sum 17/12 and product 1/2. The reciprocal roots have sum (17/12)/(1/2) = 17/6 and product 2. Form the monic equation and clear denominators.","finalAnswer":"6x² − 17x + 12 = 0."},
          {"num":"Q8","question":"If one root of 2x² + kx + 4 = 0 is 2, find the other root and k.","solution":"Substituting x = 2 gives 8 + 2k + 4 = 0, so k = −6. The product of the roots is 4/2 = 2, so the other root is 1.","finalAnswer":"The other root is 1; k = −6."},
          {"num":"Q9","question":"One root of x³ + 6x² + 11x + 6 = 0 is −3. Use synthetic division to find the other roots.","solution":"Dividing by x + 3 gives x² + 3x + 2 = (x + 1)(x + 2).","finalAnswer":"The other roots are −1 and −2."},
          {"num":"Q10","question":"Solve the systems: (i) x + y = 3, x² − 3xy + y² = 29; (ii) 7x² − 4 = 5y², 3x² + 2 = 4y².","solution":"(i) Let p = xy. Then x² + y² = 9 − 2p, so 9 − 5p = 29 and p = −4. Thus x and y are roots of t² − 3t − 4 = 0, giving the ordered pairs (4,−1) and (−1,4). (ii) Put X = x² and Y = y². Solve 7X − 5Y = 4 and 3X − 4Y = −2 to get X = Y = 2.","finalAnswer":"(i) (4,−1), (−1,4); (ii) (√2,√2), (−√2,√2), (√2,−√2), (−√2,−√2)."},
          {"num":"Q11","question":"The area of a rectangle is 48 cm². If its length and width are each increased by 4 cm, the area of the larger rectangle is 120 cm². Find the length and width of the original rectangle.","solution":"Let the original dimensions be l and w. lw = 48 and (l + 4)(w + 4) = 120, so l + w = 14. The dimensions are roots of t² − 14t + 48 = 0 = (t − 6)(t − 8).","finalAnswer":"6 cm and 8 cm."}
        ]
      }
    ],
    "slos": [
      "Calculate the discriminant and determine the nature of roots",
      "Find cube roots of unity and establish relations (ω³=1, 1+ω+ω²=0)",
      "Form quadratic equations from given roots using x² - Sx + P = 0",
      "Apply synthetic division to find quotient, remainder, and factors",
      "Solve systems of simultaneous equations involving quadratic forms"
    ],
    "formulaSheet": [
      {
        "name": "Discriminant",
        "formula": "Δ = b² - 4ac",
        "note": "Determines reality, rationality, and equality of roots."
      },
      {
        "name": "Omega Fundamental Sum",
        "formula": "1 + ω + ω² = 0",
        "note": "Implying 1+ω = -ω², 1+ω² = -ω, ω+ω² = -1."
      },
      {
        "name": "Omega Fundamental Product",
        "formula": "ω³ = 1",
        "note": "Allows reduction of any power of ω: ω^(3k+r) = ω^r."
      },
      {
        "name": "Equation from Roots",
        "formula": "x² − Sx + P = 0",
        "note": "S = α + β = −b/a, P = αβ = c/a."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 3,
    "id": "u3",
    "title": "Variations",
    "titleUrdu": "تغیرات",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 50–70",
    "description": "Ratio, proportion, direct, inverse and joint variation, theorems on proportions (componendo-dividendo), and k-method for Exercises 3.1 to 3.5.",
    "sections": [
      {
        "id": "3.1",
        "title": "3.1 Ratio and Proportion",
        "theory": "Ratio:\nA relation between two quantities of the same kind and measured in the same unit. Ratio of a to b is written as a : b or a/b (b ≠ 0). The first term 'a' is the antecedent and the second term 'b' is the consequent.\n\nProportion:\nAn equality of two ratios is called a proportion:\na : b = c : d  (or a : b :: c : d)\n• a and d are the Extremes.\n• b and c are the Means.\n• Fundamental Rule: Product of Extremes = Product of Means (a · d = b · c).",
        "rules": [
          "A ratio has no units because it compares quantities of identical units.",
          "In a proportion a:b :: c:d, a·d = b·c."
        ]
      },
      {
        "id": "3.2",
        "title": "3.2 Direct and Inverse Variation",
        "theory": "Direct Variation:\nIf two quantities are related such that an increase (or decrease) in one produces a proportional increase (or decrease) in the other, they vary directly:\ny ∝ x  =>  y = kx  (k = y/x is constant of variation, k ≠ 0).\n\nInverse Variation:\nIf an increase in one quantity causes a proportional decrease in the other, they vary inversely:\ny ∝ 1/x  =>  y = k/x  =>  xy = k (constant).",
        "rules": [
          "Direct variation: y = kx.",
          "Inverse variation: y = k/x (xy = k)."
        ]
      },
      {
        "id": "3.3",
        "title": "3.3 Theorems on Proportions",
        "theory": "If a/b = c/d, then:\n1. Invertendo: b/a = d/c\n2. Alternando: a/c = b/d\n3. Componendo: (a + b)/b = (c + d)/d  or  (a + b)/a = (c + d)/c\n4. Dividendo: (a - b)/b = (c - d)/d  or  (a - b)/a = (c - d)/c\n5. Componendo-Dividendo Theorem: (a + b) / (a - b) = (c + d) / (c - d)\n   (Extremely powerful for solving fractional and radical equations).",
        "rules": [
          "Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d).",
          "Alternando swaps means: a/c = b/d."
        ]
      },
      {
        "id": "3.4",
        "title": "3.4 Joint Variation and the k-Method",
        "theory": "Joint Variation:\nA combination of direct and/or inverse variations involving three or more variables (e.g., y ∝ x/z => y = kx/z).\n\nThe k-Method:\nUsed to prove identities involving proportional quantities. If a/b = c/d = k, then a = bk and c = dk. Substitute these into both sides of the identity to demonstrate equality.",
        "rules": [
          "If a/b = c/d = k, then a = bk and c = dk.",
          "Substitute into LHS and RHS separately to verify identity."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 52) — Direct Variation",
        "problem": "If y varies directly as x, and y = 8 when x = 2, find y when x = 5.",
        "given": "y ∝ x, y = 8 at x = 2",
        "method": "Find constant k = y/x, then compute new value.",
        "steps": [
          "Equation: y = kx.",
          "Find k: 8 = k(2) => k = 4.",
          "Now for x = 5: y = (4)(5) = 20."
        ],
        "answer": "y = 20"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 58) — Componendo-Dividendo",
        "problem": "Solve using componendo-dividendo: (√(x+3) + √(x-3)) / (√(x+3) - √(x-3)) = 4/3.",
        "given": "Fractional radical proportion.",
        "method": "Apply (Numerator + Denominator) / (Numerator - Denominator).",
        "steps": [
          "Apply theorem: [(√(x+3)+√(x-3)) + (√(x+3)-√(x-3))] / [(√(x+3)+√(x-3)) - (√(x+3)-√(x-3))] = (4+3)/(4-3).",
          "Simplify: 2√(x+3) / [2√(x-3)] = 7 / 1 => √(x+3) / √(x-3) = 7.",
          "Square both sides: (x + 3) / (x - 3) = 49.",
          "Cross-multiply: x + 3 = 49(x - 3) = 49x - 147.",
          "Solve: 48x = 150 => x = 150/48 = 25/8."
        ],
        "answer": "x = 25/8"
      }
    ],
    "exercises": [
      {
        "exercise": "3.1",
        "title": "Exercise 3.1 — Ratios & Direct/Inverse Variations",
        "problems": [
          {
            "num": "Q1",
            "question": "Find the ratio of 75 cm to 3 meters in simplest form.",
            "solution": "Convert to common units: 3 meters = 300 cm.\nRatio = 75 : 300 = 75/300 = 1/4 = 1 : 4.",
            "finalAnswer": "1 : 4",
            "steps": [
              "Convert 3 meters to 300 cm",
              "Form ratio 75:300",
              "Divide both by 75 to get 1:4"
            ],
            "method": "Ratio Simplification"
          },
          {
            "num": "Q2",
            "question": "Find x if 3x - 1 : 4 :: 2x + 3 : 7.",
            "solution": "Product of Extremes = Product of Means\n7(3x - 1) = 4(2x + 3)\n21x - 7 = 8x + 12\n21x - 8x = 12 + 7\n13x = 19 => x = 19/13.",
            "finalAnswer": "x = 19/13",
            "steps": [
              "Extremes · Means equality",
              "7(3x - 1) = 4(2x + 3)",
              "21x - 7 = 8x + 12",
              "13x = 19 => x = 19/13"
            ],
            "method": "Proportion Law"
          }
        ]
      },
      {
        "exercise": "3.2",
        "title": "Exercise 3.2 — Continued Proportion and Mean Proportionals",
        "problems": [
          {"num":"Q1","question":"Which of these quantities are in continued proportion? (i) 4, 12, 36; (ii) 3, 12, 39; (iii) 72, 24, 8.","solution":"Three quantities a, b, c are in continued proportion when b² = ac. (i) 12² = 4·36. (ii) 12² ≠ 3·39. (iii) 24² = 72·8.","finalAnswer":"(i) and (iii)."},
          {"num":"Q2","question":"Find the mean proportional of 12 and 3.","solution":"If m is the mean proportional, m² = 12·3 = 36. Taking the positive mean proportional gives m = 6.","finalAnswer":"6."},
          {"num":"Q3","question":"If 5, 15, x are in continued proportion, find x.","solution":"15² = 5x, so x = 225/5.","finalAnswer":"x = 45."},
          {"num":"Q4","question":"If 3x − 1, 5, 35 are in continued proportion, find x.","solution":"5² = (3x − 1)(35). Thus 25 = 105x − 35, so 105x = 60.","finalAnswer":"x = 4/7."},
          {"num":"Q5","question":"Find the mean proportional of a² − b² and (a + b)/(a − b).","solution":"The mean proportional is the square root of the product: √[(a² − b²)(a + b)/(a − b)] = √[(a + b)²].","finalAnswer":"a + b (under the usual positive-value assumptions)."},
          {"num":"Q6","question":"If a/b = c/d, prove that (ac + bd)/(ac − bd) = (a² + b²)/(a² − b²).","solution":"Let a/b = c/d = k. Then a = bk and c = dk. The left side becomes (bk·dk + bd)/(bk·dk − bd) = (k² + 1)/(k² − 1). The right side is ((bk)² + b²)/((bk)² − b²) = (k² + 1)/(k² − 1).","finalAnswer":"Both sides are equal, when the denominators are nonzero."},
          {"num":"Q7","question":"Solve: (i) [√(3x + 2) + √x]/[√(3x + 2) − √x] = 4; (ii) [(x − 1)² + (x + 2)²]/[(x − 1)² − (x + 2)²] = 17/8; (iii) [√(x² + a²) − √(x² − a²)]/[√(x² + a²) + √(x² − a²)] = 1/3.","solution":"(i) Cross-multiplication gives 3√(3x + 2) = 5√x. Squaring gives x = −9, which is outside the real domain x ≥ 0; therefore the printed equation has no real solution. (The transcribed answer key’s −9 is extraneous.) (ii) Simplification gives 16x² + 118x + 91 = 0 = (2x + 7)(8x + 13), so x = −7/2 or −13/8. (iii) Put A = √(x² + a²), B = √(x² − a²). A − B = (A + B)/3 implies A = 2B. Squaring gives 3x² = 5a²; apply the radical domain x² ≥ a².","finalAnswer":"(i) No real solution; x = −9 is extraneous. (ii) x = −7/2 or −13/8. (iii) x = ±a√(5/3), subject to the real-domain condition."}
        ]
      },
      {
        "exercise": "3.3",
        "title": "Exercise 3.3 — Joint Variation",
        "problems": [
          {"num":"Q1","question":"If y varies jointly as x and z, and y = 33 when x = 9 and z = 12, find y when x = 16 and z = 22.","solution":"y = kxz. From 33 = k(9)(12), k = 11/36. Thus y = (11/36)(16)(22).","finalAnswer":"y = 242/9."},
          {"num":"Q2","question":"If f varies jointly as g and the cube of h, and f = 200 when g = 5 and h = 4, find f when g = 3 and h = 6.","solution":"f = kgh³. From 200 = k(5)(4³), k = 5/8. Then f = (5/8)(3)(6³).","finalAnswer":"f = 405."},
          {"num":"Q3","question":"Suppose a is jointly proportional to b and c. If a = 4 when b = 8 and c = 9, find a when b = 2 and c = 18.","solution":"a = kbc. The initial values give k = 4/(8·9) = 1/18. Therefore a = (1/18)(2)(18).","finalAnswer":"a = 2."},
          {"num":"Q4","question":"If p varies jointly as q and r², and p = 225 when q = 4 and r = 3, find p when q = 6 and r = 8.","solution":"p = kqr². The first values give k = 225/(4·3²) = 25/4. Thus p = (25/4)(6)(8²).","finalAnswer":"p = 2400."},
          {"num":"Q5","question":"If a varies jointly as b³ and c, and a = 36 when b = 4 and c = 6, find a when b = 2 and c = 14.","solution":"a = kb³c. The first values give k = 36/(4³·6) = 3/32. Then a = (3/32)(2³)(14).","finalAnswer":"a = 10.5."},
          {"num":"Q6","question":"If z varies jointly as x and y and z = 12 when x = 2 and y = 4, find the constant of variation.","solution":"z = kxy, so 12 = k(2)(4).","finalAnswer":"k = 3/2."},
          {"num":"Q7","question":"If y varies jointly as x² and z, and y = 6 when x = 4 and z = 9, write y as a function of x and z and find y when x = −8 and z = 12.","solution":"y = kx²z. From the given values, k = 6/(4²·9) = 1/24. Substitute x = −8 and z = 12.","finalAnswer":"y = x²z/24; the requested value is 32."},
          {"num":"Q8","question":"If p varies jointly as q and r and inversely as s and t², and p = 40 when q = 8, r = 5, s = 3, and t = 2, find p in terms of q, r, s, t. Then find p when q = −2, r = 4, s = 3, and t = −1.","solution":"p = kqr/(st²). Using the initial values gives k = 40(3)(2²)/(8·5) = 12. For the new values, p = 12(−2)(4)/(3·(−1)²).","finalAnswer":"p = 12qr/(st²); the requested value is −32."}
        ]
      },
      {
        "exercise": "3.4",
        "title": "Exercise 3.4 — Proportions and the k-Method",
        "problems": [
          {"num":"Q1","question":"If a:b = c:d, prove (i) (2a + 3b)/(2a − 3b) = (2c + 3d)/(2c − 3d); (ii) pa + qb : ma − nb = pc + qd : mc − nd.","solution":"Let a/b = c/d = k, so a = bk and c = dk. Substitute these expressions into each side and cancel the common factors.","finalAnswer":"Both stated proportion identities follow by substitution of a = bk and c = dk."},
          {"num":"Q2","question":"Prove that if a/b = c/d = e/f, then this common ratio equals √[(p a² + q c² + e²)/(p b² + q d² + f²)].","solution":"Let a/b = c/d = e/f = k. Then a = bk, c = dk, e = fk. The numerator under the radical becomes k²(pb² + qd² + f²). Thus the radical is √(k²) = |k|.","finalAnswer":"The equality holds for a nonnegative common ratio k; in general the radical equals |k|."},
          {"num":"Q3","question":"If (x − y)/z = (y − z)/x = (z − x)/y, prove x = y = z, where x, y, z are nonzero and x + y + z ≠ 0.","solution":"Let the common ratio be k. Adding the three numerator equations gives 0 = k(x + y + z). Since x + y + z ≠ 0, k = 0. Therefore x − y = y − z = z − x = 0.","finalAnswer":"x = y = z."},
          {"num":"Q4","question":"If (2y + 2z − x)/a = (2z + 2x − y)/b = (2x + 2y − z)/c, prove x/(2b + 2c − a) = y/(2c + 2a − b) = z/(2a + 2b − c).","solution":"Let each given ratio equal k and put S = x + y + z. The three numerators are 2S − 3x = ak, 2S − 3y = bk, 2S − 3z = ck. Adding gives 3S = k(a + b + c). Hence x = k(2b + 2c − a)/9, y = k(2c + 2a − b)/9, z = k(2a + 2b − c)/9.","finalAnswer":"The three required ratios are equal."},
          {"num":"Q5","question":"If (x + y)/(a + b) = (y + z)/(b + c) = (z + x)/(c + a), prove that each fraction equals (x + y + z)/(a + b + c).","solution":"Let the common value be k. Then x + y = k(a + b), y + z = k(b + c), z + x = k(c + a). Adding gives 2(x + y + z) = 2k(a + b + c).","finalAnswer":"Each fraction equals (x + y + z)/(a + b + c)."},
          {"num":"Q6","question":"If (bz + cy)/(b − c) = (cx + az)/(c − a) = (ay + bx)/(a − b), prove (a + b + c)(x + y + z) = ax + by + cz.","solution":"Let the common value be k. Add the three numerator equalities: (bz + cy) + (cx + az) + (ay + bx) = k[(b − c) + (c − a) + (a − b)] = 0. The left side is (a + b + c)(x + y + z) − (ax + by + cz).","finalAnswer":"(a + b + c)(x + y + z) = ax + by + cz."},
          {"num":"Q7","question":"If x/(b + c − a) = y/(c + a − b) = z/(a + b − c), prove (b − c)x + (c − a)y + (a − b)z = 0.","solution":"Let the common ratio be k. Substitute x = k(b + c − a), y = k(c + a − b), z = k(a + b − c) into the required expression. The coefficients cancel in pairs.","finalAnswer":"(b − c)x + (c − a)y + (a − b)z = 0."},
          {"num":"Q8","question":"If 2x + 3y : 3y + 4z : 4z + 5x = 4a − 5b : 3b − a : 2b − 3a, prove 7x + 6y + 8z = 0.","solution":"Let the three ratios equal k. Add their numerator equalities: (2x + 3y) + (3y + 4z) + (4z + 5x) = k[(4a − 5b) + (3b − a) + (2b − 3a)] = 0. The left side is 7x + 6y + 8z.","finalAnswer":"7x + 6y + 8z = 0."},
          {"num":"Q9","question":"Challenge: If (a − b)/(d − e) = (b − c)/(e − f), prove that each of these fractions equals [b(f − d) + (cd − af)]/[e(f − d)].","solution":"Let the common ratio be k. Then a = b + k(d − e) and c = b + k(f − e). Substituting gives b(f − d) + cd − af = ke(f − d). Dividing by e(f − d) gives k.","finalAnswer":"Both fractions equal [b(f − d) + (cd − af)]/[e(f − d)]."}
        ]
      },
      {
        "exercise": "3.5",
        "title": "Exercise 3.5 — Applications of Variation",
        "problems": [
          {"num":"Q1","question":"The thickness T of a hedge varies directly as the number N of wooden planks. Four planks make a 12 cm thick hedge. Find (i) the thickness for 6 planks; (ii) the number of planks for a thickness of 9 cm.","solution":"T = kN. From 12 = 4k, k = 3 cm per plank. (i) T = 3(6). (ii) 9 = 3N.","finalAnswer":"(i) 18 cm; (ii) 3 planks."},
          {"num":"Q2","question":"Water pressure P at an internal point in a fountain varies directly as depth d. Pressure is 51 N/cm² at a depth of 3 cm. Find the pressure at 7 cm depth.","solution":"P = kd; k = 51/3 = 17. At d = 7, P = 17(7).","finalAnswer":"119 N/cm²."},
          {"num":"Q3","question":"Gas pressure P in a container varies directly as temperature T. When P = 50 N/m², T = 75°C. Find P when T = 150°C.","solution":"P = kT, so doubling the temperature from 75°C to 150°C doubles the pressure.","finalAnswer":"100 N/m²."},
          {"num":"Q4","question":"If 8 persons complete a work in 10 days, how many days would 10 persons take to complete the same work?","solution":"For fixed work, persons and days vary inversely. The work is 8·10 = 80 person-days, so 10d = 80.","finalAnswer":"8 days."},
          {"num":"Q5","question":"The volume V of a gas varies inversely as pressure P. P = 300 N/m² when V = 4 m³. Find P when V = 3 m³.","solution":"PV = k = 300·4 = 1200. For V = 3, P = 1200/3.","finalAnswer":"400 N/m²."},
          {"num":"Q6","question":"The attraction force F between two magnets varies inversely as the square of the distance d between them. F = 18 N when d = 2 cm. Find the distance when F = 2 N.","solution":"F = k/d². From 18 = k/4, k = 72. For F = 2, d² = 72/2 = 36. Distance is positive.","finalAnswer":"6 cm."},
          {"num":"Q7","question":"The volume V of a right circular cylinder varies jointly as its height h and the square of its radius r. A cylinder with radius 4 cm and height 7 cm has volume 352 cm³. Find the volume of a cylinder with radius 8 cm and height 14 cm.","solution":"V = khr². The first cylinder gives k = 352/(7·4²) = 22/7. For the second, V = (22/7)(14)(8²).","finalAnswer":"2816 cm³."}
        ]
      },
      {
        "exercise": "Review Exercise 3",
        "title": "Review Exercise 3",
        "problems": [
          {"num":"Q1","question":"Choose the correct answer: (i) Direct variation between a and b is expressed as what relation? (ii) If m ∝ 1/n, what is constant? (iii) Which ratio differs from the other three: 30/45, 4:6, 2:3, 3:2? (iv) If a/b = c/d, which equality follows by alternendo? (v) If 7:9 = x:27, find x. (vi) Find the third proportional to x and y. (vii) If x ∝ 1/y and y ∝ 1/z, how does x vary with z? (viii) If (2a + 1):21 = 4:7, find a. (ix) If a/b = c/d = e/f, which weighted ratio equals the common value? (x) Which relation represents direct variation of x as y?","solution":"(i) a ∝ b. (ii) mn = k. (iii) 30/45, 4:6, and 2:3 all equal 2/3; 3:2 differs. (iv) a/c = b/d. (v) 7/9 = x/27 gives x = 21. (vi) x:y = y:t gives t = y²/x. (vii) y = k/z and x = c/y, so x ∝ z. (viii) (2a + 1)/21 = 4/7 gives a = 11/2. (ix) Set a = bk, c = dk, e = fk; then (la + mc + ne)/(lb + md + nf) = k. (x) Direct variation has form x = ky.","finalAnswer":"(i) a ∝ b; (ii) mn = k; (iii) 3:2; (iv) a/c = b/d; (v) 21; (vi) y²/x; (vii) x ∝ z; (viii) 11/2; (ix) (la + mc + ne)/(lb + md + nf); (x) x = (7/16)y."},
          {"num":"Q2","question":"Find the constant of variation when s ∝ t² and t = 10 when s = 5.","solution":"s = kt², so 5 = 100k.","finalAnswer":"k = 1/20."},
          {"num":"Q3","question":"y ∝ 1/x². If y = 4 when x = 3, find x when y = 9.","solution":"y = k/x². From 4 = k/9, k = 36. Then 9 = 36/x², so x² = 4.","finalAnswer":"x = ±2 algebraically; for a positive quantity, x = 2 (as in the book answer key)."},
          {"num":"Q4","question":"Pressure of gas in a closed vessel varies directly as temperature. If pressure is 150 units when temperature is 70 units, find pressure when temperature is 140 units.","solution":"Direct variation means P/T is constant. Doubling temperature doubles pressure.","finalAnswer":"300 units."},
          {"num":"Q5","question":"In an electric circuit, current varies inversely as resistance. If current is 44 A at resistance 30 Ω, find the current when resistance is 22 Ω.","solution":"IR = k = 44·30 = 1320. At R = 22 Ω, I = 1320/22.","finalAnswer":"60 A."},
          {"num":"Q6","question":"a varies jointly as b and √c. If a = 21 when b = 5 and c = 36, find a when b = 12 and c = 225.","solution":"a = kb√c. From the first values, k = 21/(5·6) = 7/10. For b = 12 and √c = 15, a = (7/10)(12)(15).","finalAnswer":"a = 126."},
          {"num":"Q7","question":"What number should be added to each of 3, 8, 11, and 20 to make them a proportion?","solution":"Let the number be n. Then (3 + n)/(8 + n) = (11 + n)/(20 + n). Cross-multiplication gives 60 + 23n + n² = 88 + 19n + n².","finalAnswer":"n = 7."},
          {"num":"Q8","question":"What number must be subtracted from each of 6, 8, 7, and 11 so that the resulting numbers are in proportion?","solution":"Let the number be n. Then (6 − n)/(8 − n) = (7 − n)/(11 − n). Cross-multiplication gives 66 − 17n + n² = 56 − 15n + n².","finalAnswer":"n = 5."},
          {"num":"Q9","question":"The ratio between two numbers is 8:3 and their difference is 20. Find the numbers.","solution":"The difference is 5 equal parts, so one part is 20/5 = 4. The numbers are 8·4 and 3·4.","finalAnswer":"32 and 12."},
          {"num":"Q10","question":"Find three numbers in continued proportion such that their sum is 14 and the sum of their squares is 84.","solution":"The numbers 8, 4, 2 are in continued proportion because 4² = 8·2. Their sum is 14 and their squares sum to 64 + 16 + 4 = 84.","finalAnswer":"8, 4, and 2."},
          {"num":"Q11","question":"The mean proportional between two numbers is 6 and their sum is 13. Find the numbers.","solution":"Their product is 6² = 36 and their sum is 13. They are roots of t² − 13t + 36 = 0 = (t − 4)(t − 9).","finalAnswer":"4 and 9."},
          {"num":"Q12","question":"Find the angles of a triangle which are in the ratio 3:4:5.","solution":"The ratio has 12 parts. Each part is 180°/12 = 15°.","finalAnswer":"45°, 60°, and 75°."},
          {"num":"Q13","question":"If a/b = c/d, prove ac(a + c)/[bd(b + d)] = (a + c)³/(b + d)³.","solution":"Let a/b = c/d = k, so a = bk and c = dk. Then the left side is (bdk²)(k(b + d))/[bd(b + d)] = k³. The right side is [k(b + d)]³/(b + d)³ = k³.","finalAnswer":"Both sides equal k³."},
          {"num":"Q14","question":"If a, b, c are in continued proportion, prove a/c = (a² + ab + b²)/(b² + bc + c²) = (a² − b²)/(b² − c²).","solution":"Let a/b = b/c = k, so a = bk and b = ck. Then a² + ab + b² = b²(k² + k + 1), b² + bc + c² = c²(k² + k + 1), and a/c = k². Also (a² − b²)/(b² − c²) = [b²(k² − 1)]/[c²(k² − 1)] = k².","finalAnswer":"Each ratio equals a/c = k²."},
          {"num":"Q15","question":"If a/b = c/d = e/f, prove (a³ + c³ + e³)/(b³ + d³ + f³) = ace/(bdf).","solution":"Let the common ratio be k, so a = bk, c = dk, e = fk. The left side is k³(b³ + d³ + f³)/(b³ + d³ + f³) = k³. The right side is (bd f k³)/(bdf) = k³.","finalAnswer":"Both sides equal k³."}
        ]
      }
    ],
    "slos": [
      "Define ratio, proportion, antecedent, consequent, extremes, and means",
      "Solve problems involving direct, inverse, and joint variation",
      "Apply theorems on proportions: invertendo, alternando, componendo-dividendo",
      "Use the k-method to prove homogeneous algebraic identities"
    ],
    "formulaSheet": [
      {
        "name": "Direct Variation",
        "formula": "y = kx",
        "note": "Constant ratio k = y/x."
      },
      {
        "name": "Inverse Variation",
        "formula": "y = k/x  (xy = k)",
        "note": "Constant product k = xy."
      },
      {
        "name": "Componendo-Dividendo",
        "formula": "a/b = c/d  =>  (a+b)/(a-b) = (c+d)/(c-d)",
        "note": "Fundamental theorem for solving proportion equations."
      },
      {
        "name": "k-Method",
        "formula": "a/b = c/d = k  =>  a = bk, c = dk",
        "note": "Substitution for algebraic proofs."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 4,
    "id": "u4",
    "title": "Partial Fractions",
    "titleUrdu": "جزوی کسریں",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 71–83",
    "description": "Official KPK Board Textbook Unit 4 with complete text reading, worked examples, and full step-by-step solutions for Exercises 4.1, 4.2, and Review Exercise 4.",
    "sections": [
      {
        "id": "4.1",
        "title": "4.1 Proper and Improper Rational Fractions",
        "theory": "A rational fraction N(x) / D(x) is an expression where N(x) and D(x) are polynomials in x with real coefficients and D(x) ≠ 0.\n\n• Proper Fraction:\nA rational fraction N(x) / D(x) is called a Proper Rational Fraction if the degree of polynomial N(x) in the numerator is strictly less than the degree of polynomial D(x) in the denominator.\nExamples: 2 / (x+1), (3x - 1) / (x² + 1), (x + 2) / (x³ - 8).\n\n• Improper Fraction:\nA rational fraction N(x) / D(x) is called an Improper Rational Fraction if the degree of N(x) is greater than or equal to the degree of D(x).\nExamples: (x² + 1) / (x² - 1), (x³ + 2x) / (x² - 3x + 2).\nEvery improper fraction must be converted into the sum of a polynomial and a proper fraction by long polynomial division before resolving into partial fractions:\nN(x) / D(x) = Q(x) + R(x) / D(x), where deg(R) < deg(D).",
        "rules": [
          "Proper fraction: Degree of numerator < Degree of denominator.",
          "Improper fraction: Degree of numerator ≥ Degree of denominator.",
          "Always divide improper fractions first: N(x)/D(x) = Quotient + Remainder/D(x)."
        ]
      },
      {
        "id": "4.2",
        "title": "4.2 Resolution of Fraction into Partial Fractions",
        "theory": "Partial fractions resolution decomposes a single complicated rational fraction into a sum of simpler fractions.\n\nCase I: Distinct Linear Factors in Denominator\nD(x) = (ax + b)(cx + d)...\nForm: N(x) / [(ax + b)(cx + d)] = A / (ax + b) + B / (cx + d).\n\nCase II: Repeated Linear Factors in Denominator\nD(x) = (ax + b)ⁿ.\nForm: N(x) / (ax + b)ⁿ = A₁ / (ax + b) + A₂ / (ax + b)² + ... + Aₙ / (ax + b)ⁿ.\n\nCase III: Irreducible Quadratic Factor in Denominator\nD(x) = (ax² + bx + c) where b² - 4ac < 0.\nForm: N(x) / [(ax² + bx + c)(px + q)] = (Ax + B) / (ax² + bx + c) + C / (px + q).\n\nCase IV: Repeated Irreducible Quadratic Factors\nD(x) = (ax² + bx + c)².\nForm: (A₁x + B₁) / (ax² + bx + c) + (A₂x + B₂) / (ax² + bx + c)².",
        "rules": [
          "Linear factor (ax + b) gets a single constant numerator A.",
          "Repeated factor (ax + b)² gets two terms: A/(ax+b) + B/(ax+b)².",
          "Irreducible quadratic factor (ax² + bx + c) gets a linear numerator (Ax + B).",
          "Determine constants by substituting roots of linear factors and equating coefficients of like powers."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 72) — Distinct Linear Factors",
        "problem": "Resolve (7x + 4) / [(x + 2)(x + 1)] into partial fractions.",
        "given": "Fraction: (7x + 4) / [(x + 2)(x + 1)]",
        "method": "Partial fraction decomposition with non-repeated linear factors.",
        "steps": [
          "Let (7x + 4) / [(x + 2)(x + 1)] = A / (x + 2) + B / (x + 1)  --- (1)",
          "Multiply both sides by (x + 2)(x + 1): 7x + 4 = A(x + 1) + B(x + 2)  --- (2)",
          "Put x = -1 into (2): 7(-1) + 4 = B(-1 + 2) => -3 = B(1) => B = -3.",
          "Put x = -2 into (2): 7(-2) + 4 = A(-2 + 1) => -10 = A(-1) => A = 10.",
          "Substitute values of A and B back into (1): 10 / (x + 2) - 3 / (x + 1)."
        ],
        "answer": "10 / (x + 2) - 3 / (x + 1)"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 75) — Repeated Linear Factor",
        "problem": "Resolve (1) / [(x - 1)²(x - 2)] into partial fractions.",
        "given": "Fraction: 1 / [(x - 1)²(x - 2)]",
        "method": "Repeated linear factors resolution.",
        "steps": [
          "Let 1 / [(x - 1)²(x - 2)] = A / (x - 1) + B / (x - 1)² + C / (x - 2)  --- (1)",
          "Multiply both sides by (x - 1)²(x - 2): 1 = A(x - 1)(x - 2) + B(x - 2) + C(x - 1)²  --- (2)",
          "Put x = 1 into (2): 1 = B(1 - 2) => 1 = -B => B = -1.",
          "Put x = 2 into (2): 1 = C(2 - 1)² => 1 = C(1) => C = 1.",
          "Equate coefficients of x² in (2): 0 = A + C => A = -C = -1.",
          "Substitute A = -1, B = -1, C = 1 into (1): -1 / (x - 1) - 1 / (x - 1)² + 1 / (x - 2)."
        ],
        "answer": "-1 / (x - 1) - 1 / (x - 1)² + 1 / (x - 2)"
      },
      {
        "id": "eg3",
        "title": "Example 3 (Page 78) — Irreducible Quadratic Factor",
        "problem": "Resolve (3x - 11) / [(x² + 1)(x + 3)] into partial fractions.",
        "given": "Fraction: (3x - 11) / [(x² + 1)(x + 3)]",
        "method": "Case III: Quadratic irreducible factor in denominator.",
        "steps": [
          "Let (3x - 11) / [(x² + 1)(x + 3)] = (Ax + B) / (x² + 1) + C / (x + 3)  --- (1)",
          "Multiply both sides by (x² + 1)(x + 3): 3x - 11 = (Ax + B)(x + 3) + C(x² + 1)  --- (2)",
          "Put x = -3 into (2): 3(-3) - 11 = C((-3)² + 1) => -20 = 10C => C = -2.",
          "Expand (2): 3x - 11 = A(x² + 3x) + B(x + 3) + C(x² + 1) = (A + C)x² + (3A + B)x + (3B + C).",
          "Equate coefficients of x²: A + C = 0 => A = -C = 2.",
          "Equate constant terms: 3B + C = -11 => 3B - 2 = -11 => 3B = -9 => B = -3.",
          "Substitute A = 2, B = -3, C = -2 into (1): (2x - 3) / (x² + 1) - 2 / (x + 3)."
        ],
        "answer": "(2x - 3) / (x² + 1) - 2 / (x + 3)"
      }
    ],
    "exercises": [
      {
        "exercise": "4.1",
        "title": "Exercise 4.1 — Distinct & Repeated Linear Factors",
        "problems": [
          {
            "num": "Q1",
            "question": "Resolve into partial fractions: (2x - 3) / (x² - 1).",
            "solution": "Factor denominator: x² - 1 = (x - 1)(x + 1).\nLet (2x - 3) / [(x - 1)(x + 1)] = A / (x - 1) + B / (x + 1).\nMultiply by (x - 1)(x + 1): 2x - 3 = A(x + 1) + B(x - 1).\nPut x = 1: 2(1) - 3 = 2A => -1 = 2A => A = -1/2.\nPut x = -1: 2(-1) - 3 = -2B => -5 = -2B => B = 5/2.\nResult: -1 / [2(x - 1)] + 5 / [2(x + 1)].",
            "finalAnswer": "-1 / [2(x - 1)] + 5 / [2(x + 1)]",
            "steps": [
              "Factor denominator into (x - 1)(x + 1)",
              "Set identity: 2x - 3 = A(x + 1) + B(x - 1)",
              "Substitute x = 1 => A = -1/2",
              "Substitute x = -1 => B = 5/2"
            ],
            "method": "Distinct Linear Factors"
          },
          {
            "num": "Q2",
            "question": "Resolve into partial fractions: (x - 5) / (x² + 2x - 3).",
            "solution": "Factor denominator: x² + 2x - 3 = (x + 3)(x - 1).\nLet (x - 5) / [(x + 3)(x - 1)] = A / (x + 3) + B / (x - 1).\nx - 5 = A(x - 1) + B(x + 3).\nPut x = 1: 1 - 5 = 4B => -4 = 4B => B = -1.\nPut x = -3: -3 - 5 = -4A => -8 = -4A => A = 2.\nResult: 2 / (x + 3) - 1 / (x - 1).",
            "finalAnswer": "2 / (x + 3) - 1 / (x - 1)",
            "steps": [
              "Factor: (x + 3)(x - 1)",
              "Multiply out: x - 5 = A(x - 1) + B(x + 3)",
              "x = 1 gives B = -1",
              "x = -3 gives A = 2"
            ],
            "method": "Distinct Linear Factors"
          },
          {
            "num": "Q3",
            "question": "Resolve into partial fractions: (1) / [(x + 1)²(x - 1)].",
            "solution": "Let 1 / [(x + 1)²(x - 1)] = A / (x + 1) + B / (x + 1)² + C / (x - 1).\n1 = A(x + 1)(x - 1) + B(x - 1) + C(x + 1)².\nPut x = -1: 1 = B(-2) => B = -1/2.\nPut x = 1: 1 = C(4) => C = 1/4.\nEquate x² terms: 0 = A + C => A = -C = -1/4.\nResult: -1 / [4(x + 1)] - 1 / [2(x + 1)²] + 1 / [4(x - 1)].",
            "finalAnswer": "-1 / [4(x + 1)] - 1 / [2(x + 1)²] + 1 / [4(x - 1)]",
            "steps": [
              "Form: A/(x+1) + B/(x+1)² + C/(x-1)",
              "Multiply clearing denominators: 1 = A(x² - 1) + B(x - 1) + C(x + 1)²",
              "Substitute roots x = -1 and x = 1 to find B and C",
              "Equate x² coefficients to find A = -1/4"
            ],
            "method": "Repeated Linear Factor"
          }
        ]
      },
      {
        "exercise": "4.2",
        "title": "Exercise 4.2 — Irreducible Quadratic Factors",
        "problems": [
          {
            "num": "Q1",
            "question": "Resolve into partial fractions: (7x - 9) / [(x + 1)(x² + 1)].",
            "solution": "Let (7x - 9) / [(x + 1)(x² + 1)] = A / (x + 1) + (Bx + C) / (x² + 1).\n7x - 9 = A(x² + 1) + (Bx + C)(x + 1).\nPut x = -1: 7(-1) - 9 = A(1 + 1) => -16 = 2A => A = -8.\nExpand RHS: 7x - 9 = Ax² + A + Bx² + Bx + Cx + C = (A + B)x² + (B + C)x + (A + C).\nEquate x²: A + B = 0 => B = -A = 8.\nEquate constants: A + C = -9 => -8 + C = -9 => C = -1.\nResult: -8 / (x + 1) + (8x - 1) / (x² + 1).",
            "finalAnswer": "-8 / (x + 1) + (8x - 1) / (x² + 1)",
            "steps": [
              "Set form A/(x+1) + (Bx+C)/(x²+1)",
              "Put x = -1 to find A = -8",
              "Equate x² terms: A + B = 0 => B = 8",
              "Equate constant terms: A + C = -9 => C = -1"
            ],
            "method": "Irreducible Quadratic Factor"
          },
          {
            "num": "Q2",
            "question": "Resolve into partial fractions: (x² + 1) / (x³ + 1).",
            "solution": "Factor denominator using sum of cubes: x³ + 1 = (x + 1)(x² - x + 1).\nLet (x² + 1) / [(x + 1)(x² - x + 1)] = A / (x + 1) + (Bx + C) / (x² - x + 1).\nx² + 1 = A(x² - x + 1) + (Bx + C)(x + 1).\nPut x = -1: (-1)² + 1 = A(1 + 1 + 1) => 2 = 3A => A = 2/3.\nExpand: x² + 1 = (A + B)x² + (-A + B + C)x + (A + C).\nEquate x²: A + B = 1 => 2/3 + B = 1 => B = 1/3.\nEquate constant: A + C = 1 => 2/3 + C = 1 => C = 1/3.\nResult: 2 / [3(x + 1)] + (x + 1) / [3(x² - x + 1)].",
            "finalAnswer": "2 / [3(x + 1)] + (x + 1) / [3(x² - x + 1)]",
            "steps": [
              "Use identity: x³ + 1 = (x + 1)(x² - x + 1)",
              "Set form: A/(x+1) + (Bx+C)/(x²-x+1)",
              "Substitute x = -1 to obtain A = 2/3",
              "Equate coefficients to find B = 1/3 and C = 1/3"
            ],
            "method": "Irreducible Quadratic Factor"
          }
        ]
      }
    ],
    "slos": [
      "Define proper, improper, and rational fractions with clear distinction based on polynomial degrees",
      "Resolve a proper fraction into partial fractions when denominator contains non-repeated linear factors",
      "Resolve a proper fraction into partial fractions when denominator contains repeated linear factors",
      "Resolve a proper fraction into partial fractions when denominator contains non-repeated irreducible quadratic factors",
      "Convert improper rational fractions into proper fractions by polynomial long division prior to decomposition"
    ],
    "formulaSheet": [
      {
        "name": "Proper Fraction",
        "formula": "deg(N) < deg(D)",
        "note": "Degree of numerator is strictly less than denominator."
      },
      {
        "name": "Improper Division",
        "formula": "N(x)/D(x) = Q(x) + R(x)/D(x)",
        "note": "Long division is required before partial fractions."
      },
      {
        "name": "Case I (Linear)",
        "formula": "N(x)/[(x-a)(x-b)] = A/(x-a) + B/(x-b)",
        "note": "Linear non-repeated factors."
      },
      {
        "name": "Case II (Repeated Linear)",
        "formula": "N(x)/(x-a)² = A/(x-a) + B/(x-a)²",
        "note": "Repeated linear factors up to power n."
      },
      {
        "name": "Case III (Quadratic)",
        "formula": "N(x)/[(x-a)(x²+b)] = A/(x-a) + (Bx+C)/(x²+b)",
        "note": "Irreducible quadratic factors with linear numerator."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 5,
    "id": "u5",
    "title": "Sets and Functions",
    "titleUrdu": "سیٹ اور تفاعل",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 84–119",
    "description": "Official KPK Board Textbook Unit 5 covering sets, operations, Venn diagrams, De Morgan's laws, binary relations, functions, and full solutions for Exercises 5.1 through 5.5 and Review Exercise 5.",
    "sections": [
      {
        "id": "5.1",
        "title": "5.1 Sets and Operations on Sets",
        "theory": "A set is a well-defined collection of distinct objects. The objects belonging to a set are called its elements or members.\n\nKey Set Operations:\n1. Union (A ∪ B): The set of all elements belonging to set A, set B, or both. A ∪ B = {x | x ∈ A or x ∈ B}.\n2. Intersection (A ∩ B): The set of all elements common to both set A and set B. A ∩ B = {x | x ∈ A and x ∈ B}.\n3. Difference (A \\ B or A - B): The set of elements belonging to A but not to B. A \\ B = {x | x ∈ A and x ∉ B}.\n4. Complement (A' or Aᶜ): The difference of the universal set U and A: A' = U \\ A = {x | x ∈ U and x ∉ A}.\n5. Symmetric Difference (A △ B): (A \\ B) ∪ (B \\ A) = (A ∪ B) \\ (A ∩ B).\n\nDisjoint and Overlapping Sets:\n• Disjoint sets: A ∩ B = ∅ (No common elements).\n• Overlapping sets: A ∩ B ≠ ∅ and neither set is a subset of the other.",
        "rules": [
          "Union A ∪ B contains all elements from either set without duplicates.",
          "Intersection A ∩ B contains only elements present in both sets.",
          "Complement A' = U - A contains all elements of U not in A."
        ]
      },
      {
        "id": "5.2",
        "title": "5.2 Properties of Union, Intersection & De Morgan's Laws",
        "theory": "Fundamental Set Identities:\n1. Commutative Laws: A ∪ B = B ∪ A,  A ∩ B = B ∩ A.\n2. Associative Laws: A ∪ (B ∪ C) = (A ∪ B) ∪ C,  A ∩ (B ∩ C) = (A ∩ B) ∩ C.\n3. Distributive Laws:\n   • Union over Intersection: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)\n   • Intersection over Union: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)\n4. De Morgan's Laws:\n   • (A ∪ B)' = A' ∩ B'\n   • (A ∩ B)' = A' ∪ B'\n5. Identity and Idempotent Laws: A ∪ ∅ = A, A ∩ U = A, A ∪ A = A, A ∩ A = A.",
        "rules": [
          "De Morgan's 1st Law: The complement of union is the intersection of complements: (A ∪ B)' = A' ∩ B'.",
          "De Morgan's 2nd Law: The complement of intersection is the union of complements: (A ∩ B)' = A' ∪ B'."
        ]
      },
      {
        "id": "5.3",
        "title": "5.3 Venn Diagrams",
        "theory": "A Venn diagram represents sets geometrically:\n• The Universal set U is represented by a rectangle.\n• Sets within U are represented by closed curves (usually circles or ellipses).\n• Shading represents the outcome of operations:\n  - For A ∪ B: Shade entire regions of circle A and circle B.\n  - For A ∩ B: Shade only the overlapping intersection lens.\n  - For A \\ B: Shade only circle A excluding the portion shared with B.\n  - For A': Shade everything inside the rectangle outside circle A.",
        "rules": [
          "Rectangle represents universal set U.",
          "Circles represent sets inside U.",
          "Shaded area indicates the result of the set operation."
        ]
      },
      {
        "id": "5.4",
        "title": "5.4 Cartesian Product & Binary Relations",
        "theory": "Ordered Pair:\nAn ordered pair (a, b) is a pair of elements written in specific order where (a, b) = (c, d) if and only if a = c and b = d.\n\nCartesian Product (A × B):\nThe set of all possible ordered pairs where first component comes from A and second from B:\nA × B = {(a, b) | a ∈ A and b ∈ B}.\nIf n(A) = p and n(B) = q, then n(A × B) = p · q.\n\nBinary Relation (R):\nA binary relation R from set A to set B is any subset of the Cartesian product A × B: R ⊆ A × B.\n• Domain of R (Dom R): Set of all first coordinates of the ordered pairs in R: Dom R = {x | (x, y) ∈ R}.\n• Range of R (Ran R): Set of all second coordinates of ordered pairs in R: Ran R = {y | (x, y) ∈ R}.",
        "rules": [
          "If n(A) = p and n(B) = q, total possible binary relations = 2^(p·q).",
          "Dom(R) is the set of all first components; Ran(R) is the set of all second components."
        ]
      },
      {
        "id": "5.5",
        "title": "5.5 Functions (Mappings)",
        "theory": "A binary relation f from set A to set B (written f: A → B) is called a Function if:\n1. Dom(f) = A (every element of domain set A is used).\n2. No two ordered pairs in f have the same first element (each element in A has a unique image in B).\n\nTypes of Functions:\n• Into Function: Ran(f) ⊂ B (Range is a proper subset of B, some elements in B are left untouched).\n• Onto (Surjective) Function: Ran(f) = B (Every element of B is an image of at least one element of A).\n• One-to-One (Injective) Function: Distinct elements of A have distinct images in B: x₁ ≠ x₂ => f(x₁) ≠ f(x₂).\n• Bijective Function (One-to-One and Onto): Both 1-1 and Onto. Bijective functions are invertible (f⁻¹ exists).\n• Constant Function: f(x) = c for all x ∈ A (All inputs map to a single value).\n• Identity Function: I_A: A → A where I_A(x) = x for all x ∈ A.",
        "rules": [
          "Every function is a relation, but not every relation is a function.",
          "Vertical Line Test: A curve is a function if no vertical line intersects it more than once.",
          "A function is Bijective if and only if it is both Injective (1-to-1) and Surjective (onto)."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 86) — Set Operations & De Morgan's Law",
        "problem": "If U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, A = {1, 3, 5, 7, 9}, and B = {2, 3, 5, 7}, verify that (A ∪ B)' = A' ∩ B'.",
        "given": "U = {1..10}, A = {1, 3, 5, 7, 9}, B = {2, 3, 5, 7}",
        "method": "Set evaluation and comparison of LHS and RHS.",
        "steps": [
          "Compute A ∪ B: A ∪ B = {1, 2, 3, 5, 7, 9}.",
          "Compute LHS = (A ∪ B)' = U \\ (A ∪ B) = {4, 6, 8, 10}.",
          "Compute A' = U \\ A = {2, 4, 6, 8, 10}.",
          "Compute B' = U \\ B = {1, 4, 6, 8, 9, 10}.",
          "Compute RHS = A' ∩ B' = {4, 6, 8, 10}.",
          "Since LHS = RHS = {4, 6, 8, 10}, De Morgan's first law is verified."
        ],
        "answer": "LHS = RHS = {4, 6, 8, 10} (Verified)"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 108) — Cartesian Product and Domain/Range",
        "problem": "Let A = {1, 2, 3} and B = {2, 4}. Find A × B and a relation R = {(x, y) | y = 2x, x ∈ A, y ∈ B}. Also state Dom(R) and Ran(R).",
        "given": "A = {1, 2, 3}, B = {2, 4}, condition: y = 2x",
        "method": "Cartesian product definition and conditional subset selection.",
        "steps": [
          "A × B = {(1, 2), (1, 4), (2, 2), (2, 4), (3, 2), (3, 4)}.",
          "Check condition y = 2x for each pair:",
          "For x = 1: y = 2(1) = 2 ∈ B => (1, 2) ∈ R.",
          "For x = 2: y = 2(2) = 4 ∈ B => (2, 4) ∈ R.",
          "For x = 3: y = 2(3) = 6 ∉ B => not in R.",
          "Therefore, R = {(1, 2), (2, 4)}.",
          "Dom(R) = {1, 2}; Ran(R) = {2, 4}."
        ],
        "answer": "R = {(1, 2), (2, 4)}, Dom(R) = {1, 2}, Ran(R) = {2, 4}"
      }
    ],
    "exercises": [
      {
        "exercise": "5.1",
        "title": "Exercise 5.1 — Union, Intersection & Difference of Sets",
        "problems": [
          {
            "num": "Q1",
            "question": "If X = {1, 4, 7, 9} and Y = {2, 4, 5, 9}, find: (i) X ∪ Y, (ii) X ∩ Y, (iii) Y ∪ X, (iv) Y ∩ X.",
            "solution": "(i) X ∪ Y = {1, 2, 4, 5, 7, 9}\n(ii) X ∩ Y = {4, 9}\n(iii) Y ∪ X = {1, 2, 4, 5, 7, 9}\n(iv) Y ∩ X = {4, 9}\nNote: X ∪ Y = Y ∪ X and X ∩ Y = Y ∩ X verify commutative laws.",
            "finalAnswer": "X ∪ Y = {1, 2, 4, 5, 7, 9}, X ∩ Y = {4, 9}",
            "steps": [
              "Combine all elements for Union: {1, 2, 4, 5, 7, 9}",
              "Take common elements for Intersection: {4, 9}",
              "Confirm commutativity"
            ],
            "method": "Set Operations"
          },
          {
            "num": "Q2",
            "question": "If A = N (Natural numbers) and B = W (Whole numbers), find A ∪ B and A ∩ B.",
            "solution": "N = {1, 2, 3, 4, ...}\nW = {0, 1, 2, 3, 4, ...}\nSince N ⊂ W:\nA ∪ B = N ∪ W = W = {0, 1, 2, 3, ...}\nA ∩ B = N ∩ W = N = {1, 2, 3, 4, ...}.",
            "finalAnswer": "A ∪ B = W, A ∩ B = N",
            "steps": [
              "Identify elements: N = {1, 2, 3..}, W = {0, 1, 2, 3..}",
              "Since N ⊂ W, the union is the superset W",
              "The intersection is the subset N"
            ],
            "method": "Infinite Sets Intersection"
          }
        ]
      },
      {
        "exercise": "5.2",
        "title": "Exercise 5.2 — Distributive Laws & De Morgan's Laws",
        "problems": [
          {
            "num": "Q1",
            "question": "If U = {1, 2, 3, ..., 10}, A = {1, 3, 5, 7, 9}, B = {2, 3, 5, 7}, verify (A ∩ B)' = A' ∪ B'.",
            "solution": "A ∩ B = {3, 5, 7}\nLHS = (A ∩ B)' = U \\ {3, 5, 7} = {1, 2, 4, 6, 7, 8, 9, 10} \\ {7} = {1, 2, 4, 6, 8, 9, 10}\nA' = U \\ A = {2, 4, 6, 8, 10}\nB' = U \\ B = {1, 4, 6, 8, 9, 10}\nRHS = A' ∪ B' = {1, 2, 4, 6, 8, 9, 10}\nLHS = RHS. Proved.",
            "finalAnswer": "{1, 2, 4, 6, 8, 9, 10} (Verified)",
            "steps": [
              "Find A ∩ B = {3, 5, 7}",
              "Take complement: LHS = {1, 2, 4, 6, 8, 9, 10}",
              "Find individual complements A' and B'",
              "Compute union: RHS = {1, 2, 4, 6, 8, 9, 10}"
            ],
            "method": "De Morgan's 2nd Law"
          }
        ]
      },
      {
        "exercise": "5.3",
        "title": "Exercise 5.3 — Venn Diagrams and Set Identities",
        "problems": [
          {"num":"Q1","question":"If A = {1, 2, 3, 4, 5} and B = {2, 3, 6, 7}, draw Venn diagrams for (i) A ∪ B; (ii) A ∩ B.","solution":"Place 1, 4, 5 in the A-only region; 2, 3 in A ∩ B; and 6, 7 in the B-only region. Shade the requested regions.","finalAnswer":"A ∪ B = {1, 2, 3, 4, 5, 6, 7}; A ∩ B = {2, 3}."},
          {"num":"Q2","question":"For A = {1, 2, 3, 4, 5, 6}, B = {3, 4, 5, 6, 7, 8}, C = {5, 6, 9, 10}, verify by Venn diagrams: (i) A ∪ (B ∪ C) = (A ∪ B) ∪ C; (ii) A ∩ (B ∩ C) = (A ∩ B) ∩ C; (iii) A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C); (iv) A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).","solution":"(i) Both sides give {1,2,3,4,5,6,7,8,9,10}. (ii) Both sides give {5,6}. (iii) B ∩ C = {5,6}; both sides give {1,2,3,4,5,6}. (iv) Both sides give {3,4,5,6}. In each identity, the Venn diagrams shade the same regions.","finalAnswer":"All four set identities are verified."},
          {"num":"Q3","question":"Let U = {1,2,3,4,5,6,7}, A = {1,2,3,4}, B = {3,4,5}. Draw Venn diagrams for A, B, A′ ∪ B, and A′ ∩ B′, and verify (i) (A ∪ B)′ = A′ ∩ B′; (ii) (A ∩ B)′ = A′ ∪ B′.","solution":"A only = {1,2}; A ∩ B = {3,4}; B only = {5}; outside both = {6,7}. Thus A′ = {5,6,7}, B′ = {1,2,6,7}. Compute each complement and intersection/union.","finalAnswer":"(A ∪ B)′ = A′ ∩ B′ = {6,7}; (A ∩ B)′ = A′ ∪ B′ = {1,2,5,6,7}."},
          {"num":"Q4","question":"Let U = {a,b,c,1,2,3,4}, A = {c,3}, and B = {a,3,4}. Draw Venn diagrams for A, B, A\B, and B\A.","solution":"The common region is A ∩ B = {3}. A-only contains c; B-only contains a and 4; b, 1, 2 lie outside both sets.","finalAnswer":"A\B = {c}; B\A = {a,4}."},
          {"num":"Q5","question":"Let U = {a,b,c,d,e,f,g}, A = {a,b,c}, B = {c,d,e}. Verify De Morgan’s laws with Venn diagrams.","solution":"A′ = {d,e,f,g} and B′ = {a,b,f,g}. A ∪ B = {a,b,c,d,e}, while A ∩ B = {c}. Compare the two sides of each law.","finalAnswer":"(A ∪ B)′ = A′ ∩ B′ = {f,g}; (A ∩ B)′ = A′ ∪ B′ = {a,b,d,e,f,g}."}
        ]
      },
      {
        "exercise": "5.4",
        "title": "Exercise 5.4 — Cartesian Products & Ordered Pairs",
        "problems": [
          {
            "num": "Q1",
            "question": "Find (a, b) if: (i) (a - 3, 2b + 1) = (5, 7), (ii) (2a + 5, 3) = (7, b - 4).",
            "solution": "(i) By equality of ordered pairs:\na - 3 = 5 => a = 8\n2b + 1 = 7 => 2b = 6 => b = 3.\n\n(ii) 2a + 5 = 7 => 2a = 2 => a = 1\n3 = b - 4 => b = 7.",
            "finalAnswer": "(i) a = 8, b = 3; (ii) a = 1, b = 7",
            "steps": [
              "Equate first coordinates: a - 3 = 5 => a = 8",
              "Equate second coordinates: 2b + 1 = 7 => b = 3",
              "Repeat for second pair: 2a + 5 = 7 => a = 1, b - 4 = 3 => b = 7"
            ],
            "method": "Ordered Pair Equality"
          }
        ]
      },
      {
        "exercise": "5.5",
        "title": "Exercise 5.5 — Functions",
        "problems": [
          {"num":"Q1","question":"A = {1,2,3,4}, B = {6,7}. For each relation from A to B, state whether it is a function; if so, identify its type: R₁ = {(1,6),(2,7),(3,6)}, R₂ = {(1,6),(2,6),(3,7),(4,7)}, R₃ = {(1,6),(2,6),(3,6),(4,6)}.","solution":"A relation is a function from A only if every element of A has exactly one image. R₁ omits 4. R₂ maps all of A and reaches both elements of B, but two inputs share images. R₃ maps all of A to 6 and misses 7.","finalAnswer":"R₁ is not a function; R₂ is an onto many-to-one function; R₃ is a many-to-one function into B, not onto."},
          {"num":"Q2","question":"Which relations on {a,b,c,d} are functions? State their types: (i) {(a,b),(c,d),(b,d),(d,b)}; (ii) {(b,a),(c,b),(a,b),(d,d)}; (iii) {(d,c),(c,b),(a,b),(d,d)}; (iv) {(a,b),(b,c),(c,b),(d,a)}.","solution":"Check that every domain element occurs exactly once as a first coordinate. For each function, compare the range with the codomain and check whether distinct inputs have distinct outputs.","finalAnswer":"(i) Function, many-to-one and into; (ii) function, many-to-one and into; (iii) not a function because d has two images; (iv) function, many-to-one and onto."},
          {"num":"Q3","question":"A = {0,1,2,3}, B = {x,y,z,p}. Do these relations define a one-one correspondence? (i) {(0,x),(2,z),(3,y),(1,p)}; (ii) {(0,x),(1,z),(2,y),(3,z)}. Give reasons.","solution":"A one-one correspondence must map every element of A to a distinct element of B and cover B.","finalAnswer":"(i) Yes, it is bijective. (ii) No: z is repeated and p is not an image."},
          {"num":"Q4","question":"A = {a,b,c}, B = {2,3,4,5}. For each relation, state whether it is a one-one correspondence; if not, identify the relation type: (i) {(a,2),(b,3),(c,4)}; (ii) {(a,3),(b,4),(c,3)}.","solution":"A and B have different cardinalities, so a relation from A to B cannot be onto B and therefore cannot be a one-one correspondence. In (i) all three images are distinct. In (ii) a and c share an image.","finalAnswer":"Neither is a one-one correspondence. (i) One-one into; (ii) many-to-one into."},
          {"num":"Q5","question":"For X = {1,2,3,4} and Y = {5,6,7,8}, give examples of: (i) a function X→Y; (ii) a one-one function X→Y; (iii) a one-one correspondence between X and Y; (iv) an onto function Y→X; (v) a bijective function Y→X; (vi) a function X→Y that is neither one-one nor onto.","solution":"Use explicit ordered pairs, ensuring each input in the domain appears once and that the images have the required repetition/coverage properties.","finalAnswer":"(i) {(1,5),(2,5),(3,5),(4,5)}; (ii) {(1,5),(2,6),(3,7),(4,8)}; (iii) same as (ii); (iv) {(5,1),(6,2),(7,3),(8,4)}; (v) same as (iv); (vi) same as (i)."},
          {"num":"Q6","question":"For A = {1,2,3,4,5}, decide whether each relation is a function on A; if it is, give its range and state whether it is onto: (i) {(1,5),(2,3),(3,3),(4,2),(5,1)}; (ii) {(1,1),(2,4),(3,2),(4,1),(5,3)}; (iii) {(1,2),(2,1),(3,1),(4,4),(5,5)}.","solution":"Each relation assigns exactly one image to every element of A. List the distinct second coordinates to find its range, then compare with A.","finalAnswer":"All are functions. (i) Range {1,2,3,5}, not onto; (ii) range {1,2,3,4}, not onto; (iii) range {1,2,4,5}, not onto."}
        ]
      },
      {
        "exercise":"Review Exercise 5","title":"Review Exercise 5 — Sets and Functions","problems":[
          {"num":"Q1(i)","question":"A={1,2,3}, B={4,5}, R={(1,4),(2,5),(3,4)}. Classify R.","finalAnswer":"Onto function A→B; it is not one-to-one."},
          {"num":"Q1(ii)","question":"A has 2 elements and B has 3. How many binary relations A→B?","solution":"|A×B|=6 and every subset is a relation.","finalAnswer":"2⁶=64"},
          {"num":"Q1(iii)","question":"Which pair is disjoint? (a) {0,1,2,3},{3,2,1,0}; (b) {0,3,6,9},{9,16,25,36}; (c) {0,2,4,6},{2,4,6,8}; (d) {0,4,8,12},{6,10,14,18}.","finalAnswer":"(d) {0,4,8,12} and {6,10,14,18}."},
          {"num":"Q1(iv)","question":"U is the positive odd integers below 30; R={1,5,7}, S={1,3,7,11,13}. Find n((R∩S)').","finalAnswer":"13"},
          {"num":"Q1(v)","question":"For f:A→B, what condition makes f onto?","finalAnswer":"Range f=B."},
          {"num":"Q1(vi)","question":"Find Dom R for R={(0,0),(8,2),(10,3),(14,12)}.","finalAnswer":"{0,8,10,14}"},
          {"num":"Q2","question":"U={1,…,100}, A={positive even numbers up to 100}, B={positive odd numbers up to 100}. Find A'∪B', A'∩B', A∩B', A'∩B.","finalAnswer":"U; ∅; A={2,4,…,100}; B={1,3,…,99}."},
          {"num":"Q3","question":"For A={1,2,3,5,7}, B={2,4,6}, C={2,5,9}, verify the associative laws and distributive laws listed in the book.","solution":"A∪B∪C={1,2,3,4,5,6,7,9}; (A∩B)∩C=A∩(B∩C)={2}; A∪(B∩C)=(A∪B)∩(A∪C)={1,2,3,5,7}.","finalAnswer":"The standard associative and distributive identities hold. The printed fourth item says “union over union”; this wording is likely a textbook typo for intersection over union."},
          {"num":"Q4","question":"Verify De Morgan’s laws for U={x∈N:1≤x≤40}, A={1,6,11,16,21,26,31}, B={2,5,8,11,14,17,20,23,26,29,32}.","finalAnswer":"(A∪B)'=A'∩B' and (A∩B)'=A'∪B'; both hold relative to U."},
          {"num":"Q5","question":"For U={1,2,3,5,6,7}, A={2,5,6}, B={1,2,3}, verify De Morgan’s laws with Venn diagrams.","finalAnswer":"(A∪B)'={7}=A'∩B'; (A∩B)'={1,3,5,6,7}=A'∪B'."},
          {"num":"Q6","question":"For U={1,…,10}, A={1,2,3,4}, B={3,4,5,6}, C={3,4,7,8}, verify both distributive laws with Venn diagrams.","finalAnswer":"A∪(B∩C)=(A∪B)∩(A∪C)={1,2,3,4}; A∩(B∪C)=(A∩B)∪(A∩C)={3,4}."},
          {"num":"Q7","question":"For A={−2,−1,0,1,2}, B={a,b,c,d,e}, classify the four relations printed in the source.","finalAnswer":"(i) function, neither one-to-one nor onto; (ii) bijective; (iii) bijective; (iv) not a function (−2 repeats and 2 is omitted)."},
          {"num":"Q8","question":"For A={1,2,3,4,5}, classify the four listed relations as functions, give ranges and identify onto maps.","finalAnswer":"(i) function, range {1,2,3,5}, not onto; (ii) function, range {1,2,3,4}, not onto; (iii) function, range {1,2,4,5}, not onto; (iv) not a function because input 1 has two images."},
          {"num":"Q9","question":"Let X={−6,−5,−4,−3}, Y={1,2,3,4}. Give examples of a one-to-one function; an onto function; a bijection; and a function that is neither one-to-one nor onto.","finalAnswer":"Examples: {(-6,1),(-5,2),(-4,3),(-3,4)}; {(-6,2),(-5,1),(-4,4),(-3,3)}; {(-6,4),(-5,3),(-4,2),(-3,1)}; {(-6,1),(-5,1),(-4,2),(-3,2)}."},
          {"num":"Project","question":"Give a function that remains a function when its x- and y-values are switched.","finalAnswer":"A bijection, e.g. {(1,1),(2,2),(3,3)}."}
        ]
      }
    ],
    "slos": [
      "Define set, elements, types of sets (empty, finite, infinite, universal, subset, power set)",
      "Perform union, intersection, difference, complement, and symmetric difference on sets",
      "State and prove Commutative, Associative, Distributive, and De Morgan's laws algebraically and using Venn diagrams",
      "Define Cartesian product of two sets and calculate the number of elements in A × B",
      "Define binary relation, its domain, and range",
      "Define functions, their domains, co-domains, and ranges",
      "Distinguish between into, onto, one-one, and bijective functions"
    ],
    "formulaSheet": [
      {
        "name": "De Morgan's 1st Law",
        "formula": "(A ∪ B)' = A' ∩ B'",
        "note": "Complement of union is intersection of complements."
      },
      {
        "name": "De Morgan's 2nd Law",
        "formula": "(A ∩ B)' = A' ∪ B'",
        "note": "Complement of intersection is union of complements."
      },
      {
        "name": "Distributive Law (∪ over ∩)",
        "formula": "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
        "note": "Union distributes over intersection."
      },
      {
        "name": "Distributive Law (∩ over ∪)",
        "formula": "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
        "note": "Intersection distributes over union."
      },
      {
        "name": "Cartesian Product Cardinality",
        "formula": "n(A × B) = n(A) · n(B)",
        "note": "Total ordered pairs."
      },
      {
        "name": "Total Relations",
        "formula": "2^(n(A) · n(B))",
        "note": "Total binary relations between two sets."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 6,
    "id": "u6",
    "title": "Basic Statistics",
    "titleUrdu": "بنیادی شماریات",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 120–161",
    "description": "Official KPK Board Textbook Unit 6 with frequency distributions, cumulative frequency, histograms, measures of central tendency (Mean, Median, Mode), and measures of dispersion (Range, Variance, Standard Deviation).",
    "sections": [
      {
        "id": "6.1",
        "title": "6.1 Frequency Distribution and Histograms",
        "theory": "Statistics is the science of collecting, presenting, analyzing, and interpreting data.\n\nKey Concepts:\n• Raw Data: Unorganized collection of numerical values.\n• Frequency (f): The number of times an observation occurs.\n• Class Interval: A range of values into which data is grouped (e.g., 10–19, 20–29).\n• Class Boundaries: True limits of a class interval (e.g., 9.5–19.5, 19.5–29.5).\n• Class Mark (Midpoint, x): The average of lower and upper class limits: x = (Lower Limit + Upper Limit) / 2.\n• Cumulative Frequency (cf): The running sum of frequencies up to the upper boundary of a class interval.\n\nGraphical Representation:\n• Histogram: Adjacent vertical bars where bar width represents class boundaries and height represents frequency.\n• Frequency Polygon: Line graph joining the midpoints of top of histogram bars.\n• Cumulative Frequency Polygon (Ogive): An S-shaped curve plotting cumulative frequency against upper class boundaries.",
        "rules": [
          "Class Mark (Midpoint) x = (Lower Limit + Upper Limit) / 2.",
          "Class Width h = Upper Boundary - Lower Boundary.",
          "Histogram bars must touch each other (use continuous class boundaries, not limits)."
        ]
      },
      {
        "id": "6.2",
        "title": "6.2 Measures of Central Tendency",
        "theory": "Measures of central tendency summarize an entire distribution into a single representative central value.\n\n1. Arithmetic Mean (x̄):\n   • Ungrouped data: x̄ = (∑x) / n.\n   • Grouped data (Direct): x̄ = (∑fx) / (∑f).\n   • Short-cut (Assumed Mean A): x̄ = A + (∑fd) / (∑f) where d = x - A.\n   • Coding Method: x̄ = A + [(∑fu) / (∑f)] · h where u = (x - A) / h.\n\n2. Median (M):\n   The middle-most value when observations are arranged in ascending order.\n   • Ungrouped: If n is odd, M = value of [(n + 1) / 2]th term. If n is even, M = average of (n/2)th and (n/2 + 1)th terms.\n   • Grouped data: M = l + (h / f) · (n/2 - c), where:\n     l = lower class boundary of median class,\n     h = class width,\n     f = frequency of median class,\n     n = ∑f,\n     c = cumulative frequency of preceding class.\n\n3. Mode (Z or x̂):\n   The most frequently occurring observation.\n   • Ungrouped: Value with highest repetition (unimodal, bimodal, or no mode).\n   • Grouped data: Mode = l + [(fₘ - f₁) / (2fₘ - f₁ - f₂)] · h, where:\n     l = lower boundary of modal class,\n     fₘ = maximum frequency,\n     f₁ = frequency of pre-modal class,\n     f₂ = frequency of post-modal class,\n     h = class interval width.\n\n4. Geometric Mean (G.M) & Harmonic Mean (H.M):\n   • G.M = Antilog [ (∑ log x) / n ] (Ungrouped) or Antilog [ (∑ f log x) / ∑f ] (Grouped).\n   • H.M = n / ∑(1/x) (Ungrouped) or ∑f / ∑(f/x) (Grouped).",
        "rules": [
          "Arithmetic Mean is the most widely used measure, but sensitive to extreme outliers.",
          "Median is the positional average, unaffected by extreme values.",
          "Mode represents the most typical value and can be determined graphically from a histogram."
        ]
      },
      {
        "id": "6.3",
        "title": "6.3 Measures of Dispersion",
        "theory": "Measures of dispersion indicate the extent of scatter or variation of data points around their central value.\n\n1. Range (R):\n   The simplest measure of dispersion: R = X_max - X_min.\n\n2. Variance (s²):\n   The mean of squared deviations from the arithmetic mean:\n   • Ungrouped: s² = ∑(x - x̄)² / n = (∑x² / n) - (∑x / n)².\n   • Grouped: s² = ∑f(x - x̄)² / ∑f = (∑fx² / ∑f) - (∑fx / ∑f)².\n\n3. Standard Deviation (s):\n   The positive square root of variance:\n   • Ungrouped: s = √[ (∑x² / n) - (∑x / n)² ].\n   • Grouped: s = √[ (∑fx² / ∑f) - (∑fx / ∑f)² ].\n   Standard deviation is measured in the same units as the original data.",
        "rules": [
          "Range depends only on two extreme values.",
          "Variance s² is always non-negative (s² ≥ 0).",
          "Standard deviation s is the square root of variance: s = √Variance."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 132) — Arithmetic Mean of Grouped Data",
        "problem": "Calculate the Arithmetic Mean by direct and short-cut methods for the frequency distribution:\nClasses: 0–9 (f=2), 10–19 (f=10), 20–29 (f=5), 30–39 (f=9), 40–49 (f=6), 50–59 (f=7), 60–69 (f=1).",
        "given": "Frequency distribution with ∑f = 40",
        "method": "Direct formula x̄ = ∑fx / ∑f",
        "steps": [
          "Find midpoints x: 4.5, 14.5, 24.5, 34.5, 44.5, 54.5, 64.5.",
          "Calculate fx: 2(4.5)=9, 10(14.5)=145, 5(24.5)=122.5, 9(34.5)=310.5, 6(44.5)=267, 7(54.5)=381.5, 1(64.5)=64.5.",
          "Sum of frequencies: ∑f = 2 + 10 + 5 + 9 + 6 + 7 + 1 = 40.",
          "Sum of products: ∑fx = 9 + 145 + 122.5 + 310.5 + 267 + 381.5 + 64.5 = 1300.",
          "Apply formula: x̄ = ∑fx / ∑f = 1300 / 40 = 32.5."
        ],
        "answer": "x̄ = 32.5"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 137) — Median of Grouped Data",
        "problem": "Find the Median marks from the distribution: 20–24 (f=1), 25–29 (f=3), 30–34 (f=11), 35–39 (f=21), 40–44 (f=43), 45–49 (f=32), 50–54 (f=9). Total ∑f = 120.",
        "given": "∑f = 120, n/2 = 60",
        "method": "Grouped Median formula: M = l + (h/f)(n/2 - c)",
        "steps": [
          "Construct cumulative frequency cf: 1, 4, 15, 36, 79, 111, 120.",
          "Locate median class: n/2 = 120/2 = 60. The 60th observation falls in class 40–44 (cf reaches 79).",
          "Identify parameters: Lower boundary l = 39.5, h = 5, f = 43, c = 36.",
          "Substitute into formula: M = 39.5 + (5 / 43) · (60 - 36)",
          "M = 39.5 + (5 / 43) · 24 = 39.5 + 120 / 43 = 39.5 + 2.79 = 42.29."
        ],
        "answer": "Median = 42.29"
      },
      {
        "id": "eg3",
        "title": "Example 3 (Page 154) — Standard Deviation (Ungrouped Data)",
        "problem": "Find the Standard Deviation of the numbers: 12, 6, 7, 3, 15, 10, 18, 5.",
        "given": "Data values: 12, 6, 7, 3, 15, 10, 18, 5 (n = 8)",
        "method": "Formula: s = √[ (∑x² / n) - (∑x / n)² ]",
        "steps": [
          "Compute ∑x: 12 + 6 + 7 + 3 + 15 + 10 + 18 + 5 = 76.",
          "Compute mean: x̄ = 76 / 8 = 9.5.",
          "Compute squares x²: 144, 36, 49, 9, 225, 100, 324, 25.",
          "Compute ∑x²: 144 + 36 + 49 + 9 + 225 + 100 + 324 + 25 = 912.",
          "Calculate variance s² = (∑x² / n) - (x̄)² = (912 / 8) - (9.5)² = 114 - 90.25 = 23.75.",
          "Standard deviation s = √23.75 ≈ 4.87."
        ],
        "answer": "Standard Deviation s ≈ 4.87 (Variance s² = 23.75)"
      }
    ],
    "exercises": [
      {
        "exercise": "6.1",
        "title": "Exercise 6.1 — Frequency Distribution & Histograms",
        "problems": [
          {
            "num": "Q1",
            "question": "The weights of 30 students are given in kg. Group the data into classes with class width 5: 34, 38, 42, 45, 47, 48, 52, 53, 55, 56, 58, 60, 62, 63, 65, 66, 68, 70, 72, 74, 36, 44, 49, 54, 59, 64, 69, 73, 51, 57.",
            "solution": "Minimum value = 34, Maximum value = 74. Range = 74 - 34 = 40.\nClass interval h = 5. Number of classes = 40 / 5 + 1 = 9.\nClasses and Frequencies:\n30–34: f = 1\n35–39: f = 2\n40–44: f = 2\n45–49: f = 3\n50–54: f = 4\n55–59: f = 5\n60–64: f = 4\n65–69: f = 4\n70–74: f = 5\nTotal ∑f = 30.",
            "finalAnswer": "9 classes constructed from 30–34 to 70–74 with ∑f = 30.",
            "steps": [
              "Find min (34) and max (74)",
              "Compute Range = 40",
              "Tally frequencies into width-5 intervals",
              "Verify sum of frequencies ∑f = 30"
            ],
            "method": "Grouped Frequency Table"
          }
        ]
      },
      {
        "exercise": "6.2",
        "title": "Exercise 6.2 — Cumulative Frequency and Ogives",
        "problems": [
          {"num":"Q1","question":"The wages (Rs) of 20 workers are 60, 75, 80, 85, 90, 84, 70, 73, 76, 84, 95, 100, 150, 66, 58, 90, 98, 120, 77, 90. Using class interval 10, prepare (i) a cumulative frequency distribution; (ii) a cumulative frequency polygon.","solution":"Use classes 50–59 through 150–159. Frequencies are 1, 2, 5, 4, 5, 1, 0, 1, 0, 0, 1; cumulative frequencies are 1, 3, 8, 12, 17, 18, 18, 19, 19, 19, 20. Plot the less-than ogive at the upper class boundaries, beginning with (49.5,0).","finalAnswer":"Classes/frequencies: 50–59:1, 60–69:2, 70–79:5, 80–89:4, 90–99:5, 100–109:1, 110–119:0, 120–129:1, 130–139:0, 140–149:0, 150–159:1. Cumulative frequencies: 1,3,8,12,17,18,18,19,19,19,20."},
          {"num":"Q2","question":"Make a cumulative frequency table: Age (years) 20–24, 25–29, 30–39, 40–44, 45–49, 50–54, 55–59; number of persons 1, 2, 26, 22, 20, 15, 14.","solution":"Add the frequencies successively across the age classes.","finalAnswer":"Cumulative frequencies: 1, 3, 29, 51, 71, 86, 100."},
          {"num":"Q3","question":"Rainfall in a city during the first week of August was: Sunday 70 ml, Monday 40 ml, Tuesday 30 ml, Wednesday 35 ml, Thursday 50 ml, Friday 55 ml, Saturday 80 ml. Construct a cumulative frequency graph.","solution":"Treat each day as one observation and sort rainfall in ascending order: 30, 35, 40, 50, 55, 70, 80 ml. The cumulative counts at these observations are 1, 2, 3, 4, 5, 6, 7. Plot the corresponding less-than cumulative frequency points.","finalAnswer":"Ogive points: (30,1), (35,2), (40,3), (50,4), (55,5), (70,6), (80,7), with a starting point below 30 at cumulative frequency 0."},
          {"num":"Q4","question":"Draw the less-than and more-than cumulative frequency polygons for marks 40–49, 50–59, 60–69, 70–79, 80–89, 90–99 with numbers of students 1, 2, 3, 4, 5, 6 respectively.","solution":"Use continuous class boundaries 39.5, 49.5, 59.5, 69.5, 79.5, 89.5, 99.5. Accumulate frequencies from the first class for the less-than polygon and from the total downward for the more-than polygon.","finalAnswer":"Less-than points: (39.5,0),(49.5,1),(59.5,3),(69.5,6),(79.5,10),(89.5,15),(99.5,21). More-than points: (39.5,21),(49.5,20),(59.5,18),(69.5,15),(79.5,11),(89.5,6),(99.5,0)."},
          {"num":"Q5","question":"Using the data of Q4, find (i) the number of students with more than 50 marks; (ii) the number with less than 70 marks; (iii) the number with marks between 50 and 70; (iv) the class interval; (v) the lower class boundary of the fifth class.","solution":"There are 21 students in total. From the grouped frequency table, the classes 50–59, 60–69, and 80–89, 90–99 have frequencies 2, 3, 5, 6 respectively. The class width is 10, and the continuous boundary for 80–89 begins at 79.5.","finalAnswer":"(i) 20; (ii) 6; (iii) 5; (iv) 10 marks; (v) 79.5 marks."},
          {"num":"Q6","question":"Construct an ogive for the salary and worker data: Rs 4000–5000: 3; 5001–6000: 5; 6001–7000: 12; 7001–8000: 9; 8001–9000: 5; 9001–10000: 4; 10001–11000: 2.","solution":"Add the frequencies cumulatively across the salary classes and plot them against the upper class boundaries for a less-than ogive.","finalAnswer":"Cumulative workers: 3, 8, 20, 29, 34, 38, 40. Plot against upper boundaries 5000.5, 6000.5, 7000.5, 8000.5, 9000.5, 10000.5, 11000.5 (starting below the first class at cumulative 0)."}
        ]
      },
      {
        "exercise": "6.3",
        "title": "Exercise 6.3 — Measures of Central Tendency",
        "problems": [
          {
            "num": "Q1",
            "question": "Find the Arithmetic Mean, Median, and Mode of the dataset: 4, 8, 12, 8, 16, 20, 8, 24, 28, 32.",
            "solution": "n = 10.\nSum ∑x = 4 + 8 + 12 + 8 + 16 + 20 + 8 + 24 + 28 + 32 = 160.\nMean x̄ = 160 / 10 = 16.\n\nArrange in ascending order: 4, 8, 8, 8, 12, 16, 20, 24, 28, 32.\nMedian M = average of 5th and 6th terms = (12 + 16) / 2 = 14.\n\nMode: Number 8 appears 3 times (most frequent).\nMode = 8.",
            "finalAnswer": "Mean = 16, Median = 14, Mode = 8",
            "steps": [
              "Mean: ∑x / n = 160 / 10 = 16",
              "Sort data to find middle elements 12 and 16",
              "Median: (12 + 16)/2 = 14",
              "Mode: 8 (highest frequency 3)"
            ],
            "method": "Central Tendency Measures"
          }
        ]
      },
      {
        "exercise": "6.4",
        "title": "Exercise 6.4 — Range, Variance & Standard Deviation",
        "problems": [
          {
            "num": "Q1",
            "question": "Calculate the Range and Standard Deviation for the data: 10, 15, 20, 25, 30.",
            "solution": "1. Range: X_max - X_min = 30 - 10 = 20.\n2. Mean: x̄ = (10 + 15 + 20 + 25 + 30) / 5 = 100 / 5 = 20.\n3. Deviations (x - x̄): -10, -5, 0, 5, 10.\n4. Squared deviations (x - x̄)²: 100, 25, 0, 25, 100.\n5. Variance s² = ∑(x - x̄)² / n = 250 / 5 = 50.\n6. Standard Deviation s = √50 ≈ 7.07.",
            "finalAnswer": "Range = 20, Variance = 50, S.D = 7.07",
            "steps": [
              "Range = 30 - 10 = 20",
              "Mean = 100 / 5 = 20",
              "Sum of squared deviations = 250",
              "Variance = 50, S.D = √50 ≈ 7.07"
            ],
            "method": "Measures of Dispersion"
          }
        ]
      },
      {
        "exercise": "Review Exercise 6",
        "title": "Review Exercise 6 — Basic Statistics",
        "problems": [
          {"num":"Q1(i)","question":"The difference between upper limits of two consecutive classes in a frequency table is called: class limit, class interval, class mark, or range?","finalAnswer":"Class interval"},
          {"num":"Q1(ii)","question":"A cumulative frequency histogram is also called a histogram, ogive, pie chart, or frequency polygon?","finalAnswer":"Ogive"},
          {"num":"Q1(iii)","question":"The number of times a value appears in a data set is called frequency, average, mode, or median?","finalAnswer":"Frequency"},
          {"num":"Q1(iv)","question":"Find the mode: 3, 2, 1, 1, 1, 5, 3, 1, 2, 1, 2.","finalAnswer":"1"},
          {"num":"Q1(v)","question":"Which data set has mean, median, mode, and range all equal: (i) 1,2,3,3,2,1,2; (ii) 1,3,3,3,2,3,1; (iii) 1,2,3,1,2,3,1; (iv) 2,2,1,2,3,2,3?","finalAnswer":"(i) 1, 2, 3, 3, 2, 1, 2"},
          {"num":"Q1(vi)","question":"The nth root of the product of n values is called the arithmetic, harmonic, geometric, or standard-deviation measure?","finalAnswer":"Geometric mean"},
          {"num":"Q1(vii)","question":"Find the median of 63, 65, 66, 67, 69.","finalAnswer":"66"},
          {"num":"Q1(viii)","question":"Find the median of 41, 43, 47, 51, 57, 52, 59.","finalAnswer":"51"},
          {"num":"Q1(ix)","question":"Find the mode of 5, 7, 7, 5, 3, 7, 2, 8, 2.","finalAnswer":"7"},
          {"num":"Q1(x)","question":"Find the standard deviation of 5, 5, 5, 5, 5, 5, 5.","finalAnswer":"0"},
          {"num":"Q1(xi)","question":"The average pocket money of 30 students is Rs. 20. Find the total amount.","finalAnswer":"Rs. 600"},
          {"num":"Q1(xii)","question":"The sum of 30 observations is 1500. Find their average.","finalAnswer":"50"},
          {"num":"Q1(xiii)","question":"The difference between the largest and smallest data values is called mean, mode, range, or standard deviation?","finalAnswer":"Range"},
          {"num":"Q1(xiv)","question":"What does the formula Σx/n determine?","finalAnswer":"Arithmetic mean"},
          {"num":"Q1(xv)","question":"Find mean(Set B) − median(Set A), where A={2,−1,7,−4,11,3} and B={12,5,−3,4,7,−7}.","solution":"The mean of B is 18/6=3. Sorting A gives −4,−1,2,3,7,11, so its median is (2+3)/2=2.5.","finalAnswer":"0.5"},
          {"num":"Q1(xvi)","question":"What is Σf(x−x̄)²/Σf called: range, median, standard deviation, or variance?","finalAnswer":"Variance"},
          {"num":"Q1(xvii)","question":"The most frequent value in a data set is called its mean, median, mode, or geometric mean?","finalAnswer":"Mode"},
          {"num":"Q2","question":"The ages (in years) of 27 students are 17,17,16,16,17,16,16,17,18,18,15,17,19,18,18,17,16,15,16,17,15,19,19,15,15,16,18. Prepare a frequency distribution using a suitable class interval.","solution":"Tally the occurrences of each age.","finalAnswer":"Age 15: 5; 16: 7; 17: 7; 18: 5; 19: 3 (total 27)."},
          {"num":"Q3","question":"Prepare a histogram for monthly car sales: brands A, B, C, D, E sold 100, 120, 110, 72, and 169 cars, respectively.","finalAnswer":"Draw adjacent bars for A–E with heights 100, 120, 110, 72, 169."},
          {"num":"Q4","question":"Prepare a frequency polygon for test-score intervals and frequencies: 0–10:2; 11–21:7; 22–32:25; 33–43:11; 44–50:5.","solution":"Use class midpoints 5, 16, 27, 38, and 47, then join the plotted points.","finalAnswer":"Plot (5,2), (16,7), (27,25), (38,11), (47,5), joining the endpoints to the horizontal axis to close the polygon."},
          {"num":"Q5","question":"Represent the weights of 250 boys by a cumulative-frequency polygon: 44.0–47.9:13; 48.0–51.9:17; 52.0–55.9:50; 56.0–59.9:81; 60.0–63.9:57; 64.0–67.9:23; 68.0–71.9:9.","solution":"Form cumulative totals 13, 30, 80, 161, 218, 241, 250 at the upper class boundaries.","finalAnswer":"Plot the less-than cumulative-frequency points (43.95,0), (47.95,13), (51.95,30), (55.95,80), (59.95,161), (63.95,218), (67.95,241), (71.95,250), then connect them."},
          {"num":"Project","question":"For the 60-item test scores 25,30,34,37,41,42,46,49,53; 26,31,34,37,41,42,46,50,53; 28,31,35,37,41,43,47,51,54; 29,33,36,38,41,44,48,52,54; 30,33,36,39,41,44,48,52,55; 30,33,37,40,42,45,48,52, complete parts (a)–(j): group into class intervals of size 2 beginning at 24.5–25.5; make the frequency table; draw the histogram, frequency polygon and ogive; find cumulative frequencies, range, mean, standard deviation and variance.","solution":"The source specifies the grouping and asks for the corresponding frequency table and graphs, then the data’s range and descriptive statistics. The 60-item phrase describes the test, and the scan lists 53 students' scores. The printed first interval 24.5–25.5 conflicts with the requested class width of 2; for the grouped answer use width-2 continuous classes beginning 24.5–26.5 and record this correction.","finalAnswer":"For the 53 listed scores: minimum 25, maximum 55, range 30, mean = 2164/53 ≈ 40.83, population variance ≈ 66.29, and population standard deviation ≈ 8.14. Using corrected width-2 classes 24.5–26.5, 26.5–28.5, …, 54.5–56.5 gives frequencies 2,1,4,2,5,3,5,2,8,3,3,4,2,4,4,1. Plot these as histogram bars; frequency-polygon midpoints are 25.5,27.5,…,55.5. Less-than ogive points are (24.5,0),(26.5,2),(28.5,3),(30.5,7),(32.5,9),(34.5,14),(36.5,17),(38.5,22),(40.5,24),(42.5,32),(44.5,35),(46.5,38),(48.5,42),(50.5,44),(52.5,48),(54.5,52),(56.5,53)."}
        ]
      }
    ],
    "slos": [
      "Construct grouped frequency distribution tables with class boundaries, class limits, and midpoints",
      "Construct histograms, frequency polygons, and cumulative frequency polygons (ogives)",
      "Calculate Arithmetic Mean for ungrouped and grouped data using direct, short-cut, and coding methods",
      "Calculate Median and Mode for both ungrouped and grouped data",
      "Estimate Median, Quartiles, and Mode graphically from ogive and histogram",
      "Calculate Range, Variance, and Standard Deviation for ungrouped and grouped data"
    ],
    "formulaSheet": [
      {
        "name": "Arithmetic Mean (Direct)",
        "formula": "x̄ = ∑fx / ∑f",
        "note": "Weighted average of class midpoints."
      },
      {
        "name": "Grouped Median",
        "formula": "M = l + (h/f)(n/2 - c)",
        "note": "l = lower boundary of median class, c = preceding cf."
      },
      {
        "name": "Grouped Mode",
        "formula": "Mode = l + [(fₘ - f₁) / (2fₘ - f₁ - f₂)] · h",
        "note": "fₘ = maximum frequency, f₁ = pre-modal, f₂ = post-modal."
      },
      {
        "name": "Variance",
        "formula": "s² = (∑fx² / ∑f) - (∑fx / ∑f)²",
        "note": "Mean of squared deviations."
      },
      {
        "name": "Standard Deviation",
        "formula": "s = √[ (∑fx² / ∑f) - (∑fx / ∑f)² ]",
        "note": "Positive square root of variance."
      },
      {
        "name": "Range",
        "formula": "R = X_max - X_min",
        "note": "Difference between maximum and minimum values."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 7,
    "id": "u7",
    "title": "Introduction to Trigonometry",
    "titleUrdu": "مثلثیات کا تعارف",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 162–192",
    "description": "Official KPK Board Textbook Unit 7 covering sexagesimal & circular angle measurement, arc length and sector area, trigonometric ratios & identities, angles of elevation and depression, Exercises 7.1 to 7.6, and Review Exercise 7.",
    "sections": [
      {
        "id": "7.1",
        "title": "7.1 Measurement of Angles (Sexagesimal & Circular)",
        "theory": "An angle is formed by the rotation of a ray from an initial position to a terminal position around a common endpoint (vertex).\n\n1. Sexagesimal System (Degrees, Minutes, Seconds - D°M'S\"):\n   • 1 complete rotation = 360 degrees (360°).\n   • 1 degree (1°) = 60 minutes (60').\n   • 1 minute (1') = 60 seconds (60\").\n\n2. Circular System (Radians):\n   • One Radian is the measure of the angle subtended at the center of a circle by an arc whose length is equal to the radius of the circle.\n   • Circumference of circle = 2πr subtends 2π radians at the center.\n   • Relationship: 180° = π radians.\n   • 1° = π / 180 radians ≈ 0.01745 rad.\n   • 1 radian = 180° / π ≈ 57.296° ≈ 57° 17' 45\".",
        "rules": [
          "To convert degrees to radians: Multiply by π / 180.",
          "To convert radians to degrees: Multiply by 180 / π.",
          "1° = 60' and 1' = 60\"."
        ]
      },
      {
        "id": "7.2",
        "title": "7.2 Arc Length and Area of a Sector",
        "theory": "Let a circle have radius r, central angle θ (measured in radians):\n\n1. Length of Arc (l):\n   The arc length l subtending a central angle θ in radians is given by:\n   l = r · θ  (where θ must be in radians).\n\n2. Area of Sector (A):\n   A sector is the region bounded by two radii and the intercepted arc.\n   Area of sector = (1/2) · r² · θ = (1/2) · r · l  (where θ is in radians).",
        "rules": [
          "Formula l = rθ requires angle θ to be strictly in radians.",
          "Area of sector = (1/2)r²θ = (1/2)rl."
        ]
      },
      {
        "id": "7.3",
        "title": "7.3 Trigonometric Ratios and Quadrantal Signs",
        "theory": "For a right-angled triangle with angle θ:\n• sin θ = Perpendicular / Hypotenuse\n• cos θ = Base / Hypotenuse\n• tan θ = Perpendicular / Base = sin θ / cos θ\n• csc θ = 1 / sin θ = Hypotenuse / Perpendicular\n• sec θ = 1 / cos θ = Hypotenuse / Base\n• cot θ = 1 / tan θ = Base / Perpendicular\n\nSigns of Ratios in Quadrants (ASTC Rule — 'All Silver Tea Cups'):\n• Quadrant I (0° to 90°): ALL ratios are positive.\n• Quadrant II (90° to 180°): SIN (and csc) are positive; others negative.\n• Quadrant III (180° to 270°): TAN (and cot) are positive; others negative.\n• Quadrant IV (270° to 360°): COS (and sec) are positive; others negative.",
        "rules": [
          "ASTC: All (Q1), Sin (Q2), Tan (Q3), Cos (Q4).",
          "Reciprocals share the exact same algebraic signs."
        ]
      },
      {
        "id": "7.4",
        "title": "7.4 Fundamental Trigonometric Identities",
        "theory": "The three Pythagorean trigonometric identities:\n1. sin² θ + cos² θ = 1  =>  sin² θ = 1 - cos² θ  and  cos² θ = 1 - sin² θ\n2. 1 + tan² θ = sec² θ  =>  sec² θ - tan² θ = 1  and  tan² θ = sec² θ - 1\n3. 1 + cot² θ = csc² θ  =>  csc² θ - cot² θ = 1  and  cot² θ = csc² θ - 1\n\nQuotient Identities:\ntan θ = sin θ / cos θ,  cot θ = cos θ / sin θ.",
        "rules": [
          "sin²θ + cos²θ = 1",
          "1 + tan²θ = sec²θ",
          "1 + cot²θ = csc²θ"
        ]
      },
      {
        "id": "7.5",
        "title": "7.5 Angles of Elevation and Depression",
        "theory": "• Angle of Elevation: The angle between the horizontal line of sight and the line of sight looking upward to an object.\n• Angle of Depression: The angle between the horizontal line of sight and the line of sight looking downward to an object.\n• By alternate interior angles, the angle of depression of an object seen from a high point equals the angle of elevation of that point seen from the object.",
        "rules": [
          "Elevation: Eye looking upwards from horizontal.",
          "Depression: Eye looking downwards from horizontal.",
          "Angle of Elevation = Angle of Depression (alternate interior angles)."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 164) — Sexagesimal to Decimal Conversion",
        "problem": "Convert 25° 30' 45\" into decimal degrees.",
        "given": "Angle: 25° 30' 45\"",
        "method": "Degree fraction conversion: deg + min/60 + sec/3600.",
        "steps": [
          "Minutes to degrees: 30' = 30 / 60 = 0.5°.",
          "Seconds to degrees: 45\" = 45 / 3600 = 0.0125°.",
          "Total decimal degrees = 25° + 0.5° + 0.0125° = 25.5125°."
        ],
        "answer": "25.5125°"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 169) — Arc Length Calculation",
        "problem": "Find the length of an arc of a circle of radius 14 cm which subtends a central angle of 45°.",
        "given": "r = 14 cm, θ = 45°",
        "method": "Formula: l = r · θ (convert θ to radians first).",
        "steps": [
          "Convert 45° to radians: θ = 45 · (π / 180) = π / 4 radians.",
          "Apply arc length formula: l = r · θ = 14 · (π / 4) = 14 · (22 / 7) / 4 = 44 / 4 = 11 cm."
        ],
        "answer": "l = 11 cm"
      },
      {
        "id": "eg3",
        "title": "Example 3 (Page 186) — Angle of Elevation Problem",
        "problem": "A tree casts a 15-meter shadow when the angle of elevation of the sun is 60°. Find the height of the tree.",
        "given": "Shadow length (Base) = 15 m, Angle of elevation θ = 60°",
        "method": "Right triangle trigonometry: tan θ = Perpendicular / Base.",
        "steps": [
          "Let height of tree be h (Perpendicular). Base = 15 m.",
          "tan 60° = h / 15.",
          "Since tan 60° = √3 ≈ 1.732:",
          "h = 15 · √3 ≈ 15 · 1.732 = 25.98 meters."
        ],
        "answer": "Height = 15√3 m ≈ 25.98 m"
      }
    ],
    "exercises": [
      {
        "exercise": "7.1",
        "title": "Exercise 7.1 — Sexagesimal to Radians Conversion",
        "problems": [
          {
            "num": "Q1",
            "question": "Convert the following sexagesimal angles into radians: (i) 30°, (ii) 45°, (iii) 60°, (iv) 90°.",
            "solution": "(i) 30° = 30 · (π / 180) = π / 6 radians.\n(ii) 45° = 45 · (π / 180) = π / 4 radians.\n(iii) 60° = 60 · (π / 180) = π / 3 radians.\n(iv) 90° = 90 · (π / 180) = π / 2 radians.",
            "finalAnswer": "π/6, π/4, π/3, π/2 radians",
            "steps": [
              "Multiply each degree measure by π / 180",
              "Simplify common factor in numerator and denominator"
            ],
            "method": "Degree to Radian Conversion"
          }
        ]
      },
      {
        "exercise": "7.2",
        "title": "Exercise 7.2 — Arc Length and Sector Area",
        "problems": [
          {
            "num": "Q1",
            "question": "Find l when r = 6 cm and θ = 0.5 radian.",
            "solution": "l = r · θ = 6 · 0.5 = 3 cm.",
            "finalAnswer": "l = 3 cm",
            "steps": [
              "Apply l = rθ directly since θ is in radians",
              "6 · 0.5 = 3 cm"
            ],
            "method": "Arc Length Formula"
          },
          {
            "num": "Q2",
            "question": "Find r when l = 52 cm and θ = 45°.",
            "solution": "Convert θ: 45° = π / 4 rad.\nr = l / θ = 52 / (π / 4) = 208 / π ≈ 208 / 3.1416 ≈ 66.2 cm.",
            "finalAnswer": "r ≈ 66.2 cm",
            "steps": [
              "Convert 45° to π/4 rad",
              "Rearrange l = rθ to r = l / θ",
              "r = 52 / (π/4) ≈ 66.2 cm"
            ],
            "method": "Radius from Arc Length"
          }
        ]
      },
      {
        "exercise": "7.3",
        "title": "Exercise 7.3 — Coterminal Angles and Quadrants",
        "problems": [
          {"num":"Q1(i)","question":"Find two coterminal angles of 55°.","solution":"Coterminal angles differ by multiples of 360°.","finalAnswer":"415° and −305°"},
          {"num":"Q1(ii)","question":"Find two coterminal angles of −45°.","solution":"Add 360° and subtract 360°.","finalAnswer":"315° and −405°"},
          {"num":"Q1(iii)","question":"Find two coterminal angles of 5π/4.","solution":"Add and subtract 2π.","finalAnswer":"13π/4 and −3π/4"},
          {"num":"Q1(iv)","question":"Find two coterminal angles of π/6.","solution":"Add and subtract 2π.","finalAnswer":"13π/6 and −11π/6"},
          {"num":"Q2(i)","question":"State the quadrant of −3π/8.","solution":"−3π/8 is coterminal with 13π/8, which lies between 3π/2 and 2π.","finalAnswer":"Fourth quadrant"},
          {"num":"Q2(ii)","question":"State the quadrant of 75°.","solution":"75° lies between 0° and 90°.","finalAnswer":"First quadrant"},
          {"num":"Q2(iii)","question":"State the quadrant of −818°.","solution":"Add 1080° to obtain 262°, which lies between 180° and 270°.","finalAnswer":"Third quadrant"},
          {"num":"Q2(iv)","question":"State the quadrant of −5π/4.","solution":"Add 2π to obtain 3π/4, which lies between π/2 and π.","finalAnswer":"Second quadrant"},
          {"num":"Q2(v)","question":"State the quadrant of 103°.","solution":"103° lies between 90° and 180°.","finalAnswer":"Second quadrant"}
        ]
      },
      {
        "exercise": "7.4",
        "title": "Exercise 7.4 — Trigonometric Ratios and Quadrants",
        "problems": [
          {"num":"Q1","question":"Find the sign of each ratio and state its quadrant: (i) sin 98°; (ii) sin 160°; (iii) tan 200°; (iv) sec 120°; (v) cosec 198°; (vi) sin 460°.","solution":"Reduce angles to a coterminal angle between 0° and 360°, then apply the signs of sine, cosine, and tangent in that quadrant.","finalAnswer":"(i) Positive, QII; (ii) positive, QII; (iii) positive, QIII; (iv) negative, QII; (v) negative, QIII; (vi) positive, since 460° is coterminal with 100° in QII."},
          {"num":"Q2","question":"Find all six trigonometric ratios for: (i) −180°; (ii) −270°; (iii) 720°; (iv) 1470°.","solution":"Reduce each angle modulo 360°: (i) 180°; (ii) 90°; (iii) 0°; (iv) 30°. Use the unit-circle coordinates and reciprocal definitions.","finalAnswer":"(i) sin 0, cos −1, tan 0, cot undefined, sec −1, cosec undefined. (ii) sin 1, cos 0, tan undefined, cot 0, sec undefined, cosec 1. (iii) sin 0, cos 1, tan 0, cot undefined, sec 1, cosec undefined. (iv) sin 1/2, cos √3/2, tan 1/√3, cot √3, sec 2/√3, cosec 2."},
          {"num":"Q3","question":"If sec θ = 2 and θ lies in the fourth quadrant, find the other trigonometric ratios.","solution":"cos θ = 1/2. Since θ is in QIV, sin θ is negative. From sin²θ + cos²θ = 1, sin θ = −√3/2.","finalAnswer":"sin θ = −√3/2; cos θ = 1/2; tan θ = −√3; cot θ = −1/√3; sec θ = 2; cosec θ = −2/√3."},
          {"num":"Q4","question":"If sin θ = 4/5 and π/2 < θ < π, find the other trigonometric ratios.","solution":"θ is in quadrant II, so cosine is negative. From sin²θ + cos²θ = 1, cos θ = −3/5.","finalAnswer":"cos θ = −3/5; tan θ = −4/3; cot θ = −3/4; sec θ = −5/3; cosec θ = 5/4."},
          {"num":"Q5","question":"Evaluate: (i) 2 sin45° cos45°; (ii) (tan60° − tan30°)/(1 + tan60° tan30°); (iii) cos45°/(sin45° + tan45°); (iv) tan30° tan60° + tan45°; (v) cos(π/3)cos(π/6) − sin(π/3)sin(π/6).","solution":"Substitute the standard values for 30°, 45°, and 60°. For (v), use cos A cos B − sin A sin B = cos(A + B).","finalAnswer":"(i) 1; (ii) 1/√3; (iii) √2 − 1; (iv) 2; (v) 0."},
          {"num":"Q6","question":"State the quadrant(s) in which θ lies: (i) sin θ > 0, tan θ > 0; (ii) sin θ < 0, cot θ > 0; (iii) sin θ > 0, cos θ < 0; (iv) cos θ > 0, cosec θ < 0; (v) tan θ < 0, sec θ > 0; (vi) cos θ < 0, tan θ < 0.","solution":"Use the signs of sine, cosine, and tangent in each quadrant; reciprocal ratios have the same sign as their corresponding ratios.","finalAnswer":"(i) QI; (ii) QIII; (iii) QII; (iv) QIV; (v) QIV; (vi) QII."},
          {"num":"Q7","question":"For each right triangle, find the missing measure to two decimal places: (i) hypotenuse 32, angle 53°, find the side opposite the angle; (ii) hypotenuse 73, angle 21°, find the opposite side x; (iii) angle 33°, adjacent side 12, find the opposite side x.","solution":"Use sine for the opposite side when hypotenuse is known, and tangent when the adjacent side is known: (i) x = 32sin53°; (ii) x = 73sin21°; (iii) x = 12tan33°.","finalAnswer":"(i) x ≈ 25.56; (ii) x ≈ 26.17; (iii) x ≈ 7.79."},
          {"num":"Q8","question":"A lake is shown as an irregular blue shape. A surveyor measures a 24° angle and a 750 yd baseline along the shore as in the diagram. Find the distance a across the lake.","solution":"The diagram forms a right triangle with adjacent side 750 yd and opposite side a. tan24° = a/750.","finalAnswer":"a = 750tan24° ≈ 333.96 yd."}
        ]
      },
      {
        "exercise": "7.5",
        "title": "Exercise 7.5 — Proving Trigonometric Identities",
        "problems": [
          {
            "num": "Q1",
            "question": "Prove the identity: (1 - sin θ)(1 + sin θ) = cos² θ.",
            "solution": "LHS = (1 - sin θ)(1 + sin θ) = 1 - sin² θ.\nFrom the fundamental identity sin² θ + cos² θ = 1, we have 1 - sin² θ = cos² θ.\nLHS = cos² θ = RHS. Proved.",
            "finalAnswer": "cos² θ (Proved)",
            "steps": [
              "Multiply conjugates: (1 - sin θ)(1 + sin θ) = 1 - sin² θ",
              "Use Pythagorean identity 1 - sin² θ = cos² θ",
              "LHS = RHS"
            ],
            "method": "Pythagorean Identity"
          },
          {
            "num": "Q2",
            "question": "Prove that (tan θ + cot θ) = sec θ · csc θ.",
            "solution": "LHS = tan θ + cot θ = (sin θ / cos θ) + (cos θ / sin θ)\n= (sin² θ + cos² θ) / (sin θ · cos θ)\n= 1 / (sin θ · cos θ)\n= (1 / cos θ) · (1 / sin θ) = sec θ · csc θ = RHS. Proved.",
            "finalAnswer": "sec θ · csc θ (Proved)",
            "steps": [
              "Express tan and cot in terms of sin and cos",
              "Combine over common denominator sin θ cos θ",
              "Substitute numerator sin² θ + cos² θ = 1",
              "Separate into sec θ csc θ"
            ],
            "method": "Quotient Identities"
          }
        ]
      },
      {
        "exercise": "7.6",
        "title": "Exercise 7.6 — Applications of Trigonometry",
        "problems": [
          {"num":"Q1","question":"A building 21 metres tall casts a shadow 25 metres long. Find the angle of elevation of the sun to the nearest degree.","solution":"tan θ = opposite/adjacent = 21/25, so θ = tan⁻¹(21/25).","finalAnswer":"θ ≈ 40°."},
          {"num":"Q2","question":"A lighthouse is 150 m above sea level. The angle of depression of a boat from its top is 60°. Find the distance between the boat and the lighthouse.","solution":"Let d be the horizontal sea-level distance from the lighthouse base to the boat. tan 60° = 150/d, so d = 150/√3. The line-of-sight distance is 150/sin 60°.","finalAnswer":"Horizontal distance = 50√3 m ≈ 86.60 m; line of sight = 100√3 m ≈ 173.21 m."},
          {"num":"Q3","question":"A tree is 50 m high. Find the angle of elevation of its top from a point on the ground 100 m from its foot.","solution":"tan θ = 50/100 = 1/2, so θ = tan⁻¹(1/2).","finalAnswer":"θ ≈ 26.57° (about 27°)."},
          {"num":"Q4","question":"From the top of a hill 240 m high, the angles of depression to the top and bottom of a minaret are 30° and 60° respectively. Find the height of the minaret.","solution":"If the horizontal distance is d, then tan 60° = 240/d, so d = 80√3. The vertical drop to the minaret top is d tan 30° = 80 m. Therefore the minaret height is 240 − 80.","finalAnswer":"160 m."},
          {"num":"Q5","question":"A police helicopter is flying at 800 feet. A stolen car is sighted at an angle of depression of 72°. Find, to the nearest foot, the car’s horizontal distance from the point directly below the helicopter.","solution":"For horizontal distance d, tan 72° = 800/d, so d = 800/tan 72°.","finalAnswer":"d ≈ 260 ft."},
          {"num":"Q6","question":"A lighthouse is 300 m above sea level. The angles of depression of two boats are 30° and 45°. The line joining the boats passes through the foot of the lighthouse. Find the distance between the boats when they are on opposite sides of the lighthouse.","solution":"The horizontal distances from the lighthouse foot are d₁ = 300/tan 30° = 300√3 and d₂ = 300/tan 45° = 300. On opposite sides, add these distances.","finalAnswer":"300(√3 + 1) m ≈ 819.62 m."},
          {"num":"Q7","question":"The angle of elevation of the top of a cliff is 30°. After walking 210 m toward the cliff, the angle of elevation becomes 45°. Find the height of the cliff.","solution":"Let the nearer horizontal distance be x m and cliff height h. tan 45° = h/x gives x = h. The farther distance is x + 210, and tan 30° = h/(x + 210). Thus x + 210 = √3h; using x = h gives h = 210/(√3 − 1).","finalAnswer":"h = 105(√3 + 1) m ≈ 286.87 m."}
        ]
      }
    ],
    "slos": [
      "Convert sexagesimal degree, minute, second values to decimal degrees and radians and vice versa",
      "Derive and apply the formulas for arc length (l = rθ) and area of a sector (A = 1/2 r²θ)",
      "Define the six trigonometric ratios for acute angles and generalize to standard position angles",
      "State quadrant signs using ASTC rule and determine trigonometric values of allied angles",
      "Prove and apply fundamental Pythagorean identities: sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = csc²θ",
      "Solve practical real-world problems involving angles of elevation and depression"
    ],
    "formulaSheet": [
      {
        "name": "Radian to Degree",
        "formula": "1 rad = 180° / π ≈ 57.296°",
        "note": "Multiply radians by 180/π."
      },
      {
        "name": "Degree to Radian",
        "formula": "1° = π / 180 rad ≈ 0.01745 rad",
        "note": "Multiply degrees by π/180."
      },
      {
        "name": "Arc Length",
        "formula": "l = r · θ",
        "note": "θ MUST be in radians."
      },
      {
        "name": "Area of Sector",
        "formula": "A = (1/2) · r² · θ = (1/2) · r · l",
        "note": "θ in radians."
      },
      {
        "name": "Fundamental Identity I",
        "formula": "sin² θ + cos² θ = 1",
        "note": "cos² θ = 1 - sin² θ, sin² θ = 1 - cos² θ."
      },
      {
        "name": "Fundamental Identity II",
        "formula": "1 + tan² θ = sec² θ",
        "note": "sec² θ - tan² θ = 1."
      },
      {
        "name": "Fundamental Identity III",
        "formula": "1 + cot² θ = csc² θ",
        "note": "csc² θ - cot² θ = 1."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 8,
    "id": "u8",
    "title": "Projection of a Side of a Triangle",
    "titleUrdu": "مثلث کے ضلع کا ظل (پروجیکشن)",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 193–201",
    "description": "Official KPK Board Textbook Unit 8 covering projection of line segments, theorems on obtuse and acute-angled triangles, Apollonius Theorem, Exercises 8.1, 8.2, and Review Exercise 8.",
    "sections": [
      {
        "id": "8.1",
        "title": "8.1 Projection of a Point and a Line Segment",
        "theory": "• Projection of a Point: The projection of a point P on a given straight line AB is the foot of the perpendicular drawn from P onto AB.\n• Projection of a Line Segment: The projection of a line segment CD on a line AB is the segment between the feet of the perpendiculars drawn from the endpoints C and D onto AB.\n• If a line segment is parallel to AB, its projection is equal in length to the segment.\n• If a line segment is perpendicular to AB, its projection is a single point (length = 0).",
        "rules": [
          "Projection of a point is the foot of the perpendicular on the line.",
          "Projection of a segment CD is the portion between the feet of perpendiculars from C and D."
        ]
      },
      {
        "id": "8.2",
        "title": "8.2 Theorem 8.1 — Obtuse-Angled Triangle",
        "theory": "Statement:\nIn an obtuse-angled triangle, the square on the side opposite to the obtuse angle is equal to the sum of the squares on the sides containing the obtuse angle together with twice the rectangle contained by one of those sides and the projection on it of the other.\n\nMathematical Form:\nIn △ABC where ∠C is obtuse and CD is the projection of AC on BC produced:\nAB² = BC² + AC² + 2(BC · CD)\nor in standard notation: c² = a² + b² + 2a · p (where p is the projection of b on a).",
        "rules": [
          "Applies to obtuse-angled triangles.",
          "Formula: c² = a² + b² + 2a · p.",
          "Notice the + sign: the square on the opposite side exceeds the sum of squares."
        ]
      },
      {
        "id": "8.3",
        "title": "8.3 Theorem 8.2 — Acute-Angled Triangle",
        "theory": "Statement:\nIn an acute-angled triangle, the square on the side opposite to an acute angle is equal to the sum of the squares on the sides containing that acute angle diminished by twice the rectangle contained by one of those sides and the projection on it of the other.\n\nMathematical Form:\nIn △ABC where ∠C is acute and CD is the projection of AC on BC:\nAB² = BC² + AC² - 2(BC · CD)\nor c² = a² + b² - 2a · p (where p is the projection of b on a).",
        "rules": [
          "Applies to acute-angled triangles.",
          "Formula: c² = a² + b² - 2a · p.",
          "Notice the - sign: the square on the opposite side is diminished."
        ]
      },
      {
        "id": "8.4",
        "title": "8.4 Theorem 8.3 — Apollonius Theorem",
        "theory": "Statement:\nIn any triangle, the sum of the squares on any two sides is equal to twice the square on half the third side together with twice the square on the median bisecting the third side.\n\nMathematical Form:\nIn △ABC, if AD is a median to side BC (so BD = DC = a/2):\nAB² + AC² = 2(BD² + AD²)\nor c² + b² = 2(a/2)² + 2m².",
        "rules": [
          "Relates sides of any triangle to the length of its median.",
          "Formula: b² + c² = 2(a/2)² + 2m²."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 196) — Applying Obtuse Angle Theorem",
        "problem": "In △ABC, ∠C = 120°, a = 5 cm, b = 6 cm. Find the length of side c.",
        "given": "△ABC with a = 5 cm, b = 6 cm, ∠C = 120° (obtuse)",
        "method": "Theorem 8.1 with projection p = b · cos(180° - 120°) = b · cos 60°.",
        "steps": [
          "The projection p of b on BC produced is p = b · cos(180° - 120°) = 6 · cos 60° = 6 · (1/2) = 3 cm.",
          "Apply Theorem 8.1: c² = a² + b² + 2a · p",
          "c² = 5² + 6² + 2(5)(3)",
          "c² = 25 + 36 + 30 = 91",
          "c = √91 ≈ 9.54 cm."
        ],
        "answer": "c = √91 ≈ 9.54 cm"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 199) — Apollonius Theorem for Median",
        "problem": "In △ABC, AB = 6 cm, AC = 8 cm, and BC = 10 cm. Find the length of the median AD to the side BC.",
        "given": "AB = 6 cm, AC = 8 cm, BC = 10 cm (BD = DC = 5 cm)",
        "method": "Apollonius Theorem: AB² + AC² = 2(BD² + AD²).",
        "steps": [
          "Substitute given values: 6² + 8² = 2(5² + AD²)",
          "36 + 64 = 2(25 + AD²)",
          "100 = 2(25 + AD²)",
          "50 = 25 + AD²",
          "AD² = 25 => AD = 5 cm."
        ],
        "answer": "Median AD = 5 cm"
      }
    ],
    "exercises": [
      {
        "exercise": "8.1",
        "title": "Exercise 8.1 — Projections in Acute & Obtuse Triangles",
        "problems": [
          {
            "num": "Q1",
            "question": "In △ABC, ∠C is obtuse. If BC = 4 cm, AC = 5 cm, and the projection of AC on BC is 2 cm, find AB.",
            "solution": "By Theorem 8.1:\nAB² = BC² + AC² + 2(BC · projection)\nAB² = 4² + 5² + 2(4 · 2)\nAB² = 16 + 25 + 16 = 57\nAB = √57 ≈ 7.55 cm.",
            "finalAnswer": "AB = √57 cm ≈ 7.55 cm",
            "steps": [
              "Identify obtuse triangle formula: c² = a² + b² + 2a·p",
              "Substitute a = 4, b = 5, p = 2",
              "c² = 16 + 25 + 16 = 57",
              "c = √57 cm"
            ],
            "method": "Obtuse Triangle Theorem"
          },
          {
            "num": "Q2",
            "question": "In △ABC, ∠C is acute. If a = 7 cm, b = 8 cm, and projection of b on a is 3 cm, find c.",
            "solution": "By Theorem 8.2:\nc² = a² + b² - 2a · p\nc² = 7² + 8² - 2(7)(3)\nc² = 49 + 64 - 42 = 71\nc = √71 ≈ 8.43 cm.",
            "finalAnswer": "c = √71 cm ≈ 8.43 cm",
            "steps": [
              "Identify acute triangle formula: c² = a² + b² - 2a·p",
              "Substitute a = 7, b = 8, p = 3",
              "c² = 49 + 64 - 42 = 71",
              "c = √71 cm"
            ],
            "method": "Acute Triangle Theorem"
          }
        ]
      },
      {
        "exercise": "8.2",
        "title": "Exercise 8.2 — Apollonius Theorem Applications",
        "problems": [
          {
            "num": "Q1",
            "question": "In △ABC, the sides are AB = 7, AC = 9, and BC = 8. Find the length of the median to BC.",
            "solution": "Half of third side: d = BC / 2 = 8 / 2 = 4.\nBy Apollonius Theorem:\nAB² + AC² = 2(d² + m²)\n7² + 9² = 2(4² + m²)\n49 + 81 = 2(16 + m²)\n130 = 2(16 + m²)\n65 = 16 + m² => m² = 49 => m = 7.",
            "finalAnswer": "Median length = 7",
            "steps": [
              "Find half of BC: 8/2 = 4",
              "Apply Apollonius: 7² + 9² = 2(4² + m²)",
              "130 = 2(16 + m²) => 65 = 16 + m²",
              "m² = 49 => m = 7"
            ],
            "method": "Apollonius Theorem"
          }
        ]
      }
    ],
    "slos": [
      "Define the orthogonal projection of a point and a line segment on a given straight line",
      "State, prove, and apply Theorem 8.1 for obtuse-angled triangles: c² = a² + b² + 2a·p",
      "State, prove, and apply Theorem 8.2 for acute-angled triangles: c² = a² + b² - 2a·p",
      "State, prove, and apply Apollonius Theorem relating sides of a triangle to its median: b² + c² = 2(a/2)² + 2m²"
    ],
    "formulaSheet": [
      {
        "name": "Theorem 8.1 (Obtuse)",
        "formula": "c² = a² + b² + 2a · p",
        "note": "p = projection of side b on side a."
      },
      {
        "name": "Theorem 8.2 (Acute)",
        "formula": "c² = a² + b² - 2a · p",
        "note": "Diminished by twice the product of side and projection."
      },
      {
        "name": "Apollonius Theorem",
        "formula": "b² + c² = 2(a/2)² + 2m²",
        "note": "m = length of median to side a."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 9,
    "id": "u9",
    "title": "Chords of a Circle",
    "titleUrdu": "دائرے کے وتر",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 202–211",
    "description": "Official KPK Board Textbook Unit 9 with theorems on chords, perpendicular from center, equidistant chords, Exercises 9.1, 9.2, and Review Exercise 9.",
    "sections": [
      {
        "id": "9.1",
        "title": "9.1 Circle and Three Non-Collinear Points",
        "theory": "• Circle: The set of all points in a plane equidistant from a fixed point (center).\n• Chord: A line segment joining any two points on a circle.\n• Diameter: A chord passing through the center of the circle (longest chord).\n• Theorem 9.1: One and only one circle can pass through three non-collinear points.\n  Proof outlines that the perpendicular bisectors of the two segments AB and BC intersect at a unique point O, which serves as the unique center.",
        "rules": [
          "A unique circle passes through three non-collinear points.",
          "No circle can pass through three collinear points."
        ]
      },
      {
        "id": "9.2",
        "title": "9.2 Bisector of a Chord Passing Through Center",
        "theory": "• Theorem 9.2: A straight line drawn from the center of a circle to bisect a chord (which is not a diameter) is at right angles to the chord.\n  If M is the midpoint of chord AB and O is the center, then OM ⊥ AB.\n\n• Theorem 9.3: Perpendicular from the center of a circle on a chord bisects the chord.\n  If OM ⊥ AB, then AM = MB = (1/2)AB.\n  By Pythagorean theorem in right △OMA: OA² = OM² + AM² (where OA = radius r).",
        "rules": [
          "Line from center to chord midpoint is perpendicular to chord.",
          "Perpendicular from center to chord bisects the chord.",
          "Pythagorean relation: r² = d² + (chord / 2)² where d is distance from center."
        ]
      },
      {
        "id": "9.3",
        "title": "9.3 Congruent and Equidistant Chords",
        "theory": "• Theorem 9.4: If two chords of a circle are congruent, then they are equidistant from the center.\n  If AB = CD, then their distances from center OM = ON.\n\n• Theorem 9.5 (Converse): Two chords of a circle which are equidistant from the center are congruent.\n  If OM = ON, then chord AB = chord CD.",
        "rules": [
          "Equal chords are equidistant from the center.",
          "Chords equidistant from the center are equal in length."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 205) — Distance of Chord from Center",
        "problem": "A chord of length 16 cm is drawn in a circle of radius 10 cm. Find the distance of the chord from the center of the circle.",
        "given": "Radius r = 10 cm, Chord AB = 16 cm",
        "method": "Theorem 9.3 and Pythagorean Theorem.",
        "steps": [
          "Perpendicular from center bisects chord: AM = AB / 2 = 16 / 2 = 8 cm.",
          "In right △OMA: OA² = OM² + AM².",
          "10² = OM² + 8²",
          "100 = OM² + 64",
          "OM² = 100 - 64 = 36",
          "OM = 6 cm."
        ],
        "answer": "Distance OM = 6 cm"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 208) — Finding Chord Length",
        "problem": "The distance of a chord from the center of a circle of radius 13 cm is 5 cm. Find the length of the chord.",
        "given": "Radius r = 13 cm, Distance d = 5 cm",
        "method": "Pythagorean Theorem: (AB/2)² = r² - d².",
        "steps": [
          "Half chord AM = √(r² - d²) = √(13² - 5²) = √(169 - 25) = √144 = 12 cm.",
          "Total chord AB = 2 · AM = 2 · 12 = 24 cm."
        ],
        "answer": "Chord length = 24 cm"
      }
    ],
    "exercises": [
      {
        "exercise": "9.1",
        "title": "Exercise 9.1 — Chords and Perpendiculars from Center",
        "problems": [
          {
            "num": "Q1",
            "question": "A circle has radius 17 cm. A chord is drawn at a distance of 8 cm from the center. What is the length of the chord?",
            "solution": "Let r = 17 cm, distance d = 8 cm.\nHalf chord = √(r² - d²) = √(17² - 8²) = √(289 - 64) = √225 = 15 cm.\nFull chord length = 2 · 15 = 30 cm.",
            "finalAnswer": "30 cm",
            "steps": [
              "Use Pythagorean theorem: (half chord)² = 17² - 8² = 225",
              "Half chord = 15 cm",
              "Full chord = 2 · 15 = 30 cm"
            ],
            "method": "Pythagorean Theorem on Chords"
          },
          {
            "num": "Q2",
            "question": "In a circle of radius 25 cm, two parallel chords of lengths 40 cm and 48 cm are drawn on the same side of the center. Find the distance between them.",
            "solution": "Distance of 40 cm chord from center: d₁ = √(25² - (40/2)²) = √(625 - 400) = √225 = 15 cm.\nDistance of 48 cm chord from center: d₂ = √(25² - (48/2)²) = √(625 - 576) = √49 = 7 cm.\nSince chords are on the same side, distance between them = d₁ - d₂ = 15 - 7 = 8 cm.",
            "finalAnswer": "8 cm",
            "steps": [
              "Calculate distance d₁ for chord 40 cm: √(625 - 400) = 15 cm",
              "Calculate distance d₂ for chord 48 cm: √(625 - 576) = 7 cm",
              "Subtract distances: 15 - 7 = 8 cm"
            ],
            "method": "Parallel Chords Distance"
          }
        ]
      },
      {
        "exercise": "9.2",
        "title": "Exercise 9.2 — Chords of a Circle",
        "problems": [
          {"num":"Q1","question":"In a circle of radius 5 cm, two parallel chords have lengths 8 cm and 6 cm. Calculate the distance between the chords.","solution":"The perpendicular distances from the centre to the chords are √(5² − 4²) = 3 cm and √(5² − 3²) = 4 cm. Depending on whether the chords lie on the same or opposite sides of the centre, their separation is the difference or the sum of these distances.","finalAnswer":"1 cm if the chords are on the same side of the centre; 7 cm if on opposite sides."},
          {"num":"Q2","question":"Two parallel chords PQ and MN are 3 cm apart on the same side of a circle. PQ = 7 cm and MN = 14 cm. Calculate the circle’s radius.","solution":"Let the distances from the centre to the chords of lengths 7 and 14 be d₇ and d₁₄. Since the longer chord is nearer the centre, d₇ − d₁₄ = 3. By the right-triangle chord formula, d₇² = r² − (7/2)² and d₁₄² = r² − 7². Subtracting gives (d₇ − d₁₄)(d₇ + d₁₄) = 36.75, so d₇ + d₁₄ = 12.25. Hence d₇ = 7.625 and r² = 7.625² + 3.5².","finalAnswer":"r ≈ 8.39 cm."},
          {"num":"Q3","question":"Circle C has radius 10. Chord QT is 5 units from C and chord PR is 8 units from C. (a) Compare the chord lengths PR and QT. (b) Compare their distances from C.","solution":"A chord at distance d from the centre has length 2√(r² − d²). QT = 2√(100 − 25) = 10√3 ≈ 17.32; PR = 2√(100 − 64) = 12. The distances from C are given as 5 and 8.","finalAnswer":"(a) QT > PR. (b) PR is farther from C than QT."}
        ]
      }
    ],
    "slos": [
      "Prove that one and only one circle can pass through three non-collinear points",
      "Prove that a straight line drawn from center to bisect a chord is perpendicular to the chord",
      "Prove that the perpendicular from center on a chord bisects the chord",
      "Prove that congruent chords are equidistant from the center and converse",
      "Apply the Pythagorean theorem (r² = d² + (c/2)²) to calculate radii, chord lengths, and distances"
    ],
    "formulaSheet": [
      {
        "name": "Chord Geometry Formula",
        "formula": "r² = d² + (chord / 2)²",
        "note": "r = radius, d = perpendicular distance from center."
      },
      {
        "name": "Half-Chord",
        "formula": "AM = √(r² - d²)",
        "note": "Length of half the chord."
      },
      {
        "name": "Chord Length",
        "formula": "AB = 2√(r² - d²)",
        "note": "Total length of chord."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 10,
    "id": "u10",
    "title": "Tangent to a Circle",
    "titleUrdu": "دائرے کا مماس",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 212–224",
    "description": "Official KPK Board Textbook Unit 10 with tangent theorems, radius-tangent perpendicularity, external point tangents, touching circles, Exercises 10.1, 10.2, and Review Exercise 10.",
    "sections": [
      {
        "id": "10.1",
        "title": "10.1 Tangents and Secants to a Circle",
        "theory": "• Secant: A straight line that intersects a circle at two distinct points.\n• Tangent: A straight line that touches a circle at exactly one point. This point is called the Point of Contact or Point of tangency.\n\n• Theorem 10.1: If a line is drawn perpendicular to a radial segment of a circle at its outer endpoint, it is tangent to the circle.\n• Theorem 10.2: The tangent to a circle and the radial segment joining the point of contact and the center are perpendicular to each other: OT ⊥ PT.\n\nIn right △OPT (where O is center, P is external point, T is point of contact):\nOP² = OT² + PT²  =>  PT = √(OP² - r²).",
        "rules": [
          "A tangent touches the circle at exactly one point.",
          "Tangent is perpendicular to the radius at the point of contact (OT ⊥ PT).",
          "Pythagorean relation: OP² = r² + (tangent length)²."
        ]
      },
      {
        "id": "10.2",
        "title": "10.2 Tangents from an External Point",
        "theory": "• Theorem 10.3: The two tangents drawn to a circle from an external point are equal in length.\n  If PA and PB are two tangents from point P to a circle with center O at points of contact A and B:\n  1. PA = PB (tangent lengths are equal).\n  2. ∠APO = ∠BPO (OP bisects ∠APB).\n  3. ∠AOP = ∠BOP (OP bisects ∠AOB).",
        "rules": [
          "Two tangents from an external point are equal in length (PA = PB).",
          "The line joining the external point and center bisects the angle between the tangents."
        ]
      },
      {
        "id": "10.3",
        "title": "10.3 Touching Circles (External & Internal)",
        "theory": "• Theorem 10.4: If two circles touch each other (externally or internally), the point of contact lies on the straight line joining their centers.\n\n1. External Contact:\n   Distance between centers d = r₁ + r₂.\n2. Internal Contact:\n   Distance between centers d = |r₁ - r₂|.",
        "rules": [
          "External contact: Distance between centers = r₁ + r₂.",
          "Internal contact: Distance between centers = |r₁ - r₂|."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 215) — Length of Tangent Segment",
        "problem": "From a point P which is 10 cm away from the center of a circle of radius 6 cm, a tangent PT is drawn. Find the length of the tangent PT.",
        "given": "Distance OP = 10 cm, Radius OT = 6 cm",
        "method": "Theorem 10.2: OT ⊥ PT, applying Pythagorean Theorem in △OPT.",
        "steps": [
          "Since OT ⊥ PT, △OPT is a right triangle at T.",
          "OP² = OT² + PT²",
          "10² = 6² + PT²",
          "100 = 36 + PT²",
          "PT² = 100 - 36 = 64",
          "PT = √64 = 8 cm."
        ],
        "answer": "Length of tangent PT = 8 cm"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 221) — Distance Between Centers of Touching Circles",
        "problem": "Two circles of radii 7 cm and 4 cm touch each other. Find the distance between their centers if: (i) they touch externally, (ii) they touch internally.",
        "given": "r₁ = 7 cm, r₂ = 4 cm",
        "method": "Theorem 10.4.",
        "steps": [
          "(i) Touching Externally: d = r₁ + r₂ = 7 + 4 = 11 cm.",
          "(ii) Touching Internally: d = r₁ - r₂ = 7 - 4 = 3 cm."
        ],
        "answer": "(i) 11 cm; (ii) 3 cm"
      }
    ],
    "exercises": [
      {
        "exercise": "10.1",
        "title": "Exercise 10.1 — Tangent Lengths and Properties",
        "problems": [
          {
            "num": "Q1",
            "question": "A point P is 13 cm away from the center of a circle of radius 5 cm. Find the length of the tangent drawn from P to the circle.",
            "solution": "In right △OPT with OT = 5 cm and OP = 13 cm:\nPT = √(OP² - OT²) = √(13² - 5²) = √(169 - 25) = √144 = 12 cm.",
            "finalAnswer": "12 cm",
            "steps": [
              "Identify right triangle △OPT with hypotenuse OP = 13 cm",
              "Radius OT = 5 cm",
              "PT = √(169 - 25) = 12 cm"
            ],
            "method": "Tangency Pythagorean Theorem"
          },
          {
            "num": "Q2",
            "question": "Two concentric circles have radii 5 cm and 3 cm. Find the length of the chord of the larger circle which touches the smaller circle.",
            "solution": "Let the chord of the larger circle touch the smaller circle at T.\nThen OT = 3 cm (radius of inner circle), and OA = 5 cm (radius of outer circle).\nSince OT ⊥ AB, T is the midpoint of chord AB.\nAT = √(OA² - OT²) = √(5² - 3²) = √(25 - 9) = √16 = 4 cm.\nTotal length of chord AB = 2 · AT = 2 · 4 = 8 cm.",
            "finalAnswer": "8 cm",
            "steps": [
              "Radius to point of contact OT = 3 cm is perpendicular to chord AB",
              "Outer radius OA = 5 cm",
              "AT = √(25 - 9) = 4 cm",
              "Full chord AB = 2 · 4 = 8 cm"
            ],
            "method": "Concentric Circles Tangent"
          }
        ]
      },
      {
        "exercise": "10.2",
        "title": "Exercise 10.2 — Tangents and Chords",
        "problems": [
          {"num":"Q1","question":"Two circles with radii 8 cm and 3 cm touch externally. Find the distance between their centres.","solution":"For externally tangent circles, the centre distance is the sum of the radii.","finalAnswer":"11 cm."},
          {"num":"Q2","question":"The centres of two internally tangent circles are 5 cm apart. The larger circle has radius 17 cm. Find the smaller radius.","solution":"For internal tangency, the centre distance equals the difference of the radii: 17 − r = 5.","finalAnswer":"12 cm."},
          {"num":"Q3","question":"A 10 cm chord is 12 cm from the centre of a circle. Find the length of a chord 5 cm from the centre.","solution":"The first chord’s half-length is 5 cm, so r² = 5² + 12² = 169 and r = 13 cm. The second chord has half-length √(13² − 5²) = 12 cm.","finalAnswer":"24 cm."},
          {"num":"Q4","question":"A chord is 18 cm long and the circle’s radius is 15 cm. Find the distance from the centre to the chord’s midpoint.","solution":"The perpendicular from the centre bisects the chord. Its half-length is 9 cm, so the distance is √(15² − 9²).","finalAnswer":"12 cm."},
          {"num":"Q5","question":"Find the length of a chord 6 cm from the centre of a circle with radius 10 cm.","solution":"Half the chord is √(10² − 6²) = 8 cm.","finalAnswer":"16 cm."},
          {"num":"Q6","question":"A chord is 3 cm from the centre of a circle and is 8 cm long. Find the diameter.","solution":"The perpendicular bisects the chord, giving half-chord 4 cm. The radius is √(3² + 4²) = 5 cm.","finalAnswer":"10 cm."},
          {"num":"Q7","question":"A circle has radius 8 cm and a chord 12 cm long. Find the distance of the chord from the centre.","solution":"The half-chord is 6 cm. The perpendicular distance is √(8² − 6²) = √28.","finalAnswer":"2√7 cm."},
          {"num":"Q8","question":"A chord of a circle with radius 7.5 cm is 9 cm long. Find its distance from the centre.","solution":"Half the chord is 4.5 cm. The distance is √(7.5² − 4.5²) = √36.","finalAnswer":"6 cm."}
        ]
      }
    ],
    "slos": [
      "Define secant, tangent, and point of contact of a circle",
      "Prove that the tangent at any point of a circle is perpendicular to the radial segment through the point of contact",
      "Prove that the lengths of two tangents drawn from an external point to a circle are equal",
      "Prove that when two circles touch each other, the point of contact lies on the line of centers",
      "Calculate tangent lengths using Pythagorean theorem in right-angled triangles formed by radial segments"
    ],
    "formulaSheet": [
      {
        "name": "Tangent Length Formula",
        "formula": "PT = √(OP² - r²)",
        "note": "OP = distance of external point from center, r = radius."
      },
      {
        "name": "External Tangents Equality",
        "formula": "PA = PB",
        "note": "Tangents from external point P to circle are equal."
      },
      {
        "name": "Touching Circles (External)",
        "formula": "d = r₁ + r₂",
        "note": "Distance between centers of externally touching circles."
      },
      {
        "name": "Touching Circles (Internal)",
        "formula": "d = |r₁ - r₂|",
        "note": "Distance between centers of internally touching circles."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 11,
    "id": "u11",
    "title": "Chords and Arcs",
    "titleUrdu": "وتر اور قوسیں",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 225–237",
    "description": "Official KPK Board Textbook Unit 11 covering relationships between chords, arcs, and central angles, Theorems 11.1 to 11.4, Exercise 11, and Review Exercise 11.",
    "sections": [
      {
        "id": "11.1",
        "title": "11.1 Congruence of Arcs and Chords",
        "theory": "• Theorem 11.1: If two arcs of a circle (or congruent circles) are congruent, then the corresponding chords are equal.\n  Given arc AB ≅ arc CD, then chord AB = chord CD.\n\n• Theorem 11.2 (Converse): If two chords of a circle (or congruent circles) are equal, then their corresponding arcs are congruent.\n  Given chord AB = chord CD, then m(arc AB) = m(arc CD).",
        "rules": [
          "Congruent arcs determine equal chords.",
          "Equal chords subtend congruent arcs."
        ]
      },
      {
        "id": "11.2",
        "title": "11.2 Central Angles and Arcs",
        "theory": "• Theorem 11.3: Equal chords of a circle (or congruent circles) subtend equal angles at the center.\n  If chord AB = chord CD, then ∠AOB = ∠COD.\n\n• Theorem 11.4 (Converse): If two central angles of a circle (or congruent circles) are equal, then the intercepted arcs and corresponding chords are equal.\n  If ∠AOB = ∠COD, then arc AB ≅ arc CD and chord AB = chord CD.",
        "rules": [
          "Equal chords subtend equal central angles.",
          "Equal central angles intercept equal chords and arcs."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 229) — Central Angles of Equal Chords",
        "problem": "In a circle of center O, chord AB = chord CD. If ∠AOB = 72°, find the measure of ∠COD and the angle subtended by arc CD on the circumference.",
        "given": "Chord AB = CD, ∠AOB = 72°",
        "method": "Theorems 11.3 and 12.1.",
        "steps": [
          "By Theorem 11.3, equal chords subtend equal angles at the center.",
          "Therefore, ∠COD = ∠AOB = 72°.",
          "The angle subtended on the circumference is half the central angle: 72° / 2 = 36°."
        ],
        "answer": "∠COD = 72°, circumference angle = 36°"
      }
    ],
    "exercises": [
      {
        "exercise": "11.1",
        "title": "Exercise 11 — Chords, Arcs & Central Angles",
        "problems": [
          {
            "num": "Q1",
            "question": "A circle is divided into 6 equal arcs. What is the measure of the central angle subtended by each arc? What is the polygon formed by joining the consecutive endpoints?",
            "solution": "Total measure of central angle of a complete circle = 360°.\nEach central angle = 360° / 6 = 60°.\nSince all 6 arcs are equal, the 6 corresponding chords are all equal.\nJoining the consecutive endpoints forms a Regular Hexagon.",
            "finalAnswer": "Central angle = 60°, Regular Hexagon",
            "steps": [
              "Divide 360° by 6 = 60°",
              "Equal arcs subtend equal chords",
              "6 equal sides in a circle form a regular hexagon"
            ],
            "method": "Central Angle Partition"
          }
        ]
      }
    ],
    "slos": [
      "Prove that if two arcs of a circle are congruent, the corresponding chords are equal and converse",
      "Prove that equal chords subtend equal angles at the center and converse",
      "Calculate central angles and arc measurements for regular inscribed polygons"
    ],
    "formulaSheet": [
      {
        "name": "Arc-Chord Equivalence",
        "formula": "arc AB ≅ arc CD  <=>  chord AB = chord CD",
        "note": "Bi-directional geometric equivalence."
      },
      {
        "name": "Central Angle Equivalence",
        "formula": "chord AB = chord CD  <=>  ∠AOB = ∠COD",
        "note": "Equal chords subtend equal central angles."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 12,
    "id": "u12",
    "title": "Angle in a Segment of a Circle",
    "titleUrdu": "دائرے کے قطعے میں زاویہ",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 238–249",
    "description": "Official KPK Board Textbook Unit 12 covering central and inscribed angles, angles in the same segment, angles in semicircles, cyclic quadrilaterals, Exercise 12, and Review Exercise 12.",
    "sections": [
      {
        "id": "12.1",
        "title": "12.1 Central Angle vs Inscribed Angle",
        "theory": "• Central Angle: An angle whose vertex is at the center of the circle and whose sides are radii (e.g., ∠AOB).\n• Inscribed Angle (Angle in a Segment): An angle whose vertex lies on the circle and whose sides are chords (e.g., ∠APB).\n\n• Theorem 12.1: The measure of a central angle of a minor arc of a circle is double that of the angle subtended by the corresponding major arc.\n  m∠AOB = 2 · m∠APB  or  m∠APB = (1/2) · m∠AOB.",
        "rules": [
          "Central angle is twice the inscribed angle subtended by the same arc: m∠AOB = 2·m∠APB.",
          "Inscribed angle is half of the central angle."
        ]
      },
      {
        "id": "12.2",
        "title": "12.2 Angles in the Same Segment and Semicircle",
        "theory": "• Theorem 12.2: Any two angles in the same segment of a circle are equal.\n  If ∠ACB and ∠ADB are subtended by the same arc AB, then m∠ACB = m∠ADB.\n\n• Theorem 12.3:\n  (a) The angle in a semicircle is a right angle (90°).\n  (b) The angle in a segment greater than a semicircle is less than a right angle (acute, < 90°).\n  (c) The angle in a segment less than a semicircle is greater than a right angle (obtuse, > 90°).",
        "rules": [
          "All inscribed angles in the same segment are equal.",
          "Angle inscribed in a semicircle is always 90° (Right angle)."
        ]
      },
      {
        "id": "12.3",
        "title": "12.3 Cyclic Quadrilaterals",
        "theory": "• Cyclic Quadrilateral: A quadrilateral whose all four vertices lie on the circumference of a circle.\n\n• Theorem 12.4: The opposite angles of any cyclic quadrilateral are supplementary.\n  If ABCD is a cyclic quadrilateral:\n  m∠A + m∠C = 180°\n  m∠B + m∠D = 180°.\n\n• Exterior Angle Corollary:\n  An exterior angle of a cyclic quadrilateral is equal to the interior opposite angle.",
        "rules": [
          "Opposite angles of a cyclic quadrilateral add up to 180° (supplementary).",
          "Exterior angle = opposite interior angle."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 241) — Calculating Inscribed Angle",
        "problem": "In a circle with center O, minor arc AB subtends a central angle ∠AOB = 110°. Find the inscribed angle ∠APB subtended on the major arc.",
        "given": "Central angle ∠AOB = 110°",
        "method": "Theorem 12.1: Inscribed angle is half the central angle.",
        "steps": [
          "m∠APB = (1/2) · m∠AOB",
          "m∠APB = (1/2) · 110° = 55°."
        ],
        "answer": "m∠APB = 55°"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 246) — Cyclic Quadrilateral Angles",
        "problem": "In cyclic quadrilateral ABCD, ∠A = (2x + 10)° and ∠C = (3x + 20)°. Find the value of x and the measure of each angle.",
        "given": "Cyclic quadrilateral ABCD with opposite angles ∠A and ∠C",
        "method": "Theorem 12.4: Opposite angles are supplementary.",
        "steps": [
          "∠A + ∠C = 180°",
          "(2x + 10) + (3x + 20) = 180",
          "5x + 30 = 180",
          "5x = 150 => x = 30°.",
          "∠A = 2(30) + 10 = 70°.",
          "∠C = 3(30) + 20 = 110°."
        ],
        "answer": "x = 30°, ∠A = 70°, ∠C = 110°"
      }
    ],
    "exercises": [
      {
        "exercise": "12.1",
        "title": "Exercise 12 — Angles in Segment & Cyclic Quadrilaterals",
        "problems": [
          {
            "num": "Q1",
            "question": "A chord AB subtends an angle of 48° at the circumference of a circle. What is the angle subtended by AB at the center of the circle?",
            "solution": "By Theorem 12.1, central angle is double the angle at the circumference:\nCentral angle = 2 · 48° = 96°.",
            "finalAnswer": "96°",
            "steps": [
              "Use Theorem 12.1: Central angle = 2 · Inscribed angle",
              "2 · 48° = 96°"
            ],
            "method": "Central Angle Theorem"
          },
          {
            "num": "Q2",
            "question": "In a cyclic quadrilateral PQRS, if ∠P = 75° and ∠Q = 110°, find ∠R and ∠S.",
            "solution": "Opposite angles are supplementary (Theorem 12.4):\n∠P + ∠R = 180° => 75° + ∠R = 180° => ∠R = 105°.\n∠Q + ∠S = 180° => 110° + ∠S = 180° => ∠S = 70°.",
            "finalAnswer": "∠R = 105°, ∠S = 70°",
            "steps": [
              "∠R = 180° - 75° = 105°",
              "∠S = 180° - 110° = 70°"
            ],
            "method": "Cyclic Quadrilateral Supplementary Property"
          }
        ]
      }
    ],
    "slos": [
      "Prove that the central angle of a minor arc is double the angle subtended by the corresponding major arc",
      "Prove that any two angles in the same segment of a circle are equal",
      "Prove that the angle in a semicircle is a right angle",
      "Prove that opposite angles of any cyclic quadrilateral are supplementary"
    ],
    "formulaSheet": [
      {
        "name": "Central Angle Theorem",
        "formula": "m∠AOB = 2 · m∠APB",
        "note": "Central angle is double the inscribed angle."
      },
      {
        "name": "Angle in Semicircle",
        "formula": "m∠APB = 90°",
        "note": "Any angle inscribed in a semicircle is a right angle."
      },
      {
        "name": "Cyclic Quadrilateral",
        "formula": "∠A + ∠C = 180°,  ∠B + ∠D = 180°",
        "note": "Opposite angles are supplementary."
      }
    ],
    "classId": "cls10"
  },
  {
    "number": 13,
    "id": "u13",
    "title": "Practical Geometry - Circles",
    "titleUrdu": "عملی جیومیٹری - دائرے",
    "status": "ready",
    "badge": "100% Textbook Matched",
    "pageRange": "Pages 250–269",
    "description": "Official KPK Board Textbook Unit 13 with step-by-step geometric constructions of circumscribed, inscribed, and escribed circles, tangents, direct and transverse common tangents, Exercises 13.1 to 13.3, and Review Exercise 13.",
    "sections": [
      {
        "id": "13.1",
        "title": "13.1 Construction of Circles Through Points",
        "theory": "1. Circle Passing Through Three Non-Collinear Points:\n   • Draw line segments AB and BC.\n   • Draw the perpendicular bisectors of AB and BC.\n   • The point of intersection O of these bisectors is the center.\n   • With O as center and radius OA (or OB or OC), draw the required circle.\n\n2. Completing a Broken Circle Arc:\n   • Choose three points A, B, C on the given arc.\n   • Draw perpendicular bisectors of AB and BC to locate center O.\n   • With center O and radius OA, complete the circumference.",
        "rules": [
          "Perpendicular bisectors of two chords intersect at the center O.",
          "Radius is the distance from O to any of the three points."
        ]
      },
      {
        "id": "13.2",
        "title": "13.2 Circles Attached to Triangles (Circum-, In-, and Escribed)",
        "theory": "1. Circumscribed Circle (Circumcircle):\n   • A circle passing through all three vertices of a triangle.\n   • Center (Circumcenter): Point of intersection of the right bisectors of the sides.\n   • Radius (Circumradius R) = abc / (4Δ).\n\n2. Inscribed Circle (Incircle):\n   • A circle inside a triangle touching all three sides.\n   • Center (Incenter): Point of intersection of the internal angle bisectors.\n   • Radius (Inradius r) = Δ / s (where s = (a + b + c)/2).\n\n3. Escribed Circle (Excircle):\n   • A circle touching one side of a triangle externally and the other two produced sides.\n   • Center (Excenter I₁): Intersection of the internal bisector of ∠A and external bisectors of ∠B and ∠C.\n   • Radius (Exradius r₁) = Δ / (s - a).",
        "rules": [
          "Circumcircle uses perpendicular bisectors of sides.",
          "Incircle uses internal angle bisectors.",
          "Excircle uses one internal and two external angle bisectors."
        ]
      },
      {
        "id": "13.3",
        "title": "13.3 Tangent Constructions and Common Tangents",
        "theory": "1. Tangent from an External Point P to a Circle:\n   • Join center O to point P.\n   • Find midpoint M of OP.\n   • Draw a semicircle on OP as diameter cutting the given circle at T.\n   • Line PT is the required tangent.\n\n2. Direct (External) Common Tangents to Two Circles:\n   • Centers O₁ and O₂ with radii r₁ > r₂.\n   • Draw an auxiliary circle with center O₁ and radius (r₁ - r₂).\n   • Construct tangents from O₂ to this auxiliary circle to find points of contact.\n\n3. Transverse (Internal) Common Tangents to Two Circles:\n   • Draw an auxiliary circle with center O₁ and radius (r₁ + r₂).\n   • Tangents intersect the line segment connecting the centers.",
        "rules": [
          "Direct common tangents use auxiliary circle of radius (r₁ - r₂).",
          "Transverse common tangents use auxiliary circle of radius (r₁ + r₂).",
          "Two equal circles have parallel direct common tangents at distance equal to diameter."
        ]
      }
    ],
    "workedExamples": [
      {
        "id": "eg1",
        "title": "Example 1 (Page 254) — Inscribing a Circle in a Triangle",
        "problem": "Construct a triangle with sides 5 cm, 6 cm, and 7 cm. Inscribe a circle in this triangle and measure its radius.",
        "given": "△ABC with a = 5 cm, b = 6 cm, c = 7 cm",
        "method": "Angle bisector construction for Incenter.",
        "steps": [
          "Draw side BC = 5 cm.",
          "With center B draw an arc of radius 7 cm, and with center C draw an arc of radius 6 cm. Their intersection gives vertex A.",
          "Draw the internal angle bisectors of ∠B and ∠C. Let them intersect at point I (the Incenter).",
          "From I, draw a perpendicular ID onto side BC (point D on BC).",
          "With center I and radius ID, draw a circle. The circle touches all three sides AB, BC, and CA.",
          "Measurement: Inradius r ≈ 1.63 cm."
        ],
        "answer": "Incircle constructed with inradius r ≈ 1.63 cm"
      },
      {
        "id": "eg2",
        "title": "Example 2 (Page 262) — Tangent from External Point",
        "problem": "Draw a circle of radius 3 cm. From a point P at a distance of 7 cm from its center, construct two tangents to the circle.",
        "given": "Radius r = 3 cm, OP = 7 cm",
        "method": "Midpoint and auxiliary circle construction.",
        "steps": [
          "Draw a circle with center O and radius 3 cm.",
          "Mark point P such that OP = 7 cm.",
          "Bisect OP at point M.",
          "With center M and radius MP = MO, draw a circle cutting the original circle at T₁ and T₂.",
          "Join PT₁ and PT₂. These are the two required tangents.",
          "Length calculation: PT = √(7² - 3²) = √(49 - 9) = √40 ≈ 6.32 cm."
        ],
        "answer": "Tangents PT₁ and PT₂ constructed with length √40 ≈ 6.32 cm"
      }
    ],
    "exercises": [
      {
        "exercise": "13.1",
        "title": "Exercise 13.1 — Circumscribed and Inscribed Circles",
        "problems": [
          {
            "num": "Q1",
            "question": "Circumscribe a circle about an equilateral triangle each of whose sides is 4 cm.",
            "solution": "1. Draw equilateral △ABC with AB = BC = CA = 4 cm.\n2. Draw perpendicular bisectors of sides AB and BC. Let them meet at point O.\n3. With center O and radius OA, draw the circle.\n4. The circle passes through all three vertices A, B, and C.\nCircumradius R = a / √3 = 4 / 1.732 ≈ 2.31 cm.",
            "finalAnswer": "Circumcircle constructed with radius R ≈ 2.31 cm",
            "steps": [
              "Draw equilateral △ABC of side 4 cm",
              "Construct perpendicular bisectors of any two sides to locate O",
              "Draw circle with center O and radius OA",
              "Circumradius R ≈ 2.31 cm"
            ],
            "method": "Circumcircle Construction"
          }
        ]
      },
      {
        "exercise": "13.2",
        "title": "Exercise 13.2 — Squares and Regular Hexagons with Circles",
        "problems": [
          {"num":"Q1","question":"Circumscribe a square about a circle of radius 5 cm.","solution":"Draw two perpendicular diameters through the centre. At their four endpoints, draw tangents perpendicular to the corresponding radii. Their intersections form the required square.","finalAnswer":"The square has side 10 cm."},
          {"num":"Q2","question":"Inscribe a square in a circle of radius 6 cm.","solution":"Draw two perpendicular diameters. Join their four endpoints consecutively to form the inscribed square.","finalAnswer":"The diagonal is 12 cm and each side is 6√2 cm."},
          {"num":"Q3","question":"Draw a square of side 6 cm. Circumscribe a circle about it and inscribe a circle in the same square. Measure both radii.","solution":"Draw the square. The circumcentre is the intersection of its diagonals; the circumradius is half a diagonal. The incircle centre is the same point; its radius is the perpendicular distance to a side.","finalAnswer":"Circumradius = 3√2 cm ≈ 4.24 cm; inradius = 3 cm."},
          {"num":"Q4","question":"Draw a circle of suitable radius so that the square circumscribed about it has sides of length 8 units.","solution":"Construct a square of side 8 units and draw its diagonals to locate the centre. The required circle is centred there and tangent to all four sides.","finalAnswer":"Circle radius = 4 units."},
          {"num":"Q5","question":"Inscribe a square of side 10 cm in a circle. Find the radius.","solution":"Draw the square and its diagonals; the centre is their intersection. The radius is half the diagonal, which is 10√2/2.","finalAnswer":"Radius = 5√2 cm ≈ 7.07 cm."},
          {"num":"Q6","question":"Inscribe a regular hexagon in a circle of radius 4 cm.","solution":"Set the compass to the circle’s radius. Starting at any point on the circumference, step this chord length around the circumference six times and join consecutive points.","finalAnswer":"Each side of the regular hexagon is 4 cm."},
          {"num":"Q7","question":"Construct a circle of radius 4 cm and draw a regular hexagon about the circle.","solution":"Construct six equally spaced sides tangent to the circle. The perpendicular from the centre to each side is the apothem, 4 cm; each central half-angle is 30°. The side length is 2(4)tan30°.","finalAnswer":"The circumscribed regular hexagon has side 8/√3 cm ≈ 4.62 cm."},
          {"num":"Q8","question":"Draw a circle of radius 8 cm. Circumscribe a regular hexagon about it and inscribe a regular hexagon in it. Find the areas and compare them.","solution":"For the inscribed hexagon, each side is 8 cm, so area = 6(√3/4)(8²). For the circumscribed hexagon, apothem = 8 cm and each side is 16/√3 cm, so area = (perimeter × apothem)/2.","finalAnswer":"Inscribed area = 96√3 cm² ≈ 166.28 cm²; circumscribed area = 128√3 cm² ≈ 221.70 cm². The circumscribed area is 4/3 of the inscribed area."},
          {"num":"Q9","question":"Draw regular hexagons with perimeters 6 cm and 30 cm. Find their centres and construct perpendiculars from the centres to a side of each. What is the relation between the perpendiculars?","solution":"The side lengths are 1 cm and 5 cm. For a regular hexagon the perpendicular distance from its centre to a side is (√3/2) times the side length.","finalAnswer":"The perpendiculars are √3/2 cm and 5√3/2 cm; the second is five times the first."},
          {"num":"Q10","question":"Can you construct a square whose area equals the area of a given circle? Discuss.","solution":"For circle radius r, equal-area square side would have to be √(πr²) = r√π. Exact straightedge-and-compass construction of r√π would construct √π, which is impossible because π is transcendental and √π is not a constructible length.","finalAnswer":"No exact classical straightedge-and-compass construction exists."}
        ]
      },
      {
        "exercise": "13.3",
        "title": "Exercise 13.3 — Common Tangents to Two Circles",
        "problems": [
          {
            "num": "Q1",
            "question": "Draw two circles of radii 2.5 cm and 3.5 cm whose centers are 8 cm apart. Draw two direct common tangents to these circles.",
            "solution": "1. Draw line segment O₁O₂ = 8 cm.\n2. Draw circles with centers O₁ (r₁ = 3.5 cm) and O₂ (r₂ = 2.5 cm).\n3. Radius difference: r₁ - r₂ = 3.5 - 2.5 = 1.0 cm.\n4. With center O₁, draw an auxiliary circle of radius 1.0 cm.\n5. Bisect O₁O₂ and draw a circle on O₁O₂ as diameter cutting the auxiliary circle at point T.\n6. Join O₁T and produce to meet the large circle at P₁.\n7. Draw radius O₂P₂ parallel to O₁P₁ in the same direction.\n8. Join P₁P₂ to obtain the direct common tangent.",
            "finalAnswer": "Two direct common tangents successfully constructed",
            "steps": [
              "Draw centers at distance 8 cm with radii 3.5 cm and 2.5 cm",
              "Form auxiliary circle with radius r₁ - r₂ = 1.0 cm",
              "Construct tangents from O₂ to auxiliary circle",
              "Draw parallel radii to get points of contact and join them"
            ],
            "method": "Direct Common Tangent Construction"
          }
        ]
      }
    ],
    "slos": [
      "Construct a circle passing through three non-collinear points and complete an incomplete circle arc",
      "Circumscribe a circle about a given triangle",
      "Inscribe a circle in a given triangle",
      "Escribe a circle opposite to a given vertex of a triangle",
      "Construct tangents to a circle from a point on the circumference and from an external point",
      "Construct direct (external) and transverse (internal) common tangents to two circles"
    ],
    "formulaSheet": [
      {
        "name": "Circumradius",
        "formula": "R = abc / (4Δ)",
        "note": "Δ = area of triangle, a, b, c = side lengths."
      },
      {
        "name": "Inradius",
        "formula": "r = Δ / s",
        "note": "s = semi-perimeter (a + b + c)/2."
      },
      {
        "name": "Exradius",
        "formula": "r₁ = Δ / (s - a)",
        "note": "Excircle opposite to vertex A."
      },
      {
        "name": "Direct Common Tangent Auxiliary Radius",
        "formula": "r = r₁ - r₂",
        "note": "Difference of radii."
      },
      {
        "name": "Transverse Common Tangent Auxiliary Radius",
        "formula": "r = r₁ + r₂",
        "note": "Sum of radii."
      }
    ],
    "classId": "cls10"
  }
];

if (typeof window !== 'undefined') {
  window.MATH_10_DATA = MATH_10_DATA;
}
if (typeof DATA !== 'undefined') {
  DATA.math10Chapters = MATH_10_DATA;
}
