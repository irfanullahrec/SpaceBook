# -*- coding: utf-8 -*-
"""Unit 15 (Abou Ben Adhem) corrections from source PDF 155-163 (printed 144-152)."""

PDF = list(range(155, 164))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'identify line and stanza.',
    'read poem and give orally or in writing: main idea; theme and its development; summary; personal response with justification; paraphrase.',
    'analyze how the poet uses language to appeal to the senses through use of figurative language including similes.',
    'recognize literary technique such as personification, metaphor and imagery.',
    'deduce meaning of difficult words from context.',
    'demonstrate use of question words.',
    'recognize the rules of and change the narration of statements, request / orders and questions.',
]

PRE_READING = [dict(q='Who was Abou Ben Adhem?', a='Pre-reading question (PDF 156)')]

GLOSSARY = [
    ('peace', 'serenity/ mental solace', 'سکون، ذہنی اطمینان', 'سکون، ذهني ارامي'),
    ('writest', 'writes/ writing', 'لکھتا ہے', 'لیکي'),
    ('thou', "a word meaning 'you', used when talking to only one person who is the subject of the verb", 'تو', 'ته'),
    ('blest', 'to ask God to protect somebody/something/ 2nd form of bless', 'برکت دی گئی', 'برکت ورکړل شوی'),
    ('vanish', 'to disappear suddenly and/or in a way that you cannot explain', 'غائب ہو جانا', 'ورکېدل'),
    ('raised', 'at a higher level than normal', 'اٹھایا ہوا، بلند', 'پورته شوی'),
    ('bloom', 'the state, time, or period when flowers open; freshly opened flower', 'کھلنا، کھلا ہوا پھول', 'غوړېدل، غوړېدلی ګل'),
]

ABOUT_POET = ('About the Poet: James Henry Leigh Hunt was born 19 October 1784 in Southgate, Middlesex and died on 28 August 1859 in London. '
              'As a writer, Hunt was a jack-of-all-trades, achieving early success as a critic, essayist, journalist, and poet, and establishing himself as an editor '
              'of influential journals in an age when the periodical was at the height of its cultural influence. "Abou Ben Adhem" is probably the best known poem of Leigh Hunt.')

NOTES = [
    'About the Poet restored verbatim from PDF 157 (the stored version had added Sufi background not in the book).',
    'Learning outcomes (PDF 155), pre-reading (PDF 156) and the printed glossary (PDF 157) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Comprehension question 5 is printed "Mentioned the other words..."; kept as stored ("Mention") with this note.',
    'Poem, comprehension A1-6, MCQ B1-5, vocabulary A-C, writing A-D, speaking, narration grammar A-B, Revision Exercises 1-8 (PDF 161-162) and About the Authors (PDF 163) match the book.',
]


def patch(u):
    u['authorInfo'] = ABOUT_POET
    u['author'] = 'J. H. Leigh Hunt'
