'use strict';
/* Read-aloud with device voices only: js/core/tts.js on its own, then the app's English and Urdu sentence readers in the app sandbox
 * with a fake speechSynthesis (no Audio element, no request to any website).   node tests/offline/tts.js */
const { JSDOM } = require('jsdom');
const factory = require('../../js/core/tts.js');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };
const wait = ms => new Promise(r => setTimeout(r, ms));

function fakeSynth(voices) {
  const synth = { voices, spoken: [], listeners: {}, paused: false,
    getVoices() { return this.voices; }, addEventListener(t, fn) { this.listeners[t] = fn; },
    speak(u) { this.spoken.push(u); this.last = u; }, cancel() { this.cancelled = (this.cancelled || 0) + 1; }, pause() { this.paused = true; }, resume() { this.paused = false; } };
  return synth;
}
const V = (name, lang, localService = true) => ({ name, lang, localService });

(async () => {
  // ---- the module
  {
    const dom = new JSDOM('<!doctype html><body></body>');
    const win = dom.window;
    win.speechSynthesis = fakeSynth([V('Microsoft Zira', 'en-US'), V('Microsoft David', 'en-US'), V('Google Urdu', 'ur-PK', false), V('Microsoft Asad', 'ur-PK')]);
    const T = factory(win);
    check('a language with a voice has one', T.hasVoice('en') && T.hasVoice('ur-PK') && T.hasVoice('UR'));
    check('a language without a voice has none', !T.hasVoice('ps') && !T.hasVoice('ar'));
    check('the gender hint picks the matching voice', T.pickVoice('en', 'male').name === 'Microsoft David' && T.pickVoice('en', 'female').name === 'Microsoft Zira');
    check('a local voice is preferred over a network voice', T.pickVoice('ur', 'female').name === 'Microsoft Asad', T.pickVoice('ur', 'female').name);
    check('no voice for the language gives null, never another language', T.pickVoice('ps', 'male') === null);
    T.init();
    const cl = win.document.documentElement.classList;
    check('buttons stay while voices exist', !cl.contains('sb-no-voice-en') && !cl.contains('sb-no-voice-ur'));
    check('buttons for a language with no voice are hidden (class on <html>)', cl.contains('sb-no-voice-ps') && cl.contains('sb-no-voice-ar'));
    win.speechSynthesis.voices = [V('Microsoft Zira', 'en-US')];
    win.speechSynthesis.listeners.voiceschanged();
    check('the classes follow the voice list when it changes', cl.contains('sb-no-voice-ur') && !cl.contains('sb-no-voice-en'));
    T.toast('hello');
    const t = win.document.querySelector('.sb-tts-toast');
    check('toast is a status message', t && t.getAttribute('role') === 'status' && t.textContent === 'hello' && !t.hidden);
  }
  {
    const dom = new JSDOM('<!doctype html><body></body>');
    const win = dom.window;
    win.speechSynthesis = fakeSynth([]);
    const T = factory(win);
    T.init();
    check('nothing is hidden before the first voice list arrives', !win.document.documentElement.classList.contains('sb-no-voice-en'));
    const dom2 = new JSDOM('<!doctype html><body></body>');
    const T2 = factory(dom2.window);     // no speechSynthesis at all
    T2.init();
    check('with no speech engine every read-aloud button is hidden at once', ['en', 'ur', 'ps', 'ar'].every(l => dom2.window.document.documentElement.classList.contains('sb-no-voice-' + l)));
  }

  // ---- the app: sentence readers
  const { load } = require('../../tools/lib/app_sandbox');
  const requests = [], timers = [];
  const flush = () => { const q = timers.splice(0); q.forEach(fn => { try { fn(); } catch (e) { /* a timer of the page */ } }); };
  const app = load({ page: 'lazy.html', quiet: true, before: sb => {
    sb.Audio = function (url) { requests.push(url); this.play = () => Promise.resolve(); this.pause = () => { }; };
    sb.SpeechSynthesisUtterance = function (text) { this.text = text; };
    sb.setTimeout = (fn) => { timers.push(fn); return timers.length; };
    sb.speechSynthesis = fakeSynth([V('Microsoft David', 'en-US'), V('Microsoft Asad', 'ur-PK')]);
  } });
  const run = c => app.run(c, 60000);
  run(`window.SBTTS = window.SBTTS || (typeof SBTTS !== 'undefined' ? SBTTS : null);`);
  const synth = app.sb.speechSynthesis;
  check('the page has the SBTTS module', !!app.sb.SBTTS);

  // English: two sentences
  run(`engTtsState.isPlaying = true; engTtsState.isPaused = false; engTtsState.activePrefix = 'p'; engTtsState.activeGender = 'male';
       engTtsState.sentences = [{ text: 'The sun rises.', startIdx: 0, endIdx: 2 }, { text: 'Birds sing.', startIdx: 3, endIdx: 4 }]; engTtsState.currentSentenceIdx = 0; engTtsState.speechRate = 1;
       playNextEngSentence();`);
  check('English reading speaks the sentence with a voice of this device', synth.spoken.length === 1 && synth.last.text === 'The sun rises.' && synth.last.voice && synth.last.voice.name === 'Microsoft David');
  check('English reading creates no audio element and no request to any website', requests.length === 0, requests.join(','));
  check('male voice is lower than female', synth.last.pitch < 1);
  synth.last.onstart && synth.last.onstart();
  synth.last.onboundary && synth.last.onboundary({ name: 'word', charIndex: 4 });
  check('a boundary event highlights the word being spoken', run('engTtsState.currentWordIdx') === 1, String(run('engTtsState.currentWordIdx')));
  synth.last.onend();
  flush();
  check('the next sentence follows when one ends', synth.spoken.length === 2 && synth.last.text === 'Birds sing.');
  // a cancelled utterance (new speed) must not advance the reading
  const before = run('engTtsState.currentSentenceIdx');
  const old = synth.last;
  run('setEngTtsRate(1.5)');
  flush();
  old.onend && old.onend();
  flush();
  check('the end event of a cancelled utterance does not skip a sentence', run('engTtsState.currentSentenceIdx') === before, before + ' -> ' + run('engTtsState.currentSentenceIdx'));
  run('stopEngTTS()');

  // no English voice: stops with a message, no audio
  synth.voices = [V('Microsoft Asad', 'ur-PK')];
  const spokenBefore = synth.spoken.length;
  run(`engTtsState.isPlaying = true; engTtsState.sentences = [{ text: 'Hello there.', startIdx: 0, endIdx: 1 }]; engTtsState.currentSentenceIdx = 0; playNextEngSentence();`);
  check('with no English voice nothing is spoken and nothing is requested', synth.spoken.length === spokenBefore && requests.length === 0 && run('engTtsState.isPlaying') === false);

  // Urdu
  synth.voices = [V('Microsoft David', 'en-US'), V('Microsoft Asad', 'ur-PK')];
  run(`urduTtsState.isPlaying = true; urduTtsState.isPaused = false; urduTtsState.activePrefix = 'u'; urduTtsState.activeGender = 'female';
       urduTtsState.sentences = [{ text: 'یہ ایک جملہ ہے۔', startIdx: 0, endIdx: 3 }]; urduTtsState.currentSentenceIdx = 0; urduTtsState.speechRate = 1; playNextUrduSentence();`);
  check('Urdu reading uses an Urdu voice, never an English one', synth.last.voice && synth.last.voice.lang === 'ur-PK' && synth.last.lang === 'ur-PK', synth.last.voice && synth.last.voice.name);
  check('Urdu reading requests nothing from any website', requests.length === 0);
  run('stopUrduTTS()');
  synth.voices = [V('Microsoft David', 'en-US')];
  const n2 = synth.spoken.length;
  run(`urduTtsState.isPlaying = true; urduTtsState.sentences = [{ text: 'یہ ایک جملہ ہے۔', startIdx: 0, endIdx: 3 }]; urduTtsState.currentSentenceIdx = 0; playNextUrduSentence();`);
  check('with no Urdu voice nothing is spoken (an English voice never reads Urdu)', synth.spoken.length === n2 && run('urduTtsState.isPlaying') === false);

  // source: no cloud TTS left anywhere in the app scripts
  const fs = require('fs'), path = require('path');
  const bad = ['js/app.js', 'js/universal_translate.js', 'js/word_stats.js', 'js/sb_four_lang.js', 'js/reader_tools.js'].filter(f => /translate_tts/.test(fs.readFileSync(path.join(__dirname, '..', '..', f), 'utf8')));
  check('no script asks translate.google.com for speech', bad.length === 0, bad.join(','));

  console.log(`read-aloud tests: ${passed} passed, ${failed} failed`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
