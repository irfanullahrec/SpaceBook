"""Urdu XII PDF112 (spread): p.214 Poem 6 مشق Q1–Q6 + notes مخمس / معریٰ نظم; p.215 Poem 7 author note (منیر نیازی, 1928–2006)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write the central idea of the poem “Nafeer-e-Amal”.', '۱۔ نظم ’’نفیرِ عمل‘‘ کا مرکزی خیال لکھیں۔', '۱. د "د عمل شپېلۍ" نظم مرکزي فکر ولیکئ.'),
    ('2. State the summary of this poem in your own words.', '۲۔ اس نظم کا خلاصہ اپنے الفاظ میں بیان کریں۔', '۲. د دې نظم لنډیز په خپلو کلمو بیان کړئ.'),
    ('3. Write the meanings of the following compounds: shūmī-e taqdīr, jaur-e falak, maḥrūm-e tajallī, chāra-e dard, jins-e girāṉ-māya, makr-o-riyā.', '۳۔ درج ذیل مرکبات کے معنی لکھیں: شومیِ تقدیر۔ جورِ فلک۔ محرومِ تجلّی۔ چارۂ درد۔ جنسِ گراں مایہ۔ مکر و ریا۔', '۳. د لاندې مرکباتو ماناوې ولیکئ: د تقدیر بدمرغي، د اسمان ظلم، له رڼا بې‌برخې، د درد درملنه، قیمتي جنس، چل او ریا.'),
    ('4. In what words has the poet, in the first stanza of “Nafeer-e-Amal”, taught the youth of the homeland the lesson of action?', '۴۔ نظم ’’نفیرِ عمل‘‘ کے پہلے بند میں شاعر نے کن الفاظ میں نوجوانانِ وطن کو عمل کا درس دیا ہے؟', '۴. د "د عمل شپېلۍ" په لومړي بند کې شاعر په کومو کلمو د وطن ځوانانو ته د عمل درس ورکړی؟'),
    ('5. Identify the allusions (talmīḥāt) used in this poem.', '۵۔ اس نظم میں استعمال ہونے والے تلمیحات کی نشان دہی کریں۔', '۵. په دې نظم کې کارول شوي تلمیحات په نښه کړئ.'),
    ('6. According to the poet, what should the young not be afraid of?', '۶۔ شاعر کے مطابق نوجوانوں کو کس چیز سے خوف زدہ نہیں ہونا چاہیے؟', '۶. د شاعر په وینا ځوانان باید له کوم شي ونه وېرېږي؟'),
])
ex = BOOK.record(e, 'urdu12-u23-exercise', 'Exercise', 'مشق', 'تمرین', 112, [214])

n = Builder()
n.group('lines', [
    ('Mukhammas: a poem each of whose stanzas has five lines is called a “mukhammas”.', 'مخمّس: جس نظم کے ہر بند میں پانچ مصرعے ہوں اُسے ’’مخمّس‘‘ کہتے ہیں۔', 'مخمس: هغه نظم چې په هر بند کې یې پنځه مصرعې وي، "مخمس" بلل کېږي.'),
    ('Muʿarrā naẓm (blank verse): in blank verse there is no constraint of rhyme and refrain, but adherence to metre and baḥr is necessary.', 'معریٰ نظم: معریٰ نظم میں قافیہ اور ردیف کی پابندی نہیں ہوتی مگر وزن اور بحر کی پابندی لازمی ہے۔', 'معرا نظم (سپین شعر): په معرا نظم کې د قافیې او ردیف پابندي نه وي، خو د وزن او بحر پابندي لازمي ده.'),
])
nt = BOOK.record(n, 'urdu12-u23-notes', 'Notes: mukhammas and blank verse', 'مخمّس اور معریٰ نظم', 'مخمس او معرا نظم', 112, [214])

a = Builder()
a.h('Munir Niazi', 'منیرؔ نیازی', 'منیر نیازي')
a.p('Born: 1928 · Died: 2006', 'ولادت: ۱۹۲۸ء · وفات: ۲۰۰۶ء', 'زېږېدنه: ۱۹۲۸ز · مړینه: ۲۰۰۶ز')
for x in [
    ('Munir Ahmad Khan Niazi was born in Khanpur, a village of Hoshiarpur district (East Punjab). He received his early education in Khanpur itself. After the creation of Pakistan his family migrated to Pakistan and settled in Sahiwal. After doing his Intermediate from Bahawalpur, Munir Niazi did his B.A. from Dyal Singh College Lahore. He started a weekly magazine named “Saat Rang”. Besides this he was also associated with various newspapers, journals and Radio Pakistan, and also wrote poetry for films.',
     'منیرؔ احمد خان نیازی ضلع ہوشیار پور (مشرقی پنجاب) کے ایک گاؤں خان پور میں پیدا ہوئے۔ اُنھوں نے ابتدائی تعلیم خان پور ہی میں حاصل کی۔ قیامِ پاکستان کے بعد اُن کا خاندان ہجرت کر کے پاکستان آیا اور ساہیوال میں رہائش اختیار کی۔ بہاولپور سے انٹرمیڈیٹ کرنے کے بعد منیر نیازی نے دیال سنگھ کالج لاہور سے بی۔اے کیا۔ اُنھوں نے ’’سات رنگ‘‘ کے نام سے ایک ہفتہ وار رسالہ جاری کیا۔ اس کے علاوہ وہ مختلف اخبارات، رسائل اور ریڈیو پاکستان سے بھی منسلک رہے جبکہ فلموں کے لیے بھی شاعری کرتے رہے۔',
     'منیر احمد خان نیازي د هوښیارپور ولسوالۍ (ختیځ پنجاب) د خانپور په یوه کلي کې زېږېدلی. لومړنۍ زده‌کړې یې په خانپور کې وکړې. د پاکستان له جوړېدو وروسته یې کورنۍ پاکستان ته کډه شوه او په ساهیوال کې مېشته شوه. له بهاولپوره یې د انټرمیډیټ وروسته منیر نیازي له دیال سنګه کالج لاهور نه بي.اې وکړ. هغه د "اوه رنګونه" په نوم یوه اونیزه مجله پیل کړه. سربېره پر دې له بېلابېلو ورځپاڼو، مجلو او راډیو پاکستان سره تړلی و او د فلمونو لپاره یې هم شاعري کوله.'),
    ("A single word suffices to identify Munir Niazi, and that word is “wonder” (taḥayyur): he is a poet of wonder. He wants to trace unknown states and gives familiar things a new aspect with his poetic sensibility. Munir's poetry does not grow in a mere void; rather it voices its own age, which comes before us with new signs and symbols. An element of rapturous ecstasy is also found in his poetry. He is a poet of a distinct manner who stands apart from beaten paths; his tone is so different from the common style that he can be recognised easily. In recognition of his literary services the Government of Pakistan honoured him with “Kamal-e-Fun” and “Sitara-e-Imtiaz”.",
     'منیرؔ نیازی کی شناخت کے لیے ایک ہی لفظ کافی ہے اور وہ ہے ’’تحیر‘‘ وہ تحیر کے شاعر ہیں۔ وہ نامعلوم کیفیات کا سراغ لگانا چاہتے ہیں اور جانی پہچانی اشیا کو اپنی شاعرانہ حسیات سے ایک نیا رُخ دیتے ہیں۔ منیرؔ کی شاعری محض خلا میں پروان نہیں چڑھی بلکہ اپنے عہد کی ترجمانی کرتی ہے جو نئے رموز اور علامات کے ساتھ ہمارے سامنے آتی ہیں۔ اُن کی شاعری میں والہانہ سرشاری کا عنصر بھی پایا جاتا ہے۔ وہ اپنے ڈھنگ کے ایک الگ شاعر ہیں جو گھسی پٹی راہوں سے دُور کھڑے نظر آتے ہیں۔ ان کا لہجہ عام اسلوب سے اتنا مختلف ہے کہ اُن کی شناخت آسانی سے ہو سکتی ہے۔ اُن کی ادبی خدمات کے صلے میں حکومتِ پاکستان کی جانب سے اُنھیں ’’کمالِ فن‘‘ اور ’’ستارۂ امتیاز‘‘ سے بھی نوازا گیا ہے۔',
     'د منیر نیازي د پېژندنې لپاره یوه کلمه بسنه کوي، او هغه "حیرانتیا" ده؛ هغه د حیرانتیا شاعر دی. غواړي د ناپېژندل شویو کیفیتونو سراغ ولګوي او پېژندل شویو شیانو ته په خپل شاعرانه حس نوی اړخ ورکوي. د منیر شاعري یوازې په تشه کې نه ده لویه شوې، بلکې د خپل عصر ترجماني کوي، چې له نویو رمزونو او نښو سره زموږ مخې ته راځي. په شاعرۍ کې یې د مستانه سرشارۍ عنصر هم شته. هغه د خپل ډول یو بېل شاعر دی چې له زړو لارو لرې ولاړ ښکاري؛ لهجه یې له عام سبک دومره توپیر لري چې په اسانۍ پېژندل کېږي. د ادبي خدمتونو په بدل کې د پاکستان حکومت هغه ته "کمال فن" او "ستاره امتیاز" ورکړي.'),
    ('Collections of poetry: Tez Hawa aur Tanha Phool, Jangal mein Dhanak, Dushmanon ke Darmiyan Sham, Chhe Rangeen Darwaze, etc.', 'مجموعہ ہائے کلام: تیز ہوا اور تنہا پھول، جنگل میں دھنک، دشمنوں کے درمیان شام، چھے رنگین دروازے۔ وغیرہ', 'د کلام ټولګې: تېز باد او یوازې ګل، په ځنګل کې شنه زرغونه، د دښمنانو ترمنځ ماښام، شپږ رنګینې دروازې او نور.'),
]: a.p(*x)
UT = ('I Am Always Late (Hamesha Der Kar Deta Hoon)', 'ہمیشہ دیر کر دیتا ہوں', 'زه تل ځنډ کوم', 'منیرؔ نیازی')
au = BOOK.record(a, 'urdu12-u24-author', 'About the poet: Munir Niazi', 'منیرؔ نیازی (تعارف)', 'منیر نیازي (پېژندنه)', 112, [215], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Munir Niazi and floral border are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf112', 'unit': 24, 'printedPage': 215, 'description': 'Munir Niazi died 2006 — in copyright; Poem 7 will be given as a summary with a sourceGap note; board-written author note and exercises are transcribed. The note on p.214 calls the poem a mukhammas, though “Nafeer-e-Amal” is printed in five-line stanzas (2 couplets + refrain) — consistent.'}]

if __name__ == '__main__':
    BOOK.save(112, [(23, ex), (23, nt), (24, au)], issues=issues, complete_units=[23])
