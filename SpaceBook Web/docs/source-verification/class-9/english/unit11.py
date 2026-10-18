# -*- coding: utf-8 -*-
"""Unit 11 (Safety First) corrections from source PDF 117-127 (printed 108-116)."""

PDF = list(range(117, 128))  # 118-119 are duplicate scans of printed 107-108
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'analyze passages in the text to identify the theme / general subject, key idea / central thought (a statement about general subject), and supporting details.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'use dictionary to choose appropriate word definition, identify part of speech and recognize abbreviation used in a dictionary.',
    'translate passages from Urdu to English.',
    'apply rule of capitalization wherever applicable.',
    'illustrate use of punctuation marks learned earlier.',
    'recognize and rectify faulty punctuation marks in given passages and own work.',
    'recognize and use comma to separate: subordinate clause which precedes a main clause; a non-defining relatives clause; coordinate clauses joined by one of the pure conjunction.',
    'recognize and use colon to separate indefinite clauses when there is a sharp antithesis.',
    'recognize and use semi colon between: parts of a compound sentence when no conjunction is used; the clauses of a compound sentence before conjunctive adverbs.',
]

PRE_READING = [dict(q='Look at the picture and predict what the lesson is about?', a='Pictures: an injured man on the ground and a road accident (PDF 118)')]

GLOSSARY = [
    ('collapses', 'to fall down or fall in suddenly, often after breaking apart', 'گر پڑتا ہے', 'پرځېږي'),
    ('choking', 'to be unable to breathe because the passage to your lungs is blocked or you cannot get enough air; to make somebody unable to breathe', 'دم گھٹنا', 'ساه بندېدل'),
    ('thrust', 'to push something/somebody suddenly or violently in a particular direction; to move quickly and suddenly in a particular direction', 'زور سے دھکیلنا', 'په زور ټېلول'),
    ('elevate', 'to give somebody/something a higher position or rank, often more important than they deserve - raise', 'اونچا کرنا', 'لوړول'),
    ('wound', 'an injury to part of the body, especially one in which a hole is made in the skin using a weapon', 'زخم', 'ټپ'),
    ('dislodge', 'to force or knock something out of its position', 'اپنی جگہ سے ہٹانا', 'له ځایه ایستل'),
    ('emergency', 'a sudden serious and dangerous event or situation which needs immediate action to deal with it', 'ہنگامی حالت', 'بیړني حالت'),
    ('adhesive', 'a substance that you use to make things stick together', 'چپکنے والا مادہ', 'نښلوونکې ماده'),
    ('lodge', 'make or become firmly fixed or stuck in a place', 'پھنس جانا', 'نښلېدل، بندېدل'),
    ('nostrils', 'either of the two openings at the end of the nose that you breathe through', 'نتھنے', 'د پوزې سوري'),
]

NOTES = [
    'Author corrected: the book prints no author for this unit (PDF 117); the stored "Prof. Hamidullah Khan & Aamna Aamad" are the textbook authors listed in the front matter.',
    'Learning outcomes (PDF 117), pre-reading (PDF 118) and the printed glossary (PDF 121) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Dialogue text, comprehension A1-5, MCQ B1-4, vocabulary A-B, writing A-C (including the Urdu sentences for translation), speaking and punctuation grammar match the book.',
]


def patch(u):
    u['author'] = ''
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 117).'
