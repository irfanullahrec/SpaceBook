"""Reads a kaikki.org Wiktionary dump of one language (Urdu, Pashto or Arabic) and keeps, for the words the books actually use, a short
English meaning written by Wiktionary's editors (CC BY-SA 4.0, see docs/OFFLINE_MEANINGS.md).  Inflected forms ("kartā" of "karnā") get the
meaning of their lemma.  Run once at build time; the result is committed.
  python extract_kaikki_native.py <kaikki-xx.jsonl> <vocab_xx.json> <lang ur|ps|ar> <out.tsv>
out.tsv: word <TAB> english meaning   (the word as spelled in the dump) """
import json, re, sys
src, vocab_f, lang, out_f = sys.argv[1:5]
HARAKAT = re.compile('[ً-ٰـۖ-ۭؐ-ؚ]')
def norm(w):
    w = HARAKAT.sub('', w).replace('ي', 'ی').replace('ك', 'ک')
    w = re.sub('[ہۀة]', 'ه', w)
    w = re.sub(r'[^\w\s]', '', w, flags=re.U)
    return re.sub(r'\s+', ' ', w).strip()
vocab = {}
for w, f in json.load(open(vocab_f, encoding='utf8')):
    vocab.setdefault(norm(w), f)
def clean(g):
    g = re.sub(r'\([^)]*\)', '', g)                      # (usage labels)
    g = re.sub(r'\s+', ' ', g).strip(' ;,.')
    # grammar notes and spelling variants are not meanings
    if re.match(r'^(inflection|alternative|obsolete|misspelling|nonstandard|dated|archaic|eye dialect|plural of|singular of|feminine of|masculine of|oblique|romanization|the name of|a letter|letter)', g, re.I): return ''
    return g
def short(senses, n=2):
    out = []
    for s in senses:
        for g in s.get('glosses', [])[:1]:
            c = clean(g)
            if c and len(c) <= 70 and c.lower() not in [x.lower() for x in out]:
                out.append(c)
        if len(out) >= n: break
    return out
# candidates per spelling: (priority, glosses).  0 = the word is itself a lemma, 1 = it is an inflected form listed on a lemma's page
# (so "میں" the postposition "in" wins over "mein" = I drink, a form of پینا), 2 = a spelling in a "forms" table of another entry
cand = {}
lemma_gloss = {}
entries = []
with open(src, encoding='utf8') as fh:
    for line in fh:
        try: e = json.loads(line)
        except Exception: continue
        if e.get('lang_code') != lang: continue
        entries.append(e)
for e in entries:
    g = short(e.get('senses', []))
    if g and not any(f.get('word') for s in e.get('senses', []) for f in (s.get('form_of') or [])): lemma_gloss.setdefault(norm(e['word']), g)
def add(word, glosses, prio):
    if re.search(r'[A-Za-z]', word): return                        # a word spelled in Latin letters belongs to another language
    k = norm(word)
    if k in vocab and glosses: cand.setdefault(k, []).append((prio, word, glosses))
for e in entries:
    senses = e.get('senses', [])
    form_of = [f.get('word', '') for s in senses for f in (s.get('form_of') or s.get('alt_of') or [])]
    g = short(senses)
    if form_of:
        lg = next((lemma_gloss[norm(lw)] for lw in form_of if norm(lw) in lemma_gloss), None)
        if lg: add(e['word'], lg, 1)
    elif g:
        add(e['word'], g, 0)
        for fm in e.get('forms', []) or []:
            f = fm.get('form')
            if f and not re.search(r'[A-Za-z]', f) and 'romanization' not in (fm.get('tags') or []): add(f, g, 2)
rows = {}
for k, lst in cand.items():
    best = min(p for p, _, _ in lst)
    pick = [x for x in lst if x[0] == best]
    glosses = []
    for _, _, gl in pick[:3]:
        for x in gl:
            if x.lower() not in [y.lower() for y in glosses]: glosses.append(x)
    rows[k] = (pick[0][1], glosses[:3])
with open(out_f, 'w', encoding='utf8') as o:
    for k, (w, g) in sorted(rows.items(), key=lambda kv: -vocab[kv[0]]):
        o.write(w + '\t' + '; '.join(g) + '\n')
tot = sum(vocab.values())
print(lang, 'entries', len(entries), 'words kept', len(rows), 'tokens covered %.1f%%' % (100 * sum(vocab[k] for k in rows) / tot))
