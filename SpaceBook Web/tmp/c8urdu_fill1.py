import re
D='D:/SpaceBook/SpaceBook Web/docs/source-verification/class-8/urdu/pages/'
def add(page, qlabel, ur, en, ps):
    f=D+f'p{page}.txt'; L=open(f,encoding='utf8').read().split('\n')
    i=next(k for k,l in enumerate(L) if l.startswith(f'q {qlabel} |'))
    ins=i+1
    # after the box that follows the question, if any
    if i+1<len(L) and L[i+1].startswith('box'):
        j=i+1
        while not L[j].startswith('endbox'): j+=1
        ins=j+1
    elif i+1<len(L) and L[i+1].startswith('@issue'):
        ins=i+1
    L.insert(ins, f'sol {ur} ## نمونے کا جواب || {en} || {ps}')
    open(f,'w',encoding='utf8',newline='\n').write('\n'.join(L))

add('111','۵',
 'اینٹھنا: مروڑنا، بل دینا۔ دھپ مارنا: ہاتھ سے زور سے مارنا۔ کھٹ پٹ: معمولی تکرار یا کھٹکے کی آواز۔ حماقت: بے وقوفی۔ اعانت: مدد۔ تعصبات: جانب داری کے جذبات۔ ملنسار: ملنے جلنے والا، خوش اخلاق۔ طول بلد: گرین وچ سے مشرق یا مغرب کا زاویائی فاصلہ۔ عرض بلد: خطِ استوا سے شمال یا جنوب کا زاویائی فاصلہ۔ عصبیت: بے جا جانب داری۔',
 'to wring, twist: to twist. to give a thump: to hit hard with the hand. petty quarrel or a clatter. folly: foolishness. assistance: help. prejudices: feelings of partiality. sociable: friendly, mixing easily. longitude: angular distance east or west of Greenwich. latitude: angular distance north or south of the equator. bigotry: unreasonable partiality.',
 'ګوزول: مروړل. دهپ وهل: په لاس پیاوړی وهل. کټ پټ: وړوکی جنجال یا د کټکې غږ. حماقت: بې وقوفي. مرسته: کومک. تعصبونه: د طرفدارۍ احساسات. ملنسار: له خلکو سره ګډ ګډ کېدونکی. طول البلد: له ګرینویچ څخه ختیځ یا لویدیځ ته زاویوي واټن. عرض البلد: له استوا څخه شمال یا سهیل ته زاویوي واټن. عصبیت: بې ځایه طرفداري.')
add('111','۶',
 'عید پر بازار میں تل دھرنے کو جگہ نہ تھی۔ جب چوری پکڑی گئی تو پتا چلا کہ سب حمام میں ننگے ہیں۔ بیٹے کی شرارت سن کر باپ کے پیروں تلے سے زمین نکل گئی۔ بچوں نے چھٹی کے دن گھر سر پر اٹھا لیا۔ بجلی کے ننگے تار کو چھونا آگ سے کھیلنا ہے۔ خطرہ دیکھ کر چور کے ہوش اڑ گئے اور اس کی ستی گم ہو گئی۔',
 'On Eid there was no room even for a sesame seed in the market. When the theft was caught it became clear that everyone is equally guilty. Hearing his son\'s mischief the father felt the ground slip from under his feet. The children raised the house on their heads on the holiday. Touching a bare electric wire is playing with fire. Seeing the danger the thief lost his wits.',
 'په اختر کې په بازار کې د تل د ایښودو ځای نه و. کله چې غلا ونیول شوه نو معلومه شوه چې ټول په یو شان ګناه کې دي. د زوی شرارت اورېدلو سره د پلار پښو لاندې ځمکه وخوځېده. ماشومانو د رخصتۍ په ورځ کور پر سر واخیست. د بریښنا برېښنده تار لمس کول له اور سره لوبه ده. خطر لیدو سره د غل ځواک ورک شو.')
add('148','۹',
 'ہم عید الاضحیٰ سے چند دن پہلے ابو جان کے ساتھ مویشی منڈی گئے۔ وہاں ہر طرف جانوروں کی بھیڑ تھی۔ کہیں بیل تھے، کہیں اونٹ اور کہیں بکرے۔ میں پہلی بار یہ منظر دیکھ کر حیران بھی ہوا اور خوش بھی۔ مجھے ایک سفید بکرا بہت پسند آیا۔ میں نے بھائی سے اسی کو خریدنے پر اصرار کیا۔ انھوں نے میری بات مان لی اور ہم بکرا خرید کر خوشی خوشی گھر لے آئے۔',
 'A few days before Eid-ul-Adha I went to the cattle market with my father. There was a crowd of animals everywhere: bulls, camels and goats. Seeing this scene for the first time I was both surprised and happy. I liked a white goat very much and insisted that my brother buy it. He agreed and we happily brought the goat home.',
 'د اختر څو ورځې مخکې زه له پلار سره د څارویو بازار ته ولاړم. هلته هر ځای د څارویو ګڼې ګوڼې وې: غوایان، اوښان او پسونه. دا لیدنه لومړی ځل ما ولیده، حیران او خوښ شوم. یو سپین پسه راته ډېر خوښ شو او له ورور مې ټینګار وکړ چې همدا ګټي. هغه ومنله او موږ پسه واخیست او په خوښۍ کور ته راوړ.')
add('148','۱۰',
 'گم شدہ گھڑی کا اعلان: تمام طلبہ کو اطلاع دی جاتی ہے کہ آج کھیل کے دوران میری کلائی کی گھڑی (کالے رنگ کی، سٹیل کے پٹے والی) میدان میں کہیں گر گئی ہے۔ جس کسی کو ملے براہِ کرم دفتر میں جمع کروا دے یا مجھے (جماعت ہشتم، احمد) کو واپس کر دے۔ میں اس کا شکر گزار رہوں گا۔',
 'Lost watch notice: All students are informed that during play today my black wrist watch with a steel strap fell somewhere in the ground. Whoever finds it please hand it over at the office or return it to me (Class 8, Ahmed). I shall be grateful.',
 'د ورکې ساعت اعلان: ټول زده کوونکو ته خبر ورکول کېږي چې نن د لوبې پر مهال زما د لاس تور ساعت چې د فولادو پټۍ لري په میدان کې چېرته ولوېد. څوک چې یې ومومي مهرباني وکړي په دفتر کې یې وسپاري یا ماته (اتمه ټولګی، احمد) یې راوګرځوي. مننه.')
add('105','۷',
 'پاکستانی ثقافت بہت رنگا رنگ ہے۔ ہمارے چچا ترکی میں رہتے ہیں۔ وہ پانچ دوستوں کے ساتھ لاہوری کھانے کھانے آئے۔ ہم نے تین دن میں دو شہروں کی سیر کی اور اپنی قومی زبان اردو بھی سیکھی۔ ان کا یہ سفر ہم سب کے لیے خوش گوار رہا۔',
 'Pakistani culture is very colourful. Our uncle lives in Turkey. He came with five friends to eat Lahori food. In three days we toured two cities and also learned our national language Urdu. This trip was pleasant for all of us.',
 'د پاکستان کلتور ډېر رنګارنګ دی. زموږ کاکا په ترکیه کې اوسېږي. هغه له پنځو ملګرو سره د لاهوري خواړو خوړلو ته راغی. موږ په دریو ورځو کې دوه ښارونه وکتل او خپله ملي ژبه اردو مو هم زده کړه. دا سفر ټولو ته خوښ و.')
add('146','۲',
 'میں نے مری، سوات اور ناران کاغان کی سیر کی ہے۔ مری میں برف باری دیکھ کر بہت خوشی ہوئی۔ سوات کی وادی اپنے سبز پہاڑوں اور شفاف دریا کی وجہ سے مجھے سب سے زیادہ پسند آئی۔ ناران میں ہم نے جھیل سیف الملوک دیکھی جو بہت خوب صورت ہے۔ یہ سفر میرے لیے ہمیشہ یادگار رہے گا۔',
 'I have toured Murree, Swat and Naran Kaghan. I was very happy to see snowfall in Murree. I liked the Swat valley most for its green mountains and clear river. In Naran we saw Lake Saif-ul-Malook, which is very beautiful. This trip will always be memorable for me.',
 'ما مري، سوات او ناران کاغان ولیدل. په مري کې د واورې لیدل زما لپاره ډېر خوښ و. د سوات درې مې د شنو غرونو او روښانه سیند له امله تر ټولو ښه ښکاره شوه. په ناران کې موږ سیف الملوک جهيل ولید چې ډېر ښکلی دی. دا سفر به تل ما ته یادګاري وي.')
