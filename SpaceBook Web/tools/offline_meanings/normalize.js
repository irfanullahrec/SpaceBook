'use strict';
/* Puts every lexicon row into the right language column, by the SCRIPT of each field, not by where the book's word list happened to store it.
 *
 * The books' word lists are {word: [gloss, gloss]}, but the word and the glosses are in different languages from book to book:
 *   English books      sun            -> [Urdu, Pashto]
 *   Urdu books         خوش نُمائی      -> [English, Pashto]
 *   Pashto books       بیان           -> [Urdu, English]  or  [English, Urdu]
 *   Arabic books       رَبٌّ           -> [English, Pashto]
 * and the English subject lists sometimes hold an English definition ("Steps to solve a problem") where a translation was expected.
 * Read as [English, Urdu, Pashto, Arabic] without looking, an Urdu word became an "English" key, an English gloss became an "Urdu" meaning
 * (the hover card then showed English in the Urdu row) and every Urdu->English lookup of a book word failed.
 *
 *   normalizeRow([f0, f1, f2, f3], hint) -> { en, ur, ps, ar }   (strings, '' = none)  or null
 * hint: the language the book's own words are in ('en', 'ur', 'ps', 'ar'), used only to settle Arabic-script text that cannot be told apart
 * by its letters (Urdu, Pashto and Arabic share most words). */
const RX_PS = /[ټځڅډړږښګڼۍېۉ]/g;
const RX_UR = /[ٹڈڑںھہۂےۓ]/g;
const RX_AR_ONLY = /[ةكىإأ]/g;
const RX_HARAKAT = /[ً-ٰٟ]/g;
const count = (s, rx) => (s.match(rx) || []).length;

const clean = v => String(v == null ? '' : v).replace(/<[^>]*>/g, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();
const body = v => v.replace(/\([^)]*\)/g, '');

// 'L' Latin, 'P' Pashto, 'U' Urdu, 'R' Arabic (harakat or Arabic-only letters), 'A' Arabic script that could be any of the three, '-' none
function script(v) {
  const s = body(v);
  const lat = count(s, /[A-Za-z]/g), ara = count(s, /[؀-ۿݐ-ݿ]/g);
  if (!lat && !ara) return '-';
  if (lat > ara) return 'L';
  if (count(s, RX_PS)) return 'P';
  if (count(s, RX_UR)) return 'U';
  if (count(s, RX_AR_ONLY) || count(s, RX_HARAKAT) >= 2) return 'R';
  return 'A';
}
const LANG_OF = { P: 'ps', U: 'ur', R: 'ar' };
// a Latin field is an English term when it is short; a sentence-long explanation is a definition, not a translation
const isTerm = v => body(v).split(/\s+/).filter(Boolean).length <= 6 && !/[.;:]\s*[A-Za-z]/.test(v);
// Roman Urdu ("yeh qasab kam tolta hai") and unit codes were typed into some glosses: only keep Latin that reads as English
const romanUrdu = v => /\b(hai|hain|kapray|yeh|woh|kya|ka|ki|ke)\b/i.test(v) && !/\b(the|is|are|of|to)\b/i.test(v);

function normalizeRow(fields, hint) {
  const f = [0, 1, 2, 3].map(i => clean(fields[i]));
  const sc = f.map(script);
  const out = { en: '', ur: '', ps: '', ar: '' };
  const put = (lang, v) => { if (v && !out[lang]) out[lang] = v; };
  const latinOk = (v, s) => s === 'L' && isTerm(v) && !romanUrdu(v) && !/^unit-format$/i.test(v);

  if (sc[0] === 'L') {
    // English word first (the English subjects, ENG_URDU_DICT, the offline list)
    if (!latinOk(f[0], 'L') && !isTerm(f[0])) return null;
    out.en = f[0];
    for (let k = 1; k <= 3; k++) {
      if (!f[k] || sc[k] === '-' || sc[k] === 'L') continue;                 // Latin in a target column: an English gloss or definition, never a translation
      const col = ['', 'ur', 'ps', 'ar'][k];
      put(LANG_OF[sc[k]] || col, f[k]);                                       // distinctive letters decide; otherwise the column it came in
    }
    return out;
  }

  if (sc[0] === '-') return null;
  // a word of the book's own language first (Urdu, Pashto, Arabic subjects): [native, English, other]
  let own = LANG_OF[sc[0]] || (hint && hint !== 'en' ? hint : (sc[0] === 'A' ? 'ur' : 'ar'));
  if (sc[0] === 'A' && own === 'en') own = 'ur';
  put(own, f[0]);
  for (let k = 1; k <= 3; k++) {
    const v = f[k];
    if (!v || sc[k] === '-') continue;
    if (sc[k] === 'L') { if (isTerm(v) || v.length <= 90) put('en', v); continue; }   // the English gloss (a long English definition is still a fair English meaning of an Urdu word)
    const free = ['ur', 'ps', 'ar'].filter(l => l !== own && !out[l]);
    const lang = LANG_OF[sc[k]] || free[0];
    if (lang && lang !== own) put(lang, v);
  }
  return out;
}

module.exports = { normalizeRow, script, clean };
