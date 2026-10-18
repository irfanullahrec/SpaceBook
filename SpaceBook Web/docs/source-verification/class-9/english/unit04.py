# -*- coding: utf-8 -*-
"""Unit 4 (The Daffodils) corrections from source PDF 42-49 (printed 33-40)."""

PDF = list(range(42, 50))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'identify line and stanza.',
    'read poem and give orally or in writing: main idea; theme and its development; summary; personal response with justification; paraphrase',
    'use paraphrasing skills to paraphrase stanzas: mark thought groups in the stanza; restate the message in simple prose; replace poetic words with simple ones',
    'analyze how the poet uses language to appeal to the senses through use of figurative language including similes.',
    'recognize literary technique such as personification.',
    'describe the object being personified.',
    'deduce meaning of difficult words from context.',
    'demonstrate use of question words.',
    'make and use present and past participles.',
    'illustrate use of infinitive and infinitive phrases.',
    'illustrate use of gerund and gerund phrases.',
]

PRE_READING = [
    dict(q='What is nature?', a='Pre-reading question (PDF 43)'),
    dict(q='How do you enjoy the beauty of nature?', a='Pre-reading question (PDF 43)'),
    dict(q='Would you like to visit a place of natural beauty?', a='Pre-reading question (PDF 43)'),
]

GLOSSARY = [
    ('wandered', 'to walk slowly around or to a place, often without any particular sense of purpose or direction', 'آوارہ گردی کی، بلا مقصد گھوما', 'بې موخې وګرځېد'),
    ('vales', 'valleys', 'وادیاں', 'درې'),
    ('host', 'great number or groups', 'بڑی تعداد، جھنڈ', 'ډېر شمېر، ګڼه'),
    ('fluttering', 'to move lightly and quickly; to make something move in this way', 'لہرانا، پھڑپھڑانا', 'رپېدل، ښورېدل'),
    ('stretched', 'to make something longer, wider or looser, for example by pulling it; to become longer, etc. in this way', 'پھیلا ہوا', 'غځېدلی'),
    ('margin', 'The edge ar border of something line', 'کنارہ', 'غاړه، څنډه'),
    ('sprightly', 'full of life and energy', 'چست، زندہ دل', 'چست، ژوندی'),
    ('gay', 'light-hearted and carefree / happy and cheerful', 'خوش و خرم', 'خوشحاله، بې غمه'),
    ('jocund', 'cheerful and light-hearted', 'خوش مزاج، شاداں', 'خوشحاله، زړه ور'),
    ('gazed', 'to look steadily at somebody/something for a long time, either because you are very interested or surprised, or because you are thinking of something else', 'ٹکٹکی باندھ کر دیکھا', 'په غور یې وکتل'),
    ('couch', 'a long comfortable seat for two or more people to sit on', 'صوفہ، پلنگ', 'کوچ، اوږده څوکۍ'),
    ('pensive', 'thinking deeply about something, especially because you are sad or worried', 'فکرمند، سوچ میں ڈوبا', 'په فکر کې ډوب'),
    ('vacant', 'empty; not being used', 'خالی', 'تش'),
    ('bay', 'a part of the sea, or of a large lake, partly surrounded by a wide curve of the land', 'خلیج', 'خلیج'),
    ('solitude', 'the state of being alone, especially when you find this pleasant', 'تنہائی', 'یوازیتوب'),
    ('tossing', 'to move or make somebody/something move from side to side or up and down', 'اچھالنا، جھومنا', 'ښورول، پورته ښکته کول'),
]

ABOUT_POET = ('About the Poet: William Wordsworth was born on 7 April 1770 at Cockermouth in Cambria. He was a major English poet. '
              "In 1799, Wordsworth settled at Dove Cottage in Grasmere in the Lake District. Wordsworth's well-known poem, The Daffodils was written at Dove Cottage. "
              'Wordsworth died on 23 April 1850.')

NOTES = [
    'About the Poet (PDF 44, printed 35) restored verbatim in authorInfo; the earlier invented pre-reading answers there were removed.',
    'Pre-reading questions (PDF 43) and verbatim learning outcomes (PDF 42) added.',
    'Glossary replaced with the book glossary (PDF 44): 16 words with printed meanings ("ar border", "Cambria" kept as printed); Urdu/Pashto are SpaceBook translations.',
    'Listening & speaking prompt restored to the printed wording (PDF 48).',
    'Poem text, comprehension A, MCQs B, vocabulary A-C, writing A-B and grammar A-D match the book.',
]


def patch(u):
    u['authorInfo'] = ABOUT_POET
    u['author'] = 'William Wordsworth'
    u['exercise']['speakingActivity']['prompt'] = 'Develop and practice a dialogue in group to exhibit appropriate convention of interruption.'
