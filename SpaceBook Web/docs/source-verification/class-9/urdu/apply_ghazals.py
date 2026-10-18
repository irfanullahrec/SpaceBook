# -*- coding: utf-8 -*-
"""Correct ghazal lessons 16-19 against source PDF 115-130 (printed 113-128)."""
import os, sys, datetime
sys.stdout.reconfigure(encoding='utf-8')
import urdu9_tools as T

TS = 'تشریح (اسپیس بک): '
CUT = '[مصرع اسکین میں اوپر سے کٹا ہوا ہے؛ نظر آنے والے حروف دیوانِ غالب کے مصرعے سے مطابقت رکھتے ہیں]'


def couplet(head, hen, hps, l1, l2, tash, en, ps):
    return dict(heading=head, headingEn=hen, headingPs=hps, urdu=f'{l1}\n{l2}\n\n{TS}{tash}', english=en, pashto=ps)


MIR_NEW = couplet('شعر: دوستوں کے غم کا داغ', 'Couplet: Showing Our Scar', 'شعر: خپل داغ ښودل',
                  'نہ دیکھا غمِ دوستاں شکر ہے', 'ہمیں داغ اپنا دکھا کر چلے',
                  'شکر ہے کہ ہمیں دوستوں کا غم نہیں دیکھنا پڑا؛ ہم خود ہی اپنا داغ (دکھ) انھیں دکھا کر اس دنیا سے رخصت ہو گئے۔',
                  'Thank God we did not have to see our friends grieve; instead we departed after showing them our own scar.',
                  'شکر دی چې د دوستانو غم مو ونه لید؛ موږ خپل داغ ورته وښود او روان شو.')
GHALIB_LAST = couplet('شعر ۱۳ (مقطع دوم): تصوف اور بادہ خواری', 'Couplet 13 (closing): Mysticism and Wine', 'دیارلسم شعر (مقطع): تصوف او شراب',
                      'یہ مسائلِ تصوف، یہ ترا بیان غالبؔ ' + CUT, 'تجھے ہم ولی سمجھتے جو نہ بادہ خوار ہوتا',
                      'غالب اپنے آپ سے مخاطب ہیں کہ تو تصوف کے مسائل اتنی خوبی سے بیان کرتا ہے کہ اگر شراب نہ پیتا تو لوگ تجھے ولی سمجھتے۔',
                      'O Ghalib, such points of mysticism and such eloquence! We would have taken you for a saint, were you not a drinker of wine.',
                      'اې غالبه! دا د تصوف مسایل او دا ستا بیان؛ که شرابي نه وای، موږ به ولي ګڼلی وای.')
ZAFAR_2 = couplet('شعر ۳: ظرفِ عشق اور تنگیِ عمر', 'Couplet 3: Capacity for Love, Narrow Life', 'دریم شعر: د مینې ظرف او لنډ عمر',
                  'نشۂ عشق کا گر ظرف دیا تھا مجھ کو', 'عمر کا تنگ نہ پیمانہ بنایا ہوتا',
                  'اگر مجھے عشق کے نشے کو سمونے کا ظرف دیا تھا تو میری عمر کا پیمانہ اتنا تنگ نہ بنایا ہوتا۔',
                  'If I was given the capacity to hold the intoxication of love, the cup of my life should not have been made so small.',
                  'که ما ته د مینې د نشې ظرف راکړل شوی و، نو زما د عمر پیمانه دومره تنګه نه وای جوړه شوې.')

NOTES = {
    16: ['Ghazal 2 was missing the couplet "نہ دیکھا غمِ دوستاں شکر ہے / ہمیں داغ اپنا دکھا کر چلے" (PDF 117); added in its printed position.'],
    17: ['Ghazal 2 couplet 3 restored to the printed line break: "نہ بدرقہ ہے نہ کوئی رفیق ساتھ اپنے / فقط عنایتِ پروردگار راہ میں ہے" (PDF 121).'],
    18: ['Ghazal 2 opening restored to "یہ نہ تھی ہماری قسمت..." and couplet 4 to "...یہ اگر شرار ہوتا" as printed (PDF 125).',
         'Two couplets not in the book were removed ("ہم کو معلوم ہے جنت کی حقیقت" belongs to another Ghalib ghazal; "ہوئے مر کے ہم جو رسوا" is not printed).',
         'The printed closing couplet "یہ مسائلِ تصوف..." (PDF 126, first line cut at the page top) was added with a visible note.'],
    19: ['Ghazal 1 couplet "نقدِ دل گرچہ دیا تھا مجھ کو" is not in the book; replaced with the printed "نشۂ عشق کا گر ظرف دیا تھا مجھ کو" and the printed couplet order restored (PDF 128).'],
}
PAGES = {16: [115, 116, 117, 118], 17: [119, 120, 121, 122], 18: [123, 124, 125, 126], 19: [127, 128, 129, 130]}

if os.path.exists(T.LOCK):
    sys.exit('shared lock held')
open(T.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent urdu ghazals {datetime.datetime.now().isoformat()}')
try:
    data = T.load()
    mir = T.lesson(data, 16)['sections']
    if not any('غمِ دوستاں' in s['urdu'] for s in mir):
        mir.insert(9, MIR_NEW)
    at = T.lesson(data, 17)['sections'][9]
    at['urdu'] = at['urdu'].replace('نہ بدرقہ ہے نہ کوئی رفیق ساتھ فقط\nعنایتِ پروردگار راہ میں ہے',
                                    'نہ بدرقہ ہے نہ کوئی رفیق ساتھ اپنے\nفقط عنایتِ پروردگار راہ میں ہے')
    gh = T.lesson(data, 18)['sections']
    gh[6]['urdu'] = gh[6]['urdu'].replace('نہ تھی ہماری قسمت کہ وصالِ یار ہوتا', 'یہ نہ تھی ہماری قسمت کہ وصالِ یار ہوتا', 1) if not gh[6]['urdu'].startswith('یہ نہ') else gh[6]['urdu']
    gh[9]['urdu'] = gh[9]['urdu'].replace('جسے غم سمجھ رہے ہو اگر مستعار ہوتا', 'جسے غم سمجھ رہے ہو، یہ اگر شرار ہوتا')
    gh[9]['urdu'] = gh[9]['urdu'].split('\n\n')[0] + '\n\n' + TS + 'جسے تم غم سمجھ رہے ہو اگر وہ شرارہ (چنگاری) ہوتا تو پتھر کی رگ سے بھی ایسا خون ٹپکتا جو کبھی نہ رکتا؛ یعنی میرا غم آگ سے بھی زیادہ جلانے والا ہے۔'
    gh[9]['english'] = 'Blood would have dripped from the vein of stone and never stopped, if what you take for grief were a spark.'
    gh[9]['pashto'] = 'که دا چې تاسو یې غم ګڼئ سپرغۍ وای، د ډبرې له رګ به داسې وینه څڅېدلې وای چې هېڅکله به نه درېدله.'
    T.lesson(data, 18)['sections'] = [s for s in gh if 'جنت کی حقیقت' not in s['urdu'] and 'ہوئے مر کے ہم جو رسوا' not in s['urdu']]
    if not any('مسائلِ تصوف' in s['urdu'] for s in T.lesson(data, 18)['sections']):
        T.lesson(data, 18)['sections'].append(GHALIB_LAST)
    z = T.lesson(data, 19)['sections']
    if 'نقدِ دل' in z[1]['urdu']:
        z[1], z[2] = z[2], ZAFAR_2
    for n in (16, 17, 18, 19):
        u = T.lesson(data, n)
        u['urduSections'] = [s['urdu'] for s in u['sections']]
        u['sourceReview'] = dict(sourcePdf='D:/SpaceBook/Books/9th/9th urdu/PDF/9th Urdu.pdf', pdfPages=PAGES[n],
                                 printedPages=[T.printed_of(p) for p in PAGES[n]], notes=NOTES[n],
                                 tashreeh='Couplet explanations and English/Pashto renderings are SpaceBook-authored.',
                                 reviewedAt=datetime.date.today().isoformat())
    T.save(data)
finally:
    os.remove(T.LOCK)
print(T.record_pages([(p, 'corrected', f'Lesson {n}: compared with page image; ' + ' '.join(NOTES[n])[:350]) for n in PAGES for p in PAGES[n]])['counts'])
