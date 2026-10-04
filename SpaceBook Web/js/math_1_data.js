// Khyber Pakhtunkhwa Textbook Board, Mathematics 1 (Curriculum 2020).
// Content is reorganised from the supplied workbook scans. The scans stay outside
// the app bundle; only structured lesson and practice text is loaded here.
function makeMath1Section(id, title, theory, rules, examples) {
  return { id, title, theory, rules, examples: examples || [] };
}

function makeMath1Problem(num, question, solution, finalAnswer, steps) {
  return { num, question, solution, finalAnswer, steps: steps || [solution], method: 'Show your working' };
}

function makeMath1Chapter(number, id, title, titleUrdu, pageRange, description, sections, examples, exercises, slos, formulaSheet) {
  const urduLessons = MATH_1_URDU[number] || [];
  sections.forEach((section, index) => {
    if (urduLessons[index]) {
      section.theoryUrdu = urduLessons[index].theory;
      section.rulesUrdu = urduLessons[index].rules;
    }
  });
  return {
    number, id, title, titleUrdu, status: 'ready', badge: 'Class 1 Workbook Matched', pageRange,
    description, sections, workedExamples: examples, exercises, slos, formulaSheet
  };
}

var MATH_1_URDU = {
  1: [
    { theory: 'چیزوں کو ایک ایک کرکے گنیں۔ اعداد بتاتے ہیں کہ چیزیں کتنی ہیں۔ ۰ کا مطلب ہے کہ کوئی چیز موجود نہیں۔ ۰ سے ۱۰۰ تک کے اعداد پڑھیں اور لکھیں۔', rules: ['گنتے وقت ہر چیز کی طرف ایک بار اشارہ کریں۔', '۹۹ کے بعد ۱۰۰ آتا ہے۔'] },
    { theory: 'دو ہندسوں والے عدد میں دہائیاں اور اکائیاں ہوتی ہیں۔ ۳۴ میں ۳ کا مطلب ۳ دہائیاں اور ۴ کا مطلب ۴ اکائیاں ہیں۔ اس لیے ۳۴ = ۳۰ + ۴۔', rules: ['پہلے دہائیوں کا ہندسہ اور پھر اکائیوں کا ہندسہ پڑھیں۔', 'دس اکائیاں مل کر ایک دہائی بنتی ہیں۔'] },
    { theory: 'پچھلا عدد ایک کم ہوتا ہے۔ اگلا عدد ایک زیادہ ہوتا ہے۔ دو اعداد کے درمیان آنے والا عدد پہلے سے بڑا اور دوسرے سے چھوٹا ہوتا ہے۔', rules: ['عدد کی لکیر پر دائیں طرف جانے سے اعداد بڑھتے ہیں۔', 'درمیانی عدد دونوں اعداد کے درمیان ہونا چاہیے۔'] },
    { theory: 'اعداد کا موازنہ کرنے کے لیے بڑا (>), چھوٹا (<) یا برابر (=) کا نشان استعمال کریں۔ پہلے دہائیوں کا موازنہ کریں۔ دہائیاں برابر ہوں تو اکائیوں کو دیکھیں۔', rules: ['< یا > کا کھلا حصہ بڑے عدد کی طرف ہوتا ہے۔', 'بڑھتی ترتیب چھوٹے سے بڑے اور گھٹتی ترتیب بڑے سے چھوٹے عدد تک ہوتی ہے۔'] },
    { theory: 'ترتیبی اعداد جگہ یا مقام بتاتے ہیں، جیسے پہلا، دوسرا، تیسرا اور چوتھا۔ نمونہ کسی قاعدے کے مطابق دہرایا یا بدلتا ہے۔ اگلی چیز معلوم کرنے کے لیے قاعدہ دیکھیں۔', rules: ['مقام معلوم کرنے کے لیے چیزوں کو گنیں۔', 'نمونہ مکمل کرنے سے پہلے اس کا قاعدہ بتائیں۔'] }
  ],
  2: [
    { theory: 'جمع کرنے کا مطلب گروہوں کو ملانا ہے۔ جمع کا نشان (+) استعمال کریں۔ حاصل معلوم کرنے کے لیے آگے گنتی کریں۔', rules: ['بڑے عدد سے شروع کرکے چھوٹے گروہ تک آگے گنیں۔', 'جمع کرنے والے اعداد کی ترتیب بدلنے سے حاصل نہیں بدلتا۔'] },
    { theory: 'چھوٹے اعداد جمع کرنے کے لیے آگے گنتی کریں یا چیزوں، انگلیوں اور عددی لکیر کی مدد لیں۔ ضرورت ہو تو دس کا ایک گروہ بنائیں۔', rules: ['ہر چیز کو صرف ایک بار گنیں۔', 'حاصل کو دوبارہ گن کر جمع کی پڑتال کریں۔'] },
    { theory: 'اکائیوں کو اکائیوں کے نیچے اور دہائیوں کو دہائیوں کے نیچے لکھیں۔ پہلے اکائیاں جمع کریں اور پھر دہائیاں۔ ضرورت پڑنے پر دس اکائیوں کو ایک دہائی بنائیں۔', rules: ['اعداد کو ان کی درست جگہوں کے نیچے لکھیں۔', 'دوبارہ گروہ بنائی گئی دہائی کو دہائیوں میں شامل کریں۔'] },
    { theory: 'تفریق کا مطلب چیزیں کم کرنا یا باقی تعداد معلوم کرنا ہے۔ تفریق کا نشان (−) استعمال کریں۔ پیچھے گنتی کریں یا دونوں گروہوں کا موازنہ کریں۔', rules: ['اسی عدد سے شروع کریں جس میں سے تفریق کرنی ہے۔', 'جواب کو کم کیے گئے عدد میں جمع کرکے پڑتال کریں۔'] },
    { theory: 'خالی جگہ والے سوال میں جمع اور تفریق کے تعلق سے کام لیں۔ مثال کے طور پر ۷ + □ = ۱۲ میں معلوم کریں کہ ۷ میں کتنا جمع کرنے سے ۱۲ بنتا ہے۔', rules: ['جمع اور تفریق ایک دوسرے کی پڑتال کر سکتے ہیں۔', 'کہانی والے سوالات کے لیے چیزیں یا عددی لکیر استعمال کریں۔'] }
  ],
  3: [
    { theory: 'اشیا کی لمبائی کا موازنہ کرنے کے لیے انہیں ساتھ رکھیں اور ایک سرا برابر کریں۔ لمبی، زیادہ لمبی اور سب سے لمبی جیسے الفاظ استعمال کریں۔', rules: ['موازنہ سے پہلے ایک طرف کے سرے برابر کریں۔', 'لمبائی کا موازنہ ایک ہی سمت میں کریں۔'] },
    { theory: 'جس چیز کی لمبائی کم ہو وہ چھوٹی ہوتی ہے۔ سب سے چھوٹی چیز معلوم کرنے کے لیے تمام اشیا کو ایک ہی نقطے سے ملائیں۔', rules: ['چھوٹی کا لفظ لمبائی کے لیے ہے، اونچائی یا وزن کے لیے نہیں۔', 'ہر چیز کو ایک ہی نقطۂ آغاز سے ملائیں۔'] },
    { theory: 'اونچائی بتاتی ہے کہ کوئی چیز نیچے سے اوپر تک کتنی بلند ہے۔ چیزوں کو ایک ہی ہموار سطح پر رکھ کر موازنہ کریں۔', rules: ['دونوں چیزوں کو ایک ہی بنیاد پر کھڑا رکھیں۔', 'اونچائی کے لیے بلند، زیادہ بلند اور سب سے بلند کہیں۔'] },
    { theory: 'کمیت بتاتی ہے کہ چیز کتنی بھاری یا ہلکی ہے۔ اشیا کا موازنہ ہاتھ میں اٹھا کر یا ترازو کے ذریعے کریں۔', rules: ['ترازو کا بھاری پلڑا نیچے جھکتا ہے۔', 'بھاری، ہلکا یا برابر وزن جیسے الفاظ استعمال کریں۔'] }
  ],
  4: [
    { theory: 'پیسے چیزیں خریدنے کے لیے استعمال ہوتے ہیں۔ پاکستانی کرنسی میں روپے اور پیسے شامل ہیں۔ سکوں اور نوٹوں کی مالیت مختلف ہوتی ہے۔ ان پر لکھی مالیت پڑھیں۔', rules: ['روپے کے لیے Rs لکھا جاتا ہے۔', 'پیسے گنتے وقت ہر سکے اور نوٹ کی مالیت دیکھیں۔'] },
    { theory: 'کل رقم معلوم کرنے کے لیے ہر سکے یا نوٹ کی مالیت جمع کریں۔ پہلے بڑی مالیت گنیں، پھر چھوٹی مالیت۔', rules: ['ایک جیسی مالیت کے سکے اکٹھے رکھیں۔', 'ہر سکے یا نوٹ کو صرف ایک بار گنیں۔'] },
    { theory: 'ایک ہی رقم مختلف طریقوں سے بنائی جا سکتی ہے۔ مثال کے طور پر دس روپے کا ایک نوٹ یا پانچ روپے کے دو سکے، دونوں دس روپے بنتے ہیں۔', rules: ['مختلف سکوں اور نوٹوں کی مالیت برابر ہو سکتی ہے۔', 'رقم کی پڑتال کے لیے تمام مالیتیں جمع کریں۔'] },
    { theory: 'ایک سے زیادہ چیزوں کی قیمت معلوم کرنے کے لیے قیمتیں جمع کریں۔ اگر ادا کی گئی رقم قیمت سے زیادہ ہو تو قیمت کو ادا کی گئی رقم سے منہا کرکے بقایا معلوم کریں۔', rules: ['قیمت اور بقایا مل کر ادا کی گئی رقم بنتے ہیں۔', 'روپے جمع یا منہا کرتے وقت جگہ کی قدر درست رکھیں۔'] }
  ],
  5: [
    { theory: 'گھڑی وقت بتاتی ہے۔ چھوٹی سوئی گھنٹہ بتاتی ہے اور لمبی سوئی منٹ بتاتی ہے۔ جب لمبی سوئی ۱۲ پر ہو تو چھوٹی سوئی سے گھنٹہ پڑھیں۔', rules: ['گھنٹہ معلوم کرنے کے لیے چھوٹی سوئی دیکھیں۔', 'منٹ کی سوئی ۱۲ پر ہو تو پورا گھنٹہ ہوتا ہے۔'] },
    { theory: 'سوئیوں والی گھڑی میں وقت سوئیوں سے ظاہر ہوتا ہے۔ ڈیجیٹل گھڑی وقت کو ہندسوں میں دکھاتی ہے۔ ڈیجیٹل گھڑی پر گھنٹے اور منٹ پڑھیں۔', rules: ['۷:۰۰ میں ۷ گھنٹہ ہے اور ۰۰ پورا گھنٹہ بتاتا ہے۔', 'سوئیوں والی اور ڈیجیٹل گھڑی ایک ہی وقت دکھا سکتی ہیں۔'] },
    { theory: 'دن کے حصے صبح، دوپہر، شام اور رات ہیں۔ دن کے مختلف حصوں میں ہم مختلف کام کرتے ہیں۔', rules: ['صبح، دوپہر سے پہلے آتی ہے۔', 'رات، شام کے بعد آتی ہے۔'] },
    { theory: 'ہفتے میں سات دن ہوتے ہیں: پیر، منگل، بدھ، جمعرات، جمعہ، ہفتہ اور اتوار۔ دن اسی ترتیب میں بار بار آتے ہیں۔', rules: ['ساتوں دنوں کی ترتیب یاد کریں۔', 'اتوار کے بعد پیر آتا ہے۔'] },
    { theory: 'سال میں بارہ مہینے ہوتے ہیں۔ شمسی مہینے جنوری سے دسمبر تک ہیں۔ اسلامی مہینے قمری سال کے مطابق آتے ہیں۔', rules: ['شمسی سال میں بارہ مہینے ہوتے ہیں۔', 'مہینوں کی ترتیب اور املا کیلنڈر میں دیکھیں۔'] }
  ],
  6: [
    { theory: 'چپٹی شکل کے کنارے اور کونے ہوتے ہیں۔ دائرہ گول ہوتا ہے اور اس کے سیدھے کنارے یا کونے نہیں ہوتے۔ مثلث کے ۳، مربع کے ۴ برابر اور مستطیل کے ۴ کنارے ہوتے ہیں۔', rules: ['شکل پہچاننے کے لیے کنارے اور کونے گنیں۔', 'مربع کے چار برابر کنارے جبکہ مستطیل کے دو لمبے اور دو چھوٹے کنارے ہوتے ہیں۔'] },
    { theory: 'روزمرہ چیزوں میں شکلیں تلاش کریں۔ گھڑی کا ڈائل دائرہ اور کتاب کا سرورق اکثر مستطیل ہوتا ہے۔ شکل کا نام اس کے رنگ یا سائز سے نہیں بدلتا۔', rules: ['سائز یا رنگ بدلنے سے شکل کا نام نہیں بدلتا۔', 'شک ہو تو شکل کو گھما کر کنارے دوبارہ گنیں۔'] },
    { theory: 'نمونہ کسی قاعدے کی پیروی کرتا ہے۔ اس میں شکلیں، رنگ یا چیزیں دہرائی جا سکتی ہیں۔ پہلے دہرائے جانے والے حصے کو پہچانیں، پھر اسی ترتیب کو جاری رکھیں۔', rules: ['قاعدہ معلوم کرنے کے لیے ایک سے زیادہ چیزیں دیکھیں۔', 'نمونہ جاری رکھتے وقت ترتیب وہی رکھیں۔'] },
    { theory: 'جگہ بتانے والے الفاظ سے معلوم ہوتا ہے کہ کوئی چیز کہاں ہے۔ اندر کا مطلب حد کے اندر اور باہر کا مطلب حد سے آگے ہے۔ اوپر بلند اور نیچے کم اونچائی پر ہونے کو کہتے ہیں۔', rules: ['جگہ بتاتے وقت دوسری چیز کا نام لیں۔', 'اوپر اور نیچے عمودی جگہ بتاتے ہیں۔'] },
    { theory: 'اوپر اور نیچے جگہ بتاتے ہیں۔ قریب کا مطلب نزدیک اور دور کا مطلب زیادہ فاصلے پر ہے۔ پہلے اور بعد ترتیب یا مقام بتاتے ہیں۔', rules: ['جگہ بتاتے وقت واضح کریں کہ کس چیز کے مقابلے میں بتا رہے ہیں۔', 'قریب اور دور کا موازنہ دوسری چیز کی نسبت سے ہوتا ہے۔'] }
  ]
};

var MATH_1_DATA = [
  makeMath1Chapter(1, 'u1', 'Whole Numbers', 'کامل اعداد', 'Pages 1–42',
    'Counting, reading and writing numbers to 100, place value, comparing, ordering, ordinal numbers and number patterns.', [
      makeMath1Section('1.1', 'Counting and Number Names', 'Count objects carefully, one at a time. Numbers tell how many. Read and write the numbers from 0 to 100. Zero means that there are no objects.', ['Say each number in order and point to one object as you count.', 'The number after 99 is 100.'], [
        { problem: 'Write the number name for 14.', steps: ['Say the number: fourteen.'], answer: 'fourteen' },
        { problem: 'There are 8 birds. Two more birds join them. How many birds are there?', steps: ['Start at 8 and count on: 9, 10.'], answer: '10 birds' }
      ]),
      makeMath1Section('1.2', 'Tens and Ones', 'A two-digit number has tens and ones. In 34, the digit 3 means 3 tens and the digit 4 means 4 ones. So 34 = 30 + 4.', ['Read the tens digit first, then the ones digit.', 'Ten ones make one ten.'], [
        { problem: 'Show 26 as tens and ones.', steps: ['The tens digit is 2 and the ones digit is 6.'], answer: '2 tens and 6 ones' }
      ]),
      makeMath1Section('1.3', 'Before, After and Between', 'A number before is one less. A number after is one more. A number between two numbers is greater than the first and less than the second.', ['On a number line, numbers increase as you move to the right.', 'Check that the between number is in the correct place.'], [
        { problem: 'What number comes between 47 and 49?', steps: ['Count forward from 47: 48, 49.'], answer: '48' }
      ]),
      makeMath1Section('1.4', 'Comparing and Ordering Numbers', 'Compare numbers using greater than (>), less than (<) or equal to (=). For two-digit numbers, compare the tens first. If the tens are equal, compare the ones.', ['The open side of < or > faces the greater number.', 'Ascending order goes from smallest to greatest; descending order goes from greatest to smallest.'], [
        { problem: 'Compare 52 and 25.', steps: ['52 has 5 tens; 25 has 2 tens.', 'Five tens are more than two tens.'], answer: '52 > 25' }
      ]),
      makeMath1Section('1.5', 'Ordinal Numbers and Patterns', 'Ordinal numbers show position: first, second, third, fourth and fifth. A pattern repeats or changes in a rule. Look at what comes next each time.', ['Count objects to find their position.', 'For a pattern, say the rule aloud before filling the next item.'], [
        { problem: 'Complete: 2, 4, 6, __.', steps: ['Each number increases by 2.'], answer: '8' }
      ])
    ], [
      { id: 'ex1', title: 'Counting and Place Value', problem: 'Write 38 in words and as tens and ones.', given: 'Number: 38', method: 'Read the digits and split into tens and ones.', steps: ['38 is read as thirty-eight.', 'The 3 means 3 tens and the 8 means 8 ones.', '38 = 30 + 8.'], answer: 'thirty-eight; 3 tens and 8 ones' },
      { id: 'ex2', title: 'Compare and Order', problem: 'Put 19, 91 and 29 in ascending order.', given: '19, 91, 29', method: 'Compare tens, then ones.', steps: ['19 has 1 ten, 29 has 2 tens and 91 has 9 tens.', 'Write from fewest tens to most tens.'], answer: '19, 29, 91' }
    ], [
      { exercise: '1.1', title: 'Exercise 1.1 — Whole Numbers', problems: [
        makeMath1Problem('Q1', 'Write 63 in words.', '63 is sixty-three.', 'sixty-three'),
        makeMath1Problem('Q2', 'How many tens and ones are in 47?', '47 = 40 + 7.', '4 tens and 7 ones'),
        makeMath1Problem('Q3', 'Fill in the missing numbers: 32, 33, __, 35.', 'The numbers increase by one: 32, 33, 34, 35.', '34'),
        makeMath1Problem('Q4', 'Arrange 8, 18 and 80 from greatest to smallest.', '80 has 8 tens; 18 has 1 ten; 8 has no tens.', '80, 18, 8')
      ] }
    ], {
      mcqs: [
        { q: 'What number comes after 59?', options: ['58', '60', '69', '50'], correct: 1, exp: 'Count one more than 59: the answer is 60.' },
        { q: 'How many tens are in 42?', options: ['2', '4', '40', '42'], correct: 1, exp: 'The tens digit is 4, so 42 has 4 tens.' },
        { q: 'Which sign makes 17 __ 71 true?', options: ['>', '<', '=', '+'], correct: 1, exp: '17 is smaller than 71, so use <.' },
        { q: 'What comes between 30 and 32?', options: ['29', '31', '33', '20'], correct: 1, exp: 'Counting forward gives 30, 31, 32.' }
      ],
      shortQuestions: [
        { q: 'What does zero mean?', sol: 'Zero means there are no objects or none of something.' },
        { q: 'Write 56 as tens and ones.', sol: '56 has 5 tens and 6 ones: 50 + 6.' },
        { q: 'What is ascending order?', sol: 'Ascending order means arranging numbers from the smallest to the greatest.' }
      ],
      longQuestions: [
        { q: 'Explain how to compare 36 and 63, then arrange 36, 63 and 33 in ascending order.', marks: 4, rubric: 'Award marks for comparing tens and giving the correct order.', sol: '36 has 3 tens and 63 has 6 tens, so 36 < 63. The numbers in ascending order are 33, 36, 63.' },
        { q: 'Show 74 using tens and ones, and write its number name.', marks: 3, rubric: 'Identify the place values and write the number name.', sol: '74 = 70 + 4 = 7 tens and 4 ones. Its number name is seventy-four.' }
      ]
    }, [{ name: 'Place value', formula: 'Two-digit number = tens + ones' }, { name: 'Compare', formula: 'Compare tens first, then ones' }]),

  makeMath1Chapter(2, 'u2', 'Number Operations: Addition and Subtraction', 'اعداد کے عمل: جمع اور تفریق', 'Pages 43–74',
    'Understand addition as putting together and subtraction as taking away; solve number sentences and everyday problems.', [
      makeMath1Section('2.1', 'Addition and the Plus Sign', 'Addition joins groups. The plus sign (+) means add, and the equals sign (=) means has the same value. Count on to find a total.', ['Start with the larger group and count on the smaller group.', 'Changing the order of addends does not change the total.'], [
        { problem: 'Add 6 + 3.', steps: ['Start at 6 and count on 3: 7, 8, 9.'], answer: '9' }
      ]),
      makeMath1Section('2.2', 'Adding One-Digit Numbers', 'Add small numbers by counting on, using objects, fingers or a number line. Make a group of ten when it helps.', ['Count each object only once.', 'Check an addition answer by counting the total again.'], [
        { problem: 'Add 8 + 5.', steps: ['Start at 8 and count on five numbers: 9, 10, 11, 12, 13.'], answer: '13' }
      ]),
      makeMath1Section('2.3', 'Adding Two-Digit Numbers', 'Line up tens with tens and ones with ones. Add the ones, then add the tens. Regroup ten ones as one ten when needed.', ['Keep place values in the correct columns.', 'After regrouping, add the new ten to the tens column.'], [
        { problem: 'Add 24 + 13.', steps: ['Ones: 4 + 3 = 7.', 'Tens: 2 tens + 1 ten = 3 tens.'], answer: '37' }
      ]),
      makeMath1Section('2.4', 'Subtraction and the Minus Sign', 'Subtraction takes away or finds how many are left. The minus sign (−) means subtract. Count back or compare the groups.', ['Begin with the number you are taking from.', 'Check by adding the answer to the number taken away.'], [
        { problem: 'Subtract 9 − 4.', steps: ['Count back four from 9: 8, 7, 6, 5.'], answer: '5' }
      ]),
      makeMath1Section('2.5', 'Subtracting and Finding Missing Numbers', 'For a missing number sentence, use the relationship between addition and subtraction. For example, if 7 + □ = 12, find how many more than 7 make 12.', ['Addition and subtraction can check one another.', 'Use objects or a number line for story questions.'], [
        { problem: 'Fill the box: 15 − □ = 10.', steps: ['Ask how many must be taken from 15 to leave 10.', '15 − 5 = 10.'], answer: '5' }
      ])
    ], [
      { id: 'ex1', title: 'Add and Subtract', problem: 'Solve 28 + 15 and check using a number line.', given: '28 + 15', method: 'Add ones, regroup if necessary, then add tens.', steps: ['Ones: 8 + 5 = 13. Write 3 ones and regroup 1 ten.', 'Tens: 2 + 1 + 1 regrouped ten = 4 tens.'], answer: '43' },
      { id: 'ex2', title: 'A Story Problem', problem: 'There are 35 pencils. The class uses 12. How many are left?', given: '35 pencils; 12 used', method: 'Subtract the pencils used from the starting number.', steps: ['35 − 12', 'Ones: 5 − 2 = 3.', 'Tens: 3 − 1 = 2.'], answer: '23 pencils' }
    ], [
      { exercise: '2.1', title: 'Exercise 2.1 — Addition and Subtraction', problems: [
        makeMath1Problem('Q1', 'Add 7 + 6.', 'Start at 7 and count on 6: 8, 9, 10, 11, 12, 13.', '13'),
        makeMath1Problem('Q2', 'Add 32 + 25.', 'Ones: 2 + 5 = 7. Tens: 3 + 2 = 5.', '57'),
        makeMath1Problem('Q3', 'Subtract 48 − 16.', 'Ones: 8 − 6 = 2. Tens: 4 − 1 = 3.', '32'),
        makeMath1Problem('Q4', 'A basket has 26 apples. Add 14 apples. How many apples now?', '26 + 14 = 40.', '40 apples')
      ] }
    ], {
      mcqs: [
        { q: 'What is 8 + 5?', options: ['12', '13', '14', '15'], correct: 1, exp: 'Count on five from 8 to get 13.' },
        { q: 'What is 17 − 9?', options: ['6', '7', '8', '9'], correct: 2, exp: '17 take away 9 leaves 8.' },
        { q: 'Which sign means add?', options: ['−', '+', '=', '<'], correct: 1, exp: 'The plus sign (+) means add.' },
        { q: 'What is 20 + 30?', options: ['5', '23', '50', '60'], correct: 2, exp: 'Two tens plus three tens makes five tens: 50.' }
      ],
      shortQuestions: [
        { q: 'What does subtraction mean?', sol: 'Subtraction means taking away or finding the difference between numbers.' },
        { q: 'How can addition check subtraction?', sol: 'Add the answer to the amount taken away. The result should be the starting number.' },
        { q: 'Solve: 16 + 12.', sol: 'Ones: 6 + 2 = 8. Tens: 1 + 1 = 2. The answer is 28.' }
      ],
      longQuestions: [
        { q: 'A shop had 46 oranges. It sold 23 and then received 15 more. How many oranges are there now?', marks: 4, rubric: 'Show subtraction for the sale, addition for the new oranges, and the final answer.', sol: 'First subtract the oranges sold: 46 − 23 = 23. Then add the new oranges: 23 + 15 = 38. There are 38 oranges now.' },
        { q: 'Add 27 + 18 and explain regrouping.', marks: 3, rubric: 'Add ones correctly, regroup ten ones, and give the total.', sol: 'Ones: 7 + 8 = 15, which is 1 ten and 5 ones. Tens: 2 + 1 + 1 regrouped ten = 4 tens. The total is 45.' }
      ]
    }, [{ name: 'Addition check', formula: 'Addend + Addend = Sum' }, { name: 'Subtraction check', formula: 'Difference + Number taken away = Starting number' }]),

  makeMath1Chapter(3, 'u3', 'Measurement: Length and Mass', 'پیمائش: لمبائی اور وزن', 'Pages 75–86',
    'Compare and describe objects by length, height and mass using everyday language and simple comparisons.', [
      makeMath1Section('3.1', 'Long, Longer and Longest', 'Compare lengths by placing objects side by side and lining up one end. Use long, longer and longest to describe what you see.', ['Line up the starting ends before comparing.', 'Use the same direction when comparing lengths.'], [
        { problem: 'A 10 cm pencil and a 15 cm pencil: which is longer?', steps: ['Compare 15 with 10.'], answer: 'The 15 cm pencil is longer.' }
      ]),
      makeMath1Section('3.2', 'Short, Shorter and Shortest', 'An object with less length is shorter. Compare all objects from the same starting point to find the shortest.', ['Shorter describes length, not height or weight.', 'Check each object against the same start point.'], [
        { problem: 'Which is shorter: a 12 cm ribbon or an 8 cm ribbon?', steps: ['8 is less than 12.'], answer: 'The 8 cm ribbon.' }
      ]),
      makeMath1Section('3.3', 'Tall and High', 'Height tells how tall something is from bottom to top. Compare objects standing on the same level surface.', ['Keep both objects standing on the same base.', 'Use taller and tallest for height.'], [
        { problem: 'A tree is 5 m tall and a plant is 2 m tall. Which is taller?', steps: ['5 m is greater than 2 m.'], answer: 'The tree.' }
      ]),
      makeMath1Section('3.4', 'Heavy, Heavier and Light', 'Mass tells how heavy or light an object is. Compare objects by holding them or using a balance scale.', ['A balance tips down on the heavier side.', 'Use heavier, lighter and equally heavy.'], [
        { problem: 'A book weighs more than a feather. Which is heavier?', steps: ['The book has greater mass.'], answer: 'The book.' }
      ])
    ], [
      { id: 'ex1', title: 'Compare Length', problem: 'Three strings are 6 cm, 9 cm and 4 cm long. Name the longest and shortest.', given: '6 cm, 9 cm, 4 cm', method: 'Compare the measurements.', steps: ['9 cm is the greatest length.', '4 cm is the smallest length.'], answer: 'Longest: 9 cm; shortest: 4 cm' },
      { id: 'ex2', title: 'Compare Mass', problem: 'A watermelon is heavier than an apple. Which has less mass?', given: 'Watermelon is heavier than apple.', method: 'Use the meaning of heavier and lighter.', steps: ['If the watermelon is heavier, the apple is lighter.'], answer: 'The apple.' }
    ], [
      { exercise: '3.1', title: 'Exercise 3.1 — Measurement', problems: [
        makeMath1Problem('Q1', 'Which is longer: 14 cm or 11 cm?', '14 is greater than 11.', '14 cm'),
        makeMath1Problem('Q2', 'Order from shortest to longest: 3 cm, 8 cm, 5 cm.', 'Compare the numbers: 3 < 5 < 8.', '3 cm, 5 cm, 8 cm'),
        makeMath1Problem('Q3', 'A giraffe is taller than a goat. Which animal is shorter?', 'The goat is not as tall.', 'The goat'),
        makeMath1Problem('Q4', 'A stone is heavier than a leaf. Which is lighter?', 'The leaf has less mass.', 'The leaf')
      ] }
    ], {
      mcqs: [
        { q: 'Which word describes an object with more length?', options: ['shorter', 'longer', 'lighter', 'lower'], correct: 1, exp: 'Longer describes greater length.' },
        { q: 'Which is the shortest length?', options: ['9 cm', '4 cm', '7 cm', '8 cm'], correct: 1, exp: '4 cm is the smallest measurement.' },
        { q: 'A balance dips on which side?', options: ['lighter side', 'heavier side', 'shorter side', 'taller side'], correct: 1, exp: 'The heavier object makes its side of the balance dip.' },
        { q: 'Height is measured from:', options: ['top to bottom', 'side to side', 'around the edge', 'inside to outside'], correct: 0, exp: 'Height is measured from bottom to top.' }
      ],
      shortQuestions: [
        { q: 'How can you compare the length of two pencils?', sol: 'Place them side by side and line up one end. The pencil reaching farther is longer.' },
        { q: 'What does heavier mean?', sol: 'Heavier means an object has more mass than the object being compared.' },
        { q: 'Name one tool that can compare mass.', sol: 'A balance scale can compare the mass of two objects.' }
      ],
      longQuestions: [
        { q: 'A rope is 12 cm, a ribbon is 8 cm and a thread is 4 cm. Arrange them from shortest to longest.', marks: 3, rubric: 'Compare all three lengths and use the correct order.', sol: '4 cm < 8 cm < 12 cm. From shortest to longest: thread, ribbon, rope.' },
        { q: 'Explain how to compare the height of two plants and how to compare their mass.', marks: 4, rubric: 'Describe a fair height comparison and a suitable mass comparison.', sol: 'Place both plants on the same level surface and compare from the bottom to the top. To compare their mass, carefully use a balance scale; the side that dips is heavier.' }
      ]
    }, [{ name: 'Length', formula: 'Line up the ends to compare length' }, { name: 'Mass', formula: 'A balance dips toward the heavier object' }]),

  makeMath1Chapter(4, 'u4', 'Money', 'پیسے', 'Pages 87–100',
    'Recognise Pakistani coins and notes, compare their values, make amounts and solve simple shopping problems.', [
      makeMath1Section('4.1', 'Pakistani Coins and Notes', 'Money is used to buy things. Pakistani money includes rupees and paisa. Coins and notes can have different values. Read the number and name printed on each one.', ['Rs means rupees.', 'Handle money carefully and check the value before counting.'], [
        { problem: 'How many rupees are in a Rs 10 note?', steps: ['Read the value printed on the note.'], answer: '10 rupees' }
      ]),
      makeMath1Section('4.2', 'Counting Money', 'To find the total, add the value of each coin or note. Count larger values first, then smaller ones.', ['Keep coins of the same value together.', 'Count each coin or note once.'], [
        { problem: 'Find the total of Rs 10 and Rs 5.', steps: ['10 + 5 = 15.'], answer: 'Rs 15' }
      ]),
      makeMath1Section('4.3', 'Making the Same Amount', 'The same amount can be made in different ways. For example, Rs 10 can be one Rs 10 coin/note or two Rs 5 coins.', ['Different groups can have the same total value.', 'Add all values to check an amount.'], [
        { problem: 'Make Rs 20 using two equal notes.', steps: ['20 split into two equal amounts is 10 and 10.'], answer: 'Two Rs 10 notes.' }
      ]),
      makeMath1Section('4.4', 'Adding, Subtracting and Change', 'Add prices to find the cost of more than one item. If you pay more than the cost, subtract the cost from the amount paid to find the change.', ['Cost + change = amount paid.', 'Write the rupee amounts in the same place-value columns.'], [
        { problem: 'A toy costs Rs 30. You pay Rs 50. Find the change.', steps: ['50 − 30 = 20.'], answer: 'Rs 20' }
      ])
    ], [
      { id: 'ex1', title: 'Count the Money', problem: 'Find the total value of Rs 20, Rs 10 and Rs 5.', given: 'Rs 20, Rs 10 and Rs 5', method: 'Add each value.', steps: ['20 + 10 = 30.', '30 + 5 = 35.'], answer: 'Rs 35' },
      { id: 'ex2', title: 'Find the Change', problem: 'A book costs Rs 45. Ali pays Rs 100. How much change should he receive?', given: 'Paid Rs 100; cost Rs 45', method: 'Subtract the cost from the amount paid.', steps: ['100 − 45 = 55.'], answer: 'Rs 55' }
    ], [
      { exercise: '4.1', title: 'Exercise 4.1 — Money', problems: [
        makeMath1Problem('Q1', 'Add Rs 10 + Rs 20.', '10 + 20 = 30.', 'Rs 30'),
        makeMath1Problem('Q2', 'How can you make Rs 50 with five equal notes?', '50 divided into five equal values is 10 each.', 'Five Rs 10 notes'),
        makeMath1Problem('Q3', 'A ball costs Rs 25 and a kite costs Rs 30. Find the total.', '25 + 30 = 55.', 'Rs 55'),
        makeMath1Problem('Q4', 'A child pays Rs 100 for an item costing Rs 65. Find the change.', '100 − 65 = 35.', 'Rs 35')
      ] }
    ], {
      mcqs: [
        { q: 'Rs 10 + Rs 5 = ?', options: ['Rs 5', 'Rs 10', 'Rs 15', 'Rs 20'], correct: 2, exp: '10 + 5 = 15 rupees.' },
        { q: 'A pencil costs Rs 8. How much do 2 pencils cost?', options: ['Rs 10', 'Rs 16', 'Rs 18', 'Rs 20'], correct: 1, exp: '8 + 8 = 16 rupees.' },
        { q: 'You pay Rs 50 for an item costing Rs 35. Change is:', options: ['Rs 10', 'Rs 15', 'Rs 20', 'Rs 25'], correct: 1, exp: '50 − 35 = 15 rupees.' },
        { q: 'Which is the greatest amount?', options: ['Rs 5', 'Rs 20', 'Rs 10', 'Rs 15'], correct: 1, exp: 'Rs 20 is greater than Rs 5, Rs 10 and Rs 15.' }
      ],
      shortQuestions: [
        { q: 'What does Rs stand for?', sol: 'Rs stands for rupees.' },
        { q: 'Find the total: Rs 25 + Rs 10.', sol: '25 + 10 = Rs 35.' },
        { q: 'How do you find change?', sol: 'Subtract the cost from the amount paid.' }
      ],
      longQuestions: [
        { q: 'Sara buys a book for Rs 45 and a pencil for Rs 15. She pays Rs 100. Find the total cost and her change.', marks: 4, rubric: 'Add the prices, then subtract the cost from Rs 100.', sol: 'Total cost: 45 + 15 = Rs 60. Change: 100 − 60 = Rs 40.' },
        { q: 'Show two different ways to make Rs 30 using notes or coins.', marks: 3, rubric: 'Give two combinations whose values each total Rs 30.', sol: 'One way: Rs 20 + Rs 10 = Rs 30. Another way: Rs 10 + Rs 10 + Rs 10 = Rs 30.' }
      ]
    }, [{ name: 'Total cost', formula: 'Add the prices' }, { name: 'Change', formula: 'Amount paid − Cost = Change' }]),

  makeMath1Chapter(5, 'u5', 'Time', 'وقت', 'Pages 101–113',
    'Read clock faces and digital times, identify parts of a day, days of the week and months of the year.', [
      makeMath1Section('5.1', 'The Clock', 'A clock helps us tell time. The short hand shows the hour. The long hand shows minutes. When the long hand points to 12, we read the hour shown by the short hand.', ['Read the short hand for the hour.', 'The minute hand pointing to 12 means an exact hour.'], [
        { problem: 'The short hand points to 4 and the long hand to 12. What time is it?', steps: ['The minute hand shows an exact hour.', 'Read the short hand.'], answer: '4 o’clock' }
      ]),
      makeMath1Section('5.2', 'Digital and Analogue Time', 'An analogue clock has hands. A digital clock shows time using numbers. Read the hour and minutes displayed on a digital clock.', ['In 7:00, 7 is the hour and 00 shows the exact hour.', 'The hands and digital display can show the same time.'], [
        { problem: 'Write five o’clock as a digital time.', steps: ['Five o’clock has zero minutes past five.'], answer: '5:00' }
      ]),
      makeMath1Section('5.3', 'Parts of the Day', 'A day has morning, afternoon, evening and night. We do different activities at different times of the day.', ['Morning comes before afternoon.', 'Night follows evening.'], [
        { problem: 'When do most children eat breakfast: morning or night?', steps: ['Breakfast is usually eaten at the start of the day.'], answer: 'Morning' }
      ]),
      makeMath1Section('5.4', 'Days of the Week', 'There are seven days in a week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday. The days repeat in the same order.', ['Learn the order of all seven days.', 'After Sunday comes Monday.'], [
        { problem: 'What day comes after Tuesday?', steps: ['Say the days in order: Monday, Tuesday, Wednesday.'], answer: 'Wednesday' }
      ]),
      makeMath1Section('5.5', 'Months of the Year', 'A year has twelve months. The solar calendar months are January through December. The Islamic calendar months follow the lunar year.', ['There are twelve months in the solar year.', 'Use a calendar to check the order and spelling of months.'], [
        { problem: 'Which month comes after March?', steps: ['Read the months in order.'], answer: 'April' }
      ])
    ], [
      { id: 'ex1', title: 'Read the Clock', problem: 'The short hand points to 8 and the long hand points to 12. Give the analogue and digital time.', given: 'Hour hand: 8; minute hand: 12', method: 'The minute hand at 12 means an exact hour.', steps: ['Read the hour hand: 8.', 'Write zero minutes after the colon.'], answer: '8 o’clock; 8:00' },
      { id: 'ex2', title: 'Calendar Order', problem: 'What day comes after Friday and what month comes after June?', given: 'Friday; June', method: 'Use the repeating order of days and months.', steps: ['After Friday comes Saturday.', 'After June comes July.'], answer: 'Saturday; July' }
    ], [
      { exercise: '5.1', title: 'Exercise 5.1 — Time', problems: [
        makeMath1Problem('Q1', 'What time is shown when the short hand is at 2 and the long hand is at 12?', 'The long hand at 12 means an exact hour.', '2:00'),
        makeMath1Problem('Q2', 'What day comes before Sunday?', 'The day before Sunday is Saturday.', 'Saturday'),
        makeMath1Problem('Q3', 'What month comes after September?', 'Read the months in order.', 'October'),
        makeMath1Problem('Q4', 'Name one activity children may do in the morning.', 'Answers vary; for example, go to school.', 'Go to school (sample answer)')
      ] }
    ], {
      mcqs: [
        { q: 'Which hand shows the hour on an analogue clock?', options: ['Long hand', 'Short hand', 'Both hands are the same', 'No hand'], correct: 1, exp: 'The short hand shows the hour.' },
        { q: 'How many days are in a week?', options: ['5', '6', '7', '12'], correct: 2, exp: 'A week has seven days.' },
        { q: 'Which month comes after April?', options: ['March', 'May', 'June', 'August'], correct: 1, exp: 'May comes after April.' },
        { q: 'When the long hand is on 12, it is:', options: ['half past', 'an exact hour', 'a week', 'a month'], correct: 1, exp: 'The minute hand at 12 shows an exact hour.' }
      ],
      shortQuestions: [
        { q: 'Name the two main hands on an analogue clock.', sol: 'The short hour hand and the long minute hand.' },
        { q: 'What day comes before Monday?', sol: 'Sunday comes before Monday.' },
        { q: 'How many months are in a year?', sol: 'There are twelve months in a solar year.' }
      ],
      longQuestions: [
        { q: 'Write all seven days of the week in order.', marks: 3, rubric: 'Give all seven days in the correct sequence.', sol: 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.' },
        { q: 'Explain how to read an analogue clock showing an exact hour.', marks: 4, rubric: 'Identify the hour hand, minute hand and the meaning of the minute hand at 12.', sol: 'Look at the short hand to find the hour. Check that the long minute hand points to 12. When it points to 12, it is an exact hour, such as 6:00.' }
      ]
    }, [{ name: 'Clock', formula: 'Short hand = hour; long hand = minutes' }, { name: 'Calendar', formula: '7 days in a week · 12 months in a solar year' }]),

  makeMath1Chapter(6, 'u6', 'Geometry, Shapes and Position', 'جیومیٹری، اشکال اور جگہ', 'Pages 114–139',
    'Recognise 2-D shapes, continue patterns, describe positions and use position words from the geometry unit.', [
      makeMath1Section('6.1', 'Two-Dimensional Shapes', 'A flat shape has sides and corners. A circle is round and has no straight sides or corners. A triangle has 3 sides; a square has 4 equal sides; a rectangle has 4 sides.', ['Count sides and corners to identify a shape.', 'A square has four equal sides; a rectangle has two long and two short sides.'], [
        { problem: 'How many sides does a triangle have?', steps: ['Count the straight edges.'], answer: '3 sides' }
      ]),
      makeMath1Section('6.2', 'Circles, Triangles, Squares and Rectangles', 'Look for shapes in everyday objects. A clock face may be a circle; a book cover is often a rectangle. Shapes can have different sizes and colours.', ['The shape name stays the same when its size or colour changes.', 'Turn a shape and count its sides again if unsure.'], [
        { problem: 'Which shape has four equal sides?', steps: ['A square has four equal sides.'], answer: 'Square' }
      ]),
      makeMath1Section('6.3', 'Patterns', 'A pattern follows a rule. It may repeat shapes, colours or objects. Find the part that repeats, then continue the same order.', ['Look at more than one item to discover the repeating rule.', 'Keep the same order when continuing a pattern.'], [
        { problem: 'Complete: circle, square, circle, square, __.', steps: ['The pattern alternates circle, square.'], answer: 'circle' }
      ]),
      makeMath1Section('6.4', 'Inside and Outside; Above and Below', 'Position words tell where an object is. Inside means within a boundary; outside means beyond it. Above is higher than something; below is lower.', ['Say which object is used as the reference point.', 'Above and below describe vertical position.'], [
        { problem: 'A bird is in the sky above a tree. Where is the bird compared with the tree?', steps: ['The bird is higher than the tree.'], answer: 'Above the tree.' }
      ]),
      makeMath1Section('6.5', 'Over, Under, Near, Far, Before and After', 'Over and under describe positions across or below something. Near means close; far means at a greater distance. Before and after describe order or position in a sequence.', ['Use a clear reference object when describing position.', 'Near and far depend on what is being compared.'], [
        { problem: 'A cat is beneath a table. Which position word describes the cat?', steps: ['Beneath means under.'], answer: 'Under the table.' }
      ])
    ], [
      { id: 'ex1', title: 'Name the Shapes', problem: 'Name a shape with 3 sides, a shape with 4 equal sides and a round shape with no corners.', given: 'Count sides and corners.', method: 'Match each property to a familiar 2-D shape.', steps: ['A shape with 3 sides is a triangle.', 'A shape with 4 equal sides is a square.', 'A round shape with no corners is a circle.'], answer: 'Triangle, square, circle' },
      { id: 'ex2', title: 'Use Position Words', problem: 'A ball is below a chair and near a box. Describe the ball’s position.', given: 'Ball, chair and box', method: 'Use both position clues.', steps: ['Below means under.', 'Near means close to.'], answer: 'The ball is under the chair and close to the box.' }
    ], [
      { exercise: '6.1', title: 'Exercise 6.1 — Geometry, Shapes and Position', problems: [
        makeMath1Problem('Q1', 'How many corners does a square have?', 'A square has four corners.', '4'),
        makeMath1Problem('Q2', 'Name a shape with no corners.', 'A circle is round and has no corners.', 'Circle'),
        makeMath1Problem('Q3', 'Complete the pattern: triangle, circle, triangle, circle, __.', 'The pattern repeats triangle, circle.', 'triangle'),
        makeMath1Problem('Q4', 'If a book is on top of a desk, where is the book?', 'On top means above the desk.', 'Above the desk')
      ] }
    ], {
      mcqs: [
        { q: 'How many sides does a triangle have?', options: ['2', '3', '4', '5'], correct: 1, exp: 'A triangle has three sides.' },
        { q: 'Which shape has no corners?', options: ['Square', 'Triangle', 'Circle', 'Rectangle'], correct: 2, exp: 'A circle has no corners.' },
        { q: 'The opposite of inside is:', options: ['above', 'outside', 'near', 'before'], correct: 1, exp: 'Outside means beyond the boundary.' },
        { q: 'Complete: red, blue, red, blue, __.', options: ['green', 'blue', 'red', 'yellow'], correct: 2, exp: 'The pattern repeats red, blue, so the next colour is red.' }
      ],
      shortQuestions: [
        { q: 'How many sides and corners does a square have?', sol: 'A square has 4 sides and 4 corners.' },
        { q: 'What does near mean?', sol: 'Near means close to something.' },
        { q: 'How do you continue a repeating pattern?', sol: 'Find the part that repeats and draw or write it again in the same order.' }
      ],
      longQuestions: [
        { q: 'Describe a triangle, square and circle by their sides or corners.', marks: 4, rubric: 'Give accurate properties for all three shapes.', sol: 'A triangle has 3 sides and 3 corners. A square has 4 equal sides and 4 corners. A circle is round and has no straight sides or corners.' },
        { q: 'Explain these positions: inside a box, above a table, and under a chair.', marks: 3, rubric: 'Explain each word using its reference object.', sol: 'Inside a box means within the box boundary. Above a table means higher than the table. Under a chair means below the chair.' }
      ]
    }, [{ name: 'Triangle', formula: '3 sides · 3 corners' }, { name: 'Square', formula: '4 equal sides · 4 corners' }, { name: 'Circle', formula: 'Round · no corners' }])
];
