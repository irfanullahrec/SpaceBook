"""PDF12 (printed 11–12): consonants 11–24; vowels — short vowels 25–31, long vowels 32–36, diphthongs 37–38."""
from class12_book_common import Book, Builder

BOOK = Book('english')
H = (['Phoneme', 'IPA Symbol', 'Graphemes', 'Examples'], ['صوتیہ', 'IPA علامت', 'گریفیم', 'مثالیں'], ['غږ‌پوړی', 'IPA نښه', 'ګرافیمونه', 'بېلګې'])
v = Builder()
C = [['11', '/p/', 'p, pp', 'pin, dippy'], ['12', '/r/', 'r, rr, wr, rh', 'run, carrot, wrench, rhyme'], ['13', '/s/', 's, ss, c, sc, ps, st, ce, se', 'sit, less, circle, scene, psycho, listen, pace, course'],
     ['14', '/t/', 't, tt, th, ed', 'tip, matter, thomas, ripped'], ['15', '/v/', 'v, f, ph, ve', 'vine, of, stephen, five'], ['16', '/w/', 'w, wh, u, o', 'wit, why, quick, choir'],
     ['17', '/z/', 'z, zz, s, ss, x, ze, se', 'zed, buzz, his, scissors, xylophone, craze'], ['18', '/ʒ/', 's, si, z', 'treasure, division, azure'], ['19', '/tʃ/', 'ch, tch, tu, ti, te', 'chip, watch, future, action, righteous'],
     ['20', '/ʃ/', 'sh, ce, s, ci, si, ch, sci, ti', 'sham, ocean, sure, special, pension, machine, conscience, station'], ['21', '/θ/', 'th', 'thongs'], ['22', '/ð/', 'th', 'leather'],
     ['23', '/ŋ/', 'ng, n, ngue', 'ring, pink, tongue'], ['24', '/j/', 'y, I, j', 'you, onion']]
v.table('eng12-u01-consonants-b', *[H[0]], C, H[1], H[2], C, C)
v.h('Vowels', 'مصوتے', 'غږلرونکي توري (واول)')
v.h('a. Short Vowels', 'a. مختصر مصوتے', 'a. لنډ غږلرونکي')
S = [['25', '/æ/', 'a, ai, au', 'cat, plaid, laugh'], ['26', '/e/', 'e, ea, u, ie, ai, a, eo, ei, ae', 'end, bread, bury, friend, said, many, leopard, heifer, aesthetic'],
     ['27', '/ɪ/', 'i, e, o, u, ui, y, ie', 'it, england, women, busy, guild, gym, sieve'], ['28', '/ɒ/', 'a, ho, au, aw, ough', 'swan, honest, maul, slaw, fought'],
     ['29', '/ʊ/', 'o, oo, u, ou', 'wolf, look, bush, would'], ['30', '/ʌ/', 'u, o, oo, ou', 'lug, monkey, blood, double'], ['31', '/ə/', 'a, er, i, ar, our, ur', 'about, ladder, pencil, dollar, honour, augur']]
v.table('eng12-u01-short-vowels', H[0], S, H[1], H[2], S, S)
v.h('b. Long Vowel', 'b. طویل مصوتہ', 'b. اوږد غږلرونکی')
LV = [['32', '/i:/', 'e, ee, ea, y, ey, oe, ie, i, ei, eo, ay', 'be, bee, meat, lady, key, phoenix, grief, ski, deceive, people, quay'],
      ['33', '/u:/', 'o, oo, ew, ue, u_e, oe, ough, ui, oew, ou', 'who, loon, dew, blue, flute, shoe, through, fruit, manoeuvre, group'], ['34', '/ɑ:/', 'a', 'arm'],
      ['35', '/ɜ:/', 'ir, er, ur, ear, or, our, yr', 'bird, term, burn, pearl, word, journey, myrtle'], ['36', '/ɔ:/', 'aw, a, or, oor, ore, oar, our, augh, ar, ough, au', 'paw, ball, fork, poor, fore, board, four, taught, war, bought, sauce']]
v.table('eng12-u01-long-vowels', ['Poneme', 'IPA Symbol', 'Grapheme', 'Examples'], LV, H[1], H[2], LV, LV)
v.h('c. Diphthong', 'c. دوہرا مصوتہ (ڈفتھانگ)', 'c. دوه‌غږیز (ډیفتونګ)')
D = [['37', '/eɪ/', 'a, ai, eigh, aigh, ay, er, et, ei, au, a_e, ea, ey', 'bay, maid, weigh, straight, pay, foyer, filet, eight, gauge, mate, break, they'],
     ['38', '/aɪ/', 'i, y, igh, ie, uy, ye, ai, is, eigh, i_e', 'spider, sky, night, pie, guy, stye, aisle, island, height, kite']]
v.table('eng12-u01-diphthongs-a', ['Phoneme', 'IPA Symbols', 'Grapheme', 'Examples'], D, H[1], H[2], D, D)
vg = BOOK.record(v, 'eng12-u01-ipa-b', 'Vocabulary and Grammar — IPA and the 44 phonemes (2)', 'ذخیرۂ الفاظ اور قواعد — IPA اور 44 صوتیے (2)', 'لغات او ګرامر — IPA او 44 غږ‌پوړي (2)', 12, [11, 12])
issues = [{'id': 'eng12-p11-12-tables', 'unit': 1, 'printedPage': 12, 'description': 'Phoneme tables transcribed as printed: header “Poneme” (long vowels), grapheme “I” for /j/, “ho” for /ɒ/, examples in lower case (thomas, stephen, england). Printed text retained.'}]

if __name__ == '__main__':
    BOOK.save(12, [(1, vg)], issues=issues)
