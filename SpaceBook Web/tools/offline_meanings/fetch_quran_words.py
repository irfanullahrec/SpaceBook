"""Downloads the word-by-word English and Urdu meanings of every word of the Qur'an (api.quran.com, v4, open data) ONCE, at build time.
Nothing a student does ever calls this service: the result is stored in docs/lexicon/quran_words.json and compiled into the static lexicon.
  python fetch_quran_words.py <out.json>
out.json = { "<uthmani word without marks>": {"en": {"meaning": count}, "ur": {...}} } """
import json, sys, time, urllib.request, re
out_f = sys.argv[1]
MARKS = re.compile('[\u064B-\u065F\u0670\u0640\u06D6-\u06ED\u200C\u200D]')
def norm(w):
    w = MARKS.sub('', w)
    return w.replace('\u0671', '\u0627').replace('\u064A', '\u06CC').replace('\u0643', '\u06A9')
def get(url):
    for k in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'SpaceBook-build/1.0'}), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + 3 * k)
    raise RuntimeError('failed ' + url)
res = {}
for lang in ('en', 'ur'):
    for ch in range(1, 115):
        page = 1
        while True:
            d = get(f'https://api.quran.com/api/v4/verses/by_chapter/{ch}?language={lang}&words=true&word_fields=text_uthmani,text_imlaei_simple&per_page=50&page={page}')
            for v in d['verses']:
                for w in v['words']:
                    if w.get('char_type_name') != 'word': continue
                    t = (w.get('translation') or {}).get('text', '').strip()
                    if not t: continue
                    # the same word is spelled two ways in the books: Uthmani (dagger alif) and plain (Imla'i, full alif): both spellings are keys
                    for field in ('text_uthmani', 'text_imlaei_simple'):
                        k = norm(w.get(field) or '')
                        if not k: continue
                        res.setdefault(k, {}).setdefault(lang, {})
                        res[k][lang][t] = res[k][lang].get(t, 0) + 1
            nxt = (d.get('pagination') or {}).get('next_page')
            if not nxt: break
            page = nxt
            time.sleep(0.15)
        print(lang, ch, len(res), flush=True)
json.dump(res, open(out_f, 'w', encoding='utf8'), ensure_ascii=False)
print('done', len(res))
