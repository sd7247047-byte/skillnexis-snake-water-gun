contacts = {}

while True:

    print("\n----- Contact Book -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. show all Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print("contact added successfully!")

    # Search Contact
    elif choice == '2':
        name = input("Enter name to search: ")

        if name in contacts:
            print("phone number:", contacts[name])
        else:
            print("contact not found.")

    # Update Contact
    elif choice == '3':
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone

            print("contact updated successfully!")
        else:
            print("contact not found.")

    # Delete Contact
    elif choice == '4':
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]

            print("contact deleted successfully.")
        else:
            print("contact not found.")

    # Show all Contacts
    elif choice == '5':
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nAll Contacts:")

            for name, phone in contacts.items():
                print(name, ":", phone)

    # Exit
    elif choice == '6':
        print("Thank you for using the Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")