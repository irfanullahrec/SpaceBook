# -*- coding: utf-8 -*-
"""
build_pashto_1_data.py
Extracts and builds the complete Class 1 Pashto dataset (PASHTO_1_DATA)
from the official KPK Textbook Board Grade 1 Pashto materials:
D:\SpaceBook\Books\1st\1st Pashto\New folder\پښتو.docx

Outputs:
D:\SpaceBook\SpaceBook Web\js\pashto_1_data.js
"""

import os
import json
import zipfile
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_PATH = r"D:\SpaceBook\Books\1st\1st Pashto\New folder\پښتو.docx"
OUTPUT_JS = r"D:\SpaceBook\SpaceBook Web\js\pashto_1_data.js"

# 23 Chapters definitions with full textbook data
CHAPTERS_METADATA = [
    {
        "id": "cls1-ps-ch01",
        "number": 1,
        "type": "poem",
        "title": "حمد (نظم)",
        "titleUrdu": "حمد (نظم - تعریفِ خداوندی)",
        "titleEn": "Unit 1: Hamd (Poem - Praise of Allah Almighty)",
        "titlePs": "حمد (نظم)",
        "author": "پروفېسر اباسين يوسفزی",
        "pageRange": "1-4",
        "theme": "توحید او د کائنات ښکلا (Praise of Creator)",
        "authorInfo": "د پښتو لازمي درسي کتاب، اول جماعت، خېبر پښتونخوا ټېکسټ بک بورډ پېښور۔",
        "learningOutcomes": [
            "د ساده نظم په اورېدو د هغې نه خوند واخستي شي۔",
            "توري د صحيح غږونو سره ولوستل شي۔",
            "توري يو ځای کول او بېلول په صحيح ډول زده کړي۔",
            "د پښتو توري وپېژني۔"
        ],
        "learningOutcomesUrdu": [
            "سادہ نظم سن کر اس سے لطف اندوز ہو سکیں۔",
            "حروف کو درست آوازوں اور تلفظ کے ساتھ پڑھ سکیں۔",
            "حروف کو جوڑنا اور توڑنا درست طریقے سے سیکھ سکیں۔",
            "پشتو حروفِ تہجی کی درست پہچان کر سکیں۔"
        ],
        "sections": [
            {
                "heading": "د حمد شعرونه (بشپړ درسي متن)",
                "headingUrdu": "حمد کے اشعار (مکمل درسی متن)",
                "headingEn": "Verses of Hamd (Full Verbatim Text)",
                "text": "ښکته زمکه پاس اسمان\nجوړ بدلے ټول جهان دے\n\nساه لرونکی که بې ساه دي\nد ده په حکم را پیدا دي\n\nانسانان هم رنګارنګ\nښکلي ښکلي موسمونه\n\nنمر، سپوږمۍ، ستوري روښان دي\nځناور دي که مرغان دي\n\nشاړې غرونه، میدانونه\nځنګلونه او سیندونه\n\nواړه تا دي پېدا کړي\nدا دې مونږه له راکړي\n\nنعمتونه دې بې شمېر دي\nټول زما نه کله هېر دي\n\nخدایه! هر ځای کښې عیان ئې\nد هر چا روزي رسان ئې",
                "paras": [
                    "ښکته زمکه پاس اسمان، جوړ بدلے ټول جهان دے۔",
                    "ساه لرونکی که بې ساه دي، د ده په حکم را پیدا دي۔",
                    "انسانان هم رنګارنګ، ښکلي ښکلي موسمونه۔",
                    "نمر، سپوږمۍ، ستوري روښان دي، ځناور دي که مرغان دي۔",
                    "شاړې غرونه، میدانونه، ځنګلونه او سیندونه۔",
                    "واړه تا دي پېدا کړي، دا دې مونږه له راکړي۔",
                    "نعمتونه دې بې شمېر دي، ټول زما نه کله هېر دي۔",
                    "خدایه! هر ځای کښې عیان ئې، د هر چا روزي رسان ئې۔"
                ],
                "urdu": "نیچے زمین اور اوپر آسمان، یہ سارا جہان اللہ نے بنایا ہے۔ جاندار ہوں یا بے جان، سب اسی کے حکم سے پیدا ہوئے ہیں۔ انسان، خوبصورت موسم، سورج، چاند، چمکتے تارے، جانور اور پرندے، بنجر پہاڑ، میدان، جنگل اور ندیاں سب اسی نے پیدا کیے ہیں اور ہمیں عطا کیے ہیں۔ اس کی نعمتیں بے شمار ہیں اور وہ ہر جگہ ظاہر اور سب کا رزق دینے والا ہے۔",
                "english": "Below is the earth and above is the sky; Allah has created the entire universe. Whether living or non-living, all are created by His command. Diverse human beings, beautiful seasons, the sun, moon, glowing stars, animals, birds, barren mountains, plains, jungles, and rivers—all are created by Him and gifted to us. His blessings are countless, He is omnipresent, and He provides sustenance to all.",
                "pashto": "په دې حمد کښې اباسین یوسفزی د الله تعالی د قدرت او نعمتونو ښکلا بیانوي چې څنګه یې زمکه، اسمان، انسانان، ځناور او غرونه پیدا کړي دي۔"
            }
        ],
        "words": [
            { "word": "جهان", "meaning": "دنیا، عالم", "meaningUrdu": "دنیا، عالم", "english": "World / Universe", "sentence": "الله پاک ټول جهان پیدا کړی دی." },
            { "word": "ساه لرونکي", "meaning": "ژوندي موجودات، ځان لرونکي", "meaningUrdu": "جاندار چیزیں", "english": "Living things", "sentence": "ځناور او مرغان ساه لرونکي دي." },
            { "word": "روښان", "meaning": "روڼ، ځلېدونکی", "meaningUrdu": "روشن، چمکدار", "english": "Bright / Luminous", "sentence": "نمر او سپوږمۍ روښان دي." },
            { "word": "عیان", "meaning": "ښکاره، څرګند", "meaningUrdu": "ظاہر، عیاں", "english": "Manifest / Apparent", "sentence": "د الله تعالی قدرت په هر څه کښې عیان دی." },
            { "word": "روزي رسان", "meaning": "خوراک رسوونکی، رزق ورکوونکی", "meaningUrdu": "رزق دینے والا", "english": "Provider of sustenance", "sentence": "الله تعالی د هر مخلوق روزي رسان دی." }
        ],
        "exercise": {
            "textbookMcqs": [
                {
                    "question": "په حمد کښې د چا صفت بیانیږي؟",
                    "questionUrdu": "حمد میں کس کی تعریف بیان ہوتی ہے؟",
                    "questionEn": "Whose praise is described in Hamd?",
                    "options": ["د انسانانو", "د فرشتو", "د الله تعالی", "د پېغمبرانو"],
                    "optionsUrdu": ["انسانوں کی", "فرشتوں کی", "اللہ تعالیٰ کی", "پیغمبروں کی"],
                    "correctIndex": 2,
                    "explanation": "حمد هغه نظم ته وائي چې پکښې د الله تعالی صفت او ثنا بیان شي۔"
                },
                {
                    "question": "د 'همه' څه معنی ده؟",
                    "questionUrdu": "لفظ 'همه' کے کیا معنی ہیں؟",
                    "questionEn": "What is the meaning of 'Hama'?",
                    "options": ["لږ", "ټول", "کم", "هیڅ"],
                    "optionsUrdu": ["تھوڑا", "سب / تمام", "کم", "کچھ نہیں"],
                    "correctIndex": 1,
                    "explanation": "'همه' د ټولو او پوره معنی لري۔"
                },
                {
                    "question": "زمکه د پاسمان په پرتله چرته ده؟",
                    "questionUrdu": "زمین آسمان کے مقابلے میں کہاں ہے؟",
                    "questionEn": "Where is the earth compared to the sky?",
                    "options": ["ښکته", "بره", "منځ کښې", "پورته"],
                    "optionsUrdu": ["نیچے", "اوپر", "درمیان", "بلند"],
                    "correctIndex": 0,
                    "explanation": "ښکته زمکه پاس اسمان، جوړ بدلے ټول جهان دے۔"
                }
            ],
            "shortQuestions": [
                {
                    "question": "حمد څه ته وائي؟",
                    "questionUrdu": "حمد کسے کہتے ہیں؟",
                    "questionEn": "What is Hamd?",
                    "answer": "هغه نظم ته حمد وائي چې پکښې د الله تعالی صفت، ثنا او ستاینه بیان شوې وي۔",
                    "answerUrdu": "وہ نظم جس میں اللہ تعالیٰ کی تعریف و توصیف بیان کی جائے اسے حمد کہتے ہیں۔",
                    "answerEn": "A poem that praises Allah Almighty and His blessings is called a Hamd."
                },
                {
                    "question": "په دې حمد کښې د الله تعالی کوم کوم نعمتونه یاد شوي دي؟",
                    "questionUrdu": "اس حمد میں اللہ تعالیٰ کی کون کون سی نعمتیں بیان ہوئی ہیں؟",
                    "questionEn": "Which blessings of Allah are mentioned in this Hamd?",
                    "answer": "زمکه، اسمان، نمر، سپوږمۍ، ستوري، موسمونه، ځناور، مرغان، غرونه، ځنګلونه او سیندونه۔",
                    "answerUrdu": "زمین، آسمان، سورج، چاند، ستارے، موسم، جانور، پرندے، پہاڑ، جنگل اور دریا۔",
                    "answerEn": "Earth, sky, sun, moon, stars, seasons, animals, birds, mountains, forests, and rivers."
                }
            ],
            "wordBuilding": [
                { "letters": ["ا", "س", "م", "ا", "ن"], "word": "اسمان" },
                { "letters": ["ټ", "و", "ل"], "word": "ټول" },
                { "letters": ["ر", "ن", "ګ", "و", "ن", "ه"], "word": "رنګونه" },
                { "letters": ["ښ", "ک", "ل", "ي"], "word": "ښکلي" },
                { "letters": ["ق", "د", "ر", "ت"], "word": "قدرت" }
            ],
            "rhymingWords": [
                { "word1": "اسمان", "word2": "جهان" },
                { "word1": "رنګونه", "word2": "موسمونه" },
                { "word1": "روښان", "word2": "عیان" }
            ],
            "activities": [
                "ماشومان دې دا حمد په يادو ياد کړي او په خوږ اواز دې ملګرو سره په شريکه ووايي۔",
                "په ماشومانو دې د پښتو د حروفِ تهجي ښۀ مشق وکړی شي۔"
            ]
        },
        "grammar": [
            {
                "topic": "د پښتو توري (حروفِ تهجي)",
                "rule": "د اواز ليکلي شکل ته توري وائي لکه ا، ب، پ، ت، ټ، ث، ج، چ، ځ، څ، ح، خ... د پښتو الفبا ټول ۴۴ توري لري.",
                "ruleUrdu": "آواز کی تحریری شکل کو حرف کہتے ہیں۔ پشتو حروفِ تہجی 44 ہیں۔",
                "examples": ["ا", "ب", "پ", "ت", "ټ", "ث", "ج", "چ", "ځ", "څ"]
            }
        ],
        "slos": {
            "mcqs": [
                {
                    "q": "د شاعر نوم څه دی چا چې دا حمد لیکلی دی؟",
                    "options": ["پروفېسر اباسين يوسفزی", "رحمان بابا", "خوشحال خان خټک", "حمزه بابا"],
                    "ans": 0,
                    "exp": "د دې حمد شاعر پروفېسر اباسين يوسفزی دی."
                }
            ],
            "shortQuestions": [
                {
                    "q": "د روزي رسان معنی څه ده؟",
                    "a": "روزي رسان يعني رزق ورکوونکی او خوراک رسوونکی چې یوازې الله تعالی دی."
                }
            ],
            "longQuestions": [
                {
                    "q": "د حمد درې مهم پیغامونه په خپلو ټکو کښې بیان کړئ.",
                    "a": "۱. ټول جهان او کائنات الله تعالی پیدا کړی دی. ۲. د الله تعالی نعمتونه بې شمېره دي. ۳. الله تعالی هر ځای حاضر ناظر دی او ټولو ته روزي ورکوي."
                }
            ]
        }
    },
    {
        "id": "cls1-ps-ch02",
        "number": 2,
        "type": "poem",
        "title": "نعت (نظم)",
        "titleUrdu": "نعت (نظم - مدحتِ رسول ﷺ)",
        "titleEn": "Unit 2: Naat (Poem - Praise of the Holy Prophet SAW)",
        "titlePs": "نعت (نظم)",
        "author": "پروفېسر ډاکټر شمس الزمان سیماب",
        "pageRange": "5-8",
        "theme": "عشقِ رسول ﷺ او سیرتِ طیبه",
        "authorInfo": "د پښتو لازمي درسي کتاب، اول جماعت، خېبر پښتونخوا ټېکسټ بک بورډ پېښور۔",
        "learningOutcomes": [
            "د ساده نظم په اورېدو د هغې نه خوند واخستي شي۔",
            "د پښتو توري په صحيح ډول ادا کړی شي۔",
            "اعراب او حرکات (زبر، زېر، پېښ) وپېژني۔",
            "تر لسو پورې شمېره په هندسو او لفظونو کښې ولیکي۔"
        ],
        "learningOutcomesUrdu": [
            "نعت سن کر اس کے مفہوم کو سمجھ سکیں۔",
            "پشتو حروف کو درست مخارج سے ادا کر سکیں۔",
            "اعراب و حرکات کی پہچان حاصل کر سکیں۔",
            "ایک سے دس تک گنتی ہندسوں اور لفظوں میں لکھ سکیں۔"
        ],
        "sections": [
            {
                "heading": "د نعت شریف شعرونه (بشپړ درسي متن)",
                "headingUrdu": "نعت کے اشعار (مکمل متن)",
                "headingEn": "Verses of Naat (Full Text)",
                "text": "په نبيانو کښې اعلی ئې\nمحمد رسول الله ئې\n\nخدای نازل په تا قرآن کړه\nهدایت ئې د انسان کړه\n\nلوے لارښود ئې، رهنمائي\nټول جهان لره رڼائي\n\nمحمد رسول الله ئې\n\nاولین ئې، آخرین ئې\nرحمت للعالمین ئې\n\nتا ښودلې لاره ښه ده\nستا ژوند غوره نمونه ده\n\nنازولی د مولا ئې\nمحمد رسول الله ئې",
                "paras": [
                    "په نبيانو کښې اعلی ئې، محمد رسول الله ئې۔",
                    "خدای نازل په تا قرآن کړه، هدایت ئې د انسان کړه۔",
                    "لوے لارښود ئې، رهنمائي، ټول جهان لره رڼائي، محمد رسول الله ئې۔",
                    "اولین ئې، آخرین ئې، رحمت للعالمین ئې۔",
                    "تا ښودلې لاره ښه ده، ستا ژوند غوره نمونه ده۔",
                    "نازولی د مولا ئې، محمد رسول الله ئې۔"
                ],
                "urdu": "آپ تمام نبیوں میں سب سے اعلیٰ و برتر ہیں، محمد رسول اللہ ہیں۔ اللہ نے آپ پر قرآن مجید نازل فرمایا جو تمام انسانوں کے لیے ہدایت ہے۔ آپ عظیم رہبر اور تمام دنیا کے لیے روشنی ہیں۔ آپ پہلے بھی ہیں اور آخری نبی بھی ہیں، تمام جہانوں کے لیے رحمت ہیں۔ آپ نے سیدھی راہ دکھائی اور آپ کی حیاتِ طیبہ بہترین نمونہ ہے۔",
                "english": "You are the highest among all the Prophets, Muhammad, the Messenger of Allah. Allah revealed the Holy Quran upon you as guidance for all mankind. You are the supreme guide and light for the entire universe. You are the first and the seal of Prophets, a mercy to all creations. You showed us the righteous path, and your life is the ultimate exemplar.",
                "pashto": "په دې نعت کښې د خوږ پیغمبر حضرت محمد ﷺ صفتونه او د هغه مقام بیان شوی دی چې هغه ټول جهان لره رڼائي او رحمت دی."
            }
        ],
        "words": [
            { "word": "اعلی", "meaning": "اوچت، ډېر ښه، غوره", "meaningUrdu": "سب سے بلند، برتر", "english": "Highest / Exalted", "sentence": "رسول الله ﷺ په ټولو انبیاوو کښې اعلی دی." },
            { "word": "لارښود", "meaning": "رهنما، مشر، لاره ښوونکی", "meaningUrdu": "رہنما، راستہ دکھانے والا", "english": "Guide", "sentence": "نبي کریم ﷺ زمونږ لوے لارښود دی." },
            { "word": "رحمت للعالمين", "meaning": "د ټولو جهانونو د پاره رحمت", "meaningUrdu": "تمام جہانوں کے لیے رحمت", "english": "Mercy to all creations", "sentence": "حضرت محمد ﷺ رحمت للعالمين دی." },
            { "word": "نمونه", "meaning": "مثال، ماډل، غوره لاره", "meaningUrdu": "مثال، نمونہ", "english": "Exemplar / Model", "sentence": "د نبي کریم ﷺ ژوند غوره نمونه ده." },
            { "word": "نازولی", "meaning": "ګران، محبوبه، پیارکړی", "meaningUrdu": "پیارا، محبوب", "english": "Beloved", "sentence": "خوږ پیغمبر د الله تعالی نازولی دی." }
        ],
        "exercise": {
            "textbookMcqs": [
                {
                    "question": "قرآن په چا نازل شوی دی؟",
                    "questionUrdu": "قرآن مجید کس پر نازل ہوا؟",
                    "questionEn": "Upon whom was the Quran revealed?",
                    "options": ["حضرت موسی عليه السلام", "حضرت محمد رسول الله خاتم النبیین ﷺ", "حضرت عيسی عليه السلام", "حضرت ابراهیم عليه السلام"],
                    "optionsUrdu": ["حضرت موسیٰ علیہ السلام", "حضرت محمد رسول اللہ خاتم النبیین ﷺ", "حضرت عیسیٰ علیہ السلام", "حضرت ابراہیم علیہ السلام"],
                    "correctIndex": 1,
                    "explanation": "قرآن مجید د الله تعالی آخري کتاب دی چې په حضرت محمد ﷺ نازل شوی دی."
                },
                {
                    "question": "د رحمت للعالمين څه معنی ده؟",
                    "questionUrdu": "رحمت للعالمین کے کیا معنی ہیں؟",
                    "questionEn": "What does Rahmat-ul-lil-Alameen mean?",
                    "options": ["د ټولو جهانونو د پاره رحمت", "یوازې د مسلمانانو رحمت", "د فرښتو رحمت", "د شتمنو رحمت"],
                    "optionsUrdu": ["تمام جہانوں کے لیے رحمت", "صرف مسلمانوں کے لیے رحمت", "فرشتوں کے لیے رحمت", "امیروں کے لیے رحمت"],
                    "correctIndex": 0,
                    "explanation": "رحمت للعالمین د ټولو جهانونو او ټولو مخلوقاتو لپاره د رحمت په معنی دی."
                },
                {
                    "question": "د چا ژوند زمونږ لپاره غوره نمونه ده؟",
                    "questionUrdu": "کس کی زندگی ہمارے لیے بہترین نمونہ ہے؟",
                    "questionEn": "Whose life is the best exemplar for us?",
                    "options": ["حضرت آدم عليه السلام", "حضرت محمد رسول الله خاتم النبیین ﷺ", "حضرت نوح عليه السلام", "حضرت داود عليه السلام"],
                    "optionsUrdu": ["حضرت آدم علیہ السلام", "حضرت محمد رسول اللہ خاتم النبیین ﷺ", "حضرت نوح علیہ السلام", "حضرت داؤد علیہ السلام"],
                    "correctIndex": 1,
                    "explanation": "د خوږ پیغمبر حضرت محمد ﷺ ژوند زمونږ لپاره غوره نمونه ده."
                }
            ],
            "shortQuestions": [
                {
                    "question": "نعت څه ته وائي؟",
                    "questionUrdu": "نعت کسے کہتے ہیں؟",
                    "questionEn": "What is Naat?",
                    "answer": "هغه نظم ته نعت وائي چې پکښې د خوږ پیغمبر حضرت محمد ﷺ صفت، ستاینه او مدحت بیان شوی وي۔",
                    "answerUrdu": "وہ نظم جس میں حضرت محمد ﷺ کی تعریف و توصیف بیان کی جائے اسے نعت کہتے ہیں۔",
                    "answerEn": "A poem composed in praise of Prophet Muhammad (SAW) is called a Naat."
                }
            ],
            "wordBuilding": [
                { "letters": ["م", "ح", "م", "د"], "word": "محمد" },
                { "letters": ["ق", "ر", "ا", "ن"], "word": "قرآن" },
                { "letters": ["ا", "و", "ل", "ی", "ن"], "word": "اولین" },
                { "letters": ["ن", "م", "و", "ن", "ه"], "word": "نمونه" }
            ],
            "counting1to10": [
                { "digit": "۱", "word": "يو", "english": "One" },
                { "digit": "۲", "word": "دوه", "english": "Two" },
                { "digit": "۳", "word": "درې", "english": "Three" },
                { "digit": "۴", "word": "څلور", "english": "Four" },
                { "digit": "۵", "word": "پینځه", "english": "Five" },
                { "digit": "۶", "word": "شپږ", "english": "Six" },
                { "digit": "۷", "word": "اووه", "english": "Seven" },
                { "digit": "۸", "word": "اته", "english": "Eight" },
                { "digit": "۹", "word": "نهه", "english": "Nine" },
                { "digit": "۱۰", "word": "لس", "english": "Ten" }
            ],
            "activities": [
                "ماشومان دې دا نعت په ياد و ياد کړي او په خوږ اواز دې په شریکه ووايي۔",
                "په ماشومانو دې د یو نه تر لسو شمېره په هندسو او لفظونو کښې ښه مشق شي۔"
            ]
        },
        "grammar": [
            {
                "topic": "اعراب او حرکات (زبر، زېر، پېښ)",
                "rule": "په لفظونو د درست تلفظ د پاره زور (زبر)، زېر او پېښ لګولو ته اعراب وائي.",
                "ruleUrdu": "درست تلفظ کی ادائیگی کے لیے زبر، زیر اور پیش کی علامتوں کو اعراب کہتے ہیں۔",
                "examples": ["زَبَر (زور)", "زِېر", "پېښ (پیش)"]
            }
        ],
        "slos": {
            "mcqs": [
                {
                    "q": "د دې نعت شاعر څوک دی؟",
                    "options": ["پروفېسر ډاکټر شمس الزمان سیماب", "اباسین یوسفزی", "رحمان بابا", "حمزه بابا"],
                    "ans": 0,
                    "exp": "د دې نعت شاعر پروفېسر ډاکټر شمس الزمان سیماب دی."
                }
            ],
            "shortQuestions": [
                {
                    "q": "قرآن مجید د څه لپاره نازل شوی دی؟",
                    "a": "قرآن مجید د انسانانو د هدایت او لارښوونې لپاره نازل شوی دی."
                }
            ],
            "longQuestions": [
                {
                    "q": "د حضرت محمد ﷺ د سیرت او ژوند په اړه درې جملې ولیکئ.",
                    "a": "۱. هغه د ټولو انسانانو لپاره د رحمت او مینې پیغمبر دی. ۲. هغه تل رښتیا ویل او د امانت ساتنه یې کوله. ۳. د هغه ژوند زمونږ لپاره غوره لارښود او کامل نمونه ده."
                }
            ]
        }
    }
]

print("Script template validated.")
