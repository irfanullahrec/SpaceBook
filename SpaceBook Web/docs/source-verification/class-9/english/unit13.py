# -*- coding: utf-8 -*-
"""Unit 13 (Letter to the Newspaper Editor) corrections from source PDF 134-144 (printed 123-133)."""

PDF = list(range(134, 145))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'write and revise formal letters to people in extended social and academic environment for various purposes. Write the address on the envelope clearly and in proper format.',
    'write and revise application to people in extended environment using correct format, layout and tone.',
    'analyze letters to editor to recognize effective ways of explaining and presenting an idea, a point or an opinion.',
    'write and revise letters to editor expressing ideas, points or opinions by supporting it with anecdotes, quotations, examples, analogies etc.',
    'analyze and compare various informal and formal emails to note differences of conventions, vocabulary, style and tone.',
    'write informal and formal e-mail in extended social and academic environment.',
    'recognize and use quotation marks to enclose: both parts of an interrupted quotation; usual or peculiar terms to which attention is directed to make the meaning clear.',
    'recognize and use hyphen to indicate the division of a word at the end of the line.',
    'recognize and use dash as a separator to indicate that a sentence has been broken off, or to indicate a new direction of thought.',
    'express agreement (fully and partially) politely.',
]

PRE_READING = [dict(q='Letter Writing: Letter can be formal or informal. There is a specific format for formal letter. The formal letters are written for various purposes: to ask for information; to offer thanks, congratulations or condolences; to ask advice or express a view; to give reference.',
                    a='Format of a Formal Letter: Your address · Date · Recipient\'s address · Dear (Greetings) · Your letter · Yours (Closing farewell) (PDF 135)')]

GLOSSARY = [
    ('actualities', 'the state of something existing in reality', 'حقائق', 'حقیقتونه'),
    ('influence', 'the effect that somebody/something has on the way a person thinks or behaves or on the way that something works or develops', 'اثر و رسوخ', 'اغېز'),
    ('distortion', 'a change in the shape, appearance or sound of something so that it is strange or not clear', 'بگاڑ، تحریف', 'تحریف، کږوالی'),
    ('tender', 'an offer to carry out work, supply goods, or buy land, shares, or another asset at a stated fixed price', 'ٹینڈر، بولی', 'ټنډر، داوطلبي'),
    ('epidemic', '(of something bad) occurring more and more frequently in a particular place', 'وبا', 'وبا'),
    ('sectarian', 'connected with the differences that exist between groups of people who have different religious views', 'فرقہ وارانہ', 'فرقه یي'),
    ('communal', 'shared by, or for the use of, a number of people, especially people who live together', 'اجتماعی، گروہی', 'ګډ، ټولنیز'),
    ('divisive', 'causing people to be split into groups that disagree with or oppose each other', 'تفرقہ انگیز', 'وېشونکی'),
    ('esteemed', 'great respect and admiration; a good opinion of somebody', 'معزز، قابلِ احترام', 'درناوی لرونکی'),
    ('overseer', 'a person whose job is to make sure that other workers do their work', 'نگران', 'څارونکی'),
]

NOTES = [
    'Author corrected: the letter is signed by Abrar Khan and the book prints no unit author (PDF 134, 138); the stored names are the textbook authors from the front matter.',
    'Learning outcomes (PDF 134), the pre-reading formal-letter format (PDF 135) and the printed glossary (PDF 138) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Letter text, comprehension A1-6, vocabulary A-B, writing (application model, email table, exercises A-D), speaking dialogue and punctuation grammar match the book.',
]


def patch(u):
    u['author'] = ''
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 134). The letter is signed "Abrar Khan".'
