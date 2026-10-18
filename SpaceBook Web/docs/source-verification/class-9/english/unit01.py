# -*- coding: utf-8 -*-
"""Unit 1 corrections from source PDF 10-20 (printed 1-11)."""

PDF = list(range(10, 21))
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.',
    'analyze passages in the text to identify the theme / general subject, key idea / central thought (a statement about general subject), and supporting details.',
    'apply critical thinking to interact with text and use intensive reading strategies to scan to answer short questions.',
    'use summary skills to extract salient points and develop a mind map to summarize a text.',
    'use dictionary to: choose appropriate word definition; identify part of speech; recognize abbreviation used in a dictionary; locate synonyms in a thesaurus.',
    'translate passages from English to Urdu: use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passage from English to Urdu; understand that most phrases and idioms do not translate literally from one language to another.',
    'demonstrate use of more collective, countable and uncountable nouns, material and abstract nouns.',
    'apply the rules of change of number of nouns learnt earlier.',
    'recognize and demonstrate use of some nouns that change meaning in the plural form e.g. arm-arms – arm (a part of body), arms (weapons).',
]

PRE_READING = [
    dict(q='Look at the mind map below to predict the content of the lesson.',
         a='Mind map: Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) — Rahmatul-lil-Alameen · Justice · Humanity · Patience · Sadiq and Ameen'),
]

# (word, book meaning, urdu, pashto)
GLOSSARY = [
    ('compassion', 'a strong feeling of sympathy for people who are suffering and a desire to help them', 'ہمدردی، رحم دلی', 'زړه سوی، خواخوږي'),
    ('debt', 'a sum of money that somebody owes', 'قرض', 'پور'),
    ('epitome', 'a perfect example of something', 'کامل نمونہ', 'بشپړه بېلګه'),
    ('dreadful', 'very bad or unpleasant', 'خوفناک، بہت برا', 'ډېر بد، وېرونکی'),
    ('restraining', 'to stop somebody/something from doing something', 'روکنا', 'منع کول، مخه نیول'),
    ('amnesty', 'a period of time during which people can admit to a crime or give up weapons without being punished', 'عام معافی', 'عمومي بښنه'),
    ('counselling', 'professional advice about a problem', 'مشاورت، نصیحت', 'مشوره، لارښوونه'),
    ('perseverance', 'the quality of continuing to try to achieve a particular aim despite difficulties', 'ثابت قدمی، استقامت', 'استقامت، ټینګار'),
    ('debate', 'a formal discussion on an issue at a public meeting. In a debate two or more speakers express opposing views', 'مباحثہ', 'مناظره، بحث'),
    ('precedence', 'the condition of being more important than somebody else and therefore coming or being dealt with first', 'فوقیت، ترجیح', 'لومړیتوب، غوره والی'),
    ('adversity', 'a difficult or unpleasant situation', 'مصیبت، مشکل حالات', 'سختي، کړاو'),
    ('renounced', 'to state publicly that you no longer have a particular belief or that you will no longer behave in a particular way', 'ترک کر دیا', 'پرېښود، لاس ترې واخیست'),
    ('testified', 'to say that you believe something is true because you have evidence of it', 'گواہی دی', 'شاهدي یې ورکړه'),
    ('Rabbi', 'Jewish religious scholar', 'یہودی عالم (ربی)', 'یهودي عالم (ربي)'),
    ('ostracised', 'to refuse to let somebody be a member of a social group; to refuse to meet or talk to somebody', 'سماجی بائیکاٹ کیا', 'ټولنیز بایکاټ یې کړ'),
    ('opponent', 'a person that you are playing or fighting against in a game, competition, argument, etc.', 'مخالف، حریف', 'مخالف، سیال'),
    ('scarcity', 'if there is a scarcity of something, there is not enough of it and it is difficult to obtain it', 'قلت، کمی', 'کمښت، قلت'),
    ('gracious', 'kind, polite and generous, especially to somebody of a lower social position', 'مہربان، شفیق', 'مهربان، لوی زړه لرونکی'),
    ('revenge', 'something that you do in order to make somebody suffer because they have made you suffer', 'انتقام، بدلہ', 'غچ، بدل'),
]

COMPREHENSION = [
    ('1. What does the Quran say about tolerance?',
     'The Holy Quran says: "O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient." (Al-Baqarah 2:153). It also calls the Holy Prophet Rahmatul-lil-Alameen, a mercy unto the whole mankind and universe.'),
    ('2. Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) was a man of extraordinary endurance? Explain.',
     'When the Quraish ostracised him and Banu-Hashim, they lived for three years in the valley of Shab-Abi-Talib with scarcity of food and water and no means of income. He remained calm and tolerant and never thought of revenge. He also bore the rough behaviour of Rabbi Zaid with patience.'),
    ('3. How did Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) treat the people of Makkah after victory?',
     'The Muslim army entered Makkah humbly and peacefully; no house was robbed and no one was insulted. He granted a general amnesty to the whole population, repeated Hazrat Yousuf\'s words "Have no fear this day, May Allah forgive you", and even forgave Abu Sufyan and his wife.'),
    ('4. Why was the Rabbi asking for the repayment days before the loan was due?',
     "He wanted to test Hazrat Muhammad's tolerance."),
    ('5. What does the tolerance of Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) teach us?',
     'It teaches us to be patient in adversity, to forgive even our worst enemies, to answer harsh treatment with kindness and to stay calm instead of seeking revenge.'),
    ("6. What was the effect of Hazrat Muhammad's (رسول اللہ خاتم النبیین ﷺ) kindness on the Rabbi?",
     'The Rabbi saw that tolerance and perseverance took precedence over anger and that harsh treatment was repaid with kindness. He immediately renounced his religion and testified that there is none worthy of worship but Allah and that Hazrat Muhammad is His Rasool.'),
    ('7. What is the main idea of the lesson?',
     'The life of Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) is a superb example of tolerance, forgiveness, patience and compassion, and we should follow it in our own lives.'),
]

NOTES = [
    'Comprehension A was replaced with the seven questions printed on PDF 15 (printed 6).',
    'Glossary (PDF 14, printed 5) added: 19 words with the book meanings; Urdu/Pashto meanings are SpaceBook translations.',
    'Pre-reading mind map (PDF 11, printed 2) added.',
    'The book prints the honorific (رسول اللہ خاتم النبیین ﷺ) after the name; the stored MCQs use (PBUH) and are left as they were.',
]
