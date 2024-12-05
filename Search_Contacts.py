def search_contact(contact_list):
    if not contact_list:
        print("The Contact List is empty.")
        return contact_list
    
    searchnumber = int(input("Enter your Phone Number you want to search: "))
    for contact in contact_list:
        if int(contact['Phone Number']) == searchnumber:
            print(f"Contact Details: Name: {contact['Name']} | Email: {contact['Email']} | Phone Number: {contact['Phone Number']} | Address: {contact['Address']}")
            print()
            return contact_list

    print("No book found with the given ISBN.")
    return contact_list