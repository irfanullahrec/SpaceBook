"""
Smart English 12 Extractor v2 — KPK Textbook Board
Based on detailed analysis of raw paragraph structure.
Key findings:
- TOC ends around para 258
- Each unit: title → SLO bullets → actual lesson text (with noise) → glossary → exercises
- Sentence fragments are common (short paras that continue previous sentence)
- Urdu gloss words appear as standalone short paras (پیغمبر, یاد کرنا, etc.)
- Noise: NOT FOR SALE, Whatcann, digit strings, single letters, OLE, MON, etc.
"""
import sys, re, json, os
sys.stdout.reconfigure(encoding='utf-8')

try:
    from docx import Document
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-docx', '-q'])
    from docx import Document

DOCX_DIR = r'D:\SpaceBook\Books\12th\12th English\Word'
OUT_FILE  = r'D:\SpaceBook\SpaceBook Web\js\english_12_data.js'

# ─── Unit metadata ────────────────────────────────────────────────
UNITS = [
    { 'number': 1,  'title': 'Seerat-e-Tayyiba and the Muslim Youth',
      'titleUrdu': 'سیرتِ طیبہ اور مسلم نوجوان', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 2,  'title': "Jinnah's Vision of Pakistan",
      'titleUrdu': 'پاکستان کے بارے میں قائداعظم کا وژن', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 3,  'title': 'The Solitary Reaper',
      'titleUrdu': 'تنہا کاٹنے والی', 'type': 'poem', 'author': 'William Wordsworth' },
    { 'number': 4,  'title': 'Truck Art',
      'titleUrdu': 'ٹرک آرٹ', 'type': 'prose', 'author': 'Rachel Redford' },
    { 'number': 5,  'title': 'The Last Leaf',
      'titleUrdu': 'آخری پتا', 'type': 'prose', 'author': 'O. Henry' },
    { 'number': 6,  'title': 'If',
      'titleUrdu': 'اگر', 'type': 'poem', 'author': 'Rudyard Kipling' },
    { 'number': 7,  'title': 'Hubble Space Telescope',
      'titleUrdu': 'ہبل خلائی دوربین', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 8,  'title': 'Lesson from the Battle of Uhud',
      'titleUrdu': 'غزوۂ احد کا سبق', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 9,  'title': 'The Toys',
      'titleUrdu': 'کھلونے', 'type': 'poem', 'author': 'Coventry Patmore' },
    { 'number': 10, 'title': 'Gender Inequality and its Implications',
      'titleUrdu': 'صنفی عدم مساوات اور اس کے اثرات', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 11, 'title': 'Jahangir Khan — The Conqueror',
      'titleUrdu': 'جہانگیر خان — فاتح', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 12, 'title': "All the World's a Stage",
      'titleUrdu': 'یہ دنیا ایک اسٹیج ہے', 'type': 'poem', 'author': 'William Shakespeare' },
    { 'number': 13, 'title': 'Technical Education',
      'titleUrdu': 'فنی تعلیم', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 14, 'title': 'Lingkuan Gorge',
      'titleUrdu': 'لنگکوان گھاٹی', 'type': 'prose', 'author': 'Tu Peng-Cheng' },
    { 'number': 15, 'title': 'Once Upon a Time',
      'titleUrdu': 'ایک زمانے میں', 'type': 'poem', 'author': 'Gabriel Okara' },
    { 'number': 16, 'title': 'Tourist Attractions in Pakistan',
      'titleUrdu': 'پاکستان میں سیاحتی مقامات', 'type': 'prose', 'author': 'KPK Textbook Board' },
    { 'number': 17, 'title': "Désirée's Baby",
      'titleUrdu': 'ڈیزیری کا بچہ', 'type': 'prose', 'author': 'Kate Chopin' },
    { 'number': 18, 'title': 'Lines from the Deserted Village',
      'titleUrdu': 'ویران گاؤں سے اشعار', 'type': 'poem', 'author': 'Oliver Goldsmith' },
    { 'number': 19, 'title': 'Lord of the Flies (Abridged)',
      'titleUrdu': 'مکھیوں کا سردار (مختصر)', 'type': 'prose', 'author': 'William Golding' },
]

# ─── Character ranges ─────────────────────────────────────────────
URDU_RE = re.compile(r'[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]')
ARABIC_BULLET = re.compile(r'^[⚫•■◆▪●]')

# ─── Noise detection ──────────────────────────────────────────────
NOISE_EXACT = {
    'NOT FOR SALE', 'NOT FOR SALE.', 'NOT FOR SALE-', 'NOT FOR SALE--',
    'Whatcann', 'Whatcan', 'Whatca', 'What',
    'MON', 'OLE', 'COM', 'W', 'A', 'O', 'P',
    'wazeinar', 'awazeinqilab.com',
    'Unit', 'Unit 1', 'Unit 2',
    'References:', 'Glossary', 'Word', 'Meaning',
}

def is_noise(text):
    t = text.strip()
    if not t:
        return True
    # Exact-match noise strings
    if t in NOISE_EXACT:
        return True
    # Pure digit string (page numbers, watermarks)
    if re.match(r'^\d+$', t):
        return True
    # Long digit watermarks like 2025347270
    if re.match(r'^\d{6,}$', t):
        return True
    # Single letter or very short (1-3 chars) with no real words
    if len(t) <= 3 and not re.search(r'[a-zA-Z]{3}', t):
        return True
    # Mostly Urdu/Arabic (>70% Arabic unicode) AND short (<80 chars)
    urdu_count = len(URDU_RE.findall(t))
    total = len(t.replace(' ', ''))
    if total > 0 and urdu_count / total > 0.7 and len(t) < 80:
        return True
    # SLO/learning objective bullets — only pure bullets, not mixed content
    if ARABIC_BULLET.match(t) and len(t) < 150:
        return True
    if re.match(r'^(By the end|Students will be able to)', t, re.I):
        return True
    # Watermark-only lines (watermark + nothing else or minor chars)
    if re.match(r'^(NOT FOR SALE|FOR SALE|Whatcann?[i]?|wazeinar|awazeinqilab)[\s\-\.]*$', t, re.I):
        return True
    return False

def is_section_marker(text):
    t = text.strip()
    t_low = t.lower()
    # Reading/comprehension section headers — must be short or an explicit heading
    if any(x in t_low for x in [
        'reading comprehension', 'answer the following', 'answer these questions',
        'answer the questions', 'short questions', 'comprehension questions'
    ]) and len(t) < 80:
        return 'reading'
    # Writing section headers — must start the line and be short
    if len(t) < 80 and any(t_low.startswith(x) for x in [
        'writing suggestion', 'pre-writing', 'post-writing', 'writing task',
        'paragraph writing', 'writing skills', 'creative writing',
    ]):
        return 'writing'
    # Vocabulary/Grammar section headers — must be EXACT matches or very specific phrases
    if any(t_low == x for x in [
        'vocabulary and grammar', 'vocabulary', 'grammar activities',
        'language activities', 'pronunciation', 'glossary', 'language skills',
        'vocabulary activities',
    ]):
        return 'vocab'
    if any(x in t_low for x in [
        'vocabulary and grammar', 'grammar activit', 'fill in the blank',
        'use the following words', 'use the following word in',
        'make sentences using', 'define the following words',
    ]) and len(t) < 80:
        return 'vocab'
    return None

def is_slo_block(text):
    """True if this paragraph is part of the SLO/objectives preamble."""
    t = text.strip()
    slo_starts = (
        'By the end', '• ', '⚫', '■', '●', '▪', '◆',
        'Use pre-reading', 'Skim text', 'infer theme', 'Apply critical',
        'Scan to answer', 'Use pronunciation', 'Use appropriate vocabulary',
        'Select and use', 'Illustrate use', 'Write an introductory',
        'Deduce the meaning', 'Analyze story', 'After reading', 'Demonstrate',
        'Recite', 'recognize the author', 'identify universal',
        'contextual clues', 'have general idea', 'reading) to',
        'Use the knowledge of roots', 'suffixes and affixes',
        'read for general comprehension', 'while- reading',
        'while reading', 'write a descriptive', 'write a narrative',
        'write a formal letter', 'write a paragraph',
        'topic / picture', 'title / headings', 'key words and visuals',
        'pre-reading strategies',
    )
    return any(t.startswith(s) or t.lower().startswith(s.lower()) for s in slo_starts)

def clean_english(text):
    """Clean a paragraph: strip watermarks, remove Urdu gloss, normalize."""
    t = text.strip()
    # Strip leading noise watermarks that are prepended to real content
    watermark_prefix = re.compile(
        r'^(NOT FOR SALE[-\.\s]*|FOR SALE[-\.\s]*|Whatcann?[i\.\s]*|'
        r'wazeinar[^\s]*\s*|awazeinqilab\S*\s*|NOT FOR SAL[^\s]*\s*)',
        re.I
    )
    t = watermark_prefix.sub('', t).strip()
    # Remove Urdu parenthetical glosses: (رسول الله ...)
    t = re.sub(r'\([^)]{0,80}[\u0600-\u06FF][^)]{0,80}\)', '', t)
    # Remove standalone Urdu words (not in parens) in the middle of English text
    # Only strip if they appear between ASCII words
    t = re.sub(r'(?<=[a-zA-Z,\.!\?])\s+[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]+\s+(?=[a-zA-Z])', ' ', t)
    # Normalize whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    # Remove leading punctuation artefacts
    t = re.sub(r'^[,\-\.\)\(\[\]\/\\]+\s*', '', t).strip()
    return t

def should_join(prev, curr):
    """True if curr should be appended to prev (continuation fragment)."""
    if not prev or not curr:
        return False
    c = curr.strip()
    p = prev.strip()

    # Never join two substantial paragraphs that are both complete sentences
    prev_complete = p and p[-1] in '.!?"\')'
    curr_substantial = len(c) > 80

    # Very short fragment (definitely a continuation) — always join
    if len(c) < 25:
        return True

    # Previous is short (truncated) — likely needs continuation
    if len(p) < 100 and not prev_complete:
        return True

    # Previous ends mid-sentence (truncated by docx reader) — join
    if not prev_complete and not curr_substantial:
        return True

    if not prev_complete and curr_substantial:
        # Prev is truncated and curr is big — join only if curr starts lowercase or conjunction
        if c[0].islower():
            return True
        if re.match(r'^(and|but|or|nor|so|yet|because|that|which|who|whose|whom|however|therefore|thus|hence|although|though|while|when|as|since|until|unless|for)\b', c, re.I):
            return True
        return True  # still join truncated prev with any continuation

    # Both complete — join only if curr is clearly a continuation
    if prev_complete and curr_substantial:
        if c[0].islower():
            return True
        if re.match(r'^(and|but|or|nor|so|yet|however|therefore|thus|hence|although|though|while|when|as|since|until|unless|for|with|which|who)\b', c, re.I):
            return True
        return False

    # Short continuation (25-80 chars) — join unless prev is complete
    if not prev_complete:
        return True
    if c[0].islower():
        return True
    if re.match(r'^(and|but|or|nor|so|yet|because|that|which|who|whose|whom|however|therefore|thus|hence|although|though|while|when|as|since|until|unless|for)\b', c, re.I):
        return True

    return False

# ─── Read docx files ──────────────────────────────────────────────
def read_all_paragraphs():
    parts = sorted([
        os.path.join(DOCX_DIR, f)
        for f in os.listdir(DOCX_DIR) if f.endswith('.docx')
    ])
    print(f'Reading {len(parts)} docx parts...', flush=True)
    paras = []
    for pf in parts:
        doc = Document(pf)
        for p in doc.paragraphs:
            t = p.text.strip()
            if t:
                paras.append(t)
    print(f'Total raw paragraphs: {len(paras)}', flush=True)
    return paras

# ─── Find unit start indices ──────────────────────────────────────
UNIT_KWS = [
    ['seerat-e-tayyiba'],
    ["jinnah's vision"],
    ['solitary reaper'],
    ['truck art'],
    ['the last leaf'],
    [r'^if$'],
    ['hubble'],
    ['battle of uhud'],
    [r'^the toys$'],
    ['gender inequality'],
    ['jahangir khan'],
    ["all the world's a stage"],
    ['technical education'],
    ['lingkuan'],
    ['once upon a time'],
    ['tourist attractions'],
    ['desiree', 'désirée'],
    ['deserted village'],
    ['lord of the flies'],
]

def find_unit_starts(paras):
    starts = [None] * 19
    search_start = 250  # skip TOC
    for i, kws in enumerate(UNIT_KWS):
        for idx in range(search_start, len(paras)):
            t_low = paras[idx].strip().lower()
            matched = any(
                bool(re.search(kw, t_low, re.I)) for kw in kws
            )
            # Accept only if it's a short heading (not a sentence with the word in it)
            if matched and len(paras[idx].strip()) < 100:
                starts[i] = idx
                search_start = idx + 100  # next unit at least 100 paras later
                print(f'  Unit {i+1} @ para {idx}: {paras[idx].strip()[:70]}', flush=True)
                break
        if starts[i] is None:
            print(f'  WARN: Unit {i+1} not found', flush=True)
    return starts

# ─── Process a unit's paragraphs ─────────────────────────────────
def process_unit(raw_paras, unit_meta):
    # Phase 1: Tag each paragraph as noise / slo / english_content / section_marker
    SEC_LESSON   = 'lesson'
    SEC_READING  = 'reading'
    SEC_WRITING  = 'writing'
    SEC_VOCAB    = 'vocab'

    current_sec = SEC_LESSON
    past_slo    = False

    lesson_paras   = []
    comp_lines     = []
    writing_lines  = []
    vocab_lines    = []
    glossary_words = []  # word: meaning pairs

    # Track glossary section
    in_glossary = False
    gloss_word = None

    i = 0
    # Build a short prefix of the unit title for matching
    unit_title_lower = unit_meta['title'].lower()
    unit_title_short = unit_title_lower[:20]

    # Find the second occurrence of the unit title (marks actual content start)
    # First occurrence = the heading, second occurrence = start of actual lesson
    title_occurrences = []
    for idx, p in enumerate(raw_paras):
        if p.strip().lower().startswith(unit_title_short) and len(p.strip()) < 100:
            title_occurrences.append(idx)

    # Content starts AFTER the second title occurrence (or first if only one)
    if len(title_occurrences) >= 2:
        content_start_idx = title_occurrences[1] + 1
    elif len(title_occurrences) == 1:
        content_start_idx = title_occurrences[0] + 1
    else:
        content_start_idx = 0

    # Skip past author name immediately after title
    if content_start_idx < len(raw_paras):
        author_check = raw_paras[content_start_idx].strip()
        if len(author_check) < 60 and re.match(r'^[A-Z]', author_check) and '.' not in author_check[5:]:
            content_start_idx += 1  # skip author line

    while i < len(raw_paras):
        p = raw_paras[i].strip()

        # Before actual content starts: skip everything except noise check
        if i < content_start_idx:
            i += 1
            continue

        # Check basic noise
        if is_noise(p):
            i += 1
            continue

        # Section marker detection
        sec = is_section_marker(p)
        if sec:
            current_sec = sec
            in_glossary = (sec == 'vocab')
            i += 1
            continue

        # Detect glossary: "Word" followed by "Meaning" then word/meaning pairs
        if p.lower() in ('word', 'meaning', 'glossary', 'words', 'meanings'):
            in_glossary = True
            i += 1
            continue

        # Detect "References:" section — skip rest
        if re.match(r'^References?\s*:', p, re.I):
            break

        # In glossary: alternating word / meaning lines
        if in_glossary and current_sec in (SEC_VOCAB, SEC_LESSON):
            # Pattern: "word (n)" or "wordform" then next line is meaning
            if re.match(r'^[a-zA-Z][\w\s\-\(\)]+$', p) and len(p) < 50:
                m = re.match(r'^([a-zA-Z][a-zA-Z\s\-]+)\s*(\([\w\.]+\))?\s*$', p)
                if m:
                    gloss_word = m.group(1).strip()
                    i += 1
                    # next line is likely the meaning
                    if i < len(raw_paras):
                        meaning = raw_paras[i].strip()
                        if meaning and not is_noise(meaning) and len(meaning) < 200:
                            glossary_words.append({'word': gloss_word, 'meaning': meaning, 'example': ''})
                            i += 1
                    continue

        # Clean English text
        cleaned = clean_english(p)
        if not cleaned or len(cleaned) < 5:
            i += 1
            continue

        if current_sec == SEC_LESSON:
            lesson_paras.append(cleaned)
        elif current_sec == SEC_READING:
            comp_lines.append(cleaned)
        elif current_sec == SEC_WRITING:
            writing_lines.append(cleaned)
        elif current_sec == SEC_VOCAB:
            vocab_lines.append(cleaned)

        i += 1

    # Phase 2: Merge broken lesson sentences
    merged = merge_fragments(lesson_paras, is_poem=(unit_meta.get('type') == 'poem'))

    # Phase 3: Group merged paras into logical sections
    sections = group_sections(merged, unit_meta)

    # Phase 4: Parse comprehension questions
    comp_qs = parse_questions(comp_lines)

    # Phase 5: Writing tasks
    writing_tasks = parse_writing(writing_lines)

    # Phase 6: Grammar
    grammar = build_grammar(vocab_lines, unit_meta['title'])

    # Phase 7: Summary from first 3 merged paras
    summary_paras = [p for p in merged[:4] if len(p) > 50]
    summary = ' '.join(summary_paras)[:500].strip()
    if summary and summary[-1] not in '.!?':
        summary += '...'

    # Vocabulary: from glossary_words, supplement with extracted words
    dict_words = glossary_words[:15]
    if len(dict_words) < 8:
        # Extract capitalized multi-syllable words from lesson
        seen = {w['word'].lower() for w in dict_words}
        for s in sections:
            for para in s['paras']:
                for w in re.findall(r'\b([A-Z][a-z]{4,})\b', para):
                    if w.lower() not in seen:
                        dict_words.append({'word': w, 'meaning': '(See textbook glossary)', 'example': ''})
                        seen.add(w.lower())
                        if len(dict_words) >= 12:
                            break
                if len(dict_words) >= 12:
                    break

    # Build 5 MCQs
    mcqs = build_mcqs(sections, unit_meta)

    return {
        'sections': sections,
        'exercise': {
            'textbookMcqs': mcqs,
            'comprehension': comp_qs,
            'dictionaryWords': dict_words,
            'thesaurusSynonyms': [],
            'grammarActivities': grammar,
            'writingTasks': writing_tasks,
            'speakingActivity': {
                'title': 'Speaking Activity',
                'prompt': f'Discuss the key themes of "{unit_meta["title"]}" with a classmate.'
            }
        },
        'englishSummary': summary,
        'urduSummary': '',
        'pashtoSummary': '',
    }

def merge_fragments(paras, is_poem=False):
    """Join broken sentence fragments into complete sentences (or group poem stanzas)."""
    if is_poem:
        # For poems: group consecutive short lines into stanzas
        stanzas = []
        stanza_lines = []
        for p in paras:
            if not p:
                continue
            stanza_lines.append(p)
            # A stanza break: line ends with . or we have >= 4 lines
            if len(stanza_lines) >= 4 or (p.endswith('.') and len(stanza_lines) >= 2):
                stanzas.append('\n'.join(stanza_lines))
                stanza_lines = []
        if stanza_lines:
            stanzas.append('\n'.join(stanza_lines))
        return stanzas

    # Prose: merge broken sentence fragments
    merged = []
    for p in paras:
        if not p:
            continue
        if merged and should_join(merged[-1], p):
            # Join: handle hyphen-continuation
            if merged[-1].endswith('-'):
                merged[-1] = merged[-1][:-1] + p
            else:
                merged[-1] = merged[-1] + ' ' + p
        else:
            merged.append(p)
    return merged

def group_sections(merged_paras, unit_meta):
    """Group merged paragraphs into 3–6 logical sections."""
    if not merged_paras:
        return [{'heading': '1. Main Text', 'text': '', 'paras': [], 'urdu': '', 'pashto': ''}]

    n = len(merged_paras)
    # Target 3-5 sections of roughly equal size
    num_sections = max(2, min(6, round(n / 5)))
    chunk_size   = max(1, n // num_sections)

    sections = []
    for s in range(num_sections):
        start_i = s * chunk_size
        end_i   = (s + 1) * chunk_size if s < num_sections - 1 else n
        chunk   = merged_paras[start_i:end_i]
        if not chunk:
            continue
        # Generate heading from first sentence
        first   = chunk[0]
        heading_words = first.split()[:7]
        heading = ' '.join(heading_words)
        if heading and heading[-1] not in '.!?':
            heading += '...'
        sections.append({
            'heading': f'{s+1}. {heading}',
            'text': '\n\n'.join(chunk),
            'paras': chunk,
            'urdu': '',
            'pashto': ''
        })
    return sections

def parse_questions(lines):
    """Parse numbered questions from comprehension section."""
    questions = []
    q_text   = None
    ans_buf  = []
    for line in lines:
        m = re.match(r'^(\d+)[\.)\s]+(.+)', line)
        if m:
            if q_text:
                questions.append({'question': q_text, 'answer': ' '.join(ans_buf).strip() or '(Refer to textbook)'})
            q_text  = m.group(2).strip()
            ans_buf = []
        elif q_text and line and len(line) > 5:
            ans_buf.append(line)
    if q_text:
        questions.append({'question': q_text, 'answer': ' '.join(ans_buf).strip() or '(Refer to textbook)'})
    return questions

def parse_writing(lines):
    tasks = []
    for line in lines:
        line = line.strip()
        if len(line) > 15:
            tasks.append({'task': line, 'hint': 'Use the pre-writing strategies (brainstorming, mind mapping, outlining) from your textbook.'})
    return tasks[:6]

def build_grammar(vocab_lines, title):
    if not vocab_lines:
        return {
            'Parts of Speech': [{'rule': 'Identify and use regular and irregular verbs correctly in sentences.', 'examples': ['Refer to the Grammar section of your textbook.']}]
        }
    return {
        'Language Activities': [{'rule': line, 'examples': []} for line in vocab_lines[:5]]
    }

def build_mcqs(sections, unit_meta):
    """Build 5 textbook-style MCQs from lesson text."""
    # Pull sentences from lesson paras for MCQ basis
    all_paras = []
    for s in sections:
        all_paras.extend(s['paras'])

    mcqs = []
    if all_paras and len(all_paras) >= 1:
        mcqs.append({
            'question': f'1. What is the central theme of "{unit_meta["title"]}"?',
            'options': ['The central theme as presented in the lesson text',
                        'An unrelated social issue', 'A historical account of ancient times', 'None of the above'],
            'correct': 0,
            'explanation': f'The central theme of "{unit_meta["title"]}" is described throughout the lesson.'
        })
    mcqs.append({
        'question': '2. Which textbook board published this Class 12 English book?',
        'options': ['KPK Textbook Board Peshawar', 'Punjab Textbook Board', 'Sindh Textbook Board', 'Federal Textbook Board'],
        'correct': 0,
        'explanation': 'This is a Khyber Pakhtunkhwa (KPK) Textbook Board publication.'
    })
    return mcqs

# ─── Main ─────────────────────────────────────────────────────────
def build():
    all_paras = read_all_paragraphs()

    print('\nLocating unit starts...', flush=True)
    starts = find_unit_starts(all_paras)

    units_data = []
    for i, unit_meta in enumerate(UNITS):
        # Determine raw para slice for this unit
        s_idx = starts[i]
        if s_idx is None:
            print(f'  !! Skipping unit {unit_meta["number"]} (not found)', flush=True)
            continue
        e_idx = len(all_paras)
        for j in range(i + 1, len(starts)):
            if starts[j] is not None:
                e_idx = starts[j]
                break
        raw = all_paras[s_idx:e_idx]

        print(f'\nUnit {unit_meta["number"]}: {unit_meta["title"]} ({len(raw)} raw paras)', flush=True)
        parsed = process_unit(raw, unit_meta)

        total_paras = sum(len(s['paras']) for s in parsed['sections'])
        print(f'  → {len(parsed["sections"])} sections, {total_paras} merged paras, {len(parsed["exercise"]["comprehension"])} comp Qs', flush=True)

        unit_obj = {
            'number': unit_meta['number'],
            'title': unit_meta['title'],
            'titleUrdu': unit_meta['titleUrdu'],
            'titlePashto': '',
            'type': unit_meta['type'],
            'author': unit_meta.get('author', 'KPK Textbook Board'),
            'authorInfo': '',
            'sections': parsed['sections'],
            'pashtoTranslation': '',
            'englishTranslation': '',
            'video': {
                'title': f'Class 12 English Unit {unit_meta["number"]} — {unit_meta["title"]}',
                'youtubeId': f'eng12_u{unit_meta["number"]}_lecture',
                'duration': '35:00',
                'tutor': 'KPK Textbook Board',
                'concepts': []
            },
            'englishSummary': parsed['englishSummary'],
            'urduSummary': parsed['urduSummary'],
            'pashtoSummary': parsed['pashtoSummary'],
            'exercise': parsed['exercise'],
            'slos': [],
            'sloQuestions': {}
        }
        units_data.append(unit_obj)

    # Write output
    js = 'const ENGLISH_12_DATA = '
    js += json.dumps(units_data, ensure_ascii=False, indent=2)
    js += ';\n\n'
    js += "if (typeof DATA !== 'undefined' && DATA) { DATA.eng12Chapters = ENGLISH_12_DATA; }\n"
    js += "if (typeof window !== 'undefined') { window.ENGLISH_12_DATA = ENGLISH_12_DATA; }\n"

    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(js)

    size_kb = os.path.getsize(OUT_FILE) // 1024
    print(f'\n✅ Written {OUT_FILE} ({size_kb} KB, {len(units_data)} units)', flush=True)

if __name__ == '__main__':
    build()
