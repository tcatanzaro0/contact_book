import os.path
import csv

#contactList = {}

def contactMenu():
	"""This function presents the user with a list of options then prompts them for input.
	Depending on the user's input it will call the appropriate function.
	If the choice is 6 it writes the current keys/values in contactList to a .csv file."""
	print("1. Add new contact")
	print("2. View all contacts")
	print("3. View contact's email")
	print("4. View contact's phone")
	print("5. Delete contact")
	print("6. Quit")
	print("Please enter the number of your choice: ")
	choice = int(input("> "))
	if choice == 1:
		addContact()
	elif choice == 2:
		viewContacts()
	elif choice == 3:
		contactEmail()
	elif choice == 4:
		contactPhone()
	elif choice == 5:
		deleteContact()
	elif choice == 6:
		w = csv.writer(open("contacts.csv", "w"))
		for key, val in contactList.items():
			w.writerow([key, val])

def addContact():
	"""This function allows the user to create a new contact.
	The user enters the name, phone, and email. 
	The name becomes the dictionary entry's key and the phone and email are a tuple and are the value."""
	print("\033[H\033[J")
	name = input("Please enter the contact's name: ")
	phone = input("Please enter the contact's phone number: ")
	email = input("Please enter the contact's email: ")
	contactList.setdefault(name, (phone, email))
	print("\033[H\033[J")
	print("New contact added.")
	print("Name: " + name)
	print("Phone: " + phone)
	print("Email: " + email)
	print()
	print()
	contactMenu()
	
def viewContacts():
	"""Simply prints all entries in the contactList dictionary.
	The '{}' brackets in the dictionary are removed so it simply looks better."""
	print("\033[H\033[J")
	print("You currently have the following contacts in your contact book: ")
	for key, value in contactList.items():
		print("{}: {}".format(key, value))
	print()
	print()
	contactMenu()

def contactEmail():
	"""Prompts the user for the name of the contact. 
	Then calls and prints the value in the [1] position of the appropriate entry."""
	print("\033[H\033[J")
	name = input("Enter the name of the contact: ")
	print("The contact's email is " + contactList[name][1])
	print()
	print()
	contactMenu()
	
def contactPhone():
	"""Prompts for name of the contact.
	Then calls and prints the value in the [0] position of the appropriate entry."""
	print("\033[H\033[J")
	name = input("Enter the name of the contact: ")
	print("The contact's email is " + contactList[name][0])
	print()
	print()
	contactMenu()
	
def deleteContact():
	"""Prompts the user for the name of the contact.
	Then uses the del fuction to delete the contact entered."""
	print("\033[H\033[J")
	name = input("Please enter the name of the contact to be deleted: ")
	del contactList[name]
	print()
	print()
	contactMenu()

# Checks for the presence of 'contacts.csv' in the CWD. 
# If it is present it writes the rows to the contactList dictionary.
# If it is not present it creates a blank dictionary. 	
if os.path.isfile('contacts.csv') is True:
	reader = csv.reader(open('contacts.csv', 'r'))
	contactList = {}
	for row in reader:
		k, v = row
		contactList[k] = v
if os.path.isfile('contacts.csv') is False:
	contactList = {}

print("Hello and welcome to your contact book! \n Please choose your option.")
contactMenu()


###Sources###
# https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch01s06.html
# https://stackoverflow.com/questions/1380860/add-variables-to-tuple
# https://www.tutorialspoint.com/python/python_tuples.htm
# https://docs.python.org/3/library/pprint.html
# https://stackoverflow.com/questions/40071006/python-2-7-print-a-dictionary-without-brackets-and-quotation-marks
#############
