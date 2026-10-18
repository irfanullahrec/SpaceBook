# -*- coding: utf-8 -*-
"""Unit 5 (The Madina Charter) corrections from source PDF 50-63 (printed 41-54)."""

PDF = list(range(50, 64))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.',
    'analyze passages in the text to identify the theme / general subject, key idea / central thought (a statement about the general subject), and supporting details.',
    'identify, change the form of, and use present and past perfect continuous tenses.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'identify: cataphoric and anaphoric references in a given passage; transitive and intransitive verbs in a given passage; tense of the passage.',
]

PRE_READING = [
    dict(q='Look at the mind map below to predict the content of the lesson.',
         a='Mind map: Peaceful Co-existance — Freedom and safety · Religious harmony · Love and peace · Patience and tolerance · Humanity and justice'),
]

GLOSSARY = [
    ('abolish', 'to officially end a law, a system or an institution', 'منسوخ کرنا، ختم کرنا', 'لغوه کول، پای ته رسول'),
    ('abandon', 'to leave somebody, especially somebody you are responsible for, with no intention of returning', 'چھوڑ دینا', 'پرېښودل'),
    ('charter', 'a written statement describing the rights that a particular group of people should have', 'منشور', 'منشور'),
    ('community', 'all the people who live in a particular area, country, etc. when talked about as a group', 'برادری، معاشرہ', 'ټولنه'),
    ('converts', 'to change or make somebody change their religion or beliefs', 'نو مسلم، مذہب بدلنے والے', 'نوي مسلمانان، دین بدلوونکي'),
    ('harmony', 'a state of peaceful existence and agreement', 'ہم آہنگی', 'همغږي'),
    ('inhabited', 'with people or animals living there', 'آباد', 'اباد، مېشت'),
    ('kith and kin', 'friends and relatives', 'عزیز و اقارب', 'خپلوان او دوستان'),
    ('liability', 'the state of being legally responsible for something', 'ذمہ داری', 'مسؤلیت'),
    ('migrated', 'to move from one part of the world to another', 'ہجرت کی', 'هجرت یې وکړ'),
    ('thick and thin', 'even when there are problems or difficulties', 'ہر حال میں، اچھے برے وقت میں', 'په ښه او بد وخت کې'),
    ('signatory', 'a person, a country or an organization that has signed an official agreement', 'دستخط کنندہ', 'لاسلیک کوونکی'),
]

NOTES = [
    'Learning outcomes (PDF 50) and pre-reading mind map (PDF 51, "Co-existance" as printed) added.',
    'Glossary meanings replaced with the printed meanings (PDF 54); Urdu/Pashto are SpaceBook translations; the SpaceBook example sentences were dropped from the book glossary.',
    'Revision Exercise 14 box prints "steel" (for steal); kept as printed with a note.',
    'UDHR list keeps the printed full stop after "mentioned here".',
    'Reading text, comprehension, MCQs, vocabulary, writing A-C, speaking, tense exercises and Revision Exercises 1-16 match the book.',
]


def _fix(o):
    if isinstance(o, str):
        return o.replace('A few are being mentioned here:', 'A few are being mentioned here.')
    if isinstance(o, list):
        return [_fix(x) for x in o]
    if isinstance(o, dict):
        return {k: _fix(v) for k, v in o.items()}
    return o


def patch(u):
    u['sections'] = _fix(u['sections'])
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 50).'
    r = u['exercise']['revisionExercises'][13]
    r['instruction'] = ('Form gerunds from the verbs in the box and use them to complete the sentences below. '
                        'Box (as printed): steel, cycle, skip, hike, paint, surf, race, make, cheat, bake. '
                        'SpaceBook note: "steel" is printed for "steal".')


_p5 = patch


def patch(u):
    from honorific import fix
    _p5(u)
    u['sections'] = fix(u['sections'])


NOTES.append('Empty honorific brackets in the stored text ("Hazrat Muhammad (migrated", "Rasool ()") restored to the printed honorific.')
