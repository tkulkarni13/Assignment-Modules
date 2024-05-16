# Task 1: Contact List Manager

import contacts_manager

contacts = dict() # Dictionary to store all contacts

print("Welcome to the Contact List Manager!") # Greet the user
contacts_manager.printInstructions()

while True: # Loop until the user decided to exit
    try: # Ensure the user inputs a number
        user_input_num = int(input("Please enter a number from the options above: "))
    except ValueError: # Notify user if they don't input a number
        print("Please enter a valid number.")
    else:
        if (user_input_num < 0 or user_input_num > 4): # Notify user if the pick a number out of range
            print("Please enter a number from 1-4.")

        elif (user_input_num == 1): # Add a new contact if '1' is selected
            number = input("Please enter the phone number of the contact you'd like to add: ") # Take input for phone number from user
            name = input("Please enter the name of the contact you'd like to add: ") # Take input for name from user
            contacts_manager.addContact(contacts, number, name) # Add contact to dictionary
            contacts_manager.printInstructions()
        
        elif (user_input_num == 2): # Delete a contact if '2' is selected
            number = input("Please enter the number of the contact you'd like to delete: ") # Take input for phone number from user
            contacts_manager.deleteContact(contacts, number) # Delete contact from dictionary based on phone number
            contacts_manager.printInstructions()
        
        elif (user_input_num == 3): # Display all contacts if '3' is selected
            contacts_manager.displayContacts(contacts) # Call function to print all contacts
            contacts_manager.printInstructions()
        
        elif (user_input_num == 4): # Exit program if '4' is selected
            break