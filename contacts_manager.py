def printInstructions():
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Display all contacts")
    print("4. Quit")

# Function to add a new contact
def addContact(contacts, number, name):
    if number in contacts.keys(): # Check if number is already saved
        print("This number is already saved in your contacts.")
    else:
        contacts[number] = name # Add new contact to dictionary
        print(f"{name} has been added to your contacts.") # Notify user they have added a new contact

# Function to delete a contact
def deleteContact(contacts, number):
    if number not in contacts.keys(): # Check that the number exists in contacts to be deleted
        print("This number is not saved in your contacts.")
    else:
        deleted_contact = contacts.pop(number) # Delete specified number and store in a variable
        print(f"{deleted_contact} has been removed from your contacts.") # Notify user of which contact has been removed

# Function to display all contacts saved
def displayContacts(contacts):
    if (len(contacts) == 0): # Notify user if they have not saved any contacts
        print("You have no saved contacts.")
    else:
        for number, name in contacts.items(): # Loop through all contacts
            print(f"Phone Number: {number} - Name: {name}") # Print phone number and name for each contact