"""Streams the kaikki.org English-Wiktionary dump and keeps, for the words of the book vocabulary, the human-written Urdu / Pashto / Arabic
translations and the lemma of inflected forms.  Wiktionary text is CC BY-SA 4.0 (see docs/OFFLINE_MEANINGS.md for the attribution).
  python extract_wiktionary.py <kaikki-en.jsonl> <vocab.json> <out.json>
vocab.json = [[word, freq], ...].  out.json = {"tr": {word: {"ur":[..],"ps":[..],"ar":[..]}}, "lemma": {form: lemma}} """
import json, sys, re
src, vocab_f, out_f = sys.argv[1:4]
vocab = {w for w, _ in json.load(open(vocab_f, encoding='utf8'))}
LANG = {'ur': 'ur', 'ps': 'ps', 'ar': 'ar'}
tr, lemma, pos = {}, {}, {}
n = 0
with open(src, encoding='utf8') as fh:
    for line in fh:
        n += 1
        if not line.endswith('\n'):
            break                                   # partial last line of a download still in progress
        try:
            e = json.loads(line)
        except Exception:
            continue
        w = (e.get('word') or '').lower()
        if e.get('lang_code') != 'en':
            continue
        keep = w in vocab
        # inflected forms: "running" is a form of "run"
        for s in e.get('senses', []):
            for f in s.get('form_of', []) or []:
                lw = (f.get('word') or '').lower()
                if keep and lw and lw != w and w not in lemma:
                    lemma[w] = lw
        if not keep:
            # entries for lemmas are needed too when a vocab form points to them
            continue
        slot = tr.setdefault(w, {})
        for t in e.get('translations', []) or []:
            c = t.get('lang_code')
            if c in LANG and t.get('word'):
                sense = (t.get('sense') or '')[:60]
                slot.setdefault(c, [])
                if t['word'] not in [x[0] for x in slot[c]]:
                    slot[c].append([t['word'], sense, e.get('pos', '')])
        for s in e.get('senses', []):
            for t in s.get('translations', []) or []:
                c = t.get('lang_code')
                if c in LANG and t.get('word'):
                    slot.setdefault(c, [])
                    if t['word'] not in [x[0] for x in slot[c]]:
                        slot[c].append([t['word'], (t.get('sense') or s.get('glosses', [''])[0])[:60], e.get('pos', '')])
json.dump({'tr': tr, 'lemma': lemma}, open(out_f, 'w', encoding='utf8'), ensure_ascii=False)
print('lines', n, 'words with translations', sum(1 for v in tr.values() if v), 'lemma links', len(lemma))
