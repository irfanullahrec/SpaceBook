import zipfile, xml.etree.ElementTree as ET, sys, os, re, json

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Civics\Word"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def get_paras(docx_path):
    paras = []
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(NS + 'p'):
            texts = [t.text for t in p_tag.iter(NS + 't') if t.text]
            txt = ''.join(texts).strip()
            if txt:
                paras.append(txt)
    return paras

# Read all 3 files
files = sorted([f for f in os.listdir(DOCX_DIR) if f.endswith('.docx')])
all_paras = []
for f in files:
    path = os.path.join(DOCX_DIR, f)
    p = get_paras(path)
    all_paras.extend(p)

print(f"Total paragraphs: {len(all_paras)}", file=sys.stderr)

# ---- Chapter boundaries from TOC analysis ----
# Chapter markers from initial scan:
# [48]  باب پاکستان کا نظام حکومت  -> Chapter 1
# [62]  باب : بچوں اور خواتین کے حقوق  -> Chapter 3 (in TOC)
# [98]  باب ۳ سیاسی اقتصادیات
# [104] باب ۴ بین الاقوامی تنازعات اور حل
# [117] باب : علمی مہارتیں
# [122] باب ۔۲: سیاسی جماعتیں اور سماجی تحاریک
# [128] باب ۷ امن اور تنوع
# [179] باب ۸ فعال اور ذمہ دار شہریت
# [199] باب  (start of actual content)
# [679] باب  (next major section)
# [931] باب  
# [1306] باب
# [1586] باب
# [1737] (no باب but new chapter content)
# [1940] باب
# [2196] باب

# The actual content chapters start at these paragraph indices:
# Based on the exercise markers and chapter headings:
# Ch1: [199] - [678]  (مشق at 605)
# Ch2: [679] - [930]  (مشق at 893)
# Ch3: [931] - [1304] (مشق at 1265)
# Ch4: [1306] - [1585] (مشق at 1508)
# Ch5: [1586] - [1736] (مشق at 1690)
# Ch6: [1737] - [1939] (مشق at 1875 area)
# Ch7: [1940] - [2195] (مشق at 2163)
# Ch8: [2196] - end   (مشق at 2341)

# Let's print paras around each chapter start to confirm:
chapter_starts_toc = [48, 62, 98, 104, 117, 122, 128, 179, 199]
chapter_content_starts = [199, 679, 931, 1306, 1586, 1737, 1940, 2196]
exercise_starts = [605, 893, 1265, 1508, 1690, 1875, 2163, 2341]

print("\n=== CHAPTER CONTENT START PARAS ===")
for idx in chapter_content_starts:
    for offset in range(0, 8):
        i = idx + offset
        if i < len(all_paras):
            print(f"  [{i}] {all_paras[i][:100]}")
    print()

print("\n=== EXERCISE START PARAS ===")
for idx in exercise_starts:
    for offset in range(0, 20):
        i = idx + offset
        if i < len(all_paras):
            print(f"  [{i}] {all_paras[i][:120]}")
    print()
