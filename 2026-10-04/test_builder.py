# -*- coding: utf-8 -*-
"""
SpaceBook - Class 8 Mathematics Complete Data Generator
Extracts and builds MATH_8_DATA for all 11 Units of KPTBB Grade 8 Mathematics (SNC 2022)
"""

import json
import os

units = [
    # -------------------------------------------------------------
    # UNIT 1: APPROXIMATION AND ESTIMATION
    # -------------------------------------------------------------
    {
        "number": 1,
        "id": "unit-1",
        "title": "Approximation and Estimation",
        "titleUrdu": "تقریب اور تخمینہ",
        "type": "chapter",
        "pageRange": "pp. 1–7",
        "source": "KPK Textbook Board (KPTBB) Grade 8 Mathematics (SNC 2022)",
        "englishSummary": "Unit 1 covers the fundamental principles of approximation, estimation, and significant figures. In real-world measurements and calculations, exact values are often unavailable or unnecessary. Students learn the strict rules for determining significant figures, methods for rounding whole numbers and decimals to specified degrees of accuracy (up to 5 significant figures), and calculating approximation error, defined as the absolute difference between the exact value and the approximate value: Approximation Error = |Exact Value - Approximate Value|.",
        "urduSummary": "یونٹ 1 تقریب، تخمینہ اور اہم ہندسوں (سگنیفیکینٹ فیگرز) کے بنیادی اصولوں کا احاطہ کرتا ہے۔ حقیقی زندگی میں درست قیمت کا حصول اکثر ناممکن یا غیر ضروری ہوتا ہے۔ اس یونٹ میں طلباء اہم ہندسوں کی شناخت کے قواعد، کُل اور اعشاری اعداد کو 5 اہم ہندسوں تک راؤنڈ آف کرنے کے طریقے، اور تخمینہ کی غلطی (Approximation Error = |Exact Value - Approximate Value|) کا حساب لگانا سیکھتے ہیں۔",
        "sections": [
            {
                "id": "1.0-slo",
                "title": "Student Learning Outcomes",
                "heading": "Student Learning Outcomes",
                "headingUrdu": "طلبہ کے سیکھنے کے نتائج (SLOs)",
                "text": "After completing this unit, students will be able to:\n• Round off numbers up to 5 significant figures.\n• Analyze approximation error when numbers are rounded off.\n• Solve real-world word problems involving approximation and estimation.",
                "theory": "Student Learning Outcomes:\n1. Round off whole numbers and decimal numbers up to 5 significant figures.\n2. Calculate and analyze approximation error: Approximation Error = |Exact Value - Approximated Value|.\n3. Apply rounding techniques in real-life contexts including financial budgets, physical measurements, and demographic statistics.",
                "paras": [
                    "After completing this unit, students will be able to:",
                    "• Round off numbers up to 5 significant figures.",
                    "• Analyze approximation error when numbers are rounded off.",
                    "• Solve real-world word problems involving approximation and estimation."
                ]
            },
            {
                "id": "1.1-estimation-intro",
                "title": "1.1 Introduction to Estimation and Approximation",
                "heading": "Introduction to Estimation and Approximation",
                "headingUrdu": "تخمینہ اور تقریب کا تعارف",
                "text": "In many daily life situations, we are not able to calculate the exact amount or quantity of something. We need an answer that is close to the actual calculation. In such situations we need to approximate or estimate quantities. The closeness of a measured value to the true (actual) value of something is known as measurement accuracy.",
                "theory": "In science, engineering, and everyday life, quantities are often approximated:\n• Measurement Accuracy: The closeness of a measured value to the true (actual) value.\n• Rounding off: The process of replacing a number with an approximate value that is shorter, simpler, or more explicit.\n• Significant figures (s.f.): The meaningful digits in a number that contribute to its precision.",
                "paras": [
                    "In many daily life situations, we are not able to calculate the exact amount or quantity of something.",
                    "We need an answer that is close to the actual calculation. In such situations we need to approximate or estimate quantities.",
                    "The closeness of a measured value to the true (actual) value of something is known as measurement accuracy."
                ]
            },
            {
                "id": "1.2-significant-figures",
                "title": "1.2 Rules for Determining Significant Figures",
                "heading": "Rules for Significant Figures",
                "headingUrdu": "اہم ہندسوں کے تعین کے قواعد",
                "text": "Rules to determine significant figures:\n1. All non-zero digits are significant. For example, 482 has 3 s.f.\n2. Zeros between non-zero digits are significant (captive zeros). For example, 89.045 has 5 s.f.\n3. Leading zeros (zeros before non-zero digits) are NEVER significant. For example, 0.0045 has 2 s.f.\n4. Trailing zeros after a decimal point are significant. For example, 9.500 has 4 s.f.\n5. Trailing zeros at the end of whole numbers are generally not significant unless indicated by a decimal point. For example, 9500 has 2 s.f.",
                "theory": "Rules for Significant Figures (s.f.):\n• Rule 1: All non-zero digits (1 to 9) are significant.\n• Rule 2: Zeros appearing between non-zero digits are always significant (e.g. 5004 has 4 s.f.).\n• Rule 3: Zeros to the left of the first non-zero digit are leading zeros and are NOT significant (e.g. 0.0072 has 2 s.f.).\n• Rule 4: Zeros at the end of a decimal number are significant because they show the precision of the measurement (e.g. 4.300 has 4 s.f.).\n• Rule 5: Trailing zeros in a whole number without a decimal point are place-holders and are NOT significant (e.g. 74,000 has 2 s.f.).",
                "paras": [
                    "All non-zero digits are significant. For example, 482 has 3 significant figures.",
                    "Zeros between non-zero digits are significant. For example, 89.045 has 5 significant figures.",
                    "Zeros at the beginning of a number before the first non-zero digit are never significant. For example, 0.0045 has 2 significant figures.",
                    "Zeros at the end of a number after the decimal point are significant. For example, 9.500 has 4 significant figures.",
                    "Zeros at the end of whole numbers are not significant. For example, 9500 has 2 significant figures."
                ]
            },
            {
                "id": "1.3-approximation-error",
                "title": "1.3 Approximation Error",
                "heading": "Approximation Error",
                "headingUrdu": "تقریب کی غلطی (Approximation Error)",
                "text": "The difference between the exact (actual) value and the approximated (rounded) value is called the approximation error.\nFormula:\nApproximation Error = |Exact Value - Approximated Value|\nSince error represents a deviation magnitude, it is expressed as a positive quantity.",
                "theory": "Approximation Error Analysis:\nWhen an exact measurement X is rounded to an approximate value X_approx:\nApproximation Error = |X - X_approx|\nExample: If the exact mass is 4.04 kg and it is rounded to 4 kg:\nApproximation Error = |4.04 - 4| = 0.04 kg.\nIf it is rounded to 4.0 kg:\nApproximation Error = |4.04 - 4.0| = 0.04 kg.",
                "paras": [
                    "The difference between the exact (actual) value and the approximated (rounded) value is called the approximation error.",
                    "Formula: Approximation Error = |Exact Value - Approximated Value|.",
                    "Since error represents a deviation magnitude, it is taken as an absolute positive quantity."
                ]
            }
        ],
        "workedExamples": [
            {
                "id": "we-8-1-1",
                "title": "Example 1: Rounding to Significant Figures",
                "problem": "Round off 45,768 to:\n(a) 1 significant figure\n(b) 2 significant figures\n(c) 3 significant figures\n(d) 4 significant figures",
                "solution": "(a) To 1 s.f.: First digit is 4, followed by 5 (>= 5, so round up). 45,768 ≈ 50,000.\n(b) To 2 s.f.: First two digits are 45, next digit is 7 (>= 5, round up). 45,768 ≈ 46,000.\n(c) To 3 s.f.: First three digits are 457, next digit is 6 (>= 5, round up). 45,768 ≈ 45,800.\n(d) To 4 s.f.: First four digits are 4576, next digit is 8 (>= 5, round up). 45,768 ≈ 45,770."
            },
            {
                "id": "we-8-1-2",
                "title": "Example 2: Decimal Rounding and Error",
                "problem": "The exact length of a metal rod is 23.478 cm. Round it off to 3 significant figures and calculate the approximation error.",
                "solution": "1. Exact value = 23.478 cm.\n2. To round to 3 s.f., we keep the first 3 digits: 2, 3, and 4. The next digit is 7 (which is ≥ 5), so we round up 4 to 5.\nApproximate value = 23.5 cm.\n3. Approximation Error = |Exact Value - Approximate Value|\n= |23.478 - 23.5| = |-0.022| = 0.022 cm."
            }
        ],
        "exercises": [
            {
                "exercise": "1.1",
                "title": "Exercise 1.1",
                "answerKeyText": "Class 8 Mathematics Exercise 1.1 Complete Solved Problems",
                "problems": [
                    {
                        "qNo": "1",
                        "question": "Round the following whole numbers to 3 significant figures:\n(a) 34,716\n(b) 87,932\n(c) 873,572\n(d) 93,482\n(e) 53,476\n(f) 45,705",
                        "solution": "(a) 34,716: Look at the 4th digit (1 < 5) → 34,700 (3 s.f.)\n(b) 87,932: Look at the 4th digit (3 < 5) → 87,900 (3 s.f.)\n(c) 873,572: Look at the 4th digit (5 ≥ 5, round up 3 to 4) → 874,000 (3 s.f.)\n(d) 93,482: Look at the 4th digit (8 ≥ 5, round up 4 to 5) → 93,500 (3 s.f.)\n(e) 53,476: Look at the 4th digit (7 ≥ 5, round up 4 to 5) → 53,500 (3 s.f.)\n(f) 45,705: Look at the 4th digit (0 < 5) → 45,700 (3 s.f.)"
                    },
                    {
                        "qNo": "2",
                        "question": "Round the following whole numbers to 5 significant figures:\n(a) 3,872,345\n(b) 5,362,852\n(c) 9,024,691\n(d) 8,348,347\n(e) 4,528,409\n(f) 5,245,891",
                        "solution": "(a) 3,872,345: 6th digit is 4 (< 5) → 3,872,300 (5 s.f.)\n(b) 5,362,852: 6th digit is 5 (≥ 5, round up 8 to 9) → 5,362,900 (5 s.f.)\n(c) 9,024,691: 6th digit is 9 (≥ 5, round up 6 to 7) → 9,024,700 (5 s.f.)\n(d) 8,348,347: 6th digit is 4 (< 5) → 8,348,300 (5 s.f.)\n(e) 4,528,409: 6th digit is 0 (< 5) → 4,528,400 (5 s.f.)\n(f) 5,245,891: 6th digit is 9 (≥ 5, round up 8 to 9) → 5,245,900 (5 s.f.)"
                    },
                    {
                        "qNo": "3",
                        "question": "Round the following decimal numbers to 3 significant figures:\n(a) 87.256\n(b) 58.2672\n(c) 9.24578\n(d) 2.6572\n(e) 4.8235",
                        "solution": "(a) 87.256: 4th digit is 5 (≥ 5, round up 2 to 3) → 87.3 (3 s.f.)\n(b) 58.2672: 4th digit is 6 (≥ 5, round up 2 to 3) → 58.3 (3 s.f.)\n(c) 9.24578: 4th digit is 5 (≥ 5, round up 4 to 5) → 9.25 (3 s.f.)\n(d) 2.6572: 4th digit is 7 (≥ 5, round up 5 to 6) → 2.66 (3 s.f.)\n(e) 4.8235: 4th digit is 3 (< 5) → 4.82 (3 s.f.)"
                    },
                    {
                        "qNo": "4",
                        "question": "Round the following decimal numbers to 4 significant figures:\n(a) 72.5623\n(b) 89.0367\n(c) 56.8926\n(d) 6.09871\n(e) 23.23232",
                        "solution": "(a) 72.5623: 5th digit is 2 (< 5) → 72.56 (4 s.f.)\n(b) 89.0367: 5th digit is 6 (≥ 5, round up 3 to 4) → 89.04 (4 s.f.)\n(c) 56.8926: 5th digit is 2 (< 5) → 56.89 (4 s.f.)\n(d) 6.09871: 5th digit is 7 (≥ 5, round up 8 to 9) → 6.099 (4 s.f.)\n(e) 23.23232: 5th digit is 2 (< 5) → 23.23 (4 s.f.)"
                    },
                    {
                        "qNo": "5",
                        "question": "Round the following decimal numbers to 5 significant figures:\n(a) 4.10987\n(b) 65.23689\n(c) 872.12345\n(d) 0.234877\n(e) 65.72045",
                        "solution": "(a) 4.10987: 6th digit is 7 (≥ 5, round up 8 to 9) → 4.1099 (5 s.f.)\n(b) 65.23689: 6th digit is 8 (≥ 5, round up 6 to 7) → 65.237 (5 s.f.)\n(c) 872.12345: 6th digit is 3 (< 5) → 872.12 (5 s.f.)\n(d) 0.234877: Leading zero not significant. 6th sig digit is 7 (≥ 5, round up 7 to 8) → 0.23488 (5 s.f.)\n(e) 65.72045: 6th digit is 4 (< 5) → 65.720 (5 s.f.)"
                    },
                    {
                        "qNo": "6",
                        "question": "There are 87,234 English language books and 63,245 Art books in a library. Round off these quantities to 4 significant figures and then add to find the approximate number of total books.",
                        "solution": "1. English books: 87,234 rounded to 4 s.f. = 87,230 (since 5th digit is 4 < 5).\n2. Art books: 63,245 rounded to 4 s.f. = 63,250 (since 5th digit is 5 ≥ 5).\n3. Approximate total = 87,230 + 63,250 = 150,480 books."
                    },
                    {
                        "qNo": "7",
                        "question": "Zaeem wants to buy a flat costing Rs 2,237,750. Round this amount off to 5 significant figures.",
                        "solution": "1. Exact cost = Rs 2,237,750.\n2. The first 5 significant digits are 2, 2, 3, 7, 7.\n3. The 6th digit is 5 (≥ 5, so round up 7 to 8).\n4. Approximate cost = Rs 2,237,800."
                    },
                    {
                        "qNo": "8",
                        "question": "The mass of a bag of cement is 23.765 kg. Round this mass off to 4 significant figures.",
                        "solution": "1. Exact mass = 23.765 kg.\n2. The first 4 significant digits are 2, 3, 7, 6.\n3. The 5th digit is 5 (≥ 5, so round up 6 to 7).\n4. Approximate mass = 23.77 kg."
                    },
                    {
                        "qNo": "9",
                        "question": "The volume of water in a tank is 6723.855 litres. Round this volume off to 5 significant figures.",
                        "solution": "1. Exact volume = 6723.855 litres.\n2. The first 5 significant digits are 6, 7, 2, 3, 8.\n3. The 6th digit is 5 (≥ 5, so round up 8 to 9).\n4. Approximate volume = 6723.9 litres."
                    },
                    {
                        "qNo": "10",
                        "question": "The grocery bill has an exact amount of Rs 723.657. Round this off to 5 significant figures.",
                        "solution": "1. Exact bill = Rs 723.657.\n2. The first 5 significant digits are 7, 2, 3, 6, 5.\n3. The 6th digit is 7 (≥ 5, so round up 5 to 6).\n4. Approximate bill = Rs 723.66."
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
                        "question": "A library has 127,462 monthly visitors. Round this value to:\n(a) 2 significant figures\n(b) 3 significant figures\n(c) 4 significant figures\n(d) 5 significant figures",
                        "solution": "(a) To 2 s.f.: 127,462 → 3rd digit is 7 (≥ 5, round up 2 to 3) = 130,000 visitors.\n(b) To 3 s.f.: 127,462 → 4th digit is 4 (< 5) = 127,000 visitors.\n(c) To 4 s.f.: 127,462 → 5th digit is 6 (≥ 5, round up 4 to 5) = 127,500 visitors.\n(d) To 5 s.f.: 127,462 → 6th digit is 2 (< 5) = 127,460 visitors."
                    },
                    {
                        "qNo": "2",
                        "question": "The population of Town A is 872,345 and that of Town B is 624,509. Round off each population to 4 significant figures and add to find the approximate combined population.",
                        "solution": "1. Population of Town A: 872,345 to 4 s.f. = 872,300 (since 5th digit 4 < 5).\n2. Population of Town B: 624,509 to 4 s.f. = 624,500 (since 5th digit 0 < 5).\n3. Approximate total population = 872,300 + 624,500 = 1,496,800."
                    },
                    {
                        "qNo": "3",
                        "question": "The distance between two landmarks is 452.9872 km. Round this off to:\n(a) 3 significant figures\n(b) 4 significant figures\n(c) 5 significant figures",
                        "solution": "(a) To 3 s.f.: 452.9872 → 4th digit is 9 (≥ 5, round up 2 to 3) = 453 km.\n(b) To 4 s.f.: 452.9872 → 5th digit is 8 (≥ 5, round up 9 to 10) = 453.0 km.\n(c) To 5 s.f.: 452.9872 → 6th digit is 7 (≥ 5, round up 8 to 9) = 452.99 km."
                    }
                ]
            }
        ],
        "formulas": [
            {
                "name": "Approximation Error",
                "formula": "\\text{Approximation Error} = |\\text{Exact Value} - \\text{Approximated Value}|",
                "note": "Always a positive magnitude indicating the deviation from the actual measurement."
            },
            {
                "name": "Significant Figures Rules",
                "formula": "\\text{Non-zeros} = \\text{Always sig}; \\quad \\text{Captive zeros} = \\text{Sig}; \\quad \\text{Leading zeros} = \\text{Not sig}; \\quad \\text{Trailing decimals} = \\text{Sig}",
                "note": "Standard SNC rules for determining measurement precision."
            }
        ],
        "slos": {
            "mcqs": [
                {
                    "q": "How many significant figures are in the number 0.004050?",
                    "options": ["A) 3", "B) 4", "C) 6", "D) 7"],
                    "answer": "B) 4",
                    "explanation": "Leading zeros (0.00) are not significant. The digits 4, 0 (between non-zeros), 5, and the trailing zero 0 are significant: 4 significant figures."
                },
                {
                    "q": "Round 56,782 to 3 significant figures:",
                    "options": ["A) 56,700", "B) 56,800", "C) 57,000", "D) 56,780"],
                    "answer": "B) 56,800",
                    "explanation": "The 4th digit is 8 (≥ 5), so the 3rd digit 7 rounds up to 8, giving 56,800."
                },
                {
                    "q": "If the exact length is 12.35 cm and the rounded length is 12.4 cm, what is the approximation error?",
                    "options": ["A) 0.05 cm", "B) -0.05 cm", "C) 0.5 cm", "D) 0.01 cm"],
                    "answer": "A) 0.05 cm",
                    "explanation": "|12.35 - 12.4| = |-0.05| = 0.05 cm."
                }
            ],
            "shortQuestions": [
                {
                    "q": "State the rule for leading zeros and trailing zeros in significant figures.",
                    "answer": "1. Leading zeros (zeros before the first non-zero digit, e.g., 0.005) are never significant.\n2. Trailing zeros after a decimal point (e.g., 5.20) are always significant, while trailing zeros in whole numbers without a decimal point (e.g., 5200) are place holders and not significant."
                },
                {
                    "q": "Explain why approximation error is always expressed as an absolute value.",
                    "answer": "Error represents the magnitude of the difference or deviation between the true value and the estimate. Taking the absolute value ensures the error is always non-negative."
                }
            ],
            "longQuestions": [
                {
                    "q": "A civil engineer measures three pieces of road: 14.567 km, 28.342 km, and 9.789 km. (a) Round each length to 3 significant figures. (b) Find the estimated total sum. (c) Find the exact total sum and calculate the overall approximation error.",
                    "answer": "(a) Rounding each to 3 s.f.:\n• 14.567 km → 14.6 km\n• 28.342 km → 28.3 km\n• 9.789 km → 9.79 km\n(b) Estimated total sum = 14.6 + 28.3 + 9.79 = 52.69 km.\n(c) Exact total sum = 14.567 + 28.342 + 9.789 = 52.698 km.\nApproximation Error = |Exact - Estimated| = |52.698 - 52.69| = 0.008 km."
                }
            ]
        }
    }
]

print("Unit 1 generated successfully!")
