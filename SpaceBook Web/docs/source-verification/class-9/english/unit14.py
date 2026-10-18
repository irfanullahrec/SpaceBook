# -*- coding: utf-8 -*-
"""Unit 14 (Biodiversity in Pakistan) corrections from source PDF 145-154 (printed 134-143; printed 137 missing)."""

PDF = list(range(145, 155))  # PDF 150 duplicates printed 139
LAB = 'SpaceBook answer (the textbook prints no answers): '

SOURCE_SLOS = [
    'use pre-reading strategies to predict the content of a text from topic / picture / title / headings, key words and visuals etc., by using prior knowledge, asking questions and contextual clues.',
    'identify and analyze appropriate expressions and interviewing techniques to conduct and give short interviews of a friend or relative on specific topics.',
    'write a persuasive / argumentative essay on a given topic.',
    'anticipate and respond to opposing arguments by defending point of view with factual evidence, quotations, expert opinion, logical reasoning and commonly held beliefs.',
    'interpret the situation in a visual cue and with the help of mind map giving vocabulary, structure and sensory details to write a short description.',
    'use dictionary to: choose appropriate word definition; identify part of speech; recognize abbreviation used in a dictionary; locate synonyms in a thesaurus.',
    'translate passages from English to Urdu: use the knowledge of literal and figurative meaning, grammatical gender and syntax to translate passage from English to Urdu; understand that most phrases and idioms do not translate literally from one language to another.',
    'recognize and use parenthesis (Round Brackets) to: enclose numbers or letters in enumerations in the text; express an amount in numbers previously expressed in words; mark off explanatory or supplementary material.',
    'recognize and use omission marks or ellipses to signify the omission or deletion of letters or words in sentences.',
]

PRE_READING = [
    dict(q='What is biodiversity?', a='Pre-reading question (PDF 146)'),
    dict(q='What is ecosystem?', a='Pre-reading question (PDF 146)'),
    dict(q='What do you mean by endangered species?', a='Pre-reading question (PDF 146)'),
]

GLOSSARY = [
    ('inadequate', 'not enough; not good enough', 'ناکافی', 'ناکافي'),
    ('engagement', 'an arrangement to do something at a particular time, especially something official or something connected with your job', 'شمولیت، مصروفیت', 'ګډون، بوختیا'),
    ('mainstreaming', 'o make a particular idea or opinion accepted by most people', 'مرکزی دھارے میں لانا', 'اصلي بهیر ته راوستل'),
    ('preserving', 'to keep a particular quality, feature, etc.; to make sure that something is kept', 'تحفظ کرنا', 'ساتل'),
    ('endemic', 'regularly found in a particular place or among a particular group of people and difficult to get rid of', 'مقامی، کسی خاص علاقے کا', 'سیمه ییز، ځای ځانګړی'),
    ('woodland', 'an area of land that is covered with trees', 'جنگلاتی علاقہ', 'ځنګلي سیمه'),
    ('potential', 'that can develop into something or be developed in the future', 'ممکنہ، امکانی', 'احتمالي، شونی'),
    ('diversion', 'the act of changing the direction that somebody/something is following, or what something is used for', 'رخ موڑنا', 'لوری بدلول'),
    ('cetacean', 'a marine mammal of the Order of Cetacea e.g. a whale, a dolphin etc', 'وہیل نما سمندری ممالیہ', 'د وېل ډوله بحري تی لرونکی'),
    ('extirpation', 'to remove or destroy totally', 'مکمل خاتمہ', 'بشپړ له منځه وړل'),
]

GAP_EN = ('[Source gap: printed page 137 is missing from every available copy of the textbook (PDF, JPG scans and Word file). '
          'The text between "Likewise, Balochistan\'s forests are" and "resource, lack of awareness" could not be checked and is not shown.]')
GAP_UR = '[ماخذ میں خلا: درسی کتاب کا صفحہ 137 کسی بھی دستیاب نسخے (PDF، JPG اسکین اور ورڈ فائل) میں موجود نہیں۔ "Likewise, Balochistan\'s forests are" اور "resource, lack of awareness" کے درمیان کا متن جانچا نہیں جا سکا، اس لیے نہیں دکھایا گیا۔]'
GAP_PS = '[د سرچینې تشه: د درسي کتاب 137 مخ په هېڅ موجوده نسخه (PDF، JPG سکنونه او ورډ فایل) کې نشته. د "Likewise, Balochistan\'s forests are" او "resource, lack of awareness" ترمنځ متن ونه ازمویل شو، نو نه دی ښودل شوی.]'

P138_EN = ('... resource, lack of awareness, insufficient access to local knowledge, legal impediments, limited public and stakeholder participation, '
           'lack of mainstreaming of biodiversity with other sectors, lack of transfer of technology and expertise, inadequate engagement of scientific community, '
           'poverty, increasing population, climate change and natural disasters.')
P138_UR = ('... وسائل، شعور کی کمی، مقامی علم تک ناکافی رسائی، قانونی رکاوٹیں، عوام اور اسٹیک ہولڈرز کی محدود شمولیت، دیگر شعبوں کے ساتھ حیاتیاتی تنوع کو مرکزی دھارے میں نہ لانا، '
           'ٹیکنالوجی اور مہارت کی منتقلی کی کمی، سائنسی برادری کی ناکافی شمولیت، غربت، بڑھتی آبادی، موسمیاتی تبدیلی اور قدرتی آفات۔')
P138_PS = ('... سرچینه، د پوهاوي کمښت، سیمه ییزې پوهې ته ناکافي لاسرسی، قانوني خنډونه، د خلکو او ونډه والو محدود ګډون، له نورو برخو سره د ژوندي تنوع نه یوځای کول، '
           'د ټکنالوژۍ او مهارت د لېږد کمښت، د ساینسي ټولنې ناکافي ګډون، بېوزلي، مخ په زیاتېدونکی نفوس، د اقلیم بدلون او طبیعي پېښې.')
END_EN = 'It is high time that we act now otherwise the biodiversity will vanish and the next generation would see only pictures, movies and stuffed toys of biodiversity.'
END_UR = 'اب وقت آ گیا ہے کہ ہم فوراً عمل کریں ورنہ حیاتیاتی تنوع ختم ہو جائے گا اور آنے والی نسل حیاتیاتی تنوع کو صرف تصویروں، فلموں اور بھرے ہوئے کھلونوں میں دیکھے گی۔'
END_PS = 'دا د عمل وخت دی، کنه ژوندي تنوع به له منځه ولاړ شي او راتلونکی نسل به ژوندي تنوع یوازې په انځورونو، فلمونو او ډک شویو لوبو کې ویني.'

NOTES = [
    'Printed page 137 is missing from the PDF, the JPG scans and the Word file; the stored text for that page (Juniper/mangrove paragraphs and the start of the challenges list) could not be verified and was replaced with a visible source-gap note. The removed text is kept in sourceReview.removedUnverifiedText.',
    'PDF 150 is a second scan of printed page 139 and is recorded as a duplicate.',
    'Author corrected: the book prints no unit author (PDF 145).',
    'Learning outcomes (PDF 145), pre-reading (PDF 146) and the printed glossary (PDF 148) added; Urdu/Pashto glossary meanings are SpaceBook translations; "o make" is printed this way.',
    'Reading text on printed 135-136 and 138, comprehension 1-6, vocabulary A-B, interview role play, writing A-C and parentheses/ellipsis grammar match the book.',
]


def patch(u):
    u['author'] = ''
    u['authorInfo'] = 'The book prints no author name for this unit (PDF 145).'
    s4, s5 = u['sections'][3], u['sections'][4]
    removed = dict(section4=s4.get('paras'), section5First=s5.get('paras', [None])[0])
    s4['paras'] = ["Likewise, Balochistan's forests are ...", GAP_EN]
    s4['text'] = '\n\n'.join(s4['paras'])
    s4['urdu'] = 'اسی طرح بلوچستان کے جنگلات ...\n\n' + GAP_UR
    s4['pashto'] = 'همدارنګه د بلوچستان ځنګلونه ...\n\n' + GAP_PS
    s4['heading'] = '4. Forestry Resources (printed page 137 missing)'
    s5['paras'] = [P138_EN, END_EN]
    s5['text'] = '\n\n'.join(s5['paras'])
    s5['urdu'] = P138_UR + '\n\n' + END_UR
    s5['pashto'] = P138_PS + '\n\n' + END_PS
    s5['heading'] = '5. Challenges in Conservation & A Call to Action'
    u['_removed'] = removed
