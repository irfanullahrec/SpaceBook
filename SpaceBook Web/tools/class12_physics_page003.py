from class12_source_review import upsert, section, checkpoint

SOURCE = 'Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
quote = {'id': 'phys12-front-quotation', 'printedPage': None, 'pdfPage': 3,
         'sourcePdf': SOURCE, 'title': 'Opening quotation', 'sourceLanguage': 'mixed',
         'paragraphs': ['سچائی انسان کو ہر آفت سے محفوظ رکھتی ہے اور جھوٹ اسے ہلاک کر ڈالتا ہے',
                        '(الحدیث)', '“Say no to Corruption”']}
pairs = [
    ('Truthfulness protects a person from every calamity, and falsehood destroys them.',
     quote['paragraphs'][0], 'رښتینولي انسان له هرې بلا څخه ساتي او دروغ یې هلاکوي'),
    ('(Hadith)', '(الحدیث)', '(حدیث)'),
    ('“Say no to Corruption”', '“بدعنوانی کو نہ کہیں”', '“فساد ته نه ووایئ”'),
]
quoted = section(quote, pairs,
                 [{'type': 'paragraph', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
                  {'type': 'heading', 'indices': [2]}], ('ابتدائی قول', 'پیلنی قول'), 'mixed')
quoted['sourceLanguages'] = ['ur', 'ur', 'en']
for para, language in zip(quoted['paras'], quoted['sourceLanguages']):
    para['originalLanguage'] = language
quoted['sourceOriginalLabel'] = 'English Translation / English Source Slogan (Urdu quotation preserved in Urdu):'
quoted['sourceUrduLabel'] = 'Urdu Original Quotation / Translated Slogan (اصل اردو قول):'

title = {'id': 'phys12-front-title', 'printedPage': None, 'pdfPage': 3,
         'sourcePdf': SOURCE, 'title': 'A Textbook of Physics', 'sourceLanguage': 'en',
         'paragraphs': ['Grade-XII', 'Khyber Pakhtunkhwa Textbook Board, Peshawar']}
titled = section(title, [
    ('Grade-XII', 'جماعت بارہویں', 'دولسم ټولګی'),
    (title['paragraphs'][1], 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور',
     'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')],
    [{'type': 'lines', 'indices': [0, 1]}], ('طبیعیات کی درسی کتاب', 'د فزیک درسي کتاب'))

if __name__ == '__main__':
    upsert([quote, title], [quoted, titled])
    checkpoint(3, 'corrected_verified', [quote['id'], title['id']],
               'Original spread rendered at 2x and inspected. Urdu quotation restored without invented final punctuation; scan line wraps joined as one paragraph, Hadith attribution separated, slogan quotation marks retained. English translation and Pashto translation explicitly paired with Urdu original. Title, grade and publisher preserved. Floral frames, watermark, handwritten signature and publisher emblem excluded as noninstructional decoration. Sections upserted with stable IDs; existing final topic synchronization uses same corrected objects. Scoped reader labels distinguish source Urdu from English translation.')
