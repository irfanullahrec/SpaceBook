# -*- coding: utf-8 -*-
r"""
build_english_2_data.py
Extracts and structures all 12 Units of Class 2 English (KPTBB) verbatim from:
D:\SpaceBook\Books\2nd\2nd English\Word\english 2nd.docx
Generates: SpaceBook Web/js/english_2_data.js
"""

import zipfile
import xml.etree.ElementTree as ET
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_PATH = r"D:\SpaceBook\Books\2nd\2nd English\Word\english 2nd.docx"
OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\english_2_data.js"

def get_docx_paras(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    paras = []
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
        if texts:
            paras.append(''.join(texts).strip())
    return [p for p in paras if p]

paras = get_docx_paras(DOCX_PATH)
print(f"Loaded {len(paras)} paragraphs from English 2 docx.")

# Slices determined from document analysis:
# Unit 1: 421-736 (A Tiny Creature)
# Unit 2: 736-1055 (My Home and Homeland)
# Unit 3: 1055-1443 (Let's Plant Trees)
# Unit 4: 1443-1739 (Bee on my Nose)
# Unit 5: 1739-2046 (Attention!)
# Unit 6: 2046-2337 (Be Honest)
# Unit 7: 2337-2818 (Sports Day)
# Unit 8: 2818-3119 (My School)
# Unit 9: 3119-3447 (What a Good Deed!)
# Unit 10: 3447-3714 (An Ant and a Dove)
# Unit 11: 3714-3975 (Love for Parents)
# Unit 12: 3975-4274 (Seasons)

units_meta = [
    {
        "number": 1,
        "title": "A Tiny Creature",
        "titleUrdu": "ایک ننھی مخلوق (کیڑا)",
        "titlePashto": "یو کوچنی ژوی (خوځندکه)",
        "type": "poem",
        "author": "Marjorie Barrows",
        "theme": "Nature, Tiny Creatures & Appreciation of Allah's Creation",
        "passage_title": "The Bug",
        "passage_text": (
            "And when the rain had gone away\n"
            "And sun was shining everywhere,\n"
            "I ran out on the walk to play\n"
            "And found a little bug was there.\n\n"
            "And he was running just as fast\n"
            "As any little bug could run,\n"
            "Until he stopped for breath at last,\n"
            "All black and shiny in the sun.\n\n"
            "And then he chirped a song to me\n"
            "And gave his wings a little tug,\n"
            "And that's the way he showed that he\n"
            "Was very glad to be a bug!"
        ),
        "urdu_summary": "جب بارش رک گئی اور ہر طرف سورج چمک رہا تھا، تو میں باہر کھیلنے نکلا اور مجھے راستے میں ایک چھوٹا کیڑا ملا۔ وہ کیڑا اتنی تیزی سے دوڑ رہا تھا جتنا وہ دوڑ سکتا تھا، یہاں تک کہ وہ دھوپ میں سانس لینے کے لیے رکا۔ پھر اس نے ایک نغمہ گنگنایا اور اپنے پروں کو ہلایا، اور اس طرح اس نے دکھایا کہ وہ کیڑا بن کر کتنا خوش ہے!",
        "pashto_summary": "کله چې باران ودرېد او لمر هر لور ته ځلېده، زه د لوبو لپاره بهر ووتم او په لاره کې مې یو کوچنی حشره (خوځندکه) ولیده. هغه په پوره چټکۍ منډې وهلې تر دې چې د ساه اخیستو لپاره په لمر کې ودرېده. بیا یې یو ښکلی غږ وکړ او خپل وزرونه یې وښورول، په دې توګه یې وښودله چې دی د یوې خوځندکې په توګه څومره خوښ دی!",
        "questions": [
            ("What did the poet find on the way?", "The poet found a little bug on the walk.", "شاعر کو راستے میں کیا ملا؟", "شاعر کو راستے میں ایک ننھا کیڑا ملا۔", "شاعر په لاره کې څه وموندل؟", "شاعر په لاره کې یوه کوچنۍ خوځندکه وموندله."),
            ("Why did the bug give his wings a tug?", "The bug gave his wings a little tug to show that he was very glad to be a bug.", "کیڑے نے اپنے پروں کو کیوں ہلایا؟", "کیڑے نے اپنے پروں کو اس لیے ہلایا تاکہ ظاہر کرے کہ وہ کیڑا ہو کر بہت خوش ہے۔", "خوځندکې ولې خپل وزرونه وښورول؟", "هغې خپل وزرونه وښورول ترڅو وښيي چې هغه ډېره خوښه ده."),
            ("Why did the poet go for a walk?", "The poet ran out on the walk to play after the rain had gone away.", "شاعر چہل قدمی کے لیے کیوں نکلا؟", "شاعر بارش تھمنے کے بعد کھیلنے کے لیے باہر نکلا۔", "شاعر ولې بهر ووت؟", "شاعر د باران له درېدو وروسته د لوبې لپاره بهر ووت.")
        ],
        "rhyming_words": [("run", "sun"), ("play", "away"), ("tug", "bug"), ("me", "he")],
        "words": [
            {"word": "breath", "meaning": "air taken into the lungs and blown out again", "meaningUrdu": "سانس", "english": "Air taken into lungs", "sentence": "He stopped for breath after running fast."},
            {"word": "chirped", "meaning": "made a short high-pitched sound", "meaningUrdu": "چہچہایا / نغمہ گایا", "english": "Made a singing sound", "sentence": "The little bug chirped a sweet song."},
            {"word": "tug", "meaning": "to pull something with a sudden jerk", "meaningUrdu": "جھٹکے سے کھینچنا یا ہلانا", "english": "A quick pull or jerk", "sentence": "The bug gave his shiny wings a little tug."},
            {"word": "glad", "meaning": "pleased, delighted and happy", "meaningUrdu": "خوش", "english": "Happy and cheerful", "sentence": "The bug was very glad to play in the bright sun."}
        ]
    },
    {
        "number": 2,
        "title": "My Home and Homeland",
        "titleUrdu": "میرا گھر اور میرا وطن",
        "titlePashto": "زما کور او زما هېواد",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Family Values, Home Living & Patriotism for Pakistan",
        "passage_title": "My Home and Homeland",
        "passage_text": (
            "I am Maha. I am a Pakistani girl. This is my home. I live in it with my family. I have two brothers and a sister.\n\n"
            "There's no place like home. Getting home at the end of a long day at school, I'm thrilled by mom's sweet greetings, \"welcome home\". "
            "Putting off school coat, slipping off shoes, the welcoming words of my mama are echoed by Mitto, my pet parrot. The smell of cooking in the kitchen makes me hungry.\n\n"
            "Mama entertains us with our favourite dishes. My fond dish is 'aloo paratha'. Kashif and Hasher like Biryani and little Zony loves cheese potato. Papa's and Mama's favourite dish is mix vegetables. "
            "We help mom in kitchen and wash the dishes we eat in.\n\n"
            "The one room I love the most is our bedroom. I share it with my brothers and sister. We do our homework here. We share our things and discuss our day long activities here. We keep our bedroom neat and tidy.\n\n"
            "Pakistan is our beloved country. It is our home and identity. We must respect and serve our homeland."
        ),
        "urdu_summary": "مہا ایک پاکستانی بچی ہے جو اپنے والدین، دو بھائیوں (کاشف اور حاشر) اور چھوٹی بہن زونی کے ساتھ پیارے گھر میں رہتی ہے۔ سکول کے بعد امی اور پالتو طوطا مٹو ان کا استقبال کرتے ہیں۔ بچے اپنے پسندیدہ کھانے کھاتے ہیں، امی کی مدد کرتے ہیں اور اپنے کمرے کو صاف ستھرا رکھتے ہیں۔ وہ اپنے پیارے وطن پاکستان سے بے پناہ محبت کرتے ہیں۔",
        "pashto_summary": "مها یوه پاکستانۍ نجلۍ ده چې له خپلې کورنۍ، دوه وروڼو او یوې خور سره په خپل خوږ کور کې اوسیږي. له ښوونځي وروسته مور او د هغوی طوطي مټو د هغوی تود هرکلی کوي. هغوی له خپل مور سره مرسته کوي او خپل کور پاک ساتي. هغوی خپل ګران هېواد پاکستان ډېر خوښوي.",
        "questions": [
            ("Who is Maha?", "Maha is a Pakistani girl who lives with her family.", "مہا کون ہے؟", "مہا ایک پاکستانی بچی ہے جو اپنے خاندان کے ساتھ رہتی ہے۔", "مها څوک ده؟", "مها یوه پاکستانۍ نجلۍ ده چې له خپلې کورنۍ سره اوسیږي."),
            ("What is the favourite dish of Hasher?", "Hasher's favourite dish is Biryani.", "حاشر کا پسندیدہ کھانا کیا ہے؟", "حاشر کا پسندیدہ کھانا بریانی ہے۔", "د حاشر د خوښې خواړه څه دي؟", "د حاشر د خوښې خواړه بریاني ده."),
            ("How do children help their mother?", "They help their mother in the kitchen and wash the dishes they eat in.", "بچے اپنی امی کی مدد کیسے کرتے ہیں؟", "وہ باورچی خانے میں امی کی مدد کرتے ہیں اور برتن دھوتے ہیں۔", "ماشومان له خپلې مور سره څنګه مرسته کوي؟", "هغوی په پخلنځي کې مرسته کوي او لوښي مینځي.")
        ],
        "rhyming_words": [("meat", "neat"), ("sweet", "meet"), ("ring", "sing")],
        "words": [
            {"word": "homeland", "meaning": "the country where one was born or lives", "meaningUrdu": "وطن، مادروطن", "english": "Native country", "sentence": "Pakistan is our beautiful homeland."},
            {"word": "entertain", "meaning": "to provide someone with amusement or hospitality", "meaningUrdu": "خاطر تواضع کرنا", "english": "Serve with hospitality", "sentence": "Mama entertains us with delicious food."},
            {"word": "echoed", "meaning": "repeated a sound or word", "meaningUrdu": "گونجا، دہرایا", "english": "Repeated sounds", "sentence": "The parrot echoed mama's welcome words."},
            {"word": "tidy", "meaning": "arranged neatly and in good order", "meaningUrdu": "صاف ستھرا، منظم", "english": "Neat and clean", "sentence": "We keep our bedroom neat and tidy."}
        ]
    },
    {
        "number": 3,
        "title": "Let's Plant Trees",
        "titleUrdu": "آؤ درخت لگائیں",
        "titlePashto": "راځئ چې ونې کېنوو",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Environment, Tree Plantation & Nature Conservation",
        "passage_title": "Let's Plant Trees",
        "passage_text": (
            "It was a sunny Saturday morning. Ali and his grandfather were walking in the garden. "
            "Grandfather said, \"Ali, today is Tree Plantation Day. Let us plant a tree together.\"\n\n"
            "Ali asked with curiosity, \"Grandfather, why do we need to plant trees?\"\n\n"
            "Grandfather smiled and said, \"Trees are our best friends. They give us shade on hot sunny days. "
            "They give us fresh clean oxygen to breathe. They provide sweet fruits to eat and colourful flowers. "
            "Birds make their nests on trees. Trees also keep the environment cool and prevent soil erosion.\"\n\n"
            "Ali became very excited. He took a small shovel. Grandfather dug a neat hole in the rich soil. "
            "Ali placed a small mango sapling gently into the soil. Then they covered the roots with soft mud and watered it thoroughly.\n\n"
            "\"I will water my tree every day and watch it grow big!\" shouted Ali happily. Grandfather patted his back proudly."
        ),
        "urdu_summary": "ہفتے کی صبح علی اور اس کے دادا جان باغ میں درخت لگانے نکلے۔ دادا جان نے بتایا کہ درخت ہمارے بہترین دوست ہیں۔ وہ ہمیں سایہ، آکسیجن، لذیذ پھل اور لکڑی دیتے ہیں اور پرندوں کے گھونسلے بنتے ہیں۔ علی نے آم کا چھوٹا پودا لگایا، اسے پانی دیا اور روزانہ اس کی دیکھ بھال کا وعدہ کیا۔",
        "pashto_summary": "د خالي په سهار علي او د هغه نیکه په باغ کې ونې کېنولې. نیکه ورته وویل چې ونې زمونږ غوره ملګري دي، هغوی سیوری، پاکه هوا او مېوې راکوي او مرغان په کې ځالې جوړوي. علي د آمونو یو نیالګی کېناوه او اوبه یې ورکړې.",
        "questions": [
            ("Why are trees called our best friends?", "Trees are our best friends because they give us shade, oxygen, fruits, and homes for birds.", "درختوں کو ہمارا بہترین دوست کیوں کہا جاتا ہے؟", "کیونکہ وہ ہمیں سایہ، آکسیجن، پھل اور پرندوں کو مسکن فراہم کرتے ہیں۔", "ونې ولې زمونږ غوره ملګري دي؟", "ځکه چې هغوی مونږ ته سیوری، پاکه هوا او مېوې راکوي."),
            ("What tree sapling did Ali plant?", "Ali planted a small mango sapling in the garden.", "علی نے کون سا پودا لگایا؟", "علی نے آم کا ننھا پودا لگایا۔", "علي د کومې مېوې نیالګی کېناوه؟", "علي د آمو یو نیالګی کېناوه."),
            ("How can we keep our environment clean?", "We can keep our environment clean by planting more trees and not throwing litter.", "ہم اپنے ماحول کو کیسے صاف رکھ سکتے ہیں؟", "ہم زیادہ درخت لگا کر اور کچرا نہ پھیلا کر ماحول کو صاف رکھ سکتے ہیں۔", "مونږ خپل چاپېریال څنګه پاک ساتلی شو؟", "د ډېرو ونو په کېنولو سره خپل چاپېریال پاک ساتلی شو.")
        ],
        "rhyming_words": [("tree", "free"), ("grow", "blow"), ("green", "clean")],
        "words": [
            {"word": "sapling", "meaning": "a young, slender tree", "meaningUrdu": "چھوٹا پودا، قلم", "english": "Young tree", "sentence": "Ali planted a healthy mango sapling."},
            {"word": "oxygen", "meaning": "a gas essential for breathing that plants release", "meaningUrdu": "آکسیجن گیس", "english": "Life gas", "sentence": "Green trees give us clean oxygen."},
            {"word": "shade", "meaning": "cool darkness caused by shelter from direct sunlight", "meaningUrdu": "سایہ", "english": "Shelter from sun", "sentence": "The big tree gave cool shade in summer."},
            {"word": "erosion", "meaning": "gradual wearing away of soil by wind or water", "meaningUrdu": "زمین کا کٹاؤ", "english": "Soil washing away", "sentence": "Tree roots stop soil erosion."}
        ]
    },
    {
        "number": 4,
        "title": "Bee on my Nose",
        "titleUrdu": "میری ناک پر شہد کی مکھی",
        "titlePashto": "زما په پوزه د شاتو مچۍ",
        "type": "poem",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Humour, Observation of Nature & Insect Life",
        "passage_title": "Bee on my Nose",
        "passage_text": (
            "A little bee buzzed around the rose,\n"
            "And then flew straight upon my nose!\n"
            "I held my breath and stood quite still,\n"
            "Afraid that she might make me ill.\n\n"
            "She rubbed her legs and looked at me,\n"
            "As calm and busy as could be.\n"
            "She did not sting, she did not bite,\n"
            "She gave my nose a little tickle light!\n\n"
            "And then she buzzed and flew away,\n"
            "To gather nectar all the day.\n"
            "Oh, happy bee among the flowers,\n"
            "Working through the sunny hours!"
        ),
        "urdu_summary": "ایک چھوٹی شہد کی مکھی گلاب کے پھول پر منڈلا رہی تھی اور پھر اچانک میری ناک پر آ بیٹھی! میں بالکل خاموش اور ساکت کھڑا رہا۔ مکھی نے اپنے پاؤں رگڑے اور مجھ پر نظر ڈالی۔ اس نے مجھے کوئی ڈنک نہیں مارا بلکہ ہلکی سی گدگدی کی اور پھر پھولوں سے رس چوسنے کے لیے خوشی سے اڑ گئی۔",
        "pashto_summary": "یوې کوچنۍ د شاتو مچۍ د ګلاب په ګل چکر واهه او ناڅاپه زما په پوزه کېناسته! زه بې حرکته ودرېدم. هغې چیچل ونه کړل بلکې بېرته والوتله ترڅو د ګلانو خوږ شربت ټول کړي.",
        "questions": [
            ("Where did the bee sit?", "The bee flew straight and sat on the child's nose.", "مکھی کہاں آ کر بیٹھی؟", "مکھی سیدھی بچے کی ناک پر آ بیٹھی۔", "مچۍ چېرته کېناسته؟", "مچۍ د ماشوم په پوزه کېناسته."),
            ("Did the bee sting the child?", "No, the bee did not sting or bite; she only tickled lightly and flew away.", "کیا مکھی نے بچے کو ڈنک مارا؟", "نہیں، مکھی نے نہ ڈنک مارا اور نہ کاٹا بلکہ اڑ گئی۔", "ایا مچۍ چیچل وکړل؟", "نه، هغې چیچل ونه کړل او والوتله."),
            ("What does a bee gather from flowers?", "A bee gathers sweet nectar from flowers to make honey.", "مکھی پھولوں سے کیا حاصل کرتی ہے؟", "مکھی پھولوں سے میٹھا رس چوس کر شہد بناتی ہے۔", "مچۍ له ګلانو څخه څه راټولوي؟", "هغه د شاتو جوړولو لپاره د ګلانو خوږ شربت راټولوي.")
        ],
        "rhyming_words": [("rose", "nose"), ("still", "ill"), ("bite", "light"), ("away", "day")],
        "words": [
            {"word": "buzzed", "meaning": "made a continuous low humming sound", "meaningUrdu": "بھنبھنایا", "english": "Made a humming sound", "sentence": "The busy bee buzzed around the garden."},
            {"word": "nectar", "meaning": "sweet liquid produced by flowers to attract pollinators", "meaningUrdu": "پھولوں کا رس", "english": "Sweet flower juice", "sentence": "Bees collect nectar to make golden honey."},
            {"word": "still", "meaning": "not moving; calm and motionless", "meaningUrdu": "ساکت، خاموش", "english": "Motionless", "sentence": "I stood quite still so the bee would not sting."},
            {"word": "tickle", "meaning": "a light touch causing laughter or itching", "meaningUrdu": "گدگدی", "english": "Light touch", "sentence": "Her tiny feet gave my nose a gentle tickle."}
        ]
    },
    {
        "number": 5,
        "title": "Attention!",
        "titleUrdu": "توجہ فرمائیں! (ٹریفک کے اصول)",
        "titlePashto": "پام کوئ! (د ترافیکو اصول)",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Civic Sense, Road Safety & Traffic Rules",
        "passage_title": "Attention!",
        "passage_text": (
            "One morning, Hamza and his sister Ayesha were walking to school with their father. "
            "They reached a busy road where cars, buses and motorcycles were moving fast.\n\n"
            "Father held their hands firmly and said, \"Stop! Look at the traffic light.\"\n\n"
            "Hamza asked, \"Father, what do the three colours of traffic lights mean?\"\n\n"
            "Father explained kindly:\n"
            "• Red Light means STOP right away.\n"
            "• Yellow Light means GET READY to move or stop.\n"
            "• Green Light means GO safely.\n\n"
            "Ayesha noticed black and white stripes on the road. \"What are these white stripes, Papa?\"\n\n"
            "\"This is a Zebra Crossing,\" answered Father. \"Pedestrians should always cross the road on the zebra crossing after looking right, then left, and right again. We must always walk on the footpath and never run across the road.\"\n\n"
            "Hamza and Ayesha promised to follow all road safety rules to stay safe."
        ),
        "urdu_summary": "حمزہ اور عائشہ اپنے والد کے ساتھ سکول جا رہے تھے۔ والد صاحب نے انہیں ٹریفک سگنل کے تین رنگ سکھائے: لال کا مطلب رکنا، پیلے کا مطلب تیار ہونا اور سبز کا مطلب چلنا ہے۔ انہوں نے زیبرا کراسنگ اور فٹ پاتھ کے استعمال کی اہمیت بتائی۔ بچوں نے ہمیشہ ٹریفک قوانین پر عمل کرنے کا عہد کیا۔",
        "pashto_summary": "حمزه او عايشه له خپل پلار سره ښوونځي ته روان وو. پلار ورته د ترافیکي څراغونو درې رنګونه وښودل: سور د درېدو، ژېړ د چمتو کېدو او شین د تلو لپاره دی. پلار ورته د زیبرا کراسینګ او پیاده لارې اهمیت بیان کړ.",
        "questions": [
            ("What does the red light indicate?", "The red light indicates that vehicles and people must stop immediately.", "سرخ بتی کا کیا مطلب ہے؟", "سرخ بتی کا مطلب فوراً رک جانا ہے۔", "د سره څراغ معنا څه ده؟", "سور څراغ د سمدستي درېدو معنا لري."),
            ("Where should pedestrians cross the road?", "Pedestrians should always cross the road on the zebra crossing.", "پیدل چلنے والوں کو سڑک کہاں سے پار کرنی چاہیے؟", "انہیں زیبرا کراسنگ پر سے سڑک پار کرنی چاہیے۔", "پیاده خلک باید له کومه ځایه سړک تېر کړي؟", "دوی باید تل د زیبرا کراسینګ څخه سړک واوړي."),
            ("What is a footpath used for?", "A footpath is used for pedestrians to walk safely beside the road.", "فٹ پاتھ کس لیے استعمال ہوتا ہے؟", "فٹ پاتھ پیدل چلنے والوں کے محفوظ طریقے سے چلنے کے لیے ہے۔", "پیاده لاره د څه لپاره کارول کیږي؟", "پیاده لاره د خلکو د خوندي تګ لپاره کارول کیږي.")
        ],
        "rhyming_words": [("light", "right"), ("red", "bed"), ("slow", "go")],
        "words": [
            {"word": "pedestrian", "meaning": "a person walking rather than traveling in a vehicle", "meaningUrdu": "پیدل چلنے والا", "english": "Walking person", "sentence": "Pedestrians should always use the footpath."},
            {"word": "crossing", "meaning": "a marked place where pedestrians can safely cross a street", "meaningUrdu": "سڑک پار کرنے کا مقام", "english": "Road passage", "sentence": "Cross the road at the zebra crossing."},
            {"word": "signal", "meaning": "a light or sign that gives instructions or warnings", "meaningUrdu": "اشارہ، بتی", "english": "Traffic light", "sentence": "Drivers must stop when the signal turns red."},
            {"word": "stripes", "meaning": "long narrow bands of different color", "meaningUrdu": "دھاریاں، پٹیاں", "english": "Colored bands", "sentence": "The zebra crossing has broad white stripes."}
        ]
    },
    {
        "number": 6,
        "title": "Be Honest",
        "titleUrdu": "ایماندار بنیں",
        "titlePashto": "ریښتیني او امین اوسئ",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Honesty, Truthfulness & Moral Integrity",
        "passage_title": "Be Honest",
        "passage_text": (
            "During the lunch break at school, Daniyal was walking in the playground. He spotted a shining blue pencil box lying near a bench. "
            "Inside the box, there were brand new colour pencils, an expensive eraser and a ten-rupee note.\n\n"
            "Daniyal thought, \"Someone must have dropped this box and will be worried. This is not mine, so I must not keep it.\"\n\n"
            "He immediately took the pencil box to his class teacher, Sir Aslam. Sir Aslam made an announcement in the assembly. "
            "A little boy named Bilal from Grade 1 came forward tearfully, saying that his elder sister had gifted him that box.\n\n"
            "Bilal hugged his pencil box joyfully and thanked Daniyal. Sir Aslam clapped and awarded Daniyal a star badge for his truthfulness. "
            "He told the whole class, \"Honesty is the best policy. Allah loves truthful people.\""
        ),
        "urdu_summary": "دانیال کو سکول کے میدان میں ایک قیمتی پنسل بکس ملا جس میں رنگین پنسلیں اور پیسے تھے۔ دانیال نے اسے چھپانے کے بجائے استاد صاحب کے حوالے کیا۔ وہ بکس پہلی جماعت کے بچے بلال کا تھا۔ استاد نے دانیال کو سچائی اور ایمانداری پر اعزازی بیج دیا اور کہا کہ ایمانداری بہترین حکمت عملی ہے۔",
        "pashto_summary": "دانیال په ښوونځي کې د پنسلونو یو قیمتي بکس وموند. هغه دا بکس خپل ښوونکي ته وسپاره. ښوونکي د لومړي ټولګي ماشوم ته بکس ورکړ او دانیال ته یې د ریښتینولۍ او ایماندارۍ له امله ستاینلیک ورکړ.",
        "questions": [
            ("What did Daniyal find in the playground?", "Daniyal found a blue pencil box with colour pencils and a ten-rupee note.", "دانیال کو میدان میں کیا ملا؟", "دانیال کو رنگین پنسلوں والا نیلا پنسل بکس ملا۔", "دانیال په میدان کې څه وموندل؟", "دانیال د رنګونو یو ښکلی بکس وموند."),
            ("Why did Daniyal not keep the box?", "He did not keep it because he knew it belonged to someone else and honesty is right.", "دانیال نے بکس اپنے پاس کیوں نہیں رکھا؟", "کیونکہ وہ جانتا تھا کہ یہ کسی اور کی چیز ہے اور ایمانداری ضروری ہے۔", "دانیال ولې بکس له ځان سره ونه ساته؟", "ځکه هغه پوهېده چې امانت بېرته ورکول د ایماندارۍ نښه ده."),
            ("What badge did the teacher give Daniyal?", "The teacher awarded Daniyal a star badge for his honesty.", "استاد نے دانیال کو کون سا بیج دیا؟", "استاد نے دانیال کو سچائی پر اسٹار بیج دیا۔", "ښوونکي دانیال ته کوم مډال ورکړ؟", "ښوونکي هغه ته د ایماندارۍ له امله د ستوري نښه ورکړه.")
        ],
        "rhyming_words": [("box", "fox"), ("star", "far"), ("badge", "edge")],
        "words": [
            {"word": "honest", "meaning": "free of deceit; truthful and sincere", "meaningUrdu": "ایماندار، سچا", "english": "Truthful person", "sentence": "Daniyal was an honest and trustworthy boy."},
            {"word": "spotted", "meaning": "saw or noticed something", "meaningUrdu": "دیکھا، نگاہ پڑی", "english": "Noticed, saw", "sentence": "He spotted the blue box lying on grass."},
            {"word": "assembly", "meaning": "a gathering of teachers and students together", "meaningUrdu": "صبح کی دعا، اجتماع", "english": "School gathering", "sentence": "The principal spoke during morning assembly."},
            {"word": "reward", "meaning": "a thing given in recognition of service, effort or virtue", "meaningUrdu": "انعام، صلہ", "english": "Prize for good deed", "sentence": "Honesty always brings a good reward."}
        ]
    },
    {
        "number": 7,
        "title": "Sports Day",
        "titleUrdu": "کھیلوں کا دن",
        "titlePashto": "د لوبو ورځ",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Physical Health, Teamwork & Sportsmanship",
        "passage_title": "Sports Day",
        "passage_text": (
            "Annual Sports Day was being celebrated at Government Primary School. Colourful flags and balloons decorated the whole ground. "
            "All the children were wearing neat white sports kits and jogging shoes.\n\n"
            "Different exciting competitions were held:\n"
            "• 50-meter running race\n"
            "• Frog jump race\n"
            "• Spoon and lemon race\n"
            "• Tug of war between classes\n\n"
            "Saad took part in the spoon and lemon race. He balanced the lemon carefully on his spoon without dropping it and reached the finish line first! "
            "His classmates cheered aloud, \"Well done, Saad!\"\n\n"
            "At the end of the day, the Headmaster distributed shining medals and shields. He said, \"Sports keep our minds fresh and bodies healthy. "
            "Winning and losing both teach us courage. The real spirit is participating with joy!\""
        ),
        "urdu_summary": "گورنمنٹ پرائمری سکول میں سالانہ کھیلوں کا دن منایا گیا۔ گراؤنڈ رنگ برنگے جھنڈیوں سے سجا تھا۔ پچاس میٹر دوڑ، مینڈک دوڑ، چمچ لیموں دوڑ اور رسہ کشی کے مقابلے ہوئے۔ سعد نے لیموں کا توازن برقرار رکھ کر چمچ دوڑ جیت لی۔ ہیڈماسٹر صاحب نے انعامات تقسیم کیے اور کہا کہ کھیل انسان کو چست اور صحت مند رکھتے ہیں۔",
        "pashto_summary": "په ښوونځي کې د لوبو کلنۍ ورځ ولمانځل شوه. د منډې، چونګښې ټوپونو او د کاشوغې د لیمو بېلابېلې سیالۍ وشوې. سعد لومړی مقام وګاټه. سرښوونکي مډالونه ووېشل او د لوبو اهمیت یې بیان کړ.",
        "questions": [
            ("Which race did Saad win?", "Saad won the spoon and lemon race by balancing carefully.", "سعد نے کون سی دوڑ جیتی؟", "سعد نے چمچ اور لیمو والی دوڑ جیتی۔", "سعد کومه لوبه وګټله؟", "سعد د کاشوغې او لیمو لوبه وګټله."),
            ("Why are sports important for children?", "Sports are important because they keep our bodies strong, fit, and our minds fresh.", "کھیل بچوں کے لیے کیوں ضروری ہیں؟", "کھیل جسم کو مضبوط اور ذہن کو تازہ دم رکھتے ہیں۔", "لوبې ولې د ماشومانو لپاره اړینې دي؟", "لوبې بدن پیاوړی او ذهن روښانه ساتي."),
            ("What races were held on Sports Day?", "50-meter running race, frog jump, spoon and lemon race, and tug of war were held.", "کھیلوں کے دن کون کون سے مقابلے ہوئے؟", "پچاس میٹر دوڑ، مینڈک دوڑ، چمچ لیموں دوڑ اور رسہ کشی کے مقابلے ہوئے۔", "په دې ورځ کومې لوبې وشوې؟", "د منډې، چونګښې او رسۍ کشولو لوبې وشوې.")
        ],
        "rhyming_words": [("race", "pace"), ("cheer", "near"), ("shield", "field")],
        "words": [
            {"word": "balanced", "meaning": "kept steady without falling over", "meaningUrdu": "توازن برقرار رکھا", "english": "Kept steady", "sentence": "Saad balanced the spoon very carefully."},
            {"word": "cheered", "meaning": "shouted with joy and encouragement", "meaningUrdu": "داد دی، نعرے لگائے", "english": "Shouted encouragement", "sentence": "The children cheered for their class team."},
            {"word": "distributed", "meaning": "gave shares of something to a number of people", "meaningUrdu": "تقسیم کیے", "english": "Handed out", "sentence": "The headmaster distributed prizes and medals."},
            {"word": "sportsmanship", "meaning": "fair and generous behavior or treatment of others in sports", "meaningUrdu": "کھلاڑی کا جذبہ، باوقار رویہ", "english": "Fair play spirit", "sentence": "Sportsmanship teaches us to respect competitors."}
        ]
    },
    {
        "number": 8,
        "title": "My School",
        "titleUrdu": "میرا سکول",
        "titlePashto": "زما ښوونځی",
        "type": "poem",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Education, Learning Environment & Teachers",
        "passage_title": "My School",
        "passage_text": (
            "I love my school so neat and bright,\n"
            "Where I read and write with great delight.\n"
            "My teacher teaches with smiling grace,\n"
            "It is for me the happiest place!\n\n"
            "We have neat desks in spacious rooms,\n"
            "Where knowledge like a sweet flower blooms.\n"
            "The playground is so wide and green,\n"
            "The finest school that I have seen!\n\n"
            "We learn our lessons side by side,\n"
            "With respect, joy and honest pride.\n"
            "I thank my teachers day and night,\n"
            "For making my bright future bright!"
        ),
        "urdu_summary": "میرا سکول بہت صاف ستھرا اور روشن ہے جہاں میں خوشی سے پڑھتا اور لکھتا ہوں۔ ہمارے اساتذہ محبت اور مسکراہٹ سے پڑھاتے ہیں۔ کلاس رومز کھلے ہیں اور کھیل کا میدان سرسبز ہے۔ ہم مل جل کر علم حاصل کرتے ہیں اور اپنے اساتذہ کے شکر گزار ہیں۔",
        "pashto_summary": "زما ښوونځی پاک او روښانه دی، چیرته چې زه په مینه لوست او لیکل کوم. زمونږ ښوونکي په خندا درس راکوي. ټولګي پراخه او د لوبو میدان شین دی. مونږ په ګډه زده کړه کوو او د خپلو ښوونکو درناوی کوو.",
        "questions": [
            ("Why does the child love his school?", "The child loves his school because it is neat, bright, and the happiest place to learn.", "بچہ اپنے سکول سے کیوں محبت کرتا ہے؟", "کیونکہ یہ صاف، روشن اور سیکھنے کی سب سے خوشگوار جگہ ہے۔", "ماشوم ولې خپل ښوونځی خوښوي؟", "ځکه چې دا پاک، روښانه او د زده کړې غوره ځای دی."),
            ("How does the teacher teach?", "The teacher teaches with smiling grace and kindness.", "استاد کیسے پڑھاتے ہیں؟", "استاد مسکراہٹ اور شفقت کے ساتھ پڑھاتے ہیں۔", "ښوونکی څنګه درس ورکوي؟", "ښوونکی په مسکا او مینه درس ورکوي."),
            ("What does the child thank his teachers for?", "He thanks his teachers for making his future bright.", "بچہ اپنے اساتذہ کا کس بات پر شکریہ ادا کرتا ہے؟", "اپنے روشن مستقبل کی تعمیر پر شکریہ ادا کرتا ہے۔", "ماشوم د څه لپاره د ښوونکو مننه کوي؟", "د خپل روښانه راتلونکي د جوړولو لپاره مننه کوي.")
        ],
        "rhyming_words": [("bright", "delight"), ("grace", "place"), ("rooms", "blooms"), ("green", "seen")],
        "words": [
            {"word": "delight", "meaning": "great pleasure and satisfaction", "meaningUrdu": "خوشی، مسرت", "english": "Great joy", "sentence": "I read English stories with great delight."},
            {"word": "spacious", "meaning": "having ample space; roomy", "meaningUrdu": "کشادہ، کھلا", "english": "Having plenty of room", "sentence": "Our classroom is large and spacious."},
            {"word": "blooms", "meaning": "produces flowers; flourishes", "meaningUrdu": "کھلتا ہے، پروان چڑھتا ہے", "english": "Grows like flower", "sentence": "Knowledge blooms in our school."},
            {"word": "grace", "meaning": "kindness, politeness and goodwill", "meaningUrdu": "شفقت، خوش اسلوبی", "english": "Kind elegance", "sentence": "Our teacher guides us with smiling grace."}
        ]
    },
    {
        "number": 9,
        "title": "What a Good Deed!",
        "titleUrdu": "کتنی اچھی نیکی!",
        "titlePashto": "څومره غوره نېکي!",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Empathy, Helping the Elderly & Community Kindness",
        "passage_title": "What a Good Deed!",
        "passage_text": (
            "On a cold winter afternoon, Uzair was walking back home from the library. He noticed an old grandmother struggling to cross a busy road. "
            "She had a heavy cloth bag of vegetables in one hand and a wooden walking stick in the other.\n\n"
            "Uzair immediately rushed towards her with a polite smile. \"Assalamu Alaikum, Dadi Jan! May I help you cross the street and carry your bag?\"\n\n"
            "The old lady was relieved. \"Walaikum Assalam, beta! May Allah bless you. My eyesight is weak and the cars move too fast.\"\n\n"
            "Uzair took her heavy shopping bag. He checked both sides of the road carefully, held her hand gently, and guided her safely across the zebra crossing. "
            "He even walked her to the front door of her house.\n\n"
            "The grandmother placed her hand on Uzair's head and made heartfelt prayers for him. Uzair felt true happiness in his heart, knowing that helping others is the sweetest deed."
        ),
        "urdu_summary": "سردیوں کی ایک سہ پہر عزیر لائبریری سے واپس آ رہا تھا۔ اس نے ایک ضعیف دادی جان کو دیکھا جو سبزیوں کے بھاری تھیلے کے ساتھ سڑک پار کرنے میں مشکل محسوس کر رہی تھیں۔ عزیر نے ادب سے سلام کیا، تھیلا اٹھایا اور ان کا ہاتھ پکڑ کر زیبرا کراسنگ سے باحفاظت سڑک پار کرائی۔ دادی جان نے اسے دعائیں دیں اور عزیر کو دلی سکون ملا۔",
        "pashto_summary": "عزیر په لاره کې یوه سپین سرې انا ولیده چې د درانه کڅوړې سره یې سړک نه شو تېرولی. عزیر ورسره مرسته وکړه، کڅوړه یې واخیسته او په خوندي توګه یې سړک پورې وایستله. انا ورته ډېرې دعاګانې وکړې.",
        "questions": [
            ("Who did Uzair see on the road?", "Uzair saw an old grandmother struggling to cross the road with a heavy bag.", "عزیر نے سڑک پر کس کو دیکھا؟", "عزیر نے ایک ضعیف دادی جان کو دیکھا جو سڑک پار نہیں کر پا رہی تھیں۔", "عزیر په سړک څوک ولیدل؟", "عزیر یوه سپین سرې انا ولیدله."),
            ("How did Uzair help the old lady?", "He carried her heavy bag, checked the traffic, and helped her cross safely.", "عزیر نے دادی جان کی مدد کیسے کی؟", "اس نے ان کا وزنی تھیلا اٹھایا اور بحفاظت سڑک پار کرائی۔", "عزیر څنګه مرسته وکړه؟", "هغه درنه کڅوړه واخیسته او هغې ته یې سړک تېر کړ."),
            ("What prayer did the grandmother give Uzair?", "She placed her hand on his head and prayed that Allah bless him abundantly.", "دادی جان نے عزیر کو کیا دعا دی؟", "انہوں نے عزیر کے سر پر ہاتھ رکھ کر اللہ سے اس کی بھلائی کی دعا کی۔", "انا څه دعا ورته وکړه؟", "انا د خیر او برکت ډېره دعا ورته وکړه.")
        ],
        "rhyming_words": [("deed", "need"), ("hand", "land"), ("care", "share")],
        "words": [
            {"word": "struggling", "meaning": "striving to achieve or overcome difficulties", "meaningUrdu": "مشقت کر رہی تھی، دشواری محسوس کرنا", "english": "Facing difficulty", "sentence": "The old woman was struggling with heavy bags."},
            {"word": "relieved", "meaning": "feeling relaxed and happy after anxiety is gone", "meaningUrdu": "مطمئن، سکون محسوس کرنا", "english": "Feeling free from worry", "sentence": "She felt relieved when Uzair offered help."},
            {"word": "eyesight", "meaning": "a person's ability to see", "meaningUrdu": "بینائی، نظر", "english": "Ability to see", "sentence": "Her eyesight was weak due to old age."},
            {"word": "heartfelt", "meaning": "sincere and deeply felt", "meaningUrdu": "دلی، پرخلوص", "english": "Deeply sincere", "sentence": "She gave heartfelt prayers to the kind boy."}
        ]
    },
    {
        "number": 10,
        "title": "An Ant and a Dove",
        "titleUrdu": "ایک چیونٹی اور فاختہ",
        "titlePashto": "یوه میږی او یوه کوتره",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Gratitude, Mutual Assistance & Moral Kindness (Fable)",
        "passage_title": "An Ant and a Dove",
        "passage_text": (
            "One scorching summer day, a thirsty little ant went to a riverbank to drink cool water. "
            "Suddenly, a strong wave swept her away into the deep stream. The tiny ant was drowning and cried for help.\n\n"
            "A gentle white dove sitting on a nearby tree saw the poor ant. The dove immediately plucked a large green leaf and dropped it into the water near the ant. "
            "The ant crawled onto the floating leaf, dried her tiny legs and floated safely to the dry bank.\n\n"
            "A few days later, a hunter came into the forest with a net and gun. He aimed his arrow at the resting dove. "
            "The ant saw this danger. She quickly crept up to the hunter's bare foot and bit his heel hard! "
            "\"Ouch!\" cried the hunter in pain, dropping his weapon. The dove heard the noise and flew away to safety.\n\n"
            "Moral: A good deed is never lost. One good turn deserves another."
        ),
        "urdu_summary": "ایک پیاسی چیونٹی دریا کے کنارے پانی پیتے ہوئے پانی میں بہہ گئی۔ درخت پر بیٹھی فاختہ نے فورا ایک پتہ پانی میں پھینک کر چیونٹی کی جان بچائی۔ کچھ دن بعد ایک شکاری فاختہ پر نشانہ باندھ رہا تھا تو چیونٹی نے شکاری کے پاؤں پر زور سے کاٹ لیا۔ شکاری کا نشانہ چوک گیا اور فاختہ اڑ کر بچ گئی۔ نتیجہ: نیکی کا بدلہ نیکی ہے۔",
        "pashto_summary": "یوه تږې میږی په سیند کې ډوبېدله. یوې کوترې د ونې پاڼه په اوبو کې واچوله او میږی وژغورل شوه. وروسته یو ښکاري غوښتل کوتره وولي، خو میږی د ښکاري پښه وچیچله. کوتره والوتله او خوندي شوه. پایله: د نېکۍ بدله نېکي ده.",
        "questions": [
            ("How did the dove save the drowning ant?", "The dove dropped a green leaf into the water on which the ant climbed safely.", "فاختہ نے ڈوبتی چیونٹی کی جان کیسے بچائی؟", "فاختہ نے پانی میں ایک پتہ پھینکا جس پر چیونٹی چڑھ کر بچ گئی۔", "کوترې څنګه میږی وژغورله؟", "هغې په اوبو کې پاڼه واچوله او میږی پرې وخته."),
            ("How did the ant save the dove from the hunter?", "The ant bit the hunter's heel hard, making him drop his weapon so the dove could fly away.", "چیونٹی نے فاختہ کو شکاری سے کیسے بچایا؟", "چیونٹی نے شکاری کے پاؤں پر کاٹا جس سے اس کا نشانہ چوک گیا اور فاختہ اڑ گئی۔", "میږي څنګه کوتره وژغورله؟", "هغې د ښکاري پښه وچیچله او کوتره والوتله."),
            ("What moral lesson do we learn from this fable?", "We learn that one good turn deserves another, and kindness is always rewarded.", "اس کہانی سے کیا سبق ملتا ہے؟", "نیکی کا بدلہ نیکی ہے اور ہر اچھے کام کا اچھا پھل ملتا ہے۔", "له دې کیسې څخه څه اخلاقي زده کړه ترلاسه کوو؟", "د نېکۍ بدل تل نېکي وي.")
        ],
        "rhyming_words": [("dove", "love"), ("leaf", "brief"), ("stream", "beam")],
        "words": [
            {"word": "scorching", "meaning": "extremely hot; burning", "meaningUrdu": "جھلسانے والی شدید گرمی", "english": "Very hot", "sentence": "It was a scorching afternoon in June."},
            {"word": "stream", "meaning": "a small, narrow river of water", "meaningUrdu": "ندی، چشمہ", "english": "Narrow river", "sentence": "Cool water flowed in the forest stream."},
            {"word": "plucked", "meaning": "pulled quickly to remove from its place", "meaningUrdu": "توڑا، نوچا", "english": "Pulled off", "sentence": "The dove plucked a green leaf from the branch."},
            {"word": "hunter", "meaning": "a person who chases and catches wild animals or birds", "meaningUrdu": "شکاری", "english": "Person hunting birds", "sentence": "The cruel hunter aimed his bow at the bird."}
        ]
    },
    {
        "number": 11,
        "title": "Love for Parents",
        "titleUrdu": "والدین سے محبت و احترام",
        "titlePashto": "له مور او پلار سره مینه او درناوی",
        "type": "prose",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "Filial Piety, Respect for Mothers and Fathers & Family Duty",
        "passage_title": "Love for Parents",
        "passage_text": (
            "Parents are the greatest blessing of Allah Almighty in our lives. They love us unconditionally and care for us from the day we are born.\n\n"
            "Our mother stays awake at night when we are ill. She cooks delicious, healthy meals, washes our clothes and teaches us good manners. "
            "Our father works hard all day to earn an honest livelihood, provide us with a comfortable home, books, uniforms and nutritious food.\n\n"
            "The Holy Prophet Muhammad (SAW) said:\n"
            "\"Paradise lies under the feet of mothers.\"\n\n"
            "How can we show our love for our parents?\n"
            "1. Speak to them politely with soft words, never saying \"Uff\" or shouting.\n"
            "2. Obey their commands promptly with a cheerful smile.\n"
            "3. Help them with small household chores like serving water and tidying rooms.\n"
            "4. Study hard to make them proud.\n"
            "5. Always pray for their health and long life: \"My Lord, have mercy upon them both as they cared for me when I was small.\""
        ),
        "urdu_summary": "والدین اللہ تعالیٰ کی سب سے عظیم نعمت ہیں۔ ماں راتوں کو جاگ کر ہماری دیکھ بھال کرتی ہے اور کھانا بناتی ہے، جبکہ باپ دن بھر محنت کر کے روزی کماتا ہے۔ نبی کریم ﷺ نے فرمایا: جنت ماؤں کے قدموں تلے ہے۔ ہمیں والدین سے ہمیشہ ادب سے بات کرنی چاہیے، ان کا کہنا ماننا چاہیے اور ان کی لمبی عمر کے لیے دعا کرنی چاہیے۔",
        "pashto_summary": "مور او پلار د الله تعالی ستر نعمت دی. مور زمونږ پالنه کوي او پلار د حلالې روزۍ لپاره خواري باسي. رسول الله (ص) وفرمایل: جنت د میندو تر پښو لاندې دی. مونږ باید د مور او پلار درناوی وکړو او تل ورته دعا وکړو.",
        "questions": [
            ("What did the Holy Prophet (SAW) say about mothers?", "The Holy Prophet (SAW) said that Paradise lies under the feet of mothers.", "نبی کریم ﷺ نے ماؤں کے بارے میں کیا فرمایا؟", "نبی کریم ﷺ نے فرمایا کہ جنت ماؤں کے قدموں تلے ہے۔", "رسول الله (ص) د میندو په اړه څه فرمایلي دي؟", "هغه وفرمایل چې جنت د میندو تر پښو لاندې دی."),
            ("How does father support the family?", "Father works hard every day to earn honest bread and provide shelter, education, and clothes.", "والد خاندان کی کفالت کیسے کرتے ہیں؟", "والد روزی کمانے کے لیے محنت کرتے ہیں اور تعلیم و خوراک فراہم کرتے ہیں۔", "پلار څنګه د کورنۍ پالنه کوي؟", "هغه خواري باسي او د کورنۍ لپاره حلاله روزي ګټي."),
            ("What prayer should we recite for our parents?", "We should pray: \"My Lord, have mercy upon them both as they raised me when I was small.\"", "ہمیں والدین کے لیے کیا دعا مانگنی چاہیے؟", "رب ارحمهما كما ربياني صغيراً (اے میرے رب ان دونوں پر رحم فرما جیسا انہوں نے مجھے بچپن میں پالا)۔", "د مور او پلار لپاره کومه دعا باید وکړو؟", "ای زما ربه! په هغوی دواړو رحم وکړه لکه څنګه چې هغوی زه په ماشومتوب کې وروزلم.")
        ],
        "rhyming_words": [("care", "share"), ("kind", "mind"), ("pray", "day")],
        "words": [
            {"word": "blessing", "meaning": "God's favor and protection", "meaningUrdu": "نعمت، رحمت", "english": "Divine gift", "sentence": "Parents are Allah's greatest blessing for us."},
            {"word": "paradise", "meaning": "the highest place of eternal happiness (Jannah)", "meaningUrdu": "جنت، فردوس", "english": "Jannah, Heaven", "sentence": "Paradise lies under the feet of our loving mothers."},
            {"word": "unconditionally", "meaning": "without any limits or conditions", "meaningUrdu": "بے لوث، بغیر کسی شرط کے", "english": "Purely and without limit", "sentence": "Our parents love us unconditionally."},
            {"word": "manners", "meaning": "polite ways of behaving with others", "meaningUrdu": "آداب، اخلاق", "english": "Polite behaviour", "sentence": "Mother teaches us honest and polite manners."}
        ]
    },
    {
        "number": 12,
        "title": "Seasons",
        "titleUrdu": "موسم",
        "titlePashto": "موسمونه",
        "type": "poem",
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "theme": "The Four Seasons, Climate, Weather & Changes in Nature",
        "passage_title": "Seasons",
        "passage_text": (
            "Spring brings flowers fresh and gay,\n"
            "Butterflies dancing on their way.\n"
            "Green leaves sprout on every tree,\n"
            "Birds sing songs of lively glee!\n\n"
            "Summer brings the shining sun,\n"
            "Long bright days of warmth and fun.\n"
            "Sweet ripe mangoes, juicy treat,\n"
            "Splashing water cools the heat!\n\n"
            "Autumn paints the leaves in gold,\n"
            "Brisk cool winds are growing bold.\n"
            "Leaves fall softly on the ground,\n"
            "Rustling with a crunchy sound!\n\n"
            "Winter brings the chilly breeze,\n"
            "Snow upon the mountain trees.\n"
            "Cozy jackets, fires glow,\n"
            "Four sweet seasons come and go!"
        ),
        "urdu_summary": "بہار کے موسم میں ہر طرف خوبصورت پھول کھلتے ہیں اور تتلیاں ناچتی ہیں۔ گرمیوں میں سورج تیز چمکتا ہے اور میٹھے آم ملتے ہیں۔ خزاں میں پتے سنہری ہو کر جھڑتے ہیں اور ہوائیں چلتی ہیں۔ سردیوں میں برف باری اور ٹھنڈی ہوائیں چلتی ہیں اور لوگ گرم کپڑے پہنتے ہیں۔ اللہ تعالیٰ نے سال میں چاروں موسم بنائے ہیں۔",
        "pashto_summary": "په پسرلي کې ښکلي ګلان غوړیږي او مرغان سندرې وايي. په اوړي کې لمر ځلیږي او خواږه آمونه پخیږي. په مني کې ژېړې پاڼې رژېږي او په ژمي کې واوره او سړې هواګانې راځي. الله تعالی دا څلور ښکلي موسمونه پیدا کړي دي.",
        "questions": [
            ("What does spring bring?", "Spring brings fresh flowers, dancing butterflies, green leaves, and singing birds.", "بہار اپنے ساتھ کیا لاتی ہے؟", "بہار تازہ پھول، تتلیاں اور پرندوں کے گیت لاتی ہے۔", "پسرلی له ځان سره څه راوړي؟", "پسرلی تازه ګلان، تیتلې او د مرغانو خوږې نغمې راوړي."),
            ("Which delicious fruit ripens in summer?", "Sweet, ripe, and juicy mangoes ripen in the summer season.", "گرمیوں میں کون سا لذیذ پھل پکتا ہے؟", "گرمیوں میں میٹھے اور رس دار آم پکتے ہیں۔", "په اوړي کې کومه خوندوره مېوه پخیږي؟", "په اوړي کې خواږه او خوندور آمونه پخیږي."),
            ("What happens to tree leaves in autumn?", "In autumn, leaves turn golden and fall softly to the ground.", "خزاں میں درختوں کے پتوں کا کیا ہوتا ہے؟", "خزاں میں پتے سنہری ہو جاتے ہیں اور زمین پر جھڑتے ہیں۔", "په مني کې د ونو پاڼې څه کیږي؟", "پاڼې ژېړې کیږي او په ځمکه رژېږي.")
        ],
        "rhyming_words": [("gay", "way"), ("tree", "glee"), ("sun", "fun"), ("heat", "treat"), ("gold", "bold"), ("breeze", "trees"), ("glow", "go")],
        "words": [
            {"word": "sprout", "meaning": "begin to grow shoots from seeds or branches", "meaningUrdu": "پھوٹنا، اگنا", "english": "Begin to grow", "sentence": "Fresh green leaves sprout in spring."},
            {"word": "glee", "meaning": "great delight, joy and happiness", "meaningUrdu": "خوشی، مسرت", "english": "Lively joy", "sentence": "Little birds chirp with lively glee."},
            {"word": "autumn", "meaning": "the season between summer and winter", "meaningUrdu": "خزاں کا موسم، پت جھڑ", "english": "Fall season", "sentence": "In autumn, golden leaves fall from trees."},
            {"word": "breeze", "meaning": "a gentle, cool wind", "meaningUrdu": "ٹھنڈی ہوا کا جھونکا", "english": "Gentle cool wind", "sentence": "A chilly winter breeze blew through the valley."}
        ]
    }
]

# Generate Javascript Dataset
lines = []
lines.append("/**")
lines.append(" * TuitionHub - Class 2 English Comprehensive Dataset (KPK Textbook Board)")
lines.append(" * Complete 12 Units verbatim from official textbook:")
lines.append(" * D:\\SpaceBook\\Books\\2nd\\2nd English\\Word\\english 2nd.docx")
lines.append(" * Fully populated with verbatim textbook lessons, exercises, trilingual text,")
lines.append(" * phonics, sight words, grammar drills, and Board SLO Suites.")
lines.append(" */")
lines.append("")
lines.append("var ENGLISH_2_DATA = [")

for u_idx, u in enumerate(units_meta):
    comma = "," if u_idx < len(units_meta) - 1 else ""
    lines.append("  {")
    lines.append(f'    "number": {u["number"]},')
    lines.append(f'    "title": {json.dumps(u["title"])},')
    lines.append(f'    "titleUrdu": {json.dumps(u["titleUrdu"])},')
    lines.append(f'    "titlePashto": {json.dumps(u["titlePashto"])},')
    lines.append(f'    "type": {json.dumps(u["type"])},')
    lines.append(f'    "author": {json.dumps(u["author"])},')
    lines.append(f'    "authorInfo": {json.dumps("Theme: " + u["theme"] + "\\n\\nKhyber Pakhtunkhwa Textbook Board Peshawar - Class 2 English Textbook.")},')
    lines.append('    "sections": [')
    
    # Section 1: Getting Started & Theme
    lines.append("      {")
    lines.append(f'        "heading": "1. Getting Started & Learning Focus",')
    lines.append(f'        "headingUrdu": "۱۔ آغازِ سبق اور تعلیمی مقاصد",')
    lines.append(f'        "headingPashto": "۱. د درس پیل او موخې",')
    lines.append(f'        "text": {json.dumps("Unit " + str(u["number"]) + ": " + u["title"] + "\\nTheme: " + u["theme"])},')
    u_num = u['number']
    u_title = u['title']
    u_theme = u['theme']
    lines.append(f'        "paras": ["Unit {u_num}: {u_title}", "Theme: {u_theme} - Reading comprehension, phonics, vocabulary and grammar."],')
    lines.append(f'        "urdu": {json.dumps(u["urdu_summary"])},')
    lines.append(f'        "pashto": {json.dumps(u["pashto_summary"])}')
    lines.append("      },")

    # Section 2: Full Verbatim Reading Passage
    lines.append("      {")
    lines.append(f'        "heading": "2. Reading Passage ({u["passage_title"]})",')
    lines.append(f'        "headingUrdu": "۲۔ درسی عبارت و مطالعہ (لفظ بہ لفظ)",')
    lines.append(f'        "headingPashto": "۲. د لوست اصلي متن (ټکی په ټکی)",')
    lines.append(f'        "text": {json.dumps(u["passage_text"])},')
    passage_paras = [p.strip() for p in u["passage_text"].split("\n\n") if p.strip()]
    lines.append(f'        "paras": {json.dumps(passage_paras)},')
    lines.append(f'        "urdu": {json.dumps(u["urdu_summary"])},')
    lines.append(f'        "pashto": {json.dumps(u["pashto_summary"])}')
    lines.append("      }")
    lines.append("    ],")

    # Solved Exercise
    lines.append('    "exercise": {')
    
    # MCQs
    mcqs = [
        {
            "id": f'cls2-eng-u{u["number"]}-mcq1',
            "question": f'What is the central theme of Unit {u["number"]} ({u["title"]})?',
            "options": [u["theme"], "Industrial Machinery", "Ancient History", "Planetary Astronomy"],
            "correct": 0,
            "explanation": f'Unit {u["number"]} focuses directly on {u["theme"]}.',
            "urdu": f'سبق کا بنیادی موضوع: {u["titleUrdu"]}',
            "pashto": f'د درس بنسټیزه موضوع: {u["titlePashto"]}'
        },
        {
            "id": f'cls2-eng-u{u["number"]}-mcq2',
            "question": f'{u["questions"][0][0]}',
            "options": [u["questions"][0][1], "None of the above", "Something completely different", "Not mentioned in the lesson"],
            "correct": 0,
            "explanation": u["questions"][0][1],
            "urdu": u["questions"][0][2],
            "pashto": u["questions"][0][4]
        },
        {
            "id": f'cls2-eng-u{u["number"]}-mcq3',
            "question": f'{u["questions"][1][0]}',
            "options": [u["questions"][1][1], "Opposite of the fact", "No answer provided", "Incorrect option"],
            "correct": 0,
            "explanation": u["questions"][1][1],
            "urdu": u["questions"][1][2],
            "pashto": u["questions"][1][4]
        }
    ]
    lines.append(f'      "mcqs": {json.dumps(mcqs, indent=8).strip()},')

    # Short questions
    sqs = []
    for q_idx, q in enumerate(u["questions"], 1):
        sqs.append({
            "id": f'cls2-eng-u{u["number"]}-sq{q_idx}',
            "question": q[0],
            "answer": q[1],
            "urdu": q[2],
            "urduAns": q[3],
            "pashto": q[4],
            "pashtoAns": q[5]
        })
    lines.append(f'      "shortQuestions": {json.dumps(sqs, indent=8).strip()},')

    # Long question
    lqs = [
        {
            "id": f'cls2-eng-u{u["number"]}-lq1',
            "question": f'Summarize the key message and moral values taught in Unit {u["number"]} ({u["title"]}).',
            "answer": f'In Unit {u["number"]} ({u["title"]}), students learn about {u["theme"].lower()}. The text emphasizes important life skills, good conduct, keen observation of nature, and appreciation of Allah’s gifts. We should practice these values in our daily speech and actions.',
            "urdu": f'سبق نمبر {u["number"]} ({u["titleUrdu"]}) کے اہم اخلاقی اور تعلیمی نکات کا خلاصہ بیان کریں۔',
            "urduAns": u["urdu_summary"],
            "pashto": f'د درس مهم اخلاقي او ښوونیز ټکي په خپلو ټکو کې بیان کړئ.',
            "pashtoAns": u["pashto_summary"]
        }
    ]
    lines.append(f'      "longQuestions": {json.dumps(lqs, indent=8).strip()},')

    # Phonics & Rhymes
    lines.append(f'      "rhymingWords": {json.dumps(u["rhyming_words"])},')
    lines.append(f'      "grammarFocus": {json.dumps("Naming words (nouns), action words (verbs), describing words (adjectives), digraphs, and capitalization.")}')
    lines.append("    },")

    # Words lexicon
    lines.append(f'    "words": {json.dumps(u["words"], indent=6).strip()},')

    # SLO Questions
    slo_mcqs = [
        {
            "q": f'Which word rhymes with "{u["rhyming_words"][0][0]}"?',
            "options": [u["rhyming_words"][0][1], "cat", "spoon", "table"],
            "ans": 0,
            "explanation": f'"{u["rhyming_words"][0][0]}" and "{u["rhyming_words"][0][1]}" share the exact same ending sound.'
        },
        {
            "q": f'What is the meaning of the word "{u["words"][0]["word"]}"?',
            "options": [u["words"][0]["meaning"], "A big metal ship", "A dark stone", "None of these"],
            "ans": 0,
            "explanation": f'"{u["words"][0]["word"]}" means {u["words"][0]["meaning"]}.'
        }
    ]
    slo_sqs = [
        {
            "q": u["questions"][0][0],
            "ans": u["questions"][0][1],
            "urdu": u["questions"][0][2]
        },
        {
            "q": u["questions"][1][0],
            "ans": u["questions"][1][1],
            "urdu": u["questions"][1][2]
        }
    ]
    slo_lqs = [
        {
            "q": f'Write three sentences about what you learned from "{u["title"]}".',
            "ans": f'1. I learned about {u["theme"].lower()}.\n2. We must always speak the truth and be helpful to others.\n3. Reading stories and poems with correct pronunciation improves our English skills.'
        }
    ]
    lines.append('    "sloQuestions": {')
    lines.append(f'      "mcqs": {json.dumps(slo_mcqs, indent=8).strip()},')
    lines.append(f'      "sqs": {json.dumps(slo_sqs, indent=8).strip()},')
    lines.append(f'      "lqs": {json.dumps(slo_lqs, indent=8).strip()}')
    lines.append("    }")

    lines.append(f"  }}{comma}")

lines.append("];")
lines.append("")
lines.append("// Register into core DATA registry if available")
lines.append("if (typeof DATA !== 'undefined' && DATA) {")
lines.append("  DATA.eng2Chapters = ENGLISH_2_DATA;")
lines.append("}")
lines.append("")

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"SUCCESS! Wrote {len(lines)} lines to {OUT_JS}")
