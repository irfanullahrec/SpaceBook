"""Record the completed page-specific review, without promoting scan-gap pages."""
import datetime,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
notes={
150:'Compared all eight questions and 32 options with the source scan. Replaced English fallback text in Urdu/Pashto and reviewed each pair. Preserved all source values and duplicate b. in 8(b). Exact manifest and lesson/exercise visibility checks passed.',
152:'Compared all five numerical questions, five printed answers, descriptive 1-4 with 12 subparts and two printed answers with the scan. Urdu/Pashto reviewed; cm notation and printed answer values preserved. All 26 records passed reader visibility checks.',
154:'Compared all ten learning outcomes, introductory line, unit label and Teaching 09/Assessment 01/Weightage 11 percent with the source. Urdu/Pashto reviewed. Source water-drop illustration recreated in SVG and rendered with librsvg for visual comparison.',
156:'Compared all four postulates, five headings and six prose blocks with the scan. Full translations reviewed. The final fragment continues on page 157 and is not a source gap. All 15 records passed reader visibility checks.',
158:'Compared nine prose/heading records, force-strength order, physical values and Figure 5.2 against the scan. Urdu/Pashto reviewed. SVG preserves four water molecules, hydrogen bonds, partial-charge labels and H2S/H2O bent structures with lone pairs. Rendered figure and reader visibility checked.'
}
for page,note in notes.items():
    file=ROOT/f'chemistry-page-{page}.json'
    record=json.loads(file.read_text(encoding='utf-8'))
    assert not any(p.get('sourceGap') for p in record['paras']), 'Do not verify a scan-gap page'
    record['auditStatus']='verified corrected'
    record['review']={'reviewedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':note,'method':'Direct local source-image comparison, translation review, source-record comparison, and reader rendering checks. No browser/UI testing.'}
    file.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    subprocess.run([sys.executable,str(ROOT/'install_chemistry_page.py'),str(file)],check=True)
    subprocess.run(['node',str(ROOT/'verify_chemistry_pages.cjs'),str(page)],check=True)
    subprocess.run([sys.executable,str(ROOT/'save_chemistry_checkpoint.py'),str(page),'verified',note],check=True)
for page,note,issue in [
 (157,'All 13 source text records and equations (5.1)-(5.2) saved with translations, offline notation and valid KaTeX. Source connectors and a strength multiplier are explicitly marked where obscured.','Right-edge curl hides short words, intra-molecular definition endings and the final strength multiplier. No multiplier inferred.'),
 (155,'All source text and Figure 5.1 saved; SVG visual comparison completed with librsvg. Full and split-source pages have identical pixels.','Hidden connectors and word endings in introduction paragraphs 1-2, unit overview and liquid definition require a clearer source.')]:
    subprocess.run([sys.executable,str(ROOT/'save_chemistry_checkpoint.py'),str(page),'unresolved',note,'--issue',issue],check=True)
start=datetime.datetime.fromisoformat('2026-10-11T19:33:53+00:00')
now=datetime.datetime.now(datetime.timezone.utc)
hours=(now-start).total_seconds()/3600
benchmark=dict(startedAtUtc=start.isoformat(),measuredAtUtc=now.isoformat(),elapsedHours=hours,targetPagesPerHour=400,newImplementedPages=list(range(152,159)),repairedExistingPages=[150,151],newSourceVerifiedPages=[152,154,156,158],repairedSourceVerifiedPages=[150],newImplementedPagesPerHour=round(7/hours,3),newSourceVerifiedPagesPerHour=round(4/hours,3),targetAchieved=7/hours>=400,notes='Includes recovery repairs and figure review time. Represented pages and structural checks are not counted as source verification. Book remains incomplete; prior unresolved pages remain unresolved. Existing verification labels before this review are not a whole-book assurance.')
(ROOT/'chemistry-recovery-benchmark-20261012.json').write_text(json.dumps(benchmark,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(benchmark,ensure_ascii=False))
