"""Urdu XII PDF111 (spread): pp.212–213 — Poem 6 'نفیرِ عمل' (Majeed Amjad, d.1974 — public domain) full text."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.h('The Trumpet of Action — Majeed Amjad', 'نفیرِ عمل — مجید امجدؔ', 'د عمل شپېلۍ — مجید امجد')
R = [('Youth of the homeland! Come, let us do some work.', 'نوجوانانِ وطن! آؤ کوئی کام کریں', 'د وطن ځوانانو! راشئ چې کوم کار وکړو.')]
S = [
 [('Come — how long shall we complain of the ill-luck of fate? how long mourn the failure of our efforts?', 'آؤ کب تک گلۂ شومیِ تقدیر کریں ۔ کب تلک ماتمِ ناکامیِ تدبیر کریں', 'راشئ — تر کله به د تقدیر د بدمرغۍ ګیله کوو؟ تر کله به د تدبیر د ناکامۍ ویر کوو؟'),
  ('How long shall we lament the tyranny of the old sky? how long complain of the unkindness of the days?', 'کب تلک شیونِ جورِ فلکِ پیر کریں ۔ کب تلک شکوۂ بے مہریِ ایام کریں', 'تر کله به د زاړه اسمان د ظلم ژړا کوو؟ تر کله به د ورځو د بې‌مهرۍ ګیله کوو؟')],
 [('Today the garden of the homeland is ruined by autumn; today the bedchamber of the homeland is deprived of radiance;', 'آج بربادِ خزاں ہے چمنستانِ وطن ۔ آج محرومِ تجلّی ہے شبستانِ وطن', 'نن د وطن باغ د منې له لاسه وران دی؛ نن د وطن د شپې کوټه له رڼا بې‌برخې ده؛'),
  ('the school of the homeland is a centre of wailing and lament — it is time to cure the pain of the unsuccessful heart.', 'مرکزِ نالہ و شیون ہے دبستانِ وطن ۔ وقت ہے چارۂ دردِ دلِ ناکام کریں', 'د وطن ښوونځی د فریاد او ژړا مرکز دی — وخت دی چې د ناکام زړه د درد درملنه وکړو.')],
 [('Come, let us people the ruined settlement again; come, let us set free again the fettered souls;', 'آؤ اُجڑی ہوئی بستی کو پھر آباد کریں ۔ آؤ جکڑی ہوئی روحوں کو پھر آزاد کریں', 'راشئ چې وران کلی بیا اباد کړو؛ راشئ چې تړلي روحونه بیا ازاد کړو؛'),
  ('come, let us follow somewhat the way of Farhad — this is not the condition of loyalty, to sit and rest.', 'آؤ کچھ پیرویِ مسلکِ فرہاد کریں ۔ یہ نہیں شرطِ وفا بیٹھ کے آرام کریں', 'راشئ چې یو څه د فرهاد د لارې پیروي وکړو — د وفا شرط دا نه دی چې کېنو او ارام وکړو.')],
 [('A kind of tumult is raging in the world today; today brother thirsts for the blood of his own brother;', 'ایک ہنگامہ سا ہے آج جہاں میں برپا ۔ آج بھائی ہے سگے بھائی کے خوں کا پیاسا', 'نن په نړۍ کې یو ډول ګډوډي جوړه ده؛ نن ورور د خپل حقیقي ورور د وینې تږی دی؛'),
  ('today loyalty is not found in the world even by searching — come, let us make this precious commodity common again.', 'آج ڈھونڈے سے نہیں ملتی زمانے میں وفا ۔ آؤ اس جنسِ گراں مایہ کو پھر عام کریں', 'نن په نړۍ کې په لټولو هم وفا نه پیدا کېږي — راشئ چې دا قیمتي جنس بیا عام کړو.')],
 [('Let us not fear the cup of Jamshed, nor the glory of Kay; let us not fear the majesty of Rome or the might of Rayy;', 'جامِ جم سے نہ ڈریں شوکتِ کَے سے نہ ڈریں ۔ حشمتِ رُوم اور صولتِ رَے سے نہ ڈریں', 'د جمشید له جام مه وېرېږو، د کې له شوکته مه وېرېږو؛ د روم له حشمت او د ري له صولته مه وېرېږو؛'),
  ('we are young, so let us fear nothing here; we are young, so let us have no apprehension of sorrows.', 'ہم جواں ہیں تو یہاں کی کسی شے سے نہ ڈریں ۔ ہم جواں ہیں تو نہ کچھ خدشۂ آلام کریں', 'موږ ځوانان یو، نو دلته له هېڅ شي مه وېرېږو؛ موږ ځوانان یو، نو د غمونو هېڅ اندېښنه مه کوو.')],
 [('Let us break the thread of deceit and hypocrisy — yes, break it; let us smash the begging-bowl of greed and lust — yes, smash it;', 'رشتۂ مکر و ریا توڑ بھی دیں، توڑ بھی دیں ۔ کاسۂ حرص و ہوا پھوڑ بھی دیں، پھوڑ بھی دیں', 'د چل او ریا تار وشلوو، هو وشلوو؛ د حرص او هوس کاسه ماته کړو، هو ماته کړو؛'),
  ('let us give up this strange manner of ours — yes, give it up; come, let us do some work — work, work!', 'اپنی یہ طُرفہ ادا چھوڑ بھی دیں، چھوڑ بھی دیں ۔ آؤ کچھ کام کریں، کام کریں، کام کریں', 'دا خپل عجیب انداز پرېږدو، هو پرېږدو؛ راشئ چې یو څه کار وکړو — کار وکړو، کار وکړو!')],
]
for i, st in enumerate(S, 1):
    t.p(f'Stanza {i}', f'بند {"۰۱۲۳۴۵۶"[i]}', f'بند {i}')
    t.group('lines', st)
    t.group('lines', R)
t.p('(Roz-e-Rafta)', '(روزِ رفتہ)', '(روز رفته)')
po = BOOK.record(t, 'urdu12-u23-poem', 'Poem text', 'متنِ نظم', 'د نظم متن', 111, [212, 213])
po['sourceNote'] = 'Each stanza is printed as two couplets set as side-by-side half-lines, followed by the refrain; here each pair of half-lines is joined with “ ۔ ” on one line.'
issues = [{'id': 'urdu12-pdf111', 'unit': 23, 'printedPage': 213, 'description': 'Source line printed “روزِ رفتہ”, while the author note (p.211) lists the collection as “شبِ رفتہ” — retained as printed. Majeed Amjad (d.1974) is public domain; transcribed in full.'}]

if __name__ == '__main__':
    BOOK.save(111, [(23, po)], issues=issues)
