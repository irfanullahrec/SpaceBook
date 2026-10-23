'use strict';
/* The grammar topics of the four languages of the books, from the first lessons to the hardest. Each topic: id, name, level (1 first classes ... 5 Classes 11 and 12),
 * the group it sits in, and a pattern that recognises it in the heading of a lesson, the name of an exercise or the instruction above its questions
 * (English words, or Urdu / Pashto / Arabic words in the books of those languages). The first topic whose pattern matches is the one: so the
 * specific topics come before the general ones. Dev-only, used by tools/grammar/build_grammar.js. */
const T = (id, name, lvl, group, rx, native) => ({ id, name, lvl, group, rx, native: native || '' });
// a whole word of the Arabic script (the letters, not the vowel marks, end a word): JavaScript's \b does not know them
const AL = 'ء-غف-يٱ-ۓھہ-ۃ';
const W = terms => new RegExp('(?<![' + AL + '])(?:' + terms + ')(?![' + AL + '])');

const EN = [
  T('letters', 'Letters, vowels and consonants', 1, 'Sounds and spelling', /alphabet|vowel|consonant|capital letters?\b(?!.*sentence)|small letters?|letter sounds?|phonic|blends?\b|digraph|initial (sound|letter)|syllable|word families/i),
  T('spelling', 'Spelling and sight words', 1, 'Sounds and spelling', /spell|sight words?|missing letters?|silent letters?/i),
  T('articles', 'Articles (a, an, the)', 1, 'Words and their jobs', /\barticles?\b/i),
  T('pronoun-kinds', 'Kinds of pronouns (reflexive, relative, demonstrative)', 3, 'Words and their jobs', /reflexive|relative pronouns?|demonstrative|possessive pronouns?|indefinite pronouns?|interrogative pronouns?|types of pronouns|emphatic/i),
  T('pronouns', 'Pronouns', 1, 'Words and their jobs', /pronouns?/i),
  T('noun-kinds', 'Kinds of nouns (collective, abstract, countable)', 3, 'Words and their jobs', /collective|abstract nouns?|concrete nouns?|countable|uncountable|compound nouns?|types of nouns|material nouns?|proper nouns?.*common|common nouns?.*proper/i),
  T('possessives', 'Possessives and apostrophes', 2, 'Words and their jobs', /possessive|apostrophe/i),
  T('plurals', 'Singular and plural', 1, 'Words and their jobs', /plurals?\b|singular/i),
  T('nouns', 'Nouns (naming words)', 1, 'Words and their jobs', /\bnouns?\b|naming words?|people, animals|names of/i),
  T('phrasal', 'Phrasal verbs', 4, 'Verbs and tenses', /phrasal verbs?/i),
  T('modals', 'Helping verbs and modals', 3, 'Verbs and tenses', /helping verbs?|auxiliar|modals?\b|can\b.*could|should|must\b|ought/i),
  T('subject-verb', 'Subject-verb agreement', 3, 'Verbs and tenses', /subject.?verb|agreement|concord/i),
  T('conditionals', 'Conditional sentences', 4, 'Verbs and tenses', /conditionals?|if clause|if-clause/i),
  T('voice', 'Active and passive voice', 4, 'Verbs and tenses', /passive|active voice|\bvoice\b/i),
  T('speech', 'Direct and indirect speech', 4, 'Verbs and tenses', /direct (to|and|&) indirect|indirect speech|reported speech|narration|direct speech/i),
  T('verbals', 'Gerunds, participles and infinitives', 4, 'Verbs and tenses', /gerund|participle|infinitive|-ing forms?/i),
  T('perfect', 'Perfect tenses', 3, 'Verbs and tenses', /perfect/i),
  T('continuous', 'Continuous tenses', 3, 'Verbs and tenses', /continuous|progressive/i),
  T('tenses', 'Tenses (past, present, future)', 2, 'Verbs and tenses', /\btenses?\b|simple (present|past|future)|present simple|past simple|past tense|present tense|future tense|\bwill\b.*\bshall\b|regular and irregular|irregular verbs?/i),
  T('verbs', 'Verbs (action words)', 1, 'Verbs and tenses', /action words?|\bverbs?\b|doing words?/i),
  T('adj-degrees', 'Degrees of comparison', 2, 'Words and their jobs', /degrees?|comparative|superlative|comparison/i),
  T('adj-kinds', 'Kinds and order of adjectives', 3, 'Words and their jobs', /types of adjectives|compound adjectives|order of adjectives|kinds of adjectives|proper adjectives|possessive adjectives|demonstrative adjectives|quantity/i),
  T('adjectives', 'Adjectives (describing words)', 1, 'Words and their jobs', /adjectives?|describing words?/i),
  T('adverbs', 'Adverbs', 2, 'Words and their jobs', /adverbs?/i),
  T('prepositions', 'Prepositions', 1, 'Words and their jobs', /prepositions?|direction signs|position words|in, on|on, under|up, down/i),
  T('conjunctions', 'Conjunctions and joining words', 2, 'Words and their jobs', /conjunctions?|joining words?|connectives?|linking words?|and, but|because|transition/i),
  T('determiners', 'Determiners and quantifiers', 3, 'Words and their jobs', /determiners?|quantifiers?|some and any|much and many|few and little/i),
  T('interjections', 'Interjections', 3, 'Words and their jobs', /interjections?|exclamations?/i),
  T('question-tags', 'Question tags', 4, 'Sentences', /question tags?|tag questions?/i),
  T('questions', 'Asking questions (wh-words)', 2, 'Sentences', /question words?|wh-?\s|interrogative|asking questions?|\bwho\b.*\bwhat\b/i),
  T('sentence-kinds', 'Kinds of sentences', 3, 'Sentences', /declarative|imperative|exclamatory|simple, compound|compound sentence|complex sentence|types of sentences?|kinds of sentences?|statements?, questions?/i),
  T('clauses', 'Phrases and clauses', 4, 'Sentences', /phrases?\b(?!.*vocab)|clauses?|subordinate|relative clauses?|noun clause|adverbial/i),
  T('contractions', 'Contractions', 2, 'Punctuation', /contractions?/i),
  T('punctuation', 'Punctuation and capital letters', 1, 'Punctuation', /punctuat|full stops?|commas?|question marks?|exclamation marks?|quotation|capitali[sz]e|capital letters?|colons?|semi-?colons?|hyphens?|dashes?|inverted commas/i),
  T('sentences', 'Making sentences', 1, 'Sentences', /sentences?|word order|jumbled|rearrange|unscramble|complete the sentence/i),
  T('synonyms', 'Synonyms (same meaning)', 2, 'Word study', /synonyms?|same meaning|similar meaning|thesaurus/i),
  T('antonyms', 'Antonyms (opposites)', 1, 'Word study', /antonyms?|opposites?/i),
  T('homophones', 'Homophones and homonyms', 2, 'Word study', /homophones?|homonyms?|homographs?|sound alike/i),
  T('affixes', 'Prefixes, suffixes and root words', 3, 'Word study', /prefix|suffix|root words?|word formation|affix/i),
  T('compound-words', 'Compound words', 2, 'Word study', /compound words?/i),
  T('idioms', 'Idioms and proverbs', 4, 'Word study', /idioms?|proverbs?|figurative/i),
  T('cohesion', 'Linking ideas in writing', 4, 'Sentences', /cohesi|linking devices?|transitional/i),
  T('vocabulary', 'Word meanings and vocabulary', 1, 'Word study', /word meanings?|meaning of|vocabulary|dictionary|new words|word bank|use of language/i)
];

const UR = [
  T('ur-letters', 'حروفِ تہجی اور املا', 1, 'حروف اور املا', /حروفِ? تہجی|ہجے|املا|الف بے|حروف سے لفظ|حروف الگ|حروف جوڑ|حرکات|اعراب|نقطے/, 'Letters and spelling'),
  T('ur-ism-kinds', 'اسم کی قسمیں', 3, 'اسم، ضمیر، صفت', /اسم (ذات|صفت|معرفہ|نکرہ|مصدر|علم|جنس|کیفیت|تصغیر)|اسمِ? (ذات|صفت|معرفہ|نکرہ)|معرفہ|نکرہ|اقسامِ? اسم|اسم کی اقسام/, 'Kinds of nouns'),
  T('ur-ism', 'اسم', 1, 'اسم، ضمیر، صفت', W('اسم|اسموں|چیزوں کے نام|ناموں|نام چن'), 'Nouns'),
  T('ur-zameer', 'ضمیر', 2, 'اسم، ضمیر، صفت', W('ضمیر|ضمائر|ضمیریں'), 'Pronouns'),
  T('ur-sifat', 'صفت', 2, 'اسم، ضمیر، صفت', W('صفت|صفات|صفتیں'), 'Adjectives'),
  T('ur-amr-nahi', 'فعلِ امر اور نہی', 3, 'فعل', /فعلِ? ?(امر|نہی)|امر و نہی|صیغۂ? ?(امر|نہی)|حکم دینے|منع کرنے/, 'Command and prohibition'),
  T('ur-lazim', 'فعلِ لازم اور متعدی', 4, 'فعل', W('لازم|متعدی'), 'Intransitive and transitive verbs'),
  T('ur-zamana', 'فعل کے زمانے', 3, 'فعل', /ماضی|مستقبل|فعلِ? ?حال|فعل کے زمانے|زمانۂ? ?(ماضی|حال|مستقبل)|تین زمانے/, 'Tenses'),
  T('ur-fail', 'فعل', 1, 'فعل', W('فعل|افعال|کام کے نام|فعلوں'), 'Verbs'),
  T('ur-huroof', 'حروفِ جار اور عطف', 3, 'حروف', /حروفِ? ?(جار|عطف|ربط|ندا|تعجب|تاکید)|حرفِ? ?(جار|عطف)|حروف جار|حرفِ جار|حروف عطف/, 'Prepositions and conjunctions'),
  T('ur-tazkir', 'مذکر اور مؤنث', 1, 'جنس اور عدد', /مذکر|مؤنث|مونث|تذکیر|تانیث/, 'Masculine and feminine'),
  T('ur-wahid-jama', 'واحد اور جمع', 1, 'جنس اور عدد', /واحد|جمع کی|جمع بنا|جمع کے|جمع لکھ|جمع کیجیے|جمع بنائ/, 'Singular and plural'),
  T('ur-mutazad', 'متضاد الفاظ', 1, 'الفاظ کا مطالعہ', /متضاد|الٹ|ضد/, 'Opposites'),
  T('ur-mutaradif', 'مترادف الفاظ', 2, 'الفاظ کا مطالعہ', /مترادف|ہم معنی|ہم معنیٰ/, 'Synonyms'),
  T('ur-sabiqa', 'سابقے اور لاحقے', 3, 'الفاظ کا مطالعہ', /سابق[ہے]|لاحق[ہے]|سابقے|لاحقے/, 'Prefixes and suffixes'),
  T('ur-muhavare', 'محاورے اور ضرب المثل', 3, 'الفاظ کا مطالعہ', /محاور|ضرب المثل|کہاوت/, 'Idioms and proverbs'),
  T('ur-ramooz', 'رموزِ اوقاف', 2, 'جملہ', /رموزِ? ?اوقاف|علاماتِ? ?(وقف|ترقیم)|وقف کی علامات|سکتہ|ختمہ|ندائیہ/, 'Punctuation'),
  T('ur-jumla-kinds', 'جملے کی قسمیں', 4, 'جملہ', /جملہ (اسمیہ|فعلیہ|خبریہ|انشائیہ|شرطیہ)|اسمیہ|فعلیہ|خبریہ|انشائیہ|سادہ جملہ|مرکب جملہ|مرکبات|ترکیب/, 'Kinds of sentences'),
  T('ur-jumla', 'جملہ بنانا', 1, 'جملہ', /جملہ|جملے|جملوں|فقرہ|فقرے|ترتیب|بے ترتیب/, 'Making sentences'),
  T('ur-lugat', 'الفاظ اور معنی', 1, 'الفاظ کا مطالعہ', /معنی|معانی|الفاظ|لغت|مفہوم/, 'Words and meanings')
];

const PS = [
  T('ps-letters', 'حروف او املا', 1, 'حروف او املا', /حرف|حروف|املا|ټکي جوړ|لفظونه ساز|هجا|ورکې/, 'Letters and spelling'),
  T('ps-noun', 'اسم', 1, 'اسم، ضمیر، صفت', W('اسم|اسمونه|نوم|نومونه'), 'Nouns'),
  T('ps-pronoun', 'ضمیر', 2, 'اسم، ضمیر، صفت', W('ضمیر|ضمیرونه'), 'Pronouns'),
  T('ps-adjective', 'صفت', 2, 'اسم، ضمیر، صفت', W('صفت|صفتونه|ستاینوم|ستاینومونه'), 'Adjectives'),
  T('ps-verb', 'فعل', 1, 'فعل', W('فعل|فعلونه|کړنه|کړنې'), 'Verbs'),
  T('ps-gender', 'مذکر او مؤنث', 1, 'جنس او شمېر', /مذکر|مؤنث|مونث|نرینه|ښځینه|نر او ښځه/, 'Masculine and feminine'),
  T('ps-number', 'واحد او جمع', 1, 'جنس او شمېر', /واحد|جمع|مفرد/, 'Singular and plural'),
  T('ps-opposites', 'متضاد', 1, 'د ټکو مطالعه', /متضاد|ضد|مخالف/, 'Opposites'),
  T('ps-synonyms', 'مترادف', 2, 'د ټکو مطالعه', /مترادف|هم معنی|ورته معنی/, 'Synonyms'),
  T('ps-proverbs', 'متلونه او اصطلاحات', 3, 'د ټکو مطالعه', /متل|متلونه|اصطلاح|کنایه/, 'Proverbs and idioms'),
  T('ps-punctuation', 'د وقف نخښې', 2, 'جمله', /نخښ|وقف|سکته|ختمه/, 'Punctuation'),
  T('ps-sentence', 'جمله', 1, 'جمله', /جمله|جملې|جملو/, 'Sentences'),
  T('ps-meaning', 'ټکي او معنې', 1, 'د ټکو مطالعه', /معنی|معنې|ټکي|لفظونه|لغات/, 'Words and meanings')
];

const AR = [
  T('ar-letters', 'الحروف والحركات', 1, 'الحروف والكلمات', /حروف(?! ?جار)|حرکات|حركات|تشدید|تنوین/, 'Letters and vowel marks'),
  T('ar-ism-fil-harf', 'الاسم والفعل والحرف', 1, 'أقسام الكلام', /اسم.*فعل.*حرف|الاسم|الفعل|الحرف|اسم اور فعل|اسم، فعل|کلمہ کی اقسام/, 'Noun, verb and particle'),
  T('ar-gender', 'المذكر والمؤنث', 1, 'أقسام الكلام', /مذکر|مؤنث|المذكر|المؤنث/, 'Masculine and feminine'),
  T('ar-number', 'المفرد والمثنى والجمع', 2, 'أقسام الكلام', /مفرد|مثنی|مثنى|تثنیہ|جمع|واحد/, 'Singular, dual and plural'),
  T('ar-pronoun', 'الضمائر وأسماء الإشارة', 2, 'أقسام الكلام', /ضمیر|ضمائر|اشارہ|إشارة|ہذا|ہذه|موصول/, 'Pronouns and demonstratives'),
  T('ar-tenses', 'الماضي والمضارع والأمر', 3, 'الأفعال', /ماضی|مضارع|امر|الماضي|المضارع|الأمر|نہی|صیغ/, 'Past, present and command'),
  T('ar-harf-jarr', 'حروف الجر', 3, 'أقسام الكلام', /حروفِ? جار|حرفِ? جار|حروف الجر|من، إلى|في، على/, 'Prepositions'),
  T('ar-adjective', 'النعت والصفة', 3, 'أقسام الكلام', /نعت|صفت|الصفة|منعوت/, 'Adjectives'),
  T('ar-sentence', 'الجملة الاسمية والفعلية', 3, 'الجملة', /جملہ|جملة|اسمیہ|فعلیہ|مبتدا|خبر|فاعل|مفعول|اضافت|مضاف/, 'Kinds of sentences'),
  T('ar-numbers', 'الأعداد', 4, 'الجملة', /عدد|اعداد|الأعداد|معدود/, 'Numbers'),
  T('ar-i3rab', 'الإعراب', 5, 'الجملة', /اعراب|إعراب|مرفوع|منصوب|مجرور|مبنی|معرب/, 'Case endings')
];

module.exports = { EN, UR, PS, AR, LANGS: { en: EN, ur: UR, ps: PS, ar: AR } };
