def main():
    contacts = {}

    def add_contact():
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        contacts[name.lower()] = {"name": name, "phone": phone, "email": email, "address": address}
        print(f"Contact '{name}' added successfully.")

    def view_contacts():
        if not contacts:
            print("Contact book is empty.")
        else:
            print("\n--- All Contacts ---")
            for contact_name, details in contacts.items():
                print(f"Name: {details['name']}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("-" * 20)
    
    def search_contact():
        search_term = input("Enter name or phone number to search: ").lower()
        found_contacts = []
        for name, details in contacts.items():
            if search_term in name or search_term in details['phone']:
                found_contacts.append(details)
        
        if not found_contacts:
            print("No contacts found.")
        else:
            print("\n--- Search Results ---")
            for details in found_contacts:
                print(f"Name: {details['name']}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("-" * 20)

    def update_contact():
        name_to_update = input("Enter the name of the contact to update: ").lower()
        if name_to_update in contacts:
            print(f"Current details for '{contacts[name_to_update]['name']}':")
            print(f"1. Phone: {contacts[name_to_update]['phone']}")
            print(f"2. Email: {contacts[name_to_update]['email']}")
            print(f"3. Address: {contacts[name_to_update]['address']}")
            
            choice = input("Enter the number of the field to update (1-3): ")
            
            if choice == "1":
                new_phone = input("Enter new phone number: ")
                contacts[name_to_update]['phone'] = new_phone
                print("Phone number updated.")
            elif choice == "2":
                new_email = input("Enter new email address: ")
                contacts[name_to_update]['email'] = new_email
                print("Email address updated.")
            elif choice == "3":
                new_address = input("Enter new address: ")
                contacts[name_to_update]['address'] = new_address
                print("Address updated.")
            else:
                print("Invalid choice.")
        else:
            print("Contact not found.")

    def delete_contact():
        name_to_delete = input("Enter the name of the contact to delete: ").lower()
        if name_to_delete in contacts:
            del contacts[name_to_delete]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()