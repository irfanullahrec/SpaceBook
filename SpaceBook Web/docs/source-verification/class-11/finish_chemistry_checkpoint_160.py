"""Persist current review status and throughput after source-page 160."""
import datetime,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
file=ROOT/'chemistry-page-160.json'
page=json.loads(file.read_text(encoding='utf-8'))
page['auditStatus']='verified corrected'
note='Nine complete source records and Urdu/Pashto translations compared with the scan. Figures 5.5 and 5.6 recreated as SVG; water/HF bonds, every partial charge, dotted/solid bond styles and source labels compared with librsvg renders. Reader and source-record checks passed. Last paragraph continues on page 161.'
page['review']={'reviewedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':note}
file.write_text(json.dumps(page,ensure_ascii=False,indent=2),encoding='utf-8')
subprocess.run([sys.executable,str(ROOT/'install_chemistry_page.py'),str(file)],check=True)
subprocess.run(['node',str(ROOT/'verify_chemistry_pages.cjs'),'159','160'],check=True)
subprocess.run([sys.executable,str(ROOT/'save_chemistry_checkpoint.py'),'159','unresolved','Five translated text records, Figures 5.3 and 5.4 and source figure numbering preserved. SVGs compared visually; PH3 charge placement adjusted to avoid bond-label overlap.','--issue','Curled right edge obscures words in HCl continuation, force-effects paragraph and hydrogen-bond introduction; missing fragments are marked, not inferred.'],check=True)
subprocess.run([sys.executable,str(ROOT/'save_chemistry_checkpoint.py'),'160','verified',note],check=True)
benchmark_file=ROOT/'chemistry-recovery-benchmark-20261012.json'
b=json.loads(benchmark_file.read_text(encoding='utf-8'))
now=datetime.datetime.now(datetime.timezone.utc)
hours=(now-datetime.datetime.fromisoformat(b['startedAtUtc'])).total_seconds()/3600
b.update(measuredAtUtc=now.isoformat(),elapsedHours=hours,newImplementedPages=list(range(152,161)),newSourceVerifiedPages=[152,154,156,158,160],newImplementedPagesPerHour=round(9/hours,3),newSourceVerifiedPagesPerHour=round(5/hours,3),targetAchieved=9/hours>=400)
benchmark_file.write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(b,ensure_ascii=False))
