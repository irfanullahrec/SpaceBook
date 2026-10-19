'use strict';
/* Fakes for the offline tests: a Cache Storage built on Node's own Request/Response, and a little "server" that answers fetch().
 * Nothing here is shipped. */
const crypto = require('crypto');

function makeCaches(opts = {}) {
  const store = new Map();                                      // name -> Map(url -> Response)
  const quota = { full: false };                                // set full = true: every put throws QuotaExceededError
  const urlOf = r => (typeof r === 'string' ? new URL(r, opts.base || 'https://app.test/spacebook/').href : r.url);
  const norm = (u, ignoreSearch) => (ignoreSearch ? u.split('?')[0] : u);
  function cacheApi(name) {
    const m = store.get(name);
    return {
      async match(req, o = {}) {
        const key = norm(urlOf(req), o.ignoreSearch);
        for (const [u, res] of m) if (norm(u, o.ignoreSearch) === key) return res.clone();
        return undefined;
      },
      async put(req, res) {
        if (quota.full) { const e = new Error('quota'); e.name = 'QuotaExceededError'; throw e; }
        m.set(urlOf(req), res.clone());
      },
      async delete(req) { return m.delete(urlOf(req)); },
      async keys() { return [...m.keys()].map(u => new Request(u)); },
    };
  }
  const api = {
    async open(name) { if (!store.has(name)) store.set(name, new Map()); return cacheApi(name); },
    async has(name) { return store.has(name); },
    async keys() { return [...store.keys()]; },
    async delete(name) { return store.delete(name); },
    async match(req, o = {}) {
      for (const name of store.keys()) { const r = await cacheApi(name).match(req, o); if (r) return r; }
      return undefined;
    },
  };
  return { api, store, quota, urls: name => [...(store.get(name) || new Map()).keys()] };
}

// a tiny server: files = { 'path': string | Buffer }, answers by pathname (+ query ignored); counts hits; offline = fetch rejects
function makeServer(files, base = 'https://app.test/spacebook/') {
  const srv = { online: true, hits: [], files: { ...files }, delay: 0 };
  srv.fetch = async (input, init = {}) => {
    const url = new URL(typeof input === 'string' ? input : input.url, base);
    srv.hits.push(url.pathname.replace(new URL(base).pathname, '') + url.search);
    if (init.signal && init.signal.aborted) { const e = new Error('aborted'); e.name = 'AbortError'; throw e; }
    if (!srv.online) throw new TypeError('network down');
    const rel = url.pathname.replace(new URL(base).pathname, '');
    if (!(rel in srv.files)) return new Response('missing', { status: 404 });
    const body = srv.files[rel];
    return new Response(body, { status: 200, headers: { 'Content-Type': rel.endsWith('.json') ? 'application/json' : rel.endsWith('.js') ? 'text/javascript' : 'application/octet-stream' } });
  };
  return srv;
}

const sha256 = data => crypto.createHash('sha256').update(data).digest('hex');
module.exports = { makeCaches, makeServer, sha256 };
