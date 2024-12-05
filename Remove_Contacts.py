from Save_File import save_all_contact
def remove_contact(contact_list):
    if not contact_list:
        print("The Contact List is empty.")
        return contact_list
    
    removenumber = int(input("Enter Phone Number you want to remove: "))
    for contact in contact_list:
        if int(contact['Phone Number']) == removenumber:
            contact_list.remove(contact)
            save_all_contact(contact_list)
            print(f"Contact {removenumber} has been removed.")
            return contact_list

    print("No contact found.")
    return contact_list