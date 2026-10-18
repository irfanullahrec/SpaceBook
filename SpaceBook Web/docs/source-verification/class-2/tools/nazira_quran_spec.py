"""Page spec for Class 2 Nazira Para 1 / Para 2 (scan idx, printed page, ayah ranges, side boxes) — read from the scans.
Run:  python nazira_quran_spec.py   (writes every page via nazira_quran.write())"""
import nazira_quran as nq
from nazira_quran import page, ACT1, MADD


def box(title, items):
    return [f'box note | {title}'] + ['- ' + i for i in items] + ['endbox']


def act(find):
    """'سرگرمیاں' box: find the given words and underline them (example word), then the two standard items."""
    return box('سرگرمیاں || Activities || فعالیتونه', [find] + ACT1[2:4])


STD = 'کمرۂ جماعت میں سرگرمیاں بچّوں سے کروائیے اور تمام بچّوں کو برابر موقع دیجیے۔ || Do the activities with the children in class and give every child an equal chance. || فعالیتونه په ټولګي کې وکړئ او ټولو ته برابر فرصت ورکړئ.'
ACT2 = ['درست ادائی کی مشق کیجیے اور ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔ || Practise correct reading and read to one another with correct pronunciation. || د سم ادا تمرین وکړئ او یو بل ته په سم تلفظ ولولئ.',
        'کمرۂ جماعت میں بچّوں کے سامنے بلند آواز سے پڑھنے کا عملی مظاہرہ کیجیے۔ || Demonstrate reading aloud in front of the class. || په ټولګي کې د لوړ غږ د لوستلو ښودنه وکړئ.']


def act2(find):
    return box('سرگرمیاں || Activities || فعالیتونه', [find] + ACT2)


JAZM = box('یاد رکھیے — جزم، قلقلہ، ہمزہ ساکن || Remember — jazm, qalqalah, hamzah sakin || یاد ولرئ — جزم، قلقله، ساکن همزه', [
    'جزم: جس حرف پر جزم ہو اس حرف کو پچھلے حرف کے ساتھ ملا کر پڑھتے ہیں۔ مثالیں: بَلْ، فِیْ، مِنْ، هَلْ۔ || Jazm: a letter with jazm is read joined to the letter before it. Examples: bal, fee, min, hal. || جزم: د جزم توری له مخکیني توري سره یوځای لوستل کېږي.',
    'قلقلہ: جب حروف ق ط ب ج د پر جزم ہو یا ان پر وقف کیا جائے تو آواز ٹکرا کر واپس آتی ہے۔ مثالیں: يَقْبَلُ، يُطْعِمُ، عَبْدٌ، قَبْلِ۔ || Qalqalah: when ق ط ب ج د carry jazm or are stopped on, the sound bounces back. Examples: yaqbalu, yut\'imu, \'abdun, qabli. || قلقله: کله چې ق ط ب ج د ساکن وي یا پرې وقف وشي، غږ راګرځي.',
    'ہمزہ ساکن: اگر ہمزہ پر جزم ہو یعنی ہمزہ ساکن ہو تو اس کو جھٹکا دے کر پڑھنا ہے۔ مثالیں: بَاْسٌ، يَاْمُرُ، يُؤْمِنُ۔ || Hamzah sakin: a hamzah with jazm is read with a slight catch. Examples: ba\'s, ya\'muru, yu\'minu. || ساکنه همزه په لږ ټکان لوستل کېږي.'])
MAKH = box('یاد رکھیے — حروف کی صفات || Remember — qualities of the letters || یاد ولرئ — د تورو صفات', [
    'ث ذ ظ کی آوازوں میں مخارج کے لحاظ سے فرق کرنا ہے۔ || Tell apart ث ذ ظ by their points of articulation. || ث ذ ظ د مخارجو له مخې توپیر کړئ.',
    'ت ط کی آوازوں میں مخارج کے لحاظ سے فرق کرنا ہے۔ || Tell apart ت ط by their points of articulation. || ت ط توپیر کړئ.',
    'ض ز ظ کی آوازوں میں مخارج کے لحاظ سے فرق کرنا ہے۔ || Tell apart ض ز ظ. || ض ز ظ توپیر کړئ.',
    'ث س ص کی آوازوں میں مخارج کے لحاظ سے فرق کرنا ہے۔ || Tell apart ث س ص. || ث س ص توپیر کړئ.',
    'ا ہ ع کی آوازوں میں مخارج کے لحاظ سے فرق کرنا ہے۔ || Tell apart ا ه ع. || ا ه ع توپیر کړئ.',
    'ح ہ خ کی آوازوں میں مخارج کے لحاظ سے فرق کرنا ہے۔ || Tell apart ح ه خ. || ح ه خ توپیر کړئ.',
    'خ ص ض غ ط ق ظ — یہ حروف ہمیشہ موٹی آواز سے پڑھے جاتے ہیں۔ || خ ص ض غ ط ق ظ are always read heavy (full-mouthed). || دا توري تل درانه لوستل کېږي.',
    'حرف را ( ر ) کے اوپر جب زبر یا پیش ہو تو اس کو بھی موٹی آواز سے پڑھنا ہے۔ || When ra ( ر ) has zabar or pesh, it is also read heavy. || کله چې ر زبر یا پېښ ولري، درانه لوستل کېږي.'])
GHUNNA = box('یاد رکھیے — غنّہ || Remember — ghunnah || یاد ولرئ — غنه', [
    'جب میم یا نون پر شد ہو، مثال: اُمَّ، اِنَّ، تو غنّہ کرنا ہے۔ || When mim or nun has a shadd (e.g. umma, inna), make ghunnah. || کله چې م یا ن شد ولري، غنه وکړئ.',
    'جب جزم والے میم کے بعد حرف میم یا حرف با ہو تو غنّہ کرنا ہے۔ مثالیں: اَمْ مَّا، اَمْ بِهٖ، لَهُمْ مَّا۔ || When mim sakin is followed by mim or ba, make ghunnah. Examples: am maa, am bihi, lahum maa. || کله چې ساکن م وروسته م یا ب راشي، غنه وکړئ.',
    'جب جزم والے نون یا تنوین کے بعد حروف ء ہ ع ح غ خ ل ی ا ر د کے علاوہ کوئی بھی حرف ہو تو غنّہ ہوگا۔ مثالیں: اَنْتَ، عِنْدَ، اِنْ كُنْتُمْ، عَنْ سَبِيْلٍ، فَصَبْرٌ جَمِيْلٌ، رِزْقٌ كَرِيْمٌ۔ || When nun sakin or tanween is followed by any letter other than ء ه ع ح غ خ ل ی ا ر د, there is ghunnah. Examples: anta, \'inda, in kuntum, \'an sabeelin, fasabrun jameel, rizqun kareem. || کله چې له ساکن ن یا تنوین وروسته له دې تورو پرته بل توری وي، غنه کېږي.',
    'جب جزم والے نون یا تنوین کے بعد حروف ی ن م و ہوں تو غنّہ کرنا ہے۔ مثالیں: مَنْ يَّعْمَلْ، شَیْءٍ نَّحْنُ، عَدُوٌّ مُّبِيْنٌ، غِشَاوَةٌ وَّلَهُمْ۔ || When nun sakin or tanween is followed by ی ن م و, make ghunnah. Examples: man ya\'mal, shay\'in nahnu, \'aduwwun mubeen, ghishaawatun wa lahum. || کله چې وروسته ی ن م و راشي، غنه وکړئ.'])
MADD2 = MADD[:-1] + [
    '- جن حروف پر کھڑی زبر، کھڑی زیر اور اُلٹا پیش ہو ان حروف کی آواز کو بھی حروفِ مدّہ کی طرح تھوڑا کھینچ کر پڑھنا ہے۔ مثالیں: اٰلِ، اٰخَرَ، اِلٰهِهٖ، بِهٖ، لَهٗ، مَعَهٗ۔ || Letters with standing zabar, standing zer or inverted pesh are also drawn out a little, like the letters of madd. Examples: aali, aakhara, ilaahihi, bihi, lahu, ma\'ahu. || د ولاړ زبر، ولاړ زېر او سرچپه پېښ توري هم لږ اوږد لوستل کېږي.',
    '- مد ( ٓ ): مد کے معنی آواز کو کھینچنا ہے۔ جس حرف پر مد ہو اس کی آواز کو حروفِ مدّہ کے مقابلے میں خوب کھینچ کر پڑھنا ہے۔ مثالیں: جَآءَ، شَآءَ، مَآءٍ۔ || Madd ( ٓ ) means stretching the sound. A letter with madd is drawn out much longer than the letters of madd. Examples: jaa\'a, shaa\'a, maa\'in. || مد یعنې غږ اوږدول؛ د مد توری ډېر اوږد لوستل کېږي.', 'endbox']

T_MADD = 'بچّوں کو ”یاد رکھیے“ کے تحت حروفِ مدّہ کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about the letters of madd and give examples from this page. || د مد تورو په اړه ووایئ او له دې مخه بېلګې ورکړئ.'
T_JAZM = 'بچّوں کو ”یاد رکھیے“ کے تحت جزم، قلقلہ اور ہمزہ ساکن کی شناخت کروائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", help the children identify jazm, qalqalah and hamzah sakin and give examples from this page. || جزم، قلقله او ساکنه همزه وروپېژنئ.'
T_MAKH = 'بچّوں کو ”یاد رکھیے“ کے تحت حروف کی صفات کا اعادہ کروائیے۔ || Under "Remember", revise the qualities of the letters. || د تورو صفات تکرار کړئ.'
T_GHUN = 'بچّوں کو ”یاد رکھیے“ کے تحت غنّہ کے قواعد کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children the rules of ghunnah and give examples from this page. || د غنې قواعد ووایئ او بېلګې ورکړئ.'
T_MADD2 = 'بچّوں کو ”یاد رکھیے“ کے تحت حروفِ مدّہ، کھڑی حرکات اور مد کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about the letters of madd, the standing vowels and madd, with examples from this page. || د مد تورو، ولاړو حرکتونو او مد په اړه ووایئ.'

page(49, 47, [(2, 24, 29)], act2('حروفِ مدّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (تَفْعَلُوْا) لگائیے۔ || Find the words with the letters of madd and underline them (e.g. taf\'aloo). || د مد تورو کلمې ومومئ او لاندې یې کرښه وکاږئ.'), STD, mushaf=4)
page(50, 48, [(2, 30, 37)], JAZM, T_JAZM, mushaf=5)
page(51, 49, [(2, 38, 48)], act2('مد والے الفاظ تلاش کیجیے اور لفظ کے ساتھ ( يٰبَنِیْٓ اِسْرَآءِيْلَ ) کا نشان لگائیے۔ || Find the words with madd and mark them (e.g. yaa banee israa\'eel). || د مد کلمې ومومئ او نښه یې کړئ.'), STD, mushaf=6)
page(52, 50, [(2, 49, 57)], MAKH, T_MAKH, mushaf=7)
page(53, 51, [(2, 58, 61)], act2('حروفِ لین والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (عَصَوْا) لگائیے۔ || Find the words with the letters of leen and underline them (e.g. \'asaw). || د لین تورو کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf=8)
page(54, 52, [(2, 62, 69)], GHUNNA, T_GHUN, mushaf=9)
page(55, 53, [(2, 70, 76)], act2('غنّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (اِنَّ) لگائیے۔ || Find the words with ghunnah and underline them (e.g. inna). || د غنې کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf=10,
     issue='The top of this scan is blurred by a scanning fault; the Mushaf text itself is clear.')
page(56, 54, [(2, 77, 83)], MADD2, T_MADD2, mushaf=11, issue='The top of this scan is blurred by a scanning fault; the Mushaf text itself is clear.')

LEEN = box('یاد رکھیے — حروفِ لین || Remember — the letters of leen || یاد ولرئ — د لین توري', [
    'جزم والے واؤ ( وْ ) سے پہلے والے حرف پر زبر ہو تو واؤ کی آواز کو نرمی کے ساتھ پڑھنا ہے۔ مثالیں: يَوْ، تَوْ، خَوْفٌ، فَوْقَ۔ || If the letter before a waw with jazm has a zabar, the waw is read softly. Examples: yaw, taw, khawfun, fawqa. || که د ساکن و مخکې توری زبر ولري، و په نرمۍ لوستل کېږي.',
    '( یْ ) جزم والی ہو اور اس سے پہلے حرف کے اوپر زبر ہو تو یْ کی آواز کو نرمی کے ساتھ پڑھنا ہے۔ مثالیں: بَیْ، تَیْ، كَيْفَ، لَيْسَ۔ || If a ya has jazm and the letter before it has a zabar, the ya is read softly. Examples: bay, tay, kayfa, laysa. || که ی ساکنه وي او مخکې توری زبر ولري، په نرمۍ لوستل کېږي.'])
T_LEEN = 'بچّوں کو ”یاد رکھیے“ کے تحت حروفِ لین کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about the letters of leen and give examples from this page. || د لین تورو په اړه ووایئ او بېلګې ورکړئ.'
TORN = 'A corner of this page is torn in the scan; only the margin is affected and the Mushaf text is complete.'
page(57, 55, [(2, 84, 88)], act2('قلقلہ والے الفاظ تلاش کیجیے اور لفظ کے ساتھ (اَقْرَرْتُمْ) کا نشان لگائیے۔ || Find the words with qalqalah and mark them (e.g. aqrartum). || د قلقلې کلمې ومومئ او نښه یې کړئ.'), STD, mushaf=12)
page(58, 56, [(2, 89, 93)], LEEN, T_LEEN, mushaf=13)
page(59, 57, [(2, 94, 101)], act2('حروفِ لین والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (اَلْمَوْتَ) لگائیے۔ || Find the words with the letters of leen and underline them (e.g. al-mawta). || د لین کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf=14, issue=TORN)
page(60, 58, [(2, 102, 105)], MAKH, T_MAKH, mushaf=15, issue=TORN)

STAND = box('یاد رکھیے — کھڑی زبر، کھڑی زیر، الٹا پیش || Remember — standing zabar, standing zer, inverted pesh || یاد ولرئ — ولاړ زبر، ولاړ زېر، سرچپه پېښ', [
    'جن حروف پر کھڑی زبر، کھڑی زیر اور الٹا پیش ہو ان حروف کی آواز کو بھی بالترتیب زبر، زیر اور پیش کے مقابلے میں تھوڑا کھینچ کر پڑھتے ہیں۔ مثالیں: اٰلِ، اٰخَرَ، اِلٰهِهٖ، بِهٖ، لَهٗ، مَعَهٗ۔ || Letters with standing zabar, standing zer and inverted pesh are read a little longer than ordinary zabar, zer and pesh. Examples: aali, aakhara, ilaahihi, bihi, lahu, ma’ahu. || د ولاړ زبر، ولاړ زېر او سرچپه پېښ توري د عادي حرکتونو په پرتله لږ اوږد لوستل کېږي.'])
T_STAND = 'بچّوں کو ”یاد رکھیے“ کے تحت کھڑی زبر، کھڑی زیر اور الٹا پیش کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about standing zabar, standing zer and inverted pesh, with examples from this page. || د ولاړو حرکتونو په اړه ووایئ او بېلګې ورکړئ.'
MADD3 = MADD2[:-2] + ['endbox']
T_MADD3 = 'بچّوں کو ”یاد رکھیے“ کے تحت حروفِ مدّہ اور کھڑی زبر کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about the letters of madd and the standing zabar, with examples from this page. || د مد تورو او ولاړ زبر په اړه ووایئ.'
page(61, 59, [(2, 106, 112)], act2('کھڑی زبر، کھڑی زیر اور الٹا پیش والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (نَصٰرٰی) لگائیے۔ || Find words with standing zabar, standing zer and inverted pesh and underline them (e.g. nasaaraa). || د ولاړو حرکتونو کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf=16)
page(62, 60, [(2, 113, 119)], STAND, T_STAND, mushaf=17)
page(63, 61, [(2, 120, 126)], act2('مد والے الفاظ تلاش کیجیے اور لفظ کے ساتھ (لِلطَّآئِفِيْنَ) کا نشان لگائیے۔ || Find the words with madd and mark them (e.g. lit-taa’ifeena). || د مد کلمې ومومئ او نښه یې کړئ.'), STD, mushaf=18)
page(64, 62, [(2, 127, 134)], MADD3, T_MADD3, mushaf=19)

page(65, 63, [(2, 135, 141)], act2('حروفِ مدّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (اِلٰهًا) لگائیے۔ || Find the words with the letters of madd and underline them (e.g. ilaahan). || د مد تورو کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf=20,
     issue='This page ends the first Para (Al-Baqarah 2:141).')
page(68, 66, [(2, 142, 146)], MADD3, T_MADD3, head=['@sec para2 | دوسرا پارہ || Para 2 || دویم پاره'], mushaf='2:1')

T_GHUN2 = 'بچّوں کو ”یاد رکھیے“ کے تحت غنّہ کے قواعد کا اعادہ کروائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", revise the rules of ghunnah and give examples from this page. || د غنې قواعد تکرار کړئ او بېلګې ورکړئ.'
page(69, 67, [(2, 147, 156)], act2('حروفِ مدّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (تَكُوْنَنَّ) لگائیے۔ || Find the words with the letters of madd and underline them (e.g. takoonanna). || د مد تورو کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf='2:2')
page(70, 68, [(2, 157, 164)], GHUNNA, T_GHUN2, mushaf='2:3')

T_MADDR = 'بچّوں کو ”یاد رکھیے“ کے تحت حروفِ مدّہ کا اعادہ کروائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", revise the letters of madd and give examples from this page. || د مد توري تکرار کړئ او بېلګې ورکړئ.'
page(71, 69, [(2, 165, 172)], act2('غنّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (وَمِنَ النَّاسِ) لگائیے۔ || Find the words with ghunnah and underline them (e.g. wa minan-naasi). || د غنې کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf='2:4')
page(72, 70, [(2, 173, 177)], MADD, T_MADDR, mushaf='2:5')

T_WAW = 'بچّوں کو ”یاد رکھیے“ کے تحت واؤ مدّہ اور واؤ لین کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about the waw of madd and the waw of leen, with examples from this page. || د مد واو او د لین واو په اړه ووایئ.'
page(73, 71, [(2, 178, 184)], act2('حروفِ مدّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (اٰمَنُوْا) لگائیے۔ || Find the words with the letters of madd and underline them (e.g. aamanoo). || د مد تورو کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf='2:6')
page(74, 72, [(2, 185, 187)], LEEN, T_WAW, mushaf='2:7')

STAND2 = box('یاد رکھیے || Remember || یاد ولرئ', ['کھڑی زبر، کھڑی زیر اور الٹا پیش کو بالترتیب زبر، زیر اور پیش کے مقابلے میں ذرہ لمبا کر کے پڑھتے ہیں۔ || Standing zabar, standing zer and inverted pesh are read a little longer than zabar, zer and pesh respectively. || ولاړ زبر، ولاړ زېر او سرچپه پېښ لږ اوږد لوستل کېږي.'])
T_STAND2 = 'بچّوں کو ”یاد رکھیے“ کے تحت کھڑی زبر، کھڑی زیر اور الٹا پیش کی شناخت کروائیے اور درست ادائی کے لیے اس صفحے سے مثالیں دیجیے۔ || Under "Remember", help the children identify standing zabar, standing zer and inverted pesh and give examples from this page for correct reading. || د ولاړو حرکتونو پېژندنه وکړئ او بېلګې ورکړئ.'
page(75, 73, [(2, 188, 193)], act2('حروفِ لین والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (بَيْنَكُمْ) لگائیے۔ || Find the words with the letters of leen and underline them (e.g. baynakum). || د لین کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf='2:8')
page(76, 74, [(2, 194, 197)], STAND2, T_STAND2, mushaf='2:9')

TEAR = 'A tear runs down the side panel of this scan; the side box is read from the visible parts. The Mushaf text is complete.'
page(77, 75, [(2, 198, 203)], act2('کھڑی زبر والے الفاظ تلاش کیجیے اور لفظ کے ساتھ (عَرَفٰتٍ) کا نشان لگائیے۔ || Find the words with standing zabar and mark them (e.g. ‘arafaatin). || د ولاړ زبر کلمې ومومئ او نښه یې کړئ.'), STD, mushaf='2:10', issue=TEAR)
page(78, 76, [(2, 204, 211)], JAZM, T_JAZM, mushaf='2:11', issue=TEAR)

page(79, 77, [(2, 212, 215)], act2('قلقلہ والے الفاظ تلاش کیجیے اور لفظ کے ساتھ (حَسِبْتُمْ) کا نشان لگائیے۔ || Find the words with qalqalah and mark them (e.g. hasibtum). || د قلقلې کلمې ومومئ او نښه یې کړئ.'), STD, mushaf='2:12')
page(80, 78, [(2, 216, 219)], GHUNNA, T_GHUN2, mushaf='2:13')

T_STAND3 = 'بچّوں کو ”یاد رکھیے“ کے تحت کھڑی زبر، کھڑی زیر اور الٹا پیش کی شناخت کا اعادہ کروائیے اور درست ادائی کے لیے اس صفحے سے مثالیں دیجیے۔ || Under "Remember", revise standing zabar, standing zer and inverted pesh and give examples from this page. || د ولاړو حرکتونو تکرار وکړئ او بېلګې ورکړئ.'
page(81, 79, [(2, 220, 224)], act2('غنّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (اِنَّ) لگائیے۔ || Find the words with ghunnah and underline them (e.g. inna). || د غنې کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf='2:14')
page(82, 80, [(2, 225, 229)], STAND, T_STAND3, mushaf='2:15')

page(83, 81, [(2, 230, 232)], act2('کھڑی زبر، کھڑی زیر اور الٹا پیش والے الفاظ تلاش کیجیے اور لفظ کے ساتھ (حَتّٰی) کا نشان لگائیے۔ || Find words with standing zabar, standing zer and inverted pesh and mark them (e.g. hattaa). || د ولاړو حرکتونو کلمې ومومئ او نښه یې کړئ.'), STD, mushaf='2:16')
page(84, 82, [(2, 233, 235)], JAZM, T_JAZM, mushaf='2:17')

CORNER = 'The top corner of this page is torn in the scan; only the margin is affected and the Mushaf text is complete.'
page(85, 83, [(2, 236, 242)], act2('قلقلہ والے الفاظ تلاش کیجیے اور لفظ کے ساتھ (قَبْلِ) کا نشان لگائیے۔ || Find the words with qalqalah and mark them (e.g. qabli). || د قلقلې کلمې ومومئ او نښه یې کړئ.'), STD, mushaf='2:18', issue=CORNER)
page(86, 84, [(2, 243, 247)], MADD3, T_MADDR, mushaf='2:19', issue=CORNER)
page(87, 85, [(2, 248, 252)], act2('حروفِ مدّہ والے الفاظ تلاش کیجیے اور ان کے نیچے لائن (فَشَرِبُوْا) لگائیے۔ || Find the words with the letters of madd and underline them (e.g. fasharibu). || د مد تورو کلمې ومومئ او کرښه یې وکاږئ.'), STD, mushaf='2:20',
     issue='This page ends the second Para (Al-Baqarah 2:252), which is also where Juz 2 ends; the book is complete. ' + CORNER)

if __name__ == '__main__':
    nq.write()
