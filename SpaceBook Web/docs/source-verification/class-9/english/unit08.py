# -*- coding: utf-8 -*-
"""Unit 8 (Hope is the Thing with Feathers) corrections from source PDF 84-92 (printed 75-83)."""

PDF = list(range(84, 93))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'identify line and stanza.',
    'read poem and give orally or in writing: main idea; theme and its development; summary; personal response with justification; paraphrase.',
    'use paraphrasing skills to paraphrase stanzas: mark thought groups in the stanza; restate the message in simple prose; replace poetic words with simple ones.',
    'read and analyze how the poet uses language to: appeal to the senses through use of figurative language including similes and metaphors; affect meaning through use of synonyms with different connotation and denotation; create imagery.',
    'describe the object being personified.',
    'deduce meaning of difficult words from context.',
    'Illustrate use of prepositions of position, time, movement and direction.',
    'Use prepositional phrases and clauses.',
]

GLOSSARY = [
    ('abash', 'embarrassed and ashamed because of something that you have done', 'شرمندہ کرنا', 'شرمول'),
    ('crumb', 'very small piece of food, especially of bread or cake, that has fallen off a larger piece', 'ٹکڑا، ریزہ', 'ټوټه، ذره'),
    ('gale', 'an extremely strong wind', 'آندھی، تیز ہوا', 'توند باد'),
    ('perches', '(of a bird) to land and stay on a branch, etc.', 'بسیرا کرتی ہے', 'کېني، ځای نیسي'),
    ('sore', 'part of body that is painful, and often red, especially because of infection or because a muscle has been used too much', 'دکھتا ہوا، شدید', 'دردناک، سخت'),
    ('tune', 'a series of musical notes that are sung or played in a particular order to form a piece of music', 'دھن، نغمہ', 'سندره، غږ'),
    ('extremity', 'the furthest point, end or limit of something', 'انتہا', 'انتها'),
    ('strangest', 'unusual or surprising, especially in a way that is difficult to understand', 'سب سے عجیب', 'تر ټولو عجیب'),
]

ABOUT_POET = ('About the Poet: Emily Dickinson is considered as one of the most original 19th century American poet. '
              'She was born in Amherst, Massachusetts, to a family, well known for educational and political activity. '
              'Her father was a lawyer and treasurer of the local college. Her mother was a religious, hardworking housewife. '
              'Emily was educated at Amherst Academy. She lived a secluded life. Her works have been a source of much comfort to the distressed hearts. '
              'Hope is such an example. She died at the age of fifty five.')

NOTES = [
    'About the Poet restored verbatim from PDF 85 (the stored version had added dates and reworded sentences).',
    'Learning outcomes (PDF 84) added; glossary meanings replaced with the printed ones (PDF 86); Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Listening & speaking prompt was empty; restored from PDF 91.',
    'Poem, comprehension A1-7, MCQ B1-5, vocabulary A-D, writing A-B and preposition grammar A-D match the book.',
]


def patch(u):
    u['authorInfo'] = ABOUT_POET
    u['exercise']['speakingActivity']['prompt'] = "Share 'Why We Shouldn't Lose Hope.' Express your ideas in front of the class."
