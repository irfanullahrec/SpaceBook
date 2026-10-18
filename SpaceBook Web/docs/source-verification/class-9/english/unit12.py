# -*- coding: utf-8 -*-
"""Unit 12 (The Old Woman) corrections from source PDF 128-133 (printed 117-122)."""

PDF = list(range(128, 134))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'identify line and stanza.',
    'read poem and give orally or in writing: main idea; theme and its development; summary; personal response with justification; paraphrase.',
    'use paraphrasing skills to paraphrase stanzas: mark thought groups in the stanza; restate the message in simple prose; replace poetic words with simple ones.',
    'read and analyze how the poet uses language to: appeal to the senses through use of figurative language including similes and metaphors; affect meaning through use of synonyms with different connotation and denotation; create imagery.',
    'describe the object being personified.',
    'deduce meaning of difficult words from context.',
    'use active and passive voice appropriately in speech and writing according to required communicative function.',
]

PRE_READING = [
    dict(q='What do the pictures below have in common?', a='Pictures: three elderly women (PDF 129)'),
    dict(q='What does the phrase "respect your elders" mean?', a='Pre-reading question (PDF 129)'),
    dict(q='How do you show respect to your elders?', a='Pre-reading question (PDF 129)'),
]

GLOSSARY = [
    ('radiance', "a special bright quality that shows in somebody's face, for example because they are very happy or healthy", 'چمک، نور', 'ځلا'),
    ('travail', 'an unpleasant experience or situation that involves a lot of hard work, difficulties and suffering', 'مشقت، محنت', 'زحمت، کړاو'),
    ('brood', "a person's child or children", 'اولاد', 'اولاد'),
    ('ruined', 'destroyed or severely damaged so that only parts remain', 'تباہ شدہ، کھنڈر', 'ویجاړ'),
]

ABOUT_POET = ('About the Poet: The poet Joseph Campbell was born in 1906 in White Plains, New York. He won name and fame as a writer, poet and athlete. '
              'As an athlete, he was among the fastest half-mile runners in the world. His first published work was, "Where the Two Came to Their Father". '
              'The poem, "The Old Woman" has been taken from his collection of poems. He describes the old age of a woman. '
              'The beauty of a woman vanishes and she looks like a white candle in her old age.\n\n'
              'SpaceBook note: this biography, printed in the book (PDF 130), describes the American writer Joseph Campbell (1904-1987). '
              '"The Old Woman" was written by the Irish poet Joseph Campbell (1879-1944). The printed text is kept as it appears in the book.')

ACTIVE_TO_PASSIVE = [
    ('1. I have finished the job.', 'The job has been finished by me.'),
    ('2. They built this house in 1990.', 'This house was built (by them) in 1990.'),
    ('3. He has bought a new car.', 'A new car has been bought by him.'),
    ('4. I wrote a letter.', 'A letter was written by me.'),
    ('5. They sent the parcel on Monday.', 'The parcel was sent (by them) on Monday.'),
    ('6. The police caught the thief yesterday.', 'The thief was caught by the police yesterday.'),
    ('7. She baked a cake.', 'A cake was baked by her.'),
    ('8. I read a book.', 'A book was read by me.'),
    ('9. She gave the beggar a five rupee coin.', 'The beggar was given a five rupee coin by her. / A five rupee coin was given to the beggar by her.'),
]
VOICE_CHANGE = [
    ('1. The thieves have been arrested by the police.', 'The police have arrested the thieves.'),
    ('2. The marvelous performance delivered by the children enthralled us.', 'We were enthralled by the marvelous performance delivered by the children.'),
    ('3. He has been invited to their party.', 'They have invited him to their party.'),
    ('4. We have shipped your order.', 'Your order has been shipped (by us).'),
    ('5. The girl recited the poem beautifully.', 'The poem was recited beautifully by the girl.'),
    ('6. The guests enjoyed the party.', 'The party was enjoyed by the guests.'),
    ('7. The child impressed everyone with his polite manners.', 'Everyone was impressed by the child with his polite manners.'),
    ('8. A girl from Bannu won the first prize.', 'The first prize was won by a girl from Bannu.'),
    ('9. The readers like the latest book of the writer.', 'The latest book of the writer is liked by the readers.'),
]

NOTES = [
    'About the Poet restored verbatim (PDF 130) with a SpaceBook note: the printed biography is of the American Joseph Campbell, while the poem is by the Irish poet of the same name.',
    'MCQ 2 and 5 options restored to the printed order (PDF 131-132); the SpaceBook answers keep the same option text with the new letters.',
    'Grammar A and B (Active and Passive Voice, PDF 133) were missing; added with SpaceBook answers.',
    'Learning outcomes (PDF 128), pre-reading (PDF 129) and the printed glossary (PDF 130) added; Urdu/Pashto glossary meanings are SpaceBook translations.',
    'Poem, comprehension A1-7, MCQ 1/3/4, vocabulary A-C, writing a-c and the speaking task match the book.',
]


def _reorder(m, printed):
    ans = m['answer'].split('. ', 1)[1] if '. ' in m['answer'] else m['answer']
    m['options'] = [f'{"abcd"[i]}. {t}' for i, t in enumerate(printed)]
    m['answer'] = next(o for o in m['options'] if o.endswith(ans))


def patch(u):
    u['authorInfo'] = ABOUT_POET
    mc = u['exercise']['textbookMcqs']
    _reorder(mc[1], ['The old woman is weak but with rich experience of life.', 'The old woman is strong and with wide experience of life.',
                     'The old woman is symbol of beauty and sunshine.', 'The old woman is symbol of success and growth.'])
    _reorder(mc[4], ['Difficulties of an old woman neither vanished nor runs away', 'Laborious life of an old woman',
                     'Calmness and wisdom in the life of an old woman', 'Natural beauty vanished in an old woman'])
    for m in mc:
        if not m.get('explanation', '').startswith('SpaceBook answer'):
            m['explanation'] = 'SpaceBook answer (the textbook prints no answer key): ' + m.get('explanation', '')
    ga = u['exercise'].setdefault('grammarActivities', {})
    ga['activeToPassive'] = [dict(sentence=q, answer=LAB + a) for q, a in ACTIVE_TO_PASSIVE]
    ga['voiceChange'] = [dict(sentence=q, answer=LAB + a) for q, a in VOICE_CHANGE]
    u['exercise']['speakingActivity']['prompt'] = 'Imagine you recently had an English test. In pairs express hopes and fears regarding your performance/result in the test.'
