"""Build-time machine translation of book sentences into Urdu, Pashto and Arabic with a local NLLB-200-distilled-600M (CTranslate2, int8).
Runs on this computer only: no text is sent to any website.  The output is stored in the project as static files (js/sent/) and shown to
students labelled as a computer translation, after any translation the book itself carries.
  CT2_USE_MKL=0 python mt_sentences.py <queue.json> <out.jsonl> <model_dir> [languages=ur,ps,ar] [threads=6]
queue.json = ["sentence", ...] in priority order.  out.jsonl lines: {"s": sentence, "ur": ..., "ps": ..., "ar": ...}.  Resumable. """
import ctranslate2, sentencepiece as spm, json, sys, os, time
sys.stdout.reconfigure(encoding='utf8')
queue_f, out_f, M = sys.argv[1:4]
LANGS = (sys.argv[4] if len(sys.argv) > 4 else 'ur,ps,ar').split(',')
THREADS = int(sys.argv[5]) if len(sys.argv) > 5 else 6
limit = 10 ** 9
queue = json.load(open(queue_f, encoding='utf8'))
done = set()
if os.path.exists(out_f):
    for l in open(out_f, encoding='utf8'):
        try: done.add(json.loads(l)['s'])
        except Exception: pass
todo = [s for s in queue if s not in done][:limit]
print('todo', len(todo), flush=True)
tr = ctranslate2.Translator(M, device='cpu', compute_type='int8', inter_threads=1, intra_threads=THREADS)
sp = spm.SentencePieceProcessor(); sp.load(M + '/sentencepiece.bpe.model')
CODE = {'ur': 'urd_Arab', 'ps': 'pbt_Arab', 'ar': 'arb_Arab'}

def run(items, tgt, bs):
    enc = [['eng_Latn'] + sp.encode(s, out_type=str)[:200] + ['</s>'] for s in items]
    r = tr.translate_batch(enc, target_prefix=[[tgt]] * len(enc), beam_size=1, max_batch_size=bs,
                           max_decoding_length=min(256, max(24, int(max(len(e) for e in enc) * 2.2))), repetition_penalty=1.1, batch_type='examples')
    return [sp.decode(x.hypotheses[0][1:]) for x in r]

def safe(items, tgt):
    for bs in (32, 8, 2, 1):
        try: return run(items, tgt, bs)
        except RuntimeError as e:
            print('retry', bs, str(e)[:60], flush=True); time.sleep(5)
    return [''] * len(items)

CH = 192
t0 = time.time(); n = 0
with open(out_f, 'a', encoding='utf8') as out:
    for i in range(0, len(todo), CH):
        chunk = sorted(todo[i:i + CH], key=len)
        rec = {s: {'s': s} for s in chunk}
        for lang in LANGS:
            for s, o in zip(chunk, safe(chunk, CODE[lang])):
                if o: rec[s][lang] = o
        for r in rec.values(): out.write(json.dumps(r, ensure_ascii=False) + '\n')
        out.flush(); n += len(chunk)
        print(n, 'sentences', round(n / (time.time() - t0), 2), 's/s', flush=True)
