'use strict';
/* Looks for secrets in the tracked files of a repository (and, with --history, in every commit's added lines): private keys, cloud keys, connection strings and
 * assignments of a long literal to a name such as password, secret, api_key, token. Prints file, line and the KIND of match, never the value.
 *   node tools/launch/secrets_scan.js [--repo <folder>] [--history] [--max-mb 3]
 * Exit 1 when something is found. Files that are binary or larger than --max-mb are skipped (they are listed in the count). Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), cp = require('child_process');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const REPO = path.resolve(opt('--repo', path.resolve(__dirname, '..', '..')));
const MAXB = +opt('--max-mb', 3) * 1048576;
const KINDS = [
  ['private key block', /-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----/],
  ['AWS access key id', /\bAKIA[0-9A-Z]{16}\b/],
  ['Google API key', /\bAIza[0-9A-Za-z_\-]{35}\b/],
  ['GitHub token', /\bgh[pousr]_[0-9A-Za-z]{30,}\b/],
  ['connection string with password', /\b(?:mysql|postgres|mongodb|redis|ftp|sftp):\/\/[^\s:@\/]+:[^\s@\/]+@/i],
  ['literal assigned to a secret name', /\b(?:db_?pass(?:word)?|password|passwd|secret|api_?key|access_?token|auth_?token|private_?key)\b['"\]]?\s*(?::|=>|=)\s*['"][A-Za-z0-9_\-\/+=!@#$%^&*.]{10,}['"]/i],
];
// values that are obviously not secrets: placeholders, examples, names of environment variables
const OK = /(?:your[_-]|example|placeholder|changeme|xxxx|\*{4}|<[^>]+>|\$\{|getenv|process\.env|\bnull\b|password_hash|password_verify|test_?pass|dummy)/i;
const git = a => cp.execFileSync('git', a, { cwd: REPO, encoding: 'utf8', maxBuffer: 1 << 30 });
const files = git(['ls-files']).split('\n').filter(Boolean);
const BIN = /\.(png|jpe?g|webp|gif|ico|pdf|woff2?|ttf|otf|zip|apk|jar|mp4|mp3|ogg|svg|bin|keystore|jks)$/i;
let found = 0, scanned = 0, skipped = 0;
const report = (where, kind) => { found++; console.log(`FOUND  ${where}  (${kind})`); };
for (const f of files) {
  const full = path.join(REPO, f);
  if (BIN.test(f) || !fs.existsSync(full)) { skipped++; continue; }
  let st; try { st = fs.statSync(full); } catch (e) { skipped++; continue; }
  if (!st.isFile() || st.size > MAXB) { skipped++; continue; }
  scanned++;
  const L = fs.readFileSync(full, 'utf8').split('\n');
  for (let i = 0; i < L.length; i++) {
    const line = L[i];
    if (line.length > 2000) continue;
    for (const [kind, rx] of KINDS) if (rx.test(line) && !OK.test(line)) report(`${f}:${i + 1}`, kind);
  }
  if (/(^|\/)(\.env|config\.php|id_rsa|.*\.pem|.*\.keystore|.*\.jks)$/i.test(f) && !/example|sample|template/i.test(f)) report(f, 'file that normally holds a secret is tracked');
}
if (args.includes('--history')) {
  // the history of code and configuration (the books' data files are not code and would be hundreds of MB of text)
  const log = git(['log', '-p', '--all', '-U0', '--no-color', '--format=#SHA#%h', '--', '.', ':!docs/source-verification', ':!content', ':!js/*_data*.js', ':!js/*_book*.js', ':!js/lexicon*', ':!js/sent_data*', ':!js/math_*', ':!js/*_solutions*.js', ':!*.json', ':!*.csv', ':!*.tsv', ':!*.txt', ':!lazy.html']);
  let sha = '', n = 0;
  for (const line of log.split('\n')) {
    if (line.startsWith('#SHA#')) { sha = line.slice(5); continue; }
    if (!line.startsWith('+') || line.startsWith('+++') || line.length > 2000) continue;
    n++;
    for (const [kind, rx] of KINDS) if (rx.test(line) && !OK.test(line)) report(`commit ${sha}`, kind);
  }
  console.log(`history: ${n} added lines read`);
}
console.log(`secrets scan of ${REPO}: ${scanned} files read, ${skipped} skipped (binary or over ${(MAXB / 1048576)} MB), ${found} found`);
process.exit(found ? 1 : 0);
