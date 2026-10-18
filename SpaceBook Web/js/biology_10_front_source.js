/* Class 10 Biology: textbook front matter verified against the printed book
 * (D:\SpaceBook\Books\10th\10th Bio\PDF\Biology Class 10 kpk book.pdf, PDF pages 1-3).
 * Attached to Unit 10 (the first unit of the Grade X book) and shown by biology_10_reader.js. */
(function () {
  const chapter = typeof DATA !== 'undefined' && Array.isArray(DATA.bio10Chapters) ? DATA.bio10Chapters.find(ch => ch.num === 10) : null;
  if (!chapter || chapter.__bio10FrontMatterApplied) return;
  chapter.__bio10FrontMatterApplied = true;
  const P = (text, urdu, pashto, extra) => Object.assign({text, urdu, pashto}, extra || {});
  const contents = [
    ['10', 'Gaseous Exchange', '1', 'گیسوں کا تبادلہ', 'د ګازونو تبادله'],
    ['11', 'Homeostasis', '16', 'ہومیوسٹیسس', 'هومیوسټازس'],
    ['12', 'Coordination and Control', '32', 'ہم آہنگی اور کنٹرول', 'همغږي او کنټرول'],
    ['13', 'Support and Movement', '56', 'سہارا اور حرکت', 'ملاتړ او حرکت'],
    ['14', 'Reproduction', '71', 'تولیدِ نسل', 'تولید / زېږون'],
    ['15', 'Inheritance', '97', 'وراثت', 'میراث (وراثت)'],
    ['16', 'Man and His Environment', '117', 'انسان اور اس کا ماحول', 'انسان او د هغه چاپېریال'],
    ['17', 'Biotechnology', '150', 'بائیو ٹیکنالوجی', 'بایوټکنالوژي'],
    ['18', 'Pharmacology', '164', 'فارماکولوجی', 'فارماکولوژي'],
    ['', 'Glossary', '177', 'فرہنگ', 'لغتنامه'],
    ['', 'Index', '186', 'اشاریہ', 'اشاریه']
  ];
  chapter.sourceFrontMatter = [
    {
      id: 'bio10-front-cover', kind: 'cover', pdfPage: 1, printedPage: null, summary: 'Front cover',
      title: P('A Textbook of Biology Grade X', 'حیاتیات کی درسی کتاب، دسویں جماعت', 'د بیولوژي درسي کتاب، لسم ټولګی'),
      paras: [
        P('A Textbook of', 'درسی کتاب', 'درسي کتاب'),
        P('Biology', 'حیاتیات', 'بیولوژي'),
        P('Grade X', 'دسویں جماعت', 'لسم ټولګی'),
        P('Free From Government', 'حکومت کی طرف سے مفت', 'د حکومت له خوا وړیا'),
        P('NOT FOR SALE', 'فروخت کے لیے نہیں', 'د پلور لپاره نه دی'),
        P('KHYBER PAKHTUNKHWA TEXTBOOK BOARD, PESHAWAR', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
      ],
      layout: [0, 1, 2, 3, 4, 5],
      exclusions: ['Decorative cover montage (DNA strand, gloved hand with specimen, plant cell, globe) and the board emblem carry no instructional content.', 'The "perfect24u.com" and A-PDF watermark text belongs to the scanned file, not to the printed book.']
    },
    {
      id: 'bio10-title-page', kind: 'title page', pdfPage: 2, printedPage: null, summary: 'Title page',
      title: P('A Textbook of BIOLOGY Grade X', 'حیاتیات کی درسی کتاب، دسویں جماعت', 'د بیولوژي درسي کتاب، لسم ټولګی'),
      paras: [
        P('A Textbook of', 'درسی کتاب', 'درسي کتاب'),
        P('BIOLOGY', 'حیاتیات', 'بیولوژي'),
        P('Grade X', 'دسویں جماعت', 'لسم ټولګی'),
        P('KHYBER PAKHTUNKHWA TEXTBOOK BOARD, PESHAWAR', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
        P('NOT FOR SALE', 'فروخت کے لیے نہیں', 'د پلور لپاره نه دی')
      ],
      layout: [0, 1, 2, 3, 4],
      exclusions: ['Decorative title-page montage (gloved hand with specimen, globe, plant cell) and the board emblem; no instructional figure.', 'Watermark text belongs to the scanned file.', 'No publication/credits page is present in this scan between the title page and the contents page.']
    },
    {
      id: 'bio10-contents', kind: 'contents', pdfPage: 3, printedPage: null, summary: 'Contents', open: false,
      title: P('CONTENTS', 'فہرستِ مضامین', 'منځپانګه'),
      paras: [],
      tables: {
        contents: {
          caption: P('CONTENTS', 'فہرستِ مضامین', 'منځپانګه'),
          headers: [P('Unit #', 'یونٹ نمبر', 'د یونټ شمېره'), P('Subject', 'مضمون', 'موضوع'), P('Pages #', 'صفحہ نمبر', 'د مخ شمېره')],
          rows: contents.map(([unit, subject, page, urdu, pashto]) => [unit, P(subject, urdu, pashto), page])
        }
      },
      layout: [{t: 'table', id: 'contents'}],
      exclusions: ['Decorative heart-and-vessels header art and the "Contents" running tab are page furniture.']
    }
  ];
})();
