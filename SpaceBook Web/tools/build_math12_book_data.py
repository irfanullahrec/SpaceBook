"""Build Class 12 maths around the printed book pages and Word text helper.

The scanned pages are the presentation source. The Word transcription is used
only to find section, example, and exercise headings and associate them with
printed pages; it is not shown as a substitute for the scans.
"""

from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json
import re
import sys


ROOT = Path(r"D:\SpaceBook\Books\12th\12th Maths")
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

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
UNIT_BY_PAGE = {page: (n, title, lo, hi) for n, title, lo, hi in UNITS for page in range(lo, hi + 1)}

SECTION_RE = re.compile(r"^\s*(\d{1,2}\.\d{1,2})\s+(.+?)\s*$")
EXAMPLE_RE = re.compile(r"^\s*(?:Worked\s+)?Example\s*(\d+)?\b(.*)$", re.I)
EXERCISE_RE = re.compile(r"^\s*(Review\s+Exercise|Exercise)(?:\s+([\d.]+))?\s*$", re.I)
UNIT_HEADER_RE = re.compile(r"^\s*UNIT\s*[-.]?\s*(\d{1,2})\b", re.I)
PAGE_TEXT_RE = re.compile(r"^\s*(\d{1,3})\s*$")


def read_documents():
    docs = []
    for path in sorted((ROOT / "Word").glob("*.docx")):
        with ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
        lines = []
        for paragraph in root.findall(".//w:p", NS):
            text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()
            if text:
                lines.append(text)

        # Only the fifth file reaches the answer key. The word "Answers" also
        # appears in the contents pages, so use it only after Unit 12 begins.
        if "part_05_of_05" in path.name:
            unit12_index = next((i for i, line in enumerate(lines)
                                 if re.match(r"^\s*UNIT\s*[-.]?\s*12\b", line, re.I)), 0)
            answer_index = next((i for i, line in enumerate(lines[unit12_index:], unit12_index)
                                 if line.strip().upper() == "ANSWERS"), len(lines))
            lines = lines[:answer_index]

        page_marks = []
        for i, text in enumerate(lines):
            match = PAGE_TEXT_RE.fullmatch(text)
            if not match:
                continue
            page = int(match.group(1))
            if not 1 <= page <= 356:
                continue
            before = lines[i - 1].strip().lower() if i else ""
            after = lines[i + 1].strip().lower() if i + 1 < len(lines) else ""
            if before in {"not for sale", "not for"} or after in {"not for sale", "not for"}:
                page_marks.append((i, page))
        docs.append({"name": path.name, "lines": lines, "page_marks": page_marks})
    return docs


def page_for(doc, index, unit):
    _, _, page_start, page_end = unit
    candidates = []
    for marker_index, printed_page in doc["page_marks"]:
        if marker_index < index:
            candidate = printed_page + 1
            distance = index - marker_index
            tie_order = 1
        elif marker_index > index:
            candidate = printed_page
            distance = marker_index - index
            tie_order = 0
        else:
            continue
        if page_start <= candidate <= page_end:
            candidates.append((distance, tie_order, candidate))
    if not candidates:
        return page_start
    return min(candidates)[2]


def clean_heading(text):
    return re.sub(r"\s+", " ", text.strip())


def parse_events(docs):
    all_events = []
    for doc_id, doc in enumerate(docs):
        lines = doc["lines"]
        raw = []
        i = 0
        while i < len(lines):
            text = clean_heading(lines[i])
            section = SECTION_RE.match(text)
            example = EXAMPLE_RE.match(text)
            exercise = EXERCISE_RE.match(text)
            if section and int(section.group(1).split(".")[0]) in range(1, 13):
                unit_n = int(section.group(1).split(".")[0])
                if section.group(1).count(".") == 1:
                    raw.append({"kind": "section", "unit": unit_n, "index": i,
                                "title": f"{section.group(1)} {section.group(2)}",
                                "id": section.group(1), "doc": doc_id})
            elif example:
                # The next paragraph is often the continuation of a long example title.
                title = clean_heading(text)
                raw.append({"kind": "example", "unit": None, "index": i,
                            "title": title, "number": example.group(1),
                            "doc": doc_id})
            elif exercise or re.match(r"^\s*Exercise\s*\(\s*\d+\.\d+", text, re.I):
                kind_text = exercise.group(1).lower() if exercise else "exercise"
                number = exercise.group(2) if exercise else None
                if not number and i + 1 < len(lines) and re.fullmatch(r"\d+(?:\.\d+)*", lines[i + 1].strip()):
                    number = lines[i + 1].strip()
                is_review = kind_text.startswith("review")
                title = ("Review Exercise" if is_review else "Exercise") + (f" {number}" if number else "")
                raw.append({"kind": "exercise", "unit": None, "index": i,
                            "title": title, "number": number,
                            "doc": doc_id})
            elif re.match(r"^\s*(?:Summary|History)\s*$", text, re.I):
                raw.append({"kind": "endmatter", "unit": None, "index": i,
                            "title": text, "doc": doc_id})
            i += 1

        for event in raw:
            # Numbered lesson and review headings identify their unit directly.
            if event["kind"] == "section":
                unit = UNITS[event["unit"] - 1]
            else:
                prior_units = [(i, int(m.group(1))) for i, line in enumerate(lines[:event["index"]])
                               if (m := UNIT_HEADER_RE.match(line)) and 1 <= int(m.group(1)) <= 12]
                following_units = [(i, int(m.group(1))) for i, line in enumerate(lines[event["index"] + 1:], event["index"] + 1)
                                   if (m := UNIT_HEADER_RE.match(line)) and 1 <= int(m.group(1)) <= 12]
                unit_number = prior_units[-1][1] if prior_units else (following_units[0][1] if following_units else None)
                if unit_number is None:
                    continue
                unit = UNITS[unit_number - 1]
                event["unit"] = unit_number
            event["page"] = page_for(doc, event["index"], unit)
            event["docName"] = doc["name"]
            all_events.append(event)

        # Attach the printed text following each example or exercise marker.
        for j, event in enumerate(raw):
            if event["kind"] not in {"example", "exercise"}:
                continue
            next_index = next((other["index"] for other in raw[j + 1:]
                               if other["kind"] in {"example", "exercise", "section", "endmatter"}),
                              len(lines))
            event["sourceText"] = [line for line in lines[event["index"]:next_index]
                                   if line.strip() and not re.fullmatch(r"\d{1,3}", line.strip())
                                   and line.strip().lower() not in {"not for sale", "not for"}
                                   and not re.match(r"^UNIT\s*[-.]?\s*\d+\b", line.strip(), re.I)]

    return all_events


def event_page_range(event, events, unit):
    _, _, page_start, page_end = unit
    next_pages = [other["page"] for other in events
                  if other["unit"] == event["unit"] and other["page"] > event["page"]
                  and (other["kind"] in {"section", "example", "exercise", "endmatter"})]
    next_page = min(next_pages) if next_pages else page_end + 1
    return max(page_start, event["page"]), max(event["page"], min(page_end, next_page - 1))


def unique_items(items, kind):
    deduped = {}
    for item in items:
        key = (kind, item["title"].lower(), item["page"],
               re.sub(r"\W+", " ", " ".join(item.get("sourceText", [])[:2]).lower())[:110])
        current = deduped.get(key)
        if current is None or len(item.get("sourceText", [])) > len(current.get("sourceText", [])):
            deduped[key] = item
    return sorted(deduped.values(), key=lambda x: (x["page"], x["index"], x["doc"]))


def build(docs):
    events = parse_events(docs)
    chapters = []
    for number, title, first_page, last_page in UNITS:
        unit = (number, title, first_page, last_page)
        section_events = [e for e in events if e["kind"] == "section" and e["unit"] == number]
        sections_by_id = {}
        for event in section_events:
            previous = sections_by_id.get(event["id"])
            if previous is None or event["page"] < previous["page"]:
                sections_by_id[event["id"]] = event
        ordered_sections = sorted(sections_by_id.values(), key=lambda e: (e["page"], [int(x) for x in e["id"].split(".")]))
        if not ordered_sections:
            ordered_sections = [{"kind": "section", "id": f"{number}.1", "title": title,
                                 "page": first_page, "index": 0, "doc": -1, "unit": number}]
        # The first lesson always opens on the printed unit title page.
        ordered_sections[0]["page"] = first_page
        sections = []
        for idx, event in enumerate(ordered_sections):
            start = event["page"]
            later = [x["page"] for x in ordered_sections[idx + 1:] if x["page"] > start]
            end = min(last_page, min(later) - 1 if later else last_page)
            sections.append({"id": event["id"], "title": event["title"], "theory": "",
                             "rules": [], "pageStart": start, "pageEnd": end})

        chapter_events = [e for e in events if e.get("unit") == number and e["kind"] in {"section", "example", "exercise", "endmatter"}]
        examples = []
        for i, event in enumerate(unique_items([e for e in chapter_events if e["kind"] == "example"], "example"), 1):
            start, end = event_page_range(event, chapter_events, unit)
            examples.append({"id": f"{number}-example-{i}", "title": event["title"],
                             "problem": "", "given": "", "method": "", "steps": [], "answer": "",
                             "pageStart": start, "pageEnd": end})

        exercises = []
        seen_exercises = set()
        for event in unique_items([e for e in chapter_events if e["kind"] == "exercise"], "exercise"):
            key = (event["title"].lower(), event["page"])
            if key in seen_exercises:
                continue
            seen_exercises.add(key)
            start, end = event_page_range(event, chapter_events, unit)
            exercises.append({"exercise": event["title"], "title": event["title"],
                              "description": "", "problems": [], "pageStart": start, "pageEnd": end})

        chapters.append({
            "number": number, "id": f"math12-unit-{number}", "title": title,
            "pageRange": f"Pages {first_page}–{last_page}",
            "pageStart": first_page, "pageEnd": last_page,
            "sections": sections, "workedExamples": examples, "exercises": exercises,
            "slos": {"mcqs": [], "shortQuestions": [], "longQuestions": []},
            "formulaSheet": []
        })
    return chapters


documents = read_documents()
if "--unit-headings" in sys.argv:
    requested = [int(value) for value in sys.argv[sys.argv.index("--unit-headings") + 1:]
                 if value.isdigit()]
    result = {}
    for unit_number in requested:
        result[str(unit_number)] = [line for doc in documents for line in doc["lines"]
                                    if re.match(rf"^\s*{unit_number}\.\d+(?:\.\d+)?\b", line)]
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    sys.exit(0)
chapters = build(documents)
book = {"chapters": chapters,
        "bookMeta": {"answerStart": 326, "answerEnd": 356, "pageStart": 1, "pageEnd": 356}}
if "--summary" in sys.argv:
    print(json.dumps([{
        "number": chapter["number"],
        "sections": [{"id": section["id"], "title": section["title"],
                      "pageStart": section["pageStart"], "pageEnd": section["pageEnd"]}
                     for section in chapter["sections"]],
        "workedExamples": [{"title": example["title"],
                            "pageStart": example["pageStart"], "pageEnd": example["pageEnd"]}
                           for example in chapter["workedExamples"]],
        "exercises": [{"title": exercise["title"],
                       "pageStart": exercise["pageStart"], "pageEnd": exercise["pageEnd"]}
                      for exercise in chapter["exercises"]]
    } for chapter in chapters], ensure_ascii=False, separators=(",", ":")))
else:
    print(json.dumps(book, ensure_ascii=False, separators=(",", ":")))
