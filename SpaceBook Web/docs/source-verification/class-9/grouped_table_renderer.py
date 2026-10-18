import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 SI grouped headers\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    start=text.index("    if (block.type === 'sourceDataTable') {")
    end=text.index("    if (block.type === 'table') {",start)
    chunk=text[start:end]
    anchor="      return `<div style=\"overflow-x:auto;margin:1rem 0;\"><table class=\"diff-table\"><thead><tr>${translation.headers.map(header => `<th scope=\"col\">${sanitize(header)}</th>`).join('')}</tr></thead>"
    replacement="      const grouped = translation.headerGroups && translation.subHeaders;\n      const headers = (grouped ? `<tr>${translation.headerGroups.map(group => `<th scope=\"colgroup\" colspan=\"${group.columns.length}\">${sanitize(group.title)}</th>`).join('')}</tr>` : '') + `<tr>${(translation.subHeaders || translation.headers).map(header => `<th scope=\"col\">${sanitize(header)}</th>`).join('')}</tr>`;\n      return `<div style=\"overflow-x:auto;margin:1rem 0;\"><table class=\"diff-table\"><thead>${headers}</thead>"
    assert anchor in chunk
    chunk=chunk.replace(anchor,replacement,1)
    file.write_text(text[:start]+chunk+text[end:],encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
