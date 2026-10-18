"""
analyze_unit_boundaries.py
Finds exact boundaries for:
- SLO block
- Main lesson/poem text
- About Author/Poet
- Glossary
- Reading Comprehension
- Writing Suggestions
- Grammar
across all 19 units.
"""
import docx
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th English\Word"
parts = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx')])

all_paras = []
for p in parts:
    doc = docx.Document(p)
    for par in doc.paragraphs:
        t = par.text.strip()
        all_paras.append(t)

print(f"Total raw paragraphs: {len(all_paras)}")

# Unit start markers from docx
UNIT_STARTS = [
    (1,  258,  "Seerat-e-Tayyiba and the Muslim Youth", "prose"),
    (2,  825,  "Jinnah's Vision of Pakistan", "prose"),
    (3,  1085, "The Solitary Reaper", "poem"),
    (4,  1311, "Truck Art", "prose"),
    (5,  1601, "The Last Leaf", "prose"),
    (6,  1927, "If", "poem"),
    (7,  2254, "Hubble Space Telescope", "prose"),
    (8,  2677, "Lesson from the Battle of Uhud", "prose"),
    (9,  2944, "The Toys", "poem"),
    (10, 3243, "Gender Inequality and its Implications", "prose"),
    (11, 3526, "Jahangir Khan — The Conqueror", "prose"),
    (12, 3839, "All the World's a Stage", "poem"),
    (13, 4159, "Technical Education", "prose"),
    (14, 4566, "Lingkuan Gorge", "prose"),
    (15, 4885, "Once Upon a Time", "poem"),
    (16, 5270, "Tourist Attractions in Pakistan", "prose"),
    (17, 5590, "Désirée's Baby", "prose"),
    (18, 6023, "Lines from the Deserted Village", "poem"),
    (19, 6246, "Lord of the Flies", "prose")
]

for idx, (num, start_idx, title, utype) in enumerate(UNIT_STARTS):
    next_idx = UNIT_STARTS[idx + 1][1] if idx + 1 < len(UNIT_STARTS) else len(all_paras)
    unit_slice = all_paras[start_idx:next_idx]
    
    # Locate SLO end / Text start
    slo_end = 0
    about_author_idx = -1
    glossary_idx = -1
    reading_comp_idx = -1
    writing_idx = -1
    grammar_idx = -1
    
    for i, p in enumerate(unit_slice):
        low = p.lower()
        if re.match(r'^(about the (author|poet|writer))', low):
            if about_author_idx == -1: about_author_idx = i
        elif low in ('glossary', 'word meaning', 'words and meanings') or re.match(r'^glossary\b', low):
            if glossary_idx == -1: glossary_idx = i
        elif 'reading comprehension' in low or 'answer the following' in low or 'comprehension questions' in low:
            if reading_comp_idx == -1: reading_comp_idx = i
        elif 'writing suggestion' in low or 'writing task' in low or 'post-reading' in low:
            if writing_idx == -1: writing_idx = i
        elif 'vocabulary and grammar' in low or 'grammar activities' in low:
            if grammar_idx == -1: grammar_idx = i
            
    print(f"Unit {num:2d}: {title:35s} | len={len(unit_slice)} | author={about_author_idx} | gloss={glossary_idx} | comp={reading_comp_idx} | writ={writing_idx} | gram={grammar_idx}")
