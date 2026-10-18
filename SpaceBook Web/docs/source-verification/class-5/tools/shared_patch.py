"""Minimal, lock-protected patch of a shared SpaceBook file (index.html, tools/*.js, ...).

Usage: shared_patch.py FILE --after "ANCHOR LINE SUBSTRING" --insert "NEW LINE"   (insert once, idempotent)
       shared_patch.py FILE --replace "OLD" --with "NEW"                          (exactly one occurrence)
Acquires tmp/class-content-shared.lock atomically, re-reads FILE, applies the patch, releases in finally.
Never removes another agent's lock; waits up to 120 s for it instead.
"""
import os, sys, time, json, datetime
from pathlib import Path

APP = Path(__file__).resolve().parents[4]
LOCK = APP / 'tmp' / 'class-content-shared.lock'


def arg(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


def main():
    target = (APP / sys.argv[1]).resolve()
    deadline = time.time() + 120
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            if time.time() > deadline:
                raise SystemExit('lock held by another agent: ' + LOCK.read_text(errors='replace')[:200])
            time.sleep(1)
    try:
        os.write(fd, json.dumps({'owner': 'class-5 agent', 'pid': os.getpid(), 'file': str(target),
                                 'since': datetime.datetime.now().isoformat(timespec='seconds')}).encode())
        os.close(fd)
        text = target.read_bytes().decode('utf-8')
        if arg('--after') is not None:
            anchor, new = arg('--after'), arg('--insert')
            if new in text:
                print('already present'); return
            lines = text.split('\n')
            idx = [i for i, l in enumerate(lines) if anchor in l]
            if len(idx) != 1:
                raise SystemExit(f'anchor matched {len(idx)} lines')
            indent = lines[idx[0]][:len(lines[idx[0]]) - len(lines[idx[0]].lstrip())]
            lines.insert(idx[0] + 1, indent + new.strip())
            text = '\n'.join(lines)
        else:
            old, new = arg('--replace'), arg('--with')
            if text.count(old) != 1:
                if new in text:
                    print('already present'); return
                raise SystemExit(f'old text matched {text.count(old)} times')
            text = text.replace(old, new)
        for attempt in range(20):
            try:
                target.write_bytes(text.encode('utf-8'))
                break
            except OSError:
                time.sleep(1.5)  # file briefly locked by a reader on Windows
        else:
            raise SystemExit('target stayed locked; not patched')
        print('patched', target.name)
    finally:
        try:
            LOCK.unlink()
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    main()
