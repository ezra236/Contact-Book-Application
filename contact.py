class Book:

    def __init__(self):
        self.contacts = {
            "David": {
                "email": "davidkaithia@gmail.com",
                "phone": "0799963300",
                "category": "king"
            },

            "Monica": {
                "email": "monicakaithia@gmail.com",
                "phone": "0725963300",
                "category": "queen"
            },

            "Ezra": {
                "email": "ezrakaithia@gmail.com",
                "phone": "0704963300",
                "category": "prince"
            }
        }


    def add(self):

        print("ADD CONTACTS")

        contact1 = input("ENTER THE NEW CONTACT NAME: ")
        contact_email = input("ENTER THE NEW CONTACT EMAIL: ")
        contact_phone = input("ENTER THE NEW CONTACT PHONE: ")
        contact_category = input("ENTER THE NEW CONTACT CATEGORY: ")

        self.contacts[contact1] = {
            "email": contact_email,
            "phone": contact_phone,
            "category": contact_category
        }

        print("CONTACT ADDED SUCCESFULLY!")
    

    def remove(self):
         
        print("REMOVE CONTACTS")

        contactB = input("ENTER THE NAME OF THE CONTACT TO BE REMOVED: ")
        removed_contact = self.contacts.pop(contactB, None)

        print(f"THE REMOVED CONTACT: {removed_contact}")

    
    def prints(self):
        
        print("THE SAVED CONTACTS")

        for name, info in self.contacts.items():
            print(f"Contact Name: {name}")
            for key, value in info.items():
                print(f"  {key}: {value}")


    def change(self):

        print("EDIT CONTACT")

        contactC = input("ENTER THE NAME OF THE CONTACT TO MODIFY: ")

        choice = input("WHAT NEEDS TO BE CHANGED: ")

        if choice.lower() == "email":
            change_email = input("ENTER THE NEW EMAIL: ")
            self.contacts[contactC]["email"] = change_email

        elif choice.lower() == "phone":
            change_phone = input("ENTER THE NEW PHONE: ")
            self.contacts[contactC]["phone"] = change_phone

        elif choice.lower() == "category":
            change_category = input("ENTER THE NEW CATEGORY: ")
            self.contacts[contactC]["category"] = change_category

        print("CONTACT CHANGED SUCCESFULLY!")

    
    def search_contact(self):
        search_str = input("Enter search string: ").lower()
        print("SEARCH RESULTS:")
        found = False
        for name, info in self.contacts.items():
            if name.lower().startswith(search_str):
                found = True
                print(f"Contact Name: {name}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
        if not found:
            print("No contacts found that start with that string.")



obj = Book()

print("CONTACT BOOK APPLICATION")

while True:
    print("\n1. ADD CONTACT")
    print("2. REMOVE CONTACT")
    print("3. EDIT CONTACT")
    print("4. VIEW CONTACTS")
    print("5. SEARCH CONTACT")
    print("6. EXIT")
    
    option = input("ENTER THE OPTION: ")

    if option == "1":
        obj.add()
    elif option == "2":
        obj.remove()
    elif option == "3":
        obj.change()
    elif option == "4":
        obj.prints()
    elif option == "5":
        obj.search_contact()
    elif option == "6":
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please try again.")






