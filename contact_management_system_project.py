def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")
contacts = {
    "unique_id": {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john@example.com",
        "address": "123 Main St",
        "notes": "Friend from college"
    }
}
def add_contact():
    unique_id = input("Enter a unique identifier (email/phone): ")
    if unique_id in contacts:
        print("A contact with this identifier already exists.")
        return
    
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    notes = input("Enter additional notes: ")
    
    contacts[unique_id] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "notes": notes
    }
    print("Contact added successfully!")
def edit_contact():
    unique_id = input("Enter the unique identifier of the contact to edit: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    
    print("Enter new details (leave blank to keep current information):")
    name = input(f"Name ({contacts[unique_id]['name']}): ") or contacts[unique_id]['name']
    phone = input(f"Phone number ({contacts[unique_id]['phone']}): ") or contacts[unique_id]['phone']
    email = input(f"Email address ({contacts[unique_id]['email']}): ") or contacts[unique_id]['email']
    address = input(f"Address ({contacts[unique_id]['address']}): ") or contacts[unique_id]['address']
    notes = input(f"Additional notes ({contacts[unique_id]['notes']}): ") or contacts[unique_id]['notes']
    
    contacts[unique_id] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "notes": notes
    }
    print("Contact updated successfully!")
def delete_contact():
    unique_id = input("Enter the unique identifier of the contact to delete: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    
    del contacts[unique_id]
    print("Contact deleted successfully!")
def search_contact():
    unique_id = input("Enter the unique identifier of the contact to search: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    
    contact = contacts[unique_id]
    print("Contact details:")
    for key, value in contact.items():
        print(f"{key}: {value}")
def display_all_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    for unique_id, details in contacts.items():
        print(f"ID: {unique_id}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()
def export_contacts(filename):
    with open(filename, 'w') as file:
        for unique_id, details in contacts.items():
            file.write(f"{unique_id}\n")
            for key, value in details.items():
                file.write(f"{key}:{value}\n")
            file.write("\n")
    print(f"Contacts exported to {filename}")
def import_contacts(filename):
    with open(filename, 'r') as file:
        current_id = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if ':' not in line:
                current_id = line
                contacts[current_id] = {}
            else:
                key, value = line.split(':', 1)
                contacts[current_id][key] = value
    print(f"Contacts imported from {filename}")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            filename = input("Enter filename to export: ")
            export_contacts(filename)
        elif choice == '7':
            filename = input("Enter filename to import: ")
            import_contacts(filename)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
