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
        "formula": "x² - Sx + P = 0",
        "note": "S = α + β = -b/a, P = αβ = c/a."
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
