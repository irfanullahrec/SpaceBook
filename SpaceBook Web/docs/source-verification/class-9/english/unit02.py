# -*- coding: utf-8 -*-
"""Unit 2 corrections from source PDF 21-32 (printed 12-23)."""

PDF = list(range(21, 33))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'analyze passages in the text to identify the theme / general subject, key idea / central thought (a statement about general subject), and supporting details.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'illustrate use of pronouns learned earlier.',
    'identify and demonstrate use of relative pronouns.',
    'recognize the rules of using indefinite pronouns.',
    'illustrate the use of pronouns antecedent agreement.',
    'illustrate the use of anaphoric and cataphoric references.',
    'translate passages from English to Urdu: use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passage from English to Urdu; understand that most phrases and idioms do not translate literally from one language to another.',
    'identify and recognize the functions of: pronoun – antecedent relationships; anaphoric and cataphoric references; transitional devices used for coherence and cohesion at discourse level.',
    'analyze and understand common prefixes and suffixes and use that knowledge to determine the meaning of the unfamiliar words.',
]

PRE_READING = [
    dict(q='Iqbal wants to see the qualities of an eagle (shaheen) in his young nation. What are the qualities of an eagle that makes it superior to other birds?',
         a='Picture: an eagle in flight'),
]

GLOSSARY = [
    ('exploration', 'the act of travelling through a place in order to find out something about it or look for something in it', 'کھوج، دریافت کا سفر', 'سپړنه، لټون'),
    ('Invention', 'the introduction of new things, ideas or ways of doing something', 'ایجاد', 'اختراع'),
    ('Innovation', 'the ability to have new and interesting ideas', 'جدت، نیا پن', 'نوښت'),
    ('Hamlet', 'a character from Shakespearian play who would take too much time in thinking before taking an action', 'ہیملٹ (شیکسپیئر کا کردار جو عمل سے پہلے بہت سوچتا ہے)', 'هېملټ (د شکسپیر کرکټر چې له عمل مخکې ډېر فکر کوي)'),
    ('perpetual', 'continuing for a long period of time without interruption', 'مسلسل، دائمی', 'دوامداره، تل پاتې'),
    ('foresight', 'the ability to predict what is likely to happen and to use this to prepare for the future', 'دور اندیشی', 'لرلید، مخکینی فکر'),
    ('enthusiastic', 'feeling or showing a lot of excitement and interest about somebody/something', 'پرجوش', 'په جوش، لېواله'),
    ('emperor', 'the ruler of an empire', 'شہنشاہ', 'امپراتور، شهنشاه'),
    ('thy', 'an English word that means "your"', 'تیرا', 'ستا'),
    ('forge', 'to put a lot of effort into making something successful or strong so that it will last', 'محنت سے بنانا، ڈھالنا', 'په زیار جوړول'),
    ('brilliance', 'intense brightness of light/exceptional talent or intelligence', 'چمک، ذہانت', 'ځلا، استعداد'),
    ('nova', 'a star showing a sudden large increase in brightness and then suddenly returning to its original state.', 'نووا (اچانک چمکنے والا ستارہ)', 'نووا (ناڅاپه ځلېدونکی ستوری)'),
    ('inspiration', 'a sudden brilliant or timely idea.', 'الہام، تحریک', 'الهام، هڅونه'),
]

COMPREHENSION = [
    ('1. How is the youth standard bearer of a nation?',
     "Young people carry the nation forward. If their energy is channelized in the proper direction, it can bring a sea change in the social, political and economic fabric of the nation."),
    ('2. According to Iqbal how can the youth change themselves?',
     'By becoming men of Khudi: knowing themselves ("Know thyself and success shall be thine"), developing the spirit of Ishq and perpetual struggle, and living like the Shaheen, aiming higher and exploring new worlds of creativity and knowledge.'),
    ('3. Read the 3rd paragraph and write down its key idea.',
     "Iqbal's young man is a Mard-e-Momin and Shaheen: a believer, explorer and adventurer whose strong belief in Ishq gives him creative energy to discover new stars of originality and individuality."),
    ('4. What is the main idea of the lesson?',
     'Youth was the main focus of Iqbal. He saw them as the symbol of hope and the future of the nation, and wanted them to be self-aware, active, creative and pure in heart so that the Muslim community could rise as a mighty power.'),
    ("5. According to Iqbal, the youth shouldn't confine to material achievement? Express your view on this statement.",
     "Iqbal's youth is not satisfied with material achievement and its enjoyment; he enjoys the journey of exploration and discovery and always moves to the next goal. Material success alone makes a person content and lazy, while higher intellectual and spiritual goals keep a nation progressing."),
]

NOTES = [
    'Author corrected to Waheedullah as printed on PDF 21 (was "Allama Muhammad Iqbal").',
    'Pre-reading question (PDF 22) and verbatim learning outcomes (PDF 21) added.',
    'Glossary (PDF 25, printed 16) added: 13 words with book meanings; Urdu/Pashto meanings are SpaceBook translations.',
    'Comprehension questions re-worded exactly as printed on PDF 25; answers labelled SpaceBook.',
    'MCQ 1 option d corrected to "irrational" as printed (was "irrational / ordinary").',
    'Last paragraph keeps the printed spelling "Umma"; second "Noujawan" kept as printed (PDF 23); Urdu verse corrected to begin "ہر اک مقام" as printed.',
]


REPL = [('prosperity of the Ummah,', 'prosperity of the Umma,'),
        ("Moreover, Iqbal's Naujawan is a Man of Khudi", "Moreover, Iqbal's Noujawan is a Man of Khudi"),
        ('اک مقام سے آگے مقام ہے تیرا', 'ہر اک مقام سے آگے مقام ہے تیرا')]


def _fix(o):
    if isinstance(o, str):
        for a, b in REPL:
            if b not in o:
                o = o.replace(a, b)
        return o
    if isinstance(o, list):
        return [_fix(x) for x in o]
    if isinstance(o, dict):
        return {k: _fix(v) for k, v in o.items()}
    return o


def patch(u):
    u['author'] = 'Waheedullah'
    u['authorInfo'] = 'The lesson "Iqbal' + chr(39) + 's Message to Youth" is written by Waheedullah (printed under the unit title, PDF 21). The front matter lists Waheedullah, SS (English), KP Textbook Board, Peshawar, among the reviewers.'
    m = u['exercise']['textbookMcqs'][0]
    m['options'] = [o if o != 'irrational / ordinary' else 'irrational' for o in m['options']]
    u['sections'] = _fix(u['sections'])


_base_patch = patch


def patch(u):
    _base_patch(u)
    pa = u['exercise']['prefixActivity']
    pa[1].update(sentence='No, that answer is <b>incorrect</b>. It is wrong.')
    pa[2].update(prefix='re-', word='review', sentence="Let's look at this information again. We should <b>review</b> it before the test.")


NOTES.append('Prefix exercise A (PDF 28): item 2 restored to the printed sentence; item 3 answer corrected to "review" (the printed prefix list is dis-, in-, mis-, re-, un-; "pre-" is not offered).')
