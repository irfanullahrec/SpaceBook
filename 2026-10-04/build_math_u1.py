# -*- coding: utf-8 -*-
"""
SpaceBook - Class 8 Mathematics Comprehensive Data Builder
Constructs MATH_8_DATA for all 11 Units of KPTBB Grade 8 Mathematics (SNC 2022)
"""

import json
import os
import sys

def get_unit_1():
    return {
        "number": 1,
        "id": "unit-1",
        "title": "Approximation and Estimation",
        "titleUrdu": "تقریب اور تخمینہ",
        "type": "chapter",
        "pageRange": "pp. 1–7",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 1 covers approximation and estimation techniques required in mathematical modeling and real-life measurement. It establishes exact rules for determining significant figures, methods for rounding whole numbers and decimals up to 5 significant figures, and the calculation of approximation errors defined as |Exact Value - Approximated Value|.",
        "urduSummary": "یونٹ 1 تقریب اور تخمینہ کے بنیادی تصورات پر مشتمل ہے۔ اس میں سگنیفیکینٹ فیگرز (اہم ہندسوں) کے تعین کے مستند اصول، اعداد کو 5 اہم ہندسوں تک راؤنڈ آف کرنے کے طریقے، اور تخمینہ کی غلطی |Exact Value - Approximated Value| معلوم کرنے کا طریقہ تفصیل سے بیان کیا گیا ہے۔",
        "sections": [
            {
                "id": "1.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج",
                "text": "After completing this unit, students will be able to:\n• Round off numbers up to 5 significant figures.\n• Analyze approximation error when numbers are rounded off.\n• Solve real-world word problems involving approximation.",
                "theory": "Student Learning Outcomes:\n1. Master the criteria for significant figures in measurements.\n2. Apply rounding rules to whole numbers and decimal fractions up to 5 significant figures.\n3. Compute and analyze approximation error.",
                "paras": [
                    "After completing this unit, students will be able to:",
                    "• Round off numbers up to 5 significant figures.",
                    "• Analyze approximation error when numbers are rounded off.",
                    "• Solve real-world word problems involving approximation."
                ]
            },
            {
                "id": "1.1-significant-figures",
                "title": "1.1 Significant Figures & Measurement Accuracy",
                "heading": "Significant Figures & Measurement Accuracy",
                "headingUrdu": "اہم ہندسے اور پیمائش کی درستی",
                "text": "The closeness of a measured value to the true value is known as measurement accuracy. Significant figures are digits that carry meaning contributing to measurement resolution.\nRules:\n1. All non-zero digits are significant (e.g. 524 has 3 s.f.).\n2. Zeros between non-zero digits are significant (e.g. 70.08 has 4 s.f.).\n3. Leading zeros are NEVER significant (e.g. 0.0034 has 2 s.f.).\n4. Trailing zeros after a decimal point are significant (e.g. 12.500 has 5 s.f.).\n5. Trailing zeros at the end of whole numbers are not significant unless explicitly marked (e.g. 8400 has 2 s.f.).",
                "theory": "Detailed Rules for Significant Figures:\n• Non-zero digits: 1, 2, 3, 4, 5, 6, 7, 8, 9 are always significant.\n• Captive zeros: Zeros sandwiched between non-zero digits are significant.\n• Leading zeros: Zeros preceding the first non-zero digit are place-holders and NOT significant.\n• Trailing decimal zeros: Indicate the precision of the apparatus and ARE significant.\n• Trailing integer zeros: Ambiguous in standard notation, treated as non-significant placeholders in textbook conventions.",
                "paras": [
                    "The closeness of a measured value to the true value is known as measurement accuracy.",
                    "All non-zero digits are significant.",
                    "Zeros between non-zero digits are significant.",
                    "Zeros before the first non-zero digit are never significant.",
                    "Zeros at the end of a number after a decimal point are significant.",
                    "Zeros at the end of whole numbers are not significant."
                ]
            },
            {
                "id": "1.2-approximation-error",
                "title": "1.2 Approximation Error Analysis",
                "heading": "Approximation Error Analysis",
                "headingUrdu": "تخمینہ کی غلطی کا تجزئیہ",
                "text": "When numbers are rounded off, the difference between the exact (true) value and the approximate (rounded) value is the approximation error:\nApproximation Error = |Exact Value - Approximated Value|\nBecause error measures deviation magnitude, it is always non-negative.",
                "theory": "Approximation Error Formula:\nE = |X_true - X_approx|\nWhere:\n• X_true is the original unrounded exact value.\n• X_approx is the value rounded to the specified number of significant figures or decimal places.\nExample:\nExact = 67.245, Rounded to 3 s.f. = 67.2.\nError = |67.245 - 67.2| = 0.045.",
                "paras": [
                    "When numbers are rounded off, the difference between the exact value and the approximate value is the approximation error.",
                    "Formula: Approximation Error = |Exact Value - Approximated Value|.",
                    "Because error measures deviation magnitude, it is always non-negative."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-1-1",
                "title": "Example 1: Rounding Whole Numbers",
                "problem": "Round off 847,382 to: (a) 1 s.f. (b) 2 s.f. (c) 3 s.f. (d) 4 s.f. (e) 5 s.f.",
                "solution": "(a) 1 s.f.: 847,382 → 2nd digit 4 (<5) → 800,000\n(b) 2 s.f.: 847,382 → 3rd digit 7 (≥5) → 850,000\n(c) 3 s.f.: 847,382 → 4th digit 3 (<5) → 847,000\n(d) 4 s.f.: 847,382 → 5th digit 8 (≥5) → 847,400\n(e) 5 s.f.: 847,382 → 6th digit 2 (<5) → 847,380"
            },
            {
                "id": "we-8-1-2",
                "title": "Example 2: Decimal Rounding and Error",
                "problem": "The mass of a specimen is 4.04 kg. Round to: (a) the nearest whole kg, and find error. (b) to the nearest tenth, and find error.",
                "solution": "(a) Nearest whole number: 4.04 kg ≈ 4 kg. Error = |4.04 - 4| = 0.04 kg.\n(b) Nearest tenth (1 decimal place): 4.04 kg ≈ 4.0 kg. Error = |4.04 - 4.0| = 0.04 kg."
            }
        ],
        "exercises": [
            {
                "exercise": "1.1",
                "title": "Exercise 1.1",
                "answerKeyText": "Exercise 1.1 Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Round the following whole numbers to 3 significant figures:\n(a) 34,716 (b) 87,932 (c) 873,572 (d) 93,482 (e) 53,476 (f) 45,705",
                        "solution": "(a) 34,716 → 34,700\n(b) 87,932 → 87,900\n(c) 873,572 → 874,000\n(d) 93,482 → 93,500\n(e) 53,476 → 53,500\n(f) 45,705 → 45,700"
                    },
                    {
                        "qNo": "2",
                        "question": "Round the following whole numbers to 5 significant figures:\n(a) 3,872,345 (b) 5,362,852 (c) 9,024,691 (d) 8,348,347 (e) 4,528,409 (f) 5,245,891",
                        "solution": "(a) 3,872,345 → 3,872,300\n(b) 5,362,852 → 5,362,900\n(c) 9,024,691 → 9,024,700\n(d) 8,348,347 → 8,348,300\n(e) 4,528,409 → 4,528,400\n(f) 5,245,891 → 5,245,900"
                    },
                    {
                        "qNo": "3",
                        "question": "Round the following decimal numbers to 3 significant figures:\n(a) 87.256 (b) 58.2672 (c) 9.24578 (d) 2.6572 (e) 4.8235",
                        "solution": "(a) 87.256 → 87.3\n(b) 58.2672 → 58.3\n(c) 9.24578 → 9.25\n(d) 2.6572 → 2.66\n(e) 4.8235 → 4.82"
                    },
                    {
                        "qNo": "4",
                        "question": "Round the following decimal numbers to 4 significant figures:\n(a) 72.5623 (b) 89.0367 (c) 56.8926 (d) 6.09871 (e) 23.23232",
                        "solution": "(a) 72.5623 → 72.56\n(b) 89.0367 → 89.04\n(c) 56.8926 → 56.89\n(d) 6.09871 → 6.099\n(e) 23.23232 → 23.23"
                    },
                    {
                        "qNo": "5",
                        "question": "Round the following decimal numbers to 5 significant figures:\n(a) 4.10987 (b) 65.23689 (c) 872.12345 (d) 0.234877 (e) 65.72045",
                        "solution": "(a) 4.10987 → 4.1099\n(b) 65.23689 → 65.237\n(c) 872.12345 → 872.12\n(d) 0.234877 → 0.23488\n(e) 65.72045 → 65.720"
                    },
                    {
                        "qNo": "6",
                        "question": "There are 87,234 English language books and 63,245 Art books in a library. Round off these quantities to 4 significant figures and then add to find the approximate number of total books.",
                        "solution": "English books: 87,234 ≈ 87,230 (4 s.f.).\nArt books: 63,245 ≈ 63,250 (4 s.f.).\nTotal approximate books = 87,230 + 63,250 = 150,480."
                    },
                    {
                        "qNo": "7",
                        "question": "Zaeem wants to buy a flat costing Rs 2,237,750. Round this amount off to 5 significant figures.",
                        "solution": "Rs 2,237,750 rounded to 5 s.f.: 6th digit is 5 (≥5, round up 7 to 8) → Rs 2,237,800."
                    },
                    {
                        "qNo": "8",
                        "question": "The mass of a bag of cement is 23.765 kg. Round this mass off to 4 significant figures.",
                        "solution": "23.765 kg rounded to 4 s.f.: 5th digit is 5 (≥5, round up 6 to 7) → 23.77 kg."
                    },
                    {
                        "qNo": "9",
                        "question": "The volume of water in a tank is 6723.855 litres. Round this volume off to 5 significant figures.",
                        "solution": "6723.855 litres rounded to 5 s.f.: 6th digit is 5 (≥5, round up 8 to 9) → 6723.9 litres."
                    },
                    {
                        "qNo": "10",
                        "question": "The grocery bill has an exact amount of Rs 723.657. Round this off to 5 significant figures.",
                        "solution": "Rs 723.657 rounded to 5 s.f.: 6th digit is 7 (≥5, round up 5 to 6) → Rs 723.66."
                    }
                ]
            },
            {
                "exercise": "Review 1",
                "title": "Review Exercise 1",
                "answerKeyText": "Review Exercise 1 Solutions",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "A library has 127,462 monthly visitors. Round this value to: (a) 2 s.f. (b) 3 s.f. (c) 4 s.f. (d) 5 s.f.",
                        "solution": "(a) 2 s.f.: 127,462 → 130,000\n(b) 3 s.f.: 127,462 → 127,000\n(c) 4 s.f.: 127,462 → 127,500\n(d) 5 s.f.: 127,462 → 127,460"
                    },
                    {
                        "qNo": "2",
                        "question": "The population of Town A is 872,345 and Town B is 624,509. Round off each to 4 s.f. and add to find the approximate combined population.",
                        "solution": "Town A: 872,345 ≈ 872,300 (4 s.f.).\nTown B: 624,509 ≈ 624,500 (4 s.f.).\nTotal = 872,300 + 624,500 = 1,496,800."
                    },
                    {
                        "qNo": "3",
                        "question": "The distance between two landmarks is 452.9872 km. Round this off to: (a) 3 s.f. (b) 4 s.f. (c) 5 s.f.",
                        "solution": "(a) 3 s.f.: 452.9872 → 453 km\n(b) 4 s.f.: 452.9872 → 453.0 km\n(c) 5 s.f.: 452.9872 → 452.99 km"
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Approximation Error",
                "formula": "\\text{Approximation Error} = |\\text{Exact Value} - \\text{Approximated Value}|",
                "note": "Deviational magnitude representing measurement discrepancy."
            }
        ],
        "slos": {
            "mcqs": [
                {"q": "How many significant figures are in 0.04020?", "options": ["A) 2", "B) 3", "C) 4", "D) 5"], "answer": "C) 4", "explanation": "The digits 4, 0 (between non-zeros), 2, and the trailing decimal 0 are significant."},
                {"q": "Round 48,653 to 2 significant figures:", "options": ["A) 48,000", "B) 49,000", "C) 48,700", "D) 50,000"], "answer": "B) 49,000", "explanation": "3rd digit is 6 (≥5), so 48 rounds up to 49,000."},
                {"q": "Exact = 15.68 kg, Rounded = 15.7 kg. What is the approximation error?", "options": ["A) 0.02 kg", "B) -0.02 kg", "C) 0.2 kg", "D) 0.08 kg"], "answer": "A) 0.02 kg", "explanation": "|15.68 - 15.7| = 0.02 kg."}
            ],
            "shortQuestions": [
                {"q": "Define measurement accuracy.", "answer": "Measurement accuracy is the closeness of an experimentally measured or estimated value to the true, actual value of the quantity."},
                {"q": "Explain why trailing zeros in a decimal number are considered significant.", "answer": "Trailing zeros after a decimal point indicate the precision limit of the measuring device (e.g. 5.20 cm is measured to the hundredths place, not just tenths)."}
            ],
            "longQuestions": [
                {"q": "A warehouse stores bags with weights 12.456 kg, 18.234 kg, and 25.789 kg. Round each to 3 s.f. and compute total estimated weight and approximation error.", "answer": "1. Round to 3 s.f.:\n• 12.456 kg → 12.5 kg\n• 18.234 kg → 18.2 kg\n• 25.789 kg → 25.8 kg\nEstimated total = 12.5 + 18.2 + 25.8 = 56.5 kg.\nExact total = 12.456 + 18.234 + 25.789 = 56.479 kg.\nApproximation Error = |56.479 - 56.5| = 0.021 kg."}
            ]
        }
    }

print("Unit 1 definition completed.")
