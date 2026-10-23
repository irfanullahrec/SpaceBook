/* games_vocab.js - picture words for the Little Learners and Word Builder games (Classes 1-3).
 * Hand-written for the games, NOT book text: [emoji, English, Urdu, Pashto, group]. An empty Urdu / Pashto cell means "not sure yet" and
 * the game shows only what is filled in. Every word is a plain noun a young child knows. Review queue for a native reader:
 * docs/GAMES.md ("Picture words"). Emoji are limited to ones the common Android / Windows / iOS fonts draw. */
(function () {
  'use strict';
  const W = [
    // animals
    ['🐱', 'cat', 'بلی', 'پشۍ', 'animal'], ['🐶', 'dog', 'کتا', 'سپی', 'animal'], ['🐄', 'cow', 'گائے', 'غوا', 'animal'],
    ['🐐', 'goat', 'بکری', 'وزه', 'animal'], ['🐑', 'sheep', 'بھیڑ', 'پسه', 'animal'], ['🐴', 'horse', 'گھوڑا', 'آس', 'animal'],
    ['🐪', 'camel', 'اونٹ', 'اوښ', 'animal'], ['🐘', 'elephant', 'ہاتھی', 'هاتی', 'animal'], ['🦁', 'lion', 'شیر', 'زمری', 'animal'],
    ['🐒', 'monkey', 'بندر', 'بیزو', 'animal'], ['🐇', 'rabbit', 'خرگوش', 'سیه ګوش', 'animal'], ['🦆', 'duck', 'بطخ', 'مرغابۍ', 'animal'],
    ['🐔', 'hen', 'مرغی', 'چرګه', 'animal'], ['🐦', 'bird', 'پرندہ', 'مرغۍ', 'animal'], ['🐟', 'fish', 'مچھلی', 'کبه', 'animal'],
    ['🐍', 'snake', 'سانپ', 'مار', 'animal'], ['🐭', 'mouse', 'چوہا', 'موږک', 'animal'], ['🐺', 'wolf', 'بھیڑیا', 'لیوه', 'animal'],
    ['🦅', 'eagle', 'عقاب', 'عقاب', 'animal'], ['🐢', 'turtle', 'کچھوا', '', 'animal'], ['🦋', 'butterfly', 'تتلی', '', 'animal'],
    ['🐻', 'bear', 'ریچھ', '', 'animal'], ['🦉', 'owl', 'اُلّو', '', 'animal'],
    // fruit
    ['🍎', 'apple', 'سیب', 'مڼه', 'fruit'], ['🍌', 'banana', 'کیلا', 'کېله', 'fruit'], ['🍇', 'grapes', 'انگور', 'انګور', 'fruit'],
    ['🍊', 'orange', 'مالٹا', 'مالټه', 'fruit'], ['🍉', 'watermelon', 'تربوز', 'هندوانه', 'fruit'], ['🍐', 'pear', 'ناشپاتی', 'ناک', 'fruit'],
    ['🍑', 'peach', 'آڑو', 'شفتالو', 'fruit'], ['🥭', 'mango', 'آم', 'آم', 'fruit'], ['🍋', 'lemon', 'لیموں', 'لیمو', 'fruit'],
    ['🍓', 'strawberry', 'اسٹرابیری', '', 'fruit'], ['🍒', 'cherry', 'چیری', '', 'fruit'], ['🍍', 'pineapple', 'انناس', '', 'fruit'],
    // vegetables
    ['🥕', 'carrot', 'گاجر', 'ګازره', 'veg'], ['🥔', 'potato', 'آلو', 'کچالو', 'veg'], ['🍅', 'tomato', 'ٹماٹر', 'رومي بانجن', 'veg'],
    ['🧅', 'onion', 'پیاز', 'پیاز', 'veg'], ['🥒', 'cucumber', 'کھیرا', 'بادرنګ', 'veg'], ['🌽', 'corn', 'مکئی', '', 'veg'],
    // food
    ['🍞', 'bread', 'روٹی', 'ډوډۍ', 'food'], ['🥚', 'egg', 'انڈا', 'هګۍ', 'food'], ['🥛', 'milk', 'دودھ', 'شیدې', 'food'],
    ['🍚', 'rice', 'چاول', 'وریژې', 'food'], ['🍰', 'cake', 'کیک', 'کیک', 'food'], ['🍯', 'honey', 'شہد', '', 'food'],
    // nature
    ['☀️', 'sun', 'سورج', 'لمر', 'nature'], ['🌙', 'moon', 'چاند', 'سپوږمۍ', 'nature'], ['⭐', 'star', 'ستارہ', 'ستوری', 'nature'],
    ['🌧️', 'rain', 'بارش', 'باران', 'nature'], ['☁️', 'cloud', 'بادل', 'وریځ', 'nature'], ['❄️', 'snow', 'برف', 'واوره', 'nature'],
    ['🔥', 'fire', 'آگ', 'اور', 'nature'], ['🌳', 'tree', 'درخت', 'ونه', 'nature'], ['🌸', 'flower', 'پھول', 'ګل', 'nature'],
    ['🌈', 'rainbow', 'قوسِ قزح', '', 'nature'], ['⛰️', 'mountain', 'پہاڑ', 'غر', 'nature'],
    // body
    ['👁️', 'eye', 'آنکھ', 'سترګه', 'body'], ['👂', 'ear', 'کان', 'غوږ', 'body'], ['👃', 'nose', 'ناک', 'پوزه', 'body'],
    ['👄', 'mouth', 'منہ', 'خوله', 'body'], ['✋', 'hand', 'ہاتھ', 'لاس', 'body'], ['🦶', 'foot', 'پاؤں', 'پښه', 'body'], ['🦷', 'tooth', 'دانت', 'غاښ', 'body'],
    // things
    ['📖', 'book', 'کتاب', 'کتاب', 'thing'], ['✏️', 'pencil', 'پنسل', 'پنسل', 'thing'], ['🖊️', 'pen', 'قلم', 'قلم', 'thing'],
    ['⏰', 'clock', 'گھڑی', 'ګړی', 'thing'], ['🔑', 'key', 'چابی', 'کیلي', 'thing'], ['🛏️', 'bed', 'بستر', 'بستره', 'thing'],
    ['🔔', 'bell', 'گھنٹی', 'زنګ', 'thing'], ['🎈', 'balloon', 'غبارہ', 'بالون', 'thing'], ['⚽', 'ball', 'گیند', '', 'thing'],
    ['☂️', 'umbrella', 'چھتری', '', 'thing'], ['🎒', 'bag', 'بستہ', '', 'thing'], ['✂️', 'scissors', 'قینچی', '', 'thing'],
    // places
    ['🏠', 'house', 'گھر', 'کور', 'place'], ['🏫', 'school', 'اسکول', 'ښوونځی', 'place'], ['🕌', 'mosque', 'مسجد', 'جومات', 'place'],
    ['🏥', 'hospital', 'ہسپتال', 'روغتون', 'place'],
    // vehicles
    ['🚗', 'car', 'گاڑی', 'موټر', 'vehicle'], ['🚌', 'bus', 'بس', 'بس', 'vehicle'], ['🚲', 'bicycle', 'سائیکل', 'بایسکل', 'vehicle'],
    ['🚂', 'train', 'ریل گاڑی', 'اورګاډی', 'vehicle'], ['🚢', 'ship', 'جہاز', 'بېړۍ', 'vehicle'], ['✈️', 'aeroplane', 'ہوائی جہاز', 'الوتکه', 'vehicle']
  ];
  // colours: [emoji, English, Urdu, Pashto]
  const COLORS = [
    ['🔴', 'red', 'سرخ', 'سور'], ['🔵', 'blue', 'نیلا', 'آسماني'], ['🟢', 'green', 'ہرا', 'شین'], ['🟡', 'yellow', 'پیلا', 'ژیړ'],
    ['⚫', 'black', 'کالا', 'تور'], ['⚪', 'white', 'سفید', 'سپین'], ['🟠', 'orange', 'نارنجی', 'نارنجي'], ['🟣', 'purple', 'جامنی', ''], ['🟤', 'brown', 'بھورا', '']
  ];
  // numbers 1-10: [English word, Urdu, Pashto]
  const NUMBERS = [
    ['one', 'ایک', 'یو'], ['two', 'دو', 'دوه'], ['three', 'تین', 'درې'], ['four', 'چار', 'څلور'], ['five', 'پانچ', 'پنځه'],
    ['six', 'چھ', 'شپږ'], ['seven', 'سات', 'اوه'], ['eight', 'آٹھ', 'اته'], ['nine', 'نو', 'نهه'], ['ten', 'دس', 'لس']
  ];
  // shapes: [emoji, English, Urdu, Pashto]
  const SHAPES = [
    ['⚪', 'circle', 'دائرہ', 'دایره'], ['⬜', 'square', 'مربع', 'مربع'], ['🔺', 'triangle', 'تکون', 'مثلث'], ['⭐', 'star', 'ستارہ', 'ستوری'], ['❤️', 'heart', 'دل', 'زړه']
  ];
  const NAMES = ['Ali', 'Sara', 'Hamza', 'Ayesha', 'Bilal', 'Zainab', 'Usman', 'Maryam', 'Noman', 'Hira', 'Imran', 'Fatima'];
  window.SB_GAMES_VOCAB = {
    words: W.map(r => ({e: r[0], w: r[1], ur: r[2], ps: r[3], g: r[4]})),
    colors: COLORS.map(r => ({e: r[0], w: r[1], ur: r[2], ps: r[3]})),
    numbers: NUMBERS.map(r => ({w: r[0], ur: r[1], ps: r[2]})),
    shapes: SHAPES.map(r => ({e: r[0], w: r[1], ur: r[2], ps: r[3]})),
    names: NAMES
  };
})();
