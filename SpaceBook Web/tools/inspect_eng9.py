import sys, json

sys.stdout.reconfigure(encoding="utf-8")
with open(r"D:\SpaceBook\SpaceBook Web\js\english_data.js", "r", encoding="utf-8") as f:
    text = f.read()

prefix = "const ENGLISH_DATA = "
start = text.find(prefix) + len(prefix)
end = text.rfind("];") + 1
data = json.loads(text[start:end])
u1 = data[0]
print("Keys in unit 1:", list(u1.keys()))
print("Number of sections:", len(u1.get("sections", [])))
for s in u1.get("sections", []):
    print("  Section heading:", s.get("heading"))
    print("    text len:", len(s.get("text", "")))
    print("    paras count:", len(s.get("paras", [])))
    if s.get("paras"):
        print("    sample para 0:", s.get("paras")[0][:100])
print("Exercise keys:", list(u1.get("exercise", {}).keys()))
ex = u1.get("exercise", {})
for k in ex:
    print(f"  ex[{k}] count/type:", len(ex[k]) if isinstance(ex[k], list) else type(ex[k]))
print("sloBank keys:", list(u1.get("sloBank", {}).keys()))
print("vocabulary count:", len(u1.get("vocabulary", [])))
if u1.get("vocabulary"):
    print("  vocab 0:", u1.get("vocabulary")[0])
print("grammar keys/count:", len(u1.get("grammar", [])))
if u1.get("grammar"):
    print("  grammar 0:", u1.get("grammar")[0])
