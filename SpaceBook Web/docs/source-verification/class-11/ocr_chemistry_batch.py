"""Resume-safe direct PDF rendering and OCR for the assigned Class 11 Chemistry scan."""
from __future__ import annotations
import hashlib, json, pathlib, sys, time
from datetime import datetime
import numpy as np
import pymupdf
from rapidocr_onnxruntime import RapidOCR

BASE = pathlib.Path(r"D:\SpaceBook")
PDF = BASE / "Books/11th/11th chemisty/pdf/chemistryfull.pdf"
OUT_ROOT = BASE / "SpaceBook Web/tmp/class-11"
SCALE = 1.8

def json_safe(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.integer, np.floating)):
        return value.item()
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)
def atomic_json(path: pathlib.Path, data: dict) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)

def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    start_page = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out = OUT_ROOT / f"chemistryfull-ocr-batch-{stamp}"
    suffix = 1
    while out.exists():
        out = OUT_ROOT / f"chemistryfull-ocr-batch-{stamp}-{suffix}"
        suffix += 1
    out.mkdir()
    pdf_hash = hashlib.sha256(PDF.read_bytes()).hexdigest()
    doc = pymupdf.open(PDF)
    engine = RapidOCR()
    started = time.perf_counter()
    progress = {"sourcePdf": str(PDF), "sourceSha256": pdf_hash, "pdfPages": len(doc),
                "engine": "rapidocr_onnxruntime", "renderScale": SCALE,
                "startedAt": datetime.now().astimezone().isoformat(),
                "nextPage": start_page, "pagesProcessed": 0, "pagesFailed": [],
                "outputDirectory": str(out)}
    atomic_json(out / "progress.json", progress)
    print(f"output={out}", flush=True)
    print(f"source_pages={len(doc)} start_page={start_page}", flush=True)
    for page_no in range(start_page, len(doc) + 1):
        page = doc[page_no - 1]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE),
                              colorspace=pymupdf.csRGB, alpha=False)
        pixels = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        page_started = time.perf_counter()
        try:
            result, elapsed = engine(pixels)
            rows = []
            for item in (result or []):
                box, text, confidence = item
                rows.append({"box": json_safe(box),
                             "text": str(text), "confidence": json_safe(confidence)})
            txt_path = out / f"p{page_no:03}.txt"
            json_path = out / f"p{page_no:03}.json"
            if not txt_path.exists():
                txt_path.write_text("\n".join(row["text"] for row in rows) + "\n", encoding="utf-8")
            if not json_path.exists():
                atomic_json(json_path, {"pdfPage": page_no, "printedPage": page_no - 5 if page_no >= 6 else None,
                                        "pixelSize": [pix.width, pix.height], "ocrSeconds": json_safe(elapsed),
                                        "rows": rows})
        except Exception as exc:
            progress["pagesFailed"].append({"page": page_no, "error": repr(exc)})
        progress["pagesProcessed"] = page_no - start_page + 1
        progress["nextPage"] = page_no + 1
        progress["updatedAt"] = datetime.now().astimezone().isoformat()
        progress["elapsedSeconds"] = round(time.perf_counter() - started, 2)
        progress["pagesPerHour"] = round(progress["pagesProcessed"] * 3600 / max(0.001, time.perf_counter() - started), 1)
        atomic_json(out / "progress.json", progress)
        if page_no % 10 == 0 or page_no == len(doc):
            print(f"checkpoint page={page_no}/{len(doc)} rate={progress['pagesPerHour']} pages/hour failures={len(progress['pagesFailed'])}", flush=True)
    doc.close()
    progress["finishedAt"] = datetime.now().astimezone().isoformat()
    progress["elapsedSeconds"] = round(time.perf_counter() - started, 2)
    progress["pagesPerHour"] = round(progress["pagesProcessed"] * 3600 / max(0.001, time.perf_counter() - started), 1)
    atomic_json(out / "progress.json", progress)
    print(f"complete rate={progress['pagesPerHour']} pages/hour output={out}", flush=True)

if __name__ == "__main__":
    main()
