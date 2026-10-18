# -*- coding: utf-8 -*-
"""Unit 9 (The Fantastic Shoemaker) corrections from source PDF 93-102 (printed 84-93)."""

PDF = list(range(93, 103))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'read text to make predictions about story knowledge line / content, characters, using contextual clues and prior knowledge.',
    'analyze story elements: characters, events, setting, plot, theme, tone, point of view.',
    "recognize the author's purpose and point of view.",
    'classify use convert and make declarative (affirmative and negative), interrogative, exclamatory and imperative sentences.',
    'identify and differentiate between simple, compound and complex sentences.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'use dictionary to: choose appropriate word definition; identify part of speech; recognize abbreviation used in a dictionary; locate synonyms in a thesaurus; translate passages from English to Urdu.',
    'identify the speaker or narrator in a selection.',
    'analyze to use in their own writing features of an expository composition showing comparison and contrast between things, events, situations, places, action, idea or a problem.',
    'select and use appropriate expression for various functions to ask and express preferences, emotions, wishes needs and requirements by giving reasons.',
]

PRE_READING = [
    dict(q='What are the things that you should keep in mind before buying shoes?', a='Pre-reading question (PDF 94)'),
    dict(q='What kind of shoes do you like?', a='Pre-reading question (PDF 94)'),
    dict(q='Where do you buy your shoes from?', a='Pre-reading question (PDF 94)'),
]

GLOSSARY = [
    ('crisp', 'fresh and clean; new and slightly stiff without any folds in it', 'کرارا، دو ٹوک', 'کلک، لنډ او روښانه'),
    ('grave', 'a dignified seriousness due to heavy responsibilities or cares', 'سنجیدہ، سنگین', 'جدي'),
    ('contempt', 'the feeling that somebody/something is without value and deserves no respect at all', 'حقارت', 'کرکه، سپکاوی'),
    ('bitterly', 'a way that shows feelings of sadness or anger', 'تلخی سے', 'په ترخه توګه'),
    ('dictations', 'the act of speaking or reading so that somebody can write down the words', 'املا، حکم', 'املا، امر'),
    ('irrational', 'not based on, or not using, clear logical thought', 'غیر منطقی', 'غیر منطقي'),
    ('starvation', 'the state of suffering and death caused by having no food', 'فاقہ کشی', 'لوږه'),
    ('tinkling', 'a light high ringing sound', 'جھنکار', 'شرنګ'),
    ('brooded', 'to think a lot about something that makes you annoyed, anxious or upset', 'غمگین، فکرمند', 'خپه، په فکر کې ډوب'),
    ('brisk', 'showing a desire to get things done quickly', 'تیز، چست', 'چټک'),
    ('nod', 'to move your head up and down to show agreement, understanding, etc.', 'سر ہلانا', 'سر ښورول'),
    ('wriggle', 'twist and turn with quick movements', 'بل کھانا', 'تاوېدل'),
    ('serpentine', 'like a serpent or snake', 'سانپ کی طرح بل کھاتا', 'د مار په څېر کوږ وږ'),
    ('impression', 'an idea, a feeling or an opinion that you get about somebody/something, or that somebody/something gives you', 'تاثر', 'اغېز، تاثر'),
    ('craftsman', 'a skilled person, especially one who makes beautiful things by hand', 'کاریگر، دستکار', 'لاسي کسبګر'),
    ('overused', 'to use something too much or too often', 'ضرورت سے زیادہ استعمال شدہ', 'ډېر کارول شوی'),
    ('mysterious', 'difficult to understand or explain; strange', 'پراسرار', 'پراسرار'),
    ('hesitant', 'slow to speak or act because you feel uncertain, embarrassed or unwilling', 'ہچکچاتا ہوا', 'زړه نا زړه'),
    ('mallet', 'a hammer with a large wooden head', 'لکڑی کا ہتھوڑا، موگری', 'لرګین څټک'),
    ('awl', 'a small pointed tool used for making holes, especially in leather', 'سوا (چمڑے میں سوراخ کا آلہ)', 'سوژن، د څرمنې سوري کوونکی'),
    ('anvil', 'an iron block on which a blacksmith puts hot pieces of metal before shaping them with a hammer', 'نہائی، سندان', 'سندان'),
    ('barren', 'not good enough for plants to grow on it', 'بنجر', 'شاړ'),
]

NOTES = [
    'Sections 1-3 displayed invented text (partly adapted from Galsworthy\'s "Quality", including dialect lines such as "Id shouldn\'d \'ave greaked"); the displayed paragraphs are replaced with the book text already stored in the "text" field, and the Urdu/Pashto fields are aligned with the stored translations of that text.',
    'Learning outcomes (PDF 93), pre-reading questions (PDF 94) and printed glossary meanings (PDF 97) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Listening & speaking prompt was empty; restored from PDF 100.',
    'Story text, comprehension A1-10, MCQ B1-4, vocabulary A-C, writing A-C and sentence-structure grammar match the book.',
]


def patch(u):
    for s in u['sections']:
        s['paras'] = [p for p in s['text'].split('\n\n') if p.strip()]
        if s.get('urduTranslation'):
            s['urdu'] = s['urduTranslation']
        if s.get('pashtoTranslation'):
            s['pashto'] = s['pashtoTranslation']
    u['exercise']['speakingActivity']['prompt'] = ("Share with the class your point of view about 'Contribution of Labourers'. "
                                                   'Ask and express preferences, emotions, wishes, needs and requirements by giving reasons.')
