"""HPE XII PDF48–53: pp.43–48 — accidents (road accident, first aid), snake bite, sleeping pills, stoppage of breathing; chapter 4 exercise.
Run: python class12_hpe_page048.py N (48–53)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p48():
    b = Builder()
    b.h('Accidents', 'حادثات', 'پېښې')
    P(b, [('Among accidents, accidents such as road accident, snake bite, taking sleeping pills and stoppage of breathing often occur; for them the following medical aid should be given.',
           'حادثات میں روڈ ایکسیڈنٹ، سانپ کا کاٹنا، خواب آور گولیاں کھا لینا، سانس کا بند ہونا جیسے حادثات اکثر پیش آتے ہیں ان کیلئے درج ذیل طبی امداد دی جائے۔',
           'په پېښو کې د سړک ټکر، د مار چیچل، د خوب ګولۍ خوړل، د ساه بندېدل په څېر پېښې ډېری وخت کېږي؛ د دوی لپاره دې لاندې طبي مرسته ورکړل شي.')])
    b.h('Road accident', 'روڈ ایکسیڈنٹ', 'د سړک پېښه')
    P(b, [('There is a fear of accidents occurring on the road on the basis of the following causes.', 'روڈ پر درج ذیل وجوہات کی بنا پر حادثات پیش آنے کا خدشہ ہوتا ہے۔', 'پر سړک د لاندې لاملونو له امله د پېښو وېره وي.')])
    L(b, [('Crossing the road in a careless way.', 'غیر محتاط طریقہ سے روڈ کراس کرنا۔', 'په بې‌احتیاطۍ سړک تېرول.'),
          ('Overtaking in a wrong way.', 'غلط انداز سے اوور ٹیکنگ کرنا۔', 'په ناسم ډول مخکې کېدل (اوور ټېکنګ).'),
          ('Excessive speed.', 'رفتار کا زیادہ ہونا۔', 'ډېر سرعت.'),
          ('Failure of the brake of a vehicle or motorcycle.', 'گاڑی، موٹر سائیکل کی بریک کا خراب ہونا۔', 'د موټر یا موټرسایکل د بریک خرابېدل.'),
          ('Driving a vehicle in a state of intoxication.', 'نشہ کی حالت میں گاڑی چلانا۔', 'د نشې په حالت کې موټر چلول.'),
          ('Because of slipperiness in rain.', 'بارش میں پھسلن کی وجہ سے۔', 'په باران کې د ښویدو له امله.')])
    P(b, [('If someone is injured because of these conditions, then the following immediate medical aid should be given.', 'اگر ان حالات کی وجہ سے کوئی زخمی ہو جائے تو درج ذیل فوری طبی امداد دینی چاہیے۔', 'که د دې حالاتو له امله څوک ټپي شي، لاندې سمدستي طبي مرسته دې ورکړل شي.')])
    r = rec(b, 4, 16, 48)
    deco(r, 'A photograph of a crashed car beside a truck on a highway is decorative.')
    BOOK.save(48, [(4, r)])


def p49():
    b = Builder()
    L(b, [('The situation should be examined carefully.', 'حالات کا بغور معائنہ کیا جائے۔', 'حالات دې په غور وکتل شي.'),
          ('The injury should be checked.', 'چوٹ کی جانچ کی جائے۔', 'ټپ دې وکتل شي.'),
          ('If blood is flowing, first it should be stopped.', 'خون بہہ رہا ہو تو پہلے اسے بند کیا جائے۔', 'که وینه بهېږي، لومړی دې ودرول شي.'),
          ('Take the affected person to an open place and let air reach him.', 'متاثرہ شخص کو کھلی جگہ لے جائیں اور ہوا لگنے دیں۔', 'اغېزمن کس خلاص ځای ته یوسئ او هوا ته یې پرېږدئ.'),
          ('Encourage him and give support.', 'اس کی حوصلہ افزائی کریں اور سہارا دیں۔', 'ویې هڅوئ او ملاتړ یې وکړئ.'),
          ('If breathing is stopping, restore the breathing.', 'اگر سانس بند ہو رہی ہو تو سانس کو بحال کریں۔', 'که ساه بندېږي، ساه بېرته راوستئ.'),
          ('Avoid haste.', 'جلد بازی سے گریز کریں۔', 'له بېړې ډډه وکړئ.'),
          ('If some bone has broken, do not disturb it.', 'اگر کوئی ہڈی ٹوٹ گئی ہو تو اسے نہ چھیڑیں۔', 'که کوم هډوکی مات شوی وي، لاس مه ورته وروړئ.'),
          ('Clean the wounds on the spot.', 'زخموں کو موقع پر صاف کریں۔', 'ټپونه په ځای پاک کړئ.'),
          ('Try to take him to hospital as soon as possible.', 'جلد از جلد ہسپتال پہنچانے کی کوشش کریں۔', 'هڅه وکړئ چې ژر تر ژره روغتون ته ورسول شي.')])
    b.h('Snake bite', 'سانپ کا کاٹنا', 'د مار چیچل')
    P(b, [('Most snakes are not poisonous, and if they bite there is no danger to life. However some are very poisonous, from whose bite death can occur. Therefore if such an incident happens, see that where the snake has bitten, if two tooth marks are present there, then this is a poisonous snake.',
           'اکثر سانپ زہریلے نہیں ہوتے اور کاٹ لیں تو جان کو خطرہ نہیں ہوتا۔ البتہ کچھ بہت زہریلے ہوتے ہیں جن کے کاٹنے سے موت واقع ہو سکتی ہے اس لیے اگر ایسا کوئی واقع ہو جائے تو یہ دیکھیں کہ جہاں سانپ نے کاٹا ہے اگر وہاں دو دانتوں کے نشان موجود ہوں تو یہ زہریلا سانپ ہے۔',
           'ډېری مارونه زهرجن نه وي او که وچیچي، ژوند ته خطر نه وي. خو ځینې ډېر زهرجن وي چې د چیچلو له امله یې مرګ کېدای شي؛ نو که داسې پېښه وشي، وګورئ چې مار چېرته چیچلي، که هلته د دوو غاښونو نښې وي، نو دا زهرجن مار دی.')])
    r = rec(b, 4, 17, 49)
    deco(r, 'Drawings of a hand pressing a cloth on a bleeding wound, a man calling an ambulance, and a man lying beside a snake with a hospital in a thought bubble are decorative.')
    BOOK.save(49, [(4, r)], issues=[{'id': 'hpe12-pdf049', 'unit': 4, 'printedPage': 44,
               'description': '“اگر ایسا کوئی واقع ہو جائے” (for واقعہ). Retained as printed.'}])


def p50():
    b = Builder()
    b.h('Medical aid', 'طبی امداد', 'طبي مرسته')
    L(b, [('Encourage the patient.', 'مریض کی حوصلہ افزائی کریں۔', 'ناروغ وهڅوئ.'),
          ('Tie some bandage firmly between the heart and the wound.', 'دل اور زخم کے درمیان مضبوطی سے کوئی پٹی باندھ دیں۔', 'د زړه او ټپ ترمنځ کوم پټی کلک وتړئ.'),
          ('Where there are tooth marks, take out blood and poison from there.', 'جہاں دانتوں کے نشان ہیں وہاں سے خون اور زہر نکال دیں۔', 'چېرته چې د غاښونو نښې دي، له هغه ځایه وینه او زهر وباسئ.'),
          ('If necessary, suck the poison through the mouth on the tooth marks and spit it out; take care that the one doing so has no blisters in the mouth.', 'اگر ضروری ہو تو دانتوں کے نشان پر منہ کے ذریعے زہر چوس کر تھوک دیں خیال رہے کہ ایسا کرنے والے کے منہ میں چھالے نہ ہوں۔', 'که اړینه وي، د غاښونو پر نښو په خوله زهر وزبېښئ او تو یې کړئ؛ پام وي چې د دې کار کوونکي په خوله کې زخمونه (چیچۍ) نه وي.'),
          ('Immediately take the patient to hospital.', 'مریض کو فوراً ہسپتال پہنچائیں۔', 'ناروغ سمدستي روغتون ته ورسوئ.')])
    b.h('Sleeping pills', 'خواب آور گولیاں', 'د خوب ګولۍ')
    P(b, [('Sometimes some person uses these pills in a large quantity, from which there is danger to his life. Medical aid should be given to him immediately so that his life may be saved.',
           'بعض اوقات کوئی فرد زیادہ مقدار میں یہ گولیاں استعمال کر لیتا ہے جس سے اس کی جان کو خطرہ ہوتا ہے اسے فوری طور پر طبی امداد دینی چاہیے تاکہ اس کی زندگی بچ جائے۔',
           'کله کله یو کس دا ګولۍ په ډېر مقدار کاروي چې ژوند یې له خطر سره مخ کېږي؛ سمدستي دې طبي مرسته ورکړل شي ترڅو ژوند یې وژغورل شي.')])
    b.h('Medical aid', 'طبی امداد', 'طبي مرسته')
    L(b, [('The patient should not be allowed to sleep.', 'مریض کو سونے نہ دیا جائے۔', 'ناروغ ته دې د ویده کېدو اجازه ورنه کړل شي.'),
          ('Sprinkle water on the face of the patient, or wet a towel and keep it behind the neck.', 'مریض کے منہ پر پانی کے چھینٹے ڈالیں یا تولیہ بھگو کر گردن کے پیچھے رکھیں۔', 'د ناروغ پر مخ اوبه وشیندئ یا دسمال لوند کړئ او د غاړې شا ته یې کېږدئ.'),
          ('Vomiting should be induced immediately.', 'فوراً قے کرائی جائے۔', 'سمدستي دې کانګې راوستل شي.'),
          ('Keep the courage of the patient high.', 'مریض کا حوصلہ بلند رکھیں۔', 'د ناروغ زړه‌ورتیا لوړه وساتئ.')])
    r = rec(b, 4, 18, 50)
    deco(r, 'Photographs of a gloved hand bandaging a leg and of pills with a syringe are decorative.')
    BOOK.save(50, [(4, r)])


def p51():
    b = Builder()
    L(b, [('Do not let the pulse become slow.', 'نبض کو سست نہ ہونے دیں۔', 'نبض ته د ورو کېدو اجازه مه ورکوئ.'),
          ('Take him immediately to a hospital or to a doctor.', 'فوراً ہسپتال یا ڈاکٹر کے پاس پہنچائیں۔', 'سمدستي یې روغتون یا ډاکټر ته ورسوئ.')])
    b.h('Stoppage of breathing', 'سانس کا بند ہونا', 'د ساه بندېدل')
    P(b, [('Because of shortage of oxygen in the air, leakage of gas in closed rooms or more smoke, breathing can stop, because of which there is danger of life being lost. For it the following protective measures and first aid are given.',
           'ہوا میں آکسیجن کی کمی، بند کمروں میں گیس کا لیک ہو جانا یا زیادہ دھوئیں کی وجہ سے سانس بند ہو سکتا ہے جس کی وجہ سے جان ضائع ہونے کا خطرہ ہوتا ہے اس کی درجِ ذیل حفاظتی تدابیر اور ابتدائی طبی امداد ہے۔',
           'په هوا کې د اکسیجن کمښت، په تړلو کوټو کې د ګاز لیکېدل یا د ډېر لوګي له امله ساه بندېدای شي چې له امله یې د ژوند د له لاسه ورکولو خطر وي؛ د دې لپاره لاندې ساتنیز ګامونه او لومړنۍ طبي مرسته ده.')])
    L(b, [('Certainly keep some way or other for the exit of gas in the room.', 'گیس کے اخراج کا کوئی نہ کوئی راستہ کمرے میں ضرور رکھیں۔', 'په کوټه کې د ګاز د وتلو یوه نه یوه لاره خامخا وساتئ.'),
          ('In case of smoke use a mask.', 'دھوئیں کی صورت میں ماسک کا استعمال کریں۔', 'د لوګي په صورت کې ماسک وکاروئ.'),
          ('Go towards an open and airy place.', 'کھلی اور ہوادار جگہ کی طرف جائیں۔', 'خلاص او هوادار ځای ته لاړ شئ.'),
          ('If breathing starts to stop, give him first aid immediately.', 'اگر سانس بند ہونے لگے تو فوری طور پر اسے ابتدائی طبی امداد دیں۔', 'که ساه بندېدل پیل کړي، سمدستي لومړنۍ طبي مرسته ورکړئ.')])
    b.h('Medical aid', 'طبی امداد', 'طبي مرسته')
    L(b, [('Keep the patient away from the crowd and lay him in the open air.', 'ہجوم سے مریض کو دور رکھیں اور کھلی ہوا میں لٹائیں۔', 'ناروغ له ګڼې ګوڼې لرې وساتئ او په خلاصه هوا کې یې وغځوئ.'),
          ('Give courage to the patient.', 'مریض کو حوصلہ دیں۔', 'ناروغ ته زړه ورکړئ.'),
          ('Try to deliver oxygen to the brain.', 'دماغ کو آکسیجن پہنچانے کی کوشش کریں۔', 'هڅه وکړئ چې دماغ ته اکسیجن ورسېږي.'),
          ('Artificial respiration should be given.', 'مصنوعی تنفس دیا جائے۔', 'مصنوعي تنفس دې ورکړل شي.')])
    r = rec(b, 4, 19, 51)
    BOOK.save(51, [(4, r)])


def p52():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('Flame-giving things include fuel, liquids, gunpowder and ________ .', 'شعلہ دینے والی اشیاء میں ایندھن، مائع، بارود اور ________ شامل ہیں۔', 'په لمبه ورکوونکو توکو کې سونګ، مایعات، باروت او ________ شامل دي.'), [('ink', 'سیاہی', 'رنګ (سیاهي)'), ('paint', 'پینٹ', 'رنګ (پېنټ)'), ('syrup', 'سیرپ', 'شربت'), ('water', 'پانی', 'اوبه')]),
         (('In the home, protection from fire starts first with ________ .', 'گھر میں آگ سے پہلی حفاظت ________ سے شروع ہوتی ہے۔', 'په کور کې له اور لومړنۍ ساتنه له ________ پیلېږي.'), [('guest room', 'مہمان خانہ', 'مېلمستون'), ('bedrooms', 'سونے کے کمرے', 'د خوب کوټې'), ('kitchen', 'کچن', 'پخلنځی'), ('courtyard', 'صحن', 'انګړ')]),
         (('At night the quantity of ________ in the air decreases.', 'رات کے وقت ہوا میں ________ کی مقدار کم ہو جاتی ہے۔', 'د شپې په هوا کې د ________ مقدار کمېږي.'), [('carbon dioxide', 'کاربن ڈائی آکسائیڈ', 'کاربن ډای اکسایډ'), ('nitrogen', 'نائیٹروجن', 'نایټروجن'), ('hydrogen', 'ہائیڈروجن', 'هایدروجن'), ('oxygen', 'آکسیجن', 'اکسیجن')]),
         (('The place and quantity of flame-giving things should be kept ________ .', 'شعلہ دینے والی اشیاء کی جگہ اور مقدار کو ________ رکھنا چاہیے۔', 'د لمبه ورکوونکو توکو ځای او مقدار باید ________ وساتل شي.'), [('limited', 'محدود', 'محدود'), ('wide', 'وسیع', 'پراخ'), ('supervision', 'نگرانی', 'څارنه'), ('different', 'مختلف', 'بېلابېل')]),
         (('Before constructing a building ________ is very necessary.', 'عمارت بنانے سے پہلے ________ بہت ضروری ہے۔', 'د ودانۍ له جوړولو مخکې ________ ډېر اړین دی.'), [('instructions', 'ہدایات', 'لارښوونې'), ('map', 'نقشہ', 'نقشه'), ('planning', 'منصوبہ بندی', 'پلان جوړونه'), ('papers', 'کاغذات', 'کاغذونه')]),
         (('For fire to burn heat, oxygen and ________ are needed.', 'آگ کو جلنے کیلئے حرارت، آکسیجن اور ________ کی ضرورت ہوتی ہے۔', 'د اور د سوځېدو لپاره تودوخې، اکسیجن او ________ ته اړتیا وي.'), [('water', 'پانی', 'اوبه'), ('electricity', 'بجلی', 'برېښنا'), ('environment', 'ماحول', 'چاپېریال'), ('fuel', 'ایندھن', 'سونګ')]),
         (('At workplaces there should be a proper arrangement of ________ .', 'کام کی جگہوں پر ________ کا درست انتظام ہو۔', 'د کار په ځایونو کې دې د ________ سم انتظام وي.'), [('residence', 'رہائش', 'استوګنه'), ('electricity', 'بجلی', 'برېښنا'), ('security', 'سیکورٹی', 'امنیت'), ('wall', 'دیوار', 'دېوال')]),
         (('There are ________ methods of artificial respiration.', 'مصنوعی تنفس کے ________ طریقے ہیں۔', 'د مصنوعي تنفس ________ طریقې دي.'), [('2', '2', '2'), ('3', '3', '3'), ('4', '4', '4'), ('one', 'ایک', 'یوه')])]
    for i, (q, o) in enumerate(Q, 1):
        e.mcq(['i.', 'ii.', 'iii.', 'iv.', 'v.', 'vi.', 'vii.', 'viii.'][i - 1], q, o, per_line=4)
    r = BOOK.record(e, 'hpe12-ch4-exercise-1', 'Chapter 4 exercise (1)', 'باب ۴: مشقی سوالات (۱)', '۴ څپرکی: تمریني پوښتنې (۱)', 52, [47])
    BOOK.save(52, [(4, r)], issues=[{'id': 'hpe12-pdf052', 'unit': 4, 'printedPage': 47,
               'description': 'Owner ballpoint ticks on the options are excluded. Q1(viii) asks about methods of artificial respiration, which are not described in the chapter text. Retained as printed.'}])


def p53():
    e = Builder()
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات تحریر کریں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. Write the causes of fire in detail.', 'i۔ آگ لگنے کی وجوہات تفصیل سے تحریر کریں۔', 'i. د اور لګېدو لاملونه په تفصیل ولیکئ.'),
                      ('ii. State the protective guideline for protection from fire.', 'ii۔ آگ سے بچاؤ کی حفاظتی گائیڈ لائن بیان کریں۔', 'ii. له اور د ژغورنې ساتنیز لارښود بیان کړئ.'),
                      ('iii. Why is planning necessary for constructing a building?', 'iii۔ عمارت بنانے کیلئے منصوبہ بندی کیوں ضروری ہے؟', 'iii. د ودانۍ د جوړولو لپاره پلان جوړونه ولې اړینه ده؟'),
                      ('iv. What are the common dangers from fire?', 'iv۔ آگ سے عام خطرات کیا ہے؟', 'iv. له اور عام خطرونه څه دي؟'),
                      ('v. Write the necessary instructions for protection from fire for shop, home, school, factory.', 'v۔ دکان، گھر، سکول، فیکٹری کیلئے آگ سے بچاؤ کیلئے ضروری ہدایات تحریر کریں۔', 'v. د دوکان، کور، ښوونځي، فابریکې لپاره له اور د ژغورنې اړینې لارښوونې ولیکئ.'),
                      ('vi. Write a detailed note on first aid.', 'vi۔ ابتدائی طبی امداد پر مفصل نوٹ لکھیں۔', 'vi. پر لومړنۍ طبي مرسته مفصل یادښت ولیکئ.'),
                      ('vii. State the first aid for snake bite.', 'vii۔ سانپ کے کاٹنے کی ابتدائی طبی امداد بیان کریں۔', 'vii. د مار د چیچلو لومړنۍ طبي مرسته بیان کړئ.')])
    r = BOOK.record(e, 'hpe12-ch4-exercise-2', 'Chapter 4 exercise (2)', 'باب ۴: مشقی سوالات (۲)', '۴ څپرکی: تمریني پوښتنې (۲)', 53, [48])
    BOOK.save(53, [(4, r)], complete_units=[4], issues=[{'id': 'hpe12-pdf053', 'unit': 4, 'printedPage': 48,
               'description': 'Owner Urdu ballpoint notes below the questions and a faint mirrored show-through image at the foot of the page are excluded. Q2(iv) “آگ سے عام خطرات کیا ہے”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 48
    {48: p48, 49: p49, 50: p50, 51: p51, 52: p52, 53: p53}[n]()
