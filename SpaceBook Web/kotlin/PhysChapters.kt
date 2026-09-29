package com.example.selftuitionapp.data.science

data class ScienceChapter(
    val num: Int,
    val name: String,
    val pageRange: String,
    val status: String,
    val slos: List<String>,
    val topics: List<Topic>,
    val textbookExercise: TextbookExercise,
    val numericals: List<Numerical>,
    val formulas: List<Formula>,
    val definitions: List<Definition>,
    val activities: List<Activity>,
    val tables: List<Table>,
    val checklist: List<String>
)

data class Topic(val num: String, val title: String, val summary: String, val subtopics: List<Subtopic>)
data class Subtopic(val num: String, val name: String, val desc: String, val sciNote: String, val sq: String, val mcq: MCQ)
data class MCQ(val q: String, val opts: List<String>, val ans: Int)
data class TextbookExercise(val mcqs: List<ExerciseMCQ>, val sq: List<ExerciseSQ>, val lq: List<ExerciseLQ>)
data class ExerciseMCQ(val q: String, val opts: List<String>, val ans: Int, val exp: String)
data class ExerciseSQ(val q: String, val ans: String)
data class ExerciseLQ(val q: String, val ans: String)
data class Numerical(val num: String, val statement: String, val given: String, val formula: String, val solution: String, val answer: String)
data class Formula(val name: String, val formula: String)
data class Definition(val term: String, val def: String)
data class Activity(val num: String, val name: String, val procedure: String)
data class Table(val title: String, val rows: List<List<String>>)

val physChapters = listOf(
