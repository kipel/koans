#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
	if (a <= 0) or (b <= 0) or (c <= 0):
		raise TriangleError

	s = len({a, b, c})
	if s == 1:
		return 'equilateral'
	elif s == 2:
		if a == b:
			side, base = a, c
		elif a == c:
			side, base = a, b
		else:
			side, base = b, a

		h = side**2 - base**2 / 4
		if h <= 0:
			raise TriangleError
		return 'isosceles'
	else:
		return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
