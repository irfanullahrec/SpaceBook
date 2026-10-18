"""One-time app.js wiring for Class 12 source-authored (sourceClass12Source) sections in language/humanities views."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from class12_statistics_common import _write_locked

APP = Path(__file__).resolve().parents[1] / 'js/app.js'
MARK = '/* CLASS12-SOURCE-LAYOUT */'

PARAS_OLD = "  if (subTab === 'paragraphs') {\n    // Flatten paragraphs from sections\n"
PARAS_NEW = """  if (subTab === 'paragraphs' && sections.some(s => s && s.sourceClass12Source === true && s.sourceLayout)) { """ + MARK + """
    const srcLang = (sec) => (sec.sourceLanguage === 'ur' || isUrdu) ? 'ur' : (sec.sourceLanguage === 'ps' || isPashto) ? 'ps' : 'en';
    return `<div id="langParasGrid" class="math-cards-grid-target">${sections.map((sec, sIdx) => `
      <div class="para-card" id="para-item-${sIdx}">
        <div class="para-card-header"><div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
          <span class="math-badge" style="background:#e0f2fe;color:#0369a1;">${sanitize(String(sec.sourcePageLabel || ('Part ' + (sIdx + 1))))}</span>
          <span style="font-weight:700;font-size:0.88rem;color:#0f172a;">${sanitize(sec.title || sec.heading || '')}</span></div></div>
        <div class="para-text-box" style="line-height:1.8;${srcLang(sec) !== 'en' ? 'direction:rtl;text-align:right;font-family:\'Jameel Noori Nastaleeq\',\'Noto Naskh Arabic\',serif;font-size:1.15rem;line-height:2.1;' : ''}">
          ${sec.sourceLayout ? renderScienceSourceLayout(sec, getScienceSectionParagraphsWithTranslations(sec, ch, subjKey), srcLang(sec), sIdx) : getSectionParagraphsWithTranslations(sec, ch).map(p => sanitize(p.text || '')).join('<br><br>')}
        </div>
      </div>`).join('')}</div>`;
  }

""" + PARAS_OLD

TR_OLD = """          const secUrdu = sec.urdu || sec.urduTranslation || ch.urduSummary || 'اردو ترجمہ مکمل شامل ہے۔';
          const secPashto = sec.pashto || ch.pashtoTranslation || 'د پښتو ژباړه متن کم برابر شوې ده.';
"""
TR_NEW = """          const srcLayout = sec.sourceClass12Source === true && sec.sourceLayout; """ + MARK + """
          const srcParas = srcLayout ? getScienceSectionParagraphsWithTranslations(sec, ch, subjKey) : null;
          const secUrdu = srcLayout ? renderScienceSourceLayout(sec, srcParas, 'ur', idx) : (sec.urdu || sec.urduTranslation || ch.urduSummary || 'اردو ترجمہ مکمل شامل ہے۔');
          const secPashto = srcLayout ? renderScienceSourceLayout(sec, srcParas, 'ps', idx) : (sec.pashto || ch.pashtoTranslation || 'د پښتو ژباړه متن کم برابر شوې ده.');
"""
EN_OLD = """                  ${getSectionParagraphsWithTranslations(sec, ch).map((pi, pSubIdx) => 
                    renderInteractiveParagraphHtml(pi.text, pi.urdu, pi.pashto, `trans-${idx}-${pSubIdx}`)
                  ).join('<div style="height:0.85rem;"></div>')}"""
EN_NEW = """                  ${srcLayout ? renderScienceSourceLayout(sec, srcParas, 'en', idx) : getSectionParagraphsWithTranslations(sec, ch).map((pi, pSubIdx) => 
                    renderInteractiveParagraphHtml(pi.text, pi.urdu, pi.pashto, `trans-${idx}-${pSubIdx}`)
                  ).join('<div style="height:0.85rem;"></div>')}"""

SCI_OLD = "(subjKey === 'stat' && t.sourceClass12Statistics === true)) && t.sourceLayout"
SCI_NEW = "(subjKey === 'stat' && t.sourceClass12Statistics === true) || t.sourceClass12Source === true) && t.sourceLayout"


def transform(text):
    if MARK in text:
        print('already wired'); return text
    for old, new in ((PARAS_OLD, PARAS_NEW), (TR_OLD, TR_NEW), (EN_OLD, EN_NEW), (SCI_OLD, SCI_NEW)):
        assert text.count(old) == 1, old[:80]
        text = text.replace(old, new)
    return text


_write_locked(APP, transform, 'class12-source-wire')
print('app.js wired')
