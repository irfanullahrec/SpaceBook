# -*- coding: utf-8 -*-
"""Restore the Prophet's honorific where the stored English text has an empty or open bracket."""
import re
FULL = '(رسول اللہ خاتم النبیین ﷺ)'
SHORT = '(ﷺ)'


def fix_text(s):
    if not isinstance(s, str) or '(' not in s:
        return s
    s = re.sub(r'Muhammad \(\)', 'Muhammad ' + FULL, s)
    s = re.sub(r"Muhammad \((?=[A-Za-z])", 'Muhammad ' + FULL + ' ', s)
    s = re.sub(r'Muhammad \( (?=the Rasool)', 'Muhammad ' + FULL + ' ', s)
    s = re.sub(r'\b(Rasool|He|His|him|he|his) \(\)', r'\1 ' + SHORT, s)
    return s


def fix(o):
    if isinstance(o, str):
        return fix_text(o)
    if isinstance(o, list):
        return [fix(x) for x in o]
    if isinstance(o, dict):
        return {k: fix(v) for k, v in o.items()}
    return o
