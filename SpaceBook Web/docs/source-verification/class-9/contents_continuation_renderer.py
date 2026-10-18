import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 contents continuation\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    start=text.index("    if (block.type === 'contentsTable')",text.index('function renderClass9PhysicsFrontMatterBlocks('))
    end=text.index("\n    if (block.type === 'heading')",start)
    line='''    if (block.type === 'contentsTable') return `<div style="overflow-x:auto"><table class="diff-table"><caption>${sanitize(page.title)}</caption><thead><tr>${block.headers.map(header => `<th scope="col">${sanitize(header.text)}<br><span lang="ur" dir="rtl">${sanitize(header.urdu)}</span><br><span lang="ps" dir="rtl">${sanitize(header.pashto)}</span></th>`).join('')}</tr></thead><tbody>${block.entries.map(unit => `${unit.titleIndex === undefined ? '' : `<tr><th scope="row">${unit.number ? unit.number + '.' : ''}</th><td>${render(unit.titleIndex)}</td><td>${unit.printedStartPage}</td></tr>`}${unit.topics.length ? `<tr><td></td><td>${unit.topics.map(topic => `<div style="display:flex;gap:.5rem;margin:.3rem 0;"><span>${sanitize(topic.code)}</span><div>${render(topic.index)}</div></div>`).join('')}</td><td></td></tr>` : ''}`).join('')}</tbody></table></div>`;'''
    file.write_text(text[:start]+line+text[end:],encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
