#!/bin/bash
# usage: runisl.sh script.py n1 n2 ...
cd "D:/SpaceBook/SpaceBook Web/docs/source-verification/class-11"
export TMPDIR="D:/SpaceBook/SpaceBook Web/tmp" TEMP="D:/SpaceBook/SpaceBook Web/tmp" TMP="D:/SpaceBook/SpaceBook Web/tmp"
s=$1; shift
python $s > ../../../tmp/prep.log 2>&1
for n in "$@"; do python finalize_${K:-isl}_page.py $n unresolved "Scan $n compared with source" --issue "Translations need native review"; done > ../../../tmp/fin.log 2>&1
grep "Checkpoint\|Assertion\|Error" ../../../tmp/fin.log ../../../tmp/prep.log
