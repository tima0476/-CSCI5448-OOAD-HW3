#!/usr/bin/env python3
#
# Hardware Store Simulation in Python 3
# a solution for Homework 3 of CSCI 5448, Object Oriented Analysis and Design
# University of Colorado, Boulder
#
# written by Timothy Mason (solo project)
#
# file: store.py
# description: Definition and implementation of the Store class.  This class is responsible for implementing the logic of the
# hardware rental store.  It tracks tool inventory, customers, rentals, and money.
#
import random
import rental
import tool
import customer

class Store:
	def __init__(self):
		# Initialize tool inventory - I decided to do this the simple way with
		# attributes.  Creating a specialized subclass for each tool type
		# seems like overkill.  I debated where to put this initialization,
		# but finally decided that it makes sense for a store to choose /
		# create its' own tool inventory and set the prices.  This is not
		# randomized due to the wording of the specification:

		# "store has a catalog of 20 different tools to rent, spread across 5
		# different categories (Painting, Concrete, Plumbing, Woodwork,
		# Yardwork). Each tool has a unique name (e.g. “Paint Tool 1”) and
		# belongs to a specific category; the price per day to rent a tool
		# varies by category.  You may decide on the pricing of the rental
		# categories."
		self.inventory = []
		self.inventory.append( tool.Tool( "Painting Tool 1",    "Painting",    5.95 ))
		self.inventory.append( tool.Tool( "Painting Tool 2",    "Painting",    5.95 ))
		self.inventory.append( tool.Tool( "Painting Tool 3",    "Painting",    5.95 ))
		self.inventory.append( tool.Tool( "Painting Tool 4",    "Painting",    5.95 ))
		self.inventory.append( tool.Tool( "Concrete Tool 1",    "Concrete",    8.95 ))
		self.inventory.append( tool.Tool( "Concrete Tool 2",    "Concrete",    8.95 ))
		self.inventory.append( tool.Tool( "Concrete Tool 3",    "Concrete",    8.95 ))
		self.inventory.append( tool.Tool( "Concrete Tool 4",    "Concrete",    8.95 ))
		self.inventory.append( tool.Tool( "Plumbing Tool 1",    "Plumbing",    6.95 ))
		self.inventory.append( tool.Tool( "Plumbing Tool 2",    "Plumbing",    6.95 ))
		self.inventory.append( tool.Tool( "Plumbing Tool 3",    "Plumbing",    6.95 ))
		self.inventory.append( tool.Tool( "Plumbing Tool 4",    "Plumbing",    6.95 ))
		self.inventory.append( tool.Tool( "Woodworking Tool 1", "Woodworking", 3.95 ))
		self.inventory.append( tool.Tool( "Woodworking Tool 2", "Woodworking", 3.95 ))
		self.inventory.append( tool.Tool( "Woodworking Tool 3", "Woodworking", 3.95 ))
		self.inventory.append( tool.Tool( "Woodworking Tool 4", "Woodworking", 3.95 ))
		self.inventory.append( tool.Tool( "Yardwork Tool 1",    "Yardwork",    9.95 ))
		self.inventory.append( tool.Tool( "Yardwork Tool 2",    "Yardwork",    9.95 ))
		self.inventory.append( tool.Tool( "Yardwork Tool 3",    "Yardwork",    9.95 ))
		self.inventory.append( tool.Tool( "Yardwork Tool 4",    "Yardwork",    9.95 ))

		# Initialize customer base - "This store has 10 customers".  In my
		# world, customers choose their own name and customer type
		self.customer = [customer.randomCustomer() for _ in range(10)]

		# Initialize accounting
		self.activeRentals = []
		self.archivedRentals = []
		self.money = 0.0	# and no money in the till

	def getCustomerWants(self):
		return [c.qtyWantToRent() for c in self.customer]

	def getAvailToolCount(self):
		return len(self.inventory)

	def RentToolsByCustNum(self, custNum, count, startDay):
		# Rent tools to a customer
		# cnum = The number of the customer who wants to rent a tool (index into the customer list)
		# count = The number of tools the customer wants to rent
		
		c = self.customer[custNum]		# retrieve a reference to the customer
		dur = c.timeWantToRent()		# ask the customer how long they want to rent the tool

		# Pull the desired number of tools out of inventory and rent them
		tools = [self.inventory.pop(random.randint(0,len(self.inventory)-1)) for _ in range(count)]	# Pull random tools from available inventory
				
		# collect the rental fee
		total = 0.0
		for t in tools:
			total += t.price * dur
		self.money += total

		# Log the transaction
		c.rentTools(count)									# let the customer know they successfully rented from us
		rec = rental.Rental(tools, c, startDay, dur, total)	# create a rental record
		self.activeRentals.append(rec)						# and add it to the active list

		print(" ",rec)
		
	def morningReturns(self, currentDay):
		# iterate through the active rentals, looking for expired rentals to
		# call back
		returnsList = []
		for i in range(len(self.activeRentals)):
			a = self.activeRentals[i]
			if a.expired(currentDay):
				# mark the tool to be returned
				returnsList.append(i)
		
		# process returns in reverse order so the list removal doesn't mess up
		# the list indexing
		if len(returnsList)==0:
			print("  no returns today.")

		returnsList.reverse()
		for i in returnsList:
			rec = self.activeRentals.pop(i)

			# inform the customer holding the tools that they're returning them
			rec.customer.returnTools(rec.toolCount())

			# return all of the tools in the rental record to active inventory
			for t in rec.toolsRented:
				self.inventory.append(t)
				print("  {} returned {}".format(rec.customer, t.name))
				# Note: There are now multiple references to a single tool
				# because the tool object reference was not removed from the
				# rental record after the tool was returned to inventory.
				# This is ok because the record object containing the
				# duplicate tools will be moved to the archive list, and we
				# know that the tools in the archive list are for reference
				# only.

			# store the rental record in the archive
			self.archivedRentals.append(rec)

	def getProfits(self):
		return self.money	

	def printInventory(self):
		if self.getAvailToolCount() == 0:
			print("    <no tools in inventory>")
		else:
			for t in self.inventory:
				print("   ",t.name)			

	def printRecords(self, recordList):
		for r in recordList:
			print("   ",r)

	def printActive(self):
		self.printRecords(self.activeRentals)

	def printArchive(self):
		self.printRecords(self.archivedRentals)

if __name__ == "__main__":
	# Test code - only run if executed at the top level
	print("Top level Store.py")

	s = Store()
	for t in s.inventory:
		print(t)
	for c in s.customer:
		print(c)
	print(s.getCustomerWants())