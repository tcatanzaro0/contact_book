contactList = {}

def addContact():
	name = input("Please enter the contact's name: ")
	phone = input("Please enter the contact's phone number: ")
	email = input("Please enter the contact's email: ")
	contactList.setdefault(name, (phone, email))
	print(contactList)
	
def contactEmail():
	name = input("Enter the name of the contact: ")
	print("The contact's email is " + contactList[name][1])
	
def contactPhone():
	name = input("Enter the name of the contact: ")
	print("The contact's email is " + contactList[name][0])
	

addContact()
contactEmail()
contactPhone()
