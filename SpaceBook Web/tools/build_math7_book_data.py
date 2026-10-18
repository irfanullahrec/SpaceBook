"""Extract Class 7 Mathematics lesson text from the supplied Word transcription.

The scanned KPTBB PDF remains the authority for diagrams and equations. The
Word files are used here as a navigable text transcription, not as a replacement
for checking the printed book.
"""

from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json
import re

ROOT = Path(r"D:\SpaceBook\Books\7th\7th MAths")
OUT = Path(__file__).resolve().parents[1] / "js" / "math_7_data.js"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
UNIT_RE = re.compile(r"^Unit\s+(\d{1,2})(?:\s+(.+))?$", re.I)
SECTION_RE = re.compile(r"^(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\s+(.+)$")
JUNK_RE = re.compile(r"^(?:NOT FOR SALE|HOT FOR SALE|SCANNED WITH CAMSCANNER|\d{1,3})$", re.I)
EXERCISE_RE = re.compile(r"^(Exercise\s+[\d.-]+|Review\s+Exercise)\s*$", re.I)
EXAMPLE_RE = re.compile(r"^(Examples?\s*(\d+)?\s*:?)\s*(.*)$", re.I)
# Do not mistake numeric data, graph labels, or measurements for question
# numbers. OCR often drops the punctuation after a numbered prompt, so allow
# that form only when it begins with a recognizable instruction verb.
QUESTION_RE = re.compile(
    r"^(\d{1,2})(?:[.)]\s+|\s+(?=(?:Find|Calculate|Simplify|Determine|Solve|"
    r"Write|State|Show|Verify|Check|Tick|Choose|Tell|Round|Compare|Arrange|"
    r"Express|Convert|Complete|Identify|Factor|Estimate|Draw|Plot|Measure|"
    r"What|How|If|There|A\s|An\s|The\s)))(.+)$",
    re.I,
)


def read_lines():
    result = []
    for path in sorted((ROOT / "Word").glob("*.docx")):
        with ZipFile(path) as archive:
            document = ET.fromstring(archive.read("word/document.xml"))
        for para in document.findall(".//w:p", NS):
            value = "".join(node.text or "" for node in para.findall(".//w:t", NS))
            value = re.sub(r"\s+", " ", value).strip()
            if value:
                result.append(value)
    return result


def read_answer_key(lines, chapters):
    """Attach the printed answer-key transcription to its exercise set."""
    key_start = next((i for i, line in enumerate(lines) if line.strip().lower() == "answer key"), None)
    if key_start is None:
        return
    chapter_by_number = {chapter["number"]: chapter for chapter in chapters}
    current_unit = None
    current_title = None
    current_lines = []

    def flush():
        nonlocal current_title, current_lines
        exercise_unit = int(re.search(r"Exercise\s+(\d{1,2})[.-]", current_title, re.I).group(1)) if current_title and re.search(r"Exercise\s+(\d{1,2})[.-]", current_title, re.I) else current_unit
        if current_title and exercise_unit in chapter_by_number:
            chapter = chapter_by_number[exercise_unit]
            normalized = re.sub(r"[ -]+", ".", current_title.lower()).strip(".")
            exercise = next((item for item in chapter["exercises"]
                             if re.sub(r"[ -]+", ".", item["title"].lower()).strip(".") == normalized), None)
            if exercise and current_lines:
                exercise["answerKeyText"] = "\n".join(current_lines).strip()
        current_title, current_lines = None, []

    # The first exercise heading is OCR'd immediately before the "Answer Key"
    # heading in this scan, so retain that short leading block as Exercise 1.1.
    first_heading = next((i for i in range(key_start - 1, max(-1, key_start - 10), -1)
                          if re.fullmatch(r"Exercise\s+1[.-]1", lines[i], re.I)), None)
    if first_heading is not None:
        current_unit = 1
        current_title = "Exercise 1.1"
        current_lines.extend(lines[first_heading + 1:key_start])

    exercise_re = re.compile(r"Exercise\s+(\d{1,2}[.-]\d{1,2})(?=\s|$)", re.I)
    for line in lines[key_start + 1:]:
        unit_match = re.match(r"Unit\s+(\d{1,2})\s*:", line, re.I)
        if unit_match:
            flush()
            current_unit = int(unit_match.group(1))
            continue
        exercise_matches = list(exercise_re.finditer(line))
        if exercise_matches:
            prefix = line[:exercise_matches[0].start()].strip()
            if prefix and current_title:
                current_lines.append(prefix)
                flush()
            preceding_exercise = {"9.2": "9.1"}.get(exercise_matches[0].group(1).replace("-", "."))
            if prefix and preceding_exercise:
                chapter = chapter_by_number.get(9)
                prior = next((item for item in chapter["exercises"] if item["title"] == f"Exercise {preceding_exercise}"), None) if chapter else None
                if prior:
                    prior["answerKeyText"] = prefix
            flush()
            for match_index, exercise_match in enumerate(exercise_matches):
                current_unit = int(exercise_match.group(1).split(".")[0].split("-")[0])
                current_title = "Exercise " + exercise_match.group(1).replace("-", ".")
                tail_end = exercise_matches[match_index + 1].start() if match_index + 1 < len(exercise_matches) else len(line)
                tail = line[exercise_match.end():tail_end].strip()
                current_lines = [tail] if tail else []
                if match_index + 1 < len(exercise_matches):
                    flush()
            continue
        if re.match(r"Review\s+Exercise\b", line, re.I):
            flush()
            current_title = "Review Exercise"
            tail = re.sub(r"^Review\s+Exercise\b", "", line, flags=re.I).strip()
            if tail:
                current_lines.append(tail)
            continue
        if current_title:
            current_lines.append(line)
    flush()


def build():
    lines = read_lines()
    answer_key_start = next((i for i, line in enumerate(lines) if line.strip().lower() == "answer key"), len(lines))
    pre_answer_heading = next((i for i in range(answer_key_start - 1, max(-1, answer_key_start - 10), -1)
                               if re.fullmatch(r"Exercise\s+1[.-]1", lines[i], re.I)), answer_key_start)
    starts = []
    for index, line in enumerate(lines):
        match = UNIT_RE.match(line)
        if match and int(match.group(1)) in range(1, 14):
            # Ignore the answer-key contents, which repeat the unit headings.
            if index > 10500:
                break
            number = int(match.group(1))
            title = (match.group(2) or (lines[index + 1] if index + 1 < len(lines) else "")).strip()
            if number == 13 and not match.group(2) and index + 2 < len(lines):
                title = f"{title} {lines[index + 2]}".strip()
            if number == 2:
                title = "Laws of Operations"
            elif number == 13:
                title = "Data Management and Probability"
            starts.append((index, number, title))

    chapters = []
    for unit_index, (start, number, title) in enumerate(starts):
        end = starts[unit_index + 1][0] if unit_index + 1 < len(starts) else pre_answer_heading
        body_start = start + 2
        body = [line for line in lines[body_start:end]
                if not JUNK_RE.fullmatch(line) and not UNIT_RE.match(line)]
        sections = []
        exercises = []
        examples = []
        current_title = "Student Learning Outcomes"
        current = []
        active_kind = None
        active_title = None
        active_lines = []

        def flush_active():
            nonlocal active_kind, active_title, active_lines
            if active_kind == "exercise":
                exercises.append(make_exercise(active_title, active_lines, len(exercises) + 1))
            elif active_kind == "example":
                examples.append(make_example(active_title, active_lines, len(examples) + 1))
            active_kind = None
            active_title = None
            active_lines = []

        for line in body:
            heading = SECTION_RE.match(line)
            exercise_heading = EXERCISE_RE.match(line)
            example_heading = EXAMPLE_RE.match(line)
            if line.strip().lower() == "introduction":
                flush_active()
                if current:
                    sections.append(make_section(current_title, current))
                current_title = "Introduction"
                current = [line]
                continue
            if exercise_heading:
                flush_active()
                if current:
                    sections.append(make_section(current_title, current))
                    current = []
                active_kind = "exercise"
                active_title = exercise_heading.group(1)
                continue
            if example_heading:
                flush_active()
                if current:
                    sections.append(make_section(current_title, current))
                    current = []
                active_kind = "example"
                active_title = example_heading.group(1).rstrip(":").strip()
                if example_heading.group(3):
                    active_lines.append(example_heading.group(3))
                continue
            if heading and int(heading.group(1).split(".")[0]) == number:
                flush_active()
                if current:
                    sections.append(make_section(current_title, current))
                current_title = f"{heading.group(1)} {heading.group(2)}"
                current = [line]
            else:
                if active_kind:
                    active_lines.append(line)
                else:
                    current.append(line)
        flush_active()
        if current:
            sections.append(make_section(current_title, current))
        unique_exercises = []
        seen_exercises = set()
        for exercise in exercises:
            signature = (exercise["title"].lower(), tuple(problem["question"] for problem in exercise["problems"]))
            if signature not in seen_exercises:
                seen_exercises.add(signature)
                unique_exercises.append(exercise)
        exercises = unique_exercises
        chapters.append({
            "number": number,
            "id": f"unit-{number}",
            "title": title,
            "titleUrdu": "",
            "type": "chapter",
            "sections": sections,
            "exercises": exercises,
            "workedExamples": examples,
            "englishSummary": f"Source transcription for Unit {number}: {title}.",
            "urduSummary": "",
            "source": "Khyber Pakhtunkhwa Textbook Board Class 7 Mathematics; verify diagrams and notation against the scanned pages.",
        })
    read_answer_key(lines, chapters)
    # This first exercise is legible in the supplied page images; correct the
    # OCR column-order errors against the printed page rather than preserving them.
    first_exercise = next((item for item in chapters[0]["exercises"]
                           if item["title"].lower().replace(" ", "") == "exercise1-1"), None)
    if first_exercise:
        first_exercise["problems"] = [
            {"qNo": "1", "question": "Which of the following are rational numbers?\na) 3/4\nb) 4\nc) 6/0\nd) −9/8\ne) 7/−2\nf) 66/1"},
            {"qNo": "2", "question": "Tell the place value of each digit of the given numbers.\na) 5,487,234\nb) 782,398\nc) 1,572,009\nd) 4.186\ne) 8.200\nf) 0.7694"},
            {"qNo": "3", "question": "Explain the place value of whole numbers, fractions, decimals and rational numbers by showing them in the place value table."},
        ]

    def replace_exercise(unit_number, title, entries):
        chapter = next(chapter for chapter in chapters if chapter["number"] == unit_number)
        exercise = next((item for item in chapter["exercises"] if item["title"] == title), None)
        if exercise is None:
            exercise = {"exercise": str(len(chapter["exercises"]) + 1), "title": title, "problems": []}
            chapter["exercises"].append(exercise)
        exercise["problems"] = [
            {"qNo": str(number), "question": question, "solution": solution}
            for number, question, solution in entries
        ]

    # Unit 1 exercises 1.1–1.3 were checked against the scanned opening pages
    # (printed pp. 3–10). Restore every printed question and solve every part;
    # OCR had dropped subparts and merged unrelated prompts into single cards.
    replace_exercise(1, "Exercise 1-1", [
        (1, "Which of the following are rational numbers?\na) 3/4\nb) 4\nc) 6/0\nd) −9/8\ne) 7/−2\nf) 66/1",
         "A rational number can be written as p/q where p and q are integers and q ≠ 0.\na) 3/4: rational.\nb) 4 = 4/1: rational.\nc) 6/0: not rational because the denominator is 0.\nd) −9/8: rational.\ne) 7/−2 = −7/2: rational.\nf) 66/1 = 66: rational."),
        (2, "Tell the place value of each digit of the given numbers.\na) 5,487,234\nb) 782,398\nc) 1,572,009\nd) 4.186\ne) 8.200\nf) 0.7694",
         "a) 5,487,234: 5 millions; 4 hundred-thousands; 8 ten-thousands; 7 thousands; 2 hundreds; 3 tens; 4 ones.\nb) 782,398: 7 hundred-thousands; 8 ten-thousands; 2 thousands; 3 hundreds; 9 tens; 8 ones.\nc) 1,572,009: 1 million; 5 hundred-thousands; 7 ten-thousands; 2 thousands; 0 hundreds; 0 tens; 9 ones.\nd) 4.186: 4 ones; 1 tenth; 8 hundredths; 6 thousandths.\ne) 8.200: 8 ones; 2 tenths; 0 hundredths; 0 thousandths.\nf) 0.7694: 0 ones; 7 tenths; 6 hundredths; 9 thousandths; 4 ten-thousandths."),
        (3, "Explain the place value of whole numbers, fractions, decimals and rational numbers by showing them in a place-value table.",
         "Place each digit in its column; a digit's value is its digit multiplied by the value of its place. Example: 532.678 = 5 hundreds + 3 tens + 2 ones + 6 tenths + 7 hundredths + 8 thousandths. In table form: Hundreds 5 | Tens 3 | Ones 2 | Tenths 6 | Hundredths 7 | Thousandths 8. A fraction such as 3/4 = 0.75 occupies 7 tenths and 5 hundredths. A whole number such as 4 is 4 ones (or 4/1). This demonstrates place value for whole, decimal and rational forms."),
    ])
    replace_exercise(1, "Exercise 1.2", [
        (1, "Round each number to the nearest 10, 100 and 1000.\na) 53,152\nb) 898,430\nc) 7,431,897\nd) 1,399,267",
         "a) 53,152 → nearest 10: 53,150; nearest 100: 53,200; nearest 1000: 53,000.\nb) 898,430 → 898,430; 898,400; 898,000.\nc) 7,431,897 → 7,431,900; 7,431,900; 7,432,000.\nd) 1,399,267 → 1,399,270; 1,399,300; 1,399,000."),
        (2, "Calculate. Then estimate by rounding the numbers to check whether each answer is reasonable.\na) 6258 + 3422\nb) 11,852 + 48,412\nc) 15,203 − 10,545\nd) 49,396 − 22,415\ne) 624 × 23\nf) 988 × 18\ng) 13,216 ÷ 56\nh) 32,436 ÷ 34",
         "a) 6,258 + 3,422 = 9,680. Estimate: 6,300 + 3,400 = 9,700; reasonable.\nb) 11,852 + 48,412 = 60,264. Estimate: 11,900 + 48,400 = 60,300; reasonable.\nc) 15,203 − 10,545 = 4,658. Estimate: 15,200 − 10,500 = 4,700; reasonable.\nd) 49,396 − 22,415 = 26,981. Estimate: 49,400 − 22,400 = 27,000; reasonable.\ne) 624 × 23 = 14,352. Estimate: 600 × 20 = 12,000; this is a coarse estimate (the textbook answer key labels it not reasonable, though the exact product is correct).\nf) 988 × 18 = 17,784. Estimate: 1,000 × 20 = 20,000; reasonable as a rough estimate (the printed key labels it not reasonable).\ng) 13,216 ÷ 56 = 236 exactly. Estimate: 13,200 ÷ 60 ≈ 220; close.\nh) 32,436 ÷ 34 = 954 exactly. Estimate: 32,000 ÷ 30 ≈ 1,067; a rough estimate; the printed key labels it not reasonable."),
    ])
    replace_exercise(1, "Exercise 1.3", [
        (1, "Represent the following integer intervals on number lines.\ni) −2 to +5\nii) −8 to 0\niii) −5 to +5",
         "i) Mark consecutive ticks −2, −1, 0, 1, 2, 3, 4, 5 and highlight the interval from −2 through +5.\nii) Mark −8, −7, −6, −5, −4, −3, −2, −1, 0 and highlight −8 through 0.\niii) Mark −5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5 and highlight −5 through +5. The ticks are equally spaced with negative values left of 0 and positive values right of 0."),
        (2, "Write the corresponding opposite-sign numbers.\ni) −2\nii) +5\niii) +10\niv) −7\nv) −23",
         "The corresponding number has the same absolute value and the opposite sign: i) +2; ii) −5; iii) −10; iv) +7; v) +23."),
        (3, "Write the numerical (absolute) value of each integer: +2, +7, 0, −1, −7, +5, −5, −15, +13, +12, −14.",
         "Absolute value is distance from 0, so remove the sign (and |0| = 0): 2, 7, 0, 1, 7, 5, 5, 15, 13, 12, 14."),
        (4, "Arrange the absolute or numerical values in ascending and descending order.\na) +18, +9, 0, +1, +5, +20\nb) +18, +10, −1, +1, 0, +20\nc) −15, 0, −10, −3, −1, +1, +5, +10, −7\nd) +10, −1, +1, +15, +10, −7\ne) +17, +20, 17, +1, −5, +5, +19, +13, −13, −11",
         "First take absolute values, then sort.\na) Ascending: 0, 1, 5, 9, 18, 20. Descending: 20, 18, 9, 5, 1, 0.\nb) Ascending: 0, 1, 1, 10, 18, 20. Descending: 20, 18, 10, 1, 1, 0.\nc) Absolute values are 15, 0, 10, 3, 1, 1, 5, 10, 7. Ascending: 0, 1, 1, 3, 5, 7, 10, 10, 15. Descending: 15, 10, 10, 7, 5, 3, 1, 1, 0.\nd) Absolute values are 10, 1, 1, 15, 10, 7. Ascending: 1, 1, 7, 10, 10, 15. Descending: 15, 10, 10, 7, 1, 1.\ne) Absolute values are 17, 20, 17, 1, 5, 5, 19, 13, 13, 11. Ascending: 1, 5, 5, 11, 13, 13, 17, 17, 19, 20. Descending: 20, 19, 17, 17, 13, 13, 11, 5, 5, 1."),
        (5, "Junaid paid a loan of Rs 30 from his pocket money. Represent this using a positive or negative number.",
         "A payment reduces his money, so it is represented by −30 rupees."),
        (6, "Hammad got Rs 200 on Eid-ul-Fitr. Represent this using a positive or negative number.",
         "Receiving money increases his amount, so it is represented by +200 rupees."),
        (7, "If +6 represents 6 m above sea level, what does −6 represent?",
         "The negative sign means the opposite direction from above sea level. −6 represents 6 m below sea level."),
        (8, "If −10 represents 10 units left from zero on the number line, what does +5 represent?",
         "+5 represents 5 units to the right of zero on the number line."),
        (9, "If −20 represents a loss of Rs 20 on an article, what does +50 represent?",
         "A positive amount is a gain, so +50 represents a profit of Rs 50."),
        (10, "If +40 represents a clockwise turn of an aircraft, what does −30 represent?",
         "The negative sign indicates the opposite direction, so −30 represents a 30° anticlockwise turn."),
    ])
    replace_exercise(1, "Exercise 1.4", [
        (1, "Represent the following rational numbers on a number line.\na) 3/4\nb) −2/5\nc) 6/4, −35/14\nd) 10/15, −8/24\ne) 7/4, 9/2, −11/4\nf) 1/2, −4/7, −13/4\ng) 9/2, −11/2\nh) 11/4, 39/−26, −14/12",
         "Convert each fraction to a decimal or mixed number, then mark it between the neighboring integers.\na) 3/4 = 0.75.\nb) −2/5 = −0.4.\nc) 6/4 = 1.5; −35/14 = −2.5.\nd) 10/15 = 2/3 ≈ 0.667; −8/24 = −1/3 ≈ −0.333.\ne) 7/4 = 1.75; 9/2 = 4.5; −11/4 = −2.75.\nf) 1/2 = 0.5; −4/7 ≈ −0.571; −13/4 = −3.25.\ng) 9/2 = 4.5; −11/2 = −5.5.\nh) 11/4 = 2.75; 39/−26 = −1.5; −14/12 = −7/6 ≈ −1.167. On every line, place negative values left of 0 and positive values right of 0."),
        (2, "Write three equivalent rational numbers for each.\na) 2/3\nb) 7/24\nc) 4/9\nd) 11/14\ne) 13/25\nf) 5/17\ng) 1/6\nh) 6/29",
         "Multiply numerator and denominator by the same nonzero integer (here 2, 3 and 4).\na) 4/6, 6/9, 8/12.\nb) 14/48, 21/72, 28/96.\nc) 8/18, 12/27, 16/36.\nd) 22/28, 33/42, 44/56.\ne) 26/50, 39/75, 52/100.\nf) 10/34, 15/51, 20/68.\ng) 2/12, 3/18, 4/24.\nh) 12/58, 18/87, 24/116."),
        (3, "Find the reciprocal of each rational number.\na) 9/10\nb) 7/−15\nc) −2/25\nd) 3/31\ne) −13/37",
         "Swap numerator and denominator; keep the sign.\na) 10/9.\nb) −15/7.\nc) −25/2.\nd) 31/3.\ne) −37/13."),
        (4, "Represent the following inequalities on number lines.\na) x > 7\nb) x > 5 and x < 9\nc) x ≥ 1 but x ≤ 6\nd) x > 5 but x ≤ 12\ne) x ≥ 6\nf) x ≥ 2 and x < 10\ng) x ≤ 7 but x ≥ 1\nh) x < 12 but x ≥ 5\ni) x < 9\nj) x ≤ 12\nk) x < 6 but x > 2\nl) x ≥ 3 but x ≤ 8\nm) x ≤ 9 but x > 4\nn) odd numbers x > 3 but x ≤ 15",
         "Use an open circle for < or > and a filled circle for ≤ or ≥; shade the interval satisfying both bounds.\na) (7, ∞).\nb) (5, 9).\nc) [1, 6].\nd) (5, 12].\ne) [6, ∞).\nf) [2, 10).\ng) [1, 7].\nh) [5, 12).\ni) (−∞, 9).\nj) (−∞, 12].\nk) (2, 6).\nl) [3, 8].\nm) (4, 9].\nn) The permitted odd integers are {5, 7, 9, 11, 13, 15}. The scan's interval questions use real number lines; for n, list only odd integers in the stated range."),
        (5, "Represent these sets of integers on number lines.\na) −7 to +6\nb) −9 to +7\nc) −10 to 0\nd) −5 to +13\ne) −5 to +10\nf) −2 to +7\ng) −4 to +5\nh) −2 to 0",
         "Mark each listed integer at equal spacing, with both endpoints included.\na) {−7, −6, −5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5, 6}.\nb) {−9, −8, −7, −6, −5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5, 6, 7}.\nc) {−10, −9, −8, −7, −6, −5, −4, −3, −2, −1, 0}.\nd) {−5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}.\ne) {−5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.\nf) {−2, −1, 0, 1, 2, 3, 4, 5, 6, 7}.\ng) {−4, −3, −2, −1, 0, 1, 2, 3, 4, 5}.\nh) {−2, −1, 0}."),
        (6, "Read the arrows on the decimal number line and write the missing decimals.\na) first arrow\nb) second arrow\nc) third arrow",
         "The scale runs from 0 to 0.2 in equal 0.005 steps. Reading the arrow positions gives a) 0.02; b) 0.115; c) 0.18."),
        (7, "Represent these decimals on number lines.\na) 6.2, 6.9, 6.6\nb) 0.5, 0.1, 0.8, 0.3\nc) 0.03, 0.05, 0.07, 0.08",
         "Place the values in increasing order on equally scaled number lines.\na) 6.2 < 6.6 < 6.9.\nb) 0.1 < 0.3 < 0.5 < 0.8.\nc) 0.03 < 0.05 < 0.07 < 0.08."),
    ])
    replace_exercise(1, "Exercise 1.5", [
        (1, "Express each improper fraction as a mixed number in simplest form.\na) 18/4\nb) 12/9\nc) 26/10",
         "Divide numerator by denominator; the quotient is the whole part and the remainder is the fractional numerator.\na) 18/4 = 4 remainder 2 = 4 2/4 = 4 1/2.\nb) 12/9 = 1 remainder 3 = 1 3/9 = 1 1/3.\nc) 26/10 = 2 remainder 6 = 2 6/10 = 2 3/5."),
        (2, "Write each mixed number as an improper fraction.\na) 1 3/5\nb) 3 5/6\nc) 1 7/9\nd) 3 3/4",
         "Multiply the whole number by the denominator, add the numerator, and keep the same denominator.\na) (1×5+3)/5 = 8/5.\nb) (3×6+5)/6 = 23/6.\nc) (1×9+7)/9 = 16/9.\nd) (3×4+3)/4 = 15/4."),
    ])
    # Exercise 1.6 was checked against the complete scan on printed p.21.
    replace_exercise(1, "Exercise 1.6", [
        (1, "Compare and write <, > or =.\na) 50,856 ; 26,700\nb) 111,245 ; 10,987\nc) 1,236 ; 9,999\nd) 5,680 ; 5,688",
         "Compare place values from left to right.\na) 50,856 > 26,700.\nb) 111,245 > 10,987.\nc) 1,236 < 9,999.\nd) 5,680 < 5,688 (the first three digits match; 0 < 8 in the tens place)."),
        (2, "Arrange in ascending and descending order.\na) 10,820; 1,820; 35,236; 66,102; 90,526\nb) 9,002; 10,364; 8,305; 19,634; 20,465\nc) 24,666; 26,403; 82,023; 31,666; 81,023",
         "a) Ascending: 1,820 < 10,820 < 35,236 < 66,102 < 90,526. Descending: 90,526 > 66,102 > 35,236 > 10,820 > 1,820.\nb) Ascending: 8,305 < 9,002 < 10,364 < 19,634 < 20,465. Descending: 20,465 > 19,634 > 10,364 > 9,002 > 8,305.\nc) Ascending: 24,666 < 26,403 < 31,666 < 81,023 < 82,023. Descending: 82,023 > 81,023 > 31,666 > 26,403 > 24,666."),
        (3, "Which is greater? Give the reason.\na) −666 or −6,666\nb) −2,340 or −234\nc) −10,000 or −1,000\nd) −55 or −555",
         "For negative integers, the one closer to zero is greater.\na) −666 > −6,666.\nb) −234 > −2,340.\nc) −1,000 > −10,000.\nd) −55 > −555."),
        (4, "Arrange each set of integers in ascending and descending order.\na) −5, +4, −13, −1, 0, 3, 7\nb) −5, −3, +3, +2, +11, −12\nc) −33, −12, 0, +11, +9, +5, −16\nd) −12, 0, +17, +11, +6, −8, −5\ne) −3, 0, +1, +8, +7, −5, −4, +9\nf) −15, −11, 0, +23, +24, +27, −14",
         "a) Ascending: −13, −5, −1, 0, 3, 4, 7; descending: 7, 4, 3, 0, −1, −5, −13.\nb) Ascending: −12, −5, −3, 2, 3, 11; descending: 11, 3, 2, −3, −5, −12.\nc) Ascending: −33, −16, −12, 0, 5, 9, 11; descending: 11, 9, 5, 0, −12, −16, −33.\nd) Ascending: −12, −8, −5, 0, 6, 11, 17; descending: 17, 11, 6, 0, −5, −8, −12.\ne) Ascending: −5, −4, −3, 0, 1, 7, 8, 9; descending: 9, 8, 7, 1, 0, −3, −4, −5.\nf) Ascending: −15, −14, −11, 0, 23, 24, 27; descending: 27, 24, 23, 0, −11, −14, −15."),
        (5, "Compare and write <, > or =.\na) 4/7 ; 1/3\nb) −1/2 ; 5/11\nc) 9/4 ; −11/12\nd) −3/4 ; −7/4\ne) 4/9 ; −19/4\nf) 1/7 ; 7/2\ng) −6/7 ; −9/8\nh) 11/13 ; −7/13\ni) −6/15 ; −13/2\nj) −2/5 ; −1/2",
         "Use common denominators or compare signs.\na) 4/7 > 1/3 because 12/21 > 7/21.\nb) −1/2 < 5/11 because a negative is less than a positive.\nc) 9/4 > −11/12 because a positive is greater than a negative.\nd) −3/4 > −7/4 because −3/4 is closer to zero.\ne) 4/9 > −19/4.\nf) 1/7 < 7/2.\ng) −6/7 > −9/8 since −48/56 > −63/56.\nh) 11/13 > −7/13.\ni) −6/15 > −13/2.\nj) −2/5 > −1/2 since −4/10 > −5/10."),
        (6, "Arrange each group of rational numbers in ascending and descending order.\na) 4/7, 3/8, 9/11\nb) 5/9, 7/13, −9/8\nc) 20/21, 23/42, −25/7\nd) −7/3, 6/14, 4/12\ne) 4/3, 8/12, 7/15, −2/7\nf) 6/8, 5/21, 13/16, 15/17\ng) 2/3, 5/7, −9/11, 10/13\nh) 21/23, 7/46, 2/69",
         "Compare values using equivalent fractions or decimals.\na) Ascending: 3/8 < 4/7 < 9/11; descending: 9/11 > 4/7 > 3/8.\nb) Ascending: −9/8 < 7/13 < 5/9; descending: 5/9 > 7/13 > −9/8.\nc) Ascending: −25/7 < 23/42 < 20/21; descending: 20/21 > 23/42 > −25/7.\nd) Ascending: −7/3 < 4/12 < 6/14; descending: 6/14 > 4/12 > −7/3.\ne) Ascending: −2/7 < 7/15 < 8/12 < 4/3; descending: 4/3 > 8/12 > 7/15 > −2/7.\nf) Ascending: 5/21 < 6/8 < 13/16 < 15/17; descending: 15/17 > 13/16 > 6/8 > 5/21.\ng) Ascending: −9/11 < 2/3 < 5/7 < 10/13; descending: 10/13 > 5/7 > 2/3 > −9/11.\nh) Ascending: 2/69 < 7/46 < 21/23; descending: 21/23 > 7/46 > 2/69."),
        (7, "Tick the smaller number in each group.\na) 1.23, 1.22, 1.20\nb) 9.62, 9.09, 9.68, 9.10\nc) 0.234, 0.23, 0.324, 0.214",
         "Write equal decimal places, then compare.\na) 1.20 is smallest.\nb) 9.09 is smallest (9.09 < 9.10 < 9.62 < 9.68).\nc) 0.214 is smallest (0.214 < 0.230 < 0.234 < 0.324)."),
        (8, "Arrange in ascending and descending order.\na) 8.5, 8.56, 8.503\nb) 0.231, 0.001, 0.01\nc) 5.112, 5.013, 5.002",
         "Pad trailing zeros so the decimal places match.\na) 8.500, 8.560, 8.503. Ascending: 8.5 < 8.503 < 8.56; descending: 8.56 > 8.503 > 8.5.\nb) Ascending: 0.001 < 0.01 < 0.231; descending: 0.231 > 0.01 > 0.001.\nc) Ascending: 5.002 < 5.013 < 5.112; descending: 5.112 > 5.013 > 5.002."),
    ])
    # Unit 1 review questions and project checked against printed pp.22–23.
    replace_exercise(1, "Review Exercise", [
        (1, "Choose the right answer.\na) The number a/b, where a and b are integers, is rational if b is: i) zero ii) not zero iii) any number iv) none\nb) A rational number can be represented in the form of: i) geometry ii) fraction iii) circle iv) LCM\nc) The neutral integer is: i) 1 ii) −1 iii) 0 iv) 5\nd) Rational numbers with the same denominator are called: i) equivalent ii) proper iii) like iv) unlike\ne) Round 54.231 to the nearest whole number: i) 54 ii) 55 iii) 542 iv) 553",
         "a) ii, not zero: a rational number has denominator b ≠ 0.\nb) ii, fraction: rational numbers have the form a/b.\nc) iii, 0: zero is the neutral integer.\nd) iii, like rational numbers.\ne) i, 54: the tenths digit is 2 (< 5), so keep 54."),
        (2, "Represent on number lines.\na) −5/4\nb) 8/5\nc) 15/2, −7/4\nd) 1/15, −3/2\ne) 17/3, −18/2\nf) 23, 24, 27\ng) −1, −4, −11\nh) −2, −8, −15",
         "Convert to locate each point; negative values lie left of zero.\na) −5/4 = −1 1/4, between −2 and −1.\nb) 8/5 = 1 3/5, between 1 and 2.\nc) 15/2 = 7 1/2; −7/4 = −1 3/4.\nd) 1/15 ≈ 0.067; −3/2 = −1.5.\ne) 17/3 = 5 2/3; −18/2 = −9.\nf) Mark 23, 24, 27 at equal integer intervals.\ng) Mark −11, −4, −1 in that left-to-right order.\nh) Mark −15, −8, −2 in that left-to-right order."),
        (3, "Write each rational number in reduced form.\na) 54/24\nb) 5/30\nc) 14/84\nd) 77/98\ne) 6/102",
         "Divide numerator and denominator by their greatest common divisor.\na) 54/24 ÷ 6 = 9/4.\nb) 5/30 ÷ 5 = 1/6.\nc) 14/84 ÷ 14 = 1/6.\nd) 77/98 ÷ 7 = 11/14.\ne) 6/102 ÷ 6 = 1/17."),
        (4, "Write three equivalent rational numbers for each.\na) 4/5\nb) 9/11\nc) 6/23\nd) 7/8\ne) 19/25\nf) 51/67",
         "Multiply numerator and denominator by 2, 3 and 4.\na) 8/10, 12/15, 16/20.\nb) 18/22, 27/33, 36/44.\nc) 12/46, 18/69, 24/92.\nd) 14/16, 21/24, 28/32.\ne) 38/50, 57/75, 76/100.\nf) 102/134, 153/201, 204/268."),
        (5, "Compare and write <, > or =.\na) 23/17 ; 21/15\nb) −1/2 ; 3/5\nc) 34 ; 78\nd) −5 ; −7\ne) 17.1 ; 1.5",
         "a) 23/17 < 21/15 because 23×15 = 345 < 357 = 21×17.\nb) −1/2 < 3/5 because negative < positive.\nc) 34 < 78.\nd) −5 > −7 because −5 is closer to zero.\ne) 17.1 > 1.5."),
        (6, "Compare and arrange in ascending and descending order.\na) 14/17, 17/34, 5/51\nb) 3/5, −7/20, −4/21\nc) +21, +13, 0, +25\nd) 65, 39, 84, 56",
         "a) Ascending: 5/51 < 17/34 < 14/17; descending: 14/17 > 17/34 > 5/51.\nb) Ascending: −7/20 < −4/21 < 3/5; descending: 3/5 > −4/21 > −7/20.\nc) Ascending: 0 < 13 < 21 < 25; descending: 25 > 21 > 13 > 0.\nd) Ascending: 39 < 56 < 65 < 84; descending: 84 > 65 > 56 > 39."),
        (7, "Math project: model number sets, ordering, place value and rounding with flash cards, then present the work.",
         "Sample completed display: Natural numbers {1, 2, 3}; whole numbers {0, 1, 2, 3}; integers {−2, −1, 0, 1, 2}; rational numbers {−1/2, 0, 3/4, 2}. The sets nest as N ⊂ W ⊂ Z ⊂ Q. Ordering example: −1/2 < 0 < 3/4 < 2. Place-value example: 4,582 = 4,000 + 500 + 80 + 2. Rounded to nearest 10, 100 and 1,000: 4,580; 4,600; 5,000. Teams can make more cards and check each other's placement."),
    ])

    # Unit 2 exercise wording, subparts, and answers checked against printed
    # pages 26-40 and the answer pages 275-276.
    replace_exercise(2, "Exercise 2.1", [
        (1, "Add the following rational numbers.\na) 3/4 and 4/5\nb) −7/11 and 13/14\nc) −4/9, 7/12 and −3/8\nd) −3/5, −1/10 and −4/15\ne) 2/9 and −4/15\nf) −6/7 and 9/13\ng) 12/15 and −13/17\nh) 4/13, 6/11 and −3/22\ni) −1/7, 1/9 and 1/5",
         "Use the least common denominator in each part.\na) 3/4 + 4/5 = 15/20 + 16/20 = 31/20.\nb) −7/11 + 13/14 = −98/154 + 143/154 = 45/154.\nc) −4/9 + 7/12 − 3/8 = −32/72 + 42/72 − 27/72 = −17/72.\nd) −3/5 − 1/10 − 4/15 = −18/30 − 3/30 − 8/30 = −29/30.\ne) 2/9 − 4/15 = 10/45 − 12/45 = −2/45.\nf) −6/7 + 9/13 = −78/91 + 63/91 = −15/91.\ng) 12/15 − 13/17 = 4/5 − 13/17 = 68/85 − 65/85 = 3/85.\nh) 4/13 + 6/11 − 3/22 = 88/286 + 156/286 − 39/286 = 205/286.\ni) −1/7 + 1/9 + 1/5 = −45/315 + 35/315 + 63/315 = 53/315."),
        (2, "Subtract the following.\na) 1/2 from 3/5\nb) −7/10 from −9/10\nc) −4/9 from 2/27\nd) 5/17 from −3/34\ne) −7/11 from −1/3\nf) −6/13 from 5/14\ng) 9/10 from −1/10\nh) 6/7 from 2/21\ni) 8/13 from 7/11",
         "Remember: subtracting a number means adding its opposite.\na) 3/5 − 1/2 = 6/10 − 5/10 = 1/10.\nb) −9/10 − (−7/10) = −9/10 + 7/10 = −2/10 = −1/5.\nc) 2/27 − (−4/9) = 2/27 + 12/27 = 14/27.\nd) −3/34 − 5/17 = −3/34 − 10/34 = −13/34.\ne) −1/3 − (−7/11) = −11/33 + 21/33 = 10/33.\nf) 5/14 − (−6/13) = 65/182 + 84/182 = 149/182.\ng) −1/10 − 9/10 = −10/10 = −1.\nh) 2/21 − 6/7 = 2/21 − 18/21 = −16/21.\ni) 7/11 − 8/13 = 91/143 − 88/143 = 3/143."),
    ])
    replace_exercise(2, "Exercise 2.2", [
        (1, "Find the additive inverse of each rational number.\na) 4/5\nb) −13/6\nc) 9/−19\nd) 6/23\ne) −31/97",
         "a) −4/5; b) 13/6; c) 9/19; d) −6/23; e) 31/97. Each answer is the given number with its sign reversed."),
        (2, "Verify the following addition properties.\na) −13/14 + 15/28 = 15/28 + (−13/14)\nb) 7/15 + (−6/17) = (−6/17) + 7/15\nc) 9/20 + (14/19 + 1/7) = (9/20 + 14/19) + 1/7\nd) (−3/10 + 11/13) + (−5/11) = −3/10 + (11/13 − 5/11)\ne) −2/3 + (−7/9 + 2/13) = (−2/3 − 7/9) + 2/13\nf) (−1/4 + 1/6) − 1/8 = −1/4 + (1/6 − 1/8)",
         "Evaluate both sides using common denominators.\na) LHS = −13/14 + 15/28 = −26/28 + 15/28 = −11/28. RHS = 15/28 − 26/28 = −11/28.\nb) LHS = 7/15 − 6/17 = 119/255 − 90/255 = 29/255; reversing the addends on the RHS gives the same sum, 29/255 (commutative property).\nc) Both sides are equal by associativity; value = 9/20 + 14/19 + 1/7 = 3537/2660.\nd) Both sides are equal by associativity; value = −3/10 + 11/13 − 5/11 = 131/1430.\ne) Both sides are equal by associativity; value = −2/3 − 7/9 + 2/13 = −151/117.\nf) LHS = (−1/4 + 1/6) − 1/8 = −1/12 − 1/8 = −5/24. RHS = −1/4 + (1/6 − 1/8) = −1/4 + 1/24 = −5/24. Hence both sides match."),
    ])
    replace_exercise(2, "Exercise 2.3", [
        (1, "Multiply.\na) 1/4 × 7/8\nb) (−9/20) × (−13/14)\nc) (−4/9) × 11/12 × (−3/8)\nd) 5/8 × (−1/16) × (−3/7)\ne) 9/11 × (−3/22) × 5/33\nf) (−3/19) × 7/20",
         "a) 7/32; b) 117/280; c) 11/72; d) 15/896; e) −45/2662; f) −21/380."),
        (2, "Divide.\na) 7/12 ÷ 14/39\nb) (−25/31) ÷ (5/−62)\nc) (−1/2) ÷ 4/7\nd) 9/11 ÷ 33/35\ne) (−19/21) ÷ (−21/38)\nf) 15/23 ÷ (−23/25)\ng) 8/(−13) ÷ 26/37\nh) (−1/7) ÷ (−2/15)",
         "a) 13/8; b) 10; c) −7/8; d) 105/121; e) 722/441; f) −375/529; g) −148/169; h) 15/14."),
    ])
    replace_exercise(2, "Exercise 2.4", [
        (1, "Find the multiplicative inverse of each rational number.\na) 13/41\nb) −16/17\nc) 15/−31\nd) −5/−33\ne) −97/101",
         "a) 41/13; b) −17/16; c) −31/15; d) 33/5; e) −101/97."),
        (2, "Verify the commutative property of multiplication for each given pair of rational numbers (a-c).",
         "In each part, multiply the two factors in either order. The products are equal: a) 2/35; b) −368/595; c) 11/15."),
        (3, "Verify the associative property of multiplication for each given triple of rational numbers (a-d).",
         "Evaluate both groupings; multiplication gives the same product on each side in every part. This verifies (a × b) × c = a × (b × c)."),
        (4, "Verify the distributive property of multiplication over addition or subtraction for each expression (a-c).",
         "Expand the factor across each term inside the parentheses. The left and right sides agree in a), b), and c), verifying a(b ± c) = ab ± ac."),
    ])
    replace_exercise(2, "Exercise 2.5", [
        (1, "An empty pot weighs 1/4 kg. Filled with sugar it weighs 3 4/5 kg. Find (a) the sugar's weight and (b) the pot's weight when half-filled.",
         "a) 3 4/5 − 1/4 = 76/20 − 5/20 = 71/20 = 3 11/20 kg. b) 1/4 + (1/2 × 71/20) = 81/40 = 2 1/40 kg."),
        (2, "Ahtasham buys 16/5 litres of honey and Talha buys 12/7 litres. Find (a) the total and (b) how much more Ahtasham buys.",
         "a) 16/5 + 12/7 = 172/35 = 4 32/35 L. b) 16/5 − 12/7 = 52/35 = 1 17/35 L."),
        (3, "Hina uses 2 5/9 m of cloth for floor cushions and 1 5/7 m for two pillows from 5 m. Find (a) the cloth used and (b) the cloth left.",
         "a) 23/9 + 12/7 = 269/63 = 4 17/63 m. b) 5 − 269/63 = 46/63 m."),
        (4, "2/5 of a stick is painted red and 1/3 white. The rest is blue. What fraction is blue?",
         "1 − 2/5 − 1/3 = 15/15 − 6/15 − 5/15 = 4/15."),
        (5, "A park perimeter is 10 km. If 4/5 of the wall is built, what fraction of the wall remains incomplete?",
         "1 − 4/5 = 1/5 of the wall, which is 2 km of the 10 km perimeter."),
        (6, "Tariq sells 2 2/5, 4 1/5, 3 2/3, and 4 1/2 kg of almonds Monday to Thursday. Friday's amount is half the four-day total. Find Friday's amount and the Monday-Friday total.",
         "Monday–Thursday: integer parts total 13; fractional parts 2/5 + 1/5 + 2/3 + 1/2 = 53/30 = 1 23/30. Thus the four-day total is 14 23/30 = 443/30 kg. Friday is half: (1/2)(443/30) = 443/60 = 7 23/60 kg. The question's part (b) asks for the amount sold Monday–Thursday: 14 23/30 kg."),
        (7, "Hiba's room is 6.5 m by 5.7 m. Find the carpet cost at Rs 140 per m².",
         "Area = 6.5 × 5.7 = 37.05 m². Cost = 37.05 × 140 = Rs 5,187."),
    ])
    replace_exercise(2, "Exercise 2.6", [
        (1, "Simplify using BODMAS; round answers to 3 decimal places where needed.\na) 2 1/3 + (3 1/3 + 1 2/3)\nb) 2 1/5 + {4 × (3/2 + 7/5)} − 5/29\nc) 3/5 × [2/3 − (2 3/5 + 5/6 − 29/10)]\nd) 1 7/8 + [5 1/6 × {2 2/5 × (4/5 − 1/2)}]\ne) (1 1/4)^2 × [6/25 + 3/5 + (1/3 + 4 1/2 − 2 1/3)]\nf) 3.3 + 2.02 × (50.85 − 32.15)\ng) (3.9)^2 + (15.89 × 22.8 − 70.1)\nh) 0.088 × [3.1 + 2.02 × (2 − 0.75)]\ni) 9 − [2.4285 + (1.0714 + 0.7142)]\nj) 5.5 − [1.55 × {(3.25 − 0.25) × 0.572}]",
         "Follow brackets and powers first, then multiplication, then addition/subtraction.\na) (3 1/3 + 1 2/3) = 5; 2 1/3 + 5 = 7 1/3.\nb) 2 1/5 + 4(3/2 + 7/5) − 5/29 = 11/5 + 4(29/10) − 5/29 = 69/5 − 5/29 = 1976/145 = 13 91/145.\nc) Inner parentheses: 2 3/5 + 5/6 − 29/10 = 13/5 + 5/6 − 29/10 = 8/15. Then 3/5(2/3 − 8/15) = 3/5 × 2/15 = 2/25.\nd) 4/5 − 1/2 = 3/10; 2 2/5 × 3/10 = 18/25; 5 1/6 × 18/25 = 93/25. Finally 1 7/8 + 93/25 = 15/8 + 93/25 = 1119/200 = 5.595.\ne) 1 1/4 squared = 25/16. Inner parentheses: 1/3 + 4 1/2 − 2 1/3 = 5/2; bracket = 6/25 + 3/5 + 5/2 = 167/50. Product = 25/16 × 167/50 = 167/32 = 5.219 (to 3 d.p.).\nf) 50.85 − 32.15 = 18.70; 3.3 + 2.02 × 18.70 = 3.3 + 37.774 = 41.074.\ng) 3.9² = 15.21; 15.89 × 22.8 = 362.292; 15.21 + (362.292 − 70.1) = 307.402.\nh) 2 − 0.75 = 1.25; 3.1 + 2.02 × 1.25 = 5.625; 0.088 × 5.625 = 0.495.\ni) 1.0714 + 0.7142 = 1.7856; 2.4285 + 1.7856 = 4.2141; 9 − 4.2141 = 4.7859 ≈ 4.786.\nj) 3.25 − 0.25 = 3; 3 × 0.572 = 1.716; 1.55 × 1.716 = 2.6598; 5.5 − 2.6598 = 2.8402 ≈ 2.840."),
    ])
    replace_exercise(2, "Review Exercise", [
        (1, "Choose the correct option.\na) 7/9 + 1/2: i) 23/18 ii) 8/18 iii) 20/18 iv) 15/18\nb) 5/13 + (−7/26): i) −3/26 ii) +3/26 iii) −2/26 iv) 2/26\nc) −11/15 + (−2/15): i) −9/15 ii) −13/15 iii) 9/15 iv) 13/15\nd) Rational numbers with the same denominator are called: i) non-zero ii) proper iii) like iv) unlike\ne) 14/21 is equivalent to: i) 7/3 ii) 2/3 iii) 2/21 iv) 3/2\nf) 1/6 + (−2/5): i) −7/30 ii) 2/6 iii) −2/5 iv) −2/11\ng) Additive inverse of 5/6: i) 0 ii) 1 iii) −5/6 iv) −6/5",
         "Use common denominators.\na) 7/9 + 1/2 = 14/18 + 9/18 = 23/18 (i).\nb) 5/13 − 7/26 = 10/26 − 7/26 = 3/26 (ii).\nc) (−11−2)/15 = −13/15 (ii).\nd) Same-denominator rational numbers are like rational numbers (iii).\ne) 14/21 ÷ 7 = 2/3 (ii).\nf) 1/6 − 2/5 = 5/30 − 12/30 = −7/30 (i).\ng) The additive inverse is −5/6 (iii), since their sum is zero."),
        (2, "Add.\na) 7/15 and 3/31\nb) −11/41 and −2/82\nc) −3/17, 5/17 and −3/34\nd) −14/15, −17/18 and 19/20\ne) 4/27 and −1/24\nf) 11/21, −7/21 and −11/42",
         "Find a common denominator in each part.\na) 217/465 + 45/465 = 262/465.\nb) −11/41 − 1/41 = −12/41.\nc) −6/34 + 10/34 − 3/34 = 1/34.\nd) −168/180 − 170/180 + 171/180 = −167/180.\ne) 32/216 − 9/216 = 23/216.\nf) 22/42 − 14/42 − 11/42 = −3/42 = −1/14."),
        (3, "Subtract.\na) 9/14 from 2/28\nb) −17/21 from −18/23\nc) −4/9 from 2/27\nd) 5/17 from −3/34\ne) −51/61 from −2/122\nf) 5/42 from 1/21",
         "Subtract the first named number from the second.\na) 2/28 − 9/14 = 1/14 − 9/14 = −4/7.\nb) −18/23 − (−17/21) = −378/483 + 391/483 = 13/483.\nc) 2/27 − (−4/9) = 2/27 + 12/27 = 14/27.\nd) −3/34 − 5/17 = −3/34 − 10/34 = −13/34.\ne) −2/122 − (−51/61) = −1/61 + 51/61 = 50/61.\nf) 1/21 − 5/42 = 2/42 − 5/42 = −1/14."),
        (4, "Multiply.\na) 11/14 and 27/28\nb) −34/35 and −7/17\nc) −1/9, 5/12 and −2/25\nd) −13/15, −13/20 and 7/25\ne) 7/88, 11/35 and 33/37\nf) 98/99, −33/44 and −7/8",
         "Multiply numerators and denominators, then reduce.\na) (11×27)/(14×28) = 297/392.\nb) (−34×−7)/(35×17) = 238/595 = 2/5.\nc) (−1×5×−2)/(9×12×25) = 10/2700 = 1/270.\nd) (−13×−13×7)/(15×20×25) = 1183/7500.\ne) (7×11×33)/(88×35×37) = 33/1480.\nf) (98×−33×−7)/(99×44×8) = 343/528."),
        (5, "Find the reciprocal of each: 98/99, 56/−78, −3/37, −7/41, −39/71.",
         "a) 99/98; b) −39/28; c) −37/3; d) −41/7; e) −71/39."),
        (6, "Divide.\na) 17/22 ÷ 24/51\nb) −2 6/37 ÷ 74/−75\nc) −1/3 ÷ 3/4\nd) 49/51 ÷ 13/17\ne) −23/41 ÷ −21/31\nf) 32/33 ÷ −62/77\ng) −1/13 ÷ 26/37\nh) −1/9 ÷ −2/81",
         "Change division to multiplication by the reciprocal.\na) 17/22 × 51/24 = 289/176.\nb) −80/37 × (−75/74) = 3000/1369.\nc) −1/3 × 4/3 = −4/9.\nd) 49/51 × 17/13 = 49/39.\ne) −23/41 × (−31/21) = 713/861.\nf) 32/33 × (−77/62) = −112/93.\ng) −1/13 × 37/26 = −37/338.\nh) −1/9 × (−81/2) = 9/2."),
        (7, "Find the additive inverses of −77/78, 16/33, 44/−53, −1/3 and −21/56.",
         "a) 77/78; b) −16/33; c) 44/53; d) 1/3; e) 21/56."),
        (8, "Find the multiplicative inverses of 1/31, −6/21, 1/−100, −4/−133 and −17/121.",
         "a) 31; b) −7/2; c) −100; d) 133/4; e) −121/17."),
        (9, "Verify commutative property under addition and multiplication.\na) 2/3, 8/9\nb) 3/4, 5/8\nc) 11/28, 33/44\nd) 11/15, −21/56\ne) −1/3, −16/33\nf) 24/51, −39/71",
         "Switching the order leaves the result unchanged.\na) 2/3 + 8/9 = 22/9 = 8/9 + 2/3.\nb) 3/4 + 5/8 = 11/8 = 5/8 + 3/4.\nc) 11/28 + 33/44 = 8/7 = 33/44 + 11/28.\nd) 11/15 × (−21/56) = −11/40, in either order.\ne) (−1/3)(−16/33) = 16/99, in either order.\nf) 24/51 × (−39/71) = −312/1207, in either order."),
        (10, "Verify the associative property under addition (a–c) and multiplication (d–f).\na) 17/22, 1/6, 2/−13\nb) 1/7, −2/77, 5/14\nc) 2/−3, −1/4, −21/31\nd) 5/−44, 9/47, −1/21\ne) 56/57, 11/16, −2/12\nf) −6/7, 37/−42, 3/17",
         "Re-grouping does not change the result.\na) Both groupings equal 17/22 + 1/6 − 2/13 = 337/429.\nb) Both groupings equal 1/7 − 2/77 + 5/14 = 73/154.\nc) Both groupings equal −2/3 − 1/4 − 21/31 = −593/372.\nd) Both groupings equal (−5/44)(9/47)(−1/21) = 15/14476.\ne) Both groupings equal (56/57)(11/16)(−1/6) = −77/684.\nf) Both groupings equal (−6/7)(−37/42)(3/17) = 111/833."),
        (11, "Simplify using BODMAS.\na) 13.65 − [4.65 + 3 × {18.45 − (3.65 × 3.75)}]\nb) [{(9 × 1/3 − 3/9) ÷ 5/16} × 5/12 + 3/4]",
         "a) 3.65×3.75=13.6875; 18.45−13.6875=4.7625; 4.65+3×4.7625=18.9375; 13.65−18.9375=−5.2875.\nb) The scan shows division by 5/16 inside the braces: 9×1/3−3/9=3−1/3=8/3; (8/3)÷(5/16)=128/15; ×5/12=8/9; +3/4=59/36. The OCR answer-key transcription gives 155/36, which does not match the visible expression; use 59/36 for the expression as printed in the page scan."),
        (12, "Rohan pays Rs 36.45 for a rickshaw, Rs 34.50 for a metro bus, and Rs 56.56 for a metro train from Rs 1,300. How much remains?",
         "Spent = 36.45 + 34.50 + 56.56 = Rs 127.51. Remaining = 1,300 − 127.51 = Rs 1,172.49."),
        (13, "A large pack has 8 erasers, a medium pack 15, and a small pack 20. Ibrahim has 3 small, 2 medium, and 2 large packs. Find the total erasers.",
         "3 × 20 + 2 × 15 + 2 × 8 = 60 + 30 + 16 = 106 erasers."),
        (14, "Usman’s family uses 13 3/9 L for bathing, 10 5/15 L for cleaning, and 6 2/9 L for cooking. Find the total.",
         "13 1/3 + 10 1/3 + 6 2/9 = 29 8/9 L."),
        (15, "A restaurant sells 3 sandwiches at Rs 250 each, 2 cold drinks at Rs 180 each, and coffee for Rs 210. Add Rs 112 tax. From Rs 5,000, find the bill and change.",
         "Bill = 3(250) + 2(180) + 210 + 112 = Rs 1,432. Change = 5,000 − 1,432 = Rs 3,568."),
        (16, "Ali has Rs 564.32 and Fahad Rs 876.89. How much more do they need together to buy a book costing Rs 2,234.23?",
         "Together they have Rs 1,441.21. Needed = 2,234.23 − 1,441.21 = Rs 793.02."),
        (17, "Math project: make flash cards showing properties of rational numbers, explain each property, and present worked examples.",
         "Sample cards: Commutative addition: 2/3 + 1/4 = 1/4 + 2/3 = 11/12. Associative addition: (1/2 + 1/3) + 1/6 = 1/2 + (1/3 + 1/6) = 1. Distributive property: 2/5 × (3/4 + 1/2) = 2/5 × 3/4 + 2/5 × 1/2 = 1/2. Each group can prepare the property name, statement and both evaluated sides on a card."),
    ])
    # Unit 3 questions were merged by OCR across lines and columns. Rebuild the
    # numbered exercise groups from the page scans (printed pages 46–56) and
    # attach answers to those exact question numbers.
    replace_exercise(3, "Exercise 3.1", [
        (1, "Find the square of each number: a) 16; b) 625; c) 2560; d) 1089; e) 562; f) 1600; g) 810; h) 2500; i) 490; j) 5600; k) 10200; l) 1210.",
         "a) 256; b) 390,625; c) 6,553,600; d) 1,185,921; e) 315,844; f) 2,560,000; g) 656,100; h) 6,250,000; i) 240,100; j) 31,360,000; k) 104,040,000; l) 1,464,100. Example: 1089² = (1100−11)² = 1,185,921."),
        (2, "Without calculating the full squares, decide which of these could be perfect squares by checking their ending digit(s): 441, 625, 2560, 1089, 562, 1600, 810, 2500, 490, 5600, 10200, 1210.",
         "A square cannot end in 2, 3, 7, or 8. Possible by the last-digit test: 441, 625, 1089, 1600, 2500, 5600, 10200. Not possible: 2560, 562, 810, 490, 1210. A possible ending does not prove a number is a square; for example, 5600 and 10200 are not perfect squares."),
        (3, "Use prime factorisation to test whether these are perfect squares: a) 49; b) 98; c) 144; d) 784; e) 125; f) 1600; g) 147; h) 81; i) 450; j) 630; k) 90; l) 900.",
         "A number is a perfect square when every prime has an even exponent. a) 49=7², yes; b) 98=2×7², no; c) 144=2⁴×3², yes; d) 784=2⁴×7², yes; e) 125=5³, no; f) 1600=2⁶×5², yes; g) 147=3×7², no; h) 81=3⁴, yes; i) 450=2×3²×5², no; j) 630=2×3²×5×7, no; k) 90=2×3²×5, no; l) 900=2²×3²×5², yes."),
        (4, "Tick the perfect squares of even numbers: a) 81; b) 121; c) 256; d) 324; e) 49; f) 625; g) 25.",
         "Tick c) 256 = 16² and d) 324 = 18². The other perfect squares listed have odd square roots."),
        (5, "For each proper fraction, square it and verify that its square is smaller: a) 3/4; b) 9/10; c) 17/20; d) 15/17; e) 2/7; f) 4/11; g) 6/13; h) 11/21; i) 45/46; j) 99/100; k) 34/45; l) 17/100.",
         "a) 9/16 < 3/4; b) 81/100 < 9/10; c) 289/400 < 17/20; d) 225/289 < 15/17; e) 4/49 < 2/7; f) 16/121 < 4/11; g) 36/169 < 6/13; h) 121/441 < 11/21; i) 2025/2116 < 45/46; j) 9801/10000 < 99/100; k) 1156/2025 < 34/45; l) 289/10000 < 17/100. Since 0 < x < 1, multiplying x by itself makes it smaller."),
        (6, "Square each decimal and compare it with the original: a) 0.2; b) 5.1; c) 2.1; d) 6.8; e) 1.02; f) 0.05; g) 0.23; h) 0.98; i) 0.55; j) 0.10; k) 0.89; l) 3.24.",
         "a) 0.2²=0.04<0.2; b) 5.1²=26.01>5.1; c) 2.1²=4.41>2.1; d) 6.8²=46.24>6.8; e) 1.02²=1.0404>1.02; f) 0.05²=0.0025<0.05; g) 0.23²=0.0529<0.23; h) 0.98²=0.9604<0.98; i) 0.55²=0.3025<0.55; j) 0.10²=0.01<0.10; k) 0.89²=0.7921<0.89; l) 3.24²=10.4976>3.24. The printed instruction says each square is smaller, but that claim is false for numbers greater than 1; the comparisons above give the correct results."),
    ])
    replace_exercise(3, "Exercise 3.2", [
        (1, "Find each square root by factorisation: a) 64; b) 121; c) 169; d) 625; e) 324; f) 225; g) 49; h) 900.",
         "Pair equal prime factors and take one from each pair: a) √64=8; b) √121=11; c) √169=13; d) √625=25; e) √324=18; f) √225=15; g) √49=7; h) √900=30."),
        (2, "Find the square root by factorisation: a) 256/361; b) 3 1/16; c) 5 125/100; d) 100/841; e) 400/361; f) 625/144; g) 16/484; h) 36/961.",
         "Take the square root of numerator and denominator separately; convert mixed numbers to improper fractions first.\na) √(256/361)=16/19.\nb) 3 1/16 = 49/16, so √(49/16)=7/4.\nc) 5 125/100 = 625/100, so √(625/100)=25/10=5/2.\nd) √(100/841)=10/29.\ne) √(400/361)=20/19.\nf) √(625/144)=25/12.\ng) √(16/484)=4/22=2/11.\nh) √(36/961)=6/31."),
        (3, "Find each square root: a) 0.49; b) 0.25; c) 1.69; d) 56.25; e) 7.84; f) 11.56; g) 5.29; h) 2.25.",
         "a) 0.7; b) 0.5; c) 1.3; d) 7.5; e) 2.8; f) 3.4; g) 2.3; h) 1.5. For example, 1.69=169/100, so √1.69=13/10=1.3."),
    ])
    replace_exercise(3, "Exercise 3.3", [
        (1, "Find each natural-number square root by the division method: a) 729; b) 400; c) 576; d) 841; e) 225; f) 36; g) 144; h) 625.",
         "a) 27; b) 20; c) 24; d) 29; e) 15; f) 6; g) 12; h) 25. Example: pairing digits in 729 gives √729=27."),
        (2, "Find each fraction square root by the division method: a) 25/625; b) 784/81; c) 169/256; d) 289/324; e) 9/49; f) 676/576; g) 121/49; h) 64/900.",
         "Take the square root of numerator and denominator, then simplify: a) 1/5; b) 28/9; c) 13/16; d) 17/18; e) 3/7; f) 26/24=13/12; g) 11/7; h) 8/30=4/15."),
        (3, "Find each decimal square root by the division method: a) 62.41; b) 79.21; c) 86.49; d) 92.16; e) 2.89; f) 1.69; g) 1.21; h) 7.84.",
         "a) 7.9; b) 8.9; c) 9.3; d) 9.6; e) 1.7; f) 1.3; g) 1.1; h) 2.8. Example: √62.41=√(6241/100)=79/10=7.9."),
    ])
    replace_exercise(3, "Exercise 3.4", [
        (1, "There are 784 chairs in a hall, with the same number of chairs in each row as the total number of rows. Find the number of rows.",
         "If there are n rows, there are n chairs in each row, so n²=784. Thus n=√784=28 rows."),
        (2, "A triangle has base 32 cm and altitude 18 cm. If a square has twice the triangle's area, find the square's side length.",
         "Triangle area=½×32×18=288 cm². Square area=2×288=576 cm². Side=√576=24 cm. The printed answer key appears to show 24√2; that does not match the stated dimensions and area formula."),
        (3, "A 28 cm by 7 cm rectangular sheet has the same area as a square paper. Find the square's side length.",
         "Rectangle area=28×7=196 cm². The square side is √196=14 cm."),
        (4, "A square field has side length 45 m. Find the cost of levelling it at Rs 455 per square metre.",
         "Area=45²=2,025 m². Cost=2,025×455=Rs 921,375."),
        (5, "Find the side length of a square-shaped Masjid with area 900 m².",
         "Side=√900=30 m."),
        (6, "A square-shaped parking area has area 225 m². Find the cost of constructing a tiled path around it at Rs 435 per metre.",
         "Side=√225=15 m, so the perimeter is 4×15=60 m. At Rs 435 per metre, the cost is 60×435=Rs 26,100. The printed key gives Rs 97,875 (=225×435), which uses area rather than the stated perimeter and unit rate."),
        (7, "A square garden has area 169 m². Find (a) its perimeter and (b) fencing cost at Rs 670 per metre.",
         "Side=√169=13 m. (a) Perimeter=4×13=52 m. (b) Cost=52×670=Rs 34,840."),
    ])
    replace_exercise(3, "Review Exercise", [
        (1, "Choose the correct option: (a) square of an even number is what type of number? (b) square of what fraction is less than itself? (c) If y=x², x=...? (d) a number is what by itself to form its square? (e) a decimal less than what has a smaller square?",
         "a) even; b) proper; c) √y (taking the non-negative square root for the textbook's natural-number context); d) multiplied; e) 1."),
        (2, "Find the squares: a) 91; b) 107; c) 127; d) 156; e) 149; f) 16.",
         "a) 8,281; b) 11,449; c) 16,129; d) 24,336; e) 22,201; f) 256."),
        (3, "Test whether these are perfect squares: a) 121; b) 225; c) 325; d) 441.",
         "a) yes, 11²; b) yes, 15²; c) no (18²=324 and 19²=361); d) yes, 21²."),
        (4, "Tick the perfect squares of odd numbers: a) 289; b) 225; c) 64; d) 196.",
         "a) 289=17² and b) 225=15². The other two are squares of even numbers."),
        (5, "Find the square of each proper fraction: a) 5/9; b) 16/25; c) 9/17; d) 53/57.",
         "a) 25/81; b) 256/625; c) 81/289; d) 2,809/3,249."),
        (6, "Find the square roots by factorisation and division: a) 100; b) 841; c) 900; d) 256.",
         "a) 10; b) 29; c) 30; d) 16."),
        (7, "Find the square roots by factorisation: a) 1.69; b) 3.24; c) 2.25; d) 0.09.",
         "a) 1.3; b) 1.8; c) 1.5; d) 0.3."),
        (8, "Find the square roots by the division method: a) 0.16; b) 0.81; c) 1.96; d) 7.84.",
         "a) 0.4; b) 0.9; c) 1.4; d) 2.8."),
        (9, "A square garden has area 961 m². Find the cost of fencing it at Rs 205 per metre.",
         "Side=√961=31 m; perimeter=4×31=124 m. Cost=124×205=Rs 25,420."),
        (10, "A square garden has area 484 m². Find the wire length needed to cover all its sides.",
         "Side=√484=22 m; wire length=perimeter=4×22=88 m."),
        (11, "A square has the same area as a 6 cm by 24 cm rectangle. Find the square's side.",
         "Rectangle area=6×24=144 cm², so the square side is √144=12 cm."),
        (12, "Arrange 196 students in equal rows, with the number of rows equal to the number of students in each row.",
         "√196=14, so arrange 14 rows of 14 students."),
        (13, "A parallelogram has base 16 cm and altitude 9 cm. A square has the same area. Find the square's side.",
         "Parallelogram area=16×9=144 cm². Square side=√144=12 cm."),
        (14, "Math project: use flashcards with three-digit natural numbers, decimals and fractions; find square roots and match them to answer cards.",
         "Sample matching cards: 144 ↔ 12; 2.25 ↔ 1.5; 25/36 ↔ 5/6. Verify by squaring each answer: 12²=144, 1.5²=2.25, and (5/6)²=25/36. Groups can make more exact-square cards and exchange them to check their work."),
    ])
    # Replace OCR-damaged Unit 3 explanations with readable, scan-aligned text.
    unit3 = next(chapter for chapter in chapters if chapter["number"] == 3)
    section_rewrites = {
        "3.1.2": ("3.1.2 Square of a Number", [
            "A number multiplied by itself is its square. For example, 5 × 5 = 25, written 5² and read ‘five squared’. In general, a × a = a². Squares of integers are non-negative: for example, (−4)² = (−4)(−4) = 16. A perfect square is the square of a whole number, such as 144 = 12²."
        ]),
        "3.2": ("3.2 Square Roots", [
            "Square root reverses squaring. If a² = b for a non-negative number a, then √b = a. The symbol √ is the radical sign and b is the radicand. For example, 1²=1, 2²=4 and 3²=9, so √1=1, √4=2 and √9=3. A square array with n rows and n columns contains n² small squares; n is the square root of n². The two methods in this unit are prime factorisation and the division method."
        ]),
        "3.2.1": ("3.2.1 Square Root by Factorisation Method", [
            "To find a square root by prime factorisation: (1) factor the number into primes; (2) group equal primes into pairs; (3) take one factor from every pair and multiply. For example, 144 = 2 × 2 × 2 × 2 × 3 × 3 = 2² × 2² × 3², so √144 = 2 × 2 × 3 = 12. For a fraction, factor numerator and denominator separately; √(16/25)=4/5. Convert a mixed number to an improper fraction first."
        ]),
    }
    for section in unit3["sections"]:
        if section["id"] in section_rewrites:
            heading, paras = section_rewrites[section["id"]]
            body = "\n\n".join(paras)
            section.update({"title": heading, "heading": heading, "theory": f"{heading}\n\n{body}", "text": f"{heading}\n\n{body}", "paras": [heading, *paras]})
    for example in unit3["workedExamples"]:
        if "988" in example.get("problem", ""):
            example.update({
                "title": "Example: Is 988 a perfect square?",
                "problem": "Test 988 by prime factorisation.",
                "solution": "988 = 2 × 494 = 2² × 247 = 2² × 13 × 19. The prime exponents 1 for 13 and 19 are odd, so the factors cannot all be paired. Therefore 988 is not a perfect square. The scanned text prints an incorrect factorisation (2×2×2×11×11=968), so this solution uses the correct factorisation of 988."
            })
    # Unit 4 exercise cards checked against the scanned pages (printed pages
    # 60–75). The final two review answers below intentionally follow the
    # quantities in the questions where the printed back-of-book key conflicts.
    replace_exercise(4, "Exercise 4.1", [
        (1, "Seven litres of milk cost Rs 770. Find the unit rate per litre.", "Rs 770 ÷ 7 L = Rs 110 per litre."),
        (2, "A factory worker works 78 hours over 5 days. Find the average working time per day.", "78 ÷ 5 = 15.6 hours per day = 15 hours 36 minutes per day."),
        (3, "Ahad completes 6 jogging-track rounds in 2 hours. Find his average rate.", "6 ÷ 2 = 3 rounds per hour."),
        (4, "A person types 480 words in half an hour. How long will it take to type (a) 765 words; (b) 1,250 words; (c) 6,230 words?", "Typing rate=480÷30=16 words/min. a) 765÷16=47.8125 min (about 47 min 49 sec); b) 1,250÷16=78.125 min; c) 6,230÷16=389.375 min. The printed answer key's first value appears inconsistent with the stated rate; these follow directly from the scanned question."),
        (5, "Raza's heart beats 228 times in 3 minutes. Find the average heart-beat rate.", "228 ÷ 3 = 76 beats per minute."),
        (6, "Maha skips rope 108 times in 4 minutes. Find her average rate per minute.", "108 ÷ 4 = 27 skips per minute."),
        (7, "Madiha writes 66 pages in 3 days. Find her average writing rate per day.", "66 ÷ 3 = 22 pages per day."),
    ])
    replace_exercise(4, "Exercise 4.2", [
        (1, "Simplify each ratio: (a) 444 to 234; (b) 16 h to 22 h; (c) 565 m to 50 m to 229 m; (d) 12 g to 88 g to 56 g; (e) 100 m to 60 m to 88 m.", "Divide all terms by their common factor: a) 74:39; b) 8:11; c) 565:50:229; d) 3:22:14; e) 25:15:22."),
        (2, "Divide Rs 340 between Sara and Sonia in the ratio 3:7.", "Total parts=3+7=10; one part=340÷10=Rs 34. Sara=3×34=Rs 102; Sonia=7×34=Rs 238."),
        (3, "Divide Rs 342,000 among A, B and C in the ratio 2:3:4.", "Total parts=9; one part=342,000÷9=Rs 38,000. A=Rs 76,000; B=Rs 114,000; C=Rs 152,000."),
        (4, "Rashid earns Rs 32,000 per month and spends Rs 24,000. Find (a) his savings and (b) the ratio of expenditure to savings.", "a) Savings=32,000−24,000=Rs 8,000. b) 24,000:8,000=3:1."),
        (5, "Saleem's salary rises from Rs 30,000 to Rs 42,000. Find (a) old salary:new salary and (b) increase:new salary.", "Increase=42,000−30,000=Rs 12,000. a) 30,000:42,000=5:7. b) 12,000:42,000=2:7."),
    ])
    replace_exercise(4, "Exercise 4.3", [
        (1, "Change each quantity in the stated ratio. State whether it increases or decreases: (a) 48 m in 5:8; (b) 126 h in 7:3; (c) 8,900 in 9:10; (d) 666 in 5:3; (e) 428 in 3:4; (f) 35 in 2:5; (g) 708 in 7:6.", "Use new quantity=old quantity×(first ratio term ÷ second term). a) 48×5/8=30 m, decrease; b) 126×7/3=294 h, increase; c) 8,900×9/10=8,010, decrease; d) 666×5/3=1,110, increase; e) 428×3/4=321, decrease; f) 35×2/5=14, decrease; g) 708×7/6=826, increase."),
        (2, "A school increases its teachers from 28 to 40. Find new teachers:previous teachers.", "40:28=10:7."),
        (3, "A chopper's price falls from Rs 11,250 to Rs 8,750 after discount. Find discounted price:original price.", "8,750:11,250; divide both terms by 1,250 to get 7:9."),
        (4, "Change 63 in the ratio 5:3. Will the new quantity be greater or smaller?", "5/3>1, so it increases. New quantity=63×5/3=105."),
        (5, "Change 522 in the ratio 5:6. Will the new quantity be greater or smaller?", "5/6<1, so it decreases. New quantity=522×5/6=435."),
        (6, "A baker makes 360 cupcakes daily. If the amount increases in the ratio 7:6, how many cupcakes will be made daily?", "360×7/6=420 cupcakes."),
        (7, "A factory has 456 workers and decreases the number in the ratio 7:8. How many workers remain?", "New:old=7:8, so 456×7/8=399 workers."),
    ])
    replace_exercise(4, "Exercise 4.4", [
        (1, "Find x: (a) x/21=4/7; (b) 1/x=2/3; (c) 5/15=x/30; (d) x:24=8:6; (e) 15:x=100:200.", "Cross-multiply: a) 7x=84, x=12; b) 2x=3, x=3/2; c) 5×30=15x, x=10; d) x/24=8/6, x=32; e) 15/x=100/200=1/2, x=30."),
        (2, "Find the fourth proportional to 3, 9 and 7.", "Let x be the fourth term: 3:9=7:x. Then 3x=63, so x=21."),
        (3, "Beenish reads 25 pages in 40 minutes. How many pages will she read in 60 minutes at the same rate?", "Direct proportion: 25×60/40=37.5 pages."),
        (4, "Seven bats cost Rs 5,500. Find the cost of 3 bats at the same rate.", "One bat costs 5,500÷7. Three cost 5,500×3/7=Rs 2,357.14 (to 2 d.p.). The printed key appears to give Rs 2,457.14, which does not follow from the stated values."),
        (5, "Five litres of cooking oil cost Rs 755. Find the cost of 9 litres.", "Unit price=755÷5=Rs 151/L. Cost=151×9=Rs 1,359."),
        (6, "Eight men make 18 chairs in 9 days. How many men are needed to make 27 chairs in the same number of days?", "Direct proportion to chairs: 8×27/18=12 men."),
        (7, "A motorbike uses 2 L to travel 100 km. How much fuel is needed for 50 km?", "2×50/100=1 L."),
        (8, "Food in a camp of 36 people lasts 20 days. If 12 more people arrive, how many days will it last?", "People×days is constant: 36×20=48×d, so d=720÷48=15 days."),
        (9, "Fourteen men can paint a Masjid in 12 hours. How long will 10 men take at the same rate?", "Work is fixed, so men×hours is constant: 14×12=10×h. Thus h=168÷10=16.8 hours. The printed answer key appears to give 8.57 hours; that conflicts with inverse proportion and the scanned question."),
        (10, "Think Higher.\na) What should be added to both 17 and 12 so their ratio is 4:3?\nb) In what ratio must 21 be decreased to get 14?\nc) A 55 cm × 30 cm mirror is enlarged in the ratio 6:5. Find the new dimensions.",
         "a) Let x be added: (17+x)/(12+x)=4/3. Cross-multiply: 51+3x=48+4x, so x=3; the new ratio is 20:15=4:3.\nb) New:old=14:21=2:3.\nc) Scale factor=6/5. New dimensions: 55×6/5=66 cm and 30×6/5=36 cm."),
    ])
    replace_exercise(4, "Review Exercise", [
        (1, "Choose the correct answers: (a) comparison of quantities; (b) what equality of two ratios is called; (c) ratio of 20 boys to 15 girls; (d) what happens to the second quantity when both are directly proportional and the first decreases; (e) a ratio equivalent to 12:4; (f) relation between vehicle speed and travel time for fixed distance; (g) relation between a square's length and width; (h) 76 changed in ratio 5:2.", "a) ratio; b) proportion; c) 20:15=4:3; d) it decreases; e) 12:4=6:2; f) inversely proportional; g) directly proportional (equal); h) 76×5/2=190."),
        (2, "Define and give an example of (a) rate; (b) ratio; (c) average rate; (d) proportion and its types.", "a) Rate compares quantities with different units, e.g. 60 km/h. b) Ratio compares like quantities, e.g. 2:3. c) Average rate=total amount÷total time, e.g. 66 pages÷3 days=22 pages/day. d) A proportion states two ratios are equal; direct proportion changes in the same direction, inverse proportion in opposite directions."),
        (3, "A park has 35 benches. The number is decreased in the ratio 4:5. How many benches remain?", "New:old=4:5, so 35×4/5=28 benches."),
        (4, "Israr donated Rs 8,100 in 2021. He increases the donation in the ratio 11:9 for 2022. Find the new donation.", "New amount=8,100×11/9=Rs 9,900."),
        (5, "A tailor stitches 18 scarves in 3 hours. Find the average rate per hour.", "18÷3=6 scarves per hour."),
        (6, "Find x: (a) 1:10=x:5; (b) 8:4=20:x; (c) x:32=4:8; (d) 50:x=200:100.", "a) x/5=1/10, x=1/2; b) 8x=80, x=10; c) x/32=1/2, x=16; d) 50/x=2, x=25."),
        (7, "Ali and Anas share money in the ratio 5:6. Anas receives Rs 170. Find Ali's share and the total.", "Six parts=Rs 170, so one part=170/6. Ali gets 5×170/6=Rs 141.67 (to 2 d.p.); total=11×170/6=Rs 311.67 (to 2 d.p.)."),
        (8, "Ten workers complete a job in 7 days. How many workers are needed to finish it in 14 days?", "Inverse proportion: 10×7=w×14, so w=5 workers."),
        (9, "Food in a camp of 150 men lasts 40 days. How long will it last if the camp has 120 men?", "Men×days=constant: 150×40=120×d, so d=6,000/120=50 days. The printed answer key appears to say 32 days, which conflicts with the stated figures."),
        (10, "Math project: collect real-life examples of constant and average rates, ratio changes, and direct and inverse proportion; present and explain the data.", "Sample set: constant rate—tap fills 12 L in 3 min, 4 L/min; average rate—travel 90 km in 2 h, 45 km/h; change in ratio—an 80 cm ribbon changed in new:old ratio 3:4 becomes 60 cm; direct proportion—3 notebooks cost Rs 150, so 7 cost Rs 350; inverse proportion—4 workers take 12 days, so 8 workers take 6 days for the same work. State units and show the calculation for each example."),
    ])
    # Unit 5's table and application questions were badly split across OCR
    # columns. These groups follow the photographed exercise pages 80–88.
    replace_exercise(5, "Exercise 5.1", [
        (1, "Complete the cost/selling price/profit/loss table. (a) CP Rs 1,800, SP Rs 1,500; (b) CP Rs 2,450, SP Rs 2,200; (c) CP Rs 4,000, profit Rs 1,260; (d) CP Rs 6,425, loss Rs 200; (e) CP Rs 9,000, loss Rs 2,000. Find the missing price, amount, and percentage in each row.",
         "Profit=SP−CP; loss=CP−SP; percentage=amount÷CP×100. a) loss Rs 300; 16.67%. b) loss Rs 250; 10.20%. c) SP=4,000+1,260=Rs 5,260; profit%=1,260/4,000×100=31.5%. d) SP=6,425−200=Rs 6,225; loss%=200/6,425×100≈3.11%. e) SP=9,000−2,000=Rs 7,000; loss%=2,000/9,000×100≈22.22%."),
        (2, "A watch is bought for Rs 250 and sold for Rs 300. Find the profit and profit percentage.", "Profit=300−250=Rs 50. Profit%=50/250×100=20%."),
        (3, "Amna buys a doll for Rs 475 and sells it for Rs 425. Find her loss and loss percentage.", "Loss=475−425=Rs 50. Loss%=50/475×100≈10.53%."),
        (4, "Usman buys a bike for Rs 50,000 and sells it for Rs 40,000. Find his profit or loss and percentage.", "Loss=50,000−40,000=Rs 10,000. Loss%=10,000/50,000×100=20%."),
        (5, "Najma buys a house for Rs 750,000 and sells it for Rs 800,000. Find her profit or loss percentage.", "Profit=800,000−750,000=Rs 50,000. Profit%=50,000/750,000×100≈6.67%."),
        (6, "A chair's marked price is Rs 800 and its selling price is Rs 600. Find the discount percentage.", "Discount=800−600=Rs 200. Discount%=200/800×100=25%."),
        (7, "A shirt marked Rs 450 is sold for Rs 375. Find the discount and discount percentage.", "Discount=450−375=Rs 75. Discount%=75/450×100≈16.67%."),
    ])
    replace_exercise(5, "Exercise 5.2", [
        (1, "Calculate property tax at 8% on: (a) Rs 175,500; (b) Rs 3,467,890; (c) Rs 12,345,678; (d) Rs 34,567,800.", "Tax=0.08×amount. a) Rs 14,040; b) Rs 277,431.20; c) Rs 987,654.24; d) Rs 2,765,424. The scanned key appears to misprint part (b); multiplying the stated amount by 8% gives Rs 277,431.20."),
        (2, "Find the total price after 17% general sales tax on: (a) car Rs 1,856,000; (b) motorbike Rs 125,000; (c) bus Rs 7,500,000.", "Total=price×1.17. a) Rs 2,171,520; b) Rs 146,250; c) Rs 8,775,000."),
        (3, "Find property tax on a property worth Rs 650,000 at 1.5%.", "650,000×0.015=Rs 9,750."),
        (4, "A factory owner pays Rs 40,500 property tax at 9%. Find the property's worth.", "Property value=40,500÷0.09=Rs 450,000."),
        (5, "A house is worth Rs 8,000,000. Find property tax at 6%.", "8,000,000×0.06=Rs 480,000."),
        (6, "Find property tax on a plot worth Rs 6,700,400 at 2.5%.", "6,700,400×0.025=Rs 167,510."),
        (7, "Madeeha pays Rs 7,800 property tax at 3%. Find her house's worth.", "7,800÷0.03=Rs 260,000."),
        (8, "A buyer paid Rs 350 GST at a rate of 17%. Find the item's pre-tax cost.", "Cost=350÷0.17≈Rs 2,058.82."),
        (9, "Raza buys an item for Rs 1,590 with GST at 10%. Find the total cost.", "GST=1,590×0.10=Rs 159. Total=1,590+159=Rs 1,749."),
        (10, "Ali buys a motorcycle for Rs 52,900 and pays 5% tax. He sells it for Rs 53,500 and charges 7% tax. Find the value-added tax payable (output tax minus input tax).", "Input tax=52,900×5%=Rs 2,645. Output tax=53,500×7%=Rs 3,745. VAT payable=3,745−2,645=Rs 1,100."),
        (11, "A shopkeeper buys rice for Rs 6,890 and pays 4% tax, then sells it for Rs 7,900 and charges 6% tax. Find the VAT payable.", "Input tax=6,890×4%=Rs 275.60. Output tax=7,900×6%=Rs 474. VAT payable=474−275.60=Rs 198.40."),
        (12, "Umar earns 2.2% commission on an item sale of Rs 78,600. Find his commission.", "78,600×0.022=Rs 1,729.20."),
        (13, "Kamal earns 3.2% commission on six laptops whose total sale price is Rs 471,000. Find his commission.", "471,000×0.032=Rs 15,072."),
    ])
    replace_exercise(5, "Exercise 5.3", [
        (1, "Asma saves Rs 78,480 in a year. Find her Zakat at 2.5%.", "78,480×0.025=Rs 1,962."),
        (2, "Hassan pays Rs 7,750 Zakat. Find the yearly savings it was calculated on at 2.5%.", "7,750÷0.025=Rs 310,000."),
        (3, "Mr Akram pays Rs 20,000 Zakat. Find his annual savings at 2.5%.", "20,000÷0.025=Rs 800,000."),
        (4, "Mr Salman earns Rs 224,000 from a rice crop and pays Ushr at 5%. Find the Ushr.", "224,000×0.05=Rs 11,200."),
        (5, "Haris sells mangoes for Rs 66,000 and pays Ushr at 10%. Find the Ushr.", "66,000×0.10=Rs 6,600."),
        (6, "Madeeha's annual savings are Rs 180,000. Find Zakat at 2.5%.", "180,000×0.025=Rs 4,500."),
        (7, "A farmer pays Rs 17,670 Ushr at 10%. Find the crop value.", "17,670÷0.10=Rs 176,700."),
        (8, "Find Ushr at 5% on a farmer's earnings of Rs 346,000.", "346,000×0.05=Rs 17,300."),
    ])
    replace_exercise(5, "Review Exercise", [
        (1, "Choose the correct option: (a) percentage loss when 12 eggs cost Rs 72, two are rotten, and the remaining eggs sell for Rs 60; (b) marked price of a Rs 30 notebook after a Rs 5 discount; (c) tax based on annual property value; (d) fixed Zakat rate; (e) meaning of GST; (f) tax paid by Muslim farmers on produce; (g) tax based on yearly income; (h) 5% commission on a Rs 5,000 sale.", "a) loss%=12/72×100=16.67% (iii); b) Rs 35 (iii); c) property tax (i); d) 2.5% (iii); e) General Sales Tax (iii); f) Ushr (iv); g) income tax (ii); h) Rs 250 (iii)."),
        (2, "Find profit or loss and its percentage: (a) CP Rs 67,300, SP Rs 65,200; (b) CP Rs 8,500, SP Rs 8,650.", "a) Loss=2,100; loss%=2,100/67,300×100≈3.12%. b) Profit=150; profit%=150/8,500×100≈1.76%."),
        (3, "Marked price is Rs 7,845 and selling price is Rs 7,690. Find the discount and discount percentage.", "Discount=7,845−7,690=Rs 155; percentage=155/7,845×100≈1.98%."),
        (4, "An item has a discount of Rs 900 and sells for Rs 6,500. Find the marked price.", "Marked price=6,500+900=Rs 7,400."),
        (5, "A shopkeeper sells an oven for Rs 39,900 at a 25% profit. Find its cost price.", "Selling price=125% of cost, so CP=39,900÷1.25=Rs 31,920."),
        (6, "Sadia saves Rs 89,000 in a year. Find Zakat at 2.5%.", "89,000×0.025=Rs 2,225."),
        (7, "Umar buys a used car for Rs 450,000, spends Rs 58,000 on repairs, and sells it for Rs 440,000. Find profit or loss percentage.", "Total cost=450,000+58,000=Rs 508,000. Loss=508,000−440,000=Rs 68,000. Loss%=68,000/508,000×100≈13.39%."),
        (8, "A shopkeeper buys a cupboard for Rs 18,900 and pays 4% tax, then sells it for Rs 21,400 and charges 6% tax. Find VAT payable.", "Input tax=18,900×4%=Rs 756. Output tax=21,400×6%=Rs 1,284. VAT payable=1,284−756=Rs 528."),
        (9, "Saad's yearly income is Rs 236,000. Find the income tax using the textbook key's implied 5% rate.", "236,000×0.05=Rs 11,800. The exercise itself does not state a rate, so this result depends on the 5% rate implied by the answer key."),
        (10, "A shop sells for Rs 2,555,750 through an agent who earns 1.7% commission. Find the commission.", "2,555,750×0.017=Rs 43,447.75."),
        (11, "Math project: create at least five everyday cost-price/selling-price situations. Classify each as profit or loss, solve them, and present the result cards.", "Sample cards: (1) CP Rs 500, SP Rs 575 → profit Rs 75, 15%. (2) CP Rs 1,200, SP Rs 1,080 → loss Rs 120, 10%. (3) CP Rs 800, SP Rs 920 → profit Rs 120, 15%. (4) CP Rs 2,500, SP Rs 2,000 → loss Rs 500, 20%. (5) CP Rs 4,000, SP Rs 4,600 → profit Rs 600, 15%. The percentage in each case is profit or loss divided by CP × 100."),
    ])
    # Unit 6 set notation, operations, Venn relations, and review questions
    # checked against the scans on printed pages 95–102.
    replace_exercise(6, "Exercise 6.1", [
        (1, "Write each set in descriptive form: (a) {January, June, July}; (b) {a,b,c,d,e}; (c) {−1,−2,−3,−4}; (d) {Thursday, Saturday}; (e) {2,4,6,8}; (f) {14,16,18,...}; (g) {1,3,5,7,9,...}; (h) {10,12,14,16,20}; (i) {2,4,6,8,...}; (j) {101,103,105,107,109}; (k) {0,1,2,3,...}; (l) {1,4,9,16,25}; (m) {1,3,5,7,9}; (n) {22,33,44,55,...}.", "a) months beginning with J; b) first five letters of the English alphabet; c) first four negative integers; d) Thursday and Saturday (this finite set has no unique simpler rule); e) first four positive even numbers; f) even numbers beginning at 14; g) positive odd numbers; h) {10,12,14,16,20} (the listed set); i) positive even numbers; j) odd numbers from 101 through 109; k) whole numbers; l) first five square numbers; m) first five positive odd numbers; n) positive multiples of 11 beginning at 22."),
        (2, "Write in tabular form: (a) odd numbers between 30 and 60; (b) natural numbers less than 40; (c) multiples of 12 less than 60; (d) common factors of 18, 30 and 42; (e) numbers divisible by both 3 and 4; (f) factors of 81 between 5 and 30.", "a) {31,33,35,37,39,41,43,45,47,49,51,53,55,57,59}; b) {1,2,...,39}; c) {12,24,36,48}; d) {1,2,3,6}; e) {12,24,36,48,...}; f) {9,27}."),
        (3, "Decide which pairs of sets are equal: (a) {a,c,t} and {c,a,t}; (b) {22,24,26,28} and {24,26,22,28}; (c) {1,3,5,7} and {1,3,5,7,9,11}; (d) ∅ and { }; (e) {∅} and ∅; (f) {eraser,pen,marker} and {sharpener,scale}; (g) {A} and {A}; (h) odd numbers between 4 and 10 and {5,7,9}; (i) {73,79,83,87} and primes between 72 and 88.", "Equal: a, b, d, g, h. Not equal: c, e, f, i. Order does not matter in a set; however, {∅} has one element while ∅ has none, and 87 is not prime."),
        (4, "Decide which pairs are equivalent (have the same number of elements): (a) two sets each with four listed elements; (b) a three-element set and a four-element set; (c) {∅} and ∅; (d) a four-element set and a three-element set; (e) ∅ and ∅; (f) five rivers and the odd multiples of 7 between 5 and 65; (g) all multiples of 8 and all even numbers.", "Equivalent: a, e, f, g. Not equivalent: b, c, d. For f the multiples are {7,21,35,49,63}, five elements. For g both sets are countably infinite and can be paired one-to-one."),
        (5, "Let A={1,2,3}, B={2,3,4}, Y={3,4,5}, D={1,2,3,4}. Which statements are true? (a) A⊆B; (b) B⊄D; (c) D⊇Y; (d) A⊆D; (e) B⊄A; (f) Y⊆A.", "Only d and e are true. A is contained in D; B contains 4, so it is not contained in A. The other stated inclusions fail by checking their elements."),
        (6, "For U={a,b,...,z}, S={a,b,c,d,e}, T={f,g,h,i}, V={a,b,e}, find S′, T′, V′ and U′.", "S′={f,g,h,...,z}; T′={a,b,c,d,e,j,k,...,z}; V′={c,d,f,g,h,...,z}; U′=∅. Complements are taken relative to U."),
        (7, "For U={0,1,2,...,20}, A={0,2,4,...,18}, and B={3,6,9,12,15}, check the printed claims: (a) B′=A; (b) A′=B; (c) A\\B=A; (d) B\\A=B.", "All four printed claims are false for these sets. (a) 1∈B′ but 1∉A. (b) 1∈A′ but 1∉B. (c) A\\B={0,2,4,8,10,14,16,18}, because 6 and 12 are shared. (d) B\\A={3,9,15}, because 6 and 12 are shared. The exercise's statements conflict with its given sets."),
        (8, "For each pair, say whether the sets are disjoint or overlapping: (a) {1,2,3,4,5} and {2,4,6}; (b) positive integers and {−1,−2,−3,−4}; (c) first five multiples of 2 and factors of 9; (d) whole numbers and natural numbers that are neither prime nor composite; (e) natural numbers less than 5 and natural numbers at least 5.", "Overlapping: a (common elements 2,4) and d (the second set contains 1). Disjoint: b, c and e."),
    ])
    replace_exercise(6, "Exercise 6.2", [
        (1, "Write in tabular form: (a) natural numbers N; (b) whole numbers W; (c) integers Z; (d) even numbers E; (e) odd integers O; (f) prime numbers P; (g) composite numbers K.", "a) N={1,2,3,...}; b) W={0,1,2,3,...}; c) Z={0,±1,±2,±3,...}; d) E={2,4,6,...}; e) O={±1,±3,±5,...}; f) P={2,3,5,7,11,...}; g) K={4,6,8,9,10,12,...}."),
        (2, "Draw Venn diagrams for these relationships: (a) N and Z; (b) E and W; (c) P and W; (d) Q and N; (e) W and N.", "In each diagram, draw the first named subset inside the second: (a) N⊂Z; (b) E⊂W; (c) P⊂W; (d) N⊂Q; (e) N⊂W. Use nested circles and label each circle; every natural number is whole, integer and rational, and every prime is whole."),
    ])
    replace_exercise(6, "Exercise 6.3", [
        (1, "Find the unions: (a) A={2,4,6}, B={1,3,5,7}; (b) U={a,b,c,d,e}, V={c,d,e}; (c) K={2,4,6,8,10}, D={1,5,10}; (d) Z=integers, X={−1,−2,−3}, Y={1,2,3,4,5,6,7,8}; (e) E={2,4,6,8,...}, F={4,8,12,16}, N={1,2,3,4,...}.", "a) A∪B={1,2,3,4,5,6,7}; b) U∪V={a,b,c,d,e}; c) K∪D={1,2,4,5,6,8,10}; d) Z∪X∪Y=Z; e) E∪F∪N=N, since E and F are subsets of N."),
        (2, "Find the intersections: (a) {0,1,2,3}∩{−3,−2,−1,0}; (b) {1,2,...,10}∩{1,3,5,7,9}; (c) {2,6,10,14,16}∩{4,8,12,16}; (d) {3,5,7,9}∩{1,2,3}∩W; (e) {a,f,g}∩{g,h,p,r,s,m}∩{l,m,n,o}.", "a) {0}; b) {1,3,5,7,9}; c) {16}; d) {3}; e) ∅, because no element is common to all three sets."),
        (3, "If E is the set of positive even numbers and W is the set of whole numbers, find E∪W and E∩W.", "E⊂W, so E∪W=W={0,1,2,...} and E∩W=E={2,4,6,...}."),
        (4, "If P is the set of prime numbers and Z is the set of integers, find P∪Z and P∩Z.", "P⊂Z, so P∪Z=Z and P∩Z=P."),
        (5, "Let S={2,3,4}, U={0,2,4}, V={3,7,9}. Find (a) S−U; (b) S−V; (c) U−V; (d) U−S; (e) V−S; (f) V−U.", "a) {3}; b) {2,4}; c) {0,2,4}; d) {0}; e) {7,9}; f) {3,7,9}. Remove from the first set every element that occurs in the second."),
        (6, "Let A={3,5,7,9}, B={2,3,4,5}, K={1,5,10,15}. Find (a) A∪B∪K and (b) A∩B∩K.", "a) {1,2,3,4,5,7,9,10,15}; b) {5}."),
        (7, "Let X={1,2,...,20}, Y={2,4,6,8,10,...}, W={0,1,2,3,...}. Find (a) X∪Y∪W and (b) X∩Y∩W.", "a) W={0,1,2,...}, because X and Y are subsets of W; b) {2,4,6,8,10,12,14,16,18,20}."),
        (8, "If L={1,3,4,5,6,7,8} and M=∅, find (a) L∪M and (b) L∩M.", "a) L∪∅=L={1,3,4,5,6,7,8}; b) L∩∅=∅."),
        (9, "For U={1,2,...,20}, B={1,3,5,7,9,11}, D={2,4,6,8,10}, verify: (a) B′∪B=U; (b) D∩D′=∅; (c) U′=∅; (d) ∅′=U; (e) U′∪B=B; (f) (B∪D)′=B′∩D′; (g) B∪∅=B; (h) (B∩D)′=B′∪D′.", "a) A set and its complement partition U, so B′∪B=U. b) A set and its complement are disjoint. c) U has no elements outside U, so U′=∅. d) Every element of U is outside ∅, so ∅′=U. e) ∅∪B=B. f) De Morgan's law gives (B∪D)′=B′∩D′. g) B∪∅=B. h) De Morgan's law gives (B∩D)′=B′∪D′."),
    ])
    replace_exercise(6, "Review Exercise", [
        (1, "Choose the correct option: (a) the form that describes common characteristics of set elements; (b) the symbol for union; (c) the set of elements common to two sets; (d) A∪∅; (e) two sets with no common elements; (f) the set of all objects under consideration.", "a) descriptive form (ii); b) ∪ (ii); c) intersection (i); d) A (iv); e) disjoint sets (ii); f) universal set (i)."),
        (2, "Write in tabular form: (a) five 2D shapes with four sides; (b) prime numbers; (c) first five multiples of 3; (d) even factors of 45; (e) composite numbers less than 40; (f) odd numbers less than 18.", "a) {square, rectangle, trapezium, kite, rhombus}; b) {2,3,5,7,11,13,17,19,23,29,31,37,...}; c) {3,6,9,12,15}; d) ∅ (45 has no even factor); e) {4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39}; f) {1,3,5,7,9,11,13,15,17}."),
        (3, "Write each set in descriptive form: (a) {1,2,3,...}; (b) {1,2,3,4,5,6}; (c) {5,10,15,20,25,30}; (d) {3,5,7,11}; (e) {5,10,15,20}.", "a) natural numbers; b) natural numbers from 1 through 6; c) first six positive multiples of 5; d) prime numbers less than 12; e) first four positive multiples of 5."),
        (4, "If X={5,10,15,20,...} and Y={10,20,30,...}, find (a) X∪Y; (b) Y∪X; (c) X∩Y; (d) Y∩X.", "Y⊂X, so a) X; b) X; c) Y; d) Y."),
        (5, "Let U be whole numbers and N be natural numbers. Find (a) U′; (b) N′; (c) N∩N′; (d) N∪N′.", "Relative to U, a) U′=∅; b) N′={0}; c) N∩N′=∅; d) N∪N′=U."),
        (6, "Math project: use number cards 1–100 and make a Venn diagram for multiples of 3 and even numbers. Place each number in the correct region.", "Within 1–20, multiples of 3 are {3,6,9,12,15,18} and even numbers are {2,4,6,8,10,12,14,16,18,20}. The overlap is {6,12,18}; multiples of 3 only are {3,9,15}; even numbers only are {2,4,8,10,14,16,20}; numbers in neither set are {1,5,7,11,13,17,19}. In the larger 1–100 project, extend each set and keep the same placement rule."),
    ])
    # Unit 7 starts with sequences and algebraic terms. These cards retain the
    # printed subparts together and use the answer page to verify the results.
    replace_exercise(7, "Exercise 7.1", [
        (1, "Identify each term-to-term rule and write the next three terms: (a) 7,10,13,16,...; (b) 100000,10000,1000,...; (c) 78125,15625,3125,...; (d) 6,12,24,48,...; (e) 120,105,90,...", "a) Add 3: 19,22,25. b) Divide by 10: 100,10,1. c) Divide by 5: 625,125,25. d) Multiply by 2: 96,192,384. e) Subtract 15: 75,60,45."),
        (2, "For each sequence, find its position-to-term rule and calculate the 10th, 18th and 67th terms: (i) 21,22,23,24,...; (ii) 5,10,15,20,...; (iii) 30,45,60,75,...", "i) nth term n+20; 10th=30, 18th=38, 67th=87. ii) nth term 5n; 10th=50, 18th=90, 67th=335. iii) nth term 15(n+1); 10th=165, 18th=285, 67th=1,020."),
        (3, "If the nth term of a sequence is 2n+5, find its 12th term.", "Substitute n=12: 2(12)+5=24+5=29."),
        (4, "If the nth term of a sequence is 3n, find its 8th term.", "Substitute n=8: 3×8=24. The 8th term is 24."),
        (5, "If the nth term is 4n+2, find (a) the 9th term; (b) the 12th term; (c) the 26th term; (d) the 50th term.", "Substitute each position n into 4n+2. a) 4×9+2=38. b) 4×12+2=50. c) 4×26+2=106. d) 4×50+2=202."),
    ])
    replace_exercise(7, "Exercise 7.2", [
        (1, "Write the terms separately: (a) 6a+8b; (b) 3y−2x−5; (c) 5x−y+7; (d) 3x²+y²; (e) 7bc−d; (f) 13y²+y+3; (g) 5x³+3x²+7; (h) a²−b²+3; (i) uv+uvw+4w.", "a) 6a, 8b. b) 3y, −2x, −5. c) 5x, −y, 7. d) 3x², y². e) 7bc, −d. f) 13y², y, 3. g) 5x³, 3x², 7. h) a², −b², 3. i) uv, uvw, 4w."),
        (2, "For each expression, identify its variables, coefficients, exponents, and constant: (a) u²+v−5; (b) 3a³+b+8; (c) 4x+6y²−4; (d) (1/3)y⁴+y+1; (e) 8a³−7a+a².", "a) Variables u,v; coefficients 1,1; exponents 2,1; constant −5. b) a,b; 3,1; 3,1; constant 8. c) x,y; 4,6; 1,2; constant −4. d) y; 1/3,1; 4,1; constant 1. e) a; 8,−7,1; 3,1,2; no constant."),
    ])
    replace_exercise(7, "Exercise 7.3", [
        (1, "For each group, identify which listed terms are valid polynomial terms and give the reason: (a) 5xy, 6yz, zx; (b) 7x², 3y², −8; (c) p², q², −r²; (d) 5xyz, 2yz, −8xy⁻²; (e) −4ab, a, −5bc; (f) 7ab, 6ca, −8ac.", "All listed terms are polynomial terms except −8xy⁻² in (d). A polynomial variable exponent must be a non-negative whole number; −2 is negative. The other terms have whole-number exponents."),
        (2, "Which are polynomials? (a) 10−13x; (b) z+z²+z⁵−7; (c) 1+1/a+1/a²+1/a³+1/a⁴; (d) m³/n; (e) 1/2−5/u; (f) 1+5m; (g) 1+5u+4u²; (h) a²+b^(3/2)+c.", "Polynomials: a, b, f, g. Not polynomials: c, d, e, h. In c and e variables occur in denominators, in d the variable is in the denominator, and in h the exponent 3/2 is not a whole number."),
        (3, "Sort into monomials, binomials and trinomials: (a) 4ab; (b) 5a²+b²−7; (c) u²−v²; (d) 3xy+zx²; (e) −3xy−7yz; (f) 5ab−7ca+2; (g) mn; (h) mn+m; (i) 2a+b; (j) 7abc; (k) 7+u+v; (l) 2p²−p−k; (m) ax²+bx−7; (n) −3mn+t; (o) 1+a+z; (p) 1+a+z.", "Monomials (one term): a, g, j. Binomials (two terms): c, d, e, h, i, n. Trinomials (three terms): b, f, k, l, m, o, p. The scan repeats the same expression for o and p; each has three terms."),
        (4, "Find each polynomial's degree: (a) y+3+3y²; (b) 3a²+a−2; (c) l³+l²+l; (d) b⁴+b³−b²; (e) 5a; (f) 2x²−5x+1; (g) 3l³−4l²; (h) 10a⁴−5a³+a²+a.", "The degree is the largest exponent: a) 2; b) 2; c) 3; d) 4; e) 1; f) 2; g) 3; h) 4."),
    ])
    replace_exercise(7, "Exercise 7.4", [
        (1, "Add and simplify: (a) (x²+3x−6)+(−2x²+x−2); (b) (3x²−4+3x)+2y+(x+y)²; (c) (5x⁴−3x²+4)+(6x²−4x²−7); (d) (5x³−7x²+3x−4)+(8x³+2x²+3x−7); (e) (6x²−7x+4)+(7x²+9x+8); (f) (2x²y−5xy+3y²)+(7xy−6y²+5x²y); (g) (4x³−5x−8)+(6x²−3x+8); (h) (9x⁵−6x³+7x²)+(7x³−6x⁵+2x²); (i) (4x²−9x+3)+(5x²−4x+7).",
         "Collect like terms: a) −x²+4x−8. b) Expand (x+y)²=x²+2xy+y², giving 4x²+2xy+y²+3x+2y−4. c) 5x⁴−x²−3. d) 13x³−5x²+6x−11. e) 13x²+2x+12. f) 7x²y+2xy−3y². g) 4x³+6x²−8x. h) 3x⁵+x³+9x². i) 9x²−13x+10."),
        (2, "Subtract and simplify: (a) −3ab−7ab; (b) (−u²−v)−(9u²+4v); (c) (3x−5y²−5)−(−6x+2y²+3); (d) (x²−5x+9)−(−10x²+3x−2); (e) (6x+8y−z)−(5x−2y−z); (f) (7−2x²)−(8x²−8y); (g) (3x²−5x+7)−(5x²−2x−1); (h) (7a³+9a−1)−(2a³−5a+9).",
         "Change every sign in the second expression, then combine like terms: a) −10ab. b) −10u²−5v. c) 9x−7y²−8. d) 11x²−8x+11. e) x+10y. f) −10x²+8y+7. g) −2x²−3x+8. h) 5a³+14a−10."),
        (3, "How much is −8x less than 12x?", "12x−(−8x)=20x."),
        (4, "How much is 4v+z greater than 7v−2z?", "(4v+z)−(7v−2z)=−3v+3z."),
        (5, "What must be added to 2l²−m²+n² to get l²+m²−n²?", "Required expression=(l²+m²−n²)−(2l²−m²+n²)=−l²+2m²−2n²."),
        (6, "Subtract a²+b²+c² from 4a²+2b²−3c², then add that result to 5a²−6b².", "First difference=(4a²+2b²−3c²)−(a²+b²+c²)=3a²+b²−4c². Add it: 5a²−6b²+3a²+b²−4c²=8a²−5b²−4c²."),
        (7, "Subtract x−5y−z from the sum of 2x−y+z and x+y−5z.", "Sum=(2x−y+z)+(x+y−5z)=3x−4z. Subtract: (3x−4z)−(x−5y−z)=2x+5y−3z."),
        (8, "The sum of two expressions is 5u²+2uv−v². One is 2u²+3v². Find the other.", "Other=(5u²+2uv−v²)−(2u²+3v²)=3u²+2uv−4v²."),
        (9, "Subtract 2x²y−3y² from 3x²−5x²y+2y²; then subtract that result from the sum of 3xy²+5y²−2x²y and x²y+5x²−3xy².", "First result=3x²−7x²y+5y². The other sum=5x²−x²y+5y². Subtract the first from the sum: 2x²+6x²y."),
        (10, "If A=x²−xy+z, B=3x²+4xy+4z and C=7x²−6xy−7z, find (a) A+B; (b) A−B; (c) A+C; (d) A+B−C; (e) A−B+C; (f) A−B−C.", "a) 4x²+3xy+5z. b) −2x²−5xy−3z. c) 8x²−7xy−6z. d) −3x²+9xy+12z. e) 5x²−11xy−10z. f) −9x²+xy+4z."),
    ])
    replace_exercise(7, "Exercise 7.5", [
        (1, "Multiply.\na) (x³+3x²−x)(x−2)\nb) (−3x²+2x)(2y)(3+y)\nc) (7a²−3a+3)(3a−4)\nd) (2x+5)(x+1)\ne) 8u²(6u²−4u+1)\nf) (6a²−3a+3)(7a−4a²)\ng) (9y²−6y−3)(7y²−4y)\nh) (4k⁵−5k²+k³)(k²−k⁵)\ni) (4a−9)(4a²+5)\nj) (5n−4)(6n²−6n+6)\nk) (6x²+3x)(6x³+4x²)\nl) (8n²+4n)(6n²+6n−1)\nm) (r²+8)(4r²+8r−9)\nn) (2a³−5a+9)(9a−1)\no) (8x³+6x²)(5x²−8x)\np) (5a+8b)(a−3b)\nq) (2a²+6a+3)(7a²−6a+1)\nr) (7u³+8u−6u²)(6u⁴+4u³+3u²)\ns) (8v³+7v−3v²)(3v²+4v)\nt) (8m²+4m+6)(6m²−5m)\nu) (6f²+2l+3)(3f²+6)",
         "Distribute each term across the other factor, then combine like terms.\na) x⁴+x³−7x²+2x.\nb) −6x²y²−18x²y+4xy²+12xy.\nc) 21a³−37a²+21a−12.\nd) 2x²+7x+5.\ne) 48u⁴−32u³+8u².\nf) −24a⁴+54a³−33a²+21a.\ng) 63y⁴−78y³+3y²+12y.\nh) −4k¹⁰−k⁸+9k⁷+k⁵−5k⁴.\ni) 16a³−36a²+20a−45.\nj) 30n³−54n²+54n−24.\nk) 36x⁵+42x⁴+12x³.\nl) 48n⁴+72n³+16n²−4n.\nm) 4r⁴+8r³+23r²+64r−72.\nn) 18a⁴−2a³−45a²+86a−9.\no) 40x⁵−34x⁴−48x³.\np) 5a²−7ab−24b².\nq) 14a⁴+30a³−13a²−12a+3.\nr) 42u⁷−8u⁶+45u⁵+14u⁴+24u³.\ns) 24v⁵+23v⁴+9v³+28v².\nt) 48m⁴−16m³+16m²−30m.\nu) 18f⁴+6f²l+45f²+12l+18."),
    ])
    replace_exercise(7, "Exercise 7.6", [
        (1, "Simplify using the order of operations.\na) 5x + (4x+2)(3x−4)\nb) 4(x²+3x(2x+1))\nc) 2a[6a²−{3a+(2a²−a)}]\nd) −15u²−2v{v−4v(3v−2u)}\ne) 5x(r+y)+{r−(2x−y)}\nf) 7y−[2y²−{2y(3y²+y+1)}]\ng) 3m²−[(2m²−m+1)(m²+m)−2m(m+1)]\nh) 6k²−[(2k²−k)+(k²+k)(k+3)]\ni) 8u²−[(2u²−u)(u²+u+3)−6u²(u²+1)]\nj) 21v²−[2v(v+1)(v²+v)−4v²(v+1)]\nk) 64x−(12x−5x)+3\nl) (12x²+5x²)÷4x",
         "Work inside the innermost brackets, distribute products, then combine like terms.\na) (4x+2)(3x−4)=12x²−10x−8; add 5x to get 12x²−5x−8.\nb) 3x(2x+1)=6x²+3x; multiply the bracket by 4: 28x²+12x.\nc) 3a+(2a²−a)=2a²+2a; 6a²−(2a²+2a)=4a²−2a; multiply by 2a: 8a³−4a².\nd) v−4v(3v−2u)=v−12v²+8uv. Multiplying by −2v gives −2v²+24v³−16uv²; include −15u²: −15u²−16uv²+24v³−2v².\ne) 5x(r+y)+r−(2x−y)=5xr+5xy+r−2x+y.\nf) 2y(3y²+y+1)=6y³+2y²+2y; 7y−[2y²−(6y³+2y²+2y)]=6y³+9y.\ng) (2m²−m+1)(m²+m)=2m⁴+m³+m; 2m(m+1)=2m²+2m. Thus 3m²−[(2m⁴+m³+m)−(2m²+2m)] = −2m⁴−m³+5m²+m.\nh) (k²+k)(k+3)=k³+4k²+3k. Inside the bracket: k³+6k²+2k; subtract from 6k² to get −k³−2k.\ni) (2u²−u)(u²+u+3)=2u⁴+u³+5u²−3u; 6u²(u²+1)=6u⁴+6u². Subtract inside, then from 8u²: 4u⁴−u³+9u²+3u.\nj) 2v(v+1)(v²+v)=2v⁴+4v³+2v²; 4v²(v+1)=4v³+4v². The bracket is 2v⁴−2v²; result 23v²−2v⁴.\nk) 12x−5x=7x, so 64x−7x+3=57x+3.\nl) (12x²+5x²)/(4x)=17x²/(4x)=17x/4 (x≠0)."),
    ])
    replace_exercise(7, "Exercise 7.7", [
        (1, "Using identities, find each binomial square.\na) (a+b)²\nb) (5a+4b)²\nc) (x−y)²\nd) (7a−b)²\ne) (4c+3d)²\nf) (2m−n)²\ng) (6x−2y)²\nh) (5x+7y)²",
         "Apply (p+q)²=p²+2pq+q² and (p−q)²=p²−2pq+q².\na) a²+2ab+b².\nb) 25a²+40ab+16b².\nc) x²−2xy+y².\nd) 49a²−14ab+b².\ne) 16c²+24cd+9d².\nf) 4m²−4mn+n².\ng) 36x²−24xy+4y².\nh) 25x²+70xy+49y²."),
        (2, "Find each product using identities.\na) (2x+y)(2x−y)\nb) (4a−5)(4a+5)\nc) (6a+7b)(6a−7b)\nd) (m+n)(m−n)\ne) (c/2−2d)(c/2+2d)\nf) (11a−11b)(11a+11b)",
         "Use (p+q)(p−q)=p²−q².\na) 4x²−y².\nb) 16a²−25.\nc) 36a²−49b².\nd) m²−n².\ne) c²/4−4d².\nf) 121a²−121b²."),
        (3, "Find a²+b² if a−b=8 and ab=3.", "Square the difference: (a−b)²=a²−2ab+b². Therefore a²+b²=(a−b)²+2ab=8²+2(3)=64+6=70."),
        (4, "Find x²+1/x² if x−1/x=4.", "Square both sides: (x−1/x)²=x²−2+1/x²=16. Add 2 to both sides: x²+1/x²=18."),
    ])
    replace_exercise(7, "Exercise 7.8", [
        (1, "Factorize by taking common factors.\na) a⁴−2a²\nb) ab−bc\nc) 2xy−4xy−6xy\nd) 32xy−16x\ne) 7a²b+ab−7a²c−ac\nf) 6x⁴−2x³y+3x⁴y²−x³y³\ng) 6x+9y+18z\nh) x(x²−y)−5x(x−y)\ni) (a²+bc)−(b+c)a",
         "Factor out the greatest common factor in each expression.\na) a²(a²−2).\nb) b(a−c).\nc) −8xy (combining like terms first).\nd) 16x(2y−1).\ne) (a−c)(7a²+b).\nf) x³(6x−2y+3xy²−y³).\ng) 3(2x+3y+6z).\nh) x[(x²−y)−5(x−y)]=x(x²−5x+4y).\ni) a²+bc−ab−ac=(a−c)(a−b)."),
        (2, "Factorize using algebraic identities.\na) 4x²−9\nb) 81a²−b²\nc) 4y²−16\nd) 5u²−80v²\ne) (a+b)²−c²\nf) 100x²−81\ng) 16x²−49y²\nh) (x/2)²−(y+9)²\ni) a⁴−b⁴\nj) 4x²+12xy+9y²\nk) a²−2a+1\nl) a⁴/b²−8ab+16b⁴/a²\nm) 1+14n+49n²\nn) 25a²−10ab+b²\no) 9a²+30ab+25b²\np) 81x²+72xy+16y²\nq) 4x²−12+9/x²\nr) 4x²−36x²yz+81x²y²z²",
         "Use difference of squares or perfect-square identities.\na) (2x−3)(2x+3).\nb) (9a−b)(9a+b).\nc) 4(y−2)(y+2).\nd) 5(u−4v)(u+4v).\ne) (a+b−c)(a+b+c).\nf) (10x−9)(10x+9).\ng) (4x−7y)(4x+7y).\nh) (x/2−y−9)(x/2+y+9).\ni) (a−b)(a+b)(a²+b²).\nj) (2x+3y)².\nk) (a−1)².\nl) (a²/b−4b²/a)².\nm) (1+7n)².\nn) (5a−b)².\no) (3a+5b)².\np) (9x+4y)².\nq) (2x−3/x)².\nr) (2x−9xyz)²."),
        (3, "Factorize by grouping.\na) a²+8a+4a+32\nb) x²+3x−5x−15\nc) 7x²+49x+7x+x²\nd) 9−9n−n+n²\ne) ax+bx−ay−by\nf) 25a²+3b²+15b+5a²b\ng) x²−6xy−3x²y+18xy²\nh) a²−2a+ab−2b\ni) c²−7c+5c−35",
         "Group terms, factor each group, then factor out the common binomial.\na) (a+4)(a+8).\nb) (x−5)(x+3).\nc) 8x(x+7).\nd) (1−n)(9−n).\ne) (a+b)(x−y).\nf) (b+5)(5a²+3b).\ng) x(x−3y)(x−6y).\nh) (a−2)(a+b).\ni) (c−7)(c+5)."),
    ])
    replace_exercise(7, "Exercise 7.9", [
        (1, "Factorize by middle-term breaking.\na) 2x²+5x+2\nb) x²−9x+18\nc) x²+3x−4=0\nd) x²−12x+35\ne) x²+5x+4\nf) 9x²+6x+1\ng) 2x²+7x+3",
         "Split the middle term into factors of the constant term whose sum is the x coefficient.\na) 2x²+4x+x+2=(2x+1)(x+2).\nb) x²−3x−6x+18=(x−3)(x−6).\nc) x²+4x−x−4=(x−1)(x+4); therefore x=1 or x=−4.\nd) x²−5x−7x+35=(x−5)(x−7).\ne) x²+x+4x+4=(x+1)(x+4).\nf) (3x+1)².\ng) 2x²+6x+x+3=(2x+1)(x+3)."),
        (2, "Think Higher: Find the yellow area. The outer rectangle is (2x+4) by 4x; the blue rectangle is (2x−2) by (2x−1), and the purple square has side x.",
         "Yellow area = outer rectangle − blue rectangle − purple square = 4x(2x+4)−(2x−2)(2x−1)−x². Expand: 8x²+16x−(4x²−6x+2)−x²=3x²+22x−2 square units."),
    ])
    replace_exercise(7, "Review Exercise", [
        (1, "Choose the correct option.\na) Letters representing unknown quantities: variables / coefficients / constants / exponents.\nb) The value of a ______ is not fixed: coefficient / variable / constant / exponent.\nc) Repeated multiplication of the same variable is represented by: coefficient / variable / constant / exponent.\nd) In 2x²+3x−1, the constant is: x / −1 / 2 / 3.\ne) The highest exponent in a polynomial is its: degree / coefficient / power / term.\nf) Polynomial variable exponents must be: whole / integer / even / odd numbers.\ng) A polynomial with two terms is a: monomial / binomial / trinomial / quadrinomial.", "a) variables. b) variable. c) exponent. d) −1. e) degree. f) whole (non-negative integers). g) binomial."),
        (2, "If the nth term is 5n−2, find the 7th term.", "Substitute n=7: 5(7)−2=35−2=33."),
        (3, "If the nth term is 8n+1, find the 15th term.", "Substitute n=15: 8(15)+1=120+1=121."),
        (4, "Find each sum.\na) a², a²−b², and a²−b²+c²\nb) uv²+4u²v, −6u²v−2uv²+1\nc) 6x²+4y−6z², −6x−7y−z, and 7x²+9y\nd) 6u²−8v+9w and −2u²+2v",
         "Combine like terms.\na) 3a²−2b²+c².\nb) (uv²−2uv²)+(4u²v−6u²v)+1=−uv²−2u²v+1.\nc) 13x²−6x+6y−6z²−z.\nd) 4u²−6v+9w."),
        (5, "Subtract as directed.\na) Subtract 4x²−5y² from 3x²−6y².\nb) Subtract 99l−4m+5n from 15l−8m−9n.\nc) Subtract 10x²−12y²+15x−16y from 17x²−13y²−31x−16y.\nd) Subtract 3a²+ab−bc−3c from 9a²−5bc+6ab−4c.",
         "Subtract by changing the signs of the expression being removed.\na) −x²−y².\nb) −84l−4m−14n.\nc) 7x²−y²−46x.\nd) 6a²+5ab−4bc−c."),
        (6, "Find the products.\na) x², x³ and x\nb) (5−9a)(4a²+6a−3)\nc) 3x(2+4x)(6x²−2x)\nd) (6x²−4x²+x−9)(3x²+7x)",
         "Multiply and combine like terms.\na) x²·x³·x=x⁶.\nb) −36a³−34a²+57a−15.\nc) First (2+4x)(6x²−2x)=24x³+4x²−4x; multiplying by 3x gives 72x⁴+12x³−12x².\nd) (2x²+x−9)(3x²+7x)=6x⁴+17x³−20x²−63x."),
        (7, "Simplify.\na) 12a²−[a²−5a(5a²−a)]\nb) 7u²−[2u−{3u(2u+3u)}]\nc) 11a−(2a²−a)+4a²−7a+6a²\nd) 13(u+v)+{8(u−v)−3(u+6u−u)}",
         "Simplify inside brackets first.\na) 12a²−[a²−25a³+5a²]=25a³+6a².\nb) 3u(5u)=15u²; 7u²−[2u−15u²]=22u²−2u.\nc) 11a−2a²+a+4a²−7a+6a²=8a²+5a.\nd) 13u+13v+8u−8v−3(6u)=3u+5v."),
        (8, "Factorize.\na) p²+7p−2p−14\nb) 2ab−6bc−a+3c\nc) y²+3y−6y−18\nd) x²−6xy−3x+18y\ne) a²−2a+ab−2b\nf) x²−8x+16\ng) 5x²+11x+2\nh) 3x²−8x+4\ni) 4x²+7x+3",
         "Factor by grouping or splitting the middle term.\na) (p+7)(p−2).\nb) (a−3c)(2b−1).\nc) (y−6)(y+3).\nd) (x−3)(x−6y).\ne) (a−2)(a+b).\nf) (x−4)².\ng) (5x+1)(x+2).\nh) (3x−2)(x−2).\ni) (4x+3)(x+1)."),
    ])
    replace_exercise(8, "Exercise 8.1", [
        (1, "Solve using the balancing method and verify.\na) 8x+1/2=−10\nb) −99x=33\nc) 7−5x=−3/4\nd) 32x/4+16x/5=10\ne) 2−11x=5x−4\nf) 4(x−3)=4(3x+1)\ng) 0.34x+2.4=6.5x\nh) 7(x+4)=25(x−4)\ni) (0.3x−0.6)/(5x−4)=0.6/0.5\nj) 7+4(3x−1)=2x−3\nk) (5x−0.3)/(7x−2.1)=5/6",
         "Apply the same operation to both sides; substitute each result to verify.\na) 8x=−10.5, x=−21/16. Check: −10.5+0.5=−10.\nb) x=−1/3. Check: −99(−1/3)=33.\nc) −5x=−31/4, x=31/20.\nd) (8+16/5)x=10; (56/5)x=10, x=25/28.\ne) 6=16x, x=3/8.\nf) −12=8x+4, x=−2.\ng) 2.4=6.16x, x=30/77.\nh) 18x=128, x=64/9.\ni) Since 0.6/0.5=1.2, 0.3x−0.6=6x−4.8; x=14/19 (and 5x−4≠0).\nj) 10x=−6, x=−3/5.\nk) Cross multiply: 6(5x−0.3)=5(7x−2.1); x=87/50."),
        (2, "Solve using the transposition method and verify.\na) 5x−7=44\nb) 14x=28\nc) 2(x−2)/(2x+4)=8/3\nd) (2x−2)/(3x−3)=1 1/3\ne) 0.8x/(3.4x+0.1)=1 1/3\nf) (4y+6)/(5y+7)=1/2",
         "a) 5x=51, x=51/5.\nb) x=2.\nc) Cross multiply: 6(x−2)=8(x+2), giving x=−22/5 (denominator is nonzero).\nd) For x≠1, (2x−2)/(3x−3)=2/3, which cannot equal 4/3; there is no solution. At x=1 the expression is undefined.\ne) Cross multiply: 12x=68x+2, so x=−1/28? Rechecking with fractions: 0.8x=4/3(3.4x+0.1) gives 2.4x=13.6x+0.4; hence x=−1/28.\nf) 2(4y+6)=5y+7, so y=−5/3."),
    ])
    replace_exercise(8, "Exercise 8.2", [
        (1, "The sum of four consecutive multiples of 6 is 84. Find the four multiples.", "Let the multiples be 6n, 6(n+1), 6(n+2), 6(n+3). Their sum is 24n+36=84, so n=2. The multiples are 12, 18, 24 and 30."),
        (2, "The difference between the digits of a two-digit number is 4. Interchanging the digits makes the sum of the original and new numbers 110. Find the number.", "Let the tens and units digits be a and b. Then a+b=10 because (10a+b)+(10b+a)=110. Also |a−b|=4. Thus (a,b)=(7,3) or (3,7); the possible original numbers are 73 and 37."),
        (3, "If 990 is decreased by 3 times a number, the result is the number decreased by 30. Find the number.", "990−3x=x−30. Thus 1020=4x and x=255."),
        (4, "Find the number if two fifths of it increased by 2 is half of it.", "(2/5)x+2=x/2. Multiply by 10: 4x+20=5x, so x=20."),
        (5, "In a library, 2/5 of the books are Hadith books. Three fourths of the remaining books are Mathematics books. The 642 books remaining are on other subjects. Find the total number of books.", "After Hadith books, 3/5 of the total remains. Other-subject books are one fourth of that remainder: (1/4)(3/5)T=642. Hence 3T/20=642 and T=4,280 books."),
        (6, "The second angle in a triangle is two thirds of the first angle. The third angle is 36 less than twice the second angle. Find all angles.", "Let the first angle be A; the second is 2A/3 and the third is 2(2A/3)−36. Their sum is 180: A+2A/3+4A/3−36=180, so A=72°. The second is 48° and the third is 60°."),
        (7, "The difference between two supplementary angles is 40°. Find the angles.", "Let the larger be x and smaller y. x+y=180 and x−y=40. Adding gives 2x=220, so x=110° and y=70°."),
        (8, "Noor is 5 years older than Umair. After 4 years, Umair will be half as old as Noor. Find their present ages.", "Let Umair be u; Noor is u+5. Then u+4=(u+5+4)/2, giving 2u+8=u+9 and u=1. Umair is 1 year old and Noor is 6."),
    ])
    replace_exercise(8, "Exercise 8.3", [
        (1, "Identify which are linear equations in two variables. Justify.\na) 6x+3=0\nb) 7x−7y=9\nc) 2x−3y=14\nd) 2x²+5y=3\ne) 6x−8y²=12\nf) 8x−2y=10\ng) 16x²+z=8",
         "A linear equation in two variables has each variable to the first power and can be written ax+by=c.\na) No: it has only x (the y coefficient is zero).\nb) Yes, first degree in x,y.\nc) Yes, first degree in x,y.\nd) No: x has exponent 2.\ne) No: y has exponent 2.\nf) Yes, first degree in x,y.\ng) No: x has exponent 2 (also uses z rather than y)."),
        (2, "Construct a linear equation in two variables. Let x and y be the two numbers.\na) 24 less than twice a number equals three times another number.\nb) 15 added to a number equals twice another number.\nc) A number subtracted from 8, added to four times another number, equals 20.\nd) 8 decreased by a number equals 5 added to another number.\ne) Twice a number decreased by 7 equals five times another number.\nf) Thrice a number equals another number decreased by 2.",
         "Translate each statement directly.\na) 2x−24=3y.\nb) x+15=2y.\nc) (8−x)+4y=20.\nd) 8−x=5+y.\ne) 2x−7=5y.\nf) 3x=y−2."),
        (3, "Seven silver chains and three golden chains have a total length of 27 m. Construct an equation in two variables.", "Let x be the length of a silver chain and y the length of a golden chain, in metres. Then 7x+3y=27."),
        (4, "Eight buckets and nine tubs have a total capacity of 121 litres. Construct an equation in two variables.", "Let x be the capacity of one bucket and y the capacity of one tub, in litres. Then 8x+9y=121."),
        (5, "Hassan's age added to three times Nida's age is 30 years. Construct an equation in two variables.", "Let x be Hassan's age and y Nida's age. Then x+3y=30."),
        (6, "The price of 10 books and 3 notebooks is Rs 2,950. Construct an equation in two variables.", "Let x be the price of a book and y the price of a notebook, in rupees. Then 10x+3y=2,950."),
    ])
    replace_exercise(8, "Exercise 8.4", [
        (1, "Solve each equation for y and give at least five ordered-pair solutions.\na) 2x−y=1\nb) x+y=3\nc) 3x+2y=−2\nd) 2x−y=−1\ne) 2x+3y=10\nf) 3x+4y=18\ng) 2x+y=6\nh) 3x+y=4\ni) y=−4x+3\nj) y−2=x\nk) 2x−y=8\nl) −2x−y=−1",
         "Isolate y, then substitute convenient x-values. Each ordered pair is (x,y), and every listed pair satisfies its equation.\na) y=2x−1: (0,−1),(1,1),(2,3),(3,5),(4,7).\nb) y=3−x: (0,3),(1,2),(2,1),(3,0),(4,−1).\nc) y=−(3x+2)/2: (−4,5),(−2,2),(0,−1),(2,−4),(4,−7).\nd) y=2x+1: (0,1),(1,3),(2,5),(3,7),(4,9).\ne) y=(10−2x)/3: (−2,4),(1,2),(4,0),(7,−2),(10,−4).\nf) y=(18−3x)/4: (−2,6),(2,3),(6,0),(10,−3),(14,−6).\ng) y=6−2x: (0,6),(1,4),(2,2),(3,0),(4,−2).\nh) y=4−3x: (0,4),(1,1),(2,−2),(3,−5),(4,−8).\ni) y=−4x+3: (0,3),(1,−1),(2,−5),(3,−9),(4,−13).\nj) y=x+2: (0,2),(1,3),(2,4),(3,5),(4,6).\nk) y=2x−8: (0,−8),(1,−6),(2,−4),(3,−2),(4,0).\nl) y=1−2x: (0,1),(1,−1),(2,−3),(3,−5),(4,−7)."),
    ])
    replace_exercise(8, "Exercise 8.5", [
        (1, "Identify the quadrant for each ordered pair.\na) (1,1)\nb) (1,−1)\nc) (4,2)\nd) (−2,−3)\ne) (2,1)\nf) (1,−9)\ng) (−5,2)\nh) (3,−5)\ni) (−3,2)", "Quadrant signs are I (+,+), II (−,+), III (−,−), IV (+,−).\na) I. b) IV. c) I. d) III. e) I. f) IV. g) II. h) IV. i) II."),
        (2, "Read x and y and write the ordered pair for each plotted point on the graph.", "Reading from the plotted grid: (3,3), (−3,−2), (−5,−4), and (7,−6). Check each by moving horizontally from the origin for x, then vertically for y."),
        (3, "Plot each ordered pair.\na) E(9,−5)\nb) Q(−6,2)\nc) D(−8,4)\nd) S(9,−2)\ne) T(−1,−3)\nf) L(2,6)\ng) N(0,−3)\nh) J(5,−5)\ni) F(−1,−1)\nj) B(−7,−8)\nk) D(7,−1)", "Plot x first along the horizontal axis, then y vertically.\na) (9,−5), quadrant IV. b) (−6,2), quadrant II. c) (−8,4), quadrant II. d) (9,−2), quadrant IV. e) (−1,−3), quadrant III. f) (2,6), quadrant I. g) (0,−3), on the negative y-axis. h) (5,−5), quadrant IV. i) (−1,−1), quadrant III. j) (−7,−8), quadrant III. k) (7,−1), quadrant IV."),
    ])
    replace_exercise(8, "Exercise 8.6", [
        (1, "Identify which equations describe vertical or horizontal lines, then graph.\na) 2x−8=0\nb) 3x+6=0\nc) x−5=0\nd) 2y−4=0\ne) 3y−9=0\nf) y−5=0", "Solve for the fixed coordinate.\na) x=4, vertical; points (4,0),(4,2).\nb) x=−2, vertical; points (−2,0),(−2,2).\nc) x=5, vertical; points (5,0),(5,2).\nd) y=2, horizontal; points (0,2),(2,2).\ne) y=3, horizontal; points (0,3),(2,3).\nf) y=5, horizontal; points (0,5),(2,5). Join each pair with a straight line."),
        (2, "Draw the graphs.\na) x=3\nb) x=−8\nc) x=2\nd) x=−1\ne) x=4\nf) x=2.5\ng) x=4.5\nh) x=−1.5", "Each is a vertical line. Use two points with the fixed x-coordinate: a) (3,0),(3,2); b) (−8,0),(−8,2); c) (2,0),(2,2); d) (−1,0),(−1,2); e) (4,0),(4,2); f) (2.5,0),(2.5,2); g) (4.5,0),(4.5,2); h) (−1.5,0),(−1.5,2)."),
        (3, "Draw the graphs.\na) y=4\nb) y=−9\nc) y=3.5\nd) y=−2.5\ne) y=5\nf) y=−1\ng) y=−3\nh) y=−5", "Each is a horizontal line. Use two points with the fixed y-coordinate: a) (0,4),(2,4); b) (0,−9),(2,−9); c) (0,3.5),(2,3.5); d) (0,−2.5),(2,−2.5); e) (0,5),(2,5); f) (0,−1),(2,−1); g) (0,−3),(2,−3); h) (0,−5),(2,−5)."),
    ])
    replace_exercise(8, "Exercise 8.7", [
        (1, "Plot the graph of each linear equation in two variables.\na) 3x−5y=20\nb) 5x−y=10\nc) 2x+3y=10\nd) 3x+4y=18\ne) x+y=6\nf) x+y=18\ng) 3x−2y=21\nh) 4x+y=29\ni) −2x+y=−1\nj) 3x+y=4\nk) y=−4x+3\nl) y−2=x",
         "Find two points per equation, plot them, and join them with a straight line.\na) y=(3x−20)/5; points (0,−4),(5,−1).\nb) y=5x−10; (0,−10),(2,0).\nc) y=(10−2x)/3; (2,2),(5,0).\nd) y=(18−3x)/4; (2,3),(6,0).\ne) y=6−x; (0,6),(6,0).\nf) y=18−x; (0,18),(18,0).\ng) y=(3x−21)/2; (1,−9),(7,0).\nh) y=29−4x; (0,29),(7,1).\ni) y=2x−1; (0,−1),(1,1).\nj) y=4−3x; (0,4),(1,1).\nk) y=−4x+3; (0,3),(1,−1).\nl) y=x+2; (0,2),(1,3).\nThink Higher: a) With east and north positive, Zara's position is (−3,−2) km. b) Let c be the crayon length and e the eraser length, in cm: c−2e=5."),
    ])
    replace_exercise(8, "Review Exercise", [
        (1, "Choose the correct option.\na) If 4x/6=2, then x is: 2, 3, 4, or 6.\nb) Which is not linear: 8x−5=60; 3x+5y²=12; 3/4+x=0; 3/(2x)−1/x=3/5?\nc) Solve 8x+5=3x+4 (options −1/6, −1/5, −6, −5).\nd) Solve the printed decimal equation 0.1x+0.1=0.2x+0.3 (options 0,1,0.2,1.2).\ne) Standard form of a linear equation in x,y.\nf) Identify a linear equation in two variables: 2x+3=0; 3x−y=6; 4x²−7y=2; x−3=8.\ng) Solve 2x+3=0 (options 5,−3,−3/2,−2/3).\nh) Which pair satisfies 2x−y=−1?\ni) Which quadrant contains (4,−2)?\nj) Which point is not in quadrant III: (−2,−1),(−3,−1),(−1,2),(−3,−2)?",
         "a) x=3 (option ii). b) Both 3x+5y²=12 and 3/(2x)−1/x=3/5 are nonlinear as printed (options ii and iv), so the single-choice item is ambiguous. c) 5x=−1, x=−1/5 (option ii). d) Solving the printed equation gives x=−2, absent from the options; the scan or answer choices contain an error. e) ax+by=c (option iii). f) 3x−y=6 (option ii). g) x=−3/2 (option iii). h) (−2,−3), since −4−(−3)=−1 (option iv). i) Quadrant IV. j) (−1,2) (option iii)."),
        (2, "Write three examples of linear equations in one variable.", "Examples: 2x+5=11; 7x−3=18; x/4=6. Each has one variable to the first power."),
        (3, "Write the standard form of the equation of a: a) horizontal line; b) vertical line.", "a) y=c, where c is a constant. b) x=c, where c is a constant."),
        (4, "Solve and verify.\na) 3(0.2x+3)/[4(5.2x−3)]=−7/2\nb) (9x−3)/3=(4x−3)/2\nc) 7(8x−1)/[12(x−2)]=8/9",
         "a) Cross multiply: 6(0.2x+3)=−28(5.2x−3). Thus 1.2x+18=−145.6x+84, so x=165/367. Substitution gives both sides −7/2.\nb) 2(9x−3)=3(4x−3), so 18x−6=12x−9 and x=−1/2. Both sides equal −5/2.\nc) 63(8x−1)=96(x−2), so 408x=−129 and x=−43/136. Substitution verifies the equality; x≠2."),
        (5, "The sum of five consecutive odd numbers is 625. Find them.", "Let the middle odd number be n. The five are n−4,n−2,n,n+2,n+4; their sum is 5n=625, so n=125. Numbers: 121,123,125,127,129."),
        (6, "The price of a printer is 1/8 the price of a photocopy machine. Four photocopy machines and seven printers cost Rs 77,025. Find each price.", "Let copier price be c; printer price is c/8. Then 4c+7c/8=77,025, so 39c/8=77,025 and c=Rs 15,800. Printer=15,800/8=Rs 1,975."),
        (7, "A rectangular garden has perimeter 190 m. Its length is 5 less than three times its width. Find both dimensions.", "Let width=w and length=3w−5. Then 2(l+w)=190, so (3w−5)+w=95; 4w=100 and w=25 m. Length=70 m."),
        (8, "In an isosceles triangle, the second angle is 20° more than half of one base angle. Find all angles.", "Let each equal base angle be b. The second (vertex) angle is b/2+20. Then 2b+b/2+20=180, so b=64°. The vertex angle is 52°. Angles: 64°,64°,52°."),
        (9, "Construct equations in x and y.\na) 2 subtracted from 4 times a number equals 4 times another number.\nb) 8 added to twice a number equals thrice another number.\nc) A number decreased by 3 equals 4 times another number.\nd) 2 decreased by a number equals another number.", "a) 4x−2=4y. b) 2x+8=3y. c) x−3=4y. d) 2−x=y."),
        (10, "Three rice bags and five sugar bags have a mass of 65 kg. Write a linear equation in two variables.", "Let r and s be the mass of one rice and sugar bag in kg. 3r+5s=65."),
        (11, "Ten cakes and four sandwiches cost Rs 6,800. Write a linear equation in two variables.", "Let c be the price of a cake and s the price of a sandwich. 10c+4s=6,800."),
        (12, "Give at least five solutions and graph each equation.\na) x−y=4\nb) 2x−y=1\nc) x+2y=3\nd) x−2y=2",
         "a) y=x−4: (0,−4),(1,−3),(2,−2),(3,−1),(4,0).\nb) y=2x−1: (0,−1),(1,1),(2,3),(3,5),(4,7).\nc) y=(3−x)/2: (−3,3),(−1,2),(1,1),(3,0),(5,−1).\nd) y=(x−2)/2: (0,−1),(2,0),(4,1),(6,2),(8,3). Plot each set and join its points with a straight line."),
        (13, "Plot A(−5,2), B(2,−3), C(4,1), and D(−3,−5) on the coordinate plane.", "A lies in quadrant II, B in IV, C in I, and D in III. Plot each by moving x units horizontally from the origin, then y units vertically."),
        (14, "Write the ordered pair for each plotted point on the graph.", "Reading the plotted grid: (1,9), (11,8), (−7,4), (−7,−2), (−9,−6), (6,−1), and (10,−7)."),
        (15, "Find the ordered pair(s) with x-coordinate 5 from the labeled graph.", "Only point R has x=5; its ordered pair is (5,4)."),
        (16, "Graph in one variable: a) x−5=0; b) 2x+1=0; c) y−5=0; d) 2y+1=0.", "a) x=5, vertical. b) x=−1/2, vertical. c) y=5, horizontal. d) y=−1/2, horizontal."),
        (17, "Graph: a) x=3; b) x=−10; c) x=−1; d) x=−3.5.", "These are vertical lines through their stated x-values. Two points per line: a) (3,0),(3,2); b) (−10,0),(−10,2); c) (−1,0),(−1,2); d) (−3.5,0),(−3.5,2)."),
        (18, "Graph: a) y=−2.5; b) y=3; c) y=−7; d) y=4.", "These are horizontal lines through their stated y-values. Two points per line: a) (0,−2.5),(2,−2.5); b) (0,3),(2,3); c) (0,−7),(2,−7); d) (0,4),(2,4)."),
        (19, "Math Project: In groups, place labeled location stickers on a Cartesian plane and challenge other groups to identify ordered pairs or place markers at named ordered pairs.", "Sample solution: choose and label any coordinates, such as school (−3,2), hospital (2,4), bank (5,−1), park (−4,−3), and shop (1,−2). Record each marker's ordered pair; award a point for each correctly identified location and subtract one for an incorrect response, as the project directs."),
    ])
    replace_exercise(9, "Exercise 9.2", [
        (1, "Find each circumference using π=3.14. In the diagrams, a–c show diameters and d–f show radii.\na) 11.5 cm\nb) 2 cm\nc) 4.2 cm\nd) r=5 cm\ne) r=3.2 cm\nf) r=6.2 mm",
         "Use C=πd or C=2πr.\na) 3.14(11.5)=36.11 cm.\nb) 3.14(2)=6.28 cm.\nc) 3.14(4.2)=13.188 cm.\nd) 2(3.14)(5)=31.4 cm.\ne) 2(3.14)(3.2)=20.096 cm.\nf) 2(3.14)(6.2)=38.936 mm."),
        (2, "Find each circumference from its radius.\na) 0.5 cm\nb) 4 cm\nc) 7.2 m\nd) 9.6 cm\ne) 10.5 cm\nf) 100.5 cm", "Apply C=2πr (π=3.14). a) 3.14 cm. b) 25.12 cm. c) 45.216 m. d) 60.288 cm. e) 65.94 cm. f) 631.14 cm."),
        (3, "Find each circumference from its diameter.\na) 6.8 cm\nb) 5.5 cm\nc) 8.3 cm\nd) 11.6 cm\ne) 4.4 m\nf) 9.5 cm", "Apply C=πd (π=3.14). a) 21.352 cm. b) 17.27 cm. c) 26.062 cm. d) 36.424 cm. e) 13.816 m. f) 29.83 cm."),
        (4, "The diameter of a circle is 12.4 cm. Find its circumference.", "C=πd=3.14(12.4)=38.936 cm."),
        (5, "A circle has circumference 48.984 cm. Find its radius and diameter.", "d=C/π=48.984/3.14=15.6 cm; r=d/2=7.8 cm."),
        (6, "A circle has radius 6.5 cm. Find its diameter.", "d=2r=13 cm."),
        (7, "A circle has diameter 23.3 cm. Find its circumference.", "C=3.14(23.3)=73.162 cm."),
        (8, "Find the circumference of a wheel whose diameter is 34 cm.", "C=3.14(34)=106.76 cm per revolution."),
        (9, "Find the area of circles with these radii.\na) 2.3 cm\nb) 6.5 cm\nc) 11.2 cm\nd) 8.5 cm\ne) 10.7 m\nf) 14.8 m\ng) 2.7 m\nh) 9.25 m", "Use A=πr² with π=3.14. a) 16.6106 cm². b) 132.665 cm². c) 393.8816 cm². d) 226.865 cm². e) 359.4986 m². f) 687.7856 m². g) 22.8906 m². h) 268.66625 m²."),
        (10, "Find the area of a circle whose diameter is 6.2 cm.", "r=3.1 cm. A=3.14(3.1²)=30.1754 cm²."),
        (11, "A circle has diameter 15.5 m. Find its area.", "r=7.75 m. A=3.14(7.75²)=188.59625 m²."),
        (12, "A circle has circumference 44.588 cm. Find its area.", "r=C/(2π)=44.588/6.28=7.1 cm. A=3.14(7.1²)=158.2874 cm²."),
        (13, "A circle has area 54.95 m². Find its circumference.", "r=√(A/π)=√(54.95/3.14)=√17.5≈4.1833 m. Thus C=2πr≈26.2711 m."),
    ])
    replace_exercise(9, "Exercise 9.1", [
        (1, "Find the perimeter and area of the composite shapes.\na) An L shape has top width 6 m, top strip height 2 m, inner horizontal 2 m, inner vertical 5 m and bottom width 3 m.\nb) An L shape has vertical arm height 4 m, horizontal arm length 5 m, arm thickness 2 m and inner horizontal length 3 m.",
         "a) Missing left vertical=2+5=7 m; missing short horizontal=6−2−3=1 m. Area=6×2+3×5=27 m². Perimeter=6+2+2+5+3+7+1=26 m.\nb) Missing upright width=5−3=2 m; total height=4+2=6 m. Area=2×4+5×2=18 m². Perimeter=2(5+6)=22 m."),
        (2, "Find the perimeter and area of each shaded region.\na) L-shaped outer region: top 6 m, right side 12 m, lower stem width 1 m, inner step height 4 m; subtract a 1 m×1 m unshaded square.\nb) Cross-shaped outer region: top bar 8 m wide, outer upper height 4 m, left arm 3 m×3 m, lower stem 6 m×4 m and right step 2 m; subtract an unshaded 4 m×2 m rectangle.",
         "a) L area before the square=6×8+1×4=52 m²; subtract 1 m², so shaded area=51 m². Outer boundary=36 m; add the square-hole boundary 4 m, giving shaded perimeter=40 m.\nb) Decompose the yellow region into top bar 8×4, left arm 3×3 and lower stem 6×4, then subtract the 4×2 hole: area=32+9+24−8=57 m². The outer boundary is 38 m and the hole boundary is 12 m, so total shaded perimeter=50 m."),
    ])
    replace_exercise(9, "Exercise 9.3", [
        (1, "A car wheel has diameter 54 cm. How far does the car travel after 423 revolutions?", "Distance per revolution=C=πd=3.14(54)=169.56 cm. In 423 revolutions: 169.56×423=71,723.88 cm=717.2388 m."),
        (2, "A circular ground has diameter 31 m. Find (a) the cost of planting grass at Rs 345/m²; (b) the cost of fencing at Rs 143/m.", "r=15.5 m. Area=3.14(15.5²)=754.385 m²; grass cost=754.385×345=Rs 260,262.825 (≈Rs 260,262.83). Circumference=3.14(31)=97.34 m; fencing cost=97.34×143=Rs 13,919.62."),
        (3, "A circular parking area has radius 112.2 m. Find the cost of tiling at Rs 580/m².", "Area=3.14(112.2²)=39,528.9576 m². Cost=39,528.9576×580=Rs 22,926,795.408 (≈Rs 22,926,795.41)."),
        (4, "A circular playground has diameter 5.7 m. Find the cost of planting grass at Rs 342/m².", "r=2.85 m. Area=3.14(2.85²)=25.50465 m². Cost=25.50465×342=Rs 8,722.5903."),
        (5, "A train wheel has radius 0.34 m. How far will the train travel in 1,234 revolutions?", "Circumference per revolution=2(3.14)(0.34)=2.1352 m. Distance=2.1352×1,234=2,634.8368 m."),
        (6, "A circular playground has diameter 890 m. Find the total cost if half is planted with grass at Rs 85/m² and the rest cemented at Rs 404/m².", "Radius=445 m; total area=3.14(445²)=621,798.5 m², so each half is 310,899.25 m². Total cost=310,899.25(85+404)=Rs 152,029,733.25."),
        (7, "A circular walking track has radius 10 m and a 2 m wide path around the inside boundary. Find construction cost at Rs 450/m².", "The path is the annulus between radii 10 m and 8 m. Area=3.14(10²−8²)=113.04 m². Cost=113.04×450=Rs 50,868."),
        (8, "The circumference of a circular ground is 6,561.3 m. Find its radius.", "r=C/(2π)=6,561.3/6.28≈1,044.793 m (about 1,044.79 m)."),
    ])
    replace_exercise(9, "Exercise 9.4", [
        (1, "Find the total surface area of each cylinder.\na) diameter 8 cm, length 10 cm\nb) diameter 6 cm, height 3.5 cm\nc) radius 4 cm, height 9 cm\nd) diameter 15 cm, height 4.2 cm\ne) radius 5 m, height 10 m\nf) diameter 7.2 m, height 5.2 m",
         "Use TSA=2πr(r+h), with π=3.14.\na) r=4: 2(3.14)(4)(14)=351.68 cm².\nb) r=3: 2(3.14)(3)(6.5)=122.46 cm².\nc) 2(3.14)(4)(13)=326.56 cm².\nd) r=7.5: 2(3.14)(7.5)(11.7)=551.07 cm².\ne) 2(3.14)(5)(15)=471 m².\nf) r=3.6: 2(3.14)(3.6)(8.8)=198.9504 m²."),
        (2, "A rod is 6 cm long and has radius 4.1 cm. Find its curved surface area.", "CSA=2πrh=2(3.14)(4.1)(6)=154.488 cm²."),
        (3, "A cylinder has diameter 19.2 cm and length 5.3 cm. Find its curved surface area.", "CSA=πdh=3.14(19.2)(5.3)=319.5264 cm²."),
        (4, "A cylinder has radius 2.3 cm and length 6.3 cm. Find its total surface area.", "TSA=2πr(r+h)=2(3.14)(2.3)(2.3+6.3)=124.2184 cm²."),
        (5, "Find the total surface area of a 4.3 cm long tin with radius 3.5 cm.", "TSA=2πr(r+h)=2(3.14)(3.5)(3.5+4.3)=171.444 cm²."),
    ])
    replace_exercise(9, "Exercise 9.5", [
        (1, "Find the volume of each cylinder.\na) r=7.2 cm, h=5 cm\nb) r=1 cm, h=3 cm\nc) r=9 cm, h=8 cm\nd) r=12 cm, h=6 cm\ne) r=5 cm, h=14 cm\nf) diameter=10 cm, length=20 cm",
         "Use V=πr²h with π=3.14.\na) 3.14(7.2²)(5)=813.888 cm³.\nb) 3.14(1²)(3)=9.42 cm³.\nc) 3.14(9²)(8)=2,034.72 cm³.\nd) 3.14(12²)(6)=2,712.96 cm³.\ne) 3.14(5²)(14)=1,099 cm³.\nf) r=5 cm: 3.14(5²)(20)=1,570 cm³."),
        (2, "Find each cylinder's volume.\na) h=24 m, r=10 m\nb) h=5.5 m, r=2.7 m\nc) h=6.2 cm, r=6.9 cm\nd) h=33.4 m, r=11.5 m\ne) h=12.4 m, r=5.7 m\nf) h=9 cm, r=6 cm",
         "V=πr²h.\na) 7,536 m³. b) 125.8983 m³. c) 926.87148 cm³. d) 13,869.851 m³. e) 1,265.03064 m³. f) 1,017.36 cm³."),
        (3, "Find the volume of a cylinder with height 8.8 cm and radius 2.7 cm.", "V=3.14(2.7²)(8.8)=201.43728 cm³."),
        (4, "A cylinder has volume 233.34 cm³ and height 8 cm. Find its radius.", "r=√(V/(πh))=√(233.34/(3.14×8))≈3.0478 cm, about 3.05 cm."),
        (5, "A beaker has radius 6 cm and volume 3,242 cm³. Find its height.", "h=V/(πr²)=3,242/(3.14×36)≈28.6801 cm."),
        (6, "A cylinder has height 7.2 cm and volume 4,321 cm³. Find its radius.", "r=√(V/(πh))=√(4,321/(3.14×7.2))≈13.8249 cm."),
        (7, "A hollow iron pipe has internal radius 7.5 cm, external radius 10.2 cm, and length 0.35 m. Find the volume of iron used.", "Convert length to 35 cm. Iron volume=πh(R²−r²)=3.14(35)(10.2²−7.5²)=5,252.121 cm³."),
        (8, "A cylindrical pipe is 12.3 cm long and has diameter 12 cm. Find its surface area.", "For the open-ended pipe, use curved area πdh=3.14(12)(12.3)=463.464 cm²."),
        (9, "A cylindrical pool has diameter 11 m and height 3 m. Find its capacity.", "r=5.5 m. V=3.14(5.5²)(3)=284.955 m³, or 284,955 litres."),
        (10, "An oil tank is 24 m high with radius 12.6 m. Oil fills it to a height of 24−9.5 m. Find the oil volume.", "Oil height=14.5 m. V=3.14(12.6²)(14.5)=7,228.3428 m³."),
        (11, "A drum has radius 7.1 m and volume 1,111 m³. Find its height.", "h=1,111/(3.14×7.1²)≈7.0189 m."),
        (12, "A cylindrical tower has radius 23 m and height 65 m. Find the cost to paint its curved wall at Rs 432/m².", "Curved area=2πrh=2(3.14)(23)(65)=9,388.6 m². Cost=9,388.6×432=Rs 4,055,875.20."),
        (13, "Paint the outside curved walls of four cylindrical warehouses, each 17.3 m in diameter and 25 m high, at Rs 450/m². Find the total cost.", "Total curved area=4πdh=4(3.14)(17.3)(25)=5,432.2 m². Cost=5,432.2×450=Rs 2,444,490."),
        (14, "Find the volume and total surface area of a cylinder with radius 6 cm and height 29 cm.", "V=3.14(6²)(29)=3,278.16 cm³. TSA=2πr(r+h)=2(3.14)(6)(35)=1,318.8 cm²."),
        (15, "Each of eight cylindrical mosque pillars has circumference 15 m and height 18 m. Find the cost of filling them with cement at Rs 745/m³.", "r=C/(2π)=15/6.28≈2.38854 m. Volume per pillar=πr²h≈322.45223 m³. Eight pillars hold ≈2,579.61783 m³; cost≈Rs 1,921,815.29."),
    ])
    replace_exercise(9, "Exercise 9.6", [
        (1, "Find the surface area of each prism.\na) rectangular prism 9 m×3 m×13 m\nb) rectangular prism 20 cm×6 cm×4 cm\nc) cube, side 4 cm\nd) triangular prism: right-triangle sides 1.5 m, 2 m, 2.5 m; length 10 m\ne) triangular prism: triangle base 13 cm, altitude 6 cm, side lengths 8 cm, 10 cm, 13 cm; length 14 cm\nf) triangular prism: base 12 m, altitude 11 m, side lengths 7.4 m, 13 m, 12 m; length 7 m",
         "For a cuboid use 2(lw+lh+wh); for a triangular prism use 2(area of base)+(base perimeter)(length).\na) 2(9×3+9×13+3×13)=366 m².\nb) 2(20×6+20×4+6×4)=448 cm².\nc) 6(4²)=96 cm².\nd) Two triangle areas=2(½×1.5×2)=3; lateral area=(1.5+2+2.5)×10=60; total=63 m².\ne) Two triangle areas=2(½×13×6)=78; lateral area=(8+10+13)×14=434; total=512 cm².\nf) Two triangle areas=2(½×12×11)=132; lateral area=(7.4+13+12)×7=226.8; total=358.8 m²."),
        (2, "Find the volume of each prism.\na) cuboid 7 cm×12 cm×2 cm\nb) cuboid 6 m×4 m×11 m\nc) triangular prism: triangle base 13 cm, altitude 10 cm, length 12 cm\nd) triangular prism: triangle base 10 m, altitude 13 m, length 17 m\ne) triangular prism: triangle base 7 cm, altitude 6 cm, length 15 cm",
         "Volume=base area×prism length.\na) 7×12×2=168 cm³.\nb) 6×4×11=264 m³.\nc) (½×13×10)×12=780 cm³.\nd) (½×10×13)×17=1,105 m³.\ne) (½×7×6)×15=315 cm³."),
    ])
    replace_exercise(9, "Exercise 9.7", [
        (1, "Find the total surface area of a box with length 8 cm, breadth 6 cm and height 5 cm.", "TSA=2(lw+lh+wh)=2(48+40+30)=236 cm²."),
        (2, "Find the tin sheet area and cost for a tin box measuring 40 cm×15 cm×35 cm, at Rs 1.25/cm².", "Assuming a closed box, TSA=2(40×15+40×35+15×35)=5,050 cm². Cost=5,050×1.25=Rs 6,312.50."),
        (3, "A pool is 35 m long, 15 m wide and 1.5 m deep. Find the cost of cementing its walls at Rs 45/m².", "The four inside walls have area 2(35×1.5)+2(15×1.5)=150 m². Cost=150×45=Rs 6,750."),
        (4, "A triangular camping tent is 4.5 m long and its triangular face area is 20 m². Find its volume.", "V=base cross-sectional area×length=20×4.5=90 m³."),
        (5, "A triangular-prism candy jar is 7 cm long. Its triangular base has side lengths 4 cm, 5 cm and 3 cm; find its total surface area.", "The base is a 3–4–5 right triangle, so its area is ½(3)(4)=6 cm² and perimeter=12 cm. TSA=2(6)+12(7)=96 cm²."),
    ])
    replace_exercise(9, "Review Exercise", [
        (1, "Choose the correct option.\na) The total boundary length of a circle is its circumference / volume / base / diameter.\nb) The symbol for pi.\nc) π is approximately 2.12 / 3.12 / 3.11 / 3.14.\nd) Formula for circumference.\ne) Formula for area of a circle.\nf) Formula for total surface area of a cylinder.\ng) Formula for volume of a cylinder.", "a) Circumference. b) π. c) 3.14. d) C=2πr (equivalently πd). e) A=πr². f) TSA=2πr(r+h). g) V=πr²h."),
        (2, "Find the area and circumference of each circle.\na) r=3.3 cm\nb) r=4.3 cm\nc) r=9.3 cm\nd) r=5.8 cm\ne) r=11.9 cm\nf) r=23.3 cm", "Use A=3.14r² and C=6.28r.\na) A=34.1946 cm², C=20.724 cm.\nb) A=58.0586 cm², C=27.004 cm.\nc) A=271.5786 cm², C=58.404 cm.\nd) A=105.6296 cm², C=36.424 cm.\ne) A=444.6554 cm², C=74.732 cm.\nf) A=1,704.6746 cm², C=146.324 cm."),
        (3, "Find the total surface area and volume of each cylinder.\na) r=3.3 cm, h=13 cm\nb) r=9.3 cm, h=20 cm\nc) r=4.2 cm, h=12 cm\nd) r=5.3 cm, h=9 cm", "Use TSA=2πr(r+h), V=πr²h, π=3.14.\na) TSA=337.8012 cm²; V=444.5298 cm³.\nb) TSA=1,711.2372 cm²; V=5,431.572 cm³.\nc) TSA=427.2912 cm²; V=664.6752 cm³.\nd) TSA=475.9612 cm²; V=793.8234 cm³."),
        (4, "A circular ground has radius 78.3 m. Find the fencing cost at Rs 112 per metre.", "Circumference=2πr=2(3.14)(78.3)=491.724 m. Cost=491.724×112=Rs 55,073.088 (≈Rs 55,073.09)."),
        (5, "Find the total surface area of a cylinder with radius 5 cm and height 34 cm.", "TSA=2πr(r+h)=2(3.14)(5)(39)=1,224.6 cm²."),
        (6, "A cylindrical decoration is 34 cm long and has diameter 19 cm. Find the steel sheet area required.", "For a closed cylinder, r=9.5 cm. TSA=2πr(r+h)=2(3.14)(9.5)(43.5)=2,595.21 cm²."),
        (7, "A room is 4.5 m long, 3.5 m wide and 3 m high. Find cementing cost for its walls and floor at Rs 28/m².", "Four walls area=2h(l+w)=2(3)(4.5+3.5)=48 m². Floor=4.5×3.5=15.75 m². Total=63.75 m²; cost=63.75×28=Rs 1,785."),
        (8, "Math Project: Roll two dice, draw a rectangle with those side lengths on a square grid, and compare areas.", "For a sample roll of 4 and 2, draw a 4×2 rectangle. Area=4×2=8 square units; perimeter=2(4+2)=12 units. Repeat for each roll and compare areas."),
    ])
    replace_exercise(10, "Exercise 10.1", [
        (1, "Convert.\na) 3 m to cm\nb) 893 cm to m and cm\nc) 56 m 8 cm to cm\nd) 10 km to m\ne) 101 cm to m and cm\nf) 18 km 550 m to km\ng) 50 cm to mm", "Use 1 km=1,000 m, 1 m=100 cm, and 1 cm=10 mm. a) 300 cm. b) 8 m 93 cm. c) 5,608 cm. d) 10,000 m. e) 1 m 1 cm. f) 18.55 km. g) 500 mm."),
    ])
    replace_exercise(10, "Exercise 10.2", [
        (1, "Express these times in the 24-hour clock format: a) 7:45 a.m. and 7:45 p.m.; b) 12:00 a.m. and 12:00 p.m.; c) 4:15 a.m. and 4:15 p.m.; d) 5:22 a.m. and 5:22 p.m.", "a) 07:45, 19:45. b) 00:00, 12:00. c) 04:15, 16:15. d) 05:22, 17:22."),
        (2, "Write in the 12-hour clock format.\na) 03:50\nb) 00:41\nc) 16:56\nd) 22:18", "a) 3:50 a.m. b) 12:41 a.m. c) 4:56 p.m. d) 10:18 p.m."),
        (3, "Convert from 24-hour to 12-hour clock.\na) 01:30\nb) 15:32\nc) 09:45\nd) 00:10", "a) 1:30 a.m. b) 3:32 p.m. c) 9:45 a.m. d) 12:10 a.m."),
        (4, "Convert from 12-hour to 24-hour clock.\na) 06:05 a.m.\nb) 05:32 a.m.\nc) 01:45 p.m.\nd) 12:59 a.m.", "a) 06:05. b) 05:32. c) 13:45. d) 00:59."),
        (5, "Convert.\na) 2 hours 25 minutes to minutes\nb) 365 minutes to hours and minutes\nc) 19 minutes 25 seconds to seconds\nd) 2 hours 20 minutes to minutes\ne) 465 minutes to minutes and seconds\nf) 3,000 seconds to minutes and seconds", "a) 2×60+25=145 min. b) 365=6×60+5=6 h 5 min. c) 19×60+25=1,165 s. d) 2×60+20=140 min. e) 465 min 0 s. f) 3,000÷60=50 min 0 s."),
        (6, "Convert km/h to m/s.\na) 65\nb) 123\nc) 72\nd) 128\ne) 323\nf) 1,221", "Multiply by 5/18. a) 18.0556 m/s. b) 34.1667 m/s. c) 20 m/s. d) 35.5556 m/s. e) 89.7222 m/s. f) 339.1667 m/s."),
        (7, "Convert m/s to km/h.\na) 23\nb) 12\nc) 7\nd) 17\ne) 35\nf) 3", "Multiply by 3.6. a) 82.8 km/h. b) 43.2 km/h. c) 25.2 km/h. d) 61.2 km/h. e) 126 km/h. f) 10.8 km/h."),
        (8, "Convert m/h to cm/s.\na) 670\nb) 590\nc) 499\nd) 184", "Multiply m/h by 100/3,600. a) 18.6111 cm/s. b) 16.3889 cm/s. c) 13.8611 cm/s. d) 5.1111 cm/s."),
        (9, "Convert cm/s to m/h.\na) 199\nb) 345\nc) 21\nd) 99", "Multiply by 36. a) 7,164 m/h. b) 12,420 m/h. c) 756 m/h. d) 3,564 m/h."),
    ])
    replace_exercise(10, "Exercise 10.3", [
        (1, "A bus leaves Lahore at 10:25 and reaches Islamabad at 14:40. How long is the journey?", "14:40−10:25=4 hours 15 minutes."),
        (2, "Taaiba reaches the Allama Iqbal Museum at 10:45 a.m. and spends 3 hours 40 minutes there. When does she leave?", "10:45 a.m.+3 h 40 min=2:25 p.m."),
        (3, "Complete the departure/arrival/journey table: (a) departs 1:01 a.m., journey 5 h 15 min; (b) arrives 7:20 p.m., journey 11 h 2 min; (c) departs 8:55 p.m., arrives 6:20 a.m.; (d) departs 10:40 a.m., journey 5 h 50 min.", "a) Arrival 6:16 a.m. b) Departure 8:18 a.m. c) Journey 9 h 25 min (overnight). d) Arrival 4:30 p.m."),
        (4, "A Multan–Karachi journey takes 10 h 45 min. Asad leaves at 6:54 a.m. When does he arrive?", "6:54 a.m.+10 h 45 min=5:39 p.m."),
        (5, "Rabia leaves at 4:25 a.m. Monday and reaches at 7:20 p.m. Tuesday. How long is the journey?", "From Monday 4:25 a.m. to Tuesday 4:25 a.m. is 24 h; to 7:20 p.m. adds 14 h 55 min. Total=38 h 55 min."),
        (6, "Ahmad arrives in Murree at 7:28 a.m. after a 6 h 49 min journey from Lahore. Find his departure time.", "7:28 a.m.−6 h 49 min=12:39 a.m."),
    ])
    replace_exercise(10, "Exercise 10.4", [
        (1, "Rizwan travels 125 km in 2 hours on his bike. Find his average speed.", "Average speed=125÷2=62.5 km/h."),
        (2, "Hadia travels 640 km by car in 8 hours. Find her average speed.", "640÷8=80 km/h."),
        (3, "A total distance of 12 km is covered in 7 hours. Find the average speed.", "12÷7≈1.7143 km/h."),
        (4, "A train travels at 200 km/h for 3 hours, then 150 km/h for 5 hours. Find its average speed.", "Total distance=200×3+150×5=1,350 km; total time=8 h. Average=1,350÷8=168.75 km/h."),
        (5, "A car travels at 109 km/h for 5 hours and 100 km/h for 2 hours. Find its average speed.", "Distance=109×5+100×2=745 km; time=7 h. Average=745÷7≈106.4286 km/h."),
    ])
    replace_exercise(10, "Exercise 10.5", [
        (1, "A plane travels 535,760 m in 8,500 s. Find its speed in m/s and km/h.", "Speed=535,760÷8,500≈63.0306 m/s. Convert: 63.0306×3.6≈226.91 km/h."),
        (2, "Afnan rides 6 km to school in 35 minutes. Find the speed in km/h.", "35 min=35/60 h. Speed=6÷(35/60)=72/7≈10.2857 km/h."),
        (3, "How long does a bus take to travel 1,520 km at 100 km/h?", "Time=1,520÷100=15.2 h=15 h 12 min."),
        (4, "A car travels at 8,250 m/s. How far does it travel in 2 hours?", "2 h=7,200 s. Distance=8,250×7,200=59,400,000 m=59,400 km."),
        (5, "A train leaves at 1:00 p.m. and arrives at 6:00 p.m. The stations are 432 km apart. Find its speed.", "Time=5 h. Speed=432÷5=86.4 km/h."),
        (6, "Amir walks 5 km in 3 hours. How far can he travel in 30 minutes at the same speed?", "Speed=5/3 km/h. In 0.5 h, distance=(5/3)(0.5)=5/6≈0.8333 km."),
        (7, "A tourist climbs a 45 m hill in 15 minutes. How long to climb a 90 m hill at the same rate?", "90 m is twice as high as 45 m, so time=2×15=30 minutes."),
        (8, "A bus travels 312 km in 4 hours. How far will it travel in 8 hours at the same speed?", "Speed=312÷4=78 km/h. Distance=78×8=624 km."),
        (9, "A truck covers a distance in 12 hours at 102 km/h. How long for the same distance at 96 km/h?", "Distance=102×12=1,224 km. Time=1,224÷96=12.75 h=12 h 45 min."),
    ])
    replace_exercise(10, "Review Exercise", [
        (1, "Choose the correct option.\na) Minutes in 5 hours: 360,180,240,300.\nb) Metres in 500 cm: 5,50,500,5000.\nc) To convert km/h to m/h, multiply by: 100,10,1000,1.\nd) Equal distances covered in equal times is: distance, uniform speed, average speed, time.\ne) This item is not visible in the supplied scan.\nf) The duration in which things happen is: time, speed, distance, proportion.\ng) Speed equals: distance/time, time/distance, distance×time, time×time.", "a) 300 minutes. b) 5 metres. c) 1,000. d) Uniform speed. f) Time. g) Distance÷time. The scanned review jumps from d to f, so item e is absent from the source images."),
        (2, "Convert distances.\na) 8 m to cm\nb) 5 km 70 m to m\nc) 110 cm to mm\nd) 50 m 6 cm to cm\ne) 44 km to m\nf) 3 m 15 cm to cm\ng) 56,000 m to km\nh) 96,314 m to km and m\ni) 99 mm to cm and mm", "a) 800 cm. b) 5,070 m. c) 1,100 mm. d) 5,006 cm. e) 44,000 m. f) 315 cm. g) 56 km. h) 96 km 314 m. i) 9 cm 9 mm."),
        (3, "Convert times.\na) 2 h 25 min to minutes\nb) 255 min to hours and minutes\nc) 880 s to minutes and seconds\nd) 360 min to hours", "a) 145 min. b) 4 h 15 min. c) 14 min 40 s. d) 6 h."),
        (4, "Convert speeds.\na) 849 m/h to km/h\nb) 450 m/h to cm/s\nd) 124 cm/s to m/h", "a) 0.849 km/h. b) 450×100/3,600=12.5 cm/s. d) 124×36=4,464 m/h."),
        (5, "Amir leaves City A at 11:57 a.m. and reaches City B at 1:22 p.m. Find the journey time.", "From 11:57 to 12:57 is 1 hour; to 1:22 adds 25 minutes. Total=1 h 25 min."),
        (6, "A bus travels 560 km in 10 hours. Find its average speed.", "Average speed=560÷10=56 km/h."),
        (7, "Think Higher: Divide the listed distances into two groups with equal total length, using all values: 3.1 km, 7,400 m, 0.3 km, 3.3 km, 800 m, 270,000 cm, 2,410,000 cm, 200 m and 6,100 m. Also find the midpoint between 565.62 m and 5.62 cm.", "The listed lengths total 48,000 m, so each equal group would need 24,000 m. However, 2,410,000 cm=24,100 m, while all the other lengths total 23,900 m; no equal partition is possible as printed. This is a source-data inconsistency. Midpoint: convert 5.62 cm=0.0562 m; (565.62+0.0562)/2=282.8381 m=282 m 83.81 cm."),
        (8, "Math Project: Make pairs of 12-hour and 24-hour time cards; match the equivalent times and score each correct match.", "Example pairs: 12:00 a.m.↔00:00; 7:45 a.m.↔07:45; 1:22 p.m.↔13:22; 6:00 p.m.↔18:00. A complete matched set earns a point as the project describes."),
    ])
    replace_exercise(11, "Exercise 11.1", [
        (1, "Draw and describe properties of: a) square b) rectangle c) parallelogram d) rhombus e) trapezium f) kite. Include parallel/equal sides, equal/right angles and symmetry.",
         "a) Square: 4 equal sides, 4 right angles, two pairs of parallel opposite sides, 4 symmetry axes (two medians and two diagonals). The book text says 6 axes, but that is incorrect.\nb) Rectangle: opposite sides equal and parallel, 4 right angles, 2 symmetry axes.\nc) Parallelogram: opposite sides equal and parallel; opposite angles equal; adjacent angles sum to 180°; generally no symmetry axis.\nd) Rhombus: 4 equal sides, opposite sides parallel, opposite angles equal, adjacent angles supplementary; 2 diagonal symmetry axes.\ne) Trapezium: one pair of opposite sides parallel; same-side interior angles on each leg sum to 180°. Isosceles trapezium has one symmetry axis.\nf) Kite: two pairs of adjacent equal sides; one pair of opposite angles equal; one symmetry axis."),
        (2, "Name the five illustrated quadrilaterals.", "Left to right: rhombus, kite, trapezium, parallelogram, right trapezium."),
        (3, "Find the marked angles in each parallelogram.\na) one angle 78°, opposite angle a\nb) upper-right angle110°, adjacent lower-right angle b\nc) lower-left angle85°, opposite upper-right angle c and adjacent lower-right angle d\nd) one angle 125°, marked angles e, f, g",
         "Opposite parallelogram angles are equal; adjacent angles sum to 180°.\na) a=78°. b) b=180°−110°=70°. c) c=85° (opposite angles); d=180°−85°=95°. d) f=125° (opposite the 125° angle); e=g=55° (adjacent)."),
        (4, "Find the marked angles in each rhombus.\na) one angle 65°, opposite marked angle\nb) one angle 118°, adjacent marked angle b\nc) one angle 60°, marked adjacent c and opposite d\nd) top angle 15°, find e, f, g",
         "A rhombus has opposite angles equal and adjacent angles supplementary.\na) 65°. b) b=62°. c) c=120°, d=60°. d) e=165°, f=15°, g=165°."),
        (5, "Find the marked angles in each trapezium.\na) parallel vertical sides and a right angle at the lower right; find a\nb) parallel horizontal bases, lower-right angle 22°, find b\nc) parallel bases, upper-left 105°, lower-right 18°, find c and d",
         "Consecutive interior angles on a transversal between parallel sides are supplementary.\na) a=90°. b) b=180°−22°=158°. c) c=180°−105°=75°; d=180°−18°=162°."),
        (6, "Find the unknown angles in each kite.\na) angles 53° and 135° are shown\nb) angles B=104° and D=40° are shown\nc) P=50°, Q=122°, and a right-angle marker at R are printed; find S and examine the kite description",
         "a) The equal opposite angles are at X and V, so X=135°. The four angles total360°, hence U=360°−135°−135°−53°=37°.\nb) E=C because they are the equal opposite angles; each=(360°−104°−40°)/2=108°.\nc) Taking the printed right-angle marker literally gives R=90° and S=360°−50°−122°−90°=98°. This conflicts with the claimed kite geometry: for the shown kite orientation, S should equal Q=122°, which would instead require R=360°−50°−122°−122°=66°. Thus the printed right-angle marker and the kite description cannot both hold. The two interpretations are stated explicitly rather than changing the given50° angle."),
        (7, "Draw lines of symmetry for each pictured quadrilateral, if any: rhombus, ordinary trapezium, isosceles trapezium, parallelogram and kite.", "a) Rhombus: both diagonals (2 lines). b) Non-isosceles trapezium: none. c) Isosceles trapezium: one perpendicular bisector of the parallel sides. d) Parallelogram: none. e) Kite: one diagonal through the vertices where equal sides meet."),
    ])
    replace_exercise(11, "Exercise 11.2", [
        (1, "Identify the regular and irregular polygons in the two rows of figures, and justify.", "A regular polygon has all sides and all interior angles equal. In the scan, the regular figures are the equilateral triangle, regular octagon, regular hexagon, square, regular hexagon, regular pentagon and rotated square (diamond). The remaining figures are irregular because their side lengths/angles are unequal or they are concave."),
        (2, "Draw an irregular polygon that has an odd number of sides.", "Example: draw a non-regular pentagon (five unequal sides and/or angles)."),
        (3, "Draw a regular polygon that has an even number of sides.", "Example: draw a regular hexagon with six equal sides and equal angles."),
        (4, "Draw a concave polygon with 5 sides.", "Draw a five-sided polygon with one vertex pushed inward so one interior angle is reflex (>180°)."),
    ])
    replace_exercise(11, "Exercise 11.3", [
        (1, "Find the sum of interior angles of the four pictured polygons by counting triangles.", "Counting boundary segments from left to right gives7,8,9 and10 sides. Draw diagonals from one vertex to the non-adjacent vertices: a) heptagon→5 triangles→5×180°=900°; b) octagon→6 triangles→1080°; c) nonagon→7 triangles→1260°; d) decagon→8 triangles→1440°. In each case the triangle count is n−2."),
        (2, "Complete the interior-angle-sum table for polygons with 6, 9, 11, 15, 20 and 18 sides.", "Use S=180°(n−2). n=6:720°. n=9:1,260°. n=11:1,620°. n=15:2,340°. n=20:3,240°. n=18:2,880°."),
        (3, "Find each interior angle of a regular polygon with: a) 5 sides b) 6 sides c) 8 sides d) 10 sides e) 13 sides f) 20 sides.", "Each angle=180°(n−2)/n. a)108°. b)120°. c)135°. d)144°. e)1,980/13≈152.3077°. f)162°."),
        (4, "Find the missing marked angles.\na) Triangle has angles x, 3x, and exterior angle 160° at its third vertex.\nb) Triangle has interior angles y, 92° and 41°, with exterior angle x adjacent to 92°.", "a) Interior angle at the third vertex=180−160=20°. Then x+3x+20=180, so x=40° and 3x=120°. b) x=180−92=88°; y=180−92−41=47°."),
        (5, "Find an exterior angle of a regular 8-sided polygon.", "360°/8=45°."),
        (6, "Find an interior angle of a regular 6-sided polygon.", "180°(6−2)/6=120°."),
        (7, "Find an exterior angle of a regular 9-sided polygon.", "360°/9=40°."),
        (8, "Find an interior angle of a regular 11-sided polygon.", "180°(11−2)/11=1,620°/11≈147.2727°."),
        (9, "Four interior angles of a pentagon are 115°, 92°, 107° and 83°. Find the fifth.", "Pentagon sum=540°. Fifth=540−(115+92+107+83)=143°."),
        (10, "Find the unknown angles.\na) Heptagon angles129°,116°,120°,y,125°,135° and130°.\nb) Pentagon angles 105°,117°,100°,115° and x.\nc) Hexagon angles 135°,62°,151°,140°, (n+6)° and n°.\nd) Pentagon ABCDE has E=B=115°,C=D=90°; find angle A.\ne) Hexagon angles 120°,90°,110°,160°,130° and x.", "Use the interior sum 180°(n−2). a) y=900−(129+116+120+125+135+130)=145°. b) x=540−(105+117+100+115)=103°. c) (n+6)+n=720−488=232, so n=113° and n+6=119°. d) Pentagon sum=540°; A=540°−(115°+115°+90°+90°)=130°. e) Hexagon sum=720°; x=720°−(120°+90°+110°+160°+130°)=110°."),
    ])
    replace_exercise(11, "Exercise 11.4", [
        (1, "Label the circle parts in each diagram.", "a) O is the centre; AB is a diameter; OA, OB and OC are radii; PQ is a chord; the short arc PQ is a minor arc; the region between chord PQ and arc PQ is a segment. b) AB and CD are chords; any chord through O is a diameter; O is the centre. Label the smaller arc minor and the larger arc major."),
        (2, "Draw a circle of radius 5 cm and label all its parts.", "With a compass set to 5 cm, draw the circle. Mark centre O, a radius of 5 cm, a diameter of 10 cm, a chord, a minor and major arc, a semicircle, and a segment bounded by a chord and its arc."),
        (3, "Draw a circle with three radii.", "Mark centre O and draw three line segments from O to distinct points on the circumference; each is a radius."),
        (4, "Draw a circle of 6 cm and divide it into two semicircles.", "Draw a 6 cm diameter through the centre. It divides the circle into two equal semicircles; each has radius 3 cm."),
    ])
    replace_exercise(11, "Review Exercise", [
        (1, "Choose the correct option.\na) Longest chord: radius/segment/diameter/sectors.\nb) A circle is a set of: points/lines/segments/sectors.\nc) Angle in a semicircle: right/obtuse/acute/straight.\nd) Which has no line of symmetry: square/rectangle/rhombus/parallelogram?\ne) Which has only one pair of parallel sides?\nf) A polygon with no interior reflex angle is called what?", "a) Diameter. b) Points. c) Right angle. d) An ordinary parallelogram (option iv) has no line of symmetry. e) Trapezium (option i). f) Convex polygon (option ii): none of its interior angles is reflex."),
        (2, "Explain the difference between convex and concave polygons.", "A convex polygon has no interior angle greater than 180° and all vertices point outward. A concave polygon has at least one reflex interior angle (>180°) and at least one vertex pointing inward."),
        (3, "Draw a circle and label/define its centre, radius, diameter, chord, arcs, semicircle and segment.", "Centre: fixed point equidistant from the circumference. Radius: centre to circumference. Diameter: chord through the centre, twice the radius. Chord: segment joining circumference points. Arc: part of circumference; a semicircle is half the circle formed by a diameter. Segment: region bounded by a chord and its arc."),
        (4, "Describe properties of a square, rectangle, parallelogram, rhombus, trapezium and kite.", "Square: four equal sides and right angles. Rectangle: opposite sides equal/parallel and four right angles. Parallelogram: opposite sides equal/parallel and opposite angles equal. Rhombus: four equal sides, opposite sides parallel and opposite angles equal. Trapezium: one pair of opposite sides parallel. Kite: two pairs of adjacent equal sides and one pair of opposite equal angles."),
        (5, "Use the figures.\na) ABCD is a rhombus with AB=10 cm; find remaining side lengths and angle relations x,y,z,w.\nb) PQRS is a parallelogram; find angle sums and equal opposite angles.\nc) ABCD is a trapezium; find angle sums and its parallel sides.", "a) All four sides are 10 cm. Opposite angles are equal: x=z and y=w; adjacent angles are supplementary, so x+y=180°. Therefore x+z=2x and w+x=180°; no individual angle value is determined without an angle measurement. b) m+n+o+l=360°; opposite angles m=o and l=n. c) z+y=180°, w+x=180°, x+y+z+w=360°, and AB∥DC."),
        (6, "Classify each pictured polygon as regular/irregular and convex/concave.", "a) Regular convex equilateral triangle. b) Irregular concave. c) Regular convex square. d) Irregular concave. e) Irregular convex. f) Regular convex hexagon."),
        (7, "Draw an irregular polygon with an even number of sides.", "Example: an irregular hexagon with six unequal sides and/or angles."),
        (8, "Draw a regular polygon with an odd number of sides.", "Example: a regular pentagon."),
        (9, "Draw a concave polygon with five sides.", "Draw a concave pentagon with one vertex indented so one angle is reflex."),
        (10, "Draw a convex polygon with nine sides.", "Draw a nonagon with all vertices pointing outward and no reflex interior angles."),
        (11, "Find each interior angle of regular polygons with: a) 5 sides b) 10 sides c) 7 sides.", "a)108°. b)144°. c)900°/7≈128.5714°. Use 180°(n−2)/n."),
        (12, "Describe: a) an exterior angle of a triangle and its two opposite interior angles; b) interior and exterior angles of a polygon.", "a) A triangle's exterior angle equals the sum of its two opposite interior angles. b) An interior angle and adjacent exterior angle sum to 180°; one exterior angle at each vertex sums to 360° for any polygon."),
        (13, "Find interior-angle sums for polygons with: a) 5 sides b) 3 sides c) 7 sides d) 4 sides e) 8 sides.", "a)540°. b)180°. c)900°. d)360°. e)1,080°. Formula: 180°(n−2)."),
        (14, "Find an exterior angle of a regular 4-sided polygon.", "360°/4=90°."),
        (15, "Find an interior angle of a regular 5-sided polygon.", "180°(5−2)/5=108°."),
        (16, "Find an exterior angle of a regular 6-sided polygon.", "360°/6=60°."),
        (17, "Find an interior angle of a regular 8-sided polygon.", "180°(8−2)/8=135°."),
        (18, "Draw a circle and two chords that do not pass through its centre.", "Draw two segments joining circumference points away from the centre; neither is a diameter."),
        (19, "Draw a circle with radius 7 cm and two segments.", "Draw the circle with a 7 cm compass setting. Draw two chords and shade the regions between each chord and its smaller arc; these are segments."),
        (20, "Math Project: Compare randomly selected quadrilaterals and record their similarities/differences.", "Example: square and rectangle both have four right angles and opposite sides parallel; only the square has all sides equal. Rhombus and square have four equal sides; only the square must have right angles. Trapezium has one pair of parallel sides; parallelogram has two. A kite has two pairs of adjacent equal sides."),
    ])
    replace_exercise(12, "Exercise 12.1", [
        (1, "Draw the line(s) of symmetry for each illustrated shape.", "Use the mirror axes shown by the shapes: block D has one horizontal axis; the T-like figure has one vertical axis; the isosceles trapezium has one vertical axis; block C has one horizontal axis; U has one vertical axis; the regular hexagon has six axes."),
        (2, "Decide whether each dotted line is a line of symmetry; then identify which figures have a line of symmetry.", "a) B with a vertical line: no. b) N with a vertical line: no. c) E with a horizontal line: yes. d) I with a horizontal line: yes. e) The offset step shape: no. f) Oval with a vertical line: yes. Thus c,d,f are symmetric about their shown dotted lines."),
        (3, "Write the rotational-symmetry order of each shape.", "a) Plus sign: order 4. b) Hourglass shape: order 2. c) L shape: order 1. d) Opposing matching buses: order 2."),
        (4, "Rotate the given images about the origin. a) Rotate the triangle with vertices (1,1),(1,5),(5,1) through180° counterclockwise. b) Rotate the pentagon with vertices (1,−1),(5,−1),(5,−4),(3,−5),(1,−4) through90° clockwise.", "a) A half-turn about the origin changes the sign of both coordinates: (x,y)→(−x,−y). Thus (1,1)→(−1,−1), (1,5)→(−1,−5), (5,1)→(−5,−1). Plot and join the three image vertices.\nb) For90° clockwise use (x,y)→(y,−x). The five mappings, in vertex order, are (1,−1)→(−1,−1); (5,−1)→(−1,−5); (5,−4)→(−4,−5); (3,−5)→(−5,−3); (1,−4)→(−4,−1). Plot and join the five image points, closing the pentagon. Both images have the same lengths and angles as the original shapes."),
        (5, "Draw a triangle on the coordinate plane and rotate it 270° clockwise about the origin.", "Sample: triangle P(1,1), Q(4,1), R(2,3). A 270° clockwise turn is 90° counterclockwise, (x,y)→(−y,x). Image: P′(−1,1), Q′(−1,4), R′(−3,2)."),
        (6, "Draw a trapezium on a coordinate plane and rotate it 90° clockwise about the origin.", "Sample trapezium vertices (1,1),(5,1),(4,3),(2,3). Apply (x,y)→(y,−x): image vertices (1,−1),(1,−5),(3,−4),(3,−2)."),
        (7, "Find the rotated coordinates of P(−6,−4): a) 90° clockwise b) 180° counterclockwise c) 270° clockwise.", "a) (−4,6). b) (6,4). c) (4,−6)."),
        (8, "Find the rotated coordinates of P(3,9): a) 90° counterclockwise b) 180° clockwise c) 270° counterclockwise.", "a) (−9,3). b) (−3,−9). c) (9,−3)."),
    ])
    replace_exercise(12, "Exercise 12.3", [
        (1, "Translate each figure and write its image coordinates. Vertices are listed around each boundary. a) Move by (-2,-4); original vertices: (-8,3), (-3,3), (-8,8). b) Move by (3,1); original vertices: (-9,9), (-4,9), (-4,5), (-3,5), (-3,4), (-5,4), (-5,3), (-6,3), (-6,4), (-9,4). c) Move by (4,3); original vertices: (6,-2), (10,-6), (6,-10), (2,-6). d) Move by (2,-2); original vertices: (2,2), (9,2), (9,5), (5,5), (5,9), (2,9). ", "Add the given horizontal and vertical displacement to every vertex. Preserve vertex order when joining the image points.\na) (-8,3)→(-10,-1); (-3,3)→(-5,-1); (-8,8)→(-10,4).\nb) (-9,9)→(-6,10); (-4,9)→(-1,10); (-4,5)→(-1,6); (-3,5)→(0,6); (-3,4)→(0,5); (-5,4)→(-2,5); (-5,3)→(-2,4); (-6,3)→(-3,4); (-6,4)→(-3,5); (-9,4)→(-6,5).\nc) (6,-2)→(10,1); (10,-6)→(14,-3); (6,-10)→(10,-7); (2,-6)→(6,-3).\nd) (2,2)→(4,0); (9,2)→(11,0); (9,5)→(11,3); (5,5)→(7,3); (5,9)→(7,7); (2,9)→(4,7).\n"),
        (2, "Name the images and describe each translation; the lighter figure is the image. a) Parallelogram EFGH to E′F′G′H′: E(−10,−2), F(−7,−2), G(−9,1), H(−6,1); E′(6,−2), F′(9,−2), G′(7,1), H′(10,1). b) Triangle ABC to A′B′C′: A(−2,4), B(−9,1), C(−7,6); A′(8,2), B′(4,−5), C′(3,0).", "a) The figures are parallelograms. Each x-coordinate increases by16 and each y-coordinate remains unchanged. For example E:6−(−10)=16, −2−(−2)=0; G:7−(−9)=16,1−1=0. Thus the translation is16 units right, (x,y)→(x+16,y). Join vertices around the boundary E,F,H,G.\nb) The figures are triangles, but the printed coordinates do not describe one translation. A→A′ gives displacement (10,−2); B→B′ gives (13,−6); C→C′ gives (10,−6). A translation requires the same displacement for every corresponding vertex. Therefore no single translation maps the printed triangle ABC to the printed A′B′C′; the diagram needs correction before a unique translation can be given."),
    ])
    replace_exercise(12, "Exercise 12.4", [
        (1, "Construct an equilateral triangle ABC with AB=BC=AC=3.8 cm.", "Draw AB=3.8 cm. With compass radius3.8 cm, draw arcs centered at A and B; their intersection is C. Join AC and BC. Each angle is 60°."),
        (2, "Construct an isosceles triangle PQR with PQ=8 cm and QR=PR=4.5 cm.", "Draw base PQ=8 cm. Draw 4.5 cm radius arcs centered at P and Q; their intersection is R. Join PR and QR. The base is 8 cm and both equal sides are 4.5 cm."),
        (3, "Construct a scalene triangle ABC with AB=3 cm, BC=6 cm and AC=2.5 cm.", "No such triangle can be constructed: 3+2.5=5.5 cm<6 cm, violating the triangle inequality. The printed measurements are inconsistent."),
        (4, "Construct equilateral triangle RST with ∠RST=∠STR=60° and ST=4.5 cm.", "Draw ST=4.5 cm. Construct 60° rays at S and T on the same side of ST. Their intersection is R; join the sides. All sides are 4.5 cm."),
        (5, "Construct scalene triangle DEF with ∠DEF=35°, ∠EDF=55° and DE=5 cm.", "Third angle F=180−35−55=90°. Draw DE=5 cm, construct 35° at E and 55° at D; the rays meet at F. The three angles are distinct, so it is scalene and right-angled."),
        (6, "Construct right triangle ABC with ∠ABC=90°, AB=7 cm and BC=3.2 cm.", "Draw AB=7 cm and a perpendicular at B. Mark C 3.2 cm from B on that ray; join A to C. AC=√(7²+3.2²)=√59.24≈7.6968 cm."),
        (7, "Construct acute triangle PQR with ∠PRQ=65°, PR=4.7 cm and QR=5.2 cm.", "Draw PR=4.7 cm. At R construct 65°; mark Q on its ray so RQ=5.2 cm, then join P and Q. The included angle and adjacent sides define the triangle."),
        (8, "Construct obtuse triangle DEF with ∠EFD=135°, EF=8 cm and FD=5 cm.", "Draw EF=8 cm. At F construct 135° to FE; mark D on that ray with FD=5 cm, then join D to E. The 135° angle makes the triangle obtuse."),
    ])
    replace_exercise(12, "Exercise 12.5", [
        (1, "Find the unknown angles in the six printed figures. a) A triangle has angles 20°,130°,x. b) A triangle has angles 60°,40°,a. c) In triangle ABC, A=60°, the exterior angle at B on straight line ABD is120°, and the unknowns are x at B and y at C. d) ACD, BCEF and DEG are straight lines. Triangle ABC has B=75° and C=65°; triangle EGF has E=50° and G=40°. Find x at C, y at D, z at E and w at F. e) Lines RTV and STU cross at T: triangle RST has R=80°,S=55°,angle a at T; triangle UTV has U=90°,V=30°,angle b at T. f) The left base exterior angle is105°; at the right vertex, the base extension makes102° with an upward ray, and the opposite downward ray makes30° with the extended sloping side. Find left base angle a, right base angle b, angle c between the upward ray and sloping side, and top angle d.", "a) x=180°−20°−130°=30°.\nb) a=180°−60°−40°=80°.\nc) x=180°−120°=60° (linear pair); y=180°−60°−60°=60°.\nd) x=65° (vertically opposite at C). z=50° (vertically opposite at E). In triangle CDE, y=180°−65°−50°=65°. In triangle EGF, w=180°−50°−40°=90°.\ne) Left triangle: a=180°−80°−55°=45°. Right triangle: b=180°−90°−30°=60°. These printed data are inconsistent: if RTV and STU are straight, a and b must be equal as vertically opposite angles. Thus45° and60° are the separate triangle calculations, but no single straight-line figure satisfies all the given angles.\nf) a=180°−105°=75°. c=30° (vertically opposite to the marked30° angle). Along the straight base line, b+c+102°=180°, so b=180°−30°−102°=48°. Finally d=180°−75°−48°=57°."),
        (2, "In triangle ABC, find ∠ABC. The angle at A is 90° and at C is 68°.", "∠ABC=180−90−68=22°."),
        (3, "Find a and b in an isosceles triangle whose vertex angle is 52°.", "Base angles are equal: a=b=(180−52)/2=64°."),
        (4, "Think Higher: Colour the square grid so it is symmetric about both dotted lines.", "Reflect every colored square across the vertical and horizontal dotted axes, keeping corresponding squares the same color. Each orbit of reflected cells must match."),
        (5, "Think Higher: Find the unknown marked angles in the star diagram.", "Use triangle angle sum 180°, linear-pair sums 180°, vertically opposite angles equal, and the matching tick marks for equal sides/base angles. The scan's dense star labels are not legible enough for a reliable numeric list; enter each angle equation from the diagram before evaluating."),
        (6, "Can an isosceles triangle be equilateral? Can an equilateral triangle be isosceles? Draw an isosceles right triangle.", "Yes to both: an equilateral triangle has at least two equal sides, so it is a special isosceles triangle. An isosceles right triangle has angles 45°,45°,90°."),
    ])
    replace_exercise(12, "Review Exercise", [
        (1, "Choose the correct option.\na) A line of symmetry divides a shape into quarters/halves/thirds/fourths.\nb) A shape unchanged at least twice during a full turn has which symmetry?\nc) Turning a shape around a fixed point is called what?\nd) Moving a shape to a new place is called what?\ne) Translation does not affect which property?\nf) Translate 2 left and 1 down.\ng) Rule for 90° counterclockwise or 270° clockwise rotation.\nh) Interpret (x,y)→(x−4,y+6).",
         "a) Halves. b) Rotational symmetry. c) Rotation. d) Translation. e) Size. f) (x−2,y−1). g) Switch x and y and change the sign of the new x: (x,y)→(−y,x). h) Subtract 4 from x and add 6 to y."),
        (2, "For each pictured figure, decide whether the dotted line is a line of symmetry.", "The five diagrams show: a) popsicle with vertical axis—yes; b) star with vertical axis—yes; c) circle with vertical axis—yes; d) horizontal stepped figure—yes if top and bottom halves match; e) parallelogram with a midline—no. The printed drawings make d somewhat unclear."),
        (3, "Draw the line(s) of symmetry for the three pictured shapes, if any.", "a) Crossed X-like shape: draw its matching diagonal axes (four if all arms are equal). b) Notched rectangle: horizontal centre line. c) Bent arrow-like shape: horizontal centre line if the upper and lower halves match."),
        (4, "Tick the figures with rotational symmetry; state their order and centre.", "From left to right: a) irregular trapezium—order1; b) double-headed arrow—order2, centre midpoint; c) four-way arrow—order4, centre intersection; d) square—order4, centre; e) curved arrow—order1; f) centrally symmetric irregular rectangle-like shape—order2, centre."),
        (5, "Rotate the shown pentagon through 180° counterclockwise about the origin.", "Use (x,y)→(−x,−y) for each vertex; then connect the five image points in their original order. This preserves side lengths and orientation up to the half-turn."),
        (6, "Draw a pentagon and rotate it 90° counterclockwise about the origin.", "Sample pentagon A(1,1), B(4,1), C(5,3), D(3,5), E(1,4). Apply (x,y)→(−y,x): A′(−1,1), B′(−1,4), C′(−3,5), D′(−5,3), E′(−4,1)."),
        (7, "Draw a rectangle and rotate it 180° counterclockwise about the origin.", "Sample rectangle vertices (1,1),(5,1),(5,3),(1,3) become (−1,−1),(−5,−1),(−5,−3),(−1,−3)."),
        (8, "Translate the graph image by (x,y)→(x+5,y+8).", "Add 5 to every vertex's x-coordinate and 8 to its y-coordinate; the translation vector is (5,8)."),
        (9, "Name each pair of graph images and describe the translation from the darker to lighter figure.", "Both pairs show congruent polygons. For each pair, choose corresponding vertices and subtract their coordinates; the same horizontal and vertical displacement applies to every vertex. The scan grid is faint, so use the displayed graph coordinates to read the exact displacement."),
        (10, "Construct an equilateral triangle PQR with PQ=QR=7 cm.", "Draw PQ=7 cm; draw 7 cm arcs at P and Q; their intersection is R. Join PR and QR."),
        (11, "Construct isosceles triangle ABC with AB=4 cm and BC=AC=6 cm.", "Draw AB=4 cm. Draw 6 cm arcs centered at A and B; their intersection is C. Join AC and BC."),
        (12, "Construct right triangle LMN with ∠LMN=90°, LM=6.3 cm and MN=4.5 cm.", "Draw LM=6.3 cm; erect a perpendicular at M; mark N 4.5 cm from M and join L to N."),
        (13, "Construct scalene triangle DEF with ∠DEF=40°, ∠EDF=20° and DE=7 cm.", "The third angle is 120°. Draw DE=7 cm, construct 40° at E and 20° at D; the rays meet at F."),
        (14, "Construct acute triangle PQR with ∠PRQ=70°, PR=6 cm and QR=5 cm.", "Draw PR=6 cm. At R construct 70°; mark Q 5 cm along the second arm and join P to Q."),
        (15, "Construct obtuse triangle DEF with ∠EFD=140°, EF=5 cm and FD=3 cm.", "Draw EF=5 cm. Construct 140° at F; mark D 3 cm along the ray and join D to E."),
        (16, "Find the unknown angles in the pictured triangles.\na) 20°,110°,x\nb) 60°, exterior 128°, and apex a\nc) isosceles, vertex 86°, base angle a\nd) apex55°, exterior at C150°\ne) isosceles, one base angle60°",
         "a) x=50°. b) interior base angle=52°; a=68°. c) a=47° for each base angle. d) C=30°, B=95°. e) both base angles are 60°, hence the third is 60°."),
        (17, "Think Higher: Can an isosceles triangle be equilateral? Can an equilateral triangle be isosceles? Draw an isosceles right triangle.", "Yes to both: an equilateral triangle is a special case of an isosceles triangle. An isosceles right triangle has angles 45°,45°,90°."),
        (18, "Math Project: Demonstrate reflection, rotation or translation on a coordinate plane and explain the result.", "Example translation: map every point (x,y) to (x+3,y−2), shifting the shape 3 right and 2 down without changing its size or orientation. A rotation example uses (x,y)→(−y,x), a 90° counterclockwise turn about the origin."),
    ])
    for exercise_86 in (item for chapter in chapters for item in chapter["exercises"]
                        if chapter["number"] == 8 and item["title"] == "Exercise 8.6"):
        exercise_86["answerKeyText"] = (
            "1. a) x=4, vertical; points (4,0), (4,2). b) x=-2, vertical; points (-2,0), (-2,2). "
            "c) x=5, vertical; points (5,0), (5,2). d) y=2, horizontal; points (0,2), (2,2). "
            "e) y=3, horizontal; points (0,3), (2,3). f) y=5, horizontal; points (0,5), (2,5).\n\n"
            "2. a) x=3 vertical; b) x=-8 vertical; c) x=2 vertical; d) x=-1 vertical; "
            "e) x=4 vertical; f) x=2.5 vertical; g) x=4.5 vertical; h) x=-1.5 vertical. "
            "For each, plot any two points with the given x-coordinate and join them vertically.\n\n"
            "3. a) y=4 horizontal; b) y=-9 horizontal; c) y=3.5 horizontal; d) y=-2.5 horizontal; "
            "e) y=5 horizontal; f) y=-1 horizontal; g) y=-3 horizontal; h) y=-5 horizontal. "
            "For each, plot any two points with the given y-coordinate and join them horizontally."
        )
    exercise_111 = next((item for item in chapters[10]["exercises"] if item["title"] == "Exercise 11.1"), None)
    if exercise_111:
        exercise_111["answerKeyText"] = (
            "The printed key gives selected answers: 1. a) 78°; b) 70°; c) 85°, 95°; d) 55°, 125°, 55°. "
            "4. a) 65°; b) 62°; c) 120°, 60°. 6. a) ∠X = 135°, ∠U = 37°; "
            "b) ∠C = 108°, ∠E = 108°; c) ∠ZS = 122°, ∠R = 66°. Other items rely on figures or construction steps."
        )
    exercise_131 = next((item for item in chapters[12]["exercises"] if item["title"] == "Exercise 13.1"), None)
    if exercise_131:
        exercise_131["problems"] = [
            {"qNo": "1", "question": "The table gives commercial and residential new buildings constructed in July–November: Commercial 5, 35, 15, 10, 5; Residential 10, 15, 5, 5, 20. Draw a vertical multiple bar graph using an appropriate scale.", "solution": "Use months on the horizontal axis and number of buildings on the vertical axis. Choose 5 buildings per grid interval. Draw paired bars for each month: July (5,10), August (35,15), September (15,5), October (10,5), November (5,20), in the order commercial, residential. Add a key and axis labels."},
            {"qNo": "2", "question": "Read the multiple bar graph of textbook and notebook sales. Find: a) textbooks sold Monday; b) textbooks sold Wednesday; c) day with fewest notebooks; d) day with most notebooks; e) total notebooks sold on Tuesday and Wednesday altogether; f) day with most books altogether.", "solution": "Read each bar using5 books per marked interval. Textbooks/notebooks by day are Monday15/10, Tuesday20/40, Wednesday25/20, Thursday35/35. a) Monday:15 textbooks. b) Wednesday:25 textbooks. c) Monday has the fewest notebooks (10). d) Tuesday has the most notebooks (40). e) Tuesday and Wednesday notebooks:40+20=60. f) Daily combined totals are25,60,45,70; Thursday has the greatest total,70 books."},
        ]
        exercise_131["answerKeyText"] = (
            "2. a) 15; b) 25; c) Monday; d) Tuesday; e) 60; f) Thursday. "
            "Question 1 is a multiple-bar-graph construction; the source answer key provides the graph rather than a written result."
        )
    replace_exercise(13, "Exercise 13.2", [
        (1, "The line graph gives toy production: January 2,000; February 3,000; March 1,500; April 6,000; May 3,500; June 5,000. Answer: a) highest production; b) months showing a decrease; c) how many more toys in May than March; d) increase from January to April.", "a) April, 6,000 toys. b) February to March and April to May. c) 3,500−1,500=2,000 toys. d) 6,000−2,000=4,000 toys."),
        (3, "The table shows visitors to the Shahi Qila, Lahore, in five months: March 6000, April 8500, May 7000, June 9000, July 6500. Draw a line graph to represent the data.", "Label the horizontal axis Month and the vertical axis Number of visitors. Use equal spacing for March through July and a vertical scale of 1000 visitors per major division (500 per half-division), from 0 to 10000. Plot (March,6000), (April,8500), (May,7000), (June,9000), (July,6500), then join consecutive points with straight segments. June has the most visitors (9000); March has the fewest (6000)."),
        (4, "Temperatures recorded every two hours on a day in April were: 8 a.m. 16.5°C; 10 a.m. 20.2°C; 12 p.m. 28.8°C; 2 p.m. 32.4°C; 4 p.m. 30.7°C; 6 p.m. 26.6°C. Draw a line graph.", "Label the horizontal axis Time and space the six readings equally, two hours apart. Label the vertical axis Temperature (°C), using a scale from 0 to 35°C. Plot (8 a.m.,16.5), (10 a.m.,20.2), (12 p.m.,28.8), (2 p.m.,32.4), (4 p.m.,30.7), (6 p.m.,26.6), and join consecutive points with straight segments. The temperature rises until 2 p.m. and then falls. The maximum recorded temperature is 32.4°C at 2 p.m.; the minimum is 16.5°C at 8 a.m."),
    ])
    replace_exercise(13, "Exercise 13.3", [
        (1, "A family's monthly budget totals Rs 39,800: food Rs 3,150; education Rs 1,950; conveyance Rs 21,100; savings Rs 2,400; miscellaneous Rs 11,200. Draw a pie graph and describe it.", "Convert each amount to a central angle using (amount/39,800)×360°. Food: 28.49°; education: 17.64°; conveyance: 190.85°; savings: 21.71°; miscellaneous: 101.31° (rounded to two decimals, total 360°). Draw adjacent sectors with these angles. Conveyance is the largest item; education is the smallest."),
        (2, "Junaid saved Rs 45, Rs 56, Rs 65 and Rs 75 over four weeks. Draw a pie graph.", "Total=45+56+65+75=Rs 241. Sector angles are 45/241×360≈67.22°, 56/241×360≈83.65°, 65/241×360≈97.14°, and 75/241×360≈112.0°. These sum to 360° (rounding may cause a 0.01° difference). Draw and label the four sectors."),
        (3, "A school conducts a survey of favourite subjects: 423 students like Maths, 123 like History, 222 like English and 86 like Urdu. Draw a pie graph.", "Total=423+123+222+86=854 students. Use angle=(frequency/854)×360°. Maths: 178.31°; History: 51.85°; English: 93.58°; Urdu: 36.25°. Rounded whole-degree sectors are 178°,52°,94°,36° and total 360°. Draw a circle, measure these angles from successive radii, and label every sector. Maths is the most popular subject; Urdu is the least popular."),
        (4, "The table gives transport used by a stated 1080 students: bus 198, cycle 180, bike 240, car 27 and on foot 200. Represent the data with a pie graph and describe the findings.", "The printed counts total 198+180+240+27+200=845, which differs from the stated 1080. These counts cannot produce a complete 1080-student pie chart. A chart of the 845 listed observations uses angle=(count/845)×360°: bus 84.36°, cycle 76.69°, bike 102.25°, car 11.50°, on foot 85.21°. Label it 'Listed transport observations (845)' so it does not imply coverage of all 1080 students. Bike is the most common listed mode and car the least common. The remaining 235 students have no category supplied."),
        (5, "The pie graph shows marks of 90 students in a Maths test out of 100. Its sectors are labelled Above 50 (72°), Above 70 (100°), Above 80 (108°), Above 90 (80°). Find: a–d) the number in each sector; e) between 50 and 80; f) between 70 and 90; g) the ratio of the Above 50 and Above 90 sectors; h) the difference between the Above 50 and Above 80 sectors.", "Each student occupies 360°/90=4°. Divide each angle by 4: a)18; b)25; c)27; d)20 students. e)18+25=43. f)25+27=52. g)18:20=9:10. h)27−18=9 students. The book uses its 'Above' labels for separate score bands; these answers follow that intended band interpretation. Taken literally, above-50 students would include the higher-score groups too, so the labels should not be interpreted as overlapping cumulative totals."),
        (6, "Collect data about anything that can be presented using graphs. Draw suitable graphs, state your conclusions and justify your choice of graph using its shape.", "Sample response: ask 20 classmates for their favourite fruit. Suppose apple=8, mango=6, banana=4 and orange=2. Draw a bar graph with fruit on the horizontal axis and number of students on the vertical axis. Bar heights are 8,6,4,2. A pie graph is also suitable: angles are 144°,108°,72°,36°. Apple is most popular (8/20=40%); orange is least popular (2/20=10%). The bar graph makes category comparisons easy; the pie graph shows each category's share of the total. A line graph is unsuitable because the categories have no time sequence. This is example data; replace it with your own collected observations."),
    ])
    replace_exercise(13, "Exercise 13.4", [
        (1, "The hockey team scored in 20 matches: 3,0,1,4,4,1,2,0,2,2,0,2,0,1,3,1,2,1,1,3. Make a frequency table.", "Tally each score: 0 occurs 4 times; 1 occurs 6 times; 2 occurs 5 times; 3 occurs 3 times; 4 occurs 2 times. Check: 4+6+5+3+2=20 matches."),
        (2, "The blood groups of 25 people in a blood donation bank are B,A,A,O,B,B,B,B,A,B,B,B,A,A,O,O,B,B,B,B,B,A,O,O,A. Represent the data in a frequency distribution table and describe the findings.", "Count each occurrence once. Blood group | Tally (groups of five) | Frequency: A | 5+2 | 7; B | 5+5+3 | 13; O | 5 | 5. Total=7+13+5=25 people. B is the most frequent blood group (13 people); O is the least frequent among those listed (5 people). No person in the supplied data has blood group AB (frequency 0)."),
        (3, "Complete the grouped frequency table for these plant heights (cm): 130,125,125,126,127,127,128,128,128,129; 125,140,142,143,144,144,146,146,147,149; 134,135,135,136,136,137,137,138,138,139; 139,130,131,131,131,132,132,133,133,133. Use intervals 125–129,130–134,135–139,140–144,145–149. Find a) class size; b) classes with equal frequency; c) highest-frequency class; d) lowest-frequency class; e) upper limit of 135–139; f) lower limit of 130–134.", "Tally every height into exactly one class. Class | Tally (groups of five) | Frequency: 125–129 | 5+5 | 10; 130–134 | 5+5+1 | 11; 135–139 | 5+5 | 10; 140–144 | 5 | 5; 145–149 | 4 | 4. Total=10+11+10+5+4=40 plants. a) Class size=130−125=5 cm. b) 125–129 and 135–139 each have 10 plants. c) 130–134, with 11 plants. d) 145–149, with 4 plants. e) Upper limit=139 cm. f) Lower limit=130 cm."),
        (4, "The donations (Rs) are 3118, 4123, 6124, 2125, 1127, 4128, 5129, 2130, 2130, 7133, 4136, 7138, 3141, 2142, 5149, 4150, 6154. Construct a grouped frequency table.", "The range is 7138−1127=6011. Using equal-width classes of 1,000: 1000–1999:1; 2000–2999:4; 3000–3999:2; 4000–4999:4; 5000–5999:2; 6000–6999:2; 7000–7999:2. The frequencies total 17."),
        (5, "Construct a frequency table for the weights of Class 7 students (kg): 20,24,21,18,20,24,21,18; 19,24,19,21,24,20,18,18; 20,24,18,24,26,21,19,26.", "Weight (kg) | Frequency: 18 | 5; 19 | 3; 20 | 4; 21 | 4; 24 | 6; 26 | 2. Count each of the 24 printed weights once. Check: 5+3+4+4+6+2=24 observations. The most frequent weight is 24 kg, occurring six times."),
        (6, "Make a grouped frequency table for marks of 24 students: 55,70,57,73,55,59,64,72,60,48,58,54,69,51,63,78,75,64,65,57,71,78,76,68.", "One valid grouping is 45–54: 3 (48,51,54); 55–64: 10 (55,55,57,57,58,59,60,63,64,64); 65–74: 7 (65,68,69,70,71,72,73); 75–84: 4 (75,76,78,78). The frequencies total 24."),
        (7, "Marks table: 55–69 has 24 students, 70–84 has 10, 85–99 has 15. Find number of classes, total students, lowest data value, count from 70 to 84, and count with 70 or more.", "a) 3 classes. b) 24+10+15=49 students. c) The lowest class has lower limit 55; the exact smallest observed mark cannot be recovered from grouped data. d) 10 students. e) 10+15=25 students."),
    ])
    replace_exercise(13, "Exercise 13.5", [
        (1, "Draw a histogram for class intervals 30–34, 35–39, 40–44, 45–49, 50–54 with frequencies 4,6,12,10,8.", "Use continuous boundaries 29.5–34.5, 34.5–39.5, 39.5–44.5, 44.5–49.5, 49.5–54.5. Draw adjoining bars of equal width 5 and heights 4,6,12,10,8."),
        (2, "Thirty crates of eggs have rotten-egg counts 0,1,4,5,6,7,8,9 with frequencies 2,9,3,4,2,5,1,4. Draw a histogram.", "This is discrete data. Use unit-width adjoining bars centered at the values, with boundaries −0.5 to 0.5, 0.5 to 1.5, 3.5 to 4.5, 4.5 to 5.5, 5.5 to 6.5, 6.5 to 7.5, 7.5 to 8.5, 8.5 to 9.5 and heights 2,9,3,4,2,5,1,4. (The gap at 2 and 3 has frequency 0.)"),
        (3, "Draw a histogram: intervals 15–19,20–24,25–29,30–34,35–39; frequencies 5,9,12,10,4.", "Use boundaries 14.5–19.5, 19.5–24.5, 24.5–29.5, 29.5–34.5, 34.5–39.5; contiguous bar heights 5,9,12,10,4."),
        (4, "Draw a histogram for intervals 5–14,15–24,25–34,35–44,45–54 with frequencies 3,5,2,4,12.", "Use boundaries 4.5–14.5,14.5–24.5,24.5–34.5,34.5–44.5,44.5–54.5. Draw adjoining bars of width 10 and heights 3,5,2,4,12."),
    ])
    replace_exercise(13, "Exercise 13.6", [
        (1, "Find the mean: a) 30,32,40,25,21; b) 51,62,45,62,72,68; c) 114,154,240,112; d) 500,560,640,520,480.", "Use mean=sum/count. a) 148/5=29.6. b) 360/6=60. c) 620/4=155. d) 2700/5=540."),
        (2, "Find the mean weight (kg): 60,72,58,66,54,63,77,60,59,71.", "Sum=60+72+58+66+54+63+77+60+59+71=640 kg; n=10. Mean=640/10=64 kg."),
        (3, "A person's average daily income for the first five days is Rs 2,400. With the sixth day included, the six-day average is Rs 2,500. Find the sixth day's income.", "First five days total=5×2400=Rs 12,000. Six-day total=6×2500=Rs 15,000. Sixth-day income=15,000−12,000=Rs 3,000."),
        (4, "Wire lengths (m) in grouped data: 1–10:2, 11–20:7, 21–30:10, 31–40:3, 41–50:1. Find mean length.", "Use class midpoints 5.5,15.5,25.5,35.5,45.5. Σfm=11+108.5+255+106.5+45.5=526.5; Σf=23. Mean=526.5/23≈22.89 m."),
        (5, "Employees' job duration: 1–3 years:12; 3–5:22; 5–7:27; 7–9:19. Find the mean duration.", "Use midpoints 2,4,6,8. Σfm=24+88+162+152=426; total employees=80. Mean=426/80=5.325 years, about 5 years 3 months 27 days."),
        (6, "Marks of 15 students: 36,25,32,40,28,35,26,32,30,27,32,28,39,20,35. Find median and mode.", "Arrange in order: 20,25,26,27,28,28,30,32,32,32,35,35,36,39,40. The 8th of 15 values is the median, 32. The most frequent value is 32, so mode=32."),
        (7, "Marks are 92 in Maths, 75 in English, 80 in Islamiat, 86 in Science, with respective weights 5,4,3,4. Find the weighted mean.", "Weighted mean=(92×5+75×4+80×3+86×4)/(5+4+3+4)=1344/16=84."),
        (8, "Find the median: a) 18,15,16,13,11; b) 200,150,230,175,300,250.", "a) Ordered 11,13,15,16,18; median=15. b) Ordered 150,175,200,230,250,300; median=(200+230)/2=215."),
        (9, "Find the mode: a) 6,7,7,12,14,15,17; b) 12,15,14,15,17,18,14,16.", "a) 7 occurs twice; mode=7. b) 14 and 15 each occur twice; the data are bimodal, modes 14 and 15."),
    ])
    replace_exercise(13, "Exercise 13.7", [
        (1, "A bag has 7 blue, 4 green, 4 red and 5 yellow marbles. Find probabilities and classify: a) blue; b) not blue; c) orange; d) marble; e) blue or green.", "There are 20 marbles. a) P(blue)=7/20. b) P(not blue)=13/20. c) P(orange)=0 (impossible). d) P(marble)=20/20=1 (certain). e) P(blue or green)=(7+4)/20=11/20."),
        (2, "The spinner has eight equal sectors labelled 3,2,6,3,2,4,5,1. Find each probability and its complement: a) <3; b) not 5; c) smaller than 6; d) odd; e) prime; f) even; g) 10.", "a) P(<3)=3/8 (1,2,2); complement=5/8. b) P(not 5)=7/8; complement=1/8. c) P(<6)=7/8; complement=1/8. d) P(odd)=4/8=1/2; complement=1/2. e) The five prime-number sectors are labelled 2,2,3,3,5. Thus P(prime)=5/8; P(not prime)=3/8. Count sectors separately even when their labels repeat; 1 is not prime. f) Even labels 2,6,2,4: 4/8=1/2; complement=1/2. g) P(10)=0; complement=1."),
        (3, "A jar has 3 square, 3 circular and 3 triangular buttons. State which events are impossible/certain and find each probability and complement: picking a square, a button, not a button, circular, triangular, not rectangular.", "There are 9 buttons. a) Square=3/9=1/3 (complement 2/3). Button=1 (complement 0). Not a button=0 (complement 1). Circular=3/9=1/3 (complement 2/3). Triangular=1/3 (complement 2/3). For the textbook’s separate shape categories, no button is labelled rectangular, giving P(not rectangular)=1 and complement 0. Under the mathematical definition, a square is also a rectangle: the three square buttons then count as rectangular, giving P(not rectangular)=6/9=2/3 and complement 1/3. The distinction comes from the use of shape names in this question. Picking a button is certain; not a button is impossible."),
        (4, "Madiha chooses from {1,8,4,10,3,6}. Find probabilities and complements: a) 1-digit; b) multiple of 2; c) 9; d) not a number; e) 2-digit even number.", "There are 6 equally likely numbers. a) Five are one-digit, so 5/6; complement=1/6. b) Four are even, so 4/6=2/3; complement=1/3. c) 9 is absent, so 0; complement=1. d) All outcomes are numbers, so 0; complement=1. e) 10 is the only two-digit even number, so 1/6; complement=5/6."),
    ])
    replace_exercise(13, "Review Exercise", [
        (1, "Choose the correct options: a) graph for change over time; b) meaning of discrete; c) measure of likelihood; d) result of a random experiment; e) 50% chance; f) range of probability; g) name for number of occurrences; h) distribution arranged in a table.", "a) Line graph. b) Distinct/separate. c) Probability. d) Outcome. e) Equally likely. f) 0 to 1. g) Frequency. h) Frequency distribution."),
        (2, "A bakery sold 84 rolls Monday, 96 Tuesday, 66 Wednesday, 48 Thursday, 54 Friday. Draw a line graph.", "Plot and join (Mon,84), (Tue,96), (Wed,66), (Thu,48), (Fri,54). Label days on the x-axis and rolls sold on the y-axis; a scale of 12 rolls per division reaches 96 exactly."),
        (3, "Draw a horizontal multiple bar graph for male/female flood-fund collectors: Groups A–E; males 20,30,18,15,25; females 25,30,25,35,25.", "Use groups on the vertical axis and number of students on the horizontal axis. Draw paired bars for A (20,25), B (30,30), C (18,25), D (15,35), E (25,25), with a legend for male and female. Scale 5 students per division works."),
        (4, "Make a frequency table for Shahid Afridi's runs in three overs: 2,0,4,0,6,6,6,4,2,4,2,6,6,2,4,4,4,4.", "Tally the listed scores in ascending order. From the printed sequence: 0 occurs 2 times; 2 occurs 4 times; 4 occurs 7 times; 6 occurs 5 times. Total=18 balls recorded."),
        (5, "Construct frequency tables: a) 4,3,6,5,2,4,3,3,6,4,2,3,2,2,3,3,4,5,6,4,2,3,4; b) 6,7,5,4,5,6,6,8,7,9,6,5,6,7,7,8,9,4,6,7,6,5.", "a) Score: 2→5, 3→7, 4→6, 5→2, 6→3 (check listed values; tally each once before use). b) Score: 4→2, 5→4, 6→7, 7→5, 8→2, 9→2. Put values in ascending order and check frequencies sum to the number of observations."),
        (6, "Make a frequency table for 30 marks: 20,6,23,19,9,14,15,3,1,12,10,20,13,3,17,10,11,6,21,9,6,10,9,4,5,1,5,11,7,24.", "Ungrouped frequencies: 1→2, 3→2, 4→1, 5→2, 6→3, 7→1, 9→3, 10→3, 11→2, 12→1, 13→1, 14→1, 15→1, 17→1, 19→1, 20→2, 21→1, 23→1, 24→1. Check the frequencies total 30."),
        (7, "House construction expense percentages: brick 15%, cement 20%, steel 10%, labour 25%, miscellaneous 30%; total Rs 1,800,000. Draw a pie graph and describe it.", "Angles: brick 54°, cement 72°, steel 36°, labour 90°, miscellaneous 108°. Amounts: Rs 270,000; Rs 360,000; Rs 180,000; Rs 450,000; Rs 540,000. Miscellaneous is largest; steel is smallest."),
        (8, "The following data are weights (grams) of different kinds of candies. Draw a histogram for this continuous data: 60,60.5,61,61,61.5,63.5,63.5,63.5,64,64,64,64,64,64,64,64.5,64.5,64.5,64.5; 64.5,64.5,64.5,64.5,66,66,66,66,66,66,66,66,66,66,66.5,66.5,66.5,66.5,66.5; 66.5,66.5,66.5,66.5,66.5,66.5,67,67,67,67,67,67,67,67,67,67,67,67,67.5,67.5; 67.5,67.5,67.5,67.5,67.5,68,68,69,69,69,69,69,69,69,69,69,69,69.5,69.5,69.5; 69.5,69.5,70,70,70,70,70,70,70.5,70.5,70.5,71,71,71.", "Use equal-width classes of 2 grams, with each lower boundary included and each upper boundary excluded. Class (g) | Frequency: 60≤w<62 | 5; 62≤w<64 | 3; 64≤w<66 | 15; 66≤w<68 | 40; 68≤w<70 | 17; 70≤w<72 | 12. Check: 5+3+15+40+17+12=92 candies. Draw adjacent bars with boundaries 60,62,64,66,68,70,72 on the horizontal axis and frequencies 5,3,15,40,17,12 on the vertical axis. Label the axes Weight (g) and Frequency. The 66≤w<68 class has the largest frequency. Other equal-width groupings are possible if every observation is counted once."),
        (9, "Draw a histogram for the discrete data: 9,9,9.5,9.5,10,10,10,10,10,10,10.5,10.5,10.5,10.5,10.5,10.5,10.5,10.5; 11,11,11,11,11,11,11,11,11,11,11,11,11,11.5,11.5,11.5,11.5,11.5,11.5,11.5; 12,12,12,12,12,12,12,12.5,12.5,12.5,12.5,14.", "Frequency table: 9→2; 9.5→2; 10→6; 10.5→8; 11→13; 11.5→7; 12→7; 12.5→4; 13→0; 13.5→0; 14→1. Check: 2+2+6+8+13+7+7+4+0+0+1=50. Draw adjacent bins of width 0.5 centred on these values: [8.75,9.25), [9.25,9.75), and so on through [13.75,14.25). Their heights are the listed frequencies. Label the horizontal axis Data value and the vertical axis Frequency; retain the empty bins at 13 and 13.5. The highest bar is at 11 with frequency 13."),
        (10, "Construct a frequency distribution of the heights (in inches) of 35 persons, then calculate the grouped mean: 60,72,70,69,58,59,60,63,62,60,72,72,70,71,57,65,67,65,66,53,55,65,60,72,70,69,72,72,60,57,63,65,66,72,59.", "Choose classes of width 5. Class | Frequency f | Midpoint m | fm: 50–54 | 1 | 52 | 52; 55–59 | 6 | 57 | 342; 60–64 | 8 | 62 | 496; 65–69 | 9 | 67 | 603; 70–74 | 11 | 72 | 792. Total frequency=35; total fm=2285. Grouped mean=Σ(fm)/Σf=2285/35≈65.29 inches. This is an estimate because each class is represented by its midpoint."),
        (11, "Find mean, median and mode: a) 250,125,620,180,200,125,200,180; b) 12,18,15,16,12,15,18,18,18,18,16,19.", "a) Sum=1880; mean=1880/8=235. Ordered data: 125,125,180,180,200,200,250,620. Median=(180+200)/2=190. Modes=125,180,200, each occurring twice. b) Sum=195; mean=195/12=16.25. Ordered data: 12,12,15,15,16,16,18,18,18,18,18,19. Median=(16+18)/2=17. Mode=18, occurring five times."),
        (12, "Sidra picks one marble without looking from the pictured bag containing 3 red, 6 green and 3 blue marbles. a) Find i) P(red), ii) P(green), iii) P(blue), iv) P(not blue), v) P(marble), vi) P(yellow), vii) P(not a marble). b) Find each event's complement. c) Identify certain, impossible and equally likely events.", "There are 3+6+3=12 marbles. Use P(event)=favourable outcomes/12. a) i)3/12=1/4; ii)6/12=1/2; iii)3/12=1/4; iv)(3+6)/12=3/4; v)12/12=1; vi)0/12=0; vii)0/12=0. b) Subtract each probability from 1, in the same order: not red=3/4; not green=1/2; not blue=3/4; blue=1/4; not a marble=0; not yellow=1; marble=1. c) Picking a marble is certain; picking yellow or something other than a marble is impossible. Red and blue are equally likely (each 1/4). Green and not green are also equally likely (each 1/2)."),
    ])
    review12 = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Review Exercise")
    # Printed review numbering skips 3 and 7 on pp.237–238.
    review_numbering = {"1":"1","2":"2","3":"4","4":"5","5":"6","6":"8","7":"9",
                        "8":"10","9":"11","10":"12","11":"13","12":"14","13":"15",
                        "14":"16","15":"17","16":"18","18":"Project"}
    review12["problems"] = [problem for problem in review12["problems"] if problem["qNo"] != "17"]
    for problem in review12["problems"]:
        original_number = problem["qNo"]
        problem["qNo"] = review_numbering[original_number]
        if original_number == "2":
            problem["solution"] = "a) Yes: the vertical line divides the popsicle into matching halves. b) Yes: the vertical line divides the star-topped shape into matching halves. c) Yes: a diameter is a symmetry line of a circle. d) No: the upper-left projection does not have a matching projection directly below the dotted horizontal line. e) No: the slanted parallelogram is not reflected onto itself by the dotted horizontal line."
        elif original_number == "18":
            problem["question"] = "Math Project: work in groups to demonstrate reflection, rotation or translation. Materials: coloured cardboard or chart papers, a large coordinate-plane print, scissors, glue, pins, ruler and pencils. Each member chooses a transformation, cuts coloured shapes, displays the transformation on a coordinate sheet, and presents the result to the other groups."
            problem["solution"] = "Sample presentation: cut a triangle with vertices A(1,1),B(4,1),C(2,3). For translation3 units right and2 down, apply (x,y)→(x+3,y−2): A′(4,−1),B′(7,−1),C′(5,1). For reflection in the y-axis, apply (x,y)→(−x,y): A′(−1,1),B′(−4,1),C′(−2,3). For90° counterclockwise rotation about the origin, apply (x,y)→(−y,x): A′(−1,1),B′(−1,4),C′(−3,2). Choose one transformation, label the original and image, and explain its rule. Corresponding side lengths are preserved in each case; reflection reverses orientation. These coordinates are a sample for the open-ended project."
    # A few Word transcription parts repeat a heading and its surrounding
    # paragraphs. Keep the first exercise of each printed title after applying
    # scan-checked replacements, so duplicate review cards do not appear.
    for chapter in chapters:
        unique = []
        seen_titles = set()
        for exercise in chapter["exercises"]:
            title = re.sub(r"\s+", " ", exercise["title"]).strip().lower()
            if title in seen_titles:
                continue
            seen_titles.add(title)
            unique.append(exercise)
        chapter["exercises"] = unique
    unit7 = next(chapter for chapter in chapters if chapter["number"] == 7)
    unit7["workedExamples"].insert(0, {
        "id": "we-7-unit7-opening-pool",
        "title": "Opening problem: rectangular pool dimensions",
        "problem": "A rectangular pool has side lengths x + 3 m and x − 5 m and area 20 m². Find its dimensions.",
        "solution": "Area = length × width, so (x+3)(x−5)=20. Expand: x²−2x−15=20, hence x²−2x−35=0. Factor: (x−7)(x+5)=0, giving x=7 or x=−5. Since a length x−5 must be positive, x=7. The sides are x+3=10 m and x−5=2 m; 10×2=20 m²."
    })
    unit13 = chapters[12]
    for section in unit13["sections"]:
        if section["id"] == "13.1.1":
            section["id"] = "13.3.1"
            section["title"] = "13.3.1 Choosing an Appropriate Type of Graph/Chart"
            section["heading"] = section["title"]
    unit13_additions = {
        "13.3": ("13.3 Pie Graph", [
            "A pie graph is a circle divided into sectors. The full circle represents the total, and each sector represents one category's share of that total.",
            "To draw a pie graph, calculate each central angle: angle = (category frequency ÷ total frequency) × 360°. Draw a circle, use a protractor to mark each sector in sequence, then label the categories.",
            "Example: five students contributed Rs 940, 800, 1,000, 1,200 and 1,100. The total is Rs 5,040. The sector angles are approximately 67°, 57°, 71°, 86° and 79°, respectively. Their sum is 360°."
        ]),
        "13.4": ("13.4 Data and its Presentation", [
            "Data are observations or measurements collected for a purpose. Presenting data in tables and graphs helps readers see patterns, compare values and communicate findings clearly.",
            "Choose a graph that fits the kind of information: bar and multiple-bar graphs compare categories, line graphs show change over time, pie graphs show parts of a whole, and histograms display grouped numerical data."
        ]),
        "13.4.1": ("13.4.1 Data and Data Collection", [
            "Raw data are information collected before it has been organized. Data collection is the process of gathering that information.",
            "Discrete data are separate, countable whole-number values, such as the number of students, people in a population, players or animals. Continuous data are measurements that can take fractional or decimal values within a range, such as height, mass, volume or temperature."
        ]),
        "13.4.3": ("13.4.3 Grouped Frequency Distribution and Class Boundaries", [
            "When data contain many different values, group them into equal-width class intervals. The range is the highest value minus the lowest value. A class interval has a lower limit and an upper limit; its class size is the difference between those limits.",
            "A grouped frequency table lists each interval and the number of observations in it. Tally the observations once, then check that the frequencies add to the total number of observations.",
            "Class boundaries are the midpoints between adjacent class limits. For whole-number classes such as 53–57 followed by 58–62, the shared boundary is (57+58)/2=57.5, so the continuous boundaries are 52.5–57.5 and 57.5–62.5."
        ]),
        "13.6.1": ("13.6.1 Arithmetic Mean", [
            "The arithmetic mean is the sum of all observations divided by the number of observations: mean = Σx/n.",
            "Example: for 1, 6, 8, 9, 7, 5, the sum is 36 and there are 6 values, so the mean is 36/6=6.",
            "For a missing value, use total = mean × number of values. If four boys have mean weight 24 kg, their total is 96 kg. If five boys including another have mean 24.6 kg, their combined total is 123 kg, so the fifth boy weighs 123−96=27 kg."
        ]),
        "13.7.1": ("13.7.1 Types of Events", [
            "Two events are complementary when exactly one of them occurs; their probabilities add to 1. Thus P(not A)=1−P(A). An event with probability 1 is certain, while an event with probability 0 is impossible.",
            "Outcomes are equally likely when they have the same chance. For equally likely outcomes, P(event)=number of favourable outcomes ÷ total possible outcomes. For example, from the set {3,4,6,7,8,10}, four numbers are even, so P(even)=4/6=2/3 and P(not even)=1/3."
        ]),
    }
    existing_ids = {section["id"] for section in unit13["sections"]}
    for section_id, (title, paragraphs) in unit13_additions.items():
        if section_id not in existing_ids:
            unit13["sections"].append(make_section(title, paragraphs))
    def section_order(section):
        if section["title"].lower() == "student learning outcomes":
            return (0, (-2,))
        if section["title"].lower() == "introduction":
            return (0, (-1,))
        match = re.match(r"^(\d+(?:\.\d+)+)", section["id"])
        return (1, tuple(map(int, match.group(1).split(".")))) if match else (2, ())
    unit13["sections"].sort(key=section_order)
    if not any(section["id"] == "13.6.3" for section in unit13["sections"]):
        median_section = make_section("13.6.3 Median", [
            "The median is the value that divides ordered data into two equal halves. First arrange the values from least to greatest. If the number of values is odd, the median is the single middle value. If the number is even, take the arithmetic mean of the two middle values.",
            "Example: for 6, 3, 8, 14, 12, 10, 9, 14, 16, the ordered list is 3, 6, 8, 9, 10, 12, 14, 14, 16. There are 9 values, so the 5th value is the median: 10.",
            "Example: for 10, 12, 14, 16, 18, 20, the two middle values are 14 and 16. Median=(14+16)/2=15."
        ])
        mode_index = next((i for i, section in enumerate(unit13["sections"]) if section["id"] == "13.6.4"), None)
        unit13["sections"].insert(mode_index if mode_index is not None else len(unit13["sections"]), median_section)
    unit13_key_text = {
        "Exercise 13.1": "2. a) 15; b) 25; c) Monday; d) Tuesday; e) 60; f) Thursday. 1. Draw grouped bars from the two data rows using a consistent scale.",
        "Exercise 13.2": "1. a) April; b) February and April; c) 2,000 toys; d) 4,000 toys.",
        "Exercise 13.3": "3. Total 854; rounded angles 178°,52°,94°,36°. 4. Listed counts total 845, not 1080; see worked explanation. 5. a)18; b)25; c)27; d)20; e)43; f)52; g)9:10; h)9. 6. Open data-collection task; sample response supplied.",
        "Exercise 13.4": "1. Frequencies 4,6,5,3,2 for scores 0–4. 2. A=7, B=13, O=5 (AB=0). 3. Class frequencies 10,11,10,5,4; a)5 cm; b)125–129 and 135–139; c)130–134; d)145–149; e)139; f)130. 4. Frequencies 1,4,2,4,2,2,2 for the listed width-1000 classes. 5. Frequencies 5,3,4,4,6,2 for weights 18,19,20,21,24,26. 6. Frequencies 3,10,7,4 for the listed classes. 7. a)3 classes; b)49 students; c)lower class limit 55; exact smallest mark unknown; d)10; e)25.",
        "Exercise 13.6": "1. a) 29.6 (about 30); b) 60; c) 155; d) 540. 2. 64 kg. 3. Rs 3,000. 4. 22.89 m. 5. 5.325 years. 6. Median 32; mode 32. 7. 84. 8. a) 15; b) 215. 9. a) 7; b) 14 and 15. Recalculated from the printed question data; some figures in the scan's key disagree.",
        "Exercise 13.7": "1. a) 7/20; b) 13/20; c) 0 (impossible); d) 1 (certain); e) 11/20. 2. a) 3/8; b) 7/8; c) 7/8; d) 1/2; e) 5/8; f) 1/2; g) 0. 3. Square 1/3; button 1 (certain); not a button 0 (impossible); circle 1/3; triangle 1/3; not rectangular 1. 4. a) 5/6; b) 2/3; c) 0; d) 0; e) 1/6.",
        "Review Exercise": "1. a) iii; b) iii; c) ii; d) i; e) iv; f) iii; g) ii; h) i. 10. Grouped mean approximately 65.29 inches using width-5 classes. 11. a) Mean 235, median 190, modes 125, 180 and 200; b) mean 16.25, median 17, mode 18.",
    }
    for exercise in unit13["exercises"]:
        if exercise["title"] in unit13_key_text:
            exercise["answerKeyText"] = unit13_key_text[exercise["title"]]
    chapters[10]["workedExamples"] = [
        {"id": "we-11-parallelogram", "title": "Opposite and adjacent angles in a parallelogram", "problem": "In parallelogram EFGH, ∠EHG=98°. Find the other three angles.", "solution": "Opposite angles are equal, so ∠EFG=98°. Adjacent angles are supplementary: 180°−98°=82°. Thus ∠HEF=82° and ∠HGF=82°. The four angles are 82°,98°,82°,98° around the figure."},
        {"id": "we-11-rhombus", "title": "Angles in a rhombus", "problem": "In rhombus PQRS, ∠QRS=70°. Find the other three angles.", "solution": "Opposite angles are equal, so ∠QPS=70°. Adjacent angles sum to 180°: ∠PSR=180°−70°=110°. The opposite angle ∠PQR=110°. The remaining angles are 70°,110°,110°."},
        {"id": "we-11-trapezium", "title": "Supplementary angles in a trapezium", "problem": "In trapezium EFGH, EF∥HG and ∠FEH=55°. Find the interior angle at H on the same non-parallel side.", "solution": "The two interior angles on transversal EH between parallel lines EF and HG add to 180°. So ∠EHG=180°−55°=125°."},
        {"id": "we-11-kite", "title": "Unknown angles in a kite", "problem": "A kite has one pair of equal opposite angles A and C; the other angles are 80° and 60°. Find A and C.", "solution": "The angles of a quadrilateral sum to 360°. Since A=C, 2A+80°+60°=360°. Thus 2A=220° and A=C=110°."},
        {"id": "we-11-polygon-interior", "title": "Interior angles of regular polygons", "problem": "Find each interior angle of regular polygons with 5, 6, 7 and 8 sides.", "solution": "For n sides, each interior angle is 180°(n−2)/n. Pentagon: 540°/5=108°. Hexagon: 720°/6=120°. Heptagon: 900°/7≈128.57°. Octagon: 1080°/8=135°."},
        {"id": "we-11-polygon-sum", "title": "Sum of interior angles", "problem": "Find the sum of a polygon's interior angles when it has 9 sides.", "solution": "An n-sided polygon's interior-angle sum is 180°(n−2). For n=9: 180°×7=1,260°."},
        {"id": "we-11-polygon-exterior", "title": "Exterior angles of regular polygons", "problem": "Find the exterior angle of a regular octagon and the sum of exterior angles of any polygon.", "solution": "The exterior angles of any polygon sum to 360°. For a regular octagon, each is 360°/8=45°."
        }
    ]
    unit11_sections = chapters[10]["sections"]
    for section in unit11_sections:
        if section["id"] == "11.3.3":
            section["title"] = "11.3.3 Measure of Exterior Angles of a Polygon"
            section["heading"] = section["title"]
    unit11_additions = {
        "11.1.5": ("11.1.5 Trapezium", ["A trapezium is a quadrilateral with exactly one pair of opposite parallel sides. The angles on the same non-parallel side are supplementary: each such pair sums to 180°.", "If AB∥DC, then ∠A+∠D=180° and ∠B+∠C=180°."]),
        "11.2.1": ("11.2.1 Types of Polygon", ["A polygon is a closed plane figure made from three or more straight line segments. Names depend on the number of sides: triangle 3, quadrilateral 4, pentagon 5, hexagon 6, heptagon 7 and octagon 8.", "A polygon is regular when all sides and all interior angles are equal; otherwise it is irregular. A convex polygon has no reflex interior angle and all vertices point outward. A concave polygon has at least one reflex interior angle and an inward-pointing vertex."]),
        "11.3.4": ("11.3.4 Exterior Angle of a Triangle", ["An exterior angle of a triangle equals the sum of its two non-adjacent interior angles. It also forms a linear pair with the adjacent interior angle, so the two add to 180°.", "For example, if the remote interior angles are 50° and 60°, the exterior angle is 50°+60°=110°. The adjacent interior angle is 180°−110°=70°."]),
    }
    unit11_ids = {section["id"] for section in unit11_sections}
    for section_id, (title, paragraphs) in unit11_additions.items():
        if section_id not in unit11_ids:
            unit11_sections.append(make_section(title, paragraphs))
    unit11_sections.sort(key=section_order)
    chapters[11]["workedExamples"] = [
        {"id": "we-12-rotation", "title": "Rotate a rectangle 90° counterclockwise", "problem": "Rotate rectangle ABCD with A(2,6), B(7,6), C(7,2), D(2,2) about the origin through 90° counterclockwise.", "solution": "Use (x,y)→(−y,x). A′(−6,2), B′(−6,7), C′(−2,7), D′(−2,2). Plot the four image points and connect them in order."},
        {"id": "we-12-translation", "title": "Translate a triangle 2 right and 3 up", "problem": "Translate A(−4,1), B(−6,4), C(−2,4) by 2 units right and 3 units up.", "solution": "The rule is (x,y)→(x+2,y+3). Thus A′(−2,4), B′(−4,7), C′(0,7). Connect the image vertices in the original order."},
        {"id": "we-12-describe-translation", "title": "Describe a translation from matching vertices", "problem": "A(1,4) maps to A′(−3,−4). Describe the translation.", "solution": "The x-coordinate changes by −3−1=−4 and the y-coordinate by −4−4=−8. The rule is (x,y)→(x−4,y−8), or 4 units left and 8 units down."},
        {"id": "we-12-equilateral", "title": "Construct an equilateral triangle", "problem": "Construct triangle MNO with MN=4 cm and ∠M=∠N=60°.", "solution": "Draw MN=4 cm. At M and N construct 60° rays on the same side of MN. Their intersection is O. Join OM and ON; all three sides are equal and all angles are 60°."},
        {"id": "we-12-isosceles", "title": "Construct an isosceles triangle", "problem": "Construct triangle PQR with PQ=4 cm and base angles ∠P=∠Q=50°.", "solution": "Draw PQ=4 cm. Construct 50° rays at P and Q on the same side of PQ. Their intersection is R. The equal base angles make RP=RQ; the apex angle is 180°−50°−50°=80°."},
        {"id": "we-12-scalene", "title": "Construct a scalene triangle", "problem": "Construct triangle PQR with ∠P=40°, ∠Q=50° and PQ=5 cm.", "solution": "Draw PQ=5 cm. Construct a 40° ray at P and a 50° ray at Q on the same side of PQ. Their intersection is R. The third angle is 180°−40°−50°=90°; the angles are all different, so the triangle is scalene and right-angled."},
        {"id": "we-12-acute", "title": "Construct an acute triangle", "problem": "Construct an acute triangle LMN with LM=3.5 cm, LN=3 cm and ∠L=40°.", "solution": "Draw LM=3.5 cm. At L construct 40°. On that ray mark N so LN=3 cm, then join M to N. The included angle and two side lengths determine the triangle; all its angles are less than 90° as shown in the source diagram."},
        {"id": "we-12-obtuse", "title": "Construct an obtuse triangle", "problem": "Construct triangle LMN with LM=4 cm, LN=3.8 cm and ∠L=120°.", "solution": "Draw LM=4 cm. Construct a 120° ray at L; mark N 3.8 cm from L on the ray and join N to M. Since ∠L=120°, the triangle is obtuse."},
        {"id": "we-12-right", "title": "Construct a right triangle", "problem": "Construct triangle LMN with LM=3 cm, LN=2.5 cm and ∠L=90°.", "solution": "Draw LM=3 cm. Construct a perpendicular ray at L and mark N 2.5 cm from L. Join N to M. The right angle is at L; MN=√(3²+2.5²)=√15.25≈3.91 cm."},
        {"id": "we-12-triangle-angle", "title": "Find an unknown angle in a triangle", "problem": "Triangle ABC has ∠ABC=26° and ∠ACB=84°. Find ∠BAC.", "solution": "The interior angles of a triangle total 180°. ∠BAC=180°−26°−84°=70°."},
        {"id": "we-12-exterior-angle", "title": "Example 2: angles at intersecting straight lines", "problem": "Find ∠RTS when SU and VR are straight lines meeting at T. In triangle TUV, ∠TUV=90° and ∠UVT=45°. The left triangle RST shows ∠R=75° and ∠S=60°.", "solution": "In triangle TUV, ∠VTU=180°−90°−45°=45°. ∠RTS and ∠VTU are vertically opposite angles formed by the two straight lines, so ∠RTS=45°. The left triangle confirms this:180°−75°−60°=45°."},
        {"id": "we-12-right-angle-sum", "title": "Example 3: acute angles in a right triangle", "problem": "In right-angled triangle MNO, ∠MNO=90° and ∠OMN=15°. Find ∠NOM.", "solution": "The two angles other than the right angle sum to90°. Therefore ∠NOM=90°−∠OMN=90°−15°=75°. Check:15°+90°+75°=180°."},
        {"id": "we-12-linear-pair-example", "title": "Find the unknown angles in triangle ABC", "problem": "Triangle ABC has ∠A=60°. B,C,D lie on a straight line, and exterior angle ∠ACD=140°. Find ∠ACB and ∠ABC.", "solution": "Since BD is a straight line, ∠ACB+∠ACD=180°. Thus ∠ACB=180°−140°=40°. Now ∠A+∠B+∠C=180°, so ∠ABC=180°−60°−40°=80°. Check:60°+80°+40°=180°."}
    ]
    unit12_sections = chapters[11]["sections"]
    unit12_additions = {
        "12.1.1": ("12.1.1 Reflective Symmetry", ["A figure has line symmetry if folding it along a line makes the two halves match exactly. The fold line is the line of symmetry, and it divides the figure into matching halves.", "A shape can have vertical, horizontal or diagonal symmetry lines. A dotted line is a symmetry line only when reflection across it maps every point of the shape to a matching point."]),
        "12.4.3": ("12.4.3 Scalene Triangle", ["A scalene triangle has three unequal sides. Its three angles are also unequal.", "To construct one from two base angles and the included side, draw the base, construct each angle at an endpoint on the same side of the base, and join the rays at their intersection. For the example with base PQ=5 cm and angles 40° and 50°, the third angle is 90° and the triangle remains scalene because its angles differ."]),
        "12.5": ("12.5 Finding Unknown Angles of a Triangle", ["Activity from printed p.233: draw a triangle on paper; mark its three angles with different colours; cut out the three corners; place them next to one another on a straight line. Together they form a straight angle, illustrating that a+b+c=180°.", "The three interior angles of every triangle add to 180°. If two angles are known, subtract their sum from 180° to find the third angle.", "An exterior angle and its adjacent interior angle form a straight line and add to 180°. The exterior angle also equals the sum of the two remote interior angles. These facts can be combined with vertically opposite angles, which are equal, to solve diagrams."]),
    }
    unit12_ids = {section["id"] for section in unit12_sections}
    for section_id, (title, paragraphs) in unit12_additions.items():
        if section_id not in unit12_ids:
            unit12_sections.append(make_section(title, paragraphs))
    translation_paragraphs = [
        "A translation moves or shifts an object from one position to another. Every point moves the same distance in the same direction. The shape, size and orientation remain unchanged.",
        "Describe a translation in words or with an ordered-pair rule. Moving right increases x; moving left decreases x. Moving up increases y; moving down decreases y.",
        "Illustration 1: 2 units right and 3 units up gives (x,y)→(x+2,y+3). Add 2 to each x-coordinate and 3 to each y-coordinate.",
        "Illustration 2: 3 units right and 2 units down gives (x,y)→(x+3,y−2). Add 3 to each x-coordinate and subtract 2 from each y-coordinate. The printed sentence says subtract 3, but its stated movement and formula both require subtracting 2.",
        "Quick Check: translate P(2,1), Q(4,1), R(5,3), S(2,3) 2 units up and 5 units left. Apply (x,y)→(x−5,y+2). P′=(2−5,1+2)=(−3,3); Q′=(4−5,1+2)=(−1,3); R′=(5−5,3+2)=(0,5); S′=(2−5,3+2)=(−3,5). Join corresponding vertices in the same order."
    ]
    for index, section in enumerate(unit12_sections):
        if section["id"] == "12.3":
            unit12_sections[index] = make_section("12.3 Translating Objects/Images", translation_paragraphs)
    unit12_sections.sort(key=section_order)
    unit13["workedExamples"] = [
        {"id": "we-13-1", "title": "Multiple bar graph: employees by department", "problem": "Employees joining three departments over five months: Research 15,25,10,15,20; Designing 20,25,15,30,35; Editing 5,20,15,10,25 (May through September). Draw a vertical multiple bar graph.", "solution": "Put months on the horizontal axis and employees on the vertical axis. Use a scale of 5 employees per division. Draw three adjacent bars for each month using the department values in the order Research, Designing, Editing; include a color key and label both axes."},
        {"id": "we-13-3", "title": "Pie graph: student contributions", "problem": "Dania, Marwa, Fahad, Afnan and Rohaan contributed Rs 940, 800, 1,000, 1,200 and 1,100. Find the sector angles and draw a pie graph.", "solution": "Total=940+800+1000+1200+1100=Rs 5,040. Sector angle=(amount/5040)×360°: Dania 67°, Marwa 57°, Fahad 71°, Afnan 86°, Rohaan 79° (rounded to whole degrees; total 360°). Draw the sectors in that order and label them."},
        {"id": "we-13-4a", "title": "Ungrouped frequency distribution: test scores", "problem": "Prepare a frequency table for 40 scores. The printed table lists scores 2,3,5,6,7,8,9,10.", "solution": "Score 2: frequency 3; 3: 2; 5: 2; 6: 5; 7: 9; 8: 7; 9: 7; 10: 5. Total frequency=3+2+2+5+9+7+7+5=40. Record a tally for each observation before counting."},
        {"id": "we-13-4b", "title": "Grouped frequency distribution: weekly savings", "problem": "Thirty-five children's weekly savings range from Rs 32 to Rs 51. Make four equal-width groups and a grouped frequency table.", "solution": "Range=51−32=19. Use class intervals 32–37, 38–43, 44–49, 50–55. The printed table gives frequencies 7,7,9,12, respectively; total=35. The largest group is Rs 50–55, and 23 children saved less than Rs 50."},
        {"id": "we-13-4c", "title": "Class boundaries", "problem": "Find continuous boundaries for intervals 53–57, 58–62, 63–67 and 68–72.", "solution": "The midpoint between adjacent whole-number class limits is 0.5. Subtract 0.5 from each lower limit and add 0.5 to each upper limit: 52.5–57.5, 57.5–62.5, 62.5–67.5 and 67.5–72.5."},
        {"id": "we-13-5a", "title": "Histogram: August temperatures", "problem": "Make a frequency distribution and histogram for 31 daily August temperatures using class width 3°C.", "solution": "Use class intervals 35–37, 38–40, 41–43, 44–46, 47–49 and 50–52. Their frequencies are 1,8,4,9,6,3. Use continuous boundaries 34.5,37.5,40.5,43.5,46.5,49.5,52.5 and draw adjoining bars with those heights."},
        {"id": "we-13-5b", "title": "Reading a histogram: women's heights", "problem": "Read a histogram with class boundaries 58.5–60.5, 60.5–62.5, 62.5–64.5, 64.5–66.5 and frequencies 10,12,8,4.", "solution": "There are 4 classes. Class width=2 inches. Total women=10+12+8+4=34. The greatest frequency is 12, in the 60.5–62.5 inch class."},
        {"id": "we-13-6a", "title": "Arithmetic mean", "problem": "Find the mean of 1, 6, 8, 9, 7, 5.", "solution": "Mean=Σx/n=(1+6+8+9+7+5)/6=36/6=6."},
        {"id": "we-13-6b", "title": "Find a missing value from the mean", "problem": "Four boys have average weight 24 kg. When a fifth boy is included, their average is 24.6 kg. Find the fifth boy's weight.", "solution": "The first four weigh 4×24=96 kg in total. All five weigh 5×24.6=123 kg. The fifth boy weighs 123−96=27 kg."},
        {"id": "we-13-6c", "title": "Mean of grouped data", "problem": "Find the mean marks for intervals 25–39,40–54,55–69,70–84,85–99 with frequencies 3,4,8,9,6.", "solution": "Midpoints are 32,47,62,77,92. Multiply by frequencies: 96,188,496,693,552. Σfm=2,025 and Σf=30, so grouped mean=2,025/30=67.5 marks."},
        {"id": "we-13-6d", "title": "Mode", "problem": "Find the mode of a) 3,4,4,5,5,5,5,6,7,7; b) 7,8,8,9,10,10,11,12.", "solution": "a) 5 occurs four times, more than any other value, so mode=5. b) 8 and 10 each occur twice, the greatest frequency, so the data are bimodal with modes 8 and 10."},
        {"id": "we-13-7", "title": "Certain, impossible and complementary events", "problem": "A card is chosen from a set containing only even numbers. Then a number is chosen from {3,4,6,7,8,10}. Find relevant probabilities.", "solution": "In the all-even card set, P(even)=1 (certain) and P(odd)=0 (impossible). For {3,4,6,7,8,10}, four of six outcomes are even, so P(even)=4/6=2/3. Its complement is P(not even)=1−2/3=1/3."}
    ]
    # Native solution figures use the same reviewed counts as the worked answers.
    review13 = next(ex for ex in unit13["exercises"] if ex["title"] == "Review Exercise")
    for problem in review13["problems"]:
        if problem["qNo"] == "8":
            problem["solutionDiagram"] = {
                "type": "histogram", "title": "Candy weights: grouped histogram",
                "xLabel": "Weight (g)", "yLabel": "Frequency", "yMax": 40,
                "bars": [{"lower": 60+2*i, "upper": 62+2*i, "frequency": f}
                         for i, f in enumerate([5,3,15,40,17,12])]}
        elif problem["qNo"] == "9":
            problem["solutionDiagram"] = {
                "type": "histogram", "title": "Discrete data: histogram with empty bins",
                "xLabel": "Data value (bin width 0.5)", "yLabel": "Frequency", "yMax": 15,
                "bars": [{"lower": 8.75+0.5*i, "upper": 9.25+0.5*i, "frequency": f}
                         for i, f in enumerate([2,2,6,8,13,7,7,4,0,0,1])]}
    exercise134 = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.4")
    tables = {
        "2": ("Blood groups of 25 people", ["Blood group", "Frequency"], [["A",7],["B",13],["O",5],["AB",0],["Total",25]]),
        "3": ("Plant heights", ["Height (cm)", "Frequency"], [["125–129",10],["130–134",11],["135–139",10],["140–144",5],["145–149",4],["Total",40]]),
        "5": ("Student weights", ["Weight (kg)", "Frequency"], [[18,5],[19,3],[20,4],[21,4],[24,6],[26,2],["Total",24]])}
    for problem in exercise134["problems"]:
        if problem["qNo"] in tables:
            title, headers, rows = tables[problem["qNo"]]
            problem["solutionDiagram"] = {"type": "frequency-table", "title": title,
                                          "headers": headers, "rows": rows}
    exercise135 = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.5")
    histograms135 = {
        "1": (29.5, 5, [4,6,12,10,8], "Class boundary", "Frequency"),
        "2": (-0.5, 1, [2,9,0,0,3,4,2,5,1,4], "Rotten eggs per crate", "Number of crates"),
        "3": (14.5, 5, [5,9,12,10,4], "Class boundary", "Frequency"),
        "4": (4.5, 10, [3,5,2,4,12], "Class boundary", "Frequency")}
    for problem in exercise135["problems"]:
        lower, width, frequencies, x_label, y_label = histograms135[problem["qNo"]]
        problem["solutionDiagram"] = {
            "type": "histogram", "title": "Exercise 13.5 — Question " + problem["qNo"],
            "xLabel": x_label, "yLabel": y_label, "yMax": 15 if max(frequencies)>10 else 10,
            "bars": [{"lower": lower+width*i, "upper": lower+width*(i+1), "frequency": f}
                     for i, f in enumerate(frequencies)]}
    transformations = [
        ("a) 2 left, 4 down", [-2,-4], [[-8,3],[-3,3],[-8,8]]),
        ("b) 3 right, 1 up", [3,1], [[-9,9],[-4,9],[-4,5],[-3,5],[-3,4],[-5,4],[-5,3],[-6,3],[-6,4],[-9,4]]),
        ("c) 4 right, 3 up", [4,3], [[6,-2],[10,-6],[6,-10],[2,-6]]),
        ("d) 2 right, 2 down", [2,-2], [[2,2],[9,2],[9,5],[5,5],[5,9],[2,9]])]
    translation_exercise = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Exercise 12.3")
    translation_exercise["problems"][0]["solutionDiagram"] = {
        "type": "coordinate-panels", "panels": [
            {"title": title, "shapes": [{"name": "Original", "points": points},
             {"name": "Translated image", "points": [[x+vector[0], y+vector[1]] for x,y in points]}]}
            for title, vector, points in transformations]}
    def transformation_panel(title, points, transform):
        return {"title": title, "shapes": [
            {"name": "Original", "points": points},
            {"name": "Image", "points": [list(transform(x,y)) for x,y in points]}]}
    rotation_exercise = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Exercise 12.1")
    rotation_panels = {
        "4": [transformation_panel("a) 180° counterclockwise", [[1,1],[1,5],[5,1]], lambda x,y: (-x,-y)),
              transformation_panel("b) 90° clockwise", [[1,-1],[5,-1],[5,-4],[3,-5],[1,-4]], lambda x,y: (y,-x))],
        "5": [transformation_panel("Sample triangle: 270° clockwise", [[1,1],[4,1],[2,3]], lambda x,y: (-y,x))],
        "6": [transformation_panel("Sample trapezium: 90° clockwise", [[1,1],[5,1],[4,3],[2,3]], lambda x,y: (y,-x))]}
    for problem in rotation_exercise["problems"]:
        if problem["qNo"] in rotation_panels:
            problem["solutionDiagram"] = {"type": "coordinate-panels", "panels": rotation_panels[problem["qNo"]]}
    for example in chapters[11]["workedExamples"]:
        if example["id"] == "we-12-rotation":
            example["diagram"] = {"type": "coordinate-panels", "panels": [
                transformation_panel("Rectangle rotated 90° counterclockwise", [[2,6],[7,6],[7,2],[2,2]], lambda x,y: (-y,x))]}
        elif example["id"] == "we-12-translation":
            example["diagram"] = {"type": "coordinate-panels", "panels": [
                transformation_panel("Triangle translated 2 right and 3 up", [[-4,1],[-6,4],[-2,4]], lambda x,y: (x+2,y+3))]}
    import math
    construction_exercise = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Exercise 12.4")
    rad = math.radians
    f_x = 5*math.tan(rad(35))/(math.tan(rad(55))+math.tan(rad(35)))
    construction_data = {
        "1": ([[0,0],[3.8,0],[1.9,3.8*math.sqrt(3)/2]], list("ABC"), ["3.8 cm"]*3, ["60°"]*3),
        "2": ([[0,0],[8,0],[4,math.sqrt(4.5**2-4**2)]], list("PQR"), ["8 cm","4.5 cm","4.5 cm"], []),
        "4": ([[0,0],[4.5,0],[2.25,4.5*math.sqrt(3)/2]], list("STR"), ["4.5 cm"]*3, ["60°"]*3),
        "5": ([[0,0],[5,0],[f_x,f_x*math.tan(rad(55))]], list("DEF"), ["5 cm","",""], ["55°","35°","90°"]),
        "6": ([[0,7],[0,0],[3.2,0]], list("ABC"), ["7 cm","3.2 cm",""], ["","90°",""]),
        "7": ([[4.7,0],[5.2*math.cos(rad(65)),5.2*math.sin(rad(65))],[0,0]], list("PQR"), ["","5.2 cm","4.7 cm"], ["","","65°"]),
        "8": ([[5*math.cos(rad(135)),5*math.sin(rad(135))],[8,0],[0,0]], list("DEF"), ["","8 cm","5 cm"], ["","","135°"])}
    for problem in construction_exercise["problems"]:
        if problem["qNo"] in construction_data:
            points, names, sides, angles = construction_data[problem["qNo"]]
            problem["solutionDiagram"] = {"type":"construction-triangle", "title":"Exercise 12.4 — Question "+problem["qNo"],
                "points":points,"names":names,"sideLabels":sides,"angleLabels":angles}
    for problem in review12["problems"]:
        if problem["qNo"] == "6":
            points = [[-9,8],[-6,10],[-3,8],[-4,5],[-8,5]]
            problem["question"] = "Rotate the shown pentagon through180° counterclockwise about the origin. Its vertices in boundary order are (−9,8),(−6,10),(−3,8),(−4,5),(−8,5)."
            problem["solution"] = "For a180° turn, use (x,y)→(−x,−y). The images are (9,−8),(6,−10),(3,−8),(4,−5),(8,−5), respectively. Plot these points and join them in the same order, closing the pentagon. Both coordinates change sign; each point and its image are equally far from the origin on opposite sides."
            problem["solutionDiagram"] = {"type":"coordinate-panels", "panels":[transformation_panel("Review6: half-turn about the origin",points,lambda x,y:(-x,-y))]}
        elif problem["qNo"] == "10":
            points = [[-9,-4],[-3,-2],[-3,-10],[-9,-10]]
            problem["question"] = "Translate the quadrilateral with vertices (−9,−4),(−3,−2),(−3,−10),(−9,−10) using (x,y)→(x+5,y+8). Write the image coordinates."
            problem["solution"] = "Add5 to each x-coordinate and8 to each y-coordinate: (−9,−4)→(−4,4); (−3,−2)→(2,6); (−3,−10)→(2,−2); (−9,−10)→(−4,−2). Join the four image points in that order. Every vertex moves5 units right and8 units up."
            problem["solutionDiagram"] = {"type":"coordinate-panels", "panels":[transformation_panel("Review10: translate5 right and8 up",points,lambda x,y:(x+5,y+8))]}
    for problem in review12["problems"]:
        if problem["qNo"] == "11":
            triangle = [[-9,7],[-9,2],[-3,2]]
            parallelogram = [[-9,-10],[-4,-10],[-3,-3],[-8,-3]]
            problem["question"] = "Name the shapes and describe the translation to the lighter image. a) Original triangle vertices (−9,7),(−9,2),(−3,2); image vertices (1,−2),(1,−7),(7,−7). b) Original parallelogram vertices (−9,−10),(−4,−10),(−3,−3),(−8,−3); image vertices (2,−3),(7,−3),(8,4),(3,4)."
            problem["solution"] = "a) The shape is a right triangle. From (−9,7) to (1,−2), the displacement is (1−(−9),−2−7)=(10,−9). The other two corresponding vertices give the same displacement. Move10 units right and9 units down: (x,y)→(x+10,y−9). b) The shape is a parallelogram. From (−9,−10) to (2,−3), the displacement is (2−(−9),−3−(−10))=(11,7). All four corresponding vertices have this displacement. Move11 units right and7 units up: (x,y)→(x+11,y+7)."
            problem["solutionDiagram"] = {"type":"coordinate-panels", "panels":[
                transformation_panel("Review11(a): triangle",triangle,lambda x,y:(x+10,y-9)),
                transformation_panel("Review11(b): parallelogram",parallelogram,lambda x,y:(x+11,y+7))]}
    polygon_lessons = {
        "11.2.2": ("11.2.2 Regular and Irregular Polygons", [
            "A regular polygon has all sides equal in length and all interior angles equal in measure. Both conditions are necessary. The textbook examples are a regular quadrilateral (square), a regular hexagon and a regular octagon.",
            "An irregular polygon fails at least one of those conditions: its sides are not all equal, or its angles are not all equal, or both. This does not mean every side and every angle must be different. For example, a non-square rectangle has equal angles but unequal adjacent sides, so it is irregular.",
            "The illustrated irregular examples have5 sides (pentagon),6 sides (hexagon),7 sides (heptagon),8 sides (octagon),9 sides (nonagon) and10 sides (decagon). Count the straight boundary segments, including edges around inward notches."]),
        "11.2.3": ("11.2.3 Convex and Concave Polygons", [
            "A convex polygon has no reflex interior angle; its vertices point outward. For a non-degenerate convex polygon, every interior angle is less than180°. The book illustrates a triangle, pentagon, hexagon, heptagon and octagon.",
            "A concave polygon has at least one reflex interior angle, greater than180° and less than360°. At least one vertex points inward. A dent or inward notch distinguishes the concave example from the convex figures.",
            "Quick Check: can a triangle have a reflex angle? No. A triangle's three positive interior angles total180°, so none can exceed180°. Every non-degenerate triangle is convex."])}
    for index, section in enumerate(chapters[10]["sections"]):
        if section["id"] in polygon_lessons:
            title, paragraphs = polygon_lessons[section["id"]]
            chapters[10]["sections"][index] = make_section(title, paragraphs)
    angle_lessons = {
        "11.3.1": ("11.3.1 Interior Angles of a Polygon", [
            "For a polygon with n sides, the sum of its interior angles is180°(n−2). In a convex polygon, joining one vertex to all non-adjacent vertices divides it into n−2 triangles; each contributes180°.",
            "Source table: triangle n3→180°; quadrilateral n4→360°; pentagon n5→540°; hexagon n6→720°; heptagon n7→900°; octagon n8→1080°.",
            "The illustrated triangle is already one triangle. A diagonal divides the quadrilateral into two triangles, giving2×180°=360°. Two diagonals from one vertex divide the pentagon into three triangles, giving3×180°=540°. A pentagon has five sides; the source sentence saying four is a typo."]),
        "11.3.2": ("11.3.2 Interior Angles of Regular Polygons", [
            "All interior angles of a regular polygon are equal. Divide the sum by n: each interior angle=180°(n−2)/n.",
            "Pentagon:180°(5−2)/5=108°. Hexagon:180°(6−2)/6=120°. Heptagon:180°(7−2)/7=900°/7≈128.57°. Octagon:180°(8−2)/8=135°.",
            "Quick Check: a)9 sides:180°(9−2)/9=140°; b)12 sides:180°(12−2)/12=150°; c)20 sides:180°(20−2)/20=162°.",
            "The total180°(n−2) applies to regular and irregular simple polygons with the same number of sides. Dividing that total by n gives each angle only when all angles are equal."]),
        "11.3.3": ("11.3.3 Measure of Exterior Angles of a Polygon", [
            "Triangle theorem: in triangle PQR, extend QR through R to S. The exterior angle ∠PRS equals the sum of the remote interior angles ∠QPR and ∠PQR.",
            "Proof: ∠QPR+∠PQR+∠PRQ=180°. Also ∠PRQ+∠PRS=180° because QR and RS form a straight line. Equate the two sums and subtract ∠PRQ to obtain ∠QPR+∠PQR=∠PRS.",
            "For a convex pentagon with interior angles a,b,c,d,e, the adjacent exterior angles are180°−a,180°−b,180°−c,180°−d,180°−e. All five interior/exterior pairs total5×180°=900°. Subtract the interior sum540° to obtain exterior sum360°.",
            "For a convex n-sided polygon, the sum of one exterior angle at each vertex is180°n−180°(n−2)=360°. For a regular polygon each exterior angle is360°/n; irregular polygons generally have unequal exterior angles.",
            "Regular triangle:360°/3=120° (the printed180° result is incorrect); square:90°; pentagon:72°; hexagon:60°; heptagon:360°/7≈51.43°; octagon:45°."])}
    chapters[10]["sections"] = [section for section in chapters[10]["sections"] if section["id"] != "11.3.4"]
    for index, section in enumerate(chapters[10]["sections"]):
        if section["id"] in angle_lessons:
            title, paragraphs = angle_lessons[section["id"]]
            chapters[10]["sections"][index] = make_section(title, paragraphs)
    for example in chapters[10]["workedExamples"]:
        if example["id"] == "we-11-polygon-sum":
            example.update(title="Quick Check: interior angles", problem="Calculate each interior angle of regular polygons with9,12 and20 sides.", solution="Use180°(n−2)/n. For9 sides:1260°/9=140°. For12 sides:1800°/12=150°. For20 sides:3240°/20=162°.")
    polygon_exercise = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Exercise 11.3")
    polygon_exercise["problems"][0]["solutionDiagram"] = {"type":"polygon-triangulations", "sides":[7,8,9,10]}
    circle_exercise = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Exercise 11.4")
    for problem in circle_exercise["problems"]:
        if problem["qNo"] == "1":
            problem["solution"] = "a) O is the centre. AB is a diameter because it passes through O. OA,OB and OC are radii. PQ is a chord. The upper region between chord PQ and its short arc is a minor segment; the rest is the major segment. The two arcs between P and Q are the minor and major arcs. AB divides the circle into two semicircles. b) O is the centre; AB and CD are chords. The unlabelled sloping chord passing through O is a diameter. Its two halves are radii, and it divides the circle into two semicircles. The full boundary is the circumference."
        elif problem["qNo"] == "4":
            problem["question"] = "Draw a circle of6 cm and then divide it into two semicircles."
            problem["solution"] = "The question does not specify whether6 cm is the radius or diameter. Taking6 cm as the radius: set a compass to6 cm, draw the circle with centre O, then draw a straight line through O meeting the circle at A and B. AB is a12 cm diameter and splits the circle into equal semicircles. If6 cm was intended as the diameter, set the compass to3 cm instead; the same construction applies. State which measurement you used."
    circle_exercise["problems"].extend([
        {"qNo":"Think Higher 1", "question":"Find ∠BAC if ∠CAD=∠ADC. B,C,D lie on a straight line, ∠ABC=60°, and the exterior angle at D is150°.",
         "solution":"∠ADC=180°−150°=30°. Therefore ∠CAD=30°. In triangle ABD, ∠BAD=180°−60°−30°=90°. Subtract ∠CAD: ∠BAC=90°−30°=60°."},
        {"qNo":"Think Higher 2", "question":"What is the relationship between the number of sides of a polygon and each interior angle, and between the number of sides and each exterior angle?",
         "solution":"For a regular n-sided polygon, each interior angle is180°−360°/n and each exterior angle is360°/n. As n increases, each interior angle increases toward180°, while each exterior angle decreases toward0°. Their sum at a vertex is180°. For an irregular polygon, n determines the interior-angle sum, not each individual angle."},
        {"qNo":"Think Higher 4", "question":"Why is the sum of the exterior angles of a polygon considered360°?",
         "solution":"Walking once around a convex polygon, turn through one exterior angle at each vertex. After returning to the start facing the original direction, the total turn is one full revolution,360°. Algebraically, n adjacent interior/exterior pairs total180°n; subtracting the interior sum180°(n−2) leaves360°."},
        {"qNo":"Think Higher 5", "question":"LM is a straight line through P and Q, and PQRS is a rectangle. Diagonal PR makes37° with PS. Find x between PR and PQ, y between PL and PS, v between RS and RP, w between RP and RQ, u at Q inside the rectangle and z between QR and QM.",
         "solution":"Every rectangle corner is90°. At P, x=90°−37°=53° and y=90°. Since PS∥QR, w=37° by alternate interior angles. At R, v=90°−w=53°. At Q, u=90°; because L,P,Q,M are collinear, z=180°−u=90°."}
    ])
    review11 = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Review Exercise")
    for problem in review11["problems"]:
        if problem["qNo"] == "20":
            problem["qNo"] = "Project"
            problem["question"] = "Math Project: compare quadrilaterals as a whole-class activity. Materials: cut-outs of four-sided shapes, marker and eraser. Place the cut-outs in a large bowl on the teacher's table. Each student randomly picks two shapes, places them on the board, and completes a similarities/differences table. The teacher and class check the comparison."
            problem["solution"] = "Sample comparison: square and non-square rectangle. Similarities: four sides, four right angles, two pairs of parallel opposite sides, equal opposite sides, and diagonals that bisect one another. Differences: the square has four equal sides and four symmetry axes; the non-square rectangle has two longer and two shorter sides and two symmetry axes. Another sample: square and non-square rhombus both have four equal sides and parallel opposite sides; only the square has four right angles. Record the properties of the actual two cut-outs selected."
    for problem in circle_exercise["problems"]:
        if problem["qNo"] == "3":
            problem["solutionDiagram"] = {"type":"circle-construction","mode":"radii","title":"Three radii: OA, OB and OC"}
        elif problem["qNo"] == "4":
            problem["solutionDiagram"] = {"type":"circle-construction","mode":"semicircles","radius":6,"title":"Two semicircles — using radius6 cm"}
    for problem in review11["problems"]:
        if problem["qNo"] in ("18","19"):
            problem["solutionDiagram"] = {"type":"circle-construction","mode":"chords" if problem["qNo"]=="18" else "segments",
                "title":"Two chords away from the centre" if problem["qNo"]=="18" else "Two shaded circular segments", "radius":None if problem["qNo"]=="18" else 7}
    quadrilateral_lessons = {
        "11.1.6": ("11.1.6 Kite", [
            "A kite has two distinct pairs of equal adjacent sides. In the source figure DEFG, DE=EF and DG=GF. The opposite angles between unequal sides are equal: ∠D=∠F.",
            "The four interior angles total360°. In the illustrated kite, E=90°,D=100°,F=100°,G=70°; these add to360°.",
            "Worked example: in kite ABCD, D=80°,B=60° and A=C. Hence2A+80°+60°=360°, so2A=220° and A=C=110°."]),
        "11.1.7": ("11.1.7 Lines of Symmetry in Quadrilaterals", [
            "A symmetry line divides a figure into two halves that match when folded onto one another.",
            "Square: four lines of symmetry—the two diagonals and the horizontal and vertical lines through the centre. The source sentence says six, but the correct count is four.",
            "Non-square rectangle: two symmetry lines, each through the midpoints of a pair of opposite sides. An ordinary parallelogram has no symmetry line; special parallelograms such as rectangles and rhombuses are exceptions.",
            "An ordinary trapezium has no symmetry line. An isosceles trapezium, whose non-parallel sides are equal, has one symmetry line perpendicular to its parallel sides.",
            "A non-square rhombus has two symmetry lines, its diagonals. An ordinary kite has one symmetry line through the vertices where each pair of equal adjacent sides meets.",
            "Activity: use several cut-out quadrilaterals. Fold each in different directions and check whether its halves overlap exactly. Count only folds producing a complete match; record the counts for square4, rectangle2, ordinary parallelogram0, ordinary trapezium0, isosceles trapezium1, rhombus2 and kite1."])}
    for index, section in enumerate(chapters[10]["sections"]):
        if section["id"] in quadrilateral_lessons:
            title, paragraphs = quadrilateral_lessons[section["id"]]
            chapters[10]["sections"][index] = make_section(title, paragraphs)
    symmetry_shapes = {
        "rhombus": {"title":"Rhombus","points":[[150,35],[245,120],[150,205],[55,120]],"axes":[[150,20,150,220],[35,120,265,120]]},
        "trapezium": {"title":"Ordinary trapezium","points":[[75,65],[210,65],[255,180],[75,180]],"axes":[]},
        "isosceles": {"title":"Isosceles trapezium","points":[[100,65],[200,65],[255,180],[45,180]],"axes":[[150,35,150,215]]},
        "parallelogram": {"title":"Ordinary parallelogram","points":[[60,65],[215,65],[255,180],[100,180]],"axes":[]},
        "kite": {"title":"Kite","points":[[150,25],[215,100],[150,215],[85,100]],"axes":[[150,10,150,230]]},
        "square": {"title":"Square","points":[[75,45],[225,45],[225,195],[75,195]],"axes":[[150,25,150,215],[55,120,245,120],[60,30,240,210],[60,210,240,30]]},
        "rectangle": {"title":"Non-square rectangle","points":[[45,70],[255,70],[255,170],[45,170]],"axes":[[150,40,150,200],[25,120,275,120]]}}
    quadrilateral_exercise = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Exercise 11.1")
    for problem in quadrilateral_exercise["problems"]:
        if problem["qNo"] == "7":
            problem["solutionDiagram"] = {"type":"symmetry-panels","panels":[symmetry_shapes[key] for key in ["rhombus","trapezium","isosceles","parallelogram","kite"]]}
        elif problem["qNo"] == "1":
            problem["solutionDiagram"] = {"type":"symmetry-panels","panels":[symmetry_shapes[key] for key in ["square","rectangle","parallelogram","rhombus","trapezium","kite"]]}
    circle_paragraphs = [
        "A circle is the set of points in a plane at the same distance from a fixed point called its centre. The tip of a clock hand traces a circle as the hand turns around its pivot.",
        "Centre: the fixed point equally distant from every point on the circle. In the source radius/diameter figures, A is the centre.",
        "Radius: the distance from the centre to the boundary. AB is a radial segment in the source figure. The plural of radius is radii, and all radii of a circle have the same length.",
        "Diameter: a chord passing through the centre. In the source figure, BC passes through centre A, so BC is a diameter. Diameter=2×radius. A diameter is the longest chord.",
        "Circumference: the total length around the circle's boundary.",
        "Chord: a line segment joining two points on the circumference. PQ and RT are chords in the source illustration; BC is the chord through the centre and is therefore a diameter.",
        "Segment of a circle: a region bounded by a chord and an arc. A non-diameter chord divides the circular region into a smaller minor segment and a larger major segment. In the source figure, chord PQ and minor arc PDQ enclose the shaded minor segment; chord PQ and major arc PEQ enclose the major segment.",
        "Arc: part of the circumference between two endpoints. A minor arc is shorter than a semicircle; a major arc is longer. In the source example, BC denotes the minor arc and BDC the major arc passing through D.",
        "Semicircle: either half produced by a diameter. Diameter BC divides the source circle into two equal semicircles. Each semicircular arc measures180°.",
        "The overview also labels a sector: the region bounded by two radii and their connecting arc. A sector has two straight radius boundaries; a segment has a chord boundary.",
        "Compass activity: choose a centre, set the compass to the required radius and turn it once without changing the opening. Mark and label a radius, diameter, chord, minor/major arcs, semicircle and segment. The exercises and Think Higher questions following this lesson have their own worked answers.",
        "Chapter summary: an angle subtended by a diameter at a point on the circle is a right angle. An isosceles trapezium has equal non-parallel sides. Convex polygons have no reflex interior angles; concave polygons have at least one. Polygons with the same number of sides have the same interior-angle sum, whether regular or irregular. Adjacent interior/exterior angles sum to180°; one exterior angle at each vertex of a convex polygon totals360°."
    ]
    for index, section in enumerate(chapters[10]["sections"]):
        if section["id"] == "11.4":
            chapters[10]["sections"][index] = make_section("11.4 Circle", circle_paragraphs)
    exercise_131["problems"][1]["solutionDiagram"] = {
        "type":"frequency-table", "title":"Bookshop sales read from the graph",
        "headers":["Day","Textbooks","Notebooks","All books"],
        "rows":[["Monday",15,10,25],["Tuesday",20,40,60],["Wednesday",25,20,45],["Thursday",35,35,70]]}
    exercise_131["problems"][0]["solutionDiagram"] = {
        "type":"grouped-bars","title":"New buildings constructed","xLabel":"Month","yLabel":"Number of buildings",
        "yMax":40,"step":5,"labels":["July","August","September","October","November"],
        "series":[{"name":"Commercial","values":[5,35,15,10,5]},{"name":"Residential","values":[10,15,5,5,20]}]}
    exercise_131["problems"][1]["diagram"] = {
        "type":"grouped-bars","title":"Bookshop sale","xLabel":"Day","yLabel":"Number of books sold",
        "yMax":45,"step":5,"labels":["Monday","Tuesday","Wednesday","Thursday"],
        "series":[{"name":"Textbooks","values":[15,20,25,35]},{"name":"Notebooks","values":[10,40,20,35]}]}
    line_exercise = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.2")
    line_charts = {
        "1": ("Toy production",["Jan","Feb","Mar","Apr","May","Jun"],[2000,3000,1500,6000,3500,5000],7000,1000,"Month","Number of toys"),
        "3": ("Visitors to Shahi Qila",["March","April","May","June","July"],[6000,8500,7000,9000,6500],10000,1000,"Month","Number of visitors"),
        "4": ("Temperature through the day",["8 a.m.","10 a.m.","12 p.m.","2 p.m.","4 p.m.","6 p.m."],[16.5,20.2,28.8,32.4,30.7,26.6],35,5,"Time","Temperature (°C)")}
    for problem in line_exercise["problems"]:
        title, labels, values, maximum, step, x_label, y_label = line_charts[problem["qNo"]]
        problem["diagram" if problem["qNo"]=="1" else "solutionDiagram"] = {
            "type":"category-line","title":title,"labels":labels,"series":[{"name":title,"values":values}],
            "yMax":maximum,"step":step,"xLabel":x_label,"yLabel":y_label}
    pie_exercise = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.3")
    pie_data = {
        "1": ("Monthly budget (rupees)",["Food","Education","Conveyance","Savings","Miscellaneous"],[3150,1950,21100,2400,11200]),
        "2": ("Junaid's savings (rupees)",["Week1","Week2","Week3","Week4"],[45,56,65,75]),
        "3": ("Favourite subjects (students)",["Maths","History","English","Urdu"],[423,123,222,86]),
        "4": ("Listed transport observations (845 students)",["Bus","Cycle","Bike","Car","On foot"],[198,180,240,27,200])}
    for problem in pie_exercise["problems"]:
        if problem["qNo"] in pie_data:
            title, labels, values = pie_data[problem["qNo"]]
            problem["solutionDiagram"] = {"type":"pie-sectors","title":title,"labels":labels,"values":values}
    # Printed p.269: retain the open-ended class project separately from Q1–Q12.
    statistics_review = next(ex for ex in unit13["exercises"] if ex["title"] == "Review Exercise")
    statistics_review["problems"].append({
        "qNo": "Project",
        "question": "Math Project (printed page 269). Materials: chart papers, graph papers and glue stick/thumb pins. Work in groups. Assign each member a task, such as organizing data using graphs, calculating the mean, median and mode, or drawing a frequency-distribution chart and histogram. Each group presents its work and explains which charts suit which kinds of data and which measure of central tendency is more suitable for the collected values.",
        "solution": "Sample project only: collect ten measured lengths in centimetres: 12, 14, 14, 15, 16, 16, 16, 18, 19, 20. Your group's actual observations may differ. Step 1 — organize the observations in ascending order as shown. Step 2 — make equal-width classes: 10 ≤ length < 15 has frequency 3; 15 ≤ length < 20 has frequency 6; 20 ≤ length < 25 has frequency 1. Total frequency = 3 + 6 + 1 = 10. Step 3 — draw the histogram with touching bars, class boundaries 10, 15, 20, 25 on the horizontal axis and frequency on the vertical axis; bar heights are 3, 6, 1. Step 4 — use the original observations for the exact mean: sum = 12 + 14 + 14 + 15 + 16 + 16 + 16 + 18 + 19 + 20 = 160 cm; mean = 160 ÷ 10 = 16 cm. Step 5 — there are ten ordered observations, so median = (5th + 6th observations) ÷ 2 = (16 + 16) ÷ 2 = 16 cm. Step 6 — 16 occurs three times, more than any other length, so mode = 16 cm. Presentation: a histogram suits grouped continuous measurements; a bar chart suits separate categories; a pie chart shows parts of one total; a line graph shows change over time. Here all three measures are 16 cm, so they give the same central value. For data with extreme observations, the median is often more representative than the mean; for a most-common category, use the mode. Explain your choice using your own collected data.",
        "diagram": {"type":"frequency-table", "title":"Sample project: measured lengths", "headers":["Length (cm)","Frequency"], "rows":[["10 ≤ length < 15",3],["15 ≤ length < 20",6],["20 ≤ length < 25",1],["Total",10]]},
        "solutionDiagram": {"type":"histogram", "title":"Sample project: length distribution", "xLabel":"Length (cm)", "yLabel":"Frequency", "bars":[{"lower":10,"upper":15,"frequency":3},{"lower":15,"upper":20,"frequency":6},{"lower":20,"upper":25,"frequency":1}]}
    })
    # Review p.268, checked against enlarged PDF index137 (right page).
    review_problems = {p["qNo"]: p for p in statistics_review["problems"]}
    review_problems["2"]["question"] = "A bakery sold 84 chicken rolls on Monday, 96 on Tuesday, 66 on Wednesday, 48 on Thursday and 54 on Friday. Draw a line graph for the given data."
    review_problems["2"]["solutionDiagram"] = {"type":"category-line","title":"Chicken rolls sold by the bakery","labels":["Monday","Tuesday","Wednesday","Thursday","Friday"],"series":[{"name":"Chicken rolls","values":[84,96,66,48,54]}],"yMax":108,"step":12,"xLabel":"Day","yLabel":"Chicken rolls sold"}
    review_problems["4"]["question"] = "Following are the runs Shahid Afridi made in a local match in 3 overs. Represent them in a frequency table: 2, 0, 4, 4, 0, 6, 6, 6, 4, 2, 4, 2, 6, 6, 2, 4, 4, 4."
    review_problems["4"]["solution"] = "Count each observation once. Score 0 occurs twice, score 2 occurs four times, score 4 occurs seven times and score 6 occurs five times. Frequencies total 2 + 4 + 7 + 5 = 18, matching the 18 listed balls in three overs."
    review_problems["4"]["solutionDiagram"] = {"type":"frequency-table","title":"Runs per ball","headers":["Runs","Frequency"],"rows":[[0,2],[2,4],[4,7],[6,5],["Total",18]]}
    review_problems["5"]["solution"] = "(a) Count each value in the 23 observations: 2 occurs 5 times; 3 occurs 7 times; 4 occurs 6 times; 5 occurs 2 times; 6 occurs 3 times. Check: 5 + 7 + 6 + 2 + 3 = 23. (b) In the 22 observations: 4 occurs 2 times; 5 occurs 4 times; 6 occurs 7 times; 7 occurs 5 times; 8 occurs 2 times; 9 occurs 2 times. Check: 2 + 4 + 7 + 5 + 2 + 2 = 22. A zero in the combined table means that value does not appear in that dataset."
    review_problems["5"]["solutionDiagram"] = {"type":"frequency-table","title":"Frequency tables for (a) and (b)","headers":["Value","Frequency (a)","Frequency (b)"],"rows":[[2,5,0],[3,7,0],[4,6,2],[5,2,4],[6,3,7],[7,0,5],[8,0,2],[9,0,2],["Total",23,22]]}
    review_problems["6"]["question"] = "The following marks out of 25 were obtained by 30 students. Represent them in a frequency table: 20, 6, 23, 19, 9, 14, 15, 3, 1, 12, 10, 20, 13, 3, 17, 10, 11, 6, 21, 9, 6, 10, 9, 4, 5, 1, 5, 11, 7, 24."
    review_problems["6"]["solutionDiagram"] = {"type":"frequency-table","title":"Marks out of 25","headers":["Mark","Number of students"],"rows":[[1,2],[3,2],[4,1],[5,2],[6,3],[7,1],[9,3],[10,3],[11,2],[12,1],[13,1],[14,1],[15,1],[17,1],[19,1],[20,2],[21,1],[23,1],[24,1],["Total",30]]}
    review_problems["7"]["solution"] = "A full circle is 360°, so multiply each percentage by 360 ÷ 100 = 3.6 to obtain its sector angle. Brick: 15 × 3.6 = 54°; cement: 20 × 3.6 = 72°; steel: 10 × 3.6 = 36°; labour: 25 × 3.6 = 90°; miscellaneous: 30 × 3.6 = 108°. Check: 54 + 72 + 36 + 90 + 108 = 360°. Each 1% of Rs 1,800,000 is Rs 18,000. The respective costs are Rs 270,000, Rs 360,000, Rs 180,000, Rs 450,000 and Rs 540,000; these sum to Rs 1,800,000. Miscellaneous has the largest share (30%); steel has the smallest (10%). Labour and miscellaneous together account for 55% of the cost."
    review_problems["7"]["solutionDiagram"] = {"type":"pie-sectors","title":"House construction expenditure (%)","labels":["Brick","Cement","Steel","Labour","Miscellaneous"],"values":[15,20,10,25,30]}
    review_problems["3"]["solutionDiagram"] = {"type":"horizontal-grouped-bars","title":"Members collecting flood funds","labels":["Group A","Group B","Group C","Group D","Group E"],"series":[{"name":"Male","values":[20,30,18,15,25]},{"name":"Female","values":[25,30,25,35,25]}],"xMax":40,"step":5,"xLabel":"Number of members"}
    review_problems["3"]["solution"] = "Draw a horizontal number scale from 0 to 40, with a division every 5 members. List Groups A–E down the vertical axis. Draw two horizontal bars of equal thickness for each group, starting at zero: Group A male 20, female 25; Group B male 30, female 30; Group C male 18, female 25; Group D male 15, female 35; Group E male 25, female 25. The 18-member bar ends between 15 and 20. Use different colours for male and female members and include a legend. Groups B and E have equal male and female membership; Group D has the most female members (35)."
    review_problems["1"]["question"] = "Encircle the correct option (printed pp.267–268).\n(a) Which graph/chart is suitable for showing data changing over time? (i) Bar (ii) Pie (iii) Line (iv) Picture.\n(b) The term discrete means: (i) Joined (ii) Connected (iii) Distinct (iv) Combined.\n(c) How likely something is to happen is known as: (i) Mean (ii) Probability (iii) Certainty (iv) Surety.\n(d) The possible result of a random experiment is called: (i) An outcome (ii) An experiment (iii) A median (iv) An average.\n(e) When there is a 50% chance of an event, i.e. 1/2, the event is said to be: (i) Certain (ii) Impossible (iii) Sure (iv) Equally likely.\n(f) The probability of an event is any number from: (i) 0 to 10 (ii) 1 to 10 (iii) 0 to 1 (iv) 0 to 1/2.\n(g) The number of times a specific observation occurs in collected data is called its: (i) Data (ii) Frequency (iii) Raw materials (iv) Grouped data.\n(h) The ___ distribution organizes information in the form of a table: (i) Frequency (ii) Pie (iii) Range (iv) Class interval."
    review_problems["1"]["solution"] = "(a) (iii) Line: successive points show changes over time. (b) (iii) Distinct: discrete values are separate values. (c) (ii) Probability: it measures the likelihood of an event. (d) (i) An outcome: one possible result of an experiment. (e) (iv) Equally likely is the intended option: more precisely, the event and its complement each have probability 1/2, so happening and not happening are equally likely. (f) (iii) 0 to 1, including both endpoints: 0 is impossible and 1 is certain. (g) (ii) Frequency: count how often that observation appears. (h) (i) Frequency: a frequency-distribution table lists values or classes alongside their frequencies."
    probability_exercise = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.7")
    probability_exercise["problems"].append({"qNo":"Think Higher", "question":"In a match between Team A and Team B, Team A has a 25% chance of winning. Describe the complementary event (printed p.267).", "solution":"Let E be the event that Team A wins. Its complement is that Team A does not win. P(not E) = 1 − P(E) = 1 − 0.25 = 0.75 = 75%. If the match must have exactly one winner, this means Team B wins. If a draw or tie is possible, those outcomes also belong to Team A not winning; therefore Team B winning alone need not have probability 75%."})
    unit13["sections"].append(make_section("Summary and Vocabulary", [
        "Printed p.267 summary: graphs display data pictorially and can show a relationship between two quantities. A pie graph uses sectors of a circle to represent parts of a whole. Discrete means distinct or separate. A sample space contains all possible outcomes of an experiment. A favourable outcome is one belonging to the event under consideration. Every probability lies between 0 and 1 inclusive.",
        "Vocabulary — histogram: adjoining bars displaying frequencies over numerical intervals; discrete data: separate countable values; continuous data: measurements that may take any value within an interval; grouped data: observations organized into classes; ungrouped data: observations listed individually or by individual value.",
        "Mean: sum of observations divided by their number. Median: middle ordered observation, or the mean of the two middle observations. Mode: most frequently occurring value. Frequency distribution: a table listing values or classes and their frequencies.",
        "Probability: numerical measure of likelihood. Certain event: probability 1. Impossible event: probability 0. Complement: all outcomes in the sample space that are not in the event; its probability is 1 minus the event's probability."
    ]))
    probability_problems = {p["qNo"]:p for p in probability_exercise["problems"]}
    probability_problems["2"]["diagram"] = {"type":"number-spinner","title":"Exercise 13.7: eight equal spinner sectors","labels":[2,6,3,2,4,5,1,3]}
    probability_problems["2"]["solutionDiagram"] = {"type":"frequency-table","title":"Events and their complements","headers":["Event","Probability","Complementary event","Probability"],"rows":[["Number < 3","3/8","Number ≥ 3","5/8"],["Not 5","7/8","5","1/8"],["Number < 6","7/8","6","1/8"],["Odd","1/2","Even","1/2"],["Prime","5/8","Not prime (1, 4, 6)","3/8"],["Even","1/2","Odd","1/2"],["10","0","Not 10","1"]]}
    probability_problems["1"]["solution"] += " Green and red are equally likely colours because each has 4 of the 20 marbles, so each has probability 1/5. Among the five events listed in parts (a)–(e), none has probability 1/2 and no two have equal probabilities. Thus none of these listed events is equally likely to its own complement."
    probability_problems["4"]["solution"] += " Events (c) and (d) are impossible. Their complements, not choosing 9 and choosing a number, are certain. None of the five requested events itself is certain."
    probability_lessons = {
        "13.7": make_section("13.7 Probability", [
            "Probability measures how likely an event is to happen. This lesson recalls experiments, outcomes, sample spaces and events before calculating their probabilities.",
            "Experiment or trial: a repeatable process with well-defined possible results. A random experiment has an uncertain result. Examples in the book are tossing a coin, rolling a die, spinning a spinner and picking an object from a group without looking.",
            "Outcome: one possible result of a random experiment. For example, a coin can land heads or tails, and a die can show 1, 2, 3, 4, 5 or 6.",
            "Sample space: the set of all possible outcomes. For a die, S = {1, 2, 3, 4, 5, 6}. For a coin, S = {head, tail}. It acts as the universal set for the experiment's outcomes.",
            "Event: an outcome or collection of outcomes. Getting a head when tossing a coin and getting 3 when rolling a die are examples. A favourable or desired outcome is an outcome belonging to the event being considered.",
            r"For equally likely outcomes, \(P(E)=\frac{\text{number of favourable outcomes}}{\text{total number of possible outcomes}}\). Count individual outcomes consistently in both numerator and denominator."
        ]),
        "13.7.1": make_section("13.7.1 Types of Events", [
            "Equally likely and not equally likely outcomes: Ali's pouch contains 4 red, 5 blue and 1 green pencil. There are 4 + 5 + 1 = 10 pencils. Assume every pencil has the same chance of being selected without looking.",
            r"There are 5 blue pencils, so \(P(\text{blue})=\frac{5}{10}=\frac12\). There are 4 + 1 = 5 non-blue pencils, so \(P(\text{not blue})=\frac{5}{10}=\frac12\). Picking blue and not picking blue are equally likely: each has a 50% chance. The three colours themselves are not equally likely: red has probability 4/10, blue 5/10 and green 1/10.",
            r"Certain event: every object in the pouch is a pencil, so \(P(\text{pencil})=\frac{10}{10}=1\), a 100% chance. Impossible event: no object is a non-pencil, so \(P(\text{not a pencil})=\frac{0}{10}=0\), a 0% chance.",
            "Probability line: probabilities lie from 0 to 1 inclusive. Mark 0 as impossible, 1/2 as equally likely to happen or not happen, and 1 as certain. For randomly picking a blue marble, a bag containing no blue marbles gives 0; a bag with half blue gives 1/2; an all-blue bag gives 1.",
            "Example 1: Umar selects one of the number cards 2, 4, 6, 8, 10, 12. Every card is even, so P(even) = 6/6 = 1 and choosing even is certain. None is odd, so P(odd) = 0/6 = 0 and choosing odd is impossible.",
            "Complement of an event: all outcomes in the sample space that are not in the event. An event and its complement cannot occur together and together cover every possible outcome. Merely being unable to occur together is not sufficient for events to be complementary.",
            r"Thus \(P(E^c)=1-P(E)\) and \(P(E)+P(E^c)=1\).",
            r"Sara's experiment: choose a number at random from {3, 4, 6, 7, 8, 10}. (a) Even numbers are {4, 6, 8, 10}, so \(P(\text{even})=\frac46=\frac23\). The complement is {3, 7}, giving \(P(\text{not even})=1-\frac23=\frac13\).",
            r"(b) Factors of 12 present in the sample space are {3, 4, 6}. Therefore \(P(\text{factor of 12})=\frac36=\frac12\). The other numbers {7, 8, 10} form the complement, so \(P(\text{not a factor of 12})=1-\frac12=\frac12\). The printed solution mistakenly refers to an even number in this factor calculation; the event here is being a factor of 12."
        ])}
    unit13["sections"] = [probability_lessons.get(section["id"], section) for section in unit13["sections"]]
    averages_exercise = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.6")
    averages = {p["qNo"]:p for p in averages_exercise["problems"]}
    averages["4"]["solution"] = r"For grouped data, use each class midpoint as its representative length. Midpoint \(m=\frac{\text{lower limit}+\text{upper limit}}2\). This gives 5.5, 15.5, 25.5, 35.5 and 45.5 metres. Multiply each midpoint by its frequency: 2×5.5=11; 7×15.5=108.5; 10×25.5=255; 3×35.5=106.5; 1×45.5=45.5. The total frequency is 2+7+10+3+1=23 wires and the weighted total is 526.5 metres. Hence the estimated mean length is \(\bar{x}=\frac{\sum fm}{\sum f}=\frac{526.5}{23}\approx22.89\text{ m}\). This is a grouped-data estimate because individual wire lengths are not supplied."
    averages["4"]["solutionDiagram"] = {"type":"frequency-table","title":"Wire lengths: mean calculation","headers":["Length (m)","Frequency f","Midpoint m","f × m"],"rows":[["1–10",2,5.5,11],["11–20",7,15.5,108.5],["21–30",10,25.5,255],["31–40",3,35.5,106.5],["41–50",1,45.5,45.5],["Total",23,"—",526.5]]}
    averages["5"]["solution"] = r"The class midpoints are (1+3)/2=2, (3+5)/2=4, (5+7)/2=6 and (7+9)/2=8 years. Products of midpoint and frequency are 12×2=24, 22×4=88, 27×6=162 and 19×8=152. Total employees = 12+22+27+19=80; weighted total = 24+88+162+152=426 years. Therefore \(\bar{x}=\frac{426}{80}=5.325\text{ years}\). This is the mean estimated from the grouped data; it is approximately 5.33 years."
    averages["5"]["solutionDiagram"] = {"type":"frequency-table","title":"Job duration: mean calculation","headers":["Duration (years)","Employees f","Midpoint m","f × m"],"rows":[["1–3",12,2,24],["3–5",22,4,88],["5–7",27,6,162],["7–9",19,8,152],["Total",80,"—",426]]}
    averages["7"]["solution"] = r"Multiply each mark by its assigned weight: Mathematics 92×5=460; English 75×4=300; Islamiat 80×3=240; Science 86×4=344. Add weighted marks: 460+300+240+344=1344. Add weights: 5+4+3+4=16. The weighted mean is \(\frac{\sum wx}{\sum w}=\frac{1344}{16}=84\). Divide by the total weight, not by the four subjects."
    averages["7"]["solutionDiagram"] = {"type":"frequency-table","title":"Weighted marks","headers":["Subject","Mark x","Weight w","w × x"],"rows":[["Mathematics",92,5,460],["English",75,4,300],["Islamiat",80,3,240],["Science",86,4,344],["Total","—",16,1344]]}
    central_lessons = {
        "13.6.2": make_section("13.6.2 Mean of Grouped Data", [
            "When only grouped observations are available, represent each class by its midpoint. Multiply each midpoint by the class frequency, add these products, and divide by the total frequency. This estimates the mean because the individual observations within each class are unknown.",
            r"Midpoint \(m=\frac{\text{lower class limit}+\text{upper class limit}}2\); grouped mean \(\bar{x}\approx\frac{\sum fm}{\sum f}\). The midpoint obtained from the two class boundaries is the same as that obtained from the two limits.",
            "Source example (pp.259–260): classes 25–39, 40–54, 55–69, 70–84, 85–99 have frequencies 3, 4, 8, 9, 6. Their midpoints are (25+39)/2=32, (40+54)/2=47, (55+69)/2=62, (70+84)/2=77 and (85+99)/2=92.",
            "Multiply: 32×3=96; 47×4=188; 62×8=496; 77×9=693; 92×6=552. Add products: 96+188+496+693+552=2025. Add frequencies: 3+4+8+9+6=30. Estimated mean=2025/30=67.5. The printed table mistakenly gives 47×4 as 96; the correct product is 188, which agrees with the printed total 2025."
        ]),
        "13.6.4": make_section("13.6.4 Mode", [
            "The mode is the value occurring most frequently. Count how often each distinct value occurs, then find the value or values with the greatest frequency.",
            "Example 1(i): 3, 4, 4, 5, 5, 5, 5, 6, 7, 7. The frequencies are 3:1, 4:2, 5:4, 6:1, 7:2. The greatest frequency is 4, belonging to the value 5. Therefore the mode is 5.",
            "Example 1(ii): 7, 8, 8, 9, 10, 10, 11, 12. Both 8 and 10 occur twice; every other value occurs once. Therefore there are two modes, 8 and 10. Such data are called bimodal."
        ]),
        "13.6.5": make_section("13.6.5 Appropriate Measure of Central Tendency", [
            "The arithmetic mean uses every observation and is useful when the data have no extreme values that distort the average. The median is the middle of the ordered data and is often more representative when there are extreme values. The mode identifies the most frequent observation and is useful for describing popularity or demand.",
            "Source example (p.262): numbers of a popular ice-cream flavour sold during ten days are 85, 96, 76, 108, 85, 80, 100, 85, 70, 95. Find the mean, median and mode, then compare which measure best represents the data.",
            "Mean: the total is 85+96+76+108+85+80+100+85+70+95=880. Divide by ten days: 880/10=88 sales per day.",
            "Order the observations: 70, 76, 80, 85, 85, 85, 95, 96, 100, 108. There are ten observations, so median=(5th+6th)/2=(85+85)/2=85. The value 85 occurs three times, more than any other value; mode=85.",
            "Comparison: the mean describes average daily sales (88), the median describes the middle sales count (85), and the mode gives the most common daily count (85). The source discussion highlights popularity, so the mode answers the most-common-value question; the median gives the same number here. A mean does not need to be one of the observed values to be useful. The book's concluding reference to mean and median conflicts with its preceding discussion of median and mode. Choose the measure according to the question being answered."
        ])}
    unit13["sections"] = [central_lessons.get(section["id"], section) for section in unit13["sections"]]
    mean_paragraphs = [
        "The arithmetic mean is found by adding all observations and dividing by the number of observations. It uses every value in the dataset.",
        r"If the observations are represented by x and there are n of them, \(\bar{x}=\frac{\sum x}{n}\). The symbol \(\sum x\), read as sum of x, means the total of all observations. Rearranging gives \(\sum x=n\bar{x}\): total = number of observations × mean.",
        r"Example 1: find the mean of 1, 6, 8, 9, 7, 5. There are n=6 observations. Their sum is 1+6+8+9+7+5=36. Hence \(\bar{x}=\frac{36}{6}=6\).",
        "Example 2: the average weight of four boys is 24 kg. With a fifth boy included, the mean becomes 24.6 kg. Find the fifth boy's weight.",
        r"The four boys' total weight is 4×24=96 kg. Let the fifth boy weigh y kg. The five boys' total is 96+y kg, so \(24.6=\frac{96+y}{5}\). Multiply both sides by 5: 123=96+y. Subtract 96: y=27 kg. Check: (96+27)/5=123/5=24.6 kg. The printed initial n=6 is a typo: there are four boys initially and five after the addition."
    ]
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.6.1":
            unit13["sections"][index] = make_section("13.6.1 Arithmetic Mean", mean_paragraphs)
        elif section["id"] == "13.6":
            unit13["sections"][index] = make_section("13.6 Measures of Central Tendency", ["Organizing data in a frequency distribution helps us see patterns and trends. Sometimes we need one representative value to describe the dataset. Such a value is called an average or a measure of central tendency.", "This section introduces three measures: arithmetic mean, median and mode. They describe different aspects of the data, so the choice depends on what we want to find out."])
    examples13 = unit13["workedExamples"]
    for example in examples13:
        if example["id"] == "we-13-6b":
            example["solution"] = mean_paragraphs[-1]
        elif example["id"] == "we-13-7":
            example["problem"] = "Umar chooses a card from {2,4,6,8,10,12}. Classify choosing even and choosing odd as certain or impossible. Sara then chooses a number from {3,4,6,7,8,10}; find P(even), P(factor of 12) and their complements."
            example["solution"] = "Umar: all six cards are even, so P(even)=6/6=1 (certain); none is odd, so P(odd)=0/6=0 (impossible). Sara: even outcomes {4,6,8,10} give P(even)=4/6=2/3; the complement {3,7} gives P(not even)=2/6=1/3. Factors of12 in her set are {3,4,6}, giving P(factor of12)=3/6=1/2; the complement {7,8,10} also has probability3/6=1/2."
    median_example = {"id":"we-13-6-median","title":"Median — Example 1 (pp.260–261)","problem":"Find the median: (i) 6,3,8,14,12,10,9,14,16; (ii) 10,12,14,16,18,20.","solution":"(i) Arrange in ascending order: 3,6,8,9,10,12,14,14,16. There are9 observations, so the middle position is (9+1)/2=5. The fifth value is10; median=10. (ii) The six values are already ordered. The middle positions are3 and4, with values14 and16. Median=(14+16)/2=30/2=15."}
    examples13.insert(next(i for i,e in enumerate(examples13) if e["id"]=="we-13-6d"),median_example)
    examples13.insert(next(i for i,e in enumerate(examples13) if e["id"]=="we-13-7"),{"id":"we-13-6-comparison","title":"Choosing a measure — Example 1 (p.262)","problem":"The numbers of a popular ice-cream flavour sold in ten days are85,96,76,108,85,80,100,85,70,95. Calculate mean, median and mode, and compare their suitability.","solution":"Total=880; mean=880/10=88. Ordered values:70,76,80,85,85,85,95,96,100,108. Median=(85+85)/2=85. Since85 occurs three times, mode=85. The mean answers average daily sales; the mode answers the most common daily sales count; the median gives the middle sales count. Median and mode coincide here. The mean remains valid even though88 is not an observed daily count."})
    histogram_paragraphs = [
        "A histogram represents a frequency distribution using adjoining vertical rectangular bars. Put class boundaries on the horizontal axis and frequency on the vertical axis. For equal-width classes, the height of each bar is proportional to its frequency. There are no gaps between adjacent intervals.",
        "Example 1 (p.256): maximum temperatures in Lahore for the 31 days of August 2021, in °C: 35,38,38,38,40,42,40,45,46,48,46,43,42,42,38,39,38,45,45,46,48,50,49,50,49,45,49,46,45,48,51. Prepare a frequency distribution with class width3°C and draw a histogram.",
        "The smallest listed temperature is35°C and the largest is51°C. The book prints52 as the largest value, but52 is the upper limit of the final chosen class. Use six classes:35–37,38–40,41–43,44–46,47–49,50–52. Their continuous boundaries are34.5–37.5,37.5–40.5,40.5–43.5,43.5–46.5,46.5–49.5,49.5–52.5.",
        "Tallying the original observations gives frequencies1,8,4,9,6,3. Check:1+8+4+9+6+3=31 days. Draw touching bars of width3°C and these heights. Label the horizontal axis Temperature (°C) and the vertical axis Number of days.",
        "Example 2 (p.257): the women's height histogram has class boundaries58.5–60.5,60.5–62.5,62.5–64.5,64.5–66.5 inches and frequencies10,12,8,4. (i) There are four classes. (ii) Class width=60.5−58.5=2 inches. (iii) Total women=10+12+8+4=34. (iv) The largest frequency is12, in the60.5–62.5 inch class. The second column of the printed solution table contains frequencies, despite its incorrect Class Boundaries heading.",
        "For these examples all class widths are equal. If unequal-width classes are used, histogram areas must represent frequencies; use frequency density (frequency divided by class width) as bar height."
    ]
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.5.1":
            unit13["sections"][index] = make_section("13.5.1 Construction of Histogram", histogram_paragraphs)
    for example in unit13["workedExamples"]:
        if example["id"] == "we-13-5a":
            example["problem"] = histogram_paragraphs[1]
            example["solution"] = " ".join(histogram_paragraphs[2:4])
            example["diagram"] = {"type":"histogram","title":"Lahore maximum temperatures, August2021","xLabel":"Temperature (°C)","yLabel":"Number of days","bars":[{"lower":34.5+3*i,"upper":37.5+3*i,"frequency":f} for i,f in enumerate([1,8,4,9,6,3])]}
        elif example["id"] == "we-13-5b":
            example["problem"] = "The histogram shows women's heights in inches. (i) What is the total number of classes? (ii) What is the class width? (iii) What is the total number of women? (iv) Which class has maximum frequency?"
            example["solution"] = histogram_paragraphs[4]
            example["diagram"] = {"type":"histogram","title":"Heights of women","xLabel":"Height (inches)","yLabel":"Number of women","bars":[{"lower":58.5+2*i,"upper":60.5+2*i,"frequency":f} for i,f in enumerate([10,12,8,4])]}
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.5":
            unit13["sections"][index] = make_section("13.5 Histogram", [
                "A histogram displays grouped numerical data. Mark class intervals or boundaries along the horizontal axis and frequencies along the vertical axis. For the equal-width classes used here, draw adjoining rectangular bars whose heights equal the corresponding frequencies. The width of each bar represents the width of its class.",
                "Bar chart versus histogram — categories: a bar chart can compare categories such as favourite fruits or students' names. A histogram represents numerical intervals, such as heights or temperatures.",
                "Order: histogram intervals must stay in numerical order. Bar-chart categories may be reordered when their meaning permits it; days or other ordered categories should retain their meaningful sequence.",
                "Spacing: bar-chart bars have equal gaps to separate categories. Histogram bars touch at their shared class boundaries. A class with zero observations has a zero-height bar; keep its interval on the axis rather than removing it.",
                "For equal-width intervals, higher histogram bars mean greater frequency. For unequal-width intervals, use frequency density so that bar area represents frequency."
            ])
    frequency_exercise = next(ex for ex in unit13["exercises"] if ex["title"] == "Exercise 13.4")
    for problem in frequency_exercise["problems"]:
        if problem["qNo"] == "6":
            problem["question"] = "The following marks out of100 were obtained by24 students. Make a grouped frequency table:55,70,57,73,55,59,64,72,60,48,58,54,69,51,63,78,75,64,65,57,71,78,76,68."
            problem["solutionDiagram"] = {"type":"frequency-table","title":"One valid grouping of the24 marks","headers":["Marks","Observations in the class","Frequency"],"rows":[["45–54","48,51,54",3],["55–64","55,55,57,57,58,59,60,63,64,64",10],["65–74","65,68,69,70,71,72,73",7],["75–84","75,76,78,78",4],["Total","",24]]}
        elif problem["qNo"] == "7":
            problem["diagram"] = {"type":"frequency-table","title":"Marks obtained in Mathematics","headers":["Marks","Number of students"],"rows":[["55–69",24],["70–84",10],["85–99",15]]}
    grouped_paragraphs = [
        "Range is the largest observation minus the smallest. Class intervals group observations into ranges. Each has a lower limit and an upper limit. Choose intervals that cover every observation without overlap. For these whole-number data, inclusive classes32–37 and38–43 have boundary width6, not5.",
        "Example1 (p.252): the weekly savings in rupees of35 children are32,33,33,34,35,36,37;38,38,39,40,41,42,43;44,47,47,48,48,48,49;49,49,50,50,50,50,50;50,51,51,51,51,51,51. Make a grouped frequency distribution.",
        "Minimum=32, maximum=51, range=51−32=19. The book chooses four classes32–37,38–43,44–49,50–55. Their frequencies are7,7,9,12, totalling35. Its intermediate calculation19/4=4.75 rounded to5 does not match the actual boundary width6 of these chosen classes. Retain the printed classes when reproducing its table.",
        "Class32–37 contains32,33,33,34,35,36,37. Class38–43 contains38,38,39,40,41,42,43. Class44–49 contains44,47,47,48,48,48,49,49,49. Class50–55 contains six50s and six51s.",
        "Conclusions: the largest group has12 children saving Rs50–55; it is not a majority of all35. There are7+7=14 children saving Rs32–43 (the printed conclusion says seven). There are7+7+9=23 saving less than Rs50 and9 saving Rs44–49.",
        "Activity: collect your classmates' heights, order them, choose suitable non-overlapping intervals, make a grouped frequency table and share the findings with your teacher. Answers depend on actual measurements. Check that every measurement is counted exactly once and frequencies sum to the class size. For large datasets, tally directly without listing every observation in each class.",
        "Class boundaries lie halfway between consecutive classes' adjacent limits. For whole-number limits57 and58, the common boundary is(57+58)/2=57.5. Half the gap is(58−57)/2=0.5; this is the adjustment, not the boundary itself.",
        "Source boundary example (p.253):53–57 becomes52.5–57.5 with frequency4;58–62 becomes57.5–62.5 with frequency9;63–67 becomes62.5–67.5 with frequency9;68–72 becomes67.5–72.5 with frequency13. Frequencies total35. Subtract0.5 from each lower limit and add0.5 to each upper limit; adjacent boundaries meet without gaps."
    ]
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.4.3":
            unit13["sections"][index] = make_section("13.4.3 Grouped Frequency Distribution and Class Boundaries", grouped_paragraphs)
    for example in unit13["workedExamples"]:
        if example["id"] == "we-13-4b":
            example["problem"] = grouped_paragraphs[1]
            example["solution"] = " ".join(grouped_paragraphs[2:5])
            example["diagram"] = {"type":"frequency-table","title":"Weekly savings of35 children","headers":["Savings (Rs)","Frequency"],"rows":[["32–37",7],["38–43",7],["44–49",9],["50–55",12],["Total",35]]}
        elif example["id"] == "we-13-4c":
            example["solution"] = " ".join(grouped_paragraphs[6:])
            example["diagram"] = {"type":"frequency-table","title":"Class boundaries","headers":["Class interval","Class boundaries","Frequency"],"rows":[["53–57","52.5–57.5",4],["58–62","57.5–62.5",9],["63–67","62.5–67.5",9],["68–72","67.5–72.5",13],["Total","",35]]}
    data_lessons = {
        "13.4": make_section("13.4 Data and its Presentation", ["Collecting, organizing and presenting data helps us understand information. This section introduces raw data, discrete and continuous data, and frequency distributions."]),
        "13.4.1": make_section("13.4.1 Data and Data Collection", [
            "Raw data are information collected before organization or arrangement. Data collection is the process of gathering that information.",
            "Discrete data have separate, countable possible values. The book's examples are the number of Grade7 students, the population of Islamabad, the number of players in a match, the number of animals in a zoo and the number of fans in a school. These are whole-number counts.",
            "Continuous data come from measurements that can take any value within a range. Examples are Grade7 students' weights, the volume of a liquid, a person's height and a city's temperature. Measurement precision may limit how many decimal places we record.",
            "Note it down — which are continuous: the speed of a car, the number of cars in a showroom, or the mass of a bag of rice? Answer: speed and mass are continuous measurements; the number of cars is a discrete count.",
            "The distinction depends on the possible values and how the quantity is obtained. A height recorded as a whole number is still a continuous measurement. A count remains discrete even when it is written with a decimal point, such as3.0 cars."
        ]),
        "13.4.2": make_section("13.4.2 Frequency Distribution", [
            "Frequency is the number of times a particular observation occurs. A frequency distribution organizes observations and their frequencies into a table. An ungrouped frequency table gives each distinct observation its own row.",
            "Example1 (pp.250–251):40 Class7 students' Mathematics scores out of10, in ascending order, are2,2,2,3,3,5,5,6,6,6;6,6,7,7,7,7,7,7,7,7;7,8,8,8,8,8,8,8,9,9;9,9,9,9,9,10,10,10,10,10. Prepare a frequency table.",
            "Step1: make columns for score, tally marks and frequency. List the observed scores in ascending order:2,3,5,6,7,8,9,10. Step2: read every score once and add a tally to its row. Group tallies in fives to make counting easier. Step3: count the tallies. Frequencies are respectively3,2,2,5,9,7,7,5. Check:3+2+2+5+9+7+7+5=40.",
            "Grouped frequency distribution: when there are many distinct values, putting each in a separate row can make a long table. Combine observations into non-overlapping classes of suitable width, then count the observations belonging to each class.",
            "Comparison activity: make a chart comparing discrete with continuous data and grouped with ungrouped data. Suggested answer: discrete means separate countable values; continuous means measurements within a range. Ungrouped tables retain individual values; grouped tables combine values into intervals, making large datasets easier to summarize but losing exact individual values. Either discrete or continuous numerical data can be grouped."
        ])}
    unit13["sections"] = [data_lessons.get(section["id"], section) for section in unit13["sections"]]
    for example in unit13["workedExamples"]:
        if example["id"] == "we-13-4a":
            example["problem"] = data_lessons["13.4.2"]["paras"][1]
            example["solution"] = data_lessons["13.4.2"]["paras"][2]
            example["diagram"] = {"type":"frequency-table","title":"Mathematics scores out of10","headers":["Score","Tally groups (5 + remaining)","Frequency"],"rows":[[2,"|||",3],[3,"||",2],[5,"||",2],[6,"5",5],[7,"5 + ||||",9],[8,"5 + ||",7],[9,"5 + ||",7],[10,"5",5],["Total","",40]]}
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.3.1":
            unit13["sections"][index] = make_section("13.3.1 Choosing an Appropriate Type of Graph/Chart", [
                "A graph presents data visually. Choose a chart that makes the intended comparison clear and represents the data accurately. The source prints this subsection as13.1.1 although it appears after the pie-graph lesson; it is organized here under13.3.",
                "Pictograph: uses pictures or symbols to display amounts in an attractive, accessible way. Include a key stating how much one symbol represents.",
                "Bar chart: compares separate categories, such as favourite sports or the Mathematics marks of five students. Label categories and values clearly. Bars make differences in amounts easy to compare.",
                "Multiple bar chart: compares two or more data series for the same categories. The source example compares men and women voting for three candidates. Use a legend to identify each series.",
                "Line graph: shows how a quantity changes over time. The source examples are the dollar exchange rate and a city's temperature. Put observations in time order and label units.",
                "Pie chart: compares parts of one whole, such as business partners' percentage shares. Sectors must represent non-overlapping parts of the same total; their angles add to360°.",
                "Class activity: divide into two groups and give each group a card containing a pie graph. Read values from the sectors and explain how the full-circle total is divided. Use sector value = sector angle ÷360° × total."
            ])
    for problem in pie_exercise["problems"]:
        if problem["qNo"] == "5":
            problem["diagram"] = {"type":"pie-sectors","title":"Printed marks-chart sector angles (degrees)","labels":["Above50","Above70","Above80","Above90"],"values":[72,100,108,80]}
            problem["solutionDiagram"] = {"type":"frequency-table","title":"Students represented by each printed sector","headers":["Printed label","Sector angle","Calculation","Students"],"rows":[["Above50","72°","90 ×72/360",18],["Above70","100°","90 ×100/360",25],["Above80","108°","90 ×108/360",27],["Above90","80°","90 ×80/360",20],["Total","360°","",90]]}
        elif problem["qNo"] == "6":
            problem["solutionDiagram"] = {"type":"grouped-bars","title":"Sample collected data: favourite fruit","labels":["Apple","Mango","Banana","Orange"],"series":[{"name":"Students","values":[8,6,4,2]}],"yMax":10,"step":2,"xLabel":"Favourite fruit","yLabel":"Number of students"}
    for example in unit13["workedExamples"]:
        if example["id"] == "we-13-3":
            example["problem"] = "Five students helped needy children pay their school fees. Dania contributed Rs940, Marwa Rs800, Fahad Rs1000, Afnan Rs1200 and Rohaan Rs1100. Draw a pie graph (pp.246–247)."
            example["solution"] = r"Step1: total contributions=940+800+1000+1200+1100=Rs5040. Step2: use \(\text{sector angle}=\frac{\text{contribution}}{5040}\times360^\circ\). Dania:940/14≈67.14°; Marwa:800/14≈57.14°; Fahad:1000/14≈71.43°; Afnan:1200/14≈85.71°; Rohaan:1100/14≈78.57°. Rounded to whole degrees, these are67°,57°,71°,86°,79°, which total360°. Step3: draw a circle and an initial radius. Step4: place the protractor at the centre and measure67° from the initial radius; draw the next radius for Dania's sector. Step5: start from that new radius and mark57° for Marwa. Continue with71°,86° and79° for the remaining students. Label each sector and add a title. The native chart uses the exact contribution proportions; hand construction may use the book's rounded angles."
            example["diagram"] = {"type":"pie-sectors","title":"Contributions for school fees (Rs)","labels":["Dania","Marwa","Fahad","Afnan","Rohaan"],"values":[940,800,1000,1200,1100]}
    quick_pie = {"id":"we-13-3-quick","title":"Quick Check — expenditure pie graph (p.247)","problem":"Draw a pie graph for expenditure: food2400, clothes1000, bills1500.","solution":r"Total=2400+1000+1500=4900. Food angle \(=\frac{2400}{4900}\times360^\circ\approx176.33^\circ\). Clothes angle \(=\frac{1000}{4900}\times360^\circ\approx73.47^\circ\). Bills angle \(=\frac{1500}{4900}\times360^\circ\approx110.20^\circ\). These total360° to two decimal places. Draw a circle, start with one radius and mark the sectors successively with a protractor. Label the sectors food, clothes and bills. Food is the largest share; clothes is the smallest. If drawing to whole degrees, adjust the final sector to close the circle; independently rounding every angle here gives359°.","diagram":{"type":"pie-sectors","title":"Quick Check: expenditure","labels":["Food","Clothes","Bills"],"values":[2400,1000,1500]}}
    unit13["workedExamples"].insert(next(i for i,e in enumerate(unit13["workedExamples"]) if e["id"]=="we-13-3")+1,quick_pie)
    pie_reading = {"id":"we-13-3-reading","title":"Reading a pie graph — Example1 (pp.245–246)","problem":"A pie graph represents4320 books sold in a bookstore during six weeks. The sector angles for weeks1–6 are35°,45°,22°,42°,126°,90°. (a) What is the graph about? (b) In which week were most books sold? (c) In which week were least books sold? (d) What percentage of the total books was sold in the fourth week?","solution":r"(a) The chart shows how4320 book sales were distributed over six weeks. (b) Week5: its126° sector is largest. (c) Week3: its22° sector is smallest. (d) Week4 has42° out of360°. Its book count is \(\frac{42}{360}\times4320=504\). Its percentage is \(\frac{504}{4320}\times100=11\frac23\%\approx11.7\%\). As a check, each degree represents4320/360=12 books, so weekly counts are420,540,264,504,1512,1080; their sum is4320. The angles total35+45+22+42+126+90=360°.","diagram":{"type":"pie-sectors","title":"Book sales over six weeks (sector angles in degrees)","labels":["Week1","Week2","Week3","Week4","Week5","Week6"],"values":[35,45,22,42,126,90]}}
    unit13["workedExamples"].insert(next(i for i,e in enumerate(unit13["workedExamples"]) if e["id"]=="we-13-3"),pie_reading)
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.3":
            unit13["sections"][index] = make_section("13.3 Pie Graph", [
                "A pie graph is a circle divided into sectors. The full circle represents the total quantity, and each sector represents one part. The sector angle is proportional to that part's share of the total.",
                r"To read a sector, use \(\text{part}=\frac{\text{sector angle}}{360^\circ}\times\text{total}\). Its percentage is \(\frac{\text{sector angle}}{360^\circ}\times100\%\).",
                pie_reading["problem"], pie_reading["solution"],
                r"To construct a pie graph, first add all observations. Then calculate each sector angle using \(\theta=\frac{\text{category value}}{\text{total}}\times360^\circ\). Draw a circle and radius, use a protractor to mark successive central angles, and label the sectors. All sectors must together make360°. The school-fee contribution example and expenditure Quick Check provide worked constructions."
            ])
    line_lesson = [
        "A line graph plots observations as points and joins successive points with straight lines. It helps us see how a quantity changes, often over time. Use time on the horizontal axis and the measured quantity on the vertical axis; choose and label a consistent scale.",
        "Source example (p.244): Madiha's weekly Mathematics marks out of10 are Week1:3, Week2:7, Week3:5, Week4:5, Week5:8. Plot these five points in week order and join consecutive points.",
        "Reading the graph: from Week1 to Week2, the increase is7−3=4 marks. From Week2 to Week3, the decrease is7−5=2 marks. Weeks3 and4 have equal marks,5, so their connecting segment is horizontal. Week5 has the highest mark,8, and Week1 the lowest,3.",
        "A rising segment indicates an increase and a falling segment a decrease. A horizontal segment indicates no change between the two plotted observations. The line joins the recorded observations; values at unrecorded times are not additional measured results."
    ]
    for index, section in enumerate(unit13["sections"]):
        if section["id"] == "13.2":
            unit13["sections"][index] = make_section("13.2 Line Graph", line_lesson)
    unit13["workedExamples"].insert(next(i for i,e in enumerate(unit13["workedExamples"]) if e["id"]=="we-13-3-reading"),{
        "id":"we-13-2","title":"Reading a line graph: weekly Mathematics marks (p.244)",
        "problem":"Interpret Madiha's marks out of10 over five weeks:3,7,5,5,8. Compare successive weeks and identify the highest and lowest marks.",
        "solution":line_lesson[2],
        "diagram":{"type":"category-line","title":"Madiha's weekly Mathematics marks","labels":["Week1","Week2","Week3","Week4","Week5"],"series":[{"name":"Marks","values":[3,7,5,5,8]}],"yMax":10,"step":1,"xLabel":"Week","yLabel":"Marks out of10"}
    })
    line_exercise["problems"][0]["solution"] = "(a) April has the highest production:6000 toys. (b) The two months are March and May: production fell from3000 in February to1500 in March, and from6000 in April to3500 in May. (c) May produced3500−1500=2000 more toys than March. (d) The increase from January to April is6000−2000=4000 toys. This is the net increase between the two named months."
    opening13 = {
        "student-learning-outcomes": make_section("Student Learning Outcomes", [
            "Draw and interpret bar graphs, line graphs and pie charts; distinguish bar graphs from histograms. Construct and compare histograms for discrete and continuous data with equal interval widths.",
            "Select and justify a suitable graph for a dataset and draw conclusions from its shape. Distinguish discrete, continuous, grouped and ungrouped data.",
            "Calculate mean, median and mode for ungrouped data and mean for grouped data. Solve real-world problems and compare which central measure is most appropriate.",
            "Construct frequency-distribution tables, identifying frequency, lower/upper class limits, class intervals and midpoints. Explain and calculate probabilities of certain events, impossible events and complementary events.",
            "Opening question (p.241): the forecast gives a67% chance of rain tomorrow. What is the probability it will not rain? Answer: rain and no rain are complementary, so100%−67%=33%, or0.33."
        ]),
        "introduction": make_section("Introduction", ["Earlier classes introduced simple bar graphs and pie charts. This unit extends that work to selecting suitable charts, constructing histograms, distinguishing data types, making frequency tables and understanding probability."]),
        "13.1": make_section("13.1 Multiple Bar Graph", [
            "A multiple bar graph extends a simple bar graph by showing two or more related data series for the same categories. Bars may be vertical or horizontal. Group related bars together and use consistent colours with a legend to distinguish the series.",
            "Example1 (p.242): employees joining an educational office during May, June, July, August and September. Research:15,25,10,15,20. Designing:20,25,15,30,35. Editing:5,20,15,10,25. Draw a vertical multiple bar graph.",
            "Draw perpendicular horizontal and vertical axes. Put the five months in order on the horizontal axis; put employee counts on the vertical axis with a suitable scale, such as5 employees per division. Draw three equal-width adjacent bars per month in the same department order. Leave equal gaps between month groups and label the axes and legend.",
            "Class activity: work in groups to create a table of real-life data suitable for a multiple bar graph. Exchange it with another group and draw its graph. A possible task is counting borrowed storybooks and textbooks on each school day; collect actual counts, give the table clear headings and compare both series using one common scale."
        ])}
    unit13["sections"] = [opening13.get(section["id"], section) for section in unit13["sections"]]
    for example in unit13["workedExamples"]:
        if example["id"] == "we-13-1":
            example["solution"] = opening13["13.1"]["paras"][2]
            example["diagram"] = {"type":"grouped-bars","title":"Employees joining the educational office","labels":["May","June","July","August","September"],"series":[{"name":"Research","values":[15,25,10,15,20]},{"name":"Designing","values":[20,25,15,30,35]},{"name":"Editing","values":[5,20,15,10,25]}],"yMax":40,"step":5,"xLabel":"Month","yLabel":"Number of employees"}
    angle_exercise = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Exercise 12.5")
    for problem in angle_exercise["problems"]:
        if "star diagram" in problem["question"]:
            problem["question"] = "Think Higher2 (printed p.235): find the marked angles in the star figure. The outer triangles are DBC, EFD, GHF, IHJ, KJL, MLN and ANB. Use their printed equal-side marks, right angles and given angles."
            problem["solution"] = "Use the local markings of each small triangle. (a),(b): triangle DBC has equal-side marks on DB, DC and BC, and its angle at D is60°. It is equilateral, so a=b=60°. (c),(d): EF=ED and angle FED=30°, so the equal base angles are c=d=(180°−30°)/2=75°. (e): triangle GHF has angle G=45° and angle H=90°, so e=180°−45°−90°=45°. (f),(g): triangle IHJ has matching side marks and angle I=60°, so f=g=60°. (h): triangle KJL has60° at J and60° at L; h=180°−60°−60°=60°. (i): triangle MLN has30° at M and90° at L; i=180°−30°−90°=60°. (j): triangle ANB has70° at N and70° at B; j=180°−70°−70°=40°. The marked central angle LON is vertically opposite the given40° angle FOD, so it is40°. Source consistency note: these answers use each indicated local triangle. The full drawing contains conflicting extra markings. For example, M,L,O are drawn on one line and the right angle at L makes angle OLN90°, but the equal marks LO=ON would make triangle LON have two right angles, which is impossible. Thus the whole star cannot satisfy every printed mark simultaneously; the local calculations above should not be treated as proof that the entire drawing is geometrically consistent."
    for problem in angle_exercise["problems"]:
        if "Colour the square grid" in problem["question"]:
            problem["question"] = "Think Higher1 (printed p.235): colour the square grid to make it symmetric along both dotted lines. Preserve the given coloured squares."
            problem["diagram"] = {"type":"colour-symmetry-grid","title":"Original symmetry-grid activity","rows":[["G","Y","R","","",""],["Y","R","C","","",""],["R","B","G","","",""],["","","","G","B","R"],["","","","C","R","Y"],["","","","R","Y","G"]]}
            problem["solutionDiagram"] = {"type":"colour-symmetry-grid","title":"Completed grid: reflection in both axes","rows":[["G","Y","R","R","Y","G"],["Y","R","C","C","R","Y"],["R","B","G","G","B","R"],["R","B","G","G","B","R"],["Y","R","C","C","R","Y"],["G","Y","R","R","Y","G"]]}
            problem["solution"] = "Reflect each given square across the vertical dotted line: columns1 and6 match, columns2 and5 match, and columns3 and4 match. Reflect across the horizontal dotted line: rows1 and6 match, rows2 and5 match, and rows3 and4 match. Completed rows from top to bottom are: (1) green,yellow,red,red,yellow,green; (2) yellow,red,cyan,cyan,red,yellow; (3) red,blue,green,green,blue,red; (4) the same as row3; (5) the same as row2; (6) the same as row1. This preserves all starting colours and fills the18 blank squares. Folding along either dotted axis places matching colours on top of each other."
    # Preserve p.235's separate Think Higher numbering, rather than inventing Q4–Q6.
    for problem in angle_exercise["problems"]:
        if problem["qNo"] == "4":
            problem["qNo"] = "Think Higher1"
        elif problem["qNo"] == "5":
            problem["qNo"] = "Think Higher2"
    angle_exercise["problems"] = [p for p in angle_exercise["problems"] if p["qNo"] != "6"]
    angle_exercise["problems"].extend([
        {"qNo":"Think Higher3","question":"Can an isosceles triangle be an equilateral triangle?","solution":"Yes, using the inclusive definition: an isosceles triangle has at least two equal sides. If its third side is also equal to those two, it is equilateral. For example, side lengths4 cm,4 cm,4 cm satisfy both definitions. If a class uses 'exactly two equal sides' for isosceles, that narrower convention excludes equilateral triangles; state the definition being used."},
        {"qNo":"Think Higher4","question":"Can an equilateral triangle be an isosceles triangle?","solution":"Yes under the at-least-two-equal-sides definition. Every equilateral triangle has three equal sides, so it necessarily has at least two equal sides and is a special isosceles triangle. Its three angles are60°."},
        {"qNo":"Think Higher5","question":"Draw a triangle which is isosceles as well as right-angled. Use a set square and ruler.","solution":"Choose a point A. Use the set square to draw two perpendicular rays from A. With the ruler mark B4 cm along one ray and C4 cm along the other. Join B to C. Then AB=AC=4 cm, so triangle ABC is isosceles; angle A=90°, so it is right-angled. The other two angles are equal and sum to90°, giving45° each. The4 cm length is a sample choice; any equal positive lengths along the two perpendicular rays work.","solutionDiagram":{"type":"construction-triangle","title":"Sample isosceles right triangle","points":[[0,0],[4,0],[0,4]],"names":["A","B","C"],"sideLabels":["4 cm","","4 cm"],"angleLabels":["90°","45°","45°"]}}
    ])
    chapters[11]["sections"].append(make_section("Summary and Vocabulary", [
        "Printed p.236 summary: rotational symmetry describes a figure matching itself during a full360° turn about a centre. The order counts matching positions in one full turn. A figure with order1 has only the full-turn match; non-trivial rotational symmetry has order at least2. The centre of rotation is the fixed point about which it turns.",
        "A translation can be described in words or by ordered pairs. Every point moves the same distance in the same direction; size and shape remain unchanged.",
        "Transformation: a rule moving or changing a figure. Pre-image: the original figure. Reflection: a mirror transformation in a line. Rotation: a turn about a centre. Translation: a slide. Symmetry: a transformation that makes the figure coincide with itself.",
        "Isosceles triangle: at least two equal sides. Equilateral triangle: three equal sides. Scalene triangle: no equal sides. Right-angled triangle: one90° angle. Acute-angled triangle: all angles less than90°. Obtuse-angled triangle: one angle greater than90°."
    ]))
    import math
    asa_constructions = [
        ("12.4.1", "Equilateral Triangle", "we-12-equilateral", ["M","N","O"],4,60,60),
        ("12.4.2", "Isosceles Triangle", "we-12-isosceles", ["P","Q","R"],4,50,50),
        ("12.4.3", "Scalene Triangle", "we-12-scalene", ["P","Q","R"],5,40,50)]
    for sid, name, eid, names, base, left, right in asa_constructions:
        a,b,c = names
        third = 180-left-right
        steps = f"Draw {a}{b}={base} cm with a ruler. Place the protractor centre at {a}, align its baseline with {a}{b}, and draw a ray making{left}° on one side of the base. At {b}, align the protractor with {b}{a} and draw a ray making{right}° on the same side of the base. Label the intersection {c}. Join the vertices to complete triangle {a}{b}{c}. The third angle is180°−{left}°−{right}°={third}°."
        definition = {"12.4.1":"An equilateral triangle has three equal sides and three60° angles.","12.4.2":"An isosceles triangle has at least two equal sides. Equal base angles give equal opposite sides; here PR=QR.","12.4.3":"A scalene triangle has three unequal sides. Here its angles40°,50°,90° are all different, so its sides are all different; it is also right-angled."}[sid]
        for index, section in enumerate(chapters[11]["sections"]):
            if section["id"] == sid:
                chapters[11]["sections"][index] = make_section(sid+" "+name,[definition,f"Source example: construct triangle {a}{b}{c} with {a}{b}={base} cm, angle {a}={left}° and angle {b}={right}°.",steps])
        x = base*math.tan(math.radians(right))/(math.tan(math.radians(left))+math.tan(math.radians(right)))
        for example in chapters[11]["workedExamples"]:
            if example["id"] == eid:
                example["solution"] = steps+" "+definition
                example["diagram"] = {"type":"construction-triangle","title":name+" construction","points":[[0,0],[base,0],[x,x*math.tan(math.radians(left))]],"names":names,"sideLabels":[str(base)+" cm","",""],"angleLabels":[str(left)+"°",str(right)+"°",str(third)+"°"]}
    chapters[11]["workedExamples"].extend([
        {"id":"we-12-quick-scalene","title":"Quick Check (p.231), part(a)","problem":"Write construction steps and name triangle LMN with angle M=50°, angle N=60° and MN=5 cm.","solution":"Draw MN=5 cm. At M draw a50° ray to MN; at N draw a60° ray to NM, both above the base. Their intersection is L. Angle L=180°−50°−60°=70°. All three angles are different, so the triangle is scalene; all are less than90°, so it is acute-angled."},
        {"id":"we-12-quick-isosceles","title":"Quick Check (p.231), part(b)","problem":"Write construction steps and name triangle MNO with angle M=angle N=70° and MN=7 cm.","solution":"Draw MN=7 cm. Draw a70° ray at M to MN and another70° ray at N to NM on the same side. Name their intersection O. Angle O=180°−70°−70°=40°. The equal base angles give OM=ON, so the triangle is isosceles. All angles are acute."},
        {"id":"we-12-quick-two-right","title":"Quick Check: two right angles (p.231)","problem":"Can a triangle have two right angles? Give a reason.","solution":"No. Two right angles already sum to90°+90°=180°, leaving0° for the third angle. A non-degenerate triangle must have three positive angles whose sum is180°."}
    ])
    sas_examples = [
        ("12.4.4","Acute-angled Triangle","we-12-acute",3.5,3,40),
        ("12.4.5","Obtuse-angled Triangle","we-12-obtuse",4,3.8,120),
        ("12.4.6","Right-angled Triangle","we-12-right",3,2.5,90)]
    for sid, title, eid, lm, ln, angle_l in sas_examples:
        nx = ln*math.cos(math.radians(angle_l))
        ny = ln*math.sin(math.radians(angle_l))
        mn = math.hypot(lm-nx,ny)
        angle_m = math.degrees(math.atan2(ny,lm-nx))
        angle_n = 180-angle_l-angle_m
        steps = f"Draw LM={lm} cm with a ruler. Centre the protractor at L and align its baseline with LM. Mark{angle_l}° and draw the ray LO through that mark. Set the compass opening to{ln} cm; with centre L draw an arc meeting ray LO at N. Join N to M. The constructed triangle has LM={lm} cm, LN={ln} cm and angle MLN={angle_l}°."
        note = f"Calculated check of the supplied measurements: MN≈{mn:.2f} cm, angle M≈{angle_m:.2f}° and angle N≈{angle_n:.2f}°. These values are checks of the drawing, not extra construction givens."
        if sid == "12.4.4":
            definition = "An acute-angled triangle has all three angles less than90°."
            note += " The printed diagram's MN=2 cm and angles60°/80° do not exactly match LM=3.5 cm, LN=3 cm and angle L=40°; use the stated construction measurements."
        elif sid == "12.4.5":
            definition = "An obtuse-angled triangle has one angle greater than90° and less than180°."
            note += " The printed30°/30° labels would require equal sides opposite them, but LM=4 cm and LN=3.8 cm are unequal. The construction retains the given side lengths and120° angle."
        else:
            definition = "A right-angled triangle has one90° angle. Its other two angles sum to90°."
            note += " The printed40°/50° labels are approximate; the given side lengths yield the values above."
        for index, section in enumerate(chapters[11]["sections"]):
            if section["id"] == sid:
                chapters[11]["sections"][index] = make_section(sid+" "+title,[definition,f"Example1: construct triangle LMN with LM={lm} cm, LN={ln} cm and angle L={angle_l}°.",steps,note])
        for example in chapters[11]["workedExamples"]:
            if example["id"] == eid:
                example["solution"] = steps+" "+note
                example["diagram"] = {"type":"construction-triangle","title":title+" from the stated measurements","points":[[0,0],[lm,0],[nx,ny]],"names":["L","M","N"],"sideLabels":[str(lm)+" cm","",str(ln)+" cm"],"angleLabels":[str(angle_l)+"°","",""]}
    description_paras = [
        "To describe a translation, choose a vertex of the original figure and its corresponding image. Subtract original coordinates from image coordinates: horizontal movement=x′−x and vertical movement=y′−y. Check that every other vertex has the same movement.",
        "Example1 (p.228): A(1,4), B(3,7), C(5,5), D(4,2) map to A′(−3,−4), B′(−1,−1), C′(1,−3), D′(0,−6). From A to A′, horizontal movement=−3−1=−4 and vertical movement=−4−4=−8.",
        "Therefore the translation is4 units left and8 units down, with rule(x,y)→(x−4,y−8). Check B:(3−4,7−8)=(−1,−1); C:(5−4,5−8)=(1,−3); D:(4−4,2−8)=(0,−6). All four vertices obey the same rule.",
        "The printed graph labels C′ as(2,−3), which does not agree with C(5,5) and a4-left translation. Applying the stated rule gives C′(1,−3); this corrected coordinate is used in the redrawn example."
    ]
    for index, section in enumerate(chapters[11]["sections"]):
        if section["id"] == "12.3.1":
            chapters[11]["sections"][index] = make_section("12.3.1 Describing a Translation", description_paras)
    for example in chapters[11]["workedExamples"]:
        if example["id"] == "we-12-describe-translation":
            example["problem"] = "Describe the translation of quadrilateral A(1,4), B(3,7), C(5,5), D(4,2) when A maps to A′(−3,−4), and find every image vertex."
            example["solution"] = " ".join(description_paras[1:])
            example["diagram"] = {"type":"coordinate-panels","panels":[transformation_panel("4 units left and8 units down",[[1,4],[3,7],[5,5],[4,2]],lambda x,y:(x-4,y-8))]}
    chapters[11]["workedExamples"].append({"id":"we-12-translation-quick","title":"Quick Check:6 left and7 up (p.227)","problem":"Translate the rectangle Q(2,−7), R(10,−7), S(10,−5), T(2,−5)6 units left and7 units up. Graph its image.","solution":"The rule is(x,y)→(x−6,y+7). Apply it to each vertex: Q′=(2−6,−7+7)=(−4,0); R′=(10−6,−7+7)=(4,0); S′=(10−6,−5+7)=(4,2); T′=(2−6,−5+7)=(−4,2). Plot these four points and join them in order. The image is the same8-unit-wide,2-unit-high rectangle, now lying on and above the x-axis. The unrelated A′(−2,4) text printed in the source grid belongs to the preceding example, not to this rectangle.","diagram":{"type":"coordinate-panels","panels":[transformation_panel("Quick Check:6 left and7 up",[[2,-7],[10,-7],[10,-5],[2,-5]],lambda x,y:(x-6,y+7))]}})
    rotation_paragraphs = [
        "A rotation turns a figure about a fixed centre. Specify the centre, angle and clockwise or counterclockwise direction. In the textbook's convention, an unspecified direction is counterclockwise. Rotating preserves lengths, angles and shape.",
        "To rotate about the origin: identify every original vertex; apply the same coordinate rule to each; plot the new points; join them in the original order. These rules apply about the origin(0,0).",
        "90° counterclockwise, or270° clockwise: (x,y)→(−y,x). Change the sign of the original y-coordinate and place it first; place the original x-coordinate second. Source examples: A(2,4)→A′(−4,2); B(−3,1)→B′(−1,−3).",
        "180° in either direction: (x,y)→(−x,−y). Change both signs. Source examples: J(2,4)→J′(−2,−4); K(3,1)→K′(−3,−1).",
        "90° clockwise, or270° counterclockwise: (x,y)→(y,−x). Put the original y-coordinate first and the negative of the original x-coordinate second. Therefore J(2,4)→J′(4,−2) and K(3,1)→K′(1,−3). The printed examples in this third case repeat the180° answers by mistake; the stated90° clockwise rule gives these corrected results.",
        "Worked rectangle (p.224): rotate A(2,6), B(7,6), C(7,2), D(2,2)90° counterclockwise about the origin. Applying(−y,x) gives A′(−6,2), B′(−6,7), C′(−2,7), D′(−2,2). Join the image vertices in order. This is a rotated image; the source's references to a reflected image here are wording errors.",
        "Activity: use a cut-out shape and turn it around a marked centre. Track one vertex as it moves and compare the starting figure with its image. Describe the centre, direction and angle using the correct rotation terminology."
    ]
    for index, section in enumerate(chapters[11]["sections"]):
        if section["id"] == "12.2.1":
            chapters[11]["sections"][index] = make_section("12.2.1 Rotation of Objects on the Coordinate Plane", rotation_paragraphs)
    chapters[11]["workedExamples"].extend([
        {"id":"we-12-rotation-quick-point","title":"Quick Check: rotate P(−10,6) (p.223)","problem":"Find P′ when P(−10,6) is rotated about the origin: (a)90° counterclockwise; (b)180° counterclockwise; (c)90° clockwise; (d)270° counterclockwise.","solution":"(a) Use(−y,x): P′=(−6,−10). (b) Use(−x,−y): P′=(10,−6). (c) Use(y,−x): P′=(6,10). (d)270° counterclockwise equals90° clockwise, so P′=(6,10)."},
        {"id":"we-12-rotation-quick-triangle","title":"Quick Check: half-turn of a triangle (p.224)","problem":"Draw any triangle and rotate it180° counterclockwise about the origin.","solution":"Sample choice: A(1,1), B(4,1), C(2,3). For a180° turn, use(x,y)→(−x,−y). Thus A′(−1,−1), B′(−4,−1), C′(−2,−3). Plot and join both triples in order. The origin is the midpoint of each vertex and its corresponding image. Other chosen triangles are equally valid when every vertex follows this rule.","diagram":{"type":"coordinate-panels","panels":[transformation_panel("Sample triangle:180° about the origin",[[1,1],[4,1],[2,3]],lambda x,y:(-x,-y))]}}
    ])
    symmetry_lessons = {
        "12.1": make_section("12.1 Transformations", [
            "A transformation changes a figure's position, orientation or size according to a rule. This unit studies reflection, rotation and translation. These three preserve lengths and angles, so the image has the same size and shape as the original.",
            "The original figure is the pre-image; the transformed figure is its image. A reflection flips a figure in a mirror line, a rotation turns it about a centre, and a translation slides every point by the same movement."
        ]),
        "12.1.1": make_section("12.1.1 Reflective Symmetry", [
            "A figure has line symmetry when its two parts match exactly after folding along a line. That fold is its line of symmetry. Matching exactly means that every point on one side has a matching point the same perpendicular distance away on the other side; merely dividing the area equally is not enough.",
            "Source figures on p.221: (a) a semicircle has the vertical symmetry line through its centre; (b) the isosceles trapezium has a vertical symmetry line; (c) the right-pointing arrow has a horizontal symmetry line; (d) the sideways kite has a horizontal symmetry line. The butterfly's left and right wings match across a vertical line.",
            "A drawn dotted line is only a proposed symmetry line. Fold or reflect the figure to check whether its outlines match. The irregular yellow figure on p.221 does not match across the shown line.",
            "The drawn block letters E and D have horizontal symmetry. The drawn H and X on p.222 have both horizontal and vertical symmetry. Letter symmetry depends on the exact font and shape used.",
            "In the four comparison figures on p.222, the shown lines in (a) and (b) fail the exact-match test; the shown lines in (c) and (d) do give matching halves. A line passing through a shape is not automatically a line of symmetry.",
            "Activity: draw and cut out two-dimensional shapes. Fold them or use a mirror to identify every symmetry line. Group the shapes according to their numbers of lines. Bring letter cut-outs and check their actual outlines in the same way."
        ]),
        "12.2": make_section("12.2 Rotational Symmetry", [
            "A figure has rotational symmetry when turning it about a centre makes it coincide with itself before a full turn. The order is the number of matching positions in one360° turn, counting the final full-turn match but not counting the initial position twice.",
            "The four-petal figure on p.222 matches after90°,180°,270° and360°, so its order is4. The smallest matching turn is360°/4=90°. The centre of rotation is the fixed point around which the figure turns.",
            "The second source example is a hexagonal shape with two coloured dots. The entire marked figure matches at180° and360°, giving order2. The dots are part of the figure: ignore neither them nor their positions when judging a match. At90° and270° it does not match the starting figure.",
            "For a finite rotational order n, the smallest matching angle is360°/n. A figure matching only after a full360° turn has order1 and no non-trivial rotational symmetry. Use the complete figure, including colours and labels, when counting matches.",
            "Activity: place a cut-out over its traced outline and mark a centre. Turn it slowly through360°, recording each angle at which the entire shape matches the outline. Count those matches to find its order."
        ])}
    chapters[11]["sections"] = [symmetry_lessons.get(section["id"],section) for section in chapters[11]["sections"]]
    chapters[11]["workedExamples"].insert(0,{
        "id":"we-12-reflection-examples","title":"Reflective symmetry: source figures (p.221)",
        "problem":"Explain the symmetry lines shown for the isosceles trapezium, right-pointing arrow and sideways kite.",
        "solution":"The isosceles trapezium has a vertical line through the midpoints of its parallel sides: its left and right halves match. The arrow has a horizontal line through its centre: its top and bottom halves match. The sideways kite also has a horizontal line joining its two vertices where the equal-side pairs meet. Reflecting each outline across its indicated line maps every edge to a corresponding edge.",
        "diagram":{"type":"symmetry-panels","panels":[
            {"title":"(b) Isosceles trapezium","points":[[100,65],[200,65],[250,180],[50,180]],"axes":[[150,35,150,210]]},
            {"title":"(c) Right-pointing arrow","points":[[40,95],[190,95],[190,65],[260,120],[190,175],[190,145],[40,145]],"axes":[[20,120,280,120]]},
            {"title":"(d) Sideways kite","points":[[65,120],[125,60],[260,120],[125,180]],"axes":[[40,120,280,120]]}
        ]}
    })
    chapters[11]["workedExamples"].insert(1,{
        "id":"we-12-letter-quick","title":"Quick Check: letter symmetry (p.222)",
        "problem":"The letters in the source Quick Check are not symmetric about the dotted lines. Why? Consider the visible F, G and J and apply the same folding test to each printed outline.",
        "solution":"Fold or reflect each letter across its marked dotted line. F has upper and middle arms but no matching bottom arm, so its top and bottom do not coincide; left and right do not coincide either. G has an opening and an inward bar that do not match their reflected positions. J has a lower hook without a matching upper hook. Thus the proposed horizontal or vertical lines do not divide these drawn letters into matching mirror halves. Judge the actual printed letter outline, since symmetry can change with the typeface. The final faint character in the supplied scan has not been reliably identified; use the same exact-overlap test for that outline."
    })
    symmetry_exercise = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Exercise 12.1")
    for problem in symmetry_exercise["problems"]:
        if problem["qNo"] == "1":
            problem["question"] = "Draw all lines of symmetry for the six source figures, from left to right: a sideways semicircle, a T-shaped outline, an isosceles trapezium, a C-shaped outline, U and a regular hexagon."
            problem["solution"] = "(1) Sideways semicircle: one horizontal line through its centre, perpendicular to its vertical diameter. (2) T-shaped outline: one vertical centre line. (3) Isosceles trapezium: one vertical line through the midpoints of the parallel sides. (4) C-shaped outline: one horizontal centre line. (5) U: one vertical centre line. (6) Regular hexagon: six lines, three through pairs of opposite vertices and three through midpoints of opposite sides. Each line must make the two reflected halves coincide."
        elif problem["qNo"] == "2":
            problem["solution"] = "For the dotted lines actually shown: (a) No—the vertical line does not reflect B onto itself. (b) No—the vertical line does not reflect N onto itself. (c) Yes—the horizontal line reflects the drawn E onto itself. (d) Yes—the horizontal line bisects the narrow rectangular I-shaped figure into matching halves. (e) No—the vertical line fails for the offset step shape. (f) Yes—the vertical line passes through the centre of the oval. Therefore c,d,f have symmetry about their marked lines. The separate question 'Which figures have lines of symmetry?' also includes B (a), whose drawn matching lobes give a horizontal line, even though its displayed vertical line is wrong. N and the offset step do not have reflection symmetry in the pictured forms."
        elif problem["qNo"] == "3":
            problem["solution"] = "(a) Equal-armed plus: order4, matching every90°. (b) Hourglass: order2, matching after180° and360°. (c) L-shaped figure: order1; it matches only after360°, so it has no non-trivial rotational symmetry. (d) Opposed decorated bow-tie figure: order2; a180° turn exchanges the matching halves. Judge the complete shape and its internal pattern, not just the outer outline."
    geometry_review = next(ex for ex in chapters[11]["exercises"] if ex["title"] == "Review Exercise")
    review_mcq = next(p for p in geometry_review["problems"] if p["qNo"] == "1")
    review_mcq["question"] = "Encircle the correct option (pp.236–237).\n(a) A line of symmetry divides the symmetric shape into: (i) Quarters (ii) Halves (iii) Thirds (iv) Fourths.\n(b) If a figure looks exactly the same at least twice during a full rotation, it has: (i) Translation symmetry (ii) Reflective symmetry (iii) Rotational symmetry (iv) Line symmetry.\n(c) Turning a shape around a fixed centre of rotation is: (i) Reflection (ii) Translation (iii) Rotation (iv) Dilation.\n(d) Moving or shifting an object from one place to another is: (i) Reflection (ii) Translation (iii) Rotation (iv) Dilation.\n(e) Translating an object does not affect its: (i) Position (ii) Location (iii) Placement (iv) Size.\n(f)2 units left and1 unit down is: (i)(x,y)→(x+2,y−1) (ii)(x,y)→(x−2,y+1) (iii)(x,y)→(x+2,y+1) (iv)(x,y)→(x−2,y−1).\n(g) A90° counterclockwise or270° clockwise rotation about the origin will: (i) Change the sign of x and switch x,y (ii) Change the sign of x only (iii) Change the sign of y only (iv) Change the sign of y and switch x,y.\n(h)(x,y)→(x−4,y+6) means: (i) Add4 to x and6 to y (ii) Subtract4 from y and add6 to x (iii) Add4 to x and6 to y (iv) Subtract4 from x and add6 to y. Options(i) and(iii) are repeated in the source."
    review_mcq["solution"] = "(a)(ii) Halves: folding in the symmetry line makes the halves match exactly. (b)(iii) Rotational symmetry: the figure coincides with itself during a turn about its centre. (c)(iii) Rotation: a turn about a fixed point. (d)(ii) Translation: all points slide by the same displacement. (e)(iv) Size: a translation changes position but preserves lengths and angles. (f)(iv)(x−2,y−1): left decreases x and down decreases y. (g)(iv): negate the original y and interchange the coordinates, giving(−y,x). (h)(iv): subtract4 from x and add6 to y, which moves every point4 units left and6 units up."
    review_triangles = {
        "12": ([[0,0],[7,0],[3.5,7*math.sqrt(3)/2]],["P","Q","R"],["7 cm","7 cm","7 cm"],["60°","60°","60°"]),
        "13": ([[0,0],[4,0],[2,math.sqrt(32)]],["A","B","C"],["4 cm","6 cm","6 cm"],["","",""]),
        "14": ([[0,0],[6.3,0],[6.3,4.5]],["L","M","N"],["6.3 cm","4.5 cm",""],["","90°",""]),
        "15": ([[0,0],[7,0],[7*math.tan(math.radians(40))/(math.tan(math.radians(20))+math.tan(math.radians(40))),7*math.tan(math.radians(40))*math.tan(math.radians(20))/(math.tan(math.radians(20))+math.tan(math.radians(40)))]],["D","E","F"],["7 cm","",""],["20°","40°","120°"]),
        "16": ([[6,0],[5*math.cos(math.radians(70)),5*math.sin(math.radians(70))],[0,0]],["P","Q","R"],["","5 cm","6 cm"],["","","70°"]),
        "17": ([[3*math.cos(math.radians(140)),3*math.sin(math.radians(140))],[5,0],[0,0]],["D","E","F"],["","5 cm","3 cm"],["","","140°"])}
    for problem in geometry_review["problems"]:
        if problem["qNo"] in review_triangles:
            points,names,sides,angles = review_triangles[problem["qNo"]]
            problem["solutionDiagram"] = {"type":"construction-triangle","title":"Review Q"+problem["qNo"]+": triangle"+"".join(names),"points":points,"names":names,"sideLabels":sides,"angleLabels":angles}
            problem["solution"] += " Use a ruler for the stated lengths and a protractor for any given angle. Keep the construction on one side of the chosen base and label all vertices. The diagram shows one valid orientation; its reflection across the base is also a valid construction."
            if problem["qNo"] == "12":
                problem["solution"] += " The word equilateral also requires PR=7 cm, even though only PQ and QR are explicitly listed."
            elif problem["qNo"] == "15":
                problem["solution"] += " Its angles20°,40°,120° are unequal, so all sides are unequal: it is scalene and also obtuse-angled."
    for index, section in enumerate(chapters[11]["sections"]):
        if section["id"] == "student-learning-outcomes":
            chapters[11]["sections"][index] = make_section("Student Learning Outcomes", [
                "Recognize, identify and draw lines of symmetry in two-dimensional shapes. Rotate objects, recognize rotational symmetry and find its order.",
                "Translate an object and describe its transformation precisely. Calculate unknown angles in a triangle.",
                "Construct equilateral, isosceles, scalene, acute-angled, right-angled and obtuse-angled triangles.",
                "Opening question (p.220): a wall clock needs to move from its current position to the marked position on its left. Must it be rotated or flipped, or can it move without changing its orientation? Answer: translate the clock to the left. Every point moves the same distance in the same direction, and the clock stays upright. Neither turning nor reflection is needed. The picture gives no numerical distance, so none is assumed."
            ])
    chapters[11]["sections"].insert(1,make_section("Introduction", ["Earlier work covered angles, their construction, reflection and rotation. This unit develops transformations further: describing rotations and translations, recognizing symmetry, constructing triangles and finding their unknown angles."]))
    quadrilateral_opening = {
        "student-learning-outcomes": make_section("Student Learning Outcomes", [
            "Recognize squares, rectangles, parallelograms, rhombuses, trapeziums and kites using parallel/equal sides, equal/right angles and symmetry lines. Calculate unknown angles using these properties.",
            "Distinguish convex and concave polygons. Relate interior and exterior angles, including a triangle's exterior angle and its opposite interior angles. Calculate polygon interior-angle sums and individual interior/exterior angles.",
            "Describe a circle's centre, radius, diameter, chords, arcs, major/minor arcs, semicircles and segments.",
            "Opening activity (p.198): find four-sided shapes in the pictured chart. Look for closed outlines with exactly four straight sides, such as the diamond-shaped sign and quadrilateral panels in the pictured objects. Count each selected outline once; distinguish whole outlines from smaller internal panels. The illustration contains overlapping details, so explain which outlines you counted."
        ]),
        "introduction": make_section("Introduction", ["Earlier work covered drawing line segments of given lengths, perpendicular lines, angles and angle bisectors, and basic quadrilateral and polygon properties. This unit develops those properties and their angle relationships further."]),
        "11.1": make_section("11.1 Quadrilaterals and Their Properties", [
            "A quadrilateral is a closed figure with four straight sides, four vertices and four interior angles. Its interior angles sum to360°. This unit considers squares, rectangles, parallelograms, rhombuses, trapeziums and kites.",
            "Source Previous Knowledge Check (p.199) asks about data and bar graphs. Data are collected information; organizing data means arranging it, for example in a table. A bar graph represents category values by bar lengths. Bars can be vertical or horizontal; multiple bars compare related series. To present data, label the categories, choose a uniform numerical scale and draw bars of the appropriate lengths. These prompts appear in the source despite the geometry topic.",
            "Recall activity: describe familiar quadrilaterals, sketch each and identify its equal sides, parallel sides and angles."
        ]),
        "11.1.1": make_section("11.1.1 Square", [
            "Square ABCD has sides AB, BC, CD and DA, and angles ABC, BCD, CDA and DAB. All four sides are equal: AB=BC=CD=DA. Each interior angle is90°.",
            "Opposite sides are parallel: AB∥DC and BC∥AD. Parallel lines remain the same perpendicular distance apart and do not meet in the plane.",
            "Adjacent sides share a vertex and are perpendicular: AB⊥BC, BC⊥CD, CD⊥DA and DA⊥AB. Thus a square has two pairs of parallel sides and four pairs of perpendicular adjacent sides.",
            "Reading the source diagram: matching side ticks show equal lengths, matching arrowheads show parallel sides and small corner squares show right angles. These marks state properties even when a sketch is not drawn exactly to scale."
        ])}
    chapters[10]["sections"] = [quadrilateral_opening.get(section["id"],section) for section in chapters[10]["sections"]]
    quadrilateral_properties = {
        "11.1.2": make_section("11.1.2 Rectangles", [
            "Rectangle JKLM has sides JK, KL, LM and MJ. Opposite sides are equal and parallel: JK=ML with JK∥ML, and KL=JM with KL∥JM.",
            "All four interior angles are right angles: angle JKL=angle KLM=angle LMJ=angle MJK=90°. Each adjacent side pair is perpendicular: JK⊥KL, KL⊥LM, LM⊥MJ and MJ⊥JK.",
            "A rectangle has two pairs of equal opposite parallel sides and four perpendicular adjacent pairs. A square is a special rectangle whose four sides are all equal."
        ]),
        "11.1.3": make_section("11.1.3 Parallelogram", [
            "In parallelogram ABCD, opposite sides are equal and parallel: AB=DC, AD=BC, AB∥DC and AD∥BC. Opposite angles are equal: a=c and b=d.",
            "Adjacent interior angles on the same side of a transversal between parallel sides sum to180°: a+b=180°, b+c=180°, c+d=180° and d+a=180°.",
            "Example1 (pp.200–201): EFGH is a parallelogram with angle EHG=98°. Find the other three angles. Angle EFG is opposite EHG, so angle EFG=98°. Angle HGF is adjacent to EHG, so angle HGF=180°−98°=82°. Angle HEF is opposite HGF, so angle HEF=82°. Check:98°+82°+98°+82°=360°."
        ]),
        "11.1.4": make_section("11.1.4 Rhombus", [
            "A rhombus is a parallelogram with all four sides equal. In rhombus ABCD, AB=BC=CD=DA; opposite sides are parallel, AB∥DC and AD∥BC.",
            "Opposite angles are equal: a=c and b=d. Each adjacent pair sums to180°: a+b, b+c, c+d and d+a are all180°. Equal side lengths do not require every angle to be90°; a square is the special rhombus with right angles.",
            "Example1 (p.201): in rhombus PQRS, angle QRS=70°. The opposite angle QPS=70°. The adjacent angle PSR=180°−70°=110°. Its opposite angle PQR=110°. Thus the three missing angles are P70°, Q110° and S110°. Check:70°+110°+70°+110°=360°."
        ])}
    chapters[10]["sections"] = [quadrilateral_properties.get(section["id"],section) for section in chapters[10]["sections"]]
    for index, section in enumerate(chapters[10]["sections"]):
        if section["id"] == "11.1.5":
            chapters[10]["sections"][index] = make_section("11.1.5 Trapezium", [
                "The textbook defines a trapezium as a quadrilateral with exactly one pair of opposite parallel sides. In ABCD, AB∥DC. The parallel sides need not be horizontal in a drawing.",
                "The two angles along each non-parallel side are supplementary: angle A+angle D=180° and angle B+angle C=180°. These are interior angles on the same side of a transversal between the parallel lines.",
                "Example1 (p.202): in trapezium EFGH, EF∥HG and angle E=55°. Find h at H. Along side EH, h+55°=180°, hence h=180°−55°=125°. The information does not determine F and G separately, although they also sum to180°."
            ])
    for example in chapters[10]["workedExamples"]:
        if example["id"] == "we-11-trapezium":
            example["problem"] = "In trapezium EFGH, EF is parallel to HG and angle E=55°. Find angle h at H."
            example["solution"] = "EH crosses the parallel sides EF and HG. The interior angles at E and H on the same side sum to180°. Thus h+55°=180° and h=125°. Check:55°+125°=180°."
            example["diagram"] = {"type":"labelled-polygon","title":"Trapezium EFGH: EF parallel to HG","points":[[75,60],[345,60],[305,235],[75+175/math.tan(math.radians(55)),235]],"names":["E","F","G","H"],"angles":["55°","","","h =125°"]}
    parallelogram_offset = 180*math.tan(math.radians(8))
    rhombus_side = 165
    rhombus_dx = rhombus_side*math.cos(math.radians(70))
    rhombus_dy = rhombus_side*math.sin(math.radians(70))
    labelled_examples = {
        "we-11-parallelogram": {"type":"labelled-polygon","title":"Parallelogram EFGH: opposite angles match","points":[[90-parallelogram_offset,50],[330-parallelogram_offset,50],[330,230],[90,230]],"names":["E","F","G","H"],"angles":["82°","98°","82°","98°"]},
        "we-11-rhombus": {"type":"labelled-polygon","title":"Rhombus PQRS: all four sides equal","points":[[75,55],[75+rhombus_side,55],[75+rhombus_side+rhombus_dx,55+rhombus_dy],[75+rhombus_dx,55+rhombus_dy]],"names":["P","Q","R","S"],"angles":["70°","110°","70°","110°"]},
        "we-11-kite": {"type":"labelled-polygon","title":"Kite ABCD: angles A and C are equal","points":[[185,65],[185+80/math.tan(math.radians(30)),145],[185,225],[185-80/math.tan(math.radians(40)),145]],"names":["A","B","C","D"],"angles":["110°","60°","110°","80°"]}
    }
    for example in chapters[10]["workedExamples"]:
        if example["id"] in labelled_examples:
            example["diagram"] = labelled_examples[example["id"]]
        if example["id"] == "we-11-kite":
            example["problem"] = "In kite ABCD, angle D=80°, angle B=60° and opposite angles A and C are equal. Find angles A and C."
            example["solution"] = r"The four interior angles sum to360°. Since A=C, \(A+60^\circ+A+80^\circ=360^\circ\). Combine terms: \(2A+140^\circ=360^\circ\). Subtract140°:2A=220°. Divide by2:A=110°. Hence C=110° too. Check:110°+60°+110°+80°=360°."
    polygon_review = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Review Exercise")
    for problem in polygon_review["problems"]:
        if problem["qNo"] == "6":
            problem["solution"] = "A regular polygon must have all sides equal and all interior angles equal. A convex polygon has no inward notch; a concave polygon has a reflex interior angle. (a) Convex triangle. The scan has no equal-side or angle marks, so it does not establish an equilateral triangle; do not assume regularity solely from this small sketch. If intended as equilateral, it is regular; otherwise it is irregular. (b) Irregular concave hexagon: the right-hand notch creates a reflex angle. (c) The intended square is regular and convex. (d) Irregular concave heptagon: the upper notch creates a reflex angle. (e) Irregular convex quadrilateral: unequal sides/angles, with no inward notch. (f) Irregular convex heptagon: tracing its outline gives seven sides, not six, and the lengths/angles are not all equal."
        elif problem["qNo"] == "7":
            problem["solution"] = "One sample is the six-sided polygon A(0,0), B(4,0), C(5,2), D(3,4), E(1,3), F(−1,1). Join the vertices in that order and close FA. It has6 sides, an even number, and AB=4 while BC=√5, so its sides are not all equal and it is irregular. Other irregular polygons with an even number of sides also satisfy the request."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Sample irregular hexagon (six sides)","points":[[110,235],[310,235],[360,135],[260,35],[160,85],[60,185]],"names":["A","B","C","D","E","F"]}
    for problem in polygon_review["problems"]:
        if problem["qNo"] == "8":
            problem["solution"] = "Sample answer: draw a regular pentagon ABCDE. Mark five points equally spaced around a circle, separated by360°/5=72° at the centre, then join neighbouring points. The five sides are equal and each interior angle is(5−2)×180°/5=108°. Five is odd, so the figure meets both requirements. Other regular polygons with an odd number of sides are also valid."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Sample regular pentagon: five equal sides","points":[[210+105*math.cos(-math.pi/2+i*2*math.pi/5),150+105*math.sin(-math.pi/2+i*2*math.pi/5)] for i in range(5)],"names":list("ABCDE")}
        elif problem["qNo"] == "9":
            problem["solution"] = "Sample answer: join A(0,0), B(4,0), C(4,4), D(2,2), E(0,4), then return to A. The boundary has exactly five sides and does not cross itself. D forms an inward notch: the interior angle there is270°, greater than180°. Therefore this is a concave pentagon."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Concave pentagon with an inward notch at D","points":[[100,250],[320,250],[320,30],[210,140],[100,30]],"names":list("ABCDE")}
        elif problem["qNo"] == "10":
            problem["solution"] = "One valid answer is a regular nonagon. Mark nine equally spaced points around a circle with central angle360°/9=40° between successive points, then join them in order. The polygon has nine sides and every interior angle is(9−2)×180°/9=140°, less than180°. It is therefore convex. The question does not require regularity; any simple convex nine-sided polygon is valid."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Sample convex nonagon: nine sides","points":[[210+105*math.cos(-math.pi/2+i*2*math.pi/9),150+105*math.sin(-math.pi/2+i*2*math.pi/9)] for i in range(9)],"names":list("ABCDEFGHI")}
    for problem in polygon_review["problems"]:
        if problem["qNo"] == "1":
            problem["question"] = "Encircle the correct option (p.217).\n(a) The longest chord of the circle is: (i) radius (ii) segment (iii) diameter (iv) sectors.\n(b) A circle is a plane figure that is a set of: (i) points (ii) lines (iii) segments (iv) sectors.\n(c) 'The angle of the semicircle' is a/an ___ angle: (i) right (ii) obtuse (iii) acute (iv) straight.\n(d) Which has no line of symmetry? (i) square (ii) rectangle (iii) rhombus (iv) parallelogram.\n(e) Which has only one pair of parallel sides? (i) trapezium (ii) square (iii) rectangle (iv) parallelogram.\n(f) A polygon with no interior reflex angles is: (i) right polygon (ii) convex polygon (iii) concave polygon (iv) reflex polygon."
            problem["solution"] = "(a)(iii) Diameter: it joins two circle points through the centre and is the longest chord. (b)(i) Points: every point of a circle is the same distance from its centre. (c) The source wording is ambiguous. The standard theorem 'angle in a semicircle' means the angle at a circumference point subtended by a diameter; that angle is90°, option(i), right. The angle at the centre spanning a semicircle is180°, option(iv), straight. These are different angles; use the intended angle-in-a-semicircle theorem for the book's answer. (d)(iv) An ordinary oblique parallelogram has no reflection line. Special parallelograms such as squares, rectangles and rhombuses do have lines, so this choice refers to the ordinary pictured/type example. (e)(i) Trapezium, using this book's exactly-one-parallel-pair definition. (f)(ii) Convex polygon: none of its interior angles exceeds180°; a concave polygon has a reflex interior angle."
        elif problem["qNo"] == "2":
            problem["solution"] = "A convex polygon has every interior angle less than180°; every segment joining two points inside it stays inside or on its boundary. A concave polygon has at least one reflex interior angle greater than180° and an inward notch; some segment joining two interior points passes outside it. Examples are a square (convex) and an indented pentagon (concave). These statements concern simple non-degenerate polygons."
    for problem in polygon_review["problems"]:
        if problem["qNo"] == "3":
            problem["solution"] = "Draw a circle with compass centre O. Label opposite ends of a straight line through O as A and B. Mark C at the bottom of the circle, and D and E on the upper circumference; join OC and DE. Centre O is equally distant from every point on the circumference. Radius OC joins the centre to the circumference. Diameter AB passes through O and equals two radii. Chord DE joins two circumference points; AB is also a chord. The shorter curved path from D to E is the minor arc; the longer path through C is the major arc DCE. Diameter AB divides the circular region into two semicircles; the lower one is bounded by AB and arc ACB. The shaded minor segment is bounded by chord DE and the minor arc DE. A segment has one chord boundary, unlike a sector, which has two radius boundaries."
            problem["solutionDiagram"] = {"type":"circle-parts","title":"Review Q3: labelled parts of a circle"}
    for problem in circle_exercise["problems"]:
        if problem["qNo"] == "2":
            problem["solution"] = "Set the compass opening to5 cm and draw a circle with centre O. Mark radius OC=5 cm and diameter AB=10 cm. Choose two other circumference points D and E and join them to form a chord. Label the shorter arc DE and longer arc DCE; shade the region between chord DE and its shorter arc as a minor segment. Diameter AB divides the circle into two semicircles. The displayed diagram illustrates the labels; use a ruler and compass for an actual5 cm radius on paper."
            problem["solutionDiagram"] = {"type":"circle-parts","title":"Circle of radius5 cm: OC=5 cm; AB=10 cm"}
    for index, section in enumerate(chapters[10]["sections"]):
        if section["id"] == "11.2":
            chapters[10]["sections"][index] = make_section("11.2 Polygons", [
                "A polygon is a closed plane figure made from three or more straight line segments called sides. Triangles and quadrilaterals are polygons. In this unit the sides meet only at their endpoints and do not cross each other.",
                "A closed figure can be traced from a starting point back to the same point without a break. Being closed alone does not make a figure a polygon: its boundary must also consist of straight segments. The curved outline in the source note illustrates closure, not a polygon."
            ])
        elif section["id"] == "11.2.1":
            chapters[10]["sections"][index] = make_section("11.2.1 Types of Polygon", [
                "Name a polygon by counting its straight sides once around the boundary. Its number of vertices equals its number of sides.",
                "Triangle:3 sides. Quadrilateral:4 sides. Pentagon:5 sides. Hexagon:6 sides. Heptagon:7 sides. Octagon:8 sides.",
                "The source shows both outward-pointing and indented examples of several types. An inward notch does not change how sides are counted: follow every change of direction along the boundary. Both convex and concave five-sided figures are pentagons.",
                "Naming note: penta means five, hexa six, hepta seven, octa eight, nona nine and deca ten. Thus a nonagon has9 sides and a decagon10. Whether a polygon is regular or irregular is a separate question from its name by side count."
            ])
    chapters[10]["workedExamples"].append({"id":"we-11-polygon-count","title":"Reading the polygon examples (p.205)","problem":"How can an indented figure still be a pentagon, hexagon, heptagon or octagon?","solution":"Start at one vertex, follow the entire boundary and count each straight segment exactly once, including those around an inward notch. Five segments give a pentagon, six a hexagon, seven a heptagon and eight an octagon. An indentation makes the polygon concave but does not prevent it from being named by its number of sides. In the sample below, AB,BC,CD,DE and EA are the five sides; D is the inward vertex.","diagram":{"type":"labelled-polygon","title":"Five sides: a concave pentagon","points":[[90,245],[330,245],[330,50],[210,145],[90,50]],"names":list("ABCDE")}})
    polygon_exercise = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Exercise 11.2")
    polygon_exercise["exercise"] = "2"
    for problem in polygon_exercise["problems"]:
        if problem["qNo"] == "1":
            problem["solution"] = "Read each row from left to right. Top row (eight figures):1 regular,2 regular,3 irregular,4 irregular,5 irregular,6 regular,7 irregular,8 irregular. Bottom row (seven figures):1 regular,2 irregular,3 regular,4 regular,5 regular,6 irregular,7 irregular. A regular polygon has both equal sides and equal interior angles. The notched figures are concave, so they cannot be regular. The bottom-row rectangle is not a square: equal right angles alone are insufficient because its side lengths are not all equal. Rotating the square into a diamond orientation does not change its regularity. These classifications follow the intended equal-sided regular drawings in the textbook."
        elif problem["qNo"] == "2":
            problem["solution"] = "Sample: join A(0,0), B(4,0), C(5,2), D(2,4), E(0,2), then close EA. There are five sides, an odd number. AB=4 while EA=2, so not all sides are equal and the pentagon is irregular. Many other odd-sided irregular polygons are valid."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Sample irregular pentagon: five sides","points":[[85,250],[285,250],[335,150],[185,50],[85,150]],"names":list("ABCDE")}
        elif problem["qNo"] == "3":
            problem["solution"] = "Sample: draw a regular hexagon. Mark six points equally spaced around a circle,60° apart at the centre, and join consecutive points. All six sides are equal and each interior angle is120°. Six is even, so the shape meets both requirements. A square or regular octagon would also work."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Sample regular hexagon: six equal sides","points":[[210+105*math.cos(i*math.pi/3),150+105*math.sin(i*math.pi/3)] for i in range(6)],"names":list("ABCDEF")}
        elif problem["qNo"] == "4":
            problem["solution"] = "Sample: join A(0,0), B(4,0), C(4,4), D(2,2), E(0,4), then return to A. Count the five straight sides. D is an inward notch with a270° interior angle, so the polygon is concave. The boundary does not cross itself."
            problem["solutionDiagram"] = {"type":"labelled-polygon","title":"Sample concave pentagon","points":[[100,250],[320,250],[320,30],[210,140],[100,30]],"names":list("ABCDE")}
    angles_exercise = next(ex for ex in chapters[10]["exercises"] if ex["title"] == "Exercise 11.3")
    for problem in angles_exercise["problems"]:
        if problem["qNo"] == "2":
            problem["solution"] = r"For an n-sided simple polygon, \(S=(n-2)\times180^\circ\). Substitute each side count:6 sides:(6−2)×180°=720°;9 sides:(9−2)×180°=1260°;11 sides:(11−2)×180°=1620°;15 sides:(15−2)×180°=2340°;20 sides:(20−2)×180°=3240°;18 sides:(18−2)×180°=2880°. These are sums of all interior angles, not single angles."
            problem["solutionDiagram"] = {"type":"frequency-table","title":"Completed interior-angle-sum table","headers":["Sides n","Calculation","Interior-angle sum"],"rows":[[n,f"({n}−2) ×180°",str((n-2)*180)+"°"] for n in [6,9,11,15,20,18]]}
        elif problem["qNo"] == "3":
            problem["solution"] = r"Regular polygons have equal interior angles. Divide the total interior-angle sum by n: \(I=\frac{(n-2)180^\circ}{n}\). (a)5 sides:540°/5=108°. (b)6 sides:720°/6=120°. (c)8 sides:1080°/8=135°. (d)10 sides:1440°/10=144°. (e)13 sides:1980°/13≈152.31°. (f)20 sides:3240°/20=162°. Keep1980°/13 as the exact answer for(e); the decimal is rounded."
            problem["solutionDiagram"] = {"type":"frequency-table","title":"Each interior angle of a regular polygon","headers":["Part","Sides","Angle sum","Divide by sides"],"rows":[["a",5,"540°","108°"],["b",6,"720°","120°"],["c",8,"1080°","135°"],["d",10,"1440°","144°"],["e",13,"1980°","1980°/13 ≈152.31°"],["f",20,"3240°","162°"]]}
    review_angle_solutions = {
        "11": r"For a regular n-sided polygon, each interior angle is \(I=\frac{(n-2)180^\circ}{n}\). (a)n=5: total=(5−2)×180°=540°; each=540°/5=108°. (b)n=10: total=8×180°=1440°; each=1440°/10=144°. (c)n=7: total=5×180°=900°; each=900°/7≈128.57°. The fraction is exact; the decimal is rounded.",
        "12": "(a) Extend side BC of triangle ABC to D. Angle ACD is the exterior angle at C. Triangle sum gives A+B+C=180°, and the straight line gives C+ACD=180°. Subtract C from both equalities: ACD=A+B, the sum of the two non-adjacent interior angles. (b) An interior angle and its adjacent exterior angle form a linear pair and sum to180°. For a convex polygon, one consistently chosen exterior angle at each vertex totals360°, one full turn. Hence in a regular n-sided polygon each exterior angle is360°/n and each interior angle is180°−360°/n. For concave polygons, the full-turn rule uses signed turning angles; do not simply add unsigned exterior angles without a convention.",
        "13": r"Use \(S=(n-2)180^\circ\). (a)5 sides:(5−2)×180°=3×180°=540°. (b)3 sides:(3−2)×180°=180°. (c)7 sides:(7−2)×180°=5×180°=900°. (d)4 sides:(4−2)×180°=2×180°=360°. (e)8 sides:(8−2)×180°=6×180°=1080°. Regularity is not required for these sums.",
        "14": "A regular4-sided polygon has four equal exterior angles summing to360°. Each=360°/4=90°. Check:4×90°=360°.",
        "15": "The interior-angle sum of a pentagon is(5−2)×180°=540°. Regularity makes its five angles equal, so each=540°/5=108°. Equivalently, exterior angle=360°/5=72° and interior=180°−72°=108°.",
        "16": "A regular hexagon has six equal exterior angles summing to360°. Each=360°/6=60°. Its adjacent interior angle is180°−60°=120°.",
        "17": "An octagon's interior-angle sum is(8−2)×180°=1080°. Divide equally among eight vertices:1080°/8=135°. Check using its exterior angle:360°/8=45°, and135°+45°=180°."
    }
    for problem in polygon_review["problems"]:
        if problem["qNo"] in review_angle_solutions:
            problem["solution"] = review_angle_solutions[problem["qNo"]]
        if problem["qNo"] == "Project":
            problem["solutionDiagram"] = {"type":"frequency-table","title":"Sample quadrilateral comparison","headers":["Pair","Similarities","Differences"],"rows":[["Square / rectangle","Four right angles; opposite sides parallel","Square has all sides equal; a non-square rectangle does not"],["Square / rhombus","Four equal sides; opposite sides parallel","Square has four right angles; a non-square rhombus does not"],["Trapezium / parallelogram","Four sides; at least one parallel pair","Exactly one parallel pair versus two, using the book's definition"]]}
    for problem in polygon_review["problems"]:
        if problem["qNo"] == "4":
            problem["solution"] = "Every quadrilateral has four sides and interior-angle sum360°. Square: all four sides equal, opposite sides parallel, all angles90° and four symmetry lines. Rectangle: opposite sides equal and parallel, all angles90°; a non-square rectangle has two symmetry lines. Parallelogram: opposite sides equal and parallel, opposite angles equal, adjacent angles sum to180°; an ordinary oblique parallelogram has no reflection line. Rhombus: four equal sides, opposite sides parallel, opposite angles equal, adjacent angles supplementary; a non-square rhombus has two symmetry lines along its diagonals. Trapezium: exactly one pair of parallel opposite sides under the book's definition; angles along either non-parallel side sum to180°. A general trapezium has no symmetry line, while an isosceles trapezium has one. Kite: two pairs of adjacent equal sides; the opposite angles between unequal sides are equal. An ordinary kite has one symmetry line through the vertices where the equal-side pairs meet. Squares are special rectangles and rhombuses, so specify the non-square cases when counting symmetry lines."
            problem["solutionDiagram"] = {"type":"frequency-table","title":"Quadrilateral properties","headers":["Shape","Equal sides","Parallel pairs","Angle property"],"rows":[["Square","All four",2,"All90°"],["Rectangle","Opposite pairs",2,"All90°"],["Parallelogram","Opposite pairs",2,"Opposite equal; adjacent sum180°"],["Rhombus","All four",2,"Opposite equal; adjacent sum180°"],["Trapezium","Not required",1,"Angles along each non-parallel side sum180°"],["Kite","Two adjacent pairs","Not required","One opposite pair equal (ordinary kite)"]]}
        elif problem["qNo"] == "5":
            problem["question"] = "Look at the figures and fill in the blanks (pp.217–218). (a) ABCD is a rhombus, AB=10 cm; x,y,z,w label angles A,B,C,D respectively. Find the remaining side lengths, then(i) angle x,(ii) x+y,(iii) w+x. (b) PQRS is a parallelogram with angles o,l,m,n at P,Q,R,S respectively. Complete(i) l+m+n+o;(ii) m=___ and l=___. (c) ABCD is a trapezium with AB parallel to DC and angles x,y,z,w at A,B,C,D respectively. Complete(i) z+y;(ii) w+x;(iii) x+y+z+w;(iv) the only pair of parallel sides."
            problem["solution"] = "(a) Equal rhombus sides give BC=CD=DA=10 cm. (i)x=z because opposite angles are equal; no numerical value of x is determined by the10 cm side length. (ii)x+y=180° because adjacent angles are supplementary. (iii)w+x=180° for the same reason. (b)(i)l+m+n+o=360°, the quadrilateral angle sum. (ii)m=o and l=n because opposite parallelogram angles are equal. (c)(i)z+y=180°, the interior angles along transversal BC between AB and DC. (ii)w+x=180°, along transversal AD. (iii)x+y+z+w=360°. (iv)AB and DC are the only parallel pair."
    # Printed p.205: the first outline is a square rotated onto a vertex.
    symmetry_q7 = next(problem for ex in chapters[10]["exercises"] if ex["title"] == "Exercise 11.1" for problem in ex["problems"] if str(problem["qNo"]) == "7")
    symmetry_q7["question"] = "Draw the lines of symmetry for each of the five pictured quadrilaterals, from left to right (p.205)."
    symmetry_q7["solution"] = "(a) The rotated square has four lines of symmetry: its two diagonals and the two lines joining midpoints of opposite sides. Turning a square does not change its symmetry. (b) The non-isosceles trapezium has no line of symmetry. (c) The intended isosceles trapezium has one line: the perpendicular bisector of its parallel bases. (d) The ordinary oblique parallelogram has no line of symmetry. (e) The kite has one line through the two vertices where equal adjacent sides meet. To check a proposed line, reflect the whole outline across it: both halves must coincide."
    symmetry_q7["solutionDiagram"]["panels"][0] = {
        "title": "Rotated square: four lines",
        "points": [[150,35],[235,120],[150,205],[65,120]],
        "axes": [[150,15,150,225],[45,120,255,120],[65,35,235,205],[65,205,235,35]]
    }

    # Native redrawings of the regular/irregular examples on printed p.206.
    def regular_gallery_polygon(n, title, fill):
        return {"title":title,"fill":fill,"points":[[math.cos(-math.pi/2 + 2*math.pi*i/n),math.sin(-math.pi/2 + 2*math.pi*i/n)] for i in range(n)]}
    regular_panels = [
        {"title":"Regular quadrilateral (square)","fill":"#67e8f9","points":[[0,0],[1,0],[1,1],[0,1]]},
        regular_gallery_polygon(6,"Regular hexagon","#86efac"),
        regular_gallery_polygon(8,"Regular octagon","#f9a8d4")
    ]
    irregular_panels = [
        {"title":"Irregular pentagon","fill":"#67e8f9","points":[[75,233],[154,262],[111,275],[99,304],[62,274]]},
        {"title":"Irregular hexagon","fill":"#86efac","points":[[259,247],[289,228],[335,267],[286,301],[289,279],[259,307]]},
        {"title":"Irregular heptagon","fill":"#fca5a5","points":[[422,255],[456,245],[469,270],[456,288],[475,305],[426,305],[402,282]]},
        {"title":"Irregular octagon","fill":"#f9a8d4","points":[[58,340],[102,362],[146,335],[178,385],[136,366],[107,394],[69,409],[80,379]]},
        {"title":"Irregular nonagon","fill":"#a5f3fc","points":[[280,350],[338,366],[331,408],[307,408],[295,385],[264,412],[253,377],[295,368],[265,360]]},
        {"title":"Irregular decagon","fill":"#fde68a","points":[[401,347],[431,354],[441,369],[450,354],[485,348],[485,408],[457,401],[443,384],[438,396],[402,406]]}
    ]
    next(section for section in chapters[10]["sections"] if section["id"]=="11.2.2")["diagram"] = {"type":"polygon-gallery","panels":regular_panels+irregular_panels}
    convex_panels = [regular_gallery_polygon(n,name,"#bae6fd") for n,name in [(3,"Convex triangle"),(5,"Convex pentagon"),(6,"Convex hexagon"),(7,"Convex heptagon"),(8,"Convex octagon")]]
    convex_panels.append({"title":"Concave polygon: inward corner","fill":"#c4b5fd","points":[[263,677],[297,690],[330,676],[341,702],[319,720],[275,721]]})
    next(section for section in chapters[10]["sections"] if section["id"]=="11.2.3")["diagram"] = {"type":"polygon-gallery","panels":convex_panels}

    # Exercise 11.2 p.207: restore all figures, preserving row-position labels.
    polygon_question = next(problem for ex in chapters[10]["exercises"] if ex["title"]=="Exercise 11.2" for problem in ex["problems"] if str(problem["qNo"])=="1")
    polygon_question["question"] = "Identify the regular and irregular polygons among the following figures. Justify your answer. The figures are labelled by their position in the textbook: top row 1–8, then bottom row 1–7."
    polygon_question["diagram"] = {"type":"polygon-gallery","panels":[
        regular_gallery_polygon(3,"Top row 1","#f9a8d4"),
        regular_gallery_polygon(8,"Top row 2","#99f6e4"),
        {"title":"Top row 3","fill":"#bef264","points":[[218,166],[232,144],[244,134],[265,144],[257,169],[244,158]]},
        {"title":"Top row 4","fill":"#fbcfe8","points":[[285,164],[294,153],[285,146],[296,123],[322,130],[307,149],[320,159]]},
        {"title":"Top row 5","fill":"#cffafe","points":[[337,139],[349,123],[368,119],[391,125],[375,153],[362,133]]},
        regular_gallery_polygon(7,"Top row 6","#67e8f9"),
        {"title":"Top row 7","fill":"#6ee7b7","points":[[465,148],[497,120],[510,148]]},
        {"title":"Top row 8","fill":"#e2e8f0","points":[[522,129],[531,124],[574,121],[578,149],[548,157],[546,148],[531,152],[525,139],[530,135]]},
        {"title":"Bottom row 1","fill":"#f8fafc","points":[[0,0],[1,0],[1,1],[0,1]]},
        {"title":"Bottom row 2","fill":"#fca5a5","points":[[0,0],[1.6,0],[1.6,1],[0,1]]},
        regular_gallery_polygon(6,"Bottom row 3","#fef08a"),
        regular_gallery_polygon(5,"Bottom row 4","#fde68a"),
        regular_gallery_polygon(4,"Bottom row 5","#67e8f9"),
        {"title":"Bottom row 6","fill":"#fbcfe8","points":[[440,190],[472,205],[501,188],[479,216],[513,229],[473,221],[447,229],[454,213]]},
        {"title":"Bottom row 7","fill":"#f8fafc","points":[[518,217],[524,188],[538,208],[548,193],[559,209],[577,214],[568,230],[553,216],[547,212],[540,220]]}
    ]}

    # Printed pp.207–208: table and triangle partitions accompany the proof.
    interior_section = next(section for section in chapters[10]["sections"] if section["id"]=="11.3.1")
    interior_section["diagram"] = {"type":"diagram-group","items":[
        {"type":"frequency-table","title":"Sum of interior angles (p.207)","columns":["Polygon","Number of sides","Calculation","Sum"],"rows":[[name,str(n),f"180° × ({n} − 2) = 180° × {n-2}",f"{180*(n-2)}°"] for n,name in [(3,"Triangle"),(4,"Quadrilateral"),(5,"Pentagon"),(6,"Hexagon"),(7,"Heptagon"),(8,"Octagon")]]},
        {"type":"polygon-triangulations","sides":[3,4,5]}
    ]}
    pentagon_example = {
        "id":"we-11-interior-pentagon-source",
        "title":"Interior angle of a regular pentagon (p.208)",
        "problem":"Find each interior angle of a regular pentagon.",
        "solution":r"A pentagon has five sides. Its interior-angle sum is \(180^\circ(5-2)=540^\circ\). Because the pentagon is regular, its five interior angles are equal. Divide the total equally: \(\frac{540^\circ}{5}=108^\circ\). Check: \(5\times108^\circ=540^\circ\).",
        "diagram":{"type":"labelled-polygon","title":"Regular pentagon: each interior angle is 108°","points":[[210+110*math.cos(-math.pi/2+i*2*math.pi/5),150+110*math.sin(-math.pi/2+i*2*math.pi/5)] for i in range(5)],"names":["A","B","C","D","E"],"angles":["108°"]*5}
    }
    chapters[10]["workedExamples"] = [example for example in chapters[10]["workedExamples"] if example["id"]!=pentagon_example["id"]] + [pentagon_example]

    # Printed p.209: retain separate worked cases and the exact heptagon value.
    interior_examples = [
        (6,"hexagon",r"\frac{180^\circ(6-2)}{6}=\frac{720^\circ}{6}=120^\circ", "120°"),
        (7,"heptagon",r"\frac{180^\circ(7-2)}{7}=\frac{900^\circ}{7}=128\frac{4}{7}^\circ\approx128.57^\circ", "900°/7"),
        (8,"octagon",r"\frac{180^\circ(8-2)}{8}=\frac{1080^\circ}{8}=135^\circ", "135°")
    ]
    for n,name,working,angle_label in interior_examples:
        example_id=f"we-11-interior-{name}-source"
        solution = f"A {name} has {n} sides. Joining one vertex to the non-adjacent vertices divides it into {n-2} triangles. The sum of its interior angles is {n-2} × 180° = {(n-2)*180}°. Since the polygon is regular, divide by {n} equal angles: \\(" + working + r"\)."
        if n==7:
            solution += " The printed 128.5° is a truncated approximation. The exact answer is 900°/7; rounded to one decimal place it is 128.6°, or to two decimal places 128.57°. Keep the exact fraction when checking that seven angles total 900°."
        example={"id":example_id,"title":f"Interior angle of a regular {name} (p.209)","problem":f"Find each interior angle of a regular {name}.","solution":solution,"diagram":{"type":"labelled-polygon","title":f"Regular {name}: {angle_label} at every vertex","points":[[210+115*math.cos(-math.pi/2+i*2*math.pi/n),150+115*math.sin(-math.pi/2+i*2*math.pi/n)] for i in range(n)],"names":list("ABCDEFGH"[:n]),"angles":[angle_label]+[""]*(n-1)}}
        chapters[10]["workedExamples"]=[e for e in chapters[10]["workedExamples"] if e["id"]!=example_id]+[example]
    quick_interior=next(e for e in chapters[10]["workedExamples"] if e["id"]=="we-11-polygon-sum")
    quick_interior["solution"]=r"Each angle of a regular n-sided polygon is \(\frac{180^\circ(n-2)}{n}\). (a) Nine sides: sum \(180^\circ(9-2)=1260^\circ\), so each angle is \(1260^\circ/9=140^\circ\). (b) Twelve sides: sum \(180^\circ(12-2)=1800^\circ\), so each angle is \(1800^\circ/12=150^\circ\). (c) Twenty sides: sum \(180^\circ(20-2)=3240^\circ\), so each angle is \(3240^\circ/20=162^\circ\). Multiplying each answer by its number of sides recovers its interior-angle sum."
    quick_interior["diagram"]={"type":"frequency-table","title":"Quick Check answers (p.209)","columns":["Part","Sides","Sum of interior angles","Each interior angle"],"rows":[["a","9","1260°","140°"],["b","12","1800°","150°"],["c","20","3240°","162°"]]}

    # Printed pp.210–211: side-extension diagrams and exterior-angle table.
    exterior_section=next(section for section in chapters[10]["sections"] if section["id"]=="11.3.3")
    exterior_section["diagram"]={"type":"diagram-group","items":[
        {"type":"exterior-angle-proof","mode":"triangle","title":"Triangle PQR: QR extended through R to S"},
        {"type":"exterior-angle-proof","mode":"pentagon","title":"Pentagon: extend each side in the same direction"},
        {"type":"frequency-table","title":"Exterior angles of regular polygons (p.211)","columns":["Regular polygon","Sides","Each exterior angle"],"rows":[["Triangle","3","360° ÷ 3 = 120°"],["Square","4","360° ÷ 4 = 90°"],["Pentagon","5","360° ÷ 5 = 72°"],["Hexagon","6","360° ÷ 6 = 60°"],["Heptagon","7","360° ÷ 7 ≈ 51.43°"],["Octagon","8","360° ÷ 8 = 45°"]]}
    ]}
    exterior_example=next(e for e in chapters[10]["workedExamples"] if e["id"]=="we-11-polygon-exterior")
    exterior_example["problem"]="Find each exterior angle of a regular octagon. Explain why one exterior angle at each vertex of a convex polygon totals 360°."
    exterior_example["solution"]=r"At every vertex, the interior angle and its adjacent exterior angle make a straight angle of \(180^\circ\). For n vertices their total is \(180^\circ n\). Subtract the interior-angle sum: \(180^\circ n-180^\circ(n-2)=360^\circ\). In a regular octagon the eight exterior angles are equal, so each is \(360^\circ/8=45^\circ\). Its interior angle is \(180^\circ-45^\circ=135^\circ\). Check: \(8\times45^\circ=360^\circ\). For concave polygons the full-turn result uses signed turning angles; do not add unsigned reflex-vertex turns as if every vertex were convex."

    # Exercise11.3 p.212: full reasoning and clean exercise-specific key.
    interior_exercise=next(ex for ex in chapters[10]["exercises"] if ex["title"]=="Exercise 11.3")
    interior_exercise["exercise"]="3"
    for problem in interior_exercise["problems"]:
        q=str(problem["qNo"])
        if q=="1":
            problem["diagram"]={"type":"polygon-gallery","panels":[regular_gallery_polygon(n,f"Figure {i+1}",color) for i,(n,color) in enumerate([(7,"#6ee7b7"),(8,"#f9a8d4"),(9,"#67e8f9"),(10,"#fef08a")])]}
        elif q=="4":
            problem["solution"]=r"(a) The interior angle at C and the exterior 160° angle form a straight line: \(\angle C=180^\circ-160^\circ=20^\circ\). In triangle SBC, \(x+3x+20^\circ=180^\circ\), so \(4x=160^\circ\) and \(x=40^\circ\). The angle labelled 3x is \(120^\circ\). Check: \(40^\circ+120^\circ+20^\circ=180^\circ\). (b) The exterior angle x is adjacent to 92°: \(x=180^\circ-92^\circ=88^\circ\). The remaining interior angle is \(y=180^\circ-92^\circ-41^\circ=47^\circ\). Check with the exterior-angle theorem: \(x=y+41^\circ=88^\circ\)."
        elif q in ("5","7"):
            n=8 if q=="5" else 9; result=360//n
            problem["solution"]=f"The exterior angles total 360°. The regular polygon has {n} equal exterior angles. Therefore each exterior angle is \\(360^\\circ/{n}={result}^\\circ\\). Check: {n} × {result}° = 360°."
        elif q=="6":
            problem["solution"]=r"A hexagon has six sides. Its interior-angle sum is \((6-2)\times180^\circ=720^\circ\). Regularity makes the six angles equal, so each interior angle is \(720^\circ/6=120^\circ\). Its adjacent exterior angle is 60°, and \(120^\circ+60^\circ=180^\circ\)."
        elif q=="8":
            problem["solution"]=r"An 11-sided polygon has interior-angle sum \((11-2)\times180^\circ=1620^\circ\). Divide equally among its 11 angles: \(I=\frac{1620^\circ}{11}=147\frac{3}{11}^\circ\approx147.27^\circ\). The fraction is exact; the decimal is rounded to two places. Check using the exact result: \(11\times\frac{1620^\circ}{11}=1620^\circ\)."
    interior_exercise["answerKeyText"]="1. 900°,1080°,1260°,1440°. 2. 720°,1260°,1620°,2340°,3240°,2880°. 3. a108°,b120°,c135°,d144°,e1980°/13≈152.31°,f162°. 4. a x40° and3x120°; b x88°,y47°. 5.45°. 6.120°. 7.40°. 8.1620°/11≈147.27°. 9.143°. 10. a145°; b103°; c n113°,n+6=119°; d130°; e110°."

    # Exercise11.3 Q4: question diagrams retain unknowns until solution is opened.
    missing_angle_question=next(p for p in interior_exercise["problems"] if str(p["qNo"])=="4")
    missing_angle_question["diagram"]={"type":"diagram-group","items":[
        {"type":"annotated-angle-figure","title":"4(a): find x and the angle labelled 3x (schematic)",
         "points":[[65,170],[175,220],[330,120]],
         "extensions":[[330,120,370,94]],
         "labels":[[51,166,"S"],[175,244,"B"],[333,140,"C"],[98,178,"x"],[180,202,"3x"],[302,91,"160°"]]},
        {"type":"annotated-angle-figure","title":"4(b): find x and y (schematic)",
         "points":[[95,45],[285,118],[190,265]],"extensions":[[285,118,370,151]],
         "labels":[[120,83,"y"],[257,131,"92°"],[195,229,"41°"],[310,151,"x"]]}
    ]}

    # Printed p.213: all five unknown-angle figures, with source vertex labels.
    polygon_q10=next(p for p in interior_exercise["problems"] if str(p["qNo"])=="10")
    polygon_q10["diagram"]={"type":"diagram-group","items":[
        {"type":"labelled-polygon","title":"10(a): seven-sided polygon (schematic)","points":[[145,60],[255,45],[325,125],[310,220],[205,270],[105,235],[75,145]],"names":["S","T","V","W","X","Y","R"],"angles":["129°","116°","120°","y°","125°","135°","130°"]},
        {"type":"labelled-polygon","title":"10(b): pentagon (schematic)","points":[[170,50],[340,100],[315,235],[135,265],[55,155]],"names":["P","M","N","Q","O"],"angles":["117°","100°","x°","115°","105°"]},
        {"type":"labelled-polygon","title":"10(c): hexagon (schematic)","points":[[265,40],[360,70],[350,160],[165,270],[65,240],[75,140]],"names":["A","B","C","D","E","F"],"angles":["135°","62°","151°","140°","n°","(n+6)°"]},
        {"type":"labelled-polygon","title":"10(d): find angle A (schematic)","points":[[210,40],[320,120],[320,255],[100,255],[100,120]],"names":["A","B","C","D","E"],"angles":["?","115°","90°","90°","115°"]},
        {"type":"labelled-polygon","title":"10(e): hexagon (schematic)","points":[[160,95],[295,35],[350,165],[280,260],[200,260],[150,240]],"names":["","","","","",""],"angles":["120°","90°","110°","130°","160°","x°"]}
    ]}
    next(p for p in interior_exercise["problems"] if str(p["qNo"])=="9")["solution"]=r"A pentagon has five sides, so the sum of its interior angles is \((5-2)\times180^\circ=540^\circ\). Add the four known angles: \(115^\circ+92^\circ+107^\circ+83^\circ=397^\circ\). The fifth angle is \(540^\circ-397^\circ=143^\circ\). Check: \(397^\circ+143^\circ=540^\circ\)."
    polygon_q10["solution"]=r"Use \(S=(k-2)180^\circ\), where k is the number of sides. (a) Seven sides give \(S=900^\circ\). The known angles total \(129+116+120+125+135+130=755^\circ\), so \(y=900^\circ-755^\circ=145^\circ\). (b) Five sides give \(S=540^\circ\). Thus \(x=540^\circ-(105+117+100+115)^\circ=103^\circ\). (c) Six sides give \(S=720^\circ\). The four numerical angles total488°, so \(n+(n+6)=720-488=232\). Hence \(2n=226\), \(n=113\), and the angle labelled \((n+6)^\circ\) is119°. (d) Five sides give540°. The square corner marks mean90° each, so \(A=540^\circ-115^\circ-115^\circ-90^\circ-90^\circ=130^\circ\). (e) Count all six vertices, including the lower-left bend marked160°. Then \(x=720^\circ-(120+90+110+130+160)^\circ=110^\circ\). Check each answer by adding it to the given angles and recovering the appropriate polygon sum."

    # Circle figures on p.214 use distinct source labels for each construction.
    circle_lesson=next(section for section in chapters[10]["sections"] if section["id"]=="11.4")
    circle_lesson["diagram"]={"type":"diagram-group","items":[
        {"type":"source-labelled-circle","title":"Radius AB: A is the centre","centre":"A","points":{"B":225},"lines":[["A","B"]]},
        {"type":"source-labelled-circle","title":"Diameter BC passes through centre A","centre":"A","points":{"B":225,"C":45},"lines":[["B","C"]]},
        {"type":"source-labelled-circle","title":"Chords PQ and RT; diameter BC","centre":"A","points":{"P":190,"Q":95,"R":275,"T":10,"B":230,"C":50},"lines":[["P","Q"],["R","T"],["B","C"]]},
        {"type":"source-labelled-circle","title":"Chord PQ: shaded minor segment PDQ and major segment PEQ","centre":"O","points":{"P":225,"D":270,"Q":315,"E":90},"lines":[["P","Q"]],"segment":["P","Q"]}
    ]}

    # Printed p.215: preserve source letter positions in circle exercise figures.
    circle_exercise=next(ex for ex in chapters[10]["exercises"] if ex["title"]=="Exercise 11.4")
    circle_exercise["exercise"]="4"
    circle_question=next(p for p in circle_exercise["problems"] if str(p["qNo"])=="1")
    circle_question["diagram"]={"type":"diagram-group","items":[
        {"type":"source-labelled-circle","title":"1(a): label the parts of the circle","centre":"O","points":{"A":180,"B":0,"C":40,"P":210,"Q":305},"lines":[["A","B"],["O","C"],["P","Q"]]},
        {"type":"source-labelled-circle","title":"1(b): label the parts of the circle","centre":"O","points":{"A":225,"B":325,"C":165,"D":45,"U":195,"V":15},"lines":[["A","B"],["C","D"],["U","V"]],"hiddenLabels":["U","V"]}
    ]}
    circle_lesson["diagram"]["items"].extend([
        {"type":"source-labelled-circle","title":"Minor arc BC; major arc BDC passes through D","centre":"O","points":{"B":20,"C":160,"D":270},"lines":[["O","B"],["O","C"]]},
        {"type":"source-labelled-circle","title":"Diameter BC divides the circle into two semicircles","centre":"O","points":{"B":315,"C":135},"lines":[["B","C"]]}
    ])
    next(p for p in circle_exercise["problems"] if str(p["qNo"])=="3")["solution"]="Choose a centre O and set a compass to any convenient fixed radius. Draw the complete circle without changing the opening. Mark three different boundary points A, B and C. Use a ruler to join O to each point. OA, OB and OC are three radii, and OA=OB=OC because all boundary points are the same distance from O. A radius ends at the centre and one boundary point; do not extend it across the circle unless you want a diameter."

    # Printed p.216: source Think Higher diagrams and vocabulary.
    for problem in circle_exercise["problems"]:
        if str(problem["qNo"])=="Think Higher 1":
            problem["diagram"]={"type":"annotated-angle-figure","title":"Think Higher 1: ∠CAD = ∠ADC (schematic)","points":[[75,230],[160,65],[345,230]],"extensions":[[160,65,160,230],[345,230,405,230]],"labels":[[65,250,"B"],[160,50,"A"],[160,250,"C"],[345,250,"D"],[110,217,"60°"],[361,207,"150°"]]}
            problem["solution"]=r"The 150° exterior angle and ∠ADC form a linear pair, so \(\angle ADC=180^\circ-150^\circ=30^\circ\). The given equality then gives \(\angle CAD=30^\circ\). In triangle ABD, \(\angle BAD=180^\circ-60^\circ-30^\circ=90^\circ\). AC splits this angle, so \(\angle BAC=\angle BAD-\angle CAD=90^\circ-30^\circ=60^\circ\). Check: triangle ACD has angles30°,30°,120°; since B,C,D are collinear, ∠ACB=60°, making triangle ABC's angle sum180°."
        elif str(problem["qNo"])=="Think Higher 5":
            problem["diagram"]={"type":"annotated-angle-figure","title":"Think Higher 5: rectangle PQRS on straight line LM","points":[[150,245],[286,245],[286,65],[150,65]],"extensions":[[150,245,286,65],[70,245,370,245]],"labels":[[150,267,"P"],[286,267,"Q"],[296,53,"R"],[143,53,"S"],[60,250,"L"],[382,250,"M"],[166,206,"37°"],[183,232,"x"],[133,229,"y"],[262,228,"u"],[307,229,"z"],[261,93,"v"],[276,120,"w"]]}
            problem["solution"]=r"Each rectangle corner is90°. At P the diagonal splits the corner into37° and x, so \(x=90^\circ-37^\circ=53^\circ\). PS is perpendicular to the straight line LM, giving \(y=90^\circ\). The parallel sides PS and QR and transversal PR give alternate interior angles \(w=37^\circ\). At R, \(v=90^\circ-w=53^\circ\). At Q, the rectangle gives \(u=90^\circ\). The adjacent angle z lies on straight line PQM, so \(z=180^\circ-u=90^\circ\). Checks: \(x+37^\circ=90^\circ\), \(v+w=90^\circ\), and \(u+z=180^\circ\)."
    vocabulary11=make_section("Vocabulary (p.216)",[
        "Polygon: a closed plane figure bounded by straight line segments. Regular polygon: all sides and all interior angles are equal. Irregular polygon: at least one of those conditions fails.",
        "Convex polygon: no inward corner or reflex interior angle. Concave polygon: at least one inward corner with a reflex interior angle. Interior angle: an angle inside a polygon at a vertex. Exterior angle: the angle formed by a side and an extension of its adjacent side.",
        "Pentagon:5 sides; hexagon:6; heptagon:7; octagon:8.",
        "Centre: the fixed point equally distant from the circle's boundary. Radius: the distance from centre to boundary. Diameter: a chord through the centre, twice the radius. Chord: a line segment joining two boundary points.",
        "Arc: part of the circumference. Minor arc: less than half the circumference; major arc: more than half. Semicircle: either half of a circle divided by a diameter. Segment: the region bounded by a chord and its corresponding arc."
    ])
    vocabulary11["id"]="unit11-vocabulary"
    chapters[10]["sections"]=[section for section in chapters[10]["sections"] if section["id"]!="unit11-vocabulary"]+[vocabulary11]

    # Review pp.217–218: the variable-angle questions require their source figures.
    review11=next(ex for ex in chapters[10]["exercises"] if "Review" in ex["title"])
    review_q5=next(p for p in review11["problems"] if str(p["qNo"])=="5")
    review_q5["diagram"]={"type":"diagram-group","items":[
        {"type":"annotated-angle-figure","title":"5(a): rhombus ABCD, AB = 10 cm (schematic)","points":[[115,230],[295,230],[260,53.435],[80,53.435]],"labels":[[105,254,"A"],[304,254,"B"],[269,39,"C"],[69,39,"D"],[205,257,"10 cm"],[135,211,"x"],[273,211,"y"],[245,82,"z"],[104,82,"w"]]},
        {"type":"labelled-polygon","title":"5(b): parallelogram PQRS (schematic)","points":[[85,235],[315,235],[360,65],[130,65]],"names":["P","Q","R","S"],"angles":["o","l","m","n"]},
        {"type":"labelled-polygon","title":"5(c): trapezium ABCD, AB ∥ DC (schematic)","points":[[75,245],[350,245],[280,70],[155,70]],"names":["A","B","C","D"],"angles":["x","y","z","w"]}
    ]}
    # Keep the source summary separate from the circle definition lesson.
    summary_paragraphs=[para for para in circle_lesson["paras"] if para.startswith("Chapter summary:")]
    if summary_paragraphs:
        remaining=[para for para in circle_lesson["paras"] if not para.startswith("Chapter summary:")]
        circle_lesson["paras"]=remaining
        circle_lesson["text"]=circle_lesson["theory"]="\n\n".join(remaining)
    summary11=make_section("Summary (p.216)",[
        "A circle consists of the points in a plane at the same distance from its centre. An angle subtended by a diameter at a point on the circle is a right angle.",
        "An isosceles trapezium has equal non-parallel sides. Convex polygons have all vertices pointing outward; concave polygons have at least one inward vertex with a reflex interior angle.",
        "Regular and irregular simple polygons with the same number of sides have the same interior-angle sum: (n−2) × 180°. Only equal-angle polygons permit this sum to be divided by n to obtain every individual angle.",
        "An exterior angle of a triangle equals 180° minus its adjacent interior angle; it also equals the sum of the two opposite interior angles. One exterior angle at each vertex of a convex polygon sums to360°."
    ])
    summary11["id"]="unit11-summary"
    chapters[10]["sections"]=[section for section in chapters[10]["sections"] if section["id"]!="unit11-summary"]
    vocabulary_index=next(i for i,section in enumerate(chapters[10]["sections"]) if section["id"]=="unit11-vocabulary")
    chapters[10]["sections"].insert(vocabulary_index,summary11)

    # Review p.218 Q6: trace the six source outlines without inventing equality marks.
    review_q6=next(problem for problem in review11["problems"] if str(problem["qNo"])=="6")
    review_q6["diagram"]={"type":"polygon-gallery","panels":[
        {"title":"(a)","points":[[49,83],[144,150],[64,214]]},
        {"title":"(b)","points":[[268,86],[461,86],[407,139],[461,190],[270,188],[227,139]]},
        {"title":"(c)","points":[[0,0],[1,0],[1,1],[0,1]]},
        {"title":"(d)","points":[[874,98],[933,126],[990,100],[1026,159],[961,237],[881,237],[844,158]]},
        {"title":"(e): faint outline reconstructed","points":[[1128,100],[1288,110],[1386,224],[1162,219]]},
        {"title":"(f)","points":[[1459,130],[1542,122],[1610,152],[1608,196],[1540,223],[1457,212],[1420,168]]}
    ]}
    review_q6["question"]="Tell whether each polygon is regular or not regular. Also explain whether it is convex or concave. Figures (a)–(f) follow the source order; figure (e)'s faint outline has been reconstructed."

    # Review p.219: complete ruler-and-compass directions and a usable project record.
    for problem in review11["problems"]:
        if str(problem["qNo"])=="18":
            problem["solution"]="1. Mark a point O and draw a circle with a compass at any convenient radius. 2. Mark two boundary points A and B above O, then join AB with a ruler. 3. Mark two other boundary points C and D below O, then join CD. 4. Check that both endpoints of each segment lie on the circumference and neither segment passes through O. AB and CD are chords. Neither is a diameter, because a diameter must pass through the centre. The displayed sample uses two parallel chords, but the question does not require the chords to be parallel."
        elif str(problem["qNo"])=="19":
            problem["solution"]=r"1. Mark centre O. Use a ruler to set the compass opening to7 cm and draw the circle without changing that opening. 2. Mark A and B on its upper boundary and draw chord AB away from O. Shade the small region between AB and the upper arc AB. 3. Mark C and D on the lower boundary and draw chord CD away from O. Shade the small region between CD and the lower arc CD. These are two circular segments: each is bounded by one chord and one arc. The chords themselves are line segments; the shaded areas are segments of the circle. Check that every radius is7 cm and the diameter is \(2\times7=14\) cm. The screen illustration shows the construction; use a ruler and compass to obtain the stated length on paper."
        elif str(problem["qNo"])=="Project":
            problem["diagram"]={"type":"frequency-table","title":"Record the two cut-outs you picked","headers":["First shape","Second shape","Similarities","Differences"],"rows":[["________","________","________","________"]]}
            problem["solution"] += " Suggested checks: count the sides; identify parallel pairs; compare side lengths; count right angles; and check reflection lines by folding the cut-out. A rotated shape keeps the same properties. Use the non-square versions when explaining differences between a square and a rectangle or rhombus. The completed table below is a sample; other randomly selected pairs have different valid comparisons."

    # Printed p.221: all four reflection examples must also appear with the lesson.
    reflection_example=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-reflection-examples")
    reflection_example["problem"]="Explain the symmetry lines shown for the semicircle, isosceles trapezium, right-pointing arrow and sideways kite."
    reflection_example["solution"]="(a) The semicircle has one vertical symmetry line through its centre and the midpoint of its diameter. Its left and right halves coincide. A horizontal line is not a symmetry line, because it would reflect the curved half below the diameter. (b) The isosceles trapezium has a vertical line through the midpoints of its parallel bases: its left and right halves match. (c) The arrow has a horizontal line through its centre: its top and bottom halves match. (d) The sideways kite has a horizontal line through the two vertices where equal-side pairs meet. In each case, reflecting every point across the marked line gives the same complete outline."
    reflection_example["diagram"]["panels"]=[panel for panel in reflection_example["diagram"]["panels"] if panel.get("shape")!="semicircle"]
    reflection_example["diagram"]["panels"].insert(0,{"title":"(a) Semicircle","shape":"semicircle","axes":[[150,45,150,195]]})
    next(section for section in chapters[11]["sections"] if section["id"]=="12.1.1")["diagram"] = reflection_example["diagram"]

    # Printed p.222: the complete marked figure determines rotation order.
    rotation_lesson=next(section for section in chapters[11]["sections"] if section["id"]=="12.2")
    rotation_lesson["diagram"]={"type":"diagram-group","items":[
        {"type":"rotation-sequence","shape":"flower","title":"Four-petal figure: matches at 90°, 180°, 270° and 360°; order 4"},
        {"type":"rotation-sequence","shape":"marked-hexagon","title":"Hexagon with two dots: matches at 180° and 360°; order 2"}
    ]}
    rotation_source={"id":"we-12-rotation-order-source","title":"Why the marked hexagon has order 2 (p.222)","problem":"The textbook hexagon has two dots on opposite sides. Explain why its rotational symmetry is order 2 rather than order 6.","solution":"A rotation must match the whole figure, including the two dots. At180° the two dots exchange positions and the hexagon matches its starting outline. At360° the complete figure returns to its original position. At60° or120°, even though a regular hexagon's outline would match, the dots would be in different positions. At90° and270° the dots are at the left and right rather than the top and bottom, and the outline also has a different orientation. Therefore there are two matches during a full turn, giving order2. Count360° once; the0° starting picture is not an extra rotation.","diagram":{"type":"rotation-sequence","shape":"marked-hexagon","title":"Compare both the outline and the dots"}}
    chapters[11]["workedExamples"]=[example for example in chapters[11]["workedExamples"] if example["id"]!=rotation_source["id"]]+[rotation_source]

    # Printed p.223: plot the source point examples with visible labels.
    source_rotation_panels=[]
    for title,points,labels,transform in [
        ("90° counterclockwise: A and B",[[2,4],[-3,1]],["A","B"],lambda x,y:(-y,x)),
        ("180°: J and K",[[2,4],[3,1]],["J","K"],lambda x,y:(-x,-y)),
        ("90° clockwise: corrected J and K images",[[2,4],[3,1]],["J","K"],lambda x,y:(y,-x))
    ]:
        panel=transformation_panel(title,points,transform)
        panel["shapes"][0].update({"kind":"points","labels":labels})
        panel["shapes"][1].update({"kind":"points","labels":[label+"′" for label in labels]})
        source_rotation_panels.append(panel)
    next(section for section in chapters[11]["sections"] if section["id"]=="12.2.1")["diagram"]={"type":"coordinate-panels","panels":source_rotation_panels}

    # Printed p.224: explicit substitutions and vertex correspondence on the plots.
    rectangle_rotation=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-rotation")
    rectangle_rotation["solution"]=r"For a 90° counterclockwise turn about the origin, use \((x,y)\mapsto(-y,x)\): negate the original y-coordinate to get the new x-coordinate, then use the original x-coordinate as the new y-coordinate. Thus \(A(2,6)\mapsto A'(-6,2)\), \(B(7,6)\mapsto B'(-6,7)\), \(C(7,2)\mapsto C'(-2,7)\), and \(D(2,2)\mapsto D'(-2,2)\). Plot and join A′,B′,C′,D′,A′ in that order. The original rectangle is5 units wide and4 units high; the rotated rectangle is4 units wide and5 units high. Its side lengths and right angles are preserved. All vertices move from quadrantI to quadrantII. This is a rotation; the source's references to a reflected image in these steps should read rotated image."
    rectangle_panel=rectangle_rotation["diagram"]["panels"][0]
    rectangle_panel["shapes"][0]["labels"]=["A","B","C","D"]
    rectangle_panel["shapes"][1]["labels"]=["A′","B′","C′","D′"]
    rectangle_rotation["diagram"]={"type":"diagram-group","items":[
        {"type":"frequency-table","title":"Apply (x,y) → (−y,x) to each vertex","headers":["Vertex","Original coordinates","New coordinates"],"rows":[["A → A′","(2,6)","(−6,2)"],["B → B′","(7,6)","(−6,7)"],["C → C′","(7,2)","(−2,7)"],["D → D′","(2,2)","(−2,2)"]]},
        {"type":"coordinate-panels","panels":[rectangle_panel]}
    ]}
    triangle_rotation=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-rotation-quick-triangle")
    triangle_rotation["diagram"]["panels"][0]["shapes"][0]["labels"]=["A","B","C"]
    triangle_rotation["diagram"]["panels"][0]["shapes"][1]["labels"]=["A′","B′","C′"]

    # Exercise12.1 p.225: original graphs appear before the solution is opened.
    rotation_exercise=next(ex for ex in chapters[11]["exercises"] if ex["title"]=="Exercise 12.1")
    rotation_q4=next(problem for problem in rotation_exercise["problems"] if str(problem["qNo"])=="4")
    rotation_q4["diagram"]={"type":"coordinate-panels","panels":[
        {"title":"4(a): rotate this triangle 180° counterclockwise","shapes":[{"name":"Given triangle","points":[[1,1],[1,5],[5,1]]}]},
        {"title":"4(b): rotate this pentagon 90° clockwise","shapes":[{"name":"Given pentagon","points":[[1,-1],[5,-1],[5,-4],[3,-5],[1,-4]]}]}
    ]}
    rotation_q5=next(problem for problem in rotation_exercise["problems"] if str(problem["qNo"])=="5")
    rotation_q5["solution"]=r"Choose a sample triangle P(1,1), Q(4,1), R(2,3), plot its vertices and join them. A 270° clockwise turn has the same final position as a 90° counterclockwise turn. Use \((x,y)\mapsto(-y,x)\). Thus \(P(1,1)\mapsto P'(-1,1)\), \(Q(4,1)\mapsto Q'(-1,4)\), and \(R(2,3)\mapsto R'(-3,2)\). Plot and join P′Q′R′P′. The original side PQ and image side P′Q′ are both3 units long. Every point keeps its distance from the origin, and the triangle keeps its size and shape. Since the question says to draw a triangle of your own, other starting coordinates are valid if all vertices follow the same rotation rule."
    rotation_q5["solutionDiagram"]["panels"][0]["shapes"][0]["labels"]=["P","Q","R"]
    rotation_q5["solutionDiagram"]["panels"][0]["shapes"][1]["labels"]=["P′","Q′","R′"]

    # Printed p.226: show the rotation rule and substitution for every answer.
    for problem in rotation_exercise["problems"]:
        q=str(problem["qNo"])
        if q=="6":
            problem["solution"]=r"Choose A(1,1), B(5,1), C(4,3), D(2,3). AB and CD are horizontal and parallel; the other pair of opposite sides is not parallel, so ABCD is a trapezium. Plot and join ABCDA. For90° clockwise about the origin, use \((x,y)\mapsto(y,-x)\). The vertices become A′(1,−1), B′(1,−5), C′(3,−4), D′(3,−2). Plot and join A′B′C′D′A′. The parallel bases now lie vertically on x=1 and x=3, with lengths4 and2 units preserved. Other starting trapeziums are valid if all vertices follow the same rule."
            problem["solutionDiagram"]["panels"][0]["shapes"][0]["labels"]=["A","B","C","D"]
            problem["solutionDiagram"]["panels"][0]["shapes"][1]["labels"]=["A′","B′","C′","D′"]
        elif q in ("7","8"):
            if q=="7":
                original=[-6,-4]
                cases=[("(a) 90° clockwise",lambda x,y:(y,-x)),("(b) 180° counterclockwise",lambda x,y:(-x,-y)),("(c) 270° clockwise",lambda x,y:(-y,x))]
                problem["solution"]=r"Start with \(P(-6,-4)\). (a)90° clockwise uses \((x,y)\mapsto(y,-x)\), giving \(P'(-4,-(-6))=P'(-4,6)\): x=−4,y=6. (b)180° counterclockwise uses \((x,y)\mapsto(-x,-y)\), giving \(P'(6,4)\): x=6,y=4. (c)270° clockwise equals90° counterclockwise; use \((x,y)\mapsto(-y,x)\), giving \(P'(4,-6)\): x=4,y=−6. Each part starts from the original P, not from the previous answer."
            else:
                original=[3,9]
                cases=[("(a) 90° counterclockwise",lambda x,y:(-y,x)),("(b) 180° clockwise",lambda x,y:(-x,-y)),("(c) 270° counterclockwise",lambda x,y:(y,-x))]
                problem["solution"]=r"Start with \(P(3,9)\). (a)90° counterclockwise uses \((x,y)\mapsto(-y,x)\), so \(P'=(-9,3)\): x=−9,y=3. (b)180° clockwise changes both signs: \(P'=(-3,-9)\), so x=−3,y=−9. (c)270° counterclockwise equals90° clockwise; use \((x,y)\mapsto(y,-x)\), so \(P'=(9,-3)\): x=9,y=−3. Each turn is about the origin and starts from the original point."
            panels=[]
            for title,rule in cases:
                panel=transformation_panel(title,[original],rule)
                panel["shapes"][0].update({"kind":"points","labels":["P"]})
                panel["shapes"][1].update({"kind":"points","labels":["P′"]})
                panels.append(panel)
            problem["solutionDiagram"]={"type":"coordinate-panels","panels":panels}

    # Printed p.226: a complete worked Quick Check with the exact source vertices.
    translation_panel226=transformation_panel("Five units left and two units up",[[2,1],[4,1],[5,3],[2,3]],lambda x,y:(x-5,y+2))
    translation_panel226["shapes"][0]["labels"]=["P","Q","R","S"]
    translation_panel226["shapes"][1]["labels"]=["P′","Q′","R′","S′"]
    translation_quick226={
        "id":"we-12-translation-quick-226",
        "title":"Quick Check: two units up and five units left (p.226)",
        "problem":"Fill in the ordered pairs of the translated image: P(2,1), Q(4,1), R(5,3), S(2,3), moved2 units up and5 units left. Find P′,Q′,R′,S′.",
        "solution":r"Left5 means subtract5 from x; up2 means add2 to y. Apply \((x,y)\mapsto(x-5,y+2)\) to every vertex. \(P'=(2-5,1+2)=(-3,3)\); \(Q'=(4-5,1+2)=(-1,3)\); \(R'=(5-5,3+2)=(0,5)\); \(S'=(2-5,3+2)=(-3,5)\). Plot these points and join P′Q′R′S′P′. For each corresponding pair, image x minus original x is−5 and image y minus original y is2. This confirms that all four points moved together. The shape keeps its size and orientation.",
        "diagram":{"type":"diagram-group","items":[
            {"type":"frequency-table","title":"Completed ordered pairs","headers":["Vertex","x − 5","y + 2","Image"],"rows":[["P","2 − 5 = −3","1 + 2 = 3","P′(−3,3)"],["Q","4 − 5 = −1","1 + 2 = 3","Q′(−1,3)"],["R","5 − 5 = 0","3 + 2 = 5","R′(0,5)"],["S","2 − 5 = −3","3 + 2 = 5","S′(−3,5)"]]},
            {"type":"coordinate-panels","panels":[translation_panel226]}
        ]}
    }
    chapters[11]["workedExamples"]=[example for example in chapters[11]["workedExamples"] if example["id"]!=translation_quick226["id"]]+[translation_quick226]
    next(section for section in chapters[11]["sections"] if section["id"]=="12.3")["diagram"]={"type":"coordinate-panels","panels":[translation_panel226]}

    # Printed p.227: complete Example1 and label both original/image vertices.
    translation_example227=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-translation")
    translation_example227["title"]="Example 1: two units right and three units up (p.227)"
    translation_example227["solution"]=r"Write the rule \((x,y)\mapsto(x+2,y+3)\). Add2 to every x-coordinate and3 to every y-coordinate: \(A(-4,1)\mapsto A'(-4+2,1+3)=A'(-2,4)\); \(B(-6,4)\mapsto B'(-6+2,4+3)=B'(-4,7)\); \(C(-2,4)\mapsto C'(-2+2,4+3)=C'(0,7)\). Plot A′,B′,C′ and join A′B′C′A′. C′ lies on the y-axis because its x-coordinate is0. For each vertex the change is(+2,+3); the original horizontal side BC and image side B′C′ are both4 units long. The upper source graph accidentally labels C(−2,4) as B; use C as in the listed coordinates and worked solution."
    translation_panel227=transformation_panel("Example 1: translate right2 and up3",[[-4,1],[-6,4],[-2,4]],lambda x,y:(x+2,y+3))
    translation_panel227["shapes"][0]["labels"]=["A","B","C"]
    translation_panel227["shapes"][1]["labels"]=["A′","B′","C′"]
    translation_example227["diagram"]={"type":"diagram-group","items":[
        {"type":"frequency-table","title":"Translation coordinates","headers":["Vertex","Original","Image"],"rows":[["A → A′","(−4,1)","(−2,4)"],["B → B′","(−6,4)","(−4,7)"],["C → C′","(−2,4)","(0,7)"]]},
        {"type":"coordinate-panels","panels":[translation_panel227]}
    ]}
    rectangle_quick227=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-translation-quick")
    rectangle_quick227["diagram"]["panels"][0]["shapes"][0]["labels"]=["Q","R","S","T"]
    rectangle_quick227["diagram"]["panels"][0]["shapes"][1]["labels"]=["Q′","R′","S′","T′"]

    # Printed pp.228–229: original-only exercise graphs and source vertex labels.
    describe_translation=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-describe-translation")
    describe_translation["diagram"]["panels"][0]["shapes"][0]["labels"]=["A","B","C","D"]
    describe_translation["diagram"]["panels"][0]["shapes"][1]["labels"]=["A′","B′","C′","D′"]
    translation_exercise=next(ex for ex in chapters[11]["exercises"] if ex["title"]=="Exercise 12.3")
    translation_question1=next(problem for problem in translation_exercise["problems"] if str(problem["qNo"])=="1")
    translation_question1["diagram"]={"type":"coordinate-panels","panels":[{"title":panel["title"],"shapes":[{"name":"Given figure","points":panel["shapes"][0]["points"]}]} for panel in translation_question1["solutionDiagram"]["panels"]]}
    translation_question1["diagram"]["panels"][0]["shapes"][0]["labels"]=["A","B","C"]
    translation_question1["solutionDiagram"]["panels"][0]["shapes"][0]["labels"]=["A","B","C"]
    translation_question1["solutionDiagram"]["panels"][0]["shapes"][1]["labels"]=["A′","B′","C′"]
    translation_question1["solution"] += "\nChecks: in(a), A moves from(−8,3) to(−10,−1), a change of(−2,−4); in(b), the first corner moves from(−9,9) to(−6,10), a change of(3,1); in(c), the upper vertex moves from(6,−2) to(10,1), a change of(4,3); in(d), the lower-left vertex moves from(2,2) to(4,0), a change of(2,−2). Apply each part's same displacement to every remaining corner, including all inward corners, and join points in their original boundary order."

    # Printed pp.229–230: replace diagram-label OCR with a complete triangle introduction.
    triangle_intro=make_section("12.4 Constructions of Triangles",[
        "A triangle is a closed plane figure formed by three line segments. In triangle ABC, the three vertices (corners) are A, B and C; its three sides are AB, BC and CA.",
        "Each side joins two vertices. The three sides enclose the triangle, and the three interior angles are at A, B and C. The source figure labels all three corners as vertices and all three boundary segments as sides.",
        "For the following constructions, use a ruler to draw the stated base length and a protractor to draw the stated angles at its endpoints. Extend the two rays until they meet; that intersection is the third vertex. Draw both rays on the same side of the base."
    ])
    triangle_intro["id"]="12.4"
    triangle_intro["diagram"]={"type":"annotated-angle-figure","title":"Triangle ABC: three sides and three vertices","points":[[210,55],[90,240],[330,240]],"labels":[[210,39,"A"],[73,254,"B"],[345,254,"C"],[123,139,"Side AB"],[300,139,"Side AC"],[210,268,"Side BC"]]}
    chapters[11]["sections"]=[triangle_intro if section["id"]=="12.4" else section for section in chapters[11]["sections"]]
    for section_id,example_id in [("12.4.1","we-12-equilateral"),("12.4.2","we-12-isosceles"),("12.4.3","we-12-scalene")]:
        section=next(section for section in chapters[11]["sections"] if section["id"]==section_id)
        example=next(example for example in chapters[11]["workedExamples"] if example["id"]==example_id)
        if example.get("diagram"):
            section["diagram"]=example["diagram"]

    # Printed p.231: show the compass arc placing N at the required distance from L.
    acute_example=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-acute")
    acute_example["diagram"]["compassArcs"]=[{"centre":0,"through":2}]
    acute_example["diagram"]["title"]="LM = 3.5 cm, LN = 3 cm, angle L = 40°; dashed arc locates N"
    next(section for section in chapters[11]["sections"] if section["id"]=="12.4.4")["diagram"]=acute_example["diagram"]
    two_right=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-quick-two-right")
    two_right["solution"]="No. A triangle's interior angles total180°. Two right angles already total90°+90°=180°, leaving0° for the third angle, which cannot form a triangle. Geometrically, drawing perpendicular rays at both ends of the same base on the same side gives parallel rays. They never meet to create a third vertex."

    # Printed p.232: compass construction marks and fuller first exercise answers.
    for example_id,section_id in [("we-12-obtuse","12.4.5"),("we-12-right","12.4.6")]:
        example=next(example for example in chapters[11]["workedExamples"] if example["id"]==example_id)
        example["diagram"]["compassArcs"]=[{"centre":0,"through":2}]
        next(section for section in chapters[11]["sections"] if section["id"]==section_id)["diagram"]=example["diagram"]
    construction_exercise=next(ex for ex in chapters[11]["exercises"] if ex["title"]=="Exercise 12.4")
    for problem in construction_exercise["problems"]:
        q=str(problem["qNo"])
        if q in ("1","2"):
            problem["solutionDiagram"]["compassArcs"]=[{"centre":0,"through":2},{"centre":1,"through":2}]
        if q=="1":
            problem["solution"]="1. Draw AB=3.8 cm with a ruler. 2. Set the compass opening to3.8 cm. With centre A, draw an arc above AB. 3. Keeping the same opening, draw another arc with centre B to cross the first; name the intersection C. 4. Join AC and BC. By construction, AC and BC both equal the compass radius3.8 cm, and AB=3.8 cm, so all three sides are equal. Triangle ABC is equilateral and each angle is60°. The intersection below AB gives a reflected but equally valid construction."
        elif q=="2":
            problem["solution"]="1. Draw PQ=8 cm. 2. Set the compass opening to4.5 cm and draw an arc above PQ with centre P. 3. Without changing the opening, draw a second arc with centre Q. Name their upper intersection R. 4. Join PR and QR. Both segments are4.5 cm because they are radii of the construction arcs, giving PR=QR and an isosceles triangle. The arcs can meet because4.5+4.5=9 cm is greater than the8 cm base. Measure the three sides to check the construction."
        elif q=="3":
            problem["solution"]=r"These measurements cannot form a triangle. The two shorter sides total \(AB+AC=3+2.5=5.5\) cm, which is less than \(BC=6\) cm. A triangle requires the sum of any two sides to be greater than the third. To see the failure geometrically, draw BC=6 cm, then draw an arc of radius3 cm from B and an arc of radius2.5 cm from C. The arcs cannot intersect: even their closest reach leaves a0.5 cm gap along BC. Therefore there is no possible third vertex A for the printed measurements; do not draw a triangle with altered lengths."

    # Exercise12.4 p.232: full construction sequences for all remaining questions.
    construction_solutions={
        "4":r"1. Draw ST=4.5 cm with a ruler. 2. Centre the protractor at S, align its baseline along ST, mark60°, and draw a ray through the mark. 3. At T, align the protractor along TS and draw a60° ray on the same side of ST. 4. Name the intersection R and join RS and RT. The third angle is \(180^\circ-60^\circ-60^\circ=60^\circ\). Equal angles have equal opposite sides, so RS=RT=ST=4.5 cm and the triangle is equilateral.",
        "5":r"1. Draw DE=5 cm. 2. At D, measure55° from DE and draw a ray. 3. At E, measure35° from ED and draw a ray on the same side of DE. 4. Name their intersection F and join DF and EF. Check the third angle: \(\angle DFE=180^\circ-55^\circ-35^\circ=90^\circ\). All three angles differ, so their opposite sides differ and the triangle is scalene. It is also right-angled at F; scalene describes its sides and right-angled describes its angles.",
        "6":r"1. Draw AB=7 cm. 2. At B, align the protractor with BA and draw a90° ray. 3. Set the compass to3.2 cm; with centre B mark C on that ray, giving BC=3.2 cm. 4. Join AC. Check AB=7 cm, BC=3.2 cm and ∠ABC=90°. Optional numerical check of the hypotenuse: \(AC=\sqrt{7^2+3.2^2}=\sqrt{59.24}\approx7.70\) cm; this is a check, not another construction measurement.",
        "7":"1. Draw PR=4.7 cm. 2. Centre the protractor at R and align its baseline with RP, pointing towards P. Measure65° and draw the ray for RQ. 3. Set the compass opening to5.2 cm and, with centre R, mark Q on the ray. 4. Join PQ. Check PR=4.7 cm, RQ=5.2 cm and the included angle PRQ=65°. Measure the other two angles with a protractor to confirm both are less than90°. They are approximately62.0° at P and53.0° at Q, so the triangle is acute-angled.",
        "8":"1. Draw EF=8 cm. 2. At F, align the protractor baseline with FE, pointing towards E. Measure135° and draw a ray. 3. Set the compass to5 cm and, with centre F, mark D on that ray. 4. Join DE. Check EF=8 cm, FD=5 cm and ∠EFD=135°. The angle at F is greater than90°, so DEF is obtuse-angled. Choose the correct protractor scale: the required angle is135°, not its45° supplement."
    }
    for problem in construction_exercise["problems"]:
        q=str(problem["qNo"])
        if q in construction_solutions:
            problem["solution"]=construction_solutions[q]
        if q=="6": problem["solutionDiagram"]["compassArcs"]=[{"centre":1,"through":2}]
        if q=="7": problem["solutionDiagram"]["compassArcs"]=[{"centre":2,"through":1}]
        if q=="8": problem["solutionDiagram"]["compassArcs"]=[{"centre":2,"through":0}]

    # Printed p.233: restore the triangle and intersecting-line example figures.
    triangle_angle_example=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-triangle-angle")
    triangle_angle_example["title"]="Example 1: missing angle of triangle ABC (p.233)"
    triangle_angle_example["solution"]=r"The interior angles of triangle ABC total180°. Therefore \(\angle ABC+\angle ACB+\angle BAC=180^\circ\). Substitute the given angles: \(26^\circ+84^\circ+\angle BAC=180^\circ\). Add the known angles to get110°, then subtract: \(\angle BAC=180^\circ-110^\circ=70^\circ\). Check: \(26^\circ+84^\circ+70^\circ=180^\circ\)."
    triangle_angle_example["diagram"]={"type":"labelled-polygon","title":"Triangle ABC: find angle A (schematic)","points":[[70,240],[355,240],[170,60]],"names":["A","B","C"],"angles":["?","26°","84°"]}
    crossing_example=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-exterior-angle")
    crossing_example["title"]="Example 2: vertically opposite angles at T (pp.233–234)"
    crossing_example["solution"]=r"In triangle TUV, \(\angle VTU+90^\circ+45^\circ=180^\circ\), so \(\angle VTU=45^\circ\). The straight lines SU and VR intersect at T. Their vertically opposite angles ∠RTS and ∠VTU are equal, giving \(\angle RTS=45^\circ\). The left-hand triangle independently checks this answer: \(180^\circ-75^\circ-60^\circ=45^\circ\). Do not treat the two angles at T as adjacent angles; they are opposite across the intersection."
    crossing_example["diagram"]={"type":"annotated-angle-figure","title":"SU and VR are straight lines through T (schematic)","points":[[140,60],[110,230],[230,150],[290,110],[320,240],[230,150]],"labels":[[134,43,"R"],[96,250,"S"],[229,174,"T"],[295,94,"U"],[329,259,"V"],[149,91,"75°"],[126,210,"60°"],[283,133,"90°"],[305,214,"45°"]]}

    # Printed p.234: complete the two worked figures preceding Exercise12.5.
    right_sum_example=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-right-angle-sum")
    right_sum_example["title"]="Example 3: acute angles in a right triangle (p.234)"
    right_sum_example["solution"]=r"Triangle MNO has a right angle at N. Its other two angles therefore sum to \(180^\circ-90^\circ=90^\circ\). Since \(\angle OMN=15^\circ\), \(\angle NOM=90^\circ-15^\circ=75^\circ\). Check: \(15^\circ+90^\circ+75^\circ=180^\circ\). The two acute angles in every right triangle are complementary."
    right_sum_example["diagram"]={"type":"labelled-polygon","title":"Right triangle MNO: find ∠NOM","points":[[65,110],[345,110],[345,185.026]],"names":["M","N","O"],"angles":["15°","90°","?"]}
    linear_pair_example=next(example for example in chapters[11]["workedExamples"] if example["id"]=="we-12-linear-pair-example")
    linear_pair_example["diagram"]={"type":"annotated-angle-figure","title":"B, C and D lie on a straight line (schematic)","points":[[195,50],[85,245],[320,245]],"extensions":[[320,245,400,245]],"labels":[[195,33,"A"],[72,264,"B"],[320,265,"C"],[404,265,"D"],[195,86,"60°"],[347,221,"140°"]]}
    linear_pair_example["solution"]=r"Because B,C,D are collinear, ∠ACB and ∠ACD form a linear pair. Thus \(\angle ACB=180^\circ-140^\circ=40^\circ\). The interior angles of triangle ABC total180°, so \(\angle ABC=180^\circ-60^\circ-40^\circ=80^\circ\). Check using the exterior-angle theorem: \(140^\circ=60^\circ+80^\circ\)."

    # Printed p.234: all six unknown-angle diagrams, retaining inconsistent source data in(e).
    angle_exercise=next(ex for ex in chapters[11]["exercises"] if ex["title"]=="Exercise 12.5")
    angle_q1=next(problem for problem in angle_exercise["problems"] if str(problem["qNo"])=="1")
    angle_q1["diagram"]={"type":"diagram-group","items":[
        {"type":"annotated-angle-figure","title":"1(a): find x (schematic)","points":[[60,235],[285,235],[365,85]],"labels":[[110,226,"20°"],[267,219,"130°"],[340,120,"x"]]},
        {"type":"annotated-angle-figure","title":"1(b): find a (schematic)","points":[[115,250],[175,55],[340,235]],"labels":[[149,221,"60°"],[302,216,"40°"],[182,99,"a"]]},
        {"type":"annotated-angle-figure","title":"1(c): find x and y; ABD is straight (schematic)","points":[[105,245],[285,245],[195,60]],"extensions":[[285,245,385,245]],"labels":[[92,267,"A"],[284,267,"B"],[195,43,"C"],[391,267,"D"],[142,227,"60°"],[259,228,"x"],[195,102,"y"],[313,223,"120°"]]},
        {"type":"annotated-angle-figure","title":"1(d): ACD, BCEF and DEG are straight (schematic)","points":[[100,80],[60,180],[180,120],[300,60],[300,180],[380,220],[300,270],[300,180],[180,120]],"labels":[[95,64,"B"],[48,197,"A"],[173,102,"C"],[301,44,"D"],[315,174,"E"],[395,224,"F"],[298,290,"G"],[107,108,"75°"],[150,123,"65°"],[208,124,"x"],[285,93,"y"],[282,161,"z"],[317,209,"50°"],[319,247,"40°"],[353,225,"w"]]},
        {"type":"annotated-angle-figure","title":"1(e): printed angles; see inconsistency explained in solution","points":[[125,55],[75,265],[230,160],[305,109],[370,255],[230,160]],"labels":[[120,39,"R"],[65,285,"S"],[230,185,"T"],[306,93,"U"],[384,271,"V"],[135,91,"80°"],[106,239,"55°"],[207,164,"a"],[253,166,"b"],[306,142,"90°"],[341,230,"30°"]]},
        {"type":"annotated-angle-figure","title":"1(f): straight-line and opposite-angle relations (schematic)","points":[[110,240],[140,70],[300,205]],"extensions":[[55,250.13,355,194.87],[280,105,320,305],[300,205,350,247.19]],"labels":[[83,226,"105°"],[130,225,"a"],[156,111,"d"],[275,205,"b"],[285,172,"c"],[328,180,"102°"],[342,281,"30°"]]}
    ]}

    # Printed p.235: restore the two remaining source question diagrams.
    for problem in angle_exercise["problems"]:
        if str(problem["qNo"])=="2":
            problem["diagram"]={"type":"annotated-angle-figure","title":"Question 2: find ∠ABC (schematic)","points":[[175,65],[80,240],[355,240]],"labels":[[175,47,"A"],[66,259,"B"],[369,259,"C"],[175,100,"90°"],[321,226,"68°"],[111,227,"?"]]}
            problem["solution"]=r"The square mark at A denotes a right angle, so \(\angle BAC=90^\circ\). The triangle's interior angles sum to180°: \(\angle ABC+90^\circ+68^\circ=180^\circ\). Therefore \(\angle ABC=180^\circ-158^\circ=22^\circ\). Check: \(90^\circ+68^\circ+22^\circ=180^\circ\)."
        elif str(problem["qNo"])=="3":
            problem["question"]="Find angles a and b in the pictured triangle. Its two sloping sides have matching equality marks, and the angle at G is52°."
            problem["diagram"]={"type":"annotated-angle-figure","title":"Question 3: equal sloping sides; find a and b","points":[[220,65],[130,249.53],[310,249.53]],"extensions":[[168,154,182,161],[258,161,272,154]],"labels":[[220,47,"G"],[120,271,"H"],[220,107,"52°"],[156,230,"a"],[284,230,"b"]]}
            problem["solution"]=r"The matching side marks show that the triangle is isosceles. Angles opposite its equal sides are equal, so \(a=b\). The base angles together measure \(180^\circ-52^\circ=128^\circ\). Divide equally: \(a=b=128^\circ/2=64^\circ\). Check: \(64^\circ+64^\circ+52^\circ=180^\circ\)."

    # Printed p.235: trace the full star, including the source's conflicting marks.
    star_question=next(problem for problem in angle_exercise["problems"] if str(problem["qNo"]).replace(" ","")=="ThinkHigher2")
    star_points={"A":[405,935],"B":[492,695],"C":[778,722],"D":[643,470],"E":[785,265],"F":[556,307],"G":[435,65],"H":[390,250],"I":[177,165],"J":[257,386],"K":[45,440],"L":[218,575],"M":[65,650],"N":[285,695],"O":[434,519]}
    star_edges=set()
    for triangle in ["DBC","EFD","GHF","IHJ","KJL","MLN","ANB"]:
        for index in range(3): star_edges.add(tuple(sorted([triangle[index],triangle[(index+1)%3]])))
    for vertex in "HFDBNLJ": star_edges.add(tuple(sorted(["O",vertex])))
    star_question["diagram"]={"type":"angle-network","title":"Think Higher 2: textbook star and printed markings (schematic)","points":star_points,"edges":sorted(star_edges),
        "ticks":[["D","B"],["D","C"],["B","C"],["E","F"],["E","D"],["I","H"],["I","J"],["H","J"],["K","J"],["K","L"],["L","O"],["N","O"]],
        "rightMarks":[[[398,219],[423,227],[415,259]],[[613,432],[590,443],[603,480]],[[196,583],[204,606],[235,597]]],
        "labels":[[405,970,"A"],[506,730,"B"],[797,749,"C"],[665,481,"D"],[804,275,"E"],[579,298,"F"],[435,48,"G"],[373,226,"H"],[166,151,"I"],[235,377,"J"],[25,444,"K"],[203,565,"L"],[45,663,"M"],[277,723,"N"],[446,547,"O"],
        [521,678,"a"],[747,704,"b"],[578,345,"c"],[650,426,"d"],[518,290,"e"],[339,270,"f"],[274,344,"g"],[85,455,"h"],[249,678,"i"],[405,887,"j"],
        [206,212,"60°"],[445,132,"45°"],[738,309,"30°"],[648,530,"60°"],[311,739,"70°"],[458,739,"70°"],[112,649,"30°"],[219,519,"60°"],[220,437,"60°"],[484,493,"40°"]]}

    # Complete the unlettered central angle marking from the star on p.235.
    star_question["diagram"]["angleMarks"]=[["L","O","N"],["F","O","D"]]
    summary12=next(section for section in chapters[11]["sections"] if section["id"]=="summary-and-vocabulary")
    summary12["diagram"]={"type":"frequency-table","title":"Vocabulary: classifying triangles (p.236)","headers":["Triangle name","Meaning","Angle or side check"],"rows":[
        ["Isosceles","At least two equal sides","Angles opposite those sides are equal"],
        ["Equilateral","Three equal sides","All three angles are60°"],
        ["Scalene","Three unequal sides","All three angles are unequal"],
        ["Right-angled","One angle is90°","The other two total90°"],
        ["Acute-angled","All three angles are less than90°","Their sum is180°"],
        ["Obtuse-angled","One angle is greater than90°","The other two total less than90°"]
    ]}

    # Review p.237 Q4: the asymmetric top bump rules out the old rectangle answer.
    review12=next(ex for ex in chapters[11]["exercises"] if "Review" in ex["title"])
    review_symmetry4=next(problem for problem in review12["problems"] if str(problem["qNo"])=="4")
    review_symmetry4["solution"]="(a) The intended equal-arm cross has four symmetry lines: horizontal, vertical and the two diagonal lines through its centre. (b) No line of symmetry. The small bump on the upper edge has no matching bump on the lower edge, so horizontal reflection fails. It is off-centre and has no matching upper-left bump, so vertical reflection fails too. The unequal width and height also rule out diagonal symmetry. (c) One horizontal line through the middle of the long upright part: the upper and lower arrow-like ends reflect onto one another. There is no vertical line because the long straight right edge does not match the indented left edge."
    review_symmetry4["solutionDiagram"]={"type":"symmetry-panels","panels":[
        {"title":"(a) Equal-arm cross","points":[[120,40],[150,70],[180,40],[230,90],[200,120],[230,150],[180,200],[150,170],[120,200],[70,150],[100,120],[70,90]],"axes":[[150,20,150,220],[40,120,260,120],[50,20,250,220],[50,220,250,20]]},
        {"title":"(b) Notched rectangle with off-centre bump","path":"M45 65 H205 A7 7 0 0 1 219 65 H255 V113 A7 7 0 0 0 255 127 V175 H45 V127 A7 7 0 0 0 45 113 Z","axes":[]},
        {"title":"(c) Bent arrow-like outline","points":[[190,25],[115,75],[155,75],[155,165],[115,165],[190,215]],"axes":[[90,120,215,120]]}
    ]}

    # Review p.237 Q2: proposed axes must not be presented as confirmed symmetry lines.
    review_symmetry2=next(problem for problem in review12["problems"] if str(problem["qNo"])=="2")
    review_symmetry2["diagram"]={"type":"symmetry-panels","panels":[
        {"title":"(a)","proposed":True,"path":"M100 180 V85 A50 50 0 0 1 200 85 V180 H160 V210 A10 10 0 0 1 140 210 V180 Z","axes":[[150,20,150,235]]},
        {"title":"(b)","proposed":True,"points":[[120,210],[120,100],[95,70],[135,70],[150,25],[165,70],[205,70],[180,100],[180,210]],"axes":[[150,10,150,230]]},
        {"title":"(c)","proposed":True,"path":"M230 120 A80 80 0 1 1 70 120 A80 80 0 1 1 230 120 Z","axes":[[150,20,150,220]]},
        {"title":"(d)","proposed":True,"points":[[45,60],[90,60],[90,75],[70,75],[70,100],[230,100],[230,85],[245,85],[245,175],[200,175],[200,160],[220,160],[220,150],[45,150]],"axes":[[25,125,265,125]]},
        {"title":"(e)","proposed":True,"points":[[50,75],[225,75],[270,165],[95,165]],"axes":[[30,120,285,120]]}
    ]}

    # Review p.238: original figures and complete sample drawing solutions.
    for problem in review12["problems"]:
        q=str(problem["qNo"])
        if q in ("6","10"):
            source_panel=problem["solutionDiagram"]["panels"][0]
            problem["diagram"]={"type":"coordinate-panels","panels":[{"title":"Given figure: "+("rotate180° counterclockwise" if q=="6" else "translate5 right and8 up"),"shapes":[{"name":"Given figure","points":source_panel["shapes"][0]["points"]}]}]}
        elif q=="8":
            points=[[1,1],[4,1],[5,3],[3,5],[1,4]]
            panel=transformation_panel("Sample pentagon:90° counterclockwise",points,lambda x,y:(-y,x))
            panel["shapes"][0]["labels"]=["A","B","C","D","E"]
            panel["shapes"][1]["labels"]=["A′","B′","C′","D′","E′"]
            problem["solutionDiagram"]={"type":"coordinate-panels","panels":[panel]}
            problem["solution"]=r"Choose and plot A(1,1), B(4,1), C(5,3), D(3,5), E(1,4); join ABCDEA to make a pentagon. A90° counterclockwise turn uses \((x,y)\mapsto(-y,x)\). Thus A′(−1,1), B′(−1,4), C′(−3,5), D′(−5,3), E′(−4,1). Plot and join A′B′C′D′E′A′. For example, A(1,1) becomes(−1,1) because the original y is negated and the original x becomes the new y. Check that the3-unit side AB becomes the3-unit side A′B′. Other pentagons are valid when each vertex follows the same rule."
        elif q=="9":
            panel=transformation_panel("Sample rectangle:180° counterclockwise",[[1,1],[5,1],[5,3],[1,3]],lambda x,y:(-x,-y))
            panel["shapes"][0]["labels"]=["A","B","C","D"]
            panel["shapes"][1]["labels"]=["A′","B′","C′","D′"]
            problem["solutionDiagram"]={"type":"coordinate-panels","panels":[panel]}
            problem["solution"]=r"Draw the sample rectangle A(1,1), B(5,1), C(5,3), D(1,3), joining the vertices in order. A180° turn uses \((x,y)\mapsto(-x,-y)\): A′(−1,−1), B′(−5,−1), C′(−5,−3), D′(−1,−3). Join the image vertices in the same order. Both rectangles are4 units by2 units, and each corresponding pair has midpoint O(0,0), as required by a half-turn about the origin. Other starting rectangles are valid."

    # Review p.239: concrete construction instructions and source comparison graphs.
    for problem in review12["problems"]:
        q=str(problem["qNo"])
        if q=="11":
            problem["diagram"]=problem["solutionDiagram"]
            problem["question"] += " In the web diagrams, the solid blue shape is the original and the dashed red shape is its image."
        elif q=="12":
            problem["solution"]="1. Draw PQ=7 cm. 2. Set a compass to7 cm and draw an arc with centre P. 3. Keeping the same opening, draw an arc with centre Q; label an intersection R. 4. Join PR and QR. The two new sides are both7 cm by construction, so PQ=QR=RP=7 cm. All angles are60°. Although the question lists only PQ and QR, the word equilateral requires the third side to have the same length."
        elif q=="13":
            problem["solution"]="1. Draw base AB=4 cm. 2. Set a compass to6 cm and draw an arc above AB with centre A. 3. With the same opening and centre B, draw an intersecting arc; call the intersection C. 4. Join AC and BC. Check AC=BC=6 cm and AB=4 cm. The equal sloping sides make ABC isosceles; its base angles at A and B are equal."
        elif q=="14":
            problem["solution"]="1. Draw LM=6.3 cm. 2. At M, align the protractor along ML and draw a90° ray. 3. Set a compass to4.5 cm and, with centre M, mark N on that ray. 4. Join LN. Check LM=6.3 cm, MN=4.5 cm and the included angle LMN=90°. The right angle is at M, the middle letter of the angle name."
        elif q=="15":
            problem["solution"]="1. Draw DE=7 cm. 2. At D draw a ray making20° with DE. 3. At E draw a ray making40° with ED on the same side of the base. 4. Name their intersection F and join DF and EF. Check the third angle:180°−20°−40°=120°. Since all angles differ, all sides differ and the triangle is scalene. Its120° angle at F also makes it obtuse-angled."
        elif q=="16":
            problem["solution"]="1. Draw PR=6 cm. 2. Centre the protractor at R and align its baseline with RP. Draw the second ray at70°. 3. With centre R and compass radius5 cm, mark Q on the ray. 4. Join PQ. Check PR=6 cm, QR=5 cm and angle PRQ=70°. Measure the other angles to confirm they are acute as well. Draw on either side of PR consistently; the reflected construction is equally valid."
        elif q=="17":
            problem["solution"]="1. Draw EF=5 cm. 2. At F align the protractor along FE and draw a140° ray. 3. With centre F and compass radius3 cm, mark D on this ray. 4. Join DE. Check EF=5 cm, FD=3 cm and the included angle EFD=140°. This angle is obtuse. Use the scale that measures140° from FE, not the supplementary40° scale."
        if q in ("12","13","14","16","17"):
            diagram=problem["solutionDiagram"]
            names=diagram["names"]
            pairs={"12":[("P","R"),("Q","R")],"13":[("A","C"),("B","C")],"14":[("M","N")],"16":[("R","Q")],"17":[("F","D")]}[q]
            diagram["compassArcs"]=[{"centre":names.index(a),"through":names.index(b)} for a,b in pairs]

    # Review p.239 Q18: all source figures and complete angle working.
    review_angles18=next(problem for problem in review12["problems"] if str(problem["qNo"])=="18")
    review_angles18["question"]="Find the unknown angles in the five triangles. (a) Given20° and110°, find x. (b) Given60° and exterior128°, find interior base angle b and apex a. (c) The two sloping sides are equal and their included angle is86°; find base angle a. (d) A=55° and exterior angle ACD=150° on straight line BCD; find the unknown interior angles. (e) All three sides have matching equality marks, one angle is60°, and the other angles are b and c."
    review_angles18["solution"]=r"(a) \(x=180^\circ-20^\circ-110^\circ=50^\circ\). (b) The interior angle b and exterior128° form a linear pair: \(b=180^\circ-128^\circ=52^\circ\). Then \(a=180^\circ-60^\circ-52^\circ=68^\circ\). Check: the exterior128° equals60°+68°. (c) Equal sloping sides give equal base angles. Their sum is \(180^\circ-86^\circ=94^\circ\), so \(a=94^\circ/2=47^\circ\). (d) \(\angle ACB=180^\circ-150^\circ=30^\circ\); therefore \(\angle ABC=180^\circ-55^\circ-30^\circ=95^\circ\). Check:55°+95°=150°, the exterior angle. (e) Three equal sides make the triangle equilateral. Its angles are equal, so \(b=c=180^\circ/3=60^\circ\), agreeing with the given60° angle."
    review_angles18["diagram"]={"type":"diagram-group","items":[
        {"type":"annotated-angle-figure","title":"18(a) — schematic","points":[[60,240],[280,240],[370,70]],"labels":[[110,230,"20°"],[261,225,"110°"],[342,114,"x"]]},
        {"type":"annotated-angle-figure","title":"18(b) — schematic","points":[[100,245],[180,60],[285,245]],"extensions":[[285,245,395,245]],"labels":[[137,228,"60°"],[181,99,"a"],[260,228,"b"],[318,229,"128°"]]},
        {"type":"annotated-angle-figure","title":"18(c): equal sloping sides","points":[[90,75],[350,75],[220,214.41]],"extensions":[[148,150,162,136],[278,136,292,150]],"labels":[[125,100,"a"],[220,182,"86°"]]},
        {"type":"annotated-angle-figure","title":"18(d): BCD is straight — schematic","points":[[160,55],[85,245],[310,245]],"extensions":[[310,245,400,245]],"labels":[[160,39,"A"],[72,267,"B"],[310,267,"C"],[404,266,"D"],[168,96,"55°"],[341,222,"150°"]]},
        {"type":"annotated-angle-figure","title":"18(e): all three sides are equal","points":[[120,50],[120,250],[293.205,150]],"extensions":[[110,150,130,150],[201,91,211,109],[201,209,211,191]],"labels":[[140,88,"b"],[143,223,"60°"],[257,157,"c"]]}
    ]}

    # Printed p.240: usable demonstrations for the open-ended group project.
    transformation_project=next(problem for problem in review12["problems"] if str(problem["qNo"])=="Project")
    project_panels=[]
    for title,rule in [
        ("Sample translation:3 right and2 down",lambda x,y:(x+3,y-2)),
        ("Sample reflection in the y-axis",lambda x,y:(-x,y)),
        ("Sample rotation:90° counterclockwise",lambda x,y:(-y,x))
    ]:
        panel=transformation_panel(title,[[1,1],[4,1],[2,3]],rule)
        panel["shapes"][0]["labels"]=["A","B","C"]
        panel["shapes"][1]["labels"]=["A′","B′","C′"]
        project_panels.append(panel)
    transformation_project["solutionDiagram"]={"type":"coordinate-panels","panels":project_panels}
    transformation_project["solution"] += " To prepare the display: draw and label the axes with equally spaced units; plot the original vertices; cut out the triangle; calculate the image coordinates before placing the second cut-out; label matching vertices; and write the transformation rule next to the pair. For rotation, mark O as the centre and indicate the90° counterclockwise direction. For reflection, mark the y-axis as the mirror line. For translation, mark the movement3 right and2 down. Each group member can choose one demonstration and explain how every point obeys the same rule. The book illustrates pencil-shaped cut-outs; these labelled triangles are a worked sample for its instruction to choose any shapes."

    # Printed p.242: preserve the source data table alongside the grouped bar graph.
    department_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-1")
    department_graph=department_example["diagram"]
    department_table={"type":"frequency-table","title":"Employees joining each department (p.242)","headers":["Department","May","June","July","August","September"],"rows":[["Research",15,25,10,15,20],["Designing",20,25,15,30,35],["Editing",5,20,15,10,25]]}
    department_example["diagram"]={"type":"diagram-group","items":[department_table,department_graph]}
    next(section for section in chapters[12]["sections"] if section["id"]=="13.1")["diagram"]={"type":"diagram-group","items":[department_table,department_graph]}
    department_example["solution"]="Draw perpendicular axes and label the horizontal axis Month and the vertical axis Number of employees. Mark May, June, July, August and September at equal spacing. Use a vertical scale from0 to40 in steps of5. For every month, draw three equal-width bars in the order Research, Designing, Editing, using a different consistent colour for each department and a legend. The May heights are15,20,5; June25,25,20; July10,15,15; August15,30,10; September20,35,25. Keep the same scale for all departments and start bars at0. Check the equal-height June Research/Designing bars and July Designing/Editing bars. The tallest bar is Designing in September at35 employees. The source table's first heading says Colours, but its rows contain department names; the web table uses Department for clarity."

    # Printed p.243: retain the building-count table in the exercise question.
    bar_exercise=next(ex for ex in chapters[12]["exercises"] if ex["title"]=="Exercise 13.1")
    building_question=next(problem for problem in bar_exercise["problems"] if str(problem["qNo"])=="1")
    building_question["diagram"]={"type":"frequency-table","title":"New buildings constructed during five months","headers":["Type","July","August","September","October","November"],"rows":[["Commercial",5,35,15,10,5],["Residential",10,15,5,5,20]]}
    building_question["solution"]="1. Draw and label the horizontal axis Month and the vertical axis Number of buildings. 2. Mark July to November in order at equal intervals. Use a vertical scale from0 to40 with5 buildings per division. 3. Draw two equal-width bars per month: Commercial and Residential. Their heights are July5/10, August35/15, September15/5, October10/5, November5/20. 4. Use consistent colours, add a legend and leave equal gaps between month groups. Checks: the August commercial bar reaches35, the largest single count; November residential reaches20; the October bars reach10 and5. Every bar starts at the same zero baseline. The solution graph below is drawn from the given table."

    # Printed p.244: show the source line graph inside the lesson as well as the example.
    marks_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-2")
    next(section for section in chapters[12]["sections"] if section["id"]=="13.2")["diagram"]=marks_example["diagram"]
    marks_example["solution"]=r"Read each plotted point against the vertical Marks scale: Week 1 = 3, Week 2 = 7, Week 3 = 5, Week 4 = 5, Week 5 = 8 (all out of 10). From Week 1 to Week 2, \(7-3=4\), so Madiha gained 4 marks. From Week 2 to Week 3, \(7-5=2\), so her marks fell by 2. Weeks 3 and 4 both have 5 marks, giving a horizontal line segment. Week 5 has the highest point, 8 marks; Week 1 has the lowest point, 3 marks. Read the height of a point, not the length of its connecting segment."
    toys_question=next(problem for problem in line_exercise["problems"] if str(problem["qNo"])=="1")
    toys_question["solution"]=r"First read the graph: January 2,000; February 3,000; March 1,500; April 6,000; May 3,500; June 5,000 toys. (a) April has the highest production because its point is highest: 6,000 toys. (b) March and May experienced decreases: February to March falls from 3,000 to 1,500, and April to May falls from 6,000 to 3,500. Name the month at the end of each downward segment. (c) May minus March is \(3500-1500=2000\) more toys. (d) April minus January is \(6000-2000=4000\) toys. This is the net increase between the named months; it is not the sum of their production."

    # Printed p.245: preserve both original tables in the question cards.
    visitors_question=next(problem for problem in line_exercise["problems"] if str(problem["qNo"])=="3")
    visitors_question["diagram"]={"type":"frequency-table","title":"Visitors to Shahi Qila, Lahore","headers":["Month","March","April","May","June","July"],"rows":[["Number of visitors",6000,8500,7000,9000,6500]]}
    temperature_question=next(problem for problem in line_exercise["problems"] if str(problem["qNo"])=="4")
    temperature_question["diagram"]={"type":"frequency-table","title":"Temperature readings at two-hour intervals in April","headers":["Time","8 a.m.","10 a.m.","12 noon","2 p.m.","4 p.m.","6 p.m."],"rows":[["Temperature (°C)",16.5,20.2,28.8,32.4,30.7,26.6]]}
    temperature_question["solution"] += " Mark major divisions every 5°C and subdivide consistently to position the decimal readings; a value such as 20.2°C belongs just above 20°C, not at 22°C. The displayed solution graph positions every reading using the same numerical scale."
    line_exercise["answerKeyText"]="Checked answers: 1(a) April; (b) March and May; (c) 2,000 toys; (d) 4,000 toys. Source answer-key discrepancy: the printed key lists February and April for (b), which are the starting months of the downward segments. The months experiencing the falls are March and May. Questions 3 and 4 are graph constructions; see their plotted solutions."
    pie_reading_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-3-reading")
    next(section for section in chapters[12]["sections"] if section["id"]=="13.3")["diagram"]=pie_reading_example["diagram"]

    # Printed pp.246–247: keep source tables and angle calculations with native charts.
    contribution_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-3")
    contribution_chart=contribution_example["diagram"]
    contribution_example["diagram"]={"type":"diagram-group","items":[
        {"type":"frequency-table","title":"Amounts spent helping children pay school fees","headers":["Student","Dania","Marwa","Fahad","Afnan","Rohaan"],"rows":[["Amount (Rs)",940,800,1000,1200,1100]]},
        {"type":"frequency-table","title":"Central-angle calculations: total Rs 5,040","headers":["Student","Calculation (degrees)","Angle to 2 decimal places","Book's whole-degree angle"],"rows":[["Dania","940 ÷ 5040 × 360","67.14°","67°"],["Marwa","800 ÷ 5040 × 360","57.14°","57°"],["Fahad","1000 ÷ 5040 × 360","71.43°","71°"],["Afnan","1200 ÷ 5040 × 360","85.71°","86°"],["Rohaan","1100 ÷ 5040 × 360","78.57°","79°"],["Total","5040 ÷ 5040 × 360","360° exactly before rounding","360°"]]},contribution_chart]}
    expenditure_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-3-quick")
    expenditure_chart=expenditure_example["diagram"]
    expenditure_example["diagram"]={"type":"diagram-group","items":[{"type":"frequency-table","title":"Quick Check: expenditure and calculated angles","headers":["Item","Expenditure","Angle calculation","Angle (approximately)"],"rows":[["Food",2400,"2400 ÷ 4900 × 360","176.33°"],["Clothes",1000,"1000 ÷ 4900 × 360","73.47°"],["Bills",1500,"1500 ÷ 4900 × 360","110.20°"],["Total",4900,"4900 ÷ 4900 × 360","360°"]]},expenditure_chart]}
    expenditure_example["solution"] += r" For a more accurate hand drawing, use half-degree measurements: food \(176.5^\circ\), clothes \(73.5^\circ\), bills \(110^\circ\); these sum to \(360^\circ\). If your protractor permits only whole-degree marks, one possible approximate closed chart uses food176°, clothes73° and the remaining bills angle \(360^\circ-176^\circ-73^\circ=111^\circ\). The last angle is a closure adjustment, not the independently rounded bills angle. The native chart retains the exact expenditure proportions."

    # Printed p.248: source budget table and fully worked pie constructions.
    pie_exercise=next(ex for ex in chapters[12]["exercises"] if ex["title"]=="Exercise 13.3")
    budget_question=next(problem for problem in pie_exercise["problems"] if str(problem["qNo"])=="1")
    budget_question["diagram"]={"type":"frequency-table","title":"Family budget for one month; income Rs 39,800","headers":["Category","Food","Education","Conveyance","Savings","Miscellaneous"],"rows":[["Amount (Rs)",3150,1950,21100,2400,11200]]}
    budget_question["solution"]=r"First check the total: \(3150+1950+21100+2400+11200=39800\) rupees. For every category use \(\theta=\frac{\text{amount}}{39800}\times360^\circ\). Food: \(\frac{3150}{39800}\times360^\circ\approx28.49^\circ\); education: \(\frac{1950}{39800}\times360^\circ\approx17.64^\circ\); conveyance: \(\frac{21100}{39800}\times360^\circ\approx190.85^\circ\); savings: \(\frac{2400}{39800}\times360^\circ\approx21.71^\circ\); miscellaneous: \(\frac{11200}{39800}\times360^\circ\approx101.31^\circ\). Draw a circle and radius, then measure adjacent sectors in the listed order, starting each angle from the preceding radius. Label all five sectors. The displayed two-decimal angles total360°. Findings: conveyance is the largest share, approximately53.02%, and exceeds half the budget, so its sector is larger than a semicircle. Education is the smallest share, approximately4.90%. Savings are approximately6.03% of income. The chart accounts for the entire stated income."
    savings_question=next(problem for problem in pie_exercise["problems"] if str(problem["qNo"])=="2")
    savings_question["solution"]=r"Add the four savings: \(45+56+65+75=241\) rupees. Apply \(\theta=\frac{\text{weekly saving}}{241}\times360^\circ\). Week1: \(\frac{45}{241}\times360^\circ\approx67.22^\circ\); Week2: \(\frac{56}{241}\times360^\circ\approx83.65^\circ\); Week3: \(\frac{65}{241}\times360^\circ\approx97.10^\circ\); Week4: \(\frac{75}{241}\times360^\circ\approx112.03^\circ\). These displayed angles total360°. Draw a circle, mark an initial radius, measure these four angles successively at the centre and label the sectors Week1 through Week4. For a whole-degree hand construction use67°,84°,97°,112°, which also total360°. Week4 has the greatest saving and sector; Week1 the smallest. The native chart uses exact proportions."

    # Printed p.249: original transport table and both requested sample graph types.
    transport_question=next(problem for problem in pie_exercise["problems"] if str(problem["qNo"])=="4")
    transport_question["diagram"]={"type":"frequency-table","title":"Printed transport data (stated total: 1,080 students)","headers":["Mode of transport","Bus","Cycle","Bike","Car","On foot"],"rows":[["Number of students",198,180,240,27,200]]}
    transport_question["solution"] += r" Check the discrepancy explicitly: \(1080-845=235\). Do not assign these235 students to any named mode without further information. For the chart of listed responses, start with a radius and measure the five calculated angles successively. The displayed two-decimal angles add to360.01° because of rounding; the exact fractions add to360°. A whole-degree drawing can use84°,77°,102°,12°,85°, which close at360°."
    fruit_project=next(problem for problem in pie_exercise["problems"] if str(problem["qNo"])=="6")
    fruit_bars=fruit_project["solutionDiagram"]
    fruit_project["solutionDiagram"]={"type":"diagram-group","items":[fruit_bars,{"type":"pie-sectors","title":"Sample collected data: shares of 20 fruit choices","labels":["Apple","Mango","Banana","Orange"],"values":[8,6,4,2]}]}
    fruit_project["solution"] += r" Collect one response per classmate, record tally marks, and check that the frequencies total20. Calculate sectors using \(\theta=\frac{\text{frequency}}{20}\times360^\circ\): apple144°, mango108°, banana72°, orange36°. Check \(144+108+72+36=360\). For comparing popularity, choose the bar graph: its descending heights show the ranking directly. For comparing shares of the class, choose the pie chart: its sectors show40%,30%,20%,10%. Both native graphs below represent the same illustrative data."

    # Printed pp.250–251: visible data, frequency table and comparison activity.
    data_lesson=next(section for section in chapters[12]["sections"] if section["id"]=="13.4.1")
    data_lesson["diagram"]={"type":"frequency-table","title":"Note it down: classify each quantity","headers":["Quantity","Type","Reason"],"rows":[["Speed of a car","Continuous","Measured; may lie anywhere within a range"],["Number of cars in a showroom","Discrete","Counted in whole cars"],["Mass of a bag of rice","Continuous","Measured; may include fractional kilograms"]]}
    score_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-4a")
    score_table=score_example["diagram"]
    score_grid={"type":"frequency-table","title":"Source scores: read each row from left to right","headers":["1","2","3","4","5","6","7","8","9","10"],"rows":[[2,2,2,3,3,5,5,6,6,6],[6,6,7,7,7,7,7,7,7,7],[7,8,8,8,8,8,8,8,9,9],[9,9,9,9,9,10,10,10,10,10]]}
    score_example["diagram"]={"type":"diagram-group","items":[score_grid,score_table]}
    score_example["solution"] += " The column numbers above the source grid indicate positions within each row, not score values or frequencies. There are four rows of ten observations. For example, score7 appears eight times in the second row and once in the third row, so its frequency is9. Score6 appears three times in the first row and twice in the second, giving5. No student scored4, so the source omits that row; a full0–10 table could include it with frequency0. In the tally column, the numeral5 represents one completed group of five tally strokes."
    comparison_table={"type":"frequency-table","title":"Comparison activity: two different distinctions","headers":["Term","Meaning","Example / consequence"],"rows":[["Discrete data","Separate countable possible values","Number of students"],["Continuous data","Measurements within a range","Height of a student"],["Ungrouped distribution","One row per observed value","Score7 has frequency9"],["Grouped distribution","One row per non-overlapping interval","Summarizes many values; individual values are not retained"]]}
    next(section for section in chapters[12]["sections"] if section["id"]=="13.4.2")["diagram"]={"type":"diagram-group","items":[score_grid,score_table,comparison_table]}

    # Printed pp.252–253: restore full grouped table rather than frequencies alone.
    savings_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-4b")
    savings_grid={"type":"frequency-table","title":"Weekly savings (Rs): 35 original observations","headers":["1","2","3","4","5","6","7"],"rows":[[32,33,33,34,35,36,37],[38,38,39,40,41,42,43],[44,47,47,48,48,48,49],[49,49,50,50,50,50,50],[50,51,51,51,51,51,51]]}
    savings_table={"type":"frequency-table","title":"Grouped frequency distribution of weekly savings","headers":["Class interval (Rs)","Savings in this class (Rs)","Tally groups","Frequency"],"rows":[["32–37","32,33,33,34,35,36,37","5 + 2",7],["38–43","38,38,39,40,41,42,43","5 + 2",7],["44–49","44,47,47,48,48,48,49,49,49","5 + 4",9],["50–55","50,50,50,50,50,50,51,51,51,51,51,51","5 + 5 + 2",12],["Total","35 observations","",35]]}
    savings_example["diagram"]={"type":"diagram-group","items":[savings_grid,savings_table]}
    savings_example["solution"] += r" The source uses \(51-32=19\) for the range and rounds \(19/4=4.75\) up to5 as a planning step. Its inclusive whole-number classes nevertheless contain six possible integer values each; for example32,33,34,35,36,37. Their continuous boundaries31.5 and37.5 differ by6. Distinguish this boundary width from the printed upper-minus-lower limit difference \(37-32=5\). Each5 in the tally-groups column represents a bundle of five strokes; the final numeral gives extra strokes. Count every observation exactly once."
    boundaries_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-4c")
    boundaries_example["solution"] += r" For the first interval, lower boundary \(53-0.5=52.5\), upper boundary \(57+0.5=57.5\). Repeat: \(58-0.5=57.5\), \(62+0.5=62.5\); \(63-0.5=62.5\), \(67+0.5=67.5\); \(68-0.5=67.5\), \(72+0.5=72.5\). All boundary widths are5. Changing interval notation does not change the observations or frequencies: \(4+9+9+13=35\)."
    next(section for section in chapters[12]["sections"] if section["id"]=="13.4.3")["diagram"]={"type":"diagram-group","items":[savings_grid,savings_table,boundaries_example["diagram"]]}

    # Exercise13.4 pp.253–254: complete visible question and answer tables.
    frequency_exercise=next(ex for ex in chapters[12]["exercises"] if ex["title"]=="Exercise 13.4")
    fq={str(problem["qNo"]):problem for problem in frequency_exercise["problems"]}
    fq["1"]["solutionDiagram"]={"type":"frequency-table","title":"Goals in20 hockey matches","headers":["Goals per match","Tally groups","Number of matches"],"rows":[[0,"4",4],[1,"5 + 1",6],[2,"5",5],[3,"3",3],[4,"2",2],["Total","",20]]}
    fq["1"]["solution"] += " Make one row for each possible observed score0,1,2,3,4. Read the20 match scores in order and add one tally to the corresponding row. Each completed group of five tallies counts as5, not as one match. The frequency counts matches, not goals: for example, the row for2 goals has5 matches."
    plant_grid={"type":"frequency-table","title":"Original plant measurements (cm)","headers":["1","2","3","4","5","6","7","8","9","10"],"rows":[[130,125,125,126,127,127,128,128,128,129],[125,140,142,143,144,144,146,146,147,149],[134,135,135,136,136,137,137,138,138,139],[139,130,131,131,131,132,132,133,133,133]]}
    fq["3"]["diagram"]={"type":"diagram-group","items":[plant_grid,{"type":"frequency-table","title":"Complete this source table","headers":["Height of plants (cm)","Tally","Frequency"],"rows":[[label,"—","—"] for label in ["125–129","130–134","135–139","140–144","145–149"]]}]}
    fq["3"]["solutionDiagram"]={"type":"frequency-table","title":"Completed plant-height table","headers":["Height (cm)","Tally groups","Frequency"],"rows":[["125–129","5 + 5",10],["130–134","5 + 5 + 1",11],["135–139","5 + 5",10],["140–144","5",5],["145–149","4",4],["Total","",40]]}
    fq["4"]["solutionDiagram"]={"type":"frequency-table","title":"One valid grouped table of17 donations","headers":["Donation (Rs)","Observations in class","Tally groups","Frequency"],"rows":[["1000–1999","1127","1",1],["2000–2999","2125,2130,2130,2142","4",4],["3000–3999","3118,3141","2",2],["4000–4999","4123,4128,4136,4150","4",4],["5000–5999","5129,5149","2",2],["6000–6999","6124,6154","2",2],["7000–7999","7133,7138","2",2],["Total","17 observations","",17]]}
    fq["4"]["solution"] += r" The question does not prescribe intervals, so this is one valid grouping. The smallest donation1127 lies in1000–1999 and the largest7138 in7000–7999. The consecutive lower limits differ by1000. Include both occurrences of2130 because two separate donations have that amount. Check \(1+4+2+4+2+2+2=17\)."

    # Printed p.255: original mark grid and question-by-question reasoning.
    fq["6"]["diagram"]={"type":"frequency-table","title":"Original marks out of100 for24 students","headers":["1","2","3","4","5","6","7","8"],"rows":[[55,70,57,73,55,59,64,72],[60,48,58,54,69,51,63,78],[75,64,65,57,71,78,76,68]]}
    fq["6"]["solution"] = r"Step1: identify the minimum48 and maximum78; the range is \(78-48=30\). Step2: choose four non-overlapping width10 classes covering all marks:45–54,55–64,65–74,75–84. Other suitable groupings are possible because the question does not prescribe classes. Step3: place every mark in exactly one class. 45–54 contains48,51,54 (3 students). 55–64 contains55,55,57,57,58,59,60,63,64,64 (10 students). 65–74 contains65,68,69,70,71,72,73 (7 students). 75–84 contains75,76,78,78 (4 students). Step4: check \(3+10+7+4=24\), matching the original number of students. Repeated marks are separate students and must each be counted. The completed table below shows this grouping."
    fq["7"]["solution"] = r"(a) Count the interval rows:55–69,70–84,85–99, so there are3 classes. (b) Add the frequencies: \(24+10+15=49\) students. (c) The lowest displayed class limit is55. The exact lowest observed mark is unknown: the first24 students could have any marks within55–69, and the table does not say that anyone scored exactly55. (d) Read the70–84 row:10 students. (e) Combine both classes starting at70 or above: \(10+15=25\) students. Check: the remaining24 students are in55–69, and \(25+24=49\)."
    next(section for section in chapters[12]["sections"] if section["id"]=="13.5")["diagram"]={"type":"frequency-table","title":"Bar chart and histogram: source comparison","headers":["Feature","Bar chart","Histogram"],"rows":[["Horizontal axis","Separate categories, such as names or fruit","Numerical intervals"],["Order","May be rearranged when categories have no natural order","Keep increasing numerical interval order"],["Space between bars","Usually separated by gaps","Adjacent interval bars touch"],["Bar width in this lesson","Equal visual widths for categories","Equal widths represent equal class intervals"],["Vertical axis in this lesson","Value or frequency","Frequency for equal-width classes"]]}

    # Printed pp.256–257: pair histogram examples with their source calculation tables.
    temperature_histogram=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-5a")
    temperature_plot=temperature_histogram["diagram"]
    temperature_frequency={"type":"frequency-table","title":"Lahore temperatures: class width3°C","headers":["Class interval (°C)","Class boundaries (°C)","Tally groups","Frequency (days)"],"rows":[["35–37","34.5–37.5","1",1],["38–40","37.5–40.5","5 + 3",8],["41–43","40.5–43.5","4",4],["44–46","43.5–46.5","5 + 4",9],["47–49","46.5–49.5","5 + 1",6],["50–52","49.5–52.5","3",3],["Total","","",31]]}
    temperature_histogram["diagram"]={"type":"diagram-group","items":[temperature_frequency,temperature_plot]}
    temperature_histogram["solution"] += r" Mark the horizontal boundaries34.5,37.5,40.5,43.5,46.5,49.5,52.5 at equal spacing. Use one day per vertical division, from0 to10. Draw a rectangle over each adjacent boundary pair with heights1,8,4,9,6,3 respectively. Every rectangle starts at0 and shares its edge with the next rectangle. Check the widest-temperature range is not confused with bar height: all widths are3°C; heights count days. The tallest bar represents44–46°C on9 days. The smallest frequency is1 day in35–37°C."
    construction_section=next(section for section in chapters[12]["sections"] if section["id"]=="13.5.1")
    construction_section["diagram"]={"type":"diagram-group","items":[temperature_frequency,temperature_plot]}
    women_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-5b")
    women_plot=women_example["diagram"]
    women_table={"type":"frequency-table","title":"Reading frequencies from the women's height histogram","headers":["Height boundaries (inches)","Frequency (women)"],"rows":[["58.5–60.5",10],["60.5–62.5",12],["62.5–64.5",8],["64.5–66.5",4],["Total",34]]}
    women_example["diagram"]={"type":"diagram-group","items":[women_plot,women_table]}
    women_example["solution"] += r" Read each bar's height against the vertical scale:10,12,8,4. Do not count tick marks as people. For(i), count four rectangles. For(ii), subtract consecutive boundary values: \(60.5-58.5=2\) inches. For(iii), add frequencies: \(10+12+8+4=34\). For(iv), identify the tallest bar, with height12, and read its horizontal boundaries60.5 and62.5 inches."

    # Exercise13.5 pp.257–258: original tables and explicit histogram construction.
    histogram_exercise=next(ex for ex in chapters[12]["exercises"] if ex["title"]=="Exercise 13.5")
    for problem in histogram_exercise["problems"]:
        q=str(problem["qNo"])
        if q=="2":
            problem["diagram"]={"type":"frequency-table","title":"Source table: rotten eggs in30 crates","headers":["Rotten eggs",0,1,4,5,6,7,8,9],"rows":[["Number of crates",2,9,3,4,2,5,1,4]]}
            problem["solution"] += r" Check \(2+9+3+4+2+5+1+4=30\) crates. Include intervals for2 and3 eggs with zero height; do not move the4-egg bar next to the1-egg bar and compress the horizontal scale. Mark egg counts0 through9 at equal spacing, with boundaries halfway between consecutive counts. The boundary−0.5 simply centres the first bin on0; it does not represent negative rotten eggs. The tallest bar is at1 rotten egg, representing9 crates."
        else:
            intervals,counts=({"1":(["30–34","35–39","40–44","45–49","50–54"],[4,6,12,10,8]),"3":(["15–19","20–24","25–29","30–34","35–39"],[5,9,12,10,4]),"4":(["5–14","15–24","25–34","35–44","45–54"],[3,5,2,4,12])})[q]
            problem["diagram"]={"type":"frequency-table","title":"Given frequency distribution","headers":["Class interval","Frequency"],"rows":[[label,count] for label,count in zip(intervals,counts)]+[["Total",sum(counts)]]}
            problem["solution"] += " First subtract0.5 from each lower class limit and add0.5 to each upper limit. Draw and label horizontal Class boundary and vertical Frequency axes. Mark all boundaries using one consistent horizontal scale and frequencies from0 to15 using one consistent vertical scale. Draw each rectangle from the zero baseline to its given frequency; neighbouring class rectangles share an edge. Check that the frequencies total"+str(sum(counts))+". The completed histogram below follows this construction."

    # Printed pp.259–260: mean formulas and original grouped calculation tables.
    mean_example=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-6a")
    mean_example["solution"]=r"There are6 values, so \(n=6\). Add them: \(\sum x=1+6+8+9+7+5=36\). Divide the total by the number of values: \(\bar{x}=\frac{\sum x}{n}=\frac{36}{6}=6\). Check: six equal shares of6 would total36, the same as the original values."
    grouped_mean=next(example for example in chapters[12]["workedExamples"] if example["id"]=="we-13-6c")
    midpoint_table={"type":"frequency-table","title":"Calculate each class midpoint","headers":["Class","Lower limit","Upper limit","Midpoint calculation"],"rows":[["25–39",25,39,"(25 + 39) ÷ 2 = 32"],["40–54",40,54,"(40 + 54) ÷ 2 = 47"],["55–69",55,69,"(55 + 69) ÷ 2 = 62"],["70–84",70,84,"(70 + 84) ÷ 2 = 77"],["85–99",85,99,"(85 + 99) ÷ 2 = 92"]]}
    products_table={"type":"frequency-table","title":"Multiply midpoints by frequencies","headers":["Class","Midpoint m","Frequency f","Product fm"],"rows":[["25–39",32,3,"32 × 3 = 96"],["40–54",47,4,"47 × 4 = 188"],["55–69",62,8,"62 × 8 = 496"],["70–84",77,9,"77 × 9 = 693"],["85–99",92,6,"92 × 6 = 552"],["Total","",30,2025]]}
    grouped_mean["diagram"]={"type":"diagram-group","items":[midpoint_table,products_table]}
    grouped_mean["solution"]=r"Step1: represent each class by its midpoint \(m=\frac{\text{lower limit}+\text{upper limit}}{2}\), giving32,47,62,77,92. Step2: multiply each midpoint by the frequency of its class:96,188,496,693,552. Step3: add the products, \(\sum fm=96+188+496+693+552=2025\), and the frequencies, \(\sum f=3+4+8+9+6=30\). Step4: divide: \(\bar{x}\approx\frac{\sum fm}{\sum f}=\frac{2025}{30}=67.5\) marks. This is the midpoint-based estimate of the original students' mean; individual marks are unavailable. Do not simply average the five midpoints, because the classes contain different numbers of students. The printed product47 × 4 = 96 is incorrect; the correct product188 agrees with the book's total2025 and final67.5."
    next(section for section in chapters[12]["sections"] if section["id"]=="13.6.2")["diagram"]=grouped_mean["diagram"]

    return chapters


def make_section(title, paragraphs):
    match = SECTION_RE.match(title)
    section_id = match.group(1) if match else re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    text = "\n\n".join(paragraphs)
    return {
        "id": section_id,
        "title": title,
        "theory": text,
        "heading": title,
        "headingUrdu": "",
        "text": text,
        "paras": paragraphs,
    }


def make_exercise(title, paragraphs, index):
    problems = []
    current_number = None
    current_lines = []
    for paragraph in paragraphs:
        match = QUESTION_RE.match(paragraph)
        if match:
            if current_lines:
                problems.append({"qNo": current_number or str(len(problems) + 1),
                                 "question": "\n".join(current_lines).strip()})
            current_number = match.group(1)
            current_lines = [match.group(2)]
        elif current_lines:
            current_lines.append(paragraph)
        elif paragraph.strip():
            current_lines = [paragraph]
    if current_lines:
        problems.append({"qNo": current_number or str(len(problems) + 1),
                         "question": "\n".join(current_lines).strip()})
    if not problems:
        problems = [{"qNo": "1", "question": "No exercise text was captured from the transcription."}]
    return {
        "exercise": f"{index}",
        "title": title,
        "problems": problems,
    }


def make_example(title, paragraphs, index):
    question_lines = []
    solution_lines = []
    in_solution = False
    for paragraph in paragraphs:
        solution_match = re.search(r"\b(?:S|C)olution\s*:\s*", paragraph, re.I)
        if solution_match:
            before = paragraph[:solution_match.start()].strip()
            after = paragraph[solution_match.end():].strip()
            if before:
                question_lines.append(before)
            in_solution = True
            if after:
                solution_lines.append(after)
        elif re.match(r"^(?:S|C)olution\s*:?\s*$", paragraph, re.I):
            in_solution = True
        elif in_solution:
            solution_lines.append(paragraph)
        else:
            question_lines.append(paragraph)
    return {
        "id": f"we-7-{index}",
        "title": title or f"Example {index}",
        "problem": "\n".join(question_lines).strip(),
        "solution": "\n".join(solution_lines).strip(),
    }


if __name__ == "__main__":
    data = build()
    OUT.write_text("// Class 7 Mathematics — source-derived KPTBB lessons.\n"
                   "const MATH_7_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n",
                   encoding="utf-8")
    print(f"Wrote {len(data)} units, {sum(len(c['sections']) for c in data)} lessons, "
          f"{sum(len(c['workedExamples']) for c in data)} examples, and "
          f"{sum(len(c['exercises']) for c in data)} exercise sets to {OUT}")
