# -*- coding: utf-8 -*-
"""Unit 6 (Nasiruddin) corrections from source PDF 64-72 (printed 55-63)."""

PDF = list(range(64, 73))
LAB = 'SpaceBook answer (the textbook prints no answers): '
PRACTICE = '[SpaceBook practice question — not in the textbook] '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'read a text to: make connections between their own lives and the characters, events, motives and causes of conflict in texts; make inferences and draw conclusion about character using supportive evidence from the text; compare characters in the literary selection to near similar ones in real life.',
    'classify adjectives into different types.',
    'change and use degrees of adjectives.',
    'follow orders of adjective in sentences.',
    'form adjective from nouns and verbs.',
    'translate passages from English to Urdu: use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passage from English to Urdu; understand that most phrases and idioms do not translate literally from one language to another.',
]

PRE_READING = [
    dict(q='Do you like humorous stories?', a='Pre-reading question (PDF 65)'),
    dict(q='Have you ever heard about Nasiruddin?', a='Pre-reading question (PDF 65)'),
]

GLOSSARY = [
    ('pomp', 'the impressive clothes, decorations, music, etc. and traditional customs that are part of an official occasion or ceremony', 'شان و شوکت', 'شان او شوکت'),
    ('claim', 'to say that something is true although it has not been proved and other people may not believe it', 'دعویٰ کرنا', 'ادعا کول'),
    ('anecdote', 'a short, interesting or amusing story about a real person or event', 'حکایت، لطیفہ', 'حکایت، کیسه'),
    ('merchant', 'a person who buys and sells goods in large quantities, especially one who imports and exports goods', 'سوداگر، تاجر', 'سوداګر'),
    ('cloak', 'a type of coat that has no sleeves, fastens at the neck and hangs loosely from the shoulders, worn especially in the past', 'چغہ، لبادہ', 'چپن، څادر ډوله کوټ'),
    ('worn out', 'badly damaged and/or no longer useful because it has been used a lot', 'پرانا، بوسیدہ', 'زوړ، شلېدلی'),
    ('furious', 'very angry', 'سخت غصے میں', 'ډېر په غوسه'),
    ('turban', 'a long piece of cloth wound tightly around the head, worn, for example, by Muslim or Sikh men', 'پگڑی، عمامہ', 'پټکی'),
    ('ornament', 'an object that is used as decoration in a room, garden/yard, etc. rather than for a particular purpose', 'زیور، آرائشی چیز', 'ګاڼه، د سینګار توکی'),
    ('ransacking', 'to make a place untidy, causing damage, because you are looking for something', 'تلاشی میں تہس نہس کرنا', 'لټول او ګډوډول'),
    ('fright', 'a feeling of fear', 'خوف، ڈر', 'وېره'),
    ('gallop', 'to move very fast and each step includes a stage when all four feet are off the ground together', 'سرپٹ دوڑنا', 'په ټوپ منډه وهل'),
    ('blown', 'to be moved by the wind', 'ہوا سے اڑایا گیا', 'د باد په واسطه وړل شوی'),
    ('uproot', 'to pull a tree, plant, etc. out of the ground', 'جڑ سے اکھاڑنا', 'له ریښې ایستل'),
    ('interrupt', 'to say or do something that makes somebody stop what they are saying or doing', 'بات کاٹنا، روکنا', 'خبره پرې کول'),
    ('bray', 'loud unpleasant sound of a donkey', 'گدھے کی آواز، ڈھینچوں', 'د خره هڼا'),
    ('preference', 'a greater interest in or desire for somebody/something than somebody/something else', 'ترجیح', 'غوره والی'),
]

NOTES = [
    'The textbook prints no multiple-choice questions for Unit 6; the five stored MCQs are now labelled as SpaceBook practice questions.',
    'Learning outcomes (PDF 64) and pre-reading questions (PDF 65) added; invented pre-reading answers removed from authorInfo.',
    'Glossary replaced with printed meanings (PDF 68); Urdu/Pashto are SpaceBook translations.',
    'Listening & speaking prompt restored to the printed wording (PDF 70).',
    'Reading text (ten anecdotes), comprehension, vocabulary A-B, writing A-B and grammar A-G match the book.',
]


def patch(u):
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 64).'
    for m in u['exercise']['textbookMcqs']:
        if not m['question'].startswith(PRACTICE):
            m['question'] = PRACTICE + m['question']
        m['origin'] = 'SpaceBook practice'
    u['exercise']['speakingActivity']['prompt'] = 'Role play: In a group of two carry out an interview in which the interviewer asks questions about the lesson from reviewer.'
