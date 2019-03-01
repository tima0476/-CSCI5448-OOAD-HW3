#!/usr/bin/env python3
#
# Hardware Store Simulation in Python 3
# a solution for Homework 3 of CSCI 5448, Object Oriented Analysis and Design
# University of Colorado, Boulder
#
# written by Timothy Mason (solo project)
#
# file: tool.py
# description: Implements the Tool class.
#
# Tool: Each instance of Tool represents a single tool.  A Tool is a simple data holder responsible for knowing its' 
# name, category, and rental price per day.  These attributes are passed into the constructor.
# 
class Tool:
	def __init__(self, name, category, price):
		self.name = name
		self.category = category
		self.price = price

	def __repr__(self):
		return "{} (${:0.2f}/day)".format(self.name, self.price)

if __name__ == "__main__":
	# Test code - only run if executed at the top level
	print("Testing Tool.py")
