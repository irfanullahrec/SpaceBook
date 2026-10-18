"""Debug unit 9 processing."""
import sys, re, json, os
sys.stdout.reconfigure(encoding='utf-8')
from docx import Document

DOCX_DIR = r'D:\SpaceBook\Books\12th\12th English\Word'
parts = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx')])
all_paras = []
for p in parts:
    doc = Document(p)
    for par in doc.paragraphs:
        t = par.text.strip()
        if t:
            all_paras.append(t)

# Import the module by exec'ing the script
exec(open(r'D:\SpaceBook\SpaceBook Web\tools\build_english_12_smart.py', encoding='utf-8').read().split('# ─── Main')[0])

# Now call process_unit directly for unit 9
unit_meta = {
    'number': 9, 'title': 'The Toys', 'titleUrdu': 'کھلونے',
    'type': 'poem', 'author': 'Coventry Patmore'
}
raw = all_paras[2944:3243]

# Patch process_unit to add debug
SEC_LESSON = 'lesson'
SEC_READING = 'reading'
SEC_WRITING = 'writing'
SEC_VOCAB   = 'vocab'

current_sec = SEC_LESSON
lesson_paras = []
comp_lines = []
writing_lines = []
vocab_lines = []
glossary_words = []
in_glossary = False
gloss_word = None

unit_title_lower = unit_meta['title'].lower()
unit_title_short = unit_title_lower[:20]

title_occurrences = []
for idx, p in enumerate(raw):
    if p.strip().lower().startswith(unit_title_short) and len(p.strip()) < 100:
        title_occurrences.append(idx)

if len(title_occurrences) >= 2:
    content_start_idx = title_occurrences[1] + 1
elif title_occurrences:
    content_start_idx = title_occurrences[0] + 1
else:
    content_start_idx = 0

print(f"Title occurrences: {title_occurrences}, content_start_idx={content_start_idx}")

if content_start_idx < len(raw):
    author_check = raw[content_start_idx].strip()
    print(f"Author check: {repr(author_check[:60])} len={len(author_check)}")
    if len(author_check) < 60 and re.match(r'^[A-Z]', author_check) and '.' not in author_check[5:]:
        content_start_idx += 1
        print(f"  -> Skipped as author, new csi={content_start_idx}")

i = 0
while i < len(raw):
    p = raw[i].strip()
    if i < content_start_idx:
        i += 1
        continue
    if is_noise(p):
        i += 1
        continue
    sec = is_section_marker(p)
    if sec:
        current_sec = sec
        print(f"[{i}] SECTION MARKER: {repr(p[:60])} -> {sec}")
        in_glossary = (sec == 'vocab')
        i += 1
        continue
    if p.lower() in ('word', 'meaning', 'glossary', 'words', 'meanings'):
        in_glossary = True
        print(f"[{i}] GLOSSARY START: {repr(p)}")
        i += 1
        continue
    if re.match(r'^References?\s*:', p, re.I):
        print(f"[{i}] REFERENCES BREAK: {repr(p[:60])}")
        break
    
    cleaned = clean_english(p)
    if not cleaned or len(cleaned) < 5:
        print(f"[{i}] FILTERED OUT by clean: {repr(p[:60])}")
        i += 1
        continue
    
    if current_sec == SEC_LESSON:
        lesson_paras.append(cleaned)
    i += 1

print(f"\nlesson_paras: {len(lesson_paras)}")
for j, p in enumerate(lesson_paras[:15]):
    print(f"  [{j}]: {repr(p[:80])}")

# Now merge
merged = merge_fragments(lesson_paras, is_poem=True)
print(f"\nMerged (stanzas): {len(merged)}")
for j, s in enumerate(merged[:5]):
    print(f"  stanza[{j}]: {repr(s[:100])}")
