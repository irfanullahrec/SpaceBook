"""Use the existing equation engine only for Class 12 Physics source layouts."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
lock = ROOT / 'tmp/class-content-shared.lock'
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
os.write(fd, b'class12: Physics source-layout equation formatting')
os.close(fd)
try:
    file = ROOT / 'js/app.js'
    text = file.read_bytes().decode('utf-8')
    old = """    if (lang !== 'en') return sanitize(text);
    return renderInteractiveParagraphHtml(text,
      indices.map(index => paras[index]?.urdu || '').join(' '),
      indices.map(index => paras[index]?.pashto || '').join(' '),
      `sci-source-${sectionIndex}-${key}`, true);"""
    # Match line endings as saved by the existing editor.
    newline = '\r\n' if '\r\n' in text else '\n'
    old = old.replace('\n', newline)
    new = """    const isPhysics12Source = sec.id?.startsWith('phys12-front-') &&
      sec.sourceReferences?.some(ref => ref.sourcePdf?.includes('12th/12th Physics/'));
    const equationReader = isPhysics12Source && typeof SpaceBookLessonMath !== 'undefined'
      ? SpaceBookLessonMath : null;
    if (lang !== 'en') return equationReader
      ? equationReader.mathParts(text).map(part => part.latex === undefined ? sanitize(part.text) : equationReader.renderMath(part)).join('')
      : sanitize(text);
    const parts = equationReader ? equationReader.mathParts(text) : [];
    const equations = parts.filter(part => part.latex !== undefined);
    let equationIndex = 0;
    const protectedText = equations.length
      ? parts.map(part => part.latex === undefined ? part.text : `SPACEBOOKPHYSICS${equationIndex++}TOKEN`).join('') : text;
    let result = renderInteractiveParagraphHtml(protectedText,
      indices.map(index => paras[index]?.urdu || '').join(' '),
      indices.map(index => paras[index]?.pashto || '').join(' '),
      `sci-source-${sectionIndex}-${key}`, true);
    if (equations.length) {
      result = result.replace(/<span\\b[^>]*data-word="SPACEBOOKPHYSICS(\\d+)TOKEN"[^>]*>([^<]*)<\\/span>/g,
        (_, number, content) => content.replace(`SPACEBOOKPHYSICS${number}TOKEN`, equationReader.renderMath(equations[Number(number)])));
      result = result.replace(/SPACEBOOKPHYSICS(\\d+)TOKEN/g, (_, number) => sanitize(equations[Number(number)].original));
    }
    return result;""".replace('\n', newline)
    assert text.count(old) == 1
    file.write_bytes(text.replace(old, new).encode('utf-8'))
finally:
    lock.unlink()
