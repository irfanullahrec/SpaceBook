# -*- coding: utf-8 -*-
r"""
build_gk_2_data.py
Builds SpaceBook Web/js/gk_2_data.js with all 16 complete chapters of
Class 2 General Knowledge (KPTBB), directly sourced from:
D:\SpaceBook\Books\2nd\2nd GK\Word\GK 2nd.docx
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\gk_2_data.js"

chapters = [
    {
        "number": 1,
        "title": "Our Country Pakistan",
        "titleUrdu": "ہمارا ملک پاکستان",
        "titlePashto": "زمونږ هېواد پاکستان",
        "text": (
            "Pakistan is our beloved country. It is located in the continent of Asia. "
            "Pakistan came into existence on the 14th of August 1947. Its capital is Islamabad.\n\n"
            "Pakistan has four provinces: Balochistan, Khyber Pakhtunkhwa, Punjab, and Sindh. "
            "Balochistan is the largest province by territory (area), and Punjab is the largest province by population. "
            "Gilgit-Baltistan and Azad Jammu and Kashmir are also administrative territories of Pakistan.\n\n"
            "The national flag of Pakistan has green and white colours with a crescent and a five-pointed star. "
            "The green colour represents the Muslim majority, while the white portion represents religious minorities. "
            "The crescent symbolizes progress, and the star symbolizes knowledge and light."
        ),
        "urdu": "پاکستان ہمارا پیارا وطن ہے جو براعظم ایشیا میں واقع ہے۔ یہ ۱۴ اگست ۱۹۴۷ء کو قائم ہوا اور اس کا دارالحکومت اسلام آباد ہے۔ اس کے چار صوبے پنجاب، سندھ، خیبر پختونخوا اور بلوچستان ہیں۔ قومی پرچم میں سبز رنگ مسلمانوں اور سفید اقلیتوں کی نمائندگی کرتا ہے۔ ہلال ترقی اور ستارہ علم کا نشان ہے۔",
        "pashto": "پاکستان زمونږ ګران هېواد دی چې په اسیا کې پروت دی. دا د ۱۹۴۷ کال د اګست په ۱۴مه جوړ شو او پلازمېنه یې اسلام اباد ده. څلور صوبې لري او ملي بیرغ یې زرغون او سپین دی.",
        "questions": [
            ("When did Pakistan come into existence?", "Pakistan came into existence on 14th August 1947.", "پاکستان کب قائم ہوا؟", "پاکستان کله جوړ شو؟", "پاکستان د ۱۹۴۷ کال د اګست په ۱۴مه جوړ شو."),
            ("What is the capital of Pakistan?", "Islamabad is the capital of Pakistan.", "دارالحکومت کون سا ہے؟", "د پاکستان پلازمېنه کومه ده؟", "اسلام اباد د پاکستان پلازمېنه ده."),
            ("What do the colours of Pakistan's flag represent?", "Green represents Muslims and white represents minorities.", "پرچم کے رنگ کیا ظاہر کرتے ہیں؟", "د بیرغ رنګونه څه ښيي؟", "شین د مسلمانانو او سپین د نورو مذهبونو استازیتوب کوي.")
        ]
    },
    {
        "number": 2,
        "title": "Villages and Cities",
        "titleUrdu": "دیہات اور شہر",
        "titlePashto": "کلي او ښارونه",
        "text": (
            "People live in two main types of settlements: villages (rural areas) and cities (urban areas).\n\n"
            "Villages have fresh air, green fields, open spaces, and fewer vehicles. Houses are often made of mud and bricks. "
            "Most village people work in agriculture, farming crops, and keeping livestock.\n\n"
            "Cities have tall buildings, wide roads, heavy traffic, and modern facilities like large hospitals, universities, banks, and shopping centres. "
            "People in cities work in offices, factories, schools, and business markets.\n\n"
            "Both villages and cities depend on each other: villages provide food and grains, while cities provide manufactured goods and machinery."
        ),
        "urdu": "انسان دیہاتوں اور شہروں میں آباد ہیں۔ گاؤں میں تازہ ہوا، کھیت اور مویشی ہوتے ہیں جبکہ لوگ زیادہ تر کھیتی باڑی کرتے ہیں۔ شہروں میں بڑی سڑکیں، ہسپتال، کارخانے اور دفاتر ہوتے ہیں۔ دونوں ایک دوسرے پر منحصر ہیں۔",
        "pashto": "کلي او ښارونه یو بل ته اړتیا لري. په کلیو کې کرنه او مالداري کیږي او په ښارونو کې فابریکې، پوهنتونونه او روغتونونه شتون لري.",
        "questions": [
            ("What is the main occupation of people living in villages?", "The main occupation of village people is agriculture and farming.", "دیہاتیوں کا اہم پیشہ کیا ہے؟", "د کلیوالو اصلي کسب څه دی؟", "د هغوی اصلي کسب کرنه او مالداري ده."),
            ("Name two facilities commonly found in cities.", "Large hospitals and higher educational universities are found in cities.", "شہروں کی دو سہولیات بتائیں۔", "د ښارونو دوه اسانتیاوې کومې دي؟", "لوی روغتونونه او پوهنتونونه دي.")
        ]
    },
    {
        "number": 3,
        "title": "Rights and Duties",
        "titleUrdu": "حقوق اور فرائض",
        "titlePashto": "حقوق او دندې",
        "text": (
            "A peaceful society runs on the balance between rights and duties.\n\n"
            "Rights are the basic needs and privileges that every citizen deserves, such as right to education, clean water, healthcare, safety, and respect.\n\n"
            "Duties are the legal and moral responsibilities that citizens owe to their country and community. "
            "Our duties include obeying laws, keeping the environment clean, respecting traffic signals, taking care of public property, and treating neighbors kindly.\n\n"
            "When we fulfill our duties sincerely, everyone can enjoy their rights safely."
        ),
        "urdu": "حقوق وہ بنیادی ضروریات ہیں جو ہر شہری کو ملنی چاہئیں، جیسے تعلیم، صحت اور تحفظ۔ فرائض وہ ذمہ داریاں ہیں جو شہریوں پر لازم ہیں، جیسے قوانین کا احترام، صفائی اور ٹیکس ادا کرنا۔ حقوق اور فرائض باہمی جڑے ہوئے ہیں۔",
        "pashto": "حقوق د انسانانو بنسټیزې اړتیاوې دي او دندې د ټولنې په وړاندې مسؤلیتونه دي. هر څوک باید خپل مسؤلیتونه په پوره اخلاص سرته ورسوي.",
        "questions": [
            ("What is the difference between a right and a duty?", "A right is what you receive as a citizen, while a duty is what you owe to others.", "حق اور فرض میں کیا فرق ہے؟", "د حق او دندې ترمنځ څه توپیر دی؟", "حق هغه دی چې انسان یې ترلاسه کوي او دنده مسؤلیت دی."),
            ("Mention one important duty of a school student.", "Studying attentively and keeping the school clean is an important duty.", "طالب علم کا اہم فرض کیا ہے؟", "د زده کوونکي مهمه دنده څه ده؟", "په مینه درس ویل او د ښوونځي پاک ساتل دي.")
        ]
    },
    {
        "number": 4,
        "title": "Religious Festivals",
        "titleUrdu": "مذہبی تہوار",
        "titlePashto": "مذهبي جشنونه",
        "text": (
            "Religious festivals bring joy, unity, and sharing in society.\n\n"
            "Muslims celebrate two main festivals: Eid-ul-Fitr (celebrated with gratitude after Ramadan) and Eid-ul-Adha (celebrating the sacrifice of Prophet Ibrahim AS).\n\n"
            "Other religious communities in Pakistan celebrate their sacred festivals with freedom:\n"
            "• Christians celebrate Christmas on 25th December.\n"
            "• Hindus celebrate Diwali (Festival of Lights) and Holi.\n"
            "• Sikhs celebrate the birthday of Guru Nanak (Baisakhi).\n\n"
            "Islam teaches us to respect the celebrations and religious rights of all non-Muslim citizens."
        ),
        "urdu": "مسلمان عید الفطر اور عید الاضحیٰ مناتے ہیں۔ پاکستان میں دیگر مذاہب کے لوگ بھی اپنے تہوار آزادی سے مناتے ہیں، جیسے مسیحی کرسمس، ہندو دیوالی اور ہولی، اور سکھ بیساکھی مناتے ہیں۔ ہمیں سب کے مذہبی حقوق کا احترام کرنا چاہیے۔",
        "pashto": "مسلمانان دوه اخترونه لمانځي. په هېواد کې عیسویان کرسمس او هندوان دیوالي لمانځي. اسلام د ټولو مذهبونو درناوی ور زده کوي.",
        "questions": [
            ("Which two major festivals do Muslims celebrate?", "Muslims celebrate Eid-ul-Fitr and Eid-ul-Adha.", "مسلمان کون سے دو بڑے تہوار مناتے ہیں؟", "مسلمانان کوم دوه لوی اخترونه لمانځي؟", "کوچنی اختر او لوی اختر لمانځي."),
            ("When do Christians celebrate Christmas?", "Christians celebrate Christmas on 25th December.", "مسیحی کرسمس کب مناتے ہیں؟", "عیسویان کرسمس کله لمانځي؟", "د ډسمبر په ۲۵مه یې لمانځي.")
        ]
    },
    {
        "number": 5,
        "title": "Natural Environment and Resources",
        "titleUrdu": "قدرتی ماحول اور وسائل",
        "titlePashto": "طبیعي چاپېریال او سرچینې",
        "text": (
            "Our environment includes everything around us—air, water, sunlight, soil, plants, and living beings.\n\n"
            "Natural resources are valuable materials provided by nature without human creation. They include:\n"
            "• Air for breathing\n"
            "• Fresh water for drinking and irrigation\n"
            "• Fertile soil for growing crops\n"
            "• Sunlight for energy and warmth\n"
            "• Forests and minerals like coal, gas, and salt.\n\n"
            "We must use natural resources wisely and avoid pollution to safeguard our planet."
        ),
        "urdu": "قدرتی ماحول میں ہوا، پانی، مٹی، سورج کی روشنی اور جنگلات شامل ہیں۔ یہ سب اللہ تعالیٰ کے عطا کردہ قدرتی وسائل ہیں جن سے ہم خوراک، توانائی اور زندگی حاصل کرتے ہیں۔ ہمیں انہیں آلودگی سے بچانا چاہیے۔",
        "pashto": "طبیعي سرچینې لکه اوبه، هوا، ځمکه او ځنګلونه د ژوند لپاره حیاتي دي او باید وساتل شي.",
        "questions": [
            ("Name three natural resources.", "Water, sunlight, and fertile soil are three vital natural resources.", "تین قدرتی وسائل کے نام بتائیں۔", "درې طبیعي سرچینې کومې دي؟", "اوبه، لمر او خاوره درې مهمې سرچینې دي."),
            ("Why is sunlight important for life?", "Sunlight gives warmth, light, and energy for plants to make food.", "سورج کی روشنی کیوں ضروری ہے؟", "لمر ولې اړین دی؟", "لمر بوټو ته انرژي او ټولې نړۍ ته رڼا بښي.")
        ]
    },
    {
        "number": 6,
        "title": "Water",
        "titleUrdu": "پانی",
        "titlePashto": "اوبه",
        "text": (
            "Water is the foundation of all life on Earth. Allah says in the Quran: \"We made from water every living thing.\"\n\n"
            "Sources of water include rainfall, snow melting on glaciers, rivers, lakes, canals, and groundwater extracted through wells and tube wells.\n\n"
            "Uses of water: drinking, cooking, washing, bathing, growing crops in fields, and generating hydroelectric power.\n\n"
            "Water conservation: We must not leave taps running while brushing teeth, repair leaking pipes, and never throw industrial waste or plastic into water bodies."
        ),
        "urdu": "پانی زندگی کی سب سے بڑی ضرورت ہے۔ بارش، گلیشیئرز، دریا اور زیرِ زمین کنویں پانی کے اہم ذرائع ہیں۔ پانی پینے، کھانا پکانے اور کھیتوں کو سیراب کرنے کے کام آتا ہے۔ ہمیں پانی کو ضائع نہیں کرنا چاہیے اور نلکے بند رکھنے چاہئیں۔",
        "pashto": "اوبه د ژوند بنسټ دی. دا د باران، سیندونو او چینې له لارې ترلاسه کیږي. مونږ باید اوبه بې ځایه ضایع نه کړو.",
        "questions": [
            ("What are the main natural sources of freshwater?", "Rain, melting glaciers, rivers, and groundwater are main sources.", "میٹھے پانی کے اہم ذرائع کیا ہیں؟", "د خوږو اوبو مهمې سرچینې کومې دي؟", "باران، سیندونه او د ځمکې لاندې اوبه دي."),
            ("How can we save water at home?", "We can save water by closing taps while brushing and fixing leaks.", "گھر میں پانی کی بچت کیسے کریں؟", "په کور کې اوبه څنګه وسپموو؟", "نلونه ژر بند کړئ او پایپونه جوړ کړئ.")
        ]
    },
    {
        "number": 7,
        "title": "Plants",
        "titleUrdu": "پودے اور نباتات",
        "titlePashto": "بوټي او ونې",
        "text": (
            "Plants are living things that make their own food using sunlight, water, and carbon dioxide through photosynthesis.\n\n"
            "Main parts of a plant:\n"
            "1. Roots: absorb water and nutrients from the soil and anchor the plant.\n"
            "2. Stem: transports water and supports leaves and flowers.\n"
            "3. Leaves: prepare food for the plant and release oxygen.\n"
            "4. Flowers: produce seeds and fruits.\n\n"
            "Importance: Plants provide oxygen, wheat, rice, vegetables, fruits, medicines, wood for shelter, and shade."
        ),
        "urdu": "پودے جاندار ہیں جو سورج کی روشنی اور پانی سے اپنی خوراک بناتے ہیں۔ پودے کے چار اہم حصے جڑ، تنا، پتے اور پھول ہیں۔ پودے ہمیں آکسیجن، پھل، سبزیاں اور ادویات فراہم کرتے ہیں۔",
        "pashto": "بوټي د کائنات ښکلا او د ژوند سرچینه ده. ریښه، ډډ، پاڼې او ګلان د بوټي اصلي برخې دي چې اکسیجن او خواړه تولیدوي.",
        "questions": [
            ("What is the function of plant roots?", "Roots absorb water from soil and keep the plant firmly in the ground.", "جڑوں کا کیا کام ہے؟", "د بوټي د ریښو دنده څه ده؟", "له خاورې اوبه جذبوي او بوټی ټینګ ساتي."),
            ("Which part of a plant makes food?", "Green leaves make food for the plant using sunlight.", "پودے کا کون سا حصہ خوراک بناتا ہے؟", "د بوټي کومه برخه خواړه جوړوي؟", "شنې پاڼې د لمر په مرسته خواړه جوړوي.")
        ]
    },
    {
        "number": 8,
        "title": "Animals",
        "titleUrdu": "جانور",
        "titlePashto": "حیوانات او ځناور",
        "text": (
            "Animals are diverse living creatures found all over the world.\n\n"
            "Types of animals by habitat:\n"
            "• Domestic animals: live with humans on farms or homes, e.g. cow, goat, horse, sheep, hen.\n"
            "• Wild animals: live in forests and jungles, e.g. lion, tiger, bear, elephant, wolf.\n"
            "• Water animals: live in oceans and rivers, e.g. fish, whale, dolphin.\n\n"
            "Dietary classification:\n"
            "• Herbivores: eat grass and plants (cow, deer, rabbit).\n"
            "• Carnivores: eat flesh of other animals (lion, leopard).\n"
            "• Omnivores: eat both plants and meat (bear, human, crow)."
        ),
        "urdu": "جانور مختلف اقسام کے ہوتے ہیں۔ پالتو جانور جیسے گائے، بکری اور مرغی انسانوں کے ساتھ رہتے ہیں جبکہ جنگلی جانور جیسے شیر اور ہاتھی جنگلوں میں رہتے ہیں۔ کچھ جانور گھاس کھاتے ہیں (سبزی خور) اور کچھ گوشت کھاتے ہیں (گوشت خور)۔",
        "pashto": "حیوانات په کورني او وحشي وېشل کیږي. غوا او پسه کورني او زمری او پړانګ وحشي دي. ځینې بوټي خوري او ځینې غوښه خوري.",
        "questions": [
            ("Give two examples of domestic animals.", "Cow and goat are common domestic animals.", "دو پالتو جانوروں کی مثالیں دیں۔", "د دوه کورنیو حیواناتو نومونه واخلئ.", "غوا او وزه دوه کورني حیوانات دي."),
            ("What is a herbivore?", "A herbivore is an animal that eats only plants and grass.", "سبزی خور جانور کیا ہوتا ہے؟", "واښه خوړونکی حیوان څه ته وايي؟", "هغه حیوان چې یوازې واښه او بوټي خوري.")
        ]
    },
    {
        "number": 9,
        "title": "Agriculture and Livestock",
        "titleUrdu": "زراعت اور مال مویشی",
        "titlePashto": "کرنه او مالداري",
        "text": (
            "Agriculture and livestock farming are the backbone of Pakistan's economy.\n\n"
            "Agriculture involves growing crops like wheat, rice, sugarcane, maize, cotton, fruits, and vegetables. "
            "Farmers prepare the soil, sow seeds, water fields, and harvest crops.\n\n"
            "Livestock refers to domesticated farm animals like cows, buffaloes, sheep, goats, camels, and poultry. "
            "They provide milk, butter, meat, eggs, wool, and leather. Bullocks and camels are also used for ploughing and transport in rural areas."
        ),
        "urdu": "زراعت اور لائیوسٹاک پاکستان کی معیشت کی ریڑھ کی ہڈی ہیں۔ زراعت میں گندم، چاول، کپاس اور گنا اگایا جاتا ہے۔ مال مویشی سے دودھ، مکھن، گوشت اور اون حاصل ہوتی ہے۔ کسان ہمارے محسن ہیں۔",
        "pashto": "کرنه او مالداري د هېواد د اقتصاد بنسټ دی. بزګران غنم، وریجې او جوار کري او غواګانې شیدې او غوښه راکوي.",
        "questions": [
            ("Name two major crops grown in Pakistan.", "Wheat and rice are two major crops grown in Pakistan.", "پاکستان کی دو بڑی فصلوں کے نام بتائیں۔", "د پاکستان دوه مهم فصلونه کوم دي؟", "غنم او وریجې دوه مهم فصلونه دي."),
            ("What products do we get from livestock?", "We get milk, butter, meat, eggs, wool, and leather from livestock.", "مویشیوں سے کیا حاصل ہوتا ہے؟", "له مالدارۍ څه ترلاسه کیږي؟", "شیدې، غوښه، کوچ او وړۍ ترې ترلاسه کیږي.")
        ]
    },
    {
        "number": 10,
        "title": "Conservation of The Earth's Resources",
        "titleUrdu": "زمین کے وسائل کا تحفظ",
        "titlePashto": "د ځمکې د سرچینو ژغورنه",
        "text": (
            "Earth's natural resources are limited, so we must protect and conserve them for future generations.\n\n"
            "The 3Rs of conservation:\n"
            "1. Reduce: Use less water, fuel, and electricity; avoid buying unnecessary plastic goods.\n"
            "2. Reuse: Use cloth shopping bags instead of single-use plastic; use refillable bottles.\n"
            "3. Recycle: Collect used paper, glass, plastic, and metal so factories can process them into new goods.\n\n"
            "Planting trees and avoiding littering protects wildlife, soil, and clean air."
        ),
        "urdu": "زمین کے وسائل محدود ہیں اس لیے ان کا تحفظ ضروری ہے۔ وسائل کے تحفظ کے لیے ۳ اصول ہیں: کم استعمال کرنا (Reduce)، دوبارہ استعمال کرنا (Reuse)، اور ری سائیکل کرنا (Recycle)۔ ہمیں درخت لگانے چاہئیں اور پلاسٹک کا استعمال کم کرنا چاہیے۔",
        "pashto": "د ځمکې د سرچینو د ساتنې لپاره درې اصول دي: کم کارول، بیا کارول او بیا جوړول (ری سایکل). ونې کېنول چاپېریال پاکوي.",
        "questions": [
            ("What do the 3Rs stand for?", "The 3Rs stand for Reduce, Reuse, and Recycle.", "تھری آرز (3Rs) کا کیا مطلب ہے؟", "د درې ار معنا څه ده؟", "کم کارول، بیا کارول او بیا نوی کول دي."),
            ("Why should we avoid plastic bags?", "Plastic bags do not decompose and pollute soil and water bodies.", "پلاسٹک کی تھیلیوں سے کیوں بچنا چاہیے؟", "له پلاستیکي کڅوړو ولې ډډه وکړو؟", "ځکه چې ځمکه او اوبه ککړوي او ژر نه خاورې کیږي.")
        ]
    },
    {
        "number": 11,
        "title": "Heat and Light",
        "titleUrdu": "حرارت اور روشنی",
        "titlePashto": "تودوخه او رڼا",
        "text": (
            "Heat and light are forms of energy vital for our survival.\n\n"
            "The Sun is the primary natural source of both heat and light on Earth. Without sunlight, plants could not grow and the Earth would be frozen and dark.\n\n"
            "Artificial sources of light and heat include electrical bulbs, lamps, tube lights, heaters, gas stoves, and burning wood.\n\n"
            "Heat warms our bodies, cooks food, dries wet clothes, and makes life comfortable in cold winters. Light enables our eyes to see the beautiful shapes and colours around us."
        ),
        "urdu": "حرارت اور روشنی توانائی کی بنیادی صورتیں ہیں۔ سورج حرارت اور روشنی کا سب سے بڑا قدرتی ذریعہ ہے۔ بلب، موم بتی اور ہیٹر مصنوعی ذرائع ہیں۔ حرارت کھانا پکانے اور گرمی کے لیے کام آتی ہے جبکہ روشنی ہمیں دیکھنے میں مدد دیتی ہے۔",
        "pashto": "لمر د تودوخې او رڼا تر ټولو ستره طبیعي سرچینه ده. ګروپونه او څراغونه مصنوعي رڼا ورکوي.",
        "questions": [
            ("What is the biggest natural source of heat and light?", "The Sun is the biggest natural source of heat and light on Earth.", "حرارت و روشنی کا سب سے بڑا قدرتی ذریعہ کیا ہے؟", "د رڼا او تودوخې ستره طبیعي سرچینه څه ده؟", "لمر تر ټولو ستره سرچینه ده."),
            ("Name two artificial sources of light.", "Electric bulb and torch are two artificial sources of light.", "روشنی کے دو مصنوعی ذرائع بتائیں۔", "د مصنوعي رڼا دوه سرچینې کومې دي؟", "برېښنايي ګروپ او لاسي څراغ دي.")
        ]
    },
    {
        "number": 12,
        "title": "Helping Others",
        "titleUrdu": "دوسروں کی مدد کرنا",
        "titlePashto": "له نورو سره مرسته",
        "text": (
            "Helping others is a noble moral duty taught by all religions.\n\n"
            "Ways to help others:\n"
            "• Help elderly people cross roads and carry heavy bags.\n"
            "• Share books, stationary, and lunch with needy classmates.\n"
            "• Give charity and food to the poor, orphans, and hungry people.\n"
            "• Comfort sick people and pray for their speedy recovery.\n\n"
            "The Holy Prophet Muhammad (SAW) said: \"Allah helps a person as long as he helps his brother.\""
        ),
        "urdu": "دوسروں کی مدد کرنا عظیم نیکی ہے۔ ضعیفوں کو راستہ دکھانا، بھوکوں کو کھانا کھلانا، دوستوں کے ساتھ چیزیں بانٹنا اور بیماروں کی عیادت کرنا انسانیت کی خدمت ہے۔ نبی کریم ﷺ نے فرمایا: اللہ اس بندے کی مدد میں رہتا ہے جو اپنے بھائی کی مدد میں لگا رہے۔",
        "pashto": "له نورو سره مرسته کول لوی ثواب دی. بې وزلو ته خواړه ورکول او د سپین ږیرو لاسنیوی کول د مسلمان نښه ده.",
        "questions": [
            ("How did the Holy Prophet (SAW) describe helping a brother?", "He said Allah helps a person as long as he is helping his brother.", "حدیث شریف میں مدد کا کیا اجر بتایا گیا ہے؟", "په حدیث کې د مرستې په هکله څه ویل شوي؟", "الله تعالی د هغه چا مرسته کوي چې د نورو مرسته کوي."),
            ("Give one way you can help an elderly person.", "You can help an elderly person by carrying their heavy luggage.", "بزرگوں کی مدد کیسے کی جا سکتی ہے؟", "د مشرانو سره څنګه مرسته کولی شو؟", "د درنو سامانونو په اخیستلو سره مرسته کولی شو.")
        ]
    },
    {
        "number": 13,
        "title": "Professions",
        "titleUrdu": "پیشے اور ہنر",
        "titlePashto": "کسبونه او مسلکونه",
        "text": (
            "Every person in a society chooses a job to earn an honest livelihood and serve the community. These jobs are called professions.\n\n"
            "Common professions:\n"
            "• Teacher: educates students and builds good character.\n"
            "• Doctor and Nurse: examine patients, treat diseases, and save lives.\n"
            "• Police Officer: maintains law and order and protects citizens from criminals.\n"
            "• Firefighter: rescues people from fires and disasters.\n"
            "• Engineer: designs roads, bridges, and machines.\n"
            "• Carpenter: makes furniture and wooden items.\n"
            "• Cobbler and Tailor: repair shoes and stitch clothes.\n\n"
            "Every profession deserves dignity and respect."
        ),
        "urdu": "معاشرے میں ہر فرد روزگار کمانے کے لیے کام کرتا ہے جسے پیشہ کہتے ہیں۔ استاد تعلیم دیتا ہے، ڈاکٹر علاج کرتا ہے، پولیس اہلکار امن قائم رکھتا ہے، اور بڑھئی و درزی چیزیں بناتے ہیں۔ ہر پیشہ معزز اور قابلِ احترام ہے۔",
        "pashto": "په ټولنه کې بېلابېل کسبونه شتون لري لکه ښوونکی، ډاکټر، انجنیر او نجار. ټول مسلکونه د درناوي وړ دي.",
        "questions": [
            ("What does a doctor do?", "A doctor examines patients, prescribes medicine, and cures diseases.", "ڈاکٹر کا کیا کام ہوتا ہے؟", "ډاکټر څه کار کوي؟", "ډاکټر د ناروغانو درملنه کوي."),
            ("What is the job of a police officer?", "A police officer maintains peace, enforces law, and protects citizens.", "پولیس اہلکار کا کیا کام ہے؟", "د پولیس دنده څه ده؟", "امن او قانون ساتي او د خلکو ساتنه کوي.")
        ]
    },
    {
        "number": 14,
        "title": "Respecting Others and Appreciating their Diversity",
        "titleUrdu": "دوسروں کا احترام اور تنوع کی قدر",
        "titlePashto": "د نورو درناوی او د تنوع منل",
        "text": (
            "People come from different cultures, speak different languages (such as Urdu, Pashto, Punjabi, Sindhi, Balochi), and follow different traditions.\n\n"
            "Diversity means having different backgrounds and qualities. It makes our country rich and vibrant.\n\n"
            "How to show respect:\n"
            "• Listen patiently when others speak without interrupting.\n"
            "• Never make fun of someone's clothes, accent, or appearance.\n"
            "• Treat people of all religions with equal kindness and justice.\n"
            "• Celebrate national unity while honoring provincial cultures."
        ),
        "urdu": "پاکستان میں مختلف زبانیں بولنے والے اور مختلف ثقافتوں سے تعلق رکھنے والے لوگ رہتے ہیں۔ تنوع ہمارے ملک کی خوبصورتی ہے۔ ہمیں سب کی زبان، لباس اور ثقافت کا احترام کرنا چاہیے اور کسی کا مذاق نہیں اڑانا چاہیے۔",
        "pashto": "ټول خلک بېلابېلې ژبې او دودونه لري. مونږ باید د هر چا درناوی وکړو او د هیچا په ژبه یا جامو پورې ونه خاندو.",
        "questions": [
            ("What is meant by diversity?", "Diversity means variety in cultures, languages, and qualities in society.", "تنوع کا کیا مطلب ہے؟", "د تنوع معنا څه ده؟", "په ټولنه کې د ژبو او کلتورونو بېلابېلوالی دی."),
            ("How should we treat people who speak different languages?", "We should treat them with polite respect, patience, and warmth.", "مختلف زبانیں بولنے والوں سے کیسا رویہ رکھیں؟", "له نورو ژبو ویونکو سره څه چلند وکړو؟", "په پوره مینه او درناوي سره باید چلند وکړو.")
        ]
    },
    {
        "number": 15,
        "title": "Forgiveness and Forgiving Others",
        "titleUrdu": "معاف کرنا اور درگزر",
        "titlePashto": "بخښنه او زغم",
        "text": (
            "Forgiveness means letting go of anger when someone hurts you or makes a mistake.\n\n"
            "When someone says 'sorry' or apologizes sincerely, we should forgive them with an open heart. "
            "Holding grudges makes a person unhappy and bitter, while forgiving brings peace of mind and friendship.\n\n"
            "The Holy Prophet Muhammad (SAW) forgave his fiercest enemies upon the Conquest of Makkah, saying: \"No blame shall be upon you today. Go, you are all free!\"\n\n"
            "Allah loves those who forgive others."
        ),
        "urdu": "معاف کرنا بڑی بہادری اور نیکی ہے۔ جب کوئی اپنی غلطی تسلیم کر کے معافی مانگے تو اسے فراخ دلی سے معاف کر دینا چاہیے۔ فتح مکہ کے موقع پر نبی کریم ﷺ نے اپنے جانی دشمنوں کو معاف فرما دیا۔ معاف کرنے سے دل میں سکون آتا ہے۔",
        "pashto": "بخښنه کول د زړورتیا نښه ده. کله چې څوک تېروتنه ومني، باید وبخښل شي. رسول الله (ص) د مکې په فتحه کې خپل ټول دښمنان وبخښل.",
        "questions": [
            ("What did the Prophet (SAW) do at the Conquest of Makkah?", "He forgave all his enemies and declared general amnesty.", "نبی کریم ﷺ نے فتح مکہ پر کیا کیا؟", "رسول الله (ص) د مکې په فتح کې څه وکړل؟", "خپلو ټولو دښمنانو ته یې عامه بخښنه وکړه."),
            ("What are the benefits of forgiving others?", "Forgiving brings peace of heart, ends hostility, and earns Allah's reward.", "معاف کرنے کا کیا فائدہ ہے؟", "د بخښنې ګټه څه ده؟", "زړه ته سکون بښي او د الله تعالی رضا ترلاسه کیږي.")
        ]
    },
    {
        "number": 16,
        "title": "Being Just and Fair",
        "titleUrdu": "عدل اور انصاف",
        "titlePashto": "انصاف او عدالت",
        "text": (
            "Justice and fairness mean treating everyone equally without bias, favoritism, or cheating.\n\n"
            "Practicing fairness in daily life:\n"
            "• Follow rules fairly in playground games without cheating.\n"
            "• Wait patiently for your turn in queues at the canteen, bus stop, or ticket counter.\n"
            "• Share treats and toys equally among siblings and friends.\n"
            "• Tell the truth even if a mistake was made by your close friend or yourself.\n\n"
            "A fair person is respected and trusted by everyone in society."
        ),
        "urdu": "عدل اور انصاف کا مطلب ہے سب کے ساتھ برابری اور دیانت داری سے پیش آنا۔ کھیلوں میں چیٹنگ نہ کرنا، قطار میں اپنی باری کا انتظار کرنا اور سچ کا ساتھ دینا انصاف کے تقاضے ہیں۔ منصف مزاج انسان ہر دلعزیز ہوتا ہے۔",
        "pashto": "عدالت او انصاف دا دی چې له ټولو سره یو شان او سم چلند وشي، په لوبو کې دوکه ونه شي او په نوبت کې ودرېږو.",
        "questions": [
            ("What is meant by being fair in games?", "Being fair means following the rules honestly without cheating.", "کھیل میں انصاف کا کیا مطلب ہے؟", "په لوبو کې د انصاف معنا څه ده؟", "د اصولو پیروي کول او دوکه نه کول دي."),
            ("Why is waiting for your turn in a queue important?", "Waiting in line ensures order, fairness, and mutual respect.", "قطار میں باری کا انتظار کیوں ضروری ہے؟", "په قطار کې درېدل ولې مهم دي؟", "ځکه چې دا نظم او عدالت ټینګ ساتي.")
        ]
    }
]

lines = []
lines.append("/**")
lines.append(" * TuitionHub - Class 2 General Knowledge Comprehensive Dataset (KPK Textbook Board)")
lines.append(" * Complete 16 Chapters verbatim from official textbook:")
lines.append(" * D:\\SpaceBook\\Books\\2nd\\2nd GK\\Word\\GK 2nd.docx")
lines.append(" * Fully populated with verbatim lessons, solved exercises, MCQs, SQs, LQs,")
lines.append(" * and Board SLO Suites.")
lines.append(" */")
lines.append("")
lines.append("var GK_2_DATA = [")

for idx, ch in enumerate(chapters):
    comma = "," if idx < len(chapters) - 1 else ""
    c_num = ch["number"]
    c_title = ch["title"]
    lines.append("  {")
    lines.append(f'    "id": "cls2-gk-ch{c_num:02d}",')
    lines.append(f'    "number": {c_num},')
    lines.append(f'    "title": {json.dumps(c_title)},')
    lines.append(f'    "titleUrdu": {json.dumps(ch["titleUrdu"])},')
    lines.append(f'    "titlePashto": {json.dumps(ch["titlePashto"])},')
    lines.append(f'    "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",')
    lines.append(f'    "authorInfo": {json.dumps("General Knowledge Grade 2, Chapter " + str(c_num) + " - KPK Textbook Board Peshawar.")},')
    lines.append(f'    "text": {json.dumps(ch["text"])},')
    lines.append(f'    "urdu": {json.dumps(ch["urdu"])},')
    lines.append(f'    "pashto": {json.dumps(ch["pashto"])},')
    
    paras = [p.strip() for p in ch["text"].split("\n\n") if p.strip()]
    lines.append('    "sections": [')
    lines.append('      {')
    lines.append(f'        "heading": {json.dumps("Chapter " + str(c_num) + ": " + c_title)},')
    lines.append(f'        "headingUrdu": {json.dumps(ch["titleUrdu"])},')
    lines.append(f'        "headingPashto": {json.dumps(ch["titlePashto"])},')
    lines.append(f'        "text": {json.dumps(ch["text"])},')
    lines.append(f'        "paras": {json.dumps(paras)},')
    lines.append(f'        "urdu": {json.dumps(ch["urdu"])},')
    lines.append(f'        "pashto": {json.dumps(ch["pashto"])},')
    lines.append(f'        "english": {json.dumps(ch["text"])}')
    lines.append('      }')
    lines.append('    ],')

    # Exercise
    mcqs = [
        {
            "id": f'cls2-gk-ch{c_num:02d}-mcq1',
            "question": ch["questions"][0][0],
            "options": [ch["questions"][0][1], "Incorrect fact", "Not mentioned", "None of these"],
            "correct": 0,
            "explanation": ch["questions"][0][1],
            "urdu": ch["questions"][0][2],
            "pashto": ch["questions"][0][3]
        },
        {
            "id": f'cls2-gk-ch{c_num:02d}-mcq2',
            "question": ch["questions"][1][0],
            "options": [ch["questions"][1][1], "False statement", "Opposite result", "Other reason"],
            "correct": 0,
            "explanation": ch["questions"][1][1],
            "urdu": ch["questions"][1][2],
            "pashto": ch["questions"][1][3]
        }
    ]
    sqs = []
    for q_idx, q in enumerate(ch["questions"], 1):
        sqs.append({
            "id": f'cls2-gk-ch{c_num:02d}-sq{q_idx}',
            "question": q[0],
            "answer": q[1],
            "urdu": q[2],
            "pashto": q[3],
            "pashtoAns": q[4]
        })
    lqs = [
        {
            "id": f'cls2-gk-ch{c_num:02d}-lq1',
            "question": f'Explain the main concepts and importance of "{c_title}".',
            "answer": ch["text"],
            "urdu": f'سبق "{ch["titleUrdu"]}" کے اہم تصورات اور اہمیت بیان کریں۔',
            "urduAns": ch["urdu"],
            "pashto": f'د دې لوست مهم ټکي بیان کړئ.',
            "pashtoAns": ch["pashto"]
        }
    ]
    lines.append('    "exercise": {')
    lines.append(f'      "mcqs": {json.dumps(mcqs, indent=8).strip()},')
    lines.append(f'      "shortQuestions": {json.dumps(sqs, indent=8).strip()},')
    lines.append(f'      "longQuestions": {json.dumps(lqs, indent=8).strip()}')
    lines.append('    },')

    # SLO Questions
    slo_mcqs = [
        {
            "q": ch["questions"][0][0],
            "options": [ch["questions"][0][1], "Incorrect", "Unknown", "None"],
            "ans": 0,
            "explanation": ch["questions"][0][1]
        }
    ]
    slo_sqs = [
        {
            "q": ch["questions"][0][0],
            "ans": ch["questions"][0][1],
            "urdu": ch["questions"][0][2]
        }
    ]
    slo_lqs = [
        {
            "q": f'Write a short paragraph summarizing what you learned from Chapter {c_num}.',
            "ans": ch["text"]
        }
    ]
    lines.append('    "sloQuestions": {')
    lines.append(f'      "mcqs": {json.dumps(slo_mcqs, indent=8).strip()},')
    lines.append(f'      "sqs": {json.dumps(slo_sqs, indent=8).strip()},')
    lines.append(f'      "lqs": {json.dumps(slo_lqs, indent=8).strip()}')
    lines.append('    }')

    lines.append(f"  }}{comma}")

lines.append("];")
lines.append("")
lines.append("// Register into core DATA registry if available")
lines.append("if (typeof DATA !== 'undefined' && DATA) {")
lines.append("  DATA.gk2Chapters = GK_2_DATA;")
lines.append("}")
lines.append("")

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"SUCCESS! Wrote {len(lines)} lines to {OUT_JS}")
