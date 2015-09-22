#!/usr/bin/env python

class Triangle:
	"""Represents a triangle"""
	def __init__(self, x1,y1, x2,y2, x3,y3):
		"""The three verticies of the triangle"""
		self.v1 = Point(x1,y1)


class Point:
	""" A class to represent a point in 2d space """
	def __init__(self,x,y):
		""" Initialize a point with the specified position """
		self.x = x
		self.y = y
	def move(self, delta_x, delta_y):
		""" Modifies the point by translating it by delta_x in the 
			x-direction and delta_y in the y-direction """
		self.x = self.x + delta_x
		self.y = self.y + delta_y
	def scale(self, scale_factor):
		""" Scales the point by the specified scale_factor"""
		self.x = self.x*scale_factor
		self.y = self.y*scale_factor
p = Point(2.0,1.0)
print p.x
print p.y
p.move(3.0,-1.0)
print p.x
print p.y
p.scale(2)
print p.x
print p.y
