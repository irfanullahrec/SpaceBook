# -*- coding: utf-8 -*-
"""Unit 7 (The Two Bargains) corrections from source PDF 73-83 (printed 64-74)."""
from honorific import fix

PDF = list(range(73, 84))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.',
    'analyze passages in the text to identify the theme / general subject, key idea / central thought (a statement about general subject), and supporting details.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'illustrate use of adverbs learnt earlier.',
    'recognize varying positions of adverbs in sentence according to their kind and importance.',
    'identify and use degrees of comparison of adverbs.',
    'use adverbials phrases and clauses.',
    'use dictionary to: choose appropriate word definition; identify part of speech; recognize abbreviation used in a dictionary.',
    'comprehend a text and answer questions on it.',
]

PRE_READING = [dict(q='Look at the picture and predict what the lesson is about?', a='Picture: the walled well of Bair-e-Roma (PDF 74)')]

GLOSSARY = [
    ('bitter', 'making you feel very unhappy; caused by great unhappiness', 'تلخ', 'تریخ'),
    ('broke out', 'to start suddenly', 'اچانک شروع ہوا، پھوٹ پڑا', 'ناڅاپه پیل شو'),
    ('decline', 'to say that you will not do something that somebody has asked you to do', 'انکار کرنا', 'انکار کول'),
    ('famine', 'a lack of food during a long period of time in a region', 'قحط', 'قحطي'),
    ('generosity', 'willing to give somebody money, gifts, time or kindness freely', 'سخاوت', 'سخاوت'),
    ('proclaim', 'to publicly and officially tell people about something important', 'اعلان کرنا', 'اعلانول'),
    ('scarce', 'there is not enough of it and it is only available in small quantities', 'کم یاب', 'کمیاب'),
    ('touch', 'feeling happy and grateful because of something kind that somebody has done; feeling emotional about something', 'متاثر ہونا', 'اغېزمن کېدل'),
    ('turn down', 'reject or refuse to consider an offer, a proposal, etc. or the person who makes it', 'ٹھکرانا، رد کرنا', 'ردول'),
    ('apprise', 'to tell or inform somebody of something', 'آگاہ کرنا', 'خبرول'),
    ('endowment', 'give or bequeath an income or property to a person or institution', 'وقف', 'وقف'),
]

REPL = [
    ('Arabia is a desert land where water is scarce.', 'Arabia is a desert land where water is scare.'),
    ('The Jew did not agree to sell it at first but then', 'The Jew did agree to sell it at first but then'),
]

NOTES = [
    'Empty honorific brackets in the stored text restored to the printed honorific.',
    'Two printed readings restored with this note: "water is scare" (scarce) and "The Jew did agree to sell it at first" (the sense requires "did not agree").',
    'Learning outcomes (PDF 73), pre-reading (PDF 74) and printed glossary meanings (PDF 77) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Contextual-meaning word "loaa" is printed this way (load).',
    'Listening & speaking prompt restored to the printed wording (PDF 81).',
    'Comprehension A1-9, MCQ B1-5, vocabulary A-B, writing A-D and adverb grammar A-E match the book.',
]


def _repl(o):
    if isinstance(o, str):
        for a, b in REPL:
            o = o.replace(a, b)
        return o
    if isinstance(o, list):
        return [_repl(x) for x in o]
    if isinstance(o, dict):
        return {k: _repl(v) for k, v in o.items()}
    return o


def patch(u):
    u['sections'] = _repl(fix(u['sections']))
    u['exercise'] = fix(u['exercise'])
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 73).'
    u['exercise']['speakingActivity']['prompt'] = 'Work in pairs and express your personal ideas / feelings / emotions on economic inequality in society and how can it be minimized. Share your views in front of the class.'
