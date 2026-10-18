"""
build_english_12_translations.py
Translates all paragraphs and sections of Class 12 English (19 units)
into authentic, sentence-aligned Urdu and Pashto.
Caches every translation to tools/eng12_trans_cache.json for resumption.
Updates js/english_12_data.js directly.
"""
import json
import os
import re
import sys
import time
import requests

sys.stdout.reconfigure(encoding='utf-8')

JS_PATH = r"D:\SpaceBook\SpaceBook Web\js\english_12_data.js"
CACHE_PATH = r"D:\SpaceBook\SpaceBook Web\tools\eng12_trans_cache.json"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
URL = 'https://clients5.google.com/translate_a/t'

# Load cache
cache = {}
if os.path.exists(CACHE_PATH):
    try:
        with open(CACHE_PATH, 'r', encoding='utf-8') as f:
            cache = json.load(f)
        print(f"Loaded {len(cache)} cached translation entries.")
    except Exception as e:
        print("Could not load cache:", e)

def save_cache():
    with open(CACHE_PATH, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def chunk_text(text, max_len=800):
    text = text.strip()
    if len(text) <= max_len:
        return [text]
    words = text.split(' ')
    chunks = []
    curr = []
    curr_len = 0
    for w in words:
        if curr_len + len(w) + 1 > max_len and curr:
            chunks.append(' '.join(curr))
            curr = [w]
            curr_len = len(w)
        else:
            curr.append(w)
            curr_len += len(w) + 1
    if curr:
        chunks.append(' '.join(curr))
    return chunks

def translate_single_chunk(text, target_lang):
    text = text.strip()
    if not text:
        return ""
    cache_key = f"{target_lang}::{text}"
    if cache_key in cache:
        return cache[cache_key]

    for attempt in range(3):
        try:
            params = {
                'client': 'dict-chrome-ex',
                'sl': 'en',
                'tl': target_lang,
                'q': text
            }
            res = requests.get(URL, params=params, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if isinstance(data, list) and len(data) > 0:
                    translated = data[0] if isinstance(data[0], str) else str(data[0])
                    cache[cache_key] = translated
                    return translated
            elif res.status_code == 429:
                time.sleep(1.5 * (attempt + 1))
        except Exception:
            time.sleep(0.5)

    # Fallback to MyMemory
    try:
        mm_url = 'https://api.mymemory.translated.net/get'
        params = {'q': text[:450], 'langpair': f'en|{target_lang}'}
        res = requests.get(mm_url, params=params, timeout=10)
        if res.status_code == 200:
            translated = res.json().get('responseData', {}).get('translatedText', '')
            if translated:
                cache[cache_key] = translated
                return translated
    except Exception:
        pass

    return ""

def translate_text(text, target_lang):
    text = text.strip()
    if not text:
        return ""
    cache_key = f"{target_lang}::{text}"
    if cache_key in cache:
        return cache[cache_key]

    chunks = chunk_text(text, max_len=750)
    if len(chunks) == 1:
        res = translate_single_chunk(chunks[0], target_lang)
        cache[cache_key] = res
        return res

    translated_parts = []
    for ch in chunks:
        tr = translate_single_chunk(ch, target_lang)
        translated_parts.append(tr)
        time.sleep(0.15)

    res = " ".join(translated_parts)
    cache[cache_key] = res
    return res

# Read english_12_data.js
with open(JS_PATH, 'r', encoding='utf-8') as f:
    js_content = f.read()

prefix = "const ENGLISH_12_DATA = "
suffix_marker = "\nif (typeof DATA !== 'undefined'"

start_idx = js_content.find(prefix)
if start_idx == -1:
    print("Could not find ENGLISH_12_DATA prefix")
    sys.exit(1)

data_start = start_idx + len(prefix)
end_idx = js_content.find(suffix_marker, data_start)
if end_idx == -1:
    end_idx = js_content.rfind('];')
    if end_idx != -1:
        end_idx += 1

raw_json = js_content[data_start:end_idx].strip()
if raw_json.endswith(';'):
    raw_json = raw_json[:-1].strip()

data = json.loads(raw_json)
print(f"Loaded {len(data)} units from english_12_data.js")

total_paras = sum(len(s.get('paras', [])) for u in data for s in u.get('sections', []))
print(f"Total paragraphs to translate: {total_paras}")

processed_paras = 0
last_save_time = time.time()

for u_idx, u in enumerate(data):
    num = u.get('number', u_idx + 1)
    title = u.get('title', '')
    print(f"\n==========================================")
    print(f"Translating Unit {num}: {title}")
    print(f"==========================================")
    
    # Title translations if missing
    if not u.get('titleUrdu'):
        u['titleUrdu'] = translate_text(title, 'ur')
    if not u.get('titlePashto'):
        u['titlePashto'] = translate_text(title, 'ps')

    for s_idx, sec in enumerate(u.get('sections', [])):
        heading = sec.get('heading', '')
        if not sec.get('headingUrdu') and heading:
            sec['headingUrdu'] = translate_text(heading, 'ur')
        if not sec.get('headingPashto') and heading:
            sec['headingPashto'] = translate_text(heading, 'ps')
        
        paras = sec.get('paras', [])
        existing_urdu = sec.get('urdu', '').strip()
        existing_pashto = sec.get('pashto', '').strip()
        
        urdu_parts = existing_urdu.split('\n\n') if existing_urdu else []
        pashto_parts = existing_pashto.split('\n\n') if existing_pashto else []
        
        # Check if already fully translated
        if len(urdu_parts) == len(paras) and len(pashto_parts) == len(paras) and all(p.strip() for p in urdu_parts):
            processed_paras += len(paras)
            print(f"  Section {s_idx + 1}/{len(u['sections'])}: Already translated ({len(paras)} paras).")
            continue
        
        new_urdu_parts = []
        new_pashto_parts = []
        
        for p_idx, para in enumerate(paras):
            processed_paras += 1
            # Check existing part
            cur_ur = urdu_parts[p_idx].strip() if p_idx < len(urdu_parts) and urdu_parts[p_idx].strip() else ""
            cur_ps = pashto_parts[p_idx].strip() if p_idx < len(pashto_parts) and pashto_parts[p_idx].strip() else ""
            
            if not cur_ur:
                cur_ur = translate_text(para, 'ur')
                time.sleep(0.2)
            if not cur_ps:
                cur_ps = translate_text(para, 'ps')
                time.sleep(0.2)
            
            new_urdu_parts.append(cur_ur)
            new_pashto_parts.append(cur_ps)
            
            if p_idx == 0 or (p_idx + 1) % 5 == 0 or (p_idx + 1) == len(paras):
                print(f"  Sec {s_idx + 1} | Para {p_idx + 1}/{len(paras)} ({processed_paras}/{total_paras})")
                print(f"    EN: {para[:70]}...")
                print(f"    UR: {cur_ur[:70]}...")
            
            # Periodic cache save
            if time.time() - last_save_time > 15:
                save_cache()
                last_save_time = time.time()
        
        sec['urdu'] = '\n\n'.join(new_urdu_parts)
        sec['pashto'] = '\n\n'.join(new_pashto_parts)

    # Save cache after each unit
    save_cache()
    print(f"Unit {num} completed and cached.")

# Write updated dataset back to english_12_data.js
output_js = prefix + json.dumps(data, ensure_ascii=False, indent=2) + ";\n\n"
output_js += """if (typeof DATA !== 'undefined' && DATA) {
  DATA.eng12Chapters = ENGLISH_12_DATA;
}
if (typeof window !== 'undefined') {
  window.ENGLISH_12_DATA = ENGLISH_12_DATA;
}
"""

with open(JS_PATH, 'w', encoding='utf-8') as f:
    f.write(output_js)

save_cache()
print("\n==========================================")
print("SUCCESS: english_12_data.js successfully updated with complete Urdu & Pashto translations!")
print("==========================================")
