#!/usr/bin/env bash
# Runs a command, passes its output through unchanged and keeps its exit code. When the command fails, the lines that say what failed (FAIL ..., crashed, Error:)
# are repeated as ::error:: annotations: the job log of this public repository needs a GitHub login, the annotations of a run do not.
#   bash ../.github/scripts/logged.sh node --max-old-space-size=6144 tests/reader/workspace.js
log="$(mktemp)"
"$@" 2>&1 | tee "$log"
code=${PIPESTATUS[0]}
if [ "$code" != 0 ]; then
  grep -E '^FAIL|crashed|Error:' "$log" | head -20 | cut -c1-400 | sed 's/^/::error::/'
fi
exit "$code"
