# -*- coding: utf-8 -*-
"""Unit 10 (Technology in Everyday Life) corrections from source PDF 103-116 (printed 94-107)."""

PDF = list(range(103, 117))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.',
    'translate passages from English to Urdu: use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passage from English to Urdu; understand that most phrases and idioms do not translate literally from one language to another.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'analyze sentences for clauses and phrases.',
    'identify and differentiate between main, subordinate and relative clauses.',
    'use dictionary to: choose appropriate word definition; identify part of speech; recognize abbreviation used in a dictionary; locate antonyms in a thesaurus.',
    'demonstrate use of phrases and clauses.',
]

PRE_READING = [
    dict(q='What comes in your mind when you hear the word technology?', a='Pre-reading question (PDF 104)'),
    dict(q='When do you think technology began?', a='Pre-reading question (PDF 104)'),
    dict(q='Name a few technological things that we use in our daily life.', a='Pre-reading question (PDF 104)'),
]

GLOSSARY = [
    ('disrupt', 'to make it difficult for something to continue in the normal way', 'خلل ڈالنا', 'ګډوډول'),
    ('benefit', 'an advantage that something gives you; a helpful and useful effect that something has', 'فائدہ', 'ګټه'),
    ('drought', 'a long period of time when there is little or no rain', 'خشک سالی', 'وچکالي'),
    ('proprietors', 'the owner of a business, a hotel, etc.', 'مالکان', 'مالکان'),
    ('traits', 'a particular quality in your personality', 'خصوصیات', 'ځانګړتیاوې'),
    ('genes', 'a unit inside a cell which controls a particular quality in a living thing that has been passed on from its parents', 'جین (موروثی اکائیاں)', 'جینونه'),
    ('notch', 'a level on a scale, often marking quality or achievement', 'درجہ', 'درجه'),
    ('ailments', 'an illness that is not very serious', 'بیماریاں، عارضے', 'ناروغۍ'),
    ('bulkiness', 'large and difficult to move or carry', 'بھاری پن، ضخامت', 'درنوالی، غټوالی'),
    ('conceive', 'to form an idea, a plan, etc. in your mind; to imagine something', 'تصور کرنا', 'تصور کول'),
    ('stagnant', 'not developing, growing or changing', 'جامد، ٹھہرا ہوا', 'ولاړ، نه پرمختلونکی'),
]

NOTES = [
    'Sections 1-3 displayed invented text (digital-age essay, double-edged-sword paragraph) that is not in the book; the displayed paragraphs are replaced with the book text already stored in the "text" field, and Urdu/Pashto fields aligned with its stored translations.',
    'authorInfo described an invented lesson summary; the book prints no author name (PDF 103).',
    'Learning outcomes (PDF 103), pre-reading questions (PDF 104) and printed glossary meanings (PDF 107) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Listening & speaking prompt was empty; restored from PDF 110.',
    'Comprehension A1-7, MCQ B1-5, C, vocabulary A-B, writing A-C, phrase/clause grammar and Revision Exercises 1-13 match the book.',
]


def patch(u):
    for s in u['sections']:
        s['paras'] = [p for p in s['text'].split('\n\n') if p.strip()]
        if s.get('urduTranslation'):
            s['urdu'] = s['urduTranslation']
        if s.get('pashtoTranslation'):
            s['pashto'] = s['pashtoTranslation']
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 103).'
    u['author'] = ''
    u['exercise']['speakingActivity']['prompt'] = ("Share with the class your point of view about 'Contribution of Technology in our Daily Life'. "
                                                   'Express satisfaction/ dissatisfaction, approval/ disapproval, and agreement/ disagreement (fully and partially) politely.')
