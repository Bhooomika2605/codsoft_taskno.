contact = {}
print("\t\t Contact Book")
def dis_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key.title(),contact.get(key)))
while True: 
    choice = int(input("Enter your choice \n1. Add new contact \n2. Search contact \n3. Display contact \n4. Edit contact \n5.Delete contact \n6.Exit \n "))
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the contact name to search: ")   
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("404! Name not found in contact book.")
    elif choice==3:
        if not contact:
            print("Sorry, contact book is empty.")
        else:
            dis_contact()
    elif choice==4:
        edit_contact  = input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone = input("Enter the number: ")
            contact[edit_contact]=phone
            print("Contact updated")
            dis_contact()
        else:
            print("404!! Contact not found. ")
    elif choice==5:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ") 
            if confirm == 'y' or confirm =='Y':
                contact.pop(del_contact)
            dis_contact()
        else:
            print("Name is not found in contact book.")
    else:
        break
                