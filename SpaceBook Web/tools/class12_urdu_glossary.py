"""Shared helper for the Urdu XII glossary (فرہنگ, printed p.246 →): one table per lesson heading.

Each entry is (urdu_word, urdu_meaning, english_gloss, pashto_gloss). The Urdu columns are transcribed
from the page; EN/PS give an aligned translation of the board-written meaning.
"""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
UNIT = 34
UT = ('Glossary (Farhang)', 'فرہنگ', 'وییپانګه (فرهنګ)')
H = (['Word', 'Meaning'], ['الفاظ', 'معانی'], ['کلمه', 'مانا'])


def page(pdf, printed, sections, rid=None, first=False, issues=None, complete=False, note=None):
    b = Builder()
    if first:
        b.h('Glossary', 'فرہنگ', 'وییپانګه')
    for n, (en_head, ur_head, ps_head, rows) in enumerate(sections, 1):
        b.h(en_head, ur_head, ps_head)
        tid = f'urdu12-gl-{pdf}-{n}'
        b.table(tid, H[0], [[w, e] for w, m, e, p in rows],
                H[1], H[2], [[w, m] for w, m, e, p in rows], [[w, p] for w, m, e, p in rows])
    rec = BOOK.record(b, rid or f'urdu12-glossary-{pdf}', f'Glossary (PDF {pdf})', f'فرہنگ ({pdf})', f'وییپانګه ({pdf})', pdf, printed,
                      unit_title=UT if first else None)
    if first:
        rec['sourceCoverIllustrationReview'] = 'Open-book icon beside the “فرہنگ” banner and the decorative book-spine borders are not reproduced.'
    if note:
        rec['sourceNote'] = note
    BOOK.save(pdf, [(UNIT, rec)], issues=issues or [], complete_units=[UNIT] if complete else None)
