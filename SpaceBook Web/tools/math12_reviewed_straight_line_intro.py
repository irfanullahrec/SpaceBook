"""Printed page 178, compared with full PDF 77 and duplicate JPG 93."""
from math12_reviewed_unit1 import heading,paragraph,page,figure
OBJECTIVES=[
('7.1 Division of a line segment',[
'Recall distance formula to calculate distance between two points given in Cartesian plane.',
'Find coordinates of a point that divides the line segment in given ratio (internally and externally).',
'Show that the medians and angle bisectors of a triangle are concurrent.']),
('7.2 Slope of a straight line',[
'Define the slope of a line.',
'Derive formula to find the slope of a line passing through two points.',
'Find the condition that two straight lines with given slopes may be parallel to each other, or perpendicular to each other.']),
('7.3 Equation of a straight line parallel to Co-ordinate axes',[
'Find the equation of a straight line parallel to y-axis and at a distance a from it, or x-axis and at a distance b from it.']),
('7.4 Standard form of equation of a straight line',[
'Define intercepts of a straight line. Derive equation of a straight line in slope-intercept form, point-slope form, two-point form, intercepts form, symmetric form, normal form.',
'Show that a linear equation in two variables represents a straight line.',
'Reduce the general form of the equation of a straight line to the other standard forms.']),
('7.5 Distance of a point from a line',[
'Recognize a point with respect to position of a line.',
'Find the perpendicular distance from a point to the given straight lines.']),
('7.6 Angle between lines',[
'Find the angle between two coplanar intersecting straight lines.',
'Find the equation of family of lines passing through the point of intersection of two given lines.',
'Calculate angles of the triangle when the slopes of the sides are given.']),
('7.7 Concurrency of straight lines',[
'Find the condition of concurrency of three straight lines.',
'Find the equation of median, altitude and right bisector of a triangle.',
'Show that three right bisectors, three medians, or three altitudes, of a triangle are concurrent.']),
('7.8 Area of a triangular region',[
'Find area of a triangular region whose vertices are given.']),
('7.9 Homogenous equation',[
'Recognize homogeneous linear and quadratic equations in two variables.',
'Investigate that the 2nd degree homogeneous equation in two variables x and y represents a pair of straight lines through the origin and find acute angle between them.'])]
INTRO=[heading('Introduction'),paragraph('We are familiar about Cartesian coordinate system, we have learnt about it in our previous classes. This Cartesian coordinate system may be helpful to know the slope formula, Pythagoras theorem and distance formula. In this lesson we will learn in details and write the equations involving arbitrary points. Most of the geometric ideas can be expressed using algebraic equations. Analytic geometry is defined as:'),paragraph('“The study of relationship between geometry and algebra is called analytic geometry”.'),figure('figure-7-1','Figure 7.1','Source illustration of a cyclist ascending a sloping line beside a shaded right triangle')]
PAGES=[page('077_page_2.jpg',178,[heading('Unit 7 — PLANE ANALYTIC GEOMETRY STRAIGHT LINE'),heading('By the end of this unit, the students will be able to:')]+[b for title,items in OBJECTIVES for b in [heading(title)]+[paragraph(t) for t in items]]+INTRO)]
PAGES[0]['objectives']=OBJECTIVES
PAGES[0].update(title='PLANE ANALYTIC GEOMETRY STRAIGHT LINE',visualStatus='All nine objective groups and introduction transcribed; dedicated original cyclist illustration retained',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':77,'side':'right','reason':'Full spread and duplicate 093_page_2.jpg both inspected visually'})
FIGURE_PDF_CROPS=[(77,'figure-7-1',(1350,838,1501,978))]
