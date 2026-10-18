"""Apply reviewed JPG transcriptions without touching unreviewed lessons or sources."""
from pathlib import Path
import json
from math12_reviewed_translations import TRANSLATIONS as MATH12_TRANSLATIONS, WORDS as MATH12_WORDS
from math12_reviewed_unit1 import PAGES, FIGURE_PDF_CROPS
from math12_reviewed_straight_line_intro import PAGES as STRAIGHT_PAGES, OBJECTIVES as STRAIGHT_OBJECTIVES, INTRO as STRAIGHT_INTRO, FIGURE_PDF_CROPS as STRAIGHT_CROPS
from math12_reviewed_distance_formula import PAGES as DISTANCE_PAGES, EXAMPLES as STRAIGHT_EXAMPLES
STRAIGHT_PAGES.extend(DISTANCE_PAGES)
from math12_reviewed_triangle_concurrency import PAGES as TRIANGLE_PAGES, EXAMPLES as TRIANGLE_EXAMPLES
STRAIGHT_PAGES.extend(TRIANGLE_PAGES)
STRAIGHT_EXAMPLES.extend(TRIANGLE_EXAMPLES)
from math12_reviewed_exercise71 import PAGES as EX71_PAGES, EXAMPLES as EX71_EXAMPLES, QUESTIONS as EX71_QUESTIONS, STEPS as EX71_STEPS, ANSWERS as EX71_ANSWERS
STRAIGHT_PAGES.extend(EX71_PAGES)
STRAIGHT_EXAMPLES.extend(EX71_EXAMPLES)
from math12_reviewed_slope import PAGES as SLOPE_PAGES, EXAMPLES as SLOPE_EXAMPLES
STRAIGHT_PAGES.extend(SLOPE_PAGES)
STRAIGHT_EXAMPLES.extend(SLOPE_EXAMPLES)
from math12_reviewed_line_forms import PAGES as LINE_FORM_PAGES, EXAMPLES as LINE_FORM_EXAMPLES
STRAIGHT_PAGES.extend(LINE_FORM_PAGES)
STRAIGHT_EXAMPLES.extend(LINE_FORM_EXAMPLES)
from math12_reviewed_intercept_symmetric import PAGES as SYMMETRIC_PAGES, EXAMPLES as SYMMETRIC_EXAMPLES
STRAIGHT_PAGES.extend(SYMMETRIC_PAGES)
STRAIGHT_EXAMPLES.extend(SYMMETRIC_EXAMPLES)
from math12_reviewed_general_line import PAGES as GENERAL_LINE_PAGES
STRAIGHT_PAGES.extend(GENERAL_LINE_PAGES)
from math12_reviewed_exercise72 import PAGES as EX72_PAGES, QUESTIONS as EX72_QUESTIONS, STEPS as EX72_STEPS, ANSWERS as EX72_ANSWERS, GRAPHS as EX72_GRAPHS, PROJECT as EX72_PROJECT, FIGURE_PDF_CROPS as EX72_CROPS
STRAIGHT_PAGES.extend(EX72_PAGES)
from math12_reviewed_line_position import PAGES as LINE_POSITION_PAGES, EXAMPLES as LINE_POSITION_EXAMPLES
STRAIGHT_PAGES.extend(LINE_POSITION_PAGES)
STRAIGHT_EXAMPLES.extend(LINE_POSITION_EXAMPLES)
from math12_reviewed_line_angles import PAGES as LINE_ANGLE_PAGES, EXAMPLES as LINE_ANGLE_EXAMPLES
STRAIGHT_PAGES.extend(LINE_ANGLE_PAGES)
STRAIGHT_EXAMPLES.extend(LINE_ANGLE_EXAMPLES)
from math12_reviewed_line_family import PAGES as LINE_FAMILY_PAGES, EXAMPLES as LINE_FAMILY_EXAMPLES
STRAIGHT_PAGES.extend(LINE_FAMILY_PAGES)
STRAIGHT_EXAMPLES.extend(LINE_FAMILY_EXAMPLES)
from math12_reviewed_exercise73 import PAGES as EX73_PAGES, QUESTIONS as EX73_QUESTIONS, STEPS as EX73_STEPS, ANSWERS as EX73_ANSWERS, HISTORY as EX73_HISTORY, FIGURE_PDF_CROPS as EX73_CROPS
STRAIGHT_PAGES.extend(EX73_PAGES)
from math12_reviewed_line_concurrency import PAGES as CONCURRENCY_PAGES, EXAMPLES as CONCURRENCY_EXAMPLES
STRAIGHT_PAGES.extend(CONCURRENCY_PAGES)
STRAIGHT_EXAMPLES.extend(CONCURRENCY_EXAMPLES)
from math12_reviewed_triangle_lines import PAGES as TRIANGLE_LINE_PAGES, EXAMPLES as TRIANGLE_LINE_EXAMPLES
STRAIGHT_PAGES.extend(TRIANGLE_LINE_PAGES)
STRAIGHT_EXAMPLES.extend(TRIANGLE_LINE_EXAMPLES)
from math12_reviewed_triangle_concurrency_proofs import PAGES as TRIANGLE_PROOF_PAGES, EXAMPLES as TRIANGLE_PROOF_EXAMPLES
STRAIGHT_PAGES.extend(TRIANGLE_PROOF_PAGES)
STRAIGHT_EXAMPLES.extend(TRIANGLE_PROOF_EXAMPLES)
from math12_reviewed_triangle_area import PAGES as TRIANGLE_AREA_PAGES, EXAMPLES as TRIANGLE_AREA_EXAMPLES
STRAIGHT_PAGES.extend(TRIANGLE_AREA_PAGES)
STRAIGHT_EXAMPLES.extend(TRIANGLE_AREA_EXAMPLES)
from math12_reviewed_homogeneous_lines import PAGES as HOMOGENEOUS_PAGES, EXAMPLES as HOMOGENEOUS_EXAMPLES, FIGURE_PDF_CROPS as HOMOGENEOUS_CROPS
STRAIGHT_PAGES.extend(HOMOGENEOUS_PAGES)
STRAIGHT_EXAMPLES.extend(HOMOGENEOUS_EXAMPLES)
from math12_reviewed_exercise74 import PAGES as EX74_PAGES, QUESTIONS as EX74_QUESTIONS, STEPS as EX74_STEPS, ANSWERS as EX74_ANSWERS
STRAIGHT_PAGES.extend(EX74_PAGES)
from math12_reviewed_unit7_close import PAGES as UNIT7_CLOSE_PAGES, REVIEW as UNIT7_REVIEW, FIGURE_PDF_CROPS as UNIT7_CLOSE_CROPS
STRAIGHT_PAGES.extend(UNIT7_CLOSE_PAGES)
from math12_reviewed_conics_intro import PAGES as CONIC_PAGES, OBJECTIVES as CONIC_OBJECTIVES, INTRO as CONIC_INTRO
from math12_reviewed_circle_general import PAGES as CIRCLE_GENERAL_PAGES, EXAMPLES as CONIC_EXAMPLES
CONIC_PAGES.extend(CIRCLE_GENERAL_PAGES)
from math12_reviewed_circle_tangent_cases import PAGES as CIRCLE_CASE_PAGES, EXAMPLES as CIRCLE_CASE_EXAMPLES
CONIC_PAGES.extend(CIRCLE_CASE_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_CASE_EXAMPLES)
from math12_reviewed_exercise81 import PAGES as EX81_PAGES, QUESTIONS as EX81_QUESTIONS, STEPS as EX81_STEPS, ANSWERS as EX81_ANSWERS
CONIC_PAGES.extend(EX81_PAGES)
from math12_reviewed_circle_intersections import PAGES as CIRCLE_INTERSECTION_PAGES, EXAMPLES as CIRCLE_INTERSECTION_EXAMPLES
CONIC_PAGES.extend(CIRCLE_INTERSECTION_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_INTERSECTION_EXAMPLES)
from math12_reviewed_circle_tangent_slope import PAGES as CIRCLE_SLOPE_PAGES, EXAMPLES as CIRCLE_SLOPE_EXAMPLES
CONIC_PAGES.extend(CIRCLE_SLOPE_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_SLOPE_EXAMPLES)
from math12_reviewed_circle_point_tangents import PAGES as CIRCLE_POINT_PAGES, EXAMPLES as CIRCLE_POINT_EXAMPLES
CONIC_PAGES.extend(CIRCLE_POINT_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_POINT_EXAMPLES)
from math12_reviewed_circle_external_tangents import PAGES as CIRCLE_EXTERNAL_PAGES, EXAMPLES as CIRCLE_EXTERNAL_EXAMPLES, FIGURE_PDF_CROPS as CIRCLE_HISTORY_CROPS
CONIC_PAGES.extend(CIRCLE_EXTERNAL_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_EXTERNAL_EXAMPLES)
from math12_reviewed_exercise82 import PAGES as EX82_PAGES, QUESTIONS as EX82_QUESTIONS, STEPS as EX82_STEPS, ANSWERS as EX82_ANSWERS
CONIC_PAGES.extend(EX82_PAGES)
from math12_reviewed_circle_chords import PAGES as CIRCLE_CHORD_PAGES, EXAMPLES as CIRCLE_CHORD_EXAMPLES
CONIC_PAGES.extend(CIRCLE_CHORD_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_CHORD_EXAMPLES)
from math12_reviewed_circle_angles import PAGES as CIRCLE_ANGLE_PAGES, EXAMPLES as CIRCLE_ANGLE_EXAMPLES
CONIC_PAGES.extend(CIRCLE_ANGLE_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_ANGLE_EXAMPLES)
from math12_reviewed_circle_radial_tangent import PAGES as CIRCLE_RADIAL_PAGES, EXAMPLES as CIRCLE_RADIAL_EXAMPLES
CONIC_PAGES.extend(CIRCLE_RADIAL_PAGES)
CONIC_EXAMPLES.extend(CIRCLE_RADIAL_EXAMPLES)
from math12_reviewed_unit8_close import PAGES as UNIT8_CLOSE_PAGES, QUESTIONS83 as EX83_QUESTIONS, STEPS83 as EX83_STEPS, ANSWERS83 as EX83_ANSWERS, REVIEW as UNIT8_REVIEW
CONIC_PAGES.extend(UNIT8_CLOSE_PAGES)
from math12_reviewed_conics2_intro import PAGES as CONICS2_PAGES, OBJECTIVES as CONICS2_OBJECTIVES, INTRO as CONICS2_INTRO
from math12_reviewed_parabola_standard import PAGES as PARABOLA_STANDARD_PAGES, EXAMPLES as CONICS2_EXAMPLES
CONICS2_PAGES.extend(PARABOLA_STANDARD_PAGES)
from math12_reviewed_parabola_tangency import PAGES as PARABOLA_TANGENCY_PAGES, EXAMPLES as PARABOLA_TANGENCY_EXAMPLES
CONICS2_PAGES.extend(PARABOLA_TANGENCY_PAGES)
CONICS2_EXAMPLES.extend(PARABOLA_TANGENCY_EXAMPLES)
from math12_reviewed_parabola_applications import PAGES as PARABOLA_APPLICATION_PAGES, EXAMPLES as PARABOLA_APPLICATION_EXAMPLES
CONICS2_PAGES.extend(PARABOLA_APPLICATION_PAGES)
CONICS2_EXAMPLES.extend(PARABOLA_APPLICATION_EXAMPLES)
from math12_reviewed_exercise91 import PAGES as EXERCISE91_PAGES, QUESTIONS as QUESTIONS91, STEPS as STEPS91, ANSWERS as ANSWERS91, question_graph as graph91, arch as arch91, answer_graphs as answer_graphs91
CONICS2_PAGES.extend(EXERCISE91_PAGES)
from math12_reviewed_ellipse_standard import PAGES as ELLIPSE_STANDARD_PAGES
CONICS2_PAGES.extend(ELLIPSE_STANDARD_PAGES)
from math12_reviewed_ellipse_elements import PAGES as ELLIPSE_ELEMENT_PAGES, EXAMPLES as ELLIPSE_ELEMENT_EXAMPLES
CONICS2_PAGES.extend(ELLIPSE_ELEMENT_PAGES)
CONICS2_EXAMPLES.extend(ELLIPSE_ELEMENT_EXAMPLES)
from math12_reviewed_ellipse_tangency import PAGES as ELLIPSE_TANGENCY_PAGES, EXAMPLES as ELLIPSE_TANGENCY_EXAMPLES
CONICS2_PAGES.extend(ELLIPSE_TANGENCY_PAGES)
CONICS2_EXAMPLES.extend(ELLIPSE_TANGENCY_EXAMPLES)
from math12_reviewed_exercise92 import PAGES as EXERCISE92_PAGES, QUESTIONS as QUESTIONS92, STEPS as STEPS92, ANSWERS as ANSWERS92, diagram as diagram92
CONICS2_PAGES.extend(EXERCISE92_PAGES)
from math12_reviewed_hyperbola_standard import PAGES as HYPERBOLA_STANDARD_PAGES, EXAMPLES as HYPERBOLA_STANDARD_EXAMPLES, FIGURE_PDF_CROPS as HYPERBOLA_BLURRED_CROPS
CONICS2_PAGES.extend(HYPERBOLA_STANDARD_PAGES)
CONICS2_EXAMPLES.extend(HYPERBOLA_STANDARD_EXAMPLES)
from math12_reviewed_hyperbola_translation import PAGES as HYPERBOLA_TRANSLATION_PAGES, EXAMPLES as HYPERBOLA_TRANSLATION_EXAMPLES
CONICS2_PAGES.extend(HYPERBOLA_TRANSLATION_PAGES)
CONICS2_EXAMPLES.extend(HYPERBOLA_TRANSLATION_EXAMPLES)
from math12_reviewed_hyperbola_tangency import PAGES as HYPERBOLA_TANGENCY_PAGES, EXAMPLES as HYPERBOLA_TANGENCY_EXAMPLES
CONICS2_PAGES.extend(HYPERBOLA_TANGENCY_PAGES)
CONICS2_EXAMPLES.extend(HYPERBOLA_TANGENCY_EXAMPLES)
from math12_reviewed_exercise93 import PAGES as EXERCISE93_PAGES, QUESTIONS as QUESTIONS93, STEPS as STEPS93, ANSWERS as ANSWERS93, source_graphs as source_graphs93, learning_graphs as learning_graphs93
CONICS2_PAGES.extend(EXERCISE93_PAGES)
from math12_reviewed_axes_transform import PAGES as AXES_TRANSFORM_PAGES, EXAMPLES as AXES_TRANSFORM_EXAMPLES
CONICS2_PAGES.extend(AXES_TRANSFORM_PAGES)
CONICS2_EXAMPLES.extend(AXES_TRANSFORM_EXAMPLES)
from math12_reviewed_exercise94 import PAGES as EXERCISE94_PAGES, EXAMPLES as EXERCISE94_EXAMPLES, QUESTIONS as QUESTIONS94, STEPS as STEPS94, ANSWERS as ANSWERS94
from math12_reviewed_unit9_close import PAGES as UNIT9_CLOSE_PAGES
CONICS2_PAGES.extend(EXERCISE94_PAGES+UNIT9_CLOSE_PAGES)
CONICS2_EXAMPLES.extend(EXERCISE94_EXAMPLES)
from math12_reviewed_differential_intro import PAGES as ODE_PAGES, EXAMPLES as ODE_EXAMPLES, OBJECTIVES as ODE_OBJECTIVES, INTRO as ODE_INTRO
from math12_reviewed_differential_formation import PAGES as ODE_FORMATION_PAGES, EXAMPLES as ODE_FORMATION_EXAMPLES, FORMATION as ODE_FORMATION
ODE_PAGES.extend(ODE_FORMATION_PAGES)
ODE_EXAMPLES.extend(ODE_FORMATION_EXAMPLES)
from math12_reviewed_exercise101 import PAGES as EX101_PAGES, QUESTIONS as EX101_QUESTIONS, STEPS as EX101_STEPS, ANSWERS as EX101_ANSWERS, FIGURE_PDF_CROPS as EX101_CROPS
ODE_PAGES.extend(EX101_PAGES)
from math12_reviewed_differential_separation import PAGES as ODE_SEPARATION_PAGES, EXAMPLES as ODE_SEPARATION_EXAMPLES
ODE_PAGES.extend(ODE_SEPARATION_PAGES)
ODE_EXAMPLES.extend(ODE_SEPARATION_EXAMPLES)
from math12_reviewed_differential_homogeneous import PAGES as ODE_HOMOGENEOUS_PAGES, EXAMPLES as ODE_HOMOGENEOUS_EXAMPLES, BACTERIAL_END, TRAJECTORY_INTRO
ODE_PAGES.extend(ODE_HOMOGENEOUS_PAGES)
ODE_EXAMPLES.extend(ODE_HOMOGENEOUS_EXAMPLES)
from math12_reviewed_differential_trajectories import PAGES as ODE_TRAJECTORY_PAGES, EXAMPLES as ODE_TRAJECTORY_EXAMPLES, FIGURE_PDF_CROPS as ODE_TRAJECTORY_CROPS
ODE_PAGES.extend(ODE_TRAJECTORY_PAGES)
ODE_EXAMPLES.extend(ODE_TRAJECTORY_EXAMPLES)
from math12_reviewed_exercise102 import PAGES as EX102_PAGES, QUESTIONS as EX102_QUESTIONS, STEPS as EX102_STEPS, ANSWERS as EX102_ANSWERS
ODE_PAGES.extend(EX102_PAGES)
from math12_reviewed_unit10_close import PAGES as UNIT10_CLOSE_PAGES, ITEMS as REVIEW10_ITEMS, SUMMARY as UNIT10_SUMMARY, HISTORY as UNIT10_HISTORY, FIGURE_PDF_CROPS as UNIT10_CLOSE_CROPS
ODE_PAGES.extend(UNIT10_CLOSE_PAGES)
from math12_reviewed_partial_intro import PAGES as PARTIAL_PAGES, EXAMPLES as PARTIAL_EXAMPLES, OBJECTIVES as PARTIAL_OBJECTIVES, INTRO as PARTIAL_INTRO
from math12_reviewed_partial_derivatives import PAGES as PARTIAL_DERIVATIVE_PAGES, EXAMPLES as PARTIAL_DERIVATIVE_EXAMPLES
PARTIAL_PAGES.extend(PARTIAL_DERIVATIVE_PAGES)
PARTIAL_EXAMPLES.extend(PARTIAL_DERIVATIVE_EXAMPLES)
from math12_reviewed_exercise111 import PAGES as EX111_PAGES, EXAMPLES as EX111_EXAMPLES, QUESTIONS as EX111_QUESTIONS, STEPS as EX111_STEPS, ANSWERS as EX111_ANSWERS, TEMPERATURE_END, HISTORY as PARTIAL_EULER_HISTORY, FIGURE_PDF_CROPS as EX111_CROPS
PARTIAL_PAGES.extend(EX111_PAGES)
PARTIAL_EXAMPLES.extend(EX111_EXAMPLES)
from math12_reviewed_euler_theorem import PAGES as EULER_PAGES, EXAMPLES as EULER_EXAMPLES
PARTIAL_PAGES.extend(EULER_PAGES)
PARTIAL_EXAMPLES.extend(EULER_EXAMPLES)
from math12_reviewed_exercise112 import PAGES as EX112_PAGES, EXAMPLES as EX112_EXAMPLES, QUESTIONS as EX112_QUESTIONS, STEPS as EX112_STEPS, ANSWERS as EX112_ANSWERS, MAPLE as PARTIAL_MAPLE
PARTIAL_PAGES.extend(EX112_PAGES)
PARTIAL_EXAMPLES.extend(EX112_EXAMPLES)
from math12_reviewed_unit11_close import PAGES as UNIT11_CLOSE_PAGES, ITEMS as REVIEW11_ITEMS, SUMMARY as UNIT11_SUMMARY, HISTORY as UNIT11_HISTORY, FIGURE_PDF_CROPS as UNIT11_CLOSE_CROPS
PARTIAL_PAGES.extend(UNIT11_CLOSE_PAGES)
from math12_reviewed_numerical_intro import PAGES as NUMERICAL_PAGES, OBJECTIVES as NUMERICAL_OBJECTIVES, INTRO as NUMERICAL_INTRO
from math12_reviewed_numerical_bisection import PAGES as BISECTION_PAGES, EXAMPLES as NUMERICAL_EXAMPLES
NUMERICAL_PAGES.extend(BISECTION_PAGES)
from math12_reviewed_numerical_iterations import PAGES as NUMERICAL_ITERATION_PAGES, EXAMPLES as NUMERICAL_ITERATION_EXAMPLES
NUMERICAL_PAGES.extend(NUMERICAL_ITERATION_PAGES)
NUMERICAL_EXAMPLES.extend(NUMERICAL_ITERATION_EXAMPLES)
from math12_reviewed_numerical_newton import PAGES as NUMERICAL_NEWTON_PAGES, EXAMPLES as NUMERICAL_NEWTON_EXAMPLES
NUMERICAL_PAGES.extend(NUMERICAL_NEWTON_PAGES)
NUMERICAL_EXAMPLES.extend(NUMERICAL_NEWTON_EXAMPLES)
from math12_reviewed_exercise121 import PAGES as EX121_PAGES, QUESTIONS as EX121_QUESTIONS, STEPS as EX121_STEPS, ANSWERS as EX121_ANSWERS, HISTORY as NUMERICAL_QUSTA_HISTORY, FIGURE_PDF_CROPS as EX121_CROPS
NUMERICAL_PAGES.extend(EX121_PAGES)
from math12_reviewed_numerical_quadrature import PAGES as QUADRATURE_PAGES
NUMERICAL_PAGES.extend(QUADRATURE_PAGES)
from math12_reviewed_numerical_simpson import PAGES as SIMPSON_PAGES, EXAMPLES as SIMPSON_EXAMPLES
NUMERICAL_PAGES.extend(SIMPSON_PAGES)
NUMERICAL_EXAMPLES.extend(SIMPSON_EXAMPLES)
from math12_reviewed_numerical_maple_integral import PAGES as NUMERICAL_MAPLE_PAGES, EXAMPLES as NUMERICAL_MAPLE_EXAMPLES, FIGURE_PDF_CROPS as NUMERICAL_MAPLE_CROPS
NUMERICAL_PAGES.extend(NUMERICAL_MAPLE_PAGES)
NUMERICAL_EXAMPLES.extend(NUMERICAL_MAPLE_EXAMPLES)
from math12_reviewed_exercise122 import PAGES as EX122_PAGES, QUESTIONS as EX122_QUESTIONS, STEPS as EX122_STEPS, ANSWERS as EX122_ANSWERS, SOLUTION_GRAPHS as EX122_GRAPHS, FIGURE_PDF_CROPS as EX122_CROPS
NUMERICAL_PAGES.extend(EX122_PAGES)
from math12_reviewed_unit12_close import PAGES as UNIT12_CLOSE_PAGES, ITEMS as REVIEW12_ITEMS, SUMMARY as UNIT12_SUMMARY, HISTORY as UNIT12_HISTORY, PROJECT_QUESTIONS as PROJECT12_QUESTIONS, PROJECT_STEPS as PROJECT12_STEPS, PROJECT_ANSWERS as PROJECT12_ANSWERS, project_graph as PROJECT12_GRAPH, FIGURE_PDF_CROPS as UNIT12_CLOSE_CROPS
NUMERICAL_PAGES.extend(UNIT12_CLOSE_PAGES)
from math12_reviewed_answers326 import PAGES as ANSWER_PAGES
from math12_reviewed_answers327 import PAGES as ANSWER327_PAGES, EX21 as ANSWER327_EX21, EX22 as ANSWER327_EX22
ANSWER_PAGES.extend(ANSWER327_PAGES)
from math12_reviewed_answers328 import PAGES as ANSWER328_PAGES, BLOCKS as ANSWER328_BLOCKS
ANSWER_PAGES.extend(ANSWER328_PAGES)
from math12_reviewed_answers329_330 import PAGES as ANSWER329_PAGES, BLOCKS329, BLOCKS330
ANSWER_PAGES.extend(ANSWER329_PAGES)
from math12_reviewed_answers331 import PAGES as ANSWER331_PAGES, EX23 as ANSWER331_EX23, EX24 as ANSWER331_EX24, REVIEW as ANSWER331_REVIEW
ANSWER_PAGES.extend(ANSWER331_PAGES)
from math12_reviewed_answers332 import PAGES as ANSWER332_PAGES, EX31 as ANSWER332_EX31, EX32 as ANSWER332_EX32
ANSWER_PAGES.extend(ANSWER332_PAGES)
from math12_reviewed_answers333 import PAGES as ANSWER333_PAGES, EX33 as ANSWER333_EX33, EX34 as ANSWER333_EX34
ANSWER_PAGES.extend(ANSWER333_PAGES)
from math12_reviewed_answers334 import PAGES as ANSWER334_PAGES, EX34 as ANSWER334_EX34, EX35 as ANSWER334_EX35, REVIEW3 as ANSWER334_REVIEW3, EX41 as ANSWER334_EX41
ANSWER_PAGES.extend(ANSWER334_PAGES)
from math12_reviewed_answers335 import PAGES as ANSWER335_PAGES, EX41 as ANSWER335_EX41, EX42 as ANSWER335_EX42, EX43 as ANSWER335_EX43
ANSWER_PAGES.extend(ANSWER335_PAGES)
from math12_reviewed_answers336 import PAGES as ANSWER336_PAGES, EX43 as ANSWER336_EX43, REVIEW4 as ANSWER336_REVIEW4, EX51 as ANSWER336_EX51
ANSWER_PAGES.extend(ANSWER336_PAGES)
from math12_reviewed_answers337 import PAGES as ANSWER337_PAGES, EX51 as ANSWER337_EX51, EX52 as ANSWER337_EX52, REVIEW5 as ANSWER337_REVIEW5, EX61 as ANSWER337_EX61
ANSWER_PAGES.extend(ANSWER337_PAGES)
from math12_reviewed_answers338 import PAGES as ANSWER338_PAGES, EX61 as ANSWER338_EX61, EX62 as ANSWER338_EX62, EX63 as ANSWER338_EX63
ANSWER_PAGES.extend(ANSWER338_PAGES)
from math12_reviewed_answers339 import PAGES as ANSWER339_PAGES, EX63 as ANSWER339_EX63, EX64 as ANSWER339_EX64, REVIEW6 as ANSWER339_REVIEW6, EX71 as ANSWER339_EX71, EX72 as ANSWER339_EX72
ANSWER_PAGES.extend(ANSWER339_PAGES)
from math12_reviewed_answers340 import PAGES as ANSWER340_PAGES, EX72 as ANSWER340_EX72, EX73 as ANSWER340_EX73, EX74 as ANSWER340_EX74, REVIEW7 as ANSWER340_REVIEW7, EX81 as ANSWER340_EX81
ANSWER_PAGES.extend(ANSWER340_PAGES)
from math12_reviewed_answers341 import PAGES as ANSWER341_PAGES, EX81 as ANSWER341_EX81, EX82 as ANSWER341_EX82, REVIEW8 as ANSWER341_REVIEW8, EX91 as ANSWER341_EX91
ANSWER_PAGES.extend(ANSWER341_PAGES)
from math12_reviewed_answers342 import PAGES as ANSWER342_PAGES, EX91 as ANSWER342_EX91, EX92 as ANSWER342_EX92
ANSWER_PAGES.extend(ANSWER342_PAGES)
from math12_reviewed_answers343 import PAGES as ANSWER343_PAGES, EX92 as ANSWER343_EX92, EX93 as ANSWER343_EX93
ANSWER_PAGES.extend(ANSWER343_PAGES)
from math12_reviewed_answers344 import PAGES as ANSWER344_PAGES, EX93 as ANSWER344_EX93
ANSWER_PAGES.extend(ANSWER344_PAGES)
from math12_reviewed_answers345 import PAGES as ANSWER345_PAGES, EX94 as ANSWER345_EX94, EX101 as ANSWER345_EX101, EX102 as ANSWER345_EX102
ANSWER_PAGES.extend(ANSWER345_PAGES)
from math12_reviewed_answers346 import PAGES as ANSWER346_PAGES, EX102 as ANSWER346_EX102, REVIEW10 as ANSWER346_REVIEW10, EX111 as ANSWER346_EX111, EX112 as ANSWER346_EX112, REVIEW11 as ANSWER346_REVIEW11
ANSWER_PAGES.extend(ANSWER346_PAGES)
from math12_reviewed_answers347 import PAGES as ANSWER347_PAGES, EX121 as ANSWER347_EX121, EX122 as ANSWER347_EX122, REVIEW12 as ANSWER347_REVIEW12
ANSWER_PAGES.extend(ANSWER347_PAGES)
from math12_reviewed_backmatter import PAGES as BACKMATTER_PAGES, AUTHORS as BOOK_AUTHORS, FEEDBACK as BOOK_FEEDBACK, QUOTES as BOOK_QUOTES, BACK_FULL as BOOK_BACK_COVER, FIGURE_PDF_CROPS as BACKMATTER_CROPS, write_rotated_assets
from math12_reviewed_graphics import PAGES as GRAPHICS_PAGES, FIGURE_PDF_CROPS as GRAPHICS_CROPS
from pypdf import PdfReader
from math12_reviewed_matrices import PAGES as MATRIX_PAGES
from math12_reviewed_functions import PAGES as FUNCTION_PAGES, FIGURE_PDF_CROPS as FUNCTION_CROPS
from math12_reviewed_modulus import PAGES as MODULUS_PAGES
FUNCTION_PAGES.extend(MODULUS_PAGES)
from math12_reviewed_composition import PAGES as COMPOSITION_PAGES
FUNCTION_PAGES.extend(COMPOSITION_PAGES)
from math12_reviewed_exercise21 import PAGES as EX21_PAGES, FIGURE_PDF_CROPS as EX21_CROPS, QUESTIONS as EX21_QUESTIONS, GRAPHS as EX21_GRAPHS, PROJECT as EX21_PROJECT, STEPS as EX21_STEPS, ANSWERS as EX21_ANSWERS
FUNCTION_PAGES.extend(EX21_PAGES)
from math12_reviewed_transcendental import PAGES as TRANSCENDENTAL_PAGES
FUNCTION_PAGES.extend(TRANSCENDENTAL_PAGES)
from math12_reviewed_exponential import PAGES as EXPONENTIAL_PAGES
FUNCTION_PAGES.extend(EXPONENTIAL_PAGES)
from math12_reviewed_logarithms import PAGES as LOGARITHM_PAGES
FUNCTION_PAGES.extend(LOGARITHM_PAGES)
from math12_reviewed_log_rules import PAGES as LOG_RULE_PAGES
FUNCTION_PAGES.extend(LOG_RULE_PAGES)
from math12_reviewed_hyperbolic import PAGES as HYPERBOLIC_PAGES, FIGURE_PDF_CROPS as HYPERBOLIC_CROPS
FUNCTION_PAGES.extend(HYPERBOLIC_PAGES)
from math12_reviewed_parametric import PAGES as PARAMETRIC_PAGES
FUNCTION_PAGES.extend(PARAMETRIC_PAGES)
from math12_reviewed_exponential_graphs import PAGES as EXP_GRAPH_PAGES
FUNCTION_PAGES.extend(EXP_GRAPH_PAGES)
from math12_reviewed_log_graphs import PAGES as LOG_GRAPH_PAGES
FUNCTION_PAGES.extend(LOG_GRAPH_PAGES)
from math12_reviewed_conic_graphs import PAGES as CONIC_GRAPH_PAGES
FUNCTION_PAGES.extend(CONIC_GRAPH_PAGES)
from math12_reviewed_compound import PAGES as COMPOUND_PAGES
FUNCTION_PAGES.extend(COMPOUND_PAGES)
from math12_reviewed_maple_plots import PAGES as MAPLE_PLOT_PAGES
FUNCTION_PAGES.extend(MAPLE_PLOT_PAGES)
from math12_reviewed_maple_implicit import PAGES as MAPLE_IMPLICIT_PAGES
FUNCTION_PAGES.extend(MAPLE_IMPLICIT_PAGES)
from math12_reviewed_exercise22 import PAGES as EX22_PAGES, QUESTIONS as EX22_QUESTIONS, STEPS as EX22_STEPS, ANSWERS as EX22_ANSWERS, SOLUTION_BLOCKS as EX22_SOLUTION_BLOCKS, CLARIFICATIONS as EX22_CLARIFICATIONS
FUNCTION_PAGES.extend(EX22_PAGES)
from math12_reviewed_intervals import PAGES as INTERVAL_PAGES
FUNCTION_PAGES.extend(INTERVAL_PAGES)
from math12_reviewed_sequences import PAGES as SEQUENCE_PAGES
FUNCTION_PAGES.extend(SEQUENCE_PAGES)
from math12_reviewed_sequence_limits import PAGES as SEQUENCE_LIMIT_PAGES, EXAMPLES as SEQUENCE_LIMIT_EXAMPLES
FUNCTION_PAGES.extend(SEQUENCE_LIMIT_PAGES)
from math12_reviewed_function_limit_rules import PAGES as FUNCTION_LIMIT_RULE_PAGES, EXAMPLES as FUNCTION_LIMIT_RULE_EXAMPLES
FUNCTION_PAGES.extend(FUNCTION_LIMIT_RULE_PAGES)
SEQUENCE_LIMIT_EXAMPLES.extend(FUNCTION_LIMIT_RULE_EXAMPLES)
from math12_reviewed_important_limits import PAGES as IMPORTANT_LIMIT_PAGES
FUNCTION_PAGES.extend(IMPORTANT_LIMIT_PAGES)
from math12_reviewed_limit_proofs import PAGES as LIMIT_PROOF_PAGES
FUNCTION_PAGES.extend(LIMIT_PROOF_PAGES)
from math12_reviewed_sine_limit import PAGES as SINE_LIMIT_PAGES, EXAMPLES as SINE_LIMIT_EXAMPLES
FUNCTION_PAGES.extend(SINE_LIMIT_PAGES)
SEQUENCE_LIMIT_EXAMPLES.extend(SINE_LIMIT_EXAMPLES)
from math12_reviewed_maple_limits import PAGES as MAPLE_LIMIT_PAGES, EXAMPLES as MAPLE_LIMIT_EXAMPLES
FUNCTION_PAGES.extend(MAPLE_LIMIT_PAGES)
SEQUENCE_LIMIT_EXAMPLES.extend(MAPLE_LIMIT_EXAMPLES)
from math12_reviewed_exercise23 import PAGES as EX23_PAGES, QUESTIONS as EX23_QUESTIONS, STEPS as EX23_STEPS, ANSWERS as EX23_ANSWERS, PROJECT as EX23_PROJECT, FIGURE_PDF_CROPS as EX23_CROPS, CLARIFICATIONS as EX23_CLARIFICATIONS
FUNCTION_PAGES.extend(EX23_PAGES)
from math12_reviewed_continuity import PAGES as CONTINUITY_PAGES, EXAMPLES as CONTINUITY_EXAMPLES, FIGURE_PDF_CROPS as CONTINUITY_CROPS
from math12_reviewed_exercise24 import PAGES as EX24_PAGES, QUESTIONS as EX24_QUESTIONS, STEPS as EX24_STEPS, ANSWERS as EX24_ANSWERS, BLOCKS as EX24_BLOCKS, SOLUTIONS as EX24_SOLUTIONS, CLARIFICATIONS as EX24_CLARIFICATIONS
FUNCTION_PAGES.extend(CONTINUITY_PAGES)
FUNCTION_PAGES.extend(EX24_PAGES)
from math12_reviewed_review2 import PAGES as REVIEW2_PAGES, QUESTIONS as REVIEW2_QUESTIONS, BLOCKS as REVIEW2_BLOCKS, NUMS as REVIEW2_NUMS, STEPS as REVIEW2_STEPS, LETTERS as REVIEW2_LETTERS, CLARIFICATIONS as REVIEW2_CLARIFICATIONS
FUNCTION_PAGES.extend(REVIEW2_PAGES)
from math12_reviewed_summary2 import PAGES as SUMMARY2_PAGES, FIGURE_PDF_CROPS as SUMMARY2_CROPS
FUNCTION_PAGES.extend(SUMMARY2_PAGES)
from math12_reviewed_exercise31 import PAGES as EX31_PAGES, QUESTIONS as EX31_QUESTIONS, STEPS as EX31_STEPS, ANSWERS as EX31_ANSWERS, SOLUTIONS as EX31_SOLUTIONS, FIGURE_PDF_CROPS as EX31_CROPS
from math12_reviewed_vector_functions import PAGES as VECTOR_PAGES, EXAMPLES as VECTOR_EXAMPLES, FIGURE_PDF_CROPS as VECTOR_CROPS
from math12_reviewed_exercise51 import PAGES as EX51_PAGES, QUESTIONS as EX51_QUESTIONS, STEPS as EX51_STEPS, ANSWERS as EX51_ANSWERS
VECTOR_PAGES.extend(EX51_PAGES)
from math12_reviewed_vector_derivative import PAGES as VECTOR_DERIVATIVE_PAGES, EXAMPLES as VECTOR_DERIVATIVE_EXAMPLES
VECTOR_PAGES.extend(VECTOR_DERIVATIVE_PAGES)
from math12_reviewed_vector_proofs import PAGES as VECTOR_PROOF_PAGES
VECTOR_PAGES.extend(VECTOR_PROOF_PAGES)
from math12_reviewed_vector_motion import PAGES as VECTOR_MOTION_PAGES, EXAMPLES as VECTOR_MOTION_EXAMPLES
VECTOR_PAGES.extend(VECTOR_MOTION_PAGES)
VECTOR_EXAMPLES.extend(VECTOR_MOTION_EXAMPLES)
from math12_reviewed_exercise52 import PAGES as EX52_PAGES, QUESTIONS as EX52_QUESTIONS, STEPS as EX52_STEPS, ANSWERS as EX52_ANSWERS, EXAMPLE as VECTOR_EXAMPLE13
VECTOR_PAGES.extend(EX52_PAGES)
VECTOR_EXAMPLES.append(VECTOR_EXAMPLE13)
from math12_reviewed_unit5_close import PAGES as UNIT5_CLOSE_PAGES, REVIEW as REVIEW5_ITEMS, FIGURE_PDF_CROPS as UNIT5_CLOSE_CROPS, PROJECT as VECTOR_PROJECT
VECTOR_PAGES.extend(UNIT5_CLOSE_PAGES)
VECTOR_EXAMPLES.extend(VECTOR_DERIVATIVE_EXAMPLES)
from math12_reviewed_integration_parts import PAGES as INTEGRATION_PAGES, EXAMPLES as INTEGRATION_EXAMPLES
from math12_reviewed_radical_parts import PAGES as RADICAL_PARTS_PAGES, EXAMPLES as RADICAL_PARTS_EXAMPLES
INTEGRATION_PAGES.extend(RADICAL_PARTS_PAGES)
INTEGRATION_EXAMPLES.extend(RADICAL_PARTS_EXAMPLES)
from math12_reviewed_exercise62 import PAGES as EX62_PAGES, QUESTIONS as EX62_QUESTIONS, STEPS as EX62_STEPS, ANSWERS as EX62_ANSWERS, FIGURE_PDF_CROPS as EX62_CROPS
INTEGRATION_PAGES.extend(EX62_PAGES)
from math12_reviewed_partial_fractions import PAGES as PARTIAL_FRACTION_PAGES, EXAMPLES as PARTIAL_FRACTION_EXAMPLES
INTEGRATION_PAGES.extend(PARTIAL_FRACTION_PAGES)
INTEGRATION_EXAMPLES.extend(PARTIAL_FRACTION_EXAMPLES)
from math12_reviewed_definite_integrals import PAGES as DEFINITE_PAGES, EXAMPLES as DEFINITE_EXAMPLES, FIGURE_PDF_CROPS as DEFINITE_CROPS
INTEGRATION_PAGES.extend(DEFINITE_PAGES)
INTEGRATION_EXAMPLES.extend(DEFINITE_EXAMPLES)
from math12_reviewed_integral_properties import PAGES as INTEGRAL_PROPERTY_PAGES, CHALLENGES as INTEGRAL_CHALLENGES
INTEGRATION_PAGES.extend(INTEGRAL_PROPERTY_PAGES)
from math12_reviewed_definite_examples import PAGES as DEFINITE_EXAMPLE_PAGES, EXAMPLES as DEFINITE_MORE_EXAMPLES
INTEGRATION_PAGES.extend(DEFINITE_EXAMPLE_PAGES)
INTEGRATION_EXAMPLES.extend(DEFINITE_MORE_EXAMPLES)
from math12_reviewed_integral_area import PAGES as INTEGRAL_AREA_PAGES, EXAMPLES as INTEGRAL_AREA_EXAMPLES
INTEGRATION_PAGES.extend(INTEGRAL_AREA_PAGES)
INTEGRATION_EXAMPLES.extend(INTEGRAL_AREA_EXAMPLES)
from math12_reviewed_exercise64 import PAGES as EX64_PAGES, QUESTIONS as EX64_QUESTIONS, STEPS as EX64_STEPS, ANSWERS as EX64_ANSWERS, GRAPHS as EX64_GRAPHS, FIGURE_PDF_CROPS as EX64_CROPS
INTEGRATION_PAGES.extend(EX64_PAGES)
from math12_reviewed_unit6_close import PAGES as UNIT6_CLOSE_PAGES, REVIEW as REVIEW6_ITEMS
INTEGRATION_PAGES.extend(UNIT6_CLOSE_PAGES)
from math12_reviewed_exercise63 import QUESTIONS as EX63_QUESTIONS, STEPS as EX63_STEPS, ANSWERS as EX63_ANSWERS
from math12_reviewed_higher_derivatives import PAGES as HIGHER_PAGES, EXAMPLES as HIGHER_EXAMPLES
from math12_reviewed_implicit_second import PAGES as IMPLICIT_SECOND_PAGES, EXAMPLES as IMPLICIT_SECOND_EXAMPLES
HIGHER_PAGES.extend(IMPLICIT_SECOND_PAGES)
HIGHER_EXAMPLES.extend(IMPLICIT_SECOND_EXAMPLES)
from math12_reviewed_exercise41 import PAGES as EX41_PAGES, QUESTIONS as EX41_QUESTIONS, STEPS as EX41_STEPS, ANSWERS as EX41_ANSWERS, CLARIFICATIONS as EX41_CLARIFICATIONS, PROJECTS as EX41_PROJECTS
HIGHER_PAGES.extend(EX41_PAGES)
from math12_reviewed_taylor import PAGES as TAYLOR_PAGES, EXAMPLES as TAYLOR_EXAMPLES, CHALLENGE as TAYLOR_CHALLENGE
HIGHER_PAGES.extend(TAYLOR_PAGES)
HIGHER_EXAMPLES.extend(TAYLOR_EXAMPLES)
from math12_reviewed_tangents import PAGES as TANGENT_PAGES, EXAMPLES as TANGENT_EXAMPLES
HIGHER_PAGES.extend(TANGENT_PAGES)
HIGHER_EXAMPLES.extend(TANGENT_EXAMPLES)
from math12_reviewed_exercise42 import PAGES as EX42_PAGES, QUESTIONS as EX42_QUESTIONS, STEPS as EX42_STEPS, ANSWERS as EX42_ANSWERS, CLARIFICATIONS as EX42_CLARIFICATIONS, FIGURE_PDF_CROPS as EX42_CROPS
HIGHER_PAGES.extend(EX42_PAGES)
from math12_reviewed_extrema import PAGES as EXTREMA_PAGES, EXAMPLES as EXTREMA_EXAMPLES
HIGHER_PAGES.extend(EXTREMA_PAGES)
HIGHER_EXAMPLES.extend(EXTREMA_EXAMPLES)
from math12_reviewed_second_test import PAGES as SECOND_TEST_PAGES, EXAMPLES as SECOND_TEST_EXAMPLES
HIGHER_PAGES.extend(SECOND_TEST_PAGES)
HIGHER_EXAMPLES.extend(SECOND_TEST_EXAMPLES)
from math12_reviewed_exercise43 import PAGES as EX43_PAGES, QUESTIONS as EX43_QUESTIONS, STEPS as EX43_STEPS, ANSWERS as EX43_ANSWERS, CLARIFICATIONS as EX43_CLARIFICATIONS, GRAPHS as EX43_GRAPHS
HIGHER_PAGES.extend(EX43_PAGES)
from math12_reviewed_unit4_close import PAGES as UNIT4_CLOSE_PAGES, REVIEW as REVIEW4_ITEMS, FIGURE_PDF_CROPS as UNIT4_CLOSE_CROPS
HIGHER_PAGES.extend(UNIT4_CLOSE_PAGES)
from math12_reviewed_differentiation import PAGES as DIFFERENTIATION_PAGES, FIGURE_PDF_CROPS as DIFFERENTIATION_CROPS, EXAMPLES as DIFFERENTIATION_EXAMPLES
from math12_reviewed_trigonometry import PAGES as TRIG_PAGES, FIGURE_PDF_CROPS as TRIG_CROPS, EXAMPLES as TRIG_EXAMPLES
DIFFERENTIATION_PAGES.extend(TRIG_PAGES)
DIFFERENTIATION_CROPS.extend(TRIG_CROPS)
DIFFERENTIATION_EXAMPLES.extend(TRIG_EXAMPLES)
from math12_reviewed_exponential_derivatives import PAGES as EXP_PAGES, EXAMPLES as EXP_EXAMPLES
DIFFERENTIATION_PAGES.extend(EXP_PAGES)
DIFFERENTIATION_EXAMPLES.extend(EXP_EXAMPLES)
from math12_reviewed_hyperbolic_derivatives import PAGES as HYP_DIFF_PAGES, EXAMPLES as HYP_DIFF_EXAMPLES
DIFFERENTIATION_PAGES.extend(HYP_DIFF_PAGES)
DIFFERENTIATION_EXAMPLES.extend(HYP_DIFF_EXAMPLES)
from math12_reviewed_unit3_close import PAGES as UNIT3_CLOSE_PAGES, EXAMPLES as UNIT3_CLOSE_EXAMPLES, FIGURE_PDF_CROPS as UNIT3_CLOSE_CROPS, REVIEW as REVIEW3_ITEMS, PROJECT as BALLOON_PROJECT
DIFFERENTIATION_PAGES.extend(UNIT3_CLOSE_PAGES)
DIFFERENTIATION_EXAMPLES.extend(UNIT3_CLOSE_EXAMPLES)
DIFFERENTIATION_CROPS.extend(UNIT3_CLOSE_CROPS)
from math12_reviewed_exercise32 import PAGES as EX32_PAGES, QUESTIONS as EX32_QUESTIONS, FIGURE_PDF_CROPS as EX32_CROPS, STEPS as EX32_STEPS, ANSWERS as EX32_ANSWERS, PROJECT as EX32_PROJECT
DIFFERENTIATION_PAGES.extend(EX32_PAGES)
DIFFERENTIATION_PAGES.extend(EX31_PAGES)
DIFFERENTIATION_PAGES.sort(key=lambda page:page["page"])
SEQUENCE_LIMIT_EXAMPLES.extend(CONTINUITY_EXAMPLES)
for function_page in FUNCTION_PAGES:
    function_page['title']='FUNCTIONS AND LIMITS'

ROOT = Path(__file__).resolve().parents[1]
pages = [
    {"file": "001_page_1.jpg", "page": "cover", "title": "A Textbook of Mathematics", "paragraphs": ["For Grade XII", "Free From Government", "NOT FOR SALE", "Khyber Pakhtunkhwa Textbook Board, Peshawar."], "visualStatus": "decorative artwork retained in source; no instructional diagram"},
    {"file": "003_page_1.jpg", "page": "opening quotation", "title": "THE SEEKING OF KNOWLEDGE IS OBLIGATORY FOR EVERY MUSLIM", "paragraphs": ["(AL-TIRMIDHI # 74)", "Stop Corruption", "Save the Nation."], "visualStatus": "decorative floral borders"},
    {"file": "003_page_2.jpg", "page": "i", "title": "A Textbook of Mathematics", "paragraphs": ["For Grade XII", "Khyber Pakhtunkhwa Textbook Board, Peshawar."], "visualStatus": "title-page geometry illustrations pending digital reconstruction"},
    {"file": "004_page_1.jpg", "page": "ii", "title": "All rights reserved with the Leading Books Publishers, Peshawar", "paragraphs": [
        "Approved by:", "Developed according to the National Curriculum 2006 and approved by Directorate of Curriculum & Teachers Education (DCTE), Khyber Pakhtunkhwa, Abbottabad. vide NOC No. 2958-59/G-04/CTR/Maths-XII_LBP dated: 31-05-2021.",
        "Authors:", "Mumtaz Khan", "Waqas Ahmed", "Review Supervision:", "Gohar Ali Khan, Director, Curriculum and Teachers Education, Abbottabad, Khyber Pakhtunkhwa.",
        "Focal Person:", "Zulfiqar Khan, Additional Director, Curriculum and Textbook Review, DCTE, Abbottabad.", "Re-reviewers:",
        "Nadeem Sultan, Principal, GHS Pawa, Abbottabad", "Majid Khan, Assistant Professor, GPGC Mandian, Abbottabad", "Muhammad Nasim, Subject Specialist, GHSS Muslim Abad, Abbottabad", "Abbas Khan, Desk Officer, DCTE, Abbottabad Khyber Pakhtunkhwa", "Shakeel Iqbal, Ex-Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "Editor:", "Nasir Kamal, Desk Officer Khyber Pakhtunkhwa Textbook Board, Peshawar", "Printing Supervision:", "Arshad Khan Afridi, Chairman", "Abdul Wali Khan, Member (E&P)", "Khyber Pakhtunkhwa Textbook Board, Peshawar", "Printed for Academic Year: 2022-2023", "Website: www.kptbb.gov.pk", "Email: membertbb@yahoo.com", "Telephone: 091-7217159-60"
    ], "visualStatus": "text and layout represented digitally"},
    {"file": "004_page_2.jpg", "page": "iii", "title": "Table of Contents", "paragraphs": [], "contents": [
        ["1", "INTRODUCTION TO SYMBOLIC PACKAGE, MAPLE", 1], ["2", "FUNCTIONS AND LIMITS", 25], ["3", "DIFFERENTIATION", 63], ["4", "HIGHER ORDER DERIVATIVES AND APPLICATIONS", 101], ["5", "DIFFERENTIATION OF VECTOR FUNCTIONS", 130], ["6", "INTEGRATION", 142], ["7", "PLANE ANALYTIC GEOMETRY STRAIGHT LINE", 178], ["8", "CONICS–I", 213], ["9", "CONICS–II", 241], ["10", "DIFFERENTIAL EQUATIONS", 286], ["11", "PARTIAL DIFFERENTIATION", 300], ["12", "INTRODUCTION TO NUMERICAL METHODS", 309], ["", "ANSWERS", 326]
    ], "visualStatus": "table represented digitally"},
    {"file": "005_page_1.jpg", "page": 1, "title": "INTRODUCTION TO SYMBOLIC PACKAGE: MAPLE", "paragraphs": [], "objectives": [
        ["1.1 Introduction", ["Recognize MAPLE environment.", "Recognize basic MAPLE commands.", "Use MAPLE as a calculator.", "Use online MAPLE help."]],
        ["1.2 Polynomials", ["Use MAPLE commands for.", "factoring a polynomial,", "expanding an expression,", "simplifying an expression,", "simplifying a rational expression,", "substituting into an expression."]],
        ["1.3 Graphics", ["Plot a two-dimensional graph.", "Demonstrate domain and range of a plot.", "Sketch parametric equations.", "Know plotting options."]],
        ["1.4 Matrices", ["Recognize matrix and vector entry arrangement.", "Apply matrix operations.", "Compute inverse and transpose of a matrix."]]
    ], "visualStatus": "no instructional diagram"}
]
intro = "In the modern age of science and technology, the technical computation has become the heart of problem solving in engineering and mathematics. To help us, MAPLE offers a vast repository of mathematical algorithms converting a wide range of applications. It is a symbolic and numeric computing tools as well as a multi-paradigm programming language maple was conceived at the university of waterloo in 1980. From the first day it continues to be the benchmark software for mathematical and symbolic computation. Maple user interface allows us to harness all the computational power by using context sensitive means, interactive assistant and task templates. In this unit we will learn how to use the basic commands that will allow and lead us into the creative, dynamic and captivating world of MAPLE explorations."
parts = [intro, "Maple software consists of three different parts.",
    "i. User interface", "It handles the input of mathematical expressions and different commands. User interface also handles the display of output and the control of the MAPLE worksheet environment.",
    "ii. Kernel", "It is a small collection of compiled C code. The entire kernel is loaded when a MAPLE session is started. It contains those essential facilities that required to run maple and perform basic mathematical operations. The components of kernel include the .maple programming language interpreter, arithmetics and memory management facilities and fundamental functions. The small size of kernel ensures that the maple system is portable, compact and efficient.",
    "iii. Library", "It contains most of the maple routines including functions relating to algebra, statistics, calculus, graphics and other topics. This library also consists of individual routines and different packages of routines. All the library routines which are implemented in the high level maple programming language can be viewed and modified. Hence, it is useful to learn the maple programming language so that we can modify the existing code to produce the required routines."]
pages[-1]["sections"] = [{"heading": "1.1 Introduction", "paragraphs": [intro]}, {"heading": "1.1.1 Recognition of MAPLE environment", "paragraphs": parts[1:]}]
pages.extend(PAGES)
pages.extend(GRAPHICS_PAGES)
pages.extend(MATRIX_PAGES)

asset_dir = ROOT / 'assets/math12'
asset_dir.mkdir(parents=True, exist_ok=True)
source_dir = ROOT.parent / 'Books/12th/12th Maths/JPG'
full_pdf = PdfReader(source_dir.parent / 'PDF/Math Book for 12 class KPTBB.pdf')
spread_images = {}
crop_manifest_path = asset_dir / "source-crop-manifest.json"
crop_manifest = json.loads(crop_manifest_path.read_text(encoding="utf-8")) if crop_manifest_path.exists() else {}
pdf_stamp = (source_dir.parent / "PDF/Math Book for 12 class KPTBB.pdf").stat().st_mtime_ns
for pdf_page, asset_name, rectangle in FIGURE_PDF_CROPS + GRAPHICS_CROPS + FUNCTION_CROPS + EX21_CROPS + HYPERBOLIC_CROPS + EX23_CROPS + CONTINUITY_CROPS + SUMMARY2_CROPS + DIFFERENTIATION_CROPS + EX31_CROPS + EX32_CROPS + EX42_CROPS + UNIT4_CLOSE_CROPS + VECTOR_CROPS + UNIT5_CLOSE_CROPS + EX62_CROPS + DEFINITE_CROPS + EX64_CROPS + STRAIGHT_CROPS + EX72_CROPS + EX73_CROPS + HOMOGENEOUS_CROPS + UNIT7_CLOSE_CROPS + CIRCLE_HISTORY_CROPS + HYPERBOLA_BLURRED_CROPS + EX101_CROPS + ODE_TRAJECTORY_CROPS + UNIT10_CLOSE_CROPS + EX111_CROPS + UNIT11_CLOSE_CROPS + EX121_CROPS + NUMERICAL_MAPLE_CROPS + EX122_CROPS + UNIT12_CLOSE_CROPS + BACKMATTER_CROPS:
    crop_key = str(pdf_stamp)+":"+str(pdf_page)+":"+str(rectangle)
    if crop_manifest.get(asset_name)==crop_key and (asset_dir/(asset_name+".jpg")).exists():
        continue
    if pdf_page not in spread_images:
        spread_images[pdf_page] = max(full_pdf.pages[pdf_page - 1].images, key=lambda image: image.image.width * image.image.height).image.convert('RGB')
    original = spread_images[pdf_page]
    original.crop(rectangle).save(asset_dir / (asset_name + '.jpg'), quality=92)
    crop_manifest[asset_name]=crop_key
write_rotated_assets(full_pdf,asset_dir,crop_manifest,str(pdf_stamp))
crop_manifest_path.write_text(json.dumps(crop_manifest,indent=2),encoding='utf-8')

target = ROOT / "js/math_12_data.js"
text = target.read_text(encoding="utf-8")
marker = "// BEGIN JPG-VERIFIED MATH12 SOURCE REVISION"
if marker in text:
    text = text[:text.index(marker)].rstrip() + "\n"
text += marker + "\nMATH_12_DATA[0].sourcePages = " + json.dumps(pages, ensure_ascii=False, indent=2) + ";\n"
text += 'MATH_12_DATA[1].sourcePages = ' + json.dumps(FUNCTION_PAGES, ensure_ascii=False, indent=2) + ';\n'
text += 'MATH_12_DATA[2].sourcePages = ' + json.dumps(DIFFERENTIATION_PAGES, ensure_ascii=False, indent=2) + ';\n'
text += 'MATH_12_DATA[3].sourcePages = ' + json.dumps(HIGHER_PAGES, ensure_ascii=False, indent=2) + ';\n'
# Keep the unreviewed subsections of 1.2 while replacing reviewed content only.
text += """const math12Intro = MATH_12_DATA[0].sections[0];
const math12ReviewedPages = MATH_12_DATA[0].sourcePages;
math12Intro.sourceBlocks = math12ReviewedPages[5].sections.flatMap(section => [{type:'heading', text:section.heading}, ...section.paragraphs.map(text => ({type:'paragraph', text}))]);
math12Intro.sourceBlocks.push(...math12ReviewedPages.filter(page => page.page >= 2 && page.page <= 5).flatMap(page => page.blocks));
math12Intro.sourceBlocks.push(math12ReviewedPages.find(page => page.page === 6).blocks[0]);
const math12BlockText = block => [block.text, block.result, block.caption, block.diagram && block.diagram.title, block.label, ...(block.headers || []), ...(block.rows || []).map(row => row.join(' ')), ...(block.items || [])].filter(Boolean).join('\\n');
math12Intro.theory = math12Intro.sourceBlocks.map(math12BlockText).join('\\n\\n');
math12Intro.sourceReferences = math12ReviewedPages.filter(page => typeof page.page === 'number' && page.page <= 6).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope: page.page === 6 ? 'Figure 1.4 only' : page.page === 1 ? '1.1 and 1.1.1' : 'full page', verification: page.sourceDefects && page.sourceDefects.length ? 'partial: source clipping' : 'visually compared with JPG', alternateVerification:page.alternateVerification}));
const math12Polynomials = MATH_12_DATA[0].sections[1];
math12Polynomials.sourceBlocks = math12ReviewedPages.find(page => page.page === 6).blocks.slice(1);
math12Polynomials.sourceBlocks.push(...math12ReviewedPages.filter(page => page.page >= 7 && page.page <= 9).flatMap(page => page.blocks));
math12Polynomials.sourceBlocks.push(...math12ReviewedPages.find(page => page.page === 10).blocks.slice(0,2));
math12Polynomials.theory = math12Polynomials.sourceBlocks.map(math12BlockText).join('\\n\\n');
math12Polynomials.sourceReferences = math12ReviewedPages.filter(page => page.page >= 6 && page.page <= 10).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope:page.page === 6 ? '1.2 and 1.2.1' : page.page === 10 ? 'Figures 1.9 and 1.10' : 'full page', verification:'visually compared with JPG and full PDF'}));
const math12Graphics = MATH_12_DATA[0].sections[2];
math12Graphics.sourceBlocks = [...math12ReviewedPages.find(page => page.page === 10).blocks.slice(2), ...math12ReviewedPages.filter(page => page.page >= 11 && page.page <= 18).flatMap(page => page.blocks)].reduce((blocks, block) => {
  if (block.continuesPreviousParagraph && blocks.length && blocks[blocks.length-1].type === 'paragraph') blocks[blocks.length-1] = {...blocks[blocks.length-1], text:blocks[blocks.length-1].text + ' ' + block.text};
  else blocks.push(block);
  return blocks;
}, []);
math12Graphics.unreviewedTheory = '';
math12Graphics.theory = math12Graphics.sourceBlocks.map(math12BlockText).join('\\n\\n');
math12Graphics.sourceReferences = math12ReviewedPages.filter(page => page.page >= 10 && page.page <= 18).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope:page.page === 10 ? '1.3 and opening sentence of 1.3.1' : 'full page', verification:'visually compared with JPG and full PDF', alternateVerification:page.alternateVerification}));
const math12Matrices = MATH_12_DATA[0].sections[3];
math12Matrices.unreviewedTheory = '';
math12Matrices.sourceBlocks = math12ReviewedPages.filter(page => page.page >= 19 && page.page <= 24).flatMap(page => page.blocks);
math12Matrices.theory = math12Matrices.sourceBlocks.map(math12BlockText).join('\\n\\n') + '\\n\\n' + math12Matrices.unreviewedTheory;
math12Matrices.sourceReferences = math12ReviewedPages.filter(page => page.page >= 19 && page.page <= 24).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope:'full page', verification:'visually compared with JPG', alternateVerification:page.alternateVerification}));
MATH_12_DATA[0].workedExamples.forEach((example, index) => {
  const ranges = [[4,5],[5,5],[11,11],[11,11],[12,12],[18,18]];
  example.sourceReferences = [{class:12, subject:'Mathematics', pageStart:ranges[index][0], pageEnd:ranges[index][1], verification:'visually compared with JPG and full PDF'}];
  example.solutionOrigin = 'SpaceBook learning enhancement';
  example.progressiveSolution = true;
});
MATH_12_DATA[0].workedExamples[4].problem = math12ReviewedPages.find(page => page.page === 12).blocks[3].text + ' ' + math12ReviewedPages.find(page => page.page === 12).blocks[4].text;
MATH_12_DATA[0].workedExamples[4].sourceClarification = 'The printed question uses x for both coordinates. The cosine and sine coordinate pair in the command and the circle in Figure 1.15 indicate x = cos(t), y = sin(t). The original question above retains the printed wording.';
const math12Functions = MATH_12_DATA[1].sections[0];
math12Functions.unreviewedTheory = '';
math12Functions.sourceBlocks = [...MATH_12_DATA[1].sourcePages.find(page => page.page === 26).blocks, ...MATH_12_DATA[1].sourcePages.find(page => page.page === 27).blocks, ...MATH_12_DATA[1].sourcePages.find(page => page.page === 28).blocks.slice(0,5)].reduce((blocks, block) => {
  if (block.continuesPreviousParagraph && blocks.length && blocks[blocks.length-1].type === 'paragraph') blocks[blocks.length-1] = {...blocks[blocks.length-1], text:blocks[blocks.length-1].text + ' ' + block.text};
  else blocks.push(block);
  return blocks;
}, []);
math12Functions.theory = math12Functions.sourceBlocks.map(math12BlockText).join('\\n\\n') + '\\n\\n' + math12Functions.unreviewedTheory;
math12Functions.sourceReferences = MATH_12_DATA[1].sourcePages.filter(page => page.page>=26 && page.page<=28).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope:page.page===28 ? 'Example 2 continuation before section 2.2' : 'full page', verification:'visually compared with JPG and full PDF', alternateVerification:page.alternateVerification}));
const math12Composition = MATH_12_DATA[1].sections[1];
math12Composition.unreviewedTheory = '';
math12Composition.sourceBlocks = [...MATH_12_DATA[1].sourcePages.find(page => page.page === 28).blocks.slice(5), ...MATH_12_DATA[1].sourcePages.find(page => page.page === 29).blocks.slice(0,20)];
math12Composition.theory = math12Composition.sourceBlocks.map(math12BlockText).join('\\n\\n') + '\\n\\n' + math12Composition.unreviewedTheory;
math12Composition.sourceReferences = MATH_12_DATA[1].sourcePages.filter(page => page.page>=28 && page.page<=29).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope:page.page===28 ? '2.2 through Example 3' : '2.2.2 and Examples 4–5', verification:'visually compared with JPG and full PDF'}));
const math12Inverse = MATH_12_DATA[1].sections[2];
math12Inverse.unreviewedTheory = math12Inverse.theory.slice(math12Inverse.theory.indexOf('Read the graphs'));
math12Inverse.sourceBlocks = [...MATH_12_DATA[1].sourcePages.find(page => page.page===29).blocks.slice(20), ...MATH_12_DATA[1].sourcePages.find(page => page.page===30).blocks];
math12Inverse.theory = math12Inverse.sourceBlocks.map(math12BlockText).join('\\n\\n') + '\\n\\n' + math12Inverse.unreviewedTheory;
math12Inverse.sourceReferences = MATH_12_DATA[1].sourcePages.filter(page => page.page>=29 && page.page<=30).map(page => ({class:12, subject:'Mathematics', page:page.page, jpg:page.file, scope:page.page===29 ? '2.3' : 'full page', verification:'visually compared with JPG and full PDF'}));
const math12Unit2Examples = MATH_12_DATA[1].workedExamples;
Object.assign(math12Unit2Examples[0], {
  problem:'Find the domain and range of the function whose graph is shown in Figure 2.2.',
  given:'The displayed graph has closed endpoints at x = −6 and x = 2; its vertical extent is 0 to 4.',
  method:'Read all x-values for the domain and all y-values for the range.',
  steps:['Project the displayed curve onto the x-axis: it covers −6 through 2.', 'Both horizontal endpoints are closed, so include −6 and 2 in the domain.', 'Project the displayed curve onto the y-axis: it covers 0 through 4.', 'The curve reaches the extreme y-values, so include both endpoints in the range.'],
  answer:'Domain: [−6, 2]. Range: [0, 4].',
  diagram:MATH_12_DATA[1].sourcePages.find(page => page.page===27).blocks[0].diagram
});
Object.assign(math12Unit2Examples[1], {
  problem:'Graph the following absolute value functions and identify its domain and range: f(x) = |3x − 4|.',
  given:'f(x) = |3x − 4|', method:'Find where the expression inside the absolute value changes sign.',
  steps:['Solve 3x − 4 = 0 to find the vertex x = 4/3.', 'For x ≥ 4/3, f(x) = 3x − 4. For x < 4/3, f(x) = −3x + 4.', 'Plot the vertex (4/3, 0), the point (0, 4), and the point (8/3, 4). Join them along the two straight branches.', 'Every real x is allowed, and the minimum function value is 0.'],
  answer:'Vertex: (4/3, 0). Domain: (−∞, ∞). Range: [0, ∞).',
  sourceClarification:'The printed problem uses |3x − 4|; its printed solution and Figure 2.5 use |3x + 4|. This labelled learning solution answers the original problem with the minus sign.',
  diagram:{...MATH_12_DATA[1].sourcePages.find(page => page.page===27).blocks.find(block => block.caption==='Figure 2.5').diagram, title:'SpaceBook learning enhancement: f(x) = |3x − 4|', absolute:{a:3,b:-4}}
});
Object.assign(math12Unit2Examples[2], {
  problem:'Let f(x) = 2x − 1 and g(x) = √(3x + 5). Find (a) g(f(4)), (b) f(g(4)), (c) f(g(−2)).',
  given:'f(x) = 2x − 1; g(x) = √(3x + 5)', method:'Evaluate the inner function first and check that its input is in the domain.',
  steps:['(a) First f(4) = 2(4) − 1 = 7. Then g(f(4)) = g(7) = √(3(7) + 5) = √26.', '(b) First g(4) = √(3(4) + 5) = √17. Then f(g(4)) = f(√17) = 2√17 − 1.', '(c) The real domain of g requires 3x + 5 ≥ 0, so x ≥ −5/3.', 'Because −2 < −5/3, g(−2) is not real. The outer function f therefore cannot be evaluated on that output in this real-function problem.'],
  answer:'(a) √26; (b) 2√17 − 1; (c) undefined over the real numbers.', diagram:null
});
math12Unit2Examples.slice(0,3).forEach((example,index) => {
  const ranges=[[26,27],[27,28],[28,28]];
  example.solutionOrigin='SpaceBook learning enhancement'; example.progressiveSolution=true;
  example.sourceReferences=[{class:12, subject:'Mathematics', pageStart:ranges[index][0], pageEnd:ranges[index][1], verification:'visually compared with JPG and full PDF'}];
});
Object.assign(math12Unit2Examples[3], {
  problem:'Let f(x) = 4x + 1 and g(x) = 2x² + 5x. Find (a) g(f(x)), (b) f(g(x)).',
  given:'f(x) = 4x + 1; g(x) = 2x² + 5x', method:'Substitute the inner expression into the outer function.',
  steps:['For g(f(x)), substitute 4x + 1 for the input of g: 2(4x + 1)² + 5(4x + 1).', 'Expand (4x + 1)² = 16x² + 8x + 1, then combine terms to get 32x² + 36x + 7.', 'For f(g(x)), substitute 2x² + 5x for the input of f: 4(2x² + 5x) + 1.', 'Expand to get 8x² + 20x + 1. The two compositions are different.'],
  answer:'(a) 32x² + 36x + 7; (b) 8x² + 20x + 1.', diagram:null
});
Object.assign(math12Unit2Examples[4], {
  problem:'Given L(p) = 0.7√(p² + 3) and p(t) = 1 + 0.02t³, where t is years from now and p is population in hundred thousands, what carbon-monoxide level is expected in 4 years?',
  given:'L(p) = 0.7√(p² + 3); p(t) = 1 + 0.02t³', method:'Compose L with p, then evaluate at t = 4.',
  steps:['Substitute p(t) into L to obtain L(p(t)) = 0.7√((1 + 0.02t³)² + 3).', 'At t = 4, p(4) = 1 + 0.02(64) = 2.28, corresponding to 228,000 people.', 'Evaluate L(2.28) = 0.7√(2.28² + 3) = 0.7√8.1984.', 'This is approximately 2.0043 parts per million, which rounds to the printed 2.0 ppm.'],
  answer:'Approximately 2.0 ppm.', diagram:null
});
const math12PollutionSource = MATH_12_DATA[1].sourcePages.find(page => page.page===29).blocks;
math12Unit2Examples[4].problem = [11,13,14].map(index => math12PollutionSource[index].text).join(' ');
math12Unit2Examples[4].sourceQuestionBlocks = [math12PollutionSource[12]];
const math12InverseExamples = [
  {id:'we-2-6',num:'6',title:'Example 6', problem:'Find the inverse function of f(t) = 3t − 8.', given:'f(t) = 3t − 8', method:'Set the output equal to a new variable and solve for the original input.', steps:['Write z = 3t − 8.', 'Add 8 to both sides: z + 8 = 3t.', 'Divide by 3: t = (z + 8)/3.', 'Replace the inverse input z by t: f⁻¹(t) = (t + 8)/3. Substituting f(t) gives ((3t − 8) + 8)/3 = t.'], answer:'f⁻¹(t) = (t + 8)/3.',diagram:null},
  {id:'we-2-7',num:'7',title:'Example 7',problem:'Let f(x) = 2x + 3, g(x) = 3x, and h(x) = f(g(x)). Find (a) h(x), (b) f⁻¹(x), (c) g⁻¹(x), (d) h⁻¹(x).', given:'f(x) = 2x + 3; g(x) = 3x; h = f ∘ g', method:'Compose first; solve each linear equation for its input to obtain the inverse.', steps:['(a) h(x) = f(3x) = 2(3x) + 3 = 6x + 3.', '(b) From y = 2x + 3, solve x = (y − 3)/2, so f⁻¹(x) = (x − 3)/2.', '(c) From y = 3x, solve x = y/3, so g⁻¹(x) = x/3.', '(d) From y = 6x + 3, solve x = (y − 3)/6, so h⁻¹(x) = (x − 3)/6. This also equals g⁻¹(f⁻¹(x)).'],answer:'(a) 6x + 3; (b) (x − 3)/2; (c) x/3; (d) (x − 3)/6.',diagram:null}
];
math12Unit2Examples.splice(5,0,...math12InverseExamples);
math12InverseExamples.forEach(example => {example.id = 'we-2-source-' + example.num;});
math12Unit2Examples.slice(3,7).forEach((example,index) => {
  const page=index<2 ? 29 : 30;
  example.solutionOrigin='SpaceBook learning enhancement'; example.progressiveSolution=true;
  example.sourceReferences=[{class:12,subject:'Mathematics',pageStart:page,pageEnd:page,verification:'visually compared with JPG and full PDF'}];
});
"""
exercise_data = []
for index, question in enumerate(EX21_QUESTIONS):
    exercise_data.append({'question':question, 'steps':EX21_STEPS[index], 'answer':EX21_ANSWERS[index], 'solution':'\n'.join(EX21_STEPS[index]), 'progressiveSolution':True, 'solutionOrigin':'SpaceBook learning enhancement', 'sourceReferences':[{'class':12,'subject':'Mathematics','page':31,'jpg':'020_page_1.jpg','verification':'visually compared with JPG and full PDF'}], 'sourceQuestionBlocks':EX21_GRAPHS if index==0 else EX21_PROJECT if index==4 else [], 'solutionStatus':'partial: photographic profile endpoints unverified' if index==4 else 'worked and checked'})
exercise_data[0]['sourceClarification'] = 'The textbook answer page 326 prints (−∞, 5) for (a). The plotted parabola reaches its maximum, so the learning answer includes 5. The standard formulas in the learning solution are inferred from the shapes and scales, not printed labels.'
exercise_data[0]['answerKeyReference'] = {'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':167,'printedPage':326,'scope':'Exercise 2.1 Question 1 domain and range answers','verification':'visually inspected'}
text += 'const math12Exercise21Revision = ' + json.dumps(exercise_data, ensure_ascii=False, indent=2) + ';\n'
text += """math12Exercise21Revision.forEach((revision,index) => {
  const problem = MATH_12_DATA[1].exercises[0].problems[index];
  if(index === 1) {problem.solutionDiagram=problem.diagram; problem.diagram=null;}
  Object.assign(problem,revision);
});
MATH_12_DATA[1].exercises[0].pageStart = 31;
MATH_12_DATA[1].exercises[0].pageEnd = 31;
MATH_12_DATA[1].sections[2].unreviewedTheory = '';
MATH_12_DATA[1].sections[2].theory = MATH_12_DATA[1].sections[2].sourceBlocks.map(math12BlockText).join('\\n\\n');
const math12Transcendental = MATH_12_DATA[1].sections[3];
math12Transcendental.sourceBlocks = MATH_12_DATA[1].sourcePages.filter(page => page.page>=32 && page.page<=36).flatMap(page=>page.blocks);
const math12ParametricPage=MATH_12_DATA[1].sourcePages.find(page=>page.page===37);
const math12GraphicalStart=math12ParametricPage.blocks.findIndex(block=>block.text==='2.5 Graphical Representation');
math12Transcendental.sourceBlocks.push(...math12ParametricPage.blocks.slice(0,math12GraphicalStart));
math12Transcendental.unreviewedTheory = '';
math12Transcendental.theory = math12Transcendental.sourceBlocks.map(math12BlockText).join('\\n\\n');
math12Transcendental.sourceReferences = MATH_12_DATA[1].sourcePages.filter(page=>page.page>=32 && page.page<=36).map(page=>({class:12,subject:'Mathematics',page:page.page,jpg:page.file,scope:'full page',verification:page.sourceDefects && page.sourceDefects.length ? 'partial: faint source phrase' : 'visually compared with JPG and full PDF',alternateVerification:page.alternateVerification}));
math12Transcendental.sourceReferences.push({class:12,subject:'Mathematics',page:37,jpg:'023_page_1.jpg',scope:'Remember box and parametric representation through Example 12',verification:'visually compared with JPG and full PDF'});
const math12Graphical=MATH_12_DATA[1].sections[4];
math12Graphical.unreviewedTheory='';
const math12Page44=MATH_12_DATA[1].sourcePages.find(page=>page.page===44);
const math12Exercise22Start=math12Page44.blocks.findIndex(block=>block.text==='Exercise 2.2');
math12Graphical.title='2.5 Graphical Representation';
math12Graphical.sourceBlocks=math12ParametricPage.blocks.slice(math12GraphicalStart).concat(...MATH_12_DATA[1].sourcePages.filter(page=>page.page>=38 && page.page<=43).map(page=>page.blocks),math12Page44.blocks.slice(0,math12Exercise22Start));
math12Graphical.theory=math12Graphical.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Graphical.unreviewedTheory;
math12Graphical.sourceReferences=[{class:12,subject:'Mathematics',page:37,jpg:'023_page_1.jpg',scope:'2.5 and Example 13',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:38,jpg:'023_page_2.jpg',scope:'full page',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:39,jpg:'024_page_1.jpg',scope:'full page',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:40,jpg:'024_page_2.jpg',scope:'full page',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:41,jpg:'025_page_1.jpg',scope:'full page',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:42,jpg:'025_page_2.jpg',scope:'full page; Example 23 verified across pages 42–43',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:43,jpg:'026_page_1.jpg',scope:'full page; Example 24 verified across pages 43–44',verification:'visually compared with JPG and full PDF'},{class:12,subject:'Mathematics',page:44,jpg:'026_page_2.jpg',scope:'Example 24 continuation; Exercise 2.2 appears in the exercises tab',verification:'visually compared with JPG and full PDF'}];
const math12Limits=MATH_12_DATA[1].sections[5];
math12Limits.title='2.6 Limit of Function';
math12Limits.unreviewedTheory='';
math12Limits.sourceBlocks=MATH_12_DATA[1].sourcePages.filter(page=>page.page>=45&&page.page<=50).flatMap(page=>page.blocks.map(block=>({...block})));
const math12Continuation=math12Limits.sourceBlocks.findIndex(block=>block.text&&block.text.startsWith('gets smaller and smaller'));
if(math12Continuation>0){math12Limits.sourceBlocks[math12Continuation-1].text+=' '+math12Limits.sourceBlocks[math12Continuation].text;math12Limits.sourceBlocks.splice(math12Continuation,1);}
math12Limits.theory=math12Limits.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Limits.unreviewedTheory;
math12Limits.sourceReferences=MATH_12_DATA[1].sourcePages.filter(page=>page.page>=45&&page.page<=50).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));
const math12ImportantLimits=MATH_12_DATA[1].sections[6];
math12ImportantLimits.title='2.7 Important Limits';
math12ImportantLimits.unreviewedTheory='';
math12ImportantLimits.sourceBlocks=MATH_12_DATA[1].sourcePages.filter(page=>page.page>=51&&page.page<=55).flatMap(page=>page.blocks);
math12ImportantLimits.theory=math12ImportantLimits.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12ImportantLimits.unreviewedTheory;
math12ImportantLimits.sourceReferences=MATH_12_DATA[1].sourcePages.filter(page=>page.page>=51&&page.page<=55).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));
const math12Continuity=MATH_12_DATA[1].sections[7];
math12Continuity.unreviewedTheory='';
math12Continuity.sourceBlocks=MATH_12_DATA[1].sourcePages.filter(page=>page.page>=57&&page.page<=59).flatMap(page=>page.blocks);
math12Continuity.theory=math12Continuity.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Continuity.unreviewedTheory;
math12Continuity.sourceReferences=MATH_12_DATA[1].sourcePages.filter(page=>page.page>=57&&page.page<=59).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));
Object.assign(MATH_12_DATA[1].workedExamples.find(example=>example.num==='8'), {
  problem:'Cholera bacteria grow according to N = N₀ exp(1.386t), where t is hours and N₀ is the initial count. Starting with 25 bacteria, find the count to the nearest unit after (a) 1 hour, (b) 3 hours, (c) 4 hours, and (d) interpret.',
  given:'N₀ = 25; N(t) = 25 exp(1.386t)', method:'Substitute each time into the exponential model, then round to the nearest whole bacterium.',
  steps:['Substitute N₀ = 25 to obtain N(t) = 25 exp(1.386t).', '(a) N(1) = 25 exp(1.386) ≈ 99.9706, so the nearest whole-number count is 100.', '(b) N(3) = 25 exp(4.158) ≈ 1598.5877, so the count is 1599.', '(c) N(4) = 25 exp(5.544) ≈ 6392.4688, so the count is 6392.', '(d) The positive exponential rate means the model population grows as time increases; its multiplier over each hour is exp(1.386), approximately 4.'],
  answer:'(a) 100; (b) 1599; (c) 6392 bacteria. (d) Exponential growth.',
  sourceClarification:'The printed solution gives 99.97 after one hour; the question asks for the nearest unit, so this learning solution rounds it to 100.',
  solutionOrigin:'SpaceBook learning enhancement',progressiveSolution:true,
  sourceReferences:[{class:12,subject:'Mathematics',pageStart:34,pageEnd:34,verification:'visually compared with JPG and full PDF'}],
  diagram:MATH_12_DATA[1].sourcePages.find(page=>page.page===34).blocks.find(block=>block.caption==='Figure 2.6').diagram
});
const math12GrowthSource=MATH_12_DATA[1].sourcePages.find(page=>page.page===34).blocks;
MATH_12_DATA[1].workedExamples.find(example=>example.num==='8').problem = math12GrowthSource[3].text + ' ' + math12GrowthSource[4].result + ' ' + math12GrowthSource[5].text;
Object.assign(MATH_12_DATA[1].workedExamples.find(example=>example.num==='9'), {
  problem:'Evaluate (a) log 10000, (b) log .01, (c) log √10.', given:'Common logarithms have base 10.',method:'Express each argument as a power of 10.',
  steps:['(a) 10000 = 10⁴, so log 10000 = log(10⁴) = 4 log 10 = 4.', '(b) .01 = 1/100 = 10⁻², so log .01 = −2 log 10 = −2.', '(c) √10 is the one-half power of 10, so log √10 = (1/2) log 10 = 1/2.'],
  answer:'(a) 4; (b) −2; (c) 1/2.',diagram:null,
  sourceClarification:'The printed question already includes the result 1/2 in part (c). The source lesson retains it; this learning question leaves the evaluation to the solution steps.',
  progressiveSolution:true,solutionOrigin:'SpaceBook learning enhancement',sourceReferences:[{class:12,subject:'Mathematics',pageStart:35,pageEnd:35,verification:'visually compared with JPG and full PDF'}]
});
Object.assign(MATH_12_DATA[1].workedExamples.find(example=>example.num==='10'), {
  problem:'Find x to four decimal places: (a) 10ˣ = 2; (b) eˣ = 3.', given:'Solve each exponential equation for x.',method:'Apply the logarithm with the same base as the exponential.',
  steps:['(a) Apply the common logarithm to 10ˣ = 2: x log 10 = log 2.', 'Because log 10 = 1, x = log 2 ≈ 0.3010299957. To four decimal places, x ≈ 0.3010.', '(b) Apply the natural logarithm to eˣ = 3: x ln e = ln 3.', 'Because ln e = 1, x = ln 3 ≈ 1.0986122887. To four decimal places, x ≈ 1.0986.'],
  answer:'(a) x ≈ 0.3010; (b) x ≈ 1.0986.',diagram:null,
  progressiveSolution:true,solutionOrigin:'SpaceBook learning enhancement',sourceReferences:[{class:12,subject:'Mathematics',pageStart:35,pageEnd:35,verification:'visually compared with JPG and full PDF'}]
});
Object.assign(MATH_12_DATA[1].workedExamples.find(example=>example.num==='11'), {
  problem:MATH_12_DATA[1].sourcePages.find(page=>page.page===35).blocks.slice(-3).map(block=>block.text||block.result).join(' '),
  given:'T(n) = −1.43 ln((10000 − n)/(4998n)); n = 500 or 5000.', method:'Substitute each population into the textbook model, then evaluate the natural logarithm.',
  steps:['For n = 500, the logarithm argument is (10000 − 500)/(4998 × 500) = 9500/2499000.', 'T(500) = −1.43 ln(9500/2499000) ≈ 7.9685 days, or about 8 days to the nearest whole day.', 'For n = 5000, the logarithm argument is (10000 − 5000)/(4998 × 5000) = 5000/24990000 = 1/4998.', 'T(5000) = −1.43 ln(1/4998) ≈ 12.1790 days, or about 12 days to the nearest whole day.'],
  answer:'(a) ≈7.9685 days (about 8); (b) ≈12.1790 days (about 12).',diagram:null,
  sourceClarification:'The printed solution uses rounded intermediate values and prints 7.96903 and 12.17. This learning evaluation retains the given model and uses unrounded ratios. The printed solution also says flu although the question says covid-19; its source wording remains in the lesson.',
  progressiveSolution:true,solutionOrigin:'SpaceBook learning enhancement',sourceReferences:[{class:12,subject:'Mathematics',pageStart:35,pageEnd:36,verification:'visually compared with JPG and full PDF'}]
});
const math12ParametricExamples=[
  {id:'we-2-source-12',num:'12',title:'Example 12',problem:'Sketch the graph of the parametric functions (x(t), y(t)) = (3 − t, 2t) for all t.',given:'x = 3 − t; y = 2t; t ∈ ℝ',method:'Plot parameter values and eliminate t to identify the complete line.',steps:['For t = 0, the point is (3, 0). For t = 1, it is (2, 2). For t = 2, it is (1, 4).', 'Increasing t by 1 changes the position by (−1, 2), which is the direction vector.', 'From x = 3 − t, solve t = 3 − x. Substitute into y = 2t to get y = 6 − 2x.', 'Because all real t are allowed, the graph is the entire straight line through (3, 0) with direction (−1, 2).'],answer:'y = 6 − 2x, for all real x.',diagram:math12ParametricPage.blocks.find(block=>block.caption==='Figure 2.9').diagram},
  {id:'we-2-source-13',num:'13',title:'Example 13',problem:'Draw the graphs of y = eˣ and y = e⁻ˣ.',given:'Two exponential functions with opposite exponent signs.',method:'Use corresponding points and the reflection across the y-axis.',steps:['For x = −2, −1, 0, 1, 2, the values of eˣ are approximately 0.1353, 0.3679, 1, 2.7183, 7.3891.', 'For the same x-values, the values of e⁻ˣ are approximately 7.3891, 2.7183, 1, 0.3679, 0.1353.', 'Plot the points and join each set with a smooth curve. Both curves pass through (0, 1), and e⁻ˣ is the reflection of eˣ across the y-axis.', 'Both domains are ℝ and both ranges are (0, ∞). The horizontal axis y = 0 is an asymptote; neither curve reaches it.'],answer:'eˣ increases and e⁻ˣ decreases; both have domain ℝ and range (0, ∞).',diagram:math12ParametricPage.blocks.find(block=>block.caption==='Figure 2.10').diagram}
];
math12ParametricExamples.push({id:'we-2-source-14',num:'14',title:'Example 14',problem:'Sketch the graph of y = 2ˣ.',given:'An exponential function with base 2.',method:'Make a value table, plot its points, and draw a smooth curve.',steps:['For x = −5, −1, 0, 1, 2, 3, evaluate 2ˣ to obtain 1/32, 1/2, 1, 2, 4, 8.', 'Plot (−5, 1/32), (−1, 1/2), (0, 1), (1, 2), (2, 4), (3, 8). The textbook rounds 1/32 = 0.03125 to 0.03.', 'Join the points with a smooth increasing curve. It crosses the y-axis at (0, 1).', 'As x decreases without bound, 2ˣ approaches 0 and stays positive. Domain: ℝ; range: (0, ∞); horizontal asymptote: y = 0.'],answer:'The graph is an increasing exponential curve through (0, 1), with domain ℝ and range (0, ∞).',diagram:MATH_12_DATA[1].sourcePages.find(page=>page.page===38).blocks.find(block=>block.caption==='Figure 2.11').diagram});

const math12LogGraphExamples=[{"id": "we-2-source-15", "num": "15", "title": "Example 15", "problem": "Sketch the graph of y = log₂x.", "given": "The logarithm has base 2.", "method": "Reverse the coordinate pairs of y = 2ˣ.", "steps": ["Start with the exponential pairs (−5, 1/32), (−1, 1/2), (0, 1), (1, 2), (2, 4), (3, 8).", "Interchange coordinates to get (1/32, −5), (1/2, −1), (1, 0), (2, 1), (4, 2), (8, 3).", "Draw a smooth increasing curve through these points, reflected from y = 2ˣ across y = x.", "The logarithm requires x > 0. Its domain is (0, ∞), its range is ℝ, and its vertical asymptote is x = 0."], "answer": "An increasing logarithmic curve through (1, 0), reflected from y = 2ˣ across y = x."}, {"id": "we-2-source-16", "num": "16", "title": "Example 16", "problem": "Sketch the graph of y = log₂(x − 2).", "given": "A base-2 logarithm shifted horizontally.", "method": "Use x = 2 + 2ʸ, or translate y = log₂x two units right.", "steps": ["Rewrite y = log₂(x − 2) as x − 2 = 2ʸ, so x = 2 + 2ʸ.", "For y = −2, −1, 0, 1, 2, calculate x = 2.25, 2.5, 3, 4, 6.", "Plot (2.25, −2), (2.5, −1), (3, 0), (4, 1), (6, 2), and join them with a smooth increasing curve.", "Since x − 2 > 0, the domain is (2, ∞). The range is ℝ, the vertical asymptote is x = 2, and the x-intercept is (3, 0)."], "answer": "The graph of y = log₂x shifted two units right; domain (2, ∞), range ℝ, asymptote x = 2."}, {"id": "we-2-source-17", "num": "17", "title": "Example 17", "problem": "Sketch the graph of y = ln x.", "given": "The natural logarithm has base e.", "method": "Use the equivalent equation x = eʸ.", "steps": ["Rewrite y = ln x as x = eʸ.", "For y = −2, −1, 0, 1, 2, obtain x ≈ 0.1353, 0.3679, 1, 2.7183, 7.3891.", "Plot these (x, y) pairs and draw a smooth increasing curve. It crosses the x-axis at (1, 0).", "The domain is (0, ∞), the range is ℝ, and the vertical asymptote is x = 0. The curve is the reflection of y = eˣ across y = x."], "answer": "An increasing natural logarithm through (1, 0); domain (0, ∞), range ℝ, asymptote x = 0."}];
math12LogGraphExamples.forEach((example,index)=>{example.diagram=MATH_12_DATA[1].sourcePages.find(page=>page.page===39).blocks.find(block=>block.caption===`Figure 2.${14+index}`).diagram;math12ParametricExamples.push(example);});

const math12ConicExamples=[{"id": "we-2-source-18", "num": "18", "title": "Example 18", "problem": "Sketch the graph of x² + y² = 9.", "given": "An implicit equation in x and y.", "method": "Compare with the standard circle equation.", "steps": ["Write x² + y² = 9 as (x − 0)² + (y − 0)² = 3².", "Compare with (x − h)² + (y − k)² = r² to obtain center (0, 0) and radius 3.", "Mark (3, 0), (−3, 0), (0, 3), (0, −3), and draw the circle through them.", "The circle is the graph of an equation. It is not the graph of a single function y of x: for −3 < x < 3, most vertical lines meet it twice."], "answer": "A circle centered at (0, 0) with radius 3."}, {"id": "we-2-source-19", "num": "19", "title": "Example 19", "problem": "Sketch the graph of x²/16 + y²/9 = 1.", "given": "An ellipse centered at the origin.", "method": "Find the semi-axis lengths and foci from the standard form.", "steps": ["Compare with x²/a² + y²/b² = 1: a² = 16, b² = 9, so a = 4 and b = 3. The major axis is horizontal.", "Calculate c² = a² − b² = 16 − 9 = 7, giving foci (±√7, 0).", "Mark center (0, 0), vertices (±4, 0), and co-vertices (0, ±3).", "Draw a smooth closed ellipse through the four axis endpoints. Its horizontal width is 8 and its vertical height is 6."], "answer": "Ellipse centered at (0, 0); vertices (±4, 0), co-vertices (0, ±3), foci (±√7, 0).", "sourceClarification": "The source lists vertices (±3, 0) and co-vertices (0, ±4), interchanging the numerical lengths. This learning solution follows the given equation."}, {"id": "we-2-source-20", "num": "20", "title": "Example 20", "problem": "Sketch the graph of (x(t), y(t)) = (3t², 4t + 3).", "given": "x = 3t² and y = 4t + 3, for real t.", "method": "Make a parameter table and eliminate t.", "steps": ["For t = −2, −1, 0, 1, 2, the points are (12, −5), (3, −1), (0, 3), (3, 7), (12, 11).", "Solve y = 4t + 3 for t: t = (y − 3)/4.", "Substitute into x = 3t²: x = 3((y − 3)/4)² = (3/16)(y − 3)².", "Equivalently, (y − 3)² = (16/3)x. Draw a right-opening parabola with vertex (0, 3) and axis y = 3. As t increases, travel from the lower branch through the vertex to the upper branch."], "answer": "x = (3/16)(y − 3)²; right-opening parabola with vertex (0, 3) and axis y = 3.", "sourceClarification": "The source changes the coefficient from 3/16 to 3/8 in its final implication. This solution retains the coefficient obtained from the given parametric equations."}];
math12ConicExamples.forEach((example,index)=>{example.diagram=MATH_12_DATA[1].sourcePages.find(page=>page.page===40).blocks.find(block=>block.caption===`Figure 2.${17+index}`).diagram;math12ParametricExamples.push(example);});

const math12CompoundExamples=[{"id": "we-2-source-21", "num": "21", "title": "Example 21", "problem": "Sketch (x(t), y(t)) = (3 cos t, 2 sin t), for 0 ≤ t ≤ 2π.", "given": "x = 3 cos t; y = 2 sin t; one complete parameter interval.", "method": "Eliminate t with cos²t + sin²t = 1 and follow the parameter direction.", "steps": ["Divide by the amplitudes: x/3 = cos t and y/2 = sin t.", "Square and add: x²/9 + y²/4 = cos²t + sin²t = 1.", "The ellipse has center (0, 0), horizontal semi-axis 3 and vertical semi-axis 2. Its endpoints are (±3, 0) and (0, ±2).", "At t = 0, π/2, π, 3π/2, 2π, the points are (3, 0), (0, 2), (−3, 0), (0, −2), (3, 0). Draw one complete ellipse, travelled counterclockwise."], "answer": "x²/9 + y²/4 = 1, traversed once counterclockwise from (3, 0).", "diagram": {"type": "source-function-graph", "title": "x = 3 cos t, y = 2 sin t, 0 ≤ t ≤ 2π", "xMin": -4, "xMax": 4, "yMin": -3, "yMax": 3, "xTicks": [-3, -2, -1, 0, 1, 2, 3], "yTicks": [-2, -1, 1, 2], "ellipse": {"a": 3, "b": 2}}}, {"id": "we-2-source-22", "num": "22", "title": "Example 22", "problem": "Graph f(x) = 3 − x for x < −2; x + 2 for −2 ≤ x < 2; 1 for x ≥ 2.", "given": "Three formulas with different domains.", "method": "Plot each branch separately and apply its endpoint conditions.", "steps": ["For x < −2, draw y = 3 − x as a ray extending left, through (−3, 6), with an open endpoint at (−2, 5).", "For −2 ≤ x < 2, draw y = x + 2 from the closed point (−2, 0) to the open point (2, 4).", "For x ≥ 2, draw the horizontal ray y = 1 from the closed point (2, 1) to the right.", "Check f(−2) = 0 and f(2) = 1. There are jumps at both boundaries. The domain is ℝ and the range is [0, 4) ∪ (5, ∞)."], "answer": "Open points (−2, 5), (2, 4); closed points (−2, 0), (2, 1); domain ℝ, range [0, 4) ∪ (5, ∞)."}];
math12CompoundExamples[1].diagram=MATH_12_DATA[1].sourcePages.find(page=>page.page===41).blocks.find(block=>block.caption==='Figure 2.20').diagram;
math12ParametricExamples.push(...math12CompoundExamples);

const math12MapleExample={"id": "we-2-source-23", "num": "23", "title": "Example 23", "problem": "Use Maple commands to graph (a) f(x) = −(x + 2)² with printed domain [0, −4]; (b) (cos t, sin t), −3.5 ≤ t ≤ 3.5; (c) x² − y² = 1, with x and y from −5 to 5.", "given": "An explicit function, a parametric curve, and an implicit equation.", "method": "Choose a plot command matching each representation and specify its range.", "steps": ["(a) Interpret the displayed graph on −4 ≤ x ≤ 0. Enter plot(-(x+2)^2, x=-4..0); The parabola has vertex (−2, 0) and endpoints (−4, −4), (0, −4).", "(b) Enter plot([cos(t), sin(t), t=-3.5..3.5], -1.5..1.5, -1.5..1.5); Squaring and adding gives x² + y² = 1.", "The parameter interval has length 7 > 2π, so it travels slightly more than one complete circle. Reversing sine and cosine keeps the same circle but reverses its direction.", "(c) Enter plots[implicitplot](x^2-y^2=1, x=-5..5, y=-5..5); This plots both branches of the implicit relation.", "Identify the hyperbola vertices (−1, 0), (1, 0), and asymptotes y = ±x. The two branches open left and right.", "Compare the command plots with the source context-menu plots. They show the same curves, although the automatic context-menu viewing ranges can differ."], "answer": "(a) Downward parabola, vertex (−2, 0). (b) Unit circle. (c) Hyperbola x² − y² = 1, vertices (±1, 0), asymptotes y = ±x.", "sourceClarification": "The printed interval [0, −4] is reversed. This learning command uses [−4, 0], matching the source graph. Printed commands and coordinate ordering remain in the lesson."};
math12MapleExample.diagram=MATH_12_DATA[1].sourcePages.find(page=>page.page===43).blocks.find(block=>block.caption==='Figure 2.25').diagram;
math12ParametricExamples.push(math12MapleExample);

const math12AnimationExample={"id": "we-2-source-24", "num": "24", "title": "Example 24", "problem": "Use Maple commands for (a) f(x) = x² − b and (b) the surface cos(tx) sin(ty).", "given": "The source commands animate b from −5 to 5 and t from 1 to 2.", "method": "Identify the plotted quantity and parameter, then compare representative frames.", "steps": ["(a) Use plots[animate](plot, [x^2-b, x=-10..10], b=-5..5); For each fixed b, the graph is a parabola with vertex (0, −b).", "At b = −5, 0, 5, the frames are y = x² + 5, y = x², y = x² − 5. Increasing b moves the parabola downward.", "(b) Interpret the displayed plot3d command as z = cos(tx) sin(ty), over −π ≤ x, y ≤ π.", "Use plots[animate]('plot3d', [cos(t*x)*sin(t*y), x=-Pi..Pi, y=-Pi..Pi], t=1..2);", "At t = 1, z = cos x sin y. Its values lie between −1 and 1; z(0, π/2) = 1 and z(0, −π/2) = −1. At t = 2, the surface has twice the spatial frequency in both directions.", "The context-menu commands add axis labels to the same mathematical plots. Compare the printed frames b = −5 and t = 1 with the digital source figures."], "answer": "(a) Parabolas with vertex (0, −b), moving downward as b increases. (b) Surface z = cos(tx) sin(ty), with printed frame t = 1 and animation parameter 1 ≤ t ≤ 2.", "sourceClarification": "The question’s coordinate notation and ranges differ from its commands. This learning solution follows the displayed commands; the original versions remain in the lesson."};
math12AnimationExample.diagram=math12Page44.blocks.find(block=>block.caption==='Figure 2.29').diagram;
math12ParametricExamples.push(math12AnimationExample);
math12ParametricExamples.forEach(example=>{
  example.solutionOrigin='SpaceBook learning enhancement';example.progressiveSolution=true;
  example.sourceReferences=[{class:12,subject:'Mathematics',pageStart:Number(example.num)>=24?43:Number(example.num)>=23?42:Number(example.num)>=21?41:Number(example.num)>=18?40:Number(example.num)>=15?39:example.num==='14'?38:37,pageEnd:Number(example.num)>=24?44:Number(example.num)>=23?43:Number(example.num)>=21?41:Number(example.num)>=18?40:Number(example.num)>=15?39:example.num==='14'?38:37,verification:'visually compared with JPG and full PDF'}];
  MATH_12_DATA[1].workedExamples=MATH_12_DATA[1].workedExamples.filter(existing=>existing.num!==example.num);
  const index=MATH_12_DATA[1].workedExamples.findIndex(existing=>Number(existing.num)>Number(example.num));
  MATH_12_DATA[1].workedExamples.splice(index<0 ? MATH_12_DATA[1].workedExamples.length : index,0,example);
});
"""
text += 'const math12SequenceLimitExamples='+json.dumps(SEQUENCE_LIMIT_EXAMPLES,ensure_ascii=False)+';\n'
text += """math12SequenceLimitExamples.forEach(example=>{
  MATH_12_DATA[1].workedExamples=MATH_12_DATA[1].workedExamples.filter(existing=>existing.num!==example.num);
  const index=MATH_12_DATA[1].workedExamples.findIndex(existing=>Number(existing.num)>Number(example.num));
  MATH_12_DATA[1].workedExamples.splice(index<0?MATH_12_DATA[1].workedExamples.length:index,0,example);
});\n"""
exercise22_data=[]
for index, question in enumerate(EX22_QUESTIONS):
    revision={'question':question,'sourceReferences':[{'page':44,'jpg':'026_page_2.jpg','verification':'visually compared with JPG and full PDF'}],'diagram':None,'sourceQuestionBlocks':[],'options':[],'solution':'','answer':'','progressiveSolution':False,'solutionStatus':'partial: source question verified; learning solution and graph review pending'}
    if index < len(EX22_STEPS):
        revision.update({'steps':EX22_STEPS[index],'answer':EX22_ANSWERS[index],'solution':'\n'.join(EX22_STEPS[index]),'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','solutionStatus':'worked and checked','answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':168,'printedPage':327,'scope':'Exercise 2.2 Questions 1–3','verification':'visually inspected'}})
    if index in EX22_SOLUTION_BLOCKS: revision['solutionBlocks']=EX22_SOLUTION_BLOCKS[index]
    if index==0: revision['sourceClarification']='The source answer key calls (b) algebraic and (g) explicit. The learning classifications give their more specific types. The circle in (e) is an implicit equation, not a single-valued function y of x.'
    if index==1: revision['sourceClarification']='The answer key rounds to one decimal place (100, 70.9, 50.3, 11.6 g). This solution reports two decimal places.'
    if index==2: revision['sourceClarification']='The answer key shows wider coordinate axes. These learning graphs restrict the curves to the requested closed intervals, with both endpoints included.'
    if index in EX22_CLARIFICATIONS: revision['sourceClarification']=EX22_CLARIFICATIONS[index]
    if index>=3 and index<=6: revision['answerKeyReference']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPages':[168,169] if index==4 else [168] if index==3 else [169],'printedPages':[328,329] if index==4 else [328] if index==3 else [329,330] if index==5 else [330],'scope':'Exercise 2.2 Question '+str(index+1),'verification':'visually inspected; mismatches recorded separately'}
    if index==7: revision.pop('answerKeyReference',None)
    exercise22_data.append(revision)
text += 'const math12Exercise22Revision='+json.dumps(exercise22_data,ensure_ascii=False)+';\n'
text += """math12Exercise22Revision.forEach((revision,index)=>{const problem=MATH_12_DATA[1].exercises[1].problems[index];problem.unreviewedSolution={solution:problem.solution,answer:problem.answer,diagram:problem.diagram};Object.assign(problem,revision);});
MATH_12_DATA[1].exercises[1].pageStart=44;MATH_12_DATA[1].exercises[1].pageEnd=44;
"""
text += '\nconst math12IntervalExamples=[{"id": "we-2-source-24-intervals", "num": "24", "title": "Example 24 — Intervals", "problem": "Represent (a) [−2, ∞), (b) [4, ∞), (c) [−2, 1] on number lines.", "given": "Three intervals, including two unbounded intervals.", "method": "Mark included endpoints with solid dots and shade the interval.", "steps": ["(a) [−2, ∞) means x ≥ −2. Put a solid dot at −2 and draw a ray to the right.", "(b) [4, ∞) means x ≥ 4. Put a solid dot at 4 and draw a ray to the right.", "(c) [−2, 1] means −2 ≤ x ≤ 1. Put solid dots at both −2 and 1 and shade the segment between them.", "Infinity is not an endpoint number. Use a parenthesis next to ∞, and use an arrow on the number line to show that the ray continues."], "answer": "(a) x ≥ −2; (b) x ≥ 4; (c) −2 ≤ x ≤ 1.", "solutionBlocks": [{"type": "diagram", "id": "math12-source-interval24-a", "caption": "Example 24 (a), continued", "diagram": {"type": "source-number-line", "title": "Example 24 (a), continued", "xMin": -5, "xMax": 5, "ticks": [-4, -3, -2, -1, 0, 1, 2, 3, 4], "left": -2, "leftClosed": true, "right": null}}, {"type": "diagram", "id": "math12-source-interval24-b", "caption": "Example 24 (b)", "diagram": {"type": "source-number-line", "title": "Example 24 (b)", "xMin": -0.5, "xMax": 8.5, "ticks": [0, 1, 2, 3, 4, 5, 6, 7, 8], "left": 4, "leftClosed": true, "right": null}}, {"type": "diagram", "id": "math12-source-interval24-c", "caption": "Example 24 (c)", "diagram": {"type": "source-number-line", "title": "Example 24 (c)", "xMin": -3, "xMax": 4, "ticks": [-2, -1, 0, 1, 2, 3], "left": -2, "leftClosed": true, "right": 1, "rightClosed": true}}], "sourceClarification": "The textbook prints Example 24 again here, after its animation Example 24. This distinct source example keeps its printed number.", "progressiveSolution": true, "solutionOrigin": "SpaceBook learning enhancement", "sourceReferences": [{"pageStart": 45, "pageEnd": 46, "verification": "visually compared with JPG and full PDF"}]}, {"id": "we-2-source-25", "num": "25", "title": "Example 25", "problem": "Use the three given number lines to indicate the interval notation.", "sourceQuestionBlocks": [{"type": "diagram", "id": "math12-source-interval25-a", "caption": "Example 25 (a)", "diagram": {"type": "source-number-line", "title": "Example 25 (a)", "xMin": -6, "xMax": 6, "ticks": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], "left": -5, "leftClosed": false, "right": 3, "rightClosed": false}}, {"type": "diagram", "id": "math12-source-interval25-b", "caption": "Example 25 (b)", "diagram": {"type": "source-number-line", "title": "Example 25 (b)", "xMin": 2.5, "xMax": 10.5, "ticks": [3, 4, 5, 6, 7, 8, 9, 10], "left": 4, "leftClosed": true, "right": 7, "rightClosed": true}}, {"type": "diagram", "id": "math12-source-interval25-c", "caption": "Example 25 (c)", "diagram": {"type": "source-number-line", "title": "Example 25 (c)", "xMin": -5, "xMax": 3, "ticks": [-4, -3, -2, -1, 0, 1, 2], "left": null, "right": -1, "rightClosed": true, "extraPoints": [-4]}}], "given": "Open or closed endpoint marks and the shaded regions.", "method": "Read endpoint inclusion, then choose parentheses or square brackets.", "steps": ["(a) The segment lies between −5 and 3 with open endpoints, so −5 < x < 3 and the interval is (−5, 3).", "(b) The solid dots at 4 and 7 include both ends: 4 ≤ x ≤ 7, or [4, 7].", "(c) The ray continues left without bound and ends with a solid dot at −1: x ≤ −1, or (−∞, −1].", "A solid marked point inside a shaded ray, such as −4 in (c), does not create another interval endpoint. Infinity always uses a parenthesis."], "answer": "(a) (−5, 3); (b) [4, 7]; (c) (−∞, −1].", "progressiveSolution": true, "solutionOrigin": "SpaceBook learning enhancement", "sourceReferences": [{"pageStart": 46, "pageEnd": 46, "verification": "visually compared with JPG and full PDF"}]}];\nMATH_12_DATA[1].workedExamples=MATH_12_DATA[1].workedExamples.filter(example=>example.num!==\'25\');\nconst math12IntervalIndex=MATH_12_DATA[1].workedExamples.findIndex(example=>Number(example.num)>25);\nMATH_12_DATA[1].workedExamples.splice(math12IntervalIndex<0?MATH_12_DATA[1].workedExamples.length:math12IntervalIndex,0,...math12IntervalExamples);\n'
exercise23_data=[]
for index, question in enumerate(EX23_QUESTIONS):
    revision={'id':'ex-2-3-'+('project' if index==6 else 'q'+str(index+1)),'qNo':'Project' if index==6 else str(index+1),'question':question,'steps':EX23_STEPS[index],'solution':'\n'.join(EX23_STEPS[index]),'answer':EX23_ANSWERS[index],'diagram':None,'sourceQuestionBlocks':EX23_PROJECT if index==6 else [],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','solutionStatus':'partial: first project model legibility pending' if index==6 else 'worked and checked','sourceReferences':[{'page':56,'jpg':'032_page_2.jpg','verification':'visually compared with JPG and full PDF; project coefficient uncertainty separately recorded'}]}
    if index in EX23_CLARIFICATIONS: revision['sourceClarification']=EX23_CLARIFICATIONS[index]
    if index in [0,1,2,3,5]: revision['answerKeyReference']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':331,'scope':'Exercise 2.3 Question '+str(index+1),'verification':'visually inspected; discrepancies stated separately'}
    exercise23_data.append(revision)
text += 'const math12Exercise23Revision='+json.dumps(exercise23_data,ensure_ascii=False)+';\n'
text += """MATH_12_DATA[1].exercises[2].problems=math12Exercise23Revision.map((revision,index)=>({...revision,unreviewedSolution:MATH_12_DATA[1].exercises[2].problems[index]}));
MATH_12_DATA[1].exercises[2].pageStart=56;MATH_12_DATA[1].exercises[2].pageEnd=56;
"""
exercise24_data=[]
for index, question in enumerate(EX24_QUESTIONS):
    revision={'id':'ex-2-4-'+('project' if index==7 else 'q'+str(index+1)),'qNo':'Project' if index==7 else str(index+1),'question':question,'steps':EX24_STEPS[index],'solution':'\n'.join(EX24_STEPS[index]),'answer':EX24_ANSWERS[index],'diagram':None,'sourceQuestionBlocks':EX24_BLOCKS[index],'solutionBlocks':EX24_SOLUTIONS[index],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','solutionStatus':'worked and checked','sourceReferences':[{'page':59 if index==7 else 60,'jpg':'034_page_1.jpg' if index==7 else '034_page_2.jpg','verification':'visually compared with JPG and full PDF'}]}
    if index in EX24_CLARIFICATIONS: revision['sourceClarification']=EX24_CLARIFICATIONS[index]
    if index<7: revision['answerKeyReference']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':331,'scope':'Exercise 2.4 Question '+str(index+1),'verification':'visually inspected; Question 7 discrepancy separately explained'}
    exercise24_data.append(revision)
text += 'const math12Exercise24Revision='+json.dumps(exercise24_data,ensure_ascii=False)+';\n'
text += """MATH_12_DATA[1].exercises[3].problems=math12Exercise24Revision.map((revision,index)=>({...revision,unreviewedSolution:MATH_12_DATA[1].exercises[3].problems[index]}));
MATH_12_DATA[1].exercises[3].pageStart=59;MATH_12_DATA[1].exercises[3].pageEnd=60;
"""
review2_data=[]
for index, question in enumerate(REVIEW2_QUESTIONS):
    revision={'id':'ex-2-review-'+str(index+1),'qNo':REVIEW2_NUMS[index],'question':question,'sourceQuestionBlocks':[REVIEW2_BLOCKS[index]],'steps':REVIEW2_STEPS[index],'solution':'\n'.join(REVIEW2_STEPS[index]),'answer':'Option ('+REVIEW2_LETTERS[index]+')'+(' — printed (b) is identical' if index==2 else ''),'diagram':None,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','solutionStatus':'worked and checked','sourceReferences':[{'page':61,'jpg':'035_page_1.jpg','verification':'visually compared with JPG and full PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':331,'scope':'Review Exercise 2, Question 1 ('+REVIEW2_NUMS[index]+')','verification':'visually inspected; duplicate option and approximation caveats stated separately'}}
    if index in REVIEW2_CLARIFICATIONS: revision['sourceClarification']=REVIEW2_CLARIFICATIONS[index]
    review2_data.append(revision)
text += 'const math12Review2Revision='+json.dumps(review2_data,ensure_ascii=False)+';\n'
text += """MATH_12_DATA[1].exercises[4].problems=math12Review2Revision.map((revision,index)=>({...revision,unreviewedSolution:MATH_12_DATA[1].exercises[4].problems[index]}));
MATH_12_DATA[1].exercises[4].title='Review Exercise 2';MATH_12_DATA[1].exercises[4].pageStart=61;MATH_12_DATA[1].exercises[4].pageEnd=61;
"""
text += """MATH_12_DATA[1].sourceSummaryBlocks=MATH_12_DATA[1].sourcePages.find(page=>page.page===62).blocks;
MATH_12_DATA[1].sourceSummaryReferences=[{page:62,jpg:'035_page_2.jpg',verification:'visually compared with JPG and full PDF'}];
"""
text += """const math12DerivativeIntro=MATH_12_DATA[2].sections[0];
math12DerivativeIntro.unreviewedTheory='';
math12DerivativeIntro.sourceBlocks=MATH_12_DATA[2].sourcePages.filter(page=>page.page>=64&&page.page<=69).flatMap(page=>page.blocks);
math12DerivativeIntro.theory=math12DerivativeIntro.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12DerivativeIntro.unreviewedTheory;
math12DerivativeIntro.sourceReferences=MATH_12_DATA[2].sourcePages.filter(page=>page.page>=64&&page.page<=69).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));
"""
text += """const math12DerivativeTheorems=MATH_12_DATA[2].sections[1];
math12DerivativeTheorems.unreviewedTheory='';
math12DerivativeTheorems.sourceBlocks=MATH_12_DATA[2].sourcePages.filter(page=>page.page>=71&&page.page<=74).flatMap(page=>page.blocks);
math12DerivativeTheorems.sourceReferences=MATH_12_DATA[2].sourcePages.filter(page=>page.page>=71&&page.page<=74).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));
math12DerivativeTheorems.theory=math12DerivativeTheorems.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12DerivativeTheorems.unreviewedTheory;
"""
text += "const math12Applications=MATH_12_DATA[2].sections[2];\nmath12Applications.unreviewedTheory=math12Applications.theory.slice(math12Applications.theory.indexOf('Find the derivative of the following functions'));\nmath12Applications.sourceBlocks=MATH_12_DATA[2].sourcePages.find(page=>page.page===75).blocks.slice(5);\nmath12Applications.sourceReferences=[{page:75,jpg:'042_page_1.jpg',verification:'visually compared with JPG and full PDF'}];\nmath12Applications.theory=math12Applications.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Applications.unreviewedTheory;\nmath12DerivativeTheorems.sourceBlocks.push(...MATH_12_DATA[2].sourcePages.find(page=>page.page===75).blocks.slice(0,5));\nmath12DerivativeTheorems.sourceReferences.push({page:75,jpg:'042_page_1.jpg',verification:'visually compared with JPG and full PDF'});\nmath12DerivativeTheorems.theory=math12DerivativeTheorems.sourceBlocks.map(math12BlockText).join('\\n\\n');\n"
text += "const math12Chain=MATH_12_DATA[2].sections[3];\nmath12Chain.unreviewedTheory=math12Chain.theory.slice(math12Chain.theory.length);\nmath12Chain.sourceBlocks=MATH_12_DATA[2].sourcePages.filter(page=>page.page>=77&&page.page<=81).flatMap(page=>page.blocks);\nmath12Chain.sourceReferences=MATH_12_DATA[2].sourcePages.filter(page=>page.page>=77&&page.page<=81).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));\nmath12Chain.theory=math12Chain.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Chain.unreviewedTheory;\n"
text += "const math12Trig=MATH_12_DATA[2].sections[4];\nmath12Trig.unreviewedTheory=math12Trig.theory.slice(math12Trig.theory.indexOf('Derivative of cos'));\nmath12Trig.sourceBlocks=MATH_12_DATA[2].sourcePages.find(page=>page.page===82).blocks.slice(8);\nmath12Trig.sourceReferences=[{page:82,jpg:'045_page_2.jpg',verification:'visually compared with JPG and full PDF'}];\nmath12Trig.theory=math12Trig.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Trig.unreviewedTheory;\nmath12Chain.sourceBlocks=math12Chain.sourceBlocks.filter(block=>!(block.type==='heading'&&block.text==='Exercise 3.3')&&!(/^\\d\\. Find the derivative|^2\\. Determine the derivative|^3\\. Find dy/.test(block.text||'')));\nmath12Chain.theory=math12Chain.sourceBlocks.map(math12BlockText).join('\\n\\n');\n"
text += "math12Trig.unreviewedTheory=math12Trig.unreviewedTheory.slice(math12Trig.unreviewedTheory.indexOf('Use of first principle'));\nmath12Trig.sourceBlocks.push(...MATH_12_DATA[2].sourcePages.filter(page=>page.page>=83&&page.page<=88).flatMap(page=>page.blocks));\nmath12Trig.sourceReferences.push(...MATH_12_DATA[2].sourcePages.filter(page=>page.page>=83&&page.page<=88).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'})));\nmath12Trig.theory=math12Trig.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Trig.unreviewedTheory;\n"
text += "math12Trig.unreviewedTheory='';\nmath12Trig.sourceBlocks.push(...MATH_12_DATA[2].sourcePages.find(page=>page.page===89).blocks,...MATH_12_DATA[2].sourcePages.find(page=>page.page===90).blocks.slice(0,4));\nmath12Trig.sourceReferences.push({page:89,jpg:'049_page_1.jpg',verification:'visually compared with JPG and full PDF'},{page:90,jpg:'049_page_2.jpg',verification:'Example 18 conclusion visually compared with JPG and full PDF'});\nmath12Trig.theory=math12Trig.sourceBlocks.map(math12BlockText).join('\\n\\n');\nconst math12Exponential=MATH_12_DATA[2].sections[5];\nmath12Exponential.unreviewedTheory=math12Exponential.theory.slice(math12Exponential.theory.indexOf('Derivative of'));\nmath12Exponential.sourceBlocks=MATH_12_DATA[2].sourcePages.find(page=>page.page===90).blocks.slice(-2);\nmath12Exponential.sourceReferences=[{page:90,jpg:'049_page_2.jpg',verification:'section introduction visually compared with JPG and full PDF'}];\nmath12Exponential.theory=math12Exponential.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Exponential.unreviewedTheory;\n"
text += "math12Exponential.unreviewedTheory='';\nmath12Exponential.sourceBlocks.push(...MATH_12_DATA[2].sourcePages.filter(page=>page.page>=91&&page.page<=93).flatMap(page=>page.page===93?page.blocks.slice(0,-2):page.blocks));\nmath12Exponential.sourceReferences.push(...MATH_12_DATA[2].sourcePages.filter(page=>page.page>=91&&page.page<=93).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'})));\nmath12Exponential.theory=math12Exponential.sourceBlocks.map(math12BlockText).join('\\n\\n');\nconst math12Hyperbolic=MATH_12_DATA[2].sections[6];\nmath12Hyperbolic.unreviewedTheory=math12Hyperbolic.theory.slice(math12Hyperbolic.theory.indexOf('Derivative of'));\nmath12Hyperbolic.sourceBlocks=MATH_12_DATA[2].sourcePages.find(page=>page.page===93).blocks.slice(-2);\nmath12Hyperbolic.sourceReferences=[{page:93,jpg:'051_page_1.jpg',verification:'section introduction visually compared with JPG and full PDF'}];\nmath12Hyperbolic.theory=math12Hyperbolic.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Hyperbolic.unreviewedTheory;\n"
text += "math12Hyperbolic.unreviewedTheory=math12Hyperbolic.unreviewedTheory.slice(math12Hyperbolic.unreviewedTheory.indexOf('This result'));\nmath12Hyperbolic.sourceBlocks.push(...MATH_12_DATA[2].sourcePages.filter(page=>page.page>=94&&page.page<=96).flatMap(page=>page.blocks));\nmath12Hyperbolic.sourceReferences.push(...MATH_12_DATA[2].sourcePages.filter(page=>page.page>=94&&page.page<=96).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'})));\nmath12Hyperbolic.theory=math12Hyperbolic.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Hyperbolic.unreviewedTheory;\n"
text += "const math12Source97=MATH_12_DATA[2].sourcePages.find(page=>page.page===97);const math12MapleStart=math12Source97.blocks.findIndex(block=>block.type==='heading'&&block.text.startsWith('3.8'));\nmath12Hyperbolic.unreviewedTheory='';math12Hyperbolic.sourceBlocks.push(...math12Source97.blocks.slice(0,math12MapleStart));math12Hyperbolic.sourceReferences.push({page:97,jpg:math12Source97.file,verification:'visually compared with JPG and full PDF'});math12Hyperbolic.theory=math12Hyperbolic.sourceBlocks.map(math12BlockText).join('\\n\\n');\nconst math12Source98=MATH_12_DATA[2].sourcePages.find(page=>page.page===98);const math12MapleEnd=math12Source98.blocks.findIndex(block=>block.type==='heading'&&block.text==='Exercise 3.5');const math12MapleBlocks=math12Source97.blocks.slice(math12MapleStart).concat(math12Source98.blocks.slice(0,math12MapleEnd));MATH_12_DATA[2].sections.push({id:'sec-3-8',title:'3.8 MAPLE Command diff to Differentiate a Function',sourceBlocks:math12MapleBlocks,sourceReferences:[{page:97,jpg:math12Source97.file,verification:'visually compared with JPG and full PDF'},{page:98,jpg:math12Source98.file,verification:'visually compared with JPG and full PDF'}],theory:math12MapleBlocks.map(math12BlockText).join('\\n\\n'),unreviewedTheory:''});\nconst math12Source100=MATH_12_DATA[2].sourcePages.find(page=>page.page===100);MATH_12_DATA[2].sourceSummaryBlocks=math12Source100.blocks.slice(4);MATH_12_DATA[2].sourceSummaryReferences=[{page:100,jpg:math12Source100.file,verification:'visually compared with JPG and full PDF'}];\n"
text += 'const math12DerivativeExamples='+json.dumps(DIFFERENTIATION_EXAMPLES,ensure_ascii=False)+';\n'
text += 'math12DerivativeExamples.forEach(revision=>{const examples=MATH_12_DATA[2].workedExamples;const existing=examples.find(example=>example.num===revision.num);if(existing){Object.assign(existing,revision);}else{const index=examples.findIndex(example=>Number(example.num)>Number(revision.num));examples.splice(index<0?examples.length:index,0,revision);}});\n'
text += 'math12DerivativeExamples.forEach(revision=>{const chapter=MATH_12_DATA[2];const duplicates=chapter.workedExamples.filter(example=>example.num===revision.num&&example.id!==revision.id);chapter.unreviewedDuplicateExamples=(chapter.unreviewedDuplicateExamples||[]).concat(duplicates);chapter.workedExamples=chapter.workedExamples.filter(example=>example.num!==revision.num||example.id===revision.id);});\n'

from math12_reviewed_exercise34 import QUESTIONS as EX34_QUESTIONS, STEPS as EX34_STEPS, ANSWERS as EX34_ANSWERS, CLARIFICATIONS as EX34_CLARIFICATIONS
ex34=[]
for i,q in enumerate(EX34_QUESTIONS):
    revision={'id':'ex-3-4-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX34_STEPS[i],'solution':'\n'.join(EX34_STEPS[i]),'answer':EX34_ANSWERS[i],'progressiveSolution':True,'solutionStatus':'worked and checked','solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':90,'jpg':'049_page_2.jpg','verification':'visually compared with JPG and full PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPages':[333,334],'scope':'Exercise 3.4 Questions 1–5 only; answer pages not transcribed or marked complete'}}
    if i in EX34_CLARIFICATIONS: revision['sourceClarification']=EX34_CLARIFICATIONS[i]
    ex34.append(revision)
text+='const math12Exercise34='+json.dumps(ex34,ensure_ascii=False)+';\nMATH_12_DATA[2].exercises[3].unreviewedProblems=MATH_12_DATA[2].exercises[3].problems;MATH_12_DATA[2].exercises[3].problems=math12Exercise34;\n'
text+="MATH_12_DATA[2].exercises.slice(0,4).forEach((exercise,index)=>{exercise.title=exercise.exercise='Exercise 3.'+(index+1);});\n"
from math12_reviewed_exercise35 import QUESTIONS as EX35_QUESTIONS, STEPS as EX35_STEPS, ANSWERS as EX35_ANSWERS, CLARIFICATIONS as EX35_CLARIFICATIONS
ex35=[]
for i,q in enumerate(EX35_QUESTIONS):
    revision={'id':'ex-3-5-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX35_STEPS[i],'solution':'\n'.join(EX35_STEPS[i]),'answer':EX35_ANSWERS[i],'progressiveSolution':True,'solutionStatus':'worked and checked','solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':98 if i<4 else 99,'jpg':'053_page_2.jpg' if i<4 else '054_page_1.jpg','verification':'visually compared with JPG and full PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPage':334,'scope':'Exercise 3.5 Questions 1–6 only; no separate Question 7 key, answer page not transcribed or marked complete'}}
    if i in EX35_CLARIFICATIONS:revision['sourceClarification']=EX35_CLARIFICATIONS[i]
    if i==6:revision.pop('answerKeyReference')
    ex35.append(revision)
review3=[]
for num,q,options,answer,steps in REVIEW3_ITEMS:
    question=q+' '+' '.join('('+letter+') '+option for letter,option in zip('abcd',options))
    revision={'id':'ex-3-review-'+num,'qNo':num,'question':question,'steps':steps,'solution':'\n'.join(steps),'answer':'Option ('+answer+')'+(' — also (a) on t > 0' if num=='vi' else ' — also (d)' if num=='vii' else ''),'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','solutionStatus':'worked and checked','sourceReferences':[{'page':99,'jpg':'054_page_1.jpg','verification':'complete question and all four options visually compared with JPG and full PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPage':334,'scope':'Review Exercise 3 Question 1 ('+num+'); answer page not transcribed or marked complete'}}
    if num in ['vi','vii']:revision['sourceClarification']='Two printed options are equivalent on the stated derivative domain; the key-selected option and the equivalent option are both identified.'
    review3.append(revision)
text+='const math12Exercise35='+json.dumps(ex35,ensure_ascii=False)+';\nMATH_12_DATA[2].exercises[4].unreviewedProblems=MATH_12_DATA[2].exercises[4].problems;MATH_12_DATA[2].exercises[4].problems=math12Exercise35;MATH_12_DATA[2].exercises[4].title=MATH_12_DATA[2].exercises[4].exercise="Exercise 3.5";\n'
BALLOON_PROJECT['solution']='\n'.join(BALLOON_PROJECT['steps'])
text+='MATH_12_DATA[2].exercises[5].problems=['+json.dumps(BALLOON_PROJECT,ensure_ascii=False)+'];MATH_12_DATA[2].exercises[5].title=MATH_12_DATA[2].exercises[5].exercise="Project — Spherical Balloon";\n'
text+='MATH_12_DATA[2].exercises[6].problems='+json.dumps(review3,ensure_ascii=False)+';MATH_12_DATA[2].exercises[6].title=MATH_12_DATA[2].exercises[6].exercise="Review Exercise 3";\n'
exercise31_data=[]
text += 'const math12Exercise32Questions='+json.dumps(EX32_QUESTIONS,ensure_ascii=False)+';\n'
text += "math12Exercise32Questions.forEach((question,index)=>{const ex=MATH_12_DATA[2].exercises[1];ex.problems[index]={id:'ex-3-2-q'+(index+1),qNo:String(index+1),question,steps:[],answer:'',solution:'',progressiveSolution:false,solutionStatus:'partial: Source question verified; learning solution pending',unreviewedSolution:ex.problems[index],sourceReferences:[{page:76,jpg:'042_page_2.jpg',verification:'visually compared with JPG and full PDF'}]};});\n"
text += 'MATH_12_DATA[2].exercises[1].sourceContextBlocks=MATH_12_DATA[2].sourcePages.find(page=>page.page===76).blocks.slice(0,5).concat(MATH_12_DATA[2].sourcePages.find(page=>page.page===76).blocks.slice(11));\n'
text += 'const math12Exercise32Steps='+json.dumps(EX32_STEPS,ensure_ascii=False)+';\nconst math12Exercise32Answers='+json.dumps(EX32_ANSWERS,ensure_ascii=False)+';\n'
text += "MATH_12_DATA[2].exercises[1].problems.forEach((p,index)=>Object.assign(p,{steps:math12Exercise32Steps[index],answer:math12Exercise32Answers[index],solution:math12Exercise32Steps[index].join('\\n'),progressiveSolution:true,solutionOrigin:'SpaceBook learning enhancement',solutionStatus:'worked and checked',answerKeyReference:{pdf:'Math Book for 12 class KPTBB.pdf',pdfPage:170,printedPage:332,scope:'Exercise 3.2 Questions 1–5 only; answer page not transcribed'}}));MATH_12_DATA[2].exercises[1].problems[1].sourceClarification='The answer key prints the correct 9x² + 2x − 6, followed by an unrelated extra equality copied from Question 1(d). The independent product-rule solution uses the correct first result.';\n"
text += 'MATH_12_DATA[2].exercises[1].problems.push('+json.dumps(EX32_PROJECT,ensure_ascii=False)+');\n'
from math12_reviewed_exercise33 import QUESTIONS as EX33_QUESTIONS, STEPS as EX33_STEPS, ANSWERS as EX33_ANSWERS, CLARIFICATIONS as EX33_CLARIFICATIONS
ex33=[]
for i,q in enumerate(EX33_QUESTIONS):
    revision={'id':'ex-3-3-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX33_STEPS[i],'solution':'\n'.join(EX33_STEPS[i]),'answer':EX33_ANSWERS[i],'progressiveSolution':True,'solutionStatus':'worked and checked','solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':81 if i<3 else 82,'verification':'visually compared with JPG and full PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPage':333,'scope':'Exercise 3.3 only; key discrepancies independently corrected'}}
    if i in EX33_CLARIFICATIONS: revision['sourceClarification']=EX33_CLARIFICATIONS[i]
    if i==8: revision['solutionBlocks']=[{'type':'diagram','caption':'Source boat diagram, reconstructed digitally','diagram':{'type':'source-motor-boats','title':'Motor boats'}}]
    ex33.append(revision)
text += 'const math12Exercise33='+json.dumps(ex33,ensure_ascii=False)+';\n'
text += "MATH_12_DATA[2].exercises[2].unreviewedProblems=MATH_12_DATA[2].exercises[2].problems;MATH_12_DATA[2].exercises[2].problems=math12Exercise33;MATH_12_DATA[2].exercises[2].title='Exercise 3.3';\n"
for index, question in enumerate(EX31_QUESTIONS):
    revision={'id':'ex-3-1-q'+str(index+1),'qNo':str(index+1),'question':question,'steps':EX31_STEPS[index],'solution':'\n'.join(EX31_STEPS[index]),'answer':EX31_ANSWERS[index],'diagram':None,'solutionBlocks':EX31_SOLUTIONS[index],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','solutionStatus':'worked and checked','sourceReferences':[{'page':70,'jpg':'039_page_2.jpg','verification':'visually compared with JPG and full PDF'}]}
    exercise31_data.append(revision)
text += 'const math12Exercise31Revision='+json.dumps(exercise31_data,ensure_ascii=False)+';\n'
text += """MATH_12_DATA[2].exercises[0].problems=math12Exercise31Revision.map((revision,index)=>({...revision,unreviewedSolution:MATH_12_DATA[2].exercises[0].problems[index]}));
MATH_12_DATA[2].exercises[0].sourceContextBlocks=MATH_12_DATA[2].sourcePages.find(page=>page.page===70).blocks.slice(-4);
MATH_12_DATA[2].exercises[0].pageStart=70;MATH_12_DATA[2].exercises[0].pageEnd=70;
"""
text += 'const math12HigherExamples='+json.dumps(HIGHER_EXAMPLES,ensure_ascii=False)+';\n'
text += """const math12Higher=MATH_12_DATA[3].sections[0];
const math12HigherTail=math12Higher.theory.indexOf('The second implicit derivative');
math12Higher.unreviewedTheory='';
math12Higher.sourceBlocks=MATH_12_DATA[3].sourcePages.filter(page=>page.page<=108).flatMap(page=>page.blocks);
math12Higher.sourceReferences=MATH_12_DATA[3].sourcePages.filter(page=>page.page<=108).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));
math12Higher.theory=math12Higher.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Higher.unreviewedTheory;
math12HigherExamples.forEach(revision=>{const chapter=MATH_12_DATA[3];const existing=chapter.workedExamples.find(example=>example.num===revision.num);if(existing)Object.assign(existing,revision);else{const index=chapter.workedExamples.findIndex(example=>Number(example.num)>Number(revision.num));chapter.workedExamples.splice(index<0?chapter.workedExamples.length:index,0,revision);}const duplicates=chapter.workedExamples.filter(example=>example.num===revision.num&&example.id!==revision.id);chapter.unreviewedDuplicateExamples=(chapter.unreviewedDuplicateExamples||[]).concat(duplicates);chapter.workedExamples=chapter.workedExamples.filter(example=>example.num!==revision.num||example.id===revision.id);});
"""
ex41=[]
for i,q in enumerate(EX41_QUESTIONS):
    revision={'id':'ex-4-1-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX41_STEPS[i],'solution':'\n'.join(EX41_STEPS[i]),'answer':EX41_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':109,'jpg':'059_page_1.jpg','verification':'source question and derivative order visually compared with JPG and PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPages':[171,172],'printedPages':[334,335],'scope':'Exercise 4.1 Questions 1–6 only; answer pages not transcribed or marked complete'}}
    if i in EX41_CLARIFICATIONS:revision['sourceClarification']=EX41_CLARIFICATIONS[i]
    ex41.append(revision)
text+='const math12Exercise41='+json.dumps(ex41+EX41_PROJECTS,ensure_ascii=False)+';\n'
text+="const math12Ex41=MATH_12_DATA[3].exercises.find(ex=>ex.title==='Exercise 4.1');math12Ex41.unreviewedProblems=math12Ex41.problems;math12Ex41.problems=math12Exercise41;math12Ex41.pageStart=math12Ex41.pageEnd=109;MATH_12_DATA[3].exercises=MATH_12_DATA[3].exercises.filter(ex=>ex!==math12Ex41);MATH_12_DATA[3].exercises.unshift(math12Ex41);\n"
text+="const math12Taylor=MATH_12_DATA[3].sections[1];math12Taylor.unreviewedTheory='';math12Taylor.sourceBlocks=MATH_12_DATA[3].sourcePages.filter(page=>page.page>=110&&page.page<=114).flatMap(page=>page.blocks);math12Taylor.sourceReferences=MATH_12_DATA[3].sourcePages.filter(page=>page.page>=110&&page.page<=114).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));math12Taylor.theory=math12Taylor.sourceBlocks.map(math12BlockText).join('\\n\\n');\n"
text+='MATH_12_DATA[3].exercises.push({id:"ex-4-taylor-challenge",title:"Challenge — Taylor Series at 3",exercise:"Challenge — Taylor Series at 3",pageStart:114,pageEnd:114,problems:['+json.dumps(TAYLOR_CHALLENGE,ensure_ascii=False)+']});\n'
text+="const math12Tangent=MATH_12_DATA[3].sections[2];math12Tangent.unreviewedTheory='';math12Tangent.sourceBlocks=MATH_12_DATA[3].sourcePages.filter(page=>page.page>=115&&page.page<=117).flatMap(page=>page.blocks);math12Tangent.sourceReferences=MATH_12_DATA[3].sourcePages.filter(page=>page.page>=115&&page.page<=117).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));math12Tangent.theory=math12Tangent.sourceBlocks.map(math12BlockText).join('\\n\\n');\n"
ex42=[]
for i,q in enumerate(EX42_QUESTIONS):
    revision={'id':'ex-4-2-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX42_STEPS[i],'solution':'\n'.join(EX42_STEPS[i]),'answer':EX42_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':118,'jpg':'063_page_2.jpg','verification':'all source subparts and coefficients visually checked'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':172,'printedPage':335,'scope':'Exercise 4.2 Questions 1–8 only; answer page not transcribed or marked complete'}}
    if i in EX42_CLARIFICATIONS:revision['sourceClarification']=EX42_CLARIFICATIONS[i]
    ex42.append(revision)
text+='const math12Exercise42='+json.dumps(ex42,ensure_ascii=False)+';\n'
text+="const math12Ex42=MATH_12_DATA[3].exercises.find(ex=>ex.title==='Exercise 4.2');math12Ex42.unreviewedProblems=math12Ex42.problems;math12Ex42.problems=math12Exercise42;math12Ex42.pageStart=math12Ex42.pageEnd=118;math12Ex42.sourceContextBlocks=MATH_12_DATA[3].sourcePages.find(page=>page.page===118).blocks.slice(9);\n"
text+="const math12Extrema=MATH_12_DATA[3].sections[3];const math12ExtremaTail=math12Extrema.theory.indexOf('second derivative');math12Extrema.unreviewedTheory='';math12Extrema.sourceBlocks=MATH_12_DATA[3].sourcePages.filter(page=>page.page>=119&&page.page<=126).flatMap(page=>page.page===126?page.blocks.slice(0,page.blocks.findIndex(block=>block.type==='heading'&&block.text==='Exercise 4.3')):page.blocks);math12Extrema.sourceReferences=MATH_12_DATA[3].sourcePages.filter(page=>page.page>=119&&page.page<=126).map(page=>({page:page.page,jpg:page.file,verification:'visually compared with JPG and full PDF'}));math12Extrema.theory=math12Extrema.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Extrema.unreviewedTheory;\n"
ex43=[]
for i,q in enumerate(EX43_QUESTIONS):
    revision={'id':'ex-4-3-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX43_STEPS[i],'solution':'\n'.join(EX43_STEPS[i]),'answer':EX43_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':126 if i<2 else 127,'jpg':'067_page_2.jpg' if i<2 else '068_page_1.jpg','verification':'all source question subparts and exponents checked against JPG/PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':172,'printedPages':[335,336],'scope':'Exercise 4.3 Questions 1–10 only; source mismatches separately clarified, answer pages not transcribed or marked complete'}}
    if i in EX43_CLARIFICATIONS:revision['sourceClarification']=EX43_CLARIFICATIONS[i]
    if i==3:revision['solutionBlocks']=EX43_GRAPHS
    ex43.append(revision)
text+='const math12Exercise43='+json.dumps(ex43,ensure_ascii=False)+';\n'
text+="const math12Ex43=MATH_12_DATA[3].exercises.find(ex=>ex.title==='Exercise 4.3');math12Ex43.unreviewedProblems=math12Ex43.problems;math12Ex43.problems=math12Exercise43;math12Ex43.pageStart=126;math12Ex43.pageEnd=127;\n"
review4=[]
for num,q,options,answer,steps in REVIEW4_ITEMS:
    revision={'id':'ex-4-review-'+num,'qNo':num,'question':q+' '+' '.join('('+letter+') '+opt for letter,opt in zip('abcd',options)),'steps':steps,'solution':'\n'.join(steps),'answer':'Option ('+answer+')','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':128,'jpg':'068_page_2.jpg','verification':'all source question text and four choices visually compared with JPG/PDF'}],'answerKeyReference':{'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':172,'printedPage':336,'scope':'Review Exercise 4 Question 1 ('+num+') only; answer page not transcribed or marked complete'}}
    if num=='vi':revision['sourceClarification']='Key-intended (b) needs f′(x₀) instead of the printed f′(x). No source option is fully correct for a general function as written.'
    if num=='viii':revision['sourceClarification']='Options (b) and (d) are identical normal equations for m ≠ 0; both are correct, while the key selects (d).'
    review4.append(revision)
text+='const math12Review4='+json.dumps(review4,ensure_ascii=False)+';\n'
text+="const math12Rev4=MATH_12_DATA[3].exercises.find(ex=>ex.title==='Review Exercise 4');math12Rev4.unreviewedProblems=math12Rev4.problems;math12Rev4.problems=math12Review4;math12Rev4.pageStart=math12Rev4.pageEnd=128;MATH_12_DATA[3].sourceSummaryBlocks=MATH_12_DATA[3].sourcePages.find(page=>page.page===129).blocks;MATH_12_DATA[3].sourceSummaryReferences=[{page:129,jpg:'069_page_1.jpg',verification:'complete source summary and history box visually compared with JPG/PDF'}];\n"
text += 'MATH_12_DATA[4].sourcePages = '+json.dumps(VECTOR_PAGES,ensure_ascii=False,indent=2)+';\n'
text += 'const math12VectorExamples='+json.dumps(VECTOR_EXAMPLES,ensure_ascii=False)+';\n'
text += """math12VectorExamples.forEach(example=>{const chapter=MATH_12_DATA[4];const old=chapter.workedExamples.find(e=>e.num===example.num);if(old)Object.assign(old,example);else{const next=chapter.workedExamples.findIndex(e=>Number(e.num)>Number(example.num));chapter.workedExamples.splice(next<0?chapter.workedExamples.length:next,0,example);}});
const math12Vector132=MATH_12_DATA[4].sourcePages.find(p=>p.page===132),math12VectorLimitStart=math12Vector132.blocks.findIndex(b=>b.type==='heading'&&b.text==='5.2 Limit and Continuity');
const math12VectorIntro=MATH_12_DATA[4].sections[0];math12VectorIntro.unreviewedTheory='';math12VectorIntro.sourceBlocks=MATH_12_DATA[4].sourcePages.filter(p=>p.page===130||p.page===131).flatMap(p=>p.blocks).concat(math12Vector132.blocks.slice(0,math12VectorLimitStart));math12VectorIntro.theory=math12VectorIntro.sourceBlocks.map(math12BlockText).join('\\n\\n');math12VectorIntro.sourceReferences=MATH_12_DATA[4].sourcePages.filter(p=>p.page<=132).map(p=>({page:p.page,jpg:p.file,verification:'visually compared with JPG and full PDF'}));
const math12VectorLimits=MATH_12_DATA[4].sections[1];math12VectorLimits.unreviewedTheory='';math12VectorLimits.sourceBlocks=math12Vector132.blocks.slice(math12VectorLimitStart).concat(MATH_12_DATA[4].sourcePages.find(p=>p.page===133).blocks);math12VectorLimits.theory=math12VectorLimits.sourceBlocks.map(math12BlockText).join('\\n\\n');math12VectorLimits.sourceReferences=MATH_12_DATA[4].sourcePages.filter(p=>p.page>=132).map(p=>({page:p.page,jpg:p.file,verification:'visually compared with JPG and full PDF'}));
"""
ex51=[{'id':'ex-5-1-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX51_STEPS[i],'solution':'\n'.join(EX51_STEPS[i]),'answer':EX51_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':134,'jpg':'071_page_2.jpg','verification':'every subpart visually compared with JPG and enlarged full PDF'}]} for i,q in enumerate(EX51_QUESTIONS)]
text+='const math12Exercise51='+json.dumps(ex51,ensure_ascii=False)+';\n'
text+="""const math12Ex51=MATH_12_DATA[4].exercises.find(ex=>ex.title==='Exercise 5.1');math12Ex51.unreviewedProblems=math12Ex51.problems;math12Ex51.problems=math12Exercise51;math12Ex51.pageStart=math12Ex51.pageEnd=134;
const math12Vector134=MATH_12_DATA[4].sourcePages.find(p=>p.page===134);const math12VectorDerivativeStart=math12Vector134.blocks.findIndex(b=>b.type==='heading'&&b.text.startsWith('5.3'));
const math12VectorDerivative=MATH_12_DATA[4].sections[2];math12VectorDerivative.unreviewedTheory=math12VectorDerivative.theory;math12VectorDerivative.sourceBlocks=math12Vector134.blocks.slice(math12VectorDerivativeStart);math12VectorDerivative.sourceReferences=[{page:134,jpg:'071_page_2.jpg',verification:'derivative definition checked against JPG/PDF'}];math12VectorDerivative.theory=math12VectorDerivative.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12VectorDerivative.unreviewedTheory;
"""
text+="""const math12Vector135=MATH_12_DATA[4].sourcePages.find(p=>p.page===135),math12VectorRuleStart=math12Vector135.blocks.findIndex(b=>b.type==='heading'&&b.text==='5.4 Vector Differentiation');math12VectorDerivative.unreviewedTheory='';math12VectorDerivative.sourceBlocks.push(...math12Vector135.blocks.slice(0,math12VectorRuleStart));math12VectorDerivative.sourceReferences.push({page:135,jpg:'072_page_1.jpg',verification:'theorem and both source examples checked'});math12VectorDerivative.theory=math12VectorDerivative.sourceBlocks.map(math12BlockText).join('\\n\\n');const math12VectorRules=MATH_12_DATA[4].sections[3];math12VectorRules.unreviewedTheory=math12VectorRules.theory;math12VectorRules.sourceBlocks=math12Vector135.blocks.slice(math12VectorRuleStart);math12VectorRules.sourceReferences=[{page:135,jpg:'072_page_1.jpg',verification:'six differentiation rules checked'}];math12VectorRules.theory=math12VectorRules.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12VectorRules.unreviewedTheory;
"""
text+="""math12VectorRules.sourceBlocks.push(...MATH_12_DATA[4].sourcePages.find(p=>p.page===136).blocks);math12VectorRules.sourceReferences.push({page:136,jpg:'072_page_2.jpg',verification:'all five printed proof chains visually checked'});math12VectorRules.theory=math12VectorRules.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12VectorRules.unreviewedTheory;
"""
text+="""math12VectorRules.sourceBlocks.push(...MATH_12_DATA[4].sourcePages.filter(p=>p.page===137||p.page===138).flatMap(p=>p.blocks));math12VectorRules.sourceReferences.push(...MATH_12_DATA[4].sourcePages.filter(p=>p.page===137||p.page===138).map(p=>({page:p.page,jpg:p.file,verification:'source worked calculations and velocity/acceleration/speed definitions checked'})));math12VectorRules.theory=math12VectorRules.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12VectorRules.unreviewedTheory;
"""
ex52=[{'id':'ex-5-2-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX52_STEPS[i],'solution':'\n'.join(EX52_STEPS[i]),'answer':EX52_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':139,'jpg':'074_page_1.jpg','verification':'all source subparts and derivative orders checked at enlarged resolution'}]} for i,q in enumerate(EX52_QUESTIONS)]
text+='const math12Exercise52='+json.dumps(ex52,ensure_ascii=False)+';\n'
text+="""const math12Ex52=MATH_12_DATA[4].exercises.find(ex=>ex.title==='Exercise 5.2');math12Ex52.unreviewedProblems=math12Ex52.problems;math12Ex52.problems=math12Exercise52;math12Ex52.pageStart=math12Ex52.pageEnd=139;const math12Vector139=MATH_12_DATA[4].sourcePages.find(p=>p.page===139);math12VectorRules.sourceBlocks.push(...math12Vector139.blocks.slice(0,math12Vector139.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 5.2')));math12VectorRules.sourceReferences.push({page:139,jpg:'074_page_1.jpg',verification:'complete Example 13 solution and direction normalization checked'});math12VectorRules.theory=math12VectorRules.sourceBlocks.map(math12BlockText).join('\\n\\n');math12VectorRules.unreviewedTheory='';
"""
text+="MATH_12_DATA[4].exercises=[math12Ex51,math12Ex52,...MATH_12_DATA[4].exercises.filter(ex=>ex!==math12Ex51&&ex!==math12Ex52)];\n"
review5=[]
for num,q,options,answer,steps in REVIEW5_ITEMS:
 review5.append({'id':'ex-5-review-'+num,'qNo':num,'question':q+' '+' '.join('('+letter+') '+option for letter,option in zip('abcd',options)),'answer':('Option ('+answer+')') if len(answer)==1 else answer,'steps':steps,'solution':'\n'.join(steps),'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':140,'jpg':'074_page_2.jpg','verification':'all four source options checked; inconsistent questions explained separately'}]})
text+='const math12Review5='+json.dumps(review5,ensure_ascii=False)+';\n'
text+="const math12Rev5=MATH_12_DATA[4].exercises.find(ex=>ex.title==='Review Exercise 5');math12Rev5.unreviewedProblems=math12Rev5.problems;math12Rev5.problems=math12Review5;math12Rev5.pageStart=math12Rev5.pageEnd=140;MATH_12_DATA[4].sourceSummaryBlocks=MATH_12_DATA[4].sourcePages.find(p=>p.page===141).blocks;MATH_12_DATA[4].sourceSummaryReferences=[{page:141,jpg:'075_page_1.jpg',verification:'complete native summary and exact source history/project art checked'}];\n"
text+='MATH_12_DATA[4].exercises.push({id:"ex-5-project-source141",title:"Project — Vector Motion",pageStart:141,pageEnd:141,problems:['+json.dumps(VECTOR_PROJECT,ensure_ascii=False)+']});\n'
text+='MATH_12_DATA[5].sourcePages='+json.dumps(INTEGRATION_PAGES,ensure_ascii=False,indent=2)+';\n'
text+='const math12IntegrationExamples='+json.dumps(INTEGRATION_EXAMPLES,ensure_ascii=False)+';\n'
text+="""math12IntegrationExamples.forEach(example=>{const chapter=MATH_12_DATA[5];const old=chapter.workedExamples.find(e=>e.num===example.num);if(old)Object.assign(old,example);else chapter.workedExamples.push(example);});MATH_12_DATA[5].workedExamples.sort((a,b)=>Number(a.num)-Number(b.num));
const math12Integration158=MATH_12_DATA[5].sourcePages.find(p=>p.page===158),math12Integration159=MATH_12_DATA[5].sourcePages.find(p=>p.page===159),math12PartsStart=math12Integration159.blocks.findIndex(b=>b.type==='heading'&&b.text==='6.4 Integration by Parts');
const math12Substitution=MATH_12_DATA[5].sections[1];math12Substitution.unreviewedTheory=math12Substitution.theory;math12Substitution.sourceBlocks=math12Integration158.blocks.concat(math12Integration159.blocks.slice(0,math12PartsStart));math12Substitution.sourceReferences=[{page:158,jpg:'083_page_2.jpg',verification:'available continuation only; preceding pages absent'},{page:159,jpg:'084_page_1.jpg',verification:'Example 9 conclusion checked'}];math12Substitution.theory=math12Substitution.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Substitution.unreviewedTheory;
const math12Parts=MATH_12_DATA[5].sections[3];math12Parts.unreviewedTheory=math12Parts.theory;math12Parts.sourceBlocks=math12Integration159.blocks.slice(math12PartsStart);math12Parts.sourceReferences=[{page:159,jpg:'084_page_1.jpg',verification:'full parts definition and proof, Example 10, radical proof opening checked'}];math12Parts.theory=math12Parts.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Parts.unreviewedTheory;
MATH_12_DATA[5].sourceGap={pageStart:142,pageEnd:157,status:'unavailable in supplied JPG, PDF and Word formats',impact:'Unit opening, objectives, initial rules and examples are not source-complete.'};
"""
text+="""math12Parts.unreviewedTheory='';math12Parts.sourceBlocks.push(...MATH_12_DATA[5].sourcePages.filter(p=>p.page===160||p.page===161).flatMap(p=>p.blocks));math12Parts.sourceReferences.push(...MATH_12_DATA[5].sourcePages.filter(p=>p.page===160||p.page===161).map(p=>({page:p.page,jpg:p.file,verification:'full radical derivations, source misprints and Examples 11/12 checked'})));math12Parts.theory=math12Parts.sourceBlocks.map(math12BlockText).join('\\n\\n');
"""
ex62=[{'id':'ex-6-2-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX62_STEPS[i],'solution':'\n'.join(EX62_STEPS[i]),'answer':EX62_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':162,'jpg':'085_page_2.jpg','verification':'all seventeen printed subparts checked'}]} for i,q in enumerate(EX62_QUESTIONS)]
text+='const math12Exercise62='+json.dumps(ex62,ensure_ascii=False)+';\n'
text+="""const math12Ex62=MATH_12_DATA[5].exercises.find(ex=>ex.title==='Exercise 6.2');math12Ex62.unreviewedProblems=math12Ex62.problems;math12Ex62.problems=math12Exercise62;math12Ex62.pageStart=math12Ex62.pageEnd=162;const math12Integration162=MATH_12_DATA[5].sourcePages.find(p=>p.page===162);math12Ex62.sourceContextBlocks=math12Integration162.blocks.slice(math12Integration162.blocks.findIndex(b=>b.type==='heading'&&b.text==='History'));math12Parts.sourceBlocks.push(...math12Integration162.blocks.slice(0,math12Integration162.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 6.2')));math12Parts.sourceReferences.push({page:162,jpg:'085_page_2.jpg',verification:'ILATE mnemonic/table checked'});math12Parts.theory=math12Parts.sourceBlocks.map(math12BlockText).join('\\n\\n');
"""
ex63=[{'id':'ex-6-3-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX63_STEPS[i],'solution':'\n'.join(EX63_STEPS[i]),'answer':EX63_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':165,'jpg':'087_page_1.jpg','verification':'all ten rational subparts and three applied source questions inspected'}]} for i,q in enumerate(EX63_QUESTIONS)]
text+='const math12Exercise63='+json.dumps(ex63,ensure_ascii=False)+';\n'
text+="""const math12Ex63=MATH_12_DATA[5].exercises.find(ex=>ex.title==='Exercise 6.3');math12Ex63.unreviewedProblems=math12Ex63.problems;math12Ex63.problems=math12Exercise63;math12Ex63.pageStart=math12Ex63.pageEnd=165;const math12Partial=MATH_12_DATA[5].sections[4];math12Partial.unreviewedTheory='';math12Partial.sourceBlocks=MATH_12_DATA[5].sourcePages.filter(p=>p.page>=163&&p.page<=165).flatMap(p=>p.page===165?p.blocks.slice(0,p.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 6.3')):p.blocks);math12Partial.sourceReferences=MATH_12_DATA[5].sourcePages.filter(p=>p.page>=163&&p.page<=165).map(p=>({page:p.page,jpg:p.file,verification:'complete partial-fraction theory, source example and hint checked'}));math12Partial.theory=math12Partial.sourceBlocks.map(math12BlockText).join('\\n\\n');
"""
text+="""const math12Definite=MATH_12_DATA[5].sections[5];math12Definite.unreviewedTheory=math12Definite.theory;math12Definite.sourceBlocks=MATH_12_DATA[5].sourcePages.filter(p=>p.page>=166&&p.page<=168).flatMap(p=>p.blocks);math12Definite.sourceReferences=MATH_12_DATA[5].sourcePages.filter(p=>p.page>=166&&p.page<=168).map(p=>({page:p.page,jpg:p.file,verification:'definition, five source figures and full fundamental theorem checked'}));math12Definite.theory=math12Definite.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Definite.unreviewedTheory;
"""
text+="""math12Definite.sourceBlocks.push(...MATH_12_DATA[5].sourcePages.filter(p=>p.page>=169&&p.page<=172).flatMap(p=>p.blocks));math12Definite.sourceReferences.push(...MATH_12_DATA[5].sourcePages.filter(p=>p.page>=169&&p.page<=172).map(p=>({page:p.page,jpg:p.file,verification:'all source properties, proof chains, challenges, Examples 16–18 and signed-area opening checked'})));math12Definite.theory=math12Definite.sourceBlocks.map(math12BlockText).join('\\n\\n')+'\\n\\n'+math12Definite.unreviewedTheory;
"""
text+='MATH_12_DATA[5].exercises.push({id:"ex-6-integral-property-challenges",title:"Challenges — Integral Properties",pageStart:169,pageEnd:170,problems:'+json.dumps(INTEGRAL_CHALLENGES,ensure_ascii=False)+'});\n'
text+="""math12Definite.unreviewedTheory='';math12Definite.sourceBlocks.push(...MATH_12_DATA[5].sourcePages.filter(p=>p.page===173||p.page===174).flatMap(p=>p.blocks));math12Definite.sourceReferences.push(...MATH_12_DATA[5].sourcePages.filter(p=>p.page===173||p.page===174).map(p=>({page:p.page,jpg:p.file,verification:'all source area rules, native polynomial regions and source Maple commands/palettes checked'})));math12Definite.theory=math12Definite.sourceBlocks.map(math12BlockText).join('\\n\\n');
const math12ReviewedIntegrationNums=new Set(math12IntegrationExamples.map(e=>e.num)),math12SeenIntegrationNums=new Set();MATH_12_DATA[5].unreviewedDuplicateExamples=[];MATH_12_DATA[5].workedExamples=MATH_12_DATA[5].workedExamples.filter(e=>{if(!math12ReviewedIntegrationNums.has(e.num))return true;if(math12SeenIntegrationNums.has(e.num)){MATH_12_DATA[5].unreviewedDuplicateExamples.push(e);return false;}math12SeenIntegrationNums.add(e.num);return true;});
"""
ex64=[]
for i,q in enumerate(EX64_QUESTIONS):
 revision={'id':'ex-6-4-q'+str(i+1),'qNo':str(i+1),'question':q,'steps':EX64_STEPS[i],'solution':'\n'.join(EX64_STEPS[i]),'answer':EX64_ANSWERS[i],'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':175,'jpg':'076_page_1.jpg','verification':'all source expressions, shaded intervals and rate units visually checked'}]}
 if i==3:revision['sourceQuestionBlocks']=EX64_GRAPHS
 ex64.append(revision)
text+='const math12Exercise64='+json.dumps(ex64,ensure_ascii=False)+';\n'
text+="""const math12Ex64=MATH_12_DATA[5].exercises.find(ex=>ex.title==='Exercise 6.4');math12Ex64.unreviewedProblems=math12Ex64.problems;math12Ex64.problems=math12Exercise64;math12Ex64.pageStart=math12Ex64.pageEnd=175;const math12Integration175=MATH_12_DATA[5].sourcePages.find(p=>p.page===175);math12Ex64.sourceContextBlocks=math12Integration175.blocks.slice(0,math12Integration175.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 6.4'));MATH_12_DATA[5].exercises=[...MATH_12_DATA[5].exercises.filter(e=>e.title==='Exercise 6.1'),math12Ex62,math12Ex63,math12Ex64,...MATH_12_DATA[5].exercises.filter(e=>!['Exercise 6.1','Exercise 6.2','Exercise 6.3','Exercise 6.4'].includes(e.title))];
"""
review6=[]
for num,q,options,answer,steps in REVIEW6_ITEMS:
 review6.append({'id':'ex-6-review-'+num,'qNo':num,'question':q+' '+' '.join('('+letter+') '+option for letter,option in zip('abcd',options)),'steps':steps,'solution':'\n'.join(steps),'answer':('Option ('+answer+')') if len(answer)==1 else answer,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':176,'jpg':'076_page_2.jpg','verification':'all source choices enlarged and visually checked; invalid and duplicate choices explained'}]})
text+='const math12Review6='+json.dumps(review6,ensure_ascii=False)+';\n'
text+="""const math12Rev6=MATH_12_DATA[5].exercises.find(ex=>ex.title==='Review Exercise 6');math12Rev6.unreviewedProblems=math12Rev6.problems;math12Rev6.problems=math12Review6;math12Rev6.pageStart=math12Rev6.pageEnd=176;MATH_12_DATA[5].sourceSummaryBlocks=MATH_12_DATA[5].sourcePages.find(p=>p.page===177).blocks;MATH_12_DATA[5].sourceSummaryReferences=[{page:177,jpg:'077_page_1.jpg',verification:'complete native summary checked'}];
const math12ActualSubstitution=MATH_12_DATA[5].sections[2];math12ActualSubstitution.unreviewedTheory=math12ActualSubstitution.theory;math12ActualSubstitution.sourceBlocks=math12Substitution.sourceBlocks;math12ActualSubstitution.sourceReferences=math12Substitution.sourceReferences;math12ActualSubstitution.theory=math12ActualSubstitution.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ActualSubstitution.title='6.3 Integration by Substitution';math12ActualSubstitution.sourceStatus='partial: preceding source pages 142–157 unavailable';
for(const [index,title] of [[0,'6.1 Introduction'],[1,'6.2 Rules of Integration']]){const section=MATH_12_DATA[5].sections[index];section.unreviewedTheory=section.unreviewedTheory||section.theory;section.title=title;section.sourceBlocks=[{type:'clarification',text:'The supplied JPG, PDF and Word sources omit printed pages 142–157, containing the opening of this unit. This section cannot be marked source-complete; no missing textbook wording or questions have been invented.'}];section.sourceReferences=[];section.theory=section.sourceBlocks[0].text;section.sourceStatus='unavailable in supplied source formats';}
"""
text+='MATH_12_DATA[6].sourcePages='+json.dumps(STRAIGHT_PAGES,ensure_ascii=False)+';\n'
text+='MATH_12_DATA[6].sourceObjectives='+json.dumps(STRAIGHT_OBJECTIVES,ensure_ascii=False)+';MATH_12_DATA[6].sourceIntroductionBlocks='+json.dumps(STRAIGHT_INTRO,ensure_ascii=False)+';\n'
text+="MATH_12_DATA[6].sections.unshift({id:'sec-7-introduction',title:'Introduction to Analytic Geometry',sourceBlocks:MATH_12_DATA[6].sourceIntroductionBlocks,theory:MATH_12_DATA[6].sourceIntroductionBlocks.map(math12BlockText).join('\\n\\n'),sourceReferences:[{page:178,jpg:'077_page_2.jpg',verification:'JPG/PDF and duplicate compared visually'}]});\n"
text+='const math12StraightExamples='+json.dumps(STRAIGHT_EXAMPLES,ensure_ascii=False)+';\n'
text+="math12StraightExamples.forEach(e=>{e.problem=e.question;e.title='Example '+e.num+' — '+e.title;e.given=e.question;e.method='Apply the defining formulas, then check the result against the stated conditions.';const old=MATH_12_DATA[6].workedExamples.find(x=>x.num===e.num);if(old){old.unreviewedProblem=old.problem;Object.assign(old,e);}else MATH_12_DATA[6].workedExamples.push(e);});const math12Distance=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-1');math12Distance.unreviewedTheory=math12Distance.theory;math12Distance.sourceBlocks=MATH_12_DATA[6].sourcePages.filter(p=>p.page>=179&&p.page<=182).flatMap(p=>p.blocks);math12Distance.theory=math12Distance.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Distance.sourceReferences=MATH_12_DATA[6].sourcePages.filter(p=>p.page>=179&&p.page<=182).map(p=>({page:p.page,jpg:p.file,verification:'full JPG/PDF proof visually checked'}));\n"
text+="const math12Source183=MATH_12_DATA[6].sourcePages.find(p=>p.page===183);const math12Ex71Start=math12Source183.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 7.1');math12Distance.sourceBlocks.push(...math12Source183.blocks.slice(0,math12Ex71Start));math12Distance.theory=math12Distance.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Distance.sourceReferences.push({page:183,jpg:'080_page_1.jpg',verification:'incenter proof completion and examples checked'});\n"
review71=[{'id':'ex-7-1-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':183,'jpg':'080_page_1.jpg','verification':'All five source question groups and exact coordinates visually checked'}]} for i,(q,steps,ans) in enumerate(zip(EX71_QUESTIONS,EX71_STEPS,EX71_ANSWERS),1)]
text+='const math12ReviewedEx71='+json.dumps(review71,ensure_ascii=False)+';\n'
text+="const math12Ex71=MATH_12_DATA[6].exercises.find(e=>e.title==='Exercise 7.1');math12Ex71.unreviewedProblems=math12Ex71.problems;math12Ex71.problems=math12ReviewedEx71;math12Ex71.pageStart=math12Ex71.pageEnd=183;\n"
text+="const math12Slope=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-2'),math12Source185=MATH_12_DATA[6].sourcePages.find(p=>p.page===185),math12AxisStart=math12Source185.blocks.findIndex(b=>b.type==='heading'&&b.text.startsWith('7.3 Equation'));math12Slope.unreviewedTheory=math12Slope.theory;math12Slope.sourceBlocks=MATH_12_DATA[6].sourcePages.find(p=>p.page===184).blocks.concat(math12Source185.blocks.slice(0,math12AxisStart));math12Slope.theory=math12Slope.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Slope.sourceReferences=[{page:184,jpg:'080_page_2.jpg'},{page:185,jpg:'081_page_1.jpg'}];const math12Axis=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-3');math12Axis.unreviewedTheory=math12Axis.theory;math12Axis.sourceBlocks=math12Source185.blocks.slice(math12AxisStart);math12Axis.theory=math12Axis.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Axis.sourceReferences=[{page:185,jpg:'081_page_1.jpg'}];\n"
text+="const math12StraightNums=new Set(math12StraightExamples.map(e=>e.num)),math12StraightSeen=new Set();MATH_12_DATA[6].unreviewedDuplicateExamples=[];MATH_12_DATA[6].workedExamples=MATH_12_DATA[6].workedExamples.filter(e=>{if(!math12StraightNums.has(e.num))return true;if(math12StraightSeen.has(e.num)){MATH_12_DATA[6].unreviewedDuplicateExamples.push(e);return false;}math12StraightSeen.add(e.num);return true;}).sort((a,b)=>Number(a.num)-Number(b.num));\n"
text+="const math12Source186=MATH_12_DATA[6].sourcePages.find(p=>p.page===186),math12FormStart=math12Source186.blocks.findIndex(b=>b.type==='heading'&&b.text.startsWith('7.4 Standard'));math12Axis.sourceBlocks.push(...math12Source186.blocks.slice(0,math12FormStart));math12Axis.theory=math12Axis.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Axis.sourceReferences.push({page:186,jpg:'081_page_2.jpg'});const math12Forms=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-4');math12Forms.unreviewedTheory=math12Forms.theory;math12Forms.sourceBlocks=math12Source186.blocks.slice(math12FormStart).concat(MATH_12_DATA[6].sourcePages.find(p=>p.page===187).blocks);math12Forms.theory=math12Forms.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Forms.sourceReferences=[{page:186,jpg:'081_page_2.jpg'},{page:187,jpg:'082_page_1.jpg'}];\n"
text+="math12Forms.sourceBlocks.push(...MATH_12_DATA[6].sourcePages.filter(p=>p.page===188||p.page===189).flatMap(p=>p.blocks));math12Forms.theory=math12Forms.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Forms.sourceReferences.push({page:188,jpg:'082_page_2.jpg'},{page:189,jpg:'083_page_1.jpg'});\n"
text+="math12Forms.sourceBlocks.push(...MATH_12_DATA[6].sourcePages.filter(p=>p.page===190||p.page===191).flatMap(p=>p.blocks));math12Forms.theory=math12Forms.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Forms.sourceReferences.push({page:190,jpg:'099_page_2.jpg'},{page:191,jpg:'100_page_1.jpg'});\n"
review72=[{'id':'ex-7-2-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':192,'jpg':'100_page_2.jpg','verification':'All eight question groups and exact plotted intercepts visually checked'}],**({'sourceQuestionBlocks':EX72_GRAPHS} if i==1 else {})} for i,(q,steps,ans) in enumerate(zip(EX72_QUESTIONS,EX72_STEPS,EX72_ANSWERS),1)]
text+='const math12ReviewedEx72='+json.dumps(review72,ensure_ascii=False)+';\n'
text+="const math12Ex72=MATH_12_DATA[6].exercises.find(e=>e.title==='Exercise 7.2');math12Ex72.unreviewedProblems=math12Ex72.problems;math12Ex72.problems=math12ReviewedEx72;math12Ex72.pageStart=math12Ex72.pageEnd=192;\n"
project72={'id':'ex-7-project-midpoint','qNo':'Project',**EX72_PROJECT,'solution':'\n'.join(EX72_PROJECT['steps']),'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement; sample coordinates explicitly distinguished from source','sourceReferences':[{'page':192,'jpg':'100_page_2.jpg','verification':'Entire project question and original illustration visually checked'}]}
text+='MATH_12_DATA[6].exercises.push({id:"ex-7-midpoint-project",title:"Project — Home and School Midpoint",pageStart:192,pageEnd:192,problems:['+json.dumps(project72,ensure_ascii=False)+']});\n'
text+="const math12Source194=MATH_12_DATA[6].sourcePages.find(p=>p.page===194),math12AngleStart=math12Source194.blocks.findIndex(b=>b.type==='heading'&&b.text==='7.6 Angle between Lines'),math12Position=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-5');math12Position.unreviewedTheory=math12Position.theory;math12Position.sourceBlocks=MATH_12_DATA[6].sourcePages.find(p=>p.page===193).blocks.concat(math12Source194.blocks.slice(0,math12AngleStart));math12Position.theory=math12Position.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Position.sourceReferences=[{page:193,jpg:'101_page_1.jpg'},{page:194,jpg:'101_page_2.jpg'}];const math12Angle=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-6');math12Angle.unreviewedTheory=math12Angle.theory;math12Angle.sourceBlocks=math12Source194.blocks.slice(math12AngleStart);math12Angle.theory=math12Angle.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Angle.sourceReferences=[{page:194,jpg:'101_page_2.jpg'}];\n"
text+="math12Angle.sourceBlocks.push(...MATH_12_DATA[6].sourcePages.filter(p=>p.page===195||p.page===196).flatMap(p=>p.blocks));math12Angle.theory=math12Angle.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Angle.sourceReferences.push({page:195,jpg:'102_page_1.jpg'},{page:196,jpg:'102_page_2.jpg'});\n"
text+="math12Angle.sourceBlocks.push(...MATH_12_DATA[6].sourcePages.filter(p=>p.page===197||p.page===198).flatMap(p=>p.blocks));math12Angle.theory=math12Angle.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Angle.sourceReferences.push({page:197,jpg:'103_page_1.jpg'},{page:198,jpg:'103_page_2.jpg'});\n"
review73=[{'id':'ex-7-3-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':199,'jpg':'104_page_1.jpg','verification':'All eight exact source question groups visually checked; obtuse angles and right-angle exception independently calculated'}]} for i,(q,steps,ans) in enumerate(zip(EX73_QUESTIONS,EX73_STEPS,EX73_ANSWERS),1)]
text+='const math12ReviewedEx73='+json.dumps(review73,ensure_ascii=False)+';\n'
text+="const math12Ex73=MATH_12_DATA[6].exercises.find(e=>e.title==='Exercise 7.3');math12Ex73.unreviewedProblems=math12Ex73.problems;math12Ex73.problems=math12ReviewedEx73;math12Ex73.pageStart=math12Ex73.pageEnd=199;\n"
text+='math12Angle.sourceBlocks.push(...'+json.dumps(EX73_HISTORY,ensure_ascii=False)+');math12Angle.theory=math12Angle.sourceBlocks.map(math12BlockText).join("\\n\\n");math12Angle.sourceReferences.push({page:199,jpg:"104_page_1.jpg",verification:"Full source history and portrait inspected"});\n'
text+="const math12Concurrency=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-7');math12Concurrency.unreviewedTheory=math12Concurrency.theory;math12Concurrency.sourceBlocks=MATH_12_DATA[6].sourcePages.filter(p=>p.page===200||p.page===201).flatMap(p=>p.blocks);math12Concurrency.theory=math12Concurrency.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Concurrency.sourceReferences=[{page:200,jpg:'104_page_2.jpg'},{page:201,jpg:'105_page_1.jpg'}];\n"
text+="math12Concurrency.sourceBlocks.push(...MATH_12_DATA[6].sourcePages.filter(p=>p.page===202||p.page===203).flatMap(p=>p.blocks));math12Concurrency.theory=math12Concurrency.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Concurrency.sourceReferences.push({page:202,jpg:'105_page_2.jpg'},{page:203,jpg:'106_page_1.jpg'});\n"
text+="math12Concurrency.sourceBlocks.push(...MATH_12_DATA[6].sourcePages.filter(p=>p.page===204||p.page===205).flatMap(p=>p.blocks));math12Concurrency.theory=math12Concurrency.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Concurrency.sourceReferences.push({page:204,jpg:'106_page_2.jpg'},{page:205,jpg:'107_page_1.jpg'});\n"
text+="const math12Source206=MATH_12_DATA[6].sourcePages.find(p=>p.page===206),math12AreaStart=math12Source206.blocks.findIndex(b=>b.type==='heading'&&b.text==='7.8 Area of a Triangular Region');math12Concurrency.sourceBlocks.push(...math12Source206.blocks.slice(0,math12AreaStart));math12Concurrency.theory=math12Concurrency.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Concurrency.sourceReferences.push({page:206,jpg:'107_page_2.jpg'});const math12TriangleArea=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-8');math12TriangleArea.unreviewedTheory=math12TriangleArea.theory;math12TriangleArea.sourceBlocks=math12Source206.blocks.slice(math12AreaStart);math12TriangleArea.theory=math12TriangleArea.sourceBlocks.map(math12BlockText).join('\\n\\n');math12TriangleArea.sourceReferences=[{page:206,jpg:'107_page_2.jpg'}];\n"
text+="const math12Homogeneous=MATH_12_DATA[6].sections.find(s=>s.id==='sec-7-9');math12Homogeneous.unreviewedTheory=math12Homogeneous.theory;math12Homogeneous.sourceBlocks=MATH_12_DATA[6].sourcePages.filter(p=>p.page>=207&&p.page<=209).flatMap(p=>p.blocks);math12Homogeneous.theory=math12Homogeneous.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Homogeneous.sourceReferences=MATH_12_DATA[6].sourcePages.filter(p=>p.page>=207&&p.page<=209).map(p=>({page:p.page,jpg:p.file}));\n"
review74=[{'id':'ex-7-4-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':210,'jpg':'109_page_2.jpg','verification':'All eight source groups visually reviewed and exact arithmetic checked'}]} for i,(q,steps,ans) in enumerate(zip(EX74_QUESTIONS,EX74_STEPS,EX74_ANSWERS),1)]
text+='const math12ReviewedEx74='+json.dumps(review74,ensure_ascii=False)+';\n'
text+="const math12Ex74=MATH_12_DATA[6].exercises.find(e=>e.title==='Exercise 7.4');math12Ex74.unreviewedProblems=math12Ex74.problems;math12Ex74.problems=math12ReviewedEx74;math12Ex74.pageStart=math12Ex74.pageEnd=210;\n"
review7=[]
for num,q,options,answer,steps in UNIT7_REVIEW:
 review7.append({'id':'ex-7-review-'+num,'qNo':num,'question':q+' '+' '.join('('+letter+') '+option for letter,option in zip('abcd',options)),'steps':steps,'solution':'\n'.join(steps),'answer':('Option ('+answer+')') if len(answer)==1 else answer,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':211,'jpg':'110_page_1.jpg','verification':'All source choices enlarged and visually checked; incorrect area choices explained'}]})
text+='const math12Review7='+json.dumps(review7,ensure_ascii=False)+';\n'
text+="const math12Rev7=MATH_12_DATA[6].exercises.find(ex=>ex.title==='Review Exercise 7');math12Rev7.unreviewedProblems=math12Rev7.problems;math12Rev7.problems=math12Review7;math12Rev7.pageStart=math12Rev7.pageEnd=211;MATH_12_DATA[6].sourceSummaryBlocks=MATH_12_DATA[6].sourcePages.find(p=>p.page===212).blocks;MATH_12_DATA[6].sourceSummaryReferences=[{page:212,jpg:'110_page_2.jpg',verification:'Complete native summary visually checked'}];\n"
text+='MATH_12_DATA[7].sourcePages='+json.dumps(CONIC_PAGES,ensure_ascii=False)+';\n'
text+='MATH_12_DATA[7].sourceObjectives='+json.dumps(CONIC_OBJECTIVES,ensure_ascii=False)+';MATH_12_DATA[7].sourceIntroductionBlocks='+json.dumps(CONIC_INTRO,ensure_ascii=False)+';\n'
text+="MATH_12_DATA[7].sections.unshift({id:'sec-8-introduction',title:'Introduction to Conics',sourceBlocks:MATH_12_DATA[7].sourceIntroductionBlocks,theory:MATH_12_DATA[7].sourceIntroductionBlocks.map(math12BlockText).join('\\n\\n'),sourceReferences:[{page:213,jpg:'111_page_1.jpg'}]});const math12ConicFamily=MATH_12_DATA[7].sections.find(s=>s.id==='sec-8-1'),math12Source213=MATH_12_DATA[7].sourcePages.find(p=>p.page===213),math12Source214=MATH_12_DATA[7].sourcePages.find(p=>p.page===214),math12CircleStart=math12Source214.blocks.findIndex(b=>b.type==='heading'&&b.text==='8.2 Circle');math12ConicFamily.unreviewedTheory=math12ConicFamily.theory;math12ConicFamily.sourceBlocks=math12Source213.blocks.slice(MATH_12_DATA[7].sourceIntroductionBlocks.length).concat(math12Source214.blocks.slice(0,math12CircleStart));math12ConicFamily.theory=math12ConicFamily.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ConicFamily.sourceReferences=[{page:213,jpg:'111_page_1.jpg'},{page:214,jpg:'111_page_2.jpg'}];const math12Circle=MATH_12_DATA[7].sections.find(s=>s.id==='sec-8-2');math12Circle.unreviewedTheory=math12Circle.theory;math12Circle.sourceBlocks=math12Source214.blocks.slice(math12CircleStart);math12Circle.theory=math12Circle.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Circle.sourceReferences=[{page:214,jpg:'111_page_2.jpg'}];\n"
text+='const math12CircleReviewedExamples='+json.dumps(CONIC_EXAMPLES,ensure_ascii=False)+';\n'
text+="math12CircleReviewedExamples.forEach(e=>{e.problem=e.question;e.given=e.question;e.method='Identify the geometry, apply the relevant relation, and check the original conditions.';e.title='Example '+e.num+' — '+e.title;const old=MATH_12_DATA[7].workedExamples.find(x=>x.num===e.num);if(old){old.unreviewedProblem=old.problem;Object.assign(old,e);}else MATH_12_DATA[7].workedExamples.push(e);});const math12ConicNums=new Set(math12CircleReviewedExamples.map(e=>e.num)),math12ConicSeen=new Set();MATH_12_DATA[7].unreviewedDuplicateExamples=[];MATH_12_DATA[7].workedExamples=MATH_12_DATA[7].workedExamples.filter(e=>{if(!math12ConicNums.has(e.num))return true;if(math12ConicSeen.has(e.num)){MATH_12_DATA[7].unreviewedDuplicateExamples.push(e);return false;}math12ConicSeen.add(e.num);return true;}).sort((a,b)=>Number(a.num)-Number(b.num));math12Circle.sourceBlocks.push(...MATH_12_DATA[7].sourcePages.filter(p=>p.page>=215&&p.page<=220).flatMap(p=>p.blocks));math12Circle.theory=math12Circle.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Circle.sourceReferences.push(...MATH_12_DATA[7].sourcePages.filter(p=>p.page>=215&&p.page<=220).map(p=>({page:p.page,jpg:p.file})));\n"
review81=[{'id':'ex-8-1-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':221,'jpg':'115_page_1.jpg','verification':'Every source subpart visually reviewed and exact calculations checked'}]} for i,(q,steps,ans) in enumerate(zip(EX81_QUESTIONS,EX81_STEPS,EX81_ANSWERS),1)]
text+='const math12ReviewedEx81='+json.dumps(review81,ensure_ascii=False)+';\n'
text+="const math12Ex81=MATH_12_DATA[7].exercises.find(e=>e.title==='Exercise 8.1');math12Ex81.unreviewedProblems=math12Ex81.problems;math12Ex81.problems=math12ReviewedEx81;math12Ex81.pageStart=math12Ex81.pageEnd=221;\n"
text+="const math12CircleTangents=MATH_12_DATA[7].sections.find(s=>s.id==='sec-8-3');math12CircleTangents.unreviewedTheory=math12CircleTangents.theory;math12CircleTangents.sourceBlocks=MATH_12_DATA[7].sourcePages.filter(p=>p.page>=222&&p.page<=230).flatMap(p=>p.blocks);math12CircleTangents.theory=math12CircleTangents.sourceBlocks.map(math12BlockText).join('\\n\\n');math12CircleTangents.sourceReferences=MATH_12_DATA[7].sourcePages.filter(p=>p.page>=222&&p.page<=230).map(p=>({page:p.page,jpg:p.file}));\n"
review82=[{'id':'ex-8-2-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':231,'jpg':'120_page_1.jpg','verification':'All twelve source groups and tangent-length domains reviewed'}]} for i,(q,steps,ans) in enumerate(zip(EX82_QUESTIONS,EX82_STEPS,EX82_ANSWERS),1)]
text+='const math12ReviewedEx82='+json.dumps(review82,ensure_ascii=False)+';\n'
text+="const math12Ex82=MATH_12_DATA[7].exercises.find(e=>e.title==='Exercise 8.2');math12Ex82.unreviewedProblems=math12Ex82.problems;math12Ex82.problems=math12ReviewedEx82;math12Ex82.pageStart=math12Ex82.pageEnd=231;\n"
text+="const math12CircleProperties=MATH_12_DATA[7].sections.find(s=>s.id==='sec-8-4');math12CircleProperties.unreviewedTheory=math12CircleProperties.theory;math12CircleProperties.sourceBlocks=MATH_12_DATA[7].sourcePages.filter(p=>p.page>=232&&p.page<=238).flatMap(p=>{const i=p.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 8.3');return i>=0?p.blocks.slice(0,i):p.blocks;});math12CircleProperties.theory=math12CircleProperties.sourceBlocks.map(math12BlockText).join('\\n\\n');math12CircleProperties.sourceReferences=MATH_12_DATA[7].sourcePages.filter(p=>p.page>=232&&p.page<=238).map(p=>({page:p.page,jpg:p.file}));\n"
review83=[{'id':'ex-8-3-'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':238,'pageEnd':239,'jpg':'123_page_2.jpg','verification':'All six source groups, continuation and invalid contact coordinates visually checked'}]} for i,(q,steps,ans) in enumerate(zip(EX83_QUESTIONS,EX83_STEPS,EX83_ANSWERS),1)]
text+='const math12ReviewedEx83='+json.dumps(review83,ensure_ascii=False)+';\n'
text+="const math12Ex83=MATH_12_DATA[7].exercises.find(e=>e.id==='ex-8-3');math12Ex83.unreviewedTitle=math12Ex83.title;math12Ex83.title=math12Ex83.exercise='Exercise 8.3';math12Ex83.unreviewedProblems=math12Ex83.problems;math12Ex83.problems=math12ReviewedEx83;math12Ex83.pageStart=238;math12Ex83.pageEnd=239;\n"
review8=[]
for num,q,options,answer,steps in UNIT8_REVIEW:
 review8.append({'id':'ex-8-review-'+num,'qNo':num,'question':q+' '+' '.join('('+letter+') '+option for letter,option in zip('abcd',options)),'steps':steps,'solution':'\n'.join(steps),'answer':('Option ('+answer+')') if len(answer)==1 else answer,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':239,'jpg':'124_page_1.jpg','verification':'All source choices visually checked, including missing general center and radius answers'}]})
text+='const math12Review8='+json.dumps(review8,ensure_ascii=False)+';\n'
text+="const math12Rev8=MATH_12_DATA[7].exercises.find(ex=>ex.title==='Review Exercise 8');math12Rev8.unreviewedProblems=math12Rev8.problems;math12Rev8.problems=math12Review8;math12Rev8.pageStart=math12Rev8.pageEnd=239;MATH_12_DATA[7].sourceSummaryBlocks=MATH_12_DATA[7].sourcePages.find(p=>p.page===240).blocks;MATH_12_DATA[7].sourceSummaryReferences=[{page:240,jpg:'124_page_2.jpg',verification:'Complete native summary and enlarged general tangency condition checked'}];\n"
text+='MATH_12_DATA[8].sourcePages='+json.dumps(CONICS2_PAGES,ensure_ascii=False)+';\n'
text+='MATH_12_DATA[8].sourceObjectives='+json.dumps(CONICS2_OBJECTIVES,ensure_ascii=False)+';MATH_12_DATA[8].sourceIntroductionBlocks='+json.dumps(CONICS2_INTRO,ensure_ascii=False)+';\n'
text+="MATH_12_DATA[8].sections.unshift({id:'sec-9-introduction',title:'Introduction to Conics II',sourceBlocks:MATH_12_DATA[8].sourceIntroductionBlocks,theory:MATH_12_DATA[8].sourceIntroductionBlocks.map(math12BlockText).join('\\n\\n'),sourceReferences:[{page:242,jpg:'125_page_2.jpg'}]});const math12Parabola=MATH_12_DATA[8].sections.find(s=>s.id==='sec-9-1');math12Parabola.unreviewedTheory=math12Parabola.theory;math12Parabola.sourceBlocks=MATH_12_DATA[8].sourcePages.find(p=>p.page===242).blocks.slice(MATH_12_DATA[8].sourceIntroductionBlocks.length);math12Parabola.theory=math12Parabola.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Parabola.sourceReferences=[{page:242,jpg:'125_page_2.jpg'}];\n"
text+="math12Parabola.sourceBlocks.push(...MATH_12_DATA[8].sourcePages.filter(p=>p.page>=243&&p.page<=250).flatMap(p=>p.blocks));math12Parabola.theory=math12Parabola.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Parabola.sourceReferences.push(...MATH_12_DATA[8].sourcePages.filter(p=>p.page>=243&&p.page<=250).map(p=>({page:p.page,jpg:p.file})));\n"
text+='const math12Conics2ReviewedExamples='+json.dumps(CONICS2_EXAMPLES,ensure_ascii=False)+';\n'
text+="math12Conics2ReviewedExamples.forEach(e=>{e.problem=e.question;e.given=e.question;e.method='Identify the geometry, apply the relevant relation, and check the original conditions.';e.title='Example '+e.num+' — '+e.title;const old=MATH_12_DATA[8].workedExamples.find(x=>x.num===e.num);if(old){old.unreviewedProblem=old.problem;Object.assign(old,e);}else MATH_12_DATA[8].workedExamples.push(e);});const math12Conics2Nums=new Set(math12Conics2ReviewedExamples.map(e=>e.num)),math12Conics2Seen=new Set();MATH_12_DATA[8].unreviewedDuplicateExamples=[];MATH_12_DATA[8].workedExamples=MATH_12_DATA[8].workedExamples.filter(e=>{if(!math12Conics2Nums.has(e.num))return true;if(math12Conics2Seen.has(e.num)){MATH_12_DATA[8].unreviewedDuplicateExamples.push(e);return false;}math12Conics2Seen.add(e.num);return true;}).sort((a,b)=>Number(a.num)-Number(b.num));\n"
ex91=[]
for i,(q,steps,ans) in enumerate(zip(QUESTIONS91,STEPS91,ANSWERS91),1):
 e={'id':'ex-9-1-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':251 if i<9 else 252,'jpg':'130_page_1.jpg' if i<9 else '130_page_2.jpg','verification':'All printed subparts, graph labels and dimensions visually checked'}]}
 if i==1:e['solutionBlocks']=answer_graphs91()
 if i==2:e['sourceQuestionBlocks']=[graph91(1),graph91(2)]
 if i==10:e['sourceQuestionBlocks']=[arch91()]
 ex91.append(e)
text+='const math12ReviewedExercise91='+json.dumps(ex91,ensure_ascii=False)+';\n'
text+="const math12Ex91=MATH_12_DATA[8].exercises.find(e=>e.title==='Exercise 9.1');math12Ex91.unreviewedProblems=math12Ex91.problems;math12Ex91.problems=math12ReviewedExercise91;math12Ex91.pageStart=251;math12Ex91.pageEnd=252;math12Ex91.sourceContextBlocks=MATH_12_DATA[8].sourcePages.find(p=>p.page===252).blocks.slice(3);\n"
text+="const math12Ellipse=MATH_12_DATA[8].sections.find(s=>s.id==='sec-9-2');math12Ellipse.unreviewedTheory=math12Ellipse.theory;math12Ellipse.sourceBlocks=MATH_12_DATA[8].sourcePages.filter(p=>p.page>=253&&p.page<=263).flatMap(p=>p.blocks);math12Ellipse.theory=math12Ellipse.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Ellipse.sourceReferences=MATH_12_DATA[8].sourcePages.filter(p=>p.page>=253&&p.page<=263).map(p=>({page:p.page,jpg:p.file}));\n"
ex92=[]
for i,(q,steps,ans) in enumerate(zip(QUESTIONS92,STEPS92,ANSWERS92),1):
 e={'id':'ex-9-2-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':264,'jpg':'136_page_2.jpg','verification':'All printed subparts, graph labels and point membership checked'}]}
 if i==1:e['solutionBlocks']=[diagram92(j,True) for j in range(3)]
 if i==2:e['sourceQuestionBlocks']=[diagram92(j) for j in range(3)]
 ex92.append(e)
text+='const math12ReviewedExercise92='+json.dumps(ex92,ensure_ascii=False)+';\n'
text+="const math12Ex92=MATH_12_DATA[8].exercises.find(e=>e.title==='Exercise 9.2');math12Ex92.unreviewedProblems=math12Ex92.problems;math12Ex92.problems=math12ReviewedExercise92;math12Ex92.pageStart=math12Ex92.pageEnd=264;\n"
text+="const math12Hyperbola=MATH_12_DATA[8].sections.find(s=>s.id==='sec-9-3');math12Hyperbola.unreviewedTheory=math12Hyperbola.theory;math12Hyperbola.sourceBlocks=MATH_12_DATA[8].sourcePages.filter(p=>p.page>=265&&p.page<=276).flatMap(p=>p.blocks);math12Hyperbola.theory=math12Hyperbola.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Hyperbola.sourceReferences=MATH_12_DATA[8].sourcePages.filter(p=>p.page>=265&&p.page<=276).map(p=>({page:p.page,jpg:p.file}));\n"
ex93=[]
for i,(q,steps,ans) in enumerate(zip(QUESTIONS93,STEPS93,ANSWERS93),1):
 e={'id':'ex-9-3-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':277 if i<7 else 278,'jpg':'143_page_1.jpg' if i<7 else '143_page_2.jpg','verification':'Every source subpart and original graph label checked'}]}
 if i in [1,6]:e['solutionBlocks']=learning_graphs93(i)
 if i==2:e['sourceQuestionBlocks']=source_graphs93()
 ex93.append(e)
text+='const math12ReviewedExercise93='+json.dumps(ex93,ensure_ascii=False)+';\n'
text+="const math12Ex93=MATH_12_DATA[8].exercises.find(e=>e.title==='Exercise 9.3');math12Ex93.unreviewedProblems=math12Ex93.problems;math12Ex93.problems=math12ReviewedExercise93;math12Ex93.pageStart=277;math12Ex93.pageEnd=278;math12Ex93.sourceContextBlocks=MATH_12_DATA[8].sourcePages.find(p=>p.page===278).blocks.slice(3);\n"
text+="const math12Axes=MATH_12_DATA[8].sections.find(s=>s.id==='sec-9-4');math12Axes.unreviewedTheory=math12Axes.theory;math12Axes.sourceBlocks=MATH_12_DATA[8].sourcePages.filter(p=>p.page>=279&&p.page<=282).flatMap(p=>p.blocks);math12Axes.theory=math12Axes.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Axes.sourceReferences=MATH_12_DATA[8].sourcePages.filter(p=>p.page>=279&&p.page<=282).map(p=>({page:p.page,jpg:p.file}));\n"
ex94=[]
for i,(q,steps,ans) in enumerate(zip(QUESTIONS94,STEPS94,ANSWERS94),1):
 ex94.append({'id':'ex-9-4-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':283,'jpg':'146_page_1.jpg','verification':'All angle signs, shifted origins and conic coefficients visually checked; expansions independently computed'}]})
text+='const math12ReviewedExercise94='+json.dumps(ex94,ensure_ascii=False)+';\n'
text+="const math12Ex94=MATH_12_DATA[8].exercises.find(e=>e.title==='Exercise 9.4');math12Ex94.unreviewedProblems=math12Ex94.problems;math12Ex94.problems=math12ReviewedExercise94;math12Ex94.pageStart=math12Ex94.pageEnd=283;const math12Source283=MATH_12_DATA[8].sourcePages.find(p=>p.page===283);math12Axes.sourceBlocks.push(...math12Source283.blocks.slice(0,math12Source283.blocks.findIndex(b=>b.type==='heading'&&b.text==='Exercise 9.4')));math12Axes.theory=math12Axes.sourceBlocks.map(math12BlockText).join('\\n\\n');math12Axes.sourceReferences.push({page:283,jpg:'146_page_1.jpg'});MATH_12_DATA[8].sourceSummaryBlocks=MATH_12_DATA[8].sourcePages.filter(p=>p.page===284||p.page===285).flatMap(p=>p.blocks);MATH_12_DATA[8].sourceSummaryReferences=[{page:284,jpg:'146_page_2.jpg'},{page:285,jpg:'147_page_1.jpg'}];MATH_12_DATA[8].unreviewedExercises=MATH_12_DATA[8].exercises.filter(e=>!['Exercise 9.1','Exercise 9.2','Exercise 9.3','Exercise 9.4'].includes(e.title));MATH_12_DATA[8].exercises=MATH_12_DATA[8].exercises.filter(e=>['Exercise 9.1','Exercise 9.2','Exercise 9.3','Exercise 9.4'].includes(e.title));\n"
text+='MATH_12_DATA[9].sourcePages='+json.dumps(ODE_PAGES,ensure_ascii=False)+';\n'
text+='MATH_12_DATA[9].sourceObjectives='+json.dumps(ODE_OBJECTIVES,ensure_ascii=False)+';MATH_12_DATA[9].sourceIntroductionBlocks='+json.dumps(ODE_INTRO,ensure_ascii=False)+';\n'
text+="MATH_12_DATA[9].sections.unshift({id:'sec-10-introduction',title:'Introduction to Differential Equations',sourceBlocks:MATH_12_DATA[9].sourceIntroductionBlocks,theory:MATH_12_DATA[9].sourceIntroductionBlocks.map(math12BlockText).join('\\n\\n'),sourceReferences:[{page:286,jpg:'147_page_2.jpg'}]});const math12ODEDefinitions=MATH_12_DATA[9].sections.find(s=>s.id==='sec-10-1');math12ODEDefinitions.unreviewedTheory=math12ODEDefinitions.theory;math12ODEDefinitions.sourceBlocks=MATH_12_DATA[9].sourcePages[0].blocks.slice(MATH_12_DATA[9].sourceIntroductionBlocks.length).concat(MATH_12_DATA[9].sourcePages.filter(p=>p.page>=287&&p.page<=288).flatMap(p=>p.blocks));math12ODEDefinitions.theory=math12ODEDefinitions.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ODEDefinitions.sourceReferences=MATH_12_DATA[9].sourcePages.map(p=>({page:p.page,jpg:p.file}));\n"
text+='const math12ODEReviewedExamples='+json.dumps(ODE_EXAMPLES,ensure_ascii=False)+';\n'
text+="math12ODEReviewedExamples.forEach(e=>{e.problem=e.question;e.given=e.question;e.method='Identify derivatives, apply the definition, and verify the original equation and conditions.';e.title='Example '+e.num+' — '+e.title;const old=MATH_12_DATA[9].workedExamples.find(x=>x.num===e.num);if(old){old.unreviewedProblem=old.problem;Object.assign(old,e);}else MATH_12_DATA[9].workedExamples.push(e);});\n"
text+="math12ODEDefinitions.sourceBlocks.push(...MATH_12_DATA[9].sourcePages.find(p=>p.page===289).blocks.slice(0,MATH_12_DATA[9].sourcePages.find(p=>p.page===289).blocks.length-"+str(len(ODE_FORMATION))+"));math12ODEDefinitions.theory=math12ODEDefinitions.sourceBlocks.map(math12BlockText).join('\\n\\n');const math12ODEFormation=MATH_12_DATA[9].sections.find(s=>s.id==='sec-10-2');math12ODEFormation.unreviewedTheory=math12ODEFormation.theory;\n"
text+='math12ODEFormation.sourceBlocks='+json.dumps(ODE_FORMATION,ensure_ascii=False)+';\n'
text+="math12ODEFormation.theory=math12ODEFormation.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ODEFormation.sourceReferences=[{page:289,jpg:'149_page_1.jpg'}];\n"
ex101=[]
for i,(q,steps,ans) in enumerate(zip(EX101_QUESTIONS,EX101_STEPS,EX101_ANSWERS),1):
 ex101.append({'id':'ex-10-1-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':290,'jpg':'149_page_2.jpg','verification':'Enlarged source exercise expressions checked; Q2(c) exponent remains explicitly partial'}]})
ex101[1].update(sourceQuestionBlocks=[EX101_PAGES[0]['blocks'][6]],sourceStatus='partial_source_legibility')
text+='const math12ReviewedExercise101='+json.dumps(ex101,ensure_ascii=False)+';\n'
text+="const math12Ex101=MATH_12_DATA[9].exercises.find(e=>e.title==='Exercise 10.1');math12Ex101.unreviewedProblems=math12Ex101.problems;math12Ex101.problems=math12ReviewedExercise101;math12Ex101.pageStart=math12Ex101.pageEnd=290;math12Ex101.sourceContextBlocks=MATH_12_DATA[9].sourcePages.find(p=>p.page===290).blocks.slice(7);\n"
text+="const math12ODESolutions=MATH_12_DATA[9].sections.find(s=>s.id==='sec-10-3');math12ODESolutions.unreviewedTheory=math12ODESolutions.theory;math12ODESolutions.sourceBlocks=MATH_12_DATA[9].sourcePages.filter(p=>p.page>=291&&p.page<=294).flatMap(p=>p.blocks);math12ODESolutions.theory=math12ODESolutions.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ODESolutions.sourceReferences=MATH_12_DATA[9].sourcePages.filter(p=>p.page>=291&&p.page<=294).map(p=>({page:p.page,jpg:p.file}));const math12ODENums=new Set(math12ODEReviewedExamples.map(e=>e.num)),math12ODESeen=new Set();MATH_12_DATA[9].unreviewedDuplicateExamples=[];MATH_12_DATA[9].workedExamples=MATH_12_DATA[9].workedExamples.filter(e=>{if(!math12ODENums.has(e.num))return true;if(math12ODESeen.has(e.num)){MATH_12_DATA[9].unreviewedDuplicateExamples.push(e);return false;}math12ODESeen.add(e.num);return true;}).sort((a,b)=>Number(a.num)-Number(b.num));\n"
text+='math12ODESolutions.sourceBlocks.push(...'+json.dumps(BACTERIAL_END,ensure_ascii=False)+');\n'
text+="math12ODESolutions.theory=math12ODESolutions.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ODESolutions.sourceReferences.push({page:295,jpg:'152_page_1.jpg'});const math12ODETrajectories=MATH_12_DATA[9].sections.find(s=>s.id==='sec-10-4');math12ODETrajectories.unreviewedTheory=math12ODETrajectories.theory;\n"
text+='math12ODETrajectories.sourceBlocks='+json.dumps(TRAJECTORY_INTRO,ensure_ascii=False)+';\n'
text+="math12ODETrajectories.theory=math12ODETrajectories.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ODETrajectories.sourceReferences=[{page:295,jpg:'152_page_1.jpg'}];\n"
text+="math12ODETrajectories.sourceBlocks.push(...MATH_12_DATA[9].sourcePages.find(p=>p.page===296).blocks);math12ODETrajectories.theory=math12ODETrajectories.sourceBlocks.map(math12BlockText).join('\\n\\n');math12ODETrajectories.sourceReferences.push({page:296,jpg:'152_page_2.jpg'});\n"
ex102=[]
for i,(q,steps,ans) in enumerate(zip(EX102_QUESTIONS,EX102_STEPS,EX102_ANSWERS),1):
 ex102.append({'id':'ex-10-2-q'+str(i),'qNo':str(i) if i<11 else '10 (repeated)','question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':297,'jpg':'153_page_1.jpg','verification':'All source expressions and initial values checked; repeated question number retained'}]})
text+='const math12ReviewedExercise102='+json.dumps(ex102,ensure_ascii=False)+';\n'
text+="const math12Ex102=MATH_12_DATA[9].exercises.find(e=>e.title==='Exercise 10.2');math12Ex102.unreviewedProblems=math12Ex102.problems;math12Ex102.problems=math12ReviewedExercise102;math12Ex102.pageStart=math12Ex102.pageEnd=297;\n"
review10=[]
for n,q,opts,steps,ans in REVIEW10_ITEMS:
 review10.append({'id':'review-10-'+n,'qNo':n,'question':q+' (a) '+opts[0]+'; (b) '+opts[1]+'; (c) '+opts[2]+'; (d) '+opts[3]+'.','steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':298,'jpg':'153_page_2.jpg','verification':'All four source choices checked visually; literal stem mismatch retained'}]})
text+='const math12ReviewedReview10='+json.dumps(review10,ensure_ascii=False)+';\n'
text+="const math12Rev10=MATH_12_DATA[9].exercises.find(e=>e.title==='Review Exercise 10');math12Rev10.unreviewedProblems=math12Rev10.problems;math12Rev10.problems=math12ReviewedReview10;math12Rev10.pageStart=math12Rev10.pageEnd=298;\n"
text+='MATH_12_DATA[9].sourceSummaryBlocks='+json.dumps(UNIT10_SUMMARY+UNIT10_HISTORY,ensure_ascii=False)+';MATH_12_DATA[9].sourceSummaryReferences=[{page:299,jpg:"154_page_1.jpg"}];\n'
text+='MATH_12_DATA[10].sourcePages='+json.dumps(PARTIAL_PAGES,ensure_ascii=False)+';MATH_12_DATA[10].sourceObjectives='+json.dumps(PARTIAL_OBJECTIVES,ensure_ascii=False)+';MATH_12_DATA[10].sourceIntroductionBlocks='+json.dumps(PARTIAL_INTRO,ensure_ascii=False)+';\n'
text+="MATH_12_DATA[10].sections.unshift({id:'sec-11-introduction',title:'Introduction to Partial Differentiation',sourceBlocks:MATH_12_DATA[10].sourceIntroductionBlocks,theory:MATH_12_DATA[10].sourceIntroductionBlocks.map(math12BlockText).join('\\n\\n'),sourceReferences:[{page:300,jpg:'154_page_2.jpg'}]});const math12PartialFunctions=MATH_12_DATA[10].sections.find(s=>s.id==='sec-11-1');math12PartialFunctions.unreviewedTheory=math12PartialFunctions.theory;math12PartialFunctions.sourceBlocks=MATH_12_DATA[10].sourcePages[0].blocks.slice(MATH_12_DATA[10].sourceIntroductionBlocks.length).concat(MATH_12_DATA[10].sourcePages.filter(p=>p.page>=301&&p.page<=302).flatMap(p=>p.blocks));math12PartialFunctions.theory=math12PartialFunctions.sourceBlocks.map(math12BlockText).join('\\n\\n');math12PartialFunctions.sourceReferences=MATH_12_DATA[10].sourcePages.map(p=>({page:p.page,jpg:p.file}));\n"
text+='const math12PartialReviewedExamples='+json.dumps(PARTIAL_EXAMPLES,ensure_ascii=False)+';\n'
text+="math12PartialReviewedExamples.forEach(e=>{e.problem=e.question;e.given=e.question;e.method='Identify the independent variables, apply the definition, and verify the result.';e.title='Example '+e.num+' — '+e.title;const old=MATH_12_DATA[10].workedExamples.find(x=>x.num===e.num);if(old){old.unreviewedProblem=old.problem;Object.assign(old,e);}else MATH_12_DATA[10].workedExamples.push(e);});\n"
text+='math12PartialFunctions.sourceBlocks.push(...'+json.dumps(TEMPERATURE_END+PARTIAL_EULER_HISTORY,ensure_ascii=False)+');\n'
text+="math12PartialFunctions.theory=math12PartialFunctions.sourceBlocks.map(math12BlockText).join('\\n\\n');\n"
ex111=[]
for i,(q,steps,ans) in enumerate(zip(EX111_QUESTIONS,EX111_STEPS,EX111_ANSWERS),1):
 ex111.append({'id':'ex-11-1-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':303,'jpg':'156_page_1.jpg','verification':'All source expressions checked; evaluation/composition ambiguity separately explained'}]})
text+='const math12ReviewedExercise111='+json.dumps(ex111,ensure_ascii=False)+';\n'
text+="const math12Ex111=MATH_12_DATA[10].exercises.find(e=>e.title==='Exercise 11.1');math12Ex111.unreviewedProblems=math12Ex111.problems;math12Ex111.problems=math12ReviewedExercise111;math12Ex111.pageStart=math12Ex111.pageEnd=303;\n"
text+="const math12EulerTheorem=MATH_12_DATA[10].sections.find(s=>s.id==='sec-11-2');math12EulerTheorem.unreviewedTheory=math12EulerTheorem.theory;math12EulerTheorem.sourceBlocks=MATH_12_DATA[10].sourcePages.filter(p=>p.page>=304&&p.page<=305).flatMap(p=>p.blocks);math12EulerTheorem.theory=math12EulerTheorem.sourceBlocks.map(math12BlockText).join('\\n\\n');math12EulerTheorem.sourceReferences=MATH_12_DATA[10].sourcePages.filter(p=>p.page>=304&&p.page<=305).map(p=>({page:p.page,jpg:p.file}));\n"
text+='math12EulerTheorem.sourceBlocks.push(...'+json.dumps(PARTIAL_MAPLE,ensure_ascii=False)+');\n'
text+="math12EulerTheorem.theory=math12EulerTheorem.sourceBlocks.map(math12BlockText).join('\\n\\n');math12EulerTheorem.sourceReferences.push({page:306,jpg:'157_page_2.jpg'});\n"
ex112=[]
for i,(q,steps,ans) in enumerate(zip(EX112_QUESTIONS,EX112_STEPS,EX112_ANSWERS),1):
 ex112.append({'id':'ex-11-2-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':306,'jpg':'157_page_2.jpg'},{'page':307,'jpg':'158_page_1.jpg','verification':'Full continuation and leading minus visually checked'}]})
text+='const math12ReviewedExercise112='+json.dumps(ex112,ensure_ascii=False)+';\n'
text+="const math12Ex112=MATH_12_DATA[10].exercises.find(e=>e.title==='Exercise 11.2');math12Ex112.unreviewedProblems=math12Ex112.problems;math12Ex112.problems=math12ReviewedExercise112;math12Ex112.pageStart=306;math12Ex112.pageEnd=307;\n"
review11=[]
for n,q,opts,steps,ans in REVIEW11_ITEMS:
 review11.append({'id':'review-11-'+n,'qNo':n,'question':q+' (a) '+opts[0]+'; (b) '+opts[1]+'; (c) '+opts[2]+'; (d) '+opts[3]+'.','steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':307,'jpg':'158_page_1.jpg','verification':'All choices and label defects visually checked'}]})
text+='const math12ReviewedReview11='+json.dumps(review11,ensure_ascii=False)+';\n'
text+="const math12Rev11=MATH_12_DATA[10].exercises.find(e=>e.title==='Review Exercise 11');math12Rev11.unreviewedProblems=math12Rev11.problems;math12Rev11.problems=math12ReviewedReview11;math12Rev11.pageStart=math12Rev11.pageEnd=307;\n"
text+='MATH_12_DATA[10].sourceSummaryBlocks='+json.dumps(UNIT11_SUMMARY+UNIT11_HISTORY,ensure_ascii=False)+';MATH_12_DATA[10].sourceSummaryReferences=[{page:308,jpg:"158_page_2.jpg"}];\n'
text+='MATH_12_DATA[11].sourcePages='+json.dumps(NUMERICAL_PAGES,ensure_ascii=False)+';MATH_12_DATA[11].sourceObjectives='+json.dumps(NUMERICAL_OBJECTIVES,ensure_ascii=False)+';MATH_12_DATA[11].sourceIntroductionBlocks='+json.dumps(NUMERICAL_INTRO,ensure_ascii=False)+';\n'
text+="MATH_12_DATA[11].sections.unshift({id:'sec-12-introduction',title:'Introduction to Numerical Methods',sourceBlocks:MATH_12_DATA[11].sourceIntroductionBlocks,theory:MATH_12_DATA[11].sourceIntroductionBlocks.map(math12BlockText).join('\\n\\n'),sourceReferences:[{page:309,jpg:'159_page_1.jpg'}]});const math12NumericalRoots=MATH_12_DATA[11].sections.find(s=>s.id==='sec-12-1');math12NumericalRoots.unreviewedTheory=math12NumericalRoots.theory;math12NumericalRoots.sourceBlocks=MATH_12_DATA[11].sourcePages[0].blocks.slice(MATH_12_DATA[11].sourceIntroductionBlocks.length).concat(MATH_12_DATA[11].sourcePages.filter(p=>p.page>=310&&p.page<=315).flatMap(p=>p.blocks));math12NumericalRoots.theory=math12NumericalRoots.sourceBlocks.map(math12BlockText).join('\\n\\n');math12NumericalRoots.sourceReferences=MATH_12_DATA[11].sourcePages.map(p=>({page:p.page,jpg:p.file}));\n"
text+='const math12NumericalReviewedExamples='+json.dumps(NUMERICAL_EXAMPLES,ensure_ascii=False)+';\n'
text+="math12NumericalReviewedExamples.forEach(e=>{e.problem=e.question;e.given=e.question;e.method='Verify assumptions, calculate each iterate, and check the remaining bracket or residual.';e.title='Example '+e.num+' — '+e.title;const old=MATH_12_DATA[11].workedExamples.find(x=>x.num===e.num);if(old){old.unreviewedProblem=old.problem;Object.assign(old,e);}else MATH_12_DATA[11].workedExamples.push(e);});\n"
text+='math12NumericalRoots.sourceBlocks.push(...'+json.dumps(NUMERICAL_QUSTA_HISTORY,ensure_ascii=False)+');\n'
text+="math12NumericalRoots.theory=math12NumericalRoots.sourceBlocks.map(math12BlockText).join('\\n\\n');\n"
ex121=[]
for i,(q,steps,ans) in enumerate(zip(EX121_QUESTIONS,EX121_STEPS,EX121_ANSWERS),1):
 ex121.append({'id':'ex-12-1-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':316,'jpg':'162_page_2.jpg','verification':'All source intervals and starting values checked; iterations independently computed'}]})
text+='const math12ReviewedExercise121='+json.dumps(ex121,ensure_ascii=False)+';\n'
text+="const math12Ex121=MATH_12_DATA[11].exercises.find(e=>e.title==='Exercise 12.1');math12Ex121.unreviewedProblems=math12Ex121.problems;math12Ex121.problems=math12ReviewedExercise121;math12Ex121.pageStart=math12Ex121.pageEnd=316;\n"
text+="const math12NumericalQuadrature=MATH_12_DATA[11].sections.find(s=>s.id==='sec-12-2');math12NumericalQuadrature.unreviewedTheory=math12NumericalQuadrature.theory;math12NumericalQuadrature.sourceBlocks=MATH_12_DATA[11].sourcePages.filter(p=>p.page>=317&&p.page<=322).flatMap(p=>p.blocks);math12NumericalQuadrature.theory=math12NumericalQuadrature.sourceBlocks.map(math12BlockText).join('\\n\\n');math12NumericalQuadrature.sourceReferences=MATH_12_DATA[11].sourcePages.filter(p=>p.page>=317&&p.page<=322).map(p=>({page:p.page,jpg:p.file}));\n"
ex122=[]
for i,(q,steps,ans) in enumerate(zip(EX122_QUESTIONS,EX122_STEPS,EX122_ANSWERS),1):
 v={'id':'ex-12-2-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':323,'jpg':'166_page_1.jpg','verification':'All bounds and source wording checked; sums independently calculated'}]}
 if i in EX122_GRAPHS:v['solutionBlocks']=EX122_GRAPHS[i]
 if i==5:v.update(solutionStatus='partial: Source omits the integrand; a supplemental sample is shown.',sourceStatus='under_specified_source_problem')
 ex122.append(v)
text+='const math12ReviewedExercise122='+json.dumps(ex122,ensure_ascii=False)+';\n'
text+="const math12Ex122=MATH_12_DATA[11].exercises.find(e=>e.title==='Exercise 12.2');math12Ex122.unreviewedProblems=math12Ex122.problems;math12Ex122.problems=math12ReviewedExercise122;math12Ex122.pageStart=math12Ex122.pageEnd=323;\n"
review12=[]
for n,q,opts,steps,ans in REVIEW12_ITEMS:
 review12.append({'id':'review-12-'+n,'qNo':n,'question':q+' (a) '+opts[0]+'; (b) '+opts[1]+'; (c) '+opts[2]+'; (d) '+opts[3]+'.','steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':324,'jpg':'166_page_2.jpg','verification':'All source choices and wording anomalies checked visually'}]})
text+='const math12ReviewedReview12='+json.dumps(review12,ensure_ascii=False)+';\n'
text+="const math12Rev12=MATH_12_DATA[11].exercises.find(e=>e.title==='Review Exercise 12');math12Rev12.unreviewedProblems=math12Rev12.problems;math12Rev12.problems=math12ReviewedReview12;math12Rev12.pageStart=math12Rev12.pageEnd=324;\n"
projects12=[]
for i,(q,steps,ans) in enumerate(zip(PROJECT12_QUESTIONS,PROJECT12_STEPS,PROJECT12_ANSWERS),1):
 projects12.append({'id':'ex-12-project-q'+str(i),'qNo':str(i),'question':q,'steps':steps,'solution':'\n'.join(steps),'answer':ans,'progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement — chosen project sample','sourceReferences':[{'page':324,'jpg':'166_page_2.jpg','verification':'Source open-choice project prompts checked'}]})
projects12[0]['solutionBlocks']=[PROJECT12_GRAPH()]
text+='MATH_12_DATA[11].exercises.push({id:"ex-12-source-project",title:"Project",pageStart:324,pageEnd:324,problems:'+json.dumps(projects12,ensure_ascii=False)+'});\n'
text+='MATH_12_DATA[11].sourceSummaryBlocks='+json.dumps(UNIT12_SUMMARY+UNIT12_HISTORY,ensure_ascii=False)+';MATH_12_DATA[11].sourceSummaryReferences=[{page:325,jpg:"167_page_1.jpg"}];\n'
text+="MATH_12_DATA[11].unreviewedExercises=MATH_12_DATA[11].exercises.filter(e=>!['Exercise 12.1','Exercise 12.2','Review Exercise 12','Project'].includes(e.title));MATH_12_DATA[11].exercises=MATH_12_DATA[11].exercises.filter(e=>['Exercise 12.1','Exercise 12.2','Review Exercise 12','Project'].includes(e.title));const math12Source323=MATH_12_DATA[11].sourcePages.find(p=>p.page===323);math12NumericalQuadrature.sourceBlocks.push(...math12Source323.blocks.slice(math12Source323.blocks.findIndex(b=>b.type==='heading'&&b.text==='History')));math12NumericalQuadrature.theory=math12NumericalQuadrature.sourceBlocks.map(math12BlockText).join('\\n\\n');math12NumericalQuadrature.sourceReferences.push({page:323,jpg:'166_page_1.jpg'});\n"
text+='MATH_12_DATA[11].sourceAnswerPages='+json.dumps(ANSWER_PAGES,ensure_ascii=False)+';\n'
text+='const math12Answer21=MATH_12_DATA[1].exercises.find(e=>e.title==="Exercise 2.1");math12Answer21.sourceContextBlocks=[...(math12Answer21.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 326"},...MATH_12_DATA[11].sourceAnswerPages[0].blocks];math12Answer21.sourceAnswerReferences=[{page:326,jpg:"167_page_2.jpg"}];\n'
text+='math12Answer21.sourceContextBlocks.push({type:"heading",text:"Printed answer key — page 327"},...'+json.dumps(ANSWER327_EX21,ensure_ascii=False)+');math12Answer21.sourceAnswerReferences.push({page:327,jpg:"168_page_1.jpg"});\n'
text+='const math12Answer22=MATH_12_DATA[1].exercises.find(e=>e.title==="Exercise 2.2");math12Answer22.sourceContextBlocks=[...(math12Answer22.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 327"},...'+json.dumps(ANSWER327_EX22,ensure_ascii=False)+'];math12Answer22.sourceAnswerReferences=[{page:327,jpg:"168_page_1.jpg"}];\n'
text+='math12Answer22.sourceContextBlocks.push({type:"heading",text:"Printed answer key — page 328"},...'+json.dumps(ANSWER328_BLOCKS,ensure_ascii=False)+');math12Answer22.sourceAnswerReferences.push({page:328,jpg:"168_page_2.jpg"});\n'
text+='math12Answer22.sourceContextBlocks.push({type:"heading",text:"Printed answer key — pages 329–330"},...'+json.dumps(BLOCKS329+BLOCKS330,ensure_ascii=False)+');math12Answer22.sourceAnswerReferences.push({page:329,jpg:"169_page_1.jpg"},{page:330,jpg:"169_page_2.jpg"});\n'
text+='MATH_12_DATA[1].exercises.find(e=>e.title==="Exercise 2.3").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 331"},...'+json.dumps(ANSWER331_EX23,ensure_ascii=False)+'];MATH_12_DATA[1].exercises.find(e=>e.title==="Exercise 2.3").sourceAnswerReferences=[{page:331,jpg:"170_page_1.jpg"}];\n'
text+='MATH_12_DATA[1].exercises.find(e=>e.title==="Exercise 2.4").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 331"},...'+json.dumps(ANSWER331_EX24,ensure_ascii=False)+'];MATH_12_DATA[1].exercises.find(e=>e.title==="Exercise 2.4").sourceAnswerReferences=[{page:331,jpg:"170_page_1.jpg"}];\n'
text+='MATH_12_DATA[1].exercises.find(e=>e.title==="Review Exercise 2").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 331"},...'+json.dumps(ANSWER331_REVIEW,ensure_ascii=False)+'];MATH_12_DATA[1].exercises.find(e=>e.title==="Review Exercise 2").sourceAnswerReferences=[{page:331,jpg:"170_page_1.jpg"}];\n'
text+='MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.1").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 332"},...'+json.dumps(ANSWER332_EX31,ensure_ascii=False)+'];MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.1").sourceAnswerReferences=[{page:332,jpg:"170_page_2.jpg"}];\n'
text+='MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.2").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 332"},...'+json.dumps(ANSWER332_EX32,ensure_ascii=False)+'];MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.2").sourceAnswerReferences=[{page:332,jpg:"170_page_2.jpg"}];\n'
text+='MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.3").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 333"},...'+json.dumps(ANSWER333_EX33,ensure_ascii=False)+'];MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.3").sourceAnswerReferences=[{page:333,jpg:"171_page_1.jpg"}];\n'
text+='MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.4").sourceContextBlocks=[{type:"heading",text:"Printed answer key — page 333"},...'+json.dumps(ANSWER333_EX34,ensure_ascii=False)+'];MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.4").sourceAnswerReferences=[{page:333,jpg:"171_page_1.jpg"}];\n'
text+='const math12Key334_2_Exercise34=MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.4");math12Key334_2_Exercise34.sourceContextBlocks=[...(math12Key334_2_Exercise34.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 334"},...'+json.dumps(ANSWER334_EX34,ensure_ascii=False)+'];\n'
text+='const math12Key334_2_Exercise35=MATH_12_DATA[2].exercises.find(e=>e.title==="Exercise 3.5");math12Key334_2_Exercise35.sourceContextBlocks=[...(math12Key334_2_Exercise35.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 334"},...'+json.dumps(ANSWER334_EX35,ensure_ascii=False)+'];\n'
text+='const math12Key334_2_ReviewExercise3=MATH_12_DATA[2].exercises.find(e=>e.title==="Review Exercise 3");math12Key334_2_ReviewExercise3.sourceContextBlocks=[...(math12Key334_2_ReviewExercise3.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 334"},...'+json.dumps(ANSWER334_REVIEW3,ensure_ascii=False)+'];\n'
text+='const math12Key334_3_Exercise41=MATH_12_DATA[3].exercises.find(e=>e.title==="Exercise 4.1");math12Key334_3_Exercise41.sourceContextBlocks=[...(math12Key334_3_Exercise41.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 334"},...'+json.dumps(ANSWER334_EX41,ensure_ascii=False)+'];\n'
for key334 in ['math12Key334_2_Exercise34','math12Key334_2_Exercise35','math12Key334_2_ReviewExercise3','math12Key334_3_Exercise41']:
 text+=key334+'.sourceAnswerReferences=[...('+key334+'.sourceAnswerReferences||[]),{page:334,jpg:"171_page_2.jpg"}];\n'
text+='const math12Key335Exercise41=MATH_12_DATA[3].exercises.find(e=>e.title==="Exercise 4.1");math12Key335Exercise41.sourceContextBlocks=[...(math12Key335Exercise41.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 335"},...'+json.dumps(ANSWER335_EX41,ensure_ascii=False)+'];math12Key335Exercise41.sourceAnswerReferences=[...(math12Key335Exercise41.sourceAnswerReferences||[]),{page:335,jpg:"172_page_1.jpg"}];\n'
text+='const math12Key335Exercise42=MATH_12_DATA[3].exercises.find(e=>e.title==="Exercise 4.2");math12Key335Exercise42.sourceContextBlocks=[...(math12Key335Exercise42.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 335"},...'+json.dumps(ANSWER335_EX42,ensure_ascii=False)+'];math12Key335Exercise42.sourceAnswerReferences=[...(math12Key335Exercise42.sourceAnswerReferences||[]),{page:335,jpg:"172_page_1.jpg"}];\n'
text+='const math12Key335Exercise43=MATH_12_DATA[3].exercises.find(e=>e.title==="Exercise 4.3");math12Key335Exercise43.sourceContextBlocks=[...(math12Key335Exercise43.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 335"},...'+json.dumps(ANSWER335_EX43,ensure_ascii=False)+'];math12Key335Exercise43.sourceAnswerReferences=[...(math12Key335Exercise43.sourceAnswerReferences||[]),{page:335,jpg:"172_page_1.jpg"}];\n'
text+='const math12Key336Exercise43=MATH_12_DATA[3].exercises.find(e=>e.title==="Exercise 4.3");math12Key336Exercise43.sourceContextBlocks=[...(math12Key336Exercise43.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 336"},...'+json.dumps(ANSWER336_EX43,ensure_ascii=False)+'];math12Key336Exercise43.sourceAnswerReferences=[...(math12Key336Exercise43.sourceAnswerReferences||[]),{page:336,jpg:"172_page_2.jpg"}];\n'
text+='const math12Key336ReviewExercise4=MATH_12_DATA[3].exercises.find(e=>e.title==="Review Exercise 4");math12Key336ReviewExercise4.sourceContextBlocks=[...(math12Key336ReviewExercise4.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 336"},...'+json.dumps(ANSWER336_REVIEW4,ensure_ascii=False)+'];math12Key336ReviewExercise4.sourceAnswerReferences=[...(math12Key336ReviewExercise4.sourceAnswerReferences||[]),{page:336,jpg:"172_page_2.jpg"}];\n'
text+='const math12Key336Exercise51=MATH_12_DATA[4].exercises.find(e=>e.title==="Exercise 5.1");math12Key336Exercise51.sourceContextBlocks=[...(math12Key336Exercise51.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 336"},...'+json.dumps(ANSWER336_EX51,ensure_ascii=False)+'];math12Key336Exercise51.sourceAnswerReferences=[...(math12Key336Exercise51.sourceAnswerReferences||[]),{page:336,jpg:"172_page_2.jpg"}];\n'
text+='const math12Key337Exercise51=MATH_12_DATA[4].exercises.find(e=>e.title==="Exercise 5.1");math12Key337Exercise51.sourceContextBlocks=[...(math12Key337Exercise51.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 337"},...'+json.dumps(ANSWER337_EX51,ensure_ascii=False)+'];math12Key337Exercise51.sourceAnswerReferences=[...(math12Key337Exercise51.sourceAnswerReferences||[]),{page:337,jpg:"173_page_1.jpg"}];\n'
text+='const math12Key337Exercise52=MATH_12_DATA[4].exercises.find(e=>e.title==="Exercise 5.2");math12Key337Exercise52.sourceContextBlocks=[...(math12Key337Exercise52.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 337"},...'+json.dumps(ANSWER337_EX52,ensure_ascii=False)+'];math12Key337Exercise52.sourceAnswerReferences=[...(math12Key337Exercise52.sourceAnswerReferences||[]),{page:337,jpg:"173_page_1.jpg"}];\n'
text+='const math12Key337ReviewExercise5=MATH_12_DATA[4].exercises.find(e=>e.title==="Review Exercise 5");math12Key337ReviewExercise5.sourceContextBlocks=[...(math12Key337ReviewExercise5.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 337"},...'+json.dumps(ANSWER337_REVIEW5,ensure_ascii=False)+'];math12Key337ReviewExercise5.sourceAnswerReferences=[...(math12Key337ReviewExercise5.sourceAnswerReferences||[]),{page:337,jpg:"173_page_1.jpg"}];\n'
text+='const math12Key337Exercise61=MATH_12_DATA[5].exercises.find(e=>e.title==="Exercise 6.1");math12Key337Exercise61.sourceContextBlocks=[...(math12Key337Exercise61.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 337"},...'+json.dumps(ANSWER337_EX61,ensure_ascii=False)+'];math12Key337Exercise61.sourceAnswerReferences=[...(math12Key337Exercise61.sourceAnswerReferences||[]),{page:337,jpg:"173_page_1.jpg"}];\n'
text+='const math12Key338Exercise61=MATH_12_DATA[5].exercises.find(e=>e.title==="Exercise 6.1");math12Key338Exercise61.sourceContextBlocks=[...(math12Key338Exercise61.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 338"},...'+json.dumps(ANSWER338_EX61,ensure_ascii=False)+'];math12Key338Exercise61.sourceAnswerReferences=[...(math12Key338Exercise61.sourceAnswerReferences||[]),{page:338,jpg:"173_page_2.jpg"}];\n'
text+='const math12Key338Exercise62=MATH_12_DATA[5].exercises.find(e=>e.title==="Exercise 6.2");math12Key338Exercise62.sourceContextBlocks=[...(math12Key338Exercise62.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 338"},...'+json.dumps(ANSWER338_EX62,ensure_ascii=False)+'];math12Key338Exercise62.sourceAnswerReferences=[...(math12Key338Exercise62.sourceAnswerReferences||[]),{page:338,jpg:"173_page_2.jpg"}];\n'
text+='const math12Key338Exercise63=MATH_12_DATA[5].exercises.find(e=>e.title==="Exercise 6.3");math12Key338Exercise63.sourceContextBlocks=[...(math12Key338Exercise63.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 338"},...'+json.dumps(ANSWER338_EX63,ensure_ascii=False)+'];math12Key338Exercise63.sourceAnswerReferences=[...(math12Key338Exercise63.sourceAnswerReferences||[]),{page:338,jpg:"173_page_2.jpg"}];\n'
text+='const math12Key339Exercise63=MATH_12_DATA[5].exercises.find(e=>e.title==="Exercise 6.3");math12Key339Exercise63.sourceContextBlocks=[...(math12Key339Exercise63.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 339"},...'+json.dumps(ANSWER339_EX63,ensure_ascii=False)+'];math12Key339Exercise63.sourceAnswerReferences=[...(math12Key339Exercise63.sourceAnswerReferences||[]),{page:339,jpg:"174_page_1.jpg"}];\n'
text+='const math12Key339Exercise64=MATH_12_DATA[5].exercises.find(e=>e.title==="Exercise 6.4");math12Key339Exercise64.sourceContextBlocks=[...(math12Key339Exercise64.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 339"},...'+json.dumps(ANSWER339_EX64,ensure_ascii=False)+'];math12Key339Exercise64.sourceAnswerReferences=[...(math12Key339Exercise64.sourceAnswerReferences||[]),{page:339,jpg:"174_page_1.jpg"}];\n'
text+='const math12Key339ReviewExercise6=MATH_12_DATA[5].exercises.find(e=>e.title==="Review Exercise 6");math12Key339ReviewExercise6.sourceContextBlocks=[...(math12Key339ReviewExercise6.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 339"},...'+json.dumps(ANSWER339_REVIEW6,ensure_ascii=False)+'];math12Key339ReviewExercise6.sourceAnswerReferences=[...(math12Key339ReviewExercise6.sourceAnswerReferences||[]),{page:339,jpg:"174_page_1.jpg"}];\n'
text+='const math12Key339Exercise71=MATH_12_DATA[6].exercises.find(e=>e.title==="Exercise 7.1");math12Key339Exercise71.sourceContextBlocks=[...(math12Key339Exercise71.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 339"},...'+json.dumps(ANSWER339_EX71,ensure_ascii=False)+'];math12Key339Exercise71.sourceAnswerReferences=[...(math12Key339Exercise71.sourceAnswerReferences||[]),{page:339,jpg:"174_page_1.jpg"}];\n'
text+='const math12Key339Exercise72=MATH_12_DATA[6].exercises.find(e=>e.title==="Exercise 7.2");math12Key339Exercise72.sourceContextBlocks=[...(math12Key339Exercise72.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 339"},...'+json.dumps(ANSWER339_EX72,ensure_ascii=False)+'];math12Key339Exercise72.sourceAnswerReferences=[...(math12Key339Exercise72.sourceAnswerReferences||[]),{page:339,jpg:"174_page_1.jpg"}];\n'
text+='const math12Key340Exercise72=MATH_12_DATA[6].exercises.find(e=>e.title==="Exercise 7.2");math12Key340Exercise72.sourceContextBlocks=[...(math12Key340Exercise72.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 340"},...'+json.dumps(ANSWER340_EX72,ensure_ascii=False)+'];math12Key340Exercise72.sourceAnswerReferences=[...(math12Key340Exercise72.sourceAnswerReferences||[]),{page:340,jpg:"174_page_2.jpg"}];\n'
text+='const math12Key340Exercise73=MATH_12_DATA[6].exercises.find(e=>e.title==="Exercise 7.3");math12Key340Exercise73.sourceContextBlocks=[...(math12Key340Exercise73.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 340"},...'+json.dumps(ANSWER340_EX73,ensure_ascii=False)+'];math12Key340Exercise73.sourceAnswerReferences=[...(math12Key340Exercise73.sourceAnswerReferences||[]),{page:340,jpg:"174_page_2.jpg"}];\n'
text+='const math12Key340Exercise74=MATH_12_DATA[6].exercises.find(e=>e.title==="Exercise 7.4");math12Key340Exercise74.sourceContextBlocks=[...(math12Key340Exercise74.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 340"},...'+json.dumps(ANSWER340_EX74,ensure_ascii=False)+'];math12Key340Exercise74.sourceAnswerReferences=[...(math12Key340Exercise74.sourceAnswerReferences||[]),{page:340,jpg:"174_page_2.jpg"}];\n'
text+='const math12Key340ReviewExercise7=MATH_12_DATA[6].exercises.find(e=>e.title==="Review Exercise 7");math12Key340ReviewExercise7.sourceContextBlocks=[...(math12Key340ReviewExercise7.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 340"},...'+json.dumps(ANSWER340_REVIEW7,ensure_ascii=False)+'];math12Key340ReviewExercise7.sourceAnswerReferences=[...(math12Key340ReviewExercise7.sourceAnswerReferences||[]),{page:340,jpg:"174_page_2.jpg"}];\n'
text+='const math12Key340Exercise81=MATH_12_DATA[7].exercises.find(e=>e.title==="Exercise 8.1");math12Key340Exercise81.sourceContextBlocks=[...(math12Key340Exercise81.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 340"},...'+json.dumps(ANSWER340_EX81,ensure_ascii=False)+'];math12Key340Exercise81.sourceAnswerReferences=[...(math12Key340Exercise81.sourceAnswerReferences||[]),{page:340,jpg:"174_page_2.jpg"}];\n'
text+='const math12Key341Exercise81=MATH_12_DATA[7].exercises.find(e=>e.title==="Exercise 8.1");math12Key341Exercise81.sourceContextBlocks=[...(math12Key341Exercise81.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 341"},...'+json.dumps(ANSWER341_EX81,ensure_ascii=False)+'];math12Key341Exercise81.sourceAnswerReferences=[...(math12Key341Exercise81.sourceAnswerReferences||[]),{page:341,jpg:"175_page_1.jpg"}];\n'
text+='const math12Key341Exercise82=MATH_12_DATA[7].exercises.find(e=>e.title==="Exercise 8.2");math12Key341Exercise82.sourceContextBlocks=[...(math12Key341Exercise82.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 341"},...'+json.dumps(ANSWER341_EX82,ensure_ascii=False)+'];math12Key341Exercise82.sourceAnswerReferences=[...(math12Key341Exercise82.sourceAnswerReferences||[]),{page:341,jpg:"175_page_1.jpg"}];\n'
text+='const math12Key341ReviewExercise8=MATH_12_DATA[7].exercises.find(e=>e.title==="Review Exercise 8");math12Key341ReviewExercise8.sourceContextBlocks=[...(math12Key341ReviewExercise8.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 341"},...'+json.dumps(ANSWER341_REVIEW8,ensure_ascii=False)+'];math12Key341ReviewExercise8.sourceAnswerReferences=[...(math12Key341ReviewExercise8.sourceAnswerReferences||[]),{page:341,jpg:"175_page_1.jpg"}];\n'
text+='const math12Key341Exercise91=MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.1");math12Key341Exercise91.sourceContextBlocks=[...(math12Key341Exercise91.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 341"},...'+json.dumps(ANSWER341_EX91,ensure_ascii=False)+'];math12Key341Exercise91.sourceAnswerReferences=[...(math12Key341Exercise91.sourceAnswerReferences||[]),{page:341,jpg:"175_page_1.jpg"}];\n'
text+='const math12Key342Exercise91=MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.1");math12Key342Exercise91.sourceContextBlocks=[...(math12Key342Exercise91.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 342"},...'+json.dumps(ANSWER342_EX91,ensure_ascii=False)+'];math12Key342Exercise91.sourceAnswerReferences=[...(math12Key342Exercise91.sourceAnswerReferences||[]),{page:342,jpg:"175_page_2.jpg"}];\n'
text+='const math12Key342Exercise92=MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.2");math12Key342Exercise92.sourceContextBlocks=[...(math12Key342Exercise92.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 342"},...'+json.dumps(ANSWER342_EX92,ensure_ascii=False)+'];math12Key342Exercise92.sourceAnswerReferences=[...(math12Key342Exercise92.sourceAnswerReferences||[]),{page:342,jpg:"175_page_2.jpg"}];\n'
text+='const math12Key343Exercise92=MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.2");math12Key343Exercise92.sourceContextBlocks=[...(math12Key343Exercise92.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 343"},...'+json.dumps(ANSWER343_EX92,ensure_ascii=False)+'];math12Key343Exercise92.sourceAnswerReferences=[...(math12Key343Exercise92.sourceAnswerReferences||[]),{page:343,jpg:"176_page_1.jpg"}];\n'
text+='const math12Key343Exercise93=MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.3");math12Key343Exercise93.sourceContextBlocks=[...(math12Key343Exercise93.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 343"},...'+json.dumps(ANSWER343_EX93,ensure_ascii=False)+'];math12Key343Exercise93.sourceAnswerReferences=[...(math12Key343Exercise93.sourceAnswerReferences||[]),{page:343,jpg:"176_page_1.jpg"}];\n'
text+='MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.3").sourceContextBlocks.push({type:"heading",text:"Printed answer key — page 344"},...'+json.dumps(ANSWER344_EX93,ensure_ascii=False)+');MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.3").sourceAnswerReferences.push({page:344,jpg:"176_page_2.jpg"});\n'
text+='const math12Key345Exercise94=MATH_12_DATA[8].exercises.find(e=>e.title==="Exercise 9.4");math12Key345Exercise94.sourceContextBlocks=[...(math12Key345Exercise94.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 345"},...'+json.dumps(ANSWER345_EX94,ensure_ascii=False)+'];math12Key345Exercise94.sourceAnswerReferences=[...(math12Key345Exercise94.sourceAnswerReferences||[]),{page:345,jpg:"177_page_1.jpg"}];\n'
text+='const math12Key345Exercise101=MATH_12_DATA[9].exercises.find(e=>e.title==="Exercise 10.1");math12Key345Exercise101.sourceContextBlocks=[...(math12Key345Exercise101.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 345"},...'+json.dumps(ANSWER345_EX101,ensure_ascii=False)+'];math12Key345Exercise101.sourceAnswerReferences=[...(math12Key345Exercise101.sourceAnswerReferences||[]),{page:345,jpg:"177_page_1.jpg"}];\n'
text+='const math12Key345Exercise102=MATH_12_DATA[9].exercises.find(e=>e.title==="Exercise 10.2");math12Key345Exercise102.sourceContextBlocks=[...(math12Key345Exercise102.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 345"},...'+json.dumps(ANSWER345_EX102,ensure_ascii=False)+'];math12Key345Exercise102.sourceAnswerReferences=[...(math12Key345Exercise102.sourceAnswerReferences||[]),{page:345,jpg:"177_page_1.jpg"}];\n'
text+='const math12Key346Exercise102=MATH_12_DATA[9].exercises.find(e=>e.title==="Exercise 10.2");math12Key346Exercise102.sourceContextBlocks=[...(math12Key346Exercise102.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 346"},...'+json.dumps(ANSWER346_EX102,ensure_ascii=False)+'];math12Key346Exercise102.sourceAnswerReferences=[...(math12Key346Exercise102.sourceAnswerReferences||[]),{page:346,jpg:"177_page_2.jpg"}];\n'
text+='const math12Key346ReviewExercise10=MATH_12_DATA[9].exercises.find(e=>e.title==="Review Exercise 10");math12Key346ReviewExercise10.sourceContextBlocks=[...(math12Key346ReviewExercise10.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 346"},...'+json.dumps(ANSWER346_REVIEW10,ensure_ascii=False)+'];math12Key346ReviewExercise10.sourceAnswerReferences=[...(math12Key346ReviewExercise10.sourceAnswerReferences||[]),{page:346,jpg:"177_page_2.jpg"}];\n'
text+='const math12Key346Exercise111=MATH_12_DATA[10].exercises.find(e=>e.title==="Exercise 11.1");math12Key346Exercise111.sourceContextBlocks=[...(math12Key346Exercise111.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 346"},...'+json.dumps(ANSWER346_EX111,ensure_ascii=False)+'];math12Key346Exercise111.sourceAnswerReferences=[...(math12Key346Exercise111.sourceAnswerReferences||[]),{page:346,jpg:"177_page_2.jpg"}];\n'
text+='const math12Key346Exercise112=MATH_12_DATA[10].exercises.find(e=>e.title==="Exercise 11.2");math12Key346Exercise112.sourceContextBlocks=[...(math12Key346Exercise112.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 346"},...'+json.dumps(ANSWER346_EX112,ensure_ascii=False)+'];math12Key346Exercise112.sourceAnswerReferences=[...(math12Key346Exercise112.sourceAnswerReferences||[]),{page:346,jpg:"177_page_2.jpg"}];\n'
text+='const math12Key346ReviewExercise11=MATH_12_DATA[10].exercises.find(e=>e.title==="Review Exercise 11");math12Key346ReviewExercise11.sourceContextBlocks=[...(math12Key346ReviewExercise11.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 346"},...'+json.dumps(ANSWER346_REVIEW11,ensure_ascii=False)+'];math12Key346ReviewExercise11.sourceAnswerReferences=[...(math12Key346ReviewExercise11.sourceAnswerReferences||[]),{page:346,jpg:"177_page_2.jpg"}];\n'
text+='const math12Key347Exercise121=MATH_12_DATA[11].exercises.find(e=>e.title==="Exercise 12.1");math12Key347Exercise121.sourceContextBlocks=[...(math12Key347Exercise121.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 347"},...'+json.dumps(ANSWER347_EX121,ensure_ascii=False)+'];math12Key347Exercise121.sourceAnswerReferences=[...(math12Key347Exercise121.sourceAnswerReferences||[]),{page:347,jpg:"178_page_1.jpg"}];\n'
text+='const math12Key347Exercise122=MATH_12_DATA[11].exercises.find(e=>e.title==="Exercise 12.2");math12Key347Exercise122.sourceContextBlocks=[...(math12Key347Exercise122.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 347"},...'+json.dumps(ANSWER347_EX122,ensure_ascii=False)+'];math12Key347Exercise122.sourceAnswerReferences=[...(math12Key347Exercise122.sourceAnswerReferences||[]),{page:347,jpg:"178_page_1.jpg"}];\n'
text+='const math12Key347ReviewExercise12=MATH_12_DATA[11].exercises.find(e=>e.title==="Review Exercise 12");math12Key347ReviewExercise12.sourceContextBlocks=[...(math12Key347ReviewExercise12.sourceContextBlocks||[]),{type:"heading",text:"Printed answer key — page 347"},...'+json.dumps(ANSWER347_REVIEW12,ensure_ascii=False)+'];math12Key347ReviewExercise12.sourceAnswerReferences=[...(math12Key347ReviewExercise12.sourceAnswerReferences||[]),{page:347,jpg:"178_page_1.jpg"}];\n'
text+='MATH_12_DATA[11].sourceBackMatterPages='+json.dumps(BACKMATTER_PAGES,ensure_ascii=False)+';\n'
book_blocks=BOOK_AUTHORS+BOOK_FEEDBACK+BOOK_QUOTES+BOOK_BACK_COVER
text+='MATH_12_DATA[11].sections.push({id:"sec-12-book-matter",num:"Book",title:"About the book and final pages",sourceBlocks:'+json.dumps(book_blocks,ensure_ascii=False)+',sourceReferences:'+json.dumps([{'page':p['page'],'jpg':p['file']} for p in BACKMATTER_PAGES],ensure_ascii=False)+',theory:'+json.dumps('\n\n'.join(' '.join(str(b.get(k,'')) for k in ['text','caption']) for b in book_blocks),ensure_ascii=False)+',unreviewedTheory:""});\n'
text+='const MATH12_SENTENCE_TRANSLATIONS='+json.dumps(MATH12_TRANSLATIONS,ensure_ascii=False)+';\nconst MATH12_WORD_MEANINGS='+json.dumps(MATH12_WORDS,ensure_ascii=False)+';\n'
text+='function attachMath12Translations(value){if(!value||typeof value!=="object")return;if(value.text&&MATH12_SENTENCE_TRANSLATIONS[value.text])value.sentenceTranslations=MATH12_SENTENCE_TRANSLATIONS[value.text];for(const [key,child] of Object.entries(value)){if(key!=="sentenceTranslations"&&typeof child==="object")attachMath12Translations(child);}}attachMath12Translations(MATH_12_DATA);\n'
target.write_text(text, encoding="utf-8", newline="\n")
progress_dir = ROOT / "docs/source-verification"
progress_dir.mkdir(parents=True, exist_ok=True)
source = ROOT.parent / "Books/12th/12th Maths/JPG"
entries = []
for index, file in enumerate(sorted(source.glob('*.jpg')), 1):
    page = next((p for p in pages + FUNCTION_PAGES + DIFFERENTIATION_PAGES + HIGHER_PAGES + VECTOR_PAGES + INTEGRATION_PAGES + STRAIGHT_PAGES + CONIC_PAGES + CONICS2_PAGES + ODE_PAGES + PARTIAL_PAGES + NUMERICAL_PAGES + ANSWER_PAGES + BACKMATTER_PAGES if p['file'] == file.name), None)
    entries.append({"sequence": index, "jpg": file.name, "textStatus": ("partial_source_clipping" if page.get('sourceDefects') else "visually_verified") if page else "pending", "visualStatus": page['visualStatus'] if page else "pending", "translationStatus": "pending", "pageComplete": False, **({"alternateVerification":page['alternateVerification']} if page and page.get('alternateVerification') else {})})
state = {"classOrder": list(range(12, 0, -1)), "ownership": {"status": "IN_PROGRESS", "direction": "12 to 1", "agent": "current Codex chat", "book": "Class 12 Mathematics", "nextPrintedPage": None, "currentStage": "translations_and_source_repairs"}, "currentClass": 12, "currentSubject": "Mathematics", "bookStatus": "in_revision", "nextSource": "translation: Class 12 Mathematics — Unit 1", "pendingWork": "Urdu/Pashto sentence and word translations, speech checks, and unresolved source defects are pending", "sourceCount": len(entries), "pages": entries, "fullPdf": {"file": "Math Book for 12 class KPTBB.pdf", "physicalPages": len(full_pdf.pages), "layout": "Cover followed by a third-party advertisement and two-page textbook spreads", "supplements": [{"physicalPage": 2, "classification": "third-party source-copy advertisement", "verification": "Rendered with Poppler and inspected visually; native PDF text also extracted", "instructionalContent": False, "disposition": "Accounted for; excluded from textbook lessons because it is an inserted advertisement rather than KPTBB curriculum content"}]}, "resolvedIssues": ["Printed page 3 JPG clipping resolved visually against full PDF page 6, left side.", "Figures 1.1–1.10 restored as cropped original software illustrations with digital commands and results.", "Full PDF physical page 2 is an inserted advertisement, accounting for its absence from the JPG textbook sequence.", "Printed page 17 JPG clipping resolved against full PDF page 13, left side.", "Plotting options through page 18 restored without silently correcting printed syntax or spelling."], "issues": ["Title-page diagrams and translations still pending.", "Example 5 repeats x for the second coordinate; original wording retained and SpaceBook clarification added.", "Figure 1.16 partial arcs retained from the scan pending exact digital reconstruction; endpoints are not defined by the printed command.", "Printed pages 142–157 are absent from the supplied JPG sequence, matching split PDF parts and full PDF: physical 75 pairs 141 with 174; physical 83 pairs 189 with 158. Word parts contain the same continuation and no Unit 6 opening. Unit 6 source beginning and Examples 1–8 opening remain unavailable; do not mark them complete."]}
for entry in entries:
    reviewed_page = next((page for page in pages + FUNCTION_PAGES + DIFFERENTIATION_PAGES + HIGHER_PAGES + VECTOR_PAGES + INTEGRATION_PAGES + STRAIGHT_PAGES + CONIC_PAGES + CONICS2_PAGES + ODE_PAGES + PARTIAL_PAGES + NUMERICAL_PAGES + ANSWER_PAGES + BACKMATTER_PAGES if page['file']==entry['jpg']), None)
    if reviewed_page:
        if reviewed_page.get('textStatus'): entry['textStatus']=reviewed_page['textStatus']
        elif reviewed_page['page']==33: entry['textStatus']='partial_source_legibility'
        for field in ['sourceNotes','sourceDefects']:
            if reviewed_page.get(field): entry[field] = reviewed_page[field]
    if entry['jpg']=='026_page_2.jpg':
        entry['exerciseSolutionStatus']='Questions 1–8 worked and checked; 29 digital learning graphs; answer-key mismatches separately clarified'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPages':[168,169],'printedPages':[327,328,329,330],'scope':'Exercise 2.2 Questions 1–7; answer pages are not transcribed or complete'}
    if entry['jpg']=='020_page_1.jpg':
        entry['exerciseSolutionStatus'] = 'Four numbered questions worked and checked; photographic project partial because exact horizontal endpoints are unverified'
        entry['answerKeyVerification'] = {'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':167,'printedPage':326,'scope':'Question 1 intervals only; this does not mark answer page 326 transcribed or complete'}
state['issues'].append('Exercise 2.1 photographic project horizontal endpoints remain unverified; its UI and progress record show a partial solution.')
for entry in entries:
    if entry['jpg']=='032_page_2.jpg':
        entry['exerciseStatus']='All six numbered Exercise 2.3 questions have complete learning solutions; Project (i) exact formula remains partially legible and explicitly marked partial'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':331,'scope':'Exercise 2.3 Questions 1–4 and 6 only; answer page not transcribed or marked complete'}
state['issues'].append('Exercise 2.3 Project (i) coefficients remain unclear in both source copies; source crop and partial learning classification retained.')
for entry in entries:
    if entry['jpg']=='034_page_2.jpg':
        entry['exerciseStatus']='Seven Exercise 2.4 questions have full progressive learning solutions and five native graphs; page 59 Project has a worked sample selection with expected Maple outputs, not executed outputs'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':331,'scope':'Exercise 2.4 Questions 1–7 only; answer page not transcribed or marked complete'}
state['issues'].append('Exercise 2.4 Question 7 answer key true contradicts the printed denominator x³ + 2.7; expected false and interior pole explained separately.')
for entry in entries:
    if entry['jpg']=='035_page_1.jpg':
        entry['exerciseStatus']='All fifteen review questions and sixty printed choices transcribed; full progressive explanations include source ambiguities'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':331,'scope':'Review Exercise 2, Question 1 (i)–(xv); key checked visually, answer page not transcribed or marked complete'}
for entry in entries:
    if entry['jpg']=='042_page_2.jpg':
        entry['exerciseStatus']='All five Exercise 3.2 questions and measured-length ladder project have progressive worked learning solutions; source ladder illustration reconstructed as native SVG'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':170,'printedPage':332,'scope':'Exercise 3.2 Questions 1–5 only; answer page not transcribed or marked complete'}
state['issues'].append('Exercise 3.2 Question 2(a) answer key includes an unrelated extra equality; correct first result retained in learning solution.')
for entry in entries:
    if entry['jpg'] in ['045_page_1.jpg', '045_page_2.jpg']:
        entry['exerciseStatus']='All nine Exercise 3.3 questions have progressive worked learning solutions; source boat diagram reconstructed as native SVG'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPage':333,'scope':'Exercise 3.3 Questions 1–9 only; answer page not transcribed or marked complete'}
state['issues'].append('Exercise 3.3 Question 3(b) answer key gives 12t²/a; the printed parametric equations give 4t²/a, explained separately.')
for entry in entries:
    if entry['jpg']=='049_page_2.jpg':
        entry['exerciseStatus']='All five Exercise 3.4 questions and eighteen subparts have checked progressive solutions, with original-domain and principal-branch restrictions'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPages':[333,334],'scope':'Exercise 3.4 Questions 1–5 only; key checked visually, answer pages not transcribed or marked complete'}
state['issues'].extend(['Example 18(b) replaces √(4x²) with 2x; the negative-x branch is corrected separately.', 'Printed inverse secant/cosecant rules omit absolute values required on the standard negative principal branches; corrections remain separate from the source formulas.', 'Exercise 3.4 Question 3(f) key has a plus sign where differentiation of 1/x requires a minus; Question 5 key repeats t = 3 labels for t = 4 and 5.'])
for entry in entries:
    if entry['jpg'] in ['053_page_2.jpg','054_page_1.jpg']:
        entry['exerciseStatus']='All seven Exercise 3.5 questions have progressive solutions; page 99 also has all ten Review Exercise 3 items and all forty choices, with duplicate correct options explained'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'printedPage':334,'scope':'Exercise 3.5 Questions 1–6 and Review Exercise 3 only; key visually checked, page not transcribed or marked complete'}
    if entry['jpg']=='054_page_2.jpg':entry['exerciseStatus']='Spherical-balloon project has a complete progressive solution and its exact dedicated source artwork; full printed summary and separate corrections included'
state['issues'].extend(['Example 19(c) differentiates ln u as 1/ln u; the correct 1/u solution is separated from the source.', 'The printed inverse-coth proof loses a minus sign; the following formula box gives the correct negative derivative.', 'Exercise 3.5 Question 1(c) key moves +1 into the exponent; Question 2(a) key replaces source x³ with x⁵; entries 1(h) and 4(a) are exchanged.', 'Exercise 3.5 Question 3(d) has no real logarithm domain; the key solves the separately explained logarithm-of-absolute-value alternative.', 'Exercise 3.5 unbased log notation and Question 4(a) cube placement remain ambiguous; branch/base interpretations are stated explicitly.', 'Review Exercise 3 items (vi) and (vii) each contain two equivalent correct options; both are explained alongside the key-selected answer.'])
for entry in entries:
    if entry['jpg']=='059_page_1.jpg':
        entry['exerciseStatus']='All six Exercise 4.1 groups and both project expressions have progressive solutions; domains, derivative orders and key discrepancies checked'
        entry['answerKeyVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPages':[171,172],'printedPages':[334,335],'scope':'Exercise 4.1 Questions 1–6 only; answer pages not transcribed or marked complete'}
    if entry['jpg']=='063_page_2.jpg':entry['exerciseStatus']='All eight Exercise 4.2 groups worked, including singular intersection branch angles and full coordinates; exact history portrait retained'
    if entry['jpg'] in ['067_page_2.jpg','068_page_1.jpg']:entry['exerciseStatus']='All ten Exercise 4.3 groups worked, with two dedicated Question 4 graphs; source/key cube-root discrepancy, units and domain pole explained'
    if entry['jpg']=='068_page_2.jpg':entry['exerciseStatus']='All ten Review 4 items and forty options transcribed; complete progressive explanations, Taylor typo and duplicate normal equations separately identified'
    if entry['jpg']=='069_page_1.jpg':entry['summaryStatus']='Complete native summary and exact source history portrait; offset/finite-series/domain qualifications separate from source'
state['issues'].extend(['Unit 4 Example 5 Remember box reverses first derivative; its second-derivative proof loses a chain factor. Correct source and learning results kept separate.', 'Unit 4 Example 7 prints a first-derivative command beside a second-derivative output; nested correction is provided with expected, not executed, results.', 'Exercise 4.1 key loses polynomial derivative powers, gives a third derivative for a fourth-order request, and changes +7 to +2 in Question 6(a).', 'Taylor/Maclaurin finite expressions and offset labels need convergence/approximation qualifications; the source is preserved and limitations explained.', 'Figures 4.1 and 4.6 contain inconsistent source annotations retained in their native reconstructions with explicit clarification.', 'Unit 4 Example 29 asks for maximum cost after finding the minimum; the stated model has no finite maximum on x > 0.', 'Exercise 4.3 Question 3(a) extra = 0 contradicts its prescribed values; Question 3(d) key solves a different cube-root radicand containing an extra x.', 'Review 4 (vi) has no fully correct option as written due to a Taylor coefficient typo; (viii) has two equivalent correct normal equations.'])
state['sourceGaps']=[{'printedPageStart':142,'printedPageEnd':157,'status':'unavailable_in_supplied_formats','verification':'JPG 075_page_2.jpg is printed 174; JPG 083_page_2.jpg is printed 158. Full PDF physical 75 and 83 inspected. Split PDF source mapping agrees. Word parts 2/3 checked for Unit 6 opening; only continuation exists.','impact':'Unit 6 objectives, introduction, rules, initial substitution material and early exercise/source example content cannot be transcribed as source-complete.'}]
for entry in entries:
 if entry['jpg']=='074_page_2.jpg':entry['exerciseStatus']='All ten review items and forty options transcribed with progressive explanations; invalid limit argument, duplicate choices, acceleration sign and continuity assumptions clarified.'
 if entry['jpg']=='075_page_1.jpg':entry['summaryStatus']='Complete native summary, history portrait and project photograph; separate seven-step checked sample project.'
 if entry['jpg']=='073_page_1.jpg':entry['visualStatus']='All six Example 8 determinant layouts restored as native accessible tables beside full source calculations.'
state['issues'].extend(['Unit 5 Example 12 uses degree cosine after a radian derivative; consistent radian speed and alternate degree model explained separately.','Unit 5 Example 13 final direction approximation omits normalization; correct unit direction supplied separately.','Review 5 (v) printed constant argument has no correct option; intended variable argument matches identical (a)/(d). Review 5 (ix) has no correct acceleration option.'])
state['duplicateSources']=[{'printedPage':174,'canonicalJpg':'075_page_2.jpg','duplicateJpg':'091_page_2.jpg','fullPdfPhysicalPages':[75,91],'verification':'Both full PDF spreads and canonical JPG visually inspected; same complete Example 20/21 page appears twice.'}]
for entry in entries:
 if entry['jpg']=='091_page_2.jpg':entry.update({'textStatus':'visually_verified_duplicate','visualStatus':'Same printed page 174 as canonical 075_page_2.jpg; native content and source figures represented once','duplicateOf':'075_page_2.jpg','printedPage':174,'pageComplete':False,'translationStatus':'pending'})
state['duplicateSources'].append({'printedPage':175,'canonicalJpg':'076_page_1.jpg','duplicateJpg':'092_page_1.jpg','fullPdfPhysicalPages':[76,92],'verification':'Canonical full PDF page and duplicate JPG visually inspected; all history, exercise expressions and four shaded figures match.'})
for entry in entries:
 if entry['jpg']=='092_page_1.jpg':entry.update({'textStatus':'visually_verified_duplicate','visualStatus':'Duplicate of reviewed printed 175 with complete native source exercises and dedicated illustrations','duplicateOf':'076_page_1.jpg','printedPage':175,'pageComplete':False,'translationStatus':'pending'})
 if entry['jpg']=='076_page_1.jpg':entry['exerciseStatus']='All six groups, eight first-group integrals, two rational integrals, four curve areas, four shaded setups, oil-leak day amounts and two Maple expected outputs worked; exact x^(-2) source exponent retained.'
for number,canonical,duplicate in [(176,'076_page_2.jpg','092_page_2.jpg'),(177,'077_page_1.jpg','093_page_1.jpg'),(178,'077_page_2.jpg','093_page_2.jpg'),(179,'078_page_1.jpg','094_page_1.jpg'),(180,'078_page_2.jpg','094_page_2.jpg'),(181,'079_page_1.jpg','095_page_1.jpg'),(182,'079_page_2.jpg','095_page_2.jpg'),(183,'080_page_1.jpg','096_page_1.jpg'),(184,'080_page_2.jpg','096_page_2.jpg'),(185,'081_page_1.jpg','097_page_1.jpg'),(186,'081_page_2.jpg','097_page_2.jpg'),(187,'082_page_1.jpg','098_page_1.jpg'),(188,'082_page_2.jpg','098_page_2.jpg'),(189,'083_page_1.jpg','099_page_1.jpg')]:
 state['duplicateSources'].append({'printedPage':number,'canonicalJpg':canonical,'duplicateJpg':duplicate,'verification':'Canonical full PDF source and duplicate JPG both visually inspected; complete native text and dedicated figures match.'})
 for entry in entries:
  if entry['jpg']==duplicate:entry.update({'textStatus':'visually_verified_duplicate','visualStatus':'Duplicate of reviewed printed '+str(number),'duplicateOf':canonical,'printedPage':number,'pageComplete':False,'translationStatus':'pending'})
state['issues'].extend(['Unit 7 source calls the incenter a centroid, mixes signed and unsigned external ratios, and supplies a non-collinear dividing point in Exercise 7.1 Q4(b); originals retained with separate checked clarification.','Unit 7 vertical-line source uses ordinate b and x = −b at distance a; correct abscissa x and x = −a explained separately.','Unit 6 source opening 142–157 is unavailable across supplied formats; sections 6.1/6.2 and Exercise 6.1 cannot be source-complete. Source substitution continuation belongs in 6.3, with original unreviewed text preserved separately.','Source definite-area formula mixes signed −A+B with unsigned A+B; original lines preserved and corrected separately.','Review 6 (iv) uses integrand parameter t with dx and has no correct square-root option; (viii) has equivalent correct options (a) and (c).'])
state['issues'].extend(['Printed 207 definition (i) remains partially legible across JPG/PDF/Word; exact crop retained, conventional formula labelled as inference only.','Unit 7 Exercise 7.4 Q2(c) is not concurrent and Review 7 (ix) has no correct area option.','Unit 8 Example 2 swaps x/y coefficients; Example 6 final center sign, Example 12 off-circle contact and Example 19 tangent constant are corrected separately from the source.','Unit 8 Exercise 8.2 Q2(a), Exercise 8.3 Q2 and Q6(b) contain off-circle points. Review 8 (ii)/(iii) have no generally correct center/radius option.','Unit 8 source tangent and angle derivations omit vertical cases or angle branches; original formulas and division-free learning checks retained.'])
state['issues'].extend(['Printed 265–266 hyperbola opening is motion-blurred across supplied JPG/PDF and garbled in Word; unresolved source fragments retained with a separately labelled learning derivation.','Exercise 9.1 Q2 has conflicting directrix/coordinate labels; Q4 is a perpendicular-bisector locus and Q5 has two unspecified opening directions.','Exercise 9.2 Q2(b) left endpoint y sign is wrong; all three Q6 contact points are off their ellipses.','Printed 263 ellipse summary mixes a<b denominator notation with semimajor-a element formulas; source entries retained with separate consistent corrections.'])
state['issues'].extend(['Unit 9 hyperbola intersection expansions use a wrong constant sign; Remember box repeats ellipse plus-b² while the correct tangent uses minus-b² and excludes asymptote slopes.','Unit 9 Examples 26–27 and Exercise 9.3 Q9(b) use off-curve contacts; no at-point tangent/normal is defined.','Exercise 9.3 Q2(d) has conflicting focus/vertex labels; Q3(c) specifies a family rather than a unique hyperbola.','Example 28 repeats Y² and reverses translation signs; Example 29 inverse Y sign and Example 30 squared-bracket coefficients are wrong.','Unit 9 summaries contain an incorrect vertical hyperbola slope and mixed eccentricity/axis statements; originals retained with separate corrected conditions.','Unit 9 has four source exercises; unsupported baseline extra exercise preserved in unreviewedExercises and excluded from source exercise list.'])
reviewed_answer_numbers={page['page'] for page in ANSWER_PAGES}
for entry in entries:
 key=entry.get('answerKeyVerification')
 if key:
  key_numbers=key.get('printedPages',[key.get('printedPage')])
  if all(number in reviewed_answer_numbers for number in key_numbers):
   key['answerPageTranscription']='Separately transcribed natively and displayed beside the matching exercises; translations remain pending.'
   key['scope']=key['scope'].split(';')[0]+'; corresponding printed key pages are now separately transcribed, without changing the checked learning solutions'
state['issues'].extend(['Exercise 10.1 Q2(c) has an uncertified smudged exponent; exact source crop retained and conditional verification separated. Exercise 10.1 Q2(d) does not satisfy its printed equation.', 'Exercise 10.2 Q4(b) gives initial y=0 where the equation requires a nonzero finite y derivative; no classical differentiable solution meets the condition.', 'Unit 11 source homogeneity examples use commas in place of sums; history series has a wrong constant. Original formulas and separate qualifications retained.', 'Unit 12 source false-position calculations leave the bracket and contain wrong residuals. Newton Example 3 prints a wrong derivative sign, and Maple examples mix functions or interval counts.', 'Exercise 12.1 includes invalid brackets and a function with no real root; Exercise 12.2 Q5 omits its integrand and remains partial with an explicitly chosen sample.', 'Printed answer-key omissions, incorrect signs, derivative orders, graph labels and units are preserved alongside separate checked learning explanations. Source translations and TTS remain pending.'])
def translated_source_texts(value):
 if isinstance(value,str):return {value} if value in MATH12_TRANSLATIONS else set()
 if isinstance(value,list):return set().union(*(translated_source_texts(item) for item in value)) if value else set()
 if isinstance(value,dict):return set().union(*(translated_source_texts(item) for item in value.values())) if value else set()
 return set()
for source_page in pages:
 translated_texts=translated_source_texts(source_page)
 if translated_texts:
  entry=next(item for item in entries if item['jpg']==source_page['file'])
  entry.update(translationStatus='partially_translated',translatedPassages=len(translated_texts),translatedSentences=sum(len(MATH12_TRANSLATIONS[value]) for value in translated_texts),translationScope='Exact aligned Urdu/Pashto source passages; untranslated headings, captions, frontmatter and other content remain pending',ttsStatus='Device voice controls implemented; unavailable language voices reported explicitly, no recorded audio verification claimed')
state['translationCoverage']={'passages':len(MATH12_TRANSLATIONS),'sentences':sum(len(pairs) for pairs in MATH12_TRANSLATIONS.values()),'wordMeanings':len(MATH12_WORDS),'status':'partial','scope':'Unit 1 introduction, environment and basic commands; remaining source and learning content pending','speech':'Language-specific device voice selection with visible unavailable-voice feedback; recorded audio not generated'}
(progress_dir / "math12.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(f"Applied {len(pages + FUNCTION_PAGES + DIFFERENTIATION_PAGES + HIGHER_PAGES + VECTOR_PAGES + INTEGRATION_PAGES + STRAIGHT_PAGES + CONIC_PAGES + CONICS2_PAGES + ODE_PAGES + PARTIAL_PAGES + NUMERICAL_PAGES + ANSWER_PAGES + BACKMATTER_PAGES)} reviewed transcriptions; {len(entries)} source pages tracked; book remains incomplete.")
