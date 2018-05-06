import pprint
pp = pprint.PrettyPrinter(indent=4, width=1)

contactList = {}

def contactMenu():
	print("Hello and welcome to your contact book! \n Please choose your option.")
	print("1. Add new contact")
	print("2. View all contacts")
	print("3. View contact's email")
	print("4. View contact's phone")
	print("5 Delete contact")
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
	#elif choice == 5:
		

def addContact():
	name = input("Please enter the contact's name: ")
	phone = input("Please enter the contact's phone number: ")
	email = input("Please enter the contact's email: ")
	contactList.setdefault(name, (phone, email))
	print("New contact added.")
	print("Name: " + name)
	print("Phone: " + phone)
	print("Email: " + email)
	contactMenu()
	
def viewContacts():
	for key, value in contactList.items():
		print("{}: {}".format(key, value))

def contactEmail():
	name = input("Enter the name of the contact: ")
	print("The contact's email is " + contactList[name][1])
	
def contactPhone():
	name = input("Enter the name of the contact: ")
	print("The contact's email is " + contactList[name][0])
	

contactMenu()


###Sources###
# https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch01s06.html
# https://stackoverflow.com/questions/1380860/add-variables-to-tuple
# https://www.tutorialspoint.com/python/python_tuples.htm
# https://docs.python.org/3/library/pprint.html
# https://stackoverflow.com/questions/40071006/python-2-7-print-a-dictionary-without-brackets-and-quotation-marks
#############
