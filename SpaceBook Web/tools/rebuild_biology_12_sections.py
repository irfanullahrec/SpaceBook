# -*- coding: utf-8 -*-
"""
Rebuild sections of js/biology_12_data.js from the official KPTBB DOCX source
with aggressive OCR-noise removal and paragraph re-flow.

- Drops page furniture (running headers, page numbers, watermarks, 'Chapter N')
- Drops figure/table captions and figure label clusters
- Drops KEY CONCEPTS listing blocks
- Merges line-wrapped paragraph fragments back into single paragraphs
- Splits content into numbered sections (14.1, 15.2.3 ...)
- Preserves chapter-level metadata (exercise, sloBank, summaries) from the
  existing dataset

Usage:  python rebuild_biology_12_sections.py [--dry-run]
"""
import zipfile, xml.etree.ElementTree as ET, sys, os, re, json, io, collections

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Biology\Word"
OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\biology_12_data.js"
DRY = '--dry-run' in sys.argv

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# Verified chapter start paragraph indices in the flattened DOCX paragraph stream
BOUNDARIES = [
    (14, 61), (15, 706), (16, 1398), (17, 2085), (18, 2832), (19, 3179),
    (20, 3472), (21, 3934), (22, 4336), (23, 5365), (24, 6365), (25, 6988),
    (26, 7311), (27, 8105),
]

CHAPTER_TITLES = {
    14: "Respiration", 15: "Homeostasis", 16: "Support and Movement",
    17: "Nervous Coordination", 18: "Chemical Coordination", 19: "Behaviour",
    20: "Reproduction", 21: "Development and Aging", 22: "Inheritance",
    23: "Chromosomes and DNA", 24: "Evolution", 25: "Man and His Environment",
    26: "Biotechnology", 27: "Biology and Human Welfare",
}

SIDEBAR_HEADERS = {
    'skills', 'for your information', 'tidbit', 'activity', 'think about it',
    'key points', 'making connections', 'science and society', 'science point',
    'career point', 'glossary', 'exercise', 'self assessment', 'summary',
    'useful websites for biology students', 'appendix', 'answers',
    'do you know', 'nndcat preparation',
}

TERMINAL = '.!?;”"’)'

HEAD_RE = re.compile(r'^(\d{2})\.(\d+)(\.\d+)?(\s|$|:)')
BULLET_RE = re.compile(r'^[\u25aa\u2022\u25cf\-\*\u2013\u2014]\s*')
LIST_RE = re.compile(r'^\(?([a-zA-Zivx]{1,4})\)?[\.\)]\s+\S')
STANDALONE_MARK_RE = re.compile(r'^\(?([ivx]+|[a-z])\)?[\.\)]?$')
MARKER_ONLY_RE = re.compile(r'^\(?(\d{1,2}|[ivxIVX]{1,4}|[a-z])\)?[.)]?$')
NOISE_RE = re.compile(
    r'^(MDCAT|BY FUTURE|YOUSEER|DOCTORS|AHMAD|\+\+|dd\d+|6-|V\.|Chapton)$')

# OCR errors in section headings (source text is wrong, textbook is right)
HEADING_FIXES = {
    'Reflex Are': 'Reflex Arc',
    'Influx of Nations': 'Influx of Na+ ions',
    'GENOMEIC LIBRARY': 'GENOMIC LIBRARY',
    'Types of Nerve Impulse: I.': 'Types of Nerve Impulse',
}

# OCR errors in body text (dropped leading capital)
PARA_FIXES = [
    (re.compile(r'(?<![A-Za-z])regor Mendel'), 'Gregor Mendel'),
]


def load_paragraphs():
    files = sorted(f for f in os.listdir(DOCX_DIR)
                   if f.endswith('.docx') and not f.startswith('~$'))
    paras = []
    for fn in files:
        with zipfile.ZipFile(os.path.join(DOCX_DIR, fn)) as z:
            root = ET.fromstring(z.read('word/document.xml'))
        for p in root.iter(NS + 'p'):
            t = ''.join(x.text for x in p.iter(NS + 't') if x.text).strip()
            if t:
                paras.append(re.sub(r'\s+', ' ', t))
    return paras


def is_furniture(line, chnum, title):
    low = line.lower()
    if 'inqilab' in low or 'camscanner' in low:
        return True
    if re.fullmatch(r'chapter\s+\d{1,2}', low):
        return True
    if re.fullmatch(r'\d{1,4}', line):
        return True
    if low == title.lower() or line.upper() in ('UNIT', 'KEY CONCEPTS'):
        return True
    if low.rstrip('?:.! ') in SIDEBAR_HEADERS:
        return True
    if NOISE_RE.match(line):
        return True
    return False


def strip_chapter_header(line):
    """'Chapter 15 nimals have ...' -> 'nimals have ...'"""
    return re.sub(r'^Chapter\s+\d{1,2}\s*', '', line).strip()


CAP_MARKER = re.compile(r'(?:Fig|Figure|Table|Hig)\s*:?\s*\d+\s*\.?\s*\d*\.?')


def is_caption(line):
    return bool(CAP_MARKER.match(line))


def strip_caption(line):
    """Remove 'Fig/Table: x.y ...' caption text while keeping real prose."""
    if CAP_MARKER.match(line):
        m = CAP_MARKER.match(line)
        rest = line[m.end():].strip()
        # drop a short leading caption sentence, keep what follows
        sm = re.match(r'^(.{0,140}?[.!?])\s+([A-Z(].*)$', rest)
        if sm and len(sm.group(1).split()) <= 14:
            rest = sm.group(2)
        return rest
    out = line
    while True:
        m = CAP_MARKER.search(out)
        if not m:
            break
        tail = out[m.start():]
        sm = re.match(r'^.{0,140}?[.!?]\s+', tail)
        if sm and len(tail[:sm.end()].split()) <= 20:
            out = out[:m.start()] + tail[sm.end():]
        else:
            out = out[:m.start()]
            break
    return out.strip()


def is_sidebar(line):
    return line.lower().strip(':').rstrip('.') in SIDEBAR_HEADERS


def is_prose(ln):
    """Long body-text line (not a numbered heading, not a caption)."""
    return len(ln) > 60 and not HEAD_RE.match(ln) and not CAP_MARKER.match(ln)


def drop_key_concepts(lines, chnum):
    out, i = [], 0
    n = len(lines)
    while i < n:
        if lines[i].lower().rstrip(':') == 'key concepts':
            start = i + 1
            i = start
            stopped = False
            while i < n:
                ln = lines[i]
                nxt = lines[i + 1] if i + 1 < n else ''
                m = re.match(r'^(\d{1,2})\.(\d{1,3})', ln)
                # real section heading whose body follows
                if m and int(m.group(1)) == chnum and is_prose(nxt):
                    stopped = True
                    break
                # chapter intro / body text begins
                if is_prose(ln):
                    stopped = True
                    break
                i += 1
            if not stopped:      # safety: keep the tail instead of losing it
                out.extend(lines[start:])
                return out
            continue             # skip the key-concepts list + page furniture
        out.append(lines[i])
        i += 1
    return out


def repair_letters(lines):
    """Re-attach drop-cap single letters to the line that lost them."""
    out = []
    for ln in lines:
        if re.fullmatch(r'[A-Z]', ln):
            out.append(ln)
            continue
        if out and re.fullmatch(r'[A-Z]', out[-1]):
            if ln and ln[0].islower():
                out[-1] = out[-1] + ln
                continue
            if ln.startswith(("'", '"')):
                out[-1] = out[-1] + ln.lstrip("'\"")
                continue
            out.pop()               # orphan letter -> drop
        out.append(ln)
    return out


def drop_clusters(lines, report):
    """Remove runs of >=3 short, unpunctuated lines (figure/table labels)."""
    keep, n = [], len(lines)
    i = 0
    while i < n:
        ln = lines[i]
        def label_like(x):
            if '\x00' in x:
                return False            # text recovered from a caption line
            if len(x) > 48:
                return False
            if x.rstrip()[-1:] in TERMINAL or x.rstrip().endswith(':'):
                return False
            if BULLET_RE.match(x) or LIST_RE.match(x) or HEAD_RE.match(x):
                return False
            if is_sidebar(x) or is_caption(x):
                return False
            if re.search(r'[.!?;]$', x):
                return False
            return True
        if label_like(ln):
            j = i
            while j < n and label_like(lines[j]):
                j += 1
            run = lines[i:j]
            if len(run) >= 3:
                report.extend(run)
                i = j
                continue
            keep.extend(run)
            i = j
            continue
        keep.append(ln)
        i += 1
    return keep


def merge_fragments(lines, report):
    out = []
    for ln in lines:
        if not ln:
            continue
        if out:
            prev = out[-1]
            new_para = False
            if is_sidebar(prev) or is_sidebar(ln) or HEAD_RE.match(ln) \
               or HEAD_RE.match(prev) or is_caption(ln) or is_caption(prev):
                new_para = True
            elif prev.isupper() and len(prev) < 60:
                new_para = True        # ALL-CAPS heading continuation
            elif BULLET_RE.match(ln) and not prev.rstrip().endswith(':'):
                new_para = True
            elif LIST_RE.match(ln) and len(ln) > 12 and \
                    not prev.rstrip().endswith(':'):
                new_para = True
            elif prev.rstrip()[-1:] in TERMINAL:
                new_para = True
            if not new_para:
                if prev.rstrip()[-1:] in '([-' or ln[0].islower():
                    out[-1] = prev.rstrip() + ' ' + ln
                else:
                    out[-1] = prev.rstrip() + ' ' + ln
                report.append('merged')
                continue
        out.append(ln)
    return out


EMBED_HEAD_RE = re.compile(
    r'(?:^|(?<=[.!?]\s))(\d{1,2}\.\d{1,3}(?:\.\d{1,3})?\s+[A-Z][^.!?]{2,70}:)')


def split_heading_line(ln, chnum):
    """Split 'NN.M Title: <body> <NN.M Title>: ...' glued OCR lines."""
    c = ln.find(':')
    if c <= 0 or len(ln) - c - 1 < 40:
        return ln, []
    head = ln[:c + 1]
    rest = ln[c + 1:].strip()
    if not rest:
        return ln, []
    em = EMBED_HEAD_RE.search(rest)
    if em:
        body = rest[:em.start()].strip()
        tail = rest[em.start():].strip()
        parts = ([body] if body else []) + [tail]
        return head, parts
    return head, [rest]


def split_trailing_heading(ln, chnum):
    """Split '...sentence. NN.M Title: <body of next section>' lines."""
    em = EMBED_HEAD_RE.search(ln)
    if not em:
        return None
    m = HEAD_RE.match(em.group(1))
    if not m or int(m.group(1)) not in range(14, 28):
        return None
    before = ln[:em.start()].strip()
    if len(before) < 15:
        return None
    return [before, ln[em.start():].strip()]


def build_sections(lines, chnum):
    """Split cleaned chapter lines into numbered sections."""
    sections = []
    current = None
    heading_buf = None
    pending = collections.deque(lines)

    def flush():
        nonlocal current
        if current and current['paras']:
            current['text'] = '\n\n'.join(current['paras'])
            sections.append(current)
        current = None

    while pending:
        ln = pending.popleft()
        if not ln:
            continue
        m = HEAD_RE.match(ln)
        if m:
            head, parts = split_heading_line(ln, chnum)
            mh = HEAD_RE.match(head)
            title = head
            if int(mh.group(1)) != chnum:
                title = f"{chnum}.{mh.group(2)}" + \
                    (f".{mh.group(3).lstrip('.')}" if mh.group(3) else '') + \
                    head[mh.end(3) if mh.group(3) else mh.end(2):]
            for bad, good in HEADING_FIXES.items():
                if bad in title:
                    title = title.replace(bad, good)
            if not re.sub(r'^\d+(\.\d+)*\s*', '', title).strip():
                continue    # bare TOC number (e.g. '23.1'), not a real heading
            flush()
            current = {
                'heading': title,
                'paras': [],
                'text': '',
            }
            heading_buf = title
            for p in reversed(parts):
                pending.appendleft(p)
            continue
        if heading_buf is not None and current is not None:
            # ALL-CAPS continuation of a split heading
            if ln.isupper() and len(ln) < 60 and not HEAD_RE.match(ln) \
                    and len(current['heading']) + len(ln) < 110:
                current['heading'] = (current['heading'] + ' ' + ln).strip()
                heading_buf = None
                continue
            heading_buf = None
        if current is None:
            if ln.isupper() and len(ln) < 30:
                continue        # unit-opener label (e.g. 'CHROMOSOME' / 'AND DNA')
            current = {'heading': f'{chnum}.0 Introduction', 'paras': [],
                       'text': ''}
        split = split_trailing_heading(ln, chnum)
        if split:
            for p in reversed(split):
                pending.appendleft(p)
            continue
        for rx, rep in PARA_FIXES:
            ln = rx.sub(rep, ln)
        current['paras'].append(ln)

    # heading continuation for last section
    flush()
    # absorb trailing ALL-CAPS lines that were captured as paras
    kept = []
    for s in sections:
        while s['paras'] and s['paras'][0].isupper() \
                and len(s['paras'][0]) < 60 \
                and len(s['heading']) + len(s['paras'][0]) < 110:
            s['heading'] = (s['heading'] + ' ' + s['paras'].pop(0)).strip()
        # strip label junk glued onto a colon heading
        m = re.match(r'^(.*?:)\s+(.*)$', s['heading'])
        if m:
            tail = m.group(2)
            junk = (not re.search(r'[a-z]', tail)
                    and (len(tail.split()) >= 6
                         or re.fullmatch(r'[A-Z]\.?\s?[A-Z]\.?|[A-Z]{1,3}[;,)]*',
                                         tail.strip())))
            if junk:
                s['heading'] = m.group(1)
        if not s['paras']:
            continue
        s['text'] = '\n\n'.join(s['paras'])
        kept.append(s)
    return kept


def main():
    paras = load_paragraphs()
    print(f'Loaded {len(paras)} source paragraphs')

    chapters_new = {}
    dropped = []
    for idx, (chnum, start) in enumerate(BOUNDARIES):
        end = BOUNDARIES[idx + 1][1] if idx + 1 < len(BOUNDARIES) else len(paras)
        title = CHAPTER_TITLES[chnum]
        raw_lines = [strip_chapter_header(r) for r in paras[start:end]]
        raw_lines = drop_key_concepts(raw_lines, chnum)
        lines = []
        for ln in raw_lines:
            if is_furniture(ln, chnum, title):
                continue
            if CAP_MARKER.search(ln):
                kept = strip_caption(ln)
                dropped.append(ln)
                if len(kept.split()) >= 6:
                    ln = kept + '\x00'      # prose recovered from caption line
                elif kept.strip():
                    lines.append(kept)      # short label -> cluster rule decides
                continue
            lines.append(ln)

        lines = repair_letters(lines)
        lines = drop_clusters(lines, dropped)
        lines = [x.replace('\x00', '') for x in lines]
        merge_log = []
        lines = merge_fragments(lines, merge_log)
        # orphaned list markers (1. / i. / a)) - dropped after clustering and
        # merging so they cannot extend label clusters or split paragraphs
        lines = [ln for ln in lines if not MARKER_ONLY_RE.match(ln)]

        sections = build_sections(lines, chnum)
        chapters_new[chnum] = sections
        nparas = sum(len(s['paras']) for s in sections)
        print(f'  ch{chnum:>2} {title:<26} sections={len(sections):>3} '
              f'paragraphs={nparas:>4} merges={len(merge_log)}')

    print(f'Dropped {len(dropped)} caption/label lines')
    # sanity: residual noise
    bad = 0
    for ch, secs in chapters_new.items():
        for s in secs:
            for p in s['paras']:
                if re.search(r'(?i)inqilab|^chapter \d+$|^fig\s*:', p) or \
                        re.fullmatch(r'\d{1,4}', p):
                    bad += 1
                    if bad < 15:
                        print('   RESIDUAL:', repr(p[:90]))
    print(f'Residual noise paragraphs: {bad}')

    # show dropped samples for review
    print('\n--- sample of dropped lines (40 of %d) ---' % len(dropped))
    for d in dropped[:40]:
        print('   ', repr(d[:80]))

    if DRY:
        return

    # ---- merge into existing dataset (keep chapter metadata) ----
    with io.open(OUT_JS, encoding='utf-8') as f:
        src = f.read()
    data = json.loads(src[src.index('['):src.rindex(']') + 1])

    for ch in data:
        n = ch['number']
        secs = chapters_new.get(n, [])
        ch['sections'] = [{
            'heading': s['heading'],
            'title': s['heading'],
            'headingUrdu': '',
            'headingPashto': '',
            'urduTitle': '',
            'text': s['text'],
            'paras': s['paras'],
            'urdu': '',
            'pashto': '',
        } for s in secs]
        ch.setdefault('id', f"cls12-bio-ch{n:02d}")
        ch['titlePashto'] = ch.get('titlePashto') or ''

    header = ("// Complete Class 12 Biology Textbook Dataset (KPTBB)\n"
              "// Extracted verbatim from official textbook DOCX, OCR noise cleaned\n"
              "const BIOLOGY_12_DATA = ")
    footer = (";\n\nif (typeof DATA !== 'undefined' && DATA) { DATA.bio12Chapters"
              " = BIOLOGY_12_DATA; }\n"
              "if (typeof window !== 'undefined') { window.BIOLOGY_12_DATA = "
              "BIOLOGY_12_DATA; }\n")
    with io.open(OUT_JS, 'w', encoding='utf-8') as f:
        f.write(header)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(footer)
    print(f'\nWrote {OUT_JS} ({os.path.getsize(OUT_JS):,} bytes)')


if __name__ == '__main__':
    main()
