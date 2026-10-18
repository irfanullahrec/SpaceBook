"""Compare OCR text with English source paragraphs saved in the Class 11 Physics reader."""
import csv
import json
import pathlib
import re
import subprocess
import sys
import unicodedata
from collections import Counter

ROOT = pathlib.Path(r"D:\SpaceBook")
OCR_DIR = pathlib.Path(sys.argv[1])
EXPORTER = r"""
const fs=require('fs'),vm=require('vm');
const c=vm.createContext({});
vm.runInContext(fs.readFileSync('SpaceBook Web/js/phys_11_data.js','utf8'),c);
const data=vm.runInContext('PHYS_11_DATA',c), pages={};
for(const ch of data) for(const s of ch.sections) {
  const n=s.source && s.source.pdfPage;
  if(!Number.isInteger(n) || s.sourceLanguage!=='en') continue;
  const paras=[...(s.paras||[]),
    ...(s.continuation?[s.continuation.transition,s.continuation.extension]:[]),
    ...(s.branches||[]).flatMap(b=>b.paras||[])];
  const text=paras.map(p=>p.original||p.text||'').filter(Boolean);
  if(text.length) (pages[n] ||= []).push(...text);
}
process.stdout.write(JSON.stringify(pages));
"""

def normalize(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", value)

def grams(value):
    return Counter(value[i:i+3] for i in range(max(0, len(value)-2)))

def main():
    exported = subprocess.run(["node", "-e", EXPORTER], cwd=ROOT, check=True,
                              capture_output=True, text=True, encoding="utf-8")
    data = json.loads(exported.stdout)
    rows = []
    for page in sorted(int(key) for key in data):
        paragraphs = data[str(page)]
        source = normalize(" ".join(paragraphs))
        ocr_path = OCR_DIR / f"p{page:03}.txt"
        if not ocr_path.exists():
            rows.append({"pdfPage":page,"status":"ocr_pending","sourceChars":len(source),
                         "sourceCoverage":0.0,"minParagraphCoverage":0.0,"matchRatio":0.0})
            continue
        ocr = normalize(ocr_path.read_text(encoding="utf-8", errors="replace"))
        if not ocr:
            rows.append({"pdfPage":page,"status":"empty_ocr","sourceChars":len(source),
                         "sourceCoverage":0.0,"minParagraphCoverage":0.0,"matchRatio":0.0})
            continue
        source_grams, ocr_grams = grams(source), grams(ocr)
        matched = sum((source_grams & ocr_grams).values())
        coverage = matched / max(1, sum(source_grams.values()))
        score = 2 * matched / max(1, sum(source_grams.values()) + sum(ocr_grams.values()))
        paragraph_scores = []
        for paragraph in paragraphs:
            normalized = normalize(paragraph)
            paragraph_grams = grams(normalized)
            if paragraph_grams:
                seen = sum((paragraph_grams & ocr_grams).values())
                paragraph_scores.append(round(seen / sum(paragraph_grams.values()), 4))
        minimum = min(paragraph_scores, default=0.0)
        status = "compare" if coverage >= 0.72 and minimum >= 0.45 else "review"
        rows.append({"pdfPage":page,"status":status,"sourceChars":len(source),"ocrChars":len(ocr),
                     "matchedTrigrams":matched,"sourceCoverage":round(coverage,4),
                     "minParagraphCoverage":minimum,"matchRatio":round(score,4)})
    report = {
        "ocrDirectory":str(OCR_DIR),
        "comparison":"normalized character-trigram overlap; low page or paragraph coverage requires source review and never marks a page verified",
        "pages":rows
    }
    (OCR_DIR / "source-code-comparison.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = ["pdfPage","status","sourceChars","ocrChars","matchedTrigrams",
              "sourceCoverage","minParagraphCoverage","matchRatio"]
    with (OCR_DIR / "source-code-comparison.csv").open("w",newline="",encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    low = [r for r in rows if r["status"] == "review"]
    pending = sum(r["status"] == "ocr_pending" for r in rows)
    lowest = sorted(((r["pdfPage"],r["sourceCoverage"],r["minParagraphCoverage"])
                     for r in rows if r.get("ocrChars")), key=lambda item:item[1])[:12]
    print(f"compared={len(rows)} pages awaiting_ocr={pending} low_match={len(low)}")
    print("lowest page and paragraph coverage:", lowest)

if __name__ == "__main__":
    main()