"""Build-time machine translation of the book words that have no stored meaning, with a round-trip check.
Runs a local NLLB-200-distilled-600M (CTranslate2, int8) on this computer: no text goes to any website.
  CT2_USE_MKL=0 python mt_words.py <queue.json> <out.jsonl> <model_dir>
Each output line: {"w": word, "ur": [translation, back-translation], "ps": [...], "ar": [...]}.  Resumable: words already in out.jsonl are skipped. """
import ctranslate2, sentencepiece as spm, json, sys, os, time
sys.stdout.reconfigure(encoding='utf8')
queue_f, out_f, M = sys.argv[1:4]
queue = json.load(open(queue_f, encoding='utf8'))
done = set()
if os.path.exists(out_f):
    for l in open(out_f, encoding='utf8'):
        try: done.add(json.loads(l)['w'])
        except Exception: pass
tr = ctranslate2.Translator(M, device='cpu', compute_type='int8', inter_threads=1, intra_threads=4)
sp = spm.SentencePieceProcessor(); sp.load(M + '/sentencepiece.bpe.model')
CODE = {'ur': 'urd_Arab', 'ps': 'pbt_Arab', 'ar': 'arb_Arab'}
def run(items, src, tgt, beam=2, bs=96):
    enc = [[src] + sp.encode(s, out_type=str) + ['</s>'] for s in items]
    r = tr.translate_batch(enc, target_prefix=[[tgt]] * len(enc), beam_size=beam, max_batch_size=bs, max_decoding_length=24)
    return [sp.decode(x.hypotheses[0][1:]) for x in r]
CH = 960
todo = [q for q in queue if q[0] not in done]
print('todo', len(todo), flush=True)
t0 = time.time(); n = 0
with open(out_f, 'a', encoding='utf8') as out:
    for i in range(0, len(todo), CH):
        chunk = todo[i:i + CH]
        rec = {q[0]: {'w': q[0]} for q in chunk}
        for lang in ('ur', 'ps', 'ar'):
            words = [q[0] for q in chunk if lang in q[2].split(',')]
            if not words: continue
            fwd = run(words, 'eng_Latn', CODE[lang])
            back = run(fwd, CODE[lang], 'eng_Latn')
            for w, f, b in zip(words, fwd, back): rec[w][lang] = [f, b]
        for r in rec.values(): out.write(json.dumps(r, ensure_ascii=False) + '\n')
        out.flush(); n += len(chunk)
        print(n, 'words', round(n / (time.time() - t0), 1), 'w/s', flush=True)
