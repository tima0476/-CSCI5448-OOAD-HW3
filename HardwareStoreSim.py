#!/usr/bin/env python3
#
# Hardware Store Simulation in Python 3
# a solution for Homework 3 of CSCI 5448, Object Oriented Analysis and Design
# University of Colorado, Boulder
#
# written by Timothy Mason (solo project)
#
# name: HardwareStoreSim.py
# description:  This is the main entry point for the Hardware Store
# simulation.  It implements the class HardwareStoreSim, which is responsible
# for keeping track of time, dispatching daily events, and running final
# reports at the end of the sim.  There is also code at the bottom of the file
# to instantiate the HardwareStoreSim and start the execution.
#
import random
import store

class HardwareStoreSim:
	def __init__(self):
		# self.store = store.Store()
		self.store = None
	
	# RunSimulation(days) - Execute the hardware store simulation for the
	# specified number of days. This is the main entry point of the program
	def RunSimulation(self, days):
		# Create the Store
		self.store = store.Store()

		# Iterate through the days of the sim
		for currentDay in range(1,days+1):
			print()
			if currentDay>1:
				print("Morning returns, day {}.".format(currentDay))
				# Tell the store to pull back the returns for the day
				self.store.morningReturns(currentDay)

			c = self.store.getAvailToolCount()
			if c==1:
				desc="tool"
			else:
				desc="tools"
			print("Open for business, day {}.  {} {} available.".format(currentDay, c, desc))

			# The simulation spec very strongly specifies that customers
			# somehow magically never attempt to visit the store if they
			# wouldn't be able to rent any tools.  Therefore, we have to
			# interrogate the customers about there desires in the sim
			# controller, and only send customers to the store if they can get
			# what they want.
			#
			# Get a list of what each customer wants to rent (only the store
			# knows who the customers are, so the store is responsible for
			# calling each customer to record their desires)
			w = self.store.getCustomerWants()

			# As long as the store has sufficient inventory, send customers
			# one at a time starting from a random spot in the list (to give
			# those at the back of the list a better chance)
			first = random.randint(1,len(w))
			noCustom = True
			for i in range(len(w)):
				j = (i+first)%len(w)	# offset start index, and wrap to zero if went past end
				if w[j]>0 and w[j]<=self.store.getAvailToolCount():
					self.store.RentToolsByCustNum(j, w[j], currentDay)
					noCustom = False
			if noCustom:
				print("  no customers today.  :(")
			

		# Print the final reports
		self.PrintReports()

	def PrintReports(self):
		print()
		print("-"*80)
		print()
		print("Final Reports:")
		print()
		c = self.store.getAvailToolCount()
		if c==1:
			toolWord = "tool"
		else:
			toolWord = "tools"
		print("  Inventory: {} {} available to rent:".format(c, toolWord))
		self.store.printInventory()
		print()
		print("  Total profits: ${:0.2f}".format(self.store.getProfits()))
		print()
		print("  Completed rentals:")
		self.store.printArchive()
		print()
		print("  Active rentals:")
		self.store.printActive()


if __name__ == "__main__":
	print("Homework 3 - Hardware Store Simulation")
	print()
	print("Universtiy of Colorado, Boulder")
	print("CSCI 5448, Object Oriented Analysis and Design")
	print()
	print("Timothy Mason (solo project)")
	print()

	sim = HardwareStoreSim()
	sim.RunSimulation(35)	# Simulate 35 days of the simulation
