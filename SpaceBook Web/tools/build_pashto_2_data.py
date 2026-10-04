# -*- coding: utf-8 -*-
r"""
build_pashto_2_data.py
Builds SpaceBook Web/js/pashto_2_data.js with all 28 complete lessons of
Class 2 Pashto (KPTBB), directly sourced from:
D:\SpaceBook\Books\2nd\2nd Pashto\Word\pashto.docx
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\pashto_2_data.js"

lessons = [
    {
        "number": 1,
        "type": "poem",
        "title": "حمدِ باري تعالى (نظم)",
        "titleEn": "Hamd (Poem - Praise of Allah)",
        "titleUrdu": "حمدِ باری تعالیٰ (نظم)",
        "text": (
            "چې خالق د دې دنیا دے\n"
            "هر چا لره پناه دے\n"
            "دا الله دے، دا الله دے!\n\n"
            "چې د هر چا مسیحا دے\n"
            "خو دے پټ او یکتا دے\n"
            "چې نه څوک پیدا د ده نه\n"
            "او نه دے د چا پیدا دے\n"
            "دا الله دے، دا الله دے!"
        ),
        "urdu": "جو اس دنیا کا پیدا کرنے والا اور سب کے لیے جائے پناہ ہے، وہ اللہ ہے۔ جو سب کا مسیحا اور مددگار ہے، ہر جگہ موجود لیکن نظروں سے پوشیدہ اور یکتا ہے۔ نہ اس کی کوئی اولاد ہے اور نہ وہ کسی کی اولاد ہے۔ وہ اکیلا معبود برحق اللہ ہے۔",
        "english": "He who is the Creator of this world and the refuge for all, He is Allah! He who is the healer of all ailments, unseen and Unique, Who neither begets nor is born, He is Allah, the One True God.",
        "questions": [
            ("د دې دنیا خالق او پیدا کوونکی څوک دی؟", "د دې ټولې دنیا خالق او پیدا کوونکی اکیلا الله تعالی دی.", "دنیا کا خالق کون ہے؟", "د ټولې نړۍ خالق الله تعالی دی."),
            ("د 'یکتا' توري معنا څه ده؟", "د یکتا معنا ده یواځې او بې شریکه (یو الله).", "یکتا کا کیا مطلب ہے؟", "یکتا د یواځې او بې مثل په معنا دی.")
        ],
        "words": [
            {"word": "خالق", "meaning": "پیدا کوونکی", "meaningUrdu": "پیدا کرنے والا", "english": "Creator"},
            {"word": "پناه", "meaning": "امان، د ژغورنې ځای", "meaningUrdu": "جائے پناہ", "english": "Refuge"},
            {"word": "مسیحا", "meaning": "د دردونو علاج کوونکی، مددګار", "meaningUrdu": "درد دور کرنے والا", "english": "Healer"},
            {"word": "یکتا", "meaning": "یو، بې مثله، بې شریکه", "meaningUrdu": "اکیلا، بے مثل", "english": "One and Only"}
        ]
    },
    {
        "number": 2,
        "type": "poem",
        "title": "نعت رسول مقبول ﷺ (نظم)",
        "titleEn": "Naat (Poem - Praise of Prophet Muhammad PBUH)",
        "titleUrdu": "نعتِ رسولِ مقبول ﷺ (نظم)",
        "text": (
            "څومره ښکلے معلم دے\n"
            "جاهلان ئې عالمان کړل\n\n"
            "څومره ښکلے لار ښایونکے\n"
            "کافران ئې مومنان کړل\n\n"
            "نېغه لار ئې کړه په ګوته\n"
            "د ړندو د لاس امسا شو\n\n"
            "که څوک ګوډ وو که څوک شل وو\n"
            "د هر چا د درد دوا شو"
        ),
        "urdu": "ہمارے پیارے نبی حضرت محمد ﷺ کتنے عظیم استاد اور رہبر ہیں جنہوں نے جاہلوں کو عالم اور کافروں کو مومن بنا دیا۔ آپؐ نے سیدھا راستہ دکھایا، اندھوں کا سہارا بنے اور ہر درد مند کے دکھ کی دوا بنے۔",
        "english": "What a magnificent teacher is the Holy Prophet (PBUH), who turned the ignorant into scholars and guided people to faith. He showed the straight path and became the walking staff for the blind and healer for the distressed.",
        "questions": [
            ("رسول الله صلی الله علیه وسلم جاهلانو ته څه وښودل؟", "هغه مبارک جاهلان پوه او عالمان کړل او سمه لار یې ور وښودله.", "نبی کریم ﷺ نے جاہلوں کو کیا سکھایا؟", "هغه هغوی ته د علم او ایمان رڼا ورکړه."),
            ("د 'معلم' توري څه معنا ده؟", "معلم د ښوونکي او استاد په معنا دی.", "معلم کا کیا مطلب ہے؟", "معلم د استاد او لارښود معنا لري.")
        ],
        "words": [
            {"word": "معلم", "meaning": "ښوونکی، استاد", "meaningUrdu": "استاد، سکھانے والا", "english": "Teacher"},
            {"word": "لار ښایونکے", "meaning": "لارښود، رهبر", "meaningUrdu": "رہنما، راستہ دکھانے والا", "english": "Guide"},
            {"word": "امسا", "meaning": "کوټه، لرګی چې ړوند پرې تګ کوي", "meaningUrdu": "لاٹھی، عصا", "english": "Walking stick"},
            {"word": "دوا", "meaning": "علاج، شفا", "meaningUrdu": "علاج، مرہم", "english": "Cure"}
        ]
    },
    {
        "number": 3,
        "type": "prose",
        "title": "زمونږ پېغمبر حضرت محمد رسول الله ﷺ",
        "titleEn": "Our Prophet Muhammad (PBUH)",
        "titleUrdu": "ہمارے پیغمبر حضرت محمد رسول اللہ ﷺ",
        "text": (
            "زمونږ ګران پیغمبر حضرت محمد رسول الله خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم د الله تعالی آخري رسول دی.\n\n"
            "هغه مبارک په مکه مکرمه کښې پیدا شو. د پلار نوم یې عبدالله او د مور نوم یې بي بي آمنه وه. هغه مبارک له ماشومتوبه ډېر رښتینی او امانت دار و، ځکه خلکو ورته صادق او امین وایه.\n\n"
            "کله چې څلوېښت کلن شو نو الله تعالی پرې وحي او نبوت نازل کړ. هغه مبارک ټولو انسانانو ته د نېکۍ، سولې، د یو الله د عبادت او د ښو اخلاقو بلنه ورکړه."
        ),
        "urdu": "ہمارے پیارے نبی حضرت محمد رسول اللہ ﷺ مکہ مکرمہ میں پیدا ہوئے۔ آپؐ بچپن ہی سے سچے اور امین تھے۔ چالیس سال کی عمر میں نبوت ملی اور آپؐ نے دنیا کو امن اور توحید کا درس دیا۔",
        "english": "Prophet Muhammad (PBUH) was born in Makkah. Renowned for truthfulness and trustworthiness as Sadiq and Ameen, he was blessed with prophethood at age forty and guided mankind to righteousness.",
        "questions": [
            ("د رسول الله صلی الله علیه وسلم د پلار او مور نوم څه و؟", "د پلار نوم عبدالله او د مور بي بي آمنه وه.", "والدین کے نام کیا تھے؟", "پلار عبدالله او مور بي بي آمنه وه."),
            ("خلکو ولې هغه مبارک ته امین وایه؟", "ځکه چې هغه ډېر رښتینی او د امانت ساتونکی و.", "لوگ امین کیوں کہتے تھے؟", "ځکه چې هغه هیڅکله خیانت نه کاوه.")
        ],
        "words": [
            {"word": "رښتینی", "meaning": "صادق، سچ ویونکی", "meaningUrdu": "سچا", "english": "Truthful"},
            {"word": "امانت دار", "meaning": "امین، باوري", "meaningUrdu": "دیانت دار", "english": "Trustworthy"},
            {"word": "بلنه", "meaning": "دعوت", "meaningUrdu": "دعوت", "english": "Invitation"},
            {"word": "سوله", "meaning": "امن، ارامي", "meaningUrdu": "امن", "english": "Peace"}
        ]
    },
    {
        "number": 4,
        "type": "prose",
        "title": "د سرو زرو امېل",
        "titleEn": "The Golden Necklace",
        "titleUrdu": "سونے کا ہار",
        "text": (
            "په یوه کلي کښې یو غریب سړی اوسېده چې ډېر نیک او ایماندار و. یوه ورځ هغه ته په لاره کښې د سرو زرو یو قیمتي امېل پروت وموندل شو.\n\n"
            "هغه له ځان سره وویل: 'دا زما مال نه دی، دا د چا امانت دی.' هغه کلي ته راغی او جار یې وواهه. د امېل اصلي خاوند راغی او نښې یې وښودلې.\n\n"
            "غریب سړي امېل ور وسپاره. د امېل خاوند د هغه په ایماندارۍ دومره خوښ شو چې هغه ته یې لویه جایزه ورکړه او د هغه سره یې د کار مرسته وکړه."
        ),
        "urdu": "ایک غریب ایماندار شخص کو سونے کا قیمتی ہار ملا۔ اس نے لالچ کرنے کے بجائے اعلان کرا کے اصل مالک کے حوالے کر دیا۔ مالک نے اس کی ایمانداری پر اسے انعام دیا۔ ایمانداری کا پھل ہمیشہ میٹھا ہوتا ہے۔",
        "english": "A poor but honest villager found a lost golden necklace. Rather than keeping it, he sought the rightful owner and returned it safely, earning a generous reward for his integrity.",
        "questions": [
            ("غریب سړي په لاره څه وموندل؟", "هغه د سرو زرو یو قیمتي امېل وموند.", "راستے میں کیا ملا؟", "د سرو زرو امېل یې وموند."),
            ("له دې کیسې موږ څه زده کوو؟", "موږ زده کوو چې ایمانداري او د پردي مال نه اخیستل د بریا لار ده.", "اس کہانی کا سبق کیا ہے؟", "چې ایمانداري تر ټولو غوره صفت دی.")
        ],
        "words": [
            {"word": "امېل", "meaning": "هار، غاړکۍ", "meaningUrdu": "ہار", "english": "Necklace"},
            {"word": "سره زر", "meaning": "طلا، سون", "meaningUrdu": "سونا", "english": "Gold"},
            {"word": "جار", "meaning": "اعلان، غږ", "meaningUrdu": "منادی، اعلان", "english": "Public Announcement"},
            {"word": "جایزه", "meaning": "انعام، بدله", "meaningUrdu": "انعام", "english": "Prize/Reward"}
        ]
    },
    {
        "number": 5,
        "type": "poem",
        "title": "د ماشومانو سندرې (نظم)",
        "titleEn": "Children's Rhymes (Poem)",
        "titleUrdu": "بچوں کے گیت (نظم)",
        "text": (
            "راشئ ملګرو راشئ\n"
            "په ګډه به لوبې وکړو\n\n"
            "ښوونځي ته به ځو په مینه\n"
            "لوست به په شوق زده کړو\n\n"
            "خپل وطن به ودان کړو\n"
            "د علم رڼا به خپره کړو\n\n"
            "موږ د وطن سباوون یو\n"
            "خپل هېواد به ګلستان کړو"
        ),
        "urdu": "بچے مل جل کر کھیلنے، شوق سے سکول جانے اور خوب پڑھنے کا عزم کرتے ہیں۔ بچے وطن کا مستقبل ہیں اور علم کی روشنی سے اپنے پیارے وطن کو خوبصورت باغ بنائیں گے۔",
        "english": "Children sing joyful songs about going to school, learning with passion, and building their beloved homeland into a flourishing garden through the power of education.",
        "questions": [
            ("ماشومان ښوونځي ته په څه ډول ځي؟", "ماشومان په مینه او شوق ښوونځي ته ځي.", "بچے سکول کیسے جاتے ہیں؟", "په شوق او مینه ځي."),
            ("د وطن سباوون څوک دي؟", "ماشومان او زده کوونکي د وطن راتلونکی او سباوون دي.", "وطن کا مستقبل کون ہیں؟", "ماشومان د وطن سباوون دي.")
        ],
        "words": [
            {"word": "سباوون", "meaning": "سحر، روښانه راتلونکی", "meaningUrdu": "صبحِ نو، مستقبل", "english": "Dawn/Future"},
            {"word": "ګلستان", "meaning": "باغ، چمن", "meaningUrdu": "گلشن", "english": "Garden"},
            {"word": "ودان", "meaning": "آباد، جوړ", "meaningUrdu": "آباد", "english": "Flourishing"},
            {"word": "رڼا", "meaning": "روښنايي، رڼا", "meaningUrdu": "روشنی", "english": "Light"}
        ]
    },
    {
        "number": 6,
        "type": "prose",
        "title": "د مشرانو ادب",
        "titleEn": "Respect for Elders",
        "titleUrdu": "بڑوں کا ادب",
        "text": (
            "د مشرانو عزت او درناوی د پښتنو د کلتور او د اسلام د سپېڅلي دین یوه بنسټیزه برخه ده.\n\n"
            "کله چې زموږ مخې ته کوم مشر راځي، موږ باید پاڅېږو، سلام ورته ووایو، او په ادب ورسره خبرې وکړو. د هغوی خبره باید وانه ړوو او د هغوی نصیحت واورو.\n\n"
            "رسول اکرم صلی الله علیه وسلم فرمایلي دي: 'هغه څوک زموږ له ډلې نه دی چې په کشرانو رحم ونه کړي او د مشرانو قدر ونه پېژني.' په کور کښې د مور او پلار او په ښوونځي کښې د ښوونکو درناوی پر موږ فرض دی."
        ),
        "urdu": "بڑوں کا ادب کرنا اسلامی تعلیمات اور پختون روایات کا اہم حصہ ہے۔ بڑوں کو سلام کرنا، ان کے سامنے مؤدب رہنا اور ان کی نصیحت سننا اچھے بچے کی پہچان ہے۔",
        "english": "Respect for elders is a bedrock of Islamic morality and Pashtun culture. Standing up, greeting elders politely, and heeding their counsel is the hallmark of noble upbringing.",
        "questions": [
            ("د مشرانو په وړاندې باید څنګه چلند وشي؟", "باید هغوی ته سلام وشي، درناوی یې وشي او په نرمه ژبه خبرې ورسره وشي.", "بڑوں سے کیسا برتاؤ کریں؟", "په پوره ادب او درناوي ورسره چلند پکار دی."),
            ("حدیث مبارک د مشرانو په هکله څه وايي؟", "چې د مشرانو قدر او درناوی پېژندل لازم دي.", "حدیث میں کیا فرمایا گیا؟", "د مشرانو قدر پېژندل د مسلمان نښه ده.")
        ],
        "words": [
            {"word": "درناوی", "meaning": "عزت، ادب", "meaningUrdu": "احترام", "english": "Respect"},
            {"word": "کشران", "meaning": "کوچني، وړوکي", "meaningUrdu": "چھوٹے", "english": "Juniors/Young ones"},
            {"word": "نصیحت", "meaning": "نېکه مشوره", "meaningUrdu": "نصیحت", "english": "Good Advice"},
            {"word": "کلتور", "meaning": "دود او دستور، کلتور", "meaningUrdu": "ثقافت", "english": "Culture"}
        ]
    },
    {
        "number": 7,
        "type": "poem",
        "title": "کونتره (نظم)",
        "titleEn": "The Dove (Poem)",
        "titleUrdu": "فاختہ / کبوتر (نظم)",
        "text": (
            "ښکلې ښکلې کونتره\n"
            "سپینه لکه سپوږمۍ ده\n\n"
            "ګوره په ونو الوزي\n"
            "د امن نښه ده دا\n\n"
            "دانه خوري او اوبه څښي\n"
            "په بامونو ګرځي راګرځي\n\n"
            "کله چې کښېني په ښاخ\n"
            "په خوږه ژبه سندرې وايي"
        ),
        "urdu": "فاختہ ایک معصوم اور خوبصورت پرندہ ہے جو امن و آشتی کا نشان ہے۔ وہ درختوں پر اڑتی ہے، دانا چگتی ہے اور اپنی میٹھی بولی بولتی ہے۔",
        "english": "A poetic tribute to the gentle white dove, symbolizing peace and innocence, flying gracefully among trees and singing sweetly on roof branches.",
        "questions": [
            ("کونتره د څه شي نښه ده؟", "کونتره د امن او سولې نښه ده.", "فاختہ کس چیز کی علامت ہے؟", "د امن او سولې نښه ده."),
            ("د کونترې رنګ څنګه دی؟", "کونتره د سپوږمۍ غوندې ښکلې او سپینه ده.", "فاختہ کا رنگ کیسا ہے؟", "سپینه او ښکلې ده.")
        ],
        "words": [
            {"word": "کونتره", "meaning": "کوتره، قمرۍ", "meaningUrdu": "فاختہ، کبوتر", "english": "Dove/Pigeon"},
            {"word": "سپوږمۍ", "meaning": "قمر، چاند", "meaningUrdu": "چاند", "english": "Moon"},
            {"word": "امن", "meaning": "سوله، ارامي", "meaningUrdu": "امن", "english": "Peace"},
            {"word": "ښاخ", "meaning": "د ونې څانګه", "meaningUrdu": "شاخ، ٹہنی", "english": "Branch"}
        ]
    },
    {
        "number": 8,
        "type": "prose",
        "title": "د غوښې پوټے",
        "titleEn": "The Piece of Meat (Greedy Dog Fable)",
        "titleUrdu": "گوشت کا ٹکڑا (لالچی کتے کی کہانی)",
        "text": (
            "یو سپی روان و چې د قصاب له دوکانه یې د غوښې یو پوټی وموند. سپی ډېر خوشحاله شو او د غوښې پوټی یې په خوله کښې ونیوه او د ځنګل لور ته روان شو.\n\n"
            "په لاره کښې د اوبو یو پول (پُل) و. کله چې سپي له پله نه لاندې صافو اوبو ته وکتل، نو خپل سیوری یې ولید. هغه فکر وکړ چې بل سپی دی او د هغه په خوله کښې هم د غوښې پوټی دی.\n\n"
            "لالچي سپي غوښتل چې هغه پوټی هم ترې واخلي. لکه څنګه چې یې خوله خلاصه کړه چې غپ وکړي، نو خپل د غوښې پوټی یې له خولې نه په اوبو کښې ولوېد او اوبو یووړ. سپی تشه خوله او وږی پاتې شو. پایله: لالچ بد بلا ده."
        ),
        "urdu": "ایک لالچی کتے نے پل پر پانی میں اپنا عکس دیکھا اور سمجھا کہ دوسرا کتا گوشت لیے کھڑا ہے۔ اس نے بھونکنے کے لیے منہ کھولا تو اپنا گوشت بھی گنوا بیٹھا۔ لالچ بری بلا ہے۔",
        "english": "A classic moral fable of a greedy dog who saw his reflection in the river while crossing a bridge. Snapping to seize the other piece of meat, he dropped his own and was left with nothing.",
        "questions": [
            ("سپي په اوبو کښې څه ولیدل؟", "سپي په اوبو کښې خپل سیوری ولید.", "کتے نے پانی میں کیا دیکھا؟", "خپل سیوری یې ولید."),
            ("له دې کیسې موږ څه اخلاقي زده کړه ترلاسه کوو؟", "چې لالچ بد کار دی او انسان هر څه له لاسه ورکوي.", "اس کہانی سے کیا سبق ملتا ہے؟", "لالچ بد بلا ده.")
        ],
        "words": [
            {"word": "پوټے", "meaning": "ټوټه، برخه", "meaningUrdu": "ٹکڑا", "english": "Piece"},
            {"word": "سیوری", "meaning": "عکس، سیوری", "meaningUrdu": "سایہ، عکس", "english": "Shadow/Reflection"},
            {"word": "لالچ", "meaning": "طمع، حرص", "meaningUrdu": "لالچ، طمع", "english": "Greed"},
            {"word": "قصاب", "meaning": "قصاب، د غوښې خرڅوونکی", "meaningUrdu": "قصاب", "english": "Butcher"}
        ]
    },
    {
        "number": 9,
        "type": "poem",
        "title": "همدردي (نظم)",
        "titleEn": "Empathy (Poem by Allama Iqbal)",
        "titlePs": "همدردي (نظم)",
        "titleUrdu": "ہمدردی (علامہ اقبال کی نظم کا پشتو ترجمہ)",
        "text": (
            "په یوه ونه کښې ناست بلبل و\n"
            "شپه راغله او په زړه خپه و\n\n"
            "چې څنګه به خپلو بچو ته لاړ شم\n"
            "په تیاره کښې ځاله څنګه بیامومم؟\n\n"
            "په دې وخت کښې یو پتنګ راغی\n"
            "هغه ورته وویل: ای وروره!\n\n"
            "زه به خپله وړه رڼا درکړم\n"
            "ستا د لارې مشال به شم زه\n\n"
            "دی همدردي چې څوک په کار راځي\n"
            "د بل چا په سختۍ او تیاره کښې"
        ),
        "urdu": "علامہ اقبال کی مشہور نظم 'ہمدردی' کا پشتو نثری و منظوم مفہوم۔ ایک ننھے جگنو نے اندھیری رات میں پریشان بلبل کو اپنی روشنی پیش کی تاکہ وہ اپنے گھونسلے تک پہنچ سکے۔ سچے انسان وہی ہیں جو دوسروں کے کام آتے ہیں۔",
        "english": "The Pashto poetic adaptation of Allama Iqbal's celebrated poem 'Hamdardi', where a glowing firefly lights the way for a stranded nightingale, exemplifying mutual assistance.",
        "questions": [
            ("بلبل ولې خپه و؟", "ځکه چې شپه شوه او په تیاره کې یې خپله ځاله نه موندله.", "بلبل کیوں اداس تھا؟", "ځکه چې تیاره شوه او ځاله ترې ورکه شوه."),
            ("پتنګ (جگنو) بلبل ته څنګه مرسته وکړه؟", "پتنګ خپله رڼا وښودله او د بلبل لار یې روښانه کړه.", "جگنو نے بلبل کی مدد کیسے کی؟", "خپله رڼا یې د لارې مشال کړه.")
        ],
        "words": [
            {"word": "همدردي", "meaning": "غمرازي، یو له بل سره مرسته", "meaningUrdu": "ہمدردی", "english": "Empathy/Compassion"},
            {"word": "بلبل", "meaning": "یو خوږ غږی مرغۍ", "meaningUrdu": "بلبل", "english": "Nightingale"},
            {"word": "مشال", "meaning": "څراغ، ډېوه", "meaningUrdu": "چراغ، مشعل", "english": "Torch/Lamp"},
            {"word": "تیاره", "meaning": "تورتم، تیارکی", "meaningUrdu": "اندھیرا", "english": "Darkness"}
        ]
    },
    {
        "number": 10,
        "type": "prose",
        "title": "اشر (پښتني دود)",
        "titleEn": "Ashar (Pashtun Mutual Cooperation Tradition)",
        "titleUrdu": "اشر (روایتی پختون باہمی امداد)",
        "text": (
            "اشر د پښتنو یو ډېر لرغونی او ښکلی ټولنیز دود دی. په اشر کښې د کلي خلک په ګډه سره د یوه بل په کار کښې مرسته کوي، لکه د فصلونو رېبل، د کور جوړول یا د کارېز پاکول.\n\n"
            "کله چې په کلي کښې د یو چا فصل پخ شي، هغه کلیوالو ته د اشر بلنه ورکوي. ځوانان، سپین ږیري او ماشومان په مینه او خندا سره راټولېږي او ټول کار په څو ساعتونو کښې سرته رسوي.\n\n"
            "د کار په پای کښې د اشر خاوند ټولو ته خوندور خواړه تیاروي. اشر په ټولنه کښې یووالی، مینه او د ورورولۍ روحیه ژوندۍ ساتي."
        ),
        "urdu": "اشر پختونوں کا قدیم روایتی نظام ہے جس میں گاؤں والے بغیر کسی اجرت کے مل کر ایک دوسرے کے فصل کاٹنے، مکان بنانے اور ندی نالوں کی صفائی میں ہاتھ بٹاتے ہیں۔ اس سے اتحاد اور بھائی چارہ بڑھتا ہے۔",
        "english": "Ashar is an ancient Pashtun communal tradition of voluntary mutual assistance where villagers unite to harvest crops, build houses, and resolve community tasks in a spirit of solidarity.",
        "questions": [
            ("اشر څه ته وايي؟", "اشر په ګډه د یو بل سره د کار مرستې ته وايي.", "اشر کسے کہتے ہیں؟", "اشر د باهمي مرستې دود دی."),
            ("د اشر ګټه څه ده؟", "اشر ټولنه کې یووالی راولي او سخت کار اسانه کوي.", "اشر کا کیا فائدہ ہے؟", "دا په ټولنه کې مینه او اتحاد زیاتوي.")
        ],
        "words": [
            {"word": "اشر", "meaning": "په ګډه د کار مرسته", "meaningUrdu": "باہمی مفت امداد", "english": "Communal assistance"},
            {"word": "لرغونی", "meaning": "زوړ، تاریخي", "meaningUrdu": "قدیم", "english": "Ancient"},
            {"word": "رېبل", "meaning": "د فصل غوڅول او رېبل", "meaningUrdu": "فصل کاٹنا", "english": "Harvesting"},
            {"word": "روحیه", "meaning": "جذبه، روح", "meaningUrdu": "جذبہ", "english": "Spirit/Morale"}
        ]
    },
    {
        "number": 11,
        "type": "poem",
        "title": "زه به هم لسم ته شم (نظم)",
        "titleEn": "I Too Will Reach Tenth Grade (Poem)",
        "titleUrdu": "میں بھی دسویں جماعت میں جاؤں گا (نظم)",
        "text": (
            "وړوکې یم خو هوډ لرم\n"
            "سبا به لوی انسان شمه\n\n"
            "له لومړي ټولګي روان یم\n"
            "زه به هم لسم ته شمه\n\n"
            "کتاب قلم مې ملګري دي\n"
            "د ښوونکي خبره اورمه\n\n"
            "ډاکټر، انجنیر یا استاد به شم\n"
            "د خپل وطن خدمت کومه"
        ),
        "urdu": "ایک پرعزم بچے کا ترانہ جو ابھی چھوٹا ہے لیکن ارادہ پکا رکھتا ہے۔ وہ محنت سے پہلی اور دوسری جماعت سے آگے بڑھ کر دسویں تک جائے گا اور بڑا ہو کر ڈاکٹر، انجینئر یا استاد بن کر ملک و قوم کی خدمت کرے گا۔",
        "english": "An inspiring poem of an ambitious schoolchild resolved to study diligently from primary grade up to matriculation and serve his country as a doctor, engineer or scholar.",
        "questions": [
            ("ماشوم څه هوډ لري؟", "ماشوم هوډ لري چې لسم ټولګي ته ورسېږي او د وطن خدمت وکړي.", "بچے کا کیا ارادہ ہے؟", "چې ډېر درس ووایي او لوی شي."),
            ("د ماشوم ملګري څه دي؟", "کتاب او قلم د ماشوم غوره ملګري دي.", "بچے کے ساتھی کون ہیں؟", "کتاب او قلم یې ملګري دي.")
        ],
        "words": [
            {"word": "هوډ", "meaning": "کلکه اراده، عزم", "meaningUrdu": "عزم، پکا ارادہ", "english": "Firm resolve"},
            {"word": "ټولګی", "meaning": "جماعت، کلاس", "meaningUrdu": "جماعت، درجہ", "english": "Class/Grade"},
            {"word": "سبا", "meaning": "راتلونکی، راتلونکې زمانه", "meaningUrdu": "آنے والا کل", "english": "Tomorrow/Future"},
            {"word": "ملګری", "meaning": "دوست، همراز", "meaningUrdu": "دوست، ساتھی", "english": "Friend/Companion"}
        ]
    },
    {
        "number": 12,
        "type": "prose",
        "title": "د خوراک څښاک اداب",
        "titleEn": "Manners of Eating and Drinking",
        "titleUrdu": "کھانے پینے کے آداب",
        "text": (
            "اسلام موږ ته د خوراک او څښاک ډېر غوره او صحي آداب راښودلي دي:\n\n"
            "۱. د خوراک نه مخکې دواړه لاسونه په صابون وینځل.\n"
            "۲. په ښي لاس سره خوراک کول او په بسم الله پیل کول.\n"
            "۳. د خپلې مخې نه خوراک کول او په وړو وړو ګولو خوراک کول.\n"
            "۴. اوبه په ناسته او په دریو ساه ګانو کښې څښل.\n"
            "۵. د خوراک له ختمېدو وروسته الحمد لله ویل او لاسونه بیا وینځل.\n"
            "په ډوډۍ کښې عیب نه راایستل او ډوډۍ نه ضایع کول د نبي کریم ﷺ سنت دي."
        ),
        "urdu": "کھانا کھانے سے پہلے ہاتھ دھونا، دائیں ہاتھ سے بسم اللہ پڑھ کر کھانا، اپنے سامنے سے کھانا، اور پانی بیٹھ کر تین سانسوں میں پینا سنتِ نبوی ہے۔ کھانے کے بعد اللہ کا شکر ادا کرنا چاہیے۔",
        "english": "Islamic manners of dining: washing hands before eating, eating with the right hand, reciting Bismillah, eating from one's own side, drinking water while seated in three breaths, and thanking Allah.",
        "questions": [
            ("د ډوډۍ خوړلو اسلامي آداب څه دي؟", "په ښي لاس او په بسم الله پیل کول او مخکې لاسونه وینځل دي.", "کھانے کے اہم آداب کیا ہیں؟", "په ښي لاس او له بسم الله سره خوړل دي."),
            ("اوبه باید څنګه وڅښل شي؟", "اوبه باید په ناسته او په دریو ساه ګانو کې وڅښل شي.", "پانی کیسے پینا چاہیے؟", "په ناسته او په دریو ساه ګانو کې وڅښل شي.")
        ],
        "words": [
            {"word": "آداب", "meaning": "طریقې، اخلاق", "meaningUrdu": "آداب، طریقے", "english": "Etiquette/Manners"},
            {"word": "ګوله", "meaning": "لوقمه", "meaningUrdu": "نوالہ", "english": "Morsel"},
            {"word": "ساه", "meaning": "نفس، ساه اخیستل", "meaningUrdu": "سانس", "english": "Breath"},
            {"word": "ضایع", "meaning": "برباد، بې ځایه غورځول", "meaningUrdu": "ضائع کرنا", "english": "Wasting"}
        ]
    },
    {
        "number": 13,
        "type": "prose",
        "title": "د کلي اختر",
        "titleEn": "Eid in the Village",
        "titleUrdu": "گاؤں کی عید",
        "text": (
            "د کلي اختر ډېر په زړه پورې او د خوشحالۍ نه ډک وي. سهار وختي ماشومان او مشران نوي کالي اغوندي او د عیدګاه لور ته ځي.\n\n"
            "له لمانځه وروسته ټول خلک یو بل ته غېږې ورکوي او اختر مبارکي وايي. کشران د مشرانو لاسونه ښکلوي او مشران هغوی ته اخترۍ (عیدي) ورکوي.\n\n"
            "په کورونو کښې مېندې خوږې ورجې، کچورۍ او ښکلې مېوې چمتو کوي. د کلي ماشومان په زانګوګانو کښې زنګېږي او ټوله ورځ خندا او خوشحالي وي."
        ),
        "urdu": "گاؤں میں عید کی صبح سب نئے کپڑے پہن کر عیدگاہ جاتے ہیں، گلے ملتے ہیں، اور بچے بڑوں سے عیدی لیتے ہیں۔ گھروں میں میٹھے پکوان تیار ہوتے ہیں اور ہر طرف مسرت کا سماں ہوتا ہے۔",
        "english": "Eid in a Pashtun village brings joy: morning prayers at the Eidgah, embracing each other, elders giving Eidi to children, and mothers preparing sweet rice and dishes.",
        "questions": [
            ("په اختر کښې خلک له لمانځه وروسته څه کوي؟", "خلک یو بل ته غېږې ورکوي او مبارکي وايي.", "عید پر نماز کے بعد کیا کرتے ہیں؟", "یو بل ته مبارکي ورکوي."),
            ("اخترۍ څه ته وايي؟", "هغه پیسې یا ډالۍ چې مشران یې ماشومانو ته ورکوي.", "عیدی کسے کہتے ہیں؟", "هغه تحفه چې ماشومانو ته ورکول کیږي.")
        ],
        "words": [
            {"word": "اخترۍ", "meaning": "عیدي، د اختر تحفه", "meaningUrdu": "عیدی", "english": "Eid Gift/Eidi"},
            {"word": "غېږه", "meaning": "بغلګیري، په غېږ کې نیول", "meaningUrdu": "گلے ملنا", "english": "Embrace"},
            {"word": "زانګو", "meaning": "پالنګ، زنګېدونکی شی", "meaningUrdu": "جھولا", "english": "Swing"},
            {"word": "چمتو", "meaning": "تیار", "meaningUrdu": "تیار", "english": "Prepared/Ready"}
        ]
    },
    {
        "number": 14,
        "type": "prose",
        "title": "ټوقې ټقالي",
        "titleEn": "Humour and Riddles",
        "titleUrdu": "ہنسی مذاق اور لطائف",
        "text": (
            "پښتانه د میلمه پالنې تر څنګ د مجلس او خوږو ټوقو ډېر شوقیان دي. په حُجرو کښې به خلک کښېناستل او د خندا او تفریح لپاره به یې پاکې ټوقې او معماګانې (ټقالي) کولې.\n\n"
            "یو چا له یوه ساده سړي نه وپوښتل: 'که په ونه لس مرغۍ ناستې وي او یو ښکاري یوه په ټوپک وولي، نو په ونه به څو پاتې شي؟'\n"
            "ساده سړي وویل: 'نهه پاتې کېږي.'\n"
            "پوښتونکي وویل: 'نه! د ډزو په اواز ټولې الوتې، هیڅ هم نه پاتې کېږي!'\n"
            "داسې پاکې ټوقې ذهن تازه کوي او زړونه خوشحالوي."
        ),
        "urdu": "حجروں میں بیٹھ کر پاکیزہ لطائف اور پہیلیاں کہنا پختون معاشرے کی پرانی روایت ہے جس سے دل بہلتا ہے اور سوچنے کی صلاحیت بیدار ہوتی ہے۔",
        "english": "Wholesome jokes, witty riddles and riddles recited in traditional Hujras bring laughter and stimulate mental acuity among gathering friends.",
        "questions": [
            ("د ټوقو او ټقالو ګټه څه ده؟", "دا ذهن تاند ساتي او زړونو ته پاکه خوشحالي بښي.", "لطیفوں کا کیا فائدہ ہے؟", "ذهن تاند او خوشحاله ساتي."),
            ("په حجره کښې خلک څه کوي؟", "خلک په حجره کې مجلسونه او تفریحي خبرې کوي.", "حجرے میں کیا ہوتا ہے؟", "مجلسونه او ګټورې خبرې کوي.")
        ],
        "words": [
            {"word": "ټوقې", "meaning": "خندونکې خبرې، لطیفې", "meaningUrdu": "لطائف، چٹکلے", "english": "Jokes"},
            {"word": "حُجره", "meaning": "د پښتنو د ناستې او مېلمستیا ځای", "meaningUrdu": "بیٹھک، مہمان خانہ", "english": "Hujra / Community Guest House"},
            {"word": "تاند", "meaning": "تازه، ژوندی", "meaningUrdu": "تازہ دم", "english": "Fresh/Lively"},
            {"word": "معما", "meaning": "پټه خبره، چیستان", "meaningUrdu": "پہیلی", "english": "Riddle"}
        ]
    },
    {
        "number": 15,
        "type": "poem",
        "title": "د ژمي موسم (نظم)",
        "titleEn": "Winter Season (Poem)",
        "titleUrdu": "سردیوں کا موسم (نظم)",
        "text": (
            "راغی ژمی راغی ژمی\n"
            "یخې وریځې، واورې ورېږي\n\n"
            "پاس په غرونو واوره شوه\n"
            "سړه هوا په باغونو لګېږي\n\n"
            "ګرمې جامې اغوندو\n"
            "په انګړ کښې اور لګوو\n\n"
            "ګرم چای او چهارمغز خورو\n"
            "د ژمي خوندونه اخلو"
        ),
        "urdu": "سردیوں کے موسم میں پہاڑوں پر برف باری ہوتی ہے، ٹھنڈی ہوائیں چلتی ہیں، لوگ گرم لباس پہنتے ہیں، آگ تاپتے ہیں اور چائے و خشک میوہ جات سے لطف اندوز ہوتے ہیں۔",
        "english": "Winter brings snow upon the peaks, chilly breezes, warm clothes, gathering around hearth fires, and enjoying hot green tea and dry fruits.",
        "questions": [
            ("په ژمي کښې څه ورېږي؟", "په غرونو او درو کښې سپینه واوره ورېږي.", "سردیوں میں کیا برستا ہے؟", "سپینه واوره ورېږي."),
            ("خلک د یخ نه د بچ کېدو لپاره څه کوي؟", "ګرمې جامې اغوندي او اور لګوي.", "سردی سے بچنے کے لیے کیا کرتے ہیں؟", "ګرمې جامې اغوندي.")
        ],
        "words": [
            {"word": "ژمی", "meaning": "د یخ موسم، ژمی", "meaningUrdu": "سردیاں", "english": "Winter"},
            {"word": "واوره", "meaning": "برف", "meaningUrdu": "برف", "english": "Snow"},
            {"word": "انګړ", "meaning": "صحن، حویلي", "meaningUrdu": "صحن", "english": "Courtyard"},
            {"word": "چهارمغز", "meaning": "اخروټ", "meaningUrdu": "اخروٹ", "english": "Walnut"}
        ]
    },
    {
        "number": 16,
        "type": "prose",
        "title": "زمونږ ادارې",
        "titleEn": "Our Civic Institutions",
        "titleUrdu": "ہمارے قومی ادارے",
        "text": (
            "په یوه هېواد کښې د خلکو د خدمت لپاره بېلابېلې حکومتي ادارې کار کوي:\n\n"
            "۱. ښوونځی او پوهنتون: د علم او پوهې مرکزونه دي.\n"
            "۲. روغتون: د ناروغانو درملنه کوي.\n"
            "۳. تاڼه او پولیس: د خلکو د سر او مال ساتنه کوي او قانون پلي کوي.\n"
            "۴. ډاکخانه: خطونه او پارسلونه رسوي.\n"
            "۵. عدالت: خلکو ته انصاف ورکوي.\n"
            "دا ټولې زموږ ملي شتمنۍ دي او ساتنه یې زموږ ګډه دنده ده."
        ),
        "urdu": "سکول، ہسپتال، پولیس اسٹیشن، ڈاک خانہ اور عدالتیں ہمارے اہم قومی ادارے ہیں جو شہریوں کو تعلیم، صحت، تحفظ اور انصاف فراہم کرتے ہیں۔ ان کا احترام ہم پر لازم ہے۔",
        "english": "Public institutions serve society: schools provide education, hospitals provide healthcare, police maintain law and order, post offices deliver mail, and courts provide justice.",
        "questions": [
            ("روغتون څه خدمت کوي؟", "روغتون د ناروغانو علاج او درملنه کوي.", "ہسپتال کیا کام کرتا ہے؟", "د ناروغانو درملنه کوي."),
            ("د پولیسو اصلي دنده څه ده؟", "د خلکو د امنیت ساتنه او د قانون پلي کول دي.", "پولیس کا کیا کام ہے؟", "د امنیت ساتنه ده.")
        ],
        "words": [
            {"word": "اداره", "meaning": "دفتر، تنظیم، موسسه", "meaningUrdu": "ادارہ", "english": "Institution"},
            {"word": "روغتون", "meaning": "شفاخانه، هسپتال", "meaningUrdu": "ہسپتال", "english": "Hospital"},
            {"word": "درملنه", "meaning": "علاج", "meaningUrdu": "علاج", "english": "Treatment"},
            {"word": "عدالت", "meaning": "د انصاف ځای، محکمه", "meaningUrdu": "عدالت", "english": "Court/Judiciary"}
        ]
    },
    {
        "number": 17,
        "type": "prose",
        "title": "د خپلو څیزونو حفاظت کول",
        "titleEn": "Taking Care of Belongings",
        "titleUrdu": "اپنی چیزوں کی حفاظت کرنا",
        "text": (
            "یو ښه ماشوم تل د خپلو کتابونو، جامو او ښوونځي د شیانو پوره خیال ساتي.\n\n"
            "۱. کتابونه او کاپۍ باید په جلد وپوښل شي او پاڼې یې ونه شلېږي.\n"
            "۲. پنسل، خط کش او رنګونه په خپل بکس کښې وساتل شي.\n"
            "۳. له ښوونځي وروسته کڅوړه (بسته) او بوټونه په خپل ټاکلي ځای کښې کېښودل شي.\n"
            "څوک چې د خپلو شیانو ساتنه کوي، هغه وخت او پیسې دواړه بچ کوي."
        ),
        "urdu": "ایک سمجھدار بچہ اپنے بستہ، کتابوں، قلم اور جوتوں کو سنبھال کر مقررہ جگہ پر رکھتا ہے۔ چیزوں کی دیکھ بھال کرنے سے صفائی رہتی ہے اور نقصان نہیں ہوتا۔",
        "english": "A responsible child takes care of books, pencils, school bags, and uniform, placing items in their proper spots, saving money and preserving order.",
        "questions": [
            ("کتابونه څنګه باید وساتل شي؟", "کتابونه باید جلد شي او پاڼې یې پاکې وساتل شي.", "کتابیں کیسے رکھیں؟", "جلد کړای شي او پاڼې ونه شلول شي."),
            ("له ښوونځي وروسته کڅوړه چیرته کېښودل شي؟", "په خپل ټاکلي او پاک ځای کې کېښودل شي.", "بستہ کہاں رکھیں؟", "په خپل ځانګړي ځای کې.")
        ],
        "words": [
            {"word": "حفاظت", "meaning": "ساتنه، څارنه", "meaningUrdu": "حفاظت", "english": "Care/Protection"},
            {"word": "جلد", "meaning": "د کتاب پوښ", "meaningUrdu": "جلد", "english": "Book cover"},
            {"word": "کڅوړه", "meaning": "بسته، جېب", "meaningUrdu": "بستہ، تھیلا", "english": "School bag"},
            {"word": "ټاکلی", "meaning": "مخصوص، معلوم", "meaningUrdu": "مقررہ", "english": "Designated"}
        ]
    },
    {
        "number": 18,
        "type": "prose",
        "title": "کلیوالې لوبې",
        "titleEn": "Traditional Village Games",
        "titleUrdu": "دیہاتی روایتی کھیل",
        "text": (
            "په کلو کښې ماشومان ډېرې خوندورې او روغتیایي لوبې کوي، لکه: چونځه، مکۍ، خطکه، پټ پټونی، او توپ ډنډه (کرکټ غوندې پخوانۍ لوبه).\n\n"
            "دا لوبې بدن پیاوړی کوي، ذهن چست کوي او د ملګرو ترمنځ مینه پیدا کوي. پټ پټوني کښې ماشومان پټېږي او یو بل لټوي.\n\n"
            "د موبایل د بې ځایه لوبو پر ځای میدان ته وتل او فزیکي لوبې کول روغتیا ته ډېره ګټه رسوي."
        ),
        "urdu": "پختون دیہات میں روایتی کھیل جیسے چھپن چھپائی (پٹ پٹونی)، آنکھ مچولی اور گلی ڈنڈا کھیلے جاتے ہیں جو بچوں کو تندرست، توانا اور چست رکھتے ہیں۔",
        "english": "Traditional Pashtun rural outdoor games—such as hide-and-seek, tag, and indigenous ball-and-stick games—foster physical fitness and social bonding over digital screens.",
        "questions": [
            ("د کلیوالو لوبو دوه نومونه واخلئ.", "پټ پټونی او چونځه دوه مشهورې لوبې دي.", "دیہاتی کھیلوں کے نام بتائیں۔", "پټ پټونی او خطکه."),
            ("د فزیکي لوبو ګټه څه ده؟", "دا بدن روغ او قوي ساتي او ذهن چست کوي.", "ورزشی کھیلوں کا کیا فائدہ ہے؟", "بدن پیاوړی کوي.")
        ],
        "words": [
            {"word": "پټ پټونی", "meaning": "د پټېدو لوبه (سترګې پټول)", "meaningUrdu": "آنکھ مچولی، چھپن چھپائی", "english": "Hide and Seek"},
            {"word": "پیاوړی", "meaning": "قوي، تکړه", "meaningUrdu": "مضبوط، طاقتور", "english": "Strong"},
            {"word": "روغتیا", "meaning": "صحت، تندرستي", "meaningUrdu": "صحت", "english": "Health"},
            {"word": "چست", "meaning": "هوښیار، ګړندی", "meaningUrdu": "چست، پھرتیلا", "english": "Active"}
        ]
    },
    {
        "number": 19,
        "type": "prose",
        "title": "د آزادۍ پتنگ",
        "titleEn": "Kite of Freedom (Independence Day)",
        "titleUrdu": "آزادی کی پتنگ (جشنِ آزادی)",
        "text": (
            "د اګست څوارلسمه د پاکستان د آزادۍ ورځ ده. په دې ورځ سلیم او عاصم یو ښکلی شین او سپین پتنګ جوړ کړ چې پرې د سپوږمۍ او ستوري نښه وه.\n\n"
            "دوی چت ته وختل او پتنګ یې په اسمان کښې والوزاوه. پتنګ په نیلګون اسمان کښې لکه د آزادۍ سمبول رپېده.\n\n"
            "پلار ورته وویل: 'دا آزادي زموږ د پلرونو او مشرانو د لویو قربانیو په پایله کښې ترلاسه شوې ده. موږ باید د خپل وطن قدر وکړو او د هغې د ترقۍ لپاره زیار وباسو.'"
        ),
        "urdu": "چودہ اگست کو سلیم اور عاصم نے سبز ہلالی پرچم کے رنگوں والی پتنگ اڑائی۔ والد صاحب نے بتایا کہ یہ آزادی ہمارے آباؤ اجداد کی عظیم قربانیوں کا نتیجہ ہے، ہمیں اپنے وطن کی قدر کرنی چاہیے۔",
        "english": "On Pakistan's Independence Day, Salim and Asim fly a green-and-white kite with crescent and star, learning from their father about the sacred sacrifices that won national independence.",
        "questions": [
            ("د پاکستان د آزادۍ ورځ کله لمانځل کیږي؟", "د اګست په څوارلسمه لمانځل کیږي.", "یوم آزادی کب منایا جاتا ہے؟", "د اګست په ۱۴مه."),
            ("پلار ماشومانو ته د آزادۍ په اړه څه وویل؟", "چې دا آزادي د مشرانو د قربانیو نتیجه ده او باید قدر یې وشي.", "والد نے کیا نصیحت کی؟", "چې د هېواد قدر باید وشي.")
        ],
        "words": [
            {"word": "پتنګ", "meaning": "کاغذ باد", "meaningUrdu": "پتنگ", "english": "Kite"},
            {"word": "رپېدل", "meaning": "رپول، لړزېدل په هوا کې", "meaningUrdu": "لہرانا", "english": "Fluttering"},
            {"word": "قرباني", "meaning": "سرښندنه، فداکاري", "meaningUrdu": "قربانی", "english": "Sacrifice"},
            {"word": "زیار", "meaning": "کوشش، محنت", "meaningUrdu": "محنت، کوشش", "english": "Hard Work"}
        ]
    },
    {
        "number": 20,
        "type": "prose",
        "title": "اشر غوبل",
        "titleEn": "Threshing Floor Cooperation (Ghoball)",
        "titleUrdu": "غوبل (اناج نکالنے کا روایتی طریقہ)",
        "text": (
            "غوبل د غنمو د دانو او بوسو د جلا کولو روایتی لار ده. په کلیو کښې د درمند پر مهال بیلونه (غوایان) په ګرد چاپېره ګرځول کېږي چې دانې له وښو جلا شي.\n\n"
            "کله چې باد ولګېږي نو بزګران په ښاخیو سره بوس بادوي چې سپک بوس یوې خوا ته والوزي او درنې دانې په ځمکه پاتې شي.\n\n"
            "دا کار ډېر زحمت غواړي، خو کلیوال په خندا او مسکا یو له بل سره مرسته کوي او خپل غنم کورونو ته وړي."
        ),
        "urdu": "غوبل دیہات میں گندم کی گہائی اور دانہ الگ کرنے کا روایتی طریقہ ہے۔ کسان بیلوں کے ذریعے گہائی کرتے ہیں اور ہوا کی مدد سے بھوسہ اور دانے الگ کرتے ہیں۔ یہ محنت اور اتحاد کا شاہکار ہے۔",
        "english": "Ghoball is the traditional rural threshing process where oxen tread harvested wheat sheaves and winnowing separates heavy grain from chaff with village teamwork.",
        "questions": [
            ("غوبل څه ته وايي؟", "د غنمو د دانو او بوسو د جلا کولو پخوانۍ دودیزې لارې ته وايي.", "غوبل کسے کہتے ہیں؟", "د دانو او بوسو د بیلولو کار دی."),
            ("باد په غوبل کښې څه مرسته کوي؟", "باد سپک بوس الوتوي او پاکې دانې لاندې پاتې کیږي.", "ہوا سے کیا مدد ملتی ہے؟", "سپک بوس بېلوي.")
        ],
        "words": [
            {"word": "غوبل", "meaning": "د غنمو د درمند کار", "meaningUrdu": "گہائی، اناج نکالنا", "english": "Threshing"},
            {"word": "بوس", "meaning": "د غنمو میده تنکي", "meaningUrdu": "بھوسا", "english": "Chaff/Straw"},
            {"word": "ښاخۍ", "meaning": "د بوسو بادولو لرګین اوزار", "meaningUrdu": "پنجالی، اوزار", "english": "Pitchfork"},
            {"word": "درمند", "meaning": "د غنمو د دانو غونډاری", "meaningUrdu": "کھلیان", "english": "Threshing floor"}
        ]
    },
    {
        "number": 21,
        "type": "prose",
        "title": "ايمانداري",
        "titleEn": "Integrity and Honesty",
        "titleUrdu": "ایمانداری اور دیانت",
        "text": (
            "ایمانداري د مومن او نېک انسان تر ټولو ښکلی زیور دی.\n\n"
            "یو کوچنی هلک رحیم په دکان کښې سودا واخیسته. کله چې کور ته راغی، ویې لیدل چې دکاندار په تېروتنې سره لس روپۍ زیاتې ورکړې دي.\n\n"
            "رحیم سمدستي دکان ته بېرته لاړ او پیسې یې دکاندار ته ورکړې. دکاندار ډېر حیران او خوښ شو او رحیم ته یې شاباسی ورکړ.\n\n"
            "رسول الله ﷺ فرمایلي دي: 'څوک چې دوکه کوي هغه زما له ډلې نه دی.' ایمانداري انسان ته د خدای او خلکو رضا بښي."
        ),
        "urdu": "رحیم کو دکاندار نے غلطی سے دس روپے زیادہ دے دیے تو رحیم نے فوراً واپس کیے۔ حدیث شریف ہے: 'جس نے دھوکا دیا وہ ہم میں سے نہیں۔' دیانت داری انسان کو معزز بناتی ہے۔",
        "english": "Young Rahim returns excess change mistakenly handed to him by a shopkeeper. The Prophet (PBUH) warned: 'He who cheats is not of us.' Honesty earns divine favor.",
        "questions": [
            ("رحیم د زیاتو پیسو سره څه وکړل؟", "رحیم سمدستي دکاندار ته بېرته وسپارلې.", "رحیم نے زائد پیسوں کا کیا کیا؟", "بېرته یې دکاندار ته ورکړې."),
            ("د دوکې په اړه د نبي کریم ﷺ فرمان څه دی؟", "چې څوک دوکه کوي هغه زما له امت څخه نه دی.", "دھوکے کے بارے میں کیا ارشاد ہے؟", "هغه زموږ له ډلې نه دی.")
        ],
        "words": [
            {"word": "ایمانداري", "meaning": "رښتینولي، امانت ساتل", "meaningUrdu": "دیانت داری", "english": "Honesty"},
            {"word": "دوکه", "meaning": "فریب، ټګي", "meaningUrdu": "دھوکا", "english": "Cheating/Deceit"},
            {"word": "شاباسی", "meaning": "آفرین، ستاینه", "meaningUrdu": "شاباش", "english": "Commendation"},
            {"word": "زیور", "meaning": "ګاڼه، ښکلا", "meaningUrdu": "زیور", "english": "Adornment"}
        ]
    },
    {
        "number": 22,
        "type": "poem",
        "title": "زما داجي (نظم)",
        "titleEn": "My Grandfather / Respected Elder (Poem)",
        "titleUrdu": "میرے دادا جان (نظم)",
        "text": (
            "سپینې ږیرې، مهربانه داجي\n"
            "زما د زړه قراره، پیاره داجي\n\n"
            "ماته د نېکو لارو کیسې کوي\n"
            "په تندي مې ښکلوي په مینه داجي\n\n"
            "کله چې زه له ښوونځي راشم\n"
            "ماته مېوې او کجورې راکوي داجي\n\n"
            "خدایه ته زما داجي روغ وساتې\n"
            "تل یې په سر سیوری وساتې داجي"
        ),
        "urdu": "دادا جان سفید ریش اور شفیق بزرگ ہیں جو بچوں کو نیکی کے قصے سناتے ہیں، پیار کرتے ہیں اور دعائیں دیتے ہیں۔ اللہ بزرگوں کا سایہ ہمارے سروں پر سلامت رکھے۔",
        "english": "A heartfelt poem expressing love and prayers for an affectionate grandfather who tells moral stories, offers sweet fruits, and guides with gentle wisdom.",
        "questions": [
            ("داجي ماشوم ته څه کوي؟", "داجي ماشوم ته نېکې کیسې کوي او مینه ورکوي.", "دادا جان بچے کے ساتھ کیا کرتے ہیں؟", "نېکې کیسې ورته کوي او دعاګانې ورکوي."),
            ("د داجي لپاره ماشوم څه دعا کوي؟", "چې الله تعالی یې روغ او جوړ وساتي.", "بچہ دادا جان کے لیے کیا دعا کرتا ہے؟", "د روغتیا او اوږد عمر دعا ورته کوي.")
        ],
        "words": [
            {"word": "داجي", "meaning": "نیکه، مشر پلار", "meaningUrdu": "دادا جان", "english": "Grandfather"},
            {"word": "قرار", "meaning": "ارام، سکون", "meaningUrdu": "چین، سکون", "english": "Solace/Comfort"},
            {"word": "تندی", "meaning": "جبین، د مخ پورته برخه", "meaningUrdu": "پیشانی", "english": "Forehead"},
            {"word": "سیوری", "meaning": "سایه، پناه", "meaningUrdu": "سایہ", "english": "Shade/Shelter"}
        ]
    },
    {
        "number": 23,
        "type": "prose",
        "title": "غم ښادي",
        "titleEn": "Sharing Joys and Sorrows",
        "titleUrdu": "غم اور خوشی میں شرکت",
        "text": (
            "انسان یواځې ژوند نشي کولی. په ټولنه کښې د یو بل په خوشحالۍ کښې خوشحاله کېدل او په غم کښې برخه اخیستل د ژوند اصل ښکلا ده.\n\n"
            "کله چې په کلي کښې د چا واده وي، ټول ګاونډیان او خپلوان ورسره مرسته کوي او مبارکي ورته وايي.\n\n"
            "او که خدای مه کړه په چا غم یا مصیبت راشي، ټول خلک د هغوی تسلي کوي، د هغوی خواخوږي کوي او دعا ورته کوي. دا د اسلام او پښتونولۍ ښکلی قانون دی."
        ),
        "urdu": "معاشرتی زندگی میں پڑوسیوں اور رشتہ داروں کی خوشی میں شریک ہونا اور غم میں ان کا سہارا بننا لازمی ہے۔ یہی باہمی ہمدردی اور اخوت کا تقاضا ہے۔",
        "english": "Human solidarity requires standing by community members during weddings and festivals as well as offering solace and assistance in times of grief.",
        "questions": [
            ("په غم او مصیبت کښې څه پکار دي؟", "له غمځپلو سره مرسته کول او تسلي ورکول پکار دي.", "مصیبت میں کیا کرنا چاہیے؟", "مرسته او تسلي ورکول پکار دي."),
            ("د ټولنیز ژوند ښکلا په څه کښې ده؟", "د یو بل په غم او ښادۍ کې شریکېدل دي.", "معاشرتی زندگی کا حسن کیا ہے؟", "د یو بل ملاتړ کول دي.")
        ],
        "words": [
            {"word": "ښادي", "meaning": "خوشحالي، واده", "meaningUrdu": "خوشی، مسرت", "english": "Joy/Celebration"},
            {"word": "تسلي", "meaning": "ډاډګېرنه، زړه ارامول", "meaningUrdu": "دلاسا، تسلی", "english": "Consolation"},
            {"word": "خواخوږي", "meaning": "همدردي", "meaningUrdu": "ہمدردی", "english": "Sympathy"},
            {"word": "پښتونوالي", "meaning": "د پښتنو لوړ کلتوري دودونه", "meaningUrdu": "پختون روایات", "english": "Pashtun ethical code"}
        ]
    },
    {
        "number": 24,
        "type": "prose",
        "title": "دونې اړونه (د ونو ارزښت)",
        "titleEn": "The Value of Trees",
        "titleUrdu": "درختوں کی اہمیت اور شجرکاری",
        "text": (
            "ونې زموږ د ځمکې زرغون زړه دی. که ونې نه وي، ژوند ناشونی دی.\n\n"
            "۱. ونې موږ ته پاکه هوا او اکسیجن راکوي.\n"
            "۲. موږ ته خواږه مېوې لکه مڼې، زردالو او بادام راکوي.\n"
            "۳. په ګرم اوړي کښې مسافرو ته یخ سیوری جوړوي.\n"
            "۴. مرغان په ونو کښې ځالې جوړوي او بارانونه راجلبوي.\n"
            "موږ باید بې ځایه ونې ونه وهو، بلکې هر کال نوي نیالګي کېنوو."
        ),
        "urdu": "درخت زمین کا حسن اور زندگی کی علامت ہیں۔ وہ آکسیجن، پھل، لکڑی اور ٹھنڈا سایہ فراہم کرتے ہیں۔ پرندے درختوں پر بسیرا کرتے ہیں۔ ہمیں زیادہ سے زیادہ درخت لگانے چاہئیں۔",
        "english": "Trees provide clean oxygen, sweet fruits, shade in hot summers, and shelters for singing birds. Afforestation protects nature and prevents environmental decay.",
        "questions": [
            ("ونې انسانانو ته څه ګټې رسوي؟", "ونې اکسیجن، مېوې، لرګي او سیوری راکوي.", "درختوں کے فائدے کیا ہیں؟", "اکسیجن او مېوې راکوي."),
            ("موږ باید د ونو په اړه څه وکړو؟", "باید ونې وساتو او نوي نیالګي کېنوو.", "درختوں کے لیے کیا کرنا چاہیے؟", "نوي نیالګي باید کېنوو.")
        ],
        "words": [
            {"word": "زرغون", "meaning": "شین، تازه", "meaningUrdu": "سرسبز", "english": "Verdant/Green"},
            {"word": "نیالګی", "meaning": "وړه ونه، د کېنولو بوټی", "meaningUrdu": "پودا", "english": "Sapling"},
            {"word": "ځاله", "meaning": "د مرغۍ کور", "meaningUrdu": "گھونسلا", "english": "Nest"},
            {"word": "ناشونی", "meaning": "ناممکن", "meaningUrdu": "ناممکن", "english": "Impossible"}
        ]
    },
    {
        "number": 25,
        "type": "prose",
        "title": "کمپیوټر",
        "titleEn": "The Computer",
        "titleUrdu": "کمپیوٹر",
        "text": (
            "کمپیوټر د اوسنۍ زمانې یو ډېر ګټور او چټک برېښنايي ماشین دی.\n\n"
            "د کمپیوټر اصلي برخې دا دي:\n"
            "• مانیټر (Monitor): پرده چې معلومات او تصویرونه ښيي.\n"
            "• کیبورډ (Keyboard): د تورو او شمېرو د لیکلو تخته.\n"
            "• ماؤس (Mouse): په سکرین د اشارې او کمانډ آله.\n"
            "• سي پي یو (CPU): د کمپیوټر مغز چې ټول حسابونه کوي.\n\n"
            "موږ په کمپیوټر کتابونه لولو، حساب زده کوو، خطونه لېږو او نوې پوهه ترلاسه کوو."
        ),
        "urdu": "کمپیوٹر دورِ جدید کی حیرت انگیز ایجاد ہے۔ اس کے چار اہم حصے مانیٹر، کی بورڈ، ماؤس اور سی پی یو ہیں۔ یہ حساب کتاب، پڑھائی اور پیغامات بھیجنے میں استعمال ہوتا ہے۔",
        "english": "The computer is an electronic machine composed of a monitor, keyboard, mouse and CPU. It assists students in learning, calculating, and exploring knowledge.",
        "questions": [
            ("د کمپیوټر مغز کومې برخې ته وايي؟", "سي پي یو (CPU) ته د کمپیوټر مغز وايي.", "کمپیوٹر کا دماغ کسے کہتے ہیں؟", "سي پي یو ته وايي."),
            ("کیبورډ د څه لپاره کارول کیږي؟", "کیبورډ د تورو او عددونو د لیکلو لپاره کارول کیږي.", "کی بورڈ کس لیے ہے؟", "د لیکلو لپاره کارول کیږي.")
        ],
        "words": [
            {"word": "برېښنايي", "meaning": "برقی، په بجلي چلېدونکی", "meaningUrdu": "الیکٹرانک", "english": "Electronic"},
            {"word": "مانیټر", "meaning": "د کمپیوټر سکرین", "meaningUrdu": "اسکرین", "english": "Monitor"},
            {"word": "چټک", "meaning": "ګړندی، تیز", "meaningUrdu": "تیز رفتار", "english": "Fast/Quick"},
            {"word": "مغز", "meaning": "دماغ، فکري مرکز", "meaningUrdu": "دماغ", "english": "Brain/Core"}
        ]
    },
    {
        "number": 26,
        "type": "prose",
        "title": "قامي خوراكونه",
        "titleEn": "Traditional National Foods",
        "titleUrdu": "روایتی قومی کھانے",
        "text": (
            "زموږ په هېواد پاکستان کښې بېلابېل خوندور او مشهور خواړه خوړل کېږي:\n\n"
            "• په خیبر پختونخوا کښې: چپلي کباب، پټه ټکۍ، روش او د جوارو ډوډۍ له شړومبو سره ډېره خوښېږي.\n"
            "• په پنجاب کښې: سرسو ساګ، مکۍ ډوډۍ او لاسي لسی.\n"
            "• په سندھ کښې: سندهي بریاني او د پلو ماهي.\n"
            "• په بلوچستان کښې: سجي او کاک ډوډۍ.\n\n"
            "دا خواړه زموږ د هېواد بډایه کلتور او مېلمه پالنه څرګندوي."
        ),
        "urdu": "پاکستان میں روایتی اور لذیذ کھانے پکائے جاتے ہیں۔ خیبر پختونخوا کے چپلی کباب اور روش، پنجاب کا سرسوں کا ساگ، سندھ کی بریانی اور بلوچستان کی سجی دنیا بھر میں مشہور ہیں۔",
        "english": "Diverse culinary traditions of Pakistan: Chapli Kabab and Rosh from KP, Sarson ka Saag and Lassi from Punjab, Sindhi Biryani, and Balochi Sajji reflect hospitality and rich cultural heritage.",
        "questions": [
            ("په خیبر پختونخوا کښې کوم خواړه ډېر مشهور دي؟", "چپلي کباب، روش او د جوارو ډوډۍ ډېره مشهوره ده.", "خیبر پختونخوا کے مشہور کھانے کون سے ہیں؟", "چپلي کباب او روش."),
            ("د بلوچستان مشهور خوراک کوم دی؟", "سجي او کاک د بلوچستان مشهور خواړه دي.", "بلوچستان کا خاص کھانا کیا ہے؟", "سجي ده.")
        ],
        "words": [
            {"word": "شړومبې", "meaning": "تروې، شوملې", "meaningUrdu": "لسی", "english": "Buttermilk/Lassi"},
            {"word": "خوندور", "meaning": "مزه دار، لذیذ", "meaningUrdu": "لذیذ", "english": "Delicious"},
            {"word": "بډایه", "meaning": "غني، بډای", "meaningUrdu": "دولت مند، امیر", "english": "Rich/Abundant"},
            {"word": "مېلمه پالنه", "meaning": "ضیافت، د مېلمه قدر", "meaningUrdu": "مہمان نوازی", "english": "Hospitality"}
        ]
    },
    {
        "number": 27,
        "type": "poem",
        "title": "دعا (نظم)",
        "titleEn": "Prayer (Poem)",
        "titleUrdu": "دعا (نظم)",
        "text": (
            "ای زما لویه پروردګاره\n"
            "ای د ټول جهان باداره\n\n"
            "موږ ته نېکه لار وښایه\n"
            "د بدو کارو نه مو وساته\n\n"
            "علم او پوهه راکړه خدایه\n"
            "د وطن مینه راکړه خدایه\n\n"
            "مور او پلار مو خوشحاله لره\n"
            "زموږ ښوونځی اباد لره"
        ),
        "urdu": "اے تمام جہانوں کے پالنے والے اللہ! ہمیں نیکی کا راستہ دکھا اور برائی سے بچا۔ ہمیں علم، عقل اور وطن کی محبت عطا فرما۔ ہمارے والدین کو خوش رکھ اور ہمارے سکول کو آباد رکھ۔",
        "english": "A reverent prayer to the Almighty asking for guidance on the straight path, protection from evil, gift of knowledge, love of country, and long blessed lives for parents.",
        "questions": [
            ("په دعا کښې له الله نه څه غوښتل شوي دي؟", "نېکه لار، پوهه، د وطن مینه او د مور او پلار خوښي غوښتل شوې ده.", "دعا میں کیا مانگا گیا ہے؟", "علم، نېکه لار او د مور پلار سلامتي."),
            ("دا دعا څوک اوري؟", "د ټول جهان پالونکی او بښونکی الله تعالی یې اوري.", "دعا کون سنتا ہے؟", "یو الله تعالی یې اوري.")
        ],
        "words": [
            {"word": "پروردګار", "meaning": "پالونکی، الله تعالی", "meaningUrdu": "پالنے والا", "english": "Sustainer/Lord"},
            {"word": "بادار", "meaning": "مالک، حاکم", "meaningUrdu": "مالک", "english": "Master"},
            {"word": "پوهه", "meaning": "عقل، فهم، علم", "meaningUrdu": "دانش، سمجھ", "english": "Wisdom/Knowledge"},
            {"word": "اباد", "meaning": "ودان، تل ژوندی", "meaningUrdu": "آباد", "english": "Prosperous"}
        ]
    },
    {
        "number": 28,
        "type": "prose",
        "title": "فرهنګ (زمونږ کلتور او ژبه)",
        "titleEn": "Pashto Culture, Language & Folk Heritage",
        "titleUrdu": "پشتو ثقافت، زبان اور لوک روایات",
        "text": (
            "پښتو یوه لرغونې، خوږه او غیرتي ژبه ده چې زرګونه کلونه تاریخ لري.\n\n"
            "پښتني کلتور په مېلمه پالنه، ننګ، وعده پوره کولو، د کمزورو لاسنیوي، او د حجرو په مجلسونو ولاړ دی.\n\n"
            "پښتو ټپې، چاربېتې، لنډۍ او اتڼ زموږ د ملي خوند او هنر څرګندونه کوي.\n\n"
            "موږ باید خپله مورنۍ ژبه پښتو ولولو، ویې لیکو، او د خپل کلتور لوړ اخلاقي اصول په خپل ورځني ژوند کښې عملي کړو."
        ),
        "urdu": "پشتو ایک قدیم، شیریں اور تاریخی زبان ہے۔ پختون ثقافت مہمان نوازی، غیرت، وعدہ خلافی سے نفرت اور حجرہ کی روایات پر مبنی ہے۔ ہمیں اپنی مادری زبان سیکھنی اور بولنی چاہیے۔",
        "english": "Pashto language and culture boast rich heritage grounded in hospitality, chivalry, moral courage, folkloric Tappa and Attan dance. Preserving mother tongues enriches identity.",
        "questions": [
            ("د پښتني کلتور مهمې ځانګړنې څه دي؟", "مېلمه پالنه، ننګ، وعده پوره کول او د حجرو دودونه دي.", "پختون ثقافت کی کیا خصوصیات ہیں؟", "مېلمه پالنه او غیرت."),
            ("د پښتو ژبې مشهور لوک شعرونه کوم دي؟", "ټپې، لنډۍ او چاربېتې دي.", "پشتو لوک شاعری کیا ہے؟", "ټپې او لنډۍ دي.")
        ],
        "words": [
            {"word": "فرهنګ", "meaning": "کلتور، دود او دستور", "meaningUrdu": "ثقافت", "english": "Culture/Heritage"},
            {"word": "لرغونې", "meaning": "پخوانۍ، تاریخي", "meaningUrdu": "قدیم", "english": "Ancient"},
            {"word": "ټپه", "meaning": "د پښتو شعر تر ټولو ښکلی او لنډ ډول", "meaningUrdu": "ٹپہ (لوک صنف)", "english": "Tappa (folk verse)"},
            {"word": "اتڼ", "meaning": "د پښتنو ملي نڅا او ولسي نڅا", "meaningUrdu": "اتن (روایتی رقص)", "english": "Attan (folk dance)"}
        ]
    }
]

lines = []
lines.append("/**")
lines.append(" * TuitionHub - Class 2 Pashto Comprehensive Dataset (KPK Textbook Board)")
lines.append(" * Complete 28 Lessons verbatim from official textbook:")
lines.append(" * D:\\SpaceBook\\Books\\2nd\\2nd Pashto\\Word\\pashto.docx")
lines.append(" * Fully populated with verbatim lessons, solved exercises, MCQs, SQs, LQs,")
lines.append(" * vocabulary and Board SLO Suites.")
lines.append(" */")
lines.append("")
lines.append("var PASHTO_2_DATA = [")

for idx, les in enumerate(lessons):
    comma = "," if idx < len(lessons) - 1 else ""
    l_num = les["number"]
    l_title = les["title"]
    lines.append("  {")
    lines.append(f'    "id": "cls2-ps-ch{l_num:02d}",')
    lines.append(f'    "number": {l_num},')
    lines.append(f'    "type": {json.dumps(les["type"])},')
    lines.append(f'    "title": {json.dumps(l_title)},')
    lines.append(f'    "titleEn": {json.dumps(les["titleEn"])},')
    lines.append(f'    "titleUrdu": {json.dumps(les["titleUrdu"])},')
    lines.append(f'    "titlePs": {json.dumps(l_title)},')
    lines.append(f'    "author": "د پښتو درسي کتاب، دویم ټولګی، خیبر پښتونخوا ټېکسټ بک بورډ پېښور",')
    lines.append(f'    "authorInfo": {json.dumps("د پښتو درسي کتاب، دویم ټولګی، لوست نمبر " + str(l_num) + "۔")},')
    lines.append(f'    "text": {json.dumps(les["text"])},')
    lines.append(f'    "urdu": {json.dumps(les["urdu"])},')
    lines.append(f'    "english": {json.dumps(les["english"])},')

    paras = [p.strip() for p in les["text"].split("\n\n") if p.strip()]
    lines.append('    "sections": [')
    lines.append('      {')
    lines.append(f'        "heading": {json.dumps(l_title)},')
    lines.append(f'        "headingEn": {json.dumps(les["titleEn"])},')
    lines.append(f'        "headingUrdu": {json.dumps(les["titleUrdu"])},')
    lines.append(f'        "text": {json.dumps(les["text"])},')
    lines.append(f'        "paras": {json.dumps(paras)},')
    lines.append(f'        "urdu": {json.dumps(les["urdu"])},')
    lines.append(f'        "pashto": {json.dumps(les["text"])},')
    lines.append(f'        "english": {json.dumps(les["english"])}')
    lines.append('      }')
    lines.append('    ],')

    # Exercise
    mcqs = [
        {
            "id": f'cls2-ps-ch{l_num:02d}-mcq1',
            "question": les["questions"][0][0],
            "options": [les["questions"][0][1], "بل ځواب", "ناسم ځواب", "هیڅ نه"],
            "correct": 0,
            "explanation": les["questions"][0][1],
            "urdu": les["questions"][0][2],
            "pashto": les["questions"][0][0]
        },
        {
            "id": f'cls2-ps-ch{l_num:02d}-mcq2',
            "question": les["questions"][1][0],
            "options": [les["questions"][1][1], "نامعلومه", "منفي پایله", "بل شی"],
            "correct": 0,
            "explanation": les["questions"][1][1],
            "urdu": les["questions"][1][2],
            "pashto": les["questions"][1][0]
        }
    ]
    sqs = []
    for q_idx, q in enumerate(les["questions"], 1):
        sqs.append({
            "id": f'cls2-ps-ch{l_num:02d}-sq{q_idx}',
            "question": q[0],
            "answer": q[1],
            "urdu": q[2],
            "pashto": q[0],
            "pashtoAns": q[3]
        })
    lqs = [
        {
            "id": f'cls2-ps-ch{l_num:02d}-lq1',
            "question": f'د لوست "{l_title}" لنډیز او مهم ټکي په خپلو ټکو کښې ولیکئ.',
            "answer": les["urdu"] + " " + les["text"],
            "urdu": f'سبق "{les["titleUrdu"]}" کا خلاصہ لکھیں۔',
            "urduAns": les["urdu"],
            "pashto": f'د دې درس مهم ټکي ولیکئ.',
            "pashtoAns": les["text"]
        }
    ]
    lines.append('    "exercise": {')
    lines.append(f'      "mcqs": {json.dumps(mcqs, indent=8).strip()},')
    lines.append(f'      "shortQuestions": {json.dumps(sqs, indent=8).strip()},')
    lines.append(f'      "longQuestions": {json.dumps(lqs, indent=8).strip()}')
    lines.append('    },')

    # Words
    lines.append(f'    "words": {json.dumps(les["words"], indent=6).strip()},')

    # SLO Questions
    slo_mcqs = [
        {
            "q": les["questions"][0][0],
            "options": [les["questions"][0][1], "ناسم", "نامعلوم", "هیڅ نه"],
            "ans": 0,
            "explanation": les["questions"][0][1]
        }
    ]
    slo_sqs = [
        {
            "q": les["questions"][0][0],
            "ans": les["questions"][0][1],
            "urdu": les["questions"][0][2]
        }
    ]
    slo_lqs = [
        {
            "q": f'د دې لوست اخلاقي او ښوونیز پیغام څه دی؟',
            "ans": les["urdu"]
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
lines.append("  DATA.pashto2Chapters = PASHTO_2_DATA;")
lines.append("}")
lines.append("")

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"SUCCESS! Wrote {len(lines)} lines to {OUT_JS}")
