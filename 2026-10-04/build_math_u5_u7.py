# -*- coding: utf-8 -*-
"""
SpaceBook - Units 5, 6, 7 Data Builder for Class 8 Mathematics
"""

def get_unit_5():
    return {
        "number": 5,
        "id": "unit-5",
        "title": "Sets",
        "titleUrdu": "سیٹ",
        "type": "chapter",
        "pageRange": "pp. 86–103",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 5 investigates advanced set theory: set builder notations, classifications (finite, infinite, empty, universal), subsets (proper ⊂, improper ⊆), and power sets P(A) containing 2^n elements. It demonstrates operations including union, intersection, difference, and complement, visualized through Venn diagrams, and provides rigorous proofs of De Morgan's laws: (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'.",
        "urduSummary": "یونٹ 5 سیٹ تھیوری کے اعلیٰ تصورات کا احاطہ کرتا ہے جن میں سیٹ بلڈر نوٹیشن، اقسام (محدود، لامحدود، خالی، کائناتی سیٹ)، ماتحت سیٹ (واجب اور غیر واجب) اور پاور سیٹ (P(A) = 2^n) شامل ہیں۔ اس میں یونین، تقاطع، فرق، اور تکملہ (Complement) کے عملی سوالات، وین ڈایاگرامز کے ذریعے ان کا اظہار، اور ڈی مورگن کے قوانین ((A ∪ B)' = A' ∩ B' اور (A ∩ B)' = A' ∪ B') کے باقاعدہ ثبوت شامل ہیں۔",
        "sections": [
            {
                "id": "5.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Express sets in descriptive, tabular, and set-builder notations.\n• Find subsets and write the power set of a set.\n• Perform set operations (union, intersection, difference, complement).\n• Verify commutative, associative, distributive, and De Morgan's laws using Venn diagrams.",
                "theory": "Core Competencies:\n1. Power Set: If set A has n elements, the power set P(A) contains 2^n subsets.\n2. De Morgan's Laws: (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'.\n3. Distributive Laws: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).",
                "paras": [
                    "Express sets in descriptive, tabular, and set-builder notations.",
                    "Determine all subsets and construct power sets.",
                    "Execute union, intersection, relative complement, and absolute complement.",
                    "Prove De Morgan's laws and distributive laws numerically and with Venn diagrams."
                ]
            },
            {
                "id": "5.1-subsets-power-sets",
                "title": "5.1 Subsets and Power Set",
                "heading": "Subsets and Power Set",
                "headingUrdu": "ماتحت سیٹ اور پاور سیٹ",
                "text": "• Proper Subset (⊂): If A ⊆ B and A ≠ B, A is a proper subset of B. Number of proper subsets = 2^n - 1.\n• Improper Subset: Every set is an improper subset of itself.\n• Power Set P(A): The set of all possible subsets of A. If n(A) = n, then n(P(A)) = 2^n.\n• Empty set ∅ is a subset of every set.",
                "theory": "Formula for Power Set:\nFor any finite set A with n elements:\nTotal subsets = 2^n\nProper subsets = 2^n - 1\nImproper subset = 1 (the set itself).",
                "paras": [
                    "The empty set is a subset of every set.",
                    "A proper subset contains fewer elements than the parent set.",
                    "The power set contains all possible subsets.",
                    "The total number of elements in P(A) is 2^n."
                ]
            },
            {
                "id": "5.2-de-morgans-laws",
                "title": "5.2 Operations & De Morgan's Laws",
                "heading": "Operations & De Morgan's Laws",
                "headingUrdu": "عملیات اور ڈی مورگن کے قوانین",
                "text": "• Universal Set (U): The overarching set containing all elements under consideration.\n• Complement A' = U - A.\n• De Morgan's Laws:\n1. (A ∪ B)' = A' ∩ B'\n2. (A ∩ B)' = A' ∪ B'",
                "theory": "Verification of De Morgan's Laws:\nLaw 1: The complement of the union equals the intersection of the complements.\nLaw 2: The complement of the intersection equals the union of the complements.",
                "paras": [
                    "Complement of a set is the elements in the universal set not present in the given set.",
                    "De Morgan's First Law states: (A ∪ B)' = A' ∩ B'.",
                    "De Morgan's Second Law states: (A ∩ B)' = A' ∪ B'."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-5-1",
                "title": "Example 1: Power Set Construction",
                "problem": "Find the power set of A = {1, 2, 3}.",
                "solution": "Here n(A) = 3, so n(P(A)) = 2³ = 8.\nSubsets:\n• 0-element subset: ∅\n• 1-element subsets: {1}, {2}, {3}\n• 2-element subsets: {1, 2}, {1, 3}, {2, 3}\n• 3-element subset: {1, 2, 3}\nP(A) = { ∅, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }."
            },
            {
                "id": "we-8-5-2",
                "title": "Example 2: Verification of De Morgan's Law",
                "problem": "If U = {1, 2, 3, 4, 5, 6}, A = {2, 4}, and B = {4, 6}, verify that (A ∪ B)' = A' ∩ B'.",
                "solution": "1. Left Hand Side (LHS):\nA ∪ B = {2, 4, 6}\n(A ∪ B)' = U - (A ∪ B) = {1, 3, 5}.\n2. Right Hand Side (RHS):\nA' = U - A = {1, 3, 5, 6}\nB' = U - B = {1, 2, 3, 5}\nA' ∩ B' = {1, 3, 5}.\nLHS = RHS = {1, 3, 5}. Hence proved."
            }
        ],
        "exercises": [
            {
                "exercise": "5.1",
                "title": "Exercise 5.1: Subsets & Power Sets",
                "answerKeyText": "Exercise 5.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Write all subsets of:\n(a) {a}\n(b) {x, y}\n(c) {1, 2, 3}",
                        "solution": "(a) Subsets of {a}: ∅, {a} (2 subsets)\n(b) Subsets of {x, y}: ∅, {x}, {y}, {x, y} (4 subsets)\n(c) Subsets of {1, 2, 3}: ∅, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} (8 subsets)"
                    },
                    {
                        "qNo": "2",
                        "question": "Write the power set P(B) for B = {-1, 1}.",
                        "solution": "P(B) = { ∅, {-1}, {1}, {-1, 1} }."
                    }
                ]
            },
            {
                "exercise": "5.2",
                "title": "Exercise 5.2: Set Operations & De Morgan's",
                "answerKeyText": "Exercise 5.2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "If U = {1, 2, 3, ..., 10}, A = {1, 3, 5, 7, 9}, B = {2, 3, 5, 7}, find:\n(a) A ∪ B (b) A ∩ B (c) A - B (d) A'",
                        "solution": "(a) A ∪ B = {1, 2, 3, 5, 7, 9}\n(b) A ∩ B = {3, 5, 7}\n(c) A - B = {1, 9}\n(d) A' = U - A = {2, 4, 6, 8, 10}"
                    },
                    {
                        "qNo": "2",
                        "question": "Verify (A ∩ B)' = A' ∪ B' for U = {1, 2, 3, 4, 5}, A = {1, 2, 3}, B = {3, 4}.",
                        "solution": "A ∩ B = {3} → (A ∩ B)' = {1, 2, 4, 5}.\nA' = {4, 5}, B' = {1, 2, 5} → A' ∪ B' = {1, 2, 4, 5}.\nLHS = RHS. Verified."
                    }
                ]
            },
            {
                "exercise": "Review 5",
                "title": "Review Exercise 5",
                "answerKeyText": "Review Exercise 5 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "If a set has 5 elements, how many subsets does its power set contain?",
                        "solution": "Number of elements in power set = 2⁵ = 32 subsets."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Power Set Formula",
                "formula": "n(P(A)) = 2^n",
                "note": "Total subsets of a set with n elements."
            },
            {
                "name": "De Morgan's Laws",
                "formula": "(A \\cup B)' = A' \\cap B', \\quad (A \\cap B)' = A' \\cup B'",
                "note": "Fundamental duality laws in set theory."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "If n(A) = 4, then the number of proper subsets of A is:", "options": ["A) 16", "B) 15", "C) 8", "D) 7"], "answer": "B) 15", "explanation": "2⁴ - 1 = 16 - 1 = 15."},
                {"q": "(A ∪ B)' is equal to:", "options": ["A) A' ∪ B'", "B) A' ∩ B'", "C) A ∩ B", "D) U"], "answer": "B) A' ∩ B'", "explanation": "De Morgan's first law."},
                {"q": "A - B is equal to:", "options": ["A) A ∩ B'", "B) A' ∩ B", "C) A ∪ B'", "D) B - A"], "answer": "A) A ∩ B'", "explanation": "By definition, elements in A and not in B."}
            ],
            "shortQuestions": [
                {"q": "What is the difference between a proper subset and an improper subset?", "answer": "A proper subset A ⊂ B contains some but not all elements of B (so A ≠ B and n(A) < n(B)). An improper subset of B is B itself (A = B)."},
                {"q": "Write De Morgan's Laws in mathematical symbols.", "answer": "1. (A ∪ B)' = A' ∩ B'\n2. (A ∩ B)' = A' ∪ B'"}
            ],
            "longQuestions": [
                {"q": "For U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, A = {2, 4, 6, 8, 10}, and B = {1, 2, 3, 4, 5, 6}, verify both of De Morgan's Laws.", "answer": "1. Verification of (A ∪ B)' = A' ∩ B':\n• A ∪ B = {1, 2, 3, 4, 5, 6, 8, 10}\n• (A ∪ B)' = {7, 9}\n• A' = {1, 3, 5, 7, 9}\n• B' = {7, 8, 9, 10}\n• A' ∩ B' = {7, 9}\nLHS = RHS = {7, 9}.\n2. Verification of (A ∩ B)' = A' ∪ B':\n• A ∩ B = {2, 4, 6}\n• (A ∩ B)' = {1, 3, 5, 7, 8, 9, 10}\n• A' ∪ B' = {1, 3, 5, 7, 8, 9, 10}\nLHS = RHS. Both laws verified."}
            ]
        }
    }


def get_unit_6():
    return {
        "number": 6,
        "id": "unit-6",
        "title": "Sequences and Algebra",
        "titleUrdu": "تسلسل اور الجبرا",
        "type": "chapter",
        "pageRange": "pp. 104–146",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 6 comprehensively develops sequences, polynomials, and algebraic manipulations. It begins with arithmetic sequences and finding the nth term (an = a + (n-1)d), classifies polynomials by degree and terms, and masters algebraic operations (addition, subtraction, multiplication, long division). It explores standard algebraic identities ((a±b)², a²-b², (a+b+c)², (a±b)³) and techniques of factorization (common factors, grouping, identities, and middle-term splitting).",
        "urduSummary": "یونٹ 6 الجبرا، کثیر رقمی جملوں (Polynomials)، اور حسابی تسلسل (Arithmetic Sequences) کا احاطہ کرتا ہے۔ اس میں تسلسل کا n-واں رُکن (an = a + (n-1)d) معلوم کرنا، کثیر رقمی جملوں کی جمع، تفریق، ضرب، اور طویل تقسیم شامل ہیں۔ مزید برآں، اہم الجبرائی کلیات ((a±b)²، a²-b²، (a+b+c)²، (a±b)³) اور تجزی (Factorization) کے مختلف طریقے تفصیلاً حل کیے گئے ہیں۔",
        "sections": [
            {
                "id": "6.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Find the general nth term of an arithmetic sequence.\n• Add, subtract, multiply, and divide polynomials.\n• Apply algebraic identities to expand expressions.\n• Factorize algebraic expressions using grouping, identities, and middle-term splitting.",
                "theory": "Core Competencies:\n1. Sequence Formula: a_n = a + (n - 1)d.\n2. Polynomial Division: Dividend = (Divisor × Quotient) + Remainder.\n3. Identities:\n• (a + b)² = a² + 2ab + b²\n• (a - b)² = a² - 2ab + b²\n• a² - b² = (a - b)(a + b)\n• (a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca\n• (a ± b)³ = a³ ± 3a²b + 3ab² ± b³.",
                "paras": [
                    "Identify arithmetic sequences and determine the nth term formula.",
                    "Perform four fundamental operations on algebraic polynomials.",
                    "Apply quadratic and cubic algebraic identities.",
                    "Factorize expressions completely using systematic methods."
                ]
            },
            {
                "id": "6.1-sequences",
                "title": "6.1 Number Sequences and the nth Term",
                "heading": "Number Sequences and the nth Term",
                "headingUrdu": "عددی تسلسل اور n-واں رُکن",
                "text": "A sequence is an ordered list of numbers following a specific mathematical pattern.\nIn an Arithmetic Sequence, the difference between consecutive terms is constant (d = common difference).\nThe nth term is given by:\na_n = a + (n - 1)d\nwhere 'a' is the first term and 'd' is the common difference.",
                "theory": "General Term Formula:\na_1 = a\na_2 = a + d\na_3 = a + 2d\n...\na_n = a + (n - 1)d.",
                "paras": [
                    "An arithmetic sequence has a constant common difference between successive terms.",
                    "The formula for the nth term is an = a + (n - 1)d.",
                    "This formula allows direct calculation of any distant term without listing intermediate terms."
                ]
            },
            {
                "id": "6.2-polynomial-operations",
                "title": "6.2 Operations on Polynomials",
                "heading": "Operations on Polynomials",
                "headingUrdu": "کثیر رقمی جملوں پر عملیات",
                "text": "• Degree of Polynomial: The highest power of the variable in the polynomial.\n• Addition & Subtraction: Combine like terms (terms with identical variable powers).\n• Multiplication: Multiply coefficients and add exponents of like variables.\n• Long Division: Arrange in descending powers; divide first term of dividend by first term of divisor.",
                "theory": "Properties of Polynomial Division:\nDividend P(x) = D(x) × Q(x) + R(x)\nwhere degree of R(x) < degree of D(x). If R(x) = 0, D(x) is an exact factor.",
                "paras": [
                    "Polynomials are classified by degree: linear, quadratic, cubic.",
                    "Like terms have identical variable components.",
                    "Long division systematically reduces polynomial degrees step by step."
                ]
            },
            {
                "id": "6.3-algebraic-identities",
                "title": "6.3 Algebraic Identities and Factorization",
                "heading": "Algebraic Identities & Factorization",
                "headingUrdu": "الجبرائی کلیات اور تجزی",
                "text": "Identities:\n1. (a + b)² = a² + 2ab + b²\n2. (a - b)² = a² - 2ab + b²\n3. a² - b² = (a - b)(a + b)\n4. (a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca\n5. (a + b)³ = a³ + 3ab(a + b) + b³\n6. (a - b)³ = a³ - 3ab(a - b) - b³\nFactorization converts polynomial sums into products of simpler polynomials.",
                "theory": "Methods of Factorization:\n1. Taking Common Factor: ax + ay = a(x + y)\n2. Grouping: ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)\n3. Difference of Squares: a² - b² = (a - b)(a + b)\n4. Middle-term Splitting: x² + (p + q)x + pq = (x + p)(x + q).",
                "paras": [
                    "Identities are equations true for all values of the variables.",
                    "Factorization reverses the process of algebraic expansion.",
                    "Trinomials of the form ax² + bx + c are factorized by splitting the linear middle term."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-6-1",
                "title": "Example 1: Finding the nth Term",
                "problem": "Find the 20th term of the arithmetic sequence: 4, 9, 14, 19, ...",
                "solution": "Here first term a = 4.\nCommon difference d = 9 - 4 = 5.\na_n = a + (n - 1)d\na_20 = 4 + (20 - 1) × 5 = 4 + 19 × 5 = 4 + 95 = 99."
            },
            {
                "id": "we-8-6-2",
                "title": "Example 2: Middle-Term Factorization",
                "problem": "Factorize x² - 7x + 12.",
                "solution": "We need two numbers p and q such that:\np + q = -7 and p × q = 12.\nThe numbers are -3 and -4.\nx² - 7x + 12 = x² - 3x - 4x + 12\n= x(x - 3) - 4(x - 3)\n= (x - 3)(x - 4)."
            }
        ],
        "exercises": [
            {
                "exercise": "6.1",
                "title": "Exercise 6.1: Sequences & nth Term",
                "answerKeyText": "Exercise 6.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the next three terms of: 2, 7, 12, 17, ...",
                        "solution": "Common difference d = 5.\n5th term = 17 + 5 = 22.\n6th term = 22 + 5 = 27.\n7th term = 27 + 5 = 32."
                    },
                    {
                        "qNo": "2",
                        "question": "Find the 50th term of the sequence 3, 7, 11, 15, ...",
                        "solution": "a = 3, d = 4.\na_50 = 3 + (50 - 1) × 4 = 3 + 49 × 4 = 3 + 196 = 199."
                    }
                ]
            },
            {
                "exercise": "6.5",
                "title": "Exercise 6.5: Polynomial Operations",
                "answerKeyText": "Exercise 6.5 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Multiply (2x + 3) by (3x - 4).",
                        "solution": "(2x + 3)(3x - 4) = 2x(3x - 4) + 3(3x - 4)\n= 6x² - 8x + 9x - 12\n= 6x² + x - 12."
                    },
                    {
                        "qNo": "2",
                        "question": "Divide (x² + 5x + 6) by (x + 2).",
                        "solution": "(x² + 5x + 6) = (x + 2)(x + 3).\nQuotient = x + 3, Remainder = 0."
                    }
                ]
            },
            {
                "exercise": "6.8",
                "title": "Exercise 6.8: Algebraic Identities",
                "answerKeyText": "Exercise 6.8 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Expand using identities:\n(a) (3x + 2y)²\n(b) (5a - 4b)²\n(c) (4x + 7)(4x - 7)",
                        "solution": "(a) (3x + 2y)² = (3x)² + 2(3x)(2y) + (2y)² = 9x² + 12xy + 4y².\n(b) (5a - 4b)² = (5a)² - 2(5a)(4b) + (4b)² = 25a² - 40ab + 16b².\n(c) (4x + 7)(4x - 7) = (4x)² - (7)² = 16x² - 49."
                    }
                ]
            },
            {
                "exercise": "6.10",
                "title": "Exercise 6.10: Factorization",
                "answerKeyText": "Exercise 6.10 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Factorize:\n(a) x² - 25\n(b) 4a² - 9b²\n(c) x² + 9x + 20",
                        "solution": "(a) x² - 5² = (x - 5)(x + 5)\n(b) (2a)² - (3b)² = (2a - 3b)(2a + 3b)\n(c) x² + 4x + 5x + 20 = x(x + 4) + 5(x + 4) = (x + 4)(x + 5)"
                    }
                ]
            },
            {
                "exercise": "Review 6",
                "title": "Review Exercise 6",
                "answerKeyText": "Review Exercise 6 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "If x + 1/x = 5, find the value of x² + 1/x².",
                        "solution": "Squaring both sides: (x + 1/x)² = 5²\nx² + 2 + 1/x² = 25\nx² + 1/x² = 25 - 2 = 23."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Arithmetic nth Term",
                "formula": "a_n = a + (n - 1)d",
                "note": "General term of an arithmetic progression."
            },
            {
                "name": "Difference of Squares",
                "formula": "a^2 - b^2 = (a - b)(a + b)",
                "note": "Key algebraic factorization formula."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "The 10th term of sequence 5, 8, 11, ... is:", "options": ["A) 32", "B) 35", "C) 38", "D) 29"], "answer": "A) 32", "explanation": "a10 = 5 + 9(3) = 5 + 27 = 32."},
                {"q": "(2a - 3b)² is equal to:", "options": ["A) 4a² - 9b²", "B) 4a² - 12ab + 9b²", "C) 4a² + 12ab + 9b²", "D) 4a² - 6ab + 9b²"], "answer": "B) 4a² - 12ab + 9b²", "explanation": "(2a)² - 2(2a)(3b) + (3b)²."},
                {"q": "Factors of x² - 16 are:", "options": ["A) (x - 4)(x - 4)", "B) (x + 4)(x - 4)", "C) (x + 8)(x - 2)", "D) (x - 16)(x + 1)"], "answer": "B) (x + 4)(x - 4)", "explanation": "Difference of squares."}
            ],
            "shortQuestions": [
                {"q": "Define the degree of a polynomial.", "answer": "The degree of a polynomial is the highest non-negative power of the variable present in any of its terms."},
                {"q": "Expand (a + b + c)².", "answer": "(a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca."}
            ],
            "longQuestions": [
                {"q": "If x - 1/x = 4, find the value of: (a) x² + 1/x² and (b) x⁴ + 1/x⁴.", "answer": "(a) Squaring x - 1/x = 4 gives (x - 1/x)² = 16 → x² - 2 + 1/x² = 16 → x² + 1/x² = 18.\n(b) Squaring x² + 1/x² = 18 gives (x² + 1/x²)² = 18² = 324 → x⁴ + 2 + 1/x⁴ = 324 → x⁴ + 1/x⁴ = 322."}
            ]
        }
    }


def get_unit_7():
    return {
        "number": 7,
        "id": "unit-7",
        "title": "Exponents and Laws of Exponents",
        "titleUrdu": "قوت نما اور قوت نما کے قوانین",
        "type": "chapter",
        "pageRange": "pp. 147–162",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 7 establishes the formal rules of indices (exponents) and scientific notation. It proves and applies the Product Law (a^m · a^n = a^(m+n)), Quotient Law (a^m / a^n = a^(m-n)), Power of a Power ((a^m)^n = a^(mn)), Power of a Product ((ab)^n = a^n b^n), Power of a Quotient ((a/b)^n = a^n / b^n), Zero Exponent (a^0 = 1), and Negative Exponent (a^(-n) = 1/a^n). It introduces standard scientific notation for astronomical and microscopic numbers.",
        "urduSummary": "یونٹ 7 قوت نما (Exponents) اور اس کے تمام بنیادی قوانین کی جامع وضاحت کرتا ہے۔ اس میں حاصلِ ضرب کا قانون (a^m · a^n = a^(m+n))، حاصلِ تقسیم کا قانون (a^m / a^n = a^(m-n))، قوت کی قوت کا قانون ((a^m)^n = a^(mn))، صفر قوت نما (a^0 = 1)، اور منفی قوت نما (a^(-n) = 1/a^n) شامل ہیں۔ مزید برآں، بہت بڑی اور بہت چھوٹی مقداروں کو سائنسی طریقہ تحریر (سائنٹیفک نوٹیشن) میں لکھنے کی مشقیں شامل ہیں۔",
        "sections": [
            {
                "id": "7.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Understand base and exponent in exponential expressions.\n• Apply laws of exponents to simplify expressions.\n• Convert very large and very small numbers into scientific notation and vice versa.",
                "theory": "Core Competencies:\n1. Base & Exponent: In a^n, 'a' is the base and 'n' is the exponent.\n2. Seven Laws of Indices.\n3. Scientific Notation: Expressing N in form A × 10^n where 1 ≤ A < 10 and n ∈ Z.",
                "paras": [
                    "Identify the base and index in exponential notation.",
                    "Apply all seven laws of exponents to simplify algebraic fractions.",
                    "Express physical and astronomical constants in standard scientific notation."
                ]
            },
            {
                "id": "7.1-laws-of-exponents",
                "title": "7.1 Laws of Exponents",
                "heading": "Laws of Exponents",
                "headingUrdu": "قوت نما کے قوانین",
                "text": "Laws:\n1. a^m × a^n = a^(m + n)\n2. a^m ÷ a^n = a^(m - n) (for a ≠ 0)\n3. (a^m)^n = a^(m × n)\n4. (a × b)^n = a^n × b^n\n5. (a / b)^n = a^n / b^n (b ≠ 0)\n6. a^0 = 1 (a ≠ 0)\n7. a^(-n) = 1 / a^n",
                "theory": "Exponents Rules Application:\n• Multiplication with same base: add powers.\n• Division with same base: subtract powers.\n• Any non-zero base raised to power 0 equals 1.\n• Negative exponents invert the base across the fraction bar.",
                "paras": [
                    "Powers add during multiplication of identical bases.",
                    "Powers subtract during division of identical bases.",
                    "Any non-zero quantity raised to power zero is identically one.",
                    "A negative power indicates the reciprocal of the positive power."
                ]
            },
            {
                "id": "7.2-scientific-notation",
                "title": "7.2 Scientific Notation",
                "heading": "Scientific Notation",
                "headingUrdu": "سائنسی طریقہ تحریر",
                "text": "Scientific notation writes numbers as A × 10^n, where 1 ≤ A < 10 and n is an integer.\n• Large numbers have positive powers of 10 (e.g. 150,000,000 = 1.5 × 10^8).\n• Small numbers have negative powers of 10 (e.g. 0.0000045 = 4.5 × 10^(-6)).",
                "theory": "Steps to convert to Scientific Notation:\n1. Move decimal point so that exactly one non-zero digit is to its left.\n2. Count the number of places shifted: shifted left → positive exponent n; shifted right → negative exponent -n.",
                "paras": [
                    "Scientific notation standardizes extremely large or minute numbers.",
                    "The coefficient A must satisfy 1 ≤ A < 10.",
                    "Moving the decimal to the left produces a positive exponent; to the right produces a negative exponent."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-7-1",
                "title": "Example 1: Simplifying with Laws of Exponents",
                "problem": "Simplify: (2³ × 2⁵) / 2⁴",
                "solution": "Numerator = 2^(3 + 5) = 2^8.\nExpression = 2^8 / 2^4 = 2^(8 - 4) = 2^4 = 16."
            },
            {
                "id": "we-8-7-2",
                "title": "Example 2: Scientific Notation",
                "problem": "Convert to scientific notation: (a) 384,000,000 m (distance to moon) (b) 0.000025 kg.",
                "solution": "(a) 384,000,000 = 3.84 × 10^8 m.\n(b) 0.000025 = 2.5 × 10^(-5) kg."
            }
        ],
        "exercises": [
            {
                "exercise": "7.1",
                "title": "Exercise 7.1: Exponent Laws",
                "answerKeyText": "Exercise 7.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Simplify using exponent laws:\n(a) x⁴ × x⁷\n(b) y¹² ÷ y⁵\n(c) (2³)²\n(d) 5⁰",
                        "solution": "(a) x^(4 + 7) = x¹¹\n(b) y^(12 - 5) = y⁷\n(c) 2^(3 × 2) = 2⁶ = 64\n(d) 5⁰ = 1"
                    }
                ]
            },
            {
                "exercise": "7.2",
                "title": "Exercise 7.2: Negative Exponents",
                "answerKeyText": "Exercise 7.2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Express with positive exponents:\n(a) x^(-3)\n(b) 2^(-4)\n(c) (a / b)^(-2)",
                        "solution": "(a) 1 / x³\n(b) 1 / 2⁴ = 1 / 16\n(c) (b / a)² = b² / a²"
                    }
                ]
            },
            {
                "exercise": "7.3",
                "title": "Exercise 7.3: Scientific Notation",
                "answerKeyText": "Exercise 7.3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Write in scientific notation:\n(a) 57,000,000\n(b) 0.00064\n(c) 9,800,000",
                        "solution": "(a) 5.7 × 10⁷\n(b) 6.4 × 10^(-4)\n(c) 9.8 × 10⁶"
                    }
                ]
            },
            {
                "exercise": "Review 7",
                "title": "Review Exercise 7",
                "answerKeyText": "Review Exercise 7 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Simplify: (x³ y⁴)² / (x² y³)",
                        "solution": "= (x⁶ y⁸) / (x² y³) = x^(6 - 2) y^(8 - 3) = x⁴ y⁵."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Laws of Indices",
                "formula": "a^m a^n = a^{m+n}, \\quad \\frac{a^m}{a^n} = a^{m-n}, \\quad (a^m)^n = a^{mn}, \\quad a^0 = 1",
                "note": "Standard exponential arithmetic."
            },
            {
                "name": "Scientific Notation",
                "formula": "N = A \\times 10^n \\quad (1 \\le A < 10, \\, n \\in \\mathbb{Z})",
                "note": "Standard scientific format."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "The value of 7⁰ is:", "options": ["A) 0", "B) 7", "C) 1", "D) Undefined"], "answer": "C) 1", "explanation": "Any non-zero number to power 0 equals 1."},
                {"q": "(3²)³ is equal to:", "options": ["A) 3⁵", "B) 3⁶", "C) 3⁸", "D) 9²"], "answer": "B) 3⁶", "explanation": "Power of power multiplies: 2 × 3 = 6."},
                {"q": "0.0078 in scientific notation is:", "options": ["A) 78 × 10^(-4)", "B) 7.8 × 10^(-3)", "C) 7.8 × 10³", "D) 0.78 × 10^(-2)"], "answer": "B) 7.8 × 10^(-3)", "explanation": "Decimal shifts 3 places to the right: 7.8 × 10^(-3)."}
            ],
            "shortQuestions": [
                {"q": "Prove that a⁰ = 1 using the quotient law of exponents.", "answer": "By quotient law, a^m / a^m = a^(m - m) = a⁰. But any non-zero number divided by itself equals 1 (a^m / a^m = 1). Therefore, a⁰ = 1."},
                {"q": "What is the requirement for the number A in standard scientific notation A × 10^n?", "answer": "The coefficient A must satisfy 1 ≤ A < 10, meaning there must be exactly one non-zero digit before the decimal point."}
            ],
            "longQuestions": [
                {"q": "Simplify: [(2a³ b²)³ × (3a² b)⁴] / [6(ab)⁵] and express the final answer in terms of positive exponents.", "answer": "1. Numerator:\n• (2a³ b²)³ = 2³ a^(3×3) b^(2×3) = 8 a⁹ b⁶\n• (3a² b)⁴ = 3⁴ a^(2×4) b⁴ = 81 a⁸ b⁴\n• Product = (8 × 81) a^(9+8) b^(6+4) = 648 a¹⁷ b¹⁰\n2. Denominator:\n• 6 (ab)⁵ = 6 a⁵ b⁵\n3. Division:\n• (648 / 6) a^(17 - 5) b^(10 - 5) = 108 a¹² b⁵."}
            ]
        }
    }

print("Units 5, 6, 7 defined successfully.")
