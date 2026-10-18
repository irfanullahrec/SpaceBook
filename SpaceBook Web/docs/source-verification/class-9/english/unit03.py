# -*- coding: utf-8 -*-
"""Unit 3 corrections from source PDF 33-41 (printed 24-32)."""

PDF = list(range(33, 42))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.',
    'analyze passages in the text to identify the theme / general subject, key idea / central thought (a statement about general subject), and supporting details.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'apply rules for use of articles (a / an / the) wherever applicable in speech and writing.',
    'illustrate use and functions of all modal verbs.',
    'illustrate use of regular and irregular verbs in speech and writing.',
    'illustrate use of transitive and intransitive verbs.',
    'use dictionary to: choose appropriate word definition; identify part of speech; locate synonyms in a thesaurus.',
    'translate passages from English to Urdu: use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passage from English to Urdu; understand that most phrases and idioms do not translate literally from one language to another.',
]

PRE_READING = [
    dict(q='Who do you think a leader is?', a='Pre-reading question (PDF 34)'),
    dict(q='Why do you think Quaid-e-Azam is a great leader?', a='Pre-reading question (PDF 34)'),
]

GLOSSARY = [
    ('dignified', 'calm and serious and deserving respect', 'باوقار', 'باوقاره'),
    ('empire', 'a group of countries or states that are controlled by one ruler or government', 'سلطنت', 'امپراتوري، سلطنت'),
    ('stern', 'serious and often disapproving; expecting somebody to obey you', 'سخت گیر، سنجیدہ', 'سخت، جدي'),
    ('stretched', 'being longer', 'پھیلا ہوا', 'غځېدلی'),
    ('slogan', "a word or phrase that is easy to remember, used for example by a political party or in advertising to attract people's attention or to suggest an idea quickly", 'نعرہ', 'شعار'),
    ('vast', 'extremely large in area, size, amount, etc.', 'وسیع', 'پراخ'),
    ('cheering', 'loud shouting that shows support, praise or encouragement for somebody', 'خوشی کے نعرے، داد', 'د خوښۍ چیغې، هرکلی'),
    ('foreign', 'in or from a country that is not your own', 'غیر ملکی', 'بهرنی'),
    ('leadership', 'the state or position of being a person who leads a group of people, especially the head of a country, an organization, etc.', 'قیادت', 'مشري'),
    ('homeless', 'people who have no home', 'بے گھر', 'بې کوره'),
    ('excitement', 'a feeling of great enthusiasm and eagerness', 'جوش و خروش', 'جوش او لېوالتیا'),
    ('refuge', 'the state of being safe or sheltered', 'پناہ', 'پناه'),
    ('violence', 'behaviour involving physical force intended to hurt, damage', 'تشدد', 'تاوتریخوالی'),
    ('determination', 'firmness of purpose.', 'عزم، پختہ ارادہ', 'هوډ، ټینګ اراده'),
]

NOTES = [
    'Pre-reading questions (PDF 34) and verbatim learning outcomes (PDF 33) added; the earlier invented pre-reading text in authorInfo was replaced.',
    'Glossary (PDF 36, printed 27) added: 14 words with book meanings; Urdu/Pashto meanings are SpaceBook translations.',
    'Opening date restored to "August 7th, 1947" as printed (PDF 34).',
    'MCQ 2 and 3 options restored to the printed wording (PDF 37).',
    'Comprehension, phrases, vocabulary, antonyms, grammar (articles, modals, regular verbs, transitive/intransitive), writing G-J and role play match the book.',
]


def _fix(o):
    if isinstance(o, str):
        return o.replace('It was August 7, 1947, when', 'It was August 7th, 1947, when')
    if isinstance(o, list):
        return [_fix(x) for x in o]
    if isinstance(o, dict):
        return {k: _fix(v) for k, v in o.items()}
    return o


def patch(u):
    u['sections'] = _fix(u['sections'])
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 33).'
    mc = u['exercise']['textbookMcqs']
    mc[1]['options'] = ['an angry voice', 'a long, deep voice', 'an irritated voice', 'an annoyed voice']
    mc[2]['options'] = ['newly developed country', 'undeveloped country', 'not fully formed country', 'an advanced country']
