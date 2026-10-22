"""Remove the template-generated filler exercise blocks (Pak Studies 12, Economics 12).
They appear on no printed page. Generators were changed to emit empty lists; this
applies the same to the committed data files without regenerating from the docx."""
import json, re, sys, io
FILES = {
 'js/pakstudy_12_data.js': 'مرکزی موضوع کیا ہے',
 'js/economics_12_data.js': 'بنیادی معاشی موضوع کیا ہے',
}
for path, marker in FILES.items():
    s = io.open(path, encoding='utf-8').read()
    i = s.index('= [') + 2
    dec = json.JSONDecoder()
    data, end = dec.raw_decode(s, i)
    n = 0
    for ch in data:
        for k in ('exercise', 'sloBank'):
            b = ch.get(k)
            if b and any(marker in (q.get('q') or '') for q in b.get('mcqs', [])):
                ch[k] = {'mcqs': [], 'shortQuestions': [], 'longQuestions': []}
                n += 1
    out = s[:i] + json.dumps(data, ensure_ascii=False, indent=2) + s[end:]
    io.open(path, 'w', encoding='utf-8', newline='').write(out)
    print(path, 'blocks cleared:', n, 'remaining filler:', out.count('علمِ فلکیات'))
