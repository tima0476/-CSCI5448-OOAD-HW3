#!/usr/bin/env python3
#
# Hardware Store Simulation in Python 3
# a solution for Homework 3 of CSCI 5448, Object Oriented Analysis and Design
# University of Colorado, Boulder
#
# written by Timothy Mason (solo project)
#
# file: rental.py
# description:  Implementation of the Rental class.  This class is responsible for tracking the details of tool rentals; one
# class instance per rental record.
#
import tool
import customer

class Rental:
	def __init__(self, toolsRented, customer, startDay, rentalPeriod, total):
		# toolsRented = list of Tool objects
		# customer = Customer object
		# startDay = integer number of starting day
		# rentalPeriod = integer number of days for the rental
		self.toolsRented = toolsRented
		self.customer = customer
		self.startDay = startDay
		self.rentalPeriod = rentalPeriod
		self.total = total

	def expired(self, currentDay):
		return (self.startDay + self.rentalPeriod)<=currentDay

	def toolCount(self):
		return len(self.toolsRented)

	def __repr__(self):
		# which tools were rented by which customer for how many days along with the total amount of that rental
		if self.rentalPeriod==1:
			dayWord = "day"
		else:
			dayWord = "days"
		count = len(self.toolsRented)
		return "{} rented {} tool{} {} for {} {} on day {}.  Total = ${:0.2f}".format(self.customer, count, ["","s","s"][count-1], 
			self.toolsRented, self.rentalPeriod, dayWord, self.startDay, self.total)


if __name__ == "__main__":		
	# Test code - only run if executed at the top level
	print("Top level Rental.py")
