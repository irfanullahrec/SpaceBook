# -*- coding: utf-8 -*-
"""
SpaceBook - Units 2, 3, 4 Data Builder for Class 8 Mathematics
"""

def get_unit_2():
    return {
        "number": 2,
        "id": "unit-2",
        "title": "Real Numbers",
        "titleUrdu": "حقیقی اعداد",
        "type": "chapter",
        "pageRange": "pp. 8–32",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 2 establishes the complete system of Real Numbers (R = Q ∪ Q'). It classifies decimal expansions into terminating, non-terminating recurring (rational numbers Q), and non-terminating non-recurring (irrational numbers Q'). It demonstrates representing real numbers on a number line, calculating absolute values |a|, ordering properties (<, >, =), and verifying fundamental algebraic properties (commutative, associative, distributive, additive/multiplicative identities and inverses).",
        "urduSummary": "یونٹ 2 حقیقی اعداد (R = Q ∪ Q') کے مکمل نظام کی تفہیم فراہم کرتا ہے۔ یہ اعشاری اعداد کی تقسیم مختتم (terminating)، غیر مختتم متوالی (recurring rational)، اور غیر مختتم غیر متوالی (non-recurring irrational) میں کرتا ہے۔ اس یونٹ میں عددی خط پر حقیقی اعداد کا اظہار، مطلق قیمت (|a|)، ترتیب کے خصائص، اور بنیادی الجبرائی خواص (خاصیت مبادلہ، تلازم، اور تقسیمی) شامل ہیں۔",
        "sections": [
            {
                "id": "2.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Differentiate between rational and irrational numbers.\n• Recognize terminating, non-terminating, recurring, and non-recurring decimals.\n• Represent real numbers on a number line and compute absolute value.\n• Demonstrate ordering and fundamental algebraic properties of real numbers.",
                "theory": "Core SLOs:\n1. Classify numbers into Rational (Q) and Irrational (Q') sets.\n2. Apply the terminating decimal rule: a reduced fraction p/q terminates iff the prime factors of q are only 2, 5, or both.\n3. Understand absolute value as geometric distance from the origin: |a| ≥ 0.",
                "paras": [
                    "After completing this unit, students will be able to:",
                    "• Differentiate between rational and irrational numbers.",
                    "• Recognize terminating and non-terminating decimals.",
                    "• Represent real numbers on a number line and recognize absolute value.",
                    "• Apply algebraic properties: closure, commutative, associative, distributive, identity, and inverse."
                ]
            },
            {
                "id": "2.1-decimals",
                "title": "2.1 Types of Decimal Numbers",
                "heading": "Types of Decimal Numbers",
                "headingUrdu": "اعشاری اعداد کی اقسام",
                "text": "1. Terminating Decimals: Decimals having a finite number of decimal digits after the decimal point (e.g. 7/8 = 0.875).\n2. Non-Terminating Decimals: Decimals where division never ends (e.g. 1/3 = 0.333...).\nRule: If a reduced rational number in standard form p/q has no prime factors in q other than 2 or 5, it is a terminating decimal. Otherwise, it is non-terminating.",
                "theory": "Decimal Classification:\n• Terminating Decimals: Remainder becomes zero (e.g., 3/4 = 0.75, 11/10 = 1.1).\n• Non-terminating Recurring Decimals: Remainder never becomes zero; a digit or block of digits repeats indefinitely (e.g., 2/3 = 0.666..., 1/7 = 0.142857142857...).\n• Non-terminating Non-recurring Decimals: Digits continue infinitely without repeating any pattern (e.g., √2 = 1.4142135..., π = 3.1415926...). These are IRRATIONAL numbers.",
                "paras": [
                    "Terminating decimal numbers have a finite number of digits after the decimal point.",
                    "Non-terminating decimal numbers have an infinite number of digits after the decimal point.",
                    "Recurring decimals repeat a digit or block of digits periodically.",
                    "Non-recurring non-terminating decimals do not repeat any periodic pattern and represent irrational numbers."
                ]
            },
            {
                "id": "2.2-rational-irrational",
                "title": "2.2 Rational and Irrational Numbers",
                "heading": "Rational and Irrational Numbers",
                "headingUrdu": "ناطق اور غیر ناطق اعداد",
                "text": "• Rational Numbers (Q): Any number that can be expressed in the form p/q, where p, q ∈ Z and q ≠ 0.\n• Irrational Numbers (Q'): Any real number that cannot be written in the form p/q. Their decimal form is non-terminating and non-recurring.\n• Real Numbers (R): The union of all rational and irrational numbers: R = Q ∪ Q' and Q ∩ Q' = ∅.",
                "theory": "The Real Number Hierarchy:\nNatural Numbers (N) ⊂ Whole Numbers (W) ⊂ Integers (Z) ⊂ Rational Numbers (Q) ⊂ Real Numbers (R).\nIrrational numbers (Q') include square roots of non-perfect squares (√2, √3, √5, √7), mathematical constants (π, e), and all non-terminating non-repeating decimals.",
                "paras": [
                    "A rational number can be expressed as a quotient of two integers p/q with q ≠ 0.",
                    "An irrational number cannot be expressed as p/q.",
                    "The set of real numbers R is the union of rational and irrational numbers.",
                    "Square roots of prime numbers are always irrational."
                ]
            },
            {
                "id": "2.3-absolute-properties",
                "title": "2.3 Absolute Value and Properties of Real Numbers",
                "heading": "Absolute Value and Properties of Real Numbers",
                "headingUrdu": "مطلق قیمت اور حقیقی اعداد کی خصوصیات",
                "text": "• Absolute Value |a|: The distance of real number 'a' from 0 on the number line. |a| = a if a ≥ 0, and |a| = -a if a < 0. Always |a| ≥ 0.\n• Properties of Real Numbers under Addition and Multiplication:\n1. Commutative: a + b = b + a and a × b = b × a\n2. Associative: (a + b) + c = a + (b + c) and (ab)c = a(bc)\n3. Distributive: a(b + c) = ab + ac\n4. Identities: 0 is additive identity (a + 0 = a); 1 is multiplicative identity (a × 1 = a)\n5. Inverses: Additive inverse of a is -a; Multiplicative inverse of a (a ≠ 0) is 1/a.",
                "theory": "Mathematical Summary of Real Number Axioms:\n• Closure: a + b ∈ R and ab ∈ R for all a, b ∈ R.\n• Commutative Property: a + b = b + a; ab = ba.\n• Associative Property: (a + b) + c = a + (b + c); (ab)c = a(bc).\n• Distributive Property of Multiplication over Addition: a(b + c) = ab + ac.\n• Identity Elements: Additive identity = 0; Multiplicative identity = 1.\n• Inverse Elements: Additive inverse = -a; Multiplicative inverse = 1/a (for a ≠ 0).",
                "paras": [
                    "The absolute value of a real number is its distance from zero on the number line.",
                    "The absolute value is always non-negative: |x| ≥ 0.",
                    "Real numbers satisfy commutative, associative, and distributive laws.",
                    "Zero is the additive identity and one is the multiplicative identity."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-2-1",
                "title": "Example 1: Terminating vs Non-Terminating",
                "problem": "Without actual division, determine whether 7/250 and 11/14 are terminating or non-terminating decimals.",
                "solution": "1. For 7/250: Denominator = 250 = 2 × 5³. Prime factors are only 2 and 5. Therefore, 7/250 is a TERMINATING decimal (7/250 = 0.028).\n2. For 11/14: Denominator = 14 = 2 × 7. Since it contains 7 (a prime factor other than 2 or 5), 11/14 is a NON-TERMINATING decimal."
            },
            {
                "id": "we-8-2-2",
                "title": "Example 2: Absolute Value Evaluation",
                "problem": "Evaluate: (a) |-15| (b) |7.8| (c) -|-12| (d) |5 - 9|",
                "solution": "(a) |-15| = 15\n(b) |7.8| = 7.8\n(c) -|-12| = -(12) = -12\n(d) |5 - 9| = |-4| = 4"
            }
        ],
        "exercises": [
            {
                "exercise": "2.1",
                "title": "Exercise 2.1",
                "answerKeyText": "Exercise 2.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Separate terminating and non-terminating decimals without actual division:\n(a) 13/8 (b) 7/12 (c) 9/20 (d) 5/6 (e) 17/25 (f) 19/30 (g) 3/16 (h) 22/7",
                        "solution": "(a) 13/8: 8 = 2³ → Terminating\n(b) 7/12: 12 = 2² × 3 (contains 3) → Non-terminating\n(c) 9/20: 20 = 2² × 5 → Terminating\n(d) 5/6: 6 = 2 × 3 → Non-terminating\n(e) 17/25: 25 = 5² → Terminating\n(f) 19/30: 30 = 2 × 3 × 5 → Non-terminating\n(g) 3/16: 16 = 2⁴ → Terminating\n(h) 22/7: Denominator has 7 → Non-terminating"
                    },
                    {
                        "qNo": "2",
                        "question": "Convert into decimals and state whether recurring or non-recurring:\n(a) 2/3 (b) 15/4 (c) 1/7 (d) 11/8 (e) 5/6 (f) 13/8",
                        "solution": "(a) 2/3 = 0.666... → Recurring\n(b) 15/4 = 3.75 → Terminating (Non-recurring)\n(c) 1/7 = 0.142857142857... → Recurring\n(d) 11/8 = 1.375 → Terminating (Non-recurring)\n(e) 5/6 = 0.8333... → Recurring\n(f) 13/8 = 1.625 → Terminating (Non-recurring)"
                    }
                ]
            },
            {
                "exercise": "2.2",
                "title": "Exercise 2.2",
                "answerKeyText": "Exercise 2.2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Classify the following into Rational and Irrational numbers:\n(a) √4 (b) √7 (c) 3/11 (d) π (e) 0.35 (f) √16 (g) √23 (h) 2.71828...",
                        "solution": "(a) √4 = 2 = 2/1 → Rational\n(b) √7: 7 is not a perfect square → Irrational\n(c) 3/11: Quotient of integers → Rational\n(d) π: Non-terminating non-repeating → Irrational\n(e) 0.35 = 35/100 → Rational\n(f) √16 = 4 → Rational\n(g) √23: Not a perfect square → Irrational\n(h) 2.71828...: Non-repeating infinite decimal → Irrational"
                    }
                ]
            },
            {
                "exercise": "2.3",
                "title": "Exercise 2.3",
                "answerKeyText": "Exercise 2.3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the absolute value of each of the following:\n(a) -9 (b) 3.4 (c) -8.1 (d) 0 (e) -25/3 (f) 14",
                        "solution": "(a) |-9| = 9\n(b) |3.4| = 3.4\n(c) |-8.1| = 8.1\n(d) |0| = 0\n(e) |-25/3| = 25/3\n(f) |14| = 14"
                    }
                ]
            },
            {
                "exercise": "2.4",
                "title": "Exercise 2.4",
                "answerKeyText": "Exercise 2.4 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Name the property used in each statement:\n(a) 5 + 7 = 7 + 5\n(b) 3 × (4 × 5) = (3 × 4) × 5\n(c) 8 × (2 + 9) = 8 × 2 + 8 × 9\n(d) 15 + 0 = 15\n(e) 9 × (1/9) = 1\n(f) 6 + (-6) = 0",
                        "solution": "(a) Commutative property of addition\n(b) Associative property of multiplication\n(c) Distributive property of multiplication over addition\n(d) Additive identity property\n(e) Multiplicative inverse property\n(f) Additive inverse property"
                    },
                    {
                        "qNo": "2",
                        "question": "Find the additive and multiplicative inverse of:\n(a) 10 (b) -25 (c) 3/4 (d) -7/9",
                        "solution": "(a) 10: Additive inverse = -10, Multiplicative inverse = 1/10\n(b) -25: Additive inverse = 25, Multiplicative inverse = -1/25\n(c) 3/4: Additive inverse = -3/4, Multiplicative inverse = 4/3\n(d) -7/9: Additive inverse = 7/9, Multiplicative inverse = -9/7"
                    }
                ]
            },
            {
                "exercise": "Review 2",
                "title": "Review Exercise 2",
                "answerKeyText": "Review Exercise 2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Choose the correct option:\n(i) The number √5 is: (a) Rational (b) Irrational (c) Integer (d) Natural\n(ii) The multiplicative inverse of -3/5 is: (a) 3/5 (b) -5/3 (c) 5/3 (d) 1\n(iii) | -18 | is equal to: (a) -18 (b) 18 (c) 0 (d) ±18",
                        "solution": "(i) (b) Irrational\n(ii) (b) -5/3\n(iii) (b) 18"
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Absolute Value",
                "formula": "|a| = \\begin{cases} a & \\text{if } a \\ge 0 \\\\ -a & \\text{if } a < 0 \\end{cases}",
                "note": "Distance from origin; always non-negative."
            },
            {
                "name": "Terminating Decimal Condition",
                "formula": "q = 2^m \\times 5^n \\quad (m, n \\in \\mathbb{W})",
                "note": "A reduced rational fraction p/q terminates if and only if prime factors of q are strictly 2 and/or 5."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "Which of the following numbers is irrational?", "options": ["A) 0.75", "B) √9", "C) √11", "D) -4/7"], "answer": "C) √11", "explanation": "11 is a prime number and not a perfect square, so √11 is non-terminating and non-recurring."},
                {"q": "The additive identity in real numbers is:", "options": ["A) 1", "B) 0", "C) -1", "D) Any real number"], "answer": "B) 0", "explanation": "a + 0 = a for any real number a."},
                {"q": "The value of |-9.5| + |9.5| is:", "options": ["A) 0", "B) 19", "C) -19", "D) 9.5"], "answer": "B) 19", "explanation": "9.5 + 9.5 = 19."}
            ],
            "shortQuestions": [
                {"q": "Why is 22/7 a rational number while π is irrational?", "answer": "22/7 is expressed as the ratio of two integers (p/q with q ≠ 0), so it is rational (with a repeating decimal expansion). π is the exact ratio of a circle's circumference to diameter, which is a non-terminating non-repeating decimal, making it irrational. 22/7 is only an approximation of π."},
                {"q": "State the Distributive Property of Multiplication over Addition.", "answer": "For any three real numbers a, b, c: a × (b + c) = (a × b) + (a × c)."}
            ],
            "longQuestions": [
                {"q": "Verify the Associative Property of Addition and Multiplication for a = -1/2, b = 2/3, and c = 5/6.", "answer": "1. Addition: (a + b) + c = (-1/2 + 2/3) + 5/6 = (-3/6 + 4/6) + 5/6 = 1/6 + 5/6 = 6/6 = 1.\na + (b + c) = -1/2 + (2/3 + 5/6) = -1/2 + (4/6 + 5/6) = -1/2 + 9/6 = -3/6 + 9/6 = 6/6 = 1.\nBoth sides equal 1. Verified.\n2. Multiplication: (a × b) × c = (-1/2 × 2/3) × 5/6 = -1/3 × 5/6 = -5/18.\na × (b × c) = -1/2 × (2/3 × 5/6) = -1/2 × 10/18 = -10/36 = -5/18.\nBoth sides equal -5/18. Verified."}
            ]
        }
    }


def get_unit_3():
    return {
        "number": 3,
        "id": "unit-3",
        "title": "Financial Arithmetic",
        "titleUrdu": "مالیاتی حساب",
        "type": "chapter",
        "pageRange": "pp. 33–59",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 3 covers financial mathematics in commerce and Islamic jurisprudence: compound proportion (direct and inverse relationships involving multiple quantities), commercial profit and loss percentages, trade discount, commercial bank profit/mark-up rates, partnership business profit distribution, Islamic principles of inheritance (shares of widow, sons, and daughters), and tax calculations (Property Tax, General Sales Tax, and Income Tax).",
        "urduSummary": "یونٹ 3 تجارتی اور اسلامی فقہ پر مبنی مالیاتی حساب کا احاطہ کرتا ہے۔ اس میں مرکب تناسب (براہ راست اور معکوس تناسب)، نفع اور نقصان کا فیصد، تجارتی چھوٹ (ڈسکاؤنٹ)، بینک مارک اپ، کاروباری شراکت داری میں نفع کی تقسیم، اسلامی وراثت کے قوانین (بیوہ، بیٹیوں اور بیٹوں کے حصے)، اور ٹیکسوں (پراپرٹی ٹیکس، جنرل سیلز ٹیکس اور انکم ٹیکس) کا مکمل حساب کتاب شامل ہے۔",
        "sections": [
            {
                "id": "3.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Solve problems involving compound proportion.\n• Calculate profit, loss, profit percentage, and loss percentage.\n• Solve problems on discount and commercial banking transactions.\n• Distribute inheritance according to Islamic law.\n• Calculate partnership profit/loss and various taxes (GST, Property Tax, Income Tax).",
                "theory": "Financial Arithmetic core competencies:\n1. Compound Proportion: Analyzing problems involving three or more quantities with mixed direct and inverse variations.\n2. Business Profit & Loss: Cost Price (CP), Sale Price (SP), Profit = SP - CP, Loss = CP - SP.\n3. Islamic Inheritance: Applying legal Quranic shares: Widow (1/8 if children exist, 1/4 if no children), remainder to children with sons receiving twice the share of daughters (2:1).",
                "paras": [
                    "Solve problems involving compound proportion.",
                    "Calculate profit, loss, profit percentage, and loss percentage.",
                    "Solve problems on discount and banking transactions.",
                    "Distribute inheritance according to Islamic law.",
                    "Calculate partnership distribution and taxes (GST, property tax, income tax)."
                ]
            },
            {
                "id": "3.1-compound-proportion",
                "title": "3.1 Compound Proportion",
                "heading": "Compound Proportion",
                "headingUrdu": "مرکب تناسب",
                "text": "Compound proportion is a relationship between two or more proportions. When solving compound proportion problems:\n1. Identify direct variations (both quantities increase or decrease together).\n2. Identify inverse variations (as one quantity increases, the other decreases).\n3. Set up the proportional equation and solve for the unknown.",
                "theory": "Compound Proportion Methodology:\nLet unknown quantity be x. Arrange variables in tabular columns:\n• Arrow pointing towards x.\n• For directly proportional quantities, arrow points in the same direction.\n• For inversely proportional quantities, arrow points in the opposite direction.\nEquate ratio of tails to heads and solve for x.",
                "paras": [
                    "Compound proportion relates three or more quantities involving direct or inverse variations.",
                    "Direct proportion occurs when an increase in one quantity produces a proportionate increase in another.",
                    "Inverse proportion occurs when an increase in one quantity causes a proportionate decrease in another."
                ]
            },
            {
                "id": "3.2-profit-loss-discount",
                "title": "3.2 Profit, Loss, and Discount",
                "heading": "Profit, Loss, and Discount",
                "headingUrdu": "نفع، نقصان اور چھوٹ (ڈسکاؤنٹ)",
                "text": "• Profit = Sale Price (SP) - Cost Price (CP) (when SP > CP)\n• Loss = Cost Price (CP) - Sale Price (SP) (when CP > SP)\n• Profit % = (Profit / CP) × 100\n• Loss % = (Loss / CP) × 100\n• Discount = Marked Price (MP) - Sale Price (SP)\n• Discount % = (Discount / MP) × 100",
                "theory": "Commercial Trading Formulas:\n• Profit % and Loss % are ALWAYS calculated on the Cost Price (CP).\n• Discount % is ALWAYS calculated on the Marked Price (MP).\n• Sale Price with Discount: SP = MP × (100 - Discount %) / 100.\n• Sale Price with Profit: SP = CP × (100 + Profit %) / 100.\n• Sale Price with Loss: SP = CP × (100 - Loss %) / 100.",
                "paras": [
                    "Profit occurs when selling price exceeds cost price.",
                    "Loss occurs when cost price exceeds selling price.",
                    "Profit and loss percentages are calculated relative to cost price.",
                    "Discount is the concession given on marked price."
                ]
            },
            {
                "id": "3.3-inheritance-partnership",
                "title": "3.3 Islamic Inheritance and Partnership",
                "heading": "Islamic Inheritance and Partnership",
                "headingUrdu": "اسلامی وراثت اور شراکت داری",
                "text": "• Islamic Inheritance: Before distributing the deceased person's wealth:\n1. Pay funeral expenses.\n2. Pay outstanding debts.\n3. Pay legal bequests (wasiyyat, up to 1/3 of remaining wealth).\n4. Distribute remaining inheritance: Widow receives 1/8 (if children exist) or 1/4 (if no children). Remaining wealth is divided among children such that each son gets twice the share of each daughter (2 : 1 ratio).\n• Partnership: Profit or loss is shared in direct ratio of the invested capital and time period.",
                "theory": "Rules of Inheritance:\nNet Estate = Total Estate - (Funeral Expenses + Debts + Bequests)\n• Widow's Share: 1/8 of Net Estate (in presence of children).\n• Residue = Net Estate - Widow's Share.\n• Ratio: Each Son : Each Daughter = 2 : 1.\nPartnership Profit Sharing:\nShare = (Partner's Investment Ratio / Sum of Ratios) × Total Profit.",
                "paras": [
                    "Before inheritance distribution, burial expenses and debts must be paid.",
                    "The widow receives 1/8 of the remaining estate if there are children.",
                    "Sons receive twice the share of daughters (ratio 2 : 1).",
                    "Partners share profit or loss in direct proportion to their capital contributions."
                ]
            },
            {
                "id": "3.4-taxes",
                "title": "3.4 Taxes (Property Tax, GST, Income Tax)",
                "heading": "Taxes (Property Tax, GST, Income Tax)",
                "headingUrdu": "ٹیکس (پراپرٹی ٹیکس، جنرل سیلز ٹیکس، انکم ٹیکس)",
                "text": "• Property Tax: Tax paid on the value of property owned.\n  Property Tax = Tax Rate × Property Value.\n• General Sales Tax (GST): Tax charged on the sale of goods and services.\n  GST Amount = (GST Rate / 100) × Price of item.\n• Income Tax: Tax levied by the government directly on annual personal income above the tax exemption threshold.",
                "theory": "Taxation Calculation:\n• Net Price = Marked Price + GST.\n• Taxable Income = Annual Income - Exemption Limit.\n• Income Tax = Taxable Income × Income Tax Rate.",
                "paras": [
                    "Property tax is calculated as a percentage of property value.",
                    "General sales tax is added to the price of commodities.",
                    "Income tax is levied on earnings exceeding the legally exempted threshold."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-3-1",
                "title": "Example 1: Compound Proportion",
                "problem": "If 15 workers can build a 120-meter wall in 8 days, how many workers are needed to build a 300-meter wall in 10 days?",
                "solution": "Workers (w), Wall length (L), Days (d).\nWorkers is directly proportional to Wall Length, and inversely proportional to Days.\nw2 = w1 × (L2 / L1) × (d1 / d2)\nw2 = 15 × (300 / 120) × (8 / 10)\n= 15 × (2.5) × (0.8) = 15 × 2 = 30 workers."
            },
            {
                "id": "we-8-3-2",
                "title": "Example 2: Islamic Inheritance",
                "problem": "A man dies leaving an estate of Rs 800,000. He leaves behind a widow, 2 sons, and 1 daughter. Distribute the inheritance after clearing a debt of Rs 80,000.",
                "solution": "1. Net Estate = Rs 800,000 - Rs 80,000 = Rs 720,000.\n2. Widow's share (1/8) = (1/8) × 720,000 = Rs 90,000.\n3. Remaining estate = Rs 720,000 - Rs 90,000 = Rs 630,000.\n4. Children's shares:\n2 sons (2 × 2 = 4 parts) + 1 daughter (1 part) = 5 parts.\nValue of 1 part = 630,000 / 5 = Rs 126,000.\n• Daughter's share = 1 × 126,000 = Rs 126,000.\n• Each son's share = 2 × 126,000 = Rs 252,000."
            }
        ],
        "exercises": [
            {
                "exercise": "3.1",
                "title": "Exercise 3.1: Compound Proportion",
                "answerKeyText": "Exercise 3.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "If 30 men consume 60 kg of flour in 15 days, how many kilograms of flour will 40 men consume in 20 days?",
                        "solution": "Flour is directly proportional to men and days.\nFlour = 60 × (40 / 30) × (20 / 15)\n= 60 × (4/3) × (4/3) = 60 × 16 / 9 = 106.67 kg (or approx 106 2/3 kg)."
                    },
                    {
                        "qNo": "2",
                        "question": "A factory produces 22,500 pens in 12 days working 8 hours a day. How many pens will be produced in 10 days working 9 hours a day?",
                        "solution": "Pens = 22,500 × (10 / 12) × (9 / 8)\n= 22,500 × (5/6) × (9/8) = 22,500 × (45 / 48) = 21,093.75 (approx 21,094 pens)."
                    }
                ]
            },
            {
                "exercise": "3.2",
                "title": "Exercise 3.2: Profit and Loss",
                "answerKeyText": "Exercise 3.2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find profit or loss percentage:\n(a) CP = Rs 390, SP = Rs 380\n(b) CP = Rs 5800, SP = Rs 5600\n(c) CP = Rs 3700, SP = Rs 3760\n(d) CP = Rs 400, SP = Rs 680",
                        "solution": "(a) Loss = 390 - 380 = Rs 10. Loss % = (10/390) × 100 = 2.56% loss.\n(b) Loss = 5800 - 5600 = Rs 200. Loss % = (200/5800) × 100 = 3.45% loss.\n(c) Profit = 3760 - 3700 = Rs 60. Profit % = (60/3700) × 100 = 1.62% profit.\n(d) Profit = 680 - 400 = Rs 280. Profit % = (280/400) × 100 = 70% profit."
                    }
                ]
            },
            {
                "exercise": "3.3",
                "title": "Exercise 3.3: Discount and Banking",
                "answerKeyText": "Exercise 3.3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "A shirt marked at Rs 800 is sold at an 8% discount. Find the discount amount and selling price.",
                        "solution": "Discount = 8% of 800 = (8/100) × 800 = Rs 64.\nSale Price = 800 - 64 = Rs 736."
                    }
                ]
            },
            {
                "exercise": "3.4",
                "title": "Exercise 3.4: Inheritance & Partnership",
                "answerKeyText": "Exercise 3.4 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "A deceased person leaves an estate of Rs 150,000. He leaves behind a widow, 1 son, and 1 daughter. Distribute the property.",
                        "solution": "1. Widow's share (1/8) = 150,000 / 8 = Rs 18,750.\n2. Remaining estate = 150,000 - 18,750 = Rs 131,250.\n3. Son and daughter ratio = 2 : 1 (Total = 3 parts).\n• Value of 1 part = 131,250 / 3 = Rs 43,750.\n• Daughter's share = Rs 43,750.\n• Son's share = 2 × 43,750 = Rs 87,500."
                    }
                ]
            },
            {
                "exercise": "3.5",
                "title": "Exercise 3.5: Taxation",
                "answerKeyText": "Exercise 3.5 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Calculate the property tax on a house valued at Rs 6,500,000 at a tax rate of 0.5%.",
                        "solution": "Property Tax = (0.5 / 100) × 6,500,000 = Rs 32,500."
                    },
                    {
                        "qNo": "2",
                        "question": "An article priced at Rs 4500 is sold with 17% General Sales Tax (GST). Calculate the GST amount and total price paid by the consumer.",
                        "solution": "GST = (17 / 100) × 4500 = Rs 765.\nTotal price = 4500 + 765 = Rs 5,265."
                    }
                ]
            },
            {
                "exercise": "Review 3",
                "title": "Review Exercise 3",
                "answerKeyText": "Review Exercise 3 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Review comprehensive questions on financial arithmetic, ratios, and taxes.",
                        "solution": "Solved across business profit, inheritance distribution, and tax assessments."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Profit % & Loss %",
                "formula": "\\text{Profit \\%} = \\frac{\\text{Profit}}{\\text{CP}} \\times 100, \\quad \\text{Loss \\%} = \\frac{\\text{Loss}}{\\text{CP}} \\times 100",
                "note": "Always computed on Cost Price (CP)."
            },
            {
                "name": "Widow's Islamic Share",
                "formula": "\\text{Share} = \\frac{1}{8} \\times \\text{Net Estate} \\quad (\\text{with children})",
                "note": "Sons and daughters divide remainder in 2:1 ratio."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "If CP = Rs 500 and SP = Rs 600, what is the profit percentage?", "options": ["A) 10%", "B) 20%", "C) 25%", "D) 16.6%"], "answer": "B) 20%", "explanation": "Profit = 100. Profit % = (100/500) × 100 = 20%."},
                {"q": "What is the Islamic share of a widow when the deceased has surviving children?", "options": ["A) 1/2", "B) 1/4", "C) 1/8", "D) 1/3"], "answer": "C) 1/8", "explanation": "Quranic prescription: 1/8 in the presence of children."},
                {"q": "A discount of 15% on a marked price of Rs 2000 equals:", "options": ["A) Rs 150", "B) Rs 300", "C) Rs 1700", "D) Rs 2300"], "answer": "B) Rs 300", "explanation": "0.15 × 2000 = Rs 300."}
            ],
            "shortQuestions": [
                {"q": "Differentiate between Direct Proportion and Inverse Proportion.", "answer": "In Direct Proportion, both quantities increase or decrease in the same ratio (x/y = k). In Inverse Proportion, when one quantity increases, the other decreases proportionately (x × y = k)."},
                {"q": "What deductions are made from an estate before inheritance distribution?", "answer": "1. Funeral/burial expenses, 2. Payment of all outstanding debts, 3. Execution of valid bequests (up to 1/3 of the estate)."}
            ],
            "longQuestions": [
                {"q": "Three partners A, B, and C invested Rs 40,000, Rs 60,000, and Rs 100,000 in a business. At the end of the year, they earned a total profit of Rs 50,000. Find each partner's share.", "answer": "Ratio of investment: A : B : C = 40,000 : 60,000 : 100,000 = 2 : 3 : 5.\nSum of ratios = 2 + 3 + 5 = 10.\n• Partner A's share = (2/10) × 50,000 = Rs 10,000.\n• Partner B's share = (3/10) × 50,000 = Rs 15,000.\n• Partner C's share = (5/10) × 50,000 = Rs 25,000."}
            ]
        }
    }


def get_unit_4():
    return {
        "number": 4,
        "id": "unit-4",
        "title": "Square Roots and Cube Roots",
        "titleUrdu": "جذر المربع اور جذر الکعب",
        "type": "chapter",
        "pageRange": "pp. 60–85",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 4 develops the theory and methods of calculating square roots and cube roots of rational numbers. It covers prime factorization and long division methods for perfect squares and non-perfect square approximations, roots of proper and decimal fractions, and cube roots by prime factorization. It includes real-world word problems on square areas and cubic volumes.",
        "urduSummary": "یونٹ 4 ناطق اعداد کے جذر المربع (Square Root) اور جذر الکعب (Cube Root) کی نظریاتی اور عملی تفہیم فراہم کرتا ہے۔ اس میں مفرد تجزی (Prime Factorization) اور بذریعہ تقسیم (Division Method) سے جذر معلوم کرنا، کسروں اور اعشاری اعداد کے جذر، اور کیوب روٹس کے طریقے شامل ہیں۔ اس کے علاوہ مربع رقبوں اور مکعب حجم سے متعلق عملی سوالات بھی حل کیے گئے ہیں۔",
        "sections": [
            {
                "id": "4.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Find square roots of natural numbers by prime factorization and division method.\n• Find square roots of common fractions and decimal fractions.\n• Calculate cubes and cube roots of numbers by prime factorization.\n• Solve real-life word problems involving square roots and cube roots.",
                "theory": "Core Mathematical Outcomes:\n1. Master the square root algorithm (division method) with pairing from right to left.\n2. Handle decimal places in square roots (pairing digits before and after the decimal point).\n3. Find cube roots using triplet groupings of prime factors: ∛(a³) = a.",
                "paras": [
                    "Find square roots by prime factorization and division methods.",
                    "Find square roots of common fractions and decimal numbers.",
                    "Calculate cube roots by prime factorization.",
                    "Solve real-world problems on squares, cubes, and geometric dimensions."
                ]
            },
            {
                "id": "4.1-square-roots",
                "title": "4.1 Square Roots: Prime Factorization and Division",
                "heading": "Square Roots: Factorization & Division",
                "headingUrdu": "جذر المربع: مفرد تجزی اور تقسیم کا طریقہ",
                "text": "The square root of a number x is that number y which when multiplied by itself gives x: √x = y iff y² = x.\nMethods:\n1. Prime Factorization: Express number as prime factors, pair identical factors, take one from each pair.\n2. Division Method: Pair digits starting from the unit's place. Find largest integer whose square is ≤ the first period. Double the quotient for subsequent divisors.",
                "theory": "Rules for Square Roots:\n• √(a × b) = √a × √b\n• √(a / b) = √a / √b\n• Number of digits in √N: If N has n digits, the number of digits in its square root is n/2 (if n is even) or (n + 1)/2 (if n is odd).",
                "paras": [
                    "The square root is the inverse operation of squaring.",
                    "Prime factorization groups identical factors in pairs.",
                    "The division method allows finding square roots of large numbers and decimals efficiently."
                ]
            },
            {
                "id": "4.2-cube-roots",
                "title": "4.2 Cube and Cube Roots",
                "heading": "Cube and Cube Roots",
                "headingUrdu": "مکعب اور جذر الکعب",
                "text": "The cube of a number x is x³ = x × x × x. The cube root of a number x is written ∛x.\nTo find the cube root by prime factorization:\n1. Resolve the number into prime factors.\n2. Group the identical factors into triplets (groups of three).\n3. Take one factor from each triplet and multiply them together.",
                "theory": "Properties of Cubes:\n• The cube of an even number is always even.\n• The cube of an odd number is always odd.\n• ∛(a × b) = ∛a × ∛b\n• ∛(a / b) = ∛a / ∛b\n• Cube root of negative numbers: ∛(-x) = -∛x.",
                "paras": [
                    "A cube is obtained by multiplying a number by itself three times.",
                    "The cube root inverse operation groups prime factors into triplets.",
                    "Volume of a cube is V = s³, and edge length is s = ∛V."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-4-1",
                "title": "Example 1: Square Root by Division",
                "problem": "Find the square root of 55,225 using the division method.",
                "solution": "1. Make pairs from right: 5, 52, 25.\n2. First period is 5. 2² = 4 ≤ 5. Remainder = 1. Quotient = 2.\n3. Bring down 52 → 152. New divisor: 2 × 2 = 4_ → 43 × 3 = 129. Remainder = 23. Quotient = 23.\n4. Bring down 25 → 2325. New divisor: 46_ → 465 × 5 = 2325. Remainder = 0.\nTherefore, √55,225 = 235."
            },
            {
                "id": "we-8-4-2",
                "title": "Example 2: Cube Root by Factorization",
                "problem": "Find the cube root of 216,000 by prime factorization.",
                "solution": "216,000 = 216 × 1000 = 6³ × 10³ = (2³ × 3³) × (2³ × 5³)\n= 2⁶ × 3³ × 5³ = (2² × 3 × 5)³ = (4 × 15)³ = 60³.\nTherefore, ∛216,000 = 60."
            }
        ],
        "exercises": [
            {
                "exercise": "4.1",
                "title": "Exercise 4.1: Square Roots",
                "answerKeyText": "Exercise 4.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the square root by prime factorization:\n(a) 784 (b) 1225 (c) 2025 (d) 4096",
                        "solution": "(a) 784 = 2⁴ × 7² → √(2⁴ × 7²) = 2² × 7 = 4 × 7 = 28.\n(b) 1225 = 5² × 7² → √(5² × 7²) = 5 × 7 = 35.\n(c) 2025 = 3⁴ × 5² → √(3⁴ × 5²) = 3² × 5 = 9 × 5 = 45.\n(d) 4096 = 2¹² → √(2¹²) = 2⁶ = 64."
                    },
                    {
                        "qNo": "2",
                        "question": "Find the square root by division method:\n(a) 10,201 (b) 15,129 (c) 184.96",
                        "solution": "(a) √10,201 = 101.\n(b) √15,129 = 123.\n(c) √184.96 = 13.6."
                    }
                ]
            },
            {
                "exercise": "4.2",
                "title": "Exercise 4.2: Cube Roots",
                "answerKeyText": "Exercise 4.2 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Find the cube root by prime factorization:\n(a) 729 (b) 3375 (c) 15,625 (d) 274,625",
                        "solution": "(a) 729 = 3⁶ = (3²)³ → ∛729 = 9.\n(b) 3375 = 3³ × 5³ → ∛3375 = 3 × 5 = 15.\n(c) 15,625 = 5⁶ = (5²)³ → ∛15,625 = 25.\n(d) 274,625 = 5³ × 13³ → ∛274,625 = 5 × 13 = 65."
                    }
                ]
            },
            {
                "exercise": "Review 4",
                "title": "Review Exercise 4",
                "answerKeyText": "Review Exercise 4 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "The area of a square field is 5184 m². Find the length of each side.",
                        "solution": "Side = √Area = √5184 = 72 meters."
                    },
                    {
                        "qNo": "2",
                        "question": "A cubic water tank has a capacity of 2197 m³. Find the length of its side.",
                        "solution": "Side = ∛Volume = ∛2197 = 13 meters."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Square and Square Root",
                "formula": "\\sqrt{x} = y \\iff y^2 = x, \\quad \\sqrt{a \\times b} = \\sqrt{a} \\times \\sqrt{b}",
                "note": "Inverse of squaring."
            },
            {
                "name": "Cube and Cube Root",
                "formula": "\\sqrt[3]{x} = y \\iff y^3 = x, \\quad \\sqrt[3]{a \\times b} = \\sqrt[3]{a} \\times \\sqrt[3]{b}",
                "note": "Triplets of prime factors."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "The square root of 0.04 is:", "options": ["A) 0.02", "B) 0.2", "C) 2", "D) 0.002"], "answer": "B) 0.2", "explanation": "0.2 × 0.2 = 0.04."},
                {"q": "How many digits are in the square root of a 6-digit perfect square?", "options": ["A) 2", "B) 3", "C) 4", "D) 5"], "answer": "B) 3", "explanation": "For even n digits, digits in root = n/2 = 6/2 = 3."},
                {"q": "The cube root of -512 is:", "options": ["A) 8", "B) -8", "C) 16", "D) -16"], "answer": "B) -8", "explanation": "(-8)³ = -512."}
            ],
            "shortQuestions": [
                {"q": "Can the square root of a negative real number be real?", "answer": "No. The square of any real number is always non-negative. Therefore, the square root of a negative number is not a real number."},
                {"q": "Explain how pairing of digits is done for a decimal number when using the division method.", "answer": "Pairing starts from the decimal point: integers are paired towards the left (units, tens), while decimal fractions are paired towards the right (tenths, hundredths). If needed, a trailing zero is added to complete the final decimal pair."}
            ],
            "longQuestions": [
                {"q": "A rectangular field has length 48 m and width 27 m. A square field has the same area as this rectangular field. Find the perimeter of the square field.", "answer": "1. Area of rectangle = length × width = 48 m × 27 m = 1296 m².\n2. Area of square = 1296 m².\n3. Side of square = √1296 = 36 m.\n4. Perimeter of square = 4 × side = 4 × 36 m = 144 m."}
            ]
        }
    }

print("Units 2, 3, 4 defined successfully.")
