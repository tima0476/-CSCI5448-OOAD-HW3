#!/usr/bin/env python3
#
# Hardware Store Simulation in Python 3
# a solution for Homework 3 of CSCI 5448, Object Oriented Analysis and Design
# University of Colorado, Boulder
#
# written by Timothy Mason (solo project)
#
# file: customer.py
# description:  Defines and implements the Customer class plus the CasualCustomer,
# RegularCustomer, and BusinessCustomer subclasses.  The Customer class is an abstract
# base class responsible for name, plus minimum and maximum tool rental quantities and durations. 
# The class is also responsible for providing information about desired tool rentals.
#
# The subclasses are concrete classes which specialize Customer according to specific rental
# quantity and duration requirements of the various customer types.
#
# This family of classes is intended to be used as part of the "Strategy Pattern"
#
import names
import rental
import random

class Customer:
	def __init__(self):
		self.name = names.GenerateName()	# each customer chooses their own randomly generated name.
		self.minLen = 0
		self.maxLen = 0
		self.minQty = 0
		self.maxQty = 0
		self.activeRentalCount = 0
		self.typeName = "Generic customer"

	def __repr__(self):
		return self.typeName + " " + self.name

	def qtyWantToRent(self):
		# Report how many tools this customer wants to rent today, within the allowed bounds
		if (self.activeRentalCount >= 3) or random.getrandbits(1):  # 50% chance customer will want to come in, but 0% if already renting 3 tools
			return 0

		# Customer has decided they want to come in.  Decide how many tools are wanted.
		desired = random.randrange(self.minQty, self.maxQty+1)

		# check that the desired number is in bounds
		if (desired+self.activeRentalCount > 3):
			# if desired takes us over the max allowed, then scale back the desire to meet the max
			desired = 3 - self.activeRentalCount
		
		if (desired < self.minQty):
			# if we're not allowed to rent enough tools to meet our minimum, then don't ask for anything
			desired = 0
		
		return desired

	def timeWantToRent(self):
		return random.randint(self.minLen, self.maxLen)		# Randomly choose the rental length within the bounds of my customer type

	def rentTools(self, count):
		self.activeRentalCount += count

	def returnTools(self, count):
		self.activeRentalCount -= count
		assert (self.activeRentalCount>=0)	# screen for accounting errors

class CasualCustomer(Customer):
	def __init__(self):
		Customer.__init__(self)
		# Casual customers rent one or two tools for one or two nights. 
		self.minLen = 1
		self.maxLen = 2
		self.minQty = 1
		self.maxQty = 2
		self.typeName = "Casual customer"


class RegularCustomer(Customer):
	def __init__(self):
		Customer.__init__(self)
		# Regular customers will rent one to three tools each time they visit for 3 to 5 nights.
		self.minLen = 3
		self.maxLen = 5
		self.minQty = 1
		self.maxQty = 3
		self.typeName = "Regular customer"

class BusinessCustomer(Customer):
	def __init__(self):
		Customer.__init__(self)
		# Business customers always rent three tools for seven nights. 
		self.minLen = 7
		self.maxLen = 7
		self.minQty = 3
		self.maxQty = 3
		self.typeName = "Business customer"

def randomCustomer():
	# a generator function to instantiate a random type of customer
	availTypes = [CasualCustomer, RegularCustomer, BusinessCustomer]
	return availTypes[random.randrange(0, len(availTypes))]()

if __name__ == "__main__":
	# Test code - only run if this script is executed in isolation.
	print("Testing Customer.py")

	t = []
	for i in range(20):
		t.append( randomCustomer() )

	for c in t:
		print(c)
