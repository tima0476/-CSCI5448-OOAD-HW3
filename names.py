#!/usr/bin/env python3
#
# Hardware Store Simulation in Python 3
# a solution for Homework 3 of CSCI 5448, Object Oriented Analysis and Design
# University of Colorado, Boulder
#
# written by Timothy Mason (solo project)
#
# file: names.py
# description: Contains a utility function GenerateName() to return a string with a randomly generated
# "American" first & last name.  Sources for the name lists are credited in the code comments prior to
# the list contents.

import random

def GenerateName():
	# from "Top Names Over the Last 100 Years" - https://www.ssa.gov/oact/babynames/decades/century.html
	commonFirstNames = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer',
	'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara', 'Richard',
	'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Margaret',
	'Christopher', 'Karen', 'Daniel', 'Nancy', 'Matthew', 'Lisa', 'Anthony',
	'Betty', 'Donald', 'Dorothy', 'Mark', 'Sandra', 'Paul', 'Ashley', 'Steven',
	'Kimberly', 'Andrew', 'Donna', 'Kenneth', 'Emily', 'George', 'Carol',
	'Joshua', 'Michelle', 'Kevin', 'Amanda', 'Brian', 'Melissa', 'Edward',
	'Deborah', 'Ronald', 'Stephanie', 'Timothy', 'Rebecca', 'Jason', 'Laura',
	'Jeffrey', 'Helen', 'Ryan', 'Sharon', 'Jacob', 'Cynthia', 'Gary', 'Kathleen',
	'Nicholas', 'Amy', 'Eric', 'Shirley', 'Stephen', 'Angela', 'Jonathan', 'Anna',
	'Larry', 'Ruth', 'Justin', 'Brenda', 'Scott', 'Pamela', 'Brandon', 'Nicole',
	'Frank', 'Katherine', 'Benjamin', 'Samantha', 'Gregory', 'Christine',
	'Raymond', 'Catherine', 'Samuel', 'Virginia', 'Patrick', 'Debra', 'Alexander',
	'Rachel', 'Jack', 'Janet', 'Dennis', 'Emma', 'Jerry', 'Carolyn', 'Tyler',
	'Maria', 'Aaron', 'Heather', 'Henry', 'Diane', 'Jose', 'Julie', 'Douglas',
	'Joyce', 'Peter', 'Evelyn', 'Adam', 'Joan', 'Nathan', 'Victoria', 'Zachary',
	'Kelly', 'Walter', 'Christina', 'Kyle', 'Lauren', 'Harold', 'Frances', 'Carl',
	'Martha', 'Jeremy', 'Judith', 'Gerald', 'Cheryl', 'Keith', 'Megan', 'Roger',
	'Andrea', 'Arthur', 'Olivia', 'Terry', 'Ann', 'Lawrence', 'Jean', 'Sean',
	'Alice', 'Christian', 'Jacqueline', 'Ethan', 'Hannah', 'Austin', 'Doris',
	'Joe', 'Kathryn', 'Albert', 'Gloria', 'Jesse', 'Teresa', 'Willie', 'Sara',
	'Billy', 'Janice', 'Bryan', 'Marie', 'Bruce', 'Julia', 'Noah', 'Grace',
	'Jordan', 'Judy', 'Dylan', 'Theresa', 'Ralph', 'Madison', 'Roy', 'Beverly',
	'Alan', 'Denise', 'Wayne', 'Marilyn', 'Eugene', 'Amber', 'Juan', 'Danielle',
	'Gabriel', 'Rose', 'Louis', 'Brittany', 'Russell', 'Diana', 'Randy',
	'Abigail', 'Vincent', 'Natalie', 'Philip', 'Jane', 'Logan', 'Lori', 'Bobby',
	'Alexis', 'Harry', 'Tiffany', 'Johnny', 'Kayla']

	# "100 Most Popular American Last Names" - https://www.rong-chang.com/namesdict/100_last_names.htm common

	commonLastNames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis',
	'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson',
	'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
	'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young',
	'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams',
	'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts',
	'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins',
	'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell',
	'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward',
	'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly',
	'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson',
	'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes',
	'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant',
	'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes']

	return commonFirstNames[random.randrange(0,len(commonFirstNames))] + " " + commonLastNames[random.randrange(0,len(commonLastNames))]

if __name__ == "__main__":
	# Test code
	print("Executing names.py from top level.  Here are 20 random names:")
	for i in range(20):
		print("{:>2}: {}".format(i+1, GenerateName()))
