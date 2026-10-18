"""Generic Class 12 source-authoring pipeline for the non-science books (English, Urdu, Pak Studies, …).

Reuses the Statistics Builder (aligned EN/UR/PS paragraph records + layout blocks) but saves into each subject's
own data file under the shared lock, flags records `sourceClass12Source` (rendered by app.js through
renderScienceSourceLayout inside the language/humanities lesson views) and keeps per-PDF audits and a progress file.

Usage in a page script:
    from class12_book_common import Book, Builder
    BOOK = Book('english')
    b = Builder(); ...; rec = BOOK.record(b, 'eng12-…', 'Title', 'اردو', 'پښتو', pdf, [printed…])
    BOOK.save(pdf, [(unit, rec)], issues=[…], complete_units=[…])
"""
from pathlib import Path
import json, re
from datetime import datetime, timezone
from class12_statistics_common import Builder, pair, _write_locked, section  # noqa: F401  (Builder re-exported)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/source-verification/class-12'

BOOKS = {
    'english': dict(subject='English', source='D:/SpaceBook/Books/12th/12th English/PDF/English Book for 12 class KPTBB.pdf',
                    data='js/english_12_data.js', var='ENGLISH_12_DATA', total=122, prefix='eng12'),
    'urdu': dict(subject='Urdu', source='D:/SpaceBook/Books/12th/12th Urdu/PDF/Urdu Book for 12 class KPTBB.pdf',
                 data='js/urdu_12_data.js', var='URDU_12_DATA', total=139, prefix='urdu12', sourceLang='ur'),
    'pak': dict(subject='Pakistan Studies', source='D:/SpaceBook/Books/12th/12th Pak Studies/PDF/Pak-study Book for 12 class KPTBB.pdf',
                data='js/pakstudy_12_data.js', var='PAKSTUDY_12_DATA', total=117, prefix='pak12', sourceLang='ur'),
    'cs': dict(subject='Computer Science', source='D:/SpaceBook/Books/12th/12th Computer Science/PDF/Computer-Sc  Book for 12 class KPTBB.pdf',
               data='js/computer_12_data.js', var='COMP_12_DATA', total=166, prefix='cs12'),
    'civics': dict(subject='Civics', source='D:/SpaceBook/Books/12th/12th Civics/PDF/Civics Book for 12 class KPTBB.pdf',
                   data='js/civics_12_data.js', var='CIVICS_12_DATA', total=95, prefix='civ12', sourceLang='ur'),
    'eco': dict(subject='Economics', source='D:/SpaceBook/Books/12th/12th Economics/PDF/Economic Book for 12 class KPTBB.pdf',
                data='js/economics_12_data.js', var='ECON_12_DATA', total=163, prefix='eco12', sourceLang='ur'),
    'hpe': dict(subject='Health & Physical Education', source='D:/SpaceBook/Books/12th/12th HPE/PDF/HPE book UM 12th class KPK.pdf',
                data='js/hpe_12_data.js', var='HPE_12_DATA', total=157, prefix='hpe12', sourceLang='ur'),
    'iski': dict(subject='Islamiat Ikhtiari', source='D:/SpaceBook/Books/12th/12th Islamiat Ikhtiari/PDF/Islamiat-Ikhtiari Book for 12 class KPTBB.pdf',
                 data='js/islamiat_ikhtiari_12_data.js', var='ISLAMIAT_OPT_12_DATA', total=130, prefix='iski12', sourceLang='ur'),
    'ihist': dict(subject='Islamic History', source='D:/SpaceBook/Books/12th/12th Islamic History/PDF/Islamic History book 12th class KPK.pdf',
                  data='js/islamic_history_12_data.js', var='ISLAMIC_HISTORY_12_DATA', total=118, prefix='ihist12', sourceLang='ur'),
    'quran': dict(subject='Mutalia-e-Quran', source='D:/SpaceBook/Books/12th/12th Mutalia e Quran/PDF/Mutlia_e_Quran_Book_KPK_12.pdf',
                  data='js/quran_12_data.js', var='QURAN_12_DATA', total=231, prefix='mq12', sourceLang='ur'),
}

SYNC = r'''
const unitOf=n=>__VAR__.find(item=>String(item.number)===String(n));
const isAuthored=s=>s&&s.sourceClass12Source===true;
for(const record of audit.sections){
 let unit=unitOf(record.unit);
 if(!unit){unit={number:record.unit,title:record.unitTitle||String(record.unit),titleUrdu:record.unitTitleUrdu||'',titlePashto:record.unitTitlePashto||'',type:'source',sections:[]};if(String(record.unit)==='FM')__VAR__.unshift(unit);else __VAR__.push(unit);}
 if(record.unitTitle){unit.title=record.unitTitle;unit.titleUrdu=record.unitTitleUrdu||unit.titleUrdu;unit.titlePashto=record.unitTitlePashto||unit.titlePashto;if(record.unitTitleEn){unit.titleEn=record.unitTitleEn;}if(record.unitAuthor){unit.author=record.unitAuthor;}}
 const holderId='__PREFIX__-u'+record.unit+'-pending';
 unit.sections=unit.sections||[];
 if(!unit.sections.some(isAuthored)&&!unit.sections.some(s=>s.id===holderId)&&unit.sections.length){
  const legacy=unit.sections.filter(s=>!isAuthored(s));
  const legacyParas=legacy.flatMap(s=>Array.isArray(s.paras)?s.paras.map(p=>typeof p==='string'?p:(p.text||'')):((s.theory||s.text)?[s.theory||s.text]:[]));
  unit.sections=[{id:holderId,heading:'Remaining unit text — source verification in progress',title:'Remaining unit text — source verification in progress',headingUrdu:'باقی متن — ماخذ سے تصدیق جاری ہے',headingPashto:'پاتې متن — له سرچينې سره تاييد روان دی',
   paras:legacyParas,theory:legacyParas.join('\n\n'),sourcePendingAuthoring:true}];
 }
 const data=Object.assign({},record);delete data.unit;delete data.unitTitle;delete data.unitTitleUrdu;delete data.unitTitlePashto;delete data.unitTitleEn;delete data.unitAuthor;
 data.heading=data.heading||data.title;
 const index=unit.sections.findIndex(s=>s.id===data.id);
 if(index>=0)unit.sections[index]=data;
 else{const holder=unit.sections.findIndex(s=>s.id===holderId);unit.sections.splice(holder<0?unit.sections.length:holder,0,data);}
}
for(const n of audit.completeUnits){const unit=unitOf(n);if(!unit)continue;unit.sections=unit.sections.filter(s=>s.id!=='__PREFIX__-u'+n+'-pending');
 unit.sourceVerified=true;if(unit.exercise&&!unit.exercise.sourceAuthored){unit.legacyExerciseUnverified=unit.exercise;delete unit.exercise;}}
for(const unit of __VAR__.filter(u=>audit.sections.some(r=>String(r.unit)===String(u.number))||audit.completeUnits.map(String).includes(String(u.number)))){
 unit.sourceIssues=[...(unit.sourceIssues||[]).filter(i=>!audit.issues.some(j=>j.id===i.id)),...audit.issues.filter(i=>String(i.unit??audit.sections[0]?.unit)===String(unit.number))];
}
'''


class Book:
    def __init__(self, key):
        c = BOOKS[key]
        self.key, self.c = key, c
        self.data = ROOT / c['data']
        self.progress_path = OUT / f'{key}-progress.json'
        (OUT / key).mkdir(exist_ok=True)

    def record(self, builder, identity, title, urtitle, pstitle, pdf, printed, unit_title=None):
        r = section(identity, title, urtitle, pstitle, builder.paras, builder.layout, builder.blocks, pdf, printed)
        r.pop('sourceClass12Statistics', None)
        r['sourceClass12Source'] = True
        r['sourceSubject'] = self.c['subject']
        r['heading'] = title
        r['sourcePageLabel'] = f'PDF {pdf}' + (f' · p. {"–".join(str(x) for x in printed if x is not None)}' if [x for x in printed if x is not None] else '')
        r['sourceReferences'] = [{'sourcePdf': self.c['source'], 'pdfPage': pdf, 'printedPages': list(printed)}]
        if self.c.get('sourceLang') == 'ur':
            # Urdu-original book: the Urdu text is the source; `text` carries the English translation.
            r['sourceLanguage'] = 'ur'
            r['titleEn'] = title
            r['title'] = r['heading'] = urtitle
            r['text'] = r['urdu']
        if unit_title:
            if self.c.get('sourceLang') == 'ur':
                # unit_title = (english, urdu, pashto[, author]) → keep the Urdu title as the unit's display title
                r['unitTitle'], r['unitTitleUrdu'], r['unitTitlePashto'] = unit_title[1], unit_title[1], unit_title[2]
                r['unitTitleEn'] = unit_title[0]
                if len(unit_title) > 3: r['unitAuthor'] = unit_title[3]
            else:
                r['unitTitle'], r['unitTitleUrdu'], r['unitTitlePashto'] = unit_title
        return r

    def save(self, pdf, records, issues=None, complete_units=None):
        audit = {'pdfPage': pdf, 'sections': [dict(r, unit=u) for u, r in records], 'issues': issues or [], 'completeUnits': complete_units or []}
        tag = self.c['prefix'].upper()
        marker = f'// BEGIN CLASS12 {tag} PDF{pdf:03d} SOURCE'
        end = f'// END CLASS12 {tag} PDF{pdf:03d} SOURCE'
        sync = SYNC.replace('__VAR__', self.c['var']).replace('__PREFIX__', self.c['prefix'])
        block = marker + '\n{ const audit = ' + json.dumps(audit, ensure_ascii=False, indent=1) + ';' + sync + '}\n' + end + '\n'
        var = self.c['var']

        def transform(text):
            if marker in text:
                a = text.index(marker); b = text.index(end, a) + len(end)
                return text[:a] + block.rstrip('\n') + text[b:]
            later = [m for m in re.finditer(rf'// BEGIN CLASS12 {tag} PDF(\d{{3}}) SOURCE', text) if int(m.group(1)) > pdf]
            if later:
                a = later[0].start(); return text[:a] + block + '\n' + text[a:]
            # first time: insert before the export lines that publish the array
            anchor = re.search(r'\n(if \(typeof DATA !== .undefined.|if \(typeof window !== .undefined.)', text)
            prev = [m for m in re.finditer(rf'// END CLASS12 {tag} PDF\d{{3}} SOURCE\n', text)]
            if prev:
                a = prev[-1].end(); return text[:a] + '\n' + block + text[a:]
            if anchor:
                a = anchor.start() + 1; return text[:a] + block + '\n' + text[a:]
            return text.rstrip() + '\n\n' + block
        _write_locked(self.data, transform, f'class12-{self.key}')
        (OUT / f'{self.key}/pdf{pdf:03d}.json').write_text(json.dumps(audit, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f'{self.c["subject"]} PDF {pdf} saved ({len(records)} record(s)).')

    def progress(self):
        if self.progress_path.exists():
            return json.loads(self.progress_path.read_text(encoding='utf-8'))
        return {'schemaVersion': 1, 'subject': self.c['subject'], 'class': 12, 'sourcePdf': self.c['source'], 'totalPdfPages': self.c['total'],
                'workflow': 'inspect scan → compare with OCR/legacy → author aligned EN/UR/PS record → save → record → next',
                'pages': [{'pdfPage': n, 'status': 'not_started'} for n in range(1, self.c['total'] + 1)]}

    def mark(self, pdf, evidence, status='corrected_verified'):
        p = self.progress(); total = self.c['total']
        e = p['pages'][pdf - 1]; assert e['pdfPage'] == pdf
        e.update({'status': status, 'evidence': evidence, 'markedUtc': datetime.now(timezone.utc).isoformat()})
        ok = ('corrected_verified', 'verified_unchanged', 'excluded')
        contiguous = 0
        for x in p['pages']:
            if x['status'] in ok: contiguous = x['pdfPage']
            else: break
        p['lastContiguousResolvedPdfPage'] = contiguous
        p['nextPdfPage'] = contiguous + 1 if contiguous < total else None
        p['resolvedCount'] = sum(x['status'] in ok for x in p['pages'])
        p['phase'] = 'complete' if p['resolvedCount'] == total else 'sequential_source_authoring'
        p['updatedUtc'] = datetime.now(timezone.utc).isoformat()
        self.progress_path.write_text(json.dumps(p, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f'marked {self.c["subject"]} PDF', pdf, status)


def gloss(builder, tid, rows):
    """Glossary table: rows = (word, meaning_en, meaning_ur, meaning_ps); the headword stays English in every view."""
    return builder.table(tid, ['Word', 'Meaning'], [[w, m] for w, m, _, _ in rows], ['لفظ', 'معنی'], ['کلمه', 'مانا'],
                         [[w, u] for w, _, u, _ in rows], [[w, p] for w, _, _, p in rows])


def qlines(builder, items):
    """Numbered question / item lines: items = (en, ur, ps)."""
    return builder.group('lines', items)
